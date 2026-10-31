# P-C-2024-2403774-be4a823f

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
2403774

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
微信公众号：数学模型

<!-- b000009 | title | pages [1] -->
Uncovering the Hidden Momentum: A Data-Science Exploration of

<!-- b000010 | title | pages [1] -->
Tennis Match Dynamics

<!-- b000011 | prose | pages [1] -->
Tennis, as a comprehensive sport, has always been a subject of great interest. Besides the physical demands on athletes, exceptional skills and outstanding tactical strategies are key to victory. This study delves into the concept of "athletic potential" in competitive sports, an inherent vitality and advantage that becomes apparent during matches, utilizing data science and machine learning techniques. Ultimately, the data-driven insights derived from our models will provide valuable guidance and reference for coaches This article primarily establishes two models: the XGBoost-based Momentum Quantification Model and the Tennis Match Point Time-Convolution Model.

<!-- b000012 | title | pages [1] -->
微信号：MATHmodels

<!-- b000013 | prose | pages [1] -->
Before building the models, we initially conducted data preprocessing, including the identification of outliers and handling missing values using strategies such as the Interquartile Range (IQR). We also selectively removed or imputed data based on practical significance. Subsequently, we designed variables based on different timeframes (Current-Past) and various temporal scales (Short-Medium-Long). Finally, we used Spearman's correlation coefficient to eliminate variables with high correlations to the dependent variable and those exhibiting autocorrelation.

<!-- b000014 | heading | pages [1] -->
Addressing the first problem, this study introduces improvements to the XGBoost-based

<!-- b000015 | prose | pages [1] -->
momentum estimation of players. We establish a relationship between momentum and short-term match outcomes, achieving a precision MSE (Mean Square Error) indicator of 0.02 through a 5- fold cross- validation approach.

<!-- b000016 | prose | pages [1] -->
Regarding the second problem, we randomly generated match scenarios based on game rules and original data. We applied the model developed for problem one to estimate the momentum for both real and random matches. Ultimately, by comparing various metrics that measure the correlation between momentum and match outcomes, we provide strong evidence supporting the impact of momentum on match scores.

<!-- b000017 | prose | pages [1] -->
For the third problem, we utilized Bayesian online change-point detection methods to identify crucial turning points in matches, and we visualized the results using two sample matches. To accommodate the different temporal characteristics of match data, such as capturing immediate situations in short timeframes and understanding overall trends in long timeframes, we designed the Tennis Match Point Temporal Convolutional Network. This model achieved a Top-1 accuracy of 75.70% in predicting turning points.

<!-- b000018 | prose | pages [1] -->
Concerning the fourth problem, we conducted domain transfer testing using tennis match data from the 2023 Wimbledon Women's Singles. The momentum prediction achieved a precise MSE indicator of 0.025, demonstrating the high generalization performance of our model.

<!-- b000019 | prose | pages [1] -->
Additionally, we performed sensitivity analysis to explore the impact of input variations on the model. Finally, the strengths and weaknesses of our model are summarized. In conclusion, we include a letter to tennis coaches at the end of the article, introducing the overall concept and results of our research.

<!-- b000020 | keywords | pages [1] -->
Keywords: Tennis Athletic Potential, XGBoost, Momentum Quantification, Temporal

<!-- b000021 | prose | pages [1] -->
Convolutional Network

<!-- b000022 | prose | pages [1] -->
关注数学模型

<!-- b000023 | furniture | pages [1] -->
2

<!-- b000024 | furniture | pages [1] -->
MATHmodels

<!-- b000025 | furniture | pages [1] -->
获取更多资讯

<!-- b000026 | furniture | pages [2] -->
Team # 2403774                                                                                 Page 2 of 23

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1 Introduction .................................................................................................................................. 3

<!-- b000029 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000030 | contents | pages [2] -->
1.1 Background ............................................................................................................................ 3

<!-- b000031 | contents | pages [2] -->
1.2 Restatment of the Problem ..................................................................................................... 3

<!-- b000032 | contents | pages [2] -->
1.3 Our Work ................................................................................................................................ 3

<!-- b000033 | contents | pages [2] -->
2 Assumptions And Notations ........................................................................................................ 4

<!-- b000034 | contents | pages [2] -->
2.1 Assuptions .............................................................................................................................. 4

<!-- b000035 | contents | pages [2] -->
2.2 Notations ................................................................................................................................ 4

<!-- b000036 | contents | pages [2] -->
3 Data Preprocessing ....................................................................................................................... 5

<!-- b000037 | contents | pages [2] -->
3.1 Data Cleaning ......................................................................................................................... 5

<!-- b000038 | contents | pages [2] -->
3.2 Data Transformation .............................................................................................................. 6

<!-- b000039 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000040 | contents | pages [2] -->
3.3 Feature Recombination .......................................................................................................... 7

<!-- b000041 | contents | pages [2] -->
3.4 Variable Selection .................................................................................................................. 8

<!-- b000042 | contents | pages [2] -->
4 Task 1: Momentum quantization and prediction model ........................................................ 10

<!-- b000043 | contents | pages [2] -->
4.1 Definition and Quantification of Momentum ...................................................................... 10

<!-- b000044 | contents | pages [2] -->
4.2 XGBoost-Based Momentum Quatification Model .............................................................. 10

<!-- b000045 | contents | pages [2] -->
4.3 Results Visualization and Analysis ...................................................................................... 12

<!-- b000046 | contents | pages [2] -->
5 Task 2: The Momentum-Outcome Connection ....................................................................... 13

<!-- b000047 | contents | pages [2] -->
5.1 Random Match Scenario Generation ................................................................................... 13

<!-- b000048 | contents | pages [2] -->
5.2 Analysis of the Impact of Momentum on Scores ................................................................. 13

<!-- b000049 | contents | pages [2] -->
6 Bayesian Inflection point Detection and Prediction ................................................................ 15

<!-- b000050 | contents | pages [2] -->
6.1 Bayesian Online Inflection point Detection Method for Identifying Inflection points ........ 15

<!-- b000051 | contents | pages [2] -->
6.2 Correlation Analysis of Inflection Points ............................................................................. 17

<!-- b000052 | contents | pages [2] -->
6.3 Tennis Match Point Temporal Convolutional Network ....................................................... 18

<!-- b000053 | contents | pages [2] -->
6.4 Suggestions .......................................................................................................................... 19

<!-- b000054 | contents | pages [2] -->
7 Task 4: Model Validation and Evaluation ................................................................................ 20

<!-- b000055 | contents | pages [2] -->
7.1 Model Validation with Other Matches and Accuracy .......................................................... 20

<!-- b000056 | contents | pages [2] -->
7.2 Model Evaluation ................................................................................................................... 21

<!-- b000057 | contents | pages [2] -->
8 Sensitivity Analysis ..................................................................................................................... 21

<!-- b000058 | contents | pages [2] -->
9 Advantages and Disadvantages Analysis .................................................................................... 22

<!-- b000059 | contents | pages [2] -->
9.1 Advantages ............................................................................................................................. 22

<!-- b000060 | contents | pages [2] -->
9.2 Disadvantages ........................................................................................................................ 22

<!-- b000061 | contents | pages [2] -->
References ......................................................................................................................................... 23

<!-- b000062 | contents | pages [2] -->
关注数学模型

<!-- b000063 | furniture | pages [2] -->
2

<!-- b000064 | furniture | pages [2] -->
MATHmodels

<!-- b000065 | furniture | pages [2] -->
获取更多资讯

<!-- b000066 | furniture | pages [3] -->
Team # 2403774                                                                                 Page 3 of 23

<!-- b000067 | heading | pages [3] -->
1 Introduction

<!-- b000068 | heading | pages [3] -->
1.1 Background

<!-- b000069 | prose | pages [3] -->
"To become the first man in a decade to defeat Novak Djokovic on Centre Court at Wimbledon is truly a remarkable feat I'll always cherish," Alcaraz reflected on his historic win. 微信公众号：数学模型 In the gripping Wimbledon men's singles final of 2023, the prodigious 20-year-old Spaniard, Alcaraz, outplayed the venerable 36-year-old Serbian champion, Djokovic, in a five-set thriller to claim the prestigious title. Despite a rocky start, where Alcaraz dropped the first set 1-6, he tenaciously fought back to secure the match, leaving the audience in awe of the stunning upset.

<!-- b000070 | prose | pages [3] -->
Competitive momentum, within the realm of sports, represents the intrinsic vigor and edge that becomes apparent during a match. It denotes the collective strength and prowess of either a team or an individual athlete, which is instrumental in asserting dominance within the game.

<!-- b000071 | prose | pages [3] -->
To harness this competitive momentum, a diverse set of skills is crucial, encompassing technical prowess, tactical acumen, psychological resilience, and rigorous physical conditioning. Possession of such attributes enables athletes to elevate their performance, dominate the competition, and achieve superior results.

<!-- b000072 | prose | pages [3] -->
Despite its frequent mention in sports narratives, competitive momentum remains an elusive, 微信号：MATHmodels subjective concept, one that defies direct measurement through conventional statistical methods. Therefore, sports analysts and coaches are often inclined to leverage specific in-game data, such as points scored, service speed, error rates, and more, to construct models that endeavor to quantify the effects of momentum and forecast game trends and outcomes.

<!-- b000073 | heading | pages [3] -->
1.2 Restatment of the Problem

<!-- b000074 | prose | pages [3] -->
Through the analysis and investigation of the background and negotiators’ guidance of the problem, the restate of the problem can be expressed as follows: ⚫

<!-- b000075 | heading | pages [3] -->
Build a mathematic model for Match Flow Analysis:

<!-- b000076 | prose | pages [3] -->
✓ Create a model that captures the progression of a tennis match based on the scorning events.The model should be capable of identifying who is well-performed at any given moment, and quantify their level of superiority.

<!-- b000077 | prose | pages [3] -->
✓ Include a visualization that depicts the flow of the match, as informed by the model.

<!-- b000078 | prose | pages [3] -->
✓ Incorporate the advantage that players have while serving into the model. ⚫ Use the model to evaluate the claim by a tennis coach who doesn’t believe the role of “momentum”. ⚫ Predict Shifts in “Momentum”:

