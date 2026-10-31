# P-C-2024-2401298-07d37078

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen C 2024 MCM/ICM Summary Sheet Team Control Number 2401298

<!-- b000002 | title | pages [1] -->
"Momentum" Exists In Tennis Game As Residual Effect - A Dual-Temporal Bayesian Network Model

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
This study investigates tennis match dynamics through sophisticated statistical modeling and a novel Dual-Temporal Bayesian Network approach. By analyzing Wimbledon data, we address five key questions:

<!-- b000005 | prose | pages [1] -->
Performance Metrics (Problem 1): We introduce a server/returner reweighting strategy to accurately evaluate the performance of a player. We further utilize sliding window and Area Under Curve (AUC) methods to ensure continuity and locality, thus better capturing the fluctuations within the game.

<!-- b000006 | prose | pages [1] -->
Momentum Existence (Problem 2): Rigorous hypothesis testing (Ljung-Box Q Test and Runs Test) fails to reject null hypothesis of complete randomness. But instantaneous winning rates can reveal slight deviations from randomness, suggesting the presence of subtle momentum effects, albeit not overwhelmingly conclusive.

<!-- b000007 | prose | pages [1] -->
Momentum Prediction (Problem 3): We take a 2-step approach. We first separate out the momentum effect by considering it as the residual of a Naive Binomial Model. Subsequently, we develop a Dual-Temporal Bayesian Network Model to predict this residual effect. The network incorporates various latent variables such as physiology, perception, and self-efficacy. An additional outcome of this model is the calculation of the importance of factors on momentum through the reduction of information entropy.

<!-- b000008 | prose | pages [1] -->
Predictive Analysis (Problem 4): Our model is tested on the Wimbledon 2023 competition, where it successfully predicts most match fluctuations. We analyze instances of failure and propose potential future enhancements. The model framework is also applied to an additional dataset of female tennis matches, revealing intriguing differences. Most importantly, we generalize our data into a universal framework for predicting momentum in sports games.

<!-- b000009 | prose | pages [1] -->
Coaching Strategies (Memo) : Finally, we draft a memo for coaches, synthesizing our findings into statistical findings and targeted recommendations of minimising errors, strategic aggression, resilience building, and more. Our goal is to offer a competitive advantage.

<!-- b000010 | prose | pages [1] -->
Our findings highlight the complexity of tennis match dynamics, combining rigorous statistical validation with sophisticated predictive modeling. Our model not only demonstrates effective prediction and significant robustness but is also broadly applicable across various sports scenarios.

<!-- b000011 | keywords | pages [1] -->
Keywords: Tennis, Momentum, Bayesian Networks, Statistical Analysis, Performance Metrics.

<!-- b000012 | furniture | pages [1] -->
微信公众号：数学模型 微信号：MATHmodels 关注数学模型 获取更多资讯 2 MATHmodels

<!-- b000013 | furniture | pages [2] -->
Team # 2401298

<!-- b000014 | furniture | pages [2] -->
Page 2 of 25

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Introduction

<!-- b000017 | contents | pages [2] -->
3

<!-- b000018 | contents | pages [2] -->
1.1

<!-- b000019 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [2] -->
3

<!-- b000021 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000022 | contents | pages [2] -->
1.2

<!-- b000023 | contents | pages [2] -->
Clarifications and Restatements . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
3

<!-- b000025 | contents | pages [2] -->
1.3

<!-- b000026 | contents | pages [2] -->
Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | contents | pages [2] -->
2 Preparation for Modeling

<!-- b000029 | contents | pages [2] -->
4

<!-- b000030 | contents | pages [2] -->
2.1

<!-- b000031 | contents | pages [2] -->
Model Assumptions

<!-- b000032 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
4

<!-- b000034 | contents | pages [2] -->
2.2

<!-- b000035 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
4

<!-- b000037 | contents | pages [2] -->
2.3

<!-- b000038 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
3 Problem 1: Probability Difference Evaluation Strategy

<!-- b000041 | contents | pages [2] -->
5

<!-- b000042 | contents | pages [2] -->
3.1

<!-- b000043 | contents | pages [2] -->
Important Impact of Server

<!-- b000044 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
5

<!-- b000046 | contents | pages [2] -->
3.2

<!-- b000047 | contents | pages [2] -->
Sliding Point Interval Approach . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
6

<!-- b000049 | contents | pages [2] -->
3.3

<!-- b000050 | contents | pages [2] -->
Sliding Time Window Approach

<!-- b000051 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
7

<!-- b000053 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000054 | contents | pages [2] -->
4 Problem 2: Momentum Existence

<!-- b000055 | contents | pages [2] -->
8

<!-- b000056 | contents | pages [2] -->
4.1

<!-- b000057 | contents | pages [2] -->
Hypothesis Testing Preparation . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
8

<!-- b000059 | contents | pages [2] -->
4.2

<!-- b000060 | contents | pages [2] -->
Ljung-Box Q Test and Runs Test Statistical Analysis . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
9

<!-- b000062 | contents | pages [2] -->
4.3

<!-- b000063 | contents | pages [2] -->
Instantaneous Winning Rates . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
10

<!-- b000065 | contents | pages [2] -->
5 Problem 3: Momentum Prediction

<!-- b000066 | contents | pages [2] -->
11

<!-- b000067 | contents | pages [2] -->
5.1

<!-- b000068 | contents | pages [2] -->
The building block: Naive Binomial Model . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
11

<!-- b000070 | contents | pages [2] -->
5.2

<!-- b000071 | contents | pages [2] -->
Momentum as residual effect

<!-- b000072 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
12

<!-- b000074 | contents | pages [2] -->
5.2.1

<!-- b000075 | contents | pages [2] -->
Variable identification . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
13

<!-- b000077 | contents | pages [2] -->
5.2.2

<!-- b000078 | contents | pages [2] -->
Model Construction

<!-- b000079 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
15

<!-- b000081 | contents | pages [2] -->
5.2.3

<!-- b000082 | contents | pages [2] -->
Data fitting

<!-- b000083 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
17

<!-- b000085 | contents | pages [2] -->
5.2.4

<!-- b000086 | contents | pages [2] -->
Inference on Match Data . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
19

<!-- b000088 | contents | pages [2] -->
5.2.5

<!-- b000089 | contents | pages [2] -->
Advisement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
19

<!-- b000091 | contents | pages [2] -->
6 Problem 4 : Swings Prediction and Model Generalization

<!-- b000092 | contents | pages [2] -->
20

<!-- b000093 | contents | pages [2] -->
7 Model Analysis

<!-- b000094 | contents | pages [2] -->
22

<!-- b000095 | contents | pages [2] -->
7.1

<!-- b000096 | contents | pages [2] -->
Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
22

<!-- b000098 | contents | pages [2] -->
7.2

<!-- b000099 | contents | pages [2] -->
Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
22

<!-- b000101 | contents | pages [2] -->
7.3

<!-- b000102 | contents | pages [2] -->
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
23

<!-- b000104 | contents | pages [2] -->
8 Memorandum

<!-- b000105 | contents | pages [2] -->
23

<!-- b000106 | contents | pages [2] -->
References

<!-- b000107 | contents | pages [2] -->
25

<!-- b000108 | contents | pages [2] -->
关注数学模型

<!-- b000109 | furniture | pages [2] -->
2

<!-- b000110 | furniture | pages [2] -->
MATHmodels

<!-- b000111 | furniture | pages [2] -->
获取更多资讯

<!-- b000112 | furniture | pages [3] -->
Team # 2401298

<!-- b000113 | furniture | pages [3] -->
Page 3 of 25

<!-- b000114 | heading | pages [3] -->
1 Introduction

<!-- b000115 | heading | pages [3] -->
1.1 Problem Background

<!-- b000116 | prose | pages [3] -->
微信公众号：数学模型 The historic Wimbledon 2023 match between Carlos Alcaraz and Novak Djokovic illuminated the profound impact of momentum in tennis. This match not only capti- vated tennis enthusiasts but also highlighted a complex, yet underexplored, aspect of competitive sports: the ability of players to shift the match’s dynamics through "mo- mentum". The significance of momentum in determining match outcomes has become [9]. This a key area of interest. Volleyball players even use this for allocation decisions underscores the need for a sophisticated model that captures the essence of momentum and explains the underlying rationale.

