# P-C-2024-2401919-3f4373c1

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

<!-- b000006 | title | pages [1] -->
2401919

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Harnessing the Power of Momentum:

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | title | pages [1] -->
How to Dominate a Tennis Match?

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
“Tennis more than any other sport, is a game of momentum.” famous American tennis coach Chuck Kriese said. In tennis, momentum is a powerful and crucial aspect of the match. It’s both mysterious and elusive, making it challenging to harness. To enhance our understanding of momentum and offer valuable match preparation advice to players, we conduct in-depth and close studies on momentum from multiple perspectives and levels.

<!-- b000013 | prose | pages [1] -->
Firstly, we establish a Point-tracking Evaluation PCA-TOPSIS Model to evaluate each player’s performance scores (momentum scores) at different moments in a match. In this model, we integrate the

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
strengths of two different models and developed a comprehensive evaluation system for player performance. Based upon the existing data, we established a holistic assessment framework that encompasses 5 major dimensions and 18 specific indicators. We also create a graph to illustrate the performance score changes of the two players in 2023 Wimbledon Gentlemen’s Singles Final. Our results was subjected to KMO and Bartlett’s sphericity tests for validation.

<!-- b000016 | prose | pages [1] -->
Secondly, we conducted a white noise test to verify if the coach’s postulation of random match swings is correct. In the Autocorrelation Function and Partial Autocorrelation Function tests, the graphs exhibited first-order truncation and fourth-order tailing respectively. In the Ljung-Box Test and Box-Pierce Test, the p-values were significantly smaller than 0.05, leading to the rejection of the null hypothesis. All these findings indicate that the score fluctuations and match swings are not random, contradicting the coach’s belief.

<!-- b000017 | prose | pages [1] -->
Thirdly, building upon the established momentum scoring system, we introduced the GM(1,1) Grey Prediction Model to forecast the shifts in the match process. A turning point is defined as a significant fluctuation in the score difference of the two players at adjacent moments that exceeds a predefined threshold. Using the grey prediction model, we predicted the turning points in the Final and compared them with the actual data through a line graph. We were pleasantly surprised to find that the predicted turning points largely overlap with the actual data, indicating excellent predictive performance. The average relative error is 0.0378, the absolute correlation is 0.9895, and the mean square deviation ratio is 0.1284. Furthermore, we also examined the relationship between various indicators and the turning points in the game. The major dimension with strongest correlation was offensive efficiency, while the specific indicator with strongest correlation was the cumulative number of games won. Based on these findings, we provided recommendations to the players, emphasizing the importance of proactive attacking strategies and focusing on long-term development.

<!-- b000018 | prose | pages [1] -->
Lastly, we expanded our model and applied it to other types of matches. We obtained the data from the

<!-- b000019 | heading | pages [1] -->
2023 Wimbledon Ladies’ Singles Final and used our model to predict the turning points. The results showed

<!-- b000020 | prose | pages [1] -->
that the predictive performance was also remarkable, although slightly inferior to the results in the men’s matches. Thus, we concluded that the model has good generalizability, but adjustments to the indicators and relevant parameters may be necessary when applying it to different types of matches.

<!-- b000021 | prose | pages [1] -->
In addition, we perform a sensitivity analysis to evaluate the responsiveness of our model to variations in input parameters. The results demonstrate strong accuracy and robustness in handling different scenarios.

<!-- b000022 | keywords | pages [1] -->
Keywords: Momentum, PCA-TOPSIS Model, White Noise Test, Grey Prediction Model, ACF&PACF

<!-- b000023 | furniture | pages [1] -->
关注数学模型

<!-- b000024 | furniture | pages [1] -->
2

<!-- b000025 | furniture | pages [1] -->
MATHmodels

<!-- b000026 | furniture | pages [1] -->
获取更多资讯

<!-- b000027 | furniture | pages [2] -->
Team # 2401919

<!-- b000028 | furniture | pages [2] -->
Page 2 of 25

<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | contents | pages [2] -->
1

<!-- b000031 | heading | pages [2] -->
Introduction

<!-- b000032 | prose | pages [2] -->
3

<!-- b000033 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000034 | prose | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000035 | prose | pages [2] -->
2

<!-- b000036 | heading | pages [2] -->
Preparation of the Models

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000039 | heading | pages [2] -->
Assumptions

<!-- b000040 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000041 | heading | pages [2] -->
Notations

<!-- b000042 | prose | pages [2] -->
5 Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 6 Missing and Abnormal Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.1 6 Different Types of Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.2 6

<!-- b000043 | heading | pages [2] -->
TASK1&2: Point-tracking Evaluation PCA-TOPSIS Model

<!-- b000044 | prose | pages [2] -->
3 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 The Structure of PCA-TOPSIS Model 6 Select and Process Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 7 Select Appropriate Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 7 Data Dimensionless Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2 8

<!-- b000045 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000046 | prose | pages [2] -->
Determine Components and Weights . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 Obtain the Scores and Visualization

<!-- b000047 | prose | pages [2] -->
4

<!-- b000048 | heading | pages [2] -->
Task3: The White Noise Tests for Our Model

<!-- b000049 | prose | pages [2] -->
11

<!-- b000050 | prose | pages [2] -->
12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 White Noise Sequence 12 Autocorrelation Graph and Partial Autocorrelation Graph Test 4.2 . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | prose | pages [2] -->
12 Ljung-Box Test and Box-Pierce Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 13 Complete Results and Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 14

<!-- b000052 | heading | pages [2] -->
Task4: Momentum Swings GM(1,1) Grey Prediction Model

<!-- b000053 | prose | pages [2] -->
5 15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Data Processing and Examination 15 Construction of New Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 15 Level Comparison Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.2 5.2 Utilize the Model to Obtain the Predicted Values 15 . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | prose | pages [2] -->
15 Build Momentum Swings Grey Forecasting Model 5.2.1 . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | prose | pages [2] -->
15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 Model Diagnosis 16

<!-- b000056 | prose | pages [2] -->
Task5: Quantify the Impact of Different Factors on the Swings 6 17 Gray Relational Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 17 Advice to a Player Going into a New Match . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000057 | prose | pages [2] -->
7

<!-- b000058 | heading | pages [2] -->
Task6: Test the Accuracy of the Prediction Model

<!-- b000059 | prose | pages [2] -->
18

<!-- b000060 | prose | pages [2] -->
18

<!-- b000061 | heading | pages [2] -->
Task7: Generalize the Model Applicable to Other Matches

<!-- b000062 | prose | pages [2] -->
8

<!-- b000063 | prose | pages [2] -->
9

<!-- b000064 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000065 | heading | pages [2] -->
10 Model Assessment

<!-- b000066 | prose | pages [2] -->
19

<!-- b000067 | prose | pages [2] -->
21

<!-- b000068 | prose | pages [2] -->
21 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.1 Strengths 21 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2

<!-- b000069 | heading | pages [2] -->
11 Letter

<!-- b000070 | heading | pages [2] -->
Appendices

<!-- b000071 | heading | pages [2] -->
Appendix A

<!-- b000072 | prose | pages [2] -->
Evaluation Criteria

<!-- b000073 | heading | pages [2] -->
Appendix B

<!-- b000074 | prose | pages [2] -->
Code

<!-- b000075 | prose | pages [2] -->
21

<!-- b000076 | prose | pages [2] -->
22

<!-- b000077 | prose | pages [2] -->
23

<!-- b000078 | prose | pages [2] -->
23

<!-- b000079 | prose | pages [2] -->
24

<!-- b000080 | furniture | pages [2] -->
关注数学模型

<!-- b000081 | furniture | pages [2] -->
2

<!-- b000082 | furniture | pages [2] -->
MATHmodels

<!-- b000083 | furniture | pages [2] -->
获取更多资讯

<!-- b000084 | furniture | pages [3] -->
Team # 2401919

<!-- b000085 | prose | pages [3] -->
1

<!-- b000086 | heading | pages [3] -->
Introduction

<!-- b000087 | prose | pages [3] -->
1.1 Problem Background

<!-- b000088 | furniture | pages [3] -->
Page 3 of 25

<!-- b000089 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000090 | prose | pages [3] -->
Tennis is a highly competitive and technically demanding sport that enjoys widespread popularity. In men’s singles tennis matches, the outcome is determined by a best-of-five sets format (the first player to win three sets is the winner). Each set is made up of multiple games, with the objective being to win six games and lead the opponent by at least two games. If the score reaches 6-6, a tiebreaker is played to determine the winner of that set. In a tiebreaker, the first player to reach seven points with a minimum lead of two points secures the set victory. However, in the fifth set, the tiebreaker changes to a first-to-ten-points format. Within each game, players strive to win at least four points, but they must secure victory with a two-point advantage.

<!-- b000091 | prose | pages [3] -->
In tennis matches, the situation often changes in the blink of an eye. This exhilarating sport is a blend of tactics and skills, where every serve, return, or shot can alter the course of the game. Sometimes we witness one player’s unstoppable momentum, swiftly securing victory. Other times,

<!-- b000092 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000093 | prose | pages [3] -->
we see intense battles where both sides fiercely compete, experiencing numerous lead changes and comebacks before determining a winner, like the duel between Carlos Alcaraz and Novak Djokovic in the 2023 Wimbledon final.

<!-- b000094 | prose | pages [3] -->
Carlos Alcaraz

<!-- b000095 | prose | pages [3] -->
Jannik Sinner

<!-- b000096 | heading | pages [3] -->
2023 Wimbledon Gentlemen’s Singles

<!-- b000097 | prose | pages [3] -->
3:1

<!-- b000098 | prose | pages [3] -->
Carlos Alcaraz

<!-- b000099 | prose | pages [3] -->
Nicolas Jarry

<!-- b000100 | prose | pages [3] -->
Carlos Alcaraz

<!-- b000101 | prose | pages [3] -->
3:1

<!-- b000102 | prose | pages [3] -->
Alexander Zverev

<!-- b000103 | prose | pages [3] -->
Matteo Berrettini

<!-- b000104 | prose | pages [3] -->
0:3

<!-- b000105 | prose | pages [3] -->
Matteo Berrettini

<!-- b000106 | prose | pages [3] -->
Carlos Alcaraz

<!-- b000107 | prose | pages [3] -->
3:0

<!-- b000108 | prose | pages [3] -->
Frances Tiafoe

<!-- b000109 | prose | pages [3] -->
Grigor Dimitrov

<!-- b000110 | prose | pages [3] -->
0:3

<!-- b000111 | prose | pages [3] -->
Grigor Dimitrov

<!-- b000112 | prose | pages [3] -->
Holger Rune

<!-- b000113 | prose | pages [3] -->
1:3

<!-- b000114 | prose | pages [3] -->
3

<!-- b000115 | prose | pages [3] -->
Alejandro Davidovich

<!-- b000116 | prose | pages [3] -->
Holger Rune

<!-- b000117 | prose | pages [3] -->
2:3

<!-- b000118 | prose | pages [3] -->
Carlos Alcaraz

<!-- b000119 | prose | pages [3] -->
:

<!-- b000120 | prose | pages [3] -->
Holger Rune

<!-- b000121 | prose | pages [3] -->
Daniil Medvedev

<!-- b000122 | prose | pages [3] -->
0

<!-- b000123 | prose | pages [3] -->
Daniil Medvedev

<!-- b000124 | prose | pages [3] -->
3:1

<!-- b000125 | prose | pages [3] -->
3:1

<!-- b000126 | prose | pages [3] -->
Jannik Sinner

<!-- b000127 | prose | pages [3] -->
Quentin Halys

<!-- b000128 | prose | pages [3] -->
Jannik Sinner

<!-- b000129 | prose | pages [3] -->
3:0

<!-- b000130 | prose | pages [3] -->
Daniel Elahi

<!-- b000131 | prose | pages [3] -->
Daniel Elahi

<!-- b000132 | prose | pages [3] -->
3:2

<!-- b000133 | prose | pages [3] -->
Mikael Ymer

<!-- b000134 | prose | pages [3] -->
Jannik Sinner

<!-- b000135 | prose | pages [3] -->
3:1

<!-- b000136 | prose | pages [3] -->
Guido Pella

<!-- b000137 | prose | pages [3] -->
Roman Safiullin

<!-- b000138 | prose | pages [3] -->
0:3

<!-- b000139 | prose | pages [3] -->
Roman Safiullin

<!-- b000140 | prose | pages [3] -->
Roman Safiullin

<!-- b000141 | prose | pages [3] -->
3:1

<!-- b000142 | prose | pages [3] -->
0

<!-- b000143 | prose | pages [3] -->
Denis Shapovalov

<!-- b000144 | prose | pages [3] -->
Denis Shapovalov

<!-- b000145 | prose | pages [3] -->
3:1

<!-- b000146 | prose | pages [3] -->
:

<!-- b000147 | prose | pages [3] -->
Novak Djokovic

<!-- b000148 | prose | pages [3] -->
Liam Broady

<!-- b000149 | prose | pages [3] -->
3

<!-- b000150 | prose | pages [3] -->
Andrey Rublev

<!-- b000151 | prose | pages [3] -->
Andrey Rublev

<!-- b000152 | prose | pages [3] -->
3:1

<!-- b000153 | prose | pages [3] -->
3:2

