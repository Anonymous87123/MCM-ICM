# P-C-2022-2203120-59ecfcb7

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2022

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | title | pages [1] -->
2203120

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Trading Strategy Model Based on Dynamic

<!-- b000009 | title | pages [1] -->
Programming

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
It is of great signiﬁcance for traders to buy and sell volatile assets reasonably in market transactions. Traders choose diﬀerent trading strategies and get diﬀerent beneﬁts. This paper studies the best trading strategies for diﬀerent traders based on the daily prices of gold and bitcoin in the past.

<!-- b000012 | prose | pages [1] -->
For problem 1, the original data is preprocessed ﬁrstly, including ﬁlling the missing value by the daily price of gold in the past, and standardize all the original data. Following the processed data, the ARIMA model is used to establish the price prediction model. Correlation coeﬃceents between the prediction results and the price of gold and bitcoin are 0.8592 and 0.9304 respectively. The eﬀectiveness of our model is denoted. Thirdly, a dynamic programming model with largest total assets and risk as the regular termis is established, with the constraints hit rate and transaction volume limit.

<!-- b000013 | prose | pages [1] -->
Lastly, the optimal daily trading strategy is solved with dynamic programming method. Final proﬁt is $ 132089.1078 on September 10, 2021.

<!-- b000014 | prose | pages [1] -->
For problem 2, we prove our strategy is the best judged from the generalization ability, robustness and beneﬁt of the model.

<!-- b000015 | prose | pages [1] -->
By adjusting the variable parameters in the model, the strategies suitable for three traders are formed, which are insurance type, common type and radical type. The solution method of problem 1 is used to obtain the changes of each asset and the total earnings of the three trading strategies. Furthermore, the variable parameters in the model are disturbed, and the total assets change within a certain range, indicating that the model has strong anti-interference ability. Finally, the assets obtained by the three types of trading strategies are $14312.6827, $50040.5474 and $132089.1078 respectively. It can be seen that our model yield can resist inﬂation greatly.

<!-- b000016 | prose | pages [1] -->
For problem 3, ﬁrstly, the sensitivity is deﬁned as the change rate of transaction frequency. By changing the transaction cost of gold and bitcoin, it is calculated that the sensitivity of gold transaction cost is 0.0422 and that of bitcoin transaction cost is 0.0658.

<!-- b000017 | prose | pages [1] -->
It can be seen from the comparison that the transaction strategy is more sensitive to the transaction cost of bitcoin. Secondly, the impact of transaction cost on transaction frequency, asset return and asset risk are analyzed. We ﬁnd that when the transaction cost increases, the transaction frequency, asset return and asset risk are decreases correspondingly.

<!-- b000018 | prose | pages [1] -->
For problem 4, we summarize the models and strategies established in the ﬁrst three questions, and introduce to traders in the form of memorandum how to simply use the trading strategy to trade and the beneﬁts brought by diﬀerent trading strategies.

<!-- b000019 | keywords | pages [1] -->
Keywords: quantitative investment; ARIMA model; dynamic programming

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | heading | pages [2] -->
Introduction

<!-- b000023 | prose | pages [2] -->
2 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2

<!-- b000024 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000025 | prose | pages [2] -->
2

<!-- b000026 | heading | pages [2] -->
General Assumptions and Notations

<!-- b000027 | prose | pages [2] -->
2

<!-- b000028 | prose | pages [2] -->
4

<!-- b000029 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000030 | heading | pages [2] -->
Assumptions

<!-- b000031 | prose | pages [2] -->
4

<!-- b000032 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000033 | heading | pages [2] -->
Notations

<!-- b000034 | prose | pages [2] -->
4

<!-- b000035 | prose | pages [2] -->
Problem 1: Prediction and Strategy in the Investment 3 4

<!-- b000036 | prose | pages [2] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5

<!-- b000037 | prose | pages [2] -->
Model Establishment of Problem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 5 Price Prediction Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2 Trading Strategy Model 8

<!-- b000038 | prose | pages [2] -->
Model Solving: Finding Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 10

<!-- b000039 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 Results and Model Evaluation 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4.1 Model Results 11 Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4.2 12

<!-- b000040 | prose | pages [2] -->
Problem 2: Prove Optimization of the Strategy 4

<!-- b000041 | prose | pages [2] -->
4.1 Generalization Ability of the Model

<!-- b000042 | prose | pages [2] -->
12

<!-- b000043 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | prose | pages [2] -->
13

<!-- b000045 | prose | pages [2] -->
Robustness of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Yield of the Strategy 16

<!-- b000046 | heading | pages [2] -->
Problem 3: Sensitivity of Strategy to Transaction Cost

<!-- b000047 | prose | pages [2] -->
5 16

<!-- b000048 | prose | pages [2] -->
Sensitivity Diﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 17

<!-- b000049 | prose | pages [2] -->
Impact of Transaction Costs on Strategy . . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000050 | prose | pages [2] -->
6

<!-- b000051 | heading | pages [2] -->
Conclusion

<!-- b000052 | prose | pages [2] -->
17

<!-- b000053 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Strengths 18

<!-- b000054 | prose | pages [2] -->
Possible Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000055 | prose | pages [2] -->
7

<!-- b000056 | heading | pages [2] -->
Memorandum

<!-- b000057 | heading | pages [2] -->
Appendices

<!-- b000058 | prose | pages [2] -->
19

<!-- b000059 | prose | pages [2] -->
19

<!-- b000060 | prose | pages [2] -->
23

<!-- b000061 | heading | pages [2] -->
Appendix A Changes of Various Types of Traders’ Assetes

<!-- b000062 | prose | pages [2] -->
23

<!-- b000063 | furniture | pages [3] -->
Team # 2203120

<!-- b000064 | furniture | pages [3] -->
Page 2 of 23

<!-- b000065 | prose | pages [3] -->
1

<!-- b000066 | heading | pages [3] -->
Introduction

<!-- b000067 | prose | pages [3] -->
1.1 Problem Background

<!-- b000068 | prose | pages [3] -->
Market traders buy and sell volatile assets frequently, with a goal to maximize their total return. There is usually a commission for each purchase and sale. Two such assets are gold and bitcoin.The price changes of bitcoin and gold from September 11, 2016 to September 10, 2021 are shown in

<!-- b000069 | caption | pages [3] -->
Figure 1. The source of gold daily prices is London Bullion Market Association and the source of

<!-- b000070 | prose | pages [3] -->
bitcoin daily prices is NASDAQ.

<!-- b000071 | prose | pages [3] -->
(a) Gold daily prices, U.S. dollars per troy ounce (b) Bitcoin daily prices, U.S. dollars per bitcoin

<!-- b000072 | caption | pages [3] -->
Figure 1: The prices of two assets

<!-- b000073 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000074 | prose | pages [3] -->
In this problem, we are asked by a trader to develop a model that uses only the past stream of daily prices to date to determine each day if the trader should buy, hold, or sell their assets in their portfolio. We will start with $1000 on September 11, 2016 and use the ﬁve-year trading period, from September 11, 2016 to September 10, 2021. On each trading day, the trader will have a portfolio consisting of cash, gold, and bitcoin [C, G, B] in U.S. dollars, troy ounces, and bitcoins, respectively.We should only use these data to solve the following problems:

<!-- b000075 | prose | pages [3] -->
• Develop a model that gives the best daily trading strategy based only on price data up to that day. Use the model and strategy to predict the value of the initial $1000 investment on September 10, 2021.

<!-- b000076 | prose | pages [3] -->
• Present evidence that the model provides the best strategy.

<!-- b000077 | prose | pages [3] -->
• Determine how sensitive the strategy is to transaction costs and how transaction costs aﬀect the strategy and results.

<!-- b000078 | prose | pages [3] -->
• Communicate the strategy, model, and results to the trader in a memorandum of at most two pages.

<!-- b000079 | prose | pages [3] -->
1.3 Problem Analysis

