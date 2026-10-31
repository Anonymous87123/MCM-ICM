# P-C-2022-2208834-e1b081c3

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2022

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
C

<!-- b000005 | title | pages [1] -->
2208834

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
An Improved Pairs Trading Strategy Based on

<!-- b000008 | title | pages [1] -->
Cointegration of Gold and Bitcoin

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
As a traditional investment, gold is often seen as a safe haven asset with stable returns due to its commodity nature, while bitcoin is seen as an emerging trading asset with high volatility and more arbitrage opportunities. The purpose of this report is to establish a trading model for gold and bitcoin that uses price data up to the day to provide the best investment return. We provide a pairs trading strategy that outperforms all other strategies and is robust and has lower risk.

<!-- b000011 | prose | pages [1] -->
In order to get the best trading strategy, we ﬁrstly observe the pre-processed and normalized data, and ﬁnd that there is a cointegration relationship between them. Secondly, we process the data using the Modiﬁed Dollar Neutral strategy (MDN), which is an improvement of the pairs trading.By using MDN, we predict the data and make a buying and selling decision. Finally, we conduct a backtest using the data of the last ﬁve years, and the results show that after continuous trading and asset transformation using the pairs trading strategy, the $1,000 on September 10, 2016 turn into $106,986.1 on September 10, 2021, with a nearly 107 times year-on-year increase in net asset value and a huge return rate.

<!-- b000012 | prose | pages [1] -->
For the purpose of proving that our strategy is the best strategy, we compare the pairs trading strategy with random trading strategy and machine learning strategy LSTM and XGBoost respec- tively. The results show that the Sharpe ratio of pairs trading strategy is 1.53-2.32 times that of other trading strategies, excess return is 1.49-3.17 times that of other trading strategies, and geometric return is 1.63-3.25 times that of other trading strategies, indicating that pairs trading strategy has higher proﬁtability and lower risk.

<!-- b000013 | prose | pages [1] -->
Then, we analyze the sensitivity of this strategy to transaction costs. The results show that: i. There is a negative exponential relationship between transaction cost and return. When the transaction cost is 0, the theoretical return can reach $120000. ii. Transaction cost is positively correlated with the number of transactions. When the commission ratio is 0.5%, the total return will approach 0 after 500 simulated transactions. The experimental results are in good agreement with our mathematical derivation.

<!-- b000014 | prose | pages [1] -->
In addition, we consider the impact of market risk on trading strategy. We divide the market risk into price risk and reinvestment risk. Then we emphatically explore the non-investable interval highly related to transaction cost under the reinvestment risk, and then set parameters: risk aversion coeﬃcient (λ) is used to discuss the impact of diﬀerent risk aversion degrees of diﬀerent investors on investment utility, as a supplement to the matching strategy.

<!-- b000015 | prose | pages [1] -->
Finally, we write a memo for traders based on the results of the pairs trading strategy, the strength and the possible improvements of the model comparison, and the results of the sensitivity analysis to make our results more scientiﬁc and practical.

<!-- b000016 | keywords | pages [1] -->
Keywords: Modiﬁed Dollar Neutral Strategy; Cointegration; Pairs Trading; Risk Evaluation

<!-- b000017 | furniture | pages [2] -->
Team # 2208834

<!-- b000018 | furniture | pages [2] -->
Page 1 of 24

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1 Introduction

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
1.1

<!-- b000023 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
3

<!-- b000025 | contents | pages [2] -->
1.2

<!-- b000026 | contents | pages [2] -->
Our work

<!-- b000027 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
2 Assumptions

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
3 Model Preparation

<!-- b000032 | contents | pages [2] -->
4

<!-- b000033 | contents | pages [2] -->
3.1

<!-- b000034 | contents | pages [2] -->
Exploratory Data Analysis (EDA)

<!-- b000035 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
4

<!-- b000037 | contents | pages [2] -->
3.1.1

<!-- b000038 | contents | pages [2] -->
Data Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
4

<!-- b000040 | contents | pages [2] -->
3.1.2

<!-- b000041 | contents | pages [2] -->
Stationarity Test

<!-- b000042 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
4

<!-- b000044 | contents | pages [2] -->
3.2

<!-- b000045 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
5

<!-- b000047 | contents | pages [2] -->
L2 Norm Normalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
3.3

<!-- b000049 | contents | pages [2] -->
6

<!-- b000050 | contents | pages [2] -->
4 Investment Strategy of Pairs Trading Based on Cointegration

<!-- b000051 | contents | pages [2] -->
6

<!-- b000052 | contents | pages [2] -->
4.1

<!-- b000053 | contents | pages [2] -->
Data Exploration

<!-- b000054 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
6

<!-- b000056 | contents | pages [2] -->
4.1.1

<!-- b000057 | contents | pages [2] -->
Data Observation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
6

<!-- b000059 | contents | pages [2] -->
4.1.2

<!-- b000060 | contents | pages [2] -->
Cointegration Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
6

<!-- b000062 | contents | pages [2] -->
4.1.3

<!-- b000063 | contents | pages [2] -->
Johanson Cointegration Test . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
7

<!-- b000065 | contents | pages [2] -->
4.1.4

<!-- b000066 | contents | pages [2] -->
Calculation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
7

<!-- b000068 | contents | pages [2] -->
4.2

<!-- b000069 | contents | pages [2] -->
Pairs Trading

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
7

<!-- b000072 | contents | pages [2] -->
4.2.1

<!-- b000073 | contents | pages [2] -->
Pairs Trading Strategies

<!-- b000074 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
8

<!-- b000076 | contents | pages [2] -->
4.2.2

<!-- b000077 | contents | pages [2] -->
Related Formula

<!-- b000078 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
8

<!-- b000080 | contents | pages [2] -->
4.2.3

<!-- b000081 | contents | pages [2] -->
Pairs Trading Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
9

<!-- b000083 | contents | pages [2] -->
5 Strategies Analysis and Comparison

<!-- b000084 | contents | pages [2] -->
9

<!-- b000085 | contents | pages [2] -->
5.1

<!-- b000086 | contents | pages [2] -->
Basic Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
9

<!-- b000088 | contents | pages [2] -->
5.1.1

<!-- b000089 | contents | pages [2] -->
Theoretical Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
9

<!-- b000091 | contents | pages [2] -->
5.1.2

<!-- b000092 | contents | pages [2] -->
Strategy under Stochastic Simulation Method . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
11

<!-- b000094 | contents | pages [2] -->
5.1.3

<!-- b000095 | contents | pages [2] -->
Machine Learning Approach——XGBoost . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
11

<!-- b000097 | contents | pages [2] -->
5.1.4

<!-- b000098 | contents | pages [2] -->
Machine Learning Approach——LSTM . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
11

<!-- b000100 | contents | pages [2] -->
5.2

<!-- b000101 | contents | pages [2] -->
Reiterate the Pairs Trading Strategy

<!-- b000102 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
11

<!-- b000104 | furniture | pages [3] -->
Team # 2208834

<!-- b000105 | furniture | pages [3] -->
Page 2 of 24

<!-- b000106 | contents | pages [3] -->
5.3

<!-- b000107 | contents | pages [3] -->
Horizontal Comparison of Indicators . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [3] -->
12

<!-- b000109 | contents | pages [3] -->
5.3.1

<!-- b000110 | contents | pages [3] -->
Comparison of Basic Indicators . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [3] -->
12

<!-- b000112 | contents | pages [3] -->
5.3.2

<!-- b000113 | contents | pages [3] -->
Developing Indicators

<!-- b000114 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000115 | contents | pages [3] -->
13

<!-- b000116 | contents | pages [3] -->
5.4

