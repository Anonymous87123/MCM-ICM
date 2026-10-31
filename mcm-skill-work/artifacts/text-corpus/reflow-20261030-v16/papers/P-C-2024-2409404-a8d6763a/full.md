# P-C-2024-2409404-a8d6763a

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
2409404

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Riding the Momentum

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
"If you have momentum, you want to try to keep that momentum going, keep that conﬁdence rolling for you. You know, that’s why the streak is there," said Djokovis. Undoubtedly, momen- tum is the key to success for Djokovic. Does momentum effectively function? To effectively tackle this inquiry and offer valuable guidance to coaches and players, we present the fol- lowing thoughts.

<!-- b000012 | prose | pages [1] -->
For task one, it is necessary to capture the ﬂow of play and identify crucial moments while also quantifying the player’s performance. We establish the Momentum Quantiza- tion Model Based on Sliding Windows (MQ-SW) that assesses the performance level of each player at given moments, taking into account the inﬂuence of past mistakes and other factors. Additionally, we incorporate the player’s serving advantage into the calculation. Furthermore, we discern the crucial aspects of the match by considering both the tennis regulations and the CUSUM algorithm. Figure 4 depicts the visual representation of the match progression between Carlos Alcaraz and Novak Djokovic. The model demonstrates

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
proﬁciency in quantifying a player’s momentum and precisely identifying crucial moments.

<!-- b000015 | prose | pages [1] -->
For task two, we need to examine the impact of "momentum" on the game and deter- mine if the ﬂuctuations in the game condition and successive player scores are random. Thus, we begin by examining the volatility of the game’s condition using the Point Vic- tor factor and the MQ-SW Model. Subsequently, we employ the Runs Test to assess the state of the game and the successive scores of the participants. Upon computation, the p −value < 0.01, indicating that the variability in the game scenario. Next, we discretize the momentum of both players at each instance and employ the Chi-square Test to com- pare the aforementioned indices. The experimental p −value < 0.01, indicating that the "momentum" element is highly likely to be the reason, as demonstrated in Table 5.

<!-- b000016 | prose | pages [1] -->
For task three, we need to predict the volatility of the circumstances in a tennis match. The dependent variable is the discretized "momentum", whereas the independent variables consist of other factors associated with players. We established the Prediction for Match Trend Model Based on PCA&XGBoost (PMT-PX). The model uses the principal compo- nent analysis to examine the variation in scatter on a two-dimensional coordinate graph and subsequently utilizes XGBoost to train on the match data. From this, we have identi- ﬁed the most signiﬁcant inﬂuencing factors, namely "Point Victor" and "Break PT" at the current moment. The corresponding scores are displayed in Table 6.

<!-- b000017 | prose | pages [1] -->
For task four, it requires an examination of the model’s effect and its capacity to general- ize. We assess the model using several metrics, such as the confusion matrix, classiﬁcation report, and ROC curve. The area under the curve (AUC) is 0.75, indicating a discernible ef- fect. We utilize the model to evaluate the U.S. Open women’s ﬁnal. The results indicate that the model exhibits a commendable level of generalization and is capable of efﬁciently and accurately identifying the target. Simultaneously, we conduct an analysis of the model’s drawbacks and provide the elements that should be taken into account in the future. Fur- thermore, the model sensitivity analysis is conducted by altering the dimensions of the sliding window along with the additional advantage parameter of the player’s serve. The outcomes indicate that the model exhibits a high level of robustness.

<!-- b000018 | prose | pages [1] -->
We ﬁnally write a memorandum, including our model and strategy, for the coaches and players. We hope our memorandum can be valuable to them and actually help them.

<!-- b000019 | keywords | pages [1] -->
Keywords: Momentum, MQ-SW, Runs Test, Chi-square Test, PMT-PX

<!-- b000020 | prose | pages [1] -->
关注数学模型

<!-- b000021 | furniture | pages [1] -->
2

<!-- b000022 | furniture | pages [1] -->
MATHmodels

<!-- b000023 | furniture | pages [1] -->
获取更多资讯

<!-- b000024 | furniture | pages [2] -->
Team # 2409404

<!-- b000025 | furniture | pages [2] -->
Page 2 of 25

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1 Introduction

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
1.1

<!-- b000030 | contents | pages [2] -->
Probelm Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
3

<!-- b000032 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000033 | contents | pages [2] -->
1.2

<!-- b000034 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
3

<!-- b000036 | contents | pages [2] -->
1.3

<!-- b000037 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
4

<!-- b000039 | contents | pages [2] -->
1.4

<!-- b000040 | contents | pages [2] -->
Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000043 | contents | pages [2] -->
5

<!-- b000044 | contents | pages [2] -->
2.1

<!-- b000045 | contents | pages [2] -->
Assumptions and Explanations . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
5

<!-- b000047 | contents | pages [2] -->
2.2

<!-- b000048 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
5

<!-- b000050 | contents | pages [2] -->
2.3

<!-- b000051 | contents | pages [2] -->
Data Preparation

<!-- b000052 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
5

<!-- b000054 | contents | pages [2] -->
2.3.1

<!-- b000055 | contents | pages [2] -->
Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
5

<!-- b000057 | contents | pages [2] -->
2.3.2

<!-- b000058 | contents | pages [2] -->
Data Pre-processing

<!-- b000059 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
6

<!-- b000061 | contents | pages [2] -->
3 Establish the Momentum Quantization Model Based on Sliding Windows

<!-- b000062 | contents | pages [2] -->
6

<!-- b000063 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000064 | contents | pages [2] -->
3.1

<!-- b000065 | contents | pages [2] -->
Quantization of Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
6

<!-- b000067 | contents | pages [2] -->
3.2

<!-- b000068 | contents | pages [2] -->
Identiﬁcation of Key Points in the Game . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
7

<!-- b000070 | contents | pages [2] -->
3.3

<!-- b000071 | contents | pages [2] -->
Competition Flow Visualization . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
8

<!-- b000073 | contents | pages [2] -->
4 Momentum’s Impact on the Game Situation

<!-- b000074 | contents | pages [2] -->
10

<!-- b000075 | contents | pages [2] -->
The Runs Test —Stochastic Analysis . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
4.1

<!-- b000077 | contents | pages [2] -->
10

<!-- b000078 | contents | pages [2] -->
The Chi-square Test —Correlation Analysis . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
4.2

<!-- b000080 | contents | pages [2] -->
11

<!-- b000081 | contents | pages [2] -->
4.3

<!-- b000082 | contents | pages [2] -->
Reach a Verdict

<!-- b000083 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
12

<!-- b000085 | contents | pages [2] -->
5 Establish the Prediction for Match Trend Model Based on PCA&XGBoost

<!-- b000086 | contents | pages [2] -->
12

<!-- b000087 | contents | pages [2] -->
Principal Component Analysis —Determine the Model . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
5.1

<!-- b000089 | contents | pages [2] -->
12

<!-- b000090 | contents | pages [2] -->
XGBoost —Match Trend Prediction . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
5.2

<!-- b000092 | contents | pages [2] -->
13

<!-- b000093 | contents | pages [2] -->
5.3

<!-- b000094 | contents | pages [2] -->
Factor Importance Extraction

<!-- b000095 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
14

<!-- b000097 | contents | pages [2] -->
5.4

<!-- b000098 | contents | pages [2] -->
Tactical Suggestions for the Game . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
15

<!-- b000100 | contents | pages [2] -->
6 Model Effect Analysis

<!-- b000101 | contents | pages [2] -->
16

<!-- b000102 | contents | pages [2] -->
6.1

<!-- b000103 | contents | pages [2] -->
Model Testing on a New Race . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
16

<!-- b000105 | contents | pages [2] -->
Generalized Ability Analysis —U.S. Open Women’s Singles

<!-- b000106 | contents | pages [2] -->
6.2

<!-- b000107 | contents | pages [2] -->
. . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
18

<!-- b000109 | contents | pages [2] -->
6.3

<!-- b000110 | contents | pages [2] -->
Future Consideration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [2] -->
20

<!-- b000112 | contents | pages [2] -->
7 Sensitivity Analysis

<!-- b000113 | contents | pages [2] -->
21

<!-- b000114 | contents | pages [2] -->
8 Model Evaluation

<!-- b000115 | contents | pages [2] -->
22

<!-- b000116 | contents | pages [2] -->
8.1

<!-- b000117 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000118 | contents | pages [2] -->
22

<!-- b000119 | contents | pages [2] -->
8.2

<!-- b000120 | contents | pages [2] -->
Weaknesses and Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [2] -->
22

<!-- b000122 | contents | pages [2] -->
9 Conclusion

<!-- b000123 | contents | pages [2] -->
22

<!-- b000124 | contents | pages [2] -->
References

<!-- b000125 | contents | pages [2] -->
23

<!-- b000126 | contents | pages [2] -->
Memorandum

<!-- b000127 | contents | pages [2] -->
24

<!-- b000128 | contents | pages [2] -->
关注数学模型

<!-- b000129 | furniture | pages [2] -->
2

<!-- b000130 | furniture | pages [2] -->
MATHmodels

<!-- b000131 | furniture | pages [2] -->
获取更多资讯

<!-- b000132 | furniture | pages [3] -->
Team # 2409404

<!-- b000133 | furniture | pages [3] -->
Page 3 of 25

<!-- b000134 | heading | pages [3] -->
1 Introduction

<!-- b000135 | heading | pages [3] -->
1.1 Probelm Background

<!-- b000136 | prose | pages [3] -->
微信公众号：数学模型 In the men’s singles ﬁnal of the 2023 Wimbledon Open, Spanish rising star Carlos Al- caraz ended Novak Djokovic’s legendary player’s unbeaten run at Wimbledon since 2013. So What factors inﬂuenced the outcome of this seemingly unbalanced match?What factors contribute to the occurrence of analogous scenarios for individuals or players who appear to have a dominant position in the situation or game? Indeed, these conclusions are frequently ascribed to the phenomenon of "momentum".

