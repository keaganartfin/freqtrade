/Bandtastic.py
/BreakEven.py
/CustomStoplossWithPSAR.py
/Diamond.py
/FixedRiskRewardLoss.py
/GodStra.py
/Heracles.py
/HourBasedStrategy.py
/InformativeSample.py
/MultiMa.py
/PatternRecognition.py
/PowerTower.py
/Strategy001_custom_exit.py
/Supertrend.py
/SwingHighToSky.py
/UniversalMACD.py
/berlinguyinca/ADXMomentum.py
/berlinguyinca/ASDTSRockwellTrading.py
/berlinguyinca/AdxSmas.py
/berlinguyinca/AverageStrategy.py
/berlinguyinca/AwesomeMacd.py
/berlinguyinca/BbandRsi.py
/berlinguyinca/BinHV27.py
/berlinguyinca/BinHV45.py
/berlinguyinca/CCIStrategy.py
/berlinguyinca/CMCWinner.py
/berlinguyinca/ClucMay72018.py
/berlinguyinca/CofiBitStrategy.py
/berlinguyinca/CombinedBinHAndCluc.py
/berlinguyinca/DoesNothingStrategy.py
/berlinguyinca/EMASkipPump.py
/berlinguyinca/Freqtrade_backtest_validation_freqtrade1.py
/berlinguyinca/Low_BB.py
/berlinguyinca/MACDStrategy.py
/berlinguyinca/MACDStrategy_crossed.py
/berlinguyinca/MultiRSI.py
/berlinguyinca/Quickie.py
/berlinguyinca/ReinforcedAverageStrategy.py
/berlinguyinca/ReinforcedQuickie.py
/berlinguyinca/ReinforcedSmoothScalp.py
/berlinguyinca/Scalp.py
/berlinguyinca/Simple.py
/berlinguyinca/SmoothOperator.py
/berlinguyinca/SmoothScalp.py
/berlinguyinca/TDSequentialStrategy.py
/berlinguyinca/TechnicalExampleStrategy.py
/futures/FAdxSmaStrategy.py
/futures/FOttStrategy.py
/futures/FReinforcedStrategy.py
/futures/FSampleStrategy.py
/futures/FSupertrendStrategy.py
/futures/Readme.md
/futures/TrendFollowingStrategy.py
/futures/VolatilitySystem.py
/hlhb.py
/lookahead_bias/DevilStra.py
/lookahead_bias/GodStraNew.py
/lookahead_bias/Zeus.py
/lookahead_bias/readme.md
/lookahead_bias/wtc.py
/mabStra.py
/multi_tf.py
/short_term_roi_strategy.py



Bandtastic.py: This strategy utilizes Bollinger Bands, which are a powerful tool to identify overbought and oversold conditions. This can be useful in identifying optimal entry and exit points for trades.

Supertrend.py: Supertrend is a trend-following indicator that combines moving averages and the Average True Range (ATR) to provide signals for trend direction and possible trend reversals. This indicator can help improve trade entry and exit timing in trending markets.

UniversalMACD.py: This strategy employs the Moving Average Convergence Divergence (MACD) indicator, which can provide insights into the momentum and trend of the market. Combining MACD with other indicators can help enhance the accuracy of your strategy.

Heracles.py: Heracles strategy is based on several indicators such as RSI, EMA, and Stochastic. These indicators can be used individually or combined to generate buy/sell signals in various market conditions, providing a versatile approach to market analysis.

MultiMa.py: As the name suggests, this strategy combines multiple moving averages with different timeframes to generate buy/sell signals. Using multiple moving averages can help identify trends and crossovers, which may prove beneficial for your custom strategy.

berlinguyinca/AdxSmas.py: This strategy combines the ADX (Average Directional Index) and SMAs (Simple Moving Averages) to identify trends and potential trade entries. The ADX is a useful tool for measuring the strength of a trend, while SMAs can help identify trend direction and crossovers.

berlinguyinca/CCIStrategy.py: The Commodity Channel Index (CCI) is an oscillator that measures the deviation of an asset's price from its historical average. The CCI can help identify overbought and oversold conditions and could be combined with other indicators to create a more robust strategy.










