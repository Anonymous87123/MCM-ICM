# P-C-2024-2401298-07d37078

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

<!-- b000006 | furniture | pages [1] -->
2401298

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
"Momentum" Exists In Tennis Game As Residual Effect -

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | title | pages [1] -->
A Dual-Temporal Bayesian Network Model

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
This study investigates tennis match dynamics through sophisticated statistical mod- eling and a novel Dual-Temporal Bayesian Network approach. By analyzing Wimble- don data, we address five key questions:

<!-- b000013 | prose | pages [1] -->
Performance Metrics (Problem 1): We introduce a server/returner reweighting strategy to accurately evaluate the performance of a player. We further utilize sliding window and Area Under Curve (AUC) methods to ensure continuity and locality, thus better capturing the fluctuations within the game.

<!-- b000014 | prose | pages [1] -->
Momentum Existence (Problem 2): Rigorous hypothesis testing (Ljung-Box Q Test and Runs Test) fails to reject null hypothesis of complete randomness. But instanta-

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
neous winning rates can reveal slight deviations from randomness, suggesting the presence of subtle momentum effects, albeit not overwhelmingly conclusive.

<!-- b000017 | prose | pages [1] -->
Momentum Prediction (Problem 3): We take a 2-step approach. We first separate out the momentum effect by considering it as the residual of a Naive Binomial Model. Subsequently, we develop a Dual-Temporal Bayesian Network Model to predict this residual effect. The network incorporates various latent variables such as physiology, perception, and self-efficacy. An additional outcome of this model is the calculation of the importance of factors on momentum through the reduction of information entropy.

<!-- b000018 | prose | pages [1] -->
Predictive Analysis (Problem 4): Our model is tested on the Wimbledon 2023 com- petition, where it successfully predicts most match fluctuations. We analyze instances of failure and propose potential future enhancements. The model framework is also applied to an additional dataset of female tennis matches, revealing intriguing dif- ferences. Most importantly, we generalize our data into a universal framework for predicting momentum in sports games.

<!-- b000019 | prose | pages [1] -->
Coaching Strategies (Memo) : Finally, we draft a memo for coaches, synthesiz- ing our findings into statistical findings and targeted recommendations of minimising errors, strategic aggression, resilience building, and more. Our goal is to offer a com- petitive advantage.

<!-- b000020 | prose | pages [1] -->
Our findings highlight the complexity of tennis match dynamics, combining rigor- ous statistical validation with sophisticated predictive modeling. Our model not only demonstrates effective prediction and significant robustness but is also broadly appli- cable across various sports scenarios.

<!-- b000021 | keywords | pages [1] -->
Keywords: Tennis, Momentum, Bayesian Networks, Statistical Analysis, Perfor-

<!-- b000022 | prose | pages [1] -->
mance Metrics.

<!-- b000023 | prose | pages [1] -->
关注数学模型

<!-- b000024 | furniture | pages [1] -->
2

<!-- b000025 | furniture | pages [1] -->
MATHmodels

<!-- b000026 | furniture | pages [1] -->
获取更多资讯

<!-- b000027 | furniture | pages [2] -->
Team # 2401298

<!-- b000028 | furniture | pages [2] -->
Page 2 of 25

<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | contents | pages [2] -->
1

<!-- b000031 | heading | pages [2] -->
Introduction

<!-- b000032 | prose | pages [2] -->
3 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000033 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000034 | prose | pages [2] -->
Clarifications and Restatements . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000035 | prose | pages [2] -->
2

<!-- b000036 | heading | pages [2] -->
Preparation for Modeling

<!-- b000037 | prose | pages [2] -->
3

<!-- b000038 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 Model Assumptions 4 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 4 Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 5

<!-- b000039 | prose | pages [2] -->
Problem 1: Probability Difference Evaluation Strategy 3 5 . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 Important Impact of Server 5 Sliding Point Interval Approach . . . . . . . . . . . . . . . . . . . . . . . . 3.2 3.3 Sliding Time Window Approach 6 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
7

<!-- b000041 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000042 | prose | pages [2] -->
4 Problem 2: Momentum Existence 8 Hypothesis Testing Preparation . . . . . . . . . . . . . . . . . . . . . . . . 4.1 8 Ljung-Box Q Test and Runs Test Statistical Analysis . . . . . . . . . . . . 4.2 9 Instantaneous Winning Rates . . . . . . . . . . . . . . . . . . . . . . . . . 4.3

<!-- b000043 | prose | pages [2] -->
5 Problem 3: Momentum Prediction

<!-- b000044 | prose | pages [2] -->
10

<!-- b000045 | prose | pages [2] -->
11 The building block: Naive Binomial Model . . . . . . . . . . . . . . . . . 5.1 11 . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 Momentum as residual effect 12 Variable identification . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 13 . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 Model Construction 15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 Data fitting 17 Inference on Match Data . . . . . . . . . . . . . . . . . . . . . . . . 5.2.4 19 Advisement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.5 19

<!-- b000046 | heading | pages [2] -->
Problem 4 : Swings Prediction and Model Generalization

<!-- b000047 | prose | pages [2] -->
6

<!-- b000048 | prose | pages [2] -->
7

<!-- b000049 | heading | pages [2] -->
Model Analysis

<!-- b000050 | prose | pages [2] -->
20

<!-- b000051 | prose | pages [2] -->
22 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 22 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 22 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3

<!-- b000052 | prose | pages [2] -->
8

<!-- b000053 | heading | pages [2] -->
Memorandum

<!-- b000054 | heading | pages [2] -->
References

<!-- b000055 | references | pages [2] -->
23

<!-- b000056 | references | pages [2] -->
23

<!-- b000057 | references | pages [2] -->
25

<!-- b000058 | references | pages [2] -->
关注数学模型

<!-- b000059 | furniture | pages [2] -->
2

<!-- b000060 | furniture | pages [2] -->
MATHmodels

<!-- b000061 | furniture | pages [2] -->
获取更多资讯

<!-- b000062 | furniture | pages [3] -->
Team # 2401298

<!-- b000063 | references | pages [3] -->
1

<!-- b000064 | heading | pages [3] -->
Introduction

<!-- b000065 | prose | pages [3] -->
1.1 Problem Background

<!-- b000066 | furniture | pages [3] -->
Page 3 of 25

<!-- b000067 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000068 | prose | pages [3] -->
The historic Wimbledon 2023 match between Carlos Alcaraz and Novak Djokovic illuminated the profound impact of momentum in tennis. This match not only capti- vated tennis enthusiasts but also highlighted a complex, yet underexplored, aspect of competitive sports: the ability of players to shift the match’s dynamics through "mo- mentum". The significance of momentum in determining match outcomes has become

<!-- b000069 | prose | pages [3] -->
[9]. This

<!-- b000070 | prose | pages [3] -->
a key area of interest. Volleyball players even use this for allocation decisions

<!-- b000071 | prose | pages [3] -->
underscores the need for a sophisticated model that captures the essence of momentum and explains the underlying rationale.

<!-- b000072 | prose | pages [3] -->
Clarifications and Restatements 1.2

<!-- b000073 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000074 | prose | pages [3] -->
Our task revolves around developing a quantifiable model of momentum in tennis, which aims to identify key indicators of momentum shifts, evaluate their impact on match results, and discern the extent to which these shifts can be attributed to skill, strategy, or mere chance. We will do the following steps:

<!-- b000075 | heading | pages [3] -->
1. create a model that delineates the flow of a tennis match, quantifying player perfor-

<!-- b000076 | prose | pages [3] -->
mance over time.

<!-- b000077 | heading | pages [3] -->
2. construct a hypothesis testing framework to evaluate whether swings in matches

<!-- b000078 | prose | pages [3] -->
are due to momentum or mere chance.

<!-- b000079 | heading | pages [3] -->
3. use our model to predict changes in match dynamics, identifying potential indica-

<!-- b000080 | prose | pages [3] -->
tors signaling a shift in match.

<!-- b000081 | heading | pages [3] -->
4. test the predictive power of our model across various matches, surfaces, and possi-

<!-- b000082 | prose | pages [3] -->
bly other similar sports, assessing its generalizability.

<!-- b000083 | heading | pages [3] -->
5. synthesize our findings into actionable strategies for coaches, aiding them in prepar-

<!-- b000084 | prose | pages [3] -->
ing players for shifts in match dynamics and responding effectively to momentum changes during play.

<!-- b000085 | prose | pages [3] -->
1.3 Our work

<!-- b000086 | prose | pages [3] -->
In response to this challenge, our approach intertwines statistical analysis, machine learning techniques, and dynamic simulations to forge a comprehensive model of ten- nis momentum. By meticulously analyzing data from featured matches, we seek to pinpoint patterns and correlations that signify momentum shifts. Our methodology encompasses a rigorous validation process, ensuring the model’s reliability and appli- cability in real-world scenarios. Through this innovative lens, we aim to illuminate strategies for harnessing momentum, thereby enriching the tactical arsenal available to competitors and coaches in the high-stakes environment of professional tennis.

