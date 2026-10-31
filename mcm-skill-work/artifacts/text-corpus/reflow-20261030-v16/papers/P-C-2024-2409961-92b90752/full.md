# P-C-2024-2409961-92b90752

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
2409961

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
微信公众号：数学模型

<!-- b000009 | title | pages [1] -->
Momentum Prediction and Core Feature Extraction

<!-- b000010 | title | pages [1] -->
Based on GRU with Integrated Gradients

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
Currently, coaches, players, and managers are all aware that "momentum" plays a huge role in the progress of tennis matches. By analyzing the changes in momentum during the game, we can evaluate the performance of players during specific time periods and make speculations about the game results. By understanding the factors that influence the momentum of the game, we can assess the fluctuations in the game process and construct a player training system. Therefore, it is

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
crucial to recognize the role of "momentum" in the game and use it to help players cope with events that affect the progress of the game.

<!-- b000015 | prose | pages [1] -->
Firstly, we established an Instantaneous Score Rate (ISR) model to capture match points. After using the cubic spline interpolation method to process discrete data, the model can smoothly estimate the Instantaneous score rate at any time and accurately capture key moments in the competition. Based on the results of this model, we can quickly identify the performance of players at specific time points. In addition, the results of the model clearly demonstrate the first mover advantage of the serving party in the game, which is consistent with the facts. Then, we establish a model to test the role of momentum in the competition. The results indicate that there is not independent between fluctuations in the game and the success of players. In addition to the first mover advantage, there will be a strong "momentum" in the game that affects the Instantaneous Score Rate.

<!-- b000016 | prose | pages [1] -->
Next, in order to predict fluctuations in the competition, we use Gated Recurrent Neural Network Model (GRU) with Integrated Gradients for feature disentanglement engineering. Based on the GRU model, we can fit the "momentum" function under existing conditions to accurately predict the change in competition momentum. We manually divided the original indicators into six dimensions. Using the Integrated Gradient algorithm, the impact of six dimensions on the output is indicated from the GRU model output. Based on the model results, we have identified 12 important indicators that have an significant impact on schedule fluctuations. On this basis, we established a competency evaluation system based on six dimensions, and provided targeted suggestions to players based on the analysis of real player abilities.

<!-- b000017 | prose | pages [1] -->
In addition, we tested the predictive ability of the model in real-time data of different genders, game systems, and ball games. The test results have shown that our model can accurately predict other competition processes and has high generalization ability.

<!-- b000018 | prose | pages [1] -->
Finally, in order to help coaches cultivate players to better cope with events that affect the tennis schedule, we provide targeted recommendations. We hope these suggestions can help players achieve victory in the new game.

<!-- b000019 | keywords | pages [1] -->
Keywords: Momentum, GRU, Integrated Gradient, Disentanglement.

<!-- b000020 | furniture | pages [1] -->
关注数学模型

<!-- b000021 | furniture | pages [1] -->
2

<!-- b000022 | furniture | pages [1] -->
MATHmodels

<!-- b000023 | furniture | pages [1] -->
获取更多资讯

<!-- b000024 | furniture | pages [2] -->
Team # 2409961

<!-- b000025 | furniture | pages [2] -->
Page 1 of 24

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000028 | contents | pages [2] -->
1 Introduction

<!-- b000029 | contents | pages [2] -->
2

<!-- b000030 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
3 Model Preparation

<!-- b000033 | contents | pages [2] -->
4

<!-- b000034 | contents | pages [2] -->
3.1

<!-- b000035 | contents | pages [2] -->
Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
4

<!-- b000037 | contents | pages [2] -->
3.2

<!-- b000038 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
4 Instantaneous Scoring Rate Model

<!-- b000041 | contents | pages [2] -->
5

<!-- b000042 | contents | pages [2] -->
4.1

<!-- b000043 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000044 | contents | pages [2] -->
Cubic spline interpolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
5

<!-- b000046 | contents | pages [2] -->
4.2

<!-- b000047 | contents | pages [2] -->
Instantaneous Scoring Rate for the match

<!-- b000048 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
7

<!-- b000050 | contents | pages [2] -->
5 Test of Independence Between Momentum and Victory

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
5.1

<!-- b000053 | contents | pages [2] -->
Assumption: Momentum and victory are independent . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
8

<!-- b000055 | contents | pages [2] -->
5.2

<!-- b000056 | contents | pages [2] -->
Verification: Momentum has an impact on victory . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
9

<!-- b000058 | contents | pages [2] -->
6 Disentangled feature Engineering via GRU with integrated gradients

<!-- b000059 | contents | pages [2] -->
9

<!-- b000060 | contents | pages [2] -->
6.1

<!-- b000061 | contents | pages [2] -->
Important Data Extraction

<!-- b000062 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
9

<!-- b000064 | contents | pages [2] -->
6.2

<!-- b000065 | contents | pages [2] -->
Match Suggestion Based on Capability Evaluation . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
15

<!-- b000067 | contents | pages [2] -->
7 Generalization Testing

<!-- b000068 | contents | pages [2] -->
16

<!-- b000069 | contents | pages [2] -->
7.1

<!-- b000070 | contents | pages [2] -->
Basic Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
16

<!-- b000072 | contents | pages [2] -->
7.2

<!-- b000073 | contents | pages [2] -->
Error Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
16

<!-- b000075 | contents | pages [2] -->
7.3

<!-- b000076 | contents | pages [2] -->
Generalization Ability Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
17

<!-- b000078 | contents | pages [2] -->
8 Conclusion

<!-- b000079 | contents | pages [2] -->
19

<!-- b000080 | contents | pages [2] -->
9 Strengths and Possible Improvements

<!-- b000081 | contents | pages [2] -->
19

<!-- b000082 | contents | pages [2] -->
9.1

<!-- b000083 | contents | pages [2] -->
Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
19

<!-- b000085 | contents | pages [2] -->
9.2

<!-- b000086 | contents | pages [2] -->
Possible Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
19

<!-- b000088 | contents | pages [2] -->
Appendices

<!-- b000089 | contents | pages [2] -->
23

<!-- b000090 | furniture | pages [2] -->
关注数学模型

<!-- b000091 | furniture | pages [2] -->
2

<!-- b000092 | furniture | pages [2] -->
MATHmodels

<!-- b000093 | furniture | pages [2] -->
获取更多资讯

<!-- b000094 | furniture | pages [3] -->
Team # 2409961

<!-- b000095 | furniture | pages [3] -->
Page 2 of 24

<!-- b000096 | heading | pages [3] -->
1 Introduction

<!-- b000097 | heading | pages [3] -->
Background

<!-- b000098 | prose | pages [3] -->
微信公众号：数学模型 In the men’s final of the 2023 Wimbledon Open, Novak Djokovic took on rising Spanish star Carlos Alcaraz. Djokovic seemed destined for an easy win, winning the first set by an absolute margin of 5 points; while the second set was tense, with Alcaraz winning 7-6 in a tie-break; and the third set was the opposite of the first, with Alcaraz defeating Djokovic by an absolute margin of 5 points... After a number of changes in the trend of the tournament, Grand Slam Djokovic, one of the greatest players in history, lost at Wimbledon for the first time since 2013. [1]

<!-- b000099 | prose | pages [3] -->
In tennis, "momentum" means the power that a player acquires in a match through movement or a series of events. When momentum can be used to measure a player’s performance at a particular point in a match, the players themselves, coaches, and managers have an advantage in determining how the situation on the court is changing, for example, which player is likely to be the winner of the next point [2]. As a result, coaches would like to better understand if momentum can be used 微信号：MATHmodels to determine player performance and the extent to which it can be used at a given point in time. If possible, coaches would like to gain a better understanding of the factors that influence fluctuations in Momentum, so that they can better judge the future course of the game and use it as a reference in training to develop more successful players.

<!-- b000100 | prose | pages [3] -->
Academics have paid attention to the issue of "momentum" in sports events. Some scholars have looked at the psychology of athletes [3], the point of serve [4], Strategic momentum [5] and other aspects of momentum in mental tennis. Existing empirical research suggests that in tennis, players can control the match to benefit themselves from momentum, and that the amount of countermovement will result in a player having a significantly lower chance of winning the underdog set than his opponent [6] . Generalized linear mixed-effects models have also been constructed to demonstrate the legacy effects of score, game, and set [7] . Therefore, by analyzing a large amount of game flow data, we can explore the relationship between momentum and its scoring rate and winning rate based on determining the performance of players in different time periods, and visualize the game flow from the perspective of momentum, with a view to providing references for coaches, players, the public and the media.