<!-- b000079 | prose | pages [3] -->
✓ Construct a model to forsee the pivotal moments that shifts the “momentum” of the game,and identify the key indicators that drive these shifts.

<!-- b000080 | prose | pages [3] -->
✓ Offer advise to a player entering a new match against a different opponent, based on the dynamics of “momentum” swings. ⚫

<!-- b000081 | heading | pages [3] -->
Model Testing:

<!-- b000082 | prose | pages [3] -->
✓ Test the model against additional matches to evaluate its effectiveness in forecasting momentum swings and the outcomes of games.

<!-- b000083 | prose | pages [3] -->
✓ Should the model display occasional inaccuracies, pinpoint elements that could be incorporated in future versions to enhance its predictive accuracy.

<!-- b000084 | prose | pages [3] -->
✓ Consider how the model might be adapted to other contexts, such as women's matches, different court surfaces, or other racket sports like table tennis. ⚫ Compose a one-to-two-page memo to be included in the report, offering advice to tennis coaches according to the study.

<!-- b000085 | heading | pages [3] -->
1.3 Our Work

<!-- b000086 | prose | pages [3, 4] -->
关注数学模型 In line with the background and research questions, our work encompasses the following aspects: (1) Data preprocessing to obtain the required independent variables for subsequent modeling. Establishing an XGBoost-based momentum quantification model to quantify and assess a player's performance at specific times, and visualizing the momentum in relation to match outcomes. (2) Simulating a random match to compare the momentum of a random match with that of a real 微信公众号：数学模型 match. Using Pearson correlation coefficients, we confirmed that a player's fluctuations and success during a match are not random but influenced by momentum. (3) Utilizing Bayesian online changepoint detection methods to identify turning points in each match and obtaining the importance ranking of independent variables through Spearman rank correlation. We then developed the Tennis Match Point Time-Convolution Model, which can predict when turning points are likely to occur. (4) Validating the model using data from other matches and conducting an evaluation of the model's performance.

<!-- b000087 | furniture | pages [3] -->
2

<!-- b000088 | furniture | pages [3] -->
MATHmodels

<!-- b000089 | furniture | pages [3] -->
获取更多资讯

<!-- b000090 | furniture | pages [4] -->
Team # 2403774                                                                                 Page 4 of 23

<!-- b000092 | heading | pages [4] -->
2 Assumptions And Notations

<!-- b000093 | heading | pages [4] -->
2.1 Assuptions

<!-- b000094 | prose | pages [4] -->
⚫ The sum of momentum of two players is constant. Momentum reflects a player's ability to 微信号：MATHmodels score against an opponent. Given the momentum of player 1, the momentum of player 2 can be derived symmetrically, which is conducive to describing the player's state. ⚫ The effect of momentum is primarily short-term. A player's momentum at a given moment may remain stable in a local time window and change with subsequent wins and losses. ⚫ There is a certain degree of momentum inheritance between each game, set and match. At the beginning of each game, the player will be somewhat affected by the situation of the previous game or the overall set and court, thus obtaining different initial momentum. ⚫ The impact of data outside the table on the match is ignored. The physical quality of athletes and other factors can be reflected in the information of the match given in the table, and other factors have a small impact and can be ignored. ⚫ The number of promotions a player makes may be unrelated to momentum. Both sides in each match have the same number of advances and similar physical exertion, so the effect of advance records on momentum is not taken into account. ⚫ The total distance run to some extent represents the value of physical exertion. It is common sense that the more an athlete runs, the greater the physical exertion.

<!-- b000095 | heading | pages [4] -->
2.2 Notations

<!-- b000096 | prose | pages [4] -->
Tabel 1:Symbols and Descriotions

<!-- b000097 | prose | pages [4, 5] -->
Symbol Description Current iteration step 𝑏 Ensemble of models 𝑀 Learning rate 𝜂 Number of samples in the dataset 𝑖 Total number of samples in the dataset 𝑚 Use to adjust the complexity of the tree. 𝛾,𝜆 Momentum based on match outcomes 𝑦𝑖 (𝑡) Model's prediction of momentum at iteration t 𝑌𝑖 Current number of leaf nodes in the regression tree 𝑇 Momentum of player i at time t 𝑌𝑖 关注数学模型 Maximum momentum 𝑀𝑚0 Serving momentum factor 𝑀𝑓=0.1 𝑀𝑓

<!-- b000098 | furniture | pages [4] -->
2

<!-- b000099 | furniture | pages [4] -->
MATHmodels

<!-- b000100 | furniture | pages [4] -->
获取更多资讯

<!-- b000101 | furniture | pages [5] -->
Team # 2403774                                                                                 Page 5 of 23

<!-- b000103 | heading | pages [5] -->
3 Data Preprocessing

<!-- b000104 | heading | pages [5] -->
3.1 Data Cleaning

<!-- b000105 | prose | pages [5] -->
微信公众号：数学模型 Due to the randomness of data and missing records from devices, it is necessary to clean the data. This involves correcting anomalies and filling in missing values to ensure the accuracy of subsequent analyses and the reliability of modeling. Taking the current serve speed column(speed_mph) and Player 1's running distance column (p1_distance_run) as examples, the methods and process of data cleaning are detailed as follows.

<!-- b000106 | heading | pages [5] -->
3.1.1 Correction of Anomalous Values

<!-- b000107 | prose | pages [5] -->
Due to the randomness in data collection, there may be outliers in the samples that significantly differ from the majority of the values, thus it requirs repair or removal. Use the Interquartile Range (IQR) method to identify the lower quartile Q1 at the 25% position and the upper quartile Q3 at the 75% position in the data, then calculate the interquartile range (IQR), with the calculation formula as follows:

<!-- b000108 | prose | pages [5] -->
𝑄1 = 𝑛+ 1 微信号：MATHmodels (1) 4 𝑄3 = 3(𝑛+ 1) (2) 4 (3) 𝐼𝑄𝑅= 𝑄3 −Q1 In the formula, n is the size of the dataset. If n is not an integer, linear interpolation can be performed between the two data points closest to n to estimate Q1 and Q3. The interquartile range (IQR) represents the distance between Q3 and Q1.

<!-- b000109 | prose | pages [5] -->
In this paper, data outside the range [Q1 - 1.5 IQR, Q3 + 1.5 IQR] is defined as an outlier and is subjected to correction. Taking speed_mph as an example, the box plot of its outliers is shown in

<!-- b000110 | caption | pages [5] -->
Figure 1.

<!-- b000111 | prose | pages [5] -->
For the outliers on the left side of the figure, they are replaced by performing data fitting interpolation within the group of matches they belong to. It is worth noting that for the p1_distance_run data column, since p1_distance_run is related to rally_count, the more rallies played, the greater the running distance of the player. Therefore, it is necessary to first remove the impact of the number of rallies on running distance. First,divide p1_distance_run by rally_count,and then proceed to correct the outliers. The box plots of outliers before and after preprocessing are shown in

<!-- b000112 | caption | pages [5] -->
Figure 2. The processed outliers are then subjected to data fitting interpolation, and multiplied by

<!-- b000113 | prose | pages [5] -->
rally_count to serve as the new corrected values for p1_distance_run.

<!-- b000114 | caption | pages [5] -->
Figure 1:Outlier boxplot of speed mph

<!-- b000115 | caption | pages [5] -->
Figure 2: Box plots of outliers for p1_distance_run before and after preprocessing

<!-- b000116 | heading | pages [5] -->
3.1.2 Filling Missing Data

<!-- b000117 | prose | pages [5, 6] -->
Firstly, it is necessary to identify missing values in the dataset. Taking speed_mph as an example, a heatmap of missing values can be generated using the Heatmap Function from the Seaborn Library in Python. This heatmap provides a visual representation of missing data within the dataset. The result 关注数学模型 of generating a heatmap using the heatmap function is shown in Figure 3. In the figure, there are large yellow bands with gaps, indicating continuous missing data in this segment. Upon comparison, it is observed that this missing data all originates from the match_id = 2023-wimbledon-1310, which is attributed to system errors such as missing device records and the importance of the speed_mph parameter. Therefore, the data from this match is not considered, and the remaining 30 sets of data 微信公众号：数学模型 will be used for subsequent analysis and modeling.

<!-- b000118 | furniture | pages [5] -->
2

<!-- b000119 | furniture | pages [5] -->
MATHmodels

<!-- b000120 | furniture | pages [5] -->
获取更多资讯

<!-- b000121 | furniture | pages [6] -->
Team # 2403774                                                                                 Page 6 of 23

<!-- b000123 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000124 | caption | pages [6] -->
Figure 3: The heatmap of missing values for "speed_mph."

<!-- b000125 | prose | pages [6] -->
Additionally, considering the real circumstances of the matches, when there is a double fault situation in serving, meaning p1_double_fault + p2_double_fault = 1, both speed_mph and rally_count should be equal to 0. Taking the match_id=1301 as an example, all the data with speed_mph=NA is selected, as shown in Table 2.

<!-- b000126 | prose | pages [6] -->
Tabel 2: Partial data when match_id=1301 race speed_mph=NA

<!-- b000127 | prose | pages [6] -->
p2_double p1_double p1_double_fault+p2_double elapsed_time rally_count speed_mph _fault _fault _fault 0:32:57 0 1 1 0 NA 2:06:20 1 0 1 0 NA 2:14:53 0 1 1 0 NA 2:28:21 1 0 1 0 NA 2:53:10 1 0 1 0 NA 2:55:10 1 0 1 0 NA 3:05:04 0 0 0 3 NA 3:13:12 1 0 1 0 NA 3:22:58 1 0 1 0 NA 3:28:08 0 1 1 0 NA 3:33:45 1 0 1 0 NA

<!-- b000128 | prose | pages [6] -->
From the table, it can be observed that when elapsed_time is 3:05:04, neither side committed a double fault, and thus, the recorded speed_mph as NA is considered a genuine missing value. The rally_count of 3 also supports this conclusion. In contrast, for other instances where speed_mph is NA, double faults occurred. Although speed_mph is recorded as missing, it should be imputed.

