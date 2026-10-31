# P-C-2024-2425454-a27c2efc

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | prose | pages [1] -->
Problem Chosen

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
1

<!-- b000027 | heading | pages [2] -->
Introduction

<!-- b000028 | prose | pages [2] -->
3 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000029 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000030 | prose | pages [2] -->
Restatement and Analysis of the Problem . . . . . . . . . . . . . . . . . . . . . 1.2 3 Overview of Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000031 | prose | pages [2] -->
2

<!-- b000032 | heading | pages [2] -->
Assumptions and Justification

<!-- b000033 | prose | pages [2] -->
3

<!-- b000034 | heading | pages [2] -->
List of Notation

<!-- b000035 | prose | pages [2] -->
4 Data Pre-processing

<!-- b000036 | prose | pages [2] -->
5 Task 1 : Captures the Flow of Play 5.1 Specifying Conceptual Significance

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | prose | pages [2] -->
5

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | prose | pages [2] -->
5

<!-- b000041 | prose | pages [2] -->
6 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
6 Leverage Quantitative Momentum Capture Model . . . . . . . . . . . . . . . . 5.2 6 Impact of Short-term Motivation and Confidence Boost on Serve Suc- 5.2.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . cess Rate 6 Monte Carlo Simulation for Winning Probability 5.2.2 . . . . . . . . . . . .

<!-- b000043 | prose | pages [2] -->
9

<!-- b000044 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000045 | prose | pages [2] -->
Leveraging Every Point with Counterfactual Framework 5.2.3 . . . . . . . .

<!-- b000046 | prose | pages [2] -->
10 Defining Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.4 11 Visualization of the Flow of Play . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 11

<!-- b000047 | prose | pages [2] -->
Task 2 : Whether the Swings of Play and Momentum are correlated 6 12 Run Test for Assessing Randomness in Match Scores Sequence . . . . . . . . . 6.1 12 Scores-Momentum Contingency Analysis 6.2 . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | prose | pages [2] -->
13

<!-- b000049 | prose | pages [2] -->
Task 3 : Identify Indicators Signaling a Change in Flow 7 14 . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 GSRF Swing Predictor Model 14 The Swings Reversal Point . . . . . . . . . . . . . . . . . . . . . . . . 7.1.1 14 . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1.2 The Selected Indicator 15 GSRF Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1.3 15 The Predicted Swings Results of the Match 7.1.4 . . . . . . . . . . . . . . .

<!-- b000050 | prose | pages [2] -->
16 Player Performance Factor Analysis Model . . . . . . . . . . . . . . . . . . . . 7.2 17

<!-- b000051 | heading | pages [2] -->
Task 4 : Assess the Generalization of Model

<!-- b000052 | prose | pages [2] -->
8 20 Generalization in women’s tennis matches . . . . . . . . . . . . . . . . . . . . 8.1 20 Discussion on the impact of the playing surface. . . . . . . . . . . . . . . . . . 8.2

<!-- b000053 | prose | pages [2] -->
9

<!-- b000054 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000055 | heading | pages [2] -->
10 Strength and Weakness

<!-- b000056 | prose | pages [2] -->
22

<!-- b000057 | prose | pages [2] -->
22

<!-- b000058 | prose | pages [2] -->
23 10.1 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | prose | pages [2] -->
23 10.2 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | heading | pages [2] -->
11 Further Discussion

<!-- b000061 | heading | pages [2] -->
Memorandum

<!-- b000062 | prose | pages [2] -->
Reference

<!-- b000063 | prose | pages [2] -->
23

<!-- b000064 | prose | pages [2] -->
23

<!-- b000065 | prose | pages [2] -->
24

<!-- b000066 | prose | pages [2] -->
25

<!-- b000067 | prose | pages [2] -->
关注数学模型

<!-- b000068 | furniture | pages [2] -->
2

<!-- b000069 | furniture | pages [2] -->
MATHmodels

<!-- b000070 | furniture | pages [2] -->
获取更多资讯

<!-- b000071 | furniture | pages [3] -->
Team # 2425454

<!-- b000072 | prose | pages [3] -->
1

<!-- b000073 | heading | pages [3] -->
Introduction

<!-- b000074 | prose | pages [3] -->
1.1

<!-- b000075 | heading | pages [3] -->
Background

<!-- b000076 | furniture | pages [3] -->
Page 3 of 25

<!-- b000077 | prose | pages [3] -->
Tennis matches are exciting and ever-changing. Players who seem to be dominating expe-

<!-- b000078 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000079 | prose | pages [3] -->
rience incredible swings from time to time. For example, a player may be in control of the match with a series of points, but at one rally, the opponent suddenly breaks and the situation is reversed. We often attribute this dramatic turn of events to "momentum".

<!-- b000080 | prose | pages [3] -->
"Momentum" heightens emotional intensity in the match, creating unpredictability and anticipation, making each moment charged and intense.

<!-- b000081 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000082 | caption | pages [3] -->
Figure 1: The fast-changing, heart-stopping swings of a tennis match.

<!-- b000083 | prose | pages [3] -->
Restatement and Analysis of the Problem 1.2

<!-- b000084 | prose | pages [3] -->
We need to complete the following tasks based on the data given in the question and additional data from ourselves:

<!-- b000085 | prose | pages [3] -->
• Task 1 : Build a model to capture the flow of play as points occur.

<!-- b000086 | prose | pages [3] -->
The model is required to be able to qualitatively and quantitatively describe performance of players at a given time and provide a visualization. In particular, the model should take the higher probability of the server winning into account.

<!-- b000087 | prose | pages [3] -->
• Task 2 : Assess whether swings in play and runs of success by one player during a match are random.

<!-- b000088 | prose | pages [3] -->
• Task 3 : Look for indicators that identify the point in time when the game situation is reversed.

<!-- b000089 | prose | pages [3] -->
– Develop a model to predict swings in a match. Find the indicator with the highest

<!-- b000090 | prose | pages [3] -->
correlation.

<!-- b000091 | prose | pages [3] -->
– Based on momentum swings in past games, we need to give players advice on how

<!-- b000092 | prose | pages [3] -->
to deal with other opponents.

<!-- b000093 | prose | pages [3] -->
• Task 4 : Evaluate the generalisability of the model we have developed to other competitions.

<!-- b000094 | prose | pages [3] -->
• Task 5 : Write a memo summarising the results and giving targeted advice to coaches and players.

<!-- b000095 | prose | pages [3] -->
关注数学模型

<!-- b000096 | furniture | pages [3] -->
2

<!-- b000097 | furniture | pages [3] -->
MATHmodels

<!-- b000098 | furniture | pages [3] -->
获取更多资讯

<!-- b000099 | furniture | pages [4] -->
Team # 2425454

<!-- b000100 | furniture | pages [4] -->
Page 4 of 25

<!-- b000101 | prose | pages [4] -->
After some analysis, we found that there is a close relationship between the tasks: In Task 1 and Task 2, we need to build a model describing the situation of the game (i.e. the relative performance of two players) and explore the relationship between "momentum" and changes in the game situation, respectively. The results of these two tasks are the basis of task 3. In task

<!-- b000102 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000103 | prose | pages [4] -->
3, we need to further build a model that can predict the situation fluctuations in the competition and find out the key factors that affect the competition. We also need to start to consider the applicability of our model. Can it provide competition suggestions for players to achieve better results? The fourth task is to consider the extensibility of our model. Are we still valuable in other competitions? Finally, in the memo, we need to focus on our model and its value.

<!-- b000104 | prose | pages [4] -->
In summary, we should effectively build a model that can predict the fluctuations of the competition situation, provide practical advice to players and coaches, and be extensible across different competitions.

<!-- b000105 | prose | pages [4] -->
1.3 Overview of Our Work

<!-- b000106 | prose | pages [4] -->
On the basis of the above analysis, we have carried out our work. Our working framework is shown in Figure 2.

<!-- b000107 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000108 | caption | pages [4] -->
Figure 2: Our Work Overview Schematic Diagram

<!-- b000109 | prose | pages [4] -->
关注数学模型

<!-- b000110 | furniture | pages [4] -->
2

<!-- b000111 | furniture | pages [4] -->
MATHmodels

<!-- b000112 | furniture | pages [4] -->
获取更多资讯

<!-- b000113 | furniture | pages [5] -->
Team # 2425454

<!-- b000114 | furniture | pages [5] -->
Page 5 of 25

<!-- b000115 | prose | pages [5] -->
The detailed modeling process and model details are presented in the following article.

<!-- b000116 | heading | pages [5] -->
Assumptions and Justification

<!-- b000117 | prose | pages [5] -->
2

<!-- b000118 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000119 | prose | pages [5] -->
To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified.

<!-- b000120 | prose | pages [5] -->
• When a player wins a point, he experiences a short-term "motivational" effect that increases the probability of winning the next point. The motivation effect can lead to increased self-confidence on a psychological level as well as increased physical conditioning on a physiological level.

<!-- b000121 | prose | pages [5] -->
• Lifting effects are cumulative. A string of successes may have a positive psychological and emotional effect on a player, so that a player winning more points in a row will result in a greater probability of winning the next point on serve.

<!-- b000122 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000123 | prose | pages [5] -->
3

<!-- b000124 | heading | pages [5] -->
List of Notation

<!-- b000125 | heading | pages [5] -->
Symbol

<!-- b000126 | prose | pages [5] -->
p, q mi

<!-- b000127 | prose | pages [5] -->
Meaning

<!-- b000128 | prose | pages [5] -->
Probability of Winning Increase in the Rate of Serve points TAB The Cumulative Total Score Li G M λ Leverage of the ith Point The leverage Gained Momentum Tuning Parameter

<!-- b000129 | prose | pages [5] -->
Noted: Symbols not specified in the table should be referred to their first occurrence.

<!-- b000130 | prose | pages [5] -->
4 Data Pre-processing

<!-- b000131 | prose | pages [5] -->
• Outlier Handling

<!-- b000132 | prose | pages [5] -->
No clear outliers were observed in the data. However, in a match between Frances Tiafoe and Grigor Dimitrov during the third round, a notable occurrence occurred with a 24-hour time gap between two points at a set score of 2:0, as shown in Table 1.

<!-- b000133 | caption | pages [5] -->
Table 1: Suspected Outliers

<!-- b000134 | prose | pages [5] -->
关注数学模型

<!-- b000135 | furniture | pages [5] -->
2

<!-- b000136 | furniture | pages [5] -->
MATHmodels

<!-- b000137 | furniture | pages [5] -->
获取更多资讯

<!-- b000138 | furniture | pages [6] -->
Team # 2425454

<!-- b000139 | furniture | pages [6] -->
Page 6 of 25

<!-- b000140 | prose | pages [6] -->
Upon consulting relevant information, we found the following explanation:

<!-- b000141 | prose | pages [6] -->
". . . . . . Saturday’s game was suspended due to inclement weather, so it was postponed to a day later to continue on Sunday.. . . . . . "

<!-- b000142 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000143 | prose | pages [6] -->
Therefore, the data is correct.

<!-- b000144 | prose | pages [6] -->
• Missing Value Handling

<!-- b000145 | prose | pages [6] -->
In thedatasetgiveninthequestion, thequantitiesservewidth, servedepth, and returndepth have missing values, for which we use the nearest-neighbour filling method to fill them.

<!-- b000146 | prose | pages [6] -->
• Tag Encoding of String Type Data

<!-- b000147 | prose | pages [6] -->
There are many categorical variables in the data given in the title, presented as strings. In order to make it easier for the model to receive this type of data, we preprocess this type of data by means of label coding, using virtual coding for the last three columns of servewidth, servedepth, and returndepth in the data of the tennis match.

<!-- b000148 | prose | pages [6] -->
Task 1 : Captures the Flow of Play 5

<!-- b000149 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000150 | prose | pages [6] -->
Specifying Conceptual Significance 5.1

<!-- b000151 | prose | pages [6] -->
Since a relatively large number of concepts are introduced in our model, we first identify and clarify the meaning of the introduced concepts here.

<!-- b000152 | prose | pages [6] -->
• Short-term Motivation refers to a brief period of above-average performance by a player following a motivating event.

<!-- b000153 | prose | pages [6] -->
• Confidence Boost is when a player, drawing upon their self-awareness developed through multiple games in their professional career and an assessment of the current situation, generates positive expectations regarding the outcome of the match.

<!-- b000154 | prose | pages [6] -->
• Serve Success Rate is probability of scoring in a service game.

<!-- b000155 | prose | pages [6] -->
• Winning Probability is the likelihood of the player winning the game/set/match.

