# P-C-2024-2401919-3f4373c1

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
Lastly, we expanded our model and applied it to other types of matches. We obtained the data from the 2023 Wimbledon Ladies’ Singles Final and used our model to predict the turning points. The results showed that the predictive performance was also remarkable, although slightly inferior to the results in the men’s matches. Thus, we concluded that the model has good generalizability, but adjustments to the indicators and relevant parameters may be necessary when applying it to different types of matches.

<!-- b000019 | prose | pages [1] -->
In addition, we perform a sensitivity analysis to evaluate the responsiveness of our model to variations in input parameters. The results demonstrate strong accuracy and robustness in handling different scenarios.

<!-- b000020 | keywords | pages [1] -->
Keywords: Momentum, PCA-TOPSIS Model, White Noise Test, Grey Prediction Model, ACF&PACF

<!-- b000021 | furniture | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team # 2401919

<!-- b000026 | furniture | pages [2] -->
Page 2 of 25

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1 Introduction

<!-- b000029 | contents | pages [2] -->
3

<!-- b000030 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000031 | contents | pages [2] -->
1.1

<!-- b000032 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
3

<!-- b000034 | contents | pages [2] -->
1.2

<!-- b000035 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
4

<!-- b000037 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000038 | contents | pages [2] -->
4

<!-- b000039 | contents | pages [2] -->
2.1

<!-- b000040 | contents | pages [2] -->
Assumptions

<!-- b000041 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
4

<!-- b000043 | contents | pages [2] -->
2.2

<!-- b000044 | contents | pages [2] -->
Notations

<!-- b000045 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
5

<!-- b000047 | contents | pages [2] -->
2.3

<!-- b000048 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
6

<!-- b000050 | contents | pages [2] -->
2.3.1

<!-- b000051 | contents | pages [2] -->
Missing and Abnormal Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
6

<!-- b000053 | contents | pages [2] -->
2.3.2

<!-- b000054 | contents | pages [2] -->
Different Types of Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
6

<!-- b000056 | contents | pages [2] -->
3 TASK1&2: Point-tracking Evaluation PCA-TOPSIS Model

<!-- b000057 | contents | pages [2] -->
6

<!-- b000058 | contents | pages [2] -->
3.1

<!-- b000059 | contents | pages [2] -->
The Structure of PCA-TOPSIS Model

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
6

<!-- b000062 | contents | pages [2] -->
3.2

<!-- b000063 | contents | pages [2] -->
Select and Process Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
7

<!-- b000065 | contents | pages [2] -->
3.2.1

<!-- b000066 | contents | pages [2] -->
Select Appropriate Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
7

<!-- b000068 | contents | pages [2] -->
3.2.2

<!-- b000069 | contents | pages [2] -->
Data Dimensionless Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
8

<!-- b000071 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000072 | contents | pages [2] -->
3.3

<!-- b000073 | contents | pages [2] -->
Determine Components and Weights . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
9

<!-- b000075 | contents | pages [2] -->
3.4

<!-- b000076 | contents | pages [2] -->
Obtain the Scores and Visualization

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
11

<!-- b000079 | contents | pages [2] -->
4 Task3: The White Noise Tests for Our Model

<!-- b000080 | contents | pages [2] -->
12

<!-- b000081 | contents | pages [2] -->
4.1

<!-- b000082 | contents | pages [2] -->
White Noise Sequence

<!-- b000083 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
12

<!-- b000085 | contents | pages [2] -->
4.2

<!-- b000086 | contents | pages [2] -->
Autocorrelation Graph and Partial Autocorrelation Graph Test

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
12

<!-- b000089 | contents | pages [2] -->
4.3

<!-- b000090 | contents | pages [2] -->
Ljung-Box Test and Box-Pierce Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
13

<!-- b000092 | contents | pages [2] -->
4.4

<!-- b000093 | contents | pages [2] -->
Complete Results and Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
14

<!-- b000095 | contents | pages [2] -->
5 Task4: Momentum Swings GM(1,1) Grey Prediction Model

<!-- b000096 | contents | pages [2] -->
15

<!-- b000097 | contents | pages [2] -->
5.1

<!-- b000098 | contents | pages [2] -->
Data Processing and Examination

<!-- b000099 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
15

<!-- b000101 | contents | pages [2] -->
5.1.1

<!-- b000102 | contents | pages [2] -->
Construction of New Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
15

<!-- b000104 | contents | pages [2] -->
5.1.2

<!-- b000105 | contents | pages [2] -->
Level Comparison Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
15

<!-- b000107 | contents | pages [2] -->
5.2

<!-- b000108 | contents | pages [2] -->
Utilize the Model to Obtain the Predicted Values

<!-- b000109 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [2] -->
15

<!-- b000111 | contents | pages [2] -->
5.2.1

<!-- b000112 | contents | pages [2] -->
Build Momentum Swings Grey Forecasting Model

<!-- b000113 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000114 | contents | pages [2] -->
15

<!-- b000115 | contents | pages [2] -->
5.3

<!-- b000116 | contents | pages [2] -->
Model Diagnosis

<!-- b000117 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000118 | contents | pages [2] -->
16

<!-- b000119 | contents | pages [2] -->
6 Task5: Quantify the Impact of Different Factors on the Swings

<!-- b000120 | contents | pages [2] -->
17

<!-- b000121 | contents | pages [2] -->
6.1

<!-- b000122 | contents | pages [2] -->
Gray Relational Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
17

<!-- b000124 | contents | pages [2] -->
6.2

<!-- b000125 | contents | pages [2] -->
Advice to a Player Going into a New Match . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000126 | contents | pages [2] -->
18

<!-- b000127 | contents | pages [2] -->
7 Task6: Test the Accuracy of the Prediction Model

<!-- b000128 | contents | pages [2] -->
18

<!-- b000129 | contents | pages [2] -->
8 Task7: Generalize the Model Applicable to Other Matches

<!-- b000130 | contents | pages [2] -->
19

<!-- b000131 | contents | pages [2] -->
9 Sensitivity Analysis

<!-- b000132 | contents | pages [2] -->
21

<!-- b000133 | contents | pages [2] -->
10 Model Assessment

<!-- b000134 | contents | pages [2] -->
21

<!-- b000135 | contents | pages [2] -->
10.1

<!-- b000136 | contents | pages [2] -->
Strengths

<!-- b000137 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000138 | contents | pages [2] -->
21

<!-- b000139 | contents | pages [2] -->
10.2

<!-- b000140 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000141 | contents | pages [2] -->
21

<!-- b000142 | contents | pages [2] -->
11 Letter

<!-- b000143 | contents | pages [2] -->
22

<!-- b000144 | contents | pages [2] -->
Appendices

<!-- b000145 | contents | pages [2] -->
23

<!-- b000146 | contents | pages [2] -->
Appendix A

<!-- b000147 | contents | pages [2] -->
Evaluation Criteria

<!-- b000148 | contents | pages [2] -->
23

<!-- b000149 | contents | pages [2] -->
Appendix B

<!-- b000150 | contents | pages [2] -->
Code

<!-- b000151 | contents | pages [2] -->
24

<!-- b000152 | furniture | pages [2] -->
关注数学模型

<!-- b000153 | furniture | pages [2] -->
2

<!-- b000154 | furniture | pages [2] -->
MATHmodels

<!-- b000155 | furniture | pages [2] -->
获取更多资讯

<!-- b000156 | furniture | pages [3] -->
Team # 2401919

<!-- b000157 | furniture | pages [3] -->
Page 3 of 25

<!-- b000158 | heading | pages [3] -->
1 Introduction

<!-- b000159 | heading | pages [3] -->
1.1 Problem Background

<!-- b000160 | prose | pages [3] -->
微信公众号：数学模型 Tennis is a highly competitive and technically demanding sport that enjoys widespread popularity. In men’s singles tennis matches, the outcome is determined by a best-of-five sets format (the first player to win three sets is the winner). Each set is made up of multiple games, with the objective being to win six games and lead the opponent by at least two games. If the score reaches 6-6, a tiebreaker is played to determine the winner of that set. In a tiebreaker, the first player to reach seven points with a minimum lead of two points secures the set victory. However, in the fifth set, the tiebreaker changes to a first-to-ten-points format. Within each game, players strive to win at least four points, but they must secure victory with a two-point advantage.

<!-- b000161 | prose | pages [3] -->
In tennis matches, the situation often changes in the blink of an eye. This exhilarating sport is a blend of tactics and skills, where every serve, return, or shot can alter the course of the game. Sometimes we witness one player’s unstoppable momentum, swiftly securing victory. Other times, 微信号：MATHmodels we see intense battles where both sides fiercely compete, experiencing numerous lead changes and comebacks before determining a winner, like the duel between Carlos Alcaraz and Novak Djokovic in the 2023 Wimbledon final.

<!-- b000162 | prose | pages [3] -->
Jannik Sinner Carlos Alcaraz 2023 Wimbledon Gentlemen’s Singles 3:1 3:1 Carlos Alcaraz Jannik Sinner Nicolas Jarry Quentin Halys Carlos Alcaraz Jannik Sinner 3:0 3:1 Alexander Zverev Daniel Elahi Matteo Berrettini Daniel Elahi 0:3 3:2 Matteo Berrettini Mikael Ymer Carlos Alcaraz Jannik Sinner 3:0 3:1 Frances Tiafoe Guido Pella Grigor Dimitrov Roman Safiullin 0:3 0:3 Grigor Dimitrov Roman Safiullin Roman Safiullin Holger Rune 1:3 3:1 0 3 Alejandro Davidovich Denis Shapovalov Holger Rune Denis Shapovalov 2:3 3:1 : Novak Djokovic Carlos Alcaraz : Holger Rune Liam Broady 3 Daniil Medvedev Andrey Rublev 0 Daniil Medvedev Andrey Rublev 3:1 3:1 3:2 Marton Fucsovics David Goffin Daniil Medvedev Andrey Rublev 2:0 3:2 Jiri Lehecka Alexander Bublik Jiri Lehecka Alexander Bublik 3:2 3:0 Novak Djokovic Tommy Paul Maximilian Marterer Daniil Medvedev 3:2 1:3 Christopher Eubanks Lorenzo Musetti Christopher Hubert Hurkacz 3:0 0:3 Eubanks Christopher Hubert Hurkacz Christopher O'Connell Novak Djokovic 3:2 1:3 Eubanks Laslo Djere Stan Wawrinka Stefanos Tsitsipas Novak Djokovic 0:3 0:3 Stefanos Tsitsipas Novak Djokovic

<!-- b000163 | caption | pages [3] -->
Figure 1: 2023 Wimbledon Gentlemen’s Singles

<!-- b000164 | prose | pages [3] -->
The dynamics and trajectory of a match, including astonishing turnarounds, can be attributed to the players’ “momentum”. Momentum has always been emphasized, but quantifying and proving its true impact on the game, as well as identifying the factors that generate and shift momentum, is challenging. To better assist players in achieving success, we will delve into these aspects, providing coaches with advice on helping players prepare for and respond to game-altering events, fully harnessing the power of momentum. Specifically, we will utilize the provided data to carry out the following tasks:

<!-- b000165 | prose | pages [3] -->
1. Present the changing trends of match results over time.

<!-- b000166 | prose | pages [3] -->
2. Evaluate the performance of players at a specific moment.

<!-- b000167 | furniture | pages [3] -->
关注数学模型

<!-- b000168 | furniture | pages [3] -->
2

<!-- b000169 | furniture | pages [3] -->
MATHmodels

<!-- b000170 | furniture | pages [3] -->
获取更多资讯

<!-- b000171 | furniture | pages [4] -->
Team # 2401919

<!-- b000172 | furniture | pages [4] -->
Page 4 of 25

<!-- b000173 | prose | pages [4] -->
3. Verify if swings in momentum in a match are random.

<!-- b000174 | prose | pages [4] -->
4. Establish a prediction model to forecast shifts in the game situation.

<!-- b000175 | prose | pages [4] -->
5. Evaluate factors influencing the swings and provide players with recommendations. 微信公众号：数学模型 6. Validate the accuracy of the prediction model in actual matches and optimize them.

<!-- b000176 | prose | pages [4] -->
7. Expand the model to other types of matches.

<!-- b000177 | heading | pages [4] -->
1.2 Our Work

<!-- b000178 | prose | pages [4] -->
To explore the role and influence of “momentum” in tennis matches, we selected different indicators from game data for quantification and analysis. In the first question, we constructed a PCA-TOPSIS model and selected 18 indicators to evaluate player performance and determine their weights. In the second question, we conducted a white noise test on the model results, proving that changes in game momentum are not random and refuting the coach’s viewpoint. In the third question, we further constructed a GM(1, 1) gray prediction model to forecast turning points in the 微信号：MATHmodels game and determined the factor with the highest correlation coefficient with momentum shifts. In the fourth question, we compared the model with real game data to test its accuracy and extended its application to other matches, making it more widely applicable. Lastly, we test the PCA-TOPSIS model’s sensitivity.The overview of our work is shown in Figure 2.

<!-- b000179 | prose | pages [4] -->
White Noise Tests Nonrandomness

<!-- b000180 | prose | pages [4] -->
Players’ PCA-TOPSIS Data Reprocessing Scores

<!-- b000181 | heading | pages [4] -->
Model

<!-- b000182 | prose | pages [4] -->
Given Data Swing GM(1,1) Grey Point

<!-- b000183 | heading | pages [4] -->
Prediction Model

<!-- b000184 | prose | pages [4] -->
Most Related Test the Expand to Factor Accuracy Other Matches

<!-- b000185 | caption | pages [4] -->
Figure 2: Overview of Our Work

<!-- b000186 | heading | pages [4] -->
2 Preparation of the Models

<!-- b000187 | heading | pages [4] -->
2.1 Assumptions

<!-- b000188 | prose | pages [4] -->
The following reasonable assumptions can be made in this paper:

<!-- b000189 | prose | pages [4, 5] -->
• The players are in a normal physiological, physical and mental state, without any severe injuries or using banned substances.

<!-- b000190 | furniture | pages [4] -->
关注数学模型

<!-- b000191 | furniture | pages [4] -->
2

<!-- b000192 | furniture | pages [4] -->
MATHmodels

<!-- b000193 | furniture | pages [4] -->
获取更多资讯

<!-- b000194 | furniture | pages [5] -->
Team # 2401919

<!-- b000195 | furniture | pages [5] -->
Page 5 of 25

<!-- b000197 | prose | pages [5] -->
• The players did not engage in any match-fixing or similar activities during the competition.

<!-- b000198 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000199 | prose | pages [5] -->
• The recording of the values for each player at every moment is accurate, fair, and in accordance with the rules of the competition.

<!-- b000200 | prose | pages [5] -->
• The performance of the players on the field is rarely affected by the conditions of the venue, weather, or the atmosphere of the audience.

<!-- b000201 | prose | pages [5] -->
• The performance of each player in this game is rarely affected by the results of previous matches, instead concentrating on the current match.

<!-- b000202 | heading | pages [5] -->
2.2 Notations

<!-- b000203 | prose | pages [5] -->
In our paper, we have adopted the nomenclature presented in Table 1 for model construction. Any additional symbol which is not frequently used will be introduced once they are utilized in the 微信号：MATHmodels following text. All variables are targeted at a certain set, and the training data for the model also includes data of an entire set. In particular, "so far" and "accumulative" means cumulative value since the very beginning of current set. Definitions without these words means value at current moment.

<!-- b000204 | caption | pages [5] -->
Table 1: Symbols and Definitions

<!-- b000205 | prose | pages [5] -->
Symbol Definition 𝑆𝑖 Number of sets won by player 𝑖 𝐺𝑖 Number of games won by player 𝑖 𝑃𝑖 Number of points won by player 𝑖 𝐴𝑖 Number of untouchable winning serves hit by player 𝑖so far 𝐵𝑖 Player 𝑖’s break point conversion rate so far 𝑁𝑖 Player 𝑖’s net point winning rate so far 𝐹𝑆𝑢𝑖 Player 𝑖’s first serve success rate so far 𝐹𝑆𝑐𝑖 Player 𝑖’s first serve score rate so far 𝑆𝑆𝑐𝑖 Player 𝑖’s second serve score rate so far 𝑅𝑆𝑐𝑖 Player 𝑖’s return score rate so far 𝐷𝐹𝑖 Number of double faults made by player 𝑖so far 𝑈𝐸𝑖 Number of unforced errors made by player 𝑖so far 𝐷𝑖 Player 𝑖’s distance ran during point 𝑉𝑖 Player 𝑖’s speed of serve 𝑆𝑊𝑖 Player 𝑖’s direction of serve 𝑆𝐷𝑖 Player 𝑖’s depth of serve 𝑅𝐷𝑖 Player 𝑖’s depth of return 𝑆𝐶𝑖 Player 𝑖’s accumulative serve count △𝑀 Momentum score difference between two players.

<!-- b000206 | prose | pages [5] -->
𝑖= 1, 2

<!-- b000207 | furniture | pages [5] -->
关注数学模型

<!-- b000208 | furniture | pages [5] -->
2

<!-- b000209 | furniture | pages [5] -->
MATHmodels

<!-- b000210 | furniture | pages [5] -->
获取更多资讯

<!-- b000211 | furniture | pages [6] -->
Team # 2401919

<!-- b000212 | furniture | pages [6] -->
Page 6 of 25

<!-- b000213 | heading | pages [6] -->
2.3 Data Cleaning

<!-- b000214 | heading | pages [6] -->
2.3.1 Missing and Abnormal Data

<!-- b000215 | prose | pages [6] -->
微信公众号：数学模型 We have observed some missing data in speed_mph, serve_width, serve_depth, and return_depth variables, which is presented as "NA". Considering the continuous nature of the game process, we will not remove entire rows of data. Instead, the missing values in speed_mph will be replaced with the average value. As for serve_width, serve_depth, and return_depth variables, the missing values will be assigned as 0.

<!-- b000216 | heading | pages [6] -->
2.3.2 Different Types of Data

<!-- b000217 | prose | pages [6] -->
(1) Data Accumulation in Numerical data For some numerical data in categorical form, they have only two values: 0 and 1. During calculations, an excess of 0s can result in "nan" errors, preventing further computation. To address this, the values will be accumulated. To eliminate the impact of accumulation, they will subsequently be decremented.

<!-- b000218 | prose | pages [6] -->
微信号：MATHmodels (2) Data Mapping in Non-numeric Data For the non-numerical variables serve_width, serve_depth, and return_depth, we will map them to numbers after rigorous judgements.

<!-- b000219 | prose | pages [6] -->
• serve_width: C=1, BC=2, B=3, BW=4, W=5

<!-- b000220 | prose | pages [6] -->
• serve_depth: NCTL=1, CTL=2

<!-- b000221 | prose | pages [6] -->
• return_depth: ND=1, D=2

<!-- b000222 | heading | pages [6] -->
3 TASK1&2: Point-tracking Evaluation PCA-TOPSIS Model

<!-- b000223 | heading | pages [6] -->
3.1 The Structure of PCA-TOPSIS Model

<!-- b000224 | prose | pages [6] -->
In this section, we need to select specific indicators to track the progress of each match point and the performance of players. The traditional TOPSIS analysis method relies heavily on subjective weighting of indicators, which can significantly influence the results. Therefore, we introduce the relatively objective method, Principal Component Analysis (PCA), to analyze the dataset and reduce dimensionality. Subsequently, we determine the weights for each indicator and rank the proximity of the evaluated objects’ numerical distance to the ideal target. This novel PCA-TOPSIS model combines the advantages of both models and enables more accurate tracking of the players’ performance at each match point.The structure of our idea can be illustrated by Figure 3.

<!-- b000225 | prose | pages [6] -->
What’s more, each player has significant variations in their playing style, personal level, and other individual factors. Additionally, each game is influenced by multiple complex factors and is subject to frequent changes. Therefore, instead of analyzing the performance of all players in all games using the same model, we choose to build separate models for the performance of each player in each game. This approach provides greater accuracy and relevance.

<!-- b000226 | furniture | pages [6] -->
关注数学模型

<!-- b000227 | furniture | pages [6] -->
2

<!-- b000228 | furniture | pages [6] -->
MATHmodels

<!-- b000229 | furniture | pages [6] -->
获取更多资讯

<!-- b000230 | furniture | pages [7] -->
Team # 2401919

<!-- b000231 | furniture | pages [7] -->
Page 7 of 25

<!-- b000232 | prose | pages [7] -->
Collect the raw data for selected indicators

<!-- b000233 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000234 | heading | pages [7] -->
Data processing: dimensionless processing

<!-- b000235 | prose | pages [7] -->
Compute the correlation matrix, eigenvalues, and variance contribution rate.

<!-- b000236 | prose | pages [7] -->
Determine the principal components and weights

<!-- b000237 | prose | pages [7] -->
Obtain the comprehensive evaluation results.

<!-- b000238 | caption | pages [7] -->
Figure 3: Schematic of PCA-TOPSIS Model

<!-- b000239 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000240 | heading | pages [7] -->
3.2 Select and Process Indicators

<!-- b000241 | heading | pages [7] -->
3.2.1 Select Appropriate Indicators

<!-- b000242 | prose | pages [7] -->
To evaluate the performance of athletes on the field, we have developed a performance assessment system consisting of five aspects: current situation, offensive effectiveness, error situation, technical fitness, and starting advantage. Each first-level indicator is divided into many second-level indicators. As shown in Figure 4 below.

<!-- b000243 | prose | pages [7] -->
NP rate Return depth RP rate

<!-- b000244 | prose | pages [7] -->
Technical RP rate Offensive Running distance Fitness Effectiveness FSU rate Starting Serve direction Advantage Sets won Error Current Situation Sets won Situation Accumulative Double fault serves Unforced number error number Points won

<!-- b000245 | caption | pages [7] -->
Figure 4: Performance Assessment System