<!-- b000137 | prose | pages [3] -->
Momentum is deﬁned in the dictionary as "strength or force gained by motion or by a series of events", but in actual sports, a team or player may feel energized during a game, but it is difﬁcult to accurately measure this phenomenon. Furthermore, assuming that such momentum exists, it is difﬁcult to determine how the various events of a game generate 微信号：MATHmodels or alter momentum. So, is there a computable and estimable frontal model of momentum available to aid players in achieving improved outcomes?

<!-- b000138 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000139 | prose | pages [3] -->
Given the problem’s background information and constrained conditions, we must complete the following tasks:

<!-- b000140 | prose | pages [3] -->
• Task 1: Build a model that captures the ﬂow of the match as it occurs and apply it to one or more matches to visualize the ﬂow of the match. The model needs to be able to identify the time period in the match when a player performs better and the degree of excellence within that time period.

<!-- b000141 | prose | pages [3] -->
• Task 2: A coach is skeptical about the role of momentum, arguing that ﬂuctuations in match situations and consecutive wins by players occur randomly, use a model to evaluate this coach’s claim.

<!-- b000142 | prose | pages [3] -->
• Task 3: Coaches need to be clear on whether there are indicators that can assist in determining when a game’s trend will shift.

<!-- b000143 | prose | pages [3] -->
– Using data from at least one match, build a model that predicts the movement of a match and identify which factors, if any, have the greatest impact on the movement of a match.

<!-- b000144 | prose | pages [3] -->
– Based on the difference in "momentum" in previous matches, help a player de- termine the correct strategy for a new match against a different opponent.

<!-- b000145 | prose | pages [3] -->
• Task 4: Test the current model in one or more other games and evaluate the model’s prediction of in-game ﬂuctuations; if the prediction is poor, can factors be identiﬁed for inclusion in future models? How generalizable is the model to other games, tour- naments, ﬁeld types, and other sports?

<!-- b000146 | prose | pages [3] -->
• Task 5: Write a memo summarizing the ﬁndings. Explain to a coach the role of "mo- mentum" and make recommendations to prepare players for events that affect the course of a tennis match.

<!-- b000147 | prose | pages [3] -->
关注数学模型

<!-- b000148 | furniture | pages [3] -->
2

<!-- b000149 | furniture | pages [3] -->
MATHmodels

<!-- b000150 | furniture | pages [3] -->
获取更多资讯

<!-- b000151 | furniture | pages [4] -->
Team # 2409404

<!-- b000152 | furniture | pages [4] -->
Page 4 of 25

<!-- b000153 | heading | pages [4] -->
1.3 Literature Review

<!-- b000154 | prose | pages [4] -->
The situation of a tennis match is rapidly changing. In the face of the variability of environment, strategy, and process, momentum, a factor that may turn the match around, 微信公众号：数学模型 has become a focus of research.

<!-- b000155 | prose | pages [4] -->
Ben Moss et al. argue that the uncertainty of the momentum effect in tennis, which may [1]. In addition, if a vary from player to player, needs to be considered at an individual level player breaks his opponent’s serve when facing a game point, he is more likely to hold his serve in the next round of serve reception.

<!-- b000156 | prose | pages [4] -->
Zhang Xiaofei suggests that the gain or loss of a key score will have a serious impact on a player’s momentum, thus affecting the direction of the match. In the face of changes in the score, some players may increase their momentum, attack courageously, and take the initiative. While some players may attach too much importance to the change of score, and whenever they encounter the change of key score, their momentum may be reduced, and [2]. 微信号：MATHmodels then the game will turn around

<!-- b000157 | prose | pages [4] -->
Chen Liang suggests that there is a direct "attack-defense relationship" in tennis and that in order to win a match, one must maximize one’s own performance and inhibit one’s opponents to the maximum extent possible. Under the joint effect of oneself, opponent, and competition environment, the momentum of both sides usually will not remain stable during the competition, and the change of the contrast relationship will form the stage "rise [3] of the competitive performance. and fall"

<!-- b000158 | prose | pages [4] -->
In conclusion, momentum affects different players in different ways, which is impor- tant for the psychological support of athletes.

<!-- b000159 | heading | pages [4] -->
1.4 Our work

<!-- b000160 | prose | pages [4] -->
For ease of description and visualization, we have drawn a ﬂow chart (Figure 1) to represent our work.

<!-- b000161 | prose | pages [4] -->
Prepare Task 1 Task 2 Quantification of the momentum Data collection The Runs Test Data pre-processing Selection of Weighing Set the size of Stochastic analysis of player-related of indicators the moving window situational fluctuations and indicator factors player continuity scores Identification of key points in the game Correlation analysis of momentum Tunning point of Game Point the momentum (CUSUM) Chi-square Test Visual analysis of match flows

<!-- b000162 | prose | pages [4] -->
Task 3 Task 4 Final Testing of the Model Advice for Prediction of the swings in the match Coaches and Athletes Confusion Classification PCA & XGBOOST ROC Curve Matrix Report Importance extraction Application capacity of factors Model Enhancement Tactical suggestions for （Prospects for the future） the game

<!-- b000163 | caption | pages [4] -->
Figure 1: Flow chart of our work

<!-- b000164 | prose | pages [4] -->
关注数学模型

<!-- b000165 | furniture | pages [4] -->
2

<!-- b000166 | furniture | pages [4] -->
MATHmodels

<!-- b000167 | furniture | pages [4] -->
获取更多资讯

<!-- b000168 | furniture | pages [5] -->
Team # 2409404

<!-- b000169 | furniture | pages [5] -->
Page 5 of 25

<!-- b000170 | heading | pages [5] -->
2 Preparation of the Models

<!-- b000171 | heading | pages [5] -->
2.1 Assumptions and Explanations

<!-- b000172 | prose | pages [5] -->
微信公众号：数学模型 To simplify the issue, we have made the following assumptions, each of which is ap- propriately reasonable.

<!-- b000173 | prose | pages [5] -->
• Assumption 1: The entire game is not affected by external factors such as unfair deci- sions by the referee.

<!-- b000174 | prose | pages [5] -->
,→Explanation: An unfair judgement by the referee will mislead our judgement of the player’s score, thus not accurately calculating the impact of momentum on the athlete.

<!-- b000175 | prose | pages [5] -->
• Assumption 2: Players were in good physical condition throughout the game.

<!-- b000176 | prose | pages [5] -->
,→Explanation: Physical condition will affect an athlete’s performance in a game, while existing data makes it difﬁcult to measure a player’s moment-to-moment con- 微信号：MATHmodels dition.

<!-- b000177 | prose | pages [5] -->
• Assumption 3: The athlete has not used illegal drugs such as doping and has not cheated in competition.

<!-- b000178 | prose | pages [5] -->
,→Explanation: Doping can substantially increase an athlete’s level of competitive- ness, deviating from reality and affecting the calculation of momentum. Doping is also strictly prohibited in competition.

<!-- b000179 | heading | pages [5] -->
2.2 Notations

<!-- b000180 | prose | pages [5] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000181 | caption | pages [5] -->
Table 1: Notations

<!-- b000182 | heading | pages [5] -->
Symbol

<!-- b000183 | prose | pages [5] -->
Deﬁnition

<!-- b000184 | prose | pages [5] -->
α Extra Advantages of the Player’s Serve β Sliding Window Size i Scoring Moment E(·) Data Average V(·) Data Variance

<!-- b000185 | prose | pages [5] -->
* Some variables are not listed here because they have different meanings in different places, so we will discuss them in detail in each section.

<!-- b000186 | heading | pages [5] -->
2.3 Data Preparation

<!-- b000187 | heading | pages [5] -->
2.3.1 Data Collection

<!-- b000188 | prose | pages [5] -->
To enhance the credibility of our analysis, we have gathered a substantial quantity of information from the following sources, in addition to the data provided by the contest questions. Refer to Table 2.

<!-- b000189 | prose | pages [5] -->
The data from the US Open Women’s Singles Final between C. Gauff and A. Sabalenka

<!-- b000190 | prose | pages [5, 6] -->
关注数学模型 on September 9, 2023, were collected using mathematical statistics and video observation methods to assess the model’s ability to make generalizations.

<!-- b000191 | furniture | pages [5] -->
2

<!-- b000192 | furniture | pages [5] -->
MATHmodels

<!-- b000193 | furniture | pages [5] -->
获取更多资讯

<!-- b000194 | furniture | pages [6] -->
Team # 2409404

<!-- b000195 | furniture | pages [6] -->
Page 6 of 25

<!-- b000197 | caption | pages [6] -->
Table 2: Data Sources and Websites

<!-- b000198 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000199 | heading | pages [6] -->
Data Source

<!-- b000200 | prose | pages [6] -->
Website https://sports.cctv.com/ CCTV https://www.usopen.org/index.html US Open https://www.wimbledon.com/en_GB/index.html Wimbledon

<!-- b000201 | heading | pages [6] -->
2.3.2 Data Pre-processing

<!-- b000202 | prose | pages [6] -->
Upon gathering and arranging the data, it becomes apparent that there are discrep- ancies between the data’s format and the data provided in the question. Therefore, it is imperative to preprocess the necessary data. Initially, the data header is standardized and the indicators are abbreviated to simplify the following listing. The corresponding details can be found in Table 3. Furthermore, it has been discovered that there are gaps in the mea- 微信号：MATHmodels surements of "winner shot type", "serve width", "serve depth", and "return depth". Based on the data analysis, the vacancies are attributed to the lack of such occurrences, so we re- place them with a value of zero. Furthermore, it was discovered that the aforementioned indicators consisted of text-based categorical data. Therefore, the implementation of Label Encoder processing was deemed necessary, which involves providing a distinct numerical value to each category.

<!-- b000203 | caption | pages [6] -->
Table 3: Abbreviations for factors

<!-- b000204 | prose | pages [6] -->
Former Glossary Former Glossary Former Glossary match_id MI game_victor GAV p1_break_pt P1BP SNO SEV P2BP set_no set_victor p2_break_pt game_no GNO p1_ace P1ACE p1_break_pt_won P1BPW PNO P2ACE P2BPW point_no p2_ace p2_break_pt_won p1_sets P1SE p1_winner P1W p1_break_pt_missed P1BPM P2SE P2W P2BPM p2_sets p2_winner p2_break_pt_missed P1GA WST P1DR p1_games winner_shot_type p1_distance_run p2_games P2GA p1_double_fault P1DF p2_distance_run P2DR P1SC P2DF RC p1_score p2_double_fault rally_count p2_score P2SC p1_unf_err P1UE speed_mph SM SER P2UE SW server p2_unf_err serve_width serve_no SERNO p1_net_pt P1NP serve_depth SD PV P2NP RD point_victor p2_net_pt return_depth P1PW P1NPW ETS p1_points_won p1_net_pt_won elapsed_time_seconds P2PW P2NPW MS p2_points_won p2_net_pt_won momentum swings

