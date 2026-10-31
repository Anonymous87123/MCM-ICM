# P-C-2022-2229059-dacff43d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | title | pages [1] -->
2229059

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
F1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
Problem Chosen

<!-- b000010 | prose | pages [1] -->
T3

<!-- b000011 | prose | pages [1] -->
F3

<!-- b000012 | title | pages [1] -->
C

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | title | pages [1] -->
2022

<!-- b000016 | prose | pages [1] -->
MCM/ICM

<!-- b000017 | heading | pages [1] -->
Summary Sheet

<!-- b000018 | title | pages [1] -->
Day Trading in Bitcoin and Gold

<!-- b000019 | prose | pages [1] -->
Everyday, market traders buy and sell financial assets with a goal to maximize their total return. Two popular investment asset choices are gold and bitcoin. Bitcoin is an extremely volatile asset and does not have a strong fundamental base like other assets on the market. However, it is able to be traded every day. In contrast, gold is stable, often used as a hedge against downward movements in other sectors, but it can only be traded Monday through Friday – days when the market is open. Our team has been asked by a trader to develop a model, using only past asset prices to date, that determines daily trading actions, in order to maximize profit. For each purchase or sale of bitcoin and gold, a cost is applied to the transaction.

<!-- b000020 | prose | pages [1] -->
We have built a model that calculates the optimal selling and buying times using past values that take into account transaction fees and balances the ideal amount of gold and bitcoin traded. It uses an instantaneous logic model to analyze current market features and determine the most favorable trading action. The model runs from 9/11/2016 to 9/10/2021 and only uses the data given before the time slot it is currently in. Although the data is not continuous, it serves our purpose well as our model uses a macro scale prediction process to recommend trades. We utilize two different day trading theories and combine them into a weighted model.

<!-- b000021 | prose | pages [1] -->
Using common day trading theories we implement logic to guide our model’s deci- sion making. Reversion to the mean and momentum theory contribute heavily and are the drivers of the model that choose whether a trade should be executed. We add, critically, a normalizing weight factor W. This weight factor cancels out noise that could prompt the model to choose a less favorable trade. On top of the model for standard market con- ditions, we add logic that is activated in extreme market conditions and takes precedence over the standard model.

<!-- b000022 | prose | pages [1] -->
The main advantage of our approach is that the model utilizes a well-made conglom- eration of strategies allowing us to avoid common day trading failures. The model han- dles extreme market conditions, and can choose between different trading options; im- portant things when trading a volatile medium like bitcoin. Limitations of our approach are a fixed logic system. It is not sensitive to small changes that might be capitalized on by different strategies, and chooses to wait for macroscopic trends in the market.

<!-- b000023 | keywords | pages [1] -->
Key Words: Momentum Trading, Technical Analysis, Reversion to Mean, Noise Can-

<!-- b000024 | prose | pages [1] -->
cellation, Normalization, Time Aggregation

<!-- b000025 | furniture | pages [2] -->
Team # 2229059

<!-- b000026 | heading | pages [2] -->
contents

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1

<!-- b000029 | heading | pages [2] -->
Introduction

<!-- b000030 | prose | pages [2] -->
1

<!-- b000031 | prose | pages [2] -->
Restatement of problems . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 1

<!-- b000032 | prose | pages [2] -->
General Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 1

<!-- b000033 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000034 | heading | pages [2] -->
Assumptions

<!-- b000035 | prose | pages [2] -->
2

<!-- b000036 | prose | pages [2] -->
Non-Zero Assumption . . . . . . . . . . . . . . . . . . . . . . . 1.3.1 2

<!-- b000037 | prose | pages [2] -->
No Outside Investment . . . . . . . . . . . . . . . . . . . . . . . 1.3.2 2

<!-- b000038 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.3 Price Oscillation

<!-- b000039 | prose | pages [2] -->
2 Analysis of the Problem

<!-- b000040 | prose | pages [2] -->
3

<!-- b000041 | heading | pages [2] -->
Calculating and Simplifying the Model

<!-- b000042 | prose | pages [2] -->
3

<!-- b000043 | prose | pages [2] -->
4

<!-- b000044 | prose | pages [2] -->
5

<!-- b000045 | prose | pages [2] -->
Momentum Trading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5

<!-- b000046 | prose | pages [2] -->
Reversion-to-Mean . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 5

<!-- b000047 | prose | pages [2] -->
Calculating Profitability . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 5

<!-- b000048 | prose | pages [2] -->
Selling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 6

<!-- b000049 | prose | pages [2] -->
Extreme Market Conditions . . . . . . . . . . . . . . . . . . . . . . . . . 3.5 6

<!-- b000050 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.6 No-Buy Condition 7

<!-- b000051 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.7 Holding Assets 7

<!-- b000052 | prose | pages [2] -->
Daily Buy/Sell Order . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.8 7

<!-- b000053 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.9 Noise Normalization

<!-- b000054 | prose | pages [2] -->
4

<!-- b000055 | heading | pages [2] -->
The Model Results

<!-- b000056 | prose | pages [2] -->
8

<!-- b000057 | prose | pages [2] -->
9

<!-- b000058 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 General Result 9

<!-- b000059 | prose | pages [2] -->
Weight Factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 10

<!-- b000060 | prose | pages [2] -->
Parameter Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 10

<!-- b000061 | prose | pages [2] -->
Changes in Transaction Fees . . . . . . . . . . . . . . . . . . . . . . . . 4.4

<!-- b000062 | prose | pages [2] -->
5

<!-- b000063 | heading | pages [2] -->
Validating the Model

<!-- b000064 | prose | pages [2] -->
12

<!-- b000065 | prose | pages [2] -->
13

<!-- b000066 | prose | pages [2] -->
Bitcoin Buy/Sell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 13

<!-- b000067 | prose | pages [2] -->
Gold Buy/Sell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 13

<!-- b000068 | furniture | pages [3] -->
Team # 2229059

<!-- b000069 | prose | pages [3] -->
6

<!-- b000070 | heading | pages [3] -->
Strengths and Weaknesses

<!-- b000071 | heading | pages [3] -->
contents

<!-- b000072 | contents | pages [3] -->
15

<!-- b000073 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [3] -->
6.1

<!-- b000075 | contents | pages [3] -->
Strengths

