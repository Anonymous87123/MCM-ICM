# P-C-2024-2401445-6a882749

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
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
First, after data preprocessing, we introduce the Dynamic Play Index (DPI) to measure match flow. We quantify DPI using a linear combination of performance(PE), personal strength(PS), and serving advantage(SA). Specifically, we quantify PE with probabilities from Gradient Boosting Trees based on Grid Search (GBDT), summa- rize PS with a six-dimensional evaluation index, and represent SA with a binary vari-

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
able. Thus, We yield GBDT’s optimal parameters: [learning rate: 0.2, max depth: 5, n estimators: 300], and achieve an accuracy of 82.4%. Consequently, we calculate the DPI at each match moment as DPI = 0.28 × PE + 0.32 × PS + 0.4 × SA. Employ- ing this methodology, we effectively delineate the match flow for the 2023 Wimbledon encounter, match ID "2023-wimbledon-1701".

<!-- b000015 | prose | pages [1] -->
Then, to prove the existence of momentum, we employ a proof by contradiction, initially assuming that momentum does not exist. We combine Gaussian distribu- tions with PS and SA from Task 1. Using these, we simulate scores for 7 matches, from quarter-finals to the final. We compare these simulated scores to actual scores using the Dynamic Time Warping (DTW) algorithm. We find that Model 1’s score predictions, implying the presence of momentum, align more closely with actual data, showing a similarity closer to 50% than those of simulations assuming no momentum.

<!-- b000016 | prose | pages [1] -->
After that, we develop a turning point prediction model using Random Forest Classification and the Hidden Markov Model (HMM). First, we define the momen- tum based on the performance difference from Model I. Using Random Forest, we predict momentum shift with a 77.6% accuracy rate. Moreover, the model identifies the five most critical indicators for momentum shifts, with the player’s consecutive points being the most significant. Next, we employ HMM to explain how different players react to momentum changes and offer four suggestions targeting momentum.

<!-- b000017 | prose | pages [1] -->
Next, we apply Model II to the men’s singles match "wimbledon-1602", the women’s singles "wimbledon-2503", and the acrylic surface match "usopen-1102". The model performs slightly better in the first two cases but poorly in the last. Considering re- call rates, we suggest incorporating factors like court surface material to refine the model. Additionally, we introduce Gaussian noise to the significant indicators to test sensitivity. The model’s accuracy falls 8%, demonstrating robustness.

<!-- b000018 | prose | pages [1] -->
Finally, we discuss the strengths and weaknesses of our model and report the find- ings in a memo to the coaches.

<!-- b000019 | keywords | pages [1] -->
Keywords: Dynamic Play Index; Dynamic Time Warping; Random Forest; Hidden

<!-- b000020 | prose | pages [1] -->
Markov Model.

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
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000032 | contents | pages [2] -->
1.2

<!-- b000033 | contents | pages [2] -->
Restatement of the Problem

<!-- b000034 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
3

<!-- b000036 | contents | pages [2] -->
1.3

<!-- b000037 | contents | pages [2] -->
Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
4

<!-- b000039 | contents | pages [2] -->
2 Assumption

<!-- b000040 | contents | pages [2] -->
4

<!-- b000041 | contents | pages [2] -->
3 Notations

<!-- b000042 | contents | pages [2] -->
5

<!-- b000043 | contents | pages [2] -->
4 Model I: Measuring the flow of the match by DPI

<!-- b000044 | contents | pages [2] -->
6

<!-- b000045 | contents | pages [2] -->
4.1

<!-- b000046 | contents | pages [2] -->
Model Establishment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
6

<!-- b000048 | contents | pages [2] -->
4.1.1

<!-- b000049 | contents | pages [2] -->
Data preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
6

<!-- b000051 | contents | pages [2] -->
4.1.2

<!-- b000052 | contents | pages [2] -->
Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
7

<!-- b000054 | contents | pages [2] -->
4.1.3

<!-- b000055 | contents | pages [2] -->
Personal Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
9

<!-- b000057 | contents | pages [2] -->
4.1.4

<!-- b000058 | contents | pages [2] -->
Serving Advantage . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
9

<!-- b000060 | contents | pages [2] -->
4.2

<!-- b000061 | contents | pages [2] -->
Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
9

<!-- b000063 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000064 | contents | pages [2] -->
5 Task 2: Proving the Existence of Momentum

<!-- b000065 | contents | pages [2] -->
10

<!-- b000066 | contents | pages [2] -->
5.1

<!-- b000067 | contents | pages [2] -->
Simulating the Game Process

<!-- b000068 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
11

<!-- b000070 | contents | pages [2] -->
5.2

<!-- b000071 | contents | pages [2] -->
Quantifying the similarity . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
11

<!-- b000073 | contents | pages [2] -->
5.3

<!-- b000074 | contents | pages [2] -->
Assessing the similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
12

<!-- b000076 | contents | pages [2] -->
6 Model II: Momentum Turning Point Identification and Prediction Model

<!-- b000077 | contents | pages [2] -->
based on HMM-Random Forest

<!-- b000078 | contents | pages [2] -->
13

<!-- b000079 | contents | pages [2] -->
6.1

<!-- b000080 | contents | pages [2] -->
Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
13

<!-- b000082 | contents | pages [2] -->
6.1.1

<!-- b000083 | contents | pages [2] -->
Momentum

<!-- b000084 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [2] -->
13

<!-- b000086 | contents | pages [2] -->
6.1.2

<!-- b000087 | contents | pages [2] -->
Swing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
13

<!-- b000089 | contents | pages [2] -->
6.1.3

<!-- b000090 | contents | pages [2] -->
Turning Point . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
13

<!-- b000092 | contents | pages [2] -->
6.2

<!-- b000093 | contents | pages [2] -->
Figuring Out the Main indicators . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
13

<!-- b000095 | contents | pages [2] -->
6.3

<!-- b000096 | contents | pages [2] -->
Adjusting the Model based on HMM . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
15

<!-- b000098 | contents | pages [2] -->
6.4

<!-- b000099 | contents | pages [2] -->
The Final Piece of the Model: Situational Leverage . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
16

<!-- b000101 | contents | pages [2] -->
6.5

<!-- b000102 | contents | pages [2] -->
Results and Advices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
16

<!-- b000104 | contents | pages [2] -->
7 Task 4: Model Generalization

<!-- b000105 | contents | pages [2] -->
18

<!-- b000106 | contents | pages [2] -->
2023 Wimbledon Men’s Singles 1602: Jannik Sinner VS Novak Djokovic . .

<!-- b000107 | contents | pages [2] -->
7.1

<!-- b000108 | contents | pages [2] -->
19

<!-- b000109 | contents | pages [2] -->
2023 Wimbledon Women’s Singles 2503: Ons Jabeur VS Elena Rybakina . .

<!-- b000110 | contents | pages [2] -->
7.2

<!-- b000111 | contents | pages [2] -->
19

<!-- b000112 | contents | pages [2] -->
2020 US Open 1102: Alexandre Muller VS Arthur Rinderknech . . . . . . . .

<!-- b000113 | contents | pages [2] -->
7.3

<!-- b000114 | contents | pages [2] -->
20

<!-- b000115 | contents | pages [2] -->
8 Sensitivity Analysis

<!-- b000116 | contents | pages [2] -->
20

<!-- b000117 | contents | pages [2] -->
9 Strength and Weakness

<!-- b000118 | contents | pages [2] -->
20

<!-- b000119 | contents | pages [2] -->
9.1

<!-- b000120 | contents | pages [2] -->
Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [2] -->
20

<!-- b000122 | contents | pages [2] -->
9.2

<!-- b000123 | contents | pages [2] -->
Weakness and Further Discussion . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000124 | contents | pages [2] -->
21

<!-- b000125 | contents | pages [2] -->
Reference

<!-- b000126 | contents | pages [2] -->
22

<!-- b000127 | contents | pages [2] -->
10 Memorandum for The Coaches

<!-- b000128 | contents | pages [2] -->
23

<!-- b000129 | contents | pages [2] -->
Appendices

<!-- b000130 | contents | pages [2] -->
25

