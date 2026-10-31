# P-C-2022-2200688-b6248fa6

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
2200688

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
PADRRI: Prediction And Decision Models For Best Return And

<!-- b000008 | title | pages [1] -->
Risk With High Interpretability

<!-- b000009 | prose | pages [1] -->
Gold and Bitcoin are two volatile assets that market traders often need to buy and sell frequently to maximize their total return. Due to market factors such as the volatility of prices, the policies of quantitative investment are of great significance to resist the risk and get profit. To provide the best daily trading strategy that achieves the maximum return, we establish the PADRRI model (Prediction And Decision models for best Return and Risk with high Interpretability).

<!-- b000010 | prose | pages [1] -->
The PADRRI model is divided into two parts. The first part is the forecasting model, whose accuracy has a direct impact on the strategy of our model, and in turn affects the final total return. We compared some common time series forecasting algorithms, including deep learning-based methods such as LSTM , Autoregressive Integrated Moving Average model (ARIMA) and so on. With comparison and experiments, Prophet algorithm is finally adopted which accurately and efficiently predicts the prices of gold and bitcoin with higher interpretability. Additionally, to reduce overfitting and improve the prediction accuracy, an improved Prophet algorithm called X-Prophet is used by introducing a strong classifier model, XGBoost.

<!-- b000011 | prose | pages [1] -->
Based on the high instability of the bitcoin price, Sliding Window Mechanism is proposed to predict the future bitcoin price using only data within a sliding window (e.g., the previous season). Interestingly, this design is highly consistent with the way economics experts predict bitcoin prices in real-world scenarios, which can be regarded as a combination of machine learning and human intuition. The proposed approach significantly improves the prediction accuracy and provides strong support for decision models. With the improved forecasting model X-Prophet cooperated with the sliding window mechanism, we achieve highly accurate predictions of gold and bitcoin prices and provides a solid foundation for the trading decision phase.

<!-- b000012 | prose | pages [1] -->
The second part is the Decision model that uses the prediction results of the forecasting model to generate the best daily trading policies to maximize the return. However, relying solely on forecasts of future prices may lead to higher investment risks. To balance this risk, a combination of forecasting results and the 5-day SMA Principle are adopted. In this way, expert knowledge in finance can be combined with machine predictions to provide more robust decisions in a human-machine collaborative fashion. Our model has proven to be quite effective in making decisions and has resulted in a significant return.

<!-- b000013 | prose | pages [1] -->
For PADRRI, we also provide evidence that our algorithm can maximize the total return for market traders. The effectiveness of the prediction model X-Prophet is first demonstrated, followed by a presentation of the decision model’s ability to provide the best trading strategy under the assumption of highly accurate prediction results. The experimental results show that our prediction model and decision model can achieve a pretty good result.

<!-- b000014 | prose | pages [1] -->
We also conduct sensitivity analysis, which shows that our model is robust to the key parameters like transaction costs. And then the strengths, weaknesses and further improvements of our model are summarized. A brief conclusion is presented in the paper. Finally, a memo which communicates our strategy, model, and results to the trader and provides suggestions on the best daily trading strategy is written in the end of paper.

<!-- b000015 | keywords | pages [1] -->
Keywords: Forecasting, Prophet, Sliding Window Mechanism, 5-day SMA

<!-- b000016 | furniture | pages [2] -->
Team 2200688

<!-- b000017 | furniture | pages [2] -->
Page 2

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1 Introduction

<!-- b000020 | contents | pages [2] -->
3

<!-- b000021 | contents | pages [2] -->
1.1

<!-- b000022 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | contents | pages [2] -->
1.2

<!-- b000025 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
3

<!-- b000027 | contents | pages [2] -->
1.3

<!-- b000028 | contents | pages [2] -->
Our work

<!-- b000029 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
4

<!-- b000031 | contents | pages [2] -->
2 Assumptions

<!-- b000032 | contents | pages [2] -->
5

<!-- b000033 | contents | pages [2] -->
3 Abbreviation and Definitions

<!-- b000034 | contents | pages [2] -->
5

<!-- b000035 | contents | pages [2] -->
4 Model

<!-- b000036 | contents | pages [2] -->
5

<!-- b000037 | contents | pages [2] -->
4.1

<!-- b000038 | contents | pages [2] -->
Prediction Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
4.1.1

<!-- b000041 | contents | pages [2] -->
Model Selection

<!-- b000042 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
6

<!-- b000044 | contents | pages [2] -->
4.1.2

<!-- b000045 | contents | pages [2] -->
Prophet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
6

<!-- b000047 | contents | pages [2] -->
4.1.3

<!-- b000048 | contents | pages [2] -->
Improvement Prophet - X-Prophet . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
9

<!-- b000050 | contents | pages [2] -->
4.2

<!-- b000051 | contents | pages [2] -->
Decision Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
10

<!-- b000053 | contents | pages [2] -->
4.2.1

<!-- b000054 | contents | pages [2] -->
The 5-day SMA method of decision making . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
10

<!-- b000056 | contents | pages [2] -->
4.2.2

<!-- b000057 | contents | pages [2] -->
Decision-making method based on adaptive price forecasts for the next N days

<!-- b000058 | contents | pages [2] -->
11

<!-- b000059 | contents | pages [2] -->
5 Implementation

<!-- b000060 | contents | pages [2] -->
11

<!-- b000061 | contents | pages [2] -->
5.1

<!-- b000062 | contents | pages [2] -->
Data Preprocessing and Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
11

<!-- b000064 | contents | pages [2] -->
5.1.1

<!-- b000065 | contents | pages [2] -->
Data Normalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
12

<!-- b000067 | contents | pages [2] -->
5.1.2

<!-- b000068 | contents | pages [2] -->
Stability Testing

<!-- b000069 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
12

<!-- b000071 | contents | pages [2] -->
5.1.3

<!-- b000072 | contents | pages [2] -->
Pure Randomness Testing

<!-- b000073 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
13

<!-- b000075 | contents | pages [2] -->
5.2

<!-- b000076 | contents | pages [2] -->
Prediction using X-Prophet model

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
13

<!-- b000079 | contents | pages [2] -->
5.2.1

<!-- b000080 | contents | pages [2] -->
Single Period Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
14

<!-- b000082 | contents | pages [2] -->
5.2.2

<!-- b000083 | contents | pages [2] -->
Global Forecast . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
14

<!-- b000085 | contents | pages [2] -->
5.3

<!-- b000086 | contents | pages [2] -->
Get Best Profit by Decision Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
16

<!-- b000088 | contents | pages [2] -->
6 Evidence of model optimality

<!-- b000089 | contents | pages [2] -->
16

<!-- b000090 | contents | pages [2] -->
6.1

<!-- b000091 | contents | pages [2] -->
Description of Final Profit Calculation Procedure . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
17

<!-- b000093 | contents | pages [2] -->
6.2

<!-- b000094 | contents | pages [2] -->
The Proposed Model Gives Optimal Decision . . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [2] -->
18

<!-- b000096 | contents | pages [2] -->
6.3

<!-- b000097 | contents | pages [2] -->
The Proposed Model Considers About Risks . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [2] -->
19

<!-- b000099 | contents | pages [2] -->
7 Sensitive Analysis

<!-- b000100 | contents | pages [2] -->
19

<!-- b000101 | contents | pages [2] -->
8 Strengths and weaknesses

<!-- b000102 | contents | pages [2] -->
20

<!-- b000103 | contents | pages [2] -->
8.1

<!-- b000104 | contents | pages [2] -->
Strengths

<!-- b000105 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
20

<!-- b000107 | contents | pages [2] -->
8.2

<!-- b000108 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
20

<!-- b000110 | contents | pages [2] -->
8.3

<!-- b000111 | contents | pages [2] -->
Further Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [2] -->
21

<!-- b000113 | contents | pages [2] -->
9 Conclusion

<!-- b000114 | contents | pages [2] -->
21

<!-- b000115 | contents | pages [2] -->
10 Memorandum

