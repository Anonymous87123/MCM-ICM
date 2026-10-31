# P-C-2022-2204883-34c13ed1

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
2204883

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Gold Strategy for Gold & Bitcoin traders

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In today’s society, with the continuous development of the economy, more and more people try to increase their income by means of asset investment. However, in the face of a large number of ﬁnancial products in the market, how to accurately predict their price movements, maximize returns and minimize risks through the right way of buying and selling is what every market trader wants to know.

<!-- b000011 | prose | pages [1] -->
A trader who only focus on two ﬁnancial products, gold and bitcoin, comes to us for help. In order to achieve the ambitious goal, we need to come up with a buying and selling plan that maximizes returns and minimize risks by analyzing the previous price data of gold and bitcoin respectively.

<!-- b000012 | prose | pages [1] -->
For task 1, after data preprocessing, we build price prediction models for gold and bitcoin respectively by using LSTM(Long Short-Term Memory), and investment strategy model by using MLP(Multi-objective Linear Programming) to maximize returns and minimize risks simultaneously. The price prediction result of gold reaches an MAPE(Mean Absolute Percentage Error) value of 0.007261 while the price prediction result of bitcoin reaches an MAPE value of 0.041630. Based on the investment strategy model, we develop the best daily trading strategy which ﬁnally makes the initial $1,000 investment worth $14,325.13 on September 10, 2021. The net proﬁt exceeds 13 times of the initial asset.

<!-- b000013 | prose | pages [1] -->
For task 2, we provide evidence that our model gives the best strategy by setting up 10 evaluation metrics and comparing the values of those metrics under 2 simple investment strategies, 1 idealized investment strategy and 1 commonly used investment strategy on the market, and the investment strategy obtained by our model. The result shows that our model develops a strategy with not only a high proﬁt but also a good balance between risk and return.

<!-- b000014 | prose | pages [1] -->
For task 3, We analyze the sensitivity of our strategy to the transaction costs of gold and bitcoin by changing the commission of one asset and keeping the commission of the other asset unchanged alternately. We set 5 metrics to measure the eﬀect on strategies and 2 metrics to measure the eﬀect on results. We ﬁnd that when the commission of gold increases, the net proﬁt remains the same and the win rate shows an upward trend; when the commission of bitcoin increases, the net proﬁt decreases signiﬁcantly and the win rate shows a decreasing trend. Therefore, we conclude that investment strategies are more sensitive to changes in the transaction costs of bitcoin.

<!-- b000015 | prose | pages [1] -->
Finally, we write a memorandum including our strategy, model, and results for the trader. We hope this memorandum will become a valuable reference for him or her further investment.

<!-- b000016 | keywords | pages [1] -->
Keywords: gold, bitcoin, trading strategy, Long Short-Term Memory, Multi-objective Linear

<!-- b000017 | prose | pages [1] -->
Programming, risk and return, sensitivity analysis

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1

<!-- b000020 | heading | pages [2] -->
Introduction

<!-- b000021 | prose | pages [2] -->
2

<!-- b000022 | heading | pages [2] -->
Model Assumptions and Notations

<!-- b000023 | prose | pages [2] -->
1

<!-- b000024 | prose | pages [2] -->
2

<!-- b000025 | prose | pages [2] -->
Assumptions and justiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 2

<!-- b000026 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000027 | heading | pages [2] -->
Notations

<!-- b000028 | prose | pages [2] -->
3 Data Preprocessing

<!-- b000029 | prose | pages [2] -->
2

<!-- b000030 | prose | pages [2] -->
3

<!-- b000031 | prose | pages [2] -->
Task 1: Price Predictions & The Best Trading Strategy 4 3

<!-- b000032 | prose | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 3

<!-- b000033 | prose | pages [2] -->
The Price Prediction Model Based on LSTM . . . . . . . . . . . . . . . . . . . 4.2 4

<!-- b000034 | prose | pages [2] -->
Investment Strategy Model Based on MLP . . . . . . . . . . . . . . . . . . . . 4.3 7

<!-- b000035 | prose | pages [2] -->
The MLP Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 8

<!-- b000036 | prose | pages [2] -->
Investment Strategy Based on The MLP Model . . . . . . . . . . . . . 4.3.2 8

<!-- b000037 | prose | pages [2] -->
The Result of Our Investment Strategy . . . . . . . . . . . . . . . . . . 4.3.3

<!-- b000038 | prose | pages [2] -->
5 Task 2: Proof of The Best Strategy

<!-- b000039 | prose | pages [2] -->
14

<!-- b000040 | prose | pages [2] -->
15

<!-- b000041 | prose | pages [2] -->
Metrics for Evaluating Investment Strategies . . . . . . . . . . . . . . . . . . . 5.1 15

<!-- b000042 | prose | pages [2] -->
Evidence for A Good Investment Strategy . . . . . . . . . . . . . . . . . . . . 5.2 17

<!-- b000043 | heading | pages [2] -->
Task 3: Sensitivity of Transaction Costs for The Strategy

<!-- b000044 | prose | pages [2] -->
6 19

<!-- b000045 | prose | pages [2] -->
Sensitivity of The Commissions of Gold . . . . . . . . . . . . . . . . . . . . . 6.1 19

<!-- b000046 | prose | pages [2] -->
Sensitivity of The Commissions of Bitcoin . . . . . . . . . . . . . . . . . . . . 6.2 20

<!-- b000047 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 Analysis of The Result

<!-- b000048 | prose | pages [2] -->
7

<!-- b000049 | heading | pages [2] -->
Task 4: Memorandum for The Trader

<!-- b000050 | prose | pages [2] -->
21

<!-- b000051 | prose | pages [2] -->
22

<!-- b000052 | heading | pages [2] -->
Strengths and Weaknesses of Our Strategy

<!-- b000053 | prose | pages [2] -->
8 23

<!-- b000054 | prose | pages [2] -->
The Price Prediction model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 23

<!-- b000055 | prose | pages [2] -->
The Investment Strategy model . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 23

<!-- b000056 | furniture | pages [3] -->
Team # 2204883

<!-- b000057 | furniture | pages [3] -->
Page 1 of 23

<!-- b000058 | prose | pages [3] -->
1

<!-- b000059 | heading | pages [3] -->
Introduction

<!-- b000060 | prose | pages [3] -->
In today’s society, with the continuous development of the economy, more and more people want to increase their income by means of asset investment. However, in the face of a large number of ﬁnancial products in the market, how to accurately predict their price movements and maximize returns through the right way of buying and selling is what every market trader wants to know.

<!-- b000061 | prose | pages [3] -->
A trader who only focus on two ﬁnancial products, gold and bitcoin, comes to us for help. In order to achieve the ambitious goal, we need to come up with a buying and selling plan that maximizes returns by analyzing the previous price data of gold and bitcoin respectively.

<!-- b000062 | prose | pages [3] -->
To achieve our goal, we need to:

<!-- b000063 | prose | pages [3] -->
• Pre-process the data provided by COMAP oﬃcial.

<!-- b000064 | prose | pages [3] -->
• Build price prediction models for gold and bitcoin respectively.

<!-- b000065 | prose | pages [3] -->
• Build investment strategy model considering the predicted price of gold and bitcoin and their commissions for each transaction.

<!-- b000066 | prose | pages [3] -->
• Prove that our investment strategy is good enough by calculating strategy evaluation metrics and comparing the value to several other strategies.

<!-- b000067 | prose | pages [3] -->
• Analyze the sensitivity of our strategy to transaction costs by changing the commission value of gold and bitcoin.

<!-- b000068 | prose | pages [3] -->
• Write a memorandum including our strategy, model and results for the trader as a reference for his or her investment.

<!-- b000069 | prose | pages [3] -->
Our modeling framework can be illustrated as shown in Figure 1.

<!-- b000070 | caption | pages [3] -->
Figure 1: Modeling framework

<!-- b000071 | furniture | pages [4] -->
Team # 2204883

<!-- b000072 | furniture | pages [4] -->
Page 2 of 23

<!-- b000073 | prose | pages [4] -->
2

<!-- b000074 | heading | pages [4] -->
Model Assumptions and Notations

<!-- b000075 | prose | pages [4] -->
2.1

<!-- b000076 | heading | pages [4] -->
Assumptions and justiﬁcation

<!-- b000077 | prose | pages [4] -->
• The data provided in this problem is valid and reliable.

<!-- b000078 | prose | pages [4] -->
• There is no minimum purchase limit for both gold and bitcoin.

<!-- b000079 | prose | pages [4] -->
By visiting the oﬃcial website of London Bullion Market, we learned that the minimum purchase limit of gold on the trading market is one lot, i.e. 100 troy ounces, yet the initial capital of the trader in this problem cannot even buy 1 troy ounce of gold, so we made the assumption above.

<!-- b000080 | prose | pages [4] -->
• The inﬂation of the U.S. dollar can be ignored.

<!-- b000081 | prose | pages [4] -->
Although the inﬂation rate of the U.S. dollar is objectively existed, the inﬂation rate of the U.S. dollar over the past 5 years is not provided in this problem, so we default that the value of the U.S. dollar has not changed over the 5 years when calculating the ﬁnal return of the investment.

<!-- b000082 | prose | pages [4] -->
• We do not make any investments in the ﬁrst several days from September 11, 2016.

<!-- b000083 | prose | pages [4] -->
Although our model can give a prediction value, we do not make any investment because we can only refer to the price data up to that day and the training set data is too small in the ﬁrst few days, which can easily lead to a poor prediction result.

<!-- b000084 | prose | pages [4] -->
• The change of the commission costs does not inﬂuence the daily value of gold and bitcoin.

<!-- b000085 | prose | pages [4] -->
Since we need to determine the sensitivity of our strategy to transaction costs, we have to change the value of the commission of gold and bitcoin and see if the strategy changes or not. Therefore we need to assume that the daily values of gold and bitcoin do not change when the commission costs are changed.

<!-- b000086 | prose | pages [4] -->
• The daily value of gold and bitcoin is the value we buy or sell gold and bitcoin on that day.

<!-- b000087 | prose | pages [4] -->
Although in real life the prices of both gold and bitcoin ﬂuctuate over the course of a day, since the problem does not provide more detailed data, we have to make this assumption.

