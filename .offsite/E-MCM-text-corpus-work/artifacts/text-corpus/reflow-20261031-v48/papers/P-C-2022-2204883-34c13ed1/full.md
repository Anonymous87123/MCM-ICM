# P-C-2022-2204883-34c13ed1

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
2204883

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Gold Strategy for Gold & Bitcoin traders

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
In today’s society, with the continuous development of the economy, more and more people try to increase their income by means of asset investment. However, in the face of a large number of ﬁnancial products in the market, how to accurately predict their price movements, maximize returns and minimize risks through the right way of buying and selling is what every market trader wants to know.

<!-- b000010 | prose | pages [1] -->
A trader who only focus on two ﬁnancial products, gold and bitcoin, comes to us for help. In order to achieve the ambitious goal, we need to come up with a buying and selling plan that maximizes returns and minimize risks by analyzing the previous price data of gold and bitcoin respectively.

<!-- b000011 | prose | pages [1] -->
For task 1, after data preprocessing, we build price prediction models for gold and bitcoin respectively by using LSTM(Long Short-Term Memory), and investment strategy model by using MLP(Multi-objective Linear Programming) to maximize returns and minimize risks simultaneously. The price prediction result of gold reaches an MAPE(Mean Absolute Percentage Error) value of 0.007261 while the price prediction result of bitcoin reaches an MAPE value of 0.041630. Based on the investment strategy model, we develop the best daily trading strategy which ﬁnally makes the initial $1,000 investment worth $14,325.13 on September 10, 2021. The net proﬁt exceeds 13 times of the initial asset.

<!-- b000012 | prose | pages [1] -->
For task 2, we provide evidence that our model gives the best strategy by setting up 10 evaluation metrics and comparing the values of those metrics under 2 simple investment strategies, 1 idealized investment strategy and 1 commonly used investment strategy on the market, and the investment strategy obtained by our model. The result shows that our model develops a strategy with not only a high proﬁt but also a good balance between risk and return.

<!-- b000013 | prose | pages [1] -->
For task 3, We analyze the sensitivity of our strategy to the transaction costs of gold and bitcoin by changing the commission of one asset and keeping the commission of the other asset unchanged alternately. We set 5 metrics to measure the eﬀect on strategies and 2 metrics to measure the eﬀect on results. We ﬁnd that when the commission of gold increases, the net proﬁt remains the same and the win rate shows an upward trend; when the commission of bitcoin increases, the net proﬁt decreases signiﬁcantly and the win rate shows a decreasing trend. Therefore, we conclude that investment strategies are more sensitive to changes in the transaction costs of bitcoin.

<!-- b000014 | prose | pages [1] -->
Finally, we write a memorandum including our strategy, model, and results for the trader. We hope this memorandum will become a valuable reference for him or her further investment.

<!-- b000015 | keywords | pages [1] -->
Keywords: gold, bitcoin, trading strategy, Long Short-Term Memory, Multi-objective Linear

<!-- b000016 | prose | pages [1] -->
Programming, risk and return, sensitivity analysis

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction

<!-- b000019 | contents | pages [2] -->
1

<!-- b000020 | contents | pages [2] -->
2 Model Assumptions and Notations

<!-- b000021 | contents | pages [2] -->
2

<!-- b000022 | contents | pages [2] -->
2.1

<!-- b000023 | contents | pages [2] -->
Assumptions and justiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
2

<!-- b000025 | contents | pages [2] -->
2.2

<!-- b000026 | contents | pages [2] -->
Notations

<!-- b000027 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
3 Data Preprocessing

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
4 Task 1: Price Predictions & The Best Trading Strategy

<!-- b000032 | contents | pages [2] -->
3

<!-- b000033 | contents | pages [2] -->
4.1

<!-- b000034 | contents | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
3

<!-- b000036 | contents | pages [2] -->
4.2

<!-- b000037 | contents | pages [2] -->
The Price Prediction Model Based on LSTM . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
4

<!-- b000039 | contents | pages [2] -->
4.3

<!-- b000040 | contents | pages [2] -->
Investment Strategy Model Based on MLP . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
7

<!-- b000042 | contents | pages [2] -->
4.3.1

<!-- b000043 | contents | pages [2] -->
The MLP Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
8

<!-- b000045 | contents | pages [2] -->
4.3.2

<!-- b000046 | contents | pages [2] -->
Investment Strategy Based on The MLP Model . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
8

<!-- b000048 | contents | pages [2] -->
4.3.3

<!-- b000049 | contents | pages [2] -->
The Result of Our Investment Strategy . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
14

<!-- b000051 | contents | pages [2] -->
5 Task 2: Proof of The Best Strategy

<!-- b000052 | contents | pages [2] -->
15

<!-- b000053 | contents | pages [2] -->
5.1

<!-- b000054 | contents | pages [2] -->
Metrics for Evaluating Investment Strategies . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
15

<!-- b000056 | contents | pages [2] -->
5.2

<!-- b000057 | contents | pages [2] -->
Evidence for A Good Investment Strategy . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
17

<!-- b000059 | contents | pages [2] -->
6 Task 3: Sensitivity of Transaction Costs for The Strategy

<!-- b000060 | contents | pages [2] -->
19

<!-- b000061 | contents | pages [2] -->
6.1

<!-- b000062 | contents | pages [2] -->
Sensitivity of The Commissions of Gold . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
19

<!-- b000064 | contents | pages [2] -->
6.2

<!-- b000065 | contents | pages [2] -->
Sensitivity of The Commissions of Bitcoin . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
20

<!-- b000067 | contents | pages [2] -->
6.3

<!-- b000068 | contents | pages [2] -->
Analysis of The Result

<!-- b000069 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
21

<!-- b000071 | contents | pages [2] -->
7 Task 4: Memorandum for The Trader

<!-- b000072 | contents | pages [2] -->
22

<!-- b000073 | contents | pages [2] -->
8 Strengths and Weaknesses of Our Strategy

<!-- b000074 | contents | pages [2] -->
23

<!-- b000075 | contents | pages [2] -->
8.1

<!-- b000076 | contents | pages [2] -->
The Price Prediction model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
23

<!-- b000078 | contents | pages [2] -->
8.2

<!-- b000079 | contents | pages [2] -->
The Investment Strategy model . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
23

<!-- b000081 | furniture | pages [3] -->
Team # 2204883

<!-- b000082 | furniture | pages [3] -->
Page 1 of 23

<!-- b000083 | heading | pages [3] -->
1 Introduction

<!-- b000084 | prose | pages [3] -->
In today’s society, with the continuous development of the economy, more and more people want to increase their income by means of asset investment. However, in the face of a large number of ﬁnancial products in the market, how to accurately predict their price movements and maximize returns through the right way of buying and selling is what every market trader wants to know.

<!-- b000085 | prose | pages [3] -->
A trader who only focus on two ﬁnancial products, gold and bitcoin, comes to us for help. In order to achieve the ambitious goal, we need to come up with a buying and selling plan that maximizes returns by analyzing the previous price data of gold and bitcoin respectively.

<!-- b000086 | prose | pages [3] -->
To achieve our goal, we need to:

<!-- b000087 | prose | pages [3] -->
• Pre-process the data provided by COMAP oﬃcial.

<!-- b000088 | prose | pages [3] -->
• Build price prediction models for gold and bitcoin respectively.

<!-- b000089 | prose | pages [3] -->
• Build investment strategy model considering the predicted price of gold and bitcoin and their commissions for each transaction.

<!-- b000090 | prose | pages [3] -->
• Prove that our investment strategy is good enough by calculating strategy evaluation metrics and comparing the value to several other strategies.

<!-- b000091 | prose | pages [3] -->
• Analyze the sensitivity of our strategy to transaction costs by changing the commission value of gold and bitcoin.

<!-- b000092 | prose | pages [3] -->
• Write a memorandum including our strategy, model and results for the trader as a reference for his or her investment.

<!-- b000093 | prose | pages [3] -->
Our modeling framework can be illustrated as shown in Figure 1.

<!-- b000094 | caption | pages [3] -->
Figure 1: Modeling framework

<!-- b000095 | furniture | pages [4] -->
Team # 2204883

<!-- b000096 | furniture | pages [4] -->
Page 2 of 23

<!-- b000097 | heading | pages [4] -->
2 Model Assumptions and Notations

<!-- b000098 | heading | pages [4] -->
2.1 Assumptions and justiﬁcation

<!-- b000099 | prose | pages [4] -->
• The data provided in this problem is valid and reliable.

<!-- b000100 | prose | pages [4] -->
• There is no minimum purchase limit for both gold and bitcoin.