<!-- b000080 | prose | pages [3] -->
For problem 1, The premise of formulating the strategy is to accurately predict the price trend of gold and bitcoin in the future. Therefore, it is necessary to establish a price prediction model to lay the foundation for formulating the strategy. Common time series prediction models include LSTM,

<!-- b000081 | furniture | pages [4] -->
Team # 2203120

<!-- b000082 | furniture | pages [4] -->
Page 3 of 23

<!-- b000083 | prose | pages [4] -->
BP neural network, RNN, encoder-decoder model, etc. In view of the simplicity and eﬃciency of ARIMA model, which only needs endogenous variables rather than other exogenous variables, we choose to use ARIMA model.

<!-- b000084 | prose | pages [4] -->
Next, establish a trading strategy model according to the established indicators, give the trading strategy and calculate the ﬁnal income. Intuitively, the price ﬂuctuation of bitcoin is much greater than that of gold, so we guess the risk is greater than that of gold. Therefore, the risk of investment can be described by the variance of price change. This is essentially a dynamic programming problem. We can quantify the return and risk, take the maximum beneﬁt as the objective function, ﬁnd the constraints and establish the model.

<!-- b000085 | prose | pages [4] -->
With regard to problem 2, The optimization of the model can be proved from three aspects: generalization ability, robustness and proﬁt. The generalization ability of the model is reﬂected in that changing the parameters in the model can make the model formulate diﬀerent kinds of strategies. Therefore, we divide the strategies into insurance type, common type and radical type. The robustness of the model means that small changes in parameters will not aﬀect the overall strategy, and the anti-interference of the model is strong. It also shows that compared with other investments, our strategy has a better rate of return.

<!-- b000086 | prose | pages [4] -->
As for problem 3, It is known that the transaction cost is the Commission. Intuitively, the increase of commission should appropriately reduce the transactions. The decrease of commission can increase the number of transactions. The ultimate goal is to maximize the income. Based on the transaction strategy model established by the ﬁrst question, by changing the cost α in the model and observing the corresponding changes of transaction frequency, asset return and asset risk, we can get the sensitivity of three types of strategies to transaction cost.

<!-- b000087 | caption | pages [4] -->
Figure 2: Overall structure

<!-- b000088 | furniture | pages [5] -->
Team # 2203120

<!-- b000089 | furniture | pages [5] -->
Page 4 of 23

<!-- b000090 | prose | pages [5] -->
2

<!-- b000091 | heading | pages [5] -->
General Assumptions and Notations

<!-- b000092 | prose | pages [5] -->
2.1

<!-- b000093 | heading | pages [5] -->
Assumptions

<!-- b000094 | prose | pages [5] -->
To simplify our problems, we make the following basic assumptions, each of which is adequately justiﬁed.

<!-- b000095 | prose | pages [5] -->
• All data are authentic.

<!-- b000096 | prose | pages [5] -->
• The investor is physically and mentally healthy and has no burden such as huge loans.

<!-- b000097 | prose | pages [5] -->
• Without considering inﬂation and other economic changes in recent years, only tabular data are used.

<!-- b000098 | prose | pages [5] -->
• All transactions are conducted in US dollars. The commission is deducted from the amount paid instead of being given separately.

<!-- b000099 | prose | pages [5] -->
• Since it is only US $1000, the minimum transaction unit of US dollar and bitcoin under normal circumstances is not considered for the universality of the model.

<!-- b000100 | prose | pages [5] -->
2.2

<!-- b000101 | heading | pages [5] -->
Notations

<!-- b000102 | prose | pages [5] -->
In this work, we use the nomenclature in Table 1 in the model construction. Other none- frequent-used symbols will be introduced once they are used.

<!-- b000103 | caption | pages [5] -->
Table 1: Notations

<!-- b000104 | prose | pages [5] -->
Symbols Descripition

<!-- b000105 | prose | pages [5] -->
t1 = 3, t2 = 3 gold trading cycle (including holidays), bitcoin trading cycle n number of cycles in ﬁve years DSgi, DSbi hit rate of training prediction model, i=2,3...n Ri = [Ci Gi Bi] asset distribution in the i-th cycle, R0 = [1000 0 0] Ai total assets in the i-th cycle, A0=1000 qi proportion of cash in total assets in the i-th cycle ei, fi threshold of increase or decrease in the i-th cycle Xg(i), Xb(i) forecast average price in the i-th cycle Yg(i), Yb(i) real average price of gold in the i-th cycle αg, αb proportion of commission of each transaction in the transaction amount R2

<!-- b000106 | prose | pages [5] -->
gi, R2

<!-- b000107 | prose | pages [5] -->
decision coeﬃcient of the trained model in the i-th cycle bi

<!-- b000108 | prose | pages [5] -->
3 Problem 1: Prediction and Strategy in the Investment

<!-- b000109 | prose | pages [5] -->
In this section, based on the existing data, we use ARIMA model to predict the price trend of gold and bitcoin in the future, so as to establish a model and give the best daily trading strategy. Dynamic programming is used to estimate the value of the initial $1000 investment by September 10, 2021.

<!-- b000110 | furniture | pages [6] -->
Team # 2203120

<!-- b000111 | furniture | pages [6] -->
Page 5 of 23

<!-- b000112 | prose | pages [6] -->
3.1 Data Preprocessing

<!-- b000113 | prose | pages [6] -->
Before data analysis, the availability of data must be guaranteed.

<!-- b000114 | prose | pages [6] -->
• Missing value processing. Unlike bitcoin, which is traded daily, gold is traded only on trading days, so the data is not continuous. For the convenience of subsequent modeling, the missing value is ﬁlled with the mean value before and after the day.

<!-- b000115 | prose | pages [6] -->
• Data standardization. In regression prediction, standardization gives eigenvalues equal weight. Since we predict by period, we process the data by period. Calculate the mean(¯x) and standard deviation(SD) of data(x), then the processed data x′ = (x−¯x)

<!-- b000116 | prose | pages [6] -->
SD .

<!-- b000117 | prose | pages [6] -->
3.2

<!-- b000118 | heading | pages [6] -->
Model Establishment of Problem 1

<!-- b000119 | prose | pages [6] -->
3.2.1

<!-- b000120 | heading | pages [6] -->
Price Prediction Model

<!-- b000121 | prose | pages [6] -->
Improving forecasting especially time series forecasting accuracy is an important yet often diﬃcult task facing decision makers in many areas. Autoregressive integrated moving average (ARIMA) models are one of the most popular linear models in time series forecasting, which have been widely applied in order to construct more accurate hybrid models during the past decade [2].

<!-- b000122 | prose | pages [6] -->
ARIMA model combines three basic methods:

<!-- b000123 | prose | pages [6] -->
• Autoregressive(AR). Describe the relationship between the current value and the historical value, and use the historical time data of the variable to predict itself. The order of AR model is recorded as p value.The formula is as follows:

<!-- b000124 | prose | pages [6] -->
yt = α0 + α1yt−1 + α2yt−2 + · · · + αpyt−p + ϵt (1)

<!-- b000125 | prose | pages [6] -->
where, and α is the coeﬃcient, ϵt stands for error.

<!-- b000126 | prose | pages [6] -->
• Integrated(I). When the time series becomes stationary, the diﬀerence needs to be made, and the order of the diﬀerence is recorded as d value. Generally, ﬁrst order is enough.

<!-- b000127 | prose | pages [6] -->
• Moving average(MA). Moving average model focuses on the accumulation of error terms in autoregressive model. The order of MA model is recorded as q value.The formula is as follows:

<!-- b000128 | prose | pages [6] -->
yt = c + ϵt + θ1ϵt−1 + θ2ϵt−2 + · · · + θqϵt−q (2)

<!-- b000129 | prose | pages [6] -->
where, c represents the constant term, ϵt is the white noise process of variance, and θ is the coeﬃcient.

<!-- b000130 | prose | pages [6] -->
The model is called ARIMA (p, d, q), as shown in the ﬁgure3, where p is the autoregressive term, q is the moving average term, and D is the number of diﬀerences. We will follow the steps listed below to build and solve our model.