<!-- b000131 | contents | pages [2] -->
Appendix A Indicators Chosen for Training Random Forest Model

<!-- b000132 | contents | pages [2] -->
25

<!-- b000133 | contents | pages [2] -->
关注数学模型

<!-- b000134 | furniture | pages [2] -->
2

<!-- b000135 | furniture | pages [2] -->
MATHmodels

<!-- b000136 | furniture | pages [2] -->
获取更多资讯

<!-- b000137 | furniture | pages [3] -->
Team # 2401445

<!-- b000138 | furniture | pages [3] -->
Page 3 of 26

<!-- b000139 | heading | pages [3] -->
1 Introduction

<!-- b000140 | heading | pages [3] -->
1.1 Problem Background

<!-- b000141 | prose | pages [3] -->
In sports, "momentum" is seen as a dual-edged sword, capable of propelling ath- 微信公众号：数学模型 letes towards victory or serving as a pivotal factor in turning the tide of defeat. It’s widely regarded as a crucial determinant of success. However, the real impact of mo- mentum in tennis sparks a heated debate.

<!-- b000142 | prose | pages [3] -->
Some research supports its significant psychological and physiological impacts on players, influencing match outcomes. For example, Dietl, Helmut, and Cornel Nes- seler (2017) found that players have a 54.2% chance of winning the last set after win- ning the penultimate set. Furthermore, Seidl, Robert, and Patrick Lucey (2022) intro- duced a counter-factual method for women’s tennis, automatically highlighting key match moments with "leverage," "clutch," and "momentum" metrics.

<!-- b000143 | prose | pages [3] -->
Conversely, other research disputes the impact of momentum, suggesting it may be a psychological illusion rather than a statistically significant factor. For instance, 微信号：MATHmodels analysis from the US Open men’s singles and studies on service point sequences in elite tennis failed to find statistical evidence supporting momentum’s influence on match outcomes[3]. Moreover, studies from O’Donoghue, Peter, and Emily Brown propose that the perceived momentum effect might not significantly alter the course of a match, indicating that outcomes could be influenced more by skill and chance than by a momentum-driven psychological advantage[4].

<!-- b000144 | caption | pages [3] -->
Figure 1: The battle between two parties

<!-- b000145 | prose | pages [3] -->
Therefore, understanding and quantifying momentum’s role is essential for devel- oping adaptive strategies in tennis, providing critical insights for players and coaches to navigate the game’s dynamic challenges.

<!-- b000146 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000147 | prose | pages [3] -->
The challenge at hand involves the analysis of data from the Wimbledon 2023 men’s tennis matches with the objective of gaining insights into the concept of "mo- mentum." The primary tasks to be addressed include:

<!-- b000148 | prose | pages [3] -->
• Measuring the flow of match: Construct a model that illustrates the progression

<!-- b000149 | prose | pages [3, 4] -->
关注数学模型 of gameplay, enabling the identification of the dominant player at any given mo- ment and quantifying their performance advantage. This should also involve the creation of visual representations of the match flow.

<!-- b000150 | furniture | pages [3] -->
2

<!-- b000151 | furniture | pages [3] -->
MATHmodels

<!-- b000152 | furniture | pages [3] -->
获取更多资讯

<!-- b000153 | furniture | pages [4] -->
Team # 2401445

<!-- b000154 | furniture | pages [4] -->
Page 4 of 26

<!-- b000156 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000157 | prose | pages [4] -->
• Momentum existence evaluation: Evaluate the assertion that swings in match play and sequences of success are random events, unaffected by the influence of momentum.

<!-- b000158 | prose | pages [4] -->
• Turning point prediction: Develop a system for forecasting instances when the balance of play is likely to shift between players. This should encompass the identification of contributing factors to such changes, along with recommenda- tions for players based on historical patterns of momentum swings.

<!-- b000159 | prose | pages [4] -->
• Model testing and generalization: Apply the developed model to additional matches in order to assess its predictive accuracy and investigate its applica- bility in various contexts, including matches on different playing surfaces and potentially in other sports.

<!-- b000160 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000161 | prose | pages [4] -->
• Reporting: Produce a comprehensive report that consolidates the findings of the analysis and offers coaching advice regarding the role of momentum and strategies for managing shifts in the flow of play during matches.

<!-- b000162 | heading | pages [4] -->
1.3 Our work

<!-- b000163 | caption | pages [4] -->
Figure 2: Our work

<!-- b000164 | heading | pages [4] -->
2 Assumption

<!-- b000165 | heading | pages [4] -->
Assumption 1: We assume a player’s individual ability remains constant during

<!-- b000166 | prose | pages [4] -->
a match because a player’s skill level, physical condition, strategy, and mental state are considered fixed throughout the game. This means any variation in match per- formance is attributed to external factors or the opponent’s play, rather than changes in the player’s inherent capability. This assumption simplifies analysis by focusing on match dynamics without accounting for fluctuating player conditions or strategies within the game.

<!-- b000167 | prose | pages [4, 5] -->
关注数学模型 Assumption 2: We assume that a player’s ability value can be inferred from existing match data. This is because the data contains detailed records of perfor- mances, outcomes, and statistics that, when analyzed, reveal patterns and indicators of a player’s skill level. By quantifying these elements, we aim to establish a reliable 微信公众号：数学模型 measure of individual abilities that can inform further analyses and predictions.

<!-- b000168 | furniture | pages [4] -->
2

<!-- b000169 | furniture | pages [4] -->
MATHmodels

<!-- b000170 | furniture | pages [4] -->
获取更多资讯

<!-- b000171 | furniture | pages [5] -->
Team # 2401445

<!-- b000172 | furniture | pages [5] -->
Page 5 of 26

<!-- b000174 | prose | pages [5] -->
Assumption 3: We assume that the player with the serve has an advantage. Be- cause serving initiates play and allows the server to control the game’s pace and style from the outset, historical data and professional observations consistently show that players serving have a higher probability of winning the game. This assumption is foundational for analyzing match dynamics and strategies, considering the serve’s critical role in tennis.

<!-- b000175 | heading | pages [5] -->
3 Notations

<!-- b000176 | caption | pages [5] -->
Table 1: Summary of Key Symbols and Their Descriptions

<!-- b000177 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000178 | heading | pages [5] -->
Symbol

<!-- b000179 | prose | pages [5] -->
Description PE Performance PS Personal Strength SA Serving Advantage M Number of Models Tm Decision Tree Obtained from the mth Training PWOL Percentage of Matches in which the Winner Outscored the Loser D Distance Between Two Sequences Q, A, O, B, Π The Parameters of HMM SL Situational Leverage playeri lose the tth point oi,t playeri win the tth point wi,t

<!-- b000180 | prose | pages [5] -->
关注数学模型

<!-- b000181 | furniture | pages [5] -->
2

<!-- b000182 | furniture | pages [5] -->
MATHmodels

<!-- b000183 | furniture | pages [5] -->
获取更多资讯

<!-- b000184 | furniture | pages [6] -->
Team # 2401445

<!-- b000185 | furniture | pages [6] -->
Page 6 of 26

<!-- b000186 | heading | pages [6] -->
4 Model I: Measuring the flow of the match by DPI

<!-- b000187 | prose | pages [6] -->
Inspired by the concept of dynamic win probabilities seen in chess, we develop the Dynamic Play Index (DPI) to seek the dynamic flow of tennis. This index dynamically 微信公众号：数学模型 reflects a player’s performance and likelihood of winning a game, adjusting in real- time with each scored point.

<!-- b000188 | prose | pages [6] -->
We construct the DPI by considering three primary factors: Performance (PE), Per- sonal Strength (PS), and Serving Advantage (SA). The model is represented by the equation DPI = α × PE + β × PS + γ × SA, (1)

<!-- b000189 | prose | pages [6] -->
where α, β, and γ denote the weights for each factor. We aim to keep our model straightforward, employing a linear approach to effectively capture the complex dy- namics of a tennis match, thus enabling us to quantify and visualize the ebb and flow of play and the relative performance of the players throughout a match.

<!-- b000190 | heading | pages [6] -->
4.1 Model Establishment

