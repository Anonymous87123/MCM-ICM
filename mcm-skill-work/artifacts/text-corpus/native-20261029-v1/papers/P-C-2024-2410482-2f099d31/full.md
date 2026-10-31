# P-C-2024-2410482-2f099d31

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
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
2410482

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | heading | pages [1] -->
SUMMARY

<!-- b000009 | prose | pages [1] -->
Y

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
Players and spectators often wonder"what’s going on"during the match due to the incredible

<!-- b000012 | prose | pages [1] -->
swings, which are commonly attributed to momentum. Momentum is not about technique; instead,

<!-- b000013 | prose | pages [1] -->
it covers the real problems that tennis players face. Therefore, momentum is the hidden force that

<!-- b000014 | prose | pages [1] -->
controls the flow of the match.

<!-- b000015 | prose | pages [1] -->
For task 1, first, we decompose the match flow into two distinct indicators: winning probability

<!-- b000016 | prose | pages [1] -->
and momentum—the former indicating match situation favorability, the latter control over game

<!-- b000017 | prose | pages [1] -->
dynamics.Subsequently, utilizing the Markov Model for winning probability calculations, we

<!-- b000018 | prose | pages [1] -->
estimated win chances using conditional probabilities. Crucially, we rigorously defined the abstract

<!-- b000019 | prose | pages [1] -->
concept of momentum, incorporating the significance variance of individual points, and identifying

<!-- b000020 | title | pages [1] -->
微信号：MATHmodels

<!-- b000021 | prose | pages [1] -->
closely related factors.

<!-- b000022 | prose | pages [1] -->
For task 2, We translate randomness into the question of whether momentum effects are

<!-- b000023 | prose | pages [1] -->
significant.Utilizing hypothesis testing and logistic regression, we find momentum significantly

<!-- b000024 | prose | pages [1] -->
correlated with player performance, evidenced by a t-statistic for momentum yielding a p-value

<!-- b000025 | prose | pages [1] -->
well below 0.05 and a 95% confidence interval for the coefficient that excludes zero.

<!-- b000026 | prose | pages [1] -->
For task 3, Employing State Space Model and Kalman Filter, our model not only forecasts

<!-- b000027 | prose | pages [1] -->
springs in momentum with superior accuracy compared to the ARIMAR model but also offers en-

<!-- b000028 | prose | pages [1] -->
hanced mathematical interpretability over machine learning algorithms, demonstrating exceptional

<!-- b000029 | prose | pages [1] -->
predictive outcomes in our final assessment.Based on this, we analyze factors related to momentum

<!-- b000030 | prose | pages [1] -->
swings and provide corresponding recommendations.

<!-- b000031 | prose | pages [1] -->
For task 4, to evaluate the universality of our model, we selected a women’s tennis match

<!-- b000032 | prose | pages [1] -->
and a women’s table tennis match for analysis, achieving a low MSE of 0.051 in women’s tennis

<!-- b000033 | prose | pages [1] -->
predictions.Upon examining inaccuracies in both cases, we identified that enhancing the model’s

<!-- b000034 | prose | pages [1] -->
depiction of non-linearity will be an important direction for future improvements.

<!-- b000035 | prose | pages [1] -->
We also conduct sensitivity analysis, which shows how different samples affect the word state

<!-- b000036 | prose | pages [1] -->
space model.And then the strengths and weaknesses of our model are summarized.Finally, a memo

<!-- b000037 | prose | pages [1] -->
to coaches presenting the overall ideas and results about momentum is written at the end of the

<!-- b000038 | prose | pages [1] -->
paper.

<!-- b000039 | keywords | pages [1] -->
Keywords:Momentum;Markov Chain;Hypothesis testing;State Space Model;Kalman Filter Al-

<!-- b000040 | prose | pages [1] -->
gorithm

<!-- b000041 | furniture | pages [1] -->
关注数学模型

<!-- b000042 | furniture | pages [1] -->
2

<!-- b000043 | furniture | pages [1] -->
MATHmodels

<!-- b000044 | furniture | pages [1] -->
获取更多资讯

<!-- b000045 | prose | pages [2] -->
CONTENT

<!-- b000046 | prose | pages [2] -->
1

<!-- b000047 | heading | pages [2] -->
Introduction

<!-- b000048 | prose | pages [2] -->
2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2

<!-- b000049 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000050 | prose | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 3 Data Resource . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000051 | prose | pages [2] -->
2

<!-- b000052 | heading | pages [2] -->
Assumptions and Justifications

<!-- b000053 | prose | pages [2] -->
3

<!-- b000054 | heading | pages [2] -->
Notation

<!-- b000055 | prose | pages [2] -->
3

<!-- b000056 | prose | pages [2] -->
3

<!-- b000057 | prose | pages [2] -->
4

<!-- b000058 | prose | pages [2] -->
4 Assessing Player Performance within Match Flow 4 Model I:Markov Model to Predict Win Probabilities . . . . . . . . . . . . . . . . . . . 4.1 5 Explanation of the Serving Scoring 4.1.1 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | prose | pages [2] -->
5 Establishment and Predictive Outcomes of the Markov Model 4.1.2 . . . . . . . . .

<!-- b000060 | prose | pages [2] -->
5

<!-- b000061 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000062 | prose | pages [2] -->
Searching for the Defination of Momentum 4.2 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | prose | pages [2] -->
7 How to Quantify Momentum? . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 7 The Defination of Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 9

<!-- b000064 | prose | pages [2] -->
10 Is It Random? Measuring the Significance of Momentum Effecs 5 Analysis and Methodology Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 10 Parameter Estimation: Based on MLE . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 11 . . . . . . . . . . . . . . . . . . . The Result of Regression and Hypothesis Testing 5.3 12

<!-- b000065 | heading | pages [2] -->
Momentum Projections,Influencing Factors and Recommendations

<!-- b000066 | prose | pages [2] -->
6 13 Prediction of the Momentum and Swings 6.1 . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | prose | pages [2] -->
13 Introduction to State Space Model and Kalman Filter Algorithm . . . . . . . . 6.1.1 13 Building Predictive Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.2 6.1.3 Prediction Results and Analysis 15 . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | prose | pages [2] -->
16 Model Evaluation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.4 17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 Correlation Analysis 17 Suggestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 18 Suggestions for Players with Strong Momentum . . . . . . . . . . . . . . . . . 6.3.1 19 Suggestions for Relatively Stable Momentum . . . . . . . . . . . . . . . . . . 6.3.2 19

<!-- b000069 | prose | pages [2] -->
Extension Test ——In Women’s Tennis and Table Tennis Matches 7 7.1 Scenario of Women’s Tennis Matches 19 . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | prose | pages [2] -->
20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Scenario of Table Tennis Matches

<!-- b000071 | prose | pages [2] -->
8

<!-- b000072 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000073 | prose | pages [2] -->
9

<!-- b000074 | heading | pages [2] -->
Strengths and Weakness

<!-- b000075 | prose | pages [2] -->
21

<!-- b000076 | prose | pages [2] -->
22

<!-- b000077 | prose | pages [2] -->
23

<!-- b000078 | furniture | pages [2] -->
关注数学模型

<!-- b000079 | furniture | pages [2] -->
1

<!-- b000080 | furniture | pages [2] -->
2

<!-- b000081 | furniture | pages [2] -->
MATHmodels

<!-- b000082 | furniture | pages [2] -->
获取更多资讯

<!-- b000083 | furniture | pages [3] -->
Team 2410482

<!-- b000084 | prose | pages [3] -->
1

<!-- b000085 | heading | pages [3] -->
Introduction

<!-- b000086 | prose | pages [3] -->
1.1

<!-- b000087 | heading | pages [3] -->
Background

<!-- b000088 | furniture | pages [3] -->
Page 2

<!-- b000089 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000090 | prose | pages [3] -->
In the evolving landscape of sports, technological advancements have greatly enhanced the analysis

<!-- b000091 | prose | pages [3] -->
of athletes’ performances, focusing primarily on outcomes like scores. However, this approach often

<!-- b000092 | prose | pages [3] -->
overlooks the analysis of a player’s in-game state.

<!-- b000093 | prose | pages [3] -->
To improve predictions of scoring trends and

<!-- b000094 | prose | pages [3] -->
devise effective strategies, it’s crucial to study a player’s "momentum". Momentum, a psychological

<!-- b000095 | prose | pages [3] -->
edge gained through consecutive wins, can significantly affect an opponent’s confidence and play.

<!-- b000096 | prose | pages [3] -->
Understanding and leveraging momentum is vital for success in tennis and other sports, as it influences

<!-- b000097 | prose | pages [3] -->
a player’s confidence, aggression, and overall performance.

<!-- b000098 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000099 | prose | pages [3] -->
1.2

<!-- b000100 | heading | pages [3] -->
Problem Restatement

<!-- b000101 | prose | pages [3] -->
Considering the background information and restricted conditions identified in the problem state-

<!-- b000102 | prose | pages [3] -->
ment, we need to solve the following problems:

<!-- b000103 | prose | pages [3] -->
• Create a model using data from the 2023 Wimbledon men’s matches to analyze the dynamics

<!-- b000104 | prose | pages [3] -->
of match play, identify the leading player at any moment, and quantify their performance advantage.

<!-- b000105 | prose | pages [3] -->
Additionally, visualize match flows to illustrate our findings, applying this model to selected matches.

<!-- b000106 | prose | pages [3] -->
• Evaluate the validity of momentum in tennis, examining whether patterns of success or shifts in

<!-- b000107 | prose | pages [3] -->
play are random or influenced by momentum.

<!-- b000108 | prose | pages [3] -->
• Develop a predictive model based on match data to identify factors influencing play dynamics

<!-- b000109 | prose | pages [3] -->
and suggest strategies for players entering new matches, considering previous momentum shifts.

<!-- b000110 | prose | pages [3] -->
• Assess the model’s performance across different matches, pinpoint necessary enhancements,

<!-- b000111 | prose | pages [3] -->
and evaluate its suitability for other analytical endeavors.

<!-- b000112 | prose | pages [3] -->
• Summarize the findings in a concise two-page memo, providing coaching advice on utilizing

<!-- b000113 | prose | pages [3] -->
momentum and preparing for events affecting match dynamics.

<!-- b000114 | furniture | pages [3] -->
关注数学模型

<!-- b000115 | furniture | pages [3] -->
2

<!-- b000116 | furniture | pages [3] -->
MATHmodels

<!-- b000117 | furniture | pages [3] -->
获取更多资讯

<!-- b000118 | furniture | pages [4] -->
Team 2410482

<!-- b000119 | prose | pages [4] -->
1.3 Our Work

<!-- b000120 | furniture | pages [4] -->
Page 3

<!-- b000121 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000122 | caption | pages [4] -->
Figure 1: Our Work

<!-- b000123 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000124 | prose | pages [4] -->
1.4 Data Resource

<!-- b000125 | prose | pages [4] -->
Match

<!-- b000126 | prose | pages [4] -->
Woman’s tennis match Table tennis match

<!-- b000127 | prose | pages [4] -->
Website

<!-- b000128 | prose | pages [4] -->
https://www.wimbledon.com/ https://www.kaggle.com/datasets

<!-- b000129 | heading | pages [4] -->
Assumptions and Justifications

<!-- b000130 | prose | pages [4] -->
2

<!-- b000131 | prose | pages [4] -->
To simplify our modeling, we make the following assumptions:

<!-- b000132 | heading | pages [4] -->
Assumption 1:Recent performance is indicative of future performance

<!-- b000133 | prose | pages [4] -->
Justification:This means that if an athlete has performed well in their most recent competition

<!-- b000134 | prose | pages [4] -->
there is a higher likelihood that they will continue to perform well in their next competition.

<!-- b000135 | heading | pages [4] -->
Assumption 2:Stability of physical state

<!-- b000136 | prose | pages [4] -->
Justification:It is assumed that athletes’ fitness status isrelatively stable in the short term, such

<!-- b000137 | prose | pages [4] -->
that strengths or weaknesses in fitness will continue to affecttheir performance in the following

<!-- b000138 | prose | pages [4] -->
competitions.

<!-- b000139 | heading | pages [4] -->
Assumption 3:Our model has Markov Property

<!-- b000140 | prose | pages [4] -->
Justification: the next state depends only on the current state and is independent of earlier states.

<!-- b000141 | furniture | pages [4] -->
关注数学模型

<!-- b000142 | furniture | pages [4] -->
2

<!-- b000143 | furniture | pages [4] -->
MATHmodels

<!-- b000144 | furniture | pages [4] -->
获取更多资讯

<!-- b000145 | furniture | pages [5] -->
Team 2410482

<!-- b000146 | prose | pages [5] -->
3

<!-- b000147 | heading | pages [5] -->
Notation

<!-- b000148 | prose | pages [5] -->
Symbol

<!-- b000149 | furniture | pages [5] -->
Page 4

<!-- b000150 | prose | pages [5] -->
Explaination

<!-- b000151 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000152 | prose | pages [5] -->
𝑝𝐴𝐵 A’s service score rate when A has a match with B 𝑞𝐴𝐵 A’s receive points score rate when A has a match with B 𝐿 𝑀 𝜔 𝛽 𝑊 The leberage of a game The value of momentum the coefficient to measure momentum the coefficient of logistic regression equation the swings of winning probability The corresponding variances of 𝑀𝑡conditional on information at time t-1 Σ𝑡|𝑡−1

<!-- b000153 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000154 | prose | pages [5] -->
Task 1: Assessing Player Performance within Match Flow 4

<!-- b000155 | prose | pages [5] -->
For play’s performance at a given time, we measure it from two different angles——winning

<!-- b000156 | prose | pages [5] -->
rate and momentum.The winning rate excludes any psychological factors, outside factors, and strictly

<!-- b000157 | prose | pages [5] -->
introduces the advantages and disadvantages of the situation from a mathematical point of view

<!-- b000158 | prose | pages [5] -->
according to the ability of both sides, while momentum shows the player’s ability to control the

<!-- b000159 | prose | pages [5] -->
situation on the field.

<!-- b000160 | caption | pages [5] -->
Figure 2: relationship between player performance and winning percentage & momentum

<!-- b000161 | furniture | pages [5] -->
关注数学模型

<!-- b000162 | furniture | pages [5] -->
2

<!-- b000163 | furniture | pages [5] -->
MATHmodels

<!-- b000164 | furniture | pages [5] -->
获取更多资讯

<!-- b000165 | furniture | pages [6] -->
Team 2410482

<!-- b000166 | furniture | pages [6] -->
Page 5

<!-- b000167 | heading | pages [6] -->
Model I:Markov Model to Predict Win Probabilities

<!-- b000168 | prose | pages [6] -->
4.1

<!-- b000169 | prose | pages [6] -->
4.1.1 Explanation of the Serving Scoring

<!-- b000170 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000171 | prose | pages [6] -->
Considering that there is A big difference in the scoring rate between the receiving side and the

<!-- b000172 | prose | pages [6] -->
serving side in tennis match, we cannot use the same scoring rate to measure the serving and receiving

<!-- b000173 | prose | pages [6] -->
situations. Instead, we use two different symbols 𝑝𝐴𝐵, 𝑞𝐴𝐵to measure the serving and receiving scoring

<!-- b000174 | prose | pages [6] -->
rate of A in the match between A and B respectively.

<!-- b000175 | prose | pages [6] -->
In the match between A and B, A’s service scoring rate 𝑝𝐴𝐵is related to A’s service level and B’s

<!-- b000176 | prose | pages [6] -->
service receiving level, which can be defined by the mean of A’s career average service scoring rate

<!-- b000177 | prose | pages [6] -->
𝑝𝐴𝐵and B’s career average service scoring rate 𝑞𝐵can i.e. :

<!-- b000178 | prose | pages [6] -->
𝑝𝐴𝐵= 𝑝𝐴+ 𝑞𝐵

<!-- b000179 | prose | pages [6] -->
+ 𝑒 (1) 2

<!-- b000180 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000181 | prose | pages [6] -->
e is the amendment item, which is changed according to the different situations of the two sides.

<!-- b000182 | prose | pages [6] -->
In the same way:

<!-- b000183 | prose | pages [6] -->
𝑞𝐴𝐵= 𝑞𝐴+ 𝑝𝐵

<!-- b000184 | prose | pages [6] -->
+ 𝑒 (2) 2

<!-- b000185 | heading | pages [6] -->
Establishment and Predictive Outcomes of the Markov Model

<!-- b000186 | prose | pages [6] -->
4.1.2

<!-- b000187 | prose | pages [6] -->
To calculate the probability of winning at a certain moment, we introduce The Markov Model.

<!-- b000188 | prose | pages [6] -->
In processes where future outcomes depend solely on the current state and not on past con-

<!-- b000189 | prose | pages [6] -->
ditions, such as tennis matches, the calculation of winning probabilities considers only the current

<!-- b000190 | prose | pages [6] -->
score. Psychological and external factors are excluded, making the win probability directly tied to the

<!-- b000191 | prose | pages [6] -->
present score. This scenario is suitable for analysis using Markov chains, which facilitate probability

<!-- b000192 | prose | pages [6] -->
calculations through event transformation relationships. An example application is computing the win

<!-- b000193 | prose | pages [6] -->
probability in a tennis match based on specific scores, illustrated by the following flow chart:

<!-- b000194 | caption | pages [6] -->
Figure 3: the flow chart of the Markov Model

<!-- b000195 | furniture | pages [6] -->
关注数学模型

<!-- b000196 | furniture | pages [6] -->
2

<!-- b000197 | furniture | pages [6] -->
MATHmodels

<!-- b000198 | furniture | pages [6] -->
获取更多资讯

<!-- b000199 | furniture | pages [7] -->
Team 2410482

<!-- b000200 | furniture | pages [7] -->
Page 6

<!-- b000201 | prose | pages [7] -->
The scores of A and B in the ongoing match are (𝑎, 𝑏), the ranges of which are shown in the

<!-- b000202 | prose | pages [7] -->
following table:

<!-- b000203 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000204 | prose | pages [7] -->
0 1 2 2 3 4 5 (2,0) 0 (0,0) (1,0) (3,0) (4,0) none (2,1) 1 (0,1) (1,1) (3,1) (4,1) none (2,2) 2 (0,2) (1,2) (3,2) (4,2) none (2,3) 3 (0,3) (1,3) (3,3) (4,3) (5,3) (2,4) 4 (0,4) (1,4) (3,4) (4,4) none none 5 none none (3,5) none none

<!-- b000205 | prose | pages [7] -->
1,2, and 3 in the table above represent the actual score of 15,30,and 40 respectively.(4,3),(3,4) respec-

<!-- b000206 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000207 | prose | pages [7] -->
tively represent the two sides scored AD, while special scores (4,4),(5,3) represent the equalizer and

<!-- b000208 | prose | pages [7] -->
another goal after AD to win the game. In particular , the actual probability of winning the game after

<!-- b000209 | prose | pages [7] -->
(4,3) and (3,4) is the same as (3,2) and (2,3) and the probability of winning the game after (3,3) and

<!-- b000210 | prose | pages [7] -->
(4,4) is the same as (2,2). What’s more, the case which scores one more point after (4,3) to get (5,3)

<!-- b000211 | prose | pages [7] -->
and wins the game is equivalent to the case which scores one more point after (3,2) to get (4,2) and

<!-- b000212 | prose | pages [7] -->
win the game. Therefore, although in the table lists there are special score (3, 4), (4, 3), (3, 3), (3, 3),

<!-- b000213 | prose | pages [7] -->
(5, 3), (4, 4) , these six special cases do not appear in the Markov model flow chart.

<!-- b000214 | prose | pages [7] -->
On the basis of the above descriptions, the following formulas can be listed according to Markov

<!-- b000215 | prose | pages [7] -->
model and conditional probability formula:

<!-- b000216 | prose | pages [7] -->
𝑃(𝑎, 𝑏) = 𝑝∗𝑃(𝑎+ 1, 𝑏) + (1 −𝑝) ∗𝑃(𝑎, 𝑏+ 1) (3)

<!-- b000217 | prose | pages [7] -->
P(a,b) in the formula above represents the probability of winning the game under the score (a,b),

<!-- b000218 | prose | pages [7] -->
and p represents the probability of winning a ball (varies according to the server). According to the

<!-- b000219 | prose | pages [7] -->
above formula, the probability of winning the game under any score can be obtained by backward

<!-- b000220 | prose | pages [7] -->
recursion.

<!-- b000221 | prose | pages [7] -->
Similarly, the Markov model can be used to find the probability of winning the whole game at any

<!-- b000222 | prose | pages [7] -->
score. This probability can be used to measure the advantages and disadvantages on the tennis court.

<!-- b000223 | prose | pages [7] -->
Based on the given data of the 2023 Wimbledon Gentlemen’s final and the data of career average

<!-- b000224 | prose | pages [7] -->
serving point rate and receiving point rate of Carlos Alcaraz and Novak Djokovic, we used the Markov

<!-- b000225 | prose | pages [7] -->
model to calculate the winning rate of both players at every moment on the court, as shown in the figure

<!-- b000226 | prose | pages [7] -->
below:

<!-- b000227 | furniture | pages [7] -->
关注数学模型

<!-- b000228 | furniture | pages [7] -->
2

<!-- b000229 | furniture | pages [7] -->
MATHmodels

<!-- b000230 | furniture | pages [7] -->
获取更多资讯

<!-- b000231 | furniture | pages [8] -->
Team 2410482

<!-- b000232 | furniture | pages [8] -->
Page 7

<!-- b000233 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000234 | caption | pages [8] -->
Figure 4: 2023 Wimbledon Gentlemen’s singles final winning final chart

<!-- b000235 | prose | pages [8] -->
As can be seen from the picture, the match experienced ups and downs. Novak Djokovic occupied

<!-- b000236 | prose | pages [8] -->
the advantage of the match during 1-21 games, but after 21 games, the wind changed and Carlos Alcaraz,

<!-- b000237 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000238 | prose | pages [8] -->
who had been lagging behind, gained the initiative. However, after Novak Djokovic’s tenacious chase,

<!-- b000239 | prose | pages [8] -->
the two sides were almost back on the same starting line in the 38th game, and at last Carlos Alcaraz

<!-- b000240 | prose | pages [8] -->
again took the fight to the win. The result of accurate probability calculation is also consistent with

<!-- b000241 | prose | pages [8] -->
people’s intuitive perception of the game, so it can be seen that the winning rate chart can reflect the

<!-- b000242 | prose | pages [8] -->
situation on the field to a large extent.

