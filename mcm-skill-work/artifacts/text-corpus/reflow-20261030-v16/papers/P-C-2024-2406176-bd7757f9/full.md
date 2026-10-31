# P-C-2024-2406176-bd7757f9

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
The paper extends its analysis to dynamic strategic choices made by tennis players during matches, employing the Mixed-Strategy Nash Equilibrium model. K-means clustering is utilized to determine strategic clusters. The Nash equilibrium is calculated, offering insights into optimal strategy combinations against different opponents.

<!-- b000016 | prose | pages [1] -->
The efficacy of the proposed models is validated through testing on notable tennis matches, including the extraordinarily tight 2023 Wimbledon Gentlemen’s Final between Carlos Alcaraz and Novak Djokovic, and the one-sided 2017 French Open match between Andy Murray and Andrey Kuznetsov. The SP model exhibits high accuracy (85.32% for the Alcaraz vs. Djokovic match, and 88.34% for the Murray vs. Kuznetsov match), while the FSF model accurately cap- tures momentum trends, taking into account the score situation and historical commentary. Eventually, we pinpoint crucial factors for inclusion in future models.

<!-- b000017 | keywords | pages [1] -->
Keywords: tennis; momentum; real-time win probability; Elo rating system; mixed-strategy Nash

<!-- b000018 | prose | pages [1] -->
equilibrium; quantification model

<!-- b000019 | furniture | pages [1] -->
关注数学模型

<!-- b000020 | furniture | pages [1] -->
2

<!-- b000021 | furniture | pages [1] -->
MATHmodels

<!-- b000022 | furniture | pages [1] -->
获取更多资讯

<!-- b000023 | furniture | pages [2] -->
Team # 2406176

<!-- b000024 | furniture | pages [2] -->
Page 2 of 27

<!-- b000025 | heading | pages [2] -->
Contents

<!-- b000026 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000027 | contents | pages [2] -->
1 Introduction

<!-- b000028 | contents | pages [2] -->
4

<!-- b000029 | contents | pages [2] -->
1.1

<!-- b000030 | contents | pages [2] -->
Background Information

<!-- b000031 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
4

<!-- b000033 | contents | pages [2] -->
1.2

<!-- b000034 | contents | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
4

<!-- b000036 | contents | pages [2] -->
1.3

<!-- b000037 | contents | pages [2] -->
Model Overview

<!-- b000038 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
2 Assumptions

<!-- b000041 | contents | pages [2] -->
5

<!-- b000042 | contents | pages [2] -->
3 Notifications

<!-- b000043 | contents | pages [2] -->
6

<!-- b000044 | contents | pages [2] -->
4 Data Source

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000047 | contents | pages [2] -->
5 Real-Time Momentum Quantification Model

<!-- b000048 | contents | pages [2] -->
6

<!-- b000049 | contents | pages [2] -->
5.1

<!-- b000050 | contents | pages [2] -->
Pre-match Win Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
7

<!-- b000052 | contents | pages [2] -->
5.2

<!-- b000053 | contents | pages [2] -->
Probability of Winning the First Point

<!-- b000054 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
8

<!-- b000056 | contents | pages [2] -->
5.3

<!-- b000057 | contents | pages [2] -->
Dynamic Computation of the Subsequent Points’ Win Probabilities . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
9

<!-- b000059 | contents | pages [2] -->
5.4

<!-- b000060 | contents | pages [2] -->
Quantification of Momentum . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
11

<!-- b000062 | contents | pages [2] -->
5.4.1

<!-- b000063 | contents | pages [2] -->
Verification of the Significance of Momentum . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
12

<!-- b000065 | contents | pages [2] -->
5.5

<!-- b000066 | contents | pages [2] -->
Momentum Trend Value (MMTTV) Visualization . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
14

<!-- b000068 | contents | pages [2] -->
6 Swing Prediction Model

<!-- b000069 | contents | pages [2] -->
15

<!-- b000070 | contents | pages [2] -->
6.1

<!-- b000071 | contents | pages [2] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
15

<!-- b000073 | contents | pages [2] -->
6.2

<!-- b000074 | contents | pages [2] -->
Indicators Calculation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
15

<!-- b000076 | contents | pages [2] -->
6.3

<!-- b000077 | contents | pages [2] -->
Exploratory Factor Analysis

<!-- b000078 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
16

<!-- b000080 | contents | pages [2] -->
6.4

<!-- b000081 | contents | pages [2] -->
Prediction of Swing Based on Multivariate Linear Regression Model . . . . . . . .

<!-- b000082 | contents | pages [2] -->
17

<!-- b000083 | contents | pages [2] -->
7 Mixed-Strategy Nash Equilibrium Model

<!-- b000084 | contents | pages [2] -->
18

<!-- b000085 | contents | pages [2] -->
7.1

<!-- b000086 | contents | pages [2] -->
Strategy Payoff Calculation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
18

<!-- b000088 | contents | pages [2] -->
7.2

<!-- b000089 | contents | pages [2] -->
Model Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
20

<!-- b000091 | contents | pages [2] -->
8 Test of FSF Model and SP Model

<!-- b000092 | contents | pages [2] -->
21

<!-- b000093 | contents | pages [2] -->
8.1

<!-- b000094 | contents | pages [2] -->
The Match between Alcaraz and Djokovic . . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [2] -->
21

<!-- b000096 | furniture | pages [2] -->
关注数学模型

<!-- b000097 | furniture | pages [2] -->
2

<!-- b000098 | furniture | pages [2] -->
MATHmodels

<!-- b000099 | furniture | pages [2] -->
获取更多资讯

<!-- b000100 | furniture | pages [3] -->
Team # 2406176

<!-- b000101 | furniture | pages [3] -->
Page 3 of 27

<!-- b000102 | contents | pages [3] -->
8.2

<!-- b000103 | contents | pages [3] -->
Model Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [3] -->
22

<!-- b000105 | contents | pages [3] -->
8.3

<!-- b000106 | contents | pages [3] -->
Contextual Limitations in SP Model . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [3] -->
22

<!-- b000108 | contents | pages [3] -->
8.4

<!-- b000109 | contents | pages [3] -->
Key Indicators to be Included in Future Models . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [3] -->
22

<!-- b000111 | contents | pages [3] -->
微信公众号：数学模型

<!-- b000112 | heading | pages [3] -->
9 Sensitivity Analysis

<!-- b000113 | prose | pages [3] -->
23

<!-- b000114 | heading | pages [3] -->
Appendices

<!-- b000115 | prose | pages [3] -->
26

<!-- b000116 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000117 | furniture | pages [3] -->
关注数学模型

<!-- b000118 | furniture | pages [3] -->
2

<!-- b000119 | furniture | pages [3] -->
MATHmodels

<!-- b000120 | furniture | pages [3] -->
获取更多资讯

<!-- b000121 | furniture | pages [4] -->
Team # 2406176

<!-- b000122 | furniture | pages [4] -->
Page 4 of 27

<!-- b000123 | heading | pages [4] -->
1 Introduction

<!-- b000124 | heading | pages [4] -->
1.1 Background Information

<!-- b000125 | prose | pages [4] -->
微信公众号：数学模型 In the 2023 Wimbledon final, Carlos Alcaraz overcame Novak Djokovic’s initial dominance to win, demonstrating a thrilling momentum shift. This echoed the 2008 final where Rafael Nadal triumphed over Roger Federer, highlighting the unpredictable and captivating nature of tennis.

<!-- b000126 | prose | pages [4] -->
Research has shown that athletes, especially tennis players, can experience a psychological or physiological boost known as momentum. This concept was first explored in a study by Gilovich, Vallone, and Tversky (1985), who identified a ‘hot hand’ phenomenon in basketball where a player’s real-time performance significantly exceeds pre-match expectations based on his overall record. However, momentum can be temporary and may shift to the opponent, leading to swings where potential winners lose several points or games.

<!-- b000127 | prose | pages [4] -->
This paper explores the dynamic performance changes of players throughout a game and offers in-depth insights into how players’ techniques and strategies should adapt in response to their 微信号：MATHmodels opponents’ key factors.

<!-- b000128 | heading | pages [4] -->
1.2 Problem Analysis

<!-- b000129 | prose | pages [4] -->
• Task 1: Construct a model that dynamically calculates the performance of both players within the match, taking serving-advantage into consideration.

<!-- b000130 | prose | pages [4] -->
In this paper, we develop an RTWP (Real-Time Win Probability) model that accurately predicts the win probability of the subsequent point based on Elo rating system in real time. On that basis, we built the RTMQ (Real-Time Momentum Quantification) model by effectively quantifying player performance, by calculating the difference between real- time and pre-match win rates under separate serve/receive conditions (considering the serving side’s advantage). Finally we apply Fourier-series fitting to MMT to obtain the momentum trend value (MMTTV).

<!-- b000131 | prose | pages [4] -->
• Task 2: Evaluate the significance of ’momentum’ in tennis matches.

<!-- b000132 | prose | pages [4] -->
We took the 2023 Winbledon final as an example and tested our RTWP model and the CWP (Constant Win Probability) model, which neglects the influence of momentum. A Kolmogorov-Smirnov (K-S) test is performed taking the model results as the input and confirms the significant role that momentum plays in the match, reversing the coach’s hypothesis.

<!-- b000133 | prose | pages [4] -->
• Task 3: Determine the key indicators that could trigger a momentum shift.

<!-- b000134 | prose | pages [4, 5] -->
We introduce the Swing Prediction (SP) model to anticipate substantial momentum shifts, using the more stable MMTTV as a sample for each set. This is because the frequent in-set momentum shifts can render predictions based on real-time momentum data at the end of each set unreliable. MMTTV has no such fluctuations and effectively captures the trend of MMT. Subsequently, we identify technical indicators influencing player performance, extract common factors through factor analysis, and employ these as independent variables in a Multivariate Linear Regression to predict the swings. Subsequently, we apply K-means clustering to distinguish between different tactics and finally calculate the player’s optimal strategy using a mixed-strategy Nash equilibrium approach.

<!-- b000135 | furniture | pages [4] -->
关注数学模型