<!-- b000076 | contents | pages [3] -->
15

<!-- b000077 | contents | pages [3] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [3] -->
6.2

<!-- b000079 | contents | pages [3] -->
7

<!-- b000080 | heading | pages [3] -->
Conclusions

<!-- b000081 | prose | pages [3] -->
8

<!-- b000082 | heading | pages [3] -->
Memorandum

<!-- b000083 | heading | pages [3] -->
Appendices

<!-- b000084 | heading | pages [3] -->
Appendix A First appendix

<!-- b000085 | prose | pages [3] -->
15

<!-- b000086 | prose | pages [3] -->
16

<!-- b000087 | prose | pages [3] -->
17

<!-- b000088 | prose | pages [3] -->
20

<!-- b000089 | prose | pages [3] -->
20

<!-- b000090 | furniture | pages [4] -->
Team # 2229059

<!-- b000091 | furniture | pages [4] -->
Page 1 of 21

<!-- b000092 | prose | pages [4] -->
1

<!-- b000093 | heading | pages [4] -->
Introduction

<!-- b000094 | prose | pages [4] -->
1.1 Restatement of problems

<!-- b000095 | prose | pages [4] -->
Day trading is a predictive problem. It is easy to look back and recognize signals in a stock’s movement that lead to it’s eventual rise or decline, but predicting movements before it happens is an altogether harder problem. Additionally, new assets of different forms come onto the market frequently, and obey different rules, thus requiring different strategies. To add onto the problem, frequency trading is a relatively new discipline, and there is only 40 years of data (at most). In the grand scheme of data science, this is a small data set and it is hard to glean trends from this alone. Because of this, it is important to develop a model that can function using little to no prior data. The assumptions must be contained and edge cases must be accounted for in a successful model. For this specific problem, we have gold, bitcoin, and cash as usable assets. We have no prior data when our model launches. There is a fee associated with trades. The problem is to make money. Approaches are:

<!-- b000096 | prose | pages [4] -->
• finding a model that can extend market trends, or

<!-- b000097 | prose | pages [4] -->
• find a model that can react instantaneously to market moves

<!-- b000098 | prose | pages [4] -->
These models must use their prediction of the market and cleverly make decisions about the most profitable trades. We decided to focus our efforts on a reactive model. The challenges associated with this model are:

<!-- b000099 | prose | pages [4] -->
• the triggers for a buy,

<!-- b000100 | prose | pages [4] -->
• the triggers for a sell,

<!-- b000101 | prose | pages [4] -->
• portfolio awareness, how to balance asset makeup,

<!-- b000102 | prose | pages [4] -->
• extreme market conditions,

<!-- b000103 | prose | pages [4] -->
• different magnitudes of signals,

<!-- b000104 | prose | pages [4] -->
• noise in data

<!-- b000105 | prose | pages [4] -->
1.2 General Definitions

<!-- b000106 | prose | pages [4] -->
• Bitcoin: a digital currency decentralized using blockchains that have lower trans- action fees than traditional online payment mechanisms [Investopedia 2022] Gold: the stored value of the precious metal gold, linked to currencies and interest rates [Investopedia].

<!-- b000107 | prose | pages [4] -->
• Cash: in this problem, cash is in the form of the U.S. dollar ($)

<!-- b000108 | furniture | pages [5] -->
Team # 2229059

<!-- b000109 | furniture | pages [5] -->
Page 2 of 21

<!-- b000110 | prose | pages [5] -->
• Buy: Acquiring bitcoin or gold through trading in its value in cash plus the addi- tional 1% and 2% transaction cost.

<!-- b000111 | prose | pages [5] -->
• Sell: Acquiring the value of cash that corresponds to the value of the asset being sold minus the 1% or 2% transaction fees.

<!-- b000112 | prose | pages [5] -->
• Volatility: the statistical measure of the range of returns on investment (dispersion) for a given security or market index [Investopedia 2022].

<!-- b000113 | prose | pages [5] -->
• Momentum Trading: Buying securities while they are on the rise to sell them at a higher price [Investopedia 2022].

<!-- b000114 | prose | pages [5] -->
• Technical Analysis: A trading strategy that analyzes statistical trends gathered from past trading activity [Investopedia 2022].

<!-- b000115 | prose | pages [5] -->
• Reversion to Mean: Asset prices will eventually revert to the long-run mean [In- vestopedia 2022].

<!-- b000116 | prose | pages [5] -->
• Time Aggregation: Clustering of all data points over a period of time [IBM 2019]

<!-- b000117 | prose | pages [5] -->
• Total Run Period: September 11, 2016 to September 11, 2021

<!-- b000118 | prose | pages [5] -->
1.3

<!-- b000119 | heading | pages [5] -->
Assumptions

<!-- b000120 | prose | pages [5] -->
We make several assumptions in this model to aid in our modeling.

<!-- b000121 | prose | pages [5] -->
1.3.1

<!-- b000122 | heading | pages [5] -->
Non-Zero Assumption

<!-- b000123 | prose | pages [5] -->
Assumption: We assume that the price of the assets will not fall to zero, and stay at zero.

<!-- b000124 | prose | pages [5] -->
Justification: Gold is very stable, and is often used as a hedge against unfavorable mar- ket conditions. It is safe to assume that the price of this commodity will not reach zero. Bitcoin is a foundation for cryptocurrency. There would have to be a full scale melt- down of all crypto infrastructure, either resulting in faulty blockchain usage (not enough miners) or 0 demand. Both of these are extremely unlikely.

<!-- b000125 | prose | pages [5] -->
1.3.2 No Outside Investment

<!-- b000126 | prose | pages [5] -->
Assumption: We assume that we will not be able to leverage our investments and use margin in our model.

<!-- b000127 | prose | pages [5] -->
Justification: Day trading in bitcoin is already a high risk investment, and using margin makes the risk untenable.

<!-- b000128 | furniture | pages [6] -->
Team # 2229059

<!-- b000129 | furniture | pages [6] -->
Page 3 of 21

<!-- b000130 | prose | pages [6] -->
1.3.3 Price Oscillation

<!-- b000131 | prose | pages [6] -->
Assumption: We assume that the price of the assets will oscillate over time.

