# P-C-2022-2218743-984f9ab2

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2022

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | title | pages [1] -->
C

<!-- b000004 | title | pages [1] -->
2218743

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Gold-Bitcoin Market Portfolio Investment Strategy

<!-- b000008 | title | pages [1] -->
Model and Its Application

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In order to obtain higher investment returns and minimize risks, We strive to establish the optimal investment strategy model for eﬀective investment portfolio with two risky assets, gold and bitcoin, and cash, a risk-free asset. The optimal investment decision test and sensitivity test are carried out on the model we established. First, we use the ARIMA algorithm and determine reasonable model parameters based on historical data to predict the asset price of the next day. Considering that too frequent transactions will increase transaction costs, we judge the current market state based on the moving average long-arrangement method, and establishes a trading day selection model with the bull and bear market as the standard. Then, we use the CVaR method to measure the risk of a portfolio. On this basis, we establish the revenue-CVAR dual-objective optimization model, and we use the improved NSGA-II algorithm to obtain a series of feasible portfolios set. Then, combined with the upper limit constraint of the downside semi-variance of the asset portfolio, we obtain the optimal daily trading strategy. Bringing the available data into the built model, we ﬁnd that the ﬁnal investment strategy has a 5-year total investment return of 616.63%, an average annual return of 261.41%, and a maximum annual return of 664.69%, which proves that the investment strategy has strong proﬁtability.

<!-- b000011 | prose | pages [1] -->
Second, we prove that the model provides the optimal investment strategy. In the prediction deviation test, the MAPE values are all less than 0.1 and very close to 0 and the R2-score are all greater than 94% and close to 1. This shows that the model can accurately predict the obvious ﬂuctuations of prices and grasp the investment opportunity. In the performance test of the investment strategy, the results show that the investment model can buy in the early stage of the bull market, hold it to rise, and accurately grasp the proﬁt opportunities. Meanwhile, the model has the ability to survive the bear market smoothly, which means it has a high ability to resist risk ﬂuctuations. In addition, on the basis of the given investment strategies, random disturbances are applied to generate 1000 groups of simulated investment strategies. Comparing yield of diﬀerent investment strategies, we ﬁnd that the 5-year average annual return of the simulated investment is lower than the investment strategy we give, and the 5-year total return of our investment strategy is higher than 93% of the simulated investment strategies, which proves that our investment model can maximize proﬁt and minimize risk at the same time.

<!-- b000012 | prose | pages [1] -->
We test the model’s sensitivity to transaction costs. By adjusting the parameter settings of the transaction costs in the model, we ﬁnd that the investment model is more sensitive to the transaction cost of bitcoin, that is, the transaction cost of bitcoin decreases by 1%, and the 5-year average annual investment rate of return increases by 1.75%. In addition, the model is more sensitive to lower transaction costs than to higher transaction costs. Finally, after multiple robustness tests, the investment model also performs well under diﬀerent transaction costs, all exceeding 90% of the simulated decisions.

<!-- b000013 | keywords | pages [1] -->
Keywords: ARIMA algorithm; NSGS-II algorithm; CVAR; downside semi-variance; multi

<!-- b000014 | prose | pages [1] -->
objective programming solution

<!-- b000015 | furniture | pages [2] -->
Team # 2218743

<!-- b000016 | furniture | pages [2] -->
Page 1 of 23

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction

<!-- b000019 | contents | pages [2] -->
3

<!-- b000020 | contents | pages [2] -->
1.1

<!-- b000021 | contents | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000022 | contents | pages [2] -->
3

<!-- b000023 | contents | pages [2] -->
1.2

<!-- b000024 | contents | pages [2] -->
The Flow Chart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
3

<!-- b000026 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000027 | contents | pages [2] -->
4

<!-- b000028 | contents | pages [2] -->
2.1

<!-- b000029 | contents | pages [2] -->
Assumptions

<!-- b000030 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
2.2

<!-- b000033 | contents | pages [2] -->
Notations

<!-- b000034 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
4

<!-- b000036 | contents | pages [2] -->
3 Data processing and analysis

<!-- b000037 | contents | pages [2] -->
4

<!-- b000038 | contents | pages [2] -->
3.1

<!-- b000039 | contents | pages [2] -->
Data Pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
4

<!-- b000041 | contents | pages [2] -->
3.2

<!-- b000042 | contents | pages [2] -->
Descriptive Statistical Analysis . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
5

<!-- b000044 | contents | pages [2] -->
4 Establishment and Application of Investment Strategy Model

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
4.1

<!-- b000047 | contents | pages [2] -->
Predicting Asset Prices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
6

<!-- b000049 | contents | pages [2] -->
4.1.1

<!-- b000050 | contents | pages [2] -->
Autoregressive Integrated Moving Average Model

<!-- b000051 | contents | pages [2] -->
. . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
6

<!-- b000053 | contents | pages [2] -->
4.1.2

<!-- b000054 | contents | pages [2] -->
Building Asset Price Forecasting Models

<!-- b000055 | contents | pages [2] -->
. . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
6

<!-- b000057 | contents | pages [2] -->
4.1.3

<!-- b000058 | contents | pages [2] -->
Results Analysis

<!-- b000059 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
8

<!-- b000061 | contents | pages [2] -->
4.2

<!-- b000062 | contents | pages [2] -->
Selecting Trading Dates Based on Market Conditions . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
9

<!-- b000064 | contents | pages [2] -->
4.2.1

<!-- b000065 | contents | pages [2] -->
Moving Average Long Arrangement Method

<!-- b000066 | contents | pages [2] -->
. . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
10

<!-- b000068 | contents | pages [2] -->
4.2.2

<!-- b000069 | contents | pages [2] -->
Building Trading Day Selection Model

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
10

<!-- b000072 | contents | pages [2] -->
4.2.3

<!-- b000073 | contents | pages [2] -->
Results Analysis

<!-- b000074 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
10

<!-- b000076 | contents | pages [2] -->
4.3

<!-- b000077 | contents | pages [2] -->
Measuring the Risk of Portfolio

<!-- b000078 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
11

<!-- b000080 | contents | pages [2] -->
4.3.1

<!-- b000081 | contents | pages [2] -->
Conditional Value at Risk (CVaR) . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
11

<!-- b000083 | contents | pages [2] -->
4.4

<!-- b000084 | contents | pages [2] -->
Finding the Best Investment Strategy . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [2] -->
12

<!-- b000086 | contents | pages [2] -->
4.4.1

<!-- b000087 | contents | pages [2] -->
Establishment of Optimization 0bjective Functions and Constraints

<!-- b000088 | contents | pages [2] -->
. .

<!-- b000089 | contents | pages [2] -->
12

<!-- b000090 | contents | pages [2] -->
4.4.2

<!-- b000091 | contents | pages [2] -->
Principle of NSGA-II Algorithm . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
13

<!-- b000093 | contents | pages [2] -->
4.4.3

<!-- b000094 | contents | pages [2] -->
Building Investment Decision Model

<!-- b000095 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
14

<!-- b000097 | contents | pages [2] -->
4.4.4

<!-- b000098 | contents | pages [2] -->
Results Analysis

<!-- b000099 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
15

<!-- b000101 | contents | pages [2] -->
5 Investment Strategy Optimality Test

<!-- b000102 | contents | pages [2] -->
16

<!-- b000103 | contents | pages [2] -->
5.1

<!-- b000104 | contents | pages [2] -->
Prediction Accuracy Test of Model . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
16

<!-- b000106 | contents | pages [2] -->
5.2

<!-- b000107 | contents | pages [2] -->
Eﬀectiveness Test of Investment Strategies . . . . . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
16

<!-- b000109 | furniture | pages [3] -->
Team # 2218743

<!-- b000110 | furniture | pages [3] -->
Page 2 of 23