<!-- b000101 | prose | pages [4] -->
By visiting the oﬃcial website of London Bullion Market, we learned that the minimum purchase limit of gold on the trading market is one lot, i.e. 100 troy ounces, yet the initial capital of the trader in this problem cannot even buy 1 troy ounce of gold, so we made the assumption above.

<!-- b000102 | prose | pages [4] -->
• The inﬂation of the U.S. dollar can be ignored.

<!-- b000103 | prose | pages [4] -->
Although the inﬂation rate of the U.S. dollar is objectively existed, the inﬂation rate of the U.S. dollar over the past 5 years is not provided in this problem, so we default that the value of the U.S. dollar has not changed over the 5 years when calculating the ﬁnal return of the investment.

<!-- b000104 | prose | pages [4] -->
• We do not make any investments in the ﬁrst several days from September 11, 2016.

<!-- b000105 | prose | pages [4] -->
Although our model can give a prediction value, we do not make any investment because we can only refer to the price data up to that day and the training set data is too small in the ﬁrst few days, which can easily lead to a poor prediction result.

<!-- b000106 | prose | pages [4] -->
• The change of the commission costs does not inﬂuence the daily value of gold and bitcoin.

<!-- b000107 | prose | pages [4] -->
Since we need to determine the sensitivity of our strategy to transaction costs, we have to change the value of the commission of gold and bitcoin and see if the strategy changes or not. Therefore we need to assume that the daily values of gold and bitcoin do not change when the commission costs are changed.

<!-- b000108 | prose | pages [4] -->
• The daily value of gold and bitcoin is the value we buy or sell gold and bitcoin on that day.

<!-- b000109 | prose | pages [4] -->
Although in real life the prices of both gold and bitcoin ﬂuctuate over the course of a day, since the problem does not provide more detailed data, we have to make this assumption.

<!-- b000110 | prose | pages [4] -->
• In the price prediction model, both prediction of gold price and bitcoin reach the best result under a same parameter combination.

<!-- b000111 | prose | pages [4] -->
• The prices of gold and bitcoin do not aﬀect each other.

<!-- b000112 | prose | pages [4] -->
We believe that gold prices and bitcoin prices are independent of each other.

<!-- b000113 | heading | pages [4] -->
2.2 Notations

<!-- b000114 | prose | pages [4] -->
In this work, we use the nomenclature in Table 1 in the model construction. Other none- frequent-used symbols will be introduced once they are used.

<!-- b000115 | furniture | pages [5] -->
Team # 2204883

<!-- b000116 | prose | pages [5] -->
Symbols Deﬁnitions 푏 bias vector of LSTM 퐶 memory cell value of LSTM ˜퐶 candidate value of memory cell 푑 sliding window size ′ 푑 training sliding window size 푓 output function of forget gate ℎ hidden state of LSTM 푖 input function of forget gate 퐿 loss of one single trade 푙 hidden layer size of RNN 푀 total number of trades 푚 number of proﬁtable trades 표 output function of forget gate

<!-- b000117 | furniture | pages [5] -->
Page 3 of 23

<!-- b000118 | prose | pages [5] -->
Symbols Deﬁnitions 푃 proﬁt of one single trade 푟 price of an asset 푆 risk of purchasing 푡 data of trading 푉 number of investment 푣 average percentage of assets invested 푊 weight matrix of LSTM 푤 total worth of assets 훼 commission for each transaction 휖 epoch of RNN 휆 learning rate of RNN 휎 Sigmoid function 휔 optimal value of objective function

<!-- b000119 | caption | pages [5] -->
Table 1: Symbol list

<!-- b000120 | heading | pages [5] -->
3 Data Preprocessing

<!-- b000121 | prose | pages [5] -->
Sincewe are only allowed to use thedatasets ’LBMA-GOLD.csv’ and ’BCHAIN-MKPRU.csv’ provided by COMAP oﬃcial, we need to pre-process the data for both datasets before solving the problem.

<!-- b000122 | prose | pages [5] -->
Notice that there is no missing value in the bitcoin price dataset ’BCHAIN-MKPRU.csv’, however in the gold price dataset ’LBMA-GOLD.csv’, there are 10 trading days with missing price data, except for the non-trading days which do not appear in the dataset.

<!-- b000123 | prose | pages [5] -->
To facilitate the follow-up process, and to ensure the reliability and reasonableness of the data, we take the average of the prices of the two trading days before and after each trading day with missing gold price as the gold price of that day. The trading days with missing gold price and their corrected gold prices are shown in the table below.

<!-- b000124 | prose | pages [5] -->
Date Gold Price(Corrected) 12/23/16 1132.975 12/30/16 1148.45 12/22/17 1271.975 12/29/17 1301.525 12/24/18 1263.075 Date Gold Price(Corrected) 12/31/18 1280.95 12/24/19 1496.8 12/31/19 1520.925 12/24/20 1874.65 12/31/20 1915.4

<!-- b000125 | caption | pages [5] -->
Table 2: Trading days with missing gold price and corrected gold price

<!-- b000126 | heading | pages [5] -->
4 Task 1: Price Predictions & The Best Trading Strategy

<!-- b000127 | heading | pages [5] -->
4.1 Problem Analysis

<!-- b000128 | prose | pages [5, 6] -->
In this task, our goal is to develop a daily trading strategy based on the price data from previous days. However, the real investment behavior is implemented based on the expectations for the following days. That is, before we can develop a daily trading strategy, we need to make price predictions for gold and bitcoin for the following days respectively. Therefore, the answer to this task needs to consist of the following two steps:

<!-- b000129 | furniture | pages [6] -->
Team # 2204883

<!-- b000130 | furniture | pages [6] -->
Page 4 of 23

<!-- b000132 | prose | pages [6] -->
• Step 1: Predict the price changes of gold and bitcoin in the following days based on the price data from the previous days.

<!-- b000133 | prose | pages [6] -->
Since the price ﬂuctuations of gold and bitcoin are time-series in nature, we decide to use a time-series based model to predict the prices of gold and bitcoin respectively.

<!-- b000134 | prose | pages [6] -->
• Step 2: Develop a strategy based on the predicted price using an investment strategy model.

<!-- b000135 | heading | pages [6] -->
4.2 The Price Prediction Model Based on LSTM

<!-- b000136 | prose | pages [6] -->
LSTM(Long Short-Term Memory) is a special type of RNN(Recurrent Neural Net- work), which solves the problem of gradient explosion and gradient disappearance during the training of RNNs in long sequences, i.e., when the number of layers of the network increases, the subsequent nodes become less perceptive of the previous nodes, and the phenomenon of forgetting the previous information over time occurs[1][2].

<!-- b000137 | prose | pages [6] -->
Based on RNN, LSTM adds a memory unit to each neural unit in the hidden layer: an information transmission belt called "cell state", and uses structures such as forget gates, input gates, and output gates to control the memory information on the time series[3][4]. In this way, LSTM can dig deeper into the potential patterns between data and make the prediction more accurate and reliable. We are now going to introduce the function of each gate.

<!-- b000138 | caption | pages [6] -->
Figure 2: Workﬂow of LSTM

<!-- b000139 | prose | pages [6] -->
i. Forget Gate

<!-- b000140 | prose | pages [6] -->
The function of the forget gate is to selectively forget certain information from the past. LSTM uses the Sigmoid function to achieve the goal. The Sigmoid function is shown below:

<!-- b000141 | prose | pages [6] -->
1 휎(푥) = (1) 1 + 푒−푥

<!-- b000142 | prose | pages [6, 7] -->
In the forget gate, the information of the hidden state of the previous moment (t-1 moment) ℎ푡−1 is input into the Sigmoid function together with the data of this moment (t moment) 푥푡, and the output value is between 0 and 1, which indicates whether we should forget this information. The closer the output value is to 0, the more the probability we should forget this information and vice versa. The output function of the forget gate is shown below:

<!-- b000143 | furniture | pages [7] -->
Team # 2204883

<!-- b000144 | furniture | pages [7] -->
Page 5 of 23

<!-- b000146 | prose | pages [7] -->
푓푡= 휎(푊푓· [ℎ푡−1, 푥푡] + 푏푓) (2)

<!-- b000147 | prose | pages [7] -->
in which [ℎ푡−1, 푥푡] is the concatenated vector of ℎ푡−1 and 푥푡, 푊푓is the weight matrix for the forget gate in RNN which adjust the dimension of the concatenated vector, and 푏푓is the bias vector for the forget gate in RNN. The output value 푓푡will destine whether we should forget the previous memory cell value 퐶푡−1 in the input gate.