<!-- b000132 | prose | pages [6] -->
Justification: For any profit to be made from the value of the stock, this assumption must be true. This is a fixed risk assumption: If the stock is flat for all times in the interval, then the model loses the fee, no more.

<!-- b000133 | furniture | pages [7] -->
Team # 2229059

<!-- b000134 | furniture | pages [7] -->
Page 4 of 21

<!-- b000135 | prose | pages [7] -->
2 Analysis of the Problem

<!-- b000136 | prose | pages [7] -->
(b) 1b: Gold Price from 9/11/2016 to 9/10/2021 (a) 1a: Bitcoin Price from 9/11/2016 to 9/10/2021

<!-- b000137 | caption | pages [7] -->
Figure 1: Plots of bitcoin and gold

<!-- b000138 | caption | pages [7] -->
Figure 2: Bitcoin Price from 9/11/2016 to 9/10/2021

<!-- b000139 | prose | pages [7] -->
Figures 1a and 1b show the price evolution of bitcoin and gold from 9/11/2016 to 9/10/2021. Although the movement appears to be connected, figure 2 shows that the difference in scale is drastic. To determine the best trades, we develop a model that returns predictions for profitability on each asset with respect to cash. These predictions are compared, and using the profitability metric, the optimal trade amount is also determined. The model is fully connected; this means that it is aware of other trades happening, and will not make contradictory or redundant actions.

<!-- b000140 | furniture | pages [8] -->
Team # 2229059

<!-- b000141 | furniture | pages [8] -->
Page 5 of 21

<!-- b000142 | heading | pages [8] -->
Calculating and Simplifying the Model

<!-- b000143 | prose | pages [8] -->
3

<!-- b000144 | prose | pages [8] -->
3.1 Momentum Trading

<!-- b000145 | prose | pages [8] -->
We use the common trading technique called momentum trading in our model. We cal- culate the momentum of the asset using the price gradient of an asset and the moving average. The price gradient is a simple calculation. At a time t, we calculate the gradient G by

<!-- b000146 | prose | pages [8] -->
G = ∇P or Gt(n) ≈Pt −Pt−n+1

<!-- b000147 | prose | pages [8] -->
where Pt is the price of the asset at time t. The moving average is given by

<!-- b000148 | prose | pages [8] -->
At(n) =

<!-- b000149 | prose | pages [8] -->
Pn−1

<!-- b000150 | prose | pages [8] -->
i=0 wiPt−i Pn−1

<!-- b000151 | prose | pages [8] -->
i=0 wi

<!-- b000152 | prose | pages [8] -->
where wi is the weight given to the price and Pt is the same as before. For both metrics, n is the time interval we observe. The model then decides whether to buy or sell an asset at a time t like

<!-- b000153 | prose | pages [8] -->


<!-- b000154 | prose | pages [8] -->
Gt(n) (gradient)

<!-- b000155 | prose | pages [8] -->
Mt(n) =

<!-- b000156 | prose | pages [8] -->
Pt −At(n) (difference between price and moving average)

<!-- b000157 | prose | pages [8] -->
Both cases must be true for Mt(n) to return a buy signal. If both Gt(n) > 1 and Pt−At(n) > 1 then Mt(n) > 1 and a buy signal is issued and remains active until the next time period t + 1. Otherwise, a sell signal is issued. Combining the two techniques allows us to capitalize on price increases more efficiently.

<!-- b000158 | prose | pages [8] -->
3.2 Reversion-to-Mean

<!-- b000159 | prose | pages [8] -->
Momentum trading is a good method if the price tends to break out above a moving average. We want our model to be conscious of movements below the moving-average as well, and thus we implement reversion-to-mean strategies. We write

<!-- b000160 | prose | pages [8] -->
Z µ+i

<!-- b000161 | prose | pages [8] -->
Z µ+ j

<!-- b000162 | prose | pages [8] -->
P(x)dx >

<!-- b000163 | prose | pages [8] -->
i > j > 0 P(x)dx

<!-- b000164 | prose | pages [8] -->
µ−j

<!-- b000165 | prose | pages [8] -->
µ−i

<!-- b000166 | prose | pages [8] -->
for

<!-- b000167 | prose | pages [8] -->
For our model, this says that the farther the price deviates from the moving average, the more likely it is on the next time step to be closer to the moving average. This can be interpreted qualitatively by noting that as the price of an asset falls far below the moving average, it is likely to make positive moves in the future and thus the signal is a buy.

<!-- b000168 | prose | pages [8] -->
3.3 Calculating Profitability

<!-- b000169 | caption | pages [8] -->
Figure 3 describes the general logic that we use to determine buy/sell indicators. We

<!-- b000170 | prose | pages [8] -->
extend this by adding a ’profitability’ metric to each indicator that is returned. For mo- mentum trades, we say that the profitability is proportional to the gradient of the price.

<!-- b000171 | furniture | pages [9] -->
Team # 2229059

<!-- b000172 | furniture | pages [9] -->
Page 6 of 21

<!-- b000173 | caption | pages [9] -->
Figure 3: Flow Chart Describing our buy logic.

<!-- b000174 | prose | pages [9] -->
This is given by the momentum metric. Our justification for this is that if the momen- tum is extremely high, the trend will carry on for longer, and profit is more likely. For reversion-to-the-mean trades, we say that the profitability is proportional to the square of the distance from the mean. Given the assumption that the price will revert to the mean, our model makes small trades for normal oscillations, and in large drops in price that fall far below the moving average, the model recognizes this as a crash and buys larger amounts.

<!-- b000175 | prose | pages [9] -->
3.4 Selling

<!-- b000176 | prose | pages [9] -->
Our selling mechanism is simple and conservative. One of our assumptions is that the price oscillates. That is, after a period of increase, there will be a period of decrease. Our selling implementation compares the price of the asset on the day with the average price paid for an asset. Adding in fees, the model then determines if the profit made from a sell would be greater than a margin L. This looks like

<!-- b000177 | prose | pages [9] -->
S = (1 −fa) · P −

<!-- b000178 | prose | pages [9] -->
Pn

<!-- b000179 | prose | pages [9] -->
i=0 (1 −fai)Ci

<!-- b000180 | prose | pages [9] -->
−L i

