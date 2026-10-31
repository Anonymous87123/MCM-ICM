# P-C-2024-2403774-be4a823f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | prose | pages [1] -->
Problem Chosen

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | title | pages [1] -->
2403774

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
Uncovering the Hidden Momentum: A Data-Science Exploration of

<!-- b000012 | prose | pages [1] -->
Tennis Match Dynamics

<!-- b000013 | prose | pages [1] -->
Tennis, as a comprehensive sport, has always been a subject of great interest. Besides the physical demands on athletes, exceptional skills and outstanding tactical strategies are key to victory. This study delves into the concept of "athletic potential" in competitive sports, an inherent vitality and advantage that becomes apparent during matches, utilizing data science and machine learning techniques. Ultimately, the data-driven insights derived from our models will provide valuable guidance and reference for coaches

<!-- b000014 | prose | pages [1] -->
This article primarily establishes two models: the XGBoost-based Momentum Quantification Model and the Tennis Match Point Time-Convolution Model.

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | title | pages [1] -->
微信号：MATHmodels

<!-- b000018 | prose | pages [1] -->
Before building the models, we initially conducted data preprocessing, including the identification of outliers and handling missing values using strategies such as the Interquartile Range (IQR). We also selectively removed or imputed data based on practical significance. Subsequently, we designed variables based on different timeframes (Current-Past) and

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | prose | pages [1] -->
various temporal scales (Short-Medium-Long). Finally, we used Spearman's correlation coefficient to eliminate variables with high correlations to the dependent variable and those exhibiting

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | prose | pages [1] -->
autocorrelation.

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
Addressing the first problem, this study introduces improvements to the XGBoost-based momentum estimation of players. We establish a relationship between momentum and short-term match outcomes, achieving a precision MSE (Mean Square Error) indicator of 0.02 through a 5- fold cross-

<!-- b000025 | prose | pages [1] -->
validation approach. Regarding the second problem, we randomly generated match scenarios based on game rules and original data. We applied the model developed for problem one to estimate the momentum for both real and random matches. Ultimately, by comparing various metrics that measure the correlation between momentum and match outcomes, we provide strong evidence supporting the impact of momentum on match scores.

<!-- b000026 | prose | pages [1] -->
For the third problem, we utilized Bayesian online change-point detection methods to identify crucial turning points in matches, and we visualized the results using two sample matches. To accommodate the different temporal characteristics of match data, such as capturing immediate situations in short timeframes and understanding overall trends in long timeframes, we designed the Tennis Match Point Temporal Convolutional Network. This model achieved a Top-1 accuracy of 75.70% in predicting turning points.

<!-- b000027 | prose | pages [1] -->
Concerning the fourth problem, we conducted domain transfer testing using tennis match data from the 2023 Wimbledon Women's Singles. The momentum prediction achieved a precise MSE indicator of 0.025, demonstrating the high generalization performance of our model.

<!-- b000028 | prose | pages [1] -->
Additionally, we performed sensitivity analysis to explore the impact of input variations on the model. Finally, the strengths and weaknesses of our model are summarized. In conclusion, we include a letter to tennis coaches at the end of the article, introducing the overall concept and results of our research.

<!-- b000029 | keywords | pages [1] -->
Keywords: Tennis Athletic Potential, XGBoost, Momentum Quantification, Temporal

<!-- b000030 | prose | pages [1] -->
Convolutional Network

<!-- b000031 | prose | pages [1] -->
关注数学模型

<!-- b000032 | furniture | pages [1] -->
2

<!-- b000033 | furniture | pages [1] -->
MATHmodels

<!-- b000034 | furniture | pages [1] -->
获取更多资讯

<!-- b000035 | furniture | pages [2] -->
Team # 2403774                                                                                 Page 2 of 23

<!-- b000036 | furniture | pages [2] -->


<!-- b000037 | heading | pages [2] -->
Contents

<!-- b000038 | contents | pages [2] -->
1 Introduction .................................................................................................................................. 3

<!-- b000039 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000040 | contents | pages [2] -->
1.1 Background ............................................................................................................................ 3

<!-- b000041 | contents | pages [2] -->
1.2 Restatment of the Problem ..................................................................................................... 3

<!-- b000042 | contents | pages [2] -->
1.3 Our Work ................................................................................................................................ 3

<!-- b000043 | contents | pages [2] -->
2 Assumptions And Notations ........................................................................................................ 4

<!-- b000044 | contents | pages [2] -->
2.1 Assuptions .............................................................................................................................. 4

<!-- b000045 | contents | pages [2] -->
2.2 Notations ................................................................................................................................ 4

<!-- b000046 | contents | pages [2] -->
3 Data Preprocessing ....................................................................................................................... 5

<!-- b000047 | contents | pages [2] -->
3.1 Data Cleaning ......................................................................................................................... 5

<!-- b000048 | contents | pages [2] -->
3.2 Data Transformation .............................................................................................................. 6

<!-- b000049 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000050 | contents | pages [2] -->
3.3 Feature Recombination .......................................................................................................... 7

<!-- b000051 | contents | pages [2] -->
3.4 Variable Selection .................................................................................................................. 8

<!-- b000052 | contents | pages [2] -->
4 Task 1: Momentum quantization and prediction model ........................................................ 10

<!-- b000053 | contents | pages [2] -->
4.1 Definition and Quantification of Momentum ...................................................................... 10

<!-- b000054 | contents | pages [2] -->
4.2 XGBoost-Based Momentum Quatification Model .............................................................. 10

<!-- b000055 | contents | pages [2] -->
4.3 Results Visualization and Analysis ...................................................................................... 12

<!-- b000056 | contents | pages [2] -->
5 Task 2: The Momentum-Outcome Connection ....................................................................... 13

<!-- b000057 | contents | pages [2] -->
5.1 Random Match Scenario Generation ................................................................................... 13

<!-- b000058 | contents | pages [2] -->
5.2 Analysis of the Impact of Momentum on Scores ................................................................. 13

<!-- b000059 | contents | pages [2] -->
6 Bayesian Inflection point Detection and Prediction ................................................................ 15

<!-- b000060 | contents | pages [2] -->
6.1 Bayesian Online Inflection point Detection Method for Identifying Inflection points ........ 15

<!-- b000061 | contents | pages [2] -->
6.2 Correlation Analysis of Inflection Points ............................................................................. 17

<!-- b000062 | contents | pages [2] -->
6.3 Tennis Match Point Temporal Convolutional Network ....................................................... 18

<!-- b000063 | contents | pages [2] -->
6.4 Suggestions .......................................................................................................................... 19

<!-- b000064 | contents | pages [2] -->
7 Task 4: Model Validation and Evaluation ................................................................................ 20

<!-- b000065 | contents | pages [2] -->
7.1 Model Validation with Other Matches and Accuracy .......................................................... 20

<!-- b000066 | contents | pages [2] -->
7.2 Model Evaluation ................................................................................................................... 21

<!-- b000067 | contents | pages [2] -->
8 Sensitivity Analysis ..................................................................................................................... 21

<!-- b000068 | contents | pages [2] -->
9 Advantages and Disadvantages Analysis .................................................................................... 22

<!-- b000069 | contents | pages [2] -->
9.1 Advantages ............................................................................................................................. 22

<!-- b000070 | contents | pages [2] -->
9.2 Disadvantages ........................................................................................................................ 22

<!-- b000071 | contents | pages [2] -->
References ......................................................................................................................................... 23

<!-- b000072 | furniture | pages [2] -->


<!-- b000073 | furniture | pages [2] -->


<!-- b000074 | contents | pages [2] -->
关注数学模型

<!-- b000075 | furniture | pages [2] -->
2

<!-- b000076 | furniture | pages [2] -->
MATHmodels

<!-- b000077 | furniture | pages [2] -->
获取更多资讯

<!-- b000078 | furniture | pages [3] -->
Team # 2403774                                                                                 Page 3 of 23

<!-- b000079 | furniture | pages [3] -->


<!-- b000080 | heading | pages [3] -->
1 Introduction

<!-- b000081 | heading | pages [3] -->
1.1 Background

<!-- b000082 | prose | pages [3] -->
"To become the first man in a decade to defeat Novak Djokovic on Centre Court at Wimbledon is truly a remarkable feat I'll always cherish," Alcaraz reflected on his historic win.

<!-- b000083 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000084 | prose | pages [3] -->
In the gripping Wimbledon men's singles final of 2023, the prodigious 20-year-old Spaniard, Alcaraz, outplayed the venerable 36-year-old Serbian champion, Djokovic, in a five-set thriller to claim the prestigious title. Despite a rocky start, where Alcaraz dropped the first set 1-6, he tenaciously fought back to secure the match, leaving the audience in awe of the stunning upset.

<!-- b000085 | prose | pages [3] -->
Competitive momentum, within the realm of sports, represents the intrinsic vigor and edge that becomes apparent during a match. It denotes the collective strength and prowess of either a team or an individual athlete, which is instrumental in asserting dominance within the game.

<!-- b000086 | prose | pages [3] -->
To harness this competitive momentum, a diverse set of skills is crucial, encompassing technical prowess, tactical acumen, psychological resilience, and rigorous physical conditioning. Possession of such attributes enables athletes to elevate their performance, dominate the competition, and achieve superior results.

<!-- b000087 | prose | pages [3] -->
Despite its frequent mention in sports narratives, competitive momentum remains an elusive,

<!-- b000088 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000089 | prose | pages [3] -->
subjective concept, one that defies direct measurement through conventional statistical methods. Therefore, sports analysts and coaches are often inclined to leverage specific in-game data, such as points scored, service speed, error rates, and more, to construct models that endeavor to quantify the effects of momentum and forecast game trends and outcomes.

<!-- b000090 | heading | pages [3] -->
1.2 Restatment of the Problem

<!-- b000091 | prose | pages [3] -->
Through the analysis and investigation of the background and negotiators’ guidance of the problem, the restate of the problem can be expressed as follows: ⚫

<!-- b000092 | heading | pages [3] -->
Build a mathematic model for Match Flow Analysis:

<!-- b000093 | prose | pages [3] -->
✓ Create a model that captures the progression of a tennis match based on the scorning

<!-- b000094 | prose | pages [3] -->
events.The model should be capable of identifying who is well-performed at any given moment, and quantify their level of superiority. ✓ Include a visualization that depicts the flow of the match, as informed by the model. ✓ Incorporate the advantage that players have while serving into the model. ⚫ Use the model to evaluate the claim by a tennis coach who doesn’t believe the role of “momentum”. ⚫ Predict Shifts in “Momentum”: ✓ Construct a model to forsee the pivotal moments that shifts the “momentum” of the

<!-- b000095 | prose | pages [3] -->
game,and identify the key indicators that drive these shifts. ✓ Offer advise to a player entering a new match against a different opponent, based on the

<!-- b000096 | prose | pages [3] -->
dynamics of “momentum” swings. ⚫

<!-- b000097 | heading | pages [3] -->
Model Testing:

<!-- b000098 | prose | pages [3] -->
✓ Test the model against additional matches to evaluate its effectiveness in forecasting

<!-- b000099 | prose | pages [3] -->
momentum swings and the outcomes of games. ✓ Should the model display occasional inaccuracies, pinpoint elements that could be

<!-- b000100 | prose | pages [3] -->
incorporated in future versions to enhance its predictive accuracy. ✓ Consider how the model might be adapted to other contexts, such as women's matches,

<!-- b000101 | prose | pages [3] -->
different court surfaces, or other racket sports like table tennis. ⚫ Compose a one-to-two-page memo to be included in the report, offering advice to tennis coaches according to the study.

<!-- b000102 | heading | pages [3] -->
1.3 Our Work

<!-- b000103 | prose | pages [3] -->
关注数学模型

<!-- b000104 | furniture | pages [3] -->
2

<!-- b000105 | furniture | pages [3] -->
MATHmodels

<!-- b000106 | furniture | pages [3] -->
获取更多资讯