<!-- b000148 | prose | pages [7] -->
ii. Input Gate

<!-- b000149 | prose | pages [7] -->
The function of the input gate is to selectively memorize certain information from the past and to decide the value of the current memory cell 퐶푡.

<!-- b000150 | prose | pages [7] -->
In the input gate, two intermediate variables are generated: the output value of input gate 푖푡, shown in equation (3):

<!-- b000151 | prose | pages [7] -->
푖푡= 휎(푊푖· [ℎ푡−1, 푥푡] + 푏푖) (3)

<!-- b000152 | prose | pages [7] -->
and the candidate memory cell value ˜퐶푡, show in equation (4):

<!-- b000153 | prose | pages [7] -->
˜퐶푡= 푡푎푛ℎ(푊퐶· [ℎ푡−1, 푥푡] + 푏퐶) (4)

<!-- b000154 | prose | pages [7] -->
Same as the output of forget gate, the output value of input gate is between 0 1, which indicates whether we should forget the information of the candidate memory cell value. The closer the output value is to 0, the more the probability we should forget this information and vice versa. Moreover, LSTM model need us to use 푡푎푛ℎ() function to normalize the value of ˜퐶푡to (-1, 1).

<!-- b000155 | prose | pages [7] -->
After calculating the intermediate variables, LSTM model need us to combine the output of both forget gate and input gate to generate the ﬁnal value of the current memory cell 퐶푡, and the equation is shown below:

<!-- b000156 | prose | pages [7] -->
퐶푡= 푓푡퐶푡−1 + 푖푡˜퐶푡 (5)

<!-- b000157 | prose | pages [7] -->
iii. Output Gate

<!-- b000158 | prose | pages [7] -->
The function of the output gate is to selectively generate the value of the current hidden state ℎ푡. The output value of the output gate 표푡plays the role as an intermediate variable, and we use equation (6) to calculate this value.

<!-- b000159 | prose | pages [7] -->
표푡= 휎(푊표· [ℎ푡−1, 푥푡] + 푏표) (6)

<!-- b000160 | prose | pages [7] -->
in which 푊표is the weight matrix for the output gate in RNN which adjust the dimension of the concatenated vector, and 푏표is the bias vector for the output gate in RNN. The output value 표푡destines the value of the current hidden state ℎ푡in the equation below:

<!-- b000161 | furniture | pages [8] -->
Team # 2204883

<!-- b000162 | furniture | pages [8] -->
Page 6 of 23

<!-- b000163 | prose | pages [8] -->
ℎ푡= 표푡푡푎푛ℎ(퐶푡) (7)

<!-- b000164 | prose | pages [8] -->
With the value of ℎ푡and 퐶푡generated at time 푡, we can iteratively calculate the values at time 푡+ 1 using the functions of the three gates until the time limit is reached and the ﬁnal prediction result is generated.