<!-- b000117 | heading | pages [3] -->
1.2 Clarifications and Restatements

<!-- b000118 | prose | pages [3] -->
微信号：MATHmodels Our task revolves around developing a quantifiable model of momentum in tennis, which aims to identify key indicators of momentum shifts, evaluate their impact on match results, and discern the extent to which these shifts can be attributed to skill, strategy, or mere chance. We will do the following steps:

<!-- b000119 | prose | pages [3] -->
1. create a model that delineates the flow of a tennis match, quantifying player perfor- mance over time.

<!-- b000120 | prose | pages [3] -->
2. construct a hypothesis testing framework to evaluate whether swings in matches are due to momentum or mere chance.

<!-- b000121 | prose | pages [3] -->
3. use our model to predict changes in match dynamics, identifying potential indica- tors signaling a shift in match.

<!-- b000122 | prose | pages [3] -->
4. test the predictive power of our model across various matches, surfaces, and possi- bly other similar sports, assessing its generalizability.

<!-- b000123 | prose | pages [3] -->
5. synthesize our findings into actionable strategies for coaches, aiding them in prepar- ing players for shifts in match dynamics and responding effectively to momentum changes during play.

<!-- b000124 | heading | pages [3] -->
1.3 Our work

<!-- b000125 | prose | pages [3] -->
In response to this challenge, our approach intertwines statistical analysis, machine learning techniques, and dynamic simulations to forge a comprehensive model of ten- nis momentum. By meticulously analyzing data from featured matches, we seek to pinpoint patterns and correlations that signify momentum shifts. Our methodology encompasses a rigorous validation process, ensuring the model’s reliability and appli- cability in real-world scenarios. Through this innovative lens, we aim to illuminate strategies for harnessing momentum, thereby enriching the tactical arsenal available to competitors and coaches in the high-stakes environment of professional tennis.

<!-- b000126 | prose | pages [3, 4] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000127 | furniture | pages [3] -->
2

<!-- b000128 | furniture | pages [3] -->
MATHmodels

<!-- b000129 | furniture | pages [3] -->
获取更多资讯

<!-- b000130 | furniture | pages [4] -->
Team # 2401298

<!-- b000131 | furniture | pages [4] -->
Page 4 of 25

<!-- b000133 | caption | pages [4] -->
Figure 1: Framework of Our Work

<!-- b000134 | heading | pages [4] -->
2 Preparation for Modeling

<!-- b000135 | heading | pages [4] -->
2.1 Model Assumptions

<!-- b000136 | prose | pages [4] -->
Some fundamental assumptions are listed below.

<!-- b000137 | prose | pages [4] -->
• Assumption 1: Factors such as weather, crowd support, and minor injuries do not significantly affect the match outcome.

<!-- b000138 | prose | pages [4] -->
→Justification: While these factors can influence a match, including them in a model adds complexity and unpredictability. For a broad analysis, it’s practical to focus on more measurable and consistent factors.

<!-- b000139 | prose | pages [4] -->
• Assumption 2: A player’s current world ranking is reliable indicators of their potential performance in an upcoming match.

<!-- b000140 | prose | pages [4] -->
→Justification: Rankings are based on a player’s performance in tournaments over a rolling period, reflecting their overall ability.

<!-- b000141 | heading | pages [4] -->
2.2 Notations

<!-- b000142 | prose | pages [4] -->
Some primary notations are listed below.

<!-- b000143 | prose | pages [4, 5] -->
关注数学模型 Symbol Definition M 1 the probability that player 1 wins a point regardless of the server 微信公众号：数学模型 AUC Area Under Curve, a measure of model accuracy Q Ljung-Box statistic Z Z-score for Runs Test r1 or r2 Expected losing round for player 1 or player 2 B Intrinsic probability function of winning a point λ The parameter determining Duel-Temporal Bayesian Network L the likelihood of data from 1 match between players E Momentum effect as difference between actual and expected points

<!-- b000144 | furniture | pages [4] -->
2

<!-- b000145 | furniture | pages [4] -->
MATHmodels

<!-- b000146 | furniture | pages [4] -->
获取更多资讯

<!-- b000147 | furniture | pages [5] -->
Team # 2401298

<!-- b000148 | furniture | pages [5] -->
Page 5 of 25

<!-- b000149 | caption | pages [5] -->
Table 1: Notations Table

<!-- b000151 | heading | pages [5] -->
2.3 Data Cleaning

<!-- b000152 | prose | pages [5] -->
微信号：MATHmodels After observing the Wimbledon_featured_matches.csv data set, we handle outlier values in column elapsed_time (rows 586 to 636), and delete the speed_mph column because of a significant number of missing values in it, which can impact the whole analysis.

<!-- b000153 | heading | pages [5] -->
3 Problem 1: Probability Difference Evaluation Strategy

<!-- b000154 | heading | pages [5] -->
3.1 Important Impact of Server

<!-- b000155 | prose | pages [5] -->
Let’s consider the change in the points difference between player 1 and player 2 in a match, according to Wimbledon_featured_matches.csv data set, we subtract p2_points_won data from p1_points_won to get points difference, namely:

<!-- b000156 | prose | pages [5] -->
points difference = p1_points_won - p2_points_won (1)

<!-- b000157 | prose | pages [5] -->
This formula helps us visualize the flow of a match, as depicted in the graph below, which highlights points difference over time:

<!-- b000158 | caption | pages [5] -->
Figure 2: Points Difference for Match 2023-wimbledon-1301

<!-- b000159 | prose | pages [5] -->
Where two colored dotted lines have also been added: green represents the server 关注数学模型 from player 1 to player 2, and purple represents the server from player 2 to player 1.

<!-- b000160 | furniture | pages [5] -->
2

<!-- b000161 | furniture | pages [5] -->
MATHmodels

<!-- b000162 | furniture | pages [5] -->
获取更多资讯

<!-- b000163 | furniture | pages [6] -->
Team # 2401298

<!-- b000164 | furniture | pages [6] -->
Page 6 of 25

<!-- b000165 | prose | pages [6] -->
A key observation is that the player currently serving has a higher chance of win- ning the point, especially when point number = [20, 50] or [180, 220] . However, the overall trend of points difference remains relatively stable, regardless of who serves, indicating that serving alone doesn’t drastically shift match momentum. So, we cannot 微信公众号：数学模型 be influenced by who is the server when we try to identify which player is performing better at a given time in the match.

<!-- b000166 | heading | pages [6] -->
3.2 Sliding Point Interval Approach

<!-- b000167 | prose | pages [6] -->
To further analyse match dynamics, we focus on the probability difference between the players winning a point. In a match, the performance of two players depends on the probability difference M 1 or M 2, M 1 is the probability that player 1 wins a point regardless of the server, and M 2 is the probability that player 2 wins a point regardless of the server.

<!-- b000168 | prose | pages [6] -->
Next, according to the column point_no in the given data set, we can calculate p1 微信号：MATHmodels and p2 by choosing a fixed length ω of the data, p1 is the probability that player 1 wins a point on serve and p2 is the probability that player 2 wins a point on serve, ω is the point interval. If player 1 serves n1 times and player 2 serves n2 times (where w = n1 + n2), player 1 wins x1 points and player 2 wins x2 points, then p1 = x1 n1 and p2 = x2 n2. Actually,   1 −p2 p1 we can obtain the performance metric: . If player 1 and player 2 have 1 −p1 p2 the same chance of serving, the ideal value of p1 and p2 should be equal, then

<!-- b000169 | prose | pages [6] -->
 1 M 1    1 −p2 p1 21 = (2) M 2 1 −p1 p2 2

<!-- b000170 | prose | pages [6] -->
When M 1 > 0.5, it means player 1 performs better than player 2, and for M 1 < 0.5 the opposite. Futhermore, the higher the value, the better the performance of the player 1, thus it can identify which player is performing better at a given time in the match, as well as how much better they are performing.

