# P-C-2024-2418251-0c8c04e5

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2024

<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | title | pages [1] -->
2418251

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
微信公众号：数学模型

<!-- b000009 | title | pages [1] -->
Momentum: Powerful Magic for Winning

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
In the 2023 Wimbledon Finals, Carlos Alcaraz dethroned Novak Djokovic in a captivating display of youthful exuberance over seasoned skill. The match’s dynamic ebb and ﬂow highlighted the intangible factor of momentum. To capture this phenomenon, our team crafted mathematical models that leveraged Wimbledon data to quantify player momentum, offering fresh insights into what drives tennis triumphs.

<!-- b000012 | prose | pages [1] -->
For Model 1, we started by cleaning the data to remove outliers. We then extracted the match data for Novak Djokovic from the Finals. By feeding his data into a Recurrent Neural Network

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
(RNN), we calculated his winning probability for each game when serving and receiving. The re- sults showed a signiﬁcantly higher winning probability when serving than receiving, which aligns with experience. Additionally, we created visualization charts to intuitively display the changes in winning probability throughout the match.

<!-- b000015 | prose | pages [1] -->
For Model 2, we ﬁrst deﬁned an algorithm for potential points. Potential point is a state quan- tity related to ﬁve features: service points, break points, continuous scoring, unforced errors, and distance run. We used Principal Component Analysis (PCA) on ﬁve features to extract three prin- cipal component vectors as input features and built a momentum model based on Support Vector Machines (MSVM). This model was used to obtain the single-game momentum and accumulated set momentum for two players. We conducted a correlation analysis between the calculated single- game momentum and the single-game winning probability obtained from Model 1, yielding corre- lation values of 0.704 and 0.729. This indicates that a player’s success is not random but related to momentum.

<!-- b000016 | prose | pages [1] -->
For Model 3, we built an ARIMA time series forecasting model. Using the momentum data from model 2, we obtained predictions for the accmulated momentum of the two players. The results suggestted that Carlos Alcaraz would have higher momentum, making it more likely for him to win. Following this, we offered advice on how to capitalize on momentum shifts during a match, focusing on seizing opportunities for continuous scoring, handling service games, and converting break points.

<!-- b000017 | prose | pages [1] -->
Next, we tested and veriﬁed our model using data from another match in the Wimbledon Cham- pionships (match 1502). The model’s calculations of accumulated momentum closely matches the match ﬂow. We also provided general advice for modifying the model for different types of com- petition. After conducting a sensitivity analysis, the results shows that the momentum calculation model is highly sensitive to various input features.

<!-- b000018 | prose | pages [1] -->
Finally, we wrote a memo for tennis coaches. The memo summarizes our model, explains the role of momentum, and offers recommendations.

<!-- b000019 | keywords | pages [1] -->
Keywords: Momentum; RNN; PCA; The MSVM Model; ARIMA

<!-- b000020 | furniture | pages [1] -->
关注数学模型

<!-- b000021 | furniture | pages [1] -->
2

<!-- b000022 | furniture | pages [1] -->
MATHmodels

<!-- b000023 | furniture | pages [1] -->
获取更多资讯

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
Introduction

<!-- b000027 | prose | pages [2] -->
2

<!-- b000028 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000029 | prose | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Ourwork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 3 Assumptions and Justiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000030 | prose | pages [2] -->
2

<!-- b000031 | heading | pages [2] -->
Notations

<!-- b000032 | prose | pages [2] -->
3

<!-- b000033 | prose | pages [2] -->
4

<!-- b000034 | heading | pages [2] -->
Establishment and Solution of Single Game Winning Probability Model

<!-- b000035 | prose | pages [2] -->
3 4

<!-- b000036 | heading | pages [2] -->
Single Game Winning Probability Model Based on Recurrent Neural Network (RNN)

<!-- b000037 | prose | pages [2] -->
3.1 4

<!-- b000038 | heading | pages [2] -->
Serving Player Winning Probability Model

<!-- b000039 | prose | pages [2] -->
3.1.1 . . . . . . . . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
5 Receiving Player Winning Probability Model . . . . . . . . . . . . . . . . 3.1.2 7

<!-- b000041 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000042 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 Visualization of the Match Flow 8

<!-- b000043 | heading | pages [2] -->
Establishment and Solution of the Momentum Model

<!-- b000044 | prose | pages [2] -->
4 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Feature Selection 9 Potential Point Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 9 Principal Component Analysis (PCA) Dimensionality Reduction . . . . . . . . . . 4.3 10

<!-- b000045 | heading | pages [2] -->
Momentum Model Based on Support Vector Machines (SVM)

<!-- b000046 | prose | pages [2] -->
4.4 . . . . . . . . . . .

<!-- b000047 | prose | pages [2] -->
12 Statistical Test of Factors Affecting Momentum . . . . . . . . . . . . . . . . . . . 4.5 14 The Impact of Momentum on the Probability of Winning a Match 4.5.1 . . . . .

<!-- b000048 | prose | pages [2] -->
14 The Impact of other Factors on Momentum 4.5.2

<!-- b000049 | prose | pages [2] -->
5

<!-- b000050 | heading | pages [2] -->
Predictive Model for Shifts in Momentum

<!-- b000051 | prose | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000052 | prose | pages [2] -->
15

<!-- b000053 | prose | pages [2] -->
15 Accumulated Momentum Prediction Model Based on ARIMA . . . . . . . . . . . 5.1 16 Advice Based on Shifts in Momentum . . . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000054 | prose | pages [2] -->
6

<!-- b000055 | heading | pages [2] -->
Veriﬁcation and Application of the Model

<!-- b000056 | prose | pages [2] -->
17

<!-- b000057 | prose | pages [2] -->
18 Veriﬁcation within the Same Type of Competition . . . . . . . . . . . . . . . . . . 6.1 18 Application to other Types of Competitions 6.2

<!-- b000058 | prose | pages [2] -->
7

<!-- b000059 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000060 | prose | pages [2] -->
8

<!-- b000061 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000062 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | prose | pages [2] -->
19

<!-- b000064 | prose | pages [2] -->
19

<!-- b000065 | prose | pages [2] -->
20 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 20 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000066 | heading | pages [2] -->
Appendices

<!-- b000067 | prose | pages [2] -->
20

<!-- b000068 | prose | pages [2] -->
23

<!-- b000069 | furniture | pages [2] -->
关注数学模型

<!-- b000070 | furniture | pages [2] -->
1

<!-- b000071 | furniture | pages [2] -->
1

<!-- b000072 | furniture | pages [2] -->
2

<!-- b000073 | furniture | pages [2] -->
MATHmodels

<!-- b000074 | furniture | pages [2] -->
获取更多资讯

<!-- b000075 | furniture | pages [3] -->
Team # 2418251

<!-- b000076 | prose | pages [3] -->
1

<!-- b000077 | heading | pages [3] -->
Introduction

<!-- b000078 | furniture | pages [3] -->
Page 2 of 23

<!-- b000079 | prose | pages [3] -->
Billy Shirley once said:“Watch Out for Momentum : There may not even be such

<!-- b000080 | prose | pages [3] -->
a thing in sports, but you can be sure you’ll be told whenever it shifts.”

<!-- b000081 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000082 | prose | pages [3] -->
1.1 Problem Background

<!-- b000083 | prose | pages [3] -->
In the 2023 Wimbledon Gentlemen’s cham- pionship, 20-year-old Carlos Alcaraz emerged victorious against 36-year-old Novak Djokovic, handing Djokovic his ﬁrst Wimbledon defeat since 2013 and halting his remarkable run in Grand Slam tournaments. The ﬁnal was ﬁlled with dramatic turns of performance. Djokovic started strong by claiming the ﬁrst set 6-1, only

<!-- b000084 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000085 | prose | pages [3] -->
[1]

<!-- b000086 | caption | pages [3] -->
Figure 1: Novak Djokovic & Carlos Alcaraz

<!-- b000087 | prose | pages [3] -->
for Alcaraz to make a comeback, securing the second set through a tie-breaker and dominating the third set 6-1. Although Djokovic managed to take the fourth set 6-3, Alcaraz ultimately clinched the win with a 6-4 score in the decid- ing ﬁfth set. The game showcased notable shifts in momentum, underscoring the difﬁculty in quantifying how various events within the match af- fect a player’s or team’s performance. Yet the omnipresence of momentum is so pervasive that it’s acknowledged not solely by commentators, mentors, and competitors but also sensed by a laid- back spectator lounging on their sofa. So for coaches, comprehending precisely what momentum is can be vital, as this understanding will aid them in directing the game.

<!-- b000088 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000089 | prose | pages [3] -->
Considering the background information and restricted conditions identiﬁed in the problem statement, we need to solve the following problems:

<!-- b000090 | prose | pages [3] -->
• Problem 1:Develop a tennis match ﬂow model to assess player performance, considering serve advantage and visualize the match dynamics.

<!-- b000091 | prose | pages [3] -->
• Problem 2:Assess the tennis coach’s skepticism about the role of “momentum” versus ran- domness in match outcomes using a performance model/metric.

<!-- b000092 | prose | pages [3] -->
• Problem 3:Develop a predictive model for tennis match swings and advise on strategy con- sidering past “momentum” differentials.

<!-- b000093 | prose | pages [3] -->
• Problem 4:Test and validate the tennis swing prediction model on other matches, identify performance factors, and assess generalizability to different contexts.

<!-- b000094 | prose | pages [3] -->
• Problem 5:Include a page memo summarizing results with advice for coaches on the role of “momentum”, and how to prepare players to respond to events that impact the ﬂow of play during a tennis match.

<!-- b000095 | furniture | pages [3] -->
关注数学模型

<!-- b000096 | furniture | pages [3] -->
2