<!-- b000243 | prose | pages [8] -->
Searching for the Defination of Momentum 4.2

<!-- b000244 | prose | pages [8] -->
4.2.1 How to Quantify Momentum?

<!-- b000245 | prose | pages [8] -->
In the dictionary, one definition of momentum is "strength or force gained by motion or by a series

<!-- b000246 | prose | pages [8] -->
of events". In sports, we can always clearly feel the momentum of the team that has scored consecutive

<!-- b000247 | prose | pages [8] -->
points, which will produce a mysterious force to make it full of motivation. However, when we talk

<!-- b000248 | prose | pages [8] -->
about momentum, we are more of an abstract understanding of things. In order to make the data of

<!-- b000249 | prose | pages [8] -->
game play a bigger role, our job is to quantify momentum. First, we must consider what momentum is

<!-- b000250 | prose | pages [8] -->
associated with.

<!-- b000251 | prose | pages [8] -->
• Scores Consecutive Points

<!-- b000252 | prose | pages [8] -->
In sports games, often the side that scores consecutive points will gain momentum and gain a

<!-- b000253 | prose | pages [8] -->
psychological lead in the game.

<!-- b000254 | prose | pages [8] -->
We use the number of scoring consecutive points to show the degree of scoring consecutive points.

<!-- b000255 | prose | pages [8] -->
If the opponent scores consecutive points, the index of scoring consecutive points is the opposite number

<!-- b000256 | prose | pages [8] -->
of consecutive points of the opponent. However, the influence of the number of scoring consecutive

<!-- b000257 | prose | pages [8] -->
scores on the momentum should not be proportional, because there is a law of ”diminishing marginal

<!-- b000258 | prose | pages [8] -->
utility” in economics, which indicates that the increment of consumer satisfaction shows a decreasing

<!-- b000259 | furniture | pages [8] -->
关注数学模型

<!-- b000260 | furniture | pages [8] -->
2

<!-- b000261 | furniture | pages [8] -->
MATHmodels

<!-- b000262 | furniture | pages [8] -->
获取更多资讯

<!-- b000263 | furniture | pages [9] -->
Team 2410482

<!-- b000264 | furniture | pages [9] -->
Page 8

<!-- b000265 | prose | pages [9] -->
law with the increase of consumption quantity. Therefore, we measure the effect of scoring consecutive

<!-- b000266 | prose | pages [9] -->
2 −𝑒−𝑥 𝑥 2) = 𝑒

<!-- b000267 | prose | pages [9] -->
points on momentum by applying the odd function𝑣= 𝑓(𝑥) = 𝑡𝑎𝑛ℎ( 𝑥

<!-- b000268 | prose | pages [9] -->
decreases and converges to 0 at 𝑥> 0.

<!-- b000269 | prose | pages [9] -->
2

<!-- b000270 | prose | pages [9] -->
2 whose derivative 2 +𝑒−𝑥 𝑥

<!-- b000271 | prose | pages [9] -->
𝑒

<!-- b000272 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000273 | prose | pages [9] -->
• The Number of Consecutive Win of Games and The Importance of Each Game

<!-- b000274 | prose | pages [9] -->
In addition to scoring consecutive points, winning consecutive games also greatly increases

<!-- b000275 | prose | pages [9] -->
momentum, and the more crucial the games win, the greater the momentum increases.

<!-- b000276 | prose | pages [9] -->
To measure the importance of each game, we defined a new metric called "Leberage".In ordert

<!-- b000277 | prose | pages [9] -->
o better illustrate Leberage’s definition, I will give an example before giving the formula:

<!-- b000278 | prose | pages [9] -->
A tennis match of two players A and B is going to the key moment to decide the outcome which

<!-- b000279 | prose | pages [9] -->
means the set points of both sides are tied 2:2 and the game points are also 6:6 into the tiebreak. At

<!-- b000280 | prose | pages [9] -->
this time, the player who wins the game will get the victory. In other words, if A wins the game, A’s

<!-- b000281 | prose | pages [9] -->
probability of winning the match will become 1, and if A loses the game, A’s probability of winning the

<!-- b000282 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000283 | prose | pages [9] -->
match will become 0. So, the outcome of this game will make the change of the winning probability

<!-- b000284 | prose | pages [9] -->
up to 100%.

<!-- b000285 | prose | pages [9] -->
Think about another scenario, the tennis match just started, the two sides launched the first set of

<!-- b000286 | prose | pages [9] -->
the game, if A wins, the winning rate of the game increases from 0.5 to 0.6, if A loses, the winning rate

<!-- b000287 | prose | pages [9] -->
of the game is only reduced to 0.4, and there is still a great chance to reverse the game. The influence of

<!-- b000288 | prose | pages [9] -->
this game on the winning rate is only 0.6-0.4=0.2. In other words, Leberage can be defined as "winning

<!-- b000289 | prose | pages [9] -->
rate difference". Here is Leberage 𝐿𝑎for 𝑔𝑎𝑚𝑒𝑎:

<!-- b000290 | prose | pages [9] -->
𝐿𝑎= 𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑤𝑖𝑛𝑔𝑎𝑚𝑒𝑎) −𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑙𝑜𝑠𝑠𝑔𝑎𝑚𝑒𝑎) (4)

<!-- b000291 | prose | pages [9] -->
𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑤𝑖𝑛𝑔𝑎𝑚𝑒𝑎) and 𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑙𝑜𝑠𝑠𝑔𝑎𝑚𝑒𝑎) in the formula above represent

<!-- b000292 | prose | pages [9] -->
the conditional probability of winning the match under the condition of winning and losing the game

<!-- b000293 | prose | pages [9] -->
The introduction of Markov Model in the previous chapter provides a shortcut for respectively.

<!-- b000294 | prose | pages [9] -->
calculating conditional probability.

<!-- b000295 | prose | pages [9] -->
After defining leberage, we can measure momentum by combining two metrics consecutive wins

<!-- b000296 | prose | pages [9] -->
and the importance of different games together. Considering that sets closer to the current time have

<!-- b000297 | prose | pages [9] -->
more influence on the current momentum, we weighted Leberage exponentially to get the following

<!-- b000298 | prose | pages [9] -->
indicator 𝑢𝑡:

<!-- b000299 | prose | pages [9] -->
𝑢𝑡= 𝐿𝑡−1(−1)𝑟𝑡−1 + (1 −𝛼)𝐿𝑡−2(−1)𝑟𝑡−2 + (1 −𝛼)2𝐿𝑡−3(−1)𝑟𝑡−3 + ...... + (1 −𝛼)𝑡−2𝐿1

<!-- b000300 | prose | pages [9] -->
(5) 1 + (1 −𝛼) + (1 −𝛼)2 + ...... + (1 −𝛼)𝑡−2

<!-- b000301 | prose | pages [9] -->
𝐿𝑡indicates the Leberage corresponding to set t. 𝑟𝑡represents victory in set t and is a 0-1 variable

<!-- b000302 | furniture | pages [9] -->
关注数学模型

<!-- b000303 | furniture | pages [9] -->
2

<!-- b000304 | furniture | pages [9] -->
MATHmodels

<!-- b000305 | furniture | pages [9] -->
获取更多资讯

<!-- b000306 | furniture | pages [10] -->
Team 2410482

<!-- b000307 | furniture | pages [10] -->
Page 9

<!-- b000308 | prose | pages [10] -->
, which means that 0 is taken if set t won and 1 is taken if set t lost. In addition, 𝛼is the corresponding

<!-- b000309 | prose | pages [10] -->
coefficient of Lerberage, and the change of its value affects the weight of Lerberage at different times.

<!-- b000310 | prose | pages [10] -->
For ease of calculation, in this article 𝛼is always the constant value 0.33.

<!-- b000311 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000312 | prose | pages [10] -->
In fact, the rise of momentum is not just a short-term trend across a few balls, but also a long-term

<!-- b000313 | prose | pages [10] -->
trend across a few sets or even a few matches. This is also well reflected in our factor considerations,

<!-- b000314 | prose | pages [10] -->
where consecutive points determine the short-term trend of momentum, and consecutive wins determine

<!-- b000315 | prose | pages [10] -->
the long-term trend of momentum.

<!-- b000316 | prose | pages [10] -->
• Other Factors

<!-- b000317 | prose | pages [10] -->
There are other factors that affect momentum.The variables include:

<!-- b000318 | prose | pages [10] -->
1.Presence of unforced errors in the previous point (x), with values 0,1,-1.Where 0 indicates no

<!-- b000319 | prose | pages [10] -->
unforced errors by either player, 1 signifies an unforced error by the player, and -1 denotes an unforced

<!-- b000320 | prose | pages [10] -->
error by the opponent.

<!-- b000321 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000322 | prose | pages [10] -->
2.Occurrence of a winner in the previous point (y), with a value range of 0,1,-1, adopting the

<!-- b000323 | prose | pages [10] -->
same valuation method.

<!-- b000324 | prose | pages [10] -->
3.The current point being a game, set, or match point (z), with values 0,1,-1, using the same

<!-- b000325 | prose | pages [10] -->
valuation approach.

<!-- b000326 | prose | pages [10] -->
The given data also contains many other factors, such as running distance, serving speed, etc.,

<!-- b000327 | prose | pages [10] -->
although they will also affect the situation and affect the trend of the score, they can not directly affect

<!-- b000328 | prose | pages [10] -->
the momentum from the perspective of the players, so they are no longer considered here.

<!-- b000329 | prose | pages [10] -->
4.2.2 The Defination of Momentum

<!-- b000330 | prose | pages [10] -->
According to the five important factors we have listed, momentum is defined using a linear model,

<!-- b000331 | prose | pages [10] -->
and the magnitude of momentum is represented by M, then:

<!-- b000332 | prose | pages [10] -->
𝑀𝑛= 𝜔𝑋𝑇+ 𝜀 (6)

<!-- b000333 | prose | pages [10] -->
𝜔isparameter matrix，namely𝜔= [𝜔1, 𝜔2, 𝜔3, 𝜔4, 𝜔5]，Xisfactormatrix,namely X=

<!-- b000334 | prose | pages [10] -->
𝑢∗

<!-- b000335 | prose | pages [10] -->
𝑛, 𝑣∗

<!-- b000336 | prose | pages [10] -->
𝑛, 𝑥∗

<!-- b000337 | prose | pages [10] -->
𝑛, 𝑦∗

<!-- b000338 | prose | pages [10] -->
𝑛, 𝑧∗

<!-- b000339 | prose | pages [10] -->


<!-- b000340 | prose | pages [10] -->


<!-- b000341 | prose | pages [10] -->
,

<!-- b000342 | prose | pages [10] -->
𝑛

<!-- b000343 | prose | pages [10] -->
𝑛represent the result of standardization on the corresponding value of 𝑢, 𝑥, 𝑦, 𝑧and their

<!-- b000344 | prose | pages [10] -->
𝑣∗

<!-- b000345 | prose | pages [10] -->
𝑛, 𝑥∗

<!-- b000346 | prose | pages [10] -->
𝑛, 𝑦∗

<!-- b000347 | prose | pages [10] -->
𝑛, 𝑧∗

<!-- b000348 | prose | pages [10] -->
corresponding sequence at the n point,𝑢∗

<!-- b000349 | prose | pages [10] -->
𝑛represents the result of standardization on the corresponding

<!-- b000350 | prose | pages [10] -->
value of u and its corresponding sequence at the n point. 𝜀is a disturbing factor, which will change