<!-- b000156 | prose | pages [6] -->
• Leverage measures how a ball’s outcome impacts the margin of victory.

<!-- b000157 | prose | pages [6] -->
• Momentum aims to describe which player is in control at any given point in the match—based on who is currently winning more points and who is prevailing in cru- cial (high-leverage) moments. It is defined as a player’s exponentially weighted leverage average.

<!-- b000158 | prose | pages [6] -->
At each point in the match, both competing players will have their own momentum values. • We define the fluctuations in momentum as the Flow of Play. The relationship between the above concepts, i.e., the framework of the model, is shown schematically below, and in the following we show the model building process in full.

<!-- b000159 | heading | pages [6] -->
Leverage Quantitative Momentum Capture Model

<!-- b000160 | prose | pages [6] -->
5.2

<!-- b000161 | prose | pages [6] -->
Impact of Short-term Motivation and Confidence Boost on Serve Success Rate 5.2.1

<!-- b000162 | prose | pages [6] -->
Short-term Motivation refers to a brief period of above-average performance by a player following a motivating event (e.g., a breaking serve) during a match, a phenomenon known in sports as "hot hands"[1]. We developed a probabilistic model that quantifies Short-term Motivation as an increase in serve success rate.

<!-- b000163 | prose | pages [6] -->
The following two assumptions are necessary:

<!-- b000164 | prose | pages [6] -->
关注数学模型

<!-- b000165 | furniture | pages [6] -->
2

<!-- b000166 | furniture | pages [6] -->
MATHmodels

<!-- b000167 | furniture | pages [6] -->
获取更多资讯

<!-- b000168 | furniture | pages [7] -->
Team # 2425454

<!-- b000169 | furniture | pages [7] -->
Page 7 of 25

<!-- b000170 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000171 | caption | pages [7] -->
Figure 3: Relationships Between Concepts, i.e., Schematic of the Framework of the Model

<!-- b000172 | prose | pages [7] -->
• When a player wins a point, he experiences a short-term "motivational" effect that in- creases the probability of winning the next point. • Lifting effects are cumulative. A string of successes may have a positive psychological

<!-- b000173 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000174 | prose | pages [7] -->
and emotional effect on a player, so that a player winning more points in a row will result in a greater probability of winning the next point on serve. Here i denotes the number of consecutive points scored by a player A or his opponent B; and mi denotes the increase in the rate of serving points on a player’s next serve after winning ipoints consecutively due to the short-term motivation gained. Then, the probability of winning the next serve under short-term motivation ps versus qs is calculated by equations (1) .

<!-- b000175 | prose | pages [7] -->
ps = pf(1 + mA

<!-- b000176 | prose | pages [7] -->
i );

<!-- b000177 | prose | pages [7] -->
(1)

<!-- b000178 | prose | pages [7] -->
qs = qf(1 + mB

<!-- b000179 | prose | pages [7] -->
i ),

<!-- b000180 | prose | pages [7] -->
where pf and qf are the scoring probabilities before player A and player B are motivated, respectively.

<!-- b000181 | prose | pages [7] -->
The short-term motivation that a player receives for scoring a game n times in a row is referred to as n-order short-term motivation. Using the dataset given in the title, we statistically obtained a plot of the total number of short-term motivations occurring in a match versus order, and the results are shown in Figure 4. It is clear to see that short-term motivations of order four and above rarely occur in the dataset used in this study. Therefore, only short-term motivations of order three and below are considered in this paper.

<!-- b000182 | prose | pages [7] -->
Short-term motivation focuses on short-term status enhancement during matches and ignores sources of motivation on a longer time scale in the player’s lifetime, so we continue to introduce a confidence-boosting factor.

<!-- b000183 | prose | pages [7] -->
A new tuning parameter λ is introduced, which represents the effect of the confidence boosting factor on the success rate of the next serve [2], the probabilities after the effect are expressed as ps and qs – see equation (2)

<!-- b000184 | prose | pages [7] -->
λ pt + (1 −TAB

<!-- b000185 | prose | pages [7] -->
pc = TAB

<!-- b000186 | prose | pages [7] -->
λ )p0;

<!-- b000187 | prose | pages [7] -->
(2)

<!-- b000188 | prose | pages [7] -->
λ qt + (1 −TAB

<!-- b000189 | prose | pages [7] -->
qc = TAB

<!-- b000190 | prose | pages [7] -->
λ )q0,

<!-- b000191 | prose | pages [7] -->
where TAB denotes the cumulative total score of the opposing players since the start of the match, and pt and qt denote the probability of scoring for player A and player B, respectively,

<!-- b000192 | prose | pages [7] -->
关注数学模型

<!-- b000193 | furniture | pages [7] -->
2

<!-- b000194 | furniture | pages [7] -->
MATHmodels

<!-- b000195 | furniture | pages [7] -->
获取更多资讯

<!-- b000196 | furniture | pages [8] -->
Team # 2425454

<!-- b000197 | furniture | pages [8] -->
Page 8 of 25

<!-- b000198 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000199 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000200 | caption | pages [8] -->
Figure 4: Histogram of the Total Count of Short-Term Incentives Occurring in Competitions as

<!-- b000201 | prose | pages [8] -->
a Function of Order

