# P-C-2022-2218931-a1aa7569

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
2218931

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
Finding the Best Strategy with Quantitative Models

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Market traders seek to maximize returns through frequent buying and selling activities. However, ﬁnancial markets are complex and volatile, and it is not easy to achieve their goals by relying only on experience to determine trading strategies. Quantitative trading methods make the path to return precise and reliable by building a reasonable model.

<!-- b000011 | prose | pages [1] -->
We constructed model I: LM-BP Neural Network Model and model II: Recurrent Decision Model. The two models are closely linked and constitute the ﬁnal Quantitative Trading Decision Model, which is used to help traders determine the best decisions for a portfolio consisting of cash, gold, and bitcoin.

<!-- b000012 | prose | pages [1] -->
For model I: We use the Levenberg-Marquardt algorithm based on numerical optimization to improve the traditional BP neural network. The model uses valid historical price data for seven days to make long-term and short-term price forecasts. Subject to trading rules, the long-term forecast for gold is ﬁve days after the day; the long-term forecast for Bitcoin is seven days after the day. Both short-term forecasts are for the next day. We tested the model with historical price data, and its R2 exceeded 0.99, and the predictions worked well.

<!-- b000013 | prose | pages [1] -->
For model II: The core idea of the circular decision model is to execute a "buy low, sell high" strategy based on the future price trend of an investment product. It consists of four stages: "Stand by", buy, hold and sell. No decisions are made for the ﬁrst ten days to accumulate historical price data; buy them if there is an uptrend in the short or long term and reach a threshold. Threshold settings are related to transaction costs and expected returns. The short-term and long-term thresholds are 2% and 3% for gold and 3.5% and 4.5% for Bitcoin. We use the Sharpe ratio to measure the riskiness of a portfolio and use it to determine the purchase share of each product in the portfolio. Sell them if both short-term and long-term forecast price declines. Account funds should be updated after each transaction is completed.

<!-- b000014 | prose | pages [1] -->
We can draw the following conclusions after model solving, model checking, and sensitivity analysis. We input historical price data into quantitative investment decision-making models for simulated trading for problem one. The initial capital is $1,000, and after a ﬁve-year trading period, the asset value is $270,836. For problem two, the evidence that we make the best decisions is that the model’s parameters have been optimized; the investment returns are also higher than simple long-term trading, short-term trading, and some high-performance investment companies. For problem three,we ﬁnd that both the trading strategy and the trading results are susceptible to the Bitcoin commission payment ratio change and less sensitive to the gold commission payment ratio change.

<!-- b000015 | prose | pages [1] -->
Finally, we wrote a memo for the trader with our models, strategies, and results. Moreover, the advantages and disadvantages of the model are analyzed.

<!-- b000016 | keywords | pages [1] -->
Keywords: LM-BP

<!-- b000017 | prose | pages [1] -->
long and short term forecast circular decision quantitative investment

<!-- b000018 | furniture | pages [2] -->
Team # 2218931

<!-- b000019 | furniture | pages [2] -->
Page 2 of 25

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | heading | pages [2] -->
Introduction

<!-- b000023 | prose | pages [2] -->
3

<!-- b000024 | prose | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000025 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3

<!-- b000026 | prose | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 4

<!-- b000027 | prose | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000028 | prose | pages [2] -->
2

<!-- b000029 | heading | pages [2] -->
Assumptions and Explanations

<!-- b000030 | prose | pages [2] -->
3

<!-- b000031 | heading | pages [2] -->
Notations

<!-- b000032 | prose | pages [2] -->
4

<!-- b000033 | heading | pages [2] -->
Quantitative Trading Decision Model

<!-- b000034 | prose | pages [2] -->
5

<!-- b000035 | prose | pages [2] -->
6

<!-- b000036 | prose | pages [2] -->
7

<!-- b000037 | prose | pages [2] -->
7

<!-- b000038 | prose | pages [2] -->
Price Prediction Model Based on LM-BP Neural Network 4.1 . . . . . . . . . . . . .

<!-- b000039 | prose | pages [2] -->
7

<!-- b000040 | prose | pages [2] -->
The Training Process of BP Neural Network . . . . . . . . . . . . . . . . . 4.1.1 8

<!-- b000041 | prose | pages [2] -->
Introduction to the Principle of LM Algorithm 4.1.2 . . . . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
10

<!-- b000043 | prose | pages [2] -->
Model Solution and Result Analysis . . . . . . . . . . . . . . . . . . . . . 4.1.3 11

<!-- b000044 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Recurrent Decision Model 13

<!-- b000045 | prose | pages [2] -->
Model Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 13

<!-- b000046 | prose | pages [2] -->
Modeling Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 13

<!-- b000047 | prose | pages [2] -->
Model Solving and Results Analysis 4.2.3

<!-- b000048 | prose | pages [2] -->
5

<!-- b000049 | heading | pages [2] -->
Prove the Model by Providing Evidence

<!-- b000050 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000051 | prose | pages [2] -->
15

<!-- b000052 | prose | pages [2] -->
16

<!-- b000053 | heading | pages [2] -->
The Eﬀect of Transaction Costs on Model Sensitivity

<!-- b000054 | prose | pages [2] -->
6

<!-- b000055 | prose | pages [2] -->
7

<!-- b000056 | heading | pages [2] -->
Evaluation of Strengths and Weaknesses

<!-- b000057 | prose | pages [2] -->
17

<!-- b000058 | prose | pages [2] -->
20

<!-- b000059 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 Strengths 20

<!-- b000060 | prose | pages [2] -->
Weaknesses and Further Improvements . . . . . . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000061 | prose | pages [2] -->
8

<!-- b000062 | heading | pages [2] -->
Memorandum to the Trader

<!-- b000063 | heading | pages [2] -->
Appendices

<!-- b000064 | prose | pages [2] -->
20

<!-- b000065 | prose | pages [2] -->
20

<!-- b000066 | prose | pages [2] -->
25

<!-- b000067 | furniture | pages [3] -->
Team # 2218931

<!-- b000068 | furniture | pages [3] -->
Page 3 of 25

<!-- b000069 | prose | pages [3] -->
1

<!-- b000070 | heading | pages [3] -->
Introduction

<!-- b000071 | prose | pages [3] -->
1.1 Problem Background

<!-- b000072 | prose | pages [3] -->
"Looking at the prices, I can see something we can study here, maybe a way to predict, mathemat- ically or statistically. So I built some models, and models got better and better. Finally, the modal replaced the fundamental stuﬀ."

<!-- b000073 | prose | pages [3] -->
—James Simons,the King of Quants

<!-- b000074 | prose | pages [3] -->
With the continuous development of deep learning and artiﬁcial intelligence, quantitative trading strategies have gradually become mature and accepted by traders.Quantitative trading has gradually emergedsince the 1970s. Sharpe’s Capital Asset Pricing Model and Ross’sArbitragePricing Theory have promoted its prosperity extensively. Although the impact of the ﬁnancial crisis has not been avoided and there are still model failures, quantitative investment is still necessary and practical. After all, the Medallion Fund operated by Simons has an average annual return of 35%!

<!-- b000075 | prose | pages [3] -->
Compared with traditional investment methods that rely on investment experience or analysis of ﬁnancial data, establishing a suitable forecasting model based on the historical price data of the investment object and quantifying the decision-making method of an eﬀective trading strategy can help traders make trading decisions more conveniently while obtaining higher returns.

<!-- b000076 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000077 | prose | pages [3] -->
Through in-depth analysis and research on the background of the problem, combined with topic- speciﬁc constraints and requirements given, the restate of the problem can be expressed as follows:

<!-- b000078 | prose | pages [3] -->
• Develop a Quantitative Trading Decision Model based on the historical price data of gold and bitcoin over the past ﬁve years, constrained by trading rules and providing the best daily trading strategy. Note that the model can only be built using the given price data on and before the trading day. That is, when making daily trading strategies, we do not know the future prices of gold and bitcoin.

<!-- b000079 | prose | pages [3] -->
• Beginning on September 11, 2016, traders used an initial capital of $1,000 to adjust the investment portfolio consisting of U.S. dollars, troy ounces, and bitcoins according to the decisions given by the Quantitative Trading Decision Model and calculate the investment income after a ﬁve-year trading period.