<!-- b000107 | furniture | pages [4] -->
Team # 2403774                                                                                 Page 4 of 23

<!-- b000108 | furniture | pages [4] -->


<!-- b000109 | prose | pages [4] -->
In line with the background and research questions, our work encompasses the following aspects: (1) Data preprocessing to obtain the required independent variables for subsequent modeling. Establishing an XGBoost-based momentum quantification model to quantify and assess a player's performance at specific times, and visualizing the momentum in relation to match outcomes. (2) Simulating a random match to compare the momentum of a random match with that of a real

<!-- b000110 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000111 | prose | pages [4] -->
match. Using Pearson correlation coefficients, we confirmed that a player's fluctuations and success during a match are not random but influenced by momentum. (3) Utilizing Bayesian online changepoint detection methods to identify turning points in each match and obtaining the importance ranking of independent variables through Spearman rank correlation. We then developed the Tennis Match Point Time-Convolution Model, which can predict when turning points are likely to occur. (4) Validating the model using data from other matches and conducting an evaluation of the model's performance.

<!-- b000112 | heading | pages [4] -->
2 Assumptions And Notations

<!-- b000113 | heading | pages [4] -->
2.1 Assuptions

<!-- b000114 | prose | pages [4] -->
⚫ The sum of momentum of two players is constant. Momentum reflects a player's ability to

<!-- b000115 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000116 | prose | pages [4] -->
score against an opponent. Given the momentum of player 1, the momentum of player 2 can be derived symmetrically, which is conducive to describing the player's state. ⚫ The effect of momentum is primarily short-term. A player's momentum at a given moment may remain stable in a local time window and change with subsequent wins and losses. ⚫ There is a certain degree of momentum inheritance between each game, set and match. At the beginning of each game, the player will be somewhat affected by the situation of the previous game or the overall set and court, thus obtaining different initial momentum. ⚫ The impact of data outside the table on the match is ignored. The physical quality of athletes and other factors can be reflected in the information of the match given in the table, and other factors have a small impact and can be ignored. ⚫ The number of promotions a player makes may be unrelated to momentum. Both sides in each match have the same number of advances and similar physical exertion, so the effect of advance records on momentum is not taken into account. ⚫ The total distance run to some extent represents the value of physical exertion. It is common sense that the more an athlete runs, the greater the physical exertion.

<!-- b000117 | heading | pages [4] -->
2.2 Notations

<!-- b000118 | prose | pages [4] -->
Tabel 1:Symbols and Descriotions

<!-- b000119 | prose | pages [4] -->
Symbol Description Current iteration step 𝑏 𝑀 𝜂 Ensemble of models Learning rate Number of samples in the dataset 𝑖 Total number of samples in the dataset 𝑚

<!-- b000120 | prose | pages [4] -->
Use to adjust the complexity of the tree. 𝛾,𝜆 Momentum based on match outcomes 𝑦𝑖

<!-- b000121 | prose | pages [4] -->
(𝑡) Model's prediction of momentum at iteration t

<!-- b000122 | prose | pages [4] -->
𝑌𝑖

<!-- b000123 | prose | pages [4] -->
Current number of leaf nodes in the regression tree 𝑇 Momentum of player i at time t 𝑌𝑖

<!-- b000124 | prose | pages [4] -->
关注数学模型

<!-- b000125 | furniture | pages [4] -->
2

<!-- b000126 | furniture | pages [4] -->
MATHmodels

<!-- b000127 | furniture | pages [4] -->
获取更多资讯

<!-- b000128 | furniture | pages [5] -->
Team # 2403774                                                                                 Page 5 of 23

<!-- b000129 | furniture | pages [5] -->


<!-- b000130 | prose | pages [5] -->
Maximum momentum 𝑀𝑚0 Serving momentum factor 𝑀𝑓=0.1 𝑀𝑓

<!-- b000131 | heading | pages [5] -->
3 Data Preprocessing

<!-- b000132 | heading | pages [5] -->
3.1 Data Cleaning

<!-- b000133 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000134 | prose | pages [5] -->
Due to the randomness of data and missing records from devices, it is necessary to clean the data. This involves correcting anomalies and filling in missing values to ensure the accuracy of subsequent analyses and the reliability of modeling. Taking the current serve speed column(speed_mph) and Player 1's running distance column (p1_distance_run) as examples, the methods and process of data cleaning are detailed as follows.

<!-- b000135 | heading | pages [5] -->
3.1.1 Correction of Anomalous Values

<!-- b000136 | prose | pages [5] -->
Due to the randomness in data collection, there may be outliers in the samples that significantly differ from the majority of the values, thus it requirs repair or removal. Use the Interquartile Range (IQR) method to identify the lower quartile Q1 at the 25% position and the upper quartile Q3 at the 75% position in the data, then calculate the interquartile range (IQR), with the calculation formula as follows:

<!-- b000137 | prose | pages [5] -->
𝑄1 = 𝑛+ 1

<!-- b000138 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000139 | prose | pages [5] -->
(1) 4

<!-- b000140 | prose | pages [5] -->
𝑄3 = 3(𝑛+ 1)

<!-- b000141 | prose | pages [5] -->
(2) 4

<!-- b000142 | prose | pages [5] -->
(3) 𝐼𝑄𝑅= 𝑄3 −Q1 In the formula, n is the size of the dataset. If n is not an integer, linear interpolation can be performed between the two data points closest to n to estimate Q1 and Q3. The interquartile range (IQR) represents the distance between Q3 and Q1.

<!-- b000143 | prose | pages [5] -->
In this paper, data outside the range [Q1 - 1.5 IQR, Q3 + 1.5 IQR] is defined as an outlier and is subjected to correction. Taking speed_mph as an example, the box plot of its outliers is shown in

<!-- b000144 | caption | pages [5] -->
Figure 1.

<!-- b000145 | prose | pages [5] -->
For the outliers on the left side of the figure, they are replaced by performing data fitting interpolation within the group of matches they belong to. It is worth noting that for the p1_distance_run data column, since p1_distance_run is related to rally_count, the more rallies played, the greater the running distance of the player. Therefore, it is necessary to first remove the impact of the number of rallies on running distance. First,divide p1_distance_run by rally_count,and then proceed to correct the outliers. The box plots of outliers before and after preprocessing are shown in

<!-- b000146 | caption | pages [5] -->
Figure 2. The processed outliers are then subjected to data fitting interpolation, and multiplied by

<!-- b000147 | prose | pages [5] -->
rally_count to serve as the new corrected values for p1_distance_run.

<!-- b000148 | furniture | pages [5] -->


<!-- b000149 | caption | pages [5] -->
Figure 1:Outlier boxplot of speed mph

<!-- b000150 | caption | pages [5] -->
Figure 2: Box plots of outliers for p1_distance_run before and after preprocessing

<!-- b000151 | heading | pages [5] -->
3.1.2 Filling Missing Data

<!-- b000152 | prose | pages [5] -->
Firstly, it is necessary to identify missing values in the dataset. Taking speed_mph as an example, a heatmap of missing values can be generated using the Heatmap Function from the Seaborn Library in Python. This heatmap provides a visual representation of missing data within the dataset. The result

<!-- b000153 | prose | pages [5] -->
关注数学模型

<!-- b000154 | furniture | pages [5] -->
2

<!-- b000155 | furniture | pages [5] -->
MATHmodels

<!-- b000156 | furniture | pages [5] -->
获取更多资讯

<!-- b000157 | furniture | pages [6] -->
Team # 2403774                                                                                 Page 6 of 23

<!-- b000158 | furniture | pages [6] -->


<!-- b000159 | prose | pages [6] -->
of generating a heatmap using the heatmap function is shown in Figure 3. In the figure, there are large yellow bands with gaps, indicating continuous missing data in this segment. Upon comparison, it is observed that this missing data all originates from the match_id = 2023-wimbledon-1310, which is attributed to system errors such as missing device records and the importance of the speed_mph parameter. Therefore, the data from this match is not considered, and the remaining 30 sets of data

<!-- b000160 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000161 | prose | pages [6] -->
will be used for subsequent analysis and modeling.

<!-- b000162 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000163 | furniture | pages [6] -->


<!-- b000164 | caption | pages [6] -->
Figure 3: The heatmap of missing values for "speed_mph."

<!-- b000165 | prose | pages [6] -->
Additionally, considering the real circumstances of the matches, when there is a double fault situation in serving, meaning p1_double_fault + p2_double_fault = 1, both speed_mph and rally_count should be equal to 0. Taking the match_id=1301 as an example, all the data with speed_mph=NA is selected, as shown in Table 2.

<!-- b000166 | prose | pages [6] -->
Tabel 2: Partial data when match_id=1301 race speed_mph=NA

<!-- b000167 | prose | pages [6] -->
p2_double

<!-- b000168 | prose | pages [6] -->
p1_double_fault+p2_double

<!-- b000169 | prose | pages [6] -->
p1_double elapsed_time

<!-- b000170 | prose | pages [6] -->
_fault

<!-- b000171 | prose | pages [6] -->
_fault

<!-- b000172 | prose | pages [6] -->
0:32:57 0 1

<!-- b000173 | prose | pages [6] -->
2:06:20 1 0

<!-- b000174 | prose | pages [6] -->
2:14:53 0 1

<!-- b000175 | prose | pages [6] -->
2:28:21 1 0

<!-- b000176 | prose | pages [6] -->
2:53:10 1 0

<!-- b000177 | prose | pages [6] -->
2:55:10 1 0

<!-- b000178 | prose | pages [6] -->
3:05:04 0 0

<!-- b000179 | prose | pages [6] -->
3:13:12 1 0

<!-- b000180 | prose | pages [6] -->
3:22:58 1 0

<!-- b000181 | prose | pages [6] -->
3:28:08 0 1

<!-- b000182 | prose | pages [6] -->
3:33:45 1 0

<!-- b000183 | prose | pages [6] -->
rally_count speed_mph _fault

<!-- b000184 | prose | pages [6] -->
1 0 NA

<!-- b000185 | prose | pages [6] -->
1 0 NA

<!-- b000186 | prose | pages [6] -->
1 0 NA

<!-- b000187 | prose | pages [6] -->
1 0 NA

<!-- b000188 | prose | pages [6] -->
1 0 NA

<!-- b000189 | prose | pages [6] -->
1 0 NA

<!-- b000190 | prose | pages [6] -->
0 3 NA

<!-- b000191 | prose | pages [6] -->
1 0 NA

<!-- b000192 | prose | pages [6] -->
1 0 NA

<!-- b000193 | prose | pages [6] -->
1 0 NA

<!-- b000194 | prose | pages [6] -->
1 0 NA

<!-- b000195 | prose | pages [6] -->
From the table, it can be observed that when elapsed_time is 3:05:04, neither side committed a double fault, and thus, the recorded speed_mph as NA is considered a genuine missing value. The rally_count of 3 also supports this conclusion. In contrast, for other instances where speed_mph is NA, double faults occurred. Although speed_mph is recorded as missing, it should be imputed.

<!-- b000196 | prose | pages [6] -->
The nearest-neighbor interpolation method is employed for filling in missing values. This method is suitable for imputing missing values in time series data and typically does not introduce new data structures or models. It effectively preserves the original data distribution or characteristics. Similarly, the same method was used for data cleaning in other variables within the dataset.

<!-- b000197 | heading | pages [6] -->
3.2 Data Transformation

<!-- b000198 | prose | pages [6] -->
关注数学模型

<!-- b000199 | furniture | pages [6] -->
2

<!-- b000200 | furniture | pages [6] -->
MATHmodels

<!-- b000201 | furniture | pages [6] -->
获取更多资讯

<!-- b000202 | furniture | pages [7] -->
Team # 2403774                                                                                 Page 7 of 23

<!-- b000203 | furniture | pages [7] -->