<!-- b000097 | furniture | pages [3] -->
MATHmodels

<!-- b000098 | furniture | pages [3] -->
获取更多资讯

<!-- b000099 | furniture | pages [4] -->
Team # 2418251

<!-- b000100 | prose | pages [4] -->
1.3 Ourwork

<!-- b000101 | furniture | pages [4] -->
Page 3 of 23

<!-- b000102 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000103 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000104 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000105 | prose | pages [4] -->
1.4

<!-- b000106 | heading | pages [4] -->
Assumptions and Justiﬁcation

<!-- b000107 | prose | pages [4] -->
• Assumption 1:Assume that after each set, the athlete’s accumulated momentum is updated.

<!-- b000108 | prose | pages [4] -->
Justiﬁcation:After each set, the athlete gets a chance to rest, stabilize, and the coach will provide corresponding strategies, thus it’s appropriate to update the athlete’s momentum.

<!-- b000109 | prose | pages [4] -->
• Assumption 2:Ignore the impact of tiebreakers on momentum trends.

<!-- b000110 | prose | pages [4] -->
Justiﬁcation:In tiebreakers, the situation changes dramatically with alternating service rights, and the athletes’ mental states are highly tense, so the inﬂuence of momentum is minimal. Therefore, the impact of tiebreakers on momentum trends can be neglected.

<!-- b000111 | prose | pages [4] -->
• Assumption 3:The momentum in each game is discrete.

<!-- b000112 | heading | pages [4] -->
Justiﬁcation:The model considers momentum to be discrete within each game, as there

<!-- b000113 | prose | pages [4] -->
is no more continuous data available to accurately depict it. Therefore, the calculation of momentum is based on discrete intervals within the games.

<!-- b000114 | prose | pages [4] -->
• Assumption 4:Ignore the impact of environmental factors and athletes’ psychological states.

<!-- b000115 | prose | pages [4] -->
Justiﬁcation:The environment of the court, wind speed, and the athletes’ psychological states can all have an impact on the progression of the match. However, since no speciﬁc data is provided in the question and psychological states cannot be quantitatively described, the inﬂuence of these factors is therefore neglected.

<!-- b000116 | furniture | pages [4] -->
关注数学模型

<!-- b000117 | furniture | pages [4] -->
2

<!-- b000118 | furniture | pages [4] -->
MATHmodels

<!-- b000119 | furniture | pages [4] -->
获取更多资讯

<!-- b000120 | furniture | pages [5] -->
Team # 2418251

<!-- b000121 | prose | pages [5] -->
2

<!-- b000122 | heading | pages [5] -->
Notations

<!-- b000123 | furniture | pages [5] -->
Page 4 of 23

<!-- b000124 | caption | pages [5] -->
Table 1: Notation

<!-- b000125 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000126 | heading | pages [5] -->
Symbol

<!-- b000127 | prose | pages [5] -->
X1 1 X2 2 X3 3 X4 4 t

<!-- b000128 | prose | pages [5] -->
Meaning

<!-- b000129 | prose | pages [5] -->
Single-serve rate Killing-shot rate Error rate break-of-serve rate Total number of balls in a single game 5 tf 6 tace 7 tw 8 tuf 9 Yp 10 Number of successful ﬁrst serves Number of aces Number of winning points Number of unforced errors Winning rate

<!-- b000130 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000131 | prose | pages [5] -->
Mb 11 Ms 12 Mc 13 Mu 14 Mi 15 M 16 i 17 n Potential point_Break of serve Potential point_Serve Potential point_Continuous Potential point_Unforced Error Potential points of each game Potential Point The current game number Total number of games played in the set 18 Mo 19 Momentum

<!-- b000132 | prose | pages [5] -->
*Note: Here is a partial notation.Detailed explanations for each symbol can be found in the corresponding text.

<!-- b000133 | heading | pages [5] -->
Establishment and Solution of Single Game Winning Proba-

<!-- b000134 | prose | pages [5] -->
3

<!-- b000135 | heading | pages [5] -->
bility Model

<!-- b000136 | heading | pages [5] -->
Single Game Winning Probability Model Based on Recurrent Neural

<!-- b000137 | prose | pages [5] -->
3.1 Network (RNN)

<!-- b000138 | prose | pages [5] -->
In tennis, players who are serving have a higher probability of winning. Therefore, we construct separate winning probability models for players based on both the serving and receiving aspects. Given the numerous factors that can inﬂuence the outcome of a tennis match, we focus on key features and use neural network methods to build our winning probability model. However, the traditional neural network produces outputs that depend only on the current input, which makes them less capable of accurately predicting data that changes over time. In contrast, the output of Recurrent Neural Network (RNN) is determined by both the current input and the previous moment’s output, similar to adding a memory unit to the neural network. This allows the RNN to remember the behavior from the previous moment and respond appropriately based on the current input and past behavior. Compared to the traditional neural network, which is like a broken chain, RNN exhibits a continuous characteristic. This characteristic makes RNN more suitable for our modeling than the traditional neural network.

<!-- b000139 | furniture | pages [5] -->
关注数学模型

<!-- b000140 | furniture | pages [5] -->
2

<!-- b000141 | furniture | pages [5] -->
MATHmodels

<!-- b000142 | furniture | pages [5] -->
获取更多资讯

<!-- b000143 | furniture | pages [6] -->
Team # 2418251

<!-- b000144 | furniture | pages [6] -->
Page 5 of 23

<!-- b000145 | heading | pages [6] -->
Serving Player Winning Probability Model

<!-- b000146 | prose | pages [6] -->
3.1.1

<!-- b000147 | prose | pages [6] -->
In the model, we use the win probability in each game as the output feature and select single-serve rate, killing-shot rate, and error rate as the three representative input features. We perform data preprocessing by

<!-- b000148 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000149 | prose | pages [6] -->
extracting the given data from the problem and calculating the conversion to the serving player’s single-serve rate, killing-shot rate, and error rate as the input features.

<!-- b000150 | prose | pages [6] -->
X1 = tf

<!-- b000151 | prose | pages [6] -->
(1) t

<!-- b000152 | prose | pages [6] -->
In this equation, t represents the total number of balls in a single game, and tf represents the number of successful ﬁrst serves. Using this equation, we can calculate the single-serve rate X1.

<!-- b000153 | prose | pages [6] -->
We deﬁne the killing-shot rate X2 and the error rate X3 in the same way.

<!-- b000154 | prose | pages [6] -->
X2 = tace

<!-- b000155 | prose | pages [6] -->
(2)

<!-- b000156 | prose | pages [6] -->
tw

<!-- b000157 | prose | pages [6] -->
X3 = tuf

<!-- b000158 | prose | pages [6] -->
(3)

<!-- b000159 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000160 | prose | pages [6] -->
t

<!-- b000161 | prose | pages [6] -->
We deﬁne the vector Y predicted by three input features as the athlete’s service winning rate.

<!-- b000162 | prose | pages [6] -->
Yp = tw

<!-- b000163 | prose | pages [6] -->
(4) t

<!-- b000164 | prose | pages [6] -->
In the equation 2,3 and 4, tace represents the number of aces, tw represents the number of winning points, and tuf represents the number of unforced errors. Yp represents winning rate, which is based on past data.

<!-- b000165 | prose | pages [6] -->
We construct and input the matrix X = [X1, X2, X3] after extracting the three input feature vectors. For each Xi, we have Xi = (X1, X2, · · · , Xt)T (i = 1, 2, 3, · · · ), where Xt represents the input feature at time t. After determining the features, we process with the propagation of RNN. The process is as follows:

<!-- b000166 | prose | pages [6] -->
ht = f (WihXt + Whhht−1 + bh) (5)

<!-- b000167 | prose | pages [6] -->
yt = Whoht + b0 (6)

<!-- b000168 | prose | pages [6] -->
Where, ht represents the hidden layer state, Wih is the weight matrix from the inputlayer to the hidden layer, Whh is the weight matrix from the hidden layer to itself, and bh is thebias vector for the hidden layer. Who is the weight matrix from the hidden layer to the outputlayer, and bo, is the bias vector for the output layer.

<!-- b000169 | prose | pages [6] -->
Regarding the objective function, we assume that the model’s predicted output is as following:

<!-- b000170 | prose | pages [6] -->
bY = ( ˆy1, ˆy2, · · · , ˆyt)T

<!-- b000171 | prose | pages [6] -->
The actual output is as following:

<!-- b000172 | prose | pages [6] -->
(7)

<!-- b000173 | prose | pages [6] -->
Y = (y1, y2, · · · , yt)T (8)

<!-- b000174 | prose | pages [6] -->
Then the objective function can be deﬁned as following:

<!-- b000175 | prose | pages [6] -->
Pt

<!-- b000176 | prose | pages [6] -->
L = 1

<!-- b000177 | prose | pages [6] -->
i=1 ( ˆyi −yi)2

<!-- b000178 | prose | pages [6] -->
t

<!-- b000179 | prose | pages [6] -->
(9)

<!-- b000180 | furniture | pages [6] -->
关注数学模型

<!-- b000181 | furniture | pages [6] -->
2

<!-- b000182 | furniture | pages [6] -->
MATHmodels

<!-- b000183 | furniture | pages [6] -->
获取更多资讯

<!-- b000184 | furniture | pages [7] -->
Team # 2418251

<!-- b000185 | furniture | pages [7] -->
Page 6 of 23

<!-- b000186 | prose | pages [7] -->
First, we clean the dataset in the problem, removing outliers. Afterward, we use the backpropagation al- gorithm and the optimizer in MATLAB to update the model’s parameters, minimizing the objective function, and thus completing the initial construction of the model.

<!-- b000187 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000188 | prose | pages [7] -->
We incorporated all the data from Novak Djokovic’s service games in the match for model training, calculating his service game winning probability through factors such as the killing-shot rate, single-serve rate, and error rate.