<!-- b000131 | furniture | pages [7] -->
Team # 2203120

<!-- b000132 | furniture | pages [7] -->
Page 6 of 23

<!-- b000133 | caption | pages [7] -->
Figure 3: Structure of ARIMA model

<!-- b000134 | prose | pages [7] -->
step1 Stabilization

<!-- b000135 | prose | pages [7] -->
To use ARIMA model, the time series must be stationary. We use the Augmented Dickey- fuller unit root test to test the stationarity. If the P value obtained from ADF test is less than 0.05, it is a stable time series. If it is unstable, we convert the non-stationary process into a stationary process by diﬀerence method. It can be seen from the table 2 that the time series becomes stable after the ﬁrst-order diﬀerence.

<!-- b000136 | caption | pages [7] -->
Table 2: P value of gold and bitcoin time series before and after diﬀerence

<!-- b000137 | prose | pages [7] -->
P value before diﬀerence

<!-- b000138 | prose | pages [7] -->
gold 0.6734 bitcoin 0.9921

<!-- b000139 | prose | pages [7] -->
step2 Selection of p and q

<!-- b000140 | prose | pages [7] -->
P value after diﬀerence

<!-- b000141 | prose | pages [7] -->
0.0043 0.0000

<!-- b000142 | prose | pages [7] -->
Use autocorrelation function(ACF) and partial autocorrelation function(PACF) to determine the values of p and q. the conﬁrmation method is shown in the table 3.

<!-- b000143 | caption | pages [7] -->
Table 3: Conﬁrmation method of p value and q value

<!-- b000144 | prose | pages [7] -->
Model ACF

<!-- b000145 | prose | pages [7] -->
AR(P)

<!-- b000146 | prose | pages [7] -->
PACF

<!-- b000147 | prose | pages [7] -->
attenuation tends to 0 MA(q) truncation after p-order truncation after q-order ARMA(p, q) attenuation tends to 0 attenuation tends to 0 after q-order attenuation tends to 0 after p-order

<!-- b000148 | prose | pages [7] -->
NOTE: Truncation means falling within the conﬁdence interval (95% of the points comply with the rule)

<!-- b000149 | caption | pages [7] -->
Figure 4 (a) shows the truncation of gold data using level 2 ACF and level 1 PACF, and

<!-- b000150 | caption | pages [7] -->
Figure 4 (b) shows the truncation of bitcoin data using level 2 ACF and level 2 PACF. From

<!-- b000151 | prose | pages [7] -->
this, we can determine the p value and q value respectively.

<!-- b000152 | furniture | pages [8] -->
Team # 2203120

<!-- b000153 | furniture | pages [8] -->
Page 7 of 23

<!-- b000154 | prose | pages [8] -->
(a) ACF chart and PACF chart of gold (b) ACF chart and PACF chart of bitcoin

<!-- b000155 | caption | pages [8] -->
Figure 4: ACF chart and PACF chart

<!-- b000156 | prose | pages [8] -->
step3 White noise test

<!-- b000157 | prose | pages [8] -->
If the white noise is obtained, it means that the useful information in the time series has been extracted, and the rest are all random disturbances, which cannot be predicted and used.[9] If the residual sequence passes the white noise test, the modeling can be terminated, because there is no information to continue to extract.

<!-- b000158 | prose | pages [8] -->
The ARIMA model of gold is ARIMA(2,1,1) and bitcoin is ARIMA(2,1,2). The p value of the white noise test output of this model is very close to 0, indicating that it follows the normal distribution with the mean value of 0, that is, it is a white noise.

<!-- b000159 | prose | pages [8] -->
step4 Prediction

<!-- b000160 | prose | pages [8] -->
In order to predict the future market timely and accurately, we use the data of 30 consecutive days as the training set and the data of the next 3 days as the test set. The moving step of the training set is 3. The prediction results of one cycle are shown in the ﬁgure 5. The correlation coeﬃcient R2 of gold is 0.8592 and that of bitcoin is 0.9304. The prediction results of the model are relatively successful and can be used.

<!-- b000161 | prose | pages [8] -->
(a) Forecast chart of gold in one cycle (b) Forecast chart of bitcoin in one cycle

<!-- b000162 | caption | pages [8] -->
Figure 5: Forecast charts in one cycle

<!-- b000163 | furniture | pages [9] -->
Team # 2203120

<!-- b000164 | prose | pages [9] -->
3.2.2

<!-- b000165 | heading | pages [9] -->
Trading Strategy Model

<!-- b000166 | furniture | pages [9] -->
Page 8 of 23

<!-- b000167 | prose | pages [9] -->
The best daily trading strategy is given only according to the price data. We need to judge the forecast data and give the strategy according to the forecast. Therefore, we deﬁne variable parameters as shown in the table 4 to quantify the strategy.

<!-- b000168 | caption | pages [9] -->
Table 4: Variable parameters

<!-- b000169 | prose | pages [9] -->
Symbols

<!-- b000170 | prose | pages [9] -->
β, γ

<!-- b000171 | prose | pages [9] -->
Descripition

<!-- b000172 | prose | pages [9] -->
proportion of increase or decrease DS hit rate wH, wL purchase proportion, H/L stands for a higher/lower proportion m selling proportion threshold of Decision coeﬃcient R2 R2

<!-- b000173 | prose | pages [9] -->
q cash retention ratio i

<!-- b000174 | prose | pages [9] -->
Decision coeﬃcient(R2): it is used to evaluate the volatility predicted by the model. The closer the index value is to 1, the higher the ﬁtting performance of the model.

<!-- b000175 | prose | pages [9] -->
Pt

<!-- b000176 | prose | pages [9] -->
j=1

<!-- b000177 | prose | pages [9] -->
R2

<!-- b000178 | prose | pages [9] -->
i =

<!-- b000179 | prose | pages [9] -->
Pt

<!-- b000180 | prose | pages [9] -->
j=1

<!-- b000181 | prose | pages [9] -->
2

<!-- b000182 | prose | pages [9] -->
   

<!-- b000183 | prose | pages [9] -->
xi,j −Y(i)

<!-- b000184 | prose | pages [9] -->
(3)

<!-- b000185 | prose | pages [9] -->
   

<!-- b000186 | prose | pages [9] -->
2

<!-- b000187 | prose | pages [9] -->
yi,j −Y(i)

<!-- b000188 | prose | pages [9] -->
where xi,j represents the predicted value of day j in cycle i and yi,j represents the actual value of day j in cycle iand Y(i) represents the mean of the true value in cycle i.

<!-- b000189 | prose | pages [9] -->
Hit rate(DS): it is used to evaluate the accuracy of the model in predicting the rise and fall, so as to evaluate the prediction of the long-term trend of the model.