<!-- b000101 | prose | pages [3] -->
Some scholars have pointed out that the factors that cause changes in momentum are multiple, including errors and psychological changes during the game [8] . Some empirical scholars have also focused on the indicator of break points in the data as an important variable in the study of momentum shifts in matches. [5] On this basis, by examining the mechanisms by which different factors influence "momentum", we can analyze which factors have the greatest impact on match volatility and suggest that coaches, players, the public, and the media pay attention to these indicators.

<!-- b000102 | prose | pages [3] -->
A preliminary finding of some studies is that, from a psychological point of view, there is little difference in the ability of male and female tennis players to overcome the influence of momentum in order to win the match. [9] In examining the influence of momentum, gender, venue, and type of match may affect the results of the analysis, which leads us to test the generalizability of the model to changing contexts.

<!-- b000103 | furniture | pages [3] -->
关注数学模型

<!-- b000104 | furniture | pages [3] -->
2

<!-- b000105 | furniture | pages [3] -->
MATHmodels

<!-- b000106 | furniture | pages [3] -->
获取更多资讯

<!-- b000107 | furniture | pages [4] -->
Team # 2409961

<!-- b000108 | furniture | pages [4] -->
Page 3 of 24

<!-- b000109 | heading | pages [4] -->
Problem Restatement

<!-- b000110 | prose | pages [4] -->
• Build model 1 to capture match points in the flow of the game and identify the players who performed better and to what extent at a given point in the game. 微信公众号：数学模型 - Test Provide a visualization of the flow of the game based on Model 1.

<!-- b000111 | prose | pages [4] -->
- Judging whether the fluctuation of momentum in the match is independent of the subsequent scoring situation.

<!-- b000112 | prose | pages [4] -->
• Build Model 2 to predict fluctuations in game "momentum" and identify better metrics to help determine game situations.

<!-- b000113 | prose | pages [4] -->
- Test the accuracy and generalizability in predicting the degree of fluctuation in a match.

<!-- b000114 | prose | pages [4] -->
- Gives tactical strategies for winning tennis matches against different opponents based on fluctuations in momentum.

<!-- b000115 | prose | pages [4] -->
• A memo written by summarizes the results and advises coaches on the following directions:

<!-- b000116 | prose | pages [4] -->
- Influencing the direction of play through the "momentum" of the game.

<!-- b000117 | prose | pages [4] -->
- Preparing players for events that affect the tennis schedule.

<!-- b000118 | prose | pages [4] -->
微信号：MATHmodels Our Work

<!-- b000119 | prose | pages [4] -->
We examined the extent to which "momentum" reflects player performance in tennis, and based on its impact indicators, we provide tennis coaches with suggestions for focusing on the role of "momentum" and developing good players based on this concept, as described below:

<!-- b000120 | prose | pages [4] -->
• Build Model 1 to visualize the game schedule.

<!-- b000121 | prose | pages [4] -->
• Based on Model 1, evaluate the coach’s stochastic assumption that fluctuations in momentum during a match are independent of a player’s subsequent score.

<!-- b000122 | prose | pages [4] -->
• Builds Model 2, which predicts game fluctuations and identifies the relevant indicators that have the most significant impact on the direction of the game.

<!-- b000123 | prose | pages [4] -->
• Based on Model 2, provide advice to players in a new round of the tournament on how to play against different opponents.

<!-- b000124 | prose | pages [4] -->
• Test the above model, examine its generalizability, and point out the influencing factors that are lacking in consideration.

<!-- b000125 | prose | pages [4] -->
• Summarizes the results of the study and makes recommendations to coaches

<!-- b000126 | heading | pages [4] -->
STEP 4 Testing Model Generalizability and Making

<!-- b000127 | heading | pages [4] -->
STEP 1：Establishing the Instantaneous Scoring Rate Model (ISR)

<!-- b000128 | prose | pages [4] -->
Suggestions to the Coach Identifying Players Using Cubic Spline Who Perform Well at Searching for Conducting Making Interpolation a Specific Moment. Data on Different Generalization Processing Smoothly Estimating Suggestions for the Genders, Other Studies on the Discrete Data the Scoring Rate Coach Ball Games Model Proving the Existence of a First-Mover Advantage

<!-- b000129 | prose | pages [4] -->
STEP 3 ：Predicting match fluctuations and identifying the most significant correlated indicators

<!-- b000130 | heading | pages [4] -->
STEP 2：Establish Flow-Independent Models

<!-- b000131 | prose | pages [4] -->
affecting the course of the game. and Non-Independent Models Backpropagation using Integrated Gradients algorithm Flow Potential Analyzing the Magnitude of Selecting 12 FAIL Independent GRU model Dimensional Influence Key Indicators Models Evaluate the Coach’s Mentality Offensive Independence Test Establishing a Stochastic Competency

<!-- b000132 | heading | pages [4] -->
Assumption

<!-- b000133 | prose | pages [4] -->
Data Evaluation System Endurance Skill Non- Dimensionality Independent Reduction CORRECT Models Error Rate Key Point

<!-- b000134 | caption | pages [4] -->
Figure 1: Our Work Frame

<!-- b000135 | furniture | pages [4] -->
关注数学模型

<!-- b000136 | furniture | pages [4] -->
2

<!-- b000137 | furniture | pages [4] -->
MATHmodels

<!-- b000138 | furniture | pages [4] -->
获取更多资讯

<!-- b000139 | furniture | pages [5] -->
Team # 2409961

<!-- b000140 | furniture | pages [5] -->
Page 4 of 24

<!-- b000141 | heading | pages [5] -->
2 Assumptions and Notations

<!-- b000142 | heading | pages [5] -->
Assumptions

<!-- b000143 | prose | pages [5] -->
微信公众号：数学模型 Asm. 1 Not considering the decline in performance of players due to injury or physical factors

<!-- b000144 | prose | pages [5] -->
Asm. 2 There is no negative game phenomenon such as players maliciously controlling points

<!-- b000145 | prose | pages [5] -->
Asm. 3 The competition is formal, and the vast majority of off field factors have been screened out. The only off field factor that can affect the game situation is the current score of the match

<!-- b000146 | prose | pages [5] -->
Asm. 4 Assuming previous research data is accurate.

<!-- b000147 | heading | pages [5] -->
Notations

<!-- b000148 | prose | pages [5] -->
In this work, we use the notations in Table 1 in the model construction. Other symbols will 微信号：MATHmodels be introduced once they are used.

<!-- b000149 | caption | pages [5] -->
Table 1: Notations used in this literature

<!-- b000150 | prose | pages [5] -->
symbol Description

<!-- b000151 | prose | pages [5] -->
i Point number in match ti The point begins with a serve 1 minute and thirty-one seconds after the start of the first point of the match. yi Player 2’s relative point for the Game relative to Player 1 f Relative Score Curve(f(ti) = yi) ISRi Instantaneous score rate at the ith point of match m Momentum Curve

<!-- b000152 | heading | pages [5] -->
3 Model Preparation

<!-- b000153 | prose | pages [5] -->
Our data primarily comes from the problems provided, with a minority of the data manually extracted from the official tennis website.

<!-- b000154 | heading | pages [5] -->
3.1 Data Collection

<!-- b000155 | prose | pages [5] -->
The dataset, maintained by Jeff Sackmann and available publicly on GitHub1, encompasses detailed point-by-point data from Grand Slam tennis matches. It provides exhaustive details for each point scored, including serve details, scoring, and errors. Additionally, we manually collected the final match of table tennis from the 2020 Olympics2 as our supplementary dataset. We also collected matches from Github3 as auxiliary information, obtaining extra details about the matches such as the type of surface, the type of tournament, etc.

<!-- b000156 | prose | pages [5] -->
1https://github.com/JeffSackmann/tennis slam pointbypoint 2https://olympics.com/zh/olympic-games/tokyo-2020/results/table-tennis 3https://github.com/JeffSackmann/tennis MatchChartingProject

<!-- b000157 | furniture | pages [5] -->
关注数学模型

<!-- b000158 | furniture | pages [5] -->
2

<!-- b000159 | furniture | pages [5] -->
MATHmodels

<!-- b000160 | furniture | pages [5] -->
获取更多资讯

<!-- b000161 | furniture | pages [6] -->
Team # 2409961

<!-- b000162 | furniture | pages [6] -->
Page 5 of 24

<!-- b000163 | heading | pages [6] -->
3.2 Data Cleaning