<!-- b000204 | prose | pages [7] -->
In this study, some variables are unordered multicategorical variables represented as text in the dataset. Taking "winner_shot_type" as an example, it is represented as "F" for "Forehand Winner," "B" for "Backhand Winner," and "0" for "Other Winner." Analysis reveals that it belongs to an unordered multicategorical variable. From a numerical perspective, assigning values 1, 2, and 3 would imply an ordinal relationship, which is not accurate. In reality, the methods of winning are

<!-- b000205 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000206 | prose | pages [7] -->
independent and do not have a hierarchical order. Assigning values of 1, 2, and 3 and incorporating them into the model would be inappropriate, so they need to be transformed into dummy variables.

<!-- b000207 | prose | pages [7] -->
For example, with regard to the "winner_shot_type" variable, there are three possible values: "F" is transformed into {0, 1}, "B" into {0, 1}, and "0" into {0, 0}. Similarly, other variables are transformed using the same method.

<!-- b000208 | heading | pages [7] -->
3.3 Feature Recombination

<!-- b000209 | prose | pages [7] -->
As shown in Table 3, based on the dataset and in accordance with the rules of tennis matches, the following 36 sets of variables are selected as potential independent variables that may affect momentum. These independent variables are categorized into three types based on the time scale: current time, previous shot time, and long-term time. The independent variables included in the long- term time category are calculated based on existing data and encompass various information related to the same game, set, and match.

<!-- b000210 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000211 | prose | pages [7] -->
Tabel 3: Variable - Symbol comparison table

<!-- b000212 | prose | pages [7] -->
Instantaneous Calculated Variables

<!-- b000213 | heading | pages [7] -->
Symbols

<!-- b000214 | prose | pages [7] -->
Instantaneous Local Variable Current server Current serve count Current serve speed Current serve width Current serve depth Rounds taken for current game score Current return depth Current set count Current game count server serve_no speed_mph serve_width serve_depth rally_count return_depth set_no game_no Historical Instant Variable Previous point's score Point_Score Previous point's score without touch during serve, option 1 Serve_No_Touch_1 Previous point's score without touch during serve, option 2 Serve_No_Touch_2 Previous point's score without touch during rally, option 1 Rally_No_Touch_1 Previous point's score without touch during rally, option 2 Previous point's no-touch win type Previous point's running distance, option 1 Previous point's running distance, option 2

<!-- b000215 | furniture | pages [7] -->


<!-- b000216 | prose | pages [7] -->
Time Interval Calculated Variables

<!-- b000217 | prose | pages [7] -->
Rally_No_Touch_2 Win_Type Serve_No_Touch_1 Serve_No_Touch_2

<!-- b000218 | heading | pages [7] -->
Symbols

<!-- b000219 | prose | pages [7] -->
Set Level Interval Variable Current set's athlete's consecutive points won, option 1 Consecutive_1 Current set's athlete's consecutive points won, option 2 Number of games won in the current set, option 1 Consecutive_2 Games_1

<!-- b000220 | prose | pages [7] -->
关注数学模型

<!-- b000221 | furniture | pages [7] -->
2

<!-- b000222 | furniture | pages [7] -->
MATHmodels

<!-- b000223 | furniture | pages [7] -->
获取更多资讯

<!-- b000224 | furniture | pages [8] -->
Team # 2403774                                                                                 Page 8 of 23

<!-- b000225 | furniture | pages [8] -->


<!-- b000226 | prose | pages [8] -->
Number of games won in the current set, option 2 Number of double faults in this set, option 1 Number of double faults in this set, option 2 Number of unforced errors in this set, option 1 Games_2 Double_Faults_1 Double_Faults_2 Unforced_Errors_1

<!-- b000227 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000228 | prose | pages [8] -->
Number of unforced errors in this set, option 2 Number of net touches in this set, option 1 Number of net touches in this set, option 2 Current match's points lead progress Unforced_Errors_2 Net_Touches_1 Net_Touches_2 Lead_Progress Game Level Interval Variable Total distance covered in this match, option 1 Total distance covered in this match, option 2 Total_Distance_1 Total_Distance_2 Number of break points won by the athlete in this match, option 1 Break_Points_Won_1 Number of break points won by the athlete in this match, option 2 Break_Points_Won_2 Number of break points lost by the athlete in this match, option 1 Break_Points_Lost_1 Number of break points lost by the athlete in this match, option 2 Break_Points_Lost_2

<!-- b000229 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000230 | prose | pages [8] -->
Point Level Interval Variable Total distance covered in this match, option 1 Total distance covered in this match, option 2

<!-- b000231 | heading | pages [8] -->
3.4 Variable Selection

<!-- b000232 | prose | pages [8] -->
Total_Distance_Match_1 Total_Distance_Match_2

<!-- b000233 | prose | pages [8] -->
In the initial selection of variables, comprehensive coverage of the model was considered, but there may be some correlations among certain variables. To further improve the operational efficiency and simplicity of the model, a correlation analysis[1] was conducted on the variables intended for inclusion in the model. As shown in Figure 4, the confusion matrix[11] of variables clearly reveals the presence of high correlations among variables. Therefore, variable selection[2] based on correlation is necessary.

<!-- b000234 | furniture | pages [8] -->


<!-- b000235 | caption | pages [8] -->
Figure 4: Confusion matrix plot of variables

<!-- b000236 | heading | pages [8] -->
3.4.1 Correlation Analysis

<!-- b000237 | prose | pages [8] -->
The Spearman rank correlation coefficient[10] is a non-parametric statistical measure suitable for testing the correlation of abnormal distribution or ordered categorical data variables. The autocorrelations among the independent variables are calculated as shown in Figure 5. Based on this,

<!-- b000238 | prose | pages [8] -->
关注数学模型

<!-- b000239 | furniture | pages [8] -->
2

<!-- b000240 | furniture | pages [8] -->
MATHmodels

<!-- b000241 | furniture | pages [8] -->
获取更多资讯

<!-- b000242 | furniture | pages [9] -->
Team # 2403774                                                                                 Page 9 of 23

<!-- b000243 | furniture | pages [9] -->


<!-- b000244 | prose | pages [9] -->
some variables[3,4] with high autocorrelations in the figure were removed. For example, "set_no" showed strong correlations with "Games_1," "Games_2," "Total_Distance_Match_1," and "Total_Distance_Match_2." We chose "Total_Distance_Match_1" as the final independent variable, reflecting the player 1's energy consumption, and removed the other variables.

<!-- b000245 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000246 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000247 | furniture | pages [9] -->


<!-- b000248 | caption | pages [9] -->
Figure 5: The degree of self-correlation between independent variables

<!-- b000249 | heading | pages [9] -->
3.4.2 Variable Importance Ranking

<!-- b000250 | prose | pages [9] -->
After removing linearly correlated variables, there were still many variables, and not all of them had a significant impact on the model's results. To improve computational efficiency and further rank the importance of independent variables, the variables were sorted based on their impact on the dependent variable, which is whether the match is scored. Variables were sequentially removed from the smallest impact factor to the largest until a significant difference in model accuracy occurred.

<!-- b000251 | prose | pages [9] -->
When the variable "set_no" was removed, the classification accuracy decreased significantly from 95.5% to 66.1%. Therefore, the removal of independent variables was terminated at this point. The final selection of independent variables includes the following: server, Consecutive_2, Double_Faults_1, Consecutive_1, Net_Touches_2, Net_Touches_1, Double_Faults_2, Unforced_Errors_2, Point_Score, Lead_Progress, Unforced_Errors_1, Break_Points_Won_1, Serve_No_Touch_2, Break_Points_Won_2, Serve_No_Touch_1, Rally_No_Touch_1, return_depth, and Total_Distance_Match_1.

<!-- b000252 | furniture | pages [9] -->


<!-- b000253 | caption | pages [9] -->
Figure 6: The correlation ranking of different independent variables with the dependent variable

<!-- b000254 | prose | pages [9] -->
关注数学模型

<!-- b000255 | furniture | pages [9] -->
2

<!-- b000256 | furniture | pages [9] -->
MATHmodels

<!-- b000257 | furniture | pages [9] -->
获取更多资讯

<!-- b000258 | furniture | pages [10] -->
Team # 2403774                                                                                 Page 10 of 23

<!-- b000259 | furniture | pages [10] -->


<!-- b000260 | heading | pages [10] -->
4 Task 1: Momentum quantization and prediction model

<!-- b000261 | prose | pages [10] -->
In this section, we first define and quantify momentum. Then, we identify which player performs better and to what extent at specific moments in the game by building an XGBoost momentum prediction model.

<!-- b000262 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000263 | heading | pages [10] -->
4.1 Definition and Quantification of Momentum

<!-- b000264 | prose | pages [10] -->
We define momentum as follows: Momentum is implicitly embedded in the game state, explicitly reflecting the continuous scoring and losing in the game results. We make the following assumption: if the game state is related to scoring and losing, it can be reflected through momentum, completing the mapping from the distribution of game states to the distribution of scoring situations, establishing a relationship between the two distributions; conversely, if there is no relationship between them, such a mapping would be impossible to achieve.

<!-- b000265 | prose | pages [10] -->
Let the current game result sequence be 𝑃= {𝑃0, 𝑃1, … , 𝑃𝑁}, and the current moment be i, with N samples in total. We aim to estimate a player's momentum at moment 𝑖 by considering the game results in the vicinity of moment i. First, we need to create a window around moment i to capture the game's state within a short time frame. Next, we assign weights to these game results within the window, with results closer to the moment i contributing more significantly to momentum estimation,

<!-- b000266 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000267 | prose | pages [10] -->
while data from more distant matches have a smaller contribution.

<!-- b000268 | prose | pages [10] -->
Considering that in tennis matches, the serving player has a higher probability of winning points, we introduce a serving momentum factor, denoted as 𝑀𝑓, to adjust the momentum labels. When Player 1 serves, they gain an initial energy boost, and vice versa, they lose some energy when receiving. Both the gained and lost momentum are controlled by the momentum factor. Therefore, the momentum label formula can be expressed as follows:

<!-- b000269 | prose | pages [10] -->
𝑌𝑖= ( 𝑚

<!-- b000270 | prose | pages [10] -->
) (1 −𝑀𝑡) + 𝑀𝑡, 𝑀𝑡= 0.1

<!-- b000271 | prose | pages [10] -->
𝑀𝑚0

<!-- b000272 | prose | pages [10] -->
(4)

<!-- b000273 | heading | pages [10] -->
4.2 XGBoost-Based Momentum Quatification Model

<!-- b000274 | prose | pages [10] -->
Due to the non-linearity between independent variables and the final outcome of the game, we chose to use machine learning methods to discover the underlying relationship between independent and dependent variables. After considering various machine learning models, we opted for XGBoost for momentum prediction. XGBoost[8,9] utilizes an optimized distributed gradient boosting algorithm that allows rapid training of large-scale datasets while maintaining efficient resource utilization.

<!-- b000275 | prose | pages [10] -->
The construction and solution steps of the XGBoost momentum prediction model are as follows: (1) Data Preprocessing Before constructing the model, while maintaining the consistency of data distribution, the original dataset is initially divided into a training set S (80%) and a test set T (20%). The model is trained on S and the model's generalization ability is tested on T. For the training set S, further p-fold k-fold cross-validation is applied, where S is randomly divided into k subsets, and in each iteration, k-1 subsets are used for training, while the remaining one is used for validation. To reduce errors due to different sample divisions, this process is repeated p times, resulting in the average of p+k validation results as the model evaluation result. In this study, p=5 and k=5, meaning 5 times 5-fold cross-validation was utilized.

<!-- b000276 | prose | pages [10] -->
(2) Basis Function Construction XGBoost gradually adds new models in each iteration to expand its understanding of new data. Its formula is as follows:

<!-- b000277 | prose | pages [10] -->
(5) 𝑀𝑏= 𝑀𝑏−1 + 𝜂∙𝑇𝑏 (3) Definition of Loss Function The goal of XGBoost training is to minimize the loss function, which includes both traditional loss functions and regularization terms that describe model complexity.