================== SUMMARY METRICS ==================
| Metric                      | Value               |
|-----------------------------+---------------------|
| Backtesting from            | 2021-01-01 00:00:00 |
| Backtesting to              | 2023-03-31 20:30:00 |
| Max open trades             | 10                  |
|                             |                     |
| Total/Daily Avg Trades      | 4008 / 4.89         |
| Starting balance            | 1000 USDT           |
| Final balance               | 252.9 USDT          |
| Absolute profit             | -747.1 USDT         |
| Total profit %              | -74.71%             |
| CAGR %                      | -45.81%             |
| Sortino                     | -21.43              |
| Sharpe                      | -7.76               |
| Calmar                      | -2.27               |
| Profit factor               | 0.60                |
| Expectancy                  | -0.02               |
| Trades per day              | 4.89                |
| Avg. daily profit %         | -0.09%              |
| Avg. stake amount           | 99.998 USDT         |
| Total trade volume          | 400792.868 USDT     |
|                             |                     |
| Best Pair                   | AXS/USDT 13.95%     |
| Worst Pair                  | BAL/USDT -323.04%   |
| Best trade                  | REQ/USDT 5.00%      |
| Worst trade                 | BAL/USDT -10.70%    |
| Best day                    | 27.679 USDT         |
| Worst day                   | -40.752 USDT        |
| Days win/draw/lose          | 623 / 68 / 129      |
| Avg. Duration Winners       | 3:16:00             |
| Avg. Duration Loser         | 1 day, 13:25:00     |
| Rejected Entry signals      | 0                   |
| Entry/Exit Timeouts         | 0 / 0               |
|                             |                     |
| Min balance                 | 240.291 USDT        |
| Max balance                 | 1037.862 USDT       |
| Max % of account underwater | 76.85%              |
| Absolute Drawdown (Account) | 76.85%              |
| Absolute Drawdown           | 797.572 USDT        |
| Drawdown high               | 37.862 USDT         |
| Drawdown low                | -759.709 USDT       |
| Drawdown Start              | 2021-03-09 09:40:00 |
| Drawdown End                | 2023-03-15 16:10:00 |
| Market change               | -6.73%              |
=====================================================




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
from indicators import *
import numpy as np # noqa



def supertrend(dataframe, period=7, multiplier=3):
    hl2 = (dataframe['high'] + dataframe['low']) / 2
    atr = ta.ATR(dataframe, timeperiod=period)
    upper_band = hl2 + (multiplier * atr)
    lower_band = hl2 - (multiplier * atr)

    dataframe['supertrend_upper'] = upper_band
    dataframe['supertrend_lower'] = lower_band

    dataframe['in_uptrend'] = True
    for current in range(1, len(dataframe)):
        previous = current - 1

        if dataframe['close'][current] > dataframe['supertrend_upper'][previous]:
            dataframe.loc[current, 'in_uptrend'] = True
        elif dataframe['close'][current] < dataframe['supertrend_lower'][previous]:
            dataframe.loc[current, 'in_uptrend'] = False
        else:
            dataframe.loc[current, 'in_uptrend'] = dataframe['in_uptrend'][previous]
            if dataframe['in_uptrend'][current] and dataframe['supertrend_lower'][current] < dataframe['supertrend_lower'][previous]:
                dataframe.loc[current, 'supertrend_lower'] = dataframe['supertrend_lower'][previous]
            if not dataframe['in_uptrend'][current] and dataframe['supertrend_upper'][current] > dataframe['supertrend_upper'][previous]:
                dataframe.loc[current, 'supertrend_upper'] = dataframe['supertrend_upper'][previous]

    dataframe['supertrend'] = np.where(dataframe['in_uptrend'], dataframe['supertrend_lower'], dataframe['supertrend_upper'])
    dataframe.drop(['supertrend_upper', 'supertrend_lower', 'in_uptrend'], axis=1, inplace=True)

    return dataframe

def process_pair(dataframe, metadata):
    return CustomStrategy.populate_indicators(dataframe, metadata)

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
    
    @staticmethod
    def advise_all_indicators(pair_data: Dict[str, DataFrame]) -> Dict[str, DataFrame]:
        def process_pair(dataframe, metadata):
            return CustomStrategy.populate_indicators(dataframe, metadata)


        with ThreadPoolExecutor() as executor:
            results = executor.map(lambda x: process_pair(*x[1]), pair_data.items())

        return {pair: result.copy() for (_, pair), (result, _) in zip(pair_data.items(), results)}

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.advise_all_indicators = CustomStrategy.advise_all_indicators


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