<!-- b000181 | prose | pages [9] -->
Where fa is the fee of an asset, P is the price of the asset, and C is the cost paid for an asset. We sum over the differing costs paid, including the reduction from fees, to calculate the average cost of an asset we have on the market. Specifically, this says that the sell indicator S is (1 −fg) · P (the amount gained from a sell, including fees) minus Pn

<!-- b000182 | prose | pages [9] -->
0 (1−fgn)Cn (the average price of an asset in the market) minus the margin L. If S > 0, the n model sells.

<!-- b000183 | prose | pages [9] -->
3.5 Extreme Market Conditions

<!-- b000184 | prose | pages [9] -->
Bitcoin is a highly volatile asset, and is subject to large jumps in price. Capitalizing on these movements successfully is critical to making large profits. We implement an ’extreme market condition’ that takes over the model when activated. The condition for

<!-- b000185 | furniture | pages [10] -->
Team # 2229059

<!-- b000186 | furniture | pages [10] -->
Page 7 of 21

<!-- b000187 | prose | pages [10] -->
an extreme market condition is the gradient being over 5 times the average gradient over the history of the model.

<!-- b000188 | prose | pages [10] -->
Pn

<!-- b000189 | prose | pages [10] -->
i=0 Gt(i)

<!-- b000190 | prose | pages [10] -->
E = Gt(n) −C ·

<!-- b000191 | prose | pages [10] -->
n where C is a scaling factor. If E is positive, then the price of an asset is growing rapidly and an extreme market condition takes over. If this is the case, the model is not allowed to sell an asset until the price has regressed to a percentage of its maximum value over the interval, or a price ∆P below its maximum over the interval. This eliminates the possibility of a premature sell, as would happen if our model used its normal sell function.

<!-- b000192 | prose | pages [10] -->
3.6 No-Buy Condition

<!-- b000193 | prose | pages [10] -->
Following an extreme market condition comes abnormal selling conditions. Often times, as the price of an asset regresses, there will be small increases on the way back down. Following an extreme market condition and a peak, it is unlikely that there will be another surge immediately following. Thus, we implement a ’no-buy’ condition, that is activated when there has been an extreme market condition in a recent time interval and the model has recently sold an asset. The model is then no longer allowed to buy back into the market for a number of days.

<!-- b000194 | prose | pages [10] -->
3.7 Holding Assets

<!-- b000195 | prose | pages [10] -->
Because of the erratic nature of stocks, it is hard to predict the exact movement of a stock on any day. Additionally, the data given is daily. We choose to focus on larger movement trends and ignore minuscule price changes. The reason for this is fees: buying and selling at every possible change in price may seem to be extremely profitable, but the fees begin to play a major role in the profits at this point. Additionally, in periods of large gain or fall, small corrections will cause the model to sell when it should be considering longer- term gains. Thus, we implement a holding period of z days. Once the model buys an asset, it can no longer sell for those z days.

<!-- b000196 | prose | pages [10] -->
Daily Buy/Sell Order 3.8

<!-- b000197 | prose | pages [10] -->
We assume that the model checks the prices in the market once a day, because our data is daily. The order of action on a given day is to first check for ’no-buy’ and extreme market conditions. If no-active, then the model immediately moves to the sell indicators. If extreme market conditions are activated, control is shifted to the extreme market logic and the rest of the program is skipped. The model then checks the buy indicators, and compares them to decide what to buy. It stores this decision and checks the sell indicator for the other asset. Then, the model executes the order, selling first if indicated, and then buying. If neither buy markers were activated, then the model can choose to sell both assets.

<!-- b000198 | furniture | pages [11] -->
Team # 2229059

<!-- b000199 | furniture | pages [11] -->
Page 8 of 21

<!-- b000200 | prose | pages [11] -->
3.9 Noise Normalization

<!-- b000201 | prose | pages [11] -->
As shown in figure 2, the assets can differ in the magnitude of movement. We tackle this problem by introducing a weight factor that goes like

<!-- b000202 | prose | pages [11] -->
W = C 1

<!-- b000203 | prose | pages [11] -->
t2

<!-- b000204 | prose | pages [11] -->
where t is time in days, and C is a scalar constant. As t approaches larger values, the weight factor becomes very small. This drowns out small changes in price movement, so that the model considers large signals only. When comparing the profitability between gold and bitcoin, the bitcoin markers are considered much more heavily than the gold markers. This allows the model to choose the more profitable trade.

<!-- b000205 | furniture | pages [12] -->
Team # 2229059

<!-- b000206 | furniture | pages [12] -->
Page 9 of 21

<!-- b000207 | prose | pages [12] -->
4

<!-- b000208 | heading | pages [12] -->
The Model Results

<!-- b000209 | prose | pages [12] -->
4.1

<!-- b000210 | heading | pages [12] -->
General Result

<!-- b000211 | caption | pages [12] -->
Figure 4: Our results.

<!-- b000212 | caption | pages [12] -->
Figure 4 shows the results of our model. The total ends at $220, 486. This represents

<!-- b000213 | prose | pages [12] -->
a return on investment of 21, 948% and an annualized return on investment of 194%. Observing figure 4 and comparing figure 1a and 1b we can see that the model sells at near-optimal points. Note the times t ≈500, 1050, 1625. These are critical points cor- responding to bitcoin crashes. Because of the setup of our model, the portfolio is, in general, bitcoin heavy. However, the model activates the extreme market conditions, and executes the necessary trades to preserve the portfolio value. We see a common trend: the model sells all bitcoin when it gets large sell signals, and then slowly buys back in as bitcoin decreases or stays level. Our model is designed to make money. Thus, it sacri- fices hedges like gold in favor of going in all in on bitcoin when it receives a large buy signal. Compare figure 1a we can see that the model follows bitcoin very closely, as it invests heavily in the asset. Especially on the up-trends, the performance is near identi- cal. However, our model stays much flatter through the down-trends, again showing how the model is selling and staying in cash through periods of price decrease. Because of the reversion-to-the-mean strategy, the model slowly buys back in as the price of bitcoin decreases, decreasing the overall asset cost.

<!-- b000214 | furniture | pages [13] -->
Team # 2229059

<!-- b000215 | furniture | pages [13] -->
Page 10 of 21

<!-- b000216 | prose | pages [13] -->
4.2 Weight Factor