<!-- b000117 | contents | pages [3] -->
Vertical Comparison of Pairs Trading Strategy . . . . . . . . . . . . . . . . . . . .

<!-- b000118 | contents | pages [3] -->
14

<!-- b000119 | contents | pages [3] -->
5.5

<!-- b000120 | contents | pages [3] -->
Conclusion

<!-- b000121 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [3] -->
14

<!-- b000123 | heading | pages [3] -->
6 The impact of Risk on Investment Strategy

<!-- b000124 | prose | pages [3] -->
15

<!-- b000125 | prose | pages [3] -->
6.1 Impact of Market Risk on Investment Strategy . . . . . . . . . . . . . . . . . . . . 15

<!-- b000126 | prose | pages [3] -->
6.1.1 Price Risk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

<!-- b000127 | prose | pages [3] -->
6.1.2 Reinvestment Risk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

<!-- b000128 | prose | pages [3] -->
6.2 The Inﬂuence of Individuals’ Risk Aversion on Trading Strategy . . . . . . . . . . 17

<!-- b000129 | heading | pages [3] -->
7 Sensitivity Analysis

<!-- b000130 | prose | pages [3] -->
17

<!-- b000131 | heading | pages [3] -->
8 Conclusions

<!-- b000132 | prose | pages [3] -->
19

<!-- b000133 | prose | pages [3] -->
8.1 Summary of Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000134 | prose | pages [3] -->
8.1.1 Results of Problem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000135 | prose | pages [3] -->
8.1.2 Results of Problem 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000136 | prose | pages [3] -->
8.1.3 Results of Problem 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

<!-- b000137 | prose | pages [3] -->
8.1.4 Results of Problem 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

<!-- b000138 | prose | pages [3] -->
8.2 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

<!-- b000139 | prose | pages [3] -->
8.3 Possible Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

<!-- b000140 | heading | pages [3] -->
Appendices

<!-- b000141 | prose | pages [3] -->
23

<!-- b000142 | heading | pages [3] -->
Appendix A Code Structure and Related Works

<!-- b000143 | prose | pages [3] -->
23

<!-- b000144 | furniture | pages [4] -->
Team # 2208834

<!-- b000145 | furniture | pages [4] -->
Page 3 of 24

<!-- b000146 | heading | pages [4] -->
1 Introduction

<!-- b000147 | heading | pages [4] -->
1.1 Problem Background

<!-- b000148 | prose | pages [4] -->
Market trading usually involves buying and selling risk assets. Investors want to limit their trading risk while maximizing returns, and this can be achieve by invest wisely in a variety of assets.

<!-- b000149 | prose | pages [4] -->
Serious gold investors (gold bugs) love gold because of its ability to store value during tumul- tuous times and its use as an inﬂation hedge. Bitcoin buyers and other crypto enthusiasts, however, would argue that bitcoin oﬀers the same level of protection but is superior due to its ease of storage and transfer.

<!-- b000150 | prose | pages [4] -->
Under the same initial capital conditions, diﬀerent portfolios will bring diﬀerent returns and associated risks, so it is necessary to study the best way to balance portfolio, that is to say, the appropriate proportions of gold and bitcoin in the portfolio.

<!-- b000151 | heading | pages [4] -->
1.2 Our work

<!-- b000152 | prose | pages [4] -->
In order to facilitate the evaluation of the trading model, we build a backtesting system(See the appendix). All of our models (the best model and the three baseline models) are easily estimated using this system. In order to create the optimal trading strategy, we build a pairs trading model based on two given assets. Through trading simulation, we can the trading results of any model (how much is the initial $1000 investment worth on 9/10/2021). By comparing the transactions of these models, we conﬁrm the superiority of our model. Then we test the robustness of the model and the sensitivity to transaction costs, and ﬁnally convey our model, strategy and results to traders through memos.

<!-- b000153 | prose | pages [4] -->
To solve these problems, our team will do the following:

<!-- b000154 | prose | pages [4] -->
• As preparation, we explore the data and test the stationarity of the data set. We clean, select and normalize the tested data.

<!-- b000155 | prose | pages [4] -->
• We consider the relationship between gold price trend and bitcoin price trend, and ﬁnd that they passed the cointegration test. On this basis, we use the paired trading strategy to back test the data, so as to obtain the trading mode and trading strategy.

<!-- b000156 | prose | pages [4] -->
• In order to conﬁrm that our model is optimal, we constructed three baseline models for comparison, namely, random strategy, xgboost strategy and attention-based LSTM strategy.

<!-- b000157 | prose | pages [4] -->
The latter two are based on current mainstream machine learning or time series analysis models. We compare and analyze returns(arithmetic return, geometric time weighted return, Jensen alpha), robustness, risk indicators (Sharpe ratio) and other indicators(information ratio, tracking error) of the three methods. By disturbing our model’s parameters, we test the robustness of the model to its own parameters.

<!-- b000158 | prose | pages [4] -->
• Based on the previous research, we also consider the risk of transactions. We divide the market risks that aﬀect the trading strategy into price risk and Reinvestment risk, and take personal risk preference into account to explore their impact on the choice of trading strategy.

<!-- b000159 | heading | pages [4] -->
2 Assumptions

<!-- b000160 | prose | pages [4] -->
In order to simplify the above problems, we make the following reasonable assumptions:

<!-- b000161 | furniture | pages [5] -->
Team # 2208834

<!-- b000162 | furniture | pages [5] -->
Page 4 of 24

<!-- b000163 | prose | pages [5] -->
• Assumption1: The data given obeys to the basic assumptions of historical simulation method.

<!-- b000164 | prose | pages [5] -->
History will repeat itself, and the subsequent market price can be simulated according to the historical price to get the predicted price.

<!-- b000165 | prose | pages [5] -->
• Assumption2: Markets are relatively perfect and ﬂexible. All transactions have no transac- tion delay, whether buying or selling, which are immediate transactions, immediate success;

<!-- b000166 | prose | pages [5] -->
The transaction cost of the same asset remains the same every time it is traded; Transactions can be subdivided indeﬁnitely, with no size limit.

<!-- b000167 | prose | pages [5] -->
• Assumption3:In reality short-selling and leverage is allowed, but if we use unlimited leverage or borrow approach, there is no approach that will beat the method which investors add the endless leverage on the rising asset. This will make our study meaningless. So, in our strategies design, we don’ t think of the short-selling and leverage.

<!-- b000168 | prose | pages [5] -->
• Assumption4: Asset prices remain the same for the same day, and all transactions are settled at the day’s closing price.

<!-- b000169 | heading | pages [5] -->
3 Model Preparation

<!-- b000170 | heading | pages [5] -->
3.1 Exploratory Data Analysis (EDA)

<!-- b000171 | heading | pages [5] -->
3.1.1 Data Observation

<!-- b000172 | prose | pages [5] -->
We select the oﬃcial data set, lbma-gold CSV and bchain-mkpru CSV for data observation. The two data sets show the closing price in U.S. dollars of gold on the indicated date and the price in U.S. dollars of a single bitcoin on the indicated date from November 9, 2016 to 9,2021. First, we describe the basic data as follows:

<!-- b000173 | prose | pages [5] -->
(a) gold (b) bitcoin

<!-- b000174 | caption | pages [5] -->
Figure 1: The daily asset prices

<!-- b000175 | prose | pages [5] -->
To better observe price changes, we calculated daily returns:

<!-- b000176 | prose | pages [5] -->
Return = (Ct −Ct−1) /Ct−1 × 100% (1)

<!-- b000177 | prose | pages [5] -->
We can get the information from the histogram of historical ﬂuctuating prices in Figure 2.