<!-- b000191 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000192 | heading | pages [6] -->
4.1.1 Data preprocessing

<!-- b000193 | prose | pages [6] -->
Upon reviewing the data, we identified missing values primarily in four columns: speed_mph, serve_width, serve_depth, and return_depth. The number of missing values in each column is as shown in the figure. We observed the most significant data gaps in matches 2023-wimbledon-1310 and 2023-wimbledon-1311. In these matches, a large portion of speed_mph data was missing, along with anomalies in rally_count (predominantly zeros). The serve speeds for players Guido Pella and Mikael Ymer were absent.

<!-- b000194 | caption | pages [6] -->
Figure 3: Missing Value Distribution Plot

<!-- b000195 | prose | pages [6] -->
When conducting our analysis on performance, we opted to impute the missing values for speed_mph and rally_count using median values. This approach helps to mitigate the impact of outliers and maintains consistency in the data.

<!-- b000196 | prose | pages [6] -->
For the analysis of personal strength, we decided to remove all performance in- dicators for both players entirely. This decision ensures the accuracy of our analysis

<!-- b000197 | prose | pages [6, 7] -->
关注数学模型 and prevents misleading statistical inferences. By adopting these methods, we aim to provide a reliable and fair assessment of players’ capabilities, taking into account the available data.

<!-- b000198 | furniture | pages [6] -->
2

<!-- b000199 | furniture | pages [6] -->
MATHmodels

<!-- b000200 | furniture | pages [6] -->
获取更多资讯

<!-- b000201 | furniture | pages [7] -->
Team # 2401445

<!-- b000202 | furniture | pages [7] -->
Page 7 of 26

<!-- b000204 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000205 | heading | pages [7] -->
4.1.2 Performance

<!-- b000206 | prose | pages [7] -->
To assess a player based on the current situation of the game, we establish a met- ric known as "performance". It’s important to note that this evaluation is distinct from considerations of Personal Strength or external factors. To measure a player’s perfor- mance, we focus on measuring the impact of their actions on the likelihood of winning the current game.

<!-- b000207 | prose | pages [7] -->
Therefore, we define performance as the chance of a player winning a game, pre- dicted by analyzing various situational factors: p1_sets, p2_sets, p1_games, p2_games, p1_current_point, p2_current_point, server, through a Gradient Boosting Trees clas- sification model.

<!-- b000208 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000209 | caption | pages [7] -->
Figure 4: Gradient Boosting Tree + Grid Search Diagram

<!-- b000210 | prose | pages [7] -->
In our analysis, the principle of the Gradient Boosting Trees (GBT) classification model is central to quantifying player performance. As we can see on the graph above, this model is an ensemble of decision trees, formulated as an additive model where each tree incrementally improves the model’s accuracy. The fundamental expression for a boosting tree model is represented as:

<!-- b000211 | prose | pages [7] -->
M X F(x) = Tm(x; Θm) (2) m=1

<!-- b000212 | prose | pages [7] -->
where F(x) denotes the final model, Tm(x; Θm) represents the mth decision tree pa- rameterized by Θm, and M is the total number of trees.

<!-- b000213 | prose | pages [7] -->
The GBT algorithm updates the model iteratively, allowing each subsequent tree to correct the residuals of the predictions from all previous trees. At step m, the model is updated as follows:

<!-- b000214 | prose | pages [7] -->
Fm(x) = Fm−1(x) + αTm(x; Θm) (3)

<!-- b000215 | prose | pages [7, 8] -->
关注数学模型 where α is the learning rate controlling the contribution of each tree. This sequential correction aims to minimize a loss function, L, which for a binary classification prob- lem, often employs the exponential loss function to effectively differentiate between the two classes: 微信公众号：数学模型 L(y, y′) = exp(−yy′) (4)

<!-- b000216 | furniture | pages [7] -->
2

<!-- b000217 | furniture | pages [7] -->
MATHmodels

<!-- b000218 | furniture | pages [7] -->
获取更多资讯

<!-- b000219 | furniture | pages [8] -->
Team # 2401445

<!-- b000220 | furniture | pages [8] -->
Page 8 of 26

<!-- b000222 | prose | pages [8] -->
Building on the fou ndational principles of the Gradient Boosting Trees model, we actively employ grid search to optimize its hyperparameters. This approach system- atically explores a spectrum of parameter values to identify the set that minimizes the prediction error. By evaluating the model’s performance across all possible combina- tions of predefined hyperparameters, we ensure the refinement and accuracy of our predictions:

<!-- b000223 | prose | pages [8] -->
Grid Search = min Θ L(F(x; Θ), y) (5)

<!-- b000224 | prose | pages [8] -->
Adapting the Gradient Boosting Trees model to our analysis, it’s noteworthy that although the GBT algorithm fundamentally outputs binary classification results—indicating 微信号：MATHmodels win or loss for each game — we utilize the probability estimated by the classifier for a win as the value of "performance". This method transforms binary win-loss out- comes into a continuous measure of win probability.

<!-- b000225 | prose | pages [8] -->
Gradient Boosting Trees stand out in this tennis analysis for their precision. This method significantly enhances our capability to predict tennis match results, achieving a prediction accuracy of 82.4% for the final match based on earlier data, thus validating the effectiveness of our performance model.

<!-- b000226 | caption | pages [8] -->
Figure 5: Performance for Alcaraz as Points Occur

<!-- b000227 | prose | pages [8] -->
The graph we present illustrates the performance of Carlos Alcaraz during the final match. In this graph, the x-axis represents the cumulative score between the competi- tors, while the y-axis indicates his performance. Notably, points where performance exceeds 0.5 are highlighted in bold. This visualization distinctly highlights that, based solely on the scoring dynamics within the match, Alcaraz often found himself in a po- sition of advantage. It’s important to note that this metric focuses exclusively on the current score situation, without factoring in individual strengths, serving turns, or other external elements.

<!-- b000228 | prose | pages [8] -->
关注数学模型

<!-- b000229 | furniture | pages [8] -->
2

<!-- b000230 | furniture | pages [8] -->
MATHmodels

<!-- b000231 | furniture | pages [8] -->
获取更多资讯

<!-- b000232 | furniture | pages [9] -->
Team # 2401445

<!-- b000233 | furniture | pages [9] -->
Page 9 of 26

<!-- b000234 | heading | pages [9] -->
4.1.3 Personal Strength

<!-- b000235 | prose | pages [9] -->
In our initial analysis, we focused solely on situational factors. Now, we expand our perspective to include individual player capabilities. Drawing on the research 微信公众号：数学模型 by Fitzpatrick et al. (2019), we utilize the PWOL (Percentage of matches in which the Winner Outscored the Loser) method to identify six key indicators of elite tennis players, summarized as the table below.

<!-- b000236 | caption | pages [9] -->
Table 2: Summary of Personal Strength

<!-- b000237 | prose | pages [9] -->
Characteristic Equation PWOL

<!-- b000238 | prose | pages [9] -->
1st serve-return wins/1st serve-returns × 100 1st Serve-Return Win % 80.2% Break points won/Break points played × 100 Break Points Won % 68.3% Points won 0–4 rally/Points played 0–4 rally × 100 0-4 Rally Win % 66.1% Avg. 1st Serve Speed Mean 1st serve speed 54.7% Aces/Serves × 100 Aces % 52.7% Double faults/Points served × 100 Double Faults % 47.6% 微信号：MATHmodels Untouchable Rate % based on p1_winner 33.4%

<!-- b000239 | prose | pages [9] -->
As to the calculation of Overall Individual Capability, we initially map the actual values of the indicators to a 60-100 scale in order to standardize the range of values. Subsequently, we apply a weighted average calculation based on the PWOL values to derive the player’s composite score. This process is encapsulated in the following formula: Pn i=1 IndexScorei × PWOLi PS = (6) Pn i=1 PWOLi where PS is the player’s overall strength score, calculated as a weighted average based on key indicators; IndexScorei is the normalized score for the ith indicator, adjusted to a 60-100 scale; PWOLi denotes the weight of the ith indicator, reflecting its importance according to the "Percentage of matches in which the Winner Outscored the Loser".