<!-- b000129 | prose | pages [6] -->
The nearest-neighbor interpolation method is employed for filling in missing values. This method is suitable for imputing missing values in time series data and typically does not introduce new data structures or models. It effectively preserves the original data distribution or characteristics. Similarly, the same method was used for data cleaning in other variables within the dataset.

<!-- b000130 | heading | pages [6] -->
3.2 Data Transformation

<!-- b000131 | prose | pages [6, 7] -->
关注数学模型 In this study, some variables are unordered multicategorical variables represented as text in the dataset. Taking "winner_shot_type" as an example, it is represented as "F" for "Forehand Winner," "B" for "Backhand Winner," and "0" for "Other Winner." Analysis reveals that it belongs to an unordered multicategorical variable. From a numerical perspective, assigning values 1, 2, and 3 would imply an ordinal relationship, which is not accurate. In reality, the methods of winning are 微信公众号：数学模型 independent and do not have a hierarchical order. Assigning values of 1, 2, and 3 and incorporating them into the model would be inappropriate, so they need to be transformed into dummy variables.

<!-- b000132 | furniture | pages [6] -->
2

<!-- b000133 | furniture | pages [6] -->
MATHmodels

<!-- b000134 | furniture | pages [6] -->
获取更多资讯

<!-- b000135 | furniture | pages [7] -->
Team # 2403774                                                                                 Page 7 of 23

<!-- b000137 | prose | pages [7] -->
For example, with regard to the "winner_shot_type" variable, there are three possible values: "F" is transformed into {0, 1}, "B" into {0, 1}, and "0" into {0, 0}. Similarly, other variables are transformed using the same method.

<!-- b000138 | heading | pages [7] -->
3.3 Feature Recombination

<!-- b000139 | prose | pages [7] -->
As shown in Table 3, based on the dataset and in accordance with the rules of tennis matches, the following 36 sets of variables are selected as potential independent variables that may affect momentum. These independent variables are categorized into three types based on the time scale: current time, previous shot time, and long-term time. The independent variables included in the long- term time category are calculated based on existing data and encompass various information related to the same game, set, and match. 微信号：MATHmodels Tabel 3: Variable - Symbol comparison table Instantaneous Calculated Variables

<!-- b000140 | heading | pages [7] -->
Symbols

<!-- b000141 | prose | pages [7] -->
Instantaneous Local Variable Current server server Current serve count serve_no Current serve speed speed_mph Current serve width serve_width Current serve depth serve_depth Rounds taken for current game score rally_count Current return depth return_depth Current set count set_no Current game count game_no Historical Instant Variable Previous point's score Point_Score Previous point's score without touch during serve, option 1 Serve_No_Touch_1 Previous point's score without touch during serve, option 2 Serve_No_Touch_2 Previous point's score without touch during rally, option 1 Rally_No_Touch_1 Previous point's score without touch during rally, option 2 Rally_No_Touch_2 Previous point's no-touch win type Win_Type Previous point's running distance, option 1 Serve_No_Touch_1 Previous point's running distance, option 2 Serve_No_Touch_2

<!-- b000142 | prose | pages [7] -->
Time Interval Calculated Variables

<!-- b000143 | heading | pages [7] -->
Symbols

<!-- b000144 | prose | pages [7, 8] -->
Set Level Interval Variable Current set's athlete's consecutive points won, option 1 Consecutive_1 Current set's athlete's consecutive points won, option 2 Consecutive_2 Number of games won in the current set, option 1 Games_1 关注数学模型 Number of games won in the current set, option 2 Games_2 Number of double faults in this set, option 1 Double_Faults_1 Number of double faults in this set, option 2 Double_Faults_2 Number of unforced errors in this set, option 1 Unforced_Errors_1 微信公众号：数学模型 Number of unforced errors in this set, option 2 Unforced_Errors_2 Number of net touches in this set, option 1 Net_Touches_1 Number of net touches in this set, option 2 Net_Touches_2 Current match's points lead progress Lead_Progress Game Level Interval Variable Total distance covered in this match, option 1 Total_Distance_1 Total distance covered in this match, option 2 Total_Distance_2 Number of break points won by the athlete in this match, option 1 Break_Points_Won_1 Number of break points won by the athlete in this match, option 2 Break_Points_Won_2 Number of break points lost by the athlete in this match, option 1 Break_Points_Lost_1 Number of break points lost by the athlete in this match, option 2 Break_Points_Lost_2 微信号：MATHmodels Point Level Interval Variable Total distance covered in this match, option 1 Total_Distance_Match_1 Total distance covered in this match, option 2 Total_Distance_Match_2

<!-- b000145 | furniture | pages [7] -->
2

<!-- b000146 | furniture | pages [7] -->
MATHmodels

<!-- b000147 | furniture | pages [7] -->
获取更多资讯

<!-- b000148 | furniture | pages [8] -->
Team # 2403774                                                                                 Page 8 of 23

<!-- b000150 | heading | pages [8] -->
3.4 Variable Selection

<!-- b000151 | prose | pages [8] -->
In the initial selection of variables, comprehensive coverage of the model was considered, but there may be some correlations among certain variables. To further improve the operational efficiency and simplicity of the model, a correlation analysis[1] was conducted on the variables intended for inclusion in the model. As shown in Figure 4, the confusion matrix[11] of variables clearly reveals the presence of high correlations among variables. Therefore, variable selection[2] based on correlation is necessary.

<!-- b000152 | caption | pages [8] -->
Figure 4: Confusion matrix plot of variables

<!-- b000153 | heading | pages [8] -->
3.4.1 Correlation Analysis

<!-- b000154 | prose | pages [8] -->
The Spearman rank correlation coefficient[10] is a non-parametric statistical measure suitable for testing the correlation of abnormal distribution or ordered categorical data variables. The autocorrelations among the independent variables are calculated as shown in Figure 5. Based on this,

<!-- b000155 | prose | pages [8, 9] -->
关注数学模型 some variables[3,4] with high autocorrelations in the figure were removed. For example, "set_no" showed strong correlations with "Games_1," "Games_2," "Total_Distance_Match_1," and "Total_Distance_Match_2." We chose "Total_Distance_Match_1" as the final independent variable, reflecting the player 1's energy consumption, and removed the other variables.

<!-- b000156 | furniture | pages [8] -->
2

<!-- b000157 | furniture | pages [8] -->
MATHmodels

<!-- b000158 | furniture | pages [8] -->
获取更多资讯

<!-- b000159 | furniture | pages [9] -->
Team # 2403774                                                                                 Page 9 of 23

<!-- b000161 | prose | pages [9] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000162 | caption | pages [9] -->
Figure 5: The degree of self-correlation between independent variables

<!-- b000163 | heading | pages [9] -->
3.4.2 Variable Importance Ranking

<!-- b000164 | prose | pages [9] -->
After removing linearly correlated variables, there were still many variables, and not all of them had a significant impact on the model's results. To improve computational efficiency and further rank the importance of independent variables, the variables were sorted based on their impact on the dependent variable, which is whether the match is scored. Variables were sequentially removed from the smallest impact factor to the largest until a significant difference in model accuracy occurred.

<!-- b000165 | prose | pages [9] -->
When the variable "set_no" was removed, the classification accuracy decreased significantly from 95.5% to 66.1%. Therefore, the removal of independent variables was terminated at this point. The final selection of independent variables includes the following: server, Consecutive_2, Consecutive_1, Net_Touches_2, Double_Faults_1, Net_Touches_1, Double_Faults_2, Unforced_Errors_2, Point_Score, Lead_Progress, Unforced_Errors_1, Break_Points_Won_1, Serve_No_Touch_2, Break_Points_Won_2, Serve_No_Touch_1, Rally_No_Touch_1, return_depth, and Total_Distance_Match_1.

<!-- b000166 | caption | pages [9] -->
Figure 6: The correlation ranking of different independent variables with the dependent variable

<!-- b000167 | prose | pages [9] -->
关注数学模型

<!-- b000168 | furniture | pages [9] -->
2

<!-- b000169 | furniture | pages [9] -->
MATHmodels

<!-- b000170 | furniture | pages [9] -->
获取更多资讯

<!-- b000171 | furniture | pages [10] -->
Team # 2403774                                                                                 Page 10 of 23

<!-- b000172 | heading | pages [10] -->
4 Task 1: Momentum quantization and prediction model

<!-- b000173 | prose | pages [10] -->
In this section, we first define and quantify momentum. Then, we identify which player performs better and to what extent at specific moments in the game by building an XGBoost momentum prediction model.

<!-- b000174 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000175 | heading | pages [10] -->
4.1 Definition and Quantification of Momentum

<!-- b000176 | prose | pages [10] -->
We define momentum as follows: Momentum is implicitly embedded in the game state, explicitly reflecting the continuous scoring and losing in the game results. We make the following assumption: if the game state is related to scoring and losing, it can be reflected through momentum, completing the mapping from the distribution of game states to the distribution of scoring situations, establishing a relationship between the two distributions; conversely, if there is no relationship between them, such a mapping would be impossible to achieve.

<!-- b000177 | prose | pages [10] -->
Let the current game result sequence be 𝑃= {𝑃0, 𝑃1, … , 𝑃𝑁}, and the current moment be i, with N samples in total. We aim to estimate a player's momentum at moment 𝑖 by considering the game results in the vicinity of moment i. First, we need to create a window around moment i to capture the game's state within a short time frame. Next, we assign weights to these game results within the window, with results closer to the moment i contributing more significantly to momentum estimation, 微信号：MATHmodels while data from more distant matches have a smaller contribution.

<!-- b000178 | prose | pages [10] -->
Considering that in tennis matches, the serving player has a higher probability of winning points, we introduce a serving momentum factor, denoted as 𝑀𝑓, to adjust the momentum labels. When Player 1 serves, they gain an initial energy boost, and vice versa, they lose some energy when receiving. Both the gained and lost momentum are controlled by the momentum factor. Therefore, the momentum label formula can be expressed as follows:

<!-- b000179 | prose | pages [10] -->
𝑌𝑖= ( 𝑚 ) (1 −𝑀𝑡) + 𝑀𝑡, 𝑀𝑡= 0.1 (4) 𝑀𝑚0

<!-- b000180 | heading | pages [10] -->
4.2 XGBoost-Based Momentum Quatification Model

<!-- b000181 | prose | pages [10] -->
Due to the non-linearity between independent variables and the final outcome of the game, we chose to use machine learning methods to discover the underlying relationship between independent and dependent variables. After considering various machine learning models, we opted for XGBoost for momentum prediction. XGBoost[8,9] utilizes an optimized distributed gradient boosting algorithm that allows rapid training of large-scale datasets while maintaining efficient resource utilization.

<!-- b000182 | prose | pages [10] -->
The construction and solution steps of the XGBoost momentum prediction model are as follows:

<!-- b000183 | prose | pages [10] -->
(1) Data Preprocessing Before constructing the model, while maintaining the consistency of data distribution, the original dataset is initially divided into a training set S (80%) and a test set T (20%). The model is trained on S and the model's generalization ability is tested on T. For the training set S, further p-fold k-fold cross-validation is applied, where S is randomly divided into k subsets, and in each iteration, k-1 subsets are used for training, while the remaining one is used for validation. To reduce errors due to different sample divisions, this process is repeated p times, resulting in the average of p+k validation results as the model evaluation result. In this study, p=5 and k=5, meaning 5 times 5-fold cross-validation was utilized.

<!-- b000184 | prose | pages [10] -->
(2) Basis Function Construction XGBoost gradually adds new models in each iteration to expand its understanding of new data. Its formula is as follows:

<!-- b000185 | prose | pages [10] -->
(5) 𝑀𝑏= 𝑀𝑏−1 + 𝜂∙𝑇𝑏 (3) Definition of Loss Function The goal of XGBoost training is to minimize the loss function, which includes both traditional loss functions and regularization terms that describe model complexity.

