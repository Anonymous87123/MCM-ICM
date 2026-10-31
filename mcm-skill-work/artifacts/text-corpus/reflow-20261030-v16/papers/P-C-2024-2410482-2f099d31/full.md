# P-C-2024-2410482-2f099d31

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
and momentum—the former indicating match situation favorability, the latter control over game dynamics.Subsequently, utilizing the Markov Model for winning probability calculations, we estimated win chances using conditional probabilities. Crucially, we rigorously defined the abstract concept of momentum, incorporating the significance variance of individual points, and identifying

<!-- b000017 | title | pages [1] -->
微信号：MATHmodels

<!-- b000018 | prose | pages [1] -->
closely related factors.

<!-- b000019 | prose | pages [1] -->
For task 2, We translate randomness into the question of whether momentum effects are significant.Utilizing hypothesis testing and logistic regression, we find momentum significantly correlated with player performance, evidenced by a t-statistic for momentum yielding a p-value well below 0.05 and a 95% confidence interval for the coefficient that excludes zero.

<!-- b000020 | prose | pages [1] -->
For task 3, Employing State Space Model and Kalman Filter, our model not only forecasts springs in momentum with superior accuracy compared to the ARIMAR model but also offers en- hanced mathematical interpretability over machine learning algorithms, demonstrating exceptional predictive outcomes in our final assessment.Based on this, we analyze factors related to momentum swings and provide corresponding recommendations.

<!-- b000021 | prose | pages [1] -->
For task 4, to evaluate the universality of our model, we selected a women’s tennis match and a women’s table tennis match for analysis, achieving a low MSE of 0.051 in women’s tennis predictions.Upon examining inaccuracies in both cases, we identified that enhancing the model’s depiction of non-linearity will be an important direction for future improvements.

<!-- b000022 | prose | pages [1] -->
We also conduct sensitivity analysis, which shows how different samples affect the word state space model.And then the strengths and weaknesses of our model are summarized.Finally, a memo to coaches presenting the overall ideas and results about momentum is written at the end of the paper.

<!-- b000023 | keywords | pages [1] -->
Keywords:Momentum;Markov Chain;Hypothesis testing;State Space Model;Kalman Filter Al-

<!-- b000024 | prose | pages [1] -->
gorithm

<!-- b000025 | furniture | pages [1] -->
关注数学模型

<!-- b000026 | furniture | pages [1] -->
2

<!-- b000027 | furniture | pages [1] -->
MATHmodels

<!-- b000028 | furniture | pages [1] -->
获取更多资讯

<!-- b000029 | heading | pages [2] -->
CONTENT

<!-- b000030 | contents | pages [2] -->
1 Introduction

<!-- b000031 | contents | pages [2] -->
2

<!-- b000032 | contents | pages [2] -->
1.1

<!-- b000033 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
2

<!-- b000035 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000036 | contents | pages [2] -->
1.2

<!-- b000037 | contents | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
2

<!-- b000039 | contents | pages [2] -->
1.3

<!-- b000040 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
3

<!-- b000042 | contents | pages [2] -->
1.4

<!-- b000043 | contents | pages [2] -->
Data Resource . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
3

<!-- b000045 | contents | pages [2] -->
2 Assumptions and Justifications

<!-- b000046 | contents | pages [2] -->
3

<!-- b000047 | contents | pages [2] -->
3 Notation

<!-- b000048 | contents | pages [2] -->
4

<!-- b000049 | contents | pages [2] -->
4

<!-- b000050 | contents | pages [2] -->
4 Assessing Player Performance within Match Flow

<!-- b000051 | contents | pages [2] -->
4.1

<!-- b000052 | contents | pages [2] -->
Model I:Markov Model to Predict Win Probabilities . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
5

<!-- b000054 | contents | pages [2] -->
4.1.1

<!-- b000055 | contents | pages [2] -->
Explanation of the Serving Scoring

<!-- b000056 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
5

<!-- b000058 | contents | pages [2] -->
4.1.2

<!-- b000059 | contents | pages [2] -->
Establishment and Predictive Outcomes of the Markov Model

<!-- b000060 | contents | pages [2] -->
. . . . . . . . .

<!-- b000061 | contents | pages [2] -->
5

<!-- b000062 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000063 | contents | pages [2] -->
4.2

<!-- b000064 | contents | pages [2] -->
Searching for the Defination of Momentum

<!-- b000065 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
7

<!-- b000067 | contents | pages [2] -->
4.2.1

<!-- b000068 | contents | pages [2] -->
How to Quantify Momentum? . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
7

<!-- b000070 | contents | pages [2] -->
4.2.2

<!-- b000071 | contents | pages [2] -->
The Defination of Momentum . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
9

<!-- b000073 | contents | pages [2] -->
10

<!-- b000074 | contents | pages [2] -->
5 Is It Random? Measuring the Significance of Momentum Effecs

<!-- b000075 | contents | pages [2] -->
5.1

<!-- b000076 | contents | pages [2] -->
Analysis and Methodology Overview . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
10

<!-- b000078 | contents | pages [2] -->
5.2

<!-- b000079 | contents | pages [2] -->
Parameter Estimation: Based on MLE . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
11

<!-- b000081 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
5.3

<!-- b000083 | contents | pages [2] -->
The Result of Regression and Hypothesis Testing

<!-- b000084 | contents | pages [2] -->
12

<!-- b000085 | contents | pages [2] -->
6 Momentum Projections,Influencing Factors and Recommendations

<!-- b000086 | contents | pages [2] -->
13

<!-- b000087 | contents | pages [2] -->
6.1

<!-- b000088 | contents | pages [2] -->
Prediction of the Momentum and Swings

<!-- b000089 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
13

<!-- b000091 | contents | pages [2] -->
6.1.1

<!-- b000092 | contents | pages [2] -->
Introduction to State Space Model and Kalman Filter Algorithm . . . . . . . .

<!-- b000093 | contents | pages [2] -->
13

<!-- b000094 | contents | pages [2] -->
6.1.2

<!-- b000095 | contents | pages [2] -->
Building Predictive Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
15

<!-- b000097 | contents | pages [2] -->
6.1.3

<!-- b000098 | contents | pages [2] -->
Prediction Results and Analysis

<!-- b000099 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
16

<!-- b000101 | contents | pages [2] -->
Model Evaluation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
6.1.4

<!-- b000103 | contents | pages [2] -->
17

<!-- b000104 | contents | pages [2] -->
6.2

<!-- b000105 | contents | pages [2] -->
Correlation Analysis

<!-- b000106 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [2] -->
17

<!-- b000108 | contents | pages [2] -->
6.3

<!-- b000109 | contents | pages [2] -->
Suggestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [2] -->
18

<!-- b000111 | contents | pages [2] -->
6.3.1

<!-- b000112 | contents | pages [2] -->
Suggestions for Players with Strong Momentum . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [2] -->
19

<!-- b000114 | contents | pages [2] -->
6.3.2

<!-- b000115 | contents | pages [2] -->
Suggestions for Relatively Stable Momentum . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
19

<!-- b000117 | contents | pages [2] -->
Extension Test ——In Women’s Tennis and Table Tennis Matches

<!-- b000118 | contents | pages [2] -->
7

<!-- b000119 | contents | pages [2] -->
19

<!-- b000120 | contents | pages [2] -->
7.1

<!-- b000121 | contents | pages [2] -->
Scenario of Women’s Tennis Matches

<!-- b000122 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
20

<!-- b000124 | contents | pages [2] -->
7.2

<!-- b000125 | contents | pages [2] -->
Scenario of Table Tennis Matches

<!-- b000126 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000127 | contents | pages [2] -->
21

<!-- b000128 | contents | pages [2] -->
8 Sensitivity Analysis

<!-- b000129 | contents | pages [2] -->
22

<!-- b000130 | contents | pages [2] -->
9 Strengths and Weakness

<!-- b000131 | contents | pages [2] -->
23

<!-- b000132 | furniture | pages [2] -->
关注数学模型

<!-- b000133 | furniture | pages [2] -->
1

<!-- b000134 | furniture | pages [2] -->
2

<!-- b000135 | furniture | pages [2] -->
MATHmodels

<!-- b000136 | furniture | pages [2] -->
获取更多资讯

<!-- b000137 | furniture | pages [3] -->
Team 2410482

<!-- b000138 | furniture | pages [3] -->
Page 2

<!-- b000139 | heading | pages [3] -->
1 Introduction

<!-- b000140 | heading | pages [3] -->
1.1 Background

<!-- b000141 | prose | pages [3] -->
微信公众号：数学模型 In the evolving landscape of sports, technological advancements have greatly enhanced the analysis of athletes’ performances, focusing primarily on outcomes like scores. However, this approach often overlooks the analysis of a player’s in-game state. To improve predictions of scoring trends and devise effective strategies, it’s crucial to study a player’s "momentum". Momentum, a psychological

