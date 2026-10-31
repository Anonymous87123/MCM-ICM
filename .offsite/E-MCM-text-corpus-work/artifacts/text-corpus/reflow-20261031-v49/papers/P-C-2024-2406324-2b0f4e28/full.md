# P-C-2024-2406324-2b0f4e28

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

<!-- b000006 | furniture | pages [1] -->
2406324

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Command the Flow: Analysis and Prediction of

<!-- b000009 | title | pages [1] -->
Momentum in Tennis Matches

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
This study addresses the complex phenomenon of momentum in tennis by analyzing data from Wimbledon 2023 men’s matches. By using the Exponential Weighted Moving Average (EWMA), an evaluation model is constructed to quantitatively define momentum and swings during the matches. The combined result of the run test and context study proves momentum is not random. Based on the numerical curves of momentum, we build a prediction model that combines the low error rate of Long Short-Term Memory (LSTM) networks and factor contribution analysis of Extreme Gradient Boosting (XGBoost). Clustered transfer learning is introduced with K-means clustering to improve the prediction model in accuracy. SHapley Additive exPlanations (SHAP) is applied to find out which

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
factors are most related to the swings in tennis matches. In sensitive analysis, we verified our choice of step size and cluster number, pointing out possible directions for future work. We have also collected data from Women’s matches (2023 WTA US Open). The prediction error becomes significantly larger, for which we have explained generally. With all the conclusions drawn, we write a memo for tennis coaches at the end of this paper.

<!-- b000015 | keywords | pages [1] -->
Keywords: Momentum

<!-- b000016 | prose | pages [1] -->
EWMA LSTM K-means SHAP

<!-- b000017 | furniture | pages [1] -->
关注数学模型

<!-- b000018 | furniture | pages [1] -->
2

<!-- b000019 | furniture | pages [1] -->
MATHmodels

<!-- b000020 | furniture | pages [1] -->
获取更多资讯

<!-- b000021 | furniture | pages [2] -->
Team 2406324

<!-- b000022 | furniture | pages [2] -->
Page 1 of 25

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
1 Introduction

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000027 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
2.1

<!-- b000030 | contents | pages [2] -->
Assumptions

<!-- b000031 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
3

<!-- b000033 | contents | pages [2] -->
2.2

<!-- b000034 | contents | pages [2] -->
Notations

<!-- b000035 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
3

<!-- b000037 | contents | pages [2] -->
3 Data Processing

<!-- b000038 | contents | pages [2] -->
4

<!-- b000039 | contents | pages [2] -->
3.1

<!-- b000040 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
3.2

<!-- b000043 | contents | pages [2] -->
Data Compression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
4

<!-- b000045 | contents | pages [2] -->
3.3

<!-- b000046 | contents | pages [2] -->
Data Overview

<!-- b000047 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
5

<!-- b000049 | contents | pages [2] -->
4 Evaluation: Momentum and Swings

<!-- b000050 | contents | pages [2] -->
6

<!-- b000051 | contents | pages [2] -->
4.1

<!-- b000052 | contents | pages [2] -->
Definition of Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
6

<!-- b000054 | contents | pages [2] -->
4.2

<!-- b000055 | contents | pages [2] -->
Model Visualization and Validation

<!-- b000056 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
8

<!-- b000058 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000059 | contents | pages [2] -->
4.3

<!-- b000060 | contents | pages [2] -->
Randomness & Certainty of Swings . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
10

<!-- b000062 | contents | pages [2] -->
5 Prediction: Time Series Forcasting

<!-- b000063 | contents | pages [2] -->
11

<!-- b000064 | contents | pages [2] -->
5.1

<!-- b000065 | contents | pages [2] -->
Model Selection: RNN, GRU, & LSTM . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
11

<!-- b000067 | contents | pages [2] -->
5.2

<!-- b000068 | contents | pages [2] -->
Transfer Learning: PCA & K-means . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
13

<!-- b000070 | contents | pages [2] -->
5.3

<!-- b000071 | contents | pages [2] -->
Related Factors: XGBoost & SHAP . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
15

<!-- b000073 | contents | pages [2] -->
6 Sensitivity Analysis

<!-- b000074 | contents | pages [2] -->
17

<!-- b000075 | contents | pages [2] -->
6.1

<!-- b000076 | contents | pages [2] -->
Step Size in the LSTM Model

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
17

<!-- b000079 | contents | pages [2] -->
6.2

<!-- b000080 | contents | pages [2] -->
The Number of Clusters in K-means . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
18

<!-- b000082 | contents | pages [2] -->
7 Conclusion

<!-- b000083 | contents | pages [2] -->
19

<!-- b000084 | contents | pages [2] -->
7.1

<!-- b000085 | contents | pages [2] -->
Strength and Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
19

<!-- b000087 | contents | pages [2] -->
7.2

<!-- b000088 | contents | pages [2] -->
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [2] -->
19

<!-- b000090 | contents | pages [2] -->
8 Memorandum

<!-- b000091 | contents | pages [2] -->
20

<!-- b000092 | contents | pages [2] -->
9 Appendices

<!-- b000093 | contents | pages [2] -->
23

<!-- b000094 | contents | pages [2] -->
10 Report on Use of AI

<!-- b000095 | contents | pages [2] -->
25

<!-- b000096 | furniture | pages [2] -->
关注数学模型

<!-- b000097 | furniture | pages [2] -->
2

<!-- b000098 | furniture | pages [2] -->
MATHmodels

<!-- b000099 | furniture | pages [2] -->
获取更多资讯

<!-- b000100 | furniture | pages [3] -->
Team 2406324

<!-- b000101 | furniture | pages [3] -->
Page 2 of 25

<!-- b000102 | heading | pages [3] -->
1 Introduction

<!-- b000103 | prose | pages [3] -->
In many sports competitions, it might often occur that the stronger player or team loses the game. At any given time in a match, the score does not always reflect the true strength of the players, or even 微信公众号：数学模型 the state of the game (Higham, 2000). We can sometimes feel a kind of hidden force that controls the flow of the match, which is defined as the momentum of the game (Higham, 2000). It affects the outcome of the contest and adds to the overall unpredictablity. If the players and their coach can understand and predict the momentum of the game, they can adjust their strategy to take advantage of it and increase their chance of winning the game.

<!-- b000104 | prose | pages [3] -->
The appearence of momentum is especially obvious in tennis matches, since the game is divided into many periods and the situation on the field is constantly changing. In previous studies, a great deal of data was counted to statistically prove the existence of momentum in tennis matches (Moss & Donoghue, 2017). Most researchers have reached an agreement that success does breed success, which means that a series of consecutive winning points is likely to set up a good starting position for the next ball (Meier, Flepp, Ruedisser, & Franck, 2020). However, there are also arguments that falling 微信号：MATHmodels behind temporarily will push the players’ nerves and help them try harder to catch up (Fu, Ke, & Tan, 2015). Despite different opinions, they all agree that the momentum does exist and is often affected by interruptions such as rest periods and important events such as break points converted (Meier, Flepp, Ruedisser, & Franck, 2020).

<!-- b000105 | prose | pages [3] -->
In this paper, we have learned and concluded from previous studies the basic properties of mo- mentum in tennis. We cleaned and processed the data from Wimbledon 2023 men’s matches after the first 2 rounds as the basis of our research (COMAP, 2024). A model is then proposed to quantify the momentum of a game and predict the final outcome (Albert & Koning, 2007). We will show that the swings in a game are not random, and that good indicators could be found for them. We will also extend our model to Women’s Tennis, and discuss how generalizable our model is. The flowchart shown below summarizes the main work and results of our paper.

<!-- b000106 | caption | pages [3] -->
Figure 1: Train of thoughts when reviewing literatures

<!-- b000107 | furniture | pages [3] -->
关注数学模型

<!-- b000108 | furniture | pages [3] -->
2

<!-- b000109 | furniture | pages [3] -->
MATHmodels

<!-- b000110 | furniture | pages [3] -->
获取更多资讯

<!-- b000111 | furniture | pages [4] -->
Team 2406324

<!-- b000112 | furniture | pages [4] -->
Page 3 of 25

<!-- b000113 | heading | pages [4] -->
2 Assumptions and Notations

<!-- b000114 | heading | pages [4] -->
2.1 Assumptions

<!-- b000115 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000116 | prose | pages [4] -->
• Only regular breaks The match is assumed not to be suspended due to any sudden events like weather changes (rain, snow, lawn conditions) or player injuries. The duration of the changeover interruptions between games and sets should strictly follow the official states in the International Tennis Federation’s (ITF’s) rule book.

<!-- b000117 | prose | pages [4] -->
• Full commitment Both athletes were fully committed to the match, without any abnormal situations like match-fixing or abandonment due to disparity in strength. Previous head-to-head records between the two players that could have affected their confidence are not considered.

<!-- b000118 | prose | pages [4] -->
• No extra disturbence 微信号：MATHmodels There are no disturbing incidents before or during the match that could have affected the players’ mentality, including family emergencies, public opinion influences, etc. In this sense, the mental fluctuations of both the two players can be attributed solely to limited factors such as scoring, running, and physical condition on the field.

<!-- b000119 | prose | pages [4] -->
• No physical exertion All players experienced the same number of matches in earlier rounds and were in good and consistent physical condition before this match. The physical exertion of the players due to different situations encountered in the previous rounds was negligible.

<!-- b000120 | heading | pages [4] -->
2.2 Notations

<!-- b000121 | prose | pages [4] -->
Symbol Definition

<!-- b000122 | prose | pages [4] -->
M(x) Momentum at point x P(x) Momentum based on points G(x) Momentum based on games ri Scoring rates in one game gi Game scores pi Point scores wi Weights for game scores ωi Weights for point scores P1/2(x) Player 1 or 2’s predicted momentum R1/2(x) Player 1 or 2’s real momentum L Loss function N Maximum point number in a match