<!-- b000154 | prose | pages [3] -->
Marton Fucsovics

<!-- b000155 | prose | pages [3] -->
Daniil Medvedev

<!-- b000156 | prose | pages [3] -->
2:0

<!-- b000157 | prose | pages [3] -->
Jiri Lehecka

<!-- b000158 | prose | pages [3] -->
Jiri Lehecka

<!-- b000159 | prose | pages [3] -->
3:2

<!-- b000160 | prose | pages [3] -->
Tommy Paul

<!-- b000161 | prose | pages [3] -->
Daniil Medvedev

<!-- b000162 | prose | pages [3] -->
3:2

<!-- b000163 | prose | pages [3] -->
Christopher Eubanks

<!-- b000164 | prose | pages [3] -->
Christopher

<!-- b000165 | prose | pages [3] -->
3:0

<!-- b000166 | prose | pages [3] -->
Eubanks

<!-- b000167 | prose | pages [3] -->
Christopher

<!-- b000168 | prose | pages [3] -->
Christopher

<!-- b000169 | prose | pages [3] -->
O'Connell

<!-- b000170 | prose | pages [3] -->
3:2

<!-- b000171 | prose | pages [3] -->
Eubanks

<!-- b000172 | prose | pages [3] -->
Laslo Djere

<!-- b000173 | prose | pages [3] -->
Stefanos Tsitsipas

<!-- b000174 | prose | pages [3] -->
0:3

<!-- b000175 | prose | pages [3] -->
Stefanos Tsitsipas

<!-- b000176 | prose | pages [3] -->
David Goffin

<!-- b000177 | prose | pages [3] -->
Andrey Rublev

<!-- b000178 | prose | pages [3] -->
3:2

<!-- b000179 | prose | pages [3] -->
Alexander Bublik

<!-- b000180 | prose | pages [3] -->
Alexander Bublik

<!-- b000181 | prose | pages [3] -->
3:0

<!-- b000182 | prose | pages [3] -->
Novak Djokovic

<!-- b000183 | prose | pages [3] -->
Maximilian Marterer

<!-- b000184 | prose | pages [3] -->
1:3

<!-- b000185 | prose | pages [3] -->
Lorenzo Musetti

<!-- b000186 | prose | pages [3] -->
Hubert Hurkacz

<!-- b000187 | prose | pages [3] -->
0:3

<!-- b000188 | prose | pages [3] -->
Hubert Hurkacz

<!-- b000189 | prose | pages [3] -->
Novak Djokovic

<!-- b000190 | prose | pages [3] -->
1:3

<!-- b000191 | prose | pages [3] -->
Stan Wawrinka

<!-- b000192 | prose | pages [3] -->
Novak Djokovic

<!-- b000193 | prose | pages [3] -->
0:3

<!-- b000194 | prose | pages [3] -->
Novak Djokovic

<!-- b000195 | caption | pages [3] -->
Figure 1: 2023 Wimbledon Gentlemen’s Singles

<!-- b000196 | prose | pages [3] -->
The dynamics and trajectory of a match, including astonishing turnarounds, can be attributed to the players’ “momentum”. Momentum has always been emphasized, but quantifying and proving its true impact on the game, as well as identifying the factors that generate and shift momentum, is challenging. To better assist players in achieving success, we will delve into these aspects, providing coaches with advice on helping players prepare for and respond to game-altering events, fully harnessing the power of momentum. Specifically, we will utilize the provided data to carry out the following tasks:

<!-- b000197 | prose | pages [3] -->
1. Present the changing trends of match results over time.

<!-- b000198 | prose | pages [3] -->
2. Evaluate the performance of players at a specific moment.

<!-- b000199 | furniture | pages [3] -->
关注数学模型

<!-- b000200 | furniture | pages [3] -->
2

<!-- b000201 | furniture | pages [3] -->
MATHmodels

<!-- b000202 | furniture | pages [3] -->
获取更多资讯

<!-- b000203 | furniture | pages [4] -->
Team # 2401919

<!-- b000204 | furniture | pages [4] -->
Page 4 of 25

<!-- b000205 | prose | pages [4] -->
3. Verify if swings in momentum in a match are random.

<!-- b000206 | prose | pages [4] -->
4. Establish a prediction model to forecast shifts in the game situation.

<!-- b000207 | prose | pages [4] -->
5. Evaluate factors influencing the swings and provide players with recommendations.

<!-- b000208 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000209 | prose | pages [4] -->
6. Validate the accuracy of the prediction model in actual matches and optimize them.

<!-- b000210 | prose | pages [4] -->
7. Expand the model to other types of matches.

<!-- b000211 | prose | pages [4] -->
1.2 Our Work

<!-- b000212 | prose | pages [4] -->
To explore the role and influence of “momentum” in tennis matches, we selected different indicators from game data for quantification and analysis. In the first question, we constructed a PCA-TOPSIS model and selected 18 indicators to evaluate player performance and determine their weights. In the second question, we conducted a white noise test on the model results, proving that changes in game momentum are not random and refuting the coach’s viewpoint. In the third question, we further constructed a GM(1, 1) gray prediction model to forecast turning points in the

<!-- b000213 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000214 | prose | pages [4] -->
game and determined the factor with the highest correlation coefficient with momentum shifts. In the fourth question, we compared the model with real game data to test its accuracy and extended its application to other matches, making it more widely applicable. Lastly, we test the PCA-TOPSIS model’s sensitivity.The overview of our work is shown in Figure 2.

<!-- b000215 | prose | pages [4] -->
White Noise Tests Nonrandomness

<!-- b000216 | prose | pages [4] -->
Players’

<!-- b000217 | prose | pages [4] -->
PCA-TOPSIS

<!-- b000218 | prose | pages [4] -->
Data Reprocessing

<!-- b000219 | prose | pages [4] -->
Scores

<!-- b000220 | heading | pages [4] -->
Model

<!-- b000221 | prose | pages [4] -->
Given Data

<!-- b000222 | prose | pages [4] -->
Swing

<!-- b000223 | prose | pages [4] -->
GM(1,1) Grey

<!-- b000224 | prose | pages [4] -->
Point

<!-- b000225 | heading | pages [4] -->
Prediction Model

<!-- b000226 | prose | pages [4] -->
Most Related

<!-- b000227 | prose | pages [4] -->
Test the Expand to

<!-- b000228 | prose | pages [4] -->
Factor

<!-- b000229 | prose | pages [4] -->
Accuracy Other Matches

<!-- b000230 | caption | pages [4] -->
Figure 2: Overview of Our Work

<!-- b000231 | prose | pages [4] -->
2

<!-- b000232 | heading | pages [4] -->
Preparation of the Models

<!-- b000233 | prose | pages [4] -->
2.1

<!-- b000234 | heading | pages [4] -->
Assumptions

<!-- b000235 | prose | pages [4] -->
The following reasonable assumptions can be made in this paper:

<!-- b000236 | prose | pages [4] -->
• The players are in a normal physiological, physical and mental state, without any severe

<!-- b000237 | furniture | pages [4] -->
关注数学模型

<!-- b000238 | furniture | pages [4] -->
2

<!-- b000239 | furniture | pages [4] -->
MATHmodels

<!-- b000240 | furniture | pages [4] -->
获取更多资讯

<!-- b000241 | furniture | pages [5] -->
Team # 2401919

<!-- b000242 | prose | pages [5] -->
injuries or using banned substances.

<!-- b000243 | furniture | pages [5] -->
Page 5 of 25

<!-- b000244 | prose | pages [5] -->
• The players did not engage in any match-fixing or similar activities during the competition.

<!-- b000245 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000246 | prose | pages [5] -->
• The recording of the values for each player at every moment is accurate, fair, and in accordance with the rules of the competition.

<!-- b000247 | prose | pages [5] -->
• The performance of the players on the field is rarely affected by the conditions of the venue, weather, or the atmosphere of the audience.

<!-- b000248 | prose | pages [5] -->
• The performance of each player in this game is rarely affected by the results of previous matches, instead concentrating on the current match.

<!-- b000249 | prose | pages [5] -->
2.2

<!-- b000250 | heading | pages [5] -->
Notations

<!-- b000251 | prose | pages [5] -->
In our paper, we have adopted the nomenclature presented in Table 1 for model construction. Any additional symbol which is not frequently used will be introduced once they are utilized in the

<!-- b000252 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000253 | prose | pages [5] -->
following text. All variables are targeted at a certain set, and the training data for the model also includes data of an entire set. In particular, "so far" and "accumulative" means cumulative value since the very beginning of current set. Definitions without these words means value at current moment.

<!-- b000254 | caption | pages [5] -->
Table 1: Symbols and Definitions

<!-- b000255 | prose | pages [5] -->
Symbol Definition

<!-- b000256 | prose | pages [5] -->
Number of sets won by player 𝑖 𝑆𝑖 Number of games won by player 𝑖 𝐺𝑖 Number of points won by player 𝑖 𝑃𝑖 Number of untouchable winning serves hit by player 𝑖so far 𝐴𝑖 Player 𝑖’s break point conversion rate so far 𝐵𝑖 Player 𝑖’s net point winning rate so far 𝑁𝑖 Player 𝑖’s first serve success rate so far 𝐹𝑆𝑢𝑖 Player 𝑖’s first serve score rate so far 𝐹𝑆𝑐𝑖 Player 𝑖’s second serve score rate so far 𝑆𝑆𝑐𝑖 Player 𝑖’s return score rate so far 𝑅𝑆𝑐𝑖 Number of double faults made by player 𝑖so far 𝐷𝐹𝑖 Number of unforced errors made by player 𝑖so far 𝑈𝐸𝑖 Player 𝑖’s distance ran during point 𝐷𝑖 Player 𝑖’s speed of serve 𝑉𝑖 Player 𝑖’s direction of serve 𝑆𝑊𝑖 Player 𝑖’s depth of serve 𝑆𝐷𝑖 Player 𝑖’s depth of return 𝑅𝐷𝑖 Player 𝑖’s accumulative serve count 𝑆𝐶𝑖 △𝑀 Momentum score difference between two players. 𝑖= 1, 2

<!-- b000257 | furniture | pages [5] -->
关注数学模型

<!-- b000258 | furniture | pages [5] -->
2

<!-- b000259 | furniture | pages [5] -->
MATHmodels

<!-- b000260 | furniture | pages [5] -->
获取更多资讯

<!-- b000261 | furniture | pages [6] -->
Team # 2401919

<!-- b000262 | prose | pages [6] -->
2.3 Data Cleaning

<!-- b000263 | prose | pages [6] -->
2.3.1 Missing and Abnormal Data

<!-- b000264 | furniture | pages [6] -->
Page 6 of 25

<!-- b000265 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000266 | prose | pages [6] -->
We have observed some missing data in speed_mph, serve_width, serve_depth, and return_depth variables, which is presented as "NA". Considering the continuous nature of the game process, we will not remove entire rows of data. Instead, the missing values in speed_mph will be replaced with the average value. As for serve_width, serve_depth, and return_depth variables, the missing values will be assigned as 0.

<!-- b000267 | prose | pages [6] -->
2.3.2 Different Types of Data

<!-- b000268 | prose | pages [6] -->
(1) Data Accumulation in Numerical data For some numerical data in categorical form, they have only two values: 0 and 1. During calculations, an excess of 0s can result in "nan" errors, preventing further computation. To address this, the values will be accumulated. To eliminate the impact of accumulation, they will subsequently be decremented.

<!-- b000269 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000270 | prose | pages [6] -->
(2) Data Mapping in Non-numeric Data For the non-numerical variables serve_width, serve_depth, and return_depth, we will map them to numbers after rigorous judgements.

<!-- b000271 | prose | pages [6] -->
• serve_width: C=1, BC=2, B=3, BW=4, W=5

<!-- b000272 | prose | pages [6] -->
• serve_depth: NCTL=1, CTL=2

<!-- b000273 | prose | pages [6] -->
• return_depth: ND=1, D=2

<!-- b000274 | heading | pages [6] -->
TASK1&2: Point-tracking Evaluation PCA-TOPSIS Model

<!-- b000275 | prose | pages [6] -->
3

<!-- b000276 | heading | pages [6] -->
The Structure of PCA-TOPSIS Model

<!-- b000277 | prose | pages [6] -->
3.1

<!-- b000278 | prose | pages [6] -->
In this section, we need to select specific indicators to track the progress of each match point and the performance of players. The traditional TOPSIS analysis method relies heavily on subjective weighting of indicators, which can significantly influence the results. Therefore, we introduce the relatively objective method, Principal Component Analysis (PCA), to analyze the dataset and reduce dimensionality. Subsequently, we determine the weights for each indicator and rank the proximity of the evaluated objects’ numerical distance to the ideal target. This novel PCA-TOPSIS model combines the advantages of both models and enables more accurate tracking of the players’ performance at each match point.The structure of our idea can be illustrated by Figure 3.

<!-- b000279 | prose | pages [6] -->
What’s more, each player has significant variations in their playing style, personal level, and other individual factors. Additionally, each game is influenced by multiple complex factors and is subject to frequent changes. Therefore, instead of analyzing the performance of all players in all games using the same model, we choose to build separate models for the performance of each player in each game. This approach provides greater accuracy and relevance.