<!-- b000142 | prose | pages [3] -->
edge gained through consecutive wins, can significantly affect an opponent’s confidence and play.

<!-- b000143 | prose | pages [3] -->
Understanding and leveraging momentum is vital for success in tennis and other sports, as it influences

<!-- b000144 | prose | pages [3] -->
a player’s confidence, aggression, and overall performance.

<!-- b000145 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000146 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000147 | prose | pages [3] -->
Considering the background information and restricted conditions identified in the problem state- ment, we need to solve the following problems:

<!-- b000148 | prose | pages [3] -->
• Create a model using data from the 2023 Wimbledon men’s matches to analyze the dynamics of match play, identify the leading player at any moment, and quantify their performance advantage. Additionally, visualize match flows to illustrate our findings, applying this model to selected matches.

<!-- b000149 | prose | pages [3] -->
• Evaluate the validity of momentum in tennis, examining whether patterns of success or shifts in play are random or influenced by momentum.

<!-- b000150 | prose | pages [3] -->
• Develop a predictive model based on match data to identify factors influencing play dynamics and suggest strategies for players entering new matches, considering previous momentum shifts.

<!-- b000151 | prose | pages [3] -->
• Assess the model’s performance across different matches, pinpoint necessary enhancements, and evaluate its suitability for other analytical endeavors.

<!-- b000152 | prose | pages [3] -->
• Summarize the findings in a concise two-page memo, providing coaching advice on utilizing momentum and preparing for events affecting match dynamics.

<!-- b000153 | furniture | pages [3] -->
关注数学模型

<!-- b000154 | furniture | pages [3] -->
2

<!-- b000155 | furniture | pages [3] -->
MATHmodels

<!-- b000156 | furniture | pages [3] -->
获取更多资讯

<!-- b000157 | furniture | pages [4] -->
Team 2410482

<!-- b000158 | furniture | pages [4] -->
Page 3

<!-- b000159 | heading | pages [4] -->
1.3 Our Work

<!-- b000160 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000161 | caption | pages [4] -->
Figure 1: Our Work

<!-- b000162 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000163 | heading | pages [4] -->
1.4 Data Resource

<!-- b000164 | prose | pages [4] -->
Match Website

<!-- b000165 | prose | pages [4] -->
Woman’s tennis match https://www.wimbledon.com/ Table tennis match https://www.kaggle.com/datasets

<!-- b000166 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000167 | prose | pages [4] -->
To simplify our modeling, we make the following assumptions:

<!-- b000168 | prose | pages [4] -->
Assumption 1:Recent performance is indicative of future performance Justification:This means that if an athlete has performed well in their most recent competition

<!-- b000169 | prose | pages [4] -->
there is a higher likelihood that they will continue to perform well in their next competition.

<!-- b000170 | heading | pages [4] -->
Assumption 2:Stability of physical state

<!-- b000171 | prose | pages [4] -->
Justification:It is assumed that athletes’ fitness status isrelatively stable in the short term, such that strengths or weaknesses in fitness will continue to affecttheir performance in the following competitions.

<!-- b000172 | prose | pages [4] -->
Assumption 3:Our model has Markov Property Justification: the next state depends only on the current state and is independent of earlier states.

<!-- b000173 | furniture | pages [4] -->
关注数学模型

<!-- b000174 | furniture | pages [4] -->
2

<!-- b000175 | furniture | pages [4] -->
MATHmodels

<!-- b000176 | furniture | pages [4] -->
获取更多资讯

<!-- b000177 | furniture | pages [5] -->
Team 2410482

<!-- b000178 | furniture | pages [5] -->
Page 4

<!-- b000179 | heading | pages [5] -->
3 Notation

<!-- b000180 | prose | pages [5] -->
Symbol Explaination 微信公众号：数学模型 𝑝𝐴𝐵 A’s service score rate when A has a match with B 𝑞𝐴𝐵 A’s receive points score rate when A has a match with B 𝐿 The leberage of a game 𝑀 The value of momentum 𝜔 the coefficient to measure momentum 𝛽 the coefficient of logistic regression equation 𝑊 the swings of winning probability The corresponding variances of 𝑀𝑡conditional on information at time t-1 Σ𝑡|𝑡−1

<!-- b000181 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000182 | heading | pages [5] -->
4 Task 1: Assessing Player Performance within Match Flow

<!-- b000183 | prose | pages [5] -->
For play’s performance at a given time, we measure it from two different angles——winning rate and momentum.The winning rate excludes any psychological factors, outside factors, and strictly introduces the advantages and disadvantages of the situation from a mathematical point of view according to the ability of both sides, while momentum shows the player’s ability to control the situation on the field.

<!-- b000184 | caption | pages [5] -->
Figure 2: relationship between player performance and winning percentage & momentum

<!-- b000185 | furniture | pages [5] -->
关注数学模型

<!-- b000186 | furniture | pages [5] -->
2

<!-- b000187 | furniture | pages [5] -->
MATHmodels

<!-- b000188 | furniture | pages [5] -->
获取更多资讯

<!-- b000189 | furniture | pages [6] -->
Team 2410482

<!-- b000190 | furniture | pages [6] -->
Page 5

<!-- b000191 | heading | pages [6] -->
4.1 Model I:Markov Model to Predict Win Probabilities

<!-- b000192 | heading | pages [6] -->
4.1.1 Explanation of the Serving Scoring

<!-- b000193 | prose | pages [6] -->
微信公众号：数学模型 Considering that there is A big difference in the scoring rate between the receiving side and the serving side in tennis match, we cannot use the same scoring rate to measure the serving and receiving situations. Instead, we use two different symbols 𝑝𝐴𝐵, 𝑞𝐴𝐵to measure the serving and receiving scoring rate of A in the match between A and B respectively.

<!-- b000194 | prose | pages [6] -->
In the match between A and B, A’s service scoring rate 𝑝𝐴𝐵is related to A’s service level and B’s service receiving level, which can be defined by the mean of A’s career average service scoring rate 𝑝𝐴𝐵and B’s career average service scoring rate 𝑞𝐵can i.e. :

<!-- b000195 | prose | pages [6] -->
𝑝𝐴𝐵= 𝑝𝐴+ 𝑞𝐵 + 𝑒 (1) 2 微信号：MATHmodels e is the amendment item, which is changed according to the different situations of the two sides. In the same way:

<!-- b000196 | prose | pages [6] -->
𝑞𝐴𝐵= 𝑞𝐴+ 𝑝𝐵 + 𝑒 (2) 2

<!-- b000197 | heading | pages [6] -->
4.1.2 Establishment and Predictive Outcomes of the Markov Model

<!-- b000198 | prose | pages [6] -->
To calculate the probability of winning at a certain moment, we introduce The Markov Model.

<!-- b000199 | prose | pages [6] -->
In processes where future outcomes depend solely on the current state and not on past con- ditions, such as tennis matches, the calculation of winning probabilities considers only the current score. Psychological and external factors are excluded, making the win probability directly tied to the present score. This scenario is suitable for analysis using Markov chains, which facilitate probability calculations through event transformation relationships. An example application is computing the win probability in a tennis match based on specific scores, illustrated by the following flow chart:

<!-- b000200 | caption | pages [6] -->
Figure 3: the flow chart of the Markov Model

<!-- b000201 | furniture | pages [6] -->
关注数学模型

<!-- b000202 | furniture | pages [6] -->
2

<!-- b000203 | furniture | pages [6] -->
MATHmodels

<!-- b000204 | furniture | pages [6] -->
获取更多资讯

<!-- b000205 | furniture | pages [7] -->
Team 2410482

<!-- b000206 | furniture | pages [7] -->
Page 6

<!-- b000207 | prose | pages [7] -->
The scores of A and B in the ongoing match are (𝑎, 𝑏), the ranges of which are shown in the following table:

<!-- b000208 | prose | pages [7] -->
微信公众号：数学模型 0 1 2 3 4 5 0 (0,0) (1,0) (2,0) (3,0) (4,0) none 1 (0,1) (1,1) (2,1) (3,1) (4,1) none 2 (0,2) (1,2) (2,2) (3,2) (4,2) none 3 (0,3) (1,3) (2,3) (3,3) (4,3) (5,3) 4 (0,4) (1,4) (2,4) (3,4) (4,4) none 5 none none none (3,5) none none

<!-- b000209 | prose | pages [7] -->
1,2, and 3 in the table above represent the actual score of 15,30,and 40 respectively.(4,3),(3,4) respec- 微信号：MATHmodels tively represent the two sides scored AD, while special scores (4,4),(5,3) represent the equalizer and another goal after AD to win the game. In particular , the actual probability of winning the game after (4,3) and (3,4) is the same as (3,2) and (2,3) and the probability of winning the game after (3,3) and (4,4) is the same as (2,2). What’s more, the case which scores one more point after (4,3) to get (5,3) and wins the game is equivalent to the case which scores one more point after (3,2) to get (4,2) and win the game. Therefore, although in the table lists there are special score (3, 4), (4, 3), (3, 3), (3, 3), (5, 3), (4, 4) , these six special cases do not appear in the Markov model flow chart.

