# P-C-2025-2510185-3f933168

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2025

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2510185

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Maximizing Medal Performance: Athlete and Event

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | title | pages [1] -->
Potential Indices

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
As the highest-level global sporting event, the Olympic Games attract worldwide attention. Olympic achievements not only represent the limits of human athletic performance but also reflect comprehensive national strength.

<!-- b000013 | prose | pages [1] -->
First, after data preprocessing, we introduce the Athlete Potential Index (API) to quantify athlete performance. We define the API as an exponentially decaying function of Medals won by an athlete/team (PWM). The PWM exhibits a linear relationship with the number of Gold, Sil- ver, and Bronze medals. Following a comparison of various models, we select a Random Forest

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
(RF) model optimized using Grid SearchCV. The optimal hyperparameters are [max_depth=10, min_samples_split=4, n_estimators=180], achieving an R-squared (R²) value of 0.8792. Conse- quently, we employ the RF model with bootstrapping to generate 95% confidence intervals for medal predictions. Our analysis suggests that the United States is most likely to improve its medal count, while South Korea is most likely to experience a decrease.

<!-- b000016 | prose | pages [1] -->
Then, to predict medal acquisition by medal-less nations/regions, we employ a BP neural network classifier after comparing several classification models. The classifier achieves an Area Under the ROC Curve (AUC) of 0.94. We apply this model to predict medal acquisition for 77 nations/regions. The nations/regions with the highest probability of winning their first medal are Guam (GUM) and ESA, with Guam having a probability of 0.153.

<!-- b000017 | prose | pages [1] -->
Subsequently, we analyzed the six nations/regions’ participation and medal counts across dif- ferent events. Utilizing the feature importance attribute of the Random Forest model, we predict medal counts and derive the importance of various sports for each nation (Figure 11). Swimming emerges as a significant sport for most nations analyzed.

<!-- b000018 | prose | pages [1] -->
Next, to investigate the impact of “Great Coach” we compile a list of renowned coaches in sports such as gymnastics, athletics, and swimming. We use the Random Forest model to predict changes in medal counts attributed to these coaches. Our results indicate that “Great Coach” contribute up to 28.8% to performance improvement. Specifically, at an average athlete API of 70, the presence of a “Great Coach” is associated with an increase of 0.2 gold medals and 1.8 total medals. We introduce the Event Potential Index (EPI) to quantify the potential improvement after hiring a “Great Coach”. We recommend that China consider hiring a “Great Coach” for women’s gymnastics, Germany for men’s shooting, and Jamaica for men’s athletics, which is projected to yield an increase of approximately 1.6 medals.

<!-- b000019 | prose | pages [1] -->
Finally We made new discoveries and provided suggestions on (1)Number of participants; (2)Events with negative importance; (3)Projects suitable for hiring great coaches. Next, by vary- ing the dataset size, we assessed the impact on prediction and information gain. we observed minimal changes in both. This demonstrates the model’s strong robustness.

<!-- b000020 | keywords | pages [1] -->
Keywords: Athlete Potential Index; Event Potential Index; Random Forest; BP Neural Network

<!-- b000021 | prose | pages [1] -->
Classifier

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | heading | pages [2] -->
Introduction

<!-- b000025 | prose | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
1.1 Background

<!-- b000027 | prose | pages [2] -->
3

<!-- b000028 | heading | pages [2] -->
1.2 Restatement of Problem

<!-- b000029 | prose | pages [2] -->
3

<!-- b000030 | heading | pages [2] -->
1.3 Our work

<!-- b000031 | prose | pages [2] -->
4

<!-- b000032 | heading | pages [2] -->
Preparation for Modeling

<!-- b000033 | prose | pages [2] -->
5 2 5 2.1 Assumptions .

<!-- b000034 | heading | pages [2] -->
2.2 Notations

<!-- b000035 | prose | pages [2] -->
5 2.3

<!-- b000036 | heading | pages [2] -->
Data Processing

<!-- b000037 | prose | pages [2] -->
5

<!-- b000038 | heading | pages [2] -->
Task 1: Medal Count Prediction Model

<!-- b000039 | prose | pages [2] -->
7 3 Feature Engineering . . 7 3.1

<!-- b000040 | heading | pages [2] -->
3.1.1 Athlete Potential Index (API)

<!-- b000041 | prose | pages [2] -->
7

<!-- b000042 | heading | pages [2] -->
3.1.2 Participation Scale (PS) . .

<!-- b000043 | prose | pages [2] -->
8 3.2 Model Selection . . 8 Task 1.1: 2028 Olympic VMT Prediction 3.3 11 3.3.1 11

<!-- b000044 | heading | pages [2] -->
Grid SearchCV - Random Forest Model

<!-- b000045 | prose | pages [2] -->
3.3.2 Prediction Results . 11 95% Confidence Intervals by Bootstrap 12 3.3.3 Task 1.2: The Probability of First Medal 12 3.4

<!-- b000046 | heading | pages [2] -->
3.4.1 BP Neural Network Classifier

<!-- b000047 | prose | pages [2] -->
13 Task 1.3: The Impact of Events on Medals 14 3.5 15

<!-- b000048 | heading | pages [2] -->
3.5.2 The Impact of Home Country Events

<!-- b000049 | prose | pages [2] -->
17

<!-- b000050 | prose | pages [2] -->
Task 2: “Great Coach" 18 Contribution to Medals 4

<!-- b000051 | heading | pages [2] -->
4.1 Existence of “Great Coach" Effect

<!-- b000052 | prose | pages [2] -->
18

<!-- b000053 | heading | pages [2] -->
4.2 Contribution of "Great Coach"

<!-- b000054 | prose | pages [2] -->
19

<!-- b000055 | heading | pages [2] -->
4.3 Event Investment and Impact

<!-- b000056 | prose | pages [2] -->
19

<!-- b000057 | heading | pages [2] -->
4.3.1 Event Potential Index (EPI)

<!-- b000058 | prose | pages [2] -->
19 4.3.2 Post-investment Results . 20

<!-- b000059 | prose | pages [2] -->
Task 3: Other Original Insights 21 5

<!-- b000060 | heading | pages [2] -->
5.1 Common Traits of No Medal Nations

<!-- b000061 | prose | pages [2] -->
21 5.21 Negative Impact Events 21 5.3 21

<!-- b000062 | heading | pages [2] -->
Recommendations of “Great Coach'

<!-- b000063 | prose | pages [2] -->
1 22 6

<!-- b000064 | heading | pages [2] -->
6.1 Sensitivity Analysis

<!-- b000065 | prose | pages [2] -->
22 Strengths and Weaknesses . 22 6.2

<!-- b000066 | heading | pages [2] -->
Conclusions

<!-- b000067 | prose | pages [2] -->
24 7

<!-- b000068 | heading | pages [2] -->
References

<!-- b000069 | references | pages [2] -->
24

<!-- b000070 | references | pages [2] -->
关注数学模型

<!-- b000071 | furniture | pages [2] -->
获取更多资讯

<!-- b000072 | furniture | pages [3] -->
Page 3 of 24

<!-- b000073 | furniture | pages [3] -->
Team #2510185

<!-- b000074 | heading | pages [3] -->
Introduction

<!-- b000075 | prose | pages [3] -->
1

<!-- b000076 | heading | pages [3] -->
Background

<!-- b000077 | prose | pages [3] -->
1.1

<!-- b000078 | prose | pages [3] -->
The Olympic Games are the world's most prestigious sporting event, and in most of the time, becoming an Olympic champion is regarded as the highest honor in sports[1]. This pursuit of excellence naturally fosters intense competition between nations and regions, with the medal count serving as a key indicator of sporting prowess on the global stage.

<!-- b000079 | prose | pages [3] -->
At the recently concluded Paris 2024 Olympic Games, the United States and China led the medal count (tied for the most gold medals), followed by Japan, Australia, and host nation France[2]. Notably, several countries, including Albania, achieved historic first-time Olympic medals.

<!-- b000080 | prose | pages [3] -->
Some studies predict medal counts based on a country's political and economic context[3], while others focus on the recent performance of athletes at the Games[4]. These approaches have consistently achieved high accuracy. In this study, we aim to explore patterns in medal counts 光 using historical Olympic data.

<!-- b000081 | prose | pages [3] -->
PARiS 2O24

<!-- b000082 | prose | pages [3] -->
Sliver NOC Gold Sliver Total NOC Gold Total Bronze Bronze

<!-- b000083 | prose | pages [3] -->
126 40 44 United States 42

<!-- b000084 | prose | pages [3] -->
27 24 91 China 40

<!-- b000085 | prose | pages [3] -->
20 12 13 45 Japan 18 19 53 16 Australia

<!-- b000086 | prose | pages [3] -->
16 16 22 France 64

<!-- b000087 | prose | pages [3] -->
15 12 34 Netherlands 7

<!-- b000088 | caption | pages [3] -->
Figure 1: From Paris 2024 to LA 2028: Medal Table Prediction

<!-- b000089 | heading | pages [3] -->
1.2 Restatement of Problem

<!-- b000090 | prose | pages [3] -->
The challenge is to analyze and predict the medal table for the 2028 Los Angeles Olympics using publicly available data from all previous Summer Olympics. In addition, other patterns, including the "Great Coach" effect, should be explored. The specific questions are:

<!-- b000091 | heading | pages [3] -->
Build a Medal count prediction model:

<!-- b000092 | prose | pages [3, 4] -->
The model should include at least gold medals and total medals. Measure the performance of the model and estimate the uncertainty or accuracy of the prediction.

<!-- b000093 | furniture | pages [4] -->
Team #2510185

<!-- b000094 | furniture | pages [4] -->
Page 4 of 24

<!-- b000096 | prose | pages [4] -->
• Specific Event type analysis:

<!-- b000097 | prose | pages [4] -->
Consider the number and types of events, explore the relationships between events, and the number of medals won by each country in each event. Examine the most dominant events in each country, and analyze the reasons and impact on the results.

<!-- b000098 | prose | pages [4] -->
• Model prediction:

<!-- b000099 | prose | pages [4] -->
1. Predict the medal table for the 2028 Summer Olympics in Los Angeles and give a prediction interval for the result. Analyze countries that may improve or decline.

<!-- b000100 | prose | pages [4] -->
2. Focus on countries/regions that have not yet won a medal and predict their probability of winning their first medal at the 2028 Olympics.

<!-- b000101 | prose | pages [4] -->
• Explore the existence of the "Great Coach" effect:

<!-- b000102 | prose | pages [4] -->
Look for changes due to the "Great Coach" effect and estimate its impact on medal changes.

<!-- b000103 | prose | pages [4] -->
Select three countries, determine the sports in which they should consider investing in a great coach, and estimate the impact.

<!-- b000104 | prose | pages [4] -->
• Explore other patterns:

<!-- b000105 | prose | pages [4] -->
Analyze other patterns related to the number of medals displayed by the model. Use these findings to inform the Olympic committees of various countries.

<!-- b000106 | heading | pages [4] -->
1.3 Our work

<!-- b000107 | prose | pages [4] -->
Task 1: Medal prediction by API Task 2: The impact of “Great Coach” Gold Event select Performance of a athlete(PWM) Sliver n_estimators max_depth min_samples_split 180 10 4 Bronze 3 models Event Potential Index(EPI) Athlete Potential Index(API) Grid searchCV Comparison Participation scale(PS) R2 =0.8792 … Features Random Trend Pressure AAPI Space Forest EPI=ω1×Total_trend+ω2×Total_space+ω3×AAPI Task 1.3 Task 1.2 Task 1.1 Model Prediction BP neural network Events improtance Bootstrap The Contribution of “Great Coach” : 28.8% classification •AAPI≈65，Bronze 0.9, Sliver 0.2, Gold 0.02, Total 1.2 VMT •AAPI≈70，Bronze 0.7, Sliver 0.9, Gold 0.2 , Total 1.8 USA 95% Confidence

<!-- b000108 | heading | pages [4] -->
Sensitivity Analyses

<!-- b000109 | prose | pages [4] -->
KOR

<!-- b000110 | prose | pages [4] -->
50% cross validation 60,70,80% Training set Task 3: original insights R2 =0.7642 Small fluctuations Suggestions for the Unawarded countries Medals of negative 'Great Coach' Effect get medal importance High Level of Robustness

<!-- b000111 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000112 | prose | pages [4] -->
关注数学模型

<!-- b000113 | furniture | pages [4] -->
2

<!-- b000114 | furniture | pages [4] -->
MATHmodels

<!-- b000115 | furniture | pages [4] -->
获取更多资讯

<!-- b000116 | furniture | pages [5] -->
Team #2510185

<!-- b000117 | furniture | pages [5] -->
Page 5 of 24

<!-- b000118 | heading | pages [5] -->
2 Preparation for Modeling

<!-- b000119 | heading | pages [5] -->
2.1 Assumptions

<!-- b000120 | prose | pages [5] -->
We make the following assumptions to complete our model. In addition, we will refine these simplified assumptions later.

<!-- b000121 | prose | pages [5] -->
• We assume that an athlete’s competitive ability can be fully inferred from the historical data provided. This is because the given dataset only contains information about a player’s 微信公众号：数学模型 participation in previous Olympic Games and the medals he won (gold, silver, or bronze).

<!-- b000122 | prose | pages [5] -->
We believe that a player’s ability based on this information is sufficient.

<!-- b000123 | prose | pages [5] -->
• We assume that the competitive ability of an athlete or team remains constant over the four years between games. This is because we cannot obtain any other information about athletes between Games from the dataset provided.

<!-- b000124 | prose | pages [5] -->
• We assume that the probability of a country that has never won a medal to win a medal is only related to the historical data of previous participation. This is because there is no more realistic data on countries that have never won a medal in the data set provided.

<!-- b000125 | prose | pages [5] -->
Although this may be a relatively important factor. 微信号：MATHmodels

<!-- b000126 | heading | pages [5] -->
2.2 Notations

<!-- b000127 | caption | pages [5] -->
Table 1: Notations Table

<!-- b000128 | heading | pages [5] -->
Symbol

<!-- b000129 | prose | pages [5] -->
Description

<!-- b000130 | prose | pages [5] -->
PES Performance score of an athlete/team PWM Medals won by an athlete/team HA Host advantage The Olympic Games of number i Ni API Athlete Potential Index EPI Event Potential Index PS Scale of Participation (by NOC)

<!-- b000131 | heading | pages [5] -->
2.3 Data Processing

<!-- b000132 | prose | pages [5] -->
After observing the datasets provided by the topic, summerOly_athletes.csv, summerOly_hosts.csv, summerOly_medal_counts.csv and summerOly_programs.csv contain some abnormal or missing values. The following describes the data processing of these abnormal and missing values. Further data processing will be done as needed in the later text. The processing procedures are shown in

<!-- b000133 | caption | pages [5] -->
Figure 3.

<!-- b000134 | prose | pages [5, 6] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m SummerOly_athletes

<!-- b000135 | furniture | pages [5] -->
m

<!-- b000136 | furniture | pages [5] -->
m

<!-- b000137 | furniture | pages [5] -->
m

<!-- b000138 | furniture | pages [5] -->
m

<!-- b000139 | furniture | pages [5] -->
m

<!-- b000140 | furniture | pages [5] -->
m

<!-- b000141 | furniture | pages [5] -->
m

<!-- b000142 | furniture | pages [5] -->
m

<!-- b000143 | furniture | pages [5] -->
m

<!-- b000144 | furniture | pages [5] -->
m

<!-- b000145 | furniture | pages [5] -->
m

<!-- b000146 | furniture | pages [5] -->
m

<!-- b000147 | furniture | pages [5] -->
m

<!-- b000148 | furniture | pages [5] -->
m

<!-- b000149 | furniture | pages [5] -->
m

<!-- b000150 | furniture | pages [5] -->
m

<!-- b000151 | furniture | pages [5] -->
m

<!-- b000152 | furniture | pages [5] -->
m

<!-- b000153 | furniture | pages [5] -->
m

<!-- b000154 | furniture | pages [5] -->
m

<!-- b000155 | furniture | pages [5] -->
m

<!-- b000156 | furniture | pages [5] -->
m

<!-- b000157 | furniture | pages [5] -->
m

<!-- b000158 | furniture | pages [5] -->
m

<!-- b000159 | furniture | pages [5] -->
m

<!-- b000160 | furniture | pages [5] -->
m

<!-- b000161 | furniture | pages [5] -->
m

<!-- b000162 | furniture | pages [5] -->
m

<!-- b000163 | furniture | pages [5] -->
m

<!-- b000164 | furniture | pages [5] -->
m

<!-- b000165 | furniture | pages [5] -->
m

<!-- b000166 | furniture | pages [5] -->
m

<!-- b000167 | furniture | pages [5] -->
m

<!-- b000168 | furniture | pages [5] -->
m

<!-- b000169 | furniture | pages [5] -->
m

<!-- b000170 | furniture | pages [5] -->
m

<!-- b000171 | furniture | pages [5] -->
m

<!-- b000172 | furniture | pages [5] -->
m

<!-- b000173 | furniture | pages [5] -->
m

<!-- b000174 | furniture | pages [5] -->
m

<!-- b000175 | furniture | pages [5] -->
m

<!-- b000176 | furniture | pages [5] -->
m

<!-- b000177 | furniture | pages [5] -->
m

<!-- b000178 | furniture | pages [5] -->
m

<!-- b000179 | furniture | pages [5] -->
m

<!-- b000180 | furniture | pages [5] -->
m

<!-- b000181 | furniture | pages [5] -->
m

<!-- b000182 | furniture | pages [5] -->
m

<!-- b000183 | furniture | pages [5] -->
m

<!-- b000184 | furniture | pages [5] -->
m

<!-- b000185 | furniture | pages [5] -->
m

<!-- b000186 | furniture | pages [5] -->
m

<!-- b000187 | furniture | pages [5] -->
m

<!-- b000188 | furniture | pages [5] -->
m

<!-- b000189 | furniture | pages [5] -->
m

<!-- b000190 | furniture | pages [5] -->
m

<!-- b000191 | furniture | pages [5] -->
m

<!-- b000192 | furniture | pages [5] -->
m

<!-- b000193 | furniture | pages [5] -->
m

<!-- b000194 | furniture | pages [5] -->
m

<!-- b000195 | furniture | pages [5] -->
m

<!-- b000196 | furniture | pages [5] -->
m

<!-- b000197 | furniture | pages [5] -->
m

<!-- b000198 | furniture | pages [5] -->
m

<!-- b000199 | furniture | pages [5] -->
m

<!-- b000200 | furniture | pages [5] -->
m

<!-- b000201 | furniture | pages [5] -->
m

<!-- b000202 | furniture | pages [5] -->
m

<!-- b000203 | furniture | pages [5] -->
m

<!-- b000204 | furniture | pages [5] -->
m

<!-- b000205 | furniture | pages [5] -->
m

<!-- b000206 | furniture | pages [5] -->
m

<!-- b000207 | furniture | pages [5] -->
m

<!-- b000208 | furniture | pages [5] -->
m

<!-- b000209 | furniture | pages [5] -->
m

<!-- b000210 | furniture | pages [5] -->
m