<!-- b000164 | prose | pages [6] -->
The available data were divided into 32 time-series data according to the belonging matches for subsequent model training. For the missing values (NaN) in the data, we filled them according 微信公众号：数学模型 to the distribution they belonged to: (1) The missing values of serve speed were sampled and filled according to the player’s serving habits in other matches using a normal distribution. (2) Missing values for variables with two values, such as depth of return and serve position, were sampled to fill them based on the frequency of that player’s values for that data in other matches using a Bernoulli distribution. (3) Missing values for variables with multiple different values, such as depth of serve, were sampled and filled in based on a multinomial distribution based on the frequency of the player’s values of this data in other matches. (4) Missing values for distance run were sampled according to the player’s habits and filled in according to a uniform distribution. For the outlier 0 in the tension value of the data, we constructed a new distribution using the frequency of tension values in other games and resampled it according to that distribution.

<!-- b000165 | heading | pages [6] -->
4 Instantaneous Scoring Rate Model

<!-- b000166 | prose | pages [6] -->
微信号：MATHmodels At the end of a tennis match, we can not only get the result of the match, but often also get a lot of information about the tournament process, i.e. whether the player who serves first has an advantage over the player who serves later, which player performs better in the early part of the match, which player performs better in the late part of the match and to what extent they are all better, etc. Due to the discrete characteristics of the data of the whole tournament process, in order to analyze the whole tournament process as well as to predict the tournament trend, we use the cubic spline interpolation method to interpolate the original discrete data{(ti, yi)} into a quadratic differentiable functionf in order to derive the Instantaneous Scoring Ratio at each point.

<!-- b000167 | prose | pages [6] -->
ISRi = ( d dtf)(ti) (1)

<!-- b000168 | heading | pages [6] -->
4.1 Cubic spline interpolation

<!-- b000169 | prose | pages [6] -->
Cubic spline interpolation not only ensures smooth continuity of the curve through each given point, but also ensures continuity of the first- and second-order derivatives of the curve, avoiding the oscillations that are common to higher-order polynomial interpolation - the Longe phenomenon. Its ability to control locally means that adjusting a point will affect only a small part of the curve, not the whole. Based on the above advantages, we utilize cubic spline interpolation for interpolation to quadratic differentiable functions. The cubic spline interpolation formula is shown below:

<!-- b000170 | prose | pages [6] -->
. . . 1 0 0 0 0       m0 y2−y1 −y1−y0 h0 2(h0 + h1) h1    h1 h0  m1 y3−y2 −y2−y1 h1 2(h1 + h2) h2 . . .   0 0 h2 h1 m2 ... y4−y3 −y3−y2 h2 2(h2 + h3) 0 0 = 6 h3 h2 m3 ... ... ... ... ... . . .

<!-- b000171 | prose | pages [6, 7] -->
yn−yn−1 −yn−1−yn−2 hn−2 . . . hn−1 0 mn hn−1 hn−2 . . . 0 0 0 1 (2) We write the interpolated sample points as {(ti, yi)}n i=0 (it may be useful to set t0 < · · · < tn), and define hi = ti+1 −ti(i = 0, . . . , n −1),and select boundary conditions as natural boundary conditions.After the solution of mi(i = 0, . . . , n), the interpolation function between ti and ti+1 can be expressed by the following equation: 微信公众号：数学模型 f(t) = yi+(yi+1 −yi −hi 2 mi−hi 6 (mi+1−mi))x+ mi 2 t2+ mi+1 −mi t3 (ti ≤t < ti+1) (3) hi 6hi

<!-- b000172 | furniture | pages [6] -->
关注数学模型

<!-- b000173 | furniture | pages [6] -->
2

<!-- b000174 | furniture | pages [6] -->
MATHmodels

<!-- b000175 | furniture | pages [6] -->
获取更多资讯

<!-- b000176 | furniture | pages [7] -->
Team # 2409961

<!-- b000177 | furniture | pages [7] -->
Page 6 of 24

<!-- b000179 | prose | pages [7] -->
It can be proved that the segmented function is everywhere quadratically differentiable.

<!-- b000180 | prose | pages [7] -->
Therefore, we are able to obtain an interpolation function based on the difference between the cumulative scores of the two sides of the match as shown in Figure 2, where the vertical coordinates of the points on the graph indicate the total score of player 2 at this time minus the total score of player 1 at this time.

<!-- b000181 | prose | pages [7] -->
Cubic Spline Interpolation of the Given Data 微信号：MATHmodels Original Data 5 Cubic Spline Interpolation

<!-- b000182 | prose | pages [7] -->
0

<!-- b000183 | prose | pages [7] -->
Y −5

<!-- b000184 | prose | pages [7] -->
−10

<!-- b000185 | prose | pages [7] -->
−15 0 2000 4000 6000 8000 10000 12000 14000 Time

<!-- b000186 | caption | pages [7] -->
Figure 2: Relative Score Curve

<!-- b000187 | prose | pages [7] -->
After obtaining the relative scoring curve, we can use the derivative to describe the instantaneous change in scoring, i.e., the current direction of the match. The derivative of the relative scoring curve is shown in the Figure 3, and it can be used to describe the match flow very well:

<!-- b000188 | prose | pages [7] -->
ISR curve 0.75 0.50 0.25 0.00 ISR −0.25 −0.50 ISR Player 2 −0.75 Player 1 −1.00 0 2000 4000 6000 8000 10000 12000 14000 Time

<!-- b000189 | caption | pages [7] -->
Figure 3: Instantaneous Score Rate Curve

<!-- b000190 | furniture | pages [7] -->
关注数学模型

<!-- b000191 | furniture | pages [7] -->
2

<!-- b000192 | furniture | pages [7] -->
MATHmodels

<!-- b000193 | furniture | pages [7] -->
获取更多资讯

<!-- b000194 | furniture | pages [8] -->
Team # 2409961

<!-- b000195 | furniture | pages [8] -->
Page 7 of 24

<!-- b000196 | heading | pages [8] -->
4.2 Instantaneous Scoring Rate for the match

<!-- b000197 | prose | pages [8] -->
Utilizing the differentiability of the cubic spline function, we derive the interpolated contin- uous function and observe the derivative value of each scoring point, thus reflecting the relative 微信公众号：数学模型 instantaneous scoring rate between the two players to capture the critical moments in the game. In addition to this, by analyzing the position of the instantaneous scoring rate relative to 0 at each moment, we can assess the scoring efficiency of each player at this moment, as shown in Fig. 4: when the instantaneous scoring rate is lower than 0, it means that the player’s scoring will be reduced at this point, whereas the position away from 0 responds to the extent to which the player scores or loses points at this point - -The further the distance from 0, the higher or lower the player’s scoring rate then, thus allowing identification of which player is performing better at a given point in time.

<!-- b000198 | prose | pages [8] -->
Based on the above image, we colored the scatterplot according to which player served first at that score, and the coloring results are shown in Figure 4:

<!-- b000199 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000200 | caption | pages [8] -->
Figure 4: Scatter plot of March Flow

<!-- b000201 | prose | pages [8] -->
Based on the above analysis, it is easy to find that the relative scoring rate of player 1 is usually higher when player 1 serves first, and the relative scoring rate of player 2 is higher when player 2 serves first. Meanwhile, by studying the frequency graph of the game, as shown in Fig. 5, we can see that whether it is Player 1 or Player 2, the one who serves first will get a higher winning rate, which is the first-hand advantage in the game.

<!-- b000202 | furniture | pages [8] -->
关注数学模型

<!-- b000203 | furniture | pages [8] -->
2

<!-- b000204 | furniture | pages [8] -->
MATHmodels

<!-- b000205 | furniture | pages [8] -->
获取更多资讯

<!-- b000206 | furniture | pages [9] -->
Team # 2409961

<!-- b000207 | furniture | pages [9] -->
Page 8 of 24

<!-- b000208 | prose | pages [9] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000209 | caption | pages [9] -->
Figure 5: Histogram of ISR Distinguishing the Server

<!-- b000210 | heading | pages [9] -->
5 Test of Independence Between Momentum and Victory

<!-- b000211 | prose | pages [9] -->
In order to investigate the role of "momentum" in the game, we developed a flow and momentum independent model and a non-independent model to test whether there is randomness between fluctuations in the game and players’ success, so as to better respond to coaches’ questions. The study shows that the flow and momentum independent model does not hold, and that flow and momentum are not independent, and that sequential hands and momentum will jointly affect the scoring rate. The specific testing process is as follows:

<!-- b000212 | prose | pages [9] -->
5.1 Assumption: Momentum and victory are independent

<!-- b000213 | prose | pages [9, 10] -->
If the future scoring rate and the potential are independent of each other, a change in the potential will not affect the future scoring rate. In this case, we first eliminate the part of the future scoring rate of the two players about the first-hand advantage, that is, we subtract the instantaneous scoring rate of each moment from its expectation and divide it by the sample variance. The difference should be independent and follow the same bounded distribution, and the same is true for the difference in the expected instantaneous scoring rate of the other player. The distribution of the instantaneous scoring rate of the two players and their expected difference is shown in Figure 6. From the central limit theorem, if the sequence of independent random variables with the same distribution has a bounded expectation and variance, then the sequence of random variables after normalization and will be based on the distribution converges to the standard normal distribution, with single-peak characteristics. However, as can be seen from Figure6, the difference distribution has bimodal peaks and does not obey the normal distribution. Therefore, the prior and the potential are not independent, and the flow-potential independence model does not hold.