<!-- b000246 | prose | pages [7, 8] -->
(1) Current Situation The current situation refers to the on-court position of the athlete up until the present moment, reflecting their scoring breakthrough ability within a certain timeframe. In this regard, we have selected cumulative sets won, cumulative games won, and cumulative points won as secondary indicators, which respectively reflect the athlete’s scoring ability, game breakthrough capability, and set breakthrough capability within a certain timeframe.

<!-- b000247 | furniture | pages [7] -->
关注数学模型

<!-- b000248 | furniture | pages [7] -->
2

<!-- b000249 | furniture | pages [7] -->
MATHmodels

<!-- b000250 | furniture | pages [7] -->
获取更多资讯

<!-- b000251 | furniture | pages [8] -->
Team # 2401919

<!-- b000252 | furniture | pages [8] -->
Page 8 of 25

<!-- b000254 | prose | pages [8] -->
(2) Offensive Effectiveness Offensive efficiency refers to the practical effectiveness of the 微信公众号：数学模型 athlete’s various technical actions on the court in scoring, reflecting their efficiency and capability in offensive breakthroughs. In this aspect, we have selected ACE count, BP rate (break point conversion rate) , NP rate (net points won rate), FSU rate (first serve success rate) , FSC rate (first serve points won rate) , SSC rate (second serve points won rate), and RP rate (return points won rate) as secondary indicators, all of which are accumulated data within a certain timeframe.

<!-- b000255 | prose | pages [8] -->
(3) Error Situation Error situations refer to the occurrence of various mistakes by the athlete on the court, reflecting the stability of their performance in critical moments. In this aspect, we have selected double faults count and unforced error count as secondary indicators, both of which are accumulated data within a certain timeframe.

<!-- b000256 | prose | pages [8] -->
Among these, double faults count reflects the athlete’s serving stability and their ability to capitalize on the advantage of serving first; unforced error count reflects their technical stability. 微信号：MATHmodels (4) Technical Fitness Technical and physical abilities refer to the athlete’s physical condition and technical choices displayed on the court, reflecting their level of physical fitness and tactical strategy selection. In this aspect, we have selected running distance, serving speed, serving depth, serving direction, and return depth as secondary indicators, all of which are data at the current moment.

<!-- b000257 | prose | pages [8] -->
Among these, running distance reflects the athlete’s physical condition, mobility, and intensity, while also reflecting their running level and tactical choices; serving speed, serving depth, and serving direction reflect their serving technique level and tactical choices; return depth reflects their return technique and tactical choices.

<!-- b000258 | prose | pages [8] -->
(5) Starting Advantage Serving advantage refers to the relative advantage the athlete possesses as the server, which influences their on-court performance in terms of psychology, match state, and offensive opportunities, among other aspects. In this aspect, we have selected the number of serves as a secondary indicator.

<!-- b000259 | prose | pages [8] -->
The number of serves represents the accumulated number of serves by the athlete within a certain timeframe. This indicator is used to offset the advantage the athlete has as the server in terms of scoring and offense, in order to obtain a more accurate on-court performance evaluation.

<!-- b000260 | heading | pages [8] -->
3.2.2 Data Dimensionless Process

<!-- b000261 | prose | pages [8] -->
Dimensionalization refers to the process of removing the dimensionality of different indicators, which makes them incomparable due to the different units of measurement. Therefore, it is necessary to normalize the data first in order to eliminate the dimensional influence. This is done by transforming the original variables to eliminate the influence of their units of measurement, enabling subsequent analysis. In this case, we choose the standardization method to normalize the data, which transforms the values of all indicators to have a mean of 0 and a variance of 1. The formula below takes 𝑆𝑖as an example while 𝑡means sample point in this time series.

<!-- b000262 | prose | pages [8] -->
𝑖= 𝑆𝑖,𝑡−𝜇(𝑆𝑖) 𝑆∗ 𝑖= 1, 2 (1) 𝜎(𝑆𝑖)

<!-- b000263 | furniture | pages [8] -->
关注数学模型

<!-- b000264 | furniture | pages [8] -->
2

<!-- b000265 | furniture | pages [8] -->
MATHmodels

<!-- b000266 | furniture | pages [8] -->
获取更多资讯

<!-- b000267 | furniture | pages [9] -->
Team # 2401919

<!-- b000268 | furniture | pages [9] -->
Page 9 of 25

<!-- b000269 | heading | pages [9] -->
3.3 Determine Components and Weights

<!-- b000270 | prose | pages [9] -->
After obtaining standardized data for each indicator, we calculate the covariance and correlation matrix among the variables. Taking 𝑆𝑖and 𝐺𝑗for example, the calculation formula is shown below. 微信公众号：数学模型 𝐶𝑜𝑣(𝑆∗ 𝑖, 𝐺∗ 𝑗) 𝑅𝑆∗ 𝑖, 𝑗∈{1, 2} 𝑗= (2) 𝑖,𝐺∗ √︃ 𝑉𝑎𝑟(𝑆∗ 𝑖) · 𝑉𝑎𝑟(𝐺∗ 𝑗)

<!-- b000271 | prose | pages [9] -->
The heat map of the correlation coefficient matrix containing all variables is shown in Figure 5. We could clearly see that there is a strong positive correlation between 𝑉1 and 𝐹𝑆𝑢1, the same as the common sense, the faster your serve speed, the more likely you will get your first serve success. We could also see that there is a strong negative correlation between 𝐷𝐹1,𝑈𝐸1 and 𝑆1, 𝐺1, 𝑃1, which is also intuitive. The more double faults and unforced errors you commit, the less likely you will win, to name but a few.

<!-- b000272 | prose | pages [9] -->
微信号：MATHmodels Correlation Coefficient Matrix Heat Map

<!-- b000273 | prose | pages [9] -->
SC2 RD2 SD2 SW2 V2 D2 UE2 DF2 RSc2 SSc2 FSc2 FSu2 N2 B2 A2 Legend P2 0.8 G2 0.4 S2 SC1 0.0 RD1 0.4 SD1 0.8 SW1 V1 D1 UE1 DF1 RSc1 SSc1 FSc1 FSu1 N1 B1 A1 P1 G1 S1

<!-- b000274 | prose | pages [9] -->
S1 G1 P1 A1 B1 N1 FSu1 FSc1 SSc1 RSc1 DF1 UE1 D1 V1 SW1 SD1 RD1 SC1 S2 G2 P2 A2 B2 N2 FSu2 FSc2 SSc2 RSc2 DF2 UE2 D2 V2 SW2 SD2 RD2 SC2

<!-- b000275 | caption | pages [9] -->
Figure 5: Heat Map of Correlation

<!-- b000276 | prose | pages [9] -->
According to the characteristic equation |𝑅−𝜆𝐼| = 0, the eigenvalues 𝜆𝑘(𝑘= 1, 2, 3...18) are computed. The eigenvalue contribution rate and cumulative contribution rate are represented by formulas (3) and (4) respectively.

<!-- b000277 | prose | pages [9, 10] -->
𝜆𝑘 𝑇𝑘= (3) Í𝑝 𝑗=1 𝜆𝑗 Í𝑘 𝑖=1 𝜆𝑖 𝐷𝑘= (4) Í𝑝 𝑗=1 𝜆𝑗

<!-- b000278 | furniture | pages [9] -->
关注数学模型

<!-- b000279 | furniture | pages [9] -->
2

<!-- b000280 | furniture | pages [9] -->
MATHmodels

<!-- b000281 | furniture | pages [9] -->
获取更多资讯

<!-- b000282 | furniture | pages [10] -->
Team # 2401919

<!-- b000283 | furniture | pages [10] -->
Page 10 of 25

<!-- b000285 | prose | pages [10] -->
Specifically, 𝑝in the formula means the number of principal components, in our paper 𝑝equals 微信公众号：数学模型 to 18. We select the six largest eigenvalues corresponding to the cumulative contribution rate 𝐷𝑘⩾85% as the principal components. The information contribution rate and the cumulative contribution rate of each principal components is shown in Table 2.

<!-- b000286 | caption | pages [10] -->
Table 2: Contribution Rate of Principal Components

<!-- b000287 | prose | pages [10] -->
Component Information Contribution Rate Cumulative Contribution Rate 1 39.10% 39.10% 2 16.26% 55.36% 3 13.58% 68.93% 4 6.89% 75.82% 5 5.56% 81.38% 6 5.27% 86.65% 7 3.63% 90.28% 8 3.18% 93.46% 微信号：MATHmodels 9 2.01% 95.47% 10 1.35% 96.82% 11 1.27% 98.09% 12 0.87% 98.89% 13 0.52% 99.41% 14 0.25% 99.66% 15 0.15% 99.81% 16 0.08% 99.89% 17 0.05% 99.94% 18 0.01% 100%

<!-- b000288 | prose | pages [10] -->
After calculation, the eigenvectors of the sixth largest eigenvalues are shown in Figure 6.

<!-- b000289 | prose | pages [10] -->
Indicator 1 2 3 4 5 6 S 0.3141 0.1361 0.3539 0.3303 -0.2017 0.2687 G -0.2509 0.1995 -0.1737 -0.2051 0.2341 0.1327 P 0.0147 0.1237 0.0459 0.0309 0.4024 0.0991 A 0.2498 -0.6152 0.0717 0.0375 0.1913 -0.3198 B 0.0556 -0.0314 0.0653 0.1136 -0.1435 -0.2424 N 0.0272 -0.0813 0.06 0.1624 0.1308 -0.2495 FSu 0.1029 -0.6193 -0.0975 -0.2994 0.0929 0.3146 FSc 0.1479 -0.2073 0.0213 0.0223 0.1766 0.2622 SSc 0.0546 0.0876 0.0083 -0.13 0.0613 -0.5214 RSc 0.1159 0.0673 0.0759 0.0089 -0.0045 -0.4324 DF -0.037 -0.0305 -0.041 -0.0521 0.0149 0.0412 UE -0.1677 0.0011 -0.0972 0.1041 -0.0617 0.136 D -0.5621 -0.1858 -0.1521 -0.1191 0.0042 -0.1685 V -0.286 -0.2102 -0.2053 0.809 -0.5104 0.0083 SW 0.2692 0.0876 -0.8185 0.0404 -0.2919 -0.0345 SD 0.4667 0.1195 -0.2572 0.038 0.2096 -0.0118 RD -0.0751 -0.001 0.0351 -0.1219 0.4807 -0.0239 SC 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000

<!-- b000290 | caption | pages [10] -->
Figure 6: Corresponding Eigenvectors of the First Six Largest Principal Components

<!-- b000291 | prose | pages [10] -->
The table above displays the eigenvalues of the six principal components extracted from the indicator data of Player 1 in the final matches. The six principal components have varying emphasis on each indicator, and here we will provide a detailed explanation using Player 1 as an example, with Player 2 following a similar pattern.

<!-- b000292 | furniture | pages [10] -->
关注数学模型

<!-- b000293 | furniture | pages [10] -->
2