<!-- b000211 | furniture | pages [5] -->
m

<!-- b000212 | furniture | pages [5] -->
m

<!-- b000213 | furniture | pages [5] -->
m

<!-- b000214 | furniture | pages [5] -->
m

<!-- b000215 | furniture | pages [5] -->
m

<!-- b000216 | furniture | pages [5] -->
m

<!-- b000217 | furniture | pages [5] -->
m

<!-- b000218 | furniture | pages [5] -->
m

<!-- b000219 | furniture | pages [5] -->
m

<!-- b000220 | furniture | pages [5] -->
m

<!-- b000221 | furniture | pages [5] -->
m

<!-- b000222 | furniture | pages [5] -->
m

<!-- b000223 | furniture | pages [5] -->
m

<!-- b000224 | furniture | pages [5] -->
m

<!-- b000225 | furniture | pages [5] -->
m

<!-- b000226 | furniture | pages [5] -->
m

<!-- b000227 | furniture | pages [5] -->
m

<!-- b000228 | furniture | pages [5] -->
m

<!-- b000229 | furniture | pages [5] -->
m

<!-- b000230 | furniture | pages [5] -->
m

<!-- b000231 | furniture | pages [5] -->
m

<!-- b000232 | furniture | pages [5] -->
m

<!-- b000233 | furniture | pages [5] -->
m

<!-- b000234 | furniture | pages [5] -->
m

<!-- b000235 | furniture | pages [5] -->
m

<!-- b000236 | furniture | pages [5] -->
m

<!-- b000237 | furniture | pages [5] -->
m

<!-- b000238 | furniture | pages [5] -->
m

<!-- b000239 | furniture | pages [5] -->
m

<!-- b000240 | furniture | pages [5] -->
m

<!-- b000241 | furniture | pages [5] -->
m

<!-- b000242 | furniture | pages [5] -->
m

<!-- b000243 | furniture | pages [5] -->
m

<!-- b000244 | furniture | pages [5] -->
m

<!-- b000245 | furniture | pages [5] -->
m

<!-- b000246 | furniture | pages [5] -->
m

<!-- b000247 | furniture | pages [5] -->
m

<!-- b000248 | furniture | pages [5] -->
m

<!-- b000249 | furniture | pages [5] -->
m

<!-- b000250 | furniture | pages [5] -->
m

<!-- b000251 | furniture | pages [5] -->
m

<!-- b000252 | furniture | pages [5] -->
m

<!-- b000253 | furniture | pages [5] -->
m

<!-- b000254 | furniture | pages [5] -->
m

<!-- b000255 | furniture | pages [5] -->
m

<!-- b000256 | furniture | pages [5] -->
m

<!-- b000257 | furniture | pages [5] -->
m

<!-- b000258 | furniture | pages [5] -->
m

<!-- b000259 | furniture | pages [5] -->
m

<!-- b000260 | furniture | pages [5] -->
m

<!-- b000261 | furniture | pages [5] -->
m

<!-- b000262 | furniture | pages [5] -->
m

<!-- b000263 | furniture | pages [5] -->
m

<!-- b000264 | furniture | pages [5] -->
m

<!-- b000265 | furniture | pages [5] -->
m

<!-- b000266 | furniture | pages [5] -->
m

<!-- b000267 | furniture | pages [5] -->
m

<!-- b000268 | furniture | pages [5] -->
m

<!-- b000269 | furniture | pages [5] -->
m

<!-- b000270 | furniture | pages [5] -->
m

<!-- b000271 | furniture | pages [5] -->
m

<!-- b000272 | furniture | pages [5] -->
m

<!-- b000273 | furniture | pages [5] -->
m

<!-- b000274 | furniture | pages [5] -->
m

<!-- b000275 | furniture | pages [5] -->
m

<!-- b000276 | furniture | pages [5] -->
m

<!-- b000277 | furniture | pages [5] -->
m

<!-- b000278 | furniture | pages [5] -->
m

<!-- b000279 | furniture | pages [5] -->
m

<!-- b000280 | furniture | pages [5] -->
m

<!-- b000281 | furniture | pages [5] -->
m

<!-- b000282 | furniture | pages [5] -->
m

<!-- b000283 | furniture | pages [5] -->
m

<!-- b000284 | furniture | pages [5] -->
m

<!-- b000285 | furniture | pages [5] -->
m

<!-- b000286 | furniture | pages [5] -->
m

<!-- b000287 | furniture | pages [5] -->
m

<!-- b000288 | furniture | pages [5] -->
m

<!-- b000289 | furniture | pages [5] -->
m

<!-- b000290 | furniture | pages [5] -->
m

<!-- b000291 | furniture | pages [5] -->
m

<!-- b000292 | furniture | pages [5] -->
m

<!-- b000293 | furniture | pages [5] -->
m

<!-- b000294 | furniture | pages [5] -->
m

<!-- b000295 | furniture | pages [5] -->
m

<!-- b000296 | furniture | pages [5] -->
m

<!-- b000297 | furniture | pages [5] -->
m

<!-- b000298 | furniture | pages [5] -->
m

<!-- b000299 | furniture | pages [5] -->
m

<!-- b000300 | furniture | pages [5] -->
m

<!-- b000301 | furniture | pages [5] -->
m

<!-- b000302 | furniture | pages [5] -->
m

<!-- b000303 | furniture | pages [5] -->
m

<!-- b000304 | furniture | pages [5] -->
m

<!-- b000305 | furniture | pages [5] -->
m

<!-- b000306 | furniture | pages [5] -->
m

<!-- b000307 | furniture | pages [5] -->
m

<!-- b000308 | furniture | pages [5] -->
m

<!-- b000309 | furniture | pages [5] -->
m

<!-- b000310 | furniture | pages [5] -->
m

<!-- b000311 | furniture | pages [5] -->
m

<!-- b000312 | furniture | pages [5] -->
m

<!-- b000313 | furniture | pages [5] -->
m

<!-- b000314 | furniture | pages [5] -->
m

<!-- b000315 | furniture | pages [5] -->
m

<!-- b000316 | furniture | pages [5] -->
m

<!-- b000317 | furniture | pages [5] -->
m

<!-- b000318 | furniture | pages [5] -->
m

<!-- b000319 | furniture | pages [5] -->
m

<!-- b000320 | furniture | pages [5] -->
m

<!-- b000321 | furniture | pages [5] -->
m

<!-- b000322 | furniture | pages [5] -->
m

<!-- b000323 | furniture | pages [5] -->
m

<!-- b000324 | furniture | pages [5] -->
m

<!-- b000325 | furniture | pages [5] -->
m

<!-- b000326 | furniture | pages [5] -->
m

<!-- b000327 | furniture | pages [5] -->
m

<!-- b000328 | furniture | pages [5] -->
m

<!-- b000329 | furniture | pages [5] -->
m

<!-- b000330 | furniture | pages [5] -->
m

<!-- b000331 | furniture | pages [5] -->
m

<!-- b000332 | furniture | pages [5] -->
m

<!-- b000333 | furniture | pages [5] -->
m

<!-- b000334 | furniture | pages [5] -->
m

<!-- b000335 | furniture | pages [5] -->
m

<!-- b000336 | furniture | pages [5] -->
m

<!-- b000337 | furniture | pages [5] -->
m

<!-- b000338 | furniture | pages [5] -->
m

<!-- b000339 | furniture | pages [5] -->
m

<!-- b000340 | furniture | pages [5] -->
m

<!-- b000341 | furniture | pages [5] -->
m

<!-- b000342 | furniture | pages [5] -->
m

<!-- b000343 | furniture | pages [5] -->
m

<!-- b000344 | furniture | pages [5] -->
m

<!-- b000345 | furniture | pages [5] -->
m

<!-- b000346 | furniture | pages [5] -->
m

<!-- b000347 | furniture | pages [5] -->
m

<!-- b000348 | furniture | pages [5] -->
m

<!-- b000349 | furniture | pages [5] -->
m

<!-- b000350 | furniture | pages [5] -->
m

<!-- b000351 | furniture | pages [5] -->
m

<!-- b000352 | furniture | pages [5] -->
m

<!-- b000353 | furniture | pages [5] -->
m

<!-- b000354 | furniture | pages [5] -->
m

<!-- b000355 | furniture | pages [5] -->
m

<!-- b000356 | furniture | pages [5] -->
m

<!-- b000357 | furniture | pages [5] -->
m

<!-- b000358 | furniture | pages [5] -->
m

<!-- b000359 | furniture | pages [5] -->
m

<!-- b000360 | furniture | pages [5] -->
m

<!-- b000361 | furniture | pages [5] -->
m

<!-- b000362 | furniture | pages [5] -->
m

<!-- b000363 | furniture | pages [5] -->
m

<!-- b000364 | furniture | pages [5] -->
m

<!-- b000365 | furniture | pages [5] -->
m

<!-- b000366 | furniture | pages [5] -->
m

<!-- b000367 | furniture | pages [5] -->
m

<!-- b000368 | furniture | pages [5] -->
m

<!-- b000369 | furniture | pages [5] -->
m

<!-- b000370 | furniture | pages [5] -->
m

<!-- b000371 | furniture | pages [5] -->
m

<!-- b000372 | furniture | pages [5] -->
m

<!-- b000373 | furniture | pages [5] -->
m

<!-- b000374 | furniture | pages [5] -->
m

<!-- b000375 | furniture | pages [5] -->
m

<!-- b000376 | furniture | pages [5] -->
m

<!-- b000377 | furniture | pages [5] -->
m

<!-- b000378 | furniture | pages [5] -->
m

<!-- b000379 | furniture | pages [5] -->
m

<!-- b000380 | furniture | pages [5] -->
m

<!-- b000381 | furniture | pages [5] -->
m

<!-- b000382 | furniture | pages [5] -->
m

<!-- b000383 | furniture | pages [5] -->
m

<!-- b000384 | furniture | pages [5] -->
m

<!-- b000385 | furniture | pages [5] -->
m

<!-- b000386 | furniture | pages [5] -->
m

<!-- b000387 | furniture | pages [5] -->
m

<!-- b000388 | furniture | pages [5] -->
m

<!-- b000389 | furniture | pages [5] -->
m

<!-- b000390 | furniture | pages [5] -->
m

<!-- b000391 | furniture | pages [5] -->
m

<!-- b000392 | furniture | pages [5] -->
m

<!-- b000393 | furniture | pages [5] -->
m

<!-- b000394 | furniture | pages [5] -->
m

<!-- b000395 | furniture | pages [5] -->
m

<!-- b000396 | furniture | pages [5] -->
m

<!-- b000397 | furniture | pages [5] -->
m

<!-- b000398 | furniture | pages [5] -->
m

<!-- b000399 | furniture | pages [5] -->
m

<!-- b000400 | furniture | pages [5] -->
m

<!-- b000401 | furniture | pages [5] -->
m

<!-- b000402 | furniture | pages [5] -->
m

<!-- b000403 | furniture | pages [5] -->
m

<!-- b000404 | furniture | pages [5] -->
m

<!-- b000405 | furniture | pages [5] -->
m

<!-- b000406 | furniture | pages [5] -->
m

<!-- b000407 | furniture | pages [5] -->
m

<!-- b000408 | furniture | pages [5] -->
m

<!-- b000409 | furniture | pages [5] -->
m

<!-- b000410 | furniture | pages [5] -->
m

<!-- b000411 | furniture | pages [5] -->
m

<!-- b000412 | furniture | pages [5] -->
m

<!-- b000413 | furniture | pages [5] -->
m

<!-- b000414 | furniture | pages [5] -->
m

<!-- b000415 | furniture | pages [5] -->
m

<!-- b000416 | furniture | pages [5] -->
m

<!-- b000417 | furniture | pages [5] -->
m

<!-- b000418 | furniture | pages [5] -->
m

<!-- b000419 | furniture | pages [5] -->
m

<!-- b000420 | furniture | pages [5] -->
m

<!-- b000421 | furniture | pages [5] -->
m

<!-- b000422 | furniture | pages [5] -->
m

<!-- b000423 | furniture | pages [5] -->
m

<!-- b000424 | furniture | pages [5] -->
m

<!-- b000425 | furniture | pages [5] -->
m

<!-- b000426 | furniture | pages [5] -->
m

<!-- b000427 | furniture | pages [5] -->
m

<!-- b000428 | furniture | pages [5] -->
m

<!-- b000429 | furniture | pages [5] -->
m

<!-- b000430 | furniture | pages [5] -->
m

<!-- b000431 | furniture | pages [5] -->
m

<!-- b000432 | furniture | pages [5] -->
m

<!-- b000433 | furniture | pages [5] -->
m

<!-- b000434 | furniture | pages [5] -->
m

<!-- b000435 | furniture | pages [5] -->
m

<!-- b000436 | furniture | pages [5] -->
m

<!-- b000437 | furniture | pages [5] -->
m

<!-- b000438 | furniture | pages [5] -->
m

<!-- b000439 | furniture | pages [5] -->
m

<!-- b000440 | furniture | pages [5] -->
m

<!-- b000441 | furniture | pages [5] -->
m

<!-- b000442 | furniture | pages [5] -->
m

<!-- b000443 | furniture | pages [5] -->
m

<!-- b000444 | furniture | pages [5] -->
m

<!-- b000445 | furniture | pages [5] -->
m

<!-- b000446 | furniture | pages [5] -->
m

<!-- b000447 | furniture | pages [5] -->
m

<!-- b000448 | furniture | pages [5] -->
m

<!-- b000449 | furniture | pages [5] -->
m

<!-- b000450 | furniture | pages [5] -->
m

<!-- b000451 | furniture | pages [5] -->
m

<!-- b000452 | furniture | pages [5] -->
m

<!-- b000453 | furniture | pages [5] -->
m

<!-- b000454 | furniture | pages [5] -->
m

<!-- b000455 | furniture | pages [5] -->
m

<!-- b000456 | furniture | pages [5] -->
m

<!-- b000457 | furniture | pages [5] -->
m

<!-- b000458 | furniture | pages [5] -->
m

<!-- b000459 | furniture | pages [6] -->
Team #2510185

<!-- b000460 | furniture | pages [6] -->
Page 6 of 24

<!-- b000461 | caption | pages [6] -->
Figure 3: Data processing

<!-- b000463 | prose | pages [6] -->
The data in the Team column of the SummerOly_athletes.csv file is misaligned or garbled.

<!-- b000464 | prose | pages [6] -->
We noticed that the 1906 Olympics were an intercalated Olympics (unofficial Olympics), and the results were not officially recognized by the International Olympic Committee (IOC). We ulti- mately decided not to use any data from 1906.

<!-- b000465 | prose | pages [6] -->
summerOly_hosts

<!-- b000466 | prose | pages [6] -->
The Host column in the summerOly_hosts.csv dataset contains both countries and cities. To obtain precise information on the host countries, we performed a column-splitting operation to separate the data accordingly.

<!-- b000467 | prose | pages [6] -->
summerOly_medal_counts

<!-- b000468 | prose | pages [6] -->
In the summerOly_medal_counts.csv dataset, the NOC column contains 72 instances of garbled data marked as "??". These entries were removed directly.

<!-- b000469 | prose | pages [6] -->
Additionally, inconsistencies in country names, such as "Great Britain" in this dataset versus "United Kingdom" in other tables, caused mismatches in host information and athlete data. To address this, we standardized the country names across all datasets.

<!-- b000470 | prose | pages [6] -->
summerOly_programs

<!-- b000471 | prose | pages [6] -->
The summerOly_programs.csv file contains missing values and garbled data marked as "?". Missing or garbled entries in columns A–C were corrected using online resources. For columns beyond E, garbled data were removed, and missing values were confirmed to be zeros based on Total events statistics.

<!-- b000472 | prose | pages [6] -->
Significant fluctuations in medal rankings for 1904, 1908, and 1984, likely due to geopolitical factors, led to the exclusion of these years from the analysis.

<!-- b000473 | prose | pages [6] -->
关注数学模型

<!-- b000474 | furniture | pages [6] -->
2

<!-- b000475 | furniture | pages [6] -->
MATHmodels

<!-- b000476 | furniture | pages [6] -->
获取更多资讯

<!-- b000477 | furniture | pages [7] -->
Team #2510185

<!-- b000478 | furniture | pages [7] -->
Page 7 of 24

<!-- b000479 | heading | pages [7] -->
3 Task 1: Medal Count Prediction Model

<!-- b000480 | prose | pages [7] -->
The flowchart for Task 1 is as follows:

<!-- b000481 | prose | pages [7] -->
Data processing Data sorting 微信公众号：数学模型 Linear SVM Feature engineering Adjust the training set regression Random Model selection Classifier model selection XGBoost forest BP neural Random Medal Ranking prediction Medal prediction probability network forest

<!-- b000482 | prose | pages [7] -->
Task1.1: 2028 Medal Table Forecast Task1.2: Prediction of the first medal

<!-- b000483 | prose | pages [7] -->
Data of types and numbers of events 微信号：MATHmodels Number of award-winning athletes

<!-- b000484 | prose | pages [7] -->
RF prediction and importance output

<!-- b000485 | prose | pages [7] -->
Task1.3: The Importance of Events to medals

<!-- b000486 | caption | pages [7] -->
Figure 4: Flowchart for Task 1

<!-- b000487 | heading | pages [7] -->
3.1 Feature Engineering

<!-- b000488 | heading | pages [7] -->
3.1.1 Athlete Potential Index (API)

<!-- b000489 | prose | pages [7] -->
Inspired by Ruiz and Mario’s (2024) research on the Olympic performance index of countries[5], we developed the Athlete Potential Index (API) based on athletes’ previous Olympic medal perfor- mances to describe athletes’ dynamic performance across Olympic Games. This potential index describes an athlete’s past performance and the results they can achieve in the current Olympic event, dynamically adjusted for each Olympic Games.

<!-- b000490 | prose | pages [7] -->
Note that the dataset only provides information about an athlete/team for the last few Olympic Games. Combining relevant papers and parameter tuning practices, we define the API as follows:

<!-- b000491 | prose | pages [7] -->
i i−j 1 X PWM j × API = (1) 2 j=1

<!-- b000492 | prose | pages [7] -->
where i represents the number of the next Olympic Games, and j represents the number of Olympic Games with recorded results.

<!-- b000493 | prose | pages [7] -->
PWM = 100 × NG + 90 × NS + 80 × NB + 60 × NM (2)

<!-- b000494 | prose | pages [7] -->
where,

<!-- b000495 | prose | pages [7, 8] -->
• NG represents the number of gold medals, • NS represents the number of silver medals

<!-- b000496 | furniture | pages [8] -->
Team #2510185

<!-- b000497 | furniture | pages [8] -->
Page 8 of 24

<!-- b000499 | prose | pages [8] -->
• NB represents the number of bronze medals

<!-- b000500 | prose | pages [8] -->
• NM represents the number of events without medals

<!-- b000501 | prose | pages [8] -->
• If the athlete has never participated in a competition, their PWM is 0.

<!-- b000502 | heading | pages [8] -->
3.1.2 Participation Scale (PS)

