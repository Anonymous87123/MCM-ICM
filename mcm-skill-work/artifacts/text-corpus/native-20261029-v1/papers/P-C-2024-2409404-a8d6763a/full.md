# P-C-2024-2409404-a8d6763a

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
For task two, we need to examine the impact of "momentum" on the game and deter- mine if the ﬂuctuations in the game condition and successive player scores are random. Thus, we begin by examining the volatility of the game’s condition using the Point Vic- tor factor and the MQ-SW Model. Subsequently, we employ the Runs Test to assess the state of the game and the successive scores of the participants. Upon computation, the

<!-- b000016 | prose | pages [1] -->
p −value < 0.01, indicating that the variability in the game scenario. Next, we discretize the momentum of both players at each instance and employ the Chi-square Test to com- pare the aforementioned indices. The experimental p −value < 0.01, indicating that the "momentum" element is highly likely to be the reason, as demonstrated in Table 5.

<!-- b000017 | prose | pages [1] -->
For task three, we need to predict the volatility of the circumstances in a tennis match. The dependent variable is the discretized "momentum", whereas the independent variables consist of other factors associated with players. We established the Prediction for Match Trend Model Based on PCA&XGBoost (PMT-PX). The model uses the principal compo- nent analysis to examine the variation in scatter on a two-dimensional coordinate graph and subsequently utilizes XGBoost to train on the match data. From this, we have identi- ﬁed the most signiﬁcant inﬂuencing factors, namely "Point Victor" and "Break PT" at the current moment. The corresponding scores are displayed in Table 6.

<!-- b000018 | prose | pages [1] -->
For task four, it requires an examination of the model’s effect and its capacity to general- ize. We assess the model using several metrics, such as the confusion matrix, classiﬁcation report, and ROC curve. The area under the curve (AUC) is 0.75, indicating a discernible ef- fect. We utilize the model to evaluate the U.S. Open women’s ﬁnal. The results indicate that the model exhibits a commendable level of generalization and is capable of efﬁciently and accurately identifying the target. Simultaneously, we conduct an analysis of the model’s drawbacks and provide the elements that should be taken into account in the future. Fur- thermore, the model sensitivity analysis is conducted by altering the dimensions of the sliding window along with the additional advantage parameter of the player’s serve. The outcomes indicate that the model exhibits a high level of robustness.

<!-- b000019 | prose | pages [1] -->
We ﬁnally write a memorandum, including our model and strategy, for the coaches and players. We hope our memorandum can be valuable to them and actually help them.

<!-- b000020 | keywords | pages [1] -->
Keywords: Momentum, MQ-SW, Runs Test, Chi-square Test, PMT-PX

<!-- b000021 | prose | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team # 2409404

<!-- b000026 | furniture | pages [2] -->
Page 2 of 25

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1

<!-- b000029 | heading | pages [2] -->
Introduction

<!-- b000030 | prose | pages [2] -->
3 Probelm Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000031 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000032 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 4 Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000033 | prose | pages [2] -->
2

<!-- b000034 | heading | pages [2] -->
Preparation of the Models

<!-- b000035 | prose | pages [2] -->
4

<!-- b000036 | prose | pages [2] -->
5 Assumptions and Explanations . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 5 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 Data Preparation 5 Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.2 Data Pre-processing 6

<!-- b000037 | heading | pages [2] -->
Establish the Momentum Quantization Model Based on Sliding Windows

<!-- b000038 | prose | pages [2] -->
3 6

<!-- b000039 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000040 | prose | pages [2] -->
Quantization of Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 6 Identiﬁcation of Key Points in the Game . . . . . . . . . . . . . . . . . . . . . . 3.2 7 Competition Flow Visualization . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 8

<!-- b000041 | prose | pages [2] -->
Momentum’s Impact on the Game Situation 4 10 The Runs Test —Stochastic Analysis . . . . . . . . . . . . . . . . . . . . . . . . 4.1 10 The Chi-square Test —Correlation Analysis . . . . . . . . . . . . . . . . . . . . 4.2 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Reach a Verdict 12

<!-- b000042 | heading | pages [2] -->
Establish the Prediction for Match Trend Model Based on PCA&XGBoost

<!-- b000043 | prose | pages [2] -->
5 12 Principal Component Analysis —Determine the Model . . . . . . . . . . . . . 5.1 12 XGBoost —Match Trend Prediction . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 Factor Importance Extraction 14 Tactical Suggestions for the Game . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4

<!-- b000044 | prose | pages [2] -->
6

<!-- b000045 | heading | pages [2] -->
Model Effect Analysis

<!-- b000046 | prose | pages [2] -->
15

<!-- b000047 | prose | pages [2] -->
16 Model Testing on a New Race . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 16 Generalized Ability Analysis —U.S. Open Women’s Singles 6.2 . . . . . . . . . .

<!-- b000048 | prose | pages [2] -->
18 Future Consideration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000049 | prose | pages [2] -->
7

<!-- b000050 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000051 | prose | pages [2] -->
8

<!-- b000052 | heading | pages [2] -->
Model Evaluation

<!-- b000053 | prose | pages [2] -->
20

<!-- b000054 | prose | pages [2] -->
21

<!-- b000055 | prose | pages [2] -->
22 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 22 Weaknesses and Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000056 | prose | pages [2] -->
9

<!-- b000057 | heading | pages [2] -->
Conclusion

<!-- b000058 | heading | pages [2] -->
References

<!-- b000059 | heading | pages [2] -->
Memorandum

<!-- b000060 | prose | pages [2] -->
22

<!-- b000061 | prose | pages [2] -->
22

<!-- b000062 | prose | pages [2] -->
23

<!-- b000063 | prose | pages [2] -->
24

<!-- b000064 | prose | pages [2] -->
关注数学模型

<!-- b000065 | furniture | pages [2] -->
2

<!-- b000066 | furniture | pages [2] -->
MATHmodels

<!-- b000067 | furniture | pages [2] -->
获取更多资讯

<!-- b000068 | furniture | pages [3] -->
Team # 2409404

<!-- b000069 | prose | pages [3] -->
1

<!-- b000070 | heading | pages [3] -->
Introduction

<!-- b000071 | prose | pages [3] -->
1.1 Probelm Background

<!-- b000072 | furniture | pages [3] -->
Page 3 of 25

<!-- b000073 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000074 | prose | pages [3] -->
In the men’s singles ﬁnal of the 2023 Wimbledon Open, Spanish rising star Carlos Al- caraz ended Novak Djokovic’s legendary player’s unbeaten run at Wimbledon since 2013. So What factors inﬂuenced the outcome of this seemingly unbalanced match?What factors contribute to the occurrence of analogous scenarios for individuals or players who appear to have a dominant position in the situation or game? Indeed, these conclusions are frequently ascribed to the phenomenon of "momentum".

<!-- b000075 | prose | pages [3] -->
Momentum is deﬁned in the dictionary as "strength or force gained by motion or by a series of events", but in actual sports, a team or player may feel energized during a game, but it is difﬁcult to accurately measure this phenomenon. Furthermore, assuming that such momentum exists, it is difﬁcult to determine how the various events of a game generate

<!-- b000076 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000077 | prose | pages [3] -->
or alter momentum. So, is there a computable and estimable frontal model of momentum available to aid players in achieving improved outcomes?

<!-- b000078 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000079 | prose | pages [3] -->
Given the problem’s background information and constrained conditions, we must complete the following tasks:

<!-- b000080 | prose | pages [3] -->
• Task 1: Build a model that captures the ﬂow of the match as it occurs and apply it to one or more matches to visualize the ﬂow of the match. The model needs to be able to identify the time period in the match when a player performs better and the degree of excellence within that time period. • Task 2: A coach is skeptical about the role of momentum, arguing that ﬂuctuations in match situations and consecutive wins by players occur randomly, use a model to evaluate this coach’s claim. • Task 3: Coaches need to be clear on whether there are indicators that can assist in determining when a game’s trend will shift.

<!-- b000081 | prose | pages [3] -->
– Using data from at least one match, build a model that predicts the movement

<!-- b000082 | prose | pages [3] -->
of a match and identify which factors, if any, have the greatest impact on the movement of a match. – Based on the difference in "momentum" in previous matches, help a player de-

<!-- b000083 | prose | pages [3] -->
termine the correct strategy for a new match against a different opponent. • Task 4: Test the current model in one or more other games and evaluate the model’s prediction of in-game ﬂuctuations; if the prediction is poor, can factors be identiﬁed for inclusion in future models? How generalizable is the model to other games, tour- naments, ﬁeld types, and other sports? • Task 5: Write a memo summarizing the ﬁndings. Explain to a coach the role of "mo- mentum" and make recommendations to prepare players for events that affect the course of a tennis match.

<!-- b000084 | prose | pages [3] -->
关注数学模型

<!-- b000085 | furniture | pages [3] -->
2

<!-- b000086 | furniture | pages [3] -->
MATHmodels

<!-- b000087 | furniture | pages [3] -->
获取更多资讯

<!-- b000088 | furniture | pages [4] -->
Team # 2409404

<!-- b000089 | prose | pages [4] -->
1.3 Literature Review

<!-- b000090 | furniture | pages [4] -->
Page 4 of 25

<!-- b000091 | prose | pages [4] -->
The situation of a tennis match is rapidly changing. In the face of the variability of environment, strategy, and process, momentum, a factor that may turn the match around,

<!-- b000092 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000093 | prose | pages [4] -->
has become a focus of research.

<!-- b000094 | prose | pages [4] -->
Ben Moss et al. argue that the uncertainty of the momentum effect in tennis, which may

<!-- b000095 | prose | pages [4] -->
[1]. In addition, if a

<!-- b000096 | prose | pages [4] -->
vary from player to player, needs to be considered at an individual level

<!-- b000097 | prose | pages [4] -->
player breaks his opponent’s serve when facing a game point, he is more likely to hold his serve in the next round of serve reception.

<!-- b000098 | prose | pages [4] -->
Zhang Xiaofei suggests that the gain or loss of a key score will have a serious impact on a player’s momentum, thus affecting the direction of the match. In the face of changes in the score, some players may increase their momentum, attack courageously, and take the initiative. While some players may attach too much importance to the change of score, and whenever they encounter the change of key score, their momentum may be reduced, and

<!-- b000099 | prose | pages [4] -->
[2].

<!-- b000100 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000101 | prose | pages [4] -->
then the game will turn around

<!-- b000102 | prose | pages [4] -->
Chen Liang suggests that there is a direct "attack-defense relationship" in tennis and that in order to win a match, one must maximize one’s own performance and inhibit one’s opponents to the maximum extent possible. Under the joint effect of oneself, opponent, and competition environment, the momentum of both sides usually will not remain stable during the competition, and the change of the contrast relationship will form the stage "rise

<!-- b000103 | prose | pages [4] -->
[3] of the competitive performance.

<!-- b000104 | prose | pages [4] -->
and fall"

<!-- b000105 | prose | pages [4] -->
In conclusion, momentum affects different players in different ways, which is impor- tant for the psychological support of athletes.

<!-- b000106 | prose | pages [4] -->
1.4 Our work

<!-- b000107 | prose | pages [4] -->
For ease of description and visualization, we have drawn a ﬂow chart (Figure 1) to represent our work.

<!-- b000108 | prose | pages [4] -->
Task 1

<!-- b000109 | prose | pages [4] -->
Prepare

<!-- b000110 | prose | pages [4] -->
Task 2

<!-- b000111 | prose | pages [4] -->
Quantification of the momentum

<!-- b000112 | prose | pages [4] -->
Data collection Data pre-processing

<!-- b000113 | prose | pages [4] -->
The Runs Test

<!-- b000114 | prose | pages [4] -->
Selection of

<!-- b000115 | prose | pages [4] -->
Set the size of

<!-- b000116 | prose | pages [4] -->
Weighing

<!-- b000117 | prose | pages [4] -->
Stochastic analysis of

<!-- b000118 | prose | pages [4] -->
player-related

<!-- b000119 | prose | pages [4] -->
the moving window

<!-- b000120 | prose | pages [4] -->
of indicators

<!-- b000121 | prose | pages [4] -->
situational fluctuations and

<!-- b000122 | prose | pages [4] -->
indicator factors

<!-- b000123 | prose | pages [4] -->
player continuity scores

<!-- b000124 | prose | pages [4] -->
Identification of key points in the game

<!-- b000125 | prose | pages [4] -->
Game Point

<!-- b000126 | prose | pages [4] -->
Correlation analysis of momentum

<!-- b000127 | prose | pages [4] -->
Tunning point of the momentum (CUSUM)

<!-- b000128 | prose | pages [4] -->
Chi-square Test

<!-- b000129 | prose | pages [4] -->
Visual analysis of match flows

<!-- b000130 | prose | pages [4] -->
Task 3

<!-- b000131 | prose | pages [4] -->
Task 4

<!-- b000132 | prose | pages [4] -->
Final