<!-- b000087 | prose | pages [3] -->
关注数学模型

<!-- b000088 | furniture | pages [3] -->
2

<!-- b000089 | furniture | pages [3] -->
MATHmodels

<!-- b000090 | furniture | pages [3] -->
获取更多资讯

<!-- b000091 | furniture | pages [4] -->
Team # 2401298

<!-- b000092 | furniture | pages [4] -->
Page 4 of 25

<!-- b000093 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000094 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000095 | caption | pages [4] -->
Figure 1: Framework of Our Work

<!-- b000096 | prose | pages [4] -->
2

<!-- b000097 | heading | pages [4] -->
Preparation for Modeling

<!-- b000098 | prose | pages [4] -->
2.1

<!-- b000099 | heading | pages [4] -->
Model Assumptions

<!-- b000100 | prose | pages [4] -->
Some fundamental assumptions are listed below.

<!-- b000101 | prose | pages [4] -->
• Assumption 1: Factors such as weather, crowd support, and minor injuries do not significantly affect the match outcome. →Justification: While these factors can influence a match, including them in a model adds complexity and unpredictability. For a broad analysis, it’s practical to focus on more measurable and consistent factors.

<!-- b000102 | prose | pages [4] -->
• Assumption 2: A player’s current world ranking is reliable indicators of their potential performance in an upcoming match. →Justification: Rankings are based on a player’s performance in tournaments over a rolling period, reflecting their overall ability.

<!-- b000103 | prose | pages [4] -->
2.2

<!-- b000104 | heading | pages [4] -->
Notations

<!-- b000105 | prose | pages [4] -->
Some primary notations are listed below.

<!-- b000106 | prose | pages [4] -->
关注数学模型

<!-- b000107 | furniture | pages [4] -->
2

<!-- b000108 | furniture | pages [4] -->
MATHmodels

<!-- b000109 | furniture | pages [4] -->
获取更多资讯

<!-- b000110 | furniture | pages [5] -->
Team # 2401298

<!-- b000111 | furniture | pages [5] -->
Page 5 of 25

<!-- b000112 | caption | pages [5] -->
Table 1: Notations Table

<!-- b000113 | prose | pages [5] -->
Symbol M 1 Definition the probability that player 1 wins a point regardless of the server

<!-- b000114 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000115 | prose | pages [5] -->
Area Under Curve, a measure of model accuracy AUC Q Ljung-Box statistic Z Z-score for Runs Test r1 or r2 Expected losing round for player 1 or player 2 B Intrinsic probability function of winning a point λ The parameter determining Duel-Temporal Bayesian Network L the likelihood of data from 1 match between players E Momentum effect as difference between actual and expected points

<!-- b000116 | prose | pages [5] -->
2.3 Data Cleaning

<!-- b000117 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000118 | prose | pages [5] -->
After observing the Wimbledon_featured_matches.csv data set, we handle outlier values in column elapsed_time (rows 586 to 636), and delete the speed_mph column because of a significant number of missing values in it, which can impact the whole analysis.

<!-- b000119 | prose | pages [5] -->
Problem 1: Probability Difference Evaluation Strategy 3

<!-- b000120 | prose | pages [5] -->
3.1 Important Impact of Server

<!-- b000121 | prose | pages [5] -->
Let’s consider the change in the points difference between player 1 and player 2 in a match, according to Wimbledon_featured_matches.csv data set, we subtract p2_points_won data from p1_points_won to get points difference, namely:

<!-- b000122 | prose | pages [5] -->
points difference = p1_points_won - p2_points_won (1)

<!-- b000123 | prose | pages [5] -->
This formula helps us visualize the flow of a match, as depicted in the graph below, which highlights points difference over time:

<!-- b000124 | caption | pages [5] -->
Figure 2: Points Difference for Match 2023-wimbledon-1301

<!-- b000125 | prose | pages [5] -->
Where two colored dotted lines have also been added: green represents the server 关注数学模型 from player 1 to player 2, and purple represents the server from player 2 to player 1.

<!-- b000126 | furniture | pages [5] -->
2

<!-- b000127 | furniture | pages [5] -->
MATHmodels

<!-- b000128 | furniture | pages [5] -->
获取更多资讯

<!-- b000129 | furniture | pages [6] -->
Team # 2401298

<!-- b000130 | furniture | pages [6] -->
Page 6 of 25

<!-- b000131 | prose | pages [6] -->
A key observation is that the player currently serving has a higher chance of win- ning the point, especially when point number = [20, 50] or [180, 220] . However, the overall trend of points difference remains relatively stable, regardless of who serves, indicating that serving alone doesn’t drastically shift match momentum. So, we cannot

<!-- b000132 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000133 | prose | pages [6] -->
be influenced by who is the server when we try to identify which player is performing better at a given time in the match.

<!-- b000134 | prose | pages [6] -->
Sliding Point Interval Approach 3.2

<!-- b000135 | prose | pages [6] -->
To further analyse match dynamics, we focus on the probability difference between the players winning a point. In a match, the performance of two players depends on the probability difference M 1 or M 2, M 1 is the probability that player 1 wins a point regardless of the server, and M 2 is the probability that player 2 wins a point regardless of the server.

<!-- b000136 | prose | pages [6] -->
Next, according to the column point_no in the given data set, we can calculate p1

<!-- b000137 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000138 | prose | pages [6] -->
and p2 by choosing a fixed length ω of the data, p1 is the probability that player 1 wins a point on serve and p2 is the probability that player 2 wins a point on serve, ω is the point interval. If player 1 serves n1 times and player 2 serves n2 times (where w = n1 + n2), player 1 wins x1 points and player 2 wins x2 points, then p1 = x1

<!-- b000139 | prose | pages [6] -->


<!-- b000140 | prose | pages [6] -->
we can obtain the performance metric:

<!-- b000141 | prose | pages [6] -->
n1 and p2 = x2

<!-- b000142 | prose | pages [6] -->
n2. Actually,

<!-- b000143 | prose | pages [6] -->


<!-- b000144 | prose | pages [6] -->
1 −p2 p1

<!-- b000145 | prose | pages [6] -->
. If player 1 and player 2 have

<!-- b000146 | prose | pages [6] -->
1 −p1 p2

<!-- b000147 | prose | pages [6] -->
the same chance of serving, the ideal value of p1 and p2 should be equal, then

<!-- b000148 | prose | pages [6] -->
M 1

<!-- b000149 | prose | pages [6] -->


<!-- b000150 | prose | pages [6] -->
 p1

<!-- b000151 | prose | pages [6] -->
=

<!-- b000152 | prose | pages [6] -->
M 2

<!-- b000153 | prose | pages [6] -->
1 −p1

<!-- b000154 | prose | pages [6] -->
 1

<!-- b000155 | prose | pages [6] -->


<!-- b000156 | prose | pages [6] -->
1 −p2

<!-- b000157 | prose | pages [6] -->
21

<!-- b000158 | prose | pages [6] -->
(2)

<!-- b000159 | prose | pages [6] -->
p2

<!-- b000160 | prose | pages [6] -->
2

<!-- b000161 | prose | pages [6] -->
When M 1 > 0.5, it means player 1 performs better than player 2, and for M 1 < 0.5 the opposite. Futhermore, the higher the value, the better the performance of the player 1, thus it can identify which player is performing better at a given time in the match, as well as how much better they are performing.

<!-- b000162 | prose | pages [6] -->
To visualize the differenent performance of players 1 and 2, we bring in a rolling window of length ω. For each match, we can utilize this "rolling window" to calcu- late the difference between the performance of player 1 and player 2, and combined with cubic spline interpolation, we can plot the corresponding change in the degree of performance, and draw the following curve (ω = 30):

<!-- b000163 | caption | pages [6] -->
Figure 3: Probability Difference for Match 2023-wimbledon-1301

<!-- b000164 | prose | pages [6] -->
Where the abscissa is the total number of points scored in a match (the number关注数学模型

<!-- b000165 | furniture | pages [6] -->
2

<!-- b000166 | furniture | pages [6] -->
MATHmodels

<!-- b000167 | furniture | pages [6] -->
获取更多资讯

<!-- b000168 | furniture | pages [7] -->
Team # 2401298

<!-- b000169 | furniture | pages [7] -->
Page 7 of 25

<!-- b000170 | prose | pages [7] -->
pluses 1 when two players finish a ball, corresponding to the column point_no in the given data), the ordinate represents the probability difference M 1. Compared with Figure 2, we find that the changing of the server has nothing to do with the probability difference, which means comparing with the probability difference is more significant