<!-- b000080 | prose | pages [3] -->
• Present evidence that the parameters in the established model are optimal, and the obtained strategy is the optimal strategy of the model. Prove that our strategy can achieve higher returns than other strategies.

<!-- b000081 | prose | pages [3] -->
• Considering the results obtained above, prepare one to two pages of memorandum to com- municate the model and strategy to the trader.

<!-- b000082 | furniture | pages [4] -->
Team # 2218931

<!-- b000083 | furniture | pages [4] -->
Page 4 of 25

<!-- b000084 | prose | pages [4] -->
1.3 Literature Review

<!-- b000085 | prose | pages [4] -->
In order to determine the best daily trading strategy, the prices of gold and Bitcoin can be predicted step by step and then combined with the existing investment portfolio strategies to determine the appropriate trading method and establish a quantitative trading decision-making model. The relevant research of the following scholars is for us Provides ideas:

<!-- b000086 | prose | pages [4] -->
• The price of gold has the characteristics of dynamic, nonlinear and time-varying.

<!-- b000087 | prose | pages [4] -->
The prediction of the gold price by traditional methods relies on the linear relationship between its prices, which has obvious limitations and low prediction accuracy. Zeng Lian et al. (2010) [1]and Zhang Jundong et al. (2010) [2]used an improved neural network model to achieve high-precision simulation of gold price forecasting. Lin Yu et al. (2010) [3] and Jing Zhigang and Shi Guoliang (2017) [4]adopted an improved ARIMA model, which has higher prediction accuracy than a single prediction model. In recent years, the price prediction model based on LSTM has attracted the attention of scholars. Yuan Dongfang (2021) [5] predicted the price of gold futures based on the CEEMDAN-PCA-LSTM model.

<!-- b000088 | prose | pages [4] -->
• Muzammal(2019) [6] found that bitcoin prices are highly volatile, and Wong’s(2014) [7] economic analysis shows that the returns are incredibly high. Katsiampa(2017), Selin(2020), Duan(2020) [8–10] forecast Bitcoin price and volatility using traditional time series fore- casting methods. Compared with traditional linear statistical models, artiﬁcial intelligence methods can better capture the high volatility of Bitcoin prices. Marendra(2018) [11] com- pared the ARIMA model with the LSTM deep learning model and found that the mean absolute error of the LSTM model was signiﬁcantly lower. Ciaian(2016) [12] further com- pared the deep learning model, the autoregressive ensemble model, and the ARIMA model and concluded that the deep learning model performed better in classiﬁcation prediction.

<!-- b000089 | prose | pages [4] -->
• Quantitative trading relies on computers to conﬁgure investment portfolios, which is more scientiﬁc and rational than traditional trading decisions.

<!-- b000090 | prose | pages [4] -->
Its quantitative models can be roughly divided into two categories.

<!-- b000091 | prose | pages [4] -->
One is the model based on statistical theory.

<!-- b000092 | prose | pages [4] -->
For example, Zhang Peng (2008) [13]studied the mean-variance and mean-VaR portfolio models when short selling is not allowed and veriﬁed the algorithm’s eﬀectiveness through empirical research. The other category relies on the development of artiﬁcial intelligence technology, such as trading algorithms based on deep reinforcement learning. Xiong Lidong (2019) [14] and Fan Xiaoyu (2021) [15] studied it. They found that the strategy does not rely on complex expert experience, nor does it need to make explicit predictions about the market environment, and can directly output trading strategies its eﬀectiveness.

<!-- b000093 | prose | pages [4] -->
To more intuitively reﬂect the research situation of scholars in the ﬁeld of quantitative trading, we draw Figure 1 based on the content of the literature review.

<!-- b000094 | furniture | pages [5] -->
Team # 2218931

<!-- b000095 | furniture | pages [5] -->
Page 5 of 25

<!-- b000096 | caption | pages [5] -->
Figure 1: Literature Review Framework of Model

<!-- b000097 | prose | pages [5] -->
1.4 Our Work

<!-- b000098 | prose | pages [5] -->
The problem requires building a quantitative trading decision model to achieve the best trading strategy. Our work mainly includes the following:

<!-- b000099 | prose | pages [5] -->
1) Based on the price data of gold and bitcoin, the LM-BP Neural Network Model is constructed. Use the model’s output of the predicted price to build a Recurrent Decision Model. The two constitute a Quantitative Trading Decision Model together, providing the best daily trading strategy.

<!-- b000100 | prose | pages [5] -->
2) We prove that our strategy is optimal by optimizing parameters and setting a control group.

<!-- b000101 | prose | pages [5] -->
3) Change the commission ratio for gold and bitcoin, and analyze the impact of transaction costs on strategies and results.

<!-- b000102 | prose | pages [5] -->
4) Wrote a memo for traders with our models, strategies and results.

<!-- b000103 | prose | pages [5] -->
In order to avoid complicated description, intuitively reﬂect our work process, the ﬂow chart is shown in Figure 2:

<!-- b000104 | furniture | pages [6] -->
Team # 2218931

<!-- b000105 | furniture | pages [6] -->
Page 6 of 25

<!-- b000106 | caption | pages [6] -->
Figure 2: Flow Chart of Our Work

<!-- b000107 | prose | pages [6] -->
2

<!-- b000108 | heading | pages [6] -->
Assumptions and Explanations

<!-- b000109 | prose | pages [6] -->
In reality, ﬁnancial markets operate in complex situations, we need to make reasonable assumptions to simplify the model, and each hypothesis is closely followed by its corresponding explanation:

<!-- b000110 | prose | pages [6] -->
• Assumption 1: The amount of funds traded is small enough not to aﬀect the behavior of other traders in the market and the price of ﬁnancial assets.

<!-- b000111 | prose | pages [6] -->
,→Explanation:Larger transaction capital volumes may impact market prices, resulting in transaction costs not necessarily proportional to transaction value.

<!-- b000112 | prose | pages [6] -->
• Assumption 2: Regardless of the price ﬂuctuations of gold and bitcoin on the day, the given data is used as the day’s trading price.

<!-- b000113 | prose | pages [6] -->
,→Explanation:The price of gold and bitcoin is volatile at diﬀerent times of the day, so their prices are not volatile. However, considering that the trading period is long and only a given daily historical price can be used, we make this assumption.

<!-- b000114 | prose | pages [6] -->
• Assumption 3:Traders can purchase any amount of Bitcoin and Gold according to the optimal allocation of funds, and the purchase amount can be a non-integer number.

<!-- b000115 | prose | pages [6] -->
,→Explanation:Traders rarely use all their funds to buy gold or bitcoin in reality, and the number of transactions is usually a whole number. In order to ﬁnd the optimal combination strategy, we allow exceptional cases to occur.

<!-- b000116 | prose | pages [6] -->
• Assumption 4:Only consider trading strategies where a short sale is not allowed.

<!-- b000117 | prose | pages [6] -->
,→Explanation:Allowing short sale increases the risk for traders and ﬁnancial markets, and our goal is to maximize returns with as little risk as possible.

<!-- b000118 | furniture | pages [7] -->
Team # 2218931

<!-- b000119 | furniture | pages [7] -->
Page 7 of 25

<!-- b000120 | prose | pages [7] -->
Additional assumptions are made to simplify analysis for individual sections. These assump- tions will be discussed at the appropriate locations.

<!-- b000121 | prose | pages [7] -->
3

<!-- b000122 | heading | pages [7] -->
Notations

<!-- b000123 | caption | pages [7] -->
Table 1 shows the necessary notations and signs used in this paper. Other notations and signs will

<!-- b000124 | prose | pages [7] -->
be declaired or deﬁned when using.

<!-- b000125 | caption | pages [7] -->
Table 1: Notions and Symbol Description

<!-- b000126 | prose | pages [7] -->
Symbols Description

<!-- b000127 | prose | pages [7] -->
Hj The hidden layer output of the neural network Ok The output of the output layer of the neural network Wij The weights from the input layer to the hidden layer Wjk The weights from the hidden layer to the output layer aj Thresholding in the hidden layer of a neural network f An assumed functional relation which maps a parameter vector t Assume buying gold or bitcoin on day t t′ Assume selling gold or bitcoin on day t′