<!-- b000278 | prose | pages [10] -->
关注数学模型

<!-- b000279 | furniture | pages [10] -->
2

<!-- b000280 | furniture | pages [10] -->
MATHmodels

<!-- b000281 | furniture | pages [10] -->
获取更多资讯

<!-- b000282 | furniture | pages [11] -->
Team # 2403774                                                                                 Page 11 of 23

<!-- b000283 | furniture | pages [11] -->


<!-- b000284 | prose | pages [11] -->
𝑚

<!-- b000285 | prose | pages [11] -->
min 𝑂𝑏𝑗= ∑𝑙(𝑦𝑖, 𝑦̂𝑖

<!-- b000286 | prose | pages [11] -->
𝑖=1

<!-- b000287 | prose | pages [11] -->
(𝑡−1) + 𝑓𝑖(𝑥𝑖)) + 𝛺(𝑓𝑘)

<!-- b000288 | prose | pages [11] -->
(6)

<!-- b000289 | prose | pages [11] -->
In the formula, the first term represents the difference between the momentum predicted by the model and the momentum calculated based on game results, while the second term represents the

<!-- b000290 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000291 | prose | pages [11] -->
model's complexity. In the above formula, {i} represents the number of samples in the dataset, and {m} represents the total number of samples in the dataset. {γ} and {λ} are used to adjust the complexity of the tree. The regularization term can smooth the final learning weight and prevent overfitting, improving the generalization ability of momentum prediction across matches and players.

<!-- b000292 | prose | pages [11] -->
(4) Momentum Error Prediction Predicting the momentum can be considered a regression task. In each optimization step, the model minimizes the mean squared error (MSE) between the predicted momentum and the labeled momentum, defined as follows:

<!-- b000293 | prose | pages [11] -->
(𝑡)) =

<!-- b000294 | furniture | pages [11] -->


<!-- b000295 | prose | pages [11] -->
𝑙(𝑦𝑖, 𝑌̂𝑖

<!-- b000296 | prose | pages [11] -->
2

<!-- b000297 | prose | pages [11] -->
1 1

<!-- b000298 | prose | pages [11] -->
(𝑡))

<!-- b000299 | furniture | pages [11] -->


<!-- b000300 | prose | pages [11] -->
(7)

<!-- b000301 | prose | pages [11] -->
2 (𝑦𝑖−𝑌̂𝑖

<!-- b000302 | prose | pages [11] -->
(𝑡)} represents the momentum

<!-- b000303 | prose | pages [11] -->
In the formula, {𝑦𝑖 } represents the label of momentum, {𝑌̂𝑖

<!-- b000304 | prose | pages [11] -->
prediction of the model in t iterations

<!-- b000305 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000306 | prose | pages [11] -->
(5) Structural Regularization Term Calculation The formula for calculating the regularization term is as follows:

<!-- b000307 | prose | pages [11] -->
𝑇

<!-- b000308 | prose | pages [11] -->
𝛺(𝑓𝑡) = 𝛾𝑇+ 1

<!-- b000309 | prose | pages [11] -->
2

<!-- b000310 | prose | pages [11] -->
(8)

<!-- b000311 | prose | pages [11] -->
2 𝜆∑𝑤𝑗

<!-- b000312 | prose | pages [11] -->
𝑗=1

<!-- b000313 | prose | pages [11] -->
In the formula, the hyperparameters {γ} and {λ} control the strength of the penalty, {T} represents the current number of leaf nodes in the regression tree, and the last term is the L2 norm of the leaf node values.

<!-- b000314 | prose | pages [11] -->
Based on the MSE loss function, pseudo-residuals can be derived and expressed as:

<!-- b000315 | prose | pages [11] -->
(𝑏−1))

<!-- b000316 | prose | pages [11] -->
𝜕𝑙(𝑦𝑖, 𝑦̂𝑖

<!-- b000317 | prose | pages [11] -->
𝑟𝑖𝑏= −[

<!-- b000318 | prose | pages [11] -->
(𝑏−1)

<!-- b000319 | prose | pages [11] -->
𝜕𝑦̂𝑖

<!-- b000320 | prose | pages [11] -->
(𝑏−1) (9)

<!-- b000321 | prose | pages [11] -->
] = 𝑦𝑖−𝑦̂𝑖

<!-- b000322 | prose | pages [11] -->
In each iteration of the model, these pseudo-residuals are used as gradients of the loss function with respect to the model predictions to train new decision trees. This way, each iteration of the model attempts to correct the prediction errors of the previous iteration.

<!-- b000323 | prose | pages [11] -->
(6) Momentum Prediction Model Construction In summary, our model can be summarized as follows:

<!-- b000324 | prose | pages [11] -->
𝑚

<!-- b000325 | prose | pages [11] -->
𝑚𝑖𝑛 𝑂𝑏𝑗= ∑𝑙(𝑦𝑖, 𝑦̂𝑖

<!-- b000326 | prose | pages [11] -->
𝑖=1

<!-- b000327 | prose | pages [11] -->
𝐾 𝑦̂𝑖= ∑

<!-- b000328 | prose | pages [11] -->
(𝑡−1) + 𝑓𝑖(𝑥𝑖)) + 𝛺(𝑓𝑘)

<!-- b000329 | furniture | pages [11] -->


<!-- b000330 | prose | pages [11] -->
𝑓𝑘(𝑥𝑖) 𝑘=1

<!-- b000331 | furniture | pages [11] -->


<!-- b000332 | prose | pages [11] -->
𝛺(𝑓𝑘) = 𝛾𝑇+

<!-- b000333 | furniture | pages [11] -->


<!-- b000334 | prose | pages [11] -->
1

<!-- b000335 | prose | pages [11] -->
(𝑡)) =

<!-- b000336 | prose | pages [11] -->
, 𝑓𝑘∈𝜑

<!-- b000337 | prose | pages [11] -->
1

<!-- b000338 | prose | pages [11] -->
2 𝜆𝑤2

<!-- b000339 | prose | pages [11] -->
(10)