<!-- b000123 | furniture | pages [4] -->
关注数学模型

<!-- b000124 | furniture | pages [4] -->
2

<!-- b000125 | furniture | pages [4] -->
MATHmodels

<!-- b000126 | furniture | pages [4] -->
获取更多资讯

<!-- b000127 | furniture | pages [5] -->
Team 2406324

<!-- b000128 | furniture | pages [5] -->
Page 4 of 25

<!-- b000129 | heading | pages [5] -->
3 Data Processing

<!-- b000130 | heading | pages [5] -->
3.1 Data Cleaning

<!-- b000131 | prose | pages [5] -->
微信公众号：数学模型 We based our study on the data from all Wimbledon 2023 men’s matches after the first 2 rounds (COMAP, 2024). In the table, we found some missing values and outliers. For example, in the ”speed mph” column on row 408, there is a missing value. Considering that a player’s serve speed tends to be continuous within a game, we used Lagrangian interpolation to fill in the missing values. It is worth mentioning that we chose the data points within the same game as the missing value as the given data points. This avoids overfitting and ensures the credibility of the missing value replacement. Taking the serve speed in row 408 as an example, the replaced value is 115mph. Due to limited space, the specific calculation process is not shown here.

<!-- b000132 | heading | pages [5] -->
3.2 Data Compression

<!-- b000133 | prose | pages [5] -->
The massive redundant tabular data volume does not necessarily benefit our subsequent prediction 微信号：MATHmodels model. Therefore, we hope to use the principal component analysis (PCA) method to reduce the dimensionality of the data. Before this, we first utilized the Spearman correlation analysis to find the correlations between different data categories. For example, the ”distance ran during points” of two players in a match has a strong correlation. Therefore, ”p1 distance run” and ”p2 distance run” can be compressed into one dimension. As shown in Figure 2 below, we can determine the objects for PCA compression through the Spearman correlation analysis.

<!-- b000134 | caption | pages [5] -->
Figure 2: A 10 × 10 heatmap illustrating the correlation between various metrics such as the distance

<!-- b000135 | prose | pages [5] -->
moved by two players, break point conversion rates, and winning points. Blue indicates a positive correlation, while green indicates a negative correlation.

<!-- b000136 | furniture | pages [5] -->
关注数学模型

<!-- b000137 | furniture | pages [5] -->
2

<!-- b000138 | furniture | pages [5] -->
MATHmodels

<!-- b000139 | furniture | pages [5] -->
获取更多资讯

<!-- b000140 | furniture | pages [6] -->
Team 2406324

<!-- b000141 | furniture | pages [6] -->
Page 5 of 25

<!-- b000142 | prose | pages [6] -->
In the graph, there is a clear positive correlation between the distances moved by the two players, a negative correlation in the winning points category, and varying degrees of positive correlation between their individual break point performance and overall break point conversion. As a result, it is possible to compress this initial ten-dimensional data vector into a lower-dimensional representation. In the same 微信公众号：数学模型 way, we can broadly categorize these factors into three groups. The result will be a three-dimensional vector, which saves a lot of computational resources in following analysis.

<!-- b000143 | heading | pages [6] -->
3.3 Data Overview

<!-- b000144 | prose | pages [6] -->
Analyzing the ”Number of Won Games per Set for each player” in a tennis match reveals insights into performance consistency, adaptability, and resilience. It showcases stamina, strategic adjustments, and psychological strength as players’ effectiveness evolves. This metric signifies a player’s ability to maintain or elevate their performance level under match pressure.Additionally, evaluating the ”Scoring Differences of Each Game in Each Set” unveils the match’s competitiveness, highlighting moments of dominance or vulnerability. It aids in identifying critical turning points and strategy effectiveness, 微信号：MATHmodels providing a detailed view that complements broader performance trends observed through won games. Together, these analyses comprehensively assess player dynamics and strategic outcomes in tennis matches.

<!-- b000145 | prose | pages [6] -->
(a) (b)

<!-- b000146 | caption | pages [6] -->
Figure 3: (a): Statistics of the number of games won by each player for each match. (b): Analysis of the

<!-- b000147 | prose | pages [6] -->
point difference between the two players in each game of each match. The size of the dots represents the absolute value of the point difference, and the color depth of the dots indicates the frequency of occurrence of that point difference.

<!-- b000148 | prose | pages [6] -->
In essence, Figure 3 (a) portrays the competitive nature of a tennis match, with both players having their moments of strength and struggle. The second figure highlights the competitiveness, momentum swings, and ultimately, the outcome of the match based on each player’s performance in individual games. Through these two figures, we can have an overview of the whole match. Both figures devide the match into five sets, which allows us to analyze the match from different perspectives. In this way, we obtain the basic ideas for further analysis: devide match into sets, and then into games.

<!-- b000149 | furniture | pages [6] -->
关注数学模型

<!-- b000150 | furniture | pages [6] -->
2

<!-- b000151 | furniture | pages [6] -->
MATHmodels

<!-- b000152 | furniture | pages [6] -->
获取更多资讯

<!-- b000153 | furniture | pages [7] -->
Team 2406324

<!-- b000154 | furniture | pages [7] -->
Page 6 of 25

<!-- b000155 | heading | pages [7] -->
4 Evaluation: Momentum and Swings

<!-- b000156 | heading | pages [7] -->
4.1 Definition of Momentum

<!-- b000157 | prose | pages [7] -->
微信公众号：数学模型 In physics, momentum represents a kind of force that is generated by the movement of an object. The faster you go, the harder it will be for someone to stop you. Here in tennis, the concept of momentum is almost the same. It represents the difficulty of stopping a player from his scoring streak, or the effort needed to reverse current disadvantages. To be more specific, the momentum of a player is largely determined by:

<!-- b000158 | prose | pages [7] -->
• Microscopically, the scoring of several hits in the vicinity of the moment;

<!-- b000159 | prose | pages [7] -->
• Macroscopically, the overall performance of the player in the current set.

<!-- b000160 | prose | pages [7] -->
Based on our understanding of momentum, its minimum unit of change is accurate to each point. Therefore, when studying the momentum of a certain player in a match, we want to design a function M(x), where the independent variable x is the number of the point in the match, and the dependent variable is the standardized momentum. Overall, this function M(x) is obtained by adding two parts, 微信号：MATHmodels namely:

<!-- b000161 | prose | pages [7] -->
M(x) = α · G(x) + β · P(x) + ϵ

<!-- b000162 | prose | pages [7] -->
G(x) mainly focuses on a baseline momentum value that each game within a set should have. For any point in a game, we will calculate an invariant baseline momentum value for the player based on the scoring conditions of the previous and next five games, which exactly builds up G(x). Taking the exponential weighted moving average (EWMA) algorithm as our reference, we formulated a specific calculation formula for G(x) (Lucas & Saccucci, 1990; Cox, 1961). To be noted, the weights have been slightly simplified and adjusted to ensure the consistency of the calculation of G(x) for serving and receiving games.

<!-- b000163 | prose | pages [7] -->
In our algorithm, the largest weight w0 = 0.4 is assigned to the score of the current game, denoted as g0; the adjacent previous and next game scores g−1, g1 were assigned moderate weights w−1 = w1 = 0.25; the two games further backward and forward g−2, g2 were assigned the smallest weights w−2 = w2 = 0.05. Since g−2, g0, and g2 belong to serving games while the rest two g−1, and g1 belong to receiving games (or both two group reversed), we allocated a total weight of 0.5 to each category to ensure consistency in calculating G(x) for either serving or receiving games. In conclusion, we have:

<!-- b000164 | prose | pages [7] -->
i=2 X wi · gi = 0.05 g−2 + 0.25 g−1 + 0.4 g0 + 0.25 g1 + 0.05 g2 G(x) = i=−2

<!-- b000165 | prose | pages [7, 8] -->
Considering the game scores gi assigned based on the scoring conditions of each game, we believe simply using the scoring rate linearly is flawed. For example, previous research has pointed out that a 100% scoring rate to win a game should boost momentum slightly more than a 67% rate, such as leading 40:30 then winning one more point (Weinberg & Jackson, 1989). However, losing the game with a 33% rate, although still only differing by 33% from 67%, represents a huge change in momentum. Therefore, we introduced sigmoid function instead of the linear relationship between game score and scoring rate, to greatly amplify the impact on momentum between winning and losing a game. Figure 4 provides a direct comparison, as the green region is largely expanded by the sigmoid function. Denote the scoring rate of the i-th game as ri, we have:

<!-- b000166 | furniture | pages [7] -->
关注数学模型

<!-- b000167 | furniture | pages [7] -->
2

<!-- b000168 | furniture | pages [7] -->
MATHmodels

<!-- b000169 | furniture | pages [7] -->
获取更多资讯

<!-- b000170 | furniture | pages [8] -->
Team 2406324

<!-- b000171 | furniture | pages [8] -->
Page 7 of 25

<!-- b000173 | prose | pages [8] -->
e10ri−5 0 ⩽ri ⩽1 gi = 1 + e10ri−5, 微信公众号：数学模型 微信号：MATHmodels (a) (b)

<!-- b000174 | caption | pages [8] -->
Figure 4: Comparison of the linear and sigmoid relationship between scoring rate and game score. (a)

<!-- b000175 | prose | pages [8] -->
Linear relationship (b) Sigmoid relationship. The difference between 33% and 67% scoring rate is emphasized by the sigmoid function.

<!-- b000176 | prose | pages [8] -->
The two plots shown above serve as a direct comparison between the linear and sigmoid relationship between scoring rate and game score. The x-axis represents the scoring rate, and the y-axis represents the game score, both ranging from 0 to 1. Near the middle point (0.5, 0.5), the sigmoid function has a much steeper slope than the linear function, which means that the momentum change becomes more sensitive to the win or loss of the game. As shown in the figure, the sharp difference between 33% and 67% scoring rate is now very obvious, which is consistent with our expectations.

