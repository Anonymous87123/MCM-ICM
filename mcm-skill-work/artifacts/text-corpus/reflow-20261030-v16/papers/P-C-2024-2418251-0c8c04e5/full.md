# P-C-2024-2418251-0c8c04e5

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2024

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
1 Introduction

<!-- b000026 | contents | pages [2] -->
2

<!-- b000027 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000028 | contents | pages [2] -->
1.1

<!-- b000029 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
2

<!-- b000031 | contents | pages [2] -->
1.2

<!-- b000032 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
2

<!-- b000034 | contents | pages [2] -->
1.3

<!-- b000035 | contents | pages [2] -->
Ourwork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
3

<!-- b000037 | contents | pages [2] -->
1.4

<!-- b000038 | contents | pages [2] -->
Assumptions and Justiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
2 Notations

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
3 Establishment and Solution of Single Game Winning Probability Model

<!-- b000043 | contents | pages [2] -->
4

<!-- b000044 | contents | pages [2] -->
3.1 Single Game Winning Probability Model Based on Recurrent Neural Network (RNN)

<!-- b000045 | contents | pages [2] -->
4

<!-- b000046 | contents | pages [2] -->
3.1.1 Serving Player Winning Probability Model

<!-- b000047 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
5

<!-- b000049 | contents | pages [2] -->
3.1.2

<!-- b000050 | contents | pages [2] -->
Receiving Player Winning Probability Model . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
7

<!-- b000052 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000053 | contents | pages [2] -->
3.2 Visualization of the Match Flow

<!-- b000054 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
8

<!-- b000056 | contents | pages [2] -->
4 Establishment and Solution of the Momentum Model

<!-- b000057 | contents | pages [2] -->
8

<!-- b000058 | contents | pages [2] -->
4.1 Feature Selection

<!-- b000059 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
9

<!-- b000061 | contents | pages [2] -->
4.2

<!-- b000062 | contents | pages [2] -->
Potential Point Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
9

<!-- b000064 | contents | pages [2] -->
4.3

<!-- b000065 | contents | pages [2] -->
Principal Component Analysis (PCA) Dimensionality Reduction . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
10

<!-- b000067 | contents | pages [2] -->
4.4 Momentum Model Based on Support Vector Machines (SVM)

<!-- b000068 | contents | pages [2] -->
. . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
12

<!-- b000070 | contents | pages [2] -->
4.5

<!-- b000071 | contents | pages [2] -->
Statistical Test of Factors Affecting Momentum . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
14

<!-- b000073 | contents | pages [2] -->
4.5.1 The Impact of Momentum on the Probability of Winning a Match

<!-- b000074 | contents | pages [2] -->
. . . . .

<!-- b000075 | contents | pages [2] -->
14

<!-- b000076 | contents | pages [2] -->
4.5.2 The Impact of other Factors on Momentum

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
15

<!-- b000079 | contents | pages [2] -->
5 Predictive Model for Shifts in Momentum

<!-- b000080 | contents | pages [2] -->
15

<!-- b000081 | contents | pages [2] -->
5.1

<!-- b000082 | contents | pages [2] -->
Accumulated Momentum Prediction Model Based on ARIMA . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
16

<!-- b000084 | contents | pages [2] -->
5.2

<!-- b000085 | contents | pages [2] -->
Advice Based on Shifts in Momentum . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
17

<!-- b000087 | contents | pages [2] -->
6 Veriﬁcation and Application of the Model

<!-- b000088 | contents | pages [2] -->
18

<!-- b000089 | contents | pages [2] -->
6.1

<!-- b000090 | contents | pages [2] -->
Veriﬁcation within the Same Type of Competition . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
18

<!-- b000092 | contents | pages [2] -->
6.2 Application to other Types of Competitions

<!-- b000093 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
19

<!-- b000095 | contents | pages [2] -->
7 Sensitivity Analysis

<!-- b000096 | contents | pages [2] -->
19

<!-- b000097 | contents | pages [2] -->
8 Strengths and Weaknesses

<!-- b000098 | contents | pages [2] -->
20

<!-- b000099 | contents | pages [2] -->
8.1

<!-- b000100 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000101 | contents | pages [2] -->
20

<!-- b000102 | contents | pages [2] -->
8.2

<!-- b000103 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
20

<!-- b000105 | contents | pages [2] -->
Appendices

<!-- b000106 | contents | pages [2] -->
23

<!-- b000107 | furniture | pages [2] -->
关注数学模型

<!-- b000108 | furniture | pages [2] -->
1

<!-- b000109 | furniture | pages [2] -->
2

<!-- b000110 | furniture | pages [2] -->
MATHmodels

<!-- b000111 | furniture | pages [2] -->
获取更多资讯

<!-- b000112 | furniture | pages [3] -->
Team # 2418251

<!-- b000113 | furniture | pages [3] -->
Page 2 of 23

<!-- b000114 | heading | pages [3] -->
1 Introduction

<!-- b000115 | prose | pages [3] -->
Billy Shirley once said:“Watch Out for Momentum : There may not even be such a thing in sports, but you can be sure you’ll be told whenever it shifts.” 微信公众号：数学模型

<!-- b000116 | heading | pages [3] -->
1.1 Problem Background

<!-- b000117 | prose | pages [3] -->
In the 2023 Wimbledon Gentlemen’s cham- pionship, 20-year-old Carlos Alcaraz emerged victorious against 36-year-old Novak Djokovic, handing Djokovic his ﬁrst Wimbledon defeat since 2013 and halting his remarkable run in Grand Slam tournaments. The ﬁnal was ﬁlled with dramatic turns of performance. Djokovic started strong by claiming the ﬁrst set 6-1, only 微信号：MATHmodels for Alcaraz to make a comeback, securing the second set through a tie-breaker and dominating the third set 6-1. Although Djokovic managed to take the fourth set 6-3, Alcaraz ultimately clinched the win with a 6-4 score in the decid- [1]

<!-- b000118 | caption | pages [3] -->
Figure 1: Novak Djokovic & Carlos Alcaraz

<!-- b000119 | prose | pages [3] -->
ing ﬁfth set. The game showcased notable shifts in momentum, underscoring the difﬁculty in quantifying how various events within the match af- fect a player’s or team’s performance. Yet the omnipresence of momentum is so pervasive that it’s acknowledged not solely by commentators, mentors, and competitors but also sensed by a laid- back spectator lounging on their sofa. So for coaches, comprehending precisely what momentum is can be vital, as this understanding will aid them in directing the game.

<!-- b000120 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000121 | prose | pages [3] -->
Considering the background information and restricted conditions identiﬁed in the problem statement, we need to solve the following problems:

<!-- b000122 | prose | pages [3] -->
• Problem 1:Develop a tennis match ﬂow model to assess player performance, considering serve advantage and visualize the match dynamics.

<!-- b000123 | prose | pages [3] -->
• Problem 2:Assess the tennis coach’s skepticism about the role of “momentum” versus ran- domness in match outcomes using a performance model/metric.

<!-- b000124 | prose | pages [3] -->
• Problem 3:Develop a predictive model for tennis match swings and advise on strategy con- sidering past “momentum” differentials.

<!-- b000125 | prose | pages [3] -->
• Problem 4:Test and validate the tennis swing prediction model on other matches, identify performance factors, and assess generalizability to different contexts.

<!-- b000126 | prose | pages [3] -->
• Problem 5:Include a page memo summarizing results with advice for coaches on the role of “momentum”, and how to prepare players to respond to events that impact the ﬂow of play during a tennis match.

<!-- b000127 | furniture | pages [3] -->
关注数学模型

<!-- b000128 | furniture | pages [3] -->
2

<!-- b000129 | furniture | pages [3] -->
MATHmodels

<!-- b000130 | furniture | pages [3] -->
获取更多资讯

<!-- b000131 | furniture | pages [4] -->
Team # 2418251

<!-- b000132 | furniture | pages [4] -->
Page 3 of 23

<!-- b000133 | heading | pages [4] -->
1.3 Ourwork

<!-- b000134 | prose | pages [4] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000135 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000136 | heading | pages [4] -->
1.4 Assumptions and Justiﬁcation

<!-- b000137 | prose | pages [4] -->
• Assumption 1:Assume that after each set, the athlete’s accumulated momentum is updated.

<!-- b000138 | prose | pages [4] -->
Justiﬁcation:After each set, the athlete gets a chance to rest, stabilize, and the coach will provide corresponding strategies, thus it’s appropriate to update the athlete’s momentum.

<!-- b000139 | prose | pages [4] -->
• Assumption 2:Ignore the impact of tiebreakers on momentum trends.

