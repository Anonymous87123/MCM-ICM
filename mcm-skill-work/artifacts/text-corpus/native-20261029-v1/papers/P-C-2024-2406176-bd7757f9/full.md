# P-C-2024-2406176-bd7757f9

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
2406176

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | prose | pages [1] -->
Momentum, elucidating the phenomenon wherein a player’s real-time performance surpasses pre-match expectations, holds paramount significance in tennis matches. This paper introduces the Real-Time Momentum Quantification (RTMQ) model, which quantifies momentum by assessing the disparity between a player’s pre-match win probability and the real-time win probability. The study establishes the importance of momentum by comparing our model’s results with an alternative model that neglects in-match performance. Notably, specialized indicators are employed to predict momentum swings, and game theory is applied to strategize against different opponents.

<!-- b000011 | prose | pages [1] -->
First, we use the independent and identically distributed (IID) assumption to reverse calculate the server’s probability of winning the first point (𝑝0), base on the Elo rating system. IID assumption is not applied to calculate any other value, including real-time win probability. Then, RTMQ model is constructed by integrating 𝑝0 and the Real-Time Win Probability (RTWP) model for

<!-- b000012 | title | pages [1] -->
微信号：MATHmodels

<!-- b000013 | prose | pages [1] -->
calculating subsequent point win probabilities during a match, that also eliminates the effect of the serve side advantage. The resulting momentum difference aligns seamlessly with real-world The significance of momentum is confirmed through a K-S test, rejecting the observations. hypothesis that in-match performance is inconsequential. Further analysis involves applying the Fourier Series Fitting (FSF) model to track momentum trend.

<!-- b000014 | prose | pages [1] -->
To forecast large momentum shifts, a Swing Prediction (SP) model is introduced. The model operates on a per-set basis, as a set provides a more comprehensive dataset for analysis compared to individual games. We sample the momentum trend value (MMTTV) from the momentum trend at the end of each set. This is because the frequent in-set momentum shifts can render predictions based on real-time momentum data at the end of each set unreliable. At the same time, key technical performance factors are distilled from specialized indicators through factor analysis. We then employ a Multivariate Linear Regression model to predict the swings. Our model demonstrates an impressive prediction accuracy of 90.44% on our test problem, with specific factors such as 2nd_serve_direct_won and Net_approach_point_won identified as crucial contributors to player 1’s momentum.

<!-- b000015 | prose | pages [1] -->
The paper extends its analysis to dynamic strategic choices made by tennis players during matches, employing the Mixed-Strategy Nash Equilibrium model.

<!-- b000016 | prose | pages [1] -->
K-means clustering is utilized to determine strategic clusters. The Nash equilibrium is calculated, offering insights into optimal strategy combinations against different opponents.

<!-- b000017 | prose | pages [1] -->
The efficacy of the proposed models is validated through testing on notable tennis matches, including the extraordinarily tight 2023 Wimbledon Gentlemen’s Final between Carlos Alcaraz and Novak Djokovic, and the one-sided 2017 French Open match between Andy Murray and Andrey Kuznetsov. The SP model exhibits high accuracy (85.32% for the Alcaraz vs. Djokovic match, and 88.34% for the Murray vs. Kuznetsov match), while the FSF model accurately cap- tures momentum trends, taking into account the score situation and historical commentary. Eventually, we pinpoint crucial factors for inclusion in future models.

<!-- b000018 | keywords | pages [1] -->
Keywords: tennis; momentum; real-time win probability; Elo rating system; mixed-strategy Nash

<!-- b000019 | prose | pages [1] -->
equilibrium; quantification model

<!-- b000020 | furniture | pages [1] -->
关注数学模型

<!-- b000021 | furniture | pages [1] -->
2

<!-- b000022 | furniture | pages [1] -->
MATHmodels

<!-- b000023 | furniture | pages [1] -->
获取更多资讯

<!-- b000024 | furniture | pages [2] -->
Team # 2406176

<!-- b000025 | furniture | pages [2] -->
Page 2 of 27

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000028 | contents | pages [2] -->
1

<!-- b000029 | heading | pages [2] -->
Introduction

<!-- b000030 | prose | pages [2] -->
4

<!-- b000031 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background Information 4

<!-- b000032 | prose | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 4

<!-- b000033 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 Model Overview

<!-- b000034 | prose | pages [2] -->
2

<!-- b000035 | heading | pages [2] -->
Assumptions

<!-- b000036 | prose | pages [2] -->
3 Notifications

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | heading | pages [2] -->
Data Source

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | prose | pages [2] -->
5

<!-- b000041 | prose | pages [2] -->
6

<!-- b000042 | prose | pages [2] -->
6

<!-- b000043 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000044 | heading | pages [2] -->
Real-Time Momentum Quantification Model

<!-- b000045 | prose | pages [2] -->
5 6

<!-- b000046 | prose | pages [2] -->
Pre-match Win Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1

<!-- b000047 | prose | pages [2] -->
5.2 Probability of Winning the First Point

<!-- b000048 | prose | pages [2] -->
7

<!-- b000049 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | prose | pages [2] -->
8

<!-- b000051 | prose | pages [2] -->
Dynamic Computation of the Subsequent Points’ Win Probabilities . . . . . . . . . 5.3 9

<!-- b000052 | prose | pages [2] -->
Quantification of Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 11

<!-- b000053 | prose | pages [2] -->
Verification of the Significance of Momentum . . . . . . . . . . . . . . . . 5.4.1 12

<!-- b000054 | prose | pages [2] -->
Momentum Trend Value (MMTTV) Visualization . . . . . . . . . . . . . . . . . . 5.5

<!-- b000055 | prose | pages [2] -->
6

<!-- b000056 | heading | pages [2] -->
Swing Prediction Model

<!-- b000057 | prose | pages [2] -->
14

<!-- b000058 | prose | pages [2] -->
15

<!-- b000059 | prose | pages [2] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 15

<!-- b000060 | prose | pages [2] -->
Indicators Calculation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 15

<!-- b000061 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 Exploratory Factor Analysis 16

<!-- b000062 | prose | pages [2] -->
Prediction of Swing Based on Multivariate Linear Regression Model . . . . . . . . 6.4

<!-- b000063 | prose | pages [2] -->
7

<!-- b000064 | heading | pages [2] -->
Mixed-Strategy Nash Equilibrium Model

<!-- b000065 | prose | pages [2] -->
17

<!-- b000066 | prose | pages [2] -->
18

<!-- b000067 | prose | pages [2] -->
Strategy Payoff Calculation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 18

<!-- b000068 | prose | pages [2] -->
Model Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000069 | prose | pages [2] -->
8

<!-- b000070 | heading | pages [2] -->
Test of FSF Model and SP Model

<!-- b000071 | prose | pages [2] -->
20

<!-- b000072 | prose | pages [2] -->
21

<!-- b000073 | prose | pages [2] -->
The Match between Alcaraz and Djokovic . . . . . . . . . . . . . . . . . . . . . . 8.1 21

<!-- b000074 | furniture | pages [2] -->
关注数学模型

<!-- b000075 | furniture | pages [2] -->
2

<!-- b000076 | furniture | pages [2] -->
MATHmodels

<!-- b000077 | furniture | pages [2] -->
获取更多资讯

<!-- b000078 | furniture | pages [3] -->
Team # 2406176

<!-- b000079 | furniture | pages [3] -->
Page 3 of 27

<!-- b000080 | prose | pages [3] -->
Model Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 22

<!-- b000081 | prose | pages [3] -->
Contextual Limitations in SP Model . . . . . . . . . . . . . . . . . . . . . . . . . 8.3 22

<!-- b000082 | prose | pages [3] -->
Key Indicators to be Included in Future Models . . . . . . . . . . . . . . . . . . . 8.4 22

<!-- b000083 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000084 | prose | pages [3] -->
9

<!-- b000085 | heading | pages [3] -->
Sensitivity Analysis

<!-- b000086 | heading | pages [3] -->
Appendices

<!-- b000087 | prose | pages [3] -->
23

<!-- b000088 | prose | pages [3] -->
26

<!-- b000089 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000090 | furniture | pages [3] -->
关注数学模型

<!-- b000091 | furniture | pages [3] -->
2

<!-- b000092 | furniture | pages [3] -->
MATHmodels

<!-- b000093 | furniture | pages [3] -->
获取更多资讯

<!-- b000094 | furniture | pages [4] -->
Team # 2406176

<!-- b000095 | prose | pages [4] -->
1

<!-- b000096 | heading | pages [4] -->
Introduction

<!-- b000097 | prose | pages [4] -->
1.1 Background Information

<!-- b000098 | furniture | pages [4] -->
Page 4 of 27

<!-- b000099 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000100 | prose | pages [4] -->
In the 2023 Wimbledon final, Carlos Alcaraz overcame Novak Djokovic’s initial dominance to win, demonstrating a thrilling momentum shift. This echoed the 2008 final where Rafael Nadal triumphed over Roger Federer, highlighting the unpredictable and captivating nature of tennis.

<!-- b000101 | prose | pages [4] -->
Research has shown that athletes, especially tennis players, can experience a psychological or physiological boost known as momentum. This concept was first explored in a study by Gilovich, Vallone, and Tversky (1985), who identified a ‘hot hand’ phenomenon in basketball where a player’s real-time performance significantly exceeds pre-match expectations based on his overall record. However, momentum can be temporary and may shift to the opponent, leading to swings where potential winners lose several points or games.

<!-- b000102 | prose | pages [4] -->
This paper explores the dynamic performance changes of players throughout a game and offers in-depth insights into how players’ techniques and strategies should adapt in response to their

<!-- b000103 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000104 | prose | pages [4] -->
opponents’ key factors.

<!-- b000105 | prose | pages [4] -->
1.2 Problem Analysis

<!-- b000106 | prose | pages [4] -->
• Task 1: Construct a model that dynamically calculates the performance of both players within the match, taking serving-advantage into consideration.

<!-- b000107 | prose | pages [4] -->
In this paper, we develop an RTWP (Real-Time Win Probability) model that accurately predicts the win probability of the subsequent point based on Elo rating system in real time. On that basis, we built the RTMQ (Real-Time Momentum Quantification) model by effectively quantifying player performance, by calculating the difference between real- time and pre-match win rates under separate serve/receive conditions (considering the serving side’s advantage). Finally we apply Fourier-series fitting to MMT to obtain the momentum trend value (MMTTV).

<!-- b000108 | prose | pages [4] -->
• Task 2: Evaluate the significance of ’momentum’ in tennis matches.

<!-- b000109 | prose | pages [4] -->
We took the 2023 Winbledon final as an example and tested our RTWP model and the

<!-- b000110 | heading | pages [4] -->
CWP (Constant Win Probability) model, which neglects the influence of momentum. A

<!-- b000111 | prose | pages [4] -->
Kolmogorov-Smirnov (K-S) test is performed taking the model results as the input and confirms the significant role that momentum plays in the match, reversing the coach’s hypothesis.

<!-- b000112 | prose | pages [4] -->
• Task 3: Determine the key indicators that could trigger a momentum shift.

<!-- b000113 | prose | pages [4] -->
We introduce the Swing Prediction (SP) model to anticipate substantial momentum shifts, using the more stable MMTTV as a sample for each set. This is because the frequent in-set momentum shifts can render predictions based on real-time momentum data at the end of each set unreliable. MMTTV has no such fluctuations and effectively captures the trend of MMT. Subsequently, we identify technical indicators influencing player performance, extract common factors through factor analysis, and employ these as independent variables in a Multivariate Linear Regression to predict the swings. Subsequently, we apply K-means

<!-- b000114 | furniture | pages [4] -->
关注数学模型