<!-- b000136 | furniture | pages [4] -->
2

<!-- b000137 | furniture | pages [4] -->
MATHmodels

<!-- b000138 | furniture | pages [4] -->
获取更多资讯

<!-- b000139 | furniture | pages [5] -->
Team # 2406176

<!-- b000140 | furniture | pages [5] -->
Page 5 of 27

<!-- b000142 | prose | pages [5] -->
• Task 4: Assess the model’s ability to predict match swings and evaluate its performance 微信公众号：数学模型 across various tournaments, court surfaces, and other sports.

<!-- b000143 | prose | pages [5] -->
We validated the accuracy of our model using data from other matches in the dataset and conducted a sensitivity analysis. Subsequently, we discussed potential improvements to the model by considering factors such as climate and court surface. Finally, we further discussed the generalization capabilities of our model using the 2017 French Open Men’s Singles dataset as an example.

<!-- b000144 | heading | pages [5] -->
1.3 Model Overview

<!-- b000145 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000146 | caption | pages [5] -->
Figure 1: Model Overview

<!-- b000147 | heading | pages [5] -->
2 Assumptions

<!-- b000148 | prose | pages [5] -->
• All tennis players in the table demonstrate a high level of adaptability during play. This adaptability is reflected in their ability to continuously modify strategies based on their opponent’s characteristics.

<!-- b000149 | prose | pages [5] -->
• The technical indicators in the table, such as the way of winning, are able to fully characterize the strategy adopted by the current player. Changes in these indicators during a match can fully characterize changes in a player’s strategy.

<!-- b000150 | prose | pages [5] -->
• All data are authentic.

<!-- b000151 | furniture | pages [5] -->
关注数学模型

<!-- b000152 | furniture | pages [5] -->
2

<!-- b000153 | furniture | pages [5] -->
MATHmodels

<!-- b000154 | furniture | pages [5] -->
获取更多资讯

<!-- b000155 | furniture | pages [6] -->
Team # 2406176

<!-- b000156 | furniture | pages [6] -->
Page 6 of 27

<!-- b000157 | heading | pages [6] -->
3 Notifications

<!-- b000158 | caption | pages [6] -->
Table 1: Significant symbols in this paper

<!-- b000159 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000160 | heading | pages [6] -->
Symbols

<!-- b000161 | prose | pages [6] -->
Description the 𝑖𝑡ℎplayer’s Elo rating at the 𝑡𝑡ℎmatch 𝐸𝑖(𝑡) a prediction based on Elo indicating that the 𝑖𝑡ℎplayer defeats the 𝑗𝑡ℎopponent 𝑃𝑖𝑗(𝑡) 𝑝0 the probability of a server winning the first point, constant during match ˆ𝑝(𝑆𝑚) the probability of a server winning the next point, dynamic within match 𝜂(𝑆𝑚) a dynamic weight that balances the pre-match and in-match serve information 𝜆𝑖 a weight emphasizing performance at the moment over the initial performance PA(t) Real-Time Win Probability of player A MMTA(t) Real-Time Momentum value of player A MMTTVA(t) Real-Time Momentum Trend value of player A

<!-- b000162 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000163 | heading | pages [6] -->
4 Data Source

<!-- b000164 | caption | pages [6] -->
Table 2: The websites we use to obtain the necessary data

<!-- b000165 | prose | pages [6] -->
No. Website Usage

<!-- b000166 | prose | pages [6] -->
1 https://www.tenelos.com/ Acquire Elo ratings of all players before match Acquire 𝑚𝑖to calculate 𝐾𝑖of players before match 2 https://www.atptour.com/en/rankings/ singles?DateWeek=2023-07-03 3 https://www.wimbledon.com/ Search for relevant data of players in the dataset 4 https://github.com/JeffSackmann/ ten- 2017 French Open dataset for problem 4 nis_slam_pointbypoint

<!-- b000167 | heading | pages [6] -->
5 Real-Time Momentum Quantification Model

<!-- b000168 | prose | pages [6] -->
In our RTMQ model, we adopt a definition of momentum that is consistent with the classic interpretation of Gilovich et al. (1985). In this context, momentum is defined as a player’s performance during a given period that significantly exceeds his expected performance based on pre-match predictions. The calculation of momentum involves determining the difference between the pre-match win probability and the real-time win probability. The greater the difference, the greater the momentum.

<!-- b000169 | prose | pages [6] -->
The modeling process is divided into four stages: obtaining the pre-match win prediction, determining the first point’s win probability, dynamically computing the subsequent points’ win probabilities, and calculating the difference eventually. The modeling flow of the RTMQ model is shown below.

<!-- b000170 | furniture | pages [6] -->
关注数学模型

<!-- b000171 | furniture | pages [6] -->
2

<!-- b000172 | furniture | pages [6] -->
MATHmodels

<!-- b000173 | furniture | pages [6] -->
获取更多资讯

<!-- b000174 | furniture | pages [7] -->
Team # 2406176

<!-- b000175 | furniture | pages [7] -->
Page 7 of 27

<!-- b000176 | prose | pages [7] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000177 | caption | pages [7] -->
Figure 2: RTMQ model setup

<!-- b000178 | heading | pages [7] -->
5.1 Pre-match Win Prediction

<!-- b000179 | prose | pages [7] -->
We utilize the Elo rating system to predict match outcomes before the game. This outstand- ing system, dynamic and zero-sum, adjusts player ratings based on match outcomes and maintains fairness. Its simplicity, robustness, and proven effectiveness across sports highlight its adaptability and reliability.

<!-- b000180 | prose | pages [7] -->
The rating of a player is calculated with the following recursive formula:

<!-- b000181 | prose | pages [7] -->
𝐸𝑖(𝑡+ 1) = 𝐸𝑖(𝑡) + 𝐾𝑖×  𝑃𝑖𝑗(𝑡) −𝑊𝑖(𝑡) (1) 𝐸𝑖(1) = 1500

<!-- b000182 | prose | pages [7, 8] -->
where 𝐸𝑖denotes the 𝑖𝑡ℎplayer’s Elo rating (in a player’s very first tour match, 𝐸𝑖(1) is assigned 1500), 𝑡is the number of match, 𝑊𝑖is a discrete variable that equals 1 if the player loses the match and equals 0 if the player wins the match, and 𝑃𝑖𝑗(𝑡) is a prediction based on Elo indicating that the 𝑖𝑡ℎplayer defeats the 𝑗𝑡ℎopponent. 𝐾𝑖, relevant to the number of the player’s career matches, is equal to 250 𝐾𝑖= (2) (𝑚𝑖(𝑡) + 5)0.4 where 𝑚𝑖(𝑡) is match number. 𝑃𝑖𝑗(𝑡) is calculated through

<!-- b000183 | furniture | pages [7] -->
关注数学模型

<!-- b000184 | furniture | pages [7] -->
2

<!-- b000185 | furniture | pages [7] -->
MATHmodels

<!-- b000186 | furniture | pages [7] -->
获取更多资讯

<!-- b000187 | furniture | pages [8] -->
Team # 2406176

<!-- b000188 | furniture | pages [8] -->
Page 8 of 27

<!-- b000190 | prose | pages [8] -->
−1 (𝐸𝑗(𝑡)−𝐸𝑖(𝑡))  𝑃𝑖𝑗(𝑡) = 1 + 10 (3) 400 微信公众号：数学模型 which matches our intuition. When 𝐸𝑗(𝑡) < 𝐸𝑖(𝑡) and 𝐸𝑗(𝑡) −𝐸𝑖(𝑡) decreases, indicating a rising competence of the 𝑖𝑡ℎplayer over the 𝑗𝑡ℎplayer, the winning probability 𝑃𝑖𝑗increases.

<!-- b000191 | heading | pages [8] -->
5.2 Probability of Winning the First Point

<!-- b000192 | prose | pages [8] -->
To track the performance of the players, the win probability of the first point is calculated. We take the independent and identically distributed (IID) assumption and use 𝑃𝑖𝑗to reverse calculate the probability of the pre-match serving side winning the first point. The probability of securing the initial serving/receiving point in a match, represented as 𝑝0/𝑝0 −𝜀(𝜀= 0.25 for men athletes and = 0.15 for women athletes, according to previous research led by Machar Reid), are assumed to be the same as the probability of winning any subsequent serving/receiving point 微信号：MATHmodels prior to the beginning of the match. The probability of winning the upcoming point, ˆ𝑝(𝑆𝑚), will be recalculated after the conclusion of the first points as they occur. In mathematical terms, we aim to solve for 𝑝0 through 𝑓0(𝑝0, 𝑞0) = 𝑃𝑖𝑗 (4)

<!-- b000193 | prose | pages [8] -->
where 𝑞0 = 1 −𝑝0. The figure below indicates the progression of scores in a tennis game for a server (if receiver, 𝑝𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑟 = 𝑝0 −𝜀and 𝑞𝑟𝑒𝑐𝑒𝑖𝑣𝑒𝑟 = 1 −𝑝0 + 𝜀). 0 0

<!-- b000194 | caption | pages [8] -->
Figure 3: Progression of scores in a tennis game for a server

<!-- b000195 | prose | pages [8] -->
The following algorithm demonstrates the computation of 𝑓0(𝑝0, 1 −𝑝0), which is entirely based on probability. The pseudocode below outlines the calculation of match-winning probability.

<!-- b000196 | furniture | pages [8] -->
关注数学模型

<!-- b000197 | furniture | pages [8] -->
2

<!-- b000198 | furniture | pages [8] -->
MATHmodels

<!-- b000199 | furniture | pages [8] -->
获取更多资讯

<!-- b000200 | furniture | pages [9] -->
Team # 2406176

<!-- b000201 | furniture | pages [9] -->
Page 9 of 27

<!-- b000202 | heading | pages [9] -->
Algorithm 1 Probability of Winning a Tennis Match

<!-- b000203 | prose | pages [9] -->
Data: Player A’s and Player B’s probability of winning the first point 𝑝𝐴 0 , 𝑝𝐵 0 as servers

<!-- b000204 | heading | pages [9] -->
Result: Probability of Player A winning the match 𝑃𝑖𝑗