<!-- b000214 | furniture | pages [9] -->
关注数学模型

<!-- b000215 | furniture | pages [9] -->
2

<!-- b000216 | furniture | pages [9] -->
MATHmodels

<!-- b000217 | furniture | pages [9] -->
获取更多资讯

<!-- b000218 | furniture | pages [10] -->
Team # 2409961

<!-- b000219 | furniture | pages [10] -->
Page 9 of 24

<!-- b000221 | prose | pages [10] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000222 | caption | pages [10] -->
Figure 6: Histogram of ISR Distinguishing the Server after normalization

<!-- b000223 | prose | pages [10] -->
5.2 Verification: Momentum has an impact on victory

<!-- b000224 | prose | pages [10] -->
Since the independent model did not hold, we further examined the non-independent model, i.e., factors other than the forehand serve affecting the match scoring rate. As can be seen in Figure 6, the instantaneous scoring rate of the two players coincides with the peak of their expected difference wave after the effect of the forehand serve on the scoring rate is removed. This indicates that at a certain period of time, no matter the player is a forehand serve or a backhand serve, there is a stronger advantage at some time, such as right side of the wave peak in Fig. 6 represents that the player who serves the ball with the backhand serve has a stronger advantage at a certain time, so the potential and the successive hands will jointly affect the scoring rate, and the non-independence model is established.

<!-- b000225 | heading | pages [10] -->
6 Disentangled feature Engineering via GRU with integrated

<!-- b000226 | prose | pages [10] -->
gradients

<!-- b000227 | prose | pages [10] -->
In order to further investigate when the flow of the game shifts from favoring one player to favoring another, this study, based on the GRU model and the integrated points algorithm, aims to be able to get the prediction results of the game’s momentum shift in order to get the key factors affecting the game’s momentum shift and thus to make suggestions for the players to get a better performance in the new game.

<!-- b000228 | heading | pages [10] -->
6.1 Important Data Extraction

<!-- b000229 | prose | pages [10, 11] -->
In the previous section we obtained the calculation of the instantaneous scoring rate by interpolation and then derivation, but it can be noticed that the amplitude and frequency of vibration of this scoring rate are extremely large, which is very unfavorable for us to estimate this value effectively. Thus, we chose to use a 10-point moving average in smoothing the instantaneous scoring rate, i.e., each point on this average is equal to the average of the instantaneous scoring rate at the first ten scoring points (including the scoring points at this moment): 微信公众号：数学模型 9 m(ti) = 1 X ISRi−k (i ≥10) (4) 10 k=0

<!-- b000230 | furniture | pages [10] -->
关注数学模型

<!-- b000231 | furniture | pages [10] -->
2

<!-- b000232 | furniture | pages [10] -->
MATHmodels

<!-- b000233 | furniture | pages [10] -->
获取更多资讯

<!-- b000234 | furniture | pages [11] -->
Team # 2409961

<!-- b000235 | furniture | pages [11] -->
Page 10 of 24

<!-- b000237 | prose | pages [11] -->
Momentum curve

<!-- b000238 | prose | pages [11] -->
Momentum 0.2 Player 2 Player 1 0.1 Momentum 0.0 微信号：MATHmodels −0.1

<!-- b000239 | prose | pages [11] -->
−0.2 0 2000 4000 6000 8000 10000 12000 14000 Time

<!-- b000240 | caption | pages [11] -->
Figure 7: Momentum Curve

<!-- b000241 | prose | pages [11] -->
It can be seen that the moving average can effectively reflect the trend of the Instantaneous Scoring Rate, so we choose the moving average as the momentum of the match. Therefore, when the average line crosses the 0 axis, it means that the momentum of the game has changed at this time. We tried to fit the "momentum" function based on the known information through the neural network GRU. First of all, we will introduce the GRU model, GRU is simpler than the structure of an LSTM network, and the effect is also very good, so it is also a current streaming kind of network, which can solve the long dependence problem in the RNN network. There are only two gates in the GRU model: the update gate and the reset gate, respectively. The specific structure is shown in the following schematic:

<!-- b000242 | prose | pages [11] -->
In this schematic, the calculation formula of each element is specified as follows:

<!-- b000243 | prose | pages [11, 12] -->
rt = σ (Wr · [ht−1, xt]) zt = σ (Wz · [ht−1, xt]) ˜ht = tanh (W˜h · [rt ∗ht−1, xt]) (5) ht = (1 −zt) ∗ht−1 + zt ∗˜ht yt = σ (Wo · ht) RNN model in the sequence is too long will occur when the gradient disappears problem, result- ing in the parameters only capturing the local relationship, not learning the long-term association, the ability to remember the words in the front of the sequence being weak, and the GRU model 微信公众号：数学模型

<!-- b000244 | furniture | pages [11] -->
关注数学模型

<!-- b000245 | furniture | pages [11] -->
2

<!-- b000246 | furniture | pages [11] -->
MATHmodels

<!-- b000247 | furniture | pages [11] -->
获取更多资讯

<!-- b000248 | furniture | pages [12] -->
Team # 2409961

<!-- b000249 | furniture | pages [12] -->
Page 11 of 24

<!-- b000251 | caption | pages [12] -->
Figure 8: Gate Recurrent Unit Model

<!-- b000252 | prose | pages [12] -->
to a certain extent to ensure that use of the fewer parameters to mitigate the problem of gradient vanishing.

<!-- b000253 | prose | pages [12] -->
微信号：MATHmodels 𝑥𝑡−1 Multi-head Feature Map 𝑥𝑡 GRU

<!-- b000254 | prose | pages [12] -->
ℎ𝑡−1

<!-- b000255 | prose | pages [12] -->
1 𝑓𝑡

<!-- b000256 | prose | pages [12] -->
… ℎ𝑡 0 2 Player Embedding 𝑥𝑡−1 𝑓𝑡 0 𝑥𝑡 Player Momentum MLP

<!-- b000257 | caption | pages [12] -->
Figure 9: GRU Model with Reconstructed Input and Player Embedding

<!-- b000258 | prose | pages [12] -->
To further model the match process between player1 and player2, we added Player Embedding to the GRU, generating a feature vector for each player, as shown in the Figure 9. Assuming that at the current moment t, players p1 and p2 are in a match, and the initial feature is x0 t, we transform this feature through a multi-head feature mapping layer to obtain xt, and then merge it with the embeddings of the players:

<!-- b000259 | prose | pages [12, 13] -->
xt = [Multi-MLP(x0 t) || Emb(p1) || Emb(p2)] (6) ht = GRU(xt) (7)

<!-- b000260 | furniture | pages [12] -->
关注数学模型

<!-- b000261 | furniture | pages [12] -->
2

<!-- b000262 | furniture | pages [12] -->
MATHmodels

<!-- b000263 | furniture | pages [12] -->
获取更多资讯

<!-- b000264 | furniture | pages [13] -->
Team # 2409961

<!-- b000265 | furniture | pages [13] -->
Page 12 of 24

<!-- b000267 | prose | pages [13] -->
Emb represents an embedding function. Afterward, we generate the momentum for different 微信公众号：数学模型 players, that is:

<!-- b000268 | prose | pages [13] -->
f 1 t = MLPp1([ht || Emb(p1)]) (8) f 2 t = MLPp2([ht || Emb(p2)]) (9)

<!-- b000269 | prose | pages [13] -->
Thus, we have generated the momentum of the players at moment t, where the difference between them is the momentum predicted by the model at this moment.

<!-- b000270 | prose | pages [13] -->
mt = f 2 t −f 1 (10) t

<!-- b000271 | prose | pages [13] -->
During training, we utilize the MSE loss function to enable the model to learn how to predict the real momentum.

<!-- b000272 | prose | pages [13] -->
微信号：MATHmodels However, due to the complexity of the original data, there are many indicators, and the high cost of obtaining the data, which makes the input of GRU more complicated. To make the model have a practical prediction function under the existing conditions, we optimize the inputs, to be able to invert the output of the original inputs through the output of the optimized inputs, to get the key influencing factors of the "momentum". The process is described below:

<!-- b000273 | prose | pages [13] -->
Classify the input of GRU