<!-- b000294 | furniture | pages [10] -->
MATHmodels

<!-- b000295 | furniture | pages [10] -->
获取更多资讯

<!-- b000296 | furniture | pages [11] -->
Team # 2401919

<!-- b000297 | furniture | pages [11] -->
Page 11 of 25

<!-- b000298 | prose | pages [11] -->
In the first and fifth columns, the eigenvalues with larger absolute values are concentrated in the fourth aspect of the evaluation system. The two indicators with the largest absolute eigenvalues in the first column are running distance and serving depth, while the two indicators with the largest absolute eigenvalues in the fifth column are serving speed and return depth. This reflects that the 微信公众号：数学模型 emphasis of the first and fifth principal components is on the athlete’s technical and physical abilities.

<!-- b000299 | prose | pages [11] -->
In the second and sixth columns, the eigenvalues with larger absolute values are concentrated in the second aspect of the evaluation system. The two indicators with the largest absolute eigenvalues in the second column are the number of aces and first serve success rate, while the two indicators with the largest absolute eigenvalues in the sixth column are second serve points won rate and return points won rate. This reflects that the emphasis of the second and sixth principal components is on the athlete’s offensive efficiency.

<!-- b000300 | prose | pages [11] -->
In the third and fourth columns, the eigenvalues with larger absolute values are scattered in the first and fourth aspects. The two indicators with the largest absolute eigenvalues in the third column are serving direction in the fourth aspect and cumulative sets won in the first aspect, while the two 微信号：MATHmodels indicators with the largest absolute eigenvalues in the fourth column are serving speed in the fourth aspect and cumulative sets won in the first aspect. This reflects that the third and fourth principal components have a combined emphasis on the athlete’s current situation, technical and physical abilities.

<!-- b000301 | prose | pages [11] -->
We have factored the serve into our model as 𝑆𝐶𝑖, while the eigenvalues of the serve count feature in all six principal components are extremely low, indicating that the impact of the serve count on the overall evaluation system is negligible. This could be caused by that although in tennis the player serving had a much higher probability of winning the point, the two athletes take turns serving, and over time, the serve count of the two athletes tends to be equal. As a result, the role of the serve count indicator in the evaluation system in distinguishing between the two players approaches zero, and therefore, its contribution to the information is very subtle.

<!-- b000302 | prose | pages [11] -->
Therefore, we extract 6 new variables to replace the original 18 indicators. Based on the coefficients of the indicators, we obtain the principal component decision matrix.

<!-- b000303 | prose | pages [11] -->
𝑊= (𝑤𝑖𝑗) ∈R18×6 (5)

<!-- b000304 | prose | pages [11] -->
Then, we calculate the weight 𝑊𝑖of each principal component by dividing the eigenvalue 𝜆𝑖of that principal component by the sum of all eigenvalues. The weights of the principal components are identical to their information contribution rate, namely 𝑊1 = 0.3910, 𝑊2 = 0.1626, 𝑊3 = 0.1358, 𝑊4 = 0.0689, 𝑊5 = 0.0527, 𝑊6 = 0.0363.

<!-- b000305 | heading | pages [11] -->
3.4 Obtain the Scores and Visualization

<!-- b000306 | prose | pages [11] -->
We could obtain the scores simply multiply three matrices.

<!-- b000307 | prose | pages [11] -->
𝑆= 𝑍𝑊𝐼∈R𝑡×1, 𝑍∈R𝑡×𝑝, 𝑊∈R𝑝×ℎ, 𝐼∈Rℎ×1 (6)

<!-- b000308 | prose | pages [11] -->
𝑆means Score Matrix, 𝑍means Standardized Data Matrix, 𝐼means Information Contribution Rate Matrix, 𝑡means the number of time sample points, 𝑝means the number of original variables, ℎmeans the number of principal components we selected.

<!-- b000309 | furniture | pages [11] -->
关注数学模型

<!-- b000310 | furniture | pages [11] -->
2

<!-- b000311 | furniture | pages [11] -->
MATHmodels

<!-- b000312 | furniture | pages [11] -->
获取更多资讯

<!-- b000313 | furniture | pages [12] -->
Team # 2401919

<!-- b000314 | furniture | pages [12] -->
Page 12 of 25

<!-- b000315 | prose | pages [12] -->
Based on this result, we can determine the performance scores, namely "momentum" for each player in the whole match, representing the potential outcome of the game. We choose the Final between Carlos Alcaraz and Novak Djokovic for visualization, as shown in Figure 7 below.

<!-- b000316 | prose | pages [12] -->
微信公众号：数学模型 Score Trend Chart score normalized_score player1 0.5 player2 0.0

<!-- b000317 | prose | pages [12] -->
0.5

<!-- b000318 | prose | pages [12] -->
0 50 100 150 200 250 300 time

<!-- b000319 | caption | pages [12] -->
Figure 7: Score Trend Chart

<!-- b000320 | prose | pages [12] -->
微信号：MATHmodels We conduct the KMO and Bartlett’s test of sphericity on the model results. The KMO test yields a value of 0.8263, and the p-value of the Barlett’s sphericity test was less than 0.01, indicating that our analysis results are relatively reliable. Please refer to the KMO Test Evaluation Criteria in Appendix A.

<!-- b000321 | heading | pages [12] -->
4 Task3: The White Noise Tests for Our Model

<!-- b000322 | heading | pages [12] -->
4.1 White Noise Sequence

<!-- b000323 | prose | pages [12] -->
According to Wikipedia, a white noise sequence is a common random process in statistics and signal processing. It possesses specific characteristics that result in a uniform distribution of energy across all frequencies, consisting of a series of mutually independent random variables with identical probability distributions. These random variables have no correlation with each other, thus exhibiting complete temporal independence. This means that each value in the sequence is independently generated from the same probability distribution. The white noise test can be used to assess whether a stationary sequence is random before making predictions.

<!-- b000324 | prose | pages [12] -->
With an aim to confirm or falsify the coach’s conjecture, we have made a synonymous conversion, examining whether the generated time series of athlete performance scores, which could be approximately considered as explicit expression of implicit state, namely athlete’s momentum, are random sequences. Hence, we employ the white noise test to assess the randomness of fluctuations.

<!-- b000325 | heading | pages [12] -->
4.2 Autocorrelation Graph and Partial Autocorrelation Graph Test

<!-- b000326 | prose | pages [12, 13] -->
By definition, white noise is a series of independent random variables with the same distribution, uncorrelated over time, meaning each value is generated independently. Under ideal conditions, except for the zero-order autocorrelation coefficient which is 1, for all k > 0, the autocorrelation coefficient with a lag of k is expected to be 0. However, due to the finite length of the sample sequence, the autocorrelation coefficient for a lag of k is not exactly 0. Instead, values near zero are considered indicative of no autocorrelation. Due to the presence of random disturbances, the autocorrelation coefficients are not strictly equal to 0. Therefore, when the autocorrelation coefficients fall within 95% confidence interval, we deem it as a white noise sequence. If a sequence has a significant number of autocorrelation coefficients outside this range, it is likely not a white noise sequence. The following explanation will be based on the autocorrelation and partial autocorrelation graphs of player 1 in the final match to illustrate that.

<!-- b000327 | furniture | pages [12] -->
关注数学模型

<!-- b000328 | furniture | pages [12] -->
2

<!-- b000329 | furniture | pages [12] -->
MATHmodels

<!-- b000330 | furniture | pages [12] -->
获取更多资讯

<!-- b000331 | furniture | pages [13] -->
Team # 2401919

<!-- b000332 | furniture | pages [13] -->
Page 13 of 25

<!-- b000334 | prose | pages [13] -->
微信公众号：数学模型 Autocorrelation 1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00 0 5 10 15 20 Partial Autocorrelation 1.00 微信号：MATHmodels 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00 0 5 10 15 20

<!-- b000335 | caption | pages [13] -->
Figure 8: Autocorrelation Graph and Partial Autocorrelation Graph

<!-- b000336 | prose | pages [13] -->
As shown in Figure 8, on the on hand, the autocorrelation plot exhibits first-order truncation, meaning that before the autocorrelation coefficients enter the 95% confidence interval, there are first-order autocorrelation coefficient values outside the boundaries. On the other hand, the partial autocorrelation plot shows fourth-order tailing, indicating that before the partial autocorrelation coefficients enter the 95% confidence interval, there are fourth-order partial autocorrelation coefficient values outside the boundaries. Summarizing from the phenomenons above, we have reasons to preliminarily believe that the sequence is likely not a white noise sequence.

<!-- b000337 | heading | pages [13] -->
4.3 Ljung-Box Test and Box-Pierce Test

<!-- b000338 | prose | pages [13] -->
In order to perform statistical tests, we make the following assumptions：

<!-- b000339 | prose | pages [13] -->
𝐻0 : 𝜌1 = 𝜌2 = . . . = 𝜌ℎ= 0 (7)

<!-- b000340 | prose | pages [13, 14] -->
The values of the lag-h series are mutually independent, and the sequence is composed of independently and identically distributed white noise, namely the correlations in the population from which the sample is taken are 0, so that any observed correlations in the data result from randomness of the sampling process.

<!-- b000341 | furniture | pages [13] -->
关注数学模型

<!-- b000342 | furniture | pages [13] -->
2

<!-- b000343 | furniture | pages [13] -->
MATHmodels

<!-- b000344 | furniture | pages [13] -->
获取更多资讯

<!-- b000345 | furniture | pages [14] -->
Team # 2401919

<!-- b000346 | furniture | pages [14] -->
Page 14 of 25

<!-- b000348 | prose | pages [14] -->
𝐻𝑎: ∃𝜌𝑘≠0, 1 ⩽𝑘⩽ℎ (8) 微信公众号：数学模型 The values of the lag-h series are mutually correlative, and the sequence is composed of non-independently and identically distributed white noise, namely they exhibit serial correlation.

<!-- b000349 | prose | pages [14] -->
In traditional testing methods, a sample size less than 30 is considered as a small sample, on which Ljung-Box Test works better. Joel et al. pointed out that when the sample size is on the order of 500, Box-Pierce Test works better. In the 2023 Wimbledon Gentlemen’s Singles Final we used as an example, the amount of data is around 300, so we adopt both two statistics to gain a more comprehensive assessment of our model.

<!-- b000350 | prose | pages [14] -->
The test statistic in the Ljung-Box test is:

<!-- b000351 | prose | pages [14] -->
ℎ ˆ𝜌2 𝑘 ∑︁ 𝑄𝐿𝐵= 𝑛(𝑛+ 2) (9) 微信号：MATHmodels 𝑛−𝑘 𝑘=1

<!-- b000352 | prose | pages [14] -->
The test statistic in the Box-Pierce test is:

<!-- b000353 | prose | pages [14] -->
ℎ ∑︁ 𝑄𝐵𝑃= 𝑛 ˆ𝜌2 (10) 𝑘 𝑘=1