<!-- b000178 | heading | pages [5] -->
3.1.2 Stationarity Test

<!-- b000179 | prose | pages [5, 6] -->
In order to facilitate the calculation of the model in the next step, we test the stationarity of the data set. For the given data set, we use the mainstream unit root test method to test whether there is a (a) gold_return (b) bitcoin_return

<!-- b000180 | furniture | pages [6] -->
Team # 2208834

<!-- b000181 | furniture | pages [6] -->
Page 5 of 24

<!-- b000183 | caption | pages [6] -->
Figure 2: Histogram of the return distribution

<!-- b000184 | prose | pages [6] -->
unit root in the series. If there is, it is a non-stationary series, and if there is not, it is a stationary series.

<!-- b000185 | prose | pages [6] -->
The inspection process is consistent with DF inspection. If we want to strictly judge whether the sequence is wide and stable, we can directly test whether it is stable without intercept term and trend term; If the original hypothesis cannot be rejected (e.g. p > 0.05), that means the series is non-stationary, it is still necessary to test whether the series is stable. If the trend is not stable and the trend is not stable, the ﬁrst-order diﬀerence and other stabilization methods can be used for processing before testing. If the trend is stable, the diﬀerence method should not be used for stabilization due to excessive diﬀerence.Through the stationarity test, we can get the following ACF diagram.

<!-- b000186 | prose | pages [6] -->
(a) acf_normal (b) acf_diﬀer1 (c) acf_diﬀer2

<!-- b000187 | caption | pages [6] -->
Figure 3: ACF inspection chart

<!-- b000188 | prose | pages [6] -->
Through ADF test, we can see that the original data set is relatively stable and tends to normal distribution. Therefore, we will use the original data for further consideration.

<!-- b000189 | heading | pages [6] -->
3.2 Data Cleaning

<!-- b000190 | prose | pages [6] -->
Whether the data is clean or not is directly related to the accuracy and robustness of the ﬁnal model, and will also aﬀect the ﬁnal conclusion. Therefore, we cleaned the bitcoin price and gold price data obtained in previous years to enhance the accuracy and credibility of our results.

<!-- b000191 | prose | pages [6] -->
We ﬁrst deal with the missing value of the data. In the process of processing, we ﬁnd that because there are certain trading days for gold trading, and bitcoin can be traded at any time, there is inevitably a vacancy in gold price data. Considering that the data of gold price on non-trading days will not be aﬀected by market trends and consumer preferences, we ﬁll the data of vacancy value with the ﬁrst valid data before it.

<!-- b000192 | furniture | pages [7] -->
Team # 2208834

<!-- b000193 | furniture | pages [7] -->
Page 6 of 24

<!-- b000194 | caption | pages [7] -->
Figure 4: Handling the missing values

<!-- b000195 | heading | pages [7] -->
L2 Norm Normalization

<!-- b000196 | prose | pages [7] -->
3.3

<!-- b000197 | prose | pages [7] -->
The L2 norm of vector x (x1, x2, . . . , xn) is deﬁned as:

<!-- b000198 | prose | pages [7] -->
q x2 1 + x2 2 + . . . + x2 norm(x) = (2) n

<!-- b000199 | prose | pages [7] -->
The equivalent form of the above equation is as follows:

<!-- b000200 | prose | pages [7] -->
xi x′ i = (3) norm(x)

<!-- b000201 | prose | pages [7] -->
In the description of the model below, we will use the data processed above for further operation.

<!-- b000202 | heading | pages [7] -->
4 Investment Strategy of Pairs Trading Based on Cointegration

<!-- b000203 | heading | pages [7] -->
4.1 Data Exploration

<!-- b000204 | heading | pages [7] -->
4.1.1 Data Observation

<!-- b000205 | prose | pages [7] -->
After normalizing the data, we can see from the ﬁgure that the trend of bitcoin price has experienced four stages of stability - rise - fall - rise again, and the trend of gold price has gone through ﬁve stages of stability - rise - fall - rise again - fall again. And we can see that compared with the trend of gold price, the price of bitcoin has a certain lag. Therefore, we guess that there is a certain correlation between the price trend of bitcoin price and the trend of gold price.

<!-- b000206 | caption | pages [7] -->
Figure 5: Observation of price correlation

<!-- b000207 | heading | pages [7] -->
4.1.2 Cointegration Theory

<!-- b000208 | prose | pages [7] -->
The contents of cointegration are:

<!-- b000209 | furniture | pages [8] -->
Team # 2208834

<!-- b000210 | furniture | pages [8] -->
Page 7 of 24

<!-- b000211 | prose | pages [8] -->
Suppose sequence Xt is d-order cointegration,donated by Xt ∼I(d). If there is a non-zero vector β and the condition holds Yt = βXt ∼I(d−b), then Xt is said to have b,d-order cointegration relations, donated by Xt ∼CI(d, b). We call β as a cointegration vector.

<!-- b000212 | prose | pages [8] -->
Especially, when Xt and Yt are both integration of order one, in general, the linear combination of Xt and Yt is still an integration of order one. But for some non-zero vectors β, it makes: Yt −βXt ∼I(0).At this time, the non-zero vector β is called cointegration vector. Each of these βt is the cointegration coeﬃcient at time t.In other words, if the two sets of sequences are non-stationary, but are stationary after the ﬁrst-order diﬀerence, and the two sets of sequences are stationary after some linear combination, there is a cointegration relationship between them.

<!-- b000213 | heading | pages [8] -->
4.1.3 Johanson Cointegration Test

<!-- b000214 | prose | pages [8] -->
Nonstationary series are prone to pseudo regression, and the signiﬁcance of cointegration is to test whether the causal relationship described by their regression equation is pseudo regression. Therefore, we decide to use Johansen cointegration test to test the data set.

<!-- b000215 | prose | pages [8] -->
Johanson cointegration test is a test method based on VAR model, but it can also be directly used for cointegration test between multiple variables.

<!-- b000216 | prose | pages [8] -->
Test trace statistics:

<!-- b000217 | prose | pages [8] -->
N X LRM = −n log (1 −λi) (4) i=M−1 Where, M is the number of cointegration vectors, λi is the ith eigenvalue arranged by size,and N is the sample size.

<!-- b000218 | heading | pages [8] -->
4.1.4 Calculation Results

<!-- b000219 | prose | pages [8] -->
Therefore, by calculating their respective rates of return, we can get the correlation coeﬃcient of their rates of return and the degree of their deviation from the mean, and test the cointegration of the two groups of data. After testing, we ﬁnd that there is a lagging cointegration relationship between the price trend of bitcoin and the price trend of gold. This lays the foundation for our following trading methods.

<!-- b000220 | heading | pages [8] -->
4.2 Pairs Trading

<!-- b000221 | prose | pages [8] -->
The basic idea of pairs trading is to ﬁnd two stocks with highly similar historical trends in the stock market. Due to the similarity of their ﬂuctuations, at the same period of time, the rising and falling trends and ranges of the two are basically the same, which is the so-called "equilibrium". When there is a large deviation in the trend at a certain moment, we will enter the long position (i.e. buying) of the stock below the average and the short position (i.e. short selling) of the stock above the average. When the two return to the mean value, we close the positions of the two stocks to lock in the income.

<!-- b000222 | prose | pages [8] -->
We approximately regard bitcoin and gold as two stocks, and apply the pairs trading strategy to the trading between bitcoin market and gold market. We use the historical data provided by the topic to predict the future price of bitcoin and gold, and make decisions to maximize our own income.Ultimately,we use dollar neutral strategy to build the prediction and decision-making system of bitcoin and gold.

<!-- b000223 | furniture | pages [9] -->
Team # 2208834