<!-- b000351 | prose | pages [10] -->
with the changes of athletes’ condition on the court, weather conditions and other objective factors.

<!-- b000352 | prose | pages [10] -->
Here, we assume that it follows the normal distribution with the mean value of 0 and standard deviation

<!-- b000353 | prose | pages [10] -->
of 𝜎,that is 𝜀∼𝑁(0, 𝜎2).

<!-- b000354 | prose | pages [10] -->
After comprehensively evaluating the influence of five factors on momentum, we set 𝜔=

<!-- b000355 | prose | pages [10] -->
[0.5, 0.2, 0, 1, −0.1, 0.1].

<!-- b000356 | furniture | pages [10] -->
关注数学模型

<!-- b000357 | furniture | pages [10] -->
2

<!-- b000358 | furniture | pages [10] -->
MATHmodels

<!-- b000359 | furniture | pages [10] -->
获取更多资讯

<!-- b000360 | furniture | pages [11] -->
Team 2410482

<!-- b000361 | furniture | pages [11] -->
Page 10

<!-- b000362 | prose | pages [11] -->
Based on this model, we use the 2023 Wimbledon Gentlemen’s singles final as an example to plot

<!-- b000363 | prose | pages [11] -->
the momentum trends of Novak Djokovic throughout the match:

<!-- b000364 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000365 | prose | pages [11] -->
图5: momentum trends of Novak Djokovic in 2023 Wimbledon Gentlemen’s final

<!-- b000366 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000367 | prose | pages [11] -->
As can be seen from the figure, there are two ups and downs in momentum in terms of the

<!-- b000368 | prose | pages [11] -->
general trend, and its ups and downs are roughly in line with the audience’s intuitive cognition of the

<!-- b000369 | prose | pages [11] -->
game. Looking at the details, momentum fluctuates within a certain range depending on the specific

<!-- b000370 | prose | pages [11] -->
circumstances of each point.

<!-- b000371 | prose | pages [11] -->
Is It Random? Measuring the Significance of Momentum Ef- 5

<!-- b000372 | prose | pages [11] -->
fects

<!-- b000373 | prose | pages [11] -->
Analysis and Methodology Overview 5.1

<!-- b000374 | prose | pages [11] -->
In light of the preliminary discussions and the model established, our initial hypothesis posits

<!-- b000375 | prose | pages [11] -->
that "momentum"significantly influences outcomes within the context of the game, suggesting that an

<!-- b000376 | prose | pages [11] -->
athlete’s victory correlates with momentum rather than being a mere product of random fluctuations

<!-- b000377 | prose | pages [11] -->
in performance as suggested by the coach’s perspectives. To substantiate this assertion, we propose to

<!-- b000378 | prose | pages [11] -->
employ hypothesis testing and logistic regression analysis as methodological approaches to elucidate

<!-- b000379 | prose | pages [11] -->
the relationship between an athlete’s momentum and score.

<!-- b000380 | furniture | pages [11] -->
关注数学模型

<!-- b000381 | furniture | pages [11] -->
2

<!-- b000382 | furniture | pages [11] -->
MATHmodels

<!-- b000383 | furniture | pages [11] -->
获取更多资讯

<!-- b000384 | furniture | pages [12] -->
Team 2410482

<!-- b000385 | furniture | pages [12] -->
Page 11

<!-- b000386 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000387 | caption | pages [12] -->
Figure 6: flow chart

<!-- b000388 | prose | pages [12] -->
To effectively counter the coach’s argument and adhere to the principle of protecting the null

<!-- b000389 | prose | pages [12] -->
hypothesis through hypothesis testing, we establish the following hypotheses:

<!-- b000390 | prose | pages [12] -->
Null Hypothesis(𝐻0): There is no significant relationship between M(momentum) and P(the

<!-- b000391 | prose | pages [12] -->
scoring probability).

<!-- b000392 | prose | pages [12] -->
Alternative Hypothesis(𝐻1): There is a significant relationship between M(momentum)and

<!-- b000393 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000394 | prose | pages [12] -->
P(the scoring probability).

<!-- b000395 | prose | pages [12] -->
Subsequently, to explore whether there is a significant relationship between momentum and

<!-- b000396 | prose | pages [12] -->
winning a game, we conduct a logistic regression analysis. the function form is shown as follows:

<!-- b000397 | prose | pages [12] -->
𝑃(𝑌= 1)

<!-- b000398 | prose | pages [12] -->
5 ∑︁

<!-- b000399 | prose | pages [12] -->
𝛽𝑖𝑋𝑖

<!-- b000400 | prose | pages [12] -->
1 −𝑃(𝑌= 1) = 𝛽0 + 𝛽1𝑀+ ln

<!-- b000401 | prose | pages [12] -->
(7)

<!-- b000402 | prose | pages [12] -->
𝑖=2

<!-- b000403 | prose | pages [12] -->
Let P refers to the scoring probability; 1-P refers to losing point probability, which is different

<!-- b000404 | prose | pages [12] -->
from the previous winning rate, which refers to a certain match, but here refers to each point. 𝛽0 refers

<!-- b000405 | prose | pages [12] -->
to intercept term which is a constant;𝛽1 refers to the coefficient of the impact of momentum on the

<!-- b000406 | prose | pages [12] -->
probability of winning; M refers to momentum ; 𝑋𝑖(𝑖= 2, 3, 4, 5) refers to other control variables,

<!-- b000407 | prose | pages [12] -->
which has no influence on momentum but may also correlate with scores,which represent running

<!-- b000408 | prose | pages [12] -->
distance difference, serve speed, net points or no points, and winning rate, respectively, all of which

<!-- b000409 | prose | pages [12] -->
are control variables 𝛽𝑖(𝑖= 2, 3, 4, 5) represents the coefficient of the impact of other control variables

<!-- b000410 | prose | pages [12] -->
on the probability of winning.

<!-- b000411 | prose | pages [12] -->
Parameter Estimation: Based on MLE 5.2

<!-- b000412 | prose | pages [12] -->
Maximum Likelihood Estimation (MLE) is a key method in statistics for finding the best-fitting

<!-- b000413 | prose | pages [12] -->
parameters in logistic regression, ensuring models accurately reflect observed data.In our parameter

<!-- b000414 | prose | pages [12] -->
estimation, the formula for mle is as follows:

<!-- b000415 | prose | pages [12] -->
𝑛

<!-- b000416 | prose | pages [12] -->
𝑌𝑖𝑙𝑜𝑔𝑃(𝑌𝑖= 1|𝑋𝑖) + (1 −𝑌𝑖)𝑙𝑜𝑔(1 −𝑃(𝑌𝑖= 1|𝑋𝑖))

<!-- b000417 | prose | pages [12] -->
∑︁

<!-- b000418 | prose | pages [12] -->
ℓ(𝛽) =

<!-- b000419 | prose | pages [12] -->


<!-- b000420 | prose | pages [12] -->
𝑖=1

<!-- b000421 | prose | pages [12] -->


<!-- b000422 | prose | pages [12] -->
(8)

<!-- b000423 | furniture | pages [12] -->
关注数学模型

<!-- b000424 | furniture | pages [12] -->
2

<!-- b000425 | furniture | pages [12] -->
MATHmodels

<!-- b000426 | furniture | pages [12] -->
获取更多资讯

<!-- b000427 | furniture | pages [13] -->
Team 2410482

<!-- b000428 | furniture | pages [13] -->
Page 12

<!-- b000429 | prose | pages [13] -->
ℓ(𝛽) is the logarithmic likelihood function to be maximized;𝛽= [𝛽0, 𝛽1, 𝛽2, 𝛽3, 𝛽4, 𝛽5] is a matrix

<!-- b000430 | prose | pages [13] -->
of parameter variables in logistic regression；𝑌𝑖is the 𝑖𝑡ℎobservation result of the dependent variable

<!-- b000431 | prose | pages [13] -->
𝑌；𝑋𝑖= [𝑋𝑖

<!-- b000432 | prose | pages [13] -->
1, 𝑋𝑖 2, 𝑋𝑖 3, 𝑋𝑖 4, 𝑋𝑖 5] is the matrix of the 𝑖𝑡ℎobservation of the independent variable.，The

<!-- b000433 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000434 | prose | pages [13] -->
expression of 𝑃(𝑌𝑖= 1|𝑋𝑖) is as follows:

<!-- b000435 | prose | pages [13] -->
𝑃(𝑌𝑖= 1|𝑋𝑖) = 1

<!-- b000436 | prose | pages [13] -->
(9) 1 + 𝑒−(𝛽0+𝛽1𝑋𝑖 1+......+𝛽5𝑋𝑖 5)

<!-- b000437 | prose | pages [13] -->
Based on the above formula, gradient descent method is adopted to optimize the parameters to

<!-- b000438 | prose | pages [13] -->
find the maximum likelihood function, and the optimization formula is as follows：

<!-- b000439 | prose | pages [13] -->
𝛽𝑛𝑒𝑤= 𝛽𝑜𝑙𝑑+ 𝛾𝜕ℓ

<!-- b000440 | prose | pages [13] -->
𝛼is the optimized parameter.

<!-- b000441 | prose | pages [13] -->
(10) 𝜕𝛽

<!-- b000442 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000443 | heading | pages [13] -->
The Result of Regression and Hypothesis Testing

<!-- b000444 | prose | pages [13] -->
5.3

<!-- b000445 | prose | pages [13] -->
According to this model, the results we got are shown in the following table:

<!-- b000446 | prose | pages [13] -->
regression parameter variable name

<!-- b000447 | prose | pages [13] -->
estimates

<!-- b000448 | prose | pages [13] -->
momentum 1.500 difference in moving

<!-- b000449 | prose | pages [13] -->
-0.004 distance

<!-- b000450 | prose | pages [13] -->
server and serve speed 0.008 whether player won the point while at the

<!-- b000451 | prose | pages [13] -->
-0.251

<!-- b000452 | prose | pages [13] -->
net or not

<!-- b000453 | prose | pages [13] -->
winning rate -1.994 intercept 0.883

<!-- b000454 | prose | pages [13] -->
the 95% confidence intervals T-statistic p. value

<!-- b000455 | prose | pages [13] -->
of the regression parameters <0.001 35.347 (1.0052,1.9939)

<!-- b000456 | prose | pages [13] -->
0.065 0.798 (-0.0316,0.0243)

<!-- b000457 | prose | pages [13] -->
<0.001 35.446 0.0052,0.0103)

<!-- b000458 | prose | pages [13] -->
0.704 0.402 (-0.8384,-0.3358)

<!-- b000459 | prose | pages [13] -->
7.613 0.006 (-3.4111,-0.5777) 5.512 0.019

<!-- b000460 | prose | pages [13] -->
It can be seen that the p.value corresponding to the momentum T-statistic is much less than 0.05,

<!-- b000461 | prose | pages [13] -->
and the 95% confidence interval of the 𝛽1 1 estimate does not contain 0. Therefore, we reject the null

<!-- b000462 | prose | pages [13] -->
hypothesis 𝐻0, which means momentum has a significant relationship with score.

<!-- b000463 | furniture | pages [13] -->
关注数学模型

<!-- b000464 | furniture | pages [13] -->
2

<!-- b000465 | furniture | pages [13] -->
MATHmodels

<!-- b000466 | furniture | pages [13] -->
获取更多资讯