<!-- b000354 | prose | pages [14] -->
where 𝑛is the sample size, ˆ𝜌𝑘is the sample autocorrelation at lag 𝑘, and ℎis the number of lags being tested, which is set to ℎ= 20 here. For significance level 𝛼= 0.05, the critical region for rejection of the hypothesis of randomness is:

<!-- b000355 | prose | pages [14] -->
𝑄> 𝜒2 1−𝛼,ℎ⇔𝑝< 𝛼 (11)

<!-- b000356 | prose | pages [14] -->
According to the Ljung-Box test and Box-Pierce test, we have the following explanations. Results show that 𝑝𝐿𝐵= 6.645 × 10−13 and 𝑝𝐵𝑃= 2.087 × 10−12. Both the p-values from the Ljung-Box test and the Box-Pierce test are much smaller than 0.05, leading us to reject the null hypothesis. Therefore, the sequence is not a white noise sequence. This conclusion aligns with the results obtained from the autocorrelation and partial autocorrelation analysis, which both indicate that the sequence is not a random sequence.

<!-- b000357 | heading | pages [14] -->
4.4 Complete Results and Conclusions

<!-- b000358 | prose | pages [14] -->
Based on the aforementioned white noise testing methods, we conducted tests on a total of 62 sequences from 31 matches. Among them, 60 sequences were found to be non-white-noise, while only 2 sequences were identified as white noise. This indicates that the non-random sequence rate is as high as 96.78%. At this point we could overturn the coach’s statement, as the swings in play and runs of success by one player are obviously not random.

<!-- b000359 | furniture | pages [14] -->
关注数学模型

<!-- b000360 | furniture | pages [14] -->
2

<!-- b000361 | furniture | pages [14] -->
MATHmodels

<!-- b000362 | furniture | pages [14] -->
获取更多资讯

<!-- b000363 | furniture | pages [15] -->
Team # 2401919

<!-- b000364 | furniture | pages [15] -->
Page 15 of 25

<!-- b000365 | heading | pages [15] -->
5 Task4: Momentum Swings GM(1,1) Grey Prediction Model

<!-- b000366 | heading | pages [15] -->
5.1 Data Processing and Examination

<!-- b000367 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000368 | heading | pages [15] -->
5.1.1 Construction of New Sequence

<!-- b000369 | prose | pages [15] -->
To predict when a match undergoes swings in momentum, transitioning from one player to another, we extend our evaluation model to achieve the goal. Firstly, we subtract the scores of the two players at each sample point to obtain the difference between their scores, creating a new sequence of {Δ𝑀1, Δ𝑀2, . . . , Δ𝑀𝑛}. The value above zero in this sequence means that player 1 outperforms player 2 and vice versa. While this could not be considered as "momentum swings", so we use the difference between adjacent moments as a standard to detect drastic changes. After that we get an IAGO sequence. Only when the difference surpasses our predetermined threshold, we consider it as a swing in momentum during the match. Eventually, we pick the eligible time point out to generate a brand-new ”catastrophic sequence“ for future prediction, which is displayed as {𝑡(0)(1), 𝑡(0)(2), . . . , 𝑡(0)(𝑛)}.

<!-- b000370 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000371 | heading | pages [15] -->
5.1.2 Level Comparison Test

<!-- b000372 | prose | pages [15] -->
To ensure the feasibility of the modeling method, it is necessary to perform inspection and processing on the sequence, one of which is calculating the ratio of the series. If all the ratios 𝜆(𝑘)   𝑒−2 2 𝑛+1, 𝑒 fall within the interval Θ = , the sequence can be used in the construction of GM(1,1) 𝑛+1

<!-- b000373 | prose | pages [15] -->
model. Below is the calculation formula of level ratio.

<!-- b000374 | prose | pages [15] -->
𝜆(𝑘) = 𝑡(0)(𝑘−1) , 𝑘= 2, 3, · · · , 𝑛 (12) 𝑡(0)(𝑘)

<!-- b000375 | prose | pages [15] -->
After inspection, all of the ratios fall within the interval of (0.9200, 1.0869). Therefore, there is no need for a translation transformation, and the GM(1,1) model is applicable.

<!-- b000376 | heading | pages [15] -->
5.2 Utilize the Model to Obtain the Predicted Values

<!-- b000377 | heading | pages [15] -->
5.2.1 Build Momentum Swings Grey Forecasting Model

<!-- b000378 | prose | pages [15] -->
Disaster prediction, also known as disaster grey prediction, is an application of the GM(1,1) grey prediction model. Specifically, it involves identifying abnormal points (or so-called disaster points) in a sequence, which are points that are either significantly larger or smaller than the others. These abnormal points are then used to construct a subsequence and from this subsequence, a time distribution sequence is obtained. GM(1,1) model is then established for the time distribution sequence of the abnormal points to predict their future time distribution, thus determining when the abnormal points are likely to occur in the future.

<!-- b000379 | prose | pages [15] -->
Based on this idea and previous data processing, we extract all time points that exceed a certain threshold to form a new sequence. Subsequently, we construct a GM(1,1) grey prediction model, considering all points exceeding the threshold as turning points in the prediction and predict their time distribution based on the established model.

<!-- b000380 | prose | pages [15, 16] -->
Grey forecasting refers to the estimation and prediction of the developmental patterns of system behavior characteristics using the GM model. It can also be used to estimate and calculate the occurrence time of abnormal behavior characteristics, as well as study the future time distribution of events within a specific time zone, and so on. It is evident that the functionality of this model aligns with the requirements of our need. As a consequence, we generate the AGO sequence and average 微信公众号：数学模型 sequence below.

<!-- b000381 | furniture | pages [15] -->
关注数学模型

<!-- b000382 | furniture | pages [15] -->
2

<!-- b000383 | furniture | pages [15] -->
MATHmodels

<!-- b000384 | furniture | pages [15] -->
获取更多资讯

<!-- b000385 | furniture | pages [16] -->
Team # 2401919

<!-- b000386 | furniture | pages [16] -->
Page 16 of 25

<!-- b000388 | prose | pages [16] -->
𝑘 𝑡(1) = (𝑡(1)(1), 𝑡(1)(2), . . . , 𝑡(1)(𝑛)), ∑︁ 𝑡(1)(𝑘) = 𝑡(0)(𝑖), 𝑘= 1, 2, . . . , 𝑛 𝑖=1 𝑧(1) = (𝑧(1)(2), 𝑧(1)(3), . . . , 𝑧(1)(𝑛)), 𝑧(1)(𝑘) = 0.5𝑥(1)(𝑘) + 0.5𝑥(1)(𝑘−1), 𝑘= 2, 3, . . . , 𝑛

<!-- b000389 | prose | pages [16] -->
Then we establish the grey differential equation, where 𝑎and 𝑏are unknown parameters.

<!-- b000390 | prose | pages [16] -->
𝑡(0)(𝑘) + 𝑎𝑧(1)(𝑘) = 𝑏, 𝑘= 2, 3, . . . , 𝑛 (13)

<!-- b000391 | prose | pages [16] -->
Then the corresponding whitening differential equation is written as below, where m is a 微信号：MATHmodels continous variable. 𝑑𝑡(1) 𝑑𝑚+ 𝑎𝑡(1)(𝑚) = 𝑏 (14)

<!-- b000392 | prose | pages [16] -->
−𝑧(1)(2) 1   −𝑧(1)(3) 1 We define 𝑢= (𝑎, 𝑏)𝑇, 𝑌= (𝑡(0)(2), 𝑡(0)(3), . . . , 𝑡(0)(𝑛))𝑇, 𝐵= ... ... By least square

<!-- b000393 | prose | pages [16] -->
−𝑧(1)(𝑛) 1 method, we could find the ˆ𝑢= (𝐵𝑇𝐵)−1𝐵𝑇𝑌that makes 𝐽( ˆ𝑢) = (𝑌−𝐵ˆ𝑢)𝑇(𝑌−𝐵ˆ𝑢) obtain the minimum value. By solving the whitening differential equation, we can obtain the predictive values, which is explicitly represented below.

<!-- b000394 | prose | pages [16] -->
𝑡(1)(𝑘+ 1) = (𝑡(0)(1) −𝑏 𝑎)𝑒−𝑎𝑘+ 𝑏 𝑎, 𝑘= 0, 1, . . . , 𝑛−1, . . . (15)

<!-- b000395 | prose | pages [16] -->
When the predictive value exceeds the threshold, it is defined as 1 (representing a turning point), otherwise it is defined as 0. We can obtain the comparison results between the predictive values and the original data, as shown in Figure 9.

<!-- b000396 | prose | pages [16] -->
As can be seen from the graph, the predicted values closely match or even overlap with the actual values, indicating a high level of fit and accuracy in this model. This accuracy is closely related to the characteristics of the GM(1,1) model, which is suitable for sequences with a small amount of data (around 20) and short-to-medium-term predictions.

<!-- b000397 | heading | pages [16] -->
5.3 Model Diagnosis

<!-- b000398 | prose | pages [16] -->
Based on the diagnosis, the average relative error Δ of this model is 0.0378, indicating a Second Class accuracy. Additionally, the absolute correlation 𝑔0 is calculated as 0.9895, and the mean square deviation ratio 𝐶0 is 0.1284, both indicating a First Class accuracy. These results indicate a high level of accuracy in the model, making it suitable for predicting turning points in competitions. Please refer to the Appendix A for the evaluation criteria.

<!-- b000399 | furniture | pages [16] -->
关注数学模型

<!-- b000400 | furniture | pages [16] -->
2

<!-- b000401 | furniture | pages [16] -->
MATHmodels

<!-- b000402 | furniture | pages [16] -->
获取更多资讯

<!-- b000403 | furniture | pages [17] -->
Team # 2401919

<!-- b000404 | furniture | pages [17] -->
Page 17 of 25

<!-- b000405 | prose | pages [17] -->
Predict Turning Point 1 actual_value predictive_value

<!-- b000406 | prose | pages [17] -->
微信公众号：数学模型 Turning Point

<!-- b000407 | prose | pages [17] -->
0 0 50 100 150 200 250 300 350 Time

<!-- b000408 | caption | pages [17] -->
Figure 9: Predictive and Actual Turning plot in Gentlemen’s Singles Final

<!-- b000409 | heading | pages [17] -->
6 Task5: Quantify the Impact of Different Factors on the Swings

<!-- b000410 | heading | pages [17] -->
6.1 Gray Relational Analysis

<!-- b000411 | prose | pages [17] -->
Grey relational analysis gauges the relationship between sequences by comparing their geometric 微信号：MATHmodels shapes. It involves converting discrete data points into continuous line graphs using linear interpolation. A model is then built to assess correlation based on the geometric features of these graphs. The closer the shapes, the higher the correlation between the sequences.

<!-- b000412 | prose | pages [17] -->
To explore the correlation between various factors and match fluctuations, let’s consider the final match as an example. We apply the grey relational analysis method to calculate the correlation between the sequences of various indicators and the performance difference sequences of the two athletes. This analysis helps us determine which factors are most related to match swings and provide corresponding recommendations for improving performance.