<!-- b000171 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000172 | prose | pages [7] -->
than comparing with the points difference.

<!-- b000173 | prose | pages [7] -->
From Figure 3, the part above the red line indicates that player 1 (Carlos Alcaraz) is better than player 2 (Nicolas Jarry), and the part below the red line indicates that player 2 (Nicolas Jarry) is better than player 1 (Carlos Alcaraz), besides, the position of the peaks and valleys indicates that the player is performing particularly well.

<!-- b000174 | prose | pages [7] -->
Sliding Time Window Approach 3.3

<!-- b000175 | prose | pages [7] -->
However, it is not enough to select data points to draw according to the uniform interval of the total score, we should also do even segmentation from the perspective of the time of the game, remember that L represents the length of the time window,

<!-- b000176 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000177 | prose | pages [7] -->
λ represents the step size of each time window move, replace the point number with ti as the abscissa, ti = λ seconds, 2λ seconds, . . . For instance, if L = 600 seconds is used as the length of the time window, two players may play a total of 12 points or 18 points, and then set λ = 60 seconds as the step size of the time window movement, the result is more reflective of the player’s performance and more natural.

<!-- b000178 | prose | pages [7] -->
By adjusting different L and λ, we plot the variation as follows:

<!-- b000179 | caption | pages [7] -->
Figure 4: Performance Evaluation with Different Windows for Match 2023-wimbledon-1301

<!-- b000180 | prose | pages [7] -->
We can observe from the graph that the player’s performance at certain moments is dramatically affected by the length of the time window L while slightly affected by the step size of each time window movement λ. Generally, small window introduces noises while large window are unable to depict the rapidly changing dynamic of the game. To solve this, one common method is to apply filters, such as Gaussian filter, which requires a specific kernel function. This requires altering Formula 2. But we here propose a simpler yet equally effective approach named AUC (area under curve), as defined in the following formula:

<!-- b000181 | prose | pages [7] -->
1 A(t) = Lmax −Lmin

<!-- b000182 | prose | pages [7] -->
Z Lmax

<!-- b000183 | prose | pages [7] -->
ML(t) dL (3)

<!-- b000184 | prose | pages [7] -->
Lmin

<!-- b000185 | prose | pages [7] -->
Where ML(t) denotes the performance of one player at time t when considering win- dow length L . In practice we can simply discretize dL to be 1. Similar to kernal-based关注数学模型

<!-- b000186 | furniture | pages [7] -->
2

<!-- b000187 | furniture | pages [7] -->
MATHmodels

<!-- b000188 | furniture | pages [7] -->
获取更多资讯

<!-- b000189 | furniture | pages [8] -->
Team # 2401298

<!-- b000190 | furniture | pages [8] -->
Page 8 of 25

<!-- b000191 | prose | pages [8] -->
methods, AUC also weights the points winning with temporal distance (this can be easily seen by expressing ML(t) as sum of indicator functions then switching the sum- mation order, we skip the details here). The following is the generated graph using this method.

<!-- b000192 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000193 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000194 | caption | pages [8] -->
Figure 5: AUC-Time Plot for Match 2023-wimbledon-1301

<!-- b000195 | prose | pages [8] -->
From this graph we can determine which player is performing better at a certain time. When the curve is above 0.5, player 1 takes an upper hand, while the contrary happens when player 2 performs better. And the farther the curve’s distance from the equilibrium line, the greater the difference between players’ performance.

<!-- b000196 | prose | pages [8] -->
4 Problem 2: Momentum Existence

<!-- b000197 | prose | pages [8] -->
Given our analysis revealing potential patterns in "momentum", we now rigorously examine these observations through hypothesis testing to validate the presence of mo- mentum.

<!-- b000198 | prose | pages [8] -->
4.1 Hypothesis Testing Preparation

<!-- b000199 | prose | pages [8] -->
We first constructed the Hypothesis Testing Framework:

<!-- b000200 | prose | pages [8] -->
Null Hypothesis (H0): For a fixed server, the scoring of points by a player is inde- pendent and identically distributed (i.i.d.) and thus follows a binomial distribution. Alternative Hypothesis (H1): The complement of H0, suggesting that scoring is not entirely random, and some form of "momentum" or sequence dependency exists.

<!-- b000201 | prose | pages [8] -->
To evaluate the claim regarding the non-existence of "momentum", we denoted that in any given match, when Player 1 serves, the probability of Player 1 winning a point is p1, and when Player 2 serves, the probability of Player 1 winning a point is p2. The calculation of these probabilities, p1 and p2, is explained in Section 3.

<!-- b000202 | prose | pages [8] -->
For each match, we calculated the winning probabilities by: counting the number of points won and the total number of serves by Player 1 to calculate p1 and counting关注数学模型

<!-- b000203 | furniture | pages [8] -->
2

<!-- b000204 | furniture | pages [8] -->
MATHmodels

<!-- b000205 | furniture | pages [8] -->
获取更多资讯

<!-- b000206 | furniture | pages [9] -->
Team # 2401298

<!-- b000207 | furniture | pages [9] -->
Page 9 of 25

<!-- b000208 | prose | pages [9] -->
the number of points won by Player 1 against the total serves of Player 2 to calculate p2.

<!-- b000209 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000210 | prose | pages [9] -->
Ljung-Box Q Test and Runs Test Statistical Analysis 4.2

<!-- b000211 | prose | pages [9] -->
If scoring was entirely random, we would expect no significant autocorrelation be- tween consecutive points.

<!-- b000212 | prose | pages [9] -->
We separate out the scenarios for Player 1’s serve and Player 2’s serve and build se- quences for each match.Then calculate the autocorrelation for each sequence and Em- ploy an appropriate statistical test (Ljung-Box Q test) to assess whether the sequence’s autocorrelation is significant.

<!-- b000213 | prose | pages [9] -->
The statistic for the Ljung-Box Q test is calculated as follows:

<!-- b000214 | prose | pages [9] -->
h

<!-- b000215 | prose | pages [9] -->
ˆρ2

<!-- b000216 | prose | pages [9] -->
X

<!-- b000217 | prose | pages [9] -->
k

<!-- b000218 | prose | pages [9] -->
Q = n(n + 2)

<!-- b000219 | prose | pages [9] -->
(4)

<!-- b000220 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000221 | prose | pages [9] -->
n −k

<!-- b000222 | prose | pages [9] -->
k=1

<!-- b000223 | prose | pages [9] -->
Where: n is the sample size of the time series. h is the maximum number of lags considered for autocorrelation detection. ˆρk is the sample autocorrelation coefficient at lag k. Q is the Ljung Box statistic, which follows an approximate chi square distribution under the null hypothesis with degrees of freedom h −m, where m is the number of parameters in the model (for simple time series analysis, m is typically taken as m = 0).

<!-- b000224 | prose | pages [9] -->
The Ljung-Box Q test results for the first match, with a corresponding p-value of 0.497 for autocorrelations up to 10 observations, indicated a p-value greater than com- mon significance levels (e.g., 0.05). The results of other matches are similar. This sug- gests insufficient evidence to reject the null hypothesis H0.

<!-- b000225 | prose | pages [9] -->
Then we conducted the runs test to analyze the number of "runs" in a data sequence, where a "run" is defined as a sequence of identical elements occurring consecutively. We calculate the Expected Number of Runs and Variance,and get theZ-Score by:

<!-- b000226 | prose | pages [9] -->
Z = (R −E[R]) p

<!-- b000227 | prose | pages [9] -->
(5)

<!-- b000228 | prose | pages [9] -->
V ar(R)

<!-- b000229 | prose | pages [9] -->
Where: R represents the actual number of runs. E[R] is the expected number of runs, calculated as E[R] = 1+ 2n1n2

<!-- b000230 | prose | pages [9] -->
n1+n2. Var(R) is the variance of the number of runs, calculated as Var(R) = 2n1n2(2n1n2−n1−n2)

<!-- b000231 | prose | pages [9] -->
(n1+n2)2(n1+n2−1) . n1 and n2 are the counts of the two outcomes (e.g., wins and losses) in the sequence.

<!-- b000232 | prose | pages [9] -->
Then we calculate the P-Value Calculation by: P = 2(1 −Φ(|Z|)) to get the P = 0.691, which is greater than common significance levels (e.g., 0.05) suggests that the hypothesis of the points being i.i.d cannot be dismissed. The results of other matches are similar.

<!-- b000233 | prose | pages [9] -->
Here we plot the results of 2 methods with different matches. As evidenced by P values exceeding the 0.05 benchmark across various matches except for a few ones, we cannot reject the H0 for most matches.

<!-- b000234 | prose | pages [9] -->
关注数学模型

<!-- b000235 | furniture | pages [9] -->
2