<!-- b000503 | prose | pages [8] -->
The scale of a country’s participation in the Olympic Games is a factor that is often taken into account[3]. According to the number of athletes representing the country in the Olympic Games, we divide the participation scale into five levels, denoted by 1-5, as defined below:

<!-- b000504 | caption | pages [8] -->
Table 2: Participation Scale (PS) based on Athlete Number

<!-- b000505 | prose | pages [8] -->
Athlete Number Participation Scale (PS)

<!-- b000506 | prose | pages [8] -->
0-9 1 10-49 2 50-99 3 100-149 4 150 or more 5

<!-- b000507 | heading | pages [8] -->
3.2 Model Selection

<!-- b000508 | prose | pages [8] -->
After data processing and feature engineering, we obtain the following features:

<!-- b000509 | caption | pages [8] -->
Table 3: Feature Reference in Model 1

<!-- b000510 | heading | pages [8] -->
Symbol

<!-- b000511 | prose | pages [8] -->
Description

<!-- b000512 | prose | pages [8] -->
Year The year of the Olympic Games N_A Number of Athletes N_E Number of Events AAPI Average of API PS Scale of Participation (by NOC) HS Host advantage N_G Number of Gold N_S Number of Silver N_B Number of Bronze Total Total medals

<!-- b000513 | prose | pages [8] -->
We compiled the above characteristics of the Olympics for five countries: Japan, the United States, France, China, and Great Britain, and formed a dataset to train the model.

<!-- b000514 | prose | pages [8] -->
The correlation matrix for the current feature mapping is shown in Figure 5.

<!-- b000515 | prose | pages [8] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000516 | furniture | pages [8] -->
2

<!-- b000517 | prose | pages [8, 9] -->
m m m m m m m m m m m m m m m m m m m m m m m 微信公众号：数学模型 微信号：MATHmodels

<!-- b000518 | furniture | pages [8] -->
m

<!-- b000519 | furniture | pages [8] -->
m

<!-- b000520 | furniture | pages [8] -->
m

<!-- b000521 | furniture | pages [8] -->
m

<!-- b000522 | furniture | pages [8] -->
m

<!-- b000523 | furniture | pages [8] -->
m

<!-- b000524 | furniture | pages [8] -->
m

<!-- b000525 | furniture | pages [8] -->
m

<!-- b000526 | furniture | pages [8] -->
m

<!-- b000527 | furniture | pages [8] -->
m

<!-- b000528 | furniture | pages [8] -->
m

<!-- b000529 | furniture | pages [8] -->
m

<!-- b000530 | furniture | pages [8] -->
m

<!-- b000531 | furniture | pages [8] -->
m

<!-- b000532 | furniture | pages [8] -->
m

<!-- b000533 | furniture | pages [8] -->
m

<!-- b000534 | furniture | pages [8] -->
m

<!-- b000535 | furniture | pages [8] -->
m

<!-- b000536 | furniture | pages [8] -->
m

<!-- b000537 | furniture | pages [8] -->
m

<!-- b000538 | furniture | pages [8] -->
m

<!-- b000539 | furniture | pages [8] -->
m

<!-- b000540 | furniture | pages [8] -->
m

<!-- b000541 | furniture | pages [8] -->
m

<!-- b000542 | furniture | pages [8] -->
m

<!-- b000543 | furniture | pages [8] -->
m

<!-- b000544 | furniture | pages [8] -->
m

<!-- b000545 | furniture | pages [8] -->
m

<!-- b000546 | furniture | pages [8] -->
m

<!-- b000547 | furniture | pages [8] -->
m

<!-- b000548 | furniture | pages [8] -->
m

<!-- b000549 | furniture | pages [8] -->
m

<!-- b000550 | furniture | pages [8] -->
m

<!-- b000551 | furniture | pages [8] -->
m

<!-- b000552 | furniture | pages [8] -->
m

<!-- b000553 | furniture | pages [8] -->
m

<!-- b000554 | furniture | pages [8] -->
m

<!-- b000555 | furniture | pages [8] -->
m

<!-- b000556 | furniture | pages [8] -->
m

<!-- b000557 | furniture | pages [8] -->
m

<!-- b000558 | furniture | pages [8] -->
m

<!-- b000559 | furniture | pages [8] -->
m

<!-- b000560 | furniture | pages [8] -->
m

<!-- b000561 | furniture | pages [8] -->
m

<!-- b000562 | furniture | pages [8] -->
m

<!-- b000563 | furniture | pages [8] -->
m

<!-- b000564 | furniture | pages [8] -->
m

<!-- b000565 | furniture | pages [8] -->
m

<!-- b000566 | furniture | pages [8] -->
m

<!-- b000567 | furniture | pages [8] -->
m

<!-- b000568 | furniture | pages [8] -->
m

<!-- b000569 | furniture | pages [8] -->
m

<!-- b000570 | furniture | pages [8] -->
m

<!-- b000571 | furniture | pages [8] -->
m

<!-- b000572 | furniture | pages [8] -->
m

<!-- b000573 | furniture | pages [8] -->
m

<!-- b000574 | furniture | pages [8] -->
m

<!-- b000575 | furniture | pages [8] -->
m

<!-- b000576 | furniture | pages [8] -->
m

<!-- b000577 | furniture | pages [8] -->
m

<!-- b000578 | furniture | pages [8] -->
m

<!-- b000579 | furniture | pages [8] -->
m

<!-- b000580 | furniture | pages [8] -->
m

<!-- b000581 | furniture | pages [8] -->
m

<!-- b000582 | furniture | pages [8] -->
m

<!-- b000583 | furniture | pages [8] -->
m

<!-- b000584 | furniture | pages [8] -->
m

<!-- b000585 | furniture | pages [8] -->
m

<!-- b000586 | furniture | pages [8] -->
m

<!-- b000587 | furniture | pages [8] -->
m

<!-- b000588 | furniture | pages [8] -->
m

<!-- b000589 | furniture | pages [8] -->
m

<!-- b000590 | furniture | pages [8] -->
m

<!-- b000591 | furniture | pages [8] -->
m

<!-- b000592 | furniture | pages [8] -->
m

<!-- b000593 | furniture | pages [8] -->
m

<!-- b000594 | furniture | pages [8] -->
m

<!-- b000595 | furniture | pages [8] -->
m

<!-- b000596 | furniture | pages [8] -->
m

<!-- b000597 | furniture | pages [8] -->
m

<!-- b000598 | furniture | pages [8] -->
m

<!-- b000599 | furniture | pages [8] -->
m

<!-- b000600 | furniture | pages [8] -->
m

<!-- b000601 | furniture | pages [8] -->
m

<!-- b000602 | furniture | pages [8] -->
m

<!-- b000603 | furniture | pages [8] -->
m

<!-- b000604 | furniture | pages [8] -->
m

<!-- b000605 | furniture | pages [8] -->
m

<!-- b000606 | furniture | pages [8] -->
m

<!-- b000607 | furniture | pages [8] -->
m

<!-- b000608 | furniture | pages [8] -->
m

<!-- b000609 | furniture | pages [8] -->
m

<!-- b000610 | furniture | pages [8] -->
m

<!-- b000611 | furniture | pages [8] -->
m

<!-- b000612 | furniture | pages [8] -->
m

<!-- b000613 | furniture | pages [8] -->
m

<!-- b000614 | furniture | pages [8] -->
MATHmodels

<!-- b000615 | furniture | pages [8] -->
m

<!-- b000616 | furniture | pages [8] -->
m

<!-- b000617 | furniture | pages [8] -->
m

<!-- b000618 | furniture | pages [8] -->
m

<!-- b000619 | furniture | pages [8] -->
m

<!-- b000620 | furniture | pages [8] -->
m

<!-- b000621 | furniture | pages [8] -->
m

<!-- b000622 | furniture | pages [8] -->
m

<!-- b000623 | furniture | pages [8] -->
m

<!-- b000624 | furniture | pages [8] -->
m

<!-- b000625 | furniture | pages [8] -->
m

<!-- b000626 | furniture | pages [8] -->
m

<!-- b000627 | furniture | pages [8] -->
m

<!-- b000628 | furniture | pages [8] -->
m

<!-- b000629 | furniture | pages [8] -->
m

<!-- b000630 | furniture | pages [8] -->
获取更多资讯

<!-- b000631 | furniture | pages [8] -->
m

<!-- b000632 | furniture | pages [8] -->
m

<!-- b000633 | furniture | pages [8] -->
m

<!-- b000634 | furniture | pages [8] -->
m

<!-- b000635 | furniture | pages [8] -->
m

<!-- b000636 | furniture | pages [8] -->
m

<!-- b000637 | furniture | pages [8] -->
m

<!-- b000638 | furniture | pages [8] -->
m

<!-- b000639 | furniture | pages [8] -->
m

<!-- b000640 | furniture | pages [8] -->
m

<!-- b000641 | furniture | pages [8] -->
m

<!-- b000642 | furniture | pages [8] -->
m

<!-- b000643 | furniture | pages [8] -->
m

<!-- b000644 | furniture | pages [8] -->
m

<!-- b000645 | furniture | pages [8] -->
m

<!-- b000646 | furniture | pages [8] -->
m

<!-- b000647 | furniture | pages [8] -->
m

<!-- b000648 | furniture | pages [8] -->
m

<!-- b000649 | furniture | pages [8] -->
m

<!-- b000650 | furniture | pages [8] -->
m

<!-- b000651 | furniture | pages [8] -->
m

<!-- b000652 | furniture | pages [8] -->
m

<!-- b000653 | furniture | pages [8] -->
m

<!-- b000654 | furniture | pages [8] -->
m

<!-- b000655 | furniture | pages [8] -->
m

<!-- b000656 | furniture | pages [8] -->
m

<!-- b000657 | furniture | pages [8] -->
m

<!-- b000658 | furniture | pages [8] -->
m

<!-- b000659 | furniture | pages [8] -->
m

<!-- b000660 | furniture | pages [8] -->
m

<!-- b000661 | furniture | pages [8] -->
m

<!-- b000662 | furniture | pages [8] -->
m

<!-- b000663 | furniture | pages [8] -->
m

<!-- b000664 | furniture | pages [8] -->
m

<!-- b000665 | furniture | pages [8] -->
m

<!-- b000666 | furniture | pages [8] -->
m

<!-- b000667 | furniture | pages [8] -->
m

<!-- b000668 | furniture | pages [8] -->
m

<!-- b000669 | furniture | pages [8] -->
m

<!-- b000670 | furniture | pages [8] -->
m

<!-- b000671 | furniture | pages [8] -->
m

<!-- b000672 | furniture | pages [8] -->
m

<!-- b000673 | furniture | pages [8] -->
m

<!-- b000674 | furniture | pages [8] -->
m

<!-- b000675 | furniture | pages [8] -->
m

<!-- b000676 | furniture | pages [8] -->
m

<!-- b000677 | furniture | pages [8] -->
m

<!-- b000678 | furniture | pages [8] -->
m

<!-- b000679 | furniture | pages [8] -->
m

<!-- b000680 | furniture | pages [8] -->
m

<!-- b000681 | furniture | pages [8] -->
m

<!-- b000682 | furniture | pages [8] -->
m

<!-- b000683 | furniture | pages [8] -->
m

<!-- b000684 | furniture | pages [8] -->
m

<!-- b000685 | furniture | pages [8] -->
m

<!-- b000686 | furniture | pages [8] -->
m

<!-- b000687 | furniture | pages [8] -->
m

<!-- b000688 | furniture | pages [8] -->
m

<!-- b000689 | furniture | pages [8] -->
m

<!-- b000690 | furniture | pages [8] -->
m

<!-- b000691 | furniture | pages [8] -->
m

<!-- b000692 | furniture | pages [8] -->
m

<!-- b000693 | furniture | pages [8] -->
m

<!-- b000694 | furniture | pages [8] -->
m

<!-- b000695 | furniture | pages [8] -->
m

<!-- b000696 | furniture | pages [8] -->
m

<!-- b000697 | furniture | pages [8] -->
m

<!-- b000698 | furniture | pages [8] -->
m

<!-- b000699 | furniture | pages [8] -->
m

<!-- b000700 | furniture | pages [8] -->
m

<!-- b000701 | furniture | pages [8] -->
m

<!-- b000702 | furniture | pages [8] -->
m

<!-- b000703 | furniture | pages [8] -->
m

<!-- b000704 | furniture | pages [8] -->
m

<!-- b000705 | furniture | pages [8] -->
m

<!-- b000706 | furniture | pages [8] -->
m

<!-- b000707 | furniture | pages [8] -->
m

<!-- b000708 | furniture | pages [8] -->
m

<!-- b000709 | furniture | pages [8] -->
m

<!-- b000710 | furniture | pages [8] -->
m

<!-- b000711 | furniture | pages [8] -->
m

<!-- b000712 | furniture | pages [8] -->
m

<!-- b000713 | furniture | pages [8] -->
m

<!-- b000714 | furniture | pages [8] -->
m

<!-- b000715 | furniture | pages [8] -->
m

<!-- b000716 | furniture | pages [8] -->
m

<!-- b000717 | furniture | pages [8] -->
m

<!-- b000718 | furniture | pages [8] -->
m

<!-- b000719 | furniture | pages [8] -->
m

<!-- b000720 | furniture | pages [8] -->
m

<!-- b000721 | furniture | pages [8] -->
m

<!-- b000722 | furniture | pages [8] -->
m

<!-- b000723 | furniture | pages [8] -->
m

<!-- b000724 | furniture | pages [8] -->
m

<!-- b000725 | furniture | pages [8] -->
m

<!-- b000726 | furniture | pages [8] -->
m

<!-- b000727 | furniture | pages [8] -->
m

<!-- b000728 | furniture | pages [8] -->
m

<!-- b000729 | furniture | pages [8] -->
m

<!-- b000730 | furniture | pages [8] -->
m

<!-- b000731 | furniture | pages [8] -->
m

<!-- b000732 | furniture | pages [8] -->
m

<!-- b000733 | furniture | pages [8] -->
m

<!-- b000734 | furniture | pages [8] -->
m

<!-- b000735 | furniture | pages [8] -->
m

<!-- b000736 | furniture | pages [8] -->
m

<!-- b000737 | furniture | pages [8] -->
m

<!-- b000738 | furniture | pages [8] -->
m

<!-- b000739 | furniture | pages [8] -->
m

<!-- b000740 | furniture | pages [8] -->
m

<!-- b000741 | furniture | pages [8] -->
m

<!-- b000742 | furniture | pages [8] -->
m

<!-- b000743 | furniture | pages [8] -->
m

<!-- b000744 | furniture | pages [8] -->
m

<!-- b000745 | furniture | pages [8] -->
m

<!-- b000746 | furniture | pages [8] -->
m

<!-- b000747 | furniture | pages [8] -->
m

<!-- b000748 | furniture | pages [8] -->
m

<!-- b000749 | furniture | pages [8] -->
m

<!-- b000750 | furniture | pages [8] -->
m

<!-- b000751 | furniture | pages [8] -->
m

<!-- b000752 | furniture | pages [8] -->
m

<!-- b000753 | furniture | pages [8] -->
m

<!-- b000754 | furniture | pages [8] -->
m

<!-- b000755 | furniture | pages [8] -->
m

<!-- b000756 | furniture | pages [8] -->
m

<!-- b000757 | furniture | pages [8] -->
m

<!-- b000758 | furniture | pages [8] -->
m

<!-- b000759 | furniture | pages [8] -->
m

<!-- b000760 | furniture | pages [8] -->
m

<!-- b000761 | furniture | pages [8] -->
m

<!-- b000762 | furniture | pages [8] -->
m

<!-- b000763 | furniture | pages [8] -->
m

<!-- b000764 | furniture | pages [8] -->
m

<!-- b000765 | furniture | pages [8] -->
m

<!-- b000766 | furniture | pages [8] -->
m

<!-- b000767 | furniture | pages [8] -->
m

<!-- b000768 | furniture | pages [8] -->
m

<!-- b000769 | furniture | pages [8] -->
m

<!-- b000770 | furniture | pages [8] -->
m

<!-- b000771 | furniture | pages [8] -->
m

<!-- b000772 | furniture | pages [8] -->
m

<!-- b000773 | furniture | pages [8] -->
m

<!-- b000774 | furniture | pages [8] -->
m

<!-- b000775 | furniture | pages [8] -->
m

<!-- b000776 | furniture | pages [8] -->
m

<!-- b000777 | furniture | pages [8] -->
m

<!-- b000778 | furniture | pages [8] -->
m

<!-- b000779 | furniture | pages [8] -->
m

<!-- b000780 | furniture | pages [8] -->
m

<!-- b000781 | furniture | pages [8] -->
m

<!-- b000782 | furniture | pages [8] -->
m

<!-- b000783 | furniture | pages [8] -->
m

<!-- b000784 | furniture | pages [8] -->
m

<!-- b000785 | furniture | pages [8] -->
m

<!-- b000786 | furniture | pages [8] -->
m

<!-- b000787 | furniture | pages [8] -->
m

<!-- b000788 | furniture | pages [8] -->
m

<!-- b000789 | furniture | pages [8] -->
m

<!-- b000790 | furniture | pages [8] -->
m

<!-- b000791 | furniture | pages [8] -->
m

<!-- b000792 | furniture | pages [8] -->
m

<!-- b000793 | furniture | pages [8] -->
m

<!-- b000794 | furniture | pages [8] -->
m

<!-- b000795 | furniture | pages [8] -->
m

<!-- b000796 | furniture | pages [8] -->
m

<!-- b000797 | furniture | pages [8] -->
m

<!-- b000798 | furniture | pages [8] -->
m

<!-- b000799 | furniture | pages [8] -->
m

<!-- b000800 | furniture | pages [8] -->
m

<!-- b000801 | furniture | pages [8] -->
m

<!-- b000802 | furniture | pages [8] -->
m

<!-- b000803 | furniture | pages [8] -->
m

<!-- b000804 | furniture | pages [8] -->
m

<!-- b000805 | furniture | pages [8] -->
m

<!-- b000806 | furniture | pages [8] -->
m

<!-- b000807 | furniture | pages [8] -->
m

<!-- b000808 | furniture | pages [8] -->
m

<!-- b000809 | furniture | pages [8] -->
m

<!-- b000810 | furniture | pages [8] -->
m

<!-- b000811 | furniture | pages [8] -->
m

<!-- b000812 | furniture | pages [8] -->
m

<!-- b000813 | furniture | pages [8] -->
m

<!-- b000814 | furniture | pages [8] -->
m

<!-- b000815 | furniture | pages [8] -->
m

<!-- b000816 | furniture | pages [8] -->
m

<!-- b000817 | furniture | pages [8] -->
m

<!-- b000818 | furniture | pages [8] -->
m

<!-- b000819 | furniture | pages [8] -->
m

<!-- b000820 | furniture | pages [8] -->
m

<!-- b000821 | furniture | pages [8] -->
m

<!-- b000822 | furniture | pages [8] -->
m

<!-- b000823 | furniture | pages [8] -->
m

<!-- b000824 | furniture | pages [8] -->
m

<!-- b000825 | furniture | pages [8] -->
m