<!-- b000189 | caption | pages [7] -->
Table 2: Novak Djokovic’s service game data from Wimbledon Championship.

<!-- b000190 | prose | pages [7] -->
Match_id Set_no.

<!-- b000191 | prose | pages [7] -->
Game_no.

<!-- b000192 | prose | pages [7] -->
1316 1 1 1316 1 3 1316 1 5 · · · · · · · · · 1701 5 9

<!-- b000193 | prose | pages [7] -->
X1 X2 X3 Yp Point_no.

<!-- b000194 | prose | pages [7] -->
5 0.25 1 0 0.8 4 0.25 0 0 1 5 0.25 0.8 0 0.8 · · · · · · · · · · · · · · · 5 0.25 0.8 0.8 0.8

<!-- b000195 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000196 | prose | pages [7] -->
Through model calculations, we obtained the service player’s winning probability based on three input features and compared it with the player’s actual winning rate. The results are as follows:

<!-- b000197 | caption | pages [7] -->
Figure 3: The ﬁtting results for the service

<!-- b000198 | prose | pages [7] -->
player’s winning probability

<!-- b000199 | caption | pages [7] -->
Figure 4: Histogram of prediction error for

<!-- b000200 | prose | pages [7] -->
Serving

<!-- b000201 | prose | pages [7] -->
In the ﬁgure 3, the red line represents the winning probability of the service player calculated by the model, and the green line represents the reference winning rate. Both demonstrate a high degree of ﬁtting precision, as shown in the ﬁgure 4 above.

<!-- b000202 | prose | pages [7] -->
In the ﬁgure 4, the pink frequency distribution histogram represents the error distribution frequency of the service winning rate model. The mean squared error (MSE) is 0.012922. The coefﬁcient of determina- tion R2 is 0.56119.

<!-- b000203 | furniture | pages [7] -->
关注数学模型

<!-- b000204 | furniture | pages [7] -->
2

<!-- b000205 | furniture | pages [7] -->
MATHmodels

<!-- b000206 | furniture | pages [7] -->
获取更多资讯

<!-- b000207 | furniture | pages [8] -->
Team # 2418251

<!-- b000208 | furniture | pages [8] -->
Page 7 of 23

<!-- b000209 | heading | pages [8] -->
Receiving Player Winning Probability Model

<!-- b000210 | prose | pages [8] -->
3.1.2

<!-- b000211 | prose | pages [8] -->
For the construction of a winning probability model for receiving players, we will also use the winning rate of each game as the output feature. However, the input features need to be rebuilt because receiving

<!-- b000212 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000213 | prose | pages [8] -->
players have a natural disadvantage compared to serving players. Therefore, when a receiving player breaks of serve, it greatly increases their conﬁdence and winning rate. Therefore, for the receiving player’s win- ning rate model, we select break of serve, killing shot, and error, as representative input features. We will preprocess the data provided in the problem and calculate the receiving player’s killing-shot rate X2, error rate X3, and break-of-serve rate x4. These will be input into an RNN model. We deﬁne break-of-serve rate x4 as following:

<!-- b000214 | prose | pages [8] -->
X4 = tbreak

<!-- b000215 | prose | pages [8] -->
(10)

<!-- b000216 | prose | pages [8] -->
tbreak_point

<!-- b000217 | prose | pages [8] -->
Where,tbreak_point represents the number of times a breakpoint is reached, and tbreak represents the number of successful break-of-serve.

<!-- b000218 | prose | pages [8] -->
Similarly, we train our model using all the data from the service games in which Novak Djokovic

<!-- b000219 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000220 | prose | pages [8] -->
received the ball. We calculate Novak Djokovic’s receiving game winning probability based on his kill-shot rate, break-of-serve rate, and error rate.

<!-- b000221 | caption | pages [8] -->
Table 3: Novak Djokovic’s receiving game data from Wimbledon Championship.

<!-- b000222 | prose | pages [8] -->
Match_id Set_no.

<!-- b000223 | prose | pages [8] -->
Game_no.

<!-- b000224 | prose | pages [8] -->
1316 1 2 1316 1 4 1316 1 6 · · · · · · · · · 1701 5 10

<!-- b000225 | prose | pages [8] -->
X2 X3 X4 Yp Point_no.

<!-- b000226 | prose | pages [8] -->
8 0.33 0 0.25 0.375 6 0 0 0.33 0.333 6 0.25 1 0 0.667 · · · · · · · · · · · · · · · 6 0.5 0 0 0.33

<!-- b000227 | prose | pages [8] -->
Through the training and calculation of the model, we obtained the winning probability of the receiving player based on three input features, and compared it with the winning rate of the player. The results are as follows:

<!-- b000228 | caption | pages [8] -->
Figure 5: The ﬁtting results for the service

<!-- b000229 | prose | pages [8] -->
player’s receiving probability

<!-- b000230 | caption | pages [8] -->
Figure 6: Histogram of prediction error for

<!-- b000231 | prose | pages [8] -->
receiving

<!-- b000232 | furniture | pages [8] -->
关注数学模型

<!-- b000233 | furniture | pages [8] -->
2

<!-- b000234 | furniture | pages [8] -->
MATHmodels

<!-- b000235 | furniture | pages [8] -->
获取更多资讯

<!-- b000236 | furniture | pages [9] -->
Team # 2418251

<!-- b000237 | furniture | pages [9] -->
Page 8 of 23

<!-- b000238 | prose | pages [9] -->
In the ﬁgure5, the red line represents the winning probability of the receiving player calculated by the model, and the green line represents the reference winning rate. The two have a high degree of ﬁtting accuracy.

<!-- b000239 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000240 | prose | pages [9] -->
In the ﬁgure 6, the pink frequency distribution histogram represents the error distribution frequency of the service winning rate model. The mean squared error (MSE) is 0.017458. The coefﬁcient of determina- tion R2 is 0.66442.

<!-- b000241 | prose | pages [9] -->
Finally, we compared and visualized the winning probability of serving and receiving for the same player, and obtained the following result:

<!-- b000242 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000243 | caption | pages [9] -->
Figure 7: Comparison of winning probability of serving and receiving

<!-- b000244 | prose | pages [9] -->
In ﬁgure7, the red line represents the winning probability of the server, while the green line represents the wining probability of the receiver. We can conclude that the server’s winning probability is generally higher than that of the receiver. Therefore, serving has a natural advantage, which is closely related to the momentum of the tennis player and also determines the direction of the tennis match.

<!-- b000245 | prose | pages [9] -->
3.2 Visualization of the Match Flow

<!-- b000246 | prose | pages [9] -->
We uses the match data from the Wimbledon ﬁnal between Carlos Alcaraz and Novak Djokovic (2023- wimbledon-1701) as a reference to visualize the match ﬂow.

<!-- b000247 | prose | pages [9] -->
In ﬁgure8, numbers 1 and 2 represent the winning athletes. The blue bar chart indicates the number of games each won, while the line chart describes the point difference between them. Through this chart, we can visually see the ﬂow of the entire match. Overall, the two players were well-matched, and the game was quite intense, with a particular highlight in the second set where it took thirteen games for the winner to emerge. In the end, player 1 secured three sets while player 2 took two sets but ultimately lost.

<!-- b000248 | heading | pages [9] -->
Establishment and Solution of the Momentum Model

<!-- b000249 | prose | pages [9] -->
4

<!-- b000250 | prose | pages [9] -->
Professional sports have always been a highly competitive industry both on and off the ﬁeld. Gaining an advantage can have crucial effects, which often lead to individual success and team victories. The study of momentum is one of the most challenging topics in sports analytics because while people can deﬁnitely

<!-- b000251 | furniture | pages [9] -->
关注数学模型

<!-- b000252 | furniture | pages [9] -->
2

<!-- b000253 | furniture | pages [9] -->
MATHmodels

<!-- b000254 | furniture | pages [9] -->
获取更多资讯

<!-- b000255 | furniture | pages [10] -->
Team # 2418251

<!-- b000256 | furniture | pages [10] -->
Page 9 of 23

<!-- b000257 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000258 | caption | pages [10] -->
Figure 8: 2023-Wimbledon-1701

<!-- b000259 | prose | pages [10] -->
sense a "winning streak" when it occurs, expressing it is still difﬁcult. Therefore, we have established

<!-- b000260 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000261 | prose | pages [10] -->
a momentum computation model based on machine learning to quantitatively analyze the momentum of players.[5]

<!-- b000262 | prose | pages [10] -->
4.1 Feature Selection

<!-- b000263 | prose | pages [10] -->
The manifestation of momentum is often a sense of power that a tennis player experiences when winning a match, and it is closely linked to the signiﬁcant progressions within the game. Since crucial points and progressions tend to inﬂuence the direction of the match, gaining or losing key points can lead to an increase or decrease in momentum. Therefore, we use the following events during a tennis match to describe the characteristics of momentum:

<!-- b000264 | prose | pages [10] -->
• Serve:Serving is crucial in tennis, especially when players are evenly matched, giving the server a higher chance of winning. A good serve, fast, with spin and varied placement, challenges the opponent’s defense. Servers can control the match pace and upset the opponent’s rhythm. Variations in serving can also disrupt the opponent’s return, creating offensive opportunities.

<!-- b000265 | prose | pages [10] -->
• Continuous Scoring Process:Consecutive scoring enhances conﬁdence and morale, im- proving focus and stroke technique. It can develop a “striking habit”, leading to smoother, more precise shots. This reﬂects the buildup of momentum in a match.

<!-- b000266 | prose | pages [10] -->
• Break of Serve:Achieving a break of serve boosts conﬁdence and momentum, as it signiﬁes an advantage. It encourages better performance and alters match dynamics, putting the player who broke ahead and forcing the opponent to break back. This affects both players’ mental states and strategies.