<!-- b000217 | caption | pages [13] -->
Figure 5: The weight factor normalizing the magnitude of the signals.

<!-- b000218 | caption | pages [13] -->
Figure 5 is the effect of the weight factor on the buy signals. The y-axis is a unitless

<!-- b000219 | prose | pages [13] -->
measure of profitability. We can see that although the magnitude of price movements in bitcoin increase, the signals that the model generates are normalized. Note the high signals in 0 < t < 100. This is due to the lack of data, since the model can only use data points it has seen. Note also that this is the only time that gold has a large buy signal. For the rest of the time the model is active bitcoin is much more highly valued and takes precedent. The model thus sees bitcoin as being much more profitable, due to its volatility.

<!-- b000220 | prose | pages [13] -->
4.3 Parameter Optimization

<!-- b000221 | caption | pages [13] -->
Figure 6: Results under different combinations.

<!-- b000222 | furniture | pages [14] -->
Team # 2229059

<!-- b000223 | furniture | pages [14] -->
Page 11 of 21

<!-- b000224 | caption | pages [14] -->
Figure 6 shows the results of our model under different variations of parameters. The

<!-- b000225 | prose | pages [14] -->
parameters varied are in the format [T, N, E]. T is the time the model must hold an asset. L is the price the asset must fall to (as a percentage of the maximum price) for the model to begin buying assets again. E is the percentage of the max price that an asset must fall to for the model to sell in an extreme market condition. In the table below, we can see that the combination [12, 0.6, 0.89] is optimal.

<!-- b000226 | prose | pages [14] -->
Observe that small changes at the beginning are indicative of overall model success. Our model works excellently given the data. At low times, there is no history for the model to average over, and thus it perceives smaller signals as larger magnitude buys. Because of this, the model is profitable at low times. Having a larger portfolio earlier on leverages the model, which is why we see huge divergence in the final amounts in figure 6.

<!-- b000227 | prose | pages [14] -->
Per formance Index

<!-- b000228 | prose | pages [14] -->
Poor 1

<!-- b000229 | prose | pages [14] -->
Poor 2

<!-- b000230 | prose | pages [14] -->
Poor 3

<!-- b000231 | prose | pages [14] -->
Good 4

<!-- b000232 | prose | pages [14] -->
Great 5

<!-- b000233 | prose | pages [14] -->
Great 6

<!-- b000234 | prose | pages [14] -->
Good 7

<!-- b000235 | prose | pages [14] -->
Great 8

<!-- b000236 | prose | pages [14] -->
Good 9

<!-- b000237 | prose | pages [14] -->
Poor 10

<!-- b000238 | prose | pages [14] -->
Poor 11

<!-- b000239 | prose | pages [14] -->
Poor 12

<!-- b000240 | prose | pages [14] -->
Poor 13

<!-- b000241 | prose | pages [14] -->
Great 14

<!-- b000242 | prose | pages [14] -->
Great 15

<!-- b000243 | prose | pages [14] -->
Poor 16

<!-- b000244 | prose | pages [14] -->
Good 17

<!-- b000245 | prose | pages [14] -->
Good 18

<!-- b000246 | prose | pages [14] -->
Poor 19

<!-- b000247 | prose | pages [14] -->
Poor 20

<!-- b000248 | prose | pages [14] -->
Poor 21

<!-- b000249 | prose | pages [14] -->
Poor 22

<!-- b000250 | prose | pages [14] -->
Best 23

<!-- b000251 | prose | pages [14] -->
Great 24

<!-- b000252 | prose | pages [14] -->
Poor 25

<!-- b000253 | prose | pages [14] -->
Great 26

<!-- b000254 | prose | pages [14] -->
Great 27

<!-- b000255 | prose | pages [14] -->
Parameter Set Final Amount in USD

<!-- b000256 | prose | pages [14] -->
[5, 0.4, 0.86] 14023

<!-- b000257 | prose | pages [14] -->
[5, 0.4, 0.89] 24183

<!-- b000258 | prose | pages [14] -->
[5, 0.4, 0.895] 24183

<!-- b000259 | prose | pages [14] -->
[5, 0.6, 0.86] 117416

<!-- b000260 | prose | pages [14] -->
[5, 0.6, 0.89] 185291

<!-- b000261 | prose | pages [14] -->
[5, 0.6, 0.895] 169463

<!-- b000262 | prose | pages [14] -->
[5, 0.65, 0.86] 106137

<!-- b000263 | prose | pages [14] -->
[5, 0.65, 0.89] 157249

<!-- b000264 | prose | pages [14] -->
[5, 0.65, 0.895] 140421

<!-- b000265 | prose | pages [14] -->
[6, 0.4, 0.86] 13307

<!-- b000266 | prose | pages [14] -->
[6, 0.4, 0.89] 24183

<!-- b000267 | prose | pages [14] -->
[6, 0.4, 0.895] 24183

<!-- b000268 | prose | pages [14] -->
[6, 0.6, 0.86] 90167

<!-- b000269 | prose | pages [14] -->
[6, 0.6, 0.89] 181230

<!-- b000270 | prose | pages [14] -->
[6, 0.6, 0.895] 169178

<!-- b000271 | prose | pages [14] -->
[6, 0.65, 0.86] 82855

<!-- b000272 | prose | pages [14] -->
[6, 0.65, 0.89] 135476

<!-- b000273 | prose | pages [14] -->
[6, 0.65, 0.895] 123393

<!-- b000274 | prose | pages [14] -->
[12, 0.4, 0.86] 72670

<!-- b000275 | prose | pages [14] -->
[12, 0.4, 0.89] 24183

<!-- b000276 | prose | pages [14] -->
[12, 0.4, 0.895] 24183

<!-- b000277 | prose | pages [14] -->
[12, 0.6, 0.86] 72670

<!-- b000278 | prose | pages [14] -->
[12, 0.6, 0.89] 220486

<!-- b000279 | prose | pages [14] -->
[12, 0.6, 0.895] 178076

<!-- b000280 | prose | pages [14] -->
[12, 0.65, 0.86] 72670

<!-- b000281 | prose | pages [14] -->
[12, 0.65, 0.89] 175510

<!-- b000282 | prose | pages [14] -->
[12, 0.65, 0.895] 162657

<!-- b000283 | furniture | pages [15] -->
Team # 2229059

