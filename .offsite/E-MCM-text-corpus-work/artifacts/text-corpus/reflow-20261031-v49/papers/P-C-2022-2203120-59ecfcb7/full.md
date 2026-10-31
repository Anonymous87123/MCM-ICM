# P-C-2022-2203120-59ecfcb7

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
2203120

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Trading Strategy Model Based on Dynamic

<!-- b000008 | title | pages [1] -->
Programming

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
It is of great signiﬁcance for traders to buy and sell volatile assets reasonably in market transactions. Traders choose diﬀerent trading strategies and get diﬀerent beneﬁts. This paper studies the best trading strategies for diﬀerent traders based on the daily prices of gold and bitcoin in the past.

<!-- b000011 | prose | pages [1] -->
For problem 1, the original data is preprocessed ﬁrstly, including ﬁlling the missing value by the daily price of gold in the past, and standardize all the original data. Following the processed data, the ARIMA model is used to establish the price prediction model. Correlation coeﬃceents between the prediction results and the price of gold and bitcoin are 0.8592 and 0.9304 respectively. The eﬀectiveness of our model is denoted. Thirdly, a dynamic programming model with largest total assets and risk as the regular termis is established, with the constraints hit rate and transaction volume limit. Lastly, the optimal daily trading strategy is solved with dynamic programming method. Final proﬁt is $ 132089.1078 on September 10, 2021.

<!-- b000012 | prose | pages [1] -->
For problem 2, we prove our strategy is the best judged from the generalization ability, robustness and beneﬁt of the model. By adjusting the variable parameters in the model, the strategies suitable for three traders are formed, which are insurance type, common type and radical type. The solution method of problem 1 is used to obtain the changes of each asset and the total earnings of the three trading strategies. Furthermore, the variable parameters in the model are disturbed, and the total assets change within a certain range, indicating that the model has strong anti-interference ability. Finally, the assets obtained by the three types of trading strategies are $14312.6827, $50040.5474 and $132089.1078 respectively. It can be seen that our model yield can resist inﬂation greatly.

<!-- b000013 | prose | pages [1] -->
For problem 3, ﬁrstly, the sensitivity is deﬁned as the change rate of transaction frequency. By changing the transaction cost of gold and bitcoin, it is calculated that the sensitivity of gold transaction cost is 0.0422 and that of bitcoin transaction cost is 0.0658. It can be seen from the comparison that the transaction strategy is more sensitive to the transaction cost of bitcoin. Secondly, the impact of transaction cost on transaction frequency, asset return and asset risk are analyzed. We ﬁnd that when the transaction cost increases, the transaction frequency, asset return and asset risk are decreases correspondingly.

<!-- b000014 | prose | pages [1] -->
For problem 4, we summarize the models and strategies established in the ﬁrst three questions, and introduce to traders in the form of memorandum how to simply use the trading strategy to trade and the beneﬁts brought by diﬀerent trading strategies.

<!-- b000015 | keywords | pages [1] -->
Keywords: quantitative investment; ARIMA model; dynamic programming

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1 Introduction

<!-- b000018 | contents | pages [2] -->
2

<!-- b000019 | contents | pages [2] -->
1.1

<!-- b000020 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
2

<!-- b000022 | contents | pages [2] -->
1.2

<!-- b000023 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
2

<!-- b000025 | contents | pages [2] -->
1.3

<!-- b000026 | contents | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
2

<!-- b000028 | contents | pages [2] -->
2 General Assumptions and Notations

<!-- b000029 | contents | pages [2] -->
4

<!-- b000030 | contents | pages [2] -->
2.1

<!-- b000031 | contents | pages [2] -->
Assumptions

<!-- b000032 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
4

<!-- b000034 | contents | pages [2] -->
2.2

<!-- b000035 | contents | pages [2] -->
Notations

<!-- b000036 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
4

<!-- b000038 | contents | pages [2] -->
3 Problem 1: Prediction and Strategy in the Investment

<!-- b000039 | contents | pages [2] -->
4

<!-- b000040 | contents | pages [2] -->
3.1

<!-- b000041 | contents | pages [2] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
5

<!-- b000043 | contents | pages [2] -->
3.2

<!-- b000044 | contents | pages [2] -->
Model Establishment of Problem 1 . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
5

<!-- b000046 | contents | pages [2] -->
3.2.1

<!-- b000047 | contents | pages [2] -->
Price Prediction Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
5

<!-- b000049 | contents | pages [2] -->
3.2.2

<!-- b000050 | contents | pages [2] -->
Trading Strategy Model

<!-- b000051 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
8

<!-- b000053 | contents | pages [2] -->
3.3

<!-- b000054 | contents | pages [2] -->
Model Solving: Finding Strategies . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
10

<!-- b000056 | contents | pages [2] -->
3.4

<!-- b000057 | contents | pages [2] -->
Results and Model Evaluation

<!-- b000058 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
11

<!-- b000060 | contents | pages [2] -->
3.4.1

<!-- b000061 | contents | pages [2] -->
Model Results

<!-- b000062 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
11

<!-- b000064 | contents | pages [2] -->
3.4.2

<!-- b000065 | contents | pages [2] -->
Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
12

<!-- b000067 | contents | pages [2] -->
4 Problem 2: Prove Optimization of the Strategy

<!-- b000068 | contents | pages [2] -->
12

<!-- b000069 | contents | pages [2] -->
4.1

<!-- b000070 | contents | pages [2] -->
Generalization Ability of the Model

<!-- b000071 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
13

<!-- b000073 | contents | pages [2] -->
4.2

<!-- b000074 | contents | pages [2] -->
Robustness of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
15

<!-- b000076 | contents | pages [2] -->
4.3

<!-- b000077 | contents | pages [2] -->
Yield of the Strategy

<!-- b000078 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
16

<!-- b000080 | contents | pages [2] -->
5 Problem 3: Sensitivity of Strategy to Transaction Cost

<!-- b000081 | contents | pages [2] -->
16

<!-- b000082 | contents | pages [2] -->
5.1

<!-- b000083 | contents | pages [2] -->
Sensitivity Diﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
17

<!-- b000085 | contents | pages [2] -->
5.2

<!-- b000086 | contents | pages [2] -->
Impact of Transaction Costs on Strategy . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
17

<!-- b000088 | contents | pages [2] -->
6 Conclusion

<!-- b000089 | contents | pages [2] -->
18

<!-- b000090 | contents | pages [2] -->
6.1

<!-- b000091 | contents | pages [2] -->
Strengths

<!-- b000092 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
18

<!-- b000094 | contents | pages [2] -->
6.2

<!-- b000095 | contents | pages [2] -->
Possible Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
19

<!-- b000097 | contents | pages [2] -->
7 Memorandum

<!-- b000098 | contents | pages [2] -->
19

<!-- b000099 | contents | pages [2] -->
Appendices

<!-- b000100 | contents | pages [2] -->
23

<!-- b000101 | contents | pages [2] -->
Appendix A Changes of Various Types of Traders’ Assetes

<!-- b000102 | contents | pages [2] -->
23

<!-- b000103 | furniture | pages [3] -->
Team # 2203120