<!-- b000236 | furniture | pages [9] -->
MATHmodels

<!-- b000237 | furniture | pages [9] -->
获取更多资讯

<!-- b000238 | furniture | pages [10] -->
Team # 2401298

<!-- b000239 | furniture | pages [10] -->
Page 10 of 25

<!-- b000240 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000241 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000242 | caption | pages [10] -->
Figure 6: feature importance

<!-- b000243 | prose | pages [10] -->
4.3 Instantaneous Winning Rates

<!-- b000244 | prose | pages [10] -->
[4], we employed

<!-- b000245 | prose | pages [10] -->
To check the i.i.d. argument, inspired by the paper [Sun, Y., 2004]

<!-- b000246 | prose | pages [10] -->
an instantaneous winning rate approach. This rate refers to the probability of a player winning the next point immediately after winning a point, under a constant server con- dition. We calculated and compared the instantaneous winning rates in two scenarios: The rate at which Player 1 wins the next point immediately after winning a point while serving and the rate at which Player 1 wins the next point immediately after winning a point against Player 2’s serve.

<!-- b000247 | caption | pages [10] -->
Table 2: Probability of Winning Based on Serving State

<!-- b000248 | prose | pages [10] -->
P of winning when serving Player and State

<!-- b000249 | prose | pages [10] -->
Player 2 0.6874 Player 1immediate 0.6978 Player 2 0.6594 Player 2immediate 0.6683

<!-- b000250 | prose | pages [10] -->
P of winning when not serving

<!-- b000251 | prose | pages [10] -->
0.3406 0.3498 0.3126 0.3261

<!-- b000252 | prose | pages [10] -->
The observed increase in winning rates by around 1% might indicate the influence of momentum, challenging the claim of randomness in scoring sequences within tennis matches.

<!-- b000253 | prose | pages [10] -->
Delving into the subtleties of the match data revealed an intriguing pattern: players demonstrated a marginally increased probability of securing the next point following a win, whether serving or returning. While the data does not overwhelmingly endorse the notion of momentum, it does quietly nod to its existence.

<!-- b000254 | prose | pages [10] -->
关注数学模型

<!-- b000255 | furniture | pages [10] -->
2

<!-- b000256 | furniture | pages [10] -->
MATHmodels

<!-- b000257 | furniture | pages [10] -->
获取更多资讯

<!-- b000258 | furniture | pages [11] -->
Team # 2401298

<!-- b000259 | furniture | pages [11] -->
Page 11 of 25

<!-- b000260 | prose | pages [11] -->
Problem 3: Momentum Prediction 5

<!-- b000261 | heading | pages [11] -->
The building block: Naive Binomial Model

<!-- b000262 | prose | pages [11] -->
5.1

<!-- b000263 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000264 | prose | pages [11] -->
One immediate issue in identifying "momentum" in competition is that all variables we observe are mixed with the momentum effect and the effect from the skill level difference of the players. In order to "separate out" the effect of momentum, we first develop a naive model without considering any momentum. Or, equivalently, a model under the assumption that the points won are identically distributed random variables.

<!-- b000265 | prose | pages [11] -->
[5].

<!-- b000266 | prose | pages [11] -->
We term this model the Binomial Model, denoted by BM

<!-- b000267 | prose | pages [11] -->
To develop this model, we collect the world rank of players as additional prior information ... And convert them into relative rank in 2023 Wimbledon competition. By "relative", we re-rank the 32 players according to their rankings relative to each other, resulting an array of integers between 1 and 32. Then BM is simply a function of (Rank1, Rank2).

<!-- b000268 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000269 | prose | pages [11] -->
Our Binomial model takes the rank of two players then return the "intrinsic proba- bility" of winning a certain point, which under the naive assumption, stay constantly across the whole match.

<!-- b000270 | prose | pages [11] -->
It’s notable that in tennis competition, strength difference between top rank players are often more evident than players with lower ranks. For example, we may expect the difference between rank 1 and rank 2 players larger than the difference between rank 31 and rank 32 players. On the contrary, the notion of "expected losing round"

<!-- b000271 | prose | pages [11] -->
[5]. Specifically, we define

<!-- b000272 | prose | pages [11] -->
can capture this prior well

<!-- b000273 | prose | pages [11] -->
r1 = 6 −log2(Rank1) (6)

<!-- b000274 | prose | pages [11] -->
Consequently, we can define BM(Rank1, Rank2) := f1(r1, r2). Set f2(x, y) = f1(x+y

<!-- b000275 | prose | pages [11] -->
x−y 2 ,

<!-- b000276 | prose | pages [11] -->
2 ) we have BM = f2(r1 −r2, r1 + r2) . We provide the following approximation for f2 :

<!-- b000277 | prose | pages [11] -->
eλ(r1−r2) f2(r1 −r2, r1 + r2) =

<!-- b000278 | prose | pages [11] -->
1 + eλ(r1−r2) + s (7)

<!-- b000279 | prose | pages [11] -->
Where s > 0 is the server advantage. Alternatively, we can set the right hand side as

<!-- b000280 | prose | pages [11] -->
eλ(r1−r2)+µ(r1+r2)

<!-- b000281 | prose | pages [11] -->
1+eλ(r1−r2)+µ(r1+r2) + s with more parameters.

<!-- b000282 | prose | pages [11] -->
But during experiment we have found the value of mu to be considerably small thus we ignore it here. Ideally, if the Formula (6) has captured the rank-strength relationship well enough, then this simplification makes sense. Refer to [Klaassen and Magnus, [2] for further justification. 2001]

<!-- b000283 | prose | pages [11] -->
We then estimate the parameter λ on our point-to-point data of 31 matches by max- imizing the likelyhood.

<!-- b000284 | prose | pages [11] -->
Step 1: Likelihood Function

<!-- b000285 | prose | pages [11] -->
Assuming the outcomes of individual points are independent (an assumption of our naive model), the likelihood of observing the data from a single match between player 1 and player 2, where player 1 wins n1 points and player 2 wins n2 points, can be represented as a binomial distribution:

<!-- b000286 | prose | pages [11] -->
关注数学模型

<!-- b000287 | furniture | pages [11] -->
2

<!-- b000288 | furniture | pages [11] -->
MATHmodels

<!-- b000289 | furniture | pages [11] -->
获取更多资讯

<!-- b000290 | furniture | pages [12] -->
Team # 2401298

<!-- b000291 | prose | pages [12] -->
eλ(r1−r2)

<!-- b000292 | prose | pages [12] -->
n1 + n2

<!-- b000293 | prose | pages [12] -->
 

<!-- b000294 | prose | pages [12] -->
L(λ, s|n1, n2) =

<!-- b000295 | furniture | pages [12] -->
Page 12 of 25

<!-- b000296 | prose | pages [12] -->
n1 

<!-- b000297 | prose | pages [12] -->
n2

<!-- b000298 | prose | pages [12] -->
eλ(r1−r2)  1 −

<!-- b000299 | prose | pages [12] -->
1 + eλ(r1−r2) + s

<!-- b000300 | prose | pages [12] -->
n1

<!-- b000301 | prose | pages [12] -->
1 + eλ(r1−r2) + s

<!-- b000302 | prose | pages [12] -->
(8)

<!-- b000303 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000304 | prose | pages [12] -->
Step 2: Log-Likelihood

<!-- b000305 | prose | pages [12] -->
To simplify calculations and to deal with potential numerical underflow, it’s com- mon to work with the log-likelihood rather than the likelihood itself.

<!-- b000306 | furniture | pages [12] -->


<!-- b000307 | prose | pages [12] -->
!

<!-- b000308 | furniture | pages [12] -->


<!-- b000309 | furniture | pages [12] -->


<!-- b000310 | prose | pages [12] -->
!!

<!-- b000311 | prose | pages [12] -->
eλ(r1−r2)

<!-- b000312 | prose | pages [12] -->
n1 + n2

<!-- b000313 | prose | pages [12] -->


<!-- b000314 | prose | pages [12] -->
log L(λ, s|n1, n2) = log

<!-- b000315 | prose | pages [12] -->
eλ(r1−r2)

<!-- b000316 | prose | pages [12] -->
1 −

<!-- b000317 | prose | pages [12] -->
1 + eλ(r1−r2) + s

<!-- b000318 | prose | pages [12] -->
+n1 log

<!-- b000319 | prose | pages [12] -->
n1

<!-- b000320 | prose | pages [12] -->
+n2 log

<!-- b000321 | prose | pages [12] -->
1 + eλ(r1−r2) + s

<!-- b000322 | prose | pages [12] -->
(9)

<!-- b000323 | prose | pages [12] -->
Step 3: Aggregate Log-Likelihood Over All Matches

<!-- b000324 | prose | pages [12] -->
To estimate λ, s using data from all 31 matches, we sum the log-likelihoods across