<!-- b000128 | prose | pages [7] -->
α1,2 Short-term predicted price increase threshold for gold or bitcoin β1,2 Long-term predicted price increase threshold for gold or bitcoin

<!-- b000129 | prose | pages [7] -->
4

<!-- b000130 | heading | pages [7] -->
Quantitative Trading Decision Model

<!-- b000131 | prose | pages [7] -->
Traders decide the day’s portfolio investment strategy according to the prices of gold and bitcoin. In order to obtain the best investment returns, they need to have a reasonable and accurate estimate of the future price trends and ﬂuctuations of the two and then follow a certain trading strategy to make today’s investment decisions. Therefore, the Quantitative Trading Decision Model to be established include two steps: ﬁrst, construct a high-precision prediction model, and then quantitative modeling of the investment strategy is carried out, and ﬁnally, realize the purpose of automatic quantitative trading decision-making.

<!-- b000132 | prose | pages [7] -->
4.1

<!-- b000133 | heading | pages [7] -->
Price Prediction Model Based on LM-BP Neural Network

<!-- b000134 | prose | pages [7] -->
In recent years, due to the good nonlinear characteristics, ﬂexible and eﬀective learning methods, and strong anti-interference ability of the BP neural network, it has been widely used in forecasting research. We consider using neural network methods to predict their prices by combining the prediction models in the literature review and the dynamic, nonlinear, and volatility characteristics of gold and bitcoin prices.

<!-- b000135 | prose | pages [7] -->
When the traditional BP algorithm based on the standard gradient descent method solves practical problems, the quality of the solution is often aﬀected because the convergence speed is too slow. Therefore, many improved training algorithms based on nonlinear optimization have been proposed to improve the convergence speed of network training. The improved algorithms can be divided into two categories:

<!-- b000136 | furniture | pages [8] -->
Team # 2218931

<!-- b000137 | furniture | pages [8] -->
Page 8 of 25

<!-- b000138 | heading | pages [8] -->
• Improvement methods based on standard gradient descent. Including BP algorithm with

<!-- b000139 | prose | pages [8] -->
additional momentum, BP algorithm with variable learning rate, and elastic BP algorithm. Such improved algorithms are primarily applied to simple problems.

<!-- b000140 | heading | pages [8] -->
• Network training algorithms based on numerical optimization methods. Including quasi-

<!-- b000141 | prose | pages [8] -->
Newton method, Levenberg-Marquardt method (after this referred to as LM), and conjugate gradient method. Use the ﬁrst and second derivative information of the objective function at the same time. It is a better choice for complex practical problems.

<!-- b000142 | prose | pages [8] -->
Since the price trends of gold and bitcoin are complex and the amount of data is large, the numerical optimization method is more suitable for improving the BP neural network. Zhou Kaili and Kang Yaohong (2005) [16] designed a MATLAB simulation program. They found that the LM algorithm has the fastest convergence speed and higher computational accuracy for small and medium-sized neural networks. Given the advantages of the above LM algorithm, this section uses the LM-BP neural network algorithm to predict the price of gold and bitcoin.

<!-- b000143 | prose | pages [8] -->
4.1.1 The Training Process of BP Neural Network

<!-- b000144 | prose | pages [8] -->
The training process of the BP Neural Network consists of two parts: the forward propagation of the signal and the backpropagation of the error. The signal is passed from the neural network’s input layer, through the hidden layer, to the output layer, where the output signal and error signal are generated. If the error signal meets the requirements, the calculation ends; otherwise, the signal is transferred to backpropagation. The weights and thresholds are adjusted layer by layer, and the network parameters are updated through the gradient descent strategy. The training ﬂow chart of the LM-BP Neural Network is as follows.

<!-- b000145 | heading | pages [8] -->
1. Determining the Neural Network Structure. That is, determine the number of neural

<!-- b000146 | prose | pages [8] -->
network layers and the number of hidden nodes in each hidden layer. Usually, after many attempts, the value of n that makes the model prediction eﬀect optimal is obtained.

<!-- b000147 | heading | pages [8] -->
2. Initialize weights and thresholds. Initialize the weights between the input and hidden layers,

<!-- b000148 | prose | pages [8] -->
the threshold, and the learning rate between the hidden and output layers. Each connection weight and the threshold is usually assigned a random value in the interval (-1,1).

<!-- b000149 | heading | pages [8] -->
3. Forward propagation calculation. Through the forward propagation of the determined

<!-- b000150 | prose | pages [8] -->
network, calculate the hidden layer output Hj, the output layer output Ok:

<!-- b000151 | prose | pages [8] -->
n ∑

<!-- b000152 | prose | pages [8] -->
Hj = f(

<!-- b000153 | prose | pages [8] -->
Wij + aj), j = 1, 2, . . . , L (1)

<!-- b000154 | prose | pages [8] -->
i=1

<!-- b000155 | prose | pages [8] -->
n ∑

<!-- b000156 | prose | pages [8] -->
Ok =

<!-- b000157 | prose | pages [8] -->
WjkHj + bk, k = 1, 2, . . . , m (2)

<!-- b000158 | prose | pages [8] -->
i=1

<!-- b000159 | prose | pages [8] -->
Where Wij is the weight from the input layer to the hidden layer, aj is the hidden layer threshold, L is the number of hidden layer nodes, Wjk is the weight from the hidden layer to the output layer, bk is the output layer threshold.

<!-- b000160 | furniture | pages [9] -->
Team # 2218931

<!-- b000161 | furniture | pages [9] -->
Page 9 of 25

<!-- b000162 | caption | pages [9] -->
Figure 3: Algorithm ﬂow chart of LM-BP

<!-- b000163 | heading | pages [9] -->
4. Error calculation. The prediction error is the diﬀerence between the expected value Yk and

<!-- b000164 | prose | pages [9] -->
the predicted value.

<!-- b000165 | prose | pages [9] -->
ek = Yk −Ok, k = 1, 2, . . . , m (3)

<!-- b000166 | heading | pages [9] -->
5. Weight update. The weights in the established neural network are updated and adjusted

<!-- b000167 | prose | pages [9] -->
according to the calculated prediction error ek. The calculation formula is as follows, η is the learning rate constant.

<!-- b000168 | prose | pages [9] -->
m ∑

<!-- b000169 | prose | pages [9] -->
Wij = Wij + ηHj((1 −Hj)xi

<!-- b000170 | prose | pages [9] -->
k=1

<!-- b000171 | prose | pages [9] -->
Wjk = Wjk + ηHjek

<!-- b000172 | prose | pages [9] -->
Wjkek) i = 1, 2, . . . , n; j = 1, 2, . . . , L (4)

<!-- b000173 | prose | pages [9] -->
j = 1, 2, . . . , L; k = 1, 2, . . . , m (5)

<!-- b000174 | heading | pages [9] -->
6. Threshold update. Update the thresholds aj, bk according to the prediction error ek:

<!-- b000175 | prose | pages [9] -->
∑

<!-- b000176 | prose | pages [9] -->
aj = aj + ηHj(

<!-- b000177 | prose | pages [9] -->
k=1

<!-- b000178 | prose | pages [9] -->
m m

<!-- b000179 | prose | pages [9] -->
Wjkek), bk = bk + ηek (6)

<!-- b000180 | heading | pages [9] -->
7. Iteration stop condition. Iteratively update the parameters until the minimum mean square

<!-- b000181 | prose | pages [9] -->
error is less than the set value, the iteration terminates, and the BP Neural Network training ends.

<!-- b000182 | furniture | pages [10] -->
Team # 2218931

<!-- b000183 | furniture | pages [10] -->
Page 10 of 25

<!-- b000184 | prose | pages [10] -->
4.1.2

<!-- b000185 | heading | pages [10] -->
Introduction to the Principle of LM Algorithm