<!-- b000104 | furniture | pages [3] -->
Page 2 of 23

<!-- b000105 | heading | pages [3] -->
1 Introduction

<!-- b000106 | heading | pages [3] -->
1.1 Problem Background

<!-- b000107 | prose | pages [3] -->
Market traders buy and sell volatile assets frequently, with a goal to maximize their total return. There is usually a commission for each purchase and sale. Two such assets are gold and bitcoin.The price changes of bitcoin and gold from September 11, 2016 to September 10, 2021 are shown in

<!-- b000108 | caption | pages [3] -->
Figure 1. The source of gold daily prices is London Bullion Market Association and the source of

<!-- b000109 | prose | pages [3] -->
bitcoin daily prices is NASDAQ.

<!-- b000110 | prose | pages [3] -->
(a) Gold daily prices, U.S. dollars per troy ounce (b) Bitcoin daily prices, U.S. dollars per bitcoin

<!-- b000111 | caption | pages [3] -->
Figure 1: The prices of two assets

<!-- b000112 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000113 | prose | pages [3] -->
In this problem, we are asked by a trader to develop a model that uses only the past stream of daily prices to date to determine each day if the trader should buy, hold, or sell their assets in their portfolio. We will start with $1000 on September 11, 2016 and use the ﬁve-year trading period, from September 11, 2016 to September 10, 2021. On each trading day, the trader will have a portfolio consisting of cash, gold, and bitcoin [C, G, B] in U.S. dollars, troy ounces, and bitcoins, respectively.We should only use these data to solve the following problems:

<!-- b000114 | prose | pages [3] -->
• Develop a model that gives the best daily trading strategy based only on price data up to that day. Use the model and strategy to predict the value of the initial $1000 investment on September 10, 2021.

<!-- b000115 | prose | pages [3] -->
• Present evidence that the model provides the best strategy.

<!-- b000116 | prose | pages [3] -->
• Determine how sensitive the strategy is to transaction costs and how transaction costs aﬀect the strategy and results.

<!-- b000117 | prose | pages [3] -->
• Communicate the strategy, model, and results to the trader in a memorandum of at most two pages.

<!-- b000118 | heading | pages [3] -->
1.3 Problem Analysis

<!-- b000119 | prose | pages [3, 4] -->
For problem 1, The premise of formulating the strategy is to accurately predict the price trend of gold and bitcoin in the future. Therefore, it is necessary to establish a price prediction model to lay the foundation for formulating the strategy. Common time series prediction models include LSTM, BP neural network, RNN, encoder-decoder model, etc. In view of the simplicity and eﬃciency of ARIMA model, which only needs endogenous variables rather than other exogenous variables, we choose to use ARIMA model.

<!-- b000120 | furniture | pages [4] -->
Team # 2203120

<!-- b000121 | furniture | pages [4] -->
Page 3 of 23

<!-- b000123 | prose | pages [4] -->
Next, establish a trading strategy model according to the established indicators, give the trading strategy and calculate the ﬁnal income. Intuitively, the price ﬂuctuation of bitcoin is much greater than that of gold, so we guess the risk is greater than that of gold. Therefore, the risk of investment can be described by the variance of price change. This is essentially a dynamic programming problem. We can quantify the return and risk, take the maximum beneﬁt as the objective function, ﬁnd the constraints and establish the model.

<!-- b000124 | prose | pages [4] -->
With regard to problem 2, The optimization of the model can be proved from three aspects: generalization ability, robustness and proﬁt. The generalization ability of the model is reﬂected in that changing the parameters in the model can make the model formulate diﬀerent kinds of strategies. Therefore, we divide the strategies into insurance type, common type and radical type. The robustness of the model means that small changes in parameters will not aﬀect the overall strategy, and the anti-interference of the model is strong. It also shows that compared with other investments, our strategy has a better rate of return.

<!-- b000125 | prose | pages [4] -->
As for problem 3, It is known that the transaction cost is the Commission. Intuitively, the increase of commission should appropriately reduce the transactions. The decrease of commission can increase the number of transactions. The ultimate goal is to maximize the income. Based on the transaction strategy model established by the ﬁrst question, by changing the cost α in the model and observing the corresponding changes of transaction frequency, asset return and asset risk, we can get the sensitivity of three types of strategies to transaction cost.

<!-- b000126 | caption | pages [4] -->
Figure 2: Overall structure

<!-- b000127 | furniture | pages [5] -->
Team # 2203120

<!-- b000128 | furniture | pages [5] -->
Page 4 of 23

<!-- b000129 | heading | pages [5] -->
2 General Assumptions and Notations

<!-- b000130 | heading | pages [5] -->
2.1 Assumptions

<!-- b000131 | prose | pages [5] -->
To simplify our problems, we make the following basic assumptions, each of which is adequately justiﬁed.

<!-- b000132 | prose | pages [5] -->
• All data are authentic.

<!-- b000133 | prose | pages [5] -->
• The investor is physically and mentally healthy and has no burden such as huge loans.

<!-- b000134 | prose | pages [5] -->
• Without considering inﬂation and other economic changes in recent years, only tabular data are used.

<!-- b000135 | prose | pages [5] -->
• All transactions are conducted in US dollars. The commission is deducted from the amount paid instead of being given separately.

<!-- b000136 | prose | pages [5] -->
• Since it is only US $1000, the minimum transaction unit of US dollar and bitcoin under normal circumstances is not considered for the universality of the model.

<!-- b000137 | heading | pages [5] -->
2.2 Notations

<!-- b000138 | prose | pages [5] -->
In this work, we use the nomenclature in Table 1 in the model construction. Other none- frequent-used symbols will be introduced once they are used.

<!-- b000139 | caption | pages [5] -->
Table 1: Notations

<!-- b000140 | prose | pages [5] -->
Symbols Descripition

<!-- b000141 | prose | pages [5] -->
t1 = 3, t2 = 3 gold trading cycle (including holidays), bitcoin trading cycle n number of cycles in ﬁve years DSgi, DSbi hit rate of training prediction model, i=2,3...n Ri = [Ci Gi Bi] asset distribution in the i-th cycle, R0 = [1000 0 0] Ai total assets in the i-th cycle, A0=1000 qi proportion of cash in total assets in the i-th cycle ei, fi threshold of increase or decrease in the i-th cycle Xg(i), Xb(i) forecast average price in the i-th cycle Yg(i), Yb(i) real average price of gold in the i-th cycle αg, αb proportion of commission of each transaction in the transaction amount R2 gi, R2 decision coeﬃcient of the trained model in the i-th cycle bi

<!-- b000142 | heading | pages [5] -->
3 Problem 1: Prediction and Strategy in the Investment

<!-- b000143 | prose | pages [5] -->
In this section, based on the existing data, we use ARIMA model to predict the price trend of gold and bitcoin in the future, so as to establish a model and give the best daily trading strategy. Dynamic programming is used to estimate the value of the initial $1000 investment by September 10, 2021.

<!-- b000144 | furniture | pages [6] -->
Team # 2203120

<!-- b000145 | furniture | pages [6] -->
Page 5 of 23

<!-- b000146 | heading | pages [6] -->
3.1 Data Preprocessing