<!-- b000111 | contents | pages [3] -->
5.2.1

<!-- b000112 | contents | pages [3] -->
Analyzing Critical Period of Investment . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [3] -->
16

<!-- b000114 | contents | pages [3] -->
5.2.2

<!-- b000115 | contents | pages [3] -->
Random Interference Method

<!-- b000116 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000117 | contents | pages [3] -->
17

<!-- b000118 | heading | pages [3] -->
6 Sensitivity Analysis of Investment Model

<!-- b000119 | prose | pages [3] -->
17

<!-- b000120 | prose | pages [3] -->
6.1 Market Risk Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000121 | prose | pages [3] -->
6.2 Sensitivity Analysis and Robustness Test . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000122 | prose | pages [3] -->
6.2.1 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000123 | prose | pages [3] -->
6.2.2 Robustness Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000124 | heading | pages [3] -->
7 Model Evaluation

<!-- b000125 | prose | pages [3] -->
20

<!-- b000126 | prose | pages [3] -->
7.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

<!-- b000127 | prose | pages [3] -->
7.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

<!-- b000128 | heading | pages [3] -->
Memorandum

<!-- b000129 | prose | pages [3] -->
21

<!-- b000130 | heading | pages [3] -->
Reference

<!-- b000131 | references | pages [3] -->
23

<!-- b000132 | furniture | pages [4] -->
Team # 2218743

<!-- b000133 | furniture | pages [4] -->
Page 3 of 23

<!-- b000134 | heading | pages [4] -->
1 Introduction

<!-- b000135 | heading | pages [4] -->
1.1 Problem Restatement

<!-- b000136 | prose | pages [4] -->
People are always looking for good investment methods to improve their asset status, and when faced with investment decisions, market traders must seek the best opportunity to invest. In order to maximize returns and diversify risks, traders often invest in multiple assets, forming a portfolio. For any investment portfolio, how to balance the two indicators of portfolio expected return and risk for asset allocation is the core problem that needs to be solved. The famous American economist Harry Markowitz systematically put forward the Portfolio Theory in 1952. On the basis of some assumptions, he established a mean-variance model of optimal asset allocation. This provides a theoretical basis for investors to ﬁnd the best asset allocation ratio and achieve the best eﬃciency of the investment portfolio.

<!-- b000137 | prose | pages [4] -->
First, in this case, we need to develop a mathematical model for traders investing in both assets based on the past stream of daily prices of gold and bitcoin, which can provide the optimal daily portfolio investment strategy for ﬁve years. According to the idea of Portfolio Theory, we must comprehensively consider the beneﬁts and risks, and the impact of the commission for transaction of bitcoin and gold on the investment strategy should also be taken into account.

<!-- b000138 | prose | pages [4] -->
Second, in order to build traders’ conﬁdence in our model, we need to demonstrate in some way that the strategy provided by our model is the most eﬀective. Then, as commission for transaction is one of the important factors aﬀecting investment decisions, we need to ﬁnd a sensitivity test method to measure the sensitivity of transaction costs to model results.

<!-- b000139 | prose | pages [4] -->
Finally, we need to provide traders with a memorandum of less than two pages showing the results of our work, including our model, the investment strategy derived from the model, and an analysis of the results.

<!-- b000140 | heading | pages [4] -->
1.2 The Flow Chart

<!-- b000141 | prose | pages [4] -->
The ﬂow chart of the work in this paper is shown as follows.

<!-- b000142 | caption | pages [4] -->
Figure 1: The ﬂow chart of our work.

<!-- b000143 | furniture | pages [5] -->
Team # 2218743

<!-- b000144 | furniture | pages [5] -->
Page 4 of 23

<!-- b000145 | heading | pages [5] -->
2 Assumptions and Notations

<!-- b000146 | heading | pages [5] -->
2.1 Assumptions

<!-- b000147 | prose | pages [5] -->
In order to facilitate the establishment of the optimal investment strategy model, we make the following assumptions and simpliﬁcations according to the actual situation and classical theory:

<!-- b000148 | prose | pages [5] -->
• Assuming that volatile assets such as gold and bitcoin are not allowed for short-sell transactions.

<!-- b000149 | prose | pages [5] -->
• Assuming that traders are not allowed to borrow USD during the investment process.

<!-- b000150 | prose | pages [5] -->
• Assuming that the rate of return on cash is always 0.

<!-- b000151 | prose | pages [5] -->
• Assuming that traders are all risk averters. When faced with two alternatives, and other things are equal, they will choose the portfolio with less risk.

<!-- b000152 | prose | pages [5] -->
• Assuming that traders are never satisﬁed. When faced with two alternatives, and other things are equal, they will choose the portfolio with the higher expected rate of return.

<!-- b000153 | prose | pages [5] -->
• Assuming that gold, bitcoin and USD are inﬁnitely divisible.

<!-- b000154 | prose | pages [5] -->
• Assuming that market information is open and transparent, and traders can obtain various information at the same time.

<!-- b000155 | heading | pages [5] -->
2.2 Notations

<!-- b000156 | prose | pages [5] -->
In this work, we use the nomenclature in Table 1 in the model construction. Other nonefrequent-used symbols will be introduced once they are used.

<!-- b000157 | caption | pages [5] -->
Table 1: Notations used in this literature.

<!-- b000158 | prose | pages [5] -->
Symbol Deﬁnition Unit

<!-- b000159 | prose | pages [5] -->
The price of gold on day t U.S. dollars gt The forecast price of gold on day T U.S. dollars Gt The price of bitcoin on day t U.S. dollars bt The forecast price of bitcoin on day T U.S. dollars Bt The amount of cash in the portfolio on day t U.S. dollars xt Amount of gold in the portfolio on day t troy ounces yt The amount of bitcoin in the portfolio on day t bitcoins zt The actual return of the portfolio on day t U.S. dollars It The transaction cost rate of gold / αgold The transaction cost rate of bitcoin / αbitcoin

<!-- b000160 | heading | pages [5] -->
3 Data processing and analysis

<!-- b000161 | heading | pages [5] -->
3.1 Data Pre-processing

<!-- b000162 | prose | pages [5, 6] -->
First of all, we observe that there are 10 missing values in the gold price data. The dates corresponding to the missing values are the working day or the previous working day on Christmas Eve and New Year’s Eve every year. Based on the actual situation, we consider the date on which the missing value occurs as the date when the gold market is closed. For the convenience of data analysis, we set the gold price corresponding to the date when the gold market is closed as the gold price of the previous day.

<!-- b000163 | furniture | pages [6] -->
Team # 2218743

<!-- b000164 | furniture | pages [6] -->
Page 5 of 23

<!-- b000166 | heading | pages [6] -->
3.2 Descriptive Statistical Analysis

<!-- b000167 | prose | pages [6] -->
Based on the data given, we analyze the data by statistical methods and drew the following statistical graphs. It can be seen from Figure 2 and Figure 3 that the prices of gold and Bitcoin have changed greatly in the past ﬁve years, and especially the price of Bitcoin has changed more dramatically. The range for sequence {bt} is $62960.36 and the range for sequence {gt} is $941.45.

<!-- b000168 | caption | pages [6] -->
Figure 2: Time series plot of gold price sequence {gt}.

<!-- b000169 | caption | pages [6] -->
Figure 3: Time series plot of bitcoin price sequence {bt}.

<!-- b000170 | caption | pages [6] -->
Figure 4 depict the year-to-year changes in the standard deviation and Pearson correlation

<!-- b000171 | prose | pages [6] -->
coeﬃcient of gold and bitcoin prices. We can see that the standard deviation of the sequence {bt} is much larger than that of the sequence {gt} , and the absolute value of the correlation coeﬃcient is relatively large. This shows that the price of Bitcoin ﬂuctuates more violently, and there is a strong correlation between the price of Bitcoin and gold.