<!-- b000202 | prose | pages [8] -->
since the start of the match up to the present. p0 and q0 denote the historical data on the success rate of the opposing teams’ serves on the grass court surface prior to the current match (source: https://www.infosys.com/)

<!-- b000203 | prose | pages [8] -->
Eq. (2) describes the phenomenon that a player’s historical results always have the greatest impact on player status at the start of a match, and then diminish as the match progresses - the performance of the current match begins to influence player play more.

<!-- b000204 | prose | pages [8] -->
We then performed a linear interpolation of the obtained probabilities. The interpolation coefficient is the cumulative total score of the current pair divided by the coefficient λ (i.e. TAB

<!-- b000205 | prose | pages [8] -->
λ ).

<!-- b000206 | prose | pages [8] -->
The short-term motivation is fluctuating as the match progresses, while the confidence boost takes into account the player’s self-perception established over the course of his career as well as the current situation in the match, which is the "undertone" of the motivated state, therefore, we use pc and qc in Eq. (2) instead of pf and qf in Eq. (1), we can get the success rate of the next serve after considering the short-term motivation and confidence improvement:

<!-- b000207 | prose | pages [8] -->
· pc + (1 −TAB

<!-- b000208 | prose | pages [8] -->
p = [TAB

<!-- b000209 | prose | pages [8] -->
λ λ )pt](1 + mA

<!-- b000210 | prose | pages [8] -->
i );

<!-- b000211 | prose | pages [8] -->
· qc + (1 −TAB

<!-- b000212 | prose | pages [8] -->
q = [TAB

<!-- b000213 | prose | pages [8] -->
λ λ )qt](1 + mB

<!-- b000214 | prose | pages [8] -->
i ).

<!-- b000215 | prose | pages [8] -->
The above equation shows the effect of short-term motivation and confidence enhancement on serve percentage.

<!-- b000216 | prose | pages [8] -->
In tennis matches, players typically have an advantage when serving[3]. According to the data we have collected, the serving success rate of professional players exceeds 50%. Based on this understanding, players gain confidence in serving games. Due to this "confidence boost," we have incorporated the player’s performance in serving games into consideration in our model.

<!-- b000217 | prose | pages [8] -->
关注数学模型

<!-- b000218 | furniture | pages [8] -->
2

<!-- b000219 | furniture | pages [8] -->
MATHmodels

<!-- b000220 | furniture | pages [8] -->
获取更多资讯

<!-- b000221 | furniture | pages [9] -->
Team # 2425454

<!-- b000222 | furniture | pages [9] -->
Page 9 of 25

<!-- b000223 | prose | pages [9] -->
Monte Carlo Simulation for Winning Probability 5.2.2

<!-- b000224 | prose | pages [9] -->
As a sports competition, there is a great deal of uncertainty in tennis, for which Monte Carlo algorithms can provide probabilistic estimates of the outcome.

<!-- b000225 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000226 | prose | pages [9] -->
Based on the serve success rate obtained in the previous section, we use the Monte Carlo algorithm to simulate each ball, and ultimately obtain the winners and losers of each game, set and even the whole match. Then in this process, the randomness and diversity of the simulation are ensured by generating a large number of random number seeds.

<!-- b000227 | prose | pages [9] -->
Here is the pseudo-code for the algorithm we used:

<!-- b000228 | heading | pages [9] -->
Algorithm 1: Monte Carlo Simulation for Winning Probability

<!-- b000229 | prose | pages [9] -->
Input: phist,data Output: win_p

<!-- b000230 | heading | pages [9] -->
1 begin

<!-- b000231 | prose | pages [9] -->
for i in scores do 2

<!-- b000232 | prose | pages [9] -->
for i 1 to n do 3

<!-- b000233 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000234 | prose | pages [9] -->
repeat 4

<!-- b000235 | prose | pages [9] -->
Calculate pcur based on previous data 5

<!-- b000236 | prose | pages [9] -->
Calculate scoring probability based on the formula.3 6

<!-- b000237 | prose | pages [9] -->
Update players’ score/game/set based on tennis rule 7

<!-- b000238 | prose | pages [9] -->
Record nwin of game/set/match 8

<!-- b000239 | prose | pages [9] -->
until one side wins the match; 9

<!-- b000240 | prose | pages [9] -->
end 10

<!-- b000241 | prose | pages [9] -->
win_p[i] ←nwin/n 11

<!-- b000242 | prose | pages [9] -->
end 12

<!-- b000243 | heading | pages [9] -->
13 end

<!-- b000244 | prose | pages [9] -->
We use the above algorithm to perform N = 1000 simulations of the remaining fixtures after each ball and determine the final outcome of that game. If the number of wins of player K(K = A, B) in the result is n, then we say that the winning rate of player K after that ball is n N × 100%.

<!-- b000245 | prose | pages [9] -->
The graph below illustrates the real-time fluctuations in match-winning probabilities, sim- ulated through the Monte Carlo algorithm, for Djokovic (highlighted in red) and Alcarez (highlighted in green) during the 2023 Wimbledon final.

<!-- b000246 | caption | pages [9] -->
Figure 5: Wimbledon Final Real-Time Predicted Win Probability Swings Chart. The thick gray

<!-- b000247 | prose | pages [9] -->
dashed lines represent set divisions, while the thin gray dashed lines represent game divisions.

<!-- b000248 | prose | pages [9] -->
关注数学模型

<!-- b000249 | furniture | pages [9] -->
2

<!-- b000250 | furniture | pages [9] -->
MATHmodels

<!-- b000251 | furniture | pages [9] -->
获取更多资讯

<!-- b000252 | furniture | pages [10] -->
Team # 2425454

<!-- b000253 | furniture | pages [10] -->
Page 10 of 25

<!-- b000254 | prose | pages [10] -->
It can be seen that the situation is very anxious, and the match winning probablity in the middle of the game fluctuates greatly throughout the match. The first set was easily won by Djokovic, but the second was tense . . . . . . This is consistent with the facts. Thus, the reliability of the algorithm is verified.

<!-- b000255 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000256 | prose | pages [10] -->
Leveraging Every Point with Counterfactual Framework 5.2.3

<!-- b000257 | prose | pages [10] -->
Next, we will employ a counterfactual framework[4] to delve into the analysis of the impact of each point in a tennis match. By defining ’leverage’ as a measure of the magnitude of change in winning probability resulting from winning or losing a particular point, we will quantify the potential influence of each point on the outcome of each game/set, and even the entire match.

<!-- b000258 | prose | pages [10] -->
The following example shows the exact steps of our leverage quantisation process.

<!-- b000259 | prose | pages [10] -->
• Current Scenario: Player A is down 0-15 in the current game, his real-time winning probablity (abbreviated as RTWP in the latter.) is 69%.

<!-- b000260 | prose | pages [10] -->
• Define Realistic Scenario: If player A wins this point, the score becomes 30-30 and his

<!-- b000261 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000262 | prose | pages [10] -->
RTWP becomes 71%.

<!-- b000263 | prose | pages [10] -->
• Imagine the Opposite Scenario: if player A loses this point, the score becomes 15-40 and his RTWP becomes 65%.

<!-- b000264 | prose | pages [10] -->
• Calculating Leverage: By comparing the change in A’s RTWP in these two scenarios, the Leverage for this point is calculated to be 6%.

<!-- b000265 | prose | pages [10] -->
Note: The above data is fictional. The above process is shown schematically below:

<!-- b000266 | caption | pages [10] -->
Figure 6: Leveraged Quantitative Schematic

<!-- b000267 | prose | pages [10] -->
We set Li to represent the leverage of the ith point. The positive or negative sign does not indicate the magnitude but only signifies which player gained the point. Throughout the subsequent analysis, we consistently calculate the leverage with respect to Player A. If Li > 0, it means that player A won the ith point; if Li < 0, it means that player B won the ith point; if Li = 0, it means that the ith point did not result in a change in winning percentage.

<!-- b000268 | prose | pages [10] -->
If playerK wins the ith point, the playerK is called to have gained leverage, and vice versa, the player is called to have lost leverage. The leverage gained is treated as a separate variable and denoted by the symbol G. To wit:

<!-- b000269 | prose | pages [10] -->
(

<!-- b000270 | prose | pages [10] -->
Li ⩾0 Li,

<!-- b000271 | prose | pages [10] -->
(

<!-- b000272 | prose | pages [10] -->
Li ⩽0 Li,

<!-- b000273 | prose | pages [10] -->
Li < 0 , GB

<!-- b000274 | prose | pages [10] -->
GA

<!-- b000275 | prose | pages [10] -->
i =

<!-- b000276 | prose | pages [10] -->
0,

<!-- b000277 | prose | pages [10] -->
i =

<!-- b000278 | prose | pages [10] -->
0, Li > 0

<!-- b000279 | prose | pages [10] -->
关注数学模型

<!-- b000280 | furniture | pages [10] -->
2

<!-- b000281 | furniture | pages [10] -->
MATHmodels

<!-- b000282 | furniture | pages [10] -->
获取更多资讯

<!-- b000283 | furniture | pages [11] -->
Team # 2425454

<!-- b000284 | prose | pages [11] -->
5.2.4 Defining Momentum

<!-- b000285 | furniture | pages [11] -->
Page 11 of 25

<!-- b000286 | prose | pages [11] -->
We define momentum(M) as an exponentially weighted moving average of the leverage gained by a player[5].

<!-- b000287 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000288 | prose | pages [11] -->
i−1 + (1 −α)2GK

<!-- b000289 | prose | pages [11] -->
= GK

<!-- b000290 | prose | pages [11] -->
i + (1 −α)GK

<!-- b000291 | prose | pages [11] -->
M K

<!-- b000292 | prose | pages [11] -->
i−2 + · · · + (1 −α)iGK

<!-- b000293 | prose | pages [11] -->
0 , 1 + (1 −α) + (1 −α)2 + · · · + (1 −α)t

<!-- b000294 | prose | pages [11] -->
i

<!-- b000295 | prose | pages [11] -->
where [G0, G1, . . . , Gi] is the leverage of i recent points, and the points are listed in chronological order.α is the smoothing coefficient ,and α ∈(0, 1). Due to the fact that the impact of previous goals diminishes on the player’s current impact as the game progresses, the importance of a certain points decreases exponentially as the game progresses, The leverage of the most recent goal has the greatest impact on momentum, and the sooner the point is scored, the less it impact on momentum.

<!-- b000296 | prose | pages [11] -->
Finally, by focusing on the fluctuations in momentum, we can capture "the flow of play".

<!-- b000297 | prose | pages [11] -->
5.3 Visualization of the Flow of Play

<!-- b000298 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000299 | prose | pages [11] -->
Utilizing our model, we have described the match flow of the Wimbledon Final in 2023. The parameter α is set to 0.33, by testing the leverage defined by the handicap winning percentage, it better reflects the fluctuation of the game. The visualization is presented as follows:

<!-- b000300 | caption | pages [11] -->
Figure 7: The Visualization of Match Flow. The thick gray dashed lines represent set divisions,

<!-- b000301 | prose | pages [11] -->
while the thin gray dashed lines represent game divisions.The same applies to the subsequent figure.

<!-- b000302 | prose | pages [11] -->
Our results perfectly describe the flow of the match. We can correlate the fluctuations in momentum in the graph with the remarkable moments in the game:

<!-- b000303 | prose | pages [11] -->
Riding a dominating momentum after crushing the opponent in the first set, Djokovic had the opportunity to claim the second set. However, Alcaraz overcame the initial struggle and secured a crucial break in the second set, leading 2-1; Djokovic swiftly responded with a break of his own, but Alcaraz seized the opportunity in a tense tiebreak, winning the set with a brilliant backhand winner. In the third set, Djokovic struggled with a low momentum, while Alcaraz continued his high momentum, leading 2-1. In the fourth set, Djokovic broke Alcaraz twice, leveling the match.

<!-- b000304 | prose | pages [11] -->
Then, in the decisive fifth set, Djokovic missed a golden opportunity while leading, allowing Alcaraz to break and take a 2-1 lead. With Djokovic’s momentum dropping, he once again violated rules by smashing his racket against the net post, subsequently trailing 3-1. Alcaraz remained resolute, maintaining his high momentum. When Djokovic hit a forehand into the net, Alcaraz secured his extraordinary victory at 3-1."

<!-- b000305 | prose | pages [11] -->
关注数学模型

<!-- b000306 | furniture | pages [11] -->
2

<!-- b000307 | furniture | pages [11] -->
MATHmodels

<!-- b000308 | furniture | pages [11] -->
获取更多资讯

<!-- b000309 | furniture | pages [12] -->
Team # 2425454

<!-- b000310 | furniture | pages [12] -->
Page 12 of 25

<!-- b000311 | prose | pages [12] -->
It can be found that the momentum we define shows the race flow well.

<!-- b000312 | prose | pages [12] -->
Task 2 : Whether the Swings of Play and Momentum are 6 correlated

<!-- b000313 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000314 | prose | pages [12] -->
A tennis coach argues that swings in play and runs of success in a match are random and not related to momentum. In response to this view, we plan to determine whether the distribution of scores in a match is completely random by means of a Runs Test.

<!-- b000315 | prose | pages [12] -->
Run Test for Assessing Randomness in Match Scores Sequence 6.1

<!-- b000316 | prose | pages [12] -->
The runs test is commonly employed to examine whether a binary sample with two potential outcomes, such as X and Y, originates from a binomial distribution.

<!-- b000317 | prose | pages [12] -->
In the runs test, a sample is drawn from a population containing X and Y, assuming n X’s and m Y’s are drawn. Subsequently, X and Y are arranged in order of sampling to form a sequence. In this sequence, consecutive occurrences of X or Y are referred to as a run. The total number of runs is denoted as the run count r.

<!-- b000318 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000319 | caption | pages [12] -->
Figure 8: Runs Example Chart

<!-- b000320 | prose | pages [12] -->
In the XY sequence shown in Figure 8, there are n = 4 runs of X and m = 4 runs of Y, with a total of r = 8 runs.

<!-- b000321 | prose | pages [12] -->
• The null hypothesis H0: The arrangement of X and Y is random, with the probability of drawing X each time as P, and the probability of drawing Y as 1P.

<!-- b000322 | prose | pages [12] -->
• The alternative hypothesis H1: The arrangement of X and Y is non-random, indicating no regularity in the probability of drawing X or Y.

<!-- b000323 | prose | pages [12] -->
If H0 holds, based on the parity of r, there are different scenarios:

<!-- b000324 | prose | pages [12] -->
 n −1 2

<!-- b000325 | prose | pages [12] -->
P(r = 2k) =

<!-- b000326 | prose | pages [12] -->
  m−1

<!-- b000327 | prose | pages [12] -->


<!-- b000328 | prose | pages [12] -->
k −1

<!-- b000329 | prose | pages [12] -->
k −1

<!-- b000330 | prose | pages [12] -->
 n + m

<!-- b000331 | prose | pages [12] -->
; 

<!-- b000332 | prose | pages [12] -->
n

<!-- b000333 | prose | pages [12] -->
 m −1

<!-- b000334 | prose | pages [12] -->
 m −1

<!-- b000335 | prose | pages [12] -->


<!-- b000336 | prose | pages [12] -->
+

<!-- b000337 | prose | pages [12] -->
k −1

<!-- b000338 | prose | pages [12] -->
P(r = 2k + 1) =

<!-- b000339 | prose | pages [12] -->
 n −1

<!-- b000340 | prose | pages [12] -->
  n −1

<!-- b000341 | prose | pages [12] -->


<!-- b000342 | prose | pages [12] -->


<!-- b000343 | prose | pages [12] -->
+

<!-- b000344 | prose | pages [12] -->
k −1

<!-- b000345 | prose | pages [12] -->
k

<!-- b000346 | prose | pages [12] -->
k

<!-- b000347 | prose | pages [12] -->
 n + m

<!-- b000348 | prose | pages [12] -->


<!-- b000349 | prose | pages [12] -->
n

<!-- b000350 | prose | pages [12] -->
The mathematical expectation of r is E(r) = 2mn

<!-- b000351 | prose | pages [12] -->
m + n + 1, the variance of r is V (r) =

<!-- b000352 | prose | pages [12] -->
关注数学模型

<!-- b000353 | furniture | pages [12] -->
2

<!-- b000354 | furniture | pages [12] -->
MATHmodels

<!-- b000355 | furniture | pages [12] -->
获取更多资讯

<!-- b000356 | furniture | pages [13] -->
Team # 2425454

<!-- b000357 | prose | pages [13] -->
2mn(2mn −m −n)

<!-- b000358 | furniture | pages [13] -->
Page 13 of 25

<!-- b000359 | prose | pages [13] -->
, and the statisticZ constructed from the number of trips follows a normal

<!-- b000360 | prose | pages [13] -->
(m + n)2(m + n −1)

<!-- b000361 | prose | pages [13] -->
distribution, that is, Z = r −E(r)

<!-- b000362 | prose | pages [13] -->
∼N(0, 1).

<!-- b000363 | prose | pages [13] -->
p

<!-- b000364 | prose | pages [13] -->
V (R)

<!-- b000365 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000366 | prose | pages [13] -->
We recorded the outcome of each point within each game throughout the entire match. If player A won the point, it was recorded as 1, and 0 otherwise. This resulted in sequences representing the distribution of scores within each game, and runs were calculated based on this. Subsequently, a runs test was conducted for each game. The results indicated that within a 90% confidence interval, the percentage of games rejecting the null hypothesis accounted for 45.11% of the total number of games.

<!-- b000367 | prose | pages [13] -->
This suggests that scoring in a game is not completely randomized.

<!-- b000368 | prose | pages [13] -->
Scores-Momentum Contingency Analysis 6.2

<!-- b000369 | prose | pages [13] -->
"In the previous section, we employed the runs test to investigate whether the scoring sequence of opposing sides in tennis matches exhibits randomness. The result was negative,

<!-- b000370 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000371 | prose | pages [13] -->
indicating that the match dynamics are not random.

<!-- b000372 | prose | pages [13] -->
Subsequently, to explore whether the fluctuations in the game are related to momentum, we conducted a contingency table analysis on the relationship between the score of each point and the momentum of the opposing sides.

<!-- b000373 | prose | pages [13] -->
We first counted the winners and losers of each point as well as the relationship between the momentum of playerA and playerB in terms of magnitude when competing for this point, as shown in the table below:

<!-- b000374 | caption | pages [13] -->
Table 2: Score vs. Momentum Table

<!-- b000375 | prose | pages [13] -->
Player A Won the Point

<!-- b000376 | prose | pages [13] -->
MA ⩾MB n11 MA < MB n21

<!-- b000377 | prose | pages [13] -->
Player B Won the Point

<!-- b000378 | prose | pages [13] -->
n12 n22

<!-- b000379 | prose | pages [13] -->
In the table, nijrepresents the frequency with which events in row i and column j occur simultaneously, where i represents the comparison of player A’s momentum with player B’s momentum, and jrepresents the winner of the match point. Let the original hypothesis be H0, indicating that there is no correlation between score and momentum, and the alternative hypothesis be H1, indicating that there is a correlation between score and momentum.

<!-- b000380 | prose | pages [13] -->
Assuming that there is no correlation between score and momentum, for each cell in Table 1 calculate the expected frequency E.

<!-- b000381 | prose | pages [13] -->
Since the total sample with all expected frequencies is greater than 5, the conditions for using the chi-squaretest aremet. Therefore, weusedthechi-squaretest toassessthedifferencebetween the observed and expected frequencies. Taking Wimbledon as an example, the calculated chi- square statistic X = 5.566, indicating that the observed frequencies are significantly different from the expected frequencies; the significance level P = 0.018, indicating the rejection of the original hypothesis H0 at the 90% confidence level that the relationship between the winners and losers of each point and the magnitude of playerA’s and playerB’s momentum when competing for that point is correlated.

<!-- b000382 | prose | pages [13] -->
So "momentum" does play an important role in the game, and swings in play and runs of success are not random.

<!-- b000383 | prose | pages [13] -->
关注数学模型

<!-- b000384 | furniture | pages [13] -->
2

<!-- b000385 | furniture | pages [13] -->
MATHmodels

<!-- b000386 | furniture | pages [13] -->
获取更多资讯

<!-- b000387 | furniture | pages [14] -->
Team # 2425454

<!-- b000388 | furniture | pages [14] -->
Page 14 of 25

<!-- b000389 | prose | pages [14] -->
Task 3 : Identify Indicators Signaling a Change in Flow 7

<!-- b000390 | prose | pages [14] -->
7.1

<!-- b000391 | heading | pages [14] -->
GSRF Swing Predictor Model

<!-- b000392 | prose | pages [14] -->
First, we need to develop a model to predict swings in a match and look for the factors most

<!-- b000393 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000394 | prose | pages [14] -->
associated with swings.So we developed the GSRF Swing Predictor Model.

<!-- b000395 | prose | pages [14] -->
Our model needs to be able to predict whether there will be swings at s points in the future, and determine its direction accurately - whether it will be a wave in favor of the player or a swing in favor of his opponent. To do this, we first introduce the concept of ’swing reversal points’, which have two different types.

<!-- b000396 | prose | pages [14] -->
7.1.1 The Swings Reversal Point

<!-- b000397 | prose | pages [14] -->
We use the ‘scipy.signal.find_peaks‘ function in Python to locate the peaks in the curves representing the momentum changes over time for both the player and the opponent. Between the peaks of the player and opponent, we identify the point where the momentum value is closest to 0 as the "swing" reversal point.

<!-- b000398 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000399 | prose | pages [14] -->
If the peak of the opponent comes before the player’s peak, indicating the advantage is leaning towards the player, the reversal point between these two peaks is marked as a transition point favoring the player, labeled as "1". Conversely, if the player’s peak comes before the opponent’s peak, indicating the advantage is shifting towards the opponent, the point between these two peaks is marked as a reversal point favoring the opponent, labeled as "-1". Points that are not transition points are labeled as "0". The schematic representation of this process is illustrated in Figure 9.

<!-- b000400 | caption | pages [14] -->
Figure 9: Rurning Swing Points Selection Process and Schematic Diagram

<!-- b000401 | prose | pages [14] -->
We verified the method using the 2023 Wimbledon final data, and the results are good, as shown in the figure below:

<!-- b000402 | prose | pages [14] -->
关注数学模型

<!-- b000403 | furniture | pages [14] -->
2

<!-- b000404 | furniture | pages [14] -->
MATHmodels

<!-- b000405 | furniture | pages [14] -->
获取更多资讯

<!-- b000406 | furniture | pages [15] -->
Team # 2425454

<!-- b000407 | furniture | pages [15] -->
Page 15 of 25

<!-- b000408 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000409 | caption | pages [15] -->
Figure 10: GSRF Algorithm Flow Diagram

<!-- b000410 | prose | pages [15] -->
To predict swings in future matches, we take a subset of players’ on-court performance metrics and use the grid search Random Forest (GSRF)[6] algorithm to predict which of three scenarios each point in future belongs to.

<!-- b000411 | prose | pages [15] -->
Next, we will describe the selected indicator data and explain the algorithm flow.

<!-- b000412 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000413 | prose | pages [15] -->
7.1.2 The Selected Indicator

<!-- b000414 | prose | pages [15] -->
Through the given tennis dataset, we have selected two categories of indicators for prediction. One category pertains to individual player metrics, while the other involves shared metrics when the two players compete. These two categories of indicators are listed as follows:

<!-- b000415 | prose | pages [15] -->
The first category: p1_ace: Whether player 1 hits an "unreturnable" ball during the serve; p1_ace: p1 total aces; p1_break_pt: Break point: player 1 has the opportunity to win a point in opponent’s service game; p1_double_fault: Player 1 committed two faults in serving, resulting in a lost point; p1_double_fault: p1 total double faults; p1_net_pt: Player 1 approached the net in this round; p1_net_pt_won: Player 1 won the point when approaching the net in this round; p1_score: Player 1’s score in this game; p1_sets: Number of sets won by player 1; p1_unf_err: Player 1 made an unforced error in this round; p1_winner: Whether player 1 hit an "unreturnable" ball,p1_games: p1 won games; p1_points_won: p1 total points won; p1_distance_run: p1 distance run in this point; brp1: p1 break point conversion rate; p1_distance_run_total: p1 total distance run; ntp1: p1 net points won percentage.

<!-- b000416 | prose | pages [15] -->
Player 2 has exactly the same indicator type as Player 1, so it is not repeated.

<!-- b000417 | prose | pages [15] -->
The second category: elapsed_time: Duration of the point ; speed_mph: Serve speed ; rally_count: Cumulative number of hits ; rally_count: Total hits in a rally ; return_depth: Depth of returning, indicating whether the return lands near the baseline, midcourt, or frontcourt ; serve_depth: Depth of the serve, indicating whether the serve is placed in the front, mid, or backcourt of the tennis court ; serve_no: Which serve the player is in, the first or second ; serve_width: Direction of the serve ; server: Player serving.

<!-- b000418 | prose | pages [15] -->
Some of the indicators are original metrics from the dataset, while others (in bold) are derived through calculations based on the original metrics.

<!-- b000419 | prose | pages [15] -->
7.1.3

<!-- b000420 | heading | pages [15] -->
GSRF Algorithm

<!-- b000421 | prose | pages [15] -->
The GSRF algorithm consists of the Random Forest and Grid Search algorithm.

<!-- b000422 | prose | pages [15] -->
The Grid Search algorithm is a parameter optimization technique that iterates through a It trains and evaluates the model for each possible combination specified parameter grid.

<!-- b000423 | prose | pages [15] -->
关注数学模型

<!-- b000424 | furniture | pages [15] -->
2

<!-- b000425 | furniture | pages [15] -->
MATHmodels

<!-- b000426 | furniture | pages [15] -->
获取更多资讯

<!-- b000427 | furniture | pages [16] -->
Team # 2425454

<!-- b000428 | furniture | pages [16] -->
Page 16 of 25

<!-- b000429 | prose | pages [16] -->
of parameters, ultimately outputting the best parameter set along with corresponding model performance metrics.

<!-- b000430 | prose | pages [16] -->
Random Forest, is a machine learning algorithm that trains based on multiple decision trees. During training, it randomly selects a subset of features for each tree. In the classification

<!-- b000431 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000432 | prose | pages [16] -->
process, Random Forest aggregates the predicted classification results of each decision tree through averaging or voting, yielding the final result.

<!-- b000433 | prose | pages [16] -->
Unlike the regular Random Forest algorithm, the GSRF algorithm utilizes the best hy- perparameter combinations to train and predict the Random Forest model. This significantly enhances the model’s performance, mitigating issues such as overfitting or underfitting. The GSRF algorithm workflow is illustrated in Figure 11.

<!-- b000434 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000435 | caption | pages [16] -->
Figure 11: GSRF Algorithm Flow Diagram

<!-- b000436 | heading | pages [16] -->
The Predicted Swings Results of the Match

<!-- b000437 | prose | pages [16] -->
7.1.4

<!-- b000438 | prose | pages [16] -->
We utilize the aforementioned classification indicators as input parameters for the Random Forest model to predict future scenarios.

<!-- b000439 | prose | pages [16] -->
As an example, for a particular match, we split the dataset into training and testing sets in an 8:2 ratio. We employed the RandomForestRegressor algorithm from the ensemble module in the scikit-learn (sklearn) machine learning library, along with the GridSearchCV algorithm from sklearn. The optimal hyperparameter combination obtained from GridSearchCV is as follows:

<!-- b000440 | caption | pages [16] -->
Table 3: Table of Optimal Hyperparameter Combinations

<!-- b000441 | prose | pages [16] -->
min_samples_leaf Indicator Names max_depth

<!-- b000442 | prose | pages [16] -->
Values None 1

<!-- b000443 | prose | pages [16] -->
min_samples_split n_estimators

<!-- b000444 | prose | pages [16] -->
3 100

<!-- b000445 | prose | pages [16] -->
The prediction accuracy of the model is up to 94%, and the performance of the test set is also good. The confusion matrix diagram is drawn as follows:

<!-- b000446 | prose | pages [16] -->
关注数学模型

<!-- b000447 | furniture | pages [16] -->
2

<!-- b000448 | furniture | pages [16] -->
MATHmodels

<!-- b000449 | furniture | pages [16] -->
获取更多资讯

<!-- b000450 | furniture | pages [17] -->
Team # 2425454

<!-- b000451 | furniture | pages [17] -->
Page 17 of 25

<!-- b000452 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000453 | caption | pages [17] -->
Figure 12: Confusion Matrix

<!-- b000454 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000455 | prose | pages [17] -->
As can be seen from the matrix, most of the samples were correctly categorized, only 3 samples were not correctly categorized, and none of the samples from any of the reversal point types were categorized into another reversal point type.

<!-- b000456 | prose | pages [17] -->
From the random forest, we can also obtain the importance of various metrics, as shown in the following figure:

<!-- b000457 | caption | pages [17] -->
Figure 13: Bar Chart of Metric Importance

<!-- b000458 | prose | pages [17] -->
As seen in the graph above, the total score of opponents is the most relevant metric for swings in the match.

<!-- b000459 | prose | pages [17] -->
7.2

<!-- b000460 | heading | pages [17] -->
Player Performance Factor Analysis Model

<!-- b000461 | prose | pages [17] -->
The influencing factors obtained from the analysis of the GSRF Swing Predictor Model established in the previous section, which predicts the direction of the game, are complex and diverse. This complexity makes it less convenient for coaches to guide players and understand the momentum of the game. Therefore, we conducted a factor analysis[7] on the indicators that have a significant impact on "swing" to extract independent common factors, enabling players to clearly capture the factors influencing the direction of the game.

<!-- b000462 | prose | pages [17] -->
关注数学模型

<!-- b000463 | furniture | pages [17] -->
2

<!-- b000464 | furniture | pages [17] -->
MATHmodels

<!-- b000465 | furniture | pages [17] -->
获取更多资讯

<!-- b000466 | furniture | pages [18] -->
Team # 2425454

<!-- b000467 | furniture | pages [18] -->
Page 18 of 25

<!-- b000468 | prose | pages [18] -->
We selected the top 15 indicators in terms of feature importance and conducted the Kaiser- Meyer-Olkin (KMO) test and Bartlett’s test[8] using SPSS.The test results are as follows:

<!-- b000469 | caption | pages [18] -->
Table 4: Kaiser-Meyer-Olkin (KMO) and Bartlett’s Test

<!-- b000470 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000471 | prose | pages [18] -->
KMO Sampling Adequacy Measure 0.708

<!-- b000472 | prose | pages [18] -->
Approximate Chi-Square 11512.67 Degrees of Freedom

<!-- b000473 | prose | pages [18] -->
Bartlett’s Sphericity Test

<!-- b000474 | prose | pages [18] -->
105 Significance 0

<!-- b000475 | prose | pages [18] -->
According to the table, the statistic for Bartlett’s sphericity test is 11512.67, and the cor- responding probability (P-value) is 0. At a 95% significance level, the null hypothesis should be rejected, indicating a significant difference between the correlation matrix and the identity matrix. Meanwhile, the KMO value is 0.708. According to Kaiser’s standard for interpreting KMO, it suggests suitability for factor analysis, indicating factors that influence swing[9].

<!-- b000476 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000477 | prose | pages [18] -->
Next, we utilized SPSS and conducted a principal component analysis for extraction. The scree plot obtained is shown in Figure 14. It was observed that when the number of extractions reached 4, the contribution rate became quite small. Therefore, we decided to extract 4 common factors.

<!-- b000478 | caption | pages [18] -->
Figure 14: Scree plot of Principal Component Analysis

<!-- b000479 | prose | pages [18] -->
We utilized the Kaiser normalization and varimax rotation method to obtain the rotated component matrix, as shown below:

<!-- b000480 | prose | pages [18] -->
关注数学模型

<!-- b000481 | furniture | pages [18] -->
2

<!-- b000482 | furniture | pages [18] -->
MATHmodels

<!-- b000483 | furniture | pages [18] -->
获取更多资讯

<!-- b000484 | furniture | pages [19] -->
Team # 2425454

<!-- b000485 | furniture | pages [19] -->
Page 19 of 25

<!-- b000486 | caption | pages [19] -->
Table 5: The Rotated Component Matrix

<!-- b000487 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000488 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000489 | prose | pages [19] -->
Next, we analyze the four factors in the component matrix.

<!-- b000490 | prose | pages [19] -->
Factor 1 loadsheavilyonp1_pointswon, p2_pointswon, rally_count, p1_distanceruntotal, and p2_distance_run_total. It involves aspects such as shot count and running distance, rep- resenting the player’s stamina and energy expenditure during the match. We name this factor the Expenditure Factor.

<!-- b000491 | prose | pages [19] -->
Factor 2 primarily involves break point conversion rates (brp1, brp2) and net point conversion rates (ntp1, ntp2). As it can reflect the player’s technical proficiency during the match, we name it the Technical Factor.

<!-- b000492 | prose | pages [19] -->
Factor 3 loads significantly on p1_distancerun and p2_distance_run, primarily reflecting the players’ running patterns during the match, likely related to court coverage and movement tactics. We name it the Running Distance Factor.

<!-- b000493 | prose | pages [19] -->
Factor 4 loads heavily on p1_games and p2_games, mainly focusing on the players’ game situations during the match. We name it the Game Situation Factor.

<!-- b000494 | prose | pages [19] -->
The coach can provide guidance to the players by comparing the abilities of their players with those of the next opponent in these four factors.

<!-- b000495 | prose | pages [19] -->
Utilizing the Expenditure Factor, the coach can analyze the stamina gap between players and opponents, enabling targeted training for the players’ fitness levels and endurance before the match. The Technical Factor reflects a player’s technical proficiency, including break points and volleys, aiding the coach in devising more effective strategies. For instance, if a player excels

<!-- b000496 | prose | pages [19] -->
关注数学模型

<!-- b000497 | furniture | pages [19] -->
2

<!-- b000498 | furniture | pages [19] -->
MATHmodels

<!-- b000499 | furniture | pages [19] -->
获取更多资讯

<!-- b000500 | furniture | pages [20] -->
Team # 2425454

<!-- b000501 | furniture | pages [20] -->
Page 20 of 25

<!-- b000502 | prose | pages [20] -->
in volleys, encouraging them to employ net strategies more frequently could be beneficial. The Running Distance Factor is associated with court coverage and movement tactics. Coaches can optimize players’ running strategies based on these factors to enhance control over opponents and reduce self-pressure. The Game Situation Factor primarily focuses on players’ game

<!-- b000503 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000504 | prose | pages [20] -->
scores, assisting in analyzing situations and guiding players to flexibly adjust strategies during matches.

<!-- b000505 | prose | pages [20] -->
In essence, strengthening mental and physical resilience is crucial against diverse opponents, and focusing on improving break points and volley techniques gives players a substantial edge.

<!-- b000506 | heading | pages [20] -->
Task 4 : Assess the Generalization of Model

<!-- b000507 | prose | pages [20] -->
8

<!-- b000508 | prose | pages [20] -->
Generalization in women’s tennis matches 8.1

<!-- b000509 | prose | pages [20] -->
To assess the generalization of our model, we tested it in the 2023 Wimbledon Women’s Singles final. The test results are as follows:

<!-- b000510 | prose | pages [20] -->
We obtained data on the 2023 Wimbledon women’s singles final that is consistent across all

<!-- b000511 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000512 | prose | pages [20] -->
metrics with the dataset given in this question(source:https://www.wimbledon.com/index.html). Women’s tennis differs from men’s tennis matches in that two out of three sets are taken. Therefore, we modified the rules related to the relevant sets for Monte Carlo simulation to solve the real-time winning probability of the match. The calculated momentum for the whole match is shown below:

<!-- b000513 | caption | pages [20] -->
Figure 15: Wimbledon Final Real-Time Predicted Win Probability Swings Chart.The thick gray

<!-- b000514 | prose | pages [20] -->
dashed lines represent set divisions, while the thin gray dashed lines represent game divisions.

<!-- b000515 | prose | pages [20] -->
For Marketa Vondronsova, the match was a windfall.

<!-- b000516 | prose | pages [20] -->
Using the model from Task 3 again, the momentum fluctuations for this match are illustrated in the following graph:

<!-- b000517 | prose | pages [20] -->
关注数学模型

<!-- b000518 | furniture | pages [20] -->
2

<!-- b000519 | furniture | pages [20] -->
MATHmodels

<!-- b000520 | furniture | pages [20] -->
获取更多资讯

<!-- b000521 | furniture | pages [21] -->
Team # 2425454

<!-- b000522 | furniture | pages [21] -->
Page 21 of 25

<!-- b000523 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000524 | caption | pages [21] -->
Figure 16: Momentum Fluctuations and Transition Points in Fluctuations.

<!-- b000525 | prose | pages [21] -->
Similarly, the prediction of short-term NME transition points has the following results on the test set.

<!-- b000526 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000527 | caption | pages [21] -->
Figure 17: Women’s Singles Confusion Matrix

<!-- b000528 | prose | pages [21] -->
It is not difficult to find that there are fewer samples with wrong scores, indicating that the application of our model to women’s tennis matches is feasible. And the important indexes obtained by GSRF model for women’s tennis game appeared a little difference with men’s tennis game. For example, the most important factor affecting the women’s tennis game is the total distance run (as shown in Fig. 18), while the men are the total score of the opponent, which may be related to the difference in physical strength between men and women.

<!-- b000529 | caption | pages [21] -->
Figure 18: GSRF Algorithm Flow Diagram

<!-- b000530 | prose | pages [21] -->
关注数学模型

<!-- b000531 | furniture | pages [21] -->
2

<!-- b000532 | furniture | pages [21] -->
MATHmodels

<!-- b000533 | furniture | pages [21] -->
获取更多资讯

<!-- b000534 | furniture | pages [22] -->
Team # 2425454

<!-- b000535 | furniture | pages [22] -->
Page 22 of 25

<!-- b000536 | prose | pages [22] -->
Discussion on the impact of the playing surface. 8.2

<!-- b000537 | prose | pages [22] -->
Research[10] indicates that, with a consistent return speed of 100 km/h and a landing angle of 30◦, on grass, the rebound angle is approximately 36◦at a speed of about 73 km/h; on hard courts, it’s around 41◦at a speed of about 67 km/h; while on clay courts, the rebound angle is

<!-- b000538 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000539 | prose | pages [22] -->
about 44◦at a speed of about 57 km/h. Different launch angles and rebound heights are also observed.

<!-- b000540 | prose | pages [22] -->
In summary, playing surface types significantly impact the game. Athletes need to adapt their techniques and physical fitness to the surface characteristics for better performance. Studying momentum variations on different surfaces is essential.

<!-- b000541 | prose | pages [22] -->
While we believe our model is applicable across surfaces, unfortunately, we couldn’t find match data for various surfaces in the limited time, which will be part of our future work.

<!-- b000542 | prose | pages [22] -->
9

<!-- b000543 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000544 | prose | pages [22] -->
Short-term Motivation Parameter mi

<!-- b000545 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000546 | prose | pages [22] -->
The short-term motivation parameter mi was estimated by us from the dataset with some bias. We perturbed mi, (±5%, ±10%), and the calculated changes in the Wimbledon final winning percentage and momentum calculations are shown in the results in the following figure:

<!-- b000547 | caption | pages [22] -->
Figure 19: The Momentum Variation with respect to mi Graph

<!-- b000548 | caption | pages [22] -->
Figure 20: Score Quantity Sensitivity Analysis

<!-- b000549 | prose | pages [22] -->
From the above figure, it can be observed that the win rate and momentum are not sensitive to the variations in mi and remain relatively stable. From the above figure, it can be observed that the win rate and momentum are not sensitive to the variations in mi and remain relatively stable.

<!-- b000550 | prose | pages [22] -->
关注数学模型

<!-- b000551 | furniture | pages [22] -->
2

<!-- b000552 | furniture | pages [22] -->
MATHmodels

<!-- b000553 | furniture | pages [22] -->
获取更多资讯

<!-- b000554 | furniture | pages [23] -->
Team # 2425454

<!-- b000555 | furniture | pages [23] -->
Page 23 of 25

<!-- b000556 | heading | pages [23] -->
Parameters in the GSRF model: Score quantity s

<!-- b000557 | prose | pages [23] -->
In the GSRF model, the parameter is the given score quantity s, and sensitivity analysis is required. By varying the score quantity from 1 to 10, we found that the accuracy remains above 85%. We selected the top five stable indicators in terms of feature importance and plotted the

<!-- b000558 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000559 | prose | pages [23] -->
changes in their feature importance. The figure below illustrates the sensitivity to s.

<!-- b000560 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000561 | caption | pages [23] -->
Figure 21: The Win Rate as a Function of mi Graph

<!-- b000562 | prose | pages [23] -->
From the figure, it can be observed that within a short-term (i.e., not too long a score quantity), the changes in feature importance are not sensitive, indicating the robustness of the GSRF model.

<!-- b000563 | prose | pages [23] -->
10

<!-- b000564 | heading | pages [23] -->
Strength and Weakness

<!-- b000565 | prose | pages [23] -->
10.1

<!-- b000566 | heading | pages [23] -->
Strength

<!-- b000567 | prose | pages [23] -->
• For different sports, design rules for calculating win rates, incorporating key indicators to enhance the model’s applicability.

<!-- b000568 | prose | pages [23] -->
• The GSRF model demonstrates a high accuracy rate of 94% in predicting match fluctua- tions, with very few misclassified samples.

<!-- b000569 | prose | pages [23] -->
10.2

<!-- b000570 | heading | pages [23] -->
Weakness

<!-- b000571 | prose | pages [23] -->
• There hasn’t been an attempt to employ machine learning models to measure the magni- tude of changes in winning probability based on whether a match is won or lost.

<!-- b000572 | prose | pages [23] -->
11

<!-- b000573 | heading | pages [23] -->
Further Discussion

<!-- b000574 | prose | pages [23] -->
• For different sports, design rules for calculating win rates, incorporating key indicators to enhance the model’s applicability.

<!-- b000575 | prose | pages [23] -->
• Utilize the GSRF model to predict match fluctuations and the significance of indicators, providing athletes with more detailed performance improvement strategies.

<!-- b000576 | prose | pages [23] -->
关注数学模型

<!-- b000577 | furniture | pages [23] -->
2

<!-- b000578 | furniture | pages [23] -->
MATHmodels

<!-- b000579 | furniture | pages [23] -->
获取更多资讯

<!-- b000580 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000581 | prose | pages [24] -->
To:Tennis Team From:Team#2425454 Date : February 5

<!-- b000582 | prose | pages [24] -->
Dear Coach, It is my honor to present our research findings to you. In this study, we first explored the relationship between "momentum" and changes in the game situation. We then further developed models capable of predicting fluctuations in the game situation and identified key factors influencing match outcomes. Momentum refers to the psychological advantage a player gains by consecutively winning points or

<!-- b000583 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000584 | prose | pages [24] -->
matches. It provides players with a sense of control in the game, exerting pressure on opponents and increasing their likelihood of making mistakes. When players have momentum, they play more dynamically, reducing fear and inhibition, leading to a more aggressive and confident playing style. Next, let me explain how to use momentum to win more tennis matches and how to prepare players to cope with events that influence the course of tennis matches.

<!-- b000585 | prose | pages [24] -->
Taking Control from the Start The first and arguably most crucial step in gaining momentum in tennis is to have a strong start. The initial points of a match are pivotal, setting the tone for the rest of the game. Winning the early points instills confidence and control, putting pressure on your opponent. Focus on Your Footwork Footwork is another essential aspect of gaining momentum in tennis. Your movement on the court can have a significant impact on your ability to control the game. Command the Net Controlling the net is a key strategy in establishing momentum in tennis. This involves approaching the net and executing volleys and overhead shots. Being at the net forces your opponent to make powerful shots and quick decisions. Remember, momentum is fleeting and can shift in an instant. Maintaining mental resilience ensures you can seize it when it works in your favor and reclaim it when it doesn't. Mastering the art of momentum in tennis can give you a significant advantage over your opponents, leading to more victories and ultimately elevating your level of play.

<!-- b000586 | prose | pages [24] -->
Thank you for reading, as the same love tennis people, we sincerely admire the dedication and efforts of tennis players. We hope that our models and recommendations will have a positive impact on your training and competition, and help you achieve better results. If you have any more questions, feel free to email us and we'll be happy to discuss them with you.

<!-- b000587 | prose | pages [24] -->
Look forward to seeing your team achieve more victories in future competitions!

<!-- b000588 | prose | pages [24] -->
Yours Sincerely,

<!-- b000589 | prose | pages [24] -->
关注数学模型

<!-- b000590 | furniture | pages [24] -->
2

<!-- b000591 | furniture | pages [24] -->
Team #2425454

<!-- b000592 | furniture | pages [24] -->
MATHmodels

<!-- b000593 | furniture | pages [24] -->
获取更多资讯

<!-- b000594 | furniture | pages [25] -->
Team # 2425454

<!-- b000595 | heading | pages [25] -->
References

<!-- b000596 | furniture | pages [25] -->
Page 25 of 25

<!-- b000597 | references | pages [25] -->
Agnieszka M Madurska. “A set-by-set analysis method for predicting the outcome of

<!-- b000598 | references | pages [25] -->
[1]

<!-- b000599 | references | pages [25] -->
professional singles tennis matches”. In: Imperial College London, Department of Com-

<!-- b000600 | references | pages [25] -->
微信公众号：数学模型

<!-- b000601 | references | pages [25] -->
puting: London, UK (2012), pp. 1–98.

<!-- b000602 | references | pages [25] -->
Ana Šarčević;Damir Pintar;Mihaela Vranić;Ante Gojsalić. “Modeling In-Match Sports

<!-- b000603 | references | pages [25] -->
[2]

<!-- b000604 | references | pages [25] -->
DynamicsUsingtheEvolvingProbabilityMethod”. In: AppliedSciences (2021),pp.4429–

<!-- b000605 | references | pages [25] -->
4508.

<!-- b000606 | references | pages [25] -->
Jan R Magnus and Franc JGM Klaassen. “On the advantage of serving first in a tennis

<!-- b000607 | references | pages [25] -->
[3]

<!-- b000608 | references | pages [25] -->
set: four years at Wimbledon”. In: Journal of the Royal Statistical Society: Series D (The

<!-- b000609 | references | pages [25] -->
Statistician) 48.2 (1999), pp. 247–256.

<!-- b000610 | references | pages [25] -->
Karl Christoph Klauer, Thomas Jacobsen, and Gerd Migulla. “Counterfactual process-

<!-- b000611 | references | pages [25] -->
[4]

<!-- b000612 | references | pages [25] -->
ing: Test of an hierarchical correspondence model”. In: European Journal of Social

<!-- b000613 | references | pages [25] -->
Psychology 25.5 (1995), pp. 577–595.

<!-- b000614 | references | pages [25] -->
Seidl Robert;Lucey Patrick. “Live Counter-Factual Analysis in Women’s Tennis using

<!-- b000615 | references | pages [25] -->
[5]

<!-- b000616 | references | pages [25] -->
Automatic Key-Moment Detection”. In: MIT Sloan Sports Analytics Conference. (2022).

<!-- b000617 | references | pages [25] -->
微信号：MATHmodels

<!-- b000618 | references | pages [25] -->
Brandon Giles, Stephanie Kovalchik, and Machar Reid. “A machine learning approach

<!-- b000619 | references | pages [25] -->
[6]

<!-- b000620 | references | pages [25] -->
for automatic detection and classification of changes of direction from player tracking

<!-- b000621 | references | pages [25] -->
data in professional tennis”. In: Journal of sports sciences 38.1 (2020), pp. 106–113.

<!-- b000622 | references | pages [25] -->
Noora Shrestha. “Factor analysis as a tool for survey analysis”. In: American Journal of

<!-- b000623 | references | pages [25] -->
[7]

<!-- b000624 | references | pages [25] -->
Applied Mathematics and Statistics 9.1 (2021), pp. 4–11.

<!-- b000625 | references | pages [25] -->
Zhanneta Kozina et al. “General and individual factor structure of complex preparation

<!-- b000626 | references | pages [25] -->
[8]

<!-- b000627 | references | pages [25] -->
of young tennis players of 10-12 years”. In: Journal of Physical Education and Sport 20

<!-- b000628 | references | pages [25] -->
(2020), pp. 1242–1249.

<!-- b000629 | references | pages [25] -->
Shabrina Tri Asti Nasution, Devi Ayu Putri, and Thezar Fiqih Hidayat Hasibuan. “AN

<!-- b000630 | references | pages [25] -->
[9]

<!-- b000631 | references | pages [25] -->
ANALYSIS FACTOR THROUGH KAISER-MEYER-OLKIN: DISCLOSING AUDIT

<!-- b000632 | references | pages [25] -->
TENUREINBANKINGCOMPANIESLISTEDONINDONESIASTOCKEXCHANGE

<!-- b000633 | references | pages [25] -->
2019–2022”. In: Jurnal Ekonomi 12.01 (2023), pp. 1694–1700.

<!-- b000634 | references | pages [25] -->
Rod Cross. “Measurement of the speed and bounce of tennis courts”. In: Sports Technol-

<!-- b000635 | references | pages [25] -->
[10]

<!-- b000636 | references | pages [25] -->
ogy 3.2 (2010), pp. 112–120.

<!-- b000637 | references | pages [25] -->
关注数学模型

<!-- b000638 | furniture | pages [25] -->
2

<!-- b000639 | furniture | pages [25] -->
MATHmodels

<!-- b000640 | furniture | pages [25] -->
获取更多资讯

<!-- b000641 | heading | pages [26] -->
Report on Use of AI

<!-- b000642 | ai_disclosure | pages [26] -->
1. OpenAI ChatGPT(GPT 3.5 )

<!-- b000643 | ai_disclosure | pages [26] -->
Query1:<p1_games

<!-- b000644 | ai_disclosure | pages [26] -->
p1_points_won

<!-- b000645 | ai_disclosure | pages [26] -->
微信公众号：数学模型

<!-- b000646 | ai_disclosure | pages [26] -->
p1_distance_run

<!-- b000647 | ai_disclosure | pages [26] -->
brp1

<!-- b000648 | ai_disclosure | pages [26] -->
p1_distance_run

<!-- b000649 | ai_disclosure | pages [26] -->
ntp1

<!-- b000650 | ai_disclosure | pages [26] -->
p1_ace

<!-- b000651 | ai_disclosure | pages [26] -->
p1_ace

<!-- b000652 | ai_disclosure | pages [26] -->
p1_break_pt

<!-- b000653 | ai_disclosure | pages [26] -->
p1_double_fault

<!-- b000654 | ai_disclosure | pages [26] -->
p1_double_fault

<!-- b000655 | ai_disclosure | pages [26] -->
p1_net_pt

<!-- b000656 | ai_disclosure | pages [26] -->
p1_net_pt_won

<!-- b000657 | ai_disclosure | pages [26] -->
p1_score

<!-- b000658 | ai_disclosure | pages [26] -->
p1_sets

<!-- b000659 | ai_disclosure | pages [26] -->
p1_unf_err

<!-- b000660 | ai_disclosure | pages [26] -->
p1_winner

<!-- b000661 | ai_disclosure | pages [26] -->
微信号：MATHmodels

<!-- b000662 | ai_disclosure | pages [26] -->
Put this data together into a paragraph, these are the individual athlete indicators data. The first

<!-- b000663 | ai_disclosure | pages [26] -->
six of them are our own construction, meaning respectively: cumulative wins up to this point

<!-- b000664 | ai_disclosure | pages [26] -->
Cumulative total score up to this point

<!-- b000665 | ai_disclosure | pages [26] -->
The distance the point runs

<!-- b000666 | ai_disclosure | pages [26] -->
Service break rate

<!-- b000667 | ai_disclosure | pages [26] -->
Total distance run by the player up to that point

<!-- b000668 | ai_disclosure | pages [26] -->
Scoring rate near the net

<!-- b000669 | ai_disclosure | pages [26] -->
Please tidy it up for me>

<!-- b000670 | ai_disclosure | pages [26] -->
Output:<The following is a compilation of the individual metrics data you provided for

<!-- b000671 | ai_disclosure | pages [26] -->
athletes:

<!-- b000672 | ai_disclosure | pages [26] -->
p1_games: Cumulative wins up to this point

<!-- b000673 | ai_disclosure | pages [26] -->
p1_points_won: indicates the total score as of this point

<!-- b000674 | ai_disclosure | pages [26] -->
p1_distance_run: indicates the run distance of this point

<!-- b000675 | ai_disclosure | pages [26] -->
brp1: Break rate

<!-- b000676 | ai_disclosure | pages [26] -->
p1_distance_run: The total distance run by the player up to this point

<!-- b000677 | ai_disclosure | pages [26] -->
ntp1: near net scoring rate

<!-- b000678 | ai_disclosure | pages [26] -->
p1_ace: indicates the total number of ACES

<!-- b000679 | ai_disclosure | pages [26] -->
p1_break_pt: Total break points

<!-- b000680 | ai_disclosure | pages [26] -->
p1_double_fault: indicates the total number of double errors

<!-- b000681 | ai_disclosure | pages [26] -->
p1_net_pt: indicates the total number of online accesses

<!-- b000682 | ai_disclosure | pages [26] -->
p1_net_pt_won: indicates the total number of Internet access scores

<!-- b000683 | ai_disclosure | pages [26] -->
p1_score: indicates the total score

<!-- b000684 | ai_disclosure | pages [26] -->
p1_sets: indicates the total number of disks

<!-- b000685 | ai_disclosure | pages [26] -->
p1_unf_err: Total number of unforced errors

<!-- b000686 | ai_disclosure | pages [26] -->
p1_winner: Total number of winning points

<!-- b000687 | ai_disclosure | pages [26] -->
Note that "p1_distance_run" appears twice, if this is an error, please provide the correct variable

<!-- b000688 | ai_disclosure | pages [26] -->
name.>

<!-- b000689 | ai_disclosure | pages [26] -->
2. OpenAI ChatGPT(GPT 3.5.)

<!-- b000690 | ai_disclosure | pages [26] -->
Query1:<Please provide me with suggestions for modification>

<!-- b000691 | ai_disclosure | pages [26] -->
Output:<I changed "p1_distance_run" to "p_distance_run_total" to distinguish it from

<!-- b000692 | ai_disclosure | pages [26] -->
"p_distance_run". If this is still a problem, provide the correct variable name.>

<!-- b000693 | ai_disclosure | pages [26] -->
3. OpenAI ChatGPT(GPT 3.5)

<!-- b000694 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b000695 | furniture | pages [26] -->
2

<!-- b000696 | furniture | pages [26] -->
MATHmodels

<!-- b000697 | furniture | pages [26] -->
获取更多资讯

<!-- b000698 | ai_disclosure | pages [27] -->
Query1:<The model built needs to be able to predict whether a "swing" will occur at s points

<!-- b000699 | ai_disclosure | pages [27] -->
in the future and its direction - whether it will be a swing in favor of the athlete or a swing in

<!-- b000700 | ai_disclosure | pages [27] -->
favor of his opponent. To do this, we first defined three possible scenarios for each point and the

<!-- b000701 | ai_disclosure | pages [27] -->
concept of swing turning points.>

<!-- b000702 | ai_disclosure | pages [27] -->
Output:<Your description is already quite clear, but if you'd like a refined version, you might

<!-- b000703 | ai_disclosure | pages [27] -->
微信公众号：数学模型

<!-- b000704 | ai_disclosure | pages [27] -->
consider the following expression:

<!-- b000705 | ai_disclosure | pages [27] -->
"Our model aims to predict whether there will be 'fluctuations' in s future points of a match and

<!-- b000706 | ai_disclosure | pages [27] -->
accurately determine their direction—whether they favor the athlete or their opponent. To

<!-- b000707 | ai_disclosure | pages [27] -->
achieve this, we have clearly defined three possible scenarios for each point and introduced the

<!-- b000708 | ai_disclosure | pages [27] -->
concept of a 'fluctuation turning point.'">

<!-- b000709 | ai_disclosure | pages [27] -->
4. OpenAI ChatGPT(GPT 3.5)

<!-- b000710 | ai_disclosure | pages [27] -->
Query1:<What does rally mean in tennis>

<!-- b000711 | ai_disclosure | pages [27] -->
Output:<In tennis, "rally" refers to the continuous exchange of shots between two or more

<!-- b000712 | ai_disclosure | pages [27] -->
players. During a match, players engage in a back-and-forth of hitting the ball, responding to each

<!-- b000713 | ai_disclosure | pages [27] -->
other's serves and returns, forming a coherent sequence of shots. This continuous exchange of

<!-- b000714 | ai_disclosure | pages [27] -->
shots typically takes place in different areas of the court until one player fails to return the

<!-- b000715 | ai_disclosure | pages [27] -->
opponent's shot or makes an error. "Rally" reflects the intense competition and the application of

<!-- b000716 | ai_disclosure | pages [27] -->
skills and tactics in a tennis match, making it a common element of the game.>

<!-- b000717 | ai_disclosure | pages [27] -->
微信号：MATHmodels

<!-- b000718 | ai_disclosure | pages [27] -->
5. OpenAI ChatGPT(GPT 3.5)

<!-- b000719 | ai_disclosure | pages [27] -->
Query1:<What can you call a model that predicts swings in the match based on GSRF>

<!-- b000720 | ai_disclosure | pages [27] -->
Output:<1. **GSRF Swing Predictor Model**

<!-- b000721 | ai_disclosure | pages [27] -->
2. **Match Dynamics Forecasting with GSRF**

<!-- b000722 | ai_disclosure | pages [27] -->
3. **OptiSwing Model Powered by GSRF**

<!-- b000723 | ai_disclosure | pages [27] -->
4. **GSRF Momentum Forecast Model**

<!-- b000724 | ai_disclosure | pages [27] -->
5. **PrecisionSwing: A GSRF-based Model**

<!-- b000725 | ai_disclosure | pages [27] -->
When choosing a name, make sure it clearly conveys the model's purpose and the features based

<!-- b000726 | ai_disclosure | pages [27] -->
on GSRF, highlighting the functionality and advantages of the model.>

<!-- b000727 | ai_disclosure | pages [27] -->
6. OpenAI ChatGPT(GPT 3.5)

<!-- b000728 | ai_disclosure | pages [27] -->
Query1:<What are the characteristics and norms of memo writing>

<!-- b000729 | ai_disclosure | pages [27] -->
Output:<The writing of a memo should have the following characteristics and guidelines:

<!-- b000730 | ai_disclosure | pages [27] -->
1. **Conciseness:** Memos should be brief and to the point, avoiding lengthy and unnecessary

<!-- b000731 | ai_disclosure | pages [27] -->
details. Information should be presented directly, enabling readers to quickly grasp the main

<!-- b000732 | ai_disclosure | pages [27] -->
content.

<!-- b000733 | ai_disclosure | pages [27] -->
2. **Clarity and Specificity:** Memos should be clear and specific in conveying information.

<!-- b000734 | ai_disclosure | pages [27] -->
Avoid ambiguity and provide details that help readers understand the purpose and context of the

<!-- b000735 | ai_disclosure | pages [27] -->
memo.

<!-- b000736 | ai_disclosure | pages [27] -->
3. **Structured Format:** Memos typically follow a structured format, including headings such

<!-- b000737 | ai_disclosure | pages [27] -->
as "To," "From," "Date," and "Subject." This format helps organize information and makes it easy

<!-- b000738 | ai_disclosure | pages [27] -->
for readers to locate key details.

<!-- b000739 | ai_disclosure | pages [27] -->
4. **Professional Tone:** Maintain a professional and formal tone in memo writing. Use clear

<!-- b000740 | ai_disclosure | pages [27] -->
language and avoid slang or overly casual expressions.

<!-- b000741 | ai_disclosure | pages [27] -->
5. **Actionable Content:** If applicable, include actionable items or recommendations in the

<!-- b000742 | ai_disclosure | pages [27] -->
memo. Clearly state what actions, if any, need to be taken by the recipients.

<!-- b000743 | ai_disclosure | pages [27] -->
6. **Relevance:** Ensure that the content of the memo is relevant to the recipients and pertains

<!-- b000744 | ai_disclosure | pages [27] -->
to the subject at hand. Avoid including unnecessary information that may distract from the main

<!-- b000745 | ai_disclosure | pages [27] -->
message.

<!-- b000746 | ai_disclosure | pages [27] -->
关注数学模型

<!-- b000747 | furniture | pages [27] -->
2

<!-- b000748 | furniture | pages [27] -->
MATHmodels

<!-- b000749 | furniture | pages [27] -->
获取更多资讯

<!-- b000750 | ai_disclosure | pages [28] -->
7. **Correct Grammar and Spelling:** Check and double-check for proper grammar, punctuation,

<!-- b000751 | ai_disclosure | pages [28] -->
and spelling. Memos should be error-free to convey professionalism and attention to detail.

<!-- b000752 | ai_disclosure | pages [28] -->
8. **Date and Reference:** Include the date of the memo and any relevant references or

<!-- b000753 | ai_disclosure | pages [28] -->
attachments. This helps provide context and allows for easy cross-referencing.

<!-- b000754 | ai_disclosure | pages [28] -->
微信公众号：数学模型

<!-- b000755 | ai_disclosure | pages [28] -->
9. **Audience Consideration:** Tailor the memo to the specific audience, considering their

<!-- b000756 | ai_disclosure | pages [28] -->
background, knowledge, and needs. This ensures that the information is presented in a way that

<!-- b000757 | ai_disclosure | pages [28] -->
resonates with the recipients.>

<!-- b000758 | ai_disclosure | pages [28] -->
7. OpenAI ChatGPT(GPT 3.5)

<!-- b000759 | ai_disclosure | pages [28] -->
Query1:<Format cloth>

<!-- b000760 | ai_disclosure | pages [28] -->
Output:<The format of a memo typically includes the following elements:

<!-- b000761 | ai_disclosure | pages [28] -->
1. **Header Information:**

<!-- b000762 | ai_disclosure | pages [28] -->
- Date: The date of the memo.

<!-- b000763 | ai_disclosure | pages [28] -->
- To: The primary recipient of the memo.

<!-- b000764 | ai_disclosure | pages [28] -->
- From: The author of the memo.

<!-- b000765 | ai_disclosure | pages [28] -->
- Subject: The subject or purpose of the memo.

<!-- b000766 | ai_disclosure | pages [28] -->
微信号：MATHmodels

<!-- b000767 | ai_disclosure | pages [28] -->
Example:

<!-- b000768 | ai_disclosure | pages [28] -->
```

<!-- b000769 | ai_disclosure | pages [28] -->
Date: [Date]

<!-- b000770 | ai_disclosure | pages [28] -->
To: [Recipient]

<!-- b000771 | ai_disclosure | pages [28] -->
From: [Author]

<!-- b000772 | ai_disclosure | pages [28] -->
Subject: [Subject]

<!-- b000773 | ai_disclosure | pages [28] -->
```

<!-- b000774 | ai_disclosure | pages [28] -->
2. **Introduction (Opening Paragraph):**

<!-- b000775 | ai_disclosure | pages [28] -->
- Briefly introduce the purpose and background of the memo.

<!-- b000776 | ai_disclosure | pages [28] -->
- Provide an overview to let the reader know the main content of the memo.

<!-- b000777 | ai_disclosure | pages [28] -->
Example:

<!-- b000778 | ai_disclosure | pages [28] -->
```

<!-- b000779 | ai_disclosure | pages [28] -->
Dear [Recipient],

<!-- b000780 | ai_disclosure | pages [28] -->
I am writing to [Purpose]. This memo outlines [Overview].

<!-- b000781 | ai_disclosure | pages [28] -->
```

<!-- b000782 | ai_disclosure | pages [28] -->
3. **Body:**

<!-- b000783 | ai_disclosure | pages [28] -->
- Paragraphs elaborating on the main content, ensuring logical flow.

<!-- b000784 | ai_disclosure | pages [28] -->
- Use headings, numbering, or other formatting to emphasize important information.

<!-- b000785 | ai_disclosure | pages [28] -->
Example:

<!-- b000786 | ai_disclosure | pages [28] -->
```

<!-- b000787 | ai_disclosure | pages [28] -->
1. Overview

<!-- b000788 | ai_disclosure | pages [28] -->
[Content]

<!-- b000789 | ai_disclosure | pages [28] -->
2. Recommendations

<!-- b000790 | ai_disclosure | pages [28] -->
[Content]

<!-- b000791 | ai_disclosure | pages [28] -->
```

<!-- b000792 | ai_disclosure | pages [28] -->
4. **Conclusion:**

<!-- b000793 | ai_disclosure | pages [28] -->
- Summarize the main points or recommendations of the memo.

<!-- b000794 | ai_disclosure | pages [28] -->
- Emphasize expected actions or decisions.

<!-- b000795 | ai_disclosure | pages [28] -->
Example:

<!-- b000796 | ai_disclosure | pages [28] -->
```

<!-- b000797 | ai_disclosure | pages [28] -->
关注数学模型

<!-- b000798 | furniture | pages [28] -->
2

<!-- b000799 | furniture | pages [28] -->
MATHmodels

<!-- b000800 | furniture | pages [28] -->
获取更多资讯

<!-- b000801 | ai_disclosure | pages [29] -->
In conclusion, [Summarize points/recommendations]. I recommend [Specific

<!-- b000802 | ai_disclosure | pages [29] -->
recommendations].

<!-- b000803 | ai_disclosure | pages [29] -->
```

<!-- b000804 | ai_disclosure | pages [29] -->
5. **Appendix or Supplementary Information (if needed):**

<!-- b000805 | ai_disclosure | pages [29] -->
微信公众号：数学模型

<!-- b000806 | ai_disclosure | pages [29] -->
- Include additional data, charts, images, etc., to support main points.

<!-- b000807 | ai_disclosure | pages [29] -->
Example:

<!-- b000808 | ai_disclosure | pages [29] -->
```

<!-- b000809 | ai_disclosure | pages [29] -->
Appendix A: [Additional Information Title]

<!-- b000810 | ai_disclosure | pages [29] -->
[Content]

<!-- b000811 | ai_disclosure | pages [29] -->
```

<!-- b000812 | ai_disclosure | pages [29] -->
6. **Closing Remarks:**

<!-- b000813 | ai_disclosure | pages [29] -->
- Conclude the memo, thanking the reader for their time.

<!-- b000814 | ai_disclosure | pages [29] -->
- Provide further contact information for discussions regarding any questions or concerns.

<!-- b000815 | ai_disclosure | pages [29] -->
Example:

<!-- b000816 | ai_disclosure | pages [29] -->
```

<!-- b000817 | ai_disclosure | pages [29] -->
Thank you for your attention to this matter. If you have any questions or concerns, please feel

<!-- b000818 | ai_disclosure | pages [29] -->
微信号：MATHmodels

<!-- b000819 | ai_disclosure | pages [29] -->
free to contact me at [Contact Information].

<!-- b000820 | ai_disclosure | pages [29] -->
```

<!-- b000821 | ai_disclosure | pages [29] -->
7. **Signature:**

<!-- b000822 | ai_disclosure | pages [29] -->
- Provide the author's signature and position.

<!-- b000823 | ai_disclosure | pages [29] -->
Example:

<!-- b000824 | ai_disclosure | pages [29] -->
```

<!-- b000825 | ai_disclosure | pages [29] -->
Sincerely,

<!-- b000826 | ai_disclosure | pages [29] -->
[Signature]

<!-- b000827 | ai_disclosure | pages [29] -->
[Position]

<!-- b000828 | ai_disclosure | pages [29] -->
```

<!-- b000829 | ai_disclosure | pages [29] -->
Ensure the overall layout of the memo is clear, use concise language to ensure readers can

<!-- b000830 | ai_disclosure | pages [29] -->
quickly understand and take necessary actions.>

<!-- b000831 | ai_disclosure | pages [29] -->
8. OpenAI ChatGPT(GPT 3.5)

<!-- b000832 | ai_disclosure | pages [29] -->
Query1:<To show the fluctuation data of a game, where can you find such data>

<!-- b000833 | ai_disclosure | pages [29] -->
Output:<To showcase fluctuations in a game through data, you can obtain real-time data from

<!-- b000834 | ai_disclosure | pages [29] -->
various sources. Here are some common data sources:

<!-- b000835 | ai_disclosure | pages [29] -->
1. **Official Sports League Websites:** Most sports leagues provide real-time match data on

<!-- b000836 | ai_disclosure | pages [29] -->
their official websites, such as the NBA, NFL, soccer leagues, etc. These websites typically offer

<!-- b000837 | ai_disclosure | pages [29] -->
scores, statistics, and real-time updates on the progress of the game.

<!-- b000838 | ai_disclosure | pages [29] -->
2. **Sports News Websites and Apps:** Sports news websites and apps often provide real-time

<!-- b000839 | ai_disclosure | pages [29] -->
match updates and statistical data. Platforms like ESPN, CBS Sports, Yahoo Sports, etc., are

<!-- b000840 | ai_disclosure | pages [29] -->
common sports news sources offering real-time scores, player statistics, and more.

<!-- b000841 | ai_disclosure | pages [29] -->
3. **Professional Data Providers:** Some professional sports data providers, such as Sportradar,

<!-- b000842 | ai_disclosure | pages [29] -->
Stats Perform, etc., offer comprehensive real-time sports data services. These companies cater to

<!-- b000843 | ai_disclosure | pages [29] -->
media, betting companies, and other organizations, and may provide APIs for developers.

<!-- b000844 | ai_disclosure | pages [29] -->
4. **Broadcasting Platforms:** On official or affiliated broadcasting platforms for certain sports

<!-- b000845 | ai_disclosure | pages [29] -->
events, you can find real-time match data. This may include live commentary, score statistics, and

<!-- b000846 | ai_disclosure | pages [29] -->
other information.

<!-- b000847 | ai_disclosure | pages [29] -->
5. **Social Media:** Social media platforms, especially Twitter, can be a source of real-time game

<!-- b000848 | ai_disclosure | pages [29] -->
关注数学模型

<!-- b000849 | furniture | pages [29] -->
2

<!-- b000850 | furniture | pages [29] -->
MATHmodels

<!-- b000851 | furniture | pages [29] -->
获取更多资讯

<!-- b000852 | ai_disclosure | pages [30] -->
data. Official sports accounts, reporters, teams, and players often provide live updates during

<!-- b000853 | ai_disclosure | pages [30] -->
matches.

<!-- b000854 | ai_disclosure | pages [30] -->
Regardless of the data source you choose, ensure that the data is reliable, updated in real-time,

<!-- b000855 | ai_disclosure | pages [30] -->
and aligns with the information you want to convey. Some data sources may require registration

<!-- b000856 | ai_disclosure | pages [30] -->
微信公众号：数学模型

<!-- b000857 | ai_disclosure | pages [30] -->
or the use of API keys for data access. When using such data, adhere to relevant usage

<!-- b000858 | ai_disclosure | pages [30] -->
agreements and legal regulations.>

<!-- b000859 | ai_disclosure | pages [30] -->
9. OpenAI ChatGPT(GPT 3.5)

<!-- b000860 | ai_disclosure | pages [30] -->
Query1:<Run analysis of the sequence of the scoring order of the opposing teams

<!-- b000861 | ai_disclosure | pages [30] -->
What can we call this section>

<!-- b000862 | ai_disclosure | pages [30] -->
Output:<The title for this section can be "Sequential Run-Length Analysis of Match Scores in

<!-- b000863 | ai_disclosure | pages [30] -->
Tennis." This title explicitly expresses the theme of the section, involving a run-length analysis of

<!-- b000864 | ai_disclosure | pages [30] -->
the sequential scores of opposing sides in tennis matches to gain insights into scoring patterns

<!-- b000865 | ai_disclosure | pages [30] -->
and trends during the game.>

<!-- b000866 | ai_disclosure | pages [30] -->
10. OpenAI ChatGPT(GPT 3.5)

<!-- b000867 | ai_disclosure | pages [30] -->
Query1:<

<!-- b000868 | ai_disclosure | pages [30] -->
Counterfactual frameworks are often used to estimate the impact of an event on an outcome. In

<!-- b000869 | ai_disclosure | pages [30] -->
微信号：MATHmodels

<!-- b000870 | ai_disclosure | pages [30] -->
tennis, it is possible to quantify the impact of each shot on the outcome of a match by

<!-- b000871 | ai_disclosure | pages [30] -->
introducing leverage.

<!-- b000872 | ai_disclosure | pages [30] -->
What can the section be called>

<!-- b000873 | ai_disclosure | pages [30] -->
Output:<The title for this section can be "Leverage Analysis in Tennis: Quantifying the Impact

<!-- b000874 | ai_disclosure | pages [30] -->
of Each Point." This title explicitly conveys the theme of the section, involving the analysis of the

<!-- b000875 | ai_disclosure | pages [30] -->
potential impact of each point on the match outcome using a counterfactual framework and the

<!-- b000876 | ai_disclosure | pages [30] -->
concept of leverage.>

<!-- b000877 | ai_disclosure | pages [30] -->
11. OpenAI ChatGPT(GPT 3.5)

<!-- b000878 | ai_disclosure | pages [30] -->
Query1:<What are the game statistics for all the games prior to the game the player is

<!-- b000879 | ai_disclosure | pages [30] -->
currently competing in>

<!-- b000880 | ai_disclosure | pages [30] -->
Output:<The data encompassing a player's performance in all the preceding matches before

<!-- b000881 | ai_disclosure | pages [30] -->
the current one is commonly referred to as "Pre-match Data" or "Historical Data." This

<!-- b000882 | ai_disclosure | pages [30] -->
incorporates a player's previous performances, including scoring, assists, goal differentials, and

<!-- b000883 | ai_disclosure | pages [30] -->
other relevant statistics. Such data holds significant reference value for analyzing and predicting a

<!-- b000884 | ai_disclosure | pages [30] -->
player's performance in the current match.>

<!-- b000885 | ai_disclosure | pages [30] -->
12. OpenAI ChatGPT(GPT 3.5)

<!-- b000886 | ai_disclosure | pages [30] -->
Query1:<Short term Motivation and Confidence Boost What can this bar be called for an

<!-- b000887 | ai_disclosure | pages [30] -->
increase in the scoring rate of the serve>

<!-- b000888 | ai_disclosure | pages [30] -->
Output:<This section can be titled "Impact of Short-term Motivation and Confidence Boost on

<!-- b000889 | ai_disclosure | pages [30] -->
Serve Success Rate," highlighting the influence of short-term motivation and confidence

<!-- b000890 | ai_disclosure | pages [30] -->
enhancement on the success rate of serves.>

<!-- b000891 | ai_disclosure | pages [30] -->
13. OpenAI ChatGPT(GPT 3.5)

<!-- b000892 | ai_disclosure | pages [30] -->
Query1:<momentum>

<!-- b000893 | ai_disclosure | pages [30] -->
Output:<The term "Momentum" has different definitions in various fields. Here are some

<!-- b000894 | ai_disclosure | pages [30] -->
common meanings:

<!-- b000895 | ai_disclosure | pages [30] -->
1. **Physics:** In physics, momentum is a property of an object in motion, defined as the

<!-- b000896 | ai_disclosure | pages [30] -->
product of its mass and velocity. It is a conserved quantity in a conservative system, meaning that

<!-- b000897 | ai_disclosure | pages [30] -->
in the absence of external forces, the total momentum of a system remains constant.

<!-- b000898 | ai_disclosure | pages [30] -->
2. **Financial Markets:** In the financial domain, momentum is often used to describe the trend

<!-- b000899 | ai_disclosure | pages [30] -->
of asset prices. Momentum in asset prices refers to the rate of change over a period, typically

<!-- b000900 | ai_disclosure | pages [30] -->
expressed as a percentage change or return over a specific time frame.

<!-- b000901 | ai_disclosure | pages [30] -->
关注数学模型

<!-- b000902 | furniture | pages [30] -->
2

<!-- b000903 | furniture | pages [30] -->
MATHmodels

<!-- b000904 | furniture | pages [30] -->
获取更多资讯

<!-- b000905 | ai_disclosure | pages [31] -->
3. **Business and Management:** In business and management, momentum might refer to the

<!-- b000906 | ai_disclosure | pages [31] -->
competitive strength and growth trajectory of an organization or company in the market. A

<!-- b000907 | ai_disclosure | pages [31] -->
company with positive momentum in the market suggests continuous success in sales, market

<!-- b000908 | ai_disclosure | pages [31] -->
share, or innovation.

<!-- b000909 | ai_disclosure | pages [31] -->
微信公众号：数学模型

<!-- b000910 | ai_disclosure | pages [31] -->
4. **Sports:** In sports, momentum is commonly used to describe the performance trend of a

<!-- b000911 | ai_disclosure | pages [31] -->
team or athlete during a game. A player or team with momentum is considered to have a

<!-- b000912 | ai_disclosure | pages [31] -->
continuous string of success in the competition.

<!-- b000913 | ai_disclosure | pages [31] -->
In essence, "Momentum" signifies a trend or development in a particular direction. Its

<!-- b000914 | ai_disclosure | pages [31] -->
interpretation may vary depending on the context in which it is used.>

<!-- b000915 | ai_disclosure | pages [31] -->
14. OpenAI ChatGPT(GPT 3.5)

<!-- b000916 | ai_disclosure | pages [31] -->
Query1:<leverage>

<!-- b000917 | ai_disclosure | pages [31] -->
Output:<"Leverage" is a financial and economic term commonly used to describe the practice

<!-- b000918 | ai_disclosure | pages [31] -->
of borrowing or using debt capital to increase investment returns. In the realms of investment

<!-- b000919 | ai_disclosure | pages [31] -->
and finance, leverage can enhance returns, but it also amplifies risks. Leverage can be achieved

<!-- b000920 | ai_disclosure | pages [31] -->
through debt financing, derivatives, and other means with the goal of increasing the rate of

<!-- b000921 | ai_disclosure | pages [31] -->
return on an investment.

<!-- b000922 | ai_disclosure | pages [31] -->
微信号：MATHmodels

<!-- b000923 | ai_disclosure | pages [31] -->
Moreover, in different contexts, "leverage" can also be used to describe the concept of achieving

<!-- b000924 | ai_disclosure | pages [31] -->
greater effects through technical or strategic means, such as in the business context of "strategic

<!-- b000925 | ai_disclosure | pages [31] -->
leverage." In the sports domain, "leverage" may refer to the tactics or strategies employed during

<!-- b000926 | ai_disclosure | pages [31] -->
a game to achieve better results. In different contexts, the term may carry slightly different

<!-- b000927 | ai_disclosure | pages [31] -->
meanings.>

<!-- b000928 | ai_disclosure | pages [31] -->
15. OpenAI ChatGPT(GPT 3.5)

<!-- b000929 | ai_disclosure | pages [31] -->
Query1:<When an athlete is good in a game we call it hothand, but what can you call an

<!-- b000930 | ai_disclosure | pages [31] -->
athlete's state over time>

<!-- b000931 | ai_disclosure | pages [31] -->
Output:<Over an extended period, a player's performance is commonly referred to as their

<!-- b000932 | ai_disclosure | pages [31] -->
"steady state" or "long-term performance." The term contrasting with "hothand" might be

<!-- b000933 | ai_disclosure | pages [31] -->
"coldhand," used to describe a state of consistently poor or unstable performance over the long

<!-- b000934 | ai_disclosure | pages [31] -->
term. Both terms are often employed to characterize the performance trends of athletes in

<!-- b000935 | ai_disclosure | pages [31] -->
games. It is essential to note, however, that these terms can be contentious at times, as in sports

<!-- b000936 | ai_disclosure | pages [31] -->
psychology, it is sometimes challenging to substantiate whether these phenomena truly exist.>

<!-- b000937 | ai_disclosure | pages [31] -->
16. OpenAI ChatGPT(GPT 3.5)

<!-- b000938 | ai_disclosure | pages [31] -->
Query1:<A tennis coach is skeptical that “momentum” plays any role in the match. Instead,

<!-- b000939 | ai_disclosure | pages [31] -->
he

<!-- b000940 | ai_disclosure | pages [31] -->
postulates that swings in play and runs of success by one player are random. Use your

<!-- b000941 | ai_disclosure | pages [31] -->
model/metric to assess this claim.

<!-- b000942 | ai_disclosure | pages [31] -->
What is the opposite of this coach's view>

<!-- b000943 | ai_disclosure | pages [31] -->
Output:<The opposite viewpoint to the tennis coach's skepticism about the role of

<!-- b000944 | ai_disclosure | pages [31] -->
"momentum" in the match would be the belief that "momentum" does indeed play a significant

<!-- b000945 | ai_disclosure | pages [31] -->
role in the game. This opposing perspective suggests that swings in play and runs of success by

<!-- b000946 | ai_disclosure | pages [31] -->
one player are not entirely random but are influenced by momentum, which could be attributed

<!-- b000947 | ai_disclosure | pages [31] -->
to various factors such as confidence, skill, or psychological aspects affecting player

<!-- b000948 | ai_disclosure | pages [31] -->
performance.>

<!-- b000949 | ai_disclosure | pages [31] -->
17. OpenAI ChatGPT(GPT 3.5)

<!-- b000950 | ai_disclosure | pages [31] -->
Query1:<What can I call the chapter that uses contingency tables to analyze the relationship

<!-- b000951 | ai_disclosure | pages [31] -->
between score and momentum>

<!-- b000952 | ai_disclosure | pages [31] -->
Output:<This section can be titled either "Correlation Analysis of Scores and Momentum" or

<!-- b000953 | ai_disclosure | pages [31] -->
"Contingency Table Analysis of Scores and Momentum.">

<!-- b000954 | ai_disclosure | pages [31] -->
关注数学模型

<!-- b000955 | furniture | pages [31] -->
2

<!-- b000956 | furniture | pages [31] -->
MATHmodels

<!-- b000957 | furniture | pages [31] -->
获取更多资讯
