import pandas as pd
from pandas import DataFrame
from typing import Dict, Any

class IchimokuIndicator:
    def __init__(self, conversion_line_period: int = 9, base_line_period: int = 26,
                 leading_span_b_period: int = 52, displacement: int = 26):
        self.conversion_line_period = conversion_line_period
        self.base_line_period = base_line_period
        self.leading_span_b_period = leading_span_b_period
        self.displacement = displacement

    def calculate(self, dataframe: DataFrame) -> DataFrame:
        hl2 = (dataframe['high'] + dataframe['low']) / 2
        conversion_line = hl2.rolling(window=self.conversion_line_period).max() + hl2.rolling(window=self.conversion_line_period).min()
        conversion_line /= 2
        dataframe['tenkan_sen'] = conversion_line

        base_line = hl2.rolling(window=self.base_line_period).max() + hl2.rolling(window=self.base_line_period).min()
        base_line /= 2
        dataframe['kijun_sen'] = base_line

        leading_span_a = (dataframe['tenkan_sen'] + dataframe['kijun_sen']) / 2
        dataframe['senkou_span_a'] = leading_span_a.shift(self.displacement)

        leading_span_b = hl2.rolling(window=self.leading_span_b_period).max() + hl2.rolling(window=self.leading_span_b_period).min()
        leading_span_b /= 2
        dataframe['senkou_span_b'] = leading_span_b.shift(self.displacement)

        dataframe['chikou_span'] = dataframe['close'].shift(-self.displacement)

        return dataframe