<!-- b000325 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000326 | prose | pages [12] -->
all matches:

<!-- b000327 | prose | pages [12] -->
X

<!-- b000328 | prose | pages [12] -->
log L(λ, s) =

<!-- b000329 | prose | pages [12] -->
matches

<!-- b000330 | prose | pages [12] -->
Step 4: Maximizing the Log-Likelihood

<!-- b000331 | prose | pages [12] -->
log L(λ, s|n1, n2) (10)

<!-- b000332 | prose | pages [12] -->
Owing to the smoothness of the function, we can easily apply Newton method, which requires the computation of first and second derivative, to iteratively adjust λ, s to find the maximum. The optimal value is computed as lambda = 0.0624, s = 0.1742 .

<!-- b000333 | prose | pages [12] -->
5.2 Momentum as residual effect

<!-- b000334 | prose | pages [12] -->
It’s easy for us to observe the equivalence between no momentum statement and ⇐⇒ memoryless statement. "Momentum doesn’t exist" "The process of winning points is independent of the past of the game, or in another word, memoryless"

<!-- b000335 | prose | pages [12] -->
Now by inversing both sides, we can measure the momentum effect as:

<!-- b000336 | prose | pages [12] -->
E := S −ˆS (11)

<!-- b000337 | prose | pages [12] -->
Where S is the points winning in reality while ˆS is the points winning predicted by the Binomial model. Since no strict definition of momentum exists as a statistic. We now use formula (11) to define the value of momentum. This formula can be under- stand intuitively, as previous critics on momentum often describe it as “seeing some-

<!-- b000338 | prose | pages [12] -->
[4]

<!-- b000339 | prose | pages [12] -->
thing out of randomness.”

<!-- b000340 | prose | pages [12] -->
In order to design a model to predict the residual, there are several key facts worth noticing:

<!-- b000341 | prose | pages [12] -->
The reason why "momentum" is so hard to grasp statistically is that this concept implies some "hidden state" exists in the system of sports play. So a generative model is preferred. The direct 1-step prediction can be extremely noisy and thus posing a challenge for effective model-fitting. We need specific approach to reduce the impact of the noise. The influence of past game state should be encoded in this model. And 关注数学模型 the effect from the past could potentially last for a long time.

<!-- b000342 | furniture | pages [12] -->
2

<!-- b000343 | furniture | pages [12] -->
MATHmodels

<!-- b000344 | furniture | pages [12] -->
获取更多资讯

<!-- b000345 | furniture | pages [13] -->
Team # 2401298

<!-- b000346 | furniture | pages [13] -->
Page 13 of 25

<!-- b000347 | prose | pages [13] -->
Taking all these into account, we introduce our novel Duel-Temporal Bayesian Net- work. As a variation of normal Dynamical Bayesian Network, it not only constructs a hidden model for the tennis game play, but also encodes long-short term memory from the past, enabling a comprehensive detection of "momentum".

<!-- b000348 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000349 | prose | pages [13] -->
5.2.1 Variable identification

<!-- b000350 | prose | pages [13] -->
In tennis, what’s not seen can be just as influential as the scoreboard. For example, a player’s sudden surge or dip in performance isn’t always from the visible aces or double faults. It’s often the hidden triggers – maybe how the match’s strain is weighing on their shoulders – that can turn the tide. A tennis game is not only a competition in strength or technique, but also involves complicated psychological and physiological dynamics.

<!-- b000351 | prose | pages [13] -->
[1], we see that momentum is a complex

<!-- b000352 | prose | pages [13] -->
Drawing from the insights of [Taylor J., 1994]

<!-- b000353 | prose | pages [13] -->
system of cognition, physiology, and emotion, all sparked by precipitating events and

<!-- b000354 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000355 | prose | pages [13] -->
manifesting in performance changes. This paper’s concept of a "momentum chain", which suggests that an initial event can trigger alterations in an athlete’s cognition, affect, and physiology, leading to behavioral changes that influence performance, res- onates with the invisible forces at play in tennis, guiding us to consider latent variables.

<!-- b000356 | prose | pages [13] -->
Based on this framework, we select 3 latent variables in our model: "Physiology", "perception of control", and "self-efficacy". They play a crucial role in capturing the complex, non-observable factors that influence the momentum swings in a tennis match.

<!-- b000357 | heading | pages [13] -->
1. Physiology: The physical condition of the players, like fatigue, energy levels,

<!-- b000358 | prose | pages [13] -->
and even subtle injuries.

<!-- b000359 | heading | pages [13] -->
2. Perception of Control: This represents a player’s ability to control the match.

<!-- b000360 | heading | pages [13] -->
3. Self-efficacy: Self-efficacy is a player’s belief in their capability,which is the fuel

<!-- b000361 | prose | pages [13] -->
that powers player’s persistence.

<!-- b000362 | prose | pages [13] -->
[1], precipitating events, such as specific shots, critical

<!-- b000363 | prose | pages [13] -->
According to [Taylor J., 1994]

<!-- b000364 | prose | pages [13] -->
points shift a player’s mental and physiological state indirectly. These hidden state are the undercurrents of the game, unseen but vital. Incorporating these into our model allows for a more accurate understanding and prediction of momentum swings.

<!-- b000365 | prose | pages [13] -->
Then we get the diagram below. The arrows in the following diagram represent influential relationships between various factors. This complex network of influences reflects the multifaceted nature of competitive sports, where physical, mental, and sit- uational factors all intertwine to affect the outcome of a match.

<!-- b000366 | prose | pages [13] -->
关注数学模型

<!-- b000367 | furniture | pages [13] -->
2

<!-- b000368 | furniture | pages [13] -->
MATHmodels

<!-- b000369 | furniture | pages [13] -->
获取更多资讯

<!-- b000370 | furniture | pages [14] -->
Team # 2401298

<!-- b000371 | furniture | pages [14] -->
Page 14 of 25

<!-- b000372 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000373 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000374 | caption | pages [14] -->
Figure 7: Identified Variables

<!-- b000375 | prose | pages [14] -->
Due to the limitation of our data (only 31 matches), a complicated model like this is prone to overfitting and thus not suitable for robustness prediction. To simplify the model construction, we utilized random forest to search for variables that are insignif- icant for prediction.Here are some top features:

<!-- b000376 | caption | pages [14] -->
Table 3: Feature Importance

<!-- b000377 | prose | pages [14] -->
p2_winner p1_unf_err Feature p2_unf_err p1_winner 0.111018 Importance 0.120587 0.101907 0.094330 rally_count server Feature p2_net_pt_won game_victor 0.081359 Importance 0.084700 0.047800 0.043592 p2_distance_run p1_net_pt_won Feature p1_distance_run 0.032348 Importance 0.032918 0.032152

<!-- b000378 | prose | pages [14] -->
To simplify our network, we should visualize the correlation between features us- ing a correlation heatmap. This is crucial for feature engineering. The correlation heatmap of the top-10 features shows the relationships between variables that are most predictive of the point victor in a tennis match. Here are some insights from the heatmap:

<!-- b000379 | prose | pages [14] -->
Unforced Errors (p_1_unf_err, p_2_unf_err): These features show a significant cor- relation with the outcome of points, implying that players’ mistakes can crucially in- fluence point results.

<!-- b000380 | prose | pages [14] -->
Winners (p_1_winner, p_2_winner): Points won by players due to winning shots are highly correlated with the match outcome.

<!-- b000381 | prose | pages [14] -->
Serving (server): The role of the server in a point has a notable correlation with关注数学模型

<!-- b000382 | furniture | pages [14] -->
2

<!-- b000383 | furniture | pages [14] -->
MATHmodels

<!-- b000384 | furniture | pages [14] -->
获取更多资讯

<!-- b000385 | furniture | pages [15] -->
Team # 2401298

<!-- b000386 | prose | pages [15] -->
point outcomes.

<!-- b000387 | furniture | pages [15] -->
Page 15 of 25

<!-- b000388 | prose | pages [15] -->
Physical and Strategic Aspects (rally_count, p_1_net_pt_won, p_2_net_pt_won): These features suggest the physical exertion and strategic play involved in points, such as

<!-- b000389 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000390 | prose | pages [15] -->
longer rallies and successful net plays contributing to point outcomes.

<!-- b000391 | prose | pages [15] -->
This reveals several layers of the game that potentially contribute to momentum, such as the direct impact like unforced errors, winning shots, and the advantage con- ferred by serving. Additionally, the physical and strategic elements like rally counts and net points could influence a player’s dominance during a match as well.

<!-- b000392 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000393 | caption | pages [15] -->
Figure 8: Correlation Heatmap of Top-10 Features

<!-- b000394 | prose | pages [15] -->
5.2.2

<!-- b000395 | heading | pages [15] -->
Model Construction