<!-- b000088 | prose | pages [4] -->
• In the price prediction model, both prediction of gold price and bitcoin reach the best result under a same parameter combination.

<!-- b000089 | prose | pages [4] -->
• The prices of gold and bitcoin do not aﬀect each other.

<!-- b000090 | prose | pages [4] -->
We believe that gold prices and bitcoin prices are independent of each other.

<!-- b000091 | prose | pages [4] -->
2.2

<!-- b000092 | heading | pages [4] -->
Notations

<!-- b000093 | prose | pages [4] -->
In this work, we use the nomenclature in Table 1 in the model construction. Other none- frequent-used symbols will be introduced once they are used.

<!-- b000094 | furniture | pages [5] -->
Team # 2204883

<!-- b000095 | prose | pages [5] -->
Symbols Deﬁnitions 푏 bias vector of LSTM 퐶 memory cell value of LSTM ˜퐶 candidate value of memory cell 푑 sliding window size

<!-- b000096 | prose | pages [5] -->
′

<!-- b000097 | prose | pages [5] -->
푑

<!-- b000098 | prose | pages [5] -->
training sliding window size 푓 output function of forget gate ℎ hidden state of LSTM 푖 input function of forget gate 퐿 loss of one single trade 푙 hidden layer size of RNN 푀 total number of trades 푚 number of proﬁtable trades 표 output function of forget gate

<!-- b000099 | furniture | pages [5] -->
Page 3 of 23

<!-- b000100 | prose | pages [5] -->
Symbols Deﬁnitions 푃 푃 proﬁt of one single trade 푟 푟 price of an asset 푆 푆 risk of purchasing 푡 푡 data of trading

<!-- b000101 | prose | pages [5] -->
푉 푉 number of investment 푣 푣 average percentage of assets invested 푊 푊 weight matrix of LSTM 푤 푤 total worth of assets 훼 훼 commission for each transaction 휖 휖 epoch of RNN 휆 휆 learning rate of RNN 휎 휎 Sigmoid function 휔 휔 optimal value of objective function

<!-- b000102 | caption | pages [5] -->
Table 1: Symbol list

<!-- b000103 | prose | pages [5] -->
3 Data Preprocessing

<!-- b000104 | prose | pages [5] -->
Sincewe are only allowed to use thedatasets ’LBMA-GOLD.csv’ and ’BCHAIN-MKPRU.csv’ provided by COMAP oﬃcial, we need to pre-process the data for both datasets before solving the problem.

<!-- b000105 | prose | pages [5] -->
Notice that there is no missing value in the bitcoin price dataset ’BCHAIN-MKPRU.csv’, however in the gold price dataset ’LBMA-GOLD.csv’, there are 10 trading days with missing price data, except for the non-trading days which do not appear in the dataset.

<!-- b000106 | prose | pages [5] -->
To facilitate the follow-up process, and to ensure the reliability and reasonableness of the data, we take the average of the prices of the two trading days before and after each trading day with missing gold price as the gold price of that day. The trading days with missing gold price and their corrected gold prices are shown in the table below.

<!-- b000107 | prose | pages [5] -->
Date Gold Price(Corrected) 12/23/16 1132.975 12/30/16 1148.45 12/22/17 1271.975 12/29/17 1301.525 12/24/18 1263.075 Date Gold Price(Corrected) 12/31/18 1280.95 12/24/19 1496.8 12/31/19 1520.925 12/24/20 1874.65 12/31/20 1915.4

<!-- b000108 | caption | pages [5] -->
Table 2: Trading days with missing gold price and corrected gold price

<!-- b000109 | prose | pages [5] -->
Task 1: Price Predictions & The Best Trading Strategy 4

<!-- b000110 | prose | pages [5] -->
4.1 Problem Analysis

<!-- b000111 | prose | pages [5] -->
In this task, our goal is to develop a daily trading strategy based on the price data from previous days. However, the real investment behavior is implemented based on the expectations for the following days. That is, before we can develop a daily trading strategy, we need to make

<!-- b000112 | furniture | pages [6] -->
Team # 2204883

<!-- b000113 | furniture | pages [6] -->
Page 4 of 23

<!-- b000114 | prose | pages [6] -->
price predictions for gold and bitcoin for the following days respectively. Therefore, the answer to this task needs to consist of the following two steps:

<!-- b000115 | prose | pages [6] -->
• Step 1: Predict the price changes of gold and bitcoin in the following days based on the price data from the previous days.

<!-- b000116 | prose | pages [6] -->
Since the price ﬂuctuations of gold and bitcoin are time-series in nature, we decide to use a time-series based model to predict the prices of gold and bitcoin respectively.

<!-- b000117 | prose | pages [6] -->
• Step 2: Develop a strategy based on the predicted price using an investment strategy model.

<!-- b000118 | prose | pages [6] -->
4.2

<!-- b000119 | heading | pages [6] -->
The Price Prediction Model Based on LSTM

<!-- b000120 | prose | pages [6] -->
LSTM(Long Short-Term Memory) is a special type of RNN(Recurrent Neural Net- work), which solves the problem of gradient explosion and gradient disappearance during the training of RNNs in long sequences, i.e., when the number of layers of the network increases, the subsequent nodes become less perceptive of the previous nodes, and the phenomenon of forgetting the previous information over time occurs[1][2].

<!-- b000121 | prose | pages [6] -->
Based on RNN, LSTM adds a memory unit to each neural unit in the hidden layer: an information transmission belt called "cell state", and uses structures such as forget gates, input gates, and output gates to control the memory information on the time series[3][4]. In this way, LSTM can dig deeper into the potential patterns between data and make the prediction more accurate and reliable. We are now going to introduce the function of each gate.

<!-- b000122 | caption | pages [6] -->
Figure 2: Workﬂow of LSTM

<!-- b000123 | prose | pages [6] -->
i. Forget Gate

<!-- b000124 | prose | pages [6] -->
The function of the forget gate is to selectively forget certain information from the past. LSTM uses the Sigmoid function to achieve the goal. The Sigmoid function is shown below:

<!-- b000125 | prose | pages [6] -->
1 휎(푥) = (1) 1 + 푒−푥

<!-- b000126 | prose | pages [6] -->
In the forget gate, the information of the hidden state of the previous moment (t-1 moment) ℎ푡−1 is input into the Sigmoid function together with the data of this moment (t moment) 푥푡, and

<!-- b000127 | furniture | pages [7] -->
Team # 2204883

<!-- b000128 | furniture | pages [7] -->
Page 5 of 23

<!-- b000129 | prose | pages [7] -->
the output value is between 0 and 1, which indicates whether we should forget this information. The closer the output value is to 0, the more the probability we should forget this information and vice versa. The output function of the forget gate is shown below:

<!-- b000130 | prose | pages [7] -->
푓푡= 휎(푊푓· [ℎ푡−1, 푥푡] + 푏푓) (2)

<!-- b000131 | prose | pages [7] -->
in which [ℎ푡−1, 푥푡] is the concatenated vector of ℎ푡−1 and 푥푡, 푊푓is the weight matrix for the forget gate in RNN which adjust the dimension of the concatenated vector, and 푏푓is the bias vector for the forget gate in RNN. The output value 푓푡will destine whether we should forget the previous memory cell value 퐶푡−1 in the input gate.

<!-- b000132 | prose | pages [7] -->
ii. Input Gate

<!-- b000133 | prose | pages [7] -->
The function of the input gate is to selectively memorize certain information from the past and to decide the value of the current memory cell 퐶푡.

<!-- b000134 | prose | pages [7] -->
In the input gate, two intermediate variables are generated: the output value of input gate 푖푡, shown in equation (3):

<!-- b000135 | prose | pages [7] -->
푖푡= 휎(푊푖· [ℎ푡−1, 푥푡] + 푏푖) (3)

<!-- b000136 | prose | pages [7] -->
and the candidate memory cell value ˜퐶푡, show in equation (4):

<!-- b000137 | prose | pages [7] -->
˜퐶푡= 푡푎푛ℎ(푊퐶· [ℎ푡−1, 푥푡] + 푏퐶) (4)

<!-- b000138 | prose | pages [7] -->
Same as the output of forget gate, the output value of input gate is between 0 1, which indicates whether we should forget the information of the candidate memory cell value. The closer the output value is to 0, the more the probability we should forget this information and vice versa. Moreover, LSTM model need us to use 푡푎푛ℎ() function to normalize the value of

<!-- b000139 | prose | pages [7] -->
˜퐶푡to (-1, 1).

<!-- b000140 | prose | pages [7] -->
After calculating the intermediate variables, LSTM model need us to combine the output of both forget gate and input gate to generate the ﬁnal value of the current memory cell 퐶푡, and the equation is shown below:

<!-- b000141 | prose | pages [7] -->
퐶푡= 푓푡퐶푡−1 + 푖푡˜퐶푡

<!-- b000142 | prose | pages [7] -->
iii. Output Gate

<!-- b000143 | prose | pages [7] -->
(5)

<!-- b000144 | prose | pages [7] -->
The function of the output gate is to selectively generate the value of the current hidden state ℎ푡. The output value of the output gate 표푡plays the role as an intermediate variable, and we use equation (6) to calculate this value.

<!-- b000145 | prose | pages [7] -->
표푡= 휎(푊표· [ℎ푡−1, 푥푡] + 푏표) (6)

<!-- b000146 | prose | pages [7] -->
in which 푊표is the weight matrix for the output gate in RNN which adjust the dimension of the concatenated vector, and 푏표is the bias vector for the output gate in RNN. The output value 표푡destines the value of the current hidden state ℎ푡in the equation below:

<!-- b000147 | furniture | pages [8] -->
Team # 2204883

<!-- b000148 | furniture | pages [8] -->
Page 6 of 23

<!-- b000149 | prose | pages [8] -->
ℎ푡= 표푡푡푎푛ℎ(퐶푡) (7)

<!-- b000150 | prose | pages [8] -->
With the value of ℎ푡and 퐶푡generated at time 푡, we can iteratively calculate the values at time 푡+ 1 using the functions of the three gates until the time limit is reached and the ﬁnal prediction result is generated.