<!-- b000280 | furniture | pages [6] -->
关注数学模型

<!-- b000281 | furniture | pages [6] -->
2

<!-- b000282 | furniture | pages [6] -->
MATHmodels

<!-- b000283 | furniture | pages [6] -->
获取更多资讯

<!-- b000284 | furniture | pages [7] -->
Team # 2401919

<!-- b000285 | furniture | pages [7] -->
Page 7 of 25

<!-- b000286 | prose | pages [7] -->
Collect the raw data for selected indicators

<!-- b000287 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000288 | heading | pages [7] -->
Data processing: dimensionless processing

<!-- b000289 | prose | pages [7] -->
Compute the correlation matrix, eigenvalues, and

<!-- b000290 | prose | pages [7] -->
variance contribution rate.

<!-- b000291 | prose | pages [7] -->
Determine the principal components and weights

<!-- b000292 | prose | pages [7] -->
Obtain the comprehensive evaluation results.

<!-- b000293 | caption | pages [7] -->
Figure 3: Schematic of PCA-TOPSIS Model

<!-- b000294 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000295 | prose | pages [7] -->
3.2 Select and Process Indicators

<!-- b000296 | prose | pages [7] -->
3.2.1 Select Appropriate Indicators

<!-- b000297 | prose | pages [7] -->
To evaluate the performance of athletes on the field, we have developed a performance assessment system consisting of five aspects: current situation, offensive effectiveness, error situation, technical fitness, and starting advantage. Each first-level indicator is divided into many second-level indicators. As shown in Figure 4 below.

<!-- b000298 | prose | pages [7] -->
NP rate

<!-- b000299 | prose | pages [7] -->
RP rate

<!-- b000300 | prose | pages [7] -->
RP rate

<!-- b000301 | prose | pages [7] -->
Offensive Effectiveness

<!-- b000302 | prose | pages [7] -->
FSU rate

<!-- b000303 | prose | pages [7] -->
Return depth

<!-- b000304 | prose | pages [7] -->
Technical

<!-- b000305 | prose | pages [7] -->
Running distance Fitness

<!-- b000306 | prose | pages [7] -->
Starting

<!-- b000307 | prose | pages [7] -->
Serve direction

<!-- b000308 | prose | pages [7] -->
Advantage

<!-- b000309 | prose | pages [7] -->
Sets won

<!-- b000310 | prose | pages [7] -->
Current

<!-- b000311 | prose | pages [7] -->
Sets won

<!-- b000312 | prose | pages [7] -->
Situation

<!-- b000313 | prose | pages [7] -->
Error Situation

<!-- b000314 | prose | pages [7] -->
Accumulative

<!-- b000315 | prose | pages [7] -->
Points won

<!-- b000316 | prose | pages [7] -->
Double fault

<!-- b000317 | prose | pages [7] -->
serves

<!-- b000318 | prose | pages [7] -->
Unforced number error number

<!-- b000319 | caption | pages [7] -->
Figure 4: Performance Assessment System

<!-- b000320 | prose | pages [7] -->
(1) Current Situation The current situation refers to the on-court position of the athlete up until the present moment, reflecting their scoring breakthrough ability within a certain timeframe. In this regard, we have selected cumulative sets won, cumulative games won, and cumulative points won as

<!-- b000321 | furniture | pages [7] -->
关注数学模型

<!-- b000322 | furniture | pages [7] -->
2

<!-- b000323 | furniture | pages [7] -->
MATHmodels

<!-- b000324 | furniture | pages [7] -->
获取更多资讯

<!-- b000325 | furniture | pages [8] -->
Team # 2401919

<!-- b000326 | furniture | pages [8] -->
Page 8 of 25

<!-- b000327 | prose | pages [8] -->
secondary indicators, which respectively reflect the athlete’s scoring ability, game breakthrough capability, and set breakthrough capability within a certain timeframe.

<!-- b000328 | prose | pages [8] -->
(2) Offensive Effectiveness Offensive efficiency refers to the practical effectiveness of the

<!-- b000329 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000330 | prose | pages [8] -->
athlete’s various technical actions on the court in scoring, reflecting their efficiency and capability in offensive breakthroughs. In this aspect, we have selected ACE count, BP rate (break point conversion rate) , NP rate (net points won rate), FSU rate (first serve success rate) , FSC rate (first serve points won rate) , SSC rate (second serve points won rate), and RP rate (return points won rate) as secondary indicators, all of which are accumulated data within a certain timeframe.

<!-- b000331 | prose | pages [8] -->
(3) Error Situation Error situations refer to the occurrence of various mistakes by the athlete on the court, reflecting the stability of their performance in critical moments. In this aspect, we have selected double faults count and unforced error count as secondary indicators, both of which are accumulated data within a certain timeframe.

<!-- b000332 | prose | pages [8] -->
Among these, double faults count reflects the athlete’s serving stability and their ability to capitalize on the advantage of serving first; unforced error count reflects their technical stability.

<!-- b000333 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000334 | prose | pages [8] -->
(4) Technical Fitness Technical and physical abilities refer to the athlete’s physical condition and technical choices displayed on the court, reflecting their level of physical fitness and tactical strategy selection. In this aspect, we have selected running distance, serving speed, serving depth, serving direction, and return depth as secondary indicators, all of which are data at the current moment.

<!-- b000335 | prose | pages [8] -->
Among these, running distance reflects the athlete’s physical condition, mobility, and intensity, while also reflecting their running level and tactical choices; serving speed, serving depth, and serving direction reflect their serving technique level and tactical choices; return depth reflects their return technique and tactical choices.

<!-- b000336 | prose | pages [8] -->
(5) Starting Advantage Serving advantage refers to the relative advantage the athlete possesses as the server, which influences their on-court performance in terms of psychology, match state, and offensive opportunities, among other aspects. In this aspect, we have selected the number of serves as a secondary indicator.

<!-- b000337 | prose | pages [8] -->
The number of serves represents the accumulated number of serves by the athlete within a certain timeframe. This indicator is used to offset the advantage the athlete has as the server in terms of scoring and offense, in order to obtain a more accurate on-court performance evaluation.

<!-- b000338 | prose | pages [8] -->
3.2.2 Data Dimensionless Process

<!-- b000339 | prose | pages [8] -->
Dimensionalization refers to the process of removing the dimensionality of different indicators, which makes them incomparable due to the different units of measurement. Therefore, it is necessary to normalize the data first in order to eliminate the dimensional influence. This is done by transforming the original variables to eliminate the influence of their units of measurement, enabling subsequent analysis. In this case, we choose the standardization method to normalize the data, which transforms the values of all indicators to have a mean of 0 and a variance of 1. The formula below takes 𝑆𝑖as an example while 𝑡means sample point in this time series.

<!-- b000340 | prose | pages [8] -->
𝑖= 𝑆𝑖,𝑡−𝜇(𝑆𝑖)

<!-- b000341 | prose | pages [8] -->
𝑆∗

<!-- b000342 | prose | pages [8] -->
𝜎(𝑆𝑖) 𝑖= 1, 2 (1)

<!-- b000343 | furniture | pages [8] -->
关注数学模型

<!-- b000344 | furniture | pages [8] -->
2

<!-- b000345 | furniture | pages [8] -->
MATHmodels

<!-- b000346 | furniture | pages [8] -->
获取更多资讯

<!-- b000347 | furniture | pages [9] -->
Team # 2401919

<!-- b000348 | furniture | pages [9] -->
Page 9 of 25

<!-- b000349 | prose | pages [9] -->
Determine Components and Weights 3.3

<!-- b000350 | prose | pages [9] -->
After obtaining standardized data for each indicator, we calculate the covariance and correlation matrix among the variables. Taking 𝑆𝑖and 𝐺𝑗for example, the calculation formula is shown below.

<!-- b000351 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000352 | prose | pages [9] -->
𝑖, 𝐺∗

<!-- b000353 | prose | pages [9] -->
𝐶𝑜𝑣(𝑆∗

<!-- b000354 | prose | pages [9] -->
𝑅𝑆∗

<!-- b000355 | prose | pages [9] -->
𝑗=

<!-- b000356 | prose | pages [9] -->
𝑖,𝐺∗

<!-- b000357 | prose | pages [9] -->
√︃ 𝑗)

<!-- b000358 | prose | pages [9] -->
𝑖, 𝑗∈{1, 2} (2)