<!-- b000467 | furniture | pages [14] -->
Team 2410482

<!-- b000468 | furniture | pages [14] -->
Page 13

<!-- b000469 | prose | pages [14] -->
Momentum Projections,Influencing Factors and Recommenda- 6

<!-- b000470 | prose | pages [14] -->
tions

<!-- b000471 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000472 | prose | pages [14] -->
In the previous chapters, we found the qualitative definition of momentum by consulting pro-

<!-- b000473 | prose | pages [14] -->
fessional literature, and we gave the quantitative definition of momentum based on this to ensure the

<!-- b000474 | prose | pages [14] -->
rationality of the quantitative definition. Since the State Space Model can directly model the state of the

<!-- b000475 | prose | pages [14] -->
dynamic system that cannot be directly observed and capture the change of the system state over time,

<!-- b000476 | prose | pages [14] -->
it is very suitable for the characteristics of potential energy in tennis match, and has great advantages

<!-- b000477 | prose | pages [14] -->
compared with ARIMA for predicting observable measurements and some machine learning models

<!-- b000478 | prose | pages [14] -->
with limited model explanation. Therefore, we will use the State Space Model and Kalman filter

<!-- b000479 | prose | pages [14] -->
algorithm to predict the momentum that is difficult to be observed. We get that the predicted result

<!-- b000480 | prose | pages [14] -->
is highly consistent with the defined result, which further ensures the rationality of the definition of

<!-- b000481 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000482 | prose | pages [14] -->
potential energy. Then, the correlation analysis of momentum predictor and game factors (based on

<!-- b000483 | prose | pages [14] -->
literature) was carried out, and we obtained that Net pt won, Winner,Ace were significantly correlated

<!-- b000484 | prose | pages [14] -->
with momentum in a positive direction, and Unforced Errors, Break pt missed, Double fault was sig-

<!-- b000485 | prose | pages [14] -->
nificantly correlated with momentum in a negative direction. Finally, based on the above conclusions,

<!-- b000486 | prose | pages [14] -->
we give some suggestions.

<!-- b000487 | prose | pages [14] -->
Prediction of the Momentum and Swings 6.1

<!-- b000488 | heading | pages [14] -->
Introduction to State Space Model and Kalman Filter Algorithm

<!-- b000489 | prose | pages [14] -->
6.1.1

<!-- b000490 | prose | pages [14] -->
The State Space Model originated in the aerospace and control engineering fields in the 1950s to

<!-- b000491 | prose | pages [14] -->
describe the state changes of dynamic systems and how to control the system state through 𝑖𝑛𝑝𝑢𝑡𝑠[1].

<!-- b000492 | prose | pages [14] -->
It is used to describe and analyze the dynamic behavior of the system, and has two outstanding

<!-- b000493 | prose | pages [14] -->
characteristics: First, the State Space Model distinguishes the internal state of the system from the

<!-- b000494 | prose | pages [14] -->
observed output. This allows it to handle situations where the internal state of the system may not be

<!-- b000495 | prose | pages [14] -->
directly observable, estimating these hidden states from the observed data. Second, the State Space

<!-- b000496 | prose | pages [14] -->
Model can be used to estimate the future state of the system based on the current and past states. These

<!-- b000497 | prose | pages [14] -->
two features are very important for the context of this problem.

<!-- b000498 | prose | pages [14] -->
The State Space Model consists of two main equations:

<!-- b000499 | prose | pages [14] -->
State Equation: Describes the time evolution of the state of a system (usually not directly observ-

<!-- b000500 | prose | pages [14] -->
able).

<!-- b000501 | prose | pages [14] -->
𝑥𝑡+1 = 𝐴𝑥𝑡+ 𝐵𝑢𝑡+ 𝜔𝑡 (11)

<!-- b000502 | furniture | pages [14] -->
关注数学模型

<!-- b000503 | furniture | pages [14] -->
2

<!-- b000504 | furniture | pages [14] -->
MATHmodels

<!-- b000505 | furniture | pages [14] -->
获取更多资讯

<!-- b000506 | furniture | pages [15] -->
Team 2410482

<!-- b000507 | furniture | pages [15] -->
Page 14

<!-- b000508 | prose | pages [15] -->
where 𝑥𝑡represents the state vector at time t,A is the state transition matrix,𝑢𝑡is the control input

<!-- b000509 | prose | pages [15] -->
vector,B is the control input matrix,𝜔𝑡is the process noise, representing the model’s uncertainty.

<!-- b000510 | prose | pages [15] -->
Observation Equation：Describes how to measure the state of a system by means of observations

<!-- b000511 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000512 | prose | pages [15] -->
containing noise.

<!-- b000513 | prose | pages [15] -->
𝑦𝑡= 𝐶𝑥𝑡+ 𝑣𝑡 (12)

<!-- b000514 | prose | pages [15] -->
where 𝑦𝑡represents the observation vector at time𝑡,𝐶is the observation matrix, 𝑣𝑡is the observation

<!-- b000515 | prose | pages [15] -->
noise, accounting for measyrement errors.

<!-- b000516 | prose | pages [15] -->
We can understand the process of the State Space Model through the figure below, and it can be

<!-- b000517 | prose | pages [15] -->
seen from the figure that the core of the State Space Model solving algorithm is Kalman filter.

<!-- b000518 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000519 | caption | pages [15] -->
Figure 7: schematic of the State Space Model

<!-- b000520 | prose | pages [15] -->
Since people’s subjective understanding (the theoretical state value generated by the establishment

<!-- b000521 | prose | pages [15] -->
of mathematical models) and measurement (sensor and other measurement values) are not accurate,

<!-- b000522 | prose | pages [15] -->
Kalman filter is introduced to infer the state of a linear dynamic system from a series of noise

<!-- b000523 | prose | pages [15] -->
measurements, and the error of both is synthesized to obtain the optimal prediction of the true value. The

<!-- b000524 | prose | pages [15] -->
essence of Kalman filtering algorithm is to use the property that the fusion of two normal distributions

<!-- b000525 | prose | pages [15] -->
is still a normal distribution to iterate, which can be better understood through the following figure.

<!-- b000526 | caption | pages [15] -->
Figure 8: schematic of the Kalman filter

<!-- b000527 | furniture | pages [15] -->
关注数学模型

<!-- b000528 | furniture | pages [15] -->
2

<!-- b000529 | furniture | pages [15] -->
MATHmodels

<!-- b000530 | furniture | pages [15] -->
获取更多资讯

<!-- b000531 | furniture | pages [16] -->
Team 2410482

<!-- b000532 | furniture | pages [16] -->
Page 15

<!-- b000533 | prose | pages [16] -->
With the above foundation, understanding the mathematical expression of Kalman filtering be-

<!-- b000534 | prose | pages [16] -->
comes very easy.

<!-- b000535 | prose | pages [16] -->
1.Prediction Phase:Before receiving the new measurement, the Kalman filter predicts the current

<!-- b000536 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000537 | prose | pages [16] -->
state and error covariance based on the previous state:

<!-- b000538 | prose | pages [16] -->
(

<!-- b000539 | prose | pages [16] -->
𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑𝑠𝑡𝑎𝑡𝑒𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑒:

<!-- b000540 | prose | pages [16] -->
𝑥𝑡|𝑡−1 = 𝐴ˆ 𝑥𝑡−1 + 𝐵𝑢𝑡−1; ˆ

<!-- b000541 | prose | pages [16] -->
(13)

<!-- b000542 | prose | pages [16] -->
𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑𝑒𝑟𝑟𝑜𝑟𝑐𝑜𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒: 𝑃𝑡|𝑡−1 = 𝐴𝑃𝑡−1|𝑡−1𝐴𝑇+ 𝑄

<!-- b000543 | prose | pages [16] -->
where Q is the process noise covariance matrix.

<!-- b000544 | prose | pages [16] -->
2.Update Phase:Upon receiving a new measurement 𝑦𝑡, the filter updates its estimates:

<!-- b000545 | prose | pages [16] -->
𝐾𝑎𝑙𝑚𝑎𝑛𝑔𝑎𝑖𝑛: 𝐾𝑡= 𝑃𝑡|𝑡−1𝐶𝑇(𝐶𝑃𝑡|𝑡−1𝐶𝑇+ 𝑅)−1;

<!-- b000546 | prose | pages [16] -->


<!-- b000547 | prose | pages [16] -->
𝑈𝑝𝑑𝑎𝑡𝑒𝑑𝑠𝑡𝑎𝑡𝑒𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑒: ˆ𝑥𝑡= 𝑥𝑡|𝑡−1 + 𝐾𝑡(𝑦𝑡−𝐶 𝑥𝑡|𝑡−1);

<!-- b000548 | prose | pages [16] -->
(14)

<!-- b000549 | prose | pages [16] -->
ˆ ˆ

<!-- b000550 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000551 | prose | pages [16] -->


<!-- b000552 | prose | pages [16] -->
𝑈𝑝𝑑𝑎𝑡𝑒𝑑𝑒𝑟𝑟𝑜𝑟𝑐𝑜𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒: 𝑃𝑡= (𝐼−𝐾𝑡𝐶)𝑃𝑡|𝑡−1

<!-- b000553 | prose | pages [16] -->
where R is the observation noise covariance matrix.

<!-- b000554 | prose | pages [16] -->
6.1.2

<!-- b000555 | heading | pages [16] -->
Building Predictive Model

<!-- b000556 | prose | pages [16] -->
Based on 334 points of Novak Djokovic versus Carlos Alcaraz , we build the model through the

<!-- b000557 | prose | pages [16] -->
following steps:

<!-- b000558 | heading | pages [16] -->
Step 1 Determining the State Space Model

<!-- b000559 | prose | pages [16] -->
We consider a state space model in which the momentum is a time-varying latent state process.In a

<!-- b000560 | prose | pages [16] -->
match, the momentum of a player changes with the progress of the game, and because of the differences

<!-- b000561 | prose | pages [16] -->
in the physical and mental qualities of the players themselves, the play on the court, and the situation

<!-- b000562 | prose | pages [16] -->
they face, for a particular player, the momentum is assumed to follow an autoregressive process:

<!-- b000563 | prose | pages [16] -->
𝑀𝑡= 𝜇+ 𝜑𝑀𝑡−1 + 𝜔𝑡 (15)

<!-- b000564 | prose | pages [16] -->
Where 𝜇is a constant term,which serves as a baseline level that provides an initial value for

<!-- b000565 | prose | pages [16] -->
𝜑is the autoregressive coefficient and the disturbances are the subsequent optimization process.

<!-- b000566 | prose | pages [16] -->
independently and identical distributed with𝜔𝑡∼𝑁(0, 𝜎2

<!-- b000567 | prose | pages [16] -->
𝜔).

<!-- b000568 | prose | pages [16] -->
In addition, we can assume that the swings in a player’s winning rate(𝑊𝑡) depend on momentum,

<!-- b000569 | prose | pages [16] -->
where the swings in win percentage can be obtained by observation through the Markov Chain of

<!-- b000570 | prose | pages [16] -->
Model I. At the same time, in our continuous optimization and updating of the model, we found that

<!-- b000571 | prose | pages [16] -->
adding the service advantage correction 𝛿can significantly improve the fit degree of the predicted value

<!-- b000572 | prose | pages [16] -->
and the defined value. The observation equation as follows:

<!-- b000573 | furniture | pages [16] -->
关注数学模型

<!-- b000574 | furniture | pages [16] -->
2

<!-- b000575 | furniture | pages [16] -->
MATHmodels

<!-- b000576 | furniture | pages [16] -->
获取更多资讯

<!-- b000577 | furniture | pages [17] -->
Team 2410482

<!-- b000578 | furniture | pages [17] -->
Page 16

<!-- b000579 | prose | pages [17] -->
𝑊𝑡= 𝛿+ 𝑀𝑡+ 𝜏𝑡 (16)

<!-- b000580 | prose | pages [17] -->
Where 𝑊𝑡refers to swings in winning rate,𝛿refers to service advantage corrections,𝑀𝑡refers to

<!-- b000581 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000582 | prose | pages [17] -->
momentum.𝜏𝑡∼𝑁(0, 𝜎2

<!-- b000583 | prose | pages [17] -->
𝑡). Therefore,the state space model takes the form:

<!-- b000584 | prose | pages [17] -->
(

<!-- b000585 | prose | pages [17] -->
𝑆𝑡𝑎𝑡𝑒𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛: 𝑀𝑡= 𝑀𝑡= 𝜇+ 𝜑𝑀𝑡−1 + 𝜔𝑡

<!-- b000586 | prose | pages [17] -->
(17)

<!-- b000587 | prose | pages [17] -->
𝑂𝑏𝑠𝑒𝑟𝑣𝑎𝑡𝑖𝑜𝑛𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛: 𝑊𝑡= 𝛿+ 𝑀𝑡+ 𝜏𝑡

<!-- b000588 | prose | pages [17] -->
Step 2 Implementation of the Kalman Filter

<!-- b000589 | prose | pages [17] -->
Before implementing the Kalman filter, the prior mean and variance have to be defined.The initial

<!-- b000590 | prose | pages [17] -->
𝜇 mean is set to 𝑀1|0 = 𝜎2

<!-- b000591 | prose | pages [17] -->
𝜔

<!-- b000592 | prose | pages [17] -->
1−𝜙1 and initial covariance is Σ1|0 =

<!-- b000593 | prose | pages [17] -->
1,which are the conditional expectation 1−𝜑2

<!-- b000594 | prose | pages [17] -->
of the predicted momentum. Let 𝑀𝑡|𝑡−1be the predicted momentum for time 𝑡conditional on the

<!-- b000595 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000596 | prose | pages [17] -->
information obtained from time 𝑡−1. Furthermore, let 𝑀𝑡|𝑡denote the updated momentum conditional

<!-- b000597 | prose | pages [17] -->
on the information obtained up to time𝑡. The corresponding variances of 𝑀𝑡conditional on information

<!-- b000598 | prose | pages [17] -->
at time 𝑡−1 is denoted as Σ𝑡|𝑡−1and the updated variance is given byΣ𝑡|𝑡. 𝐺𝑘is defined by covariance

<!-- b000599 | prose | pages [17] -->
and 𝜑2

<!-- b000600 | prose | pages [17] -->
𝑡simply for computational simplicity.Drawing from Manner’s work in 2015[2], the Kalman filter

<!-- b000601 | prose | pages [17] -->
procedure employed for the dynamic state space model mentioned can be defined as follows:

<!-- b000602 | prose | pages [17] -->
Prediction Step:

<!-- b000603 | prose | pages [17] -->
(

<!-- b000604 | prose | pages [17] -->
𝑀𝑡|𝑡−1 = 𝜇+ 𝜑𝑡𝑀𝑡−1|𝑡−1 Σ𝑡|𝑡−1 = 𝜑2

<!-- b000605 | prose | pages [17] -->
Observation Step:

<!-- b000606 | prose | pages [17] -->
(18)

<!-- b000607 | prose | pages [17] -->
𝑡Σ𝑡−1|𝑡−1 + 𝜎2

<!-- b000608 | prose | pages [17] -->
𝜔

<!-- b000609 | prose | pages [17] -->
ˆ𝑦𝑡= 𝛿+ 𝑀𝑡|𝑡−1

<!-- b000610 | prose | pages [17] -->


<!-- b000611 | prose | pages [17] -->
𝐺𝑡= Σ𝑡|𝑡−1 + 𝜎2

<!-- b000612 | prose | pages [17] -->


<!-- b000613 | prose | pages [17] -->
(19)

<!-- b000614 | prose | pages [17] -->
𝑡 ˆ𝑒𝑡= 𝑦𝑡−ˆ𝑦𝑡

<!-- b000615 | prose | pages [17] -->
Updating Step:

<!-- b000616 | prose | pages [17] -->
𝑀𝑡|𝑡= 𝑀𝑡|𝑡−1 + ˆ𝑒𝑡Σ𝑡|𝑡−1

<!-- b000617 | prose | pages [17] -->


<!-- b000618 | prose | pages [17] -->
𝐺𝑡

<!-- b000619 | prose | pages [17] -->
(20)

<!-- b000620 | prose | pages [17] -->
Σ2

<!-- b000621 | prose | pages [17] -->
𝑡|𝑡−1

<!-- b000622 | prose | pages [17] -->
Σ𝑡|𝑡= Σ𝑡|𝑡−1 −

<!-- b000623 | prose | pages [17] -->


<!-- b000624 | prose | pages [17] -->
6.1.3

<!-- b000625 | heading | pages [17] -->
Prediction Results and Analysis

<!-- b000626 | prose | pages [17] -->
𝐺𝑡

<!-- b000627 | prose | pages [17] -->
Based on the establishment of the above model, we implement the model through R language to

<!-- b000628 | prose | pages [17] -->
get the result. First,check that our object is a predictable object. Then, in the results we give, we get the

<!-- b000629 | prose | pages [17] -->
momentum of Novak Djokovic, and the momentum of Carlos Alcaraz is opposite. At the same time,

<!-- b000630 | prose | pages [17] -->
the athlete who is interested in momentum must also be interested in the change in momentum, because

<!-- b000631 | prose | pages [17] -->
the momentum we predict is continuous, so we define the derivative at each point as the swings of

<!-- b000632 | furniture | pages [17] -->
关注数学模型

<!-- b000633 | furniture | pages [17] -->
2

<!-- b000634 | furniture | pages [17] -->
MATHmodels

<!-- b000635 | furniture | pages [17] -->
获取更多资讯

<!-- b000636 | furniture | pages [18] -->
Team 2410482

<!-- b000637 | furniture | pages [18] -->
Page 17

<!-- b000638 | prose | pages [18] -->
momentum, which is calculated as M’. Momentum and the swings of momentum change over time are

<!-- b000639 | prose | pages [18] -->
shown in the figure. The red realization shows the change in momentum over the course of the race,

<!-- b000640 | prose | pages [18] -->
and the dashed blue line shows the change in swings of momentum over the course of the race.

<!-- b000641 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000642 | caption | pages [18] -->
Figure 9: prognostic map

<!-- b000643 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000644 | prose | pages [18] -->
6.1.4

<!-- b000645 | heading | pages [18] -->
Model Evaluation

<!-- b000646 | prose | pages [18] -->
In this study, cross-validation was utilized to verify the accuracy of each model. Evaluation

<!-- b000647 | prose | pages [18] -->
indicators, including Mean Square Error (MSE), Root Mean Square Error (RMSE), Mean Absolute

<!-- b000648 | prose | pages [18] -->
Error (MAE), and R-squared (𝑅2) from cross-validation results. These indicators assess the accuracy

<!-- b000649 | prose | pages [18] -->
of both the estimated and validated models, ensuring the reliability of the model assessments.

<!-- b000650 | prose | pages [18] -->
indicators MSE

<!-- b000651 | prose | pages [18] -->
Predictive Model 0.0454

<!-- b000652 | prose | pages [18] -->
𝑅2 RMSE MAE

<!-- b000653 | prose | pages [18] -->
0.2131 0.1660 0.8902

<!-- b000654 | prose | pages [18] -->
In terms of the above evaluation indicators. MSE, RMSE, and MAE are all relatively low, while

<!-- b000655 | prose | pages [18] -->
R-squared is close to 1, indicating that the model is a good fit and can explain most of the variability

<!-- b000656 | prose | pages [18] -->
of the observed values. This shows that from the mathematical point of view, the model has good

<!-- b000657 | prose | pages [18] -->
predictive performance.

<!-- b000658 | prose | pages [18] -->
6.2 Correlation Analysis

<!-- b000659 | prose | pages [18] -->
Based on the given data of the competition and the factors mentioned in the literature, we finally

<!-- b000660 | prose | pages [18] -->
determined to do the correlation analysis between the swings of momentum and 12 factors,which is Un-

<!-- b000661 | prose | pages [18] -->
forced Errors,Ace,Match Point,Distance run,Rally count,Winner,Double fault,Net pt,Net pt won,

<!-- b000662 | prose | pages [18] -->
Break _pt,Break _pt _won,Break _pt _missed.

<!-- b000663 | furniture | pages [18] -->
关注数学模型

<!-- b000664 | furniture | pages [18] -->
2

<!-- b000665 | furniture | pages [18] -->
MATHmodels

<!-- b000666 | furniture | pages [18] -->
获取更多资讯

<!-- b000667 | furniture | pages [19] -->
Team 2410482

<!-- b000668 | furniture | pages [19] -->
Page 18

<!-- b000669 | prose | pages [19] -->
For whether the 12 factors are significantly correlated with the swings of momentum and the

<!-- b000670 | prose | pages [19] -->
degree of correlation, we use P-value and Pearson correlation coefficient as analysis indicators. In

<!-- b000671 | prose | pages [19] -->
terms of P value, 𝑃< 0.05 indicates that this factor is significantly correlated with momentum change.

<!-- b000672 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000673 | prose | pages [19] -->
For Pearson correlation coefficient, 0 is the boundary, and the positive correlation increases as the

<!-- b000674 | prose | pages [19] -->
value approaches 1, while the negative correlation increases as the value approaches -1. The data was

<!-- b000675 | prose | pages [19] -->
imported into Origin and analyzed to obtain the following two correlation analysis charts:

<!-- b000676 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000677 | caption | pages [19] -->
Figure 10: Correlation Analysis figure1

<!-- b000678 | caption | pages [19] -->
Figure 11: Correlation Analysis figure2

<!-- b000679 | prose | pages [19] -->
6.3 Suggestions

<!-- b000680 | prose | pages [19] -->
Athletes usually need to conduct targeted research on the opponent’s skills and tactics before

<!-- b000681 | prose | pages [19] -->
the game. If the momentum fluctuation of the opponent’s previous game is targeted research, it is

<!-- b000682 | prose | pages [19] -->
conducive to occupy the advantage of the game in the psychological level. We divided the athletes

<!-- b000683 | prose | pages [19] -->
into two different types according to the size of momentum fluctuation, namely, the type with strong

<!-- b000684 | prose | pages [19] -->
momentum fluctuation and the type with relatively stable momentum.

<!-- b000685 | furniture | pages [19] -->
关注数学模型

<!-- b000686 | furniture | pages [19] -->
2

<!-- b000687 | furniture | pages [19] -->
MATHmodels

<!-- b000688 | furniture | pages [19] -->
获取更多资讯

<!-- b000689 | furniture | pages [20] -->
Team 2410482

<!-- b000690 | furniture | pages [20] -->
Page 19

<!-- b000691 | prose | pages [20] -->
Suggestions for Players with Strong Momentum 6.3.1

<!-- b000692 | prose | pages [20] -->
The momentum of a player with strong momentum fluctuations in a normal game often has ups

<!-- b000693 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000694 | prose | pages [20] -->
and downs and fluctuations. This is a double-edged sword. Once the momentum is at the peak of the

<!-- b000695 | prose | pages [20] -->
disadvantage, there is a great possibility to reverse the unfavorable situation, but at the same time, the

<!-- b000696 | prose | pages [20] -->
advantage of the score is also easy to fall because of the opponent’s continuous score or the trough of

<!-- b000697 | prose | pages [20] -->
the momentum, which is inadvertently reversed.

<!-- b000698 | prose | pages [20] -->
If the opponent is such a player, then the opponent is more likely to be affected by changes in the

<!-- b000699 | prose | pages [20] -->
match situation. From the correlation analysis, we can see that the unforced errors and the waste of

<!-- b000700 | prose | pages [20] -->
break points are negatively correlated with the swings of momentum, so we can seize the weakness of

<!-- b000701 | prose | pages [20] -->
the opponent, play more aggressive balls, mobilize the opponent’s movement, and force the opponent to

<!-- b000702 | prose | pages [20] -->
miss opportunities and make mistakes. The appearance of net points and winner is positively correlated

<!-- b000703 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000704 | prose | pages [20] -->
with the change of momentum, so we should play less short balls that fall in front of the net, do not

<!-- b000705 | prose | pages [20] -->
give the opponent the chance to score in front of the net, and increase the defense ability.

<!-- b000706 | prose | pages [20] -->
Suggestions for Relatively Stable Momentum 6.3.2

<!-- b000707 | prose | pages [20] -->
Players tend to have relatively stable momentum throughout the game and are not prone to

<!-- b000708 | prose | pages [20] -->
dramatic fluctuations. In the advantage situation, such players have strong ability to control and expand

<!-- b000709 | prose | pages [20] -->
the advantage. In the disadvantageous situation, such players are also prone to the weakness of lack of

<!-- b000710 | prose | pages [20] -->
toughness and lack of flipping ability.

<!-- b000711 | prose | pages [20] -->
When the opponent is such a player, the opening is particularly important. If seize the advantage

<!-- b000712 | prose | pages [20] -->
in the opening, it is easy to achieve an overwhelming advantage in the whole game. It is difficult to

<!-- b000713 | prose | pages [20] -->
reverse such an opponent if you start from a weak position. Therefore, it is necessary to take the lead

<!-- b000714 | prose | pages [20] -->
in the opening, with a strong offensive play to gain momentum.

<!-- b000715 | prose | pages [20] -->
ExtensionTest ——InWomen’sTennisandTableTennisMatches 7

<!-- b000716 | prose | pages [20] -->
To evaluate the universality of our model, we selected a women’s tennis match and a women’s

<!-- b000717 | prose | pages [20] -->
table tennis match for analysis. For details on the data sources, refer to Section 1.4, Data Sources.

<!-- b000718 | prose | pages [20] -->
In the women’s tennis match analysis, our model showed good predictive ability with potential for

<!-- b000719 | prose | pages [20] -->
enhancement. By analyzing predictions and considering gender differences in tennis,we significantly

<!-- b000720 | prose | pages [20] -->
enhanced the model’s fit by adjusting the service advantage correction coefficient(𝛿)，resulting in an

<!-- b000721 | prose | pages [20] -->
exceptional predictive model.

<!-- b000722 | prose | pages [20] -->
In the analysis of women’s table tennis, the model’s predictions, particularly for real-time trends

<!-- b000723 | prose | pages [20] -->
and extremes, were suboptimal. Adjusting the autoregressive coefficient notably enhanced extreme

<!-- b000724 | furniture | pages [20] -->
关注数学模型

<!-- b000725 | furniture | pages [20] -->
2

<!-- b000726 | furniture | pages [20] -->
MATHmodels

<!-- b000727 | furniture | pages [20] -->
获取更多资讯

<!-- b000728 | furniture | pages [21] -->
Team 2410482

<!-- b000729 | furniture | pages [21] -->
Page 20

<!-- b000730 | prose | pages [21] -->
value predictions, yet results remained less satisfactory compared to tennis predictions.

<!-- b000731 | prose | pages [21] -->
Through

<!-- b000732 | prose | pages [21] -->
analysis, we identified that accurately depicting nonlinear relationships will be crucial for the model’s

<!-- b000733 | prose | pages [21] -->
future improvements.

<!-- b000734 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000735 | prose | pages [21] -->
7.1 Scenario of Women’s Tennis Matches

<!-- b000736 | prose | pages [21] -->
We selected a match from the 2023 U.S. Open final between Coco Gauff and Aryna Sabalenka

<!-- b000737 | prose | pages [21] -->
for our study. In this match,Coco Gauff overcame Aryna Sabalenka with a score of 2-6, 6-3, 6-2.

<!-- b000738 | prose | pages [21] -->
This victory not only secured Gauff her first Grand Slam title but also positioned her as the new face

<!-- b000739 | prose | pages [21] -->
of American tennis,echoing the legacy of Serena Williams. We first calculated Aryna Sabalenka’s

<!-- b000740 | prose | pages [21] -->
momentum by definition given by us, which allowed us to derive Coco Gauff’s momentum accordingly.

<!-- b000741 | prose | pages [21] -->
Subsequently, using Model II (we obtained the predicted values of momentum.) The results are

<!-- b000742 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000743 | prose | pages [21] -->
illustrated in the figure on the left "Before optimization":

<!-- b000744 | caption | pages [21] -->
Figure 12: Before and after change

<!-- b000745 | prose | pages [21] -->
The graph shows the actual momentum as a red curve and the predicted momentum in blue,

<!-- b000746 | prose | pages [21] -->
highlighting close alignment at most points and indicating the predictive model’s consistency with

<!-- b000747 | prose | pages [21] -->
reality. Notably, discrepancies between predictions and actual values are larger at the match’s start and

<!-- b000748 | prose | pages [21] -->
end, likely due to the unpredictability of these phases and possible limitations in the metrics’ ability

<!-- b000749 | prose | pages [21] -->
to capture the match’s dynamics, resulting in greater prediction errors. However, during the middle

<!-- b000750 | prose | pages [21] -->
phase, the alignment improves, suggesting the model’s enhanced performance. Sharp deviations in

<!-- b000751 | prose | pages [21] -->
actual momentum at the 60th and 120th points, not fully captured by predictions, may be attributed to

<!-- b000752 | prose | pages [21] -->
unforeseen events or factors not accounted for in the model.

<!-- b000753 | prose | pages [21] -->
Following adjustments and optimizations to the original state space model, we significantly

<!-- b000754 | prose | pages [21] -->
improved the model’s fit by changing 𝛿to 0.005(the service advantage correction coefficient in the

<!-- b000755 | prose | pages [21] -->
observation equation: 𝑊𝑡= 𝛿+ 𝑀𝑡+ 𝜏𝑡) The results, depicted on the right side:"After optimization" suggest this improvement may be due to the format differences between men’s and women’s matches

<!-- b000756 | prose | pages [21] -->
—men’s are typically best-of-five sets, while women’s are best-of-three. More sets in men’s matches

<!-- b000757 | prose | pages [21] -->
could mean a larger dataset, potentially enabling more accurate long-term trend and pattern predictions.

<!-- b000758 | furniture | pages [21] -->
关注数学模型

<!-- b000759 | furniture | pages [21] -->
2

<!-- b000760 | furniture | pages [21] -->
MATHmodels

<!-- b000761 | furniture | pages [21] -->
获取更多资讯

<!-- b000762 | furniture | pages [22] -->
Team 2410482

<!-- b000763 | furniture | pages [22] -->
Page 21

<!-- b000764 | prose | pages [22] -->
Moreover, men’s tennis often focuses on power and service, whereas women’s tennis emphasizes

<!-- b000765 | prose | pages [22] -->
strategy and variation in play. Thus, outcomes in men’s matches might be more dominated by top

<!-- b000766 | prose | pages [22] -->
players, simplifying predictions to some extent. After adjusting the service advantage coefficient,

<!-- b000767 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000768 | prose | pages [22] -->
the model’s fit improved significantly, with the prediction residuals showing 𝑀𝑆𝐸= 0.051,𝑀𝐴𝐸=

<!-- b000769 | prose | pages [22] -->
0.1932, and 𝑅2=0.8763, further proving the enhanced predictive effectiveness of our revised model.

<!-- b000770 | prose | pages [22] -->
Overall, the predictive curve generally follows the actual trend, despite deviations at certain

<!-- b000771 | prose | pages [22] -->
points. Continuous experimentation and analysis of deviation causes significantly increased prediction

<!-- b000772 | prose | pages [22] -->
accuracy.

<!-- b000773 | prose | pages [22] -->
7.2 Scenario of Table Tennis Matches

<!-- b000774 | prose | pages [22] -->
We selected a match from the 2020 WTT Macau International Table Tennis Tournament Women’s

<!-- b000775 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000776 | prose | pages [22] -->
Singles semifinals between Manyu Wang and Yingsha Sun.In the dazzling display at the 2020 WTT

<!-- b000777 | prose | pages [22] -->
Macau, Sun Yingsha outplayed Wang Manyu 5-1 in the Women’s Singles, showcasing strategic mastery

<!-- b000778 | prose | pages [22] -->
and securing a historic win in this premier event.

<!-- b000779 | prose | pages [22] -->
We firstly find out the momentum of Yingsha Sun through the definition, and accordingly we can

<!-- b000780 | prose | pages [22] -->
get the momentum of Manyu Wang, and then we get the predicted value of momentum through Model

<!-- b000781 | prose | pages [22] -->
II.The results are as follows:

<!-- b000782 | caption | pages [22] -->
Figure 13: Before and after change

<!-- b000783 | prose | pages [22] -->
The red curve represents the actual momentum values, while the blue curve represents the forecast

<!-- b000784 | prose | pages [22] -->
momentum values. In most time series, the prediction curve closely follows the actual curve, indicating

<!-- b000785 | prose | pages [22] -->
that the prediction model has a high ability to approximate the actual trend.However, the deviation

<!-- b000786 | prose | pages [22] -->
between the two curves also reveals the limitation of the prediction accuracy of the model at a specific

<!-- b000787 | prose | pages [22] -->
time, especially at the extreme point of the momentum.

<!-- b000788 | prose | pages [22] -->
This deviation suggests that the model may need to incorporate more variables that affect the

<!-- b000789 | prose | pages [22] -->
momentum of the game or to re-weight the existing variables in order to more accurately predict

<!-- b000790 | prose | pages [22] -->
fluctuations in momentum during the game.Furthermore, this analysis may also indicate that the

<!-- b000791 | prose | pages [22] -->
model’s ability to capture non-linear relationships in the data needs to be improved.Therefore, we

<!-- b000792 | furniture | pages [22] -->
关注数学模型

<!-- b000793 | furniture | pages [22] -->
2

<!-- b000794 | furniture | pages [22] -->
MATHmodels

<!-- b000795 | furniture | pages [22] -->
获取更多资讯

<!-- b000796 | furniture | pages [23] -->
Team 2410482

<!-- b000797 | furniture | pages [23] -->
Page 22

<!-- b000798 | prose | pages [23] -->
adjusted the 𝜑(autoregressive coefficients) in the state equation of the original state space model to

<!-- b000799 | prose | pages [23] -->
reduce the smoothness of predictions and increase the accuracy of extreme value estimation.However,

<!-- b000800 | prose | pages [23] -->
we can still see that the effectiveness of the estimates needs to be enhanced. We speculate that this

<!-- b000801 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000802 | prose | pages [23] -->
is due to the rapid and variable nature of table tennis matches, which requires the model to have a

<!-- b000803 | prose | pages [23] -->
higher temporal resolution capability to capture the subtle dynamic changes in the game. Additionally,

<!-- b000804 | prose | pages [23] -->
it necessitates the incorporation of non-linear relationship modeling. Thus, enhancing the model’s

<!-- b000805 | prose | pages [23] -->
depiction of non-linearity will be an important direction for future improvements.

<!-- b000806 | prose | pages [23] -->
8

<!-- b000807 | heading | pages [23] -->
Sensitivity Analysis

<!-- b000808 | prose | pages [23] -->
In our prediction Model——State Space Model and Kalman Filter Algorithm, two constants of

<!-- b000809 | prose | pages [23] -->
the State Equation and Observation Equation are highly correlated with the players themselves. Among

<!-- b000810 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000811 | prose | pages [23] -->
them, are the autoregressive coefficient 𝜑，which is related to the player’s personal ability, and the

<!-- b000812 | prose | pages [23] -->
service advantage correction item 𝛿, which is related to the player’s service strength.

<!-- b000813 | prose | pages [23] -->
To test the sensitivity of our prediction model, State Space Model, we divided the remaining 30

<!-- b000814 | prose | pages [23] -->
players in the data set, except Carlos Alcaraz and Novak Djokovic, into 9 groups according to the two

<!-- b000815 | prose | pages [23] -->
indexes of individual ability and service scoring rate, and ensured that the number of players in each

<!-- b000816 | prose | pages [23] -->
group was 3 or 4. Individual ability and service scoring rate were both grouped from high to low and

<!-- b000817 | prose | pages [23] -->
numbered 1,2,3. Each group of players used the State Space Model to predict the momentum change,

<!-- b000818 | prose | pages [23] -->
and compared the predicted result with the calculated true value of the swings of momentum to obtain

<!-- b000819 | prose | pages [23] -->
the prediction accuracy rate. Then, the average accuracy rate of each group members was taken as the

<!-- b000820 | prose | pages [23] -->
numerical representative of the group and drawn into the following three-dimensional map:

<!-- b000821 | caption | pages [23] -->
Figure 14: Sensitivity Analysis

<!-- b000822 | prose | pages [23] -->
As can be seen in the figure above, the average accuracy of group are all higher than 70%. The

<!-- b000823 | furniture | pages [23] -->
关注数学模型

<!-- b000824 | furniture | pages [23] -->
2

<!-- b000825 | furniture | pages [23] -->
MATHmodels

<!-- b000826 | furniture | pages [23] -->
获取更多资讯

<!-- b000827 | furniture | pages [24] -->
Team 2410482

<!-- b000828 | furniture | pages [24] -->
Page 23

<!-- b000829 | prose | pages [24] -->
minimum value is 72% corresponding to service set 3-personal ability set 3, and the maximum value

<!-- b000830 | prose | pages [24] -->
is 87% of service set 1-personal ability set 1. And whether it is individual ability or service scoring

<!-- b000831 | prose | pages [24] -->
rate, the average accuracy rate increases with the decrease of group number, that is, the improvement

<!-- b000832 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000833 | prose | pages [24] -->
of ability. Therefore, we can conclude that we have the high accuracy of the prediction model, the low

<!-- b000834 | prose | pages [24] -->
sensitivity and the higher the player’s personal ability is, the better the prediction effect of the swings

<!-- b000835 | prose | pages [24] -->
of momentum will be.

<!-- b000836 | prose | pages [24] -->
9

<!-- b000837 | heading | pages [24] -->
Strengths and Weakness

<!-- b000838 | heading | pages [24] -->
Strengths:

<!-- b000839 | prose | pages [24] -->
•Tennis matches are divided into points, sets and reels. A game consists of points, a set consists

<!-- b000840 | prose | pages [24] -->
of different sets, and a match consists of different disks. This structure is well suited for modeling by

<!-- b000841 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000842 | prose | pages [24] -->
Markov method. The Markov model we apply accurately calculates the true winning percentage value.

<!-- b000843 | prose | pages [24] -->
•Our innovative binary definitions of winning percentage and momentum provide a comprehensive

<!-- b000844 | prose | pages [24] -->
measure of player performance on a technical level, a situational level, and all aspects of psychological

<!-- b000845 | prose | pages [24] -->
factors.

<!-- b000846 | prose | pages [24] -->
•Since state-space models can directly model the states of a dynamic system that cannot be

<!-- b000847 | prose | pages [24] -->
directly observed and capture the change of the system state over time, they are very well suited to

<!-- b000848 | prose | pages [24] -->
the characteristics of the potential energy in a tennis match, and have a great advantage over ARIMA,

<!-- b000849 | prose | pages [24] -->
which makes predictions on observable measurements, and some machine learning models, which have

<!-- b000850 | prose | pages [24] -->
a limited explanatory nature of the models.

<!-- b000851 | heading | pages [24] -->
Weakness:

<!-- b000852 | prose | pages [24] -->
Our model’s ability to capture non-linear relationships in the data needs to be improved.Thus,

<!-- b000853 | prose | pages [24] -->
enhancing the model’s depiction of non-linearity will be an important direction for future improvements.

<!-- b000854 | prose | pages [24] -->
REFERENCE

<!-- b000855 | prose | pages [24] -->
[1] Pilar Poncela.Time series analysis by state space methods: J. Durbin and S.J. Koopman, Oxford

<!-- b000856 | prose | pages [24] -->
Statistical Series 24, 2001, Oxford University Press, ISBN 0-19-852354-8, 254 pages, price:

<!-- b000857 | prose | pages [24] -->
￡36.00 (hardback)[J].International Journal of Forecasting,2004,Vol.20(1): 139-141

<!-- b000858 | prose | pages [24] -->
[2] Manner, H. (2015). Modeling and forecasting the outcomes of NBA basketball games. Institute

<!-- b000859 | prose | pages [24] -->
of Econometrics and Statistics, University of Cologne.

<!-- b000860 | furniture | pages [24] -->
关注数学模型

<!-- b000861 | furniture | pages [24] -->
2

<!-- b000862 | furniture | pages [24] -->
MATHmodels

<!-- b000863 | furniture | pages [24] -->
获取更多资讯

<!-- b000864 | furniture | pages [25] -->
Team 2410482

<!-- b000865 | furniture | pages [25] -->
Page 24

<!-- b000866 | heading | pages [25] -->
Memorandum

<!-- b000867 | prose | pages [25] -->
To: The Coach

<!-- b000868 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000869 | prose | pages [25] -->
From: Team# 2410482

<!-- b000870 | prose | pages [25] -->
Subiect: Momentum: The Hidden Force in Tennis

<!-- b000871 | prose | pages [25] -->
Date: February 5,2024

<!-- b000872 | prose | pages [25] -->
Dear Sir or Madame:

<!-- b000873 | prose | pages [25] -->
Sports competitions are not just a contest of physical strength between two sides, but also a

<!-- b000874 | prose | pages [25] -->
psychological battle. To win, it’s not enough to simply lead in the score; one must also dominate the

<!-- b000875 | prose | pages [25] -->
mental. Every athlete faces three unavoidable issues, which are the keys to victory：

<!-- b000876 | prose | pages [25] -->
（a）How to hold on to a lead?

<!-- b000877 | prose | pages [25] -->
（b）How to fight back from hopeless positions?

<!-- b000878 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000879 | prose | pages [25] -->
（c）How to grasp opportunities that come your way?

<!-- b000880 | prose | pages [25] -->
To address these three issues, we must introduce the protagonist of today’s discussion: momentum.

<!-- b000881 | prose | pages [25] -->
The growth of momentum is the answer to the three aforementioned questions. By incorporating factors

<!-- b000882 | prose | pages [25] -->
that affect the morale in a tennis match, such as scoring on crucial points, consecutive points scored,

<!-- b000883 | prose | pages [25] -->
and unforced errors, we have constructed a mathematical model to quantitatively measure momentum.

<!-- b000884 | prose | pages [25] -->
Is momentum controllable? Some people describe it as momentum creeping in and creeping out

<!-- b000885 | prose | pages [25] -->
of the match.However, in fact, the flow of momentum can be controlled, just like the flow of water

<!-- b000886 | prose | pages [25] -->
can be controlled.We have analyzed voluminous datasets from real matches to see how momentum

<!-- b000887 | prose | pages [25] -->
correlates with common tennis statistics, such as points won at the net, aces, running distance, etc. We

<!-- b000888 | prose | pages [25] -->
found that each factor affects momentum changes to varying degrees. Notably, double faults and points

<!-- b000889 | prose | pages [25] -->
won at the net have a p-value less than 0.05, meaning we can be 95% confident that these factors are

<!-- b000890 | prose | pages [25] -->
correlated with shifts in momentum.

<!-- b000891 | prose | pages [25] -->
While improving athletes’ skills, also focus on their ability to read the game, seize and control

<!-- b000892 | prose | pages [25] -->
momentum. Our suggestions for match preparation include:

<!-- b000893 | prose | pages [25] -->
Divide athletes into two categories based on momentum: stable and variable. Against those with

<!-- b000894 | prose | pages [25] -->
variable momentum, exploit weaknesses with aggressive shots and force errors. Minimize short balls

<!-- b000895 | prose | pages [25] -->
to avoid giving smash opportunities. Against stable momentum opponents, emphasize the importance

<!-- b000896 | prose | pages [25] -->
of a strong start to control the match flow.

<!-- b000897 | prose | pages [25] -->
Finally, we hope our insights into momentum prove helpful to you. Sincerely, we wish your

<!-- b000898 | prose | pages [25] -->
athletes greater success!

<!-- b000899 | furniture | pages [25] -->
关注数学模型

<!-- b000900 | furniture | pages [25] -->
2

<!-- b000901 | furniture | pages [25] -->
MATHmodels

<!-- b000902 | furniture | pages [25] -->
获取更多资讯

<!-- b000903 | furniture | pages [26] -->
Team 2410482

<!-- b000904 | furniture | pages [26] -->
Page 25

<!-- b000905 | heading | pages [26] -->
Report on Use of AI

<!-- b000906 | ai_disclosure | pages [26] -->
•We used ChatGPT 4 for English touch-ups throughout the text, but it was reviewed and revised

<!-- b000907 | ai_disclosure | pages [26] -->
微信公众号：数学模型

<!-- b000908 | ai_disclosure | pages [26] -->
by the team.

<!-- b000909 | ai_disclosure | pages [26] -->
•We used ChatGPT4 to help us understand the State Space Model and Kalman Filter Algorithm,

<!-- b000910 | ai_disclosure | pages [26] -->
and referenced parts of the Model introduction, all of which were manually reviewed.

<!-- b000911 | ai_disclosure | pages [26] -->
微信号：MATHmodels

<!-- b000912 | furniture | pages [26] -->
关注数学模型

<!-- b000913 | furniture | pages [26] -->
2

<!-- b000914 | furniture | pages [26] -->
MATHmodels

<!-- b000915 | furniture | pages [26] -->
获取更多资讯
