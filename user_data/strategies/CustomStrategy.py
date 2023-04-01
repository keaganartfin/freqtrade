# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy
from typing import Dict, List
from functools import reduce
from pandas import DataFrame
# -------------------------------- 

import talib.abstract as ta
from finta import TA
import freqtrade.vendor.qtpylib.indicators as qtpylib
from indicators.IchimokuIndicator import IchimokuIndicator
import numpy # noqa


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
        dataframe['supertrend'] = ta.SUPERTREND(dataframe)

        return dataframe


    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                # Bollinger Bands
                (dataframe['close'] < dataframe['bb_lowerband']) &

                # RSI
                (dataframe['rsi'] < 30) &

                # Moving Averages
                (dataframe['ema_short'] > dataframe['ema_long']) &

                # MACD
                (dataframe['macd'] > dataframe['macdsignal']) &

                # ADX
                (dataframe['adx'] > 25) &

                # Parabolic SAR
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
                # Bollinger Bands
                (dataframe['close'] > dataframe['bb_upperband']) &

                # RSI
                (dataframe['rsi'] > 70) &

                # Moving Averages
                (dataframe['ema_short'] < dataframe['ema_long']) &

                # MACD
                (dataframe['macd'] < dataframe['macdsignal']) &

                # ADX
                (dataframe['adx'] > 25) &

                # Parabolic SAR
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