<!-- b000210 | prose | pages [7] -->
On the basis of the above descriptions, the following formulas can be listed according to Markov model and conditional probability formula:

<!-- b000211 | prose | pages [7] -->
𝑃(𝑎, 𝑏) = 𝑝∗𝑃(𝑎+ 1, 𝑏) + (1 −𝑝) ∗𝑃(𝑎, 𝑏+ 1) (3)

<!-- b000212 | prose | pages [7] -->
P(a,b) in the formula above represents the probability of winning the game under the score (a,b), and p represents the probability of winning a ball (varies according to the server). According to the above formula, the probability of winning the game under any score can be obtained by backward recursion.

<!-- b000213 | prose | pages [7] -->
Similarly, the Markov model can be used to find the probability of winning the whole game at any score. This probability can be used to measure the advantages and disadvantages on the tennis court. Based on the given data of the 2023 Wimbledon Gentlemen’s final and the data of career average serving point rate and receiving point rate of Carlos Alcaraz and Novak Djokovic, we used the Markov model to calculate the winning rate of both players at every moment on the court, as shown in the figure below:

<!-- b000214 | furniture | pages [7] -->
关注数学模型

<!-- b000215 | furniture | pages [7] -->
2

<!-- b000216 | furniture | pages [7] -->
MATHmodels

<!-- b000217 | furniture | pages [7] -->
获取更多资讯

<!-- b000218 | furniture | pages [8] -->
Team 2410482

<!-- b000219 | furniture | pages [8] -->
Page 7

<!-- b000220 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000221 | caption | pages [8] -->
Figure 4: 2023 Wimbledon Gentlemen’s singles final winning final chart

<!-- b000222 | prose | pages [8] -->
As can be seen from the picture, the match experienced ups and downs. Novak Djokovic occupied the advantage of the match during 1-21 games, but after 21 games, the wind changed and Carlos Alcaraz, 微信号：MATHmodels who had been lagging behind, gained the initiative. However, after Novak Djokovic’s tenacious chase, the two sides were almost back on the same starting line in the 38th game, and at last Carlos Alcaraz again took the fight to the win. The result of accurate probability calculation is also consistent with people’s intuitive perception of the game, so it can be seen that the winning rate chart can reflect the situation on the field to a large extent.

<!-- b000223 | heading | pages [8] -->
4.2 Searching for the Defination of Momentum

<!-- b000224 | prose | pages [8] -->
4.2.1 How to Quantify Momentum?

<!-- b000225 | prose | pages [8] -->
In the dictionary, one definition of momentum is "strength or force gained by motion or by a series of events". In sports, we can always clearly feel the momentum of the team that has scored consecutive

<!-- b000226 | prose | pages [8] -->
points, which will produce a mysterious force to make it full of motivation. However, when we talk

<!-- b000227 | prose | pages [8] -->
about momentum, we are more of an abstract understanding of things. In order to make the data of

<!-- b000228 | prose | pages [8] -->
game play a bigger role, our job is to quantify momentum. First, we must consider what momentum is

<!-- b000229 | prose | pages [8] -->
associated with.

<!-- b000230 | prose | pages [8] -->
• Scores Consecutive Points In sports games, often the side that scores consecutive points will gain momentum and gain a psychological lead in the game.

<!-- b000231 | prose | pages [8, 9] -->
We use the number of scoring consecutive points to show the degree of scoring consecutive points. If the opponent scores consecutive points, the index of scoring consecutive points is the opposite number of consecutive points of the opponent. However, the influence of the number of scoring consecutive scores on the momentum should not be proportional, because there is a law of ”diminishing marginal utility” in economics, which indicates that the increment of consumer satisfaction shows a decreasing law with the increase of consumption quantity. Therefore, we measure the effect of scoring consecutive 2 −𝑒−𝑥 𝑥 points on momentum by applying the odd function𝑣= 𝑓(𝑥) = 𝑡𝑎𝑛ℎ( 𝑥 2) = 𝑒 2 2 whose derivative 2 +𝑒−𝑥 𝑥 𝑒 decreases and converges to 0 at 𝑥> 0. 微信公众号：数学模型

<!-- b000232 | furniture | pages [8] -->
关注数学模型

<!-- b000233 | furniture | pages [8] -->
2

<!-- b000234 | furniture | pages [8] -->
MATHmodels

<!-- b000235 | furniture | pages [8] -->
获取更多资讯

<!-- b000236 | furniture | pages [9] -->
Team 2410482

<!-- b000237 | furniture | pages [9] -->
Page 8

<!-- b000239 | prose | pages [9] -->
• The Number of Consecutive Win of Games and The Importance of Each Game In addition to scoring consecutive points, winning consecutive games also greatly increases momentum, and the more crucial the games win, the greater the momentum increases.

<!-- b000240 | prose | pages [9] -->
To measure the importance of each game, we defined a new metric called "Leberage".In ordert

<!-- b000241 | prose | pages [9] -->
o better illustrate Leberage’s definition, I will give an example before giving the formula:

<!-- b000242 | prose | pages [9] -->
A tennis match of two players A and B is going to the key moment to decide the outcome which means the set points of both sides are tied 2:2 and the game points are also 6:6 into the tiebreak. At this time, the player who wins the game will get the victory. In other words, if A wins the game, A’s probability of winning the match will become 1, and if A loses the game, A’s probability of winning the 微信号：MATHmodels match will become 0. So, the outcome of this game will make the change of the winning probability up to 100%.

<!-- b000243 | prose | pages [9] -->
Think about another scenario, the tennis match just started, the two sides launched the first set of the game, if A wins, the winning rate of the game increases from 0.5 to 0.6, if A loses, the winning rate of the game is only reduced to 0.4, and there is still a great chance to reverse the game. The influence of this game on the winning rate is only 0.6-0.4=0.2. In other words, Leberage can be defined as "winning rate difference". Here is Leberage 𝐿𝑎for 𝑔𝑎𝑚𝑒𝑎:

<!-- b000244 | prose | pages [9] -->
𝐿𝑎= 𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑤𝑖𝑛𝑔𝑎𝑚𝑒𝑎) −𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑙𝑜𝑠𝑠𝑔𝑎𝑚𝑒𝑎) (4)

<!-- b000245 | prose | pages [9] -->
𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑤𝑖𝑛𝑔𝑎𝑚𝑒𝑎) and 𝑃(𝑤𝑖𝑛𝑡ℎ𝑒𝑚𝑎𝑡𝑐ℎ|𝑙𝑜𝑠𝑠𝑔𝑎𝑚𝑒𝑎) in the formula above represent the conditional probability of winning the match under the condition of winning and losing the game respectively. The introduction of Markov Model in the previous chapter provides a shortcut for calculating conditional probability.

<!-- b000246 | prose | pages [9] -->
After defining leberage, we can measure momentum by combining two metrics consecutive wins and the importance of different games together. Considering that sets closer to the current time have more influence on the current momentum, we weighted Leberage exponentially to get the following indicator 𝑢𝑡:

<!-- b000247 | prose | pages [9] -->
𝑢𝑡= 𝐿𝑡−1(−1)𝑟𝑡−1 + (1 −𝛼)𝐿𝑡−2(−1)𝑟𝑡−2 + (1 −𝛼)2𝐿𝑡−3(−1)𝑟𝑡−3 + ...... + (1 −𝛼)𝑡−2𝐿1 (5) 1 + (1 −𝛼) + (1 −𝛼)2 + ...... + (1 −𝛼)𝑡−2

<!-- b000248 | prose | pages [9, 10] -->
𝐿𝑡indicates the Leberage corresponding to set t. 𝑟𝑡represents victory in set t and is a 0-1 variable , which means that 0 is taken if set t won and 1 is taken if set t lost. In addition, 𝛼is the corresponding coefficient of Lerberage, and the change of its value affects the weight of Lerberage at different times. For ease of calculation, in this article 𝛼is always the constant value 0.33. 微信公众号：数学模型 In fact, the rise of momentum is not just a short-term trend across a few balls, but also a long-term trend across a few sets or even a few matches. This is also well reflected in our factor considerations, where consecutive points determine the short-term trend of momentum, and consecutive wins determine the long-term trend of momentum.

<!-- b000249 | furniture | pages [9] -->
关注数学模型

<!-- b000250 | furniture | pages [9] -->
2

<!-- b000251 | furniture | pages [9] -->
MATHmodels

<!-- b000252 | furniture | pages [9] -->
获取更多资讯

<!-- b000253 | furniture | pages [10] -->
Team 2410482

<!-- b000254 | furniture | pages [10] -->
Page 9