<!-- b000133 | prose | pages [4] -->
Testing of the Model

<!-- b000134 | prose | pages [4] -->
Prediction of the swings in the match

<!-- b000135 | prose | pages [4] -->
Advice for Coaches and Athletes

<!-- b000136 | prose | pages [4] -->
Classification

<!-- b000137 | prose | pages [4] -->
Confusion

<!-- b000138 | prose | pages [4] -->
PCA & XGBOOST

<!-- b000139 | prose | pages [4] -->
Matrix

<!-- b000140 | prose | pages [4] -->
Importance extraction

<!-- b000141 | prose | pages [4] -->
ROC Curve Report

<!-- b000142 | prose | pages [4] -->
Application capacity

<!-- b000143 | prose | pages [4] -->
of factors

<!-- b000144 | prose | pages [4] -->
Model Enhancement

<!-- b000145 | prose | pages [4] -->
Tactical suggestions for

<!-- b000146 | prose | pages [4] -->
（Prospects for the future）

<!-- b000147 | prose | pages [4] -->
the game

<!-- b000148 | caption | pages [4] -->
Figure 1: Flow chart of our work

<!-- b000149 | prose | pages [4] -->
关注数学模型

<!-- b000150 | furniture | pages [4] -->
2

<!-- b000151 | furniture | pages [4] -->
MATHmodels

<!-- b000152 | furniture | pages [4] -->
获取更多资讯

<!-- b000153 | furniture | pages [5] -->
Team # 2409404

<!-- b000154 | prose | pages [5] -->
2

<!-- b000155 | heading | pages [5] -->
Preparation of the Models

<!-- b000156 | prose | pages [5] -->
2.1

<!-- b000157 | heading | pages [5] -->
Assumptions and Explanations

<!-- b000158 | furniture | pages [5] -->
Page 5 of 25

<!-- b000159 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000160 | prose | pages [5] -->
To simplify the issue, we have made the following assumptions, each of which is ap- propriately reasonable.

<!-- b000161 | prose | pages [5] -->
• Assumption 1: The entire game is not affected by external factors such as unfair deci- sions by the referee. ,→Explanation: An unfair judgement by the referee will mislead our judgement of the player’s score, thus not accurately calculating the impact of momentum on the athlete. • Assumption 2: Players were in good physical condition throughout the game.

<!-- b000162 | prose | pages [5] -->
,→Explanation: Physical condition will affect an athlete’s performance in a game, while existing data makes it difﬁcult to measure a player’s moment-to-moment con-

<!-- b000163 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000164 | prose | pages [5] -->
dition. • Assumption 3: The athlete has not used illegal drugs such as doping and has not cheated in competition. ,→Explanation: Doping can substantially increase an athlete’s level of competitive- ness, deviating from reality and affecting the calculation of momentum. Doping is also strictly prohibited in competition.

<!-- b000165 | prose | pages [5] -->
2.2

<!-- b000166 | heading | pages [5] -->
Notations

<!-- b000167 | prose | pages [5] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000168 | caption | pages [5] -->
Table 1: Notations

<!-- b000169 | heading | pages [5] -->
Symbol

<!-- b000170 | prose | pages [5] -->
α

<!-- b000171 | prose | pages [5] -->
Deﬁnition

<!-- b000172 | prose | pages [5] -->
Extra Advantages of the Player’s Serve β Sliding Window Size i Scoring Moment E(·) Data Average V(·) Data Variance

<!-- b000173 | prose | pages [5] -->
* Some variables are not listed here because they have different meanings in different places, so we will discuss them in detail in each section.

<!-- b000174 | prose | pages [5] -->
2.3

<!-- b000175 | heading | pages [5] -->
Data Preparation

<!-- b000176 | prose | pages [5] -->
2.3.1

<!-- b000177 | heading | pages [5] -->
Data Collection

<!-- b000178 | prose | pages [5] -->
To enhance the credibility of our analysis, we have gathered a substantial quantity of information from the following sources, in addition to the data provided by the contest questions. Refer to Table 2.

<!-- b000179 | prose | pages [5] -->
The data from the US Open Women’s Singles Final between C. Gauff and A. Sabalenka

<!-- b000180 | prose | pages [5] -->
关注数学模型

<!-- b000181 | furniture | pages [5] -->
2

<!-- b000182 | furniture | pages [5] -->
MATHmodels

<!-- b000183 | furniture | pages [5] -->
获取更多资讯

<!-- b000184 | furniture | pages [6] -->
Team # 2409404

<!-- b000185 | furniture | pages [6] -->
Page 6 of 25

<!-- b000186 | prose | pages [6] -->
on September 9, 2023, were collected using mathematical statistics and video observation methods to assess the model’s ability to make generalizations.

<!-- b000187 | caption | pages [6] -->
Table 2: Data Sources and Websites

<!-- b000188 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000189 | heading | pages [6] -->
Data Source

<!-- b000190 | prose | pages [6] -->
Website

<!-- b000191 | prose | pages [6] -->
https://sports.cctv.com/ CCTV https://www.usopen.org/index.html US Open https://www.wimbledon.com/en_GB/index.html Wimbledon

<!-- b000192 | prose | pages [6] -->
2.3.2 Data Pre-processing

<!-- b000193 | prose | pages [6] -->
Upon gathering and arranging the data, it becomes apparent that there are discrep- ancies between the data’s format and the data provided in the question. Therefore, it is imperative to preprocess the necessary data. Initially, the data header is standardized and the indicators are abbreviated to simplify the following listing. The corresponding details can be found in Table 3. Furthermore, it has been discovered that there are gaps in the mea-

<!-- b000194 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000195 | prose | pages [6] -->
surements of "winner shot type", "serve width", "serve depth", and "return depth". Based on the data analysis, the vacancies are attributed to the lack of such occurrences, so we re- place them with a value of zero. Furthermore, it was discovered that the aforementioned indicators consisted of text-based categorical data. Therefore, the implementation of Label Encoder processing was deemed necessary, which involves providing a distinct numerical value to each category.

<!-- b000196 | caption | pages [6] -->
Table 3: Abbreviations for factors

<!-- b000197 | prose | pages [6] -->
Former Glossary Former

<!-- b000198 | prose | pages [6] -->
MI match_id game_victor SNO set_victor set_no GNO game_no p1_ace PNO p2_ace point_no P1SE p1_sets p1_winner P2SE p2_winner p2_sets P1GA p1_games winner_shot_type P2GA p2_games p1_double_fault P1SC p1_score p2_double_fault P2SC p2_score p1_unf_err SER p2_unf_err server SERNO serve_no p1_net_pt PV point_victor p2_net_pt P1PW p1_points_won p1_net_pt_won P2PW p2_points_won p2_net_pt_won

<!-- b000199 | prose | pages [6] -->
Glossary Former Glossary

<!-- b000200 | prose | pages [6] -->
GAV P1BP p1_break_pt SEV P2BP p2_break_pt P1ACE P1BPW p1_break_pt_won P2ACE P2BPW p2_break_pt_won P1W P1BPM p1_break_pt_missed P2W P2BPM p2_break_pt_missed WST P1DR p1_distance_run P1DF P2DR p2_distance_run P2DF RC rally_count P1UE SM speed_mph P2UE SW serve_width P1NP SD serve_depth P2NP RD return_depth P1NPW ETS elapsed_time_seconds P2NPW MS momentum swings

<!-- b000201 | heading | pages [6] -->
Establish the Momentum Quantization Model Based on

<!-- b000202 | prose | pages [6] -->
3 Sliding Windows

<!-- b000203 | prose | pages [6] -->
3.1 Quantization of Momentum

<!-- b000204 | prose | pages [6] -->
To assess the current performance and level of excellence of a player during a game, we utilize the concept of a sliding window. This method considers the uncertainty of the game’s progression and calculates the player’s performance over a recent series of rounds.

<!-- b000205 | prose | pages [6] -->
关注数学模型

<!-- b000206 | furniture | pages [6] -->
2

<!-- b000207 | furniture | pages [6] -->
MATHmodels

<!-- b000208 | furniture | pages [6] -->
获取更多资讯

<!-- b000209 | furniture | pages [7] -->
Team # 2409404

<!-- b000210 | furniture | pages [7] -->
Page 7 of 25

<!-- b000211 | prose | pages [7] -->
By doing so, we can obtain a quantiﬁed measure of the player’s momentum at that particu- lar moment. The quantized momentum value for a player at time i (after the moment when the player scored) is deﬁned as:

<!-- b000212 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000213 | prose | pages [7] -->
i

<!-- b000214 | prose | pages [7] -->
[GAi + SCi + (α + 1) SER + PVi + BPWi + ACEi + NPWi + Wi −UEi −DFi]

<!-- b000215 | prose | pages [7] -->
M =

<!-- b000216 | prose | pages [7] -->
∑ i−β+1

<!-- b000217 | prose | pages [7] -->
(1)

<!-- b000218 | prose | pages [7] -->
The variables in question are β, which represents the size of the moving window; α, which represents the percentage of the player’s additional advantage on serve, and GA, which represents the number of games won by the player during the window. SC represents the total number of sets won by the player. PV stands for "winner of the point", indicating the player who successfully wins a point. BPW refers to the number of times the player successfully wins a break point. ACE represents the number of times the player hits an untouchable winning serve. NPW indicates the number of net points gained by the player. W represents the frequency at which a player successfully executed an unbeatable winning

<!-- b000219 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000220 | prose | pages [7] -->
shot, UE represents the frequency at which a player committed an unforced error, and DE represents the frequency at which a player failed to make both serves and hence lost the point.

<!-- b000221 | prose | pages [7] -->
In this quantitative approach, two crucial parameters can be identiﬁed: the magnitude of the sliding window, denoted as β, and the proportion of additional advantage that is discounted due to the player’s serve, represented by α.

<!-- b000222 | prose | pages [7] -->
By utilizing the provided formula, we can calculate the precise numerical value of mo- mentum for each player at any given moment. By comparing the momentum values be- tween the two sides of the game, we can determine which player is performing better at a speciﬁc moment. This allows us to derive the speciﬁc value of their performance.

<!-- b000223 | prose | pages [7] -->
Identiﬁcation of Key Points in the Game 3.2

<!-- b000224 | prose | pages [7] -->
To comprehend the strengths and weaknesses of the aforementioned models in assess- ing player momentum values throughout a match, we will now outline several crucial as- pects of the match. These aspects will also be depicted in the forthcoming visualization of the match ﬂow.

<!-- b000225 | prose | pages [7] -->
Special Circumstances

<!-- b000226 | prose | pages [7] -->
Normal Circumstances

<!-- b000227 | prose | pages [7] -->
Scoring Rules

<!-- b000228 | prose | pages [7] -->
1

<!-- b000229 | prose | pages [7] -->
2

<!-- b000230 | prose | pages [7] -->
3

<!-- b000231 | prose | pages [7] -->
15 points

<!-- b000232 | prose | pages [7] -->
30 points

<!-- b000233 | prose | pages [7] -->
40 points

<!-- b000234 | prose | pages [7] -->
Point

<!-- b000235 | prose | pages [7] -->
AD

<!-- b000236 | prose | pages [7] -->
Advantange

<!-- b000237 | prose | pages [7] -->
Game

<!-- b000238 | prose | pages [7] -->
When the score is 40-40 in a Game

<!-- b000239 | prose | pages [7] -->
AD

<!-- b000240 | prose | pages [7] -->
When the score is 6-6 in a Set

<!-- b000241 | prose | pages [7] -->
1 7

<!-- b000242 | prose | pages [7] -->
……

<!-- b000243 | prose | pages [7] -->
……

<!-- b000244 | prose | pages [7] -->
Tiebreak

<!-- b000245 | prose | pages [7] -->
When the score is 5-5 in a Set

<!-- b000246 | prose | pages [7] -->
best-of-five series

<!-- b000247 | prose | pages [7] -->
best-of-three series

<!-- b000248 | prose | pages [7] -->
Set Set

<!-- b000249 | prose | pages [7] -->
One side wins two more games

<!-- b000250 | caption | pages [7] -->
Figure 2: Rules of Tennis

<!-- b000251 | prose | pages [7] -->
关注数学模型

<!-- b000252 | furniture | pages [7] -->
2

<!-- b000253 | furniture | pages [7] -->
MATHmodels

<!-- b000254 | furniture | pages [7] -->
获取更多资讯

<!-- b000255 | furniture | pages [8] -->
Team # 2409404

<!-- b000256 | furniture | pages [8] -->
Page 8 of 25

<!-- b000257 | prose | pages [8] -->
• Game Point: This crucial point determines the winner of the set between the two play- ers and is ofﬁcially acknowledged in accordance with the established rules of tennis, as depicted in Figure 2. • Tuning Point of Momentum: The Cumulative Sum (CUSUM) technique is employed

<!-- b000258 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000259 | prose | pages [8] -->
at this stage to identify the momentum of the participants. To detect any mutation, the data can be analyzed by calculating the cumulative total to track the cumulative change over time.

