# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy
from typing import Dict, List
from functools import reduce
from pandas import DataFrame
# -------------------------------- 

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
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
        """
        Adds several different TA indicators to the given DataFrame

        Performance Note: For the best performance be frugal on the number of indicators
        you are using. Let uncomment only the indicator you are using in your strategies
        or your hyperopt configuration, otherwise you will waste your memory and CPU usage.
        """

        # Stochastics Slow
        stoch = ta.STOCH(dataframe, fastk_period=14, slowk_period=3, slowd_period=3)
        dataframe['slowk'] = stoch['slowk']
        dataframe['slowd'] = stoch['slowd']
        
        # EMA - Exponential Moving Average
        dataframe['ema50'] = ta.EMA(dataframe, timeperiod=50)
        dataframe['ema100'] = ta.EMA(dataframe, timeperiod=100)

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)

        # Inverse Fisher transform on RSI, values [-1.0, 1.0] (https://goo.gl/2JGGoy)
        rsi = 0.1 * (dataframe['rsi'] - 50)
        dataframe['fisher_rsi'] = (numpy.exp(2 * rsi) - 1) / (numpy.exp(2 * rsi) + 1)

        # Bollinger bands
        bollinger = ta.BBANDS(dataframe, timeperiod=self.bollinger_bands_window, nbdevup=self.bollinger_bands_std, nbdevdn=self.bollinger_bands_std)
        dataframe['bb_lowerband'] = bollinger['lowerband']
        dataframe['bb_middleband'] = bollinger['middleband']
        dataframe['bb_upperband'] = bollinger['upperband']

        # SAR Parabol
        dataframe['sar'] = ta.SAR(dataframe)

        # Hammer: values [0, 100]
        dataframe['CDLHAMMER'] = ta.CDLHAMMER(dataframe)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (
                (dataframe['rsi'] < 30) &
                (dataframe['slowk'] < 20) &
                (dataframe['slowd'] < 20) &
                (dataframe['ema50'] > dataframe['ema100'])&
                (dataframe['bb_lowerband'] > dataframe['close']) &
                (dataframe['CDLHAMMER'] == 100)
            ),
            'enter_long'] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (   
                (dataframe['rsi'] > 70) &
                (dataframe['slowk'] > 80) &
                (dataframe['slowd'] > 80) &
                (dataframe['ema50'] < dataframe['ema100'])
            ) | (
                (dataframe['sar'] > dataframe['close']) &
                (dataframe['fisher_rsi'] > 0.3)
            ) | (
                (dataframe['close'] > dataframe['bb_upperband'])
            ),
            'exit_long'] = 1
        return dataframe