<!-- b000115 | furniture | pages [4] -->
2

<!-- b000116 | furniture | pages [4] -->
MATHmodels

<!-- b000117 | furniture | pages [4] -->
获取更多资讯

<!-- b000118 | furniture | pages [5] -->
Team # 2406176

<!-- b000119 | furniture | pages [5] -->
Page 5 of 27

<!-- b000120 | prose | pages [5] -->
clustering to distinguish between different tactics and finally calculate the player’s optimal strategy using a mixed-strategy Nash equilibrium approach.

<!-- b000121 | prose | pages [5] -->
• Task 4: Assess the model’s ability to predict match swings and evaluate its performance

<!-- b000122 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000123 | prose | pages [5] -->
across various tournaments, court surfaces, and other sports.

<!-- b000124 | prose | pages [5] -->
We validated the accuracy of our model using data from other matches in the dataset and conducted a sensitivity analysis. Subsequently, we discussed potential improvements to the model by considering factors such as climate and court surface. Finally, we further discussed the generalization capabilities of our model using the 2017 French Open Men’s Singles dataset as an example.

<!-- b000125 | prose | pages [5] -->
1.3

<!-- b000126 | heading | pages [5] -->
Model Overview

<!-- b000127 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000128 | caption | pages [5] -->
Figure 1: Model Overview

<!-- b000129 | prose | pages [5] -->
2

<!-- b000130 | heading | pages [5] -->
Assumptions

<!-- b000131 | prose | pages [5] -->
• All tennis players in the table demonstrate a high level of adaptability during play. This adaptability is reflected in their ability to continuously modify strategies based on their opponent’s characteristics.

<!-- b000132 | prose | pages [5] -->
• The technical indicators in the table, such as the way of winning, are able to fully characterize the strategy adopted by the current player. Changes in these indicators during a match can fully characterize changes in a player’s strategy.

<!-- b000133 | prose | pages [5] -->
• All data are authentic.

<!-- b000134 | furniture | pages [5] -->
关注数学模型

<!-- b000135 | furniture | pages [5] -->
2

<!-- b000136 | furniture | pages [5] -->
MATHmodels

<!-- b000137 | furniture | pages [5] -->
获取更多资讯

<!-- b000138 | furniture | pages [6] -->
Team # 2406176

<!-- b000139 | prose | pages [6] -->
3 Notifications

<!-- b000140 | furniture | pages [6] -->
Page 6 of 27

<!-- b000141 | caption | pages [6] -->
Table 1: Significant symbols in this paper

<!-- b000142 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000143 | heading | pages [6] -->
Symbols

<!-- b000144 | prose | pages [6] -->
Description

<!-- b000145 | prose | pages [6] -->
the 𝑖𝑡ℎplayer’s Elo rating at the 𝑡𝑡ℎmatch 𝐸𝑖(𝑡) a prediction based on Elo indicating that the 𝑖𝑡ℎplayer defeats the 𝑗𝑡ℎopponent 𝑃𝑖𝑗(𝑡) 𝑝0 the probability of a server winning the first point, constant during match ˆ𝑝(𝑆𝑚) the probability of a server winning the next point, dynamic within match 𝜂(𝑆𝑚) a dynamic weight that balances the pre-match and in-match serve information 𝜆𝑖 a weight emphasizing performance at the moment over the initial performance PA(t) Real-Time Win Probability of player A MMTA(t) Real-Time Momentum value of player A MMTTVA(t) Real-Time Momentum Trend value of player A

<!-- b000146 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000147 | prose | pages [6] -->
4

<!-- b000148 | heading | pages [6] -->
Data Source

<!-- b000149 | caption | pages [6] -->
Table 2: The websites we use to obtain the necessary data

<!-- b000150 | prose | pages [6] -->
No.

<!-- b000151 | prose | pages [6] -->
Website

<!-- b000152 | prose | pages [6] -->
1 https://www.tenelos.com/ https://www.atptour.com/en/rankings/ 2 singles?DateWeek=2023-07-03

<!-- b000153 | prose | pages [6] -->
3 https://www.wimbledon.com/ 4 https://github.com/JeffSackmann/ ten- nis_slam_pointbypoint

<!-- b000154 | prose | pages [6] -->
Usage

<!-- b000155 | prose | pages [6] -->
Acquire Elo ratings of all players before match

<!-- b000156 | prose | pages [6] -->
Acquire 𝑚𝑖to calculate 𝐾𝑖of players before match

<!-- b000157 | prose | pages [6] -->
Search for relevant data of players in the dataset

<!-- b000158 | prose | pages [6] -->
2017 French Open dataset for problem 4

<!-- b000159 | heading | pages [6] -->
Real-Time Momentum Quantification Model

<!-- b000160 | prose | pages [6] -->
5

<!-- b000161 | prose | pages [6] -->
In our RTMQ model, we adopt a definition of momentum that is consistent with the classic interpretation of Gilovich et al. (1985). In this context, momentum is defined as a player’s performance during a given period that significantly exceeds his expected performance based on pre-match predictions. The calculation of momentum involves determining the difference between the pre-match win probability and the real-time win probability. The greater the difference, the greater the momentum.

<!-- b000162 | prose | pages [6] -->
The modeling process is divided into four stages: obtaining the pre-match win prediction, determining the first point’s win probability, dynamically computing the subsequent points’ win probabilities, and calculating the difference eventually. The modeling flow of the RTMQ model is shown below.

<!-- b000163 | furniture | pages [6] -->
关注数学模型

<!-- b000164 | furniture | pages [6] -->
2

<!-- b000165 | furniture | pages [6] -->
MATHmodels

<!-- b000166 | furniture | pages [6] -->
获取更多资讯

<!-- b000167 | furniture | pages [7] -->
Team # 2406176

<!-- b000168 | furniture | pages [7] -->
Page 7 of 27

<!-- b000169 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000170 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000171 | caption | pages [7] -->
Figure 2: RTMQ model setup

<!-- b000172 | prose | pages [7] -->
5.1 Pre-match Win Prediction

<!-- b000173 | prose | pages [7] -->
We utilize the Elo rating system to predict match outcomes before the game. This outstand- ing system, dynamic and zero-sum, adjusts player ratings based on match outcomes and maintains fairness. Its simplicity, robustness, and proven effectiveness across sports highlight its adaptability and reliability.

<!-- b000174 | prose | pages [7] -->
The rating of a player is calculated with the following recursive formula:

<!-- b000175 | prose | pages [7] -->
𝐸𝑖(𝑡+ 1) = 𝐸𝑖(𝑡) + 𝐾𝑖×  𝑃𝑖𝑗(𝑡) −𝑊𝑖(𝑡)

<!-- b000176 | prose | pages [7] -->
𝐸𝑖(1) = 1500 (1)

<!-- b000177 | prose | pages [7] -->
where 𝐸𝑖denotes the 𝑖𝑡ℎplayer’s Elo rating (in a player’s very first tour match, 𝐸𝑖(1) is assigned 1500), 𝑡is the number of match, 𝑊𝑖is a discrete variable that equals 1 if the player loses the match and equals 0 if the player wins the match, and 𝑃𝑖𝑗(𝑡) is a prediction based on Elo indicating that the 𝑖𝑡ℎplayer defeats the 𝑗𝑡ℎopponent. 𝐾𝑖, relevant to the number of the player’s career matches, is equal to

<!-- b000178 | prose | pages [7] -->
𝐾𝑖= 250

<!-- b000179 | prose | pages [7] -->
(2) (𝑚𝑖(𝑡) + 5)0.4

<!-- b000180 | furniture | pages [7] -->
关注数学模型

<!-- b000181 | furniture | pages [7] -->
2

<!-- b000182 | furniture | pages [7] -->
MATHmodels

<!-- b000183 | furniture | pages [7] -->
获取更多资讯

<!-- b000184 | furniture | pages [8] -->
Team # 2406176

<!-- b000185 | furniture | pages [8] -->
Page 8 of 27

<!-- b000186 | prose | pages [8] -->
where 𝑚𝑖(𝑡) is match number. 𝑃𝑖𝑗(𝑡) is calculated through

<!-- b000187 | prose | pages [8] -->


<!-- b000188 | prose | pages [8] -->
𝑃𝑖𝑗(𝑡) =

<!-- b000189 | prose | pages [8] -->
1 + 10

<!-- b000190 | prose | pages [8] -->
−1

<!-- b000191 | prose | pages [8] -->
(𝐸𝑗(𝑡)−𝐸𝑖(𝑡))

<!-- b000192 | prose | pages [8] -->
(3)

<!-- b000193 | prose | pages [8] -->
400

<!-- b000194 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000195 | prose | pages [8] -->
which matches our intuition. When 𝐸𝑗(𝑡) < 𝐸𝑖(𝑡) and 𝐸𝑗(𝑡) −𝐸𝑖(𝑡) decreases, indicating a rising competence of the 𝑖𝑡ℎplayer over the 𝑗𝑡ℎplayer, the winning probability 𝑃𝑖𝑗increases.

<!-- b000196 | prose | pages [8] -->
Probability of Winning the First Point 5.2

<!-- b000197 | prose | pages [8] -->
To track the performance of the players, the win probability of the first point is calculated. We take the independent and identically distributed (IID) assumption and use 𝑃𝑖𝑗to reverse calculate the probability of the pre-match serving side winning the first point. The probability of securing the initial serving/receiving point in a match, represented as 𝑝0/𝑝0 −𝜀(𝜀= 0.25 for men athletes and = 0.15 for women athletes, according to previous research led by Machar Reid), are assumed to be the same as the probability of winning any subsequent serving/receiving point

<!-- b000198 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000199 | prose | pages [8] -->
prior to the beginning of the match. The probability of winning the upcoming point, ˆ𝑝(𝑆𝑚), will be recalculated after the conclusion of the first points as they occur. In mathematical terms, we aim to solve for 𝑝0 through

<!-- b000200 | prose | pages [8] -->
𝑓0(𝑝0, 𝑞0) = 𝑃𝑖𝑗 (4)

<!-- b000201 | prose | pages [8] -->
where 𝑞0 = 1 −𝑝0. The figure below indicates the progression of scores in a tennis game for a server (if receiver, 𝑝𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑟

<!-- b000202 | prose | pages [8] -->
= 𝑝0 −𝜀and 𝑞𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑟 0

<!-- b000203 | prose | pages [8] -->
0 = 1 −𝑝0 + 𝜀).

<!-- b000204 | caption | pages [8] -->
Figure 3: Progression of scores in a tennis game for a server

<!-- b000205 | prose | pages [8] -->
The following algorithm demonstrates the computation of 𝑓0(𝑝0, 1 −𝑝0), which is entirely based on probability. The pseudocode below outlines the calculation of match-winning probability.

<!-- b000206 | furniture | pages [8] -->
关注数学模型

<!-- b000207 | furniture | pages [8] -->
2

<!-- b000208 | furniture | pages [8] -->
MATHmodels

<!-- b000209 | furniture | pages [8] -->
获取更多资讯

<!-- b000210 | furniture | pages [9] -->
Team # 2406176

<!-- b000211 | furniture | pages [9] -->
Page 9 of 27

<!-- b000212 | heading | pages [9] -->
Algorithm 1 Probability of Winning a Tennis Match

<!-- b000213 | prose | pages [9] -->
Data: Player A’s and Player B’s probability of winning the first point 𝑝𝐴

<!-- b000214 | prose | pages [9] -->
0 , 𝑝𝐵 0 as servers

<!-- b000215 | heading | pages [9] -->
Result: Probability of Player A winning the match 𝑃𝑖𝑗

<!-- b000216 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000217 | prose | pages [9] -->
begin

