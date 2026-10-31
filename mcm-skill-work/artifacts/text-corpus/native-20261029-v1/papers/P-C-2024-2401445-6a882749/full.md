# P-C-2024-2401445-6a882749

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | furniture | pages [1] -->
2401445

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Unveiling the Dynamics of Tennis

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
The 2023 Wimbledon final witnessed young prodigy Carlos Alcaraz overturn a seasoned champion, also sparking debates on the role of momentum in tennis. In this paper, we build an evaluative model to measure players’ dynamic state, validated the existence of momentum, and created a predictive model for momentum swings.

<!-- b000012 | prose | pages [1] -->
First, after data preprocessing, we introduce the Dynamic Play Index (DPI) to measure match flow. We quantify DPI using a linear combination of performance(PE),

<!-- b000013 | heading | pages [1] -->
personal strength(PS), and serving advantage(SA). Specifically, we quantify PE with

<!-- b000014 | prose | pages [1] -->
probabilities from Gradient Boosting Trees based on Grid Search (GBDT), summa- rize PS with a six-dimensional evaluation index, and represent SA with a binary vari-

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
able. Thus, We yield GBDT’s optimal parameters: [learning rate: 0.2, max depth: 5, n estimators: 300], and achieve an accuracy of 82.4%. Consequently, we calculate the DPI at each match moment as DPI = 0.28 × PE + 0.32 × PS + 0.4 × SA. Employ- ing this methodology, we effectively delineate the match flow for the 2023 Wimbledon encounter, match ID "2023-wimbledon-1701".

<!-- b000017 | prose | pages [1] -->
Then, to prove the existence of momentum, we employ a proof by contradiction, initially assuming that momentum does not exist. We combine Gaussian distribu- tions with PS and SA from Task 1. Using these, we simulate scores for 7 matches, from quarter-finals to the final. We compare these simulated scores to actual scores using the Dynamic Time Warping (DTW) algorithm. We find that Model 1’s score predictions, implying the presence of momentum, align more closely with actual data, showing a similarity closer to 50% than those of simulations assuming no momentum.

<!-- b000018 | prose | pages [1] -->
After that, we develop a turning point prediction model using Random Forest Classification and the Hidden Markov Model (HMM). First, we define the momen- tum based on the performance difference from Model I. Using Random Forest, we predict momentum shift with a 77.6% accuracy rate. Moreover, the model identifies the five most critical indicators for momentum shifts, with the player’s consecutive points being the most significant. Next, we employ HMM to explain how different players react to momentum changes and offer four suggestions targeting momentum.

<!-- b000019 | prose | pages [1] -->
Next, we apply Model II to the men’s singles match "wimbledon-1602", the women’s singles "wimbledon-2503", and the acrylic surface match "usopen-1102". The model performs slightly better in the first two cases but poorly in the last. Considering re- call rates, we suggest incorporating factors like court surface material to refine the model. Additionally, we introduce Gaussian noise to the significant indicators to test sensitivity. The model’s accuracy falls 8%, demonstrating robustness.

<!-- b000020 | prose | pages [1] -->
Finally, we discuss the strengths and weaknesses of our model and report the find- ings in a memo to the coaches.

<!-- b000021 | keywords | pages [1] -->
Keywords: Dynamic Play Index; Dynamic Time Warping; Random Forest; Hidden

<!-- b000022 | prose | pages [1] -->
Markov Model.

<!-- b000023 | prose | pages [1] -->
关注数学模型

<!-- b000024 | furniture | pages [1] -->
2

<!-- b000025 | furniture | pages [1] -->
MATHmodels

<!-- b000026 | furniture | pages [1] -->
获取更多资讯

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1

<!-- b000029 | heading | pages [2] -->
Introduction

<!-- b000030 | prose | pages [2] -->
3 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000031 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000032 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Restatement of the Problem 3 Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000033 | prose | pages [2] -->
2

<!-- b000034 | heading | pages [2] -->
Assumption

<!-- b000035 | prose | pages [2] -->
3

<!-- b000036 | heading | pages [2] -->
Notations

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | prose | pages [2] -->
4

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | heading | pages [2] -->
Model I: Measuring the flow of the match by DPI

<!-- b000041 | prose | pages [2] -->
4 6 Model Establishment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 6 Data preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 6 Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 7 Personal Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.3 9 Serving Advantage . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.4 9 Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 9

<!-- b000042 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000043 | prose | pages [2] -->
Task 2: Proving the Existence of Momentum 5 10 . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Simulating the Game Process 11 Quantifying the similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 11 Assessing the similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 12

<!-- b000044 | heading | pages [2] -->
Model II: Momentum Turning Point Identification and Prediction Model

<!-- b000045 | prose | pages [2] -->
6 based on HMM-Random Forest 13 Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.1 Momentum 13 Swing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.2 13 Turning Point . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.3 13 Figuring Out the Main indicators . . . . . . . . . . . . . . . . . . . . . . . 6.2 13 Adjusting the Model based on HMM . . . . . . . . . . . . . . . . . . . . . 6.3 15 The Final Piece of the Model: Situational Leverage . . . . . . . . . . . . . 6.4 16 Results and Advices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.5

<!-- b000046 | prose | pages [2] -->
7

<!-- b000047 | heading | pages [2] -->
Task 4: Model Generalization

<!-- b000048 | prose | pages [2] -->
16

<!-- b000049 | prose | pages [2] -->
18 2023 Wimbledon Men’s Singles 1602: Jannik Sinner VS Novak Djokovic . . 7.1 19 2023 Wimbledon Women’s Singles 2503: Ons Jabeur VS Elena Rybakina . . 7.2 19 2020 US Open 1102: Alexandre Muller VS Arthur Rinderknech . . . . . . . . 7.3

<!-- b000050 | prose | pages [2] -->
8

<!-- b000051 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000052 | prose | pages [2] -->
9

<!-- b000053 | heading | pages [2] -->
Strength and Weakness

<!-- b000054 | prose | pages [2] -->
20

<!-- b000055 | prose | pages [2] -->
20

<!-- b000056 | prose | pages [2] -->
20 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 20 Weakness and Further Discussion . . . . . . . . . . . . . . . . . . . . . . . 9.2

<!-- b000057 | prose | pages [2] -->
Reference

<!-- b000058 | heading | pages [2] -->
10 Memorandum for The Coaches

<!-- b000059 | heading | pages [2] -->
Appendices

<!-- b000060 | prose | pages [2] -->
21

<!-- b000061 | prose | pages [2] -->
22

<!-- b000062 | prose | pages [2] -->
23

<!-- b000063 | prose | pages [2] -->
25

<!-- b000064 | heading | pages [2] -->
Appendix A Indicators Chosen for Training Random Forest Model

<!-- b000065 | prose | pages [2] -->
25

<!-- b000066 | prose | pages [2] -->
关注数学模型

<!-- b000067 | furniture | pages [2] -->
2

<!-- b000068 | furniture | pages [2] -->
MATHmodels

<!-- b000069 | furniture | pages [2] -->
获取更多资讯

<!-- b000070 | furniture | pages [3] -->
Team # 2401445

<!-- b000071 | prose | pages [3] -->
1

<!-- b000072 | heading | pages [3] -->
Introduction

<!-- b000073 | prose | pages [3] -->
1.1 Problem Background

<!-- b000074 | furniture | pages [3] -->
Page 3 of 26

<!-- b000075 | prose | pages [3] -->
In sports, "momentum" is seen as a dual-edged sword, capable of propelling ath-

<!-- b000076 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000077 | prose | pages [3] -->
letes towards victory or serving as a pivotal factor in turning the tide of defeat. It’s widely regarded as a crucial determinant of success. However, the real impact of mo- mentum in tennis sparks a heated debate.

<!-- b000078 | prose | pages [3] -->
Some research supports its significant psychological and physiological impacts on players, influencing match outcomes. For example, Dietl, Helmut, and Cornel Nes- seler (2017) found that players have a 54.2% chance of winning the last set after win- ning the penultimate set. Furthermore, Seidl, Robert, and Patrick Lucey (2022) intro- duced a counter-factual method for women’s tennis, automatically highlighting key match moments with "leverage," "clutch," and "momentum" metrics.

<!-- b000079 | prose | pages [3] -->
Conversely, other research disputes the impact of momentum, suggesting it may be a psychological illusion rather than a statistically significant factor. For instance,

<!-- b000080 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000081 | prose | pages [3] -->
analysis from the US Open men’s singles and studies on service point sequences in elite tennis failed to find statistical evidence supporting momentum’s influence on match outcomes[3]. Moreover, studies from O’Donoghue, Peter, and Emily Brown propose that the perceived momentum effect might not significantly alter the course of a match, indicating that outcomes could be influenced more by skill and chance than by a momentum-driven psychological advantage[4].