<!-- b000140 | prose | pages [4] -->
Justiﬁcation:In tiebreakers, the situation changes dramatically with alternating service rights, and the athletes’ mental states are highly tense, so the inﬂuence of momentum is minimal.

<!-- b000141 | prose | pages [4] -->
Therefore, the impact of tiebreakers on momentum trends can be neglected.

<!-- b000142 | prose | pages [4] -->
• Assumption 3:The momentum in each game is discrete.

<!-- b000143 | heading | pages [4] -->
Justiﬁcation:The model considers momentum to be discrete within each game, as there

<!-- b000144 | prose | pages [4] -->
is no more continuous data available to accurately depict it. Therefore, the calculation of momentum is based on discrete intervals within the games.

<!-- b000145 | prose | pages [4] -->
• Assumption 4:Ignore the impact of environmental factors and athletes’ psychological states.

<!-- b000146 | prose | pages [4] -->
Justiﬁcation:The environment of the court, wind speed, and the athletes’ psychological states can all have an impact on the progression of the match. However, since no speciﬁc data is provided in the question and psychological states cannot be quantitatively described, the inﬂuence of these factors is therefore neglected.

<!-- b000147 | furniture | pages [4] -->
关注数学模型

<!-- b000148 | furniture | pages [4] -->
2

<!-- b000149 | furniture | pages [4] -->
MATHmodels

<!-- b000150 | furniture | pages [4] -->
获取更多资讯

<!-- b000151 | furniture | pages [5] -->
Team # 2418251

<!-- b000152 | furniture | pages [5] -->
Page 4 of 23

<!-- b000153 | heading | pages [5] -->
2 Notations

<!-- b000154 | caption | pages [5] -->
Table 1: Notation

<!-- b000155 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000156 | heading | pages [5] -->
Symbol

<!-- b000157 | prose | pages [5] -->
Meaning

<!-- b000158 | prose | pages [5] -->
X1 1 Single-serve rate X2 2 Killing-shot rate X3 3 Error rate X4 4 break-of-serve rate t 5 Total number of balls in a single game tf 6 Number of successful ﬁrst serves tace 7 Number of aces tw 8 Number of winning points tuf 9 Number of unforced errors Yp 10 Winning rate 微信号：MATHmodels Mb 11 Potential point_Break of serve Ms 12 Potential point_Serve Mc 13 Potential point_Continuous Mu 14 Potential point_Unforced Error Mi 15 Potential points of each game M 16 Potential Point i 17 The current game number n 18 Total number of games played in the set Mo 19 Momentum

<!-- b000159 | prose | pages [5] -->
*Note: Here is a partial notation.Detailed explanations for each symbol can be found in the corresponding text.

<!-- b000160 | heading | pages [5] -->
3 Establishment and Solution of Single Game Winning Proba-

<!-- b000161 | prose | pages [5] -->
bility Model

<!-- b000162 | heading | pages [5] -->
3.1 Single Game Winning Probability Model Based on Recurrent Neural

<!-- b000163 | prose | pages [5] -->
Network (RNN)

<!-- b000164 | prose | pages [5] -->
In tennis, players who are serving have a higher probability of winning. Therefore, we construct separate winning probability models for players based on both the serving and receiving aspects. Given the numerous factors that can inﬂuence the outcome of a tennis match, we focus on key features and use neural network methods to build our winning probability model. However, the traditional neural network produces outputs that depend only on the current input, which makes them less capable of accurately predicting data that changes over time. In contrast, the output of Recurrent Neural Network (RNN) is determined by both the current input and the previous moment’s output, similar to adding a memory unit to the neural network. This allows the RNN to remember the behavior from the previous moment and respond appropriately based on the current input and past behavior. Compared to the traditional neural network, which is like a broken chain, RNN exhibits a continuous characteristic. This characteristic makes RNN more suitable for our modeling than the traditional neural network.

<!-- b000165 | furniture | pages [5] -->
关注数学模型

<!-- b000166 | furniture | pages [5] -->
2

<!-- b000167 | furniture | pages [5] -->
MATHmodels

<!-- b000168 | furniture | pages [5] -->
获取更多资讯

<!-- b000169 | furniture | pages [6] -->
Team # 2418251

<!-- b000170 | furniture | pages [6] -->
Page 5 of 23

<!-- b000171 | heading | pages [6] -->
3.1.1 Serving Player Winning Probability Model

<!-- b000172 | prose | pages [6] -->
In the model, we use the win probability in each game as the output feature and select single-serve rate, killing-shot rate, and error rate as the three representative input features. We perform data preprocessing by 微信公众号：数学模型 extracting the given data from the problem and calculating the conversion to the serving player’s single-serve rate, killing-shot rate, and error rate as the input features.

<!-- b000173 | prose | pages [6] -->
X1 = tf (1) t

<!-- b000174 | prose | pages [6] -->
In this equation, t represents the total number of balls in a single game, and tf represents the number of successful ﬁrst serves. Using this equation, we can calculate the single-serve rate X1.

<!-- b000175 | prose | pages [6] -->
We deﬁne the killing-shot rate X2 and the error rate X3 in the same way.

<!-- b000176 | prose | pages [6] -->
X2 = tace (2) tw X3 = tuf (3) 微信号：MATHmodels t

<!-- b000177 | prose | pages [6] -->
We deﬁne the vector Y predicted by three input features as the athlete’s service winning rate.

<!-- b000178 | prose | pages [6] -->
Yp = tw (4) t

<!-- b000179 | prose | pages [6] -->
In the equation 2,3 and 4, tace represents the number of aces, tw represents the number of winning points, and tuf represents the number of unforced errors. Yp represents winning rate, which is based on past data.

<!-- b000180 | prose | pages [6] -->
We construct and input the matrix X = [X1, X2, X3] after extracting the three input feature vectors. For each Xi, we have Xi = (X1, X2, · · · , Xt)T (i = 1, 2, 3, · · · ), where Xt represents the input feature at time t. After determining the features, we process with the propagation of RNN. The process is as follows:

<!-- b000181 | prose | pages [6] -->
ht = f (WihXt + Whhht−1 + bh) (5)

<!-- b000182 | prose | pages [6] -->
yt = Whoht + b0 (6)

<!-- b000183 | prose | pages [6] -->
Where, ht represents the hidden layer state, Wih is the weight matrix from the inputlayer to the hidden layer, Whh is the weight matrix from the hidden layer to itself, and bh is thebias vector for the hidden layer. Who is the weight matrix from the hidden layer to the outputlayer, and bo, is the bias vector for the output layer.

<!-- b000184 | prose | pages [6] -->
Regarding the objective function, we assume that the model’s predicted output is as following:

<!-- b000185 | prose | pages [6] -->
bY = ( ˆy1, ˆy2, · · · , ˆyt)T (7)

<!-- b000186 | prose | pages [6] -->
The actual output is as following:

<!-- b000187 | prose | pages [6] -->
Y = (y1, y2, · · · , yt)T (8)

<!-- b000188 | prose | pages [6] -->
Then the objective function can be deﬁned as following:

<!-- b000189 | prose | pages [6, 7] -->
Pt L = 1 i=1 ( ˆyi −yi)2 (9) t First, we clean the dataset in the problem, removing outliers. Afterward, we use the backpropagation al- gorithm and the optimizer in MATLAB to update the model’s parameters, minimizing the objective function, and thus completing the initial construction of the model.

<!-- b000190 | furniture | pages [6] -->
关注数学模型

<!-- b000191 | furniture | pages [6] -->
2

<!-- b000192 | furniture | pages [6] -->
MATHmodels

<!-- b000193 | furniture | pages [6] -->
获取更多资讯

<!-- b000194 | furniture | pages [7] -->
Team # 2418251

<!-- b000195 | furniture | pages [7] -->
Page 6 of 23

<!-- b000197 | prose | pages [7] -->
微信公众号：数学模型 We incorporated all the data from Novak Djokovic’s service games in the match for model training, calculating his service game winning probability through factors such as the killing-shot rate, single-serve rate, and error rate.

<!-- b000198 | caption | pages [7] -->
Table 2: Novak Djokovic’s service game data from Wimbledon Championship.

<!-- b000199 | prose | pages [7] -->
X1 X2 X3 Yp Match_id Set_no. Game_no. Point_no.

<!-- b000200 | prose | pages [7] -->
1316 1 1 5 0.25 1 0 0.8 1316 1 3 4 0.25 0 0 1 1316 1 5 5 0.25 0.8 0 0.8 · · · · · · · · · · · · · · · · · · · · · · · · 1701 5 9 5 0.25 0.8 0.8 0.8 微信号：MATHmodels Through model calculations, we obtained the service player’s winning probability based on three input features and compared it with the player’s actual winning rate. The results are as follows:

<!-- b000201 | caption | pages [7] -->
Figure 3: The ﬁtting results for the service

<!-- b000202 | caption | pages [7] -->
Figure 4: Histogram of prediction error for

<!-- b000203 | prose | pages [7] -->
player’s winning probability Serving

<!-- b000204 | prose | pages [7] -->
In the ﬁgure 3, the red line represents the winning probability of the service player calculated by the model, and the green line represents the reference winning rate. Both demonstrate a high degree of ﬁtting precision, as shown in the ﬁgure 4 above.

<!-- b000205 | prose | pages [7] -->
In the ﬁgure 4, the pink frequency distribution histogram represents the error distribution frequency of the service winning rate model. The mean squared error (MSE) is 0.012922. The coefﬁcient of determina- tion R2 is 0.56119.

<!-- b000206 | furniture | pages [7] -->
关注数学模型

<!-- b000207 | furniture | pages [7] -->
2

<!-- b000208 | furniture | pages [7] -->
MATHmodels

<!-- b000209 | furniture | pages [7] -->
获取更多资讯

<!-- b000210 | furniture | pages [8] -->
Team # 2418251

<!-- b000211 | furniture | pages [8] -->
Page 7 of 23

<!-- b000212 | heading | pages [8] -->
3.1.2 Receiving Player Winning Probability Model

<!-- b000213 | prose | pages [8] -->
For the construction of a winning probability model for receiving players, we will also use the winning rate of each game as the output feature. However, the input features need to be rebuilt because receiving 微信公众号：数学模型 players have a natural disadvantage compared to serving players. Therefore, when a receiving player breaks of serve, it greatly increases their conﬁdence and winning rate. Therefore, for the receiving player’s win- ning rate model, we select break of serve, killing shot, and error, as representative input features. We will preprocess the data provided in the problem and calculate the receiving player’s killing-shot rate X2, error rate X3, and break-of-serve rate x4. These will be input into an RNN model. We deﬁne break-of-serve rate x4 as following: tbreak X4 = (10) tbreak_point

<!-- b000214 | prose | pages [8] -->
Where,tbreak_point represents the number of times a breakpoint is reached, and tbreak represents the number of successful break-of-serve.

<!-- b000215 | prose | pages [8] -->
Similarly, we train our model using all the data from the service games in which Novak Djokovic 微信号：MATHmodels received the ball. We calculate Novak Djokovic’s receiving game winning probability based on his kill-shot rate, break-of-serve rate, and error rate.

<!-- b000216 | caption | pages [8] -->
Table 3: Novak Djokovic’s receiving game data from Wimbledon Championship.

<!-- b000217 | prose | pages [8] -->
X2 X3 X4 Yp Match_id Set_no. Game_no. Point_no.

<!-- b000218 | prose | pages [8] -->
1316 1 2 8 0.33 0 0.25 0.375 1316 1 4 6 0 0 0.33 0.333 1316 1 6 6 0.25 1 0 0.667 · · · · · · · · · · · · · · · · · · · · · · · · 1701 5 10 6 0.5 0 0 0.33

<!-- b000219 | prose | pages [8] -->
Through the training and calculation of the model, we obtained the winning probability of the receiving player based on three input features, and compared it with the winning rate of the player. The results are as follows:

<!-- b000220 | caption | pages [8] -->
Figure 5: The ﬁtting results for the service

<!-- b000221 | caption | pages [8] -->
Figure 6: Histogram of prediction error for

<!-- b000222 | prose | pages [8, 9] -->
player’s receiving probability receiving In the ﬁgure5, the red line represents the winning probability of the receiving player calculated by the model, and the green line represents the reference winning rate. The two have a high degree of ﬁtting accuracy.

<!-- b000223 | furniture | pages [8] -->
关注数学模型

<!-- b000224 | furniture | pages [8] -->
2

<!-- b000225 | furniture | pages [8] -->
MATHmodels

<!-- b000226 | furniture | pages [8] -->
获取更多资讯

<!-- b000227 | furniture | pages [9] -->
Team # 2418251

<!-- b000228 | furniture | pages [9] -->
Page 8 of 23

<!-- b000230 | prose | pages [9] -->
微信公众号：数学模型 In the ﬁgure 6, the pink frequency distribution histogram represents the error distribution frequency of the service winning rate model. The mean squared error (MSE) is 0.017458. The coefﬁcient of determina- tion R2 is 0.66442.

<!-- b000231 | prose | pages [9] -->
Finally, we compared and visualized the winning probability of serving and receiving for the same player, and obtained the following result:

<!-- b000232 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000233 | caption | pages [9] -->
Figure 7: Comparison of winning probability of serving and receiving

<!-- b000234 | prose | pages [9] -->
In ﬁgure7, the red line represents the winning probability of the server, while the green line represents the wining probability of the receiver. We can conclude that the server’s winning probability is generally higher than that of the receiver. Therefore, serving has a natural advantage, which is closely related to the momentum of the tennis player and also determines the direction of the tennis match.

<!-- b000235 | heading | pages [9] -->
3.2 Visualization of the Match Flow

<!-- b000236 | prose | pages [9] -->
We uses the match data from the Wimbledon ﬁnal between Carlos Alcaraz and Novak Djokovic (2023- wimbledon-1701) as a reference to visualize the match ﬂow.

<!-- b000237 | prose | pages [9] -->
In ﬁgure8, numbers 1 and 2 represent the winning athletes. The blue bar chart indicates the number of games each won, while the line chart describes the point difference between them. Through this chart, we can visually see the ﬂow of the entire match. Overall, the two players were well-matched, and the game was quite intense, with a particular highlight in the second set where it took thirteen games for the winner to emerge. In the end, player 1 secured three sets while player 2 took two sets but ultimately lost.

<!-- b000238 | heading | pages [9] -->
4 Establishment and Solution of the Momentum Model

<!-- b000239 | prose | pages [9, 10] -->
Professional sports have always been a highly competitive industry both on and off the ﬁeld. Gaining an advantage can have crucial effects, which often lead to individual success and team victories. The study of momentum is one of the most challenging topics in sports analytics because while people can deﬁnitely 微信公众号：数学模型

<!-- b000240 | furniture | pages [9] -->
关注数学模型

<!-- b000241 | furniture | pages [9] -->
2

<!-- b000242 | furniture | pages [9] -->
MATHmodels

<!-- b000243 | furniture | pages [9] -->
获取更多资讯

<!-- b000244 | furniture | pages [10] -->
Team # 2418251

<!-- b000245 | furniture | pages [10] -->
Page 9 of 23

<!-- b000247 | caption | pages [10] -->
Figure 8: 2023-Wimbledon-1701

<!-- b000248 | prose | pages [10] -->
sense a "winning streak" when it occurs, expressing it is still difﬁcult. Therefore, we have established 微信号：MATHmodels a momentum computation model based on machine learning to quantitatively analyze the momentum of players.[5]

<!-- b000249 | heading | pages [10] -->
4.1 Feature Selection

<!-- b000250 | prose | pages [10] -->
The manifestation of momentum is often a sense of power that a tennis player experiences when winning a match, and it is closely linked to the signiﬁcant progressions within the game. Since crucial points and progressions tend to inﬂuence the direction of the match, gaining or losing key points can lead to an increase or decrease in momentum. Therefore, we use the following events during a tennis match to describe the characteristics of momentum:

<!-- b000251 | prose | pages [10] -->
• Serve:Serving is crucial in tennis, especially when players are evenly matched, giving the server a higher chance of winning. A good serve, fast, with spin and varied placement, challenges the opponent’s defense. Servers can control the match pace and upset the opponent’s rhythm. Variations in serving can also disrupt the opponent’s return, creating offensive opportunities.

<!-- b000252 | prose | pages [10] -->
• Continuous Scoring Process:Consecutive scoring enhances conﬁdence and morale, im- proving focus and stroke technique. It can develop a “striking habit”, leading to smoother, more precise shots. This reﬂects the buildup of momentum in a match.

<!-- b000253 | prose | pages [10] -->
• Break of Serve:Achieving a break of serve boosts conﬁdence and momentum, as it signiﬁes an advantage. It encourages better performance and alters match dynamics, putting the player who broke ahead and forcing the opponent to break back. This affects both players’ mental states and strategies.

<!-- b000254 | prose | pages [10] -->
• Unforced Errors:Frequent unforced errors can damage conﬁdence and morale, leading to un- derperformance. They disrupt match dynamics, increase tension, and affect the athlete’s mental state and strategy, impacting momentum negatively.

<!-- b000255 | heading | pages [10] -->
4.2 Potential Point Model