<!-- b000224 | furniture | pages [9] -->
Page 8 of 24

<!-- b000225 | heading | pages [9] -->
4.2.1 Pairs Trading Strategies

<!-- b000226 | prose | pages [9] -->
When capturing the abnormal rise of bitcoin price trend, the pairs trading strategy will choose to buy bitcoin; On the contrary, when capturing the abnormal decline of bitcoin price trend, the pairs trading strategy will choose to sell bitcoin(in Figure 6, the red triangle indicates buying bitcoin and the green triangle indicates selling bitcoin).

<!-- b000227 | caption | pages [9] -->
Figure 6: Corresponding buying and selling strategy

<!-- b000228 | heading | pages [9] -->
4.2.2 Related Formula

<!-- b000229 | prose | pages [9] -->
We record the price of gold at time t as PG (t),the price of bitcoin at time t as PB (t).The yields of the two ﬁnancial assets from t1 to t2 are respectively:

<!-- b000230 | prose | pages [9] -->
PA (t2)  RA (t1, t2) = ln PA (t1) (5) PB (t2)  RB (t1, t2) = ln PB (t1)

<!-- b000231 | prose | pages [9] -->
During this period, the correlation coeﬃcients are:

<!-- b000232 | prose | pages [9] -->
RA(t −1, t) −¯RA (t1, t2) RB(t −1, t) −¯RB (t1, t2) Pt2     · t=t1+1 ρAB (t1, t2) = 2 · Pt2 qPt2 2 RA(t −1, t) −¯RA (t1, t2) RB(t −1, t) −¯RB (t1, t2)   t=t1+1 t=t1+1 (6) The equilibrium price is assumed to be:

<!-- b000233 | prose | pages [9] -->
¯RAB (t1, t2) = 1 2 (RA (t1, t2) + RB (t1, t2)) (7)

<!-- b000234 | prose | pages [9] -->
From the above formula, we can calculate the deviation degree of gold price and bitcoin price from the mean value as follows: ˜RA (t1, t2) = RA −¯RAB (t1, t2) (8) ˜RB (t1, t2) = RB −¯RAB (t1, t2) In the algorithm, we add a long short position constraint to meet the needs of the actual situation:

<!-- b000235 | furniture | pages [10] -->
Team # 2208834

<!-- b000236 | furniture | pages [10] -->
Page 9 of 24

<!-- b000237 | prose | pages [10] -->
i) Total Position Limit

<!-- b000238 | prose | pages [10] -->
PA(t) · |QA(t)| + PB(t) · |QB(t)| = 2 · I (9)

<!-- b000239 | prose | pages [10] -->
ii) Currency Neutrality Conditions

<!-- b000240 | prose | pages [10] -->
PA(t) · QA(t) + PB(t) · QB(t) = 0 (10)

<!-- b000241 | heading | pages [10] -->
4.2.3 Pairs Trading Algorithm

<!-- b000242 | prose | pages [10] -->
Based on the above basic data and restrictions, the process of obtaining the matching transaction strategy is as follows:

<!-- b000243 | heading | pages [10] -->
Algorithm 1: Pairs Trading Strategy(MDN)

<!-- b000244 | prose | pages [10] -->
Initialization:Account A: [C, G, B] = [1000, 0, 0]([ cash, gold, bitcoin ]) for t ←1 to T do t1 = 0,t2 = t −k Get the price data at t1 and t2:PB(t1),PG(t1),PB(t2),PG(t2) Calculate the return oﬀset for each asset, denotes as: ˜RA, ˜RB if Asset a position is not 0 and ˜RA(t −1, t) · ˜RA(t −2, t −1) < 0 then Close out end ˜RA(t −1, t) −¯RB(t −1, t) > ϵ then if Open positions to buy undervalued assets( ˜RA < 0) end Update Account A end

<!-- b000245 | heading | pages [10] -->
5 Strategies Analysis and Comparison

<!-- b000246 | prose | pages [10] -->
In this section, we brieﬂy describe how the baseline models are constructed. Then we compare the three baseline models with our model horizontally. Finally, we adjust model parameters and observe the robustness of model performance vertically.

<!-- b000247 | heading | pages [10] -->
5.1 Basic Strategies

<!-- b000248 | heading | pages [10] -->
5.1.1 Theoretical Method

<!-- b000249 | prose | pages [10] -->
i) Feature Creation With reference to various technical indicators, we constructed the following features(??) using raw data. The calculation of basic features is relatively simple, and only the calculation formula is shown here.

<!-- b000250 | prose | pages [10, 11] -->
LogReturn : rt = ln Pt (11) Pt−1 PastReturns = Rt−1 (12) Momentum = Pt −Pt−k (13) n−1 MovingAverage :SMAi = 1 X Pt−i (14) n i=0 ExponentialMA : EMAt = EMAt−1 + α [Pt −EMAt−1] (15) After the feature construction is completed, the feature is normalized ﬁrst. In order to improve information exposure, the model is easy to learn. (Training models with non-normalized data yielded poor results)

<!-- b000251 | furniture | pages [11] -->
Team # 2208834

<!-- b000252 | furniture | pages [11] -->
Page 10 of 24

<!-- b000254 | prose | pages [11] -->
ii) Feature Selection

<!-- b000255 | prose | pages [11] -->
Before feature selection, we ﬁrst use TSNE dimension reduction to observe whether the data is separable(Figure). As can be seen from the Figure 7,we are able to draw an conclusion that the result of feature construction is separable.Then we looked at the correlations between features.As can be seen from the Figure 8, almost the same type of features will have a strong correlation, but most of the heterogeneity between diﬀerent kinds of features is guaranteed.

<!-- b000256 | prose | pages [11] -->
(a) Two-dimensional bisual- (b) Heatmap of correlation matrix ization result of T-SNE

<!-- b000257 | caption | pages [11] -->
Figure 7: Validity and relevance of features

<!-- b000258 | prose | pages [11] -->
Besides,we draw scatter matrix plot of individual feature,as can be seen from Figure 10.

<!-- b000259 | caption | pages [11] -->
Figure 8: Scatter matrix between[’return’, ’RSI-6’, ’MACD’]

<!-- b000260 | furniture | pages [12] -->
Team # 2208834

<!-- b000261 | furniture | pages [12] -->
Page 11 of 24

<!-- b000262 | prose | pages [12] -->
There is some heterogeneity among the main technical indicators, so there is no need to exclude any of them. However, among the averages, only those with longer periods have certain value. Considering that the model has a strong learning ability, the model itself has a certain feature screening ability after adding the attention mechanism, so I retained the majority of features.

<!-- b000263 | heading | pages [12] -->
5.1.2 Strategy under Stochastic Simulation Method

<!-- b000264 | prose | pages [12] -->
Assume that gold and Bitcoin’s prices follow a random walk:

<!-- b000265 | prose | pages [12] -->
St+1 = St ∗exp (µ∆t + σz) (16)

<!-- b000266 | prose | pages [12] -->
St+1, St :are the asset prices of the day and the day before.

<!-- b000267 | prose | pages [12] -->
µ :the mean of changes in the logarithm of asset prices

<!-- b000268 | prose | pages [12] -->
∆t :the time interval, assumed here to be 1 day, has a value of 1/252

<!-- b000269 | prose | pages [12] -->
z :a random number that follows a standard normal distribution

<!-- b000270 | prose | pages [12] -->
Then the Monte Carlo simulation model is established according to the above equation, and enough simulations are carried out to constantly adjust the holding proportion of the three assets to obtain the ever-changing investment value.Based on this random walk, we construct a random trading strategy as an baseline.