<!-- b000082 | caption | pages [3] -->
Figure 1: The battle between two parties

<!-- b000083 | prose | pages [3] -->
Therefore, understanding and quantifying momentum’s role is essential for devel- oping adaptive strategies in tennis, providing critical insights for players and coaches to navigate the game’s dynamic challenges.

<!-- b000084 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000085 | prose | pages [3] -->
The challenge at hand involves the analysis of data from the Wimbledon 2023 men’s tennis matches with the objective of gaining insights into the concept of "mo- mentum." The primary tasks to be addressed include:

<!-- b000086 | prose | pages [3] -->
• Measuring the flow of match: Construct a model that illustrates the progression

<!-- b000087 | prose | pages [3] -->
关注数学模型

<!-- b000088 | furniture | pages [3] -->
2

<!-- b000089 | furniture | pages [3] -->
MATHmodels

<!-- b000090 | furniture | pages [3] -->
获取更多资讯

<!-- b000091 | furniture | pages [4] -->
Team # 2401445

<!-- b000092 | furniture | pages [4] -->
Page 4 of 26

<!-- b000093 | prose | pages [4] -->
of gameplay, enabling the identification of the dominant player at any given mo- ment and quantifying their performance advantage. This should also involve the creation of visual representations of the match flow.

<!-- b000094 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000095 | prose | pages [4] -->
• Momentum existence evaluation: Evaluate the assertion that swings in match play and sequences of success are random events, unaffected by the influence of momentum.

<!-- b000096 | prose | pages [4] -->
• Turning point prediction: Develop a system for forecasting instances when the balance of play is likely to shift between players. This should encompass the identification of contributing factors to such changes, along with recommenda- tions for players based on historical patterns of momentum swings.

<!-- b000097 | heading | pages [4] -->
• Model testing and generalization: Apply the developed model to additional

<!-- b000098 | prose | pages [4] -->
matches in order to assess its predictive accuracy and investigate its applica- bility in various contexts, including matches on different playing surfaces and potentially in other sports.

<!-- b000099 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000100 | prose | pages [4] -->
• Reporting: Produce a comprehensive report that consolidates the findings of the analysis and offers coaching advice regarding the role of momentum and strategies for managing shifts in the flow of play during matches.

<!-- b000101 | prose | pages [4] -->
1.3 Our work

<!-- b000102 | caption | pages [4] -->
Figure 2: Our work

<!-- b000103 | prose | pages [4] -->
2

<!-- b000104 | heading | pages [4] -->
Assumption

<!-- b000105 | heading | pages [4] -->
Assumption 1: We assume a player’s individual ability remains constant during

<!-- b000106 | prose | pages [4] -->
a match because a player’s skill level, physical condition, strategy, and mental state are considered fixed throughout the game. This means any variation in match per- formance is attributed to external factors or the opponent’s play, rather than changes in the player’s inherent capability. This assumption simplifies analysis by focusing on match dynamics without accounting for fluctuating player conditions or strategies within the game.

<!-- b000107 | prose | pages [4] -->
关注数学模型

<!-- b000108 | furniture | pages [4] -->
2

<!-- b000109 | furniture | pages [4] -->
MATHmodels

<!-- b000110 | furniture | pages [4] -->
获取更多资讯

<!-- b000111 | furniture | pages [5] -->
Team # 2401445

<!-- b000112 | furniture | pages [5] -->
Page 5 of 26

<!-- b000113 | prose | pages [5] -->
Assumption 2: We assume that a player’s ability value can be inferred from existing match data. This is because the data contains detailed records of perfor- mances, outcomes, and statistics that, when analyzed, reveal patterns and indicators of a player’s skill level. By quantifying these elements, we aim to establish a reliable

<!-- b000114 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000115 | prose | pages [5] -->
measure of individual abilities that can inform further analyses and predictions.

<!-- b000116 | prose | pages [5] -->
Assumption 3: We assume that the player with the serve has an advantage. Be- cause serving initiates play and allows the server to control the game’s pace and style from the outset, historical data and professional observations consistently show that players serving have a higher probability of winning the game. This assumption is foundational for analyzing match dynamics and strategies, considering the serve’s critical role in tennis.

<!-- b000117 | prose | pages [5] -->
3

<!-- b000118 | heading | pages [5] -->
Notations

<!-- b000119 | caption | pages [5] -->
Table 1: Summary of Key Symbols and Their Descriptions

<!-- b000120 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000121 | heading | pages [5] -->
Symbol

<!-- b000122 | prose | pages [5] -->
Description

<!-- b000123 | prose | pages [5] -->
PE Performance PS Personal Strength SA Serving Advantage M Number of Models Decision Tree Obtained from the mth Training Tm PWOL Percentage of Matches in which the Winner Outscored the Loser D Distance Between Two Sequences Q, A, O, B, Π The Parameters of HMM SL Situational Leverage playeri lose the tth point oi,t playeri win the tth point wi,t

<!-- b000124 | prose | pages [5] -->
关注数学模型

<!-- b000125 | furniture | pages [5] -->
2

<!-- b000126 | furniture | pages [5] -->
MATHmodels

<!-- b000127 | furniture | pages [5] -->
获取更多资讯

<!-- b000128 | furniture | pages [6] -->
Team # 2401445

<!-- b000129 | furniture | pages [6] -->
Page 6 of 26

<!-- b000130 | heading | pages [6] -->
Model I: Measuring the flow of the match by DPI

<!-- b000131 | prose | pages [6] -->
4

<!-- b000132 | prose | pages [6] -->
Inspired by the concept of dynamic win probabilities seen in chess, we develop the Dynamic Play Index (DPI) to seek the dynamic flow of tennis. This index dynamically

<!-- b000133 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000134 | prose | pages [6] -->
reflects a player’s performance and likelihood of winning a game, adjusting in real- time with each scored point.

<!-- b000135 | prose | pages [6] -->
We construct the DPI by considering three primary factors: Performance (PE), Per- sonal Strength (PS), and Serving Advantage (SA). The model is represented by the equation

<!-- b000136 | prose | pages [6] -->
DPI = α × PE + β × PS + γ × SA, (1)

<!-- b000137 | prose | pages [6] -->
where α, β, and γ denote the weights for each factor. We aim to keep our model straightforward, employing a linear approach to effectively capture the complex dy- namics of a tennis match, thus enabling us to quantify and visualize the ebb and flow of play and the relative performance of the players throughout a match.

<!-- b000138 | prose | pages [6] -->
4.1

<!-- b000139 | heading | pages [6] -->
Model Establishment

<!-- b000140 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000141 | prose | pages [6] -->
4.1.1 Data preprocessing

<!-- b000142 | prose | pages [6] -->
Upon reviewing the data, we identified missing values primarily in four columns: speed_mph, serve_width, serve_depth, and return_depth. The number of missing values in each column is as shown in the figure. We observed the most significant data gaps in matches 2023-wimbledon-1310 and 2023-wimbledon-1311. In these matches, a large portion of speed_mph data was missing, along with anomalies in rally_count (predominantly zeros). The serve speeds for players Guido Pella and Mikael Ymer were absent.

<!-- b000143 | caption | pages [6] -->
Figure 3: Missing Value Distribution Plot

<!-- b000144 | prose | pages [6] -->
When conducting our analysis on performance, we opted to impute the missing values for speed_mph and rally_count using median values. This approach helps to mitigate the impact of outliers and maintains consistency in the data.

<!-- b000145 | prose | pages [6] -->
For the analysis of personal strength, we decided to remove all performance in- dicators for both players entirely. This decision ensures the accuracy of our analysis

<!-- b000146 | prose | pages [6] -->
关注数学模型

<!-- b000147 | furniture | pages [6] -->
2

<!-- b000148 | furniture | pages [6] -->
MATHmodels

<!-- b000149 | furniture | pages [6] -->
获取更多资讯

<!-- b000150 | furniture | pages [7] -->
Team # 2401445

<!-- b000151 | furniture | pages [7] -->
Page 7 of 26

<!-- b000152 | prose | pages [7] -->
and prevents misleading statistical inferences. By adopting these methods, we aim to provide a reliable and fair assessment of players’ capabilities, taking into account the available data.

<!-- b000153 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000154 | prose | pages [7] -->
4.1.2 Performance

<!-- b000155 | prose | pages [7] -->
To assess a player based on the current situation of the game, we establish a met- ric known as "performance". It’s important to note that this evaluation is distinct from considerations of Personal Strength or external factors. To measure a player’s perfor- mance, we focus on measuring the impact of their actions on the likelihood of winning the current game.