<!-- b000186 | prose | pages [10, 11] -->
关注数学模型 𝑚 (𝑡−1) + 𝑓𝑖(𝑥𝑖)) + 𝛺(𝑓𝑘) (6) min 𝑂𝑏𝑗= ∑𝑙(𝑦𝑖, 𝑦̂𝑖 𝑖=1 In the formula, the first term represents the difference between the momentum predicted by the model and the momentum calculated based on game results, while the second term represents the 微信公众号：数学模型 model's complexity. In the above formula, {i} represents the number of samples in the dataset, and {m} represents the total number of samples in the dataset. {γ} and {λ} are used to adjust the complexity of the tree. The regularization term can smooth the final learning weight and prevent overfitting, improving the generalization ability of momentum prediction across matches and players.

<!-- b000187 | furniture | pages [10] -->
2

<!-- b000188 | furniture | pages [10] -->
MATHmodels

<!-- b000189 | furniture | pages [10] -->
获取更多资讯

<!-- b000190 | furniture | pages [11] -->
Team # 2403774                                                                                 Page 11 of 23

<!-- b000192 | prose | pages [11] -->
(4) Momentum Error Prediction Predicting the momentum can be considered a regression task. In each optimization step, the model minimizes the mean squared error (MSE) between the predicted momentum and the labeled momentum, defined as follows:

<!-- b000193 | prose | pages [11] -->
2 1 (𝑡)) = (𝑡)) (7) 𝑙(𝑦𝑖, 𝑌̂𝑖 2 (𝑦𝑖−𝑌̂𝑖 (𝑡)} represents the momentum In the formula, {𝑦𝑖 } represents the label of momentum, {𝑌̂𝑖 prediction of the model in t iterations 微信号：MATHmodels (5) Structural Regularization Term Calculation The formula for calculating the regularization term is as follows:

<!-- b000194 | prose | pages [11] -->
𝑇 𝛺(𝑓𝑡) = 𝛾𝑇+ 1 2 (8) 2 𝜆∑𝑤𝑗 𝑗=1 In the formula, the hyperparameters {γ} and {λ} control the strength of the penalty, {T} represents the current number of leaf nodes in the regression tree, and the last term is the L2 norm of the leaf node values.

<!-- b000195 | prose | pages [11] -->
Based on the MSE loss function, pseudo-residuals can be derived and expressed as:

<!-- b000196 | prose | pages [11] -->
(𝑏−1)) 𝜕𝑙(𝑦𝑖, 𝑦̂𝑖 (𝑏−1) (9) 𝑟𝑖𝑏= −[ ] = 𝑦𝑖−𝑦̂𝑖 (𝑏−1) 𝜕𝑦̂𝑖 In each iteration of the model, these pseudo-residuals are used as gradients of the loss function with respect to the model predictions to train new decision trees. This way, each iteration of the model attempts to correct the prediction errors of the previous iteration.

<!-- b000197 | prose | pages [11] -->
(6) Momentum Prediction Model Construction In summary, our model can be summarized as follows:

<!-- b000198 | prose | pages [11] -->
𝑚 (𝑡−1) + 𝑓𝑖(𝑥𝑖)) + 𝛺(𝑓𝑘) 𝑚𝑖𝑛 𝑂𝑏𝑗= ∑𝑙(𝑦𝑖, 𝑦̂𝑖 𝑖=1 𝐾 𝑦̂𝑖= ∑ 𝑓𝑘(𝑥𝑖) , 𝑓𝑘∈𝜑 𝑘=1 1 2 𝜆𝑤2 𝛺(𝑓𝑘) = 𝛾𝑇+ (10) 1 (𝑡)) = (𝑡))2 𝑙(𝑦𝑖, 𝑌̂𝑖 2 (𝑦𝑖−𝑌̂𝑖 𝑚 𝑀𝑚0) (1 −𝑀𝑡) + 𝑀𝑡, 𝑀𝑡= 0.1 𝑌𝑖= ( { Based on the XGBoost model described above, we model the game data, where the input is the known information at the current time point. The optimization of the objective function aims to minimize the difference between the predicted probability of winning the next time step and the actual outcome.

<!-- b000199 | prose | pages [11] -->
关注数学模型

<!-- b000200 | furniture | pages [11] -->
2

<!-- b000201 | furniture | pages [11] -->
MATHmodels

<!-- b000202 | furniture | pages [11] -->
获取更多资讯

<!-- b000203 | furniture | pages [12] -->
Team # 2403774                                                                                 Page 12 of 23

<!-- b000204 | heading | pages [12] -->
Algorithm: Momentum Quantization

<!-- b000205 | prose | pages [12] -->
Input: 𝑃[𝑖], 𝑠[𝑖], 𝑁, 𝑊 , 𝑋[𝑖] Output: 𝑞[𝑖], 𝐺[𝑖] W 𝑤=−𝑊 𝑒w 1  𝑀𝑚𝑜= ∑ 微信公众号：数学模型 2  Initialize the model Mo with a constant value 3  e.g. the mean of the labels 4 for i ←0 to 𝑁 do 5    m←0;

<!-- b000206 | prose | pages [12] -->
6    for 𝑗←−𝑊 to W do 7        if 0 ⩽𝑖+ 𝑗< 𝑁 and ∣𝑠[𝑖+ 𝑗] −𝑠[𝑖] ∣⩽1 then 8            𝑚←𝑚+ 𝑒|𝑖+𝑗| ⋅𝑃[𝑖+ 𝑗];

<!-- b000207 | prose | pages [12] -->
9    end 𝑚 10   𝑌𝑖← 𝑀𝑚0 . (1 −𝑀𝑓) + 𝑀𝑓;

<!-- b000208 | prose | pages [12] -->
𝑡−1 11   Get the predicting 𝑌̂𝑖←∑ 𝑘=1 𝑓𝑘(𝑥𝑖) 12   Get the pseudo-residual 𝑟𝑖←𝑌𝑖−𝑌̂𝑖 微信号：MATHmodels 13   Fit a regression tree 𝑇𝑖 to the pseudo-residuals 𝑟𝑗.

<!-- b000209 | prose | pages [12] -->
14   Update the model 𝑀𝑖←𝑀𝑖−1 + 𝜂⋅𝑇𝑖.

<!-- b000210 | prose | pages [12] -->
15 end

<!-- b000211 | prose | pages [12] -->
In the above algorithm, we use the match data S for each time step and differentiate whether it is the same match based on the provided number of match sessions. In the algorithm, W represents the window size, and we use exponential weighting to weigh the match data within the window and accumulate contributions to the momentum estimation in m. To normalize the estimate of momentum, we calculate the normalization factor 𝑀𝑚𝑜 as the maximum momentum and map m to the range of 0-1. According to the above algorithm, we can obtain momentum labels for each time step based on match results, which are used to fit an XGBoost model to map from match data to estimated player potentials. The fitting of the XGBoost model first obtains predictions of the previous model on the data and then calculates pseudo-residuals based on the output and labels. Afterward, a new tree is obtained based on the pseudo-residual and the specified learning rate and added to the tree ensemble.

<!-- b000212 | prose | pages [12] -->
(7) Model Evaluation To assess the predictive accuracy of the model for momentum, we selected the Mean Square Error (MSE) as a performance metric. The MSE measures the difference between the model's predicted momentum and the momentum generated based on the matches. We performed 5-fold cross- validation, and the average MSE for the model was found to be 0.02.

<!-- b000213 | heading | pages [12] -->
4.3 Results Visualization and Analysis

<!-- b000214 | prose | pages [12] -->
As shown in Figure 7, we present the estimation of Player1's momentum and their score situation, which can be symmetrically deduced for Player2. Using the XGBoost-based momentum prediction model, we calculate the changes in their momentum. Due to significant fluctuations in the results and considering that momentum quantification results can be affected by external disturbances, the use of a Kalman filter effectively eliminates noise and jitter. Compared to the original momentum results, the results after Kalman filtering are smoother. The orange line in the graph represents records from matches starting from a score of 0 and scoring 100 times, where 1 indicates a score and 0 indicates no score. According to our definition, when the momentum remains consistently above 0.5, Player1 has a greater advantage; conversely, when it falls below 0.5, Player2 has a greater advantage. At the beginning, as shown in Box 1, Player1's estimated momentum increases, indicating continuous scoring in the game with fewer losses. Subsequently, there is a turning point in the estimated momentum, following multiple losses. Then, the momentum returns to a higher level, accompanied

<!-- b000215 | prose | pages [12, 13] -->
关注数学模型 by multiple scores. In the later stages of the match, as shown in Box 2, the estimated momentum experiences a significant decline, followed by continuous losses for Player1. Even though there is 1 score, the estimated momentum continues to decline. This phenomenon demonstrates that our designed model can describe the potential scoring situation of players near a certain moment, which is the concept of momentum. 微信公众号：数学模型 微信号：MATHmodels

<!-- b000216 | furniture | pages [12] -->
2

<!-- b000217 | furniture | pages [12] -->
MATHmodels

<!-- b000218 | furniture | pages [12] -->
获取更多资讯

<!-- b000219 | furniture | pages [13] -->
Team # 2403774                                                                                 Page 13 of 23

<!-- b000221 | caption | pages [13] -->
Figure 7: Visualization of score and momentum quantification

<!-- b000222 | heading | pages [13] -->
5 Task 2: The Momentum-Outcome Connection

<!-- b000223 | prose | pages [13] -->
In this section, we first generate random match scenarios, including match feature states and match scores. Then we apply the XGBoost momentum prediction model established in question 1 to calculate potential energies for both real matches and random matches. Finally, we compare and evaluate the correlation between match states (match conditions, serve speed, etc.) and momentum by selecting multiple indicators.The results can demonstrate how momentum affects match scores.

<!-- b000224 | heading | pages [13] -->
5.1 Random Match Scenario Generation

<!-- b000225 | prose | pages [13] -->
The coach believes that match scores are independent of match states, such as player serves, which affect momentum. Based on this, we set out to generate random match states and random scores to simulate random match scenarios. As shown in Figure 8, to make random match scenarios as close as possible to real match rules, we randomly select values and options for features from a uniform distribution to create new random match states. Regarding match outcomes, we set the probability of random scores to be 50%, and each setting is independently and identically distributed. The generation of random matches is incremental, and match results, determining player victories and match completion, are calculated based on the number of sets, games, and points in a Wimbledon match.

<!-- b000226 | caption | pages [13] -->
Figure 8: The process of generating random match scenarios

<!-- b000227 | heading | pages [13] -->
5.2 Analysis of the Impact of Momentum on Scores

<!-- b000228 | prose | pages [13] -->
We utilize multiple evaluation metrics to comprehensively assess and compare the predictive performance of the model. These metrics include Mean Square Error (MSE), Root Mean Square Error

<!-- b000229 | prose | pages [13, 14] -->
关注数学模型 (RMSE), Mean Absolute Error (MAE), R-squared (R2), Adjusted R-squared (Adjusted R2), and Pearson Correlation Coefficient (Pearsonr). Their definitions and meanings can be found in Table 4.

<!-- b000230 | furniture | pages [13] -->
2

<!-- b000231 | furniture | pages [13] -->
MATHmodels

<!-- b000232 | furniture | pages [13] -->
获取更多资讯

<!-- b000233 | furniture | pages [14] -->
Team # 2403774                                                                                 Page 14 of 23

<!-- b000235 | prose | pages [14] -->
Tabel 4: Explanation of Evaluation Metrics and Numerical Significance Indicators Describes 微信公众号：数学模型 Mean Square Error A smaller MSE indicates that the model's predictions are closer (MSE) to the actual values Root Mean Square A smaller RMSE indicates higher accuracy in the model's Error (RMSE) predictions Mean Absolute Error A smaller MAE implies higher precision in the model's (MAE) predictions Mean Absolute Error An R2 value closer to 1 indicates a better fit of the model. (R2) A higher Adjusted R2 value suggests stronger explanatory Adjusted R-squared (Adjusted R2) power of the model.

<!-- b000236 | prose | pages [14] -->
The Pearsonr value ranges from -1 to 1, where 1 represents a Pearson Correlation perfect positive correlation, -1 represents a perfect negative Coefficient (Pearsonr) correlation, and 0 represents no linear correlation.

<!-- b000237 | prose | pages [14] -->
微信号：MATHmodels As shown in Table 5, the numbers from 1301 to 1701 represent the real scenarios used, with scenario 10 excluded from the analysis due to missing data (details can be found in Section 3.1.2). The label "random" represents simulated random scenarios. Our model demonstrates significantly lower levels of estimation error, with MSE, RMSE, and MAE reflecting errors within the ranges of 3.554e-3 to 8.621e-3, 5.961e-2 to 9.285e-2, and 4.625e-2 to 7.478e-2, respectively. These values are much lower than the corresponding values under random scenarios, which are 0.125576, 0.354367, and 0.297229. This indicates that our model significantly outperforms traditional methods in terms of prediction accuracy and can provide more accurate predictions of actual values.

<!-- b000238 | prose | pages [14] -->
The R2 and Adjusted R2 values of our model fall within the ranges of 0.8602 to 0.9073 and 0.8594 to 0.9071, respectively, which are far higher than the values under random scenarios, which are -2.2744 and -2.28424. This result not only demonstrates the model's strong explanatory power for data variability but also shows its stable performance even when considering model complexity.

<!-- b000239 | prose | pages [14] -->
The Pearson correlation coefficient further confirms the strong positive linear relationship between our model and actual values, with values ranging from 0.9408 to 0.9591, deviating by only 0.002911. This indicates a very high linear consistency between our model's predictions and actual label values. In other words, as actual label values increase, the model's predictions also increase, and vice versa. This high level of linear relationship suggests that the model not only accurately predicts the magnitude of actual values but also maintains a consistent trend in predictions across different ranges of label values.

<!-- b000240 | prose | pages [14] -->
In contrast, the Pearson correlation coefficient for random scenarios is close to zero, indicating almost no linear relationship between its predictions and actual label values, failing to reflect the changing trends in actual label values.

<!-- b000241 | prose | pages [14] -->
In summary, a player's score in the match is not random, and momentum plays a significant role in the game.

<!-- b000242 | heading | pages [14] -->
Tabel 5: Evaluation of Consistency between Predicted Potential Energy and Match Results

<!-- b000243 | prose | pages [14] -->
adjusted_r_squared match mse rmse mae r_squared ks_real 1301 0.005301 0.072808 0.057363 0.839388 0.838847 0.052323 1302 0.004725 0.06874 0.055849 0.866766 0.866097 0.331034 1303 0.005613 0.074917 0.059082 0.868931 0.867938 0.002346 1304 0.005553 0.074516 0.058671 0.880302 0.879945 0.052706

<!-- b000244 | prose | pages [14, 15] -->
关注数学模型 1305 0.005473 0.073977 0.059918 0.872491 0.871969 0.065444 1306 0.005082 0.071287 0.057995 0.890007 0.889674 0.0915 1307 0.006592 0.081189 0.066523 0.851584 0.850939 0.018196 1308 0.007664 0.087545 0.069851 0.835557 0.834683 0.156663 微信公众号：数学模型 1309 0.004817 0.069407 0.055093 0.871828 0.87122 0.365668 1311 0.006264 0.079147 0.062545 0.86502 0.864593 0.11801 1312 0.005775 0.075997 0.061332 0.844124 0.843553 0.206051 … … … … … … … 1701 0.003554 0.059614 0.046257 0.907333 0.907054 0.226841 random 0.136022 0.368812 0.301388 -2.54679 -2.55744 9.25E-06 Using the XGBoost momentum prediction model built in question one, we calculate potential energies by substituting random match data into the model. If the predicted momentum from random data matches the variation in match scores, it proves that the score situation is random. Conversely, if there is no match between the predicted momentum and the score situation, it demonstrates that momentum can reflect a player's scoring situation over a certain period of time. As shown in Figure 9, the left-side data points represent predicted momentum, the right-side represents label momentum, 微信号：MATHmodels which is the momentum reflected by match results, and the lines in the middle indicate that the two numbers belong to the same moment. By comparing, it is observed that in real match situations, the lines in the graph are mostly parallel to the x-axis, indicating that predicted momentum can be well- mapped to match situations. This suggests that momentum to some extent reflects match outcomes. However, in the coach's perceived random match scenarios, the lines do not exhibit a clear correspondence, indicating that the model cannot map from match states to match scores. Consequently, it implies that momentum can be used to reflect a player's scoring changes over a certain period of time.

<!-- b000245 | furniture | pages [14] -->
2

<!-- b000246 | furniture | pages [14] -->
MATHmodels

<!-- b000247 | furniture | pages [14] -->
获取更多资讯

<!-- b000248 | furniture | pages [15] -->
Team # 2403774                                                                                 Page 15 of 23

<!-- b000250 | caption | pages [15] -->
Figure 9: The mapping between the predicted mometum and the momentum defined in the contest

<!-- b000251 | heading | pages [15] -->
6 Bayesian Inflection point Detection and Prediction

<!-- b000252 | heading | pages [15] -->
6.1 Bayesian Online Inflection point Detection Method for Identifying Inflection points

<!-- b000253 | heading | pages [15] -->
6.1.1 Principle

<!-- b000254 | prose | pages [15] -->
The core principle of the Bayesian online inflection point detection method[5,6,7] is to use Bayesian statistics to identify structural changes, or inflection points, in time series data. This method calculates the conditional probability of observed time series values at each time point to assess the likelihood of a inflection point occurring. Specifically, it assumes that the time series can be divided into several segments, with data within each segment following a certain statistical distribution, and differences in distribution parameters between different segments. By applying Bayesian rules to all observed data before each time point, the posterior probability of that point being a inflection point can be estimated. Subsequently, these posterior probabilities are used to infer the locations of inflection points: points where the probability significantly increases are considered as inflection

<!-- b000255 | prose | pages [15, 16] -->
关注数学模型 points. This process is performed online, meaning that data can be processed one by one without waiting for the collection of the entire data sequence, enabling real-time inflection point detection.

<!-- b000256 | furniture | pages [15] -->
2

<!-- b000257 | furniture | pages [15] -->
MATHmodels

<!-- b000258 | furniture | pages [15] -->
获取更多资讯

<!-- b000259 | furniture | pages [16] -->
Team # 2403774                                                                                 Page 16 of 23

<!-- b000261 | prose | pages [16] -->
1.Initialize 𝑃(𝑟0) = 𝑆̃(𝑟0) or 𝑃(𝑟0 = 0) = 1 (0) = 𝑣𝑝𝑟𝑖𝑜𝑟 微信公众号：数学模型 𝑣1 (0) = 𝑥𝑝𝑟𝑖𝑜𝑟 𝑥1 2.Observe New Datum 𝑥𝑡 3.Evaluate Predictive Probability (𝑟) = 𝑃(𝑥𝑡|𝑣𝑡 (𝑟), 𝑥𝑡 (𝑟)) 𝜋𝑡 4.Calculate Growth Probabilities (𝑟)(1 −𝐻(𝑟𝑡−1)) 𝑃(𝑟𝑡= 𝑟𝑡−1 + 1, 𝑥1:𝑡) = 𝑃(𝑟𝑡−1, 𝑥1:𝑡−1)𝜋𝑡 5.Calculate Changepoint Probabilities (𝑟)𝐻(𝑟𝑡−1) 𝑃(𝑟𝑡= 0 + 1, 𝑥1:𝑡) = ∑𝑃(𝑟𝑡−1, 𝑥1:𝑡−1) 𝜋𝑡 𝑟𝑡−1 6.Calculate Evidence 微信号：MATHmodels 𝑃(𝑥1:𝑡) = ∑𝑃(𝑟𝑡, 𝑥1:𝑡) 𝑟𝑡 7.Determine Run Length Distribution 𝑃(𝑟𝑡|𝑥1:𝑡) = 𝑃(𝑟𝑡, 𝑥1:𝑡)/𝑃(𝑥1:𝑡) 8.Update Sufficient Statistics (0) = 𝑣𝑝𝑟𝑖𝑜𝑟 𝑣𝑡+1 (0) = 𝑥𝑝𝑟𝑖𝑜𝑟 𝑥𝑡+1 (𝑟+1) = 𝑣𝑡 (𝑟) + 1 𝑣𝑡+1 (𝑟+1) = 𝑥𝑡 (𝑟) + 𝑢(𝑥𝑡) 𝑥𝑡+1 9.Perform Prediction (𝑟))𝑃(𝑟𝑡|𝑥1:𝑡) 𝑃(𝑥𝑡+1|𝑥1:𝑡) = ∑𝑃(𝑥𝑡+1|𝑥𝑡 𝑟𝑡 10.Return to Step 2 Here are the meanings of the variables involved: ⚫ 𝑃(𝑟0): The probability of initializing a inflection point (inflection point). δ(r) is the Dirac delta function, which equals 1 at r=0, and 0 otherwise. Alternatively, 𝑃(𝑟0 = 0) is set to 1, indicating that there are no inflection points initially.

<!-- b000262 | prose | pages [16] -->
𝑣(0)and𝑥(0): Initialization parameters for sufficient statistics, corresponding to prior knowledge ⚫ 𝑣𝑝𝑟𝑖𝑜𝑟 and 𝑥𝑝𝑟𝑖𝑜𝑟.

<!-- b000263 | prose | pages [16] -->
(𝑟) : The predicted probability calculated after observing new data 𝑥𝑡 . It represents the ⚫ 𝜋𝑡 probability of data x_t occurring given the current sufficient statistics and inflection point location. ⚫ 𝑃(𝑟𝑡= 𝑟+ 1|𝑥1:𝑡): Growth probability at time t for a inflection point. ⚫ 𝑃(𝑟𝑡= 0|𝑥1:𝑡): Inflection point probability at time t for resetting to 0. ⚫ 𝑃(𝑥1:𝑡): Evidence probability, representing the probability of observing the data sequence 𝑥1:𝑡 at time t. ⚫ 𝑃(𝑟𝑡|𝑥1:𝑡) : Run-length distribution, indicating the probability of the current run length being 𝑟𝑡given the data sequence 𝑥1:𝑡.

<!-- b000264 | prose | pages [16] -->
𝑣(𝑟+1) and 𝑥(𝑟+1): Updated parameters for sufficient statistics. ⚫

<!-- b000265 | prose | pages [16, 17] -->
关注数学模型 ⚫ 𝑃(𝑥𝑡+1|𝑥1:𝑡): The probability of predicting the next data point 𝑥𝑡+1 at time 𝑡+ 1.

<!-- b000266 | furniture | pages [16] -->
2

<!-- b000267 | furniture | pages [16] -->
MATHmodels

<!-- b000268 | furniture | pages [16] -->
获取更多资讯

<!-- b000269 | furniture | pages [17] -->
Team # 2403774                                                                                 Page 17 of 23

<!-- b000271 | heading | pages [17] -->
6.1.2 Implementation Process

<!-- b000272 | prose | pages [17] -->
From the perspective of Player 1, we assigned one point for each victory and deducted one point for each loss. We conducted inflection point detection on Player 1's scoring trend using Bayesian online inflection point detection. We plotted the scoring trends and inflection point graphs for two matches 微信公众号：数学模型 with match IDs 1407 and 1503, as shown in Figure 10 and Figure 11.

<!-- b000273 | caption | pages [17] -->
Figure 10: The scoring trend and inflection point graph for Player 1 at matchid=1407&1503

<!-- b000274 | prose | pages [17] -->
The inflection points in the graph are presented as regions (through) rather than individual points 微信号：MATHmodels because inflection point detection typically provides a possible interval where structural changes might occur over a period of time. This represents a transitional phase rather than a discrete moment because real data may contain noise, and actual changes may occur gradually.

<!-- b000275 | prose | pages [17] -->
Taking Figure 10 as an example, based on the data in the table, when the first inflection point occurs, Player 2 made a double fault; when the second inflection point occurs, Player 1 scored a break point; when the third inflection point occurs, Player 2 scored a break point; when the fourth inflection point occurs, Player 1 scored a point without any touch. Subsequent inflection points also correspond to specific events, aligning with the facts. Therefore, we consider the approach of using Bayesian online inflection point detection to find inflection points as feasible.

<!-- b000276 | heading | pages [17] -->
6.2 Correlation Analysis of Inflection Points

<!-- b000277 | prose | pages [17] -->
Following the method outlined in Section 6.1, we detected the inflection point regions in the matches. We replaced the dependent variable with a binary variable, where 1 represents being in the inflection point region and 0 represents not being in the inflection point region. We then used the Spearman rank correlation coefficient method as described in Section 3.4.1 to calculate the correlation between independent variables and the dependent variable. Finally, we obtained the importance ranking of the 18 independent variables as shown in Figure 12.

<!-- b000278 | caption | pages [17] -->
Figure 11: Independent Variable Importance Ranking

<!-- b000279 | prose | pages [17, 18] -->
From the graph, it can be observed that the most important variable is the distance covered by the athlete, followed by whether both sides won a break point, and subsequently variables like the consecutive scoring streak. This result aligns with our expectations. Firstly, the distance covered by 关注数学模型 the athlete reflects the degree of physical exertion, with increasing distance indicating growing fatigue, which can lead to shifts in the game's momentum. Secondly, whether both sides won a break point is also a crucial factor affecting the game's trend. Winning a break point provides a boost to the player's morale and confidence while delivering a blow to the opponent's confidence. Therefore, it is considered a significant factor. Based on this, we believe that calculating the importance ranking of 微信公众号：数学模型 independent variables using this method is feasible.

<!-- b000280 | furniture | pages [17] -->
2

<!-- b000281 | furniture | pages [17] -->
MATHmodels

<!-- b000282 | furniture | pages [17] -->
获取更多资讯

<!-- b000283 | furniture | pages [18] -->
Team # 2403774                                                                                 Page 18 of 23

<!-- b000285 | heading | pages [18] -->
6.3 Tennis Match Point Temporal Convolutional Network

<!-- b000286 | prose | pages [18] -->
According to the Bayesian online inflection point detection model, we have obtained inflection point regions that are close to the Ground Truth in advance, as shown in Figure 13. We represent the inflection points using a binary model, where points within the inflection point regions are marked as 1, and the rest are marked as 0. Considering the time series nature of the data, we use a Temporal Convolutional Network (TCN) for inflection point prediction, treating it as a binary classification problem. TCN is a type of 1D convolutional model that incorporates the concept of convolution from CNN into sequential networks similar to RNN. In the TCN network, dilated causal convolutions are primarily used. This convolution is characterized by the inclusion of dilation in the regular convolution, aiming to increase the receptive field, as shown in Figure 13: 微信号：MATHmodels Causal Convolution refers to the type of convolution where the output at time t depends only on the information at and before time t and does not depend on information after time t. The diagram illustrates a typical causal convolution schematic.

<!-- b000287 | caption | pages [18] -->
Figure 12: Dilated Conv   Figure 13: Causal Conv      Figure 14: MSTCN

<!-- b000288 | prose | pages [18] -->
Due to variations in the number of rounds in different matches, it is influenced by factors such as the skill gap between the competing sides and the game's status, both subjectively and objectively pleasing. Furthermore, the presence of winning streaks due to being in a hot state or losing streaks due to being in a low state is critical information for match outcomes. Therefore, in this chapter, based on TCN and considering the characteristics of tennis matches, we have designed a Multi-Stage Temporal Convolutional Network (MSTCN), as shown in Figure 15 below. The introduction of MSTCN aims to incorporate match information across multiple time scales simultaneously for model prediction.

<!-- b000289 | prose | pages [18] -->
Multi-time scale temporal convolution, when used in tennis match prediction, offers several advantages by integrating information from different time scales. These advantages can improve prediction accuracy, enhance model generalization capabilities, and better handle complex time series data. The summarized advantages are as follows:

<!-- b000290 | heading | pages [18] -->
6.3.1 Design Details

<!-- b000291 | prose | pages [18] -->
In this study, we employed a two-layer multi-scale temporal model as described above. We have input time series data X, where X[t] represents the observation at time step t. The model extracts features from the time series through convolution operations.

<!-- b000292 | prose | pages [18] -->
Multi-Scale Temporal Convolution Layer:

<!-- b000293 | prose | pages [18] -->
The size of the first convolution kernel is k1=3, designed to capture features at shorter time scales;The size of the second convolution kernel is k2=5, intended for capturing features at

<!-- b000294 | prose | pages [18, 19] -->
关注数学模型 intermediate time scales;The size of the third convolution kernel is k3=7, aimed at capturing features at longer time scales.

<!-- b000295 | furniture | pages [18] -->
2

<!-- b000296 | furniture | pages [18] -->
MATHmodels

<!-- b000297 | furniture | pages [18] -->
获取更多资讯

<!-- b000298 | furniture | pages [19] -->
Team # 2403774                                                                                 Page 19 of 23

<!-- b000300 | prose | pages [19] -->
The formula for performing the convolution operation is as follows:

<!-- b000301 | prose | pages [19] -->
𝑍𝑖[𝑡] = 𝑓(𝑤𝑖∗𝑋[𝑡: 𝑡+ 𝑘𝑖] + 𝑏𝑖) for 𝑖= 1,2,3 (11) 微信公众号：数学模型 𝑃𝑖[𝑡] = 𝑔(𝑚𝑎𝑥(𝑓(𝑤𝑖∗𝑋[𝑡: 𝑡+ 𝑘𝑖] + 𝑏𝑖)[𝑡: 𝑡+ 𝑠])) for 𝑖= 1,2,3 (12) The equations represent a two-scale convolutional neural network layer followed by a max pooling operation. The convolutional layer computes features 𝑍1 ,  𝑍2 ,and  𝑍3 by applying kernel weights 𝑊1,𝑊2,and 𝑊3and adding biases 𝑏1, 𝑏2,and 𝑏3,respectively, with a Re LU activation function f. The subsequent pooling layer reduces dimensionality with a max pooling function g over a window sizes, resulting in pooled features 𝑃1, 𝑃2,and 𝑃3.

<!-- b000302 | prose | pages [19] -->
After the pooling layer, a fully connected layer is added to learn high-level representations of the time series.

<!-- b000303 | prose | pages [19] -->
𝑌[𝑡] = ℎ(𝑊𝑓𝑐∗𝑃1[𝑡] + 𝑏𝑓𝑐) (13) In this context:

<!-- b000304 | prose | pages [19] -->
𝑌[𝑡] is the model's output. 微信号：MATHmodels ℎ is the activation function of the fully connected layer.

<!-- b000305 | prose | pages [19] -->
𝑊𝑓𝑐 and 𝑏𝑓𝑐 are the weights and bias terms of the fully connected layer.

<!-- b000306 | prose | pages [19] -->
The two-layer multi-scale temporal convolutional network follows the same design approach.

<!-- b000307 | prose | pages [19] -->
The model's hyperparameters are defined as follows:

<!-- b000308 | prose | pages [19] -->
Tabel 6:experimental parameter setting details Name Illustration Value Epoch Total epoches in training 10 Batch_Size The number of input video in a batch 6 Leaning-Rate The learning rate for optimizer le-4 Optimizer The optimizer used in our experiment Adam

<!-- b000309 | heading | pages [19] -->
6.3.3 Results

<!-- b000310 | prose | pages [19] -->
In this section, we conducted experiments to classify whether tennis matches belong to the transition point region. Model evaluation was performed using five-fold cross-validation, and the predictive accuracies for fivea runs were 75.49%, 74.94%, 75.70%, 73.98%, and 73.83%, with an average accuracy of 74.79%.

<!-- b000311 | heading | pages [19] -->
6.4 Suggestions

<!-- b000312 | prose | pages [19] -->
Based on the performance evaluation of the multi-scale temporal convolutional network model mentioned above, we can observe that the model achieves an average accuracy of approximately 74.79% in predicting tennis match turning points. This indicates that the model has a certain degree of reliability and can predict key turning points in matches relatively accurately. Based on this, I suggest that tennis coaches can use this model to assist in training and match strategy development: ⚫ Match Preparation: Coaches can use the model's predictions to prepare strategies for potential turning points. Understanding possible turning points in a match can help players better prepare mentally and technically to face these critical moments. For example, if a break point has a significant impact on turning points, coaches can advise players to stay focused when facing break points from their opponents, delaying the arrival of a turning point. ⚫ Targeted Training: Using the features identified by the model as turning points, coaches can design specific training plans to enhance a player's performance during these critical moments.

<!-- b000313 | prose | pages [19] -->
For instance, by simulating training scenarios related to turning points, coaches can improve a

<!-- b000314 | prose | pages [19, 20] -->
关注数学模型 player's mental resilience and adaptability. ⚫ Strategy Adjustments: During the course of a match, coaches can also make timely adjustments to the game plan based on the model's predictions. For example, when approaching a predicted turning point, coaches can guide players to adopt a more conservative or aggressive playing style to respond to potential changes in the match dynamics. 微信公众号：数学模型

<!-- b000315 | furniture | pages [19] -->
2

<!-- b000316 | furniture | pages [19] -->
MATHmodels

<!-- b000317 | furniture | pages [19] -->
获取更多资讯

<!-- b000318 | furniture | pages [20] -->
Team # 2403774                                                                                 Page 20 of 23

<!-- b000320 | heading | pages [20] -->
7 Task 4: Model Validation and Evaluation

<!-- b000321 | heading | pages [20] -->
7.1 Model Validation with Other Matches and Accuracy

<!-- b000322 | prose | pages [20] -->
We obtained tennis match data for the 2023 Wimbledon Women's Singles[12,13] from the internet. We initially performed autocorrelation analysis on the independent variables in this dataset using the Spearman correlation coefficient matrix method. The results of this analysis are shown in Figure X:

<!-- b000323 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000324 | caption | pages [20] -->
Figure 15: Autocorrelation among independent variables in women's singles

<!-- b000325 | prose | pages [20] -->
After removing strongly autocorrelated independent variables, we further filtered the independent variables based on their correlation with the dependent variable. The final ranking of the correlation between the selected independent variables and the dependent variable is shown in Figure X:

<!-- b000326 | caption | pages [20] -->
Figure 16: Correlation ranking of different independent variables with the dependent variable

<!-- b000327 | prose | pages [20] -->
Using the selected independent variables, we reran the XGBoost-based potential quantification model and obtained momentum estimates and their corresponding scores for the 2023 Wimbledon women's singles matches, as shown in Figure 17:

<!-- b000328 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000329 | furniture | pages [20] -->
2

<!-- b000330 | furniture | pages [20] -->
MATHmodels

<!-- b000331 | furniture | pages [20] -->
获取更多资讯

<!-- b000332 | furniture | pages [21] -->
Team # 2403774                                                                                 Page 21 of 23

<!-- b000334 | caption | pages [21] -->
Figure 17: Visualization of women's singles scores and potential quantification

<!-- b000335 | prose | pages [21] -->
In this simulation, the XGBoost potential energy prediction model achieved an MSE (Mean Squared Error) metric of 0.025, indicating a high level of accuracy.

<!-- b000336 | heading | pages [21] -->
7.2 Model Evaluation

<!-- b000337 | prose | pages [21] -->
From the results in section 7.1, it is evident that the model also demonstrates high accuracy in simulating other matches. If the model's accuracy were to decrease, we would consider the following scenarios: the partial elimination of influential independent variables during variable selection, the neglect of other highly influential independent variables in other matches, and more. We would address these issues through the following approaches:

<!-- b000338 | prose | pages [21] -->
1. Conduct residual analysis on the model to identify systematic biases or uncaptured nonlinear relationships within the model.

<!-- b000339 | prose | pages [21] -->
2. Introduce external data to retrain the model and enhance its predictive capabilities.

<!-- b000340 | prose | pages [21] -->
3. Perform error analysis on the model's performance to determine if issues arise from data quality problems such as missing values, outliers, or incorrect data labels.

<!-- b000341 | prose | pages [21] -->
4. Collaborate with domain experts to explore whether there are essential, yet overlooked factors or relationships.

<!-- b000342 | prose | pages [21] -->
Our model exhibits strong generality for other matches, as demonstrated in section 7.1, where women's singles data was used to verify its applicability. In various matches, as long as we possess sufficient independent variable data, we can retrain a suitable model with high precision.

<!-- b000343 | heading | pages [21] -->
8 Sensitivity Analysis

<!-- b000344 | prose | pages [21] -->
To validate the sensitivity of our model to variable changes, i.e., the impact of input variations on the output momentum estimates, we randomly selected some data points from the entire dataset and modified the values of certain variables, including serve speed and running distance. We compared the changes in predicted momentum and the probability of a turning point occurrence to investigate the model's sensitivity to input changes.

<!-- b000345 | prose | pages [21] -->
We randomly selected 10 data points from all the data, used the XGBoost momentum prediction model to estimate momentum, and altered the "speed_mph" variable by ±5%. The experimental results are shown in the left figure, indicating that increasing serve speed can enhance the kinetic energy of players by 2.9%, while decreasing it can reduce the kinetic energy of players by 2.1%.

<!-- b000346 | prose | pages [21, 22] -->
关注数学模型 微信公众号：数学模型

<!-- b000347 | furniture | pages [21] -->
2

<!-- b000348 | furniture | pages [21] -->
MATHmodels

<!-- b000349 | furniture | pages [21] -->
获取更多资讯

<!-- b000350 | furniture | pages [22] -->
Team # 2403774                                                                                 Page 22 of 23

<!-- b000352 | caption | pages [22] -->
Figure 18: Sensitivity Analysis

<!-- b000353 | prose | pages [22] -->
We also selected 10 data points where a turning point occurred and altered "Total_Distance_Match_1" for Player 1 by ±10%. We then used the model from Task 3 to compare the changes in the probability of a turning point occurrence. The experimental results indicate that when athletes increase their energy expenditure, it may increase the probability of a turning point occurring by 3.4%. Conversely, decreasing energy expenditure may reduce the probability of a 微信号：MATHmodels turning point occurring by 4.1%.

<!-- b000354 | heading | pages [22] -->
9 Advantages and Disadvantages Analysis

<!-- b000355 | heading | pages [22] -->
9.1 Advantages

<!-- b000356 | prose | pages [22] -->
(1) The model employed in this paper combines machine learning and deep learning technologies, demonstrating remarkable adaptability and versatility. These models can handle inconsistent game data parameter settings and optimize model parameters to match the characteristics of specific game data through an automated training process.

<!-- b000357 | prose | pages [22] -->
(2) This paper uses an XGBoost-based quantitative prediction model, which boasts fast training speed and efficient execution performance, optimizing computational speed through parallel processing. Additionally, XGBoost offers high flexibility, allowing for customized optimization goals and evaluation criteria, reducing overfitting risk through regularization, and enhancing model generalization.

<!-- b000358 | prose | pages [22] -->
(3) The experimental design of this paper utilizes a five-fold cross-validation strategy, which offers three main advantages: reducing overfitting risk, improving model generalization, and providing reliable performance estimates.

<!-- b000359 | prose | pages [22] -->
(4) The advantages of the multi-timescale temporal convolutional model in tennis turning point prediction are summarized as follows: it can capture features at different time scales, enhance model generalization, improve the capture of time dependencies, and support irregular data sampling, ultimately improving prediction accuracy and model adaptability.

<!-- b000360 | heading | pages [22] -->
9.2 Disadvantages

<!-- b000361 | prose | pages [22] -->
(1) The model may not consider all relevant independent variables comprehensively, potentially leading to information omissions that could affect model accuracy.

<!-- b000362 | prose | pages [22] -->
(2) The multi-timescale temporal convolutional network may increase computational complexity. Since this model needs to simultaneously process information at multiple time scales, it may result in higher computational costs and resource requirements.

<!-- b000363 | prose | pages [22] -->
关注数学模型

<!-- b000364 | furniture | pages [22] -->
2

<!-- b000365 | furniture | pages [22] -->
MATHmodels

<!-- b000366 | furniture | pages [22] -->
获取更多资讯

<!-- b000367 | furniture | pages [23] -->
Team # 2403774                                                                                 Page 23 of 23

<!-- b000368 | heading | pages [23] -->
References

<!-- b000369 | references | pages [23] -->
[1] Shrestha N. Detecting multicollinearity in regression analysis[J]. American Journal of Applied

<!-- b000370 | references | pages [23] -->
Mathematics and Statistics, 2020, 8(2): 39-42.

<!-- b000371 | references | pages [23] -->
微信公众号：数学模型

<!-- b000372 | references | pages [23] -->
[2] Daoud J I. Multicollinearity and regression analysis[C]//Journal of Physics: Conference Series.

<!-- b000373 | references | pages [23] -->
IOP Publishing, 2017, 949(1): 012009.

<!-- b000374 | references | pages [23] -->
[3] Yu H, Cui P, He Y, et al. Stable learning via sparse variable independence[C]//Proceedings of the

<!-- b000375 | references | pages [23] -->
AAAI Conference on Artificial Intelligence. 2023, 37(9): 10998-11006.

<!-- b000376 | references | pages [23] -->
[4] Lee K Y, Li B, Zhao H. Variable selection via additive conditional independence[J]. J

<!-- b000377 | references | pages [23] -->
ournal of

<!-- b000378 | references | pages [23] -->
the Royal Statistical Society Series B: Statistical Methodology, 2016, 78(5): 1037-1055.

<!-- b000379 | references | pages [23] -->
[5] Wang F, Li W, Padilla O H M, et al. Multilayer random dot product graphs: Estimation and online

<!-- b000380 | references | pages [23] -->
inflection point detection[J]. arXiv preprint arXiv:2306.15286, 2023.

<!-- b000381 | references | pages [23] -->
[6] Cao Z, Seeuws N, De Vos M, et al. Inflection point Detection in Multi-

<!-- b000382 | references | pages [23] -->
Channel Time Series Via

<!-- b000383 | references | pages [23] -->
a Time-Invariant Representation[J]. IEEE Transactions on Knowledge and Data Engineering,

<!-- b000384 | references | pages [23] -->
2023.

<!-- b000385 | references | pages [23] -->
微信号：MATHmodels

<!-- b000386 | references | pages [23] -->
[7] Sellier J, Dellaportas P. Bayesian online inflection point detection with Hilbert space

<!-- b000387 | references | pages [23] -->
approximate Student-t process[C]//International Conference on Machine Learning. PMLR, 2023:

<!-- b000388 | references | pages [23] -->
30553-30569.

<!-- b000389 | references | pages [23] -->
[8] Kadra A, Lindauer M, Hutter F, et al. Well-tuned simple nets excel on tabular datasets[J].

<!-- b000390 | references | pages [23] -->
Advances in neural information processing systems, 2021, 34: 23928-23941.

<!-- b000391 | references | pages [23] -->
[9] Kadra A, Lindauer M, Hutter F, et al. Well-tuned simple nets excel on tabular datasets[J].

<!-- b000392 | references | pages [23] -->
Advances in neural information processing systems, 2021, 34: 23928-23941.

<!-- b000393 | references | pages [23] -->
[10] Sedgwick P. Spearman’s rank correlation coefficient[J]. B, 2014, 349.

<!-- b000394 | references | pages [23] -->
[11] Heydarian M, Doyle T E, Samavi R. MLCM: Multi-label confusionmatrix[J]. IEEEAccess, 2022,

<!-- b000395 | references | pages [23] -->
10: 19083-19095.

<!-- b000396 | references | pages [23] -->
[12]

<!-- b000397 | references | pages [23] -->
Takahashi H, Okamura S, Murakami S. Performance analysis in tennis since 2000: A systematic

<!-- b000398 | references | pages [23] -->
review focused on the methods of data collection[J]. 2022.

<!-- b000399 | references | pages [23] -->
[13] Data-driven analysis of point-by-point performance for male tennis player in Grand Slams

<!-- b000400 | references | pages [23] -->
https://revistas.rcaap.pt/motricidade/article/view/16370.

<!-- b000401 | references | pages [23] -->
关注数学模型

<!-- b000402 | furniture | pages [23] -->
2

<!-- b000403 | furniture | pages [23] -->
MATHmodels

<!-- b000404 | furniture | pages [23] -->
获取更多资讯

<!-- b000405 | references | pages [24] -->
Tennis

<!-- b000406 | references | pages [24] -->
Dear Sir/Madam,

<!-- b000407 | references | pages [24] -->
微信公众号：数学模型

<!-- b000408 | references | pages [24] -->
I am writing to propose a visonary approach to tennis coaching that leverages advanced analytics and

<!-- b000409 | references | pages [24] -->
machine leaning to redefine our players' training and performance enhancement.

<!-- b000410 | references | pages [24] -->
Given the evolving comprtitive nature of tennis,it’s clear that traditional methods along can’t unlock our

<!-- b000411 | references | pages [24] -->
player’full potential. As data reshapes sports, our approach to coaching must adapt to maintain a leading edge.

<!-- b000412 | references | pages [24] -->
To achieve this, we undertook the following tasks:

<!-- b000413 | references | pages [24] -->
Firstly, we conducted data cleaning, feature extraction, an analysis of autocorrelation among independent

<!-- b000414 | references | pages [24] -->
variables, and ranked the correlation between independent and dependent variables.

<!-- b000415 | references | pages [24] -->
Next, we introduced the concept of "potential energy" and developed a potential energy prediction model

<!-- b000416 | references | pages [24] -->
based on the XGBoost algorithm. We quantified the relationship between independent variables and potential

<!-- b000417 | references | pages [24] -->
微信号：MATHmodels

<!-- b000418 | references | pages [24] -->
energy and visualized this quantitative relationship using visualization techniques.

<!-- b000419 | references | pages [24] -->
Subsequently,we simulated random match scenarios and analyzed the impact of potencial energy on

<!-- b000420 | references | pages [24] -->
scores. By calculating the Pearson correlation coefficient, we confirmed that player scores in matches are not r

<!-- b000421 | references | pages [24] -->
andom but are significantly influenced by potential energy.

<!-- b000422 | references | pages [24] -->
Furthermore, we applied Bayesian online change point detection methods to successfully identify crucial

<!-- b000423 | references | pages [24] -->
turning points in matches. We conducted correlation analyses of these change points, thereby determining the

<!-- b000424 | references | pages [24] -->
importance ranking of 18 independent variables.

<!-- b000425 | references | pages [24] -->
For further application,we developed the Tennis Match Point Time-Convolution Model,which can

<!-- b000426 | references | pages [24] -->
predict when critical turning points are likely to occur during matches.

<!-- b000427 | references | pages [24] -->
Finally,by analyzing data from the 2003 Wimbledon women’s singles match,we validated the wide

<!-- b000428 | references | pages [24] -->
applicability of our model and conducted comprehensive evaluations and sensitivity analyses.

<!-- b000429 | references | pages [24] -->
Our research not only serves as a reference for future studies in related fields ,but also provides practical

<!-- b000430 | references | pages [24] -->
tools. By applying our model, one can effectively monitor player potential energy, make timely strategy adjust

<!-- b000431 | references | pages [24] -->
-ments, predict changes in match dynamics, and be well-prepared for them.

<!-- b000432 | references | pages [24] -->
I believe that by implementing these datadriven strategies, we can transform our coaching into a high

<!-- b000433 | references | pages [24] -->
precision science, making us pioneers in the tennis coaching arena. This innovative approach will empower

<!-- b000434 | references | pages [24] -->
our players to reach unprecedented heights and achieve a competitive edge on the tennis court.I look forward

<!-- b000435 | references | pages [24] -->
to engaging in a dialogue to discuss these recommendations in depth and devise a roadmap for their seamless

<!-- b000436 | references | pages [24] -->
integration into our coaching philosophy.

<!-- b000437 | references | pages [24] -->
Warm regards,

<!-- b000438 | references | pages [24] -->
Bill

<!-- b000439 | references | pages [24] -->
关注数学模型

<!-- b000440 | furniture | pages [24] -->
2

<!-- b000441 | furniture | pages [24] -->
MATHmodels

<!-- b000442 | furniture | pages [24] -->
获取更多资讯