<!-- b000177 | prose | pages [8] -->
On this basis, P(x) focuses on momentum changes within a game due to differences in consecutive points or overall scoring situations. Similar to G(x), we applied EWMA at the more microscopic level of adjusting by points within a game (Hunter, 1986). Likewise, to ensure strong correlation between momentum and current scoring as well as previous and next scoring differences, we decided to assign different weights to the scoring conditions of the previous and next five points. To keep a sense of continuity, we set the weights for point scores to be the same as the weights for game scores, namely ωi = wi. Thus we have:

<!-- b000178 | prose | pages [8] -->
i=2 X ωi · pi = 0.05 p−2 + 0.25 p−1 + 0.4 p0 + 0.25 p1 + 0.05 p2 P(x) = i=−2

<!-- b000179 | prose | pages [8, 9] -->
Here pi = 1 means the player wins the point while pi = −1 means the player loses the point. With the addition of G(x) and P(x), we have successfully defined the momentum function M(x). To be noted, we have standardized the momentum function M(x) and set α = 1, β = 0.05, γ = 0. The momentum of two players at one moment always add up to one. The core idea over the whole process is visualized in Figure 3 below. In the picture, the darker the pattern is, the further it is from the current moment. Green ball represents winning the point and black ball represents losing it there.

<!-- b000180 | furniture | pages [8] -->
关注数学模型

<!-- b000181 | furniture | pages [8] -->
2

<!-- b000182 | furniture | pages [8] -->
MATHmodels

<!-- b000183 | furniture | pages [8] -->
获取更多资讯

<!-- b000184 | furniture | pages [9] -->
Team 2406324

<!-- b000185 | furniture | pages [9] -->
Page 8 of 25

<!-- b000187 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000188 | caption | pages [9] -->
Figure 5: Schematic of the model for computing momentum (biggest ball represents ”now”).

<!-- b000189 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000190 | heading | pages [9] -->
4.2 Model Visualization and Validation

<!-- b000191 | prose | pages [9] -->
With our definition of momentum, we are now able to identify which player is performing better at any moment. We can also visualize the momentum change over the whole preocess by plotting the momentum function M(x) against the point number x. Take the classical match between Alcaraz and Djokovic in the 2023 Wimbledon Gentlemen’s final as an example, we can see the momentum change of both players in Figure 6 below.

<!-- b000192 | caption | pages [9] -->
Figure 6: Analysis of the momentum in the 2023 Wimbledon Gentlemen’s final. The green area

<!-- b000193 | prose | pages [9] -->
represents Djokovic’s momentum, while the blue stones correspond to Alcaraz. The scores for the five sets were 6:1, 6:7, 1:6, 6:3, 4:6. Djokovic narrowly lost to Alcaraz with a total score of 2:3.

<!-- b000194 | furniture | pages [9] -->
关注数学模型

<!-- b000195 | furniture | pages [9] -->
2

<!-- b000196 | furniture | pages [9] -->
MATHmodels

<!-- b000197 | furniture | pages [9] -->
获取更多资讯

<!-- b000198 | furniture | pages [10] -->
Team 2406324

<!-- b000199 | furniture | pages [10] -->
Page 9 of 25

<!-- b000200 | prose | pages [10] -->
As shown in the picture, the momentum of Djokovic largely repressed Alcaraz’s momentum in the first set. This is exactly the case as Djokovic won five games in a row at the very begining. The fluctuating curves that follow show both players becoming locked in a grueling battle in the second set, which is consistent with the final result of the second set being decided by a tiebreak. In this sense, we 微信公众号：数学模型 can say that our model is able to reflect the real situation of the match.

<!-- b000201 | prose | pages [10] -->
To further apply our model, we might be interested in the deep reasons behind the runs of success by one player. Intuitively speaking, the worth-noticing swings in play happen when the momentum of one player changes significantly. Put it graphically, these swings are located at the sharp corners of the momentum curve.

<!-- b000202 | prose | pages [10] -->
However, from our rough curve, we might end up with a lot of ”swinging points”, most of which happening When the two players are competing steadily but fiercely. For example, from the second set shown in Figure 4, we can find many sharp corners. This is a result from the two players’ good and steady performance in their own service games, which is not what we want for swings. To solve this problem, we came up with an idea to filter out the ”unimportant” corners by smoothening the curve.

<!-- b000203 | prose | pages [10] -->
微信号：MATHmodels (a) (b)

<!-- b000204 | prose | pages [10] -->
(c) (d)

<!-- b000205 | caption | pages [10] -->
Figure 7: Comparison of the four filtering algorithms: (a) Moving Median Filter (b) FIR Filter (c)

<!-- b000206 | prose | pages [10] -->
Wavelet Filter (d) Convolutional Moving Average Filter. The one we chose is (c) Wavelet Filter. Grean circles show where the filtering algorithm performed unsatisfactorily.

<!-- b000207 | furniture | pages [10] -->
关注数学模型

<!-- b000208 | furniture | pages [10] -->
2

<!-- b000209 | furniture | pages [10] -->
MATHmodels

<!-- b000210 | furniture | pages [10] -->
获取更多资讯

<!-- b000211 | furniture | pages [11] -->
Team 2406324

<!-- b000212 | furniture | pages [11] -->
Page 10 of 25

<!-- b000213 | prose | pages [11] -->
The main idea behind smoothing the curves borrows from several algorithms in digital signal processing. Our goal is to filter outliers and anomalies while preserving the momentum change trends and other key features, in order to effectively process non-stationary and nonlinear data values.

<!-- b000214 | prose | pages [11] -->
微信公众号：数学模型 Initially, we adopted the moving median filter method similar to setting up a sliding window and weights as described above (Yin & Lin, 1996). We also tried to emulate hardware filtering implementations using an FIP filter (Lim, Yong, & Parker, 1983). In addition, we drew on more recent studies, trying wavelet filters and convolutional moving average filters respectively (Qiu & Hai, 2006; Trad, Daniel, & Travassos, 2000; Yin & Du, 2022). Figure 7 above combines and compares the results obtained by the four filtering algorithms when selecting wavelet ”coif5” and decomposition level to be three.

<!-- b000215 | prose | pages [11] -->
Comparing the four filtering effect charts, it is evident that the curve obtained by the wavelet filter meets our requirements best. The curves from the convolutional moving average filter do not stay close enough to the original function at the beginning and ending stages, and fail to fit the intense competition at the end of the fourth game. The FIR filter result exhibits significant lagging, while the moving median filter leads to many step-like functions, disqualifying both methods. From the curve 微信号：MATHmodels processed by the wavelet filter, we can identify the time points when the players’ momentums reach steady extreme values, capturing the important points during the match’s progression.

<!-- b000216 | heading | pages [11] -->
4.3 Randomness & Certainty of Swings

<!-- b000217 | caption | pages [11] -->
Figure 8: The first-order derivative of the momentum function M(x) in the 2023 Wimbledon Gentle-

<!-- b000218 | prose | pages [11] -->
men’s final. The blue points are the swings we are looking for. As we are labeling integer points, there might be some deviation.

<!-- b000219 | furniture | pages [11] -->
关注数学模型

<!-- b000220 | furniture | pages [11] -->
2

<!-- b000221 | furniture | pages [11] -->
MATHmodels

<!-- b000222 | furniture | pages [11] -->
获取更多资讯

<!-- b000223 | furniture | pages [12] -->
Team 2406324

<!-- b000224 | furniture | pages [12] -->
Page 11 of 25

<!-- b000225 | prose | pages [12] -->
In fact, these extreme points on the momentum curve are not necessarily the swings we are looking for. When swings taken place, both players might expect a sharp change in momentum, which actually requires the a large enough curvature. In other words, the points with zero first derivatives of momentum and large absolute value of second derivatives are the swings we are looking for. As a result, we decided 微信公众号：数学模型 to calculate the first order difference of the momentum function M(x). The results are shown in Figure 8 above. The points with zero first-order difference and second-order difference with absolute value bigger than 0.03 is labeled blue as swings point.

<!-- b000226 | prose | pages [12] -->
Still take the 2023 Wimbledon Gentlemen’s final as an example, we now discuss whether the swings happen randomly. We first applies a run test to determine the randomness by labeling the swings as ”1” and other normal points as ”0”. The P value calculated by the run test is 0.000, far less than 0.05, which means the swings are random in the aspect of statistics.

<!-- b000227 | prose | pages [12] -->
However, when we try to find the events that lead to these turning points, we find that these swings in momentum have actual meanings. For example, the 68th point in the first set has zero first derivatives in momentumand a large second derivative. This is exactly the point when Djokovic, under a streak of consecutive losses, forcefully broke Alcaraz’s serve to break the slump. This turning point indicates 微信号：MATHmodels the swing from Alcaraz’s dominance to a phase of equilibrium established by two players.

<!-- b000228 | prose | pages [12] -->
Similarly, the 296th point in the second set is another very important turning point. Here the first derivative of momentum is zero and the second derivative is very large. This is the point when Alcaraz, under a streak of consecutive losses, broke Djokovic’s serve to break the slump. In the opening stages of the decisive set, a crucial break was efficiently achieved, breaking the deadlock. After that, there were no more turning points to assist Djokovic in making a comeback, signaling Alcaraz’s impending victory as he lifted the ultimate championship trophy.

<!-- b000229 | prose | pages [12] -->
In conclusion, the swings in momentum are random if they are viewed solely as a sequence of numbers. However, when we take other factors into consideration, we find that these swings are certain to happen to some extent. The certainty will be quantified and discussed in the next section. Now what our estimation model tells us is the momentum curve and the swings throughout any known man’s tennis match.