<!-- b000171 | prose | pages [6] -->
To visualize the differenent performance of players 1 and 2, we bring in a rolling window of length ω. For each match, we can utilize this "rolling window" to calcu- late the difference between the performance of player 1 and player 2, and combined with cubic spline interpolation, we can plot the corresponding change in the degree of performance, and draw the following curve (ω = 30):

<!-- b000172 | caption | pages [6] -->
Figure 3: Probability Difference for Match 2023-wimbledon-1301

<!-- b000173 | prose | pages [6, 7] -->
Where the abscissa is the total number of points scored in a match (the number关注数学模型 pluses 1 when two players finish a ball, corresponding to the column point_no in the given data), the ordinate represents the probability difference M 1. Compared with Figure 2, we find that the changing of the server has nothing to do with the probability difference, which means comparing with the probability difference is more significant 微信公众号：数学模型 than comparing with the points difference.

<!-- b000174 | furniture | pages [6] -->
2

<!-- b000175 | furniture | pages [6] -->
MATHmodels

<!-- b000176 | furniture | pages [6] -->
获取更多资讯

<!-- b000177 | furniture | pages [7] -->
Team # 2401298

<!-- b000178 | furniture | pages [7] -->
Page 7 of 25

<!-- b000180 | prose | pages [7] -->
From Figure 3, the part above the red line indicates that player 1 (Carlos Alcaraz) is better than player 2 (Nicolas Jarry), and the part below the red line indicates that player 2 (Nicolas Jarry) is better than player 1 (Carlos Alcaraz), besides, the position of the peaks and valleys indicates that the player is performing particularly well.

<!-- b000181 | heading | pages [7] -->
3.3 Sliding Time Window Approach

<!-- b000182 | prose | pages [7] -->
However, it is not enough to select data points to draw according to the uniform interval of the total score, we should also do even segmentation from the perspective of the time of the game, remember that L represents the length of the time window, 微信号：MATHmodels λ represents the step size of each time window move, replace the point number with ti as the abscissa, ti = λ seconds, 2λ seconds, . . . For instance, if L = 600 seconds is used as the length of the time window, two players may play a total of 12 points or 18 points, and then set λ = 60 seconds as the step size of the time window movement, the result is more reflective of the player’s performance and more natural.

<!-- b000183 | prose | pages [7] -->
By adjusting different L and λ, we plot the variation as follows:

<!-- b000184 | caption | pages [7] -->
Figure 4: Performance Evaluation with Different Windows for Match 2023-wimbledon-1301

<!-- b000185 | prose | pages [7] -->
We can observe from the graph that the player’s performance at certain moments is dramatically affected by the length of the time window L while slightly affected by the step size of each time window movement λ. Generally, small window introduces noises while large window are unable to depict the rapidly changing dynamic of the game. To solve this, one common method is to apply filters, such as Gaussian filter, which requires a specific kernel function. This requires altering Formula 2. But we here propose a simpler yet equally effective approach named AUC (area under curve), as defined in the following formula:

<!-- b000186 | prose | pages [7, 8] -->
Z Lmax 1 A(t) = ML(t) dL (3) Lmax −Lmin Lmin Where ML(t) denotes the performance of one player at time t when considering win- dow length L . In practice we can simply discretize dL to be 1. Similar to kernal-based关注数学模型 methods, AUC also weights the points winning with temporal distance (this can be easily seen by expressing ML(t) as sum of indicator functions then switching the sum- mation order, we skip the details here). The following is the generated graph using this method. 微信公众号：数学模型 微信号：MATHmodels

<!-- b000187 | furniture | pages [7] -->
2

<!-- b000188 | furniture | pages [7] -->
MATHmodels

<!-- b000189 | furniture | pages [7] -->
获取更多资讯

<!-- b000190 | furniture | pages [8] -->
Team # 2401298

<!-- b000191 | furniture | pages [8] -->
Page 8 of 25

<!-- b000193 | caption | pages [8] -->
Figure 5: AUC-Time Plot for Match 2023-wimbledon-1301

<!-- b000194 | prose | pages [8] -->
From this graph we can determine which player is performing better at a certain time. When the curve is above 0.5, player 1 takes an upper hand, while the contrary happens when player 2 performs better. And the farther the curve’s distance from the equilibrium line, the greater the difference between players’ performance.

<!-- b000195 | heading | pages [8] -->
4 Problem 2: Momentum Existence

<!-- b000196 | prose | pages [8] -->
Given our analysis revealing potential patterns in "momentum", we now rigorously examine these observations through hypothesis testing to validate the presence of mo- mentum.

<!-- b000197 | heading | pages [8] -->
4.1 Hypothesis Testing Preparation

<!-- b000198 | prose | pages [8] -->
We first constructed the Hypothesis Testing Framework:

<!-- b000199 | prose | pages [8] -->
Null Hypothesis (H0): For a fixed server, the scoring of points by a player is inde- pendent and identically distributed (i.i.d.) and thus follows a binomial distribution. Alternative Hypothesis (H1): The complement of H0, suggesting that scoring is not entirely random, and some form of "momentum" or sequence dependency exists.

<!-- b000200 | prose | pages [8] -->
To evaluate the claim regarding the non-existence of "momentum", we denoted that in any given match, when Player 1 serves, the probability of Player 1 winning a point is p1, and when Player 2 serves, the probability of Player 1 winning a point is p2. The calculation of these probabilities, p1 and p2, is explained in Section 3.

<!-- b000201 | prose | pages [8, 9] -->
For each match, we calculated the winning probabilities by: counting the number of points won and the total number of serves by Player 1 to calculate p1 and counting关注数学模型 the number of points won by Player 1 against the total serves of Player 2 to calculate p2.

<!-- b000202 | furniture | pages [8] -->
2

<!-- b000203 | furniture | pages [8] -->
MATHmodels

<!-- b000204 | furniture | pages [8] -->
获取更多资讯

<!-- b000205 | furniture | pages [9] -->
Team # 2401298

<!-- b000206 | furniture | pages [9] -->
Page 9 of 25

<!-- b000208 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000209 | heading | pages [9] -->
4.2 Ljung-Box Q Test and Runs Test Statistical Analysis

<!-- b000210 | prose | pages [9] -->
If scoring was entirely random, we would expect no significant autocorrelation be- tween consecutive points.

<!-- b000211 | prose | pages [9] -->
We separate out the scenarios for Player 1’s serve and Player 2’s serve and build se- quences for each match.Then calculate the autocorrelation for each sequence and Em- ploy an appropriate statistical test (Ljung-Box Q test) to assess whether the sequence’s autocorrelation is significant.

<!-- b000212 | prose | pages [9] -->
The statistic for the Ljung-Box Q test is calculated as follows:

<!-- b000213 | prose | pages [9] -->
h ˆρ2 X k Q = n(n + 2) (4) 微信号：MATHmodels n −k k=1

<!-- b000214 | prose | pages [9] -->
Where: n is the sample size of the time series. h is the maximum number of lags considered for autocorrelation detection. ˆρk is the sample autocorrelation coefficient at lag k. Q is the Ljung Box statistic, which follows an approximate chi square distribution under the null hypothesis with degrees of freedom h −m, where m is the number of parameters in the model (for simple time series analysis, m is typically taken as m = 0).

<!-- b000215 | prose | pages [9] -->
The Ljung-Box Q test results for the first match, with a corresponding p-value of 0.497 for autocorrelations up to 10 observations, indicated a p-value greater than com- mon significance levels (e.g., 0.05). The results of other matches are similar. This sug- gests insufficient evidence to reject the null hypothesis H0.

<!-- b000216 | prose | pages [9] -->
Then we conducted the runs test to analyze the number of "runs" in a data sequence, where a "run" is defined as a sequence of identical elements occurring consecutively. We calculate the Expected Number of Runs and Variance,and get theZ-Score by:

<!-- b000217 | prose | pages [9] -->
Z = (R −E[R]) (5) p V ar(R)

<!-- b000218 | prose | pages [9] -->
Where: R represents the actual number of runs. E[R] is the expected number of runs, calculated as E[R] = 1+ 2n1n2 n1+n2. Var(R) is the variance of the number of runs, calculated as Var(R) = 2n1n2(2n1n2−n1−n2) (n1+n2)2(n1+n2−1) . n1 and n2 are the counts of the two outcomes (e.g., wins and losses) in the sequence.