<!-- b000205 | heading | pages [6] -->
3 Establish the Momentum Quantization Model Based on

<!-- b000206 | prose | pages [6] -->
Sliding Windows

<!-- b000207 | heading | pages [6] -->
3.1 Quantization of Momentum

<!-- b000208 | prose | pages [6] -->
To assess the current performance and level of excellence of a player during a game, we utilize the concept of a sliding window. This method considers the uncertainty of the game’s progression and calculates the player’s performance over a recent series of rounds.

<!-- b000209 | prose | pages [6, 7] -->
关注数学模型 By doing so, we can obtain a quantiﬁed measure of the player’s momentum at that particu- lar moment. The quantized momentum value for a player at time i (after the moment when the player scored) is deﬁned as:

<!-- b000210 | furniture | pages [6] -->
2

<!-- b000211 | furniture | pages [6] -->
MATHmodels

<!-- b000212 | furniture | pages [6] -->
获取更多资讯

<!-- b000213 | furniture | pages [7] -->
Team # 2409404

<!-- b000214 | furniture | pages [7] -->
Page 7 of 25

<!-- b000216 | prose | pages [7] -->
微信公众号：数学模型 i [GAi + SCi + (α + 1) SER + PVi + BPWi + ACEi + NPWi + Wi −UEi −DFi] M = (1) ∑ i−β+1

<!-- b000217 | prose | pages [7] -->
The variables in question are β, which represents the size of the moving window; α, which represents the percentage of the player’s additional advantage on serve, and GA, which represents the number of games won by the player during the window. SC represents the total number of sets won by the player. PV stands for "winner of the point", indicating the player who successfully wins a point. BPW refers to the number of times the player successfully wins a break point. ACE represents the number of times the player hits an untouchable winning serve. NPW indicates the number of net points gained by the player. W represents the frequency at which a player successfully executed an unbeatable winning 微信号：MATHmodels shot, UE represents the frequency at which a player committed an unforced error, and DE represents the frequency at which a player failed to make both serves and hence lost the point.

<!-- b000218 | prose | pages [7] -->
In this quantitative approach, two crucial parameters can be identiﬁed: the magnitude of the sliding window, denoted as β, and the proportion of additional advantage that is discounted due to the player’s serve, represented by α.

<!-- b000219 | prose | pages [7] -->
By utilizing the provided formula, we can calculate the precise numerical value of mo- mentum for each player at any given moment. By comparing the momentum values be- tween the two sides of the game, we can determine which player is performing better at a speciﬁc moment. This allows us to derive the speciﬁc value of their performance.

<!-- b000220 | heading | pages [7] -->
3.2 Identiﬁcation of Key Points in the Game

<!-- b000221 | prose | pages [7] -->
To comprehend the strengths and weaknesses of the aforementioned models in assess- ing player momentum values throughout a match, we will now outline several crucial as- pects of the match. These aspects will also be depicted in the forthcoming visualization of the match ﬂow.

<!-- b000222 | prose | pages [7] -->
Special Circumstances Normal Circumstances Scoring Rules When the score is 40-40 in a Game 1 2 3 AD

<!-- b000223 | prose | pages [7] -->
15 points 30 points 40 points Point When the score is 6-6 in a Set AD 1 7 …… Advantange …… Game Tiebreak When the score is 5-5 in a Set best-of-five series

<!-- b000224 | prose | pages [7] -->
best-of-three series Set One side wins two more games

<!-- b000225 | caption | pages [7] -->
Figure 2: Rules of Tennis

<!-- b000226 | prose | pages [7, 8] -->
关注数学模型 • Game Point: This crucial point determines the winner of the set between the two play- ers and is ofﬁcially acknowledged in accordance with the established rules of tennis, as depicted in Figure 2.

<!-- b000227 | furniture | pages [7] -->
2

<!-- b000228 | furniture | pages [7] -->
MATHmodels

<!-- b000229 | furniture | pages [7] -->
获取更多资讯

<!-- b000230 | furniture | pages [8] -->
Team # 2409404

<!-- b000231 | furniture | pages [8] -->
Page 8 of 25

<!-- b000233 | prose | pages [8] -->
• Tuning Point of Momentum: The Cumulative Sum (CUSUM) technique is employed 微信公众号：数学模型 at this stage to identify the momentum of the participants. To detect any mutation, the data can be analyzed by calculating the cumulative total to track the cumulative change over time.

<!-- b000234 | heading | pages [8] -->
3.3 Competition Flow Visualization

<!-- b000235 | prose | pages [8] -->
We are choosing the 2023 Wimbledon Men’s Singles Final between Carlos Alcaraz and Novak Djokovic. Associated with the data "2023-Wimbledon-1701" To begin with, we have provided a statistical analysis of the current state of this match, as illustrated in Figure 3.

<!-- b000236 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000237 | heading | pages [8] -->
C. Alcaraz

<!-- b000238 | prose | pages [8] -->
N. Djokovic 9 ACES 2 7 DOUBLE FAULTS 3 168 166 TOTAL POINTS WON UNFORCED ERRORS 45 40 6605.5 m DISTANCE COVERED 6195.2 m 94/150（63%） 118/184（64%） FIRST SERVE % IN 66/94（70%） 73/118（62%） WIN % ON 1ST SERVE WIN % ON 2ND SERVE 37/66（56%） 28/56（50%） 5/15（33%） 5/19（26%） BREAK POINTS WON 28/46（61%） NET POINTS WON 39/65（60%） RECEIVING POINTS WON 56/150（37%） 74/184（40%）

<!-- b000239 | caption | pages [8] -->
Figure 3: Technical Statistics

<!-- b000240 | prose | pages [8] -->
Based on the graph, it is evident that Alcaraz’s serve is far superior to Djokovic’s. How- ever, Alcaraz also commits more errors. Both Alcaraz and Djokovic primarily focused on their ﬁrst serves, indicating that it is comparatively simpler to get points with the initial serve. Based on the comprehensive match statistics, Alcaraz demonstrated superior perfor- mance.

<!-- b000241 | prose | pages [8] -->
1   7 8   6   3   6 20 Alcaraz Djokovic 6   6 6   1   6 4

<!-- b000242 | prose | pages [8] -->
Carlos Alcaraz's Momentum 10 Novak Djokovic's Momentum Momentum Carlos Alcaraz's Game Point Novak Djokovic's Game Point 0 Carlos Alcaraz's Turning Point Novak Djokovic's Turning Point 10

<!-- b000243 | prose | pages [8] -->
0 2000 4000 6000 8000 10000 12000 14000 16000 Elapsed Time (seconds)

<!-- b000244 | caption | pages [8] -->
Figure 4: Match Flow

<!-- b000245 | prose | pages [8] -->
Now, equation (1) allows for the calculation of the quantitative momentum values of the two players at different moments. The sliding window size, denoted as β, is set to 5. The player’s serve advantage is discounted proportionally by a factor of α = 0.68. The value of α is determined through statistical analysis of the 31 matches provided in the attached table. It

<!-- b000246 | prose | pages [8, 9] -->
关注数学模型 is important to note that α should be determined based on various factors, such as different matches and different players.

<!-- b000247 | furniture | pages [8] -->
2

<!-- b000248 | furniture | pages [8] -->
MATHmodels

<!-- b000249 | furniture | pages [8] -->
获取更多资讯

<!-- b000250 | furniture | pages [9] -->
Team # 2409404

<!-- b000251 | furniture | pages [9] -->
Page 9 of 25

<!-- b000253 | prose | pages [9] -->
The quantitative values of momentum for both players at various periods in the match, 微信公众号：数学模型 including important points, are depicted in Figure 4. Furthermore, to more accurately il- lustrate the level of control a player has at a speciﬁc point, the momentum scatterplot is graphed, as depicted in Figure 5.

<!-- b000254 | prose | pages [9] -->
20 10 15 15 10 10 5 Novak Djokovic Carlos Alcaraz Momentum 5 5 0 0 0 5 5 5 10 10 10 15 15 0 2000 4000 6000 8000 10000 12000 14000 16000 微信号：MATHmodels Elapsed Time (seconds)

<!-- b000255 | caption | pages [9] -->
Figure 5: Match Flow Scatter

<!-- b000256 | prose | pages [9] -->
By comparing the momentum change curve with the change in the athletes’ score, we ﬁnd that the momentum will increase when the athletes are on a winning streak or serve for points, and when the momentum is well ahead of their opponents, the athletes will be at their best and have a high probability of winning the match.

<!-- b000257 | prose | pages [9] -->
In the ﬁrst set of the match, Djokovic won easily with a score of 6-1. In the ﬁrst game of the ﬁrst set, the two were neck and neck before Djokovic narrowly won the ﬁrst game, at which point their momentum barely changed. After Djokovic won the second set with consecutive points, we observed a signiﬁcant increase in momentum. Alcaraz’s loss of mo- mentum, caused by consecutive losses, led him to lose the next few games to Djokovic, almost all of them by large margins. Especially in the seventh game of the ﬁrst set, when Djokovic got the set point with a score of 5-1, his momentum also increased dramatically, and with this momentum, Djokovic did not allow his opponent to win a single ball in the seventh game.

<!-- b000258 | prose | pages [9] -->
In the second set, the two entered a crucial tie-break. In the tie-break, Alcaraz, who had failed on his ﬁrst serve, still lost the point on his second serve, and Djokovic scored a mini-break, which drastically reduced the momentum of Alcaraz, who had already lost the set, and thus lost two more balls after that. However, at around 6600 s, Alcaraz clawed his way back into the set on serve, and at this point his momentum was extremely elevated and at its peak, while Djokovic was too nervous to face such a crucial point and his momentum was reduced, and Alcaraz eventually won the set. After that, Alcaraz used the momentum of the second set to score consecutive points, and the momentum reached its peak, winning two of the last three sets to ﬁnally win the whole match.