<!-- b000260 | prose | pages [8] -->
3.3 Competition Flow Visualization

<!-- b000261 | prose | pages [8] -->
We are choosing the 2023 Wimbledon Men’s Singles Final between Carlos Alcaraz and Novak Djokovic. Associated with the data "2023-Wimbledon-1701" To begin with, we have provided a statistical analysis of the current state of this match, as illustrated in Figure 3.

<!-- b000262 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000263 | prose | pages [8] -->
C. Alcaraz

<!-- b000264 | prose | pages [8] -->
9

<!-- b000265 | prose | pages [8] -->
N. Djokovic

<!-- b000266 | prose | pages [8] -->
ACES

<!-- b000267 | prose | pages [8] -->
7

<!-- b000268 | prose | pages [8] -->
2

<!-- b000269 | prose | pages [8] -->
DOUBLE FAULTS

<!-- b000270 | prose | pages [8] -->
168

<!-- b000271 | prose | pages [8] -->
3

<!-- b000272 | prose | pages [8] -->
166

<!-- b000273 | prose | pages [8] -->
TOTAL POINTS WON

<!-- b000274 | prose | pages [8] -->
UNFORCED ERRORS

<!-- b000275 | prose | pages [8] -->
45

<!-- b000276 | prose | pages [8] -->
6605.5 m

<!-- b000277 | prose | pages [8] -->
40

<!-- b000278 | prose | pages [8] -->
DISTANCE COVERED

<!-- b000279 | prose | pages [8] -->
94/150（63%）

<!-- b000280 | prose | pages [8] -->
6195.2 m

<!-- b000281 | prose | pages [8] -->
118/184（64%）

<!-- b000282 | prose | pages [8] -->
FIRST SERVE % IN

<!-- b000283 | prose | pages [8] -->
66/94（70%） 73/118（62%）

<!-- b000284 | prose | pages [8] -->
WIN % ON 1ST SERVE

<!-- b000285 | prose | pages [8] -->
WIN % ON 2ND SERVE

<!-- b000286 | prose | pages [8] -->
28/56（50%）

<!-- b000287 | prose | pages [8] -->
5/19（26%）

<!-- b000288 | prose | pages [8] -->
37/66（56%）

<!-- b000289 | prose | pages [8] -->
5/15（33%）

<!-- b000290 | prose | pages [8] -->
BREAK POINTS WON

<!-- b000291 | prose | pages [8] -->
NET POINTS WON

<!-- b000292 | prose | pages [8] -->
28/46（61%） 39/65（60%）

<!-- b000293 | prose | pages [8] -->
RECEIVING POINTS WON

<!-- b000294 | prose | pages [8] -->
74/184（40%） 56/150（37%）

<!-- b000295 | caption | pages [8] -->
Figure 3: Technical Statistics

<!-- b000296 | prose | pages [8] -->
Based on the graph, it is evident that Alcaraz’s serve is far superior to Djokovic’s. How- ever, Alcaraz also commits more errors. Both Alcaraz and Djokovic primarily focused on their ﬁrst serves, indicating that it is comparatively simpler to get points with the initial serve. Based on the comprehensive match statistics, Alcaraz demonstrated superior perfor- mance.

<!-- b000297 | prose | pages [8] -->
20

<!-- b000298 | prose | pages [8] -->
10

<!-- b000299 | prose | pages [8] -->
Momentum

<!-- b000300 | prose | pages [8] -->
0

<!-- b000301 | prose | pages [8] -->
10

<!-- b000302 | prose | pages [8] -->
0 2000 4000 6000 8000 10000 Elapsed Time (seconds)

<!-- b000303 | prose | pages [8] -->
1   7 8   6   3   6 Alcaraz Djokovic 6   6 6   1   6 4

<!-- b000304 | prose | pages [8] -->
Carlos Alcaraz's Momentum

<!-- b000305 | prose | pages [8] -->
Novak Djokovic's Momentum

<!-- b000306 | prose | pages [8] -->
Carlos Alcaraz's Game Point

<!-- b000307 | prose | pages [8] -->
Novak Djokovic's Game Point

<!-- b000308 | prose | pages [8] -->
Carlos Alcaraz's Turning Point

<!-- b000309 | prose | pages [8] -->
Novak Djokovic's Turning Point

<!-- b000310 | prose | pages [8] -->
12000 14000 16000

<!-- b000311 | caption | pages [8] -->
Figure 4: Match Flow

<!-- b000312 | prose | pages [8] -->
Now, equation (1) allows for the calculation of the quantitative momentum values of the two players at different moments. The sliding window size, denoted as β, is set to 5. The player’s serve advantage is discounted proportionally by a factor of α = 0.68. The value of α is determined through statistical analysis of the 31 matches provided in the attached table. It

<!-- b000313 | prose | pages [8] -->
关注数学模型

<!-- b000314 | furniture | pages [8] -->
2

<!-- b000315 | furniture | pages [8] -->
MATHmodels

<!-- b000316 | furniture | pages [8] -->
获取更多资讯

<!-- b000317 | furniture | pages [9] -->
Team # 2409404

<!-- b000318 | furniture | pages [9] -->
Page 9 of 25

<!-- b000319 | prose | pages [9] -->
is important to note that α should be determined based on various factors, such as different matches and different players.

<!-- b000320 | prose | pages [9] -->
The quantitative values of momentum for both players at various periods in the match,

<!-- b000321 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000322 | prose | pages [9] -->
including important points, are depicted in Figure 4. Furthermore, to more accurately il- lustrate the level of control a player has at a speciﬁc point, the momentum scatterplot is graphed, as depicted in Figure 5.

<!-- b000323 | prose | pages [9] -->
20

<!-- b000324 | prose | pages [9] -->
15

<!-- b000325 | prose | pages [9] -->
10

<!-- b000326 | prose | pages [9] -->
Momentum

<!-- b000327 | prose | pages [9] -->
5

<!-- b000328 | prose | pages [9] -->
0

<!-- b000329 | prose | pages [9] -->
5

<!-- b000330 | prose | pages [9] -->
10

<!-- b000331 | prose | pages [9] -->
15

<!-- b000332 | prose | pages [9] -->
0 2000 4000 6000 8000 10000 12000

<!-- b000333 | prose | pages [9] -->
10

<!-- b000334 | prose | pages [9] -->
15

<!-- b000335 | prose | pages [9] -->
10

<!-- b000336 | prose | pages [9] -->
5

<!-- b000337 | prose | pages [9] -->
Novak Djokovic

<!-- b000338 | prose | pages [9] -->
Carlos Alcaraz

<!-- b000339 | prose | pages [9] -->
5

<!-- b000340 | prose | pages [9] -->
0

<!-- b000341 | prose | pages [9] -->
0

<!-- b000342 | prose | pages [9] -->
5

<!-- b000343 | prose | pages [9] -->
5

<!-- b000344 | prose | pages [9] -->
10

<!-- b000345 | prose | pages [9] -->
10

<!-- b000346 | prose | pages [9] -->
15

<!-- b000347 | prose | pages [9] -->
14000 16000

<!-- b000348 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000349 | prose | pages [9] -->
Elapsed Time (seconds)

<!-- b000350 | caption | pages [9] -->
Figure 5: Match Flow Scatter

<!-- b000351 | prose | pages [9] -->
By comparing the momentum change curve with the change in the athletes’ score, we ﬁnd that the momentum will increase when the athletes are on a winning streak or serve for points, and when the momentum is well ahead of their opponents, the athletes will be at their best and have a high probability of winning the match.

<!-- b000352 | prose | pages [9] -->
In the ﬁrst set of the match, Djokovic won easily with a score of 6-1. In the ﬁrst game of the ﬁrst set, the two were neck and neck before Djokovic narrowly won the ﬁrst game, at which point their momentum barely changed. After Djokovic won the second set with consecutive points, we observed a signiﬁcant increase in momentum. Alcaraz’s loss of mo- mentum, caused by consecutive losses, led him to lose the next few games to Djokovic, almost all of them by large margins. Especially in the seventh game of the ﬁrst set, when Djokovic got the set point with a score of 5-1, his momentum also increased dramatically, and with this momentum, Djokovic did not allow his opponent to win a single ball in the seventh game.

<!-- b000353 | prose | pages [9] -->
In the second set, the two entered a crucial tie-break. In the tie-break, Alcaraz, who had failed on his ﬁrst serve, still lost the point on his second serve, and Djokovic scored a mini-break, which drastically reduced the momentum of Alcaraz, who had already lost the set, and thus lost two more balls after that. However, at around 6600 s, Alcaraz clawed his way back into the set on serve, and at this point his momentum was extremely elevated and at its peak, while Djokovic was too nervous to face such a crucial point and his momentum was reduced, and Alcaraz eventually won the set. After that, Alcaraz used the momentum of the second set to score consecutive points, and the momentum reached its peak, winning two of the last three sets to ﬁnally win the whole match.

<!-- b000354 | prose | pages [9] -->
Throughout the match, we ﬁnd that Alcaraz’s average momentum was higher than Derkovic’s, which is one of the reasons why Alcaraz got the victory. Also as can be seen by the scatter plot, the distribution of momentum in the sets won by Alcaraz was higher than that of Derkovic.

<!-- b000355 | prose | pages [9] -->
关注数学模型

<!-- b000356 | furniture | pages [9] -->
2

<!-- b000357 | furniture | pages [9] -->
MATHmodels

<!-- b000358 | furniture | pages [9] -->
获取更多资讯

<!-- b000359 | furniture | pages [10] -->
Team # 2409404

<!-- b000360 | furniture | pages [10] -->
Page 10 of 25

<!-- b000361 | prose | pages [10] -->
Momentum’s Impact on the Game Situation 4

<!-- b000362 | prose | pages [10] -->
The Runs Test —Stochastic Analysis 4.1

<!-- b000363 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000364 | prose | pages [10] -->
The runs test is a non-parametric technique used to assess the randomness of a binary sequence consisting of only two distinct values. The run is deﬁned as a consecutive series of parts in a sequence, where each section has the same numeric value as the number "r" of

<!-- b000365 | prose | pages [10] -->
[4]. It is vital to assess the volatility of the

<!-- b000366 | prose | pages [10] -->
the journey. The duration of the run is denoted by l

<!-- b000367 | prose | pages [10] -->
scenario and the randomness of players’ consecutive scores.

<!-- b000368 | prose | pages [10] -->
It is assumed that the binary sequence under analysis is composed of m A’s and n B’s. Prior to conducting the test, two contrasting hypotheses are established: the original hypothesis and the alternative hypothesis.

<!-- b000369 | prose | pages [10] -->
• Original hypothesis H0: The arrangement of A and B is randomized; • Alternative hypothesis H1: The distribution of A and B isn’t random.

<!-- b000370 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000371 | prose | pages [10] -->
If H0 holds, then we have:

<!-- b000372 | prose | pages [10] -->
)