<!-- b000284 | prose | pages [15] -->
4.4 Changes in Transaction Fees

<!-- b000285 | furniture | pages [15] -->
Page 12 of 21

<!-- b000286 | prose | pages [15] -->
We also want to observe how the model behaves when the transaction fees change. We ran the optimal model with different sets of fees.

<!-- b000287 | caption | pages [15] -->
Figure 7: Results under different combinations.

<!-- b000288 | prose | pages [15] -->
Index Parameter Set Final Amount in USD [0.01, 0.02] 1 220486 [0.02, 0.03] 2 199945 [0.03, 0.05] 3 156038 [0.1, 0.1] 4 47452

<!-- b000289 | prose | pages [15] -->
The parameter set is [gold fee, bitcoin fee]. We can see that the performance decreases as the fees increase, as expected. The model continues to buy and sell, factoring in the fees into the buy and sell price, but for each transaction, less money stays in the portfolio. Because this model is a high-frequency trading model, the fees accumulate quickly. We can see that especially at the start, when the model is in ’normal’ market mode, it is trading most frequently and racking up the fees. As the transaction fees increase, the model generates profit at a fraction of its maximum. Since the fees are a percentage, the loss is small when the market is flat. In periods of massive price increase, however, small changes in initial value compound, leading to the disparity seen in figure 7 and accompanying chart.

<!-- b000290 | furniture | pages [16] -->
Team # 2229059

<!-- b000291 | furniture | pages [16] -->
Page 13 of 21

<!-- b000292 | prose | pages [16] -->
5

<!-- b000293 | heading | pages [16] -->
Validating the Model

<!-- b000294 | prose | pages [16] -->
We can test the performance of our model by observing the buy and sell times.

<!-- b000295 | prose | pages [16] -->
Bitcoin Buy/Sell 5.1

<!-- b000296 | caption | pages [16] -->
Figure 8: Buy (RED) and Sell (BLUE) orders for bitcoin between 1610 and 1760 days.

<!-- b000297 | caption | pages [16] -->
Figure 8 shows the buy and call orders for bitcoin from t = 1610 to t = 1760 days.

<!-- b000298 | prose | pages [16] -->
The buy orders are red, and the sell orders are blue.