<!-- b000396 | prose | pages [15] -->
Through this method, we ascertained and dropped insignificant features such as physiology. The remaining features forms the bedrock of our network. The simplified version is depicted in the following graph:

<!-- b000397 | prose | pages [15] -->
关注数学模型

<!-- b000398 | furniture | pages [15] -->
2

<!-- b000399 | furniture | pages [15] -->
MATHmodels

<!-- b000400 | furniture | pages [15] -->
获取更多资讯

<!-- b000401 | furniture | pages [16] -->
Team # 2401298

<!-- b000402 | furniture | pages [16] -->
Page 16 of 25

<!-- b000403 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000404 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000405 | caption | pages [16] -->
Figure 9: One Building Block of the Bayesian Network

<!-- b000406 | prose | pages [16] -->
Using this simpler network as one building block, we can stack two blocks together to form our Duel-Temporal Bayesian Network:

<!-- b000407 | caption | pages [16] -->
Figure 10: Duel-Temporal Bayesian Network

<!-- b000408 | prose | pages [16] -->
We have added green arrows between hidden variables in these two layers, repre- senting the continuity of mental and physical state.

<!-- b000409 | prose | pages [16] -->
关注数学模型

<!-- b000410 | furniture | pages [16] -->
2

<!-- b000411 | furniture | pages [16] -->
MATHmodels

<!-- b000412 | furniture | pages [16] -->
获取更多资讯

<!-- b000413 | furniture | pages [17] -->
Team # 2401298

<!-- b000414 | prose | pages [17] -->
5.2.3 Data fitting

<!-- b000415 | furniture | pages [17] -->
Page 17 of 25

<!-- b000416 | prose | pages [17] -->
One obstacle for effectively training this model is noise. Although we have taken into account the original strength difference and the serving advantage, we must ad-

<!-- b000417 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000418 | prose | pages [17] -->
mit the residual effect of gaining/losing at a certain point is still (and should be still) largely random. Instead of letting the model predict the state in the next point, we let it predict **the sum** of the effect in the next n points. Because of Central Limit The- orem, this reduces the noise and thus making the network’s training possible. In the same manner, all the observed variables such as player’s double fault is aggregated in a certain time interval. Specifically, suppose the current point index is t , the long-term layer’s data is aggregated in [t −40, t −10] and the effect in [t −10, t] , while the short- term layer’s data is aggregated in [t −10, t] and the effect in [t, t + 10] . We carefully separate the past game information and the future game outcome to guarantee our model is completely predictive.

<!-- b000419 | prose | pages [17] -->
The following graph depicts the shifting of denoised residual effect in the match between Carlos Alcaraz and Djokovic from Carlos’ perspective.

<!-- b000420 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000421 | caption | pages [17] -->
Figure 11: Denoised Residual Effect Cruve

<!-- b000422 | prose | pages [17] -->
Due to the existence of latent variables in our model, we utilize the Expectation- Maximization (EM) algorithm to train the network on the data of 31 matches in Wim- bledon 2023. EM is used in statistics for finding maximum likelihood estimates of parameters in probabilistic models, where the model depends on unobserved latent variables.

<!-- b000423 | prose | pages [17] -->
The EM algorithm consists of two steps: the Expectation step (E step) and the Max- imization step (M step). In the E step, the algorithm calculates the expected values of the latent variables given the current parameters of the model. In the M step, it maximizes the likelihood function to update the parameters based on these expected values. This process is repeated until convergence.

<!-- b000424 | prose | pages [17] -->
Q(θ|θ(t)) = EZ|X,θ(t)[log L(θ; X, Z)] E step:

<!-- b000425 | prose | pages [17] -->
(12)关注数学模型

<!-- b000426 | furniture | pages [17] -->
2

<!-- b000427 | furniture | pages [17] -->
MATHmodels

<!-- b000428 | furniture | pages [17] -->
获取更多资讯

<!-- b000429 | furniture | pages [18] -->
Team # 2401298

<!-- b000430 | furniture | pages [18] -->
Page 18 of 25

<!-- b000431 | prose | pages [18] -->
θ(t+1) = arg max M step:

<!-- b000432 | prose | pages [18] -->
Q(θ|θ(t)) (13) θ

<!-- b000433 | prose | pages [18] -->
In these equations, θ represents the parameters of the model, X represents the ob-

<!-- b000434 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000435 | prose | pages [18] -->
served data which consists both the output - residual effect and the input - point-to- point data, Z represents the latent variables(6 latent variables in our model), L is the likelihood function, and Q is a function that depends on the expected values of the latent variables.

<!-- b000436 | prose | pages [18] -->
During our first training, we spotted an unexpected bias in this dataset: the player 1 has overall better residual effect than the player 2. Consequently, the prior distribution (i.e. when NO evidence provided) of "player 1 has better residual effect" vs "player 2 has better residual effect" predicted by our model is about 53% vs 47%. We could mirror the dataset (i.e. switch the position of player 1 and player 2) but will also double training cost. To solve this in a more general manner, we reweight the expression of Q(θ|θ(t)) as

<!-- b000437 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000438 | prose | pages [18] -->
1 Q(θ|θ(t)) = EZ|X,θ(t)[ Reweighted E step:

<!-- b000439 | prose | pages [18] -->
P(X) log L(θ; X, Z)] (14)

<!-- b000440 | prose | pages [18] -->
Where P(X) is the prior of X occurring when considering some of its features - in our case, the residual effect advantage.

<!-- b000441 | prose | pages [18] -->
For effectively training the network, we need first discretize the variables. The terms residual_effect_1(0) and residual_effect_1(1) refer to the momentum attributed to the opponent and oneself, respectively. Similarly, unf_err_1 ranges from 0 to 2, in- dicating the relative unforced error levels between players; ’0’ implies more unforced errors in the opponent, ’1’ denotes equal levels, and ’2’ suggests more unforced errors in oneself. As for latent variables, like self_efficacy_1 values range from 0 to 1, indi- cating the relative self-efficacy levels between players; ’0’ implies higher self-efficacy in the opponent, and ’1’ suggests higher self-efficacy in oneself.

<!-- b000442 | prose | pages [18] -->
To measure the importance of variables, we compute the information gain (or equiv- alently, "entropy reduction") when given each variable. The entropy values provide a measure of uncertainty or unpredictability associated with the predictions of different variables’ effects on momentum. A greater information gain indicates greater impor- tance.

<!-- b000443 | prose | pages [18] -->
(a) (b)

<!-- b000444 | caption | pages [18] -->
Figure 12: Differences in Residual Effects and Entropy

<!-- b000445 | prose | pages [18] -->
关注数学模型

<!-- b000446 | furniture | pages [18] -->
2

<!-- b000447 | furniture | pages [18] -->
MATHmodels

<!-- b000448 | furniture | pages [18] -->
获取更多资讯

<!-- b000449 | furniture | pages [19] -->
Team # 2401298

<!-- b000450 | furniture | pages [19] -->
Page 19 of 25

<!-- b000451 | prose | pages [19] -->
As can be seen from the graph, the most substantial positive influence on momen- tum is from player’s net point won, closely followed by aces and maintaining a scoring lead. These results suggest that proactive and aggressive playstyles significantly con- tribute to a player’s momentum. In stark contrast, unforced errors are shown to under-

<!-- b000452 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000453 | prose | pages [19] -->
mine momentum, emphasizing the importance of consistency and error management in maintaining psychological advantage on the court. Double faults unexpectedly ap- pear to increase momentum slightly. We suspect this is due to the correlation between double fault and aggressive serving. Since the player’s aggressiveness isn’t identified as variable in our model, the true causal effect is thus hard to learn.

<!-- b000454 | prose | pages [19] -->
To further clarify the counterintuitive increase in momentum following double faults, our investigation delved into the patterns of serving. Baseline ace rates for servers pace

<!-- b000455 | prose | pages [19] -->
and pace 1

<!-- b000456 | prose | pages [19] -->
stood at 9.70% and 8.61%, respectively. Intriguingly, analysis post-double fault 2 revealed an uptick in ace frequency, with player 1’s ace rate pace next double fault

<!-- b000457 | prose | pages [19] -->
to 10.61% and pace next double fault ascending 1

<!-- b000458 | prose | pages [19] -->
to 9.59% within the ensuing ten serves. This suggests a 2 correlation shortcut or data bias learned by the model.

<!-- b000459 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000460 | prose | pages [19] -->
5.2.4 Inference on Match Data

<!-- b000461 | prose | pages [19] -->
During inference, all observed variables, including long term residual effect are feeding into the model. Based on these known evidence, our Bayesian network can determine the distribution of the output and latent variables, and ultimately, the mo- mentum (as residual effect) in a match. Specifically, given the structure of the network, we can describe the mathematical relationship between these variables’ distribution using the conditional dependencies depicted in the network. For computational de-