<!-- b000186 | prose | pages [10] -->
When BP neural network predicts Bitcoin price, there is a phenomenon of "overﬁtting," and the gradient descent algorithm will also make it fall into a local optimum. The convergence speed is also slow. In order to improve the price prediction eﬀect of gold and bitcoin, this paper uses the Levenberg-Marquardt algorithm to improve. This section mainly introduces the principle of the LM algorithm.

<!-- b000187 | prose | pages [10] -->
LM can be thought of as a combination of steepest descent and the Gauss-Newton method. The algorithm behaves like a steepest descent method: slow but guaranteed to converge when the current solution is far from the correct one. When the current solution is close to the correct solution, it becomes a Gauss-Newton method.

<!-- b000188 | prose | pages [10] -->
Since the establishment of the subsequent LM-BP Neural Network mainly relies on implement- ing the LM algorithm in the MATLAB toolbox, we will not introduce too much mathematical knowledge involved in the algorithm. Nevertheless, to help readers understand the algorithm prin- ciple of LM more intuitively, combined with the research of K. Madsen et al. (2004) [17], we try to give the pseudo-code of the LM algorithm as follows.

<!-- b000189 | heading | pages [10] -->
Algorithm 1: Levenberg-Marquardt method

<!-- b000190 | prose | pages [10] -->
Input: Historical prices for gold, bitcoin Output: Predicted prices for gold, bitcoin

<!-- b000191 | heading | pages [10] -->
1 begin

<!-- b000192 | prose | pages [10] -->
k:=0;

<!-- b000193 | prose | pages [10] -->
ν:=2;

<!-- b000194 | prose | pages [10] -->
x:=x0 2

<!-- b000195 | prose | pages [10] -->
A:= J(x)TJ(x);

<!-- b000196 | prose | pages [10] -->
g:= J(x)Tf(x) 3

<!-- b000197 | prose | pages [10] -->
found:=(∥g∥∞≤ε1);

<!-- b000198 | prose | pages [10] -->
µ:=τ*max{aii} 4