<!-- b000826 | furniture | pages [8] -->
m

<!-- b000827 | furniture | pages [8] -->
m

<!-- b000828 | furniture | pages [8] -->
m

<!-- b000829 | furniture | pages [8] -->
m

<!-- b000830 | furniture | pages [8] -->
m

<!-- b000831 | furniture | pages [8] -->
m

<!-- b000832 | furniture | pages [8] -->
m

<!-- b000833 | furniture | pages [8] -->
m

<!-- b000834 | furniture | pages [8] -->
m

<!-- b000835 | furniture | pages [8] -->
m

<!-- b000836 | furniture | pages [9] -->
Team #2510185

<!-- b000837 | furniture | pages [9] -->
Page 9 of 24

<!-- b000839 | caption | pages [9] -->
Figure 5: Correlation matrix of the characteristics of model 1

<!-- b000840 | prose | pages [9] -->
As can be seen from the image, for N_G, N_S, N_B, and Total, the six selected features are all correlated to some extent. Therefore, we select all of the above features to train the model.

<!-- b000841 | prose | pages [9] -->
We evaluated multiple models to select the best for prediction. Linear regression is chosen for its simplicity and interpretability. Random forests are selected for their strong predictive power and interpretability. XGBoost, known for its excellent performance, is also used for prediction.

<!-- b000842 | prose | pages [9] -->
For both random forests and XGBoost, we use a grid search to determine the best hyperpa- rameters. A total of 27 combinations of three hyperparameters are set for random forests and 54 combinations for XGBoost. The optimal parameters are:

<!-- b000843 | caption | pages [9] -->
Table 4: Random Forests Hyperparameters

<!-- b000844 | prose | pages [9] -->
n_estimators max_depth min_samples_split

<!-- b000845 | prose | pages [9] -->
180 10 4

<!-- b000846 | caption | pages [9] -->
Table 5: XGBoost Hyperparameters

<!-- b000847 | prose | pages [9] -->
eta max_depth subsample colsample_bytree

<!-- b000848 | prose | pages [9] -->
0.1 6 0.8 0.8

<!-- b000849 | prose | pages [9] -->
The fitting results of the three models’ predictions for 70% of the training set and 30% of the test set are shown in Figure 6.

<!-- b000850 | furniture | pages [10] -->
Team #2510185

<!-- b000851 | furniture | pages [10] -->
Page 10 of 24

<!-- b000852 | prose | pages [10] -->
Actual vs Predicted Total (Linear Regression) 125 100 75 Total 50 25 Actual Predicted (Linear Regression) 25 30 35 10 15 20 0 5 Actual vs Predicted Total (XGBoost)

<!-- b000853 | prose | pages [10] -->
100 80 Total 60 40 20 Actual Predicted (XGBoost) 0 25 35 30 10 15 20 5 Actual vs Predicted Total (Random Forest) 120 100 80 Total 60 40 20 Actual Predicted (Random Forest) 25 10 30 35 15 20 0 Different NOC for each Olympic Games

<!-- b000854 | caption | pages [10] -->
Figure 6: Fitted prediction curves for Linear Regression, XGBoost, and Random Forests (from top

<!-- b000855 | prose | pages [10] -->
to bottom)

<!-- b000856 | prose | pages [10] -->
Additionally, we tested the stability of model predictions using 5-fold cross-validation.

<!-- b000857 | caption | pages [10] -->
Table 6: Performance Evaluation of Three Prediction Models

<!-- b000858 | heading | pages [10] -->
Model

<!-- b000859 | prose | pages [10] -->
R² RMSE 5-fold Cross-Validation R²

<!-- b000860 | prose | pages [10] -->
15.44 Linear Regression 0.8063 0.7066 XGBoost 0.8764 12.33 0.7597 12.19 0.7642 0.8792 Random Forest

<!-- b000861 | prose | pages [10] -->
The R² and RMSE results for Random Forest and XGBoost are similar, with R² exceeding

<!-- b000862 | heading | pages [10] -->
0.85. Given the better interpretability of random forest regarding feature importance, we select the

<!-- b000863 | prose | pages [10] -->
grid-searched Random Forest as the primary model.

<!-- b000864 | prose | pages [10] -->
In 5-fold cross-validation, both Random Forest and XGBoost achieve R² values above 0.75, demonstrating the robustness of these models. However, examining the R² results for each fold reveals occasional instances of poor predictive performance. We hypothesize that increasing the size of the training set improves this. Additionally, the size of the test and training sets may also influence the RMSE values.

<!-- b000865 | prose | pages [10, 11] -->
关注数学模型 微信公众号：数学模型

<!-- b000866 | furniture | pages [10] -->
获取更多资讯

<!-- b000867 | furniture | pages [11] -->
Team #2510185

<!-- b000868 | furniture | pages [11] -->
Page 11 of 24

<!-- b000870 | heading | pages [11] -->
3.3 Task 1.1: 2028 Olympic VMT Prediction

<!-- b000871 | heading | pages [11] -->
3.3.1 Grid SearchCV - Random Forest Model

<!-- b000872 | prose | pages [11] -->
Combining the data from the medal tables of recent Olympic Games, we select the top-ranked countries to make predictions for. For the medal table predictions, we will only predict medals for the major award-winning countries mentioned above. Note that Russia did not participate in the Olympics. The flowchart for Task 1.1 is as follows:

<!-- b000873 | prose | pages [11] -->
 

<!-- b000874 | prose | pages [11] -->
Accuracy 微信号：MATHmodels Original Sample  Booststrap Sample ×300

<!-- b000875 | prose | pages [11] -->
NOC N_G L_G U_G Total

<!-- b000876 | prose | pages [11] -->
USA 50 137 43.47 55.22 …… Result 2 Result n Result 1 CHN 39 90 30.84 42.18 GBR 20 63 13.40 28.54 95% Confidence Best parameters JPN 17 43 11.28 23.06 n_estimators max_depth min_samples_split 2.5% 97.5% AUS 17 10.66 32.53 50 180 10 4 FRA 15 62 11.52 27.28 GER 14 43 8.52 21.43  NED 13 33 6.64 21.32 … … … … … DATASET

<!-- b000877 | prose | pages [11] -->
……

<!-- b000878 | prose | pages [11] -->
DECISION TREE 1 DECISION TREE 2 DECISION TREE N

<!-- b000879 | heading | pages [11] -->
RESULT 1

<!-- b000880 | heading | pages [11] -->
RESULT 2

<!-- b000881 | heading | pages [11] -->
RESULT N

<!-- b000882 | prose | pages [11] -->
VOTING

<!-- b000883 | heading | pages [11] -->
RESULT

<!-- b000884 | caption | pages [11] -->
Figure 7: Flowchart for Task 1.1

<!-- b000885 | heading | pages [11] -->
3.3.2 Prediction Results

<!-- b000886 | prose | pages [11] -->
The random forest model is used to predict the medal rankings of each country in the 2028 Los Angeles Summer Olympics. We assume that the number of participants (N_A) and the number of events (N_E) are increased in proportion to the additional events in 2028. The prediction results are shown in Table 7:

<!-- b000887 | prose | pages [11] -->
The medal rankings are based on the predicted counts of gold, silver, and bronze medals in descending order. Integer values are rounded using the "round half to even" method. Due to space constraints, only a selection of countries is displayed in the medal table, while many others are not shown. However, the same methodology is consistently applied to all countries in the rankings.

<!-- b000888 | prose | pages [11] -->
Analyzing the forecast results, we can conclude:

<!-- b000889 | prose | pages [11] -->
• Countries most likely to increase the number of medals: the United States.

<!-- b000890 | prose | pages [11] -->
• Countries most likely to decrease the number of medals: South Korea.

<!-- b000891 | furniture | pages [12] -->
Team #2510185

<!-- b000892 | furniture | pages [12] -->
Page 12 of 24

<!-- b000893 | caption | pages [12] -->
Table 7: Los Angeles Olympics (2028) Virtual Medal Table

<!-- b000894 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m △Total NOC m m Gold m m m m m m m m m m m Silver m m m Bronze Total Total (2024) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m USA 50 47 40 137 127 +11 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m CHN 39 29 22 90 91 -1 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m GBR 20 20 23 63 65 -2 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000895 | prose | pages [12] -->
JPN 17 15 15 47 45 +2 AUS 17 15 17 50 53 -3 FRA 15 25 22 62 64 -2 GER 14 8 9 31 33 -2 NED 13 8 12 33 34 -1 ITA 11 12 16 39 40 -1 KOR 10 7 9 26 32 -6 NZL 8 7 5 20 20 0 HUN 7 6 6 19 19 0 CAN 7 7 10 24 27 -3 ESP 6 5 8 19 18 +1 BRA 5 6 8 19 20 -1

<!-- b000896 | prose | pages [12] -->
3.3.3 95% Confidence Intervals by Bootstrap

<!-- b000897 | prose | pages [12] -->
For the Random Forest model, the 95% confidence intervals are estimated using the bootstrap method. The process includes the following steps:

<!-- b000898 | prose | pages [12] -->
1. Resample the training data 300 times and train a model for each resample.

<!-- b000899 | prose | pages [12] -->
2. Use the models trained on the resampled data to make predictions.

<!-- b000900 | prose | pages [12] -->
3. Determine the confidence intervals by calculating the 2.5th and 97.5th percentiles of the predictions.

<!-- b000901 | prose | pages [12] -->
The predicted intervals are presented in Table 8:

<!-- b000902 | prose | pages [12] -->
Our prediction intervals for Gold, Silver, Bronze, and Total are predicted separately, so the Total prediction interval is not determined by the intervals for the three medal categories.

<!-- b000903 | heading | pages [12] -->
3.4 Task 1.2: The Probability of First Medal

<!-- b000904 | prose | pages [12] -->
After observing and organizing the dataset, we find that there are currently 77 countries or regions that have participated in the Olympics but have never won a medal. Among them, there are many countries that have participated multiple times.

<!-- b000905 | prose | pages [12] -->
We also identify countries that have won medals for the first time in recent years, including Albania, Cabo Verde, Dominica, and Saint Lucia in 2024. Using historical data, we explore the commonalities of countries that have won medals for the first time. The following predictions are based on Hypothesis 3, which only considers the performance of athletes and not the political and economic situation of external countries.

<!-- b000906 | prose | pages [12, 13] -->
关注数学模型 U_Sil NOC L_Bro L_Gold U_Gold L_Sil U_Bro L_Total U_Total 43.4673 34.5945 USA 55.2163 36.1520 42.3355 48.5010 120.2138 146.0528 30.8390 22.9743 16.6925 CHN 42.1753 34.2540 26.8335 81.5058 103.2628 GBR 24.3835 13.3978 28.5428 16.1528 27.2090 12.6220 52.1725 76.1353 JPN 11.2848 23.0640 10.7348 18.5230 12.1013 19.8430 34.1208 56.4300 AUS 41.2213 10.6555 32.5253 10.5470 22.6360 10.0188 31.1533 76.3145 49.4793 11.5233 27.2760 18.3410 29.6038 19.6150 30.0225 86.9023 FRA 50.7058 GER 19.4945 8.5160 21.4323 3.3070 17.7790 7.1198 22.9428 15.992517.2473 6.6443 21.3190 4.0565 13.9610 6.5465 51.2725 NED ITA 10.4003 8.1100 15.2173 14.1658 48.8730 13.5638 19.4900 32.0740 14.7665 34.6253 4.2660 13.1340 4.6835 10.3085 5.8170 KOR 11.1828 29.1528 NZL 11.3150 5.4268 4.2243 9.9683 3.38287.8695 13.0338 3.9523 22.8100 HUN 4.1548 7.1308 4.8633 8.1225 7.5568 14.9703 12.6878 10.6268 5.9835 5.0590 8.8628 13.2300 19.9053 36.5445 CAN ESP 2.7575 10.2725 2.2690 8.8830 11.2775 30.4330 3.0180 10.0445 3.8375 4.5943 6.1783 11.9415 14.6100 29.4308 BRA 8.6273 8.8620

<!-- b000907 | furniture | pages [12] -->
2

<!-- b000908 | furniture | pages [12] -->
MATHmodels

<!-- b000909 | furniture | pages [12] -->
获取更多资讯

<!-- b000910 | furniture | pages [13] -->
Page 13 of 24

<!-- b000911 | furniture | pages [13] -->
Team #2510185

<!-- b000912 | caption | pages [13] -->
Table 8: 95% Confidence Intervals for Medal Predictions Using Random Forest

<!-- b000914 | prose | pages [13] -->
3.4.1 BP Neural Network Classifier

<!-- b000915 | prose | pages [13] -->
Unlike medal ranking predictions, this analysis cannot directly use previous models for train- ing and prediction. This is because for countries that have never won a medal, the dependent variable, Total, is always 0 during training, leading to significant errors and making reliable results unattainable.

<!-- b000916 | prose | pages [13] -->
1 微 Receiver Operating Characteristic (ROC) Curve 1.0

<!-- b000917 | prose | pages [13] -->
0.8

<!-- b000918 | prose | pages [13] -->
True Positive Rate 0.6

<!-- b000919 | prose | pages [13] -->
0.4

<!-- b000920 | prose | pages [13] -->
0.2

<!-- b000921 | prose | pages [13] -->
ROC curve (area = 0.94) 0.0 0.0 0.2 0.4 0.6 0.8 1.0 False Positive Rate

<!-- b000922 | caption | pages [13] -->
Figure 8: ROC Curve of BP Neural Network Classifier

<!-- b000923 | prose | pages [13, 14] -->
We use countries that have won their first Olympic medals in recent years as the training set m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and countries that have never won a medal as the test set. A classifier is used to map the likelihood m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m of a country winning a medal (PWM = 0 or > 0) to a value between 0 and 1. After comparing SVM m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and Random Forest classifiers, we selected the BP neural network classifier, which has an ROC m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m curve with an area of 0.94, as shown in Figure 8, indicating strong classification performance. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m A BP neural network classifier is used to predict the 2028 Los Angeles Olympics for countries m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000924 | furniture | pages [14] -->
Team #2510185

<!-- b000925 | furniture | pages [14] -->
Page 14 of 24

<!-- b000927 | prose | pages [14] -->
that did not win medals, and the resulting probabilities are shown in Table 9:

<!-- b000928 | caption | pages [14] -->
Table 9: Probability of Win first Medal in 2028 (Partial)

<!-- b000929 | prose | pages [14] -->
NOC N_A Prediction Probability

<!-- b000930 | prose | pages [14] -->
GUM 8 0.153210476 ESA 9 0.144216761 LBR 10 0.1420369 PLE 8 0.140068978 RWA 8 0.130942091 GAM 8 0.130942091 COD 6 0.12339206

<!-- b000931 | prose | pages [14] -->
As can be seen from the table, countries with a long history of participation and a large number of participants are more likely to win medals. The overall probability of winning is relatively low, and it cannot be ruled out that none of these countries will win a medal. Countries or regions with a relatively high probability of winning medals at the 2028 Olympics are: GUM, ESA, LBR, and PLE.

<!-- b000932 | heading | pages [14] -->
3.5 Task 1.3: The Impact of Events on Medals

<!-- b000933 | prose | pages [14] -->
In Task 1.1, we used only the number of projects and the number of participants to predict the number of medals. The correlation between the number of projects and the number of medals is 0.52. Below we examine the relationship between the number of events, the number of athletes, and the number of medals won in some countries.

<!-- b000934 | prose | pages [14] -->
By examining the table, we focus on exploring the relationship between medals and events for six countries: China, the United States, Great Britain, Germany, Japan, and France. We organize data on the number of participants in each event and the number of medalists across all Olympic Games in history for each country. Using random forests, we predict the total number of medals won, thereby determining the importance of each event in contributing to the medal count.

<!-- b000935 | prose | pages [14] -->
n X PWMA = (N_Gi + N_Si + N_Bi) (3) i=1 where n is the total number of events and i is the i-th event in an Olympic Games.

<!-- b000936 | caption | pages [14] -->
Figure 9 shows the solution framework for this subtask.

<!-- b000937 | prose | pages [14, 15] -->
关注数学模型 Olympic events Random Forest Number of medal (number and type) winning athletes

<!-- b000938 | furniture | pages [14] -->
2

<!-- b000939 | furniture | pages [14] -->
MATHmodels

<!-- b000940 | furniture | pages [14] -->
获取更多资讯

<!-- b000941 | furniture | pages [15] -->
Team #2510185

<!-- b000942 | furniture | pages [15] -->
Page 15 of 24

<!-- b000944 | prose | pages [15] -->
E1 N1

<!-- b000945 | prose | pages [15] -->
Feature lmportance E2 N2

<!-- b000946 | prose | pages [15] -->
Various Total Olympic 微信公众号：数学模型 E3 N3 Games

<!-- b000947 | prose | pages [15] -->
Nn E4

<!-- b000948 | caption | pages [15] -->
Figure 9: Flowchart for Task 1.3

<!-- b000949 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000950 | heading | pages [15] -->
3.5.1 Event Importance Based on Random Forests

<!-- b000951 | prose | pages [15] -->
We use random forests to predict the total number of medals based on the number of partici- pants and medalists in each event. The data consists of the number of participants and medalists for each event across multiple Olympic Games for a given country. Random forests are then used to generate feature importance. For example, in predicting the medal count for Germany, the R² value reaches 0.91, and the feature distribution is shown in Figure 10.

<!-- b000952 | caption | pages [15] -->
Figure 10: The event importance distribution of Germany