<!-- b000373 | prose | pages [10] -->
) ( n −1

<!-- b000374 | prose | pages [10] -->
( m −1 2

<!-- b000375 | prose | pages [10] -->
P (r = 2k) =

<!-- b000376 | prose | pages [10] -->
k −1

<!-- b000377 | prose | pages [10] -->
k −1

<!-- b000378 | prose | pages [10] -->
( m + n

<!-- b000379 | prose | pages [10] -->
) (2)

<!-- b000380 | prose | pages [10] -->
m

<!-- b000381 | prose | pages [10] -->
) ( n −1

<!-- b000382 | prose | pages [10] -->
( m −1

<!-- b000383 | prose | pages [10] -->
k −1

<!-- b000384 | prose | pages [10] -->
P (r = 2k + 1) =

<!-- b000385 | prose | pages [10] -->
)

<!-- b000386 | prose | pages [10] -->
( m −1

<!-- b000387 | prose | pages [10] -->
) ( n −1

<!-- b000388 | prose | pages [10] -->
)

<!-- b000389 | prose | pages [10] -->
+

<!-- b000390 | prose | pages [10] -->
k −1

<!-- b000391 | prose | pages [10] -->
k

<!-- b000392 | prose | pages [10] -->
k

<!-- b000393 | prose | pages [10] -->
)

<!-- b000394 | prose | pages [10] -->
( m + n

<!-- b000395 | prose | pages [10] -->
(3)

<!-- b000396 | prose | pages [10] -->
m

<!-- b000397 | prose | pages [10] -->
Given that we have chosen 31 games, both m and n represent large samples. Conse- quently, the number of the runs, denoted as r, may be considered to follow an almost nor- mal distribution. As a result, we can calculate the mathematical expectation and variance of r:

<!-- b000398 | prose | pages [10] -->
E (r) = 2mn

<!-- b000399 | prose | pages [10] -->
m + n + 1 (4)

<!-- b000400 | prose | pages [10] -->
V (r) = 2mn (2mn −m −n)

<!-- b000401 | prose | pages [10] -->
(5)

<!-- b000402 | prose | pages [10] -->
(m + n)2 (m + n −1)

<!-- b000403 | prose | pages [10] -->
The statistic is then derived from the count of the run.

<!-- b000404 | prose | pages [10] -->
Z = r −E (r) √ √

<!-- b000405 | prose | pages [10] -->
(6)

<!-- b000406 | prose | pages [10] -->
V (r)

<!-- b000407 | prose | pages [10] -->
To account for the variability of the circumstance, we utilize the Point Victor factor. In order to assess the ongoing performance of the participants, we initially employ the Point Victor factor, followed by the establishment of two indicators to measure continuous values. Subsequently, we evaluate the aforementioned sequence. Consequently, the outcomes can

<!-- b000408 | prose | pages [10] -->
关注数学模型

<!-- b000409 | furniture | pages [10] -->
2

<!-- b000410 | furniture | pages [10] -->
MATHmodels

<!-- b000411 | furniture | pages [10] -->
获取更多资讯

<!-- b000412 | furniture | pages [11] -->
Team # 2409404

<!-- b000413 | prose | pages [11] -->
be acquired as demonstrated in Table 4.

<!-- b000414 | furniture | pages [11] -->
Page 11 of 25

<!-- b000415 | caption | pages [11] -->
Table 4: The Results of the Runs Test

<!-- b000416 | prose | pages [11] -->
Testing Program Z p

<!-- b000417 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000418 | prose | pages [11] -->
Point Victor Player 1 Consecutive Win Player 2 Consecutive Win -5.613 0.00000001986<0.01 -30.606 0.000<0.01 -29.866 0.000<0.01

<!-- b000419 | prose | pages [11] -->
Upon examining the table, it becomes evident that Z-scores are less than zero for all three indicators. This is attributed to the fact that the observations are located to the left of the mean. Given a signiﬁcance level of 0.01 and p < 0.01, we can be 99 % certain that the alternative hypothesis, H0 will be rejected. This suggests that the ﬂuctuations in the situation and the consecutive scoring situations of the players are not random, indicating the presence of a driving factor.

<!-- b000420 | prose | pages [11] -->
The Chi-square Test —Correlation Analysis 4.2

<!-- b000421 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000422 | prose | pages [11] -->
To assess the variation of the scenario and the continual scoring of players in relation to Momentum, we employ the chi-square independence test. In contrast to Problem 1, when Momentum was quantiﬁed as a continuous variable, the chi-square test requires it to be a discrete categorical variable. First, we begin by discretizing the concept of momentum. Cur- rently, we possess the initial momentum values of Player 1 and Player 2, denoted as Mp1i and Mp2i, correspondingly, which are related by the following transformation equation:

<!-- b000423 | prose | pages [11] -->


<!-- b000424 | prose | pages [11] -->
{ 1, MP1i > MP2i

<!-- b000425 | prose | pages [11] -->
 

<!-- b000426 | prose | pages [11] -->
′

<!-- b000427 | prose | pages [11] -->


<!-- b000428 | prose | pages [11] -->
1i =

<!-- b000429 | prose | pages [11] -->
MP

<!-- b000430 | prose | pages [11] -->


<!-- b000431 | prose | pages [11] -->
0, MP1i < MP2i

<!-- b000432 | prose | pages [11] -->
{ 1, MP1i < MP2i

<!-- b000433 | prose | pages [11] -->
 

<!-- b000434 | prose | pages [11] -->
′

<!-- b000435 | prose | pages [11] -->


<!-- b000436 | prose | pages [11] -->
2i =

<!-- b000437 | prose | pages [11] -->
MP

<!-- b000438 | prose | pages [11] -->


<!-- b000439 | prose | pages [11] -->
(7)

<!-- b000440 | prose | pages [11] -->
0, MP1i > MP2i

<!-- b000441 | prose | pages [11] -->
Following the aforementioned equation, we get the categorical variables and next em- ploy the chi-square test. Here, it is imperative to assume that momentum is independent of ﬂuctuations in the game circumstances and the consecutive triumphs of a player. The calculated value representing the test statistic is:

<!-- b000442 | prose | pages [11] -->
R

<!-- b000443 | prose | pages [11] -->
C

<!-- b000444 | prose | pages [11] -->
χ2 =

<!-- b000445 | prose | pages [11] -->
∑

<!-- b000446 | prose | pages [11] -->
∑

<!-- b000447 | prose | pages [11] -->
j=1

<!-- b000448 | prose | pages [11] -->
k=1

<!-- b000449 | prose | pages [11] -->
( (

<!-- b000450 | prose | pages [11] -->
)2

<!-- b000451 | prose | pages [11] -->
njk −n ˆpjk

<!-- b000452 | prose | pages [11] -->
(8)

<!-- b000453 | prose | pages [11] -->
n ˆpjk

<!-- b000454 | prose | pages [11] -->
where R and C are the sizes of the R × C list of columns, and n ˆpjk is the maximum likelihood estimate obtained when H0 holds, i.e:

<!-- b000455 | prose | pages [11] -->
ˆpjk = ˆpj· ˆp·k = nj·

<!-- b000456 | prose | pages [11] -->
n · n·k

<!-- b000457 | prose | pages [11] -->
(9) n

<!-- b000458 | prose | pages [11] -->
For a given signiﬁcance level γ, the rejection domain of the test is

<!-- b000459 | prose | pages [11] -->
{

<!-- b000460 | prose | pages [11] -->
χ2 ≥χ2

<!-- b000461 | prose | pages [11] -->
} 1−γ ((R −1) (C −1))

<!-- b000462 | prose | pages [11] -->
W =

<!-- b000463 | prose | pages [11] -->
.

<!-- b000464 | prose | pages [11] -->
(10)

<!-- b000465 | prose | pages [11] -->
关注数学模型

<!-- b000466 | furniture | pages [11] -->
2

<!-- b000467 | furniture | pages [11] -->
MATHmodels

<!-- b000468 | furniture | pages [11] -->
获取更多资讯

<!-- b000469 | furniture | pages [12] -->
Team # 2409404

<!-- b000470 | furniture | pages [12] -->
Page 12 of 25

<!-- b000471 | prose | pages [12] -->
Following the aforementioned procedure, the outcomes of the chi-square test can be obtained and are presented in Table 5.

<!-- b000472 | caption | pages [12] -->
Table 5: The Results of the Chi-square Test

<!-- b000473 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000474 | prose | pages [12] -->
p1W

<!-- b000475 | prose | pages [12] -->
χ2

<!-- b000476 | prose | pages [12] -->
TestingProgram Category

<!-- b000477 | prose | pages [12] -->
SUM p

<!-- b000478 | prose | pages [12] -->
0 1

<!-- b000479 | prose | pages [12] -->
0 1936 1483 3419

<!-- b000480 | prose | pages [12] -->
p1N

<!-- b000481 | prose | pages [12] -->
1 1630 2235 3865

<!-- b000482 | prose | pages [12] -->
9.167 × 10−32 151.617

<!-- b000483 | prose | pages [12] -->
SUM 3566 3718 7284

<!-- b000484 | prose | pages [12] -->
p2W

<!-- b000485 | prose | pages [12] -->
χ2

<!-- b000486 | prose | pages [12] -->
TestingProgram Category

<!-- b000487 | prose | pages [12] -->
SUM p

<!-- b000488 | prose | pages [12] -->
0 1

<!-- b000489 | prose | pages [12] -->
0 2266 1663 3929

<!-- b000490 | prose | pages [12] -->
p2N

<!-- b000491 | prose | pages [12] -->
1 1452 1903 3355

<!-- b000492 | prose | pages [12] -->
1.962 × 10−31 150.065

<!-- b000493 | prose | pages [12] -->
SUM 3718 3566 7284

<!-- b000494 | prose | pages [12] -->
p2W

<!-- b000495 | prose | pages [12] -->
χ2

<!-- b000496 | prose | pages [12] -->
TestingProgram Category

<!-- b000497 | prose | pages [12] -->
SUM p

<!-- b000498 | prose | pages [12] -->
0 1

<!-- b000499 | prose | pages [12] -->
0 1483 1936 3419

<!-- b000500 | prose | pages [12] -->
p1N

<!-- b000501 | prose | pages [12] -->
1 2235 1630 3865

<!-- b000502 | prose | pages [12] -->
9.167 × 10−32 151.617

<!-- b000503 | prose | pages [12] -->
SUM 3718 3566 7284

<!-- b000504 | prose | pages [12] -->
p1W

<!-- b000505 | prose | pages [12] -->
χ2

<!-- b000506 | prose | pages [12] -->
TestingProgram Category

<!-- b000507 | prose | pages [12] -->
SUM p

<!-- b000508 | prose | pages [12] -->
0 1

<!-- b000509 | prose | pages [12] -->
0 1663 2266 3929

<!-- b000510 | prose | pages [12] -->
p2N

<!-- b000511 | prose | pages [12] -->
1 1903 1452 3355

<!-- b000512 | prose | pages [12] -->
1.962 × 10−31 150.065

<!-- b000513 | prose | pages [12] -->
p1 Game Point

<!-- b000514 | prose | pages [12] -->
χ2

<!-- b000515 | prose | pages [12] -->
TestingProgram Category

<!-- b000516 | prose | pages [12] -->
SUM p 0 1

<!-- b000517 | prose | pages [12] -->
0 3048 371 3419

<!-- b000518 | prose | pages [12] -->
p1N

<!-- b000519 | prose | pages [12] -->
1 3230 635 3865 1.243 × 10−9 47.256 SUM 6278 1006 7284

<!-- b000520 | prose | pages [12] -->
p2 Game Point

<!-- b000521 | prose | pages [12] -->
χ2

<!-- b000522 | prose | pages [12] -->
TestingProgram Category

<!-- b000523 | prose | pages [12] -->
SUM p 0 1

<!-- b000524 | prose | pages [12] -->
0 3534 395 3929

<!-- b000525 | prose | pages [12] -->
p2N

<!-- b000526 | prose | pages [12] -->
1 2843 512 3355 3.948 × 10−9 45.015 SUM 6377 907 7284

<!-- b000527 | prose | pages [12] -->
p2 Game Point

<!-- b000528 | prose | pages [12] -->
χ2

<!-- b000529 | prose | pages [12] -->
TestingProgram Category

<!-- b000530 | prose | pages [12] -->
SUM p 0 1

<!-- b000531 | prose | pages [12] -->
0 2901 518 3419

<!-- b000532 | prose | pages [12] -->
p1N

<!-- b000533 | prose | pages [12] -->
1 3476 389 3865 1.012 × 10−8 43.047 SUM 6377 907 7284

<!-- b000534 | prose | pages [12] -->
p1 Game Point

<!-- b000535 | prose | pages [12] -->
χ2

<!-- b000536 | prose | pages [12] -->
TestingProgram Category

<!-- b000537 | prose | pages [12] -->
SUM p 0 1

<!-- b000538 | prose | pages [12] -->
0 3287 642 3929

<!-- b000539 | prose | pages [12] -->
p2N

<!-- b000540 | prose | pages [12] -->
1 2991 364 3355 2.671 × 10−9 45.831

<!-- b000541 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000542 | prose | pages [12] -->
SUM 3566 3718 7284 SUM 6278 1006 7284

<!-- b000543 | prose | pages [12] -->
Upon examining the table, it becomes apparent that the χ2 for each test is greater, as- suming a signiﬁcant level of 0.01 and p < 0.01. This implies a 99 % level of conﬁdence in rejecting the original hypothesis H0, indicating a correlation between the volatility of the situation and the consecutive scoring situation of the players with Momentum.

<!-- b000544 | prose | pages [12] -->
4.3 Reach a Verdict

<!-- b000545 | prose | pages [12] -->
Based on the results of the Runs Test examining the unpredictability of circumstance ﬂuctuations and players’ successive scores, as well as a chi-square test assessing the rele- vance of Momentum, there is ample evidence to support the notion that Momentum plays a vital role in the outcome of a tennis match. The variability of the circumstance and the successive scores of the participants exhibit a non-random pattern, suggesting the presence of a driving element, most likely attributable to momentum.

<!-- b000546 | heading | pages [12] -->
Establish the Prediction for Match Trend Model Based on

<!-- b000547 | prose | pages [12] -->
5 PCA&XGBoost

<!-- b000548 | heading | pages [12] -->
Principal Component Analysis —Determine the Model

<!-- b000549 | prose | pages [12] -->
5.1

<!-- b000550 | prose | pages [12] -->
Based on our previous discussion, we have sufﬁcient evidence to suggest that the unpredictable ﬂuctuation in the game is connected to the momentum of the two players. Therefore, we will use momentum as the focus of our forecast. Nevertheless, in the quan- titative model of momentum, which provides continuous data on the momentum of both players at every moment, we contend that the ﬂuctuating pattern in the match can be inter- preted as a transfer of momentum. Speciﬁcally, if player 1’s momentum surpasses that of player 2, the momentum is deemed to have shifted to player 1, and vice versa for player 2.

<!-- b000551 | prose | pages [12] -->
关注数学模型

<!-- b000552 | furniture | pages [12] -->
2

<!-- b000553 | furniture | pages [12] -->
MATHmodels

<!-- b000554 | furniture | pages [12] -->
获取更多资讯

<!-- b000555 | furniture | pages [13] -->
Team # 2409404

<!-- b000556 | furniture | pages [13] -->
Page 13 of 25

<!-- b000557 | prose | pages [13] -->
The equation (7) can be used to express this technique. Let’s say that we are player 1. In this case, "1" indicates that momentum is in our favor, whereas "2" indicates that momentum is in the opposing side’s favor. By employing this discretization technique, we can obtain a crude depiction of the game’s ﬂuctuation pattern. Thus, we can consider it the dependent

<!-- b000558 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000559 | prose | pages [13] -->
variable in our forecast, referred to as MS, while the autonomous variables can be the ones listed in Table 3. Excluding MI and MS, we have chosen 43 criteria to include in the table.

<!-- b000560 | prose | pages [13] -->
To enhance model selection, we initially considered the ﬁrst 30 matches, excluding the Carlos Alcaraz VS. Novak Djokovic game.1 This analysis reduces the previously mentioned 43 elements to two dimensions. We next create a scatter plot with two scales based on this analysis, as depicted in Figure 6.

<!-- b000561 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000562 | caption | pages [13] -->
Figure 6: PCA Biplot

<!-- b000563 | prose | pages [13] -->
Upon analyzing the graph, it becomes evident that:

<!-- b000564 | prose | pages [13] -->
• Fluctuations in the match situation are challenging to classify on the two-dimensional principal components. The majority of factors do not have a signiﬁcant impact on PC1, but they have a greater inﬂuence on PC2. These factors include GNO, GA, DR, and RC. • Several parameters, including SNO, PNO, SE, PW, and ETS, have a greater impact on PC1 and a lesser one on PC2. • Only a small number of variables have a substantial impact on both PC1 and PC2. • PC2 may encounter challenges in accurately characterizing variations and establishing a more precise basis for classifying the outcomes. • The distribution of scenario ﬂuctuations has a distinct clustering pattern on PC1. • Data cannot be divided in a linear manner. • The clustering of the factor bisector plots is likely a result of the interconnection be- tween the factors, as supported by earlier investigations.

<!-- b000565 | prose | pages [13] -->
Based on the above analysis, we believe that simple classiﬁcation models make it dif- ﬁcult to predict the ﬂuctuation of the game situation more accurately, so we consider the eXtreme Gradient Boosting (XGBoost) optimization model based on the tree model.

<!-- b000566 | prose | pages [13] -->
XGBoost —Match Trend Prediction 5.2

<!-- b000567 | prose | pages [13] -->
In the previous analysis, we determined the inputs to the model as 43 factor indicators for the two players. These indicators serve as independent variables. The outputs of the model, on the other hand, are the ﬂuctuations in the match situation. We assume a value

<!-- b000568 | prose | pages [13] -->
1This is because we must make a prediction for the entire game to avoid any data leaks.

<!-- b000569 | prose | pages [13] -->
关注数学模型

<!-- b000570 | furniture | pages [13] -->
2

<!-- b000571 | furniture | pages [13] -->
MATHmodels

<!-- b000572 | furniture | pages [13] -->
获取更多资讯

<!-- b000573 | furniture | pages [14] -->
Team # 2409404

<!-- b000574 | furniture | pages [14] -->
Page 14 of 25

<!-- b000575 | prose | pages [14] -->
of 1 for the own side and 0 for the other side, making it the dependent variable. Conse- quently, the problem can be succinctly described as a categorical prediction. The model was constructed using data from the initial 30 matches, and knowledge was acquired from these matches. The last match, "2023-wimbledon-1701", was then used as the basis for sub-

<!-- b000576 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000577 | prose | pages [14] -->
sequent model evaluations. This approach can optimize the efﬁcient utilization of the avail- able dataset and, to some extent, enhance the effectiveness of the model. It is important to mention that while analyzing 30 games, we must individually compute the momentum of each player in each game. Then, we discretize it depending on the magnitude of the two in order to successfully prevent miscalculations caused by variations in the sliding window span across various games. The dependent variable can be explained as a dichotomous vari- able that changes from 1 to 0 or from 0 to 1 in two consecutive moments. This represents a change in the game’s circumstances at that time.

<!-- b000578 | prose | pages [14] -->
5.3 Factor Importance Extraction

<!-- b000579 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000580 | prose | pages [14] -->
The XGBoost model learns from 30 matches, and we can calculate the extent to which each factor contributes to learning, denoted pη(η = 1, 2, · · · , 43). In order to identify the critical factors that signiﬁcantly impact the ﬂuctuations in the matches, we calculate the importance score FIη for each factor. We then normalize the pi values and calculate the percent score. The formula is as follows:

<!-- b000581 | prose | pages [14] -->
FIη = 100 × pη (11) max (FI)

<!-- b000582 | prose | pages [14] -->
Based on the aforementioned computations, we will present the relevance scores of each factor, as depicted in Figure 7.

<!-- b000583 | prose | pages [14] -->
100

<!-- b000584 | prose | pages [14] -->
90

<!-- b000585 | prose | pages [14] -->
80

<!-- b000586 | prose | pages [14] -->
Importance of normalization

<!-- b000587 | prose | pages [14] -->
70

<!-- b000588 | prose | pages [14] -->
60

<!-- b000589 | prose | pages [14] -->
50

<!-- b000590 | prose | pages [14] -->
40

<!-- b000591 | prose | pages [14] -->
30

<!-- b000592 | prose | pages [14] -->
20

<!-- b000593 | prose | pages [14] -->
10

<!-- b000594 | prose | pages [14] -->
0

<!-- b000595 | prose | pages [14] -->
PV

<!-- b000596 | prose | pages [14] -->
SER

<!-- b000597 | prose | pages [14] -->
PNO

<!-- b000598 | prose | pages [14] -->
SNO

<!-- b000599 | prose | pages [14] -->
ETS

<!-- b000600 | prose | pages [14] -->
P1SE

<!-- b000601 | prose | pages [14] -->
P2SE

<!-- b000602 | prose | pages [14] -->
GNO

<!-- b000603 | prose | pages [14] -->
P2SC

<!-- b000604 | prose | pages [14] -->
P1SC

<!-- b000605 | prose | pages [14] -->
P2DF

<!-- b000606 | prose | pages [14] -->
P1UE

<!-- b000607 | prose | pages [14] -->
P2BP

<!-- b000608 | prose | pages [14] -->
P1BP

<!-- b000609 | prose | pages [14] -->
P2PW

<!-- b000610 | prose | pages [14] -->
P1PW

<!-- b000611 | prose | pages [14] -->
P2GA

<!-- b000612 | prose | pages [14] -->
P1GA

<!-- b000613 | prose | pages [14] -->
P2BPM

<!-- b000614 | prose | pages [14] -->
P1BPW

<!-- b000615 | prose | pages [14] -->
P2BPW

<!-- b000616 | prose | pages [14] -->
SM

<!-- b000617 | prose | pages [14] -->
SD

<!-- b000618 | prose | pages [14] -->
SW

<!-- b000619 | prose | pages [14] -->
RC

<!-- b000620 | prose | pages [14] -->
RD

<!-- b000621 | prose | pages [14] -->
SEV

<!-- b000622 | prose | pages [14] -->
P1W

<!-- b000623 | prose | pages [14] -->
P2W

<!-- b000624 | prose | pages [14] -->
WST

<!-- b000625 | prose | pages [14] -->
GAV

<!-- b000626 | prose | pages [14] -->
P1DF

<!-- b000627 | prose | pages [14] -->
P2UE

<!-- b000628 | prose | pages [14] -->
P2DR

<!-- b000629 | prose | pages [14] -->
P1DR

<!-- b000630 | prose | pages [14] -->
P2NP

<!-- b000631 | prose | pages [14] -->
P1NP

<!-- b000632 | prose | pages [14] -->
P1ACE

<!-- b000633 | prose | pages [14] -->
P2ACE

<!-- b000634 | prose | pages [14] -->
P1BPM

<!-- b000635 | prose | pages [14] -->
SERNO

<!-- b000636 | prose | pages [14] -->
P2NPW

<!-- b000637 | prose | pages [14] -->
P1NPW

<!-- b000638 | prose | pages [14] -->
Indicator abbreviations

<!-- b000639 | caption | pages [14] -->
Figure 7: Factor Importance

<!-- b000640 | prose | pages [14] -->
Out of the total of 43 indicators, 28 of them fall into the same category in pairs. For example, both P1BP and P2BP are considered break points. Therefore, we calculate the average importance scores for these indicators and provide them in Table 6.

<!-- b000641 | prose | pages [14] -->
By integrating the aforementioned graphic and table, it becomes evident that both BP (break point) and PV (point victor) signiﬁcantly contribute to accurately forecasting the

<!-- b000642 | prose | pages [14] -->
关注数学模型

<!-- b000643 | furniture | pages [14] -->
2

<!-- b000644 | furniture | pages [14] -->
MATHmodels

<!-- b000645 | furniture | pages [14] -->
获取更多资讯

<!-- b000646 | furniture | pages [15] -->
Team # 2409404

<!-- b000647 | furniture | pages [15] -->
Page 15 of 25

<!-- b000648 | caption | pages [15] -->
Table 6: Importance of Factors after Organizing

<!-- b000649 | prose | pages [15] -->
Factor Importance

<!-- b000650 | prose | pages [15] -->
Factor

<!-- b000651 | prose | pages [15] -->
PV 74.923 SER BP 30.771 ETS GA 24.406 Importance P1 P2 AVERAGE 93.395 100.000 96.698 36.801 39.985 38.393

<!-- b000652 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000653 | prose | pages [15] -->
GNO SE 21.387 SNO BPW 19.668 PNO PW 19.570 GAV DF 18.524 SM SC 14.060 RC BPM 13.912 SW UE 13.534 RD ACE 12.679 SERNO NPW 12.000 SD NP 11.825 WST DR 11.325 SEV W 6.477 40.959 19.217 30.088 30.662 19.786 25.224 23.023 23.248 23.136 14.406 26.983 20.695 18.942 19.936 19.439 13.880 20.603 17.241 19.353 10.249 14.801 17.899 11.626 14.762 12.677 15.764 14.221 12.898 14.590 13.744 13.375 12.489 12.932 12.993 12.734 12.864

<!-- b000654 | prose | pages [15] -->
game’s trajectory. While the aforementioned two criteria may be more signiﬁcant, the in- trinsic impact of other aspects should not be disregarded. Factors such as ACE, DF, DR,

<!-- b000655 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000656 | prose | pages [15] -->
SERNO, and others will also inﬂuence the game’s ﬂuctuations to a certain degree. Ulti- mately, we furnish tennis coaches with insights into the signiﬁcance of momentum and offer guidance on how players can sustain and control momentum throughout a match.

<!-- b000657 | prose | pages [15] -->
Tactical Suggestions for the Game 5.4

<!-- b000658 | prose | pages [15] -->
Based on the above analysis, while analyzing the differential in past match "momen- tum" swings, give the player some constructive suggestions.

<!-- b000659 | prose | pages [15] -->
• Reasonable distribution of physical ﬁtness. In the early stage of the game, we will try to attack, understand each other’s physical strength, tactics, etc., and retain our own physical strength; in the middle of the game, we will make reasonable use of "mo- mentum," adopt an aggressive or conservative playing style according to the current situation of the game, and appropriately consume the opponent’s physical strength; and the coaches and the players should pay attention to the changes in their physical state at this time, such as the existence of movement. Coaches and players should pay attention to the changes in physical condition, such as whether there is any movement stiffness, and take technical pause and other measures in time to ensure that the play- ers have a better momentum level. In the late stage of the game, the players synthesize the experience gained from the pre-momentum and mid-momentum to play the game and make appropriate adjustments to combine with their own physical condition. • Focus on the mental state during the match. Mental state also has a certain degree of inﬂuence on "momentum." If the player focuses too much on the score, especially in the key game or the key points in the game, his momentum may be greatly reduced because of the opponent’s scores. The player should discuss their own situation in the game with a psychological expert. Psychological experts should provide timely communication with the coaches, technical time-outs, and other measures to restore the player’s "momentum" Coaches should communicate with the players and take measures such as a technical pause to restore the players’ momentum. Players should also pay attention to the change in their own mentality during the game and adjust it

<!-- b000660 | prose | pages [15] -->
关注数学模型

<!-- b000661 | furniture | pages [15] -->
2

<!-- b000662 | furniture | pages [15] -->
MATHmodels

<!-- b000663 | furniture | pages [15] -->
获取更多资讯

<!-- b000664 | furniture | pages [16] -->
Team # 2409404

<!-- b000665 | furniture | pages [16] -->
Page 16 of 25

<!-- b000666 | prose | pages [16] -->
by appropriately slowing down the rhythm of offense. • Modify your style of play to counter the opponent’s momentum，in other words，you are never in danger if you know yourself and your rival. To lessen the opponent’s momentum in the game and boost your own momentum in this situation, familiarize

<!-- b000667 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000668 | prose | pages [16] -->
yourself with the opposing players and the situations in which their momentum will increase or decrease prior to the game. Increase the growth of the game’s direction and make appropriate modiﬁcations if you discover that the circumstances on the ﬁeld are favoring the opponent’s momentum. Concurrently, consider how you can lessen the opponent’s momentum. Aim for as many points as you can on crucial shots that slow down the opposition’s momentum. • Utilize the two serves to your advantage. Even in the event of failure, there is always a second chance; in the event of a ﬁrst serve error, the second serve will go to the conservative main. In the ﬁrst serve, the ball’s speed and power present the biggest challenge to the high difﬁculty and high skills of the ace ball. When the other player serves for the ﬁrst time, prepare to hit the ball hard and quickly. Since your opponent’s

<!-- b000669 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000670 | prose | pages [16] -->
power and speed are reduced when he serves again, it is simpler to score if you launch a swift counterattack at this point. • Focus on key points in the game. When a match reaches game point, set point, or a battle of seven, often a single point gained or lost can affect a dramatic shift in mo- mentum, which can change the course of the match.

<!-- b000671 | prose | pages [16] -->
6

<!-- b000672 | heading | pages [16] -->
Model Effect Analysis

<!-- b000673 | prose | pages [16] -->
6.1

<!-- b000674 | heading | pages [16] -->
Model Testing on a New Race

<!-- b000675 | prose | pages [16] -->
To evaluate the efﬁcacy of the established model in forecasting game volatility, we con- ducted a test using "2023-wimbledon-1701" as the subject of analysis. The subsequent cri- teria were taken into account:accuracy,Confuse Matrix Thermal Charts, the classiﬁcation report and Receiver Operating Characteristic the Curve.

<!-- b000676 | prose | pages [16] -->
• Accuracy: Accuracy refers to the proportion of accurate predictions in relation to the entire sample, i.e:

<!-- b000677 | prose | pages [16] -->
Acc = NTruePredict

<!-- b000678 | prose | pages [16] -->
× 100 % (12)

<!-- b000679 | prose | pages [16] -->
NSample

<!-- b000680 | prose | pages [16] -->
Tests have shown that NTruePredict = 231, NSample = 334, therefore, Acc = 69.16 %. • Confusion Matrix: The heat map displays the confusion matrix, where each row rep- resents the true category of the sample label, namely the actual value of the circum- stance ﬂuctuation. Each column represents the predicted category of the sample label, speciﬁcally the predicted value of the model. Hence, the total of the primary diago- nal elements in the matrix corresponds to the count of successfully predicted samples by the model. Furthermore, it is necessary to include four variables, namely TP, FN, FP, and TN, where T represents True and F represents False, indicating whether the predicted value matches the actual value; P represents Positive and N represents Neg- ative, showing whether the prediction falls into the positive or negative category. As

<!-- b000681 | prose | pages [16] -->
关注数学模型

<!-- b000682 | furniture | pages [16] -->
2

<!-- b000683 | furniture | pages [16] -->
MATHmodels

<!-- b000684 | furniture | pages [16] -->
获取更多资讯

<!-- b000685 | furniture | pages [17] -->
Team # 2409404

<!-- b000686 | furniture | pages [17] -->
Page 17 of 25

<!-- b000687 | prose | pages [17] -->
depicted in Figure 8, it is evident to see the prediction accuracy and error, as well as the level of distinction of the model for each group.

<!-- b000688 | prose | pages [17] -->
TN FP

<!-- b000689 | prose | pages [17] -->
1.0

<!-- b000690 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000691 | prose | pages [17] -->
100

<!-- b000692 | prose | pages [17] -->
117 37

<!-- b000693 | prose | pages [17] -->
0

<!-- b000694 | prose | pages [17] -->
Actual

<!-- b000695 | prose | pages [17] -->
80

<!-- b000696 | prose | pages [17] -->
FN TP

<!-- b000697 | prose | pages [17] -->
60

<!-- b000698 | prose | pages [17] -->
66 114

<!-- b000699 | prose | pages [17] -->
1

<!-- b000700 | prose | pages [17] -->
40

<!-- b000701 | prose | pages [17] -->
0 1 Predicted

<!-- b000702 | caption | pages [17] -->
Figure 8: Confusion Matrix

<!-- b000703 | prose | pages [17] -->
0.8

<!-- b000704 | prose | pages [17] -->
0.755 0.633 0.689

<!-- b000705 | prose | pages [17] -->
1

<!-- b000706 | prose | pages [17] -->
0.6

<!-- b000707 | prose | pages [17] -->
0.4

<!-- b000708 | prose | pages [17] -->
0.639 0.760 0.694

<!-- b000709 | prose | pages [17] -->
0

<!-- b000710 | prose | pages [17] -->
0.2

<!-- b000711 | prose | pages [17] -->
0.0

<!-- b000712 | prose | pages [17] -->
f1

<!-- b000713 | prose | pages [17] -->
recall

<!-- b000714 | prose | pages [17] -->
precision

<!-- b000715 | caption | pages [17] -->
Figure 9: Classiﬁcation Report

<!-- b000716 | prose | pages [17] -->
Observing the graph, we can see that the model is superior for predicting the ﬂuctua- tions of the game, with the main diagonal elements making up the majority, but there

<!-- b000717 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000718 | prose | pages [17] -->
are some limitations, perhaps in the difﬁculty of identifying changes at key points. • Classiﬁcation Rport: The classiﬁcation report computes the Precision, Recall, and F1 −score for each category in the model. In the visualization graph, deeper colors imply higher values, which correspond to better results, as depicted in Figure 9. Three examples of metrics calculation are given below:

<!-- b000719 | prose | pages [17] -->
– Precision is the percentage of correctness for all predictions in the positive cate-

<!-- b000720 | prose | pages [17] -->
gory.

<!-- b000721 | prose | pages [17] -->
TP 114 TP + FP = Precision1 = 114 + 37 = 0.755 (13)

<!-- b000722 | prose | pages [17] -->
– Recall refers to the ratio of correctly identiﬁed positive categories out of all the

<!-- b000723 | prose | pages [17] -->
actual positive categories.

<!-- b000724 | prose | pages [17] -->
Recall1 = TP 114 TP + FN = 114 + 66 = 0.633 (14)

<!-- b000725 | prose | pages [17] -->
– F1-score is calculated as the harmonic mean of Precision and Recall.

<!-- b000726 | prose | pages [17] -->
F11 = 2 × Precision × Recall

<!-- b000727 | prose | pages [17] -->
= 2 × 0.755 × 0.633

<!-- b000728 | prose | pages [17] -->
= 0.689 (15)

<!-- b000729 | prose | pages [17] -->
Precision + Recall

<!-- b000730 | prose | pages [17] -->
0.755 + 0.633

<!-- b000731 | prose | pages [17] -->
In binary class classiﬁcation, it is desirable to have a balanced distribution of positive and negative class samples. Additionally, a higher F1-score indicates better perfor- mance in both Precision and Recall of the model. • Receiver Operating Characteristic (ROC) Curve: The ROC curverepresents the rela- tionship between the sensitivity and speciﬁcity of the model. It shows the false posi- tive rate (FPR) for each category on the horizontal axis and the true positive rate (TPR) on the vertical axis. Hence, the optimal point of this curve is situated in the top left corner, namely when the false positive rate (FPR) equals zero and the true positive rate (TPR) equals one. This indicates a more favorable impact of magic. Furthermore, another crucial statistic that may be derived is the area under the curve (AUC), which indicates the effectiveness of the model. A bigger AUC value signiﬁes a more effec- tive model. Prior to plotting this image, it is imperative that we grasp the underlying

<!-- b000732 | prose | pages [17] -->
关注数学模型

<!-- b000733 | furniture | pages [17] -->
2

<!-- b000734 | furniture | pages [17] -->
MATHmodels

<!-- b000735 | furniture | pages [17] -->
获取更多资讯

<!-- b000736 | furniture | pages [18] -->
Team # 2409404

<!-- b000737 | prose | pages [18] -->
measures.

<!-- b000738 | furniture | pages [18] -->
Page 18 of 25

<!-- b000739 | prose | pages [18] -->
– Sensitivity: The deﬁnition of sensitivity, also known as the True-Positive rate, is

<!-- b000740 | prose | pages [18] -->
follows:

<!-- b000741 | prose | pages [18] -->
TP

<!-- b000742 | heading | pages [18] -->
Sensitivity = TPR =

<!-- b000743 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000744 | prose | pages [18] -->
(16) TP + FN

<!-- b000745 | prose | pages [18] -->
– Speciﬁcity: The True-Negative rate, is also known as speciﬁcity and is deﬁned

<!-- b000746 | prose | pages [18] -->
as:

<!-- b000747 | prose | pages [18] -->
TN Speciﬁcity = TNR = (17) TN + FP

<!-- b000748 | prose | pages [18] -->
– 1−Speciﬁcity: It is referred to as the False-Positive rate, deﬁned as:

<!-- b000749 | prose | pages [18] -->
FP FPR = 1 −Speciﬁcity = (18) FP + TN

<!-- b000750 | heading | pages [18] -->
– 1−Sensitivity: It is called False-Negative rate, deﬁned as:

<!-- b000751 | prose | pages [18] -->
FN

<!-- b000752 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000753 | heading | pages [18] -->
FNR = 1 −Sensitivity =

<!-- b000754 | prose | pages [18] -->
(19) FN + TP

<!-- b000755 | prose | pages [18] -->
To illustrate this model, we graph its ROC curve, depicted in Figure x. Upon exam- ining the graph, it is evident that the curve exhibits a tendency towards approaching the point (0, 1) more closely. Additionally, the AUC (Area Under the Curve) for the two categories is calculated to be 0.75. Furthermore, we have also computed the AUC for both micro-average and macro-average, both of which yield a value of 0.75. This indicates that the performance of the established model is relatively satisfactory.

<!-- b000756 | prose | pages [18] -->
1.0

<!-- b000757 | prose | pages [18] -->
0.8

<!-- b000758 | prose | pages [18] -->
True Positive Rate

<!-- b000759 | prose | pages [18] -->
0.6

<!-- b000760 | prose | pages [18] -->
0.4

<!-- b000761 | prose | pages [18] -->
0.2

<!-- b000762 | prose | pages [18] -->
0.0

<!-- b000763 | prose | pages [18] -->
0.0 0.2 0.4 0.6 0.8 False Positive Rate

<!-- b000764 | prose | pages [18] -->
ROC of class 0, AUC = 0.75

<!-- b000765 | prose | pages [18] -->
ROC of class 1, AUC = 0.75

<!-- b000766 | prose | pages [18] -->
micro-average ROC curve, AUC = 0.75

<!-- b000767 | prose | pages [18] -->
macro-average ROC curve, AUC = 0.75

<!-- b000768 | prose | pages [18] -->
1.0

<!-- b000769 | caption | pages [18] -->
Figure 10: The ROC curve

<!-- b000770 | prose | pages [18] -->
According to the analysis provided, it can be determined that the developed model has a certain degree of accuracy in predicting changes in the game’s trend. Nevertheless, there remain numerous enhancements to be made to the model in order to enhance the accuracy of the prediction. Here, we will explicitly study it by focusing on a particular women’s singles match at the US Open.

<!-- b000771 | prose | pages [18] -->
Generalized Ability Analysis —U.S. Open Women’s Singles 6.2

<!-- b000772 | prose | pages [18] -->
For the purpose of evaluating the model’s capacity to make generalizations, we have selected the match between C. Gauff and A. Sabalenka, which took place on September 9,

<!-- b000773 | prose | pages [18] -->
关注数学模型

<!-- b000774 | furniture | pages [18] -->
2

<!-- b000775 | furniture | pages [18] -->
MATHmodels

<!-- b000776 | furniture | pages [18] -->
获取更多资讯

<!-- b000777 | furniture | pages [19] -->
Team # 2409404

<!-- b000778 | furniture | pages [19] -->
Page 19 of 25

<!-- b000779 | prose | pages [19] -->
2023, as the women’s singles ﬁnal of the U.S. Open, for our analysis. Initially, we quantiﬁed the technical components of the match, as depicted in Figure 11.

<!-- b000780 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000781 | prose | pages [19] -->
C. Gauff

<!-- b000782 | prose | pages [19] -->
2

<!-- b000783 | prose | pages [19] -->
A. Sabalenka

<!-- b000784 | prose | pages [19] -->
4

<!-- b000785 | prose | pages [19] -->
ACES

<!-- b000786 | prose | pages [19] -->
DOUBLE FAULTS

<!-- b000787 | prose | pages [19] -->
5

<!-- b000788 | prose | pages [19] -->
13

<!-- b000789 | prose | pages [19] -->
6

<!-- b000790 | prose | pages [19] -->
25

<!-- b000791 | prose | pages [19] -->
WINNERS

<!-- b000792 | prose | pages [19] -->
74

<!-- b000793 | prose | pages [19] -->
TOTAL POINTS WON

<!-- b000794 | prose | pages [19] -->
83

<!-- b000795 | prose | pages [19] -->
UNFORCED ERRORS

<!-- b000796 | prose | pages [19] -->
19 46

<!-- b000797 | prose | pages [19] -->
DISTANCE COVERED

<!-- b000798 | prose | pages [19] -->
8702.4 ft 8806.5 ft

<!-- b000799 | prose | pages [19] -->
DISTANCE COVERED/PT.

<!-- b000800 | prose | pages [19] -->
55.4 ft 56.1 ft

<!-- b000801 | prose | pages [19] -->
FIRST SERVE % IN

<!-- b000802 | prose | pages [19] -->
66%

<!-- b000803 | prose | pages [19] -->
62%

<!-- b000804 | prose | pages [19] -->
52%

<!-- b000805 | prose | pages [19] -->
65%

<!-- b000806 | prose | pages [19] -->
WIN % ON 1ST SERVE

<!-- b000807 | prose | pages [19] -->
WIN % ON 2ND SERVE

<!-- b000808 | prose | pages [19] -->
52% 41%

<!-- b000809 | prose | pages [19] -->
BREAK POINTS WON

<!-- b000810 | prose | pages [19] -->
56% 40%

<!-- b000811 | prose | pages [19] -->
NET POINTS WON

<!-- b000812 | prose | pages [19] -->
70%

<!-- b000813 | prose | pages [19] -->
47%

<!-- b000814 | prose | pages [19] -->
62%

<!-- b000815 | prose | pages [19] -->
41%

<!-- b000816 | prose | pages [19] -->
RECEIVING POINTS WON

<!-- b000817 | caption | pages [19] -->
Figure 11: Technical Statistics

<!-- b000818 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000819 | prose | pages [19] -->
By examining the graph, it is evident that Gauff exhibits a notable reduction in unforced errors compared to Sabalenka. However, there is minimal disparity between the two players in terms of other statistics, such as distance covered and serve performance. Gauff gets defeated by Sabalenka’s unforced errors.

<!-- b000820 | prose | pages [19] -->
We integrate the momentum quantitative model with the match ﬂuctuation prediction model and generate visualizations in the form of a ﬂowchart and scatterplot for the corre- sponding match, as depicted in Figure 12 and Figure 13.

<!-- b000821 | prose | pages [19] -->
20

<!-- b000822 | prose | pages [19] -->
15

<!-- b000823 | prose | pages [19] -->
10

<!-- b000824 | prose | pages [19] -->
Momentum

<!-- b000825 | prose | pages [19] -->
5

<!-- b000826 | prose | pages [19] -->
0

<!-- b000827 | prose | pages [19] -->
5

<!-- b000828 | prose | pages [19] -->
10

<!-- b000829 | prose | pages [19] -->
0 1000 2000 3000 4000 Elapsed Time (seconds)

<!-- b000830 | prose | pages [19] -->
2     6     6

<!-- b000831 | prose | pages [19] -->
Gauff

<!-- b000832 | prose | pages [19] -->
6     4     2

<!-- b000833 | prose | pages [19] -->
Sabalenka

<!-- b000834 | prose | pages [19] -->
C. Gauff's Momentum

<!-- b000835 | prose | pages [19] -->
A. Sabalenka's Momentum

<!-- b000836 | prose | pages [19] -->
C. Gauff's Game Point

<!-- b000837 | prose | pages [19] -->
A. Sabalenka's Game Point

<!-- b000838 | prose | pages [19] -->
C. Gauff's Turning Point

<!-- b000839 | prose | pages [19] -->
A. Sabalenka's Turning Point

<!-- b000840 | prose | pages [19] -->
5000 6000 7000

<!-- b000841 | caption | pages [19] -->
Figure 12: Match Flow

<!-- b000842 | prose | pages [19] -->
20

<!-- b000843 | prose | pages [19] -->
15

<!-- b000844 | prose | pages [19] -->
10

<!-- b000845 | prose | pages [19] -->
Momentum

<!-- b000846 | prose | pages [19] -->
5

<!-- b000847 | prose | pages [19] -->
0

<!-- b000848 | prose | pages [19] -->
5

<!-- b000849 | prose | pages [19] -->
10

<!-- b000850 | prose | pages [19] -->
0 1000 2000 3000 4000 5000 Elapsed Time (seconds)

<!-- b000851 | prose | pages [19] -->
15

<!-- b000852 | prose | pages [19] -->
15

<!-- b000853 | prose | pages [19] -->
10

<!-- b000854 | prose | pages [19] -->
10

<!-- b000855 | prose | pages [19] -->
A. Sabalenka

<!-- b000856 | prose | pages [19] -->
C. Gauff

<!-- b000857 | prose | pages [19] -->
5

<!-- b000858 | prose | pages [19] -->
5

<!-- b000859 | prose | pages [19] -->
0

<!-- b000860 | prose | pages [19] -->
0

<!-- b000861 | prose | pages [19] -->
5

<!-- b000862 | prose | pages [19] -->
5

<!-- b000863 | prose | pages [19] -->
10

<!-- b000864 | prose | pages [19] -->
6000 7000

<!-- b000865 | caption | pages [19] -->
Figure 13: Match Flow Scatter

<!-- b000866 | prose | pages [19] -->
关注数学模型

<!-- b000867 | furniture | pages [19] -->
2

<!-- b000868 | furniture | pages [19] -->
MATHmodels

<!-- b000869 | furniture | pages [19] -->
获取更多资讯

<!-- b000870 | furniture | pages [20] -->
Team # 2409404

<!-- b000871 | furniture | pages [20] -->
Page 20 of 25

<!-- b000872 | prose | pages [20] -->
Upon analyzing the visualization with the score changes, it becomes evident that the momentum also inﬂuences the trajectory of the women’s singles match. In the initial set, Sabalenka consistently maintained a lead over Gauff by scoring consecutive points. With her strong momentum, Sabalenka easily secured victory in the ﬁrst set. However, start-

<!-- b000873 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000874 | prose | pages [20] -->
ing with the second set, Sabalenka began to commit unforced errors, resulting in a shift of momentum in favor of Gauff. At this juncture, the disparity in momentum was not signif- icant; hence, Guaff emerged victorious in the second set by a narrow margin. Sabalenka’s signiﬁcant decline in momentum throughout the third set was primarily due to her high number of unforced errors. Consequently, she suffered a substantial defeat in the third set. Meanwhile, it is observed that Guaff consistently exhibits a larger average momentum than Sablenka throughout the match. Furthermore, the distribution of momentum in the sets won by Guaff is notably greater than that of Sablenka, as depicted in the scatterplot.

<!-- b000875 | prose | pages [20] -->
Through the above analysis, combined with the technical statistics, the actual situation of the game, and the visualization of the game ﬂow, we can ﬁnd that the established model can be adapted to different types of games, with an excellent generalization ability.

<!-- b000876 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000877 | prose | pages [20] -->
6.3 Future Consideration

<!-- b000878 | prose | pages [20] -->
Through the above analysis, we can ﬁnd that the model works better. However, there are still some deﬁciencies that need to be considered in future models, which are summa- rized.

<!-- b000879 | prose | pages [20] -->
• The result of the referee’s call. Referees and players may not be consistent in their judgment of the game scenarios, and it is reasonable to expect wrong judgments, mis- judgments, and disputes. When the penalties exceed the coaches’ and athletes’ pre- game preparation and past experience, it will sharply reduce the momentum, leading to a critical response, disrupting the pre-game tactical deployment, and causing heart ﬂuctuations. • The athlete’s ability to self-adjust. Under high competition stress conditions, ath- letes’ psychological reactions are different from normal, and their emotional reactions are richer, which will lead to changes in their own momentum. However, the self- adjustment ability of different athletes varies greatly. Some athletes can quickly detach from the low momentum and reduce the impact of the momentum on themselves, while others have poor self-adjustment abilities and will be immersed in the low mo- mentum for a long time. • The level of the opponent. If your athlete has lost to the other athlete, or if the other athlete is a veteran whose strength is well known to the public, your athlete will over- estimate the opponent’s strength and develop fear and stage fright, which will seri- ously reduce your momentum. • Coach’s guidance. When an athlete’s momentum appears to diminish and affect his or her game form, effective coaching and reassurance from the coach can enable the athlete to regain his or her form and stabilize his or her momentum. • Type of venue. The probability of winning varies somewhat from athlete to athlete at different venues. For example, on hard courts, the Russians, Americans, and French

<!-- b000880 | prose | pages [20] -->
关注数学模型

<!-- b000881 | furniture | pages [20] -->
2

<!-- b000882 | furniture | pages [20] -->
MATHmodels

<!-- b000883 | furniture | pages [20] -->
获取更多资讯

<!-- b000884 | furniture | pages [21] -->
Team # 2409404

<!-- b000885 | furniture | pages [21] -->
Page 21 of 25

<!-- b000886 | prose | pages [21] -->
win the most matches. Looking at clay courts, Russians, Americans, and French are in the top three. On turf courts, Americans, Russians, and Australians are in the top three. On carpeted grounds, the Russians, the French, and the Australians take the top three spots. This has to do with their country’s training grounds; when an athlete

<!-- b000887 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000888 | prose | pages [21] -->
plays on a ﬁeld they are familiar with, their momentum will increase and it will be easier to get into shape. • Spectators’ applause. When a player scores a point and the audience cheers for him, the player not only increases his momentum by scoring a point, but the audience’s applause also increases his momentum, and his status will be better in the following game. If a player loses points and the audience boos or even applauds because of dissatisfaction, the player’s momentum will be seriously affected, and his or her game status will be in tatters.

<!-- b000889 | prose | pages [21] -->
7

<!-- b000890 | heading | pages [21] -->
Sensitivity Analysis

<!-- b000891 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000892 | prose | pages [21] -->
In order to quantitatively model momentum, we have already determined two signif- icant factors: the sliding window size, denoted as β, and the out-of-play advantage of a player’s serve, denoted as α. These parameters are now being modiﬁed to simulate various types of matches with varied serve advantages. Previously, we computed the momentum for each player. To enhance the presentation of the ﬁndings, we calculate the disparity in momentum between two players. Assuming player 1 as his reference point, when the curve is situated below the horizontal axis, it indicates that momentum is located on the other side, and vice versa. As depicted in Figure 14 and Figure 15.

<!-- b000893 | prose | pages [21] -->
30

<!-- b000894 | prose | pages [21] -->
Momentum Difference

<!-- b000895 | prose | pages [21] -->
20

<!-- b000896 | prose | pages [21] -->
10

<!-- b000897 | prose | pages [21] -->
0

<!-- b000898 | prose | pages [21] -->
10

<!-- b000899 | prose | pages [21] -->
20

<!-- b000900 | prose | pages [21] -->
30

<!-- b000901 | prose | pages [21] -->
0 2000 4000 6000 8000

<!-- b000902 | prose | pages [21] -->
α = 0.5, β = 5

<!-- b000903 | prose | pages [21] -->
α = 0.6, β = 5

<!-- b000904 | prose | pages [21] -->
α = 0.7, β = 5

<!-- b000905 | prose | pages [21] -->
α = 0.8, β = 5

<!-- b000906 | prose | pages [21] -->
10000 12000 14000 16000 Elapsed Time (seconds)

<!-- b000907 | caption | pages [21] -->
Figure 14: The Sensitivity Test for α

<!-- b000908 | prose | pages [21] -->
30

<!-- b000909 | prose | pages [21] -->
Momentum Difference

<!-- b000910 | prose | pages [21] -->
20

<!-- b000911 | prose | pages [21] -->
10

<!-- b000912 | prose | pages [21] -->
0

<!-- b000913 | prose | pages [21] -->
10

<!-- b000914 | prose | pages [21] -->
20

<!-- b000915 | prose | pages [21] -->
30

<!-- b000916 | prose | pages [21] -->
α = 0.68, β = 3

<!-- b000917 | prose | pages [21] -->
α = 0.68, β = 4

<!-- b000918 | prose | pages [21] -->
α = 0.68, β = 5

<!-- b000919 | prose | pages [21] -->
α = 0.68, β = 6

<!-- b000920 | prose | pages [21] -->
10000 0 2000 4000 6000 8000 12000 14000 16000 Elapsed Time (seconds)

<!-- b000921 | caption | pages [21] -->
Figure 15: The Sensitivity Test for β

<!-- b000922 | prose | pages [21] -->
Upon examining the aforementioned graphs, it is evident that when subjected to a

<!-- b000923 | prose | pages [21] -->
关注数学模型

<!-- b000924 | furniture | pages [21] -->
2

<!-- b000925 | furniture | pages [21] -->
MATHmodels

<!-- b000926 | furniture | pages [21] -->
获取更多资讯

<!-- b000927 | furniture | pages [22] -->
Team # 2409404

<!-- b000928 | furniture | pages [22] -->
Page 22 of 25

<!-- b000929 | prose | pages [22] -->
speciﬁc perturbation of α and β, the disparity in the players’ momentum undergoes a dis- cernible alteration, particularly when β is modiﬁed. However, overall, the momentum’s trajectory stays unaltered. Put simply, the model effectively captures the player’s condition over various matches. Hence, it is logical and justiﬁable that the curve may undergo signiﬁ-

<!-- b000930 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000931 | prose | pages [22] -->
cant changes at certain nodes. The pattern of the sensitivity test curve aligns with the actual condition once again, overall.

<!-- b000932 | prose | pages [22] -->
8

<!-- b000933 | heading | pages [22] -->
Model Evaluation

<!-- b000934 | prose | pages [22] -->
8.1

<!-- b000935 | heading | pages [22] -->
Strengths

<!-- b000936 | prose | pages [22] -->
• The model is systematic. When selecting metrics for the purpose of calculating mo- mentum, this model encompasses the entirety of the race, rather than examining only a single segment. Makes the results more relevant.

<!-- b000937 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000938 | prose | pages [22] -->
• When calculating the momentum, the scores of both the enemy and the opponent are considered at the same time, and the calculation results are more in line with the reality. • When studying whether the momentum will have an impact on the game situation, two models, namely, the tour test and the chi-square test, were used for comparative analysis, so as to make the results more accurate. • The distribution of data was obtained through principal component analysis to deter- mine the XGboost prediction model, which resulted in a higher accuracy of prediction.

<!-- b000939 | prose | pages [22] -->
8.2

<!-- b000940 | heading | pages [22] -->
Weaknesses and Improvements

<!-- b000941 | prose | pages [22] -->
• This model is only applicable to individual matches. Team momentum is not simply the sum of individual momentum, if we want to solve the momentum problem of group matches, then we also need to consider the impact of teammates’ scores or losses on each other’s momentum. • When making predictions, optimisation algorithms such as Bayesian tuning can be combined to further optimise the model hyper-parameters in order to improve predic- tion accuracy. The main method is to ﬁt a proxy model with known hyperparameters x and model results y, then use the acquisition function to select the next best (x, y), and use this new (x, y) to optimise the proxy model, repeat the above process, and ﬁnally obtain the tuned parameters.

<!-- b000942 | prose | pages [22] -->
9

<!-- b000943 | heading | pages [22] -->
Conclusion

<!-- b000944 | prose | pages [22] -->
Initially, we constructed a momentum quantiﬁcation model using a sliding-window approach. This involved specifying the size of the sliding window and evaluating the mo- mentum value of a player by considering their performance in each metric during that win- dow. In the model, we incorporate the extra beneﬁt of the player’s serve to replicate the

<!-- b000945 | prose | pages [22] -->
关注数学模型

<!-- b000946 | furniture | pages [22] -->
2

<!-- b000947 | furniture | pages [22] -->
MATHmodels

<!-- b000948 | furniture | pages [22] -->
获取更多资讯

<!-- b000949 | furniture | pages [23] -->
Team # 2409404

<!-- b000950 | furniture | pages [23] -->
Page 23 of 25

<!-- b000951 | prose | pages [23] -->
fact that in a tennis match, the serving player has a greater likelihood of winning. Simul- taneously, we analyze the crucial aspects of the match, from which we generate a visual representation of the match’s progression. This visualization allows for a clear assessment of the status and exceptional performance of each player.

<!-- b000952 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000953 | prose | pages [23] -->
Subsequently, by employing the run test and chi-square test, it was determined that momentum plays a pivotal role in the game dynamics of tennis. Hence, it is imperative for coaches and players to acknowledge the signiﬁcance of momentum.

<!-- b000954 | prose | pages [23] -->
Afterwards, the data distribution is examined through principal component analysis in order to construct a game ﬂuctuation prediction model using XGBoost. This model exhibits a higher level of accuracy, reaching up to 70 %, in predicting changes in game situations. Additionally, it identiﬁes signiﬁcant factors such as Double Fault, ACE, and consecutive scores of players.

<!-- b000955 | prose | pages [23] -->
On this basis, we evaluate the model, assess its capacity to generalize, and conduct sensitivity tests on the US Open women’s singles matches. The analysis indicates that the

<!-- b000956 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000957 | prose | pages [23] -->
model exhibits exceptional performance, possesses a high degree of generalization, demon- strates resilience, and can be easily modiﬁed for application to different types of matches. Furthermore, we provide an enumeration of the aspects that ought to be taken into account in the future to enhance the model.

<!-- b000958 | prose | pages [23] -->
Ultimately, we furnish tennis coaches with insights into the signiﬁcance of momentum and offer guidance on how players can sustain and control momentum throughout a match.

<!-- b000959 | heading | pages [23] -->
References

<!-- b000960 | references | pages [23] -->
[1] Ben Moss and Peter O’Donoghue. Momentum in us open men’s singles tennis. Interna-

<!-- b000961 | references | pages [23] -->
tional Journal of Performance Analysis in Sport, 15(3):884–896, 2015.

<!-- b000962 | references | pages [23] -->
[2] Xiaofei Zhang. Analysis of the characteristics of the key distribution points of world

<!-- b000963 | references | pages [23] -->
elite male tennis players. Master’s thesis, Guangzhou Sport University, 2019.

<!-- b000964 | references | pages [23] -->
Periodic "Fluctuate" Phenomenon of Resisting Event-Group Performance in

<!-- b000965 | references | pages [23] -->
[3] Liang Chen.

<!-- b000966 | references | pages [23] -->
Match. PhD thesis, Soochow University, 2013.

<!-- b000967 | references | pages [23] -->
[4] Jianwei Sun, Bianli Xu, Jia Su, and Xueyong Huang. Application and discussion on runs

<!-- b000968 | references | pages [23] -->
test in epidemiology. Preventive Medicine Tribune, 23(100-103+106), 2017.

<!-- b000969 | references | pages [23] -->
关注数学模型

<!-- b000970 | furniture | pages [23] -->
2

<!-- b000971 | furniture | pages [23] -->
MATHmodels

<!-- b000972 | furniture | pages [23] -->
获取更多资讯

<!-- b000973 | furniture | pages [24] -->
Team # 2409404

<!-- b000974 | furniture | pages [24] -->
Page 24 of 25

<!-- b000975 | heading | pages [24] -->
Memorandum

<!-- b000976 | prose | pages [24] -->
To: Tennis Coaches and Players

<!-- b000977 | prose | pages [24] -->
From: Team # 2409404

<!-- b000978 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000979 | prose | pages [24] -->
Date: Feb 5, 2024

<!-- b000980 | prose | pages [24] -->
Subject: Momentum Comprehension, Momentum Mastery, and Momentum Application

<!-- b000981 | prose | pages [24] -->
Dear sir or madam:

<!-- b000982 | prose | pages [24] -->
Everyone desires success on the court, and our research indicates that momentum

<!-- b000983 | prose | pages [24] -->
could be of assistance to you. In order to aid in the training of you and your players, we

<!-- b000984 | prose | pages [24] -->
have developed a predictive model of the situation during a match and a quantitative

<!-- b000985 | prose | pages [24] -->
model of players' momentum. Moreover, it furnishes players with constructive guidance

<!-- b000986 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000987 | prose | pages [24] -->
on how to adapt to the ever-changing circumstances that transpire on the playing field.

<!-- b000988 | prose | pages [24] -->
We have determined, through an analysis of past tennis matches, that momentum is a

<!-- b000989 | prose | pages [24] -->
critical factor in the sport. Tennis players have the ability to reverse the ultimate result of a

<!-- b000990 | prose | pages [24] -->
match by utilizing the force of momentum. A participant with momentum will experience a

<!-- b000991 | prose | pages [24] -->
sense that everything is proceeding in their favor. Additionally, the player will be playing

<!-- b000992 | prose | pages [24] -->
with increased assurance at this juncture, and the momentum will assist in sustaining that

<!-- b000993 | prose | pages [24] -->
assurance. A player should continue to execute the shots that help him or her acquire

<!-- b000994 | prose | pages [24] -->
momentum in tennis—perhaps aggressive play or solid play—in order to maintain

<!-- b000995 | prose | pages [24] -->
momentum and thus play tennis fearlessly.

<!-- b000996 | prose | pages [24] -->
The Momentum quantification model generates specific values by measuring each

<!-- b000997 | prose | pages [24] -->
participant's momentum values at every instant to determine who is performing better at a

<!-- b000998 | prose | pages [24] -->
particular moment in the match. Given the significant degree of unpredictability

<!-- b000999 | prose | pages [24] -->
surrounding the trajectory of the match, this model employs the concept of a sliding

<!-- b001000 | prose | pages [24] -->
window, which comprises two critical parameters: the sliding window's magnitude and the

<!-- b001001 | prose | pages [24] -->
additional benefit that a player's serve can confer. It is adaptable and can be modified in

<!-- b001002 | prose | pages [24] -->
accordance with various contests. The in-match situation prediction model can provide

<!-- b001003 | prose | pages [24] -->
real-time forecasts of the match's fluctuating trajectory and identify significant influencing

<!-- b001004 | prose | pages [24] -->
factors, including the player's Double Fault, ACE, and other relevant data.

<!-- b001005 | prose | pages [24] -->
Furthermore, the majority of Momentum's fluctuations transpire when a player

<!-- b001006 | prose | pages [24] -->
assumes the initiative and endeavors to maintain it throughout the course of the game.

<!-- b001007 | prose | pages [24] -->
关注数学模型

<!-- b001008 | furniture | pages [24] -->
2

<!-- b001009 | furniture | pages [24] -->
MATHmodels

<!-- b001010 | furniture | pages [24] -->
获取更多资讯

<!-- b001011 | furniture | pages [25] -->
Team # 2409404

<!-- b001012 | furniture | pages [25] -->
Page 25 of 25

<!-- b001013 | prose | pages [25] -->
During this phase of the game, participants are averse to losing their lead and are reluctant

<!-- b001014 | prose | pages [25] -->
to relinquish it. A shift in momentum does not warrant a loss of confidence in the game.

<!-- b001015 | prose | pages [25] -->
Maintaining perseverance and a positive mindset are critical factors in regaining the upper

<!-- b001016 | prose | pages [25] -->
微信公众号：数学模型

<!-- b001017 | prose | pages [25] -->
hand. However, the player might be required to alter their playing manner or return to

<!-- b001018 | prose | pages [25] -->
their initial approach to the game.

<!-- b001019 | prose | pages [25] -->
Based on our analysis of the results, we propose the following recommendations

<!-- b001020 | prose | pages [25] -->
(strategies):

<!-- b001021 | prose | pages [25] -->
In order to mitigate the impact of referee errors, missed opportunities, and other 

<!-- b001022 | prose | pages [25] -->
such occurrences on players' confidence, coaches ought to prioritize the cultivation of

<!-- b001023 | prose | pages [25] -->
psychological qualities. This entails supporting players in maintaining a positive outlook,

<!-- b001024 | prose | pages [25] -->
exercising patience, and having self-belief throughout the game.

<!-- b001025 | prose | pages [25] -->
微信号：MATHmodels

<!-- b001026 | prose | pages [25] -->
A diversity of venues should be covered in player training so that players do not 

<!-- b001027 | prose | pages [25] -->
become nervous when playing in unfamiliar areas.

<!-- b001028 | prose | pages [25] -->
Players ought to allocate physical energy judiciously; if physical energy is 

<!-- b001029 | prose | pages [25] -->
consumed too rapidly, the momentum value will remain in a comparatively low state.

<!-- b001030 | prose | pages [25] -->
Analyze the playing technique of your opponent prior to the match and adjust 

<!-- b001031 | prose | pages [25] -->
your strategy accordingly to gain momentum on the field.

<!-- b001032 | prose | pages [25] -->
Standardization of movements and techniques is required, and training must be 

<!-- b001033 | prose | pages [25] -->
reinforced.

<!-- b001034 | prose | pages [25] -->
Of course, our model only plays the role of prediction, but it can be enough to help you.

<!-- b001035 | prose | pages [25] -->
Thank you for reading our memo again in your busy schedule, and we hope our

<!-- b001036 | prose | pages [25] -->
suggestions are useful to you!

<!-- b001037 | prose | pages [25] -->
Yours Sincerely,

<!-- b001038 | furniture | pages [25] -->
Team # 2409404

<!-- b001039 | prose | pages [25] -->
关注数学模型

<!-- b001040 | furniture | pages [25] -->
2

<!-- b001041 | furniture | pages [25] -->
MATHmodels

<!-- b001042 | furniture | pages [25] -->
获取更多资讯
