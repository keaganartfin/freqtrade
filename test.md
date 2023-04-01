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




This was the response from the console with the suggested changes:

=========================================================== ENTER TAG STATS ===========================================================
|   TAG |   Entries |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|-------+-----------+----------------+----------------+-------------------+----------------+----------------+-------------------------|
| TOTAL |      7599 |          -0.12 |        -903.11 |          -903.859 |         -90.39 |        5:10:00 |  6709     0   890  88.3 |
===================================================== EXIT REASON STATS =====================================================
|   Exit Reason |   Exits |   Win  Draws  Loss  Win% |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |
|---------------+---------+--------------------------+----------------+----------------+-------------------+----------------|
|           roi |    3965 |   3965     0     0   100 |           1.63 |        6454.34 |           6460.48 |         645.43 |
|   exit_signal |    2744 |   2744     0     0   100 |           0.62 |        1700.54 |           1702.14 |         170.05 |
|     stop_loss |     890 |      0     0   890     0 |         -10.18 |       -9057.99 |          -9066.48 |        -905.8  |
======================================================= LEFT OPEN TRADES REPORT ========================================================
|   Pair |   Entries |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|--------+-----------+----------------+----------------+-------------------+----------------+----------------+-------------------------|
|  TOTAL |         0 |           0.00 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
================== SUMMARY METRICS ==================
| Metric                      | Value               |
|-----------------------------+---------------------|
| Backtesting from            | 2021-01-01 00:00:00 |
| Backtesting to              | 2023-03-31 20:30:00 |
| Max open trades             | 10                  |
|                             |                     |
| Total/Daily Avg Trades      | 7599 / 9.28         |
| Starting balance            | 1000 USDT           |
| Final balance               | 96.141 USDT         |
| Absolute profit             | -903.859 USDT       |
| Total profit %              | -90.39%             |
| CAGR %                      | -64.79%             |
| Sortino                     | -4644.98            |
| Sharpe                      | -5.55               |
| Calmar                      | -2.22               |
| Profit factor               | 0.90                |
| Expectancy                  | -0.01               |
| Trades per day              | 9.28                |
| Avg. daily profit %         | -0.11%              |
| Avg. stake amount           | 99.994 USDT         |
| Total trade volume          | 759855.38 USDT      |
|                             |                     |
| Best Pair                   | AVAX/USDT 105.27%   |
| Worst Pair                  | AAVE/USDT -260.11%  |
| Best trade                  | API3/USDT 6.05%     |
| Worst trade                 | ATOM/USDT -10.18%   |
| Best day                    | 103.757 USDT        |
| Worst day                   | -320.122 USDT       |
| Days win/draw/lose          | 252 / 20 / 144      |
| Avg. Duration Winners       | 4:02:00             |
| Avg. Duration Loser         | 13:42:00            |
| Rejected Entry signals      | 7                   |
| Entry/Exit Timeouts         | 0 / 0               |
|                             |                     |
| Min balance                 | 96.141 USDT         |
| Max balance                 | 1912.54 USDT        |
| Max % of account underwater | 94.97%              |
| Absolute Drawdown (Account) | 94.97%              |
| Absolute Drawdown           | 1816.399 USDT       |
| Drawdown high               | 912.54 USDT         |
| Drawdown low                | -903.859 USDT       |
| Drawdown Start              | 2021-04-17 14:20:00 |
| Drawdown End                | 2022-02-20 14:15:00 |
| Market change               | -6.73%              |
=====================================================

the goals of this project are as follows:

Completely Automated, I want to turn this bot on when I wake up in the morning and shut it off before I go to sleep, or maybe keep it on 24 hours a day depending on the state of the profits.

Use machine learning to implement better predictability when trading. (I am not sure if deep learning models would be better for this purpose or if we shouldn't add deep learning models to AA4 please give me your thoughts on this)

To make the most "total profit percentage" we can. Please walk me through how we can increase the "-90.39%" to as high as possible. 

Please use the data libraries we referred to earlier as "freqtrade docs", "Python updated libraries", "general strategies", and "strategy data" to create a walkthrough guide that will best increase the performance of the AA4 and meet these goals. 

Also, what are your thoughts on possibly adding openai's API to AA4? Do you think this would be beneficial enough to go through the headache of adding it in, or the cost to run it in the application?

Also, I am not sure if we should add deep learning models to work with the machine learning or if this would be "too much going on" and cause more problems than help, please give me your thoughts on this.