<!-- b000165 | prose | pages [8] -->
When applying LSTM model to our task, the ﬁrst thing we need to is to determine the input and output of the model. Here we use the Sliding Window Algorithm, that is, when predicting the price of gold and bitcoin for each day, we use only the price data of the previous 푑days before that day as the input to the LSTM model. In the model, each day and its previous ′ < 푑) days are used for the training process. ′(푑 푑

<!-- b000166 | prose | pages [8] -->
After the calculation of the model, we ﬁnally get the predicted value of gold ˆ푟푔,푡and the predicted value of bitcoin ˆ푟푏,푡for each date 푡respectively as the output of the model.

<!-- b000167 | prose | pages [8] -->
The process of executing Sliding Window Algorithm is shown in the ﬁgure below.

<!-- b000168 | caption | pages [8] -->
Figure 3: The process of Sliding Window Algorithm

<!-- b000169 | prose | pages [8] -->
Since in the LSTM model, changes in the hidden layer size 푙, sliding window size 푑, training ′, learning rate 휆and the value of epoch 휖will have an impact on the sliding window size 푑 prediction results, to easily obtain the best prediction result, we adjust the values of these 5 parameters separately to obtain the MAPE(Mean Absolute Percentage Error) values of gold prediction results under diﬀerent parameter values(since we believe that both prediction of gold price and bitcoin price reach the best result under the same parameter combination). The equation to calculate MAPE value is shown below:

<!-- b000170 | prose | pages [8] -->
푛 ∥푟푔,푡−ˆ푟푔,푡∥ 푀퐴푃퐸= 1 Õ (8) 푛 푟푔,푡 푡=1

<!-- b000171 | prose | pages [8] -->
Initially, we set the value of each parameter as

<!-- b000172 | prose | pages [8] -->
′ = 5, 휆= 0.001, 휖= 50]. [푙= 100, 푑= 10, 푑

<!-- b000173 | prose | pages [8, 9] -->
When tuning the parameter, each time we only change the value of one parameter and keep the values of other parameters unchanged. The MAPE values of the price prediction of gold are shown in the following table:

<!-- b000174 | furniture | pages [9] -->
Team # 2204883

<!-- b000175 | furniture | pages [9] -->
Page 7 of 23

<!-- b000177 | prose | pages [9] -->
′ 푑 푀퐴푃퐸 푑 푀퐴푃퐸 휆 푀퐴푃퐸 7 0.007320101 1 0.010315979 0.0005 0.008678837 0.007261552 10 3 0.012500496 0.0007 0.008465359 0.007261552 0.007261552 13 0.011110205 5 0.001 15 0.010985684 7 0.008998699 0.0015 0.009933032 20 0.010590555 9 0.007450314 0.002 0.010285589

<!-- b000178 | caption | pages [9] -->
Table 3: 푀퐴푃퐸values of the price prediction of gold

<!-- b000179 | prose | pages [9] -->
We found that our prediction model is sensitive to the value of sliding window size ′ and learning rate 휆. The 푀퐴푃퐸of gold prediction 푑, training sliding window size 푑 result reaches the minimum value of 0.007261552 when the values of the parameters reach a combination of

<!-- b000180 | prose | pages [9] -->
′ = 5, 휆= 0.001, 휖= 50], [푙= 100, 푑= 10, 푑

<!-- b000181 | prose | pages [9] -->
so we choose the prediction results under this combination of parameters as the ﬁnal gold and bitcoin price prediction result, which shown in the ﬁgures below.

<!-- b000182 | prose | pages [9] -->
(a) Price of gold (b) Price of bitcoin

<!-- b000183 | caption | pages [9] -->
Figure 4: Predicted price vs real prices

<!-- b000184 | prose | pages [9] -->
The price predictions for both gold and bitcoin are proven to be good by comparing the predicted curve and the real curve of the price of both gold and bitcoin.

<!-- b000185 | heading | pages [9] -->
4.3 Investment Strategy Model Based on MLP

<!-- b000186 | prose | pages [9] -->
We now have the daily price prediction for gold and bitcoin. Next we will develop our investment strategy from September 11, 2016 based on these prediction results.

<!-- b000187 | prose | pages [9] -->
Since in the price prediction model we need to forecast the price for each trading day based on the price data of the previous 10 trading days from that trading day, we do not make any investments during the ﬁrst 10 trading days of gold(that is, the ﬁrst 14 trading days of bitcoin) of this 5-year period of investment, i.e. September 11, 2016 - September 24, 2016.

<!-- b000188 | prose | pages [9, 10] -->
Noting that we have already obtained daily price prediction for gold and bitcoin, an intuitive investment strategy would be to make the most proﬁtable investment each day based on the forecast. For example, if we predict that the growth rate of bitcoin on the next day is greater than the growth rate of gold and also greater than the commission required when purchasing bitcoin, we would turn all of our assets into bitcoins. However, the fact is that the predicted price values are diﬀerent from the true values, especially when the predicted and real values are moving in opposite trends, making investment based on such strategy will be more risky.

<!-- b000189 | furniture | pages [10] -->
Team # 2204883

<!-- b000190 | furniture | pages [10] -->
Page 8 of 23

<!-- b000192 | prose | pages [10] -->
Therefore, in order to get the best investment strategy, we need to consider both the possible proﬁts and the potential risks associated with the investment strategy. Here we use an MLP(Multi-objective Linear Programming) model to solve the problem.

<!-- b000193 | heading | pages [10] -->
4.3.1 The MLP Model

<!-- b000194 | prose | pages [10] -->
MLP(Multi-objective Linear Programming) is one of the most important elements of multi-objective decision making[5]. In multi-objective decision making, a multi-objective linear programming problem is formed when it is desired that each objective is as large (or as small) as possible. A general form of an m-objective linear programming problem should be:

<!-- b000195 | prose | pages [10] -->
푓(푥) = [ 푓1(푥), 푓2(푥), ..., 푓푚(푥)]푇, 푚푖푛

<!-- b000196 | prose | pages [10] -->
( 푔푖(푥) ≤0, 푖= 1, 2, ..., 푝, 푠.푡. ℎ푗(푥) = 0, 푗= 1, 2, ..., 푞.

<!-- b000197 | prose | pages [10] -->
in which 푓1(푥), 푓2(푥), ..., 푓푚(푥) stand for 푚objective functions, 푔푖(푥), ℎ푗(푥) stand for the constraints of the objective functions.

<!-- b000198 | prose | pages [10] -->
In order to solve this problem, we apply the ideal point method. This method requires us to split the multi-objective linear programming problem into multiple single-objective linear programming problems and separately obtain the optimal values of each objective function:

<!-- b000199 | prose | pages [10] -->
휔1, 휔2, ..., 휔푚.

<!-- b000200 | prose | pages [10] -->
After that, we construct the sum of squares of the diﬀerence between each objective func- tion and the optimal value as a new objective function. By solving the following quadratic programming problem:

<!-- b000201 | prose | pages [10] -->
푚 Õ 푚푖푛 푓= ( 푓푖(푥) −휔푖)2 (9) 푖=1

<!-- b000202 | prose | pages [10] -->
( 푔푖(푥) ≤0, 푖= 1, 2, ..., 푝, 푠.푡. ℎ푗(푥) = 0, 푗= 1, 2, ..., 푞.

<!-- b000203 | prose | pages [10] -->
Finally we could obtain the optimal solution 푥표푝푡for the original multi-objective linear programming problem by this mean.

<!-- b000204 | heading | pages [10] -->
4.3.2 Investment Strategy Based on The MLP Model

<!-- b000205 | prose | pages [10] -->
We synthesize the methods of multi-objective linear programming and optimal portfolio formulation, determine the decision variables, objective function, and constraints of the plan- ning problem respectively, and obtain a model that helps us develop a daily investment strategy.

<!-- b000206 | furniture | pages [11] -->
Team # 2204883

<!-- b000207 | furniture | pages [11] -->
Page 9 of 23

<!-- b000208 | prose | pages [11] -->
Since the model integrates the predicted prices of gold and bitcoin for the next trading day and the respective investment risks, the model can be well applied to develop an investment strategy for each trading day.

<!-- b000209 | prose | pages [11] -->
To begin with, we simplify the development of an investment strategy as follows:

<!-- b000210 | prose | pages [11] -->
The worth values of cash, gold and bitcoin at the end of date 푡are noted as

<!-- b000211 | prose | pages [11] -->
[푥푐, 푥푔, 푥푏]

<!-- b000212 | prose | pages [11] -->
all in U.S. dollar, in which 푥푔equals to the product of the amount of gold(in troy ounce) and the price of gold per troy ounce, 푥푏equals to the product of the amount of bitcoin(in number) and the price of bitcoin per single bitcoin. According to the predicted price of gold(noted as ˆ푟푔,푡+1) and the predicted price of bitcoin(noted as ˆ푟푏,푡+1) on the coming day, the assets are purchased and sold to get a new portfolio noted as

<!-- b000213 | prose | pages [11] -->
′ ′ ′ [푥 푐, 푥 푔, 푥 푏]

<!-- b000214 | prose | pages [11] -->
in U.S. Dollar, which maximizes the return(noted as 푃) while minimizing the investment risk(noted as 푅).

<!-- b000215 | prose | pages [11] -->
After that, we deﬁne the investment risk 푅for the coming day(date 푡+ 1) as

<!-- b000216 | prose | pages [11] -->
′ ′ 푅= (푥 푔−푥푔)푆푔+ (푥 푏−푥푏)푆푏 (10)

<!-- b000217 | prose | pages [11] -->
in which

<!-- b000218 | prose | pages [11] -->
s 10Í 10Í  푆푔= (푟푔푗−¯푟푔푗)2, ¯푟푔푗= 1 푟푔푗 1 9 10 푗=1 푗=1 s 10Í 10Í  푆푏= (푟푏푗−¯푟푏푗)2, ¯푟푏푗= 1 푟푏푗 1 9 10 푗=1 푗=1

<!-- b000219 | prose | pages [11] -->
where 푆푔and 푆푏stand for the risk of purchasing gold and bitcoin on date 푡+ 1 respectively, 푟푔푗and 푟푏푗stand for the price value the gold and bitcoin 푗days before date 푡+ 1 respectively.

<!-- b000220 | prose | pages [11] -->
On the other hand, the predicted return 푃for the coming day(date 푡+ 1) is calculated as

<!-- b000221 | prose | pages [11] -->
푃= ( ˆ푟푔,푡+1 −푟푔,푡 푔−푥푔) + ( ˆ푟푏,푡+1 −푟푏,푡 ′ ′ ) · (푥 ) · (푥 푏−푥푏) (11) 푟푔,푡 푟푏,푡

<!-- b000222 | prose | pages [11] -->
in which 푟푔,푡and 푟푏,푡stand for the true value of gold and bitcoin at the end of date 푡. Combining the predicted returns and risks, we now obtain the objective function as the form of

<!-- b000223 | prose | pages [11] -->
푚푎푥 푃, 푚푖푛 푅

<!-- b000224 | prose | pages [11, 12] -->
and can be also written as 푚푖푛 −푃, 푅

<!-- b000225 | furniture | pages [12] -->
Team # 2204883

<!-- b000226 | furniture | pages [12] -->
Page 10 of 23

<!-- b000228 | prose | pages [12] -->
Now we turn our attention to the trading behavior, for both gold and bitcoin, there are six trading behaviors: purchasing both gold and bitcoin, purchasing gold and selling bitcoin, selling gold and purchasing bitcoin, selling both gold and bitcoin, purchasing bitcoin on non-trading days for gold, and selling bitcoin on non-trading days for gold. Noting that the constraints of the multi-objective linear programming model is diﬀerent among trading behaviors, we build MLP models for each trading behavior separately.

<!-- b000229 | prose | pages [12] -->
For further processing, we note the amount of U.S. dollar spent/received when trading gold and bitcoin as Δ푥푔and Δ푥푏respectively, an obvious constraint for each model is:

<!-- b000230 | prose | pages [12] -->
′ 푥 푐= 푥푐−Δ푥푔−Δ푥푏 (12)

<!-- b000231 | prose | pages [12] -->
Also, we note the commission for trading gold and bitcoin as 훼푔= 1% and 훼푏= 2% respectively instead of using their lengthy form 훼푔표푙푑and 훼푏푖푡푐표푖푛.

<!-- b000232 | prose | pages [12] -->
i. Purchasing both gold and bitcoin

<!-- b000233 | prose | pages [12] -->
This trading behavior can be noted as

<!-- b000234 | prose | pages [12] -->
Δ푥푔> 0, Δ푥푏> 0

<!-- b000235 | prose | pages [12] -->
′ ′ Since the value of 푥 푔−푥푔and 푥 푏−푥푏can be substituted as

<!-- b000236 | prose | pages [12] -->
( ′ 푥 푔−푥푔= (1 −훼푔)Δ푥푔 ′ 푥 푏−푥푏= (1 −훼푏)Δ푥푏

<!-- b000237 | prose | pages [12] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000238 | prose | pages [12] -->
−ˆ푟푔,푡+1 −푟푔,푡 · (1 −훼푔)Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡 푚푖푛 · (1 −훼푏)Δ푥푏 푟푔,푡 푟푏,푡

<!-- b000239 | prose | pages [12] -->
푚푖푛 (1 −훼푔)Δ푥푔푆푔+ (1 −훼푏)Δ푥푏푆푏

<!-- b000240 | prose | pages [12] -->
Δ푥푔+ Δ푥푏< 푥푐  푠.푡. Δ푥푔> 0 Δ푥푏> 0  ii. Purchasing gold and selling bitcoin

<!-- b000241 | prose | pages [12] -->
This trading behavior can be noted as

<!-- b000242 | prose | pages [12, 13] -->
Δ푥푔> 0, Δ푥푏≤0 ′ ′ Since the value of 푥 푔−푥푔and 푥 푏−푥푏can be substituted as

<!-- b000243 | furniture | pages [13] -->
Team # 2204883

<!-- b000244 | furniture | pages [13] -->
Page 11 of 23

<!-- b000246 | prose | pages [13] -->
( ′ 푥 푔−푥푔= (1 −훼푔)Δ푥푔 ′ ′ 푥 푏−푥푏= 1−훼푏Δ푥푏, 0 ≤푥 1 푏

<!-- b000247 | prose | pages [13] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000248 | prose | pages [13] -->
−ˆ푟푔,푡+1 −푟푔,푡 · (1 −훼푔)Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡 1 푚푖푛 Δ푥푏 · 푟푔,푡 푟푏,푡 1 −훼푏

<!-- b000249 | prose | pages [13] -->
1 푚푖푛 (1 −훼푔)Δ푥푔푆푔+ Δ푥푏푆푏 1 −훼푏

<!-- b000250 | prose | pages [13] -->
Δ푥푔+ Δ푥푏< 푥푐  Δ푥푔> 0 푠.푡. Δ푥푏≤0  −Δ푥푏< (1 −훼푏)푥푏

<!-- b000251 | prose | pages [13] -->
iii. Selling gold and purchasing bitcoin

<!-- b000252 | prose | pages [13] -->
This trading behavior can be noted as

<!-- b000253 | prose | pages [13] -->
Δ푥푔≤0, Δ푥푏> 0

<!-- b000254 | prose | pages [13] -->
′ ′ Since the value of 푥 푔−푥푔and 푥 푏−푥푏can be substituted as

<!-- b000255 | prose | pages [13] -->
′ ′ ( 푥 푔−푥푔= 1−훼푔Δ푥푔, 0 ≤푥 1 푔 ′ 푥 푏−푥푏= (1 −훼푏)Δ푥푏

<!-- b000256 | prose | pages [13] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000257 | prose | pages [13] -->
−ˆ푟푔,푡+1 −푟푔,푡 Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡 1 푚푖푛 · (1 −훼푏)Δ푥푏 · 푟푔,푡 1 −훼푔 푟푏,푡

<!-- b000258 | prose | pages [13] -->
1 푚푖푛 Δ푥푔푆푔+ (1 −훼푏)Δ푥푏푆푏 1 −훼푔

<!-- b000259 | prose | pages [13] -->
Δ푥푔+ Δ푥푏< 푥푐  Δ푥푔≤0 푠.푡. Δ푥푏> 0  −Δ푥푔< (1 −훼푔)푥푔

<!-- b000260 | prose | pages [13, 14] -->
iv. Selling both gold and bitcoin This trading behavior can be noted as

<!-- b000261 | furniture | pages [14] -->
Team # 2204883

<!-- b000262 | furniture | pages [14] -->
Page 12 of 23

<!-- b000264 | prose | pages [14] -->
Δ푥푔≤0, Δ푥푏≤0

<!-- b000265 | prose | pages [14] -->
′ ′ Since the value of 푥 푔−푥푔and 푥 푏−푥푏can be substituted as

<!-- b000266 | prose | pages [14] -->
′ ′ ( 푥 푔−푥푔= 1−훼푔Δ푥푔, 0 ≤푥 1 푔 ′ ′ 푥 푏−푥푏= 1−훼푏Δ푥푏, 0 ≤푥 1 푏

<!-- b000267 | prose | pages [14] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000268 | prose | pages [14] -->
−ˆ푟푔,푡+1 −푟푔,푡 Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡 1 1 푚푖푛 Δ푥푏 · · 푟푔,푡 1 −훼푔 푟푏,푡 1 −훼푏

<!-- b000269 | prose | pages [14] -->
1 1 푚푖푛 Δ푥푔푆푔+ Δ푥푏푆푏 1 −훼푔 1 −훼푏

<!-- b000270 | prose | pages [14] -->
Δ푥푔+ Δ푥푏< 푥푐  Δ푥푔≤0 푠.푡. Δ푥푏≤0 −Δ푥푔< (1 −훼푔)푥푔  −Δ푥푏< (1 −훼푏)푥푏

<!-- b000271 | prose | pages [14] -->
v. Purchasing bitcoin on non-trading days for gold

<!-- b000272 | prose | pages [14] -->
This trading behavior can be noted as

<!-- b000273 | prose | pages [14] -->
Δ푥푔= 0, Δ푥푏> 0

<!-- b000274 | prose | pages [14] -->
′ ′ Since the value of 푥 푔−푥푔and 푥 푏−푥푏can be substituted as

<!-- b000275 | prose | pages [14] -->
( ′ 푥 푔−푥푔= 0 ′ 푥 푏−푥푏= (1 −훼푏)Δ푥푏

<!-- b000276 | prose | pages [14] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000277 | prose | pages [14] -->
−ˆ푟푏,푡+1 −푟푏,푡 푚푖푛 · (1 −훼푏)Δ푥푏 푟푏,푡

<!-- b000278 | prose | pages [14, 15] -->
푚푖푛 (1 −훼푏)Δ푥푏푆푏 ( Δ푥푏< 푥푐 푠.푡. Δ푥푏> 0

<!-- b000279 | furniture | pages [15] -->
Team # 2204883

<!-- b000280 | furniture | pages [15] -->
Page 13 of 23

<!-- b000282 | prose | pages [15] -->
vi. Selling bitcoin on non-trading days for gold

<!-- b000283 | prose | pages [15] -->
This trading behavior can be noted as

<!-- b000284 | prose | pages [15] -->
Δ푥푔= 0, Δ푥푏≤0

<!-- b000285 | prose | pages [15] -->
′ ′ Since the value of 푥 푔−푥푔and 푥 푏−푥푏can be substituted as

<!-- b000286 | prose | pages [15] -->
( ′ 푥 푔−푥푔= 0 ′ 푥 푏−푥푏= 1−훼푏Δ푥푏 1

<!-- b000287 | prose | pages [15] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000288 | prose | pages [15] -->
−ˆ푟푏,푡+1 −푟푏,푡 1 푚푖푛 Δ푥푏 · 푟푏,푡 1 −훼푏

<!-- b000289 | prose | pages [15] -->
1 푚푖푛 Δ푥푏푆푏 1 −훼푏

<!-- b000290 | prose | pages [15] -->
Δ푥푏< 푥푐  푠.푡. Δ푥푏≤0 −Δ푥푏< (1 −훼푏)푥푏  Based on the six models above, we bring the price prediction results of gold and bitcoin into model i-iv for calculation on trading days of gold respectively, and bring the price prediction results of bitcoin into model v-iv for calculation on non-trading days of gold respectively, and choose the most optimal trading behavior as the portfolio for the coming day.

<!-- b000291 | prose | pages [15] -->
It is worth noting that since each trading behavior involves high commissions, even the most optimal trading behavior may cause losses after paying commissions, so we compare the return value when executing the most optimal trading behavior with the return when keeping the portfolio unchanged, if

<!-- b000292 | prose | pages [15] -->
푐+ ˆ푟푔,푡+1 푏< 푥푐+ ˆ푟푔,푡+1 푔+ ˆ푟푏,푡+1 푥푔+ ˆ푟푏,푡+1 ′ ′ ′ 푥 푥 푥 푥푏 (13) 푟푔,푡 푟푏,푡 푟푔,푡 푟푏,푡

<!-- b000293 | prose | pages [15] -->
holds, the portfolio will keep unchanged; otherwise the portfolio will be changed into the most optimal trading behavior given by the model.

<!-- b000294 | furniture | pages [16] -->
Team # 2204883

<!-- b000295 | furniture | pages [16] -->
Page 14 of 23

<!-- b000296 | heading | pages [16] -->
4.3.3 The Result of Our Investment Strategy

<!-- b000297 | prose | pages [16] -->
We take the initial worth values of cash, gold and bitcoin at September 25, 2016 , since we do not make any investment in the very beginning 14 days’ period, as

<!-- b000298 | prose | pages [16] -->
[푥푐, 푥푔, 푥푏] = [1000, 0, 0],

<!-- b000299 | prose | pages [16] -->
and the predicted value of gold and bitcoin on that day as the input of our investment strategy model. We calculate the optimal portfolio for each day with a combination of the predicted price of gold and bitcoin and the investment strategy model. The date we buy or sell bitcoin from January 1, 2017 to January 1, 2018, as an example under our investment strategy, is shown in the ﬁgure below.

<!-- b000300 | caption | pages [16] -->
Figure 5: Date to buy or sell bitcoin, from Jan.1, 2017 to Jan.1, 2018

<!-- b000301 | prose | pages [16] -->
Finally we discount the total asset value of each day by the closing price of gold and bitcoin for each day and obtain a line graph of daily assets.

<!-- b000302 | caption | pages [16] -->
Figure 6: Curve of daily asset value

<!-- b000303 | prose | pages [16] -->
The result is: by using our model and strategy, ﬁnally the initial $1,000 investment worth $14,325.13 on September 10, 2021, which makes a proﬁt more than 13 times of the initial investment.

<!-- b000304 | furniture | pages [17] -->
Team # 2204883

<!-- b000305 | furniture | pages [17] -->
Page 15 of 23

<!-- b000306 | heading | pages [17] -->
5 Task 2: Proof of The Best Strategy

<!-- b000307 | prose | pages [17] -->
In Task 1, we have already built the price prediction model as well as the investment strategy model and have obtained the most optimal investment strategy for each day of the 5-year period from September 11, 2016 to September 10, 2021.

<!-- b000308 | prose | pages [17] -->
Now we set up some evaluation metrics and proved that the investment strategy obtained by our model is the best by comparing the values of these metrics under 2 simple investment strategies (a 5-year long-term investment in gold, a 5-year long-term investment in bitcoin) , 1 idealized investment strategy and 1 commonly used investment strategy on the market, as well as under the investment strategy obtained by our model.

<!-- b000309 | heading | pages [17] -->
5.1 Metrics for Evaluating Investment Strategies

<!-- b000310 | prose | pages [17] -->
We set up 10 metrics for investment strategy evaluation.

<!-- b000311 | prose | pages [17] -->
i. ARR(Annualized Rate of Return)

<!-- b000312 | prose | pages [17] -->
ARR is a theoretical rate of return calculated by converting the current daily rate of return into an annualized rate of return. It is calculated from the equation

<!-- b000313 | prose | pages [17] -->
퐴푅푅= 푤푡−푤0 × 365 × 100% 푤0 푡

<!-- b000314 | prose | pages [17] -->
in which 푤푡means the worth of your assets on day 푡and 푤0 means the worth of your initial investment.

<!-- b000315 | prose | pages [17] -->
ii. PLR(Proﬁt/Loss Ratio)

<!-- b000316 | prose | pages [17] -->
PLR is the ratio of proﬁt to loss for each trade in a period of investment. Suppose that 푚 trades make proﬁt(푃푖for each) and 푛trades loss(퐿푗for each) in a period of investment, the PLR is calculated from the equation below.

<!-- b000317 | prose | pages [17] -->
푚Í 푃푖 푖=1 푃퐿푅= 푛Í 퐿푗 푗=1

<!-- b000318 | prose | pages [17] -->
iii. NT(Number of Trade))

<!-- b000319 | prose | pages [17] -->
NT stands for the total amount of trades in a period of investment. We deﬁne the process from opening a position to closing a position as a single trade.

<!-- b000320 | prose | pages [17] -->
iv. WR(Win Rate)

<!-- b000321 | prose | pages [17] -->
WR measures the number of proﬁtable trades as a percentage of the total number of trades. Suppose that there are 푀trades in a period of investment and in which 푚trades make proﬁt, the WR is calculated from the equation below.

<!-- b000322 | prose | pages [17] -->
푊푅= 푚 푀× 100%

<!-- b000323 | prose | pages [17, 18] -->
v. MPA(Maximum Proﬁt Amount) MPA measures the maximum proﬁt value of a single trade in a period of investment. Suppose that 푚trades make proﬁt(푃푖for each) in a period of investment, MPA can be calculated as follow.

<!-- b000324 | furniture | pages [18] -->
Team # 2204883

<!-- b000325 | furniture | pages [18] -->
Page 16 of 23

<!-- b000327 | prose | pages [18] -->
푀푃퐴= 푚푎푥{푃푖}

<!-- b000328 | prose | pages [18] -->
vi. MLA(Maximum Loss Amount)

<!-- b000329 | prose | pages [18] -->
MLA measures the maximum loss value of a single trade in a period of investment. Suppose that 푛trades loss(퐿푗for each, 퐿푗< 0) in a period of investment, MLA can be calculated as follow.

<!-- b000330 | prose | pages [18] -->
푀퐿퐴= 푚푖푛{퐿푗}

<!-- b000331 | prose | pages [18] -->
vii. MCP(Maximum umber of Consecutive Proﬁts)

<!-- b000332 | prose | pages [18] -->
MCP is the maximum number of consecutive proﬁtable trades in a period of investment.

<!-- b000333 | prose | pages [18] -->
viii. MCL(Maximum umber of Consecutive Losses)

<!-- b000334 | prose | pages [18] -->
MCL is the maximum number of consecutive lossing trades in a period of investment.

<!-- b000335 | prose | pages [18] -->
ix. MDD(Maximum Drawdown)

<!-- b000336 | prose | pages [18] -->
MDD is the maximum observed loss from a peak to a trough of a portfolio during the period of investment. It is an indicator of downside risk over the period of investment.

<!-- b000337 | prose | pages [18] -->
x. SR(Sharpe Ratio)

<!-- b000338 | prose | pages [18] -->
SR is one of the most commonly used metrics in strategy evaluation, and it is one of the most valuable performance metrics considering both return and risk. For a good strategy, the larger the value of SR, the better. SR can be calculated as follow:

<!-- b000339 | prose | pages [18] -->
1. Based on the curve of the asset, we calculate the value of DRR(Daily Rate of Return) for each day and obtain a DRR series 푤푖 퐷푅푅= {퐷푅푅푖|퐷푅푅푖= × 100%} 푤푖−1

<!-- b000340 | prose | pages [18] -->
which is subject to normal distribution;

<!-- b000341 | prose | pages [18] -->
2. Calculate the average 퐸(퐷푅푅) and the variance 퐷(퐷푅푅) of the DRR series;

<!-- b000342 | prose | pages [18] -->
3. Since in this problem, we ignore the cash interest, we ﬁnally obtain SR under the equation

<!-- b000343 | prose | pages [18] -->
퐸(퐷푅푅) 푆푅= 퐷(퐷푅푅) p

<!-- b000344 | prose | pages [18] -->
A strategy has a negative average return when 푆푅< 0, and the strategy has a positive average return when 푆푅> 0.

<!-- b000345 | furniture | pages [19] -->
Team # 2204883

<!-- b000346 | furniture | pages [19] -->
Page 17 of 23

<!-- b000347 | heading | pages [19] -->
5.2 Evidence for A Good Investment Strategy

<!-- b000348 | prose | pages [19] -->
With the 10 metrics deﬁned above, we now compare the values of those metrics under 2 simple investment strategies, 1 ideal investment strategy, 1 commonly used investment strategy on the market and our investment strategy. Brief introductions of these 4 strategies are shown below.

<!-- b000349 | heading | pages [19] -->
1. A 5-year long-term investment in gold(Gold Asset)

<!-- b000350 | prose | pages [19] -->
In brief, this strategy requires us to use all of our initial $1,000 to purchase gold on the ﬁrst trading day and to not make any gold and bitcoin related trades for the next 5 years.

<!-- b000351 | prose | pages [19] -->
For the purpose of representing the trades and calculating metrics such as MPA, MLA, etc., we equate this strategy as follows: in the absence of commissions, we sell all of our gold ﬁrst and then purchase an equal amount of gold at the same price on each trading day, except for the ﬁrst trading day.

<!-- b000352 | heading | pages [19] -->
2. A 5-year long-term investment in bitcoin(Bitcoin Asset)

<!-- b000353 | prose | pages [19] -->
This strategy shares the same idea with the strategy above. The only diﬀerence is that in this strategy, we use all of our initial $1,000 to purchase bitcoin on the ﬁrst trading day.

<!-- b000354 | prose | pages [19] -->
3. An ideal strategy in the circumstance that we know the exact value of daily price of gold and bitcoin(Ideal Asset) This strategy shares the same investment strategy model with our strategy. The diﬀerence is that our strategy is developed by bringing the predicted price values of gold and bitcoin into the model, while this ideal strategy is developed by bringing the true price values of gold and bitcoin into the model.

<!-- b000355 | heading | pages [19] -->
4. A commonly used investment strategy on the market(Rule Asset)

<!-- b000356 | prose | pages [19] -->
This strategy is developed based on the eight rules created by Joseph Granville[6]. When the moving average is below the stock price and in an uptrend, it is time to buy, and vice versa, it is time to sell.

<!-- b000357 | prose | pages [19] -->
The comparison of the curve of daily asset value among those 4 strategies and our strategy is shown in the ﬁgure below.

<!-- b000358 | caption | pages [19] -->
Figure 7: Comparison of the curve of daily asset value among strategies

<!-- b000359 | furniture | pages [20] -->
Team # 2204883

<!-- b000360 | furniture | pages [20] -->
Page 18 of 23

<!-- b000361 | prose | pages [20] -->
To make sure that the 푆푅value is valid for these strategies, we plot the distribution of 퐷푅푅(or, the yield rate) of these strategies, shown in the ﬁgures below.

<!-- b000362 | prose | pages [20] -->
(a) Distribution of our asset (b) Distribution of gold asset (c) Distribution of bitcoin asset

<!-- b000363 | prose | pages [20] -->
(d) Distribution of ideal asset (e) Distribution of rule asset

<!-- b000364 | caption | pages [20] -->
Figure 8: Distribution of 퐷푅푅in the 5 strategies

<!-- b000365 | prose | pages [20] -->
From the distribution we can see that the 퐷푅푅values of all these 5 strategies are subject to normal distribution. Thus, we can calculate 푆푅value for each strategy.

<!-- b000366 | prose | pages [20] -->
Finally the metric values of all strategies considered in this task is calculated and shown in the table below.

<!-- b000367 | prose | pages [20] -->
Strategies \ Metrics ARR PLR NT WR MPA Our Asset 266.36% 1.41 848 53.54% 1044.51 Gold Asset 15.88% 1.08 1 52.38% 80.35 Bitcoin Asset 906.88% 1.15 1 54.28% 7436.2 Ideal Asset 1406.66% 7.55 1401 73.59% 5171.07 Rule Asset 8.53% 1.47 41 21.95% 475.6 Strategies \ Metrics MLA MCP MCL MDD SR Our Asset -867.44 8 7 42.92% 0.0791 Gold Asset -104.85 10 11 18.54% 0.0268 Bitcoin Asset -7742.91 10 9 83.37% 0.078 Ideal Asset -868.93 20 3 1.89% 0.2955 Rule Asset -194.45 1 6 30.06% 0.0247

<!-- b000368 | caption | pages [20] -->
Table 4: Metric values of all strategies

<!-- b000369 | prose | pages [20, 21] -->
Without considering full transparency of future market direction, we can see from the table that the value of 푀퐷퐷and 푀퐿퐴of our model is signiﬁcantly smaller comparing to Bitcoin Asset strategy, proving that our model is more resilient to risks. Besides, our model has a high value of 퐴푅푅compared to Gold Asset strategy and Rule Asset strategy. From the perspective of the value of 푆푅, our model win the second place only behind the ideal model, indicating that our model achieve higher returns for the same risk.

<!-- b000370 | furniture | pages [21] -->
Team # 2204883

<!-- b000371 | furniture | pages [21] -->
Page 19 of 23

<!-- b000373 | heading | pages [21] -->
6 Task 3: Sensitivity of Transaction Costs for The Strategy

<!-- b000374 | prose | pages [21] -->
We analyze the sensitivity of our strategy to the commission of gold transaction and the commission of bitcoin transaction by varying the commission of one asset and keeping the commission of the other asset unchanged alternately. After that, we obtain an investment strategy for each value of commission.

<!-- b000375 | prose | pages [21] -->
When analyzing the sensitivity, we measure the trading behavior by calculating

<!-- b000376 | prose | pages [21] -->
• the average investment percentage when traders invest cash to gold 푣푔,

<!-- b000377 | prose | pages [21] -->
• the average investment percentage when traders invest cash to bitcoin 푣푏,

<!-- b000378 | prose | pages [21] -->
• the number of gold investment 푉푔,

<!-- b000379 | prose | pages [21] -->
• the number of bitcoin investment 푉푏,

<!-- b000380 | prose | pages [21] -->
• the total number of investment 푉푎,

<!-- b000381 | prose | pages [21] -->
under each investment strategy, and evaluate the performance of each investment strategy using two metrics: net proﬁt Δ푤and win rate 푊푅.

<!-- b000382 | heading | pages [21] -->
6.1 Sensitivity of The Commissions of Gold

<!-- b000383 | prose | pages [21] -->
We keep the commission of bitcoin to 2% and set the commission value of gold to 0%, 1%, 2%, 3% and 4% separately and take them into our investment strategy model respectively, and diﬀerent investment strategies are obtained. The trading behaviors are shown in the table below.

<!-- b000384 | prose | pages [21] -->
푣푔 푣푏 푉푔 푉푏 푉푎 Commission of Gold 0% 0.7622 0.8286 6 52 58 1% 0.6333 0.8391 10 40 50 2% 0.9497 0.8307 2 38 40 3% - 0.8223 0 40 40 4% - 0.8255 0 40 40

<!-- b000385 | caption | pages [21] -->
Table 5: Trading behaviors under diﬀerent commissions of gold

<!-- b000386 | prose | pages [21] -->
We ﬁnd that when the commission of gold increases, the average investment percentage when traders invest cash to gold goes up signiﬁcantly and the average investment percentage when traders invest cash to bitcoin stays the same overall. Meanwhile, with the increment of the commission of gold, the number of gold investment drops signiﬁcantly to 0, and the number of bitcoin investment remains unchanged.

<!-- b000387 | prose | pages [21] -->
It can be seen that the increment of the commission of gold has a great impact on trading strategies, as reﬂected in:

<!-- b000388 | prose | pages [21, 22] -->
• The average investment percentage when traders invest cash to gold has increased and the single investment in gold has increased. The reason may be that growth rate of gold is low, and the rise in the commission of gold has increased the threshold for investing in gold, so that a large amount of money will be spent on investing in gold only when the current risk of investing in gold is low enough.

<!-- b000389 | furniture | pages [22] -->
Team # 2204883

<!-- b000390 | furniture | pages [22] -->
Page 20 of 23

<!-- b000392 | prose | pages [22] -->
• Both the number of gold investment and bitcoin investment declined. The reason may be that the rise in the commission of gold makes the model more cautious on investing.

<!-- b000393 | prose | pages [22] -->
Eventually the number of investment in gold drops to 0, which indicates that the prediction of the increase in gold is less than the commission of gold, so the model will not make investment in gold.

<!-- b000394 | prose | pages [22] -->
The corresponding performances of each strategy are shown in the table below.

<!-- b000395 | prose | pages [22] -->
Δ푤 푊푅 Commission of Gold 0% 10874.24 0.2745 1% 14325.13 0.381 2% 13069.35 0.4474 3% 14587.49 0.4103 4% 10865.78 0.4615

<!-- b000396 | caption | pages [22] -->
Table 6: Strategy performances under diﬀerent commissions of gold

<!-- b000397 | prose | pages [22] -->
We ﬁnd that when the commission of gold increases, the net proﬁt remains the same and the win rate shows an upward trend.

<!-- b000398 | prose | pages [22] -->
It can be seen that the increment of the commission of gold has little eﬀect on the results of investment[7].

<!-- b000399 | heading | pages [22] -->
6.2 Sensitivity of The Commissions of Bitcoin

<!-- b000400 | prose | pages [22] -->
We keep the commission of gold to 1% and set the commission value of bitcoin to 1%, 2%, 3%, 4% and 5% separately and take them into our investment strategy model respectively, and diﬀerent investment strategies are obtained. The trading behaviors are shown in the table below.

<!-- b000401 | prose | pages [22] -->
푣푔 푣푏 푉푔 푉푏 푉푎 Commission of Bitcoin 1% 0.5829 0.7921 12 48 60 2% 0.6333 0.8391 10 40 50 3% 0.7622 0.8286 12 42 54 4% 0.785 0.8255 8 44 52 5% 0.7906 0.8245 8 32 40

<!-- b000402 | caption | pages [22] -->
Table 7: Trading behaviors under diﬀerent commissions of bitcoin

<!-- b000403 | prose | pages [22] -->
We ﬁnd that when the commission of bitcoin increases, the average investment percentage when traders invest cash to gold rises signiﬁcantly and the average investment percentage when traders invest cash to bitcoin remains unchanged overall. Meanwhile, with the increment of the commission of bitcoin, both the number of gold investment and the total number of investment decrease.

<!-- b000404 | prose | pages [22] -->
It can be seen that the increment of the commission of bitcoin has a great impact on trading strategies, as reﬂected in:

<!-- b000405 | furniture | pages [23] -->
Team # 2204883

<!-- b000406 | furniture | pages [23] -->
Page 21 of 23

<!-- b000407 | prose | pages [23] -->
• The average investment percentage when traders invest cash to gold increased and the single investment in gold increased. The reason may be that the rise in the commission of bitcoin makes our model more inclined to invest large amounts in gold for the long term.

<!-- b000408 | prose | pages [23] -->
• Both the number of gold investment and bitcoin investment declined. The reason may be that the rise in the commission of bitcoin has made the model more cautious when investing.

<!-- b000409 | prose | pages [23] -->
The corresponding performances of each strategy are shown in the table below.

<!-- b000410 | prose | pages [23] -->
Δ푤 푊푅 Commission of Bitcoin 1% 11632.52 0.4583 2% 14325.13 0.381 3% 2774.01 0.2745 4% 1641.35 0.2954 5% 1583.01 0.303

<!-- b000411 | caption | pages [23] -->
Table 8: Strategy performances under diﬀerent commissions of bitcoin

<!-- b000412 | prose | pages [23] -->
We ﬁnd that when the commission of bitcoin increases, the net proﬁt decreases signiﬁcantly and the win rate shows a decreasing trend.

<!-- b000413 | prose | pages [23] -->
It can be seen that when the commission of bitcoin increases, the win rate and the ﬁnal net proﬁt of the whole trading process decreases, and the trading results become worse.

<!-- b000414 | heading | pages [23] -->
6.3 Analysis of The Result

<!-- b000415 | prose | pages [23] -->
As for the diﬀerence between changing the transaction costs of gold and bitcoin, considering the impact of trading results when the transaction costs change, we believe that:

<!-- b000416 | prose | pages [23] -->
• Gold is a less risky asset, and most investments in gold are long-term investments, so the increase in transaction costs of gold do not have much impact on trading results.

<!-- b000417 | prose | pages [23] -->
• Bitcoin is a risky asset, and the increment in transaction costs of bitcoin makes our strategy more prudent to sell bitcoin and instead, makes predicting of the decline in bitcoin more diﬃcult.

<!-- b000418 | prose | pages [23] -->
As for the similarity of changing the transaction costs of gold and bitcoin, we believe that:

<!-- b000419 | prose | pages [23] -->
• The average percentage of total asset value invested in bitcoin and the number of bitcoin investment have all remained generally unchanged, probably because the short-term growth rate of bitcoin is often extremely high, making it diﬃcult to aﬀect the preference for short-term investments in bitcoin when changing the transaction costs.

<!-- b000420 | prose | pages [23] -->
• Both the number of gold investment and bitcoin investment decline as the transaction costs increase, because the increment of transaction costs makes the strategy more cautious when investing.

<!-- b000421 | prose | pages [23] -->
Therefore, we conclude that investment strategies are more sensitive to changes in bitcoin commissions.

<!-- b000422 | furniture | pages [24] -->
Team # 2204883

<!-- b000423 | furniture | pages [24] -->
Page 22 of 23

<!-- b000424 | heading | pages [24] -->
7 Task 4: Memorandum for The Trader

<!-- b000425 | prose | pages [24] -->
To: Trader in investment markets

<!-- b000426 | prose | pages [24] -->
From: Team # 2204883 of 2022 MCM

<!-- b000427 | prose | pages [24] -->
Date: February 21, 2022

<!-- b000428 | prose | pages [24] -->
Subject: ﬁnd the best investment strategy that maximize total return

<!-- b000429 | prose | pages [24] -->
Dear Sir or Madam:

<!-- b000430 | prose | pages [24] -->
The investment market is volatile, and we believe that all investors, including you, expect to maximize returns while minimizing risk. For this purpose, we analyze the daily price of gold and bitcoin from November 9, 2016 to October 9, 2021. We build two models i.e. Long Short- Term Memory market capitalization forecasting model(LSTM) and multi-objective portfolio investment programming model(MLP). Based on these two models, we are able to maintain a low investment risk while achieving higher returns.

<!-- b000431 | prose | pages [24] -->
First, we build LSTM model to help you accurately predict the future performance of your investment market. Our LSTM model use recurrent neural network to analyze the previous 14 days of market data and predict the market trend of the day, not only to predict the ups and downs, but also to get the exact value. The measurement indicator is the Mean Absolute Percentage Error (MAPE). The results show that our model is very accurate, with a MAPE value of 0.007261 for gold and 0.041630 for bitcoin. With price forecasting, investors can plan their short-term investment strategies in more detail.

<!-- b000432 | prose | pages [24] -->
Moreover, based on the predicted values of the market trend, we develop the MLP model to solve for the investment numbers of gold and bitcoin that satisfy the maximum return and minimum risk by using ideal point method. Considering that there are trading commissions, our results are compared with the future returns of maintaining the existing investments and the optimal solution is selected. After 5 years of trading, we end up with an annualized rate of return of 266.36%, in other words, an increase in assets of about 13 times.

<!-- b000433 | prose | pages [24] -->
According to our analysis of the results, the following are our recommended investment strategies:

<!-- b000434 | prose | pages [24] -->
1. Trust the data from the prediction is accurate and incorporate the programming model’s result into your investment strategy.

<!-- b000435 | prose | pages [24] -->
2. When the market has experienced a big rise and predicted trend is to be plunging, withdraw in time, since our model has predicted most of plunge.

<!-- b000436 | prose | pages [24] -->
3. Too frequent trading is not recommended due to trading commissions.

<!-- b000437 | prose | pages [24] -->
Of course, our data, models and strategies operate only on a daily basis and include only forecasts and asset portfolios based on two asset classes. For daily ﬁnancial transactions, our model can be further extended in the time dimension and portfolio dimension. Thank you for reading our memorandum in your busy schedule, hoping our suggestions are useful to you.

<!-- b000438 | prose | pages [24] -->
Yours Sincerely,

<!-- b000439 | furniture | pages [24] -->
Team # 2204883

<!-- b000440 | furniture | pages [25] -->
Team # 2204883

<!-- b000441 | furniture | pages [25] -->
Page 23 of 23

<!-- b000442 | heading | pages [25] -->
8 Strengths and Weaknesses of Our Strategy

<!-- b000443 | heading | pages [25] -->
8.1 The Price Prediction model

<!-- b000444 | prose | pages [25] -->
• Strengths: The model is based on LSTM model with strong mathematical theory support.

<!-- b000445 | prose | pages [25] -->
Sliding window algorithm is used to reduce errors caused by data redundancy. The optimal combination of parameters is obtained by calculating the 푀퐴푃퐸of the prediction results, which further optimizes the performance of the model.

<!-- b000446 | prose | pages [25] -->
• Weakness: Due to the stochastic nature of the predicting process of LSTM model, we cannot guarantee the optimality of the predicting process.

<!-- b000447 | heading | pages [25] -->
8.2 The Investment Strategy model

<!-- b000448 | prose | pages [25] -->
• Strength: By quantifying return and risk and using the MLP model, an investment strategy that balances return and risk is obtained. Diﬀerent models are built for diﬀerent trading behaviors with a strong focus.

<!-- b000449 | prose | pages [25] -->
• Weakness: When quantifying risk, no adjustment is made to the value of the parameter risk statistical period. This may aﬀect the merit of the model in developing investment strategies.

<!-- b000450 | heading | pages [25] -->
References

<!-- b000451 | references | pages [25] -->
[1] Schabacker, Richard. Technical analysis and stock market proﬁts. Harriman House Lim-

<!-- b000452 | references | pages [25] -->
ited, 2005.

<!-- b000453 | references | pages [25] -->
[2] Bao, Wei, Jun Yue, and Yulei Rao. "A deep learning framework for ﬁnancial time se-

<!-- b000454 | references | pages [25] -->
ries using stacked autoencoders and long-short term memory." PloS one 12.7 (2017):

<!-- b000455 | references | pages [25] -->
e0180944.

<!-- b000456 | references | pages [25] -->
[3] Donckels, Brecht MR, et al. "An ideal point method for the design of compromise experi-

<!-- b000457 | references | pages [25] -->
ments to simultaneously estimate the parameters of rival mathematical models." Chemical

<!-- b000458 | references | pages [25] -->
Engineering Science 65.5 (2010): 1705-1719.

<!-- b000459 | references | pages [25] -->
[4] Zou, Zhichao, and Zihao Qu. "Using LSTM in Stock prediction and Quantitative Trad-

<!-- b000460 | references | pages [25] -->
ing." CS230: Deep Learning, Winter (2020).

<!-- b000461 | references | pages [25] -->
[5] Zopounidis, Constantin, D. K. Despotis, and I. Kamaratou. "Proﬁlio Selection Using the

<!-- b000462 | references | pages [25] -->
Adelais Multiobjective Linear Programming System." Computational Economics 11.3

<!-- b000463 | references | pages [25] -->
(1998): 189-204.

<!-- b000464 | references | pages [25] -->
[6] Granville. New Key to Stock Market Proﬁts. Martino Fine Books, 1963.

<!-- b000465 | references | pages [25] -->
[7] Lv, Dongdong, et al. "An empirical study of machine learning algorithms for stock daily

<!-- b000466 | references | pages [25] -->
trading strategy." Mathematical problems in engineering 2019 (2019).