<!-- b000274 | prose | pages [13] -->
Firstly, the irrelevant and linear correlation information is eliminated from the data. It is known that there are 47 dimensions in the race data, and after removing the 5-dimensional information such as "match id", which is not very relevant to the real-time score of the race, 39 dimensions of relevant information and 1 dimension of real-time score information are obtained. Secondly, the data were categorized. The obtained 39-dimensional score-related information was categorized into 6 major attributes, namely, mentality, endurance, error rate, starting advantage, skill, and key moments, as shown in Table 1:

<!-- b000275 | caption | pages [13] -->
Table 2: Notations used in this literature

<!-- b000276 | prose | pages [13] -->
Aggregation dimension Including indicators

<!-- b000277 | prose | pages [13] -->
Mentality set no, p1 sets, p2 sets, game no, p1 games, p2 games, p1 score, p2 score, p1 points won, p2 points won, game victor, set victor Endurance elapsed time, p1 distance run, p2 distance run, rally count Error Rate serve no, p1 double fault, p2 double fault, p1 unf err, p2 unf err Offensive server, speed mph, serve width, serve depth, return depth Skill server, speed mph, serve width, serve depth, return depth Key Point p1 break pt won, p2 break pt won, p1 break pt missed, p2 break pt missed

<!-- b000278 | prose | pages [13, 14] -->
Among these attributes, the mentality attribute, the points of the game of both sides, and the set games of the game will have a complex impact on the mentality of different players, for example, the score of the game may cause the psychological defense of the trailing player to collapse; In the attribute of endurance, the running distance and the duration of the game can reflect the endurance of the players; In the attribute of error rate, when "serve no" is 2, it means that the player has served the ball twice at this point, that is, at this time, the player has made a mistake when serving the 微信公众号：数学模型 ball, and the other mistakes of the player in the match, such as double fault, unforced error, will be attributed to the "error rate".

<!-- b000279 | furniture | pages [13] -->
关注数学模型

<!-- b000280 | furniture | pages [13] -->
2

<!-- b000281 | furniture | pages [13] -->
MATHmodels

<!-- b000282 | furniture | pages [13] -->
获取更多资讯

<!-- b000283 | furniture | pages [14] -->
Team # 2409961

<!-- b000284 | furniture | pages [14] -->
Page 13 of 24

<!-- b000286 | prose | pages [14] -->
Quantitative Analysis of the Impact of GRU Input

<!-- b000287 | prose | pages [14] -->
First, the data is downscaled. The entire information in each attribute is aggregated into a single number through six Linear layers with different inputs. Then, this number is fixed to between -1 and 1 by an activation function tanh, and this number is used as the value of that attribute to regularize the data. The resulting 6-dimensional data is then fed into the GRU as an input to obtain the output, i.e., the "momentum". The flow is shown in the figure below:

<!-- b000288 | prose | pages [14] -->
Next, we introduce the integrated gradient method, an algorithm capable of calculating the strength of the influence of the input features on the most output results: The integrated gradient 微信号：MATHmodels algorithm combines the design ideas of direct gradient and the backpropagation-based imputation techniques DeepLift and LRP divide-and-conquer to satisfy the axioms of sensitivity and realization invariance. Let the input be x, the baseline value be x’, and the function mapping is denoted as F. The integral gradient for the ith dimension of the input can be expressed as follows:

<!-- b000289 | prose | pages [14] -->
Z 1 ′ ′ ∂F(x i + α × (xi −x i)) ′ IntegratedGradientsi = (xi −x dα i) × (11) ′ ∂x a=0 i

<!-- b000290 | prose | pages [14] -->
Secondly, we use the integrated integral algorithm to invert the strength of influence of each attribute on the prediction results.

<!-- b000291 | prose | pages [14] -->
Performance Metrics by Category

<!-- b000292 | prose | pages [14] -->
0.23 0.2

<!-- b000293 | prose | pages [14] -->
0.1

<!-- b000294 | prose | pages [14] -->
0.02 0.0 -0.02 Score -0.03

<!-- b000295 | prose | pages [14] -->
−0.1

<!-- b000296 | prose | pages [14] -->
−0.2

<!-- b000297 | prose | pages [14, 15] -->
-0.29 -0.31 −0.3 Mentality Endurance Error Rate Oﬀensive Skill Key Point Category According to the chart above, it can be found that there are positive and negative impact strengths, which is because the impact of the 6-dimensional attributes on the momentum is categorized into positive and negative effects, in which the miss rate plays a negative role and the rest are positive. In this study, only absolute values are considered here to reflect the magnitude of the influence 微信公众号：数学模型 strength. As shown in Figure 10, among the 6 major attributes, the influence of mindset, skill, and turnover rate on momentum is more significant, and the influence of the remaining three- dimensional attributes is relatively weak.

<!-- b000298 | caption | pages [14] -->
Figure 10: The Impact of Each Attribute

<!-- b000299 | furniture | pages [14] -->
关注数学模型

<!-- b000300 | furniture | pages [14] -->
2

<!-- b000301 | furniture | pages [14] -->
MATHmodels

<!-- b000302 | furniture | pages [14] -->
获取更多资讯

<!-- b000303 | furniture | pages [15] -->
Team # 2409961

<!-- b000304 | furniture | pages [15] -->
Page 14 of 24

<!-- b000306 | prose | pages [15] -->
Selecting high-impact information from attributes

<!-- b000307 | prose | pages [15] -->
First of all, in the training process of GRU, the back-propagation algorithm will not only optimize the parameters of GRU itself, but also optimize the 6 Linear layer coefficients in the process of data dimensionality reduction, i.e., 6 Linear layer coefficients of each dimensional information in each major class of attributes

<!-- b000308 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000309 | caption | pages [15] -->
Figure 11: Linear Layer Weights of Attributes

<!-- b000310 | prose | pages [15] -->
From this, we can consider the strength of the influence of the attributes and the proportion of each information in the attributes to select the information that has the greatest impact on the prediction.

<!-- b000311 | prose | pages [15, 16] -->
Secondly, we can see in the Figure ?? that the 6 Linear layer coefficients are still both positive and negative, and here again we consider the absolute value of the effect of the information on the attribute. Not only that, but we find that there is a lot of the same information that distinguishes Player 1 from Player 2, but since we are considering the effect of the information on the game of tennis, we add up the absolute values of the coefficients of these pairs of information and and then compare which information has the greatest impact on the attributes. We found a total of 12 highly influential messages in each of the 6 Linear layers for each of those three highly influential attributes, namely ’p1 winner’, ’p2 winner’, ’p1 net pt’, ’p2 net pt’, ’p1 net pt won’, ’p2 net pt won’, ’ p1 unf err’,’p2 unf err’, ’p1 games’, ’p2 games’, ’p1 score’, ’p2 score’, these twelve pieces of information are extremely easy to obtain race information, which drastically reduces the cost of information collection compared to the original 39-dimensional information.

<!-- b000312 | furniture | pages [15] -->
关注数学模型

<!-- b000313 | furniture | pages [15] -->
2

<!-- b000314 | furniture | pages [15] -->
MATHmodels

<!-- b000315 | furniture | pages [15] -->
获取更多资讯

<!-- b000316 | furniture | pages [16] -->
Team # 2409961

<!-- b000317 | furniture | pages [16] -->
Page 15 of 24

<!-- b000319 | heading | pages [16] -->
6.2 Match Suggestion Based on Capability Evaluation

<!-- b000320 | prose | pages [16] -->
微信公众号：数学模型 From the GRU model, it can be seen that the direction of each game is controlled by a set of attributes. Therefore, the influence strength of a set of attribute values can be calculated by the integrated gradient method based on the data of a match, and here we consider the influence strength of each attribute value as the difference between the attribute values of Player 1 and Player 2. For example, when the psychological potential attribute is 2 in the result of a match, 2 is the psychological potential of the winner - the psychological potential of the loser. Therefore, we can derive the value on each dimension for each player from 32*6 unknown quantities. Since there are only 31 sets of data in the data, we take the attribute value of the champion player Carlos Alcaraz as the standard, i.e., we consider all six dimensions to have a value of 10. In this way, the number of linear equations is equal to the number of unknown quantities, and the system of linear equations has a unique solution. Based on this, we constructed an algorithm for evaluating players’ 微信号：MATHmodels six-dimensional abilities, and by solving the system of linear equations, the six-dimensional ability attribute values of each player are obtained:

<!-- b000321 | caption | pages [16] -->
Figure 12: Player Attribute Map