<!-- b000259 | prose | pages [9] -->
Throughout the match, we ﬁnd that Alcaraz’s average momentum was higher than Derkovic’s, which is one of the reasons why Alcaraz got the victory. Also as can be seen by the scatter plot, the distribution of momentum in the sets won by Alcaraz was higher than that of Derkovic.

<!-- b000260 | prose | pages [9] -->
关注数学模型

<!-- b000261 | furniture | pages [9] -->
2

<!-- b000262 | furniture | pages [9] -->
MATHmodels

<!-- b000263 | furniture | pages [9] -->
获取更多资讯

<!-- b000264 | furniture | pages [10] -->
Team # 2409404

<!-- b000265 | furniture | pages [10] -->
Page 10 of 25

<!-- b000266 | heading | pages [10] -->
4 Momentum’s Impact on the Game Situation

<!-- b000267 | prose | pages [10] -->
The Runs Test —Stochastic Analysis 4.1 微信公众号：数学模型 The runs test is a non-parametric technique used to assess the randomness of a binary sequence consisting of only two distinct values. The run is deﬁned as a consecutive series of parts in a sequence, where each section has the same numeric value as the number "r" of [4]. It is vital to assess the volatility of the the journey. The duration of the run is denoted by l scenario and the randomness of players’ consecutive scores.

<!-- b000268 | prose | pages [10] -->
It is assumed that the binary sequence under analysis is composed of m A’s and n B’s. Prior to conducting the test, two contrasting hypotheses are established: the original hypothesis and the alternative hypothesis.

<!-- b000269 | prose | pages [10] -->
• Original hypothesis H0: The arrangement of A and B is randomized;

<!-- b000270 | prose | pages [10] -->
• Alternative hypothesis H1: The distribution of A and B isn’t random. 微信号：MATHmodels If H0 holds, then we have:

<!-- b000271 | prose | pages [10] -->
( m −1 ) ( n −1 ) 2 k −1 k −1 P (r = 2k) = ( m + n ) (2)

<!-- b000272 | prose | pages [10] -->
m

<!-- b000273 | prose | pages [10] -->
( m −1 ) ( n −1 ) ( m −1 ) ( n −1 ) + k −1 k −1 k k P (r = 2k + 1) = ( m + n ) (3)

<!-- b000274 | prose | pages [10] -->
m

<!-- b000275 | prose | pages [10] -->
Given that we have chosen 31 games, both m and n represent large samples. Conse- quently, the number of the runs, denoted as r, may be considered to follow an almost nor- mal distribution. As a result, we can calculate the mathematical expectation and variance of r: E (r) = 2mn m + n + 1 (4)

<!-- b000276 | prose | pages [10] -->
V (r) = 2mn (2mn −m −n) (5) (m + n)2 (m + n −1)

<!-- b000277 | prose | pages [10] -->
The statistic is then derived from the count of the run.

<!-- b000278 | prose | pages [10] -->
Z = r −E (r) √ (6) V (r)

<!-- b000279 | prose | pages [10] -->
To account for the variability of the circumstance, we utilize the Point Victor factor. In order to assess the ongoing performance of the participants, we initially employ the Point Victor factor, followed by the establishment of two indicators to measure continuous values. Subsequently, we evaluate the aforementioned sequence. Consequently, the outcomes can

<!-- b000280 | prose | pages [10, 11] -->
关注数学模型 be acquired as demonstrated in Table 4.

<!-- b000281 | furniture | pages [10] -->
2

<!-- b000282 | furniture | pages [10] -->
MATHmodels

<!-- b000283 | furniture | pages [10] -->
获取更多资讯

<!-- b000284 | furniture | pages [11] -->
Team # 2409404

<!-- b000285 | furniture | pages [11] -->
Page 11 of 25

<!-- b000287 | caption | pages [11] -->
Table 4: The Results of the Runs Test

<!-- b000288 | prose | pages [11] -->
Testing Program Z p 微信公众号：数学模型 Point Victor -5.613 0.00000001986<0.01 Player 1 Consecutive Win -30.606 0.000<0.01 Player 2 Consecutive Win -29.866 0.000<0.01

<!-- b000289 | prose | pages [11] -->
Upon examining the table, it becomes evident that Z-scores are less than zero for all three indicators. This is attributed to the fact that the observations are located to the left of the mean. Given a signiﬁcance level of 0.01 and p < 0.01, we can be 99 % certain that the alternative hypothesis, H0 will be rejected. This suggests that the ﬂuctuations in the situation and the consecutive scoring situations of the players are not random, indicating the presence of a driving factor.

<!-- b000290 | prose | pages [11] -->
The Chi-square Test —Correlation Analysis 4.2 微信号：MATHmodels To assess the variation of the scenario and the continual scoring of players in relation to Momentum, we employ the chi-square independence test. In contrast to Problem 1, when Momentum was quantiﬁed as a continuous variable, the chi-square test requires it to be a discrete categorical variable. First, we begin by discretizing the concept of momentum. Cur- rently, we possess the initial momentum values of Player 1 and Player 2, denoted as Mp1i and Mp2i, correspondingly, which are related by the following transformation equation:

<!-- b000291 | prose | pages [11] -->
 { 1, MP1i > MP2i   ′  1i = MP  0, MP1i < MP2i { 1, MP1i < MP2i (7)   ′  2i = MP  0, MP1i > MP2i

<!-- b000292 | prose | pages [11] -->
Following the aforementioned equation, we get the categorical variables and next em- ploy the chi-square test. Here, it is imperative to assume that momentum is independent of ﬂuctuations in the game circumstances and the consecutive triumphs of a player. The calculated value representing the test statistic is:

<!-- b000293 | prose | pages [11] -->
( )2 R C njk −n ˆpjk χ2 = ∑ ∑ (8) n ˆpjk j=1 k=1

<!-- b000294 | prose | pages [11] -->
where R and C are the sizes of the R × C list of columns, and n ˆpjk is the maximum likelihood estimate obtained when H0 holds, i.e:

<!-- b000295 | prose | pages [11] -->
ˆpjk = ˆpj· ˆp·k = nj· n · n·k (9) n

<!-- b000296 | prose | pages [11] -->
For a given signiﬁcance level γ, the rejection domain of the test is { } χ2 ≥χ2 1−γ ((R −1) (C −1)) W = . (10)

<!-- b000297 | prose | pages [11, 12] -->
关注数学模型 Following the aforementioned procedure, the outcomes of the chi-square test can be obtained and are presented in Table 5.

<!-- b000298 | furniture | pages [11] -->
2

<!-- b000299 | furniture | pages [11] -->
MATHmodels

<!-- b000300 | furniture | pages [11] -->
获取更多资讯

<!-- b000301 | furniture | pages [12] -->
Team # 2409404

<!-- b000302 | furniture | pages [12] -->
Page 12 of 25

<!-- b000304 | caption | pages [12] -->
Table 5: The Results of the Chi-square Test

<!-- b000305 | prose | pages [12] -->
微信公众号：数学模型 p1W p1 Game Point χ2 χ2 TestingProgram Category SUM TestingProgram Category SUM p p 0 1 0 1 0 1936 1483 3419 0 3048 371 3419 p1N p1N 1 1 1630 2235 3865 3230 635 3865 9.167 × 10−32 1.243 × 10−9 151.617 47.256 SUM SUM 3566 3718 7284 6278 1006 7284 p2W p2 Game Point χ2 χ2 TestingProgram Category SUM p TestingProgram Category SUM p 0 1 0 1 0 0 2266 1663 3929 3534 395 3929 p2N p2N 1 1 1452 1903 3355 2843 512 3355 1.962 × 10−31 3.948 × 10−9 150.065 45.015 SUM SUM 3718 3566 7284 6377 907 7284 p2W p2 Game Point χ2 χ2 TestingProgram Category SUM TestingProgram Category SUM p p 0 1 0 1 0 0 1483 1936 3419 2901 518 3419 p1N p1N 1 1 2235 1630 3865 3476 389 3865 9.167 × 10−32 1.012 × 10−8 151.617 43.047 SUM SUM 3718 3566 7284 6377 907 7284 p1W p1 Game Point χ2 χ2 TestingProgram Category SUM p TestingProgram Category SUM p 0 1 0 1 0 0 1663 2266 3929 3287 642 3929 p2N p2N 1 1 1903 1452 3355 2991 364 3355 1.962 × 10−31 2.671 × 10−9 150.065 45.831 微信号：MATHmodels SUM SUM 3566 3718 7284 6278 1006 7284

<!-- b000306 | prose | pages [12] -->
Upon examining the table, it becomes apparent that the χ2 for each test is greater, as- suming a signiﬁcant level of 0.01 and p < 0.01. This implies a 99 % level of conﬁdence in rejecting the original hypothesis H0, indicating a correlation between the volatility of the situation and the consecutive scoring situation of the players with Momentum.

<!-- b000307 | heading | pages [12] -->
4.3 Reach a Verdict

<!-- b000308 | prose | pages [12] -->
Based on the results of the Runs Test examining the unpredictability of circumstance ﬂuctuations and players’ successive scores, as well as a chi-square test assessing the rele- vance of Momentum, there is ample evidence to support the notion that Momentum plays a vital role in the outcome of a tennis match. The variability of the circumstance and the successive scores of the participants exhibit a non-random pattern, suggesting the presence of a driving element, most likely attributable to momentum.

<!-- b000309 | heading | pages [12] -->
5 Establish the Prediction for Match Trend Model Based on

<!-- b000310 | prose | pages [12] -->
PCA&XGBoost

<!-- b000311 | heading | pages [12] -->
Principal Component Analysis —Determine the Model

<!-- b000312 | prose | pages [12] -->
5.1

<!-- b000313 | prose | pages [12] -->
Based on our previous discussion, we have sufﬁcient evidence to suggest that the unpredictable ﬂuctuation in the game is connected to the momentum of the two players. Therefore, we will use momentum as the focus of our forecast. Nevertheless, in the quan- titative model of momentum, which provides continuous data on the momentum of both players at every moment, we contend that the ﬂuctuating pattern in the match can be inter- preted as a transfer of momentum. Speciﬁcally, if player 1’s momentum surpasses that of player 2, the momentum is deemed to have shifted to player 1, and vice versa for player 2.

<!-- b000314 | prose | pages [12, 13] -->
关注数学模型 The equation (7) can be used to express this technique. Let’s say that we are player 1. In this case, "1" indicates that momentum is in our favor, whereas "2" indicates that momentum is in the opposing side’s favor. By employing this discretization technique, we can obtain a crude depiction of the game’s ﬂuctuation pattern. Thus, we can consider it the dependent 微信公众号：数学模型 variable in our forecast, referred to as MS, while the autonomous variables can be the ones listed in Table 3. Excluding MI and MS, we have chosen 43 criteria to include in the table.

<!-- b000315 | furniture | pages [12] -->
2

<!-- b000316 | furniture | pages [12] -->
MATHmodels

<!-- b000317 | furniture | pages [12] -->
获取更多资讯

<!-- b000318 | furniture | pages [13] -->
Team # 2409404

<!-- b000319 | furniture | pages [13] -->
Page 13 of 25

<!-- b000321 | prose | pages [13] -->
To enhance model selection, we initially considered the ﬁrst 30 matches, excluding the Carlos Alcaraz VS. Novak Djokovic game.1 This analysis reduces the previously mentioned 43 elements to two dimensions. We next create a scatter plot with two scales based on this analysis, as depicted in Figure 6.

<!-- b000322 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000323 | caption | pages [13] -->
Figure 6: PCA Biplot

<!-- b000324 | prose | pages [13] -->
Upon analyzing the graph, it becomes evident that:

<!-- b000325 | prose | pages [13] -->
• Fluctuations in the match situation are challenging to classify on the two-dimensional principal components. The majority of factors do not have a signiﬁcant impact on PC1, but they have a greater inﬂuence on PC2. These factors include GNO, GA, DR, and RC.

<!-- b000326 | prose | pages [13] -->
• Several parameters, including SNO, PNO, SE, PW, and ETS, have a greater impact on PC1 and a lesser one on PC2.

<!-- b000327 | prose | pages [13] -->
• Only a small number of variables have a substantial impact on both PC1 and PC2.

<!-- b000328 | prose | pages [13] -->
• PC2 may encounter challenges in accurately characterizing variations and establishing a more precise basis for classifying the outcomes.

<!-- b000329 | prose | pages [13] -->
• The distribution of scenario ﬂuctuations has a distinct clustering pattern on PC1.

<!-- b000330 | prose | pages [13] -->
• Data cannot be divided in a linear manner.

<!-- b000331 | prose | pages [13] -->
• The clustering of the factor bisector plots is likely a result of the interconnection be- tween the factors, as supported by earlier investigations.

<!-- b000332 | prose | pages [13] -->
Based on the above analysis, we believe that simple classiﬁcation models make it dif- ﬁcult to predict the ﬂuctuation of the game situation more accurately, so we consider the eXtreme Gradient Boosting (XGBoost) optimization model based on the tree model.

<!-- b000333 | prose | pages [13] -->
XGBoost —Match Trend Prediction 5.2

<!-- b000334 | prose | pages [13] -->
In the previous analysis, we determined the inputs to the model as 43 factor indicators for the two players. These indicators serve as independent variables. The outputs of the model, on the other hand, are the ﬂuctuations in the match situation. We assume a value

<!-- b000335 | prose | pages [13] -->
1This is because we must make a prediction for the entire game to avoid any data leaks.

<!-- b000336 | prose | pages [13, 14] -->
关注数学模型 of 1 for the own side and 0 for the other side, making it the dependent variable. Conse- quently, the problem can be succinctly described as a categorical prediction. The model was constructed using data from the initial 30 matches, and knowledge was acquired from these matches. The last match, "2023-wimbledon-1701", was then used as the basis for sub- 微信公众号：数学模型 sequent model evaluations. This approach can optimize the efﬁcient utilization of the avail- able dataset and, to some extent, enhance the effectiveness of the model. It is important to mention that while analyzing 30 games, we must individually compute the momentum of each player in each game. Then, we discretize it depending on the magnitude of the two in order to successfully prevent miscalculations caused by variations in the sliding window span across various games. The dependent variable can be explained as a dichotomous vari- able that changes from 1 to 0 or from 0 to 1 in two consecutive moments. This represents a change in the game’s circumstances at that time.

<!-- b000337 | furniture | pages [13] -->
2

<!-- b000338 | furniture | pages [13] -->
MATHmodels

<!-- b000339 | furniture | pages [13] -->
获取更多资讯

<!-- b000340 | furniture | pages [14] -->
Team # 2409404

<!-- b000341 | furniture | pages [14] -->
Page 14 of 25

<!-- b000343 | heading | pages [14] -->
5.3 Factor Importance Extraction

<!-- b000344 | prose | pages [14] -->
微信号：MATHmodels The XGBoost model learns from 30 matches, and we can calculate the extent to which each factor contributes to learning, denoted pη(η = 1, 2, · · · , 43). In order to identify the critical factors that signiﬁcantly impact the ﬂuctuations in the matches, we calculate the importance score FIη for each factor. We then normalize the pi values and calculate the percent score. The formula is as follows:

<!-- b000345 | prose | pages [14] -->
pη FIη = 100 × (11) max (FI)

<!-- b000346 | prose | pages [14] -->
Based on the aforementioned computations, we will present the relevance scores of each factor, as depicted in Figure 7.

<!-- b000347 | prose | pages [14] -->
100

<!-- b000348 | prose | pages [14] -->
90

<!-- b000349 | prose | pages [14] -->
80

<!-- b000350 | prose | pages [14] -->
Importance of normalization 70

<!-- b000351 | prose | pages [14] -->
60

<!-- b000352 | prose | pages [14] -->
50

<!-- b000353 | prose | pages [14] -->
40

<!-- b000354 | prose | pages [14] -->
30

<!-- b000355 | prose | pages [14] -->
20

<!-- b000356 | prose | pages [14] -->
10

<!-- b000357 | prose | pages [14] -->
0 P2BP P1BP PV P1SE P2GA P1GA SER P1BPW P2DF ETS P2PW P1PW GNO P2BPM P2SC P2BPW SNO PNO P1UE P2SE P1SC GAV P1ACE P2NPW P2NP P1DF SM RC P1BPM SW P2DR P1W P1NP P2W RD P1NPW P1DR SERNO SD P2ACE WST P2UE SEV Indicator abbreviations

<!-- b000358 | caption | pages [14] -->
Figure 7: Factor Importance

<!-- b000359 | prose | pages [14] -->
Out of the total of 43 indicators, 28 of them fall into the same category in pairs. For example, both P1BP and P2BP are considered break points. Therefore, we calculate the average importance scores for these indicators and provide them in Table 6.

<!-- b000360 | prose | pages [14] -->
By integrating the aforementioned graphic and table, it becomes evident that both BP (break point) and PV (point victor) signiﬁcantly contribute to accurately forecasting the

<!-- b000361 | prose | pages [14, 15] -->
关注数学模型 Factor Importance Importance Factor P1 P2 AVERAGE PV 74.923 SER BP 30.771 93.395 100.000 96.698 ETS 24.406 GA 36.801 39.985 38.393 微信公众号：数学模型 GNO SE 21.387 40.959 19.217 30.088 SNO 19.668 BPW 30.662 19.786 25.224 PNO PW 19.570 23.023 23.248 23.136 GAV DF 18.524 14.406 26.983 20.695 SM SC 14.060 18.942 19.936 19.439 RC BPM 13.912 13.880 20.603 17.241 SW 13.534 UE 19.353 10.249 14.801 RD ACE 12.679 17.899 11.626 14.762 SERNO 12.000 NPW 12.677 15.764 14.221 SD NP 11.825 12.898 14.590 13.744 WST 11.325 DR 13.375 12.489 12.932 SEV W 6.477 12.993 12.734 12.864

<!-- b000362 | furniture | pages [14] -->
2

<!-- b000363 | furniture | pages [14] -->
MATHmodels

<!-- b000364 | furniture | pages [14] -->
获取更多资讯

<!-- b000365 | furniture | pages [15] -->
Team # 2409404

<!-- b000366 | furniture | pages [15] -->
Page 15 of 25

<!-- b000367 | caption | pages [15] -->
Table 6: Importance of Factors after Organizing

<!-- b000369 | prose | pages [15] -->
game’s trajectory. While the aforementioned two criteria may be more signiﬁcant, the in- trinsic impact of other aspects should not be disregarded. Factors such as ACE, DF, DR, 微信号：MATHmodels SERNO, and others will also inﬂuence the game’s ﬂuctuations to a certain degree. Ulti- mately, we furnish tennis coaches with insights into the signiﬁcance of momentum and offer guidance on how players can sustain and control momentum throughout a match.

<!-- b000370 | heading | pages [15] -->
5.4 Tactical Suggestions for the Game

<!-- b000371 | prose | pages [15] -->
Based on the above analysis, while analyzing the differential in past match "momen- tum" swings, give the player some constructive suggestions.

<!-- b000372 | prose | pages [15] -->
• Reasonable distribution of physical ﬁtness. In the early stage of the game, we will try to attack, understand each other’s physical strength, tactics, etc., and retain our own physical strength; in the middle of the game, we will make reasonable use of "mo- mentum," adopt an aggressive or conservative playing style according to the current situation of the game, and appropriately consume the opponent’s physical strength;

<!-- b000373 | prose | pages [15] -->
and the coaches and the players should pay attention to the changes in their physical state at this time, such as the existence of movement. Coaches and players should pay attention to the changes in physical condition, such as whether there is any movement stiffness, and take technical pause and other measures in time to ensure that the play- ers have a better momentum level. In the late stage of the game, the players synthesize the experience gained from the pre-momentum and mid-momentum to play the game and make appropriate adjustments to combine with their own physical condition.

<!-- b000374 | prose | pages [15] -->
• Focus on the mental state during the match. Mental state also has a certain degree of inﬂuence on "momentum." If the player focuses too much on the score, especially in the key game or the key points in the game, his momentum may be greatly reduced because of the opponent’s scores. The player should discuss their own situation in the game with a psychological expert. Psychological experts should provide timely communication with the coaches, technical time-outs, and other measures to restore the player’s "momentum" Coaches should communicate with the players and take measures such as a technical pause to restore the players’ momentum. Players should also pay attention to the change in their own mentality during the game and adjust it

<!-- b000375 | prose | pages [15, 16] -->
关注数学模型 by appropriately slowing down the rhythm of offense.

<!-- b000376 | furniture | pages [15] -->
2

<!-- b000377 | furniture | pages [15] -->
MATHmodels

<!-- b000378 | furniture | pages [15] -->
获取更多资讯

<!-- b000379 | furniture | pages [16] -->
Team # 2409404

<!-- b000380 | furniture | pages [16] -->
Page 16 of 25

<!-- b000382 | prose | pages [16] -->
• Modify your style of play to counter the opponent’s momentum，in other words，you are never in danger if you know yourself and your rival. To lessen the opponent’s momentum in the game and boost your own momentum in this situation, familiarize 微信公众号：数学模型 yourself with the opposing players and the situations in which their momentum will increase or decrease prior to the game. Increase the growth of the game’s direction and make appropriate modiﬁcations if you discover that the circumstances on the ﬁeld are favoring the opponent’s momentum. Concurrently, consider how you can lessen the opponent’s momentum. Aim for as many points as you can on crucial shots that slow down the opposition’s momentum.

<!-- b000383 | prose | pages [16] -->
• Utilize the two serves to your advantage. Even in the event of failure, there is always a second chance; in the event of a ﬁrst serve error, the second serve will go to the conservative main. In the ﬁrst serve, the ball’s speed and power present the biggest challenge to the high difﬁculty and high skills of the ace ball. When the other player serves for the ﬁrst time, prepare to hit the ball hard and quickly. Since your opponent’s 微信号：MATHmodels power and speed are reduced when he serves again, it is simpler to score if you launch a swift counterattack at this point.

<!-- b000384 | prose | pages [16] -->
• Focus on key points in the game. When a match reaches game point, set point, or a battle of seven, often a single point gained or lost can affect a dramatic shift in mo- mentum, which can change the course of the match.

<!-- b000385 | heading | pages [16] -->
6 Model Effect Analysis

<!-- b000386 | heading | pages [16] -->
6.1 Model Testing on a New Race

<!-- b000387 | prose | pages [16] -->
To evaluate the efﬁcacy of the established model in forecasting game volatility, we con- ducted a test using "2023-wimbledon-1701" as the subject of analysis. The subsequent cri- teria were taken into account:accuracy,Confuse Matrix Thermal Charts, the classiﬁcation report and Receiver Operating Characteristic the Curve.

<!-- b000388 | prose | pages [16] -->
• Accuracy: Accuracy refers to the proportion of accurate predictions in relation to the entire sample, i.e:

<!-- b000389 | prose | pages [16] -->
Acc = NTruePredict × 100 % (12) NSample Tests have shown that NTruePredict = 231, NSample = 334, therefore, Acc = 69.16 %.

<!-- b000390 | prose | pages [16] -->
• Confusion Matrix: The heat map displays the confusion matrix, where each row rep- resents the true category of the sample label, namely the actual value of the circum- stance ﬂuctuation. Each column represents the predicted category of the sample label, speciﬁcally the predicted value of the model. Hence, the total of the primary diago- nal elements in the matrix corresponds to the count of successfully predicted samples by the model. Furthermore, it is necessary to include four variables, namely TP, FN, FP, and TN, where T represents True and F represents False, indicating whether the predicted value matches the actual value; P represents Positive and N represents Neg- ative, showing whether the prediction falls into the positive or negative category. As

<!-- b000391 | prose | pages [16, 17] -->
关注数学模型 depicted in Figure 8, it is evident to see the prediction accuracy and error, as well as the level of distinction of the model for each group.

<!-- b000392 | furniture | pages [16] -->
2

<!-- b000393 | furniture | pages [16] -->
MATHmodels

<!-- b000394 | furniture | pages [16] -->
获取更多资讯

<!-- b000395 | furniture | pages [17] -->
Team # 2409404

<!-- b000396 | furniture | pages [17] -->
Page 17 of 25

<!-- b000398 | prose | pages [17] -->
1.0 TN FP 微信公众号：数学模型 0.8 100 117 37 0.755 0.633 0.689 1 0

<!-- b000399 | prose | pages [17] -->
0.6 Actual 80 0.4 FN TP 0.639 0.760 0.694 0 60 66 114 0.2 1

<!-- b000400 | prose | pages [17] -->
0.0 40 precision recall f1 0 1 Predicted

<!-- b000401 | caption | pages [17] -->
Figure 9: Classiﬁcation Report

<!-- b000402 | caption | pages [17] -->
Figure 8: Confusion Matrix

<!-- b000403 | prose | pages [17] -->
Observing the graph, we can see that the model is superior for predicting the ﬂuctua- tions of the game, with the main diagonal elements making up the majority, but there 微信号：MATHmodels are some limitations, perhaps in the difﬁculty of identifying changes at key points.

<!-- b000404 | prose | pages [17] -->
• Classiﬁcation Rport: The classiﬁcation report computes the Precision, Recall, and F1 −score for each category in the model. In the visualization graph, deeper colors imply higher values, which correspond to better results, as depicted in Figure 9. Three examples of metrics calculation are given below:

<!-- b000405 | prose | pages [17] -->
– Precision is the percentage of correctness for all predictions in the positive cate- gory.

<!-- b000406 | prose | pages [17] -->
TP 114 Precision1 = TP + FP = 114 + 37 = 0.755 (13)

<!-- b000407 | prose | pages [17] -->
– Recall refers to the ratio of correctly identiﬁed positive categories out of all the actual positive categories.

<!-- b000408 | prose | pages [17] -->
TP 114 Recall1 = TP + FN = 114 + 66 = 0.633 (14)

<!-- b000409 | prose | pages [17] -->
– F1-score is calculated as the harmonic mean of Precision and Recall.

<!-- b000410 | prose | pages [17] -->
F11 = 2 × Precision × Recall = 2 × 0.755 × 0.633 = 0.689 (15) Precision + Recall 0.755 + 0.633

<!-- b000411 | prose | pages [17] -->
In binary class classiﬁcation, it is desirable to have a balanced distribution of positive and negative class samples. Additionally, a higher F1-score indicates better perfor- mance in both Precision and Recall of the model.

<!-- b000412 | prose | pages [17] -->
• Receiver Operating Characteristic (ROC) Curve: The ROC curverepresents the rela- tionship between the sensitivity and speciﬁcity of the model. It shows the false posi- tive rate (FPR) for each category on the horizontal axis and the true positive rate (TPR) on the vertical axis. Hence, the optimal point of this curve is situated in the top left corner, namely when the false positive rate (FPR) equals zero and the true positive rate (TPR) equals one. This indicates a more favorable impact of magic. Furthermore, another crucial statistic that may be derived is the area under the curve (AUC), which indicates the effectiveness of the model. A bigger AUC value signiﬁes a more effec- tive model. Prior to plotting this image, it is imperative that we grasp the underlying

<!-- b000413 | prose | pages [17, 18] -->
关注数学模型 measures.

<!-- b000414 | furniture | pages [17] -->
2

<!-- b000415 | furniture | pages [17] -->
MATHmodels

<!-- b000416 | furniture | pages [17] -->
获取更多资讯

<!-- b000417 | furniture | pages [18] -->
Team # 2409404

<!-- b000418 | furniture | pages [18] -->
Page 18 of 25

<!-- b000420 | prose | pages [18] -->
– Sensitivity: The deﬁnition of sensitivity, also known as the True-Positive rate, is follows: TP

<!-- b000421 | heading | pages [18] -->
Sensitivity = TPR =

<!-- b000422 | prose | pages [18] -->
微信公众号：数学模型 (16) TP + FN – Speciﬁcity: The True-Negative rate, is also known as speciﬁcity and is deﬁned as: TN Speciﬁcity = TNR = (17) TN + FP – 1−Speciﬁcity: It is referred to as the False-Positive rate, deﬁned as:

<!-- b000423 | prose | pages [18] -->
FP FPR = 1 −Speciﬁcity = (18) FP + TN

<!-- b000424 | prose | pages [18] -->
– 1−Sensitivity: It is called False-Negative rate, deﬁned as:

<!-- b000425 | prose | pages [18] -->
FN 微信号：MATHmodels

<!-- b000426 | heading | pages [18] -->
FNR = 1 −Sensitivity =

<!-- b000427 | prose | pages [18] -->
(19) FN + TP

<!-- b000428 | prose | pages [18] -->
To illustrate this model, we graph its ROC curve, depicted in Figure x. Upon exam- ining the graph, it is evident that the curve exhibits a tendency towards approaching the point (0, 1) more closely. Additionally, the AUC (Area Under the Curve) for the two categories is calculated to be 0.75. Furthermore, we have also computed the AUC for both micro-average and macro-average, both of which yield a value of 0.75. This indicates that the performance of the established model is relatively satisfactory.

<!-- b000429 | prose | pages [18] -->
1.0

<!-- b000430 | prose | pages [18] -->
0.8 True Positive Rate ROC of class 0, AUC = 0.75 0.6 ROC of class 1, AUC = 0.75 micro-average ROC curve, AUC = 0.75 0.4 macro-average ROC curve, AUC = 0.75

<!-- b000431 | prose | pages [18] -->
0.2

<!-- b000432 | prose | pages [18] -->
0.0 0.0 0.2 0.4 0.6 0.8 1.0 False Positive Rate

<!-- b000433 | caption | pages [18] -->
Figure 10: The ROC curve

<!-- b000434 | prose | pages [18] -->
According to the analysis provided, it can be determined that the developed model has a certain degree of accuracy in predicting changes in the game’s trend. Nevertheless, there remain numerous enhancements to be made to the model in order to enhance the accuracy of the prediction. Here, we will explicitly study it by focusing on a particular women’s singles match at the US Open.

<!-- b000435 | prose | pages [18] -->
Generalized Ability Analysis —U.S. Open Women’s Singles 6.2

<!-- b000436 | prose | pages [18] -->
For the purpose of evaluating the model’s capacity to make generalizations, we have selected the match between C. Gauff and A. Sabalenka, which took place on September 9,

<!-- b000437 | prose | pages [18, 19] -->
关注数学模型 2023, as the women’s singles ﬁnal of the U.S. Open, for our analysis. Initially, we quantiﬁed the technical components of the match, as depicted in Figure 11.

<!-- b000438 | furniture | pages [18] -->
2

<!-- b000439 | furniture | pages [18] -->
MATHmodels

<!-- b000440 | furniture | pages [18] -->
获取更多资讯

<!-- b000441 | furniture | pages [19] -->
Team # 2409404

<!-- b000442 | furniture | pages [19] -->
Page 19 of 25

<!-- b000444 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000445 | heading | pages [19] -->
C. Gauff

<!-- b000446 | prose | pages [19] -->
A. Sabalenka 2 ACES 4 DOUBLE FAULTS 5 6 13 25 WINNERS 74 TOTAL POINTS WON 83 UNFORCED ERRORS 19 46 DISTANCE COVERED 8702.4 ft 8806.5 ft 55.4 ft DISTANCE COVERED/PT. 56.1 ft FIRST SERVE % IN 52% 66% 62% 65% WIN % ON 1ST SERVE WIN % ON 2ND SERVE 52% 41% BREAK POINTS WON 56% 40% NET POINTS WON 70% 62% 47% 41% RECEIVING POINTS WON

<!-- b000447 | caption | pages [19] -->
Figure 11: Technical Statistics

<!-- b000448 | prose | pages [19] -->
微信号：MATHmodels By examining the graph, it is evident that Gauff exhibits a notable reduction in unforced errors compared to Sabalenka. However, there is minimal disparity between the two players in terms of other statistics, such as distance covered and serve performance. Gauff gets defeated by Sabalenka’s unforced errors.

<!-- b000449 | prose | pages [19] -->
We integrate the momentum quantitative model with the match ﬂuctuation prediction model and generate visualizations in the form of a ﬂowchart and scatterplot for the corre- sponding match, as depicted in Figure 12 and Figure 13.

<!-- b000450 | prose | pages [19] -->
20 Gauff 2     6     6 Sabalenka 6     4     2 15 C. Gauff's Momentum 10 A. Sabalenka's Momentum Momentum C. Gauff's Game Point 5 A. Sabalenka's Game Point C. Gauff's Turning Point 0 A. Sabalenka's Turning Point 5 10 0 1000 2000 3000 4000 5000 6000 7000 Elapsed Time (seconds)

<!-- b000451 | caption | pages [19] -->
Figure 12: Match Flow

<!-- b000452 | prose | pages [19] -->
20 15 15 15 10 10 10 A. Sabalenka Momentum C. Gauff 5 5 5

<!-- b000453 | prose | pages [19] -->
0 0 0 5 5 5 10 10 0 1000 2000 3000 4000 5000 6000 7000 Elapsed Time (seconds)

<!-- b000454 | caption | pages [19] -->
Figure 13: Match Flow Scatter

<!-- b000455 | prose | pages [19, 20] -->
关注数学模型 Upon analyzing the visualization with the score changes, it becomes evident that the momentum also inﬂuences the trajectory of the women’s singles match. In the initial set, Sabalenka consistently maintained a lead over Gauff by scoring consecutive points. With her strong momentum, Sabalenka easily secured victory in the ﬁrst set. However, start- 微信公众号：数学模型 ing with the second set, Sabalenka began to commit unforced errors, resulting in a shift of momentum in favor of Gauff. At this juncture, the disparity in momentum was not signif- icant; hence, Guaff emerged victorious in the second set by a narrow margin. Sabalenka’s signiﬁcant decline in momentum throughout the third set was primarily due to her high number of unforced errors. Consequently, she suffered a substantial defeat in the third set. Meanwhile, it is observed that Guaff consistently exhibits a larger average momentum than Sablenka throughout the match. Furthermore, the distribution of momentum in the sets won by Guaff is notably greater than that of Sablenka, as depicted in the scatterplot.

<!-- b000456 | furniture | pages [19] -->
2

<!-- b000457 | furniture | pages [19] -->
MATHmodels

<!-- b000458 | furniture | pages [19] -->
获取更多资讯

<!-- b000459 | furniture | pages [20] -->
Team # 2409404

<!-- b000460 | furniture | pages [20] -->
Page 20 of 25

<!-- b000462 | prose | pages [20] -->
Through the above analysis, combined with the technical statistics, the actual situation of the game, and the visualization of the game ﬂow, we can ﬁnd that the established model can be adapted to different types of games, with an excellent generalization ability. 微信号：MATHmodels

<!-- b000463 | heading | pages [20] -->
6.3 Future Consideration

<!-- b000464 | prose | pages [20] -->
Through the above analysis, we can ﬁnd that the model works better. However, there are still some deﬁciencies that need to be considered in future models, which are summa- rized.

<!-- b000465 | prose | pages [20] -->
• The result of the referee’s call. Referees and players may not be consistent in their judgment of the game scenarios, and it is reasonable to expect wrong judgments, mis- judgments, and disputes. When the penalties exceed the coaches’ and athletes’ pre- game preparation and past experience, it will sharply reduce the momentum, leading to a critical response, disrupting the pre-game tactical deployment, and causing heart ﬂuctuations.

<!-- b000466 | prose | pages [20] -->
• The athlete’s ability to self-adjust. Under high competition stress conditions, ath- letes’ psychological reactions are different from normal, and their emotional reactions are richer, which will lead to changes in their own momentum. However, the self- adjustment ability of different athletes varies greatly. Some athletes can quickly detach from the low momentum and reduce the impact of the momentum on themselves, while others have poor self-adjustment abilities and will be immersed in the low mo- mentum for a long time.

<!-- b000467 | prose | pages [20] -->
• The level of the opponent. If your athlete has lost to the other athlete, or if the other athlete is a veteran whose strength is well known to the public, your athlete will over- estimate the opponent’s strength and develop fear and stage fright, which will seri- ously reduce your momentum.

<!-- b000468 | prose | pages [20] -->
• Coach’s guidance. When an athlete’s momentum appears to diminish and affect his or her game form, effective coaching and reassurance from the coach can enable the athlete to regain his or her form and stabilize his or her momentum.

<!-- b000469 | prose | pages [20] -->
• Type of venue. The probability of winning varies somewhat from athlete to athlete at different venues. For example, on hard courts, the Russians, Americans, and French

<!-- b000470 | prose | pages [20, 21] -->
关注数学模型 win the most matches. Looking at clay courts, Russians, Americans, and French are in the top three. On turf courts, Americans, Russians, and Australians are in the top three. On carpeted grounds, the Russians, the French, and the Australians take the top three spots. This has to do with their country’s training grounds; when an athlete 微信公众号：数学模型 plays on a ﬁeld they are familiar with, their momentum will increase and it will be easier to get into shape.

<!-- b000471 | furniture | pages [20] -->
2

<!-- b000472 | furniture | pages [20] -->
MATHmodels

<!-- b000473 | furniture | pages [20] -->
获取更多资讯

<!-- b000474 | furniture | pages [21] -->
Team # 2409404

<!-- b000475 | furniture | pages [21] -->
Page 21 of 25

<!-- b000477 | prose | pages [21] -->
• Spectators’ applause. When a player scores a point and the audience cheers for him, the player not only increases his momentum by scoring a point, but the audience’s applause also increases his momentum, and his status will be better in the following game. If a player loses points and the audience boos or even applauds because of dissatisfaction, the player’s momentum will be seriously affected, and his or her game status will be in tatters.

<!-- b000478 | heading | pages [21] -->
7 Sensitivity Analysis

<!-- b000479 | prose | pages [21] -->
微信号：MATHmodels In order to quantitatively model momentum, we have already determined two signif- icant factors: the sliding window size, denoted as β, and the out-of-play advantage of a player’s serve, denoted as α. These parameters are now being modiﬁed to simulate various types of matches with varied serve advantages. Previously, we computed the momentum for each player. To enhance the presentation of the ﬁndings, we calculate the disparity in momentum between two players. Assuming player 1 as his reference point, when the curve is situated below the horizontal axis, it indicates that momentum is located on the other side, and vice versa. As depicted in Figure 14 and Figure 15.

<!-- b000480 | prose | pages [21] -->
30 α = 0.5, β = 5 Momentum Difference α = 0.6, β = 5 20 α = 0.7, β = 5 10 α = 0.8, β = 5 0 10 20 30 0 2000 4000 6000 8000 10000 12000 14000 16000 Elapsed Time (seconds)

<!-- b000481 | caption | pages [21] -->
Figure 14: The Sensitivity Test for α

<!-- b000482 | prose | pages [21] -->
30 α = 0.68, β = 3 Momentum Difference α = 0.68, β = 4 20 α = 0.68, β = 5 10 α = 0.68, β = 6 0 10 20 30 0 2000 4000 6000 8000 10000 12000 14000 16000 Elapsed Time (seconds)

<!-- b000483 | caption | pages [21] -->
Figure 15: The Sensitivity Test for β

<!-- b000484 | prose | pages [21] -->
Upon examining the aforementioned graphs, it is evident that when subjected to a

<!-- b000485 | prose | pages [21, 22] -->
关注数学模型 speciﬁc perturbation of α and β, the disparity in the players’ momentum undergoes a dis- cernible alteration, particularly when β is modiﬁed. However, overall, the momentum’s trajectory stays unaltered. Put simply, the model effectively captures the player’s condition over various matches. Hence, it is logical and justiﬁable that the curve may undergo signiﬁ- 微信公众号：数学模型 cant changes at certain nodes. The pattern of the sensitivity test curve aligns with the actual condition once again, overall.

<!-- b000486 | furniture | pages [21] -->
2

<!-- b000487 | furniture | pages [21] -->
MATHmodels

<!-- b000488 | furniture | pages [21] -->
获取更多资讯

<!-- b000489 | furniture | pages [22] -->
Team # 2409404

<!-- b000490 | furniture | pages [22] -->
Page 22 of 25

<!-- b000492 | heading | pages [22] -->
8 Model Evaluation

<!-- b000493 | heading | pages [22] -->
8.1 Strengths

<!-- b000494 | prose | pages [22] -->
• The model is systematic. When selecting metrics for the purpose of calculating mo- mentum, this model encompasses the entirety of the race, rather than examining only a single segment. Makes the results more relevant. 微信号：MATHmodels

<!-- b000495 | prose | pages [22] -->
• When calculating the momentum, the scores of both the enemy and the opponent are considered at the same time, and the calculation results are more in line with the reality.

<!-- b000496 | prose | pages [22] -->
• When studying whether the momentum will have an impact on the game situation, two models, namely, the tour test and the chi-square test, were used for comparative analysis, so as to make the results more accurate.

<!-- b000497 | prose | pages [22] -->
• The distribution of data was obtained through principal component analysis to deter- mine the XGboost prediction model, which resulted in a higher accuracy of prediction.

<!-- b000498 | heading | pages [22] -->
8.2 Weaknesses and Improvements

<!-- b000499 | prose | pages [22] -->
• This model is only applicable to individual matches. Team momentum is not simply the sum of individual momentum, if we want to solve the momentum problem of group matches, then we also need to consider the impact of teammates’ scores or losses on each other’s momentum.

<!-- b000500 | prose | pages [22] -->
• When making predictions, optimisation algorithms such as Bayesian tuning can be combined to further optimise the model hyper-parameters in order to improve predic- tion accuracy. The main method is to ﬁt a proxy model with known hyperparameters x and model results y, then use the acquisition function to select the next best (x, y), and use this new (x, y) to optimise the proxy model, repeat the above process, and ﬁnally obtain the tuned parameters.

<!-- b000501 | heading | pages [22] -->
9 Conclusion

<!-- b000502 | prose | pages [22] -->
Initially, we constructed a momentum quantiﬁcation model using a sliding-window approach. This involved specifying the size of the sliding window and evaluating the mo- mentum value of a player by considering their performance in each metric during that win- dow. In the model, we incorporate the extra beneﬁt of the player’s serve to replicate the

<!-- b000503 | prose | pages [22, 23] -->
关注数学模型 fact that in a tennis match, the serving player has a greater likelihood of winning. Simul- taneously, we analyze the crucial aspects of the match, from which we generate a visual representation of the match’s progression. This visualization allows for a clear assessment of the status and exceptional performance of each player. 微信公众号：数学模型 Subsequently, by employing the run test and chi-square test, it was determined that momentum plays a pivotal role in the game dynamics of tennis. Hence, it is imperative for coaches and players to acknowledge the signiﬁcance of momentum.

<!-- b000504 | furniture | pages [22] -->
2

<!-- b000505 | furniture | pages [22] -->
MATHmodels

<!-- b000506 | furniture | pages [22] -->
获取更多资讯

<!-- b000507 | furniture | pages [23] -->
Team # 2409404

<!-- b000508 | furniture | pages [23] -->
Page 23 of 25

<!-- b000510 | prose | pages [23] -->
Afterwards, the data distribution is examined through principal component analysis in order to construct a game ﬂuctuation prediction model using XGBoost. This model exhibits a higher level of accuracy, reaching up to 70 %, in predicting changes in game situations. Additionally, it identiﬁes signiﬁcant factors such as Double Fault, ACE, and consecutive scores of players.

<!-- b000511 | prose | pages [23] -->
On this basis, we evaluate the model, assess its capacity to generalize, and conduct sensitivity tests on the US Open women’s singles matches. The analysis indicates that the 微信号：MATHmodels model exhibits exceptional performance, possesses a high degree of generalization, demon- strates resilience, and can be easily modiﬁed for application to different types of matches. Furthermore, we provide an enumeration of the aspects that ought to be taken into account in the future to enhance the model.

<!-- b000512 | prose | pages [23] -->
Ultimately, we furnish tennis coaches with insights into the signiﬁcance of momentum and offer guidance on how players can sustain and control momentum throughout a match.

<!-- b000513 | heading | pages [23] -->
References

<!-- b000514 | references | pages [23] -->
[1] Ben Moss and Peter O’Donoghue. Momentum in us open men’s singles tennis. Interna-

<!-- b000515 | references | pages [23] -->
tional Journal of Performance Analysis in Sport, 15(3):884–896, 2015.

<!-- b000516 | references | pages [23] -->
[2] Xiaofei Zhang. Analysis of the characteristics of the key distribution points of world

<!-- b000517 | references | pages [23] -->
elite male tennis players. Master’s thesis, Guangzhou Sport University, 2019.

<!-- b000518 | references | pages [23] -->
Periodic "Fluctuate" Phenomenon of Resisting Event-Group Performance in

<!-- b000519 | references | pages [23] -->
[3] Liang Chen.

<!-- b000520 | references | pages [23] -->
Match. PhD thesis, Soochow University, 2013.

<!-- b000521 | references | pages [23] -->
[4] Jianwei Sun, Bianli Xu, Jia Su, and Xueyong Huang. Application and discussion on runs

<!-- b000522 | references | pages [23] -->
test in epidemiology. Preventive Medicine Tribune, 23(100-103+106), 2017.

<!-- b000523 | references | pages [23] -->
关注数学模型

<!-- b000524 | furniture | pages [23] -->
2

<!-- b000525 | furniture | pages [23] -->
MATHmodels

<!-- b000526 | furniture | pages [23] -->
获取更多资讯

<!-- b000527 | furniture | pages [24] -->
Team # 2409404

<!-- b000528 | furniture | pages [24] -->
Page 24 of 25

<!-- b000529 | heading | pages [24] -->
Memorandum

<!-- b000530 | prose | pages [24] -->
To: Tennis Coaches and Players

<!-- b000531 | prose | pages [24] -->
From: Team # 2409404 微信公众号：数学模型 Date: Feb 5, 2024

<!-- b000532 | prose | pages [24] -->
Subject: Momentum Comprehension, Momentum Mastery, and Momentum Application

<!-- b000533 | prose | pages [24] -->
Dear sir or madam:

<!-- b000534 | prose | pages [24] -->
Everyone desires success on the court, and our research indicates that momentum could be of assistance to you. In order to aid in the training of you and your players, we have developed a predictive model of the situation during a match and a quantitative model of players' momentum. Moreover, it furnishes players with constructive guidance 微信号：MATHmodels on how to adapt to the ever-changing circumstances that transpire on the playing field.

<!-- b000535 | prose | pages [24] -->
We have determined, through an analysis of past tennis matches, that momentum is a critical factor in the sport. Tennis players have the ability to reverse the ultimate result of a match by utilizing the force of momentum. A participant with momentum will experience a sense that everything is proceeding in their favor. Additionally, the player will be playing with increased assurance at this juncture, and the momentum will assist in sustaining that assurance. A player should continue to execute the shots that help him or her acquire momentum in tennis—perhaps aggressive play or solid play—in order to maintain momentum and thus play tennis fearlessly.

<!-- b000536 | prose | pages [24] -->
The Momentum quantification model generates specific values by measuring each participant's momentum values at every instant to determine who is performing better at a particular moment in the match. Given the significant degree of unpredictability surrounding the trajectory of the match, this model employs the concept of a sliding window, which comprises two critical parameters: the sliding window's magnitude and the additional benefit that a player's serve can confer. It is adaptable and can be modified in accordance with various contests. The in-match situation prediction model can provide real-time forecasts of the match's fluctuating trajectory and identify significant influencing factors, including the player's Double Fault, ACE, and other relevant data.

<!-- b000537 | prose | pages [24] -->
Furthermore, the majority of Momentum's fluctuations transpire when a player assumes the initiative and endeavors to maintain it throughout the course of the game.

<!-- b000538 | prose | pages [24, 25] -->
关注数学模型 During this phase of the game, participants are averse to losing their lead and are reluctant to relinquish it. A shift in momentum does not warrant a loss of confidence in the game. Maintaining perseverance and a positive mindset are critical factors in regaining the upper 微信公众号：数学模型 hand. However, the player might be required to alter their playing manner or return to their initial approach to the game.

<!-- b000539 | furniture | pages [24] -->
2

<!-- b000540 | furniture | pages [24] -->
MATHmodels

<!-- b000541 | furniture | pages [24] -->
获取更多资讯

<!-- b000542 | furniture | pages [25] -->
Team # 2409404

<!-- b000543 | furniture | pages [25] -->
Page 25 of 25

<!-- b000545 | prose | pages [25] -->
Based on our analysis of the results, we propose the following recommendations (strategies):

<!-- b000546 | prose | pages [25] -->
In order to mitigate the impact of referee errors, missed opportunities, and other  such occurrences on players' confidence, coaches ought to prioritize the cultivation of psychological qualities. This entails supporting players in maintaining a positive outlook, exercising patience, and having self-belief throughout the game.

<!-- b000547 | prose | pages [25] -->
微信号：MATHmodels A diversity of venues should be covered in player training so that players do not  become nervous when playing in unfamiliar areas.

<!-- b000548 | prose | pages [25] -->
Players ought to allocate physical energy judiciously; if physical energy is  consumed too rapidly, the momentum value will remain in a comparatively low state.

<!-- b000549 | prose | pages [25] -->
Analyze the playing technique of your opponent prior to the match and adjust  your strategy accordingly to gain momentum on the field.

<!-- b000550 | prose | pages [25] -->
Standardization of movements and techniques is required, and training must be  reinforced.

<!-- b000551 | prose | pages [25] -->
Of course, our model only plays the role of prediction, but it can be enough to help you. Thank you for reading our memo again in your busy schedule, and we hope our suggestions are useful to you!

<!-- b000552 | prose | pages [25] -->
Yours Sincerely,

<!-- b000553 | furniture | pages [25] -->
Team # 2409404

<!-- b000554 | prose | pages [25] -->
关注数学模型

<!-- b000555 | furniture | pages [25] -->
2

<!-- b000556 | furniture | pages [25] -->
MATHmodels

<!-- b000557 | furniture | pages [25] -->
获取更多资讯