<!-- b000218 | prose | pages [9] -->
0 )4 + 4(𝑝𝐴 20(𝑝𝐴 0 )5(1−𝑝𝐴 0 )3 0 )2 + 0 ) + 10(𝑝𝐴

<!-- b000219 | prose | pages [9] -->
Calculate 𝑝𝐺𝐴= (𝑝𝐴

<!-- b000220 | prose | pages [9] -->
0 )4(1 −𝑝𝐴

<!-- b000221 | prose | pages [9] -->
0 )4 + 4(𝑝𝐵

<!-- b000222 | prose | pages [9] -->
0 )4(1 −𝑝𝐴

<!-- b000223 | prose | pages [9] -->
0 ) ; 0 (1−𝑝𝐴 1−2𝑝𝐴

<!-- b000224 | prose | pages [9] -->
20(𝑝𝐵 0 )5(1−𝑝𝐵 0 )3 0 )2 + 0 ) + 10(𝑝𝐵

<!-- b000225 | prose | pages [9] -->
Calculate 𝑝𝐺𝐵= (𝑝𝐵

<!-- b000226 | prose | pages [9] -->
0 )4(1 −𝑝𝐵

<!-- b000227 | prose | pages [9] -->
Set 𝑝𝑅= 1 −𝑝𝐺𝐴; Set 𝑞𝐺𝐴= 1 −𝑝𝐺𝐴; Set 𝑞𝐺𝐵= 1 −𝑝𝐺𝐵; Calculate 𝑝𝑆𝐴(6, 0) = (𝑝𝐺𝐴· 𝑞𝐺𝐵)3;

<!-- b000228 | prose | pages [9] -->
0 )4(1 −𝑝𝐵

<!-- b000229 | prose | pages [9] -->
0 ) ; 0 (1−𝑝𝐵 1−2𝑝𝐵

<!-- b000230 | prose | pages [9] -->
Calculate 𝑝𝑆𝐴(6, 1) = 3 · (𝑝𝐺𝐴)3 · 𝑞𝐺𝐴· (𝑞𝐺𝐵)3 + 3 · (𝑝𝐺𝐴)4 · 𝑝𝐺𝐵· (𝑞𝐺𝐵)2; Calculate 𝑝𝑆𝐴(6, 2) = 12 · (𝑝𝐺𝐴)5 · (𝑞𝐺𝐴)2 · 𝑝𝐺𝐵· 𝑞𝐺𝐵+ 10 · (𝑝𝐺𝐴)6 · (𝑝𝐺𝐵)2 · 𝑞𝐺𝐵; Calculate 𝑝𝑆𝐴(6, 3) = 60 · (𝑝𝐺𝐴)7 · (𝑞𝐺𝐴) · (𝑝𝐺𝐵)2 + 15 · (𝑝𝐺𝐴)8 · 𝑝𝐺𝐵; Calculate 𝑝𝑆𝐴(6, 4) = 360 · (𝑝𝐺𝐴)9 · 𝑝𝐺𝐵;

<!-- b000231 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000232 | prose | pages [9] -->
Calculate 𝑝𝑆𝐴(6, 5) = 720 · (𝑝𝐺𝐴)10; Calculate 𝑃𝑖𝑗= 𝑓0(𝑝0, 1 −𝑝0) = 𝑝𝑆𝐴(6, 0) + 𝑝𝑆𝐴(6, 1) + 𝑝𝑆𝐴(6, 2) + 𝑝𝑆𝐴(6, 3) + 𝑝𝑆𝐴(6, 4) +

<!-- b000233 | prose | pages [9] -->
𝑝𝑆𝐴(6, 5); return 𝑃𝑖𝑗;

<!-- b000234 | prose | pages [9] -->
end

<!-- b000235 | prose | pages [9] -->
This pseudocode outlines the steps to calculate the probability of Player A winning a tennis match based on the given game probabilities. Explanations of the symbols are:

<!-- b000236 | prose | pages [9] -->
• 𝑝𝐺𝑋: The probability that Player X wins a game when serving, X=A or B.

<!-- b000237 | prose | pages [9] -->
• 𝑝𝑅: The probability that Player B wins a game when receiving, i.e. 𝑝𝑅= 1 −𝑝𝐺𝐴.

<!-- b000238 | prose | pages [9] -->
• 𝑞𝐺𝑋: The probability that player X loses a game when serving, X=A or B, i.e. 𝑞𝐺𝐴= 1−𝑝𝐺𝐴.

<!-- b000239 | prose | pages [9] -->
• 𝑝𝑆𝐴(6, 𝑘): The probability that Player A wins a set with a score of 6-k, where k=0,1,2,3,4,5.

<!-- b000240 | prose | pages [9] -->
• 𝑃𝑖𝑗: The probability that Player A wins the match.

<!-- b000241 | prose | pages [9] -->
We plot the relationshipbetween 𝑃𝑖𝑗and 𝑝0. FromFigure 4 wecan see that 𝑃𝑖𝑗is amonotonically increasing function, thus we apply the dichotomy method to calculate 𝑝0.

<!-- b000242 | prose | pages [9] -->
Therefore, for a given 𝑃𝑖𝑗, the probability of winning the first point can be obtained and applied in the dynamic algorithm updating the probability of winning the next point below.

<!-- b000243 | prose | pages [9] -->
Dynamic Computation of the Subsequent Points’ Win Probabilities 5.3

<!-- b000244 | prose | pages [9] -->
Once we determine the first point’s win probability, we proceed to compute the win probability for the next point. We propose an efficient method to update the winning probability of both

<!-- b000245 | furniture | pages [9] -->
关注数学模型

<!-- b000246 | furniture | pages [9] -->
2

<!-- b000247 | furniture | pages [9] -->
MATHmodels

<!-- b000248 | furniture | pages [9] -->
获取更多资讯

<!-- b000249 | furniture | pages [10] -->
Team # 2406176

<!-- b000250 | furniture | pages [10] -->
Page 10 of 27

<!-- b000251 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000252 | caption | pages [10] -->
Figure 4: Relationship between 𝑃𝑖𝑗and 𝑝0

<!-- b000253 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000254 | prose | pages [10] -->
players in the next point through the equation below, considering the strong zero-sum game property of tennis

<!-- b000255 | prose | pages [10] -->
𝑠= ˆ𝑝𝐴𝑠(𝑆𝑚) if A is server and B is receiver

<!-- b000256 | prose | pages [10] -->
𝑝𝐴

<!-- b000257 | prose | pages [10] -->


<!-- b000258 | prose | pages [10] -->
PA(𝑡) =

<!-- b000259 | prose | pages [10] -->
(5)

<!-- b000260 | prose | pages [10] -->
𝑟= 1 −ˆ𝑝𝐵𝑠(𝑆𝑚) if A is receiver and B is server

<!-- b000261 | prose | pages [10] -->
𝑝𝐴

<!-- b000262 | prose | pages [10] -->


<!-- b000263 | prose | pages [10] -->
where PA(𝑡) is player A’s probability of winning the next point, 𝑝𝐴

<!-- b000264 | prose | pages [10] -->
𝑠/𝑝𝐴

<!-- b000265 | prose | pages [10] -->
𝑟is the probability of A winning the next point as a server/receiver. Therefore the model only requires an updating rule for the server’s probability of winning the next point. We applied the Quasi-Binomial Estimator

<!-- b000266 | prose | pages [10] -->
ˆ𝑝𝑠(𝑆𝑚) = 𝜂(𝑆𝑚) × 𝑝0 + (1 −𝜂(𝑆𝑚)) × ¯𝑝𝑠(𝑆𝑚) (6)

<!-- b000267 | prose | pages [10] -->
where ˆ𝑝𝑠(𝑆𝑚) is the probability of winning the next point for a server, ¯𝑝𝑠(𝑆𝑚) denotes the mean number of points won on serve through the 𝑛𝑡ℎpoint of the match given a scoreline of 𝑆𝑚. 𝜂(𝑆𝑚) is a dynamic weight that reflects in-match performance, varying between 0 and 1. Setting it to a constant 1 makes ˆ𝑝𝑠(𝑆𝑚) = 𝑝0, effectively disregarding in-match performance. Consequently, momentum, which is influenced by the flow of points within the match, ceases to be a factor as it no longer affects the win probability of subsequent points. 𝑝0 is the probability of winning the first point as stated in the section above. The parameter 𝜂(𝑆𝑚) balances the pre-match and in-match serve information, with larger 𝜂(𝑆𝑚) values placing more emphasis on pre-match serve expectations. 𝜂(𝑆𝑚) is calculated by

<!-- b000268 | prose | pages [10] -->
𝜂(𝑆𝑚) = 𝛼/(𝛼+ 𝑛) (7)

<!-- b000269 | prose | pages [10] -->
where 𝑛represents the number of points played on serve by the current player, while 𝛼is proportional to 𝜂and represents the pre-match confidence in a player’s serving performance, quantifying the in-match evidence needed to revise these pre-match expectations. We aim to optimize 𝑛𝑠and 𝑛𝑟to

<!-- b000270 | furniture | pages [10] -->
关注数学模型

<!-- b000271 | furniture | pages [10] -->
2

<!-- b000272 | furniture | pages [10] -->
MATHmodels

<!-- b000273 | furniture | pages [10] -->
获取更多资讯

<!-- b000274 | furniture | pages [11] -->
Team # 2406176

<!-- b000275 | furniture | pages [11] -->
Page 11 of 27

<!-- b000276 | prose | pages [11] -->
minimize inconsistencies between dynamic and pre-match serve expectations, as well as the error between observed and dynamic expectations, by minimizing a specific loss function

<!-- b000277 | prose | pages [11] -->
𝐿𝑜𝑠𝑠(𝑛) = −1

<!-- b000278 | prose | pages [11] -->
(𝑦𝑖log( ¯𝑝𝑠(𝑆𝑖)) + (1 −𝑦𝑖) log(1 −¯𝑝𝑠(𝑆𝑖))) + ( ¯𝑝𝑠(𝑆𝑖) −𝑝0)2

<!-- b000279 | prose | pages [11] -->


<!-- b000280 | prose | pages [11] -->
∑︁

<!-- b000281 | prose | pages [11] -->
𝜆𝑖

<!-- b000282 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000283 | prose | pages [11] -->
𝑚

<!-- b000284 | prose | pages [11] -->
𝑖

<!-- b000285 | prose | pages [11] -->
(8)

<!-- b000286 | prose | pages [11] -->
where 𝑦𝑖represents the number of points a server has won out of 𝑚service points. In any game, an athlete’s performance in the moment of the game is more indicative of subsequent performance than performance early in the game. Therefore the dynamic weight 𝜆𝑖is calculated as

<!-- b000287 | prose | pages [11] -->
𝜆𝑖= 𝑖

<!-- b000288 | prose | pages [11] -->
(9)

<!-- b000289 | prose | pages [11] -->
Í𝑚

<!-- b000290 | prose | pages [11] -->
𝑖=1 𝑖

<!-- b000291 | prose | pages [11] -->
We take the match between Carlos and Nicolas for instance, and the result is shown in the figure below.

<!-- b000292 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000293 | caption | pages [11] -->
Figure 5: Real-time changes in Carlos’s and Nicolas’s next point winning probability

<!-- b000294 | prose | pages [11] -->
The figure clearly indicates a significant serving side advantage, which must be factored into player performance assessments. A server with a 51% win probability isn’t necessarily performing better than a receiver with a 49% win rate. Therefore, it is necessary to further eliminate this advantage.

<!-- b000295 | prose | pages [11] -->
5.4 Quantification of Momentum

<!-- b000296 | prose | pages [11] -->
With the win probability in real time, we are capable of acquiring the player’s performance in real time

<!-- b000297 | prose | pages [11] -->
(

<!-- b000298 | prose | pages [11] -->
PA(𝑡) −𝑝𝐴

<!-- b000299 | prose | pages [11] -->
MMTA(𝑡) =

<!-- b000300 | prose | pages [11] -->
PA(𝑡) −𝑝𝐴 0 , if A is server

<!-- b000301 | prose | pages [11] -->
(10) 0 + 𝜀, if A is receiver

<!-- b000302 | prose | pages [11] -->
The real-time performance for Carlos and Nicolas in their matchup is indicated below.

<!-- b000303 | furniture | pages [11] -->
关注数学模型

<!-- b000304 | furniture | pages [11] -->
2

<!-- b000305 | furniture | pages [11] -->
MATHmodels

<!-- b000306 | furniture | pages [11] -->
获取更多资讯

<!-- b000307 | furniture | pages [12] -->
Team # 2406176

<!-- b000308 | furniture | pages [12] -->
Page 12 of 27

<!-- b000309 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000310 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000311 | caption | pages [12] -->
Figure 6: Real-time momentum of Carlos and Nicolas

<!-- b000312 | prose | pages [12] -->
Carlos’s momentum curve shows more distinct peaks than Nicolas’s, indicating that Carlos’s performance is often significantly higher than his pre-match predictions compared to Nicolas’s, especially in the middle of the game where Carlos’s momentum peaks are almost exclusive (between point #100 and #200). This suggests that Carlos has a strong momentum that helps him dominate the game during mid-match, which ultimately contributes to winning the match.

<!-- b000313 | prose | pages [12] -->
5.4.1

<!-- b000314 | heading | pages [12] -->
Verification of the Significance of Momentum

<!-- b000315 | prose | pages [12] -->
To assess the role of momentum in tennis, we apply the Constant Win Probability (CWP) model by setting 𝜂(𝑆𝑚) = 1 in the Real-Time Win Probability (RTWP) model, thereby disregarding all in-match factors including momentum. We then consider the outcome of the CWP model as our observed value. If the coach’s assertion is incorrect, the residuals (the differences between the predicted and observed outcomes) would deviate from a normal distribution, indicating a discrepancy between the models and the observed results. We employ both qualitative (probability distribution plots of the residuals) and quantitative (K-S test) methods to evaluate the validity of the coach’s hypothesis. If the coach’s claim is disproven, it confirms the existence and significance of momentum in tennis matches, thereby validating the effectiveness of our RTWP and RTMQ models.

<!-- b000316 | prose | pages [12] -->
Probability Distribution Plot of the Residuals

<!-- b000317 | prose | pages [12] -->
We plot the distribution of the residual in the figure 7 below.

<!-- b000318 | prose | pages [12] -->
This clearly suggests a non-normal distribution, since the mean values of 𝜎are all larger than 0 and it is not distributed centrally symmetric, prompting us to use the K-S test for further investigation of the residuals’ distribution.

<!-- b000319 | furniture | pages [12] -->
关注数学模型

<!-- b000320 | furniture | pages [12] -->
2

<!-- b000321 | furniture | pages [12] -->
MATHmodels

<!-- b000322 | furniture | pages [12] -->
获取更多资讯

<!-- b000323 | furniture | pages [13] -->
Team # 2406176

<!-- b000324 | furniture | pages [13] -->
Page 13 of 27

<!-- b000325 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000326 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000327 | caption | pages [13] -->
Figure 7: Probability distribution of the residual of Carlos Alcaraz and Nicolas Jarry

<!-- b000328 | prose | pages [13] -->
K-S Test to Investigate the Distribution

<!-- b000329 | prose | pages [13] -->
In this case, the Null Hypothesis (H0) is the coach’s statement that momentum does not play any role in the match. If H0 is true, then the residual should be close to a normal distribution. The pseudocode for K-S Test is shown below.

<!-- b000330 | heading | pages [13] -->
Algorithm 2 Kolmogorov-Smirnov (K-S) Test

<!-- b000331 | prose | pages [13] -->
Data: Residuals 𝜎

<!-- b000332 | heading | pages [13] -->
Result: K-S test statistic 𝐷, p-value 𝑝

<!-- b000333 | prose | pages [13] -->
begin

<!-- b000334 | prose | pages [13] -->
Sort the residuals 𝜎in ascending order;

<!-- b000335 | prose | pages [13] -->
Set 𝑁as the number of residuals; for 𝑖←1 to 𝑁do

<!-- b000336 | prose | pages [13] -->
Calculate 𝐷+ = max(𝑖/𝑁−𝜎[𝑖−1]);

<!-- b000337 | prose | pages [13] -->
Calculate 𝐷−= max(𝜎[𝑖−1] −(𝑖−1)/𝑁);

<!-- b000338 | prose | pages [13] -->
end

<!-- b000339 | prose | pages [13] -->
√

<!-- b000340 | prose | pages [13] -->
√

<!-- b000341 | prose | pages [13] -->
Calculate 𝐷= max(

<!-- b000342 | prose | pages [13] -->
𝑁· 𝐷+,

<!-- b000343 | prose | pages [13] -->
𝑁· 𝐷−);

<!-- b000344 | prose | pages [13] -->
𝑖=1(−1)𝑖−1𝑒−2𝑖2𝐷2;

<!-- b000345 | prose | pages [13] -->
Calculate 𝑝= 1 −2 Í∞

<!-- b000346 | prose | pages [13] -->
return 𝐷, 𝑝;

<!-- b000347 | prose | pages [13] -->
end

<!-- b000348 | prose | pages [13] -->
Running the K-S test as introduced in the pseudocode above, using statistical software, results are shown in table 3 below. The p-value for both players is much smaller than 0.05 (the common chosen significance level). Therefore, we reject the H0 hypothesis and confirm the significance of momentum in tennis matches.

<!-- b000349 | furniture | pages [13] -->
关注数学模型

<!-- b000350 | furniture | pages [13] -->
2

<!-- b000351 | furniture | pages [13] -->
MATHmodels

<!-- b000352 | furniture | pages [13] -->
获取更多资讯

<!-- b000353 | furniture | pages [14] -->
Team # 2406176

<!-- b000354 | furniture | pages [14] -->
Page 14 of 27

<!-- b000355 | caption | pages [14] -->
Table 3: Significant symbols in this paper

<!-- b000356 | prose | pages [14] -->
𝐷Value

<!-- b000357 | prose | pages [14] -->
Carlos

<!-- b000358 | prose | pages [14] -->
𝑝value

<!-- b000359 | prose | pages [14] -->
1.338386540467465e-62 << 0.05

<!-- b000360 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000361 | prose | pages [14] -->
0.49958267649880644 Nicolas 0.47375107203988065 5.94542201790284e-56 << 0.05

<!-- b000362 | prose | pages [14] -->
Momentum Trend Value (MMTTV) Visualization 5.5

<!-- b000363 | prose | pages [14] -->
Considering the volatility and periodicity of the real-time momentum curve, we apply Fourier series to fit the curve to eliminate the effects of cyclical fluctuations in win probabilities, acquiring the momentum trend value (MMTTV) in real time. Fourier series is a powerful mathematical tool that can be used to represent and analyze periodic functions. It describes a periodic function as a sum of sine and cosine functions. The general form of a Fourier series is

<!-- b000364 | prose | pages [14] -->
∞

<!-- b000365 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000366 | prose | pages [14] -->
∑︁

<!-- b000367 | prose | pages [14] -->
[𝑎𝑛cos(𝑛𝑤𝑥) + 𝑏𝑛sin(𝑛𝑤𝑥)]

<!-- b000368 | prose | pages [14] -->
𝑓(𝑥) = 𝑎0 +

<!-- b000369 | prose | pages [14] -->
𝑛=1

<!-- b000370 | prose | pages [14] -->
(11)

<!-- b000371 | prose | pages [14] -->
Applying Fourier series curve fitting to our real-time momentum data, we finally capture the momentum trend and obtain the MMTTV data for both athletes, which is the blue line in the figure below.

<!-- b000372 | caption | pages [14] -->
Figure 8: The momentum trend value for both players

<!-- b000373 | prose | pages [14] -->
It is easy to see from the figure that a dramatic momentum shift occurred near point #130, when Carlos’ momentum reached over 0.23 and Nicolas’ momentum dropped to about 0.06, turning the situation around and leading to the swing. The final success of Carlos is therefore closely related to this momentum shift, and subsequent sustained rises in Nicolas’ momentum did not positively affect his final result.

<!-- b000374 | furniture | pages [14] -->
关注数学模型

<!-- b000375 | furniture | pages [14] -->
2

<!-- b000376 | furniture | pages [14] -->
MATHmodels

<!-- b000377 | furniture | pages [14] -->
获取更多资讯

<!-- b000378 | furniture | pages [15] -->
Team # 2406176

<!-- b000379 | prose | pages [15] -->
6

<!-- b000380 | heading | pages [15] -->
Swing Prediction Model

<!-- b000381 | prose | pages [15] -->
6.1 Data Preprocessing

<!-- b000382 | furniture | pages [15] -->
Page 15 of 27

<!-- b000383 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000384 | prose | pages [15] -->
In the Wimbledon_featured_matches.csv, columns AQ(speed_mph), AR(serve_width), AS (serve_depth), AT(return_depth) have missing values (NA). They are handled as follows:

<!-- b000385 | prose | pages [15] -->
Step 1: Address missing values in columns AR, AS, AT.

<!-- b000386 | prose | pages [15] -->
• If either column AB or AC in a row is 1, replace NA in columns AR, AS, AT of these rows with ’F’ (Fail). This is because columns AB and AC represent points lost due to player errors. We assume that the NA values in these cases are unclassified results caused by errors.

<!-- b000387 | prose | pages [15] -->
• If any of the columns U, V, W, X in a row is 1, replace NA in columns AR, AS, AT of these rows with ’UN’ (Unknown). Columns U, V, W, X represent points scored due to high-quality shots (serve/return), with NA values attributed to unknown factors.

<!-- b000388 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000389 | prose | pages [15] -->
Step 2: Address missing values in column AQ .

<!-- b000390 | prose | pages [15] -->
• Exclude the matches between Daniel Elahi Galan and Mikael Ymer, and between Guido Pella and Roman Safiullin. This is because ball speed and rally count are both crucial technical indicator in tennis, and these matches lack the two records.

<!-- b000391 | prose | pages [15] -->
• If any of the columns U, V, W, X, AB, AC, AD, AE, AF, AG in a row is 1, replace the NA in column AQ with the average ball speed of the match. This is because the absence of ball speed data for high-quality shots, error shots, and net shots may be due to errors in the data recording process or factors that make the data unrecordable.

<!-- b000392 | prose | pages [15] -->
6.2 Indicators Calculation

<!-- b000393 | prose | pages [15] -->
Key indicators are calculated based on previous research and experience. We have identified 25 indicators based on the mainstream technical indicators in tennis, related scientific research papers and professional analysis. Due to their excessive number, our paper shows the calculation of only 3 of the indicators, the calculation and explanation of all indicators is in Appendix A.

<!-- b000394 | prose | pages [15] -->
n(ace) Aces_p𝑖= n(successful serves)

<!-- b000395 | prose | pages [15] -->
Break_p𝑖= n(server = 𝑗, break_pt_won = 𝑖)

<!-- b000396 | prose | pages [15] -->
n(server = 𝑗, break_pt = 1)

<!-- b000397 | prose | pages [15] -->
(12)

<!-- b000398 | prose | pages [15] -->
n(server = 𝑖, serve_depth = 𝐶𝑇𝐿) Depth_CTL_p𝑖= n(server = 𝑖, serve_depth ≠unknown) ...

<!-- b000399 | prose | pages [15] -->
where Aces_p𝑖represents the proportion of successful serves by player 𝑖that are aces, Break_p𝑖rep- resents the proportion of break points won by player 𝑖when player 𝑗is serving, and Depth_CTL_p𝑖 represents the proportion of serves by player 𝑖that land in the “CTL” (Close To Line) depth zone.

<!-- b000400 | furniture | pages [15] -->
关注数学模型

<!-- b000401 | furniture | pages [15] -->
2

<!-- b000402 | furniture | pages [15] -->
MATHmodels

<!-- b000403 | furniture | pages [15] -->
获取更多资讯

<!-- b000404 | furniture | pages [16] -->
Team # 2406176

<!-- b000405 | prose | pages [16] -->
6.3 Exploratory Factor Analysis

<!-- b000406 | furniture | pages [16] -->
Page 16 of 27

<!-- b000407 | prose | pages [16] -->
Given the multitude of performance indicators for a player, we use a Factor Analysis Model to distill key factors that better represent the player’s technical performance. Therefore, all indicators

<!-- b000408 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000409 | prose | pages [16] -->
can be quantified by the factors with the corresponding weights. Let 𝑋𝑝(𝑝= 1, 2, ..., 25) represent all indicators, and they can be represented by weighted factors as follows

<!-- b000410 | prose | pages [16] -->
𝛼11 𝛼12

<!-- b000411 | prose | pages [16] -->
𝜇1

<!-- b000412 | prose | pages [16] -->
𝑋1

<!-- b000413 | prose | pages [16] -->


<!-- b000414 | prose | pages [16] -->


<!-- b000415 | prose | pages [16] -->


<!-- b000416 | prose | pages [16] -->


<!-- b000417 | prose | pages [16] -->


<!-- b000418 | prose | pages [16] -->
𝛼21 𝛼22

<!-- b000419 | prose | pages [16] -->
𝜇2

<!-- b000420 | prose | pages [16] -->
𝑋2

<!-- b000421 | prose | pages [16] -->
...

<!-- b000422 | prose | pages [16] -->
...

<!-- b000423 | prose | pages [16] -->
...

<!-- b000424 | prose | pages [16] -->
...

<!-- b000425 | prose | pages [16] -->
+

<!-- b000426 | prose | pages [16] -->
=

<!-- b000427 | prose | pages [16] -->
𝛼𝑝1 𝛼𝑝2

<!-- b000428 | prose | pages [16] -->
𝜇𝑝

<!-- b000429 | prose | pages [16] -->
𝑋𝑝

<!-- b000430 | prose | pages [16] -->
𝜀1

<!-- b000431 | prose | pages [16] -->
𝐹1

<!-- b000432 | prose | pages [16] -->
𝛼1𝑚 · · ·

<!-- b000433 | prose | pages [16] -->


<!-- b000434 | prose | pages [16] -->


<!-- b000435 | prose | pages [16] -->


<!-- b000436 | prose | pages [16] -->


<!-- b000437 | prose | pages [16] -->


<!-- b000438 | prose | pages [16] -->
𝜀2

<!-- b000439 | prose | pages [16] -->
𝐹2

<!-- b000440 | prose | pages [16] -->
𝛼2𝑚 · · ·

<!-- b000441 | prose | pages [16] -->
...

<!-- b000442 | prose | pages [16] -->
...

<!-- b000443 | prose | pages [16] -->
...

<!-- b000444 | prose | pages [16] -->
+

<!-- b000445 | prose | pages [16] -->
(13)

<!-- b000446 | prose | pages [16] -->
𝜀𝑝

<!-- b000447 | prose | pages [16] -->
𝐹𝑚

<!-- b000448 | prose | pages [16] -->
𝛼𝑝𝑚 · · ·

<!-- b000449 | prose | pages [16] -->
where 𝐹1, 𝐹2, ..., 𝐹𝑚are factors that are unobservable, 𝛼𝑖𝑗is the weight matrix of the factors, 𝜇𝑖 is the mean of the variable 𝑋𝑖and 𝜀𝑖is the unique or error term for the variable 𝑋𝑖. The constraints of the model are

<!-- b000450 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000451 | prose | pages [16] -->
𝑐𝑜𝑣(𝐹, 𝜀) = 0, 𝐷(𝐹𝑖) = 1, 𝐷(𝜀𝑖) = 𝜎2

<!-- b000452 | prose | pages [16] -->
(14) 𝑖

<!-- b000453 | prose | pages [16] -->
Indicators undergo z-score normalization to normalize their scale and mitigate the effect of different units or magnitudes prior to factor analysis. We perform a Bartlett’s Test of Sphericity to determine if there is a high degree of internal correlation in the data. If so, factor analysis is performed.

<!-- b000454 | heading | pages [16] -->
Algorithm 3 Bartlett’s Test of Sphericity

<!-- b000455 | prose | pages [16] -->
Data: Indicator matrix X Result: Test statistic, p-value, and a decision on whether the data need to be factor analyzed begin

<!-- b000456 | prose | pages [16] -->
𝜒2 = −log(det(𝑅))(𝑁−1 −2𝑛+5

<!-- b000457 | prose | pages [16] -->
6 ) where 𝑅is the correlation matrix of the dataset, 𝑁= 109 (number of data points), 𝑛= 25;

<!-- b000458 | prose | pages [16] -->
𝜒2, 𝑝(𝑝+1)

<!-- b000459 | prose | pages [16] -->


<!-- b000460 | prose | pages [16] -->


<!-- b000461 | prose | pages [16] -->
𝑝= 1 −𝐹𝜒2

<!-- b000462 | prose | pages [16] -->
−1

<!-- b000463 | prose | pages [16] -->
;

<!-- b000464 | prose | pages [16] -->
2

<!-- b000465 | prose | pages [16] -->
if 𝑝< 0.05 then

<!-- b000466 | prose | pages [16] -->
The data is appropriate for factor analysis.; end else

<!-- b000467 | prose | pages [16] -->
The data is not appropriate for factor analysis.; end end

<!-- b000468 | prose | pages [16] -->
The test tells us 𝑝< 0.05, so we performed factor analysis. We extract five factors. Taking 3 factors as an example and looking at the factor loading matrix, we found:

<!-- b000469 | prose | pages [16] -->
• For Factor 1, Aces_p𝑖(0.754), 1st_srv_won_p𝑖(0.730), and Width_W_p𝑖(0.685) have the highest absolute factor loadings, which indicates that Factor 1 characterizes the player’s ability to win points and quality of play as a server. Since this factor is almost entirely related to server metrics, we treat Factor 1 as a factor specializing in server ability.

<!-- b000470 | furniture | pages [16] -->
关注数学模型

<!-- b000471 | furniture | pages [16] -->
2

<!-- b000472 | furniture | pages [16] -->
MATHmodels

<!-- b000473 | furniture | pages [16] -->
获取更多资讯

<!-- b000474 | furniture | pages [17] -->
Team # 2406176

<!-- b000475 | furniture | pages [17] -->
Page 17 of 27

<!-- b000476 | prose | pages [17] -->
• For Factor 2, Depth_CTL_p𝑖(0.792) and Net_pt_won_p𝑖(0.568) have the highest absolute factor loadings. As a result of our research, we found that when a player tends to hit a CTL ball, it is likely that the player will need to run longer distances faster to receive the ball. Thus Factor 2 characterizes whether the player tends to put more or less effort into the play.

<!-- b000477 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000478 | prose | pages [17] -->
• For Factor4, 1st_srv_drt_won_p𝑖(0.710), Winners4_p𝑖(-0.649), andSrv_avg_speed_p𝑖(0.632) have the highest absolute values of the factor loadings. Thus Factor 4 indicates the player’s explosive ability, especially the ability to win the ball in the serve-receive phase.

<!-- b000479 | prose | pages [17] -->
We name the Factor 1 as AggressiveServe, Factor 2 as ExtendedPlay, Factor 3 as Endurance, Factor 4 as ActiveDefense, and Factor 5 as ForehandBias based on the characteristics of the indicators they contain and the characteristics of the factor loading matrix.

<!-- b000480 | heading | pages [17] -->
Prediction of Swing Based on Multivariate Linear Regression Model

<!-- b000481 | prose | pages [17] -->
6.4

<!-- b000482 | prose | pages [17] -->
We utilize a Multivariate Linear Regression Model to predict tangible momentum shifts,

<!-- b000483 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000484 | prose | pages [17] -->
or swings, in tennis matches. Our model operates on a per-set basis, as a set provides a more comprehensive dataset for analysis compared to individual games. This approach minimizes the impact of outliers and enhances the reliability of the player’s performance evaluation. For instance, a shift from high to low momentum of two sets often indicates a potential swing (tends to lose the game or even match). We sample the momentum trend value (MMTTV) from the momentum trend at the end of each set. This is because the frequent in-set momentum shifts can render predictions based on real-time momentum data at the end of each set unreliable. By calculating the MMTTV values and other metrics at the end of each set, we align our methodology with previous research and established analytical strategies in sports media, thereby ensuring a robust prediction of momentum shifts. The subsequent section outlines the training process for the multivariate linear regression model that can be executed across numerous software platforms.

<!-- b000485 | heading | pages [17] -->
Algorithm 4 Multivariate Linear Regression

<!-- b000486 | prose | pages [17] -->
Data: Factor matrix (the 5 factors) X, Target vector MMTTV at the end of each set

<!-- b000487 | heading | pages [17] -->
Result: Coefficients of the 5 factors 𝛽, Predictions

<!-- b000488 | prose | pages [17] -->
begin ˆ MMTTV

<!-- b000489 | prose | pages [17] -->
Initialize coefficients 𝛽for each feature in X to 0;

<!-- b000490 | prose | pages [17] -->
Set learning rate 𝛼and convergence threshold 𝜖;

<!-- b000491 | prose | pages [17] -->
while not converged do

<!-- b000492 | prose | pages [17] -->
ˆ ˆ 1 MMTTV = Calculate the predicted probabilities Calculate the gradient 𝑘= X𝑇( ˆ 1+𝑒−X𝛽; MMTTV −MMTTV); Update coefficients 𝛽= 𝛽−𝛼𝑘; If ||𝑘|| < 𝜖, set converged to True;

<!-- b000493 | prose | pages [17] -->
end return 𝛽, ˆ MMT;

<!-- b000494 | prose | pages [17] -->
end

<!-- b000495 | furniture | pages [17] -->
关注数学模型

<!-- b000496 | furniture | pages [17] -->
2

<!-- b000497 | furniture | pages [17] -->
MATHmodels

<!-- b000498 | furniture | pages [17] -->
获取更多资讯

<!-- b000499 | furniture | pages [18] -->
Team # 2406176

<!-- b000500 | furniture | pages [18] -->
Page 18 of 27

<!-- b000501 | prose | pages [18] -->
We take the match between Carlos and Nicolas for testing our prediction model, and the result is shown in the figure below, indicating an accurate prediction.

<!-- b000502 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000503 | caption | pages [18] -->
Figure 9: Prediction of the value of momentum for both players

<!-- b000504 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000505 | prose | pages [18] -->
The result agrees well with the real-time MMTTV of the two athletes, with the peak and trough in both figures occurring at the end of the second set. Sorting the weights of the factors, AggressiveServe have the largest absolute weights, indicating that they are the most related factors to predict the swings in the match. It is reasonable because serve ability and aggressiveness are the most central indicators of a good or bad server’s ability. From the figure below we can see the trend of the indicators are similar to that of the momentum curve.

<!-- b000506 | heading | pages [18] -->
Mixed-Strategy Nash Equilibrium Model

<!-- b000507 | prose | pages [18] -->
7

<!-- b000508 | prose | pages [18] -->
In the dynamic world of tennis, players strategically adopt different tactics with a certain probability during a match to maximize their chances of winning. The choice of strategy, whether for serving or receiving, can significantly affect the outcome of the game, creating a complex web of decisions. To analyze this intricate web of strategic choices, we have adopted a Mixed-Strategy Nash Equilibrium model. This model serves as a tool for predicting the most common combinations of strategies employed by players prior to the game. As the match unfolds, the model allows us to observe shifts in players’ strategies, providing valuable insights into which strategies a player must pursue to gain an upper hand. Through our model, we aim to unravel the probabilistic nature of strategic decision-making in tennis, paving the way for more informed and effective strategies.

<!-- b000509 | prose | pages [18] -->
7.1 Strategy Payoff Calculation

<!-- b000510 | prose | pages [18] -->
First we define the set of possible strategies that the opponent in the upcoming match (assume that we need to study Stefanos Tsitsipas) may adopt. The strategies of the players can be characterized by the factors we define previously. We compute the factor value at the end of each set in the dataset, followed by cluster analysis in unsupervised learning.

<!-- b000511 | prose | pages [18] -->
We tried clustering the dataset and found that the set of strategies makes the most sense when the number of clusters is 4 for the server and 3 for the receiver. Strategies that can be adopted by servers are as follows:

<!-- b000512 | prose | pages [18] -->
• Server Strategy 1: A=0.83, B=0.72, C=0.63, E=0.49. This indicates a steep angle and fast

<!-- b000513 | furniture | pages [18] -->
关注数学模型

<!-- b000514 | furniture | pages [18] -->
2

<!-- b000515 | furniture | pages [18] -->
MATHmodels

<!-- b000516 | furniture | pages [18] -->
获取更多资讯

<!-- b000517 | furniture | pages [19] -->
Team # 2406176

<!-- b000518 | furniture | pages [19] -->
Page 19 of 27

<!-- b000519 | prose | pages [19] -->
ball speed, therefore the strategy is named Side-Tearing Assault.

<!-- b000520 | prose | pages [19] -->
• Server Strategy 2: A=0.69, B=0.31, C=0.76, E=0.79. This describes the tendency of players to use a variety of stroke speeds, stroke angles, and different ball paths to control the pace of

<!-- b000521 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000522 | prose | pages [19] -->
play, thus named Pace Control.

<!-- b000523 | prose | pages [19] -->
• Server Strategy 3: A=0.25, B=0.66, C=0.87, E=0.69. This suggests that the player tends to play each point longer, and play faster, close-to-net balls, so that the opponent is forced to go to the net and might make a mistake, thus named Low-Bounce Onslaught.

<!-- b000524 | prose | pages [19] -->
• Server Strategy 4: A=0.44, B=0.52, C=0.55, E=0.54. This suggests that players adopt slower ball speeds and hit a lot of approach shots, which is easy to create errors for the opponent, thus named Short-Ball Maneuver.

<!-- b000525 | prose | pages [19] -->
For receiver strategies:

<!-- b000526 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000527 | prose | pages [19] -->
• Receiver Strategy 1 (Bottom Line Defense): With B=0.29, C=0.67, D=0.54, E=0.88, the player tends to conserve energy, engage in extended rallies, and favor forehand shots. This strategy, characterized by precise stroke and angle control from the baseline, is a common defensive approach.

<!-- b000528 | prose | pages [19] -->
• Receiver Strategy 2 (Defense at the Net): With B=0.73, C=0.21, D=0.61, E=0.46, the player prefers to conserve energy, end points quickly, and actively defend. This strategy often involves moving to the net to counter strong baseline attacks from the opponent.

<!-- b000529 | prose | pages [19] -->
• Receiver Strategy 3 (Deep Defense): With B=0.77, C=0.87, D=0.49, E=0.81, the receiver tends to play long points with a significant forehand bias. This strategy aims to provide the player with more reaction time and make it challenging for the opponent to execute an effective attack.

<!-- b000530 | prose | pages [19] -->
The values of each factor in all strategies are shown in figure 10 below.

<!-- b000531 | caption | pages [19] -->
Figure 10: The value of factors for strategies of both servers and receivers

<!-- b000532 | furniture | pages [19] -->
关注数学模型

<!-- b000533 | furniture | pages [19] -->
2

<!-- b000534 | furniture | pages [19] -->
MATHmodels

<!-- b000535 | furniture | pages [19] -->
获取更多资讯

<!-- b000536 | furniture | pages [20] -->
Team # 2406176

<!-- b000537 | furniture | pages [20] -->
Page 20 of 27

<!-- b000538 | prose | pages [20] -->
We incorporate the median value of each strategy cluster into our Swing Prediction Model to predict the MMT value for each corresponding strategy. This predicted value represents the exact payoff of the strategy and is used to calculate the expected payoffs below.

<!-- b000539 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000540 | prose | pages [20] -->
7.2

<!-- b000541 | heading | pages [20] -->
Model Setup

<!-- b000542 | prose | pages [20] -->
Mixed Strategies. A mixed strategy for player 𝑖is defined as a probability distribution over the set of pure strategies. Let 𝑛𝑖denote the number of pure strategies available to player 𝑖. A mixed strategy for player 𝑖(the player is a server or a receiver) can then be represented as a vector

<!-- b000543 | prose | pages [20] -->
p𝑖= (𝑝𝑖1, 𝑝𝑖2, ..., 𝑝𝑖𝑛𝑖) (15)

<!-- b000544 | prose | pages [20] -->
where 𝑝𝑖𝑗is the probability that player 𝑖will play pure strategy 𝑗. These probabilities are non- negative and sum to 1

<!-- b000545 | prose | pages [20] -->
𝑝𝑖𝑗≥0,

<!-- b000546 | prose | pages [20] -->
𝑛𝑖 ∑︁

<!-- b000547 | prose | pages [20] -->
𝑝𝑖𝑗= 1 (16)

<!-- b000548 | prose | pages [20] -->
𝑗=1

<!-- b000549 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000550 | prose | pages [20] -->
Expected Payoffs. The expected payoff for player 𝑖given a profile of mixed strategies p is calculated as the sum of the payoffs for each possible outcome, weighted by the probability of that outcome. If 𝑢𝑖(𝑠1, ..., 𝑠𝑛) denotes the payoff to player 𝑖for strategy profile (𝑠1, ..., 𝑠𝑛), the expected payoff is given by:

<!-- b000551 | prose | pages [20] -->
∑︁

<!-- b000552 | prose | pages [20] -->
∑︁

<!-- b000553 | prose | pages [20] -->
𝐸[𝑢𝑖(p)] =

<!-- b000554 | prose | pages [20] -->
...

<!-- b000555 | prose | pages [20] -->
𝑠1

<!-- b000556 | prose | pages [20] -->
𝑠𝑛

<!-- b000557 | prose | pages [20] -->
𝑛 Ö

<!-- b000558 | prose | pages [20] -->
𝑝𝑗𝑠𝑗

<!-- b000559 | prose | pages [20] -->
𝑢𝑖(𝑠1, ..., 𝑠𝑛)

<!-- b000560 | prose | pages [20] -->
(17)

<!-- b000561 | prose | pages [20] -->
𝑗=1

<!-- b000562 | prose | pages [20] -->
Best Responses. A best response for player 𝑖is a strategy that maximizes player 𝑖’s expected payoff, given the strategies of the other players. Formally, a best response p∗

<!-- b000563 | prose | pages [20] -->
p∗

<!-- b000564 | prose | pages [20] -->
𝑖satisfies

<!-- b000565 | prose | pages [20] -->
p𝑖𝐸[𝑢𝑖(p𝑖, p−𝑖)]

<!-- b000566 | prose | pages [20] -->
𝑖∈arg max

<!-- b000567 | prose | pages [20] -->
Nash Equilibrium.

<!-- b000568 | prose | pages [20] -->
(18)

<!-- b000569 | prose | pages [20] -->
A mixed-strategy Nash equilibrium is a strategy profile where every player’s strategy is a best response to the strategies of the other players. Formally, a strategy profile

<!-- b000570 | prose | pages [20] -->
𝑛) is a Nash equilibrium if and only if for all 𝑖 1, ..., p∗

<!-- b000571 | prose | pages [20] -->
p∗= (p∗

<!-- b000572 | prose | pages [20] -->
p𝑖𝐸[𝑢𝑖(p𝑖, p∗

<!-- b000573 | prose | pages [20] -->
p∗

<!-- b000574 | prose | pages [20] -->
𝑖∈arg max

<!-- b000575 | prose | pages [20] -->
−𝑖)] (19)

<!-- b000576 | prose | pages [20] -->
In other words, no player can improve their expected payoff by unilaterally deviating from their Bringing our strategies into the model, the probability combination of equilibrium strategy. strategies that our player should take to against Stefanos Tsitsipas is shown in figure 11 below.

<!-- b000577 | furniture | pages [20] -->
关注数学模型

<!-- b000578 | furniture | pages [20] -->
2

<!-- b000579 | furniture | pages [20] -->
MATHmodels

<!-- b000580 | furniture | pages [20] -->
获取更多资讯

<!-- b000581 | furniture | pages [21] -->
Team # 2406176

<!-- b000582 | furniture | pages [21] -->
Page 21 of 27

<!-- b000583 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000584 | caption | pages [21] -->
Figure 11: Optimized combination of strategies when S.T. is server and R.S. is receiver

<!-- b000585 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000586 | heading | pages [21] -->
Test of FSF Model and SP Model

<!-- b000587 | prose | pages [21] -->
8

<!-- b000588 | prose | pages [21] -->
After completing the construction of FSF and SP model, we used the data of other matches as a test set to verify the accuracy of our model’s predictive ability. Here we use the FSF model instead of the RTMQ model because we want to track the momentum trend without the frequent shifts in the RTMQ model.

<!-- b000589 | prose | pages [21] -->
The Match between Alcaraz and Djokovic 8.1

<!-- b000590 | prose | pages [21] -->
First, we selected one of the most exciting match, the Grand Slam championship match between the young Carlos Alcaraz and the veteran Novak Djokovic(The match number:1701). Inputting the point-by-point data into our model generate the MMTTV prediction. Fig.x demonstrates that, despite both players’ high levels, their MMTTVs closely overlapped, reflecting the match’s intensity. Analysis showed MMTTV aligned with the actual match: Djokovic led early, Alcaraz caught up, and Djokovic surged again before Alcaraz prevailed. This trend was consistent across multiple matches, confirming the model’s accuracy.

<!-- b000591 | caption | pages [21] -->
Figure 12: FSF model and SP model results

<!-- b000592 | furniture | pages [21] -->
关注数学模型

<!-- b000593 | furniture | pages [21] -->
2

<!-- b000594 | furniture | pages [21] -->
MATHmodels

<!-- b000595 | furniture | pages [21] -->
获取更多资讯

<!-- b000596 | furniture | pages [22] -->
Team # 2406176

<!-- b000597 | prose | pages [22] -->
8.2

<!-- b000598 | heading | pages [22] -->
Model Generalization

<!-- b000599 | furniture | pages [22] -->
Page 22 of 27

<!-- b000600 | prose | pages [22] -->
To assess our model’s generalization, we used men’s singles data from the 2017 French Open, which shares similarities with the 2023 Wimbledon Championships, including the best-of-five set

<!-- b000601 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000602 | prose | pages [22] -->
format and IBM Slamtracker data collection. Despite differences in court surfaces (red clay vs. grass), our model maintained prediction accuracy, indicating good generalization.

<!-- b000603 | prose | pages [22] -->
In particular, the match between Andy Murray and Andrey Kuznetsov highlighted the model’s reliability. Murray’s dominance, reflected in his MMTTV, aligned with our predictions and the match’s outcome, further confirming the model’s effectiveness.

<!-- b000604 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000605 | caption | pages [22] -->
Figure 13: FSF model and SP model results

<!-- b000606 | heading | pages [22] -->
Contextual Limitations in SP Model

<!-- b000607 | prose | pages [22] -->
8.3

<!-- b000608 | prose | pages [22] -->
When applying SP model to conduct MMTTV predictions and dynamic game strategy selec- tions, we observed that players balance their tactical strategies based on their own abilities and those of their opponents. Within a single match context (e.g., all matches in the 2023 Wimbledon Championships can be considered as having a consistent background), the model’s predictions are accurate. However, when generalizing the model to different match contexts, various factors such as the court’s impact on tennis ball bounce, climatic conditions influenced by the time of the season, and other contextual elements prevent us from directly unifying datasets from different matches to make sufficiently accurate predictions for a player facing a new opponent in a different match context. For instance, knowing Roman Safiullin’s performance data only from grass courts at Wimbledon makes it challenging to predict his strategic choices when playing on clay courts.

<!-- b000609 | heading | pages [22] -->
Key Indicators to be Included in Future Models

<!-- b000610 | prose | pages [22] -->
8.4

<!-- b000611 | prose | pages [22] -->
Beyond the generalization verification with the French Open dataset, we further discuss the model’s generalization potential. Given the rule differences between men’s and women’s singles tennis, extending our model to women’s singles or tournaments would require reconsidering the change from best-of-five to best-of-three sets. This necessitates rederiving the initial value cali- bration’s independent and identically distributed assumption. Extending the model to other racket sports with a net, such as table tennis, would involve redefining technical indicators based on rule variations and performing common factor analysis across different sports, incorporating relevant technical analyses.

<!-- b000612 | furniture | pages [22] -->
关注数学模型

<!-- b000613 | furniture | pages [22] -->
2

<!-- b000614 | furniture | pages [22] -->
MATHmodels

<!-- b000615 | furniture | pages [22] -->
获取更多资讯

<!-- b000616 | furniture | pages [23] -->
Team # 2406176

<!-- b000617 | furniture | pages [23] -->
Page 23 of 27

<!-- b000618 | prose | pages [23] -->
9

<!-- b000619 | heading | pages [23] -->
Sensitivity Analysis

<!-- b000620 | prose | pages [23] -->
We conduct a sensitivity analysis on our model to assess its stability under external distur- bances, thereby highlighting its advantages. As shown in Fig.x, when we alter the initial game

<!-- b000621 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000622 | prose | pages [23] -->
win probability as input, the overall trend prediction curve exhibited minimal translation despite significant deviations in the initial values. The stability of the curve trend remain intact, ensuring no impact on our MMT swing predictions. This demonstrates the strong robustness of our model.

<!-- b000623 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000624 | caption | pages [23] -->
Figure 14: Sensitivity analysis of MMT model

<!-- b000625 | furniture | pages [23] -->
关注数学模型

<!-- b000626 | furniture | pages [23] -->
2

<!-- b000627 | furniture | pages [23] -->
MATHmodels

<!-- b000628 | furniture | pages [23] -->
获取更多资讯

<!-- b000629 | furniture | pages [24] -->
Team # 2406176

<!-- b000630 | prose | pages [24] -->
To: Coaches

<!-- b000631 | prose | pages [24] -->
From: Team # 2406176

<!-- b000632 | prose | pages [24] -->
Date: Feb.5th, 2024

<!-- b000633 | furniture | pages [24] -->
Page 24 of 27

<!-- b000634 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000635 | heading | pages [24] -->
MEMO: Summary of Tennis Momentum Analysis and Coaching Recommendations

<!-- b000636 | prose | pages [24] -->
We are pleased to provide you with a summary of our recent research on tennis momentum dynamics and the development of predictive models.

<!-- b000637 | prose | pages [24] -->
Our research focuses on the Real-Time Momentum Quantification (RTMQ) Model, Swing Prediction (SP) Model, and the application of the Mixed-Strategy Nash Equilibrium Model in tennis matches.

<!-- b000638 | prose | pages [24] -->
Our findings suggest that momentum plays a significant role in tennis matches.

<!-- b000639 | prose | pages [24] -->
The RTMQ model quantifies momentum by considering the disparity between pre-match and real-time win probabilities. The model calculates the difference between real-time and pre-match win rates under

<!-- b000640 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000641 | prose | pages [24] -->
separate serve/receive conditions, taking into account the serving side’s advantage. The K-S test confirms the significance of momentum, rejecting the hypothesis that in-match performance is inconsequential.

<!-- b000642 | prose | pages [24] -->
The Swing Prediction (SP) Model operates on a per-set basis and exhibits an impressive 90.44% prediction accuracy for large momentum shifts.

<!-- b000643 | prose | pages [24] -->
The model uses specialized indicators, such as 2nd_serve_direct_won and Net_approach_point_won, to predict momentum swings.

<!-- b000644 | prose | pages [24] -->
These factors contribute significantly to player momentum and can be used to prepare players to respond effectively to events that impact the flow of play during a tennis match.

<!-- b000645 | prose | pages [24] -->
The Mixed-Strategy Nash Equilibrium Model provides insights into optimal strategic combinations against diverse opponents. The model uses K-means clustering to identify strategic clusters for tailored strategies. Coaches can use this model to prepare players to respond effectively to different opponents and adjust their strategies accordingly.

<!-- b000646 | prose | pages [24] -->
In conclusion, our research equips coaches with advanced tools and insights to navigate the intricate landscape of tennis momentum. Incorporating these findings into coaching strategies will enhance players’ ability to respond effectively to events impacting the flow of play, contributing to improved match outcomes. We recommend that coaches integrate these findings into their training programs to improve players’ responsiveness to dynamic events during matches.

<!-- b000647 | prose | pages [24] -->
Feel free to reach out for further discussion or clarification.

<!-- b000648 | prose | pages [24] -->
Best Regards,

<!-- b000649 | furniture | pages [24] -->
Team # 2406176

<!-- b000650 | furniture | pages [24] -->
关注数学模型

<!-- b000651 | furniture | pages [24] -->
2

<!-- b000652 | furniture | pages [24] -->
MATHmodels

<!-- b000653 | furniture | pages [24] -->
获取更多资讯

<!-- b000654 | furniture | pages [25] -->
Team # 2406176

<!-- b000655 | heading | pages [25] -->
References

<!-- b000656 | furniture | pages [25] -->
Page 25 of 27

<!-- b000657 | references | pages [25] -->
[1] Angelini, G.; Candila, V.; De Angelis, L. Weighted Elo Rating for Tennis Match

<!-- b000658 | references | pages [25] -->
Predictions. European Journal of Operational Research 2022,

<!-- b000659 | references | pages [25] -->
297 (1),

<!-- b000660 | references | pages [25] -->
120–132.

<!-- b000661 | references | pages [25] -->
微信公众号：数学模型

<!-- b000662 | references | pages [25] -->
https://doi.org/10.1016/j.ejor.2021.04.011.

<!-- b000663 | references | pages [25] -->
[2] Newton, P. K.; Keller, J. B. Probability of Winning at Tennis I. Theory and Data. Stud Appl

<!-- b000664 | references | pages [25] -->
Math 2005, 114 (3), 241–269. https://doi.org/10.1111/j.0022-2526.2005.01547.x.

<!-- b000665 | references | pages [25] -->
[3] Sarcevic, A.; Vranic, M.; Pintar, D.; Krajna, A. Predictive Modeling of Tennis Matches:

<!-- b000666 | references | pages [25] -->
A Review. In 2022 45th Jubilee International Convention on Information, Communica-

<!-- b000667 | references | pages [25] -->
tion and Electronic Technology (MIPRO); IEEE: Opatĳa, Croatia, 2022; pp 1099–1104.

<!-- b000668 | references | pages [25] -->
https://doi.org/10.23919/MIPRO55190.2022.9803645.

<!-- b000669 | references | pages [25] -->
[4] Newton, P. K.; Aslam, K. Monte Carlo Tennis: A Stochastic Markov Chain Model. Journal

<!-- b000670 | references | pages [25] -->
of Quantitative Analysis in Sports 2009, 5 (3). https://doi.org/10.2202/1559-0410.1169.

<!-- b000671 | references | pages [25] -->
微信号：MATHmodels

<!-- b000672 | references | pages [25] -->
[5] Dietl, H. M.; Nesseler, C. Momentum in Tennis: Controlling the Match.

<!-- b000673 | references | pages [25] -->
[6] Šarčević, A.; Pintar, D.; Vranić, M.; Gojsalić, A. Modeling In-Match Sports Dynam-

<!-- b000674 | references | pages [25] -->
ics Using the Evolving Probability Method. Applied Sciences 2021, 11 (10), 4429.

<!-- b000675 | references | pages [25] -->
https://doi.org/10.3390/app11104429.

<!-- b000676 | references | pages [25] -->
[7] Glass, A. J.; Kenjegalieva, K.; Taylor, J. Game, Set and Match:

<!-- b000677 | references | pages [25] -->
Evaluating the Ef-

<!-- b000678 | references | pages [25] -->
ficiency of Male Professional Tennis Players. J Prod Anal 2015, 43 (2), 119–131.

<!-- b000679 | references | pages [25] -->
https://doi.org/10.1007/s11123-014-0401-3.

<!-- b000680 | references | pages [25] -->
[8] Klaassen, F. J. G. M.; Magnus, J. R. Forecasting the Winner of a Tennis Match. European

<!-- b000681 | references | pages [25] -->
Journal of Operational Research 2003, 148 (2), 257–267. https://doi.org/10.1016/S0377-

<!-- b000682 | references | pages [25] -->
2217(02)00682-3.

<!-- b000683 | references | pages [25] -->
[9] Bouzidis, T.; Karagiannis, G. Extending the Zero-Sum Gains Data Envelopment Analysis

<!-- b000684 | references | pages [25] -->
Model. J Prod Anal 2022, 58 (2–3), 171–184. https://doi.org/10.1007/s11123-022-00644-1.

<!-- b000685 | references | pages [25] -->
[10] Kovalchik, S.; Reid, M. A Calibration Method with Dynamic Updates for Within-Match

<!-- b000686 | references | pages [25] -->
Forecasting of Wins in Tennis. International Journal of Forecasting 2019, 35 (2), 756–766.

<!-- b000687 | references | pages [25] -->
https://doi.org/10.1016/j.ĳforecast.2017.11.008.

<!-- b000688 | references | pages [25] -->
[11] Shi Fuying, Zhang Hui, Liang Chengjun. Development of a Technical and Tactical Decision-

<!-- b000689 | references | pages [25] -->
Making Analysis System for Tennis Matches [J]. Journal of Beĳing Sport University, 2010,

<!-- b000690 | references | pages [25] -->
33(09): 129-132+138. DOI: 10.19582/j.cnki.11-3785/g8.2010.09.037.

<!-- b000691 | references | pages [25] -->
[12] Tao Zhixiang. Research on the Basic Unit of Athletic Process in Men’s Single Events of

<!-- b000692 | references | pages [25] -->
Racket Net Sports [D]. Beĳing Sport University, 2003.

<!-- b000693 | references | pages [25] -->
[13] Ferrante, Marco & Fonseca, Giovanni & Carrari, Andrea. (2017). A new marko-

<!-- b000694 | references | pages [25] -->
vian model for tennis matches. Electronic Journal of Applied Statistical Analysis. 10.

<!-- b000695 | references | pages [25] -->
10.1285/i20705948v10n3p693.

<!-- b000696 | furniture | pages [25] -->
关注数学模型

<!-- b000697 | furniture | pages [25] -->
2

<!-- b000698 | furniture | pages [25] -->
MATHmodels

<!-- b000699 | furniture | pages [25] -->
获取更多资讯

<!-- b000700 | furniture | pages [26] -->
Team # 2406176

<!-- b000701 | heading | pages [26] -->
Appendices

<!-- b000702 | heading | pages [26] -->
Indicators in Swing Prediction Model in 6.2

<!-- b000703 | furniture | pages [26] -->
Page 26 of 27

<!-- b000704 | prose | pages [26] -->
微信公众号：数学模型

<!-- b000705 | prose | pages [26] -->
n(ace) Aces_p𝑖= n(successful serves)

<!-- b000706 | prose | pages [26] -->
2 ∗n(winner) Winners_p𝑖= n(rally) −n(server) + n(winner)

<!-- b000707 | prose | pages [26] -->
Winners4_p𝑖= 2 ∗ n(winner | rally_n ≥4) n(rally | rally ≥4) −n(server | rally_n ≥4) + n(winner | rally_n ≥4)

<!-- b000708 | prose | pages [26] -->
Winners13_p𝑖= 2 ∗ n(winner |1 ≤rally_n ≤3) n(rally | 1 ≤rally_n ≤3) −n(server | 1 ≤rally_n ≤3) + n(winner | 1 ≤rally_n ≤3)

<!-- b000709 | prose | pages [26] -->
Double_fault_p𝑖= count(double_fault)

<!-- b000710 | prose | pages [26] -->
count(server)

<!-- b000711 | prose | pages [26] -->
1st_srv_in_p𝑖= count(server | serve_no = 1)

<!-- b000712 | prose | pages [26] -->
微信号：MATHmodels

<!-- b000713 | prose | pages [26] -->
serve_sum

<!-- b000714 | prose | pages [26] -->
2nd_srv_in_p𝑖= count(server | serve_no = 2, double_fault = 0) serve_sum

<!-- b000715 | prose | pages [26] -->
1st_srv_won_p𝑖= n(server | serve_no = 1, point_victor = 𝑖) n(server | serve_no = 1)

<!-- b000716 | prose | pages [26] -->
2nd_srv_won_p𝑖= n(server | serve_no = 2, point_victor = 𝑖) n(server | serve_no = 2)

<!-- b000717 | prose | pages [26] -->
Net_pt_won_p𝑖= n(net_pt_won)

<!-- b000718 | prose | pages [26] -->
n(net_pt)

<!-- b000719 | prose | pages [26] -->
n(unf_err) Total_unf_err_p𝑖= n(total points)

<!-- b000720 | prose | pages [26] -->
Break_p𝑖= n(server = 𝑗, break_pt_won = 𝑖)

<!-- b000721 | prose | pages [26] -->
n(server = 𝑗, break_pt = 1)

<!-- b000722 | prose | pages [26] -->
1st_srv_drt_won_p𝑖= n(server | serve_no = 1, rally_count = 1) n(server | serve_no = 1)

<!-- b000723 | prose | pages [26] -->
2nd_srv_drt_won_p𝑖= n(server | serve_no = 2, rally_count = 1) n(server | serve_no = 2) Srv_avg_speed_p𝑖= mean(speed_mph | server = 𝑖)

<!-- b000724 | prose | pages [26] -->
1st_rcv_won_p𝑖= n(server = 𝑗, serve_no = 1, point_victor = 𝑖) n(server = 𝑗, serve_no = 1)

<!-- b000725 | prose | pages [26] -->
2nd_rcv_won_p𝑖= n(server = 𝑗, serve_no = 2, point_victor = 𝑖) n(server = 𝑗, serve_no = 2)

<!-- b000726 | prose | pages [26] -->
n(server = 𝑖, serve_width = 𝐵) Width_B_p𝑖= n(server = 𝑖, serve_width ≠unknown)

<!-- b000727 | prose | pages [26] -->
n(server = 𝑖, serve_width = 𝐶) Width_C_p𝑖= n(server = 𝑖, serve_width ≠unknown)

<!-- b000728 | prose | pages [26] -->
n(server = 𝑖, serve_width = 𝑊) Width_W_p𝑖= n(server = 𝑖, serve_width ≠unknown)

<!-- b000729 | furniture | pages [26] -->
关注数学模型

<!-- b000730 | furniture | pages [26] -->
2

<!-- b000731 | furniture | pages [26] -->
MATHmodels

<!-- b000732 | furniture | pages [26] -->
获取更多资讯

<!-- b000733 | furniture | pages [27] -->
Team # 2406176

<!-- b000734 | furniture | pages [27] -->
Page 27 of 27

<!-- b000735 | prose | pages [27] -->
n(server = 𝑖, serve_width = 𝐵𝐶) Width_BC_p𝑖= n(server = 𝑖, serve_width ≠unknown)

<!-- b000736 | prose | pages [27] -->
微信公众号：数学模型

<!-- b000737 | prose | pages [27] -->
n(server = 𝑖, serve_width = 𝐵𝑊) Width_BW_p𝑖= n(server = 𝑖, serve_width ≠unknown)

<!-- b000738 | prose | pages [27] -->
n(server = 𝑖, serve_depth = 𝐶𝑇𝐿) Depth_CTL_p𝑖= n(server = 𝑖, serve_depth ≠unknown)

<!-- b000739 | prose | pages [27] -->
n(server = 𝑗, return_depth = 𝐷) Return_depth_D_p𝑖= n(server = 𝑗, return_depth ≠unknown)

<!-- b000740 | prose | pages [27] -->
F_won_p𝑖= n(point_victor = 𝑖, winner_shot_type = 𝐹)

<!-- b000741 | prose | pages [27] -->
n(point_victor = 𝑖)

<!-- b000742 | caption | pages [27] -->
Table 4: Indicators and their brief introductions

<!-- b000743 | prose | pages [27] -->
微信号：MATHmodels

<!-- b000744 | prose | pages [27] -->
No.

<!-- b000745 | heading | pages [27] -->
Symbol

<!-- b000746 | heading | pages [27] -->
Introduction

<!-- b000747 | prose | pages [27] -->
Proportion of successful serves that are aces for player 𝑖. 1 Aces_p𝑖 2 Winners_p𝑖 Proportion of rallies won by player 𝑖. Proportion of rallies with 4 or more shots won by player 𝑖. 3 Winners4_p𝑖 Proportion of rallies with 1 to 3 shots won by player 𝑖. 4 Winners13_p𝑖 Proportion of player 𝑖’s serves that are double faults. 5 Double_fault_p𝑖 Proportion of player 𝑖’s first serves that are in. 6 1st_srv_in_p𝑖 Proportion of player 𝑖’s second serves that are in, excluding double faults. 7 2nd_srv_in_p𝑖 Proportion of player 𝑖’s first serves that result in a point won. 8 1st_srv_won_p𝑖 Proportion of player 𝑖’s second serves that result in a point won. 9 2nd_srv_won_p𝑖 10 Net_pt_won_p𝑖 Proportion of net points won by player 𝑖. Proportion of total points that are unforced errors for player 𝑖. 11 Total_unf_err_p𝑖 Proportion of break points won by player 𝑖. 12 Break_p𝑖 Proportion of player 𝑖’s first serves that directly result in a point won. 13 1st_srv_drt_won_p𝑖 Proportion of player 𝑖’s second serves that directly result in a point won. 14 2nd_srv_drt_won_p𝑖 15 Srv_avg_speed_p𝑖 Average speed of serves for player 𝑖. Proportion of first serves received by player 𝑖that result in a point won. 16 1st_rcv_won_p𝑖 Proportion of second serves received by player 𝑖that result in a point won. 17 2nd_rcv_won_p𝑖 Proportion of player 𝑖’s serves that land in the "B" width zone. 18 Width_B_p𝑖 Proportion of player 𝑖’s serves that land in the "C" width zone. 19 Width_C_p𝑖 Proportion of player 𝑖’s serves that land in the "W" width zone. 20 Width_W_p𝑖 Proportion of player 𝑖’s serves that land in the "BC" width zone. 21 Width_BC_p𝑖 Proportion of player 𝑖’s serves that land in the "BW" width zone. 22 Width_BW_p𝑖 Proportion of player 𝑖’s serves that land in the "CTL" depth zone. 23 Depth_CTL_p𝑖 Proportion of serves received by player 𝑖that land in the "D" depth zone. 24 Return_depth_D_p𝑖 Proportion of points won by player 𝑖with a forehand shot. 25 F_won_p𝑖

<!-- b000748 | furniture | pages [27] -->
关注数学模型

<!-- b000749 | furniture | pages [27] -->
2

<!-- b000750 | furniture | pages [27] -->
MATHmodels

<!-- b000751 | furniture | pages [27] -->
获取更多资讯

<!-- b000752 | furniture | pages [28] -->
Team # 2406176

<!-- b000753 | prose | pages [28] -->
Page 28

<!-- b000754 | heading | pages [28] -->
Report on Use of AI

<!-- b000755 | ai_disclosure | pages [28] -->
1. Bing AI

<!-- b000756 | ai_disclosure | pages [28] -->
微信公众号：数学模型

<!-- b000757 | ai_disclosure | pages [28] -->
Query1: write a pseudocode for Bartlett’s Test of Sphericity, please generate in latex code

<!-- b000758 | ai_disclosure | pages [28] -->
format. you should contain all necessary mathmetical equations.

<!-- b000759 | ai_disclosure | pages [28] -->
Output: Here’s a pseudocode for Bartlett’s Test of Sphericity, which is a statistical test for the

<!-- b000760 | ai_disclosure | pages [28] -->
assumption of equal variances in the population. The test statistic is calculated as follows:

<!-- b000761 | heading | pages [28] -->
Algorithm 5 Bartlett’s Test of Sphericity

<!-- b000762 | prose | pages [28] -->
Data: Indicator matrix X Result: Test statistic, p-value, and a decision on whether the data need to be factor analyzed begin

<!-- b000763 | prose | pages [28] -->
𝜒2 = −log(det(𝑅))(𝑁−1 −2𝑛+5

<!-- b000764 | prose | pages [28] -->
6 ) where 𝑅is the correlation matrix of the dataset, 𝑁= 109 (number of data points), 𝑛= 25;

<!-- b000765 | prose | pages [28] -->
𝜒2, 𝑝(𝑝+1)

<!-- b000766 | prose | pages [28] -->


<!-- b000767 | prose | pages [28] -->


<!-- b000768 | prose | pages [28] -->
𝑝= 1 −𝐹𝜒2

<!-- b000769 | prose | pages [28] -->
−1

<!-- b000770 | prose | pages [28] -->
;

<!-- b000771 | prose | pages [28] -->
微信号：MATHmodels

<!-- b000772 | prose | pages [28] -->
2

<!-- b000773 | prose | pages [28] -->
if 𝑝< 0.05 then

<!-- b000774 | prose | pages [28] -->
The data is appropriate for factor analysis.; end else

<!-- b000775 | prose | pages [28] -->
The data is not appropriate for factor analysis.; end end

<!-- b000776 | furniture | pages [28] -->
关注数学模型

<!-- b000777 | furniture | pages [28] -->
2

<!-- b000778 | furniture | pages [28] -->
MATHmodels

<!-- b000779 | furniture | pages [28] -->
获取更多资讯