<!-- b000322 | prose | pages [16] -->
Therefore, we know six dimensions that have a large impact on player momentum, and differ- ences in these six dimensions from player to player will lead to fluctuations in the "momentum" of the game. As shown in Figure 16, we analyzed the six dimensions of ability of eight different players in the data, using the champion player Carlos Alcaraz as a standard. Overall, there is no absolute disadvantage in the six-dimensional ability of the eight players, which is consistent with the assumption made in the previous section that the players in Grand Slam tournaments have a certain degree of basic strength. However, it is also easy to see that the other players have varying degrees of deficiencies in the six dimensions compared to the champion players. We suggest that when players face different opponents in new tournaments, they should target their deficiencies in the ability dimensions in order to strive for advantages more efficiently, while they should be careful to beware of the counter-motivation that the opponents’ advantages in the ability dimensions may cause to themselves.

<!-- b000323 | prose | pages [16, 17] -->
In addition to the champion as a reference standard, the remaining players’ ability deficiencies are analyzed and targeted as follows: the six-dimensional abilities of the first two players (Matteo and Alexander) in Fig. 1 represent a class of opponents with deficiencies in mentality. Therefore, we suggest that players: (1) Pay attention to their opponents’ reactions to special events, such as scoring during the game, in order to recognize their deficiencies in the mental dimension. (2) Maintain a stable mindset and slowly break down the opponent’s mental defenses; create a pressure 微信公众号：数学模型 environment for the opponent after scoring a point; and use fakes and other striking techniques to influence the opponent’s mental posture.

<!-- b000324 | furniture | pages [16] -->
关注数学模型

<!-- b000325 | furniture | pages [16] -->
2

<!-- b000326 | furniture | pages [16] -->
MATHmodels

<!-- b000327 | furniture | pages [16] -->
获取更多资讯

<!-- b000328 | furniture | pages [17] -->
Team # 2409961

<!-- b000329 | furniture | pages [17] -->
Page 16 of 24

<!-- b000331 | prose | pages [17] -->
For the second, third, and seventh players in Fig. 16 who have dimensional deficiencies in endurance, we suggest: (1) Pay attention to the opponent’s performance in rallying, etc., and recognize his or her lack of endurance due to lack of physical strength and energy, etc. (2) Be prepared to fight a prolonged battle, stretching the battle line and fighting a war of attrition.

<!-- b000332 | prose | pages [17] -->
For the second and seventh players in Figure 16 who have dimensional deficiencies in error rate, we suggest: (1) Pay attention to whether the number of times the opponent’s serve needs to be successful and the number of non-pressure errors is high, and identify the problem that the opponent is prone to causing errors. (2) Focus on themselves and wait for the opponent to make a 微信号：MATHmodels mistake; play less skillful and less aggressive shots to lead the opponent to let down his/her guard and create an environment for him/her to make a mistake.

<!-- b000333 | heading | pages [17] -->
7 Generalization Testing

<!-- b000334 | heading | pages [17] -->
7.1 Basic Test

<!-- b000335 | prose | pages [17] -->
To further test our model, we retrained the model on a much smaller training set and will test the model in other matches. We used the first 24 matches in the dataset as the training set and the last 7 matches as the test set and obtained the results as shown in the table 3.

<!-- b000336 | caption | pages [17] -->
Table 3: Test Loss for Wimbledon Models

<!-- b000337 | prose | pages [17] -->
Match ID 1501 1502 1503 1504 1601 1602 1701 MSE 0.0201 0.0245 0.0279 0.0192 0.0306 0.0132 0.0151

<!-- b000338 | prose | pages [17] -->
In addition, we have presented the performance of our model in predicting the final as shown in the figure. The subgraph above represents the momentum of player 1 and player 2, and the difference in momentum represents the overall trend of the game, as shown in the following figure 13. As can be seen from the results, the predicted values basically coincide with the actual values, and the model results predict the match trend better.

<!-- b000339 | heading | pages [17] -->
7.2 Error Analysis

<!-- b000340 | prose | pages [17] -->
We note, however, that the model’s ability to predict sudden situational changes in the schedule is average. We believe this is due to the fact that the model can only be trained and generate relatively smooth sequences based on past datasets, and is unable to take into account the impact of unexpected factors in the fixtures. On this basis, we hypothesize that some difficult-to-quantify information may have an impact on model performance:

<!-- b000341 | prose | pages [17, 18] -->
• Venue information:Although we added the variable of different venues during the training of Player’s Momentum of 2023-wimbledon-1701

<!-- b000342 | furniture | pages [17] -->
关注数学模型

<!-- b000343 | furniture | pages [17] -->
2

<!-- b000344 | furniture | pages [17] -->
MATHmodels

<!-- b000345 | furniture | pages [17] -->
获取更多资讯

<!-- b000346 | furniture | pages [18] -->
Team # 2409961

<!-- b000347 | furniture | pages [18] -->
Page 17 of 24

<!-- b000349 | prose | pages [18] -->
player1 player1 better player2 player2 better 0.4 Player’s Momentum 微信公众号：数学模型 0.2

<!-- b000350 | prose | pages [18] -->
0.0

<!-- b000351 | prose | pages [18] -->
0 2500 5000 7500 10000 12500 15000 17500 Momentum Prediction of 2023-wimbledon-1701

<!-- b000352 | prose | pages [18] -->
momentum 0.4 predict

<!-- b000353 | prose | pages [18] -->
0.2 Momentum 0.0 微信号：MATHmodels −0.2

<!-- b000354 | prose | pages [18] -->
−0.4 0 2500 5000 7500 10000 12500 15000 17500 Time

<!-- b000355 | caption | pages [18] -->
Figure 13: Player’s Momentum and Momentum Prediction of 2023-wimbledon-1701.

<!-- b000356 | prose | pages [18] -->
the model, the model’s ability to predict matches in different venues is not only affected by the type of venues in the tournament area, but more venue details should be considered.

<!-- b000357 | prose | pages [18] -->
• Tactical Adjustment: There are individual differences in the ability of players to adjust their tactics and adapt to changes in the opponent’s tactics, which cannot be accurately calculated, but has a greater impact on the game situation.

<!-- b000358 | prose | pages [18] -->
• Players’ physical health information: Although factors such as whether or not a player is injured and the degree of injury can be measured, the impact of injuries on a player’s own play and ability to cope with the offense during the match is complex.

<!-- b000359 | prose | pages [18] -->
• Atmosphere: It is difficult to quantify the impact of crowd encouragement and other atmo- spheric factors on players, but it has a greater impact on their play.

<!-- b000360 | heading | pages [18] -->
7.3 Generalization Ability Test

<!-- b000361 | prose | pages [18] -->
1. Different surface. We selected two surfaces, Hard and Grass, for testing and drew the corresponding MSE violin plots, the results of these experiments are illustrated in Figure 14a. We can find that our model also performs better on Hard surfaces, but its effect is worse than that of Grass surfaces, with more volatility, which is because the matches in our training set are also on Grass surfaces, and the matches on Hard surfaces are actually in the tests outside the training set distribution.

<!-- b000362 | furniture | pages [18] -->
关注数学模型

<!-- b000363 | furniture | pages [18] -->
2

<!-- b000364 | furniture | pages [18] -->
MATHmodels

<!-- b000365 | furniture | pages [18] -->
获取更多资讯

<!-- b000366 | furniture | pages [19] -->
Team # 2409961

<!-- b000367 | furniture | pages [19] -->
Page 18 of 24

<!-- b000368 | prose | pages [19] -->
MSE Distribution by Surface Type MSE Distribution by Event Categories

<!-- b000369 | prose | pages [19] -->
0.08 微信公众号：数学模型 0.08

<!-- b000370 | prose | pages [19] -->
0.06 0.06

<!-- b000371 | prose | pages [19] -->
MSE MSE 0.04 0.04

<!-- b000372 | prose | pages [19] -->
0.02 0.02

<!-- b000373 | prose | pages [19] -->
0.00 0.00 Hard Grass Men's Singles Women's Singles Men's Doubles Women's Doubles Mixed Doubles Surface Type Event Categories

<!-- b000374 | prose | pages [19] -->
(a) MSE Distribution by Surface Type. (b) MSE Distribution by Event Categories.

<!-- b000375 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000376 | caption | pages [19] -->
Figure 14: Comparative Analysis of Tennis Data.

<!-- b000377 | prose | pages [19] -->
Player’s Momentum of Tokyo 2020 Olympic table tennis men’s singles ﬁnal 0.05

<!-- b000378 | prose | pages [19] -->
0.00 Player’s Momentum −0.05

<!-- b000379 | prose | pages [19] -->
−0.10 Zhendong Fan Long Ma −0.15 Zhendong Fan Better Long Ma Better

<!-- b000380 | prose | pages [19] -->
1000 1500 2000 2500 3000 3500 4000 Momentum Prediction of Tokyo 2020 Olympic table tennis men’s singles ﬁnal