<!-- b000172 | furniture | pages [7] -->
Team # 2218743

<!-- b000173 | furniture | pages [7] -->
Page 6 of 23

<!-- b000174 | prose | pages [7] -->
(a) Standard deviation.

<!-- b000175 | prose | pages [7] -->
(b) Correlation coeﬃcient.

<!-- b000176 | caption | pages [7] -->
Figure 4: Line graphs of standard deviation and correlation coeﬃcient of sequence {bt} and

<!-- b000177 | prose | pages [7] -->
{gt}.

<!-- b000178 | heading | pages [7] -->
4 Establishment andApplication of Investment Strategy Model

<!-- b000179 | heading | pages [7] -->
4.1 Predicting Asset Prices

<!-- b000180 | prose | pages [7] -->
The Autoregressive Integrated Moving Average model is a model that analyzes the dynamic changes of time series variables based on AR and MA models, and is often used in ﬁnancial data mining. The ARIMA model describes the short-term memory of sequences based on the autocorrelation of time-series data, and therefore has short-term predictive properties. According to the relevant situation of this example, after comprehensively considering various time series analysis models, we choose the ARIMA model to analyze and predict the prices of bitcoin and gold.

<!-- b000181 | heading | pages [7] -->
4.1.1 Autoregressive Integrated Moving Average Model

<!-- b000182 | prose | pages [7] -->
In the ARIMA( p, d, q) model, d is the number of diﬀerences made to change the time series into a stationary series, p is the lag order of the sequence, and q is the lag order of the random error term. The principle of the model is to convert the non-stationary sequence {rt} into a stationary sequence {rt} through d-order diﬀerence, and then use rt as the dependent variable, the lag term of rt and random error term at and the lag term of at as independent variables, and make a regression.

<!-- b000183 | heading | pages [7] -->
4.1.2 Building Asset Price Forecasting Models

<!-- b000184 | prose | pages [7] -->
1. Sequence stationary ( determine parameter d) :

<!-- b000185 | prose | pages [7] -->
First, we perform a stationarity test on the price series {gt} and {bt} of gold and bitcoin. It can be seen from the Figure 2, Figure 3, and Figure 5 below that the two time series have obvious trends, and the decay speed of the autocorrelation coeﬃcient is relatively slow. At the same time, we also conduct a Unit Root Test, and there are unit roots in these two series. Therefore gt and bt are non-stationary series and need to be further diﬀerentiated.

<!-- b000186 | furniture | pages [8] -->
Team # 2218743

<!-- b000187 | furniture | pages [8] -->
Page 7 of 23

<!-- b000188 | prose | pages [8] -->
(a) Gold price sequence {gt}. (b) Bitcoin price sequence {bt}.

<!-- b000189 | caption | pages [8] -->
Figure 5: Autocorrelation plots of gold price sequence and bitcoin price sequence.

<!-- b000190 | prose | pages [8] -->
Let gt = gt −gt−1 and bt = bt −bt−1. After taking the ﬁrst-order diﬀerence, we perform a stationarity test on {gt}, {bt}. From the Figure 6 and Figure 7 below, we can observe that the two sequences after diﬀerence always ﬂuctuate randomly around a certain value, and there is no obvious trend. The autocorrelation coeﬃcient decays rapidly, and only closely spaced sequences values have a signiﬁcant eﬀect. At the same time, the p-values of the unit root test are all close to 0. Thus, there is no unit root. So {gt} and {bt} are stationary sequences. Since we performed a ﬁrst-order diﬀerence method to obtain a stationary series, d = 1.

<!-- b000191 | prose | pages [8] -->
(a) Sequence {gt}. (b) Sequence {bt}.

<!-- b000192 | caption | pages [8] -->
Figure 6: Time series plots of sequence {gt} and sequence {bt}.

<!-- b000193 | prose | pages [8] -->
(a) Sequence {gt}. (b) Sequence {bt}.

<!-- b000194 | caption | pages [8] -->
Figure 7: Autocorrelation plots of sequence {gt} and sequence {bt}.

<!-- b000195 | prose | pages [8] -->
2. Determination of order p, q:

<!-- b000196 | furniture | pages [9] -->
Team # 2218743

<!-- b000197 | furniture | pages [9] -->
Page 8 of 23

<!-- b000198 | prose | pages [9] -->
The ARIMA( p, d, q) model has the form:

<!-- b000199 | prose | pages [9] -->
rt = rt −rt−1,

<!-- b000200 | prose | pages [9] -->
p q X X φirt−i + at − rt = φ0 + θiat−i, i=1 i=1 where {at} is a white noise sequence and both p and q are non-negative integers.

<!-- b000201 | prose | pages [9] -->
The Bayesian Information Criterion (BIC) is an information criterion function that can be used to determine the optimal order of a model, and is constructed based on a Likelihood function. According to the historical data, we calculate the BIC value of the model under diﬀerent orders through the computer programming loop, and ﬁnd the order p and q that make the BIC the smallest, that is, the optimal order of the model. After determining the optimal order, we perform parameter estimation, and then calculate the predicted prices Gt and Bt of gold and bitcoin on day t.

<!-- b000202 | prose | pages [9] -->
3. Residual test:

<!-- b000203 | prose | pages [9] -->
In order to determine the validity of the model, a residual test is also required, in which a white noise veriﬁcation is needed for the residual sequence {ˆat}. If the residuals are randomly and normally distributed and have no autocorrelation, it means that the residual sequence approximates a white noise sequence, indicating that the model ﬁtting eﬀect is great. We use the Ljung-Box statistic Q(m) to test the proximity to a white noise:

<!-- b000204 | prose | pages [9] -->
m ˆρ2 X l Q(m) = T(T + 2) T −l. l=1

<!-- b000205 | prose | pages [9] -->
When the p-value of the test is greater than 0.05, it means that the residual sequence {ˆat} passes the test at the 5% conﬁdence level, and the model is suﬃcient for modeling the dynamic linear dependence of the data.

<!-- b000206 | heading | pages [9] -->
4.1.3 Results Analysis

<!-- b000207 | caption | pages [9] -->
Figure 8 shows that the p-values of the residual test of the models at diﬀerent times are all

<!-- b000208 | prose | pages [9] -->
greater than 0.01 and most of the p-values are greater than 0.05, all of which pass the white noise test of the residuals. This is the premise that we use the ARIMA model for daily price forecasts.

<!-- b000209 | prose | pages [9] -->
(a) Gold price sequence. (b) Bitcoin price sequence.

<!-- b000210 | caption | pages [9] -->
Figure 8: Time series plots of P value of ARIMA model based on gold price sequence and

<!-- b000211 | prose | pages [9] -->
bitcoin price sequence.

<!-- b000212 | furniture | pages [10] -->
Team # 2218743

<!-- b000213 | furniture | pages [10] -->
Page 9 of 23

<!-- b000214 | caption | pages [10] -->
Figure 9 and Figure 10 shows that the predicted price curve coincides with the actual price

<!-- b000215 | prose | pages [10] -->
curve basically, the ﬂuctuation trend remains the same, and the diﬀerence between the predicted price and the actual price is not large. Among them, the prediction accuracy is very high in the period of stable price ﬂuctuation. In the bull and bear market period, the model can accurately predict the key turning point, but there is a certain prediction error. our forecasting model can achieve good forecasting results.

<!-- b000216 | caption | pages [10] -->
Figure 9: Time series plot of forecast gold price, actual gold price and the diﬀerence between

<!-- b000217 | prose | pages [10] -->
the two.

<!-- b000218 | caption | pages [10] -->
Figure 10: Time series plot of forecast bitcoin price, actual bitcoin price and the diﬀerence