<!-- b000256 | prose | pages [10] -->
• Other Factors There are other factors that affect momentum.The variables include:

<!-- b000257 | prose | pages [10] -->
1.Presence of unforced errors in the previous point (x), with values 0,1,-1.Where 0 indicates no unforced errors by either player, 1 signifies an unforced error by the player, and -1 denotes an unforced error by the opponent. 微信号：MATHmodels 2.Occurrence of a winner in the previous point (y), with a value range of 0,1,-1, adopting the same valuation method.

<!-- b000258 | prose | pages [10] -->
3.The current point being a game, set, or match point (z), with values 0,1,-1, using the same valuation approach.

<!-- b000259 | prose | pages [10] -->
The given data also contains many other factors, such as running distance, serving speed, etc., although they will also affect the situation and affect the trend of the score, they can not directly affect the momentum from the perspective of the players, so they are no longer considered here.

<!-- b000260 | heading | pages [10] -->
4.2.2 The Defination of Momentum

<!-- b000261 | prose | pages [10] -->
According to the five important factors we have listed, momentum is defined using a linear model, and the magnitude of momentum is represented by M, then:

<!-- b000262 | prose | pages [10] -->
𝑀𝑛= 𝜔𝑋𝑇+ 𝜀 (6)

<!-- b000263 | prose | pages [10] -->
𝜔isparameter matrix，namely𝜔= [𝜔1, 𝜔2, 𝜔3, 𝜔4, 𝜔5]，Xisfactormatrix,namely X= 𝑢∗ 𝑛, 𝑣∗ 𝑛, 𝑥∗ 𝑛, 𝑦∗ 𝑛, 𝑧∗   , 𝑛 𝑣∗ 𝑛, 𝑥∗ 𝑛, 𝑦∗ 𝑛, 𝑧∗ 𝑛represent the result of standardization on the corresponding value of 𝑢, 𝑥, 𝑦, 𝑧and their corresponding sequence at the n point,𝑢∗ 𝑛represents the result of standardization on the corresponding value of u and its corresponding sequence at the n point. 𝜀is a disturbing factor, which will change with the changes of athletes’ condition on the court, weather conditions and other objective factors. Here, we assume that it follows the normal distribution with the mean value of 0 and standard deviation of 𝜎,that is 𝜀∼𝑁(0, 𝜎2).

<!-- b000264 | prose | pages [10] -->
After comprehensively evaluating the influence of five factors on momentum, we set 𝜔= [0.5, 0.2, 0, 1, −0.1, 0.1].

<!-- b000265 | furniture | pages [10] -->
关注数学模型

<!-- b000266 | furniture | pages [10] -->
2

<!-- b000267 | furniture | pages [10] -->
MATHmodels

<!-- b000268 | furniture | pages [10] -->
获取更多资讯

<!-- b000269 | furniture | pages [11] -->
Team 2410482

<!-- b000270 | furniture | pages [11] -->
Page 10

<!-- b000271 | prose | pages [11] -->
Based on this model, we use the 2023 Wimbledon Gentlemen’s singles final as an example to plot the momentum trends of Novak Djokovic throughout the match:

<!-- b000272 | prose | pages [11] -->
微信公众号：数学模型 图5: momentum trends of Novak Djokovic in 2023 Wimbledon Gentlemen’s final 微信号：MATHmodels As can be seen from the figure, there are two ups and downs in momentum in terms of the general trend, and its ups and downs are roughly in line with the audience’s intuitive cognition of the game. Looking at the details, momentum fluctuates within a certain range depending on the specific circumstances of each point.

<!-- b000273 | heading | pages [11] -->
5 Is It Random? Measuring the Significance of Momentum Ef-

<!-- b000274 | prose | pages [11] -->
fects

<!-- b000275 | heading | pages [11] -->
5.1 Analysis and Methodology Overview

<!-- b000276 | prose | pages [11] -->
In light of the preliminary discussions and the model established, our initial hypothesis posits that "momentum"significantly influences outcomes within the context of the game, suggesting that an athlete’s victory correlates with momentum rather than being a mere product of random fluctuations in performance as suggested by the coach’s perspectives. To substantiate this assertion, we propose to employ hypothesis testing and logistic regression analysis as methodological approaches to elucidate the relationship between an athlete’s momentum and score.

<!-- b000277 | furniture | pages [11] -->
关注数学模型

<!-- b000278 | furniture | pages [11] -->
2

<!-- b000279 | furniture | pages [11] -->
MATHmodels

<!-- b000280 | furniture | pages [11] -->
获取更多资讯

<!-- b000281 | furniture | pages [12] -->
Team 2410482

<!-- b000282 | furniture | pages [12] -->
Page 11

<!-- b000283 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000284 | caption | pages [12] -->
Figure 6: flow chart

<!-- b000285 | prose | pages [12] -->
To effectively counter the coach’s argument and adhere to the principle of protecting the null hypothesis through hypothesis testing, we establish the following hypotheses:

<!-- b000286 | prose | pages [12] -->
Null Hypothesis(𝐻0): There is no significant relationship between M(momentum) and P(the scoring probability).

<!-- b000287 | prose | pages [12] -->
Alternative Hypothesis(𝐻1): There is a significant relationship between M(momentum)and 微信号：MATHmodels P(the scoring probability).

<!-- b000288 | prose | pages [12] -->
Subsequently, to explore whether there is a significant relationship between momentum and winning a game, we conduct a logistic regression analysis. the function form is shown as follows:

<!-- b000289 | prose | pages [12] -->
5 𝑃(𝑌= 1) ∑︁ 1 −𝑃(𝑌= 1) = 𝛽0 + 𝛽1𝑀+ 𝛽𝑖𝑋𝑖 ln (7) 𝑖=2

<!-- b000290 | prose | pages [12] -->
Let P refers to the scoring probability; 1-P refers to losing point probability, which is different from the previous winning rate, which refers to a certain match, but here refers to each point. 𝛽0 refers to intercept term which is a constant;𝛽1 refers to the coefficient of the impact of momentum on the probability of winning; M refers to momentum ; 𝑋𝑖(𝑖= 2, 3, 4, 5) refers to other control variables, which has no influence on momentum but may also correlate with scores,which represent running distance difference, serve speed, net points or no points, and winning rate, respectively, all of which are control variables 𝛽𝑖(𝑖= 2, 3, 4, 5) represents the coefficient of the impact of other control variables on the probability of winning.

<!-- b000291 | heading | pages [12] -->
5.2 Parameter Estimation: Based on MLE

<!-- b000292 | prose | pages [12] -->
Maximum Likelihood Estimation (MLE) is a key method in statistics for finding the best-fitting parameters in logistic regression, ensuring models accurately reflect observed data.In our parameter estimation, the formula for mle is as follows:

<!-- b000293 | prose | pages [12, 13] -->
𝑛 𝑌𝑖𝑙𝑜𝑔𝑃(𝑌𝑖= 1|𝑋𝑖) + (1 −𝑌𝑖)𝑙𝑜𝑔(1 −𝑃(𝑌𝑖= 1|𝑋𝑖)) ∑︁ ℓ(𝛽) =   (8) 𝑖=1 ℓ(𝛽) is the logarithmic likelihood function to be maximized;𝛽= [𝛽0, 𝛽1, 𝛽2, 𝛽3, 𝛽4, 𝛽5] is a matrix of parameter variables in logistic regression；𝑌𝑖is the 𝑖𝑡ℎobservation result of the dependent variable 𝑌；𝑋𝑖= [𝑋𝑖 1, 𝑋𝑖 2, 𝑋𝑖 3, 𝑋𝑖 4, 𝑋𝑖 5] is the matrix of the 𝑖𝑡ℎobservation of the independent variable.，The 微信公众号：数学模型 expression of 𝑃(𝑌𝑖= 1|𝑋𝑖) is as follows:

<!-- b000294 | furniture | pages [12] -->
关注数学模型

<!-- b000295 | furniture | pages [12] -->
2

<!-- b000296 | furniture | pages [12] -->
MATHmodels

<!-- b000297 | furniture | pages [12] -->
获取更多资讯

<!-- b000298 | furniture | pages [13] -->
Team 2410482

<!-- b000299 | furniture | pages [13] -->
Page 12

<!-- b000301 | prose | pages [13] -->
1 𝑃(𝑌𝑖= 1|𝑋𝑖) = (9) 1 + 𝑒−(𝛽0+𝛽1𝑋𝑖 1+......+𝛽5𝑋𝑖 5)

<!-- b000302 | prose | pages [13] -->
Based on the above formula, gradient descent method is adopted to optimize the parameters to find the maximum likelihood function, and the optimization formula is as follows：

<!-- b000303 | prose | pages [13] -->
𝛽𝑛𝑒𝑤= 𝛽𝑜𝑙𝑑+ 𝛾𝜕ℓ (10) 𝜕𝛽