<!-- b000256 | prose | pages [10, 11] -->
The concept of potential pointis a discrete state concept used to describe the condition of an athlete at a certain point or stage in a competition. Thus, the entire process of the athlete’s competition is discretized into games, and the athlete’s performance in the current game is characterized by speciﬁc scores. The sum of these scores constitutes the potential point.

<!-- b000257 | furniture | pages [10] -->
关注数学模型

<!-- b000258 | furniture | pages [10] -->
2

<!-- b000259 | furniture | pages [10] -->
MATHmodels

<!-- b000260 | furniture | pages [10] -->
获取更多资讯

<!-- b000261 | furniture | pages [11] -->
Team # 2418251

<!-- b000262 | furniture | pages [11] -->
Page 10 of 23

<!-- b000264 | prose | pages [11] -->
• “Potential point_Serve” Ms:During the athlete’s service, they have a greater advantage, and we 微信公众号：数学模型 deﬁne that for each service game, the athlete earns potential points, which are quantiﬁed as 2 points, meaning Ms=2.

<!-- b000265 | prose | pages [11] -->
• “Potential point_Continuous Scoring Process” Mc: Athletes often gain more conﬁdence when they score consecutively. We deﬁne that for every three consecutive points scored, a potential point for consecutive scoring is earned, quantiﬁed as 2 points, meaning Mc=2. Within a game, an ath- lete may achieve multiple instances of consecutive scoring; in such cases, the potential points for consecutive scoring can be cumulative.

<!-- b000266 | prose | pages [11] -->
• “Potential point_Break of Serve” Mb: When an athlete achieves a break in a game, the potential point earned is characterized by 5 points, meaning Mb=5.

<!-- b000267 | prose | pages [11] -->
• “Potential point_Unforced Errors” Mu: Athletes often commit one or more unforced errors during 微信号：MATHmodels a match, which can signiﬁcantly impact their momentum negatively. We deﬁne that each occurrence of an unforced error reduces the potential points by 0.5, meaning Mu= -0.5. Since errors can happen multiple times in a match, this value can also accumulate.

<!-- b000268 | prose | pages [11] -->
In this way, we can obtain the potential point Mi for each game of the athlete as following:

<!-- b000269 | prose | pages [11] -->
X X Mi = Mb + Ms + Mc + Mu (11)

<!-- b000270 | prose | pages [11] -->
Where, Mb,Ms,Mc and Mu represent “Potential point_Break of serve”,“Potential point_Serve”, “Potential point_Continuous Scoring Process” and “Potential point_Unforced errors”, respectively.

<!-- b000271 | prose | pages [11] -->
For an entire set, the potential points are continuously accumulating, so for this set, the potential point M is as following:

<!-- b000272 | prose | pages [11] -->
n X M = Mi (12) i=1

<!-- b000273 | prose | pages [11] -->
Where, i represents the current game number and n represents the total number of games played in the set.

<!-- b000274 | prose | pages [11] -->
As hypothesized in the paper, there is a break at the end of each set where the coach provides guidance to the athlete, and the athlete also gets a rest. Therefore, at the start of the next set, the athlete’s total momentum points are reset to zero. Moreover, regarding tiebreak games, players alternate serves, and the intensity of competition is much higher, making it difﬁcult to quantify, so it is not included in the model.

<!-- b000275 | heading | pages [11] -->
4.3 Principal Component Analysis (PCA) Dimensionality Reduction

<!-- b000276 | prose | pages [11] -->
In tennis, physical ﬁtness consumption is also an important reference standard. However, the consump- tion of physical ﬁtness cannot be quantitatively characterized into momentum points. Therefore, we extract the running distance for each game of the athletes in the dataset separately to obtain a feature column of the athlete’s running distance per game. This is then incorporated as a reference into the momentum model.

<!-- b000277 | prose | pages [11] -->
Since there are already four feature vectors, and with the introduction of running distance, there are now ﬁve input features in the model. Therefore, we perform Principal Component Analysis (PCA) to reduce the data dimensions, coupling the ﬁve features and extracting the main input features to construct the model.

<!-- b000278 | furniture | pages [11] -->
关注数学模型

<!-- b000279 | furniture | pages [11] -->
2

<!-- b000280 | furniture | pages [11] -->
MATHmodels

<!-- b000281 | furniture | pages [11] -->
获取更多资讯

<!-- b000282 | furniture | pages [12] -->
Team # 2418251

<!-- b000283 | furniture | pages [12] -->
Page 11 of 23

<!-- b000284 | prose | pages [12] -->
Let aij represent each reference data point, and ﬁrst normalize the samples.

<!-- b000285 | prose | pages [12] -->
Pn µj = 1 i=1aij (13) n 微信公众号：数学模型 r Pn 1 i=1 (aij −µi)2 s = (14) n −1

<!-- b000286 | prose | pages [12] -->
Here, µjrepresents the mean of the samples, and s represents the standard deviation of the samples. Subsequently, the correlation coefﬁcient of the samples, that is, the correlation matrix is obtained.

<!-- b000287 | prose | pages [12] -->
Pn ˜ aki × ˜ akj k=1 rij = (15) n −1   · · · r11 r12 r1j   · · · r21 r22 r11 R = (16) ... ... ... ... 微信号：MATHmodels · · · rj1 rj2 rjj

<!-- b000288 | prose | pages [12] -->
Where,rijrepresent the correlation coefﬁcient of each sample, and R represent the correlation matrix. After that, we calculate the eigenvalues λjof the correlation matrix R and extract the corresponding eigen- vectors. Based on the magnitude of the eigenvalues, we select the top k eigenvectors corresponding to the largest eigenvalues as the principal components, where k is the number of principal components we wish to retain. The value of k is determined by the contribution rate and cumulative contribution rate to decide the number of principal components to choose. Our model requires that the cumulative contribution rate of all principal components be greater than 0.85. Through calculation, we reduce the ﬁve input features to three main principal component inputs. The results are shown in ﬁgure9.

<!-- b000289 | caption | pages [12] -->
Table 4: Three principal components derived from the dimensionality reduction of Carlos Alcaraz’s data

<!-- b000290 | prose | pages [12] -->
X1 X2 X3

<!-- b000291 | prose | pages [12] -->
-0.092368448 0.497778724 -0.406497262 -0.429605389 -1.068004031 -0.833292526 0.438065808 0.644409942 -0.670082014 · · · · · · · · · -1.581903617 0.720871564 -0.652117794

<!-- b000292 | caption | pages [12] -->
Table 5: The accumulated contribution rate corresponding to the principal components.

<!-- b000293 | prose | pages [12] -->
X1 X2 X3 Principle Componets

<!-- b000294 | prose | pages [12, 13] -->
Accumulated contribution rate 0.3594 0.6391 0.8680 微信公众号：数学模型

<!-- b000295 | furniture | pages [12] -->
关注数学模型

<!-- b000296 | furniture | pages [12] -->
2

<!-- b000297 | furniture | pages [12] -->
MATHmodels

<!-- b000298 | furniture | pages [12] -->
获取更多资讯

<!-- b000299 | furniture | pages [13] -->
Team # 2418251

<!-- b000300 | furniture | pages [13] -->
Page 12 of 23

<!-- b000302 | caption | pages [13] -->
Figure 9: Heatmap of the input features after PCA processing

<!-- b000303 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000304 | caption | pages [13] -->
Figure9 is a heatmap of the three principal components obtained through principal component analysis

<!-- b000305 | prose | pages [13] -->
(PCA) dimensionality reduction. The three columns represent the three input vectors, and the color intensity represents the magnitude of the input values.

<!-- b000306 | heading | pages [13] -->
4.4 Momentum Model Based on Support Vector Machines (SVM)

<!-- b000307 | prose | pages [13] -->
“Potential points” are a discrete variable with strong linear correlation; therefore, by establishing a machine learning model and inputting principal component features with “potential points” as the reference output feature, we can derive the output momentum of the athlete.

<!-- b000308 | prose | pages [13] -->
Support Vector Machines are a typical machine learning algorithm that uses the hyperplane concept to perform regression modeling, obtaining the momentum value for each game point of an athlete. We deﬁne the three main components as X1,X2 and X3, forming the input feature matrix X = [X1, X2, X3]

<!-- b000309 | prose | pages [13] -->
Based on the SVM regression formula, we can derive the calculation method for the momentum value Mo. Mo = W T X + b (17)

<!-- b000310 | prose | pages [13] -->
Here, Morepresents the output momentum, X represents the input feature matrix. W denotes the normal vector of the hyperplane, and b denotes the bias term of the hyperplane. The parameters of the model are solved by minimizing the objective function, thereby making predictions for the variables.

<!-- b000311 | prose | pages [13] -->
     1 W T X + b 2 ∥W∥2 ≥1 minW,b s.t. Mo (18)