<!-- b000359 | prose | pages [9] -->
𝑖) · 𝑉𝑎𝑟(𝐺∗

<!-- b000360 | prose | pages [9] -->
𝑉𝑎𝑟(𝑆∗

<!-- b000361 | prose | pages [9] -->
𝑗)

<!-- b000362 | prose | pages [9] -->
The heat map of the correlation coefficient matrix containing all variables is shown in Figure 5. We could clearly see that there is a strong positive correlation between 𝑉1 and 𝐹𝑆𝑢1, the same as the

<!-- b000363 | prose | pages [9] -->
common sense, the faster your serve speed, the more likely you will get your first serve success. We could also see that there is a strong negative correlation between 𝐷𝐹1,𝑈𝐸1 and 𝑆1, 𝐺1, 𝑃1, which is also intuitive. The more double faults and unforced errors you commit, the less likely you will win, to name but a few.

<!-- b000364 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000365 | prose | pages [9] -->
Correlation Coefficient Matrix Heat Map

<!-- b000366 | prose | pages [9] -->
SC2 RD2 SD2

<!-- b000367 | prose | pages [9] -->
SW2 V2 D2

<!-- b000368 | prose | pages [9] -->
UE2 DF2

<!-- b000369 | prose | pages [9] -->
RSc2 SSc2 FSc2 FSu2 N2 B2 A2 P2

<!-- b000370 | prose | pages [9] -->
G2 S2

<!-- b000371 | prose | pages [9] -->
SC1 RD1 SD1

<!-- b000372 | prose | pages [9] -->
SW1 V1 D1

<!-- b000373 | prose | pages [9] -->
UE1 DF1

<!-- b000374 | prose | pages [9] -->
RSc1 SSc1 FSc1 FSu1 N1 B1 A1 P1

<!-- b000375 | prose | pages [9] -->
G1 S1

<!-- b000376 | prose | pages [9] -->
RD1

<!-- b000377 | prose | pages [9] -->
DF1

<!-- b000378 | prose | pages [9] -->
N1

<!-- b000379 | prose | pages [9] -->
D1

<!-- b000380 | prose | pages [9] -->
UE1

<!-- b000381 | prose | pages [9] -->
SD1

<!-- b000382 | prose | pages [9] -->
SC1

<!-- b000383 | prose | pages [9] -->
RSc1

<!-- b000384 | prose | pages [9] -->
G1

<!-- b000385 | prose | pages [9] -->
FSc1

<!-- b000386 | prose | pages [9] -->
S1

<!-- b000387 | prose | pages [9] -->
P1

<!-- b000388 | prose | pages [9] -->
A1

<!-- b000389 | prose | pages [9] -->
B1

<!-- b000390 | prose | pages [9] -->
V1

<!-- b000391 | prose | pages [9] -->
SW1

<!-- b000392 | prose | pages [9] -->
FSu1

<!-- b000393 | prose | pages [9] -->
SSc1

<!-- b000394 | prose | pages [9] -->
Legend

<!-- b000395 | prose | pages [9] -->
0.8 0.4 0.0 0.4 0.8

<!-- b000396 | prose | pages [9] -->
RD2

<!-- b000397 | prose | pages [9] -->
DF2

<!-- b000398 | prose | pages [9] -->
N2

<!-- b000399 | prose | pages [9] -->
D2

<!-- b000400 | prose | pages [9] -->
UE2

<!-- b000401 | prose | pages [9] -->
SD2

<!-- b000402 | prose | pages [9] -->
SC2

<!-- b000403 | prose | pages [9] -->
RSc2

<!-- b000404 | prose | pages [9] -->
G2 G2

<!-- b000405 | prose | pages [9] -->
FSc2

<!-- b000406 | prose | pages [9] -->
S2 S2

<!-- b000407 | prose | pages [9] -->
P2

<!-- b000408 | prose | pages [9] -->
A2

<!-- b000409 | prose | pages [9] -->
B2

<!-- b000410 | prose | pages [9] -->
V2

<!-- b000411 | prose | pages [9] -->
SW2

<!-- b000412 | prose | pages [9] -->
FSu2

<!-- b000413 | prose | pages [9] -->
SSc2

<!-- b000414 | caption | pages [9] -->
Figure 5: Heat Map of Correlation

<!-- b000415 | prose | pages [9] -->
According to the characteristic equation |𝑅−𝜆𝐼| = 0, the eigenvalues 𝜆𝑘(𝑘= 1, 2, 3...18) are computed. The eigenvalue contribution rate and cumulative contribution rate are represented by formulas (3) and (4) respectively.

<!-- b000416 | prose | pages [9] -->
𝑇𝑘= 𝜆𝑘

<!-- b000417 | prose | pages [9] -->
(3)

<!-- b000418 | prose | pages [9] -->
Í𝑝

<!-- b000419 | prose | pages [9] -->
𝑗=1 𝜆𝑗

<!-- b000420 | furniture | pages [9] -->
关注数学模型

<!-- b000421 | furniture | pages [9] -->
2

<!-- b000422 | furniture | pages [9] -->
MATHmodels

<!-- b000423 | furniture | pages [9] -->
获取更多资讯

<!-- b000424 | furniture | pages [10] -->
Team # 2401919

<!-- b000425 | prose | pages [10] -->
𝐷𝑘=

<!-- b000426 | furniture | pages [10] -->
Page 10 of 25

<!-- b000427 | prose | pages [10] -->
Í𝑘

<!-- b000428 | prose | pages [10] -->
𝑖=1 𝜆𝑖

<!-- b000429 | prose | pages [10] -->
(4)

<!-- b000430 | prose | pages [10] -->
Í𝑝

<!-- b000431 | prose | pages [10] -->
𝑗=1 𝜆𝑗

<!-- b000432 | prose | pages [10] -->
Specifically, 𝑝in the formula means the number of principal components, in our paper 𝑝equals

<!-- b000433 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000434 | prose | pages [10] -->
to 18. We select the six largest eigenvalues corresponding to the cumulative contribution rate 𝐷𝑘⩾85% as the principal components. The information contribution rate and the cumulative contribution rate of each principal components is shown in Table 2.

<!-- b000435 | caption | pages [10] -->
Table 2: Contribution Rate of Principal Components

<!-- b000436 | prose | pages [10] -->
Information Contribution Rate Component 1 39.10% 2 16.26% 3 13.58% 4 6.89% 5 5.56% 6 5.27% 7 3.63% 8 3.18% Cumulative Contribution Rate 39.10% 55.36% 68.93% 75.82% 81.38% 86.65% 90.28% 93.46%

<!-- b000437 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000438 | prose | pages [10] -->
9 2.01% 10 1.35% 11 1.27% 12 0.87% 13 0.52% 14 0.25% 15 0.15% 16 0.08% 17 0.05% 18 0.01% 95.47% 96.82% 98.09% 98.89% 99.41% 99.66% 99.81% 99.89% 99.94% 100%

<!-- b000439 | prose | pages [10] -->
After calculation, the eigenvectors of the sixth largest eigenvalues are shown in Figure 6.

<!-- b000440 | prose | pages [10] -->
Indicator 1 2

<!-- b000441 | prose | pages [10] -->
S 0.3141 0.1361 G -0.2509 0.1995 P 0.0147 0.1237 A 0.2498 -0.6152 B 0.0556 -0.0314 N 0.0272 -0.0813 FSu 0.1029 -0.6193 FSc 0.1479 -0.2073 SSc 0.0546 0.0876 RSc 0.1159 0.0673 DF -0.037 -0.0305 UE -0.1677 0.0011 D -0.5621 -0.1858 V -0.286 -0.2102 SW 0.2692 0.0876 SD 0.4667 0.1195 RD -0.0751 -0.001 SC 0.0000 0.0000

<!-- b000442 | prose | pages [10] -->
3 3 4 5 6

<!-- b000443 | prose | pages [10] -->
0.3539 0.3303 -0.2017 0.2687 -0.1737 -0.2051 0.2341 0.1327 0.0459 0.0309 0.4024 0.0991 0.0717 0.0375 0.1913 -0.3198 0.0653 0.1136 -0.1435 -0.2424 0.06 0.1624 0.1308 -0.2495 -0.0975 -0.2994 0.0929 0.3146 0.0213 0.0223 0.1766 0.2622 0.0083 -0.13 0.0613 -0.5214 0.0759 0.0089 -0.0045 -0.4324 -0.041 -0.0521 0.0149 0.0412 -0.0972 0.1041 -0.0617 0.136 -0.1521 -0.1191 0.0042 -0.1685 -0.2053 0.809 -0.5104 0.0083 -0.8185 0.0404 -0.2919 -0.0345 -0.2572 0.038 0.2096 -0.0118 0.0351 -0.1219 0.4807 -0.0239 0.0000 0.0000 0.0000 0.0000

<!-- b000444 | caption | pages [10] -->
Figure 6: Corresponding Eigenvectors of the First Six Largest Principal Components

<!-- b000445 | prose | pages [10] -->
The table above displays the eigenvalues of the six principal components extracted from the indicator data of Player 1 in the final matches. The six principal components have varying emphasis on each indicator, and here we will provide a detailed explanation using Player 1 as an example, with Player 2 following a similar pattern.

<!-- b000446 | furniture | pages [10] -->
关注数学模型

<!-- b000447 | furniture | pages [10] -->
2

<!-- b000448 | furniture | pages [10] -->
MATHmodels

<!-- b000449 | furniture | pages [10] -->
获取更多资讯

<!-- b000450 | furniture | pages [11] -->
Team # 2401919

<!-- b000451 | furniture | pages [11] -->
Page 11 of 25

<!-- b000452 | prose | pages [11] -->
In the first and fifth columns, the eigenvalues with larger absolute values are concentrated in the fourth aspect of the evaluation system. The two indicators with the largest absolute eigenvalues in the first column are running distance and serving depth, while the two indicators with the largest absolute eigenvalues in the fifth column are serving speed and return depth. This reflects that the

<!-- b000453 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000454 | prose | pages [11] -->
emphasis of the first and fifth principal components is on the athlete’s technical and physical abilities.

<!-- b000455 | prose | pages [11] -->
In the second and sixth columns, the eigenvalues with larger absolute values are concentrated in the second aspect of the evaluation system. The two indicators with the largest absolute eigenvalues in the second column are the number of aces and first serve success rate, while the two indicators with the largest absolute eigenvalues in the sixth column are second serve points won rate and return points won rate. This reflects that the emphasis of the second and sixth principal components is on the athlete’s offensive efficiency.

<!-- b000456 | prose | pages [11] -->
In the third and fourth columns, the eigenvalues with larger absolute values are scattered in the first and fourth aspects. The two indicators with the largest absolute eigenvalues in the third column are serving direction in the fourth aspect and cumulative sets won in the first aspect, while the two

<!-- b000457 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000458 | prose | pages [11] -->
indicators with the largest absolute eigenvalues in the fourth column are serving speed in the fourth aspect and cumulative sets won in the first aspect. This reflects that the third and fourth principal components have a combined emphasis on the athlete’s current situation, technical and physical abilities.

<!-- b000459 | prose | pages [11] -->
We have factored the serve into our model as 𝑆𝐶𝑖, while the eigenvalues of the serve count feature in all six principal components are extremely low, indicating that the impact of the serve count on the overall evaluation system is negligible. This could be caused by that although in tennis the player serving had a much higher probability of winning the point, the two athletes take turns serving, and over time, the serve count of the two athletes tends to be equal. As a result, the role of the serve count indicator in the evaluation system in distinguishing between the two players approaches zero, and therefore, its contribution to the information is very subtle.

<!-- b000460 | prose | pages [11] -->
Therefore, we extract 6 new variables to replace the original 18 indicators. Based on the coefficients of the indicators, we obtain the principal component decision matrix.

<!-- b000461 | prose | pages [11] -->
𝑊= (𝑤𝑖𝑗) ∈R18×6 (5)

<!-- b000462 | prose | pages [11] -->
Then, we calculate the weight 𝑊𝑖of each principal component by dividing the eigenvalue 𝜆𝑖of that principal component by the sum of all eigenvalues. The weights of the principal components are identical to their information contribution rate, namely 𝑊1 = 0.3910, 𝑊2 = 0.1626, 𝑊3 = 0.1358, 𝑊4 = 0.0689, 𝑊5 = 0.0527, 𝑊6 = 0.0363.

<!-- b000463 | prose | pages [11] -->
Obtain the Scores and Visualization 3.4

<!-- b000464 | prose | pages [11] -->
We could obtain the scores simply multiply three matrices.

<!-- b000465 | prose | pages [11] -->
𝑆= 𝑍𝑊𝐼∈R𝑡×1, 𝑍∈R𝑡×𝑝, 𝑊∈R𝑝×ℎ, 𝐼∈Rℎ×1 (6)

<!-- b000466 | prose | pages [11] -->
𝑆means Score Matrix, 𝑍means Standardized Data Matrix, 𝐼means Information Contribution Rate Matrix, 𝑡means the number of time sample points, 𝑝means the number of original variables, ℎmeans the number of principal components we selected.

<!-- b000467 | furniture | pages [11] -->
关注数学模型

<!-- b000468 | furniture | pages [11] -->
2

<!-- b000469 | furniture | pages [11] -->
MATHmodels

<!-- b000470 | furniture | pages [11] -->
获取更多资讯

<!-- b000471 | furniture | pages [12] -->
Team # 2401919

<!-- b000472 | furniture | pages [12] -->
Page 12 of 25

<!-- b000473 | prose | pages [12] -->
Based on this result, we can determine the performance scores, namely "momentum" for each player in the whole match, representing the potential outcome of the game. We choose the Final between Carlos Alcaraz and Novak Djokovic for visualization, as shown in Figure 7 below.

<!-- b000474 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000475 | prose | pages [12] -->
Score Trend Chart

<!-- b000476 | prose | pages [12] -->
normalized_score

<!-- b000477 | prose | pages [12] -->
0.5

<!-- b000478 | prose | pages [12] -->
0.0

<!-- b000479 | prose | pages [12] -->
0.5

<!-- b000480 | prose | pages [12] -->
0 50 100 150

<!-- b000481 | prose | pages [12] -->
score

<!-- b000482 | prose | pages [12] -->
player1 player2

<!-- b000483 | prose | pages [12] -->
200 250 300 time

<!-- b000484 | caption | pages [12] -->
Figure 7: Score Trend Chart

<!-- b000485 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000486 | prose | pages [12] -->
We conduct the KMO and Bartlett’s test of sphericity on the model results. The KMO test yields a value of 0.8263, and the p-value of the Barlett’s sphericity test was less than 0.01, indicating that our analysis results are relatively reliable. Please refer to the KMO Test Evaluation Criteria in Appendix A.

<!-- b000487 | heading | pages [12] -->
Task3: The White Noise Tests for Our Model

<!-- b000488 | prose | pages [12] -->
4

<!-- b000489 | prose | pages [12] -->
4.1 White Noise Sequence

<!-- b000490 | prose | pages [12] -->
According to Wikipedia, a white noise sequence is a common random process in statistics and signal processing. It possesses specific characteristics that result in a uniform distribution of energy across all frequencies, consisting of a series of mutually independent random variables with identical probability distributions. These random variables have no correlation with each other, thus exhibiting complete temporal independence. This means that each value in the sequence is independently generated from the same probability distribution. The white noise test can be used to assess whether a stationary sequence is random before making predictions.

<!-- b000491 | prose | pages [12] -->
With an aim to confirm or falsify the coach’s conjecture, we have made a synonymous conversion, examining whether the generated time series of athlete performance scores, which could be approximately considered as explicit expression of implicit state, namely athlete’s momentum, are random sequences. Hence, we employ the white noise test to assess the randomness of fluctuations.

<!-- b000492 | prose | pages [12] -->
Autocorrelation Graph and Partial Autocorrelation Graph Test 4.2

<!-- b000493 | prose | pages [12] -->
By definition, white noise is a series of independent random variables with the same distribution, uncorrelated over time, meaning each value is generated independently. Under ideal conditions, except for the zero-order autocorrelation coefficient which is 1, for all k > 0, the autocorrelation coefficient with a lag of k is expected to be 0. However, due to the finite length of the sample sequence, the autocorrelation coefficient for a lag of k is not exactly 0. Instead, values near zero are considered indicative of no autocorrelation. Due to the presence of random disturbances, the autocorrelation coefficients are not strictly equal to 0. Therefore, when the autocorrelation coefficients fall within 95% confidence interval, we deem it as a white noise sequence. If a sequence has a significant

<!-- b000494 | furniture | pages [12] -->
关注数学模型

<!-- b000495 | furniture | pages [12] -->
2

<!-- b000496 | furniture | pages [12] -->
MATHmodels

<!-- b000497 | furniture | pages [12] -->
获取更多资讯

<!-- b000498 | furniture | pages [13] -->
Team # 2401919

<!-- b000499 | furniture | pages [13] -->
Page 13 of 25

<!-- b000500 | prose | pages [13] -->
number of autocorrelation coefficients outside this range, it is likely not a white noise sequence. The following explanation will be based on the autocorrelation and partial autocorrelation graphs of player 1 in the final match to illustrate that.

<!-- b000501 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000502 | prose | pages [13] -->
Autocorrelation 1.00

<!-- b000503 | prose | pages [13] -->
0.75

<!-- b000504 | prose | pages [13] -->
0.50

<!-- b000505 | prose | pages [13] -->
0.25

<!-- b000506 | prose | pages [13] -->
0.00

<!-- b000507 | prose | pages [13] -->
0.25

<!-- b000508 | prose | pages [13] -->
0.50

<!-- b000509 | prose | pages [13] -->
0.75

<!-- b000510 | prose | pages [13] -->
1.00 0 5 10 15 20

<!-- b000511 | prose | pages [13] -->
Partial Autocorrelation 1.00

<!-- b000512 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000513 | prose | pages [13] -->
0.75

<!-- b000514 | prose | pages [13] -->
0.50

<!-- b000515 | prose | pages [13] -->
0.25

<!-- b000516 | prose | pages [13] -->
0.00

<!-- b000517 | prose | pages [13] -->
0.25

<!-- b000518 | prose | pages [13] -->
0.50

<!-- b000519 | prose | pages [13] -->
0.75

<!-- b000520 | prose | pages [13] -->
1.00 0 5 10 15 20

<!-- b000521 | caption | pages [13] -->
Figure 8: Autocorrelation Graph and Partial Autocorrelation Graph

<!-- b000522 | prose | pages [13] -->
As shown in Figure 8, on the on hand, the autocorrelation plot exhibits first-order truncation, meaning that before the autocorrelation coefficients enter the 95% confidence interval, there are first-order autocorrelation coefficient values outside the boundaries. On the other hand, the partial autocorrelation plot shows fourth-order tailing, indicating that before the partial autocorrelation coefficients enter the 95% confidence interval, there are fourth-order partial autocorrelation coefficient values outside the boundaries. Summarizing from the phenomenons above, we have reasons to preliminarily believe that the sequence is likely not a white noise sequence.

<!-- b000523 | prose | pages [13] -->
Ljung-Box Test and Box-Pierce Test 4.3

<!-- b000524 | prose | pages [13] -->
In order to perform statistical tests, we make the following assumptions：

<!-- b000525 | prose | pages [13] -->
𝐻0 : 𝜌1 = 𝜌2 = . . . = 𝜌ℎ= 0 (7)

<!-- b000526 | prose | pages [13] -->
The values of the lag-h series are mutually independent, and the sequence is composed of independently and identically distributed white noise, namely the correlations in the population from which the sample is taken are 0, so that any observed correlations in the data result from

<!-- b000527 | furniture | pages [13] -->
关注数学模型

<!-- b000528 | furniture | pages [13] -->
2

<!-- b000529 | furniture | pages [13] -->
MATHmodels

<!-- b000530 | furniture | pages [13] -->
获取更多资讯

<!-- b000531 | furniture | pages [14] -->
Team # 2401919

<!-- b000532 | prose | pages [14] -->
randomness of the sampling process.

<!-- b000533 | furniture | pages [14] -->
Page 14 of 25

<!-- b000534 | prose | pages [14] -->
𝐻𝑎: ∃𝜌𝑘≠0, 1 ⩽𝑘⩽ℎ (8)

<!-- b000535 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000536 | prose | pages [14] -->
The values of the lag-h series are mutually correlative, and the sequence is composed of non-independently and identically distributed white noise, namely they exhibit serial correlation.

<!-- b000537 | prose | pages [14] -->
In traditional testing methods, a sample size less than 30 is considered as a small sample, on which Ljung-Box Test works better. Joel et al. pointed out that when the sample size is on the order of 500, Box-Pierce Test works better. In the 2023 Wimbledon Gentlemen’s Singles Final we used as an example, the amount of data is around 300, so we adopt both two statistics to gain a more comprehensive assessment of our model.

<!-- b000538 | prose | pages [14] -->
The test statistic in the Ljung-Box test is:

<!-- b000539 | prose | pages [14] -->
ℎ

<!-- b000540 | prose | pages [14] -->
ˆ𝜌2

<!-- b000541 | prose | pages [14] -->
𝑘

<!-- b000542 | prose | pages [14] -->
∑︁

<!-- b000543 | prose | pages [14] -->
𝑄𝐿𝐵= 𝑛(𝑛+ 2)

<!-- b000544 | prose | pages [14] -->
(9)

<!-- b000545 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000546 | prose | pages [14] -->
The test statistic in the Box-Pierce test is:

<!-- b000547 | prose | pages [14] -->
𝑄𝐵𝑃= 𝑛

<!-- b000548 | prose | pages [14] -->
𝑛−𝑘

<!-- b000549 | prose | pages [14] -->
𝑘=1

<!-- b000550 | prose | pages [14] -->
ℎ ∑︁

<!-- b000551 | prose | pages [14] -->
ˆ𝜌2

<!-- b000552 | prose | pages [14] -->
(10) 𝑘

<!-- b000553 | prose | pages [14] -->
𝑘=1

<!-- b000554 | prose | pages [14] -->
where 𝑛is the sample size, ˆ𝜌𝑘is the sample autocorrelation at lag 𝑘, and ℎis the number of lags being tested, which is set to ℎ= 20 here. For significance level 𝛼= 0.05, the critical region for rejection of the hypothesis of randomness is:

<!-- b000555 | prose | pages [14] -->
1−𝛼,ℎ⇔𝑝< 𝛼

<!-- b000556 | prose | pages [14] -->
𝑄> 𝜒2

<!-- b000557 | prose | pages [14] -->
(11)

<!-- b000558 | prose | pages [14] -->
According to the Ljung-Box test and Box-Pierce test, we have the following explanations. Results show that 𝑝𝐿𝐵= 6.645 × 10−13 and 𝑝𝐵𝑃= 2.087 × 10−12. Both the p-values from the Ljung-Box test and the Box-Pierce test are much smaller than 0.05, leading us to reject the null hypothesis. Therefore, the sequence is not a white noise sequence. This conclusion aligns with the results obtained from the autocorrelation and partial autocorrelation analysis, which both indicate that the sequence is not a random sequence.

<!-- b000559 | heading | pages [14] -->
Complete Results and Conclusions

<!-- b000560 | prose | pages [14] -->
4.4

<!-- b000561 | prose | pages [14] -->
Based on the aforementioned white noise testing methods, we conducted tests on a total of 62 sequences from 31 matches. Among them, 60 sequences were found to be non-white-noise, while only 2 sequences were identified as white noise. This indicates that the non-random sequence rate is as high as 96.78%. At this point we could overturn the coach’s statement, as the swings in play and runs of success by one player are obviously not random.

<!-- b000562 | furniture | pages [14] -->
关注数学模型

<!-- b000563 | furniture | pages [14] -->
2

<!-- b000564 | furniture | pages [14] -->
MATHmodels

<!-- b000565 | furniture | pages [14] -->
获取更多资讯

<!-- b000566 | furniture | pages [15] -->
Team # 2401919

<!-- b000567 | furniture | pages [15] -->
Page 15 of 25

<!-- b000568 | heading | pages [15] -->
Task4: Momentum Swings GM(1,1) Grey Prediction Model

<!-- b000569 | prose | pages [15] -->
5

<!-- b000570 | prose | pages [15] -->
5.1

<!-- b000571 | heading | pages [15] -->
Data Processing and Examination

<!-- b000572 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000573 | prose | pages [15] -->
5.1.1 Construction of New Sequence

<!-- b000574 | prose | pages [15] -->
To predict when a match undergoes swings in momentum, transitioning from one player to another, we extend our evaluation model to achieve the goal. Firstly, we subtract the scores of the two players at each sample point to obtain the difference between their scores, creating a new sequence of {Δ𝑀1, Δ𝑀2, . . . , Δ𝑀𝑛}. The value above zero in this sequence means that player 1 outperforms player 2 and vice versa. While this could not be considered as "momentum swings", so we use the difference between adjacent moments as a standard to detect drastic changes. After that we get an IAGO sequence. Only when the difference surpasses our predetermined threshold, we consider it as a swing in momentum during the match. Eventually, we pick the eligible time point out to generate a brand-new ”catastrophic sequence“ for future prediction, which is displayed as {𝑡(0)(1), 𝑡(0)(2), . . . , 𝑡(0)(𝑛)}.

<!-- b000575 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000576 | prose | pages [15] -->
5.1.2 Level Comparison Test

<!-- b000577 | prose | pages [15] -->
To ensure the feasibility of the modeling method, it is necessary to perform inspection and processing on the sequence, one of which is calculating the ratio of the series. If all the ratios 𝜆(𝑘)

<!-- b000578 | prose | pages [15] -->


<!-- b000579 | prose | pages [15] -->


<!-- b000580 | prose | pages [15] -->
𝑒−2

<!-- b000581 | prose | pages [15] -->
2

<!-- b000582 | prose | pages [15] -->
𝑛+1, 𝑒

<!-- b000583 | prose | pages [15] -->
fall within the interval Θ =

<!-- b000584 | prose | pages [15] -->
, the sequence can be used in the construction of GM(1,1)

<!-- b000585 | prose | pages [15] -->
𝑛+1

<!-- b000586 | prose | pages [15] -->
model. Below is the calculation formula of level ratio.

<!-- b000587 | prose | pages [15] -->
𝜆(𝑘) = 𝑡(0)(𝑘−1)

<!-- b000588 | prose | pages [15] -->
𝑡(0)(𝑘) , , 𝑘= 2, 3, · · · , 𝑛 (12)

<!-- b000589 | prose | pages [15] -->
After inspection, all of the ratios fall within the interval of (0.9200, 1.0869). Therefore, there is no need for a translation transformation, and the GM(1,1) model is applicable.

<!-- b000590 | heading | pages [15] -->
Utilize the Model to Obtain the Predicted Values

<!-- b000591 | prose | pages [15] -->
5.2

<!-- b000592 | heading | pages [15] -->
Build Momentum Swings Grey Forecasting Model

<!-- b000593 | prose | pages [15] -->
5.2.1

<!-- b000594 | prose | pages [15] -->
Disaster prediction, also known as disaster grey prediction, is an application of the GM(1,1) grey prediction model. Specifically, it involves identifying abnormal points (or so-called disaster points) in a sequence, which are points that are either significantly larger or smaller than the others. These abnormal points are then used to construct a subsequence and from this subsequence, a time distribution sequence is obtained. GM(1,1) model is then established for the time distribution sequence of the abnormal points to predict their future time distribution, thus determining when the abnormal points are likely to occur in the future.

<!-- b000595 | prose | pages [15] -->
Based on this idea and previous data processing, we extract all time points that exceed a certain threshold to form a new sequence. Subsequently, we construct a GM(1,1) grey prediction model, considering all points exceeding the threshold as turning points in the prediction and predict their time distribution based on the established model.

<!-- b000596 | prose | pages [15] -->
Grey forecasting refers to the estimation and prediction of the developmental patterns of system

<!-- b000597 | furniture | pages [15] -->
关注数学模型

<!-- b000598 | furniture | pages [15] -->
2

<!-- b000599 | furniture | pages [15] -->
MATHmodels

<!-- b000600 | furniture | pages [15] -->
获取更多资讯

<!-- b000601 | furniture | pages [16] -->
Team # 2401919

<!-- b000602 | furniture | pages [16] -->
Page 16 of 25

<!-- b000603 | prose | pages [16] -->
behavior characteristics using the GM model. It can also be used to estimate and calculate the occurrence time of abnormal behavior characteristics, as well as study the future time distribution of events within a specific time zone, and so on. It is evident that the functionality of this model aligns with the requirements of our need. As a consequence, we generate the AGO sequence and average

<!-- b000604 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000605 | prose | pages [16] -->
sequence below.

<!-- b000606 | prose | pages [16] -->
𝑡(1) = (𝑡(1)(1), 𝑡(1)(2), . . . , 𝑡(1)(𝑛)),

<!-- b000607 | prose | pages [16] -->
𝑧(1) = (𝑧(1)(2), 𝑧(1)(3), . . . , 𝑧(1)(𝑛)),

<!-- b000608 | prose | pages [16] -->
𝑘 ∑︁

<!-- b000609 | prose | pages [16] -->
𝑡(1)(𝑘) =

<!-- b000610 | prose | pages [16] -->
𝑡(0)(𝑖), 𝑘= 1, 2, . . . , 𝑛

<!-- b000611 | prose | pages [16] -->
𝑖=1

<!-- b000612 | prose | pages [16] -->
𝑧(1)(𝑘) = 0.5𝑥(1)(𝑘) + 0.5𝑥(1)(𝑘−1), 𝑘= 2, 3, . . . , 𝑛

<!-- b000613 | prose | pages [16] -->
Then we establish the grey differential equation, where 𝑎and 𝑏are unknown parameters.

<!-- b000614 | prose | pages [16] -->
𝑡(0)(𝑘) + 𝑎𝑧(1)(𝑘) = 𝑏, 𝑘= 2, 3, . . . , 𝑛 (13)

<!-- b000615 | prose | pages [16] -->
Then the corresponding whitening differential equation is written as below, where m is a

<!-- b000616 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000617 | prose | pages [16] -->
continous variable.

<!-- b000618 | prose | pages [16] -->
𝑑𝑡(1)

<!-- b000619 | prose | pages [16] -->
𝑑𝑚+ 𝑎𝑡(1)(𝑚) = 𝑏 (14)

<!-- b000620 | prose | pages [16] -->
−𝑧(1)(2) 1

<!-- b000621 | prose | pages [16] -->


<!-- b000622 | prose | pages [16] -->


<!-- b000623 | prose | pages [16] -->
−𝑧(1)(3) 1

<!-- b000624 | prose | pages [16] -->
We define 𝑢= (𝑎, 𝑏)𝑇, 𝑌= (𝑡(0)(2), 𝑡(0)(3), . . . , 𝑡(0)(𝑛))𝑇, 𝐵=

<!-- b000625 | prose | pages [16] -->
... ...

<!-- b000626 | prose | pages [16] -->
By least square

<!-- b000627 | prose | pages [16] -->
−𝑧(1)(𝑛) 1

<!-- b000628 | prose | pages [16] -->
method, we could find the ˆ𝑢= (𝐵𝑇𝐵)−1𝐵𝑇𝑌that makes 𝐽( ˆ𝑢) = (𝑌−𝐵ˆ𝑢)𝑇(𝑌−𝐵ˆ𝑢) obtain the minimum value. By solving the whitening differential equation, we can obtain the predictive values, which is explicitly represented below.

<!-- b000629 | prose | pages [16] -->
𝑎)𝑒−𝑎𝑘+ 𝑏