<!-- b000413 | prose | pages [17] -->
We denote the reference sequence as {Δ𝑀1, Δ𝑀2, . . . , Δ𝑀𝑛}, and we have 18 comparison se- quences collectively referred to asΔ𝑝, specifically {Δ𝑆1, Δ𝑆2, . . . , Δ𝑆𝑛}, . . . , {Δ𝑆𝐶1, Δ𝑆𝐶2, . . . , Δ𝑆𝐶𝑛}, corresponding to the difference between the 18 indicators of player 1 and player 2. Then we calculate the correlation coefficient using the following formula, taking the Δ𝑆sequence for example.

<!-- b000414 | prose | pages [17] -->
𝜉𝑖(𝑘) = min𝑝min𝑡|Δ𝑀(𝑡) −Δ𝑝(𝑡)| + 𝜌max𝑝max𝑡|Δ𝑀(𝑡) −Δ𝑝(𝑡)| (16) |Δ𝑀(𝑘) −Δ𝑆(𝑘)| + 𝜌max𝑝max𝑡|Δ𝑀(𝑡) −Δ𝑝(𝑡)|

<!-- b000415 | prose | pages [17] -->
Where 𝜌∈[0, 1] represents the resolution coefficient. Generally, a higher 𝜌value indicates a higher resolution, while a lower 𝜌value indicates a lower resolution. The correlation coefficient defined in the above equation is an indicator that describes the degree of correlation between the comparison sequence and the reference sequence at a certain moment. Since there is a correlation coefficient for each moment, the information appears to be too scattered and inconvenient for comparison. Therefore, we provide the following equation as a measure of the correlation between the sequence Δ𝑀and the reference sequences.

<!-- b000416 | prose | pages [17] -->
𝑛 𝑟𝑖= 1 ∑︁ 𝜉𝑖(𝑘) (17) 𝑛 𝑘=1

<!-- b000417 | prose | pages [17] -->
After calculation, the correlation of each indicator is shown in Table 3.

<!-- b000418 | furniture | pages [17] -->
关注数学模型

<!-- b000419 | furniture | pages [17] -->
2

<!-- b000420 | furniture | pages [17] -->
MATHmodels

<!-- b000421 | furniture | pages [17] -->
获取更多资讯

<!-- b000422 | furniture | pages [18] -->
Team # 2401919

<!-- b000423 | furniture | pages [18] -->
Page 18 of 25

<!-- b000424 | caption | pages [18] -->
Table 3: Correlation of 18 Indicators

<!-- b000425 | prose | pages [18] -->
𝑟𝑆 𝑟𝐺 𝑟𝑃 𝑟𝐴 𝑟𝐵 𝑟𝑁 𝑟𝐹𝑆𝑢 𝑟𝐹𝑆𝑐 𝑟𝑆𝑆𝑐 0.9244 0.9250 0.8330 0.9238 0.9239 0.9239 0.9246 0.9237 0.9239 微信公众号：数学模型 𝑟𝑅𝑆𝑐 𝑟𝐷𝐹 𝑟𝑈𝐸 𝑟𝐷 𝑟𝑉 𝑟𝑆𝑊 𝑟𝑆𝐷 𝑟𝑅𝐷 𝑟𝑆𝐶 0.9237 −0.9238 −0.9008 0.6744 0.8993 0.8043 0.8846 0.8866 0.7953

<!-- b000426 | prose | pages [18] -->
From the perspective of various refined indicators, the indicator with the highest correlation is the cumulative number of games won, with the correlation 𝑟𝐺reaching 0.9250. This indicates that in the long term, this indicator has the highest correlation with the swings in the match, and the ability of players to break through in games is the most crucial factor in reversing the situation.

<!-- b000427 | prose | pages [18] -->
From the perspective of the five aspects of the evaluation system, the aspect with the highest overall correlation is the second aspect, which is the offensive efficiency of players, with an average correlation of 0.9239. This is the highest average correlation among the five aspects, indicating that 微信号：MATHmodels in the long term, the offensive efficiency of players, specifically their ability to break through in attacks, is the most crucial aspect in reversing the situation and igniting momentum.

<!-- b000428 | heading | pages [18] -->
6.2 Advice to a Player Going into a New Match

<!-- b000429 | prose | pages [18] -->
Based on the different correlations between the above indicators, aspects, and momentum swings, we provide the following recommendations for players:

<!-- b000430 | prose | pages [18] -->
Firstly, from a broader perspective, offensive efficiency is identified as the key aspect to influence the changes in the match situation. Emphasis should be placed on the athlete’s proactive approach to real-time attacks and their ability to seek breakthroughs. When facing a new opponent in a new match, the athlete is confronted with unknown and unpredictable external factors. Therefore, the athlete should firstly focus more on their own performance, take the initiative to launch attacks, and seize opportunities to break through, rather than solely adopting a passive defensive strategy. Simultaneously, in unfamiliar competition environments, athletes should boldly try different offensive tactics, identify the weak points of their opponents, gradually take control of the situation, and gain momentum.

<!-- b000431 | prose | pages [18] -->
From a more detailed perspective, the cumulative number of games won is identified as the most crucial factor for the match swings. Each game consists of many points, requiring the athlete to have a comprehensive understanding of the overall situation, including the allocation of physical energy, changeable tactical choices, targeted strategies for server and returner, and so on. This tests the athlete’s ability to coordinate and plan comprehensively. Furthermore, comparing the correlation coefficient of cumulative points, which is only 0.833, further emphasizes that the most crucial factor for an athlete in reversing the situation is not just winning individual points but rather adopting a long-term strategy.

<!-- b000432 | heading | pages [18] -->
7 Task6: Test the Accuracy of the Prediction Model

<!-- b000433 | prose | pages [18, 19] -->
To further examine the predictive performance of this model, we have also selected data from the 2023 Wimbledon Gentlemen’s Singles Semi-final (Jannik Sinner vs Novak Djokovic) to make predictions and compare them with the actual match flow. Below is the comparison graph displaying the predictive turning points alongside the actual turning points.

<!-- b000434 | furniture | pages [18] -->
关注数学模型

<!-- b000435 | furniture | pages [18] -->
2

<!-- b000436 | furniture | pages [18] -->
MATHmodels

<!-- b000437 | furniture | pages [18] -->
获取更多资讯

<!-- b000438 | furniture | pages [19] -->
Team # 2401919

<!-- b000439 | furniture | pages [19] -->
Page 19 of 25

<!-- b000441 | prose | pages [19] -->
Predict Turning Point-2023 Wimbledon Gentlemen's Single Semifinal 微信公众号：数学模型 1 actual_value predictive_value

<!-- b000442 | prose | pages [19] -->
Turning Point

<!-- b000443 | prose | pages [19] -->
0 0 50 100 150 200 Time

<!-- b000444 | caption | pages [19] -->
Figure 10: Predictive and Actual Turning Points in Gentlemen’s Singles Semifinal

<!-- b000445 | prose | pages [19] -->
微信号：MATHmodels The average relative error of this model is 0.0883, indicating a Third Class accuracy. The absolute correlation is calculated as 0.9716, and the mean square deviation ratio is 0.2859, both indicating a First Class accuracy. These results all indicate a relatively high level of accuracy, but worse compared to the Final. And we can observe that the predictive turning points are somewhat delayed compared to the actual turning points.

<!-- b000446 | prose | pages [19] -->
In order to enhance the predictive performance of this model in the future, we are considering incorporating the following factors:

<!-- b000447 | prose | pages [19] -->
• Health condition: This includes the physical health and injury status of the players. Being in good physical condition can ensure that the players perform at their best during the match.

<!-- b000448 | prose | pages [19] -->
• Court environment: This includes court conditions , weather conditions, and the atmosphere created by the audience. Different court environments can have a significant impact on the performance of the players.

<!-- b000449 | prose | pages [19] -->
• Competitor: This includes the level and tactical style of the competitor. Strong competitors can increase the pressure and tension for the players, affecting their performance.

<!-- b000450 | heading | pages [19] -->
8 Task7: Generalize the Model Applicable to Other Matches

<!-- b000451 | prose | pages [19] -->
Women’s tennis matches, compared to men’s tennis matches, tend to prioritize technique, strategy, and agility. On the other hand, men’s tennis matches may place more emphasis on strength and speed. And In Grand Slam tournaments, men play best-of-five sets, while women play best-of-three sets. This means that men’s matches can potentially last longer than women’s matches, so the physical fitness and endurance requirements are also higher.

<!-- b000452 | prose | pages [19, 20] -->
To investigate the generalizability of our model to other matches, we substitute the match data from the 2023 Wimbledon Ladies’ Singles Final (Marketa Vondrousova vs Ons Jabeur) into the model to test its predictive performance. As shown in the figure below： Predict Turning Point-2023 Wimbledon Ladies' Single Final 1 actual_value predictive_value

<!-- b000453 | furniture | pages [19] -->
关注数学模型

<!-- b000454 | furniture | pages [19] -->
2

<!-- b000455 | furniture | pages [19] -->
MATHmodels

<!-- b000456 | furniture | pages [19] -->
获取更多资讯

<!-- b000457 | furniture | pages [20] -->
Team # 2401919

<!-- b000458 | furniture | pages [20] -->
Page 20 of 25

<!-- b000460 | prose | pages [20] -->
微信公众号：数学模型 Turning Point

<!-- b000461 | prose | pages [20] -->
0 0 20 40 60 80 100 120 Time

<!-- b000462 | caption | pages [20] -->
Figure 11: Predictive and Actual Turning Points in Ladies’ Singles Final

<!-- b000463 | prose | pages [20] -->
As shown in the figure, the overall predictive performance is good, with rather small deviation from the actual turning points. The average relative error of this model is 0.0693, indicating a Third Class accuracy. The absolute correlation is calculated as 0.9896, and the mean square deviation 微信号：MATHmodels ratio is 0.2908, both indicating a First Class accuracy. These results all indicate a relatively high level of accuracy, but worse compared to the Gentlemen’s matches.

<!-- b000464 | caption | pages [20] -->
Figure 12: Contrast of Three Matches

<!-- b000465 | prose | pages [20] -->
We also plotted the predictive performance of the three matches separately in Figure 12. The closer the shape of the curve aligns with the exponential growth GM model, the more accurate the predictions are. From the graph, we can see that the predictions for the men’s singles final and semi-final matches are consistent with the exponential growth, while there are some differences between the exponential growth and the predictions for the women’s singles final match. We speculate that the difference may be due to the differences in the match format and the physical characteristics between men and women in sports.

<!-- b000466 | furniture | pages [20] -->
关注数学模型

<!-- b000467 | furniture | pages [20] -->
2

<!-- b000468 | furniture | pages [20] -->
MATHmodels

<!-- b000469 | furniture | pages [20] -->
获取更多资讯

<!-- b000470 | furniture | pages [21] -->
Team # 2401919

<!-- b000471 | furniture | pages [21] -->
Page 21 of 25

<!-- b000472 | heading | pages [21] -->
9 Sensitivity Analysis