<!-- b000340 | prose | pages [11] -->
(𝑡))2 2 (𝑦𝑖−𝑌̂𝑖

<!-- b000341 | prose | pages [11] -->
𝑙(𝑦𝑖, 𝑌̂𝑖

<!-- b000342 | furniture | pages [11] -->


<!-- b000343 | furniture | pages [11] -->


<!-- b000344 | prose | pages [11] -->
𝑚

<!-- b000345 | prose | pages [11] -->
𝑀𝑚0) (1 −𝑀𝑡) + 𝑀𝑡, 𝑀𝑡= 0.1

<!-- b000346 | prose | pages [11] -->
𝑌𝑖= (

<!-- b000347 | prose | pages [11] -->
{

<!-- b000348 | prose | pages [11] -->
Based on the XGBoost model described above, we model the game data, where the input is the known information at the current time point. The optimization of the objective function aims to minimize the difference between the predicted probability of winning the next time step and the actual outcome.

<!-- b000349 | prose | pages [11] -->
关注数学模型

<!-- b000350 | furniture | pages [11] -->
2

<!-- b000351 | furniture | pages [11] -->
MATHmodels

<!-- b000352 | furniture | pages [11] -->
获取更多资讯

<!-- b000353 | furniture | pages [12] -->
Team # 2403774                                                                                 Page 12 of 23

<!-- b000354 | furniture | pages [12] -->


<!-- b000355 | heading | pages [12] -->
Algorithm: Momentum Quantization

<!-- b000356 | prose | pages [12] -->
Input: 𝑃[𝑖], 𝑠[𝑖], 𝑁, 𝑊 , 𝑋[𝑖]

<!-- b000357 | prose | pages [12] -->
Output: 𝑞[𝑖], 𝐺[𝑖]

<!-- b000358 | prose | pages [12] -->
W 𝑤=−𝑊 𝑒w 1  𝑀𝑚𝑜= ∑

<!-- b000359 | furniture | pages [12] -->


<!-- b000360 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000361 | prose | pages [12] -->
2  Initialize the model Mo with a constant value

<!-- b000362 | prose | pages [12] -->
3  e.g. the mean of the labels

<!-- b000363 | heading | pages [12] -->
4 for i ←0 to 𝑁 do

<!-- b000364 | prose | pages [12] -->
5    m←0;

<!-- b000365 | heading | pages [12] -->
6    for 𝑗←−𝑊 to W do

<!-- b000366 | heading | pages [12] -->
7        if 0 ⩽𝑖+ 𝑗< 𝑁 and ∣𝑠[𝑖+ 𝑗] −𝑠[𝑖] ∣⩽1 then

<!-- b000367 | prose | pages [12] -->
8            𝑚←𝑚+ 𝑒|𝑖+𝑗| ⋅𝑃[𝑖+ 𝑗];

<!-- b000368 | heading | pages [12] -->
9    end

<!-- b000369 | prose | pages [12] -->
𝑚 10   𝑌𝑖←

<!-- b000370 | prose | pages [12] -->
𝑀𝑚0 . (1 −𝑀𝑓) + 𝑀𝑓;

<!-- b000371 | prose | pages [12] -->
𝑡−1 𝑘=1 𝑓𝑘(𝑥𝑖) 11   Get the predicting 𝑌̂𝑖←∑

<!-- b000372 | furniture | pages [12] -->


<!-- b000373 | furniture | pages [12] -->


<!-- b000374 | prose | pages [12] -->
12   Get the pseudo-residual 𝑟𝑖←𝑌𝑖−𝑌̂𝑖

<!-- b000375 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000376 | prose | pages [12] -->
13   Fit a regression tree 𝑇𝑖 to the pseudo-residuals 𝑟𝑗.

<!-- b000377 | prose | pages [12] -->
14   Update the model 𝑀𝑖←𝑀𝑖−1 + 𝜂⋅𝑇𝑖.

<!-- b000378 | heading | pages [12] -->
15 end

<!-- b000379 | prose | pages [12] -->
In the above algorithm, we use the match data S for each time step and differentiate whether it is the same match based on the provided number of match sessions. In the algorithm, W represents the window size, and we use exponential weighting to weigh the match data within the window and accumulate contributions to the momentum estimation in m. To normalize the estimate of momentum, we calculate the normalization factor 𝑀𝑚𝑜 as the maximum momentum and map m to the range of 0-1. According to the above algorithm, we can obtain momentum labels for each time step based on match results, which are used to fit an XGBoost model to map from match data to estimated player potentials. The fitting of the XGBoost model first obtains predictions of the previous model on the data and then calculates pseudo-residuals based on the output and labels. Afterward, a new tree is obtained based on the pseudo-residual and the specified learning rate and added to the tree ensemble.

<!-- b000380 | prose | pages [12] -->
(7) Model Evaluation To assess the predictive accuracy of the model for momentum, we selected the Mean Square Error (MSE) as a performance metric. The MSE measures the difference between the model's predicted momentum and the momentum generated based on the matches. We performed 5-fold cross- validation, and the average MSE for the model was found to be 0.02.

<!-- b000381 | heading | pages [12] -->
4.3 Results Visualization and Analysis

<!-- b000382 | prose | pages [12] -->
As shown in Figure 7, we present the estimation of Player1's momentum and their score situation, which can be symmetrically deduced for Player2. Using the XGBoost-based momentum prediction model, we calculate the changes in their momentum. Due to significant fluctuations in the results and considering that momentum quantification results can be affected by external disturbances, the use of a Kalman filter effectively eliminates noise and jitter. Compared to the original momentum results, the results after Kalman filtering are smoother. The orange line in the graph represents records from matches starting from a score of 0 and scoring 100 times, where 1 indicates a score and 0 indicates no score. According to our definition, when the momentum remains consistently above 0.5, Player1 has a greater advantage; conversely, when it falls below 0.5, Player2 has a greater advantage. At the beginning, as shown in Box 1, Player1's estimated momentum increases, indicating continuous scoring in the game with fewer losses. Subsequently, there is a turning point in the estimated momentum, following multiple losses. Then, the momentum returns to a higher level, accompanied

<!-- b000383 | prose | pages [12] -->
关注数学模型

<!-- b000384 | furniture | pages [12] -->
2

<!-- b000385 | furniture | pages [12] -->
MATHmodels

<!-- b000386 | furniture | pages [12] -->
获取更多资讯

<!-- b000387 | furniture | pages [13] -->
Team # 2403774                                                                                 Page 13 of 23

<!-- b000388 | furniture | pages [13] -->


<!-- b000389 | prose | pages [13] -->
by multiple scores. In the later stages of the match, as shown in Box 2, the estimated momentum experiences a significant decline, followed by continuous losses for Player1. Even though there is 1 score, the estimated momentum continues to decline. This phenomenon demonstrates that our designed model can describe the potential scoring situation of players near a certain moment, which is the concept of momentum.

<!-- b000390 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000391 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000392 | furniture | pages [13] -->


<!-- b000393 | caption | pages [13] -->
Figure 7: Visualization of score and momentum quantification

<!-- b000394 | heading | pages [13] -->
5 Task 2: The Momentum-Outcome Connection

<!-- b000395 | prose | pages [13] -->
In this section, we first generate random match scenarios, including match feature states and match scores. Then we apply the XGBoost momentum prediction model established in question 1 to calculate potential energies for both real matches and random matches. Finally, we compare and evaluate the correlation between match states (match conditions, serve speed, etc.) and momentum by selecting multiple indicators.The results can demonstrate how momentum affects match scores.

<!-- b000396 | heading | pages [13] -->
5.1 Random Match Scenario Generation

<!-- b000397 | prose | pages [13] -->
The coach believes that match scores are independent of match states, such as player serves, which affect momentum. Based on this, we set out to generate random match states and random scores to simulate random match scenarios. As shown in Figure 8, to make random match scenarios as close as possible to real match rules, we randomly select values and options for features from a uniform distribution to create new random match states. Regarding match outcomes, we set the probability of random scores to be 50%, and each setting is independently and identically distributed. The generation of random matches is incremental, and match results, determining player victories and match completion, are calculated based on the number of sets, games, and points in a Wimbledon match.

<!-- b000398 | furniture | pages [13] -->


<!-- b000399 | caption | pages [13] -->
Figure 8: The process of generating random match scenarios

<!-- b000400 | heading | pages [13] -->
5.2 Analysis of the Impact of Momentum on Scores

<!-- b000401 | prose | pages [13] -->
We utilize multiple evaluation metrics to comprehensively assess and compare the predictive performance of the model. These metrics include Mean Square Error (MSE), Root Mean Square Error

<!-- b000402 | prose | pages [13] -->
关注数学模型

<!-- b000403 | furniture | pages [13] -->
2

<!-- b000404 | furniture | pages [13] -->
MATHmodels

<!-- b000405 | furniture | pages [13] -->
获取更多资讯

<!-- b000406 | furniture | pages [14] -->
Team # 2403774                                                                                 Page 14 of 23

<!-- b000407 | furniture | pages [14] -->


<!-- b000408 | prose | pages [14] -->
(RMSE), Mean Absolute Error (MAE), R-squared (R2), Adjusted R-squared (Adjusted R2), and Pearson Correlation Coefficient (Pearsonr). Their definitions and meanings can be found in Table 4.

<!-- b000409 | prose | pages [14] -->
Tabel 4: Explanation of Evaluation Metrics and Numerical Significance

<!-- b000410 | prose | pages [14] -->
Indicators Describes

<!-- b000411 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000412 | prose | pages [14] -->
A smaller MSE indicates that the model's predictions are closer

<!-- b000413 | prose | pages [14] -->
Mean Square Error

<!-- b000414 | prose | pages [14] -->
(MSE)

<!-- b000415 | prose | pages [14] -->
to the actual values

<!-- b000416 | prose | pages [14] -->
A smaller RMSE indicates higher accuracy in the model's

<!-- b000417 | prose | pages [14] -->
Root Mean Square

<!-- b000418 | prose | pages [14] -->
Error (RMSE)

<!-- b000419 | prose | pages [14] -->
predictions

<!-- b000420 | prose | pages [14] -->
A smaller MAE implies higher precision in the model's

<!-- b000421 | prose | pages [14] -->
Mean Absolute Error

<!-- b000422 | prose | pages [14] -->
(MAE)

<!-- b000423 | prose | pages [14] -->
Mean Absolute Error predictions

<!-- b000424 | prose | pages [14] -->
An R2 value closer to 1 indicates a better fit of the model. (R2)

<!-- b000425 | prose | pages [14] -->
A higher Adjusted R2 value suggests stronger explanatory

<!-- b000426 | prose | pages [14] -->
Adjusted R-squared

<!-- b000427 | prose | pages [14] -->
(Adjusted R2)

<!-- b000428 | prose | pages [14] -->
power of the model.

<!-- b000429 | prose | pages [14] -->
The Pearsonr value ranges from -1 to 1, where 1 represents a

<!-- b000430 | prose | pages [14] -->
Pearson Correlation

<!-- b000431 | prose | pages [14] -->
perfect positive correlation, -1 represents a perfect negative

<!-- b000432 | prose | pages [14] -->
Coefficient (Pearsonr)

<!-- b000433 | prose | pages [14] -->
correlation, and 0 represents no linear correlation.

<!-- b000434 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000435 | prose | pages [14] -->
As shown in Table 5, the numbers from 1301 to 1701 represent the real scenarios used, with scenario 10 excluded from the analysis due to missing data (details can be found in Section 3.1.2). The label "random" represents simulated random scenarios. Our model demonstrates significantly lower levels of estimation error, with MSE, RMSE, and MAE reflecting errors within the ranges of 3.554e-3 to 8.621e-3, 5.961e-2 to 9.285e-2, and 4.625e-2 to 7.478e-2, respectively. These values are much lower than the corresponding values under random scenarios, which are 0.125576, 0.354367, and 0.297229. This indicates that our model significantly outperforms traditional methods in terms of prediction accuracy and can provide more accurate predictions of actual values.

<!-- b000436 | prose | pages [14] -->
The R2 and Adjusted R2 values of our model fall within the ranges of 0.8602 to 0.9073 and 0.8594 to 0.9071, respectively, which are far higher than the values under random scenarios, which are -2.2744 and -2.28424. This result not only demonstrates the model's strong explanatory power for data variability but also shows its stable performance even when considering model complexity.

<!-- b000437 | prose | pages [14] -->
The Pearson correlation coefficient further confirms the strong positive linear relationship between our model and actual values, with values ranging from 0.9408 to 0.9591, deviating by only 0.002911. This indicates a very high linear consistency between our model's predictions and actual label values. In other words, as actual label values increase, the model's predictions also increase, and vice versa. This high level of linear relationship suggests that the model not only accurately predicts the magnitude of actual values but also maintains a consistent trend in predictions across different ranges of label values.

<!-- b000438 | prose | pages [14] -->
In contrast, the Pearson correlation coefficient for random scenarios is close to zero, indicating almost no linear relationship between its predictions and actual label values, failing to reflect the changing trends in actual label values.

<!-- b000439 | prose | pages [14] -->
In summary, a player's score in the match is not random, and momentum plays a significant role in the game.

<!-- b000440 | heading | pages [14] -->
Tabel 5: Evaluation of Consistency between Predicted Potential Energy and Match Results

<!-- b000441 | prose | pages [14] -->
match mse rmse mae 1301 0.005301 0.072808 0.057363 1302 0.004725 0.06874 0.055849 1303 0.005613 0.074917 0.059082 1304 0.005553 0.074516 0.058671 adjusted_r_squared r_squared ks_real 0.839388 0.838847 0.052323 0.866766 0.866097 0.331034 0.868931 0.867938 0.002346 0.880302 0.879945 0.052706

<!-- b000442 | prose | pages [14] -->
关注数学模型

<!-- b000443 | furniture | pages [14] -->
2

<!-- b000444 | furniture | pages [14] -->
MATHmodels

<!-- b000445 | furniture | pages [14] -->
获取更多资讯

<!-- b000446 | furniture | pages [15] -->
Team # 2403774                                                                                 Page 15 of 23

<!-- b000447 | furniture | pages [15] -->


<!-- b000448 | prose | pages [15] -->
1305 0.005473 0.073977 0.059918 1306 0.005082 0.071287 0.057995 1307 0.006592 0.081189 0.066523 1308 0.007664 0.087545 0.069851 0.872491 0.871969 0.065444 0.890007 0.889674 0.0915 0.851584 0.850939 0.018196 0.835557 0.834683 0.156663

<!-- b000449 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000450 | prose | pages [15] -->
1309 0.004817 0.069407 0.055093 1311 0.006264 0.079147 0.062545 1312 0.005775 0.075997 0.061332 … … … … 1701 0.003554 0.059614 0.046257 random 0.136022 0.368812 0.301388 0.871828 0.87122 0.365668 0.86502 0.864593 0.11801 0.844124 0.843553 0.206051 … … … 0.907333 0.907054 0.226841 -2.54679 -2.55744 9.25E-06

<!-- b000451 | prose | pages [15] -->
Using the XGBoost momentum prediction model built in question one, we calculate potential energies by substituting random match data into the model. If the predicted momentum from random data matches the variation in match scores, it proves that the score situation is random. Conversely, if there is no match between the predicted momentum and the score situation, it demonstrates that momentum can reflect a player's scoring situation over a certain period of time. As shown in Figure 9, the left-side data points represent predicted momentum, the right-side represents label momentum,

<!-- b000452 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000453 | prose | pages [15] -->
which is the momentum reflected by match results, and the lines in the middle indicate that the two numbers belong to the same moment. By comparing, it is observed that in real match situations, the lines in the graph are mostly parallel to the x-axis, indicating that predicted momentum can be well- mapped to match situations. This suggests that momentum to some extent reflects match outcomes. However, in the coach's perceived random match scenarios, the lines do not exhibit a clear correspondence, indicating that the model cannot map from match states to match scores. Consequently, it implies that momentum can be used to reflect a player's scoring changes over a certain period of time.

<!-- b000454 | furniture | pages [15] -->


<!-- b000455 | caption | pages [15] -->
Figure 9: The mapping between the predicted mometum and the momentum defined in the contest

<!-- b000456 | heading | pages [15] -->
6 Bayesian Inflection point Detection and Prediction

<!-- b000457 | heading | pages [15] -->
6.1 Bayesian Online Inflection point Detection Method for Identifying Inflection points

<!-- b000458 | heading | pages [15] -->
6.1.1 Principle

<!-- b000459 | prose | pages [15] -->
The core principle of the Bayesian online inflection point detection method[5,6,7] is to use Bayesian statistics to identify structural changes, or inflection points, in time series data. This method calculates the conditional probability of observed time series values at each time point to assess the likelihood of a inflection point occurring. Specifically, it assumes that the time series can be divided into several segments, with data within each segment following a certain statistical distribution, and differences in distribution parameters between different segments. By applying Bayesian rules to all observed data before each time point, the posterior probability of that point being a inflection point can be estimated. Subsequently, these posterior probabilities are used to infer the locations of inflection points: points where the probability significantly increases are considered as inflection

<!-- b000460 | prose | pages [15] -->
关注数学模型

<!-- b000461 | furniture | pages [15] -->
2

<!-- b000462 | furniture | pages [15] -->
MATHmodels

<!-- b000463 | furniture | pages [15] -->
获取更多资讯

<!-- b000464 | furniture | pages [16] -->
Team # 2403774                                                                                 Page 16 of 23

<!-- b000465 | furniture | pages [16] -->


<!-- b000466 | prose | pages [16] -->
points. This process is performed online, meaning that data can be processed one by one without waiting for the collection of the entire data sequence, enabling real-time inflection point detection.

<!-- b000467 | prose | pages [16] -->
1.Initialize

<!-- b000468 | prose | pages [16] -->
𝑃(𝑟0) = 𝑆̃(𝑟0) or 𝑃(𝑟0 = 0) = 1

<!-- b000469 | prose | pages [16] -->
(0) = 𝑣𝑝𝑟𝑖𝑜𝑟

<!-- b000470 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000471 | prose | pages [16] -->
𝑣1

<!-- b000472 | prose | pages [16] -->
(0) = 𝑥𝑝𝑟𝑖𝑜𝑟

<!-- b000473 | prose | pages [16] -->
𝑥1

<!-- b000474 | prose | pages [16] -->
2.Observe New Datum 𝑥𝑡 3.Evaluate Predictive Probability

<!-- b000475 | prose | pages [16] -->
(𝑟) = 𝑃(𝑥𝑡|𝑣𝑡

<!-- b000476 | prose | pages [16] -->
𝜋𝑡

<!-- b000477 | prose | pages [16] -->
4.Calculate Growth Probabilities

<!-- b000478 | prose | pages [16] -->
(𝑟), 𝑥𝑡

<!-- b000479 | prose | pages [16] -->
(𝑟))

<!-- b000480 | prose | pages [16] -->
(𝑟)(1 −𝐻(𝑟𝑡−1))

<!-- b000481 | prose | pages [16] -->
𝑃(𝑟𝑡= 𝑟𝑡−1 + 1, 𝑥1:𝑡) = 𝑃(𝑟𝑡−1, 𝑥1:𝑡−1)𝜋𝑡

<!-- b000482 | prose | pages [16] -->
5.Calculate Changepoint Probabilities

<!-- b000483 | prose | pages [16] -->
(𝑟)𝐻(𝑟𝑡−1)

<!-- b000484 | prose | pages [16] -->
𝑃(𝑟𝑡= 0 + 1, 𝑥1:𝑡) = ∑𝑃(𝑟𝑡−1, 𝑥1:𝑡−1)

<!-- b000485 | prose | pages [16] -->
𝑟𝑡−1

<!-- b000486 | prose | pages [16] -->
6.Calculate Evidence

<!-- b000487 | prose | pages [16] -->
𝜋𝑡

<!-- b000488 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000489 | furniture | pages [16] -->


<!-- b000490 | prose | pages [16] -->
𝑃(𝑥1:𝑡) = ∑𝑃(𝑟𝑡, 𝑥1:𝑡)

<!-- b000491 | prose | pages [16] -->
7.Determine Run Length Distribution

<!-- b000492 | prose | pages [16] -->
𝑟𝑡 𝑟𝑡

<!-- b000493 | prose | pages [16] -->
𝑃(𝑟𝑡|𝑥1:𝑡) = 𝑃(𝑟𝑡, 𝑥1:𝑡)/𝑃(𝑥1:𝑡) 8.Update Sufficient Statistics

<!-- b000494 | prose | pages [16] -->
(0) = 𝑣𝑝𝑟𝑖𝑜𝑟

<!-- b000495 | prose | pages [16] -->
𝑣𝑡+1

<!-- b000496 | prose | pages [16] -->
(0) = 𝑥𝑝𝑟𝑖𝑜𝑟

<!-- b000497 | prose | pages [16] -->
𝑥𝑡+1

<!-- b000498 | prose | pages [16] -->
(𝑟+1) = 𝑣𝑡

<!-- b000499 | prose | pages [16] -->
𝑣𝑡+1

<!-- b000500 | prose | pages [16] -->
(𝑟+1) = 𝑥𝑡

<!-- b000501 | prose | pages [16] -->
𝑥𝑡+1

<!-- b000502 | prose | pages [16] -->
9.Perform Prediction

<!-- b000503 | prose | pages [16] -->
(𝑟) + 1

<!-- b000504 | prose | pages [16] -->
(𝑟) + 𝑢(𝑥𝑡)

<!-- b000505 | prose | pages [16] -->
(𝑟))𝑃(𝑟𝑡|𝑥1:𝑡)

<!-- b000506 | furniture | pages [16] -->


<!-- b000507 | prose | pages [16] -->
𝑃(𝑥𝑡+1|𝑥1:𝑡) = ∑𝑃(𝑥𝑡+1|𝑥𝑡

<!-- b000508 | prose | pages [16] -->
𝑟𝑡

<!-- b000509 | prose | pages [16] -->
10.Return to Step 2

<!-- b000510 | prose | pages [16] -->
Here are the meanings of the variables involved: ⚫ 𝑃(𝑟0): The probability of initializing a inflection point (inflection point). δ(r) is the Dirac delta function, which equals 1 at r=0, and 0 otherwise. Alternatively, 𝑃(𝑟0 = 0) is set to 1, indicating that there are no inflection points initially. 𝑣(0)and𝑥(0): Initialization parameters for sufficient statistics, corresponding to prior knowledge ⚫ 𝑣𝑝𝑟𝑖𝑜𝑟 and 𝑥𝑝𝑟𝑖𝑜𝑟.

<!-- b000511 | prose | pages [16] -->
(𝑟) : The predicted probability calculated after observing new data 𝑥𝑡 . It represents the

<!-- b000512 | prose | pages [16] -->
⚫ 𝜋𝑡

<!-- b000513 | prose | pages [16] -->
probability of data x_t occurring given the current sufficient statistics and inflection point location. ⚫ 𝑃(𝑟𝑡= 𝑟+ 1|𝑥1:𝑡): Growth probability at time t for a inflection point. ⚫ 𝑃(𝑟𝑡= 0|𝑥1:𝑡): Inflection point probability at time t for resetting to 0. ⚫ 𝑃(𝑥1:𝑡): Evidence probability, representing the probability of observing the data sequence 𝑥1:𝑡 at time t. ⚫ 𝑃(𝑟𝑡|𝑥1:𝑡) : Run-length distribution, indicating the probability of the current run length being 𝑟𝑡given the data sequence 𝑥1:𝑡. 𝑣(𝑟+1) and 𝑥(𝑟+1): Updated parameters for sufficient statistics. ⚫

<!-- b000514 | prose | pages [16] -->
关注数学模型

<!-- b000515 | furniture | pages [16] -->
2

<!-- b000516 | furniture | pages [16] -->
MATHmodels

<!-- b000517 | furniture | pages [16] -->
获取更多资讯

<!-- b000518 | furniture | pages [17] -->
Team # 2403774                                                                                 Page 17 of 23

<!-- b000519 | furniture | pages [17] -->


<!-- b000520 | prose | pages [17] -->
⚫ 𝑃(𝑥𝑡+1|𝑥1:𝑡): The probability of predicting the next data point 𝑥𝑡+1 at time 𝑡+ 1.

<!-- b000521 | heading | pages [17] -->
6.1.2 Implementation Process

<!-- b000522 | prose | pages [17] -->
From the perspective of Player 1, we assigned one point for each victory and deducted one point for each loss. We conducted inflection point detection on Player 1's scoring trend using Bayesian online inflection point detection. We plotted the scoring trends and inflection point graphs for two matches

<!-- b000523 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000524 | prose | pages [17] -->
with match IDs 1407 and 1503, as shown in Figure 10 and Figure 11.

<!-- b000525 | furniture | pages [17] -->


<!-- b000526 | caption | pages [17] -->
Figure 10: The scoring trend and inflection point graph for Player 1 at matchid=1407&1503

<!-- b000527 | prose | pages [17] -->
The inflection points in the graph are presented as regions (through) rather than individual points

<!-- b000528 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000529 | prose | pages [17] -->
because inflection point detection typically provides a possible interval where structural changes might occur over a period of time. This represents a transitional phase rather than a discrete moment because real data may contain noise, and actual changes may occur gradually.

<!-- b000530 | prose | pages [17] -->
Taking Figure 10 as an example, based on the data in the table, when the first inflection point occurs, Player 2 made a double fault; when the second inflection point occurs, Player 1 scored a break point; when the third inflection point occurs, Player 2 scored a break point; when the fourth inflection point occurs, Player 1 scored a point without any touch. Subsequent inflection points also correspond to specific events, aligning with the facts. Therefore, we consider the approach of using Bayesian online inflection point detection to find inflection points as feasible.

<!-- b000531 | heading | pages [17] -->
6.2 Correlation Analysis of Inflection Points

<!-- b000532 | prose | pages [17] -->
Following the method outlined in Section 6.1, we detected the inflection point regions in the matches. We replaced the dependent variable with a binary variable, where 1 represents being in the inflection point region and 0 represents not being in the inflection point region. We then used the Spearman rank correlation coefficient method as described in Section 3.4.1 to calculate the correlation between independent variables and the dependent variable. Finally, we obtained the importance ranking of the 18 independent variables as shown in Figure 12.

<!-- b000533 | furniture | pages [17] -->


<!-- b000534 | caption | pages [17] -->
Figure 11: Independent Variable Importance Ranking

<!-- b000535 | prose | pages [17] -->
From the graph, it can be observed that the most important variable is the distance covered by the athlete, followed by whether both sides won a break point, and subsequently variables like the consecutive scoring streak. This result aligns with our expectations. Firstly, the distance covered by

<!-- b000536 | prose | pages [17] -->
关注数学模型

<!-- b000537 | furniture | pages [17] -->
2

<!-- b000538 | furniture | pages [17] -->
MATHmodels

<!-- b000539 | furniture | pages [17] -->
获取更多资讯

<!-- b000540 | furniture | pages [18] -->
Team # 2403774                                                                                 Page 18 of 23

<!-- b000541 | furniture | pages [18] -->


<!-- b000542 | prose | pages [18] -->
the athlete reflects the degree of physical exertion, with increasing distance indicating growing fatigue, which can lead to shifts in the game's momentum. Secondly, whether both sides won a break point is also a crucial factor affecting the game's trend. Winning a break point provides a boost to the player's morale and confidence while delivering a blow to the opponent's confidence. Therefore, it is considered a significant factor. Based on this, we believe that calculating the importance ranking of

<!-- b000543 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000544 | prose | pages [18] -->
independent variables using this method is feasible.

<!-- b000545 | heading | pages [18] -->
6.3 Tennis Match Point Temporal Convolutional Network

<!-- b000546 | prose | pages [18] -->
According to the Bayesian online inflection point detection model, we have obtained inflection point regions that are close to the Ground Truth in advance, as shown in Figure 13. We represent the inflection points using a binary model, where points within the inflection point regions are marked as 1, and the rest are marked as 0. Considering the time series nature of the data, we use a Temporal Convolutional Network (TCN) for inflection point prediction, treating it as a binary classification problem. TCN is a type of 1D convolutional model that incorporates the concept of convolution from CNN into sequential networks similar to RNN. In the TCN network, dilated causal convolutions are primarily used. This convolution is characterized by the inclusion of dilation in the regular convolution, aiming to increase the receptive field, as shown in Figure 13:

<!-- b000547 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000548 | prose | pages [18] -->
Causal Convolution refers to the type of convolution where the output at time t depends only on the information at and before time t and does not depend on information after time t. The diagram illustrates a typical causal convolution schematic.

<!-- b000549 | furniture | pages [18] -->


<!-- b000550 | caption | pages [18] -->
Figure 12: Dilated Conv   Figure 13: Causal Conv      Figure 14: MSTCN

<!-- b000551 | prose | pages [18] -->
Due to variations in the number of rounds in different matches, it is influenced by factors such as the skill gap between the competing sides and the game's status, both subjectively and objectively pleasing. Furthermore, the presence of winning streaks due to being in a hot state or losing streaks due to being in a low state is critical information for match outcomes. Therefore, in this chapter, based on TCN and considering the characteristics of tennis matches, we have designed a Multi-Stage Temporal Convolutional Network (MSTCN), as shown in Figure 15 below. The introduction of MSTCN aims to incorporate match information across multiple time scales simultaneously for model prediction.

<!-- b000552 | prose | pages [18] -->
Multi-time scale temporal convolution, when used in tennis match prediction, offers several advantages by integrating information from different time scales. These advantages can improve prediction accuracy, enhance model generalization capabilities, and better handle complex time series data. The summarized advantages are as follows:

<!-- b000553 | heading | pages [18] -->
6.3.1 Design Details

<!-- b000554 | prose | pages [18] -->
In this study, we employed a two-layer multi-scale temporal model as described above. We have input time series data X, where X[t] represents the observation at time step t. The model extracts features from the time series through convolution operations.

<!-- b000555 | prose | pages [18] -->
Multi-Scale Temporal Convolution Layer: The size of the first convolution kernel is k1=3, designed to capture features at shorter time scales;The size of the second convolution kernel is k2=5, intended for capturing features at

<!-- b000556 | prose | pages [18] -->
关注数学模型

<!-- b000557 | furniture | pages [18] -->
2

<!-- b000558 | furniture | pages [18] -->
MATHmodels

<!-- b000559 | furniture | pages [18] -->
获取更多资讯

<!-- b000560 | furniture | pages [19] -->
Team # 2403774                                                                                 Page 19 of 23

<!-- b000561 | furniture | pages [19] -->


<!-- b000562 | prose | pages [19] -->
intermediate time scales;The size of the third convolution kernel is k3=7, aimed at capturing features at longer time scales.

<!-- b000563 | prose | pages [19] -->
The formula for performing the convolution operation is as follows:

<!-- b000564 | prose | pages [19] -->
𝑍𝑖[𝑡] = 𝑓(𝑤𝑖∗𝑋[𝑡: 𝑡+ 𝑘𝑖] + 𝑏𝑖) for 𝑖= 1,2,3

<!-- b000565 | furniture | pages [19] -->


<!-- b000566 | prose | pages [19] -->
(11)

<!-- b000567 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000568 | prose | pages [19] -->
𝑃𝑖[𝑡] = 𝑔(𝑚𝑎𝑥(𝑓(𝑤𝑖∗𝑋[𝑡: 𝑡+ 𝑘𝑖] + 𝑏𝑖)[𝑡: 𝑡+ 𝑠])) for 𝑖= 1,2,3

<!-- b000569 | furniture | pages [19] -->


<!-- b000570 | prose | pages [19] -->
(12)

<!-- b000571 | prose | pages [19] -->
The equations represent a two-scale convolutional neural network layer followed by a max pooling operation. The convolutional layer computes features 𝑍1 ,  𝑍2 ,and  𝑍3 by applying kernel weights 𝑊1,𝑊2,and 𝑊3and adding biases 𝑏1, 𝑏2,and 𝑏3,respectively, with a Re LU activation function f. The subsequent pooling layer reduces dimensionality with a max pooling function g over a window sizes, resulting in pooled features 𝑃1, 𝑃2,and 𝑃3.

<!-- b000572 | prose | pages [19] -->
After the pooling layer, a fully connected layer is added to learn high-level representations of the time series.

<!-- b000573 | prose | pages [19] -->
𝑌[𝑡] = ℎ(𝑊𝑓𝑐∗𝑃1[𝑡] + 𝑏𝑓𝑐)

<!-- b000574 | furniture | pages [19] -->


<!-- b000575 | prose | pages [19] -->
In this context: 𝑌[𝑡] is the model's output.

<!-- b000576 | prose | pages [19] -->
(13)

<!-- b000577 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000578 | prose | pages [19] -->
ℎ is the activation function of the fully connected layer. 𝑊𝑓𝑐 and 𝑏𝑓𝑐 are the weights and bias terms of the fully connected layer.

<!-- b000579 | prose | pages [19] -->
The two-layer multi-scale temporal convolutional network follows the same design approach. The model's hyperparameters are defined as follows:

<!-- b000580 | prose | pages [19] -->
Tabel 6:experimental parameter setting details

<!-- b000581 | prose | pages [19] -->
Name Illustration Epoch Total epoches in training Value 10 The number of input video in a batch Batch_Size 6 The learning rate for optimizer Leaning-Rate le-4 The optimizer used in our experiment Optimizer

<!-- b000582 | heading | pages [19] -->
6.3.3 Results

<!-- b000583 | prose | pages [19] -->
Adam

<!-- b000584 | prose | pages [19] -->
In this section, we conducted experiments to classify whether tennis matches belong to the transition point region. Model evaluation was performed using five-fold cross-validation, and the predictive accuracies for fivea runs were 75.49%, 74.94%, 75.70%, 73.98%, and 73.83%, with an average accuracy of 74.79%.

<!-- b000585 | heading | pages [19] -->
6.4 Suggestions

<!-- b000586 | prose | pages [19] -->
Based on the performance evaluation of the multi-scale temporal convolutional network model mentioned above, we can observe that the model achieves an average accuracy of approximately 74.79% in predicting tennis match turning points. This indicates that the model has a certain degree of reliability and can predict key turning points in matches relatively accurately. Based on this, I suggest that tennis coaches can use this model to assist in training and match strategy development: ⚫ Match Preparation: Coaches can use the model's predictions to prepare strategies for potential turning points. Understanding possible turning points in a match can help players better prepare mentally and technically to face these critical moments. For example, if a break point has a significant impact on turning points, coaches can advise players to stay focused when facing break points from their opponents, delaying the arrival of a turning point. ⚫ Targeted Training: Using the features identified by the model as turning points, coaches can design specific training plans to enhance a player's performance during these critical moments. For instance, by simulating training scenarios related to turning points, coaches can improve a

<!-- b000587 | prose | pages [19] -->
关注数学模型

<!-- b000588 | furniture | pages [19] -->
2

<!-- b000589 | furniture | pages [19] -->
MATHmodels

<!-- b000590 | furniture | pages [19] -->
获取更多资讯

<!-- b000591 | furniture | pages [20] -->
Team # 2403774                                                                                 Page 20 of 23

<!-- b000592 | furniture | pages [20] -->


<!-- b000593 | prose | pages [20] -->
player's mental resilience and adaptability. ⚫ Strategy Adjustments: During the course of a match, coaches can also make timely adjustments to the game plan based on the model's predictions. For example, when approaching a predicted turning point, coaches can guide players to adopt a more conservative or aggressive playing style to respond to potential changes in the match dynamics.

<!-- b000594 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000595 | heading | pages [20] -->
7 Task 4: Model Validation and Evaluation

<!-- b000596 | heading | pages [20] -->
7.1 Model Validation with Other Matches and Accuracy

<!-- b000597 | prose | pages [20] -->
We obtained tennis match data for the 2023 Wimbledon Women's Singles[12,13] from the internet. We initially performed autocorrelation analysis on the independent variables in this dataset using the Spearman correlation coefficient matrix method. The results of this analysis are shown in Figure X:

<!-- b000598 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000599 | furniture | pages [20] -->


<!-- b000600 | caption | pages [20] -->
Figure 15: Autocorrelation among independent variables in women's singles

<!-- b000601 | prose | pages [20] -->
After removing strongly autocorrelated independent variables, we further filtered the independent variables based on their correlation with the dependent variable. The final ranking of the correlation between the selected independent variables and the dependent variable is shown in Figure X:

<!-- b000602 | furniture | pages [20] -->


<!-- b000603 | caption | pages [20] -->
Figure 16: Correlation ranking of different independent variables with the dependent variable

<!-- b000604 | prose | pages [20] -->
Using the selected independent variables, we reran the XGBoost-based potential quantification model and obtained momentum estimates and their corresponding scores for the 2023 Wimbledon women's singles matches, as shown in Figure 17:

<!-- b000605 | furniture | pages [20] -->


<!-- b000606 | prose | pages [20] -->
关注数学模型

<!-- b000607 | furniture | pages [20] -->
2

<!-- b000608 | furniture | pages [20] -->
MATHmodels

<!-- b000609 | furniture | pages [20] -->
获取更多资讯

<!-- b000610 | furniture | pages [21] -->
Team # 2403774                                                                                 Page 21 of 23

<!-- b000611 | furniture | pages [21] -->


<!-- b000612 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000613 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000614 | furniture | pages [21] -->


<!-- b000615 | caption | pages [21] -->
Figure 17: Visualization of women's singles scores and potential quantification

<!-- b000616 | prose | pages [21] -->
In this simulation, the XGBoost potential energy prediction model achieved an MSE (Mean Squared Error) metric of 0.025, indicating a high level of accuracy.

<!-- b000617 | heading | pages [21] -->
7.2 Model Evaluation

<!-- b000618 | prose | pages [21] -->
From the results in section 7.1, it is evident that the model also demonstrates high accuracy in simulating other matches. If the model's accuracy were to decrease, we would consider the following scenarios: the partial elimination of influential independent variables during variable selection, the neglect of other highly influential independent variables in other matches, and more. We would address these issues through the following approaches:

<!-- b000619 | prose | pages [21] -->
1. Conduct residual analysis on the model to identify systematic biases or uncaptured nonlinear relationships within the model.

<!-- b000620 | prose | pages [21] -->
2. Introduce external data to retrain the model and enhance its predictive capabilities. 3. Perform error analysis on the model's performance to determine if issues arise from data quality problems such as missing values, outliers, or incorrect data labels.

<!-- b000621 | prose | pages [21] -->
4. Collaborate with domain experts to explore whether there are essential, yet overlooked factors or relationships.

<!-- b000622 | prose | pages [21] -->
Our model exhibits strong generality for other matches, as demonstrated in section 7.1, where women's singles data was used to verify its applicability. In various matches, as long as we possess sufficient independent variable data, we can retrain a suitable model with high precision.

<!-- b000623 | heading | pages [21] -->
8 Sensitivity Analysis

<!-- b000624 | prose | pages [21] -->
To validate the sensitivity of our model to variable changes, i.e., the impact of input variations on the output momentum estimates, we randomly selected some data points from the entire dataset and modified the values of certain variables, including serve speed and running distance. We compared the changes in predicted momentum and the probability of a turning point occurrence to investigate the model's sensitivity to input changes.

<!-- b000625 | prose | pages [21] -->
We randomly selected 10 data points from all the data, used the XGBoost momentum prediction model to estimate momentum, and altered the "speed_mph" variable by ±5%. The experimental results are shown in the left figure, indicating that increasing serve speed can enhance the kinetic energy of players by 2.9%, while decreasing it can reduce the kinetic energy of players by 2.1%.

<!-- b000626 | prose | pages [21] -->
关注数学模型

<!-- b000627 | furniture | pages [21] -->
2

<!-- b000628 | furniture | pages [21] -->
MATHmodels

<!-- b000629 | furniture | pages [21] -->
获取更多资讯

<!-- b000630 | furniture | pages [22] -->
Team # 2403774                                                                                 Page 22 of 23

<!-- b000631 | furniture | pages [22] -->


<!-- b000632 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000633 | furniture | pages [22] -->


<!-- b000634 | caption | pages [22] -->
Figure 18: Sensitivity Analysis

<!-- b000635 | prose | pages [22] -->
We also selected 10 data points where a turning point occurred and altered "Total_Distance_Match_1" for Player 1 by ±10%. We then used the model from Task 3 to compare the changes in the probability of a turning point occurrence. The experimental results indicate that when athletes increase their energy expenditure, it may increase the probability of a turning point occurring by 3.4%. Conversely, decreasing energy expenditure may reduce the probability of a

<!-- b000636 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000637 | prose | pages [22] -->
turning point occurring by 4.1%.

<!-- b000638 | heading | pages [22] -->
9 Advantages and Disadvantages Analysis

<!-- b000639 | heading | pages [22] -->
9.1 Advantages

<!-- b000640 | prose | pages [22] -->
(1) The model employed in this paper combines machine learning and deep learning technologies, demonstrating remarkable adaptability and versatility. These models can handle inconsistent game data parameter settings and optimize model parameters to match the characteristics of specific game data through an automated training process.

<!-- b000641 | prose | pages [22] -->
(2) This paper uses an XGBoost-based quantitative prediction model, which boasts fast training speed and efficient execution performance, optimizing computational speed through parallel processing. Additionally, XGBoost offers high flexibility, allowing for customized optimization goals and evaluation criteria, reducing overfitting risk through regularization, and

<!-- b000642 | furniture | pages [22] -->


<!-- b000643 | prose | pages [22] -->
enhancing model generalization.

<!-- b000644 | prose | pages [22] -->
(3) The experimental design of this paper utilizes a five-fold cross-validation strategy, which offers three main advantages: reducing overfitting risk, improving model generalization, and

<!-- b000645 | prose | pages [22] -->
providing reliable performance estimates.

<!-- b000646 | prose | pages [22] -->
(4) The advantages of the multi-timescale temporal convolutional model in tennis turning point prediction are summarized as follows: it can capture features at different time scales, enhance model generalization, improve the capture of time dependencies, and support irregular data sampling, ultimately improving prediction accuracy and model adaptability.

<!-- b000647 | heading | pages [22] -->
9.2 Disadvantages

<!-- b000648 | prose | pages [22] -->
(1) The model may not consider all relevant independent variables comprehensively, potentially leading to information omissions that could affect model accuracy.

<!-- b000649 | prose | pages [22] -->
(2) The multi-timescale temporal convolutional network may increase computational complexity. Since this model needs to simultaneously process information at multiple time scales, it may result in higher computational costs and resource requirements.

<!-- b000650 | furniture | pages [22] -->


<!-- b000651 | furniture | pages [22] -->


<!-- b000652 | prose | pages [22] -->
关注数学模型

<!-- b000653 | furniture | pages [22] -->
2

<!-- b000654 | furniture | pages [22] -->
MATHmodels

<!-- b000655 | furniture | pages [22] -->
获取更多资讯

<!-- b000656 | furniture | pages [23] -->
Team # 2403774                                                                                 Page 23 of 23

<!-- b000657 | furniture | pages [23] -->


<!-- b000658 | heading | pages [23] -->
References

<!-- b000659 | furniture | pages [23] -->


<!-- b000660 | references | pages [23] -->
[1] Shrestha N. Detecting multicollinearity in regression analysis[J]. American Journal of Applied

<!-- b000661 | references | pages [23] -->
Mathematics and Statistics, 2020, 8(2): 39-42.

<!-- b000662 | furniture | pages [23] -->


<!-- b000663 | furniture | pages [23] -->


<!-- b000664 | references | pages [23] -->
微信公众号：数学模型

<!-- b000665 | furniture | pages [23] -->


<!-- b000666 | references | pages [23] -->
[2] Daoud J I. Multicollinearity and regression analysis[C]//Journal of Physics: Conference Series.

<!-- b000667 | references | pages [23] -->
IOP Publishing, 2017, 949(1): 012009.

<!-- b000668 | furniture | pages [23] -->


<!-- b000669 | furniture | pages [23] -->


<!-- b000670 | references | pages [23] -->
[3] Yu H, Cui P, He Y, et al. Stable learning via sparse variable independence[C]//Proceedings of the

<!-- b000671 | references | pages [23] -->
AAAI Conference on Artificial Intelligence. 2023, 37(9): 10998-11006.

<!-- b000672 | furniture | pages [23] -->


<!-- b000673 | furniture | pages [23] -->


<!-- b000674 | references | pages [23] -->
[4] Lee K Y, Li B, Zhao H. Variable selection via additive conditional independence[J]. J

<!-- b000675 | references | pages [23] -->
ournal of

<!-- b000676 | references | pages [23] -->
the Royal Statistical Society Series B: Statistical Methodology, 2016, 78(5): 1037-1055.

<!-- b000677 | furniture | pages [23] -->


<!-- b000678 | furniture | pages [23] -->


<!-- b000679 | references | pages [23] -->
[5] Wang F, Li W, Padilla O H M, et al. Multilayer random dot product graphs: Estimation and online

<!-- b000680 | references | pages [23] -->
inflection point detection[J]. arXiv preprint arXiv:2306.15286, 2023.

<!-- b000681 | furniture | pages [23] -->


<!-- b000682 | furniture | pages [23] -->


<!-- b000683 | references | pages [23] -->
[6] Cao Z, Seeuws N, De Vos M, et al. Inflection point Detection in Multi-

<!-- b000684 | references | pages [23] -->
Channel Time Series Via

<!-- b000685 | references | pages [23] -->
a Time-Invariant Representation[J]. IEEE Transactions on Knowledge and Data Engineering,

<!-- b000686 | references | pages [23] -->
2023.

<!-- b000687 | furniture | pages [23] -->


<!-- b000688 | references | pages [23] -->
微信号：MATHmodels

<!-- b000689 | furniture | pages [23] -->


<!-- b000690 | references | pages [23] -->
[7] Sellier J, Dellaportas P. Bayesian online inflection point detection with Hilbert space

<!-- b000691 | references | pages [23] -->
approximate Student-t process[C]//International Conference on Machine Learning. PMLR, 2023:

<!-- b000692 | references | pages [23] -->
30553-30569.

<!-- b000693 | furniture | pages [23] -->


<!-- b000694 | furniture | pages [23] -->


<!-- b000695 | references | pages [23] -->
[8] Kadra A, Lindauer M, Hutter F, et al. Well-tuned simple nets excel on tabular datasets[J].

<!-- b000696 | references | pages [23] -->
Advances in neural information processing systems, 2021, 34: 23928-23941.

<!-- b000697 | furniture | pages [23] -->


<!-- b000698 | furniture | pages [23] -->


<!-- b000699 | references | pages [23] -->
[9] Kadra A, Lindauer M, Hutter F, et al. Well-tuned simple nets excel on tabular datasets[J].

<!-- b000700 | references | pages [23] -->
Advances in neural information processing systems, 2021, 34: 23928-23941.

<!-- b000701 | furniture | pages [23] -->


<!-- b000702 | furniture | pages [23] -->


<!-- b000703 | references | pages [23] -->
[10] Sedgwick P. Spearman’s rank correlation coefficient[J]. B, 2014, 349.

<!-- b000704 | furniture | pages [23] -->


<!-- b000705 | furniture | pages [23] -->


<!-- b000706 | references | pages [23] -->
[11] Heydarian M, Doyle T E, Samavi R. MLCM: Multi-label confusionmatrix[J]. IEEEAccess, 2022,

<!-- b000707 | references | pages [23] -->
10: 19083-19095.

<!-- b000708 | references | pages [23] -->
[12]

<!-- b000709 | references | pages [23] -->
Takahashi H, Okamura S, Murakami S. Performance analysis in tennis since 2000: A systematic

<!-- b000710 | references | pages [23] -->
review focused on the methods of data collection[J]. 2022.

<!-- b000711 | references | pages [23] -->
[13] Data-driven analysis of point-by-point performance for male tennis player in Grand Slams

<!-- b000712 | references | pages [23] -->
https://revistas.rcaap.pt/motricidade/article/view/16370.

<!-- b000713 | furniture | pages [23] -->


<!-- b000714 | furniture | pages [23] -->


<!-- b000715 | furniture | pages [23] -->


<!-- b000716 | furniture | pages [23] -->


<!-- b000717 | furniture | pages [23] -->


<!-- b000718 | furniture | pages [23] -->


<!-- b000719 | furniture | pages [23] -->


<!-- b000720 | furniture | pages [23] -->


<!-- b000721 | furniture | pages [23] -->


<!-- b000722 | furniture | pages [23] -->


<!-- b000723 | furniture | pages [23] -->


<!-- b000724 | furniture | pages [23] -->


<!-- b000725 | furniture | pages [23] -->


<!-- b000726 | furniture | pages [23] -->


<!-- b000727 | furniture | pages [23] -->


<!-- b000728 | references | pages [23] -->
关注数学模型

<!-- b000729 | furniture | pages [23] -->
2

<!-- b000730 | furniture | pages [23] -->
MATHmodels

<!-- b000731 | furniture | pages [23] -->
获取更多资讯

<!-- b000732 | references | pages [24] -->
Tennis

<!-- b000733 | furniture | pages [24] -->


<!-- b000734 | references | pages [24] -->
Dear Sir/Madam,

<!-- b000735 | furniture | pages [24] -->


<!-- b000736 | furniture | pages [24] -->


<!-- b000737 | references | pages [24] -->
微信公众号：数学模型

<!-- b000738 | references | pages [24] -->
I am writing to propose a visonary approach to tennis coaching that leverages advanced analytics and

<!-- b000739 | references | pages [24] -->
machine leaning to redefine our players' training and performance enhancement.

<!-- b000740 | references | pages [24] -->
Given the evolving comprtitive nature of tennis,it’s clear that traditional methods along can’t unlock our

<!-- b000741 | references | pages [24] -->
player’full potential. As data reshapes sports, our approach to coaching must adapt to maintain a leading edge.

<!-- b000742 | references | pages [24] -->
To achieve this, we undertook the following tasks:

<!-- b000743 | references | pages [24] -->
Firstly, we conducted data cleaning, feature extraction, an analysis of autocorrelation among independent

<!-- b000744 | references | pages [24] -->
variables, and ranked the correlation between independent and dependent variables.

<!-- b000745 | references | pages [24] -->
Next, we introduced the concept of "potential energy" and developed a potential energy prediction model

<!-- b000746 | references | pages [24] -->
based on the XGBoost algorithm. We quantified the relationship between independent variables and potential

<!-- b000747 | references | pages [24] -->
微信号：MATHmodels

<!-- b000748 | references | pages [24] -->
energy and visualized this quantitative relationship using visualization techniques.

<!-- b000749 | references | pages [24] -->
Subsequently,we simulated random match scenarios and analyzed the impact of potencial energy on

<!-- b000750 | references | pages [24] -->
scores. By calculating the Pearson correlation coefficient, we confirmed that player scores in matches are not r

<!-- b000751 | references | pages [24] -->
andom but are significantly influenced by potential energy.

<!-- b000752 | references | pages [24] -->
Furthermore, we applied Bayesian online change point detection methods to successfully identify crucial

<!-- b000753 | references | pages [24] -->
turning points in matches. We conducted correlation analyses of these change points, thereby determining the

<!-- b000754 | references | pages [24] -->
importance ranking of 18 independent variables.

<!-- b000755 | references | pages [24] -->
For further application,we developed the Tennis Match Point Time-Convolution Model,which can

<!-- b000756 | references | pages [24] -->
predict when critical turning points are likely to occur during matches.

<!-- b000757 | references | pages [24] -->
Finally,by analyzing data from the 2003 Wimbledon women’s singles match,we validated the wide

<!-- b000758 | references | pages [24] -->
applicability of our model and conducted comprehensive evaluations and sensitivity analyses.

<!-- b000759 | references | pages [24] -->
Our research not only serves as a reference for future studies in related fields ,but also provides practical

<!-- b000760 | references | pages [24] -->
tools. By applying our model, one can effectively monitor player potential energy, make timely strategy adjust

<!-- b000761 | references | pages [24] -->
-ments, predict changes in match dynamics, and be well-prepared for them.

<!-- b000762 | references | pages [24] -->
I believe that by implementing these datadriven strategies, we can transform our coaching into a high

<!-- b000763 | references | pages [24] -->
precision science, making us pioneers in the tennis coaching arena. This innovative approach will empower

<!-- b000764 | references | pages [24] -->
our players to reach unprecedented heights and achieve a competitive edge on the tennis court.I look forward

<!-- b000765 | references | pages [24] -->
to engaging in a dialogue to discuss these recommendations in depth and devise a roadmap for their seamless

<!-- b000766 | references | pages [24] -->
integration into our coaching philosophy.

<!-- b000767 | references | pages [24] -->
Warm regards,

<!-- b000768 | references | pages [24] -->
Bill

<!-- b000769 | furniture | pages [24] -->


<!-- b000770 | references | pages [24] -->
关注数学模型

<!-- b000771 | furniture | pages [24] -->
2

<!-- b000772 | furniture | pages [24] -->
MATHmodels

<!-- b000773 | furniture | pages [24] -->
获取更多资讯