<!-- b000199 | prose | pages [10] -->
found) and (k < kmax) do while (not 5

<!-- b000200 | prose | pages [10] -->
Solve(A + µI)h1m = −g k := k + 1; 6

<!-- b000201 | prose | pages [10] -->
if ∥h1m∥≤ε2(∥x∥+ ε2) then 7

<!-- b000202 | prose | pages [10] -->
found:=true 8

<!-- b000203 | prose | pages [10] -->
else 9

<!-- b000204 | prose | pages [10] -->
xnew :=x+ϱ 10

<!-- b000205 | prose | pages [10] -->
ϱ := (F(x) −F(xnew))/(L(0) −L(h1m)) 11

<!-- b000206 | prose | pages [10] -->
if ϱ > 0(step acceptable) then 12

<!-- b000207 | prose | pages [10] -->
x:=xnew 13

<!-- b000208 | prose | pages [10] -->
A:= J(x)TJ(x);

<!-- b000209 | prose | pages [10] -->
g:= J(x)Tf(x) 14

<!-- b000210 | prose | pages [10] -->
found:=(∥g∥∞≤ε1) 15

<!-- b000211 | prose | pages [10] -->
µ := µ ∗max{1

<!-- b000212 | prose | pages [10] -->
3, 1 −(2ϱ −1)3};

<!-- b000213 | prose | pages [10] -->
ν := 2

<!-- b000214 | prose | pages [10] -->
16

<!-- b000215 | prose | pages [10] -->
else 17

<!-- b000216 | prose | pages [10] -->
µ := µ ∗ν;

<!-- b000217 | prose | pages [10] -->
ν := 2 ∗ν 18

<!-- b000218 | prose | pages [10] -->
end 19

<!-- b000219 | prose | pages [10] -->
end 20

<!-- b000220 | heading | pages [10] -->
21 end

<!-- b000221 | prose | pages [10] -->
In the above algorithm ,f is an assumed functional relation which maps a parameter vector p ∈Rm to an estimated measurement vector xnew = f(p), xnew ∈Rn. The basis of the LM

<!-- b000222 | furniture | pages [11] -->
Team # 2218931

<!-- b000223 | furniture | pages [11] -->
Page 11 of 25

<!-- b000224 | prose | pages [11] -->
algorithm is a linear approximation to f in the neighborhood of p, and ﬁnd a small∥δp∥,where ε = x −xnew. J is the Jacobian matrix ∂f(p)

<!-- b000225 | prose | pages [11] -->
and contains the ﬁrst derivative of the network ∂p performance index to the weight and threshold. µ is referred to as the damping term. And A represents Hessian matrix,g means gradient. Among them, the error vector ν is composed of the elements of the error matrix arranged in a certain sequence.

<!-- b000226 | prose | pages [11] -->
4.1.3

<!-- b000227 | heading | pages [11] -->
Model Solution and Result Analysis

<!-- b000228 | prose | pages [11] -->
When building the model, the Trainlm function in the MATLAB toolbox is used to realize the price prediction of gold and Bitcoin based on the LM-BP neural network. We only need to set the model’s parameters and test the model’s prediction eﬀect—parameter settings.

<!-- b000229 | prose | pages [11] -->
Parameter settings. To satisfy our decision-making needs, we need to make long-term and short-term forecasts for the prices of gold and Bitcoin, respectively. The input data for both are 7-day historical price data, and the short-term forecast output for both is the forecast price for the next day. Taking into account the diﬀerence in trading time between the two, the long-term forecast output of gold is the forecast price for the next ﬁve days, and Bitcoin is seven days. The ﬁgure below shows the topology of Bitcoin’s short-term prediction model.

<!-- b000230 | caption | pages [11] -->
Figure 4: Bitcoin’s short-term prediction model

<!-- b000231 | prose | pages [11] -->
In order to avoid overﬁtting, the sample data is randomly divided for training, and the ratio of training, testing, and validation data is 70:15:15. For gold price prediction, set its hidden layer parameter to 10. For Bitcoin price prediction, set its hidden layer parameter to 16. Use mean square error to measure network performance. When the number of training times reaches 1000, the iteration stops.

<!-- b000232 | prose | pages [11] -->
Test of LM-BP Neural Network Prediction Model. The ﬁtting accuracy of the LM-BP neural network prediction model for gold prices can be generated using Matlab as ﬁgure 5.

<!-- b000233 | prose | pages [11] -->
The ﬁgure 5 shows that the R2 of the training set, test set, validation set, and the whole is more than 0.99. The same conclusion can be drawn by looking at the ﬁtted accuracy plot for Bitcoin. The predictions of the model we built worked well.

<!-- b000234 | prose | pages [11] -->
In order to make the readers feel the prediction accuracy of the model more intuitively, we compared the actual and predicted prices of gold and bitcoin and drew the line chart as shown below. It can be seen that the predicted price curve and the actual price curve almost wholly overlap, once again proving the validity and reliability of our prediction model, which lays a foundation for further trading decisions.

<!-- b000235 | furniture | pages [12] -->
Team # 2218931

<!-- b000236 | furniture | pages [12] -->
Page 12 of 25

<!-- b000237 | caption | pages [12] -->
Figure 5: Fit Accuracy Plot for Gold

<!-- b000238 | prose | pages [12] -->
(a) gold (b) bitcoin

<!-- b000239 | caption | pages [12] -->
Figure 6: Predicted price and actual price comparison chart

<!-- b000240 | furniture | pages [13] -->
Team # 2218931

<!-- b000241 | furniture | pages [13] -->
Page 13 of 25

<!-- b000242 | prose | pages [13] -->
4.2

<!-- b000243 | heading | pages [13] -->
Recurrent Decision Model

<!-- b000244 | prose | pages [13] -->
4.2.1

<!-- b000245 | heading | pages [13] -->
Model Description

<!-- b000246 | prose | pages [13] -->
In the literature review section, we summarize the commonly used portfolio investment decision- making, models. Models based on statistical theory pay more attention to the relationship between various factors that aﬀect prices and have good interpretability. A model that relies on artiﬁcial intelligence technology is similar to a "black box." We only need to input relevant data to output the corresponding decision. The latter usually works better but can also "overﬁt." However, the preconditions of this study are diﬀerent. We can only build the model based on gold and Bitcoin’s historical price data ﬂow. The input is too single, and the degree of adaptation to the above models is not high. Therefore, we consider self-built models rather than improved models.

<!-- b000247 | prose | pages [13] -->
The idea of building a decision-making model is to determine a speciﬁc trading strategy and implement it with an algorithm. Since we can only make decisions based on historical prices, and to avoid situations where the strategy is too complicated to be realized, we use the simplest "buy low and sell high based on trend forecast" strategy to build the model.

<!-- b000248 | prose | pages [13] -->
On each trading day, we can know the price of gold and bitcoin on that day, so we need to consider the latest data of the day when predicting future price changes, which means that every time we make a decision, we need to update the prediction results and make decisions based on this, so we name the model a Recurrent Decision Model.

<!-- b000249 | prose | pages [13] -->
4.2.2

<!-- b000250 | heading | pages [13] -->
Modeling Process

<!-- b000251 | prose | pages [13] -->
Please assume that the investment portfolio of cash, gold, and bitcoin is [C, G, B], and its initial state is [1000, 0, 0] from the meaning of the question. The establishment of the model consists of the following four stages:

<!-- b000252 | prose | pages [13] -->
⋆"Stand by" stage.

<!-- b000253 | prose | pages [13] -->
This stage mainly accumulates historical data required for forecasting and does not make decisions. Our decision model relies on forecasting future prices, inputting seven days of historical data into the LM-BP neural network forecasting model for short-term forecasts (both next day’s prices) and long-term forecasts. Since gold and bitcoin have diﬀerent trading rules, the long-term forecast for gold is ﬁve days in the future, while bitcoin is seven days. The decision-making model comes into play when both gold and bitcoin have accumulated seven-day valid historical price data, as shown in the following diagram.

<!-- b000254 | prose | pages [13] -->
⋆Buying stage.

<!-- b000255 | prose | pages [13] -->
At this stage, we need to consider two issues: when to buy and how to determine the buy share.

<!-- b000256 | prose | pages [13] -->
Buying Conditions (Assume Buying on Day t) .Gold buying conditions: predict that the price increase ratio on the t + 1 day is greater than 2% or the increase ratio in the next ﬁve days is greater than 3%. Bitcoin buying conditions: predict that the price increase ratio on the t + 1 day is greater than 3.5% or the increase ratio in the next ﬁve days is greater than 4.5%.

<!-- b000257 | prose | pages [13] -->
Calculate the Sharpe ratio.In actual investment, we should try our best to reduce investment risk in the pursuit of maximum return. For this, we introduce the concept of the Sharpe ratio. The

<!-- b000258 | furniture | pages [14] -->
Team # 2218931

<!-- b000259 | furniture | pages [14] -->
Page 14 of 25

<!-- b000260 | caption | pages [14] -->
Figure 7: "Stand by" stage

<!-- b000261 | prose | pages [14] -->
Sharpe ratio is used to calculate how much excess return a portfolio generates per unit of total risk exposure. The Sharpe ratio for gold and Bitcoin is calculated as follows.

<!-- b000262 | prose | pages [14] -->
expected rate of return Sharpe ratio = (7) std of gold or bitcoin over the past seven days

<!-- b000263 | prose | pages [14] -->
Among them, the expected rate of return takes the larger of the short-term rate of return or half of the long-term rate of return ( because the risk of long-term holdings is higher). If the Sharpe ratio is greater than 1, it means that the return on our investment is higher than the risk of volatility; if it is less than 1, the opposite is true. We calculate the Sharpe ratio for each portfolio. The higher the value, the better the portfolio.

<!-- b000264 | prose | pages [14] -->
Shares are determined based on the Sharpe ratio. There are two situations we need to consider :

<!-- b000265 | prose | pages [14] -->
• Buy gold and bitcoin at the same time for the day.Calculating and normalizing the Sharpe ratios for gold and Bitcoin separately will yield two buy ratios. Put all the cash be held into the purchase according to the purchase ratio, and the state of the investment portfolio at this time is[0, 0.99p1 ∗Ct−1 + Gt−1, 0.98p2 ∗Ct−1 + Bt−1]. Among them, p represents the purchase ratio, and Gt−1 represents the amount of gold held yesterday,and Bt−1 has a similar meaning. Ct−1 represents the amount of gold or bitcoin that can be bought today with cash held yesterday. After the purchase, the asset value of the account is updated based on the actual price of gold and bitcoin on the day.

<!-- b000266 | prose | pages [14] -->
• Only one investment product meets the purchase requirements. If the Sharpe ratio of the product on that day is greater than 1, all existing cash will be used to purchase the product; if it is less than 1, the product will be purchased according to the corresponding Sharpe ratio share of the cash.

<!-- b000267 | prose | pages [14] -->
If they buy gold, the state of the portfolio at this time is:[0, 0.99 ∗Ct−1 + Gt−1, Bt−1] or [Ct−1 ∗(1 −Sharpe Ratio), 0.99 ∗Sharpe Ratio ∗Ct−1 + Gt−1, Bt−1].

<!-- b000268 | prose | pages [14] -->
If they buy bitcoin, the state of the portfolio at this time is:[0, Gt−1, 0.98 ∗Ct−1 + Bt−1] or [Ct−1 ∗(1 −Sharpe Ratio), Gt−1, 0.98 ∗Ct−1 ∗Sharpe Ratio + Bt−1]. Asset value needs to be updated after purchase.

<!-- b000269 | furniture | pages [15] -->
Team # 2218931

<!-- b000270 | furniture | pages [15] -->
Page 15 of 25

<!-- b000271 | prose | pages [15] -->
⋆Holding stage.

<!-- b000272 | prose | pages [15] -->
When no cash is held, buying operations are not considered.

<!-- b000273 | prose | pages [15] -->
Only selling operations are considered. Note that even if no buying and selling operations are performed, the asset value must be updated.

<!-- b000274 | prose | pages [15] -->
⋆Selling stage. (Assume sell on t′ day)

<!-- b000275 | prose | pages [15] -->
Sell it when we predict a fall in the price of gold or bitcoin on day t′ +1, and the long-term price forecast is trending down. The changes in its investment portfolio are similar to the buying stage, so we will not go into details here. The asset value needs to be updated after the sell operation.

<!-- b000276 | prose | pages [15] -->
4.2.3

<!-- b000277 | heading | pages [15] -->
Model Solving and Results Analysis

<!-- b000278 | prose | pages [15] -->
We designed our own algorithm to solve the self-built Recurrent Decision Model. The pseudocode is as follows:

<!-- b000279 | heading | pages [15] -->
Algorithm 2: Algorithm Principle of Recurrent Decision Model

<!-- b000280 | prose | pages [15] -->
Input: Initial state for cash,gold, bitcoin Output: Predicted prices for cash,gold, bitcoin

<!-- b000281 | heading | pages [15] -->
1 for day=1 to Ttotal do

<!-- b000282 | prose | pages [15] -->
Gold’s short-term uptrend based on short-term forecast gold and today gold 2

<!-- b000283 | prose | pages [15] -->
Gold’s long-term uptrend based on long-term forecast gold and today gold 3

<!-- b000284 | prose | pages [15] -->
if gold’s short-term uptrend ≥0.02 and gold’s long-term uptrend ≥0.03 then 4

<!-- b000285 | prose | pages [15] -->
Sharpe Ratio of gold based on max(Short-term upside values, long-term upside 5

<!-- b000286 | prose | pages [15] -->
values/2)/std(gold value for the last 5 days

<!-- b000287 | prose | pages [15] -->
end 6

<!-- b000288 | prose | pages [15] -->
BTC’s short-term uptrend based on short-term forecast BTC and today BTC 7

<!-- b000289 | prose | pages [15] -->
BTC’s long-term uptrend based on long-term forecast BTC and today BTC if BTC’s 8

<!-- b000290 | prose | pages [15] -->
short-term uptrend ≥0.035and BTC’s long-term uptrend ≥0.045 then

<!-- b000291 | prose | pages [15] -->
Sharpe Ratio of BTC based on max(Short-term upside values, long-term upside 9

<!-- b000292 | prose | pages [15] -->
values/2)/std(BTC value for the last 7 days

<!-- b000293 | prose | pages [15] -->
end 10

<!-- b000294 | prose | pages [15] -->
if Income̸ = 0 and (Sharpe Ratio of Gold > 0 or Sharpe Ratio of BTC > 0) then 11

<!-- b000295 | prose | pages [15] -->
normalization(Sharpe Ratio of Gold, Sharpe Ratio of BTC) 12

<!-- b000296 | prose | pages [15] -->
Sell gold, BTC at the Sharpe ratio 13

<!-- b000297 | prose | pages [15] -->
end 14

<!-- b000298 | prose | pages [15] -->
if predicted gold is down or predicted BTC is down then 15

<!-- b000299 | prose | pages [15] -->
Buy gold, BTC; 16

<!-- b000300 | prose | pages [15] -->
end 17

<!-- b000301 | heading | pages [15] -->
18 end

<!-- b000302 | prose | pages [15] -->
Substitute and solve the predicted price according to the above algorithm, and the following conclusions can be drawn: If starting from September 11, 2016, the portfolio investment is carried out according to our quantitative trading decision-making model, then on September 10, 2021, the initial investment of $1,000 will be the value is $270836.

<!-- b000303 | furniture | pages [16] -->
Team # 2218931

<!-- b000304 | furniture | pages [16] -->
Page 16 of 25

<!-- b000305 | prose | pages [16] -->
5

<!-- b000306 | heading | pages [16] -->
Prove the Model by Providing Evidence

<!-- b000307 | prose | pages [16] -->
This section will present evidence that our model provides the best strategy.

<!-- b000308 | prose | pages [16] -->
⋆Verify that the current model parameters are optimal.

<!-- b000309 | prose | pages [16] -->
For a speciﬁc model, we get the optimal result only when each parameter takes the optimal value. When establishing the circular decision-making model, we determined the minimum increase in buying investment products based on the given transaction costs and ﬁnancial asset trading experience. In order to prove that the parameters we set are optimal values, parameter optimization is performed.

<!-- b000310 | prose | pages [16] -->
Let the short-term growth rate threshold of gold is α1, and the long-term growth rate threshold is β1; the short-term growth rate threshold of Bitcoin is α2, and the long-term growth rate threshold is β1.

<!-- b000311 | prose | pages [16] -->
Combined with the known information of the topic and the actual situation, the value range of α1 is [2,2.5,3,3.5], and the value range of β1 is [3,3.5,4,4.5,5].α2 should be in [3.5,4 ,4.5,5,5.5,6], and β2 is in [4.5,5,5.5,6,6.5,7,7.5]. We will optimize the parameters with the ultimate goal of maximum proﬁt.Comparing the investment values corresponding to diﬀerent parameters, we determined the optimal value of α1, β1, α2 and β2 are: 2,3,3.5 and 4.5. This result is consistent with the parameters set by our model.

<!-- b000312 | prose | pages [16] -->
The current model has made the optimal strategy only from the model’s perspective.

<!-- b000313 | prose | pages [16] -->
⋆Compared to other strategies, our strategy achieved the highest returns.

<!-- b000314 | prose | pages [16] -->
To validate the eﬀect of this model, we decided to use a control group for illustration. Consider long-term trading, short-term trading strategies, and compare the returns of investment companies. We set up the following ﬁve control groups and calculated end-of-period asset values. For simple designs, we omit the calculation process.

<!-- b000315 | prose | pages [16] -->
• Control Group 1: At the beginning of the period, September 12, 2016, invest all cash in gold until the end, when the total assets were $1341.276.

<!-- b000316 | prose | pages [16] -->
• Control Group 2: All cash was invested in Bitcoin at the beginning of the period on September 11, 2016, until the end of the period, when the total assets were $73,097.98.

<!-- b000317 | prose | pages [16] -->
• Control Group 3: Investing half of the cash in Bitcoin on September 11, 2016, and the other half was invested in gold on September 12, 2016, until the end of the period, when the total assets were $37,219.593.

<!-- b000318 | prose | pages [16] -->
• Control Group 4:The average annual proﬁt rate of international investment companies has reached 30%, which is outstanding. We assume that the original assets are also expanding at an average annual rate of 30%. After ﬁve years, the assets will reach $3712.93.

<!-- b000319 | prose | pages [16] -->
• Control Group 5: Buy Bitcoin with all their funds and conduct short-term trading activities. To better construct the control group, we propose a simple Bitcoin market index, a variation of the BBI index. MA stands for the daily moving average. We deﬁne the bitcoin market index as BBIbiction = (MA3 + MA6 + MA12)/3,MA3 indicates the 3-day average price,

<!-- b000320 | furniture | pages [17] -->
Team # 2218931

<!-- b000321 | furniture | pages [17] -->
Page 17 of 25

<!-- b000322 | prose | pages [17] -->
if the bitcoin price is lower than the index, the market is not sluggish. We precisely deﬁne a strategy to buy when the price of bitcoin is above the index for three consecutive days and sell when the price of bitcoin is below the index for three consecutive days. A total of 73 buying operations (72 selling operations) occurred under this strategy in ﬁve years, and the assets at the end of the period were $3117.2.

<!-- b000323 | prose | pages [17] -->
Sort our strategies and the asset values of each control group in reverse order and make the following table.

<!-- b000324 | caption | pages [17] -->
Table 2: Asset Value Comparison of Diﬀerent Strategies

<!-- b000325 | prose | pages [17] -->
Classiﬁcation Strategy

<!-- b000326 | prose | pages [17] -->
Quantitative Trading our model Long-Term Trading Control Group 2 Long-Term Trading Control Group 3 Actual Trading Control Group 4 Short-term trading Control Group 5 Long-Term Trading Control Group 1

<!-- b000327 | prose | pages [17] -->
The data in the table gives us some insights:

<!-- b000328 | prose | pages [17] -->
Asset Value ($) Ranking

<!-- b000329 | prose | pages [17] -->
270836.00 1 73097.98 2 37219.59 3 3712.93 4 3117.20 5 1341.28 6

<!-- b000330 | prose | pages [17] -->
1) Our strategy ranked ﬁrst among several control groups, and the asset value was much higher than the other strategies, indicating that the best strategy was given.

<!-- b000331 | prose | pages [17] -->
2) Control group 2 is the control group with the highest assets. The price of Bitcoin has risen rapidly in these ﬁve years, so the portfolio assets with Bitcoin assets have grown quite rapidly. However, the growth rate of gold is slightly slower due to its properties, such as value preservation. It can be found that the growth rate of investment portfolios containing only gold assets is not excellent.

<!-- b000332 | prose | pages [17] -->
3) In addition, control group 5 ranks relatively poorly due to trading on only one index, incomplete information, and signiﬁcant volatility in the Bitcoin market. At the same time, too many transactions will lead to a signiﬁcant increase in transaction costs, which will aﬀect the income. At the same time, this strategy only considers the past proﬁt and loss situation. It does not predict the future according to the current situation, resulting in the trading eﬀect of this strategy being lower than the long-term trading eﬀect.