<!-- b000219 | prose | pages [9] -->
Then we calculate the P-Value Calculation by: P = 2(1 −Φ(|Z|)) to get the P = 0.691, which is greater than common significance levels (e.g., 0.05) suggests that the hypothesis of the points being i.i.d cannot be dismissed. The results of other matches are similar.

<!-- b000220 | prose | pages [9] -->
Here we plot the results of 2 methods with different matches. As evidenced by P values exceeding the 0.05 benchmark across various matches except for a few ones, we cannot reject the H0 for most matches.

<!-- b000221 | prose | pages [9, 10] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000222 | furniture | pages [9] -->
2

<!-- b000223 | furniture | pages [9] -->
MATHmodels

<!-- b000224 | furniture | pages [9] -->
获取更多资讯

<!-- b000225 | furniture | pages [10] -->
Team # 2401298

<!-- b000226 | furniture | pages [10] -->
Page 10 of 25

<!-- b000228 | caption | pages [10] -->
Figure 6: feature importance

<!-- b000229 | heading | pages [10] -->
4.3 Instantaneous Winning Rates

<!-- b000230 | prose | pages [10] -->
[4], we employed To check the i.i.d. argument, inspired by the paper [Sun, Y., 2004] an instantaneous winning rate approach. This rate refers to the probability of a player winning the next point immediately after winning a point, under a constant server con- dition. We calculated and compared the instantaneous winning rates in two scenarios: The rate at which Player 1 wins the next point immediately after winning a point while serving and the rate at which Player 1 wins the next point immediately after winning a point against Player 2’s serve.

<!-- b000231 | caption | pages [10] -->
Table 2: Probability of Winning Based on Serving State

<!-- b000232 | prose | pages [10] -->
P of winning when serving P of winning when not serving Player and State

<!-- b000233 | prose | pages [10] -->
Player 2 0.6874 0.3406 Player 1immediate 0.6978 0.3498 Player 2 0.6594 0.3126 Player 2immediate 0.6683 0.3261

<!-- b000234 | prose | pages [10] -->
The observed increase in winning rates by around 1% might indicate the influence of momentum, challenging the claim of randomness in scoring sequences within tennis matches.

<!-- b000235 | prose | pages [10] -->
Delving into the subtleties of the match data revealed an intriguing pattern: players demonstrated a marginally increased probability of securing the next point following a win, whether serving or returning. While the data does not overwhelmingly endorse the notion of momentum, it does quietly nod to its existence.

<!-- b000236 | prose | pages [10] -->
关注数学模型

<!-- b000237 | furniture | pages [10] -->
2

<!-- b000238 | furniture | pages [10] -->
MATHmodels

<!-- b000239 | furniture | pages [10] -->
获取更多资讯

<!-- b000240 | furniture | pages [11] -->
Team # 2401298

<!-- b000241 | furniture | pages [11] -->
Page 11 of 25

<!-- b000242 | heading | pages [11] -->
5 Problem 3: Momentum Prediction

<!-- b000243 | heading | pages [11] -->
5.1 The building block: Naive Binomial Model

<!-- b000244 | prose | pages [11] -->
微信公众号：数学模型 One immediate issue in identifying "momentum" in competition is that all variables we observe are mixed with the momentum effect and the effect from the skill level difference of the players. In order to "separate out" the effect of momentum, we first develop a naive model without considering any momentum. Or, equivalently, a model under the assumption that the points won are identically distributed random variables.

<!-- b000245 | prose | pages [11] -->
[5]. We term this model the Binomial Model, denoted by BM

<!-- b000246 | prose | pages [11] -->
To develop this model, we collect the world rank of players as additional prior information ... And convert them into relative rank in 2023 Wimbledon competition. By "relative", we re-rank the 32 players according to their rankings relative to each other, resulting an array of integers between 1 and 32. Then BM is simply a function of (Rank1, Rank2).

<!-- b000247 | prose | pages [11] -->
微信号：MATHmodels Our Binomial model takes the rank of two players then return the "intrinsic proba- bility" of winning a certain point, which under the naive assumption, stay constantly across the whole match.

<!-- b000248 | prose | pages [11] -->
It’s notable that in tennis competition, strength difference between top rank players are often more evident than players with lower ranks. For example, we may expect the difference between rank 1 and rank 2 players larger than the difference between rank 31 and rank 32 players. On the contrary, the notion of "expected losing round" [5]. Specifically, we define can capture this prior well

<!-- b000249 | prose | pages [11] -->
r1 = 6 −log2(Rank1) (6)

<!-- b000250 | prose | pages [11] -->
Consequently, we can define BM(Rank1, Rank2) := f1(r1, r2). Set f2(x, y) = f1(x+y 2 , x−y 2 ) we have BM = f2(r1 −r2, r1 + r2) . We provide the following approximation for f2 :

<!-- b000251 | prose | pages [11] -->
eλ(r1−r2) f2(r1 −r2, r1 + r2) = 1 + eλ(r1−r2) + s (7)

<!-- b000252 | prose | pages [11] -->
Where s > 0 is the server advantage. Alternatively, we can set the right hand side as eλ(r1−r2)+µ(r1+r2) 1+eλ(r1−r2)+µ(r1+r2) + s with more parameters.

<!-- b000253 | prose | pages [11] -->
But during experiment we have found the value of mu to be considerably small thus we ignore it here. Ideally, if the Formula (6) has captured the rank-strength relationship well enough, then this simplification makes sense. Refer to [Klaassen and Magnus, [2] for further justification. 2001]

<!-- b000254 | prose | pages [11] -->
We then estimate the parameter λ on our point-to-point data of 31 matches by max- imizing the likelyhood.

<!-- b000255 | prose | pages [11] -->
Step 1: Likelihood Function

<!-- b000256 | prose | pages [11, 12] -->
Assuming the outcomes of individual points are independent (an assumption of our naive model), the likelihood of observing the data from a single match between player 1 and player 2, where player 1 wins n1 points and player 2 wins n2 points, can be represented as a binomial distribution: 关注数学模型 n1  n2 eλ(r1−r2) eλ(r1−r2) n1 + n2    L(λ, s|n1, n2) = 1 − 1 + eλ(r1−r2) + s 1 + eλ(r1−r2) + s (8) n1 微信公众号：数学模型 Step 2: Log-Likelihood

<!-- b000257 | furniture | pages [11] -->
2

<!-- b000258 | furniture | pages [11] -->
MATHmodels

<!-- b000259 | furniture | pages [11] -->
获取更多资讯

<!-- b000260 | furniture | pages [12] -->
Team # 2401298

<!-- b000261 | furniture | pages [12] -->
Page 12 of 25

<!-- b000263 | prose | pages [12] -->
To simplify calculations and to deal with potential numerical underflow, it’s com- mon to work with the log-likelihood rather than the likelihood itself.

<!-- b000264 | prose | pages [12] -->
! !! eλ(r1−r2) eλ(r1−r2) n1 + n2  log L(λ, s|n1, n2) = log 1 − +n1 log 1 + eλ(r1−r2) + s +n2 log 1 + eλ(r1−r2) + s n1 (9)

<!-- b000265 | prose | pages [12] -->
Step 3: Aggregate Log-Likelihood Over All Matches

<!-- b000266 | prose | pages [12] -->
To estimate λ, s using data from all 31 matches, we sum the log-likelihoods across 微信号：MATHmodels all matches:

<!-- b000267 | prose | pages [12] -->
X log L(λ, s|n1, n2) log L(λ, s) = (10) matches

<!-- b000268 | prose | pages [12] -->
Step 4: Maximizing the Log-Likelihood

<!-- b000269 | prose | pages [12] -->
Owing to the smoothness of the function, we can easily apply Newton method, which requires the computation of first and second derivative, to iteratively adjust λ, s to find the maximum. The optimal value is computed as lambda = 0.0624, s = 0.1742 .

<!-- b000270 | heading | pages [12] -->
5.2 Momentum as residual effect

