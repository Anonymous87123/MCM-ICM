# P-C-2024-2425454-a27c2efc

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
2425454

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Changing Tides: Momentum Swings in Tennis

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
Situations change rapidly in tennis, and the incredible swings are often attributed to mo- mentum. We analyze momentum through Wimbledon 2023 men’s matches data.

<!-- b000012 | prose | pages [1] -->
For Task 1, we develop a Leverage Quantitative Momentum Capture Model. Firstly, we consider the effect of short-term motivation and confidence boosting on serve percentage, and utilize the Monte Carlo algorithm to compute the winning probability(match/set/game) at each point. Then we define Leverage as how much winning or losing a ball changes the winning probability and the momentum as exponential moving average of leverage. Finally, the Wimbledon final match flow is visualized and the results are shown.

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
For Task 2, we use a statistical test to verify that "momentum" does play role in the match. Through the run test, we found that at a 90% confidence level, the proportion of non-random game scores in the given dataset accounts for 45.11% of the total, which indicates the swings in the game are not random. Furthermore, through the contingency table independence test, we determine, at a 90% confidence level, that swings in play and runs of success by one player are correlated to the momentum.

<!-- b000015 | prose | pages [1] -->
For Task 3, we establish the Grid-Search Random Forest Swing Predictor Model to fore- cast short-term swings in momentum.We select 43 indicators as inputs for the model to predict momentum transition scenarios (no transition of advantage, the advantage tilting towards oneself, the advantage transitioning to the opponent) in the next s points. The model achieved a 94% successful classification rate on the training set, demonstrating good classification perfor- mance. Utilizing GSRF, we can also identify that the factor most related to match fluctuations is the opponent’s total score.

<!-- b000016 | prose | pages [1] -->
It is necessary to consider he top 15 factors in the GSRF model in terms of feature importance, so the four factors of dimensionality reduction into Expenditure, Expenditure, Running Distance, and Game Situation Factor are utilized by factor analysis. We suggest players focus on improving physical fitness, enhancing mental resilience, and paying special attention to break and net point scoring techniques.

<!-- b000017 | prose | pages [1] -->
For Task 4 , by modifying the Monte Carlo simulation winning rule to three sets to two wins, we apply the model in the 2023 Wimbledon women’s singles final, which verifies that the model is generalizable. It is worth noting that the most related factor of swing in women’s tennis is different from that in men’s singles, it is precise the total running distance, which may be be related to the physical strength difference between men and women.

<!-- b000018 | prose | pages [1] -->
We conduct sensitivity analysis on the parameters of the short-term motivation effect in the Leverage Quantitative Momentum Capture Model and the parameters in the GSRF Swing Predictor Model, which are low in sensitivity and have high robustness.

<!-- b000019 | prose | pages [1] -->
Finally, a one-page memo with suggestions to tennis coaches is also produced to help coaches instruct players to control the pace of play.

<!-- b000020 | keywords | pages [1] -->
Keywords: Monte Carlo Simulation, Runs Test, GSRF, Factor Analysis

<!-- b000021 | prose | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | heading | pages [2] -->
Contents

<!-- b000026 | contents | pages [2] -->
1 Introduction

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | contents | pages [2] -->
1.1

<!-- b000029 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000032 | contents | pages [2] -->
1.2

<!-- b000033 | contents | pages [2] -->
Restatement and Analysis of the Problem . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
3

<!-- b000035 | contents | pages [2] -->
1.3

<!-- b000036 | contents | pages [2] -->
Overview of Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
4

<!-- b000038 | contents | pages [2] -->
2 Assumptions and Justification

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
3 List of Notation

<!-- b000041 | contents | pages [2] -->
5

<!-- b000042 | contents | pages [2] -->
4 Data Pre-processing

<!-- b000043 | contents | pages [2] -->
5

<!-- b000044 | contents | pages [2] -->
5 Task 1 : Captures the Flow of Play

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
5.1

<!-- b000047 | contents | pages [2] -->
Specifying Conceptual Significance

<!-- b000048 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
6

<!-- b000050 | contents | pages [2] -->
5.2

<!-- b000051 | contents | pages [2] -->
Leverage Quantitative Momentum Capture Model . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
6

<!-- b000053 | contents | pages [2] -->
5.2.1

<!-- b000054 | contents | pages [2] -->
Impact of Short-term Motivation and Confidence Boost on Serve Suc-

<!-- b000055 | contents | pages [2] -->
cess Rate

<!-- b000056 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
6

<!-- b000058 | contents | pages [2] -->
5.2.2

<!-- b000059 | contents | pages [2] -->
Monte Carlo Simulation for Winning Probability

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
9

<!-- b000062 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000063 | contents | pages [2] -->
5.2.3

<!-- b000064 | contents | pages [2] -->
Leveraging Every Point with Counterfactual Framework

<!-- b000065 | contents | pages [2] -->
. . . . . . . .

<!-- b000066 | contents | pages [2] -->
10

<!-- b000067 | contents | pages [2] -->
5.2.4

<!-- b000068 | contents | pages [2] -->
Defining Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
11

<!-- b000070 | contents | pages [2] -->
5.3

<!-- b000071 | contents | pages [2] -->
Visualization of the Flow of Play . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
11

<!-- b000073 | contents | pages [2] -->
6

<!-- b000074 | contents | pages [2] -->
Task 2 : Whether the Swings of Play and Momentum are correlated

<!-- b000075 | contents | pages [2] -->
12

<!-- b000076 | contents | pages [2] -->
6.1

<!-- b000077 | contents | pages [2] -->
Run Test for Assessing Randomness in Match Scores Sequence . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
12

<!-- b000079 | contents | pages [2] -->
6.2

<!-- b000080 | contents | pages [2] -->
Scores-Momentum Contingency Analysis

<!-- b000081 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
13

<!-- b000083 | contents | pages [2] -->
7 Task 3 : Identify Indicators Signaling a Change in Flow

<!-- b000084 | contents | pages [2] -->
14

<!-- b000085 | contents | pages [2] -->
7.1

<!-- b000086 | contents | pages [2] -->
GSRF Swing Predictor Model

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
14

<!-- b000089 | contents | pages [2] -->
7.1.1

<!-- b000090 | contents | pages [2] -->
The Swings Reversal Point . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
14

<!-- b000092 | contents | pages [2] -->
7.1.2

<!-- b000093 | contents | pages [2] -->
The Selected Indicator

<!-- b000094 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [2] -->
15

<!-- b000096 | contents | pages [2] -->
7.1.3

<!-- b000097 | contents | pages [2] -->
GSRF Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [2] -->
15

<!-- b000099 | contents | pages [2] -->
7.1.4

<!-- b000100 | contents | pages [2] -->
The Predicted Swings Results of the Match

<!-- b000101 | contents | pages [2] -->
. . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
16

<!-- b000103 | contents | pages [2] -->
7.2

<!-- b000104 | contents | pages [2] -->
Player Performance Factor Analysis Model . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
17

<!-- b000106 | contents | pages [2] -->
8 Task 4 : Assess the Generalization of Model

<!-- b000107 | contents | pages [2] -->
20

<!-- b000108 | contents | pages [2] -->
8.1

<!-- b000109 | contents | pages [2] -->
Generalization in women’s tennis matches . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [2] -->
20

<!-- b000111 | contents | pages [2] -->
8.2

<!-- b000112 | contents | pages [2] -->
Discussion on the impact of the playing surface. . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [2] -->
22

<!-- b000114 | contents | pages [2] -->
9 Sensitivity Analysis

<!-- b000115 | contents | pages [2] -->
22

<!-- b000116 | contents | pages [2] -->
10 Strength and Weakness

<!-- b000117 | contents | pages [2] -->
23

<!-- b000118 | contents | pages [2] -->
10.1 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
23

<!-- b000120 | contents | pages [2] -->
10.2 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [2] -->
23

<!-- b000122 | contents | pages [2] -->
11 Further Discussion

<!-- b000123 | contents | pages [2] -->
23

<!-- b000124 | contents | pages [2] -->
Memorandum

<!-- b000125 | contents | pages [2] -->
24

<!-- b000126 | contents | pages [2] -->
Reference

<!-- b000127 | contents | pages [2] -->
25

<!-- b000128 | contents | pages [2] -->
关注数学模型

<!-- b000129 | furniture | pages [2] -->
2

<!-- b000130 | furniture | pages [2] -->
MATHmodels

<!-- b000131 | furniture | pages [2] -->
获取更多资讯

<!-- b000132 | furniture | pages [3] -->
Team # 2425454

<!-- b000133 | furniture | pages [3] -->
Page 3 of 25

<!-- b000134 | heading | pages [3] -->
1 Introduction

<!-- b000135 | heading | pages [3] -->
1.1 Background

<!-- b000136 | prose | pages [3] -->
Tennis matches are exciting and ever-changing. Players who seem to be dominating expe- 微信公众号：数学模型 rience incredible swings from time to time. For example, a player may be in control of the match with a series of points, but at one rally, the opponent suddenly breaks and the situation is reversed. We often attribute this dramatic turn of events to "momentum".

<!-- b000137 | prose | pages [3] -->
"Momentum" heightens emotional intensity in the match, creating unpredictability and anticipation, making each moment charged and intense.

<!-- b000138 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000139 | caption | pages [3] -->
Figure 1: The fast-changing, heart-stopping swings of a tennis match.

<!-- b000140 | heading | pages [3] -->
1.2 Restatement and Analysis of the Problem

<!-- b000141 | prose | pages [3] -->
We need to complete the following tasks based on the data given in the question and additional data from ourselves:

<!-- b000142 | prose | pages [3] -->
• Task 1 : Build a model to capture the flow of play as points occur.

<!-- b000143 | prose | pages [3] -->
The model is required to be able to qualitatively and quantitatively describe performance of players at a given time and provide a visualization. In particular, the model should take the higher probability of the server winning into account.

<!-- b000144 | prose | pages [3] -->
• Task 2 : Assess whether swings in play and runs of success by one player during a match are random.

<!-- b000145 | prose | pages [3] -->
• Task 3 : Look for indicators that identify the point in time when the game situation is reversed.

<!-- b000146 | prose | pages [3] -->
– Develop a model to predict swings in a match. Find the indicator with the highest correlation.

<!-- b000147 | prose | pages [3] -->
– Based on momentum swings in past games, we need to give players advice on how to deal with other opponents.

<!-- b000148 | prose | pages [3] -->
• Task 4 : Evaluate the generalisability of the model we have developed to other competitions.

<!-- b000149 | prose | pages [3] -->
• Task 5 : Write a memo summarising the results and giving targeted advice to coaches and players.

<!-- b000150 | prose | pages [3, 4] -->
关注数学模型 After some analysis, we found that there is a close relationship between the tasks: In Task 1 and Task 2, we need to build a model describing the situation of the game (i.e. the relative performance of two players) and explore the relationship between "momentum" and changes in the game situation, respectively. The results of these two tasks are the basis of task 3. In task 微信公众号：数学模型 3, we need to further build a model that can predict the situation fluctuations in the competition and find out the key factors that affect the competition. We also need to start to consider the applicability of our model. Can it provide competition suggestions for players to achieve better results? The fourth task is to consider the extensibility of our model. Are we still valuable in other competitions? Finally, in the memo, we need to focus on our model and its value.

<!-- b000151 | furniture | pages [3] -->
2

<!-- b000152 | furniture | pages [3] -->
MATHmodels

<!-- b000153 | furniture | pages [3] -->
获取更多资讯

<!-- b000154 | furniture | pages [4] -->
Team # 2425454

<!-- b000155 | furniture | pages [4] -->
Page 4 of 25

<!-- b000157 | prose | pages [4] -->
In summary, we should effectively build a model that can predict the fluctuations of the competition situation, provide practical advice to players and coaches, and be extensible across different competitions.

<!-- b000158 | heading | pages [4] -->
1.3 Overview of Our Work

<!-- b000159 | prose | pages [4] -->
On the basis of the above analysis, we have carried out our work. Our working framework is shown in Figure 2. 微信号：MATHmodels

<!-- b000160 | caption | pages [4] -->
Figure 2: Our Work Overview Schematic Diagram

<!-- b000161 | prose | pages [4, 5] -->
关注数学模型 The detailed modeling process and model details are presented in the following article.

<!-- b000162 | furniture | pages [4] -->
2

<!-- b000163 | furniture | pages [4] -->
MATHmodels

<!-- b000164 | furniture | pages [4] -->
获取更多资讯