<!-- b000953 | prose | pages [15, 16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Using the same method, the results of the feature importance of the six countries are shown in

<!-- b000954 | furniture | pages [15] -->
m

<!-- b000955 | furniture | pages [15] -->
m

<!-- b000956 | furniture | pages [15] -->
m

<!-- b000957 | furniture | pages [15] -->
m

<!-- b000958 | furniture | pages [15] -->
m

<!-- b000959 | furniture | pages [15] -->
m

<!-- b000960 | furniture | pages [15] -->
m

<!-- b000961 | furniture | pages [15] -->
m

<!-- b000962 | furniture | pages [15] -->
m

<!-- b000963 | furniture | pages [15] -->
m

<!-- b000964 | furniture | pages [15] -->
m

<!-- b000965 | furniture | pages [15] -->
m

<!-- b000966 | furniture | pages [15] -->
m

<!-- b000967 | furniture | pages [15] -->
m

<!-- b000968 | furniture | pages [15] -->
m

<!-- b000969 | furniture | pages [15] -->
m

<!-- b000970 | furniture | pages [15] -->
m

<!-- b000971 | furniture | pages [15] -->
m

<!-- b000972 | furniture | pages [15] -->
m

<!-- b000973 | furniture | pages [15] -->
m

<!-- b000974 | furniture | pages [15] -->
m

<!-- b000975 | furniture | pages [15] -->
m

<!-- b000976 | furniture | pages [15] -->
m

<!-- b000977 | furniture | pages [15] -->
m

<!-- b000978 | furniture | pages [15] -->
m

<!-- b000979 | furniture | pages [15] -->
m

<!-- b000980 | furniture | pages [15] -->
m

<!-- b000981 | furniture | pages [15] -->
m

<!-- b000982 | furniture | pages [15] -->
m

<!-- b000983 | furniture | pages [15] -->
m

<!-- b000984 | furniture | pages [15] -->
m

<!-- b000985 | furniture | pages [15] -->
m

<!-- b000986 | furniture | pages [15] -->
m

<!-- b000987 | furniture | pages [15] -->
m

<!-- b000988 | furniture | pages [15] -->
m

<!-- b000989 | furniture | pages [15] -->
m

<!-- b000990 | furniture | pages [15] -->
m

<!-- b000991 | furniture | pages [15] -->
m

<!-- b000992 | furniture | pages [15] -->
m

<!-- b000993 | furniture | pages [15] -->
m

<!-- b000994 | furniture | pages [15] -->
m

<!-- b000995 | furniture | pages [15] -->
m

<!-- b000996 | furniture | pages [15] -->
m

<!-- b000997 | furniture | pages [15] -->
m

<!-- b000998 | furniture | pages [15] -->
m

<!-- b000999 | furniture | pages [15] -->
m

<!-- b001000 | furniture | pages [15] -->
m

<!-- b001001 | furniture | pages [15] -->
m

<!-- b001002 | furniture | pages [15] -->
m

<!-- b001003 | furniture | pages [15] -->
m

<!-- b001004 | furniture | pages [15] -->
m

<!-- b001005 | furniture | pages [15] -->
m

<!-- b001006 | furniture | pages [15] -->
m

<!-- b001007 | furniture | pages [15] -->
m

<!-- b001008 | furniture | pages [15] -->
m

<!-- b001009 | furniture | pages [15] -->
m

<!-- b001010 | furniture | pages [15] -->
m

<!-- b001011 | furniture | pages [15] -->
m

<!-- b001012 | furniture | pages [15] -->
m

<!-- b001013 | furniture | pages [15] -->
m

<!-- b001014 | furniture | pages [15] -->
m

<!-- b001015 | furniture | pages [15] -->
m

<!-- b001016 | furniture | pages [15] -->
m

<!-- b001017 | furniture | pages [15] -->
m

<!-- b001018 | furniture | pages [15] -->
m

<!-- b001019 | furniture | pages [15] -->
m

<!-- b001020 | furniture | pages [15] -->
m

<!-- b001021 | furniture | pages [15] -->
m

<!-- b001022 | furniture | pages [15] -->
m

<!-- b001023 | furniture | pages [15] -->
m

<!-- b001024 | furniture | pages [15] -->
m

<!-- b001025 | furniture | pages [15] -->
m

<!-- b001026 | furniture | pages [15] -->
m

<!-- b001027 | furniture | pages [15] -->
m

<!-- b001028 | furniture | pages [15] -->
m

<!-- b001029 | furniture | pages [15] -->
m

<!-- b001030 | furniture | pages [15] -->
m

<!-- b001031 | furniture | pages [15] -->
m

<!-- b001032 | furniture | pages [15] -->
m

<!-- b001033 | furniture | pages [15] -->
m

<!-- b001034 | furniture | pages [15] -->
m

<!-- b001035 | furniture | pages [15] -->
m

<!-- b001036 | furniture | pages [15] -->
m

<!-- b001037 | furniture | pages [15] -->
m

<!-- b001038 | furniture | pages [15] -->
m

<!-- b001039 | furniture | pages [15] -->
m

<!-- b001040 | furniture | pages [15] -->
m

<!-- b001041 | furniture | pages [15] -->
m

<!-- b001042 | furniture | pages [15] -->
m

<!-- b001043 | furniture | pages [15] -->
m

<!-- b001044 | furniture | pages [15] -->
m

<!-- b001045 | furniture | pages [15] -->
m

<!-- b001046 | furniture | pages [15] -->
m

<!-- b001047 | furniture | pages [15] -->
m

<!-- b001048 | furniture | pages [15] -->
m

<!-- b001049 | furniture | pages [15] -->
m

<!-- b001050 | furniture | pages [15] -->
m

<!-- b001051 | furniture | pages [15] -->
m

<!-- b001052 | furniture | pages [15] -->
m

<!-- b001053 | furniture | pages [15] -->
m

<!-- b001054 | furniture | pages [15] -->
m

<!-- b001055 | furniture | pages [15] -->
m

<!-- b001056 | furniture | pages [15] -->
m

<!-- b001057 | furniture | pages [15] -->
m

<!-- b001058 | furniture | pages [15] -->
m

<!-- b001059 | furniture | pages [15] -->
m

<!-- b001060 | furniture | pages [15] -->
m

<!-- b001061 | furniture | pages [15] -->
m

<!-- b001062 | furniture | pages [15] -->
m

<!-- b001063 | furniture | pages [15] -->
m

<!-- b001064 | furniture | pages [15] -->
m

<!-- b001065 | furniture | pages [15] -->
m

<!-- b001066 | furniture | pages [15] -->
m

<!-- b001067 | furniture | pages [15] -->
m

<!-- b001068 | furniture | pages [15] -->
m

<!-- b001069 | furniture | pages [15] -->
m

<!-- b001070 | furniture | pages [15] -->
m

<!-- b001071 | furniture | pages [15] -->
m

<!-- b001072 | furniture | pages [15] -->
m

<!-- b001073 | furniture | pages [15] -->
m

<!-- b001074 | furniture | pages [15] -->
m

<!-- b001075 | furniture | pages [15] -->
m

<!-- b001076 | furniture | pages [15] -->
m

<!-- b001077 | furniture | pages [15] -->
m

<!-- b001078 | furniture | pages [15] -->
m

<!-- b001079 | furniture | pages [15] -->
m

<!-- b001080 | furniture | pages [15] -->
m

<!-- b001081 | furniture | pages [15] -->
m

<!-- b001082 | furniture | pages [15] -->
m

<!-- b001083 | furniture | pages [15] -->
m

<!-- b001084 | furniture | pages [15] -->
m

<!-- b001085 | furniture | pages [15] -->
m

<!-- b001086 | furniture | pages [15] -->
m

<!-- b001087 | furniture | pages [15] -->
m

<!-- b001088 | furniture | pages [15] -->
m

<!-- b001089 | furniture | pages [15] -->
m

<!-- b001090 | furniture | pages [15] -->
m

<!-- b001091 | furniture | pages [15] -->
m

<!-- b001092 | furniture | pages [15] -->
m

<!-- b001093 | furniture | pages [15] -->
m

<!-- b001094 | furniture | pages [15] -->
m

<!-- b001095 | furniture | pages [15] -->
m

<!-- b001096 | furniture | pages [15] -->
m

<!-- b001097 | furniture | pages [15] -->
m

<!-- b001098 | furniture | pages [15] -->
m

<!-- b001099 | furniture | pages [15] -->
m

<!-- b001100 | furniture | pages [15] -->
m

<!-- b001101 | furniture | pages [15] -->
m

<!-- b001102 | furniture | pages [15] -->
m

<!-- b001103 | furniture | pages [15] -->
m

<!-- b001104 | furniture | pages [15] -->
m

<!-- b001105 | furniture | pages [15] -->
m

<!-- b001106 | furniture | pages [15] -->
m

<!-- b001107 | furniture | pages [15] -->
m

<!-- b001108 | furniture | pages [15] -->
m

<!-- b001109 | furniture | pages [15] -->
m

<!-- b001110 | furniture | pages [15] -->
m

<!-- b001111 | furniture | pages [15] -->
m

<!-- b001112 | furniture | pages [15] -->
m

<!-- b001113 | furniture | pages [15] -->
m

<!-- b001114 | furniture | pages [15] -->
m

<!-- b001115 | furniture | pages [15] -->
m

<!-- b001116 | furniture | pages [15] -->
m

<!-- b001117 | furniture | pages [15] -->
m

<!-- b001118 | furniture | pages [15] -->
m

<!-- b001119 | furniture | pages [15] -->
m

<!-- b001120 | furniture | pages [15] -->
m

<!-- b001121 | furniture | pages [15] -->
m

<!-- b001122 | furniture | pages [15] -->
m

<!-- b001123 | furniture | pages [15] -->
m

<!-- b001124 | furniture | pages [15] -->
m

<!-- b001125 | furniture | pages [15] -->
m

<!-- b001126 | furniture | pages [15] -->
m

<!-- b001127 | furniture | pages [15] -->
m

<!-- b001128 | furniture | pages [15] -->
m

<!-- b001129 | furniture | pages [15] -->
m

<!-- b001130 | furniture | pages [15] -->
m

<!-- b001131 | furniture | pages [15] -->
m

<!-- b001132 | furniture | pages [15] -->
m

<!-- b001133 | furniture | pages [15] -->
m

<!-- b001134 | furniture | pages [15] -->
m

<!-- b001135 | furniture | pages [15] -->
m

<!-- b001136 | furniture | pages [15] -->
m

<!-- b001137 | furniture | pages [15] -->
m

<!-- b001138 | furniture | pages [15] -->
m

<!-- b001139 | furniture | pages [15] -->
m

<!-- b001140 | furniture | pages [15] -->
m

<!-- b001141 | furniture | pages [15] -->
m

<!-- b001142 | furniture | pages [15] -->
m

<!-- b001143 | furniture | pages [15] -->
m

<!-- b001144 | furniture | pages [15] -->
m

<!-- b001145 | furniture | pages [15] -->
m

<!-- b001146 | furniture | pages [15] -->
m

<!-- b001147 | furniture | pages [15] -->
m

<!-- b001148 | furniture | pages [15] -->
m

<!-- b001149 | furniture | pages [15] -->
m

<!-- b001150 | furniture | pages [15] -->
m

<!-- b001151 | furniture | pages [15] -->
m

<!-- b001152 | furniture | pages [15] -->
m

<!-- b001153 | furniture | pages [15] -->
m

<!-- b001154 | furniture | pages [15] -->
m

<!-- b001155 | furniture | pages [15] -->
m

<!-- b001156 | furniture | pages [15] -->
m

<!-- b001157 | furniture | pages [15] -->
m

<!-- b001158 | furniture | pages [15] -->
m

<!-- b001159 | furniture | pages [15] -->
m

<!-- b001160 | furniture | pages [15] -->
m

<!-- b001161 | furniture | pages [15] -->
m

<!-- b001162 | furniture | pages [15] -->
m

<!-- b001163 | furniture | pages [15] -->
m

<!-- b001164 | furniture | pages [15] -->
m

<!-- b001165 | furniture | pages [15] -->
m

<!-- b001166 | furniture | pages [15] -->
m

<!-- b001167 | furniture | pages [15] -->
m

<!-- b001168 | furniture | pages [15] -->
m

<!-- b001169 | furniture | pages [15] -->
m

<!-- b001170 | furniture | pages [15] -->
m

<!-- b001171 | furniture | pages [15] -->
m

<!-- b001172 | furniture | pages [15] -->
m

<!-- b001173 | furniture | pages [15] -->
m

<!-- b001174 | furniture | pages [15] -->
m

<!-- b001175 | furniture | pages [15] -->
m

<!-- b001176 | furniture | pages [15] -->
m

<!-- b001177 | furniture | pages [15] -->
m

<!-- b001178 | furniture | pages [15] -->
m

<!-- b001179 | furniture | pages [15] -->
m

<!-- b001180 | furniture | pages [15] -->
m

<!-- b001181 | furniture | pages [15] -->
m

<!-- b001182 | furniture | pages [15] -->
m

<!-- b001183 | furniture | pages [15] -->
m

<!-- b001184 | furniture | pages [15] -->
m

<!-- b001185 | furniture | pages [15] -->
m

<!-- b001186 | furniture | pages [15] -->
m

<!-- b001187 | furniture | pages [15] -->
m

<!-- b001188 | furniture | pages [15] -->
m

<!-- b001189 | furniture | pages [15] -->
m

<!-- b001190 | furniture | pages [15] -->
m

<!-- b001191 | furniture | pages [15] -->
m

<!-- b001192 | furniture | pages [15] -->
m

<!-- b001193 | furniture | pages [15] -->
m

<!-- b001194 | furniture | pages [15] -->
m

<!-- b001195 | furniture | pages [15] -->
m

<!-- b001196 | furniture | pages [15] -->
m

<!-- b001197 | furniture | pages [15] -->
m

<!-- b001198 | furniture | pages [15] -->
m

<!-- b001199 | furniture | pages [15] -->
m

<!-- b001200 | furniture | pages [15] -->
m

<!-- b001201 | furniture | pages [15] -->
m

<!-- b001202 | furniture | pages [15] -->
m

<!-- b001203 | furniture | pages [15] -->
m

<!-- b001204 | furniture | pages [15] -->
m

<!-- b001205 | furniture | pages [15] -->
m

<!-- b001206 | furniture | pages [15] -->
m

<!-- b001207 | furniture | pages [15] -->
m

<!-- b001208 | furniture | pages [15] -->
m

<!-- b001209 | furniture | pages [15] -->
m

<!-- b001210 | furniture | pages [15] -->
m

<!-- b001211 | furniture | pages [15] -->
m

<!-- b001212 | furniture | pages [15] -->
m

<!-- b001213 | furniture | pages [15] -->
m

<!-- b001214 | furniture | pages [15] -->
m

<!-- b001215 | furniture | pages [15] -->
m

<!-- b001216 | furniture | pages [15] -->
m

<!-- b001217 | furniture | pages [15] -->
m

<!-- b001218 | furniture | pages [15] -->
m

<!-- b001219 | furniture | pages [15] -->
m

<!-- b001220 | furniture | pages [15] -->
m

<!-- b001221 | furniture | pages [15] -->
m

<!-- b001222 | furniture | pages [15] -->
m

<!-- b001223 | furniture | pages [15] -->
m

<!-- b001224 | furniture | pages [15] -->
m

<!-- b001225 | furniture | pages [15] -->
m

<!-- b001226 | furniture | pages [15] -->
m

<!-- b001227 | furniture | pages [15] -->
m

<!-- b001228 | furniture | pages [15] -->
m

<!-- b001229 | furniture | pages [15] -->
m

<!-- b001230 | furniture | pages [15] -->
m

<!-- b001231 | furniture | pages [15] -->
m

<!-- b001232 | furniture | pages [15] -->
m

<!-- b001233 | furniture | pages [15] -->
m

<!-- b001234 | furniture | pages [15] -->
m

<!-- b001235 | furniture | pages [15] -->
m

<!-- b001236 | furniture | pages [15] -->
m

<!-- b001237 | furniture | pages [15] -->
m

<!-- b001238 | furniture | pages [15] -->
m

<!-- b001239 | furniture | pages [15] -->
m

<!-- b001240 | furniture | pages [15] -->
m

<!-- b001241 | furniture | pages [15] -->
m

<!-- b001242 | furniture | pages [15] -->
m

<!-- b001243 | furniture | pages [15] -->
m

<!-- b001244 | furniture | pages [15] -->
m

<!-- b001245 | furniture | pages [15] -->
m

<!-- b001246 | furniture | pages [15] -->
m

<!-- b001247 | furniture | pages [15] -->
m

<!-- b001248 | furniture | pages [15] -->
m

<!-- b001249 | furniture | pages [15] -->
m

<!-- b001250 | furniture | pages [15] -->
m

<!-- b001251 | furniture | pages [15] -->
m

<!-- b001252 | furniture | pages [15] -->
m

<!-- b001253 | furniture | pages [15] -->
m

<!-- b001254 | furniture | pages [15] -->
m

<!-- b001255 | furniture | pages [15] -->
m

<!-- b001256 | furniture | pages [15] -->
m

<!-- b001257 | furniture | pages [15] -->
m

<!-- b001258 | furniture | pages [15] -->
m

<!-- b001259 | furniture | pages [15] -->
m

<!-- b001260 | furniture | pages [15] -->
m

<!-- b001261 | furniture | pages [15] -->
m

<!-- b001262 | furniture | pages [15] -->
m

<!-- b001263 | furniture | pages [15] -->
m

<!-- b001264 | furniture | pages [15] -->
m

<!-- b001265 | furniture | pages [15] -->
m

<!-- b001266 | furniture | pages [15] -->
m

<!-- b001267 | furniture | pages [15] -->
m

<!-- b001268 | furniture | pages [15] -->
m

<!-- b001269 | furniture | pages [15] -->
m

<!-- b001270 | furniture | pages [15] -->
m

<!-- b001271 | furniture | pages [15] -->
m

<!-- b001272 | furniture | pages [15] -->
m

<!-- b001273 | furniture | pages [15] -->
m

<!-- b001274 | furniture | pages [15] -->
m

<!-- b001275 | furniture | pages [15] -->
m

<!-- b001276 | furniture | pages [15] -->
m

<!-- b001277 | furniture | pages [15] -->
m

<!-- b001278 | furniture | pages [16] -->
Page 16 of 24

<!-- b001279 | furniture | pages [16] -->
Team #2510185

<!-- b001281 | caption | pages [16] -->
Figure 11.

<!-- b001282 | prose | pages [16] -->
Feature Importance Across Countries

<!-- b001283 | prose | pages [16] -->
Football Equestrianism Boxing Gymnastics Hockey Sailing Synchronized Swimming Weightlifting Fencing Cycling Countries Athletics JPN Event types FRA Water Polo GBR Rowing GER CHN Volleyball USA Badminton Handball Diving Basketball Table Tennis Wrestling Canoeing opnf Shooting Swimming -0.2 0.0 0.2 0.8 1.0 0.4 0.6 Feature Importance

<!-- b001284 | caption | pages [16] -->
Figure 11: Importance of Sports Events by Medal Count for Different Countries

<!-- b001285 | prose | pages [16] -->
Some countries have too few participants in certain sports and no medals; therefore, these were not included in the training and are assumed to have a feature importance of 0. The feature importance distribution mainly focuses on sports with a good medal expectation. It is important to note that we treat the number of participants and medalists in a sport as the essence of that sport. Therefore, our predictions include the number of events as a type. However, our predictions may amplify the impact of team events.

<!-- b001286 | prose | pages [16] -->
Analyzing the chart, the key sports for medal count in six countries are:

<!-- b001287 | prose | pages [16] -->
• Japan: Wrestling, Judo, and Table Tennis.

<!-- b001288 | prose | pages [16] -->
• France: Judo, Handball, and Swimming.

<!-- b001289 | prose | pages [16, 17] -->
关注数学模型 • Great Britain: Rowing, Diving, and Swimming. 微信公众号：数学模型

<!-- b001290 | furniture | pages [16] -->
获取更多资讯

<!-- b001291 | furniture | pages [17] -->
Team #2510185

<!-- b001292 | furniture | pages [17] -->
Page 17 of 24

<!-- b001294 | prose | pages [17] -->
• Germany: Canoeing and Shooting.

<!-- b001295 | prose | pages [17] -->
• China: Badminton, Diving, Swimming, and Shooting.

<!-- b001296 | prose | pages [17] -->
• United States: Swimming, Basketball, Volleyball, and Athletics.

<!-- b001297 | prose | pages [17] -->
The model explains that these countries have more participants in key sports and are more likely to win medals in these areas. The identified important sports align closely with the coun- tries’ traditional strengths, which significantly influence their medal counts. This indicates that our model results are highly accurate. 微信号：MATHmodels

<!-- b001298 | heading | pages [17] -->
3.5.2 The Impact of Home Country Events

<!-- b001299 | prose | pages [17] -->
The host country often adds new Olympic events. These events are related to the country in some way and are basically sports that the people of the country love. The newly added events of the host country can have a certain impact on the number of medals.

<!-- b001300 | prose | pages [17] -->
Examples include the 1996 Olympic Games in the United States, the 2020 Olympic Games in Japan, and the 2024 Olympic Games in France. We pay attention to whether the host country has certain advantages in the newly added events. According to the data provided, the main events added to these three Olympic Games were:

<!-- b001301 | prose | pages [17] -->
• 1996 Atlanta Olympics: Beach Volleyball, Mountain Biking, Softball, Lightweight Rowing, etc.

<!-- b001302 | prose | pages [17] -->
• 2020 Tokyo Olympics: Baseball, Softball, Rock Climbing, Karate, Surfing, and Skateboard- ing.

<!-- b001303 | prose | pages [17] -->
• 2024 Paris Olympics: Breakdancing, Skateboarding, Rock Climbing, and Surfing.

<!-- b001304 | prose | pages [17] -->
Here are the medal results for the three specific events:

<!-- b001305 | caption | pages [17] -->
Table 10: Medal Counts for New Events at the 1996 Atlanta Olympics

<!-- b001306 | prose | pages [17] -->
NOC N_G N_S N_B Total P_G P_T

<!-- b001307 | prose | pages [17, 18] -->
USA 41 5 18 64 33.33% 17.63% RUS 42 2 13 57 34.15% 15.70% CHN 4 45 5 54 3.25% 14.88% AUS 0 0 26 26 0 7.16% BLR 0 12 6 18 0 4.96% BUL 0 6 11 17 0 4.68% NOC N_G N_S N_B Total P_G P_T

<!-- b001308 | furniture | pages [18] -->
Team #2510185

<!-- b001309 | furniture | pages [18] -->
Page 18 of 24

<!-- b001310 | caption | pages [18] -->
Table 11: Medal Counts for New Events at the 2020 Tokyo Olympics

<!-- b001312 | prose | pages [18] -->
JPN 43 4 4 51 78.18% 29.48% USA 1 40 3 44 1.82% 25.43% DOM 0 0 24 24 0 13.87% CAN 0 0 15 15 0 8.67% BRA 1 3 0 4 1.82% 2.31% TUR 0 1 3 4 0 2.31%

<!-- b001313 | caption | pages [18] -->
Table 12: Medal Counts for New Events at the 2024 Paris Olympics

<!-- b001314 | prose | pages [18] -->
NOC N_G N_S N_B Total P_G P_T

<!-- b001315 | prose | pages [18] -->
USA 1 3 3 7 8.33% 19.44% JPN 3 3 0 6 25% 16.67% BRA 0 1 3 4 0 11.11% AUS 2 1 0 3 16.66% 8.33% FRA 1 1 1 3 8.33% 8.33% CHN 0 2 1 3 0 8.33%

<!-- b001316 | prose | pages [18] -->
where,

<!-- b001317 | prose | pages [18] -->
• P_G is the proportion of the number of people who won gold medals.

<!-- b001318 | prose | pages [18] -->
• N_G is the number of people who won gold medals. When medals are won as a team, we treat it as if each person won a medal individually.

<!-- b001319 | prose | pages [18] -->
As can be seen in the analysis table, the United States and Japan were the top medal winners in the new events in 1996 and 2020, respectively. France also did well in the new events in 2024. After reviewing the relevant information[6][7], we believe that selecting events from the home country that are either advantageous or popular in the country can greatly improve the results of the competition. For example, the new events of karate and skateboarding in Japan, and the new event of softball in the United States. These sports were originally popular in that country.

<!-- b001320 | heading | pages [18] -->
4 Task 2: “Great Coach” Contribution to Medals

<!-- b001321 | heading | pages [18] -->
4.1 Existence of “Great Coach” Effect

<!-- b001322 | prose | pages [18] -->
We first looked up Lang Ping’s coaching trajectory and considered her role as the head coach of the Chinese women’s volleyball team at the 2016 Rio Olympics[8]. We examined the results achieved by the women’s volleyball team at the Games during her tenure as coach. The results are shown in Table 13:

<!-- b001323 | prose | pages [18] -->
The Chinese women’s volleyball team secured the gold medal in women’s volleyball at the 2016 Olympics. However, in the eight years before and after this victory, their best Olympic result

<!-- b001324 | prose | pages [18, 19] -->
关注数学模型 Team Year Event Participants Great Coach Gold Silver Bronze Total 微信公众号：数学模型 China 2024 13 0 0 0 0 2.41 China 2020 12 0 0 0 0 3.85 China 2016 12 1 1 0 0 1.41 China 2012 12 0 0 0 0 3.10 China 2008 12 0 0 0 1 2.41

<!-- b001325 | furniture | pages [18] -->
2

<!-- b001326 | furniture | pages [18] -->
MATHmodels

<!-- b001327 | furniture | pages [18] -->
获取更多资讯

<!-- b001328 | furniture | pages [19] -->
Team #2510185

<!-- b001329 | furniture | pages [19] -->
Page 19 of 24

<!-- b001330 | caption | pages [19] -->
Table 13: Performance of the Chinese Women’s Volleyball Team in the Last Five Olympic Games

<!-- b001332 | prose | pages [19] -->
was a single bronze medal. This leads us to conclude that the "Great Coach" effect does indeed play a role.

<!-- b001333 | heading | pages [19] -->
4.2 Contribution of "Great Coach"

<!-- b001334 | prose | pages [19] -->
微信号：MATHmodels We expanded our analysis by researching legendary Olympic coaches and introduced a binary feature, "Great Coach" (0 or 1), into the dataset. Additional features included "Year" and "AAPI." The dataset covered events such as U.S. women’s volleyball, women’s gymnastics, and men’s sprinting; Chinese women’s volleyball and men’s swimming; German men’s canoeing; Russian women’s gymnastics; British men’s hurdles; and Jamaican women’s sprinting.

<!-- b001335 | prose | pages [19] -->
Using a random forest model to predict the "Total" medal count, the feature importance of "Great Coach" was 0.288. A BP neural network classifier was also applied to estimate the proba- bility of winning a gold medal.

<!-- b001336 | prose | pages [19] -->
For Jamaican women’s sprinting in 2024, the inclusion of the "Great Coach" feature increased the predicted medal count from 0.56 to 1.56.

<!-- b001337 | prose | pages [19] -->
• At an AAPI of approximately 65, the predicted increase was 0.9 bronze medals, 0.2 silver medals, 0.02 gold medals, and 1.2 total medals.

<!-- b001338 | prose | pages [19] -->
• At an AAPI of around 70, the predicted increase was 0.7 bronze medals, 0.9 silver medals, 0.2 gold medals, and 1.8 total medals.

<!-- b001339 | prose | pages [19] -->
These results highlight the significant impact of the "Great Coach" effect, contributing 28.8% to overall performance.

<!-- b001340 | heading | pages [19] -->
4.3 Event Investment and Impact

<!-- b001341 | heading | pages [19] -->
4.3.1 Event Potential Index (EPI)

<!-- b001342 | prose | pages [19] -->
We propose that sports with a history of multiple medals, athletes with higher AAPI, and events showing an upward trend are more likely to benefit from the introduction of a great coach. To estimate the improvement potential of an event after introducing a great coach, we define the Event Potential Index (EPI) using the following formula:

<!-- b001343 | prose | pages [19] -->
EPI = ω1 × Total_trend + ω2 × Total_space + ω3 × AAPI (4)

<!-- b001344 | prose | pages [19, 20] -->
• Total_trend represents the trend in medal count over time. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • Total_space reflects the growth potential in medal count.

<!-- b001345 | furniture | pages [19] -->
m

<!-- b001346 | furniture | pages [19] -->
m

<!-- b001347 | furniture | pages [19] -->
m

<!-- b001348 | furniture | pages [19] -->
m

<!-- b001349 | furniture | pages [19] -->
m

<!-- b001350 | furniture | pages [19] -->
m

<!-- b001351 | furniture | pages [19] -->
m

<!-- b001352 | furniture | pages [19] -->
m

<!-- b001353 | furniture | pages [19] -->
m

<!-- b001354 | furniture | pages [19] -->
m

<!-- b001355 | furniture | pages [19] -->
m

<!-- b001356 | furniture | pages [19] -->
m

<!-- b001357 | furniture | pages [19] -->
m

<!-- b001358 | furniture | pages [19] -->
m

<!-- b001359 | furniture | pages [19] -->
m

<!-- b001360 | furniture | pages [19] -->
m

<!-- b001361 | furniture | pages [19] -->
m

<!-- b001362 | furniture | pages [19] -->
m

<!-- b001363 | furniture | pages [19] -->
m

<!-- b001364 | furniture | pages [19] -->
m

<!-- b001365 | furniture | pages [19] -->
m

<!-- b001366 | furniture | pages [19] -->
m

<!-- b001367 | furniture | pages [19] -->
m

<!-- b001368 | furniture | pages [19] -->
m

<!-- b001369 | furniture | pages [19] -->
m

<!-- b001370 | furniture | pages [19] -->
m

<!-- b001371 | furniture | pages [19] -->
m

<!-- b001372 | furniture | pages [19] -->
m

<!-- b001373 | furniture | pages [19] -->
m

<!-- b001374 | furniture | pages [19] -->
m

<!-- b001375 | furniture | pages [19] -->
m

<!-- b001376 | furniture | pages [19] -->
m

<!-- b001377 | furniture | pages [19] -->
m

<!-- b001378 | furniture | pages [19] -->
m

<!-- b001379 | furniture | pages [19] -->
m

<!-- b001380 | furniture | pages [19] -->
m

<!-- b001381 | furniture | pages [19] -->
m

<!-- b001382 | furniture | pages [19] -->
m

<!-- b001383 | furniture | pages [19] -->
m

<!-- b001384 | furniture | pages [19] -->
m

<!-- b001385 | furniture | pages [19] -->
m

<!-- b001386 | furniture | pages [19] -->
m

<!-- b001387 | furniture | pages [19] -->
m

<!-- b001388 | furniture | pages [19] -->
m

<!-- b001389 | furniture | pages [19] -->
m

<!-- b001390 | furniture | pages [19] -->
m

<!-- b001391 | furniture | pages [19] -->
m

<!-- b001392 | furniture | pages [19] -->
m

<!-- b001393 | furniture | pages [19] -->
m

<!-- b001394 | furniture | pages [19] -->
m

<!-- b001395 | furniture | pages [19] -->
m

<!-- b001396 | furniture | pages [19] -->
m

<!-- b001397 | furniture | pages [19] -->
m

<!-- b001398 | furniture | pages [19] -->
m

<!-- b001399 | furniture | pages [19] -->
m

<!-- b001400 | furniture | pages [19] -->
m

<!-- b001401 | furniture | pages [19] -->
m

<!-- b001402 | furniture | pages [19] -->
m

<!-- b001403 | furniture | pages [19] -->
m

<!-- b001404 | furniture | pages [19] -->
m

<!-- b001405 | furniture | pages [19] -->
m

<!-- b001406 | furniture | pages [19] -->
m

<!-- b001407 | furniture | pages [19] -->
m

<!-- b001408 | furniture | pages [19] -->
m

<!-- b001409 | furniture | pages [19] -->
m

<!-- b001410 | furniture | pages [19] -->
m

<!-- b001411 | furniture | pages [19] -->
m

<!-- b001412 | furniture | pages [19] -->
m

<!-- b001413 | furniture | pages [19] -->
m

<!-- b001414 | furniture | pages [19] -->
m

<!-- b001415 | furniture | pages [19] -->
m

<!-- b001416 | furniture | pages [19] -->
m

<!-- b001417 | furniture | pages [19] -->
m

<!-- b001418 | furniture | pages [19] -->
m

<!-- b001419 | furniture | pages [19] -->
m

<!-- b001420 | furniture | pages [19] -->
m

<!-- b001421 | furniture | pages [19] -->
m

<!-- b001422 | furniture | pages [19] -->
m

<!-- b001423 | furniture | pages [19] -->
m

<!-- b001424 | furniture | pages [19] -->
m

<!-- b001425 | furniture | pages [19] -->
m

<!-- b001426 | furniture | pages [19] -->
m

<!-- b001427 | furniture | pages [19] -->
m

<!-- b001428 | furniture | pages [19] -->
m

<!-- b001429 | furniture | pages [19] -->
m

<!-- b001430 | furniture | pages [19] -->
m

<!-- b001431 | furniture | pages [19] -->
m

<!-- b001432 | furniture | pages [19] -->
m

<!-- b001433 | furniture | pages [19] -->
m

<!-- b001434 | furniture | pages [19] -->
m

<!-- b001435 | furniture | pages [19] -->
m

<!-- b001436 | furniture | pages [19] -->
m

<!-- b001437 | furniture | pages [19] -->
m

<!-- b001438 | furniture | pages [19] -->
m

<!-- b001439 | furniture | pages [19] -->
m

<!-- b001440 | furniture | pages [19] -->
m

<!-- b001441 | furniture | pages [19] -->
m

<!-- b001442 | furniture | pages [19] -->
m

<!-- b001443 | furniture | pages [19] -->
m

<!-- b001444 | furniture | pages [19] -->
m

<!-- b001445 | furniture | pages [19] -->
m

<!-- b001446 | furniture | pages [19] -->
m

<!-- b001447 | furniture | pages [19] -->
m

<!-- b001448 | furniture | pages [19] -->
m

<!-- b001449 | furniture | pages [19] -->
m

<!-- b001450 | furniture | pages [19] -->
m

<!-- b001451 | furniture | pages [19] -->
m

<!-- b001452 | furniture | pages [19] -->
m

<!-- b001453 | furniture | pages [19] -->
m

<!-- b001454 | furniture | pages [19] -->
m

<!-- b001455 | furniture | pages [19] -->
m

<!-- b001456 | furniture | pages [19] -->
m

<!-- b001457 | furniture | pages [19] -->
m

<!-- b001458 | furniture | pages [19] -->
m

<!-- b001459 | furniture | pages [19] -->
m

<!-- b001460 | furniture | pages [19] -->
m

<!-- b001461 | furniture | pages [19] -->
m

<!-- b001462 | furniture | pages [19] -->
m

<!-- b001463 | furniture | pages [19] -->
m

<!-- b001464 | furniture | pages [19] -->
m

<!-- b001465 | furniture | pages [19] -->
m

<!-- b001466 | furniture | pages [19] -->
m

<!-- b001467 | furniture | pages [19] -->
m

<!-- b001468 | furniture | pages [19] -->
m

<!-- b001469 | furniture | pages [19] -->
m

<!-- b001470 | furniture | pages [19] -->
m

<!-- b001471 | furniture | pages [19] -->
m

<!-- b001472 | furniture | pages [19] -->
m

<!-- b001473 | furniture | pages [19] -->
m

<!-- b001474 | furniture | pages [19] -->
m

<!-- b001475 | furniture | pages [19] -->
m

<!-- b001476 | furniture | pages [19] -->
m

<!-- b001477 | furniture | pages [19] -->
m

<!-- b001478 | furniture | pages [19] -->
m

<!-- b001479 | furniture | pages [19] -->
m

<!-- b001480 | furniture | pages [19] -->
m

<!-- b001481 | furniture | pages [19] -->
m

<!-- b001482 | furniture | pages [19] -->
m

<!-- b001483 | furniture | pages [19] -->
m

<!-- b001484 | furniture | pages [19] -->
m

<!-- b001485 | furniture | pages [19] -->
m

<!-- b001486 | furniture | pages [19] -->
m

<!-- b001487 | furniture | pages [19] -->
m

<!-- b001488 | furniture | pages [19] -->
m

<!-- b001489 | furniture | pages [19] -->
m

<!-- b001490 | furniture | pages [19] -->
m

<!-- b001491 | furniture | pages [19] -->
m

<!-- b001492 | furniture | pages [19] -->
m

<!-- b001493 | furniture | pages [19] -->
m

<!-- b001494 | furniture | pages [19] -->
m

<!-- b001495 | furniture | pages [19] -->
m

<!-- b001496 | furniture | pages [19] -->
m

<!-- b001497 | furniture | pages [19] -->
m

<!-- b001498 | furniture | pages [19] -->
m

<!-- b001499 | furniture | pages [19] -->
m

<!-- b001500 | furniture | pages [19] -->
m

<!-- b001501 | furniture | pages [19] -->
m

<!-- b001502 | furniture | pages [19] -->
m

<!-- b001503 | furniture | pages [19] -->
m

<!-- b001504 | furniture | pages [19] -->
m

<!-- b001505 | furniture | pages [19] -->
m

<!-- b001506 | furniture | pages [19] -->
m

<!-- b001507 | furniture | pages [19] -->
m

<!-- b001508 | furniture | pages [19] -->
m

<!-- b001509 | furniture | pages [19] -->
m

<!-- b001510 | furniture | pages [19] -->
m

<!-- b001511 | furniture | pages [19] -->
m

<!-- b001512 | furniture | pages [19] -->
m

<!-- b001513 | furniture | pages [19] -->
m

<!-- b001514 | furniture | pages [19] -->
m

<!-- b001515 | furniture | pages [19] -->
m

<!-- b001516 | furniture | pages [19] -->
m

<!-- b001517 | furniture | pages [19] -->
m

<!-- b001518 | furniture | pages [19] -->
m

<!-- b001519 | furniture | pages [19] -->
m

<!-- b001520 | furniture | pages [19] -->
m

<!-- b001521 | furniture | pages [19] -->
m

<!-- b001522 | furniture | pages [19] -->
m

<!-- b001523 | furniture | pages [19] -->
m

<!-- b001524 | furniture | pages [19] -->
m

<!-- b001525 | furniture | pages [19] -->
m

<!-- b001526 | furniture | pages [19] -->
m

<!-- b001527 | furniture | pages [19] -->
m

<!-- b001528 | furniture | pages [19] -->
m

<!-- b001529 | furniture | pages [19] -->
m

<!-- b001530 | furniture | pages [19] -->
m

<!-- b001531 | furniture | pages [19] -->
m

<!-- b001532 | furniture | pages [19] -->
m

<!-- b001533 | furniture | pages [19] -->
m

<!-- b001534 | furniture | pages [19] -->
m

<!-- b001535 | furniture | pages [19] -->
m

<!-- b001536 | furniture | pages [19] -->
m

<!-- b001537 | furniture | pages [19] -->
m

<!-- b001538 | furniture | pages [19] -->
m

<!-- b001539 | furniture | pages [19] -->
m

<!-- b001540 | furniture | pages [19] -->
m

<!-- b001541 | furniture | pages [19] -->
m

<!-- b001542 | furniture | pages [19] -->
m

<!-- b001543 | furniture | pages [19] -->
m

<!-- b001544 | furniture | pages [19] -->
m

<!-- b001545 | furniture | pages [19] -->
m

<!-- b001546 | furniture | pages [19] -->
m

<!-- b001547 | furniture | pages [19] -->
m

<!-- b001548 | furniture | pages [19] -->
m

<!-- b001549 | furniture | pages [19] -->
m

<!-- b001550 | furniture | pages [19] -->
m

<!-- b001551 | furniture | pages [19] -->
m

<!-- b001552 | furniture | pages [19] -->
m

<!-- b001553 | furniture | pages [19] -->
m

<!-- b001554 | furniture | pages [19] -->
m

<!-- b001555 | furniture | pages [19] -->
m

<!-- b001556 | furniture | pages [19] -->
m

<!-- b001557 | furniture | pages [19] -->
m

<!-- b001558 | furniture | pages [19] -->
m

<!-- b001559 | furniture | pages [19] -->
m

<!-- b001560 | furniture | pages [19] -->
m

<!-- b001561 | furniture | pages [19] -->
m

<!-- b001562 | furniture | pages [19] -->
m

<!-- b001563 | furniture | pages [19] -->
m

<!-- b001564 | furniture | pages [19] -->
m

<!-- b001565 | furniture | pages [19] -->
m

<!-- b001566 | furniture | pages [19] -->
m

<!-- b001567 | furniture | pages [19] -->
m

<!-- b001568 | furniture | pages [19] -->
m

<!-- b001569 | furniture | pages [19] -->
m

<!-- b001570 | furniture | pages [19] -->
m

<!-- b001571 | furniture | pages [19] -->
m

<!-- b001572 | furniture | pages [19] -->
m

<!-- b001573 | furniture | pages [19] -->
m

<!-- b001574 | furniture | pages [19] -->
m

<!-- b001575 | furniture | pages [19] -->
m

<!-- b001576 | furniture | pages [19] -->
m

<!-- b001577 | furniture | pages [19] -->
m

<!-- b001578 | furniture | pages [19] -->
m

<!-- b001579 | furniture | pages [19] -->
m

<!-- b001580 | furniture | pages [19] -->
m

<!-- b001581 | furniture | pages [19] -->
m

<!-- b001582 | furniture | pages [19] -->
m

<!-- b001583 | furniture | pages [19] -->
m

<!-- b001584 | furniture | pages [19] -->
m

<!-- b001585 | furniture | pages [19] -->
m

<!-- b001586 | furniture | pages [19] -->
m

<!-- b001587 | furniture | pages [19] -->
m

<!-- b001588 | furniture | pages [19] -->
m

<!-- b001589 | furniture | pages [19] -->
m

<!-- b001590 | furniture | pages [19] -->
m

<!-- b001591 | furniture | pages [19] -->
m

<!-- b001592 | furniture | pages [19] -->
m

<!-- b001593 | furniture | pages [19] -->
m

<!-- b001594 | furniture | pages [19] -->
m

<!-- b001595 | furniture | pages [19] -->
m

<!-- b001596 | furniture | pages [19] -->
m

<!-- b001597 | furniture | pages [19] -->
m

<!-- b001598 | furniture | pages [19] -->
m

<!-- b001599 | furniture | pages [19] -->
m

<!-- b001600 | furniture | pages [19] -->
m

<!-- b001601 | furniture | pages [19] -->
m

<!-- b001602 | furniture | pages [19] -->
m

<!-- b001603 | furniture | pages [19] -->
m

<!-- b001604 | furniture | pages [19] -->
m

<!-- b001605 | furniture | pages [19] -->
m

<!-- b001606 | furniture | pages [19] -->
m

<!-- b001607 | furniture | pages [19] -->
m

<!-- b001608 | furniture | pages [19] -->
m

<!-- b001609 | furniture | pages [19] -->
m

<!-- b001610 | furniture | pages [19] -->
m

<!-- b001611 | furniture | pages [19] -->
m

<!-- b001612 | furniture | pages [19] -->
m

<!-- b001613 | furniture | pages [19] -->
m

<!-- b001614 | furniture | pages [19] -->
m

<!-- b001615 | furniture | pages [19] -->
m

<!-- b001616 | furniture | pages [19] -->
m

<!-- b001617 | furniture | pages [19] -->
m

<!-- b001618 | furniture | pages [19] -->
m

<!-- b001619 | furniture | pages [19] -->
m

<!-- b001620 | furniture | pages [19] -->
m

<!-- b001621 | furniture | pages [19] -->
m

<!-- b001622 | furniture | pages [19] -->
m

<!-- b001623 | furniture | pages [19] -->
m

<!-- b001624 | furniture | pages [19] -->
m

<!-- b001625 | furniture | pages [19] -->
m

<!-- b001626 | furniture | pages [19] -->
m

<!-- b001627 | furniture | pages [19] -->
m

<!-- b001628 | furniture | pages [19] -->
m

<!-- b001629 | furniture | pages [19] -->
m

<!-- b001630 | furniture | pages [19] -->
m

<!-- b001631 | furniture | pages [19] -->
m

<!-- b001632 | furniture | pages [19] -->
m

<!-- b001633 | furniture | pages [19] -->
m

<!-- b001634 | furniture | pages [19] -->
m

<!-- b001635 | furniture | pages [19] -->
m

<!-- b001636 | furniture | pages [19] -->
m

<!-- b001637 | furniture | pages [19] -->
m

<!-- b001638 | furniture | pages [19] -->
m

<!-- b001639 | furniture | pages [19] -->
m

<!-- b001640 | furniture | pages [19] -->
m

<!-- b001641 | furniture | pages [19] -->
m

<!-- b001642 | furniture | pages [19] -->
m

<!-- b001643 | furniture | pages [19] -->
m

<!-- b001644 | furniture | pages [19] -->
m

<!-- b001645 | furniture | pages [19] -->
m

<!-- b001646 | furniture | pages [19] -->
m

<!-- b001647 | furniture | pages [19] -->
m

<!-- b001648 | furniture | pages [19] -->
m

<!-- b001649 | furniture | pages [19] -->
m

<!-- b001650 | furniture | pages [19] -->
m

<!-- b001651 | furniture | pages [19] -->
m

<!-- b001652 | furniture | pages [19] -->
m

<!-- b001653 | furniture | pages [19] -->
m

<!-- b001654 | furniture | pages [19] -->
m

<!-- b001655 | furniture | pages [19] -->
m

<!-- b001656 | furniture | pages [19] -->
m

<!-- b001657 | furniture | pages [19] -->
m

<!-- b001658 | furniture | pages [19] -->
m

<!-- b001659 | furniture | pages [19] -->
m

<!-- b001660 | furniture | pages [19] -->
m

<!-- b001661 | furniture | pages [19] -->
m

<!-- b001662 | furniture | pages [19] -->
m

<!-- b001663 | furniture | pages [19] -->
m

<!-- b001664 | furniture | pages [19] -->
m

<!-- b001665 | furniture | pages [19] -->
m

<!-- b001666 | furniture | pages [19] -->
m

<!-- b001667 | furniture | pages [19] -->
m

<!-- b001668 | furniture | pages [19] -->
m

<!-- b001669 | furniture | pages [20] -->
Team #2510185

<!-- b001670 | furniture | pages [20] -->
Page 20 of 24

<!-- b001672 | prose | pages [20] -->
Calculation Details:

<!-- b001673 | prose | pages [20] -->
• Total_trend:

<!-- b001674 | prose | pages [20] -->
Total_trend = pre_Total_2028 −Total_2024 (5) Total_2024 + 1 where pre_Total_2028 is the predicted medal count for the 2028 Los Angeles Olympics, and Total_2024 is the medal count from the 2024 Paris Olympics.

<!-- b001675 | prose | pages [20] -->
• Total_space:

<!-- b001676 | prose | pages [20] -->
1 Total_max  j−1 −1 Total_space = (6) Total where Total_max is the maximum medal count achieved in the event’s history, and j is the corresponding Olympic session.

<!-- b001677 | prose | pages [20] -->
Additionally, the improvement potential is influenced by the presence of dominant nations in the event. Based on the historical Olympic data and factors influencing EPI, we recommend focusing on the following events:

<!-- b001678 | prose | pages [20] -->
• China: Men’s and women’s gymnastics, men’s swimming.

<!-- b001679 | prose | pages [20] -->
• Jamaica: Men’s and women’s athletics.

<!-- b001680 | prose | pages [20] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001681 | prose | pages [20] -->
• Germany: Men’s shooting, men’s and women’s swimming. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001682 | heading | pages [20] -->
4.3.2 Post-investment Results

<!-- b001683 | prose | pages [20] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Our prediction for the above-selected sport is as is shown in Table 14. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001684 | caption | pages [20] -->
Table 14: The post-investment prediction results

<!-- b001685 | prose | pages [20] -->
NOC Events AAPI G_C N_B N_S N_G Total CHN Men’s gymnastics 67.8 0 0.50 1.33 0.50 2.41 CHN Men’s gymnastics 67.8 1 1.05 1.31 1.33 3.85 CHN Women’s gymnastics 62.7 0 0.57 0.45 0.72 1.41 CHN Women’s gymnastics 62.7 1 1.03 1.36 0.87 3.10 CHN Men’s swimming 67.8 0 0.50 1.33 0.50 2.41 CHN Men’s swimming 67.8 1 1.05 1.31 1.33 3.85 JAM Men’s athletics 68.38 0 0.71 1.61 0.907 3.32 JAM Men’s athletics 68.38 1 1.08 1.82 1.21 4.11 JAM Women’s athletics 65 0 0.66 1.26 0.72 2.68 JAM Women’s athletics 65 1 1.29 1.10 0.94 2.95 GER Men’s shooting 62.6 0 0.53 0.2 0.72 1.32 GER Men’s shooting 62.6 1 1.01 0.97 0.87 2.98 GER Women’s swimming 62.4 0 0.52 0.21 0.72 1.32 GER Women’s swimming 62.4 1 0.93 0.98 0.87 2.96 GER Men’s swimming 61.6 0 0.44 0.66 0 1.1 GER Men’s swimming 61.6 1 0.84 1.1 0.09 1.75

<!-- b001686 | prose | pages [20, 21] -->
关注数学模型 Based on our analysis, we recommend that the following three countries introduce world-class coaches in these specific events:

<!-- b001687 | furniture | pages [20] -->
2

<!-- b001688 | furniture | pages [20] -->
MATHmodels

<!-- b001689 | furniture | pages [20] -->
获取更多资讯

<!-- b001690 | furniture | pages [21] -->
Team #2510185

<!-- b001691 | furniture | pages [21] -->
Page 21 of 24

<!-- b001693 | prose | pages [21] -->
• China: Women’s gymnastics

<!-- b001694 | prose | pages [21] -->
• Jamaica: Men’s athletics 微信公众号：数学模型

<!-- b001695 | prose | pages [21] -->
• Germany: Men’s shooting

<!-- b001696 | prose | pages [21] -->
Our predictions indicate that these events are likely to see the greatest improvement in total medal counts after the introduction of great coaches, with an estimated increase of approximately 1.6 medals.

<!-- b001697 | heading | pages [21] -->
5 Task 3: Other Original Insights

<!-- b001698 | heading | pages [21] -->
5.1 Common Traits of No Medal Nations

<!-- b001699 | prose | pages [21] -->
We observed 77 nations that have never won an Olympic medal, including countries with pop- 微信号：MATHmodels ulations of tens of millions, such as Myanmar. When predicting medal acquisition, we found that nations are more likely to win their first medal when they demonstrate:

<!-- b001700 | prose | pages [21] -->
1. Long-term participation in the Games.

<!-- b001701 | prose | pages [21] -->
2. A large number of participating athletes.

<!-- b001702 | prose | pages [21] -->
3. Participation in a diverse range of sports.

<!-- b001703 | prose | pages [21] -->
For these nations determined to win medals, we recommend using our model to project the in- creased probability of medal acquisition following changes in athlete count (N_A) and event par- ticipation (N_E). Additionally, these nations could consider focusing their investments on less- dominated sports.

<!-- b001704 | heading | pages [21] -->
5.2 Negative Impact Events

<!-- b001705 | prose | pages [21] -->
Through Figure 11 (Importance of Sports to National Medal Count), we identified sports that have a negative impact on overall medal count. Given a fixed number of participating athletes, increasing participation in sports with positive importance can lead to more medals. Conversely, increasing participation in sports with negative importance is likely to result in a disproportionate investment-to-return ratio.

<!-- b001706 | prose | pages [21] -->
We recommend using our derived sport importance predictions to increase athlete participation in sports with positive importance for each nation. For example, if Germany aims to increase its medal count, it could shift investment from Boxing towards Canoeing.

<!-- b001707 | heading | pages [21] -->
5.3 Recommendations of “Great Coach”

<!-- b001708 | prose | pages [21] -->
Our model predicts that a “Great Coach” can contribute nearly 30% to performance improve- ment. Furthermore, we found that this effect is more pronounced in technically demanding sports such as Gymnastics and Shooting.

<!-- b001709 | prose | pages [21, 22] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m National Olympic Committees can use the Event Potential Index (EPI) to assess the potential performance improvement of a sport after hiring a world-class coach. By weighing the actual investment against the expected return, committees can make informed decisions about whether to hire such coaches for specific sports. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001710 | furniture | pages [21] -->
m

<!-- b001711 | furniture | pages [21] -->
m

<!-- b001712 | furniture | pages [21] -->
m

<!-- b001713 | furniture | pages [21] -->
m

<!-- b001714 | furniture | pages [21] -->
m

<!-- b001715 | furniture | pages [21] -->
m

<!-- b001716 | furniture | pages [21] -->
m

<!-- b001717 | furniture | pages [21] -->
m

<!-- b001718 | furniture | pages [21] -->
m

<!-- b001719 | furniture | pages [21] -->
m

<!-- b001720 | furniture | pages [21] -->
m

<!-- b001721 | furniture | pages [21] -->
m

<!-- b001722 | furniture | pages [21] -->
m

<!-- b001723 | furniture | pages [21] -->
m

<!-- b001724 | furniture | pages [21] -->
m

<!-- b001725 | furniture | pages [21] -->
m

<!-- b001726 | furniture | pages [21] -->
m

<!-- b001727 | furniture | pages [21] -->
m

<!-- b001728 | furniture | pages [21] -->
m

<!-- b001729 | furniture | pages [21] -->
m

<!-- b001730 | furniture | pages [21] -->
m

<!-- b001731 | furniture | pages [21] -->
m

<!-- b001732 | furniture | pages [21] -->
m

<!-- b001733 | furniture | pages [21] -->
m

<!-- b001734 | furniture | pages [21] -->
m

<!-- b001735 | furniture | pages [21] -->
m

<!-- b001736 | furniture | pages [21] -->
m

<!-- b001737 | furniture | pages [21] -->
m

<!-- b001738 | furniture | pages [21] -->
m

<!-- b001739 | furniture | pages [21] -->
m

<!-- b001740 | furniture | pages [21] -->
m

<!-- b001741 | furniture | pages [21] -->
m

<!-- b001742 | furniture | pages [21] -->
m

<!-- b001743 | furniture | pages [21] -->
m

<!-- b001744 | furniture | pages [21] -->
m

<!-- b001745 | furniture | pages [21] -->
m

<!-- b001746 | furniture | pages [21] -->
m

<!-- b001747 | furniture | pages [21] -->
m

<!-- b001748 | furniture | pages [21] -->
m

<!-- b001749 | furniture | pages [21] -->
m

<!-- b001750 | furniture | pages [21] -->
m

<!-- b001751 | furniture | pages [21] -->
m

<!-- b001752 | furniture | pages [21] -->
m

<!-- b001753 | furniture | pages [21] -->
m

<!-- b001754 | furniture | pages [21] -->
m

<!-- b001755 | furniture | pages [21] -->
m

<!-- b001756 | furniture | pages [21] -->
m

<!-- b001757 | furniture | pages [21] -->
m

<!-- b001758 | furniture | pages [21] -->
m

<!-- b001759 | furniture | pages [21] -->
m

<!-- b001760 | furniture | pages [21] -->
m

<!-- b001761 | furniture | pages [21] -->
m

<!-- b001762 | furniture | pages [21] -->
m

<!-- b001763 | furniture | pages [21] -->
m

<!-- b001764 | furniture | pages [21] -->
m

<!-- b001765 | furniture | pages [21] -->
m

<!-- b001766 | furniture | pages [21] -->
m

<!-- b001767 | furniture | pages [21] -->
m

<!-- b001768 | furniture | pages [21] -->
m

<!-- b001769 | furniture | pages [21] -->
m

<!-- b001770 | furniture | pages [21] -->
m

<!-- b001771 | furniture | pages [21] -->
m

<!-- b001772 | furniture | pages [21] -->
m

<!-- b001773 | furniture | pages [21] -->
m

<!-- b001774 | furniture | pages [21] -->
m

<!-- b001775 | furniture | pages [21] -->
m

<!-- b001776 | furniture | pages [21] -->
m

<!-- b001777 | furniture | pages [21] -->
m

<!-- b001778 | furniture | pages [21] -->
m

<!-- b001779 | furniture | pages [21] -->
m

<!-- b001780 | furniture | pages [21] -->
m

<!-- b001781 | furniture | pages [21] -->
m

<!-- b001782 | furniture | pages [21] -->
m

<!-- b001783 | furniture | pages [21] -->
m

<!-- b001784 | furniture | pages [21] -->
m

<!-- b001785 | furniture | pages [21] -->
m

<!-- b001786 | furniture | pages [21] -->
m

<!-- b001787 | furniture | pages [21] -->
m

<!-- b001788 | furniture | pages [21] -->
m

<!-- b001789 | furniture | pages [21] -->
m

<!-- b001790 | furniture | pages [21] -->
m

<!-- b001791 | furniture | pages [21] -->
m

<!-- b001792 | furniture | pages [21] -->
m

<!-- b001793 | furniture | pages [21] -->
m

<!-- b001794 | furniture | pages [21] -->
m

<!-- b001795 | furniture | pages [21] -->
m

<!-- b001796 | furniture | pages [21] -->
m

<!-- b001797 | furniture | pages [21] -->
m

<!-- b001798 | furniture | pages [21] -->
m

<!-- b001799 | furniture | pages [21] -->
m

<!-- b001800 | furniture | pages [21] -->
m

<!-- b001801 | furniture | pages [21] -->
m

<!-- b001802 | furniture | pages [21] -->
m

<!-- b001803 | furniture | pages [21] -->
m

<!-- b001804 | furniture | pages [21] -->
m

<!-- b001805 | furniture | pages [21] -->
m

<!-- b001806 | furniture | pages [21] -->
m

<!-- b001807 | furniture | pages [21] -->
m

<!-- b001808 | furniture | pages [21] -->
m

<!-- b001809 | furniture | pages [21] -->
m

<!-- b001810 | furniture | pages [21] -->
m

<!-- b001811 | furniture | pages [21] -->
m

<!-- b001812 | furniture | pages [21] -->
m

<!-- b001813 | furniture | pages [21] -->
m

<!-- b001814 | furniture | pages [21] -->
m

<!-- b001815 | furniture | pages [21] -->
m

<!-- b001816 | furniture | pages [21] -->
m

<!-- b001817 | furniture | pages [21] -->
m

<!-- b001818 | furniture | pages [21] -->
m

<!-- b001819 | furniture | pages [21] -->
m

<!-- b001820 | furniture | pages [21] -->
m

<!-- b001821 | furniture | pages [21] -->
m

<!-- b001822 | furniture | pages [21] -->
m

<!-- b001823 | furniture | pages [21] -->
m

<!-- b001824 | furniture | pages [21] -->
m

<!-- b001825 | furniture | pages [21] -->
m

<!-- b001826 | furniture | pages [21] -->
m

<!-- b001827 | furniture | pages [21] -->
m

<!-- b001828 | furniture | pages [21] -->
m

<!-- b001829 | furniture | pages [21] -->
m

<!-- b001830 | furniture | pages [21] -->
m

<!-- b001831 | furniture | pages [21] -->
m

<!-- b001832 | furniture | pages [21] -->
m

<!-- b001833 | furniture | pages [21] -->
m

<!-- b001834 | furniture | pages [21] -->
m

<!-- b001835 | furniture | pages [21] -->
m

<!-- b001836 | furniture | pages [21] -->
m

<!-- b001837 | furniture | pages [21] -->
m

<!-- b001838 | furniture | pages [21] -->
m

<!-- b001839 | furniture | pages [21] -->
m

<!-- b001840 | furniture | pages [21] -->
m

<!-- b001841 | furniture | pages [21] -->
m

<!-- b001842 | furniture | pages [21] -->
m

<!-- b001843 | furniture | pages [21] -->
m

<!-- b001844 | furniture | pages [21] -->
m

<!-- b001845 | furniture | pages [21] -->
m

<!-- b001846 | furniture | pages [21] -->
m

<!-- b001847 | furniture | pages [21] -->
m

<!-- b001848 | furniture | pages [21] -->
m

<!-- b001849 | furniture | pages [21] -->
m

<!-- b001850 | furniture | pages [21] -->
m

<!-- b001851 | furniture | pages [21] -->
m

<!-- b001852 | furniture | pages [21] -->
m

<!-- b001853 | furniture | pages [21] -->
m

<!-- b001854 | furniture | pages [21] -->
m

<!-- b001855 | furniture | pages [21] -->
m

<!-- b001856 | furniture | pages [21] -->
m

<!-- b001857 | furniture | pages [21] -->
m

<!-- b001858 | furniture | pages [21] -->
m

<!-- b001859 | furniture | pages [21] -->
m

<!-- b001860 | furniture | pages [21] -->
m

<!-- b001861 | furniture | pages [21] -->
m

<!-- b001862 | furniture | pages [21] -->
m

<!-- b001863 | furniture | pages [21] -->
m

<!-- b001864 | furniture | pages [21] -->
m

<!-- b001865 | furniture | pages [21] -->
m

<!-- b001866 | furniture | pages [21] -->
m

<!-- b001867 | furniture | pages [21] -->
m

<!-- b001868 | furniture | pages [21] -->
m

<!-- b001869 | furniture | pages [21] -->
m

<!-- b001870 | furniture | pages [21] -->
m

<!-- b001871 | furniture | pages [21] -->
m

<!-- b001872 | furniture | pages [21] -->
m

<!-- b001873 | furniture | pages [21] -->
m

<!-- b001874 | furniture | pages [21] -->
m

<!-- b001875 | furniture | pages [21] -->
m

<!-- b001876 | furniture | pages [21] -->
m

<!-- b001877 | furniture | pages [21] -->
m

<!-- b001878 | furniture | pages [21] -->
m

<!-- b001879 | furniture | pages [21] -->
m

<!-- b001880 | furniture | pages [21] -->
m

<!-- b001881 | furniture | pages [21] -->
m

<!-- b001882 | furniture | pages [21] -->
m

<!-- b001883 | furniture | pages [21] -->
m

<!-- b001884 | furniture | pages [21] -->
m

<!-- b001885 | furniture | pages [21] -->
m

<!-- b001886 | furniture | pages [21] -->
m

<!-- b001887 | furniture | pages [21] -->
m

<!-- b001888 | furniture | pages [21] -->
m

<!-- b001889 | furniture | pages [21] -->
m

<!-- b001890 | furniture | pages [21] -->
m

<!-- b001891 | furniture | pages [21] -->
m

<!-- b001892 | furniture | pages [21] -->
m

<!-- b001893 | furniture | pages [21] -->
m

<!-- b001894 | furniture | pages [21] -->
m

<!-- b001895 | furniture | pages [21] -->
m

<!-- b001896 | furniture | pages [21] -->
m

<!-- b001897 | furniture | pages [21] -->
m

<!-- b001898 | furniture | pages [21] -->
m

<!-- b001899 | furniture | pages [21] -->
m

<!-- b001900 | furniture | pages [21] -->
m

<!-- b001901 | furniture | pages [21] -->
m

<!-- b001902 | furniture | pages [21] -->
m

<!-- b001903 | furniture | pages [21] -->
m

<!-- b001904 | furniture | pages [21] -->
m

<!-- b001905 | furniture | pages [21] -->
m

<!-- b001906 | furniture | pages [21] -->
m

<!-- b001907 | furniture | pages [21] -->
m

<!-- b001908 | furniture | pages [21] -->
m

<!-- b001909 | furniture | pages [21] -->
m

<!-- b001910 | furniture | pages [21] -->
m

<!-- b001911 | furniture | pages [21] -->
m

<!-- b001912 | furniture | pages [21] -->
m

<!-- b001913 | furniture | pages [21] -->
m

<!-- b001914 | furniture | pages [21] -->
m

<!-- b001915 | furniture | pages [21] -->
m

<!-- b001916 | furniture | pages [21] -->
m

<!-- b001917 | furniture | pages [21] -->
m

<!-- b001918 | furniture | pages [21] -->
m

<!-- b001919 | furniture | pages [21] -->
m

<!-- b001920 | furniture | pages [21] -->
m

<!-- b001921 | furniture | pages [21] -->
m

<!-- b001922 | furniture | pages [21] -->
m

<!-- b001923 | furniture | pages [21] -->
m

<!-- b001924 | furniture | pages [21] -->
m

<!-- b001925 | furniture | pages [21] -->
m

<!-- b001926 | furniture | pages [21] -->
m

<!-- b001927 | furniture | pages [21] -->
m

<!-- b001928 | furniture | pages [21] -->
m

<!-- b001929 | furniture | pages [21] -->
m

<!-- b001930 | furniture | pages [21] -->
m

<!-- b001931 | furniture | pages [21] -->
m

<!-- b001932 | furniture | pages [21] -->
m

<!-- b001933 | furniture | pages [21] -->
m

<!-- b001934 | furniture | pages [21] -->
m

<!-- b001935 | furniture | pages [21] -->
m

<!-- b001936 | furniture | pages [21] -->
m

<!-- b001937 | furniture | pages [21] -->
m

<!-- b001938 | furniture | pages [21] -->
m

<!-- b001939 | furniture | pages [21] -->
m

<!-- b001940 | furniture | pages [21] -->
m

<!-- b001941 | furniture | pages [21] -->
m

<!-- b001942 | furniture | pages [21] -->
m

<!-- b001943 | furniture | pages [21] -->
m

<!-- b001944 | furniture | pages [21] -->
m

<!-- b001945 | furniture | pages [21] -->
m

<!-- b001946 | furniture | pages [21] -->
m

<!-- b001947 | furniture | pages [21] -->
m

<!-- b001948 | furniture | pages [21] -->
m

<!-- b001949 | furniture | pages [21] -->
m

<!-- b001950 | furniture | pages [21] -->
m

<!-- b001951 | furniture | pages [21] -->
m

<!-- b001952 | furniture | pages [21] -->
m

<!-- b001953 | furniture | pages [21] -->
m

<!-- b001954 | furniture | pages [21] -->
m

<!-- b001955 | furniture | pages [21] -->
m

<!-- b001956 | furniture | pages [21] -->
m

<!-- b001957 | furniture | pages [21] -->
m

<!-- b001958 | furniture | pages [21] -->
m

<!-- b001959 | furniture | pages [21] -->
m

<!-- b001960 | furniture | pages [21] -->
m

<!-- b001961 | furniture | pages [21] -->
m

<!-- b001962 | furniture | pages [21] -->
m

<!-- b001963 | furniture | pages [21] -->
m

<!-- b001964 | furniture | pages [21] -->
m

<!-- b001965 | furniture | pages [21] -->
m

<!-- b001966 | furniture | pages [21] -->
m

<!-- b001967 | furniture | pages [21] -->
m

<!-- b001968 | furniture | pages [21] -->
m

<!-- b001969 | furniture | pages [21] -->
m

<!-- b001970 | furniture | pages [21] -->
m

<!-- b001971 | furniture | pages [21] -->
m

<!-- b001972 | furniture | pages [21] -->
m

<!-- b001973 | furniture | pages [21] -->
m

<!-- b001974 | furniture | pages [21] -->
m

<!-- b001975 | furniture | pages [21] -->
m

<!-- b001976 | furniture | pages [21] -->
m

<!-- b001977 | furniture | pages [21] -->
m

<!-- b001978 | furniture | pages [21] -->
m

<!-- b001979 | furniture | pages [21] -->
m

<!-- b001980 | furniture | pages [21] -->
m

<!-- b001981 | furniture | pages [21] -->
m

<!-- b001982 | furniture | pages [21] -->
m

<!-- b001983 | furniture | pages [21] -->
m

<!-- b001984 | furniture | pages [21] -->
m

<!-- b001985 | furniture | pages [21] -->
m

<!-- b001986 | furniture | pages [21] -->
m

<!-- b001987 | furniture | pages [21] -->
m

<!-- b001988 | furniture | pages [21] -->
m

<!-- b001989 | furniture | pages [21] -->
m

<!-- b001990 | furniture | pages [21] -->
m

<!-- b001991 | furniture | pages [21] -->
m

<!-- b001992 | furniture | pages [21] -->
m

<!-- b001993 | furniture | pages [21] -->
m

<!-- b001994 | furniture | pages [21] -->
m

<!-- b001995 | furniture | pages [21] -->
m

<!-- b001996 | furniture | pages [21] -->
m

<!-- b001997 | furniture | pages [21] -->
m

<!-- b001998 | furniture | pages [21] -->
m

<!-- b001999 | furniture | pages [21] -->
m

<!-- b002000 | furniture | pages [21] -->
m

<!-- b002001 | furniture | pages [21] -->
m

<!-- b002002 | furniture | pages [21] -->
m

<!-- b002003 | furniture | pages [21] -->
m

<!-- b002004 | furniture | pages [21] -->
m

<!-- b002005 | furniture | pages [21] -->
m

<!-- b002006 | furniture | pages [21] -->
m

<!-- b002007 | furniture | pages [21] -->
m

<!-- b002008 | furniture | pages [21] -->
m

<!-- b002009 | furniture | pages [21] -->
m

<!-- b002010 | furniture | pages [21] -->
m

<!-- b002011 | furniture | pages [21] -->
m

<!-- b002012 | furniture | pages [21] -->
m

<!-- b002013 | furniture | pages [21] -->
m

<!-- b002014 | furniture | pages [21] -->
m

<!-- b002015 | furniture | pages [21] -->
m

<!-- b002016 | furniture | pages [21] -->
m

<!-- b002017 | furniture | pages [21] -->
m

<!-- b002018 | furniture | pages [21] -->
m

<!-- b002019 | furniture | pages [21] -->
m

<!-- b002020 | furniture | pages [21] -->
m

<!-- b002021 | furniture | pages [21] -->
m

<!-- b002022 | furniture | pages [21] -->
m

<!-- b002023 | furniture | pages [21] -->
m

<!-- b002024 | furniture | pages [21] -->
m

<!-- b002025 | furniture | pages [21] -->
m

<!-- b002026 | furniture | pages [21] -->
m

<!-- b002027 | furniture | pages [21] -->
m

<!-- b002028 | furniture | pages [21] -->
m

<!-- b002029 | furniture | pages [21] -->
m

<!-- b002030 | furniture | pages [21] -->
m

<!-- b002031 | furniture | pages [21] -->
m

<!-- b002032 | furniture | pages [21] -->
m

<!-- b002033 | furniture | pages [21] -->
m

<!-- b002034 | furniture | pages [22] -->
Team #2510185

<!-- b002035 | furniture | pages [22] -->
Page 22 of 24

<!-- b002037 | heading | pages [22] -->
6 Model Analysis

<!-- b002038 | prose | pages [22] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002039 | heading | pages [22] -->
6.1 Sensitivity Analysis

<!-- b002040 | prose | pages [22] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We performed 5-fold cross-validation, and the results are shown in Table 6. To further analyze m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the sensitivity of our model, we varied the size of the training set by randomly sampling 60%, 70%, and 80% of the original dataset for training and prediction. The resulting fitting curves and changes in information gain are shown in Figure 12 and Figure 13.

<!-- b002041 | prose | pages [22] -->
120 Actual Predicted (80% Train) Predicted (70% Train) 100 Predicted (60% Train)

<!-- b002042 | prose | pages [22] -->
80

<!-- b002043 | prose | pages [22] -->
Total 60

<!-- b002044 | prose | pages [22] -->
40

<!-- b002045 | prose | pages [22] -->
20

<!-- b002046 | prose | pages [22] -->
0

<!-- b002047 | prose | pages [22] -->
0 10 20 30 40 Different NOC for each Olympic Games

<!-- b002048 | caption | pages [22] -->
Figure 12: Fitting curves of different dataset

<!-- b002049 | prose | pages [22] -->
Changes in the training set size resulted in a slight decrease in predictive performance; however, the magnitude of this decrease was minimal. With training sets comprising 60%, 70%, 75%, and 80% of the original data, the model’s information gain remained relatively stable. Between 70% and 80%, minor fluctuations in the importance of the AAPI and N_E features were observed. Overall, these two features exhibited a tendency towards increased importance compared to the 60% training set. In conclusion, our model demonstrates good robustness.

<!-- b002050 | heading | pages [22] -->
6.2 Strengths and Weaknesses

<!-- b002051 | heading | pages [22] -->
Strengths:

<!-- b002052 | prose | pages [22] -->
1. We introduced a novel metric, the Athlete Potential Index (API), to assess athlete perfor- mance. This index played a significant role in model training and improved predictive accu- racy.

<!-- b002053 | prose | pages [22, 23] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b002054 | furniture | pages [22] -->
2

<!-- b002055 | furniture | pages [22] -->
MATHmodels

<!-- b002056 | furniture | pages [22] -->
获取更多资讯

<!-- b002057 | furniture | pages [23] -->
Team #2510185

<!-- b002058 | furniture | pages [23] -->
Page 23 of 24

<!-- b002060 | caption | pages [23] -->
Figure 13: Changes in information gain

<!-- b002061 | prose | pages [23] -->
2. Through a comparative analysis of Linear Regression, XGBoost, and Random Forest mod- els, we selected the optimal model for medal prediction. In the prediction set, our model achieved an R-squared (R²) value exceeding 0.87, indicating a strong goodness of fit.

<!-- b002062 | prose | pages [23] -->
3. Rigorous validation through 5-fold cross-validation and sensitivity analysis demonstrated the robustness of our model to variations in training data.

<!-- b002063 | prose | pages [23] -->
4. For the binary classification task of predicting medal acquisition (yes/no), we employed a BP neural network classifier, achieving an Area Under the ROC Curve (AUC) of 0.94, demonstrating excellent discriminatory power.

<!-- b002064 | prose | pages [23] -->
5. We provided an Event Potential Index (EPI) to guide national Olympic committees in eval- uating the potential return on investment of hiring world-class coaches for specific sports.

<!-- b002065 | heading | pages [23] -->
Weaknesses:

<!-- b002066 | prose | pages [23] -->
1. The performance of the binary classifier could potentially be further enhanced with a larger training dataset, which may lead to more reliable and generalizable results.

<!-- b002067 | prose | pages [23] -->
2. Predicting the “Great Coach” effect presents challenges in definitively identifying and quan- tifying the performance difference between existing coaches and world-class coaches. This inherent difficulty introduces uncertainty into the estimation of the coach’s contribution.

<!-- b002068 | prose | pages [23] -->
3. While we introduced the Event Potential Index (EPI), further research is needed to develop a more precise and quantitative definition of this metric, enabling more accurate and nuanced analysis.

<!-- b002069 | furniture | pages [24] -->
Team #2510185

<!-- b002070 | furniture | pages [24] -->
Page 24 of 24

<!-- b002071 | heading | pages [24] -->
7 Conclusions

<!-- b002072 | prose | pages [24] -->
In this paper, we employed a BP neural network classifier and a random forest regression model to predict the medal count for the 2028 Los Angeles Olympic Games, providing predic- tion intervals. We also assessed the key sports contributing to medal acquisition for six specific nations, identifying the sports responsible for the majority of their medals. Our analysis suggests that including locally popular or dominant sports as new Olympic events can positively impact the host nation’s medal count. We provided evidence supporting the “Great Coach” effect, estimating its contribution to be up to 28.8%, and identified potential coaching interventions for three na- tions (China, Jamaica, and Germany) projected to yield an increase of approximately 1.6 medals. Finally, we presented original insights regarding non-medal-winning nations, the importance of specific sports, and the impact of world-class coaches.

<!-- b002073 | heading | pages [24] -->
References

<!-- b002074 | references | pages [24] -->
[1] https://en.wikipedia.org/wiki/Olympic_Games.

<!-- b002075 | references | pages [24] -->
[2] https://olympics.com/en/paris-2024/medals.

<!-- b002076 | references | pages [24] -->
[3] C. Schlembach, S. L. Schmidt, D. Schreyer, and L. Wunderlich, “Forecasting the olympic

<!-- b002077 | references | pages [24] -->
medal distribution – a socioeconomic machine learning model,” Technological Forecasting

<!-- b002078 | references | pages [24] -->
and Social Change, vol. 175, p. 121314, 2022.

<!-- b002079 | references | pages [24] -->
[4] https://www.nielsen.com/news-center/2024/virtual-medal-table-forecast/.

<!-- b002080 | references | pages [24] -->
[5] M. A. Ruiz Estrada, “A new indicator to evaluate any country performance in the olympic

<!-- b002081 | references | pages [24] -->
games: The olympia-index,” Available at SSRN 4920383, 2024.

<!-- b002082 | references | pages [24] -->
[6] https://www.thepaper.cn/newsDetail_forward_16567025.

<!-- b002083 | references | pages [24] -->
[7] J. Luo, “Research on the change of the project setting of the modern summer olympic games

<!-- b002084 | references | pages [24] -->
(1984-2020),” Ph.D. dissertation, Changsha: Hunan Normal University 2020, 2020.

<!-- b002085 | references | pages [24] -->
[8] https://www.olympics.com/zh/athletes/ping-lang.

<!-- b002086 | references | pages [24] -->
关注数学模型

<!-- b002087 | furniture | pages [24] -->
2

<!-- b002088 | furniture | pages [24] -->
MATHmodels

<!-- b002089 | furniture | pages [24] -->
获取更多资讯