<!-- b000219 | prose | pages [10] -->
between the two.

<!-- b000220 | heading | pages [10] -->
4.2 Selecting Trading Dates Based on Market Conditions

<!-- b000221 | prose | pages [10] -->
In this example, since there is a 1%-2% transaction commission in the process of volatile assets trading, frequent trading will increase the transaction cost, and we believe that market traders should choose the trading day more carefully. According to the diﬀerent market condi- tions, it can be divided into trend market and shock market. Trend market can be divided into two types: bull market (trend up) and bear market (trend down). When there is no obvious price increase or price decrease trend, that is, when the market is in a volatile market, traders should choose not to trade, considering the size of transaction costs. Traders should only trade when there is a clear upward or downward trend in the price of the volatile assets, i.e. in a bull or bear market. Using this method, we can avoid the problem of high long-term transaction costs caused by maximizing short-term returns and ignoring transaction costs when making investment decisions.

<!-- b000222 | furniture | pages [11] -->
Team # 2218743

<!-- b000223 | furniture | pages [11] -->
Page 10 of 23

<!-- b000224 | heading | pages [11] -->
4.2.1 Moving Average Long Arrangement Method

<!-- b000225 | prose | pages [11] -->
The moving average long arrangement method is a commonly used method that can eﬀectively judge the market state. We use this method to judge the price trend, and then choose the appropriate trading day.

<!-- b000226 | prose | pages [11] -->
The principle of the moving average long arrangement method is to draw moving averages with diﬀerent periods, that is, MA5, MA10, MA60, etc. Among them, taking MA5 as an example, the moving average represents the arithmetic average of the price in the last 5 days. With the appearance of a new trading day, the average array moves forward day by day, adding the price of the new trading day to the array, and removing the 6th closing price from the previous countdown. And we average the new average array, ultimately forming a moving average. When multiple moving averages show an upward trend, and the shorter the period is, the higher the position of the moving average, the volatile assets are considered to be in a bull market; on the contrary, when multiple moving averages show a downward trend, and the shorter the period is, the lower the position of the moving average, the volatile assets are considered to be in a bear market.

<!-- b000227 | heading | pages [11] -->
4.2.2 Building Trading Day Selection Model

<!-- b000228 | prose | pages [11] -->
When judging with the arrangement of moving averages, traders need to independently choose moving averages that cover a larger range. Given that traders are more focused on short-term gains, we set the moving averages to be more dense on shorter date ranges. Namely: 5th, 7th, 10th, 13th, 16th, 20th, 25th, 30th, 60th, 120th.

<!-- b000229 | prose | pages [11] -->
If there is a complete long arrangement of the moving averages, that is, MA5 > MA7 > MA10 > MA13 > · · · > MA120, and the slopes of the 10 moving averages are all positive, it indicates that the price will rise sharply and enter a bull market. However, considering that the complete long arrangement is relatively rare, we assume that when the slopes of the 8 moving averages are positive, there will be an upward price trend in the market. The moving average short arrangement is the same.

<!-- b000230 | heading | pages [11] -->
4.2.3 Results Analysis

<!-- b000231 | prose | pages [11] -->
Bringing in the daily prices of gold andbitcoin, the judgment results of bull market and bear market are as follows:

<!-- b000232 | caption | pages [11] -->
Figure 11: Bull and bear market judgment chart of gold price.

<!-- b000233 | furniture | pages [12] -->
Team # 2218743

<!-- b000234 | furniture | pages [12] -->
Page 11 of 23

<!-- b000235 | caption | pages [12] -->
Figure 12: Bull and bear market judgment chart of bitcoin price.

<!-- b000236 | caption | pages [12] -->
Figure 11 and Figure 12 show that the bull and bear market distributions of gold and

<!-- b000237 | prose | pages [12] -->
Bitcoin are inconsistent, that is, the buying and selling nodes of volatile assets are diﬀerent. The discontinuity indicates that the market does not present an obvious buying and selling opportunity, and market traders will not have trading behavior. Based on the results, we get indicators describing the state of the gold and bitcoin markets: Mt and Nt.