<!-- b000304 | prose | pages [13] -->
𝛼is the optimized parameter. 微信号：MATHmodels

<!-- b000305 | heading | pages [13] -->
5.3 The Result of Regression and Hypothesis Testing

<!-- b000306 | prose | pages [13] -->
According to this model, the results we got are shown in the following table:

<!-- b000307 | prose | pages [13] -->
regression parameter the 95% confidence intervals variable name T-statistic p. value estimates of the regression parameters <0.001 momentum 1.500 35.347 (1.0052,1.9939) difference in moving -0.004 0.065 0.798 (-0.0316,0.0243) distance <0.001 server and serve speed 0.008 35.446 0.0052,0.0103) whether player won the point while at the -0.251 0.704 0.402 (-0.8384,-0.3358) net or not winning rate -1.994 7.613 0.006 (-3.4111,-0.5777) intercept 0.883 5.512 0.019

<!-- b000308 | prose | pages [13] -->
It can be seen that the p.value corresponding to the momentum T-statistic is much less than 0.05, and the 95% confidence interval of the 𝛽1 1 estimate does not contain 0. Therefore, we reject the null hypothesis 𝐻0, which means momentum has a significant relationship with score.

<!-- b000309 | furniture | pages [13] -->
关注数学模型

<!-- b000310 | furniture | pages [13] -->
2

<!-- b000311 | furniture | pages [13] -->
MATHmodels

<!-- b000312 | furniture | pages [13] -->
获取更多资讯

<!-- b000313 | furniture | pages [14] -->
Team 2410482

<!-- b000314 | furniture | pages [14] -->
Page 13

<!-- b000315 | heading | pages [14] -->
6 Momentum Projections,Influencing Factors and Recommenda-

<!-- b000316 | prose | pages [14] -->
tions 微信公众号：数学模型 In the previous chapters, we found the qualitative definition of momentum by consulting pro- fessional literature, and we gave the quantitative definition of momentum based on this to ensure the rationality of the quantitative definition. Since the State Space Model can directly model the state of the dynamic system that cannot be directly observed and capture the change of the system state over time, it is very suitable for the characteristics of potential energy in tennis match, and has great advantages compared with ARIMA for predicting observable measurements and some machine learning models with limited model explanation. Therefore, we will use the State Space Model and Kalman filter algorithm to predict the momentum that is difficult to be observed. We get that the predicted result is highly consistent with the defined result, which further ensures the rationality of the definition of 微信号：MATHmodels potential energy. Then, the correlation analysis of momentum predictor and game factors (based on literature) was carried out, and we obtained that Net pt won, Winner,Ace were significantly correlated with momentum in a positive direction, and Unforced Errors, Break pt missed, Double fault was sig- nificantly correlated with momentum in a negative direction. Finally, based on the above conclusions, we give some suggestions.

<!-- b000317 | heading | pages [14] -->
6.1 Prediction of the Momentum and Swings

<!-- b000318 | heading | pages [14] -->
6.1.1 Introduction to State Space Model and Kalman Filter Algorithm

<!-- b000319 | prose | pages [14] -->
The State Space Model originated in the aerospace and control engineering fields in the 1950s to describe the state changes of dynamic systems and how to control the system state through 𝑖𝑛𝑝𝑢𝑡𝑠[1]. It is used to describe and analyze the dynamic behavior of the system, and has two outstanding characteristics: First, the State Space Model distinguishes the internal state of the system from the observed output. This allows it to handle situations where the internal state of the system may not be directly observable, estimating these hidden states from the observed data. Second, the State Space Model can be used to estimate the future state of the system based on the current and past states. These two features are very important for the context of this problem.

<!-- b000320 | prose | pages [14] -->
The State Space Model consists of two main equations:

<!-- b000321 | prose | pages [14] -->
State Equation: Describes the time evolution of the state of a system (usually not directly observ- able).

<!-- b000322 | prose | pages [14, 15] -->
𝑥𝑡+1 = 𝐴𝑥𝑡+ 𝐵𝑢𝑡+ 𝜔𝑡 (11) where 𝑥𝑡represents the state vector at time t,A is the state transition matrix,𝑢𝑡is the control input vector,B is the control input matrix,𝜔𝑡is the process noise, representing the model’s uncertainty.

<!-- b000323 | furniture | pages [14] -->
关注数学模型

<!-- b000324 | furniture | pages [14] -->
2

<!-- b000325 | furniture | pages [14] -->
MATHmodels

<!-- b000326 | furniture | pages [14] -->
获取更多资讯

<!-- b000327 | furniture | pages [15] -->
Team 2410482

<!-- b000328 | furniture | pages [15] -->
Page 14

<!-- b000330 | prose | pages [15] -->
Observation Equation：Describes how to measure the state of a system by means of observations 微信公众号：数学模型 containing noise.

<!-- b000331 | prose | pages [15] -->
𝑦𝑡= 𝐶𝑥𝑡+ 𝑣𝑡 (12)

<!-- b000332 | prose | pages [15] -->
where 𝑦𝑡represents the observation vector at time𝑡,𝐶is the observation matrix, 𝑣𝑡is the observation noise, accounting for measyrement errors.

<!-- b000333 | prose | pages [15] -->
We can understand the process of the State Space Model through the figure below, and it can be seen from the figure that the core of the State Space Model solving algorithm is Kalman filter.

<!-- b000334 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000335 | caption | pages [15] -->
Figure 7: schematic of the State Space Model

<!-- b000336 | prose | pages [15] -->
Since people’s subjective understanding (the theoretical state value generated by the establishment of mathematical models) and measurement (sensor and other measurement values) are not accurate, Kalman filter is introduced to infer the state of a linear dynamic system from a series of noise measurements, and the error of both is synthesized to obtain the optimal prediction of the true value. The essence of Kalman filtering algorithm is to use the property that the fusion of two normal distributions is still a normal distribution to iterate, which can be better understood through the following figure.

<!-- b000337 | caption | pages [15] -->
Figure 8: schematic of the Kalman filter

<!-- b000338 | furniture | pages [15] -->
关注数学模型

<!-- b000339 | furniture | pages [15] -->
2

<!-- b000340 | furniture | pages [15] -->
MATHmodels

<!-- b000341 | furniture | pages [15] -->
获取更多资讯

<!-- b000342 | furniture | pages [16] -->
Team 2410482

<!-- b000343 | furniture | pages [16] -->
Page 15

<!-- b000344 | prose | pages [16] -->
With the above foundation, understanding the mathematical expression of Kalman filtering be- comes very easy.

<!-- b000345 | prose | pages [16] -->
1.Prediction Phase:Before receiving the new measurement, the Kalman filter predicts the current 微信公众号：数学模型 state and error covariance based on the previous state:

<!-- b000346 | prose | pages [16] -->
( 𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑𝑠𝑡𝑎𝑡𝑒𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑒: 𝑥𝑡|𝑡−1 = 𝐴ˆ 𝑥𝑡−1 + 𝐵𝑢𝑡−1; ˆ (13) 𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑𝑒𝑟𝑟𝑜𝑟𝑐𝑜𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒: 𝑃𝑡|𝑡−1 = 𝐴𝑃𝑡−1|𝑡−1𝐴𝑇+ 𝑄

<!-- b000347 | prose | pages [16] -->
where Q is the process noise covariance matrix.

<!-- b000348 | prose | pages [16] -->
2.Update Phase:Upon receiving a new measurement 𝑦𝑡, the filter updates its estimates:

<!-- b000349 | prose | pages [16] -->
𝐾𝑎𝑙𝑚𝑎𝑛𝑔𝑎𝑖𝑛: 𝐾𝑡= 𝑃𝑡|𝑡−1𝐶𝑇(𝐶𝑃𝑡|𝑡−1𝐶𝑇+ 𝑅)−1;  𝑈𝑝𝑑𝑎𝑡𝑒𝑑𝑠𝑡𝑎𝑡𝑒𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑒: ˆ𝑥𝑡= 𝑥𝑡|𝑡−1 + 𝐾𝑡(𝑦𝑡−𝐶 𝑥𝑡|𝑡−1); (14) ˆ ˆ 微信号：MATHmodels  𝑈𝑝𝑑𝑎𝑡𝑒𝑑𝑒𝑟𝑟𝑜𝑟𝑐𝑜𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒: 𝑃𝑡= (𝐼−𝐾𝑡𝐶)𝑃𝑡|𝑡−1

<!-- b000350 | prose | pages [16] -->
where R is the observation noise covariance matrix.

<!-- b000351 | heading | pages [16] -->
6.1.2 Building Predictive Model

<!-- b000352 | prose | pages [16] -->
Based on 334 points of Novak Djokovic versus Carlos Alcaraz , we build the model through the following steps:

<!-- b000353 | heading | pages [16] -->
Step 1 Determining the State Space Model

<!-- b000354 | prose | pages [16] -->
We consider a state space model in which the momentum is a time-varying latent state process.In a match, the momentum of a player changes with the progress of the game, and because of the differences in the physical and mental qualities of the players themselves, the play on the court, and the situation they face, for a particular player, the momentum is assumed to follow an autoregressive process:

<!-- b000355 | prose | pages [16] -->
𝑀𝑡= 𝜇+ 𝜑𝑀𝑡−1 + 𝜔𝑡 (15)

<!-- b000356 | prose | pages [16] -->
Where 𝜇is a constant term,which serves as a baseline level that provides an initial value for 𝜑is the autoregressive coefficient and the disturbances are the subsequent optimization process. independently and identical distributed with𝜔𝑡∼𝑁(0, 𝜎2 𝜔).

<!-- b000357 | prose | pages [16] -->
In addition, we can assume that the swings in a player’s winning rate(𝑊𝑡) depend on momentum, where the swings in win percentage can be obtained by observation through the Markov Chain of Model I. At the same time, in our continuous optimization and updating of the model, we found that adding the service advantage correction 𝛿can significantly improve the fit degree of the predicted value and the defined value. The observation equation as follows:

<!-- b000358 | furniture | pages [16] -->
关注数学模型

<!-- b000359 | furniture | pages [16] -->
2

<!-- b000360 | furniture | pages [16] -->
MATHmodels

<!-- b000361 | furniture | pages [16] -->
获取更多资讯

<!-- b000362 | furniture | pages [17] -->
Team 2410482

<!-- b000363 | furniture | pages [17] -->
Page 16

<!-- b000364 | prose | pages [17] -->
𝑊𝑡= 𝛿+ 𝑀𝑡+ 𝜏𝑡 (16)

<!-- b000365 | prose | pages [17] -->
Where 𝑊𝑡refers to swings in winning rate,𝛿refers to service advantage corrections,𝑀𝑡refers to 微信公众号：数学模型 momentum.𝜏𝑡∼𝑁(0, 𝜎2 𝑡). Therefore,the state space model takes the form:

<!-- b000366 | prose | pages [17] -->
( 𝑆𝑡𝑎𝑡𝑒𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛: 𝑀𝑡= 𝑀𝑡= 𝜇+ 𝜑𝑀𝑡−1 + 𝜔𝑡 (17) 𝑂𝑏𝑠𝑒𝑟𝑣𝑎𝑡𝑖𝑜𝑛𝐸𝑞𝑢𝑎𝑡𝑖𝑜𝑛: 𝑊𝑡= 𝛿+ 𝑀𝑡+ 𝜏𝑡

<!-- b000367 | prose | pages [17] -->
Step 2 Implementation of the Kalman Filter Before implementing the Kalman filter, the prior mean and variance have to be defined.The initial 𝜎2 𝜇 mean is set to 𝑀1|0 = 𝜔 1−𝜙1 and initial covariance is Σ1|0 = 1,which are the conditional expectation 1−𝜑2 of the predicted momentum. Let 𝑀𝑡|𝑡−1be the predicted momentum for time 𝑡conditional on the 微信号：MATHmodels information obtained from time 𝑡−1. Furthermore, let 𝑀𝑡|𝑡denote the updated momentum conditional on the information obtained up to time𝑡. The corresponding variances of 𝑀𝑡conditional on information at time 𝑡−1 is denoted as Σ𝑡|𝑡−1and the updated variance is given byΣ𝑡|𝑡. 𝐺𝑘is defined by covariance and 𝜑2 𝑡simply for computational simplicity.Drawing from Manner’s work in 2015[2], the Kalman filter procedure employed for the dynamic state space model mentioned can be defined as follows: Prediction Step:

<!-- b000368 | prose | pages [17] -->
( 𝑀𝑡|𝑡−1 = 𝜇+ 𝜑𝑡𝑀𝑡−1|𝑡−1 (18) Σ𝑡|𝑡−1 = 𝜑2 𝑡Σ𝑡−1|𝑡−1 + 𝜎2 𝜔

<!-- b000369 | prose | pages [17] -->
Observation Step:

<!-- b000370 | prose | pages [17] -->
ˆ𝑦𝑡= 𝛿+ 𝑀𝑡|𝑡−1  𝐺𝑡= Σ𝑡|𝑡−1 + 𝜎2 (19) 𝑡  ˆ𝑒𝑡= 𝑦𝑡−ˆ𝑦𝑡

<!-- b000371 | prose | pages [17] -->
Updating Step:

<!-- b000372 | prose | pages [17] -->
𝑀𝑡|𝑡= 𝑀𝑡|𝑡−1 + ˆ𝑒𝑡Σ𝑡|𝑡−1  𝐺𝑡 (20) Σ2 𝑡|𝑡−1 Σ𝑡|𝑡= Σ𝑡|𝑡−1 −  𝐺𝑡

<!-- b000373 | heading | pages [17] -->
6.1.3 Prediction Results and Analysis

<!-- b000374 | prose | pages [17, 18] -->
Based on the establishment of the above model, we implement the model through R language to get the result. First,check that our object is a predictable object. Then, in the results we give, we get the momentum of Novak Djokovic, and the momentum of Carlos Alcaraz is opposite. At the same time, the athlete who is interested in momentum must also be interested in the change in momentum, because the momentum we predict is continuous, so we define the derivative at each point as the swings of momentum, which is calculated as M’. Momentum and the swings of momentum change over time are shown in the figure. The red realization shows the change in momentum over the course of the race, and the dashed blue line shows the change in swings of momentum over the course of the race. 微信公众号：数学模型

<!-- b000375 | furniture | pages [17] -->
关注数学模型

<!-- b000376 | furniture | pages [17] -->
2

<!-- b000377 | furniture | pages [17] -->
MATHmodels

<!-- b000378 | furniture | pages [17] -->
获取更多资讯

<!-- b000379 | furniture | pages [18] -->
Team 2410482

<!-- b000380 | furniture | pages [18] -->
Page 17

<!-- b000382 | caption | pages [18] -->
Figure 9: prognostic map

<!-- b000383 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000384 | heading | pages [18] -->
6.1.4 Model Evaluation

<!-- b000385 | prose | pages [18] -->
In this study, cross-validation was utilized to verify the accuracy of each model. Evaluation indicators, including Mean Square Error (MSE), Root Mean Square Error (RMSE), Mean Absolute Error (MAE), and R-squared (𝑅2) from cross-validation results. These indicators assess the accuracy of both the estimated and validated models, ensuring the reliability of the model assessments.

<!-- b000386 | prose | pages [18] -->
𝑅2 indicators MSE RMSE MAE

<!-- b000387 | prose | pages [18] -->
Predictive Model 0.0454 0.2131 0.1660 0.8902

<!-- b000388 | prose | pages [18] -->
In terms of the above evaluation indicators. MSE, RMSE, and MAE are all relatively low, while R-squared is close to 1, indicating that the model is a good fit and can explain most of the variability of the observed values. This shows that from the mathematical point of view, the model has good predictive performance.

<!-- b000389 | heading | pages [18] -->
6.2 Correlation Analysis

<!-- b000390 | prose | pages [18] -->
Based on the given data of the competition and the factors mentioned in the literature, we finally determined to do the correlation analysis between the swings of momentum and 12 factors,which is Un- forced Errors,Ace,Match Point,Distance run,Rally count,Winner,Double fault,Net pt,Net pt won, Break _pt,Break _pt _won,Break _pt _missed.

<!-- b000391 | furniture | pages [18] -->
关注数学模型

<!-- b000392 | furniture | pages [18] -->
2

<!-- b000393 | furniture | pages [18] -->
MATHmodels

<!-- b000394 | furniture | pages [18] -->
获取更多资讯

<!-- b000395 | furniture | pages [19] -->
Team 2410482

<!-- b000396 | furniture | pages [19] -->
Page 18

<!-- b000397 | prose | pages [19] -->
For whether the 12 factors are significantly correlated with the swings of momentum and the degree of correlation, we use P-value and Pearson correlation coefficient as analysis indicators. In terms of P value, 𝑃< 0.05 indicates that this factor is significantly correlated with momentum change. 微信公众号：数学模型 For Pearson correlation coefficient, 0 is the boundary, and the positive correlation increases as the value approaches 1, while the negative correlation increases as the value approaches -1. The data was imported into Origin and analyzed to obtain the following two correlation analysis charts:

<!-- b000398 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000399 | caption | pages [19] -->
Figure 10: Correlation Analysis figure1

<!-- b000400 | caption | pages [19] -->
Figure 11: Correlation Analysis figure2

<!-- b000401 | heading | pages [19] -->
6.3 Suggestions

<!-- b000402 | prose | pages [19] -->
Athletes usually need to conduct targeted research on the opponent’s skills and tactics before the game. If the momentum fluctuation of the opponent’s previous game is targeted research, it is conducive to occupy the advantage of the game in the psychological level. We divided the athletes into two different types according to the size of momentum fluctuation, namely, the type with strong momentum fluctuation and the type with relatively stable momentum.

<!-- b000403 | furniture | pages [19] -->
关注数学模型

<!-- b000404 | furniture | pages [19] -->
2

<!-- b000405 | furniture | pages [19] -->
MATHmodels

<!-- b000406 | furniture | pages [19] -->
获取更多资讯

<!-- b000407 | furniture | pages [20] -->
Team 2410482

<!-- b000408 | furniture | pages [20] -->
Page 19

<!-- b000409 | heading | pages [20] -->
6.3.1 Suggestions for Players with Strong Momentum

<!-- b000410 | prose | pages [20] -->
The momentum of a player with strong momentum fluctuations in a normal game often has ups 微信公众号：数学模型 and downs and fluctuations. This is a double-edged sword. Once the momentum is at the peak of the disadvantage, there is a great possibility to reverse the unfavorable situation, but at the same time, the advantage of the score is also easy to fall because of the opponent’s continuous score or the trough of the momentum, which is inadvertently reversed.

<!-- b000411 | prose | pages [20] -->
If the opponent is such a player, then the opponent is more likely to be affected by changes in the match situation. From the correlation analysis, we can see that the unforced errors and the waste of break points are negatively correlated with the swings of momentum, so we can seize the weakness of the opponent, play more aggressive balls, mobilize the opponent’s movement, and force the opponent to miss opportunities and make mistakes. The appearance of net points and winner is positively correlated 微信号：MATHmodels with the change of momentum, so we should play less short balls that fall in front of the net, do not give the opponent the chance to score in front of the net, and increase the defense ability.

<!-- b000412 | heading | pages [20] -->
6.3.2 Suggestions for Relatively Stable Momentum

<!-- b000413 | prose | pages [20] -->
Players tend to have relatively stable momentum throughout the game and are not prone to dramatic fluctuations. In the advantage situation, such players have strong ability to control and expand the advantage. In the disadvantageous situation, such players are also prone to the weakness of lack of toughness and lack of flipping ability.

<!-- b000414 | prose | pages [20] -->
When the opponent is such a player, the opening is particularly important. If seize the advantage in the opening, it is easy to achieve an overwhelming advantage in the whole game. It is difficult to reverse such an opponent if you start from a weak position. Therefore, it is necessary to take the lead in the opening, with a strong offensive play to gain momentum.

<!-- b000415 | prose | pages [20] -->
ExtensionTest ——InWomen’sTennisandTableTennisMatches 7

<!-- b000416 | prose | pages [20] -->
To evaluate the universality of our model, we selected a women’s tennis match and a women’s table tennis match for analysis. For details on the data sources, refer to Section 1.4, Data Sources.

<!-- b000417 | prose | pages [20] -->
In the women’s tennis match analysis, our model showed good predictive ability with potential for enhancement. By analyzing predictions and considering gender differences in tennis,we significantly enhanced the model’s fit by adjusting the service advantage correction coefficient(𝛿)，resulting in an exceptional predictive model.

<!-- b000418 | prose | pages [20, 21] -->
In the analysis of women’s table tennis, the model’s predictions, particularly for real-time trends and extremes, were suboptimal. Adjusting the autoregressive coefficient notably enhanced extreme value predictions, yet results remained less satisfactory compared to tennis predictions. Through analysis, we identified that accurately depicting nonlinear relationships will be crucial for the model’s future improvements. 微信公众号：数学模型

<!-- b000419 | furniture | pages [20] -->
关注数学模型

<!-- b000420 | furniture | pages [20] -->
2

<!-- b000421 | furniture | pages [20] -->
MATHmodels

<!-- b000422 | furniture | pages [20] -->
获取更多资讯

<!-- b000423 | furniture | pages [21] -->
Team 2410482

<!-- b000424 | furniture | pages [21] -->
Page 20

<!-- b000426 | heading | pages [21] -->
7.1 Scenario of Women’s Tennis Matches

<!-- b000427 | prose | pages [21] -->
We selected a match from the 2023 U.S. Open final between Coco Gauff and Aryna Sabalenka for our study. In this match,Coco Gauff overcame Aryna Sabalenka with a score of 2-6, 6-3, 6-2. This victory not only secured Gauff her first Grand Slam title but also positioned her as the new face of American tennis,echoing the legacy of Serena Williams. We first calculated Aryna Sabalenka’s momentum by definition given by us, which allowed us to derive Coco Gauff’s momentum accordingly. Subsequently, using Model II (we obtained the predicted values of momentum.) The results are 微信号：MATHmodels illustrated in the figure on the left "Before optimization":

<!-- b000428 | caption | pages [21] -->
Figure 12: Before and after change

<!-- b000429 | prose | pages [21] -->
The graph shows the actual momentum as a red curve and the predicted momentum in blue, highlighting close alignment at most points and indicating the predictive model’s consistency with reality. Notably, discrepancies between predictions and actual values are larger at the match’s start and end, likely due to the unpredictability of these phases and possible limitations in the metrics’ ability to capture the match’s dynamics, resulting in greater prediction errors. However, during the middle phase, the alignment improves, suggesting the model’s enhanced performance. Sharp deviations in actual momentum at the 60th and 120th points, not fully captured by predictions, may be attributed to unforeseen events or factors not accounted for in the model.

<!-- b000430 | prose | pages [21] -->
Following adjustments and optimizations to the original state space model, we significantly improved the model’s fit by changing 𝛿to 0.005(the service advantage correction coefficient in the observation equation: 𝑊𝑡= 𝛿+ 𝑀𝑡+ 𝜏𝑡) The results, depicted on the right side:"After optimization" suggest this improvement may be due to the format differences between men’s and women’s matches —men’s are typically best-of-five sets, while women’s are best-of-three. More sets in men’s matches could mean a larger dataset, potentially enabling more accurate long-term trend and pattern predictions.

<!-- b000431 | furniture | pages [21] -->
关注数学模型

<!-- b000432 | furniture | pages [21] -->
2

<!-- b000433 | furniture | pages [21] -->
MATHmodels

<!-- b000434 | furniture | pages [21] -->
获取更多资讯

<!-- b000435 | furniture | pages [22] -->
Team 2410482

<!-- b000436 | furniture | pages [22] -->
Page 21

<!-- b000437 | prose | pages [22] -->
Moreover, men’s tennis often focuses on power and service, whereas women’s tennis emphasizes strategy and variation in play. Thus, outcomes in men’s matches might be more dominated by top players, simplifying predictions to some extent. After adjusting the service advantage coefficient, 微信公众号：数学模型 the model’s fit improved significantly, with the prediction residuals showing 𝑀𝑆𝐸= 0.051,𝑀𝐴𝐸= 0.1932, and 𝑅2=0.8763, further proving the enhanced predictive effectiveness of our revised model.

<!-- b000438 | prose | pages [22] -->
Overall, the predictive curve generally follows the actual trend, despite deviations at certain points. Continuous experimentation and analysis of deviation causes significantly increased prediction accuracy.

<!-- b000439 | heading | pages [22] -->
7.2 Scenario of Table Tennis Matches

<!-- b000440 | prose | pages [22] -->
We selected a match from the 2020 WTT Macau International Table Tennis Tournament Women’s 微信号：MATHmodels Singles semifinals between Manyu Wang and Yingsha Sun.In the dazzling display at the 2020 WTT Macau, Sun Yingsha outplayed Wang Manyu 5-1 in the Women’s Singles, showcasing strategic mastery and securing a historic win in this premier event.

<!-- b000441 | prose | pages [22] -->
We firstly find out the momentum of Yingsha Sun through the definition, and accordingly we can get the momentum of Manyu Wang, and then we get the predicted value of momentum through Model II.The results are as follows:

<!-- b000442 | caption | pages [22] -->
Figure 13: Before and after change

<!-- b000443 | prose | pages [22] -->
The red curve represents the actual momentum values, while the blue curve represents the forecast momentum values. In most time series, the prediction curve closely follows the actual curve, indicating that the prediction model has a high ability to approximate the actual trend.However, the deviation between the two curves also reveals the limitation of the prediction accuracy of the model at a specific time, especially at the extreme point of the momentum.

<!-- b000444 | prose | pages [22, 23] -->
This deviation suggests that the model may need to incorporate more variables that affect the momentum of the game or to re-weight the existing variables in order to more accurately predict fluctuations in momentum during the game.Furthermore, this analysis may also indicate that the model’s ability to capture non-linear relationships in the data needs to be improved.Therefore, we adjusted the 𝜑(autoregressive coefficients) in the state equation of the original state space model to reduce the smoothness of predictions and increase the accuracy of extreme value estimation.However, we can still see that the effectiveness of the estimates needs to be enhanced. We speculate that this 微信公众号：数学模型 is due to the rapid and variable nature of table tennis matches, which requires the model to have a higher temporal resolution capability to capture the subtle dynamic changes in the game. Additionally, it necessitates the incorporation of non-linear relationship modeling. Thus, enhancing the model’s depiction of non-linearity will be an important direction for future improvements.

<!-- b000445 | furniture | pages [22] -->
关注数学模型

<!-- b000446 | furniture | pages [22] -->
2

<!-- b000447 | furniture | pages [22] -->
MATHmodels

<!-- b000448 | furniture | pages [22] -->
获取更多资讯

<!-- b000449 | furniture | pages [23] -->
Team 2410482

<!-- b000450 | furniture | pages [23] -->
Page 22

<!-- b000452 | heading | pages [23] -->
8 Sensitivity Analysis

<!-- b000453 | prose | pages [23] -->
In our prediction Model——State Space Model and Kalman Filter Algorithm, two constants of the State Equation and Observation Equation are highly correlated with the players themselves. Among 微信号：MATHmodels them, are the autoregressive coefficient 𝜑，which is related to the player’s personal ability, and the service advantage correction item 𝛿, which is related to the player’s service strength.

<!-- b000454 | prose | pages [23] -->
To test the sensitivity of our prediction model, State Space Model, we divided the remaining 30 players in the data set, except Carlos Alcaraz and Novak Djokovic, into 9 groups according to the two indexes of individual ability and service scoring rate, and ensured that the number of players in each group was 3 or 4. Individual ability and service scoring rate were both grouped from high to low and numbered 1,2,3. Each group of players used the State Space Model to predict the momentum change, and compared the predicted result with the calculated true value of the swings of momentum to obtain the prediction accuracy rate. Then, the average accuracy rate of each group members was taken as the numerical representative of the group and drawn into the following three-dimensional map:

<!-- b000455 | caption | pages [23] -->
Figure 14: Sensitivity Analysis

<!-- b000456 | prose | pages [23, 24] -->
As can be seen in the figure above, the average accuracy of group are all higher than 70%. The minimum value is 72% corresponding to service set 3-personal ability set 3, and the maximum value is 87% of service set 1-personal ability set 1. And whether it is individual ability or service scoring rate, the average accuracy rate increases with the decrease of group number, that is, the improvement 微信公众号：数学模型 of ability. Therefore, we can conclude that we have the high accuracy of the prediction model, the low sensitivity and the higher the player’s personal ability is, the better the prediction effect of the swings of momentum will be.

<!-- b000457 | furniture | pages [23] -->
关注数学模型

<!-- b000458 | furniture | pages [23] -->
2

<!-- b000459 | furniture | pages [23] -->
MATHmodels

<!-- b000460 | furniture | pages [23] -->
获取更多资讯

<!-- b000461 | furniture | pages [24] -->
Team 2410482

<!-- b000462 | furniture | pages [24] -->
Page 23

<!-- b000464 | heading | pages [24] -->
9 Strengths and Weakness

<!-- b000465 | heading | pages [24] -->
Strengths:

<!-- b000466 | prose | pages [24] -->
•Tennis matches are divided into points, sets and reels. A game consists of points, a set consists of different sets, and a match consists of different disks. This structure is well suited for modeling by 微信号：MATHmodels Markov method. The Markov model we apply accurately calculates the true winning percentage value.

<!-- b000467 | prose | pages [24] -->
•Our innovative binary definitions of winning percentage and momentum provide a comprehensive measure of player performance on a technical level, a situational level, and all aspects of psychological factors.

<!-- b000468 | prose | pages [24] -->
•Since state-space models can directly model the states of a dynamic system that cannot be directly observed and capture the change of the system state over time, they are very well suited to the characteristics of the potential energy in a tennis match, and have a great advantage over ARIMA, which makes predictions on observable measurements, and some machine learning models, which have a limited explanatory nature of the models.

<!-- b000469 | heading | pages [24] -->
Weakness:

<!-- b000470 | prose | pages [24] -->
Our model’s ability to capture non-linear relationships in the data needs to be improved.Thus, enhancing the model’s depiction of non-linearity will be an important direction for future improvements.

<!-- b000471 | heading | pages [24] -->
REFERENCE

<!-- b000472 | references | pages [24] -->
[1] Pilar Poncela.Time series analysis by state space methods: J. Durbin and S.J. Koopman, Oxford

<!-- b000473 | references | pages [24] -->
Statistical Series 24, 2001, Oxford University Press, ISBN 0-19-852354-8, 254 pages, price:

<!-- b000474 | references | pages [24] -->
￡36.00 (hardback)[J].International Journal of Forecasting,2004,Vol.20(1): 139-141

<!-- b000475 | references | pages [24] -->
[2] Manner, H. (2015). Modeling and forecasting the outcomes of NBA basketball games. Institute

<!-- b000476 | references | pages [24] -->
of Econometrics and Statistics, University of Cologne.

<!-- b000477 | furniture | pages [24] -->
关注数学模型

<!-- b000478 | furniture | pages [24] -->
2

<!-- b000479 | furniture | pages [24] -->
MATHmodels

<!-- b000480 | furniture | pages [24] -->
获取更多资讯

<!-- b000481 | furniture | pages [25] -->
Team 2410482

<!-- b000482 | furniture | pages [25] -->
Page 24

<!-- b000483 | heading | pages [25] -->
Memorandum

<!-- b000484 | prose | pages [25] -->
To: The Coach 微信公众号：数学模型 From: Team# 2410482 Subiect: Momentum: The Hidden Force in Tennis Date: February 5,2024 Dear Sir or Madame:

<!-- b000485 | prose | pages [25] -->
Sports competitions are not just a contest of physical strength between two sides, but also a psychological battle. To win, it’s not enough to simply lead in the score; one must also dominate the mental. Every athlete faces three unavoidable issues, which are the keys to victory： （a）How to hold on to a lead?

<!-- b000486 | prose | pages [25] -->
（b）How to fight back from hopeless positions? 微信号：MATHmodels （c）How to grasp opportunities that come your way?

<!-- b000487 | prose | pages [25] -->
To address these three issues, we must introduce the protagonist of today’s discussion: momentum. The growth of momentum is the answer to the three aforementioned questions. By incorporating factors that affect the morale in a tennis match, such as scoring on crucial points, consecutive points scored, and unforced errors, we have constructed a mathematical model to quantitatively measure momentum.

<!-- b000488 | prose | pages [25] -->
Is momentum controllable? Some people describe it as momentum creeping in and creeping out of the match.However, in fact, the flow of momentum can be controlled, just like the flow of water can be controlled.We have analyzed voluminous datasets from real matches to see how momentum correlates with common tennis statistics, such as points won at the net, aces, running distance, etc. We found that each factor affects momentum changes to varying degrees. Notably, double faults and points won at the net have a p-value less than 0.05, meaning we can be 95% confident that these factors are correlated with shifts in momentum.

<!-- b000489 | prose | pages [25] -->
While improving athletes’ skills, also focus on their ability to read the game, seize and control momentum. Our suggestions for match preparation include:

<!-- b000490 | prose | pages [25] -->
Divide athletes into two categories based on momentum: stable and variable. Against those with variable momentum, exploit weaknesses with aggressive shots and force errors. Minimize short balls to avoid giving smash opportunities. Against stable momentum opponents, emphasize the importance of a strong start to control the match flow.

<!-- b000491 | prose | pages [25] -->
Finally, we hope our insights into momentum prove helpful to you. Sincerely, we wish your athletes greater success!

<!-- b000492 | furniture | pages [25] -->
关注数学模型

<!-- b000493 | furniture | pages [25] -->
2

<!-- b000494 | furniture | pages [25] -->
MATHmodels

<!-- b000495 | furniture | pages [25] -->
获取更多资讯

<!-- b000496 | furniture | pages [26] -->
Team 2410482

<!-- b000497 | furniture | pages [26] -->
Page 25

<!-- b000498 | heading | pages [26] -->
Report on Use of AI

<!-- b000499 | ai_disclosure | pages [26] -->
•We used ChatGPT 4 for English touch-ups throughout the text, but it was reviewed and revised

<!-- b000500 | ai_disclosure | pages [26] -->
微信公众号：数学模型

<!-- b000501 | ai_disclosure | pages [26] -->
by the team.

<!-- b000502 | ai_disclosure | pages [26] -->
•We used ChatGPT4 to help us understand the State Space Model and Kalman Filter Algorithm,

<!-- b000503 | ai_disclosure | pages [26] -->
and referenced parts of the Model introduction, all of which were manually reviewed.

<!-- b000504 | ai_disclosure | pages [26] -->
微信号：MATHmodels

<!-- b000505 | furniture | pages [26] -->
关注数学模型

<!-- b000506 | furniture | pages [26] -->
2

<!-- b000507 | furniture | pages [26] -->
MATHmodels

<!-- b000508 | furniture | pages [26] -->
获取更多资讯