<!-- b000116 | contents | pages [2] -->
22

<!-- b000117 | furniture | pages [3] -->
Team 2200688

<!-- b000118 | furniture | pages [3] -->
Page 3

<!-- b000119 | heading | pages [3] -->
1 Introduction

<!-- b000120 | heading | pages [3] -->
1.1 Background

<!-- b000121 | prose | pages [3] -->
Gold’s price volatility has been moderate, and liquidity has been adequate, allowing investors to avoid investment risks. Bitcoin, when compared to gold, has a higher yield, greater volatility, and is unregulated and taxed, giving it a lot of room for growth in the financial market. It can also be used to hedge against gold. As a result, a gold-and-bitcoin portfolio is extremely important. Market traders frequently purchase and sell highly volatile assets in order to maximize their total income.

<!-- b000122 | prose | pages [3] -->
According to The Street’s survey [6], bitcoin has gradually entered the lives of the general public and is having a greater impact on economic development. However, the need to pay a commission for each purchase and sale, as well as the volatility of the financial markets, makes it very telling how to allocate funds wisely for purchases and when to buy and sell gold and bitcoin. Typically, investment traders will forecast future gold and bitcoin prices based on recent gold and bitcoin price movements, and then decide whether to buy, sell, or hold based on their forecasts, maximizing their profits and mitigating risk.

<!-- b000123 | caption | pages [3] -->
Figure 1: Results of The Street’s bitcoin poll, which interviewed 1,005 U.S. citizens. [6]

<!-- b000124 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000125 | prose | pages [3] -->
We need to develop a model that uses only the past stream of daily prices to date to determine each day if the trader should buy, hold, or sell their assets in their portfolio. Trader’s portfolio only contains gold and bitcoin, and we need to note that bitcoin can be traded every day, but gold can be only traded on days the market is open.

<!-- b000126 | furniture | pages [4] -->
Team 2200688

<!-- b000127 | furniture | pages [4] -->
Page 4

<!-- b000128 | prose | pages [4] -->
After through in-depth analysis and research on the background of the problem, we can specify that our article should cover the following aspects:

<!-- b000129 | prose | pages [4] -->
1. Develop a model that gives the best daily trading strategy based only on price data up to that day.

<!-- b000130 | prose | pages [4] -->
And we should use our model to figure out how much is the initial $1000 investment worth on 9/10/2021.

<!-- b000131 | prose | pages [4] -->
2. Present evidence that our model provides the best strategy.

<!-- b000132 | prose | pages [4] -->
3. Determine how sensitive the strategy is to transaction costs. How do transaction costs affect the strategy and result.

<!-- b000133 | prose | pages [4] -->
4. Communicate the strategy, model, and results to the trader in a memorandum of at most two pages.

<!-- b000134 | heading | pages [4] -->
1.3 Our work

<!-- b000135 | prose | pages [4] -->
Decision Module Prediction Module

<!-- b000136 | prose | pages [4] -->
Next Period

<!-- b000137 | caption | pages [4] -->
Figure 2: Overall structure of our model

<!-- b000138 | prose | pages [4] -->
To provide the best daily trading strategy that achieves the maximum return, the PADRRI model is established. It is divided into two parts, namely, forecasting model and decision model. The X-Prophet algorithm is adopted with sliding window mechanism, while the 5-day SMA Principle is combined with prediction result to generate the trading policies. Our work mainly includes the following:

<!-- b000139 | prose | pages [4] -->
1. The X-Prophet algorithm is adopted to improve the accuracy of the prediction and prevent overfitting with high interpretability based on statistic model.

<!-- b000140 | prose | pages [4] -->
2. The decision model is established to give the best daily trading strategy based on the prediction result and 5-day SMA Principle to balance the return and risk.

<!-- b000141 | prose | pages [4] -->
3. Present evidence that our model provides the best strategy.

<!-- b000142 | prose | pages [4] -->
4. Do sensitive analysis to show how transaction cost affect the strategy and result.

<!-- b000143 | furniture | pages [5] -->
Team 2200688

<!-- b000144 | furniture | pages [5] -->
Page 5

<!-- b000145 | heading | pages [5] -->
2 Assumptions

<!-- b000146 | prose | pages [5] -->
To simplify the analysis of our problem, we make the following assumptions, each of which is properly justified.

<!-- b000147 | prose | pages [5] -->
1. We assume that the prices of gold and bitcoin are not significantly correlated, since gold and bitcoin are two investment assets with different characteristics in financial markets.

<!-- b000148 | prose | pages [5] -->
2. Assume that the current prices of gold and bitcoin have a strong correlation with previous prices, so that we can use previous daily price to predict the tend of price in the future.

<!-- b000149 | heading | pages [5] -->
3. Since the pricing data files LBMA-GOLD.csv and BCHAIN-MKPRU.csv can be used, we

<!-- b000150 | prose | pages [5] -->
assume that only the previous daily prices can affect the future price of gold and bitcoin.

<!-- b000151 | heading | pages [5] -->
3 Abbreviation and Definitions

<!-- b000152 | prose | pages [5] -->
For convenience, we introduce some important notations below.

<!-- b000153 | heading | pages [5] -->
Notations

<!-- b000154 | prose | pages [5] -->
Explanations a(t) the trend of the time series over the non-period b(t) the period term of Prophet c(t) the holiday term of Prophet 𝜖 the error term H(t) the model capacity k the growth rate 𝜃 the amount of change in the growth rate m the offset parameter 𝛽 the seasonality prior scale t holidays prior scale, and the default value is 10

<!-- b000155 | heading | pages [5] -->
4 Model

<!-- b000156 | heading | pages [5] -->
4.1 Prediction Model

<!-- b000157 | prose | pages [5] -->
Gold and bitcoin price forecasting is a typical time series forecasting problem. The purpose of analyzing time series is to predict future trends. Traditional time series forecasting methods, such as moving average, are used to smooth out the time series. Increasing the number of periods in the moving average method will make the smoothing of fluctuations better, but it will also make the forecast values more insensitive to the actual changes in the data. With the development of machine learning and artificial intelligence, a large number of machine learning algorithms and deep learning algorithms are used to solve time series forecasting problems. For example, the long and short term memory network (LSTM) can solve the defect of recurrent neural network (RNN) which is difficult to remember the data features with long time interval, but it is still not a good solution for long sequences. The random forest algorithm can provide an effective method to balance the data set error, but it does not solve the regression problem well and is not able to make predictions beyond the range of the training set data.

<!-- b000158 | furniture | pages [6] -->
Team 2200688

<!-- b000159 | furniture | pages [6] -->
Page 6

<!-- b000160 | prose | pages [6] -->
In this paper, we use the Prophet model, which has a simple, easy-to-explain periodic structure that is well compatible with and explains event nodes such as holidays, and experiments show that Prophet performs relatively well in predicting future prices of gold and bitcoin. Since the original Prophet is prone to over-fitting problems at some specific time points, which affects the prediction results, we use an improved version of Prophet to predict the future prices of gold and bitcoin.

<!-- b000161 | heading | pages [6] -->
4.1.1 Model Selection

<!-- b000162 | prose | pages [6] -->
ARIMA is the most commonly used time series forecasting model. However, ARIMA requires the timing data to be stationary, or stable after being differencing. And, ARIMA can only capture linear relationships by nature, but not nonlinear relationships. Therefore, to predict the time series data using ARIMA model, it must be stable, and if the data is unstable, it cannot capture the pattern. For example, the reason why Bitcoin data cannot be predicted with ARIMA is that it is non-stationary and often fluctuates due to policies and news.

<!-- b000163 | prose | pages [6] -->
LSTM is also commonly used in time series prediction because of its powerful performance. However, on the one hand, deep learning-based methods such as LSTM rely on the quantity of data and are prone to overfitting. In other words, even if LSTM fits the current data with high quality, it may lose generalization due to overfitting, which is not very meaningful for practical scenarios. On the other hand, LSTM requires high demand on computational resources and may take longer training time in the current environment. Finally, LSTM lacks interpretability and is difficult to convince the market.