<!-- b000312 | prose | pages [13] -->
The optimization of SVM is achieved by introducing a kernel function to map low-dimensional features to a high-dimensional space. This model uses the Gaussian kernel function for feature mapping.

<!-- b000313 | prose | pages [13, 14] -->
Using MATLAB software, we train a model with the data from the Wimbledon ﬁnal between Carlos Al- caraz and Novak Djokovic (2023-wimbledon-1701). We perform Principal Component Analysis (PCA) on the match data considering “Potential point_Serve”, “Potential point_Serve”, “Potential point_Continuous Scoring Process”, “Potential point_Unforced errors”, and the distance run per game. This analysis yields three principal components and the potential points for each game. These are then inputted into an SVM- based momentum calculation model to obtain the momentum for each game for both players.

<!-- b000314 | furniture | pages [13] -->
关注数学模型

<!-- b000315 | furniture | pages [13] -->
2

<!-- b000316 | furniture | pages [13] -->
MATHmodels

<!-- b000317 | furniture | pages [13] -->
获取更多资讯

<!-- b000318 | furniture | pages [14] -->
Team # 2418251

<!-- b000319 | furniture | pages [14] -->
Page 13 of 23

<!-- b000321 | caption | pages [14] -->
Table 6: Player_1:Carlos Alcaraz’s momentum points and momentum data

<!-- b000322 | prose | pages [14] -->
微信公众号：数学模型 Mb Ms Mc Mu Set_no. Game_no. Distance_run Potential points Momentum

<!-- b000323 | prose | pages [14] -->
1 1 0 0 2 1 138.548 1.5 2.3798 1 2 0 3 0 2 83.235 2 1.1220 1 3 0 0 2 1 224.138 1.5 2.3152 · · · · · · · · · · · · · · · · · · · · · · · · · · · 5 10 0 3 0 1 99.511 2.5 1.5982

<!-- b000324 | caption | pages [14] -->
Table 7: Player_2:Novak Djokovic’s potential points and momentum data

<!-- b000325 | prose | pages [14] -->
Mb Ms Mc Mu Set_no. Game_no. Distance_run Potential points Momentum

<!-- b000326 | prose | pages [14] -->
1 1 0 3 4 1 130.689 6.5 6.9377 1 2 5 0 2 0 95.182 7 6.5994 微信号：MATHmodels 1 3 0 3 2 1 206.149 4.5 4.1993 · · · · · · · · · · · · · · · · · · · · · · · · · · · 5 10 0 0 0 0 143.272 0 0.1831

<!-- b000327 | caption | pages [14] -->
Figure 10 presents the input of three principal components, with the athlete’s potential points as the

<!-- b000328 | prose | pages [14] -->
output feature for prediction. The blue solid line represents the athlete’s potential points in each game, while the red dashed line represents the athlete’s momentum. The model has a mean squared error (MSE) of 0.1735 and an R2 value of 0.90142, indicating a reliable ﬁt accuracy.

<!-- b000329 | caption | pages [14] -->
Figure 10: Momentum model based on SVM training.

<!-- b000330 | prose | pages [14] -->
Subsequently, for the Wimbledon ﬁnal between Carlos Alcaraz and Novak Djokovic (2023-wimbledon- 1701), we accumulated the momentum of each set for both players to obtain the cumulative momentum changes per set. We also visualized the momentum for each point and for each set to describe the momentum shifts during different stages of the match.

<!-- b000331 | furniture | pages [14] -->
关注数学模型

<!-- b000332 | furniture | pages [14] -->
2

<!-- b000333 | furniture | pages [14] -->
MATHmodels

<!-- b000334 | furniture | pages [14] -->
获取更多资讯

<!-- b000335 | furniture | pages [15] -->
Team # 2418251

<!-- b000336 | furniture | pages [15] -->
Page 14 of 23

<!-- b000337 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000338 | caption | pages [15] -->
Figure 11: Comparison of the momentum for

<!-- b000339 | caption | pages [15] -->
Figure 12: Comparison of the accumulated

<!-- b000340 | prose | pages [15] -->
each game between the two players momentum between the two players 微信号：MATHmodels In the ﬁgure11 and 12, the purple line represents player 1, Carlos Alcaraz, showing his momentum and accumulated momentum. The blue line represents Novak Djokovic, indicating his momentum and accumulated momentum. The single-game momentum reveals the alternating lead between the two players, while the accumulated momentum provides a clearer view of each player’s performance and lead in every set. As shown in Figure 12, Player 2 (Novak Djokovic) had strong momentum in the ﬁrst set, but Player 1 (Carlos Alcaraz) overtook him in the second and third sets. In the fourth set, Player 2 regained the lead. The ﬁnal set saw both players repeatedly trading the lead, aligning with the actual course of the ﬁnal match described in the problem.

<!-- b000341 | heading | pages [15] -->
4.5 Statistical Test of Factors Affecting Momentum

<!-- b000342 | prose | pages [15] -->
There are many factors that can inﬂuence momentum during a match, so it is necessary to identify which factors are most closely related to momentum shifts and whether momentum affects a player’s likelihood of winning.

<!-- b000343 | heading | pages [15] -->
4.5.1 The Impact of Momentum on the Probability of Winning a Match

<!-- b000344 | prose | pages [15] -->
Based on Model 1, we have developed a winning probability model for athletes’ serving and receiving. And Table 8 shows the momentum and winning probability of Player 1 and Player 2 from Model.

<!-- b000345 | caption | pages [15] -->
Table 8: The momentum and Winning Probability of Player 1 and Player 2

<!-- b000346 | prose | pages [15] -->
Set_no. Game_no. Momentum_P1 Winning probability_P1 Momentum_P2 Winning probability_P1

<!-- b000347 | prose | pages [15] -->
1 1 2.3798 0.339 6.9377 0.661 1 2 3.5018 0.329 6.5994 0.671 1 3 5.8170 0.284 4.1993 0.716 · · · · · · · · · · · · · · · · · · 5 10 1.5982 0.588 0.1831 0.412

<!-- b000348 | prose | pages [15, 16] -->
We calculated the Spearman’s rank correlation coefﬁcient between Player 1 and their winning percent- age, as well as between Player 2 and their winning percentage, to determine the direct association between winning rate and momentum. This relationship is visualized in a heatmap.

<!-- b000349 | furniture | pages [15] -->
关注数学模型

<!-- b000350 | furniture | pages [15] -->
2

<!-- b000351 | furniture | pages [15] -->
MATHmodels

<!-- b000352 | furniture | pages [15] -->
获取更多资讯

<!-- b000353 | furniture | pages [16] -->
Team # 2418251

<!-- b000354 | furniture | pages [16] -->
Page 15 of 23

<!-- b000356 | prose | pages [16] -->
In the heatmap as follow, the Spearman’s rank correlation coefﬁcient between Player 1’s winning rate 微信公众号：数学模型 and momentum is 0.704, while for Player 2 it is 0.729. Therefore, there is a close relationship between momentum and the players’ winning percentage. Changes in momentum signiﬁcantly affect the athletes’ chances of winning.

<!-- b000357 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000358 | caption | pages [16] -->
Figure 13: The direct correlation between the winning percentage and momentum for Player 1 and Player 2

<!-- b000359 | heading | pages [16] -->
4.5.2 The Impact of other Factors on Momentum

<!-- b000360 | prose | pages [16] -->
During the model-building process, we incorporated ﬁve features: Mb, Ms , Mc, Mu and Distance_run to reference the momentum. Therefore, we calculated the Spearman’s coefﬁcient correlation coefﬁcient for these ﬁve inﬂuencing factors with respect to each of the two players, and the results are shown in the table below:

<!-- b000361 | caption | pages [16] -->
Table 9: Spearman coefﬁcients of momentum with related factors_P1

<!-- b000362 | prose | pages [16] -->
Mb_P1 Ms_P1 Mc_P1 Mu_P1 Spearman’s coefﬁcient Distance_run_P1 Momentum_P2

<!-- b000363 | prose | pages [16] -->
Momentum_P1 0.457 0.49 0.868 0.032 -0.031 -0.654

<!-- b000364 | caption | pages [16] -->
Table 10: Spearman coefﬁcients of momentum with related factors_P2

<!-- b000365 | prose | pages [16] -->
Mb_P2 Ms_P2 Mc_P2 Mu_P2 Spearman’s coefﬁcient Distance_run_P2 Momentum_P1

<!-- b000366 | prose | pages [16] -->
Momentum_P2 0.436 0.435 0.871 -0.235 0.102 -0.654

<!-- b000367 | heading | pages [16] -->
5 Predictive Model for Shifts in Momentum