<!-- b000240 | heading | pages [9] -->
4.1.4 Serving Advantage

<!-- b000241 | prose | pages [9] -->
We also acknowledge the importance of service in tennis, as studies have shown that players often win more points while serving than receiving (Furlong, 1995; O’ Donoghue and Ballantyne, 2004). Therefore, we identify the serving advantage as a key feature in our model. We define this advantage using a binary variable:

<!-- b000242 | prose | pages [9] -->
( 1 if player i is serving, SA = (7) 0 otherwise.

<!-- b000243 | heading | pages [9] -->
4.2 Model Evaluation

<!-- b000244 | prose | pages [9] -->
Through the examination of relevant literature and parameter tuning practices, we have ultimately determined the weights for three indicators as follows:

<!-- b000245 | prose | pages [9] -->
α = 0.28, β = 0.32, γ = 0.4

<!-- b000246 | prose | pages [9, 10] -->
关注数学模型 微信公众号：数学模型

<!-- b000247 | furniture | pages [9] -->
2

<!-- b000248 | furniture | pages [9] -->
MATHmodels

<!-- b000249 | furniture | pages [9] -->
获取更多资讯

<!-- b000250 | furniture | pages [10] -->
Team # 2401445

<!-- b000251 | furniture | pages [10] -->
Page 10 of 26

<!-- b000253 | caption | pages [10] -->
Figure 6: DPI plot of the final

<!-- b000254 | prose | pages [10] -->
Consequently, we have plotted the Dynamic Performance Index (DPI) over the scoring sequence of the final match, as illustrated below. 微信号：MATHmodels Dividing the total of 334 scoring records of the final match into five segments, each representing a set of the game, and based on the description of the match dynamics, we evaluate whether our model accurately reflects which player is performing better at any given time during the match, as well as the extent of their performance advantage.

<!-- b000255 | prose | pages [10] -->
• In the first set, Djokovic seemed destined to win easily as he dominated 6 – 1. The DPI curve from points 0 to 45 shows Djokovic’s DPI, despite fluctuations, was significantly ahead of Alcaraz.

<!-- b000256 | prose | pages [10] -->
• The second set was tense and finally won by Alcaraz in a tie-breaker 7 – 6. The curve section from points 46 to 139 shows the DPI of both players fluctuating and in- terchanging frequently towards the end, reflecting the intensity of the situation.

<!-- b000257 | prose | pages [10] -->
• The third set was a reversal of the first, with Alcaraz winning comfortably 6 – 1. From points 140 to 209, the curve shows that, after some initial intersections, the young Spaniard’s DPI significantly leads over Djokovic, mirroring the actual scoreline.

<!-- b000258 | prose | pages [10] -->
• In the final two sets, our model showcased its superiority. In the fourth set, the young Spaniard seemed in total control as the set started, but Djokovic took complete control to win the set 6 – 3. This is reflected in our model by the orange curve overcoming the blue.

<!-- b000259 | prose | pages [10] -->
• Carrying the edge from the fourth set, Djokovic seemed poised to maintain the lead, but a shift occurred, and Alcaraz gained control, winning 6 – 4. In our model, the blue curve overtakes the orange in the midsection, eventually surpassing Djokovic’s representation.

<!-- b000260 | heading | pages [10] -->
5 Task 2: Proving the Existence of Momentum

<!-- b000261 | prose | pages [10] -->
For task 2, our approach involves employing a method of contradiction by assum- ing that momentum does not exist in tennis matches. If the conclusions drawn from this assumption significantly diverge from actual data, it would indicate the fallacy of the hypothesis.

<!-- b000262 | prose | pages [10] -->
关注数学模型

<!-- b000263 | furniture | pages [10] -->
2

<!-- b000264 | furniture | pages [10] -->
MATHmodels

<!-- b000265 | furniture | pages [10] -->
获取更多资讯

<!-- b000266 | furniture | pages [11] -->
Team # 2401445

<!-- b000267 | furniture | pages [11] -->
Page 11 of 26

<!-- b000268 | heading | pages [11] -->
5.1 Simulating the Game Process

<!-- b000269 | prose | pages [11] -->
To test the idea that momentum doesn’t affect match outcomes, we simulate games without considering momentum. Our simulation uses Gaussian noise, player strength, 微信公众号：数学模型 and serving advantagewhich come from the model I, as the only inputs. We treat changes in the game and scoring as completely random. This way, we follow tennis rules but ignore momentum, seeing if match results look different from real ones. The pseudocode for this simulation is shown below:

<!-- b000270 | heading | pages [11] -->
Algorithm 1 Enhanced Simulation of Tennis Matches with Mathematical Notation

<!-- b000271 | prose | pages [11] -->
for i = 1 to 100 do setsA, setsB ←0, 0 while (setsA < 3andsetsB < 3)and(setsA + setsB < 5) do gamesA, gamesB ←0, 0 repeat outcome ←SimulateOutcome(strengthA, strengthB, advantage) gamesA, gamesB ←UpdateGames(gamesA, gamesB, outcome) 微信号：MATHmodels if CheckSetWin(gamesA, gamesB) then setsA, setsB ←UpdateSets(setsA, setsB, outcome) break end if until set is decided end while Output(setsA, setsB) end for

<!-- b000272 | heading | pages [11] -->
5.2 Quantifying the similarity

<!-- b000273 | prose | pages [11] -->
In our analysis, we specifically compare sequences of score differences at each point update between two simulations: one that might includes momentum effects and an- other that assumes outcomes are entirely random. By doing so, we transform the prob- lem of comparing two match’s results into the problem of calculating the similarity of two sequences.

<!-- b000274 | prose | pages [11] -->
However, the length of those two sequences might not be the same, since simu- lations will not repeat themselves every time. Therefore, we apply Dynamic time warping (DTW) algorithm to calculate the similarity between two unequal-length sequences.

<!-- b000275 | prose | pages [11] -->
Dynamic Time Warping (DTW) is a renowned technique for analyzing time series, therefore offering a robust solution for comparing sequences that may vary in length or speed.

<!-- b000276 | prose | pages [11] -->
The mathematical foundation of DTW involves constructing a distance matrix D where each element D[i, j] represents the distance between the ith element of the first sequence and the jth element of the second sequence. The DTW algorithm then finds the path through this matrix that minimizes the total distance, which can be formally described as follows:

<!-- b000277 | prose | pages [11] -->
D[i, j] = distance(i, j) + min{D[i −1, j], D[i, j −1], D[i −1, j −1]}

<!-- b000278 | prose | pages [11, 12] -->
关注数学模型 where distance(i, j) calculates the distance between the two points from the sequences being compared.

<!-- b000279 | furniture | pages [11] -->
2

<!-- b000280 | furniture | pages [11] -->
MATHmodels

<!-- b000281 | furniture | pages [11] -->
获取更多资讯

<!-- b000282 | furniture | pages [12] -->
Team # 2401445

<!-- b000283 | furniture | pages [12] -->
Page 12 of 26

<!-- b000285 | heading | pages [12] -->
5.3 Assessing the similarity

<!-- b000286 | prose | pages [12] -->
微信公众号：数学模型 To assess the similarity between the sequences, two primary methods are utilized:

<!-- b000287 | heading | pages [12] -->
1. Total DTW Distance: The sum of the distances along the optimal path. A lower

<!-- b000288 | prose | pages [12] -->
total distance indicates a higher similarity between the sequences.

<!-- b000289 | heading | pages [12] -->
2. DTW Alignment Path: The path through the matrix that minimizes the cumula-

<!-- b000290 | prose | pages [12] -->
tive distance. Observing how closely the path aligns with the diagonal provides a measure of similarity, as a path near the diagonal suggests a strong correspon- dence between the sequences.

<!-- b000291 | prose | pages [12] -->
We selected seven matches from our Model 1 test set for simulation and com- parison, including four from the quarterfinals, two from the semifinals, and the final.

<!-- b000292 | prose | pages [12] -->
微信号：MATHmodels We generated simulated score sequences using random outcomes and predicted se- quences from Model 1. Employing the DTW algorithm, we calculated the Total DTW Distance for both the simulated sequences against the actual data and the Model 1 pre- dictions against the actual sequences. Additionally, we plotted the DTW Alignment Paths to visually compare the simulated and real sequences, as illustrated in the figure below.

<!-- b000293 | caption | pages [12] -->
Figure 7: DTW Alignment Path and Total DTW Distance

<!-- b000294 | prose | pages [12] -->
From the DTW Alignment Paths displayed in the upper part of the graph, it is evident that the curves of the randomly simulated sequences largely deviate from the diagonal, indicating a significant discrepancy from the actual sequence.

<!-- b000295 | prose | pages [12] -->
Furthermore, by comparing the DTW distances between the randomly simulated results, Model 1 predicted sequences, and the actual data, we observe that, except for the match between Rublev and Djokovic where both simulated and model-predicted distances are low, our model consistently yields a smaller distance compared to the random sequences in other matches.

<!-- b000296 | prose | pages [12, 13] -->
关注数学模型 In conclusion, the simulated random sequences fail to accurately represent real- world data, while the results from Model 1 provide a better prediction. This evidence disproves the initial hypothesis, thereby substantiating the existence of momentum.

<!-- b000297 | furniture | pages [12] -->
2

<!-- b000298 | furniture | pages [12] -->
MATHmodels

<!-- b000299 | furniture | pages [12] -->
获取更多资讯

<!-- b000300 | furniture | pages [13] -->
Team # 2401445

<!-- b000301 | furniture | pages [13] -->
Page 13 of 26

<!-- b000303 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000304 | heading | pages [13] -->
6 Model II: Momentum Turning Point Identification and

<!-- b000305 | heading | pages [13] -->
Prediction Model based on HMM-Random Forest

<!-- b000306 | heading | pages [13] -->
6.1 Definition

<!-- b000307 | prose | pages [13] -->
Building upon our previous findings in Task 2, where we established the existence of momentum, we now define these concepts more explicitly.

<!-- b000308 | heading | pages [13] -->
6.1.1 Momentum

<!-- b000309 | prose | pages [13] -->
Momentum represents a player’s control over the game’s dynamics. In the con- text of this task, we simplify momentum into a binary state, denoted as follows:

<!-- b000310 | prose | pages [13] -->
 1, When Player 1 has the upper hand, 微信号：MATHmodels   Momentum = 2, (8) When Player 2 has the upper hand,  0, Otherwise. 

<!-- b000311 | prose | pages [13] -->
Momentum is thus classified as either favoring Player 1, Player 2, or neither.

<!-- b000312 | heading | pages [13] -->
6.1.2 Swing

<!-- b000313 | prose | pages [13] -->
A swing refers to the action of momentum transitioning from 1 to 2 or from 2 to 1. It signifies a significant change in the balance of the match.

<!-- b000314 | heading | pages [13] -->
6.1.3 Turning Point

<!-- b000315 | prose | pages [13] -->
A turning point corresponds to the moment when a swing in momentum occurs. It is associated with a specific time point during the match and coincides with a change in the score that led to the momentum shift.

<!-- b000316 | heading | pages [13] -->
6.2 Figuring Out the Main indicators

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

<!-- b000323 | prose | pages [13, 14] -->
关注数学模型 max depth min samples leaf min samples split n estimators 10 4 10 300 微信公众号：数学模型 Based on the results, our Random Forest model achieved an accuracy of 77.6%, and the most relevant factors in predicting ranked by their contribution are:

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

<!-- b000331 | prose | pages [14] -->
Indicator Explanation

<!-- b000332 | prose | pages [14] -->
Consistent_scores Number of consecutive scores by player in a game Rally_count Total number of shots in this point Distance_run Distance run by player in this point Winner Whether player hits an "untouchable" ball in this point Ace Whether player scores an ace in this point

<!-- b000333 | caption | pages [14] -->
Table 4: Important Indicators

<!-- b000334 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000335 | caption | pages [14] -->
Figure 8: The importance of indicators

<!-- b000336 | prose | pages [14] -->
As the table shows, consistent scores come first. A sequence of consecutive scores by a player generally indicates they are in a period of dominance. When this sequence is broken, it may reveal a vulnerability or a shift in the player’s performance, often coinciding with a momentum swing.

<!-- b000337 | prose | pages [14] -->
Then come the rally count and distance run. A high rally count implies that play- ers are evenly matched, and the conclusion of an intense rally could shift the momen- tum, especially if followed by a decisive play like a winner or an error. While a player who moves more may be under more pressure, and a sudden increase or decrease in movement can signal a change in match dynamics, potentially pointing to a momen- tum shift.

<!-- b000338 | prose | pages [14, 15] -->
关注数学模型 What come next are ’winner’ and ace. Executing a shot that the opponent cannot reach, or a ’winner,’ is a strong indicator of a player seizing the initiative. Addition- ally, serving an ace is a clear sign of dominance in a game. It not only earns a point without rally but also sends a strong message to the opponent. Aces can contribute to 微信公众号：数学模型 a player’s momentum by boosting their confidence and affecting the mental state of the opponent.

<!-- b000339 | furniture | pages [14] -->
2

<!-- b000340 | furniture | pages [14] -->
MATHmodels

<!-- b000341 | furniture | pages [14] -->
获取更多资讯

<!-- b000342 | furniture | pages [15] -->
Team # 2401445

<!-- b000343 | furniture | pages [15] -->
Page 15 of 26

<!-- b000345 | heading | pages [15] -->
6.3 Adjusting the Model based on HMM

<!-- b000346 | prose | pages [15] -->
It seems that the second task can be fully accomplished by the random forest model. However, the word ’different’ in the task given inspires us to think about the different reaction players had when they were in faced with different rivals. Therefore, we consider analyzing each player deeply and take their past score into consideration. And Hidden Markov Model (HMM) greatly meets our needs.

<!-- b000347 | prose | pages [15] -->
In HMM, we consider a system being in one of several hidden states and mak- ing transitions between these states. The system emits observable outputs, which are probabilistically determined by its current state. We define the emission probability 微信号：MATHmodels matrices B1 and B2 for two distinct states, ’P1 upper’ and ’P2 upper’, respectively. Each matrix element P(xi|pj upper) represents the probability of observing the out- come xi given the system is in state pj upper, as illustrated in the following diagram:

<!-- b000348 | caption | pages [15] -->
Figure 9: How HMM works in our context

<!-- b000349 | prose | pages [15] -->
The emission probability matrices for states ’P1 upper’ and ’P2 upper’ are given side by side for comparison:

<!-- b000350 | prose | pages [15, 16] -->
关注数学模型     P(x1|p1 upper) P(x1|p2 upper) P(x2|p1 upper) P(x2|p2 upper)     P(x3|p1 upper) P(x3|p2 upper) B1 = B2 = 微信公众号：数学模型 ... ...

<!-- b000351 | furniture | pages [15] -->
2

<!-- b000352 | furniture | pages [15] -->
MATHmodels

<!-- b000353 | furniture | pages [15] -->
获取更多资讯

<!-- b000354 | furniture | pages [16] -->
Team # 2401445

<!-- b000355 | furniture | pages [16] -->
Page 16 of 26

<!-- b000357 | prose | pages [16] -->
P(xn|p1 upper) P(xn|p2 upper)

<!-- b000358 | prose | pages [16] -->
The initial state distribution, where P1 and P2 are the prior probabilities for the states ’P1 upper’ and ’P2 upper’:

<!-- b000359 | prose | pages [16] -->
P1 P2  P1+P2 × 0.5 P1+P2 × 0.5, 0.5, Π =

<!-- b000360 | prose | pages [16] -->
The matrices B1 and B2 can evolve into a third state ’Equal’ with its own emis- sion probability matrix B3. This transition is indicative of a system that reaches an equilibrium or a tie between the two states, with B3 defined as:

<!-- b000361 | prose | pages [16] -->
  P(x1|equal) 微信号：MATHmodels P(x2|equal)   P(x3|equal) B3 = ...

<!-- b000362 | prose | pages [16] -->
P(xn|equal)

<!-- b000363 | prose | pages [16] -->
The transitions between ’P1 upper’, ’P2 upper’, and ’Equal’ states are governed by transition probabilities, which are not shown in the diagram but are essential compo- nents of the HMM. Together, these matrices and the transitions between them form the core of the HMM, allowing us to model the sequence of states and corresponding observations for a given process.

<!-- b000364 | prose | pages [16] -->
Given the strong temporal correlation within each match and that the contest is between two players, we have trained a separate HMM for each match prior to the quarterfinals. These models contain temporal information from the matches and per- sonal data about the two competing players.

<!-- b000365 | heading | pages [16] -->
6.4 The Final Piece of the Model: Situational Leverage

<!-- b000366 | prose | pages [16] -->
Next, to measure the importance of a scoring point in terms of winning a game, such as when an underdog player has a chance for a break point in the first game, we introduce Situational Leverage. This concept refers to the degree of change in a player’s probability of winning the match based on the outcome of the next point, as shown in the equation below:

<!-- b000367 | prose | pages [16] -->
SLi,j = P(pei,j|wi,t) −P(pei,j|oi,t) (9)

<!-- b000368 | prose | pages [16] -->
Here, P(pei,j|wi,t) denotes PE of player i in the game j, assuming he scores in the t-th point of the game. On the other hand, P(pei,j|oi,t) denotes the PE of player i at the t-th point in the game.

<!-- b000369 | heading | pages [16] -->
6.5 Results and Advices

<!-- b000370 | prose | pages [16] -->
For the final match prediction, we utilized all the previously trained models that included the finalists, players P1 and P2. Each model provided its prediction, and

<!-- b000371 | prose | pages [16, 17] -->
关注数学模型 ultimately, we applied a hard voting mechanism to aggregate these predictions, which is displayed as follows:

<!-- b000372 | furniture | pages [16] -->
2

<!-- b000373 | furniture | pages [16] -->
MATHmodels

<!-- b000374 | furniture | pages [16] -->
获取更多资讯

<!-- b000375 | furniture | pages [17] -->
Team # 2401445

<!-- b000376 | furniture | pages [17] -->
Page 17 of 26

<!-- b000378 | prose | pages [17] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000379 | caption | pages [17] -->
Figure 10: Turning Points Prediction for the Final

<!-- b000380 | prose | pages [17] -->
The curve in the graph represents the cumulative point difference between Alcaraz and Djokovic, while the solid dots are the turning points marked by our model. It can be noted that most of the turning points are not, as we would usually expect, at the bottoms or tops of the cumulative point difference, but rather at the position after the next point. This is because we believe that to judge whether a point is a turning point, the main consideration should be whether it is the beginning of a reversal in the momentum of offense and defense, and this requires confirmation that this move has indeed achieved a reversal in scoring. From this perspective, we consider the marking of turning points to be quite successful.

<!-- b000381 | prose | pages [17] -->
Additionally, compared to the originally labeled data, our model performances well on the final match, as shown in the table.

<!-- b000382 | caption | pages [17] -->
Table 5: Model Results

<!-- b000383 | prose | pages [17] -->
Status Precision Recall F1-Score Support

<!-- b000384 | prose | pages [17] -->
No swings 0.74 0.77 0.76 142 Player1 upper hand 0.81 0.88 0.84 82 Player2 upper hand 0.84 0.74 0.79 110

<!-- b000385 | prose | pages [17] -->
In set 2, as illustrated, we observe a tense situation with densely distributed points, indicating frequent momentum shifts between the two players, which is consistent with common understanding. The turning point near 200 is also well-predicted.

<!-- b000386 | prose | pages [17, 18] -->
关注数学模型 微信公众号：数学模型

<!-- b000387 | furniture | pages [17] -->
2

<!-- b000388 | furniture | pages [17] -->
MATHmodels

<!-- b000389 | furniture | pages [17] -->
获取更多资讯

<!-- b000390 | furniture | pages [18] -->
Team # 2401445

<!-- b000391 | furniture | pages [18] -->
Page 18 of 26

<!-- b000393 | caption | pages [18] -->
Figure 11: When DPI meets turning points

<!-- b000394 | prose | pages [18] -->
In general, based on the indicators selected from random forest as well as the out- puts from HMM and leverages, we prepare 4 advices for coaches: 微信号：MATHmodels

<!-- b000395 | prose | pages [18] -->
• Consistency and Dominance: You should instruct players to strive for consistent scoring as it is a hallmark of dominance. A series of uninterrupted points often signifies control over the match. You should prepare players to recognize when their scoring streak is broken as it may indicate a potential shift in momentum and possibly expose their vulnerabilities.

<!-- b000396 | prose | pages [18] -->
• Rally Count and Movement: You should encourage players to focus on rally counts and their on-court movement. An elevated rally count usually means well-matched play, and the end of a prolonged rally can be pivotal, leading to a momentum swing, particularly if it ends with a critical winner or an unforced error. You should advise players that increased movement might suggest defen- sive pressure.

<!-- b000397 | prose | pages [18] -->
• Aggressive Play and Service: You should emphasize the importance of execut- ing winners and aces. A winner not only captures the point but also asserts dominance, potentially initiating a momentum shift. Similarly, aces serve dual purposes by securing points effortlessly and exerting psychological pressure on the opponent.

<!-- b000398 | prose | pages [18] -->
• Study Your Rival: You should develop strategies based on each player’s re- sponse to momentum shifts, considering both personal tendencies and the op- ponent’s historical patterns. This includes a thorough pre-match analysis of past performances with respect to momentum changes.

<!-- b000399 | heading | pages [18] -->
7 Task 4: Model Generalization

<!-- b000400 | prose | pages [18] -->
To test the efficacy of our model in different matches, we selected three separate events for evaluation: the Wimbledon Men’s Singles, the Wimbledon Women’s Sin- gles, and the US Open (which has a different surface). Note that the data are extracted from the official site of Wimbledon tennis[5].

<!-- b000401 | prose | pages [18, 19] -->
关注数学模型 Tcted from he table below presetrants the performance of our model applied to three different tennis matches, detailing the f1 scores for three scenarios and the overall accuracy for point classification.

<!-- b000402 | furniture | pages [18] -->
2

<!-- b000403 | furniture | pages [18] -->
MATHmodels

<!-- b000404 | furniture | pages [18] -->
获取更多资讯

<!-- b000405 | furniture | pages [19] -->
Team # 2401445

<!-- b000406 | furniture | pages [19] -->
Page 19 of 26

<!-- b000408 | prose | pages [19] -->
微信公众号：数学模型 Match 0_f1_score 1_f1_score 2_f1_score Accuracy 2023-wimbledon-2503 0.78 0.82 0.90 0.83 2023-wimbledon-1602 0.78 0.88 0.90 0.85 2023-usopen-1102 0.51 0.61 0.65 0.58

<!-- b000409 | caption | pages [19] -->
Table 6: Report of Our Prediction

<!-- b000410 | prose | pages [19] -->
2023 Wimbledon Men’s Singles 1602: Jannik Sinner VS Novak 7.1 Djokovic

<!-- b000411 | prose | pages [19] -->
For the 2023 Wimbledon Championships Men’s Singles, we employed the same prediction method as used in the second query, namely the Hidden Markov Model 微信号：MATHmodels (HMM) for forecasting.

<!-- b000412 | caption | pages [19] -->
Figure 12: Turning Points Prediction:1602

<!-- b000413 | prose | pages [19] -->
2023 Wimbledon Women’s Singles 2503: Ons Jabeur VS Elena 7.2 Rybakina

<!-- b000414 | prose | pages [19] -->
However, for the Women’s Singles and the 2023 US Open Men’s Singles, we lacked a pre-trained HMM model. Consequently, we resorted to a combined approach of Random Forest and leverage forecasting for our predictions, the results of which are illustrated in the subsequent table.

<!-- b000415 | prose | pages [19, 20] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000416 | furniture | pages [19] -->
2

<!-- b000417 | furniture | pages [19] -->
MATHmodels

<!-- b000418 | furniture | pages [19] -->
获取更多资讯

<!-- b000419 | furniture | pages [20] -->
Team # 2401445

<!-- b000420 | furniture | pages [20] -->
Page 20 of 26

<!-- b000422 | caption | pages [20] -->
Figure 13: Turning Points Prediction:2503

<!-- b000423 | prose | pages [20] -->
2020 US Open 1102: Alexandre Muller VS Arthur Rinderknech 7.3

<!-- b000424 | prose | pages [20] -->
Specifically, for the 2023 US Open Men’s Singles, our model did not achieve sat- isfactory results. We attribute this to a discrepancy between the floor material of the match venue and that of the matches in our training set.

<!-- b000425 | prose | pages [20] -->
In summary, to enhance the predictive accuracy of our model regarding the mo- mentum turning points in tennis matches, we should consider additional factors such as the court surface material and the altitude of the venue. These elements are poten- tial influencers of match momentum and player performance and merit inclusion in future model training considerations.

<!-- b000426 | heading | pages [20] -->
8 Sensitivity Analysis

<!-- b000427 | prose | pages [20] -->
Previous Task 4 tested the generalization ability of our model. In this section, we will examine the sensitivity of the model. For the key indicators given by the previous random forest model, we introduce significant Gaussian noise to "consistent scores" and "distance run," and then re-calculate the model’s recall metric. As shown in the figure, although there is a decrease in recall, the extent of the decrease is small, demon- strating the excellent robustness of our model.

<!-- b000428 | heading | pages [20] -->
9 Strength and Weakness

<!-- b000429 | heading | pages [20] -->
9.1 Strength

<!-- b000430 | prose | pages [20] -->
• Our model uniquely integrates multiple dimensions including athlete perfor- mance, personal strength, and serving advantage, offering a comprehensive evaluation of match dynamics.

<!-- b000431 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000432 | furniture | pages [20] -->
2

<!-- b000433 | furniture | pages [20] -->
MATHmodels

<!-- b000434 | furniture | pages [20] -->
获取更多资讯

<!-- b000435 | furniture | pages [21] -->
Team # 2401445

<!-- b000436 | furniture | pages [21] -->
Page 21 of 26

<!-- b000438 | caption | pages [21] -->
Figure 14: Turning Points Prediction:1102

<!-- b000439 | caption | pages [21] -->
Figure 15: Recall before and after Gaussian noise is added

<!-- b000440 | prose | pages [21] -->
• We have comprehensively modelled the standard international rules of tennis to reflect the differences from the real game.

<!-- b000441 | prose | pages [21] -->
• Our model integrates the strengths of both Random Forest and HMM.

<!-- b000442 | heading | pages [21] -->
9.2 Weakness and Further Discussion

<!-- b000443 | prose | pages [21] -->
• The HMM model is overly reliant on historical data, including the performance of established players and match records, when predicting the outcome of tennis matches.

<!-- b000444 | prose | pages [21] -->
• The model performs poorly in generalising to other ball games. Our final se- lection of metrics using the Random Forest model remains closely related to the

<!-- b000445 | prose | pages [21, 22] -->
关注数学模型 specific metrics of tennis.

<!-- b000446 | furniture | pages [21] -->
2

<!-- b000447 | furniture | pages [21] -->
MATHmodels

<!-- b000448 | furniture | pages [21] -->
获取更多资讯

<!-- b000449 | furniture | pages [22] -->
Team # 2401445

<!-- b000450 | furniture | pages [22] -->
Page 22 of 26

<!-- b000452 | heading | pages [22] -->
References

<!-- b000453 | references | pages [22] -->
微信公众号：数学模型

<!-- b000454 | references | pages [22] -->
[1] Dietl, Helmut, and Cornel Nesseler. "Momentum in tennis:

<!-- b000455 | references | pages [22] -->
Controlling the

<!-- b000456 | references | pages [22] -->
match." *UZH Business Working Paper Series* 365 (2017).

<!-- b000457 | references | pages [22] -->
[2] Seidl, R., Lucey, P. Live Counter-Factual Analysis in Women’s Tennis using Au-

<!-- b000458 | references | pages [22] -->
tomatic Key-Moment Detection.

<!-- b000459 | references | pages [22] -->
[3] Moss, Ben, and Peter O’Donoghue. "Momentum in US Open men’s singles ten-

<!-- b000460 | references | pages [22] -->
nis." *International Journal of Performance Analysis in Sport* 15.3 (2015): 884-896.

<!-- b000461 | references | pages [22] -->
[4] O’Donoghue, Peter, and Emily Brown. "Sequences of service points and the mis-

<!-- b000462 | references | pages [22] -->
perception of momentum in elite tennis." *International Journal of Performance

<!-- b000463 | references | pages [22] -->
Analysis in Sport* 9.1 (2009): 113-127.

<!-- b000464 | references | pages [22] -->
微信号：MATHmodels

<!-- b000465 | references | pages [22] -->
[5] "The Championships, Wimbledon." Accessed February 6, 2024. https://www.

<!-- b000466 | references | pages [22] -->
wimbledon.com/index.html.

<!-- b000467 | references | pages [22] -->
关注数学模型

<!-- b000468 | furniture | pages [22] -->
2

<!-- b000469 | furniture | pages [22] -->
MATHmodels

<!-- b000470 | furniture | pages [22] -->
获取更多资讯

<!-- b000471 | furniture | pages [23] -->
Team # 2401445

<!-- b000472 | furniture | pages [23] -->
Page 23 of 26

<!-- b000473 | heading | pages [23] -->
10 Memorandum for The Coaches

<!-- b000474 | prose | pages [23] -->
To: Coaches From: Team #2401445 微信公众号：数学模型 Subject: Date: February 6, 2024

<!-- b000475 | prose | pages [23] -->
The phenomenon of momentum in tennis has long been debated, with the 2023 Wimbledon final serving as a testament to its potential impact. Our study delves into the intricacies of match flow, focusing on the dynamics that drive momentum swings and their predictable patterns.

<!-- b000476 | prose | pages [23] -->
We developed a Dynamic Play Index (DPI) by integrating data preprocessing tech- niques and advanced statistical models such as Gradient Boosting Trees and the Hid- den Markov Model. Our DPI synthesizes performance metrics, personal strengths, and serving advantages into a comprehensive measure of match flow, yielding in- sights with 82.4% accuracy. 微信号：MATHmodels Understanding and capitalizing on momentum is paramount in competitive ten- nis. Our data indicates that the following elements are critical in maintaining and exploiting momentum:

<!-- b000477 | prose | pages [23] -->
• Score Streaks: Teach players to focus on the next point to build and maintain dominance. Recognize and adjust quickly if the streak is broken to prevent mo- mentum shift.

<!-- b000478 | prose | pages [23] -->
• Endurance in Rallies: Use high rally counts as a measure of player stamina and competitive edge. Train players to stay mentally engaged and look for opportu- nities to conclude rallies with strategic plays.

<!-- b000479 | prose | pages [23] -->
• Decisive Shots: Encourage players to develop precision in aggressive shots, such as winners and aces, which can change the game’s tempo and put psy- chological pressure on the opponent.

<!-- b000480 | prose | pages [23] -->
• Opponent Analysis: Implement drills that mimic rivals’ play styles and weak- nesses, enabling players to adapt their strategies during actual match play.

<!-- b000481 | prose | pages [23] -->
In the ebb and flow of a tennis match, players will inevitably face moments that test their resolve and adaptability. Our study highlights several scenarios where prepara- tion can make a significant difference:

<!-- b000482 | prose | pages [23] -->
• Closing the Gap: Teach players to compartmentalize the score when down, fo- cusing solely on earning the next point. This laser focus can help in gradually diminishing the lead of the opponent.

<!-- b000483 | prose | pages [23] -->
• Shifting Back Momentum: Introduce drills where players lose points on pur- pose and then work to recover, teaching them to identify and counteract mo- mentum shifts.

<!-- b000484 | prose | pages [23] -->
• Pressure Points: Simulate break points and tiebreaks in practice sessions, en- couraging players to employ specific, practiced responses to these high-stakes moments.

<!-- b000485 | prose | pages [23, 24] -->
关注数学模型 • Break Point Strategies: Have players practice aggressive returns and pinpoint the opponent’s weak spots during simulated break opportunities to take charge of the game’s flow.

<!-- b000486 | furniture | pages [23] -->
2

<!-- b000487 | furniture | pages [23] -->
MATHmodels

<!-- b000488 | furniture | pages [23] -->
获取更多资讯

<!-- b000489 | furniture | pages [24] -->
Team # 2401445

<!-- b000490 | furniture | pages [24] -->
Page 24 of 26

<!-- b000492 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000493 | prose | pages [24] -->
• Lead Protection: Use drills that start with the player in the lead, emphasizing the need to continue playing offensively to secure the win, rather than passively trying to maintain the lead.

<!-- b000494 | prose | pages [24] -->
Our predictive model is not only a tool for analysis but a cornerstone for building mental toughness and tactical agility in players. As a coach, your role transcends physical training. You are the architect of your players’ mental resilience, equipping them to maneuver through the psychological battles intrinsic to competitive tennis. The strategies we’ve detailed are crafted to embolden your players, enabling them to confront the challenges of match play with assured confidence and grace.

<!-- b000495 | prose | pages [24] -->
Transitioning from mental preparation to real-time match analysis, our model ex- cels by offering assessments of a player’s dynamic state as the game unfolds. This 微信号：MATHmodels granular insight into the flow of play is pivotal for making strategic decisions that har- ness the power of momentum swings. By leveraging this data, you can guide players to make intelligent, on-the-fly adjustments that can alter the course of a match.

<!-- b000496 | prose | pages [24] -->
It’s important to acknowledge, however, that our model, while comprehensive, is not without its limitations. One such area is the nuanced influence of different court surfaces on a player’s momentum — a variable that we aim to better understand and integrate into future iterations of the model. This presents an exciting opportunity for further enhancement, ensuring that our tool evolves in line with the complexities of the sport.

<!-- b000497 | prose | pages [24] -->
In conclusion, the integration of our model into your coaching methodology can be transformative. By translating our insights into practical training exercises, players can be adeptly prepared to exploit the ebb and flow of play, turning what was once an intangible concept into a quantifiable advantage. We are committed to continuous improvement, working alongside you to refine our system and support your efforts in forging champions on the court.

<!-- b000498 | prose | pages [24] -->
Warm regards,

<!-- b000499 | furniture | pages [24] -->
Team #2401445

<!-- b000500 | prose | pages [24] -->
关注数学模型

<!-- b000501 | furniture | pages [24] -->
2

<!-- b000502 | furniture | pages [24] -->
MATHmodels

<!-- b000503 | furniture | pages [24] -->
获取更多资讯

<!-- b000504 | furniture | pages [25] -->
Team # 2401445

<!-- b000505 | furniture | pages [25] -->
Page 25 of 26

<!-- b000506 | heading | pages [25] -->
Appendices

<!-- b000507 | heading | pages [25] -->
Appendix A

<!-- b000508 | prose | pages [25] -->
Indicators Chosen for Training Random For- 微信公众号：数学模型 est Model

<!-- b000509 | prose | pages [25] -->
Metric (Feature) Explanation

<!-- b000510 | prose | pages [25] -->
p1_consistent_scores Number of consecutive scores by player 1 in a game p2_consistent_scores Number of consecutive scores by player 2 in a game p1_ace Whether player 1 scores an ace in this point p2_ace Whether player 2 scores an ace in this point p1_winner Whether player 1 hits an "untouchable" ball in this point p2_winner Whether player 2 hits an "untouchable" ball in this point p1_double_fault Whether player 1 commits a double fault in this point p2_double_fault Whether player 2 commits a double fault in this point 微信号：MATHmodels p1_break_pt_won Whether player 1 breaks serve in this point p2_break_pt_won Whether player 2 breaks serve in this point p1_break_pt_missed Player 1 misses the chance to win the game on player 2’s serve p2_break_pt_missed Player 2 misses the chance to win the game on player 1’s serve p1_distance_run Distance run by player 1 in this point p2_distance_run Distance run by player 2 in this point rally_count Total number of shots in this point

<!-- b000511 | caption | pages [25] -->
Table 7: Tennis Match Metrics

<!-- b000512 | prose | pages [25] -->
AI Report

<!-- b000513 | prose | pages [25] -->
Query 1: Momentum in Tennis Papers

<!-- b000514 | prose | pages [25] -->
Input: Could you please help me to find out if there are any relevant papers on momentum in tennis, thanks!

<!-- b000515 | prose | pages [25] -->
Output: It seems there was an issue retrieving the full text of the papers directly from the websites. However, based on the search results, there are several relevant pa- pers on momentum in tennis, covering aspects such as the psychological and strategic momentum, its effects on match control, and empirical analyses of professional tennis matches. Titles include:

<!-- b000516 | prose | pages [25] -->
• Momentum in tennis: Controlling the match

<!-- b000517 | prose | pages [25] -->
• Separating psychological momentum from strategic momentum: Evidence ...

<!-- b000518 | prose | pages [25] -->
• Set-level Strategic and Psychological Momentum in Best-of-three-set ...

<!-- b000519 | prose | pages [25] -->
• Strategic and Psychological Momentum in Professional Tennis

<!-- b000520 | prose | pages [25, 26] -->
关注数学模型 Query 2: Missing Values in Data

<!-- b000521 | furniture | pages [25] -->
2

<!-- b000522 | furniture | pages [25] -->
MATHmodels

<!-- b000523 | furniture | pages [25] -->
获取更多资讯

<!-- b000524 | furniture | pages [26] -->
Team # 2401445

<!-- b000525 | furniture | pages [26] -->
Page 26 of 26

<!-- b000527 | prose | pages [26] -->
Input: Could you please help me to check the data for missing values, and if so, could you please give some proper suggestions to deal with the missing values, 微信公众号：数学模型 thanks!

<!-- b000528 | prose | pages [26] -->
Output: The dataset contains missing values in the following columns:

<!-- b000529 | prose | pages [26] -->
• speed_mph: 752 missing values

<!-- b000530 | prose | pages [26] -->
• serve_width: 54 missing values

<!-- b000531 | prose | pages [26] -->
• serve_depth: 54 missing values

<!-- b000532 | prose | pages [26] -->
• return_depth: 1309 missing values

<!-- b000533 | prose | pages [26] -->
To deal with these missing values, consider the following strategies:

<!-- b000534 | prose | pages [26] -->
微信号：MATHmodels 1. Imputation for numerical and categorical columns.

<!-- b000535 | prose | pages [26] -->
2. Deletion of rows or columns with missing values.

<!-- b000536 | prose | pages [26] -->
3. Model-Based Methods for predicting missing values.

<!-- b000537 | prose | pages [26] -->
4. Use a Flag for Missing Values to indicate missing data.

<!-- b000538 | prose | pages [26] -->
Query 3: Tennis Player Ability Evaluation Index

<!-- b000539 | prose | pages [26] -->
Input: Could you please help me to find information and papers related to the tennis player ability evaluation index, I would like to know if there is an index to quantify it, thank you.

<!-- b000540 | prose | pages [26] -->
Output: Relevant resources include:

<!-- b000541 | prose | pages [26] -->
1. Construction of Evaluation Model of Tennis Skills and Tactic Level and Applica- tion of Grey Relational Algorithm.

<!-- b000542 | prose | pages [26] -->
2. Tennis Players Comprehensive Ability Evaluation using a fuzzy comprehensive evaluation model.

<!-- b000543 | prose | pages [26] -->
3. Optimization Analysis of Tennis Players’ Physical Fitness Index Based on Data Mining and Mobile Computing with the XGBoost algorithm.

<!-- b000544 | prose | pages [26] -->
These studies focus on developing comprehensive models for evaluating tennis play- ers’ abilities across various factors.

<!-- b000545 | prose | pages [26] -->
关注数学模型

<!-- b000546 | furniture | pages [26] -->
2

<!-- b000547 | furniture | pages [26] -->
MATHmodels

<!-- b000548 | furniture | pages [26] -->
获取更多资讯