<!-- b000267 | prose | pages [10] -->
• Unforced Errors:Frequent unforced errors can damage conﬁdence and morale, leading to un- derperformance. They disrupt match dynamics, increase tension, and affect the athlete’s mental state and strategy, impacting momentum negatively.

<!-- b000268 | prose | pages [10] -->
4.2

<!-- b000269 | heading | pages [10] -->
Potential Point Model

<!-- b000270 | prose | pages [10] -->
The concept of potential pointis a discrete state concept used to describe the condition of an athlete at a certain point or stage in a competition. Thus, the entire process of the athlete’s competition is discretized

<!-- b000271 | furniture | pages [10] -->
关注数学模型

<!-- b000272 | furniture | pages [10] -->
2

<!-- b000273 | furniture | pages [10] -->
MATHmodels

<!-- b000274 | furniture | pages [10] -->
获取更多资讯

<!-- b000275 | furniture | pages [11] -->
Team # 2418251

<!-- b000276 | furniture | pages [11] -->
Page 10 of 23

<!-- b000277 | prose | pages [11] -->
into games, and the athlete’s performance in the current game is characterized by speciﬁc scores. The sum of these scores constitutes the potential point.

<!-- b000278 | prose | pages [11] -->
• “Potential point_Serve” Ms:During the athlete’s service, they have a greater advantage, and we

<!-- b000279 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000280 | prose | pages [11] -->
deﬁne that for each service game, the athlete earns potential points, which are quantiﬁed as 2 points, meaning Ms=2.

<!-- b000281 | prose | pages [11] -->
• “Potential point_Continuous Scoring Process” Mc: Athletes often gain more conﬁdence when they score consecutively. We deﬁne that for every three consecutive points scored, a potential point for consecutive scoring is earned, quantiﬁed as 2 points, meaning Mc=2. Within a game, an ath- lete may achieve multiple instances of consecutive scoring; in such cases, the potential points for consecutive scoring can be cumulative.

<!-- b000282 | prose | pages [11] -->
• “Potential point_Break of Serve” Mb: When an athlete achieves a break in a game, the potential point earned is characterized by 5 points, meaning Mb=5.

<!-- b000283 | prose | pages [11] -->
• “Potential point_Unforced Errors” Mu: Athletes often commit one or more unforced errors during

<!-- b000284 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000285 | prose | pages [11] -->
a match, which can signiﬁcantly impact their momentum negatively. We deﬁne that each occurrence of an unforced error reduces the potential points by 0.5, meaning Mu= -0.5. Since errors can happen multiple times in a match, this value can also accumulate.

<!-- b000286 | prose | pages [11] -->
In this way, we can obtain the potential point Mi for each game of the athlete as following:

<!-- b000287 | prose | pages [11] -->
Mi = Mb + Ms +

<!-- b000288 | prose | pages [11] -->
X

<!-- b000289 | prose | pages [11] -->
X

<!-- b000290 | prose | pages [11] -->
Mc +

<!-- b000291 | prose | pages [11] -->
Mu (11)

<!-- b000292 | prose | pages [11] -->
Where, Mb,Ms,Mc and Mu represent “Potential point_Break of serve”,“Potential point_Serve”, “Potential point_Continuous Scoring Process” and “Potential point_Unforced errors”, respectively.

<!-- b000293 | prose | pages [11] -->
For an entire set, the potential points are continuously accumulating, so for this set, the potential point M is as following:

<!-- b000294 | prose | pages [11] -->
M =

<!-- b000295 | prose | pages [11] -->
n n X

<!-- b000296 | prose | pages [11] -->
Mi (12)

<!-- b000297 | prose | pages [11] -->
i=1

<!-- b000298 | prose | pages [11] -->
Where, i represents the current game number and n represents the total number of games played in the set.

<!-- b000299 | prose | pages [11] -->
As hypothesized in the paper, there is a break at the end of each set where the coach provides guidance to the athlete, and the athlete also gets a rest. Therefore, at the start of the next set, the athlete’s total momentum points are reset to zero. Moreover, regarding tiebreak games, players alternate serves, and the intensity of competition is much higher, making it difﬁcult to quantify, so it is not included in the model.

<!-- b000300 | prose | pages [11] -->
Principal Component Analysis (PCA) Dimensionality Reduction 4.3

<!-- b000301 | prose | pages [11] -->
In tennis, physical ﬁtness consumption is also an important reference standard. However, the consump- tion of physical ﬁtness cannot be quantitatively characterized into momentum points. Therefore, we extract the running distance for each game of the athletes in the dataset separately to obtain a feature column of the athlete’s running distance per game. This is then incorporated as a reference into the momentum model.

<!-- b000302 | prose | pages [11] -->
Since there are already four feature vectors, and with the introduction of running distance, there are now ﬁve input features in the model. Therefore, we perform Principal Component Analysis (PCA) to reduce the data dimensions, coupling the ﬁve features and extracting the main input features to construct the model.

<!-- b000303 | furniture | pages [11] -->
关注数学模型

<!-- b000304 | furniture | pages [11] -->
2

<!-- b000305 | furniture | pages [11] -->
MATHmodels

<!-- b000306 | furniture | pages [11] -->
获取更多资讯

<!-- b000307 | furniture | pages [12] -->
Team # 2418251

<!-- b000308 | furniture | pages [12] -->
Page 11 of 23

<!-- b000309 | prose | pages [12] -->
Let aij represent each reference data point, and ﬁrst normalize the samples.

<!-- b000310 | prose | pages [12] -->
µj = 1

<!-- b000311 | prose | pages [12] -->
n

<!-- b000312 | prose | pages [12] -->
Pn

<!-- b000313 | prose | pages [12] -->
i=1aij (13)

<!-- b000314 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000315 | prose | pages [12] -->
r

<!-- b000316 | prose | pages [12] -->
Pn

<!-- b000317 | prose | pages [12] -->
1

<!-- b000318 | prose | pages [12] -->
s =

<!-- b000319 | prose | pages [12] -->
n −1

<!-- b000320 | prose | pages [12] -->
i=1 (aij −µi)2 (14)

<!-- b000321 | prose | pages [12] -->
Here, µjrepresents the mean of the samples, and s represents the standard deviation of the samples. Subsequently, the correlation coefﬁcient of the samples, that is, the correlation matrix is obtained.

<!-- b000322 | prose | pages [12] -->
Pn

<!-- b000323 | prose | pages [12] -->
k=1

<!-- b000324 | prose | pages [12] -->
rij =

<!-- b000325 | prose | pages [12] -->


<!-- b000326 | prose | pages [12] -->
r11

<!-- b000327 | prose | pages [12] -->


<!-- b000328 | prose | pages [12] -->
r21

<!-- b000329 | prose | pages [12] -->
R =

<!-- b000330 | prose | pages [12] -->
...

<!-- b000331 | prose | pages [12] -->
˜ aki × ˜ akj (15) n −1

<!-- b000332 | prose | pages [12] -->


<!-- b000333 | prose | pages [12] -->
· · · r12 r12 r1j

<!-- b000334 | prose | pages [12] -->


<!-- b000335 | prose | pages [12] -->
· · · r22 r22 r11

<!-- b000336 | prose | pages [12] -->
(16)

<!-- b000337 | prose | pages [12] -->
... ...

<!-- b000338 | prose | pages [12] -->
... ...

<!-- b000339 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000340 | prose | pages [12] -->
rj1 · · · rj2 rj2 rjj

<!-- b000341 | prose | pages [12] -->
Where,rijrepresent the correlation coefﬁcient of each sample, and R represent the correlation matrix. After that, we calculate the eigenvalues λjof the correlation matrix R and extract the corresponding eigen- vectors. Based on the magnitude of the eigenvalues, we select the top k eigenvectors corresponding to the largest eigenvalues as the principal components, where k is the number of principal components we wish to retain. The value of k is determined by the contribution rate and cumulative contribution rate to decide the number of principal components to choose. Our model requires that the cumulative contribution rate of all principal components be greater than 0.85. Through calculation, we reduce the ﬁve input features to three main principal component inputs. The results are shown in ﬁgure9.

<!-- b000342 | caption | pages [12] -->
Table 4: Three principal components derived from the dimensionality reduction of Carlos Alcaraz’s data

<!-- b000343 | prose | pages [12] -->
X1 X2 X3

<!-- b000344 | prose | pages [12] -->
0.497778724 -0.092368448 -0.406497262 -1.068004031 -0.429605389 -0.833292526 0.644409942 0.438065808 · · · -0.670082014 · · · · · · 0.720871564 -1.581903617 -0.652117794

<!-- b000345 | caption | pages [12] -->
Table 5: The accumulated contribution rate corresponding to the principal components.

<!-- b000346 | prose | pages [12] -->
Principle Componets

<!-- b000347 | prose | pages [12] -->
Accumulated contribution rate

<!-- b000348 | prose | pages [12] -->
X1 X2 X3

<!-- b000349 | prose | pages [12] -->
0.3594 0.8680 0.6391

<!-- b000350 | furniture | pages [12] -->
关注数学模型

<!-- b000351 | furniture | pages [12] -->
2

<!-- b000352 | furniture | pages [12] -->
MATHmodels

<!-- b000353 | furniture | pages [12] -->
获取更多资讯

<!-- b000354 | furniture | pages [13] -->
Team # 2418251

<!-- b000355 | furniture | pages [13] -->
Page 12 of 23

<!-- b000356 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000357 | caption | pages [13] -->
Figure 9: Heatmap of the input features after PCA processing

<!-- b000358 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000359 | caption | pages [13] -->
Figure9 is a heatmap of the three principal components obtained through principal component analysis