<!-- b000473 | prose | pages [21] -->
To test the sensitivity of the PCA-TOPSIS model, we perturbed the weights of the most influential variable, which is the number of games won, by increasing and decreasing them manually by 20%. 微信公众号：数学模型 Then we calculated the results and plotted the comparison chart as Figure 13.

<!-- b000474 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000475 | caption | pages [21] -->
Figure 13: Sensitivity Analysis

<!-- b000476 | prose | pages [21] -->
As can be seen from the graph, the variations in the results are small, indicating that the model has good generalizability, and is relatively robust.

<!-- b000477 | heading | pages [21] -->
10 Model Assessment

<!-- b000478 | heading | pages [21] -->
10.1 Strengths

<!-- b000479 | prose | pages [21] -->
• Individual models for each player allows for a more targeted approach.

<!-- b000480 | prose | pages [21] -->
• The evaluation model established by combining PCA and TOPSIS models takes advantage of both methods, making it more objective and accurate.

<!-- b000481 | prose | pages [21] -->
• The GM(1,1) gray prediction model has a good predictive effect and high generalizability.

<!-- b000482 | heading | pages [21] -->
10.2 Weaknesses

<!-- b000483 | prose | pages [21] -->
• The factors selected are not comprehensive enough and the model overlooks some important factors like health condition, court environment and so on.

<!-- b000484 | prose | pages [21] -->
• The model is not suitable for long-term predictions and is only applicable for short-term interval predictions.

<!-- b000485 | prose | pages [21] -->
• Due to the different tournament formats and specific characteristics of different sports, predicting matches in other categories requires certain parameter adjustments.

<!-- b000486 | furniture | pages [21] -->
关注数学模型

<!-- b000487 | furniture | pages [21] -->
2

<!-- b000488 | furniture | pages [21] -->
MATHmodels

<!-- b000489 | furniture | pages [21] -->
获取更多资讯

<!-- b000490 | furniture | pages [22] -->
Team # 2401919

<!-- b000491 | furniture | pages [22] -->
Page 22 of 25

<!-- b000492 | heading | pages [22] -->
11 Letter

<!-- b000493 | prose | pages [22] -->
微信公众号：数学模型 Dear Sir or Madam:

<!-- b000494 | prose | pages [22] -->
微信号：MATHmodels It is our great honor to provide tennis match preparation strategies for your players. Based on the factors in the provided data files, we build mathematical models to capture the flow of the performance of the players over time, and establish a comprehensive and practical evaluation system. Our approaches, findings, and suggestions are as follows.

<!-- b000495 | prose | pages [22] -->
Firstly, we have combined existing literature to establish a comprehensive evaluation system consisting of five major aspects. We have carefully selected appropriate indicators from the raw data. Secondly, in order to accurately analyze the impact of each indicator on players’ performance, we have conducted data normalization and employed advanced analytical methods to calculate the weights of each indicator. Furthermore, based on an advanced evaluation model, we have obtained performance scores for players, which reflect their momentum at different moments and demonstrate its non-randomness. Lastly, using an advanced forecasting model, we have predicted turning points in the competition and provided evidence of its effectiveness.

<!-- b000496 | prose | pages [22] -->
Here are some findings based on our results.  The momentum of players on the field can be seen as their performance, which can be further divided into five major aspects: current situation, offensive effectiveness, error situation, technical fitness, and starting advantage. The comprehensive performance of players in each aspect reflects their strength and weakness on the field. The momentum of players at every moment is closely related to their cumulative performance before that moment.  The fluctuations and turning points in players’ on-field performance are not random. In other words, the changes in players’ momentum during a competition are not without trace; there are underlying rules and mechanisms behind them. Moreover, momentum is closely related to the game situation. It is evident that momentum plays a crucial role in players’ ability to grasp and reverse the game situation, ultimately leading to success and continuous progress.  The turning points in a game are closely related to the number of games won by the athlete and their offensive effectiveness on the field. The athlete’s ability to break through in games and their efficiency and capability in offensive breakthroughs are key factors in determining whether they can ignite momentum and reverse the game situation. Based on these findings, we put forward some match preparation strategies as follows.  Focus on improving on-field offensive capabilities. In the face of fluctuations in the game situation, learn to take the initiative to attack, actively seek breakthroughs, improve the ability to seize control of the game, and create opportunities proactively.  Emphasize improving on-field offensive efficiency. In the face of changes on the field, it is not only important to create opportunities but also to capitalize on them, improving offensive efficiency and turning advantages into winning positions.  Pay attention to improving receiving and serving skills. When the game situation changes, strive to ensure the quality and stability of receiving and serving, while also accelerating the pace of hitting and the ability to quickly end the game in short rallies, strengthening awareness and ability to intercept at the net.  Focus on enhancing comprehensive coordination abilities on the field. When facing fluctuations in the game situation, tactically coordinate the overall situation, and scientifically allocate physical fitness. Cultivate a long-term perspective and avoid pursuing short-term gains, only focusing on immediate points. We hope our suggestions are helpful. If you have any question, please feel free to contact us.

<!-- b000497 | prose | pages [22] -->
Sincerely,

<!-- b000498 | furniture | pages [22] -->
Team # 2401919 Members

<!-- b000499 | furniture | pages [22] -->
关注数学模型

<!-- b000500 | furniture | pages [22] -->
2

<!-- b000501 | furniture | pages [22] -->
MATHmodels

<!-- b000502 | furniture | pages [22] -->
获取更多资讯

<!-- b000503 | furniture | pages [23] -->
Team # 2401919

<!-- b000504 | furniture | pages [23] -->
Page 23 of 25

<!-- b000505 | heading | pages [23] -->
References

<!-- b000506 | references | pages [23] -->
[1] Yan, Y. F.: Research on the construction of a sports intelligence evaluation index system for high-level

<!-- b000507 | references | pages [23] -->
tennis players in sports colleges based on AHP-TOPSIS analysis[D].Shandong Institute of P.E. and

<!-- b000508 | references | pages [23] -->
微信公众号：数学模型

<!-- b000509 | references | pages [23] -->
Sports,2023.DOI:10.27725/d.cnki.gsdty.2023.000137.

<!-- b000510 | references | pages [23] -->
[2] Meng, F. M., Huang, W. M.: Analysis of Female Tennis Players Winning Factors Based on Decision

<!-- b000511 | references | pages [23] -->
Tree[J].Journal of Jilin Sport University,2019,35(05):43-47.DOI:10.13720/j.cnki.22-1286.2019.05.007.

<!-- b000512 | references | pages [23] -->
[3] Richardson P A, Adler W, Hankes D. Game, set, match: Psychological momentum in tennis[J]. The

<!-- b000513 | references | pages [23] -->
Sport Psychologist, 1988, 2(1): 69-76.

<!-- b000514 | references | pages [23] -->
[4] Ma, J. C., Chen, Q. G., Liang, C. R., Zhou, Z. C.: Model Construction and Research Analysis of

<!-- b000515 | references | pages [23] -->
Winning Factors of Professional Tennis Players in Competitions[J].Bulletin of Sport Science and

<!-- b000516 | references | pages [23] -->
Technology,2023,31(04):66-68+118.DOI:10.19379/j.cnki.issn.1005-0256.2023.04.021.

<!-- b000517 | references | pages [23] -->
[5] He, W. S., Zhang, L. W., Zhang, L. C.:Technical analysis of winning factors of world’s top

<!-- b000518 | references | pages [23] -->
there male tennis players[J].Journal of Wuhan Institute of Physical Education,2011,45(09):67-

<!-- b000519 | references | pages [23] -->
微信号：MATHmodels

<!-- b000520 | references | pages [23] -->
73.DOI:10.15930/j.cnki.wtxb.2011.09.016.

<!-- b000521 | references | pages [23] -->
[6] Dietl H, Nesseler C. Momentum in tennis: Controlling the match[J]. UZH Business Working Paper

<!-- b000522 | references | pages [23] -->
Series, 2017 (365).

<!-- b000523 | references | pages [23] -->
[7] Silva J M, Hardy C J, Crace R K. Analysis of psychological momentum in intercollegiate tennis[J].

<!-- b000524 | references | pages [23] -->
Journal of sport and exercise psychology, 1988, 10(3): 346-354.

<!-- b000525 | references | pages [23] -->
[8] Bahamonde R E. Changes in angular momentum during the tennis serve[J]. Journal of sports sciences,

<!-- b000526 | references | pages [23] -->
2000, 18(8): 579-592.

<!-- b000527 | references | pages [23] -->
[9] Weinberg R, Jackson A. The effects of psychological momentum on male and female tennis players

<!-- b000528 | references | pages [23] -->
revisited[J]. Journal of Sport Behavior, 1989, 12(3): 167.

<!-- b000529 | heading | pages [23] -->
Appendices

<!-- b000530 | heading | pages [23] -->
Appendix A

<!-- b000531 | prose | pages [23] -->
Evaluation Criteria

<!-- b000532 | caption | pages [23] -->
Table 4: KMO Test Evaluation Criteria

<!-- b000533 | prose | pages [23, 24] -->
KMO measure Interpretation KMO⩾0.90 Marvelous 0.80 ⩽KMO< 0.90 Meritorious 0.70 ⩽KMO< 0.80 Average 0.60 ⩽KMO< 0.70 Mediocre 0.50 ⩽KMO< 0.60 Terrible KMO< 0.50 Unacceptable Indicators Class Average Relative Error Absolute Correlation Mean Deviation Ratio 微信公众号：数学模型 0.01 0.90 0.35 First Class 0.05 0.80 0.50 Second Class 0.10 0.70 0.65 Third Class 0.20 0.60 0.80 Fourth CLass

<!-- b000534 | furniture | pages [23] -->
关注数学模型

<!-- b000535 | furniture | pages [23] -->
2

<!-- b000536 | furniture | pages [23] -->
MATHmodels

<!-- b000537 | furniture | pages [23] -->
获取更多资讯

<!-- b000538 | furniture | pages [24] -->
Team # 2401919

<!-- b000539 | furniture | pages [24] -->
Page 24 of 25

<!-- b000540 | caption | pages [24] -->
Table 5: Grey Prediction Evaluation Criteria

<!-- b000542 | heading | pages [24] -->
Appendix B

<!-- b000543 | prose | pages [24] -->
Code

<!-- b000544 | prose | pages [24] -->
Correlation Heatmap.py