<!-- b000271 | prose | pages [12] -->
It’s easy for us to observe the equivalence between no momentum statement and ⇐⇒ memoryless statement. "Momentum doesn’t exist" "The process of winning points is independent of the past of the game, or in another word, memoryless"

<!-- b000272 | prose | pages [12] -->
Now by inversing both sides, we can measure the momentum effect as:

<!-- b000273 | prose | pages [12] -->
E := S −ˆS (11)

<!-- b000274 | prose | pages [12] -->
Where S is the points winning in reality while ˆS is the points winning predicted by the Binomial model. Since no strict definition of momentum exists as a statistic. We now use formula (11) to define the value of momentum. This formula can be under- stand intuitively, as previous critics on momentum often describe it as “seeing some- [4] thing out of randomness.”

<!-- b000275 | prose | pages [12] -->
In order to design a model to predict the residual, there are several key facts worth noticing:

<!-- b000276 | prose | pages [12] -->
The reason why "momentum" is so hard to grasp statistically is that this concept implies some "hidden state" exists in the system of sports play. So a generative model is preferred. The direct 1-step prediction can be extremely noisy and thus posing a challenge for effective model-fitting. We need specific approach to reduce the impact of the noise. The influence of past game state should be encoded in this model. And 关注数学模型 the effect from the past could potentially last for a long time.

<!-- b000277 | furniture | pages [12] -->
2

<!-- b000278 | furniture | pages [12] -->
MATHmodels

<!-- b000279 | furniture | pages [12] -->
获取更多资讯

<!-- b000280 | furniture | pages [13] -->
Team # 2401298

<!-- b000281 | furniture | pages [13] -->
Page 13 of 25

<!-- b000282 | prose | pages [13] -->
Taking all these into account, we introduce our novel Duel-Temporal Bayesian Net- work. As a variation of normal Dynamical Bayesian Network, it not only constructs a hidden model for the tennis game play, but also encodes long-short term memory from the past, enabling a comprehensive detection of "momentum". 微信公众号：数学模型

<!-- b000283 | heading | pages [13] -->
5.2.1 Variable identification

<!-- b000284 | prose | pages [13] -->
In tennis, what’s not seen can be just as influential as the scoreboard. For example, a player’s sudden surge or dip in performance isn’t always from the visible aces or double faults. It’s often the hidden triggers – maybe how the match’s strain is weighing on their shoulders – that can turn the tide. A tennis game is not only a competition in strength or technique, but also involves complicated psychological and physiological dynamics.

<!-- b000285 | prose | pages [13] -->
[1], we see that momentum is a complex Drawing from the insights of [Taylor J., 1994] system of cognition, physiology, and emotion, all sparked by precipitating events and 微信号：MATHmodels manifesting in performance changes. This paper’s concept of a "momentum chain", which suggests that an initial event can trigger alterations in an athlete’s cognition, affect, and physiology, leading to behavioral changes that influence performance, res- onates with the invisible forces at play in tennis, guiding us to consider latent variables.

<!-- b000286 | prose | pages [13] -->
Based on this framework, we select 3 latent variables in our model: "Physiology", "perception of control", and "self-efficacy". They play a crucial role in capturing the complex, non-observable factors that influence the momentum swings in a tennis match.

<!-- b000287 | heading | pages [13] -->
1. Physiology: The physical condition of the players, like fatigue, energy levels,

<!-- b000288 | prose | pages [13] -->
and even subtle injuries.

<!-- b000289 | heading | pages [13] -->
2. Perception of Control: This represents a player’s ability to control the match.

<!-- b000290 | prose | pages [13] -->
3. Self-efficacy: Self-efficacy is a player’s belief in their capability,which is the fuel that powers player’s persistence.

<!-- b000291 | prose | pages [13] -->
[1], precipitating events, such as specific shots, critical According to [Taylor J., 1994] points shift a player’s mental and physiological state indirectly. These hidden state are the undercurrents of the game, unseen but vital. Incorporating these into our model allows for a more accurate understanding and prediction of momentum swings.

<!-- b000292 | prose | pages [13] -->
Then we get the diagram below. The arrows in the following diagram represent influential relationships between various factors. This complex network of influences reflects the multifaceted nature of competitive sports, where physical, mental, and sit- uational factors all intertwine to affect the outcome of a match.

<!-- b000293 | prose | pages [13, 14] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000294 | furniture | pages [13] -->
2

<!-- b000295 | furniture | pages [13] -->
MATHmodels

<!-- b000296 | furniture | pages [13] -->
获取更多资讯

<!-- b000297 | furniture | pages [14] -->
Team # 2401298

<!-- b000298 | furniture | pages [14] -->
Page 14 of 25

<!-- b000300 | caption | pages [14] -->
Figure 7: Identified Variables

<!-- b000301 | prose | pages [14] -->
Due to the limitation of our data (only 31 matches), a complicated model like this is prone to overfitting and thus not suitable for robustness prediction. To simplify the model construction, we utilized random forest to search for variables that are insignif- icant for prediction.Here are some top features:

<!-- b000302 | caption | pages [14] -->
Table 3: Feature Importance

<!-- b000303 | prose | pages [14] -->
p1_unf_err p2_winner p2_unf_err p1_winner Feature Importance 0.120587 0.111018 0.101907 0.094330 server rally_count p2_net_pt_won game_victor Feature Importance 0.084700 0.081359 0.047800 0.043592 p1_net_pt_won p2_distance_run p1_distance_run Feature Importance 0.032918 0.032348 0.032152

<!-- b000304 | prose | pages [14] -->
To simplify our network, we should visualize the correlation between features us- ing a correlation heatmap. This is crucial for feature engineering. The correlation heatmap of the top-10 features shows the relationships between variables that are most predictive of the point victor in a tennis match. Here are some insights from the heatmap:

<!-- b000305 | prose | pages [14] -->
Unforced Errors (p_1_unf_err, p_2_unf_err): These features show a significant cor- relation with the outcome of points, implying that players’ mistakes can crucially in- fluence point results.

<!-- b000306 | prose | pages [14] -->
Winners (p_1_winner, p_2_winner): Points won by players due to winning shots are highly correlated with the match outcome.

<!-- b000307 | prose | pages [14, 15] -->
Serving (server): The role of the server in a point has a notable correlation with关注数学模型 point outcomes.

<!-- b000308 | furniture | pages [14] -->
2

<!-- b000309 | furniture | pages [14] -->
MATHmodels

<!-- b000310 | furniture | pages [14] -->
获取更多资讯

<!-- b000311 | furniture | pages [15] -->
Team # 2401298

<!-- b000312 | furniture | pages [15] -->
Page 15 of 25

<!-- b000314 | prose | pages [15] -->
Physical and Strategic Aspects (rally_count, p_1_net_pt_won, p_2_net_pt_won): These features suggest the physical exertion and strategic play involved in points, such as longer rallies and successful net plays contributing to point outcomes. 微信公众号：数学模型 This reveals several layers of the game that potentially contribute to momentum, such as the direct impact like unforced errors, winning shots, and the advantage con- ferred by serving. Additionally, the physical and strategic elements like rally counts and net points could influence a player’s dominance during a match as well.

<!-- b000315 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000316 | caption | pages [15] -->
Figure 8: Correlation Heatmap of Top-10 Features

<!-- b000317 | heading | pages [15] -->
5.2.2 Model Construction

<!-- b000318 | prose | pages [15] -->
Through this method, we ascertained and dropped insignificant features such as physiology. The remaining features forms the bedrock of our network. The simplified version is depicted in the following graph:

<!-- b000319 | prose | pages [15, 16] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000320 | furniture | pages [15] -->
2

<!-- b000321 | furniture | pages [15] -->
MATHmodels

<!-- b000322 | furniture | pages [15] -->
获取更多资讯

<!-- b000323 | furniture | pages [16] -->
Team # 2401298

<!-- b000324 | furniture | pages [16] -->
Page 16 of 25

<!-- b000326 | caption | pages [16] -->
Figure 9: One Building Block of the Bayesian Network

<!-- b000327 | prose | pages [16] -->
Using this simpler network as one building block, we can stack two blocks together to form our Duel-Temporal Bayesian Network:

<!-- b000328 | caption | pages [16] -->
Figure 10: Duel-Temporal Bayesian Network

<!-- b000329 | prose | pages [16] -->
We have added green arrows between hidden variables in these two layers, repre- senting the continuity of mental and physical state.

<!-- b000330 | prose | pages [16] -->
关注数学模型

<!-- b000331 | furniture | pages [16] -->
2

<!-- b000332 | furniture | pages [16] -->
MATHmodels

<!-- b000333 | furniture | pages [16] -->
获取更多资讯

<!-- b000334 | furniture | pages [17] -->
Team # 2401298

<!-- b000335 | furniture | pages [17] -->
Page 17 of 25

<!-- b000336 | heading | pages [17] -->
5.2.3 Data fitting

<!-- b000337 | prose | pages [17] -->
One obstacle for effectively training this model is noise. Although we have taken into account the original strength difference and the serving advantage, we must ad- 微信公众号：数学模型 mit the residual effect of gaining/losing at a certain point is still (and should be still) largely random. Instead of letting the model predict the state in the next point, we let it predict **the sum** of the effect in the next n points. Because of Central Limit The- orem, this reduces the noise and thus making the network’s training possible. In the same manner, all the observed variables such as player’s double fault is aggregated in a certain time interval. Specifically, suppose the current point index is t , the long-term layer’s data is aggregated in [t −40, t −10] and the effect in [t −10, t] , while the short- term layer’s data is aggregated in [t −10, t] and the effect in [t, t + 10] . We carefully separate the past game information and the future game outcome to guarantee our model is completely predictive.

<!-- b000338 | prose | pages [17] -->
The following graph depicts the shifting of denoised residual effect in the match between Carlos Alcaraz and Djokovic from Carlos’ perspective. 微信号：MATHmodels

<!-- b000339 | caption | pages [17] -->
Figure 11: Denoised Residual Effect Cruve

<!-- b000340 | prose | pages [17] -->
Due to the existence of latent variables in our model, we utilize the Expectation- Maximization (EM) algorithm to train the network on the data of 31 matches in Wim- bledon 2023. EM is used in statistics for finding maximum likelihood estimates of parameters in probabilistic models, where the model depends on unobserved latent variables.

<!-- b000341 | prose | pages [17] -->
The EM algorithm consists of two steps: the Expectation step (E step) and the Max- imization step (M step). In the E step, the algorithm calculates the expected values of the latent variables given the current parameters of the model. In the M step, it maximizes the likelihood function to update the parameters based on these expected values. This process is repeated until convergence.

<!-- b000342 | prose | pages [17] -->
Q(θ|θ(t)) = EZ|X,θ(t)[log L(θ; X, Z)] (12)关注数学模型 E step:

<!-- b000343 | furniture | pages [17] -->
2

<!-- b000344 | furniture | pages [17] -->
MATHmodels

<!-- b000345 | furniture | pages [17] -->
获取更多资讯

<!-- b000346 | furniture | pages [18] -->
Team # 2401298

<!-- b000347 | furniture | pages [18] -->
Page 18 of 25

<!-- b000348 | prose | pages [18] -->
θ(t+1) = arg max Q(θ|θ(t)) M step: (13) θ

<!-- b000349 | prose | pages [18] -->
In these equations, θ represents the parameters of the model, X represents the ob- 微信公众号：数学模型 served data which consists both the output - residual effect and the input - point-to- point data, Z represents the latent variables(6 latent variables in our model), L is the likelihood function, and Q is a function that depends on the expected values of the latent variables.

<!-- b000350 | prose | pages [18] -->
During our first training, we spotted an unexpected bias in this dataset: the player 1 has overall better residual effect than the player 2. Consequently, the prior distribution (i.e. when NO evidence provided) of "player 1 has better residual effect" vs "player 2 has better residual effect" predicted by our model is about 53% vs 47%. We could mirror the dataset (i.e. switch the position of player 1 and player 2) but will also double training cost. To solve this in a more general manner, we reweight the expression of Q(θ|θ(t)) as

<!-- b000351 | prose | pages [18] -->
微信号：MATHmodels 1 Q(θ|θ(t)) = EZ|X,θ(t)[ P(X) log L(θ; X, Z)] Reweighted E step: (14)

<!-- b000352 | prose | pages [18] -->
Where P(X) is the prior of X occurring when considering some of its features - in our case, the residual effect advantage.

<!-- b000353 | prose | pages [18] -->
For effectively training the network, we need first discretize the variables. The terms residual_effect_1(0) and residual_effect_1(1) refer to the momentum attributed to the opponent and oneself, respectively. Similarly, unf_err_1 ranges from 0 to 2, in- dicating the relative unforced error levels between players; ’0’ implies more unforced errors in the opponent, ’1’ denotes equal levels, and ’2’ suggests more unforced errors in oneself. As for latent variables, like self_efficacy_1 values range from 0 to 1, indi- cating the relative self-efficacy levels between players; ’0’ implies higher self-efficacy in the opponent, and ’1’ suggests higher self-efficacy in oneself.

<!-- b000354 | prose | pages [18] -->
To measure the importance of variables, we compute the information gain (or equiv- alently, "entropy reduction") when given each variable. The entropy values provide a measure of uncertainty or unpredictability associated with the predictions of different variables’ effects on momentum. A greater information gain indicates greater impor- tance.

<!-- b000355 | prose | pages [18] -->
(a) (b)

<!-- b000356 | caption | pages [18] -->
Figure 12: Differences in Residual Effects and Entropy

<!-- b000357 | prose | pages [18, 19] -->
关注数学模型 As can be seen from the graph, the most substantial positive influence on momen- tum is from player’s net point won, closely followed by aces and maintaining a scoring lead. These results suggest that proactive and aggressive playstyles significantly con- tribute to a player’s momentum. In stark contrast, unforced errors are shown to under- 微信公众号：数学模型 mine momentum, emphasizing the importance of consistency and error management in maintaining psychological advantage on the court. Double faults unexpectedly ap- pear to increase momentum slightly. We suspect this is due to the correlation between double fault and aggressive serving. Since the player’s aggressiveness isn’t identified as variable in our model, the true causal effect is thus hard to learn.

<!-- b000358 | furniture | pages [18] -->
2

<!-- b000359 | furniture | pages [18] -->
MATHmodels

<!-- b000360 | furniture | pages [18] -->
获取更多资讯

<!-- b000361 | furniture | pages [19] -->
Team # 2401298

<!-- b000362 | furniture | pages [19] -->
Page 19 of 25

<!-- b000364 | prose | pages [19] -->
To further clarify the counterintuitive increase in momentum following double faults, our investigation delved into the patterns of serving. Baseline ace rates for servers pace 1 and pace stood at 9.70% and 8.61%, respectively. Intriguingly, analysis post-double fault 2 revealed an uptick in ace frequency, with player 1’s ace rate pace next double fault ascending 1 to 10.61% and pace next double fault to 9.59% within the ensuing ten serves. This suggests a 2 correlation shortcut or data bias learned by the model.

<!-- b000365 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000366 | heading | pages [19] -->
5.2.4 Inference on Match Data

<!-- b000367 | prose | pages [19] -->
During inference, all observed variables, including long term residual effect are feeding into the model. Based on these known evidence, our Bayesian network can determine the distribution of the output and latent variables, and ultimately, the mo- mentum (as residual effect) in a match. Specifically, given the structure of the network, we can describe the mathematical relationship between these variables’ distribution using the conditional dependencies depicted in the network. For computational de- [11]. tail, refer to [(Ben, 2007)]

<!-- b000368 | heading | pages [19] -->
5.2.5 Advisement

<!-- b000369 | prose | pages [19] -->
Based on the statistical analysis from our Bayesian network, we propose the follow- ing strategies for players to potentially improve their momentum:

<!-- b000370 | heading | pages [19] -->
1. Minimize Unforced Errors: Prioritize consistency in rallies to avoid giving away

<!-- b000371 | prose | pages [19] -->
momentum through avoidable mistakes.

<!-- b000372 | heading | pages [19] -->
2. Leverage Aggressive Plays: Integrate more net approaches and aim for aces to