<!-- b000230 | heading | pages [12] -->
5 Prediction: Time Series Forcasting

<!-- b000231 | heading | pages [12] -->
5.1 Model Selection: RNN, GRU, & LSTM

<!-- b000232 | prose | pages [12] -->
Now that we have processed the data and obtained enough data for momentum and swings, we are ready to predict the future of a match. In last sections, we have verified the correlation between momentum and other factors like the distance covered by two players. Against this background, we would like to make use of the whole dataset in our prediction model. Although we have compressed the data by reducing its dimension (PCA), there still exists factors too many for us to adjust the weights manually. Therefore, we decided to apply different Rerrent Neural Network (RNN) to predict the future of a match.

<!-- b000233 | prose | pages [12, 13] -->
Given our goal of processing sequential data, we ultimately decided to select the model with the best predictive performance from among basic RNN and its more advanced counterparts GRU and LSTM. We controlled the training dataset to be consistent and chose the first match in the table data (match id 2023-wimbledon-1301) as the unified test set. According to previous research, RNN might have difficulty with long-term dependencies due to vanishing gradients. GRU solves this problem by using gating mechanisms. For LSTM, those explicitly designed memory cells might perform better in modeling long-term dependencies, which is required in our task. So we expect LSTM to outperform 微信公众号：数学模型 the other two models. The loss function we use to train our networks is shown as follows:

<!-- b000234 | furniture | pages [12] -->
关注数学模型

<!-- b000235 | furniture | pages [12] -->
2

<!-- b000236 | furniture | pages [12] -->
MATHmodels

<!-- b000237 | furniture | pages [12] -->
获取更多资讯

<!-- b000238 | furniture | pages [13] -->
Team 2406324

<!-- b000239 | furniture | pages [13] -->
Page 12 of 25

<!-- b000241 | prose | pages [13] -->
sPN x=1[P1(x) −R1(x)]2 + PN x=1[P2(x) −R2(x)]2 L = 2N

<!-- b000242 | prose | pages [13] -->
Here, L represents the loss, N represents the maxmimum point number in this match, P1/2(x) represents the predicted momentum of the first/second player at the x-th point, while R1/2(x) represents the real momentum of the first/second player at the x-th point. In building the neural networks, we chose a structure of embedding GRU / LSTM / RNN (3 layers: 32 + 32 + 16 nodes respectively) with dense layers (16 + 2 nodes) for all three models. The number of layers and nodes were kept consistent. As shown in Figure 9 below, our three neural networks had overall similar structures, with 微信号：MATHmodels small differences in the details.

<!-- b000243 | caption | pages [13] -->
Figure 9: The common structure of the three rerrent neural networks. The input layer is followed by

<!-- b000244 | prose | pages [13] -->
three hidden layers, which makes the difference.

<!-- b000245 | caption | pages [13] -->
Figure 10 below shows the prediction results from the three models without any additional im-

<!-- b000246 | prose | pages [13] -->
provements. From the fit between the predicted curves and true momentum curves, we can see that the predictions from GRU and RNN were decent, while the most advanced LSTM was quite unsatis- factory. This could be because the training dataset is too small, and there exist noticeable differences between matches. This result, inconsistent with our expectations, prompted us to improve the models by introducing clustered transfer learning.

<!-- b000247 | furniture | pages [13] -->
关注数学模型

<!-- b000248 | furniture | pages [13] -->
2

<!-- b000249 | furniture | pages [13] -->
MATHmodels

<!-- b000250 | furniture | pages [13] -->
获取更多资讯

<!-- b000251 | furniture | pages [14] -->
Team 2406324

<!-- b000252 | furniture | pages [14] -->
Page 13 of 25

<!-- b000253 | prose | pages [14] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000254 | caption | pages [14] -->
Figure 10: Comparison of the prediction given by three neural networks. The dark purple curve

<!-- b000255 | prose | pages [14] -->
represents the true momentum curve, while the blue, green, and light purple curves represents the momentum curves predicted by RNN, GRU, and LSTM respectively.

<!-- b000256 | heading | pages [14] -->
5.2 Transfer Learning: PCA & K-means

<!-- b000257 | prose | pages [14] -->
In order to improve our model, we need to cluster the matches in the dataset into a few groups. Here we temporarily set the number to be 3, and use the K-means algorithm to cluster the matches. Due to computational constraints, we first used PCA to reduce the full dataset down to 3-dimensional data points, under the premise of preserving the correlations between the different factor data. We then randomly selected three points as cluster centers to start the iteration. In each iteration, we first computed the distances between all points and centers. Next, for each point we found its nearest center, and assigned it to the cluster represented by that center. Finally, we updated each center using the mean of the points in its cluster. The iteration stopped when the change in center positions was small enough.

<!-- b000258 | heading | pages [14] -->
Algorithm 1: k-Means Clustering Algorithm

<!-- b000259 | prose | pages [14] -->
Data: Dataset with n data points and cluster numbers k

<!-- b000260 | heading | pages [14] -->
Result: Cluster groups and cluster centroids

<!-- b000261 | heading | pages [14] -->
1 Initialize k centroids by randomly selecting k points

<!-- b000262 | prose | pages [14] -->
2 while Change of cluster center centroids is larger than a threshold do for Each data point do 3 for Each centroid do 4 Calculate the distance between the centroid and the data point 5

<!-- b000263 | prose | pages [14] -->
Assign the data point to the cluster with the nearest centroid 6 Append the cluster number to the data point 7

<!-- b000264 | prose | pages [14, 15] -->
for Each cluster do 8 Calculate the mean and update it as the new centroid 9 After K-means clustering, we are then able to conduct clustered transfer learning. For the validation set, i.e. the first match, we first identified matches in the same cluster, i.e. closest matches, among the three clusters. We trained the models on these matches, and then trained again on the first match with its given dataset. The three plots (a), (b), and (c) at the first line of Figure 11 show the prediction 微信公众号：数学模型 capabilities of all three models were greatly improved. Among them, LSTM’s performance caught up with the other two models, reaching a level that was basically consistent with or even surpassing them. We can also stop training the model without going back to the first match (test dataset). It turned out to give us a better result, as shown in the corresponding three plots at second line of Figure 11.

<!-- b000265 | furniture | pages [14] -->
关注数学模型

<!-- b000266 | furniture | pages [14] -->
2

<!-- b000267 | furniture | pages [14] -->
MATHmodels

<!-- b000268 | furniture | pages [14] -->
获取更多资讯

<!-- b000269 | furniture | pages [15] -->
Team 2406324

<!-- b000270 | furniture | pages [15] -->
Page 14 of 25

<!-- b000272 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000273 | caption | pages [15] -->
Figure 11: The prediction results of the three models after introducing clustered transfer learning. The

<!-- b000274 | prose | pages [15] -->
first line shows the results after training the model on the first match, while the second line shows the results after training the model without going back to the first match.

<!-- b000275 | prose | pages [15] -->
In order to more rigorously demonstrate the performance of the three prediction models after introducing clustered transfer learning, we recorded the train loss and test loss data for each model in the table (Figure 12) below. Reassuringly, the LSTM model achieved a test loss of 0.2 under the Only Transfer with Clustering training method, close to its performance on the training set and becoming the most accurate among the three models. Meanwhile, ”train loss = test loss” also means that if we expand the size of the training dataset, it is very likely that we can further easily improve the test performance of the LSTM model. At this point, we have determined to use the LSTM model as our prediction model, and further examination of its capabilities will be discussed in the sensitivity analysis.

<!-- b000276 | furniture | pages [15] -->
关注数学模型

<!-- b000277 | furniture | pages [15] -->
2

<!-- b000278 | furniture | pages [15] -->
MATHmodels

<!-- b000279 | furniture | pages [15] -->
获取更多资讯

<!-- b000280 | furniture | pages [16] -->
Team 2406324

<!-- b000281 | furniture | pages [16] -->
Page 15 of 25

<!-- b000282 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000283 | caption | pages [16] -->
Figure 12: The train loss and test loss of the three models after introducing clustered transfer learning.

<!-- b000284 | heading | pages [16] -->
5.3 Related Factors: XGBoost & SHAP

<!-- b000285 | prose | pages [16] -->
Neural networks are well known for their excellent performance when working with large datasets. 微信号：MATHmodels With the current dataset, we have increased the prediction accuracy of LSTM on momentum to a relatively high level through various improvement methods. Through the algorithms mentioned previously, we can accurately identify the occurrences of swings based on the momentum curves, and provide tennis players and coaches with a proper predictive interval. The neural network is quite outstanding in terms of predictive capabilities.

<!-- b000286 | prose | pages [16] -->
However, as a nonlinear model, the mapping between inputs and outputs in a neural network is very complex, making it difficult to decompose the inputs and calculate each factor’s correlation. Moreover, as shown in Figure 8 above, although the embedding layers are different, all neural network models can have complex structure in one layer alone. The might also face the issue that the same input contributes differently at different time steps. In theory, we could try adding random noise to the input vectors and check which inputs affect the prediction results the most when noisy. But this requires us to abandon PCA dimensionality reduction on the original dataset, which means a training process that consumes huge computational resources and time. This poses considerable difficulties for our current team.

<!-- b000287 | prose | pages [16] -->
Therefore, we decided to introduce the XGBoost model along with the SHAP model to help us analyze the importance of each factor in the prediction. XGBoost is a kind of gradient boosting decision tree model, which is very good at analyzing the importance of each factor in the prediction. It provided us with a way to predict momentum and swings without reducing the dimensionality of the original dataset. We used the same dataset as the training set for the neural network, and the same test set as the validation set. The results are shown in Figure 13 below. The importance of each factor is calculated by the average gain of the factor in the decision tree. The larger the average gain, the more important the factor is in the prediction. In other words, the top 5 factors in the figure are the most related factors to the swings in man’s tennis matches.