<!-- b000205 | prose | pages [9] -->
微信公众号：数学模型 begin 20(𝑝𝐴 0 )5(1−𝑝𝐴 0 )3 0 )4 + 4(𝑝𝐴 0 )2 + Calculate 𝑝𝐺𝐴= (𝑝𝐴 0 )4(1 −𝑝𝐴 0 ) + 10(𝑝𝐴 0 )4(1 −𝑝𝐴 0 ) ; 1−2𝑝𝐴 0 (1−𝑝𝐴 20(𝑝𝐵 0 )5(1−𝑝𝐵 0 )3 0 )4 + 4(𝑝𝐵 0 )2 + Calculate 𝑝𝐺𝐵= (𝑝𝐵 0 )4(1 −𝑝𝐵 0 ) + 10(𝑝𝐵 0 )4(1 −𝑝𝐵 0 ) ; 1−2𝑝𝐵 0 (1−𝑝𝐵 Set 𝑝𝑅= 1 −𝑝𝐺𝐴;

<!-- b000206 | prose | pages [9] -->
Set 𝑞𝐺𝐴= 1 −𝑝𝐺𝐴;

<!-- b000207 | prose | pages [9] -->
Set 𝑞𝐺𝐵= 1 −𝑝𝐺𝐵;

<!-- b000208 | prose | pages [9] -->
Calculate 𝑝𝑆𝐴(6, 0) = (𝑝𝐺𝐴· 𝑞𝐺𝐵)3; Calculate 𝑝𝑆𝐴(6, 1) = 3 · (𝑝𝐺𝐴)3 · 𝑞𝐺𝐴· (𝑞𝐺𝐵)3 + 3 · (𝑝𝐺𝐴)4 · 𝑝𝐺𝐵· (𝑞𝐺𝐵)2; Calculate 𝑝𝑆𝐴(6, 2) = 12 · (𝑝𝐺𝐴)5 · (𝑞𝐺𝐴)2 · 𝑝𝐺𝐵· 𝑞𝐺𝐵+ 10 · (𝑝𝐺𝐴)6 · (𝑝𝐺𝐵)2 · 𝑞𝐺𝐵; Calculate 𝑝𝑆𝐴(6, 3) = 60 · (𝑝𝐺𝐴)7 · (𝑞𝐺𝐴) · (𝑝𝐺𝐵)2 + 15 · (𝑝𝐺𝐴)8 · 𝑝𝐺𝐵; Calculate 𝑝𝑆𝐴(6, 4) = 360 · (𝑝𝐺𝐴)9 · 𝑝𝐺𝐵; 微信号：MATHmodels Calculate 𝑝𝑆𝐴(6, 5) = 720 · (𝑝𝐺𝐴)10;

<!-- b000209 | prose | pages [9] -->
Calculate 𝑃𝑖𝑗= 𝑓0(𝑝0, 1 −𝑝0) = 𝑝𝑆𝐴(6, 0) + 𝑝𝑆𝐴(6, 1) + 𝑝𝑆𝐴(6, 2) + 𝑝𝑆𝐴(6, 3) + 𝑝𝑆𝐴(6, 4) + 𝑝𝑆𝐴(6, 5);

<!-- b000210 | prose | pages [9] -->
return 𝑃𝑖𝑗;

<!-- b000211 | prose | pages [9] -->
end

<!-- b000212 | prose | pages [9] -->
This pseudocode outlines the steps to calculate the probability of Player A winning a tennis match based on the given game probabilities. Explanations of the symbols are:

<!-- b000213 | prose | pages [9] -->
• 𝑝𝐺𝑋: The probability that Player X wins a game when serving, X=A or B.

<!-- b000214 | prose | pages [9] -->
• 𝑝𝑅: The probability that Player B wins a game when receiving, i.e. 𝑝𝑅= 1 −𝑝𝐺𝐴.

<!-- b000215 | prose | pages [9] -->
• 𝑞𝐺𝑋: The probability that player X loses a game when serving, X=A or B, i.e. 𝑞𝐺𝐴= 1−𝑝𝐺𝐴.

<!-- b000216 | prose | pages [9] -->
• 𝑝𝑆𝐴(6, 𝑘): The probability that Player A wins a set with a score of 6-k, where k=0,1,2,3,4,5.

<!-- b000217 | prose | pages [9] -->
• 𝑃𝑖𝑗: The probability that Player A wins the match.

<!-- b000218 | prose | pages [9] -->
We plot the relationshipbetween 𝑃𝑖𝑗and 𝑝0. FromFigure 4 wecan see that 𝑃𝑖𝑗is amonotonically increasing function, thus we apply the dichotomy method to calculate 𝑝0.

<!-- b000219 | prose | pages [9] -->
Therefore, for a given 𝑃𝑖𝑗, the probability of winning the first point can be obtained and applied in the dynamic algorithm updating the probability of winning the next point below.

<!-- b000220 | heading | pages [9] -->
5.3 Dynamic Computation of the Subsequent Points’ Win Probabilities

<!-- b000221 | prose | pages [9, 10] -->
Once we determine the first point’s win probability, we proceed to compute the win probability for the next point. We propose an efficient method to update the winning probability of both 微信公众号：数学模型

<!-- b000222 | furniture | pages [9] -->
关注数学模型

<!-- b000223 | furniture | pages [9] -->
2

<!-- b000224 | furniture | pages [9] -->
MATHmodels

<!-- b000225 | furniture | pages [9] -->
获取更多资讯

<!-- b000226 | furniture | pages [10] -->
Team # 2406176

<!-- b000227 | furniture | pages [10] -->
Page 10 of 27

<!-- b000229 | caption | pages [10] -->
Figure 4: Relationship between 𝑃𝑖𝑗and 𝑝0

<!-- b000230 | prose | pages [10] -->
微信号：MATHmodels players in the next point through the equation below, considering the strong zero-sum game property of tennis

<!-- b000231 | prose | pages [10] -->
𝑠= ˆ𝑝𝐴𝑠(𝑆𝑚) if A is server and B is receiver 𝑝𝐴  PA(𝑡) = (5) 𝑟= 1 −ˆ𝑝𝐵𝑠(𝑆𝑚) if A is receiver and B is server 𝑝𝐴  where PA(𝑡) is player A’s probability of winning the next point, 𝑝𝐴 𝑠/𝑝𝐴 𝑟is the probability of A winning the next point as a server/receiver. Therefore the model only requires an updating rule for the server’s probability of winning the next point. We applied the Quasi-Binomial Estimator

<!-- b000232 | prose | pages [10] -->
ˆ𝑝𝑠(𝑆𝑚) = 𝜂(𝑆𝑚) × 𝑝0 + (1 −𝜂(𝑆𝑚)) × ¯𝑝𝑠(𝑆𝑚) (6)

<!-- b000233 | prose | pages [10] -->
where ˆ𝑝𝑠(𝑆𝑚) is the probability of winning the next point for a server, ¯𝑝𝑠(𝑆𝑚) denotes the mean number of points won on serve through the 𝑛𝑡ℎpoint of the match given a scoreline of 𝑆𝑚. 𝜂(𝑆𝑚) is a dynamic weight that reflects in-match performance, varying between 0 and 1. Setting it to a constant 1 makes ˆ𝑝𝑠(𝑆𝑚) = 𝑝0, effectively disregarding in-match performance. Consequently, momentum, which is influenced by the flow of points within the match, ceases to be a factor as it no longer affects the win probability of subsequent points. 𝑝0 is the probability of winning the first point as stated in the section above. The parameter 𝜂(𝑆𝑚) balances the pre-match and in-match serve information, with larger 𝜂(𝑆𝑚) values placing more emphasis on pre-match serve expectations. 𝜂(𝑆𝑚) is calculated by

<!-- b000234 | prose | pages [10] -->
𝜂(𝑆𝑚) = 𝛼/(𝛼+ 𝑛) (7)

<!-- b000235 | prose | pages [10, 11] -->
where 𝑛represents the number of points played on serve by the current player, while 𝛼is proportional to 𝜂and represents the pre-match confidence in a player’s serving performance, quantifying the in-match evidence needed to revise these pre-match expectations. We aim to optimize 𝑛𝑠and 𝑛𝑟to minimize inconsistencies between dynamic and pre-match serve expectations, as well as the error between observed and dynamic expectations, by minimizing a specific loss function

<!-- b000236 | furniture | pages [10] -->
关注数学模型

<!-- b000237 | furniture | pages [10] -->
2

<!-- b000238 | furniture | pages [10] -->
MATHmodels

<!-- b000239 | furniture | pages [10] -->
获取更多资讯

<!-- b000240 | furniture | pages [11] -->
Team # 2406176

<!-- b000241 | furniture | pages [11] -->
Page 11 of 27

<!-- b000243 | prose | pages [11] -->
𝐿𝑜𝑠𝑠(𝑛) = −1  (𝑦𝑖log( ¯𝑝𝑠(𝑆𝑖)) + (1 −𝑦𝑖) log(1 −¯𝑝𝑠(𝑆𝑖))) + ( ¯𝑝𝑠(𝑆𝑖) −𝑝0)2 ∑︁ 𝜆𝑖 微信公众号：数学模型 (8) 𝑚 𝑖

<!-- b000244 | prose | pages [11] -->
where 𝑦𝑖represents the number of points a server has won out of 𝑚service points. In any game, an athlete’s performance in the moment of the game is more indicative of subsequent performance than performance early in the game. Therefore the dynamic weight 𝜆𝑖is calculated as

<!-- b000245 | prose | pages [11] -->
𝑖 𝜆𝑖= (9) Í𝑚 𝑖=1 𝑖

<!-- b000246 | prose | pages [11] -->
We take the match between Carlos and Nicolas for instance, and the result is shown in the figure below.

<!-- b000247 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000248 | caption | pages [11] -->
Figure 5: Real-time changes in Carlos’s and Nicolas’s next point winning probability

<!-- b000249 | prose | pages [11] -->
The figure clearly indicates a significant serving side advantage, which must be factored into player performance assessments. A server with a 51% win probability isn’t necessarily performing better than a receiver with a 49% win rate. Therefore, it is necessary to further eliminate this advantage.

<!-- b000250 | heading | pages [11] -->
5.4 Quantification of Momentum

<!-- b000251 | prose | pages [11] -->
With the win probability in real time, we are capable of acquiring the player’s performance in real time ( PA(𝑡) −𝑝𝐴 0 , if A is server MMTA(𝑡) = (10) PA(𝑡) −𝑝𝐴 0 + 𝜀, if A is receiver The real-time performance for Carlos and Nicolas in their matchup is indicated below.

<!-- b000252 | furniture | pages [11] -->
关注数学模型

<!-- b000253 | furniture | pages [11] -->
2

<!-- b000254 | furniture | pages [11] -->
MATHmodels

<!-- b000255 | furniture | pages [11] -->
获取更多资讯

<!-- b000256 | furniture | pages [12] -->
Team # 2406176

<!-- b000257 | furniture | pages [12] -->
Page 12 of 27

<!-- b000258 | prose | pages [12] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000259 | caption | pages [12] -->
Figure 6: Real-time momentum of Carlos and Nicolas

<!-- b000260 | prose | pages [12] -->
Carlos’s momentum curve shows more distinct peaks than Nicolas’s, indicating that Carlos’s performance is often significantly higher than his pre-match predictions compared to Nicolas’s, especially in the middle of the game where Carlos’s momentum peaks are almost exclusive (between point #100 and #200). This suggests that Carlos has a strong momentum that helps him dominate the game during mid-match, which ultimately contributes to winning the match.

<!-- b000261 | heading | pages [12] -->
5.4.1 Verification of the Significance of Momentum

<!-- b000262 | prose | pages [12] -->
To assess the role of momentum in tennis, we apply the Constant Win Probability (CWP) model by setting 𝜂(𝑆𝑚) = 1 in the Real-Time Win Probability (RTWP) model, thereby disregarding all in-match factors including momentum. We then consider the outcome of the CWP model as our observed value. If the coach’s assertion is incorrect, the residuals (the differences between the predicted and observed outcomes) would deviate from a normal distribution, indicating a discrepancy between the models and the observed results. We employ both qualitative (probability distribution plots of the residuals) and quantitative (K-S test) methods to evaluate the validity of the coach’s hypothesis. If the coach’s claim is disproven, it confirms the existence and significance of momentum in tennis matches, thereby validating the effectiveness of our RTWP and RTMQ models.

<!-- b000263 | prose | pages [12] -->
Probability Distribution Plot of the Residuals

<!-- b000264 | prose | pages [12] -->
We plot the distribution of the residual in the figure 7 below.

<!-- b000265 | prose | pages [12] -->
This clearly suggests a non-normal distribution, since the mean values of 𝜎are all larger than 0 and it is not distributed centrally symmetric, prompting us to use the K-S test for further investigation of the residuals’ distribution.

<!-- b000266 | furniture | pages [12] -->
关注数学模型

<!-- b000267 | furniture | pages [12] -->
2

<!-- b000268 | furniture | pages [12] -->
MATHmodels

<!-- b000269 | furniture | pages [12] -->
获取更多资讯

<!-- b000270 | furniture | pages [13] -->
Team # 2406176

<!-- b000271 | furniture | pages [13] -->
Page 13 of 27

<!-- b000272 | prose | pages [13] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000273 | caption | pages [13] -->
Figure 7: Probability distribution of the residual of Carlos Alcaraz and Nicolas Jarry

<!-- b000274 | prose | pages [13] -->
K-S Test to Investigate the Distribution

<!-- b000275 | prose | pages [13] -->
In this case, the Null Hypothesis (H0) is the coach’s statement that momentum does not play any role in the match. If H0 is true, then the residual should be close to a normal distribution. The pseudocode for K-S Test is shown below.

<!-- b000276 | heading | pages [13] -->
Algorithm 2 Kolmogorov-Smirnov (K-S) Test

<!-- b000277 | prose | pages [13] -->
Data: Residuals 𝜎

<!-- b000278 | heading | pages [13] -->
Result: K-S test statistic 𝐷, p-value 𝑝

<!-- b000279 | prose | pages [13] -->
begin Sort the residuals 𝜎in ascending order;

<!-- b000280 | prose | pages [13] -->
Set 𝑁as the number of residuals;

<!-- b000281 | prose | pages [13] -->
for 𝑖←1 to 𝑁do Calculate 𝐷+ = max(𝑖/𝑁−𝜎[𝑖−1]);

<!-- b000282 | prose | pages [13] -->
Calculate 𝐷−= max(𝜎[𝑖−1] −(𝑖−1)/𝑁);

<!-- b000283 | prose | pages [13] -->
end √ √ Calculate 𝐷= max( 𝑁· 𝐷+, 𝑁· 𝐷−);

<!-- b000284 | prose | pages [13] -->
𝑖=1(−1)𝑖−1𝑒−2𝑖2𝐷2; Calculate 𝑝= 1 −2 Í∞ return 𝐷, 𝑝;

<!-- b000285 | prose | pages [13] -->
end

<!-- b000286 | prose | pages [13] -->
Running the K-S test as introduced in the pseudocode above, using statistical software, results are shown in table 3 below. The p-value for both players is much smaller than 0.05 (the common chosen significance level). Therefore, we reject the H0 hypothesis and confirm the significance of momentum in tennis matches.

<!-- b000287 | furniture | pages [13] -->
关注数学模型

<!-- b000288 | furniture | pages [13] -->
2

<!-- b000289 | furniture | pages [13] -->
MATHmodels

<!-- b000290 | furniture | pages [13] -->
获取更多资讯

<!-- b000291 | furniture | pages [14] -->
Team # 2406176

<!-- b000292 | furniture | pages [14] -->
Page 14 of 27

<!-- b000293 | caption | pages [14] -->
Table 3: Significant symbols in this paper

<!-- b000294 | prose | pages [14] -->
𝐷Value 𝑝value 1.338386540467465e-62 << 0.05 Carlos 微信公众号：数学模型 0.49958267649880644 5.94542201790284e-56 << 0.05 Nicolas 0.47375107203988065

<!-- b000295 | heading | pages [14] -->
5.5 Momentum Trend Value (MMTTV) Visualization

<!-- b000296 | prose | pages [14] -->
Considering the volatility and periodicity of the real-time momentum curve, we apply Fourier series to fit the curve to eliminate the effects of cyclical fluctuations in win probabilities, acquiring the momentum trend value (MMTTV) in real time. Fourier series is a powerful mathematical tool that can be used to represent and analyze periodic functions. It describes a periodic function as a sum of sine and cosine functions. The general form of a Fourier series is ∞ 微信号：MATHmodels ∑︁ 𝑓(𝑥) = 𝑎0 + [𝑎𝑛cos(𝑛𝑤𝑥) + 𝑏𝑛sin(𝑛𝑤𝑥)] (11) 𝑛=1

<!-- b000297 | prose | pages [14] -->
Applying Fourier series curve fitting to our real-time momentum data, we finally capture the momentum trend and obtain the MMTTV data for both athletes, which is the blue line in the figure below.

<!-- b000298 | caption | pages [14] -->
Figure 8: The momentum trend value for both players

<!-- b000299 | prose | pages [14] -->
It is easy to see from the figure that a dramatic momentum shift occurred near point #130, when Carlos’ momentum reached over 0.23 and Nicolas’ momentum dropped to about 0.06, turning the situation around and leading to the swing. The final success of Carlos is therefore closely related to this momentum shift, and subsequent sustained rises in Nicolas’ momentum did not positively affect his final result.

<!-- b000300 | furniture | pages [14] -->
关注数学模型

<!-- b000301 | furniture | pages [14] -->
2

<!-- b000302 | furniture | pages [14] -->
MATHmodels

<!-- b000303 | furniture | pages [14] -->
获取更多资讯

<!-- b000304 | furniture | pages [15] -->
Team # 2406176

<!-- b000305 | furniture | pages [15] -->
Page 15 of 27

<!-- b000306 | heading | pages [15] -->
6 Swing Prediction Model

<!-- b000307 | heading | pages [15] -->
6.1 Data Preprocessing

<!-- b000308 | prose | pages [15] -->
微信公众号：数学模型 In the Wimbledon_featured_matches.csv, columns AQ(speed_mph), AR(serve_width), AS (serve_depth), AT(return_depth) have missing values (NA). They are handled as follows:

<!-- b000309 | prose | pages [15] -->
Step 1: Address missing values in columns AR, AS, AT.

<!-- b000310 | prose | pages [15] -->
• If either column AB or AC in a row is 1, replace NA in columns AR, AS, AT of these rows with ’F’ (Fail). This is because columns AB and AC represent points lost due to player errors. We assume that the NA values in these cases are unclassified results caused by errors.

<!-- b000311 | prose | pages [15] -->
• If any of the columns U, V, W, X in a row is 1, replace NA in columns AR, AS, AT of these rows with ’UN’ (Unknown). Columns U, V, W, X represent points scored due to high-quality shots (serve/return), with NA values attributed to unknown factors.

<!-- b000312 | prose | pages [15] -->
微信号：MATHmodels Step 2: Address missing values in column AQ .

<!-- b000313 | prose | pages [15] -->
• Exclude the matches between Daniel Elahi Galan and Mikael Ymer, and between Guido Pella and Roman Safiullin. This is because ball speed and rally count are both crucial technical indicator in tennis, and these matches lack the two records.

<!-- b000314 | prose | pages [15] -->
• If any of the columns U, V, W, X, AB, AC, AD, AE, AF, AG in a row is 1, replace the NA in column AQ with the average ball speed of the match. This is because the absence of ball speed data for high-quality shots, error shots, and net shots may be due to errors in the data recording process or factors that make the data unrecordable.

<!-- b000315 | heading | pages [15] -->
6.2 Indicators Calculation

<!-- b000316 | prose | pages [15] -->
Key indicators are calculated based on previous research and experience. We have identified 25 indicators based on the mainstream technical indicators in tennis, related scientific research papers and professional analysis. Due to their excessive number, our paper shows the calculation of only 3 of the indicators, the calculation and explanation of all indicators is in Appendix A.

<!-- b000317 | prose | pages [15] -->
n(ace) Aces_p𝑖= n(successful serves) Break_p𝑖= n(server = 𝑗, break_pt_won = 𝑖) n(server = 𝑗, break_pt = 1) (12) n(server = 𝑖, serve_depth = 𝐶𝑇𝐿) Depth_CTL_p𝑖= n(server = 𝑖, serve_depth ≠unknown) ...

<!-- b000318 | prose | pages [15] -->
where Aces_p𝑖represents the proportion of successful serves by player 𝑖that are aces, Break_p𝑖rep- resents the proportion of break points won by player 𝑖when player 𝑗is serving, and Depth_CTL_p𝑖 represents the proportion of serves by player 𝑖that land in the “CTL” (Close To Line) depth zone.

<!-- b000319 | furniture | pages [15] -->
关注数学模型

<!-- b000320 | furniture | pages [15] -->
2

<!-- b000321 | furniture | pages [15] -->
MATHmodels

<!-- b000322 | furniture | pages [15] -->
获取更多资讯

<!-- b000323 | furniture | pages [16] -->
Team # 2406176

<!-- b000324 | furniture | pages [16] -->
Page 16 of 27

<!-- b000325 | heading | pages [16] -->
6.3 Exploratory Factor Analysis

<!-- b000326 | prose | pages [16] -->
Given the multitude of performance indicators for a player, we use a Factor Analysis Model to distill key factors that better represent the player’s technical performance. Therefore, all indicators 微信公众号：数学模型 can be quantified by the factors with the corresponding weights. Let 𝑋𝑝(𝑝= 1, 2, ..., 25) represent all indicators, and they can be represented by weighted factors as follows

<!-- b000327 | prose | pages [16] -->
𝑋1 𝜇1 𝛼11 𝛼12 𝛼1𝑚 𝐹1 𝜀1 · · ·           𝑋2 𝜇2 𝛼21 𝛼22 𝛼2𝑚 𝐹2 𝜀2 · · · ... ... ... ... ... ... ... + + = (13)

<!-- b000328 | prose | pages [16] -->
𝑋𝑝 𝜇𝑝 𝛼𝑝1 𝛼𝑝2 𝛼𝑝𝑚 𝐹𝑚 𝜀𝑝 · · ·

<!-- b000329 | prose | pages [16] -->
where 𝐹1, 𝐹2, ..., 𝐹𝑚are factors that are unobservable, 𝛼𝑖𝑗is the weight matrix of the factors, 𝜇𝑖 is the mean of the variable 𝑋𝑖and 𝜀𝑖is the unique or error term for the variable 𝑋𝑖. The constraints of the model are 微信号：MATHmodels 𝑐𝑜𝑣(𝐹, 𝜀) = 0, 𝐷(𝐹𝑖) = 1, 𝐷(𝜀𝑖) = 𝜎2 (14) 𝑖

<!-- b000330 | prose | pages [16] -->
Indicators undergo z-score normalization to normalize their scale and mitigate the effect of different units or magnitudes prior to factor analysis. We perform a Bartlett’s Test of Sphericity to determine if there is a high degree of internal correlation in the data. If so, factor analysis is performed.

<!-- b000331 | heading | pages [16] -->
Algorithm 3 Bartlett’s Test of Sphericity

<!-- b000332 | prose | pages [16] -->
Data: Indicator matrix X Result: Test statistic, p-value, and a decision on whether the data need to be factor analyzed begin 𝜒2 = −log(det(𝑅))(𝑁−1 −2𝑛+5 6 ) where 𝑅is the correlation matrix of the dataset, 𝑁= 109 (number of data points), 𝑛= 25;

<!-- b000333 | prose | pages [16] -->
𝜒2, 𝑝(𝑝+1)   𝑝= 1 −𝐹𝜒2 −1 ; 2 if 𝑝< 0.05 then The data is appropriate for factor analysis.;

<!-- b000334 | prose | pages [16] -->
end else The data is not appropriate for factor analysis.;

<!-- b000335 | prose | pages [16] -->
end end

<!-- b000336 | prose | pages [16] -->
The test tells us 𝑝< 0.05, so we performed factor analysis. We extract five factors. Taking 3 factors as an example and looking at the factor loading matrix, we found:

<!-- b000337 | prose | pages [16] -->
• For Factor 1, Aces_p𝑖(0.754), 1st_srv_won_p𝑖(0.730), and Width_W_p𝑖(0.685) have the highest absolute factor loadings, which indicates that Factor 1 characterizes the player’s ability to win points and quality of play as a server. Since this factor is almost entirely related to server metrics, we treat Factor 1 as a factor specializing in server ability.

<!-- b000338 | furniture | pages [16] -->
关注数学模型

<!-- b000339 | furniture | pages [16] -->
2

<!-- b000340 | furniture | pages [16] -->
MATHmodels

<!-- b000341 | furniture | pages [16] -->
获取更多资讯

<!-- b000342 | furniture | pages [17] -->
Team # 2406176

<!-- b000343 | furniture | pages [17] -->
Page 17 of 27

<!-- b000344 | prose | pages [17] -->
• For Factor 2, Depth_CTL_p𝑖(0.792) and Net_pt_won_p𝑖(0.568) have the highest absolute factor loadings. As a result of our research, we found that when a player tends to hit a CTL ball, it is likely that the player will need to run longer distances faster to receive the ball. Thus Factor 2 characterizes whether the player tends to put more or less effort into the play. 微信公众号：数学模型

<!-- b000345 | prose | pages [17] -->
• For Factor4, 1st_srv_drt_won_p𝑖(0.710), Winners4_p𝑖(-0.649), andSrv_avg_speed_p𝑖(0.632) have the highest absolute values of the factor loadings. Thus Factor 4 indicates the player’s explosive ability, especially the ability to win the ball in the serve-receive phase.

<!-- b000346 | prose | pages [17] -->
We name the Factor 1 as AggressiveServe, Factor 2 as ExtendedPlay, Factor 3 as Endurance, Factor 4 as ActiveDefense, and Factor 5 as ForehandBias based on the characteristics of the indicators they contain and the characteristics of the factor loading matrix.

<!-- b000347 | heading | pages [17] -->
6.4 Prediction of Swing Based on Multivariate Linear Regression Model

<!-- b000348 | prose | pages [17] -->
We utilize a Multivariate Linear Regression Model to predict tangible momentum shifts, 微信号：MATHmodels or swings, in tennis matches. Our model operates on a per-set basis, as a set provides a more comprehensive dataset for analysis compared to individual games. This approach minimizes the impact of outliers and enhances the reliability of the player’s performance evaluation. For instance, a shift from high to low momentum of two sets often indicates a potential swing (tends to lose the game or even match). We sample the momentum trend value (MMTTV) from the momentum trend at the end of each set. This is because the frequent in-set momentum shifts can render predictions based on real-time momentum data at the end of each set unreliable. By calculating the MMTTV values and other metrics at the end of each set, we align our methodology with previous research and established analytical strategies in sports media, thereby ensuring a robust prediction of momentum shifts. The subsequent section outlines the training process for the multivariate linear regression model that can be executed across numerous software platforms.

<!-- b000349 | heading | pages [17] -->
Algorithm 4 Multivariate Linear Regression

<!-- b000350 | prose | pages [17] -->
Data: Factor matrix (the 5 factors) X, Target vector MMTTV at the end of each set

<!-- b000351 | heading | pages [17] -->
Result: Coefficients of the 5 factors 𝛽, Predictions

<!-- b000352 | prose | pages [17] -->
ˆ MMTTV begin Initialize coefficients 𝛽for each feature in X to 0;

<!-- b000353 | prose | pages [17] -->
Set learning rate 𝛼and convergence threshold 𝜖;

<!-- b000354 | prose | pages [17] -->
while not converged do ˆ 1 MMTTV = Calculate the predicted probabilities 1+𝑒−X𝛽; Calculate the gradient 𝑘= X𝑇( ˆ MMTTV −MMTTV);

<!-- b000355 | prose | pages [17] -->
Update coefficients 𝛽= 𝛽−𝛼𝑘;

<!-- b000356 | prose | pages [17] -->
If ||𝑘|| < 𝜖, set converged to True;

<!-- b000357 | prose | pages [17] -->
end return 𝛽, ˆ MMT;

<!-- b000358 | prose | pages [17, 18] -->
end We take the match between Carlos and Nicolas for testing our prediction model, and the result is shown in the figure below, indicating an accurate prediction.

<!-- b000359 | furniture | pages [17] -->
关注数学模型

<!-- b000360 | furniture | pages [17] -->
2

<!-- b000361 | furniture | pages [17] -->
MATHmodels

<!-- b000362 | furniture | pages [17] -->
获取更多资讯

<!-- b000363 | furniture | pages [18] -->
Team # 2406176

<!-- b000364 | furniture | pages [18] -->
Page 18 of 27

<!-- b000366 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000367 | caption | pages [18] -->
Figure 9: Prediction of the value of momentum for both players

<!-- b000368 | prose | pages [18] -->
微信号：MATHmodels The result agrees well with the real-time MMTTV of the two athletes, with the peak and trough in both figures occurring at the end of the second set. Sorting the weights of the factors, AggressiveServe have the largest absolute weights, indicating that they are the most related factors to predict the swings in the match. It is reasonable because serve ability and aggressiveness are the most central indicators of a good or bad server’s ability. From the figure below we can see the trend of the indicators are similar to that of the momentum curve.

<!-- b000369 | heading | pages [18] -->
7 Mixed-Strategy Nash Equilibrium Model

<!-- b000370 | prose | pages [18] -->
In the dynamic world of tennis, players strategically adopt different tactics with a certain probability during a match to maximize their chances of winning. The choice of strategy, whether for serving or receiving, can significantly affect the outcome of the game, creating a complex web of decisions. To analyze this intricate web of strategic choices, we have adopted a Mixed-Strategy Nash Equilibrium model. This model serves as a tool for predicting the most common combinations of strategies employed by players prior to the game. As the match unfolds, the model allows us to observe shifts in players’ strategies, providing valuable insights into which strategies a player must pursue to gain an upper hand. Through our model, we aim to unravel the probabilistic nature of strategic decision-making in tennis, paving the way for more informed and effective strategies.

<!-- b000371 | heading | pages [18] -->
7.1 Strategy Payoff Calculation

<!-- b000372 | prose | pages [18] -->
First we define the set of possible strategies that the opponent in the upcoming match (assume that we need to study Stefanos Tsitsipas) may adopt. The strategies of the players can be characterized by the factors we define previously. We compute the factor value at the end of each set in the dataset, followed by cluster analysis in unsupervised learning.

<!-- b000373 | prose | pages [18] -->
We tried clustering the dataset and found that the set of strategies makes the most sense when the number of clusters is 4 for the server and 3 for the receiver. Strategies that can be adopted by servers are as follows:

<!-- b000374 | prose | pages [18, 19] -->
• Server Strategy 1: A=0.83, B=0.72, C=0.63, E=0.49. This indicates a steep angle and fast ball speed, therefore the strategy is named Side-Tearing Assault.

<!-- b000375 | furniture | pages [18] -->
关注数学模型

<!-- b000376 | furniture | pages [18] -->
2

<!-- b000377 | furniture | pages [18] -->
MATHmodels

<!-- b000378 | furniture | pages [18] -->
获取更多资讯

<!-- b000379 | furniture | pages [19] -->
Team # 2406176

<!-- b000380 | furniture | pages [19] -->
Page 19 of 27

<!-- b000382 | prose | pages [19] -->
• Server Strategy 2: A=0.69, B=0.31, C=0.76, E=0.79. This describes the tendency of players to use a variety of stroke speeds, stroke angles, and different ball paths to control the pace of 微信公众号：数学模型 play, thus named Pace Control.

<!-- b000383 | prose | pages [19] -->
• Server Strategy 3: A=0.25, B=0.66, C=0.87, E=0.69. This suggests that the player tends to play each point longer, and play faster, close-to-net balls, so that the opponent is forced to go to the net and might make a mistake, thus named Low-Bounce Onslaught.

<!-- b000384 | prose | pages [19] -->
• Server Strategy 4: A=0.44, B=0.52, C=0.55, E=0.54. This suggests that players adopt slower ball speeds and hit a lot of approach shots, which is easy to create errors for the opponent, thus named Short-Ball Maneuver.

<!-- b000385 | prose | pages [19] -->
For receiver strategies:

<!-- b000386 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000387 | prose | pages [19] -->
• Receiver Strategy 1 (Bottom Line Defense): With B=0.29, C=0.67, D=0.54, E=0.88, the player tends to conserve energy, engage in extended rallies, and favor forehand shots. This strategy, characterized by precise stroke and angle control from the baseline, is a common defensive approach.

<!-- b000388 | prose | pages [19] -->
• Receiver Strategy 2 (Defense at the Net): With B=0.73, C=0.21, D=0.61, E=0.46, the player prefers to conserve energy, end points quickly, and actively defend. This strategy often involves moving to the net to counter strong baseline attacks from the opponent.

<!-- b000389 | prose | pages [19] -->
• Receiver Strategy 3 (Deep Defense): With B=0.77, C=0.87, D=0.49, E=0.81, the receiver tends to play long points with a significant forehand bias. This strategy aims to provide the player with more reaction time and make it challenging for the opponent to execute an effective attack.

<!-- b000390 | prose | pages [19] -->
The values of each factor in all strategies are shown in figure 10 below.

<!-- b000391 | caption | pages [19] -->
Figure 10: The value of factors for strategies of both servers and receivers

<!-- b000392 | furniture | pages [19] -->
关注数学模型

<!-- b000393 | furniture | pages [19] -->
2

<!-- b000394 | furniture | pages [19] -->
MATHmodels

<!-- b000395 | furniture | pages [19] -->
获取更多资讯

<!-- b000396 | furniture | pages [20] -->
Team # 2406176

<!-- b000397 | furniture | pages [20] -->
Page 20 of 27

<!-- b000398 | prose | pages [20] -->
We incorporate the median value of each strategy cluster into our Swing Prediction Model to predict the MMT value for each corresponding strategy. This predicted value represents the exact payoff of the strategy and is used to calculate the expected payoffs below.

<!-- b000399 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000400 | heading | pages [20] -->
7.2 Model Setup

<!-- b000401 | prose | pages [20] -->
Mixed Strategies. A mixed strategy for player 𝑖is defined as a probability distribution over the set of pure strategies. Let 𝑛𝑖denote the number of pure strategies available to player 𝑖. A mixed strategy for player 𝑖(the player is a server or a receiver) can then be represented as a vector

<!-- b000402 | prose | pages [20] -->
p𝑖= (𝑝𝑖1, 𝑝𝑖2, ..., 𝑝𝑖𝑛𝑖) (15)

<!-- b000403 | prose | pages [20] -->
where 𝑝𝑖𝑗is the probability that player 𝑖will play pure strategy 𝑗. These probabilities are non- negative and sum to 1 𝑛𝑖 ∑︁ 𝑝𝑖𝑗≥0, 𝑝𝑖𝑗= 1 (16) 𝑗=1 微信号：MATHmodels Expected Payoffs. The expected payoff for player 𝑖given a profile of mixed strategies p is calculated as the sum of the payoffs for each possible outcome, weighted by the probability of that outcome. If 𝑢𝑖(𝑠1, ..., 𝑠𝑛) denotes the payoff to player 𝑖for strategy profile (𝑠1, ..., 𝑠𝑛), the expected payoff is given by: 𝑛 ∑︁ ∑︁ Ö 𝐸[𝑢𝑖(p)] = ... 𝑢𝑖(𝑠1, ..., 𝑠𝑛) 𝑝𝑗𝑠𝑗 (17) 𝑠1 𝑠𝑛 𝑗=1

<!-- b000404 | prose | pages [20] -->
Best Responses. A best response for player 𝑖is a strategy that maximizes player 𝑖’s expected payoff, given the strategies of the other players. Formally, a best response p∗ 𝑖satisfies

<!-- b000405 | prose | pages [20] -->
p∗ p𝑖𝐸[𝑢𝑖(p𝑖, p−𝑖)] 𝑖∈arg max (18)

<!-- b000406 | prose | pages [20] -->
Nash Equilibrium. A mixed-strategy Nash equilibrium is a strategy profile where every player’s strategy is a best response to the strategies of the other players. Formally, a strategy profile 1, ..., p∗ 𝑛) is a Nash equilibrium if and only if for all 𝑖 p∗= (p∗

<!-- b000407 | prose | pages [20] -->
p∗ p𝑖𝐸[𝑢𝑖(p𝑖, p∗ 𝑖∈arg max −𝑖)] (19)

<!-- b000408 | prose | pages [20] -->
In other words, no player can improve their expected payoff by unilaterally deviating from their equilibrium strategy. Bringing our strategies into the model, the probability combination of strategies that our player should take to against Stefanos Tsitsipas is shown in figure 11 below.

<!-- b000409 | furniture | pages [20] -->
关注数学模型

<!-- b000410 | furniture | pages [20] -->
2

<!-- b000411 | furniture | pages [20] -->
MATHmodels

<!-- b000412 | furniture | pages [20] -->
获取更多资讯

<!-- b000413 | furniture | pages [21] -->
Team # 2406176

<!-- b000414 | furniture | pages [21] -->
Page 21 of 27

<!-- b000415 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000416 | caption | pages [21] -->
Figure 11: Optimized combination of strategies when S.T. is server and R.S. is receiver

<!-- b000417 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000418 | heading | pages [21] -->
8 Test of FSF Model and SP Model

<!-- b000419 | prose | pages [21] -->
After completing the construction of FSF and SP model, we used the data of other matches as a test set to verify the accuracy of our model’s predictive ability. Here we use the FSF model instead of the RTMQ model because we want to track the momentum trend without the frequent shifts in the RTMQ model.

<!-- b000420 | heading | pages [21] -->
8.1 The Match between Alcaraz and Djokovic

<!-- b000421 | prose | pages [21] -->
First, we selected one of the most exciting match, the Grand Slam championship match between the young Carlos Alcaraz and the veteran Novak Djokovic(The match number:1701). Inputting the point-by-point data into our model generate the MMTTV prediction. Fig.x demonstrates that, despite both players’ high levels, their MMTTVs closely overlapped, reflecting the match’s intensity. Analysis showed MMTTV aligned with the actual match: Djokovic led early, Alcaraz caught up, and Djokovic surged again before Alcaraz prevailed. This trend was consistent across multiple matches, confirming the model’s accuracy.

<!-- b000422 | caption | pages [21] -->
Figure 12: FSF model and SP model results

<!-- b000423 | furniture | pages [21] -->
关注数学模型

<!-- b000424 | furniture | pages [21] -->
2

<!-- b000425 | furniture | pages [21] -->
MATHmodels

<!-- b000426 | furniture | pages [21] -->
获取更多资讯

<!-- b000427 | furniture | pages [22] -->
Team # 2406176

<!-- b000428 | furniture | pages [22] -->
Page 22 of 27

<!-- b000429 | heading | pages [22] -->
8.2 Model Generalization

<!-- b000430 | prose | pages [22] -->
To assess our model’s generalization, we used men’s singles data from the 2017 French Open, which shares similarities with the 2023 Wimbledon Championships, including the best-of-five set 微信公众号：数学模型 format and IBM Slamtracker data collection. Despite differences in court surfaces (red clay vs. grass), our model maintained prediction accuracy, indicating good generalization.

<!-- b000431 | prose | pages [22] -->
In particular, the match between Andy Murray and Andrey Kuznetsov highlighted the model’s reliability. Murray’s dominance, reflected in his MMTTV, aligned with our predictions and the match’s outcome, further confirming the model’s effectiveness.

<!-- b000432 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000433 | caption | pages [22] -->
Figure 13: FSF model and SP model results

<!-- b000434 | heading | pages [22] -->
8.3 Contextual Limitations in SP Model

<!-- b000435 | prose | pages [22] -->
When applying SP model to conduct MMTTV predictions and dynamic game strategy selec- tions, we observed that players balance their tactical strategies based on their own abilities and those of their opponents. Within a single match context (e.g., all matches in the 2023 Wimbledon Championships can be considered as having a consistent background), the model’s predictions are accurate. However, when generalizing the model to different match contexts, various factors such as the court’s impact on tennis ball bounce, climatic conditions influenced by the time of the season, and other contextual elements prevent us from directly unifying datasets from different matches to make sufficiently accurate predictions for a player facing a new opponent in a different match context. For instance, knowing Roman Safiullin’s performance data only from grass courts at Wimbledon makes it challenging to predict his strategic choices when playing on clay courts.

<!-- b000436 | heading | pages [22] -->
8.4 Key Indicators to be Included in Future Models

<!-- b000437 | prose | pages [22] -->
Beyond the generalization verification with the French Open dataset, we further discuss the model’s generalization potential. Given the rule differences between men’s and women’s singles tennis, extending our model to women’s singles or tournaments would require reconsidering the change from best-of-five to best-of-three sets. This necessitates rederiving the initial value cali- bration’s independent and identically distributed assumption. Extending the model to other racket sports with a net, such as table tennis, would involve redefining technical indicators based on rule variations and performing common factor analysis across different sports, incorporating relevant technical analyses.

<!-- b000438 | furniture | pages [22] -->
关注数学模型

<!-- b000439 | furniture | pages [22] -->
2

<!-- b000440 | furniture | pages [22] -->
MATHmodels

<!-- b000441 | furniture | pages [22] -->
获取更多资讯

<!-- b000442 | furniture | pages [23] -->
Team # 2406176

<!-- b000443 | furniture | pages [23] -->
Page 23 of 27

<!-- b000444 | heading | pages [23] -->
9 Sensitivity Analysis

<!-- b000445 | prose | pages [23] -->
We conduct a sensitivity analysis on our model to assess its stability under external distur- bances, thereby highlighting its advantages. As shown in Fig.x, when we alter the initial game 微信公众号：数学模型 win probability as input, the overall trend prediction curve exhibited minimal translation despite significant deviations in the initial values. The stability of the curve trend remain intact, ensuring no impact on our MMT swing predictions. This demonstrates the strong robustness of our model.

<!-- b000446 | prose | pages [23, 24] -->
微信号：MATHmodels To: Coaches

<!-- b000447 | caption | pages [23] -->
Figure 14: Sensitivity analysis of MMT model

<!-- b000448 | furniture | pages [23] -->
关注数学模型

<!-- b000449 | furniture | pages [23] -->
2

<!-- b000450 | furniture | pages [23] -->
MATHmodels

<!-- b000451 | furniture | pages [23] -->
获取更多资讯

<!-- b000452 | furniture | pages [24] -->
Team # 2406176

<!-- b000453 | furniture | pages [24] -->
Page 24 of 27

<!-- b000455 | prose | pages [24] -->
From: Team # 2406176

<!-- b000456 | prose | pages [24] -->
Date: Feb.5th, 2024 微信公众号：数学模型

<!-- b000457 | heading | pages [24] -->
MEMO: Summary of Tennis Momentum Analysis and Coaching Recommendations

<!-- b000458 | prose | pages [24] -->
We are pleased to provide you with a summary of our recent research on tennis momentum dynamics and the development of predictive models. Our research focuses on the Real-Time Momentum Quantification (RTMQ) Model, Swing Prediction (SP) Model, and the application of the Mixed-Strategy Nash Equilibrium Model in tennis matches.

<!-- b000459 | prose | pages [24] -->
Our findings suggest that momentum plays a significant role in tennis matches. The RTMQ model quantifies momentum by considering the disparity between pre-match and real-time win probabilities. The model calculates the difference between real-time and pre-match win rates under 微信号：MATHmodels separate serve/receive conditions, taking into account the serving side’s advantage. The K-S test confirms the significance of momentum, rejecting the hypothesis that in-match performance is inconsequential.

<!-- b000460 | prose | pages [24] -->
The Swing Prediction (SP) Model operates on a per-set basis and exhibits an impressive 90.44% prediction accuracy for large momentum shifts. The model uses specialized indicators, such as 2nd_serve_direct_won and Net_approach_point_won, to predict momentum swings. These factors contribute significantly to player momentum and can be used to prepare players to respond effectively to events that impact the flow of play during a tennis match.

<!-- b000461 | prose | pages [24] -->
The Mixed-Strategy Nash Equilibrium Model provides insights into optimal strategic combinations against diverse opponents. The model uses K-means clustering to identify strategic clusters for tailored strategies. Coaches can use this model to prepare players to respond effectively to different opponents and adjust their strategies accordingly.

<!-- b000462 | prose | pages [24] -->
In conclusion, our research equips coaches with advanced tools and insights to navigate the intricate landscape of tennis momentum. Incorporating these findings into coaching strategies will enhance players’ ability to respond effectively to events impacting the flow of play, contributing to improved match outcomes. We recommend that coaches integrate these findings into their training programs to improve players’ responsiveness to dynamic events during matches.

<!-- b000463 | prose | pages [24] -->
Feel free to reach out for further discussion or clarification.

<!-- b000464 | prose | pages [24] -->
Best Regards,

<!-- b000465 | furniture | pages [24] -->
Team # 2406176

<!-- b000466 | furniture | pages [24] -->
关注数学模型

<!-- b000467 | furniture | pages [24] -->
2

<!-- b000468 | furniture | pages [24] -->
MATHmodels

<!-- b000469 | furniture | pages [24] -->
获取更多资讯

<!-- b000470 | furniture | pages [25] -->
Team # 2406176

<!-- b000471 | furniture | pages [25] -->
Page 25 of 27

<!-- b000472 | heading | pages [25] -->
References

<!-- b000473 | references | pages [25] -->
[1] Angelini, G.; Candila, V.; De Angelis, L. Weighted Elo Rating for Tennis Match

<!-- b000474 | references | pages [25] -->
Predictions. European Journal of Operational Research 2022,

<!-- b000475 | references | pages [25] -->
297 (1),

<!-- b000476 | references | pages [25] -->
120–132.

<!-- b000477 | references | pages [25] -->
微信公众号：数学模型

<!-- b000478 | references | pages [25] -->
https://doi.org/10.1016/j.ejor.2021.04.011.

<!-- b000479 | references | pages [25] -->
[2] Newton, P. K.; Keller, J. B. Probability of Winning at Tennis I. Theory and Data. Stud Appl

<!-- b000480 | references | pages [25] -->
Math 2005, 114 (3), 241–269. https://doi.org/10.1111/j.0022-2526.2005.01547.x.

<!-- b000481 | references | pages [25] -->
[3] Sarcevic, A.; Vranic, M.; Pintar, D.; Krajna, A. Predictive Modeling of Tennis Matches:

<!-- b000482 | references | pages [25] -->
A Review. In 2022 45th Jubilee International Convention on Information, Communica-

<!-- b000483 | references | pages [25] -->
tion and Electronic Technology (MIPRO); IEEE: Opatĳa, Croatia, 2022; pp 1099–1104.

<!-- b000484 | references | pages [25] -->
https://doi.org/10.23919/MIPRO55190.2022.9803645.

<!-- b000485 | references | pages [25] -->
[4] Newton, P. K.; Aslam, K. Monte Carlo Tennis: A Stochastic Markov Chain Model. Journal

<!-- b000486 | references | pages [25] -->
of Quantitative Analysis in Sports 2009, 5 (3). https://doi.org/10.2202/1559-0410.1169.

<!-- b000487 | references | pages [25] -->
微信号：MATHmodels

<!-- b000488 | references | pages [25] -->
[5] Dietl, H. M.; Nesseler, C. Momentum in Tennis: Controlling the Match.

<!-- b000489 | references | pages [25] -->
[6] Šarčević, A.; Pintar, D.; Vranić, M.; Gojsalić, A. Modeling In-Match Sports Dynam-

<!-- b000490 | references | pages [25] -->
ics Using the Evolving Probability Method. Applied Sciences 2021, 11 (10), 4429.

<!-- b000491 | references | pages [25] -->
https://doi.org/10.3390/app11104429.

<!-- b000492 | references | pages [25] -->
[7] Glass, A. J.; Kenjegalieva, K.; Taylor, J. Game, Set and Match:

<!-- b000493 | references | pages [25] -->
Evaluating the Ef-

<!-- b000494 | references | pages [25] -->
ficiency of Male Professional Tennis Players. J Prod Anal 2015, 43 (2), 119–131.

<!-- b000495 | references | pages [25] -->
https://doi.org/10.1007/s11123-014-0401-3.

<!-- b000496 | references | pages [25] -->
[8] Klaassen, F. J. G. M.; Magnus, J. R. Forecasting the Winner of a Tennis Match. European

<!-- b000497 | references | pages [25] -->
Journal of Operational Research 2003, 148 (2), 257–267. https://doi.org/10.1016/S0377-

<!-- b000498 | references | pages [25] -->
2217(02)00682-3.

<!-- b000499 | references | pages [25] -->
[9] Bouzidis, T.; Karagiannis, G. Extending the Zero-Sum Gains Data Envelopment Analysis

<!-- b000500 | references | pages [25] -->
Model. J Prod Anal 2022, 58 (2–3), 171–184. https://doi.org/10.1007/s11123-022-00644-1.

<!-- b000501 | references | pages [25] -->
[10] Kovalchik, S.; Reid, M. A Calibration Method with Dynamic Updates for Within-Match

<!-- b000502 | references | pages [25] -->
Forecasting of Wins in Tennis. International Journal of Forecasting 2019, 35 (2), 756–766.

<!-- b000503 | references | pages [25] -->
https://doi.org/10.1016/j.ĳforecast.2017.11.008.

<!-- b000504 | references | pages [25] -->
[11] Shi Fuying, Zhang Hui, Liang Chengjun. Development of a Technical and Tactical Decision-

<!-- b000505 | references | pages [25] -->
Making Analysis System for Tennis Matches [J]. Journal of Beĳing Sport University, 2010,

<!-- b000506 | references | pages [25] -->
33(09): 129-132+138. DOI: 10.19582/j.cnki.11-3785/g8.2010.09.037.

<!-- b000507 | references | pages [25] -->
[12] Tao Zhixiang. Research on the Basic Unit of Athletic Process in Men’s Single Events of

<!-- b000508 | references | pages [25] -->
Racket Net Sports [D]. Beĳing Sport University, 2003.

<!-- b000509 | references | pages [25] -->
[13] Ferrante, Marco & Fonseca, Giovanni & Carrari, Andrea. (2017). A new marko-

<!-- b000510 | references | pages [25] -->
vian model for tennis matches. Electronic Journal of Applied Statistical Analysis. 10.

<!-- b000511 | references | pages [25] -->
10.1285/i20705948v10n3p693.

<!-- b000512 | furniture | pages [25] -->
关注数学模型

<!-- b000513 | furniture | pages [25] -->
2

<!-- b000514 | furniture | pages [25] -->
MATHmodels

<!-- b000515 | furniture | pages [25] -->
获取更多资讯

<!-- b000516 | furniture | pages [26] -->
Team # 2406176

<!-- b000517 | furniture | pages [26] -->
Page 26 of 27

<!-- b000518 | heading | pages [26] -->
Appendices

<!-- b000519 | prose | pages [26, 27] -->
Indicators in Swing Prediction Model in 6.2 微信公众号：数学模型 n(ace) Aces_p𝑖= n(successful serves) 2 ∗n(winner) Winners_p𝑖= n(rally) −n(server) + n(winner) n(winner | rally_n ≥4) Winners4_p𝑖= 2 ∗ n(rally | rally ≥4) −n(server | rally_n ≥4) + n(winner | rally_n ≥4) n(winner |1 ≤rally_n ≤3) Winners13_p𝑖= 2 ∗ n(rally | 1 ≤rally_n ≤3) −n(server | 1 ≤rally_n ≤3) + n(winner | 1 ≤rally_n ≤3) Double_fault_p𝑖= count(double_fault) count(server) 1st_srv_in_p𝑖= count(server | serve_no = 1) 微信号：MATHmodels serve_sum 2nd_srv_in_p𝑖= count(server | serve_no = 2, double_fault = 0) serve_sum 1st_srv_won_p𝑖= n(server | serve_no = 1, point_victor = 𝑖) n(server | serve_no = 1) 2nd_srv_won_p𝑖= n(server | serve_no = 2, point_victor = 𝑖) n(server | serve_no = 2) Net_pt_won_p𝑖= n(net_pt_won) n(net_pt) n(unf_err) Total_unf_err_p𝑖= n(total points) Break_p𝑖= n(server = 𝑗, break_pt_won = 𝑖) n(server = 𝑗, break_pt = 1) 1st_srv_drt_won_p𝑖= n(server | serve_no = 1, rally_count = 1) n(server | serve_no = 1) 2nd_srv_drt_won_p𝑖= n(server | serve_no = 2, rally_count = 1) n(server | serve_no = 2) Srv_avg_speed_p𝑖= mean(speed_mph | server = 𝑖) 1st_rcv_won_p𝑖= n(server = 𝑗, serve_no = 1, point_victor = 𝑖) n(server = 𝑗, serve_no = 1) 2nd_rcv_won_p𝑖= n(server = 𝑗, serve_no = 2, point_victor = 𝑖) n(server = 𝑗, serve_no = 2) n(server = 𝑖, serve_width = 𝐵) Width_B_p𝑖= n(server = 𝑖, serve_width ≠unknown) n(server = 𝑖, serve_width = 𝐶) Width_C_p𝑖= n(server = 𝑖, serve_width ≠unknown) n(server = 𝑖, serve_width = 𝑊) Width_W_p𝑖= n(server = 𝑖, serve_width ≠unknown) n(server = 𝑖, serve_width = 𝐵𝐶) Width_BC_p𝑖= n(server = 𝑖, serve_width ≠unknown) 微信公众号：数学模型 n(server = 𝑖, serve_width = 𝐵𝑊) Width_BW_p𝑖= n(server = 𝑖, serve_width ≠unknown) n(server = 𝑖, serve_depth = 𝐶𝑇𝐿) Depth_CTL_p𝑖= n(server = 𝑖, serve_depth ≠unknown) n(server = 𝑗, return_depth = 𝐷) Return_depth_D_p𝑖= n(server = 𝑗, return_depth ≠unknown) F_won_p𝑖= n(point_victor = 𝑖, winner_shot_type = 𝐹) n(point_victor = 𝑖)

<!-- b000520 | furniture | pages [26] -->
关注数学模型

<!-- b000521 | furniture | pages [26] -->
2

<!-- b000522 | furniture | pages [26] -->
MATHmodels

<!-- b000523 | furniture | pages [26] -->
获取更多资讯

<!-- b000524 | furniture | pages [27] -->
Team # 2406176

<!-- b000525 | furniture | pages [27] -->
Page 27 of 27

<!-- b000527 | caption | pages [27] -->
Table 4: Indicators and their brief introductions

<!-- b000528 | prose | pages [27] -->
微信号：MATHmodels No.

<!-- b000529 | heading | pages [27] -->
Symbol

<!-- b000530 | heading | pages [27] -->
Introduction

<!-- b000531 | prose | pages [27, 28] -->
Proportion of successful serves that are aces for player 𝑖. 1 Aces_p𝑖 Proportion of rallies won by player 𝑖. 2 Winners_p𝑖 Proportion of rallies with 4 or more shots won by player 𝑖. 3 Winners4_p𝑖 Proportion of rallies with 1 to 3 shots won by player 𝑖. 4 Winners13_p𝑖 Proportion of player 𝑖’s serves that are double faults. 5 Double_fault_p𝑖 Proportion of player 𝑖’s first serves that are in. 6 1st_srv_in_p𝑖 Proportion of player 𝑖’s second serves that are in, excluding double faults. 7 2nd_srv_in_p𝑖 Proportion of player 𝑖’s first serves that result in a point won. 8 1st_srv_won_p𝑖 Proportion of player 𝑖’s second serves that result in a point won. 9 2nd_srv_won_p𝑖 Proportion of net points won by player 𝑖. 10 Net_pt_won_p𝑖 Proportion of total points that are unforced errors for player 𝑖. 11 Total_unf_err_p𝑖 Proportion of break points won by player 𝑖. 12 Break_p𝑖 Proportion of player 𝑖’s first serves that directly result in a point won. 13 1st_srv_drt_won_p𝑖 Proportion of player 𝑖’s second serves that directly result in a point won. 14 2nd_srv_drt_won_p𝑖 Average speed of serves for player 𝑖. 15 Srv_avg_speed_p𝑖 Proportion of first serves received by player 𝑖that result in a point won. 16 1st_rcv_won_p𝑖 Proportion of second serves received by player 𝑖that result in a point won. 17 2nd_rcv_won_p𝑖 Proportion of player 𝑖’s serves that land in the "B" width zone. 18 Width_B_p𝑖 Proportion of player 𝑖’s serves that land in the "C" width zone. 19 Width_C_p𝑖 Proportion of player 𝑖’s serves that land in the "W" width zone. 20 Width_W_p𝑖 Proportion of player 𝑖’s serves that land in the "BC" width zone. 21 Width_BC_p𝑖 Proportion of player 𝑖’s serves that land in the "BW" width zone. 22 Width_BW_p𝑖 Proportion of player 𝑖’s serves that land in the "CTL" depth zone. 23 Depth_CTL_p𝑖 Proportion of serves received by player 𝑖that land in the "D" depth zone. 24 Return_depth_D_p𝑖 Proportion of points won by player 𝑖with a forehand shot. 25 F_won_p𝑖 Page 28

<!-- b000532 | furniture | pages [27] -->
关注数学模型

<!-- b000533 | furniture | pages [27] -->
2

<!-- b000534 | furniture | pages [27] -->
MATHmodels

<!-- b000535 | furniture | pages [27] -->
获取更多资讯

<!-- b000536 | furniture | pages [28] -->
Team # 2406176

<!-- b000538 | heading | pages [28] -->
Report on Use of AI

<!-- b000539 | ai_disclosure | pages [28] -->
1. Bing AI

<!-- b000540 | ai_disclosure | pages [28] -->
微信公众号：数学模型

<!-- b000541 | ai_disclosure | pages [28] -->
Query1: write a pseudocode for Bartlett’s Test of Sphericity, please generate in latex code

<!-- b000542 | ai_disclosure | pages [28] -->
format. you should contain all necessary mathmetical equations.

<!-- b000543 | ai_disclosure | pages [28] -->
Output: Here’s a pseudocode for Bartlett’s Test of Sphericity, which is a statistical test for the

<!-- b000544 | ai_disclosure | pages [28] -->
assumption of equal variances in the population. The test statistic is calculated as follows:

<!-- b000545 | heading | pages [28] -->
Algorithm 5 Bartlett’s Test of Sphericity

<!-- b000546 | prose | pages [28] -->
Data: Indicator matrix X Result: Test statistic, p-value, and a decision on whether the data need to be factor analyzed begin 𝜒2 = −log(det(𝑅))(𝑁−1 −2𝑛+5 6 ) where 𝑅is the correlation matrix of the dataset, 𝑁= 109 (number of data points), 𝑛= 25;

<!-- b000547 | prose | pages [28] -->
𝜒2, 𝑝(𝑝+1)   𝑝= 1 −𝐹𝜒2 −1 ; 微信号：MATHmodels 2 if 𝑝< 0.05 then The data is appropriate for factor analysis.;

<!-- b000548 | prose | pages [28] -->
end else The data is not appropriate for factor analysis.;

<!-- b000549 | prose | pages [28] -->
end end

<!-- b000550 | furniture | pages [28] -->
关注数学模型

<!-- b000551 | furniture | pages [28] -->
2

<!-- b000552 | furniture | pages [28] -->
MATHmodels

<!-- b000553 | furniture | pages [28] -->
获取更多资讯