<!-- b000373 | prose | pages [19] -->
capitalize on these actions’ strong positive impact on momentum.

<!-- b000374 | heading | pages [19] -->
3. Strategic Serving: Focus on serve accuracy and variety, reducing double faults

<!-- b000375 | prose | pages [19] -->
even though they may not significantly dampen momentum, as maintaining serve is still critical for match success.

<!-- b000376 | heading | pages [19] -->
4. Mental Resilience: Develop psychological resilience to withstand the pressure

<!-- b000377 | prose | pages [19] -->
of facing break points, as overcoming them contributes less to momentum than antici- pated.

<!-- b000378 | heading | pages [19] -->
5. Maintain Lead: Strive to build and maintain a lead, as staying ahead fosters

<!-- b000379 | prose | pages [19] -->
positive momentum and can exert psychological pressure on the opponent.

<!-- b000380 | prose | pages [19] -->
Incorporating these strategies into training and match-play can help players har- ness and maintain momentum, which is a pivotal aspect of competitive tennis.

<!-- b000381 | prose | pages [19] -->
关注数学模型

<!-- b000382 | furniture | pages [19] -->
2

<!-- b000383 | furniture | pages [19] -->
MATHmodels

<!-- b000384 | furniture | pages [19] -->
获取更多资讯

<!-- b000385 | furniture | pages [20] -->
Team # 2401298

<!-- b000386 | furniture | pages [20] -->
Page 20 of 25

<!-- b000387 | heading | pages [20] -->
6 Problem 4 : Swings Prediction and Model Generaliza-

<!-- b000388 | prose | pages [20] -->
tion

<!-- b000389 | prose | pages [20] -->
微信公众号：数学模型 We first evaluated our model on the final match between Carlos Alcaraz and No- vak Djokovic. The outcomes, together with those from three additional matches, are presented in the subsequent graph. It’s notable that our model accurately forecasted the first few up and downs of the residual effect, but failed at the 230th 280th points which corresponds to the fourth set. During this phase, Novak Djokovic unexpectedly gained a significant advantage. This is probably due to the effect of factors that our model does not account for.

<!-- b000390 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000391 | caption | pages [20] -->
Figure 13: Predicted vs Actual

<!-- b000392 | prose | pages [20] -->
A possible factor that significantly influences outcomes in tennis is the personal play style of specific players, like surface preferences, injury history. These can only be modeled through their historical performances and can’t be inferred through our current approach (i.e. only consider players’ rankings). A data-based integration of player’s personal information may further boost our model’s performance.

<!-- b000393 | prose | pages [20] -->
Besides, the given Wimbledon dataset, we also test our model on a dataset of women’s singles tennis matches from JeffSackmann’s tennis_MatchChartingProject, [10]. which is called charting −w −points −2020s.csv

<!-- b000394 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型 (a) (b)

<!-- b000395 | furniture | pages [20] -->
2

<!-- b000396 | furniture | pages [20] -->
MATHmodels

<!-- b000397 | furniture | pages [20] -->
获取更多资讯

<!-- b000398 | furniture | pages [21] -->
Team # 2401298

<!-- b000399 | furniture | pages [21] -->
Page 21 of 25

<!-- b000401 | caption | pages [21] -->
Figure 14: Differences in Residual Effects and Entropy

<!-- b000402 | prose | pages [21] -->
Compared with Figure 12 , one notable distinction is the impact of aces. In our dataset, male players have a 9.14% likelihood of achieving an ace, whereas female 微信号：MATHmodels players only 4.25%. Additionally, the occurrence of double faults now clearly has a detrimental effect, as it is no longer the result of aggressive attempts to achieve an ace.

<!-- b000403 | prose | pages [21] -->
To demonstrate the adaptability of our model framework, we further generalize it into a more abstract and comprehensive form, as depicted in the following graph. This framework can be instantiated into models that are capable of dealing all kinds of sports games such as table tennis, basketball, soccer...

<!-- b000404 | caption | pages [21] -->
Figure 15: General Framework

<!-- b000405 | prose | pages [21] -->
关注数学模型

<!-- b000406 | furniture | pages [21] -->
2

<!-- b000407 | furniture | pages [21] -->
MATHmodels

<!-- b000408 | furniture | pages [21] -->
获取更多资讯

<!-- b000409 | furniture | pages [22] -->
Team # 2401298

<!-- b000410 | furniture | pages [22] -->
Page 22 of 25

<!-- b000411 | heading | pages [22] -->
7 Model Analysis

<!-- b000412 | heading | pages [22] -->
7.1 Strengths and Weaknesses

<!-- b000413 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000414 | heading | pages [22] -->
Strengths:

<!-- b000415 | prose | pages [22] -->
1. Captures both short-term and long-term momentum effects through the two- layer structure. This allows the model to account for momentum shifts arising from recent in-game events as well as longer-term psychological factors.

<!-- b000416 | prose | pages [22] -->
2. Incorporates latent variables like physiology, perception of control, and self- efficacy that are not directly observable but play an important role in momentum. This provides a more comprehensive representation of the factors influencing momentum.

<!-- b000417 | prose | pages [22] -->
3. Uses advanced machine learning techniques like expectation maximization to handle the latent variables and make the model trainable on real match data. This enables practical application of the model.

<!-- b000418 | prose | pages [22] -->
微信号：MATHmodels 4. Achieves good generalization across different players and matches in the dataset, demonstrating robustness.

<!-- b000419 | prose | pages [22] -->
5. Provides interpretable insights into how different factors like unforced errors, aggressive plays, break points etc. influence momentum.

<!-- b000420 | prose | pages [22] -->
Weaknessess:

<!-- b000421 | prose | pages [22] -->
1. Difficult to fully validate accuracy of latent variable representations and their dynamics without access to actual measurements of players’ psychological states.

<!-- b000422 | prose | pages [22] -->
2. Requires aggregation of data over intervals to reduce noise for training, losing some granularity.

<!-- b000423 | prose | pages [22] -->
3. Does not account for opponent adaptive strategies and their influence on mo- mentum. Assumes independent player behaviors.

<!-- b000424 | heading | pages [22] -->
7.2 Sensitivity Analysis

<!-- b000425 | prose | pages [22] -->
To evaluate the robustness of our proposed model, we conduct a sensitivity analysis on two aspects. 1. Modifying the model’s prediction interval. 2. Changing the training data by randomly sampling 70% and 50% from the original dataset, corresponding to 22 and 16 matches, respectively.

<!-- b000426 | prose | pages [22] -->
The following is the altered information gain from observed variables. The changes in the left graph indicates that a longer prediction interval forces the model to prioritize effects with potentially longer durations, such as "score advantage". On the contrary, short-term events like "net point won", "ace" gain less weight. In the right graph, the model trained on 50% appears notable changes, likely due to the altered distribution of matches. On the other hand, the model trained with 70% of the data remained stable, indicating a threshold of data sufficiency.

<!-- b000427 | prose | pages [22, 23] -->
关注数学模型 微信公众号：数学模型 (a) (b)

<!-- b000428 | furniture | pages [22] -->
2

<!-- b000429 | furniture | pages [22] -->
MATHmodels

<!-- b000430 | furniture | pages [22] -->
获取更多资讯

<!-- b000431 | furniture | pages [23] -->
Team # 2401298

<!-- b000432 | furniture | pages [23] -->
Page 23 of 25

<!-- b000434 | caption | pages [23] -->
Figure 16: Differences in Residual Effects and Entropy

<!-- b000435 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000436 | heading | pages [23] -->
7.3 Conclusion

<!-- b000437 | prose | pages [23] -->
In this paper, we establish our momentum predictor through a two-step process. Initially, we develop a naive binomial model aimed at recovering the "ideal" state of the game. Subsequently, the residual of its prediction is utilized as the label for our momentum predictor, the dual-temporal Bayesian network. This model framework, demonstrated to be highly generalizable and robust, allows us to uncover the latent systems underlying observable sports games.

<!-- b000438 | heading | pages [23] -->
8 Memorandum

<!-- b000439 | prose | pages [23] -->
To: Tennis Coaches