<!-- b000333 | heading | pages [17] -->
The Eﬀect of Transaction Costs on Model Sensitivity

<!-- b000334 | prose | pages [17] -->
6

<!-- b000335 | prose | pages [17] -->
In this article, transaction costs are mainly represented as commission costs when conducting buy and sell operations because there is no additional cost to hold assets. The total commission cost is closely related to the number of transactions and the percentage of commission paid per transaction. Just imagine, in the same transaction, the change in the commission payment ratio will aﬀect the transaction cost, which will impact the total assets we hold in the end.To explore how sensitive the implementation strategy of this paper is to transaction costs, we decide to adjust the commission payment ratio and observe changes in total assets.

<!-- b000336 | furniture | pages [18] -->
Team # 2218931

<!-- b000337 | furniture | pages [18] -->
Page 18 of 25

<!-- b000338 | prose | pages [18] -->
⋆The eﬀect of transaction costs on assets.

<!-- b000339 | prose | pages [18] -->
Fixed strategy, only changing the commission payment ratio of Bitcoin and gold observing the impact of changes in transaction costs on total assets.When ﬁxing the strategy, we need to consider three cases: only changing the commission ratio of gold, only changing the commission ratio of Bitcoin, and changing both simultaneously. We used MATLAB to draw a graph of the change in total assets with transaction costs when the strategy is ﬁxed as follows:

<!-- b000340 | caption | pages [18] -->
Figure 8: Fixed strategy, the impact of transaction costs on assets

<!-- b000341 | prose | pages [18] -->
From ﬁgure 8, it can be seen that:

<!-- b000342 | prose | pages [18] -->
• When the gold commission ratio remains the same and the bitcoin commission payment ratio changes, the asset changes are pretty obvious. As the commission ratio increases, total assets decrease accordingly.

<!-- b000343 | prose | pages [18] -->
• When the Bitcoin commission ratio remains the same and the gold commission payment ratio changes, there is almost no change in assets. For example, when the gold commission payment ratio is adjusted to 26%, the optimal asset obtained by the decision-making model is still $270,836. This shows that in this trading strategy, the main trading object is Bitcoin. Bitcoin is quite sensitive to changes in transaction costs, while gold is insensitive to changes in transaction costs due to too little transaction volume.

<!-- b000344 | prose | pages [18] -->
• The optimal strategy model under the speciﬁed commission ratio, the asset change obtained by only adjusting the commission ratio shows a linear relationship with the commission payment ratio.

<!-- b000345 | prose | pages [18] -->
• The model is susceptible to changes in the proportion of Bitcoin commissions but not sensitive to changes in the proportion of gold trading commissions.

<!-- b000346 | furniture | pages [19] -->
Team # 2218931

<!-- b000347 | furniture | pages [19] -->
Page 19 of 25

<!-- b000348 | prose | pages [19] -->
⋆The impact of transaction costs on strategy.

<!-- b000349 | prose | pages [19] -->
Considering the role of transaction costs in the model, the optimal strategy corresponding to diﬀerent commission ratios will also change when transaction costs change.

<!-- b000350 | prose | pages [19] -->
We further adjusted the model to explore the impact of changes in transaction costs on strategies. Most adjustments are made to the buying criteria for gold and Bitcoin. The goal of the transaction is to maximize the asset, which means that we want the beneﬁts of the transaction to exceed the cost. Therefore, we hope that after buying gold or bitcoin, the income obtained exceeds the commission cost of the transaction.

<!-- b000351 | prose | pages [19] -->
We improved the asset’s buying criteria to a short-term expected return of more than 1 − (1 −Commission payment ratio)2.

<!-- b000352 | prose | pages [19] -->
The uncertainty of long-term expected rate of return is greater than that of short-term expected rate of return, so the buying standard of long-term expected rate of return is set as the long-term expected rate of return exceeding 1 −(1 − Commission payment ratio)2 + 0.01. We have plotted the relationship between transaction costs and assets when the strategy changes with transaction costs.

<!-- b000353 | caption | pages [19] -->
Figure 9: Strategies vary with transaction costs , the impact of transaction costs on assets

<!-- b000354 | prose | pages [19] -->
From ﬁgure 9, it can be seen that:

<!-- b000355 | prose | pages [19] -->
• Gold remains insensitive to transaction costs.

<!-- b000356 | prose | pages [19] -->
• When the Bitcoin commission payment ratio is higher than 5%, the eﬀect is not apparent; when it is less than 5%, the strategy is highly sensitive to transaction costs. It is expected that the assets will change drastically. Therefore, at this time, the ﬁnal asset data under the required commission payment ratio has changed to a certain extent compared with the previous strategy.

<!-- b000357 | furniture | pages [20] -->
Team # 2218931

<!-- b000358 | furniture | pages [20] -->
Page 20 of 25

<!-- b000359 | prose | pages [20] -->
After the above analysis, we can ﬁnd that both the trading strategy and the trading results are highly sensitive to the change of the Bitcoin commission payment ratio, and less sensitive to the change of the gold commission payment ratio.

<!-- b000360 | prose | pages [20] -->
7

<!-- b000361 | heading | pages [20] -->
Evaluation of Strengths and Weaknesses

<!-- b000362 | prose | pages [20] -->
7.1

<!-- b000363 | heading | pages [20] -->
Strengths

<!-- b000364 | prose | pages [20] -->
Our model oﬀers the following strengths:

<!-- b000365 | prose | pages [20] -->
• We use the LM-BP Neural Network Model. Compared with other models such as the arima model and the gray prediction model, the model has higher prediction accuracy and can better ﬁt the data and carry out prediction work. At the same time, we construct a short-term prediction model and a long-term prediction model for gold and Bitcoin respectively.

<!-- b000366 | prose | pages [20] -->
• When constructing a decision model, using both our short-term forecast data and long-term forecast data for decision-making work, the model is more reliable than using one type of data alone.

<!-- b000367 | prose | pages [20] -->
• The optimal strategy should consider the maximization of assets and the risks we face when making decisions. In the decision model, we use the Sharpe ratio to divide the purchase share of gold and Bitcoin, considering the risks at diﬀerent proﬁt rate levels colossal diﬀerences. This approach makes the model more relevant to actual market performance and trading operations.

<!-- b000368 | prose | pages [20] -->
7.2

<!-- b000369 | heading | pages [20] -->
Weaknesses and Further Improvements

<!-- b000370 | prose | pages [20] -->
Our model has the following limitations and related improvements:

<!-- b000371 | prose | pages [20] -->
• The decision model we constructed is a greedy algorithm, and the result achieved may not be a globally optimal solution but a locally optimal solution.

<!-- b000372 | prose | pages [20] -->
• The weight of assets is too concentrated. In the simulated transaction, the main assets traded are bitcoins, and the number of gold transactions is small. The constructed model reﬂects trend timing thinking and reﬂects the market a little slower.

<!-- b000373 | prose | pages [20] -->
• Due to time constraints, the core strategy of the Recurrent Decision Model we established is relatively simple. Considering the complexity of the ﬁnancial market, we can try to establish a decision-making model based on reinforcement learning strategies in the future.

<!-- b000374 | prose | pages [20] -->
8

<!-- b000375 | heading | pages [20] -->
Memorandum to the Trader

<!-- b000376 | furniture | pages [21] -->
Team # 2218931

<!-- b000377 | furniture | pages [21] -->
Page 21 of 25

<!-- b000378 | heading | pages [21] -->
MEMORANDUM

<!-- b000379 | prose | pages [21] -->
To: The Trader

<!-- b000380 | prose | pages [21] -->
From: MCM Team #2218931

<!-- b000381 | heading | pages [21] -->
Subject: Quantitative Trading Decision Model and Investment Strategy

<!-- b000382 | prose | pages [21] -->
Date: February 21, 2022

<!-- b000383 | prose | pages [21] -->
Dear trader,

<!-- b000384 | prose | pages [21] -->
We are honored to inform you that we have built a quantitative trading decision model based only on historical price data and tried to give the best trading strategy. Our model, investment strategy and results are described below.

<!-- b000385 | heading | pages [21] -->
The Model

<!-- b000386 | prose | pages [21] -->
At your request, we have developed Quantitative Trading Decision Models that help you determine whether you should buy, hold or sell assets in your portfolio daily.

<!-- b000387 | prose | pages [21] -->
Construction idea 

<!-- b000388 | prose | pages [21] -->
Take historical price data as input. 

<!-- b000389 | prose | pages [21] -->
Build a prediction model to predict investment products' short-term and long-term price  conditions.

<!-- b000390 | prose | pages [21] -->
Determine the investment decision of the day according to a certain strategy.  LM-BP Neural Network Model  Reliable forecast results are the basis for good investment decisions. It is necessary to build a model with a good prediction effect. The prices of gold and bitcoin are dynamic and volatile and are suitable for prediction by neural network methods. The classic BP neural network uses the gradient descent method to find the optimal value, which often affects the quality of the solution due to the slow convergence speed. Therefore, we established a numerical optimization-based LM-BP Neural

<!-- b000391 | prose | pages [21] -->
Network Model. We tested the model with historical price data, and its predictions worked well.