<!-- b000462 | prose | pages [19] -->
[11].

<!-- b000463 | prose | pages [19] -->
tail, refer to [(Ben, 2007)]

<!-- b000464 | prose | pages [19] -->
5.2.5 Advisement

<!-- b000465 | prose | pages [19] -->
Based on the statistical analysis from our Bayesian network, we propose the follow- ing strategies for players to potentially improve their momentum:

<!-- b000466 | heading | pages [19] -->
1. Minimize Unforced Errors: Prioritize consistency in rallies to avoid giving away

<!-- b000467 | prose | pages [19] -->
momentum through avoidable mistakes.

<!-- b000468 | heading | pages [19] -->
2. Leverage Aggressive Plays: Integrate more net approaches and aim for aces to

<!-- b000469 | prose | pages [19] -->
capitalize on these actions’ strong positive impact on momentum.

<!-- b000470 | heading | pages [19] -->
3. Strategic Serving: Focus on serve accuracy and variety, reducing double faults

<!-- b000471 | prose | pages [19] -->
even though they may not significantly dampen momentum, as maintaining serve is still critical for match success.

<!-- b000472 | heading | pages [19] -->
4. Mental Resilience: Develop psychological resilience to withstand the pressure

<!-- b000473 | prose | pages [19] -->
of facing break points, as overcoming them contributes less to momentum than antici- pated.

<!-- b000474 | heading | pages [19] -->
5. Maintain Lead: Strive to build and maintain a lead, as staying ahead fosters

<!-- b000475 | prose | pages [19] -->
positive momentum and can exert psychological pressure on the opponent.

<!-- b000476 | prose | pages [19] -->
Incorporating these strategies into training and match-play can help players har- ness and maintain momentum, which is a pivotal aspect of competitive tennis.

<!-- b000477 | prose | pages [19] -->
关注数学模型

<!-- b000478 | furniture | pages [19] -->
2

<!-- b000479 | furniture | pages [19] -->
MATHmodels

<!-- b000480 | furniture | pages [19] -->
获取更多资讯

<!-- b000481 | furniture | pages [20] -->
Team # 2401298

<!-- b000482 | furniture | pages [20] -->
Page 20 of 25

<!-- b000483 | prose | pages [20] -->
6

<!-- b000484 | heading | pages [20] -->
Problem 4 : Swings Prediction and Model Generaliza-

<!-- b000485 | prose | pages [20] -->
tion

<!-- b000486 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000487 | prose | pages [20] -->
We first evaluated our model on the final match between Carlos Alcaraz and No- vak Djokovic. The outcomes, together with those from three additional matches, are presented in the subsequent graph. It’s notable that our model accurately forecasted the first few up and downs of the residual effect, but failed at the 230th 280th points which corresponds to the fourth set. During this phase, Novak Djokovic unexpectedly gained a significant advantage. This is probably due to the effect of factors that our model does not account for.

<!-- b000488 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000489 | caption | pages [20] -->
Figure 13: Predicted vs Actual

<!-- b000490 | prose | pages [20] -->
A possible factor that significantly influences outcomes in tennis is the personal play style of specific players, like surface preferences, injury history. These can only be modeled through their historical performances and can’t be inferred through our current approach (i.e. only consider players’ rankings). A data-based integration of player’s personal information may further boost our model’s performance.

<!-- b000491 | prose | pages [20] -->
Besides, the given Wimbledon dataset, we also test our model on a dataset of women’s singles tennis matches from JeffSackmann’s tennis_MatchChartingProject,

<!-- b000492 | prose | pages [20] -->
[10].

<!-- b000493 | prose | pages [20] -->
which is called charting −w −points −2020s.csv

<!-- b000494 | prose | pages [20] -->
关注数学模型

<!-- b000495 | furniture | pages [20] -->
2

<!-- b000496 | furniture | pages [20] -->
MATHmodels

<!-- b000497 | furniture | pages [20] -->
获取更多资讯

<!-- b000498 | furniture | pages [21] -->
Team # 2401298

<!-- b000499 | furniture | pages [21] -->
Page 21 of 25

<!-- b000500 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000501 | prose | pages [21] -->
(a) (b)

<!-- b000502 | caption | pages [21] -->
Figure 14: Differences in Residual Effects and Entropy

<!-- b000503 | prose | pages [21] -->
Compared with Figure 12 , one notable distinction is the impact of aces. In our dataset, male players have a 9.14% likelihood of achieving an ace, whereas female

<!-- b000504 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000505 | prose | pages [21] -->
players only 4.25%. Additionally, the occurrence of double faults now clearly has a detrimental effect, as it is no longer the result of aggressive attempts to achieve an ace.

<!-- b000506 | prose | pages [21] -->
To demonstrate the adaptability of our model framework, we further generalize it into a more abstract and comprehensive form, as depicted in the following graph. This framework can be instantiated into models that are capable of dealing all kinds of sports games such as table tennis, basketball, soccer...

<!-- b000507 | caption | pages [21] -->
Figure 15: General Framework

<!-- b000508 | prose | pages [21] -->
关注数学模型

<!-- b000509 | furniture | pages [21] -->
2

<!-- b000510 | furniture | pages [21] -->
MATHmodels

<!-- b000511 | furniture | pages [21] -->
获取更多资讯

<!-- b000512 | furniture | pages [22] -->
Team # 2401298

<!-- b000513 | prose | pages [22] -->
7

<!-- b000514 | heading | pages [22] -->
Model Analysis

<!-- b000515 | prose | pages [22] -->
7.1

<!-- b000516 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b000517 | furniture | pages [22] -->
Page 22 of 25

<!-- b000518 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000519 | heading | pages [22] -->
Strengths:

<!-- b000520 | prose | pages [22] -->
1. Captures both short-term and long-term momentum effects through the two- layer structure. This allows the model to account for momentum shifts arising from recent in-game events as well as longer-term psychological factors.

<!-- b000521 | prose | pages [22] -->
2. Incorporates latent variables like physiology, perception of control, and self- efficacy that are not directly observable but play an important role in momentum. This provides a more comprehensive representation of the factors influencing momentum.

<!-- b000522 | prose | pages [22] -->
3. Uses advanced machine learning techniques like expectation maximization to handle the latent variables and make the model trainable on real match data. This enables practical application of the model.

<!-- b000523 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000524 | prose | pages [22] -->
4. Achieves good generalization across different players and matches in the dataset, demonstrating robustness.

<!-- b000525 | prose | pages [22] -->
5. Provides interpretable insights into how different factors like unforced errors, aggressive plays, break points etc. influence momentum.

<!-- b000526 | prose | pages [22] -->
Weaknessess:

<!-- b000527 | prose | pages [22] -->
1. Difficult to fully validate accuracy of latent variable representations and their dynamics without access to actual measurements of players’ psychological states.

<!-- b000528 | prose | pages [22] -->
2. Requires aggregation of data over intervals to reduce noise for training, losing some granularity.

<!-- b000529 | prose | pages [22] -->
3. Does not account for opponent adaptive strategies and their influence on mo- mentum. Assumes independent player behaviors.

<!-- b000530 | prose | pages [22] -->
7.2

<!-- b000531 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000532 | prose | pages [22] -->
To evaluate the robustness of our proposed model, we conduct a sensitivity analysis on two aspects. 1. Modifying the model’s prediction interval. 2. Changing the training data by randomly sampling 70% and 50% from the original dataset, corresponding to 22 and 16 matches, respectively.

<!-- b000533 | prose | pages [22] -->
The following is the altered information gain from observed variables. The changes in the left graph indicates that a longer prediction interval forces the model to prioritize effects with potentially longer durations, such as "score advantage". On the contrary, short-term events like "net point won", "ace" gain less weight. In the right graph, the model trained on 50% appears notable changes, likely due to the altered distribution of matches. On the other hand, the model trained with 70% of the data remained stable, indicating a threshold of data sufficiency.

<!-- b000534 | prose | pages [22] -->
关注数学模型

<!-- b000535 | furniture | pages [22] -->
2

<!-- b000536 | furniture | pages [22] -->
MATHmodels

<!-- b000537 | furniture | pages [22] -->
获取更多资讯

<!-- b000538 | furniture | pages [23] -->
Team # 2401298

<!-- b000539 | furniture | pages [23] -->
Page 23 of 25

<!-- b000540 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000541 | prose | pages [23] -->
(a) (b)

<!-- b000542 | caption | pages [23] -->
Figure 16: Differences in Residual Effects and Entropy

<!-- b000543 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000544 | prose | pages [23] -->
7.3

<!-- b000545 | heading | pages [23] -->
Conclusion