<!-- b000630 | prose | pages [16] -->
𝑡(1)(𝑘+ 1) = (𝑡(0)(1) −𝑏

<!-- b000631 | prose | pages [16] -->
𝑎, 𝑘= 0, 1, . . . , 𝑛−1, . . .

<!-- b000632 | prose | pages [16] -->
(15)

<!-- b000633 | prose | pages [16] -->
When the predictive value exceeds the threshold, it is defined as 1 (representing a turning point), otherwise it is defined as 0. We can obtain the comparison results between the predictive values and the original data, as shown in Figure 9.

<!-- b000634 | prose | pages [16] -->
As can be seen from the graph, the predicted values closely match or even overlap with the actual values, indicating a high level of fit and accuracy in this model. This accuracy is closely related to the characteristics of the GM(1,1) model, which is suitable for sequences with a small amount of data (around 20) and short-to-medium-term predictions.

<!-- b000635 | prose | pages [16] -->
5.3

<!-- b000636 | heading | pages [16] -->
Model Diagnosis

<!-- b000637 | prose | pages [16] -->
Based on the diagnosis, the average relative error Δ of this model is 0.0378, indicating a Second Class accuracy. Additionally, the absolute correlation 𝑔0 is calculated as 0.9895, and the mean square deviation ratio 𝐶0 is 0.1284, both indicating a First Class accuracy. These results indicate a high level of accuracy in the model, making it suitable for predicting turning points in competitions. Please refer to the Appendix A for the evaluation criteria.

<!-- b000638 | furniture | pages [16] -->
关注数学模型

<!-- b000639 | furniture | pages [16] -->
2

<!-- b000640 | furniture | pages [16] -->
MATHmodels

<!-- b000641 | furniture | pages [16] -->
获取更多资讯

<!-- b000642 | furniture | pages [17] -->
Team # 2401919

<!-- b000643 | furniture | pages [17] -->
Page 17 of 25

<!-- b000644 | prose | pages [17] -->
Predict Turning Point

<!-- b000645 | prose | pages [17] -->
1

<!-- b000646 | prose | pages [17] -->
actual_value predictive_value

<!-- b000647 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000648 | prose | pages [17] -->
Turning Point

<!-- b000649 | prose | pages [17] -->
0

<!-- b000650 | prose | pages [17] -->
0 50 100 150 200 250 300 350 Time

<!-- b000651 | caption | pages [17] -->
Figure 9: Predictive and Actual Turning plot in Gentlemen’s Singles Final

<!-- b000652 | prose | pages [17] -->
6 Task5: Quantify the Impact of Different Factors on the Swings

<!-- b000653 | prose | pages [17] -->
6.1 Gray Relational Analysis

<!-- b000654 | prose | pages [17] -->
Grey relational analysis gauges the relationship between sequences by comparing their geometric

<!-- b000655 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000656 | prose | pages [17] -->
It involves converting discrete data points into continuous line graphs using linear shapes. interpolation. A model is then built to assess correlation based on the geometric features of these graphs. The closer the shapes, the higher the correlation between the sequences.

<!-- b000657 | prose | pages [17] -->
To explore the correlation between various factors and match fluctuations, let’s consider the final match as an example. We apply the grey relational analysis method to calculate the correlation between the sequences of various indicators and the performance difference sequences of the two athletes. This analysis helps us determine which factors are most related to match swings and provide corresponding recommendations for improving performance.

<!-- b000658 | prose | pages [17] -->
We denote the reference sequence as {Δ𝑀1, Δ𝑀2, . . . , Δ𝑀𝑛}, and we have 18 comparison se- quences collectively referred to asΔ𝑝, specifically {Δ𝑆1, Δ𝑆2, . . . , Δ𝑆𝑛}, . . . , {Δ𝑆𝐶1, Δ𝑆𝐶2, . . . , Δ𝑆𝐶𝑛}, corresponding to the difference between the 18 indicators of player 1 and player 2. Then we calculate the correlation coefficient using the following formula, taking the Δ𝑆sequence for example.

<!-- b000659 | prose | pages [17] -->
𝜉𝑖(𝑘) = min𝑝min𝑡|Δ𝑀(𝑡) −Δ𝑝(𝑡)| + 𝜌max𝑝max𝑡|Δ𝑀(𝑡) −Δ𝑝(𝑡)|

<!-- b000660 | prose | pages [17] -->
(16) |Δ𝑀(𝑘) −Δ𝑆(𝑘)| + 𝜌max𝑝max𝑡|Δ𝑀(𝑡) −Δ𝑝(𝑡)|

<!-- b000661 | prose | pages [17] -->
Where 𝜌∈[0, 1] represents the resolution coefficient. Generally, a higher 𝜌value indicates a higher resolution, while a lower 𝜌value indicates a lower resolution. The correlation coefficient defined in the above equation is an indicator that describes the degree of correlation between the comparison sequence and the reference sequence at a certain moment. Since there is a correlation coefficient for each moment, the information appears to be too scattered and inconvenient for comparison. Therefore, we provide the following equation as a measure of the correlation between the sequence Δ𝑀and the reference sequences.

<!-- b000662 | prose | pages [17] -->
𝑟𝑖= 1

<!-- b000663 | prose | pages [17] -->
𝑛

<!-- b000664 | prose | pages [17] -->
𝑛 𝑛 ∑︁

<!-- b000665 | prose | pages [17] -->
𝜉𝑖(𝑘) (17)

<!-- b000666 | prose | pages [17] -->
𝑘=1

<!-- b000667 | prose | pages [17] -->
After calculation, the correlation of each indicator is shown in Table 3.

<!-- b000668 | furniture | pages [17] -->
关注数学模型

<!-- b000669 | furniture | pages [17] -->
2

<!-- b000670 | furniture | pages [17] -->
MATHmodels

<!-- b000671 | furniture | pages [17] -->
获取更多资讯

<!-- b000672 | furniture | pages [18] -->
Team # 2401919

<!-- b000673 | furniture | pages [18] -->
Page 18 of 25

<!-- b000674 | caption | pages [18] -->
Table 3: Correlation of 18 Indicators

<!-- b000675 | prose | pages [18] -->
𝑟𝑆 𝑟𝐺 𝑟𝑃 𝑟𝐴 𝑟𝐵 𝑟𝑁 𝑟𝐹𝑆𝑢 𝑟𝐹𝑆𝑐 𝑟𝑆𝑆𝑐 0.9239 0.9244 0.9250 0.8330 0.9238 0.9239 0.9246 0.9237 0.9239

<!-- b000676 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000677 | prose | pages [18] -->
𝑟𝑅𝑆𝑐 𝑟𝐷𝐹 𝑟𝑈𝐸 𝑟𝐷 𝑟𝑉 𝑟𝑆𝑊 𝑟𝑆𝐷 𝑟𝑅𝐷 𝑟𝑆𝐶 0.8993 0.9237 −0.9238 −0.9008 0.6744 0.8043 0.8846 0.8866 0.7953

<!-- b000678 | prose | pages [18] -->
From the perspective of various refined indicators, the indicator with the highest correlation is the cumulative number of games won, with the correlation 𝑟𝐺reaching 0.9250. This indicates that in the long term, this indicator has the highest correlation with the swings in the match, and the ability of players to break through in games is the most crucial factor in reversing the situation.

<!-- b000679 | prose | pages [18] -->
From the perspective of the five aspects of the evaluation system, the aspect with the highest overall correlation is the second aspect, which is the offensive efficiency of players, with an average correlation of 0.9239. This is the highest average correlation among the five aspects, indicating that

<!-- b000680 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000681 | prose | pages [18] -->
in the long term, the offensive efficiency of players, specifically their ability to break through in attacks, is the most crucial aspect in reversing the situation and igniting momentum.

<!-- b000682 | prose | pages [18] -->
Advice to a Player Going into a New Match 6.2

<!-- b000683 | prose | pages [18] -->
Based on the different correlations between the above indicators, aspects, and momentum swings, we provide the following recommendations for players:

<!-- b000684 | prose | pages [18] -->
Firstly, from a broader perspective, offensive efficiency is identified as the key aspect to influence the changes in the match situation. Emphasis should be placed on the athlete’s proactive approach to real-time attacks and their ability to seek breakthroughs. When facing a new opponent in a new match, the athlete is confronted with unknown and unpredictable external factors. Therefore, the athlete should firstly focus more on their own performance, take the initiative to launch attacks, and seize opportunities to break through, rather than solely adopting a passive defensive strategy. Simultaneously, in unfamiliar competition environments, athletes should boldly try different offensive tactics, identify the weak points of their opponents, gradually take control of the situation, and gain momentum.

<!-- b000685 | prose | pages [18] -->
From a more detailed perspective, the cumulative number of games won is identified as the most crucial factor for the match swings. Each game consists of many points, requiring the athlete to have a comprehensive understanding of the overall situation, including the allocation of physical energy, changeable tactical choices, targeted strategies for server and returner, and so on. This tests the athlete’s ability to coordinate and plan comprehensively. Furthermore, comparing the correlation coefficient of cumulative points, which is only 0.833, further emphasizes that the most crucial factor for an athlete in reversing the situation is not just winning individual points but rather adopting a long-term strategy.

<!-- b000686 | heading | pages [18] -->
Task6: Test the Accuracy of the Prediction Model

<!-- b000687 | prose | pages [18] -->
7

<!-- b000688 | prose | pages [18] -->
To further examine the predictive performance of this model, we have also selected data from the 2023 Wimbledon Gentlemen’s Singles Semi-final (Jannik Sinner vs Novak Djokovic) to make

<!-- b000689 | furniture | pages [18] -->
关注数学模型

<!-- b000690 | furniture | pages [18] -->
2

<!-- b000691 | furniture | pages [18] -->
MATHmodels

<!-- b000692 | furniture | pages [18] -->
获取更多资讯

<!-- b000693 | furniture | pages [19] -->
Team # 2401919

<!-- b000694 | furniture | pages [19] -->
Page 19 of 25

<!-- b000695 | prose | pages [19] -->
predictions and compare them with the actual match flow. Below is the comparison graph displaying the predictive turning points alongside the actual turning points.

<!-- b000696 | prose | pages [19] -->
Predict Turning Point-2023 Wimbledon Gentlemen's Single Semifinal

<!-- b000697 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000698 | prose | pages [19] -->
1

<!-- b000699 | prose | pages [19] -->
Turning Point

<!-- b000700 | prose | pages [19] -->
0

<!-- b000701 | prose | pages [19] -->
0 50 100

<!-- b000702 | prose | pages [19] -->
actual_value predictive_value

<!-- b000703 | prose | pages [19] -->
150 200 Time

<!-- b000704 | caption | pages [19] -->
Figure 10: Predictive and Actual Turning Points in Gentlemen’s Singles Semifinal

<!-- b000705 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000706 | prose | pages [19] -->
The average relative error of this model is 0.0883, indicating a Third Class accuracy. The absolute correlation is calculated as 0.9716, and the mean square deviation ratio is 0.2859, both indicating a First Class accuracy. These results all indicate a relatively high level of accuracy, but worse compared to the Final. And we can observe that the predictive turning points are somewhat delayed compared to the actual turning points.

<!-- b000707 | prose | pages [19] -->
In order to enhance the predictive performance of this model in the future, we are considering incorporating the following factors:

<!-- b000708 | prose | pages [19] -->
• Health condition: This includes the physical health and injury status of the players. Being in good physical condition can ensure that the players perform at their best during the match.

<!-- b000709 | prose | pages [19] -->
• Court environment: This includes court conditions , weather conditions, and the atmosphere created by the audience. Different court environments can have a significant impact on the performance of the players.

<!-- b000710 | prose | pages [19] -->
• Competitor: This includes the level and tactical style of the competitor. Strong competitors can increase the pressure and tension for the players, affecting their performance.

<!-- b000711 | heading | pages [19] -->
Task7: Generalize the Model Applicable to Other Matches

<!-- b000712 | prose | pages [19] -->
8

<!-- b000713 | prose | pages [19] -->
Women’s tennis matches, compared to men’s tennis matches, tend to prioritize technique, strategy, and agility. On the other hand, men’s tennis matches may place more emphasis on strength and speed. And In Grand Slam tournaments, men play best-of-five sets, while women play best-of-three sets. This means that men’s matches can potentially last longer than women’s matches, so the physical fitness and endurance requirements are also higher.

<!-- b000714 | prose | pages [19] -->
To investigate the generalizability of our model to other matches, we substitute the match data from the 2023 Wimbledon Ladies’ Singles Final (Marketa Vondrousova vs Ons Jabeur) into the model to test its predictive performance. As shown in the figure below：

<!-- b000715 | furniture | pages [19] -->
关注数学模型

<!-- b000716 | furniture | pages [19] -->
2

<!-- b000717 | furniture | pages [19] -->
MATHmodels

<!-- b000718 | furniture | pages [19] -->
获取更多资讯

<!-- b000719 | furniture | pages [20] -->
Team # 2401919

<!-- b000720 | furniture | pages [20] -->
Page 20 of 25

<!-- b000721 | prose | pages [20] -->
Predict Turning Point-2023 Wimbledon Ladies' Single Final

<!-- b000722 | prose | pages [20] -->
1

<!-- b000723 | prose | pages [20] -->
actual_value predictive_value

<!-- b000724 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000725 | prose | pages [20] -->
Turning Point

<!-- b000726 | prose | pages [20] -->
0

<!-- b000727 | prose | pages [20] -->
0 20 40 60 80 100 120 Time

<!-- b000728 | caption | pages [20] -->
Figure 11: Predictive and Actual Turning Points in Ladies’ Singles Final

<!-- b000729 | prose | pages [20] -->
As shown in the figure, the overall predictive performance is good, with rather small deviation from the actual turning points. The average relative error of this model is 0.0693, indicating a Third Class accuracy. The absolute correlation is calculated as 0.9896, and the mean square deviation

<!-- b000730 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000731 | prose | pages [20] -->
ratio is 0.2908, both indicating a First Class accuracy. These results all indicate a relatively high level of accuracy, but worse compared to the Gentlemen’s matches.

<!-- b000732 | caption | pages [20] -->
Figure 12: Contrast of Three Matches

<!-- b000733 | prose | pages [20] -->
We also plotted the predictive performance of the three matches separately in Figure 12. The closer the shape of the curve aligns with the exponential growth GM model, the more accurate the predictions are. From the graph, we can see that the predictions for the men’s singles final and semi-final matches are consistent with the exponential growth, while there are some differences between the exponential growth and the predictions for the women’s singles final match. We speculate that the difference may be due to the differences in the match format and the physical characteristics between men and women in sports.

<!-- b000734 | furniture | pages [20] -->
关注数学模型

<!-- b000735 | furniture | pages [20] -->
2

<!-- b000736 | furniture | pages [20] -->
MATHmodels

<!-- b000737 | furniture | pages [20] -->
获取更多资讯

<!-- b000738 | furniture | pages [21] -->
Team # 2401919

<!-- b000739 | prose | pages [21] -->
9

<!-- b000740 | heading | pages [21] -->
Sensitivity Analysis

<!-- b000741 | furniture | pages [21] -->
Page 21 of 25

<!-- b000742 | prose | pages [21] -->
To test the sensitivity of the PCA-TOPSIS model, we perturbed the weights of the most influential variable, which is the number of games won, by increasing and decreasing them manually by 20%.

<!-- b000743 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000744 | prose | pages [21] -->
Then we calculated the results and plotted the comparison chart as Figure 13.

<!-- b000745 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000746 | caption | pages [21] -->
Figure 13: Sensitivity Analysis

<!-- b000747 | prose | pages [21] -->
As can be seen from the graph, the variations in the results are small, indicating that the model has good generalizability, and is relatively robust.

<!-- b000748 | prose | pages [21] -->
10

<!-- b000749 | heading | pages [21] -->
Model Assessment

<!-- b000750 | prose | pages [21] -->
10.1

<!-- b000751 | heading | pages [21] -->
Strengths

<!-- b000752 | prose | pages [21] -->
• Individual models for each player allows for a more targeted approach.

<!-- b000753 | prose | pages [21] -->
• The evaluation model established by combining PCA and TOPSIS models takes advantage of both methods, making it more objective and accurate.

<!-- b000754 | prose | pages [21] -->
• The GM(1,1) gray prediction model has a good predictive effect and high generalizability.

<!-- b000755 | prose | pages [21] -->
10.2

<!-- b000756 | heading | pages [21] -->
Weaknesses

<!-- b000757 | prose | pages [21] -->
• The factors selected are not comprehensive enough and the model overlooks some important factors like health condition, court environment and so on.

<!-- b000758 | prose | pages [21] -->
• The model is not suitable for long-term predictions and is only applicable for short-term interval predictions.

<!-- b000759 | prose | pages [21] -->
• Due to the different tournament formats and specific characteristics of different sports, predicting matches in other categories requires certain parameter adjustments.

<!-- b000760 | furniture | pages [21] -->
关注数学模型

<!-- b000761 | furniture | pages [21] -->
2

<!-- b000762 | furniture | pages [21] -->
MATHmodels

<!-- b000763 | furniture | pages [21] -->
获取更多资讯

<!-- b000764 | furniture | pages [22] -->
Team # 2401919

<!-- b000765 | prose | pages [22] -->
11

<!-- b000766 | heading | pages [22] -->
Letter

<!-- b000767 | furniture | pages [22] -->


<!-- b000768 | furniture | pages [22] -->
Page 22 of 25

<!-- b000769 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000770 | prose | pages [22] -->
Dear Sir or Madam:

<!-- b000771 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000772 | furniture | pages [22] -->


<!-- b000773 | prose | pages [22] -->
It is our great honor to provide tennis match preparation strategies for your players. Based on the factors in the provided data files, we build mathematical models to capture the flow of the performance of the players over time, and establish a comprehensive and practical evaluation system. Our approaches, findings, and suggestions are as follows.

<!-- b000774 | prose | pages [22] -->
Firstly, we have combined existing literature to establish a comprehensive evaluation system consisting of five

<!-- b000775 | furniture | pages [22] -->


<!-- b000776 | prose | pages [22] -->
major aspects. We have carefully selected appropriate indicators from the raw data. Secondly, in order to accurately analyze the impact of each indicator on players’ performance, we have conducted data normalization and employed advanced analytical methods to calculate the weights of each indicator. Furthermore, based on an advanced evaluation model, we have obtained performance scores for players, which reflect their momentum at different moments and demonstrate its non-randomness. Lastly, using an advanced forecasting model, we have predicted turning points in the competition and provided evidence of its effectiveness.

<!-- b000777 | prose | pages [22] -->
Here are some findings based on our results.  The momentum of players on the field can be seen as their performance, which can be further divided into five major aspects: current situation, offensive effectiveness, error situation, technical fitness, and starting advantage. The comprehensive performance of players in each aspect reflects their strength and weakness on the field. The momentum of players at every moment is closely related to their cumulative performance before that moment.  The fluctuations and turning points in players’ on-field performance are not random. In other words, the changes in players’ momentum during a competition are not without trace; there are underlying rules and mechanisms behind them. Moreover, momentum is closely related to the game situation. It is evident that momentum plays a crucial role in players’ ability to grasp and reverse the game situation, ultimately leading to success and continuous progress.  The turning points in a game are closely related to the number of games won by the athlete and their offensive effectiveness on the field. The athlete’s ability to break through in games and their efficiency and capability in offensive breakthroughs are key factors in determining whether they can ignite momentum and reverse the game situation. Based on these findings, we put forward some match preparation strategies as follows.  Focus on improving on-field offensive capabilities. In the face of fluctuations in the game situation, learn to take the initiative to attack, actively seek breakthroughs, improve the ability to seize control of the game, and create opportunities proactively.  Emphasize improving on-field offensive efficiency. In the face of changes on the field, it is not only important to create opportunities but also to capitalize on them, improving offensive efficiency and turning advantages into winning positions.  Pay attention to improving receiving and serving skills. When the game situation changes, strive to ensure the quality and stability of receiving and serving, while also accelerating the pace of hitting and the ability to quickly end the game in short rallies, strengthening awareness and ability to intercept at the net.  Focus on enhancing comprehensive coordination abilities on the field. When facing fluctuations in the game situation, tactically coordinate the overall situation, and scientifically allocate physical fitness. Cultivate a long-term perspective and avoid pursuing short-term gains, only focusing on immediate points. We hope our suggestions are helpful. If you have any question, please feel free to contact us.

<!-- b000778 | furniture | pages [22] -->


<!-- b000779 | prose | pages [22] -->
Sincerely,

<!-- b000780 | furniture | pages [22] -->
Team # 2401919 Members

<!-- b000781 | furniture | pages [22] -->
关注数学模型

<!-- b000782 | furniture | pages [22] -->
2

<!-- b000783 | furniture | pages [22] -->
MATHmodels

<!-- b000784 | furniture | pages [22] -->
获取更多资讯

<!-- b000785 | furniture | pages [23] -->
Team # 2401919

<!-- b000786 | heading | pages [23] -->
References

<!-- b000787 | furniture | pages [23] -->
Page 23 of 25

<!-- b000788 | references | pages [23] -->
[1] Yan, Y. F.: Research on the construction of a sports intelligence evaluation index system for high-level

<!-- b000789 | references | pages [23] -->
tennis players in sports colleges based on AHP-TOPSIS analysis[D].Shandong Institute of P.E. and

<!-- b000790 | references | pages [23] -->
微信公众号：数学模型

<!-- b000791 | references | pages [23] -->
Sports,2023.DOI:10.27725/d.cnki.gsdty.2023.000137.

<!-- b000792 | references | pages [23] -->
[2] Meng, F. M., Huang, W. M.: Analysis of Female Tennis Players Winning Factors Based on Decision

<!-- b000793 | references | pages [23] -->
Tree[J].Journal of Jilin Sport University,2019,35(05):43-47.DOI:10.13720/j.cnki.22-1286.2019.05.007.

<!-- b000794 | references | pages [23] -->
[3] Richardson P A, Adler W, Hankes D. Game, set, match: Psychological momentum in tennis[J]. The

<!-- b000795 | references | pages [23] -->
Sport Psychologist, 1988, 2(1): 69-76.

<!-- b000796 | references | pages [23] -->
[4] Ma, J. C., Chen, Q. G., Liang, C. R., Zhou, Z. C.: Model Construction and Research Analysis of

<!-- b000797 | references | pages [23] -->
Winning Factors of Professional Tennis Players in Competitions[J].Bulletin of Sport Science and

<!-- b000798 | references | pages [23] -->
Technology,2023,31(04):66-68+118.DOI:10.19379/j.cnki.issn.1005-0256.2023.04.021.

<!-- b000799 | references | pages [23] -->
[5] He, W. S., Zhang, L. W., Zhang, L. C.:Technical analysis of winning factors of world’s top

<!-- b000800 | references | pages [23] -->
there male tennis players[J].Journal of Wuhan Institute of Physical Education,2011,45(09):67-

<!-- b000801 | references | pages [23] -->
微信号：MATHmodels

<!-- b000802 | references | pages [23] -->
73.DOI:10.15930/j.cnki.wtxb.2011.09.016.

<!-- b000803 | references | pages [23] -->
[6] Dietl H, Nesseler C. Momentum in tennis: Controlling the match[J]. UZH Business Working Paper

<!-- b000804 | references | pages [23] -->
Series, 2017 (365).

<!-- b000805 | references | pages [23] -->
[7] Silva J M, Hardy C J, Crace R K. Analysis of psychological momentum in intercollegiate tennis[J].

<!-- b000806 | references | pages [23] -->
Journal of sport and exercise psychology, 1988, 10(3): 346-354.

<!-- b000807 | references | pages [23] -->
[8] Bahamonde R E. Changes in angular momentum during the tennis serve[J]. Journal of sports sciences,

<!-- b000808 | references | pages [23] -->
2000, 18(8): 579-592.

<!-- b000809 | references | pages [23] -->
[9] Weinberg R, Jackson A. The effects of psychological momentum on male and female tennis players

<!-- b000810 | references | pages [23] -->
revisited[J]. Journal of Sport Behavior, 1989, 12(3): 167.

<!-- b000811 | heading | pages [23] -->
Appendices

<!-- b000812 | prose | pages [23] -->
Evaluation Criteria

<!-- b000813 | heading | pages [23] -->
Appendix A

<!-- b000814 | caption | pages [23] -->
Table 4: KMO Test Evaluation Criteria

<!-- b000815 | prose | pages [23] -->
KMO measure KMO⩾0.90 0.80 ⩽KMO< 0.90 0.70 ⩽KMO< 0.80 0.60 ⩽KMO< 0.70 0.50 ⩽KMO< 0.60 KMO< 0.50 Interpretation Marvelous Meritorious Average Mediocre Terrible Unacceptable

<!-- b000816 | furniture | pages [23] -->
关注数学模型

<!-- b000817 | furniture | pages [23] -->
2

<!-- b000818 | furniture | pages [23] -->
MATHmodels

<!-- b000819 | furniture | pages [23] -->
获取更多资讯

<!-- b000820 | furniture | pages [24] -->
Team # 2401919

<!-- b000821 | furniture | pages [24] -->
Page 24 of 25

<!-- b000822 | caption | pages [24] -->
Table 5: Grey Prediction Evaluation Criteria

<!-- b000823 | prose | pages [24] -->
Class

<!-- b000824 | prose | pages [24] -->
Average Relative Error

<!-- b000825 | prose | pages [24] -->
Indicators

<!-- b000826 | prose | pages [24] -->
Absolute Correlation Mean Deviation Ratio

<!-- b000827 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000828 | prose | pages [24] -->
0.01 First Class

<!-- b000829 | prose | pages [24] -->
0.05 Second Class

<!-- b000830 | prose | pages [24] -->
0.10 Third Class

<!-- b000831 | prose | pages [24] -->
0.20 Fourth CLass

<!-- b000832 | heading | pages [24] -->
Appendix B

<!-- b000833 | prose | pages [24] -->
Code

<!-- b000834 | prose | pages [24] -->
Correlation Heatmap.py

<!-- b000835 | prose | pages [24] -->
0.90 0.35

<!-- b000836 | prose | pages [24] -->
0.80 0.50

<!-- b000837 | prose | pages [24] -->
0.70 0.65

<!-- b000838 | prose | pages [24] -->
0.60 0.80

<!-- b000839 | prose | pages [24] -->
correlation_matrix = np.corrcoef(standardized_data, rowvar=False) variables = [’S1’, ’G1’, ’P1’, ’A1’, ’B1’, ’N1’, ’FSu1’, ’FSc1’, ’SSc1’, ’RSc1

<!-- b000840 | prose | pages [24] -->
↩→’, ’DF1’, ’UE1’, ’D1’, ’V1’, ’SW1’, ’SD1’, ’RD1’, ’SC1’, ’S2’, ’G2’, ’ ↩→P2’, ’A2’, ’B2’, ’N2’, ’FSu2’, ’FSc2’, ’SSc2’, ’RSc2’, ’DF2’, ’UE2’, ’

<!-- b000841 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000842 | prose | pages [24] -->
↩→D2’, ’V2’, ’SW2’, ’SD2’, ’RD2’, ’SC2’] corr_mat = correlation_matrix rows, cols = np.where(corr_mat != 0) correlation_data = pd.DataFrame({’level_0’: rows, ’level_1’: cols, ’

<!-- b000843 | prose | pages [24] -->
↩→correlation’: corr_mat[rows, cols]}) sns.set_theme(style="whitegrid") cmap = sns.diverging_palette(240, 120, as_cmap=True) g = sns.scatterplot(data=correlation_data, x="level_0", y="level_1", hue="

<!-- b000844 | prose | pages [24] -->
↩→correlation", size="correlation",

<!-- b000845 | prose | pages [24] -->
palette=cmap, sizes=(50, 250), size_norm=(-.2, .8),

<!-- b000846 | prose | pages [24] -->
↩→edgecolor=".7") g.set(xlabel="", ylabel="", aspect="equal") plt.xticks(ticks=np.arange(len(variables)), labels=variables, rotation=90) plt.yticks(ticks=np.arange(len(variables)), labels=variables) sns.despine(left=True, bottom=True) plt.legend(loc=’center right’, bbox_to_anchor=(1.2, 0.5), title="Legend") plt.title(label=’Correlation Coefficient Matrix Heat Map’, pad=10) plt.show()

<!-- b000847 | prose | pages [24] -->
Predict Swings.py

<!-- b000848 | prose | pages [24] -->
predicted_sequence, a, b = GM_11(original_sequence) Evaluate(original_sequence, predicted_sequence) length = max(np.max(original_sequence), np.max(predicted_sequence))+10 x = np.arange(0, length, 1) y = np.zeros(length, dtype=int) y[original_sequence] = 1 yp = np.zeros(length, dtype=int) yp[predicted_sequence] = 1 plt.plot(x, y, label=’actual_value’, color=’blue’, linestyle=’-’, linewidth=1) plt.plot(x, yp, label=’predictive_value’, color=’green’, linestyle=’-’,

<!-- b000849 | prose | pages [24] -->
↩→linewidth=1) plt.title(’Predict Turning Point-2023 Wimbledon Gentlemen\’s Single Final’) plt.show()

<!-- b000850 | furniture | pages [24] -->
关注数学模型

<!-- b000851 | furniture | pages [24] -->
2

<!-- b000852 | furniture | pages [24] -->
MATHmodels

<!-- b000853 | furniture | pages [24] -->
获取更多资讯

<!-- b000854 | furniture | pages [25] -->
Team # 2401919

<!-- b000855 | prose | pages [25] -->
Score Trend Chart.py

<!-- b000856 | prose | pages [25] -->
score1 = process(standardized_data_p1) score2 = process(standardized_data_p2) length = len(score1)

<!-- b000857 | furniture | pages [25] -->
Page 25 of 25

<!-- b000858 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000859 | prose | pages [25] -->
x = np.arange(0, length, 1) x_downsampled = x[::5] score1_downsampled = score1[::5] score2_downsampled = score2[::5] df1 = pd.DataFrame({’time’: x_downsampled, ’normalized_score’:

<!-- b000860 | prose | pages [25] -->
↩→score1_downsampled, ’score’: ’player1’}) df2 = pd.DataFrame({’time’: x_downsampled, ’normalized_score’:

<!-- b000861 | prose | pages [25] -->
↩→score2_downsampled, ’score’: ’player2’}) df = pd.concat([df1, df2]) sns.set_theme(style="darkgrid") sns.lineplot(x=’time’, y=’normalized_score’, hue=’score’, palette=[’blue’, ’

<!-- b000862 | prose | pages [25] -->
↩→green’], linewidth=1, data=df) plt.title("Score Trend Chart", pad=10) plt.show()

<!-- b000863 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000864 | prose | pages [25] -->
Necessary Statistical Tests.py

<!-- b000865 | prose | pages [25] -->
def kmo_test(data):

<!-- b000866 | prose | pages [25] -->
X = np.corrcoef(data, rowvar=False) iX = np.linalg.inv(X) S2 = np.diag(np.diag(np.linalg.inv(iX))) AIS = np.dot(np.dot(S2, iX), S2) IS = X + AIS - 2 * S2 Dai = np.diag(np.diag(np.sqrt(AIS))) IR = np.dot(np.dot(np.linalg.inv(Dai), IS), np.linalg.inv(Dai)) AIR = np.dot(np.dot(np.linalg.inv(Dai), AIS), np.linalg.inv(Dai)) a = np.sum((AIR - np.diag(np.diag(AIR))) ** 2) AA = np.sum(a) b = np.sum((X - np.eye(X.shape[0])) ** 2) BB = np.sum(b) kmo_statistic = BB / (AA + BB) return kmo_statistic

<!-- b000867 | prose | pages [25] -->
def bartlett_test(data):

<!-- b000868 | prose | pages [25] -->
sample, variable = data.shape data_corr = np.corrcoef(data, rowvar=False) data_det = np.linalg.det(data_corr) chi2_statistic = -(sample - 1 - (2 * variable + 5) / 6) * np.log(data_det) df = variable * (variable - 1) // 2 p_value = 1 - chi2.cdf(chi2_statistic, df) return chi2_statistic, df, p_value

<!-- b000869 | prose | pages [25] -->
def test_randomness(time_series):

<!-- b000870 | prose | pages [25] -->
df = acorr_ljungbox(time_series, lags=[20], return_df=True, boxpierce=True

<!-- b000871 | prose | pages [25] -->
↩→) fig, axs = plt.subplots(2, 1, figsize=(10, 8)) plot_acf(time_series, lags=20, alpha=0.05, ax=axs[0]) plot_pacf(time_series, lags=20, alpha=0.05, ax=axs[1]) plt.show()

<!-- b000872 | furniture | pages [25] -->
关注数学模型

<!-- b000873 | furniture | pages [25] -->
2

<!-- b000874 | furniture | pages [25] -->
MATHmodels

<!-- b000875 | furniture | pages [25] -->
获取更多资讯

<!-- b000876 | furniture | pages [26] -->
Team # 2401919

<!-- b000877 | prose | pages [26] -->
Page 26

<!-- b000878 | heading | pages [26] -->
Report on Use of AI

<!-- b000879 | heading | pages [26] -->
1. OpenAI ChatGPT 3.5

<!-- b000880 | prose | pages [26] -->
微信公众号：数学模型

<!-- b000881 | prose | pages [26] -->
Query1: How do you define "momentum" in tennis? Output: In tennis, “momentum” refers to the psychological and emotional shift in a match that occurs when a player starts performing well and gaining confidence. It involves a player’s ability to maintain control over the match, dominate their opponent, and win crucial points.

<!-- b000882 | prose | pages [26] -->
Momentum can be seen as a positive flow or energy that a player experiences when they string together a series of winning points or games. It often leads to increased confidence, motivation, and focus, while simultaneously affecting the mental state of the opponent.

<!-- b000883 | prose | pages [26] -->
When a player has momentum, they often appear to be in control of the match, making fewer

<!-- b000884 | prose | pages [26] -->
errors, and executing their shots effectively. The player may exhibit a higher level of intensity, aggression, and determination. Momentum can shift back and forth between players during a match and can be influenced by factors such as winning a crucial game, making a spectacular

<!-- b000885 | prose | pages [26] -->
微信号：MATHmodels

<!-- b000886 | prose | pages [26] -->
shot, or receiving support from the crowd.

<!-- b000887 | prose | pages [26] -->
The concept of momentum in tennis is subjective and intangible, but it can play a significant role in determining the outcome of a match. Players and commentators often refer to momentum as a crucial factor that can decide the winner, as it can have a psychological impact on both players, affecting their performance and decision-making abilities.

<!-- b000888 | heading | pages [26] -->
2. OpenAI ChatGPT 3.5

<!-- b000889 | prose | pages [26] -->
Query1: How can I read and save a .csv file with different data types? Please write me a demo with Python. Output: Sure, you can use the ‘pandas‘ library in Python to read and save CSV files with different types of data. Here’s a simple demo:

<!-- b000890 | prose | pages [26] -->
‘‘‘python import pandas as pd

<!-- b000891 | prose | pages [26] -->
# Create a sample DataFrame with different types of data data = {

<!-- b000892 | prose | pages [26] -->
’Name’: [’John’, ’Alice’, ’Bob’], ’Age’: [25, 30, 35], ’Height’: [5.8, 5.5, 6.0], ’IsStudent’: [True, False, True] }