<!-- b000360 | prose | pages [13] -->
(PCA) dimensionality reduction. The three columns represent the three input vectors, and the color intensity represents the magnitude of the input values.

<!-- b000361 | heading | pages [13] -->
Momentum Model Based on Support Vector Machines (SVM)

<!-- b000362 | prose | pages [13] -->
4.4

<!-- b000363 | prose | pages [13] -->
“Potential points” are a discrete variable with strong linear correlation; therefore, by establishing a machine learning model and inputting principal component features with “potential points” as the reference output feature, we can derive the output momentum of the athlete.

<!-- b000364 | prose | pages [13] -->
Support Vector Machines are a typical machine learning algorithm that uses the hyperplane concept to perform regression modeling, obtaining the momentum value for each game point of an athlete. We deﬁne the three main components as X1,X2 and X3, forming the input feature matrix X = [X1, X2, X3]

<!-- b000365 | prose | pages [13] -->
Based on the SVM regression formula, we can derive the calculation method for the momentum value Mo.

<!-- b000366 | prose | pages [13] -->
Mo = W T X + b (17)

<!-- b000367 | prose | pages [13] -->
Here, Morepresents the output momentum, X represents the input feature matrix. W denotes the normal vector of the hyperplane, and b denotes the bias term of the hyperplane. The parameters of the model are solved by minimizing the objective function, thereby making predictions for the variables.

<!-- b000368 | prose | pages [13] -->
1 2 ∥W∥2

<!-- b000369 | prose | pages [13] -->
minW,b

<!-- b000370 | prose | pages [13] -->
 

<!-- b000371 | prose | pages [13] -->


<!-- b000372 | prose | pages [13] -->
 

<!-- b000373 | prose | pages [13] -->
W T X + b

<!-- b000374 | prose | pages [13] -->
≥1

<!-- b000375 | prose | pages [13] -->
s.t.

<!-- b000376 | prose | pages [13] -->
Mo

<!-- b000377 | prose | pages [13] -->
(18)

<!-- b000378 | prose | pages [13] -->
The optimization of SVM is achieved by introducing a kernel function to map low-dimensional features to a high-dimensional space. This model uses the Gaussian kernel function for feature mapping.

<!-- b000379 | prose | pages [13] -->
Using MATLAB software, we train a model with the data from the Wimbledon ﬁnal between Carlos Al- caraz and Novak Djokovic (2023-wimbledon-1701). We perform Principal Component Analysis (PCA) on the match data considering “Potential point_Serve”, “Potential point_Serve”, “Potential point_Continuous Scoring Process”, “Potential point_Unforced errors”, and the distance run per game. This analysis yields

<!-- b000380 | furniture | pages [13] -->
关注数学模型

<!-- b000381 | furniture | pages [13] -->
2

<!-- b000382 | furniture | pages [13] -->
MATHmodels

<!-- b000383 | furniture | pages [13] -->
获取更多资讯

<!-- b000384 | furniture | pages [14] -->
Team # 2418251

<!-- b000385 | furniture | pages [14] -->
Page 13 of 23

<!-- b000386 | prose | pages [14] -->
three principal components and the potential points for each game. These are then inputted into an SVM- based momentum calculation model to obtain the momentum for each game for both players.

<!-- b000387 | caption | pages [14] -->
Table 6: Player_1:Carlos Alcaraz’s momentum points and momentum data

<!-- b000388 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000389 | prose | pages [14] -->
Mb Ms Mc Mu Set_no.

<!-- b000390 | prose | pages [14] -->
Game_no.

<!-- b000391 | prose | pages [14] -->
1 1 0 0 2 1 1 2 0 3 0 2 1 3 0 0 2 1 · · · · · · · · · · · · · · · · · · 5 10 0 3 0 1

<!-- b000392 | prose | pages [14] -->
Distance_run Potential points Momentum

<!-- b000393 | prose | pages [14] -->
138.548 1.5 2.3798 83.235 2 1.1220 224.138 1.5 2.3152 · · · · · · · · · 99.511 2.5 1.5982

<!-- b000394 | caption | pages [14] -->
Table 7: Player_2:Novak Djokovic’s potential points and momentum data

<!-- b000395 | prose | pages [14] -->
Mb Ms Mc Mu Set_no.

<!-- b000396 | prose | pages [14] -->
Game_no.

<!-- b000397 | prose | pages [14] -->
1 1 0 3 4 1 1 2 5 0 2 0

<!-- b000398 | prose | pages [14] -->
Distance_run Potential points Momentum

<!-- b000399 | prose | pages [14] -->
130.689 6.5 6.9377 95.182 7 6.5994

<!-- b000400 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000401 | prose | pages [14] -->
1 3 0 3 2 1 · · · · · · · · · · · · · · · · · · 5 10 0 0 0 0 206.149 4.5 4.1993 · · · · · · · · · 143.272 0 0.1831

<!-- b000402 | caption | pages [14] -->
Figure 10 presents the input of three principal components, with the athlete’s potential points as the

<!-- b000403 | prose | pages [14] -->
output feature for prediction. The blue solid line represents the athlete’s potential points in each game, while the red dashed line represents the athlete’s momentum. The model has a mean squared error (MSE) of 0.1735 and an R2 value of 0.90142, indicating a reliable ﬁt accuracy.

<!-- b000404 | caption | pages [14] -->
Figure 10: Momentum model based on SVM training.

<!-- b000405 | prose | pages [14] -->
Subsequently, for the Wimbledon ﬁnal between Carlos Alcaraz and Novak Djokovic (2023-wimbledon- 1701), we accumulated the momentum of each set for both players to obtain the cumulative momentum changes per set. We also visualized the momentum for each point and for each set to describe the momentum shifts during different stages of the match.

<!-- b000406 | furniture | pages [14] -->
关注数学模型

<!-- b000407 | furniture | pages [14] -->
2

<!-- b000408 | furniture | pages [14] -->
MATHmodels

<!-- b000409 | furniture | pages [14] -->
获取更多资讯

<!-- b000410 | furniture | pages [15] -->
Team # 2418251

<!-- b000411 | furniture | pages [15] -->
Page 14 of 23

<!-- b000412 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000413 | caption | pages [15] -->
Figure 11: Comparison of the momentum for

<!-- b000414 | prose | pages [15] -->
each game between the two players

<!-- b000415 | caption | pages [15] -->
Figure 12: Comparison of the accumulated

<!-- b000416 | prose | pages [15] -->
momentum between the two players

<!-- b000417 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000418 | prose | pages [15] -->
In the ﬁgure11 and 12, the purple line represents player 1, Carlos Alcaraz, showing his momentum and accumulated momentum. The blue line represents Novak Djokovic, indicating his momentum and accumulated momentum. The single-game momentum reveals the alternating lead between the two players, while the accumulated momentum provides a clearer view of each player’s performance and lead in every set. As shown in Figure 12, Player 2 (Novak Djokovic) had strong momentum in the ﬁrst set, but Player 1 (Carlos Alcaraz) overtook him in the second and third sets. In the fourth set, Player 2 regained the lead. The ﬁnal set saw both players repeatedly trading the lead, aligning with the actual course of the ﬁnal match described in the problem.

<!-- b000419 | prose | pages [15] -->
Statistical Test of Factors Affecting Momentum 4.5

<!-- b000420 | prose | pages [15] -->
There are many factors that can inﬂuence momentum during a match, so it is necessary to identify which factors are most closely related to momentum shifts and whether momentum affects a player’s likelihood of winning.

<!-- b000421 | prose | pages [15] -->
The Impact of Momentum on the Probability of Winning a Match 4.5.1

<!-- b000422 | prose | pages [15] -->
Based on Model 1, we have developed a winning probability model for athletes’ serving and receiving. And Table 8 shows the momentum and winning probability of Player 1 and Player 2 from Model.

<!-- b000423 | caption | pages [15] -->
Table 8: The momentum and Winning Probability of Player 1 and Player 2

<!-- b000424 | prose | pages [15] -->
Winning probability_P1 Set_no.

<!-- b000425 | prose | pages [15] -->
Game_no.

<!-- b000426 | prose | pages [15] -->
Momentum_P1

<!-- b000427 | prose | pages [15] -->
1 1 2.3798 0.339 1 2 3.5018 0.329 1 3 5.8170 0.284 · · · · · · · · · · · · 5 10 1.5982 0.588

<!-- b000428 | prose | pages [15] -->
Momentum_P2 Winning probability_P1

<!-- b000429 | prose | pages [15] -->
6.9377 0.661 6.5994 0.671 4.1993 0.716 · · · · · · 0.1831 0.412

<!-- b000430 | prose | pages [15] -->
We calculated the Spearman’s rank correlation coefﬁcient between Player 1 and their winning percent-

<!-- b000431 | furniture | pages [15] -->
关注数学模型

<!-- b000432 | furniture | pages [15] -->
2

<!-- b000433 | furniture | pages [15] -->
MATHmodels

<!-- b000434 | furniture | pages [15] -->
获取更多资讯

<!-- b000435 | furniture | pages [16] -->
Team # 2418251

<!-- b000436 | furniture | pages [16] -->
Page 15 of 23

<!-- b000437 | prose | pages [16] -->
age, as well as between Player 2 and their winning percentage, to determine the direct association between winning rate and momentum. This relationship is visualized in a heatmap.

<!-- b000438 | prose | pages [16] -->
In the heatmap as follow, the Spearman’s rank correlation coefﬁcient between Player 1’s winning rate

<!-- b000439 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000440 | prose | pages [16] -->
and momentum is 0.704, while for Player 2 it is 0.729. Therefore, there is a close relationship between momentum and the players’ winning percentage. Changes in momentum signiﬁcantly affect the athletes’ chances of winning.