<!-- b000546 | prose | pages [23] -->
In this paper, we establish our momentum predictor through a two-step process. Initially, we develop a naive binomial model aimed at recovering the "ideal" state of the game. Subsequently, the residual of its prediction is utilized as the label for our momentum predictor, the dual-temporal Bayesian network. This model framework, demonstrated to be highly generalizable and robust, allows us to uncover the latent systems underlying observable sports games.

<!-- b000547 | prose | pages [23] -->
8

<!-- b000548 | heading | pages [23] -->
Memorandum

<!-- b000549 | prose | pages [23] -->
To: Tennis Coaches

<!-- b000550 | prose | pages [23] -->
From: Team #2401298

<!-- b000551 | prose | pages [23] -->
Subject: Leveraging Momentum in Tennis - Insights and Strategies for Coaching

<!-- b000552 | prose | pages [23] -->
Date: February 6, 2024

<!-- b000553 | prose | pages [23] -->
Dear Coaches,

<!-- b000554 | prose | pages [23] -->
We are thrilled to share with you our suggestions derived from our Duel-Temporal Bayesian network model, to enhance player performance through the nuanced con- cept of "momentum" in tennis. In the dynamic world of competitive tennis, the concept of "momentum" is often cited as a game-changer, potentially turning the tide in pivotal match moments. This elusive force is thought to shape match outcomes. Our research has dissected this phenomenon, aiming to transform the abstract phenomenon into tangible strategies that can be methodically applied.

<!-- b000555 | prose | pages [23] -->
关注数学模型

<!-- b000556 | furniture | pages [23] -->
2

<!-- b000557 | furniture | pages [23] -->
MATHmodels

<!-- b000558 | furniture | pages [23] -->
获取更多资讯

<!-- b000559 | furniture | pages [24] -->
Team # 2401298

<!-- b000560 | furniture | pages [24] -->
Page 24 of 25

<!-- b000561 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000562 | caption | pages [24] -->
Figure 17: Momentum in Tennis

<!-- b000563 | prose | pages [24] -->
"Momentum" is not an isolated concept, it represents the existence of complex la- tent states of tennis matches, beyond what can be captured by simply counting points. Our study analyzed the intricate dynamics of momentum in tennis matches. We have utilized statistical models and a Duel-Temporal Bayesian Network to quantify and pre-

<!-- b000564 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000565 | prose | pages [24] -->
dict the influence of psychological and physiological factors on in-game performance. Our analysis suggests that while each point’s outcome may appears statistically inde- pendent to some extent, the Bayesian network we developed tells a richer story. It reveals the hidden threads of self-efficacy, strategy, and physiological responses that weave together to form the fabric of momentum.

<!-- b000566 | prose | pages [24] -->
To enable players to harness the positive aspects of momentum while mitigating its pressures, we recommend following strategic pivots:

<!-- b000567 | heading | pages [24] -->
1. Consistency is Key: Encourage players to minimize unforced errors; our findings

<!-- b000568 | prose | pages [24] -->
link consistent play to maintaining momentum.

<!-- b000569 | heading | pages [24] -->
2. Aggressiveness Pays Off: Advise players to assert dominance with net approaches

<!-- b000570 | prose | pages [24] -->
and serves to build positive momentum.

<!-- b000571 | heading | pages [24] -->
3. Serve Smart: Emphasize varied and accurate serving techniques to uphold

<!-- b000572 | prose | pages [24] -->
momentum without risking double faults.

<!-- b000573 | heading | pages [24] -->
4. Build Resilience: Cultivate players’ mental fortitude, essential for navigating the

<!-- b000574 | prose | pages [24] -->
pressures of break points and shifting tides within matches.

<!-- b000575 | heading | pages [24] -->
5. Lead to Succeed: Strive for early leads; our model suggests this exerts

<!-- b000576 | prose | pages [24] -->
psychological pressure on opponents, bolstering momentum for the leading player.

<!-- b000577 | prose | pages [24] -->
We trust this memo provides a clear and actionable strategy for leveraging the con- cept of momentum to your advantage. Implementing these recommendations could foster a competitive edge, vital for triumphing in the modern, fast-paced game of ten- nis.

<!-- b000578 | prose | pages [24] -->
Looking forward to seeing these strategies manifest in your players’ enhanced per- formance.

<!-- b000579 | prose | pages [24] -->
Yours Sincerely,

<!-- b000580 | furniture | pages [24] -->
Team #2401298

<!-- b000581 | prose | pages [24] -->
关注数学模型

<!-- b000582 | furniture | pages [24] -->
2

<!-- b000583 | furniture | pages [24] -->
MATHmodels

<!-- b000584 | furniture | pages [24] -->
获取更多资讯

<!-- b000585 | furniture | pages [25] -->
Team # 2401298

<!-- b000586 | heading | pages [25] -->
References

<!-- b000587 | furniture | pages [25] -->
Page 25 of 25

<!-- b000588 | references | pages [25] -->
[1] Taylor, J., & Demick, A. (1994). A multidimensional model of momentum in

<!-- b000589 | references | pages [25] -->
微信公众号：数学模型

<!-- b000590 | references | pages [25] -->
sports. _Journal of Applied Sport Psychology_, _6_(1), 51-70.

<!-- b000591 | references | pages [25] -->
[2] Klaassen, F. J., & Magnus, J. R. (2001). Are points in tennis independent and iden-

<!-- b000592 | references | pages [25] -->
tically distributed? Evidence from a dynamic binary panel data model. _Journal

<!-- b000593 | references | pages [25] -->
of the American Statistical Association_, _96_(454), 500-509.

<!-- b000594 | references | pages [25] -->
[3] Motoi, S., Misu, T., Nakada, Y., Yazaki, T., Kobayashi, G., Matsumoto, T., &

<!-- b000595 | references | pages [25] -->
Yagi, N. (2012). Bayesian event detection for sport games with hidden Markov

<!-- b000596 | references | pages [25] -->
model. _Pattern Analysis and Applications_, _15_, 59-72.

<!-- b000597 | references | pages [25] -->
[4] Sun, Y. (2004). Detecting the hot hand: An alternative model. In _Proceedings of

<!-- b000598 | references | pages [25] -->
the Annual Meeting of the Cognitive Science Society_ (Vol. 26, No. 26).

<!-- b000599 | references | pages [25] -->
[5] Klaassen, F. J., & Magnus, J. R. (2003). Forecasting the winner of a tennis

<!-- b000600 | references | pages [25] -->
微信号：MATHmodels

<!-- b000601 | references | pages [25] -->
match. _European Journal of Operational Research_, _148_(2), 257-267.

<!-- b000602 | references | pages [25] -->
[6] Ge, X., & Lin, A. (2021). Dynamic causality analysis using overlapped sliding

<!-- b000603 | references | pages [25] -->
windows based on the extended convergent cross-mapping. _Nonlinear Dynam-

<!-- b000604 | references | pages [25] -->
ics_, _104_, 1753-1765.

<!-- b000605 | references | pages [25] -->
[7] Morber, J. R. (2008). _One-dimensional nanowires: Understanding growth and

<!-- b000606 | references | pages [25] -->
properties as steps toward biomedical and electrical application_. Georgia Insti-

<!-- b000607 | references | pages [25] -->
tute of Technology.

<!-- b000608 | references | pages [25] -->
[8] Madhavan, V. (2016). Predicting NBA game outcomes with hidden Markov mod-

<!-- b000609 | references | pages [25] -->
els. _Berkeley University_.

<!-- b000610 | references | pages [25] -->
[9] Raab, M., Gula, B., & Gigerenzer, G. (2012). The hot hand exists in volleyball

<!-- b000611 | references | pages [25] -->
and is used for allocation decisions. _Journal of Experimental Psychology: Ap-

<!-- b000612 | references | pages [25] -->
plied_, _18_(1), 81.

<!-- b000613 | references | pages [25] -->
[10] https://github.com/JeffSackmann/tennis_MatchChartingProject.

<!-- b000614 | references | pages [25] -->
[11] Ben Gal I (2007). "Bayesian Networks" (PDF). In Ruggeri F, Kennett RS, Faltin

<!-- b000615 | references | pages [25] -->
FW (eds.). Support-Page. Encyclopedia of Statistics in Quality and Reliabil-

<!-- b000616 | references | pages [25] -->
ity. John Wiley & Sons. doi:10.1002/9780470061572.eqr089. ISBN 978-0-470-01861-

<!-- b000617 | references | pages [25] -->
3. Archived from the original (PDF) on 2016-11-23. Retrieved 2007-08-27.

<!-- b000618 | references | pages [25] -->
关注数学模型

<!-- b000619 | furniture | pages [25] -->
2

<!-- b000620 | furniture | pages [25] -->
MATHmodels

<!-- b000621 | furniture | pages [25] -->
获取更多资讯