<!-- b000288 | furniture | pages [16] -->
关注数学模型

<!-- b000289 | furniture | pages [16] -->
2

<!-- b000290 | furniture | pages [16] -->
MATHmodels

<!-- b000291 | furniture | pages [16] -->
获取更多资讯

<!-- b000292 | furniture | pages [17] -->
Team 2406324

<!-- b000293 | furniture | pages [17] -->
Page 16 of 25

<!-- b000294 | prose | pages [17] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000295 | caption | pages [17] -->
Figure 13: The importance of each factor in the prediction

<!-- b000296 | prose | pages [17] -->
As we can clearly see from the figure, the factor most related with the swings are the distance run by the two players during points. Following are the game numbers of the two players, whose importance is self-evident. Other related factors are the speed, direction, and depth of serve. The depth of return also plays an important role.

<!-- b000297 | prose | pages [17] -->
With the conclusion above at hand, we are now able to give advice to players who are going to start a match with different opponents. Analysis of the momentum curve data from their previous matches should play the most important role here. We can analyze the curve and swings from an overall point of view, or compare the correlation between momentum and those most-important factors one by one.

<!-- b000298 | prose | pages [17] -->
For example, if player A’s past momentum swings show a concentrated distribution, it indicates relatively stable state changes. In contrast, a more dispersed distribution for player B suggests less stable fluctuations. We can then recommend the more stable player A to adopt an aggressive offensive play, as once gaining an advantage, he is more likely to maintain momentum until winning. Meanwhile, player B with larger state variations should play cautiously and avoid falling behind early.

<!-- b000299 | prose | pages [17] -->
We can also compare the timing distribution of momentum swings in past matches. This also provides useful suggestions. For example, if player A often drops momentum (concentrated negative swings) in late 2nd set, it is very likely that he will experience a physical limit during that point. As a result, he is suggested to pay more attention and assign more strength to that stage of match.

<!-- b000300 | prose | pages [17] -->
In summary, by examining differences in momentum curve characteristics between the two players’ previous matches, we can identify rhythmic and psychological fluctuation patterns unique to each player. This helps us offer strategic advice to tennis players for their new matches. It demonstrates the extensibility and practical value of our momentum prediction model.

<!-- b000301 | furniture | pages [17] -->
关注数学模型

<!-- b000302 | furniture | pages [17] -->
2

<!-- b000303 | furniture | pages [17] -->
MATHmodels

<!-- b000304 | furniture | pages [17] -->
获取更多资讯

<!-- b000305 | furniture | pages [18] -->
Team 2406324

<!-- b000306 | furniture | pages [18] -->
Page 17 of 25

<!-- b000307 | heading | pages [18] -->
6 Sensitivity Analysis

<!-- b000308 | prose | pages [18] -->
The real sports competition environment is often much more complex than these theoretical data tables. While our neural network model has achieved very good performance on existing datasets, 微信公众号：数学模型 considering unexpected factors in real-world scenarios, it’s very likely that there may be inaccuracies in the data collected before the game. After data processing and cleaning, the number of eligible data points may be limited and may not reach our expected optimal number of around ten data points. Therefore, we are conducting sensitivity testing on the model here to assess its practical applicability in real sports competition scenarios.

<!-- b000309 | heading | pages [18] -->
6.1 Step Size in the LSTM Model

<!-- b000310 | prose | pages [18] -->
Since we have chosen LSTM as the basis for the momentum prediction model, the sensitivity analysis will focus on its step size. That is, we want to obtain the relationship between model prediction accuracy and the amount of data provided by the test set. The final results are shown in Figure 14, 微信号：MATHmodels the bar chart below, which is beyond our expectations. For LSTM alone, even increasing the step size to 30 is far from the amount of data it needs to achieve the ideal prediction effect, which is also why we introduced cluster and transfer learning. For the LSTM only with transfer learning prediction method we approve as the most accurate, we find that a step size around 10 is already sufficient to make relatively accurate predictions, and further expanding the step size may even risk reducing accuracy.

<!-- b000311 | caption | pages [18] -->
Figure 14: Sensitivity analysis of the step size in the LSTM model. The x-axis represents the step

<!-- b000312 | prose | pages [18] -->
size, and the y-axis represents the prediction accuracy. The blue bar represents the prediction accuracy of the LSTM model, and the orange bar represents the prediction accuracy of the LSTM model with transfer learning.

<!-- b000313 | furniture | pages [18] -->
关注数学模型

<!-- b000314 | furniture | pages [18] -->
2

<!-- b000315 | furniture | pages [18] -->
MATHmodels

<!-- b000316 | furniture | pages [18] -->
获取更多资讯

<!-- b000317 | furniture | pages [19] -->
Team 2406324

<!-- b000318 | furniture | pages [19] -->
Page 18 of 25

<!-- b000319 | prose | pages [19] -->
As a result, we suggest that when making predictions for men’s tennis matches with a five-set system, try to use a step size of 10-15 balls to predict the next ball, and even the general trend of the entire match. Under the current situation where the training set size is limited, blindly increasing the step size not only fails to achieve better results, but also risks reducing the credibility of the prediction. 微信公众号：数学模型 In more intuitive terms, from the perspective of neural network models, the trend of each point in a men’s tennis match often has a higher correlation with the local context than the global context. The sensitivity analysis tells us that coaches may want to pay more attention to players’ performances in the first two to three sets, in order to assess their current state. Standing from a higher perspective and using the overall trend as the logical fulcrum, it is actually more likely to misjudge the current situation.

<!-- b000320 | heading | pages [19] -->
6.2 The Number of Clusters in K-means

<!-- b000321 | prose | pages [19] -->
In our prediction model (LSTM), another parameter worth further research is the number of clusters K in the K-means algorithm. Here, we will explain why all matches are divided into three categories in the previous section, and show the impact of the number of clusters on the prediction capability of 微信号：MATHmodels the model, taking LSTM as an example. We set the number of clusters to be 1-5, 10, 15 respectively, and present the deviation rate of the prediction model on the test case (Match 1301) in the form of a bar chart in Figure (a) below.

<!-- b000322 | prose | pages [19] -->
(a) (b)

<!-- b000323 | caption | pages [19] -->
Figure 15: (a): The deviation rate of the LSTM model on the test case (Match 1301) under different

<!-- b000324 | prose | pages [19] -->
numbers of clusters. (b): The three-cluster result in the 3-dimensional space.

<!-- b000325 | prose | pages [19] -->
As can be seen from the above figure, the performance of the prediction model reaches its minimum when the number of clusters is 3. Therefore, we choose to divide all matches into three categories in the previous analysis. The three-cluster result in the 3-dimensional space is shown in Figure (b) above. In future work, we will further explore the impact of the number of clusters on the prediction model with a much bigger dataset.

<!-- b000326 | furniture | pages [19] -->
关注数学模型

<!-- b000327 | furniture | pages [19] -->
2

<!-- b000328 | furniture | pages [19] -->
MATHmodels

<!-- b000329 | furniture | pages [19] -->
获取更多资讯

<!-- b000330 | furniture | pages [20] -->
Team 2406324

<!-- b000331 | furniture | pages [20] -->
Page 19 of 25

<!-- b000332 | heading | pages [20] -->
7 Conclusion

<!-- b000333 | heading | pages [20] -->
7.1 Strength and Weakness

<!-- b000334 | prose | pages [20] -->
微信公众号：数学模型 Our model is mainly divided into two parts: evaluation and prediction. Although completely different basic models are chosen, they share very similar strengths and weaknesses. Our main strength lies in the evaluation curve fitting the match situation changes, swings being almost always related to crucial moments on court, and the prediction results also providing some valuable information.

<!-- b000335 | prose | pages [20] -->
Our main weaknesses are the small dataset, lack of strong transferability of the model, and insuf- ficient neural network training. This results in a currently narrow applicable scope of our model, and limited prediction accuracy. To some extent, our model is not convincing enough.

<!-- b000336 | heading | pages [20] -->
7.2 Future Work