<!-- b000441 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000442 | caption | pages [16] -->
Figure 13: The direct correlation between the winning percentage and momentum for Player 1 and Player 2

<!-- b000443 | prose | pages [16] -->
The Impact of other Factors on Momentum 4.5.2

<!-- b000444 | prose | pages [16] -->
During the model-building process, we incorporated ﬁve features: Mb, Ms , Mc, Mu and Distance_run to reference the momentum. Therefore, we calculated the Spearman’s coefﬁcient correlation coefﬁcient for these ﬁve inﬂuencing factors with respect to each of the two players, and the results are shown in the table below:

<!-- b000445 | caption | pages [16] -->
Table 9: Spearman coefﬁcients of momentum with related factors_P1

<!-- b000446 | prose | pages [16] -->
Mc_P1 Mb_P1 Ms_P1 Spearman’s coefﬁcient

<!-- b000447 | prose | pages [16] -->
Momentum_P1 0.457 0.49 0.868

<!-- b000448 | prose | pages [16] -->
Mu_P1 Distance_run_P1 Momentum_P2

<!-- b000449 | prose | pages [16] -->
0.032 -0.031 -0.654

<!-- b000450 | caption | pages [16] -->
Table 10: Spearman coefﬁcients of momentum with related factors_P2

<!-- b000451 | prose | pages [16] -->
Mc_P2 Mb_P2 Ms_P2 Spearman’s coefﬁcient

<!-- b000452 | prose | pages [16] -->
Momentum_P2 0.436 0.435 0.871

<!-- b000453 | prose | pages [16] -->
Mu_P2 Distance_run_P2 Momentum_P1

<!-- b000454 | prose | pages [16] -->
0.102 -0.235 -0.654

<!-- b000455 | heading | pages [16] -->
Predictive Model for Shifts in Momentum

<!-- b000456 | prose | pages [16] -->
5

<!-- b000457 | prose | pages [16] -->
From the modeling process above, we know that momentum has a certain impact on the transforma- tion of the game’s ﬂow. Therefore, this section will establish a predictive model to forecast the shifts in momentum during the match.

<!-- b000458 | furniture | pages [16] -->
关注数学模型

<!-- b000459 | furniture | pages [16] -->
2

<!-- b000460 | furniture | pages [16] -->
MATHmodels

<!-- b000461 | furniture | pages [16] -->
获取更多资讯

<!-- b000462 | furniture | pages [17] -->
Team # 2418251

<!-- b000463 | furniture | pages [17] -->
Page 16 of 23

<!-- b000464 | heading | pages [17] -->
Accumulated Momentum Prediction Model Based on ARIMA

<!-- b000465 | prose | pages [17] -->
5.1

<!-- b000466 | prose | pages [17] -->
The cumulative momentum of athletes has a certain time series and cyclical volatility. We choose the ARIMA algorithm to construct the predictive model. ARIMA (Autoregressive Integrated Moving Average)

<!-- b000467 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000468 | prose | pages [17] -->
is a statistical model used for time series analysis. Its principle is based on the autocorrelation of time series and the moving average properties, and then it obtains the trend of the time series by differencing the data and ﬁtting the model.It is divided into: the Autoregressive part (AR), the Integrated part (I), and the Moving Average part (MA).

<!-- b000469 | prose | pages [17] -->
ARIMA(p,d,q) model is as following:

<!-- b000470 | prose | pages [17] -->
p X

<!-- b000471 | prose | pages [17] -->
m′

<!-- b000472 | prose | pages [17] -->
q X

<!-- b000473 | prose | pages [17] -->
αimi + εt +

<!-- b000474 | prose | pages [17] -->
t = α0 +

<!-- b000475 | prose | pages [17] -->
i=1

<!-- b000476 | prose | pages [17] -->
βiεt−i (19)

<!-- b000477 | prose | pages [17] -->
i=1

<!-- b000478 | prose | pages [17] -->
In the ARIMA(p,d,q) model, α0 is the initial constant term. αi represents the autoregressive coefﬁ- cients, indicating the impact of the past p observations on the current value. βi denotes the moving average coefﬁcients, showing the effect of the past q errors on the current value. ε is the error term. mi stands for

<!-- b000479 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000480 | prose | pages [17] -->
the accumulated momentum at previous moments, and m′

<!-- b000481 | prose | pages [17] -->
t is the predicted accumulated momentum for the next moment. p signiﬁes the order of the autoregressive part, q signiﬁes the order of the moving average, and d signiﬁes the order of differencing.

<!-- b000482 | prose | pages [17] -->
We use MATLAB to implement the aforementioned operations to perform data prediction for the accumulated momentum of Carlos Alcaraz and Novak Djokovic in their Wimbledon ﬁnal match (2023- wimbledon-1701).

<!-- b000483 | prose | pages [17] -->
Given the signiﬁcant ﬂuctuation trends in momentum for both players, we choose to use a 4th order autoregressive, 4th order moving average, and 1st order difference to construct an ARIMA model, that is, p=4, d=1, q=4, to obtain detrended data and apply it in the model.

<!-- b000484 | prose | pages [17] -->
By inputting the accumulated momentum of Carlos Alcaraz and Novak Djokovic from their previous ﬁve sets into the model, we predict the accmulated momentum values if they were to continue playing for another ten games. The result is shown in ﬁgure14.

<!-- b000485 | caption | pages [17] -->
Table 11: Accumulated momentum predicted for the next ten games

<!-- b000486 | prose | pages [17] -->
Accumulated momentum predicted for the next ten games

<!-- b000487 | prose | pages [17] -->
1 2 3 4 5 6 7 8 9 10

<!-- b000488 | prose | pages [17] -->
Carlos Alcaraz Novak Djokovic

<!-- b000489 | prose | pages [17] -->
27.0156 26.4919 23.6921 27.5516 27.2556 20.7143 27.1483 13.0571 32.2795 12.0164 33.1069 16.7490 36.1148 20.6293 35.4353 21.1249 34.3283 20.1466 34.3283 19.3927

<!-- b000490 | furniture | pages [17] -->
关注数学模型

<!-- b000491 | furniture | pages [17] -->
2

<!-- b000492 | furniture | pages [17] -->
MATHmodels

<!-- b000493 | furniture | pages [17] -->
获取更多资讯

<!-- b000494 | furniture | pages [18] -->
Team # 2418251

<!-- b000495 | furniture | pages [18] -->
Page 17 of 23

<!-- b000496 | prose | pages [18] -->
And, the corresponding visualization is showed below:

<!-- b000497 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000498 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000499 | caption | pages [18] -->
Figure 14: A accumulated momentum prediction chart for two players.

<!-- b000500 | prose | pages [18] -->
In the ﬁgure14, the dark purple and dark green lines represent the cumulative momentum trends of player 1 and 2 (Carlos Alcaraz and Novak Djokovic) for the ﬁrst ﬁve sets, respectively. The light purple and light green represent the predicted momentum values for the next ten games for both players. In future matches, it is possible that Carlos Alcaraz may continue to lead with a signiﬁcant advantage over Novak Djokovic.

<!-- b000501 | prose | pages [18] -->
5.2 Advice Based on Shifts in Momentum

<!-- b000502 | prose | pages [18] -->
Based on the modeling and analysis results, we offer the following three pieces of advice as follows:

<!-- b000503 | prose | pages [18] -->
• Capitalize on your service games. By quickly establishing dominance at the start of a service game, you can exert greater pressure on your opponent, thus gaining better control of the match’s rhythm and achieving a higher cumulative momentum. Players should practice this aspect during training to improve the quality of their serve.

<!-- b000504 | prose | pages [18] -->
• Capitalize on break points. Break points are a critical juncture and a key moment for momentum shifts. Players can disrupt their opponent’s rhythm by altering their own service return pace during the opponent’s service games, making it difﬁcult for the opponent to adapt. Seize opportunities: Once a chance arises, decisively exploit your strengths to attempt a break in the opponent’s service game.

<!-- b000505 | prose | pages [18] -->
• Continuous scoring. Moments of consecutive scoring often lead to signiﬁcant momentum shifts. Therefore, it’s essential to capitalize on your streaks, maintain an aggressive offensive stance, strive to seize the initiative, target your opponent’s weaknesses, and be bold in attempting risky shots to push through and win the match. When your opponent is on a scoring streak, look for opportunities to break the deadlock or seek a timeout for adjustments.

<!-- b000506 | furniture | pages [18] -->
关注数学模型

<!-- b000507 | furniture | pages [18] -->
2

<!-- b000508 | furniture | pages [18] -->
MATHmodels

<!-- b000509 | furniture | pages [18] -->
获取更多资讯

<!-- b000510 | furniture | pages [19] -->
Team # 2418251

<!-- b000511 | furniture | pages [19] -->
Page 18 of 23

<!-- b000512 | heading | pages [19] -->
Veriﬁcation and Application of the Model

<!-- b000513 | prose | pages [19] -->
6

<!-- b000514 | prose | pages [19] -->
Veriﬁcation within the Same Type of Competition 6.1

<!-- b000515 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000516 | prose | pages [19] -->
To verify the accuracy of the momentum model, we selected another match featuring different players, Daniil Medvedev and Christopher Eubanks, from the 2023 Wimbledon tournament (match code: 1502). Player 1 is Daniil Medvedev, and Player 2 is Christopher Eubanks. We trained the model using their match data, which included break points, serve points, continuous scoring points, unforced error points, and dis- tance run per game. We performed principal component analysis and momentum point calculation to obtain four principal components and the potential points for each game. These were then input into the SVM momentum calculation model to determine the momentum and accumulated momentum for each player in every game.

<!-- b000517 | caption | pages [19] -->
Table 12: Daniil Medvedev’s momentum data