<!-- b000299 | prose | pages [16] -->
Observing the active orders from figure 8, we can see that the model looks to buy on the upward trend. At t = 18 (t = 1628 overall), the model senses downward trend and sells. Because this is the peak, (compare figure 1a) it is an extreme market condition, and thus the sell order also triggers the no buy condition. Although this causes the model to miss the peak by a small margin, the sell price is still extremely profitable. Notice the dearth af signals from t = 18 to t = 105. This is the ’no-buy’ condition being activated after the sell indicator. Notice, critically, that this stops the model from buying in near the peak, which would be a very poor trade. The model then buys back in at t = 105 (t = 1715 overall) and continues to change the portfolio from cash to bitcoin. Compare to figure 1a we can see that this is near the trough (the minimum is around 35000$) and the bitcoin prices rise quickly again, at t = 1750 (t = 140 on figure 8. This is exactly the behavior that we want

<!-- b000300 | prose | pages [16] -->
Gold Buy/Sell 5.2

<!-- b000301 | caption | pages [16] -->
Figure 9 shows the buy and call orders for gold from t = 1610 to t = 1760 days.

<!-- b000302 | prose | pages [16] -->
We use a different time interval because at later times, bitcoin indicators are much stronger and the buy/sell analysis for gold is not insightful. We can see that the model

<!-- b000303 | furniture | pages [17] -->
Team # 2229059

<!-- b000304 | furniture | pages [17] -->
Page 14 of 21

<!-- b000305 | caption | pages [17] -->
Figure 9: Buy (RED) and Sell (BLUE) orders for gold between 460 and 560 days.

<!-- b000306 | prose | pages [17] -->
buys continuously on the uptrend, and sells at a price of roughly 1950 near the peak. These are the model’s normal buy signals: and it is working properly for gold through this interval. Figure 9 shows the buy times, but not the amounts. As the model buys, it does so like the weight factor 1

<!-- b000307 | prose | pages [17] -->
t2. Thus, at the beginning of the buy cycle the amounts are larger and the portfolio gets converted to gold in decaying amounts.

<!-- b000308 | furniture | pages [18] -->
Team # 2229059

<!-- b000309 | furniture | pages [18] -->
Page 15 of 21

<!-- b000310 | prose | pages [18] -->
6

<!-- b000311 | heading | pages [18] -->
Strengths and Weaknesses

<!-- b000312 | prose | pages [18] -->
6.1

<!-- b000313 | heading | pages [18] -->
Strengths

<!-- b000314 | prose | pages [18] -->
Our model performs well under volatile market conditions and can use that volatility to gain profit. It balances the different signals from different types of assets and is able to make decisions on whether to buy, sell, and what amount to trade with. A key feature of our model that makes it excel in the bitcoin market is its ability to trade in different growth stages. When the price of the asset is relatively flat, oscillating between two points, the model trades according to its normal logic and can make profit. If the price breaks out and begins to increase rapidly, the model immediately recognizes this and changes its logic in preparation for expected conditions and to secure maximum profit on this price move. The model is also able to differentiate between different strengths of signal; although there may be signals telling the model to buy gold, signals from bitcoin might have a stronger signature and the model will know that the most profitable trade is bitcoin.

<!-- b000315 | prose | pages [18] -->
Our model also is able to perform well using minimal to no data, as it is completely logic based. There is no need to calculate a trend from historical data, as the model can make instantaneous decisions based on current price movements alone. However, the model does adapt over time, considering moving averages and past price gradients to guide it in making the most profitable trades.

<!-- b000316 | prose | pages [18] -->
6.2

<!-- b000317 | heading | pages [18] -->
Weaknesses

<!-- b000318 | prose | pages [18] -->
A weakness of our model is that it may be over-fit to the data. Because of the nature of the problem, the model must be logic-based and/or learn on the fly. We chose the optimal parameters for our model using numerical optimization. However, the parameters we chose may work differently for different data sets. Despite this, figure 6 shows that for small variations in parameters the fall-off is not massive. Although it is far from optimal, the model is still profitable in most cases. We are also confident that the normal func- tionality of the model would be preserved, and in a normal market condition the model would work similarly.

<!-- b000319 | prose | pages [18] -->
Another weakness is that the model does not trade at maximum frequency and instead looks for bigger trends in price movement. This is primarily due to the data set; there is limited points from which dips and peaks in the price can be exploited. For volatile assets, it is hard to ascertain whether this is a weakness or strength. Although the model may lose profit on the many peaks and dips generated in the short term, the ability to capitalize efficiently on the huge price spikes is critical.

<!-- b000320 | furniture | pages [19] -->
Team # 2229059

<!-- b000321 | furniture | pages [19] -->
Page 16 of 21

<!-- b000322 | prose | pages [19] -->
7

<!-- b000323 | heading | pages [19] -->
Conclusions

<!-- b000324 | prose | pages [19] -->
Our objective was to:

<!-- b000325 | prose | pages [19] -->
• build a model that generates maximum profit over the time period.

<!-- b000326 | prose | pages [19] -->
In order to do this, we had to create an algorithm that could function with very low data sizes. We used a combination of momentum trading and reversion to the mean theories in our trading logic. We further improved this model by adding conditions for extreme market conditions that might occur in volatile markets like bitcoin. Optimizing our model revealed to us the best parameters for our model. Using these parameters, our model worked well on the data set provided and beat the market in returns, generating $219,799 from a principal investment of $1000 4 years prior.

<!-- b000327 | furniture | pages [20] -->
Team # 2229059

<!-- b000328 | furniture | pages [20] -->
Page 17 of 21

<!-- b000329 | prose | pages [20] -->
8

<!-- b000330 | heading | pages [20] -->
Memorandum

<!-- b000331 | prose | pages [20] -->
DATE: February 2022 TO: Interested Investors FROM: Modeling Team 2229059 SUBJECT: Day Trading Model

<!-- b000332 | prose | pages [20] -->
Our team was assigned to create a model that would calculate the optimal daily strategy to trade between cash, gold, and bitcoin in order to generate the most profit. The model was initialized at $1000 cash on September 11, 2016 and terminated on September 11, 2021. Using price data that was recorded up to only the day of trading, we successfully created a model that predicted future trends and informed current investment strategies utilizing various trading and normalization methods.

<!-- b000333 | prose | pages [20] -->
Our model was created on the basis of two main trading strategies: momentum theory and reversion to the mean. The momentum of the financial asset is calculated through the price gradient – the change in price in an interval of time – and moving average – the summation of previous weighted prices divided by a sum of previous weights. If both the gradient and moving average are greater than 1 at the time of trading, a buy signal will be generated. Otherwise, a sell signal is issued. Since momentum trading determines trades when the price rises above the moving average, the reversion to mean strategy is used to catch price movements below it. This theory states that the farther the price deviates away from the moving average, the greater the probability it will move towards the average on its next time step. If the price falls far below the moving average, it is more likely to increase in the future, so our model will generate a buy signal. A combination of these two theories creates the trading strategy our model uses for normal market conditions.

<!-- b000334 | prose | pages [20] -->
The second part of trading is to determine how much to buy at each trade. We do this by calculating the profitability of the current market. The profitability is directly proportional to the gradient of the price, so the larger the magnitude the gradient has, the larger the amount of assets it will purchase.

<!-- b000335 | prose | pages [20] -->
In standard market conditions, the general sequence of asset trading is coded as follows: The model checks for sell indicators, selling any assets if demanded. The model checks the gold and bitcoin buy indicators, compares them to decide if and what to buy. If neither buy signals were issued, the model can choose to sell both assets.

<!-- b000336 | prose | pages [20] -->
When an asset is bought, it will not immediately be sold, even though a contin- uous buying and selling at any increase in value may seem profitable because of the transaction fees in place. Therefore, our model implements a holding period of z days where the asset is not bought or sold.

<!-- b000337 | prose | pages [20] -->
The strategy described previously was to operate during normal market condi- tions. In the case of extreme market conditions, a second sequence of logic is acti- vated, overriding our previous methods. If the current gradient is calculated to five

<!-- b000338 | furniture | pages [21] -->
Team # 2229059

<!-- b000339 | furniture | pages [21] -->
Page 18 of 21

<!-- b000340 | prose | pages [21] -->
times the average historical gradient, the extreme market conditions algorithm is run. This means that the model will not sell until the price of the asset has returned to a price ∆P below its maximum over the interval. This method is used to prevent the premature selling that could have occurred if the normal strategy was implemented. Following the extreme market conditions sequence, we run a no-buy condition where the model will not buy into the market for a certain period of time.

<!-- b000341 | prose | pages [21] -->
After running our model for the four-year period, we obtained a final asset value of $219,799 – a return on investment of 21,880%. Our model buys and sells at near optimal points and responds effectively to market crashes and critical points. Since our model’s purpose is profit, it will buy and sell assets with that sole intention, resulting in a final portfolio of largely bitcoin and less gold.

<!-- b000342 | prose | pages [21] -->
Though our model is profitable and effective, we recognize its strengths and weaknesses. We will be glad to discuss any further recommendations on improv- ing it to increase its efficiency and profitability.

<!-- b000343 | prose | pages [21] -->
Thank you for supporting this endeavor.

<!-- b000344 | prose | pages [21] -->
Sincerely,

<!-- b000345 | prose | pages [21] -->
Modeling Team

<!-- b000346 | furniture | pages [22] -->
Team # 2229059

<!-- b000347 | heading | pages [22] -->
References

<!-- b000348 | furniture | pages [22] -->
Page 19 of 21

<!-- b000349 | references | pages [22] -->
[1] COMAP 2022. Problem C data set 1. 2022

<!-- b000350 | references | pages [22] -->
[2] COMAP 2022. Problem C data set 2. 2022

<!-- b000351 | references | pages [22] -->
[3] Wolfram Mathworld, Reversion to the Mean. https://mathworld.wolfram.

<!-- b000352 | references | pages [22] -->
com/ReversiontotheMean.html

<!-- b000353 | references | pages [22] -->
[4] Taylor & Francis Online, ’Trend following with momentum versus moving

<!-- b000354 | references | pages [22] -->
a tale of differences’. Valeriy, Zakamulin, 2020. https://www.

<!-- b000355 | references | pages [22] -->
averages:

<!-- b000356 | references | pages [22] -->
tandfonline.com/doi/full/10.1080/14697688.2020.1716057

<!-- b000357 | references | pages [22] -->
Momentum

<!-- b000358 | references | pages [22] -->
[5] Barone,

<!-- b000359 | references | pages [22] -->
Adam.

<!-- b000360 | references | pages [22] -->
“What

<!-- b000361 | references | pages [22] -->
Is

<!-- b000362 | references | pages [22] -->
Trading?”

<!-- b000363 | references | pages [22] -->
Investopedia,

<!-- b000364 | references | pages [22] -->
Investo-

<!-- b000365 | references | pages [22] -->
https://www.investopedia.com/trading/

<!-- b000366 | references | pages [22] -->
pedia,

<!-- b000367 | references | pages [22] -->
8

<!-- b000368 | references | pages [22] -->
Feb.

<!-- b000369 | references | pages [22] -->
2022,

<!-- b000370 | references | pages [22] -->
introduction-to-momentum-trading/

<!-- b000371 | references | pages [22] -->
James. “Understanding the Theory of Mean Reversion.” Investope-

<!-- b000372 | references | pages [22] -->
[6] Chen,

<!-- b000373 | references | pages [22] -->
dia, Investopedia, 5 Nov. 2021, https://www.investopedia.com/terms/m/

<!-- b000374 | references | pages [22] -->
meanreversion.asp

<!-- b000375 | references | pages [22] -->
[7] Frankenfield, Jake. “Bitcoin Definition: How Does Bitcoin Work?” Investope-

<!-- b000376 | references | pages [22] -->
dia, Investopedia, 20 Feb. 2022, https://www.investopedia.com/terms/b/

<!-- b000377 | references | pages [22] -->
bitcoin.asp

<!-- b000378 | references | pages [22] -->
https://www.investopedia.com/

<!-- b000379 | references | pages [22] -->
Investopedia,

<!-- b000380 | references | pages [22] -->
[8] “Gold.”

<!-- b000381 | references | pages [22] -->
Investopedia,

<!-- b000382 | references | pages [22] -->
gold-4689769

<!-- b000383 | references | pages [22] -->
[9] Hayes,

<!-- b000384 | references | pages [22] -->
Adam.

<!-- b000385 | references | pages [22] -->
“Understanding

<!-- b000386 | references | pages [22] -->
Technical

<!-- b000387 | references | pages [22] -->
Analysis.”

<!-- b000388 | references | pages [22] -->
Investopedia,

<!-- b000389 | references | pages [22] -->
In-

<!-- b000390 | references | pages [22] -->
https://www.investopedia.com/terms/t/

<!-- b000391 | references | pages [22] -->
vestopedia,

<!-- b000392 | references | pages [22] -->
8

<!-- b000393 | references | pages [22] -->
Feb.

<!-- b000394 | references | pages [22] -->
2022,

<!-- b000395 | references | pages [22] -->
technicalanalysis.asp

<!-- b000396 | references | pages [22] -->
[10] Hayes, Adam. “Volatility.” Investopedia, Investopedia, 8 Feb. 2022, https://www.

<!-- b000397 | references | pages [22] -->
investopedia.com/terms/v/volatility.asp

<!-- b000398 | references | pages [22] -->
[11] IBM Corporation. Time Aggregation, 2019, https://www.ibm.com/docs/en/

<!-- b000399 | references | pages [22] -->
tnpm/1.4.5?topic=series-time-aggregation

<!-- b000400 | furniture | pages [23] -->
Team # 2229059

<!-- b000401 | furniture | pages [23] -->
Page 20 of 21

<!-- b000402 | heading | pages [23] -->
Appendices

<!-- b000403 | heading | pages [23] -->
Appendix A

<!-- b000404 | prose | pages [23] -->
First appendix

<!-- b000405 | prose | pages [23] -->
Here are simulation programs we used in our model, in pseudocode.

<!-- b000406 | prose | pages [23] -->
Input python source:

<!-- b000407 | prose | pages [23] -->
import numpy as np import pandas as pd

<!-- b000408 | prose | pages [23] -->
class Portfolio():

<!-- b000409 | prose | pages [23] -->
def constructor():

<!-- b000410 | prose | pages [23] -->
make a portfolio

<!-- b000411 | prose | pages [23] -->
def sell_function():

<!-- b000412 | prose | pages [23] -->
sell assets

<!-- b000413 | prose | pages [23] -->
def buy_function():

<!-- b000414 | prose | pages [23] -->
buy assets

<!-- b000415 | prose | pages [23] -->
class Market():

<!-- b000416 | prose | pages [23] -->
def constructor():

<!-- b000417 | prose | pages [23] -->
read in data

<!-- b000418 | prose | pages [23] -->
def grad():

<!-- b000419 | prose | pages [23] -->
price gradient

<!-- b000420 | prose | pages [23] -->
def weight_factor():

<!-- b000421 | prose | pages [23] -->
calculate weight factor

<!-- b000422 | prose | pages [23] -->
def profit_chance():

<!-- b000423 | prose | pages [23] -->
calculate chances of profit for gold and bitcoin

<!-- b000424 | prose | pages [23] -->
def sell_chance():

<!-- b000425 | prose | pages [23] -->
calculate whether the model should sell

<!-- b000426 | prose | pages [23] -->
def extreme_growth(self, day):

<!-- b000427 | prose | pages [23] -->
calculate if the market is in an extreme growth period

<!-- b000428 | prose | pages [23] -->
def run():

<!-- b000429 | prose | pages [23] -->
instantiate classes initiate required lists to hold values initiate variables to starting values for each day:

<!-- b000430 | prose | pages [23] -->
check if it is a weekend check if the model can sell assets calculate the average price of assets currently in portfolio

<!-- b000431 | furniture | pages [24] -->
Team # 2229059

<!-- b000432 | furniture | pages [24] -->
Page 21 of 21

<!-- b000433 | prose | pages [24] -->
check if extreme market or no buy conditions are active if extreme market conditions are active:

<!-- b000434 | prose | pages [24] -->
use the extreme market sell conditions continue check if the model should buy gold or bitcoin go through the buy/sell logic and make appropriate trades