<!-- b000151 | prose | pages [8] -->
When applying LSTM model to our task, the ﬁrst thing we need to is to determine the input and output of the model. Here we use the Sliding Window Algorithm, that is, when predicting the price of gold and bitcoin for each day, we use only the price data of the previous 푑days before that day as the input to the LSTM model. In the model, each day and its previous

<!-- b000152 | prose | pages [8] -->
′ < 푑) days are used for the training process.

<!-- b000153 | prose | pages [8] -->
′(푑

<!-- b000154 | prose | pages [8] -->
푑

<!-- b000155 | prose | pages [8] -->
After the calculation of the model, we ﬁnally get the predicted value of gold ˆ푟푔,푡and the predicted value of bitcoin ˆ푟푏,푡for each date 푡respectively as the output of the model.

<!-- b000156 | prose | pages [8] -->
The process of executing Sliding Window Algorithm is shown in the ﬁgure below.

<!-- b000157 | caption | pages [8] -->
Figure 3: The process of Sliding Window Algorithm

<!-- b000158 | prose | pages [8] -->
Since in the LSTM model, changes in the hidden layer size 푙, sliding window size 푑, training

<!-- b000159 | prose | pages [8] -->
′, learning rate 휆and the value of epoch 휖will have an impact on the

<!-- b000160 | prose | pages [8] -->
sliding window size 푑

<!-- b000161 | prose | pages [8] -->
prediction results, to easily obtain the best prediction result, we adjust the values of these 5 parameters separately to obtain the MAPE(Mean Absolute Percentage Error) values of gold prediction results under diﬀerent parameter values(since we believe that both prediction of gold price and bitcoin price reach the best result under the same parameter combination). The equation to calculate MAPE value is shown below:

<!-- b000162 | prose | pages [8] -->
푀퐴푃퐸= 1

<!-- b000163 | prose | pages [8] -->
푛

<!-- b000164 | prose | pages [8] -->
푛 푛

<!-- b000165 | prose | pages [8] -->
∥푟푔,푡−ˆ푟푔,푡∥

<!-- b000166 | prose | pages [8] -->
Õ

<!-- b000167 | prose | pages [8] -->
(8)

<!-- b000168 | prose | pages [8] -->
푟푔,푡

<!-- b000169 | prose | pages [8] -->
푡=1 푡=1

<!-- b000170 | prose | pages [8] -->
Initially, we set the value of each parameter as

<!-- b000171 | prose | pages [8] -->
′ = 5, 휆= 0.001, 휖= 50].

<!-- b000172 | prose | pages [8] -->
[푙= 100, 푑= 10, 푑

<!-- b000173 | prose | pages [8] -->
When tuning the parameter, each time we only change the value of one parameter and keep

<!-- b000174 | furniture | pages [9] -->
Team # 2204883

<!-- b000175 | furniture | pages [9] -->
Page 7 of 23

<!-- b000176 | prose | pages [9] -->
the values of other parameters unchanged. The MAPE values of the price prediction of gold are shown in the following table:

<!-- b000177 | prose | pages [9] -->
′ 푀퐴푃퐸

<!-- b000178 | prose | pages [9] -->
푑 푀퐴푃퐸 푑

<!-- b000179 | prose | pages [9] -->
휆 푀퐴푃퐸 0.010315979 7 0.007320101 1 0.007261552 0.0005 0.008678837 0.012500496 10 3 0.0007 0.008465359 0.007261552 5 13 0.011110205 15 0.010985684 0.007261552 0.001 0.008998699 7 0.0015 0.009933032 0.007450314 20 0.010590555 9 0.002 0.010285589

<!-- b000180 | caption | pages [9] -->
Table 3: 푀퐴푃퐸values of the price prediction of gold

<!-- b000181 | prose | pages [9] -->
We found that our prediction model is sensitive to the value of sliding window size

<!-- b000182 | prose | pages [9] -->
′ and learning rate 휆. The 푀퐴푃퐸of gold prediction

<!-- b000183 | prose | pages [9] -->
푑, training sliding window size 푑

<!-- b000184 | prose | pages [9] -->
result reaches the minimum value of 0.007261552 when the values of the parameters reach a combination of

<!-- b000185 | prose | pages [9] -->
′ = 5, 휆= 0.001, 휖= 50],