<!-- b000518 | prose | pages [19] -->
Set_no.

<!-- b000519 | prose | pages [19] -->
Gmae_no.

<!-- b000520 | prose | pages [19] -->
M_b M_s M_c M_u DR M Mo A-Mo

<!-- b000521 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000522 | prose | pages [19] -->
1 1 0 0 0 2 2 0 3 2 3 3 5 0 2 · · · · · · · · · · · · · · · 5 7 5 0 2 0 92.263 0 -0.143 -0.183 0 18.837 5 4.667 4.484 0 92.433 7 6.661 11.145 · · · · · · · · · · · · · · · 0 47.094 6.5 6.371 34.379

<!-- b000523 | caption | pages [19] -->
Table 13: Christopher Eubanks’s momentum data

<!-- b000524 | prose | pages [19] -->
Set_no.

<!-- b000525 | prose | pages [19] -->
Gmae_no.

<!-- b000526 | prose | pages [19] -->
M_b M_s M_c

<!-- b000527 | prose | pages [19] -->
1 1 0 3 2 2 2 0 0 0 3 3 0 3 0 · · · · · · · · · · · · · · · 5 7 5 0 3

<!-- b000528 | prose | pages [19] -->
M_u DR M Mo A-Mo

<!-- b000529 | prose | pages [19] -->
0 93.806 5 4.583 4.583 0 18.671 0 -0.100 4.483 4 96.703 1 0.724 5.207 · · · · · · · · · · · · · · · 4 80.886 3 3.362 18.404

<!-- b000530 | prose | pages [19] -->
*Note: Set_no. represents the set number; Game_no. represents the game number; M_b , M_s , M_c and M_u,represent potential points related to break points, service points, continuous scoring points,unforced errors, respectively; DR represents distance run; M represents total potential points; Mo represents momen- tum; A-Mo represents accumulated momentum.

<!-- b000531 | prose | pages [19] -->
We visualized the momentum and accumulated momentum for both players, which are showed in ﬁg- ure15 and 16.

<!-- b000532 | furniture | pages [19] -->
关注数学模型

<!-- b000533 | furniture | pages [19] -->
2

<!-- b000534 | furniture | pages [19] -->
MATHmodels

<!-- b000535 | furniture | pages [19] -->
获取更多资讯

<!-- b000536 | furniture | pages [20] -->
Team # 2418251

<!-- b000537 | furniture | pages [20] -->
Page 19 of 23

<!-- b000538 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000539 | caption | pages [20] -->
Figure 15: Comparison of the momentum for

<!-- b000540 | prose | pages [20] -->
each game between the two players

<!-- b000541 | caption | pages [20] -->
Figure 16: Comparison of the accumulated

<!-- b000542 | prose | pages [20] -->
momentum between the two players

<!-- b000543 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000544 | prose | pages [20] -->
In the ﬁgure15 and 16, the purple line represents Player 1, Daniil Medvedev’s momentum and accum- lated momentum. The green line represents Christopher Eubanks’s momentum and accumulated momen- tum. The single game momentum shows the alternating lead in momentum between the two players, while the accumulated momentum provides a clearer view of each player’s performance and lead throughout each set. As shown in Figure 16, Player 1 (Daniil Medvedev) had strong momentum in the ﬁrst set, but Player 2 (Christopher Eubanks) overtook him in the second and third sets. In the fourth and ﬁfth sets, Player 2’s mo- mentum surpassed Player 1’s again, aligning with the actual course of the match. Therefore, our momentum model demonstrates a certain level of generality across other tennis matches.

<!-- b000545 | prose | pages [20] -->
Application to other Types of Competitions 6.2

<!-- b000546 | prose | pages [20] -->
For other types of competitions, continuous scoring often occurs in ball sports and is highly correlated with momentum, making it a valuable input feature for reference. In other ball sports, the advantage gap between serving and receiving is not signiﬁcant; hence, serve reception and breaks will not impact momen- tum as much. Additionally, a player’s psychological state, physical ﬁtness, and court environment can all affect their momentum, and these factors should also be considered. Therefore, the computational principles of our model are universally applicable across many types of competitions, but the indicators included in the calculations should be adjusted according to the type of sport. In summary, the model’s computational principles have a certain applicability in various competitions.

<!-- b000547 | prose | pages [20] -->
7

<!-- b000548 | heading | pages [20] -->
Sensitivity Analysis

<!-- b000549 | prose | pages [20] -->
We conduct a sensitivity analysis on the momentum model to verify the sensitivity of its various input parameters.

<!-- b000550 | prose | pages [20] -->
Firstly, we adjust the weights of the momentum point model and recalculate the new momentum based on principal components, comparing it with the originally calculated momentum. We use the ﬁnal match of Carlos Alcaraz and Novak Djokovic at Wimbledon 2023 (2023-wimbledon-1701) as reference data, with Carlos Alcaraz as Player 1 and Novak Djokovic as Player 2. Subsequently, we increase the weights of break-of-serve potential points, serving potential points, continuous scoring momentum points, and error momentum points by 50% in the momentum point calculation model, re-enter them into the SVM model

<!-- b000551 | furniture | pages [20] -->
关注数学模型

<!-- b000552 | furniture | pages [20] -->
2

<!-- b000553 | furniture | pages [20] -->
MATHmodels

<!-- b000554 | furniture | pages [20] -->
获取更多资讯

<!-- b000555 | furniture | pages [21] -->
Team # 2418251

<!-- b000556 | furniture | pages [21] -->
Page 20 of 23

<!-- b000557 | prose | pages [21] -->
to obtain four corresponding momentum sets, and compare these with the momentum calculated from the previous question. The results are shown in the ﬁgure below.

<!-- b000558 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000559 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000560 | caption | pages [21] -->
Figure 17: Player 1 Momentum sensitivity

<!-- b000561 | prose | pages [21] -->
analysis

<!-- b000562 | caption | pages [21] -->
Figure 18: Player 2 Momentum sensitivity

<!-- b000563 | prose | pages [21] -->
analysis

<!-- b000564 | prose | pages [21] -->
As shown in the ﬁgure17 and 18, the red line represents the momentum of Player 1 and Player 2 as cal- culated by the previous model, while the other colors represent the momentum recalculated after perturbing one weight. The results indicate that our model is sensitive.

<!-- b000565 | prose | pages [21] -->
8

<!-- b000566 | heading | pages [21] -->
Strengths and Weaknesses

<!-- b000567 | prose | pages [21] -->
8.1

<!-- b000568 | heading | pages [21] -->
Strengths

<!-- b000569 | prose | pages [21] -->
1) Introduce multiple features such as serving, breaking serve, continuous scoring, errors, and distance run to characterize momentum points, momentum, and cumulative momentum in stages. This provides a more comprehensive and speciﬁc portrayal of the athlete’s performance during the match.

<!-- b000570 | prose | pages [21] -->
2) The modeling process employs machine learning algorithms and the ARIMA algorithm, supplemented by statistical parameter validation, making the results scientiﬁcally credible.

<!-- b000571 | prose | pages [21] -->
3) This model can comprehensively depict the changes in an athlete’s momentum during a match, providing coaches with a scientiﬁc research benchmark.

<!-- b000572 | prose | pages [21] -->
8.2

<!-- b000573 | heading | pages [21] -->
Weaknesses

<!-- b000574 | prose | pages [21] -->
1) This model does not consider the impact of non-statistical factors such as the athletes’ psychological states and the environmental conditions of the competition venue on momentum. In actual matches, an athlete’s psychological state and the condition of the playing environment can have a certain effect on their performance.

<!-- b000575 | prose | pages [21] -->
2) The parameters considered by this model are mostly characteristic of tennis; when applying it to other types of sports, corresponding features of the sport in question should be reselected.

<!-- b000576 | furniture | pages [21] -->
关注数学模型

<!-- b000577 | furniture | pages [21] -->
2

<!-- b000578 | furniture | pages [21] -->
MATHmodels

<!-- b000579 | furniture | pages [21] -->
获取更多资讯

<!-- b000580 | furniture | pages [22] -->
Team # 2418251

<!-- b000581 | furniture | pages [22] -->
Page 21 of 23

<!-- b000582 | heading | pages [22] -->
Memorandum

<!-- b000583 | prose | pages [22] -->
To: Coach A

<!-- b000584 | prose | pages [22] -->
From: Team 2418251

<!-- b000585 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000586 | prose | pages [22] -->
Subject: Tennis Strategy Recommendations Based on Momentum

<!-- b000587 | prose | pages [22] -->
Date: Monday, February 5, 2024

<!-- b000588 | prose | pages [22] -->
Based on our team’s modeling and analysis, we have summarized a report for you. This may aid in your guidance and training of tennis players. Our report will unfold in three parts.

<!-- b000589 | prose | pages [22] -->
Firstly, the summary of results:Our team established a Momentum Machine Learning model (MML) using characteristics such as serving, break points, consecutive scoring, unforced errors, and distance run, to quantitatively calculate the momentum of tennis players for each game, and processed this to determine the cumulative momentum of the player for the set.We created an

<!-- b000590 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000591 | prose | pages [22] -->
ARIMA predictive model and analyzed the time series trends of the player’s cumulative momentum during the match, thereby predicting the player’s momentum for the upcoming games. Additionally, through statistical testing, we concluded that there is a strong correlation between a tennis player’s momentum and their winning rate.

<!-- b000592 | prose | pages [22] -->
Secondly, based on our evaluation, we give our recommendations:

<!-- b000593 | prose | pages [22] -->
• Utilize the momentum from serving by observing the opponent’s receiving abilities and weak- nesses, guiding players to adjust their serving strategies, and encouraging more risk-taking in serving when players score consecutively.