<!-- b000165 | furniture | pages [5] -->
Team # 2425454

<!-- b000166 | furniture | pages [5] -->
Page 5 of 25

<!-- b000168 | heading | pages [5] -->
2 Assumptions and Justification

<!-- b000169 | prose | pages [5] -->
微信公众号：数学模型 To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified.

<!-- b000170 | prose | pages [5] -->
• When a player wins a point, he experiences a short-term "motivational" effect that increases the probability of winning the next point. The motivation effect can lead to increased self-confidence on a psychological level as well as increased physical conditioning on a physiological level.

<!-- b000171 | prose | pages [5] -->
• Lifting effects are cumulative. A string of successes may have a positive psychological and emotional effect on a player, so that a player winning more points in a row will result in a greater probability of winning the next point on serve.

<!-- b000172 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000173 | heading | pages [5] -->
3 List of Notation

<!-- b000174 | heading | pages [5] -->
Symbol

<!-- b000175 | prose | pages [5] -->
Meaning

<!-- b000176 | prose | pages [5] -->
p, q Probability of Winning mi Increase in the Rate of Serve points TAB The Cumulative Total Score Li Leverage of the ith Point G The leverage Gained M Momentum λ Tuning Parameter

<!-- b000177 | prose | pages [5] -->
Noted: Symbols not specified in the table should be referred to their first occurrence.

<!-- b000178 | heading | pages [5] -->
4 Data Pre-processing

<!-- b000179 | prose | pages [5] -->
• Outlier Handling

<!-- b000180 | prose | pages [5] -->
No clear outliers were observed in the data. However, in a match between Frances Tiafoe and Grigor Dimitrov during the third round, a notable occurrence occurred with a 24-hour time gap between two points at a set score of 2:0, as shown in Table 1.

<!-- b000181 | caption | pages [5] -->
Table 1: Suspected Outliers

<!-- b000182 | prose | pages [5, 6] -->
关注数学模型 Upon consulting relevant information, we found the following explanation:

<!-- b000183 | furniture | pages [5] -->
2

<!-- b000184 | furniture | pages [5] -->
MATHmodels

<!-- b000185 | furniture | pages [5] -->
获取更多资讯

<!-- b000186 | furniture | pages [6] -->
Team # 2425454

<!-- b000187 | furniture | pages [6] -->
Page 6 of 25

<!-- b000189 | prose | pages [6] -->
". . . . . . Saturday’s game was suspended due to inclement weather, so it was postponed to a day later to continue on Sunday.. . . . . . " 微信公众号：数学模型 Therefore, the data is correct.

<!-- b000190 | prose | pages [6] -->
• Missing Value Handling In thedatasetgiveninthequestion, thequantitiesservewidth, servedepth, and returndepth have missing values, for which we use the nearest-neighbour filling method to fill them.

<!-- b000191 | prose | pages [6] -->
• Tag Encoding of String Type Data There are many categorical variables in the data given in the title, presented as strings.

<!-- b000192 | prose | pages [6] -->
In order to make it easier for the model to receive this type of data, we preprocess this type of data by means of label coding, using virtual coding for the last three columns of servewidth, servedepth, and returndepth in the data of the tennis match.

<!-- b000193 | heading | pages [6] -->
5 Task 1 : Captures the Flow of Play

<!-- b000194 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000195 | heading | pages [6] -->
5.1 Specifying Conceptual Significance

<!-- b000196 | prose | pages [6] -->
Since a relatively large number of concepts are introduced in our model, we first identify and clarify the meaning of the introduced concepts here.

<!-- b000197 | prose | pages [6] -->
• Short-term Motivation refers to a brief period of above-average performance by a player following a motivating event.

<!-- b000198 | prose | pages [6] -->
• Confidence Boost is when a player, drawing upon their self-awareness developed through multiple games in their professional career and an assessment of the current situation, generates positive expectations regarding the outcome of the match.

<!-- b000199 | prose | pages [6] -->
• Serve Success Rate is probability of scoring in a service game.

<!-- b000200 | prose | pages [6] -->
• Winning Probability is the likelihood of the player winning the game/set/match.

<!-- b000201 | prose | pages [6] -->
• Leverage measures how a ball’s outcome impacts the margin of victory.

<!-- b000202 | prose | pages [6] -->
• Momentum aims to describe which player is in control at any given point in the match—based on who is currently winning more points and who is prevailing in cru- cial (high-leverage) moments. It is defined as a player’s exponentially weighted leverage average.

<!-- b000203 | prose | pages [6] -->
At each point in the match, both competing players will have their own momentum values.

<!-- b000204 | prose | pages [6] -->
• We define the fluctuations in momentum as the Flow of Play. The relationship between the above concepts, i.e., the framework of the model, is shown schematically below, and in the following we show the model building process in full.

<!-- b000205 | heading | pages [6] -->
5.2 Leverage Quantitative Momentum Capture Model

<!-- b000206 | heading | pages [6] -->
5.2.1 Impact of Short-term Motivation and Confidence Boost on Serve Success Rate

<!-- b000207 | prose | pages [6] -->
Short-term Motivation refers to a brief period of above-average performance by a player following a motivating event (e.g., a breaking serve) during a match, a phenomenon known in sports as "hot hands"[1]. We developed a probabilistic model that quantifies Short-term Motivation as an increase in serve success rate.

<!-- b000208 | prose | pages [6] -->
The following two assumptions are necessary:

<!-- b000209 | prose | pages [6, 7] -->
关注数学模型 微信公众号：数学模型

<!-- b000210 | furniture | pages [6] -->
2

<!-- b000211 | furniture | pages [6] -->
MATHmodels

<!-- b000212 | furniture | pages [6] -->
获取更多资讯

<!-- b000213 | furniture | pages [7] -->
Team # 2425454

<!-- b000214 | furniture | pages [7] -->
Page 7 of 25

<!-- b000216 | caption | pages [7] -->
Figure 3: Relationships Between Concepts, i.e., Schematic of the Framework of the Model

<!-- b000217 | prose | pages [7] -->
• When a player wins a point, he experiences a short-term "motivational" effect that in- creases the probability of winning the next point.

<!-- b000218 | prose | pages [7] -->
• Lifting effects are cumulative. A string of successes may have a positive psychological 微信号：MATHmodels and emotional effect on a player, so that a player winning more points in a row will result in a greater probability of winning the next point on serve.

<!-- b000219 | prose | pages [7] -->
Here i denotes the number of consecutive points scored by a player A or his opponent B; and mi denotes the increase in the rate of serving points on a player’s next serve after winning ipoints consecutively due to the short-term motivation gained. Then, the probability of winning the next serve under short-term motivation ps versus qs is calculated by equations (1) .

<!-- b000220 | prose | pages [7] -->
ps = pf(1 + mA i ); (1) qs = qf(1 + mB i ),

<!-- b000221 | prose | pages [7] -->
where pf and qf are the scoring probabilities before player A and player B are motivated, respectively.

<!-- b000222 | prose | pages [7] -->
The short-term motivation that a player receives for scoring a game n times in a row is referred to as n-order short-term motivation. Using the dataset given in the title, we statistically obtained a plot of the total number of short-term motivations occurring in a match versus order, and the results are shown in Figure 4. It is clear to see that short-term motivations of order four and above rarely occur in the dataset used in this study. Therefore, only short-term motivations of order three and below are considered in this paper.

<!-- b000223 | prose | pages [7] -->
Short-term motivation focuses on short-term status enhancement during matches and ignores sources of motivation on a longer time scale in the player’s lifetime, so we continue to introduce a confidence-boosting factor.

<!-- b000224 | prose | pages [7] -->
A new tuning parameter λ is introduced, which represents the effect of the confidence boosting factor on the success rate of the next serve [2], the probabilities after the effect are expressed as ps and qs – see equation (2) pc = TAB λ pt + (1 −TAB λ )p0; (2) qc = TAB λ qt + (1 −TAB λ )q0, where TAB denotes the cumulative total score of the opposing players since the start of the match, and pt and qt denote the probability of scoring for player A and player B, respectively,

<!-- b000225 | prose | pages [7, 8] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000226 | furniture | pages [7] -->
2

<!-- b000227 | furniture | pages [7] -->
MATHmodels

<!-- b000228 | furniture | pages [7] -->
获取更多资讯

<!-- b000229 | furniture | pages [8] -->
Team # 2425454

<!-- b000230 | furniture | pages [8] -->
Page 8 of 25

<!-- b000232 | caption | pages [8] -->
Figure 4: Histogram of the Total Count of Short-Term Incentives Occurring in Competitions as

<!-- b000233 | prose | pages [8] -->
a Function of Order