<!-- b000164 | prose | pages [6] -->
Therefore, a more interpretable and efficient time series prediction model is required for this task.

<!-- b000165 | heading | pages [6] -->
4.1.2 Prophet

<!-- b000166 | prose | pages [6] -->
Prophet [1] is a data prediction tool based on python and R language open source by Facebook. As shown in Fig. 3. The algorithm is designed based on time series decomposition and machine learning fitting, and can handle not only the case of some outliers in the time series, but also the case of some missing values. Prophet can predict the future trend of the time series almost fully automatically, due to the use of pyStan, an open source tool, in the fitting model, also makes prophet can get the prediction results in a very short time.

<!-- b000167 | prose | pages [6] -->
Prophet is an additive model that consists of four components, namely the trend term, the period term, the holiday term and the error term.

<!-- b000168 | prose | pages [6] -->
𝑝(𝑡) = 𝑎(𝑡) + 𝑏(𝑡) + 𝑐(𝑡) + 𝜖 (1)

<!-- b000169 | prose | pages [6] -->
where a(t) denotes the trend term, which is the trend of the time series over the non-period. b(t) denotes the period term, c(t) denotes the holiday term, which indicates the presence of a holiday on that day, and 𝜖denotes the error term.

<!-- b000170 | prose | pages [6] -->
There are two important functions for the a(t) trend term, one based on the logistic regression function and the other based on the segmented linear function.

<!-- b000171 | prose | pages [6] -->
The logistic regression-based growth model is as follows:

<!-- b000172 | prose | pages [6, 7] -->
𝐻(𝑡) 𝑎(𝑡) = (2) ′𝜃) ∗(𝑡−(𝑚+ 𝑧(𝑡)𝑇𝛾))) 1 + 𝑒𝑥𝑝(−(𝑘+ 𝑧(𝑡) 𝑧(𝑡) = (𝑧1(𝑡), ..., 𝑧𝑠(𝑡))𝑇 (3) Modeling

<!-- b000173 | furniture | pages [7] -->
Team 2200688

<!-- b000174 | furniture | pages [7] -->
Page 7

<!-- b000176 | prose | pages [7] -->
Visually Forecast Inspect Evaluation Forecasts

<!-- b000177 | prose | pages [7] -->
Surface Problems

<!-- b000178 | caption | pages [7] -->
Figure 3: Schematic view of the analyst-in-the-loop approach to forecasting at scale, which best makes

<!-- b000179 | prose | pages [7] -->
use of human and automated tasks. [1]

<!-- b000180 | prose | pages [7] -->
𝜃(𝑡) = (𝜃1, ..., 𝜃𝑠)𝑇 (4) 𝛾(𝑡) = (𝛾1, ..., 𝛾𝑠)𝑇 (5) where H(t) denotes the model capacity, k denotes the growth rate, and, 𝜃denotes the amount of change in the growth rate. As t increases, a(t) converges to H(t). When using Prophet’s growth = ’logistic’, the value of H(t) needs to be set in advance.

<!-- b000181 | prose | pages [7] -->
A model based on segmented linear functions:

<!-- b000182 | prose | pages [7] -->
𝑎(𝑡) = (𝑘+ 𝑧(𝑡)𝜃) · 𝑡+ (𝑚+ 𝑧(𝑡)𝑇𝛾) (6) where k denotes the growth rate, 𝜃denotes the change in growth rate, and m denotes the offset parameter.

<!-- b000183 | prose | pages [7] -->
The periodic function of the seasonal periodicity b(t) can be represented by a sine or cosine function. So the periodicity of the time series can be modeled using a Fourier series, for example:

<!-- b000184 | prose | pages [7] -->
𝐼∑︁ (𝑎𝑖𝑐𝑜𝑠(2𝜋𝑖𝑡 + 𝑏𝑖𝑠𝑖𝑛(2𝜋𝑖𝑡 𝑏(𝑡) = 𝑝)) (7) 𝑝 𝑖=1

<!-- b000185 | prose | pages [7] -->
we can define the following equation:

<!-- b000186 | prose | pages [7] -->
𝛿= (𝑎1, 𝑏1, ..., 𝑎𝐼, 𝑏𝐼)𝑇 (8)

<!-- b000187 | prose | pages [7] -->
𝑥(𝑡) = [𝑐𝑜𝑠(2𝜋1𝑡 𝑝), ..., 𝑠𝑖𝑛(2𝜋𝐼𝑡 𝑝)] (9)

<!-- b000188 | prose | pages [7] -->
Therefore, we can express b(t) into vector form:

<!-- b000189 | prose | pages [7, 8] -->
𝑏(𝑡) = 𝑥(𝑡)𝛿 (10) For a sequence with a yearly period, p = 365.25 and I = 10, then:

<!-- b000190 | furniture | pages [8] -->
Team 2200688

<!-- b000191 | furniture | pages [8] -->
Page 8

<!-- b000193 | prose | pages [8] -->
𝑥(𝑡) = [𝑐𝑜𝑠( 2𝜋1𝑡 365.25), ..., 𝑠𝑖𝑛( 2𝜋10𝑡 365.25)] (11)

<!-- b000194 | prose | pages [8] -->
For a sequence with a weakly period, p = 7 and I = 3, then:

<!-- b000195 | prose | pages [8] -->
𝑥(𝑡) = [𝑐𝑜𝑠(2𝜋1𝑡 ), ..., 𝑠𝑖𝑛(2𝜋3𝑡 )] (12) 7 7 Thus, the seasonal term of the time series is: 𝑏(𝑡) = 𝑥(𝑡)𝛿, and the initialization of 𝛿is 𝛿= normal( 0, 𝛽2). 𝛽= seasonality prior scale, and a larger value of 𝛽indicates a more pronounced effect of seasonality.

<!-- b000196 | prose | pages [8] -->
Holiday items c(t) model can be written as:

<!-- b000197 | prose | pages [8] -->
𝐿 ∑︁ 𝑐(𝑡) = 𝑚(𝑡)𝑘= ∗𝐼𝑙∈𝐷𝑖 (13) 𝑖=1

<!-- b000198 | prose | pages [8] -->
𝑚(𝑡) = (𝑙∈𝐷𝑖, ..., 𝑙∈𝐷𝐿) (14) 𝑘= (𝑘1, ..., 𝑘𝐿)𝑇 (15) The initialization of k is k = Normal( 0, 𝑡2), t = holidays prior scale, and the default value is 10, when a larger value indicates that holidays have a greater impact on the model.

<!-- b000199 | prose | pages [8] -->
For the Change-point Selection in Prophet model, before introducing the changepoint, it is important to introduce the Laplace distribution, which has a probability density function as follow:

<!-- b000200 | prose | pages [8] -->
𝑓(𝑥|𝜃, 𝑡) = 𝑒𝑥𝑝(−|𝑥−𝜃|/𝑡)/2𝑡 (16) where 𝜃denotes the location parameter and t > 0 denotes the scale parameter. The Laplace distribution is somewhat different from the normal distribution. In the Prophet algorithm, it is necessary to give the location of the variable points, the number of them, and the rate of change of the growth. Therefore, there are three more important indicators, namely:

<!-- b000201 | prose | pages [8] -->
1. changepoint-range

<!-- b000202 | prose | pages [8] -->
2. n-changepoint

<!-- b000203 | prose | pages [8] -->
3. changepoint-prior-scale

<!-- b000204 | prose | pages [8] -->
Changepoint-range refers to the percentage of variable points that need to be set in a time series as long as the previous changepoint-range, in the default function changepoint-range = 0.8, n-changepoint refers to the number of variable points, in the default function is n-changepoint = 25. changepoint-prior-scale indicates the distribution of the growth rate of changepoints. [4]

<!-- b000205 | furniture | pages [9] -->
Team 2200688

<!-- b000206 | furniture | pages [9] -->
Page 9

<!-- b000207 | heading | pages [9] -->
4.1.3 Improvement Prophet - X-Prophet

<!-- b000208 | prose | pages [9] -->
The original Prophet model often tends to fall into overfitting at some special time points, which makes the error of some prediction behaviors large and makes the prediction’s performance not very good. Therefore, we use XGBoost model to optimize the Prophet model, so that the optimized model can have the advantages of both models and thus reduce the prediction error.

<!-- b000209 | prose | pages [9] -->
The structure of X-Prophet is showed in4. The X-Prophet improved model is based on the original Prophet model with an additional confidence value optimization module. The function of this module is to combine the Prophet and XGBoost sub-models, and use the XGBoost model to optimize the Prophet model and reduce the model prediction error. [2]

<!-- b000210 | caption | pages [9] -->
Figure 4: The structure of improvement prophet X-Prophet

<!-- b000211 | prose | pages [9] -->
The XGBoost model is a strong classifier model that can quickly and accurately mine the data for special time point features such as holidays, and it has a regularization term to avoid overfitting in the prediction behavior when analyzing time series data. Therefore, an improved model, X-Prophet, is proposed here with the addition of a predictor optimization module to the X-Prophet model, as shown in Fig. 4. The purpose is to introduce the XGBoost term in the optimization module and optimize Prophet by using the feature of XGBoost with regular terms, so that the two models can complement each other to obtain the improved X-Prophet model and finally achieve the purpose of reducing the prediction error and improving the prediction accuracy. For the X-Prophet model after the introduction of XGBoost optimization term, the model construction can be expressed as follows: [2]

<!-- b000212 | prose | pages [9] -->
ˆ𝑦(0) = 𝑐 (17) 𝑖

<!-- b000213 | prose | pages [9, 10] -->
ˆ𝑦(1) = ˆ𝑦(0) + 𝑓1(𝑥𝑖) (18) 𝑖 𝑖 𝑖𝑡) = ˆ𝑦(𝑡−1) ˆ𝑦( + 𝑓𝑡(𝑥𝑖) (19) 𝑖 𝑓𝑡(𝑥) = 𝑤𝑞(𝑥) (20) 𝑇 𝑙𝑜𝑠𝑠( 𝑓) = 𝑦𝑇+ 1 ∑︁ 2𝛾 𝑤2 (21) 𝑗 𝑗=1 𝑊(𝑡) = 𝑤1𝑝(𝑡) + 𝑤2 ˆ𝑦𝑡(𝑤1 + 𝑤2 = 1) (22)

<!-- b000214 | furniture | pages [10] -->
Team 2200688

<!-- b000215 | furniture | pages [10] -->
Page 10

<!-- b000217 | prose | pages [10] -->
where equation (16) - (18) indicates that the X-Prophet model analyzes the data to obtain the optimal solution at the corresponding time point. Equation (19) denotes the penalty term of the model, and the penalty term is used to control the complexity of the model. Equation (20) denotes the loss function of the model, and in each iteration, the loss function minimizes the error sum of the predicted value and the loss value, i.e., the optimal model is constructed. Equation (21) denotes the final predicted value of the model. [5]

<!-- b000218 | heading | pages [10] -->
4.2 Decision Model

<!-- b000219 | prose | pages [10] -->
We use the Improved Adaptive Price Prediction Model for the N-Day Future Based on the 5-day SMA Operating Principle to make decisions on buying and selling gold and bitcoin. The model is based on price forecasts for the next N days (e.g., 15) and is supplemented by the 5-day SMA method, which has been developed by expert research and is consistent with price movement patterns. We use this model on a daily basis to make decisions on whether to buy or sell gold and bitcoin on that day. The results of this model rely entirely on price data from the previous day: the price forecast for the next N days is based entirely on past data; the 5-day SMA uses price data from the 5 days prior to the current day. The calculation results show that our model can make quite effective decisions to maximize returns.

<!-- b000220 | heading | pages [10] -->
4.2.1 The 5-day SMA method of decision making

<!-- b000221 | prose | pages [10] -->
The 5-day SMA [3] is the average of the last 5 days’ prices and is a good indicator of the recent price situation. Compare the price of the day with the 5-day SMA on the day, if the price of the day is higher than the 5-day SMA price, it means that the price of the day is higher than the average of the last 5 days, that is, the price is in an upward trend and will maintain the possibility of rising, the decision is optimistic. However, at this point, it is necessary to further combine the "5-day deviation" to finally determine whether to buy or not to buy. This is because the current price above the 5-day SMA may be much higher than the 5-day SMA and may appear to have risen significantly. According to the laws of the market, when the price rises too much, its possibility of falling also increases greatly. The "5-day deviation" is used to characterize the ratio of the current price above the 5-day SMA. If this indicator is higher than the threshold, it means that the current price has risen too much and has a high probability of falling, so it is not recommended to buy, but to sell. If this indicator is not high, it is recommended to buy. Conversely, if the current stock price is below the current day’s 5-day SMA value, it indicates that the current day’s price is lower than the recent price and is in and maintains a high probability of a downtrend, so buying is not recommended and selling is suggested. Using the past 5-day price trend combined with a forecast of future prices can also be a good way to make decisions. If the price has fallen in the last 5 days and will rise in the future forecast data, a buy is recommended.

<!-- b000222 | furniture | pages [11] -->
Team 2200688

<!-- b000223 | furniture | pages [11] -->
Page 11

<!-- b000224 | heading | pages [11] -->
4.2.2 Decision-making method based on adaptive price forecasts for the next N days

<!-- b000225 | prose | pages [11] -->
Previously, we used the X-Prophet model to make effective forecasts of future price changes based on previous data. We take the data for the next N days as the basis for the current decision. In our model, N is an adaptive parameter with an initial value set to 15. The meaning of N is that we need to look at the trend changes for the next N days when making decisions for the current day. If N is too small, too little future forecast data will be selected and the best time to buy and sell will not be found more accurately; if N is too large, too much future forecast data will be selected and the accuracy of the forecast data values further away from the current day will be lower, again affecting the accuracy of the decision. During the working of the model, N is automatically adjusted moderately according to the style of price movement it predicts. The ideal value of N is such that only one peak or trough occurs in the forecast data for the next N days.

<!-- b000226 | prose | pages [11] -->
The model analyzes and identifies the trends in the forecast data for the next N days, which are broadly classified into the following categories:

<!-- b000227 | prose | pages [11] -->
1. Monotonically increasing

<!-- b000228 | prose | pages [11] -->
2. Monotonically decreasing

<!-- b000229 | prose | pages [11] -->
3. Monotonic increasing curve first

<!-- b000230 | prose | pages [11] -->
4. Single-valley curves first decreasing

<!-- b000231 | prose | pages [11] -->
5. Multi-peak and multi-valley increasing

<!-- b000232 | prose | pages [11] -->
6. Multi-peak and multi-valley first decreasing

<!-- b000233 | prose | pages [11] -->
For case 3 and 4, there is only one peak or trough, which means that the 𝑁value is ideal. At this point, only a decision needs to be made: for case 3, the model recommends a buy operation. If a buy has been made previously, the model’s recommendation will be ignored. For case 4, the model recommends a sell operation. The model’s recommendation is ignored if it has already sold previously. The absence of peaks or troughs in case 1 and 2 indicates that 𝑁takes too small a value. The model will multiply N by a factor 𝛼to increase it appropriately after making a buy and sell recommendation respectively, in our model 𝛼= 1.1. Case 5 and 6 shows multiple peaks and valleys, indicating that the value of 𝑁is taken too small. The model will be appropriately reduced for both N multiplied by a scale factor 𝛽after making a buy and sell recommendation, respectively. In our model, 𝛽= 0.9.

<!-- b000234 | heading | pages [11] -->
5 Implementation

<!-- b000235 | heading | pages [11] -->
5.1 Data Preprocessing and Testing

<!-- b000236 | prose | pages [11] -->
Because of the special characteristics of time series (pattern correlation between adjacent series, data are continuously generated in the time dimension), their normalization methods are also different from those of non-time series. Usually, time series analysis is based on the discovery of anomalous patterns or outliers. The choice of normalization method should also facilitate the work of subsequent algorithms or models as much as possible.

<!-- b000237 | furniture | pages [12] -->
Team 2200688

<!-- b000238 | furniture | pages [12] -->
Page 12

<!-- b000239 | heading | pages [12] -->
5.1.1 Data Normalization

<!-- b000240 | prose | pages [12] -->
Since the given data (BCHAIN-MKPRU.csv and LBMA-GOLD.csv) is relatively clean and complete, operations such as denoising are not needed, work is mainly focused on normalization processing, i.e., mapping all the data to a specified range (mapping data to a range of 0 to 1 or -1 to 1 for example) for processing. In this paper, Min-Max normalization is applied, which can be formulated by following formula:

<!-- b000241 | prose | pages [12] -->
𝑋−𝑋𝑚𝑖𝑛 𝑋𝑛𝑜𝑟𝑚= (23) 𝑋𝑚𝑎𝑥−𝑋𝑚𝑖𝑛 The data is mapped to a specified range for processing, which is more convenient and fast. Turning dimensioned expressions into dimensionless expressions facilitates indicators of different units or magnitudes to be able to be compared and weighted. After normalization, the dimensioned data set is turned into a pure quantity, which can also achieve the effect of simplifying the calculation.

<!-- b000242 | heading | pages [12] -->
5.1.2 Stability Testing

<!-- b000243 | prose | pages [12] -->
(a) (b)

<!-- b000244 | prose | pages [12] -->
(c) (d)

<!-- b000245 | caption | pages [12] -->
Figure 5: (a) and (b) plot the price of gold and bitcoin. (c) and (d) plot the correlation of gold and

<!-- b000246 | prose | pages [12] -->
bitcoin. (a) - (d) show that the time series needed predicting is a relatively stable sequence.

<!-- b000247 | prose | pages [12] -->
There are two tests for the smoothness of time series: the graph test and the unit root test, respectively.

<!-- b000248 | prose | pages [12, 13] -->
Time-series plot According to the statistical characteristics of a smooth time series, the time series plot of a smooth series always fluctuates randomly around a constant value, and the fluctuation range is bounded. If the series shows a monotonic trend and periodicity, then it is non-stationary.

<!-- b000249 | furniture | pages [13] -->
Team 2200688

<!-- b000250 | furniture | pages [13] -->
Page 13

<!-- b000252 | prose | pages [13] -->
Autocorrelation plot Smoothed series usually have short-term correlation, i.e., the autocorrelation coefficient decays quickly toward zero as the number of delay periods increases, and conversely the correlation coefficient of a non-smoothed series usually decays toward zero with a lower speed.

<!-- b000253 | prose | pages [13] -->
As shown in Fig. 5, (a) and (b) plot the price of gold and bitcoin. (c) and (d) plot the correlation of gold and bitcoin. (a) - (d) show that the time series needed predicting is a relatively stable sequence.

<!-- b000254 | heading | pages [13] -->
5.1.3 Pure Randomness Testing

<!-- b000255 | prose | pages [13] -->
The absence of any correlation between sequence values means that the sequence is a sequence with no memory, i.e., past behavior has no effect on the future, and such a sequence is called a purely random sequence such as white noise sequence. The main tests for pure randomness are the Q statistic for large samples and the LB statistic for small samples.

<!-- b000256 | prose | pages [13] -->
(b) (a)

<!-- b000257 | caption | pages [13] -->
Figure 6: (a) shows the P value of the gold randomness testing, and (b) shows the P value of the

<!-- b000258 | prose | pages [13] -->
bitcoin randomness testing. It can be observed that most of the P values are significantly less than 0.05, which shows that these sequence are not pure random sequences and provide evidence for the following prediction.

<!-- b000259 | heading | pages [13] -->
5.2 Prediction using X-Prophet model

<!-- b000260 | prose | pages [13] -->
The traditional time series prediction task uses a longer time series from the past to predict the change in that series over a certain period of time in the future. This requires only one training and one prediction. In contrast, this task requires forecasting price changes for each day using data from before that day. This requires training a separate model for each day’s decision and predicting price changes over time as needed for the decision model. Therefore, the description of the forecasting model in the following paragraphs will be divided into two parts: single-step forecasting discussed in Sec. 5.2.1 and global forecasting discussed in Sec. 5.2.2.

<!-- b000261 | furniture | pages [14] -->
Team 2200688

<!-- b000262 | furniture | pages [14] -->
Page 14

<!-- b000263 | heading | pages [14] -->
5.2.1 Single Period Prediction

<!-- b000264 | prose | pages [14] -->
As the method shown in Sec. 4.1.3, Prophet is used to make predictions, its back-end system is pro- grammed using Stan, a probabilistic programming language, which facilitates Prophet to exploit many of the advantages of Bayesian algorithms, such as Giving the model a simple and easily interpretive periodic structure. What’s more, the prediction results include confidence intervals derived from the full posterior distribution, i.e., Prophet provides a data-driven risk estimate. In addition, Prophet also provides simple, easy-to-interpret forecast results for components of the time series (e.g., days of the week, or days of the year), as shown in Fig. 7.

<!-- b000265 | caption | pages [14] -->
Figure 7: The visualization of a single step in our method.

<!-- b000266 | prose | pages [14] -->
Note that, based on the fast-changing nature of Bitcoin, we innovatively propose a Prophet model based on a sliding window mechanism, the basic idea of which is shown in Figure 8. For sequence data with less than one sliding window, we use all data from the beginning to the current one. If the length of the currently known time series is larger than the length of the sliding window, we use only the data of the most recent sliding window size for prediction. Interestingly, this design is highly consistent with the way real-life economics experts predict bitcoin prices, which can be seen as a combination of machine learning and human intuition. Based on the sliding-window mechanism, the accuracy of the prediction model for our predictions significantly outperforms models that use full-window data for prediction.

<!-- b000267 | heading | pages [14] -->
5.2.2 Global Forecast

<!-- b000268 | prose | pages [14, 15] -->
In this section, the way to predict the overall gold and bitcoin price will be discussed. In fact, the global forecasting model is composed of a number of single-step forecasting models. For each day, the future data is predicted based on the data from a previous window size. A practical parameter setting is to set the window size to be 90, which means using the price of previous season to predict the future price. As shown in Fig. 9, the first day price of the prediction is plotted. It is observed that the 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15

<!-- b000269 | furniture | pages [15] -->
Team 2200688

<!-- b000270 | furniture | pages [15] -->
Page 15

<!-- b000272 | prose | pages [15] -->
01 02 03 04 05 06 07 08 09 10 11 12 13 14 15

<!-- b000273 | caption | pages [15] -->
Figure 8: The illustration of the proposed sliding window mechanism of prediction model.

<!-- b000274 | prose | pages [15] -->
price of gold is less variable relative to bitcoin and has a higher prediction accuracy overall. The high intensity variation of Bitcoin, on the other hand, places a higher demand on the accuracy of the model predictions. After the predictions are made, the decision model can make buy and sell operations for bitcoin and gold based on these predicted data.

<!-- b000275 | prose | pages [15] -->
In general, our prediction models receive two limitations: the accuracy of the prediction and the generalization of the model. For other prediction models such as LSTM, it is possible to get good results on the given dataset with the tuning of hyperparameters. However, the same model and hyperparameters may perform poorly on another similar dataset, i.e., the problem of poor generalizability. In our model, on the one hand, prophet is based on a strong statistical theory and the model has a strong interpretability, which is more easily accepted by the market. On the other hand, the model has better generalization ability and can get a good result for most of the data, saving the time and effort of tuning.

<!-- b000276 | caption | pages [15] -->
Figure 9: The final prediction of the gold and bitcoin price using X-Prophet model.

<!-- b000277 | furniture | pages [16] -->
Team 2200688

<!-- b000278 | furniture | pages [16] -->
Page 16

<!-- b000279 | heading | pages [16] -->
5.3 Get Best Profit by Decision Model

<!-- b000280 | prose | pages [16] -->
Based on the price data predicted by X-Prophet model, it is possible to make brilliant decisions about the day’s operations. However, forecasting models cannot guarantee complete accuracy, especially when the amount of previous data is small. Therefore, it is very important to introduce the "5-day SMA" method to advise and correct the decision. When there is less amount of data available, the model prefers to base its decisions on the "5-day SMA"; when more data is available, the model prefers to base its decisions on the forecast data for the next N days.

<!-- b000281 | prose | pages [16] -->
We apply the above model to daily decisions. Using the decision model everyday, decision can be made on buying or selling gold and bitcoin for the day. We decide to trade 𝛿% of the initial principal in gold and the remaining 1 −𝛿% in bitcoin. The return on the last day changes with 𝛿. The variation is shown in 5.3.

<!-- b000282 | caption | pages [16] -->
Figure 10: Variety of profit on last day with respect to radio of buying gold(𝛿%)

<!-- b000283 | prose | pages [16] -->
The figure shows that the final return is maximum for 𝛿= 2. Therefore, 2% of the initial principal is used for gold trading and the remaining 98% is used for bitcoin trading. Using our prediction model and decision model, with a principal of $1000, the final total assets will be $285,647.

<!-- b000284 | heading | pages [16] -->
6 Evidence of model optimality

<!-- b000285 | prose | pages [16, 17] -->
The proposed model can give the best strategy of trading every day due to two reasons: (1) the proposed model can always give the optimal decision; (2) the proposed model also consider about risk, making balance between profit and possible risk. Thus, the strategy given by the model is safe and excellent.

<!-- b000286 | furniture | pages [17] -->
Team 2200688

<!-- b000287 | furniture | pages [17] -->
Page 17

<!-- b000288 | caption | pages [17] -->
Figure 11: Variety of ratio of bitcoin held and gold held per month

<!-- b000290 | prose | pages [17] -->
In the following few paragraphs, the evidence that the proposed model can provide the best strategy is shown by proving the above two reasons. Before that, the procedure of calculation of final profit and how the proposed model play its part in this procedure will be first stated.

<!-- b000291 | heading | pages [17] -->
6.1 Description of Final Profit Calculation Procedure

<!-- b000292 | prose | pages [17] -->
The objective of this problem is to maximize the return on the last day. Define the number of days from the current date to the first day as 𝑖, the number of day of the last day from the first day as 𝑙𝑎𝑠𝑡𝑑𝑎𝑦,initial cash 𝑚𝑜𝑛𝑒𝑦= $1000, the ratio of buying gold as 𝛿, the price of bitcoin on day 𝑖as 𝑏𝑖, the price of gold on day 𝑖as 𝑔𝑖(if gold is not traded on that day, the price on that day is the price on the nearest trading day to that day), the trading operation for gold on day j as 𝑜𝑝𝑗,𝑔, and for bitcoin is 𝑜𝑝𝑗,𝑏, the total assets on the jth day as 𝑃𝑗, the transaction cost of gold as 𝑐𝑔, the transaction cost of bitcoin as 𝑐𝑏. The final profit decision algorithm is shown in algorithm1.The goal of our model is to find an optimal policy 𝑃𝑜𝑙𝑖𝑐𝑦, such that:

<!-- b000293 | prose | pages [17] -->
𝑃𝑜𝑙𝑖𝑐𝑦= 𝑎𝑟𝑔𝑚𝑎𝑥(𝑃𝑙𝑎𝑠𝑡𝑑𝑎𝑦(𝑃𝑜𝑙𝑖𝑐𝑦)) (24)

<!-- b000294 | prose | pages [17, 18] -->
𝑃𝑟𝑜𝑓𝑖𝑡= 𝑃𝑙𝑎𝑠𝑡𝑑𝑎𝑦(𝑃𝑜𝑙𝑖𝑐𝑦) −𝑚𝑜𝑛𝑒𝑦 (25) where the total assets on 𝑖𝑡ℎday 𝑃𝑖can be calculated as:

<!-- b000295 | furniture | pages [18] -->
Team 2200688

<!-- b000296 | furniture | pages [18] -->
Page 18

<!-- b000298 | prose | pages [18] -->
𝑃𝑖= 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑𝑖+ 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛𝑖+ 𝑔𝑜𝑙𝑑𝑖× 𝑔𝑖+ 𝑏𝑖𝑡𝑐𝑜𝑖𝑛𝑖× 𝑏𝑖 (26)

<!-- b000299 | prose | pages [18] -->
𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑𝑖represents the money invested in gold trading on the𝑖𝑡ℎday while 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛𝑖 represents the money invested in bitcoin trading on the 𝑖𝑡ℎday. 𝑔𝑜𝑙𝑑𝑖represents the amount of gold own on the 𝑖𝑡ℎday, while 𝑏𝑖𝑡𝑐𝑜𝑖𝑛𝑖represents the amount of bitcoin own on the 𝑖𝑡ℎday.

<!-- b000300 | heading | pages [18] -->
Algorithm 1 Final Profit Decision Algorithm

<!-- b000301 | prose | pages [18] -->
Require: 𝑖∈[0, 𝑙𝑎𝑠𝑡𝑑𝑎𝑦] Ensure: 𝑃𝑙𝑎𝑠𝑡𝑑𝑎𝑦 𝑚𝑜𝑛𝑒𝑦←$1000 𝑃0 ←𝑚𝑜𝑛𝑒𝑦 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑←𝑚𝑜𝑛𝑒𝑦× 𝛿% 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛←𝑚𝑜𝑛𝑒𝑦× (1 −𝛿%) 𝑔𝑜𝑙𝑑←0 𝑏𝑖𝑡𝑐𝑜𝑖𝑛←0 for 𝑗= 1 to 𝑙𝑎𝑠𝑡𝑑𝑎𝑦do 𝑜𝑝𝑗, 𝑔, 𝑜𝑝𝑗, 𝑏←DecisionFromProposedModel if 𝑜𝑝𝑗,𝑔== buy and 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑> 0 then 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑= 0 𝑔𝑜𝑙𝑑= 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑× (1 −𝑐𝑔)/𝑔𝑖 end if if 𝑜𝑝𝑗,𝑔== sold and 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑== 0 then 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑= 𝑔𝑜𝑙𝑑× 𝑔𝑗× (1 −𝑐𝑔) 𝑔𝑜𝑙𝑑= 0 end if if 𝑜𝑝𝑗,𝑏== buy and 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛> 0 then 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛= 0 𝑏𝑖𝑡𝑐𝑜𝑖𝑛= 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛× (1 −𝑐𝑏)/𝑏𝑖 end if if 𝑜𝑝𝑗,𝑏== sold and 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛== 0 then 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛= 𝑏𝑖𝑡𝑐𝑜𝑖𝑛× 𝑏𝑗× (1 −𝑐𝑏) 𝑏𝑖𝑡𝑐𝑜𝑖𝑛= 0 end if𝑃𝑗= 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐵𝑖𝑡𝑐𝑜𝑖𝑛+ 𝑀𝑜𝑛𝑒𝑦𝐹𝑜𝑟𝐺𝑜𝑙𝑑+ 𝑏𝑖𝑡𝑐𝑜𝑖𝑛× 𝑏𝑗+ 𝑔𝑜𝑙𝑑× 𝑔𝑗 end for

<!-- b000302 | heading | pages [18] -->
6.2 The Proposed Model Gives Optimal Decision

<!-- b000303 | prose | pages [18, 19] -->
As mentioned above, the X-Prophet model has high accuracy in predicting future price changes, which makes it feasible for us to use the future forecast prices to make decisions about the current operation. The higher the accuracy of the forecasting model, the greater the probability that we will make an optimal decision. However, even if our forecasting model is quite good, it still cannot achieve 100% accuracy. Therefore, we introduce the 5-day SMA method, which is proposed by expert research, to make certain corrections to the decisions made by the forecasting model, thus making the decisions more optimal.

<!-- b000304 | furniture | pages [19] -->
Team 2200688

<!-- b000305 | furniture | pages [19] -->
Page 19

<!-- b000307 | prose | pages [19] -->
The 5-day SMA is a method that has been proven to be effective by combining a large number of price curves with big data analysis and using the prices of the past 5 days to determine price movements. The 5-day SMA is the short-term average of the SMA system, reflecting the short-term trend of the price or index. Some people also call the 5-day SMA an attack line. Regardless of whether the short- term trend of the price or index is up or down, the steepness of the 5-day SMA’s angle of operation represents the magnitude of the short-term upward or downward trend of the price or index.

<!-- b000308 | prose | pages [19] -->
Therefore, by constructing an excellent forecasting model and using empirical rules, it is possible to make a fairly accurate judgment and forecast of the price trend for the current day and beyond, and thus make scientifically accurate decisions.

<!-- b000309 | heading | pages [19] -->
6.3 The Proposed Model Considers About Risks

<!-- b000310 | prose | pages [19] -->
The price of gold is less volatile and the price of bitcoin is highly volatile. The risk of investing in gold is lower than the risk of investing in bitcoin. Although the price of bitcoin has risen much more than gold, it would be riskier to invest all the principle on bitcoin.As shown in fig.5.3,the optimal solution is not to use all of the principle to buy bitcoin, it is of high risk and earn less profit. Instead, our model select a compromise solution: use a moderate amount of principle to invest in gold and use a larger portion of the remaining principle to invest in bitcoin. This will effectively reconcile risk and return to maximize final profit.

<!-- b000311 | heading | pages [19] -->
7 Sensitive Analysis

<!-- b000312 | prose | pages [19] -->
In order to determine the sensitivity of our model against differing transaction cost, a series of sensitivity analysis is performed. In the analysis, the transaction cost of gold is taken varied from 0.00005 to 0.0030, while the transaction cost of bitcoin is taken varied from 0.0001 to 0.0030. The upper limit of transaction cost of gold and bitcoin are both taken as 0.0030, with the rule that the maximum brokerage trading commission shall not exceed 0.3% of the transaction amount.

<!-- b000313 | prose | pages [19] -->
The result of sensitivity analysis is shown in fig. 12. It can be seen that bitcoin affects the total return more significantly with the increase in transaction cost relative to gold. That’s because the price of bitcoin is much higher than gold, and transaction cost can easily affect the decision of bitcoin. Therefore, bitcoin is more sensitive to transaction cost than gold.

<!-- b000314 | prose | pages [19] -->
The result of the analysis shows that, during changing transaction cost of gold in the given range, the maximum fluctuation amount of final profit is 4.86%; during changing transaction cost of bitcoin in the given range, the maximum fluctuation amount of final profit is 0.35%. Thus, as the transaction cost of gold and bitcoin changing, the total returns do not fluctuate significantly, which shows that the proposed model has a pretty good robustness in transaction cost for both gold and bitcoin.

<!-- b000315 | furniture | pages [20] -->
Team 2200688

<!-- b000316 | furniture | pages [20] -->
Page 20

<!-- b000317 | caption | pages [20] -->
Figure 12: Sensitive Analysis on gold and bitcoin transaction.

<!-- b000318 | heading | pages [20] -->
8 Strengths and weaknesses

<!-- b000319 | heading | pages [20] -->
8.1 Strengths

<!-- b000320 | prose | pages [20] -->
1. We combine and compare a lot of methods to figure out a more effective algorithm to predict the price of gold and bitcoin, and the prediction result is accurate as you can see above.

<!-- b000321 | prose | pages [20] -->
2. We use X-Prophet model with sliding window, which is a model that combines the advantages of Prophet and XGBoost, making our prediction model result more closely to the real data.

<!-- b000322 | prose | pages [20] -->
3. Our model takes amounts of factors into consideration to obtain a universal situation, and the result shows that the performance of our model is good enough in many aspects.

<!-- b000323 | prose | pages [20] -->
4. The decision model we develop can get a pretty high total return for market trader, and we also present some evidences to demonstrate that our model can provide the best strategy.

<!-- b000324 | heading | pages [20] -->
8.2 Weaknesses

<!-- b000325 | prose | pages [20] -->
1. Since only the gold daily prices and bitcoin daily prices are available, but their prices are affected by many factors. Which may it hard to predict the prices of gold and bitcoin.

<!-- b000326 | prose | pages [20] -->
2. We do some simplifications in our model to make the calculation more easily, but it may cause additional error effects.

<!-- b000327 | furniture | pages [21] -->
Team 2200688

<!-- b000328 | furniture | pages [21] -->
Page 21

<!-- b000329 | heading | pages [21] -->
8.3 Further Improvements

<!-- b000330 | prose | pages [21] -->
In view of the imperfections of our model and work, we hope to complete a more comprehensive mathematical model with the help of deeper researches. Up to now, our team still have a poor knowledge in gold and bitcoin markets. We greatly hope that our model can become more perfect with the help of the deeper understanding of the relevant background knowledge. For example, we can add more factors that affect the price of gold and bitcoin to our model to make our prediction more accurate. As we had mentioned before, the research on gold and bitcoin is of great significance, therefore, we will try our best to do more research and improve the performance of our model.

<!-- b000331 | heading | pages [21] -->
9 Conclusion

<!-- b000332 | prose | pages [21] -->
In our article, we design a model that use only the past stream of daily prices up to date to determine the strategy that market trader should employ on given day. The model can determine if the trader should buy, hold, or sell their assets in their portfolio for each day, maximizing their total return. Our model can separate into two major phases, prediction model and decision model. For the prediction model, we compare a lot of algorithms, and finally use the improvement Prophet model call X-Prophet, and we also propose a Sliding Window Mechanism based on the instability of bitcoin price. For the decision model, we use some programming methods to determine the trading strategy. We also provide evidence that our model can achieve the maximum return balancing the risk. What’s more, we perform a sensitivity analysis to verify the stability of the model and get practical guidance significance. However, due to the limitation of information given by the data, there is still a certain gap between the reality and our model. We’ll keep trying to improve our model in the future.

<!-- b000333 | heading | pages [21] -->
References

<!-- b000334 | references | pages [21] -->
[1] Taylor

<!-- b000335 | references | pages [21] -->
SJ,

<!-- b000336 | references | pages [21] -->
Letham

<!-- b000337 | references | pages [21] -->
B.

<!-- b000338 | references | pages [21] -->
2017.

<!-- b000339 | references | pages [21] -->
Forecasting

<!-- b000340 | references | pages [21] -->
at

<!-- b000341 | references | pages [21] -->
scale.

<!-- b000342 | references | pages [21] -->
PeerJ

<!-- b000343 | references | pages [21] -->
Preprints

<!-- b000344 | references | pages [21] -->
5:e3190v2

<!-- b000345 | references | pages [21] -->
https://doi.org/10.7287/peerj.preprints.3190v2.

<!-- b000346 | references | pages [21] -->
[2] Wu, Wenpei, Song, Yalin, Wei, Shangfei. Research on electricity consumption prediction based on

<!-- b000347 | references | pages [21] -->
improved Prophet model[J]. Computer Simulation,2021,38(11):473-478.

<!-- b000348 | references | pages [21] -->
[3] Five-Day SMA Trading Method: https://caifuhao.eastmoney.com/news/

<!-- b000349 | references | pages [21] -->
[4] A

<!-- b000350 | references | pages [21] -->
study

<!-- b000351 | references | pages [21] -->
of

<!-- b000352 | references | pages [21] -->
the

<!-- b000353 | references | pages [21] -->
Facebook

<!-- b000354 | references | pages [21] -->
time

<!-- b000355 | references | pages [21] -->
series

<!-- b000356 | references | pages [21] -->
prediction

<!-- b000357 | references | pages [21] -->
algorithm

<!-- b000358 | references | pages [21] -->
Prophet,

<!-- b000359 | references | pages [21] -->
https://zhuanlan.zhihu.com/p/52330017

<!-- b000360 | references | pages [21] -->
[5] Q. M. Xia, C. H. Lan, H. J. Gu, and P. C. Guo. Research on Internet money fund based on Prophet

<!-- b000361 | references | pages [21] -->
model[C]//The winning collection of papers of 2021 (7th) National Student Statistical Modeling

<!-- b000362 | references | pages [21] -->
Competition (II). [publisher unknown],2021:2014-2051.

<!-- b000363 | references | pages [21] -->
[6] Bitcoin on air, 57% of young Americans believe bitcoin will boost global economy in 2022,

<!-- b000364 | references | pages [21] -->
https://sv.bitcoinonair.com/57-of-young-americans-believe-bitcoin-boosts-global-economy

<!-- b000365 | furniture | pages [22] -->
Team 2200688

<!-- b000366 | furniture | pages [22] -->
Page 22

<!-- b000367 | heading | pages [22] -->
10 Memorandum

<!-- b000368 | prose | pages [22] -->
To: Market trader From: Team# 2200688 Date: February 22, 2022 Subject: The best daily trading strategy of gold and bitcoin

<!-- b000369 | prose | pages [22] -->
Dear Sir or Madam:

<!-- b000370 | prose | pages [22] -->
Investors frequently make predictions and decisions about whether to buy and sell gold and bitcoin to maximize their total return. In our work, we have established PADRRI model in hope to provide you the best daily trading strategy based solely on price data up to that day. We’re excited to write this memo to show you how our model works, then we’ll recommend the best strategy for you, and finally the model’s results will be presented.

<!-- b000371 | prose | pages [22] -->
Now we would like to show you our model, which is divided into two major phases, prediction and decision. For the prediction model, we only use the price data of gold and bitcoin up to that day to predict their future price. The prediction model is the most important procedure of our work, since the accuracy of prediction will have a direct impact on our final strategy. To improve prediction accuracy, we studied and experimented with a variety of existing algorithms such as LSTM based on neural networks, ARIMA, ARCH and so on. Finally, we discovered that Prophet performed admirably in our prediction work with higher prediction accuracy. Due to the limit of Prophet, it may lead to overfitting during some specific periods of given sequence. Therefore, we utilized an improvement model called X-Prophet, which combines the advantages of Prophet and XGBoost. What’ more, based on the unstable price of bitcoin, we proposed a novel sliding window mechanism. Using the prediction model, we can predict the price trend with excellent generalization ability and interpretability.

<!-- b000372 | prose | pages [22] -->
For the decision model, through our market research on gold and bitcoin, we found that gold and bitcoin conform to 5-day SMA Principle of price patterns. In order to better adapt to the price trends of gold and bitcoin, we decided to combine the price prediction with 5-Day SMA Principle to make decisions on buying and selling gold and bitcoin. The results of the improved model are based solely on price data prior to the current day, i.e., the price forecast for the next N days is based entirely on past data. Evidence shows that our decision model is able to achieve optimal results when the forecasting model performs absolutely well.

<!-- b000373 | prose | pages [22] -->
After introducing our model, we apply the above model to day-by-day decisions to maximize the final profit. The decision model is used daily to make decisions about buying and selling gold and bitcoin for the day in conjunction with the current and previous gold and bitcoin prices. From the results mentioned in the above paper, we can see that we can maximize the final return when we use 2% of the initial principal for gold trading and the remaining 98% for bitcoin trading. As shown of the results, applying our prediction model and decision model with a principal of $1000, you will end up with total assets of $285, 647.

<!-- b000374 | prose | pages [22] -->
We hope that our model can help you make the best daily trading strategy and achieve maximum total return. Investment has risks, and enter the market need to be careful. Good luck with your risk aversion and gains!

<!-- b000375 | prose | pages [22] -->
Best wishes!

<!-- b000376 | prose | pages [22] -->
Your Sincerely,

<!-- b000377 | furniture | pages [22] -->
Team#2200688

<!-- b000378 | furniture | pages [23] -->
Team 2200688

<!-- b000379 | furniture | pages [23] -->
Page 23

<!-- b000380 | heading | pages [23] -->
Appendix 1

<!-- b000381 | prose | pages [23] -->
def five_days_sma ( day , t h i n g ) : 1 """ 2 5−day SMA 3 """ 4 five_day_avg = c o u n t _ f i v e _ d a y _ l i n e ( day , t h i n g ) 5 i f p r i c e [ t h i n g ] [ day ] [ 1 ] <= five_day_avg : 6 r e t u r n 0 7 e l s e : 8 > (1 + f i v e _ d a y _ r a t e ) ∗ i f p r i c e [ t h i n g ] [ day ] [ 1 ] 9 five_day_avg :

<!-- b000382 | prose | pages [23, 24] -->
r e t u r n 0 10 e l s e : 11 r e t u r n 1 12 13 14 def g o l d _ d e c i s i o n ( day , per iod ) : 15 """ 16 Decision on gold t r a d i n g using f o r e c a s t data in n days ’ time 17 """ 18 end = min ( len ( gf ) , day + p eri od ) 19 goldf = gf [ day : end ] 20 maxp , minp = [ ] , [ ] 21 len ( goldf ) −1) : f o r i in range (1 , 22 goldf [ i ] >= goldf [ i −1] i f and goldf [ i ] >= goldf [ i + 1 ] : 23 maxp . append ( i ) 24 goldf [ i ] <= goldf [ i −1] i f and goldf [ i ] <= goldf [ i + 1 ] : 25 minp . append ( i ) 26 27 shorten , should_buy = False , False 28 i f len ( minp ) + len ( maxp ) >= 2: 29 s h o r t e n = True 30 i f maxp and not minp : 31 should_buy = True 32 i f minp and not maxp : 33 should_buy = False 34 i f minp and maxp : 35 i f minp [ 0 ] < maxp [ 0 ] : 36 should_buy = False 37 e l s e : 38 should_buy = True 39 i f len ( goldf ) < 2: 40 r e t u r n ( False , s h o r t e n ) 41 42 i f not minp and not maxp : 43 i f goldf [ 0 ] > goldf [ 1 ] : 44 should_buy = False 45 e l s e : 46 should_buy = True 47 48 r e t u r n ( should_buy , s h o r t e n ) 49 50 def b i t c o i n _ d e c i s i o n ( day , per iod ) : 51 """ 52 Decison on b i t c o i n t r a d i n g using f o r e c a s t data in n days ’ time . 53 """ 54 end = min ( len ( bf ) , day + p eri od ) 55 b i t f = bf [ day : end ] 56 maxp , minp = [ ] , [ ] 57 len ( b i t f ) −1) : f o r i in range (1 , 58 b i t f [ i −1] i f b i t f [ i ] >= and b i t f [ i ] >= b i t f [ i + 1 ] : 59 maxp . append ( i ) 60 b i t f [ i −1] i f b i t f [ i ] <= and b i t f [ i ] <= b i t f [ i + 1 ] : 61 minp . append ( i ) 62 63 shorten , should_buy = False , False 64 i f len ( minp ) + len ( maxp ) >= 2: 65 s h o r t e n = True 66 i f maxp and not minp : 67 should_buy = True 68 i f minp and not maxp : 69 should_buy = False 70 i f minp and maxp : 71 i f minp [ 0 ] < maxp [ 0 ] : 72 should_buy = False 73 e l s e : 74 should_buy = True 75 i f len ( b i t f ) < 2: 76 r e t u r n ( False , s h o r t e n ) 77 78 i f not minp and not maxp : 79 i f b i t f [ 0 ] > b i t f [ 1 ] : 80 should_buy = False 81 e l s e : 82 should_buy = True 83 84 r e t u r n ( should_buy , s h o r t e n ) 85

<!-- b000383 | furniture | pages [24] -->
Team 2200688

<!-- b000384 | furniture | pages [24] -->
Page 24