<!-- b000368 | prose | pages [16] -->
From the modeling process above, we know that momentum has a certain impact on the transforma- tion of the game’s ﬂow. Therefore, this section will establish a predictive model to forecast the shifts in momentum during the match.

<!-- b000369 | furniture | pages [16] -->
关注数学模型

<!-- b000370 | furniture | pages [16] -->
2

<!-- b000371 | furniture | pages [16] -->
MATHmodels

<!-- b000372 | furniture | pages [16] -->
获取更多资讯

<!-- b000373 | furniture | pages [17] -->
Team # 2418251

<!-- b000374 | furniture | pages [17] -->
Page 16 of 23

<!-- b000375 | heading | pages [17] -->
5.1 Accumulated Momentum Prediction Model Based on ARIMA

<!-- b000376 | prose | pages [17] -->
The cumulative momentum of athletes has a certain time series and cyclical volatility. We choose the ARIMA algorithm to construct the predictive model. ARIMA (Autoregressive Integrated Moving Average) 微信公众号：数学模型 is a statistical model used for time series analysis. Its principle is based on the autocorrelation of time series and the moving average properties, and then it obtains the trend of the time series by differencing the data and ﬁtting the model.It is divided into: the Autoregressive part (AR), the Integrated part (I), and the Moving Average part (MA).

<!-- b000377 | prose | pages [17] -->
ARIMA(p,d,q) model is as following:

<!-- b000378 | prose | pages [17] -->
p q X X m′ t = α0 + αimi + εt + βiεt−i (19) i=1 i=1

<!-- b000379 | prose | pages [17] -->
In the ARIMA(p,d,q) model, α0 is the initial constant term. αi represents the autoregressive coefﬁ- cients, indicating the impact of the past p observations on the current value. βi denotes the moving average coefﬁcients, showing the effect of the past q errors on the current value. ε is the error term. mi stands for 微信号：MATHmodels the accumulated momentum at previous moments, and m′ t is the predicted accumulated momentum for the next moment. p signiﬁes the order of the autoregressive part, q signiﬁes the order of the moving average, and d signiﬁes the order of differencing.

<!-- b000380 | prose | pages [17] -->
We use MATLAB to implement the aforementioned operations to perform data prediction for the accumulated momentum of Carlos Alcaraz and Novak Djokovic in their Wimbledon ﬁnal match (2023- wimbledon-1701).

<!-- b000381 | prose | pages [17] -->
Given the signiﬁcant ﬂuctuation trends in momentum for both players, we choose to use a 4th order autoregressive, 4th order moving average, and 1st order difference to construct an ARIMA model, that is, p=4, d=1, q=4, to obtain detrended data and apply it in the model.

<!-- b000382 | prose | pages [17] -->
By inputting the accumulated momentum of Carlos Alcaraz and Novak Djokovic from their previous ﬁve sets into the model, we predict the accmulated momentum values if they were to continue playing for another ten games. The result is shown in ﬁgure14.

<!-- b000383 | caption | pages [17] -->
Table 11: Accumulated momentum predicted for the next ten games

<!-- b000384 | prose | pages [17] -->
Accumulated momentum predicted Carlos Alcaraz Novak Djokovic for the next ten games

<!-- b000385 | prose | pages [17, 18] -->
1 27.0156 26.4919 2 23.6921 27.5516 3 27.2556 20.7143 4 27.1483 13.0571 5 32.2795 12.0164 6 33.1069 16.7490 7 36.1148 20.6293 8 35.4353 21.1249 9 34.3283 20.1466 10 34.3283 19.3927 And, the corresponding visualization is showed below:

<!-- b000386 | furniture | pages [17] -->
关注数学模型

<!-- b000387 | furniture | pages [17] -->
2

<!-- b000388 | furniture | pages [17] -->
MATHmodels

<!-- b000389 | furniture | pages [17] -->
获取更多资讯

<!-- b000390 | furniture | pages [18] -->
Team # 2418251

<!-- b000391 | furniture | pages [18] -->
Page 17 of 23

<!-- b000393 | prose | pages [18] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000394 | caption | pages [18] -->
Figure 14: A accumulated momentum prediction chart for two players.

<!-- b000395 | prose | pages [18] -->
In the ﬁgure14, the dark purple and dark green lines represent the cumulative momentum trends of player 1 and 2 (Carlos Alcaraz and Novak Djokovic) for the ﬁrst ﬁve sets, respectively. The light purple and light green represent the predicted momentum values for the next ten games for both players. In future matches, it is possible that Carlos Alcaraz may continue to lead with a signiﬁcant advantage over Novak Djokovic.

<!-- b000396 | heading | pages [18] -->
5.2 Advice Based on Shifts in Momentum

<!-- b000397 | prose | pages [18] -->
Based on the modeling and analysis results, we offer the following three pieces of advice as follows:

<!-- b000398 | prose | pages [18] -->
• Capitalize on your service games. By quickly establishing dominance at the start of a service game, you can exert greater pressure on your opponent, thus gaining better control of the match’s rhythm and achieving a higher cumulative momentum. Players should practice this aspect during training to improve the quality of their serve.

<!-- b000399 | prose | pages [18] -->
• Capitalize on break points. Break points are a critical juncture and a key moment for momentum shifts. Players can disrupt their opponent’s rhythm by altering their own service return pace during the opponent’s service games, making it difﬁcult for the opponent to adapt. Seize opportunities: Once a chance arises, decisively exploit your strengths to attempt a break in the opponent’s service game.

<!-- b000400 | prose | pages [18] -->
• Continuous scoring. Moments of consecutive scoring often lead to signiﬁcant momentum shifts.

<!-- b000401 | prose | pages [18] -->
Therefore, it’s essential to capitalize on your streaks, maintain an aggressive offensive stance, strive to seize the initiative, target your opponent’s weaknesses, and be bold in attempting risky shots to push through and win the match. When your opponent is on a scoring streak, look for opportunities to break the deadlock or seek a timeout for adjustments.

<!-- b000402 | furniture | pages [18] -->
关注数学模型

<!-- b000403 | furniture | pages [18] -->
2

<!-- b000404 | furniture | pages [18] -->
MATHmodels

<!-- b000405 | furniture | pages [18] -->
获取更多资讯

<!-- b000406 | furniture | pages [19] -->
Team # 2418251

<!-- b000407 | furniture | pages [19] -->
Page 18 of 23

<!-- b000408 | heading | pages [19] -->
6 Veriﬁcation and Application of the Model

<!-- b000409 | heading | pages [19] -->
6.1 Veriﬁcation within the Same Type of Competition

<!-- b000410 | prose | pages [19] -->
微信公众号：数学模型 To verify the accuracy of the momentum model, we selected another match featuring different players, Daniil Medvedev and Christopher Eubanks, from the 2023 Wimbledon tournament (match code: 1502). Player 1 is Daniil Medvedev, and Player 2 is Christopher Eubanks. We trained the model using their match data, which included break points, serve points, continuous scoring points, unforced error points, and dis- tance run per game. We performed principal component analysis and momentum point calculation to obtain four principal components and the potential points for each game. These were then input into the SVM momentum calculation model to determine the momentum and accumulated momentum for each player in every game.

<!-- b000411 | caption | pages [19] -->
Table 12: Daniil Medvedev’s momentum data

<!-- b000412 | prose | pages [19] -->
Set_no. Gmae_no. M_b M_s M_c M_u DR

<!-- b000413 | heading | pages [19] -->
M Mo

<!-- b000414 | prose | pages [19] -->
A-Mo 微信号：MATHmodels 1 1 0 0 0 0 92.263 0 -0.143 -0.183 2 2 0 3 2 0 18.837 5 4.667 4.484 3 3 5 0 2 0 92.433 7 6.661 11.145 · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 5 7 5 0 2 0 47.094 6.5 6.371 34.379

<!-- b000415 | caption | pages [19] -->
Table 13: Christopher Eubanks’s momentum data

<!-- b000416 | prose | pages [19] -->
Set_no. Gmae_no. M_b M_s M_c M_u DR

<!-- b000417 | heading | pages [19] -->
M Mo

<!-- b000418 | prose | pages [19] -->
A-Mo

<!-- b000419 | prose | pages [19] -->
1 1 0 3 2 0 93.806 5 4.583 4.583 2 2 0 0 0 0 18.671 0 -0.100 4.483 3 3 0 3 0 4 96.703 1 0.724 5.207 · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 5 7 5 0 3 4 80.886 3 3.362 18.404

<!-- b000420 | prose | pages [19] -->
*Note: Set_no. represents the set number; Game_no. represents the game number; M_b , M_s , M_c and M_u,represent potential points related to break points, service points, continuous scoring points,unforced errors, respectively; DR represents distance run; M represents total potential points; Mo represents momen- tum; A-Mo represents accumulated momentum.