<!-- b000234 | prose | pages [8] -->
since the start of the match up to the present. p0 and q0 denote the historical data on the success rate of the opposing teams’ serves on the grass court surface prior to the current match (source: https://www.infosys.com/)

<!-- b000235 | prose | pages [8] -->
Eq. (2) describes the phenomenon that a player’s historical results always have the greatest impact on player status at the start of a match, and then diminish as the match progresses - the performance of the current match begins to influence player play more.

<!-- b000236 | prose | pages [8] -->
We then performed a linear interpolation of the obtained probabilities. The interpolation coefficient is the cumulative total score of the current pair divided by the coefficient λ (i.e. TAB λ ).

<!-- b000237 | prose | pages [8] -->
The short-term motivation is fluctuating as the match progresses, while the confidence boost takes into account the player’s self-perception established over the course of his career as well as the current situation in the match, which is the "undertone" of the motivated state, therefore, we use pc and qc in Eq. (2) instead of pf and qf in Eq. (1), we can get the success rate of the next serve after considering the short-term motivation and confidence improvement:

<!-- b000238 | prose | pages [8] -->
p = [TAB · pc + (1 −TAB λ )pt](1 + mA i ); λ q = [TAB · qc + (1 −TAB λ )qt](1 + mB i ). λ

<!-- b000239 | prose | pages [8] -->
The above equation shows the effect of short-term motivation and confidence enhancement on serve percentage.

<!-- b000240 | prose | pages [8] -->
In tennis matches, players typically have an advantage when serving[3]. According to the data we have collected, the serving success rate of professional players exceeds 50%. Based on this understanding, players gain confidence in serving games. Due to this "confidence boost," we have incorporated the player’s performance in serving games into consideration in our model.

<!-- b000241 | prose | pages [8] -->
关注数学模型

<!-- b000242 | furniture | pages [8] -->
2

<!-- b000243 | furniture | pages [8] -->
MATHmodels

<!-- b000244 | furniture | pages [8] -->
获取更多资讯

<!-- b000245 | furniture | pages [9] -->
Team # 2425454

<!-- b000246 | furniture | pages [9] -->
Page 9 of 25

<!-- b000247 | heading | pages [9] -->
5.2.2 Monte Carlo Simulation for Winning Probability

<!-- b000248 | prose | pages [9] -->
As a sports competition, there is a great deal of uncertainty in tennis, for which Monte Carlo algorithms can provide probabilistic estimates of the outcome.

<!-- b000249 | prose | pages [9] -->
微信公众号：数学模型 Based on the serve success rate obtained in the previous section, we use the Monte Carlo algorithm to simulate each ball, and ultimately obtain the winners and losers of each game, set and even the whole match. Then in this process, the randomness and diversity of the simulation are ensured by generating a large number of random number seeds.

<!-- b000250 | prose | pages [9] -->
Here is the pseudo-code for the algorithm we used:

<!-- b000251 | heading | pages [9] -->
Algorithm 1: Monte Carlo Simulation for Winning Probability

<!-- b000252 | prose | pages [9] -->
Input: phist,data Output: win_p 1 begin for i in scores do 2 for i 1 to n do 3 微信号：MATHmodels repeat 4 Calculate pcur based on previous data 5 Calculate scoring probability based on the formula.3 6 Update players’ score/game/set based on tennis rule 7 Record nwin of game/set/match 8 until one side wins the match; 9 end 10 win_p[i] ←nwin/n 11 end 12 13 end

<!-- b000253 | prose | pages [9] -->
We use the above algorithm to perform N = 1000 simulations of the remaining fixtures after each ball and determine the final outcome of that game. If the number of wins of player K(K = A, B) in the result is n, then we say that the winning rate of player K after that ball is n N × 100%.

<!-- b000254 | prose | pages [9] -->
The graph below illustrates the real-time fluctuations in match-winning probabilities, sim- ulated through the Monte Carlo algorithm, for Djokovic (highlighted in red) and Alcarez (highlighted in green) during the 2023 Wimbledon final.

<!-- b000255 | caption | pages [9] -->
Figure 5: Wimbledon Final Real-Time Predicted Win Probability Swings Chart. The thick gray

<!-- b000256 | prose | pages [9] -->
dashed lines represent set divisions, while the thin gray dashed lines represent game divisions.

<!-- b000257 | prose | pages [9, 10] -->
关注数学模型 It can be seen that the situation is very anxious, and the match winning probablity in the middle of the game fluctuates greatly throughout the match. The first set was easily won by Djokovic, but the second was tense . . . . . . This is consistent with the facts. Thus, the reliability of the algorithm is verified. 微信公众号：数学模型

<!-- b000258 | furniture | pages [9] -->
2

<!-- b000259 | furniture | pages [9] -->
MATHmodels

<!-- b000260 | furniture | pages [9] -->
获取更多资讯

<!-- b000261 | furniture | pages [10] -->
Team # 2425454

<!-- b000262 | furniture | pages [10] -->
Page 10 of 25

<!-- b000264 | heading | pages [10] -->
5.2.3 Leveraging Every Point with Counterfactual Framework

<!-- b000265 | prose | pages [10] -->
Next, we will employ a counterfactual framework[4] to delve into the analysis of the impact of each point in a tennis match. By defining ’leverage’ as a measure of the magnitude of change in winning probability resulting from winning or losing a particular point, we will quantify the potential influence of each point on the outcome of each game/set, and even the entire match.

<!-- b000266 | prose | pages [10] -->
The following example shows the exact steps of our leverage quantisation process.

<!-- b000267 | prose | pages [10] -->
• Current Scenario: Player A is down 0-15 in the current game, his real-time winning probablity (abbreviated as RTWP in the latter.) is 69%.

<!-- b000268 | prose | pages [10] -->
• Define Realistic Scenario: If player A wins this point, the score becomes 30-30 and his 微信号：MATHmodels RTWP becomes 71%.

<!-- b000269 | prose | pages [10] -->
• Imagine the Opposite Scenario: if player A loses this point, the score becomes 15-40 and his RTWP becomes 65%.

<!-- b000270 | prose | pages [10] -->
• Calculating Leverage: By comparing the change in A’s RTWP in these two scenarios, the Leverage for this point is calculated to be 6%.

<!-- b000271 | prose | pages [10] -->
Note: The above data is fictional. The above process is shown schematically below:

<!-- b000272 | caption | pages [10] -->
Figure 6: Leveraged Quantitative Schematic

<!-- b000273 | prose | pages [10] -->
We set Li to represent the leverage of the ith point. The positive or negative sign does not indicate the magnitude but only signifies which player gained the point. Throughout the subsequent analysis, we consistently calculate the leverage with respect to Player A. If Li > 0, it means that player A won the ith point; if Li < 0, it means that player B won the ith point; if Li = 0, it means that the ith point did not result in a change in winning percentage.

<!-- b000274 | prose | pages [10] -->
If playerK wins the ith point, the playerK is called to have gained leverage, and vice versa, the player is called to have lost leverage. The leverage gained is treated as a separate variable and denoted by the symbol G. To wit:

<!-- b000275 | prose | pages [10] -->
( ( Li ⩾0 Li ⩽0 Li, Li, GA Li < 0 , GB i = i = 0, 0, Li > 0

<!-- b000276 | prose | pages [10] -->
关注数学模型

<!-- b000277 | furniture | pages [10] -->
2

<!-- b000278 | furniture | pages [10] -->
MATHmodels

<!-- b000279 | furniture | pages [10] -->
获取更多资讯

<!-- b000280 | furniture | pages [11] -->
Team # 2425454

<!-- b000281 | furniture | pages [11] -->
Page 11 of 25

<!-- b000282 | heading | pages [11] -->
5.2.4 Defining Momentum

<!-- b000283 | prose | pages [11] -->
We define momentum(M) as an exponentially weighted moving average of the leverage gained by a player[5].

<!-- b000284 | prose | pages [11] -->
微信公众号：数学模型 = GK i + (1 −α)GK i−1 + (1 −α)2GK i−2 + · · · + (1 −α)iGK 0 M K , 1 + (1 −α) + (1 −α)2 + · · · + (1 −α)t i

<!-- b000285 | prose | pages [11] -->
where [G0, G1, . . . , Gi] is the leverage of i recent points, and the points are listed in chronological order.α is the smoothing coefficient ,and α ∈(0, 1). Due to the fact that the impact of previous goals diminishes on the player’s current impact as the game progresses, the importance of a certain points decreases exponentially as the game progresses, The leverage of the most recent goal has the greatest impact on momentum, and the sooner the point is scored, the less it impact on momentum.

<!-- b000286 | prose | pages [11] -->
Finally, by focusing on the fluctuations in momentum, we can capture "the flow of play".

<!-- b000287 | heading | pages [11] -->
5.3 Visualization of the Flow of Play

<!-- b000288 | prose | pages [11] -->
微信号：MATHmodels Utilizing our model, we have described the match flow of the Wimbledon Final in 2023. The parameter α is set to 0.33, by testing the leverage defined by the handicap winning percentage, it better reflects the fluctuation of the game. The visualization is presented as follows:

<!-- b000289 | caption | pages [11] -->
Figure 7: The Visualization of Match Flow. The thick gray dashed lines represent set divisions,

<!-- b000290 | prose | pages [11] -->
while the thin gray dashed lines represent game divisions.The same applies to the subsequent figure.

<!-- b000291 | prose | pages [11] -->
Our results perfectly describe the flow of the match. We can correlate the fluctuations in momentum in the graph with the remarkable moments in the game:

<!-- b000292 | prose | pages [11] -->
Riding a dominating momentum after crushing the opponent in the first set, Djokovic had the opportunity to claim the second set. However, Alcaraz overcame the initial struggle and secured a crucial break in the second set, leading 2-1; Djokovic swiftly responded with a break of his own, but Alcaraz seized the opportunity in a tense tiebreak, winning the set with a brilliant backhand winner. In the third set, Djokovic struggled with a low momentum, while Alcaraz continued his high momentum, leading 2-1. In the fourth set, Djokovic broke Alcaraz twice, leveling the match.

<!-- b000293 | prose | pages [11] -->
Then, in the decisive fifth set, Djokovic missed a golden opportunity while leading, allowing Alcaraz to break and take a 2-1 lead. With Djokovic’s momentum dropping, he once again violated rules by smashing his racket against the net post, subsequently trailing 3-1. Alcaraz remained resolute, maintaining his high momentum. When Djokovic hit a forehand into the net, Alcaraz secured his extraordinary victory at 3-1."

<!-- b000294 | prose | pages [11, 12] -->
关注数学模型 It can be found that the momentum we define shows the race flow well.

<!-- b000295 | furniture | pages [11] -->
2

<!-- b000296 | furniture | pages [11] -->
MATHmodels

<!-- b000297 | furniture | pages [11] -->
获取更多资讯

<!-- b000298 | furniture | pages [12] -->
Team # 2425454

<!-- b000299 | furniture | pages [12] -->
Page 12 of 25

<!-- b000301 | prose | pages [12] -->
6 Task 2 : Whether the Swings of Play and Momentum are correlated 微信公众号：数学模型 A tennis coach argues that swings in play and runs of success in a match are random and not related to momentum. In response to this view, we plan to determine whether the distribution of scores in a match is completely random by means of a Runs Test.

<!-- b000302 | heading | pages [12] -->
6.1 Run Test for Assessing Randomness in Match Scores Sequence

<!-- b000303 | prose | pages [12] -->
The runs test is commonly employed to examine whether a binary sample with two potential outcomes, such as X and Y, originates from a binomial distribution.

<!-- b000304 | prose | pages [12] -->
In the runs test, a sample is drawn from a population containing X and Y, assuming n X’s and m Y’s are drawn. Subsequently, X and Y are arranged in order of sampling to form a sequence. In this sequence, consecutive occurrences of X or Y are referred to as a run. The total number of runs is denoted as the run count r. 微信号：MATHmodels

<!-- b000305 | caption | pages [12] -->
Figure 8: Runs Example Chart

<!-- b000306 | prose | pages [12] -->
In the XY sequence shown in Figure 8, there are n = 4 runs of X and m = 4 runs of Y, with a total of r = 8 runs.

<!-- b000307 | prose | pages [12] -->
• The null hypothesis H0: The arrangement of X and Y is random, with the probability of drawing X each time as P, and the probability of drawing Y as 1P.

<!-- b000308 | prose | pages [12] -->
• The alternative hypothesis H1: The arrangement of X and Y is non-random, indicating no regularity in the probability of drawing X or Y.

<!-- b000309 | prose | pages [12] -->
If H0 holds, based on the parity of r, there are different scenarios:

<!-- b000310 | prose | pages [12] -->
 n −1   m−1  2 k −1 k −1  n + m P(r = 2k) = ;  n  m −1  m −1  n −1   n −1    + + k −1 k −1 k k  n + m P(r = 2k + 1) =  n

<!-- b000311 | prose | pages [12] -->
The mathematical expectation of r is E(r) = 2mn m + n + 1, the variance of r is V (r) =

<!-- b000312 | prose | pages [12, 13] -->
关注数学模型 2mn(2mn −m −n) , and the statisticZ constructed from the number of trips follows a normal (m + n)2(m + n −1) distribution, that is, Z = r −E(r) ∼N(0, 1). p V (R) 微信公众号：数学模型 We recorded the outcome of each point within each game throughout the entire match. If player A won the point, it was recorded as 1, and 0 otherwise. This resulted in sequences representing the distribution of scores within each game, and runs were calculated based on this. Subsequently, a runs test was conducted for each game. The results indicated that within a 90% confidence interval, the percentage of games rejecting the null hypothesis accounted for 45.11% of the total number of games.

<!-- b000313 | furniture | pages [12] -->
2

<!-- b000314 | furniture | pages [12] -->
MATHmodels

<!-- b000315 | furniture | pages [12] -->
获取更多资讯

<!-- b000316 | furniture | pages [13] -->
Team # 2425454

<!-- b000317 | furniture | pages [13] -->
Page 13 of 25

<!-- b000319 | prose | pages [13] -->
This suggests that scoring in a game is not completely randomized.

<!-- b000320 | heading | pages [13] -->
6.2 Scores-Momentum Contingency Analysis

<!-- b000321 | prose | pages [13] -->
"In the previous section, we employed the runs test to investigate whether the scoring sequence of opposing sides in tennis matches exhibits randomness. The result was negative, 微信号：MATHmodels indicating that the match dynamics are not random. Subsequently, to explore whether the fluctuations in the game are related to momentum, we conducted a contingency table analysis on the relationship between the score of each point and the momentum of the opposing sides.

<!-- b000322 | prose | pages [13] -->
We first counted the winners and losers of each point as well as the relationship between the momentum of playerA and playerB in terms of magnitude when competing for this point, as shown in the table below:

<!-- b000323 | caption | pages [13] -->
Table 2: Score vs. Momentum Table

<!-- b000324 | prose | pages [13] -->
Player A Won the Point Player B Won the Point MA ⩾MB n11 n12 MA < MB n21 n22

<!-- b000325 | prose | pages [13] -->
In the table, nijrepresents the frequency with which events in row i and column j occur simultaneously, where i represents the comparison of player A’s momentum with player B’s momentum, and jrepresents the winner of the match point. Let the original hypothesis be H0, indicating that there is no correlation between score and momentum, and the alternative hypothesis be H1, indicating that there is a correlation between score and momentum.

<!-- b000326 | prose | pages [13] -->
Assuming that there is no correlation between score and momentum, for each cell in Table 1 calculate the expected frequency E.

<!-- b000327 | prose | pages [13] -->
Since the total sample with all expected frequencies is greater than 5, the conditions for using the chi-squaretest aremet. Therefore, weusedthechi-squaretest toassessthedifferencebetween the observed and expected frequencies. Taking Wimbledon as an example, the calculated chi- square statistic X = 5.566, indicating that the observed frequencies are significantly different from the expected frequencies; the significance level P = 0.018, indicating the rejection of the original hypothesis H0 at the 90% confidence level that the relationship between the winners and losers of each point and the magnitude of playerA’s and playerB’s momentum when competing for that point is correlated.

<!-- b000328 | prose | pages [13] -->
So "momentum" does play an important role in the game, and swings in play and runs of success are not random.

<!-- b000329 | prose | pages [13] -->
关注数学模型

<!-- b000330 | furniture | pages [13] -->
2

<!-- b000331 | furniture | pages [13] -->
MATHmodels

<!-- b000332 | furniture | pages [13] -->
获取更多资讯

<!-- b000333 | furniture | pages [14] -->
Team # 2425454

<!-- b000334 | furniture | pages [14] -->
Page 14 of 25

<!-- b000335 | heading | pages [14] -->
7 Task 3 : Identify Indicators Signaling a Change in Flow

<!-- b000336 | heading | pages [14] -->
7.1 GSRF Swing Predictor Model

<!-- b000337 | prose | pages [14] -->
First, we need to develop a model to predict swings in a match and look for the factors most 微信公众号：数学模型 associated with swings.So we developed the GSRF Swing Predictor Model.

<!-- b000338 | prose | pages [14] -->
Our model needs to be able to predict whether there will be swings at s points in the future, and determine its direction accurately - whether it will be a wave in favor of the player or a swing in favor of his opponent. To do this, we first introduce the concept of ’swing reversal points’, which have two different types.

<!-- b000339 | heading | pages [14] -->
7.1.1 The Swings Reversal Point

<!-- b000340 | prose | pages [14] -->
We use the ‘scipy.signal.find_peaks‘ function in Python to locate the peaks in the curves representing the momentum changes over time for both the player and the opponent. Between the peaks of the player and opponent, we identify the point where the momentum value is closest to 0 as the "swing" reversal point.

<!-- b000341 | prose | pages [14] -->
微信号：MATHmodels If the peak of the opponent comes before the player’s peak, indicating the advantage is leaning towards the player, the reversal point between these two peaks is marked as a transition point favoring the player, labeled as "1". Conversely, if the player’s peak comes before the opponent’s peak, indicating the advantage is shifting towards the opponent, the point between these two peaks is marked as a reversal point favoring the opponent, labeled as "-1". Points that are not transition points are labeled as "0". The schematic representation of this process is illustrated in Figure 9.

<!-- b000342 | caption | pages [14] -->
Figure 9: Rurning Swing Points Selection Process and Schematic Diagram

<!-- b000343 | prose | pages [14] -->
We verified the method using the 2023 Wimbledon final data, and the results are good, as shown in the figure below:

<!-- b000344 | prose | pages [14, 15] -->
关注数学模型 微信公众号：数学模型

<!-- b000345 | furniture | pages [14] -->
2

<!-- b000346 | furniture | pages [14] -->
MATHmodels

<!-- b000347 | furniture | pages [14] -->
获取更多资讯

<!-- b000348 | furniture | pages [15] -->
Team # 2425454

<!-- b000349 | furniture | pages [15] -->
Page 15 of 25

<!-- b000351 | caption | pages [15] -->
Figure 10: GSRF Algorithm Flow Diagram

<!-- b000352 | prose | pages [15] -->
To predict swings in future matches, we take a subset of players’ on-court performance metrics and use the grid search Random Forest (GSRF)[6] algorithm to predict which of three scenarios each point in future belongs to.

<!-- b000353 | prose | pages [15] -->
Next, we will describe the selected indicator data and explain the algorithm flow.

<!-- b000354 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000355 | heading | pages [15] -->
7.1.2 The Selected Indicator

<!-- b000356 | prose | pages [15] -->
Through the given tennis dataset, we have selected two categories of indicators for prediction. One category pertains to individual player metrics, while the other involves shared metrics when the two players compete. These two categories of indicators are listed as follows:

<!-- b000357 | prose | pages [15] -->
The first category: p1_ace: Whether player 1 hits an "unreturnable" ball during the serve; p1_ace: p1 total aces; p1_break_pt: Break point: player 1 has the opportunity to win a point in opponent’s service game; p1_double_fault: Player 1 committed two faults in serving, resulting in a lost point; p1_double_fault: p1 total double faults; p1_net_pt: Player 1 approached the net in this round; p1_net_pt_won: Player 1 won the point when approaching the net in this round; p1_score: Player 1’s score in this game; p1_sets: Number of sets won by player 1; p1_unf_err: Player 1 made an unforced error in this round; p1_winner: Whether player 1 hit an "unreturnable" ball,p1_games: p1 won games; p1_points_won: p1 total points won; p1_distance_run: p1 distance run in this point; brp1: p1 break point conversion rate; p1_distance_run_total: p1 total distance run; ntp1: p1 net points won percentage.

<!-- b000358 | prose | pages [15] -->
Player 2 has exactly the same indicator type as Player 1, so it is not repeated.

<!-- b000359 | prose | pages [15] -->
The second category: elapsed_time: Duration of the point ; speed_mph: Serve speed ; rally_count: Cumulative number of hits ; rally_count: Total hits in a rally ; return_depth: Depth of returning, indicating whether the return lands near the baseline, midcourt, or frontcourt ; serve_depth: Depth of the serve, indicating whether the serve is placed in the front, mid, or backcourt of the tennis court ; serve_no: Which serve the player is in, the first or second ; serve_width: Direction of the serve ; server: Player serving.

<!-- b000360 | prose | pages [15] -->
Some of the indicators are original metrics from the dataset, while others (in bold) are derived through calculations based on the original metrics.

<!-- b000361 | heading | pages [15] -->
7.1.3 GSRF Algorithm

<!-- b000362 | prose | pages [15] -->
The GSRF algorithm consists of the Random Forest and Grid Search algorithm.

<!-- b000363 | prose | pages [15] -->
The Grid Search algorithm is a parameter optimization technique that iterates through a specified parameter grid. It trains and evaluates the model for each possible combination

<!-- b000364 | prose | pages [15, 16] -->
关注数学模型 of parameters, ultimately outputting the best parameter set along with corresponding model performance metrics.

<!-- b000365 | furniture | pages [15] -->
2

<!-- b000366 | furniture | pages [15] -->
MATHmodels

<!-- b000367 | furniture | pages [15] -->
获取更多资讯

<!-- b000368 | furniture | pages [16] -->
Team # 2425454

<!-- b000369 | furniture | pages [16] -->
Page 16 of 25

<!-- b000371 | prose | pages [16] -->
Random Forest, is a machine learning algorithm that trains based on multiple decision trees. During training, it randomly selects a subset of features for each tree. In the classification 微信公众号：数学模型 process, Random Forest aggregates the predicted classification results of each decision tree through averaging or voting, yielding the final result.

<!-- b000372 | prose | pages [16] -->
Unlike the regular Random Forest algorithm, the GSRF algorithm utilizes the best hy- perparameter combinations to train and predict the Random Forest model. This significantly enhances the model’s performance, mitigating issues such as overfitting or underfitting. The GSRF algorithm workflow is illustrated in Figure 11.

<!-- b000373 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000374 | caption | pages [16] -->
Figure 11: GSRF Algorithm Flow Diagram

<!-- b000375 | heading | pages [16] -->
7.1.4 The Predicted Swings Results of the Match

<!-- b000376 | prose | pages [16] -->
We utilize the aforementioned classification indicators as input parameters for the Random Forest model to predict future scenarios.

<!-- b000377 | prose | pages [16] -->
As an example, for a particular match, we split the dataset into training and testing sets in an 8:2 ratio. We employed the RandomForestRegressor algorithm from the ensemble module in the scikit-learn (sklearn) machine learning library, along with the GridSearchCV algorithm from sklearn. The optimal hyperparameter combination obtained from GridSearchCV is as follows:

<!-- b000378 | caption | pages [16] -->
Table 3: Table of Optimal Hyperparameter Combinations

<!-- b000379 | prose | pages [16] -->
Indicator Names max_depth min_samples_leaf min_samples_split n_estimators

<!-- b000380 | prose | pages [16] -->
Values None 1 3 100

<!-- b000381 | prose | pages [16] -->
The prediction accuracy of the model is up to 94%, and the performance of the test set is also good. The confusion matrix diagram is drawn as follows:

<!-- b000382 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型

<!-- b000383 | furniture | pages [16] -->
2

<!-- b000384 | furniture | pages [16] -->
MATHmodels

<!-- b000385 | furniture | pages [16] -->
获取更多资讯

<!-- b000386 | furniture | pages [17] -->
Team # 2425454

<!-- b000387 | furniture | pages [17] -->
Page 17 of 25

<!-- b000389 | caption | pages [17] -->
Figure 12: Confusion Matrix

<!-- b000390 | prose | pages [17] -->
微信号：MATHmodels As can be seen from the matrix, most of the samples were correctly categorized, only 3 samples were not correctly categorized, and none of the samples from any of the reversal point types were categorized into another reversal point type.

<!-- b000391 | prose | pages [17] -->
From the random forest, we can also obtain the importance of various metrics, as shown in the following figure:

<!-- b000392 | caption | pages [17] -->
Figure 13: Bar Chart of Metric Importance

<!-- b000393 | prose | pages [17] -->
As seen in the graph above, the total score of opponents is the most relevant metric for swings in the match.

<!-- b000394 | heading | pages [17] -->
7.2 Player Performance Factor Analysis Model

<!-- b000395 | prose | pages [17] -->
The influencing factors obtained from the analysis of the GSRF Swing Predictor Model established in the previous section, which predicts the direction of the game, are complex and diverse. This complexity makes it less convenient for coaches to guide players and understand the momentum of the game. Therefore, we conducted a factor analysis[7] on the indicators that have a significant impact on "swing" to extract independent common factors, enabling players to clearly capture the factors influencing the direction of the game.

<!-- b000396 | prose | pages [17, 18] -->
关注数学模型 We selected the top 15 indicators in terms of feature importance and conducted the Kaiser- Meyer-Olkin (KMO) test and Bartlett’s test[8] using SPSS.The test results are as follows:

<!-- b000397 | furniture | pages [17] -->
2

<!-- b000398 | furniture | pages [17] -->
MATHmodels

<!-- b000399 | furniture | pages [17] -->
获取更多资讯

<!-- b000400 | furniture | pages [18] -->
Team # 2425454

<!-- b000401 | furniture | pages [18] -->
Page 18 of 25

<!-- b000403 | caption | pages [18] -->
Table 4: Kaiser-Meyer-Olkin (KMO) and Bartlett’s Test

<!-- b000404 | prose | pages [18] -->
微信公众号：数学模型 KMO Sampling Adequacy Measure 0.708

<!-- b000405 | prose | pages [18] -->
Approximate Chi-Square 11512.67 Bartlett’s Sphericity Test Degrees of Freedom 105 Significance 0

<!-- b000406 | prose | pages [18] -->
According to the table, the statistic for Bartlett’s sphericity test is 11512.67, and the cor- responding probability (P-value) is 0. At a 95% significance level, the null hypothesis should be rejected, indicating a significant difference between the correlation matrix and the identity matrix. Meanwhile, the KMO value is 0.708. According to Kaiser’s standard for interpreting KMO, it suggests suitability for factor analysis, indicating factors that influence swing[9].

<!-- b000407 | prose | pages [18] -->
微信号：MATHmodels Next, we utilized SPSS and conducted a principal component analysis for extraction. The scree plot obtained is shown in Figure 14. It was observed that when the number of extractions reached 4, the contribution rate became quite small. Therefore, we decided to extract 4 common factors.

<!-- b000408 | caption | pages [18] -->
Figure 14: Scree plot of Principal Component Analysis

<!-- b000409 | prose | pages [18] -->
We utilized the Kaiser normalization and varimax rotation method to obtain the rotated component matrix, as shown below:

<!-- b000410 | prose | pages [18, 19] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels Next, we analyze the four factors in the component matrix.

<!-- b000411 | furniture | pages [18] -->
2

<!-- b000412 | furniture | pages [18] -->
MATHmodels

<!-- b000413 | furniture | pages [18] -->
获取更多资讯

<!-- b000414 | furniture | pages [19] -->
Team # 2425454

<!-- b000415 | furniture | pages [19] -->
Page 19 of 25

<!-- b000416 | caption | pages [19] -->
Table 5: The Rotated Component Matrix

<!-- b000418 | prose | pages [19] -->
Factor 1 loadsheavilyonp1_pointswon, p2_pointswon, rally_count, p1_distanceruntotal, and p2_distance_run_total. It involves aspects such as shot count and running distance, rep- resenting the player’s stamina and energy expenditure during the match. We name this factor the Expenditure Factor.

<!-- b000419 | prose | pages [19] -->
Factor 2 primarily involves break point conversion rates (brp1, brp2) and net point conversion rates (ntp1, ntp2). As it can reflect the player’s technical proficiency during the match, we name it the Technical Factor.

<!-- b000420 | prose | pages [19] -->
Factor 3 loads significantly on p1_distancerun and p2_distance_run, primarily reflecting the players’ running patterns during the match, likely related to court coverage and movement tactics. We name it the Running Distance Factor.

<!-- b000421 | prose | pages [19] -->
Factor 4 loads heavily on p1_games and p2_games, mainly focusing on the players’ game situations during the match. We name it the Game Situation Factor.

<!-- b000422 | prose | pages [19] -->
The coach can provide guidance to the players by comparing the abilities of their players with those of the next opponent in these four factors.

<!-- b000423 | prose | pages [19] -->
Utilizing the Expenditure Factor, the coach can analyze the stamina gap between players and opponents, enabling targeted training for the players’ fitness levels and endurance before the match. The Technical Factor reflects a player’s technical proficiency, including break points and volleys, aiding the coach in devising more effective strategies. For instance, if a player excels

<!-- b000424 | prose | pages [19, 20] -->
关注数学模型 in volleys, encouraging them to employ net strategies more frequently could be beneficial. The Running Distance Factor is associated with court coverage and movement tactics. Coaches can optimize players’ running strategies based on these factors to enhance control over opponents and reduce self-pressure. The Game Situation Factor primarily focuses on players’ game 微信公众号：数学模型 scores, assisting in analyzing situations and guiding players to flexibly adjust strategies during matches.

<!-- b000425 | furniture | pages [19] -->
2

<!-- b000426 | furniture | pages [19] -->
MATHmodels

<!-- b000427 | furniture | pages [19] -->
获取更多资讯

<!-- b000428 | furniture | pages [20] -->
Team # 2425454

<!-- b000429 | furniture | pages [20] -->
Page 20 of 25

<!-- b000431 | prose | pages [20] -->
In essence, strengthening mental and physical resilience is crucial against diverse opponents, and focusing on improving break points and volley techniques gives players a substantial edge.

<!-- b000432 | heading | pages [20] -->
8 Task 4 : Assess the Generalization of Model

<!-- b000433 | heading | pages [20] -->
8.1 Generalization in women’s tennis matches

<!-- b000434 | prose | pages [20] -->
To assess the generalization of our model, we tested it in the 2023 Wimbledon Women’s Singles final. The test results are as follows:

<!-- b000435 | prose | pages [20] -->
We obtained data on the 2023 Wimbledon women’s singles final that is consistent across all 微信号：MATHmodels metrics with the dataset given in this question(source:https://www.wimbledon.com/index.html). Women’s tennis differs from men’s tennis matches in that two out of three sets are taken. Therefore, we modified the rules related to the relevant sets for Monte Carlo simulation to solve the real-time winning probability of the match. The calculated momentum for the whole match is shown below:

<!-- b000436 | caption | pages [20] -->
Figure 15: Wimbledon Final Real-Time Predicted Win Probability Swings Chart.The thick gray

<!-- b000437 | prose | pages [20] -->
dashed lines represent set divisions, while the thin gray dashed lines represent game divisions.

<!-- b000438 | prose | pages [20] -->
For Marketa Vondronsova, the match was a windfall.

<!-- b000439 | prose | pages [20] -->
Using the model from Task 3 again, the momentum fluctuations for this match are illustrated in the following graph:

<!-- b000440 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型

<!-- b000441 | furniture | pages [20] -->
2

<!-- b000442 | furniture | pages [20] -->
MATHmodels

<!-- b000443 | furniture | pages [20] -->
获取更多资讯

<!-- b000444 | furniture | pages [21] -->
Team # 2425454

<!-- b000445 | furniture | pages [21] -->
Page 21 of 25

<!-- b000447 | caption | pages [21] -->
Figure 16: Momentum Fluctuations and Transition Points in Fluctuations.

<!-- b000448 | prose | pages [21] -->
Similarly, the prediction of short-term NME transition points has the following results on the test set.

<!-- b000449 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000450 | caption | pages [21] -->
Figure 17: Women’s Singles Confusion Matrix

<!-- b000451 | prose | pages [21] -->
It is not difficult to find that there are fewer samples with wrong scores, indicating that the application of our model to women’s tennis matches is feasible. And the important indexes obtained by GSRF model for women’s tennis game appeared a little difference with men’s tennis game. For example, the most important factor affecting the women’s tennis game is the total distance run (as shown in Fig. 18), while the men are the total score of the opponent, which may be related to the difference in physical strength between men and women.

<!-- b000452 | caption | pages [21] -->
Figure 18: GSRF Algorithm Flow Diagram

<!-- b000453 | prose | pages [21, 22] -->
关注数学模型 8.2 Discussion on the impact of the playing surface.

<!-- b000454 | furniture | pages [21] -->
2

<!-- b000455 | furniture | pages [21] -->
MATHmodels

<!-- b000456 | furniture | pages [21] -->
获取更多资讯

<!-- b000457 | furniture | pages [22] -->
Team # 2425454

<!-- b000458 | furniture | pages [22] -->
Page 22 of 25

<!-- b000460 | prose | pages [22] -->
Research[10] indicates that, with a consistent return speed of 100 km/h and a landing angle of 30◦, on grass, the rebound angle is approximately 36◦at a speed of about 73 km/h; on hard courts, it’s around 41◦at a speed of about 67 km/h; while on clay courts, the rebound angle is 微信公众号：数学模型 about 44◦at a speed of about 57 km/h. Different launch angles and rebound heights are also observed.

<!-- b000461 | prose | pages [22] -->
In summary, playing surface types significantly impact the game. Athletes need to adapt their techniques and physical fitness to the surface characteristics for better performance. Studying momentum variations on different surfaces is essential.

<!-- b000462 | prose | pages [22] -->
While we believe our model is applicable across surfaces, unfortunately, we couldn’t find match data for various surfaces in the limited time, which will be part of our future work.

<!-- b000463 | heading | pages [22] -->
9 Sensitivity Analysis

<!-- b000464 | prose | pages [22] -->
Short-term Motivation Parameter mi 微信号：MATHmodels The short-term motivation parameter mi was estimated by us from the dataset with some bias. We perturbed mi, (±5%, ±10%), and the calculated changes in the Wimbledon final winning percentage and momentum calculations are shown in the results in the following figure:

<!-- b000465 | caption | pages [22] -->
Figure 19: The Momentum Variation with respect to mi Graph

<!-- b000466 | caption | pages [22] -->
Figure 20: Score Quantity Sensitivity Analysis

<!-- b000467 | prose | pages [22] -->
From the above figure, it can be observed that the win rate and momentum are not sensitive to the variations in mi and remain relatively stable. From the above figure, it can be observed that the win rate and momentum are not sensitive to the variations in mi and remain relatively stable.

<!-- b000468 | prose | pages [22] -->
关注数学模型

<!-- b000469 | furniture | pages [22] -->
2

<!-- b000470 | furniture | pages [22] -->
MATHmodels

<!-- b000471 | furniture | pages [22] -->
获取更多资讯

<!-- b000472 | furniture | pages [23] -->
Team # 2425454

<!-- b000473 | furniture | pages [23] -->
Page 23 of 25

<!-- b000474 | heading | pages [23] -->
Parameters in the GSRF model: Score quantity s

<!-- b000475 | prose | pages [23] -->
In the GSRF model, the parameter is the given score quantity s, and sensitivity analysis is required. By varying the score quantity from 1 to 10, we found that the accuracy remains above 85%. We selected the top five stable indicators in terms of feature importance and plotted the 微信公众号：数学模型 changes in their feature importance. The figure below illustrates the sensitivity to s.

<!-- b000476 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000477 | caption | pages [23] -->
Figure 21: The Win Rate as a Function of mi Graph

<!-- b000478 | prose | pages [23] -->
From the figure, it can be observed that within a short-term (i.e., not too long a score quantity), the changes in feature importance are not sensitive, indicating the robustness of the GSRF model.

<!-- b000479 | heading | pages [23] -->
10 Strength and Weakness

<!-- b000480 | heading | pages [23] -->
10.1 Strength

<!-- b000481 | prose | pages [23] -->
• For different sports, design rules for calculating win rates, incorporating key indicators to enhance the model’s applicability.

<!-- b000482 | prose | pages [23] -->
• The GSRF model demonstrates a high accuracy rate of 94% in predicting match fluctua- tions, with very few misclassified samples.

<!-- b000483 | heading | pages [23] -->
10.2 Weakness

<!-- b000484 | prose | pages [23] -->
• There hasn’t been an attempt to employ machine learning models to measure the magni- tude of changes in winning probability based on whether a match is won or lost.

<!-- b000485 | heading | pages [23] -->
11 Further Discussion

<!-- b000486 | prose | pages [23] -->
• For different sports, design rules for calculating win rates, incorporating key indicators to enhance the model’s applicability.

<!-- b000487 | prose | pages [23] -->
• Utilize the GSRF model to predict match fluctuations and the significance of indicators, providing athletes with more detailed performance improvement strategies.

<!-- b000488 | prose | pages [23, 24] -->
关注数学模型 微信公众号：数学模型 To:Tennis Team From:Team#2425454 Date : February 5 Dear Coach, It is my honor to present our research findings to you. In this study, we first explored the relationship between "momentum" and changes in the game situation. We then further developed models capable of predicting fluctuations in the game situation and identified key factors influencing match outcomes. Momentum refers to the psychological advantage a player gains by consecutively winning points or 微信号：MATHmodels matches. It provides players with a sense of control in the game, exerting pressure on opponents and increasing their likelihood of making mistakes. When players have momentum, they play more dynamically, reducing fear and inhibition, leading to a more aggressive and confident playing style. Next, let me explain how to use momentum to win more tennis matches and how to prepare players to cope with events that influence the course of tennis matches.

<!-- b000489 | furniture | pages [23] -->
2

<!-- b000490 | furniture | pages [23] -->
MATHmodels

<!-- b000491 | furniture | pages [23] -->
获取更多资讯

<!-- b000493 | prose | pages [24] -->
Taking Control from the Start The first and arguably most crucial step in gaining momentum in tennis is to have a strong start. The initial points of a match are pivotal, setting the tone for the rest of the game.

<!-- b000494 | prose | pages [24] -->
Winning the early points instills confidence and control, putting pressure on your opponent.

<!-- b000495 | prose | pages [24] -->
Focus on Your Footwork Footwork is another essential aspect of gaining momentum in tennis. Your movement on the court can have a significant impact on your ability to control the game.

<!-- b000496 | prose | pages [24] -->
Command the Net Controlling the net is a key strategy in establishing momentum in tennis. This involves approaching the net and executing volleys and overhead shots. Being at the net forces your opponent to make powerful shots and quick decisions.

<!-- b000497 | prose | pages [24] -->
Remember, momentum is fleeting and can shift in an instant. Maintaining mental resilience ensures you can seize it when it works in your favor and reclaim it when it doesn't.

<!-- b000498 | prose | pages [24] -->
Mastering the art of momentum in tennis can give you a significant advantage over your opponents, leading to more victories and ultimately elevating your level of play.

<!-- b000499 | prose | pages [24] -->
Thank you for reading, as the same love tennis people, we sincerely admire the dedication and efforts of tennis players. We hope that our models and recommendations will have a positive impact on your training and competition, and help you achieve better results.

<!-- b000500 | prose | pages [24] -->
If you have any more questions, feel free to email us and we'll be happy to discuss them with you. Look forward to seeing your team achieve more victories in future competitions!

<!-- b000501 | prose | pages [24] -->
Yours Sincerely, 关注数学模型

<!-- b000502 | furniture | pages [24] -->
2

<!-- b000503 | furniture | pages [24] -->
Team #2425454

<!-- b000504 | furniture | pages [24] -->
MATHmodels

<!-- b000505 | furniture | pages [24] -->
获取更多资讯

<!-- b000506 | furniture | pages [25] -->
Team # 2425454

<!-- b000507 | furniture | pages [25] -->
Page 25 of 25

<!-- b000508 | heading | pages [25] -->
References

<!-- b000509 | references | pages [25] -->
[1]

<!-- b000510 | references | pages [25] -->
Agnieszka M Madurska. “A set-by-set analysis method for predicting the outcome of

<!-- b000511 | references | pages [25] -->
professional singles tennis matches”. In: Imperial College London, Department of Com-

<!-- b000512 | references | pages [25] -->
微信公众号：数学模型

<!-- b000513 | references | pages [25] -->
puting: London, UK (2012), pp. 1–98.

<!-- b000514 | references | pages [25] -->
[2]

<!-- b000515 | references | pages [25] -->
Ana Šarčević;Damir Pintar;Mihaela Vranić;Ante Gojsalić. “Modeling In-Match Sports

<!-- b000516 | references | pages [25] -->
DynamicsUsingtheEvolvingProbabilityMethod”. In: AppliedSciences (2021),pp.4429–

<!-- b000517 | references | pages [25] -->
4508.

<!-- b000518 | references | pages [25] -->
[3]

<!-- b000519 | references | pages [25] -->
Jan R Magnus and Franc JGM Klaassen. “On the advantage of serving first in a tennis

<!-- b000520 | references | pages [25] -->
set: four years at Wimbledon”. In: Journal of the Royal Statistical Society: Series D (The

<!-- b000521 | references | pages [25] -->
Statistician) 48.2 (1999), pp. 247–256.

<!-- b000522 | references | pages [25] -->
[4]

<!-- b000523 | references | pages [25] -->
Karl Christoph Klauer, Thomas Jacobsen, and Gerd Migulla. “Counterfactual process-

<!-- b000524 | references | pages [25] -->
ing: Test of an hierarchical correspondence model”. In: European Journal of Social

<!-- b000525 | references | pages [25] -->
Psychology 25.5 (1995), pp. 577–595.

<!-- b000526 | references | pages [25] -->
[5]

<!-- b000527 | references | pages [25] -->
Seidl Robert;Lucey Patrick. “Live Counter-Factual Analysis in Women’s Tennis using

<!-- b000528 | references | pages [25] -->
Automatic Key-Moment Detection”. In: MIT Sloan Sports Analytics Conference. (2022).

<!-- b000529 | references | pages [25] -->
微信号：MATHmodels

<!-- b000530 | references | pages [25] -->
[6]

<!-- b000531 | references | pages [25] -->
Brandon Giles, Stephanie Kovalchik, and Machar Reid. “A machine learning approach

<!-- b000532 | references | pages [25] -->
for automatic detection and classification of changes of direction from player tracking

<!-- b000533 | references | pages [25] -->
data in professional tennis”. In: Journal of sports sciences 38.1 (2020), pp. 106–113.

<!-- b000534 | references | pages [25] -->
Noora Shrestha. “Factor analysis as a tool for survey analysis”. In: American Journal of

<!-- b000535 | references | pages [25] -->
[7]

<!-- b000536 | references | pages [25] -->
Applied Mathematics and Statistics 9.1 (2021), pp. 4–11.

<!-- b000537 | references | pages [25] -->
[8]

<!-- b000538 | references | pages [25] -->
Zhanneta Kozina et al. “General and individual factor structure of complex preparation

<!-- b000539 | references | pages [25] -->
of young tennis players of 10-12 years”. In: Journal of Physical Education and Sport 20

<!-- b000540 | references | pages [25] -->
(2020), pp. 1242–1249.

<!-- b000541 | references | pages [25] -->
[9]

<!-- b000542 | references | pages [25] -->
Shabrina Tri Asti Nasution, Devi Ayu Putri, and Thezar Fiqih Hidayat Hasibuan. “AN

<!-- b000543 | references | pages [25] -->
ANALYSIS FACTOR THROUGH KAISER-MEYER-OLKIN: DISCLOSING AUDIT

<!-- b000544 | references | pages [25] -->
TENUREINBANKINGCOMPANIESLISTEDONINDONESIASTOCKEXCHANGE

<!-- b000545 | references | pages [25] -->
2019–2022”. In: Jurnal Ekonomi 12.01 (2023), pp. 1694–1700.

<!-- b000546 | references | pages [25] -->
Rod Cross. “Measurement of the speed and bounce of tennis courts”. In: Sports Technol-

<!-- b000547 | references | pages [25] -->
[10]

<!-- b000548 | references | pages [25] -->
ogy 3.2 (2010), pp. 112–120.

<!-- b000549 | references | pages [25] -->
关注数学模型

<!-- b000550 | furniture | pages [25] -->
2

<!-- b000551 | furniture | pages [25] -->
MATHmodels

<!-- b000552 | furniture | pages [25] -->
获取更多资讯

<!-- b000553 | heading | pages [26] -->
Report on Use of AI

<!-- b000554 | ai_disclosure | pages [26] -->
1. OpenAI ChatGPT(GPT 3.5 )

<!-- b000555 | ai_disclosure | pages [26] -->
Query1:<p1_games

<!-- b000556 | ai_disclosure | pages [26] -->
p1_points_won

<!-- b000557 | ai_disclosure | pages [26] -->
微信公众号：数学模型

<!-- b000558 | ai_disclosure | pages [26] -->
p1_distance_run

<!-- b000559 | ai_disclosure | pages [26] -->
brp1

<!-- b000560 | ai_disclosure | pages [26] -->
p1_distance_run

<!-- b000561 | ai_disclosure | pages [26] -->
ntp1

<!-- b000562 | ai_disclosure | pages [26] -->
p1_ace

<!-- b000563 | ai_disclosure | pages [26] -->
p1_ace

<!-- b000564 | ai_disclosure | pages [26] -->
p1_break_pt

<!-- b000565 | ai_disclosure | pages [26] -->
p1_double_fault

<!-- b000566 | ai_disclosure | pages [26] -->
p1_double_fault

<!-- b000567 | ai_disclosure | pages [26] -->
p1_net_pt

<!-- b000568 | ai_disclosure | pages [26] -->
p1_net_pt_won

<!-- b000569 | ai_disclosure | pages [26] -->
p1_score

<!-- b000570 | ai_disclosure | pages [26] -->
p1_sets

<!-- b000571 | ai_disclosure | pages [26] -->
p1_unf_err

<!-- b000572 | ai_disclosure | pages [26] -->
p1_winner

<!-- b000573 | ai_disclosure | pages [26] -->
微信号：MATHmodels

<!-- b000574 | ai_disclosure | pages [26] -->
Put this data together into a paragraph, these are the individual athlete indicators data. The first

<!-- b000575 | ai_disclosure | pages [26] -->
six of them are our own construction, meaning respectively: cumulative wins up to this point

<!-- b000576 | ai_disclosure | pages [26] -->
Cumulative total score up to this point

<!-- b000577 | ai_disclosure | pages [26] -->
The distance the point runs

<!-- b000578 | ai_disclosure | pages [26] -->
Service break rate

<!-- b000579 | ai_disclosure | pages [26] -->
Total distance run by the player up to that point

<!-- b000580 | ai_disclosure | pages [26] -->
Scoring rate near the net

<!-- b000581 | ai_disclosure | pages [26] -->
Please tidy it up for me>

<!-- b000582 | ai_disclosure | pages [26] -->
Output:<The following is a compilation of the individual metrics data you provided for

<!-- b000583 | ai_disclosure | pages [26] -->
athletes:

<!-- b000584 | ai_disclosure | pages [26] -->
p1_games: Cumulative wins up to this point

<!-- b000585 | ai_disclosure | pages [26] -->
p1_points_won: indicates the total score as of this point

<!-- b000586 | ai_disclosure | pages [26] -->
p1_distance_run: indicates the run distance of this point

<!-- b000587 | ai_disclosure | pages [26] -->
brp1: Break rate

<!-- b000588 | ai_disclosure | pages [26] -->
p1_distance_run: The total distance run by the player up to this point

<!-- b000589 | ai_disclosure | pages [26] -->
ntp1: near net scoring rate

<!-- b000590 | ai_disclosure | pages [26] -->
p1_ace: indicates the total number of ACES

<!-- b000591 | ai_disclosure | pages [26] -->
p1_break_pt: Total break points

<!-- b000592 | ai_disclosure | pages [26] -->
p1_double_fault: indicates the total number of double errors

<!-- b000593 | ai_disclosure | pages [26] -->
p1_net_pt: indicates the total number of online accesses

<!-- b000594 | ai_disclosure | pages [26] -->
p1_net_pt_won: indicates the total number of Internet access scores

<!-- b000595 | ai_disclosure | pages [26] -->
p1_score: indicates the total score

<!-- b000596 | ai_disclosure | pages [26] -->
p1_sets: indicates the total number of disks

<!-- b000597 | ai_disclosure | pages [26] -->
p1_unf_err: Total number of unforced errors

<!-- b000598 | ai_disclosure | pages [26] -->
p1_winner: Total number of winning points

<!-- b000599 | ai_disclosure | pages [26] -->
Note that "p1_distance_run" appears twice, if this is an error, please provide the correct variable

<!-- b000600 | ai_disclosure | pages [26] -->
name.>

<!-- b000601 | ai_disclosure | pages [26] -->
2. OpenAI ChatGPT(GPT 3.5.)

<!-- b000602 | ai_disclosure | pages [26] -->
Query1:<Please provide me with suggestions for modification>

<!-- b000603 | ai_disclosure | pages [26] -->
Output:<I changed "p1_distance_run" to "p_distance_run_total" to distinguish it from

<!-- b000604 | ai_disclosure | pages [26] -->
"p_distance_run". If this is still a problem, provide the correct variable name.>

<!-- b000605 | ai_disclosure | pages [26] -->
3. OpenAI ChatGPT(GPT 3.5)

<!-- b000606 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b000607 | furniture | pages [26] -->
2

<!-- b000608 | furniture | pages [26] -->
MATHmodels

<!-- b000609 | furniture | pages [26] -->
获取更多资讯

<!-- b000610 | ai_disclosure | pages [27] -->
Query1:<The model built needs to be able to predict whether a "swing" will occur at s points

<!-- b000611 | ai_disclosure | pages [27] -->
in the future and its direction - whether it will be a swing in favor of the athlete or a swing in

<!-- b000612 | ai_disclosure | pages [27] -->
favor of his opponent. To do this, we first defined three possible scenarios for each point and the

<!-- b000613 | ai_disclosure | pages [27] -->
concept of swing turning points.>

<!-- b000614 | ai_disclosure | pages [27] -->
Output:<Your description is already quite clear, but if you'd like a refined version, you might

<!-- b000615 | ai_disclosure | pages [27] -->
微信公众号：数学模型

<!-- b000616 | ai_disclosure | pages [27] -->
consider the following expression:

<!-- b000617 | ai_disclosure | pages [27] -->
"Our model aims to predict whether there will be 'fluctuations' in s future points of a match and

<!-- b000618 | ai_disclosure | pages [27] -->
accurately determine their direction—whether they favor the athlete or their opponent. To

<!-- b000619 | ai_disclosure | pages [27] -->
achieve this, we have clearly defined three possible scenarios for each point and introduced the

<!-- b000620 | ai_disclosure | pages [27] -->
concept of a 'fluctuation turning point.'">

<!-- b000621 | ai_disclosure | pages [27] -->
4. OpenAI ChatGPT(GPT 3.5)

<!-- b000622 | ai_disclosure | pages [27] -->
Query1:<What does rally mean in tennis>

<!-- b000623 | ai_disclosure | pages [27] -->
Output:<In tennis, "rally" refers to the continuous exchange of shots between two or more

<!-- b000624 | ai_disclosure | pages [27] -->
players. During a match, players engage in a back-and-forth of hitting the ball, responding to each

<!-- b000625 | ai_disclosure | pages [27] -->
other's serves and returns, forming a coherent sequence of shots. This continuous exchange of

<!-- b000626 | ai_disclosure | pages [27] -->
shots typically takes place in different areas of the court until one player fails to return the

<!-- b000627 | ai_disclosure | pages [27] -->
opponent's shot or makes an error. "Rally" reflects the intense competition and the application of

<!-- b000628 | ai_disclosure | pages [27] -->
skills and tactics in a tennis match, making it a common element of the game.>

<!-- b000629 | ai_disclosure | pages [27] -->
微信号：MATHmodels

<!-- b000630 | ai_disclosure | pages [27] -->
5. OpenAI ChatGPT(GPT 3.5)

<!-- b000631 | ai_disclosure | pages [27] -->
Query1:<What can you call a model that predicts swings in the match based on GSRF>

<!-- b000632 | ai_disclosure | pages [27] -->
Output:<1. **GSRF Swing Predictor Model**

<!-- b000633 | ai_disclosure | pages [27] -->
2. **Match Dynamics Forecasting with GSRF**

<!-- b000634 | ai_disclosure | pages [27] -->
3. **OptiSwing Model Powered by GSRF**

<!-- b000635 | ai_disclosure | pages [27] -->
4. **GSRF Momentum Forecast Model**

<!-- b000636 | ai_disclosure | pages [27] -->
5. **PrecisionSwing: A GSRF-based Model**

<!-- b000637 | ai_disclosure | pages [27] -->
When choosing a name, make sure it clearly conveys the model's purpose and the features based

<!-- b000638 | ai_disclosure | pages [27] -->
on GSRF, highlighting the functionality and advantages of the model.>

<!-- b000639 | ai_disclosure | pages [27] -->
6. OpenAI ChatGPT(GPT 3.5)

<!-- b000640 | ai_disclosure | pages [27] -->
Query1:<What are the characteristics and norms of memo writing>

<!-- b000641 | ai_disclosure | pages [27] -->
Output:<The writing of a memo should have the following characteristics and guidelines:

<!-- b000642 | ai_disclosure | pages [27] -->
1. **Conciseness:** Memos should be brief and to the point, avoiding lengthy and unnecessary

<!-- b000643 | ai_disclosure | pages [27] -->
details. Information should be presented directly, enabling readers to quickly grasp the main

<!-- b000644 | ai_disclosure | pages [27] -->
content.

<!-- b000645 | ai_disclosure | pages [27] -->
2. **Clarity and Specificity:** Memos should be clear and specific in conveying information.

<!-- b000646 | ai_disclosure | pages [27] -->
Avoid ambiguity and provide details that help readers understand the purpose and context of the

<!-- b000647 | ai_disclosure | pages [27] -->
memo.

<!-- b000648 | ai_disclosure | pages [27] -->
3. **Structured Format:** Memos typically follow a structured format, including headings such

<!-- b000649 | ai_disclosure | pages [27] -->
as "To," "From," "Date," and "Subject." This format helps organize information and makes it easy

<!-- b000650 | ai_disclosure | pages [27] -->
for readers to locate key details.

<!-- b000651 | ai_disclosure | pages [27] -->
4. **Professional Tone:** Maintain a professional and formal tone in memo writing. Use clear

<!-- b000652 | ai_disclosure | pages [27] -->
language and avoid slang or overly casual expressions.

<!-- b000653 | ai_disclosure | pages [27] -->
5. **Actionable Content:** If applicable, include actionable items or recommendations in the

<!-- b000654 | ai_disclosure | pages [27] -->
memo. Clearly state what actions, if any, need to be taken by the recipients.

<!-- b000655 | ai_disclosure | pages [27] -->
6. **Relevance:** Ensure that the content of the memo is relevant to the recipients and pertains

<!-- b000656 | ai_disclosure | pages [27] -->
to the subject at hand. Avoid including unnecessary information that may distract from the main

<!-- b000657 | ai_disclosure | pages [27] -->
message.

<!-- b000658 | ai_disclosure | pages [27] -->
关注数学模型

<!-- b000659 | furniture | pages [27] -->
2

<!-- b000660 | furniture | pages [27] -->
MATHmodels

<!-- b000661 | furniture | pages [27] -->
获取更多资讯

<!-- b000662 | ai_disclosure | pages [28] -->
7. **Correct Grammar and Spelling:** Check and double-check for proper grammar, punctuation,

<!-- b000663 | ai_disclosure | pages [28] -->
and spelling. Memos should be error-free to convey professionalism and attention to detail.

<!-- b000664 | ai_disclosure | pages [28] -->
8. **Date and Reference:** Include the date of the memo and any relevant references or

<!-- b000665 | ai_disclosure | pages [28] -->
attachments. This helps provide context and allows for easy cross-referencing.

<!-- b000666 | ai_disclosure | pages [28] -->
微信公众号：数学模型

<!-- b000667 | ai_disclosure | pages [28] -->
9. **Audience Consideration:** Tailor the memo to the specific audience, considering their

<!-- b000668 | ai_disclosure | pages [28] -->
background, knowledge, and needs. This ensures that the information is presented in a way that

<!-- b000669 | ai_disclosure | pages [28] -->
resonates with the recipients.>

<!-- b000670 | ai_disclosure | pages [28] -->
7. OpenAI ChatGPT(GPT 3.5)

<!-- b000671 | ai_disclosure | pages [28] -->
Query1:<Format cloth>

<!-- b000672 | ai_disclosure | pages [28] -->
Output:<The format of a memo typically includes the following elements:

<!-- b000673 | ai_disclosure | pages [28] -->
1. **Header Information:**

<!-- b000674 | ai_disclosure | pages [28] -->
- Date: The date of the memo.

<!-- b000675 | ai_disclosure | pages [28] -->
- To: The primary recipient of the memo.

<!-- b000676 | ai_disclosure | pages [28] -->
- From: The author of the memo.

<!-- b000677 | ai_disclosure | pages [28] -->
- Subject: The subject or purpose of the memo.

<!-- b000678 | ai_disclosure | pages [28] -->
微信号：MATHmodels

<!-- b000679 | ai_disclosure | pages [28] -->
Example:

<!-- b000680 | ai_disclosure | pages [28] -->
```

<!-- b000681 | ai_disclosure | pages [28] -->
Date: [Date]

<!-- b000682 | ai_disclosure | pages [28] -->
To: [Recipient]

<!-- b000683 | ai_disclosure | pages [28] -->
From: [Author]

<!-- b000684 | ai_disclosure | pages [28] -->
Subject: [Subject]

<!-- b000685 | ai_disclosure | pages [28] -->
```

<!-- b000686 | ai_disclosure | pages [28] -->
2. **Introduction (Opening Paragraph):**

<!-- b000687 | ai_disclosure | pages [28] -->
- Briefly introduce the purpose and background of the memo.

<!-- b000688 | ai_disclosure | pages [28] -->
- Provide an overview to let the reader know the main content of the memo.

<!-- b000689 | ai_disclosure | pages [28] -->
Example:

<!-- b000690 | ai_disclosure | pages [28] -->
```

<!-- b000691 | ai_disclosure | pages [28] -->
Dear [Recipient],

<!-- b000692 | ai_disclosure | pages [28] -->
I am writing to [Purpose]. This memo outlines [Overview].

<!-- b000693 | ai_disclosure | pages [28] -->
```

<!-- b000694 | ai_disclosure | pages [28] -->
3. **Body:**

<!-- b000695 | ai_disclosure | pages [28] -->
- Paragraphs elaborating on the main content, ensuring logical flow.

<!-- b000696 | ai_disclosure | pages [28] -->
- Use headings, numbering, or other formatting to emphasize important information.

<!-- b000697 | ai_disclosure | pages [28] -->
Example:

<!-- b000698 | ai_disclosure | pages [28] -->
```

<!-- b000699 | ai_disclosure | pages [28] -->
1. Overview

<!-- b000700 | ai_disclosure | pages [28] -->
[Content]

<!-- b000701 | ai_disclosure | pages [28] -->
2. Recommendations

<!-- b000702 | ai_disclosure | pages [28] -->
[Content]

<!-- b000703 | ai_disclosure | pages [28] -->
```

<!-- b000704 | ai_disclosure | pages [28] -->
4. **Conclusion:**

<!-- b000705 | ai_disclosure | pages [28] -->
- Summarize the main points or recommendations of the memo.

<!-- b000706 | ai_disclosure | pages [28] -->
- Emphasize expected actions or decisions.

<!-- b000707 | ai_disclosure | pages [28] -->
Example:

<!-- b000708 | ai_disclosure | pages [28] -->
```

<!-- b000709 | ai_disclosure | pages [28] -->
关注数学模型

<!-- b000710 | furniture | pages [28] -->
2

<!-- b000711 | furniture | pages [28] -->
MATHmodels

<!-- b000712 | furniture | pages [28] -->
获取更多资讯

<!-- b000713 | ai_disclosure | pages [29] -->
In conclusion, [Summarize points/recommendations]. I recommend [Specific

<!-- b000714 | ai_disclosure | pages [29] -->
recommendations].

<!-- b000715 | ai_disclosure | pages [29] -->
```

<!-- b000716 | ai_disclosure | pages [29] -->
5. **Appendix or Supplementary Information (if needed):**

<!-- b000717 | ai_disclosure | pages [29] -->
微信公众号：数学模型

<!-- b000718 | ai_disclosure | pages [29] -->
- Include additional data, charts, images, etc., to support main points.

<!-- b000719 | ai_disclosure | pages [29] -->
Example:

<!-- b000720 | ai_disclosure | pages [29] -->
```

<!-- b000721 | ai_disclosure | pages [29] -->
Appendix A: [Additional Information Title]

<!-- b000722 | ai_disclosure | pages [29] -->
[Content]

<!-- b000723 | ai_disclosure | pages [29] -->
```

<!-- b000724 | ai_disclosure | pages [29] -->
6. **Closing Remarks:**

<!-- b000725 | ai_disclosure | pages [29] -->
- Conclude the memo, thanking the reader for their time.

<!-- b000726 | ai_disclosure | pages [29] -->
- Provide further contact information for discussions regarding any questions or concerns.

<!-- b000727 | ai_disclosure | pages [29] -->
Example:

<!-- b000728 | ai_disclosure | pages [29] -->
```

<!-- b000729 | ai_disclosure | pages [29] -->
Thank you for your attention to this matter. If you have any questions or concerns, please feel

<!-- b000730 | ai_disclosure | pages [29] -->
微信号：MATHmodels

<!-- b000731 | ai_disclosure | pages [29] -->
free to contact me at [Contact Information].

<!-- b000732 | ai_disclosure | pages [29] -->
```

<!-- b000733 | ai_disclosure | pages [29] -->
7. **Signature:**

<!-- b000734 | ai_disclosure | pages [29] -->
- Provide the author's signature and position.

<!-- b000735 | ai_disclosure | pages [29] -->
Example:

<!-- b000736 | ai_disclosure | pages [29] -->
```

<!-- b000737 | ai_disclosure | pages [29] -->
Sincerely,

<!-- b000738 | ai_disclosure | pages [29] -->
[Signature]

<!-- b000739 | ai_disclosure | pages [29] -->
[Position]

<!-- b000740 | ai_disclosure | pages [29] -->
```

<!-- b000741 | ai_disclosure | pages [29] -->
Ensure the overall layout of the memo is clear, use concise language to ensure readers can

<!-- b000742 | ai_disclosure | pages [29] -->
quickly understand and take necessary actions.>

<!-- b000743 | ai_disclosure | pages [29] -->
8. OpenAI ChatGPT(GPT 3.5)

<!-- b000744 | ai_disclosure | pages [29] -->
Query1:<To show the fluctuation data of a game, where can you find such data>

<!-- b000745 | ai_disclosure | pages [29] -->
Output:<To showcase fluctuations in a game through data, you can obtain real-time data from

<!-- b000746 | ai_disclosure | pages [29] -->
various sources. Here are some common data sources:

<!-- b000747 | ai_disclosure | pages [29] -->
1. **Official Sports League Websites:** Most sports leagues provide real-time match data on

<!-- b000748 | ai_disclosure | pages [29] -->
their official websites, such as the NBA, NFL, soccer leagues, etc. These websites typically offer

<!-- b000749 | ai_disclosure | pages [29] -->
scores, statistics, and real-time updates on the progress of the game.

<!-- b000750 | ai_disclosure | pages [29] -->
2. **Sports News Websites and Apps:** Sports news websites and apps often provide real-time

<!-- b000751 | ai_disclosure | pages [29] -->
match updates and statistical data. Platforms like ESPN, CBS Sports, Yahoo Sports, etc., are

<!-- b000752 | ai_disclosure | pages [29] -->
common sports news sources offering real-time scores, player statistics, and more.

<!-- b000753 | ai_disclosure | pages [29] -->
3. **Professional Data Providers:** Some professional sports data providers, such as Sportradar,

<!-- b000754 | ai_disclosure | pages [29] -->
Stats Perform, etc., offer comprehensive real-time sports data services. These companies cater to

<!-- b000755 | ai_disclosure | pages [29] -->
media, betting companies, and other organizations, and may provide APIs for developers.

<!-- b000756 | ai_disclosure | pages [29] -->
4. **Broadcasting Platforms:** On official or affiliated broadcasting platforms for certain sports

<!-- b000757 | ai_disclosure | pages [29] -->
events, you can find real-time match data. This may include live commentary, score statistics, and

<!-- b000758 | ai_disclosure | pages [29] -->
other information.

<!-- b000759 | ai_disclosure | pages [29] -->
5. **Social Media:** Social media platforms, especially Twitter, can be a source of real-time game

<!-- b000760 | ai_disclosure | pages [29] -->
关注数学模型

<!-- b000761 | furniture | pages [29] -->
2

<!-- b000762 | furniture | pages [29] -->
MATHmodels

<!-- b000763 | furniture | pages [29] -->
获取更多资讯

<!-- b000764 | ai_disclosure | pages [30] -->
data. Official sports accounts, reporters, teams, and players often provide live updates during

<!-- b000765 | ai_disclosure | pages [30] -->
matches.

<!-- b000766 | ai_disclosure | pages [30] -->
Regardless of the data source you choose, ensure that the data is reliable, updated in real-time,

<!-- b000767 | ai_disclosure | pages [30] -->
and aligns with the information you want to convey. Some data sources may require registration

<!-- b000768 | ai_disclosure | pages [30] -->
微信公众号：数学模型

<!-- b000769 | ai_disclosure | pages [30] -->
or the use of API keys for data access. When using such data, adhere to relevant usage

<!-- b000770 | ai_disclosure | pages [30] -->
agreements and legal regulations.>

<!-- b000771 | ai_disclosure | pages [30] -->
9. OpenAI ChatGPT(GPT 3.5)

<!-- b000772 | ai_disclosure | pages [30] -->
Query1:<Run analysis of the sequence of the scoring order of the opposing teams

<!-- b000773 | ai_disclosure | pages [30] -->
What can we call this section>

<!-- b000774 | ai_disclosure | pages [30] -->
Output:<The title for this section can be "Sequential Run-Length Analysis of Match Scores in

<!-- b000775 | ai_disclosure | pages [30] -->
Tennis." This title explicitly expresses the theme of the section, involving a run-length analysis of

<!-- b000776 | ai_disclosure | pages [30] -->
the sequential scores of opposing sides in tennis matches to gain insights into scoring patterns

<!-- b000777 | ai_disclosure | pages [30] -->
and trends during the game.>

<!-- b000778 | ai_disclosure | pages [30] -->
10. OpenAI ChatGPT(GPT 3.5)

<!-- b000779 | ai_disclosure | pages [30] -->
Query1:<

<!-- b000780 | ai_disclosure | pages [30] -->
Counterfactual frameworks are often used to estimate the impact of an event on an outcome. In

<!-- b000781 | ai_disclosure | pages [30] -->
微信号：MATHmodels

<!-- b000782 | ai_disclosure | pages [30] -->
tennis, it is possible to quantify the impact of each shot on the outcome of a match by

<!-- b000783 | ai_disclosure | pages [30] -->
introducing leverage.

<!-- b000784 | ai_disclosure | pages [30] -->
What can the section be called>

<!-- b000785 | ai_disclosure | pages [30] -->
Output:<The title for this section can be "Leverage Analysis in Tennis: Quantifying the Impact

<!-- b000786 | ai_disclosure | pages [30] -->
of Each Point." This title explicitly conveys the theme of the section, involving the analysis of the

<!-- b000787 | ai_disclosure | pages [30] -->
potential impact of each point on the match outcome using a counterfactual framework and the

<!-- b000788 | ai_disclosure | pages [30] -->
concept of leverage.>

<!-- b000789 | ai_disclosure | pages [30] -->
11. OpenAI ChatGPT(GPT 3.5)

<!-- b000790 | ai_disclosure | pages [30] -->
Query1:<What are the game statistics for all the games prior to the game the player is

<!-- b000791 | ai_disclosure | pages [30] -->
currently competing in>

<!-- b000792 | ai_disclosure | pages [30] -->
Output:<The data encompassing a player's performance in all the preceding matches before

<!-- b000793 | ai_disclosure | pages [30] -->
the current one is commonly referred to as "Pre-match Data" or "Historical Data." This

<!-- b000794 | ai_disclosure | pages [30] -->
incorporates a player's previous performances, including scoring, assists, goal differentials, and

<!-- b000795 | ai_disclosure | pages [30] -->
other relevant statistics. Such data holds significant reference value for analyzing and predicting a

<!-- b000796 | ai_disclosure | pages [30] -->
player's performance in the current match.>

<!-- b000797 | ai_disclosure | pages [30] -->
12. OpenAI ChatGPT(GPT 3.5)

<!-- b000798 | ai_disclosure | pages [30] -->
Query1:<Short term Motivation and Confidence Boost What can this bar be called for an

<!-- b000799 | ai_disclosure | pages [30] -->
increase in the scoring rate of the serve>

<!-- b000800 | ai_disclosure | pages [30] -->
Output:<This section can be titled "Impact of Short-term Motivation and Confidence Boost on

<!-- b000801 | ai_disclosure | pages [30] -->
Serve Success Rate," highlighting the influence of short-term motivation and confidence

<!-- b000802 | ai_disclosure | pages [30] -->
enhancement on the success rate of serves.>

<!-- b000803 | ai_disclosure | pages [30] -->
13. OpenAI ChatGPT(GPT 3.5)

<!-- b000804 | ai_disclosure | pages [30] -->
Query1:<momentum>

<!-- b000805 | ai_disclosure | pages [30] -->
Output:<The term "Momentum" has different definitions in various fields. Here are some

<!-- b000806 | ai_disclosure | pages [30] -->
common meanings:

<!-- b000807 | ai_disclosure | pages [30] -->
1. **Physics:** In physics, momentum is a property of an object in motion, defined as the

<!-- b000808 | ai_disclosure | pages [30] -->
product of its mass and velocity. It is a conserved quantity in a conservative system, meaning that

<!-- b000809 | ai_disclosure | pages [30] -->
in the absence of external forces, the total momentum of a system remains constant.

<!-- b000810 | ai_disclosure | pages [30] -->
2. **Financial Markets:** In the financial domain, momentum is often used to describe the trend

<!-- b000811 | ai_disclosure | pages [30] -->
of asset prices. Momentum in asset prices refers to the rate of change over a period, typically

<!-- b000812 | ai_disclosure | pages [30] -->
expressed as a percentage change or return over a specific time frame.

<!-- b000813 | ai_disclosure | pages [30] -->
关注数学模型

<!-- b000814 | furniture | pages [30] -->
2

<!-- b000815 | furniture | pages [30] -->
MATHmodels

<!-- b000816 | furniture | pages [30] -->
获取更多资讯

<!-- b000817 | ai_disclosure | pages [31] -->
3. **Business and Management:** In business and management, momentum might refer to the

<!-- b000818 | ai_disclosure | pages [31] -->
competitive strength and growth trajectory of an organization or company in the market. A

<!-- b000819 | ai_disclosure | pages [31] -->
company with positive momentum in the market suggests continuous success in sales, market

<!-- b000820 | ai_disclosure | pages [31] -->
share, or innovation.

<!-- b000821 | ai_disclosure | pages [31] -->
微信公众号：数学模型

<!-- b000822 | ai_disclosure | pages [31] -->
4. **Sports:** In sports, momentum is commonly used to describe the performance trend of a

<!-- b000823 | ai_disclosure | pages [31] -->
team or athlete during a game. A player or team with momentum is considered to have a

<!-- b000824 | ai_disclosure | pages [31] -->
continuous string of success in the competition.

<!-- b000825 | ai_disclosure | pages [31] -->
In essence, "Momentum" signifies a trend or development in a particular direction. Its

<!-- b000826 | ai_disclosure | pages [31] -->
interpretation may vary depending on the context in which it is used.>

<!-- b000827 | ai_disclosure | pages [31] -->
14. OpenAI ChatGPT(GPT 3.5)

<!-- b000828 | ai_disclosure | pages [31] -->
Query1:<leverage>

<!-- b000829 | ai_disclosure | pages [31] -->
Output:<"Leverage" is a financial and economic term commonly used to describe the practice

<!-- b000830 | ai_disclosure | pages [31] -->
of borrowing or using debt capital to increase investment returns. In the realms of investment

<!-- b000831 | ai_disclosure | pages [31] -->
and finance, leverage can enhance returns, but it also amplifies risks. Leverage can be achieved

<!-- b000832 | ai_disclosure | pages [31] -->
through debt financing, derivatives, and other means with the goal of increasing the rate of

<!-- b000833 | ai_disclosure | pages [31] -->
return on an investment.

<!-- b000834 | ai_disclosure | pages [31] -->
微信号：MATHmodels

<!-- b000835 | ai_disclosure | pages [31] -->
Moreover, in different contexts, "leverage" can also be used to describe the concept of achieving

<!-- b000836 | ai_disclosure | pages [31] -->
greater effects through technical or strategic means, such as in the business context of "strategic

<!-- b000837 | ai_disclosure | pages [31] -->
leverage." In the sports domain, "leverage" may refer to the tactics or strategies employed during

<!-- b000838 | ai_disclosure | pages [31] -->
a game to achieve better results. In different contexts, the term may carry slightly different

<!-- b000839 | ai_disclosure | pages [31] -->
meanings.>

<!-- b000840 | ai_disclosure | pages [31] -->
15. OpenAI ChatGPT(GPT 3.5)

<!-- b000841 | ai_disclosure | pages [31] -->
Query1:<When an athlete is good in a game we call it hothand, but what can you call an

<!-- b000842 | ai_disclosure | pages [31] -->
athlete's state over time>

<!-- b000843 | ai_disclosure | pages [31] -->
Output:<Over an extended period, a player's performance is commonly referred to as their

<!-- b000844 | ai_disclosure | pages [31] -->
"steady state" or "long-term performance." The term contrasting with "hothand" might be

<!-- b000845 | ai_disclosure | pages [31] -->
"coldhand," used to describe a state of consistently poor or unstable performance over the long

<!-- b000846 | ai_disclosure | pages [31] -->
term. Both terms are often employed to characterize the performance trends of athletes in

<!-- b000847 | ai_disclosure | pages [31] -->
games. It is essential to note, however, that these terms can be contentious at times, as in sports

<!-- b000848 | ai_disclosure | pages [31] -->
psychology, it is sometimes challenging to substantiate whether these phenomena truly exist.>

<!-- b000849 | ai_disclosure | pages [31] -->
16. OpenAI ChatGPT(GPT 3.5)

<!-- b000850 | ai_disclosure | pages [31] -->
Query1:<A tennis coach is skeptical that “momentum” plays any role in the match. Instead,

<!-- b000851 | ai_disclosure | pages [31] -->
he

<!-- b000852 | ai_disclosure | pages [31] -->
postulates that swings in play and runs of success by one player are random. Use your

<!-- b000853 | ai_disclosure | pages [31] -->
model/metric to assess this claim.

<!-- b000854 | ai_disclosure | pages [31] -->
What is the opposite of this coach's view>

<!-- b000855 | ai_disclosure | pages [31] -->
Output:<The opposite viewpoint to the tennis coach's skepticism about the role of

<!-- b000856 | ai_disclosure | pages [31] -->
"momentum" in the match would be the belief that "momentum" does indeed play a significant

<!-- b000857 | ai_disclosure | pages [31] -->
role in the game. This opposing perspective suggests that swings in play and runs of success by

<!-- b000858 | ai_disclosure | pages [31] -->
one player are not entirely random but are influenced by momentum, which could be attributed

<!-- b000859 | ai_disclosure | pages [31] -->
to various factors such as confidence, skill, or psychological aspects affecting player

<!-- b000860 | ai_disclosure | pages [31] -->
performance.>

<!-- b000861 | ai_disclosure | pages [31] -->
17. OpenAI ChatGPT(GPT 3.5)

<!-- b000862 | ai_disclosure | pages [31] -->
Query1:<What can I call the chapter that uses contingency tables to analyze the relationship

<!-- b000863 | ai_disclosure | pages [31] -->
between score and momentum>

<!-- b000864 | ai_disclosure | pages [31] -->
Output:<This section can be titled either "Correlation Analysis of Scores and Momentum" or

<!-- b000865 | ai_disclosure | pages [31] -->
"Contingency Table Analysis of Scores and Momentum.">

<!-- b000866 | ai_disclosure | pages [31] -->
关注数学模型

<!-- b000867 | furniture | pages [31] -->
2

<!-- b000868 | furniture | pages [31] -->
MATHmodels

<!-- b000869 | furniture | pages [31] -->
获取更多资讯