<!-- b000271 | heading | pages [12] -->
5.1.3 Machine Learning Approach——XGBoost

<!-- b000272 | prose | pages [12] -->
XGBoost, which stands for Extreme Gradient Boosting, is a scalable, distributed gradient-boosted decision tree (GBDT) machine learning library. It provides parallel tree boosting and is the leading machine learning library for regression, classiﬁcation, and ranking problems. Lightgbm and XGBoost are very competitive statistical learning models in competitions of quantitative trading.

<!-- b000273 | prose | pages [12] -->
While training the model, in order to avoid data leakage we only used part of the data from the ﬁrst year for training and were very careful not to allow this part of the data to appear in the subsequent backtesting.

<!-- b000274 | heading | pages [12] -->
5.1.4 Machine Learning Approach——LSTM

<!-- b000275 | prose | pages [12] -->
Long Short-Term Memory (LSTM) is a special kind of Recurrent Neural Network(RNN). LSTM networks are explicitly designed to avoid the long-term dependency problem, and remembering information for long periods of time is practically their default behavior. In this experiment, in order to obtain better prediction eﬀect, we added attention mechanism into the model structure. We see this attention-based LSTM as a strong competitor to our model, and it is probably one of the models commonly used in quantitative trading these days. In practice, the LSTM network structure we use is as follows. We take the price data and technical indicators of the 30 trading days before the forecast date as features, and the feature dimension is [batchsize, timerange, features] = [64, 30, 20]. We use a similar approach to the previous model to avoid data leakage.

<!-- b000276 | heading | pages [12] -->
5.2 Reiterate the Pairs Trading Strategy

<!-- b000277 | prose | pages [12, 13] -->
The pairs trading model is based on the analysis that there is a lag co-integration relationship between the gold and Bitcoin prices, namely the Bitcoin with gold on price trends exist obvious lag correlation. Next according to gold price change trend, we can reasonably estimate price trend of the Bitcoin, buy the asset whose price is forecasted to rise and sell the asset whose price is expected to fall. If the current capital is suﬃcient, we will buy all the one asset; if the capital is insuﬃcient, (a) Data split without data leakage (b) Structure of attention based LSTM

<!-- b000278 | furniture | pages [13] -->
Team # 2208834

<!-- b000279 | furniture | pages [13] -->
Page 12 of 24

<!-- b000281 | caption | pages [13] -->
Figure 9: Data split and Model structure

<!-- b000282 | prose | pages [13] -->
we will hold three diﬀerent assets appropriately. Finally, the investment value under this method is obtained.

<!-- b000283 | caption | pages [13] -->
Figure 10: The net worth of four strategies

<!-- b000284 | prose | pages [13] -->
By observing the above investment value curve, it is found that the return under the pairs trading strategy is signiﬁcantly improved compared with the other two methods. It can even be compared with the price trend of Bitcoin, that after 2019, it has even exceeded the price growth of Bitcoin, indicating that the strategy has worked well.

<!-- b000285 | heading | pages [13] -->
5.3 Horizontal Comparison of Indicators

<!-- b000286 | heading | pages [13] -->
5.3.1 Comparison of Basic Indicators

<!-- b000287 | prose | pages [13] -->
We can calculate the daily return rate of the above three methods according to the following formula, and then calculate the arithmetic average return rate and return volatility through the average return rate and standard deviation of return rate:

<!-- b000288 | prose | pages [13] -->
rt = Vt −Vt−1 (17) Vt−1

<!-- b000289 | prose | pages [13] -->
Vt, Vt−1 :the position value of the current day and the previous day respectively.

<!-- b000290 | furniture | pages [14] -->
Team # 2208834

<!-- b000291 | furniture | pages [14] -->
Page 13 of 24

<!-- b000292 | prose | pages [14] -->
The annualized arithmetic average return rate and annualized return volatility are obtained in the following table:

<!-- b000293 | caption | pages [14] -->
Table 1: The basic indicators of four diﬀerent strategies

<!-- b000294 | prose | pages [14] -->
stochastic simulation method XGBoost method LSTM method Pairs Trading method Arithmetic volatility of Arithmetic volatility of Arithmetic volatility of Arithmetic volatility of return return return return return return return return 26.64% 35.83% 53.42% 58.17% 53.31% 52.16% 76.96% 50.14%

<!-- b000295 | prose | pages [14] -->
The relationship among the size of annualized arithmetic average return rate is:

<!-- b000296 | prose | pages [14] -->
Pairs Trading method>XGBoost method>LSTM method>stochastic simulation method

<!-- b000297 | prose | pages [14] -->
The relationship between the volatility of annualized returns is as follows:

<!-- b000298 | prose | pages [14] -->
XGBoost method>LSTM method>Pairs Trading method>stochastic simulation method

<!-- b000299 | heading | pages [14] -->
5.3.2 Developing Indicators

<!-- b000300 | prose | pages [14] -->
Daily geometric time-weighted return(Rt):Since we analyze the size and change of the rate of return, it is more meaningful to use daily geometric rate of return for analysis.