<!-- b000186 | prose | pages [9] -->
[푙= 100, 푑= 10, 푑

<!-- b000187 | prose | pages [9] -->
so we choose the prediction results under this combination of parameters as the ﬁnal gold and bitcoin price prediction result, which shown in the ﬁgures below.

<!-- b000188 | prose | pages [9] -->
(a) Price of gold (b) Price of bitcoin

<!-- b000189 | caption | pages [9] -->
Figure 4: Predicted price vs real prices

<!-- b000190 | prose | pages [9] -->
The price predictions for both gold and bitcoin are proven to be good by comparing the predicted curve and the real curve of the price of both gold and bitcoin.

<!-- b000191 | heading | pages [9] -->
Investment Strategy Model Based on MLP

<!-- b000192 | prose | pages [9] -->
4.3

<!-- b000193 | prose | pages [9] -->
We now have the daily price prediction for gold and bitcoin. Next we will develop our investment strategy from September 11, 2016 based on these prediction results.

<!-- b000194 | prose | pages [9] -->
Since in the price prediction model we need to forecast the price for each trading day based on the price data of the previous 10 trading days from that trading day, we do not make any investments during the ﬁrst 10 trading days of gold(that is, the ﬁrst 14 trading days of bitcoin) of this 5-year period of investment, i.e. September 11, 2016 - September 24, 2016.

<!-- b000195 | prose | pages [9] -->
Noting that we have already obtained daily price prediction for gold and bitcoin, an intuitive investment strategy would be to make the most proﬁtable investment each day based on the

<!-- b000196 | furniture | pages [10] -->
Team # 2204883

<!-- b000197 | furniture | pages [10] -->
Page 8 of 23

<!-- b000198 | prose | pages [10] -->
forecast. For example, if we predict that the growth rate of bitcoin on the next day is greater than the growth rate of gold and also greater than the commission required when purchasing bitcoin, we would turn all of our assets into bitcoins. However, the fact is that the predicted price values are diﬀerent from the true values, especially when the predicted and real values are moving in opposite trends, making investment based on such strategy will be more risky.

<!-- b000199 | prose | pages [10] -->
Therefore, in order to get the best investment strategy, we need to consider both the possible proﬁts and the potential risks associated with the investment strategy. Here we use an MLP(Multi-objective Linear Programming) model to solve the problem.

<!-- b000200 | prose | pages [10] -->
4.3.1

<!-- b000201 | heading | pages [10] -->
The MLP Model

<!-- b000202 | prose | pages [10] -->
MLP(Multi-objective Linear Programming) is one of the most important elements of In multi-objective decision making, a multi-objective multi-objective decision making[5]. linear programming problem is formed when it is desired that each objective is as large (or as small) as possible. A general form of an m-objective linear programming problem should be:

<!-- b000203 | prose | pages [10] -->
푓(푥) = [ 푓1(푥), 푓2(푥), ..., 푓푚(푥)]푇, 푚푖푛

<!-- b000204 | prose | pages [10] -->
(

<!-- b000205 | prose | pages [10] -->
푔푖(푥) ≤0,

<!-- b000206 | prose | pages [10] -->
푠.푡.

<!-- b000207 | prose | pages [10] -->
ℎ푗(푥) = 0, 푖= 1, 2, ..., 푝, 푗= 1, 2, ..., 푞.

<!-- b000208 | prose | pages [10] -->
in which 푓1(푥), 푓2(푥), ..., 푓푚(푥) stand for 푚objective functions, 푔푖(푥), ℎ푗(푥) stand for the constraints of the objective functions.

<!-- b000209 | prose | pages [10] -->
In order to solve this problem, we apply the ideal point method. This method requires us to split the multi-objective linear programming problem into multiple single-objective linear programming problems and separately obtain the optimal values of each objective function:

<!-- b000210 | prose | pages [10] -->
휔1, 휔2, ..., 휔푚.

<!-- b000211 | prose | pages [10] -->
After that, we construct the sum of squares of the diﬀerence between each objective func- tion and the optimal value as a new objective function. By solving the following quadratic programming problem:

<!-- b000212 | prose | pages [10] -->
푚 Õ

<!-- b000213 | prose | pages [10] -->
푚푖푛 푓=

<!-- b000214 | prose | pages [10] -->
푖=1

<!-- b000215 | prose | pages [10] -->
(

<!-- b000216 | prose | pages [10] -->
푔푖(푥) ≤0,

<!-- b000217 | prose | pages [10] -->
푠.푡.

<!-- b000218 | prose | pages [10] -->
ℎ푗(푥) = 0,

<!-- b000219 | prose | pages [10] -->
( 푓푖(푥) −휔푖)2 (9)

<!-- b000220 | prose | pages [10] -->
푖= 1, 2, ..., 푝, 푗= 1, 2, ..., 푞.

<!-- b000221 | prose | pages [10] -->
Finally we could obtain the optimal solution 푥표푝푡for the original multi-objective linear programming problem by this mean.

<!-- b000222 | heading | pages [10] -->
Investment Strategy Based on The MLP Model

<!-- b000223 | prose | pages [10] -->
4.3.2

<!-- b000224 | prose | pages [10] -->
We synthesize the methods of multi-objective linear programming and optimal portfolio formulation, determine the decision variables, objective function, and constraints of the plan- ning problem respectively, and obtain a model that helps us develop a daily investment strategy.

<!-- b000225 | furniture | pages [11] -->
Team # 2204883

<!-- b000226 | furniture | pages [11] -->
Page 9 of 23

<!-- b000227 | prose | pages [11] -->
Since the model integrates the predicted prices of gold and bitcoin for the next trading day and the respective investment risks, the model can be well applied to develop an investment strategy for each trading day.

<!-- b000228 | prose | pages [11] -->
To begin with, we simplify the development of an investment strategy as follows:

<!-- b000229 | prose | pages [11] -->
The worth values of cash, gold and bitcoin at the end of date 푡are noted as

<!-- b000230 | prose | pages [11] -->
[푥푐, 푥푔, 푥푏]

<!-- b000231 | prose | pages [11] -->
all in U.S. dollar, in which 푥푔equals to the product of the amount of gold(in troy ounce) and the price of gold per troy ounce, 푥푏equals to the product of the amount of bitcoin(in number) and the price of bitcoin per single bitcoin. According to the predicted price of gold(noted as ˆ푟푔,푡+1) and the predicted price of bitcoin(noted as ˆ푟푏,푡+1) on the coming day, the assets are purchased and sold to get a new portfolio noted as

<!-- b000232 | prose | pages [11] -->
′

<!-- b000233 | prose | pages [11] -->
[푥

<!-- b000234 | prose | pages [11] -->
푐, 푥

<!-- b000235 | prose | pages [11] -->
′ ′

<!-- b000236 | prose | pages [11] -->
′

<!-- b000237 | prose | pages [11] -->
푔, 푥

<!-- b000238 | prose | pages [11] -->
푏]

<!-- b000239 | prose | pages [11] -->
in U.S. Dollar, which maximizes the return(noted as 푃) while minimizing the investment risk(noted as 푅).

<!-- b000240 | prose | pages [11] -->
After that, we deﬁne the investment risk 푅for the coming day(date 푡+ 1) as

<!-- b000241 | prose | pages [11] -->
′

<!-- b000242 | prose | pages [11] -->
′

<!-- b000243 | prose | pages [11] -->
푔−푥푔)푆푔+ (푥

<!-- b000244 | prose | pages [11] -->
푅= (푥

<!-- b000245 | prose | pages [11] -->
in which

<!-- b000246 | prose | pages [11] -->
s

<!-- b000247 | prose | pages [11] -->
10Í

<!-- b000248 | prose | pages [11] -->


<!-- b000249 | prose | pages [11] -->
푏−푥푏)푆푏 (10)

<!-- b000250 | prose | pages [11] -->
10Í

<!-- b000251 | prose | pages [11] -->
(푟푔푗−¯푟푔푗)2,

<!-- b000252 | prose | pages [11] -->
푆푔=

<!-- b000253 | prose | pages [11] -->
1 9

<!-- b000254 | prose | pages [11] -->
푗=1

<!-- b000255 | prose | pages [11] -->
s

<!-- b000256 | prose | pages [11] -->
10Í

<!-- b000257 | prose | pages [11] -->


<!-- b000258 | prose | pages [11] -->
푆푏=

<!-- b000259 | prose | pages [11] -->
¯푟푔푗= 1

<!-- b000260 | prose | pages [11] -->
푟푔푗

<!-- b000261 | prose | pages [11] -->
10

<!-- b000262 | prose | pages [11] -->
푗=1

<!-- b000263 | prose | pages [11] -->
10Í

<!-- b000264 | prose | pages [11] -->
(푟푏푗−¯푟푏푗)2,

<!-- b000265 | prose | pages [11] -->
1 9

<!-- b000266 | prose | pages [11] -->
푗=1

<!-- b000267 | prose | pages [11] -->
¯푟푏푗= 1

<!-- b000268 | prose | pages [11] -->
푟푏푗

<!-- b000269 | prose | pages [11] -->
10

<!-- b000270 | prose | pages [11] -->
푗=1

<!-- b000271 | prose | pages [11] -->
where 푆푔and 푆푏stand for the risk of purchasing gold and bitcoin on date 푡+ 1 respectively, 푟푔푗and 푟푏푗stand for the price value the gold and bitcoin 푗days before date 푡+ 1 respectively.

<!-- b000272 | prose | pages [11] -->
On the other hand, the predicted return 푃for the coming day(date 푡+ 1) is calculated as

<!-- b000273 | prose | pages [11] -->
푃= ( ˆ푟푔,푡+1 −푟푔,푡

<!-- b000274 | prose | pages [11] -->
푔−푥푔) + ( ˆ푟푏,푡+1 −푟푏,푡 ′

<!-- b000275 | prose | pages [11] -->
) · (푥

<!-- b000276 | prose | pages [11] -->
푟푔,푡

<!-- b000277 | prose | pages [11] -->
′

<!-- b000278 | prose | pages [11] -->
) · (푥

<!-- b000279 | prose | pages [11] -->
푏−푥푏) (11)

<!-- b000280 | prose | pages [11] -->
푟푏,푡

<!-- b000281 | prose | pages [11] -->
in which 푟푔,푡and 푟푏,푡stand for the true value of gold and bitcoin at the end of date 푡. Combining the predicted returns and risks, we now obtain the objective function as the form of

<!-- b000282 | prose | pages [11] -->
푚푎푥 푃,

<!-- b000283 | prose | pages [11] -->
and can be also written as

<!-- b000284 | prose | pages [11] -->
푚푖푛 푅

<!-- b000285 | furniture | pages [12] -->
Team # 2204883

<!-- b000286 | prose | pages [12] -->
푚푖푛

<!-- b000287 | furniture | pages [12] -->
Page 10 of 23

<!-- b000288 | prose | pages [12] -->
−푃, 푅

<!-- b000289 | prose | pages [12] -->
Now we turn our attention to the trading behavior, for both gold and bitcoin, there are six trading behaviors: purchasing both gold and bitcoin, purchasing gold and selling bitcoin, selling gold and purchasing bitcoin, selling both gold and bitcoin, purchasing bitcoin on non-trading days for gold, and selling bitcoin on non-trading days for gold. Noting that the constraints of the multi-objective linear programming model is diﬀerent among trading behaviors, we build MLP models for each trading behavior separately.

<!-- b000290 | prose | pages [12] -->
For further processing, we note the amount of U.S. dollar spent/received when trading gold and bitcoin as Δ푥푔and Δ푥푏respectively, an obvious constraint for each model is:

<!-- b000291 | prose | pages [12] -->
′ 푐= 푥푐−Δ푥푔−Δ푥푏

<!-- b000292 | prose | pages [12] -->
푥

<!-- b000293 | prose | pages [12] -->
(12)

<!-- b000294 | prose | pages [12] -->
Also, we note the commission for trading gold and bitcoin as 훼푔= 1% and 훼푏= 2% respectively instead of using their lengthy form 훼푔표푙푑and 훼푏푖푡푐표푖푛.

<!-- b000295 | prose | pages [12] -->
i. Purchasing both gold and bitcoin

<!-- b000296 | prose | pages [12] -->
This trading behavior can be noted as

<!-- b000297 | prose | pages [12] -->
Δ푥푔> 0, Δ푥푏> 0

<!-- b000298 | prose | pages [12] -->
′

<!-- b000299 | prose | pages [12] -->
′ 푏−푥푏can be substituted as

<!-- b000300 | prose | pages [12] -->
Since the value of 푥

<!-- b000301 | prose | pages [12] -->
푔−푥푔and 푥

<!-- b000302 | prose | pages [12] -->
(

<!-- b000303 | prose | pages [12] -->
′ 푔−푥푔= (1 −훼푔)Δ푥푔

<!-- b000304 | prose | pages [12] -->
푥

<!-- b000305 | prose | pages [12] -->
′ 푏−푥푏= (1 −훼푏)Δ푥푏

<!-- b000306 | prose | pages [12] -->
푥

<!-- b000307 | prose | pages [12] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000308 | prose | pages [12] -->
−ˆ푟푔,푡+1 −푟푔,푡

<!-- b000309 | prose | pages [12] -->
· (1 −훼푔)Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡

<!-- b000310 | prose | pages [12] -->
푚푖푛

<!-- b000311 | prose | pages [12] -->
푟푔,푡

<!-- b000312 | prose | pages [12] -->
· (1 −훼푏)Δ푥푏

<!-- b000313 | prose | pages [12] -->
푟푏,푡

<!-- b000314 | prose | pages [12] -->
(1 −훼푔)Δ푥푔푆푔+ (1 −훼푏)Δ푥푏푆푏 푚푖푛

<!-- b000315 | prose | pages [12] -->
Δ푥푔+ Δ푥푏< 푥푐

<!-- b000316 | prose | pages [12] -->


<!-- b000317 | prose | pages [12] -->
푠.푡.

<!-- b000318 | prose | pages [12] -->
Δ푥푔> 0 Δ푥푏> 0

<!-- b000319 | prose | pages [12] -->


<!-- b000320 | prose | pages [12] -->
ii. Purchasing gold and selling bitcoin

<!-- b000321 | prose | pages [12] -->
This trading behavior can be noted as

<!-- b000322 | prose | pages [12] -->
Δ푥푔> 0, Δ푥푏≤0

<!-- b000323 | furniture | pages [13] -->
Team # 2204883

<!-- b000324 | prose | pages [13] -->
′

<!-- b000325 | prose | pages [13] -->
′

<!-- b000326 | prose | pages [13] -->
Since the value of 푥

<!-- b000327 | prose | pages [13] -->
푔−푥푔and 푥

<!-- b000328 | furniture | pages [13] -->
Page 11 of 23

<!-- b000329 | prose | pages [13] -->
푏−푥푏can be substituted as

<!-- b000330 | prose | pages [13] -->
(

<!-- b000331 | prose | pages [13] -->
′ 푔−푥푔= (1 −훼푔)Δ푥푔

<!-- b000332 | prose | pages [13] -->
푥

<!-- b000333 | prose | pages [13] -->
′ ′ 1−훼푏Δ푥푏, 0 ≤푥

<!-- b000334 | prose | pages [13] -->
푥

<!-- b000335 | prose | pages [13] -->
푏−푥푏= 1 푏

<!-- b000336 | prose | pages [13] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000337 | prose | pages [13] -->
−ˆ푟푔,푡+1 −푟푔,푡

<!-- b000338 | prose | pages [13] -->
· (1 −훼푔)Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡

<!-- b000339 | prose | pages [13] -->
푚푖푛

<!-- b000340 | prose | pages [13] -->
푟푔,푡

<!-- b000341 | prose | pages [13] -->
1 Δ푥푏 ·

<!-- b000342 | prose | pages [13] -->
푟푏,푡

<!-- b000343 | prose | pages [13] -->
1 −훼푏

<!-- b000344 | prose | pages [13] -->
1 (1 −훼푔)Δ푥푔푆푔+ 푚푖푛 Δ푥푏푆푏 1 −훼푏

<!-- b000345 | prose | pages [13] -->
Δ푥푔+ Δ푥푏< 푥푐

<!-- b000346 | prose | pages [13] -->


<!-- b000347 | prose | pages [13] -->
Δ푥푔> 0

<!-- b000348 | prose | pages [13] -->
푠.푡.

<!-- b000349 | prose | pages [13] -->
Δ푥푏≤0

<!-- b000350 | prose | pages [13] -->


<!-- b000351 | prose | pages [13] -->
−Δ푥푏< (1 −훼푏)푥푏

<!-- b000352 | prose | pages [13] -->
iii. Selling gold and purchasing bitcoin

<!-- b000353 | prose | pages [13] -->
This trading behavior can be noted as

<!-- b000354 | prose | pages [13] -->
Δ푥푔≤0, Δ푥푏> 0

<!-- b000355 | prose | pages [13] -->
′

<!-- b000356 | prose | pages [13] -->
′ 푏−푥푏can be substituted as

<!-- b000357 | prose | pages [13] -->
Since the value of 푥

<!-- b000358 | prose | pages [13] -->
푔−푥푔and 푥

<!-- b000359 | prose | pages [13] -->
′

<!-- b000360 | prose | pages [13] -->
(

<!-- b000361 | prose | pages [13] -->
푥

<!-- b000362 | prose | pages [13] -->
푔−푥푔= ′ 1−훼푔Δ푥푔, 0 ≤푥 1

<!-- b000363 | prose | pages [13] -->
′

<!-- b000364 | prose | pages [13] -->
푔

<!-- b000365 | prose | pages [13] -->
푏−푥푏= (1 −훼푏)Δ푥푏

<!-- b000366 | prose | pages [13] -->
푥

<!-- b000367 | prose | pages [13] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000368 | prose | pages [13] -->
−ˆ푟푔,푡+1 −푟푔,푡

<!-- b000369 | prose | pages [13] -->
1

<!-- b000370 | prose | pages [13] -->
푚푖푛

<!-- b000371 | prose | pages [13] -->
·

<!-- b000372 | prose | pages [13] -->
푟푔,푡

<!-- b000373 | prose | pages [13] -->
1 −훼푔

<!-- b000374 | prose | pages [13] -->
1

<!-- b000375 | prose | pages [13] -->
Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡

<!-- b000376 | prose | pages [13] -->
· (1 −훼푏)Δ푥푏

<!-- b000377 | prose | pages [13] -->
푟푏,푡

<!-- b000378 | prose | pages [13] -->
Δ푥푔푆푔+ (1 −훼푏)Δ푥푏푆푏 푚푖푛 1 −훼푔

<!-- b000379 | prose | pages [13] -->
Δ푥푔+ Δ푥푏< 푥푐

<!-- b000380 | prose | pages [13] -->


<!-- b000381 | prose | pages [13] -->
Δ푥푔≤0

<!-- b000382 | prose | pages [13] -->
푠.푡.

<!-- b000383 | prose | pages [13] -->
Δ푥푏> 0

<!-- b000384 | prose | pages [13] -->


<!-- b000385 | prose | pages [13] -->
−Δ푥푔< (1 −훼푔)푥푔

<!-- b000386 | prose | pages [13] -->
iv. Selling both gold and bitcoin

<!-- b000387 | furniture | pages [14] -->
Team # 2204883

<!-- b000388 | prose | pages [14] -->
This trading behavior can be noted as

<!-- b000389 | furniture | pages [14] -->
Page 12 of 23

<!-- b000390 | prose | pages [14] -->
Δ푥푔≤0, Δ푥푏≤0

<!-- b000391 | prose | pages [14] -->
′

<!-- b000392 | prose | pages [14] -->
′

<!-- b000393 | prose | pages [14] -->
Since the value of 푥

<!-- b000394 | prose | pages [14] -->
푔−푥푔and 푥

<!-- b000395 | prose | pages [14] -->
푏−푥푏can be substituted as

<!-- b000396 | prose | pages [14] -->
′

<!-- b000397 | prose | pages [14] -->
(

<!-- b000398 | prose | pages [14] -->
′ 1−훼푔Δ푥푔, 0 ≤푥

<!-- b000399 | prose | pages [14] -->
푥

<!-- b000400 | prose | pages [14] -->
푔−푥푔= 1

<!-- b000401 | prose | pages [14] -->
′

<!-- b000402 | prose | pages [14] -->
푔

<!-- b000403 | prose | pages [14] -->
′ 1−훼푏Δ푥푏, 0 ≤푥

<!-- b000404 | prose | pages [14] -->
푥

<!-- b000405 | prose | pages [14] -->
푏−푥푏= 1 푏

<!-- b000406 | prose | pages [14] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000407 | prose | pages [14] -->
−ˆ푟푔,푡+1 −푟푔,푡

<!-- b000408 | prose | pages [14] -->
1

<!-- b000409 | prose | pages [14] -->
푚푖푛

<!-- b000410 | prose | pages [14] -->
·

<!-- b000411 | prose | pages [14] -->
푟푔,푡

<!-- b000412 | prose | pages [14] -->
1 −훼푔

<!-- b000413 | prose | pages [14] -->
1

<!-- b000414 | prose | pages [14] -->
Δ푥푔−ˆ푟푏,푡+1 −푟푏,푡

<!-- b000415 | prose | pages [14] -->
1 Δ푥푏 ·

<!-- b000416 | prose | pages [14] -->
푟푏,푡

<!-- b000417 | prose | pages [14] -->
1 −훼푏

<!-- b000418 | prose | pages [14] -->
1 Δ푥푔푆푔+ 푚푖푛 1 −훼푔 Δ푥푏푆푏 1 −훼푏

<!-- b000419 | prose | pages [14] -->
Δ푥푔+ Δ푥푏< 푥푐

<!-- b000420 | prose | pages [14] -->


<!-- b000421 | prose | pages [14] -->
Δ푥푔≤0

<!-- b000422 | prose | pages [14] -->
푠.푡.

<!-- b000423 | prose | pages [14] -->
Δ푥푏≤0 −Δ푥푔< (1 −훼푔)푥푔

<!-- b000424 | prose | pages [14] -->


<!-- b000425 | prose | pages [14] -->
−Δ푥푏< (1 −훼푏)푥푏

<!-- b000426 | prose | pages [14] -->
v. Purchasing bitcoin on non-trading days for gold

<!-- b000427 | prose | pages [14] -->
This trading behavior can be noted as

<!-- b000428 | prose | pages [14] -->
Δ푥푔= 0, Δ푥푏> 0

<!-- b000429 | prose | pages [14] -->
′

<!-- b000430 | prose | pages [14] -->
′ 푏−푥푏can be substituted as

<!-- b000431 | prose | pages [14] -->
Since the value of 푥

<!-- b000432 | prose | pages [14] -->
푔−푥푔and 푥

<!-- b000433 | prose | pages [14] -->
(

<!-- b000434 | prose | pages [14] -->
′

<!-- b000435 | prose | pages [14] -->
푥

<!-- b000436 | prose | pages [14] -->
푔−푥푔= 0

<!-- b000437 | prose | pages [14] -->
′ 푏−푥푏= (1 −훼푏)Δ푥푏

<!-- b000438 | prose | pages [14] -->
푥

<!-- b000439 | prose | pages [14] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000440 | prose | pages [14] -->
−ˆ푟푏,푡+1 −푟푏,푡 푚푖푛

<!-- b000441 | prose | pages [14] -->
푟푏,푡

<!-- b000442 | prose | pages [14] -->
· (1 −훼푏)Δ푥푏

<!-- b000443 | prose | pages [14] -->
(1 −훼푏)Δ푥푏푆푏 푚푖푛

<!-- b000444 | furniture | pages [15] -->
Team # 2204883

<!-- b000445 | prose | pages [15] -->
(

<!-- b000446 | furniture | pages [15] -->
Page 13 of 23

<!-- b000447 | prose | pages [15] -->
Δ푥푏< 푥푐

<!-- b000448 | prose | pages [15] -->
푠.푡.

<!-- b000449 | prose | pages [15] -->
Δ푥푏> 0

<!-- b000450 | prose | pages [15] -->
vi. Selling bitcoin on non-trading days for gold

<!-- b000451 | prose | pages [15] -->
This trading behavior can be noted as

<!-- b000452 | prose | pages [15] -->
Δ푥푔= 0, Δ푥푏≤0

<!-- b000453 | prose | pages [15] -->
′

<!-- b000454 | prose | pages [15] -->
′ 푏−푥푏can be substituted as

<!-- b000455 | prose | pages [15] -->
Since the value of 푥

<!-- b000456 | prose | pages [15] -->
푔−푥푔and 푥

<!-- b000457 | prose | pages [15] -->
(

<!-- b000458 | prose | pages [15] -->
′

<!-- b000459 | prose | pages [15] -->
푥

<!-- b000460 | prose | pages [15] -->
푔−푥푔= 0

<!-- b000461 | prose | pages [15] -->
′

<!-- b000462 | prose | pages [15] -->
푥

<!-- b000463 | prose | pages [15] -->
푏−푥푏= 1−훼푏Δ푥푏 1

<!-- b000464 | prose | pages [15] -->
According to equation (10), (11) and (12), the MLP model for this trading behavior can be built as:

<!-- b000465 | prose | pages [15] -->
−ˆ푟푏,푡+1 −푟푏,푡 푚푖푛

<!-- b000466 | prose | pages [15] -->
푟푏,푡

<!-- b000467 | prose | pages [15] -->
푚푖푛

<!-- b000468 | prose | pages [15] -->
1 Δ푥푏 · 1 −훼푏

<!-- b000469 | prose | pages [15] -->
1 1 Δ푥푏푆푏 1 −훼푏

<!-- b000470 | prose | pages [15] -->
Δ푥푏< 푥푐

<!-- b000471 | prose | pages [15] -->


<!-- b000472 | prose | pages [15] -->
푠.푡.

<!-- b000473 | prose | pages [15] -->
Δ푥푏≤0 −Δ푥푏< (1 −훼푏)푥푏

<!-- b000474 | prose | pages [15] -->


<!-- b000475 | prose | pages [15] -->
Based on the six models above, we bring the price prediction results of gold and bitcoin into model i-iv for calculation on trading days of gold respectively, and bring the price prediction results of bitcoin into model v-iv for calculation on non-trading days of gold respectively, and choose the most optimal trading behavior as the portfolio for the coming day.

<!-- b000476 | prose | pages [15] -->
It is worth noting that since each trading behavior involves high commissions, even the most optimal trading behavior may cause losses after paying commissions, so we compare the return value when executing the most optimal trading behavior with the return when keeping the portfolio unchanged, if

<!-- b000477 | prose | pages [15] -->
푐+ ˆ푟푔,푡+1

<!-- b000478 | prose | pages [15] -->
푏< 푥푐+ ˆ푟푔,푡+1

<!-- b000479 | prose | pages [15] -->
푔+ ˆ푟푏,푡+1

<!-- b000480 | prose | pages [15] -->
′

<!-- b000481 | prose | pages [15] -->
′

<!-- b000482 | prose | pages [15] -->
′

<!-- b000483 | prose | pages [15] -->
푥

<!-- b000484 | prose | pages [15] -->
푥

<!-- b000485 | prose | pages [15] -->
푥

<!-- b000486 | prose | pages [15] -->
푟푔,푡

<!-- b000487 | prose | pages [15] -->
푟푏,푡

<!-- b000488 | prose | pages [15] -->
푥푔+ ˆ푟푏,푡+1

<!-- b000489 | prose | pages [15] -->
푥푏 (13)

<!-- b000490 | prose | pages [15] -->
푟푔,푡

<!-- b000491 | prose | pages [15] -->
푟푏,푡

<!-- b000492 | prose | pages [15] -->
holds, the portfolio will keep unchanged; otherwise the portfolio will be changed into the most optimal trading behavior given by the model.

<!-- b000493 | furniture | pages [16] -->
Team # 2204883

<!-- b000494 | furniture | pages [16] -->
Page 14 of 23

<!-- b000495 | prose | pages [16] -->
4.3.3

<!-- b000496 | heading | pages [16] -->
The Result of Our Investment Strategy

<!-- b000497 | prose | pages [16] -->
We take the initial worth values of cash, gold and bitcoin at September 25, 2016 , since we do not make any investment in the very beginning 14 days’ period, as

<!-- b000498 | prose | pages [16] -->
[푥푐, 푥푔, 푥푏] = [1000, 0, 0],

<!-- b000499 | prose | pages [16] -->
and the predicted value of gold and bitcoin on that day as the input of our investment strategy model. We calculate the optimal portfolio for each day with a combination of the predicted price of gold and bitcoin and the investment strategy model. The date we buy or sell bitcoin from January 1, 2017 to January 1, 2018, as an example under our investment strategy, is shown in the ﬁgure below.

<!-- b000500 | caption | pages [16] -->
Figure 5: Date to buy or sell bitcoin, from Jan.1, 2017 to Jan.1, 2018

<!-- b000501 | prose | pages [16] -->
Finally we discount the total asset value of each day by the closing price of gold and bitcoin for each day and obtain a line graph of daily assets.

<!-- b000502 | caption | pages [16] -->
Figure 6: Curve of daily asset value

<!-- b000503 | prose | pages [16] -->
The result is: by using our model and strategy, ﬁnally the initial $1,000 investment worth $14,325.13 on September 10, 2021, which makes a proﬁt more than 13 times of the initial investment.

<!-- b000504 | furniture | pages [17] -->
Team # 2204883

<!-- b000505 | furniture | pages [17] -->
Page 15 of 23

<!-- b000506 | prose | pages [17] -->
Task 2: Proof of The Best Strategy 5

<!-- b000507 | prose | pages [17] -->
In Task 1, we have already built the price prediction model as well as the investment strategy model and have obtained the most optimal investment strategy for each day of the 5-year period from September 11, 2016 to September 10, 2021.

<!-- b000508 | prose | pages [17] -->
Now we set up some evaluation metrics and proved that the investment strategy obtained by our model is the best by comparing the values of these metrics under 2 simple investment strategies (a 5-year long-term investment in gold, a 5-year long-term investment in bitcoin) , 1 idealized investment strategy and 1 commonly used investment strategy on the market, as well as under the investment strategy obtained by our model.

<!-- b000509 | prose | pages [17] -->
Metrics for Evaluating Investment Strategies 5.1

<!-- b000510 | prose | pages [17] -->
We set up 10 metrics for investment strategy evaluation.

<!-- b000511 | prose | pages [17] -->
i. ARR(Annualized Rate of Return)

<!-- b000512 | prose | pages [17] -->
ARR is a theoretical rate of return calculated by converting the current daily rate of return into an annualized rate of return. It is calculated from the equation

<!-- b000513 | prose | pages [17] -->
퐴푅푅= 푤푡−푤0

<!-- b000514 | prose | pages [17] -->
푤0

<!-- b000515 | prose | pages [17] -->
× 365

<!-- b000516 | prose | pages [17] -->
× 100% 푡

<!-- b000517 | prose | pages [17] -->
in which 푤푡means the worth of your assets on day 푡and 푤0 means the worth of your initial investment.

<!-- b000518 | prose | pages [17] -->
ii. PLR(Proﬁt/Loss Ratio)

<!-- b000519 | prose | pages [17] -->
PLR is the ratio of proﬁt to loss for each trade in a period of investment. Suppose that 푚 trades make proﬁt(푃푖for each) and 푛trades loss(퐿푗for each) in a period of investment, the PLR is calculated from the equation below.

<!-- b000520 | prose | pages [17] -->
푃퐿푅=

<!-- b000521 | prose | pages [17] -->
iii. NT(Number of Trade))

<!-- b000522 | prose | pages [17] -->
푚Í

<!-- b000523 | prose | pages [17] -->
푃푖

<!-- b000524 | prose | pages [17] -->
푖=1

<!-- b000525 | prose | pages [17] -->
푛Í

<!-- b000526 | prose | pages [17] -->
퐿푗

<!-- b000527 | prose | pages [17] -->
푗=1

<!-- b000528 | prose | pages [17] -->
NT stands for the total amount of trades in a period of investment. We deﬁne the process from opening a position to closing a position as a single trade.

<!-- b000529 | prose | pages [17] -->
iv. WR(Win Rate)

<!-- b000530 | prose | pages [17] -->
WR measures the number of proﬁtable trades as a percentage of the total number of trades. Suppose that there are 푀trades in a period of investment and in which 푚trades make proﬁt, the WR is calculated from the equation below.

<!-- b000531 | prose | pages [17] -->
푊푅= 푚

<!-- b000532 | prose | pages [17] -->
푀× 100%

<!-- b000533 | prose | pages [17] -->
v. MPA(Maximum Proﬁt Amount)

<!-- b000534 | furniture | pages [18] -->
Team # 2204883

<!-- b000535 | furniture | pages [18] -->
Page 16 of 23

<!-- b000536 | prose | pages [18] -->
MPA measures the maximum proﬁt value of a single trade in a period of investment. Suppose that 푚trades make proﬁt(푃푖for each) in a period of investment, MPA can be calculated as follow.

<!-- b000537 | prose | pages [18] -->
푀푃퐴= 푚푎푥{푃푖}

<!-- b000538 | prose | pages [18] -->
vi. MLA(Maximum Loss Amount)

<!-- b000539 | prose | pages [18] -->
MLA measures the maximum loss value of a single trade in a period of investment. Suppose that 푛trades loss(퐿푗for each, 퐿푗< 0) in a period of investment, MLA can be calculated as follow.

<!-- b000540 | prose | pages [18] -->
푀퐿퐴= 푚푖푛{퐿푗}

<!-- b000541 | prose | pages [18] -->
vii. MCP(Maximum umber of Consecutive Proﬁts)

<!-- b000542 | prose | pages [18] -->
MCP is the maximum number of consecutive proﬁtable trades in a period of investment.

<!-- b000543 | prose | pages [18] -->
viii. MCL(Maximum umber of Consecutive Losses)

<!-- b000544 | prose | pages [18] -->
MCL is the maximum number of consecutive lossing trades in a period of investment.

<!-- b000545 | prose | pages [18] -->
ix. MDD(Maximum Drawdown)

<!-- b000546 | prose | pages [18] -->
MDD is the maximum observed loss from a peak to a trough of a portfolio during the period of investment. It is an indicator of downside risk over the period of investment.

<!-- b000547 | prose | pages [18] -->
x. SR(Sharpe Ratio)

<!-- b000548 | prose | pages [18] -->
SR is one of the most commonly used metrics in strategy evaluation, and it is one of the most valuable performance metrics considering both return and risk. For a good strategy, the larger the value of SR, the better. SR can be calculated as follow:

<!-- b000549 | prose | pages [18] -->
1. Based on the curve of the asset, we calculate the value of DRR(Daily Rate of Return) for each day and obtain a DRR series

<!-- b000550 | prose | pages [18] -->
푤푖 퐷푅푅= {퐷푅푅푖|퐷푅푅푖=

<!-- b000551 | prose | pages [18] -->
which is subject to normal distribution;

<!-- b000552 | prose | pages [18] -->
× 100%}

<!-- b000553 | prose | pages [18] -->
푤푖−1

<!-- b000554 | prose | pages [18] -->
2. Calculate the average 퐸(퐷푅푅) and the variance 퐷(퐷푅푅) of the DRR series;

<!-- b000555 | prose | pages [18] -->
3. Since in this problem, we ignore the cash interest, we ﬁnally obtain SR under the equation

<!-- b000556 | prose | pages [18] -->
푆푅= 퐸(퐷푅푅)

<!-- b000557 | prose | pages [18] -->
퐷(퐷푅푅)

<!-- b000558 | prose | pages [18] -->
p

<!-- b000559 | prose | pages [18] -->
A strategy has a negative average return when 푆푅< 0, and the strategy has a positive average return when 푆푅> 0.

<!-- b000560 | furniture | pages [19] -->
Team # 2204883

<!-- b000561 | furniture | pages [19] -->
Page 17 of 23

<!-- b000562 | prose | pages [19] -->
5.2 Evidence for A Good Investment Strategy

<!-- b000563 | prose | pages [19] -->
With the 10 metrics deﬁned above, we now compare the values of those metrics under 2 simple investment strategies, 1 ideal investment strategy, 1 commonly used investment strategy on the market and our investment strategy. Brief introductions of these 4 strategies are shown below.

<!-- b000564 | heading | pages [19] -->
1. A 5-year long-term investment in gold(Gold Asset)

<!-- b000565 | prose | pages [19] -->
In brief, this strategy requires us to use all of our initial $1,000 to purchase gold on the ﬁrst trading day and to not make any gold and bitcoin related trades for the next 5 years. For the purpose of representing the trades and calculating metrics such as MPA, MLA, etc., we equate this strategy as follows: in the absence of commissions, we sell all of our gold ﬁrst and then purchase an equal amount of gold at the same price on each trading day, except for the ﬁrst trading day.

<!-- b000566 | heading | pages [19] -->
2. A 5-year long-term investment in bitcoin(Bitcoin Asset)

<!-- b000567 | prose | pages [19] -->
This strategy shares the same idea with the strategy above. The only diﬀerence is that in this strategy, we use all of our initial $1,000 to purchase bitcoin on the ﬁrst trading day.

<!-- b000568 | prose | pages [19] -->
3. An ideal strategy in the circumstance that we know the exact value of daily price of gold and bitcoin(Ideal Asset)

<!-- b000569 | prose | pages [19] -->
This strategy shares the same investment strategy model with our strategy. The diﬀerence is that our strategy is developed by bringing the predicted price values of gold and bitcoin into the model, while this ideal strategy is developed by bringing the true price values of gold and bitcoin into the model.

<!-- b000570 | heading | pages [19] -->
4. A commonly used investment strategy on the market(Rule Asset)

<!-- b000571 | prose | pages [19] -->
This strategy is developed based on the eight rules created by Joseph Granville[6]. When the moving average is below the stock price and in an uptrend, it is time to buy, and vice versa, it is time to sell.

<!-- b000572 | prose | pages [19] -->
The comparison of the curve of daily asset value among those 4 strategies and our strategy is shown in the ﬁgure below.

<!-- b000573 | caption | pages [19] -->
Figure 7: Comparison of the curve of daily asset value among strategies

<!-- b000574 | furniture | pages [20] -->
Team # 2204883

<!-- b000575 | furniture | pages [20] -->
Page 18 of 23

<!-- b000576 | prose | pages [20] -->
To make sure that the 푆푅value is valid for these strategies, we plot the distribution of 퐷푅푅(or, the yield rate) of these strategies, shown in the ﬁgures below.

<!-- b000577 | prose | pages [20] -->
(b) Distribution of gold asset (a) Distribution of our asset

<!-- b000578 | prose | pages [20] -->
(d) Distribution of ideal asset

<!-- b000579 | prose | pages [20] -->
(c) Distribution of bitcoin asset

<!-- b000580 | prose | pages [20] -->
(e) Distribution of rule asset

<!-- b000581 | caption | pages [20] -->
Figure 8: Distribution of 퐷푅푅in the 5 strategies

<!-- b000582 | prose | pages [20] -->
From the distribution we can see that the 퐷푅푅values of all these 5 strategies are subject to normal distribution. Thus, we can calculate 푆푅value for each strategy.

<!-- b000583 | prose | pages [20] -->
Finally the metric values of all strategies considered in this task is calculated and shown in the table below.

<!-- b000584 | prose | pages [20] -->
Strategies \ Metrics ARR Our Asset 266.36% Gold Asset 15.88% Bitcoin Asset 906.88% Ideal Asset 1406.66% 8.53% Rule Asset Strategies \ Metrics MLA Our Asset -867.44 -104.85 Gold Asset Bitcoin Asset -7742.91 Ideal Asset -868.93 Rule Asset -194.45 PLR NT WR MPA 1.41 848 53.54% 1044.51 1.08 1 52.38% 80.35 1.15 1 54.28% 7436.2 7.55 1401 73.59% 5171.07 1.47 41 21.95% 475.6 MCP MCL MDD SR 8 7 42.92% 0.0791 10 11 18.54% 0.0268 10 9 83.37% 0.078 20 3 1.89% 0.2955 1 6 30.06% 0.0247

<!-- b000585 | caption | pages [20] -->
Table 4: Metric values of all strategies

<!-- b000586 | prose | pages [20] -->
Without considering full transparency of future market direction, we can see from the table that the value of 푀퐷퐷and 푀퐿퐴of our model is signiﬁcantly smaller comparing to Bitcoin Asset strategy, proving that our model is more resilient to risks. Besides, our model has a high value of 퐴푅푅compared to Gold Asset strategy and Rule Asset strategy. From the perspective

<!-- b000587 | furniture | pages [21] -->
Team # 2204883

<!-- b000588 | furniture | pages [21] -->
Page 19 of 23

<!-- b000589 | prose | pages [21] -->
of the value of 푆푅, our model win the second place only behind the ideal model, indicating that our model achieve higher returns for the same risk.

<!-- b000590 | heading | pages [21] -->
Task 3: Sensitivity of Transaction Costs for The Strategy

<!-- b000591 | prose | pages [21] -->
6

<!-- b000592 | prose | pages [21] -->
We analyze the sensitivity of our strategy to the commission of gold transaction and the commission of bitcoin transaction by varying the commission of one asset and keeping the commission of the other asset unchanged alternately. strategy for each value of commission.

<!-- b000593 | prose | pages [21] -->
After that, we obtain an investment

<!-- b000594 | prose | pages [21] -->
When analyzing the sensitivity, we measure the trading behavior by calculating

<!-- b000595 | prose | pages [21] -->
• the average investment percentage when traders invest cash to gold 푣푔,

<!-- b000596 | prose | pages [21] -->
• the average investment percentage when traders invest cash to bitcoin 푣푏,

<!-- b000597 | prose | pages [21] -->
• the number of gold investment 푉푔,

<!-- b000598 | prose | pages [21] -->
• the number of bitcoin investment 푉푏,

<!-- b000599 | prose | pages [21] -->
• the total number of investment 푉푎,

<!-- b000600 | prose | pages [21] -->
under each investment strategy, and evaluate the performance of each investment strategy using two metrics: net proﬁt Δ푤and win rate 푊푅.

<!-- b000601 | heading | pages [21] -->
Sensitivity of The Commissions of Gold

<!-- b000602 | prose | pages [21] -->
6.1

<!-- b000603 | prose | pages [21] -->
We keep the commission of bitcoin to 2% and set the commission value of gold to 0%, 1%, 2%, 3% and 4% separately and take them into our investment strategy model respectively, and diﬀerent investment strategies are obtained. The trading behaviors are shown in the table below.

<!-- b000604 | prose | pages [21] -->
Commission of Gold 푣푔 푣푔 푣푏 푉푔 푉푏 푉푎 0.7622 0% 0.8286 6 52 58 0.6333 1% 0.8391 10 40 50 0.9497 2% 3% 4% 0.8307 2 38 40 - - 0.8223 0 40 40 - - 0.8255 0 40 40

<!-- b000605 | caption | pages [21] -->
Table 5: Trading behaviors under diﬀerent commissions of gold

<!-- b000606 | prose | pages [21] -->
We ﬁnd that when the commission of gold increases, the average investment percentage when traders invest cash to gold goes up signiﬁcantly and the average investment percentage when traders invest cash to bitcoin stays the same overall. Meanwhile, with the increment of the commission of gold, the number of gold investment drops signiﬁcantly to 0, and the number of bitcoin investment remains unchanged.

<!-- b000607 | prose | pages [21] -->
It can be seen that the increment of the commission of gold has a great impact on trading strategies, as reﬂected in:

<!-- b000608 | prose | pages [21] -->
• The average investment percentage when traders invest cash to gold has increased and the single investment in gold has increased. The reason may be that growth rate of gold is

<!-- b000609 | furniture | pages [22] -->
Team # 2204883

<!-- b000610 | furniture | pages [22] -->
Page 20 of 23

<!-- b000611 | prose | pages [22] -->
low, and the rise in the commission of gold has increased the threshold for investing in gold, so that a large amount of money will be spent on investing in gold only when the current risk of investing in gold is low enough.

<!-- b000612 | prose | pages [22] -->
• Both the number of gold investment and bitcoin investment declined. The reason may be that the rise in the commission of gold makes the model more cautious on investing. Eventually the number of investment in gold drops to 0, which indicates that the prediction of the increase in gold is less than the commission of gold, so the model will not make investment in gold.

<!-- b000613 | prose | pages [22] -->
The corresponding performances of each strategy are shown in the table below.

<!-- b000614 | prose | pages [22] -->
Commission of Gold 0% 1% 2% 3% 4% Δ푤 푊푅 10874.24 0.2745 14325.13 0.381 13069.35 0.4474 14587.49 0.4103 10865.78 0.4615

<!-- b000615 | caption | pages [22] -->
Table 6: Strategy performances under diﬀerent commissions of gold

<!-- b000616 | prose | pages [22] -->
We ﬁnd that when the commission of gold increases, the net proﬁt remains the same and the win rate shows an upward trend.

<!-- b000617 | prose | pages [22] -->
It can be seen that the increment of the commission of gold has little eﬀect on the results of investment[7].

<!-- b000618 | heading | pages [22] -->
Sensitivity of The Commissions of Bitcoin

<!-- b000619 | prose | pages [22] -->
6.2

<!-- b000620 | prose | pages [22] -->
We keep the commission of gold to 1% and set the commission value of bitcoin to 1%, 2%, 3%, 4% and 5% separately and take them into our investment strategy model respectively, and diﬀerent investment strategies are obtained. The trading behaviors are shown in the table below.

<!-- b000621 | prose | pages [22] -->
Commission of Bitcoin 푣푔 푣푏 푉푔 푉푏 푉푎 0.5829 1% 0.7921 12 48 60 0.6333 2% 3% 0.8391 10 40 50 0.7622 0.8286 12 42 54 0.785 4% 0.8255 8 44 52 0.7906 5% 0.8245 8 32 40

<!-- b000622 | caption | pages [22] -->
Table 7: Trading behaviors under diﬀerent commissions of bitcoin

<!-- b000623 | prose | pages [22] -->
We ﬁnd that when the commission of bitcoin increases, the average investment percentage when traders invest cash to gold rises signiﬁcantly and the average investment percentage when traders invest cash to bitcoin remains unchanged overall. Meanwhile, with the increment of the commission of bitcoin, both the number of gold investment and the total number of investment decrease.

<!-- b000624 | prose | pages [22] -->
It can be seen that the increment of the commission of bitcoin has a great impact on trading strategies, as reﬂected in:

<!-- b000625 | furniture | pages [23] -->
Team # 2204883

<!-- b000626 | furniture | pages [23] -->
Page 21 of 23

<!-- b000627 | prose | pages [23] -->
• The average investment percentage when traders invest cash to gold increased and the single investment in gold increased. The reason may be that the rise in the commission of bitcoin makes our model more inclined to invest large amounts in gold for the long term.

<!-- b000628 | prose | pages [23] -->
• Both the number of gold investment and bitcoin investment declined. The reason may be that the rise in the commission of bitcoin has made the model more cautious when investing.

<!-- b000629 | prose | pages [23] -->
The corresponding performances of each strategy are shown in the table below.

<!-- b000630 | prose | pages [23] -->
Commission of Bitcoin 1% 2% 3% 4% 5% Δ푤 푊푅 11632.52 0.4583 14325.13 0.381 2774.01 0.2745 1641.35 0.2954 1583.01 0.303

<!-- b000631 | caption | pages [23] -->
Table 8: Strategy performances under diﬀerent commissions of bitcoin

<!-- b000632 | prose | pages [23] -->
We ﬁnd that when the commission of bitcoin increases, the net proﬁt decreases signiﬁcantly and the win rate shows a decreasing trend.

<!-- b000633 | prose | pages [23] -->
It can be seen that when the commission of bitcoin increases, the win rate and the ﬁnal net proﬁt of the whole trading process decreases, and the trading results become worse.

<!-- b000634 | prose | pages [23] -->
6.3

<!-- b000635 | heading | pages [23] -->
Analysis of The Result

<!-- b000636 | prose | pages [23] -->
As for the diﬀerence between changing the transaction costs of gold and bitcoin, considering the impact of trading results when the transaction costs change, we believe that:

<!-- b000637 | prose | pages [23] -->
• Gold is a less risky asset, and most investments in gold are long-term investments, so the increase in transaction costs of gold do not have much impact on trading results.

<!-- b000638 | prose | pages [23] -->
• Bitcoin is a risky asset, and the increment in transaction costs of bitcoin makes our strategy more prudent to sell bitcoin and instead, makes predicting of the decline in bitcoin more diﬃcult.

<!-- b000639 | prose | pages [23] -->
As for the similarity of changing the transaction costs of gold and bitcoin, we believe that:

<!-- b000640 | prose | pages [23] -->
• The average percentage of total asset value invested in bitcoin and the number of bitcoin investment have all remained generally unchanged, probably because the short-term growth rate of bitcoin is often extremely high, making it diﬃcult to aﬀect the preference for short-term investments in bitcoin when changing the transaction costs.

<!-- b000641 | prose | pages [23] -->
• Both the number of gold investment and bitcoin investment decline as the transaction costs increase, because the increment of transaction costs makes the strategy more cautious when investing.

<!-- b000642 | prose | pages [23] -->
Therefore, we conclude that investment strategies are more sensitive to changes in bitcoin commissions.

<!-- b000643 | furniture | pages [24] -->
Team # 2204883

<!-- b000644 | furniture | pages [24] -->
Page 22 of 23

<!-- b000645 | prose | pages [24] -->
7

<!-- b000646 | heading | pages [24] -->
Task 4: Memorandum for The Trader

<!-- b000647 | prose | pages [24] -->
To: Trader in investment markets

<!-- b000648 | prose | pages [24] -->
From: Team # 2204883 of 2022 MCM

<!-- b000649 | prose | pages [24] -->
Date: February 21, 2022

<!-- b000650 | prose | pages [24] -->
Subject: ﬁnd the best investment strategy that maximize total return

<!-- b000651 | prose | pages [24] -->
Dear Sir or Madam:

<!-- b000652 | prose | pages [24] -->
The investment market is volatile, and we believe that all investors, including you, expect to maximize returns while minimizing risk. For this purpose, we analyze the daily price of gold and bitcoin from November 9, 2016 to October 9, 2021. We build two models i.e. Long Short- Term Memory market capitalization forecasting model(LSTM) and multi-objective portfolio

<!-- b000653 | prose | pages [24] -->
investment programming model(MLP). Based on these two models, we are able to maintain a low investment risk while achieving higher returns.

<!-- b000654 | prose | pages [24] -->
First, we build LSTM model to help you accurately predict the future performance of your investment market. Our LSTM model use recurrent neural network to analyze the previous 14 days of market data and predict the market trend of the day, not only to predict the ups and downs, but also to get the exact value. The measurement indicator is the Mean Absolute Percentage Error (MAPE). The results show that our model is very accurate, with a MAPE value of 0.007261 for gold and 0.041630 for bitcoin. With price forecasting, investors can plan their short-term investment strategies in more detail.

<!-- b000655 | prose | pages [24] -->
Moreover, based on the predicted values of the market trend, we develop the MLP model to solve for the investment numbers of gold and bitcoin that satisfy the maximum return and minimum risk by using ideal point method. Considering that there are trading commissions, our results are compared with the future returns of maintaining the existing investments and the optimal solution is selected. After 5 years of trading, we end up with an annualized rate of return of 266.36%, in other words, an increase in assets of about 13 times.

<!-- b000656 | prose | pages [24] -->
According to our analysis of the results, the following are our recommended investment strategies:

<!-- b000657 | prose | pages [24] -->
1. Trust the data from the prediction is accurate and incorporate the programming model’s result into your investment strategy.

<!-- b000658 | prose | pages [24] -->
2. When the market has experienced a big rise and predicted trend is to be plunging, withdraw in time, since our model has predicted most of plunge.

<!-- b000659 | prose | pages [24] -->
3. Too frequent trading is not recommended due to trading commissions.

<!-- b000660 | prose | pages [24] -->
Of course, our data, models and strategies operate only on a daily basis and include only forecasts and asset portfolios based on two asset classes. For daily ﬁnancial transactions, our model can be further extended in the time dimension and portfolio dimension. Thank you for reading our memorandum in your busy schedule, hoping our suggestions are useful to you.

<!-- b000661 | prose | pages [24] -->
Yours Sincerely,

<!-- b000662 | furniture | pages [24] -->
Team # 2204883

<!-- b000663 | furniture | pages [25] -->
Team # 2204883

<!-- b000664 | furniture | pages [25] -->
Page 23 of 23

<!-- b000665 | prose | pages [25] -->
8

<!-- b000666 | heading | pages [25] -->
Strengths and Weaknesses of Our Strategy

<!-- b000667 | prose | pages [25] -->
8.1

<!-- b000668 | heading | pages [25] -->
The Price Prediction model

<!-- b000669 | prose | pages [25] -->
• Strengths: The model is based on LSTM model with strong mathematical theory support. Sliding window algorithm is used to reduce errors caused by data redundancy. The optimal combination of parameters is obtained by calculating the 푀퐴푃퐸of the prediction results, which further optimizes the performance of the model.

<!-- b000670 | prose | pages [25] -->
• Weakness: Due to the stochastic nature of the predicting process of LSTM model, we cannot guarantee the optimality of the predicting process.

<!-- b000671 | prose | pages [25] -->
8.2

<!-- b000672 | heading | pages [25] -->
The Investment Strategy model

<!-- b000673 | prose | pages [25] -->
• Strength: By quantifying return and risk and using the MLP model, an investment strategy that balances return and risk is obtained. Diﬀerent models are built for diﬀerent trading behaviors with a strong focus.

<!-- b000674 | prose | pages [25] -->
• Weakness: When quantifying risk, no adjustment is made to the value of the parameter risk statistical period. This may aﬀect the merit of the model in developing investment strategies.

<!-- b000675 | heading | pages [25] -->
References

<!-- b000676 | references | pages [25] -->
[1] Schabacker, Richard. Technical analysis and stock market proﬁts. Harriman House Lim-

<!-- b000677 | references | pages [25] -->
ited, 2005.

<!-- b000678 | references | pages [25] -->
[2] Bao, Wei, Jun Yue, and Yulei Rao. "A deep learning framework for ﬁnancial time se-

<!-- b000679 | references | pages [25] -->
ries using stacked autoencoders and long-short term memory." PloS one 12.7 (2017):

<!-- b000680 | references | pages [25] -->
e0180944.

<!-- b000681 | references | pages [25] -->
[3] Donckels, Brecht MR, et al. "An ideal point method for the design of compromise experi-

<!-- b000682 | references | pages [25] -->
ments to simultaneously estimate the parameters of rival mathematical models." Chemical

<!-- b000683 | references | pages [25] -->
Engineering Science 65.5 (2010): 1705-1719.

<!-- b000684 | references | pages [25] -->
[4] Zou, Zhichao, and Zihao Qu. "Using LSTM in Stock prediction and Quantitative Trad-

<!-- b000685 | references | pages [25] -->
ing." CS230: Deep Learning, Winter (2020).

<!-- b000686 | references | pages [25] -->
[5] Zopounidis, Constantin, D. K. Despotis, and I. Kamaratou. "Proﬁlio Selection Using the

<!-- b000687 | references | pages [25] -->
Adelais Multiobjective Linear Programming System." Computational Economics 11.3

<!-- b000688 | references | pages [25] -->
(1998): 189-204.

<!-- b000689 | references | pages [25] -->
[6] Granville. New Key to Stock Market Proﬁts. Martino Fine Books, 1963.

<!-- b000690 | references | pages [25] -->
[7] Lv, Dongdong, et al. "An empirical study of machine learning algorithms for stock daily

<!-- b000691 | references | pages [25] -->
trading strategy." Mathematical problems in engineering 2019 (2019).