<!-- b000156 | prose | pages [7] -->
Therefore, we define performance as the chance of a player winning a game, pre- dicted by analyzing various situational factors: p1_sets, p2_sets, p1_games, p2_games, p1_current_point, p2_current_point, server, through a Gradient Boosting Trees clas- sification model.

<!-- b000157 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000158 | caption | pages [7] -->
Figure 4: Gradient Boosting Tree + Grid Search Diagram

<!-- b000159 | prose | pages [7] -->
In our analysis, the principle of the Gradient Boosting Trees (GBT) classification model is central to quantifying player performance. As we can see on the graph above, this model is an ensemble of decision trees, formulated as an additive model where each tree incrementally improves the model’s accuracy. The fundamental expression for a boosting tree model is represented as:

<!-- b000160 | prose | pages [7] -->
M X

<!-- b000161 | prose | pages [7] -->
F(x) =

<!-- b000162 | prose | pages [7] -->
m=1

<!-- b000163 | prose | pages [7] -->
Tm(x; Θm) (2)

<!-- b000164 | prose | pages [7] -->
where F(x) denotes the final model, Tm(x; Θm) represents the mth decision tree pa- rameterized by Θm, and M is the total number of trees.

<!-- b000165 | prose | pages [7] -->
The GBT algorithm updates the model iteratively, allowing each subsequent tree to correct the residuals of the predictions from all previous trees. At step m, the model is updated as follows:

<!-- b000166 | prose | pages [7] -->
Fm(x) = Fm−1(x) + αTm(x; Θm) (3)

<!-- b000167 | prose | pages [7] -->
关注数学模型

<!-- b000168 | furniture | pages [7] -->
2

<!-- b000169 | furniture | pages [7] -->
MATHmodels

<!-- b000170 | furniture | pages [7] -->
获取更多资讯

<!-- b000171 | furniture | pages [8] -->
Team # 2401445

<!-- b000172 | furniture | pages [8] -->
Page 8 of 26

<!-- b000173 | prose | pages [8] -->
where α is the learning rate controlling the contribution of each tree. This sequential correction aims to minimize a loss function, L, which for a binary classification prob- lem, often employs the exponential loss function to effectively differentiate between the two classes:

<!-- b000174 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000175 | prose | pages [8] -->
L(y, y′) = exp(−yy′) (4)

<!-- b000176 | prose | pages [8] -->
Building on the fou ndational principles of the Gradient Boosting Trees model, we actively employ grid search to optimize its hyperparameters. This approach system- atically explores a spectrum of parameter values to identify the set that minimizes the prediction error. By evaluating the model’s performance across all possible combina- tions of predefined hyperparameters, we ensure the refinement and accuracy of our predictions:

<!-- b000177 | prose | pages [8] -->
Grid Search = min

<!-- b000178 | prose | pages [8] -->
Θ L(F(x; Θ), y) (5)

<!-- b000179 | prose | pages [8] -->
Adapting the Gradient Boosting Trees model to our analysis, it’s noteworthy that although the GBT algorithm fundamentally outputs binary classification results—indicating

<!-- b000180 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000181 | prose | pages [8] -->
win or loss for each game — we utilize the probability estimated by the classifier for a win as the value of "performance". This method transforms binary win-loss out- comes into a continuous measure of win probability.

<!-- b000182 | prose | pages [8] -->
Gradient Boosting Trees stand out in this tennis analysis for their precision. This method significantly enhances our capability to predict tennis match results, achieving a prediction accuracy of 82.4% for the final match based on earlier data, thus validating the effectiveness of our performance model.

<!-- b000183 | caption | pages [8] -->
Figure 5: Performance for Alcaraz as Points Occur

<!-- b000184 | prose | pages [8] -->
The graph we present illustrates the performance of Carlos Alcaraz during the final match. In this graph, the x-axis represents the cumulative score between the competi- tors, while the y-axis indicates his performance. Notably, points where performance exceeds 0.5 are highlighted in bold. This visualization distinctly highlights that, based solely on the scoring dynamics within the match, Alcaraz often found himself in a po- sition of advantage. It’s important to note that this metric focuses exclusively on the

<!-- b000185 | heading | pages [8] -->
current score situation, without factoring in individual strengths, serving turns, or

<!-- b000186 | prose | pages [8] -->
other external elements.

<!-- b000187 | prose | pages [8] -->
关注数学模型

<!-- b000188 | furniture | pages [8] -->
2

<!-- b000189 | furniture | pages [8] -->
MATHmodels

<!-- b000190 | furniture | pages [8] -->
获取更多资讯

<!-- b000191 | furniture | pages [9] -->
Team # 2401445

<!-- b000192 | prose | pages [9] -->
4.1.3

<!-- b000193 | heading | pages [9] -->
Personal Strength

<!-- b000194 | furniture | pages [9] -->
Page 9 of 26

<!-- b000195 | prose | pages [9] -->
In our initial analysis, we focused solely on situational factors. Now, we expand our perspective to include individual player capabilities. Drawing on the research

<!-- b000196 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000197 | prose | pages [9] -->
by Fitzpatrick et al. (2019), we utilize the PWOL (Percentage of matches in which the Winner Outscored the Loser) method to identify six key indicators of elite tennis players, summarized as the table below.

<!-- b000198 | caption | pages [9] -->
Table 2: Summary of Personal Strength

<!-- b000199 | prose | pages [9] -->
Characteristic Equation PWOL

<!-- b000200 | prose | pages [9] -->
1st serve-return wins/1st serve-returns × 100 1st Serve-Return Win % 80.2% Break points won/Break points played × 100 Break Points Won % 68.3% Points won 0–4 rally/Points played 0–4 rally × 100 0-4 Rally Win % 66.1% Mean 1st serve speed Avg. 1st Serve Speed Aces % 54.7% Aces/Serves × 100 52.7% Double faults/Points served × 100 Double Faults % 47.6%

<!-- b000201 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000202 | prose | pages [9] -->
Untouchable Rate % based on p1_winner 33.4%

<!-- b000203 | prose | pages [9] -->
As to the calculation of Overall Individual Capability, we initially map the actual values of the indicators to a 60-100 scale in order to standardize the range of values. Subsequently, we apply a weighted average calculation based on the PWOL values to derive the player’s composite score. This process is encapsulated in the following formula:

<!-- b000204 | prose | pages [9] -->
Pn

<!-- b000205 | prose | pages [9] -->
i=1 IndexScorei × PWOLi

<!-- b000206 | prose | pages [9] -->
PS =

<!-- b000207 | prose | pages [9] -->
Pn

<!-- b000208 | prose | pages [9] -->
(6)

<!-- b000209 | prose | pages [9] -->
i=1 PWOLi

<!-- b000210 | prose | pages [9] -->
where PS is the player’s overall strength score, calculated as a weighted average based on key indicators; IndexScorei is the normalized score for the ith indicator, adjusted to a 60-100 scale; PWOLi denotes the weight of the ith indicator, reflecting its importance according to the "Percentage of matches in which the Winner Outscored the Loser".

<!-- b000211 | prose | pages [9] -->
4.1.4 Serving Advantage

<!-- b000212 | prose | pages [9] -->
We also acknowledge the importance of service in tennis, as studies have shown that players often win more points while serving than receiving (Furlong, 1995; O’ Donoghue and Ballantyne, 2004). Therefore, we identify the serving advantage as a key feature in our model. We define this advantage using a binary variable:

<!-- b000213 | prose | pages [9] -->
(

<!-- b000214 | prose | pages [9] -->
if player i is serving, 1

<!-- b000215 | prose | pages [9] -->
SA =

<!-- b000216 | prose | pages [9] -->
(7) otherwise. 0

<!-- b000217 | prose | pages [9] -->
4.2

<!-- b000218 | heading | pages [9] -->
Model Evaluation

<!-- b000219 | prose | pages [9] -->
Through the examination of relevant literature and parameter tuning practices, we have ultimately determined the weights for three indicators as follows:

<!-- b000220 | prose | pages [9] -->
α = 0.28, β = 0.32, γ = 0.4

<!-- b000221 | prose | pages [9] -->
关注数学模型

<!-- b000222 | furniture | pages [9] -->
2

<!-- b000223 | furniture | pages [9] -->
MATHmodels

<!-- b000224 | furniture | pages [9] -->
获取更多资讯

<!-- b000225 | furniture | pages [10] -->
Team # 2401445

<!-- b000226 | furniture | pages [10] -->
Page 10 of 26

<!-- b000227 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000228 | caption | pages [10] -->
Figure 6: DPI plot of the final

<!-- b000229 | prose | pages [10] -->
Consequently, we have plotted the Dynamic Performance Index (DPI) over the scoring sequence of the final match, as illustrated below.

<!-- b000230 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000231 | prose | pages [10] -->
Dividing the total of 334 scoring records of the final match into five segments, each representing a set of the game, and based on the description of the match dynamics, we evaluate whether our model accurately reflects which player is performing better at any given time during the match, as well as the extent of their performance advantage.

<!-- b000232 | prose | pages [10] -->
• In the first set, Djokovic seemed destined to win easily as he dominated 6 – 1. The DPI curve from points 0 to 45 shows Djokovic’s DPI, despite fluctuations, was significantly ahead of Alcaraz.

<!-- b000233 | prose | pages [10] -->
• The second set was tense and finally won by Alcaraz in a tie-breaker 7 – 6. The curve section from points 46 to 139 shows the DPI of both players fluctuating and in- terchanging frequently towards the end, reflecting the intensity of the situation.

<!-- b000234 | prose | pages [10] -->
• The third set was a reversal of the first, with Alcaraz winning comfortably 6 – 1. From points 140 to 209, the curve shows that, after some initial intersections, the young Spaniard’s DPI significantly leads over Djokovic, mirroring the actual scoreline.

<!-- b000235 | prose | pages [10] -->
• In the final two sets, our model showcased its superiority. In the fourth set, the young Spaniard seemed in total control as the set started, but Djokovic took complete control to win the set 6 – 3. This is reflected in our model by the orange curve overcoming the blue.

<!-- b000236 | prose | pages [10] -->
• Carrying the edge from the fourth set, Djokovic seemed poised to maintain the lead, but a shift occurred, and Alcaraz gained control, winning 6 – 4. In our model, the blue curve overtakes the orange in the midsection, eventually surpassing Djokovic’s representation.

<!-- b000237 | prose | pages [10] -->
Task 2: Proving the Existence of Momentum 5

<!-- b000238 | prose | pages [10] -->
For task 2, our approach involves employing a method of contradiction by assum- ing that momentum does not exist in tennis matches. If the conclusions drawn from this assumption significantly diverge from actual data, it would indicate the fallacy of the hypothesis.

<!-- b000239 | prose | pages [10] -->
关注数学模型

<!-- b000240 | furniture | pages [10] -->
2

<!-- b000241 | furniture | pages [10] -->
MATHmodels

<!-- b000242 | furniture | pages [10] -->
获取更多资讯

<!-- b000243 | furniture | pages [11] -->
Team # 2401445

<!-- b000244 | prose | pages [11] -->
5.1 Simulating the Game Process

<!-- b000245 | furniture | pages [11] -->
Page 11 of 26

<!-- b000246 | prose | pages [11] -->
To test the idea that momentum doesn’t affect match outcomes, we simulate games without considering momentum. Our simulation uses Gaussian noise, player strength,

<!-- b000247 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000248 | prose | pages [11] -->
and serving advantagewhich come from the model I, as the only inputs. We treat changes in the game and scoring as completely random. This way, we follow tennis rules but ignore momentum, seeing if match results look different from real ones. The pseudocode for this simulation is shown below:

<!-- b000249 | heading | pages [11] -->
Algorithm 1 Enhanced Simulation of Tennis Matches with Mathematical Notation

<!-- b000250 | prose | pages [11] -->
for i = 1 to 100 do

<!-- b000251 | prose | pages [11] -->
setsA, setsB ←0, 0 while (setsA < 3andsetsB < 3)and(setsA + setsB < 5) do

<!-- b000252 | prose | pages [11] -->
gamesA, gamesB ←0, 0 repeat

<!-- b000253 | prose | pages [11] -->
outcome ←SimulateOutcome(strengthA, strengthB, advantage) gamesA, gamesB ←UpdateGames(gamesA, gamesB, outcome)

<!-- b000254 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000255 | prose | pages [11] -->
if CheckSetWin(gamesA, gamesB) then

<!-- b000256 | prose | pages [11] -->
setsA, setsB ←UpdateSets(setsA, setsB, outcome) break end if until set is decided end while Output(setsA, setsB) end for

<!-- b000257 | prose | pages [11] -->
5.2 Quantifying the similarity

<!-- b000258 | prose | pages [11] -->
In our analysis, we specifically compare sequences of score differences at each point update between two simulations: one that might includes momentum effects and an- other that assumes outcomes are entirely random. By doing so, we transform the prob- lem of comparing two match’s results into the problem of calculating the similarity of two sequences.

<!-- b000259 | prose | pages [11] -->
However, the length of those two sequences might not be the same, since simu- lations will not repeat themselves every time. Therefore, we apply Dynamic time

<!-- b000260 | heading | pages [11] -->
warping (DTW) algorithm to calculate the similarity between two unequal-length

<!-- b000261 | prose | pages [11] -->
sequences.

<!-- b000262 | prose | pages [11] -->
Dynamic Time Warping (DTW) is a renowned technique for analyzing time series, therefore offering a robust solution for comparing sequences that may vary in length or speed.

<!-- b000263 | prose | pages [11] -->
The mathematical foundation of DTW involves constructing a distance matrix D where each element D[i, j] represents the distance between the ith element of the first sequence and the jth element of the second sequence. The DTW algorithm then finds the path through this matrix that minimizes the total distance, which can be formally described as follows:

<!-- b000264 | prose | pages [11] -->
D[i, j] = distance(i, j) + min{D[i −1, j], D[i, j −1], D[i −1, j −1]}

<!-- b000265 | prose | pages [11] -->
关注数学模型

<!-- b000266 | furniture | pages [11] -->
2

<!-- b000267 | furniture | pages [11] -->
MATHmodels

<!-- b000268 | furniture | pages [11] -->
获取更多资讯

<!-- b000269 | furniture | pages [12] -->
Team # 2401445

<!-- b000270 | furniture | pages [12] -->
Page 12 of 26

<!-- b000271 | prose | pages [12] -->
where distance(i, j) calculates the distance between the two points from the sequences being compared.

<!-- b000272 | prose | pages [12] -->
5.3 Assessing the similarity

<!-- b000273 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000274 | prose | pages [12] -->
To assess the similarity between the sequences, two primary methods are utilized:

<!-- b000275 | heading | pages [12] -->
1. Total DTW Distance: The sum of the distances along the optimal path. A lower

<!-- b000276 | prose | pages [12] -->
total distance indicates a higher similarity between the sequences.

<!-- b000277 | heading | pages [12] -->
2. DTW Alignment Path: The path through the matrix that minimizes the cumula-

<!-- b000278 | prose | pages [12] -->
tive distance. Observing how closely the path aligns with the diagonal provides a measure of similarity, as a path near the diagonal suggests a strong correspon- dence between the sequences.

<!-- b000279 | prose | pages [12] -->
We selected seven matches from our Model 1 test set for simulation and com- parison, including four from the quarterfinals, two from the semifinals, and the final.

<!-- b000280 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000281 | prose | pages [12] -->
We generated simulated score sequences using random outcomes and predicted se- quences from Model 1. Employing the DTW algorithm, we calculated the Total DTW Distance for both the simulated sequences against the actual data and the Model 1 pre- dictions against the actual sequences. Additionally, we plotted the DTW Alignment Paths to visually compare the simulated and real sequences, as illustrated in the figure below.

<!-- b000282 | caption | pages [12] -->
Figure 7: DTW Alignment Path and Total DTW Distance

<!-- b000283 | prose | pages [12] -->
From the DTW Alignment Paths displayed in the upper part of the graph, it is evident that the curves of the randomly simulated sequences largely deviate from the diagonal, indicating a significant discrepancy from the actual sequence.

<!-- b000284 | prose | pages [12] -->
Furthermore, by comparing the DTW distances between the randomly simulated results, Model 1 predicted sequences, and the actual data, we observe that, except for the match between Rublev and Djokovic where both simulated and model-predicted distances are low, our model consistently yields a smaller distance compared to the random sequences in other matches.

<!-- b000285 | prose | pages [12] -->
关注数学模型

<!-- b000286 | furniture | pages [12] -->
2

<!-- b000287 | furniture | pages [12] -->
MATHmodels

<!-- b000288 | furniture | pages [12] -->
获取更多资讯

<!-- b000289 | furniture | pages [13] -->
Team # 2401445

<!-- b000290 | furniture | pages [13] -->
Page 13 of 26

<!-- b000291 | prose | pages [13] -->
In conclusion, the simulated random sequences fail to accurately represent real- world data, while the results from Model 1 provide a better prediction. This evidence disproves the initial hypothesis, thereby substantiating the existence of momentum.

<!-- b000292 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000293 | heading | pages [13] -->
Model II: Momentum Turning Point Identification and

<!-- b000294 | prose | pages [13] -->
6

<!-- b000295 | heading | pages [13] -->
Prediction Model based on HMM-Random Forest

<!-- b000296 | prose | pages [13] -->
6.1 Definition

<!-- b000297 | prose | pages [13] -->
Building upon our previous findings in Task 2, where we established the existence of momentum, we now define these concepts more explicitly.

<!-- b000298 | prose | pages [13] -->
6.1.1 Momentum

<!-- b000299 | prose | pages [13] -->
Momentum represents a player’s control over the game’s dynamics. In the con- text of this task, we simplify momentum into a binary state, denoted as follows:

<!-- b000300 | prose | pages [13] -->


<!-- b000301 | prose | pages [13] -->
1, When Player 1 has the upper hand,

<!-- b000302 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000303 | prose | pages [13] -->
 

<!-- b000304 | prose | pages [13] -->
Momentum =

<!-- b000305 | prose | pages [13] -->
2,

<!-- b000306 | prose | pages [13] -->
(8)

<!-- b000307 | prose | pages [13] -->
When Player 2 has the upper hand,

<!-- b000308 | prose | pages [13] -->


<!-- b000309 | prose | pages [13] -->
0, Otherwise.

<!-- b000310 | prose | pages [13] -->


<!-- b000311 | prose | pages [13] -->
Momentum is thus classified as either favoring Player 1, Player 2, or neither.

<!-- b000312 | prose | pages [13] -->
6.1.2 Swing

<!-- b000313 | prose | pages [13] -->
A swing refers to the action of momentum transitioning from 1 to 2 or from 2 to 1. It signifies a significant change in the balance of the match.

<!-- b000314 | prose | pages [13] -->
6.1.3 Turning Point

<!-- b000315 | prose | pages [13] -->
A turning point corresponds to the moment when a swing in momentum occurs. It is associated with a specific time point during the match and coincides with a change in the score that led to the momentum shift.

<!-- b000316 | prose | pages [13] -->
Figuring Out the Main indicators 6.2

<!-- b000317 | prose | pages [13] -->
To identify the key indicators that influence momentum shifts, we need to complete two steps:

<!-- b000318 | prose | pages [13] -->
• First, develop a predictive model to forecast the turning points of momentum shifts.

<!-- b000319 | prose | pages [13] -->
• Second, infer the key indicators based on the results of the model.

<!-- b000320 | prose | pages [13] -->
The Random Forest model aligns perfectly with our requirements for this process.

<!-- b000321 | prose | pages [13] -->
Therefore, in order to prepare our dataset for training the models, we label each data point with momentum using Model 1’s performance predictions. We set a thresh- old ω to distinguish momentum for each player: if player1’s performance minus player2’s > ω, then the momentum for this point is 1.

<!-- b000322 | prose | pages [13] -->
Then, after careful filtering, we select 15 variables to train the model, and a detailed list of the variables are listed in the appendix A. And the results are as follows:

<!-- b000323 | prose | pages [13] -->
关注数学模型

<!-- b000324 | furniture | pages [13] -->
2

<!-- b000325 | furniture | pages [13] -->
MATHmodels

<!-- b000326 | furniture | pages [13] -->
获取更多资讯

<!-- b000327 | furniture | pages [14] -->
Team # 2401445

<!-- b000328 | furniture | pages [14] -->
Page 14 of 26

<!-- b000329 | caption | pages [14] -->
Table 3: The best hyperparameter combination by Grid Search

<!-- b000330 | prose | pages [14] -->
max depth min samples leaf 10 4 min samples split n estimators 10 300

<!-- b000331 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000332 | prose | pages [14] -->
Based on the results, our Random Forest model achieved an accuracy of 77.6%, and the most relevant factors in predicting ranked by their contribution are:

<!-- b000333 | prose | pages [14] -->
Indicator Explanation

<!-- b000334 | prose | pages [14] -->
Number of consecutive scores by player in a game Consistent_scores Total number of shots in this point Rally_count Distance run by player in this point Distance_run Whether player hits an "untouchable" ball in this point Winner Whether player scores an ace in this point Ace

<!-- b000335 | caption | pages [14] -->
Table 4: Important Indicators

<!-- b000336 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000337 | caption | pages [14] -->
Figure 8: The importance of indicators

<!-- b000338 | prose | pages [14] -->
As the table shows, consistent scores come first. A sequence of consecutive scores by a player generally indicates they are in a period of dominance. When this sequence is broken, it may reveal a vulnerability or a shift in the player’s performance, often coinciding with a momentum swing.

<!-- b000339 | prose | pages [14] -->
Then come the rally count and distance run. A high rally count implies that play- ers are evenly matched, and the conclusion of an intense rally could shift the momen- tum, especially if followed by a decisive play like a winner or an error. While a player who moves more may be under more pressure, and a sudden increase or decrease in movement can signal a change in match dynamics, potentially pointing to a momen- tum shift.

<!-- b000340 | prose | pages [14] -->
关注数学模型

<!-- b000341 | furniture | pages [14] -->
2

<!-- b000342 | furniture | pages [14] -->
MATHmodels

<!-- b000343 | furniture | pages [14] -->
获取更多资讯

<!-- b000344 | furniture | pages [15] -->
Team # 2401445

<!-- b000345 | furniture | pages [15] -->
Page 15 of 26

<!-- b000346 | prose | pages [15] -->
What come next are ’winner’ and ace. Executing a shot that the opponent cannot reach, or a ’winner,’ is a strong indicator of a player seizing the initiative. Addition- ally, serving an ace is a clear sign of dominance in a game. It not only earns a point without rally but also sends a strong message to the opponent. Aces can contribute to

<!-- b000347 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000348 | prose | pages [15] -->
a player’s momentum by boosting their confidence and affecting the mental state of the opponent.

<!-- b000349 | prose | pages [15] -->
6.3

<!-- b000350 | heading | pages [15] -->
Adjusting the Model based on HMM

<!-- b000351 | prose | pages [15] -->
It seems that the second task can be fully accomplished by the random forest model. However, the word ’different’ in the task given inspires us to think about the different reaction players had when they were in faced with different rivals. Therefore, we consider analyzing each player deeply and take their past score into consideration. And Hidden Markov Model (HMM) greatly meets our needs.

<!-- b000352 | prose | pages [15] -->
In HMM, we consider a system being in one of several hidden states and mak- ing transitions between these states. The system emits observable outputs, which are probabilistically determined by its current state. We define the emission probability

<!-- b000353 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000354 | prose | pages [15] -->
matrices B1 and B2 for two distinct states, ’P1 upper’ and ’P2 upper’, respectively. Each matrix element P(xi|pj upper) represents the probability of observing the out- come xi given the system is in state pj upper, as illustrated in the following diagram:

<!-- b000355 | caption | pages [15] -->
Figure 9: How HMM works in our context

<!-- b000356 | prose | pages [15] -->
The emission probability matrices for states ’P1 upper’ and ’P2 upper’ are given side by side for comparison:

<!-- b000357 | prose | pages [15] -->
关注数学模型

<!-- b000358 | furniture | pages [15] -->
2

<!-- b000359 | furniture | pages [15] -->
MATHmodels

<!-- b000360 | furniture | pages [15] -->
获取更多资讯

<!-- b000361 | furniture | pages [16] -->
Team # 2401445

<!-- b000362 | prose | pages [16] -->


<!-- b000363 | prose | pages [16] -->


<!-- b000364 | prose | pages [16] -->
P(x1|p1 upper) P(x2|p1 upper)

<!-- b000365 | prose | pages [16] -->


<!-- b000366 | prose | pages [16] -->


<!-- b000367 | prose | pages [16] -->
P(x3|p1 upper)

<!-- b000368 | prose | pages [16] -->
B1 =

<!-- b000369 | furniture | pages [16] -->
Page 16 of 26

<!-- b000370 | prose | pages [16] -->


<!-- b000371 | prose | pages [16] -->


<!-- b000372 | prose | pages [16] -->
P(x1|p2 upper) P(x2|p2 upper)

<!-- b000373 | prose | pages [16] -->


<!-- b000374 | prose | pages [16] -->


<!-- b000375 | prose | pages [16] -->
P(x3|p2 upper)

<!-- b000376 | prose | pages [16] -->
B2 =

<!-- b000377 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000378 | prose | pages [16] -->
... P(xn|p1 upper)

<!-- b000379 | prose | pages [16] -->
... P(xn|p2 upper)

<!-- b000380 | prose | pages [16] -->
The initial state distribution, where P1 and P2 are the prior probabilities for the states ’P1 upper’ and ’P2 upper’:

<!-- b000381 | prose | pages [16] -->
P1  P2 P1+P2 × 0.5 P1+P2 × 0.5, 0.5,

<!-- b000382 | prose | pages [16] -->
Π =

<!-- b000383 | prose | pages [16] -->
The matrices B1 and B2 can evolve into a third state ’Equal’ with its own emis- sion probability matrix B3. This transition is indicative of a system that reaches an equilibrium or a tie between the two states, with B3 defined as:

<!-- b000384 | prose | pages [16] -->


<!-- b000385 | prose | pages [16] -->


<!-- b000386 | prose | pages [16] -->
P(x1|equal)

<!-- b000387 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000388 | prose | pages [16] -->
P(x2|equal)

<!-- b000389 | prose | pages [16] -->


<!-- b000390 | prose | pages [16] -->


<!-- b000391 | prose | pages [16] -->
P(x3|equal)

<!-- b000392 | prose | pages [16] -->
B3 =

<!-- b000393 | prose | pages [16] -->
... P(xn|equal)

<!-- b000394 | prose | pages [16] -->
The transitions between ’P1 upper’, ’P2 upper’, and ’Equal’ states are governed by transition probabilities, which are not shown in the diagram but are essential compo- nents of the HMM. Together, these matrices and the transitions between them form the core of the HMM, allowing us to model the sequence of states and corresponding observations for a given process.

<!-- b000395 | prose | pages [16] -->
Given the strong temporal correlation within each match and that the contest is between two players, we have trained a separate HMM for each match prior to the quarterfinals. These models contain temporal information from the matches and per- sonal data about the two competing players.

<!-- b000396 | heading | pages [16] -->
The Final Piece of the Model: Situational Leverage

<!-- b000397 | prose | pages [16] -->
6.4

<!-- b000398 | prose | pages [16] -->
Next, to measure the importance of a scoring point in terms of winning a game, such as when an underdog player has a chance for a break point in the first game, we introduce Situational Leverage. This concept refers to the degree of change in a player’s probability of winning the match based on the outcome of the next point, as shown in the equation below:

<!-- b000399 | prose | pages [16] -->
SLi,j = P(pei,j|wi,t) −P(pei,j|oi,t) (9)

<!-- b000400 | prose | pages [16] -->
Here, P(pei,j|wi,t) denotes PE of player i in the game j, assuming he scores in the t-th point of the game. On the other hand, P(pei,j|oi,t) denotes the PE of player i at the t-th point in the game.

<!-- b000401 | prose | pages [16] -->
6.5

<!-- b000402 | heading | pages [16] -->
Results and Advices

<!-- b000403 | prose | pages [16] -->
For the final match prediction, we utilized all the previously trained models that included the finalists, players P1 and P2. Each model provided its prediction, and

<!-- b000404 | prose | pages [16] -->
关注数学模型

<!-- b000405 | furniture | pages [16] -->
2

<!-- b000406 | furniture | pages [16] -->
MATHmodels

<!-- b000407 | furniture | pages [16] -->
获取更多资讯

<!-- b000408 | furniture | pages [17] -->
Team # 2401445

<!-- b000409 | furniture | pages [17] -->
Page 17 of 26

<!-- b000410 | prose | pages [17] -->
ultimately, we applied a hard voting mechanism to aggregate these predictions, which is displayed as follows:

<!-- b000411 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000412 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000413 | caption | pages [17] -->
Figure 10: Turning Points Prediction for the Final

<!-- b000414 | prose | pages [17] -->
The curve in the graph represents the cumulative point difference between Alcaraz and Djokovic, while the solid dots are the turning points marked by our model. It can be noted that most of the turning points are not, as we would usually expect, at the bottoms or tops of the cumulative point difference, but rather at the position after the next point. This is because we believe that to judge whether a point is a turning point, the main consideration should be whether it is the beginning of a reversal in the momentum of offense and defense, and this requires confirmation that this move has indeed achieved a reversal in scoring. From this perspective, we consider the marking of turning points to be quite successful.

<!-- b000415 | prose | pages [17] -->
Additionally, compared to the originally labeled data, our model performances well on the final match, as shown in the table.

<!-- b000416 | caption | pages [17] -->
Table 5: Model Results

<!-- b000417 | prose | pages [17] -->
Status Precision

<!-- b000418 | prose | pages [17] -->
No swings 0.74 Player1 upper hand 0.81 Player2 upper hand 0.84

<!-- b000419 | prose | pages [17] -->
Recall F1-Score Support

<!-- b000420 | prose | pages [17] -->
0.77 0.76 142 0.88 0.84 82 0.74 0.79 110

<!-- b000421 | prose | pages [17] -->
In set 2, as illustrated, we observe a tense situation with densely distributed points, indicating frequent momentum shifts between the two players, which is consistent with common understanding. The turning point near 200 is also well-predicted.

<!-- b000422 | prose | pages [17] -->
关注数学模型

<!-- b000423 | furniture | pages [17] -->
2

<!-- b000424 | furniture | pages [17] -->
MATHmodels

<!-- b000425 | furniture | pages [17] -->
获取更多资讯

<!-- b000426 | furniture | pages [18] -->
Team # 2401445

<!-- b000427 | furniture | pages [18] -->
Page 18 of 26

<!-- b000428 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000429 | caption | pages [18] -->
Figure 11: When DPI meets turning points

<!-- b000430 | prose | pages [18] -->
In general, based on the indicators selected from random forest as well as the out- puts from HMM and leverages, we prepare 4 advices for coaches:

<!-- b000431 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000432 | prose | pages [18] -->
• Consistency and Dominance: You should instruct players to strive for consistent scoring as it is a hallmark of dominance. A series of uninterrupted points often signifies control over the match. You should prepare players to recognize when their scoring streak is broken as it may indicate a potential shift in momentum and possibly expose their vulnerabilities.

<!-- b000433 | prose | pages [18] -->
• Rally Count and Movement: You should encourage players to focus on rally counts and their on-court movement. An elevated rally count usually means well-matched play, and the end of a prolonged rally can be pivotal, leading to a momentum swing, particularly if it ends with a critical winner or an unforced error. You should advise players that increased movement might suggest defen- sive pressure.

<!-- b000434 | prose | pages [18] -->
• Aggressive Play and Service: You should emphasize the importance of execut- ing winners and aces. A winner not only captures the point but also asserts dominance, potentially initiating a momentum shift. Similarly, aces serve dual purposes by securing points effortlessly and exerting psychological pressure on the opponent.

<!-- b000435 | prose | pages [18] -->
• Study Your Rival: You should develop strategies based on each player’s re- sponse to momentum shifts, considering both personal tendencies and the op- ponent’s historical patterns. This includes a thorough pre-match analysis of past performances with respect to momentum changes.

<!-- b000436 | prose | pages [18] -->
7

<!-- b000437 | heading | pages [18] -->
Task 4: Model Generalization

<!-- b000438 | prose | pages [18] -->
To test the efficacy of our model in different matches, we selected three separate events for evaluation: the Wimbledon Men’s Singles, the Wimbledon Women’s Sin- gles, and the US Open (which has a different surface). Note that the data are extracted from the official site of Wimbledon tennis[5].

<!-- b000439 | prose | pages [18] -->
关注数学模型

<!-- b000440 | furniture | pages [18] -->
2

<!-- b000441 | furniture | pages [18] -->
MATHmodels

<!-- b000442 | furniture | pages [18] -->
获取更多资讯

<!-- b000443 | furniture | pages [19] -->
Team # 2401445

<!-- b000444 | furniture | pages [19] -->
Page 19 of 26

<!-- b000445 | prose | pages [19] -->
Tcted from he table below presetrants the performance of our model applied to three different tennis matches, detailing the f1 scores for three scenarios and the overall accuracy for point classification.

<!-- b000446 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000447 | prose | pages [19] -->
Match 0_f1_score 2023-wimbledon-2503 0.78 2023-wimbledon-1602 0.78 2023-usopen-1102 0.51 1_f1_score 2_f1_score Accuracy 0.82 0.90 0.83 0.88 0.90 0.85 0.61 0.65 0.58

<!-- b000448 | caption | pages [19] -->
Table 6: Report of Our Prediction

<!-- b000449 | heading | pages [19] -->
2023 Wimbledon Men’s Singles 1602: Jannik Sinner VS Novak

<!-- b000450 | prose | pages [19] -->
7.1 Djokovic

<!-- b000451 | prose | pages [19] -->
For the 2023 Wimbledon Championships Men’s Singles, we employed the same prediction method as used in the second query, namely the Hidden Markov Model

<!-- b000452 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000453 | prose | pages [19] -->
(HMM) for forecasting.

<!-- b000454 | caption | pages [19] -->
Figure 12: Turning Points Prediction:1602

<!-- b000455 | heading | pages [19] -->
2023 Wimbledon Women’s Singles 2503: Ons Jabeur VS Elena

<!-- b000456 | prose | pages [19] -->
7.2 Rybakina

<!-- b000457 | prose | pages [19] -->
However, for the Women’s Singles and the 2023 US Open Men’s Singles, we lacked a pre-trained HMM model. Consequently, we resorted to a combined approach of Random Forest and leverage forecasting for our predictions, the results of which are illustrated in the subsequent table.

<!-- b000458 | prose | pages [19] -->
关注数学模型

<!-- b000459 | furniture | pages [19] -->
2

<!-- b000460 | furniture | pages [19] -->
MATHmodels

<!-- b000461 | furniture | pages [19] -->
获取更多资讯

<!-- b000462 | furniture | pages [20] -->
Team # 2401445

<!-- b000463 | furniture | pages [20] -->
Page 20 of 26

<!-- b000464 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000465 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000466 | caption | pages [20] -->
Figure 13: Turning Points Prediction:2503

<!-- b000467 | heading | pages [20] -->
2020 US Open 1102: Alexandre Muller VS Arthur Rinderknech

<!-- b000468 | prose | pages [20] -->
7.3

<!-- b000469 | prose | pages [20] -->
Specifically, for the 2023 US Open Men’s Singles, our model did not achieve sat- isfactory results. We attribute this to a discrepancy between the floor material of the match venue and that of the matches in our training set.

<!-- b000470 | prose | pages [20] -->
In summary, to enhance the predictive accuracy of our model regarding the mo- mentum turning points in tennis matches, we should consider additional factors such as the court surface material and the altitude of the venue. These elements are poten- tial influencers of match momentum and player performance and merit inclusion in future model training considerations.

<!-- b000471 | prose | pages [20] -->
8

<!-- b000472 | heading | pages [20] -->
Sensitivity Analysis

<!-- b000473 | prose | pages [20] -->
Previous Task 4 tested the generalization ability of our model. In this section, we will examine the sensitivity of the model. For the key indicators given by the previous random forest model, we introduce significant Gaussian noise to "consistent scores" and "distance run," and then re-calculate the model’s recall metric. As shown in the figure, although there is a decrease in recall, the extent of the decrease is small, demon- strating the excellent robustness of our model.

<!-- b000474 | prose | pages [20] -->
9

<!-- b000475 | heading | pages [20] -->
Strength and Weakness

<!-- b000476 | prose | pages [20] -->
9.1

<!-- b000477 | heading | pages [20] -->
Strength

<!-- b000478 | heading | pages [20] -->
• Our model uniquely integrates multiple dimensions including athlete perfor-

<!-- b000479 | heading | pages [20] -->
mance, personal strength, and serving advantage, offering a comprehensive

<!-- b000480 | prose | pages [20] -->
evaluation of match dynamics.

<!-- b000481 | prose | pages [20] -->
关注数学模型

<!-- b000482 | furniture | pages [20] -->
2

<!-- b000483 | furniture | pages [20] -->
MATHmodels

<!-- b000484 | furniture | pages [20] -->
获取更多资讯

<!-- b000485 | furniture | pages [21] -->
Team # 2401445

<!-- b000486 | furniture | pages [21] -->
Page 21 of 26

<!-- b000487 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000488 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000489 | caption | pages [21] -->
Figure 14: Turning Points Prediction:1102

<!-- b000490 | caption | pages [21] -->
Figure 15: Recall before and after Gaussian noise is added

<!-- b000491 | prose | pages [21] -->
• We have comprehensively modelled the standard international rules of tennis to reflect the differences from the real game.

<!-- b000492 | prose | pages [21] -->
• Our model integrates the strengths of both Random Forest and HMM.

<!-- b000493 | prose | pages [21] -->
9.2

<!-- b000494 | heading | pages [21] -->
Weakness and Further Discussion

<!-- b000495 | prose | pages [21] -->
• The HMM model is overly reliant on historical data, including the performance of established players and match records, when predicting the outcome of tennis matches.

<!-- b000496 | prose | pages [21] -->
• The model performs poorly in generalising to other ball games. Our final se- lection of metrics using the Random Forest model remains closely related to the

<!-- b000497 | prose | pages [21] -->
关注数学模型

<!-- b000498 | furniture | pages [21] -->
2

<!-- b000499 | furniture | pages [21] -->
MATHmodels

<!-- b000500 | furniture | pages [21] -->
获取更多资讯

<!-- b000501 | furniture | pages [22] -->
Team # 2401445

<!-- b000502 | prose | pages [22] -->
specific metrics of tennis.

<!-- b000503 | heading | pages [22] -->
References

<!-- b000504 | furniture | pages [22] -->
Page 22 of 26

<!-- b000505 | references | pages [22] -->
微信公众号：数学模型

<!-- b000506 | references | pages [22] -->
[1] Dietl, Helmut, and Cornel Nesseler. "Momentum in tennis:

<!-- b000507 | references | pages [22] -->
Controlling the

<!-- b000508 | references | pages [22] -->
match." *UZH Business Working Paper Series* 365 (2017).

<!-- b000509 | references | pages [22] -->
[2] Seidl, R., Lucey, P. Live Counter-Factual Analysis in Women’s Tennis using Au-

<!-- b000510 | references | pages [22] -->
tomatic Key-Moment Detection.

<!-- b000511 | references | pages [22] -->
[3] Moss, Ben, and Peter O’Donoghue. "Momentum in US Open men’s singles ten-

<!-- b000512 | references | pages [22] -->
nis." *International Journal of Performance Analysis in Sport* 15.3 (2015): 884-896.

<!-- b000513 | references | pages [22] -->
[4] O’Donoghue, Peter, and Emily Brown. "Sequences of service points and the mis-

<!-- b000514 | references | pages [22] -->
perception of momentum in elite tennis." *International Journal of Performance

<!-- b000515 | references | pages [22] -->
Analysis in Sport* 9.1 (2009): 113-127.

<!-- b000516 | references | pages [22] -->
微信号：MATHmodels

<!-- b000517 | references | pages [22] -->
[5] "The Championships, Wimbledon." Accessed February 6, 2024. https://www.

<!-- b000518 | references | pages [22] -->
wimbledon.com/index.html.

<!-- b000519 | references | pages [22] -->
关注数学模型

<!-- b000520 | furniture | pages [22] -->
2

<!-- b000521 | furniture | pages [22] -->
MATHmodels

<!-- b000522 | furniture | pages [22] -->
获取更多资讯

<!-- b000523 | furniture | pages [23] -->
Team # 2401445

<!-- b000524 | furniture | pages [23] -->
Page 23 of 26

<!-- b000525 | heading | pages [23] -->
Memorandum for The Coaches

<!-- b000526 | prose | pages [23] -->
10

<!-- b000527 | prose | pages [23] -->
To: Coaches From: Team #2401445

<!-- b000528 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000529 | prose | pages [23] -->
Subject: Date: February 6, 2024

<!-- b000530 | prose | pages [23] -->
The phenomenon of momentum in tennis has long been debated, with the 2023 Wimbledon final serving as a testament to its potential impact. Our study delves into the intricacies of match flow, focusing on the dynamics that drive momentum swings and their predictable patterns.

<!-- b000531 | prose | pages [23] -->
We developed a Dynamic Play Index (DPI) by integrating data preprocessing tech- niques and advanced statistical models such as Gradient Boosting Trees and the Hid- den Markov Model. Our DPI synthesizes performance metrics, personal strengths, and serving advantages into a comprehensive measure of match flow, yielding in- sights with 82.4% accuracy.

<!-- b000532 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000533 | prose | pages [23] -->
Understanding and capitalizing on momentum is paramount in competitive ten- nis. Our data indicates that the following elements are critical in maintaining and exploiting momentum:

<!-- b000534 | prose | pages [23] -->
• Score Streaks: Teach players to focus on the next point to build and maintain dominance. Recognize and adjust quickly if the streak is broken to prevent mo- mentum shift.

<!-- b000535 | prose | pages [23] -->
• Endurance in Rallies: Use high rally counts as a measure of player stamina and competitive edge. Train players to stay mentally engaged and look for opportu- nities to conclude rallies with strategic plays.

<!-- b000536 | prose | pages [23] -->
• Decisive Shots: Encourage players to develop precision in aggressive shots, such as winners and aces, which can change the game’s tempo and put psy- chological pressure on the opponent.

<!-- b000537 | prose | pages [23] -->
• Opponent Analysis: Implement drills that mimic rivals’ play styles and weak- nesses, enabling players to adapt their strategies during actual match play.

<!-- b000538 | prose | pages [23] -->
In the ebb and flow of a tennis match, players will inevitably face moments that test their resolve and adaptability. Our study highlights several scenarios where prepara- tion can make a significant difference:

<!-- b000539 | prose | pages [23] -->
• Closing the Gap: Teach players to compartmentalize the score when down, fo- cusing solely on earning the next point. This laser focus can help in gradually diminishing the lead of the opponent.

<!-- b000540 | prose | pages [23] -->
• Shifting Back Momentum: Introduce drills where players lose points on pur- pose and then work to recover, teaching them to identify and counteract mo- mentum shifts.

<!-- b000541 | prose | pages [23] -->
• Pressure Points: Simulate break points and tiebreaks in practice sessions, en- couraging players to employ specific, practiced responses to these high-stakes moments.

<!-- b000542 | prose | pages [23] -->
关注数学模型

<!-- b000543 | furniture | pages [23] -->
2

<!-- b000544 | furniture | pages [23] -->
MATHmodels

<!-- b000545 | furniture | pages [23] -->
获取更多资讯

<!-- b000546 | furniture | pages [24] -->
Team # 2401445

<!-- b000547 | furniture | pages [24] -->
Page 24 of 26

<!-- b000548 | prose | pages [24] -->
• Break Point Strategies: Have players practice aggressive returns and pinpoint the opponent’s weak spots during simulated break opportunities to take charge of the game’s flow.

<!-- b000549 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000550 | prose | pages [24] -->
• Lead Protection: Use drills that start with the player in the lead, emphasizing the need to continue playing offensively to secure the win, rather than passively trying to maintain the lead.

<!-- b000551 | prose | pages [24] -->
Our predictive model is not only a tool for analysis but a cornerstone for building mental toughness and tactical agility in players. As a coach, your role transcends physical training. You are the architect of your players’ mental resilience, equipping them to maneuver through the psychological battles intrinsic to competitive tennis. The strategies we’ve detailed are crafted to embolden your players, enabling them to confront the challenges of match play with assured confidence and grace.

<!-- b000552 | prose | pages [24] -->
Transitioning from mental preparation to real-time match analysis, our model ex- cels by offering assessments of a player’s dynamic state as the game unfolds. This

<!-- b000553 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000554 | prose | pages [24] -->
granular insight into the flow of play is pivotal for making strategic decisions that har- ness the power of momentum swings. By leveraging this data, you can guide players to make intelligent, on-the-fly adjustments that can alter the course of a match.

<!-- b000555 | prose | pages [24] -->
It’s important to acknowledge, however, that our model, while comprehensive, is not without its limitations. One such area is the nuanced influence of different court surfaces on a player’s momentum — a variable that we aim to better understand and integrate into future iterations of the model. This presents an exciting opportunity for further enhancement, ensuring that our tool evolves in line with the complexities of the sport.

<!-- b000556 | prose | pages [24] -->
In conclusion, the integration of our model into your coaching methodology can be transformative. By translating our insights into practical training exercises, players can be adeptly prepared to exploit the ebb and flow of play, turning what was once an intangible concept into a quantifiable advantage. We are committed to continuous improvement, working alongside you to refine our system and support your efforts in forging champions on the court.

<!-- b000557 | prose | pages [24] -->
Warm regards,

<!-- b000558 | furniture | pages [24] -->
Team #2401445

<!-- b000559 | prose | pages [24] -->
关注数学模型

<!-- b000560 | furniture | pages [24] -->
2

<!-- b000561 | furniture | pages [24] -->
MATHmodels

<!-- b000562 | furniture | pages [24] -->
获取更多资讯

<!-- b000563 | furniture | pages [25] -->
Team # 2401445

<!-- b000564 | heading | pages [25] -->
Appendices

<!-- b000565 | furniture | pages [25] -->
Page 25 of 26

<!-- b000566 | prose | pages [25] -->
Indicators Chosen for Training Random For-

<!-- b000567 | heading | pages [25] -->
Appendix A

<!-- b000568 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000569 | heading | pages [25] -->
est Model

<!-- b000570 | prose | pages [25] -->
Metric (Feature) Explanation

<!-- b000571 | prose | pages [25] -->
Number of consecutive scores by player 1 in a game p1_consistent_scores Number of consecutive scores by player 2 in a game p2_consistent_scores Whether player 1 scores an ace in this point p1_ace Whether player 2 scores an ace in this point p2_ace Whether player 1 hits an "untouchable" ball in this point p1_winner Whether player 2 hits an "untouchable" ball in this point p2_winner Whether player 1 commits a double fault in this point p1_double_fault Whether player 2 commits a double fault in this point p2_double_fault

<!-- b000572 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000573 | prose | pages [25] -->
Whether player 1 breaks serve in this point p1_break_pt_won Whether player 2 breaks serve in this point p2_break_pt_won Player 1 misses the chance to win the game on player 2’s serve p1_break_pt_missed Player 2 misses the chance to win the game on player 1’s serve p2_break_pt_missed Distance run by player 1 in this point p1_distance_run Distance run by player 2 in this point p2_distance_run Total number of shots in this point rally_count

<!-- b000574 | caption | pages [25] -->
Table 7: Tennis Match Metrics

<!-- b000575 | prose | pages [25] -->
AI Report

<!-- b000576 | prose | pages [25] -->
Query 1: Momentum in Tennis Papers

<!-- b000577 | prose | pages [25] -->
Input: Could you please help me to find out if there are any relevant papers on momentum in tennis, thanks!

<!-- b000578 | prose | pages [25] -->
Output: It seems there was an issue retrieving the full text of the papers directly from the websites. However, based on the search results, there are several relevant pa- pers on momentum in tennis, covering aspects such as the psychological and strategic momentum, its effects on match control, and empirical analyses of professional tennis matches. Titles include:

<!-- b000579 | prose | pages [25] -->
• Momentum in tennis: Controlling the match

<!-- b000580 | prose | pages [25] -->
• Separating psychological momentum from strategic momentum: Evidence ...

<!-- b000581 | prose | pages [25] -->
• Set-level Strategic and Psychological Momentum in Best-of-three-set ...

<!-- b000582 | prose | pages [25] -->
• Strategic and Psychological Momentum in Professional Tennis

<!-- b000583 | prose | pages [25] -->
关注数学模型

<!-- b000584 | furniture | pages [25] -->
2

<!-- b000585 | furniture | pages [25] -->
MATHmodels

<!-- b000586 | furniture | pages [25] -->
获取更多资讯

<!-- b000587 | furniture | pages [26] -->
Team # 2401445

<!-- b000588 | prose | pages [26] -->
Query 2: Missing Values in Data

<!-- b000589 | furniture | pages [26] -->
Page 26 of 26

<!-- b000590 | prose | pages [26] -->
Input: Could you please help me to check the data for missing values, and if so, could you please give some proper suggestions to deal with the missing values,

<!-- b000591 | prose | pages [26] -->
微信公众号：数学模型

<!-- b000592 | prose | pages [26] -->
thanks!

<!-- b000593 | prose | pages [26] -->
Output: The dataset contains missing values in the following columns:

<!-- b000594 | prose | pages [26] -->
• speed_mph: 752 missing values

<!-- b000595 | prose | pages [26] -->
• serve_width: 54 missing values

<!-- b000596 | prose | pages [26] -->
• serve_depth: 54 missing values

<!-- b000597 | prose | pages [26] -->
• return_depth: 1309 missing values

<!-- b000598 | prose | pages [26] -->
To deal with these missing values, consider the following strategies:

<!-- b000599 | prose | pages [26] -->
微信号：MATHmodels

<!-- b000600 | prose | pages [26] -->
1. Imputation for numerical and categorical columns.

<!-- b000601 | prose | pages [26] -->
2. Deletion of rows or columns with missing values.

<!-- b000602 | prose | pages [26] -->
3. Model-Based Methods for predicting missing values.

<!-- b000603 | prose | pages [26] -->
4. Use a Flag for Missing Values to indicate missing data.

<!-- b000604 | prose | pages [26] -->
Query 3: Tennis Player Ability Evaluation Index

<!-- b000605 | prose | pages [26] -->
Input: Could you please help me to find information and papers related to the tennis player ability evaluation index, I would like to know if there is an index to quantify it, thank you.

<!-- b000606 | prose | pages [26] -->
Output: Relevant resources include:

<!-- b000607 | prose | pages [26] -->
1. Construction of Evaluation Model of Tennis Skills and Tactic Level and Applica- tion of Grey Relational Algorithm.

<!-- b000608 | prose | pages [26] -->
2. Tennis Players Comprehensive Ability Evaluation using a fuzzy comprehensive evaluation model.

<!-- b000609 | prose | pages [26] -->
3. Optimization Analysis of Tennis Players’ Physical Fitness Index Based on Data Mining and Mobile Computing with the XGBoost algorithm.

<!-- b000610 | prose | pages [26] -->
These studies focus on developing comprehensive models for evaluating tennis play- ers’ abilities across various factors.

<!-- b000611 | prose | pages [26] -->
关注数学模型

<!-- b000612 | furniture | pages [26] -->
2

<!-- b000613 | furniture | pages [26] -->
MATHmodels

<!-- b000614 | furniture | pages [26] -->
获取更多资讯