<!-- b000147 | prose | pages [6] -->
Before data analysis, the availability of data must be guaranteed.

<!-- b000148 | prose | pages [6] -->
• Missing value processing. Unlike bitcoin, which is traded daily, gold is traded only on trading days, so the data is not continuous. For the convenience of subsequent modeling, the missing value is ﬁlled with the mean value before and after the day.

<!-- b000149 | prose | pages [6] -->
• Data standardization. In regression prediction, standardization gives eigenvalues equal weight. Since we predict by period, we process the data by period. Calculate the mean(¯x) and standard deviation(SD) of data(x), then the processed data x′ = (x−¯x) SD .

<!-- b000150 | heading | pages [6] -->
3.2 Model Establishment of Problem 1

<!-- b000151 | heading | pages [6] -->
3.2.1 Price Prediction Model

<!-- b000152 | prose | pages [6] -->
Improving forecasting especially time series forecasting accuracy is an important yet often diﬃcult task facing decision makers in many areas. Autoregressive integrated moving average (ARIMA) models are one of the most popular linear models in time series forecasting, which have been widely applied in order to construct more accurate hybrid models during the past decade [2].

<!-- b000153 | prose | pages [6] -->
ARIMA model combines three basic methods:

<!-- b000154 | prose | pages [6] -->
• Autoregressive(AR). Describe the relationship between the current value and the historical value, and use the historical time data of the variable to predict itself. The order of AR model is recorded as p value.The formula is as follows:

<!-- b000155 | prose | pages [6] -->
yt = α0 + α1yt−1 + α2yt−2 + · · · + αpyt−p + ϵt (1)

<!-- b000156 | prose | pages [6] -->
where, and α is the coeﬃcient, ϵt stands for error.

<!-- b000157 | prose | pages [6] -->
• Integrated(I). When the time series becomes stationary, the diﬀerence needs to be made, and the order of the diﬀerence is recorded as d value. Generally, ﬁrst order is enough.

<!-- b000158 | prose | pages [6] -->
• Moving average(MA). Moving average model focuses on the accumulation of error terms in autoregressive model. The order of MA model is recorded as q value.The formula is as follows:

<!-- b000159 | prose | pages [6] -->
yt = c + ϵt + θ1ϵt−1 + θ2ϵt−2 + · · · + θqϵt−q (2)

<!-- b000160 | prose | pages [6] -->
where, c represents the constant term, ϵt is the white noise process of variance, and θ is the coeﬃcient.

<!-- b000161 | prose | pages [6] -->
The model is called ARIMA (p, d, q), as shown in the ﬁgure3, where p is the autoregressive term, q is the moving average term, and D is the number of diﬀerences. We will follow the steps listed below to build and solve our model.

<!-- b000162 | furniture | pages [7] -->
Team # 2203120

<!-- b000163 | furniture | pages [7] -->
Page 6 of 23

<!-- b000164 | caption | pages [7] -->
Figure 3: Structure of ARIMA model

<!-- b000165 | prose | pages [7] -->
step1 Stabilization To use ARIMA model, the time series must be stationary. We use the Augmented Dickey- fuller unit root test to test the stationarity. If the P value obtained from ADF test is less than 0.05, it is a stable time series. If it is unstable, we convert the non-stationary process into a stationary process by diﬀerence method. It can be seen from the table 2 that the time series becomes stable after the ﬁrst-order diﬀerence.

<!-- b000166 | caption | pages [7] -->
Table 2: P value of gold and bitcoin time series before and after diﬀerence

<!-- b000167 | prose | pages [7] -->
P value before diﬀerence P value after diﬀerence

<!-- b000168 | prose | pages [7] -->
gold 0.6734 0.0043 bitcoin 0.9921 0.0000

<!-- b000169 | prose | pages [7] -->
step2 Selection of p and q Use autocorrelation function(ACF) and partial autocorrelation function(PACF) to determine the values of p and q. the conﬁrmation method is shown in the table 3.

<!-- b000170 | caption | pages [7] -->
Table 3: Conﬁrmation method of p value and q value

<!-- b000171 | prose | pages [7] -->
Model ACF PACF

<!-- b000172 | prose | pages [7] -->
AR(P) attenuation tends to 0 truncation after p-order MA(q) truncation after q-order attenuation tends to 0 ARMA(p, q) attenuation tends to 0 after q-order attenuation tends to 0 after p-order

<!-- b000173 | prose | pages [7] -->
NOTE: Truncation means falling within the conﬁdence interval (95% of the points comply with the rule)

<!-- b000174 | caption | pages [7] -->
Figure 4 (a) shows the truncation of gold data using level 2 ACF and level 1 PACF, and

<!-- b000175 | caption | pages [7] -->
Figure 4 (b) shows the truncation of bitcoin data using level 2 ACF and level 2 PACF. From

<!-- b000176 | prose | pages [7] -->
this, we can determine the p value and q value respectively.

<!-- b000177 | furniture | pages [8] -->
Team # 2203120

<!-- b000178 | furniture | pages [8] -->
Page 7 of 23

<!-- b000179 | prose | pages [8] -->
(a) ACF chart and PACF chart of gold (b) ACF chart and PACF chart of bitcoin

<!-- b000180 | caption | pages [8] -->
Figure 4: ACF chart and PACF chart

<!-- b000181 | prose | pages [8] -->
step3 White noise test If the white noise is obtained, it means that the useful information in the time series has been extracted, and the rest are all random disturbances, which cannot be predicted and used.[9] If the residual sequence passes the white noise test, the modeling can be terminated, because there is no information to continue to extract.

<!-- b000182 | prose | pages [8] -->
The ARIMA model of gold is ARIMA(2,1,1) and bitcoin is ARIMA(2,1,2). The p value of the white noise test output of this model is very close to 0, indicating that it follows the normal distribution with the mean value of 0, that is, it is a white noise.

<!-- b000183 | prose | pages [8] -->
step4 Prediction In order to predict the future market timely and accurately, we use the data of 30 consecutive days as the training set and the data of the next 3 days as the test set. The moving step of the training set is 3. The prediction results of one cycle are shown in the ﬁgure 5. The correlation coeﬃcient R2 of gold is 0.8592 and that of bitcoin is 0.9304. The prediction results of the model are relatively successful and can be used.

<!-- b000184 | prose | pages [8] -->
(a) Forecast chart of gold in one cycle (b) Forecast chart of bitcoin in one cycle

<!-- b000185 | caption | pages [8] -->
Figure 5: Forecast charts in one cycle

<!-- b000186 | furniture | pages [9] -->
Team # 2203120

<!-- b000187 | furniture | pages [9] -->
Page 8 of 23

<!-- b000188 | heading | pages [9] -->
3.2.2 Trading Strategy Model

<!-- b000189 | prose | pages [9] -->
The best daily trading strategy is given only according to the price data. We need to judge the forecast data and give the strategy according to the forecast. Therefore, we deﬁne variable parameters as shown in the table 4 to quantify the strategy.

<!-- b000190 | caption | pages [9] -->
Table 4: Variable parameters

<!-- b000191 | prose | pages [9] -->
Symbols Descripition

