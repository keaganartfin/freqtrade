# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy
from typing import Dict, List
from functools import reduce
from pandas import DataFrame
# -------------------------------- 

import talib.abstract as ta
from finta import TA
import freqtrade.vendor.qtpylib.indicators as qtpylib
from concurrent.futures import ThreadPoolExecutor
import functools
from indicators import *
import numpy as np # noqa

def cross_over_up(df, col1, col2):
    return (df[col1] > df[col2]) & (df[col1].shift() <= df[col2].shift())

def cross_over_down(df, col1, col2):
    return (df[col1] < df[col2]) & (df[col1].shift() >= df[col2].shift())


def supertrend(dataframe, period=7, multiplier=3):
    hl2 = (dataframe['high'] + dataframe['low']) / 2
    atr = ta.ATR(dataframe, timeperiod=period)
    upper_band = hl2 + (multiplier * atr)
    lower_band = hl2 - (multiplier * atr)

    dataframe['supertrend_upper'] = upper_band
    dataframe['supertrend_lower'] = lower_band
    dataframe['in_uptrend'] = True

    uptrend_cross = cross_over_up(dataframe, 'close', 'supertrend_upper')
    downtrend_cross = cross_over_down(dataframe, 'close', 'supertrend_lower')
    dataframe.loc[uptrend_cross, 'in_uptrend'] = True
    dataframe.loc[downtrend_cross, 'in_uptrend'] = False
    dataframe['in_uptrend'].ffill(inplace=True)

    dataframe['supertrend_lower'] = np.where((dataframe['in_uptrend']) & (dataframe['supertrend_lower'] < dataframe['supertrend_lower'].shift()), dataframe['supertrend_lower'].shift(), dataframe['supertrend_lower'])
    dataframe['supertrend_upper'] = np.where((~dataframe['in_uptrend']) & (dataframe['supertrend_upper'] > dataframe['supertrend_upper'].shift()), dataframe['supertrend_upper'].shift(), dataframe['supertrend_upper'])

    dataframe['supertrend'] = np.where(dataframe['in_uptrend'], dataframe['supertrend_lower'], dataframe['supertrend_upper'])
    dataframe.drop(['supertrend_upper', 'supertrend_lower', 'in_uptrend'], axis=1, inplace=True)

    return dataframe

# This class is a sample. Feel free to customize it.
class CustomStrategy(IStrategy):
    """
    Strategy 002
    author@: Gerald Lonlas
    github@: https://github.com/freqtrade/freqtrade-strategies

    How to use it?
    > python3 ./freqtrade/main.py -s Strategy002
    """

    INTERFACE_VERSION: int = 3
    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi"
    minimal_roi = {
        "60":  0.01,
        "30":  0.03,
        "20":  0.04,
        "0":  0.05
    }

    # Optimal stoploss designed for the strategy
    # This attribute will be overridden if the config file contains "stoploss"
    stoploss = -0.10

    # Optimal timeframe for the strategy
    timeframe = '5m'

    # trailing stoploss
    trailing_stop = False
    trailing_stop_positive = 0.01
    trailing_stop_positive_offset = 0.02

    # run "populate_indicators" only for new candle
    process_only_new_candles = False

    # Experimental settings (configuration will overide these if set)
    use_exit_signal = True
    exit_profit_only = True
    ignore_roi_if_entry_signal = False

    # Optional order type mapping
    order_types = {
        'entry': 'limit',
        'exit': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }
    # Add the Bollinger Bands parameters
    bollinger_bands_std = 2.0
    bollinger_bands_window = 20

    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        These pair/interval combinations are non-tradeable, unless they are part
        of the whitelist as well.
        For more information, please consult the documentation
        :return: List of tuples in the format (pair, interval)
            Sample: return [("ETH/USDT", "5m"),
                            ("BTC/USDT", "15m"),
                            ]
        """
        return []
    
    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Bollinger Bands
        bollinger = ta.BBANDS(dataframe, timeperiod=20)
        dataframe['bb_lowerband'] = bollinger['lowerband']
        dataframe['bb_middleband'] = bollinger['middleband']
        dataframe['bb_upperband'] = bollinger['upperband']

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe)

        # Moving Averages
        dataframe['ema_short'] = ta.EMA(dataframe, timeperiod=5)
        dataframe['ema_long'] = ta.EMA(dataframe, timeperiod=21)

        # MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']

        # ADX
        dataframe['adx'] = ta.ADX(dataframe)

        # Parabolic SAR
        dataframe['sar'] = ta.SAR(dataframe)

        # Ichimoku Cloud
        ichimoku = IchimokuIndicator()
        dataframe = ichimoku.calculate(dataframe)
        
        # Stochastic Oscillator
        stoch = ta.STOCH(dataframe)
        dataframe['slowk'] = stoch['slowk']
        dataframe['slowd'] = stoch['slowd']

        # Supertrend
        dataframe = supertrend(dataframe)

        return dataframe
    
    

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                # Bollinger Bands & RSI
                (dataframe['close'] < dataframe['bb_lowerband']) |
                (dataframe['rsi'] < 30) &
    
                # Moving Averages & MACD
                ((dataframe['ema_short'] > dataframe['ema_long']) |
                (dataframe['macd'] > dataframe['macdsignal'])) &
    
                # ADX & Parabolic SAR
                (dataframe['adx'] > 25) &
                (dataframe['close'] > dataframe['sar']) &
    
                # Ichimoku Cloud
                (dataframe['close'] > dataframe['senkou_span_a']) &
                (dataframe['close'] > dataframe['senkou_span_b']) &
    
                # Stochastic Oscillator
                (dataframe['slowk'] < 20) &
                (dataframe['slowd'] < 20) &
    
                # Supertrend
                (dataframe['close'] > dataframe['supertrend'])
            ),
            'buy'] = 1
    
        return dataframe
    
    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                # Bollinger Bands & RSI
                (dataframe['close'] > dataframe['bb_upperband']) |
                (dataframe['rsi'] > 70) &
    
                # Moving Averages & MACD
                ((dataframe['ema_short'] < dataframe['ema_long']) |
                (dataframe['macd'] < dataframe['macdsignal'])) &
    
                # ADX & Parabolic SAR
                (dataframe['adx'] > 25) &
                (dataframe['close'] < dataframe['sar']) &
    
                # Ichimoku Cloud
                (dataframe['close'] < dataframe['senkou_span_a']) &
                (dataframe['close'] < dataframe['senkou_span_b']) &
    
                # Stochastic Oscillator
                (dataframe['slowk'] > 80) &
                (dataframe['slowd'] > 80) &
    
                # Supertrend
                (dataframe['close'] < dataframe['supertrend'])
            ),
            'sell'] = 1
    
        return dataframe