<!-- b000421 | prose | pages [19] -->
We visualized the momentum and accumulated momentum for both players, which are showed in ﬁg- ure15 and 16.

<!-- b000422 | furniture | pages [19] -->
关注数学模型

<!-- b000423 | furniture | pages [19] -->
2

<!-- b000424 | furniture | pages [19] -->
MATHmodels

<!-- b000425 | furniture | pages [19] -->
获取更多资讯

<!-- b000426 | furniture | pages [20] -->
Team # 2418251

<!-- b000427 | furniture | pages [20] -->
Page 19 of 23

<!-- b000428 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000429 | caption | pages [20] -->
Figure 15: Comparison of the momentum for

<!-- b000430 | caption | pages [20] -->
Figure 16: Comparison of the accumulated

<!-- b000431 | prose | pages [20] -->
each game between the two players momentum between the two players 微信号：MATHmodels In the ﬁgure15 and 16, the purple line represents Player 1, Daniil Medvedev’s momentum and accum- lated momentum. The green line represents Christopher Eubanks’s momentum and accumulated momen- tum. The single game momentum shows the alternating lead in momentum between the two players, while the accumulated momentum provides a clearer view of each player’s performance and lead throughout each set. As shown in Figure 16, Player 1 (Daniil Medvedev) had strong momentum in the ﬁrst set, but Player 2 (Christopher Eubanks) overtook him in the second and third sets. In the fourth and ﬁfth sets, Player 2’s mo- mentum surpassed Player 1’s again, aligning with the actual course of the match. Therefore, our momentum model demonstrates a certain level of generality across other tennis matches.

<!-- b000432 | heading | pages [20] -->
6.2 Application to other Types of Competitions

<!-- b000433 | prose | pages [20] -->
For other types of competitions, continuous scoring often occurs in ball sports and is highly correlated with momentum, making it a valuable input feature for reference. In other ball sports, the advantage gap between serving and receiving is not signiﬁcant; hence, serve reception and breaks will not impact momen- tum as much. Additionally, a player’s psychological state, physical ﬁtness, and court environment can all affect their momentum, and these factors should also be considered. Therefore, the computational principles of our model are universally applicable across many types of competitions, but the indicators included in the calculations should be adjusted according to the type of sport. In summary, the model’s computational principles have a certain applicability in various competitions.

<!-- b000434 | heading | pages [20] -->
7 Sensitivity Analysis

<!-- b000435 | prose | pages [20] -->
We conduct a sensitivity analysis on the momentum model to verify the sensitivity of its various input parameters.

<!-- b000436 | prose | pages [20, 21] -->
Firstly, we adjust the weights of the momentum point model and recalculate the new momentum based on principal components, comparing it with the originally calculated momentum. We use the ﬁnal match of Carlos Alcaraz and Novak Djokovic at Wimbledon 2023 (2023-wimbledon-1701) as reference data, with Carlos Alcaraz as Player 1 and Novak Djokovic as Player 2. Subsequently, we increase the weights of break-of-serve potential points, serving potential points, continuous scoring momentum points, and error momentum points by 50% in the momentum point calculation model, re-enter them into the SVM model to obtain four corresponding momentum sets, and compare these with the momentum calculated from the previous question. The results are shown in the ﬁgure below.

<!-- b000437 | furniture | pages [20] -->
关注数学模型

<!-- b000438 | furniture | pages [20] -->
2

<!-- b000439 | furniture | pages [20] -->
MATHmodels

<!-- b000440 | furniture | pages [20] -->
获取更多资讯

<!-- b000441 | furniture | pages [21] -->
Team # 2418251

<!-- b000442 | furniture | pages [21] -->
Page 20 of 23

<!-- b000444 | prose | pages [21] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000445 | caption | pages [21] -->
Figure 17: Player 1 Momentum sensitivity

<!-- b000446 | caption | pages [21] -->
Figure 18: Player 2 Momentum sensitivity

<!-- b000447 | prose | pages [21] -->
analysis analysis

<!-- b000448 | prose | pages [21] -->
As shown in the ﬁgure17 and 18, the red line represents the momentum of Player 1 and Player 2 as cal- culated by the previous model, while the other colors represent the momentum recalculated after perturbing one weight. The results indicate that our model is sensitive.

<!-- b000449 | heading | pages [21] -->
8 Strengths and Weaknesses

<!-- b000450 | heading | pages [21] -->
8.1 Strengths

<!-- b000451 | prose | pages [21] -->
1) Introduce multiple features such as serving, breaking serve, continuous scoring, errors, and distance run to characterize momentum points, momentum, and cumulative momentum in stages. This provides a more comprehensive and speciﬁc portrayal of the athlete’s performance during the match.

<!-- b000452 | prose | pages [21] -->
2) The modeling process employs machine learning algorithms and the ARIMA algorithm, supplemented by statistical parameter validation, making the results scientiﬁcally credible.

<!-- b000453 | prose | pages [21] -->
3) This model can comprehensively depict the changes in an athlete’s momentum during a match, providing coaches with a scientiﬁc research benchmark.

<!-- b000454 | heading | pages [21] -->
8.2 Weaknesses

<!-- b000455 | prose | pages [21] -->
1) This model does not consider the impact of non-statistical factors such as the athletes’ psychological states and the environmental conditions of the competition venue on momentum. In actual matches, an athlete’s psychological state and the condition of the playing environment can have a certain effect on their performance.

<!-- b000456 | prose | pages [21] -->
2) The parameters considered by this model are mostly characteristic of tennis; when applying it to other types of sports, corresponding features of the sport in question should be reselected.

<!-- b000457 | furniture | pages [21] -->
关注数学模型

<!-- b000458 | furniture | pages [21] -->
2

<!-- b000459 | furniture | pages [21] -->
MATHmodels

<!-- b000460 | furniture | pages [21] -->
获取更多资讯

<!-- b000461 | furniture | pages [22] -->
Team # 2418251

<!-- b000462 | furniture | pages [22] -->
Page 21 of 23

<!-- b000463 | heading | pages [22] -->
Memorandum

<!-- b000464 | prose | pages [22] -->
To: Coach A

<!-- b000465 | prose | pages [22] -->
From: Team 2418251 微信公众号：数学模型 Subject: Tennis Strategy Recommendations Based on Momentum

<!-- b000466 | prose | pages [22] -->
Date: Monday, February 5, 2024

<!-- b000467 | prose | pages [22] -->
Based on our team’s modeling and analysis, we have summarized a report for you. This may aid in your guidance and training of tennis players. Our report will unfold in three parts.

<!-- b000468 | prose | pages [22] -->
Firstly, the summary of results:Our team established a Momentum Machine Learning model (MML) using characteristics such as serving, break points, consecutive scoring, unforced errors, and distance run, to quantitatively calculate the momentum of tennis players for each game, and processed this to determine the cumulative momentum of the player for the set.We created an 微信号：MATHmodels ARIMA predictive model and analyzed the time series trends of the player’s cumulative momentum during the match, thereby predicting the player’s momentum for the upcoming games. Additionally, through statistical testing, we concluded that there is a strong correlation between a tennis player’s momentum and their winning rate.

<!-- b000469 | prose | pages [22] -->
Secondly, based on our evaluation, we give our recommendations:

<!-- b000470 | prose | pages [22] -->
• Utilize the momentum from serving by observing the opponent’s receiving abilities and weak- nesses, guiding players to adjust their serving strategies, and encouraging more risk-taking in serving when players score consecutively.

<!-- b000471 | prose | pages [22] -->
• Utilize momentum from the break point perspective by training players to recognize and exploit weak service games with aggressive returns, maintaining focus for better chances at breaking serve.

<!-- b000472 | prose | pages [22] -->
• Maintain momentum from consecutive scoring by encouraging an attacking style while re- minding players to avoid overconfidence, ensuring a stable performance.

<!-- b000473 | prose | pages [22] -->
• Utilize momentum from errors by helping players stay calm, learn from mistakes, and adjust tactics to regain match rhythm.

<!-- b000474 | prose | pages [22] -->
• Utilize running distance to maintain momentum by optimizing movement, saving energy, and exploiting the opponent’s stamina through tactical adjustments.

<!-- b000475 | prose | pages [22] -->
Thirdly, the training strategies: In tennis matches, to enhance a player’s momentum, coaches should have players strengthen their serve training, focusing on variations in speed, placement, and spin while preparing multiple serving strategies to adjust according to the opponent; improve the quality of returns, forcing opponents to make errors and creating break opportunities; cultivate quick decision-making skills, knowing how to exploit the opponent’s weaknesses and continuously pressuring to gain opportunities for consecutive scoring; maintain a positive attitude in the face of errors, not letting mistakes affect confidence; and enhance physical training to improve players’ movement speed and endurance.