<!-- b000594 | prose | pages [22] -->
• Utilize momentum from the break point perspective by training players to recognize and exploit weak service games with aggressive returns, maintaining focus for better chances at breaking serve.

<!-- b000595 | prose | pages [22] -->
• Maintain momentum from consecutive scoring by encouraging an attacking style while re- minding players to avoid overconfidence, ensuring a stable performance.

<!-- b000596 | prose | pages [22] -->
• Utilize momentum from errors by helping players stay calm, learn from mistakes, and adjust tactics to regain match rhythm.

<!-- b000597 | prose | pages [22] -->
• Utilize running distance to maintain momentum by optimizing movement, saving energy, and exploiting the opponent’s stamina through tactical adjustments.

<!-- b000598 | prose | pages [22] -->
Thirdly, the training strategies: In tennis matches, to enhance a player’s momentum, coaches should have players strengthen their serve training, focusing on variations in speed, placement, and spin while preparing multiple serving strategies to adjust according to the opponent; improve the quality of returns, forcing opponents to make errors and creating break opportunities; cultivate quick decision-making skills, knowing how to exploit the opponent’s weaknesses and continuously pressuring to gain opportunities for consecutive scoring; maintain a positive attitude in the face of errors, not letting mistakes affect confidence; and enhance physical training to improve players’ movement speed and endurance.

<!-- b000599 | furniture | pages [22] -->
关注数学模型

<!-- b000600 | furniture | pages [22] -->
1

<!-- b000601 | furniture | pages [22] -->
1

<!-- b000602 | furniture | pages [22] -->
2

<!-- b000603 | furniture | pages [22] -->
MATHmodels

<!-- b000604 | furniture | pages [22] -->
获取更多资讯

<!-- b000605 | furniture | pages [23] -->
Team # 2418251

<!-- b000606 | heading | pages [23] -->
References

<!-- b000607 | furniture | pages [23] -->
Page 22 of 23

<!-- b000608 | references | pages [23] -->
[1] https://www.news9live.com/sports/tennis/novak-djokovic-vs-carlos-alcaraz-wimbledon-2023-mens-

<!-- b000609 | references | pages [23] -->
ﬁnal-records-and-milestones-to-watch-out-for-2214729

<!-- b000610 | references | pages [23] -->
微信公众号：数学模型

<!-- b000611 | references | pages [23] -->
[2] Braidwood, J. (2023), Novak Djokovic has created a unique rival is Wimbledon defeat the beginning

<!-- b000612 | references | pages [23] -->
of the end, The Independent,https://www.independent.co.uk/sport/tennis/novak-djokovic-wimbledon-

<!-- b000613 | references | pages [23] -->
ﬁnal-carlos-alcaraz b2376600.html.

<!-- b000614 | references | pages [23] -->
[3] https://www.merriam-webster.com/dictionary/momentum

<!-- b000615 | references | pages [23] -->
[4] Rivera, J. (2023), Tennis scoring, explained: A guide to understanding the rules terms & point sys-

<!-- b000616 | references | pages [23] -->
tem at Wimbledon, The Sporting News,https://www.sportingnews.com/us/tennis/news/tennis-scoring-

<!-- b000617 | references | pages [23] -->
explained-rules-system-points terms/7uzp2evdhbd11obdd59p3p1cx.

<!-- b000618 | references | pages [23] -->
[5] Chen T, Fan Q, Liu K, Le L. Identifying key factors in momentum in basketball games. J Appl Stat.

<!-- b000619 | references | pages [23] -->
2020 Jul 21;48(16):3116-3129. doi: 10.1080/02664763.2020.1795819. PMID: 35707253; PMCID:

<!-- b000620 | references | pages [23] -->
PMC9041568.

<!-- b000621 | references | pages [23] -->
微信号：MATHmodels

<!-- b000622 | references | pages [23] -->
[6] Weimer, Louis, Steinert-Threlkeld, Zachary C., and Coltin, Kevin. ‘A Causal Approach for Detecting

<!-- b000623 | references | pages [23] -->
Team-level Momentum in NBA Games’. 1 Jan. 2023 : 117 132

<!-- b000624 | references | pages [23] -->
[7] Ruud J.R. den Hartigh, Paul L.C van Geert, Nico W. van Yperen, Ralf F.A Cox, Christophe Gernigon.

<!-- b000625 | references | pages [23] -->
Psychological momentum during and across sports matches: Evidence for interconnected time scales..

<!-- b000626 | references | pages [23] -->
Journal of Sport and Exercise Psychology, 2016, 38 (1), pp.82-92. ff10.1123/jsep.2015-0162ff.

<!-- b000627 | references | pages [23] -->
ffhal02519559

<!-- b000628 | furniture | pages [23] -->
关注数学模型

<!-- b000629 | furniture | pages [23] -->
2

<!-- b000630 | furniture | pages [23] -->
MATHmodels

<!-- b000631 | furniture | pages [23] -->
获取更多资讯

<!-- b000632 | furniture | pages [24] -->
Team # 2418251

<!-- b000633 | heading | pages [24] -->
Appendices

<!-- b000634 | prose | pages [24] -->
Page 23

<!-- b000635 | heading | pages [24] -->
Report on Use of AI

<!-- b000636 | ai_disclosure | pages [24] -->
微信公众号：数学模型

<!-- b000637 | ai_disclosure | pages [24] -->
1. Bing AI

<!-- b000638 | ai_disclosure | pages [24] -->
Query1:How to adjust a player’s serve during a tennis match?

<!-- b000639 | ai_disclosure | pages [24] -->
Output:Adjusting a player’s serve during a tennis match can be crucial for improving performance or

<!-- b000640 | ai_disclosure | pages [24] -->
responding to an opponent’s strengths or weaknesses. Here are some general tips for adjusting a player’s

<!-- b000641 | ai_disclosure | pages [24] -->
serve during a match:

<!-- b000642 | ai_disclosure | pages [24] -->
1 Analyze the Opponent: Watch the opponent’s return patterns and tendencies to identify any weak-

<!-- b000643 | ai_disclosure | pages [24] -->
nesses or areas of vulnerability. If the opponent is struggling with a particular type of serve (e.g.,

<!-- b000644 | ai_disclosure | pages [24] -->
wide, body, or T serve), focus on exploiting that weakness.

<!-- b000645 | ai_disclosure | pages [24] -->
2 Change Placement: If the opponent is consistently returning serves well from a certain area of the

<!-- b000646 | ai_disclosure | pages [24] -->
court, consider changing the placement of the serve to exploit other areas. For example, if the oppo-

<!-- b000647 | ai_disclosure | pages [24] -->
nent is consistently attacking your wide serves, try targeting the body or T.

<!-- b000648 | ai_disclosure | pages [24] -->
微信号：MATHmodels

<!-- b000649 | ai_disclosure | pages [24] -->
3 Adjust Speed and Spin: Vary the speed and spin of the serve to keep the opponent off balance. Mix

<!-- b000650 | ai_disclosure | pages [24] -->
up the pace of the serve between fast, medium, and slow serves, as well as adding topspin or slice to

<!-- b000651 | ai_disclosure | pages [24] -->
create variation.

<!-- b000652 | ai_disclosure | pages [24] -->
4 Use Deception: Incorporate deception into your serve by occasionally using a different ball toss or

<!-- b000653 | ai_disclosure | pages [24] -->
motion to keep the opponent guessing. For example, disguising a kick serve as a ﬂat serve or using a

<!-- b000654 | ai_disclosure | pages [24] -->
subtle change in ball toss can catch the opponent off guard.

<!-- b000655 | ai_disclosure | pages [24] -->
Remember that every match is unique, so the speciﬁc adjustments will depend on the opponent’s playing

<!-- b000656 | ai_disclosure | pages [24] -->
style, court conditions, and your own strengths and weaknesses. Constant awareness and adaptability are

<!-- b000657 | ai_disclosure | pages [24] -->
key to making effective adjustments to a player’s serve during a tennis match.

<!-- b000658 | ai_disclosure | pages [24] -->
2. Bing AI

<!-- b000659 | ai_disclosure | pages [24] -->
Query1: How to minimize unforced errors in tennis?

<!-- b000660 | ai_disclosure | pages [24] -->
Output:

<!-- b000661 | ai_disclosure | pages [24] -->
1 Practice regularly: The more you practice, the better you will become at playing tennis. This will help

<!-- b000662 | ai_disclosure | pages [24] -->
you to develop muscle memory and reduce the number of unforced errors you make.

<!-- b000663 | ai_disclosure | pages [24] -->
2 Focus on your footwork: Good footwork is essential in tennis. It helps you to get into the right position

<!-- b000664 | ai_disclosure | pages [24] -->
to hit the ball and reduces the chance of making an unforced error.

<!-- b000665 | ai_disclosure | pages [24] -->
3 Keep your eye on the ball: Always keep your eye on the ball when you are hitting it. This will help

<!-- b000666 | ai_disclosure | pages [24] -->
you to make better contact and reduce the number of unforced errors.

<!-- b000667 | ai_disclosure | pages [24] -->
4 Use the correct technique: Make sure you use the correct technique when hitting the ball. This will

<!-- b000668 | ai_disclosure | pages [24] -->
help you to generate more power and control, reducing the chance of making an unforced error.

<!-- b000669 | ai_disclosure | pages [24] -->
5 Stay relaxed: Tennis can be a stressful game, but it’s important to stay relaxed. If you tense up, you

<!-- b000670 | ai_disclosure | pages [24] -->
are more likely to make an unforced error.

<!-- b000671 | furniture | pages [24] -->
关注数学模型

<!-- b000672 | furniture | pages [24] -->
2

<!-- b000673 | furniture | pages [24] -->
MATHmodels

<!-- b000674 | furniture | pages [24] -->
获取更多资讯