<!-- b000893 | prose | pages [26] -->
df = pd.DataFrame(data)

<!-- b000894 | prose | pages [26] -->
# Display the DataFrame print("Original DataFrame:") print(df)

<!-- b000895 | prose | pages [26] -->
# Save the DataFrame to a CSV file df.to_csv(’sample.csv’, index=False)

<!-- b000896 | prose | pages [26] -->
# Read the CSV file back into a DataFrame df_read = pd.read_csv(’sample.csv’)

<!-- b000897 | furniture | pages [26] -->
关注数学模型

<!-- b000898 | furniture | pages [26] -->
2

<!-- b000899 | furniture | pages [26] -->
MATHmodels

<!-- b000900 | furniture | pages [26] -->
获取更多资讯

<!-- b000901 | furniture | pages [27] -->
Team # 2401919

<!-- b000902 | prose | pages [27] -->
# Display the re-imported DataFrame print("\nDataFrame read from CSV:") print(df_read)

<!-- b000903 | prose | pages [27] -->
Page 27

<!-- b000904 | prose | pages [27] -->
微信公众号：数学模型

<!-- b000905 | prose | pages [27] -->
‘‘‘

<!-- b000906 | prose | pages [27] -->
This script creates a DataFrame with columns of different data types, saves it to a CSV file, and then reads it back into another DataFrame. The ‘index=False‘ argument in ‘to_csv‘ function call is used to avoid writing row indices to the CSV file.