<!-- b000238 | prose | pages [12] -->
( The gold market is in a bull or bear market. 1 Mt = Others. 0

<!-- b000239 | prose | pages [12] -->
( The bitcoin market is in a bull or bear market. 1 Nt = Others. 0

<!-- b000240 | prose | pages [12] -->
Then when Mt = 0, our investment decision should not conduct gold transactions, and similarly when Nt = 0, we should not conduct bitcoin transactions.

<!-- b000241 | heading | pages [12] -->
4.3 Measuring the Risk of Portfolio

<!-- b000242 | prose | pages [12] -->
In order to make the best investment decisions, we must consider the risk of our asset portfolio. Choosing an appropriate method to measure portfolio risk is the key.Considering that the use of variance and β coeﬃcient to measure risk is not intuitive, and it only reﬂects the volatility of the market (or assets), we choose to use the CVaR method to measure the risk of the portfolio, which is a risk measurement method based on VaR.

<!-- b000243 | heading | pages [12] -->
4.3.1 Conditional Value at Risk (CVaR)

<!-- b000244 | prose | pages [12, 13] -->
The VaR method is used to estimate the worst loss condition of the assets held under a given conﬁdence level, that is, the maximum loss value. Since VaR cannot satisfy sub-additivity in asset diversiﬁcation and the measurement of tail losses is not suﬃcient, Uryasev and Rockafellar further proposed a conditional value-at-risk (CVaR) to overcome these defects. CVaR measures the average loss value of the investment portfolio under the condition that the loss exceeds a given VaR value, which can improve the intuitive impression for traders, and is also in line with the worst-case expectations that traders assign to assets when making transactions. At the same time, it not only satisﬁes the properties of consistent risk measurement, but also has good properties such as convexity.Under the assumption that returns r follow a normal distribution, the formula for calculating CVaR is as follow:

<!-- b000245 | furniture | pages [13] -->
Team # 2218743

<!-- b000246 | furniture | pages [13] -->
Page 12 of 23

<!-- b000248 | prose | pages [13] -->
2πexp{[φ−1(α)]2 1 1    √ CV aR = C(α)σ(r) −E(r) = } σ(r) −E(r), 1 −α 2 where α is the signiﬁcance level, E(r) is the expected value of r and σ is the standard deviation of r.

<!-- b000249 | heading | pages [13] -->
4.4 Finding the Best Investment Strategy

<!-- b000250 | prose | pages [13] -->
In order to get the optimal investment strategies, we need to comprehensively consider the returns and risks of the asset portfolio. In order to achieve the decision goals of maximizing returns and minimizing risks at the same time, we build a model for trading strategy based on the multi-objective NSGA-II algorithm, and calculate the feasible solution set of the daily asset portfolio. Ultimately, we take into account the risk aversion of market traders and use the limitation of downside semi-variance to obtain the ﬁnal daily trading strategy. By iterating through a day-by-day loop, we end up with daily transactions for ﬁve years.

<!-- b000251 | heading | pages [13] -->
4.4.1 Establishment of Optimization 0bjective Functions and Constraints

<!-- b000252 | prose | pages [13] -->
Due to the premise that traders are all risk averter, when traders make strategic decisions, they pursue proﬁt maximization and their trading decisions are limited by risks. Therefore, we set two objective functions.

<!-- b000253 | prose | pages [13] -->
1. The ﬁrst objective function: Maximum of expected investment proﬁt (eIt):

<!-- b000254 | prose | pages [13] -->
It is known that the asset allocation held on day t-1 is [xt−1, yt−1, zt−1], the prices of gold and bitcoin are gt−1, bt−1 respectively. And the asset allocation held on day t is [xt, yt, zt], and the predicted prices of gold and bitcoin are Gt, Bt. Among them, [xt, yt, zt] are optimization parameters.

<!-- b000255 | prose | pages [13] -->
Thus, the traders’s expected proﬁt eIt can be expressed as:

<!-- b000256 | prose | pages [13] -->
eIt = −1%|yt −yt−1|Gt −2%|zt −zt−1|Bt + (Gt −gt−1)yt + (Bt −bt−1)zt.

<!-- b000257 | prose | pages [13] -->
2. The second objective function: Minimum of investment risk (CVaR):

<!-- b000258 | prose | pages [13] -->
First, we deﬁne the weight vector of asset portfolio as:

<!-- b000259 | prose | pages [13] -->
Wt = (w1,t, w2,t, w3,t)T,

<!-- b000260 | prose | pages [13] -->
xt ytGt ztBt w1,t = , w2,t = , w3,t = . xt + ytGt + ztBt xt + ytGt + ztBt xt + ytGt + ztBt

<!-- b000261 | prose | pages [13] -->
Next, we deﬁne vector µt as:

<!-- b000262 | prose | pages [13] -->
µt = (µ1,t, µ2,t, µ3,t)T,

<!-- b000263 | prose | pages [13] -->
µi,t = ri,1 + ri,2 + · · · + ri,t−1 . t −1

<!-- b000264 | prose | pages [13] -->
The, we deﬁne the matrix Ct as:

<!-- b000265 | furniture | pages [14] -->
Team # 2218743

<!-- b000266 | furniture | pages [14] -->
Page 13 of 23

<!-- b000267 | prose | pages [14] -->
σ2 σ2 σ2   1,t 12,t 13,t σ2 σ2 σ2 Ct = , 21,t 2,t 23,t  σ2 σ2 σ2 31,t 3,t 33,t

<!-- b000268 | prose | pages [14] -->
t−1 1 X σ2 σ2 (ri,k −µi,t), i,t = ij,t = σi,tσj,tρij. t −2 k=1

<!-- b000269 | prose | pages [14] -->
In the above formulas, ri,t is the actual rate of return of asset i, σ2 i,t is the variance of the rate of return of asset i, and σ2 ij,t is the covariance of the rate of return of asset i and the rate of return of asset i.

<!-- b000270 | prose | pages [14] -->
Therefore, combined with the deﬁnition of CVaR, we can express the CVaR of asset portfolio:

<!-- b000271 | prose | pages [14] -->
q t CtWt −(W T W T CV aR = C(α) t µt), 2πexp{[φ−1(α)]2 1 1    √ } C(α) = . 1 −α 2

<!-- b000272 | prose | pages [14] -->
3. Constraint functions:

<!-- b000273 | prose | pages [14] -->
In particular, in the bull and bear market judgment model, we get the dataMt, Nt representing the market state. When the gold price is in a bull or bear market, we choose to trade gold; otherwise, we do not trade gold and keep our gold holdings. The same is true for the bitcoin price. The speciﬁc performance is as follow:

<!-- b000274 | prose | pages [14] -->
 yt = yt, zt = zt Mt = 1, Nt = 1    yt = yt, zt = zt−1 Mt = 1, Nt = 0  . yt = yt−1, zt = zt Mt = 0, Nt = 1    yt = yt−1, zt = zt−1 Mt = 0, Nt = 0 

<!-- b000275 | prose | pages [14] -->
At the same time, since there is no short-selling behavior in volatile assets, the holdings of gold and bitcoin in asset allocation are required to be no less than 0. In addition, we set that traders can only invest with the initial $1,000 and do not allow borrowing for daily transaction, that is, the cash held after each transaction is not less than 0. Thus, the optimization parameters are constrained as follows:

<!-- b000276 | prose | pages [14] -->
 xt = xt−1 −1%|yt −yt−1|Gt −2%|zt −zt−1|Bt −(yt −yt−1)Gt −(zt −zt−1)Bt ≥0   . yt ≥0  zt ≥0 

<!-- b000277 | heading | pages [14] -->
4.4.2 Principle of NSGA-II Algorithm

<!-- b000278 | prose | pages [14, 15] -->
The NSGA-II algorithm, a fast non-dominated multi-objective optimization algorithm with an elite retention strategy, is a multi-objective optimization algorithm based on the Pareto optimal solution. Because the algorithm can achieve multiple objectives, and can perform great in both the diversity and convergence of the solution set distribution, we choose this algorithm to solve the problem. The speciﬁc implementation process is as follows:

<!-- b000279 | furniture | pages [15] -->
Team # 2218743

<!-- b000280 | furniture | pages [15] -->
Page 14 of 23

<!-- b000282 | prose | pages [15] -->
(1) Randomly generate the initialized population of individuals, judge the hierarchical ordering of all individuals, and perform non-dominant ordering on unﬁnished individuals.

<!-- b000283 | prose | pages [15] -->
Among them, the dominance relationship refers to the Pareto dominance relationship: For the minimization multi-objective optimization problem, for n objective components fi(x),i = 1, 2, · · · , n, two decision variables Xa, Xb are given arbitrarily, if the following two conditions are true, then Xa dominates Xb.

<!-- b000284 | prose | pages [15] -->
1. ∀i ∈1, 2, · · · , n, fi(Xa) ≤fi(Xb)

<!-- b000285 | prose | pages [15] -->
2. ∃i ∈1, 2, · · · , n, s.t. fi(Xa) < fi(Xb) (2) The genetic operations of selection, crossover, and mutation are performed on the parent population, and the individual genes are genetically recombined into new individuals to generate the oﬀspring population.

<!-- b000286 | prose | pages [15] -->
(3) Combine the parent population and the oﬀspring population to generate a new population, quickly sort the new population non-dominated, calculate the crowding distance of each indi- vidual on non-dominated layer, and select the best individual to form a new parent population. Among them, the smaller the crowding distance of individuals, the denser the non-dominated individuals, and the poorer the diversity of individuals. Thus, they are eliminated.

<!-- b000287 | prose | pages [15] -->
(4) Algorithm iterates from this, and when the number of iterations reaches the expected setting, it terminates.

<!-- b000288 | heading | pages [15] -->
4.4.3 Building Investment Decision Model

<!-- b000289 | prose | pages [15] -->
According to objective function and constraint conditions, we ﬁrst use NSGA-II algorithm to achieve multi-objective programming solution, and obtain feasible solution set. As the expected return increases, the conditional value at risk (CVaR) increases. To further our ﬁnal decision, we use the downside semi-variance limitations to make the ﬁnal decision based on the feasible set. Considering the fact that investors believe that situations where actual returns are higher than average returns cannot be included in the investment risk, Markowitz proposed the method of the downside semi-variance, which solves the problem of diﬀerent investors’ preference structures to a certain extent. We believe that investors have an upper limit on their acceptance of the risk of falling returns, but there is no upper limit on their acceptance of the risk of rising returns. Therefore, we use the downside semi-variance model to optimize the risk measure to limit the risk of falling portfolio returns and get the optimal investment portfolio based on the model.

<!-- b000290 | prose | pages [15] -->
Therefore, we bring the corresponding asset allocation [xt, yt, zt] in the feasible solution into the downside semi-variance model, and solve the downside semi-variance V .

<!-- b000291 | prose | pages [15] -->
V = W TC−W T.

<!-- b000292 | prose | pages [15, 16] -->
σ2− σ2− σ2−   1,t 12,t 13,t σ2− σ2− σ2− C−= . 21,t 2,t 23,t  σ2− σ2− σ2− 31,t 3,t 33,t ( (ri,t −µi,t)2 (ri,t −µi,t) ≤0 σ2− i,t = (ri,t −µi,t) > 0 . 0

<!-- b000293 | furniture | pages [16] -->
Team # 2218743

<!-- b000294 | furniture | pages [16] -->
Page 15 of 23

<!-- b000296 | prose | pages [16] -->
( (ri,t −µi,t)2 (ri,t −µi,t) > 0 σ2+ i,t = (ri,t −µi,t) ≤0 . 0

<!-- b000297 | prose | pages [16] -->
σ2− i,t σ2+ σ2+ i,t σ2− ij,t = σ2− i,t σ2− j,t j,t j,t + + 2 2 σ2− σij,t. σ2 i,tσ2 j,t

<!-- b000298 | prose | pages [16] -->
We sort the solved downside semi-variance from smallest to largest, set the 70% quantile as the daily risk limit, and take asset portfolio under the risk limit as the best investment strategy. That means, under the condition of constraining the upper limit of risk, we select the asset allocation with the largest investment return, and then proceed to the next iterative loop solution based on the solution.

<!-- b000299 | heading | pages [16] -->
4.4.4 Results Analysis

<!-- b000300 | caption | pages [16] -->
Figure 13 depicts daily gold and bitcoin holdings (measured in U.S. dollars) based on an

<!-- b000301 | prose | pages [16] -->
investment strategy based on our model. We can see that This strategy comprehensively considers the characteristics of bitcoin and gold, and chooses to buy a lot when bitcoin is at a low level, reducing the proportion of gold assets. When the downside risk of bitcoin increases, choose to hold a large amount of gold to hedge the risk, and when the risk of both assets is high, choose to hold more cash, so as to reduce the risk while maintaining a larger return. For example, in the bitcoin bull market from 2020 to 2021, the proportion of bitcoin assets is much larger than that of gold. In the bear market, the proportion of gold assets will increase rapidly to reduce risks. The cumulative return rate of the investment strategy given by this model during 2016-2021 is shown in Figure 14. According to the ﬁnal investment decision, the total assets will reach $617,643.2 after ﬁve years, and the average annual rate of return will reach 261.41% within ﬁve years. Among them, the annual yield in the second year is the largest, which is 664.69%.

<!-- b000302 | caption | pages [16] -->
Figure 13: Time series plot of gold and bitcoin holdings (measured in U.S. dollars).

<!-- b000303 | furniture | pages [17] -->
Team # 2218743

<!-- b000304 | furniture | pages [17] -->
Page 16 of 23

<!-- b000305 | caption | pages [17] -->
Figure 14: Time series plot of cumulative return (%) from 2016 to 2021

<!-- b000306 | heading | pages [17] -->
5 Investment Strategy Optimality Test

<!-- b000307 | prose | pages [17] -->
In order to prove that the strategy provided by our model is the optimal strategy, we will analyze and prove it from the perspectives of prediction accuracy and strategy eﬀectiveness.

<!-- b000308 | heading | pages [17] -->
5.1 Prediction Accuracy Test of Model

<!-- b000309 | prose | pages [17] -->
In terms of prediction accuracy, we use ﬁve common indicators to evaluate the prediction results of ARIMA to analyze the deviation between the predicted value of volatile assets’ price and the real value. The MSE, RMSE, MAE, MAPE and R2-score results calculated by python are shown in the Table 2 below.

<!-- b000310 | caption | pages [17] -->
Table 2: Prediction error evaluation index results.

<!-- b000311 | prose | pages [17] -->
Assets MSE RMSE MAE MAPE R2-score

<!-- b000312 | prose | pages [17] -->
Gold 395.8478 19.8959 13.6976 0.009 0.9486 Bitcoin 1205107.406 1097.7738 542.9281 0.0402 0.9486

<!-- b000313 | prose | pages [17] -->
The prediction results for gold and bitcoin price show that the MAPE values are both less than 0.1, which are extremely close to 0%, indicating that the model is close to perfect. R2-score values are greater than 94%, which are close to 1, reﬂecting that all the variance of the predicted value can be explained by the actual value. This shows that the model can accurately predict the moment when the market price ﬂuctuates greatly, thus providing a good precondition for us to make subsequent investment strategies.

<!-- b000314 | heading | pages [17] -->
5.2 Eﬀectiveness Test of Investment Strategies

<!-- b000315 | prose | pages [17] -->
In terms of the eﬀectiveness of investment strategies, we use the method of analyzing critical period of investment and the method of applying random interference to test and analyze.

<!-- b000316 | heading | pages [17] -->
5.2.1 Analyzing Critical Period of Investment

<!-- b000317 | prose | pages [17, 18] -->
First, taking the period from November 2020 to April 14, 2021 as an example, Bitcoin was in a bull market with an increase of 360.2%. According to the investment strategy we gave, buy gold in the early stage of the bull market and hold it to rise. During this period, the total investment return rate reached 314.3%, and the proﬁtability was high, which made a good grasp of the proﬁt opportunities brought by this opportunity.

<!-- b000318 | furniture | pages [18] -->
Team # 2218743

<!-- b000319 | furniture | pages [18] -->
Page 17 of 23

<!-- b000321 | prose | pages [18] -->
(a) Bull market ( 2020.11-2021.4). (b) Bear market ( 2021.4-2021.7).

<!-- b000322 | caption | pages [18] -->
Figure 15: Time series plots of cumulative returns in a bull market ( 2020.11-2021.4) and a

<!-- b000323 | prose | pages [18] -->
bear market ( 2021.4-2021.7).

<!-- b000324 | prose | pages [18] -->
From April 15, 2021 to July 2021, bitcoin was in a bear market and its prices fell sharply. We can accurately predict the coming of the bear market and make quick decisions to sell bitcoin and hold more gold and cash. Consequently, the total rate of return on investment during this period has been maintained at -3%. After testing, our investment model has the ability to survive the period of bear market smoothly, has a high ability to resist risk ﬂuctuations, and can keep asset losses to a minimum.

<!-- b000325 | heading | pages [18] -->
5.2.2 Random Interference Method

<!-- b000326 | prose | pages [18] -->
The random interference method is based on the our optimal investment strategy, and applies stochastic disturbance to the gold, bitcoin and cash holdings of each day in ﬁve years, generating M groups of new simulated investment strategies. Then, we compare the M groups of investment strategies with actual investment strategies in the ﬁve-year total return and the annual return for each year. The holding amount after random disturbance is set as a random number within 10% of the gold holding amount and the bitcoin holding amount, and the cash holding amount is determined according to the gold holding amount and the bitcoin holding amount after the disturbance. Also, it is necessary to ensure that the cash holdings >0.

<!-- b000327 | prose | pages [18] -->
 (1 −10%)yt < yt + εt < (1 + 10%)yt   . (1 −10%)zt < zt + εt < (1 + 10%)zt  xt = xt−1 −1%|yt −yt−1|Gt −2%|zt −zt−1|Bt −(yt −yt−1)Gt −(zt −zt−1)Bt ≥0 

<!-- b000328 | prose | pages [18] -->
From Table 3, the average annual rate of return on simulated investment is lower than that of actual investment, and the average total rate of return within 5 years is lower by 20.96%. At the same time, only 7% of the simulated investment strategies have a 5-year total return higher than the actual investment strategies we give. The result indicates that our investment model has a good performance in the ﬁve-year period when the macroeconomic environment is constantly changing and ﬁnancial market risks are high, especially in market tracking ability, anti-risk ability, and earning ability.

<!-- b000329 | heading | pages [18] -->
6 Sensitivity Analysis of Investment Model

<!-- b000330 | prose | pages [18, 19] -->
Taking into account the changes in the macroeconomic environment from 2016 to 2021, the huge ﬂuctuations in the capital market and the subsequent changes in US trading regulations, we investment.

<!-- b000331 | furniture | pages [19] -->
Team # 2218743

<!-- b000332 | furniture | pages [19] -->
Page 18 of 23

<!-- b000333 | caption | pages [19] -->
Table 3: Comparison of the rate of return of new simulated investment and that of actual

<!-- b000335 | prose | pages [19] -->
I1st I2nd I3rd I4th I5th I1−5 year year year year year year

<!-- b000336 | prose | pages [19] -->
Actual investment 368.99% 664.69% 102.48% 55.60% 453.03% 261.41% Simulated investment 328.65% 610.85% 91.53% 49.61% 422.62% 240.45%

<!-- b000337 | prose | pages [19] -->
will conduct a targeted sensitivity analysis on the transaction cost parameters in the investment model to prove that the investment model can make corresponding adjustments to random ﬁnancial events and provide the optimal investment strategy.

<!-- b000338 | heading | pages [19] -->
6.1 Market Risk Analysis

<!-- b000339 | prose | pages [19] -->
From the overall analysis of the U.S. capital market, in November 2016, Trump was unex- pectedly elected, the dollar rose sharply, technology stocks and ﬁnancial stocks reversed, and the Federal Reserve raised interest rates by 25 basis points in December, which further promoted the dollar index to rise. At the end of 2017, the tax reform bill was passed, and the scope of inﬂuence gradually expanded from the bond market to the stock market, from the international market to the US stock market, from growth stocks to value stocks, and the S&P 500 index continued to rise. In 2018, under the combined inﬂuence of Sino-US trade frictions, the US mid-term elections and other factors, both the Nasdaq and the S&P entered a "technical bear market". In 2019, the U.S. 3-month and 10-year treasury yield curve inverted, which once triggered panic in the European and American markets and caused shocks in the global market. In 2020, aﬀected by the COVID-19 epidemic and the US election, investors have chosen to adjust their asset allocation and prefer low-risk assets. In addition, the deterioration of the US epidemic in 2021 will once again increase the risk of the stock market. Therefore, changes in the global ﬁnancial and economic environment, domestic macro-politics, and economic environment will all have a greater impact on the stock market. Then, the U.S. stock market will choose to change the cost of transaction to alleviate the impact on stock price trends.

<!-- b000340 | prose | pages [19] -->
Speciﬁcally, from the analysis of the gold market, the random short-term or long-short game will cause short-term ﬂuctuations in the gold price, and the mid-line market is determined by regional conﬂicts and geopolitics, which are diﬃcult to predict. In the long run, the dollar shows a depreciating trend, which continues to push up the price of gold. In the bitcoin market, the relationship between supply and demand greatly aﬀects the price of bitcoin. The negative price elasticity of demand allows the price of the bitcoin to continue to rise when it is high, but it also brings a huge risk of falling prices.

<!-- b000341 | prose | pages [19] -->
On the whole, there have been many changes in the international and domestic environment during the ﬁve years from 2016 to 2021, then transmitting to the stock market, which is speciﬁcally reﬂected in transaction costs. When the stock market is booming, transaction costs tend to increase, so it is important to examine the sensitivity of investment models to changes in transaction costs.

<!-- b000342 | heading | pages [19] -->
6.2 Sensitivity Analysis and Robustness Test

<!-- b000343 | heading | pages [19] -->
6.2.1 Sensitivity Analysis

<!-- b000344 | prose | pages [19, 20] -->
By increasing or decreasing the percentage of transaction cost, we adjust the transaction cost of bitcoin to 1%, 2%, and 3%, and the transaction cost of gold to 0.5%, 1%, and 1.5% respectively, run the investment model again under diﬀerent transaction costs. Finally, we analyze the results of strategy model and the range of changes in assets portfolio. The results are shown in the

<!-- b000345 | furniture | pages [20] -->
Team # 2218743

<!-- b000346 | furniture | pages [20] -->
Page 19 of 23

<!-- b000348 | caption | pages [20] -->
Table 4.

<!-- b000349 | caption | pages [20] -->
Table 4: Annual rate of return on investment under diﬀerent transaction costs.

<!-- b000350 | prose | pages [20] -->
Transaction Costs I1st I2nd I3rd I4th I5th I1−5 year year year year year year

<!-- b000351 | prose | pages [20] -->
αbitcoin=1%,αgold=0.5% 371.92% 712.55% 97.77% 57.37% 442.04% 263.93% αbitcoin=1%,αgold=1% 370.39% 710.64% 97.85% 56.36% 442.61% 263.16% αbitcoin=1%,αgold=1.5% 368.86% 708.71% 97.92% 55.33% 443.20% 262.37% αbitcoin=2%,αgold=0.5% 370.52% 666.76% 102.37% 56.66% 452.31% 262.20% αbitcoin=2%,αgold=1% 368.99% 664.69% 102.48% 55.60% 453.03% 261.41% αbitcoin=2%,αgold=1.5% 367.46% 662.60% 102.59% 54.54% 453.77% 260.62% αbitcoin=3%,αgold=0.5% 369.12% 620.69% 107.59% 55.89% 463.51% 260.44% αbitcoin=3%,αgold=1% 367.59% 618.46% 107.73% 54.79% 464.40% 259.63% αbitcoin=3%,αgold=1.5% 367.46% 662.60% 102.59% 54.54% 453.76% 260.61%

<!-- b000352 | prose | pages [20] -->
Obviously, when the transaction cost decreases, the annual rate of return increases, and the results of the investment model are more sensitive to the transaction cost of bitcoin. To be speciﬁc, when the transaction cost of bitcoin remains unchanged, the transaction cost of gold decreases by 0.5%, and the 5-year total rate of return increases by 0.79%. When the transaction cost of gold is unchanged, the transaction cost of bitcoin decreases by 1%, and the total 5-year return increases by 1.75%. In addition, when transaction costs rise, the annual rate of return falls, but its impact is smaller than the impact of lower transaction costs.The results are shown in the Table 5.

<!-- b000353 | caption | pages [20] -->
Table 5: Ranking of actual investment model performance under diﬀerent transaction costs.

<!-- b000354 | prose | pages [20] -->
Transaction Costs Rank

<!-- b000355 | prose | pages [20] -->
78 αbitcoin = 1%, αgold = 1% 66 αbitcoin = 1%, αgold = 0.5% 43 αbitcoin = 1%, αgold = 1.5% 6 αbitcoin = 2%, αgold = 0.5% 10 αbitcoin = 2%, αgold = 1.5% 17 αbitcoin = 3%, αgold = 0.5% 25 αbitcoin = 3%, αgold = 1% 56 αbitcoin = 3%, αgold = 1.5%

<!-- b000356 | prose | pages [20] -->
The performance rankings of the investment models are all in the top 10%, indicating that our models also perform well under diﬀerent transaction costs and are worthy of trust.

<!-- b000357 | heading | pages [20] -->
6.2.2 Robustness Test

<!-- b000358 | prose | pages [20] -->
After changing the transaction cost, we use the random interference method above to test the robustness of the model, thus proving that the investment model can still provide a relatively proﬁtable investment strategy under the perturbation of the transaction cost parameter. Specif- ically, we apply 1000 random disturbances to the eight models respectively, obtain the annual returns and 5-year total returns of the actual model and the model after disturbance, and give the ranking of our actual investment strategy among the investment strategies after disturbance.

<!-- b000359 | furniture | pages [21] -->
Team # 2218743

<!-- b000360 | furniture | pages [21] -->
Page 20 of 23

<!-- b000361 | heading | pages [21] -->
7 Model Evaluation

<!-- b000362 | heading | pages [21] -->
7.1 Strengths

<!-- b000363 | prose | pages [21] -->
• The investment strategy model integrates the knowledge of economics and ﬁnance, and the establishment of model is based on Markowitz’s mean-variance theory and CVAR theory, with strong reliability. In addition, the trading day judgment model is based on the moving average long arrangement method, which has passed suﬃcient historical tests and is highly credible.

<!-- b000364 | prose | pages [21] -->
• The investment strategy model is applicable to a wide range of objects, and can adjust the corresponding risk upper limit according to the diﬀerent anti-risk capabilities of traders, thereby providing targeted and optimal investment strategies.

<!-- b000365 | prose | pages [21] -->
• According to the results of the optimal investment strategy test and sensitivity analysis of the model, it is proved that our model can adapt to diﬀerent economic environments and provide the best proﬁtable investment strategy, ensuring that the risk is minimized at the same time.

<!-- b000366 | heading | pages [21] -->
7.2 Weaknesses

<!-- b000367 | prose | pages [21] -->
• Due to the limitation of the CVAR model, the investment strategy is based on the as- sumption that the return on assets obeys the normal distribution. Thus, the data of other distribution types needs to choose another model to obtain optimal strategies. Because of the limited data, our investment strategy model is only tested on a set of 5-year asset price data, and the scope of application of the model remains to be determined.

<!-- b000368 | prose | pages [21] -->
• There are too many calculation items, which is relatively cumbersome, and the running speed of the model needs to be improved.

<!-- b000369 | heading | pages [22] -->
Memorandum

<!-- b000370 | prose | pages [22] -->
To: traders

<!-- b000371 | heading | pages [22] -->
From: Model Development Team

<!-- b000372 | heading | pages [22] -->
Subject: An introduction to investment strategy models

<!-- b000373 | prose | pages [22] -->
Date: February 22, 2022

<!-- b000374 | prose | pages [22] -->
This memo introduces our investment strategy model for you from four perspectives: the establishment of transaction strategy model, the robustness of the model, the sensitivity of the model, and investment returns.

<!-- b000375 | prose | pages [22] -->
1. Establishment of transaction strategy model.

<!-- b000376 | prose | pages [22] -->
It is common sense that accurately predicting the future trend of asset prices is the basic premise of correct investment decisions. We use the ARIMA model commonly used in time series analysis to determine reasonable model parameters based on known historical data to predict the next day’s price. Because too frequent trading will increase transaction costs and bring greater investment risks , we clarify the current market state and judge whether to trade at present based on the moving average long arrangement method. Finally, we established a revenue-CVAR dual-objective optimization model and obtained a series of feasible solutions through the NSGA-II algorithm, and then the daily trading strategy is obtained by combining the upper limit of the downside semi-variance of the asset portfolio. At the same time, our model can modify the upper limit of the risk constraint according to the investor’s degree of risk aversion, and obtain the best investment strategy that matches anyone’s risk tolerance.

<!-- b000377 | caption | pages [22] -->
Figure 16: Establishment of transaction strategy model.

<!-- b000378 | prose | pages [22] -->
2. Robustness of the model.

<!-- b000379 | prose | pages [22] -->
In the prediction bias test, the MAPE values are all less than 0.1, very close to 0. R2-score values are all greater than 94%, close to 1, indicating that the model can accurately predict the key moment when the asset price ﬂuctuates greatly, thus providing a good precondition for subsequent investment decisions.

<!-- b000380 | prose | pages [22] -->
After the investment strategy optimality test, our investment model can buy assets before the bull market, hold to rise, and accurately grasp the proﬁt opportunities. At the same time, the model has the ability to survive the period of bear market smoothly, with high anti-risk ﬂuctuation ability, and can keep the asset loss to a minimum in the bear market.

<!-- b000381 | prose | pages [22, 23] -->
21 In addition, we apply random disturbance to the given investment strategies to generate 1000 groups of new simulated investment strategies. The comparison of returns shows that the average annual returns of simulated investments are lower than the investment strategies given by us, and the 5-year total returns of our investment strategies are higher than 93% of the simulated investment strategies, which is enough to prove that our investment model can provide you with a relatively proﬁtable investment strategy while minimizing risk.

<!-- b000383 | prose | pages [23] -->
3. Model sensitivity.

<!-- b000384 | prose | pages [23] -->
Since changes in the global ﬁnancial and economic environment, domestic macro-politics, and economic environment will all have an impact on the market, the volatile assets transaction costs are likely to change accordingly. By adjusting the parameter settings of transaction costs, we ﬁnd that our investment model is more sensitive to the transaction cost of bitcoin, and the model is more sensitive to the reduction of transaction cost relative to the increase of transaction cost. At the same time, after multiple robustness tests, our investment model also has good performance under diﬀerent transaction costs, exceeding 90% of the simulated decisions, which is worthy of trust.

<!-- b000385 | prose | pages [23] -->
4. Investment return.

<!-- b000386 | prose | pages [23] -->
The 5-year total rate of return on the investment reaches 616.63%, the average annual rate of return is 261.41%, and the highest annual rate of return is 664.68%, which means our model has strong proﬁtability. The lowest annual rate of return is 55.6%, which means that the model can quickly adjust asset allocation and has strong anti-risk capabilities.

<!-- b000387 | prose | pages [23] -->
Should you need more information, we’ll be glad to introduce more about the Investment Strategy Model.

<!-- b000388 | prose | pages [23] -->
From 2016 to 2018, the market performance was relatively stable and the risk was small. We are optimistic about the rise of bitcoin, choose to hold a large share of bitcoin with a relatively low valuation and hold a certain amount of gold to hedge risks, which accurately predict and grasp the upward trend of bitcoin. The three-year returns were 368.99%, 664.68%, and 102.48%.

<!-- b000389 | prose | pages [23] -->
In 2019-2021, the market performance was volatile, and bull and bear markets appeared frequently. In 2020, we accurately grasped the opportunities in the bitcoin market, buy at low prices, and achieve an annual return of 55%. In 2021, we will seize the opportunity to reduce bitcoin holdings and buy gold to take proﬁt before the bear market comes. The yield in 2021 is 453.03%, ﬁnally achieved a 5-year cumulative growth of 616.63%.

<!-- b000390 | prose | pages [23] -->
Therefore, our investment strategy model can grasp the reasonable relationship between investment opportunities and trading volume, and have the ability to stop loss and take proﬁt for the purpose of eﬀectively avoiding risks, recommending proﬁtable investment strategies that best suit your risk-resisting ability.

<!-- b000391 | prose | pages [23] -->
The above is the whole content of our model. Should you need more information, we’ll be glad to discuss our investment strategy models in detail at next meeting.

<!-- b000392 | prose | pages [23] -->
22

<!-- b000393 | furniture | pages [24] -->
Team # 2218743

<!-- b000394 | furniture | pages [24] -->
Page 23 of 23

<!-- b000395 | heading | pages [24] -->
References

<!-- b000396 | references | pages [24] -->
[1] Wang Mengtian. 2021. Research on future price trend prediction and quantitative trading

<!-- b000397 | references | pages [24] -->
strategy based on machine learning.

<!-- b000398 | references | pages [24] -->
[2] Yao Haixiang& Li Junwei& Xia Shenghao& Chen Shumin. 2021. Fuzzy trade decision

<!-- b000399 | references | pages [24] -->
based on Apriori Algorithm and neural network.

<!-- b000400 | references | pages [24] -->
[3] Huang Wenlan. 2020. Research on portfolio optimization based on multi-objective Evo-

<!-- b000401 | references | pages [24] -->
lutionary Algorithm.

<!-- b000402 | references | pages [24] -->
[4] Meng Xianghuan. 2013. Research on application of risk portfolio investment model based

<!-- b000403 | references | pages [24] -->
on multi-objective programming.

<!-- b000404 | references | pages [24] -->
[5] Zhang Yanzi. 2012. Empirical analysis of portfolio optimization in gold market.

<!-- b000405 | references | pages [24] -->
[6] Chen Keyan. 2004. Research on optimal portfolio investment model based on genetic

<!-- b000406 | references | pages [24] -->
algorithm.