<!-- b000190 | prose | pages [9] -->
(

<!-- b000191 | prose | pages [9] -->
Xt

<!-- b000192 | prose | pages [9] -->
, (xi,j+1 −xi,j) (yi,j+1 −yi,j) ⩾0 1

<!-- b000193 | prose | pages [9] -->
DSi = 1

<!-- b000194 | prose | pages [9] -->
j=1 dj × 100% ; dj =

<!-- b000195 | prose | pages [9] -->
t

<!-- b000196 | prose | pages [9] -->
j = 1, 2, 3 (4) , else 0

<!-- b000197 | prose | pages [9] -->
where di represents the predicted rise and fall in cycle i. If the rise and fall of the real value is the same as that of the predicted value, it is 1, on the contrary, it is 0.

<!-- b000198 | prose | pages [9] -->
In addition, we make the following assumptions:

<!-- b000199 | prose | pages [9] -->
• The period from September 11, 2016 to November 11, 2016 is the zero cycle, and no transaction is conducted as the experience accumulation period. Since November 12, 2016 is the ﬁrst cycle, the number of cycles is n = 588.

<!-- b000200 | prose | pages [9] -->
• If the transaction starts from the second cycle, the asset situation in the ﬁrst week is the same as that in the zero cycle.

<!-- b000201 | prose | pages [9] -->
• Since gold is not traded during holidays, when the predicted value of gold price in a certain period is empty, it means that gold is not traded in that period.

<!-- b000202 | furniture | pages [10] -->
Team # 2203120

<!-- b000203 | furniture | pages [10] -->
Page 9 of 23

<!-- b000204 | prose | pages [10] -->
• The Commission is deducted from the amount paid instead of being given separately.

<!-- b000205 | prose | pages [10] -->
We use i to record the cycle, in which cycle 0 is the experience accumulation period, which only predicts and does not trade. 3 days is a cycle. We use j to record the day. The total number of cycles is 588. Pay attention to the diﬀerence between trading days of gold and bitcoin.

<!-- b000206 | prose | pages [10] -->
To build a strategy model, we need to ﬁnd the objective function and constraints. To make more proﬁts, we need to make the risk as small as possible and the proﬁt as much as possible. Firstly, we quantify the risk and set the standard deviation of assets owned in the transaction process as the risk index S:

<!-- b000207 | prose | pages [10] -->
v u u

<!-- b000208 | prose | pages [10] -->
Pi−1

<!-- b000209 | prose | pages [10] -->
u t

<!-- b000210 | prose | pages [10] -->
j=i−30

<!-- b000211 | prose | pages [10] -->
Sj =

<!-- b000212 | prose | pages [10] -->
Calculate the amount of cash:

<!-- b000213 | prose | pages [10] -->
(

<!-- b000214 | prose | pages [10] -->
Ci−1 −Gi × wg

<!-- b000215 | prose | pages [10] -->
Ci =

<!-- b000216 | prose | pages [10] -->
 

<!-- b000217 | prose | pages [10] -->
2

<!-- b000218 | prose | pages [10] -->
∑i−1

<!-- b000219 | prose | pages [10] -->
j=i−30 Ai

<!-- b000220 | prose | pages [10] -->
Ai −

<!-- b000221 | prose | pages [10] -->
30

<!-- b000222 | prose | pages [10] -->
(5) 30

<!-- b000223 | prose | pages [10] -->
, Xg(i) −Yg(i−1) > βg × Ai−1

<!-- b000224 | prose | pages [10] -->
(6)

<!-- b000225 | prose | pages [10] -->
Ci−1 + Gi × mg × (1 −αg) × Yg(i+1)

<!-- b000226 | prose | pages [10] -->
(

<!-- b000227 | prose | pages [10] -->
Ci−1 −Bi × wb

<!-- b000228 | prose | pages [10] -->
Ci =

<!-- b000229 | prose | pages [10] -->
, Yg(i−1) −Xg(i) > γg × Ai−1

<!-- b000230 | prose | pages [10] -->
, Xb(i) −Yb(i−1) > βb × Ai−1 Ci−1 + Bi × mb × (1 −αb) × Yb(i+1)

<!-- b000231 | prose | pages [10] -->
Calculate the amount of gold and bitcoin:

<!-- b000232 | prose | pages [10] -->
(

<!-- b000233 | prose | pages [10] -->
, Yb(i−1) −Xb(i−1) > γb × Ai−1

<!-- b000234 | prose | pages [10] -->
Gi−1 + Ci × wg × (1 −αg)

<!-- b000235 | prose | pages [10] -->
Gi =

<!-- b000236 | prose | pages [10] -->
(7)

<!-- b000237 | prose | pages [10] -->
Gi−1 −Gi−1 × mg

<!-- b000238 | prose | pages [10] -->
(

<!-- b000239 | prose | pages [10] -->
Gi−1 + Bi × wb × (1 −αb)

<!-- b000240 | prose | pages [10] -->
Bi =

<!-- b000241 | prose | pages [10] -->
Gi−1 −Gi−1 × mb

<!-- b000242 | prose | pages [10] -->
Then the total asset formula is:

<!-- b000243 | prose | pages [10] -->
Ai = Ci + Gi × Yg(i) + Bi × Yb(i) (8)

<!-- b000244 | prose | pages [10] -->
Finally, the objective function and constraints are determined, and the trading strategy model is obtained:

<!-- b000245 | prose | pages [10] -->
wj,mj Aj −λ × Sj max

<!-- b000246 | prose | pages [10] -->
 

<!-- b000247 | prose | pages [10] -->
Cj, Gj, Bj, Aj ⩾0

<!-- b000248 | prose | pages [10] -->
    

<!-- b000249 | prose | pages [10] -->
DSj ⩾0.5

<!-- b000250 | prose | pages [10] -->


<!-- b000251 | prose | pages [10] -->
s.t.

<!-- b000252 | prose | pages [10] -->
Cj ⩾Aj × q

<!-- b000253 | prose | pages [10] -->
  

<!-- b000254 | prose | pages [10] -->
αg = 1%, αb = 2%

<!-- b000255 | prose | pages [10] -->
   

<!-- b000256 | prose | pages [10] -->
(9)

<!-- b000257 | prose | pages [10] -->
A0 = 1000, C0 = C1 = 1000, G0 = G1 = B0 = B1 = 0

<!-- b000258 | furniture | pages [11] -->
Team # 2203120

<!-- b000259 | furniture | pages [11] -->
Page 10 of 23

<!-- b000260 | prose | pages [11] -->
where, Wj represents the roportion of gold and bitcoin bought on day j, mj represents the roportion of gold and bitcoin sought on day j, Aj represents the total assets on day j, λ represents the coeﬃcient of regular term, which is used to control risk and return, Sj represents the current day risk. The ﬁrst constraint indicates that all assets are positive, the second constraint indicates that the accuracy of the model is greater than 0.5, the third constraint indicates that the remaining capital of the transaction is greater than q times of the total assets, and α indicates the transaction cost, A0, C0, G0, B0 represents the total assets, cash, gold and bitcoin before the ﬁrst day of trading, C1, G1, B1 represents the amount of cash, gold and bitcoin before trading on day 2.

<!-- b000261 | heading | pages [11] -->
Model Solving: Finding Strategies

<!-- b000262 | prose | pages [11] -->
3.3

<!-- b000263 | prose | pages [11] -->
After the trading strategy model is established, we need to solve the model. The speciﬁc steps are as follows:

<!-- b000264 | prose | pages [11] -->
step1 Datainitialization. Set i = 1, knowαg = 1%, set parameterβg, γg, ds, R2, wHg, wLg, mg, q,

<!-- b000265 | prose | pages [11] -->
initial asset distributionR1 = R0 = [1000 0 0], total assets r1 = r0 = 1000.

<!-- b000266 | prose | pages [11] -->
step2 Calculate hit rate (DS). The prediction model hit rate(Formula 4) can evaluate the accuracy

<!-- b000267 | prose | pages [11] -->
of the trained model in predicting the rise and fall. When the accuracy is high enough, you can continue to follow the next steps.

<!-- b000268 | prose | pages [11] -->
step3 Determine whether to trade. Firstly, due to the cost in the transaction, in order to avoid

<!-- b000269 | prose | pages [11] -->
excessive cost caused by frequent transaction, the transaction is carried out only when the increase and decrease reach a certain threshold. Secondly, in order to avoid too little cash left in the transaction, the transaction can be carried out only when the cash meets the reserved amount. The speciﬁc process is shown in the ﬁgure 6.

<!-- b000270 | caption | pages [11] -->
Figure 6: The process of determining whether to trade

<!-- b000271 | prose | pages [11] -->
where,

<!-- b000272 | prose | pages [11] -->
eg(i+1) = βg × Ai (10)

<!-- b000273 | prose | pages [11] -->
fg(i+1) = γg × Ai

<!-- b000274 | prose | pages [11] -->
qi =

<!-- b000275 | prose | pages [11] -->
(11)

<!-- b000276 | prose | pages [11] -->
Ci

<!-- b000277 | prose | pages [11] -->
(12)

<!-- b000278 | prose | pages [11] -->
Ci + Gi × Yg(i) + Bi × Yb(i)

<!-- b000279 | prose | pages [11] -->
in the formula, βg, γg represents the proportion of increase or decrease.

<!-- b000280 | furniture | pages [12] -->
Team # 2203120

<!-- b000281 | furniture | pages [12] -->
Page 11 of 23

<!-- b000282 | heading | pages [12] -->
step4 Determine the number of transactions. Prediction model discrimination coeﬃcient R2

<!-- b000283 | prose | pages [12] -->
gi can evaluate the volatility predicted by the trained model. The smaller the variable, the more stable the model is, and the proportion of buying gold during trading can be increased. The speciﬁc process is shown in the ﬁgure 7.

<!-- b000284 | caption | pages [12] -->
Figure 7: The process of determining the number of transactions

<!-- b000285 | prose | pages [12] -->
Where, the formula for total assets is

<!-- b000286 | prose | pages [12] -->
Ai+1 = Ci+1 + Gi+1 × Yg(i+1) + Bi+1 × Yb(i+1) (13)

<!-- b000287 | prose | pages [12] -->
When proportions WHg, WLg and mg are used respectively, the formula for calculating asset distribution is

<!-- b000288 | prose | pages [12] -->


<!-- b000289 | prose | pages [12] -->
Ci+1 = Ci −Ci × wLg

<!-- b000290 | prose | pages [12] -->
 

<!-- b000291 | prose | pages [12] -->
Gi+1 = Gi + Ci×wLg×(1−αg)

<!-- b000292 | prose | pages [12] -->
RWHg =

<!-- b000293 | prose | pages [12] -->
 

<!-- b000294 | prose | pages [12] -->
(14)

<!-- b000295 | prose | pages [12] -->
Yg(i+1) Bi+1 = Bi

<!-- b000296 | prose | pages [12] -->


<!-- b000297 | prose | pages [12] -->
Ci+1 = Ci −Ci × wHg

<!-- b000298 | prose | pages [12] -->
 

<!-- b000299 | prose | pages [12] -->
Gi+1 = Gi + Ci×wHg×(1−αg)

<!-- b000300 | prose | pages [12] -->
RWLg =

<!-- b000301 | prose | pages [12] -->
 

<!-- b000302 | prose | pages [12] -->
(15)

<!-- b000303 | prose | pages [12] -->
Yg(i+1) Bi+1 = Bi

<!-- b000304 | prose | pages [12] -->


<!-- b000305 | prose | pages [12] -->
Ci+1 = Ci −Ci × wLg

<!-- b000306 | prose | pages [12] -->
 

<!-- b000307 | prose | pages [12] -->
Gi+1 = Gi + Ci×wLg×(1−αg)

<!-- b000308 | prose | pages [12] -->
Rmg =

<!-- b000309 | prose | pages [12] -->
 

<!-- b000310 | prose | pages [12] -->
(16)

<!-- b000311 | prose | pages [12] -->
Yg(i+1) Bi+1 = Bi

<!-- b000312 | prose | pages [12] -->
In the formula, Yg(i+1) represents the real average price of gold on (i+1) day.

<!-- b000313 | prose | pages [12] -->
3.4

<!-- b000314 | heading | pages [12] -->
Results and Model Evaluation

<!-- b000315 | prose | pages [12] -->
3.4.1

<!-- b000316 | heading | pages [12] -->
Model Results

<!-- b000317 | prose | pages [12] -->
Using Python Programming and our model, set variable parameters: βb = 0, βg = 0.5, γb = 0.3, γg = 0.3, wHg = 0.8, wHb = 0.4, q = 0.01, the initial investment value of $1000 will be $132089.11 by September 10, 2021. The number of transactions is 9, and the ﬁnal asset distribution

<!-- b000318 | furniture | pages [13] -->
Team # 2203120

<!-- b000319 | furniture | pages [13] -->
Page 12 of 23

<!-- b000320 | prose | pages [13] -->
[C,G,B]=[22.31, 0.16, 2.84]. The changes of assets during the ﬁve-year period are shown in the ﬁgure below.

<!-- b000321 | caption | pages [13] -->
Figure 8: The changes of total assets during the ﬁve-year period

<!-- b000322 | prose | pages [13] -->
3.4.2

<!-- b000323 | heading | pages [13] -->
Model Evaluation

<!-- b000324 | prose | pages [13] -->
This result is obtained using two models. Firstly, ARIMA model is used for prediction, and we get good results: The correlation coeﬃcient R2 of gold is 0.8592 and that of bitcoin is 0.9304. They are close to 1, indicating that the predicted value is highly correlated with the real value.

<!-- b000325 | prose | pages [13] -->
Through the trading strategy model, we get speciﬁc beneﬁts. The strategy model has high availability:

<!-- b000326 | prose | pages [13] -->
• The model is only based on the price changes of gold and bitcoin in recent ﬁve years, so the model has low requirements for data.

<!-- b000327 | prose | pages [13] -->
• Our model puts forward variable parameters such as β, γ, wH, wL, m, q to form a parameter list. By changing the parameters in the list, we can achieve diﬀerent income results. In the future, we can form an investment prediction software according to the model. We only need to understand the meaning of relevant parameters to realize asset management. Therefore, our model is relatively simple and easy to understand.

<!-- b000328 | prose | pages [13] -->
• The parameters in the model have a large variable range and are more ﬂexible.

<!-- b000329 | prose | pages [13] -->
These ensures the reliability of the results.

<!-- b000330 | prose | pages [13] -->
4 Problem 2: Prove Optimization of the Strategy

<!-- b000331 | prose | pages [13] -->
Our model proposes multiple variable parameters, which can achieve diﬀerent beneﬁts by changing parameters, so the model has good generalization ability. At the same time, the small change of parameters will not aﬀect the overall strategy, and the model is robust.

<!-- b000332 | prose | pages [13] -->
Compared with other investments, our strategy has a better rate of return. The following will explain the

<!-- b000333 | furniture | pages [14] -->
Team # 2203120

<!-- b000334 | furniture | pages [14] -->
Page 13 of 23

<!-- b000335 | prose | pages [14] -->
generalization ability, robustness and proﬁt margin of the model to prove the optimization of the strategy.

<!-- b000336 | heading | pages [14] -->
Generalization Ability of the Model

<!-- b000337 | prose | pages [14] -->
4.1

<!-- b000338 | prose | pages [14] -->
Successful investment comes from two factors: one is traders’ correct understanding of the market, and the other is trading rationality. According to the reference materials[7], we divide traders into the following three types:

<!-- b000339 | prose | pages [14] -->
• Insurance-type. The purpose of such traders’ investment behavior is mainly to obtain long- term capital income, that is, they hope to obtain investment income regularly, and also hope to obtain diﬀerential proﬁts through the change of capital price in a longer term. At the same time, before investing, traders should generally master suﬃcient information and make a rational analysis of the expected proﬁts and risks of the target assets.

<!-- b000340 | prose | pages [14] -->
• Common-type. The purpose of such traders is mainly to obtain large proﬁts in a short period of time and are willing to bear some risks. Its way mainly depends on the short-term price ﬂuctuation diﬀerence to obtain proﬁts. They take technical analysis as the main means and make speculative decisions based on historical price ﬂuctuation experience. Generally speaking, the probability of success of Common-type investors is not low, but the probability of failure is also high. Its behavior has strong subjective initiative, and the probability of success depends on its accuracy in predicting market ﬂuctuations.

<!-- b000341 | prose | pages [14] -->
• Radical-type. The characteristics of radical traders’ behavior are based on luck and oppor- tunity, trading in the market with luck and hoping to make huge proﬁts in the short term. Generally speaking, the risk is very high. Unless they need money urgently, have the psy- chology of gamblers or have the ability to take risks, most people will not use this investment method.

<!-- b000342 | prose | pages [14] -->
In the model, for three types of traders, the corresponding parameters are adjusted as shown in the

<!-- b000343 | caption | pages [14] -->
table 5:

<!-- b000344 | caption | pages [14] -->
Table 5: Adjustment of variable parameters

<!-- b000345 | prose | pages [14] -->
variable parameters Insurance-type

<!-- b000346 | prose | pages [14] -->
βb 0.35 βg 0.50 γg 0.10 γb 0.10 wHg 0.95 wHb 0.15 q 0.15

<!-- b000347 | prose | pages [14] -->
Common-type Radical-type

<!-- b000348 | prose | pages [14] -->
0.10 0 0.50 0.50 0.20 0.30 0.20 0.30 0.80 0.80 0.30 0.40 0.05 0.01

<!-- b000349 | prose | pages [14] -->
Solve the model according to diﬀerent parameters adjustments and get the changes of various

<!-- b000350 | furniture | pages [15] -->
Team # 2203120

<!-- b000351 | furniture | pages [15] -->
Page 14 of 23

<!-- b000352 | prose | pages [15] -->
types of traders’ assets. The ﬁgure 9 shows the changes of various assets of insurance-type traders in ﬁve years. See the Appendix A for the ﬁgures of the other two types.

<!-- b000353 | prose | pages [15] -->
(b) Changes of gold (a) Changes of cash (c) Changes of bitcoin

<!-- b000354 | caption | pages [15] -->
Figure 9: Changes of various assets of insurance-type traders

<!-- b000355 | prose | pages [15] -->
The changes of total assets of three types of traders are shown in the ﬁgure 10:

<!-- b000356 | prose | pages [15] -->
(b) Common-type (a) Insurance-type (c) Radical-type

<!-- b000357 | caption | pages [15] -->
Figure 10: Changes in total assets of three types of traderss

<!-- b000358 | caption | pages [15] -->
Table 6: Results of three types of strategies

<!-- b000359 | prose | pages [15] -->
Insurance-type

<!-- b000360 | prose | pages [15] -->
Total assets 14312.68 [C, G, B]

<!-- b000361 | prose | pages [15] -->
Common-type Radical-type

<!-- b000362 | prose | pages [15] -->
50040.55 132089.11 [11474.39, 1.59, 1.07] Number of transactions 85 SD 3861.73 R2

<!-- b000363 | prose | pages [15] -->
0.94 g R2

<!-- b000364 | prose | pages [15] -->
0.41 b

<!-- b000365 | prose | pages [15] -->
NOTE: R2

<!-- b000366 | prose | pages [15] -->
g/R2

<!-- b000367 | prose | pages [15] -->
[421.14, 0.61, 1.05] [22.31, 0.16, 2.84] 58 9 15501.99 40067.35

<!-- b000368 | prose | pages [15] -->
0.27 0.24

<!-- b000369 | prose | pages [15] -->
0.98 0.99

<!-- b000370 | prose | pages [15] -->
b represent correlation between gold/bitcoin purchase and actual ﬂuctuation, SD represent standard deviation of 5-year assets.

<!-- b000371 | prose | pages [15] -->
Reading the data in the table 8, although radical investors have more returns, the value of SD is very large, that is, assets change greatly, so they have to bear corresponding risks. It can be

<!-- b000372 | furniture | pages [16] -->
Team # 2203120

<!-- b000373 | furniture | pages [16] -->
Page 15 of 23

<!-- b000374 | prose | pages [16] -->
seen from the number of transactions that any disturbance in the market may disturb insurance investors. From R2, we can ﬁnd that the more traders tend to venture capital, the more they will buy bitcoin; Gold symbolizes stable and conservative investment. Thus, our model gives a variety of practical and feasible strategies.

<!-- b000375 | prose | pages [16] -->
4.2

<!-- b000376 | heading | pages [16] -->
Robustness of the Model

<!-- b000377 | prose | pages [16] -->
In practical problems, the perturbation of system characteristics or parameters is often inevitable. The good robustness of the model means that the model has strong anti-interference ability, which means that the system has the ability to maintain a certain performance under the disturbance of uncertainty. As shown in the ﬁgure 11, ﬁgure 12, ﬁgure 13, they show the changes of total assets when disturbing the WH, WL and M parameters of gold and bitcoin respectively.

<!-- b000378 | prose | pages [16] -->
(a) gold (b) bitcoin

<!-- b000379 | caption | pages [16] -->
Figure 11: The impact of wL on total assets

<!-- b000380 | prose | pages [16] -->
(a) gold (b) bitcoin

<!-- b000381 | caption | pages [16] -->
Figure 12: The impact of wH on total assets

<!-- b000382 | furniture | pages [17] -->
Team # 2203120

<!-- b000383 | furniture | pages [17] -->
Page 16 of 23

<!-- b000384 | prose | pages [17] -->
(a) gold (b) bitcoin

<!-- b000385 | caption | pages [17] -->
Figure 13: The impact of m on total assets

<!-- b000386 | prose | pages [17] -->
As can be seen from the ﬁgure above, if these variables are disturbed, the ﬁnal income of the model is stable within a certain range. In fact, if the other parameters β, γ, q are disturbed, the ﬁnal return and investment risk of the model are stable within a certain range. The model has good robustness, so it is proved that the strategy we give is the best.

<!-- b000387 | prose | pages [17] -->
4.3 Yield of the Strategy

<!-- b000388 | prose | pages [17] -->
In the real economic market, because the issue of paper money sometimes exceeds the actual amount needed in circulation, there is often inﬂationso we need to manage money.Under diﬀerent levels of inﬂation, the portfolio is diverse.In reality, money, stocks and bonds are generally used as investment representatives.The portfolio in this question only includes gold ,bitcoin and cash.

<!-- b000389 | prose | pages [17] -->
Set the bank deposit interest rate as r, inﬂation rate as I,deposit amount as a, Then the actual value of the deposit after ﬁve years is

<!-- b000390 | prose | pages [17] -->
A = a(1+r−I)5 (17)

<!-- b000391 | prose | pages [17] -->
Where A represents the actual value of the money after ﬁve years of deposit in the bank.

<!-- b000392 | prose | pages [17] -->
It can be seen from the data, from 2016 to 2021,the inﬂation rate was 7%, the bank deposit interest rate was 0.5%, so the actual value of $1000 after ﬁve years is $139.2436.In contrast, with our portfolio, our total assets are $14312.6827, $50040.5474 and $132089.1078 respectively when we choose insurance, common and radical investments. The results obtained by our model are several times higher than the more conservative ﬁnancial behavior, so our model has higher income and can resist inﬂation.

<!-- b000393 | prose | pages [17] -->
5

<!-- b000394 | heading | pages [17] -->
Problem 3: Sensitivity of Strategy to Transaction Cost

<!-- b000395 | prose | pages [17] -->
Based on the transaction strategy model established by the ﬁrst question, we can get the sensitivity of the strategy to the transaction cost by changing the cost α in the model and observing the corresponding changes of transaction frequency, asset return and asset risk.

<!-- b000396 | furniture | pages [18] -->
Team # 2203120

<!-- b000397 | prose | pages [18] -->
5.1

<!-- b000398 | heading | pages [18] -->
Sensitivity Diﬁnition

<!-- b000399 | furniture | pages [18] -->
Page 17 of 23

<!-- b000400 | prose | pages [18] -->
Set initial variable α by α0, the initial transaction frequency h is h0 . After changing K(k = 1, 2, ..., 10) times, the variable α by αk. The corresponding transaction frequency h is hk.Sensitivity is deﬁned as:

<!-- b000401 | prose | pages [18] -->
P10

<!-- b000402 | prose | pages [18] -->
|hk−hk−1|

<!-- b000403 | prose | pages [18] -->
k=1

<!-- b000404 | prose | pages [18] -->
hk−1 × 100%

<!-- b000405 | prose | pages [18] -->
(18) 10 10

<!-- b000406 | prose | pages [18] -->
This indicator reﬂects the change rate of transaction frequency.

<!-- b000407 | prose | pages [18] -->
Impact of Transaction Costs on Strategy 5.2

<!-- b000408 | prose | pages [18] -->
In question 2, we divide the strategy model into insurance type, common type and radical type. When exploring the impact of cost on strategy, we should also consider these three aspects. Let’s take the common type as an example to explore the impact of various changes of α on the strategy. We mainly explore through transaction frequency, asset return and asset risk, in which asset risk is characterized by the variance of return. Speciﬁcally, it is investigated through the changes of the following four costs.

<!-- b000409 | prose | pages [18] -->
a. αg fell 0.1% each time and αb remained unchanged.

<!-- b000410 | prose | pages [18] -->
b. αg remained unchanged and αb fell 0.2% each time.

<!-- b000411 | prose | pages [18] -->
c. αg rise 1% each time and αb remained unchanged.

<!-- b000412 | prose | pages [18] -->
d. αg remained unchanged and αb rise 2% each time.

<!-- b000413 | caption | pages [18] -->
Figure 14 shows the change of strategy in case a. It can be seen from the ﬁgure that a small

<!-- b000414 | prose | pages [18] -->
change in the cost of gold will not have an impact on traders’ decisions.

<!-- b000415 | prose | pages [18] -->
(b) Changes of return (a) Changes of transaction frequency (c) Changes of risk

<!-- b000416 | caption | pages [18] -->
Figure 14: Change of strategy in case a

<!-- b000417 | prose | pages [18] -->
The result of case c is shown in the ﬁgure 15. In this case, we increase the transaction cost of gold by 0.1% each time. After reading the picture, it is found that:

<!-- b000418 | prose | pages [18] -->
1. If the cost increases to a certain extent, it will reduce the number of transactions and the total income.

<!-- b000419 | furniture | pages [19] -->
Team # 2203120

<!-- b000420 | furniture | pages [19] -->
Page 18 of 23

<!-- b000421 | prose | pages [19] -->
2. The cost increases, the transactions become less, and the possible risks are reduced.

<!-- b000422 | prose | pages [19] -->
3. The changes of the three indicators are synchronous and consistent.

<!-- b000423 | prose | pages [19] -->
It can be seen that in the face of the continuous rise in the cost of gold, our model has not ignored, keenly felt this signal, and the change direction is in line with the reality. The strategy is relatively sensitive to transaction costs.

<!-- b000424 | prose | pages [19] -->
(b) Changes of return (a) Changes of transaction frequency (c) Changes of risk

<!-- b000425 | caption | pages [19] -->
Figure 15: Change of strategy in case c

<!-- b000426 | caption | pages [19] -->
Table 7 lists the sensitivity of the strategies of the three transaction types to the cost of gold and

<!-- b000427 | prose | pages [19] -->
bitcoin respectively.

<!-- b000428 | caption | pages [19] -->
Table 7: The sensitivity of three types of strategies to two costs

<!-- b000429 | prose | pages [19] -->
Insurance-type

<!-- b000430 | prose | pages [19] -->
αg 0.0267 αb 0.2308

<!-- b000431 | prose | pages [19] -->
Through the data in the table, we can ﬁnd that:

<!-- b000432 | prose | pages [19] -->
Common-type Radical-type

<!-- b000433 | prose | pages [19] -->
0.0422 0 0.0658 0.0123

<!-- b000434 | prose | pages [19] -->
• The sensitivity of trading strategy to the cost of bitcoin is higher than that to the cost of gold.

<!-- b000435 | prose | pages [19] -->
• The insurance-type strategy is more sensitive to the cost of bitcoin, and the common-type strategy is more sensitive to the cost of gold.

<!-- b000436 | prose | pages [19] -->
• The sensitivity of radical-tupe strategy to cost is generally low.

<!-- b000437 | prose | pages [19] -->
6

<!-- b000438 | heading | pages [19] -->
Conclusion

<!-- b000439 | prose | pages [19] -->
6.1

<!-- b000440 | heading | pages [19] -->
Strengths

<!-- b000441 | prose | pages [19] -->
• Our model puts forward variable parameters to form a parameter list. By changing the parameters in the list, we can achieve diﬀerent income results. In the future, we can form

<!-- b000442 | furniture | pages [20] -->
Team # 2203120

<!-- b000443 | furniture | pages [20] -->
Page 19 of 23

<!-- b000444 | prose | pages [20] -->
an investment prediction software according to the model. We only need to understand the meaning of relevant parameters to realize asset management. Therefore, our model is relatively simple and easy to understand.

<!-- b000445 | prose | pages [20] -->
• The parameters in the model have a large variable range and are more ﬂexible.

<!-- b000446 | prose | pages [20] -->
• The model is only based on the price changes of gold and bitcoin in recent ﬁve years, so the model has low requirements for data.

<!-- b000447 | prose | pages [20] -->
6.2 Possible Improvements

<!-- b000448 | prose | pages [20] -->
• In the process of solving the model, the mixed purchase strategy of gold and bitcoin is not well considered, which needs to be improved.

<!-- b000449 | prose | pages [20] -->
• Due to the lack of ﬁnancial knowledge, the establishment of the model is not necessarily perfect.

<!-- b000450 | prose | pages [20] -->
7

<!-- b000451 | heading | pages [20] -->
Memorandum

<!-- b000452 | heading | pages [20] -->
Memorandum

<!-- b000453 | prose | pages [20] -->
To: traders

<!-- b000454 | prose | pages [20] -->
From: Team #2203120

<!-- b000455 | heading | pages [20] -->
Subject: Investment model, Trading Strategy and Results of Bitcoin and Gold

<!-- b000456 | prose | pages [20] -->
Date: February 22, 2022

<!-- b000457 | prose | pages [20] -->
With the development of economy and the popularization of ﬁnancial management concept, more and more people have joined the ranks of investment. In addition to the traditional treasury bonds, funds, stocks, gold and so on, virtual currency has increasingly appeared in people’s vision, setting oﬀa "currency speculation fever". Investment involves both returns and risks. In order to explore the best trading strategy, our team has established a trading strategy model based on the price trend of gold and bitcoin in the past ﬁve years to help you better invest.

<!-- b000458 | prose | pages [20] -->
STRATEGY

<!-- b000459 | prose | pages [20] -->
The strategy we designed mainly focuses on three questions: when to trade, what kind of assets to trade and how much to trade.

<!-- b000460 | furniture | pages [21] -->
Team # 2203120

<!-- b000461 | furniture | pages [21] -->
Page 20 of 23

<!-- b000462 | caption | pages [21] -->
Figure 16: Structure of transaction strategy model

<!-- b000463 | prose | pages [21] -->
When to trade. We measured the hit rate of the current model, the rise and fall of gold • and bitcoin, and the proportion of cash after trading. Only when the three indicators meet the trading conditions at the same time can the transaction be carried out, and it is decided whether to buy or sell. On the contrary, if the trading conditions are not met, wait until the next cycle for judgment

<!-- b000464 | prose | pages [21] -->
• Deal what. By setting the threshold of increase and decrease, compare the rise and fall range of gold and bitcoin, measure the risk and return of trading bitcoin and gold, and decide to trade gold or bitcoin.

<!-- b000465 | prose | pages [21] -->
• How much is the deal. If we decide to buy, we will use the decision coeﬃcient of the current model to decide how much to buy. When the judgment coeﬃcient is small, it means that the model we currently use is relatively stable and the risk is small. Therefore, when purchasing, we can appropriately increase the purchase proportion, on the contrary, reduce the purchase proportion; If we decide to sell, we will sell according to the preset proportion.

<!-- b000466 | prose | pages [21] -->
For the above strategies, by changing the variable parameters in the strategy, three strategies can be formed: insurance type, common type and radical type, which are suitable for diﬀerent traders and have good generalization ability. Secondly, when the variable parameters in the strategy are disturbed, the results show that the total assets change within a certain range, indicating that the anti-interference ability of the model is strong. Finally, by comparing the beneﬁts of $1000 deposited in the bank for ﬁve years and the ﬁve-year trading of this strategy, it can be seen that our strategy can resist inﬂation to a certain extent.

<!-- b000467 | heading | pages [21] -->
MODEL

<!-- b000468 | prose | pages [21] -->
The strategy is based on the prediction of the future. In view of the simplicity and eﬃciency of ARIMA model, which only needs endogenous variables rather than other exogenous variables, we choose ARIMA model as the price prediction model. In order to predict the future market timely and accurately, we use the data of 30 consecutive days as the training set and the data of the next 3 days as the test set. The correlation coeﬃcient R2 between gold’s prediction result and the real value is 0.8591, and bitcoin’s R2 is 0.9304, which are close to 1, indicating that the correlation between the predicted value and the real value is strong and the prediction accuracy is high. Such prediction lays a solid foundation for follow-up work.

<!-- b000469 | furniture | pages [22] -->
Team # 2203120

<!-- b000470 | furniture | pages [22] -->
Page 21 of 23

<!-- b000471 | prose | pages [22] -->
The determination of trading strategy is essentially a dynamic programming problem. We need to maximize the return while taking into account the risk. Therefore, establish the objective function:

<!-- b000472 | prose | pages [22] -->
wj,mj Aj −λ × Sj max

<!-- b000473 | prose | pages [22] -->
where, Wj represents the roportion of gold and bitcoin bought on day j, mj represents the roportion of gold and bitcoin sought on day j, Aj represents the total assets on day j, λ represents the coeﬃcient of regular term, which is used to control risk and return, Si represents the current day risk.

<!-- b000474 | prose | pages [22] -->
By changing the coeﬃcient of the regular term λ, the risk can be adjusted and divided into three investment strategies: steady investment, common investment and radical investment.

<!-- b000475 | heading | pages [22] -->
RESULTS

<!-- b000476 | prose | pages [22] -->
Through the training of parameters, we have obtained models for three diﬀerent populations. The best returns and some transaction information of the three models are shown in the table below:

<!-- b000477 | caption | pages [22] -->
Table 8: Results of three types of strategies

<!-- b000478 | prose | pages [22] -->
Insurance-type

<!-- b000479 | prose | pages [22] -->
Total assets 14312.68 [C, G, B]

<!-- b000480 | prose | pages [22] -->
Common-type Radical-type

<!-- b000481 | prose | pages [22] -->
50040.55 132089.11 [11474.39, 1.59, 1.07] Number of transactions 85 SD 3861.73 [421.14, 0.61, 1.05] [22.31, 0.16, 2.84] 58 9 15501.99 40067.35

<!-- b000482 | prose | pages [22] -->
Through the analysis of the results, we can see that:

<!-- b000483 | prose | pages [22] -->
• The amount of investment is mainly bitcoin.

<!-- b000484 | prose | pages [22] -->
• Insurance investment tends to trade many times and is vulnerable to market inﬂuence. Ag- gressive investments make fewer transactions.

<!-- b000485 | furniture | pages [23] -->
Team # 2203120

<!-- b000486 | furniture | pages [23] -->
Page 22 of 23

<!-- b000487 | heading | pages [23] -->
References

<!-- b000488 | references | pages [23] -->
[1] Conlon. T and McGee. R. Safe haven or risky hazard? Bitcoin during the Covid-19 bear

<!-- b000489 | references | pages [23] -->
market. FINANCE RESEARCH LETTERS, 35, 2020.

<!-- b000490 | references | pages [23] -->
[2] Khashei. M and Bĳari. M. A novel hybridization of artiﬁcial neural networks and ARIMA

<!-- b000491 | references | pages [23] -->
models for time series forecasting. APPLIED SOFT COMPUTING, 11(2):2664-2675, 2011.

<!-- b000492 | references | pages [23] -->
[3] Aasim, Singh. SN and Mohapatra. A. Repeated wavelet transform based ARIMA model for

<!-- b000493 | references | pages [23] -->
very short-term wind speed forecasting. RENEWABLE ENERGY, 136:758-768, 2019.

<!-- b000494 | references | pages [23] -->
[4] Valipour. M, Banihabib. ME and Behbahani. SMR. Comparison of the ARMA, ARIMA, and

<!-- b000495 | references | pages [23] -->
the autoregressive artiﬁcial neural network models in forecasting the monthly inﬂow of Dez

<!-- b000496 | references | pages [23] -->
dam reservoir. JOURNAL OF HYDROLOGY, 476:433-441, 2013.

<!-- b000497 | references | pages [23] -->
[5] Mahjoub. C, Bellanger. JJ, Kachouri. A and Jeannes. RL. On the performance of temporal

<!-- b000498 | references | pages [23] -->
Granger causality measurements on time series: a comparative study. SIGNAL IMAGE AND

<!-- b000499 | references | pages [23] -->
VIDEO PROCESSING, 14(5):955-963, 2020.

<!-- b000500 | references | pages [23] -->
[6] Chen. JS, Hou. JL, Wu. SM and Chang-Chien. YW. Constructing investment strategy

<!-- b000501 | references | pages [23] -->
portfolios by combination genetic algorithms. EXPERT SYSTEMS WITH APPLICATIONS,

<!-- b000502 | references | pages [23] -->
36(2):3824-3828, 2009.

<!-- b000503 | references | pages [23] -->
[7] Wang. S, Wang. XG, Meng. FL, Yang. RJ, Zhao. YJ. Investor behaviour monitoring based on

<!-- b000504 | references | pages [23] -->
deep learning. BEHAVIOUR & INFORMATION TECHNOLOGY, 40 (9):XLII-LIII, 2021.

<!-- b000505 | references | pages [23] -->
[8] Michael. SC. Can information technology enable proﬁtable diversiﬁcation?

<!-- b000506 | references | pages [23] -->
An empiri-

<!-- b000507 | references | pages [23] -->
cal examination. JOURNAL OF ENGINEERING AND TECHNOLOGY MANAGEMENT,

<!-- b000508 | references | pages [23] -->
24(3):167-185, 2007.

<!-- b000509 | references | pages [23] -->
[9] Mitic. P. Is a Reputation Time Series White Noise? INTELLIGENT DATA ENGINEERING

<!-- b000510 | references | pages [23] -->
AND AUTOMATED LEARNING - IDEAL 2017, 10585:543-550, 2017.

<!-- b000511 | references | pages [23] -->
[10] Daigle. CL and Ridge. EE, Investing in stockpeople is an investment in animal welfare and

<!-- b000512 | references | pages [23] -->
agricultural sustainability. ANIMAL FRONTIERS, 8(3):53-59, 2018.

<!-- b000513 | references | pages [23] -->
[11] Mariana. CD, Ekaputra. IA and Husodo. ZA. Are Bitcoin and Ethereum safe-havens for stocks

<!-- b000514 | references | pages [23] -->
during the COVID-19 pandemic? FINANCE RESEARCH LETTERS, 38, 2021.

<!-- b000515 | references | pages [23] -->
[12] Conlon. T, Corbet. S and Mcgee. RJ. Are cryptocurrencies a safe haven for equity markets? An

<!-- b000516 | references | pages [23] -->
international perspective from the COVID-19 pandemic. RESEARCH IN INTERNATIONAL

<!-- b000517 | references | pages [23] -->
BUSINESS AND FINANCE, 54, 2020.

<!-- b000518 | furniture | pages [24] -->
Team # 2203120

<!-- b000519 | furniture | pages [24] -->
Page 23 of 23

<!-- b000520 | heading | pages [24] -->
Appendices

<!-- b000521 | heading | pages [24] -->
Appendix A

<!-- b000522 | prose | pages [24] -->
Changes of Various Types of Traders’ Assetes

<!-- b000523 | prose | pages [24] -->
(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin

<!-- b000524 | caption | pages [24] -->
Figure 17: Changes of various assets of common-type traders

<!-- b000525 | prose | pages [24] -->
(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin

<!-- b000526 | caption | pages [24] -->
Figure 18: Changes of various assets of radical-type traders