<!-- b000192 | prose | pages [9] -->
β, γ proportion of increase or decrease DS hit rate wH, wL purchase proportion, H/L stands for a higher/lower proportion m selling proportion R2 threshold of Decision coeﬃcient R2 i q cash retention ratio

<!-- b000193 | prose | pages [9] -->
Decision coeﬃcient(R2): it is used to evaluate the volatility predicted by the model. The closer the index value is to 1, the higher the ﬁtting performance of the model.

<!-- b000194 | prose | pages [9] -->
  2 Pt xi,j −Y(i) j=1 R2 i = (3)   2 Pt yi,j −Y(i) j=1

<!-- b000195 | prose | pages [9] -->
where xi,j represents the predicted value of day j in cycle i and yi,j represents the actual value of day j in cycle iand Y(i) represents the mean of the true value in cycle i.

<!-- b000196 | prose | pages [9] -->
Hit rate(DS): it is used to evaluate the accuracy of the model in predicting the rise and fall, so as to evaluate the prediction of the long-term trend of the model.

<!-- b000197 | prose | pages [9] -->
( Xt , (xi,j+1 −xi,j) (yi,j+1 −yi,j) ⩾0 1 DSi = 1 j=1 dj × 100% ; dj = j = 1, 2, 3 (4) t 0 , else

<!-- b000198 | prose | pages [9] -->
where di represents the predicted rise and fall in cycle i. If the rise and fall of the real value is the same as that of the predicted value, it is 1, on the contrary, it is 0.

<!-- b000199 | prose | pages [9] -->
In addition, we make the following assumptions:

<!-- b000200 | prose | pages [9] -->
• The period from September 11, 2016 to November 11, 2016 is the zero cycle, and no transaction is conducted as the experience accumulation period. Since November 12, 2016 is the ﬁrst cycle, the number of cycles is n = 588.

<!-- b000201 | prose | pages [9] -->
• If the transaction starts from the second cycle, the asset situation in the ﬁrst week is the same as that in the zero cycle.

<!-- b000202 | prose | pages [9] -->
• Since gold is not traded during holidays, when the predicted value of gold price in a certain period is empty, it means that gold is not traded in that period.

<!-- b000203 | furniture | pages [10] -->
Team # 2203120

<!-- b000204 | furniture | pages [10] -->
Page 9 of 23

<!-- b000205 | prose | pages [10] -->
• The Commission is deducted from the amount paid instead of being given separately.

<!-- b000206 | prose | pages [10] -->
We use i to record the cycle, in which cycle 0 is the experience accumulation period, which only predicts and does not trade. 3 days is a cycle. We use j to record the day. The total number of cycles is 588. Pay attention to the diﬀerence between trading days of gold and bitcoin.

<!-- b000207 | prose | pages [10] -->
To build a strategy model, we need to ﬁnd the objective function and constraints. To make more proﬁts, we need to make the risk as small as possible and the proﬁt as much as possible. Firstly, we quantify the risk and set the standard deviation of assets owned in the transaction process as the risk index S: v  2 u ∑i−1 u Pi−1 j=i−30 Ai u Ai − t j=i−30 30 Sj = (5) 30

<!-- b000208 | prose | pages [10] -->
Calculate the amount of cash:

<!-- b000209 | prose | pages [10] -->
( Ci−1 −Gi × wg , Xg(i) −Yg(i−1) > βg × Ai−1 Ci = (6) Ci−1 + Gi × mg × (1 −αg) × Yg(i+1) , Yg(i−1) −Xg(i) > γg × Ai−1 ( Ci−1 −Bi × wb , Xb(i) −Yb(i−1) > βb × Ai−1 Ci = Ci−1 + Bi × mb × (1 −αb) × Yb(i+1) , Yb(i−1) −Xb(i−1) > γb × Ai−1

<!-- b000210 | prose | pages [10] -->
Calculate the amount of gold and bitcoin:

<!-- b000211 | prose | pages [10] -->
( Gi−1 + Ci × wg × (1 −αg) Gi = (7) Gi−1 −Gi−1 × mg ( Gi−1 + Bi × wb × (1 −αb) Bi = Gi−1 −Gi−1 × mb

<!-- b000212 | prose | pages [10] -->
Then the total asset formula is:

<!-- b000213 | prose | pages [10] -->
Ai = Ci + Gi × Yg(i) + Bi × Yb(i) (8)

<!-- b000214 | prose | pages [10] -->
Finally, the objective function and constraints are determined, and the trading strategy model is obtained:

<!-- b000215 | prose | pages [10, 11] -->
wj,mj Aj −λ × Sj max (9)   Cj, Gj, Bj, Aj ⩾0      DSj ⩾0.5  s.t. Cj ⩾Aj × q    αg = 1%, αb = 2%     A0 = 1000, C0 = C1 = 1000, G0 = G1 = B0 = B1 = 0 where, Wj represents the roportion of gold and bitcoin bought on day j, mj represents the roportion of gold and bitcoin sought on day j, Aj represents the total assets on day j, λ represents the coeﬃcient of regular term, which is used to control risk and return, Sj represents the current day risk. The ﬁrst constraint indicates that all assets are positive, the second constraint indicates that the accuracy of the model is greater than 0.5, the third constraint indicates that the remaining capital of the transaction is greater than q times of the total assets, and α indicates the transaction cost, A0, C0, G0, B0 represents the total assets, cash, gold and bitcoin before the ﬁrst day of trading, C1, G1, B1 represents the amount of cash, gold and bitcoin before trading on day 2.

<!-- b000216 | furniture | pages [11] -->
Team # 2203120

<!-- b000217 | furniture | pages [11] -->
Page 10 of 23

<!-- b000219 | heading | pages [11] -->
3.3 Model Solving: Finding Strategies

<!-- b000220 | prose | pages [11] -->
After the trading strategy model is established, we need to solve the model. The speciﬁc steps are as follows:

<!-- b000221 | prose | pages [11] -->
step1 Datainitialization. Set i = 1, knowαg = 1%, set parameterβg, γg, ds, R2, wHg, wLg, mg, q, initial asset distributionR1 = R0 = [1000 0 0], total assets r1 = r0 = 1000.

<!-- b000222 | prose | pages [11] -->
step2 Calculate hit rate (DS). The prediction model hit rate(Formula 4) can evaluate the accuracy of the trained model in predicting the rise and fall. When the accuracy is high enough, you can continue to follow the next steps.

<!-- b000223 | prose | pages [11] -->
step3 Determine whether to trade. Firstly, due to the cost in the transaction, in order to avoid excessive cost caused by frequent transaction, the transaction is carried out only when the increase and decrease reach a certain threshold. Secondly, in order to avoid too little cash left in the transaction, the transaction can be carried out only when the cash meets the reserved amount. The speciﬁc process is shown in the ﬁgure 6.

<!-- b000224 | caption | pages [11] -->
Figure 6: The process of determining whether to trade

<!-- b000225 | prose | pages [11] -->
where, eg(i+1) = βg × Ai (10) fg(i+1) = γg × Ai (11) Ci qi = (12) Ci + Gi × Yg(i) + Bi × Yb(i) in the formula, βg, γg represents the proportion of increase or decrease.

<!-- b000226 | furniture | pages [12] -->
Team # 2203120

<!-- b000227 | furniture | pages [12] -->
Page 11 of 23

<!-- b000228 | prose | pages [12] -->
step4 Determine the number of transactions. Prediction model discrimination coeﬃcient R2 gi can evaluate the volatility predicted by the trained model. The smaller the variable, the more stable the model is, and the proportion of buying gold during trading can be increased. The speciﬁc process is shown in the ﬁgure 7.

<!-- b000229 | caption | pages [12] -->
Figure 7: The process of determining the number of transactions

<!-- b000230 | prose | pages [12] -->
Where, the formula for total assets is

<!-- b000231 | prose | pages [12] -->
Ai+1 = Ci+1 + Gi+1 × Yg(i+1) + Bi+1 × Yb(i+1) (13)

<!-- b000232 | prose | pages [12] -->
When proportions WHg, WLg and mg are used respectively, the formula for calculating asset distribution is  Ci+1 = Ci −Ci × wLg   Gi+1 = Gi + Ci×wLg×(1−αg) RWHg = (14) Yg(i+1)   Bi+1 = Bi  Ci+1 = Ci −Ci × wHg   Gi+1 = Gi + Ci×wHg×(1−αg) RWLg = (15) Yg(i+1)   Bi+1 = Bi  Ci+1 = Ci −Ci × wLg   Gi+1 = Gi + Ci×wLg×(1−αg) Rmg = (16) Yg(i+1)   Bi+1 = Bi In the formula, Yg(i+1) represents the real average price of gold on (i+1) day.

<!-- b000233 | heading | pages [12] -->
3.4 Results and Model Evaluation

<!-- b000234 | heading | pages [12] -->
3.4.1 Model Results

<!-- b000235 | prose | pages [12, 13] -->
Using Python Programming and our model, set variable parameters: βb = 0, βg = 0.5, γb = 0.3, γg = 0.3, wHg = 0.8, wHb = 0.4, q = 0.01, the initial investment value of $1000 will be $132089.11 by September 10, 2021. The number of transactions is 9, and the ﬁnal asset distribution [C,G,B]=[22.31, 0.16, 2.84]. The changes of assets during the ﬁve-year period are shown in the ﬁgure below.

<!-- b000236 | furniture | pages [13] -->
Team # 2203120

<!-- b000237 | furniture | pages [13] -->
Page 12 of 23

<!-- b000239 | caption | pages [13] -->
Figure 8: The changes of total assets during the ﬁve-year period

<!-- b000240 | heading | pages [13] -->
3.4.2 Model Evaluation

<!-- b000241 | prose | pages [13] -->
This result is obtained using two models. Firstly, ARIMA model is used for prediction, and we get good results: The correlation coeﬃcient R2 of gold is 0.8592 and that of bitcoin is 0.9304. They are close to 1, indicating that the predicted value is highly correlated with the real value.

<!-- b000242 | prose | pages [13] -->
Through the trading strategy model, we get speciﬁc beneﬁts. The strategy model has high availability:

<!-- b000243 | prose | pages [13] -->
• The model is only based on the price changes of gold and bitcoin in recent ﬁve years, so the model has low requirements for data.

<!-- b000244 | prose | pages [13] -->
• Our model puts forward variable parameters such as β, γ, wH, wL, m, q to form a parameter list. By changing the parameters in the list, we can achieve diﬀerent income results. In the future, we can form an investment prediction software according to the model. We only need to understand the meaning of relevant parameters to realize asset management. Therefore, our model is relatively simple and easy to understand.

<!-- b000245 | prose | pages [13] -->
• The parameters in the model have a large variable range and are more ﬂexible.

<!-- b000246 | prose | pages [13] -->
These ensures the reliability of the results.

<!-- b000247 | heading | pages [13] -->
4 Problem 2: Prove Optimization of the Strategy

<!-- b000248 | prose | pages [13, 14] -->
Our model proposes multiple variable parameters, which can achieve diﬀerent beneﬁts by changing parameters, so the model has good generalization ability. At the same time, the small change of parameters will not aﬀect the overall strategy, and the model is robust. Compared with other investments, our strategy has a better rate of return. The following will explain the generalization ability, robustness and proﬁt margin of the model to prove the optimization of the strategy.

<!-- b000249 | furniture | pages [14] -->
Team # 2203120

<!-- b000250 | furniture | pages [14] -->
Page 13 of 23

<!-- b000252 | heading | pages [14] -->
4.1 Generalization Ability of the Model

<!-- b000253 | prose | pages [14] -->
Successful investment comes from two factors: one is traders’ correct understanding of the market, and the other is trading rationality. According to the reference materials[7], we divide traders into the following three types:

<!-- b000254 | prose | pages [14] -->
• Insurance-type. The purpose of such traders’ investment behavior is mainly to obtain long- term capital income, that is, they hope to obtain investment income regularly, and also hope to obtain diﬀerential proﬁts through the change of capital price in a longer term. At the same time, before investing, traders should generally master suﬃcient information and make a rational analysis of the expected proﬁts and risks of the target assets.

<!-- b000255 | prose | pages [14] -->
• Common-type. The purpose of such traders is mainly to obtain large proﬁts in a short period of time and are willing to bear some risks. Its way mainly depends on the short-term price ﬂuctuation diﬀerence to obtain proﬁts. They take technical analysis as the main means and make speculative decisions based on historical price ﬂuctuation experience. Generally speaking, the probability of success of Common-type investors is not low, but the probability of failure is also high. Its behavior has strong subjective initiative, and the probability of success depends on its accuracy in predicting market ﬂuctuations.

<!-- b000256 | prose | pages [14] -->
• Radical-type. The characteristics of radical traders’ behavior are based on luck and oppor- tunity, trading in the market with luck and hoping to make huge proﬁts in the short term.

<!-- b000257 | prose | pages [14] -->
Generally speaking, the risk is very high. Unless they need money urgently, have the psy- chology of gamblers or have the ability to take risks, most people will not use this investment method.

<!-- b000258 | prose | pages [14] -->
In the model, for three types of traders, the corresponding parameters are adjusted as shown in the

<!-- b000259 | caption | pages [14] -->
table 5:

<!-- b000260 | caption | pages [14] -->
Table 5: Adjustment of variable parameters

<!-- b000261 | prose | pages [14] -->
variable parameters Insurance-type Common-type Radical-type

<!-- b000262 | prose | pages [14] -->
βb 0.35 0.10 0 βg 0.50 0.50 0.50 γg 0.10 0.20 0.30 γb 0.10 0.20 0.30 wHg 0.95 0.80 0.80 wHb 0.15 0.30 0.40 q 0.15 0.05 0.01

<!-- b000263 | prose | pages [14, 15] -->
Solve the model according to diﬀerent parameters adjustments and get the changes of various types of traders’ assets. The ﬁgure 9 shows the changes of various assets of insurance-type traders in ﬁve years. See the Appendix A for the ﬁgures of the other two types.

<!-- b000264 | furniture | pages [15] -->
Team # 2203120

<!-- b000265 | furniture | pages [15] -->
Page 14 of 23

<!-- b000267 | prose | pages [15] -->
(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin

<!-- b000268 | caption | pages [15] -->
Figure 9: Changes of various assets of insurance-type traders

<!-- b000269 | prose | pages [15] -->
The changes of total assets of three types of traders are shown in the ﬁgure 10:

<!-- b000270 | prose | pages [15] -->
(a) Insurance-type (b) Common-type (c) Radical-type

<!-- b000271 | caption | pages [15] -->
Figure 10: Changes in total assets of three types of traderss

<!-- b000272 | caption | pages [15] -->
Table 6: Results of three types of strategies

<!-- b000273 | prose | pages [15] -->
Insurance-type Common-type Radical-type

<!-- b000274 | prose | pages [15] -->
Total assets 14312.68 50040.55 132089.11 [C, G, B] [11474.39, 1.59, 1.07] [421.14, 0.61, 1.05] [22.31, 0.16, 2.84] Number of transactions 85 58 9 SD 3861.73 15501.99 40067.35 R2 0.94 0.27 0.24 g R2 0.41 0.98 0.99 b

<!-- b000275 | prose | pages [15] -->
NOTE: R2 g/R2 b represent correlation between gold/bitcoin purchase and actual ﬂuctuation, SD represent standard deviation of 5-year assets.

<!-- b000276 | prose | pages [15, 16] -->
Reading the data in the table 8, although radical investors have more returns, the value of SD is very large, that is, assets change greatly, so they have to bear corresponding risks. It can be seen from the number of transactions that any disturbance in the market may disturb insurance investors. From R2, we can ﬁnd that the more traders tend to venture capital, the more they will buy bitcoin; Gold symbolizes stable and conservative investment. Thus, our model gives a variety of practical and feasible strategies.

<!-- b000277 | furniture | pages [16] -->
Team # 2203120

<!-- b000278 | furniture | pages [16] -->
Page 15 of 23

<!-- b000280 | heading | pages [16] -->
4.2 Robustness of the Model

<!-- b000281 | prose | pages [16] -->
In practical problems, the perturbation of system characteristics or parameters is often inevitable. The good robustness of the model means that the model has strong anti-interference ability, which means that the system has the ability to maintain a certain performance under the disturbance of uncertainty. As shown in the ﬁgure 11, ﬁgure 12, ﬁgure 13, they show the changes of total assets when disturbing the WH, WL and M parameters of gold and bitcoin respectively.

<!-- b000282 | prose | pages [16] -->
(a) gold (b) bitcoin

<!-- b000283 | caption | pages [16] -->
Figure 11: The impact of wL on total assets

<!-- b000284 | prose | pages [16, 17] -->
(a) gold (b) bitcoin (a) gold (b) bitcoin

<!-- b000285 | caption | pages [16] -->
Figure 12: The impact of wH on total assets

<!-- b000286 | furniture | pages [17] -->
Team # 2203120

<!-- b000287 | furniture | pages [17] -->
Page 16 of 23

<!-- b000289 | caption | pages [17] -->
Figure 13: The impact of m on total assets

<!-- b000290 | prose | pages [17] -->
As can be seen from the ﬁgure above, if these variables are disturbed, the ﬁnal income of the model is stable within a certain range. In fact, if the other parameters β, γ, q are disturbed, the ﬁnal return and investment risk of the model are stable within a certain range. The model has good robustness, so it is proved that the strategy we give is the best.

<!-- b000291 | heading | pages [17] -->
4.3 Yield of the Strategy

<!-- b000292 | prose | pages [17] -->
In the real economic market, because the issue of paper money sometimes exceeds the actual amount needed in circulation, there is often inﬂationso we need to manage money.Under diﬀerent levels of inﬂation, the portfolio is diverse.In reality, money, stocks and bonds are generally used as investment representatives.The portfolio in this question only includes gold ,bitcoin and cash.

<!-- b000293 | prose | pages [17] -->
Set the bank deposit interest rate as r, inﬂation rate as I,deposit amount as a, Then the actual value of the deposit after ﬁve years is

<!-- b000294 | prose | pages [17] -->
A = a(1+r−I)5 (17)

<!-- b000295 | prose | pages [17] -->
Where A represents the actual value of the money after ﬁve years of deposit in the bank.

<!-- b000296 | prose | pages [17] -->
It can be seen from the data, from 2016 to 2021,the inﬂation rate was 7%, the bank deposit interest rate was 0.5%, so the actual value of $1000 after ﬁve years is $139.2436.In contrast, with our portfolio, our total assets are $14312.6827, $50040.5474 and $132089.1078 respectively when we choose insurance, common and radical investments. The results obtained by our model are several times higher than the more conservative ﬁnancial behavior, so our model has higher income and can resist inﬂation.

<!-- b000297 | heading | pages [17] -->
5 Problem 3: Sensitivity of Strategy to Transaction Cost

<!-- b000298 | prose | pages [17] -->
Based on the transaction strategy model established by the ﬁrst question, we can get the sensitivity of the strategy to the transaction cost by changing the cost α in the model and observing the corresponding changes of transaction frequency, asset return and asset risk.

<!-- b000299 | furniture | pages [18] -->
Team # 2203120

<!-- b000300 | furniture | pages [18] -->
Page 17 of 23

<!-- b000301 | heading | pages [18] -->
5.1 Sensitivity Diﬁnition

<!-- b000302 | prose | pages [18] -->
Set initial variable α by α0, the initial transaction frequency h is h0 . After changing K(k = 1, 2, ..., 10) times, the variable α by αk. The corresponding transaction frequency h is hk.Sensitivity is deﬁned as: P10 |hk−hk−1| × 100% k=1 hk−1 (18) 10

<!-- b000303 | prose | pages [18] -->
This indicator reﬂects the change rate of transaction frequency.

<!-- b000304 | heading | pages [18] -->
5.2 Impact of Transaction Costs on Strategy

<!-- b000305 | prose | pages [18] -->
In question 2, we divide the strategy model into insurance type, common type and radical type. When exploring the impact of cost on strategy, we should also consider these three aspects. Let’s take the common type as an example to explore the impact of various changes of α on the strategy. We mainly explore through transaction frequency, asset return and asset risk, in which asset risk is characterized by the variance of return. Speciﬁcally, it is investigated through the changes of the following four costs.

<!-- b000306 | prose | pages [18] -->
a. αg fell 0.1% each time and αb remained unchanged.

<!-- b000307 | prose | pages [18] -->
b. αg remained unchanged and αb fell 0.2% each time.

<!-- b000308 | prose | pages [18] -->
c. αg rise 1% each time and αb remained unchanged.

<!-- b000309 | prose | pages [18] -->
d. αg remained unchanged and αb rise 2% each time.

<!-- b000310 | caption | pages [18] -->
Figure 14 shows the change of strategy in case a. It can be seen from the ﬁgure that a small

<!-- b000311 | prose | pages [18] -->
change in the cost of gold will not have an impact on traders’ decisions.

<!-- b000312 | prose | pages [18] -->
(a) Changes of transaction frequency (b) Changes of return (c) Changes of risk

<!-- b000313 | caption | pages [18] -->
Figure 14: Change of strategy in case a

<!-- b000314 | prose | pages [18] -->
The result of case c is shown in the ﬁgure 15. In this case, we increase the transaction cost of gold by 0.1% each time. After reading the picture, it is found that:

<!-- b000315 | prose | pages [18] -->
1. If the cost increases to a certain extent, it will reduce the number of transactions and the total income.

<!-- b000316 | furniture | pages [19] -->
Team # 2203120

<!-- b000317 | furniture | pages [19] -->
Page 18 of 23

<!-- b000318 | prose | pages [19] -->
2. The cost increases, the transactions become less, and the possible risks are reduced.

<!-- b000319 | prose | pages [19] -->
3. The changes of the three indicators are synchronous and consistent.

<!-- b000320 | prose | pages [19] -->
It can be seen that in the face of the continuous rise in the cost of gold, our model has not ignored, keenly felt this signal, and the change direction is in line with the reality. The strategy is relatively sensitive to transaction costs.

<!-- b000321 | prose | pages [19] -->
(a) Changes of transaction frequency (b) Changes of return (c) Changes of risk

<!-- b000322 | caption | pages [19] -->
Figure 15: Change of strategy in case c

<!-- b000323 | caption | pages [19] -->
Table 7 lists the sensitivity of the strategies of the three transaction types to the cost of gold and

<!-- b000324 | prose | pages [19] -->
bitcoin respectively.

<!-- b000325 | caption | pages [19] -->
Table 7: The sensitivity of three types of strategies to two costs

<!-- b000326 | prose | pages [19] -->
Insurance-type Common-type Radical-type

<!-- b000327 | prose | pages [19] -->
αg 0.0267 0.0422 0 αb 0.2308 0.0658 0.0123

<!-- b000328 | prose | pages [19] -->
Through the data in the table, we can ﬁnd that:

<!-- b000329 | prose | pages [19] -->
• The sensitivity of trading strategy to the cost of bitcoin is higher than that to the cost of gold.

<!-- b000330 | prose | pages [19] -->
• The insurance-type strategy is more sensitive to the cost of bitcoin, and the common-type strategy is more sensitive to the cost of gold.

<!-- b000331 | prose | pages [19] -->
• The sensitivity of radical-tupe strategy to cost is generally low.

<!-- b000332 | heading | pages [19] -->
6 Conclusion

<!-- b000333 | heading | pages [19] -->
6.1 Strengths

<!-- b000334 | prose | pages [19, 20] -->
• Our model puts forward variable parameters to form a parameter list. By changing the parameters in the list, we can achieve diﬀerent income results. In the future, we can form an investment prediction software according to the model. We only need to understand the meaning of relevant parameters to realize asset management. Therefore, our model is relatively simple and easy to understand.

<!-- b000335 | furniture | pages [20] -->
Team # 2203120

<!-- b000336 | furniture | pages [20] -->
Page 19 of 23

<!-- b000338 | prose | pages [20] -->
• The parameters in the model have a large variable range and are more ﬂexible.

<!-- b000339 | prose | pages [20] -->
• The model is only based on the price changes of gold and bitcoin in recent ﬁve years, so the model has low requirements for data.

<!-- b000340 | heading | pages [20] -->
6.2 Possible Improvements

<!-- b000341 | prose | pages [20] -->
• In the process of solving the model, the mixed purchase strategy of gold and bitcoin is not well considered, which needs to be improved.

<!-- b000342 | prose | pages [20] -->
• Due to the lack of ﬁnancial knowledge, the establishment of the model is not necessarily perfect.

<!-- b000343 | heading | pages [20] -->
7 Memorandum

<!-- b000344 | heading | pages [20] -->
Memorandum

<!-- b000345 | prose | pages [20] -->
To: traders

<!-- b000346 | prose | pages [20] -->
From: Team #2203120

<!-- b000347 | heading | pages [20] -->
Subject: Investment model, Trading Strategy and Results of Bitcoin and Gold

<!-- b000348 | prose | pages [20] -->
Date: February 22, 2022

<!-- b000349 | prose | pages [20] -->
With the development of economy and the popularization of ﬁnancial management concept, more and more people have joined the ranks of investment. In addition to the traditional treasury bonds, funds, stocks, gold and so on, virtual currency has increasingly appeared in people’s vision, setting oﬀa "currency speculation fever". Investment involves both returns and risks. In order to explore the best trading strategy, our team has established a trading strategy model based on the price trend of gold and bitcoin in the past ﬁve years to help you better invest.

<!-- b000350 | prose | pages [20] -->
STRATEGY

<!-- b000351 | prose | pages [20] -->
The strategy we designed mainly focuses on three questions: when to trade, what kind of assets to trade and how much to trade.

<!-- b000352 | furniture | pages [21] -->
Team # 2203120

<!-- b000353 | furniture | pages [21] -->
Page 20 of 23

<!-- b000354 | caption | pages [21] -->
Figure 16: Structure of transaction strategy model

<!-- b000355 | prose | pages [21] -->
When to trade. We measured the hit rate of the current model, the rise and fall of gold • and bitcoin, and the proportion of cash after trading. Only when the three indicators meet the trading conditions at the same time can the transaction be carried out, and it is decided whether to buy or sell. On the contrary, if the trading conditions are not met, wait until the next cycle for judgment

<!-- b000356 | prose | pages [21] -->
• Deal what. By setting the threshold of increase and decrease, compare the rise and fall range of gold and bitcoin, measure the risk and return of trading bitcoin and gold, and decide to trade gold or bitcoin.

<!-- b000357 | prose | pages [21] -->
• How much is the deal. If we decide to buy, we will use the decision coeﬃcient of the current model to decide how much to buy. When the judgment coeﬃcient is small, it means that the model we currently use is relatively stable and the risk is small. Therefore, when purchasing, we can appropriately increase the purchase proportion, on the contrary, reduce the purchase proportion; If we decide to sell, we will sell according to the preset proportion.

<!-- b000358 | prose | pages [21] -->
For the above strategies, by changing the variable parameters in the strategy, three strategies can be formed: insurance type, common type and radical type, which are suitable for diﬀerent traders and have good generalization ability. Secondly, when the variable parameters in the strategy are disturbed, the results show that the total assets change within a certain range, indicating that the anti-interference ability of the model is strong. Finally, by comparing the beneﬁts of $1000 deposited in the bank for ﬁve years and the ﬁve-year trading of this strategy, it can be seen that our strategy can resist inﬂation to a certain extent.

<!-- b000359 | heading | pages [21] -->
MODEL

<!-- b000360 | prose | pages [21] -->
The strategy is based on the prediction of the future. In view of the simplicity and eﬃciency of ARIMA model, which only needs endogenous variables rather than other exogenous variables, we choose ARIMA model as the price prediction model. In order to predict the future market timely and accurately, we use the data of 30 consecutive days as the training set and the data of the next 3 days as the test set. The correlation coeﬃcient R2 between gold’s prediction result and the real value is 0.8591, and bitcoin’s R2 is 0.9304, which are close to 1, indicating that the correlation between the predicted value and the real value is strong and the prediction accuracy is high. Such prediction lays a solid foundation for follow-up work.

<!-- b000361 | furniture | pages [22] -->
Team # 2203120

<!-- b000362 | furniture | pages [22] -->
Page 21 of 23

<!-- b000363 | prose | pages [22] -->
The determination of trading strategy is essentially a dynamic programming problem. We need to maximize the return while taking into account the risk. Therefore, establish the objective function:

<!-- b000364 | prose | pages [22] -->
wj,mj Aj −λ × Sj max

<!-- b000365 | prose | pages [22] -->
where, Wj represents the roportion of gold and bitcoin bought on day j, mj represents the roportion of gold and bitcoin sought on day j, Aj represents the total assets on day j, λ represents the coeﬃcient of regular term, which is used to control risk and return, Si represents the current day risk.

<!-- b000366 | prose | pages [22] -->
By changing the coeﬃcient of the regular term λ, the risk can be adjusted and divided into three investment strategies: steady investment, common investment and radical investment.

<!-- b000367 | heading | pages [22] -->
RESULTS

<!-- b000368 | prose | pages [22] -->
Through the training of parameters, we have obtained models for three diﬀerent populations. The best returns and some transaction information of the three models are shown in the table below:

<!-- b000369 | caption | pages [22] -->
Table 8: Results of three types of strategies

<!-- b000370 | prose | pages [22] -->
Insurance-type Common-type Radical-type

<!-- b000371 | prose | pages [22] -->
Total assets 14312.68 50040.55 132089.11 [C, G, B] [11474.39, 1.59, 1.07] [421.14, 0.61, 1.05] [22.31, 0.16, 2.84] Number of transactions 85 58 9 SD 3861.73 15501.99 40067.35

<!-- b000372 | prose | pages [22] -->
Through the analysis of the results, we can see that:

<!-- b000373 | prose | pages [22] -->
• The amount of investment is mainly bitcoin.

<!-- b000374 | prose | pages [22] -->
• Insurance investment tends to trade many times and is vulnerable to market inﬂuence. Ag- gressive investments make fewer transactions.

<!-- b000375 | furniture | pages [23] -->
Team # 2203120

<!-- b000376 | furniture | pages [23] -->
Page 22 of 23

<!-- b000377 | heading | pages [23] -->
References

<!-- b000378 | references | pages [23] -->
[1] Conlon. T and McGee. R. Safe haven or risky hazard? Bitcoin during the Covid-19 bear

<!-- b000379 | references | pages [23] -->
market. FINANCE RESEARCH LETTERS, 35, 2020.

<!-- b000380 | references | pages [23] -->
[2] Khashei. M and Bĳari. M. A novel hybridization of artiﬁcial neural networks and ARIMA

<!-- b000381 | references | pages [23] -->
models for time series forecasting. APPLIED SOFT COMPUTING, 11(2):2664-2675, 2011.

<!-- b000382 | references | pages [23] -->
[3] Aasim, Singh. SN and Mohapatra. A. Repeated wavelet transform based ARIMA model for

<!-- b000383 | references | pages [23] -->
very short-term wind speed forecasting. RENEWABLE ENERGY, 136:758-768, 2019.

<!-- b000384 | references | pages [23] -->
[4] Valipour. M, Banihabib. ME and Behbahani. SMR. Comparison of the ARMA, ARIMA, and

<!-- b000385 | references | pages [23] -->
the autoregressive artiﬁcial neural network models in forecasting the monthly inﬂow of Dez

<!-- b000386 | references | pages [23] -->
dam reservoir. JOURNAL OF HYDROLOGY, 476:433-441, 2013.

<!-- b000387 | references | pages [23] -->
[5] Mahjoub. C, Bellanger. JJ, Kachouri. A and Jeannes. RL. On the performance of temporal

<!-- b000388 | references | pages [23] -->
Granger causality measurements on time series: a comparative study. SIGNAL IMAGE AND

<!-- b000389 | references | pages [23] -->
VIDEO PROCESSING, 14(5):955-963, 2020.

<!-- b000390 | references | pages [23] -->
[6] Chen. JS, Hou. JL, Wu. SM and Chang-Chien. YW. Constructing investment strategy

<!-- b000391 | references | pages [23] -->
portfolios by combination genetic algorithms. EXPERT SYSTEMS WITH APPLICATIONS,

<!-- b000392 | references | pages [23] -->
36(2):3824-3828, 2009.

<!-- b000393 | references | pages [23] -->
[7] Wang. S, Wang. XG, Meng. FL, Yang. RJ, Zhao. YJ. Investor behaviour monitoring based on

<!-- b000394 | references | pages [23] -->
deep learning. BEHAVIOUR & INFORMATION TECHNOLOGY, 40 (9):XLII-LIII, 2021.

<!-- b000395 | references | pages [23] -->
[8] Michael. SC. Can information technology enable proﬁtable diversiﬁcation?

<!-- b000396 | references | pages [23] -->
An empiri-

<!-- b000397 | references | pages [23] -->
cal examination. JOURNAL OF ENGINEERING AND TECHNOLOGY MANAGEMENT,

<!-- b000398 | references | pages [23] -->
24(3):167-185, 2007.

<!-- b000399 | references | pages [23] -->
[9] Mitic. P. Is a Reputation Time Series White Noise? INTELLIGENT DATA ENGINEERING

<!-- b000400 | references | pages [23] -->
AND AUTOMATED LEARNING - IDEAL 2017, 10585:543-550, 2017.

<!-- b000401 | references | pages [23] -->
[10] Daigle. CL and Ridge. EE, Investing in stockpeople is an investment in animal welfare and

<!-- b000402 | references | pages [23] -->
agricultural sustainability. ANIMAL FRONTIERS, 8(3):53-59, 2018.

<!-- b000403 | references | pages [23] -->
[11] Mariana. CD, Ekaputra. IA and Husodo. ZA. Are Bitcoin and Ethereum safe-havens for stocks

<!-- b000404 | references | pages [23] -->
during the COVID-19 pandemic? FINANCE RESEARCH LETTERS, 38, 2021.

<!-- b000405 | references | pages [23] -->
[12] Conlon. T, Corbet. S and Mcgee. RJ. Are cryptocurrencies a safe haven for equity markets? An

<!-- b000406 | references | pages [23] -->
international perspective from the COVID-19 pandemic. RESEARCH IN INTERNATIONAL

<!-- b000407 | references | pages [23] -->
BUSINESS AND FINANCE, 54, 2020.

<!-- b000408 | furniture | pages [24] -->
Team # 2203120

<!-- b000409 | furniture | pages [24] -->
Page 23 of 23

<!-- b000410 | heading | pages [24] -->
Appendices

<!-- b000411 | heading | pages [24] -->
Appendix A

<!-- b000412 | prose | pages [24] -->
Changes of Various Types of Traders’ Assetes

<!-- b000413 | prose | pages [24] -->
(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin

<!-- b000414 | caption | pages [24] -->
Figure 17: Changes of various assets of common-type traders

<!-- b000415 | prose | pages [24] -->
(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin

<!-- b000416 | caption | pages [24] -->
Figure 18: Changes of various assets of radical-type traders