<!-- b000545 | prose | pages [24] -->
correlation_matrix = np.corrcoef(standardized_data, rowvar=False) variables = [’S1’, ’G1’, ’P1’, ’A1’, ’B1’, ’N1’, ’FSu1’, ’FSc1’, ’SSc1’, ’RSc1 ↩→’, ’DF1’, ’UE1’, ’D1’, ’V1’, ’SW1’, ’SD1’, ’RD1’, ’SC1’, ’S2’, ’G2’, ’ ↩→P2’, ’A2’, ’B2’, ’N2’, ’FSu2’, ’FSc2’, ’SSc2’, ’RSc2’, ’DF2’, ’UE2’, ’ 微信号：MATHmodels ↩→D2’, ’V2’, ’SW2’, ’SD2’, ’RD2’, ’SC2’] corr_mat = correlation_matrix rows, cols = np.where(corr_mat != 0) correlation_data = pd.DataFrame({’level_0’: rows, ’level_1’: cols, ’ ↩→correlation’: corr_mat[rows, cols]}) sns.set_theme(style="whitegrid") cmap = sns.diverging_palette(240, 120, as_cmap=True) g = sns.scatterplot(data=correlation_data, x="level_0", y="level_1", hue=" ↩→correlation", size="correlation", palette=cmap, sizes=(50, 250), size_norm=(-.2, .8), ↩→edgecolor=".7") g.set(xlabel="", ylabel="", aspect="equal") plt.xticks(ticks=np.arange(len(variables)), labels=variables, rotation=90) plt.yticks(ticks=np.arange(len(variables)), labels=variables) sns.despine(left=True, bottom=True) plt.legend(loc=’center right’, bbox_to_anchor=(1.2, 0.5), title="Legend") plt.title(label=’Correlation Coefficient Matrix Heat Map’, pad=10) plt.show()

<!-- b000546 | prose | pages [24] -->
Predict Swings.py

<!-- b000547 | prose | pages [24, 25] -->
predicted_sequence, a, b = GM_11(original_sequence) Evaluate(original_sequence, predicted_sequence) length = max(np.max(original_sequence), np.max(predicted_sequence))+10 x = np.arange(0, length, 1) y = np.zeros(length, dtype=int) y[original_sequence] = 1 yp = np.zeros(length, dtype=int) yp[predicted_sequence] = 1 plt.plot(x, y, label=’actual_value’, color=’blue’, linestyle=’-’, linewidth=1) plt.plot(x, yp, label=’predictive_value’, color=’green’, linestyle=’-’, ↩→linewidth=1) plt.title(’Predict Turning Point-2023 Wimbledon Gentlemen\’s Single Final’) plt.show() Score Trend Chart.py score1 = process(standardized_data_p1) score2 = process(standardized_data_p2) length = len(score1) 微信公众号：数学模型 x = np.arange(0, length, 1) x_downsampled = x[::5] score1_downsampled = score1[::5] score2_downsampled = score2[::5] df1 = pd.DataFrame({’time’: x_downsampled, ’normalized_score’:

<!-- b000548 | furniture | pages [24] -->
关注数学模型

<!-- b000549 | furniture | pages [24] -->
2

<!-- b000550 | furniture | pages [24] -->
MATHmodels

<!-- b000551 | furniture | pages [24] -->
获取更多资讯

<!-- b000552 | furniture | pages [25] -->
Team # 2401919

<!-- b000553 | furniture | pages [25] -->
Page 25 of 25

<!-- b000555 | prose | pages [25] -->
↩→score1_downsampled, ’score’: ’player1’}) df2 = pd.DataFrame({’time’: x_downsampled, ’normalized_score’:

<!-- b000556 | prose | pages [25] -->
↩→score2_downsampled, ’score’: ’player2’}) df = pd.concat([df1, df2]) sns.set_theme(style="darkgrid") sns.lineplot(x=’time’, y=’normalized_score’, hue=’score’, palette=[’blue’, ’ ↩→green’], linewidth=1, data=df) plt.title("Score Trend Chart", pad=10) plt.show() 微信号：MATHmodels Necessary Statistical Tests.py def kmo_test(data):

<!-- b000557 | prose | pages [25] -->
X = np.corrcoef(data, rowvar=False) iX = np.linalg.inv(X) S2 = np.diag(np.diag(np.linalg.inv(iX))) AIS = np.dot(np.dot(S2, iX), S2) IS = X + AIS - 2 * S2 Dai = np.diag(np.diag(np.sqrt(AIS))) IR = np.dot(np.dot(np.linalg.inv(Dai), IS), np.linalg.inv(Dai)) AIR = np.dot(np.dot(np.linalg.inv(Dai), AIS), np.linalg.inv(Dai)) a = np.sum((AIR - np.diag(np.diag(AIR))) ** 2) AA = np.sum(a) b = np.sum((X - np.eye(X.shape[0])) ** 2) BB = np.sum(b) kmo_statistic = BB / (AA + BB) return kmo_statistic

<!-- b000558 | prose | pages [25] -->
def bartlett_test(data):

<!-- b000559 | prose | pages [25] -->
sample, variable = data.shape data_corr = np.corrcoef(data, rowvar=False) data_det = np.linalg.det(data_corr) chi2_statistic = -(sample - 1 - (2 * variable + 5) / 6) * np.log(data_det) df = variable * (variable - 1) // 2 p_value = 1 - chi2.cdf(chi2_statistic, df) return chi2_statistic, df, p_value

<!-- b000560 | prose | pages [25] -->
def test_randomness(time_series):

<!-- b000561 | prose | pages [25, 26] -->
df = acorr_ljungbox(time_series, lags=[20], return_df=True, boxpierce=True ↩→) fig, axs = plt.subplots(2, 1, figsize=(10, 8)) plot_acf(time_series, lags=20, alpha=0.05, ax=axs[0]) plot_pacf(time_series, lags=20, alpha=0.05, ax=axs[1]) plt.show() Page 26

<!-- b000562 | furniture | pages [25] -->
关注数学模型

<!-- b000563 | furniture | pages [25] -->
2

<!-- b000564 | furniture | pages [25] -->
MATHmodels

<!-- b000565 | furniture | pages [25] -->
获取更多资讯

<!-- b000566 | furniture | pages [26] -->
Team # 2401919

<!-- b000568 | heading | pages [26] -->
Report on Use of AI

<!-- b000569 | heading | pages [26] -->
1. OpenAI ChatGPT 3.5

<!-- b000570 | prose | pages [26] -->
微信公众号：数学模型 Query1: How do you define "momentum" in tennis? Output: In tennis, “momentum” refers to the psychological and emotional shift in a match that occurs when a player starts performing well and gaining confidence. It involves a player’s ability to maintain control over the match, dominate their opponent, and win crucial points.

<!-- b000571 | prose | pages [26] -->
Momentum can be seen as a positive flow or energy that a player experiences when they string together a series of winning points or games. It often leads to increased confidence, motivation, and focus, while simultaneously affecting the mental state of the opponent.

<!-- b000572 | prose | pages [26] -->
When a player has momentum, they often appear to be in control of the match, making fewer errors, and executing their shots effectively. The player may exhibit a higher level of intensity, aggression, and determination. Momentum can shift back and forth between players during a match and can be influenced by factors such as winning a crucial game, making a spectacular 微信号：MATHmodels shot, or receiving support from the crowd.

<!-- b000573 | prose | pages [26] -->
The concept of momentum in tennis is subjective and intangible, but it can play a significant role in determining the outcome of a match. Players and commentators often refer to momentum as a crucial factor that can decide the winner, as it can have a psychological impact on both players, affecting their performance and decision-making abilities.

<!-- b000574 | heading | pages [26] -->
2. OpenAI ChatGPT 3.5

<!-- b000575 | prose | pages [26] -->
Query1: How can I read and save a .csv file with different data types? Please write me a demo with Python. Output: Sure, you can use the ‘pandas‘ library in Python to read and save CSV files with different types of data. Here’s a simple demo:

<!-- b000576 | prose | pages [26] -->
‘‘‘python import pandas as pd

<!-- b000577 | prose | pages [26] -->
# Create a sample DataFrame with different types of data data = { ’Name’: [’John’, ’Alice’, ’Bob’], ’Age’: [25, 30, 35], ’Height’: [5.8, 5.5, 6.0], ’IsStudent’: [True, False, True] }

<!-- b000578 | prose | pages [26] -->
df = pd.DataFrame(data)

<!-- b000579 | prose | pages [26] -->
# Display the DataFrame print("Original DataFrame:") print(df)

<!-- b000580 | prose | pages [26] -->
# Save the DataFrame to a CSV file df.to_csv(’sample.csv’, index=False)

<!-- b000581 | prose | pages [26, 27] -->
# Read the CSV file back into a DataFrame df_read = pd.read_csv(’sample.csv’) Page 27

<!-- b000582 | furniture | pages [26] -->
关注数学模型

<!-- b000583 | furniture | pages [26] -->
2

<!-- b000584 | furniture | pages [26] -->
MATHmodels

<!-- b000585 | furniture | pages [26] -->
获取更多资讯

<!-- b000586 | furniture | pages [27] -->
Team # 2401919

<!-- b000588 | prose | pages [27] -->
# Display the re-imported DataFrame print("\nDataFrame read from CSV:") print(df_read) 微信公众号：数学模型 ‘‘‘

<!-- b000589 | prose | pages [27] -->
This script creates a DataFrame with columns of different data types, saves it to a CSV file, and then reads it back into another DataFrame. The ‘index=False‘ argument in ‘to_csv‘ function call is used to avoid writing row indices to the CSV file.

<!-- b000590 | heading | pages [27] -->
3. OpenAI ChatGPT 3.5

<!-- b000591 | prose | pages [27] -->
Query1: What is the difference between men’s and women’s singles tennis? Output: Men’s and women’s singles tennis refer to separate categories of singles matches played in professional and amateur tennis. The primary differences between men’s and women’s singles tennis are related to the physical and physiological characteristics of male and female players, as well as some rule variations.

<!-- b000592 | prose | pages [27] -->
微信号：MATHmodels Match duration: Men’s matches tend to be longer in duration compared to women’s matches. This is primarily due to differences in serving speed, power, and the ability to hit winners.

<!-- b000593 | prose | pages [27] -->
Scoring format: The scoring format is the same for both men and women in terms of points, games, and sets. However, women’s matches traditionally play best-of-three sets, while men’s matches play best-of-five sets in most Grand Slam tournaments.

<!-- b000594 | prose | pages [27] -->
Serve speed and power: On average, male players have greater serve speeds and power compared to female players. This often translates into more aces and harder-hitting serves in men’s matches.

<!-- b000595 | prose | pages [27] -->
Physicality: Male players generally possess greater strength, endurance, and physicality compared to female players. This can result in more aggressive shot-making, longer rallies, and a higher intensity of play in men’s matches.

<!-- b000596 | prose | pages [27] -->
Prize money: In professional tennis, there has historically been a gap in prize money between men’s and women’s tournaments. However, in recent years, efforts have been made towards gender equality in prize money distribution.

<!-- b000597 | prose | pages [27] -->
It’s important to note that these differences are generalizations and do not apply to every individual player. There are exceptional female players who possess powerful serves and endurance, and there are male players known for their finesse and shot-making skills. Tennis is a highly individual sport, and performance in any match is influenced by various factors beyond gender.

<!-- b000598 | furniture | pages [27] -->
关注数学模型

<!-- b000599 | furniture | pages [27] -->
2

<!-- b000600 | furniture | pages [27] -->
MATHmodels

<!-- b000601 | furniture | pages [27] -->
获取更多资讯