<!-- b000337 | prose | pages [20] -->
By testing our model on other matches, we regretfully find that our model does not possess 微信号：MATHmodels strong generalizability. When we use our model to predict the momentum changes in women’s tennis matches, there are significant divergences between the predictions and reality (data from https://www.livesport.com/en/tennis/wta-singles/us-open/). Part of the reason, of course, is that our training dataset is entirely based on men’s Wimbledon tennis matches played over five sets. The differ- ences between five-set matches and three-set matches in terms of score distribution, physical exertion, and game dynamics are quite substantial, making such a model transfer inappropriate.

<!-- b000338 | prose | pages [20] -->
Furthermore, in previous research, we have learned that gender plays an important role in momentum (Page & Coats, 2017). From the results of the winner effect (success breeds success) studies, it seems that women are less influenced by momentum due to their lower circulating testosterone levels compared to men (Page & Coats, 2017). Of course, there were also arguments that the difference between male and female tennis players was gradually closing in term of their reaction toward momentum (Weinberg, Robert, & Jackson, 1989). In the future, we may consider increasing the weight of factors that objectively affect players’ physical fitness reserves, while reducing the weight of factors which have a greater impact on players’ psychological fluctuations for women’s model.

<!-- b000339 | prose | pages [20] -->
Similarly, when we use the momentum model for assessing and predicting the situation in team sports, the results are not ideal either. Take volleyball matches as an example; it is challenging to predict the course of a match through momentum, let alone the fact that volleyball team coaches can strategically call timeouts to disrupt or break the opponent’s advantageous momentum. Our findings align with previous research, which suggests that in team sports with multiple players, the overall impact of momentum is greatly weakened (Fu, Ke & Tan, 2015). The on-court scoring reflects the teamwork and synergy of the team more than the individual players’ psychological activities or skills. In these cases, we may consider focusing more on strategic momentum rather than psychological momentum.

<!-- b000340 | prose | pages [20] -->
For the prediction model of tennis momentum, two methods can be used to further improve it. On one hand, better clustering methods can be applied. Clustering methods for time series data have been emerging in recent years, which achieve better effects in grouping the elements (Saito et al. 2024; Inoue et al. 2024). On the other hand, various data synthesizing methods have been proposed, which can solve the problem of insufficient data, thus upgrading the performance of deep learning models (Yoon et al. 2019; Theodorou et al. 2023).

<!-- b000341 | furniture | pages [20] -->
关注数学模型

<!-- b000342 | furniture | pages [20] -->
2

<!-- b000343 | furniture | pages [20] -->
MATHmodels

<!-- b000344 | furniture | pages [20] -->
获取更多资讯

<!-- b000345 | furniture | pages [21] -->
Team 2406324

<!-- b000346 | furniture | pages [21] -->
Page 20 of 25

<!-- b000347 | heading | pages [21] -->
8 Memorandum

<!-- b000348 | prose | pages [21] -->
To: Tennis Coaches and Players From: MCM Team #2406324 微信公众号：数学模型 Date: Feb 6th, 2024 RE: Utilizing Momentum Analysis for Enhanced Performance in Tennis Matches

<!-- b000349 | heading | pages [21] -->
Executive Summary:

<!-- b000350 | prose | pages [21] -->
This memorandum summarizes our findings on the role of momentum in tennis, drawing on comprehensive analysis conducted on Wimbledon 2023 men’s matches data. Our research underscores the impact of momentum swings on match outcomes and provides actionable strategies for coaches to prepare players for effectively managing these dynamics. For detailed insights and data-driven evidence, readers are directed to sections covering the evaluation of momentum (Section 4), its prediction (Section 5), and sensitivity analysis (Section 6) within our full research paper.

<!-- b000351 | prose | pages [21] -->
Understanding Momentum’s Role: 微信号：MATHmodels Our analysis unequivocally demonstrates that momentum significantly influences the flow and eventual outcomes of tennis matches. An increase in momentum correlates with improved performance, while a decrease often precedes a shift in match dynamics. Key indicators of momentum shifts include consecutive winning points and critical game-winning performances, which can serve as precursors to changes in the game’s flow.

<!-- b000352 | prose | pages [21] -->
Strategies for Coaches and Players: 1. Psychological Resilience Training Encourage mental toughness and focus, particularly in situations where momentum is not in the player’s favor. Techniques such as visualization, positive self-talk, and stress reduction can be invaluable in maintaining composure and concentration during pivotal moments.

<!-- b000353 | prose | pages [21] -->
2. Analyzing Opponent Data Leverage match data to identify patterns or weaknesses in opponents that could lead to momentum shifts. This involves a thorough analysis of previous matches to understand potential triggers for momentum changes and developing strategies to exploit these opportunities.

<!-- b000354 | prose | pages [21] -->
3. Simulating Momentum Shifts in Practice Incorporate scenarios in training sessions that mimic situations where momentum shifts occur. This will help players adapt to various match situations, enhancing their ability to respond effectively to both positive and negative momentum swings.

<!-- b000355 | heading | pages [21] -->
Conclusion and Suggestions:

<!-- b000356 | prose | pages [21] -->
Momentum plays a crucial role in the dynamics of tennis matches, influencing both the psychological state of players and the overall match outcome. By recognizing the signs of momentum shifts and preparing strategies to manage these changes, coaches and players can gain a competitive edge. It is essential to integrate momentum management into training regimes and match strategies to optimize performance and achieve success in competitive tennis play.

<!-- b000357 | prose | pages [21] -->
For further details on our methodologies, data analysis, and additional recommendations, please refer to the comprehensive sections within our research paper.

<!-- b000358 | furniture | pages [21] -->
关注数学模型

<!-- b000359 | furniture | pages [21] -->
2

<!-- b000360 | furniture | pages [21] -->
MATHmodels

<!-- b000361 | furniture | pages [21] -->
获取更多资讯

<!-- b000362 | furniture | pages [22] -->
Team 2406324

<!-- b000363 | furniture | pages [22] -->
Page 21 of 25

<!-- b000364 | heading | pages [22] -->
References

<!-- b000365 | references | pages [22] -->
[1] Beaton, George H. ”Approaches to analysis of dietary data: relationship between planned analyses

<!-- b000366 | references | pages [22] -->
and choice of methodology.” The American journal of clinical nutrition 59.1 (1994): 253S-261S.

<!-- b000367 | references | pages [22] -->
微信公众号：数学模型

<!-- b000368 | references | pages [22] -->
[2] Cox, D.R., Prediction by Exponentially Weighted Moving Averages and Related Methods. Journal

<!-- b000369 | references | pages [22] -->
of the Royal Statistical Society: Series B (Methodological), 23: 414-422 (1961).

<!-- b000370 | references | pages [22] -->
[3] Daniel, Christian, Jonathan Taylor, and Sebastian Nowozin. ”Learning step size controllers for

<!-- b000371 | references | pages [22] -->
robust neural network training.” Proceedings of the AAAI Conference on Artificial Intelligence.

<!-- b000372 | references | pages [22] -->
Vol. 30. No. 1. 2016.

<!-- b000373 | references | pages [22] -->
[4] Deng, Y., Lu, L., Aponte, L. et al. Deep transfer learning and data augmentation improve glucose

<!-- b000374 | references | pages [22] -->
levels prediction in type 2 diabetes patients. npj Digit. Med. 4, 109 (2021).

<!-- b000375 | references | pages [22] -->
[5] Dietl, Helmut, and Cornel Nesseler. ”Momentum in tennis: Controlling the match.” UZH Business

<!-- b000376 | references | pages [22] -->
Working Paper Series 365 (2017).

<!-- b000377 | references | pages [22] -->
微信号：MATHmodels

<!-- b000378 | references | pages [22] -->
[6] Hu, M., Zhang, H., Wu, B. et al. Interpretable predictive model for shield attitude control

<!-- b000379 | references | pages [22] -->
performance based on XGboost and SHAP. Sci Rep 12, 18226 (2022).

<!-- b000380 | references | pages [22] -->
[7] Inoue, T., Kubota, K., Ikami, T. et al. Clustering method for time-series images using quantum-

<!-- b000381 | references | pages [22] -->
inspired digital annealer technology. Commun Eng 3, 10 (2024).

<!-- b000382 | references | pages [22] -->
[8] James M. Lucas & Michael S. Saccucci Exponentially Weighted Moving Average Control

<!-- b000383 | references | pages [22] -->
Schemes: Properties and Enhancements, Technometrics, 32:1, 1-12 (1990).

<!-- b000384 | references | pages [22] -->
[9] Jim Albert, Ruud H. Koning / Jim Albert, Ruud H. Koning. Statistical Thinking in Sports. 1st ed.,

<!-- b000385 | references | pages [22] -->
Chapman and Hall/CRC, (2007).

<!-- b000386 | references | pages [22] -->
[10] Jinsung Yoon, Daniel Jarrett, and Mihaela van der Schaar. 2019. Time-series generative adversarial

<!-- b000387 | references | pages [22] -->
networks. Proceedings of the 33rd International Conference on Neural Information Processing

<!-- b000388 | references | pages [22] -->
Systems. Curran Associates Inc., Red Hook, NY, USA, Article 494, 5508-5518.

<!-- b000389 | references | pages [22] -->
[11] J. Stuart Hunter (1986) The Exponentially Weighted Moving Average, Journal of Quality Tech-

<!-- b000390 | references | pages [22] -->
nology, 18:4, 203-210, DOI: 10.1080/00224065.1986.11979014.

<!-- b000391 | references | pages [22] -->
[12] K. P. Sinaga and M. -S. Yang, ”Unsupervised K-Means Clustering Algorithm,” in IEEE Access,

<!-- b000392 | references | pages [22] -->
vol. 8, pp. 80716-80727, 2020, doi: 10.1109/ACCESS.2020.2988796.

<!-- b000393 | references | pages [22] -->
[13] Lim, Yong, and Sydney Parker. ”FIR filter design over a discrete powers-of-two coefficient space.”

<!-- b000394 | references | pages [22] -->
IEEE Transactions on Acoustics, Speech, and Signal Processing 31.3 (1983): 583-591.

<!-- b000395 | references | pages [22] -->
[14] Liu, X., Wang, X. & Matwin, S. Improving the interpretability of deep neural networks with knowl-

<!-- b000396 | references | pages [22] -->
edge distillation. in 2018 IEEE International Conference on Data Mining Workshops (ICDMW),

<!-- b000397 | references | pages [22] -->
905-912 (IEEE, 2018).

<!-- b000398 | references | pages [22] -->
[15] Marc´ılio, Wilson E., and Danilo M. Eler. ”From explanations to feature selection: assessing

<!-- b000399 | references | pages [22] -->
SHAP values as feature selection mechanism.” 2020 33rd SIBGRAPI conference on Graphics,

<!-- b000400 | references | pages [22] -->
Patterns and Images (SIBGRAPI). Ieee, 2020.

<!-- b000401 | furniture | pages [22] -->
关注数学模型

<!-- b000402 | furniture | pages [22] -->
2

<!-- b000403 | furniture | pages [22] -->
MATHmodels

<!-- b000404 | furniture | pages [22] -->
获取更多资讯

<!-- b000405 | furniture | pages [23] -->
Team 2406324

<!-- b000406 | furniture | pages [23] -->
Page 22 of 25

<!-- b000407 | references | pages [23] -->
[16] Mokhtari, Karim El, Ben Peachey Higdon, and Ays¸e Bas¸ar. ”Interpreting financial time series

<!-- b000408 | references | pages [23] -->
with SHAP values.” Proceedings of the 29th annual international conference on computer science

<!-- b000409 | references | pages [23] -->
and software engineering. 2019.

<!-- b000410 | references | pages [23] -->
微信公众号：数学模型

<!-- b000411 | references | pages [23] -->
[17] Qiu, Hai, et al. ”Wavelet filter-based weak signature detection method and its application on

<!-- b000412 | references | pages [23] -->
rolling element bearing prognostics.” Journal of sound and vibration 289.4-5 (2006): 1066-1090.

<!-- b000413 | references | pages [23] -->
[18] Saito, H., Yoshimura, H., Tanaka, K. et al. Predicting CKD progression using time-series cluster-

<!-- b000414 | references | pages [23] -->
ing and light gradient boosting machines. Sci Rep 14, 1723 (2024).

<!-- b000415 | references | pages [23] -->
[19] Silva, John M., Charles J. Hardy, and R. Kelly Crace. ”Analysis of psychological momentum in

<!-- b000416 | references | pages [23] -->
intercollegiate tennis.” Journal of sport and exercise psychology 10.3 (1988): 346-354.

<!-- b000417 | references | pages [23] -->
[20] Trad, Daniel O., and Jandyr M. Travassos. ”Wavelet filtering of magnetotelluric data.” Geophysics

<!-- b000418 | references | pages [23] -->
65.2 (2000): 482-491.

<!-- b000419 | references | pages [23] -->
[21] Theodorou, B., Xiao, C. & Sun, J. Synthesize high-dimensional longitudinal electronic health

<!-- b000420 | references | pages [23] -->
微信号：MATHmodels

<!-- b000421 | references | pages [23] -->
records via hierarchical autoregressive language model. Nat Commun 14, 5305 (2023).

<!-- b000422 | references | pages [23] -->
[22] Weinberg, Robert, and Allen Jackson. ”The Effects of Psychological Momentum on Male and

<!-- b000423 | references | pages [23] -->
Female Tennis Players Revisited.” Journal of Sport Behavior, vol. 12, no. 3, Sept. 1989, p. 167.

<!-- b000424 | references | pages [23] -->
[23] ”WTA Singles US Open.” LiveSport, n.d., https://www.livesport.com/en/tennis/wta-singles/us-

<!-- b000425 | references | pages [23] -->
open/.

<!-- b000426 | references | pages [23] -->
[24] Yin, Du, et al. ”Moving Average-Based Performance Enhancement of Sample Convolution and

<!-- b000427 | references | pages [23] -->
Interactive Learning for Short-Term Load Forecasting.” 2022 IEEE International Symposium on

<!-- b000428 | references | pages [23] -->
Product Compliance Engineering-Asia (ISPCE-ASIA). IEEE, 2022.

<!-- b000429 | references | pages [23] -->
[25] Yin, Lin, et al. ”Weighted median filters: a tutorial.” IEEE Transactions on circuits and systems

<!-- b000430 | references | pages [23] -->
II: analog and digital signal processing 43.3 (1996): 157-192.

<!-- b000431 | references | pages [23] -->
[26] Yu, Yan, et al. ”Abnormal data detection for multivariate alarm systems based on correlation

<!-- b000432 | references | pages [23] -->
directions.” Journal of Loss Prevention in the Process Industries 45 (2017): 43-55.

<!-- b000433 | furniture | pages [23] -->
关注数学模型

<!-- b000434 | furniture | pages [23] -->
2

<!-- b000435 | furniture | pages [23] -->
MATHmodels

<!-- b000436 | furniture | pages [23] -->
获取更多资讯

<!-- b000437 | furniture | pages [24] -->
Team 2406324

<!-- b000438 | furniture | pages [24] -->
Page 23 of 25

<!-- b000439 | heading | pages [24] -->
9 Appendices

<!-- b000440 | prose | pages [24] -->
1 import matplotlib.pyplot as plt 微信公众号：数学模型 2 import pandas as pd 3 import numpy as np 4 import math 5 from sklearn.preprocessing import MinMaxScaler 6 from sklearn.metrics import mean_squared_error 7 import preprocessing 8 import tensorflow as tf 9 from tensorflow.keras.layers import GRU, Dense,SimpleRNN ,LSTM 10 from tensorflow.keras.models import Sequential 11 import seaborn as sns 12 from transferdata import transferdata 13 np.random.seed(7) 14 transfer = 1 微信号：MATHmodels 15 transfer_option = 4 16 data = pd.read_csv(’2023-wimbledon -1301.csv’, usecols=list(range(5,50))) 17 dataset = data.to_numpy() 18 scaler = MinMaxScaler(feature_range=(0, 1)) 19 dataset[:,range(43)] = scaler.fit_transform(dataset[:,range(43)]) 20 train_number = int(len(dataset) * 0.7) 21 test_number = len(dataset) - train_number 22 train_original , test_original = dataset[0:train_number ,:], dataset[ train_number:len(dataset),:] 23 step_size = 6 24 trainX , trainY = preprocessing.new_dataset(train_original , step_size) 25 testX, testY = preprocessing.new_dataset(test_original , step_size) 26 #getting transfer trainX and trainY in similar ways 27 model = Sequential() 28 model.add(LSTM(32,input_shape=(step_size ,45), return_sequences=True)) 29 model.add(LSTM(32, return_sequences=True)) 30 model.add(LSTM(16)) 31 model.add(Dense(16, activation=’sigmoid’)) 32 model.add(Dense(2, activation=’sigmoid’)) 33 model.compile(loss=’mean_squared_error’, optimizer=’adam’) 34 if transfer == 1:

<!-- b000441 | prose | pages [24] -->
model.fit(trainX_transfer , trainY_transfer , epochs=60, batch_size=16, 35 verbose=2) 36 else:

<!-- b000442 | prose | pages [24] -->
model.fit(trainX , trainY , epochs=60, batch_size=4,verbose=2) 37

<!-- b000443 | prose | pages [24] -->
38 39 if transfer_option==1:

<!-- b000444 | prose | pages [24] -->
for layer in model.layers[:4]: 40 layer.trainable = False 41 model.fit(trainX , trainY , epochs=30, batch_size=4, verbose=2) 42 43 elif transfer_option==2:

<!-- b000445 | furniture | pages [24] -->
关注数学模型

<!-- b000446 | furniture | pages [24] -->
2

<!-- b000447 | furniture | pages [24] -->
MATHmodels

<!-- b000448 | furniture | pages [24] -->
获取更多资讯

<!-- b000449 | furniture | pages [25] -->
Team 2406324

<!-- b000450 | furniture | pages [25] -->
Page 24 of 25

<!-- b000451 | prose | pages [25] -->
for layer in model.layers[-3:]: 44 layer.trainable = False 45 model.fit(trainX , trainY , epochs=30, batch_size=4, verbose=2) 46 47 elif transfer_option==0 or transfer_option==3: 微信公众号：数学模型 model.fit(trainX , trainY , epochs=30, batch_size=4, verbose=2) 48 49 trainPredict = model.predict(trainX) 50 testPredict = model.predict(testX) 51 trainScore = math.sqrt(mean_squared_error(trainY, trainPredict)) 52 print(’Train RMSE: %.2f’ % (trainScore)) 53 testScore = math.sqrt(mean_squared_error(testY, testPredict)) 54 print(’Test RMSE: %.2f’ % (testScore)) 55 Real_Y_1 = np.vstack([trainY[:,0].reshape((-1,1)),testY[:,0].reshape ((-1,1))]) 56 Real_Y_2 = np.vstack([trainY[:,1].reshape((-1,1)),testY[:,1].reshape ((-1,1))]) 57 Predict_Y_1 = np.vstack([trainPredict[:,0].reshape((-1,1)),testPredict 微信号：MATHmodels [:,0].reshape((-1,1))]) 58 Predict_Y_2 = np.vstack([trainPredict[:,1].reshape((-1,1)),testPredict [:,1].reshape((-1,1))]) 59 x = np.arange(1, len(Real_Y_1) + 1, 1) 60 plt.plot(x, Real_Y_1 , label=’Real_momentum_1’) 61 plt.plot(x, Predict_Y_1 , label=’Predict_momentum_1’) 62 plt.title(’Real and predicted momentum for player 1(LSTM only with transfer learning)’) 63 plt.legend() 64 plt.show() 65 plt.plot(x, Real_Y_2 , label=’Real_momentum_2’) 66 plt.plot(x, Predict_Y_2 , label=’Predict_momentum_2’) 67 plt.title(’Real and predicted momentum for player 2(LSTM only with transfer learning)’) 68 plt.legend() 69 plt.show() 70 data_to_save = np.column_stack((Real_Y_1.flatten(), Real_Y_2.flatten(), Predict_Y_1.flatten(), Predict_Y_2.flatten())) 71 np.savetxt(’LSTM only with transfer learning.csv’, data_to_save , delimiter =’,’, header=’Real_Y_1 ,Real_Y_2 ,Predict_Y_1 ,Predict_Y_2’, comments=’’)

<!-- b000452 | prose | pages [25] -->
Listing 1: my Python code

<!-- b000453 | furniture | pages [25] -->
关注数学模型

<!-- b000454 | furniture | pages [25] -->
2

<!-- b000455 | furniture | pages [25] -->
MATHmodels

<!-- b000456 | furniture | pages [25] -->
获取更多资讯

<!-- b000457 | furniture | pages [26] -->
Team 2406324

<!-- b000458 | furniture | pages [26] -->
Page 25 of 25

<!-- b000459 | heading | pages [26] -->
10 Report on Use of AI

<!-- b000460 | ai_disclosure | pages [26] -->
•OpenAI ChatGPT(Nov 5, 2023 version, ChatGPT-4)

<!-- b000461 | ai_disclosure | pages [26] -->
◦Query1:PleasebrieflyexplainthecommonusagesandmaindifferencesbetweenRNN,GRU,LSTM.

<!-- b000462 | ai_disclosure | pages [26] -->
微信公众号：数学模型

<!-- b000463 | ai_disclosure | pages [26] -->
◦Output: Recurrent Neural Networks (RNN), Gated Recurrent Units (GRU), and Long Short-Term

<!-- b000464 | ai_disclosure | pages [26] -->
Memory (LSTM) networks are all types of neural networks designed to handle sequential data, such as

<!-- b000465 | ai_disclosure | pages [26] -->
time series data, natural language text, and audio. They are primarily used in tasks that involve temporal

<!-- b000466 | ai_disclosure | pages [26] -->
dependencies, where the order of the input data is crucial for making predictions or understanding

<!-- b000467 | ai_disclosure | pages [26] -->
context. Common Usages RNN: Used for modeling sequence data but has limitations in learning

<!-- b000468 | ai_disclosure | pages [26] -->
long-term dependencies due to the vanishing gradient problem. Commonly used in earlier applications

<!-- b000469 | ai_disclosure | pages [26] -->
of language modeling and text generation. GRU: Introduced as a simpler alternative to LSTM with

<!-- b000470 | ai_disclosure | pages [26] -->
fewer parameters. It is efficient in capturing dependencies for sequences of moderate length and is

<!-- b000471 | ai_disclosure | pages [26] -->
used in tasks like speech recognition, language modeling, and text generation. LSTM: Specifically

<!-- b000472 | ai_disclosure | pages [26] -->
designed to overcome the vanishing gradient problem of RNNs, making it capable of learning long-

<!-- b000473 | ai_disclosure | pages [26] -->
term dependencies. LSTMs are widely used in complex sequence modeling tasks, including machine

<!-- b000474 | ai_disclosure | pages [26] -->
微信号：MATHmodels

<!-- b000475 | ai_disclosure | pages [26] -->
translation, speech recognition, and time series prediction. Main Differences Complexity: LSTMs are

<!-- b000476 | ai_disclosure | pages [26] -->
more complex than GRUs, as they have three gates (input, output, forget) compared to GRU’s two

<!-- b000477 | ai_disclosure | pages [26] -->
gates (update and reset). RNNs are the simplest, with no gates, leading to their inability to capture

<!-- b000478 | ai_disclosure | pages [26] -->
long-term dependencies as effectively as GRU and LSTM. Memory Capability: LSTMs are best suited

<!-- b000479 | ai_disclosure | pages [26] -->
for applications requiring the understanding of long-term dependencies due to their complex gating

<!-- b000480 | ai_disclosure | pages [26] -->
mechanisms. GRUs are more efficient than LSTMs for shorter sequences but can still handle long-term

<!-- b000481 | ai_disclosure | pages [26] -->
dependencies better than RNNs. Training Time and Parameters: Due to their simplicity, RNNs have

<!-- b000482 | ai_disclosure | pages [26] -->
fewer parameters and thus are faster to train than GRUs and LSTMs. However, GRUs strike a balance

<!-- b000483 | ai_disclosure | pages [26] -->
between complexity and performance, often requiring less training time than LSTMs due to having

<!-- b000484 | ai_disclosure | pages [26] -->
fewer parameters, while still performing comparably on many tasks. Use Cases: The choice between

<!-- b000485 | ai_disclosure | pages [26] -->
RNN,

<!-- b000486 | ai_disclosure | pages [26] -->
•OpenAI ChatGPT(Nov 5, 2023 version, ChatGPT-4

<!-- b000487 | ai_disclosure | pages [26] -->
◦Query2:please list some weighted average filter algorithms to process oscillating data with noise

<!-- b000488 | ai_disclosure | pages [26] -->
◦Output: Weighted average filters are crucial for processing discrete oscillating data with noise,

<!-- b000489 | ai_disclosure | pages [26] -->
as they help in smoothing the data while preserving important trends and features. Here are several

<!-- b000490 | ai_disclosure | pages [26] -->
algorithms and approaches that incorporate weighted averages to achieve effective noise reduction

<!-- b000491 | ai_disclosure | pages [26] -->
and data smoothing: Moving Average Filter (Simple and Weighted): Simple Moving Average (SMA)

<!-- b000492 | ai_disclosure | pages [26] -->
computes the average of the data points within a sliding window that moves across the dataset. Each data

<!-- b000493 | ai_disclosure | pages [26] -->
point within the window has equal weight. Weighted Moving Average (WMA) assigns different weights

<!-- b000494 | ai_disclosure | pages [26] -->
to the data points within the window, typically giving more importance to more recent data points.

<!-- b000495 | ai_disclosure | pages [26] -->
Exponential Moving Average (EMA): It applies weighting factors that decrease exponentially for older

<!-- b000496 | ai_disclosure | pages [26] -->
data points, giving more significance to recent observations without discarding older data entirely. This

<!-- b000497 | ai_disclosure | pages [26] -->
is particularly useful for smoothing data while being responsive to recent changes. Gaussian Filter:

<!-- b000498 | ai_disclosure | pages [26] -->
Utilizes a Gaussian function to assign weights to data points within the window. The weights decrease

<!-- b000499 | ai_disclosure | pages [26] -->
as the distance from the center of the window increases, following a Gaussian distribution. This filter

<!-- b000500 | ai_disclosure | pages [26] -->
is effective in reducing noise while maintaining the shape of the signal waveform. Savitzky-Golay

<!-- b000501 | ai_disclosure | pages [26] -->
Filter: Fits successive sub-sets of adjacent data points with a low-degree polynomial by the method

<!-- b000502 | ai_disclosure | pages [26] -->
of least squares. This approach provides smoothing as well as differentiation, which can be useful in

<!-- b000503 | ai_disclosure | pages [26] -->
analyzing oscillating signals where rate of change is of interest. Kalman Filter: An adaptive filter that

<!-- b000504 | furniture | pages [26] -->
关注数学模型

<!-- b000505 | furniture | pages [26] -->
2

<!-- b000506 | furniture | pages [26] -->
MATHmodels

<!-- b000507 | furniture | pages [26] -->
获取更多资讯

<!-- b000508 | furniture | pages [27] -->
Team 2406324

<!-- b000509 | furniture | pages [27] -->
Page 26 of 25

<!-- b000510 | ai_disclosure | pages [27] -->
uses a series of measurements observed over time, containing statistical noise, and produces estimates

<!-- b000511 | ai_disclosure | pages [27] -->
of unknown variables. It can be used to apply a weighted average where the weights are calculated

<!-- b000512 | ai_disclosure | pages [27] -->
based on the estimation error covariance. It’s particularly suited for systems with dynamic changes and

<!-- b000513 | ai_disclosure | pages [27] -->
can effectively filter noise from signals in real-time. Adaptive Filters: These filters adjust the weighting

<!-- b000514 | ai_disclosure | pages [27] -->
微信公众号：数学模型

<!-- b000515 | ai_disclosure | pages [27] -->
mechanism based on the characte

<!-- b000516 | ai_disclosure | pages [27] -->
•Anthropic Claude2 (Feb , 2024 version)

<!-- b000517 | ai_disclosure | pages [27] -->
◦Query: Please read this file and summarize this article for me.

<!-- b000518 | ai_disclosure | pages [27] -->
Pay more attention to the

<!-- b000519 | ai_disclosure | pages [27] -->
methodology the author used and the conclusion they reached.

<!-- b000520 | ai_disclosure | pages [27] -->
◦Output: Here is a summary of the key points from the article: Methodology: The authors

<!-- b000521 | ai_disclosure | pages [27] -->
conducted a real-effort laboratory experiment with a counting task to study tournaments between teams

<!-- b000522 | ai_disclosure | pages [27] -->
and individuals. Subjects completed 3 parts: piece-rate, tournament without feedback, tournament

<!-- b000523 | ai_disclosure | pages [27] -->
with feedback. In the team treatment, subjects were matched into pairs based on performance and then

<!-- b000524 | ai_disclosure | pages [27] -->
randomly assigned to teams. In each round of the tournament, a random pair from each team competed.

<!-- b000525 | ai_disclosure | pages [27] -->
Feedback was provided between rounds during the third part of the experiment. Conclusions: In team

<!-- b000526 | ai_disclosure | pages [27] -->
tournaments, feedback did not affect performance - teams were equally likely to win whether they

<!-- b000527 | ai_disclosure | pages [27] -->
微信号：MATHmodels

<!-- b000528 | ai_disclosure | pages [27] -->
were leading or lagging. In individual tournaments, feedback had asymmetric effects - lagging players

<!-- b000529 | ai_disclosure | pages [27] -->
worked harder while leading players slacked off. The results support theoretical predictions for team

<!-- b000530 | ai_disclosure | pages [27] -->
tournaments but contradict predictions for individual tournaments.

<!-- b000531 | ai_disclosure | pages [27] -->
Potential explanations include

<!-- b000532 | ai_disclosure | pages [27] -->
utility of winning, belief updating, and reference-dependent goals. In summary, the study finds that

<!-- b000533 | ai_disclosure | pages [27] -->
progress feedback affects effort incentives differently in team vs individual tournaments, with lagging

<!-- b000534 | ai_disclosure | pages [27] -->
teams catching up in individual but not team contests. The asymmetric responses to feedback in

<!-- b000535 | ai_disclosure | pages [27] -->
individual tournaments contrast with theoretical predictions.

<!-- b000536 | furniture | pages [27] -->
关注数学模型

<!-- b000537 | furniture | pages [27] -->
2

<!-- b000538 | furniture | pages [27] -->
MATHmodels

<!-- b000539 | furniture | pages [27] -->
获取更多资讯