<!-- b000476 | furniture | pages [22] -->
关注数学模型

<!-- b000477 | furniture | pages [22] -->
1

<!-- b000478 | furniture | pages [22] -->
2

<!-- b000479 | furniture | pages [22] -->
MATHmodels

<!-- b000480 | furniture | pages [22] -->
获取更多资讯

<!-- b000481 | furniture | pages [23] -->
Team # 2418251

<!-- b000482 | furniture | pages [23] -->
Page 22 of 23

<!-- b000483 | heading | pages [23] -->
References

<!-- b000484 | references | pages [23] -->
[1] https://www.news9live.com/sports/tennis/novak-djokovic-vs-carlos-alcaraz-wimbledon-2023-mens-

<!-- b000485 | references | pages [23] -->
ﬁnal-records-and-milestones-to-watch-out-for-2214729

<!-- b000486 | references | pages [23] -->
微信公众号：数学模型

<!-- b000487 | references | pages [23] -->
[2] Braidwood, J. (2023), Novak Djokovic has created a unique rival is Wimbledon defeat the beginning

<!-- b000488 | references | pages [23] -->
of the end, The Independent,https://www.independent.co.uk/sport/tennis/novak-djokovic-wimbledon-

<!-- b000489 | references | pages [23] -->
ﬁnal-carlos-alcaraz b2376600.html.

<!-- b000490 | references | pages [23] -->
[3] https://www.merriam-webster.com/dictionary/momentum

<!-- b000491 | references | pages [23] -->
[4] Rivera, J. (2023), Tennis scoring, explained: A guide to understanding the rules terms & point sys-

<!-- b000492 | references | pages [23] -->
tem at Wimbledon, The Sporting News,https://www.sportingnews.com/us/tennis/news/tennis-scoring-

<!-- b000493 | references | pages [23] -->
explained-rules-system-points terms/7uzp2evdhbd11obdd59p3p1cx.

<!-- b000494 | references | pages [23] -->
[5] Chen T, Fan Q, Liu K, Le L. Identifying key factors in momentum in basketball games. J Appl Stat.

<!-- b000495 | references | pages [23] -->
2020 Jul 21;48(16):3116-3129. doi: 10.1080/02664763.2020.1795819. PMID: 35707253; PMCID:

<!-- b000496 | references | pages [23] -->
PMC9041568.

<!-- b000497 | references | pages [23] -->
微信号：MATHmodels

<!-- b000498 | references | pages [23] -->
[6] Weimer, Louis, Steinert-Threlkeld, Zachary C., and Coltin, Kevin. ‘A Causal Approach for Detecting

<!-- b000499 | references | pages [23] -->
Team-level Momentum in NBA Games’. 1 Jan. 2023 : 117 132

<!-- b000500 | references | pages [23] -->
[7] Ruud J.R. den Hartigh, Paul L.C van Geert, Nico W. van Yperen, Ralf F.A Cox, Christophe Gernigon.

<!-- b000501 | references | pages [23] -->
Psychological momentum during and across sports matches: Evidence for interconnected time scales..

<!-- b000502 | references | pages [23] -->
Journal of Sport and Exercise Psychology, 2016, 38 (1), pp.82-92. ff10.1123/jsep.2015-0162ff.

<!-- b000503 | references | pages [23] -->
ffhal02519559

<!-- b000504 | furniture | pages [23] -->
关注数学模型

<!-- b000505 | furniture | pages [23] -->
2

<!-- b000506 | furniture | pages [23] -->
MATHmodels

<!-- b000507 | furniture | pages [23] -->
获取更多资讯

<!-- b000508 | furniture | pages [24] -->
Team # 2418251

<!-- b000509 | references | pages [24] -->
Page 23

<!-- b000510 | heading | pages [24] -->
Appendices

<!-- b000511 | heading | pages [24] -->
Report on Use of AI

<!-- b000512 | ai_disclosure | pages [24] -->
微信公众号：数学模型

<!-- b000513 | ai_disclosure | pages [24] -->
1. Bing AI

<!-- b000514 | ai_disclosure | pages [24] -->
Query1:How to adjust a player’s serve during a tennis match?

<!-- b000515 | ai_disclosure | pages [24] -->
Output:Adjusting a player’s serve during a tennis match can be crucial for improving performance or

<!-- b000516 | ai_disclosure | pages [24] -->
responding to an opponent’s strengths or weaknesses. Here are some general tips for adjusting a player’s

<!-- b000517 | ai_disclosure | pages [24] -->
serve during a match:

<!-- b000518 | ai_disclosure | pages [24] -->
1 Analyze the Opponent: Watch the opponent’s return patterns and tendencies to identify any weak-

<!-- b000519 | ai_disclosure | pages [24] -->
nesses or areas of vulnerability. If the opponent is struggling with a particular type of serve (e.g.,

<!-- b000520 | ai_disclosure | pages [24] -->
wide, body, or T serve), focus on exploiting that weakness.

<!-- b000521 | ai_disclosure | pages [24] -->
2 Change Placement: If the opponent is consistently returning serves well from a certain area of the

<!-- b000522 | ai_disclosure | pages [24] -->
court, consider changing the placement of the serve to exploit other areas. For example, if the oppo-

<!-- b000523 | ai_disclosure | pages [24] -->
nent is consistently attacking your wide serves, try targeting the body or T.

<!-- b000524 | ai_disclosure | pages [24] -->
微信号：MATHmodels

<!-- b000525 | ai_disclosure | pages [24] -->
3 Adjust Speed and Spin: Vary the speed and spin of the serve to keep the opponent off balance. Mix

<!-- b000526 | ai_disclosure | pages [24] -->
up the pace of the serve between fast, medium, and slow serves, as well as adding topspin or slice to

<!-- b000527 | ai_disclosure | pages [24] -->
create variation.

<!-- b000528 | ai_disclosure | pages [24] -->
4 Use Deception: Incorporate deception into your serve by occasionally using a different ball toss or

<!-- b000529 | ai_disclosure | pages [24] -->
motion to keep the opponent guessing. For example, disguising a kick serve as a ﬂat serve or using a

<!-- b000530 | ai_disclosure | pages [24] -->
subtle change in ball toss can catch the opponent off guard.

<!-- b000531 | ai_disclosure | pages [24] -->
Remember that every match is unique, so the speciﬁc adjustments will depend on the opponent’s playing

<!-- b000532 | ai_disclosure | pages [24] -->
style, court conditions, and your own strengths and weaknesses. Constant awareness and adaptability are

<!-- b000533 | ai_disclosure | pages [24] -->
key to making effective adjustments to a player’s serve during a tennis match.

<!-- b000534 | ai_disclosure | pages [24] -->
2. Bing AI

<!-- b000535 | ai_disclosure | pages [24] -->
Query1: How to minimize unforced errors in tennis?

<!-- b000536 | ai_disclosure | pages [24] -->
Output:

<!-- b000537 | ai_disclosure | pages [24] -->
1 Practice regularly: The more you practice, the better you will become at playing tennis. This will help

<!-- b000538 | ai_disclosure | pages [24] -->
you to develop muscle memory and reduce the number of unforced errors you make.

<!-- b000539 | ai_disclosure | pages [24] -->
2 Focus on your footwork: Good footwork is essential in tennis. It helps you to get into the right position

<!-- b000540 | ai_disclosure | pages [24] -->
to hit the ball and reduces the chance of making an unforced error.

<!-- b000541 | ai_disclosure | pages [24] -->
3 Keep your eye on the ball: Always keep your eye on the ball when you are hitting it. This will help

<!-- b000542 | ai_disclosure | pages [24] -->
you to make better contact and reduce the number of unforced errors.

<!-- b000543 | ai_disclosure | pages [24] -->
4 Use the correct technique: Make sure you use the correct technique when hitting the ball. This will

<!-- b000544 | ai_disclosure | pages [24] -->
help you to generate more power and control, reducing the chance of making an unforced error.

<!-- b000545 | ai_disclosure | pages [24] -->
5 Stay relaxed: Tennis can be a stressful game, but it’s important to stay relaxed. If you tense up, you

<!-- b000546 | ai_disclosure | pages [24] -->
are more likely to make an unforced error.

<!-- b000547 | furniture | pages [24] -->
关注数学模型

<!-- b000548 | furniture | pages [24] -->
2

<!-- b000549 | furniture | pages [24] -->
MATHmodels

<!-- b000550 | furniture | pages [24] -->
获取更多资讯