<!-- b000907 | heading | pages [27] -->
3. OpenAI ChatGPT 3.5

<!-- b000908 | prose | pages [27] -->
Query1: What is the difference between men’s and women’s singles tennis? Output: Men’s and women’s singles tennis refer to separate categories of singles matches played in professional and amateur tennis. The primary differences between men’s and women’s singles tennis are related to the physical and physiological characteristics of male and female players, as well as some rule variations.

<!-- b000909 | prose | pages [27] -->
微信号：MATHmodels

<!-- b000910 | prose | pages [27] -->
Match duration: Men’s matches tend to be longer in duration compared to women’s matches. This is primarily due to differences in serving speed, power, and the ability to hit winners.

<!-- b000911 | prose | pages [27] -->
Scoring format: The scoring format is the same for both men and women in terms of points, games, and sets. However, women’s matches traditionally play best-of-three sets, while men’s matches play best-of-five sets in most Grand Slam tournaments.

<!-- b000912 | prose | pages [27] -->
Serve speed and power: On average, male players have greater serve speeds and power compared to female players. This often translates into more aces and harder-hitting serves in men’s matches.

<!-- b000913 | prose | pages [27] -->
Physicality: Male players generally possess greater strength, endurance, and physicality compared to female players. This can result in more aggressive shot-making, longer rallies, and a higher intensity of play in men’s matches.

<!-- b000914 | prose | pages [27] -->
Prize money: In professional tennis, there has historically been a gap in prize money between men’s and women’s tournaments. However, in recent years, efforts have been made towards gender equality in prize money distribution.

<!-- b000915 | prose | pages [27] -->
It’s important to note that these differences are generalizations and do not apply to every individual player. There are exceptional female players who possess powerful serves and endurance, and there are male players known for their finesse and shot-making skills. Tennis is a highly individual sport, and performance in any match is influenced by various factors beyond gender.

<!-- b000916 | furniture | pages [27] -->
关注数学模型

<!-- b000917 | furniture | pages [27] -->
2

<!-- b000918 | furniture | pages [27] -->
MATHmodels

<!-- b000919 | furniture | pages [27] -->
获取更多资讯