<!-- b000381 | prose | pages [19] -->
ﬂow 0.4 predict 0.2 Momentum 0.0

<!-- b000382 | prose | pages [19] -->
−0.2 −0.4 −0.6

<!-- b000383 | prose | pages [19] -->
1000 1500 2000 2500 3000 3500 4000 Time

<!-- b000384 | caption | pages [19] -->
Figure 15: Player’s Momentum and Momentum of Tokyo 2020 Olympic table tennis men’s singles

<!-- b000385 | prose | pages [19] -->
final.

<!-- b000386 | furniture | pages [19] -->
关注数学模型

<!-- b000387 | furniture | pages [19] -->
2

<!-- b000388 | furniture | pages [19] -->
MATHmodels

<!-- b000389 | furniture | pages [19] -->
获取更多资讯

<!-- b000390 | furniture | pages [20] -->
Team # 2409961

<!-- b000391 | furniture | pages [20] -->
Page 19 of 24

<!-- b000392 | prose | pages [20] -->
2. Different event categories. We conducted experiments across various event categories, including Men’s Singles, Women’s Singles, Men’s Doubles, Women’s Doubles, and Mixed Doubles. The results of these experiments are illustrated in Figure 14b. It was observed that our model performs best in Men’s Singles matches. This is attributed to the fact that 微信公众号：数学模型 the training dataset predominantly consists of Men’s Singles matches. For other categories, there is a slight decline in model performance.

<!-- b000393 | prose | pages [20] -->
3. Other types of matches. Subsequently, we tested the application of the model to other matches, and we examined the performance of its application to the data of the table tennis final (Long Ma vs. Zhendong Fan) of the 2020 Tokyo Olympics. The result is in the Figure 15. It should be noted that due to the ball type difference, the table tennis data are different compared to the tennis, and for the features that do not exist, we set them all to zero. We found that our model also performed better in table tennis, which matches the actual match conditions.

<!-- b000394 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000395 | heading | pages [20] -->
8 Conclusion

<!-- b000396 | prose | pages [20] -->
In our work, we propose instantaneous scoring rate models to analyze player performance at specific points in time. By constructing flow momentum independent and non-independent models, it is obtained that momentum and player success are not independent of each other. Based on the manually constructed six dimensions, we utilized an integrated gradient algorithm to invert the strength of influence of the six dimensions on the output through the GRU model output. Based on the model results, we obtained 12 important metrics that have a strong impact on schedule fluctuations. Using these indicators, we were able to accurately predict the schedule fluctuations. We built a six-attribute evaluation system to make suggestions for players to deal with different opponents. On the basis of testing the generalizability of the model, we provide training suggestions for tennis coaches, pointing out the indicators and dimensions they can focus on, so as to improve the overall competitiveness of players on the court.

<!-- b000397 | heading | pages [20] -->
9 Strengths and Possible Improvements

<!-- b000398 | heading | pages [20] -->
9.1 Strength

<!-- b000399 | prose | pages [20] -->
• We are able to predict the future direction of momentum in the schedule with very little and easily accessible data at a very high level of refinement.

<!-- b000400 | prose | pages [20] -->
• we have a complete theory and algorithms for reproducing various attribute metrics of players.

<!-- b000401 | prose | pages [20] -->
• Our model has good generalization and can still maintain high prediction accuracy in other types of tennis matches (e.g., women’s matches, mixed doubles matches) and even in other ball games (e.g., table tennis).

<!-- b000402 | heading | pages [20] -->
9.2 Possible Improvements

<!-- b000403 | prose | pages [20] -->
• If we have more data, we can further train the model to better evaluate each person’s attribute values and improve their prediction accuracy by having more players compete with each other.

<!-- b000404 | furniture | pages [20] -->
关注数学模型

<!-- b000405 | furniture | pages [20] -->
2

<!-- b000406 | furniture | pages [20] -->
MATHmodels

<!-- b000407 | furniture | pages [20] -->
获取更多资讯

<!-- b000408 | furniture | pages [21] -->
Team # 2409961

<!-- b000409 | furniture | pages [21] -->
Page 20 of 24

<!-- b000410 | prose | pages [21] -->
• We are unable to obtain information through statistical data from past competitions, such as weather conditions, venue information, player tactical adjustments, and their adaptability

<!-- b000411 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000412 | heading | pages [21] -->
References

<!-- b000413 | references | pages [21] -->
[1] Braidwood, J. (2023), Novak Djokovic has created a unique rival – is Wimbledon defeat the

<!-- b000414 | references | pages [21] -->
beginning of the end, The Independent, https://www.independent.co.uk/sport/tennis/novak-

<!-- b000415 | references | pages [21] -->
djokovic-wimbledon-final-carlos-alcarazb2376600.html.

<!-- b000416 | references | pages [21] -->
[2] Silva, J. M., Hardy, C. J., Crace, R. K. (1988). Analysis of psychological momentum in

<!-- b000417 | references | pages [21] -->
intercollegiate tennis. Journal of sport and exercise psychology, 10(3), 346-354.

<!-- b000418 | references | pages [21] -->
[3] O’Donoghue, P., Brown, E. (2009). Sequences of service points and the misperception of

<!-- b000419 | references | pages [21] -->
momentum in elite tennis. International Journal of Performance Analysis in Sport, 9(1),

<!-- b000420 | references | pages [21] -->
113-127.

<!-- b000421 | references | pages [21] -->
微信号：MATHmodels

<!-- b000422 | references | pages [21] -->
[4] Meier, P., Flepp, R., Ruedisser, M., Franck, E. (2020). Separating psychological momentum

<!-- b000423 | references | pages [21] -->
from strategic momentum: Evidence from men’s professional tennis. Journal of economic

<!-- b000424 | references | pages [21] -->
psychology, 78, 102269.

<!-- b000425 | references | pages [21] -->
[5] Dietl, H., Nesseler, C. (2017). Momentum in tennis: Controlling the match. UZH Business

<!-- b000426 | references | pages [21] -->
Working Paper Series, (365)., Addison-Wesley Publishing Company, 1986.

<!-- b000427 | references | pages [21] -->
[6] Goyal, A., Simonoff, J. S. (2020). Hot Racquet or Not? An Exploration of Momentum in

<!-- b000428 | references | pages [21] -->
Grand Slam Tennis Matches. arXiv preprint arXiv:2009.05830.

<!-- b000429 | references | pages [21] -->
[7] Higham, A. (2000). Momentum: The hidden force in tennis. Coachwise 1st4sport.

<!-- b000430 | references | pages [21] -->
[8] Meier, P., Flepp, R., Ruedisser, M., Franck, E. (2020). Separating psychological momentum

<!-- b000431 | references | pages [21] -->
from strategic momentum: Evidence from men’s professional tennis. Journal of economic

<!-- b000432 | references | pages [21] -->
psychology, 78, 102269.

<!-- b000433 | references | pages [21] -->
[9] Weinberg, R., Jackson, A. (1989). The effects of psychological momentum on male and female

<!-- b000434 | references | pages [21] -->
tennis players revisited. Journal of Sport Behavior, 12(3), 167.

<!-- b000435 | furniture | pages [21] -->
关注数学模型

<!-- b000436 | furniture | pages [21] -->
2

<!-- b000437 | furniture | pages [21] -->
MATHmodels

<!-- b000438 | furniture | pages [21] -->
获取更多资讯

<!-- b000439 | furniture | pages [22] -->
Team # 2409961

<!-- b000440 | furniture | pages [22] -->
Page 21 of 24

<!-- b000441 | heading | pages [22] -->
Memo

<!-- b000442 | prose | pages [22] -->
From: Team #2409961, MCM 2024 To: Coaches 微信公众号：数学模型 Date: February 5, 2024

<!-- b000443 | prose | pages [22] -->
Dear Sir and Madam:

<!-- b000444 | prose | pages [22] -->
In response to your request, we have developed two models: an instantaneous scoring rate model and a GRU model. The instantaneous scoring rate model is used to identify which player is performing better at a given point in time and to verify the existence of a first-hand advantage. Before using the GRU model, we first utilized the momentum independent model and the non- independent model to test whether "momentum" has an impact on scoring during the game. The results were that "momentum" had a significant effect on scoring. Based on this, we divided the 微信号：MATHmodels data into 6-dimensional attributes, used the GRU model to predict the direction of the game, and used the integrated gradient algorithm to reverse the key factors affecting the "momentum" after the prediction results were available to obtain the 12 impact indicators. According to the above research, since the 12 indicators will affect the "momentum", and the "momentum" will affect the score of the game, and then affect the result of the game, in order to make the players get a better performance in the next game, we put forward the following suggestions:

<!-- b000445 | prose | pages [22] -->
• First of all, "momentum" has a significant impact on the change of the game process.

<!-- b000446 | prose | pages [22] -->
According to the above analysis, "momentum" is a quantitative expression of the fluctuation of the game process, and coaches can monitor the performance of players in the game process in a more concrete and intuitive way in real time in order to do a good job in the pre- game and post-game analysis; at the same time, this study also summarizes 12 indicators of "momentum" that affect the performance of players in the next game based on the data of the previous games. "At the same time, this study also summarizes the 12 indicators and the 6-dimensional attributes of the players based on the data of previous matches, so that coaches can make corresponding tactical strategies for the 6-dimensional attributes of the opponents before the match, and also analyze the changes in the momentum of the players based on the 12 indicators after the match, so that they can stabilize and increase their own momentum in the next match to get better results. This is the role of "momentum".

<!-- b000447 | prose | pages [22] -->
• Secondly, the pre-match analysis starts from the opponent’s 6-dimensional attributes, and targets their weak attributes to launch a fierce attack, so as to win better. For example, if the opponent’s mentality is poor, you can try to increase the score in the early part of the game to put psychological pressure on the opponent; or play steadily in the early part of the game, when the opponent slightly ahead of the opponent began to overtake the opponent, so that the opponent loses self-confidence and thus weaken the opponent’s momentum.

<!-- b000448 | prose | pages [22, 23] -->
• Again, the post-game summary from the player’s "momentum" changes, according to the 12 indicators to determine the reasons for the change in momentum at this time, so as to avoid the "momentum" advantage flows to the opponent, for the next game to get ready! First, tactics. Firstly, in terms of tactics, attention should be paid to the direction, depth and speed of the serve to make it more difficult for the opponent to receive the ball, so as to increase the player’s own momentum; at the same time, the player can hit the ball to the two sides of the court, so as to increase the opponent’s distance to receive the ball, and to consume the 微信公众号：数学模型 opponent’s physical strength, which will then make the opponent reveal his/her weaknesses.

<!-- b000449 | furniture | pages [22] -->
关注数学模型

<!-- b000450 | furniture | pages [22] -->
2

<!-- b000451 | furniture | pages [22] -->
MATHmodels

<!-- b000452 | furniture | pages [22] -->
获取更多资讯

<!-- b000453 | furniture | pages [23] -->
Team # 2409961

<!-- b000454 | furniture | pages [23] -->
Page 22 of 24

<!-- b000456 | prose | pages [23] -->
Secondly, when a player has a double fault or unforced error, he/she should adjust his/her mindset positively; at the same time, the sets, games, and points of the game are also the key to influence the player’s mindset.

<!-- b000457 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000458 | caption | pages [23] -->
Figure 16: We need caption here.

<!-- b000459 | prose | pages [23] -->
As shown in the figure, we have proposed targeted suggestions based on the three most influential dimensions and their core indicators, as shown in Figure 10. We hope our suggestions are helpful. If you have any questions, please feel free to contact us. Thank you for reading.

<!-- b000460 | prose | pages [23] -->
Sincerely, MCM Team members

<!-- b000461 | furniture | pages [23] -->
关注数学模型

<!-- b000462 | furniture | pages [23] -->
2

<!-- b000463 | furniture | pages [23] -->
MATHmodels

<!-- b000464 | furniture | pages [23] -->
获取更多资讯

<!-- b000465 | furniture | pages [24] -->
Team # 2409961

<!-- b000466 | furniture | pages [24] -->
Page 23 of 24

<!-- b000467 | heading | pages [24] -->
Appendices

<!-- b000468 | prose | pages [24] -->
Python Code: 微信公众号：数学模型 class W6(nn.Module):

<!-- b000469 | prose | pages [24] -->
def __init__(self, input_size):

<!-- b000470 | prose | pages [24] -->
super(W6, self).__init__() self.W1 = nn.Linear(len(xintai), 1, bias=False) self.W2 = nn.Linear(len(chijiuli), 1, bias=False) self.W3 = nn.Linear(len(shiwulv), 1, bias=False) self.W4 = nn.Linear(len(qishou), 1, bias=False) self.W5 = nn.Linear(len(jiqiao), 1, bias=False) self.W6 = nn.Linear(len(guanjian), 1, bias=False) self.act = nn.Tanh() 微信号：MATHmodels def forward(self, x):

<!-- b000471 | prose | pages [24] -->
x1 = x[:,:, :len(xintai)] x2 = x[:,:, len(xintai):len(xintai)+len(chijiuli)] x3 = x[:,:, len(xintai)+len(chijiuli):len(xintai)+len(chijiuli)+len (shiwulv)] x4 = x[:,:, len(xintai)+len(chijiuli)+len(shiwulv):len(xintai)+len( chijiuli)+len(shiwulv)+len(qishou)] x5 = x[:,:, len(xintai)+len(chijiuli)+len(shiwulv)+len(qishou):len( xintai)+len(chijiuli)+len(shiwulv)+len(qishou)+len(jiqiao)] x6 = x[:,:, len(xintai)+len(chijiuli)+len(shiwulv)+len(qishou)+len( jiqiao):len(xintai)+len(chijiuli)+len(shiwulv)+len(qishou)+len( jiqiao)+len(guanjian)] # concatenate the output of the 6 subnetworks x1 = self.act(self.W1(x1)) x2 = self.act(self.W2(x2)) x3 = self.act(self.W3(x3)) x4 = self.act(self.W4(x4)) x5 = self.act(self.W5(x5)) x6 = self.act(self.W6(x6)) return torch.cat((x1, x2, x3, x4, x5, x6), -1) class GruRNN(nn.Module):

<!-- b000472 | prose | pages [24] -->
def __init__(self, input_size, hidden_size=1, output_size=1, num_layers =1):

<!-- b000473 | prose | pages [24, 25] -->
super().__init__() self.gru = nn.GRU(3*hidden_size, hidden_size, num_layers, batch_first=True) # utilize the GRU model in torch.nn self.linear0 = nn.Linear(input_size, hidden_size) self.activation = nn.Tanh() self.linear01 = nn.Linear(hidden_size, hidden_size) self.linear11 = nn.Linear(hidden_size + hidden_size, hidden_size) self.dropout = nn.Dropout(0.2) self.linear21 = nn.Linear(hidden_size, output_size) self.linear12 = nn.Linear(hidden_size + hidden_size, hidden_size) 微信公众号：数学模型 self.linear22 = nn.Linear(hidden_size, output_size) self.sigmoid = nn.Tanh() self.player_embedding = nn.Embedding(32, hidden_size) def forward(self,_x, p1=None, p2=None,ig=False):

<!-- b000474 | furniture | pages [24] -->
关注数学模型

<!-- b000475 | furniture | pages [24] -->
2

<!-- b000476 | furniture | pages [24] -->
MATHmodels

<!-- b000477 | furniture | pages [24] -->
获取更多资讯

<!-- b000478 | furniture | pages [25] -->
Team # 2409961

<!-- b000479 | furniture | pages [25] -->
Page 24 of 24

<!-- b000481 | prose | pages [25] -->
p1_emb = self.player_embedding(p1) p2_emb = self.player_embedding(p2) _x = self.linear0(_x) _x = torch.cat([p1_emb , p2_emb, _x], dim=2) x, _ = self.gru(_x) s, b, h = x.shape x = x.reshape(s * b, h) 微信号：MATHmodels p1_emb = p1_emb.reshape(s * b, -1) p2_emb = p2_emb.reshape(s * b, -1) x1 = self.linear11(torch.cat([x, p1_emb], dim=1)) x1 = self.sigmoid(x1) x1 = self.dropout(x1) x1 = self.linear21(x1) x1 = x1.reshape(s, b, -1) x2 = self.linear12(torch.cat([x, p2_emb], dim=1)) x2 = self.sigmoid(x2) x2 = self.dropout(x2) x2 = self.linear22(x2) x2 = x2.reshape(s, b, -1) return x1, x2 class Net(nn.Module):

<!-- b000482 | prose | pages [25] -->
def __init__(self, input_size,hid_dim = 128):

<!-- b000483 | prose | pages [25] -->
super(Net, self).__init__() self.w6 = W6(input_size) self.gru = GruRNN(6, hid_dim, 1, 1) def forward(self, x,p1,p2):

<!-- b000484 | prose | pages [25] -->
x = self.w6(x) x = self.gru(x,p1,p2) return x

<!-- b000485 | furniture | pages [25] -->
关注数学模型

<!-- b000486 | furniture | pages [25] -->
2

<!-- b000487 | furniture | pages [25] -->
MATHmodels

<!-- b000488 | furniture | pages [25] -->
获取更多资讯
