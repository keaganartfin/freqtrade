import talib.abstract as ta
from pandas import DataFrame
from freqtrade.strategy.interface import IStrategy

class ShortTermROIStrategy(IStrategy):
    minimal_roi = {
        "0": 0.02,
        "30": 0.01,
        "60": 0.005,
        "120": 0
    }
    stoploss = -0.10
    timeframe = '5m'
    startup_candle_count = 30

    def informative_pairs(self):
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['sma_short'] = ta.SMA(dataframe, timeperiod=5)
        dataframe['sma_long'] = ta.SMA(dataframe, timeperiod=20)

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe['sma_short'] > dataframe['sma_long']) &
            (dataframe['volume'] > 0),
            'buy'] = 1

        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe['sma_short'] < dataframe['sma_long']) |
            (dataframe['volume'] > 0),
            'sell'] = 1

        return dataframe