<!-- b000440 | prose | pages [23] -->
From: Team #2401298

<!-- b000441 | prose | pages [23] -->
Subject: Leveraging Momentum in Tennis - Insights and Strategies for Coaching

<!-- b000442 | prose | pages [23] -->
Date: February 6, 2024

<!-- b000443 | prose | pages [23] -->
Dear Coaches,

<!-- b000444 | prose | pages [23] -->
We are thrilled to share with you our suggestions derived from our Duel-Temporal Bayesian network model, to enhance player performance through the nuanced con- cept of "momentum" in tennis. In the dynamic world of competitive tennis, the concept of "momentum" is often cited as a game-changer, potentially turning the tide in pivotal match moments. This elusive force is thought to shape match outcomes. Our research has dissected this phenomenon, aiming to transform the abstract phenomenon into tangible strategies that can be methodically applied.

<!-- b000445 | prose | pages [23, 24] -->
关注数学模型 微信公众号：数学模型

<!-- b000446 | furniture | pages [23] -->
2

<!-- b000447 | furniture | pages [23] -->
MATHmodels

<!-- b000448 | furniture | pages [23] -->
获取更多资讯

<!-- b000449 | furniture | pages [24] -->
Team # 2401298

<!-- b000450 | furniture | pages [24] -->
Page 24 of 25

<!-- b000452 | caption | pages [24] -->
Figure 17: Momentum in Tennis

<!-- b000453 | prose | pages [24] -->
"Momentum" is not an isolated concept, it represents the existence of complex la- tent states of tennis matches, beyond what can be captured by simply counting points. Our study analyzed the intricate dynamics of momentum in tennis matches. We have utilized statistical models and a Duel-Temporal Bayesian Network to quantify and pre- 微信号：MATHmodels dict the influence of psychological and physiological factors on in-game performance. Our analysis suggests that while each point’s outcome may appears statistically inde- pendent to some extent, the Bayesian network we developed tells a richer story. It reveals the hidden threads of self-efficacy, strategy, and physiological responses that weave together to form the fabric of momentum.

<!-- b000454 | prose | pages [24] -->
To enable players to harness the positive aspects of momentum while mitigating its pressures, we recommend following strategic pivots:

<!-- b000455 | prose | pages [24] -->
1. Consistency is Key: Encourage players to minimize unforced errors; our findings link consistent play to maintaining momentum.

<!-- b000456 | heading | pages [24] -->
2. Aggressiveness Pays Off: Advise players to assert dominance with net approaches

<!-- b000457 | prose | pages [24] -->
and serves to build positive momentum.

<!-- b000458 | heading | pages [24] -->
3. Serve Smart: Emphasize varied and accurate serving techniques to uphold

<!-- b000459 | prose | pages [24] -->
momentum without risking double faults.

<!-- b000460 | heading | pages [24] -->
4. Build Resilience: Cultivate players’ mental fortitude, essential for navigating the

<!-- b000461 | prose | pages [24] -->
pressures of break points and shifting tides within matches.

<!-- b000462 | heading | pages [24] -->
5. Lead to Succeed: Strive for early leads; our model suggests this exerts

<!-- b000463 | prose | pages [24] -->
psychological pressure on opponents, bolstering momentum for the leading player.

<!-- b000464 | prose | pages [24] -->
We trust this memo provides a clear and actionable strategy for leveraging the con- cept of momentum to your advantage. Implementing these recommendations could foster a competitive edge, vital for triumphing in the modern, fast-paced game of ten- nis.

<!-- b000465 | prose | pages [24] -->
Looking forward to seeing these strategies manifest in your players’ enhanced per- formance.

<!-- b000466 | prose | pages [24] -->
Yours Sincerely,

<!-- b000467 | furniture | pages [24] -->
Team #2401298

<!-- b000468 | prose | pages [24] -->
关注数学模型

<!-- b000469 | furniture | pages [24] -->
2

<!-- b000470 | furniture | pages [24] -->
MATHmodels

<!-- b000471 | furniture | pages [24] -->
获取更多资讯

<!-- b000472 | furniture | pages [25] -->
Team # 2401298

<!-- b000473 | furniture | pages [25] -->
Page 25 of 25

<!-- b000474 | heading | pages [25] -->
References

<!-- b000475 | references | pages [25] -->
[1] Taylor, J., & Demick, A. (1994). A multidimensional model of momentum in

<!-- b000476 | references | pages [25] -->
微信公众号：数学模型

<!-- b000477 | references | pages [25] -->
sports. _Journal of Applied Sport Psychology_, _6_(1), 51-70.

<!-- b000478 | references | pages [25] -->
[2] Klaassen, F. J., & Magnus, J. R. (2001). Are points in tennis independent and iden-

<!-- b000479 | references | pages [25] -->
tically distributed? Evidence from a dynamic binary panel data model. _Journal

<!-- b000480 | references | pages [25] -->
of the American Statistical Association_, _96_(454), 500-509.

<!-- b000481 | references | pages [25] -->
[3] Motoi, S., Misu, T., Nakada, Y., Yazaki, T., Kobayashi, G., Matsumoto, T., &

<!-- b000482 | references | pages [25] -->
Yagi, N. (2012). Bayesian event detection for sport games with hidden Markov

<!-- b000483 | references | pages [25] -->
model. _Pattern Analysis and Applications_, _15_, 59-72.

<!-- b000484 | references | pages [25] -->
[4] Sun, Y. (2004). Detecting the hot hand: An alternative model. In _Proceedings of

<!-- b000485 | references | pages [25] -->
the Annual Meeting of the Cognitive Science Society_ (Vol. 26, No. 26).

<!-- b000486 | references | pages [25] -->
[5] Klaassen, F. J., & Magnus, J. R. (2003). Forecasting the winner of a tennis

<!-- b000487 | references | pages [25] -->
微信号：MATHmodels

<!-- b000488 | references | pages [25] -->
match. _European Journal of Operational Research_, _148_(2), 257-267.

<!-- b000489 | references | pages [25] -->
[6] Ge, X., & Lin, A. (2021). Dynamic causality analysis using overlapped sliding

<!-- b000490 | references | pages [25] -->
windows based on the extended convergent cross-mapping. _Nonlinear Dynam-

<!-- b000491 | references | pages [25] -->
ics_, _104_, 1753-1765.

<!-- b000492 | references | pages [25] -->
[7] Morber, J. R. (2008). _One-dimensional nanowires: Understanding growth and

<!-- b000493 | references | pages [25] -->
properties as steps toward biomedical and electrical application_. Georgia Insti-

<!-- b000494 | references | pages [25] -->
tute of Technology.

<!-- b000495 | references | pages [25] -->
[8] Madhavan, V. (2016). Predicting NBA game outcomes with hidden Markov mod-

<!-- b000496 | references | pages [25] -->
els. _Berkeley University_.

<!-- b000497 | references | pages [25] -->
[9] Raab, M., Gula, B., & Gigerenzer, G. (2012). The hot hand exists in volleyball

<!-- b000498 | references | pages [25] -->
and is used for allocation decisions. _Journal of Experimental Psychology: Ap-

<!-- b000499 | references | pages [25] -->
plied_, _18_(1), 81.

<!-- b000500 | references | pages [25] -->
[10] https://github.com/JeffSackmann/tennis_MatchChartingProject.

<!-- b000501 | references | pages [25] -->
[11] Ben Gal I (2007). "Bayesian Networks" (PDF). In Ruggeri F, Kennett RS, Faltin

<!-- b000502 | references | pages [25] -->
FW (eds.). Support-Page. Encyclopedia of Statistics in Quality and Reliabil-

<!-- b000503 | references | pages [25] -->
ity. John Wiley & Sons. doi:10.1002/9780470061572.eqr089. ISBN 978-0-470-01861-

<!-- b000504 | references | pages [25] -->
3. Archived from the original (PDF) on 2016-11-23. Retrieved 2007-08-27.

<!-- b000505 | references | pages [25] -->
关注数学模型

<!-- b000506 | furniture | pages [25] -->
2

<!-- b000507 | furniture | pages [25] -->
MATHmodels

<!-- b000508 | furniture | pages [25] -->
获取更多资讯