<!-- b000301 | prose | pages [14] -->
n[ (1 + Rt)n = (1 + ri) (18) i=1

<!-- b000302 | prose | pages [14] -->
Jensen’s alpha: This index can measure the diﬀerence between expected return and average return. The larger this index is, it means that our expected return exceeds the theoretical return and the investment eﬀect is better. And because gold and Bitcoin are both safe-haven assets that have no obvious relationship with the SSE 50 and other indexes, and we could hold cash, we assume that rM = rf,that means Jensen’s alpha is the equivalent of excess return.

<!-- b000303 | prose | pages [14] -->
α = E (rp) −[rf + βp (rM −rf)] ⇒α = E (rp) −rf (19)

<!-- b000304 | prose | pages [14] -->
Sharpe Ratio: This indicator is used to evaluate the advantages and disadvantages of investment considering both return and risk. The higher the value, the greater the return will be obtained under the same risk, and the lower the risk will be faced under the same return, which is in line with the pursuit of investment strategy by risk-averse investors.

<!-- b000305 | prose | pages [14] -->
SR = E (rp) −rf (20) σ (rp)

<!-- b000306 | prose | pages [14] -->
Information Ratio: This indicator is used to evaluate the merits and demerits of active investment in the portfolio, namely, the degree to which the investment strategy is superior to passive investment. The higher the value, the more meaningful the investment strategy is.

<!-- b000307 | prose | pages [14] -->
α IR = (21) σ (rp −rf)

<!-- b000308 | prose | pages [14, 15] -->
Finally, the tracking error of the three methods is calculated on an annual basis. The smaller the stochastic simulation method XGBoost method LSTM method Pairs Trading method Indicators Percent/Number Percent/Number Percent/Number Percent/Number 0.08% 0.14% 0.16% 0.26% Geometric time-weighted return 0.23 0.49 0.49 0.73 Jensen’s alpha 0.63 0.85 0.95 1.46 Sharpe Ratio 0.05 0.06 0.06 0.10 Information Ratio

<!-- b000309 | furniture | pages [15] -->
Team # 2208834

<!-- b000310 | furniture | pages [15] -->
Page 14 of 24

<!-- b000311 | caption | pages [15] -->
Table 2: The developing indicators of four diﬀerent strategies

<!-- b000313 | prose | pages [15] -->
index, the stronger the risk active avoidance ability corresponding to the strategy is, and the better the strategy is.

<!-- b000314 | prose | pages [15] -->
′) −rf TE = E (rp (22) E (rp′) :The average annual returns, not the average of all returns.

<!-- b000315 | caption | pages [15] -->
Figure 11: The (yearly) tracking error of four diﬀerent strategies

<!-- b000316 | prose | pages [15] -->
Observing the line chart of tracking error above, it can be found that: in the pairs trading strategy, only the tracking error near 2017 is relatively large, but it is not diﬃcult to ﬁnd that this is because the Bitcoin and gold prices in 2017 had unexpectedly huge ﬂuctuations. However, since we assume a long-term investment of ﬁve years, the tracking error within a single period does not represent anything. Moreover, when the price ﬂuctuates greatly near 2020, the model does not have a large tracking error, indicating that the model can be adjusted independently after a huge ﬂuctuation, which also shows the excellence of the strategy.

<!-- b000317 | heading | pages [15] -->
5.4 Vertical Comparison of Pairs Trading Strategy

<!-- b000318 | prose | pages [15] -->
Due to the co-integration relationship between Bitcoin and gold prices under the condition of lag period, investment returns under diﬀerent lag periods are diﬀerent. However, there is no diﬀerence in other aspects, because there are no signiﬁcant diﬀerences in the above indicators under the trade- oﬀbetween risk and return. According to the graph of the ﬁnal value of diﬀerent lag periods, we can know that the model performance is stable only when the lag period is in the range of [15, 60] days. It is speculated that the too short time cycle is aﬀected by the short-term drastic ﬂuctuations of assets, while the too long cycle is too lagged, resulting in information loss.

<!-- b000319 | heading | pages [15] -->
5.5 Conclusion

<!-- b000320 | prose | pages [15] -->
In terms of absolute position value, the initial $1,000 investment in our pairs trading strategy ended up being worth a staggering $106,686.1 on October 9, 2021, far outperforming other existing methods.

<!-- b000321 | furniture | pages [16] -->
Team # 2208834

<!-- b000322 | furniture | pages [16] -->
Page 15 of 24

<!-- b000323 | caption | pages [16] -->
Figure 12: The ﬁnal value of diﬀerent lag period of pairs trading strategy

<!-- b000324 | prose | pages [16] -->
From the horizontal indicators analysis, the large geometric time-weighted return and Jensen’s alpha value indicate that the absolute return rate of pairs trading strategy is higher than that of existing methods. And the large information ratio and sharpe ratio indicate that from the perspective of balancing risks and returns, the pairs trading strategy still performs well and has a good performance in active investment management. Tracking error trend indicates that the strategy has good risk adaptability and can actively avoid unnecessary risks. To sum up, pairs trading strategy is an innovative, low-risk, high-return strategy.

<!-- b000325 | prose | pages [16] -->
From the analysis of the longitudinal lag period, it is found that under diﬀerent lag periods, there will be little diﬀerence in risk but deviation in returns. Therefore, we can obtain the best matching trading strategy by adjusting the lag period, which is also the advanced point of this strategy.

<!-- b000326 | caption | pages [16] -->
Figure 13: The ﬁnal returns of the four strategies

<!-- b000327 | heading | pages [16] -->
6 The impact of Risk on Investment Strategy

<!-- b000328 | prose | pages [16] -->
Maximization of return is certainly one of the most important goals we pursue, but when we design trading strategies, we have to consider the impact of the possible future uncertainty – risk. On the one hand, risk will aﬀect the price trend of assets and thus aﬀect the improvement of our strategies in reality. On the other hand, the risk aversion of diﬀerent investors will lead to diﬀerent trading strategies of diﬀerent individuals.

<!-- b000329 | heading | pages [16] -->
6.1 Impact of Market Risk on Investment Strategy

<!-- b000330 | prose | pages [16, 17] -->
Although gold and bitcoin’ s risk relative to stocks and other ﬁnancial products is low, their investments are still faced with the profound inﬂuence of the market risk of price risk. And because investors can also hold a certain amount of cash at the same time, as well as the existence of transaction costs, it is greatly possible that reinvestment risk which is caused by the situation which return of portfolio is less than the cash generated by the risk-free rate appears.

<!-- b000331 | furniture | pages [17] -->
Team # 2208834

<!-- b000332 | furniture | pages [17] -->
Page 16 of 24

<!-- b000333 | caption | pages [17] -->
Figure 14: Market risk eﬀects on trading strategy

<!-- b000335 | heading | pages [17] -->
6.1.1 Price Risk

<!-- b000336 | prose | pages [17] -->
Gold as a safe-haven assets and its price sensitivity to interest rate is too low, but the price will be also aﬀected by macroeconomic factors,such as economy, policy.For example, during the period of the COVID-19, the world had a recession. People were afraid of risky assets, and began turning to invest gold, bonds and other assets, leading to rising gold price. Therefore, when determining the investment trading strategy, we should take the inﬂuence of macro factors into account, which is also reﬂected in our own strategy decisions.

<!-- b000337 | prose | pages [17] -->
As a new hedge asset, bitcoin has similar price inﬂuencial factors to gold, so we won’t go into too much detail. However, the biggest diﬀerence between the two is that the volatility of bitcoin is higher, so when making strategies, the price volatility of bitcoin should be assumed to be higher than that of gold.

<!-- b000338 | heading | pages [17] -->
6.1.2 Reinvestment Risk

<!-- b000339 | prose | pages [17] -->
Reinvestment risk mainly depends on the relationship between excess return rate and buying and selling cost, and the following formula can be used to determine the non-trading interval:

<!-- b000340 | prose | pages [17] -->
−SCn ≤MCV An ≤PCn (23)

<!-- b000341 | prose | pages [17] -->
non −trading interval:The expected excess rate of return falls within this range which means you don’t buy or sell, holding cash instead ;

<!-- b000342 | prose | pages [17] -->
Where SCn stands for sell cost, PCn stands for purchase cost and MCVAn stands for marginal contribution to value added. MCVAn in the above formula has the following relationship with indicators such as excess return rate and information ratio:

<!-- b000343 | prose | pages [17] -->
MCV An = αn −IR∗MCARn (24)

<!-- b000344 | prose | pages [17] -->
αn = Rn −Rf (25) Where αn stands for the excess rate of return over the risk-free rate,IR stands for information ratio and MCARn stands for marginal contribution to active risk.

<!-- b000345 | furniture | pages [18] -->
Team # 2208834

<!-- b000346 | furniture | pages [18] -->
Page 17 of 24

<!-- b000347 | prose | pages [18] -->
MCARn indicates the change of the overall risk brought by a 1 % change in the weight of asset n,means:

<!-- b000348 | prose | pages [18] -->
MCARn = ∂σp (26) ∂wn Based on the above formula derivation,the non-trading interval related to the return rate of a single, the cost of buying and selling asset is set:

<!-- b000349 | prose | pages [18] -->
IR ∗MCARn −SCn + Rf ≤Rn ≤IR∗MCARn + PCn + Rf (27)

<!-- b000350 | prose | pages [18] -->
Therefore, based on the above analysis, once the predicted return of gold or bitcoin falls within the above range, our trading strategy immediately changes to hold the corresponding cash.

<!-- b000351 | heading | pages [18] -->
6.2 The Inﬂuence of Individuals’ Risk Aversion on Trading Strategy

<!-- b000352 | prose | pages [18] -->
Although the Markowitz eﬃcient frontier model used in the calculation of portfolio holding ratio assumes that all investors are completely risk-averse, in reality, diﬀerent investors have diﬀerent degrees of risk aversion, namely, given risk aversion coeﬃcient (λ).

<!-- b000353 | prose | pages [18] -->
IR λA = (28) 2 ∗ϕp

<!-- b000354 | prose | pages [18] -->
Where ϕp stands for the optimal active risk(varies between individuals).

<!-- b000355 | prose | pages [18] -->
The reason why diﬀerent degrees of risk aversion have an impact on investment strategies is that investment returns have the following utility function for investors:

<!-- b000356 | prose | pages [18] -->
U = αn −λA ∗ϕ2 p −TC (29)

<!-- b000357 | prose | pages [18] -->
Where TC stands for transaction cost.

<!-- b000358 | prose | pages [18] -->
Then Max(U) can be calculated by using partial derivative of ϕp and operations research method, and the corresponding asset holding ratio and cash holding ratio can be adjusted again.

<!-- b000359 | heading | pages [18] -->
7 Sensitivity Analysis

<!-- b000360 | prose | pages [18] -->
Next, we analyze the sensitivity of pairs transaction strategy to transaction cost.During the operation of the strategy, each transaction will generate a handling fee, which will oﬀset the account value downward in the transaction and generate an intercept. At point T1 in the ﬁgure, if all assets a0 are invested, only relevant assets with value a1 can be obtained. For the convenience of analysis, we assume that the trader invests all assets in each transaction, TC means transaction cost, there are:

<!-- b000361 | prose | pages [18] -->
a1 + TC = a0 (30)

<!-- b000362 | prose | pages [18, 19] -->
We assume that there is a transaction cost of α% in each transaction, thus TC = αat. In the process of a single transaction, the cost of each purchase is a1. Due to the limitation of transaction cost, the actual value of the purchased ﬁnancial assets is a2. From this,we can get the relationship between at and at+1 as follows: at →at+1 = at(1 + α)−1 (31) After considering one transaction process, we further consider n transaction processes.Assuming that the ratio of ﬁnancial assets sold in each transaction is still α%, we can get that the relationship between assets after n times of transaction cost an and undamaged assets a0 is as follows:

<!-- b000363 | furniture | pages [19] -->
Team # 2208834

<!-- b000364 | furniture | pages [19] -->
Page 18 of 24

<!-- b000366 | prose | pages [19] -->
an = a0(1 + α)−n (32)

<!-- b000367 | prose | pages [19] -->
Assuming that the proportion of ﬁnancial assets bought or sold in each transaction is the ﬁxed value k%,then:

<!-- b000368 | prose | pages [19] -->
αk 1 + α)na0 = an (1 − (33)

<!-- b000369 | prose | pages [19] -->
Obviously, this formula has nothing to do with the ﬂuctuation of the asset itself.

<!-- b000370 | prose | pages [19] -->
We select diﬀerent transaction cost rates as the impact indicators, take time as the horizontal axis and income as the vertical axis, we can see that the beneﬁts of the model under diﬀerent transaction costs are shown in Figure 15.

<!-- b000371 | caption | pages [19] -->
Figure 15: The return of the model under diﬀernt transaction costs

<!-- b000372 | prose | pages [19] -->
(a) Relationship between transaction times and (b) Fitting curve for brokerage and return transaction discount

<!-- b000373 | caption | pages [19] -->
Figure 16: Sensitivity analysis of transaction costs

<!-- b000374 | prose | pages [19] -->
It can be seen from the ﬁgure that at the same time point, the lower the transaction cost, the higher the return, which reﬂects the promotion eﬀect of transaction cost on return growth; Accordingly, when the return is the same, the higher the transaction cost, the longer the time required to obtain the same return, which shows the inhibitory eﬀect of high transaction cost on realizing the ideal return. The trend of the model obtained by sensitivity test is consistent with the actual situation, which also proves the rationality and robustness of the pairs trading strategy.

<!-- b000375 | furniture | pages [20] -->
Team # 2208834

<!-- b000376 | furniture | pages [20] -->
Page 19 of 24

<!-- b000377 | heading | pages [20] -->
8 Conclusions

<!-- b000378 | heading | pages [20] -->
8.1 Summary of Results

<!-- b000379 | heading | pages [20] -->
8.1.1 Results of Problem 1

<!-- b000380 | prose | pages [20] -->
After the cointegration test, according to the results of the pairs transaction model,the initial $1,000 investment in our pairs trading strategy ended up being worth a staggering $106,686.1 on October 9, 2021.Given a transaction cost (e.g. αgold = 1% and αbitcoin = 2%), our model can get the best transaction strategy up to the day and the ﬁnal income.

<!-- b000381 | caption | pages [20] -->
Figure 17: Changes in returns after adopting the pairs trading strategy

<!-- b000382 | heading | pages [20] -->
8.1.2 Results of Problem 2

<!-- b000383 | prose | pages [20] -->
According to the results of pairs trading strategy, we compare it with random trading strategy and machine learning strategy (XGBoost), which shows that our strategy is the best(Figure 18). It

<!-- b000384 | prose | pages [20] -->
(a) The value of four diﬀerent strategies (b) The absolute position value of four diﬀerent strategies

<!-- b000385 | caption | pages [20] -->
Figure 18: Algorithm eﬀect comparison

<!-- b000386 | prose | pages [20] -->
can be seen from the ﬁgure that the ﬁnal return of paired trading far exceeds that of other trading strategies. The ﬁnal return reaches 24.87 times that of random trading strategy and 8.03 times that of XGBoost trading strategy.

<!-- b000387 | furniture | pages [21] -->
Team # 2208834

<!-- b000388 | furniture | pages [21] -->
Page 20 of 24

<!-- b000389 | heading | pages [21] -->
8.1.3 Results of Problem 3

<!-- b000390 | prose | pages [21] -->
Through the sensitivity analysis of the model, it can be seen that there is a negative correlation between transaction cost and return at the same time point, and vice versa.

<!-- b000391 | prose | pages [21] -->
(a) The return of the model under dif- (b) Fitting curve for brokerage and re- (c) Relationship between transaction fernt transaction costs turn times and transaction discount

<!-- b000392 | caption | pages [21] -->
Figure 19: Sensitivity analysis of transaction cost

<!-- b000393 | heading | pages [21] -->
8.1.4 Results of Problem 4

<!-- b000394 | prose | pages [21] -->
The memorandum is attached at the end of the article.

<!-- b000395 | heading | pages [21] -->
8.2 Strength

<!-- b000396 | prose | pages [21] -->
• The model and strategy based on pairs trading are scientiﬁc and reasonable, which can maximize the income. The results obtained have strong conﬁdence.

<!-- b000397 | prose | pages [21] -->
• Compared with other random strategies, LSTM strategies and machine learning strate- gies(XGBoost), the model has stronger proﬁtability and better robustness.

<!-- b000398 | prose | pages [21] -->
• Considering the impact of various market risk factors on trading strategies, it provides theoretical and data support for traders’ decision-making.

<!-- b000399 | heading | pages [21] -->
8.3 Possible Improvements

<!-- b000400 | prose | pages [21] -->
• Select highly relevant assets from richer assets for pairs trading model.

<!-- b000401 | prose | pages [21] -->
• At present, the formula is used to directly determine whether there is an abnormal ﬂuctuation of assets. If the method of statistical learning is used to judge the ﬂuctuation, it may have better accuracy.

<!-- b000402 | prose | pages [21] -->
• In the real world, traders can control risks by adding leverage and shorting. In order to make the process clear and the results reliable, these more complex trading behaviors are not included in the experiment.

<!-- b000403 | heading | pages [22] -->
Memorandum

<!-- b000404 | prose | pages [22] -->
To: The Trader

<!-- b000405 | prose | pages [22] -->
From: Team# 2208834

<!-- b000406 | prose | pages [22] -->
Subject: Pairs trading strategy – higher return and lower risk

<!-- b000407 | prose | pages [22] -->
Date: February 22, 2022

<!-- b000408 | prose | pages [22] -->
Dear Sir or Madame,

<!-- b000409 | prose | pages [22] -->
Although quantitative trading based on machine learning has become very popular in recent years (such as statistical learning, Markov Monte Carlo or recurrent neural networks(RNNs)). However, they rely too much on data quality. Machine learning models are sometimes vulnerable to noisy data in ﬁnancial markets. They don’t perform well, especially with limited data.

<!-- b000410 | prose | pages [22] -->
The data you provided is relatively simple and noisy. Out of caution, we do not choose the black box of machine learning, but establish a math-based trading strategy: pairs-trading. It’s as easy to understand as a transparent box, and risk is manageable.

<!-- b000411 | prose | pages [22] -->
According to your needs, we observe the processed gold price trend and bitcoin price trend, and ﬁnd that there is a certain relationship between them through inspection. In this regard, we conduct Johanson-test on the data after data cleaning and normalization, and the results show that there is a cointegration relationship between them.On this basis, we use the pairs trading model to backtest the data.

<!-- b000412 | prose | pages [22] -->
In order to backtest the policy, we build a backtest system using Python. This backtesting system provides price information to the strategy accorording to trading days, getting a trading order for the strategy, and then trading it. Therefore, if the strategy is separated from the price data, the strategy can only obtain the past data and submit orders to the system.

<!-- b000413 | prose | pages [22, 23] -->
The pairs trading is a trading strategy that involves matching a long position with a short position in two stocks with a high correlation. The model treats bitcoin and gold as two stocks.Diﬀerent from the traditional algorithm that needs to make prediction before decision-making, our pairs trading algorithm has the functions of prediction and decision-making. It can infer the subsequent trend through the previous data trend and make the corresponding trading strategy.

<!-- b000415 | prose | pages [23] -->
For the purpose of proving that our strategy is the best, we compare random algorithm, machine learning algorithm XGBoost and LSTM algorithm, and highlight the advantages of our model from the following aspects:

<!-- b000416 | prose | pages [23] -->
• Sharpe Ratio could evaluate the trade-oﬀof return and risk of an investment. Our pairs trading strategy’s Sharpe Ratio is 1.46. By contrast, other models’ indicators are only below 1. Usually, SR nearly 1.5 indicates investment will have high return with low risk. So our strategy is relatively best.

<!-- b000417 | prose | pages [23] -->
• Information Ratio could indicate the ability of active investment. The indicator within our own pairs trading strategy is approximately three times higher than other existing models.

<!-- b000418 | prose | pages [23] -->
This means our strategy has a great performance of actively intervene risk to obtain higher return.

<!-- b000419 | prose | pages [23] -->
• Tracking error can trade oﬀwhether a strategy would avoid unnecessary risk. The TE of our strategy is a little higher in 2017, but in any other period is always too low. This means the strategy not only has a stronger risk avoidance, but also has a better ability of risk adaptation.

<!-- b000420 | prose | pages [23] -->
It is found that after using our trading strategy, through the diﬀerent conversion and multiple buying and selling operations of two diﬀerent ﬁnancial assets-bitcoin and gold, the $1000 on September 10, 2016 becomes $106986.1 on September 10, 2021.The net asset value has increased by nearly 107 times year-on-year, realizing a great rate of return.

<!-- b000421 | prose | pages [23] -->
Using our model will not only have suﬃcient ﬂexibility and high anti risk ability, but also bring you considerable beneﬁts. If you want to both at ease and earn money, choose our model!

<!-- b000422 | furniture | pages [24] -->
Team # 2208834

<!-- b000423 | furniture | pages [24] -->
Page 23 of 24

<!-- b000424 | heading | pages [24] -->
References

<!-- b000425 | references | pages [24] -->
[1] Charfeddine, L. , & Khediri, K. B. . (2016). Financial development and environmental quality

<!-- b000426 | references | pages [24] -->
in uae: cointegration with structural breaks. Renewable & Sustainable Energy Reviews, 55,

<!-- b000427 | references | pages [24] -->
1322-1335.

<!-- b000428 | references | pages [24] -->
[2] Hodoshima, J. , Dempster, M. , & Gatheral, J. . (2019). Stock performance by utility indiﬀer-

<!-- b000429 | references | pages [24] -->
ence pricing and the Sharpe ratio.

<!-- b000430 | references | pages [24] -->
[3] Selvin, S. , Vinayakumar, R. , Gopalakrishnan, E. A. , Menon, V. K. , & Soman, K. P. . (2017).

<!-- b000431 | references | pages [24] -->
Stock price prediction using LSTM, RNN and CNN-sliding window model. International

<!-- b000432 | references | pages [24] -->
Conference on Advances in Computing. IEEE.

<!-- b000433 | references | pages [24] -->
[4] Gashi, B. , & Date, P. . (2011). Two methods for optimal investment with trading strategies of

<!-- b000434 | references | pages [24] -->
ﬁnite variation. Ima Journal of Management Mathematics, 23(2), 171-194.

<!-- b000435 | references | pages [24] -->
[5] https://www.investopedia.com/terms/p/pairstrade.asp

<!-- b000436 | references | pages [24] -->
[6] https://www.garp.org/white-paper/forecasting-bitcoin-risk-measures-a-robust-approach

<!-- b000437 | references | pages [24] -->
[7] YE Wuyi, SUN Liping, & MIAO Baiqi(2020). A Study of Dynamic Cointegration of Gold

<!-- b000438 | references | pages [24] -->
and Bitcoin Based on Semiparametric MIDAS Quantile Regression Model.(J. Sys. Sci. &

<!-- b000439 | references | pages [24] -->
Math. Scis.)

<!-- b000440 | references | pages [24] -->
[8] Wang, Y. , & Guo, Y. . (2020). Forecasting method of stock market volatility in time series

<!-- b000441 | references | pages [24] -->
data based on mixed model of arima and xgboost. China Communications: English edition,

<!-- b000442 | references | pages [24] -->
17(3), 17.

<!-- b000443 | heading | pages [24] -->
Appendices

<!-- b000444 | heading | pages [24] -->
Appendix A

<!-- b000445 | prose | pages [24] -->
Code Structure and Related Works

<!-- b000446 | prose | pages [24] -->
In this paper, the trading strategy and experimental codes are mainly implemented in Python, and the risk control part is based on Excel, combined with statistical calculation. The speciﬁc application environment is as follows:

<!-- b000447 | furniture | pages [25] -->
Team # 2208834

<!-- b000448 | furniture | pages [25] -->
Page 24 of 24

<!-- b000449 | prose | pages [25] -->
A. Exploratory data analysis(EDA) This part contains: 1. Data reading, basic analysis, visualization; 2. Test related properties of data (such as normal distribution test, stationarity test and cointegration test) according to policy requirements.

<!-- b000450 | prose | pages [25] -->
B. Backtesting system

<!-- b000451 | prose | pages [25] -->
This section constructs a trade environment class [Class TradeEnv(Object)], which contains the relevant attributes needed by the test strategy: [data_dict], [Brokerage], [Account], [History]. Write and encapsulates the correlation function: [Getdata ()], [reset_Trade_data ()], [Record ()], [the Trade ()], and so on.

<!-- b000452 | heading | pages [25] -->
C. Strategy part

<!-- b000453 | prose | pages [25] -->
The four strategies and implementation in this section are shown in the table below:

<!-- b000454 | heading | pages [25] -->
D. Experiment

<!-- b000455 | prose | pages [25] -->
a. Comparative experiment: ﬁnancial mathematical calculation using Excel.

<!-- b000456 | prose | pages [25] -->
b. Robustness and sensitivity test: After encapsulating the experimental environment and strategy, program operation with diﬀerent experimental parameters (Time_range, Brokerage). Fi- nally, collating experimental results.