<!-- b000392 | prose | pages [21] -->
Recurrent Decision Model  R exceeded 0.99, and the 2

<!-- b000393 | prose | pages [21] -->
The core idea of the decision model is to make decisions based on the future price trend of investment products. If there is an uptrend in the short or long term and the threshold is reached, buy it, otherwise sell it. We set a threshold related to transaction costs that determine whether to buy or not. We use the Sharpe ratio to measure the riskiness of a portfolio and use it to determine the purchase share of each product in the portfolio.

<!-- b000394 | heading | pages [21] -->
Quantitative Trading Decision Model

<!-- b000395 | prose | pages [21] -->
Long and short

<!-- b000396 | prose | pages [21] -->
Historical

<!-- b000397 | prose | pages [21] -->
term forecast

<!-- b000398 | prose | pages [21] -->
Price Data

<!-- b000399 | prose | pages [21] -->
LM-BP Neural Network Model

<!-- b000400 | prose | pages [21] -->
input

<!-- b000401 | prose | pages [21] -->
Output

<!-- b000402 | prose | pages [21] -->
Recurrent

<!-- b000403 | prose | pages [21] -->
Best

<!-- b000404 | prose | pages [21] -->
Decision Model

<!-- b000405 | prose | pages [21] -->
Strategy

<!-- b000406 | prose | pages [21] -->
Schematic diagram of quantitative trading decision model

<!-- b000407 | furniture | pages [22] -->
Team # 2218931

<!-- b000408 | furniture | pages [22] -->
Page 22 of 25

<!-- b000409 | prose | pages [22] -->
Our Strategy

<!-- b000410 | prose | pages [22] -->
Our strategy is to judge the market prospects of future investment products with high forecast accuracy and then use the "buy low and sell high" strategy to make decisions. This is a simple and effective way to make decisions, primarily when only historical price data is known.

<!-- b000411 | heading | pages [22] -->
The Results

<!-- b000412 | prose | pages [22] -->
After model solving, model checking, and sensitivity analysis, we can draw the following conclusions:

<!-- b000413 | prose | pages [22] -->
We input historical price data into quantitative investment decision-making models for  simulated trading. The initial capital is $1,000, and after a five-year trading period, the asset value is $270,836. The parameters of the model we have established have been optimized. The investment returns  are also higher than simple long-term trading, short-term trading, and some high-performance investment companies. We find that both the trading strategy and the trading results are highly sensitive to the change  of the Bitcoin commission payment ratio, and less sensitive to the change of the gold commission payment ratio. The above is the summary of our study. We sincerely hope that it will provide you with useful information.

<!-- b000414 | furniture | pages [23] -->
Team # 2218931

<!-- b000415 | furniture | pages [23] -->
Page 23 of 25

<!-- b000416 | heading | pages [23] -->
References

<!-- b000417 | references | pages [23] -->
[1] Zeng Lian, Ma Dandi & Liu Zongxin. (2010). Gold price prediction based on BP neural

<!-- b000418 | references | pages [23] -->
network improvement. Computer Simulation (09), 200-203.

<!-- b000419 | references | pages [23] -->
[2] Zhang Jundong, Liu Cheng & Sun Bin.(2010). Research on gold price prediction based on

<!-- b000420 | references | pages [23] -->
artiﬁcial neural network algorithm. Economic Problems (01), 110-114.

<!-- b000421 | references | pages [23] -->
[3] Lin Yu, Kong Liuliu & Liu Pei.(2010). Gold price forecast based on ARIMA model. Journal

<!-- b000422 | references | pages [23] -->
of South China University (Social Science Edition)(01), 36-38.

<!-- b000423 | references | pages [23] -->
[4] Jing Zhigang, Shi Guoliang. Gold price prediction of LS-SVM-ARIMA combined Model

<!-- b000424 | references | pages [23] -->
based on wavelet analysis [J]. Gold, 2017,38(05):5-8+14.

<!-- b000425 | references | pages [23] -->
[5] Yuan Dongfang. Gold futures price prediction based on CEEMDAN-PCA-LSTM model [D].

<!-- b000426 | references | pages [23] -->
Shandong University, 2021. DOI: 10.27272/d.cnki.gshdu.2021.005040.

<!-- b000427 | references | pages [23] -->
[6] Muzammal M, Qu Qiang, Nasrulin B.Renovating blockchain with distributed databases:An

<!-- b000428 | references | pages [23] -->
open source system[J]. Future Generation Computer Systems, 2019, 90 (1):105-117.

<!-- b000429 | references | pages [23] -->
[7] Wong S K, Wei Q, Chau K W. IPO Location as a Quality Signal:The Case of Chinese

<!-- b000430 | references | pages [23] -->
Developers[J]. The Journal of Real Estate Finance and Economics, 2014, 49(4):551-567.

<!-- b000431 | references | pages [23] -->
[8] Katsiampa P. Volatility estimation for Bitcoin: A comparison of GARCH models[J]. Eco-

<!-- b000432 | references | pages [23] -->
nomics Letters, 2017, 158(9):3-6.

<!-- b000433 | references | pages [23] -->
[9] Selin O S.Dynamic Connectedness between Bitcoin, Gold, and Crude Oil Volatilities and

<!-- b000434 | references | pages [23] -->
Returns[J]. Journal of Risk and Financial Management, 2020, 13(11): 127-136.

<!-- b000435 | references | pages [23] -->
[10] Duan J, Zhang C, Gong Y, etal. A Content-Analysis Based Literature Review in Blockchain

<!-- b000436 | references | pages [23] -->
Adoption within Food Supply Chain[J]. International Journal of Environmental Research and

<!-- b000437 | references | pages [23] -->
Public Health, 2020, 17(5):1784.

<!-- b000438 | references | pages [23] -->
[11] Marendra A, Ramadhani T, Kim R, et al. Bitcoin price forecasting using neural decomposition

<!-- b000439 | references | pages [23] -->
and deep learning[J]. Journal of the Korea Industrial Information Systems Research, 2018,

<!-- b000440 | references | pages [23] -->
23(4):171-180.

<!-- b000441 | references | pages [23] -->
[12] Ciaian P, Rajcaniova M, Kancs D. The economics of Bitcoin price formation[J].Applied

<!-- b000442 | references | pages [23] -->
Economics, 2016, 48(19):179-195.

<!-- b000443 | references | pages [23] -->
[13] Zhang Peng. A comparative study of Mean-Variance and Mean-VaR portfolios in the case of

<!-- b000444 | references | pages [23] -->
not allowing short selling [J]. China Management Science, 2008(04):30-35.

<!-- b000445 | references | pages [23] -->
[14] Xiong Lidong. Research on quantitative trading based on deep reinforcement learning [D].

<!-- b000446 | references | pages [23] -->
University of Electronic Science and Technology of China, 2019.

<!-- b000447 | references | pages [23] -->
[15] Fan Xiaoyu. Research on portfolio strategy through deep reinforcement learning [D]. Dalian

<!-- b000448 | references | pages [23] -->
University of Technology, 2021.

<!-- b000449 | furniture | pages [24] -->
Team # 2218931

<!-- b000450 | furniture | pages [24] -->
Page 24 of 25

<!-- b000451 | references | pages [24] -->
[16] Zhou Kaili, Kang Yaohong. Neural network model and its MATLAB simulation program

<!-- b000452 | references | pages [24] -->
design [M]. Beijing: Tsinghua University Press, 2005.

<!-- b000453 | references | pages [24] -->
[17] K. Madsen, H.B. Nielsen, and O. Tingleﬀ. Methods for Non-Linear Least Squares Prob-

<!-- b000454 | references | pages [24] -->
lems[R].Denmark: Technical Uninversity of Denmark, 2004.

<!-- b000455 | furniture | pages [25] -->
Team # 2218931

<!-- b000456 | furniture | pages [25] -->
Page 25 of 25

<!-- b000457 | heading | pages [25] -->
Appendices

<!-- b000458 | prose | pages [25] -->
The ﬁgure shows that the R2 of the training set, test set, validation set, and the whole is more than 0.99.

<!-- b000459 | caption | pages [25] -->
Figure 10: Fitting Accuracy Plot for Bitcoin
