# P-C-2025-2510185-3f933168

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
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

<!-- b000022 | furniture | pages [4] -->
Team #2510185

<!-- b000023 | furniture | pages [4] -->
Page 4 of 24

<!-- b000024 | prose | pages [4] -->
of the model and estimate the uncertainty or accuracy of the prediction.

<!-- b000025 | prose | pages [4] -->
• Specific Event type analysis: Consider the number and types of events, explore the relationships between events, and the number of medals won by each country in each event. Examine the most dominant events in each country, and analyze the reasons and impact on the results.

<!-- b000026 | heading | pages [4] -->
• Model prediction:

<!-- b000027 | prose | pages [4] -->
1. Predict the medal table for the 2028 Summer Olympics in Los Angeles and give a prediction interval for the result. Analyze countries that may improve or decline.

<!-- b000028 | prose | pages [4] -->
2. Focus on countries/regions that have not yet won a medal and predict their probability of winning their first medal at the 2028 Olympics.

<!-- b000029 | prose | pages [4] -->
• Explore the existence of the "Great Coach" effect: Look for changes due to the "Great Coach" effect and estimate its impact on medal changes. Select three countries, determine the sports in which they should consider investing in a great coach, and estimate the impact.

<!-- b000030 | prose | pages [4] -->
• Explore other patterns: Analyze other patterns related to the number of medals displayed by the model. Use these findings to inform the Olympic committees of various countries.

<!-- b000031 | prose | pages [4] -->
1.3 Our work

<!-- b000032 | prose | pages [4] -->
Task 1: Medal prediction by API

<!-- b000033 | prose | pages [4] -->
Gold

<!-- b000034 | prose | pages [4] -->
Performance of a athlete(PWM)

<!-- b000035 | prose | pages [4] -->
Sliver

<!-- b000036 | prose | pages [4] -->
Task 2: The impact of “Great Coach”

<!-- b000037 | prose | pages [4] -->
Event select

<!-- b000038 | prose | pages [4] -->
min_samples_split n_estimators max_depth

<!-- b000039 | prose | pages [4] -->
180 10

<!-- b000040 | prose | pages [4] -->
Bronze

<!-- b000041 | heading | pages [4] -->
3 models

<!-- b000042 | prose | pages [4] -->
Athlete Potential Index(API)

<!-- b000043 | prose | pages [4] -->
4 4

<!-- b000044 | prose | pages [4] -->
Event Potential Index(EPI)

<!-- b000045 | prose | pages [4] -->
Grid searchCV

<!-- b000046 | prose | pages [4] -->
Comparison

<!-- b000047 | prose | pages [4] -->
Participation scale(PS)

<!-- b000048 | prose | pages [4] -->
R2 =0.8792

<!-- b000049 | prose | pages [4] -->
…

<!-- b000050 | prose | pages [4] -->
Features

<!-- b000051 | prose | pages [4] -->
Random

<!-- b000052 | prose | pages [4] -->
Forest

<!-- b000053 | prose | pages [4] -->
Task 1.3

<!-- b000054 | prose | pages [4] -->
Trend

<!-- b000055 | prose | pages [4] -->
Pressure AAPI Space

<!-- b000056 | prose | pages [4] -->
EPI=ω1×Total_trend+ω2×Total_space+ω3×AAPI

<!-- b000057 | prose | pages [4] -->
Task 1.1 Task 1.2

<!-- b000058 | prose | pages [4] -->
BP neural network

<!-- b000059 | prose | pages [4] -->
Events improtance

<!-- b000060 | prose | pages [4] -->
Model Prediction

<!-- b000061 | prose | pages [4] -->
Bootstrap

<!-- b000062 | prose | pages [4] -->
classification

<!-- b000063 | prose | pages [4] -->
VMT

<!-- b000064 | prose | pages [4] -->
95% Confidence

<!-- b000065 | prose | pages [4] -->
Task 3: original insights

<!-- b000066 | prose | pages [4] -->
The Contribution of “Great Coach” : 28.8%

<!-- b000067 | prose | pages [4] -->
•AAPI≈65，Bronze 0.9, Sliver 0.2, Gold 0.02, Total 1.2 •AAPI≈70，Bronze 0.7, Sliver 0.9, Gold 0.2 , Total 1.8

<!-- b000068 | prose | pages [4] -->
USA

<!-- b000069 | heading | pages [4] -->
Sensitivity Analyses

<!-- b000070 | prose | pages [4] -->
KOR

<!-- b000071 | heading | pages [4] -->
50% cross validation

<!-- b000072 | prose | pages [4] -->
60,70,80% Training set

<!-- b000073 | prose | pages [4] -->
R2 =0.7642 Small fluctuations

<!-- b000074 | prose | pages [4] -->
Suggestions for the

<!-- b000075 | prose | pages [4] -->
Unawarded countries

<!-- b000076 | prose | pages [4] -->
Medals of negative

<!-- b000077 | prose | pages [4] -->
'Great Coach' Effect

<!-- b000078 | prose | pages [4] -->
get medal

<!-- b000079 | prose | pages [4] -->
importance

<!-- b000080 | prose | pages [4] -->
High Level of Robustness

<!-- b000081 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000082 | prose | pages [4] -->
关注数学模型

<!-- b000083 | furniture | pages [4] -->
2

<!-- b000084 | furniture | pages [4] -->
MATHmodels

<!-- b000085 | furniture | pages [4] -->
获取更多资讯

<!-- b000086 | furniture | pages [5] -->
Team #2510185

<!-- b000087 | furniture | pages [5] -->
Page 5 of 24

<!-- b000088 | prose | pages [5] -->
2

<!-- b000089 | heading | pages [5] -->
Preparation for Modeling

<!-- b000090 | prose | pages [5] -->
2.1

<!-- b000091 | heading | pages [5] -->
Assumptions

<!-- b000092 | prose | pages [5] -->
We make the following assumptions to complete our model. In addition, we will refine these simplified assumptions later.

<!-- b000093 | prose | pages [5] -->
• We assume that an athlete’s competitive ability can be fully inferred from the historical data provided. This is because the given dataset only contains information about a player’s

<!-- b000094 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000095 | prose | pages [5] -->
participation in previous Olympic Games and the medals he won (gold, silver, or bronze). We believe that a player’s ability based on this information is sufficient.

<!-- b000096 | prose | pages [5] -->
• We assume that the competitive ability of an athlete or team remains constant over the four years between games. This is because we cannot obtain any other information about athletes between Games from the dataset provided.

<!-- b000097 | prose | pages [5] -->
• We assume that the probability of a country that has never won a medal to win a medal is only related to the historical data of previous participation. This is because there is no more realistic data on countries that have never won a medal in the data set provided. Although this may be a relatively important factor.

<!-- b000098 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000099 | prose | pages [5] -->
2.2

<!-- b000100 | heading | pages [5] -->
Notations

<!-- b000101 | caption | pages [5] -->
Table 1: Notations Table

<!-- b000102 | heading | pages [5] -->
Symbol

<!-- b000103 | prose | pages [5] -->
Description

<!-- b000104 | prose | pages [5] -->
PES Performance score of an athlete/team PWM Medals won by an athlete/team HA Host advantage The Olympic Games of number i Ni API Athlete Potential Index EPI Event Potential Index PS Scale of Participation (by NOC)

<!-- b000105 | prose | pages [5] -->
2.3

<!-- b000106 | heading | pages [5] -->
Data Processing

<!-- b000107 | prose | pages [5] -->
After observing the datasets provided by the topic, summerOly_athletes.csv, summerOly_hosts.csv, summerOly_medal_counts.csv and summerOly_programs.csv contain some abnormal or missing values. The following describes the data processing of these abnormal and missing values. Further data processing will be done as needed in the later text. The processing procedures are shown in

<!-- b000108 | caption | pages [5] -->
Figure 3.

<!-- b000109 | prose | pages [5] -->
m

<!-- b000110 | prose | pages [5] -->
m

<!-- b000111 | prose | pages [5] -->
m

<!-- b000112 | prose | pages [5] -->
m

<!-- b000113 | prose | pages [5] -->
m

<!-- b000114 | prose | pages [5] -->
m

<!-- b000115 | prose | pages [5] -->
m

<!-- b000116 | prose | pages [5] -->
m

<!-- b000117 | prose | pages [5] -->
m

<!-- b000118 | prose | pages [5] -->
m

<!-- b000119 | prose | pages [5] -->
m

<!-- b000120 | prose | pages [5] -->
m

<!-- b000121 | prose | pages [5] -->
m

<!-- b000122 | prose | pages [5] -->
m

<!-- b000123 | prose | pages [5] -->
m

<!-- b000124 | prose | pages [5] -->
m

<!-- b000125 | prose | pages [5] -->
m

<!-- b000126 | prose | pages [5] -->
m

<!-- b000127 | prose | pages [5] -->
m

<!-- b000128 | prose | pages [5] -->
m

<!-- b000129 | prose | pages [5] -->
m

<!-- b000130 | prose | pages [5] -->
m

<!-- b000131 | prose | pages [5] -->
m

<!-- b000132 | prose | pages [5] -->
m

<!-- b000133 | prose | pages [5] -->
m

<!-- b000134 | prose | pages [5] -->
m

<!-- b000135 | prose | pages [5] -->
m

<!-- b000136 | prose | pages [5] -->
m

<!-- b000137 | prose | pages [5] -->
m

<!-- b000138 | prose | pages [5] -->
m

<!-- b000139 | prose | pages [5] -->
m

<!-- b000140 | prose | pages [5] -->
m

<!-- b000141 | prose | pages [5] -->
m

<!-- b000142 | prose | pages [5] -->
m

<!-- b000143 | prose | pages [5] -->
m

<!-- b000144 | prose | pages [5] -->
m

<!-- b000145 | prose | pages [5] -->
m

<!-- b000146 | prose | pages [5] -->
m

<!-- b000147 | prose | pages [5] -->
m

<!-- b000148 | prose | pages [5] -->
m

<!-- b000149 | prose | pages [5] -->
m

<!-- b000150 | prose | pages [5] -->
m

<!-- b000151 | prose | pages [5] -->
m

<!-- b000152 | prose | pages [5] -->
m

<!-- b000153 | prose | pages [5] -->
m

<!-- b000154 | prose | pages [5] -->
m

<!-- b000155 | prose | pages [5] -->
m

<!-- b000156 | prose | pages [5] -->
m

<!-- b000157 | prose | pages [5] -->
m

<!-- b000158 | prose | pages [5] -->
m

<!-- b000159 | prose | pages [5] -->
m

<!-- b000160 | prose | pages [5] -->
m

<!-- b000161 | prose | pages [5] -->
m

<!-- b000162 | prose | pages [5] -->
m

<!-- b000163 | prose | pages [5] -->
m

<!-- b000164 | prose | pages [5] -->
m

<!-- b000165 | prose | pages [5] -->
m

<!-- b000166 | prose | pages [5] -->
m

<!-- b000167 | prose | pages [5] -->
m

<!-- b000168 | prose | pages [5] -->
m

<!-- b000169 | prose | pages [5] -->
m

<!-- b000170 | prose | pages [5] -->
m

<!-- b000171 | prose | pages [5] -->
m

<!-- b000172 | prose | pages [5] -->
m

<!-- b000173 | prose | pages [5] -->
m

<!-- b000174 | prose | pages [5] -->
m

<!-- b000175 | prose | pages [5] -->
m

<!-- b000176 | prose | pages [5] -->
m

<!-- b000177 | prose | pages [5] -->
m

<!-- b000178 | prose | pages [5] -->
m

<!-- b000179 | prose | pages [5] -->
m

<!-- b000180 | prose | pages [5] -->
m

<!-- b000181 | prose | pages [5] -->
m

<!-- b000182 | prose | pages [5] -->
m

<!-- b000183 | prose | pages [5] -->
m

<!-- b000184 | prose | pages [5] -->
m

<!-- b000185 | prose | pages [5] -->
m

<!-- b000186 | prose | pages [5] -->
m

<!-- b000187 | prose | pages [5] -->
m

<!-- b000188 | prose | pages [5] -->
m

<!-- b000189 | prose | pages [5] -->
m

<!-- b000190 | prose | pages [5] -->
m

<!-- b000191 | prose | pages [5] -->
m

<!-- b000192 | prose | pages [5] -->
m

<!-- b000193 | prose | pages [5] -->
m

<!-- b000194 | prose | pages [5] -->
m

<!-- b000195 | prose | pages [5] -->
m

<!-- b000196 | prose | pages [5] -->
m

<!-- b000197 | prose | pages [5] -->
m

<!-- b000198 | prose | pages [5] -->
m

<!-- b000199 | prose | pages [5] -->
m

<!-- b000200 | prose | pages [5] -->
m

<!-- b000201 | prose | pages [5] -->
m

<!-- b000202 | prose | pages [5] -->
m

<!-- b000203 | prose | pages [5] -->
m

<!-- b000204 | prose | pages [5] -->
m

<!-- b000205 | prose | pages [5] -->
m

<!-- b000206 | prose | pages [5] -->
m

<!-- b000207 | prose | pages [5] -->
m

<!-- b000208 | prose | pages [5] -->
m

<!-- b000209 | prose | pages [5] -->
m

<!-- b000210 | prose | pages [5] -->
m

<!-- b000211 | prose | pages [5] -->
m

<!-- b000212 | prose | pages [5] -->
m

<!-- b000213 | prose | pages [5] -->
m

<!-- b000214 | prose | pages [5] -->
m

<!-- b000215 | prose | pages [5] -->
m

<!-- b000216 | prose | pages [5] -->
m

<!-- b000217 | prose | pages [5] -->
m

<!-- b000218 | prose | pages [5] -->
m

<!-- b000219 | prose | pages [5] -->
m

<!-- b000220 | prose | pages [5] -->
m

<!-- b000221 | prose | pages [5] -->
m

<!-- b000222 | prose | pages [5] -->
m

<!-- b000223 | prose | pages [5] -->
m

<!-- b000224 | prose | pages [5] -->
m

<!-- b000225 | prose | pages [5] -->
m

<!-- b000226 | prose | pages [5] -->
m

<!-- b000227 | prose | pages [5] -->
m

<!-- b000228 | prose | pages [5] -->
m

<!-- b000229 | prose | pages [5] -->
m

<!-- b000230 | prose | pages [5] -->
m

<!-- b000231 | prose | pages [5] -->
m

<!-- b000232 | prose | pages [5] -->
m

<!-- b000233 | prose | pages [5] -->
m

<!-- b000234 | prose | pages [5] -->
m

<!-- b000235 | prose | pages [5] -->
m

<!-- b000236 | prose | pages [5] -->
m

<!-- b000237 | prose | pages [5] -->
m

<!-- b000238 | prose | pages [5] -->
m

<!-- b000239 | prose | pages [5] -->
m

<!-- b000240 | prose | pages [5] -->
m

<!-- b000241 | prose | pages [5] -->
m

<!-- b000242 | prose | pages [5] -->
m

<!-- b000243 | prose | pages [5] -->
m

<!-- b000244 | prose | pages [5] -->
m

<!-- b000245 | prose | pages [5] -->
m

<!-- b000246 | prose | pages [5] -->
m

<!-- b000247 | prose | pages [5] -->
m

<!-- b000248 | prose | pages [5] -->
m

<!-- b000249 | prose | pages [5] -->
m

<!-- b000250 | prose | pages [5] -->
m

<!-- b000251 | prose | pages [5] -->
m

<!-- b000252 | prose | pages [5] -->
m

<!-- b000253 | prose | pages [5] -->
m

<!-- b000254 | prose | pages [5] -->
m

<!-- b000255 | prose | pages [5] -->
m

<!-- b000256 | prose | pages [5] -->
m

<!-- b000257 | prose | pages [5] -->
m

<!-- b000258 | prose | pages [5] -->
m

<!-- b000259 | prose | pages [5] -->
m

<!-- b000260 | prose | pages [5] -->
m

<!-- b000261 | prose | pages [5] -->
m

<!-- b000262 | prose | pages [5] -->
m

<!-- b000263 | prose | pages [5] -->
m

<!-- b000264 | prose | pages [5] -->
m

<!-- b000265 | prose | pages [5] -->
m

<!-- b000266 | prose | pages [5] -->
m

<!-- b000267 | prose | pages [5] -->
m

<!-- b000268 | prose | pages [5] -->
m

<!-- b000269 | prose | pages [5] -->
m

<!-- b000270 | prose | pages [5] -->
m

<!-- b000271 | prose | pages [5] -->
m

<!-- b000272 | prose | pages [5] -->
m

<!-- b000273 | prose | pages [5] -->
m

<!-- b000274 | prose | pages [5] -->
m

<!-- b000275 | prose | pages [5] -->
m

<!-- b000276 | prose | pages [5] -->
m

<!-- b000277 | prose | pages [5] -->
m

<!-- b000278 | prose | pages [5] -->
m

<!-- b000279 | prose | pages [5] -->
m

<!-- b000280 | prose | pages [5] -->
m

<!-- b000281 | prose | pages [5] -->
m

<!-- b000282 | prose | pages [5] -->
m

<!-- b000283 | prose | pages [5] -->
m

<!-- b000284 | prose | pages [5] -->
m

<!-- b000285 | prose | pages [5] -->
m

<!-- b000286 | prose | pages [5] -->
m

<!-- b000287 | prose | pages [5] -->
m

<!-- b000288 | prose | pages [5] -->
m

<!-- b000289 | prose | pages [5] -->
m

<!-- b000290 | prose | pages [5] -->
m

<!-- b000291 | prose | pages [5] -->
m

<!-- b000292 | prose | pages [5] -->
m

<!-- b000293 | prose | pages [5] -->
m

<!-- b000294 | prose | pages [5] -->
m

<!-- b000295 | prose | pages [5] -->
m

<!-- b000296 | prose | pages [5] -->
m

<!-- b000297 | prose | pages [5] -->
m

<!-- b000298 | prose | pages [5] -->
m

<!-- b000299 | prose | pages [5] -->
m

<!-- b000300 | prose | pages [5] -->
m

<!-- b000301 | prose | pages [5] -->
m

<!-- b000302 | prose | pages [5] -->
m

<!-- b000303 | prose | pages [5] -->
m

<!-- b000304 | prose | pages [5] -->
m

<!-- b000305 | prose | pages [5] -->
m

<!-- b000306 | prose | pages [5] -->
m

<!-- b000307 | prose | pages [5] -->
m

<!-- b000308 | prose | pages [5] -->
m

<!-- b000309 | prose | pages [5] -->
m

<!-- b000310 | prose | pages [5] -->
m

<!-- b000311 | prose | pages [5] -->
m

<!-- b000312 | prose | pages [5] -->
m

<!-- b000313 | prose | pages [5] -->
m

<!-- b000314 | prose | pages [5] -->
m

<!-- b000315 | prose | pages [5] -->
m

<!-- b000316 | prose | pages [5] -->
m

<!-- b000317 | prose | pages [5] -->
m

<!-- b000318 | prose | pages [5] -->
m

<!-- b000319 | prose | pages [5] -->
m

<!-- b000320 | prose | pages [5] -->
m

<!-- b000321 | prose | pages [5] -->
m

<!-- b000322 | prose | pages [5] -->
m

<!-- b000323 | prose | pages [5] -->
m

<!-- b000324 | prose | pages [5] -->
m

<!-- b000325 | prose | pages [5] -->
m

<!-- b000326 | prose | pages [5] -->
m

<!-- b000327 | prose | pages [5] -->
m

<!-- b000328 | prose | pages [5] -->
m

<!-- b000329 | prose | pages [5] -->
m

<!-- b000330 | prose | pages [5] -->
m

<!-- b000331 | prose | pages [5] -->
m

<!-- b000332 | prose | pages [5] -->
m

<!-- b000333 | prose | pages [5] -->
m

<!-- b000334 | prose | pages [5] -->
m

<!-- b000335 | prose | pages [5] -->
m

<!-- b000336 | prose | pages [5] -->
m

<!-- b000337 | prose | pages [5] -->
m

<!-- b000338 | prose | pages [5] -->
m

<!-- b000339 | prose | pages [5] -->
m

<!-- b000340 | prose | pages [5] -->
m

<!-- b000341 | prose | pages [5] -->
m

<!-- b000342 | prose | pages [5] -->
m

<!-- b000343 | prose | pages [5] -->
m

<!-- b000344 | prose | pages [5] -->
m

<!-- b000345 | prose | pages [5] -->
m

<!-- b000346 | prose | pages [5] -->
m

<!-- b000347 | prose | pages [5] -->
m

<!-- b000348 | prose | pages [5] -->
m

<!-- b000349 | prose | pages [5] -->
m

<!-- b000350 | prose | pages [5] -->
m

<!-- b000351 | prose | pages [5] -->
m

<!-- b000352 | prose | pages [5] -->
m

<!-- b000353 | prose | pages [5] -->
m

<!-- b000354 | prose | pages [5] -->
m

<!-- b000355 | prose | pages [5] -->
m

<!-- b000356 | prose | pages [5] -->
m

<!-- b000357 | prose | pages [5] -->
m

<!-- b000358 | prose | pages [5] -->
m

<!-- b000359 | prose | pages [5] -->
m

<!-- b000360 | prose | pages [5] -->
m

<!-- b000361 | prose | pages [5] -->
m

<!-- b000362 | prose | pages [5] -->
m

<!-- b000363 | prose | pages [5] -->
m

<!-- b000364 | prose | pages [5] -->
m

<!-- b000365 | prose | pages [5] -->
m

<!-- b000366 | prose | pages [5] -->
m

<!-- b000367 | prose | pages [5] -->
m

<!-- b000368 | prose | pages [5] -->
m

<!-- b000369 | prose | pages [5] -->
m

<!-- b000370 | prose | pages [5] -->
m

<!-- b000371 | prose | pages [5] -->
m

<!-- b000372 | prose | pages [5] -->
m

<!-- b000373 | prose | pages [5] -->
m

<!-- b000374 | prose | pages [5] -->
m

<!-- b000375 | prose | pages [5] -->
m

<!-- b000376 | prose | pages [5] -->
m

<!-- b000377 | prose | pages [5] -->
m

<!-- b000378 | prose | pages [5] -->
m

<!-- b000379 | prose | pages [5] -->
m

<!-- b000380 | prose | pages [5] -->
m

<!-- b000381 | prose | pages [5] -->
m

<!-- b000382 | prose | pages [5] -->
m

<!-- b000383 | prose | pages [5] -->
m

<!-- b000384 | prose | pages [5] -->
m

<!-- b000385 | prose | pages [5] -->
m

<!-- b000386 | prose | pages [5] -->
m

<!-- b000387 | prose | pages [5] -->
m

<!-- b000388 | prose | pages [5] -->
m

<!-- b000389 | prose | pages [5] -->
m

<!-- b000390 | prose | pages [5] -->
m

<!-- b000391 | prose | pages [5] -->
m

<!-- b000392 | prose | pages [5] -->
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

<!-- b000459 | furniture | pages [5] -->
m

<!-- b000460 | furniture | pages [5] -->
m

<!-- b000461 | furniture | pages [5] -->
m

<!-- b000462 | furniture | pages [5] -->
m

<!-- b000463 | furniture | pages [5] -->
m

<!-- b000464 | furniture | pages [5] -->
m

<!-- b000465 | furniture | pages [5] -->
m

<!-- b000466 | furniture | pages [5] -->
m

<!-- b000467 | furniture | pages [5] -->
m

<!-- b000468 | furniture | pages [5] -->
m

<!-- b000469 | furniture | pages [5] -->
m

<!-- b000470 | furniture | pages [5] -->
m

<!-- b000471 | furniture | pages [5] -->
m

<!-- b000472 | furniture | pages [5] -->
m

<!-- b000473 | furniture | pages [5] -->
m

<!-- b000474 | furniture | pages [5] -->
m

<!-- b000475 | furniture | pages [5] -->
m

<!-- b000476 | furniture | pages [5] -->
m

<!-- b000477 | furniture | pages [5] -->
m

<!-- b000478 | furniture | pages [5] -->
m

<!-- b000479 | furniture | pages [5] -->
m

<!-- b000480 | furniture | pages [5] -->
m

<!-- b000481 | furniture | pages [5] -->
m

<!-- b000482 | furniture | pages [5] -->
m

<!-- b000483 | furniture | pages [5] -->
m

<!-- b000484 | furniture | pages [5] -->
m

<!-- b000485 | furniture | pages [5] -->
m

<!-- b000486 | furniture | pages [5] -->
m

<!-- b000487 | furniture | pages [5] -->
m

<!-- b000488 | furniture | pages [5] -->
m

<!-- b000489 | furniture | pages [5] -->
m

<!-- b000490 | furniture | pages [5] -->
m

<!-- b000491 | furniture | pages [5] -->
m

<!-- b000492 | furniture | pages [5] -->
m

<!-- b000493 | furniture | pages [5] -->
m

<!-- b000494 | furniture | pages [5] -->
m

<!-- b000495 | furniture | pages [5] -->
m

<!-- b000496 | furniture | pages [5] -->
m

<!-- b000497 | furniture | pages [5] -->
m

<!-- b000498 | furniture | pages [5] -->
m

<!-- b000499 | furniture | pages [5] -->
m

<!-- b000500 | furniture | pages [5] -->
m

<!-- b000501 | furniture | pages [5] -->
m

<!-- b000502 | furniture | pages [5] -->
m

<!-- b000503 | furniture | pages [5] -->
m

<!-- b000504 | furniture | pages [5] -->
m

<!-- b000505 | furniture | pages [5] -->
m

<!-- b000506 | furniture | pages [5] -->
m

<!-- b000507 | furniture | pages [5] -->
m

<!-- b000508 | furniture | pages [5] -->
m

<!-- b000509 | furniture | pages [5] -->
m

<!-- b000510 | furniture | pages [5] -->
m

<!-- b000511 | furniture | pages [5] -->
m

<!-- b000512 | furniture | pages [5] -->
m

<!-- b000513 | furniture | pages [5] -->
m

<!-- b000514 | furniture | pages [5] -->
m

<!-- b000515 | furniture | pages [5] -->
m

<!-- b000516 | furniture | pages [5] -->
m

<!-- b000517 | furniture | pages [5] -->
m

<!-- b000518 | furniture | pages [5] -->
m

<!-- b000519 | furniture | pages [5] -->
m

<!-- b000520 | furniture | pages [5] -->
m

<!-- b000521 | furniture | pages [5] -->
m

<!-- b000522 | furniture | pages [5] -->
m

<!-- b000523 | furniture | pages [5] -->
m

<!-- b000524 | furniture | pages [5] -->
m

<!-- b000525 | furniture | pages [5] -->
m

<!-- b000526 | furniture | pages [5] -->
m

<!-- b000527 | furniture | pages [5] -->
m

<!-- b000528 | furniture | pages [5] -->
m

<!-- b000529 | furniture | pages [5] -->
m

<!-- b000530 | furniture | pages [5] -->
m

<!-- b000531 | furniture | pages [5] -->
m

<!-- b000532 | furniture | pages [5] -->
m

<!-- b000533 | furniture | pages [5] -->
m

<!-- b000534 | furniture | pages [5] -->
m

<!-- b000535 | furniture | pages [5] -->
m

<!-- b000536 | furniture | pages [5] -->
m

<!-- b000537 | furniture | pages [5] -->
m

<!-- b000538 | furniture | pages [5] -->
m

<!-- b000539 | furniture | pages [5] -->
m

<!-- b000540 | furniture | pages [5] -->
m

<!-- b000541 | furniture | pages [5] -->
m

<!-- b000542 | furniture | pages [5] -->
m

<!-- b000543 | furniture | pages [5] -->
m

<!-- b000544 | furniture | pages [5] -->
m

<!-- b000545 | furniture | pages [5] -->
m

<!-- b000546 | furniture | pages [5] -->
m

<!-- b000547 | furniture | pages [5] -->
m

<!-- b000548 | furniture | pages [5] -->
m

<!-- b000549 | furniture | pages [5] -->
m

<!-- b000550 | furniture | pages [5] -->
m

<!-- b000551 | furniture | pages [5] -->
m

<!-- b000552 | furniture | pages [5] -->
m

<!-- b000553 | furniture | pages [5] -->
m

<!-- b000554 | furniture | pages [5] -->
m

<!-- b000555 | furniture | pages [5] -->
m

<!-- b000556 | furniture | pages [5] -->
m

<!-- b000557 | furniture | pages [5] -->
m

<!-- b000558 | furniture | pages [5] -->
m

<!-- b000559 | furniture | pages [5] -->
m

<!-- b000560 | furniture | pages [5] -->
m

<!-- b000561 | furniture | pages [5] -->
m

<!-- b000562 | furniture | pages [5] -->
m

<!-- b000563 | furniture | pages [5] -->
m

<!-- b000564 | furniture | pages [5] -->
m

<!-- b000565 | furniture | pages [5] -->
m

<!-- b000566 | furniture | pages [5] -->
m

<!-- b000567 | furniture | pages [5] -->
m

<!-- b000568 | furniture | pages [5] -->
m

<!-- b000569 | furniture | pages [5] -->
m

<!-- b000570 | furniture | pages [5] -->
m

<!-- b000571 | furniture | pages [5] -->
m

<!-- b000572 | furniture | pages [5] -->
m

<!-- b000573 | furniture | pages [5] -->
m

<!-- b000574 | furniture | pages [5] -->
m

<!-- b000575 | furniture | pages [5] -->
m

<!-- b000576 | furniture | pages [5] -->
m

<!-- b000577 | furniture | pages [5] -->
m

<!-- b000578 | furniture | pages [5] -->
m

<!-- b000579 | furniture | pages [5] -->
m

<!-- b000580 | furniture | pages [5] -->
m

<!-- b000581 | furniture | pages [5] -->
m

<!-- b000582 | furniture | pages [5] -->
m

<!-- b000583 | furniture | pages [5] -->
m

<!-- b000584 | furniture | pages [5] -->
m

<!-- b000585 | furniture | pages [5] -->
m

<!-- b000586 | furniture | pages [5] -->
m

<!-- b000587 | furniture | pages [5] -->
m

<!-- b000588 | furniture | pages [5] -->
m

<!-- b000589 | furniture | pages [5] -->
m

<!-- b000590 | furniture | pages [5] -->
m

<!-- b000591 | furniture | pages [5] -->
m

<!-- b000592 | furniture | pages [5] -->
m

<!-- b000593 | furniture | pages [5] -->
m

<!-- b000594 | furniture | pages [5] -->
m

<!-- b000595 | furniture | pages [5] -->
m

<!-- b000596 | furniture | pages [5] -->
m

<!-- b000597 | furniture | pages [5] -->
m

<!-- b000598 | furniture | pages [5] -->
m

<!-- b000599 | furniture | pages [5] -->
m

<!-- b000600 | furniture | pages [5] -->
m

<!-- b000601 | furniture | pages [5] -->
m

<!-- b000602 | furniture | pages [5] -->
m

<!-- b000603 | furniture | pages [5] -->
m

<!-- b000604 | furniture | pages [5] -->
m

<!-- b000605 | furniture | pages [5] -->
m

<!-- b000606 | furniture | pages [5] -->
m

<!-- b000607 | furniture | pages [5] -->
m

<!-- b000608 | furniture | pages [5] -->
m

<!-- b000609 | furniture | pages [5] -->
m

<!-- b000610 | furniture | pages [5] -->
m

<!-- b000611 | furniture | pages [5] -->
m

<!-- b000612 | furniture | pages [5] -->
m

<!-- b000613 | furniture | pages [5] -->
m

<!-- b000614 | furniture | pages [5] -->
m

<!-- b000615 | furniture | pages [5] -->
m

<!-- b000616 | furniture | pages [5] -->
m

<!-- b000617 | furniture | pages [5] -->
m

<!-- b000618 | furniture | pages [5] -->
m

<!-- b000619 | furniture | pages [5] -->
m

<!-- b000620 | furniture | pages [5] -->
m

<!-- b000621 | furniture | pages [5] -->
m

<!-- b000622 | furniture | pages [5] -->
m

<!-- b000623 | furniture | pages [5] -->
m

<!-- b000624 | furniture | pages [5] -->
m

<!-- b000625 | furniture | pages [5] -->
m

<!-- b000626 | furniture | pages [5] -->
m

<!-- b000627 | furniture | pages [5] -->
m

<!-- b000628 | furniture | pages [5] -->
m

<!-- b000629 | furniture | pages [5] -->
m

<!-- b000630 | furniture | pages [5] -->
m

<!-- b000631 | furniture | pages [5] -->
m

<!-- b000632 | furniture | pages [5] -->
m

<!-- b000633 | furniture | pages [5] -->
m

<!-- b000634 | furniture | pages [5] -->
m

<!-- b000635 | furniture | pages [5] -->
m

<!-- b000636 | furniture | pages [5] -->
m

<!-- b000637 | furniture | pages [5] -->
m

<!-- b000638 | furniture | pages [5] -->
m

<!-- b000639 | furniture | pages [5] -->
m

<!-- b000640 | furniture | pages [5] -->
m

<!-- b000641 | furniture | pages [5] -->
m

<!-- b000642 | furniture | pages [5] -->
m

<!-- b000643 | furniture | pages [5] -->
m

<!-- b000644 | furniture | pages [5] -->
m

<!-- b000645 | furniture | pages [5] -->
m

<!-- b000646 | furniture | pages [5] -->
m

<!-- b000647 | furniture | pages [5] -->
m

<!-- b000648 | furniture | pages [5] -->
m

<!-- b000649 | furniture | pages [5] -->
m

<!-- b000650 | furniture | pages [5] -->
m

<!-- b000651 | furniture | pages [5] -->
m

<!-- b000652 | furniture | pages [5] -->
m

<!-- b000653 | furniture | pages [5] -->
m

<!-- b000654 | furniture | pages [5] -->
m

<!-- b000655 | furniture | pages [5] -->
m

<!-- b000656 | furniture | pages [5] -->
m

<!-- b000657 | furniture | pages [5] -->
m

<!-- b000658 | furniture | pages [5] -->
m

<!-- b000659 | furniture | pages [5] -->
m

<!-- b000660 | furniture | pages [5] -->
m

<!-- b000661 | furniture | pages [5] -->
m

<!-- b000662 | furniture | pages [5] -->
m

<!-- b000663 | furniture | pages [5] -->
m

<!-- b000664 | furniture | pages [5] -->
m

<!-- b000665 | furniture | pages [5] -->
m

<!-- b000666 | furniture | pages [5] -->
m

<!-- b000667 | furniture | pages [5] -->
m

<!-- b000668 | furniture | pages [5] -->
m

<!-- b000669 | furniture | pages [5] -->
m

<!-- b000670 | furniture | pages [5] -->
m

<!-- b000671 | furniture | pages [5] -->
m

<!-- b000672 | furniture | pages [5] -->
m

<!-- b000673 | furniture | pages [5] -->
m

<!-- b000674 | furniture | pages [5] -->
m

<!-- b000675 | furniture | pages [5] -->
m

<!-- b000676 | furniture | pages [5] -->
m

<!-- b000677 | furniture | pages [5] -->
m

<!-- b000678 | furniture | pages [5] -->
m

<!-- b000679 | furniture | pages [5] -->
m

<!-- b000680 | furniture | pages [5] -->
m

<!-- b000681 | furniture | pages [5] -->
m

<!-- b000682 | furniture | pages [5] -->
m

<!-- b000683 | furniture | pages [5] -->
m

<!-- b000684 | furniture | pages [5] -->
m

<!-- b000685 | furniture | pages [5] -->
m

<!-- b000686 | furniture | pages [5] -->
m

<!-- b000687 | furniture | pages [5] -->
m

<!-- b000688 | furniture | pages [5] -->
m

<!-- b000689 | furniture | pages [5] -->
m

<!-- b000690 | furniture | pages [5] -->
m

<!-- b000691 | furniture | pages [5] -->
m

<!-- b000692 | furniture | pages [5] -->
m

<!-- b000693 | furniture | pages [5] -->
m

<!-- b000694 | furniture | pages [5] -->
m

<!-- b000695 | furniture | pages [5] -->
m

<!-- b000696 | furniture | pages [5] -->
m

<!-- b000697 | furniture | pages [5] -->
m

<!-- b000698 | furniture | pages [5] -->
m

<!-- b000699 | furniture | pages [5] -->
m

<!-- b000700 | furniture | pages [5] -->
m

<!-- b000701 | furniture | pages [5] -->
m

<!-- b000702 | furniture | pages [5] -->
m

<!-- b000703 | furniture | pages [5] -->
m

<!-- b000704 | furniture | pages [5] -->
m

<!-- b000705 | furniture | pages [5] -->
m

<!-- b000706 | furniture | pages [5] -->
m

<!-- b000707 | furniture | pages [5] -->
m

<!-- b000708 | furniture | pages [5] -->
m

<!-- b000709 | furniture | pages [5] -->
m

<!-- b000710 | furniture | pages [5] -->
m

<!-- b000711 | furniture | pages [5] -->
m

<!-- b000712 | furniture | pages [5] -->
m

<!-- b000713 | furniture | pages [5] -->
m

<!-- b000714 | furniture | pages [5] -->
m

<!-- b000715 | furniture | pages [5] -->
m

<!-- b000716 | furniture | pages [5] -->
m

<!-- b000717 | furniture | pages [5] -->
m

<!-- b000718 | furniture | pages [5] -->
m

<!-- b000719 | furniture | pages [5] -->
m

<!-- b000720 | furniture | pages [5] -->
m

<!-- b000721 | furniture | pages [5] -->
m

<!-- b000722 | furniture | pages [5] -->
m

<!-- b000723 | furniture | pages [5] -->
m

<!-- b000724 | furniture | pages [5] -->
m

<!-- b000725 | furniture | pages [5] -->
m

<!-- b000726 | furniture | pages [5] -->
m

<!-- b000727 | furniture | pages [5] -->
m

<!-- b000728 | furniture | pages [5] -->
m

<!-- b000729 | furniture | pages [5] -->
m

<!-- b000730 | furniture | pages [5] -->
m

<!-- b000731 | furniture | pages [5] -->
m

<!-- b000732 | furniture | pages [5] -->
m

<!-- b000733 | furniture | pages [5] -->
m

<!-- b000734 | furniture | pages [5] -->
m

<!-- b000735 | furniture | pages [5] -->
m

<!-- b000736 | furniture | pages [5] -->
m

<!-- b000737 | furniture | pages [5] -->
m

<!-- b000738 | furniture | pages [5] -->
m

<!-- b000739 | furniture | pages [5] -->
m

<!-- b000740 | furniture | pages [5] -->
m

<!-- b000741 | furniture | pages [5] -->
m

<!-- b000742 | furniture | pages [5] -->
m

<!-- b000743 | furniture | pages [5] -->
m

<!-- b000744 | furniture | pages [5] -->
m

<!-- b000745 | furniture | pages [5] -->
m

<!-- b000746 | furniture | pages [5] -->
m

<!-- b000747 | furniture | pages [5] -->
m

<!-- b000748 | furniture | pages [5] -->
m

<!-- b000749 | furniture | pages [5] -->
m

<!-- b000750 | furniture | pages [5] -->
m

<!-- b000751 | furniture | pages [5] -->
m

<!-- b000752 | furniture | pages [5] -->
m

<!-- b000753 | furniture | pages [5] -->
m

<!-- b000754 | furniture | pages [5] -->
m

<!-- b000755 | furniture | pages [5] -->
m

<!-- b000756 | furniture | pages [5] -->
m

<!-- b000757 | furniture | pages [5] -->
m

<!-- b000758 | furniture | pages [5] -->
m

<!-- b000759 | furniture | pages [5] -->
m

<!-- b000760 | furniture | pages [5] -->
m

<!-- b000761 | furniture | pages [5] -->
m

<!-- b000762 | furniture | pages [5] -->
m

<!-- b000763 | furniture | pages [5] -->
m

<!-- b000764 | furniture | pages [5] -->
m

<!-- b000765 | furniture | pages [5] -->
m

<!-- b000766 | furniture | pages [5] -->
m

<!-- b000767 | furniture | pages [5] -->
m

<!-- b000768 | furniture | pages [5] -->
m

<!-- b000769 | furniture | pages [5] -->
m

<!-- b000770 | furniture | pages [5] -->
m

<!-- b000771 | furniture | pages [5] -->
m

<!-- b000772 | furniture | pages [5] -->
m

<!-- b000773 | furniture | pages [5] -->
m

<!-- b000774 | furniture | pages [5] -->
m

<!-- b000775 | furniture | pages [5] -->
m

<!-- b000776 | furniture | pages [5] -->
m

<!-- b000777 | furniture | pages [5] -->
m

<!-- b000778 | furniture | pages [5] -->
m

<!-- b000779 | furniture | pages [5] -->
m

<!-- b000780 | furniture | pages [5] -->
m

<!-- b000781 | furniture | pages [5] -->
m

<!-- b000782 | furniture | pages [5] -->
m

<!-- b000783 | furniture | pages [5] -->
m

<!-- b000784 | furniture | pages [5] -->
m

<!-- b000785 | furniture | pages [5] -->
m

<!-- b000786 | furniture | pages [5] -->
m

<!-- b000787 | furniture | pages [5] -->
m

<!-- b000788 | furniture | pages [5] -->
m

<!-- b000789 | furniture | pages [5] -->
m

<!-- b000790 | furniture | pages [5] -->
m

<!-- b000791 | furniture | pages [5] -->
m

<!-- b000792 | furniture | pages [5] -->
m

<!-- b000793 | furniture | pages [5] -->
m

<!-- b000794 | furniture | pages [5] -->
m

<!-- b000795 | furniture | pages [5] -->
m

<!-- b000796 | furniture | pages [6] -->
Team #2510185

<!-- b000797 | furniture | pages [6] -->
Page 6 of 24

<!-- b000798 | caption | pages [6] -->
Figure 3: Data processing

<!-- b000799 | prose | pages [6] -->
SummerOly_athletes

<!-- b000800 | prose | pages [6] -->
The data in the Team column of the SummerOly_athletes.csv file is misaligned or garbled.

<!-- b000801 | prose | pages [6] -->
We noticed that the 1906 Olympics were an intercalated Olympics (unofficial Olympics), and the results were not officially recognized by the International Olympic Committee (IOC). We ulti- mately decided not to use any data from 1906.

<!-- b000802 | prose | pages [6] -->
summerOly_hosts

<!-- b000803 | prose | pages [6] -->
The Host column in the summerOly_hosts.csv dataset contains both countries and cities. To obtain precise information on the host countries, we performed a column-splitting operation to separate the data accordingly.

<!-- b000804 | prose | pages [6] -->
summerOly_medal_counts

<!-- b000805 | prose | pages [6] -->
In the summerOly_medal_counts.csv dataset, the NOC column contains 72 instances of garbled data marked as "??". These entries were removed directly.

<!-- b000806 | prose | pages [6] -->
Additionally, inconsistencies in country names, such as "Great Britain" in this dataset versus "United Kingdom" in other tables, caused mismatches in host information and athlete data. To address this, we standardized the country names across all datasets.

<!-- b000807 | prose | pages [6] -->
summerOly_programs

<!-- b000808 | prose | pages [6] -->
The summerOly_programs.csv file contains missing values and garbled data marked as "?". Missing or garbled entries in columns A–C were corrected using online resources. For columns beyond E, garbled data were removed, and missing values were confirmed to be zeros based on Total events statistics.

<!-- b000809 | prose | pages [6] -->
Significant fluctuations in medal rankings for 1904, 1908, and 1984, likely due to geopolitical factors, led to the exclusion of these years from the analysis.

<!-- b000810 | prose | pages [6] -->
关注数学模型

<!-- b000811 | furniture | pages [6] -->
2

<!-- b000812 | furniture | pages [6] -->
MATHmodels

<!-- b000813 | furniture | pages [6] -->
获取更多资讯

<!-- b000814 | furniture | pages [7] -->
Team #2510185

<!-- b000815 | furniture | pages [7] -->
Page 7 of 24

<!-- b000816 | heading | pages [7] -->
Task 1: Medal Count Prediction Model

<!-- b000817 | prose | pages [7] -->
3

<!-- b000818 | prose | pages [7] -->
The flowchart for Task 1 is as follows:

<!-- b000819 | prose | pages [7] -->
Data processing

<!-- b000820 | prose | pages [7] -->
Data sorting

<!-- b000821 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000822 | prose | pages [7] -->
Linear

<!-- b000823 | prose | pages [7] -->
Feature engineering

<!-- b000824 | prose | pages [7] -->
regression

<!-- b000825 | prose | pages [7] -->
Model selection

<!-- b000826 | prose | pages [7] -->
XGBoost

<!-- b000827 | prose | pages [7] -->
Random

<!-- b000828 | prose | pages [7] -->
Medal Ranking prediction

<!-- b000829 | prose | pages [7] -->
forest

<!-- b000830 | prose | pages [7] -->
Task1.1: 2028 Medal Table Forecast

<!-- b000831 | prose | pages [7] -->
SVM

<!-- b000832 | prose | pages [7] -->
Adjust the training set

<!-- b000833 | prose | pages [7] -->
Random

<!-- b000834 | prose | pages [7] -->
Classifier model selection

<!-- b000835 | prose | pages [7] -->
forest

<!-- b000836 | prose | pages [7] -->
BP neural

<!-- b000837 | prose | pages [7] -->
Medal prediction probability

<!-- b000838 | prose | pages [7] -->
network

<!-- b000839 | prose | pages [7] -->
Task1.2: Prediction of the first medal

<!-- b000840 | prose | pages [7] -->
Data of types and numbers of events

<!-- b000841 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000842 | prose | pages [7] -->
Number of award-winning athletes

<!-- b000843 | prose | pages [7] -->
RF prediction and importance output

<!-- b000844 | prose | pages [7] -->
Task1.3: The Importance of Events to medals

<!-- b000845 | caption | pages [7] -->
Figure 4: Flowchart for Task 1

<!-- b000846 | prose | pages [7] -->
3.1 Feature Engineering

<!-- b000847 | prose | pages [7] -->
3.1.1 Athlete Potential Index (API)

<!-- b000848 | prose | pages [7] -->
Inspired by Ruiz and Mario’s (2024) research on the Olympic performance index of countries[5], we developed the Athlete Potential Index (API) based on athletes’ previous Olympic medal perfor- mances to describe athletes’ dynamic performance across Olympic Games. This potential index describes an athlete’s past performance and the results they can achieve in the current Olympic event, dynamically adjusted for each Olympic Games.

<!-- b000849 | prose | pages [7] -->
Note that the dataset only provides information about an athlete/team for the last few Olympic Games. Combining relevant papers and parameter tuning practices, we define the API as follows:

<!-- b000850 | prose | pages [7] -->
i X

<!-- b000851 | prose | pages [7] -->
i−j

<!-- b000852 | prose | pages [7] -->
1

<!-- b000853 | prose | pages [7] -->
PWM j ×

<!-- b000854 | prose | pages [7] -->
API =

<!-- b000855 | prose | pages [7] -->
j=1

<!-- b000856 | prose | pages [7] -->
(1)

<!-- b000857 | prose | pages [7] -->
2

<!-- b000858 | prose | pages [7] -->
where i represents the number of the next Olympic Games, and j represents the number of Olympic Games with recorded results.

<!-- b000859 | prose | pages [7] -->
PWM = 100 × NG + 90 × NS + 80 × NB + 60 × NM

<!-- b000860 | prose | pages [7] -->
where,

<!-- b000861 | prose | pages [7] -->
• NG represents the number of gold medals,

<!-- b000862 | prose | pages [7] -->
(2)

<!-- b000863 | furniture | pages [8] -->
Team #2510185

<!-- b000864 | prose | pages [8] -->
• NS represents the number of silver medals

<!-- b000865 | furniture | pages [8] -->
Page 8 of 24

<!-- b000866 | prose | pages [8] -->
• NB represents the number of bronze medals

<!-- b000867 | prose | pages [8] -->
• NM represents the number of events without medals

<!-- b000868 | prose | pages [8] -->
• If the athlete has never participated in a competition, their PWM is 0.

<!-- b000869 | prose | pages [8] -->
3.1.2 Participation Scale (PS)

<!-- b000870 | prose | pages [8] -->
The scale of a country’s participation in the Olympic Games is a factor that is often taken into account[3]. According to the number of athletes representing the country in the Olympic Games, we divide the participation scale into five levels, denoted by 1-5, as defined below:

<!-- b000871 | caption | pages [8] -->
Table 2: Participation Scale (PS) based on Athlete Number

<!-- b000872 | prose | pages [8] -->
Participation Scale (PS) Athlete Number

<!-- b000873 | prose | pages [8] -->
0-9 10-49 50-99 100-149 150 or more

<!-- b000874 | prose | pages [8] -->
3.2

<!-- b000875 | heading | pages [8] -->
Model Selection

<!-- b000876 | prose | pages [8] -->
1 2 3 4 5

<!-- b000877 | prose | pages [8] -->
After data processing and feature engineering, we obtain the following features:

<!-- b000878 | caption | pages [8] -->
Table 3: Feature Reference in Model 1

<!-- b000879 | heading | pages [8] -->
Symbol

<!-- b000880 | prose | pages [8] -->
Description

<!-- b000881 | prose | pages [8] -->
The year of the Olympic Games Year Number of Athletes N_A Number of Events N_E Average of API AAPI Scale of Participation (by NOC) PS Host advantage HS Number of Gold N_G Number of Silver N_S Number of Bronze N_B Total Total medals

<!-- b000882 | prose | pages [8] -->
We compiled the above characteristics of the Olympics for five countries: Japan, the United States, France, China, and Great Britain, and formed a dataset to train the model.

<!-- b000883 | prose | pages [8] -->
The correlation matrix for the current feature mapping is shown in Figure 5.

<!-- b000884 | prose | pages [8] -->
m

<!-- b000885 | prose | pages [8] -->
m

<!-- b000886 | prose | pages [8] -->
m

<!-- b000887 | prose | pages [8] -->
m

<!-- b000888 | prose | pages [8] -->
m

<!-- b000889 | prose | pages [8] -->
m

<!-- b000890 | prose | pages [8] -->
m

<!-- b000891 | prose | pages [8] -->
m

<!-- b000892 | prose | pages [8] -->
m

<!-- b000893 | prose | pages [8] -->
m

<!-- b000894 | prose | pages [8] -->
m

<!-- b000895 | prose | pages [8] -->
m

<!-- b000896 | prose | pages [8] -->
m

<!-- b000897 | prose | pages [8] -->
m

<!-- b000898 | prose | pages [8] -->
m

<!-- b000899 | prose | pages [8] -->
m

<!-- b000900 | prose | pages [8] -->
m

<!-- b000901 | prose | pages [8] -->
m

<!-- b000902 | prose | pages [8] -->
m

<!-- b000903 | prose | pages [8] -->
m

<!-- b000904 | prose | pages [8] -->
m

<!-- b000905 | prose | pages [8] -->
m

<!-- b000906 | prose | pages [8] -->
m

<!-- b000907 | prose | pages [8] -->
m

<!-- b000908 | prose | pages [8] -->
m

<!-- b000909 | prose | pages [8] -->
m

<!-- b000910 | prose | pages [8] -->
m

<!-- b000911 | prose | pages [8] -->
m

<!-- b000912 | prose | pages [8] -->
m

<!-- b000913 | prose | pages [8] -->
m

<!-- b000914 | prose | pages [8] -->
m

<!-- b000915 | prose | pages [8] -->
m

<!-- b000916 | prose | pages [8] -->
m

<!-- b000917 | prose | pages [8] -->
m

<!-- b000918 | prose | pages [8] -->
m

<!-- b000919 | prose | pages [8] -->
m

<!-- b000920 | prose | pages [8] -->
m

<!-- b000921 | prose | pages [8] -->
m

<!-- b000922 | prose | pages [8] -->
m

<!-- b000923 | prose | pages [8] -->
m

<!-- b000924 | prose | pages [8] -->
m

<!-- b000925 | prose | pages [8] -->
m

<!-- b000926 | prose | pages [8] -->
m

<!-- b000927 | prose | pages [8] -->
m

<!-- b000928 | prose | pages [8] -->
m

<!-- b000929 | prose | pages [8] -->
m

<!-- b000930 | prose | pages [8] -->
m

<!-- b000931 | prose | pages [8] -->
m

<!-- b000932 | prose | pages [8] -->
m

<!-- b000933 | prose | pages [8] -->
m

<!-- b000934 | prose | pages [8] -->
m

<!-- b000935 | prose | pages [8] -->
m

<!-- b000936 | prose | pages [8] -->
m

<!-- b000937 | prose | pages [8] -->
m

<!-- b000938 | prose | pages [8] -->
m

<!-- b000939 | prose | pages [8] -->
m

<!-- b000940 | prose | pages [8] -->
m

<!-- b000941 | prose | pages [8] -->
m

<!-- b000942 | prose | pages [8] -->
m

<!-- b000943 | prose | pages [8] -->
m

<!-- b000944 | prose | pages [8] -->
m

<!-- b000945 | prose | pages [8] -->
m

<!-- b000946 | prose | pages [8] -->
m

<!-- b000947 | prose | pages [8] -->
m

<!-- b000948 | prose | pages [8] -->
m

<!-- b000949 | prose | pages [8] -->
m

<!-- b000950 | prose | pages [8] -->
m

<!-- b000951 | prose | pages [8] -->
m

<!-- b000952 | prose | pages [8] -->
m

<!-- b000953 | prose | pages [8] -->
m

<!-- b000954 | prose | pages [8] -->
m

<!-- b000955 | prose | pages [8] -->
m

<!-- b000956 | prose | pages [8] -->
m

<!-- b000957 | prose | pages [8] -->
m

<!-- b000958 | prose | pages [8] -->
m

<!-- b000959 | prose | pages [8] -->
m

<!-- b000960 | prose | pages [8] -->
m

<!-- b000961 | prose | pages [8] -->
m

<!-- b000962 | prose | pages [8] -->
m

<!-- b000963 | prose | pages [8] -->
m

<!-- b000964 | prose | pages [8] -->
m

<!-- b000965 | prose | pages [8] -->
m

<!-- b000966 | prose | pages [8] -->
m

<!-- b000967 | prose | pages [8] -->
m

<!-- b000968 | prose | pages [8] -->
m

<!-- b000969 | prose | pages [8] -->
m

<!-- b000970 | prose | pages [8] -->
m

<!-- b000971 | prose | pages [8] -->
m

<!-- b000972 | prose | pages [8] -->
m

<!-- b000973 | prose | pages [8] -->
m

<!-- b000974 | prose | pages [8] -->
m

<!-- b000975 | prose | pages [8] -->
m

<!-- b000976 | prose | pages [8] -->
m

<!-- b000977 | prose | pages [8] -->
m

<!-- b000978 | prose | pages [8] -->
m

<!-- b000979 | prose | pages [8] -->
m

<!-- b000980 | prose | pages [8] -->
m

<!-- b000981 | prose | pages [8] -->
m

<!-- b000982 | prose | pages [8] -->
m

<!-- b000983 | prose | pages [8] -->
m

<!-- b000984 | prose | pages [8] -->
m

<!-- b000985 | prose | pages [8] -->
m

<!-- b000986 | prose | pages [8] -->
m

<!-- b000987 | prose | pages [8] -->
m

<!-- b000988 | prose | pages [8] -->
m

<!-- b000989 | prose | pages [8] -->
m

<!-- b000990 | prose | pages [8] -->
m

<!-- b000991 | prose | pages [8] -->
m

<!-- b000992 | prose | pages [8] -->
m

<!-- b000993 | prose | pages [8] -->
m

<!-- b000994 | prose | pages [8] -->
m

<!-- b000995 | prose | pages [8] -->
m

<!-- b000996 | prose | pages [8] -->
m

<!-- b000997 | prose | pages [8] -->
m

<!-- b000998 | prose | pages [8] -->
m

<!-- b000999 | prose | pages [8] -->
m

<!-- b001000 | prose | pages [8] -->
m

<!-- b001001 | prose | pages [8] -->
m

<!-- b001002 | prose | pages [8] -->
m

<!-- b001003 | prose | pages [8] -->
m

<!-- b001004 | prose | pages [8] -->
m

<!-- b001005 | prose | pages [8] -->
m

<!-- b001006 | prose | pages [8] -->
m

<!-- b001007 | prose | pages [8] -->
m

<!-- b001008 | prose | pages [8] -->
m

<!-- b001009 | prose | pages [8] -->
m

<!-- b001010 | prose | pages [8] -->
m

<!-- b001011 | prose | pages [8] -->
m

<!-- b001012 | prose | pages [8] -->
m

<!-- b001013 | prose | pages [8] -->
m

<!-- b001014 | prose | pages [8] -->
m

<!-- b001015 | prose | pages [8] -->
m

<!-- b001016 | prose | pages [8] -->
m

<!-- b001017 | prose | pages [8] -->
m

<!-- b001018 | prose | pages [8] -->
m

<!-- b001019 | prose | pages [8] -->
m

<!-- b001020 | prose | pages [8] -->
m

<!-- b001021 | prose | pages [8] -->
m

<!-- b001022 | prose | pages [8] -->
m

<!-- b001023 | prose | pages [8] -->
m

<!-- b001024 | prose | pages [8] -->
m

<!-- b001025 | prose | pages [8] -->
m

<!-- b001026 | prose | pages [8] -->
m

<!-- b001027 | prose | pages [8] -->
m

<!-- b001028 | prose | pages [8] -->
m

<!-- b001029 | prose | pages [8] -->
m

<!-- b001030 | prose | pages [8] -->
m

<!-- b001031 | prose | pages [8] -->
m

<!-- b001032 | prose | pages [8] -->
m

<!-- b001033 | prose | pages [8] -->
m

<!-- b001034 | prose | pages [8] -->
m

<!-- b001035 | prose | pages [8] -->
m

<!-- b001036 | prose | pages [8] -->
m

<!-- b001037 | prose | pages [8] -->
m

<!-- b001038 | prose | pages [8] -->
m

<!-- b001039 | prose | pages [8] -->
m

<!-- b001040 | prose | pages [8] -->
m

<!-- b001041 | prose | pages [8] -->
m

<!-- b001042 | prose | pages [8] -->
m

<!-- b001043 | prose | pages [8] -->
m

<!-- b001044 | prose | pages [8] -->
m

<!-- b001045 | prose | pages [8] -->
m

<!-- b001046 | prose | pages [8] -->
m

<!-- b001047 | prose | pages [8] -->
m

<!-- b001048 | prose | pages [8] -->
m

<!-- b001049 | prose | pages [8] -->
m

<!-- b001050 | prose | pages [8] -->
m

<!-- b001051 | prose | pages [8] -->
m

<!-- b001052 | prose | pages [8] -->
m

<!-- b001053 | prose | pages [8] -->
m

<!-- b001054 | prose | pages [8] -->
m

<!-- b001055 | prose | pages [8] -->
m

<!-- b001056 | prose | pages [8] -->
m

<!-- b001057 | prose | pages [8] -->
m

<!-- b001058 | prose | pages [8] -->
m

<!-- b001059 | prose | pages [8] -->
m

<!-- b001060 | prose | pages [8] -->
m

<!-- b001061 | prose | pages [8] -->
m

<!-- b001062 | prose | pages [8] -->
m

<!-- b001063 | prose | pages [8] -->
m

<!-- b001064 | prose | pages [8] -->
m

<!-- b001065 | prose | pages [8] -->
m

<!-- b001066 | prose | pages [8] -->
m

<!-- b001067 | prose | pages [8] -->
m

<!-- b001068 | prose | pages [8] -->
m

<!-- b001069 | prose | pages [8] -->
m

<!-- b001070 | prose | pages [8] -->
m

<!-- b001071 | prose | pages [8] -->
m

<!-- b001072 | prose | pages [8] -->
m

<!-- b001073 | prose | pages [8] -->
m

<!-- b001074 | prose | pages [8] -->
m

<!-- b001075 | prose | pages [8] -->
m

<!-- b001076 | prose | pages [8] -->
m

<!-- b001077 | prose | pages [8] -->
m

<!-- b001078 | prose | pages [8] -->
m

<!-- b001079 | prose | pages [8] -->
m

<!-- b001080 | prose | pages [8] -->
m

<!-- b001081 | prose | pages [8] -->
m

<!-- b001082 | prose | pages [8] -->
m

<!-- b001083 | prose | pages [8] -->
m

<!-- b001084 | prose | pages [8] -->
m

<!-- b001085 | prose | pages [8] -->
m

<!-- b001086 | prose | pages [8] -->
m

<!-- b001087 | prose | pages [8] -->
m

<!-- b001088 | prose | pages [8] -->
m

<!-- b001089 | prose | pages [8] -->
m

<!-- b001090 | prose | pages [8] -->
m

<!-- b001091 | prose | pages [8] -->
m

<!-- b001092 | prose | pages [8] -->
m

<!-- b001093 | prose | pages [8] -->
m

<!-- b001094 | prose | pages [8] -->
m

<!-- b001095 | prose | pages [8] -->
m

<!-- b001096 | prose | pages [8] -->
m

<!-- b001097 | prose | pages [8] -->
m

<!-- b001098 | prose | pages [8] -->
m

<!-- b001099 | prose | pages [8] -->
m

<!-- b001100 | prose | pages [8] -->
m

<!-- b001101 | prose | pages [8] -->
m

<!-- b001102 | prose | pages [8] -->
m

<!-- b001103 | prose | pages [8] -->
m

<!-- b001104 | prose | pages [8] -->
m

<!-- b001105 | prose | pages [8] -->
m

<!-- b001106 | prose | pages [8] -->
m

<!-- b001107 | prose | pages [8] -->
m

<!-- b001108 | prose | pages [8] -->
m

<!-- b001109 | prose | pages [8] -->
m

<!-- b001110 | prose | pages [8] -->
m

<!-- b001111 | prose | pages [8] -->
m

<!-- b001112 | prose | pages [8] -->
m

<!-- b001113 | prose | pages [8] -->
m

<!-- b001114 | prose | pages [8] -->
m

<!-- b001115 | prose | pages [8] -->
m

<!-- b001116 | prose | pages [8] -->
m

<!-- b001117 | prose | pages [8] -->
m

<!-- b001118 | prose | pages [8] -->
m

<!-- b001119 | prose | pages [8] -->
m

<!-- b001120 | prose | pages [8] -->
m

<!-- b001121 | prose | pages [8] -->
m

<!-- b001122 | prose | pages [8] -->
m

<!-- b001123 | prose | pages [8] -->
m

<!-- b001124 | prose | pages [8] -->
m

<!-- b001125 | prose | pages [8] -->
m

<!-- b001126 | prose | pages [8] -->
m

<!-- b001127 | prose | pages [8] -->
m

<!-- b001128 | prose | pages [8] -->
m

<!-- b001129 | prose | pages [8] -->
m

<!-- b001130 | prose | pages [8] -->
m

<!-- b001131 | prose | pages [8] -->
m

<!-- b001132 | prose | pages [8] -->
m

<!-- b001133 | prose | pages [8] -->
m

<!-- b001134 | prose | pages [8] -->
m

<!-- b001135 | prose | pages [8] -->
m

<!-- b001136 | prose | pages [8] -->
m

<!-- b001137 | prose | pages [8] -->
m

<!-- b001138 | prose | pages [8] -->
m

<!-- b001139 | prose | pages [8] -->
m

<!-- b001140 | prose | pages [8] -->
m

<!-- b001141 | prose | pages [8] -->
m

<!-- b001142 | prose | pages [8] -->
m

<!-- b001143 | prose | pages [8] -->
m

<!-- b001144 | prose | pages [8] -->
m

<!-- b001145 | prose | pages [8] -->
m

<!-- b001146 | prose | pages [8] -->
m

<!-- b001147 | prose | pages [8] -->
m

<!-- b001148 | prose | pages [8] -->
m

<!-- b001149 | prose | pages [8] -->
m

<!-- b001150 | prose | pages [8] -->
m

<!-- b001151 | prose | pages [8] -->
m

<!-- b001152 | prose | pages [8] -->
m

<!-- b001153 | prose | pages [8] -->
m

<!-- b001154 | prose | pages [8] -->
m

<!-- b001155 | prose | pages [8] -->
m

<!-- b001156 | prose | pages [8] -->
m

<!-- b001157 | prose | pages [8] -->
m

<!-- b001158 | prose | pages [8] -->
m

<!-- b001159 | prose | pages [8] -->
m

<!-- b001160 | prose | pages [8] -->
m

<!-- b001161 | prose | pages [8] -->
m

<!-- b001162 | prose | pages [8] -->
m

<!-- b001163 | prose | pages [8] -->
m

<!-- b001164 | prose | pages [8] -->
m

<!-- b001165 | prose | pages [8] -->
m

<!-- b001166 | prose | pages [8] -->
m

<!-- b001167 | prose | pages [8] -->
m

<!-- b001168 | prose | pages [8] -->
m

<!-- b001169 | prose | pages [8] -->
m

<!-- b001170 | prose | pages [8] -->
m

<!-- b001171 | prose | pages [8] -->
m

<!-- b001172 | prose | pages [8] -->
m

<!-- b001173 | prose | pages [8] -->
m

<!-- b001174 | prose | pages [8] -->
m

<!-- b001175 | prose | pages [8] -->
m

<!-- b001176 | prose | pages [8] -->
m

<!-- b001177 | prose | pages [8] -->
m

<!-- b001178 | prose | pages [8] -->
m

<!-- b001179 | prose | pages [8] -->
m

<!-- b001180 | prose | pages [8] -->
m

<!-- b001181 | prose | pages [8] -->
m

<!-- b001182 | prose | pages [8] -->
m

<!-- b001183 | prose | pages [8] -->
m

<!-- b001184 | prose | pages [8] -->
m

<!-- b001185 | prose | pages [8] -->
m

<!-- b001186 | prose | pages [8] -->
m

<!-- b001187 | prose | pages [8] -->
m

<!-- b001188 | prose | pages [8] -->
m

<!-- b001189 | prose | pages [8] -->
m

<!-- b001190 | prose | pages [8] -->
m

<!-- b001191 | prose | pages [8] -->
m

<!-- b001192 | prose | pages [8] -->
m

<!-- b001193 | prose | pages [8] -->
m

<!-- b001194 | prose | pages [8] -->
m

<!-- b001195 | prose | pages [8] -->
m

<!-- b001196 | prose | pages [8] -->
m

<!-- b001197 | prose | pages [8] -->
m

<!-- b001198 | prose | pages [8] -->
m

<!-- b001199 | prose | pages [8] -->
m

<!-- b001200 | prose | pages [8] -->
m

<!-- b001201 | prose | pages [8] -->
m

<!-- b001202 | prose | pages [8] -->
m

<!-- b001203 | prose | pages [8] -->
m

<!-- b001204 | prose | pages [8] -->
m

<!-- b001205 | prose | pages [8] -->
m

<!-- b001206 | prose | pages [8] -->
m

<!-- b001207 | prose | pages [8] -->
m

<!-- b001208 | prose | pages [8] -->
m

<!-- b001209 | prose | pages [8] -->
m

<!-- b001210 | prose | pages [8] -->
m

<!-- b001211 | prose | pages [8] -->
m

<!-- b001212 | prose | pages [8] -->
m

<!-- b001213 | prose | pages [8] -->
m

<!-- b001214 | prose | pages [8] -->
m

<!-- b001215 | prose | pages [8] -->
m

<!-- b001216 | prose | pages [8] -->
m

<!-- b001217 | prose | pages [8] -->
m

<!-- b001218 | prose | pages [8] -->
m

<!-- b001219 | prose | pages [8] -->
m

<!-- b001220 | prose | pages [8] -->
m

<!-- b001221 | prose | pages [8] -->
m

<!-- b001222 | prose | pages [8] -->
m

<!-- b001223 | prose | pages [8] -->
m

<!-- b001224 | prose | pages [8] -->
m

<!-- b001225 | prose | pages [8] -->
m

<!-- b001226 | prose | pages [8] -->
m

<!-- b001227 | prose | pages [8] -->
m

<!-- b001228 | prose | pages [8] -->
m

<!-- b001229 | prose | pages [8] -->
m

<!-- b001230 | prose | pages [8] -->
m

<!-- b001231 | prose | pages [8] -->
m

<!-- b001232 | prose | pages [8] -->
m

<!-- b001233 | prose | pages [8] -->
m

<!-- b001234 | prose | pages [8] -->
m

<!-- b001235 | prose | pages [8] -->
m

<!-- b001236 | prose | pages [8] -->
m

<!-- b001237 | prose | pages [8] -->
m

<!-- b001238 | prose | pages [8] -->
m

<!-- b001239 | prose | pages [8] -->
m

<!-- b001240 | prose | pages [8] -->
m

<!-- b001241 | prose | pages [8] -->
m

<!-- b001242 | prose | pages [8] -->
m

<!-- b001243 | prose | pages [8] -->
m

<!-- b001244 | prose | pages [8] -->
m

<!-- b001245 | prose | pages [8] -->
m

<!-- b001246 | prose | pages [8] -->
m

<!-- b001247 | prose | pages [8] -->
m

<!-- b001248 | prose | pages [8] -->
m

<!-- b001249 | prose | pages [8] -->
m

<!-- b001250 | prose | pages [8] -->
m

<!-- b001251 | prose | pages [8] -->
m

<!-- b001252 | prose | pages [8] -->
m

<!-- b001253 | prose | pages [8] -->
m

<!-- b001254 | prose | pages [8] -->
m

<!-- b001255 | furniture | pages [8] -->
m

<!-- b001256 | furniture | pages [8] -->
m

<!-- b001257 | furniture | pages [8] -->
m

<!-- b001258 | furniture | pages [8] -->
m

<!-- b001259 | furniture | pages [8] -->
m

<!-- b001260 | furniture | pages [8] -->
m

<!-- b001261 | furniture | pages [8] -->
m

<!-- b001262 | furniture | pages [8] -->
m

<!-- b001263 | furniture | pages [8] -->
m

<!-- b001264 | furniture | pages [8] -->
m

<!-- b001265 | furniture | pages [8] -->
m

<!-- b001266 | furniture | pages [8] -->
m

<!-- b001267 | furniture | pages [8] -->
m

<!-- b001268 | furniture | pages [8] -->
m

<!-- b001269 | furniture | pages [8] -->
m

<!-- b001270 | furniture | pages [8] -->
m

<!-- b001271 | furniture | pages [8] -->
m

<!-- b001272 | furniture | pages [8] -->
m

<!-- b001273 | furniture | pages [8] -->
m

<!-- b001274 | furniture | pages [8] -->
m

<!-- b001275 | furniture | pages [8] -->
m

<!-- b001276 | furniture | pages [8] -->
m

<!-- b001277 | furniture | pages [8] -->
m

<!-- b001278 | furniture | pages [8] -->
m

<!-- b001279 | furniture | pages [8] -->
m

<!-- b001280 | furniture | pages [8] -->
m

<!-- b001281 | furniture | pages [8] -->
m

<!-- b001282 | furniture | pages [8] -->
m

<!-- b001283 | furniture | pages [8] -->
m

<!-- b001284 | furniture | pages [8] -->
m

<!-- b001285 | furniture | pages [8] -->
m

<!-- b001286 | furniture | pages [8] -->
m

<!-- b001287 | furniture | pages [8] -->
m

<!-- b001288 | furniture | pages [8] -->
m

<!-- b001289 | furniture | pages [8] -->
m

<!-- b001290 | furniture | pages [8] -->
m

<!-- b001291 | furniture | pages [8] -->
m

<!-- b001292 | furniture | pages [8] -->
m

<!-- b001293 | furniture | pages [8] -->
m

<!-- b001294 | furniture | pages [8] -->
m

<!-- b001295 | furniture | pages [8] -->
m

<!-- b001296 | furniture | pages [8] -->
m

<!-- b001297 | furniture | pages [8] -->
m

<!-- b001298 | furniture | pages [8] -->
m

<!-- b001299 | furniture | pages [8] -->
m

<!-- b001300 | furniture | pages [8] -->
m

<!-- b001301 | furniture | pages [8] -->
m

<!-- b001302 | furniture | pages [8] -->
m

<!-- b001303 | furniture | pages [8] -->
m

<!-- b001304 | furniture | pages [8] -->
m

<!-- b001305 | furniture | pages [8] -->
m

<!-- b001306 | furniture | pages [8] -->
m

<!-- b001307 | furniture | pages [8] -->
m

<!-- b001308 | furniture | pages [8] -->
m

<!-- b001309 | furniture | pages [8] -->
m

<!-- b001310 | furniture | pages [8] -->
m

<!-- b001311 | furniture | pages [8] -->
m

<!-- b001312 | furniture | pages [8] -->
m

<!-- b001313 | furniture | pages [8] -->
m

<!-- b001314 | furniture | pages [8] -->
m

<!-- b001315 | furniture | pages [8] -->
m

<!-- b001316 | furniture | pages [8] -->
m

<!-- b001317 | furniture | pages [8] -->
m

<!-- b001318 | furniture | pages [8] -->
m

<!-- b001319 | furniture | pages [8] -->
m

<!-- b001320 | furniture | pages [8] -->
m

<!-- b001321 | furniture | pages [8] -->
m

<!-- b001322 | furniture | pages [8] -->
m

<!-- b001323 | furniture | pages [8] -->
m

<!-- b001324 | furniture | pages [8] -->
m

<!-- b001325 | furniture | pages [8] -->
m

<!-- b001326 | furniture | pages [8] -->
m

<!-- b001327 | furniture | pages [8] -->
m

<!-- b001328 | furniture | pages [8] -->
m

<!-- b001329 | furniture | pages [8] -->
m

<!-- b001330 | furniture | pages [8] -->
m

<!-- b001331 | furniture | pages [8] -->
m

<!-- b001332 | furniture | pages [8] -->
m

<!-- b001333 | furniture | pages [8] -->
m

<!-- b001334 | furniture | pages [8] -->
m

<!-- b001335 | furniture | pages [8] -->
m

<!-- b001336 | furniture | pages [8] -->
m

<!-- b001337 | furniture | pages [8] -->
m

<!-- b001338 | furniture | pages [8] -->
m

<!-- b001339 | furniture | pages [8] -->
m

<!-- b001340 | furniture | pages [8] -->
m

<!-- b001341 | furniture | pages [8] -->
m

<!-- b001342 | furniture | pages [8] -->
m

<!-- b001343 | furniture | pages [8] -->
m

<!-- b001344 | furniture | pages [8] -->
m

<!-- b001345 | furniture | pages [8] -->
m

<!-- b001346 | furniture | pages [8] -->
m

<!-- b001347 | furniture | pages [8] -->
m

<!-- b001348 | furniture | pages [8] -->
m

<!-- b001349 | furniture | pages [8] -->
m

<!-- b001350 | furniture | pages [8] -->
m

<!-- b001351 | furniture | pages [8] -->
m

<!-- b001352 | furniture | pages [8] -->
m

<!-- b001353 | furniture | pages [8] -->
m

<!-- b001354 | furniture | pages [8] -->
m

<!-- b001355 | furniture | pages [8] -->
m

<!-- b001356 | furniture | pages [8] -->
m

<!-- b001357 | furniture | pages [8] -->
m

<!-- b001358 | furniture | pages [8] -->
m

<!-- b001359 | furniture | pages [8] -->
m

<!-- b001360 | furniture | pages [8] -->
m

<!-- b001361 | furniture | pages [8] -->
m

<!-- b001362 | furniture | pages [8] -->
m

<!-- b001363 | furniture | pages [8] -->
m

<!-- b001364 | furniture | pages [8] -->
m

<!-- b001365 | furniture | pages [8] -->
m

<!-- b001366 | furniture | pages [8] -->
m

<!-- b001367 | furniture | pages [8] -->
m

<!-- b001368 | furniture | pages [8] -->
m

<!-- b001369 | furniture | pages [8] -->
m

<!-- b001370 | furniture | pages [8] -->
m

<!-- b001371 | furniture | pages [8] -->
m

<!-- b001372 | furniture | pages [8] -->
m

<!-- b001373 | furniture | pages [8] -->
m

<!-- b001374 | furniture | pages [8] -->
m

<!-- b001375 | furniture | pages [8] -->
m

<!-- b001376 | furniture | pages [8] -->
m

<!-- b001377 | furniture | pages [8] -->
m

<!-- b001378 | furniture | pages [8] -->
m

<!-- b001379 | furniture | pages [8] -->
m

<!-- b001380 | furniture | pages [8] -->
m

<!-- b001381 | furniture | pages [8] -->
m

<!-- b001382 | furniture | pages [8] -->
m

<!-- b001383 | furniture | pages [8] -->
m

<!-- b001384 | furniture | pages [8] -->
m

<!-- b001385 | furniture | pages [8] -->
m

<!-- b001386 | furniture | pages [8] -->
m

<!-- b001387 | furniture | pages [8] -->
m

<!-- b001388 | furniture | pages [8] -->
m

<!-- b001389 | furniture | pages [8] -->
m

<!-- b001390 | furniture | pages [8] -->
m

<!-- b001391 | furniture | pages [8] -->
m

<!-- b001392 | furniture | pages [8] -->
m

<!-- b001393 | furniture | pages [8] -->
m

<!-- b001394 | furniture | pages [8] -->
m

<!-- b001395 | furniture | pages [8] -->
m

<!-- b001396 | furniture | pages [8] -->
m

<!-- b001397 | furniture | pages [8] -->
m

<!-- b001398 | furniture | pages [8] -->
m

<!-- b001399 | furniture | pages [8] -->
m

<!-- b001400 | furniture | pages [8] -->
m

<!-- b001401 | furniture | pages [8] -->
m

<!-- b001402 | furniture | pages [8] -->
m

<!-- b001403 | furniture | pages [8] -->
m

<!-- b001404 | furniture | pages [8] -->
m

<!-- b001405 | furniture | pages [8] -->
m

<!-- b001406 | furniture | pages [8] -->
m

<!-- b001407 | furniture | pages [8] -->
m

<!-- b001408 | furniture | pages [8] -->
m

<!-- b001409 | furniture | pages [8] -->
m

<!-- b001410 | furniture | pages [8] -->
m

<!-- b001411 | furniture | pages [8] -->
m

<!-- b001412 | furniture | pages [8] -->
m

<!-- b001413 | furniture | pages [8] -->
m

<!-- b001414 | furniture | pages [8] -->
m

<!-- b001415 | furniture | pages [8] -->
m

<!-- b001416 | furniture | pages [8] -->
m

<!-- b001417 | furniture | pages [8] -->
m

<!-- b001418 | furniture | pages [8] -->
m

<!-- b001419 | furniture | pages [8] -->
m

<!-- b001420 | furniture | pages [8] -->
m

<!-- b001421 | furniture | pages [8] -->
m

<!-- b001422 | furniture | pages [8] -->
m

<!-- b001423 | furniture | pages [8] -->
m

<!-- b001424 | furniture | pages [8] -->
m

<!-- b001425 | furniture | pages [8] -->
m

<!-- b001426 | furniture | pages [8] -->
m

<!-- b001427 | furniture | pages [8] -->
m

<!-- b001428 | furniture | pages [8] -->
m

<!-- b001429 | furniture | pages [8] -->
m

<!-- b001430 | furniture | pages [8] -->
m

<!-- b001431 | furniture | pages [8] -->
m

<!-- b001432 | furniture | pages [8] -->
m

<!-- b001433 | furniture | pages [8] -->
m

<!-- b001434 | furniture | pages [8] -->
m

<!-- b001435 | furniture | pages [8] -->
m

<!-- b001436 | furniture | pages [8] -->
m

<!-- b001437 | furniture | pages [8] -->
m

<!-- b001438 | furniture | pages [8] -->
m

<!-- b001439 | furniture | pages [8] -->
m

<!-- b001440 | furniture | pages [8] -->
m

<!-- b001441 | furniture | pages [8] -->
m

<!-- b001442 | furniture | pages [8] -->
m

<!-- b001443 | furniture | pages [8] -->
m

<!-- b001444 | furniture | pages [8] -->
m

<!-- b001445 | furniture | pages [8] -->
m

<!-- b001446 | furniture | pages [8] -->
m

<!-- b001447 | furniture | pages [8] -->
m

<!-- b001448 | furniture | pages [8] -->
m

<!-- b001449 | furniture | pages [8] -->
m

<!-- b001450 | furniture | pages [8] -->
m

<!-- b001451 | furniture | pages [8] -->
m

<!-- b001452 | furniture | pages [8] -->
m

<!-- b001453 | furniture | pages [8] -->
m

<!-- b001454 | furniture | pages [8] -->
m

<!-- b001455 | furniture | pages [8] -->
m

<!-- b001456 | furniture | pages [8] -->
m

<!-- b001457 | furniture | pages [8] -->
m

<!-- b001458 | furniture | pages [8] -->
m

<!-- b001459 | furniture | pages [8] -->
m

<!-- b001460 | furniture | pages [8] -->
m

<!-- b001461 | furniture | pages [8] -->
m

<!-- b001462 | furniture | pages [8] -->
m

<!-- b001463 | furniture | pages [8] -->
m

<!-- b001464 | furniture | pages [8] -->
m

<!-- b001465 | furniture | pages [8] -->
m

<!-- b001466 | furniture | pages [8] -->
m

<!-- b001467 | furniture | pages [8] -->
m

<!-- b001468 | furniture | pages [8] -->
m

<!-- b001469 | furniture | pages [8] -->
m

<!-- b001470 | furniture | pages [8] -->
m

<!-- b001471 | furniture | pages [8] -->
m

<!-- b001472 | furniture | pages [8] -->
m

<!-- b001473 | furniture | pages [8] -->
m

<!-- b001474 | furniture | pages [8] -->
m

<!-- b001475 | furniture | pages [8] -->
m

<!-- b001476 | furniture | pages [8] -->
m

<!-- b001477 | furniture | pages [8] -->
m

<!-- b001478 | furniture | pages [8] -->
m

<!-- b001479 | furniture | pages [8] -->
m

<!-- b001480 | furniture | pages [8] -->
m

<!-- b001481 | furniture | pages [8] -->
m

<!-- b001482 | furniture | pages [8] -->
m

<!-- b001483 | furniture | pages [8] -->
m

<!-- b001484 | furniture | pages [8] -->
m

<!-- b001485 | furniture | pages [8] -->
m

<!-- b001486 | furniture | pages [8] -->
m

<!-- b001487 | furniture | pages [8] -->
m

<!-- b001488 | furniture | pages [8] -->
m

<!-- b001489 | furniture | pages [8] -->
m

<!-- b001490 | furniture | pages [8] -->
m

<!-- b001491 | furniture | pages [8] -->
m

<!-- b001492 | furniture | pages [8] -->
m

<!-- b001493 | furniture | pages [8] -->
m

<!-- b001494 | furniture | pages [8] -->
m

<!-- b001495 | furniture | pages [8] -->
m

<!-- b001496 | furniture | pages [8] -->
m

<!-- b001497 | furniture | pages [8] -->
m

<!-- b001498 | furniture | pages [8] -->
m

<!-- b001499 | furniture | pages [8] -->
m

<!-- b001500 | furniture | pages [8] -->
m

<!-- b001501 | furniture | pages [8] -->
m

<!-- b001502 | furniture | pages [8] -->
m

<!-- b001503 | furniture | pages [8] -->
m

<!-- b001504 | furniture | pages [8] -->
m

<!-- b001505 | furniture | pages [8] -->
m

<!-- b001506 | furniture | pages [8] -->
m

<!-- b001507 | furniture | pages [8] -->
m

<!-- b001508 | furniture | pages [8] -->
m

<!-- b001509 | furniture | pages [8] -->
m

<!-- b001510 | furniture | pages [8] -->
m

<!-- b001511 | furniture | pages [8] -->
m

<!-- b001512 | furniture | pages [8] -->
m

<!-- b001513 | furniture | pages [8] -->
m

<!-- b001514 | furniture | pages [8] -->
m

<!-- b001515 | furniture | pages [8] -->
m

<!-- b001516 | furniture | pages [8] -->
m

<!-- b001517 | furniture | pages [8] -->
m

<!-- b001518 | furniture | pages [8] -->
m

<!-- b001519 | furniture | pages [8] -->
m

<!-- b001520 | furniture | pages [8] -->
m

<!-- b001521 | furniture | pages [8] -->
m

<!-- b001522 | furniture | pages [8] -->
m

<!-- b001523 | furniture | pages [8] -->
m

<!-- b001524 | furniture | pages [8] -->
m

<!-- b001525 | furniture | pages [8] -->
m

<!-- b001526 | furniture | pages [8] -->
m

<!-- b001527 | furniture | pages [8] -->
m

<!-- b001528 | furniture | pages [8] -->
m

<!-- b001529 | furniture | pages [8] -->
m

<!-- b001530 | furniture | pages [8] -->
m

<!-- b001531 | furniture | pages [8] -->
m

<!-- b001532 | furniture | pages [8] -->
m

<!-- b001533 | furniture | pages [8] -->
m

<!-- b001534 | furniture | pages [8] -->
m

<!-- b001535 | furniture | pages [8] -->
m

<!-- b001536 | furniture | pages [8] -->
m

<!-- b001537 | furniture | pages [8] -->
m

<!-- b001538 | furniture | pages [8] -->
m

<!-- b001539 | furniture | pages [8] -->
m

<!-- b001540 | furniture | pages [8] -->
m

<!-- b001541 | furniture | pages [8] -->
m

<!-- b001542 | furniture | pages [8] -->
m

<!-- b001543 | furniture | pages [8] -->
m

<!-- b001544 | furniture | pages [8] -->
m

<!-- b001545 | furniture | pages [8] -->
m

<!-- b001546 | furniture | pages [8] -->
m

<!-- b001547 | furniture | pages [8] -->
m

<!-- b001548 | furniture | pages [8] -->
m

<!-- b001549 | furniture | pages [8] -->
m

<!-- b001550 | furniture | pages [8] -->
m

<!-- b001551 | furniture | pages [8] -->
m

<!-- b001552 | furniture | pages [8] -->
m

<!-- b001553 | furniture | pages [8] -->
m

<!-- b001554 | furniture | pages [8] -->
m

<!-- b001555 | furniture | pages [8] -->
m

<!-- b001556 | furniture | pages [8] -->
m

<!-- b001557 | furniture | pages [8] -->
m

<!-- b001558 | furniture | pages [8] -->
m

<!-- b001559 | furniture | pages [8] -->
m

<!-- b001560 | furniture | pages [8] -->
m

<!-- b001561 | furniture | pages [8] -->
m

<!-- b001562 | furniture | pages [8] -->
m

<!-- b001563 | furniture | pages [8] -->
m

<!-- b001564 | furniture | pages [8] -->
m

<!-- b001565 | furniture | pages [8] -->
m

<!-- b001566 | furniture | pages [8] -->
m

<!-- b001567 | furniture | pages [8] -->
m

<!-- b001568 | furniture | pages [8] -->
m

<!-- b001569 | furniture | pages [8] -->
m

<!-- b001570 | furniture | pages [8] -->
m

<!-- b001571 | prose | pages [8] -->
关注数学模型

<!-- b001572 | furniture | pages [8] -->
2

<!-- b001573 | furniture | pages [8] -->
MATHmodels

<!-- b001574 | furniture | pages [8] -->
获取更多资讯

<!-- b001575 | furniture | pages [9] -->
Team #2510185

<!-- b001576 | furniture | pages [9] -->
Page 9 of 24

<!-- b001577 | prose | pages [9] -->
微信公众号：数学模型

<!-- b001578 | prose | pages [9] -->
微信号：MATHmodels

<!-- b001579 | caption | pages [9] -->
Figure 5: Correlation matrix of the characteristics of model 1

<!-- b001580 | prose | pages [9] -->
As can be seen from the image, for N_G, N_S, N_B, and Total, the six selected features are all correlated to some extent. Therefore, we select all of the above features to train the model.

<!-- b001581 | prose | pages [9] -->
We evaluated multiple models to select the best for prediction. Linear regression is chosen for its simplicity and interpretability. Random forests are selected for their strong predictive power and interpretability. XGBoost, known for its excellent performance, is also used for prediction.

<!-- b001582 | prose | pages [9] -->
For both random forests and XGBoost, we use a grid search to determine the best hyperpa- rameters. A total of 27 combinations of three hyperparameters are set for random forests and 54 combinations for XGBoost. The optimal parameters are:

<!-- b001583 | caption | pages [9] -->
Table 4: Random Forests Hyperparameters

<!-- b001584 | prose | pages [9] -->
max_depth n_estimators

<!-- b001585 | prose | pages [9] -->
180 10

<!-- b001586 | prose | pages [9] -->
min_samples_split

<!-- b001587 | prose | pages [9] -->
4

<!-- b001588 | caption | pages [9] -->
Table 5: XGBoost Hyperparameters

<!-- b001589 | prose | pages [9] -->
subsample eta max_depth

<!-- b001590 | prose | pages [9] -->
0.1 6 0.8

<!-- b001591 | prose | pages [9] -->
colsample_bytree

<!-- b001592 | prose | pages [9] -->
0.8

<!-- b001593 | prose | pages [9] -->
The fitting results of the three models’ predictions for 70% of the training set and 30% of the test set are shown in Figure 6.

<!-- b001594 | furniture | pages [11] -->
Team #2510185

<!-- b001595 | furniture | pages [11] -->
Page 11 of 24

<!-- b001596 | prose | pages [11] -->
微信公众号：数学模型

<!-- b001597 | prose | pages [11] -->
Task 1.1: 2028 Olympic VMT Prediction 3.3

<!-- b001598 | prose | pages [11] -->
3.3.1

<!-- b001599 | heading | pages [11] -->
Grid SearchCV - Random Forest Model

<!-- b001600 | prose | pages [11] -->
Combining the data from the medal tables of recent Olympic Games, we select the top-ranked countries to make predictions for. For the medal table predictions, we will only predict medals for the major award-winning countries mentioned above. Note that Russia did not participate in the Olympics. The flowchart for Task 1.1 is as follows:

<!-- b001601 | prose | pages [11] -->
 

<!-- b001602 | prose | pages [11] -->
Accuracy

<!-- b001603 | prose | pages [11] -->
微信号：MATHmodels

<!-- b001604 | prose | pages [11] -->
Original Sample

<!-- b001605 | prose | pages [11] -->
Result 2 Result 1

<!-- b001606 | prose | pages [11] -->


<!-- b001607 | prose | pages [11] -->
Booststrap Sample ×300

<!-- b001608 | prose | pages [11] -->
NOC N_G L_G U_G Total

<!-- b001609 | prose | pages [11] -->
USA 50 137 43.47 55.22

<!-- b001610 | prose | pages [11] -->
…… Result n

<!-- b001611 | prose | pages [11] -->
CHN 39 90 30.84 42.18

<!-- b001612 | prose | pages [11] -->
GBR 20 63 13.40 28.54

<!-- b001613 | prose | pages [11] -->
95% Confidence

<!-- b001614 | prose | pages [11] -->
Best parameters

<!-- b001615 | prose | pages [11] -->
n_estimators max_depth min_samples_split

<!-- b001616 | prose | pages [11] -->
2.5%

<!-- b001617 | prose | pages [11] -->
180 10 4

<!-- b001618 | prose | pages [11] -->


<!-- b001619 | prose | pages [11] -->
DATASET

<!-- b001620 | prose | pages [11] -->
……

<!-- b001621 | prose | pages [11] -->
DECISION TREE 1

<!-- b001622 | prose | pages [11] -->
JPN 17 43 11.28 23.06

<!-- b001623 | prose | pages [11] -->
97.5%

<!-- b001624 | prose | pages [11] -->
AUS 17 50 10.66 32.53

<!-- b001625 | prose | pages [11] -->
FRA 15 62 11.52 27.28

<!-- b001626 | prose | pages [11] -->
GER 14 43 8.52 21.43

<!-- b001627 | prose | pages [11] -->
NED 13 33 6.64 21.32 … … … … …

<!-- b001628 | prose | pages [11] -->
DECISION TREE N DECISION TREE 2

<!-- b001629 | heading | pages [11] -->
RESULT 1

<!-- b001630 | heading | pages [11] -->
RESULT 2

<!-- b001631 | prose | pages [11] -->
VOTING

<!-- b001632 | heading | pages [11] -->
RESULT

<!-- b001633 | heading | pages [11] -->
RESULT N

<!-- b001634 | heading | pages [11] -->
RESULT N

<!-- b001635 | caption | pages [11] -->
Figure 7: Flowchart for Task 1.1

<!-- b001636 | prose | pages [11] -->
3.3.2

<!-- b001637 | heading | pages [11] -->
Prediction Results

<!-- b001638 | prose | pages [11] -->
The random forest model is used to predict the medal rankings of each country in the 2028 Los Angeles Summer Olympics. We assume that the number of participants (N_A) and the number of events (N_E) are increased in proportion to the additional events in 2028. The prediction results are shown in Table 7:

<!-- b001639 | prose | pages [11] -->
The medal rankings are based on the predicted counts of gold, silver, and bronze medals in descending order. Integer values are rounded using the "round half to even" method. Due to space constraints, only a selection of countries is displayed in the medal table, while many others are not shown. However, the same methodology is consistently applied to all countries in the rankings.

<!-- b001640 | prose | pages [11] -->
Analyzing the forecast results, we can conclude:

<!-- b001641 | prose | pages [11] -->
• Countries most likely to increase the number of medals: the United States.

<!-- b001642 | prose | pages [11] -->
• Countries most likely to decrease the number of medals: South Korea.

<!-- b001643 | furniture | pages [12] -->
Team #2510185

<!-- b001644 | furniture | pages [12] -->
Page 12 of 24

<!-- b001645 | caption | pages [12] -->
Table 7: Los Angeles Olympics (2028) Virtual Medal Table

<!-- b001646 | prose | pages [12] -->
m

<!-- b001647 | prose | pages [12] -->
m

<!-- b001648 | prose | pages [12] -->
m

<!-- b001649 | prose | pages [12] -->
m

<!-- b001650 | prose | pages [12] -->
m

<!-- b001651 | prose | pages [12] -->
m

<!-- b001652 | prose | pages [12] -->
m

<!-- b001653 | prose | pages [12] -->
m

<!-- b001654 | prose | pages [12] -->
m

<!-- b001655 | prose | pages [12] -->
m

<!-- b001656 | prose | pages [12] -->
m

<!-- b001657 | prose | pages [12] -->
m

<!-- b001658 | prose | pages [12] -->
m

<!-- b001659 | prose | pages [12] -->
m

<!-- b001660 | prose | pages [12] -->
m

<!-- b001661 | prose | pages [12] -->
m

<!-- b001662 | prose | pages [12] -->
m

<!-- b001663 | prose | pages [12] -->
m

<!-- b001664 | prose | pages [12] -->
m

<!-- b001665 | prose | pages [12] -->
m

<!-- b001666 | prose | pages [12] -->
m

<!-- b001667 | prose | pages [12] -->
m

<!-- b001668 | prose | pages [12] -->
m

<!-- b001669 | prose | pages [12] -->
m

<!-- b001670 | prose | pages [12] -->
m

<!-- b001671 | prose | pages [12] -->
m

<!-- b001672 | prose | pages [12] -->
m

<!-- b001673 | prose | pages [12] -->
m

<!-- b001674 | prose | pages [12] -->
m

<!-- b001675 | prose | pages [12] -->
m

<!-- b001676 | prose | pages [12] -->
m

<!-- b001677 | prose | pages [12] -->
m

<!-- b001678 | prose | pages [12] -->
m

<!-- b001679 | prose | pages [12] -->
m

<!-- b001680 | prose | pages [12] -->
m

<!-- b001681 | prose | pages [12] -->
m

<!-- b001682 | prose | pages [12] -->
m

<!-- b001683 | prose | pages [12] -->
m

<!-- b001684 | prose | pages [12] -->
m

<!-- b001685 | prose | pages [12] -->
m

<!-- b001686 | prose | pages [12] -->
m

<!-- b001687 | prose | pages [12] -->
m

<!-- b001688 | prose | pages [12] -->
m

<!-- b001689 | prose | pages [12] -->
m

<!-- b001690 | prose | pages [12] -->
m

<!-- b001691 | prose | pages [12] -->
m

<!-- b001692 | prose | pages [12] -->
m

<!-- b001693 | prose | pages [12] -->
m

<!-- b001694 | prose | pages [12] -->
m

<!-- b001695 | prose | pages [12] -->
m

<!-- b001696 | prose | pages [12] -->
m

<!-- b001697 | prose | pages [12] -->
m

<!-- b001698 | prose | pages [12] -->
m

<!-- b001699 | prose | pages [12] -->
m

<!-- b001700 | prose | pages [12] -->
m

<!-- b001701 | prose | pages [12] -->
m

<!-- b001702 | prose | pages [12] -->
m

<!-- b001703 | prose | pages [12] -->
m

<!-- b001704 | prose | pages [12] -->
m

<!-- b001705 | prose | pages [12] -->
m

<!-- b001706 | prose | pages [12] -->
m

<!-- b001707 | prose | pages [12] -->
m

<!-- b001708 | prose | pages [12] -->
m

<!-- b001709 | prose | pages [12] -->
m

<!-- b001710 | prose | pages [12] -->
m

<!-- b001711 | prose | pages [12] -->
m

<!-- b001712 | prose | pages [12] -->
m

<!-- b001713 | prose | pages [12] -->
m

<!-- b001714 | prose | pages [12] -->
m

<!-- b001715 | prose | pages [12] -->
m

<!-- b001716 | prose | pages [12] -->
m

<!-- b001717 | prose | pages [12] -->
m

<!-- b001718 | prose | pages [12] -->
m

<!-- b001719 | prose | pages [12] -->
m

<!-- b001720 | prose | pages [12] -->
m

<!-- b001721 | prose | pages [12] -->
m

<!-- b001722 | prose | pages [12] -->
m

<!-- b001723 | prose | pages [12] -->
m

<!-- b001724 | prose | pages [12] -->
m

<!-- b001725 | prose | pages [12] -->
m

<!-- b001726 | prose | pages [12] -->
m

<!-- b001727 | prose | pages [12] -->
m

<!-- b001728 | prose | pages [12] -->
m

<!-- b001729 | prose | pages [12] -->
m

<!-- b001730 | prose | pages [12] -->
m

<!-- b001731 | prose | pages [12] -->
m

<!-- b001732 | prose | pages [12] -->
m

<!-- b001733 | prose | pages [12] -->
m

<!-- b001734 | prose | pages [12] -->
m

<!-- b001735 | prose | pages [12] -->
m

<!-- b001736 | prose | pages [12] -->
m

<!-- b001737 | prose | pages [12] -->
m

<!-- b001738 | prose | pages [12] -->
m

<!-- b001739 | prose | pages [12] -->
m

<!-- b001740 | prose | pages [12] -->
m

<!-- b001741 | prose | pages [12] -->
m

<!-- b001742 | prose | pages [12] -->
m

<!-- b001743 | prose | pages [12] -->
m

<!-- b001744 | prose | pages [12] -->
m

<!-- b001745 | prose | pages [12] -->
m

<!-- b001746 | prose | pages [12] -->
m

<!-- b001747 | prose | pages [12] -->
m

<!-- b001748 | prose | pages [12] -->
m

<!-- b001749 | prose | pages [12] -->
m

<!-- b001750 | prose | pages [12] -->
m

<!-- b001751 | prose | pages [12] -->
m

<!-- b001752 | prose | pages [12] -->
m

<!-- b001753 | prose | pages [12] -->
m

<!-- b001754 | prose | pages [12] -->
m

<!-- b001755 | prose | pages [12] -->
m

<!-- b001756 | prose | pages [12] -->
m

<!-- b001757 | prose | pages [12] -->
m

<!-- b001758 | prose | pages [12] -->
m

<!-- b001759 | prose | pages [12] -->
m

<!-- b001760 | prose | pages [12] -->
m

<!-- b001761 | prose | pages [12] -->
m

<!-- b001762 | prose | pages [12] -->
m

<!-- b001763 | prose | pages [12] -->
m

<!-- b001764 | prose | pages [12] -->
m

<!-- b001765 | prose | pages [12] -->
m

<!-- b001766 | prose | pages [12] -->
m

<!-- b001767 | prose | pages [12] -->
m

<!-- b001768 | prose | pages [12] -->
m

<!-- b001769 | prose | pages [12] -->
m

<!-- b001770 | prose | pages [12] -->
m

<!-- b001771 | prose | pages [12] -->
m

<!-- b001772 | prose | pages [12] -->
m

<!-- b001773 | prose | pages [12] -->
m

<!-- b001774 | prose | pages [12] -->
m

<!-- b001775 | prose | pages [12] -->
m

<!-- b001776 | prose | pages [12] -->
m

<!-- b001777 | prose | pages [12] -->
m

<!-- b001778 | prose | pages [12] -->
m

<!-- b001779 | prose | pages [12] -->
m

<!-- b001780 | prose | pages [12] -->
m

<!-- b001781 | prose | pages [12] -->
m

<!-- b001782 | prose | pages [12] -->
m

<!-- b001783 | prose | pages [12] -->
m

<!-- b001784 | prose | pages [12] -->
m

<!-- b001785 | prose | pages [12] -->
m

<!-- b001786 | prose | pages [12] -->
m

<!-- b001787 | prose | pages [12] -->
m

<!-- b001788 | prose | pages [12] -->
m

<!-- b001789 | prose | pages [12] -->
m

<!-- b001790 | prose | pages [12] -->
m

<!-- b001791 | prose | pages [12] -->
m

<!-- b001792 | prose | pages [12] -->
NOC Gold Silver Bronze

<!-- b001793 | prose | pages [12] -->
m

<!-- b001794 | prose | pages [12] -->
m

<!-- b001795 | prose | pages [12] -->
m

<!-- b001796 | prose | pages [12] -->
m

<!-- b001797 | prose | pages [12] -->
m

<!-- b001798 | prose | pages [12] -->
m

<!-- b001799 | prose | pages [12] -->
m

<!-- b001800 | prose | pages [12] -->
m

<!-- b001801 | prose | pages [12] -->
m

<!-- b001802 | prose | pages [12] -->
m

<!-- b001803 | prose | pages [12] -->
m

<!-- b001804 | prose | pages [12] -->
m

<!-- b001805 | prose | pages [12] -->
m

<!-- b001806 | prose | pages [12] -->
m

<!-- b001807 | prose | pages [12] -->
m

<!-- b001808 | prose | pages [12] -->
m

<!-- b001809 | prose | pages [12] -->
m

<!-- b001810 | prose | pages [12] -->
m

<!-- b001811 | prose | pages [12] -->
m

<!-- b001812 | prose | pages [12] -->
m

<!-- b001813 | prose | pages [12] -->
m

<!-- b001814 | prose | pages [12] -->
m

<!-- b001815 | prose | pages [12] -->
m

<!-- b001816 | prose | pages [12] -->
m

<!-- b001817 | prose | pages [12] -->
m

<!-- b001818 | prose | pages [12] -->
m

<!-- b001819 | prose | pages [12] -->
m

<!-- b001820 | prose | pages [12] -->
m

<!-- b001821 | prose | pages [12] -->
m

<!-- b001822 | prose | pages [12] -->
m

<!-- b001823 | prose | pages [12] -->
m

<!-- b001824 | prose | pages [12] -->
m

<!-- b001825 | prose | pages [12] -->
m

<!-- b001826 | prose | pages [12] -->
m

<!-- b001827 | prose | pages [12] -->
m

<!-- b001828 | prose | pages [12] -->
m

<!-- b001829 | prose | pages [12] -->
m

<!-- b001830 | prose | pages [12] -->
m

<!-- b001831 | prose | pages [12] -->
m

<!-- b001832 | prose | pages [12] -->
m

<!-- b001833 | prose | pages [12] -->
m

<!-- b001834 | prose | pages [12] -->
m

<!-- b001835 | prose | pages [12] -->
m

<!-- b001836 | prose | pages [12] -->
m

<!-- b001837 | prose | pages [12] -->
m

<!-- b001838 | prose | pages [12] -->
m

<!-- b001839 | prose | pages [12] -->
m

<!-- b001840 | prose | pages [12] -->
m

<!-- b001841 | prose | pages [12] -->
m

<!-- b001842 | prose | pages [12] -->
m

<!-- b001843 | prose | pages [12] -->
m

<!-- b001844 | prose | pages [12] -->
m

<!-- b001845 | prose | pages [12] -->
m

<!-- b001846 | prose | pages [12] -->
m

<!-- b001847 | prose | pages [12] -->
m

<!-- b001848 | prose | pages [12] -->
m

<!-- b001849 | prose | pages [12] -->
m

<!-- b001850 | prose | pages [12] -->
m

<!-- b001851 | prose | pages [12] -->
m

<!-- b001852 | prose | pages [12] -->
m

<!-- b001853 | prose | pages [12] -->
m

<!-- b001854 | prose | pages [12] -->
m

<!-- b001855 | prose | pages [12] -->
m

<!-- b001856 | prose | pages [12] -->
m

<!-- b001857 | prose | pages [12] -->
m

<!-- b001858 | prose | pages [12] -->
m

<!-- b001859 | prose | pages [12] -->
m

<!-- b001860 | prose | pages [12] -->
m

<!-- b001861 | prose | pages [12] -->
m

<!-- b001862 | prose | pages [12] -->
m

<!-- b001863 | prose | pages [12] -->
m

<!-- b001864 | prose | pages [12] -->
m

<!-- b001865 | prose | pages [12] -->
m

<!-- b001866 | prose | pages [12] -->
m

<!-- b001867 | prose | pages [12] -->
m

<!-- b001868 | prose | pages [12] -->
m

<!-- b001869 | prose | pages [12] -->
m

<!-- b001870 | prose | pages [12] -->
m

<!-- b001871 | prose | pages [12] -->
m

<!-- b001872 | prose | pages [12] -->
m

<!-- b001873 | prose | pages [12] -->
m

<!-- b001874 | prose | pages [12] -->
m

<!-- b001875 | prose | pages [12] -->
m

<!-- b001876 | prose | pages [12] -->
m

<!-- b001877 | prose | pages [12] -->
m

<!-- b001878 | prose | pages [12] -->
m

<!-- b001879 | prose | pages [12] -->
m

<!-- b001880 | prose | pages [12] -->
m

<!-- b001881 | prose | pages [12] -->
m

<!-- b001882 | prose | pages [12] -->
m

<!-- b001883 | prose | pages [12] -->
m

<!-- b001884 | prose | pages [12] -->
m

<!-- b001885 | prose | pages [12] -->
m

<!-- b001886 | prose | pages [12] -->
m

<!-- b001887 | prose | pages [12] -->
m

<!-- b001888 | prose | pages [12] -->
m

<!-- b001889 | prose | pages [12] -->
m

<!-- b001890 | prose | pages [12] -->
m

<!-- b001891 | prose | pages [12] -->
m

<!-- b001892 | prose | pages [12] -->
m

<!-- b001893 | prose | pages [12] -->
m

<!-- b001894 | prose | pages [12] -->
m

<!-- b001895 | prose | pages [12] -->
m

<!-- b001896 | prose | pages [12] -->
m

<!-- b001897 | prose | pages [12] -->
m

<!-- b001898 | prose | pages [12] -->
m

<!-- b001899 | prose | pages [12] -->
m

<!-- b001900 | prose | pages [12] -->
m

<!-- b001901 | prose | pages [12] -->
m

<!-- b001902 | prose | pages [12] -->
m

<!-- b001903 | prose | pages [12] -->
m

<!-- b001904 | prose | pages [12] -->
m

<!-- b001905 | prose | pages [12] -->
m

<!-- b001906 | prose | pages [12] -->
m

<!-- b001907 | prose | pages [12] -->
m

<!-- b001908 | prose | pages [12] -->
m

<!-- b001909 | prose | pages [12] -->
m

<!-- b001910 | prose | pages [12] -->
m

<!-- b001911 | prose | pages [12] -->
m

<!-- b001912 | prose | pages [12] -->
m

<!-- b001913 | prose | pages [12] -->
m

<!-- b001914 | prose | pages [12] -->
m

<!-- b001915 | prose | pages [12] -->
m

<!-- b001916 | prose | pages [12] -->
m

<!-- b001917 | prose | pages [12] -->
m

<!-- b001918 | prose | pages [12] -->
m

<!-- b001919 | prose | pages [12] -->
m

<!-- b001920 | prose | pages [12] -->
m

<!-- b001921 | prose | pages [12] -->
m

<!-- b001922 | prose | pages [12] -->
m

<!-- b001923 | prose | pages [12] -->
m

<!-- b001924 | prose | pages [12] -->
m

<!-- b001925 | prose | pages [12] -->
m

<!-- b001926 | prose | pages [12] -->
m

<!-- b001927 | prose | pages [12] -->
m

<!-- b001928 | prose | pages [12] -->
m

<!-- b001929 | prose | pages [12] -->
m

<!-- b001930 | prose | pages [12] -->
m

<!-- b001931 | prose | pages [12] -->
m

<!-- b001932 | prose | pages [12] -->
m

<!-- b001933 | prose | pages [12] -->
m

<!-- b001934 | prose | pages [12] -->
m

<!-- b001935 | prose | pages [12] -->
m

<!-- b001936 | prose | pages [12] -->
m

<!-- b001937 | prose | pages [12] -->
m

<!-- b001938 | prose | pages [12] -->
m

<!-- b001939 | prose | pages [12] -->
m

<!-- b001940 | prose | pages [12] -->
m

<!-- b001941 | prose | pages [12] -->
m

<!-- b001942 | prose | pages [12] -->
m

<!-- b001943 | prose | pages [12] -->
m

<!-- b001944 | prose | pages [12] -->
m

<!-- b001945 | prose | pages [12] -->
m

<!-- b001946 | prose | pages [12] -->
m

<!-- b001947 | prose | pages [12] -->
m

<!-- b001948 | prose | pages [12] -->
m

<!-- b001949 | prose | pages [12] -->
m

<!-- b001950 | prose | pages [12] -->
m

<!-- b001951 | prose | pages [12] -->
m

<!-- b001952 | prose | pages [12] -->
m

<!-- b001953 | prose | pages [12] -->
m

<!-- b001954 | prose | pages [12] -->
m

<!-- b001955 | prose | pages [12] -->
m

<!-- b001956 | prose | pages [12] -->
m

<!-- b001957 | prose | pages [12] -->
m

<!-- b001958 | prose | pages [12] -->
m

<!-- b001959 | prose | pages [12] -->
m

<!-- b001960 | prose | pages [12] -->
m

<!-- b001961 | prose | pages [12] -->
m

<!-- b001962 | prose | pages [12] -->
m

<!-- b001963 | prose | pages [12] -->
m

<!-- b001964 | prose | pages [12] -->
m

<!-- b001965 | prose | pages [12] -->
m

<!-- b001966 | prose | pages [12] -->
m

<!-- b001967 | prose | pages [12] -->
m

<!-- b001968 | prose | pages [12] -->
m

<!-- b001969 | prose | pages [12] -->
m

<!-- b001970 | prose | pages [12] -->
m

<!-- b001971 | prose | pages [12] -->
m

<!-- b001972 | prose | pages [12] -->
m

<!-- b001973 | prose | pages [12] -->
m

<!-- b001974 | prose | pages [12] -->
m

<!-- b001975 | prose | pages [12] -->
m

<!-- b001976 | prose | pages [12] -->
m

<!-- b001977 | prose | pages [12] -->
m

<!-- b001978 | prose | pages [12] -->
m

<!-- b001979 | prose | pages [12] -->
USA 50 47 40

<!-- b001980 | prose | pages [12] -->
m

<!-- b001981 | prose | pages [12] -->
m

<!-- b001982 | prose | pages [12] -->
m

<!-- b001983 | prose | pages [12] -->
m

<!-- b001984 | prose | pages [12] -->
m

<!-- b001985 | prose | pages [12] -->
m

<!-- b001986 | prose | pages [12] -->
m

<!-- b001987 | prose | pages [12] -->
m

<!-- b001988 | prose | pages [12] -->
m

<!-- b001989 | prose | pages [12] -->
m

<!-- b001990 | prose | pages [12] -->
m

<!-- b001991 | prose | pages [12] -->
m

<!-- b001992 | prose | pages [12] -->
m

<!-- b001993 | prose | pages [12] -->
m

<!-- b001994 | prose | pages [12] -->
m

<!-- b001995 | prose | pages [12] -->
m

<!-- b001996 | prose | pages [12] -->
m

<!-- b001997 | prose | pages [12] -->
m

<!-- b001998 | prose | pages [12] -->
m

<!-- b001999 | prose | pages [12] -->
m

<!-- b002000 | prose | pages [12] -->
m

<!-- b002001 | prose | pages [12] -->
m

<!-- b002002 | prose | pages [12] -->
m

<!-- b002003 | prose | pages [12] -->
m

<!-- b002004 | prose | pages [12] -->
m

<!-- b002005 | prose | pages [12] -->
m

<!-- b002006 | prose | pages [12] -->
m

<!-- b002007 | prose | pages [12] -->
m

<!-- b002008 | prose | pages [12] -->
m

<!-- b002009 | prose | pages [12] -->
m

<!-- b002010 | prose | pages [12] -->
m

<!-- b002011 | prose | pages [12] -->
m

<!-- b002012 | prose | pages [12] -->
m

<!-- b002013 | prose | pages [12] -->
m

<!-- b002014 | prose | pages [12] -->
m

<!-- b002015 | prose | pages [12] -->
m

<!-- b002016 | prose | pages [12] -->
m

<!-- b002017 | prose | pages [12] -->
m

<!-- b002018 | prose | pages [12] -->
m

<!-- b002019 | prose | pages [12] -->
m

<!-- b002020 | prose | pages [12] -->
m

<!-- b002021 | prose | pages [12] -->
m

<!-- b002022 | prose | pages [12] -->
m

<!-- b002023 | prose | pages [12] -->
m

<!-- b002024 | prose | pages [12] -->
m

<!-- b002025 | prose | pages [12] -->
m

<!-- b002026 | prose | pages [12] -->
m

<!-- b002027 | prose | pages [12] -->
m

<!-- b002028 | prose | pages [12] -->
m

<!-- b002029 | prose | pages [12] -->
m

<!-- b002030 | prose | pages [12] -->
m

<!-- b002031 | prose | pages [12] -->
m

<!-- b002032 | prose | pages [12] -->
m

<!-- b002033 | prose | pages [12] -->
m

<!-- b002034 | prose | pages [12] -->
m

<!-- b002035 | prose | pages [12] -->
m

<!-- b002036 | prose | pages [12] -->
m

<!-- b002037 | prose | pages [12] -->
m

<!-- b002038 | prose | pages [12] -->
m

<!-- b002039 | prose | pages [12] -->
m

<!-- b002040 | prose | pages [12] -->
m

<!-- b002041 | prose | pages [12] -->
m

<!-- b002042 | prose | pages [12] -->
m

<!-- b002043 | prose | pages [12] -->
m

<!-- b002044 | prose | pages [12] -->
m

<!-- b002045 | prose | pages [12] -->
m

<!-- b002046 | prose | pages [12] -->
m

<!-- b002047 | prose | pages [12] -->
m

<!-- b002048 | prose | pages [12] -->
m

<!-- b002049 | prose | pages [12] -->
m

<!-- b002050 | prose | pages [12] -->
m

<!-- b002051 | prose | pages [12] -->
m

<!-- b002052 | prose | pages [12] -->
m

<!-- b002053 | prose | pages [12] -->
m

<!-- b002054 | prose | pages [12] -->
m

<!-- b002055 | prose | pages [12] -->
m

<!-- b002056 | prose | pages [12] -->
m

<!-- b002057 | prose | pages [12] -->
m

<!-- b002058 | prose | pages [12] -->
m

<!-- b002059 | prose | pages [12] -->
m

<!-- b002060 | prose | pages [12] -->
m

<!-- b002061 | prose | pages [12] -->
m

<!-- b002062 | prose | pages [12] -->
m

<!-- b002063 | prose | pages [12] -->
m

<!-- b002064 | prose | pages [12] -->
m

<!-- b002065 | prose | pages [12] -->
m

<!-- b002066 | prose | pages [12] -->
m

<!-- b002067 | prose | pages [12] -->
m

<!-- b002068 | prose | pages [12] -->
m

<!-- b002069 | prose | pages [12] -->
m

<!-- b002070 | prose | pages [12] -->
m

<!-- b002071 | prose | pages [12] -->
m

<!-- b002072 | prose | pages [12] -->
m

<!-- b002073 | prose | pages [12] -->
m

<!-- b002074 | prose | pages [12] -->
m

<!-- b002075 | prose | pages [12] -->
m

<!-- b002076 | prose | pages [12] -->
m

<!-- b002077 | prose | pages [12] -->
m

<!-- b002078 | prose | pages [12] -->
m

<!-- b002079 | prose | pages [12] -->
m

<!-- b002080 | prose | pages [12] -->
m

<!-- b002081 | prose | pages [12] -->
m

<!-- b002082 | prose | pages [12] -->
m

<!-- b002083 | prose | pages [12] -->
m

<!-- b002084 | prose | pages [12] -->
m

<!-- b002085 | prose | pages [12] -->
m

<!-- b002086 | prose | pages [12] -->
m

<!-- b002087 | prose | pages [12] -->
m

<!-- b002088 | prose | pages [12] -->
m

<!-- b002089 | prose | pages [12] -->
m

<!-- b002090 | prose | pages [12] -->
m

<!-- b002091 | prose | pages [12] -->
m

<!-- b002092 | prose | pages [12] -->
m

<!-- b002093 | prose | pages [12] -->
m

<!-- b002094 | prose | pages [12] -->
m

<!-- b002095 | prose | pages [12] -->
m

<!-- b002096 | prose | pages [12] -->
m

<!-- b002097 | prose | pages [12] -->
m

<!-- b002098 | prose | pages [12] -->
m

<!-- b002099 | prose | pages [12] -->
m

<!-- b002100 | prose | pages [12] -->
m

<!-- b002101 | prose | pages [12] -->
m

<!-- b002102 | prose | pages [12] -->
m

<!-- b002103 | prose | pages [12] -->
m

<!-- b002104 | prose | pages [12] -->
m

<!-- b002105 | prose | pages [12] -->
m

<!-- b002106 | prose | pages [12] -->
m

<!-- b002107 | prose | pages [12] -->
m

<!-- b002108 | prose | pages [12] -->
m

<!-- b002109 | prose | pages [12] -->
m

<!-- b002110 | prose | pages [12] -->
m

<!-- b002111 | prose | pages [12] -->
m

<!-- b002112 | prose | pages [12] -->
m

<!-- b002113 | prose | pages [12] -->
m

<!-- b002114 | prose | pages [12] -->
m

<!-- b002115 | prose | pages [12] -->
m

<!-- b002116 | prose | pages [12] -->
m

<!-- b002117 | prose | pages [12] -->
m

<!-- b002118 | prose | pages [12] -->
m

<!-- b002119 | prose | pages [12] -->
m

<!-- b002120 | prose | pages [12] -->
m

<!-- b002121 | prose | pages [12] -->
m

<!-- b002122 | prose | pages [12] -->
m

<!-- b002123 | prose | pages [12] -->
m

<!-- b002124 | prose | pages [12] -->
m

<!-- b002125 | prose | pages [12] -->
m

<!-- b002126 | prose | pages [12] -->
m

<!-- b002127 | prose | pages [12] -->
m

<!-- b002128 | prose | pages [12] -->
m

<!-- b002129 | prose | pages [12] -->
m

<!-- b002130 | prose | pages [12] -->
CHN 39 29 22

<!-- b002131 | prose | pages [12] -->
m

<!-- b002132 | prose | pages [12] -->
m

<!-- b002133 | prose | pages [12] -->
m

<!-- b002134 | prose | pages [12] -->
m

<!-- b002135 | prose | pages [12] -->
m

<!-- b002136 | prose | pages [12] -->
m

<!-- b002137 | prose | pages [12] -->
m

<!-- b002138 | prose | pages [12] -->
m

<!-- b002139 | prose | pages [12] -->
m

<!-- b002140 | prose | pages [12] -->
m

<!-- b002141 | prose | pages [12] -->
m

<!-- b002142 | prose | pages [12] -->
m

<!-- b002143 | prose | pages [12] -->
m

<!-- b002144 | prose | pages [12] -->
m

<!-- b002145 | prose | pages [12] -->
m

<!-- b002146 | prose | pages [12] -->
m

<!-- b002147 | prose | pages [12] -->
m

<!-- b002148 | prose | pages [12] -->
m

<!-- b002149 | prose | pages [12] -->
m

<!-- b002150 | prose | pages [12] -->
m

<!-- b002151 | prose | pages [12] -->
m

<!-- b002152 | prose | pages [12] -->
m

<!-- b002153 | prose | pages [12] -->
m

<!-- b002154 | prose | pages [12] -->
m

<!-- b002155 | prose | pages [12] -->
m

<!-- b002156 | prose | pages [12] -->
m

<!-- b002157 | prose | pages [12] -->
m

<!-- b002158 | prose | pages [12] -->
m

<!-- b002159 | prose | pages [12] -->
m

<!-- b002160 | prose | pages [12] -->
m

<!-- b002161 | prose | pages [12] -->
m

<!-- b002162 | prose | pages [12] -->
m

<!-- b002163 | prose | pages [12] -->
m

<!-- b002164 | prose | pages [12] -->
m

<!-- b002165 | prose | pages [12] -->
m

<!-- b002166 | prose | pages [12] -->
m

<!-- b002167 | prose | pages [12] -->
m

<!-- b002168 | prose | pages [12] -->
m

<!-- b002169 | prose | pages [12] -->
m

<!-- b002170 | prose | pages [12] -->
m

<!-- b002171 | prose | pages [12] -->
m

<!-- b002172 | prose | pages [12] -->
m

<!-- b002173 | prose | pages [12] -->
m

<!-- b002174 | prose | pages [12] -->
m

<!-- b002175 | prose | pages [12] -->
m

<!-- b002176 | prose | pages [12] -->
m

<!-- b002177 | prose | pages [12] -->
m

<!-- b002178 | prose | pages [12] -->
m

<!-- b002179 | prose | pages [12] -->
m

<!-- b002180 | prose | pages [12] -->
m

<!-- b002181 | prose | pages [12] -->
m

<!-- b002182 | prose | pages [12] -->
m

<!-- b002183 | prose | pages [12] -->
m

<!-- b002184 | prose | pages [12] -->
m

<!-- b002185 | prose | pages [12] -->
m

<!-- b002186 | prose | pages [12] -->
m

<!-- b002187 | prose | pages [12] -->
m

<!-- b002188 | prose | pages [12] -->
m

<!-- b002189 | prose | pages [12] -->
m

<!-- b002190 | prose | pages [12] -->
m

<!-- b002191 | prose | pages [12] -->
m

<!-- b002192 | prose | pages [12] -->
m

<!-- b002193 | prose | pages [12] -->
m

<!-- b002194 | prose | pages [12] -->
m

<!-- b002195 | prose | pages [12] -->
m

<!-- b002196 | prose | pages [12] -->
m

<!-- b002197 | prose | pages [12] -->
m

<!-- b002198 | prose | pages [12] -->
m

<!-- b002199 | prose | pages [12] -->
m

<!-- b002200 | prose | pages [12] -->
m

<!-- b002201 | prose | pages [12] -->
m

<!-- b002202 | prose | pages [12] -->
m

<!-- b002203 | prose | pages [12] -->
m

<!-- b002204 | prose | pages [12] -->
m

<!-- b002205 | prose | pages [12] -->
m

<!-- b002206 | prose | pages [12] -->
m

<!-- b002207 | prose | pages [12] -->
m

<!-- b002208 | prose | pages [12] -->
m

<!-- b002209 | prose | pages [12] -->
m

<!-- b002210 | prose | pages [12] -->
m

<!-- b002211 | prose | pages [12] -->
m

<!-- b002212 | prose | pages [12] -->
m

<!-- b002213 | prose | pages [12] -->
m

<!-- b002214 | prose | pages [12] -->
m

<!-- b002215 | prose | pages [12] -->
m

<!-- b002216 | prose | pages [12] -->
m

<!-- b002217 | prose | pages [12] -->
m

<!-- b002218 | prose | pages [12] -->
m

<!-- b002219 | prose | pages [12] -->
m

<!-- b002220 | prose | pages [12] -->
m

<!-- b002221 | prose | pages [12] -->
m

<!-- b002222 | prose | pages [12] -->
m

<!-- b002223 | prose | pages [12] -->
m

<!-- b002224 | prose | pages [12] -->
m

<!-- b002225 | prose | pages [12] -->
m

<!-- b002226 | prose | pages [12] -->
m

<!-- b002227 | prose | pages [12] -->
m

<!-- b002228 | prose | pages [12] -->
m

<!-- b002229 | prose | pages [12] -->
m

<!-- b002230 | prose | pages [12] -->
m

<!-- b002231 | prose | pages [12] -->
m

<!-- b002232 | prose | pages [12] -->
m

<!-- b002233 | prose | pages [12] -->
m

<!-- b002234 | prose | pages [12] -->
m

<!-- b002235 | prose | pages [12] -->
m

<!-- b002236 | prose | pages [12] -->
m

<!-- b002237 | prose | pages [12] -->
m

<!-- b002238 | prose | pages [12] -->
m

<!-- b002239 | prose | pages [12] -->
m

<!-- b002240 | prose | pages [12] -->
m

<!-- b002241 | prose | pages [12] -->
m

<!-- b002242 | prose | pages [12] -->
m

<!-- b002243 | prose | pages [12] -->
m

<!-- b002244 | prose | pages [12] -->
m

<!-- b002245 | prose | pages [12] -->
m

<!-- b002246 | prose | pages [12] -->
m

<!-- b002247 | prose | pages [12] -->
m

<!-- b002248 | prose | pages [12] -->
m

<!-- b002249 | prose | pages [12] -->
m

<!-- b002250 | prose | pages [12] -->
m

<!-- b002251 | prose | pages [12] -->
m

<!-- b002252 | prose | pages [12] -->
m

<!-- b002253 | prose | pages [12] -->
m

<!-- b002254 | prose | pages [12] -->
m

<!-- b002255 | prose | pages [12] -->
m

<!-- b002256 | prose | pages [12] -->
m

<!-- b002257 | prose | pages [12] -->
m

<!-- b002258 | prose | pages [12] -->
m

<!-- b002259 | prose | pages [12] -->
m

<!-- b002260 | prose | pages [12] -->
m

<!-- b002261 | prose | pages [12] -->
m

<!-- b002262 | prose | pages [12] -->
m

<!-- b002263 | prose | pages [12] -->
m

<!-- b002264 | prose | pages [12] -->
m

<!-- b002265 | prose | pages [12] -->
m

<!-- b002266 | prose | pages [12] -->
m

<!-- b002267 | prose | pages [12] -->
m

<!-- b002268 | prose | pages [12] -->
m

<!-- b002269 | prose | pages [12] -->
m

<!-- b002270 | prose | pages [12] -->
m

<!-- b002271 | prose | pages [12] -->
m

<!-- b002272 | prose | pages [12] -->
m

<!-- b002273 | prose | pages [12] -->
m

<!-- b002274 | prose | pages [12] -->
m

<!-- b002275 | prose | pages [12] -->
m

<!-- b002276 | prose | pages [12] -->
GBR 20 20 23

<!-- b002277 | prose | pages [12] -->
m

<!-- b002278 | prose | pages [12] -->
m

<!-- b002279 | prose | pages [12] -->
m

<!-- b002280 | prose | pages [12] -->
m

<!-- b002281 | prose | pages [12] -->
m

<!-- b002282 | prose | pages [12] -->
m

<!-- b002283 | prose | pages [12] -->
m

<!-- b002284 | prose | pages [12] -->
m

<!-- b002285 | prose | pages [12] -->
m

<!-- b002286 | prose | pages [12] -->
m

<!-- b002287 | prose | pages [12] -->
m

<!-- b002288 | prose | pages [12] -->
m

<!-- b002289 | prose | pages [12] -->
m

<!-- b002290 | prose | pages [12] -->
m

<!-- b002291 | prose | pages [12] -->
m

<!-- b002292 | prose | pages [12] -->
m

<!-- b002293 | prose | pages [12] -->
m

<!-- b002294 | prose | pages [12] -->
m

<!-- b002295 | prose | pages [12] -->
m

<!-- b002296 | prose | pages [12] -->
m

<!-- b002297 | prose | pages [12] -->
m

<!-- b002298 | prose | pages [12] -->
m

<!-- b002299 | prose | pages [12] -->
m

<!-- b002300 | prose | pages [12] -->
m

<!-- b002301 | prose | pages [12] -->
m

<!-- b002302 | prose | pages [12] -->
m

<!-- b002303 | prose | pages [12] -->
m

<!-- b002304 | prose | pages [12] -->
m

<!-- b002305 | prose | pages [12] -->
m

<!-- b002306 | prose | pages [12] -->
m

<!-- b002307 | prose | pages [12] -->
m

<!-- b002308 | prose | pages [12] -->
m

<!-- b002309 | prose | pages [12] -->
m

<!-- b002310 | prose | pages [12] -->
m

<!-- b002311 | prose | pages [12] -->
m

<!-- b002312 | prose | pages [12] -->
m

<!-- b002313 | prose | pages [12] -->
m

<!-- b002314 | prose | pages [12] -->
m

<!-- b002315 | prose | pages [12] -->
m

<!-- b002316 | prose | pages [12] -->
m

<!-- b002317 | prose | pages [12] -->
m

<!-- b002318 | prose | pages [12] -->
m

<!-- b002319 | prose | pages [12] -->
m

<!-- b002320 | prose | pages [12] -->
m

<!-- b002321 | prose | pages [12] -->
m

<!-- b002322 | prose | pages [12] -->
m

<!-- b002323 | prose | pages [12] -->
m

<!-- b002324 | prose | pages [12] -->
m

<!-- b002325 | prose | pages [12] -->
m

<!-- b002326 | prose | pages [12] -->
m

<!-- b002327 | prose | pages [12] -->
m

<!-- b002328 | prose | pages [12] -->
m

<!-- b002329 | prose | pages [12] -->
m

<!-- b002330 | prose | pages [12] -->
m

<!-- b002331 | prose | pages [12] -->
m

<!-- b002332 | prose | pages [12] -->
m

<!-- b002333 | prose | pages [12] -->
m

<!-- b002334 | prose | pages [12] -->
m

<!-- b002335 | prose | pages [12] -->
m

<!-- b002336 | prose | pages [12] -->
m

<!-- b002337 | prose | pages [12] -->
JPN 17 15 15 AUS 17 15 17 FRA 15 25 22 GER 14 8 9 NED 13 8 12 ITA 11 12 16 KOR 10 7 9 NZL 8 7 5 HUN 7 6 6 CAN 7 7 10 ESP 6 5 8 BRA 5 6 8

<!-- b002338 | prose | pages [12] -->
3.3.3 95% Confidence Intervals by Bootstrap

<!-- b002339 | prose | pages [12] -->
△Total Total Total (2024)

<!-- b002340 | prose | pages [12] -->
137 127 +11 90 91 -1 63 65 -2 47 45 +2 50 53 -3 62 64 -2 31 33 -2 33 34 -1 39 40 -1 26 32 -6 20 20 0 19 19 0 24 27 -3 19 18 +1 19 20 -1

<!-- b002341 | prose | pages [12] -->
For the Random Forest model, the 95% confidence intervals are estimated using the bootstrap method. The process includes the following steps:

<!-- b002342 | prose | pages [12] -->
1. Resample the training data 300 times and train a model for each resample.

<!-- b002343 | prose | pages [12] -->
2. Use the models trained on the resampled data to make predictions.

<!-- b002344 | prose | pages [12] -->
3. Determine the confidence intervals by calculating the 2.5th and 97.5th percentiles of the predictions.

<!-- b002345 | prose | pages [12] -->
The predicted intervals are presented in Table 8:

<!-- b002346 | prose | pages [12] -->
Our prediction intervals for Gold, Silver, Bronze, and Total are predicted separately, so the Total prediction interval is not determined by the intervals for the three medal categories.

<!-- b002347 | prose | pages [12] -->
Task 1.2: The Probability of First Medal 3.4

<!-- b002348 | prose | pages [12] -->
After observing and organizing the dataset, we find that there are currently 77 countries or regions that have participated in the Olympics but have never won a medal. Among them, there are many countries that have participated multiple times.

<!-- b002349 | prose | pages [12] -->
We also identify countries that have won medals for the first time in recent years, including Albania, Cabo Verde, Dominica, and Saint Lucia in 2024. Using historical data, we explore the commonalities of countries that have won medals for the first time. The following predictions are based on Hypothesis 3, which only considers the performance of athletes and not the political and economic situation of external countries.

<!-- b002350 | prose | pages [12] -->
关注数学模型

<!-- b002351 | furniture | pages [12] -->
2

<!-- b002352 | furniture | pages [12] -->
MATHmodels

<!-- b002353 | furniture | pages [12] -->
获取更多资讯

<!-- b002354 | furniture | pages [14] -->
Team #2510185

<!-- b002355 | furniture | pages [14] -->
Page 14 of 24

<!-- b002356 | prose | pages [14] -->
m

<!-- b002357 | prose | pages [14] -->
m

<!-- b002358 | prose | pages [14] -->
m

<!-- b002359 | prose | pages [14] -->
m

<!-- b002360 | prose | pages [14] -->
m

<!-- b002361 | prose | pages [14] -->
m

<!-- b002362 | prose | pages [14] -->
m

<!-- b002363 | prose | pages [14] -->
m

<!-- b002364 | prose | pages [14] -->
m

<!-- b002365 | prose | pages [14] -->
m

<!-- b002366 | prose | pages [14] -->
m

<!-- b002367 | prose | pages [14] -->
m

<!-- b002368 | prose | pages [14] -->
m

<!-- b002369 | prose | pages [14] -->
m

<!-- b002370 | prose | pages [14] -->
m

<!-- b002371 | prose | pages [14] -->
m

<!-- b002372 | prose | pages [14] -->
m

<!-- b002373 | prose | pages [14] -->
m

<!-- b002374 | prose | pages [14] -->
m

<!-- b002375 | prose | pages [14] -->
m

<!-- b002376 | prose | pages [14] -->
m

<!-- b002377 | prose | pages [14] -->
m

<!-- b002378 | prose | pages [14] -->
m

<!-- b002379 | prose | pages [14] -->
m

<!-- b002380 | prose | pages [14] -->
m

<!-- b002381 | prose | pages [14] -->
m

<!-- b002382 | prose | pages [14] -->
m

<!-- b002383 | prose | pages [14] -->
m

<!-- b002384 | prose | pages [14] -->
m

<!-- b002385 | prose | pages [14] -->
m

<!-- b002386 | prose | pages [14] -->
m

<!-- b002387 | prose | pages [14] -->
m

<!-- b002388 | prose | pages [14] -->
m

<!-- b002389 | prose | pages [14] -->
m

<!-- b002390 | prose | pages [14] -->
m

<!-- b002391 | prose | pages [14] -->
m

<!-- b002392 | prose | pages [14] -->
m

<!-- b002393 | prose | pages [14] -->
m

<!-- b002394 | prose | pages [14] -->
and countries that have never won a medal as the test set. A classifier is used to map the likelihood

<!-- b002395 | prose | pages [14] -->
m

<!-- b002396 | prose | pages [14] -->
m

<!-- b002397 | prose | pages [14] -->
m

<!-- b002398 | prose | pages [14] -->
m

<!-- b002399 | prose | pages [14] -->
m

<!-- b002400 | prose | pages [14] -->
m

<!-- b002401 | prose | pages [14] -->
m

<!-- b002402 | prose | pages [14] -->
m

<!-- b002403 | prose | pages [14] -->
m

<!-- b002404 | prose | pages [14] -->
m

<!-- b002405 | prose | pages [14] -->
m

<!-- b002406 | prose | pages [14] -->
m

<!-- b002407 | prose | pages [14] -->
m

<!-- b002408 | prose | pages [14] -->
m

<!-- b002409 | prose | pages [14] -->
m

<!-- b002410 | prose | pages [14] -->
m

<!-- b002411 | prose | pages [14] -->
m

<!-- b002412 | prose | pages [14] -->
m

<!-- b002413 | prose | pages [14] -->
m

<!-- b002414 | prose | pages [14] -->
m

<!-- b002415 | prose | pages [14] -->
m

<!-- b002416 | prose | pages [14] -->
m

<!-- b002417 | prose | pages [14] -->
m

<!-- b002418 | prose | pages [14] -->
m

<!-- b002419 | prose | pages [14] -->
m

<!-- b002420 | prose | pages [14] -->
m

<!-- b002421 | prose | pages [14] -->
m

<!-- b002422 | prose | pages [14] -->
m

<!-- b002423 | prose | pages [14] -->
m

<!-- b002424 | prose | pages [14] -->
m

<!-- b002425 | prose | pages [14] -->
m

<!-- b002426 | prose | pages [14] -->
m

<!-- b002427 | prose | pages [14] -->
m

<!-- b002428 | prose | pages [14] -->
m

<!-- b002429 | prose | pages [14] -->
m

<!-- b002430 | prose | pages [14] -->
m

<!-- b002431 | prose | pages [14] -->
m

<!-- b002432 | prose | pages [14] -->
m

<!-- b002433 | prose | pages [14] -->
m

<!-- b002434 | prose | pages [14] -->
m

<!-- b002435 | prose | pages [14] -->
m

<!-- b002436 | prose | pages [14] -->
m

<!-- b002437 | prose | pages [14] -->
m

<!-- b002438 | prose | pages [14] -->
m

<!-- b002439 | prose | pages [14] -->
m

<!-- b002440 | prose | pages [14] -->
m

<!-- b002441 | prose | pages [14] -->
m

<!-- b002442 | prose | pages [14] -->
m

<!-- b002443 | prose | pages [14] -->
m

<!-- b002444 | prose | pages [14] -->
m

<!-- b002445 | prose | pages [14] -->
m

<!-- b002446 | prose | pages [14] -->
m

<!-- b002447 | prose | pages [14] -->
m

<!-- b002448 | prose | pages [14] -->
m

<!-- b002449 | prose | pages [14] -->
m

<!-- b002450 | prose | pages [14] -->
m

<!-- b002451 | prose | pages [14] -->
m

<!-- b002452 | prose | pages [14] -->
m

<!-- b002453 | prose | pages [14] -->
m

<!-- b002454 | prose | pages [14] -->
m

<!-- b002455 | prose | pages [14] -->
m

<!-- b002456 | prose | pages [14] -->
m

<!-- b002457 | prose | pages [14] -->
m

<!-- b002458 | prose | pages [14] -->
m

<!-- b002459 | prose | pages [14] -->
m

<!-- b002460 | prose | pages [14] -->
m

<!-- b002461 | prose | pages [14] -->
m

<!-- b002462 | prose | pages [14] -->
m

<!-- b002463 | prose | pages [14] -->
m

<!-- b002464 | prose | pages [14] -->
m

<!-- b002465 | prose | pages [14] -->
m

<!-- b002466 | prose | pages [14] -->
m

<!-- b002467 | prose | pages [14] -->
m

<!-- b002468 | prose | pages [14] -->
m

<!-- b002469 | prose | pages [14] -->
m

<!-- b002470 | prose | pages [14] -->
m

<!-- b002471 | prose | pages [14] -->
m

<!-- b002472 | prose | pages [14] -->
m

<!-- b002473 | prose | pages [14] -->
m

<!-- b002474 | prose | pages [14] -->
m

<!-- b002475 | prose | pages [14] -->
m

<!-- b002476 | prose | pages [14] -->
m

<!-- b002477 | prose | pages [14] -->
m

<!-- b002478 | prose | pages [14] -->
m

<!-- b002479 | prose | pages [14] -->
m

<!-- b002480 | prose | pages [14] -->
m

<!-- b002481 | prose | pages [14] -->
m

<!-- b002482 | prose | pages [14] -->
m

<!-- b002483 | prose | pages [14] -->
m

<!-- b002484 | prose | pages [14] -->
m

<!-- b002485 | prose | pages [14] -->
m

<!-- b002486 | prose | pages [14] -->
m

<!-- b002487 | prose | pages [14] -->
m

<!-- b002488 | prose | pages [14] -->
m

<!-- b002489 | prose | pages [14] -->
m

<!-- b002490 | prose | pages [14] -->
m

<!-- b002491 | prose | pages [14] -->
m

<!-- b002492 | prose | pages [14] -->
m

<!-- b002493 | prose | pages [14] -->
m

<!-- b002494 | prose | pages [14] -->
m

<!-- b002495 | prose | pages [14] -->
m

<!-- b002496 | prose | pages [14] -->
m

<!-- b002497 | prose | pages [14] -->
m

<!-- b002498 | prose | pages [14] -->
m

<!-- b002499 | prose | pages [14] -->
m

<!-- b002500 | prose | pages [14] -->
m

<!-- b002501 | prose | pages [14] -->
m

<!-- b002502 | prose | pages [14] -->
m

<!-- b002503 | prose | pages [14] -->
m

<!-- b002504 | prose | pages [14] -->
m

<!-- b002505 | prose | pages [14] -->
m

<!-- b002506 | prose | pages [14] -->
m

<!-- b002507 | prose | pages [14] -->
m

<!-- b002508 | prose | pages [14] -->
m

<!-- b002509 | prose | pages [14] -->
m

<!-- b002510 | prose | pages [14] -->
m

<!-- b002511 | prose | pages [14] -->
m

<!-- b002512 | prose | pages [14] -->
m

<!-- b002513 | prose | pages [14] -->
m

<!-- b002514 | prose | pages [14] -->
m

<!-- b002515 | prose | pages [14] -->
m

<!-- b002516 | prose | pages [14] -->
m

<!-- b002517 | prose | pages [14] -->
m

<!-- b002518 | prose | pages [14] -->
m

<!-- b002519 | prose | pages [14] -->
m

<!-- b002520 | prose | pages [14] -->
m

<!-- b002521 | prose | pages [14] -->
m

<!-- b002522 | prose | pages [14] -->
m

<!-- b002523 | prose | pages [14] -->
m

<!-- b002524 | prose | pages [14] -->
m

<!-- b002525 | prose | pages [14] -->
m

<!-- b002526 | prose | pages [14] -->
m

<!-- b002527 | prose | pages [14] -->
m

<!-- b002528 | prose | pages [14] -->
m

<!-- b002529 | prose | pages [14] -->
m

<!-- b002530 | prose | pages [14] -->
m

<!-- b002531 | prose | pages [14] -->
m

<!-- b002532 | prose | pages [14] -->
m

<!-- b002533 | prose | pages [14] -->
m

<!-- b002534 | prose | pages [14] -->
m

<!-- b002535 | prose | pages [14] -->
m

<!-- b002536 | prose | pages [14] -->
m

<!-- b002537 | prose | pages [14] -->
m

<!-- b002538 | prose | pages [14] -->
m

<!-- b002539 | prose | pages [14] -->
m

<!-- b002540 | prose | pages [14] -->
m

<!-- b002541 | prose | pages [14] -->
m

<!-- b002542 | prose | pages [14] -->
m

<!-- b002543 | prose | pages [14] -->
m

<!-- b002544 | prose | pages [14] -->
of a country winning a medal (PWM = 0 or > 0) to a value between 0 and 1. After comparing SVM

<!-- b002545 | prose | pages [14] -->
m

<!-- b002546 | prose | pages [14] -->
m

<!-- b002547 | prose | pages [14] -->
m

<!-- b002548 | prose | pages [14] -->
m

<!-- b002549 | prose | pages [14] -->
m

<!-- b002550 | prose | pages [14] -->
m

<!-- b002551 | prose | pages [14] -->
m

<!-- b002552 | prose | pages [14] -->
m

<!-- b002553 | prose | pages [14] -->
m

<!-- b002554 | prose | pages [14] -->
m

<!-- b002555 | prose | pages [14] -->
m

<!-- b002556 | prose | pages [14] -->
m

<!-- b002557 | prose | pages [14] -->
m

<!-- b002558 | prose | pages [14] -->
m

<!-- b002559 | prose | pages [14] -->
m

<!-- b002560 | prose | pages [14] -->
m

<!-- b002561 | prose | pages [14] -->
m

<!-- b002562 | prose | pages [14] -->
m

<!-- b002563 | prose | pages [14] -->
m

<!-- b002564 | prose | pages [14] -->
m

<!-- b002565 | prose | pages [14] -->
m

<!-- b002566 | prose | pages [14] -->
m

<!-- b002567 | prose | pages [14] -->
m

<!-- b002568 | prose | pages [14] -->
m

<!-- b002569 | prose | pages [14] -->
m

<!-- b002570 | prose | pages [14] -->
m

<!-- b002571 | prose | pages [14] -->
m

<!-- b002572 | prose | pages [14] -->
m

<!-- b002573 | prose | pages [14] -->
m

<!-- b002574 | prose | pages [14] -->
m

<!-- b002575 | prose | pages [14] -->
m

<!-- b002576 | prose | pages [14] -->
m

<!-- b002577 | prose | pages [14] -->
m

<!-- b002578 | prose | pages [14] -->
m

<!-- b002579 | prose | pages [14] -->
m

<!-- b002580 | prose | pages [14] -->
m

<!-- b002581 | prose | pages [14] -->
m

<!-- b002582 | prose | pages [14] -->
m

<!-- b002583 | prose | pages [14] -->
m

<!-- b002584 | prose | pages [14] -->
m

<!-- b002585 | prose | pages [14] -->
m

<!-- b002586 | prose | pages [14] -->
m

<!-- b002587 | prose | pages [14] -->
m

<!-- b002588 | prose | pages [14] -->
m

<!-- b002589 | prose | pages [14] -->
m

<!-- b002590 | prose | pages [14] -->
m

<!-- b002591 | prose | pages [14] -->
m

<!-- b002592 | prose | pages [14] -->
m

<!-- b002593 | prose | pages [14] -->
m

<!-- b002594 | prose | pages [14] -->
m

<!-- b002595 | prose | pages [14] -->
m

<!-- b002596 | prose | pages [14] -->
m

<!-- b002597 | prose | pages [14] -->
m

<!-- b002598 | prose | pages [14] -->
m

<!-- b002599 | prose | pages [14] -->
m

<!-- b002600 | prose | pages [14] -->
m

<!-- b002601 | prose | pages [14] -->
m

<!-- b002602 | prose | pages [14] -->
m

<!-- b002603 | prose | pages [14] -->
m

<!-- b002604 | prose | pages [14] -->
m

<!-- b002605 | prose | pages [14] -->
m

<!-- b002606 | prose | pages [14] -->
m

<!-- b002607 | prose | pages [14] -->
m

<!-- b002608 | prose | pages [14] -->
m

<!-- b002609 | prose | pages [14] -->
m

<!-- b002610 | prose | pages [14] -->
m

<!-- b002611 | prose | pages [14] -->
m

<!-- b002612 | prose | pages [14] -->
m

<!-- b002613 | prose | pages [14] -->
m

<!-- b002614 | prose | pages [14] -->
m

<!-- b002615 | prose | pages [14] -->
m

<!-- b002616 | prose | pages [14] -->
m

<!-- b002617 | prose | pages [14] -->
m

<!-- b002618 | prose | pages [14] -->
m

<!-- b002619 | prose | pages [14] -->
m

<!-- b002620 | prose | pages [14] -->
m

<!-- b002621 | prose | pages [14] -->
m

<!-- b002622 | prose | pages [14] -->
m

<!-- b002623 | prose | pages [14] -->
m

<!-- b002624 | prose | pages [14] -->
m

<!-- b002625 | prose | pages [14] -->
m

<!-- b002626 | prose | pages [14] -->
m

<!-- b002627 | prose | pages [14] -->
m

<!-- b002628 | prose | pages [14] -->
m

<!-- b002629 | prose | pages [14] -->
m

<!-- b002630 | prose | pages [14] -->
m

<!-- b002631 | prose | pages [14] -->
m

<!-- b002632 | prose | pages [14] -->
m

<!-- b002633 | prose | pages [14] -->
m

<!-- b002634 | prose | pages [14] -->
m

<!-- b002635 | prose | pages [14] -->
m

<!-- b002636 | prose | pages [14] -->
m

<!-- b002637 | prose | pages [14] -->
m

<!-- b002638 | prose | pages [14] -->
m

<!-- b002639 | prose | pages [14] -->
m

<!-- b002640 | prose | pages [14] -->
m

<!-- b002641 | prose | pages [14] -->
m

<!-- b002642 | prose | pages [14] -->
m

<!-- b002643 | prose | pages [14] -->
m

<!-- b002644 | prose | pages [14] -->
m

<!-- b002645 | prose | pages [14] -->
m

<!-- b002646 | prose | pages [14] -->
m

<!-- b002647 | prose | pages [14] -->
m

<!-- b002648 | prose | pages [14] -->
m

<!-- b002649 | prose | pages [14] -->
m

<!-- b002650 | prose | pages [14] -->
m

<!-- b002651 | prose | pages [14] -->
m

<!-- b002652 | prose | pages [14] -->
m

<!-- b002653 | prose | pages [14] -->
m

<!-- b002654 | prose | pages [14] -->
m

<!-- b002655 | prose | pages [14] -->
m

<!-- b002656 | prose | pages [14] -->
m

<!-- b002657 | prose | pages [14] -->
m

<!-- b002658 | prose | pages [14] -->
m

<!-- b002659 | prose | pages [14] -->
m

<!-- b002660 | prose | pages [14] -->
m

<!-- b002661 | prose | pages [14] -->
m

<!-- b002662 | prose | pages [14] -->
m

<!-- b002663 | prose | pages [14] -->
m

<!-- b002664 | prose | pages [14] -->
m

<!-- b002665 | prose | pages [14] -->
m

<!-- b002666 | prose | pages [14] -->
m

<!-- b002667 | prose | pages [14] -->
m

<!-- b002668 | prose | pages [14] -->
m

<!-- b002669 | prose | pages [14] -->
m

<!-- b002670 | prose | pages [14] -->
m

<!-- b002671 | prose | pages [14] -->
m

<!-- b002672 | prose | pages [14] -->
m

<!-- b002673 | prose | pages [14] -->
m

<!-- b002674 | prose | pages [14] -->
m

<!-- b002675 | prose | pages [14] -->
m

<!-- b002676 | prose | pages [14] -->
m

<!-- b002677 | prose | pages [14] -->
m

<!-- b002678 | prose | pages [14] -->
m

<!-- b002679 | prose | pages [14] -->
m

<!-- b002680 | prose | pages [14] -->
m

<!-- b002681 | prose | pages [14] -->
m

<!-- b002682 | prose | pages [14] -->
m

<!-- b002683 | prose | pages [14] -->
m

<!-- b002684 | prose | pages [14] -->
m

<!-- b002685 | prose | pages [14] -->
m

<!-- b002686 | prose | pages [14] -->
m

<!-- b002687 | prose | pages [14] -->
m

<!-- b002688 | prose | pages [14] -->
m

<!-- b002689 | prose | pages [14] -->
m

<!-- b002690 | prose | pages [14] -->
and Random Forest classifiers, we selected the BP neural network classifier, which has an ROC

<!-- b002691 | prose | pages [14] -->
m

<!-- b002692 | prose | pages [14] -->
m

<!-- b002693 | prose | pages [14] -->
m

<!-- b002694 | prose | pages [14] -->
m

<!-- b002695 | prose | pages [14] -->
m

<!-- b002696 | prose | pages [14] -->
m

<!-- b002697 | prose | pages [14] -->
m

<!-- b002698 | prose | pages [14] -->
m

<!-- b002699 | prose | pages [14] -->
m

<!-- b002700 | prose | pages [14] -->
m

<!-- b002701 | prose | pages [14] -->
m

<!-- b002702 | prose | pages [14] -->
m

<!-- b002703 | prose | pages [14] -->
m

<!-- b002704 | prose | pages [14] -->
m

<!-- b002705 | prose | pages [14] -->
m

<!-- b002706 | prose | pages [14] -->
m

<!-- b002707 | prose | pages [14] -->
m

<!-- b002708 | prose | pages [14] -->
m

<!-- b002709 | prose | pages [14] -->
m

<!-- b002710 | prose | pages [14] -->
m

<!-- b002711 | prose | pages [14] -->
m

<!-- b002712 | prose | pages [14] -->
m

<!-- b002713 | prose | pages [14] -->
m

<!-- b002714 | prose | pages [14] -->
m

<!-- b002715 | prose | pages [14] -->
m

<!-- b002716 | prose | pages [14] -->
m

<!-- b002717 | prose | pages [14] -->
m

<!-- b002718 | prose | pages [14] -->
m

<!-- b002719 | prose | pages [14] -->
m

<!-- b002720 | prose | pages [14] -->
m

<!-- b002721 | prose | pages [14] -->
m

<!-- b002722 | prose | pages [14] -->
m

<!-- b002723 | prose | pages [14] -->
m

<!-- b002724 | prose | pages [14] -->
m

<!-- b002725 | prose | pages [14] -->
m

<!-- b002726 | prose | pages [14] -->
m

<!-- b002727 | prose | pages [14] -->
m

<!-- b002728 | prose | pages [14] -->
m

<!-- b002729 | prose | pages [14] -->
m

<!-- b002730 | prose | pages [14] -->
m

<!-- b002731 | prose | pages [14] -->
m

<!-- b002732 | prose | pages [14] -->
m

<!-- b002733 | prose | pages [14] -->
m

<!-- b002734 | prose | pages [14] -->
m

<!-- b002735 | prose | pages [14] -->
m

<!-- b002736 | prose | pages [14] -->
m

<!-- b002737 | prose | pages [14] -->
m

<!-- b002738 | prose | pages [14] -->
m

<!-- b002739 | prose | pages [14] -->
m

<!-- b002740 | prose | pages [14] -->
m

<!-- b002741 | prose | pages [14] -->
m

<!-- b002742 | prose | pages [14] -->
m

<!-- b002743 | prose | pages [14] -->
m

<!-- b002744 | prose | pages [14] -->
m

<!-- b002745 | prose | pages [14] -->
m

<!-- b002746 | prose | pages [14] -->
m

<!-- b002747 | prose | pages [14] -->
m

<!-- b002748 | prose | pages [14] -->
m

<!-- b002749 | prose | pages [14] -->
m

<!-- b002750 | prose | pages [14] -->
m

<!-- b002751 | prose | pages [14] -->
m

<!-- b002752 | prose | pages [14] -->
m

<!-- b002753 | prose | pages [14] -->
m

<!-- b002754 | prose | pages [14] -->
m

<!-- b002755 | prose | pages [14] -->
m

<!-- b002756 | prose | pages [14] -->
m

<!-- b002757 | prose | pages [14] -->
m

<!-- b002758 | prose | pages [14] -->
m

<!-- b002759 | prose | pages [14] -->
m

<!-- b002760 | prose | pages [14] -->
m

<!-- b002761 | prose | pages [14] -->
m

<!-- b002762 | prose | pages [14] -->
m

<!-- b002763 | prose | pages [14] -->
m

<!-- b002764 | prose | pages [14] -->
m

<!-- b002765 | prose | pages [14] -->
m

<!-- b002766 | prose | pages [14] -->
m

<!-- b002767 | prose | pages [14] -->
m

<!-- b002768 | prose | pages [14] -->
m

<!-- b002769 | prose | pages [14] -->
m

<!-- b002770 | prose | pages [14] -->
m

<!-- b002771 | prose | pages [14] -->
m

<!-- b002772 | prose | pages [14] -->
m

<!-- b002773 | prose | pages [14] -->
m

<!-- b002774 | prose | pages [14] -->
m

<!-- b002775 | prose | pages [14] -->
m

<!-- b002776 | prose | pages [14] -->
m

<!-- b002777 | prose | pages [14] -->
m

<!-- b002778 | prose | pages [14] -->
m

<!-- b002779 | prose | pages [14] -->
m

<!-- b002780 | prose | pages [14] -->
m

<!-- b002781 | prose | pages [14] -->
m

<!-- b002782 | prose | pages [14] -->
m

<!-- b002783 | prose | pages [14] -->
m

<!-- b002784 | prose | pages [14] -->
m

<!-- b002785 | prose | pages [14] -->
m

<!-- b002786 | prose | pages [14] -->
m

<!-- b002787 | prose | pages [14] -->
m

<!-- b002788 | prose | pages [14] -->
m

<!-- b002789 | prose | pages [14] -->
m

<!-- b002790 | prose | pages [14] -->
m

<!-- b002791 | prose | pages [14] -->
m

<!-- b002792 | prose | pages [14] -->
m

<!-- b002793 | prose | pages [14] -->
m

<!-- b002794 | prose | pages [14] -->
m

<!-- b002795 | prose | pages [14] -->
m

<!-- b002796 | prose | pages [14] -->
m

<!-- b002797 | prose | pages [14] -->
m

<!-- b002798 | prose | pages [14] -->
m

<!-- b002799 | prose | pages [14] -->
m

<!-- b002800 | prose | pages [14] -->
m

<!-- b002801 | prose | pages [14] -->
m

<!-- b002802 | prose | pages [14] -->
m

<!-- b002803 | prose | pages [14] -->
m

<!-- b002804 | prose | pages [14] -->
m

<!-- b002805 | prose | pages [14] -->
m

<!-- b002806 | prose | pages [14] -->
m

<!-- b002807 | prose | pages [14] -->
m

<!-- b002808 | prose | pages [14] -->
m

<!-- b002809 | prose | pages [14] -->
m

<!-- b002810 | prose | pages [14] -->
m

<!-- b002811 | prose | pages [14] -->
m

<!-- b002812 | prose | pages [14] -->
m

<!-- b002813 | prose | pages [14] -->
m

<!-- b002814 | prose | pages [14] -->
m

<!-- b002815 | prose | pages [14] -->
m

<!-- b002816 | prose | pages [14] -->
m

<!-- b002817 | prose | pages [14] -->
m

<!-- b002818 | prose | pages [14] -->
m

<!-- b002819 | prose | pages [14] -->
m

<!-- b002820 | prose | pages [14] -->
m

<!-- b002821 | prose | pages [14] -->
m

<!-- b002822 | prose | pages [14] -->
m

<!-- b002823 | prose | pages [14] -->
m

<!-- b002824 | prose | pages [14] -->
m

<!-- b002825 | prose | pages [14] -->
m

<!-- b002826 | prose | pages [14] -->
curve with an area of 0.94, as shown in Figure 8, indicating strong classification performance.

<!-- b002827 | prose | pages [14] -->
m

<!-- b002828 | prose | pages [14] -->
m

<!-- b002829 | prose | pages [14] -->
m

<!-- b002830 | prose | pages [14] -->
m

<!-- b002831 | prose | pages [14] -->
m

<!-- b002832 | prose | pages [14] -->
m

<!-- b002833 | prose | pages [14] -->
m

<!-- b002834 | prose | pages [14] -->
m

<!-- b002835 | prose | pages [14] -->
m

<!-- b002836 | prose | pages [14] -->
m

<!-- b002837 | prose | pages [14] -->
m

<!-- b002838 | prose | pages [14] -->
m

<!-- b002839 | prose | pages [14] -->
m

<!-- b002840 | prose | pages [14] -->
m

<!-- b002841 | prose | pages [14] -->
m

<!-- b002842 | prose | pages [14] -->
m

<!-- b002843 | prose | pages [14] -->
m

<!-- b002844 | prose | pages [14] -->
m

<!-- b002845 | prose | pages [14] -->
m

<!-- b002846 | prose | pages [14] -->
m

<!-- b002847 | prose | pages [14] -->
m

<!-- b002848 | prose | pages [14] -->
m

<!-- b002849 | prose | pages [14] -->
m

<!-- b002850 | prose | pages [14] -->
m

<!-- b002851 | prose | pages [14] -->
m

<!-- b002852 | prose | pages [14] -->
m

<!-- b002853 | prose | pages [14] -->
m

<!-- b002854 | prose | pages [14] -->
m

<!-- b002855 | prose | pages [14] -->
m

<!-- b002856 | prose | pages [14] -->
m

<!-- b002857 | prose | pages [14] -->
m

<!-- b002858 | prose | pages [14] -->
m

<!-- b002859 | prose | pages [14] -->
m

<!-- b002860 | prose | pages [14] -->
m

<!-- b002861 | prose | pages [14] -->
m

<!-- b002862 | prose | pages [14] -->
m

<!-- b002863 | prose | pages [14] -->
m

<!-- b002864 | prose | pages [14] -->
m

<!-- b002865 | prose | pages [14] -->
m

<!-- b002866 | prose | pages [14] -->
m

<!-- b002867 | prose | pages [14] -->
m

<!-- b002868 | prose | pages [14] -->
m

<!-- b002869 | prose | pages [14] -->
m

<!-- b002870 | prose | pages [14] -->
m

<!-- b002871 | prose | pages [14] -->
m

<!-- b002872 | prose | pages [14] -->
m

<!-- b002873 | prose | pages [14] -->
m

<!-- b002874 | prose | pages [14] -->
m

<!-- b002875 | prose | pages [14] -->
m

<!-- b002876 | prose | pages [14] -->
m

<!-- b002877 | prose | pages [14] -->
m

<!-- b002878 | prose | pages [14] -->
m

<!-- b002879 | prose | pages [14] -->
m

<!-- b002880 | prose | pages [14] -->
m

<!-- b002881 | prose | pages [14] -->
m

<!-- b002882 | prose | pages [14] -->
m

<!-- b002883 | prose | pages [14] -->
m

<!-- b002884 | prose | pages [14] -->
m

<!-- b002885 | prose | pages [14] -->
m

<!-- b002886 | prose | pages [14] -->
m

<!-- b002887 | prose | pages [14] -->
m

<!-- b002888 | prose | pages [14] -->
m

<!-- b002889 | prose | pages [14] -->
m

<!-- b002890 | prose | pages [14] -->
m

<!-- b002891 | prose | pages [14] -->
m

<!-- b002892 | prose | pages [14] -->
m

<!-- b002893 | prose | pages [14] -->
m

<!-- b002894 | prose | pages [14] -->
m

<!-- b002895 | prose | pages [14] -->
m

<!-- b002896 | prose | pages [14] -->
m

<!-- b002897 | prose | pages [14] -->
m

<!-- b002898 | prose | pages [14] -->
m

<!-- b002899 | prose | pages [14] -->
m

<!-- b002900 | prose | pages [14] -->
m

<!-- b002901 | prose | pages [14] -->
m

<!-- b002902 | prose | pages [14] -->
m

<!-- b002903 | prose | pages [14] -->
m

<!-- b002904 | prose | pages [14] -->
m

<!-- b002905 | prose | pages [14] -->
m

<!-- b002906 | prose | pages [14] -->
m

<!-- b002907 | prose | pages [14] -->
m

<!-- b002908 | prose | pages [14] -->
m

<!-- b002909 | prose | pages [14] -->
m

<!-- b002910 | prose | pages [14] -->
m

<!-- b002911 | prose | pages [14] -->
m

<!-- b002912 | prose | pages [14] -->
m

<!-- b002913 | prose | pages [14] -->
m

<!-- b002914 | prose | pages [14] -->
m

<!-- b002915 | prose | pages [14] -->
m

<!-- b002916 | prose | pages [14] -->
m

<!-- b002917 | prose | pages [14] -->
m

<!-- b002918 | prose | pages [14] -->
m

<!-- b002919 | prose | pages [14] -->
m

<!-- b002920 | prose | pages [14] -->
m

<!-- b002921 | prose | pages [14] -->
m

<!-- b002922 | prose | pages [14] -->
m

<!-- b002923 | prose | pages [14] -->
m

<!-- b002924 | prose | pages [14] -->
m

<!-- b002925 | prose | pages [14] -->
m

<!-- b002926 | prose | pages [14] -->
m

<!-- b002927 | prose | pages [14] -->
m

<!-- b002928 | prose | pages [14] -->
m

<!-- b002929 | prose | pages [14] -->
m

<!-- b002930 | prose | pages [14] -->
m

<!-- b002931 | prose | pages [14] -->
m

<!-- b002932 | prose | pages [14] -->
m

<!-- b002933 | prose | pages [14] -->
m

<!-- b002934 | prose | pages [14] -->
m

<!-- b002935 | prose | pages [14] -->
m

<!-- b002936 | prose | pages [14] -->
m

<!-- b002937 | prose | pages [14] -->
m

<!-- b002938 | prose | pages [14] -->
m

<!-- b002939 | prose | pages [14] -->
m

<!-- b002940 | prose | pages [14] -->
m

<!-- b002941 | prose | pages [14] -->
m

<!-- b002942 | prose | pages [14] -->
m

<!-- b002943 | prose | pages [14] -->
m

<!-- b002944 | prose | pages [14] -->
m

<!-- b002945 | prose | pages [14] -->
m

<!-- b002946 | prose | pages [14] -->
m

<!-- b002947 | prose | pages [14] -->
m

<!-- b002948 | prose | pages [14] -->
m

<!-- b002949 | prose | pages [14] -->
m

<!-- b002950 | prose | pages [14] -->
m

<!-- b002951 | prose | pages [14] -->
m

<!-- b002952 | prose | pages [14] -->
m

<!-- b002953 | prose | pages [14] -->
m

<!-- b002954 | prose | pages [14] -->
m

<!-- b002955 | prose | pages [14] -->
m

<!-- b002956 | prose | pages [14] -->
m

<!-- b002957 | prose | pages [14] -->
m

<!-- b002958 | prose | pages [14] -->
m

<!-- b002959 | prose | pages [14] -->
m

<!-- b002960 | prose | pages [14] -->
m

<!-- b002961 | prose | pages [14] -->
m

<!-- b002962 | prose | pages [14] -->
m

<!-- b002963 | prose | pages [14] -->
m

<!-- b002964 | prose | pages [14] -->
m

<!-- b002965 | prose | pages [14] -->
m

<!-- b002966 | prose | pages [14] -->
m

<!-- b002967 | prose | pages [14] -->
m

<!-- b002968 | prose | pages [14] -->
m

<!-- b002969 | prose | pages [14] -->
m

<!-- b002970 | prose | pages [14] -->
m

<!-- b002971 | prose | pages [14] -->
m

<!-- b002972 | prose | pages [14] -->
m

<!-- b002973 | prose | pages [14] -->
m

<!-- b002974 | prose | pages [14] -->
m

<!-- b002975 | prose | pages [14] -->
m

<!-- b002976 | prose | pages [14] -->
m

<!-- b002977 | prose | pages [14] -->
m

<!-- b002978 | prose | pages [14] -->
m

<!-- b002979 | prose | pages [14] -->
m

<!-- b002980 | prose | pages [14] -->
m

<!-- b002981 | prose | pages [14] -->
m

<!-- b002982 | prose | pages [14] -->
m

<!-- b002983 | prose | pages [14] -->
m

<!-- b002984 | prose | pages [14] -->
m

<!-- b002985 | prose | pages [14] -->
m

<!-- b002986 | prose | pages [14] -->
m

<!-- b002987 | prose | pages [14] -->
m

<!-- b002988 | prose | pages [14] -->
m

<!-- b002989 | prose | pages [14] -->
m

<!-- b002990 | prose | pages [14] -->
m

<!-- b002991 | prose | pages [14] -->
m

<!-- b002992 | prose | pages [14] -->
m

<!-- b002993 | prose | pages [14] -->
m

<!-- b002994 | prose | pages [14] -->
m

<!-- b002995 | prose | pages [14] -->
m

<!-- b002996 | prose | pages [14] -->
m

<!-- b002997 | prose | pages [14] -->
m

<!-- b002998 | prose | pages [14] -->
m

<!-- b002999 | prose | pages [14] -->
m

<!-- b003000 | prose | pages [14] -->
m

<!-- b003001 | prose | pages [14] -->
m

<!-- b003002 | prose | pages [14] -->
m

<!-- b003003 | prose | pages [14] -->
m

<!-- b003004 | prose | pages [14] -->
m

<!-- b003005 | prose | pages [14] -->
m

<!-- b003006 | prose | pages [14] -->
m

<!-- b003007 | prose | pages [14] -->
m

<!-- b003008 | prose | pages [14] -->
m

<!-- b003009 | prose | pages [14] -->
m

<!-- b003010 | prose | pages [14] -->
m

<!-- b003011 | prose | pages [14] -->
m

<!-- b003012 | prose | pages [14] -->
m

<!-- b003013 | prose | pages [14] -->
m

<!-- b003014 | prose | pages [14] -->
m

<!-- b003015 | prose | pages [14] -->
m

<!-- b003016 | prose | pages [14] -->
m

<!-- b003017 | prose | pages [14] -->
m

<!-- b003018 | prose | pages [14] -->
m

<!-- b003019 | prose | pages [14] -->
m

<!-- b003020 | prose | pages [14] -->
m

<!-- b003021 | prose | pages [14] -->
m

<!-- b003022 | prose | pages [14] -->
A BP neural network classifier is used to predict the 2028 Los Angeles Olympics for countries

<!-- b003023 | prose | pages [14] -->
m

<!-- b003024 | prose | pages [14] -->
m

<!-- b003025 | prose | pages [14] -->
m

<!-- b003026 | prose | pages [14] -->
m

<!-- b003027 | prose | pages [14] -->
m

<!-- b003028 | prose | pages [14] -->
m

<!-- b003029 | prose | pages [14] -->
m

<!-- b003030 | prose | pages [14] -->
m

<!-- b003031 | prose | pages [14] -->
m

<!-- b003032 | prose | pages [14] -->
m

<!-- b003033 | prose | pages [14] -->
m

<!-- b003034 | prose | pages [14] -->
m

<!-- b003035 | prose | pages [14] -->
m

<!-- b003036 | prose | pages [14] -->
m

<!-- b003037 | prose | pages [14] -->
m

<!-- b003038 | prose | pages [14] -->
m

<!-- b003039 | prose | pages [14] -->
m

<!-- b003040 | prose | pages [14] -->
m

<!-- b003041 | prose | pages [14] -->
m

<!-- b003042 | prose | pages [14] -->
m

<!-- b003043 | prose | pages [14] -->
m

<!-- b003044 | prose | pages [14] -->
m

<!-- b003045 | prose | pages [14] -->
m

<!-- b003046 | prose | pages [14] -->
m

<!-- b003047 | prose | pages [14] -->
m

<!-- b003048 | prose | pages [14] -->
that did not win medals, and the resulting probabilities are shown in Table 9:

<!-- b003049 | caption | pages [14] -->
Table 9: Probability of Win first Medal in 2028 (Partial)

<!-- b003050 | prose | pages [14] -->
Prediction Probability NOC N_A

<!-- b003051 | prose | pages [14] -->
GUM 8 ESA 9 LBR 10 PLE 8 RWA 8 GAM 8 COD 6 0.153210476 0.144216761 0.1420369 0.140068978 0.130942091 0.130942091 0.12339206

<!-- b003052 | prose | pages [14] -->
As can be seen from the table, countries with a long history of participation and a large number of participants are more likely to win medals. The overall probability of winning is relatively low, and it cannot be ruled out that none of these countries will win a medal. Countries or regions with a relatively high probability of winning medals at the 2028 Olympics are: GUM, ESA, LBR, and PLE.

<!-- b003053 | prose | pages [14] -->
Task 1.3: The Impact of Events on Medals 3.5

<!-- b003054 | prose | pages [14] -->
In Task 1.1, we used only the number of projects and the number of participants to predict the number of medals. The correlation between the number of projects and the number of medals is 0.52. Below we examine the relationship between the number of events, the number of athletes, and the number of medals won in some countries.

<!-- b003055 | prose | pages [14] -->
By examining the table, we focus on exploring the relationship between medals and events for six countries: China, the United States, Great Britain, Germany, Japan, and France. We organize data on the number of participants in each event and the number of medalists across all Olympic Games in history for each country. Using random forests, we predict the total number of medals won, thereby determining the importance of each event in contributing to the medal count.

<!-- b003056 | prose | pages [14] -->
n X

<!-- b003057 | prose | pages [14] -->
(N_Gi + N_Si + N_Bi)

<!-- b003058 | prose | pages [14] -->
PWMA =

<!-- b003059 | prose | pages [14] -->
i=1

<!-- b003060 | prose | pages [14] -->
(3)

<!-- b003061 | prose | pages [14] -->
where n is the total number of events and i is the i-th event in an Olympic Games.

<!-- b003062 | caption | pages [14] -->
Figure 9 shows the solution framework for this subtask.

<!-- b003063 | prose | pages [14] -->
关注数学模型

<!-- b003064 | furniture | pages [14] -->
2

<!-- b003065 | furniture | pages [14] -->
MATHmodels

<!-- b003066 | furniture | pages [14] -->
获取更多资讯

<!-- b003067 | furniture | pages [15] -->
Team #2510185

<!-- b003068 | furniture | pages [15] -->
Page 15 of 24

<!-- b003069 | prose | pages [15] -->
Olympic events

<!-- b003070 | prose | pages [15] -->
Random Forest

<!-- b003071 | prose | pages [15] -->
Number of medal

<!-- b003072 | prose | pages [15] -->
(number and type)

<!-- b003073 | prose | pages [15] -->
winning athletes

<!-- b003074 | prose | pages [15] -->
E1

<!-- b003075 | prose | pages [15] -->
N1

<!-- b003076 | prose | pages [15] -->
Feature lmportance

<!-- b003077 | prose | pages [15] -->
E2

<!-- b003078 | prose | pages [15] -->
N2

<!-- b003079 | prose | pages [15] -->
Various

<!-- b003080 | prose | pages [15] -->
Total

<!-- b003081 | prose | pages [15] -->
Olympic

<!-- b003082 | prose | pages [15] -->
微信公众号：数学模型

<!-- b003083 | prose | pages [15] -->
E3

<!-- b003084 | prose | pages [15] -->
N3

<!-- b003085 | prose | pages [15] -->
Games

<!-- b003086 | prose | pages [15] -->
Nn

<!-- b003087 | prose | pages [15] -->
E4

<!-- b003088 | caption | pages [15] -->
Figure 9: Flowchart for Task 1.3

<!-- b003089 | prose | pages [15] -->
微信号：MATHmodels

<!-- b003090 | prose | pages [15] -->
3.5.1 Event Importance Based on Random Forests

<!-- b003091 | prose | pages [15] -->
We use random forests to predict the total number of medals based on the number of partici- pants and medalists in each event. The data consists of the number of participants and medalists for each event across multiple Olympic Games for a given country. Random forests are then used to generate feature importance. For example, in predicting the medal count for Germany, the R² value reaches 0.91, and the feature distribution is shown in Figure 10.

<!-- b003092 | caption | pages [15] -->
Figure 10: The event importance distribution of Germany

<!-- b003093 | prose | pages [15] -->
m

<!-- b003094 | prose | pages [15] -->
m

<!-- b003095 | prose | pages [15] -->
m

<!-- b003096 | prose | pages [15] -->
m

<!-- b003097 | prose | pages [15] -->
m

<!-- b003098 | prose | pages [15] -->
m

<!-- b003099 | prose | pages [15] -->
m

<!-- b003100 | prose | pages [15] -->
m

<!-- b003101 | prose | pages [15] -->
m

<!-- b003102 | prose | pages [15] -->
m

<!-- b003103 | prose | pages [15] -->
m

<!-- b003104 | prose | pages [15] -->
m

<!-- b003105 | prose | pages [15] -->
m

<!-- b003106 | prose | pages [15] -->
m

<!-- b003107 | prose | pages [15] -->
m

<!-- b003108 | prose | pages [15] -->
m

<!-- b003109 | prose | pages [15] -->
m

<!-- b003110 | prose | pages [15] -->
m

<!-- b003111 | prose | pages [15] -->
m

<!-- b003112 | prose | pages [15] -->
m

<!-- b003113 | prose | pages [15] -->
m

<!-- b003114 | prose | pages [15] -->
m

<!-- b003115 | prose | pages [15] -->
m

<!-- b003116 | prose | pages [15] -->
m

<!-- b003117 | prose | pages [15] -->
m

<!-- b003118 | prose | pages [15] -->
m

<!-- b003119 | prose | pages [15] -->
m

<!-- b003120 | prose | pages [15] -->
m

<!-- b003121 | prose | pages [15] -->
m

<!-- b003122 | prose | pages [15] -->
m

<!-- b003123 | prose | pages [15] -->
m

<!-- b003124 | prose | pages [15] -->
m

<!-- b003125 | prose | pages [15] -->
m

<!-- b003126 | prose | pages [15] -->
m

<!-- b003127 | prose | pages [15] -->
m

<!-- b003128 | prose | pages [15] -->
m

<!-- b003129 | prose | pages [15] -->
m

<!-- b003130 | prose | pages [15] -->
m

<!-- b003131 | prose | pages [15] -->
m

<!-- b003132 | prose | pages [15] -->
m

<!-- b003133 | prose | pages [15] -->
m

<!-- b003134 | prose | pages [15] -->
m

<!-- b003135 | prose | pages [15] -->
m

<!-- b003136 | prose | pages [15] -->
m

<!-- b003137 | prose | pages [15] -->
m

<!-- b003138 | prose | pages [15] -->
m

<!-- b003139 | prose | pages [15] -->
m

<!-- b003140 | prose | pages [15] -->
m

<!-- b003141 | prose | pages [15] -->
m

<!-- b003142 | prose | pages [15] -->
m

<!-- b003143 | prose | pages [15] -->
m

<!-- b003144 | prose | pages [15] -->
m

<!-- b003145 | prose | pages [15] -->
m

<!-- b003146 | prose | pages [15] -->
m

<!-- b003147 | prose | pages [15] -->
m

<!-- b003148 | prose | pages [15] -->
m

<!-- b003149 | prose | pages [15] -->
m

<!-- b003150 | prose | pages [15] -->
m

<!-- b003151 | prose | pages [15] -->
m

<!-- b003152 | prose | pages [15] -->
m

<!-- b003153 | prose | pages [15] -->
m

<!-- b003154 | prose | pages [15] -->
m

<!-- b003155 | prose | pages [15] -->
m

<!-- b003156 | prose | pages [15] -->
m

<!-- b003157 | prose | pages [15] -->
m

<!-- b003158 | prose | pages [15] -->
m

<!-- b003159 | prose | pages [15] -->
m

<!-- b003160 | prose | pages [15] -->
m

<!-- b003161 | prose | pages [15] -->
m

<!-- b003162 | prose | pages [15] -->
m

<!-- b003163 | prose | pages [15] -->
m

<!-- b003164 | prose | pages [15] -->
m

<!-- b003165 | prose | pages [15] -->
m

<!-- b003166 | prose | pages [15] -->
m

<!-- b003167 | prose | pages [15] -->
m

<!-- b003168 | prose | pages [15] -->
m

<!-- b003169 | prose | pages [15] -->
m

<!-- b003170 | prose | pages [15] -->
m

<!-- b003171 | prose | pages [15] -->
m

<!-- b003172 | prose | pages [15] -->
m

<!-- b003173 | prose | pages [15] -->
m

<!-- b003174 | prose | pages [15] -->
m

<!-- b003175 | prose | pages [15] -->
m

<!-- b003176 | prose | pages [15] -->
m

<!-- b003177 | prose | pages [15] -->
m

<!-- b003178 | prose | pages [15] -->
m

<!-- b003179 | prose | pages [15] -->
m

<!-- b003180 | prose | pages [15] -->
m

<!-- b003181 | prose | pages [15] -->
m

<!-- b003182 | prose | pages [15] -->
m

<!-- b003183 | prose | pages [15] -->
m

<!-- b003184 | prose | pages [15] -->
m

<!-- b003185 | prose | pages [15] -->
m

<!-- b003186 | prose | pages [15] -->
m

<!-- b003187 | prose | pages [15] -->
m

<!-- b003188 | prose | pages [15] -->
m

<!-- b003189 | prose | pages [15] -->
m

<!-- b003190 | prose | pages [15] -->
m

<!-- b003191 | prose | pages [15] -->
m

<!-- b003192 | prose | pages [15] -->
m

<!-- b003193 | prose | pages [15] -->
m

<!-- b003194 | prose | pages [15] -->
m

<!-- b003195 | prose | pages [15] -->
m

<!-- b003196 | prose | pages [15] -->
m

<!-- b003197 | prose | pages [15] -->
m

<!-- b003198 | prose | pages [15] -->
m

<!-- b003199 | prose | pages [15] -->
m

<!-- b003200 | prose | pages [15] -->
m

<!-- b003201 | prose | pages [15] -->
m

<!-- b003202 | prose | pages [15] -->
m

<!-- b003203 | prose | pages [15] -->
m

<!-- b003204 | prose | pages [15] -->
m

<!-- b003205 | prose | pages [15] -->
m

<!-- b003206 | prose | pages [15] -->
m

<!-- b003207 | prose | pages [15] -->
m

<!-- b003208 | prose | pages [15] -->
m

<!-- b003209 | prose | pages [15] -->
m

<!-- b003210 | prose | pages [15] -->
m

<!-- b003211 | prose | pages [15] -->
m

<!-- b003212 | prose | pages [15] -->
m

<!-- b003213 | prose | pages [15] -->
m

<!-- b003214 | prose | pages [15] -->
m

<!-- b003215 | prose | pages [15] -->
m

<!-- b003216 | prose | pages [15] -->
m

<!-- b003217 | prose | pages [15] -->
m

<!-- b003218 | prose | pages [15] -->
m

<!-- b003219 | prose | pages [15] -->
m

<!-- b003220 | prose | pages [15] -->
m

<!-- b003221 | prose | pages [15] -->
m

<!-- b003222 | prose | pages [15] -->
m

<!-- b003223 | prose | pages [15] -->
m

<!-- b003224 | prose | pages [15] -->
m

<!-- b003225 | prose | pages [15] -->
m

<!-- b003226 | prose | pages [15] -->
m

<!-- b003227 | prose | pages [15] -->
m

<!-- b003228 | prose | pages [15] -->
m

<!-- b003229 | prose | pages [15] -->
m

<!-- b003230 | prose | pages [15] -->
m

<!-- b003231 | prose | pages [15] -->
m

<!-- b003232 | prose | pages [15] -->
m

<!-- b003233 | prose | pages [15] -->
m

<!-- b003234 | prose | pages [15] -->
m

<!-- b003235 | prose | pages [15] -->
m

<!-- b003236 | prose | pages [15] -->
m

<!-- b003237 | prose | pages [15] -->
m

<!-- b003238 | prose | pages [15] -->
m

<!-- b003239 | prose | pages [15] -->
m

<!-- b003240 | prose | pages [15] -->
m

<!-- b003241 | prose | pages [15] -->
m

<!-- b003242 | prose | pages [15] -->
m

<!-- b003243 | prose | pages [15] -->
m

<!-- b003244 | prose | pages [15] -->
m

<!-- b003245 | prose | pages [15] -->
m

<!-- b003246 | prose | pages [15] -->
m

<!-- b003247 | prose | pages [15] -->
m

<!-- b003248 | prose | pages [15] -->
m

<!-- b003249 | prose | pages [15] -->
m

<!-- b003250 | prose | pages [15] -->
m

<!-- b003251 | prose | pages [15] -->
m

<!-- b003252 | prose | pages [15] -->
m

<!-- b003253 | prose | pages [15] -->
m

<!-- b003254 | prose | pages [15] -->
m

<!-- b003255 | prose | pages [15] -->
m

<!-- b003256 | prose | pages [15] -->
m

<!-- b003257 | prose | pages [15] -->
m

<!-- b003258 | prose | pages [15] -->
m

<!-- b003259 | prose | pages [15] -->
m

<!-- b003260 | prose | pages [15] -->
m

<!-- b003261 | prose | pages [15] -->
m

<!-- b003262 | prose | pages [15] -->
m

<!-- b003263 | prose | pages [15] -->
m

<!-- b003264 | prose | pages [15] -->
m

<!-- b003265 | prose | pages [15] -->
m

<!-- b003266 | prose | pages [15] -->
m

<!-- b003267 | prose | pages [15] -->
m

<!-- b003268 | prose | pages [15] -->
m

<!-- b003269 | prose | pages [15] -->
m

<!-- b003270 | prose | pages [15] -->
m

<!-- b003271 | prose | pages [15] -->
m

<!-- b003272 | prose | pages [15] -->
m

<!-- b003273 | prose | pages [15] -->
m

<!-- b003274 | prose | pages [15] -->
m

<!-- b003275 | prose | pages [15] -->
m

<!-- b003276 | prose | pages [15] -->
m

<!-- b003277 | prose | pages [15] -->
m

<!-- b003278 | prose | pages [15] -->
m

<!-- b003279 | prose | pages [15] -->
m

<!-- b003280 | prose | pages [15] -->
m

<!-- b003281 | prose | pages [15] -->
m

<!-- b003282 | prose | pages [15] -->
m

<!-- b003283 | prose | pages [15] -->
m

<!-- b003284 | prose | pages [15] -->
m

<!-- b003285 | prose | pages [15] -->
m

<!-- b003286 | prose | pages [15] -->
m

<!-- b003287 | prose | pages [15] -->
m

<!-- b003288 | prose | pages [15] -->
m

<!-- b003289 | prose | pages [15] -->
m

<!-- b003290 | prose | pages [15] -->
m

<!-- b003291 | prose | pages [15] -->
m

<!-- b003292 | prose | pages [15] -->
m

<!-- b003293 | prose | pages [15] -->
m

<!-- b003294 | prose | pages [15] -->
m

<!-- b003295 | prose | pages [15] -->
m

<!-- b003296 | prose | pages [15] -->
m

<!-- b003297 | prose | pages [15] -->
m

<!-- b003298 | prose | pages [15] -->
m

<!-- b003299 | prose | pages [15] -->
m

<!-- b003300 | prose | pages [15] -->
m

<!-- b003301 | prose | pages [15] -->
m

<!-- b003302 | prose | pages [15] -->
m

<!-- b003303 | prose | pages [15] -->
m

<!-- b003304 | prose | pages [15] -->
m

<!-- b003305 | prose | pages [15] -->
m

<!-- b003306 | prose | pages [15] -->
m

<!-- b003307 | prose | pages [15] -->
m

<!-- b003308 | prose | pages [15] -->
m

<!-- b003309 | prose | pages [15] -->
m

<!-- b003310 | prose | pages [15] -->
m

<!-- b003311 | prose | pages [15] -->
m

<!-- b003312 | prose | pages [15] -->
m

<!-- b003313 | prose | pages [15] -->
m

<!-- b003314 | prose | pages [15] -->
m

<!-- b003315 | prose | pages [15] -->
m

<!-- b003316 | prose | pages [15] -->
m

<!-- b003317 | prose | pages [15] -->
m

<!-- b003318 | prose | pages [15] -->
m

<!-- b003319 | prose | pages [15] -->
m

<!-- b003320 | prose | pages [15] -->
m

<!-- b003321 | prose | pages [15] -->
m

<!-- b003322 | prose | pages [15] -->
m

<!-- b003323 | prose | pages [15] -->
m

<!-- b003324 | prose | pages [15] -->
m

<!-- b003325 | prose | pages [15] -->
m

<!-- b003326 | prose | pages [15] -->
m

<!-- b003327 | prose | pages [15] -->
m

<!-- b003328 | prose | pages [15] -->
m

<!-- b003329 | prose | pages [15] -->
m

<!-- b003330 | prose | pages [15] -->
m

<!-- b003331 | prose | pages [15] -->
m

<!-- b003332 | prose | pages [15] -->
m

<!-- b003333 | prose | pages [15] -->
m

<!-- b003334 | prose | pages [15] -->
m

<!-- b003335 | prose | pages [15] -->
m

<!-- b003336 | prose | pages [15] -->
m

<!-- b003337 | prose | pages [15] -->
m

<!-- b003338 | prose | pages [15] -->
m

<!-- b003339 | prose | pages [15] -->
m

<!-- b003340 | prose | pages [15] -->
m

<!-- b003341 | prose | pages [15] -->
m

<!-- b003342 | prose | pages [15] -->
m

<!-- b003343 | prose | pages [15] -->
m

<!-- b003344 | prose | pages [15] -->
m

<!-- b003345 | prose | pages [15] -->
m

<!-- b003346 | prose | pages [15] -->
m

<!-- b003347 | prose | pages [15] -->
m

<!-- b003348 | prose | pages [15] -->
m

<!-- b003349 | prose | pages [15] -->
m

<!-- b003350 | prose | pages [15] -->
m

<!-- b003351 | prose | pages [15] -->
m

<!-- b003352 | prose | pages [15] -->
m

<!-- b003353 | prose | pages [15] -->
m

<!-- b003354 | prose | pages [15] -->
m

<!-- b003355 | prose | pages [15] -->
m

<!-- b003356 | prose | pages [15] -->
m

<!-- b003357 | prose | pages [15] -->
m

<!-- b003358 | prose | pages [15] -->
m

<!-- b003359 | prose | pages [15] -->
m

<!-- b003360 | prose | pages [15] -->
m

<!-- b003361 | prose | pages [15] -->
m

<!-- b003362 | prose | pages [15] -->
m

<!-- b003363 | prose | pages [15] -->
m

<!-- b003364 | prose | pages [15] -->
m

<!-- b003365 | prose | pages [15] -->
m

<!-- b003366 | prose | pages [15] -->
m

<!-- b003367 | prose | pages [15] -->
m

<!-- b003368 | prose | pages [15] -->
m

<!-- b003369 | prose | pages [15] -->
m

<!-- b003370 | prose | pages [15] -->
m

<!-- b003371 | prose | pages [15] -->
m

<!-- b003372 | prose | pages [15] -->
m

<!-- b003373 | prose | pages [15] -->
m

<!-- b003374 | prose | pages [15] -->
m

<!-- b003375 | prose | pages [15] -->
m

<!-- b003376 | prose | pages [15] -->
m

<!-- b003377 | furniture | pages [15] -->
m

<!-- b003378 | furniture | pages [15] -->
m

<!-- b003379 | furniture | pages [15] -->
m

<!-- b003380 | furniture | pages [15] -->
m

<!-- b003381 | furniture | pages [15] -->
m

<!-- b003382 | furniture | pages [15] -->
m

<!-- b003383 | furniture | pages [15] -->
m

<!-- b003384 | furniture | pages [15] -->
m

<!-- b003385 | furniture | pages [15] -->
m

<!-- b003386 | furniture | pages [15] -->
m

<!-- b003387 | furniture | pages [15] -->
m

<!-- b003388 | furniture | pages [15] -->
m

<!-- b003389 | furniture | pages [15] -->
m

<!-- b003390 | furniture | pages [15] -->
m

<!-- b003391 | furniture | pages [15] -->
m

<!-- b003392 | furniture | pages [15] -->
m

<!-- b003393 | furniture | pages [15] -->
m

<!-- b003394 | furniture | pages [15] -->
m

<!-- b003395 | furniture | pages [15] -->
m

<!-- b003396 | furniture | pages [15] -->
m

<!-- b003397 | furniture | pages [15] -->
m

<!-- b003398 | furniture | pages [15] -->
m

<!-- b003399 | furniture | pages [15] -->
m

<!-- b003400 | furniture | pages [15] -->
m

<!-- b003401 | furniture | pages [15] -->
m

<!-- b003402 | furniture | pages [15] -->
m

<!-- b003403 | furniture | pages [15] -->
m

<!-- b003404 | furniture | pages [15] -->
m

<!-- b003405 | furniture | pages [15] -->
m

<!-- b003406 | furniture | pages [15] -->
m

<!-- b003407 | furniture | pages [15] -->
m

<!-- b003408 | furniture | pages [15] -->
m

<!-- b003409 | furniture | pages [15] -->
m

<!-- b003410 | furniture | pages [15] -->
m

<!-- b003411 | furniture | pages [15] -->
m

<!-- b003412 | furniture | pages [15] -->
m

<!-- b003413 | furniture | pages [15] -->
m

<!-- b003414 | furniture | pages [15] -->
m

<!-- b003415 | furniture | pages [15] -->
m

<!-- b003416 | furniture | pages [15] -->
m

<!-- b003417 | furniture | pages [15] -->
m

<!-- b003418 | furniture | pages [15] -->
m

<!-- b003419 | furniture | pages [15] -->
m

<!-- b003420 | furniture | pages [15] -->
m

<!-- b003421 | furniture | pages [15] -->
m

<!-- b003422 | furniture | pages [15] -->
m

<!-- b003423 | furniture | pages [15] -->
m

<!-- b003424 | furniture | pages [15] -->
m

<!-- b003425 | furniture | pages [15] -->
m

<!-- b003426 | furniture | pages [15] -->
m

<!-- b003427 | furniture | pages [15] -->
m

<!-- b003428 | furniture | pages [15] -->
m

<!-- b003429 | furniture | pages [15] -->
m

<!-- b003430 | furniture | pages [15] -->
m

<!-- b003431 | furniture | pages [15] -->
m

<!-- b003432 | furniture | pages [15] -->
m

<!-- b003433 | furniture | pages [15] -->
m

<!-- b003434 | furniture | pages [15] -->
m

<!-- b003435 | furniture | pages [15] -->
m

<!-- b003436 | furniture | pages [15] -->
m

<!-- b003437 | furniture | pages [15] -->
m

<!-- b003438 | furniture | pages [15] -->
m

<!-- b003439 | furniture | pages [15] -->
m

<!-- b003440 | furniture | pages [15] -->
m

<!-- b003441 | furniture | pages [15] -->
m

<!-- b003442 | furniture | pages [15] -->
m

<!-- b003443 | furniture | pages [15] -->
m

<!-- b003444 | furniture | pages [15] -->
m

<!-- b003445 | furniture | pages [15] -->
m

<!-- b003446 | furniture | pages [15] -->
m

<!-- b003447 | furniture | pages [15] -->
m

<!-- b003448 | furniture | pages [15] -->
m

<!-- b003449 | furniture | pages [15] -->
m

<!-- b003450 | furniture | pages [15] -->
m

<!-- b003451 | furniture | pages [15] -->
m

<!-- b003452 | furniture | pages [15] -->
m

<!-- b003453 | furniture | pages [15] -->
m

<!-- b003454 | furniture | pages [15] -->
m

<!-- b003455 | furniture | pages [15] -->
m

<!-- b003456 | furniture | pages [15] -->
m

<!-- b003457 | furniture | pages [15] -->
m

<!-- b003458 | furniture | pages [15] -->
m

<!-- b003459 | furniture | pages [15] -->
m

<!-- b003460 | furniture | pages [15] -->
m

<!-- b003461 | furniture | pages [15] -->
m

<!-- b003462 | furniture | pages [15] -->
m

<!-- b003463 | furniture | pages [15] -->
m

<!-- b003464 | furniture | pages [15] -->
m

<!-- b003465 | furniture | pages [15] -->
m

<!-- b003466 | furniture | pages [15] -->
m

<!-- b003467 | furniture | pages [15] -->
m

<!-- b003468 | furniture | pages [15] -->
m

<!-- b003469 | furniture | pages [15] -->
m

<!-- b003470 | furniture | pages [15] -->
m

<!-- b003471 | furniture | pages [15] -->
m

<!-- b003472 | furniture | pages [15] -->
m

<!-- b003473 | furniture | pages [15] -->
m

<!-- b003474 | furniture | pages [15] -->
m

<!-- b003475 | furniture | pages [15] -->
m

<!-- b003476 | furniture | pages [15] -->
m

<!-- b003477 | furniture | pages [15] -->
m

<!-- b003478 | furniture | pages [15] -->
m

<!-- b003479 | furniture | pages [15] -->
m

<!-- b003480 | furniture | pages [15] -->
m

<!-- b003481 | furniture | pages [15] -->
m

<!-- b003482 | furniture | pages [15] -->
m

<!-- b003483 | furniture | pages [15] -->
m

<!-- b003484 | furniture | pages [15] -->
m

<!-- b003485 | furniture | pages [15] -->
m

<!-- b003486 | furniture | pages [15] -->
m

<!-- b003487 | furniture | pages [15] -->
m

<!-- b003488 | furniture | pages [15] -->
m

<!-- b003489 | furniture | pages [15] -->
m

<!-- b003490 | furniture | pages [15] -->
m

<!-- b003491 | furniture | pages [15] -->
m

<!-- b003492 | furniture | pages [15] -->
m

<!-- b003493 | furniture | pages [15] -->
m

<!-- b003494 | furniture | pages [15] -->
m

<!-- b003495 | furniture | pages [15] -->
m

<!-- b003496 | furniture | pages [15] -->
m

<!-- b003497 | furniture | pages [15] -->
m

<!-- b003498 | furniture | pages [15] -->
m

<!-- b003499 | furniture | pages [15] -->
m

<!-- b003500 | furniture | pages [15] -->
m

<!-- b003501 | furniture | pages [15] -->
m

<!-- b003502 | furniture | pages [15] -->
m

<!-- b003503 | furniture | pages [15] -->
m

<!-- b003504 | furniture | pages [15] -->
m

<!-- b003505 | furniture | pages [15] -->
m

<!-- b003506 | furniture | pages [15] -->
m

<!-- b003507 | furniture | pages [15] -->
m

<!-- b003508 | furniture | pages [15] -->
m

<!-- b003509 | furniture | pages [15] -->
m

<!-- b003510 | furniture | pages [15] -->
m

<!-- b003511 | furniture | pages [15] -->
m

<!-- b003512 | furniture | pages [15] -->
m

<!-- b003513 | furniture | pages [15] -->
m

<!-- b003514 | furniture | pages [15] -->
m

<!-- b003515 | furniture | pages [15] -->
m

<!-- b003516 | furniture | pages [15] -->
m

<!-- b003517 | furniture | pages [15] -->
m

<!-- b003518 | furniture | pages [15] -->
m

<!-- b003519 | furniture | pages [15] -->
m

<!-- b003520 | furniture | pages [15] -->
m

<!-- b003521 | furniture | pages [15] -->
m

<!-- b003522 | furniture | pages [15] -->
m

<!-- b003523 | furniture | pages [15] -->
m

<!-- b003524 | furniture | pages [15] -->
m

<!-- b003525 | furniture | pages [15] -->
m

<!-- b003526 | furniture | pages [15] -->
m

<!-- b003527 | furniture | pages [15] -->
m

<!-- b003528 | furniture | pages [15] -->
m

<!-- b003529 | furniture | pages [15] -->
m

<!-- b003530 | furniture | pages [15] -->
m

<!-- b003531 | furniture | pages [15] -->
m

<!-- b003532 | furniture | pages [15] -->
m

<!-- b003533 | furniture | pages [15] -->
m

<!-- b003534 | furniture | pages [15] -->
m

<!-- b003535 | furniture | pages [15] -->
m

<!-- b003536 | furniture | pages [15] -->
m

<!-- b003537 | furniture | pages [15] -->
m

<!-- b003538 | furniture | pages [15] -->
m

<!-- b003539 | furniture | pages [15] -->
m

<!-- b003540 | furniture | pages [15] -->
m

<!-- b003541 | furniture | pages [15] -->
m

<!-- b003542 | furniture | pages [15] -->
m

<!-- b003543 | furniture | pages [15] -->
m

<!-- b003544 | furniture | pages [15] -->
m

<!-- b003545 | furniture | pages [15] -->
m

<!-- b003546 | furniture | pages [15] -->
m

<!-- b003547 | furniture | pages [15] -->
m

<!-- b003548 | furniture | pages [15] -->
m

<!-- b003549 | furniture | pages [15] -->
m

<!-- b003550 | furniture | pages [15] -->
m

<!-- b003551 | furniture | pages [15] -->
m

<!-- b003552 | furniture | pages [15] -->
m

<!-- b003553 | furniture | pages [15] -->
m

<!-- b003554 | furniture | pages [15] -->
m

<!-- b003555 | furniture | pages [15] -->
m

<!-- b003556 | furniture | pages [15] -->
m

<!-- b003557 | furniture | pages [15] -->
m

<!-- b003558 | furniture | pages [15] -->
m

<!-- b003559 | furniture | pages [15] -->
m

<!-- b003560 | furniture | pages [15] -->
m

<!-- b003561 | furniture | pages [15] -->
m

<!-- b003562 | furniture | pages [15] -->
m

<!-- b003563 | furniture | pages [15] -->
m

<!-- b003564 | furniture | pages [15] -->
m

<!-- b003565 | furniture | pages [15] -->
m

<!-- b003566 | furniture | pages [15] -->
m

<!-- b003567 | furniture | pages [15] -->
m

<!-- b003568 | furniture | pages [15] -->
m

<!-- b003569 | furniture | pages [15] -->
m

<!-- b003570 | furniture | pages [15] -->
m

<!-- b003571 | furniture | pages [15] -->
m

<!-- b003572 | furniture | pages [15] -->
m

<!-- b003573 | furniture | pages [15] -->
m

<!-- b003574 | furniture | pages [15] -->
m

<!-- b003575 | furniture | pages [15] -->
m

<!-- b003576 | furniture | pages [15] -->
m

<!-- b003577 | furniture | pages [15] -->
m

<!-- b003578 | furniture | pages [15] -->
m

<!-- b003579 | furniture | pages [15] -->
m

<!-- b003580 | furniture | pages [15] -->
m

<!-- b003581 | furniture | pages [15] -->
m

<!-- b003582 | furniture | pages [15] -->
m

<!-- b003583 | furniture | pages [15] -->
m

<!-- b003584 | furniture | pages [15] -->
m

<!-- b003585 | furniture | pages [15] -->
m

<!-- b003586 | furniture | pages [15] -->
m

<!-- b003587 | furniture | pages [15] -->
m

<!-- b003588 | furniture | pages [15] -->
m

<!-- b003589 | furniture | pages [15] -->
m

<!-- b003590 | furniture | pages [15] -->
m

<!-- b003591 | furniture | pages [15] -->
m

<!-- b003592 | furniture | pages [15] -->
m

<!-- b003593 | furniture | pages [15] -->
m

<!-- b003594 | furniture | pages [15] -->
m

<!-- b003595 | furniture | pages [15] -->
m

<!-- b003596 | furniture | pages [15] -->
m

<!-- b003597 | furniture | pages [15] -->
m

<!-- b003598 | furniture | pages [15] -->
m

<!-- b003599 | furniture | pages [15] -->
m

<!-- b003600 | furniture | pages [15] -->
m

<!-- b003601 | furniture | pages [15] -->
m

<!-- b003602 | furniture | pages [15] -->
m

<!-- b003603 | furniture | pages [15] -->
m

<!-- b003604 | furniture | pages [15] -->
m

<!-- b003605 | furniture | pages [15] -->
m

<!-- b003606 | furniture | pages [15] -->
m

<!-- b003607 | furniture | pages [15] -->
m

<!-- b003608 | furniture | pages [15] -->
m

<!-- b003609 | furniture | pages [15] -->
m

<!-- b003610 | furniture | pages [15] -->
m

<!-- b003611 | furniture | pages [15] -->
m

<!-- b003612 | furniture | pages [15] -->
m

<!-- b003613 | furniture | pages [15] -->
m

<!-- b003614 | furniture | pages [15] -->
m

<!-- b003615 | furniture | pages [15] -->
m

<!-- b003616 | furniture | pages [15] -->
m

<!-- b003617 | furniture | pages [15] -->
m

<!-- b003618 | furniture | pages [15] -->
m

<!-- b003619 | furniture | pages [15] -->
m

<!-- b003620 | furniture | pages [15] -->
m

<!-- b003621 | furniture | pages [15] -->
m

<!-- b003622 | furniture | pages [15] -->
m

<!-- b003623 | furniture | pages [15] -->
m

<!-- b003624 | furniture | pages [15] -->
m

<!-- b003625 | furniture | pages [15] -->
m

<!-- b003626 | furniture | pages [15] -->
m

<!-- b003627 | furniture | pages [15] -->
m

<!-- b003628 | furniture | pages [15] -->
m

<!-- b003629 | furniture | pages [15] -->
m

<!-- b003630 | furniture | pages [15] -->
m

<!-- b003631 | furniture | pages [15] -->
m

<!-- b003632 | furniture | pages [15] -->
m

<!-- b003633 | furniture | pages [15] -->
m

<!-- b003634 | furniture | pages [15] -->
m

<!-- b003635 | furniture | pages [15] -->
m

<!-- b003636 | furniture | pages [15] -->
m

<!-- b003637 | furniture | pages [15] -->
m

<!-- b003638 | furniture | pages [15] -->
m

<!-- b003639 | furniture | pages [15] -->
m

<!-- b003640 | furniture | pages [15] -->
m

<!-- b003641 | furniture | pages [15] -->
m

<!-- b003642 | furniture | pages [15] -->
m

<!-- b003643 | furniture | pages [15] -->
m

<!-- b003644 | furniture | pages [15] -->
m

<!-- b003645 | furniture | pages [15] -->
m

<!-- b003646 | furniture | pages [15] -->
m

<!-- b003647 | furniture | pages [15] -->
m

<!-- b003648 | furniture | pages [15] -->
m

<!-- b003649 | furniture | pages [15] -->
m

<!-- b003650 | furniture | pages [15] -->
m

<!-- b003651 | furniture | pages [15] -->
m

<!-- b003652 | furniture | pages [15] -->
m

<!-- b003653 | furniture | pages [15] -->
m

<!-- b003654 | furniture | pages [15] -->
m

<!-- b003655 | furniture | pages [15] -->
m

<!-- b003656 | furniture | pages [15] -->
m

<!-- b003657 | furniture | pages [15] -->
m

<!-- b003658 | furniture | pages [15] -->
m

<!-- b003659 | furniture | pages [15] -->
m

<!-- b003660 | furniture | pages [15] -->
m

<!-- b003661 | furniture | pages [15] -->
m

<!-- b003662 | furniture | pages [15] -->
m

<!-- b003663 | furniture | pages [15] -->
m

<!-- b003664 | furniture | pages [15] -->
m

<!-- b003665 | furniture | pages [15] -->
m

<!-- b003666 | furniture | pages [15] -->
m

<!-- b003667 | furniture | pages [15] -->
m

<!-- b003668 | furniture | pages [15] -->
m

<!-- b003669 | furniture | pages [15] -->
m

<!-- b003670 | furniture | pages [15] -->
m

<!-- b003671 | furniture | pages [15] -->
m

<!-- b003672 | furniture | pages [15] -->
m

<!-- b003673 | furniture | pages [15] -->
m

<!-- b003674 | furniture | pages [15] -->
m

<!-- b003675 | furniture | pages [15] -->
m

<!-- b003676 | furniture | pages [15] -->
m

<!-- b003677 | furniture | pages [15] -->
m

<!-- b003678 | furniture | pages [15] -->
m

<!-- b003679 | furniture | pages [15] -->
m

<!-- b003680 | furniture | pages [15] -->
m

<!-- b003681 | furniture | pages [15] -->
m

<!-- b003682 | furniture | pages [15] -->
m

<!-- b003683 | furniture | pages [15] -->
m

<!-- b003684 | furniture | pages [15] -->
m

<!-- b003685 | furniture | pages [15] -->
m

<!-- b003686 | furniture | pages [15] -->
m

<!-- b003687 | furniture | pages [15] -->
m

<!-- b003688 | furniture | pages [15] -->
m

<!-- b003689 | furniture | pages [15] -->
m

<!-- b003690 | furniture | pages [15] -->
m

<!-- b003691 | furniture | pages [15] -->
m

<!-- b003692 | furniture | pages [15] -->
m

<!-- b003693 | furniture | pages [15] -->
m

<!-- b003694 | furniture | pages [15] -->
m

<!-- b003695 | furniture | pages [15] -->
m

<!-- b003696 | furniture | pages [15] -->
m

<!-- b003697 | furniture | pages [15] -->
m

<!-- b003698 | furniture | pages [15] -->
m

<!-- b003699 | furniture | pages [15] -->
m

<!-- b003700 | furniture | pages [15] -->
m

<!-- b003701 | furniture | pages [15] -->
m

<!-- b003702 | furniture | pages [15] -->
m

<!-- b003703 | furniture | pages [15] -->
m

<!-- b003704 | furniture | pages [15] -->
m

<!-- b003705 | furniture | pages [15] -->
m

<!-- b003706 | furniture | pages [15] -->
m

<!-- b003707 | furniture | pages [15] -->
m

<!-- b003708 | furniture | pages [15] -->
m

<!-- b003709 | furniture | pages [15] -->
m

<!-- b003710 | furniture | pages [15] -->
m

<!-- b003711 | furniture | pages [15] -->
m

<!-- b003712 | furniture | pages [15] -->
m

<!-- b003713 | furniture | pages [15] -->
m

<!-- b003714 | furniture | pages [15] -->
m

<!-- b003715 | furniture | pages [15] -->
m

<!-- b003716 | furniture | pages [15] -->
m

<!-- b003717 | furniture | pages [15] -->
m

<!-- b003718 | furniture | pages [15] -->
m

<!-- b003719 | furniture | pages [15] -->
m

<!-- b003720 | furniture | pages [15] -->
m

<!-- b003721 | furniture | pages [15] -->
m

<!-- b003722 | furniture | pages [15] -->
m

<!-- b003723 | furniture | pages [15] -->
m

<!-- b003724 | furniture | pages [15] -->
m

<!-- b003725 | furniture | pages [15] -->
m

<!-- b003726 | furniture | pages [15] -->
m

<!-- b003727 | furniture | pages [15] -->
m

<!-- b003728 | furniture | pages [15] -->
m

<!-- b003729 | furniture | pages [15] -->
m

<!-- b003730 | furniture | pages [15] -->
m

<!-- b003731 | furniture | pages [15] -->
m

<!-- b003732 | furniture | pages [15] -->
m

<!-- b003733 | furniture | pages [15] -->
m

<!-- b003734 | furniture | pages [15] -->
m

<!-- b003735 | furniture | pages [15] -->
m

<!-- b003736 | furniture | pages [15] -->
m

<!-- b003737 | furniture | pages [15] -->
m

<!-- b003738 | furniture | pages [15] -->
m

<!-- b003739 | furniture | pages [15] -->
m

<!-- b003740 | furniture | pages [15] -->
m

<!-- b003741 | furniture | pages [15] -->
m

<!-- b003742 | furniture | pages [15] -->
m

<!-- b003743 | furniture | pages [15] -->
m

<!-- b003744 | furniture | pages [15] -->
m

<!-- b003745 | furniture | pages [15] -->
m

<!-- b003746 | furniture | pages [15] -->
m

<!-- b003747 | furniture | pages [15] -->
m

<!-- b003748 | furniture | pages [15] -->
m

<!-- b003749 | furniture | pages [15] -->
m

<!-- b003750 | furniture | pages [15] -->
m

<!-- b003751 | furniture | pages [15] -->
m

<!-- b003752 | furniture | pages [15] -->
m

<!-- b003753 | furniture | pages [15] -->
m

<!-- b003754 | furniture | pages [15] -->
m

<!-- b003755 | furniture | pages [15] -->
m

<!-- b003756 | furniture | pages [15] -->
m

<!-- b003757 | furniture | pages [15] -->
m

<!-- b003758 | furniture | pages [15] -->
m

<!-- b003759 | furniture | pages [15] -->
m

<!-- b003760 | furniture | pages [15] -->
m

<!-- b003761 | furniture | pages [15] -->
m

<!-- b003762 | furniture | pages [15] -->
m

<!-- b003763 | furniture | pages [15] -->
m

<!-- b003764 | furniture | pages [15] -->
m

<!-- b003765 | furniture | pages [15] -->
m

<!-- b003766 | furniture | pages [15] -->
m

<!-- b003767 | furniture | pages [15] -->
m

<!-- b003768 | furniture | pages [15] -->
m

<!-- b003769 | furniture | pages [15] -->
m

<!-- b003770 | furniture | pages [15] -->
m

<!-- b003771 | furniture | pages [15] -->
m

<!-- b003772 | furniture | pages [15] -->
m

<!-- b003773 | furniture | pages [15] -->
m

<!-- b003774 | furniture | pages [15] -->
m

<!-- b003775 | furniture | pages [15] -->
m

<!-- b003776 | furniture | pages [15] -->
m

<!-- b003777 | furniture | pages [15] -->
m

<!-- b003778 | furniture | pages [15] -->
m

<!-- b003779 | furniture | pages [15] -->
m

<!-- b003780 | furniture | pages [17] -->
Team #2510185

<!-- b003781 | furniture | pages [17] -->
Page 17 of 24

<!-- b003782 | prose | pages [17] -->
• Great Britain: Rowing, Diving, and Swimming.

<!-- b003783 | prose | pages [17] -->
微信公众号：数学模型

<!-- b003784 | prose | pages [17] -->
• Germany: Canoeing and Shooting.

<!-- b003785 | prose | pages [17] -->
• China: Badminton, Diving, Swimming, and Shooting.

<!-- b003786 | prose | pages [17] -->
• United States: Swimming, Basketball, Volleyball, and Athletics.

<!-- b003787 | prose | pages [17] -->
The model explains that these countries have more participants in key sports and are more likely to win medals in these areas. The identified important sports align closely with the coun- tries’ traditional strengths, which significantly influence their medal counts. This indicates that our model results are highly accurate.

<!-- b003788 | prose | pages [17] -->
微信号：MATHmodels

<!-- b003789 | prose | pages [17] -->
3.5.2 The Impact of Home Country Events

<!-- b003790 | prose | pages [17] -->
The host country often adds new Olympic events. These events are related to the country in some way and are basically sports that the people of the country love. The newly added events of the host country can have a certain impact on the number of medals.

<!-- b003791 | prose | pages [17] -->
Examples include the 1996 Olympic Games in the United States, the 2020 Olympic Games in Japan, and the 2024 Olympic Games in France. We pay attention to whether the host country has certain advantages in the newly added events. According to the data provided, the main events added to these three Olympic Games were:

<!-- b003792 | prose | pages [17] -->
• 1996 Atlanta Olympics: Beach Volleyball, Mountain Biking, Softball, Lightweight Rowing, etc.

<!-- b003793 | prose | pages [17] -->
• 2020 Tokyo Olympics: Baseball, Softball, Rock Climbing, Karate, Surfing, and Skateboard- ing.

<!-- b003794 | prose | pages [17] -->
• 2024 Paris Olympics: Breakdancing, Skateboarding, Rock Climbing, and Surfing.

<!-- b003795 | prose | pages [17] -->
Here are the medal results for the three specific events:

<!-- b003796 | caption | pages [17] -->
Table 10: Medal Counts for New Events at the 1996 Atlanta Olympics

<!-- b003797 | prose | pages [17] -->
NOC N_G N_S N_B

<!-- b003798 | prose | pages [17] -->
USA 41 5 18 RUS 42 2 13 CHN 4 45 5 AUS 0 0 26 BLR 0 12 6 BUL 0 6 11

<!-- b003799 | prose | pages [17] -->
Total P_G P_T

<!-- b003800 | prose | pages [17] -->
64 33.33% 17.63% 57 34.15% 15.70% 54 3.25% 14.88% 26 0 7.16% 18 0 4.96% 17 0 4.68%

<!-- b003801 | furniture | pages [18] -->
Team #2510185

<!-- b003802 | furniture | pages [18] -->
Page 18 of 24

<!-- b003803 | caption | pages [18] -->
Table 11: Medal Counts for New Events at the 2020 Tokyo Olympics

<!-- b003804 | prose | pages [18] -->
NOC N_G N_S N_B

<!-- b003805 | prose | pages [18] -->
JPN 43 4 4 USA 1 40 3 DOM 0 0 24 CAN 0 0 15 BRA 1 3 0 TUR 0 1 3

<!-- b003806 | prose | pages [18] -->
Total P_G P_T

<!-- b003807 | prose | pages [18] -->
51 78.18% 29.48% 44 1.82% 25.43% 24 0 13.87% 15 0 8.67% 4 1.82% 2.31% 4 0 2.31%

<!-- b003808 | caption | pages [18] -->
Table 12: Medal Counts for New Events at the 2024 Paris Olympics

<!-- b003809 | prose | pages [18] -->
NOC N_G N_S N_B

<!-- b003810 | prose | pages [18] -->
USA 1 3 3 JPN 3 3 0 BRA 0 1 3 AUS 2 1 0 FRA 1 1 1 CHN 0 2 1

<!-- b003811 | prose | pages [18] -->
where,

<!-- b003812 | prose | pages [18] -->
Total P_G P_T

<!-- b003813 | prose | pages [18] -->
7 8.33% 19.44% 6 25% 16.67% 4 0 11.11% 3 16.66% 8.33% 3 8.33% 8.33% 3 0 8.33%

<!-- b003814 | prose | pages [18] -->
• P_G is the proportion of the number of people who won gold medals.

<!-- b003815 | prose | pages [18] -->
• N_G is the number of people who won gold medals. When medals are won as a team, we treat it as if each person won a medal individually.

<!-- b003816 | prose | pages [18] -->
As can be seen in the analysis table, the United States and Japan were the top medal winners in the new events in 1996 and 2020, respectively. France also did well in the new events in 2024. After reviewing the relevant information[6][7], we believe that selecting events from the home country that are either advantageous or popular in the country can greatly improve the results of the competition. For example, the new events of karate and skateboarding in Japan, and the new event of softball in the United States. These sports were originally popular in that country.

<!-- b003817 | prose | pages [18] -->
Task 2: “Great Coach” Contribution to Medals 4

<!-- b003818 | prose | pages [18] -->
Existence of “Great Coach” Effect 4.1

<!-- b003819 | prose | pages [18] -->
We first looked up Lang Ping’s coaching trajectory and considered her role as the head coach of the Chinese women’s volleyball team at the 2016 Rio Olympics[8]. We examined the results achieved by the women’s volleyball team at the Games during her tenure as coach. The results are shown in Table 13:

<!-- b003820 | prose | pages [18] -->
The Chinese women’s volleyball team secured the gold medal in women’s volleyball at the 2016 Olympics. However, in the eight years before and after this victory, their best Olympic result

<!-- b003821 | prose | pages [18] -->
关注数学模型

<!-- b003822 | furniture | pages [18] -->
2

<!-- b003823 | furniture | pages [18] -->
MATHmodels

<!-- b003824 | furniture | pages [18] -->
获取更多资讯

<!-- b003825 | furniture | pages [19] -->
Team #2510185

<!-- b003826 | furniture | pages [19] -->
Page 19 of 24

<!-- b003827 | caption | pages [19] -->
Table 13: Performance of the Chinese Women’s Volleyball Team in the Last Five Olympic Games

<!-- b003828 | prose | pages [19] -->
Great Coach Team Year Event Participants Gold Silver Bronze Total

<!-- b003829 | prose | pages [19] -->
微信公众号：数学模型

<!-- b003830 | prose | pages [19] -->
China 2024 13 China 2020 12 China 2016 12 China 2012 12 China 2008 12 0 0 0 0 2.41 0 0 0 0 3.85 1 1 0 0 1.41 0 0 0 0 3.10 0 0 0 1 2.41

<!-- b003831 | prose | pages [19] -->
was a single bronze medal. This leads us to conclude that the "Great Coach" effect does indeed play a role.

<!-- b003832 | prose | pages [19] -->
4.2 Contribution of "Great Coach"

<!-- b003833 | prose | pages [19] -->
微信号：MATHmodels

<!-- b003834 | prose | pages [19] -->
We expanded our analysis by researching legendary Olympic coaches and introduced a binary feature, "Great Coach" (0 or 1), into the dataset. Additional features included "Year" and "AAPI." The dataset covered events such as U.S. women’s volleyball, women’s gymnastics, and men’s sprinting; Chinese women’s volleyball and men’s swimming; German men’s canoeing; Russian women’s gymnastics; British men’s hurdles; and Jamaican women’s sprinting.

<!-- b003835 | prose | pages [19] -->
Using a random forest model to predict the "Total" medal count, the feature importance of "Great Coach" was 0.288. A BP neural network classifier was also applied to estimate the proba- bility of winning a gold medal.

<!-- b003836 | prose | pages [19] -->
For Jamaican women’s sprinting in 2024, the inclusion of the "Great Coach" feature increased the predicted medal count from 0.56 to 1.56.

<!-- b003837 | prose | pages [19] -->
• At an AAPI of approximately 65, the predicted increase was 0.9 bronze medals, 0.2 silver medals, 0.02 gold medals, and 1.2 total medals.

<!-- b003838 | prose | pages [19] -->
• At an AAPI of around 70, the predicted increase was 0.7 bronze medals, 0.9 silver medals, 0.2 gold medals, and 1.8 total medals.

<!-- b003839 | prose | pages [19] -->
These results highlight the significant impact of the "Great Coach" effect, contributing 28.8% to overall performance.

<!-- b003840 | prose | pages [19] -->
4.3 Event Investment and Impact

<!-- b003841 | prose | pages [19] -->
4.3.1 Event Potential Index (EPI)

<!-- b003842 | prose | pages [19] -->
We propose that sports with a history of multiple medals, athletes with higher AAPI, and events showing an upward trend are more likely to benefit from the introduction of a great coach. To estimate the improvement potential of an event after introducing a great coach, we define the Event Potential Index (EPI) using the following formula:

<!-- b003843 | prose | pages [19] -->
EPI = ω1 × Total_trend + ω2 × Total_space + ω3 × AAPI (4)

<!-- b003844 | prose | pages [19] -->
• Total_trend represents the trend in medal count over time.

<!-- b003845 | prose | pages [19] -->
m

<!-- b003846 | prose | pages [19] -->
m

<!-- b003847 | prose | pages [19] -->
m

<!-- b003848 | prose | pages [19] -->
m

<!-- b003849 | prose | pages [19] -->
m

<!-- b003850 | prose | pages [19] -->
m

<!-- b003851 | prose | pages [19] -->
m

<!-- b003852 | prose | pages [19] -->
m

<!-- b003853 | prose | pages [19] -->
m

<!-- b003854 | prose | pages [19] -->
m

<!-- b003855 | prose | pages [19] -->
m

<!-- b003856 | prose | pages [19] -->
m

<!-- b003857 | prose | pages [19] -->
m

<!-- b003858 | prose | pages [19] -->
m

<!-- b003859 | prose | pages [19] -->
m

<!-- b003860 | prose | pages [19] -->
m

<!-- b003861 | prose | pages [19] -->
m

<!-- b003862 | prose | pages [19] -->
m

<!-- b003863 | prose | pages [19] -->
m

<!-- b003864 | prose | pages [19] -->
m

<!-- b003865 | prose | pages [19] -->
m

<!-- b003866 | prose | pages [19] -->
m

<!-- b003867 | prose | pages [19] -->
m

<!-- b003868 | prose | pages [19] -->
m

<!-- b003869 | prose | pages [19] -->
m

<!-- b003870 | prose | pages [19] -->
m

<!-- b003871 | prose | pages [19] -->
m

<!-- b003872 | prose | pages [19] -->
m

<!-- b003873 | prose | pages [19] -->
m

<!-- b003874 | prose | pages [19] -->
m

<!-- b003875 | prose | pages [19] -->
m

<!-- b003876 | prose | pages [19] -->
m

<!-- b003877 | prose | pages [19] -->
m

<!-- b003878 | prose | pages [19] -->
m

<!-- b003879 | prose | pages [19] -->
m

<!-- b003880 | prose | pages [19] -->
m

<!-- b003881 | prose | pages [19] -->
m

<!-- b003882 | prose | pages [19] -->
m

<!-- b003883 | prose | pages [19] -->
m

<!-- b003884 | prose | pages [19] -->
m

<!-- b003885 | prose | pages [19] -->
m

<!-- b003886 | prose | pages [19] -->
m

<!-- b003887 | prose | pages [19] -->
m

<!-- b003888 | prose | pages [19] -->
m

<!-- b003889 | prose | pages [19] -->
m

<!-- b003890 | prose | pages [19] -->
m

<!-- b003891 | prose | pages [19] -->
m

<!-- b003892 | prose | pages [19] -->
m

<!-- b003893 | prose | pages [19] -->
m

<!-- b003894 | prose | pages [19] -->
m

<!-- b003895 | prose | pages [19] -->
m

<!-- b003896 | prose | pages [19] -->
m

<!-- b003897 | prose | pages [19] -->
m

<!-- b003898 | prose | pages [19] -->
m

<!-- b003899 | prose | pages [19] -->
m

<!-- b003900 | prose | pages [19] -->
m

<!-- b003901 | prose | pages [19] -->
m

<!-- b003902 | prose | pages [19] -->
m

<!-- b003903 | prose | pages [19] -->
m

<!-- b003904 | prose | pages [19] -->
m

<!-- b003905 | prose | pages [19] -->
m

<!-- b003906 | prose | pages [19] -->
m

<!-- b003907 | prose | pages [19] -->
m

<!-- b003908 | prose | pages [19] -->
m

<!-- b003909 | prose | pages [19] -->
m

<!-- b003910 | prose | pages [19] -->
m

<!-- b003911 | prose | pages [19] -->
m

<!-- b003912 | prose | pages [19] -->
m

<!-- b003913 | prose | pages [19] -->
m

<!-- b003914 | prose | pages [19] -->
m

<!-- b003915 | prose | pages [19] -->
m

<!-- b003916 | prose | pages [19] -->
m

<!-- b003917 | prose | pages [19] -->
m

<!-- b003918 | prose | pages [19] -->
m

<!-- b003919 | prose | pages [19] -->
m

<!-- b003920 | prose | pages [19] -->
m

<!-- b003921 | prose | pages [19] -->
m

<!-- b003922 | prose | pages [19] -->
m

<!-- b003923 | prose | pages [19] -->
m

<!-- b003924 | prose | pages [19] -->
m

<!-- b003925 | prose | pages [19] -->
m

<!-- b003926 | prose | pages [19] -->
m

<!-- b003927 | prose | pages [19] -->
m

<!-- b003928 | prose | pages [19] -->
m

<!-- b003929 | prose | pages [19] -->
m

<!-- b003930 | prose | pages [19] -->
m

<!-- b003931 | prose | pages [19] -->
m

<!-- b003932 | prose | pages [19] -->
m

<!-- b003933 | prose | pages [19] -->
m

<!-- b003934 | prose | pages [19] -->
m

<!-- b003935 | prose | pages [19] -->
m

<!-- b003936 | prose | pages [19] -->
m

<!-- b003937 | prose | pages [19] -->
m

<!-- b003938 | prose | pages [19] -->
m

<!-- b003939 | prose | pages [19] -->
m

<!-- b003940 | prose | pages [19] -->
m

<!-- b003941 | prose | pages [19] -->
m

<!-- b003942 | prose | pages [19] -->
m

<!-- b003943 | prose | pages [19] -->
m

<!-- b003944 | prose | pages [19] -->
m

<!-- b003945 | prose | pages [19] -->
m

<!-- b003946 | prose | pages [19] -->
m

<!-- b003947 | prose | pages [19] -->
m

<!-- b003948 | prose | pages [19] -->
m

<!-- b003949 | prose | pages [19] -->
m

<!-- b003950 | prose | pages [19] -->
m

<!-- b003951 | prose | pages [19] -->
m

<!-- b003952 | prose | pages [19] -->
m

<!-- b003953 | prose | pages [19] -->
m

<!-- b003954 | prose | pages [19] -->
m

<!-- b003955 | prose | pages [19] -->
m

<!-- b003956 | prose | pages [19] -->
m

<!-- b003957 | prose | pages [19] -->
m

<!-- b003958 | prose | pages [19] -->
m

<!-- b003959 | prose | pages [19] -->
m

<!-- b003960 | prose | pages [19] -->
m

<!-- b003961 | prose | pages [19] -->
m

<!-- b003962 | prose | pages [19] -->
m

<!-- b003963 | prose | pages [19] -->
m

<!-- b003964 | prose | pages [19] -->
m

<!-- b003965 | prose | pages [19] -->
m

<!-- b003966 | prose | pages [19] -->
m

<!-- b003967 | prose | pages [19] -->
m

<!-- b003968 | prose | pages [19] -->
m

<!-- b003969 | prose | pages [19] -->
m

<!-- b003970 | prose | pages [19] -->
m

<!-- b003971 | prose | pages [19] -->
m

<!-- b003972 | prose | pages [19] -->
m

<!-- b003973 | prose | pages [19] -->
m

<!-- b003974 | prose | pages [19] -->
m

<!-- b003975 | prose | pages [19] -->
m

<!-- b003976 | prose | pages [19] -->
m

<!-- b003977 | prose | pages [19] -->
m

<!-- b003978 | prose | pages [19] -->
m

<!-- b003979 | prose | pages [19] -->
m

<!-- b003980 | prose | pages [19] -->
m

<!-- b003981 | prose | pages [19] -->
m

<!-- b003982 | prose | pages [19] -->
m

<!-- b003983 | prose | pages [19] -->
m

<!-- b003984 | prose | pages [19] -->
m

<!-- b003985 | prose | pages [19] -->
m

<!-- b003986 | prose | pages [19] -->
m

<!-- b003987 | prose | pages [19] -->
m

<!-- b003988 | prose | pages [19] -->
m

<!-- b003989 | prose | pages [19] -->
m

<!-- b003990 | prose | pages [19] -->
m

<!-- b003991 | prose | pages [19] -->
m

<!-- b003992 | prose | pages [19] -->
m

<!-- b003993 | prose | pages [19] -->
m

<!-- b003994 | prose | pages [19] -->
m

<!-- b003995 | prose | pages [19] -->
m

<!-- b003996 | prose | pages [19] -->
m

<!-- b003997 | prose | pages [19] -->
m

<!-- b003998 | prose | pages [19] -->
m

<!-- b003999 | prose | pages [19] -->
m

<!-- b004000 | prose | pages [19] -->
m

<!-- b004001 | prose | pages [19] -->
m

<!-- b004002 | prose | pages [19] -->
m

<!-- b004003 | prose | pages [19] -->
m

<!-- b004004 | prose | pages [19] -->
m

<!-- b004005 | prose | pages [19] -->
m

<!-- b004006 | prose | pages [19] -->
m

<!-- b004007 | prose | pages [19] -->
m

<!-- b004008 | prose | pages [19] -->
m

<!-- b004009 | prose | pages [19] -->
m

<!-- b004010 | prose | pages [19] -->
m

<!-- b004011 | prose | pages [19] -->
m

<!-- b004012 | prose | pages [19] -->
m

<!-- b004013 | prose | pages [19] -->
m

<!-- b004014 | prose | pages [19] -->
m

<!-- b004015 | prose | pages [19] -->
m

<!-- b004016 | prose | pages [19] -->
m

<!-- b004017 | prose | pages [19] -->
m

<!-- b004018 | prose | pages [19] -->
m

<!-- b004019 | prose | pages [19] -->
m

<!-- b004020 | prose | pages [19] -->
m

<!-- b004021 | prose | pages [19] -->
m

<!-- b004022 | prose | pages [19] -->
m

<!-- b004023 | prose | pages [19] -->
m

<!-- b004024 | prose | pages [19] -->
m

<!-- b004025 | prose | pages [19] -->
m

<!-- b004026 | prose | pages [19] -->
m

<!-- b004027 | prose | pages [19] -->
m

<!-- b004028 | prose | pages [19] -->
m

<!-- b004029 | prose | pages [19] -->
m

<!-- b004030 | prose | pages [19] -->
m

<!-- b004031 | prose | pages [19] -->
m

<!-- b004032 | prose | pages [19] -->
m

<!-- b004033 | prose | pages [19] -->
m

<!-- b004034 | prose | pages [19] -->
m

<!-- b004035 | prose | pages [19] -->
m

<!-- b004036 | prose | pages [19] -->
m

<!-- b004037 | prose | pages [19] -->
m

<!-- b004038 | prose | pages [19] -->
m

<!-- b004039 | prose | pages [19] -->
m

<!-- b004040 | prose | pages [19] -->
m

<!-- b004041 | prose | pages [19] -->
m

<!-- b004042 | prose | pages [19] -->
m

<!-- b004043 | prose | pages [19] -->
m

<!-- b004044 | prose | pages [19] -->
m

<!-- b004045 | prose | pages [19] -->
m

<!-- b004046 | prose | pages [19] -->
m

<!-- b004047 | prose | pages [19] -->
m

<!-- b004048 | prose | pages [19] -->
m

<!-- b004049 | prose | pages [19] -->
m

<!-- b004050 | prose | pages [19] -->
m

<!-- b004051 | prose | pages [19] -->
m

<!-- b004052 | prose | pages [19] -->
m

<!-- b004053 | prose | pages [19] -->
m

<!-- b004054 | prose | pages [19] -->
m

<!-- b004055 | prose | pages [19] -->
m

<!-- b004056 | prose | pages [19] -->
m

<!-- b004057 | prose | pages [19] -->
m

<!-- b004058 | prose | pages [19] -->
m

<!-- b004059 | prose | pages [19] -->
m

<!-- b004060 | prose | pages [19] -->
m

<!-- b004061 | prose | pages [19] -->
m

<!-- b004062 | prose | pages [19] -->
m

<!-- b004063 | prose | pages [19] -->
m

<!-- b004064 | prose | pages [19] -->
m

<!-- b004065 | prose | pages [19] -->
m

<!-- b004066 | prose | pages [19] -->
m

<!-- b004067 | prose | pages [19] -->
m

<!-- b004068 | prose | pages [19] -->
m

<!-- b004069 | prose | pages [19] -->
m

<!-- b004070 | prose | pages [19] -->
m

<!-- b004071 | prose | pages [19] -->
m

<!-- b004072 | prose | pages [19] -->
m

<!-- b004073 | prose | pages [19] -->
m

<!-- b004074 | prose | pages [19] -->
m

<!-- b004075 | prose | pages [19] -->
m

<!-- b004076 | prose | pages [19] -->
m

<!-- b004077 | prose | pages [19] -->
m

<!-- b004078 | prose | pages [19] -->
m

<!-- b004079 | prose | pages [19] -->
m

<!-- b004080 | prose | pages [19] -->
m

<!-- b004081 | prose | pages [19] -->
m

<!-- b004082 | prose | pages [19] -->
m

<!-- b004083 | prose | pages [19] -->
m

<!-- b004084 | prose | pages [19] -->
m

<!-- b004085 | prose | pages [19] -->
m

<!-- b004086 | prose | pages [19] -->
m

<!-- b004087 | prose | pages [19] -->
m

<!-- b004088 | prose | pages [19] -->
m

<!-- b004089 | prose | pages [19] -->
m

<!-- b004090 | prose | pages [19] -->
m

<!-- b004091 | prose | pages [19] -->
m

<!-- b004092 | prose | pages [19] -->
m

<!-- b004093 | prose | pages [19] -->
m

<!-- b004094 | prose | pages [19] -->
m

<!-- b004095 | prose | pages [19] -->
m

<!-- b004096 | prose | pages [19] -->
m

<!-- b004097 | prose | pages [19] -->
m

<!-- b004098 | prose | pages [19] -->
m

<!-- b004099 | prose | pages [19] -->
m

<!-- b004100 | prose | pages [19] -->
m

<!-- b004101 | prose | pages [19] -->
m

<!-- b004102 | prose | pages [19] -->
m

<!-- b004103 | prose | pages [19] -->
m

<!-- b004104 | prose | pages [19] -->
m

<!-- b004105 | prose | pages [19] -->
m

<!-- b004106 | prose | pages [19] -->
m

<!-- b004107 | prose | pages [19] -->
m

<!-- b004108 | prose | pages [19] -->
m

<!-- b004109 | prose | pages [19] -->
m

<!-- b004110 | prose | pages [19] -->
m

<!-- b004111 | prose | pages [19] -->
m

<!-- b004112 | prose | pages [19] -->
m

<!-- b004113 | prose | pages [19] -->
m

<!-- b004114 | prose | pages [19] -->
m

<!-- b004115 | prose | pages [19] -->
m

<!-- b004116 | prose | pages [19] -->
m

<!-- b004117 | prose | pages [19] -->
m

<!-- b004118 | prose | pages [19] -->
m

<!-- b004119 | prose | pages [19] -->
m

<!-- b004120 | prose | pages [19] -->
m

<!-- b004121 | prose | pages [19] -->
m

<!-- b004122 | prose | pages [19] -->
m

<!-- b004123 | prose | pages [19] -->
m

<!-- b004124 | prose | pages [19] -->
m

<!-- b004125 | prose | pages [19] -->
m

<!-- b004126 | prose | pages [19] -->
m

<!-- b004127 | prose | pages [19] -->
m

<!-- b004128 | prose | pages [19] -->
m

<!-- b004129 | furniture | pages [19] -->
m

<!-- b004130 | furniture | pages [19] -->
m

<!-- b004131 | furniture | pages [19] -->
m

<!-- b004132 | furniture | pages [19] -->
m

<!-- b004133 | furniture | pages [19] -->
m

<!-- b004134 | furniture | pages [19] -->
m

<!-- b004135 | furniture | pages [19] -->
m

<!-- b004136 | furniture | pages [19] -->
m

<!-- b004137 | furniture | pages [19] -->
m

<!-- b004138 | furniture | pages [19] -->
m

<!-- b004139 | furniture | pages [19] -->
m

<!-- b004140 | furniture | pages [19] -->
m

<!-- b004141 | furniture | pages [19] -->
m

<!-- b004142 | furniture | pages [19] -->
m

<!-- b004143 | furniture | pages [19] -->
m

<!-- b004144 | furniture | pages [19] -->
m

<!-- b004145 | furniture | pages [19] -->
m

<!-- b004146 | furniture | pages [19] -->
m

<!-- b004147 | furniture | pages [19] -->
m

<!-- b004148 | furniture | pages [19] -->
m

<!-- b004149 | furniture | pages [19] -->
m

<!-- b004150 | furniture | pages [19] -->
m

<!-- b004151 | furniture | pages [19] -->
m

<!-- b004152 | furniture | pages [19] -->
m

<!-- b004153 | furniture | pages [19] -->
m

<!-- b004154 | furniture | pages [19] -->
m

<!-- b004155 | furniture | pages [19] -->
m

<!-- b004156 | furniture | pages [19] -->
m

<!-- b004157 | furniture | pages [19] -->
m

<!-- b004158 | furniture | pages [19] -->
m

<!-- b004159 | furniture | pages [19] -->
m

<!-- b004160 | furniture | pages [19] -->
m

<!-- b004161 | furniture | pages [19] -->
m

<!-- b004162 | furniture | pages [19] -->
m

<!-- b004163 | furniture | pages [19] -->
m

<!-- b004164 | furniture | pages [19] -->
m

<!-- b004165 | furniture | pages [19] -->
m

<!-- b004166 | furniture | pages [19] -->
m

<!-- b004167 | furniture | pages [19] -->
m

<!-- b004168 | furniture | pages [19] -->
m

<!-- b004169 | furniture | pages [19] -->
m

<!-- b004170 | furniture | pages [19] -->
m

<!-- b004171 | furniture | pages [19] -->
m

<!-- b004172 | furniture | pages [19] -->
m

<!-- b004173 | furniture | pages [19] -->
m

<!-- b004174 | furniture | pages [19] -->
m

<!-- b004175 | furniture | pages [19] -->
m

<!-- b004176 | furniture | pages [19] -->
m

<!-- b004177 | furniture | pages [19] -->
m

<!-- b004178 | furniture | pages [19] -->
m

<!-- b004179 | furniture | pages [19] -->
m

<!-- b004180 | furniture | pages [19] -->
m

<!-- b004181 | furniture | pages [19] -->
m

<!-- b004182 | furniture | pages [19] -->
m

<!-- b004183 | furniture | pages [19] -->
m

<!-- b004184 | furniture | pages [19] -->
m

<!-- b004185 | furniture | pages [19] -->
m

<!-- b004186 | furniture | pages [19] -->
m

<!-- b004187 | furniture | pages [19] -->
m

<!-- b004188 | furniture | pages [19] -->
m

<!-- b004189 | furniture | pages [19] -->
m

<!-- b004190 | furniture | pages [19] -->
m

<!-- b004191 | furniture | pages [19] -->
m

<!-- b004192 | furniture | pages [19] -->
m

<!-- b004193 | furniture | pages [19] -->
m

<!-- b004194 | furniture | pages [19] -->
m

<!-- b004195 | furniture | pages [19] -->
m

<!-- b004196 | furniture | pages [19] -->
m

<!-- b004197 | furniture | pages [19] -->
m

<!-- b004198 | furniture | pages [19] -->
m

<!-- b004199 | furniture | pages [19] -->
m

<!-- b004200 | furniture | pages [19] -->
m

<!-- b004201 | furniture | pages [19] -->
m

<!-- b004202 | furniture | pages [19] -->
m

<!-- b004203 | furniture | pages [19] -->
m

<!-- b004204 | furniture | pages [19] -->
m

<!-- b004205 | furniture | pages [19] -->
m

<!-- b004206 | furniture | pages [19] -->
m

<!-- b004207 | furniture | pages [19] -->
m

<!-- b004208 | furniture | pages [19] -->
m

<!-- b004209 | furniture | pages [19] -->
m

<!-- b004210 | furniture | pages [19] -->
m

<!-- b004211 | furniture | pages [19] -->
m

<!-- b004212 | furniture | pages [19] -->
m

<!-- b004213 | furniture | pages [19] -->
m

<!-- b004214 | furniture | pages [19] -->
m

<!-- b004215 | furniture | pages [19] -->
m

<!-- b004216 | furniture | pages [19] -->
m

<!-- b004217 | furniture | pages [19] -->
m

<!-- b004218 | furniture | pages [19] -->
m

<!-- b004219 | furniture | pages [19] -->
m

<!-- b004220 | furniture | pages [19] -->
m

<!-- b004221 | furniture | pages [19] -->
m

<!-- b004222 | furniture | pages [19] -->
m

<!-- b004223 | furniture | pages [19] -->
m

<!-- b004224 | furniture | pages [19] -->
m

<!-- b004225 | furniture | pages [19] -->
m

<!-- b004226 | furniture | pages [19] -->
m

<!-- b004227 | furniture | pages [19] -->
m

<!-- b004228 | furniture | pages [19] -->
m

<!-- b004229 | furniture | pages [19] -->
m

<!-- b004230 | furniture | pages [19] -->
m

<!-- b004231 | furniture | pages [19] -->
m

<!-- b004232 | furniture | pages [19] -->
m

<!-- b004233 | furniture | pages [19] -->
m

<!-- b004234 | furniture | pages [19] -->
m

<!-- b004235 | furniture | pages [19] -->
m

<!-- b004236 | furniture | pages [19] -->
m

<!-- b004237 | furniture | pages [19] -->
m

<!-- b004238 | furniture | pages [19] -->
m

<!-- b004239 | furniture | pages [19] -->
m

<!-- b004240 | furniture | pages [19] -->
m

<!-- b004241 | furniture | pages [19] -->
m

<!-- b004242 | furniture | pages [19] -->
m

<!-- b004243 | furniture | pages [19] -->
m

<!-- b004244 | furniture | pages [19] -->
m

<!-- b004245 | furniture | pages [19] -->
m

<!-- b004246 | furniture | pages [19] -->
m

<!-- b004247 | furniture | pages [19] -->
m

<!-- b004248 | furniture | pages [19] -->
m

<!-- b004249 | furniture | pages [19] -->
m

<!-- b004250 | furniture | pages [19] -->
m

<!-- b004251 | furniture | pages [19] -->
m

<!-- b004252 | furniture | pages [19] -->
m

<!-- b004253 | furniture | pages [19] -->
m

<!-- b004254 | furniture | pages [19] -->
m

<!-- b004255 | furniture | pages [19] -->
m

<!-- b004256 | furniture | pages [19] -->
m

<!-- b004257 | furniture | pages [19] -->
m

<!-- b004258 | furniture | pages [19] -->
m

<!-- b004259 | furniture | pages [19] -->
m

<!-- b004260 | furniture | pages [19] -->
m

<!-- b004261 | furniture | pages [19] -->
m

<!-- b004262 | furniture | pages [19] -->
m

<!-- b004263 | furniture | pages [19] -->
m

<!-- b004264 | furniture | pages [19] -->
m

<!-- b004265 | furniture | pages [19] -->
m

<!-- b004266 | furniture | pages [19] -->
m

<!-- b004267 | furniture | pages [19] -->
m

<!-- b004268 | furniture | pages [19] -->
m

<!-- b004269 | furniture | pages [19] -->
m

<!-- b004270 | furniture | pages [19] -->
m

<!-- b004271 | furniture | pages [19] -->
m

<!-- b004272 | furniture | pages [19] -->
m

<!-- b004273 | furniture | pages [19] -->
m

<!-- b004274 | furniture | pages [19] -->
m

<!-- b004275 | furniture | pages [19] -->
m

<!-- b004276 | furniture | pages [19] -->
m

<!-- b004277 | furniture | pages [19] -->
m

<!-- b004278 | furniture | pages [19] -->
m

<!-- b004279 | furniture | pages [19] -->
m

<!-- b004280 | furniture | pages [19] -->
m

<!-- b004281 | furniture | pages [19] -->
m

<!-- b004282 | furniture | pages [19] -->
m

<!-- b004283 | furniture | pages [19] -->
m

<!-- b004284 | furniture | pages [19] -->
m

<!-- b004285 | furniture | pages [19] -->
m

<!-- b004286 | furniture | pages [19] -->
m

<!-- b004287 | furniture | pages [19] -->
m

<!-- b004288 | furniture | pages [19] -->
m

<!-- b004289 | furniture | pages [19] -->
m

<!-- b004290 | furniture | pages [19] -->
m

<!-- b004291 | furniture | pages [19] -->
m

<!-- b004292 | furniture | pages [19] -->
m

<!-- b004293 | furniture | pages [19] -->
m

<!-- b004294 | furniture | pages [19] -->
m

<!-- b004295 | furniture | pages [19] -->
m

<!-- b004296 | furniture | pages [19] -->
m

<!-- b004297 | furniture | pages [19] -->
m

<!-- b004298 | furniture | pages [19] -->
m

<!-- b004299 | furniture | pages [19] -->
m

<!-- b004300 | furniture | pages [19] -->
m

<!-- b004301 | furniture | pages [19] -->
m

<!-- b004302 | furniture | pages [19] -->
m

<!-- b004303 | furniture | pages [19] -->
m

<!-- b004304 | furniture | pages [19] -->
m

<!-- b004305 | furniture | pages [19] -->
m

<!-- b004306 | furniture | pages [19] -->
m

<!-- b004307 | furniture | pages [19] -->
m

<!-- b004308 | furniture | pages [19] -->
m

<!-- b004309 | furniture | pages [19] -->
m

<!-- b004310 | furniture | pages [19] -->
m

<!-- b004311 | furniture | pages [19] -->
m

<!-- b004312 | furniture | pages [19] -->
m

<!-- b004313 | furniture | pages [19] -->
m

<!-- b004314 | furniture | pages [19] -->
m

<!-- b004315 | furniture | pages [19] -->
m

<!-- b004316 | furniture | pages [19] -->
m

<!-- b004317 | furniture | pages [19] -->
m

<!-- b004318 | furniture | pages [19] -->
m

<!-- b004319 | furniture | pages [19] -->
m

<!-- b004320 | furniture | pages [19] -->
m

<!-- b004321 | furniture | pages [19] -->
m

<!-- b004322 | furniture | pages [19] -->
m

<!-- b004323 | furniture | pages [19] -->
m

<!-- b004324 | furniture | pages [19] -->
m

<!-- b004325 | furniture | pages [19] -->
m

<!-- b004326 | furniture | pages [19] -->
m

<!-- b004327 | furniture | pages [19] -->
m

<!-- b004328 | furniture | pages [19] -->
m

<!-- b004329 | furniture | pages [19] -->
m

<!-- b004330 | furniture | pages [19] -->
m

<!-- b004331 | furniture | pages [19] -->
m

<!-- b004332 | furniture | pages [19] -->
m

<!-- b004333 | furniture | pages [19] -->
m

<!-- b004334 | furniture | pages [19] -->
m

<!-- b004335 | furniture | pages [19] -->
m

<!-- b004336 | furniture | pages [19] -->
m

<!-- b004337 | furniture | pages [19] -->
m

<!-- b004338 | furniture | pages [19] -->
m

<!-- b004339 | furniture | pages [19] -->
m

<!-- b004340 | furniture | pages [19] -->
m

<!-- b004341 | furniture | pages [19] -->
m

<!-- b004342 | furniture | pages [19] -->
m

<!-- b004343 | furniture | pages [19] -->
m

<!-- b004344 | furniture | pages [19] -->
m

<!-- b004345 | furniture | pages [19] -->
m

<!-- b004346 | furniture | pages [19] -->
m

<!-- b004347 | furniture | pages [19] -->
m

<!-- b004348 | furniture | pages [19] -->
m

<!-- b004349 | furniture | pages [19] -->
m

<!-- b004350 | furniture | pages [19] -->
m

<!-- b004351 | furniture | pages [19] -->
m

<!-- b004352 | furniture | pages [19] -->
m

<!-- b004353 | furniture | pages [19] -->
m

<!-- b004354 | furniture | pages [19] -->
m

<!-- b004355 | furniture | pages [19] -->
m

<!-- b004356 | furniture | pages [19] -->
m

<!-- b004357 | furniture | pages [19] -->
m

<!-- b004358 | furniture | pages [19] -->
m

<!-- b004359 | furniture | pages [19] -->
m

<!-- b004360 | furniture | pages [19] -->
m

<!-- b004361 | furniture | pages [19] -->
m

<!-- b004362 | furniture | pages [19] -->
m

<!-- b004363 | furniture | pages [19] -->
m

<!-- b004364 | furniture | pages [19] -->
m

<!-- b004365 | furniture | pages [19] -->
m

<!-- b004366 | furniture | pages [19] -->
m

<!-- b004367 | furniture | pages [19] -->
m

<!-- b004368 | furniture | pages [19] -->
m

<!-- b004369 | furniture | pages [19] -->
m

<!-- b004370 | furniture | pages [19] -->
m

<!-- b004371 | furniture | pages [19] -->
m

<!-- b004372 | furniture | pages [19] -->
m

<!-- b004373 | furniture | pages [19] -->
m

<!-- b004374 | furniture | pages [19] -->
m

<!-- b004375 | furniture | pages [19] -->
m

<!-- b004376 | furniture | pages [19] -->
m

<!-- b004377 | furniture | pages [19] -->
m

<!-- b004378 | furniture | pages [19] -->
m

<!-- b004379 | furniture | pages [19] -->
m

<!-- b004380 | furniture | pages [19] -->
m

<!-- b004381 | furniture | pages [19] -->
m

<!-- b004382 | furniture | pages [19] -->
m

<!-- b004383 | furniture | pages [19] -->
m

<!-- b004384 | furniture | pages [19] -->
m

<!-- b004385 | furniture | pages [19] -->
m

<!-- b004386 | furniture | pages [19] -->
m

<!-- b004387 | furniture | pages [19] -->
m

<!-- b004388 | furniture | pages [19] -->
m

<!-- b004389 | furniture | pages [19] -->
m

<!-- b004390 | furniture | pages [19] -->
m

<!-- b004391 | furniture | pages [19] -->
m

<!-- b004392 | furniture | pages [19] -->
m

<!-- b004393 | furniture | pages [19] -->
m

<!-- b004394 | furniture | pages [19] -->
m

<!-- b004395 | furniture | pages [19] -->
m

<!-- b004396 | furniture | pages [19] -->
m

<!-- b004397 | furniture | pages [19] -->
m

<!-- b004398 | furniture | pages [19] -->
m

<!-- b004399 | furniture | pages [19] -->
m

<!-- b004400 | furniture | pages [19] -->
m

<!-- b004401 | furniture | pages [19] -->
m

<!-- b004402 | furniture | pages [19] -->
m

<!-- b004403 | furniture | pages [19] -->
m

<!-- b004404 | furniture | pages [19] -->
m

<!-- b004405 | furniture | pages [19] -->
m

<!-- b004406 | furniture | pages [19] -->
m

<!-- b004407 | furniture | pages [19] -->
m

<!-- b004408 | furniture | pages [19] -->
m

<!-- b004409 | furniture | pages [19] -->
m

<!-- b004410 | furniture | pages [19] -->
m

<!-- b004411 | furniture | pages [19] -->
m

<!-- b004412 | furniture | pages [19] -->
m

<!-- b004413 | furniture | pages [19] -->
m

<!-- b004414 | furniture | pages [19] -->
m

<!-- b004415 | furniture | pages [19] -->
m

<!-- b004416 | furniture | pages [19] -->
m

<!-- b004417 | furniture | pages [19] -->
m

<!-- b004418 | furniture | pages [19] -->
m

<!-- b004419 | furniture | pages [19] -->
m

<!-- b004420 | furniture | pages [19] -->
m

<!-- b004421 | furniture | pages [19] -->
m

<!-- b004422 | furniture | pages [19] -->
m

<!-- b004423 | furniture | pages [19] -->
m

<!-- b004424 | furniture | pages [19] -->
m

<!-- b004425 | furniture | pages [19] -->
m

<!-- b004426 | furniture | pages [19] -->
m

<!-- b004427 | furniture | pages [19] -->
m

<!-- b004428 | furniture | pages [19] -->
m

<!-- b004429 | furniture | pages [19] -->
m

<!-- b004430 | furniture | pages [19] -->
m

<!-- b004431 | furniture | pages [19] -->
m

<!-- b004432 | furniture | pages [19] -->
m

<!-- b004433 | furniture | pages [19] -->
m

<!-- b004434 | furniture | pages [19] -->
m

<!-- b004435 | furniture | pages [19] -->
m

<!-- b004436 | furniture | pages [19] -->
m

<!-- b004437 | furniture | pages [19] -->
m

<!-- b004438 | furniture | pages [19] -->
m

<!-- b004439 | furniture | pages [19] -->
m

<!-- b004440 | furniture | pages [19] -->
m

<!-- b004441 | furniture | pages [19] -->
m

<!-- b004442 | furniture | pages [19] -->
m

<!-- b004443 | furniture | pages [19] -->
m

<!-- b004444 | furniture | pages [19] -->
m

<!-- b004445 | furniture | pages [19] -->
m

<!-- b004446 | furniture | pages [19] -->
m

<!-- b004447 | furniture | pages [19] -->
m

<!-- b004448 | furniture | pages [19] -->
m

<!-- b004449 | furniture | pages [19] -->
m

<!-- b004450 | furniture | pages [19] -->
m

<!-- b004451 | furniture | pages [19] -->
m

<!-- b004452 | furniture | pages [19] -->
m

<!-- b004453 | furniture | pages [19] -->
m

<!-- b004454 | furniture | pages [19] -->
m

<!-- b004455 | furniture | pages [19] -->
m

<!-- b004456 | furniture | pages [19] -->
m

<!-- b004457 | furniture | pages [19] -->
m

<!-- b004458 | furniture | pages [19] -->
m

<!-- b004459 | furniture | pages [19] -->
m

<!-- b004460 | furniture | pages [19] -->
m

<!-- b004461 | furniture | pages [19] -->
m

<!-- b004462 | furniture | pages [19] -->
m

<!-- b004463 | furniture | pages [19] -->
m

<!-- b004464 | furniture | pages [19] -->
m

<!-- b004465 | furniture | pages [19] -->
m

<!-- b004466 | furniture | pages [19] -->
m

<!-- b004467 | furniture | pages [19] -->
m

<!-- b004468 | furniture | pages [19] -->
m

<!-- b004469 | furniture | pages [19] -->
m

<!-- b004470 | furniture | pages [19] -->
m

<!-- b004471 | furniture | pages [19] -->
m

<!-- b004472 | furniture | pages [19] -->
m

<!-- b004473 | furniture | pages [19] -->
m

<!-- b004474 | furniture | pages [19] -->
m

<!-- b004475 | furniture | pages [19] -->
m

<!-- b004476 | furniture | pages [19] -->
m

<!-- b004477 | furniture | pages [19] -->
m

<!-- b004478 | furniture | pages [19] -->
m

<!-- b004479 | furniture | pages [19] -->
m

<!-- b004480 | furniture | pages [19] -->
m

<!-- b004481 | furniture | pages [19] -->
m

<!-- b004482 | furniture | pages [19] -->
m

<!-- b004483 | furniture | pages [19] -->
m

<!-- b004484 | furniture | pages [19] -->
m

<!-- b004485 | furniture | pages [19] -->
m

<!-- b004486 | furniture | pages [19] -->
m

<!-- b004487 | furniture | pages [19] -->
m

<!-- b004488 | furniture | pages [19] -->
m

<!-- b004489 | furniture | pages [19] -->
m

<!-- b004490 | furniture | pages [19] -->
m

<!-- b004491 | furniture | pages [19] -->
m

<!-- b004492 | furniture | pages [19] -->
m

<!-- b004493 | furniture | pages [19] -->
m

<!-- b004494 | furniture | pages [19] -->
m

<!-- b004495 | furniture | pages [19] -->
m

<!-- b004496 | furniture | pages [19] -->
m

<!-- b004497 | furniture | pages [19] -->
m

<!-- b004498 | furniture | pages [19] -->
m

<!-- b004499 | furniture | pages [19] -->
m

<!-- b004500 | furniture | pages [19] -->
m

<!-- b004501 | furniture | pages [19] -->
m

<!-- b004502 | furniture | pages [19] -->
m

<!-- b004503 | furniture | pages [19] -->
m

<!-- b004504 | furniture | pages [19] -->
m

<!-- b004505 | furniture | pages [19] -->
m

<!-- b004506 | furniture | pages [19] -->
m

<!-- b004507 | furniture | pages [19] -->
m

<!-- b004508 | furniture | pages [19] -->
m

<!-- b004509 | furniture | pages [19] -->
m

<!-- b004510 | furniture | pages [19] -->
m

<!-- b004511 | furniture | pages [19] -->
m

<!-- b004512 | furniture | pages [19] -->
m

<!-- b004513 | furniture | pages [19] -->
m

<!-- b004514 | furniture | pages [19] -->
m

<!-- b004515 | furniture | pages [19] -->
m

<!-- b004516 | furniture | pages [19] -->
m

<!-- b004517 | furniture | pages [19] -->
m

<!-- b004518 | furniture | pages [19] -->
m

<!-- b004519 | furniture | pages [19] -->
m

<!-- b004520 | furniture | pages [19] -->
m

<!-- b004521 | furniture | pages [19] -->
m

<!-- b004522 | furniture | pages [19] -->
m

<!-- b004523 | furniture | pages [19] -->
m

<!-- b004524 | furniture | pages [19] -->
m

<!-- b004525 | furniture | pages [19] -->
m

<!-- b004526 | furniture | pages [19] -->
m

<!-- b004527 | furniture | pages [19] -->
m

<!-- b004528 | furniture | pages [19] -->
m

<!-- b004529 | furniture | pages [19] -->
m

<!-- b004530 | furniture | pages [19] -->
m

<!-- b004531 | furniture | pages [19] -->
m

<!-- b004532 | furniture | pages [20] -->
Team #2510185

<!-- b004533 | furniture | pages [20] -->
Page 20 of 24

<!-- b004534 | prose | pages [20] -->
• Total_space reflects the growth potential in medal count.

<!-- b004535 | prose | pages [20] -->
Calculation Details:

<!-- b004536 | prose | pages [20] -->
• Total_trend:

<!-- b004537 | prose | pages [20] -->
Total_trend = pre_Total_2028 −Total_2024

<!-- b004538 | prose | pages [20] -->
(5) Total_2024 + 1

<!-- b004539 | prose | pages [20] -->
where pre_Total_2028 is the predicted medal count for the 2028 Los Angeles Olympics, and Total_2024 is the medal count from the 2024 Paris Olympics.

<!-- b004540 | prose | pages [20] -->
• Total_space:

<!-- b004541 | prose | pages [20] -->
Total_space =

<!-- b004542 | prose | pages [20] -->
1

<!-- b004543 | prose | pages [20] -->
Total_max

<!-- b004544 | prose | pages [20] -->
 j−1

<!-- b004545 | prose | pages [20] -->
−1 (6)

<!-- b004546 | prose | pages [20] -->
Total

<!-- b004547 | prose | pages [20] -->
where Total_max is the maximum medal count achieved in the event’s history, and j is the corresponding Olympic session. Additionally, the improvement potential is influenced by the presence of dominant nations in the event. Based on the historical Olympic data and factors influencing EPI, we recommend focusing on the following events:

<!-- b004548 | prose | pages [20] -->
• China: Men’s and women’s gymnastics, men’s swimming.

<!-- b004549 | prose | pages [20] -->
• Jamaica: Men’s and women’s athletics.

<!-- b004550 | prose | pages [20] -->
m

<!-- b004551 | prose | pages [20] -->
m

<!-- b004552 | prose | pages [20] -->
m

<!-- b004553 | prose | pages [20] -->
m

<!-- b004554 | prose | pages [20] -->
m

<!-- b004555 | prose | pages [20] -->
m

<!-- b004556 | prose | pages [20] -->
m

<!-- b004557 | prose | pages [20] -->
m

<!-- b004558 | prose | pages [20] -->
m

<!-- b004559 | prose | pages [20] -->
m

<!-- b004560 | prose | pages [20] -->
m

<!-- b004561 | prose | pages [20] -->
m

<!-- b004562 | prose | pages [20] -->
m

<!-- b004563 | prose | pages [20] -->
m

<!-- b004564 | prose | pages [20] -->
m

<!-- b004565 | prose | pages [20] -->
m

<!-- b004566 | prose | pages [20] -->
m

<!-- b004567 | prose | pages [20] -->
m

<!-- b004568 | prose | pages [20] -->
m

<!-- b004569 | prose | pages [20] -->
m

<!-- b004570 | prose | pages [20] -->
m

<!-- b004571 | prose | pages [20] -->
m

<!-- b004572 | prose | pages [20] -->
m

<!-- b004573 | prose | pages [20] -->
m

<!-- b004574 | prose | pages [20] -->
m

<!-- b004575 | prose | pages [20] -->
m

<!-- b004576 | prose | pages [20] -->
m

<!-- b004577 | prose | pages [20] -->
m

<!-- b004578 | prose | pages [20] -->
m

<!-- b004579 | prose | pages [20] -->
m

<!-- b004580 | prose | pages [20] -->
m

<!-- b004581 | prose | pages [20] -->
m

<!-- b004582 | prose | pages [20] -->
m

<!-- b004583 | prose | pages [20] -->
m

<!-- b004584 | prose | pages [20] -->
m

<!-- b004585 | prose | pages [20] -->
m

<!-- b004586 | prose | pages [20] -->
m

<!-- b004587 | prose | pages [20] -->
m

<!-- b004588 | prose | pages [20] -->
m

<!-- b004589 | prose | pages [20] -->
m

<!-- b004590 | prose | pages [20] -->
m

<!-- b004591 | prose | pages [20] -->
m

<!-- b004592 | prose | pages [20] -->
m

<!-- b004593 | prose | pages [20] -->
m

<!-- b004594 | prose | pages [20] -->
m

<!-- b004595 | prose | pages [20] -->
m

<!-- b004596 | prose | pages [20] -->
m

<!-- b004597 | prose | pages [20] -->
m

<!-- b004598 | prose | pages [20] -->
m

<!-- b004599 | prose | pages [20] -->
m

<!-- b004600 | prose | pages [20] -->
m

<!-- b004601 | prose | pages [20] -->
m

<!-- b004602 | prose | pages [20] -->
m

<!-- b004603 | prose | pages [20] -->
m

<!-- b004604 | prose | pages [20] -->
m

<!-- b004605 | prose | pages [20] -->
m

<!-- b004606 | prose | pages [20] -->
m

<!-- b004607 | prose | pages [20] -->
m

<!-- b004608 | prose | pages [20] -->
m

<!-- b004609 | prose | pages [20] -->
m

<!-- b004610 | prose | pages [20] -->
m

<!-- b004611 | prose | pages [20] -->
m

<!-- b004612 | prose | pages [20] -->
m

<!-- b004613 | prose | pages [20] -->
m

<!-- b004614 | prose | pages [20] -->
m

<!-- b004615 | prose | pages [20] -->
m

<!-- b004616 | prose | pages [20] -->
m

<!-- b004617 | prose | pages [20] -->
m

<!-- b004618 | prose | pages [20] -->
m

<!-- b004619 | prose | pages [20] -->
m

<!-- b004620 | prose | pages [20] -->
m

<!-- b004621 | prose | pages [20] -->
m

<!-- b004622 | prose | pages [20] -->
m

<!-- b004623 | prose | pages [20] -->
m

<!-- b004624 | prose | pages [20] -->
m

<!-- b004625 | prose | pages [20] -->
m

<!-- b004626 | prose | pages [20] -->
m

<!-- b004627 | prose | pages [20] -->
m

<!-- b004628 | prose | pages [20] -->
m

<!-- b004629 | prose | pages [20] -->
m

<!-- b004630 | prose | pages [20] -->
m

<!-- b004631 | prose | pages [20] -->
m

<!-- b004632 | prose | pages [20] -->
m

<!-- b004633 | prose | pages [20] -->
m

<!-- b004634 | prose | pages [20] -->
m

<!-- b004635 | prose | pages [20] -->
m

<!-- b004636 | prose | pages [20] -->
m

<!-- b004637 | prose | pages [20] -->
m

<!-- b004638 | prose | pages [20] -->
m

<!-- b004639 | prose | pages [20] -->
m

<!-- b004640 | prose | pages [20] -->
m

<!-- b004641 | prose | pages [20] -->
m

<!-- b004642 | prose | pages [20] -->
m

<!-- b004643 | prose | pages [20] -->
m

<!-- b004644 | prose | pages [20] -->
m

<!-- b004645 | prose | pages [20] -->
m

<!-- b004646 | prose | pages [20] -->
m

<!-- b004647 | prose | pages [20] -->
m

<!-- b004648 | prose | pages [20] -->
m

<!-- b004649 | prose | pages [20] -->
m

<!-- b004650 | prose | pages [20] -->
m

<!-- b004651 | prose | pages [20] -->
m

<!-- b004652 | prose | pages [20] -->
m

<!-- b004653 | prose | pages [20] -->
m

<!-- b004654 | prose | pages [20] -->
m

<!-- b004655 | prose | pages [20] -->
m

<!-- b004656 | prose | pages [20] -->
m

<!-- b004657 | prose | pages [20] -->
m

<!-- b004658 | prose | pages [20] -->
• Germany: Men’s shooting, men’s and women’s swimming.

<!-- b004659 | prose | pages [20] -->
4.3.2

<!-- b004660 | heading | pages [20] -->
Post-investment Results

<!-- b004661 | prose | pages [20] -->
m

<!-- b004662 | prose | pages [20] -->
m

<!-- b004663 | prose | pages [20] -->
m

<!-- b004664 | prose | pages [20] -->
m

<!-- b004665 | prose | pages [20] -->
m

<!-- b004666 | prose | pages [20] -->
m

<!-- b004667 | prose | pages [20] -->
m

<!-- b004668 | prose | pages [20] -->
m

<!-- b004669 | prose | pages [20] -->
m

<!-- b004670 | prose | pages [20] -->
m

<!-- b004671 | prose | pages [20] -->
m

<!-- b004672 | prose | pages [20] -->
m

<!-- b004673 | prose | pages [20] -->
m

<!-- b004674 | prose | pages [20] -->
m

<!-- b004675 | prose | pages [20] -->
m

<!-- b004676 | prose | pages [20] -->
m

<!-- b004677 | prose | pages [20] -->
m

<!-- b004678 | prose | pages [20] -->
m

<!-- b004679 | prose | pages [20] -->
m

<!-- b004680 | prose | pages [20] -->
m

<!-- b004681 | prose | pages [20] -->
m

<!-- b004682 | prose | pages [20] -->
m

<!-- b004683 | prose | pages [20] -->
m

<!-- b004684 | prose | pages [20] -->
m

<!-- b004685 | prose | pages [20] -->
m

<!-- b004686 | prose | pages [20] -->
m

<!-- b004687 | prose | pages [20] -->
m

<!-- b004688 | prose | pages [20] -->
m

<!-- b004689 | prose | pages [20] -->
m

<!-- b004690 | prose | pages [20] -->
m

<!-- b004691 | prose | pages [20] -->
m

<!-- b004692 | prose | pages [20] -->
m

<!-- b004693 | prose | pages [20] -->
m

<!-- b004694 | prose | pages [20] -->
m

<!-- b004695 | prose | pages [20] -->
m

<!-- b004696 | prose | pages [20] -->
m

<!-- b004697 | prose | pages [20] -->
m

<!-- b004698 | prose | pages [20] -->
m

<!-- b004699 | prose | pages [20] -->
m

<!-- b004700 | prose | pages [20] -->
m

<!-- b004701 | prose | pages [20] -->
m

<!-- b004702 | prose | pages [20] -->
m

<!-- b004703 | prose | pages [20] -->
m

<!-- b004704 | prose | pages [20] -->
m

<!-- b004705 | prose | pages [20] -->
m

<!-- b004706 | prose | pages [20] -->
m

<!-- b004707 | prose | pages [20] -->
m

<!-- b004708 | prose | pages [20] -->
m

<!-- b004709 | prose | pages [20] -->
m

<!-- b004710 | prose | pages [20] -->
m

<!-- b004711 | prose | pages [20] -->
m

<!-- b004712 | prose | pages [20] -->
m

<!-- b004713 | prose | pages [20] -->
m

<!-- b004714 | prose | pages [20] -->
m

<!-- b004715 | prose | pages [20] -->
m

<!-- b004716 | prose | pages [20] -->
m

<!-- b004717 | prose | pages [20] -->
m

<!-- b004718 | prose | pages [20] -->
m

<!-- b004719 | prose | pages [20] -->
m

<!-- b004720 | prose | pages [20] -->
m

<!-- b004721 | prose | pages [20] -->
m

<!-- b004722 | prose | pages [20] -->
m

<!-- b004723 | prose | pages [20] -->
m

<!-- b004724 | prose | pages [20] -->
m

<!-- b004725 | prose | pages [20] -->
m

<!-- b004726 | prose | pages [20] -->
m

<!-- b004727 | prose | pages [20] -->
m

<!-- b004728 | prose | pages [20] -->
m

<!-- b004729 | prose | pages [20] -->
m

<!-- b004730 | prose | pages [20] -->
m

<!-- b004731 | prose | pages [20] -->
m

<!-- b004732 | prose | pages [20] -->
m

<!-- b004733 | prose | pages [20] -->
m

<!-- b004734 | prose | pages [20] -->
m

<!-- b004735 | prose | pages [20] -->
m

<!-- b004736 | prose | pages [20] -->
m

<!-- b004737 | prose | pages [20] -->
m

<!-- b004738 | prose | pages [20] -->
m

<!-- b004739 | prose | pages [20] -->
m

<!-- b004740 | prose | pages [20] -->
m

<!-- b004741 | prose | pages [20] -->
m

<!-- b004742 | prose | pages [20] -->
m

<!-- b004743 | prose | pages [20] -->
m

<!-- b004744 | prose | pages [20] -->
m

<!-- b004745 | prose | pages [20] -->
m

<!-- b004746 | prose | pages [20] -->
m

<!-- b004747 | prose | pages [20] -->
m

<!-- b004748 | prose | pages [20] -->
m

<!-- b004749 | prose | pages [20] -->
m

<!-- b004750 | prose | pages [20] -->
m

<!-- b004751 | prose | pages [20] -->
m

<!-- b004752 | prose | pages [20] -->
m

<!-- b004753 | prose | pages [20] -->
m

<!-- b004754 | prose | pages [20] -->
m

<!-- b004755 | prose | pages [20] -->
m

<!-- b004756 | prose | pages [20] -->
m

<!-- b004757 | prose | pages [20] -->
m

<!-- b004758 | prose | pages [20] -->
m

<!-- b004759 | prose | pages [20] -->
m

<!-- b004760 | prose | pages [20] -->
m

<!-- b004761 | prose | pages [20] -->
m

<!-- b004762 | prose | pages [20] -->
m

<!-- b004763 | prose | pages [20] -->
m

<!-- b004764 | prose | pages [20] -->
m

<!-- b004765 | prose | pages [20] -->
m

<!-- b004766 | prose | pages [20] -->
m

<!-- b004767 | prose | pages [20] -->
m

<!-- b004768 | prose | pages [20] -->
m

<!-- b004769 | prose | pages [20] -->
m

<!-- b004770 | prose | pages [20] -->
m

<!-- b004771 | prose | pages [20] -->
m

<!-- b004772 | prose | pages [20] -->
m

<!-- b004773 | prose | pages [20] -->
m

<!-- b004774 | prose | pages [20] -->
m

<!-- b004775 | prose | pages [20] -->
m

<!-- b004776 | prose | pages [20] -->
m

<!-- b004777 | prose | pages [20] -->
m

<!-- b004778 | prose | pages [20] -->
m

<!-- b004779 | prose | pages [20] -->
m

<!-- b004780 | prose | pages [20] -->
m

<!-- b004781 | prose | pages [20] -->
m

<!-- b004782 | prose | pages [20] -->
m

<!-- b004783 | prose | pages [20] -->
m

<!-- b004784 | prose | pages [20] -->
m

<!-- b004785 | prose | pages [20] -->
m

<!-- b004786 | prose | pages [20] -->
m

<!-- b004787 | prose | pages [20] -->
m

<!-- b004788 | prose | pages [20] -->
m

<!-- b004789 | prose | pages [20] -->
m

<!-- b004790 | prose | pages [20] -->
m

<!-- b004791 | prose | pages [20] -->
m

<!-- b004792 | prose | pages [20] -->
m

<!-- b004793 | prose | pages [20] -->
m

<!-- b004794 | prose | pages [20] -->
m

<!-- b004795 | prose | pages [20] -->
m

<!-- b004796 | prose | pages [20] -->
m

<!-- b004797 | prose | pages [20] -->
m

<!-- b004798 | prose | pages [20] -->
m

<!-- b004799 | prose | pages [20] -->
m

<!-- b004800 | prose | pages [20] -->
m

<!-- b004801 | prose | pages [20] -->
m

<!-- b004802 | prose | pages [20] -->
m

<!-- b004803 | prose | pages [20] -->
m

<!-- b004804 | prose | pages [20] -->
m

<!-- b004805 | prose | pages [20] -->
m

<!-- b004806 | prose | pages [20] -->
m

<!-- b004807 | prose | pages [20] -->
m

<!-- b004808 | prose | pages [20] -->
m

<!-- b004809 | prose | pages [20] -->
m

<!-- b004810 | prose | pages [20] -->
m

<!-- b004811 | prose | pages [20] -->
m

<!-- b004812 | prose | pages [20] -->
m

<!-- b004813 | prose | pages [20] -->
m

<!-- b004814 | prose | pages [20] -->
m

<!-- b004815 | prose | pages [20] -->
m

<!-- b004816 | prose | pages [20] -->
m

<!-- b004817 | prose | pages [20] -->
m

<!-- b004818 | prose | pages [20] -->
m

<!-- b004819 | prose | pages [20] -->
m

<!-- b004820 | prose | pages [20] -->
m

<!-- b004821 | prose | pages [20] -->
m

<!-- b004822 | prose | pages [20] -->
m

<!-- b004823 | prose | pages [20] -->
m

<!-- b004824 | prose | pages [20] -->
m

<!-- b004825 | prose | pages [20] -->
m

<!-- b004826 | prose | pages [20] -->
m

<!-- b004827 | prose | pages [20] -->
m

<!-- b004828 | prose | pages [20] -->
m

<!-- b004829 | prose | pages [20] -->
m

<!-- b004830 | prose | pages [20] -->
m

<!-- b004831 | prose | pages [20] -->
m

<!-- b004832 | prose | pages [20] -->
m

<!-- b004833 | prose | pages [20] -->
m

<!-- b004834 | prose | pages [20] -->
m

<!-- b004835 | prose | pages [20] -->
m

<!-- b004836 | prose | pages [20] -->
m

<!-- b004837 | prose | pages [20] -->
m

<!-- b004838 | prose | pages [20] -->
m

<!-- b004839 | prose | pages [20] -->
m

<!-- b004840 | prose | pages [20] -->
m

<!-- b004841 | prose | pages [20] -->
m

<!-- b004842 | prose | pages [20] -->
m

<!-- b004843 | prose | pages [20] -->
m

<!-- b004844 | prose | pages [20] -->
m

<!-- b004845 | prose | pages [20] -->
m

<!-- b004846 | prose | pages [20] -->
m

<!-- b004847 | prose | pages [20] -->
m

<!-- b004848 | prose | pages [20] -->
m

<!-- b004849 | prose | pages [20] -->
m

<!-- b004850 | prose | pages [20] -->
m

<!-- b004851 | prose | pages [20] -->
m

<!-- b004852 | prose | pages [20] -->
m

<!-- b004853 | prose | pages [20] -->
m

<!-- b004854 | prose | pages [20] -->
m

<!-- b004855 | prose | pages [20] -->
m

<!-- b004856 | prose | pages [20] -->
m

<!-- b004857 | prose | pages [20] -->
m

<!-- b004858 | prose | pages [20] -->
m

<!-- b004859 | prose | pages [20] -->
m

<!-- b004860 | prose | pages [20] -->
m

<!-- b004861 | prose | pages [20] -->
m

<!-- b004862 | prose | pages [20] -->
m

<!-- b004863 | prose | pages [20] -->
m

<!-- b004864 | prose | pages [20] -->
m

<!-- b004865 | prose | pages [20] -->
m

<!-- b004866 | prose | pages [20] -->
m

<!-- b004867 | prose | pages [20] -->
m

<!-- b004868 | prose | pages [20] -->
m

<!-- b004869 | prose | pages [20] -->
m

<!-- b004870 | prose | pages [20] -->
m

<!-- b004871 | prose | pages [20] -->
m

<!-- b004872 | prose | pages [20] -->
m

<!-- b004873 | prose | pages [20] -->
m

<!-- b004874 | prose | pages [20] -->
m

<!-- b004875 | prose | pages [20] -->
m

<!-- b004876 | prose | pages [20] -->
m

<!-- b004877 | prose | pages [20] -->
m

<!-- b004878 | prose | pages [20] -->
m

<!-- b004879 | prose | pages [20] -->
m

<!-- b004880 | prose | pages [20] -->
m

<!-- b004881 | prose | pages [20] -->
m

<!-- b004882 | prose | pages [20] -->
m

<!-- b004883 | prose | pages [20] -->
m

<!-- b004884 | prose | pages [20] -->
m

<!-- b004885 | prose | pages [20] -->
m

<!-- b004886 | prose | pages [20] -->
m

<!-- b004887 | prose | pages [20] -->
m

<!-- b004888 | prose | pages [20] -->
m

<!-- b004889 | prose | pages [20] -->
m

<!-- b004890 | prose | pages [20] -->
m

<!-- b004891 | prose | pages [20] -->
m

<!-- b004892 | prose | pages [20] -->
m

<!-- b004893 | prose | pages [20] -->
m

<!-- b004894 | prose | pages [20] -->
m

<!-- b004895 | prose | pages [20] -->
m

<!-- b004896 | prose | pages [20] -->
m

<!-- b004897 | prose | pages [20] -->
m

<!-- b004898 | prose | pages [20] -->
m

<!-- b004899 | prose | pages [20] -->
m

<!-- b004900 | prose | pages [20] -->
m

<!-- b004901 | prose | pages [20] -->
m

<!-- b004902 | prose | pages [20] -->
m

<!-- b004903 | prose | pages [20] -->
m

<!-- b004904 | prose | pages [20] -->
m

<!-- b004905 | prose | pages [20] -->
m

<!-- b004906 | prose | pages [20] -->
m

<!-- b004907 | prose | pages [20] -->
m

<!-- b004908 | prose | pages [20] -->
m

<!-- b004909 | prose | pages [20] -->
m

<!-- b004910 | prose | pages [20] -->
m

<!-- b004911 | prose | pages [20] -->
m

<!-- b004912 | prose | pages [20] -->
m

<!-- b004913 | prose | pages [20] -->
m

<!-- b004914 | prose | pages [20] -->
m

<!-- b004915 | prose | pages [20] -->
m

<!-- b004916 | prose | pages [20] -->
m

<!-- b004917 | prose | pages [20] -->
m

<!-- b004918 | prose | pages [20] -->
m

<!-- b004919 | prose | pages [20] -->
m

<!-- b004920 | prose | pages [20] -->
m

<!-- b004921 | prose | pages [20] -->
m

<!-- b004922 | prose | pages [20] -->
m

<!-- b004923 | prose | pages [20] -->
m

<!-- b004924 | prose | pages [20] -->
m

<!-- b004925 | prose | pages [20] -->
m

<!-- b004926 | prose | pages [20] -->
m

<!-- b004927 | prose | pages [20] -->
m

<!-- b004928 | prose | pages [20] -->
m

<!-- b004929 | prose | pages [20] -->
m

<!-- b004930 | prose | pages [20] -->
m

<!-- b004931 | prose | pages [20] -->
m

<!-- b004932 | prose | pages [20] -->
m

<!-- b004933 | prose | pages [20] -->
m

<!-- b004934 | prose | pages [20] -->
m

<!-- b004935 | prose | pages [20] -->
m

<!-- b004936 | prose | pages [20] -->
m

<!-- b004937 | prose | pages [20] -->
m

<!-- b004938 | prose | pages [20] -->
m

<!-- b004939 | prose | pages [20] -->
m

<!-- b004940 | prose | pages [20] -->
m

<!-- b004941 | prose | pages [20] -->
m

<!-- b004942 | prose | pages [20] -->
m

<!-- b004943 | prose | pages [20] -->
m

<!-- b004944 | prose | pages [20] -->
m

<!-- b004945 | prose | pages [20] -->
m

<!-- b004946 | prose | pages [20] -->
m

<!-- b004947 | prose | pages [20] -->
m

<!-- b004948 | prose | pages [20] -->
m

<!-- b004949 | prose | pages [20] -->
m

<!-- b004950 | prose | pages [20] -->
m

<!-- b004951 | prose | pages [20] -->
m

<!-- b004952 | prose | pages [20] -->
m

<!-- b004953 | prose | pages [20] -->
m

<!-- b004954 | prose | pages [20] -->
m

<!-- b004955 | prose | pages [20] -->
m

<!-- b004956 | prose | pages [20] -->
m

<!-- b004957 | prose | pages [20] -->
m

<!-- b004958 | prose | pages [20] -->
m

<!-- b004959 | prose | pages [20] -->
m

<!-- b004960 | prose | pages [20] -->
m

<!-- b004961 | prose | pages [20] -->
m

<!-- b004962 | prose | pages [20] -->
m

<!-- b004963 | prose | pages [20] -->
m

<!-- b004964 | prose | pages [20] -->
m

<!-- b004965 | prose | pages [20] -->
m

<!-- b004966 | prose | pages [20] -->
m

<!-- b004967 | prose | pages [20] -->
m

<!-- b004968 | prose | pages [20] -->
m

<!-- b004969 | prose | pages [20] -->
m

<!-- b004970 | prose | pages [20] -->
m

<!-- b004971 | prose | pages [20] -->
m

<!-- b004972 | prose | pages [20] -->
m

<!-- b004973 | prose | pages [20] -->
m

<!-- b004974 | prose | pages [20] -->
m

<!-- b004975 | prose | pages [20] -->
m

<!-- b004976 | prose | pages [20] -->
m

<!-- b004977 | prose | pages [20] -->
m

<!-- b004978 | prose | pages [20] -->
m

<!-- b004979 | prose | pages [20] -->
m

<!-- b004980 | prose | pages [20] -->
m

<!-- b004981 | prose | pages [20] -->
m

<!-- b004982 | prose | pages [20] -->
m

<!-- b004983 | prose | pages [20] -->
m

<!-- b004984 | prose | pages [20] -->
m

<!-- b004985 | prose | pages [20] -->
m

<!-- b004986 | prose | pages [20] -->
m

<!-- b004987 | prose | pages [20] -->
m

<!-- b004988 | prose | pages [20] -->
m

<!-- b004989 | prose | pages [20] -->
m

<!-- b004990 | prose | pages [20] -->
m

<!-- b004991 | prose | pages [20] -->
m

<!-- b004992 | prose | pages [20] -->
m

<!-- b004993 | prose | pages [20] -->
m

<!-- b004994 | prose | pages [20] -->
m

<!-- b004995 | prose | pages [20] -->
m

<!-- b004996 | prose | pages [20] -->
m

<!-- b004997 | prose | pages [20] -->
m

<!-- b004998 | prose | pages [20] -->
m

<!-- b004999 | prose | pages [20] -->
m

<!-- b005000 | prose | pages [20] -->
m

<!-- b005001 | prose | pages [20] -->
m

<!-- b005002 | prose | pages [20] -->
m

<!-- b005003 | prose | pages [20] -->
m

<!-- b005004 | prose | pages [20] -->
m

<!-- b005005 | prose | pages [20] -->
m

<!-- b005006 | prose | pages [20] -->
m

<!-- b005007 | prose | pages [20] -->
m

<!-- b005008 | prose | pages [20] -->
m

<!-- b005009 | prose | pages [20] -->
m

<!-- b005010 | prose | pages [20] -->
m

<!-- b005011 | prose | pages [20] -->
m

<!-- b005012 | prose | pages [20] -->
m

<!-- b005013 | prose | pages [20] -->
m

<!-- b005014 | prose | pages [20] -->
m

<!-- b005015 | prose | pages [20] -->
m

<!-- b005016 | prose | pages [20] -->
m

<!-- b005017 | prose | pages [20] -->
m

<!-- b005018 | prose | pages [20] -->
m

<!-- b005019 | prose | pages [20] -->
m

<!-- b005020 | prose | pages [20] -->
m

<!-- b005021 | prose | pages [20] -->
m

<!-- b005022 | prose | pages [20] -->
m

<!-- b005023 | prose | pages [20] -->
m

<!-- b005024 | prose | pages [20] -->
m

<!-- b005025 | prose | pages [20] -->
m

<!-- b005026 | prose | pages [20] -->
m

<!-- b005027 | prose | pages [20] -->
m

<!-- b005028 | prose | pages [20] -->
m

<!-- b005029 | prose | pages [20] -->
m

<!-- b005030 | prose | pages [20] -->
m

<!-- b005031 | prose | pages [20] -->
m

<!-- b005032 | prose | pages [20] -->
m

<!-- b005033 | prose | pages [20] -->
m

<!-- b005034 | prose | pages [20] -->
m

<!-- b005035 | prose | pages [20] -->
m

<!-- b005036 | prose | pages [20] -->
m

<!-- b005037 | prose | pages [20] -->
m

<!-- b005038 | prose | pages [20] -->
m

<!-- b005039 | prose | pages [20] -->
m

<!-- b005040 | prose | pages [20] -->
m

<!-- b005041 | prose | pages [20] -->
m

<!-- b005042 | prose | pages [20] -->
m

<!-- b005043 | prose | pages [20] -->
m

<!-- b005044 | prose | pages [20] -->
m

<!-- b005045 | prose | pages [20] -->
m

<!-- b005046 | prose | pages [20] -->
m

<!-- b005047 | prose | pages [20] -->
m

<!-- b005048 | prose | pages [20] -->
m

<!-- b005049 | prose | pages [20] -->
m

<!-- b005050 | prose | pages [20] -->
m

<!-- b005051 | prose | pages [20] -->
m

<!-- b005052 | prose | pages [20] -->
m

<!-- b005053 | prose | pages [20] -->
m

<!-- b005054 | prose | pages [20] -->
m

<!-- b005055 | prose | pages [20] -->
m

<!-- b005056 | prose | pages [20] -->
m

<!-- b005057 | prose | pages [20] -->
m

<!-- b005058 | prose | pages [20] -->
m

<!-- b005059 | prose | pages [20] -->
m

<!-- b005060 | prose | pages [20] -->
m

<!-- b005061 | prose | pages [20] -->
m

<!-- b005062 | prose | pages [20] -->
m

<!-- b005063 | prose | pages [20] -->
m

<!-- b005064 | prose | pages [20] -->
m

<!-- b005065 | prose | pages [20] -->
m

<!-- b005066 | prose | pages [20] -->
m

<!-- b005067 | prose | pages [20] -->
m

<!-- b005068 | prose | pages [20] -->
m

<!-- b005069 | prose | pages [20] -->
m

<!-- b005070 | prose | pages [20] -->
m

<!-- b005071 | prose | pages [20] -->
m

<!-- b005072 | prose | pages [20] -->
m

<!-- b005073 | prose | pages [20] -->
m

<!-- b005074 | prose | pages [20] -->
m

<!-- b005075 | prose | pages [20] -->
m

<!-- b005076 | prose | pages [20] -->
m

<!-- b005077 | prose | pages [20] -->
m

<!-- b005078 | prose | pages [20] -->
m

<!-- b005079 | prose | pages [20] -->
m

<!-- b005080 | prose | pages [20] -->
m

<!-- b005081 | prose | pages [20] -->
m

<!-- b005082 | prose | pages [20] -->
m

<!-- b005083 | prose | pages [20] -->
m

<!-- b005084 | prose | pages [20] -->
m

<!-- b005085 | prose | pages [20] -->
m

<!-- b005086 | prose | pages [20] -->
m

<!-- b005087 | prose | pages [20] -->
m

<!-- b005088 | prose | pages [20] -->
m

<!-- b005089 | prose | pages [20] -->
m

<!-- b005090 | prose | pages [20] -->
m

<!-- b005091 | prose | pages [20] -->
m

<!-- b005092 | prose | pages [20] -->
m

<!-- b005093 | prose | pages [20] -->
m

<!-- b005094 | prose | pages [20] -->
m

<!-- b005095 | prose | pages [20] -->
m

<!-- b005096 | prose | pages [20] -->
m

<!-- b005097 | prose | pages [20] -->
m

<!-- b005098 | prose | pages [20] -->
m

<!-- b005099 | prose | pages [20] -->
m

<!-- b005100 | prose | pages [20] -->
m

<!-- b005101 | prose | pages [20] -->
m

<!-- b005102 | prose | pages [20] -->
m

<!-- b005103 | prose | pages [20] -->
m

<!-- b005104 | prose | pages [20] -->
m

<!-- b005105 | prose | pages [20] -->
m

<!-- b005106 | prose | pages [20] -->
m

<!-- b005107 | prose | pages [20] -->
m

<!-- b005108 | prose | pages [20] -->
m

<!-- b005109 | prose | pages [20] -->
m

<!-- b005110 | prose | pages [20] -->
m

<!-- b005111 | prose | pages [20] -->
m

<!-- b005112 | prose | pages [20] -->
m

<!-- b005113 | prose | pages [20] -->
m

<!-- b005114 | prose | pages [20] -->
m

<!-- b005115 | prose | pages [20] -->
m

<!-- b005116 | prose | pages [20] -->
m

<!-- b005117 | prose | pages [20] -->
m

<!-- b005118 | prose | pages [20] -->
m

<!-- b005119 | prose | pages [20] -->
Our prediction for the above-selected sport is as is shown in Table 14.

<!-- b005120 | prose | pages [20] -->
m

<!-- b005121 | prose | pages [20] -->
m

<!-- b005122 | prose | pages [20] -->
m

<!-- b005123 | prose | pages [20] -->
m

<!-- b005124 | prose | pages [20] -->
m

<!-- b005125 | prose | pages [20] -->
m

<!-- b005126 | prose | pages [20] -->
m

<!-- b005127 | prose | pages [20] -->
m

<!-- b005128 | prose | pages [20] -->
m

<!-- b005129 | prose | pages [20] -->
m

<!-- b005130 | prose | pages [20] -->
m

<!-- b005131 | prose | pages [20] -->
m

<!-- b005132 | prose | pages [20] -->
m

<!-- b005133 | prose | pages [20] -->
m

<!-- b005134 | prose | pages [20] -->
m

<!-- b005135 | prose | pages [20] -->
m

<!-- b005136 | prose | pages [20] -->
m

<!-- b005137 | prose | pages [20] -->
m

<!-- b005138 | prose | pages [20] -->
m

<!-- b005139 | prose | pages [20] -->
m

<!-- b005140 | prose | pages [20] -->
m

<!-- b005141 | prose | pages [20] -->
m

<!-- b005142 | prose | pages [20] -->
m

<!-- b005143 | prose | pages [20] -->
m

<!-- b005144 | prose | pages [20] -->
m

<!-- b005145 | prose | pages [20] -->
m

<!-- b005146 | prose | pages [20] -->
m

<!-- b005147 | prose | pages [20] -->
m

<!-- b005148 | prose | pages [20] -->
m

<!-- b005149 | prose | pages [20] -->
m

<!-- b005150 | prose | pages [20] -->
m

<!-- b005151 | prose | pages [20] -->
m

<!-- b005152 | prose | pages [20] -->
m

<!-- b005153 | prose | pages [20] -->
m

<!-- b005154 | prose | pages [20] -->
m

<!-- b005155 | prose | pages [20] -->
m

<!-- b005156 | prose | pages [20] -->
m

<!-- b005157 | prose | pages [20] -->
m

<!-- b005158 | prose | pages [20] -->
m

<!-- b005159 | prose | pages [20] -->
m

<!-- b005160 | prose | pages [20] -->
m

<!-- b005161 | prose | pages [20] -->
m

<!-- b005162 | prose | pages [20] -->
m

<!-- b005163 | prose | pages [20] -->
m

<!-- b005164 | prose | pages [20] -->
m

<!-- b005165 | prose | pages [20] -->
m

<!-- b005166 | prose | pages [20] -->
m

<!-- b005167 | prose | pages [20] -->
m

<!-- b005168 | prose | pages [20] -->
m

<!-- b005169 | prose | pages [20] -->
m

<!-- b005170 | prose | pages [20] -->
m

<!-- b005171 | prose | pages [20] -->
m

<!-- b005172 | prose | pages [20] -->
m

<!-- b005173 | prose | pages [20] -->
m

<!-- b005174 | prose | pages [20] -->
m

<!-- b005175 | prose | pages [20] -->
m

<!-- b005176 | prose | pages [20] -->
m

<!-- b005177 | prose | pages [20] -->
m

<!-- b005178 | prose | pages [20] -->
m

<!-- b005179 | prose | pages [20] -->
m

<!-- b005180 | prose | pages [20] -->
m

<!-- b005181 | prose | pages [20] -->
m

<!-- b005182 | prose | pages [20] -->
m

<!-- b005183 | prose | pages [20] -->
m

<!-- b005184 | prose | pages [20] -->
m

<!-- b005185 | prose | pages [20] -->
m

<!-- b005186 | prose | pages [20] -->
m

<!-- b005187 | prose | pages [20] -->
m

<!-- b005188 | prose | pages [20] -->
m

<!-- b005189 | prose | pages [20] -->
m

<!-- b005190 | prose | pages [20] -->
m

<!-- b005191 | prose | pages [20] -->
m

<!-- b005192 | prose | pages [20] -->
m

<!-- b005193 | prose | pages [20] -->
m

<!-- b005194 | prose | pages [20] -->
m

<!-- b005195 | prose | pages [20] -->
m

<!-- b005196 | prose | pages [20] -->
m

<!-- b005197 | prose | pages [20] -->
m

<!-- b005198 | prose | pages [20] -->
m

<!-- b005199 | prose | pages [20] -->
m

<!-- b005200 | prose | pages [20] -->
m

<!-- b005201 | prose | pages [20] -->
m

<!-- b005202 | prose | pages [20] -->
m

<!-- b005203 | prose | pages [20] -->
m

<!-- b005204 | prose | pages [20] -->
m

<!-- b005205 | prose | pages [20] -->
m

<!-- b005206 | prose | pages [20] -->
m

<!-- b005207 | prose | pages [20] -->
m

<!-- b005208 | prose | pages [20] -->
m

<!-- b005209 | prose | pages [20] -->
m

<!-- b005210 | prose | pages [20] -->
m

<!-- b005211 | prose | pages [20] -->
m

<!-- b005212 | prose | pages [20] -->
m

<!-- b005213 | prose | pages [20] -->
m

<!-- b005214 | prose | pages [20] -->
m

<!-- b005215 | prose | pages [20] -->
m

<!-- b005216 | prose | pages [20] -->
m

<!-- b005217 | prose | pages [20] -->
m

<!-- b005218 | prose | pages [20] -->
m

<!-- b005219 | prose | pages [20] -->
m

<!-- b005220 | prose | pages [20] -->
m

<!-- b005221 | prose | pages [20] -->
m

<!-- b005222 | prose | pages [20] -->
m

<!-- b005223 | prose | pages [20] -->
m

<!-- b005224 | prose | pages [20] -->
m

<!-- b005225 | prose | pages [20] -->
m

<!-- b005226 | prose | pages [20] -->
m

<!-- b005227 | prose | pages [20] -->
m

<!-- b005228 | prose | pages [20] -->
m

<!-- b005229 | prose | pages [20] -->
m

<!-- b005230 | prose | pages [20] -->
m

<!-- b005231 | prose | pages [20] -->
m

<!-- b005232 | prose | pages [20] -->
m

<!-- b005233 | prose | pages [20] -->
m

<!-- b005234 | prose | pages [20] -->
m

<!-- b005235 | prose | pages [20] -->
m

<!-- b005236 | prose | pages [20] -->
m

<!-- b005237 | prose | pages [20] -->
m

<!-- b005238 | prose | pages [20] -->
m

<!-- b005239 | prose | pages [20] -->
m

<!-- b005240 | prose | pages [20] -->
m

<!-- b005241 | caption | pages [20] -->
Table 14: The post-investment prediction results

<!-- b005242 | prose | pages [20] -->
NOC Events AAPI CHN Men’s gymnastics 67.8 CHN Men’s gymnastics 67.8 CHN Women’s gymnastics 62.7 CHN Women’s gymnastics 62.7 CHN Men’s swimming 67.8 CHN Men’s swimming 67.8 JAM Men’s athletics 68.38 JAM Men’s athletics 68.38 JAM Women’s athletics 65 JAM Women’s athletics 65 GER Men’s shooting 62.6 GER Men’s shooting 62.6 GER Women’s swimming 62.4 GER Women’s swimming 62.4 GER Men’s swimming 61.6 GER Men’s swimming 61.6 G_C N_B N_S N_G Total 0 0.50 1.33 0.50 2.41 1 1.05 1.31 1.33 3.85 0 0.57 0.45 0.72 1.41 1 1.03 1.36 0.87 3.10 0 0.50 1.33 0.50 2.41 1 1.05 1.31 1.33 3.85 0 0.71 1.61 0.907 3.32 1 1.08 1.82 1.21 4.11 0 0.66 1.26 0.72 2.68 1 1.29 1.10 0.94 2.95 0 0.53 0.2 0.72 1.32 1 1.01 0.97 0.87 2.98 0 0.52 0.21 0.72 1.32 1 0.93 0.98 0.87 2.96 0 0.44 0.66 0 1.1 1 0.84 1.1 0.09 1.75

<!-- b005243 | prose | pages [20] -->
关注数学模型

<!-- b005244 | furniture | pages [20] -->
2

<!-- b005245 | furniture | pages [20] -->
MATHmodels

<!-- b005246 | furniture | pages [20] -->
获取更多资讯

<!-- b005247 | furniture | pages [21] -->
Team #2510185

<!-- b005248 | furniture | pages [21] -->
Page 21 of 24

<!-- b005249 | prose | pages [21] -->
Based on our analysis, we recommend that the following three countries introduce world-class coaches in these specific events:

<!-- b005250 | prose | pages [21] -->
• China: Women’s gymnastics

<!-- b005251 | prose | pages [21] -->
• Jamaica: Men’s athletics

<!-- b005252 | prose | pages [21] -->
微信公众号：数学模型

<!-- b005253 | prose | pages [21] -->
• Germany: Men’s shooting

<!-- b005254 | prose | pages [21] -->
Our predictions indicate that these events are likely to see the greatest improvement in total medal counts after the introduction of great coaches, with an estimated increase of approximately 1.6 medals.

<!-- b005255 | prose | pages [21] -->
5 Task 3: Other Original Insights

<!-- b005256 | prose | pages [21] -->
5.1 Common Traits of No Medal Nations

<!-- b005257 | prose | pages [21] -->
We observed 77 nations that have never won an Olympic medal, including countries with pop-

<!-- b005258 | prose | pages [21] -->
微信号：MATHmodels

<!-- b005259 | prose | pages [21] -->
ulations of tens of millions, such as Myanmar. When predicting medal acquisition, we found that nations are more likely to win their first medal when they demonstrate:

<!-- b005260 | prose | pages [21] -->
1. Long-term participation in the Games.

<!-- b005261 | prose | pages [21] -->
2. A large number of participating athletes.

<!-- b005262 | prose | pages [21] -->
3. Participation in a diverse range of sports.

<!-- b005263 | prose | pages [21] -->
For these nations determined to win medals, we recommend using our model to project the in- creased probability of medal acquisition following changes in athlete count (N_A) and event par- ticipation (N_E). Additionally, these nations could consider focusing their investments on less- dominated sports.

<!-- b005264 | prose | pages [21] -->
5.2 Negative Impact Events

<!-- b005265 | prose | pages [21] -->
Through Figure 11 (Importance of Sports to National Medal Count), we identified sports that have a negative impact on overall medal count. Given a fixed number of participating athletes, increasing participation in sports with positive importance can lead to more medals. Conversely, increasing participation in sports with negative importance is likely to result in a disproportionate investment-to-return ratio.

<!-- b005266 | prose | pages [21] -->
We recommend using our derived sport importance predictions to increase athlete participation in sports with positive importance for each nation. For example, if Germany aims to increase its medal count, it could shift investment from Boxing towards Canoeing.

<!-- b005267 | prose | pages [21] -->
5.3

<!-- b005268 | heading | pages [21] -->
Recommendations of “Great Coach”

<!-- b005269 | prose | pages [21] -->
Our model predicts that a “Great Coach” can contribute nearly 30% to performance improve- ment. Furthermore, we found that this effect is more pronounced in technically demanding sports such as Gymnastics and Shooting.

<!-- b005270 | prose | pages [21] -->
m

<!-- b005271 | prose | pages [21] -->
m

<!-- b005272 | prose | pages [21] -->
m

<!-- b005273 | prose | pages [21] -->
m

<!-- b005274 | prose | pages [21] -->
m

<!-- b005275 | prose | pages [21] -->
m

<!-- b005276 | prose | pages [21] -->
m

<!-- b005277 | prose | pages [21] -->
m

<!-- b005278 | prose | pages [21] -->
m

<!-- b005279 | prose | pages [21] -->
m

<!-- b005280 | prose | pages [21] -->
m

<!-- b005281 | prose | pages [21] -->
m

<!-- b005282 | prose | pages [21] -->
m

<!-- b005283 | prose | pages [21] -->
m

<!-- b005284 | prose | pages [21] -->
m

<!-- b005285 | prose | pages [21] -->
m

<!-- b005286 | prose | pages [21] -->
m

<!-- b005287 | prose | pages [21] -->
m

<!-- b005288 | prose | pages [21] -->
m

<!-- b005289 | prose | pages [21] -->
m

<!-- b005290 | prose | pages [21] -->
m

<!-- b005291 | prose | pages [21] -->
m

<!-- b005292 | prose | pages [21] -->
m

<!-- b005293 | prose | pages [21] -->
m

<!-- b005294 | prose | pages [21] -->
m

<!-- b005295 | prose | pages [21] -->
m

<!-- b005296 | prose | pages [21] -->
m

<!-- b005297 | prose | pages [21] -->
m

<!-- b005298 | prose | pages [21] -->
m

<!-- b005299 | prose | pages [21] -->
m

<!-- b005300 | prose | pages [21] -->
m

<!-- b005301 | prose | pages [21] -->
m

<!-- b005302 | prose | pages [21] -->
m

<!-- b005303 | prose | pages [21] -->
m

<!-- b005304 | prose | pages [21] -->
m

<!-- b005305 | prose | pages [21] -->
m

<!-- b005306 | prose | pages [21] -->
m

<!-- b005307 | prose | pages [21] -->
m

<!-- b005308 | prose | pages [21] -->
m

<!-- b005309 | prose | pages [21] -->
m

<!-- b005310 | prose | pages [21] -->
m

<!-- b005311 | prose | pages [21] -->
m

<!-- b005312 | prose | pages [21] -->
m

<!-- b005313 | prose | pages [21] -->
m

<!-- b005314 | prose | pages [21] -->
m

<!-- b005315 | prose | pages [21] -->
m

<!-- b005316 | prose | pages [21] -->
m

<!-- b005317 | prose | pages [21] -->
m

<!-- b005318 | prose | pages [21] -->
m

<!-- b005319 | prose | pages [21] -->
m

<!-- b005320 | prose | pages [21] -->
m

<!-- b005321 | prose | pages [21] -->
m

<!-- b005322 | prose | pages [21] -->
m

<!-- b005323 | prose | pages [21] -->
m

<!-- b005324 | prose | pages [21] -->
m

<!-- b005325 | prose | pages [21] -->
m

<!-- b005326 | prose | pages [21] -->
m

<!-- b005327 | prose | pages [21] -->
m

<!-- b005328 | prose | pages [21] -->
m

<!-- b005329 | prose | pages [21] -->
m

<!-- b005330 | prose | pages [21] -->
m

<!-- b005331 | prose | pages [21] -->
m

<!-- b005332 | prose | pages [21] -->
m

<!-- b005333 | prose | pages [21] -->
m

<!-- b005334 | prose | pages [21] -->
m

<!-- b005335 | prose | pages [21] -->
m

<!-- b005336 | prose | pages [21] -->
m

<!-- b005337 | prose | pages [21] -->
m

<!-- b005338 | prose | pages [21] -->
m

<!-- b005339 | prose | pages [21] -->
m

<!-- b005340 | prose | pages [21] -->
m

<!-- b005341 | prose | pages [21] -->
m

<!-- b005342 | prose | pages [21] -->
m

<!-- b005343 | prose | pages [21] -->
m

<!-- b005344 | prose | pages [21] -->
m

<!-- b005345 | prose | pages [21] -->
m

<!-- b005346 | prose | pages [21] -->
m

<!-- b005347 | prose | pages [21] -->
m

<!-- b005348 | prose | pages [21] -->
m

<!-- b005349 | prose | pages [21] -->
m

<!-- b005350 | prose | pages [21] -->
m

<!-- b005351 | prose | pages [21] -->
m

<!-- b005352 | prose | pages [21] -->
m

<!-- b005353 | prose | pages [21] -->
m

<!-- b005354 | prose | pages [21] -->
m

<!-- b005355 | prose | pages [21] -->
m

<!-- b005356 | prose | pages [21] -->
m

<!-- b005357 | prose | pages [21] -->
m

<!-- b005358 | prose | pages [21] -->
m

<!-- b005359 | prose | pages [21] -->
m

<!-- b005360 | prose | pages [21] -->
m

<!-- b005361 | prose | pages [21] -->
m

<!-- b005362 | prose | pages [21] -->
m

<!-- b005363 | prose | pages [21] -->
m

<!-- b005364 | prose | pages [21] -->
m

<!-- b005365 | prose | pages [21] -->
m

<!-- b005366 | prose | pages [21] -->
m

<!-- b005367 | prose | pages [21] -->
m

<!-- b005368 | prose | pages [21] -->
m

<!-- b005369 | prose | pages [21] -->
m

<!-- b005370 | prose | pages [21] -->
m

<!-- b005371 | prose | pages [21] -->
m

<!-- b005372 | prose | pages [21] -->
m

<!-- b005373 | prose | pages [21] -->
m

<!-- b005374 | prose | pages [21] -->
m

<!-- b005375 | prose | pages [21] -->
m

<!-- b005376 | prose | pages [21] -->
m

<!-- b005377 | prose | pages [21] -->
m

<!-- b005378 | prose | pages [21] -->
m

<!-- b005379 | prose | pages [21] -->
m

<!-- b005380 | prose | pages [21] -->
m

<!-- b005381 | prose | pages [21] -->
m

<!-- b005382 | prose | pages [21] -->
m

<!-- b005383 | prose | pages [21] -->
m

<!-- b005384 | prose | pages [21] -->
m

<!-- b005385 | prose | pages [21] -->
m

<!-- b005386 | prose | pages [21] -->
m

<!-- b005387 | prose | pages [21] -->
m

<!-- b005388 | prose | pages [21] -->
m

<!-- b005389 | prose | pages [21] -->
m

<!-- b005390 | prose | pages [21] -->
m

<!-- b005391 | prose | pages [21] -->
m

<!-- b005392 | prose | pages [21] -->
m

<!-- b005393 | prose | pages [21] -->
m

<!-- b005394 | prose | pages [21] -->
m

<!-- b005395 | prose | pages [21] -->
m

<!-- b005396 | prose | pages [21] -->
m

<!-- b005397 | prose | pages [21] -->
m

<!-- b005398 | prose | pages [21] -->
m

<!-- b005399 | prose | pages [21] -->
m

<!-- b005400 | prose | pages [21] -->
m

<!-- b005401 | prose | pages [21] -->
m

<!-- b005402 | prose | pages [21] -->
m

<!-- b005403 | prose | pages [21] -->
m

<!-- b005404 | prose | pages [21] -->
m

<!-- b005405 | prose | pages [21] -->
m

<!-- b005406 | prose | pages [21] -->
m

<!-- b005407 | prose | pages [21] -->
m

<!-- b005408 | prose | pages [21] -->
m

<!-- b005409 | prose | pages [21] -->
m

<!-- b005410 | prose | pages [21] -->
m

<!-- b005411 | prose | pages [21] -->
m

<!-- b005412 | prose | pages [21] -->
m

<!-- b005413 | prose | pages [21] -->
m

<!-- b005414 | prose | pages [21] -->
m

<!-- b005415 | prose | pages [21] -->
m

<!-- b005416 | prose | pages [21] -->
m

<!-- b005417 | prose | pages [21] -->
m

<!-- b005418 | prose | pages [21] -->
m

<!-- b005419 | prose | pages [21] -->
m

<!-- b005420 | prose | pages [21] -->
m

<!-- b005421 | prose | pages [21] -->
m

<!-- b005422 | prose | pages [21] -->
m

<!-- b005423 | prose | pages [21] -->
m

<!-- b005424 | prose | pages [21] -->
m

<!-- b005425 | prose | pages [21] -->
m

<!-- b005426 | prose | pages [21] -->
m

<!-- b005427 | prose | pages [21] -->
m

<!-- b005428 | prose | pages [21] -->
m

<!-- b005429 | prose | pages [21] -->
m

<!-- b005430 | prose | pages [21] -->
m

<!-- b005431 | prose | pages [21] -->
m

<!-- b005432 | prose | pages [21] -->
m

<!-- b005433 | prose | pages [21] -->
m

<!-- b005434 | prose | pages [21] -->
m

<!-- b005435 | prose | pages [21] -->
m

<!-- b005436 | prose | pages [21] -->
m

<!-- b005437 | prose | pages [21] -->
m

<!-- b005438 | prose | pages [21] -->
m

<!-- b005439 | prose | pages [21] -->
m

<!-- b005440 | prose | pages [21] -->
m

<!-- b005441 | prose | pages [21] -->
m

<!-- b005442 | prose | pages [21] -->
m

<!-- b005443 | prose | pages [21] -->
m

<!-- b005444 | prose | pages [21] -->
m

<!-- b005445 | prose | pages [21] -->
m

<!-- b005446 | prose | pages [21] -->
m

<!-- b005447 | prose | pages [21] -->
m

<!-- b005448 | prose | pages [21] -->
m

<!-- b005449 | prose | pages [21] -->
m

<!-- b005450 | prose | pages [21] -->
m

<!-- b005451 | prose | pages [21] -->
m

<!-- b005452 | prose | pages [21] -->
m

<!-- b005453 | prose | pages [21] -->
m

<!-- b005454 | prose | pages [21] -->
m

<!-- b005455 | prose | pages [21] -->
m

<!-- b005456 | prose | pages [21] -->
m

<!-- b005457 | prose | pages [21] -->
m

<!-- b005458 | prose | pages [21] -->
m

<!-- b005459 | prose | pages [21] -->
m

<!-- b005460 | prose | pages [21] -->
m

<!-- b005461 | prose | pages [21] -->
m

<!-- b005462 | prose | pages [21] -->
m

<!-- b005463 | prose | pages [21] -->
m

<!-- b005464 | prose | pages [21] -->
m

<!-- b005465 | prose | pages [21] -->
m

<!-- b005466 | prose | pages [21] -->
m

<!-- b005467 | prose | pages [21] -->
m

<!-- b005468 | prose | pages [21] -->
m

<!-- b005469 | prose | pages [21] -->
m

<!-- b005470 | prose | pages [21] -->
m

<!-- b005471 | prose | pages [21] -->
m

<!-- b005472 | prose | pages [21] -->
m

<!-- b005473 | prose | pages [21] -->
m

<!-- b005474 | prose | pages [21] -->
m

<!-- b005475 | prose | pages [21] -->
m

<!-- b005476 | prose | pages [21] -->
m

<!-- b005477 | prose | pages [21] -->
m

<!-- b005478 | prose | pages [21] -->
m

<!-- b005479 | prose | pages [21] -->
m

<!-- b005480 | prose | pages [21] -->
m

<!-- b005481 | prose | pages [21] -->
m

<!-- b005482 | prose | pages [21] -->
m

<!-- b005483 | prose | pages [21] -->
m

<!-- b005484 | prose | pages [21] -->
m

<!-- b005485 | prose | pages [21] -->
m

<!-- b005486 | prose | pages [21] -->
m

<!-- b005487 | prose | pages [21] -->
m

<!-- b005488 | prose | pages [21] -->
m

<!-- b005489 | prose | pages [21] -->
m

<!-- b005490 | prose | pages [21] -->
m

<!-- b005491 | prose | pages [21] -->
m

<!-- b005492 | prose | pages [21] -->
m

<!-- b005493 | prose | pages [21] -->
m

<!-- b005494 | prose | pages [21] -->
m

<!-- b005495 | prose | pages [21] -->
m

<!-- b005496 | prose | pages [21] -->
m

<!-- b005497 | prose | pages [21] -->
m

<!-- b005498 | prose | pages [21] -->
m

<!-- b005499 | prose | pages [21] -->
m

<!-- b005500 | prose | pages [21] -->
m

<!-- b005501 | prose | pages [21] -->
m

<!-- b005502 | prose | pages [21] -->
m

<!-- b005503 | prose | pages [21] -->
m

<!-- b005504 | prose | pages [21] -->
m

<!-- b005505 | prose | pages [21] -->
m

<!-- b005506 | prose | pages [21] -->
m

<!-- b005507 | prose | pages [21] -->
m

<!-- b005508 | prose | pages [21] -->
m

<!-- b005509 | prose | pages [21] -->
m

<!-- b005510 | prose | pages [21] -->
m

<!-- b005511 | prose | pages [21] -->
m

<!-- b005512 | prose | pages [21] -->
m

<!-- b005513 | prose | pages [21] -->
m

<!-- b005514 | prose | pages [21] -->
m

<!-- b005515 | prose | pages [21] -->
m

<!-- b005516 | prose | pages [21] -->
m

<!-- b005517 | prose | pages [21] -->
m

<!-- b005518 | prose | pages [21] -->
m

<!-- b005519 | prose | pages [21] -->
m

<!-- b005520 | prose | pages [21] -->
m

<!-- b005521 | prose | pages [21] -->
m

<!-- b005522 | prose | pages [21] -->
m

<!-- b005523 | prose | pages [21] -->
m

<!-- b005524 | prose | pages [21] -->
m

<!-- b005525 | prose | pages [21] -->
m

<!-- b005526 | prose | pages [21] -->
m

<!-- b005527 | prose | pages [21] -->
m

<!-- b005528 | prose | pages [21] -->
m

<!-- b005529 | prose | pages [21] -->
m

<!-- b005530 | prose | pages [21] -->
m

<!-- b005531 | prose | pages [21] -->
m

<!-- b005532 | prose | pages [21] -->
m

<!-- b005533 | prose | pages [21] -->
m

<!-- b005534 | prose | pages [21] -->
m

<!-- b005535 | prose | pages [21] -->
m

<!-- b005536 | prose | pages [21] -->
m

<!-- b005537 | prose | pages [21] -->
m

<!-- b005538 | prose | pages [21] -->
m

<!-- b005539 | prose | pages [21] -->
m

<!-- b005540 | prose | pages [21] -->
m

<!-- b005541 | prose | pages [21] -->
m

<!-- b005542 | prose | pages [21] -->
m

<!-- b005543 | prose | pages [21] -->
m

<!-- b005544 | prose | pages [21] -->
m

<!-- b005545 | prose | pages [21] -->
m

<!-- b005546 | prose | pages [21] -->
m

<!-- b005547 | prose | pages [21] -->
m

<!-- b005548 | prose | pages [21] -->
m

<!-- b005549 | prose | pages [21] -->
m

<!-- b005550 | prose | pages [21] -->
m

<!-- b005551 | prose | pages [21] -->
m

<!-- b005552 | prose | pages [21] -->
m

<!-- b005553 | prose | pages [21] -->
m

<!-- b005554 | furniture | pages [21] -->
m

<!-- b005555 | furniture | pages [21] -->
m

<!-- b005556 | furniture | pages [21] -->
m

<!-- b005557 | furniture | pages [21] -->
m

<!-- b005558 | furniture | pages [21] -->
m

<!-- b005559 | furniture | pages [21] -->
m

<!-- b005560 | furniture | pages [21] -->
m

<!-- b005561 | furniture | pages [21] -->
m

<!-- b005562 | furniture | pages [21] -->
m

<!-- b005563 | furniture | pages [21] -->
m

<!-- b005564 | furniture | pages [21] -->
m

<!-- b005565 | furniture | pages [21] -->
m

<!-- b005566 | furniture | pages [21] -->
m

<!-- b005567 | furniture | pages [21] -->
m

<!-- b005568 | furniture | pages [21] -->
m

<!-- b005569 | furniture | pages [21] -->
m

<!-- b005570 | furniture | pages [21] -->
m

<!-- b005571 | furniture | pages [21] -->
m

<!-- b005572 | furniture | pages [21] -->
m

<!-- b005573 | furniture | pages [21] -->
m

<!-- b005574 | furniture | pages [21] -->
m

<!-- b005575 | furniture | pages [21] -->
m

<!-- b005576 | furniture | pages [21] -->
m

<!-- b005577 | furniture | pages [21] -->
m

<!-- b005578 | furniture | pages [21] -->
m

<!-- b005579 | furniture | pages [21] -->
m

<!-- b005580 | furniture | pages [21] -->
m

<!-- b005581 | furniture | pages [21] -->
m

<!-- b005582 | furniture | pages [21] -->
m

<!-- b005583 | furniture | pages [21] -->
m

<!-- b005584 | furniture | pages [21] -->
m

<!-- b005585 | furniture | pages [21] -->
m

<!-- b005586 | furniture | pages [21] -->
m

<!-- b005587 | furniture | pages [21] -->
m

<!-- b005588 | furniture | pages [21] -->
m

<!-- b005589 | furniture | pages [21] -->
m

<!-- b005590 | furniture | pages [21] -->
m

<!-- b005591 | furniture | pages [21] -->
m

<!-- b005592 | furniture | pages [21] -->
m

<!-- b005593 | furniture | pages [21] -->
m

<!-- b005594 | furniture | pages [21] -->
m

<!-- b005595 | furniture | pages [21] -->
m

<!-- b005596 | furniture | pages [21] -->
m

<!-- b005597 | furniture | pages [21] -->
m

<!-- b005598 | furniture | pages [21] -->
m

<!-- b005599 | furniture | pages [21] -->
m

<!-- b005600 | furniture | pages [21] -->
m

<!-- b005601 | furniture | pages [21] -->
m

<!-- b005602 | furniture | pages [21] -->
m

<!-- b005603 | furniture | pages [21] -->
m

<!-- b005604 | furniture | pages [21] -->
m

<!-- b005605 | furniture | pages [21] -->
m

<!-- b005606 | furniture | pages [21] -->
m

<!-- b005607 | furniture | pages [21] -->
m

<!-- b005608 | furniture | pages [21] -->
m

<!-- b005609 | furniture | pages [21] -->
m

<!-- b005610 | furniture | pages [21] -->
m

<!-- b005611 | furniture | pages [21] -->
m

<!-- b005612 | furniture | pages [21] -->
m

<!-- b005613 | furniture | pages [21] -->
m

<!-- b005614 | furniture | pages [21] -->
m

<!-- b005615 | furniture | pages [21] -->
m

<!-- b005616 | furniture | pages [21] -->
m

<!-- b005617 | furniture | pages [21] -->
m

<!-- b005618 | furniture | pages [21] -->
m

<!-- b005619 | furniture | pages [21] -->
m

<!-- b005620 | furniture | pages [21] -->
m

<!-- b005621 | furniture | pages [21] -->
m

<!-- b005622 | furniture | pages [21] -->
m

<!-- b005623 | furniture | pages [21] -->
m

<!-- b005624 | furniture | pages [21] -->
m

<!-- b005625 | furniture | pages [21] -->
m

<!-- b005626 | furniture | pages [21] -->
m

<!-- b005627 | furniture | pages [21] -->
m

<!-- b005628 | furniture | pages [21] -->
m

<!-- b005629 | furniture | pages [21] -->
m

<!-- b005630 | furniture | pages [21] -->
m

<!-- b005631 | furniture | pages [21] -->
m

<!-- b005632 | furniture | pages [21] -->
m

<!-- b005633 | furniture | pages [21] -->
m

<!-- b005634 | furniture | pages [21] -->
m

<!-- b005635 | furniture | pages [21] -->
m

<!-- b005636 | furniture | pages [21] -->
m

<!-- b005637 | furniture | pages [21] -->
m

<!-- b005638 | furniture | pages [21] -->
m

<!-- b005639 | furniture | pages [21] -->
m

<!-- b005640 | furniture | pages [21] -->
m

<!-- b005641 | furniture | pages [21] -->
m

<!-- b005642 | furniture | pages [21] -->
m

<!-- b005643 | furniture | pages [21] -->
m

<!-- b005644 | furniture | pages [21] -->
m

<!-- b005645 | furniture | pages [21] -->
m

<!-- b005646 | furniture | pages [21] -->
m

<!-- b005647 | furniture | pages [21] -->
m

<!-- b005648 | furniture | pages [21] -->
m

<!-- b005649 | furniture | pages [21] -->
m

<!-- b005650 | furniture | pages [21] -->
m

<!-- b005651 | furniture | pages [21] -->
m

<!-- b005652 | furniture | pages [21] -->
m

<!-- b005653 | furniture | pages [21] -->
m

<!-- b005654 | furniture | pages [21] -->
m

<!-- b005655 | furniture | pages [21] -->
m

<!-- b005656 | furniture | pages [21] -->
m

<!-- b005657 | furniture | pages [21] -->
m

<!-- b005658 | furniture | pages [21] -->
m

<!-- b005659 | furniture | pages [21] -->
m

<!-- b005660 | furniture | pages [21] -->
m

<!-- b005661 | furniture | pages [21] -->
m

<!-- b005662 | furniture | pages [21] -->
m

<!-- b005663 | furniture | pages [21] -->
m

<!-- b005664 | furniture | pages [21] -->
m

<!-- b005665 | furniture | pages [21] -->
m

<!-- b005666 | furniture | pages [21] -->
m

<!-- b005667 | furniture | pages [21] -->
m

<!-- b005668 | furniture | pages [21] -->
m

<!-- b005669 | furniture | pages [21] -->
m

<!-- b005670 | furniture | pages [21] -->
m

<!-- b005671 | furniture | pages [21] -->
m

<!-- b005672 | furniture | pages [21] -->
m

<!-- b005673 | furniture | pages [21] -->
m

<!-- b005674 | furniture | pages [21] -->
m

<!-- b005675 | furniture | pages [21] -->
m

<!-- b005676 | furniture | pages [21] -->
m

<!-- b005677 | furniture | pages [21] -->
m

<!-- b005678 | furniture | pages [21] -->
m

<!-- b005679 | furniture | pages [21] -->
m

<!-- b005680 | furniture | pages [21] -->
m

<!-- b005681 | furniture | pages [21] -->
m

<!-- b005682 | furniture | pages [21] -->
m

<!-- b005683 | furniture | pages [21] -->
m

<!-- b005684 | furniture | pages [21] -->
m

<!-- b005685 | furniture | pages [21] -->
m

<!-- b005686 | furniture | pages [21] -->
m

<!-- b005687 | furniture | pages [21] -->
m

<!-- b005688 | furniture | pages [21] -->
m

<!-- b005689 | furniture | pages [21] -->
m

<!-- b005690 | furniture | pages [21] -->
m

<!-- b005691 | furniture | pages [21] -->
m

<!-- b005692 | furniture | pages [21] -->
m

<!-- b005693 | furniture | pages [21] -->
m

<!-- b005694 | furniture | pages [21] -->
m

<!-- b005695 | furniture | pages [21] -->
m

<!-- b005696 | furniture | pages [21] -->
m

<!-- b005697 | furniture | pages [21] -->
m

<!-- b005698 | furniture | pages [21] -->
m

<!-- b005699 | furniture | pages [21] -->
m

<!-- b005700 | furniture | pages [21] -->
m

<!-- b005701 | furniture | pages [21] -->
m

<!-- b005702 | furniture | pages [21] -->
m

<!-- b005703 | furniture | pages [21] -->
m

<!-- b005704 | furniture | pages [21] -->
m

<!-- b005705 | furniture | pages [21] -->
m

<!-- b005706 | furniture | pages [21] -->
m

<!-- b005707 | furniture | pages [21] -->
m

<!-- b005708 | furniture | pages [21] -->
m

<!-- b005709 | furniture | pages [21] -->
m

<!-- b005710 | furniture | pages [21] -->
m

<!-- b005711 | furniture | pages [21] -->
m

<!-- b005712 | furniture | pages [21] -->
m

<!-- b005713 | furniture | pages [21] -->
m

<!-- b005714 | furniture | pages [21] -->
m

<!-- b005715 | furniture | pages [21] -->
m

<!-- b005716 | furniture | pages [21] -->
m

<!-- b005717 | furniture | pages [21] -->
m

<!-- b005718 | furniture | pages [21] -->
m

<!-- b005719 | furniture | pages [21] -->
m

<!-- b005720 | furniture | pages [21] -->
m

<!-- b005721 | furniture | pages [21] -->
m

<!-- b005722 | furniture | pages [21] -->
m

<!-- b005723 | furniture | pages [21] -->
m

<!-- b005724 | furniture | pages [21] -->
m

<!-- b005725 | furniture | pages [21] -->
m

<!-- b005726 | furniture | pages [21] -->
m

<!-- b005727 | furniture | pages [21] -->
m

<!-- b005728 | furniture | pages [21] -->
m

<!-- b005729 | furniture | pages [21] -->
m

<!-- b005730 | furniture | pages [21] -->
m

<!-- b005731 | furniture | pages [21] -->
m

<!-- b005732 | furniture | pages [21] -->
m

<!-- b005733 | furniture | pages [21] -->
m

<!-- b005734 | furniture | pages [21] -->
m

<!-- b005735 | furniture | pages [21] -->
m

<!-- b005736 | furniture | pages [21] -->
m

<!-- b005737 | furniture | pages [21] -->
m

<!-- b005738 | furniture | pages [21] -->
m

<!-- b005739 | furniture | pages [21] -->
m

<!-- b005740 | furniture | pages [21] -->
m

<!-- b005741 | furniture | pages [21] -->
m

<!-- b005742 | furniture | pages [21] -->
m

<!-- b005743 | furniture | pages [21] -->
m

<!-- b005744 | furniture | pages [21] -->
m

<!-- b005745 | furniture | pages [21] -->
m

<!-- b005746 | furniture | pages [21] -->
m

<!-- b005747 | furniture | pages [21] -->
m

<!-- b005748 | furniture | pages [21] -->
m

<!-- b005749 | furniture | pages [21] -->
m

<!-- b005750 | furniture | pages [21] -->
m

<!-- b005751 | furniture | pages [21] -->
m

<!-- b005752 | furniture | pages [21] -->
m

<!-- b005753 | furniture | pages [21] -->
m

<!-- b005754 | furniture | pages [21] -->
m

<!-- b005755 | furniture | pages [21] -->
m

<!-- b005756 | furniture | pages [21] -->
m

<!-- b005757 | furniture | pages [21] -->
m

<!-- b005758 | furniture | pages [21] -->
m

<!-- b005759 | furniture | pages [21] -->
m

<!-- b005760 | furniture | pages [21] -->
m

<!-- b005761 | furniture | pages [21] -->
m

<!-- b005762 | furniture | pages [21] -->
m

<!-- b005763 | furniture | pages [21] -->
m

<!-- b005764 | furniture | pages [21] -->
m

<!-- b005765 | furniture | pages [21] -->
m

<!-- b005766 | furniture | pages [21] -->
m

<!-- b005767 | furniture | pages [21] -->
m

<!-- b005768 | furniture | pages [21] -->
m

<!-- b005769 | furniture | pages [21] -->
m

<!-- b005770 | furniture | pages [21] -->
m

<!-- b005771 | furniture | pages [21] -->
m

<!-- b005772 | furniture | pages [21] -->
m

<!-- b005773 | furniture | pages [21] -->
m

<!-- b005774 | furniture | pages [21] -->
m

<!-- b005775 | furniture | pages [21] -->
m

<!-- b005776 | furniture | pages [21] -->
m

<!-- b005777 | furniture | pages [21] -->
m

<!-- b005778 | furniture | pages [21] -->
m

<!-- b005779 | furniture | pages [21] -->
m

<!-- b005780 | furniture | pages [21] -->
m

<!-- b005781 | furniture | pages [21] -->
m

<!-- b005782 | furniture | pages [21] -->
m

<!-- b005783 | furniture | pages [21] -->
m

<!-- b005784 | furniture | pages [21] -->
m

<!-- b005785 | furniture | pages [21] -->
m

<!-- b005786 | furniture | pages [21] -->
m

<!-- b005787 | furniture | pages [21] -->
m

<!-- b005788 | furniture | pages [21] -->
m

<!-- b005789 | furniture | pages [21] -->
m

<!-- b005790 | furniture | pages [21] -->
m

<!-- b005791 | furniture | pages [21] -->
m

<!-- b005792 | furniture | pages [21] -->
m

<!-- b005793 | furniture | pages [21] -->
m

<!-- b005794 | furniture | pages [21] -->
m

<!-- b005795 | furniture | pages [21] -->
m

<!-- b005796 | furniture | pages [21] -->
m

<!-- b005797 | furniture | pages [21] -->
m

<!-- b005798 | furniture | pages [21] -->
m

<!-- b005799 | furniture | pages [21] -->
m

<!-- b005800 | furniture | pages [21] -->
m

<!-- b005801 | furniture | pages [21] -->
m

<!-- b005802 | furniture | pages [21] -->
m

<!-- b005803 | furniture | pages [21] -->
m

<!-- b005804 | furniture | pages [21] -->
m

<!-- b005805 | furniture | pages [21] -->
m

<!-- b005806 | furniture | pages [21] -->
m

<!-- b005807 | furniture | pages [21] -->
m

<!-- b005808 | furniture | pages [21] -->
m

<!-- b005809 | furniture | pages [21] -->
m

<!-- b005810 | furniture | pages [21] -->
m

<!-- b005811 | furniture | pages [21] -->
m

<!-- b005812 | furniture | pages [21] -->
m

<!-- b005813 | furniture | pages [21] -->
m

<!-- b005814 | furniture | pages [21] -->
m

<!-- b005815 | furniture | pages [21] -->
m

<!-- b005816 | furniture | pages [21] -->
m

<!-- b005817 | furniture | pages [21] -->
m

<!-- b005818 | furniture | pages [21] -->
m

<!-- b005819 | furniture | pages [21] -->
m

<!-- b005820 | furniture | pages [21] -->
m

<!-- b005821 | furniture | pages [21] -->
m

<!-- b005822 | furniture | pages [21] -->
m

<!-- b005823 | furniture | pages [21] -->
m

<!-- b005824 | furniture | pages [21] -->
m

<!-- b005825 | furniture | pages [21] -->
m

<!-- b005826 | furniture | pages [21] -->
m

<!-- b005827 | furniture | pages [21] -->
m

<!-- b005828 | furniture | pages [21] -->
m

<!-- b005829 | furniture | pages [21] -->
m

<!-- b005830 | furniture | pages [21] -->
m

<!-- b005831 | furniture | pages [21] -->
m

<!-- b005832 | furniture | pages [21] -->
m

<!-- b005833 | furniture | pages [21] -->
m

<!-- b005834 | furniture | pages [21] -->
m

<!-- b005835 | furniture | pages [21] -->
m

<!-- b005836 | furniture | pages [21] -->
m

<!-- b005837 | furniture | pages [21] -->
m

<!-- b005838 | furniture | pages [21] -->
m

<!-- b005839 | furniture | pages [21] -->
m

<!-- b005840 | furniture | pages [21] -->
m

<!-- b005841 | furniture | pages [21] -->
m

<!-- b005842 | furniture | pages [21] -->
m

<!-- b005843 | furniture | pages [21] -->
m

<!-- b005844 | furniture | pages [21] -->
m

<!-- b005845 | furniture | pages [21] -->
m

<!-- b005846 | furniture | pages [21] -->
m

<!-- b005847 | furniture | pages [21] -->
m

<!-- b005848 | furniture | pages [21] -->
m

<!-- b005849 | furniture | pages [21] -->
m

<!-- b005850 | furniture | pages [21] -->
m

<!-- b005851 | furniture | pages [21] -->
m

<!-- b005852 | furniture | pages [21] -->
m

<!-- b005853 | furniture | pages [21] -->
m

<!-- b005854 | furniture | pages [21] -->
m

<!-- b005855 | furniture | pages [21] -->
m

<!-- b005856 | furniture | pages [21] -->
m

<!-- b005857 | furniture | pages [21] -->
m

<!-- b005858 | furniture | pages [21] -->
m

<!-- b005859 | furniture | pages [21] -->
m

<!-- b005860 | furniture | pages [21] -->
m

<!-- b005861 | furniture | pages [21] -->
m

<!-- b005862 | furniture | pages [21] -->
m

<!-- b005863 | furniture | pages [21] -->
m

<!-- b005864 | furniture | pages [21] -->
m

<!-- b005865 | furniture | pages [21] -->
m

<!-- b005866 | furniture | pages [21] -->
m

<!-- b005867 | furniture | pages [21] -->
m

<!-- b005868 | furniture | pages [21] -->
m

<!-- b005869 | furniture | pages [21] -->
m

<!-- b005870 | furniture | pages [21] -->
m

<!-- b005871 | furniture | pages [21] -->
m

<!-- b005872 | furniture | pages [21] -->
m

<!-- b005873 | furniture | pages [21] -->
m

<!-- b005874 | furniture | pages [21] -->
m

<!-- b005875 | furniture | pages [21] -->
m

<!-- b005876 | furniture | pages [21] -->
m

<!-- b005877 | furniture | pages [21] -->
m

<!-- b005878 | furniture | pages [21] -->
m

<!-- b005879 | furniture | pages [21] -->
m

<!-- b005880 | furniture | pages [21] -->
m

<!-- b005881 | furniture | pages [21] -->
m

<!-- b005882 | furniture | pages [21] -->
m

<!-- b005883 | furniture | pages [21] -->
m

<!-- b005884 | furniture | pages [21] -->
m

<!-- b005885 | furniture | pages [21] -->
m

<!-- b005886 | furniture | pages [21] -->
m

<!-- b005887 | furniture | pages [21] -->
m

<!-- b005888 | furniture | pages [21] -->
m

<!-- b005889 | furniture | pages [21] -->
m

<!-- b005890 | furniture | pages [21] -->
m

<!-- b005891 | furniture | pages [21] -->
m

<!-- b005892 | furniture | pages [21] -->
m

<!-- b005893 | furniture | pages [21] -->
m

<!-- b005894 | furniture | pages [21] -->
m

<!-- b005895 | furniture | pages [21] -->
m

<!-- b005896 | furniture | pages [21] -->
m

<!-- b005897 | furniture | pages [21] -->
m

<!-- b005898 | furniture | pages [21] -->
m

<!-- b005899 | furniture | pages [21] -->
m

<!-- b005900 | furniture | pages [21] -->
m

<!-- b005901 | furniture | pages [21] -->
m

<!-- b005902 | furniture | pages [21] -->
m

<!-- b005903 | furniture | pages [21] -->
m

<!-- b005904 | furniture | pages [21] -->
m

<!-- b005905 | furniture | pages [21] -->
m

<!-- b005906 | furniture | pages [21] -->
m

<!-- b005907 | furniture | pages [21] -->
m

<!-- b005908 | furniture | pages [21] -->
m

<!-- b005909 | furniture | pages [21] -->
m

<!-- b005910 | furniture | pages [21] -->
m

<!-- b005911 | furniture | pages [21] -->
m

<!-- b005912 | furniture | pages [21] -->
m

<!-- b005913 | furniture | pages [21] -->
m

<!-- b005914 | furniture | pages [21] -->
m

<!-- b005915 | furniture | pages [21] -->
m

<!-- b005916 | furniture | pages [21] -->
m

<!-- b005917 | furniture | pages [21] -->
m

<!-- b005918 | furniture | pages [21] -->
m

<!-- b005919 | furniture | pages [21] -->
m

<!-- b005920 | furniture | pages [21] -->
m

<!-- b005921 | furniture | pages [21] -->
m

<!-- b005922 | furniture | pages [21] -->
m

<!-- b005923 | furniture | pages [21] -->
m

<!-- b005924 | furniture | pages [21] -->
m

<!-- b005925 | furniture | pages [21] -->
m

<!-- b005926 | furniture | pages [21] -->
m

<!-- b005927 | furniture | pages [21] -->
m

<!-- b005928 | furniture | pages [21] -->
m

<!-- b005929 | furniture | pages [21] -->
m

<!-- b005930 | furniture | pages [21] -->
m

<!-- b005931 | furniture | pages [21] -->
m

<!-- b005932 | furniture | pages [21] -->
m

<!-- b005933 | furniture | pages [21] -->
m

<!-- b005934 | furniture | pages [21] -->
m

<!-- b005935 | furniture | pages [21] -->
m

<!-- b005936 | furniture | pages [21] -->
m

<!-- b005937 | furniture | pages [21] -->
m

<!-- b005938 | furniture | pages [21] -->
m

<!-- b005939 | furniture | pages [21] -->
m

<!-- b005940 | furniture | pages [21] -->
m

<!-- b005941 | furniture | pages [21] -->
m

<!-- b005942 | furniture | pages [21] -->
m

<!-- b005943 | furniture | pages [21] -->
m

<!-- b005944 | furniture | pages [21] -->
m

<!-- b005945 | furniture | pages [21] -->
m

<!-- b005946 | furniture | pages [21] -->
m

<!-- b005947 | furniture | pages [21] -->
m

<!-- b005948 | furniture | pages [21] -->
m

<!-- b005949 | furniture | pages [21] -->
m

<!-- b005950 | furniture | pages [21] -->
m

<!-- b005951 | furniture | pages [21] -->
m

<!-- b005952 | furniture | pages [21] -->
m

<!-- b005953 | furniture | pages [21] -->
m

<!-- b005954 | furniture | pages [21] -->
m

<!-- b005955 | furniture | pages [21] -->
m

<!-- b005956 | furniture | pages [21] -->
m

<!-- b005957 | furniture | pages [22] -->
Team #2510185

<!-- b005958 | furniture | pages [22] -->
Page 22 of 24

<!-- b005959 | prose | pages [22] -->
National Olympic Committees can use the Event Potential Index (EPI) to assess the potential performance improvement of a sport after hiring a world-class coach. By weighing the actual investment against the expected return, committees can make informed decisions about whether to hire such coaches for specific sports.

<!-- b005960 | prose | pages [22] -->
m

<!-- b005961 | prose | pages [22] -->
m

<!-- b005962 | prose | pages [22] -->
m

<!-- b005963 | prose | pages [22] -->
m

<!-- b005964 | prose | pages [22] -->
m

<!-- b005965 | prose | pages [22] -->
m

<!-- b005966 | prose | pages [22] -->
m

<!-- b005967 | prose | pages [22] -->
m

<!-- b005968 | prose | pages [22] -->
m

<!-- b005969 | prose | pages [22] -->
m

<!-- b005970 | prose | pages [22] -->
m

<!-- b005971 | prose | pages [22] -->
m

<!-- b005972 | prose | pages [22] -->
m

<!-- b005973 | prose | pages [22] -->
m

<!-- b005974 | prose | pages [22] -->
m

<!-- b005975 | prose | pages [22] -->
m

<!-- b005976 | prose | pages [22] -->
m

<!-- b005977 | prose | pages [22] -->
m

<!-- b005978 | prose | pages [22] -->
m

<!-- b005979 | prose | pages [22] -->
m

<!-- b005980 | prose | pages [22] -->
m

<!-- b005981 | prose | pages [22] -->
m

<!-- b005982 | prose | pages [22] -->
m

<!-- b005983 | prose | pages [22] -->
m

<!-- b005984 | prose | pages [22] -->
m

<!-- b005985 | prose | pages [22] -->
m

<!-- b005986 | prose | pages [22] -->
m

<!-- b005987 | prose | pages [22] -->
m

<!-- b005988 | prose | pages [22] -->
m

<!-- b005989 | prose | pages [22] -->
m

<!-- b005990 | prose | pages [22] -->
m

<!-- b005991 | prose | pages [22] -->
m

<!-- b005992 | prose | pages [22] -->
m

<!-- b005993 | prose | pages [22] -->
m

<!-- b005994 | prose | pages [22] -->
m

<!-- b005995 | prose | pages [22] -->
m

<!-- b005996 | prose | pages [22] -->
m

<!-- b005997 | prose | pages [22] -->
m

<!-- b005998 | prose | pages [22] -->
m

<!-- b005999 | prose | pages [22] -->
m

<!-- b006000 | prose | pages [22] -->
m

<!-- b006001 | prose | pages [22] -->
m

<!-- b006002 | prose | pages [22] -->
m

<!-- b006003 | prose | pages [22] -->
m

<!-- b006004 | prose | pages [22] -->
m

<!-- b006005 | prose | pages [22] -->
m

<!-- b006006 | prose | pages [22] -->
m

<!-- b006007 | prose | pages [22] -->
m

<!-- b006008 | prose | pages [22] -->
m

<!-- b006009 | prose | pages [22] -->
m

<!-- b006010 | prose | pages [22] -->
m

<!-- b006011 | prose | pages [22] -->
m

<!-- b006012 | prose | pages [22] -->
m

<!-- b006013 | prose | pages [22] -->
m

<!-- b006014 | prose | pages [22] -->
m

<!-- b006015 | prose | pages [22] -->
m

<!-- b006016 | prose | pages [22] -->
m

<!-- b006017 | prose | pages [22] -->
m

<!-- b006018 | prose | pages [22] -->
m

<!-- b006019 | prose | pages [22] -->
m

<!-- b006020 | prose | pages [22] -->
m

<!-- b006021 | prose | pages [22] -->
m

<!-- b006022 | prose | pages [22] -->
m

<!-- b006023 | prose | pages [22] -->
m

<!-- b006024 | prose | pages [22] -->
m

<!-- b006025 | prose | pages [22] -->
m

<!-- b006026 | prose | pages [22] -->
m

<!-- b006027 | prose | pages [22] -->
m

<!-- b006028 | prose | pages [22] -->
m

<!-- b006029 | prose | pages [22] -->
m

<!-- b006030 | prose | pages [22] -->
m

<!-- b006031 | prose | pages [22] -->
m

<!-- b006032 | prose | pages [22] -->
m

<!-- b006033 | prose | pages [22] -->
m

<!-- b006034 | prose | pages [22] -->
m

<!-- b006035 | prose | pages [22] -->
m

<!-- b006036 | prose | pages [22] -->
m

<!-- b006037 | prose | pages [22] -->
m

<!-- b006038 | prose | pages [22] -->
m

<!-- b006039 | prose | pages [22] -->
m

<!-- b006040 | prose | pages [22] -->
m

<!-- b006041 | prose | pages [22] -->
m

<!-- b006042 | prose | pages [22] -->
m

<!-- b006043 | prose | pages [22] -->
m

<!-- b006044 | prose | pages [22] -->
m

<!-- b006045 | prose | pages [22] -->
m

<!-- b006046 | prose | pages [22] -->
m

<!-- b006047 | prose | pages [22] -->
m

<!-- b006048 | prose | pages [22] -->
m

<!-- b006049 | prose | pages [22] -->
m

<!-- b006050 | prose | pages [22] -->
m

<!-- b006051 | prose | pages [22] -->
m

<!-- b006052 | prose | pages [22] -->
m

<!-- b006053 | prose | pages [22] -->
m

<!-- b006054 | prose | pages [22] -->
m

<!-- b006055 | prose | pages [22] -->
6

<!-- b006056 | heading | pages [22] -->
Model Analysis

<!-- b006057 | prose | pages [22] -->
m

<!-- b006058 | prose | pages [22] -->
m

<!-- b006059 | prose | pages [22] -->
m

<!-- b006060 | prose | pages [22] -->
m

<!-- b006061 | prose | pages [22] -->
m

<!-- b006062 | prose | pages [22] -->
m

<!-- b006063 | prose | pages [22] -->
m

<!-- b006064 | prose | pages [22] -->
m

<!-- b006065 | prose | pages [22] -->
m

<!-- b006066 | prose | pages [22] -->
m

<!-- b006067 | prose | pages [22] -->
m

<!-- b006068 | prose | pages [22] -->
m

<!-- b006069 | prose | pages [22] -->
m

<!-- b006070 | prose | pages [22] -->
m

<!-- b006071 | prose | pages [22] -->
m

<!-- b006072 | prose | pages [22] -->
m

<!-- b006073 | prose | pages [22] -->
m

<!-- b006074 | prose | pages [22] -->
m

<!-- b006075 | prose | pages [22] -->
m

<!-- b006076 | prose | pages [22] -->
m

<!-- b006077 | prose | pages [22] -->
m

<!-- b006078 | prose | pages [22] -->
m

<!-- b006079 | prose | pages [22] -->
m

<!-- b006080 | prose | pages [22] -->
m

<!-- b006081 | prose | pages [22] -->
m

<!-- b006082 | prose | pages [22] -->
m

<!-- b006083 | prose | pages [22] -->
m

<!-- b006084 | prose | pages [22] -->
m

<!-- b006085 | prose | pages [22] -->
m

<!-- b006086 | prose | pages [22] -->
m

<!-- b006087 | prose | pages [22] -->
m

<!-- b006088 | prose | pages [22] -->
m

<!-- b006089 | prose | pages [22] -->
m

<!-- b006090 | prose | pages [22] -->
m

<!-- b006091 | prose | pages [22] -->
m

<!-- b006092 | prose | pages [22] -->
m

<!-- b006093 | prose | pages [22] -->
m

<!-- b006094 | prose | pages [22] -->
m

<!-- b006095 | prose | pages [22] -->
m

<!-- b006096 | prose | pages [22] -->
m

<!-- b006097 | prose | pages [22] -->
m

<!-- b006098 | prose | pages [22] -->
m

<!-- b006099 | prose | pages [22] -->
m

<!-- b006100 | prose | pages [22] -->
m

<!-- b006101 | prose | pages [22] -->
m

<!-- b006102 | prose | pages [22] -->
m

<!-- b006103 | prose | pages [22] -->
m

<!-- b006104 | prose | pages [22] -->
m

<!-- b006105 | prose | pages [22] -->
m

<!-- b006106 | prose | pages [22] -->
m

<!-- b006107 | prose | pages [22] -->
m

<!-- b006108 | prose | pages [22] -->
m

<!-- b006109 | prose | pages [22] -->
m

<!-- b006110 | prose | pages [22] -->
m

<!-- b006111 | prose | pages [22] -->
m

<!-- b006112 | prose | pages [22] -->
m

<!-- b006113 | prose | pages [22] -->
m

<!-- b006114 | prose | pages [22] -->
m

<!-- b006115 | prose | pages [22] -->
m

<!-- b006116 | prose | pages [22] -->
m

<!-- b006117 | prose | pages [22] -->
m

<!-- b006118 | prose | pages [22] -->
m

<!-- b006119 | prose | pages [22] -->
m

<!-- b006120 | prose | pages [22] -->
m

<!-- b006121 | prose | pages [22] -->
m

<!-- b006122 | prose | pages [22] -->
m

<!-- b006123 | prose | pages [22] -->
m

<!-- b006124 | prose | pages [22] -->
m

<!-- b006125 | prose | pages [22] -->
m

<!-- b006126 | prose | pages [22] -->
m

<!-- b006127 | prose | pages [22] -->
m

<!-- b006128 | prose | pages [22] -->
m

<!-- b006129 | prose | pages [22] -->
m

<!-- b006130 | prose | pages [22] -->
m

<!-- b006131 | prose | pages [22] -->
m

<!-- b006132 | prose | pages [22] -->
m

<!-- b006133 | prose | pages [22] -->
m

<!-- b006134 | prose | pages [22] -->
m

<!-- b006135 | prose | pages [22] -->
m

<!-- b006136 | prose | pages [22] -->
m

<!-- b006137 | prose | pages [22] -->
m

<!-- b006138 | prose | pages [22] -->
m

<!-- b006139 | prose | pages [22] -->
m

<!-- b006140 | prose | pages [22] -->
m

<!-- b006141 | prose | pages [22] -->
m

<!-- b006142 | prose | pages [22] -->
m

<!-- b006143 | prose | pages [22] -->
m

<!-- b006144 | prose | pages [22] -->
m

<!-- b006145 | prose | pages [22] -->
m

<!-- b006146 | prose | pages [22] -->
m

<!-- b006147 | prose | pages [22] -->
m

<!-- b006148 | prose | pages [22] -->
m

<!-- b006149 | prose | pages [22] -->
m

<!-- b006150 | prose | pages [22] -->
m

<!-- b006151 | prose | pages [22] -->
m

<!-- b006152 | prose | pages [22] -->
m

<!-- b006153 | prose | pages [22] -->
m

<!-- b006154 | prose | pages [22] -->
m

<!-- b006155 | prose | pages [22] -->
m

<!-- b006156 | prose | pages [22] -->
m

<!-- b006157 | prose | pages [22] -->
m

<!-- b006158 | prose | pages [22] -->
m

<!-- b006159 | prose | pages [22] -->
m

<!-- b006160 | prose | pages [22] -->
m

<!-- b006161 | prose | pages [22] -->
m

<!-- b006162 | prose | pages [22] -->
m

<!-- b006163 | prose | pages [22] -->
m

<!-- b006164 | prose | pages [22] -->
m

<!-- b006165 | prose | pages [22] -->
m

<!-- b006166 | prose | pages [22] -->
m

<!-- b006167 | prose | pages [22] -->
m

<!-- b006168 | prose | pages [22] -->
m

<!-- b006169 | prose | pages [22] -->
m

<!-- b006170 | prose | pages [22] -->
m

<!-- b006171 | prose | pages [22] -->
m

<!-- b006172 | prose | pages [22] -->
m

<!-- b006173 | prose | pages [22] -->
m

<!-- b006174 | prose | pages [22] -->
m

<!-- b006175 | prose | pages [22] -->
m

<!-- b006176 | prose | pages [22] -->
m

<!-- b006177 | prose | pages [22] -->
m

<!-- b006178 | prose | pages [22] -->
m

<!-- b006179 | prose | pages [22] -->
m

<!-- b006180 | prose | pages [22] -->
m

<!-- b006181 | prose | pages [22] -->
m

<!-- b006182 | prose | pages [22] -->
m

<!-- b006183 | prose | pages [22] -->
m

<!-- b006184 | prose | pages [22] -->
m

<!-- b006185 | prose | pages [22] -->
m

<!-- b006186 | prose | pages [22] -->
m

<!-- b006187 | prose | pages [22] -->
m

<!-- b006188 | prose | pages [22] -->
m

<!-- b006189 | prose | pages [22] -->
m

<!-- b006190 | prose | pages [22] -->
m

<!-- b006191 | prose | pages [22] -->
m

<!-- b006192 | prose | pages [22] -->
m

<!-- b006193 | prose | pages [22] -->
m

<!-- b006194 | prose | pages [22] -->
m

<!-- b006195 | prose | pages [22] -->
m

<!-- b006196 | prose | pages [22] -->
m

<!-- b006197 | prose | pages [22] -->
m

<!-- b006198 | prose | pages [22] -->
m

<!-- b006199 | prose | pages [22] -->
m

<!-- b006200 | prose | pages [22] -->
m

<!-- b006201 | prose | pages [22] -->
m

<!-- b006202 | prose | pages [22] -->
m

<!-- b006203 | prose | pages [22] -->
m

<!-- b006204 | prose | pages [22] -->
m

<!-- b006205 | prose | pages [22] -->
m

<!-- b006206 | prose | pages [22] -->
m

<!-- b006207 | prose | pages [22] -->
m

<!-- b006208 | prose | pages [22] -->
m

<!-- b006209 | prose | pages [22] -->
m

<!-- b006210 | prose | pages [22] -->
m

<!-- b006211 | prose | pages [22] -->
m

<!-- b006212 | prose | pages [22] -->
m

<!-- b006213 | prose | pages [22] -->
m

<!-- b006214 | prose | pages [22] -->
m

<!-- b006215 | prose | pages [22] -->
m

<!-- b006216 | prose | pages [22] -->
m

<!-- b006217 | prose | pages [22] -->
m

<!-- b006218 | prose | pages [22] -->
m

<!-- b006219 | prose | pages [22] -->
m

<!-- b006220 | prose | pages [22] -->
m

<!-- b006221 | prose | pages [22] -->
m

<!-- b006222 | prose | pages [22] -->
m

<!-- b006223 | prose | pages [22] -->
m

<!-- b006224 | prose | pages [22] -->
m

<!-- b006225 | prose | pages [22] -->
m

<!-- b006226 | prose | pages [22] -->
m

<!-- b006227 | prose | pages [22] -->
m

<!-- b006228 | prose | pages [22] -->
m

<!-- b006229 | prose | pages [22] -->
m

<!-- b006230 | prose | pages [22] -->
m

<!-- b006231 | prose | pages [22] -->
m

<!-- b006232 | prose | pages [22] -->
m

<!-- b006233 | prose | pages [22] -->
m

<!-- b006234 | prose | pages [22] -->
m

<!-- b006235 | prose | pages [22] -->
m

<!-- b006236 | prose | pages [22] -->
m

<!-- b006237 | prose | pages [22] -->
m

<!-- b006238 | prose | pages [22] -->
m

<!-- b006239 | prose | pages [22] -->
m

<!-- b006240 | prose | pages [22] -->
m

<!-- b006241 | prose | pages [22] -->
m

<!-- b006242 | prose | pages [22] -->
m

<!-- b006243 | prose | pages [22] -->
m

<!-- b006244 | prose | pages [22] -->
m

<!-- b006245 | prose | pages [22] -->
m

<!-- b006246 | prose | pages [22] -->
m

<!-- b006247 | prose | pages [22] -->
m

<!-- b006248 | prose | pages [22] -->
m

<!-- b006249 | prose | pages [22] -->
m

<!-- b006250 | prose | pages [22] -->
m

<!-- b006251 | prose | pages [22] -->
m

<!-- b006252 | prose | pages [22] -->
m

<!-- b006253 | prose | pages [22] -->
m

<!-- b006254 | prose | pages [22] -->
m

<!-- b006255 | prose | pages [22] -->
m

<!-- b006256 | prose | pages [22] -->
m

<!-- b006257 | prose | pages [22] -->
m

<!-- b006258 | prose | pages [22] -->
m

<!-- b006259 | prose | pages [22] -->
m

<!-- b006260 | prose | pages [22] -->
m

<!-- b006261 | prose | pages [22] -->
m

<!-- b006262 | prose | pages [22] -->
m

<!-- b006263 | prose | pages [22] -->
m

<!-- b006264 | prose | pages [22] -->
m

<!-- b006265 | prose | pages [22] -->
m

<!-- b006266 | prose | pages [22] -->
m

<!-- b006267 | prose | pages [22] -->
m

<!-- b006268 | prose | pages [22] -->
m

<!-- b006269 | prose | pages [22] -->
m

<!-- b006270 | prose | pages [22] -->
m

<!-- b006271 | prose | pages [22] -->
m

<!-- b006272 | prose | pages [22] -->
m

<!-- b006273 | prose | pages [22] -->
m

<!-- b006274 | prose | pages [22] -->
m

<!-- b006275 | prose | pages [22] -->
m

<!-- b006276 | prose | pages [22] -->
m

<!-- b006277 | prose | pages [22] -->
m

<!-- b006278 | prose | pages [22] -->
m

<!-- b006279 | prose | pages [22] -->
m

<!-- b006280 | prose | pages [22] -->
m

<!-- b006281 | prose | pages [22] -->
m

<!-- b006282 | prose | pages [22] -->
m

<!-- b006283 | prose | pages [22] -->
m

<!-- b006284 | prose | pages [22] -->
m

<!-- b006285 | prose | pages [22] -->
m

<!-- b006286 | prose | pages [22] -->
m

<!-- b006287 | prose | pages [22] -->
m

<!-- b006288 | prose | pages [22] -->
m

<!-- b006289 | prose | pages [22] -->
m

<!-- b006290 | prose | pages [22] -->
m

<!-- b006291 | prose | pages [22] -->
m

<!-- b006292 | prose | pages [22] -->
m

<!-- b006293 | prose | pages [22] -->
m

<!-- b006294 | prose | pages [22] -->
m

<!-- b006295 | prose | pages [22] -->
m

<!-- b006296 | prose | pages [22] -->
m

<!-- b006297 | prose | pages [22] -->
m

<!-- b006298 | prose | pages [22] -->
m

<!-- b006299 | prose | pages [22] -->
m

<!-- b006300 | prose | pages [22] -->
m

<!-- b006301 | prose | pages [22] -->
m

<!-- b006302 | prose | pages [22] -->
m

<!-- b006303 | prose | pages [22] -->
m

<!-- b006304 | prose | pages [22] -->
m

<!-- b006305 | prose | pages [22] -->
m

<!-- b006306 | prose | pages [22] -->
m

<!-- b006307 | prose | pages [22] -->
m

<!-- b006308 | prose | pages [22] -->
m

<!-- b006309 | prose | pages [22] -->
m

<!-- b006310 | prose | pages [22] -->
m

<!-- b006311 | prose | pages [22] -->
m

<!-- b006312 | prose | pages [22] -->
m

<!-- b006313 | prose | pages [22] -->
m

<!-- b006314 | prose | pages [22] -->
m

<!-- b006315 | prose | pages [22] -->
m

<!-- b006316 | prose | pages [22] -->
m

<!-- b006317 | prose | pages [22] -->
m

<!-- b006318 | prose | pages [22] -->
m

<!-- b006319 | prose | pages [22] -->
m

<!-- b006320 | prose | pages [22] -->
m

<!-- b006321 | prose | pages [22] -->
m

<!-- b006322 | prose | pages [22] -->
m

<!-- b006323 | prose | pages [22] -->
m

<!-- b006324 | prose | pages [22] -->
m

<!-- b006325 | prose | pages [22] -->
m

<!-- b006326 | prose | pages [22] -->
m

<!-- b006327 | prose | pages [22] -->
m

<!-- b006328 | prose | pages [22] -->
m

<!-- b006329 | prose | pages [22] -->
m

<!-- b006330 | prose | pages [22] -->
m

<!-- b006331 | prose | pages [22] -->
m

<!-- b006332 | prose | pages [22] -->
m

<!-- b006333 | prose | pages [22] -->
6.1

<!-- b006334 | heading | pages [22] -->
Sensitivity Analysis

<!-- b006335 | prose | pages [22] -->
m

<!-- b006336 | prose | pages [22] -->
m

<!-- b006337 | prose | pages [22] -->
m

<!-- b006338 | prose | pages [22] -->
m

<!-- b006339 | prose | pages [22] -->
m

<!-- b006340 | prose | pages [22] -->
m

<!-- b006341 | prose | pages [22] -->
m

<!-- b006342 | prose | pages [22] -->
m

<!-- b006343 | prose | pages [22] -->
m

<!-- b006344 | prose | pages [22] -->
m

<!-- b006345 | prose | pages [22] -->
m

<!-- b006346 | prose | pages [22] -->
m

<!-- b006347 | prose | pages [22] -->
m

<!-- b006348 | prose | pages [22] -->
m

<!-- b006349 | prose | pages [22] -->
m

<!-- b006350 | prose | pages [22] -->
m

<!-- b006351 | prose | pages [22] -->
m

<!-- b006352 | prose | pages [22] -->
m

<!-- b006353 | prose | pages [22] -->
m

<!-- b006354 | prose | pages [22] -->
m

<!-- b006355 | prose | pages [22] -->
m

<!-- b006356 | prose | pages [22] -->
m

<!-- b006357 | prose | pages [22] -->
m

<!-- b006358 | prose | pages [22] -->
m

<!-- b006359 | prose | pages [22] -->
m

<!-- b006360 | prose | pages [22] -->
m

<!-- b006361 | prose | pages [22] -->
m

<!-- b006362 | prose | pages [22] -->
m

<!-- b006363 | prose | pages [22] -->
m

<!-- b006364 | prose | pages [22] -->
m

<!-- b006365 | prose | pages [22] -->
m

<!-- b006366 | prose | pages [22] -->
m

<!-- b006367 | prose | pages [22] -->
m

<!-- b006368 | prose | pages [22] -->
m

<!-- b006369 | prose | pages [22] -->
m

<!-- b006370 | prose | pages [22] -->
m

<!-- b006371 | prose | pages [22] -->
m

<!-- b006372 | prose | pages [22] -->
m

<!-- b006373 | prose | pages [22] -->
m

<!-- b006374 | prose | pages [22] -->
m

<!-- b006375 | prose | pages [22] -->
m

<!-- b006376 | prose | pages [22] -->
m

<!-- b006377 | prose | pages [22] -->
m

<!-- b006378 | prose | pages [22] -->
m

<!-- b006379 | prose | pages [22] -->
m

<!-- b006380 | prose | pages [22] -->
m

<!-- b006381 | prose | pages [22] -->
m

<!-- b006382 | prose | pages [22] -->
m

<!-- b006383 | prose | pages [22] -->
m

<!-- b006384 | prose | pages [22] -->
m

<!-- b006385 | prose | pages [22] -->
m

<!-- b006386 | prose | pages [22] -->
m

<!-- b006387 | prose | pages [22] -->
m

<!-- b006388 | prose | pages [22] -->
m

<!-- b006389 | prose | pages [22] -->
m

<!-- b006390 | prose | pages [22] -->
m

<!-- b006391 | prose | pages [22] -->
m

<!-- b006392 | prose | pages [22] -->
m

<!-- b006393 | prose | pages [22] -->
m

<!-- b006394 | prose | pages [22] -->
m

<!-- b006395 | prose | pages [22] -->
m

<!-- b006396 | prose | pages [22] -->
m

<!-- b006397 | prose | pages [22] -->
m

<!-- b006398 | prose | pages [22] -->
m

<!-- b006399 | prose | pages [22] -->
m

<!-- b006400 | prose | pages [22] -->
m

<!-- b006401 | prose | pages [22] -->
m

<!-- b006402 | prose | pages [22] -->
m

<!-- b006403 | prose | pages [22] -->
m

<!-- b006404 | prose | pages [22] -->
m

<!-- b006405 | prose | pages [22] -->
m

<!-- b006406 | prose | pages [22] -->
m

<!-- b006407 | prose | pages [22] -->
m

<!-- b006408 | prose | pages [22] -->
m

<!-- b006409 | prose | pages [22] -->
m

<!-- b006410 | prose | pages [22] -->
m

<!-- b006411 | prose | pages [22] -->
m

<!-- b006412 | prose | pages [22] -->
m

<!-- b006413 | prose | pages [22] -->
m

<!-- b006414 | prose | pages [22] -->
m

<!-- b006415 | prose | pages [22] -->
m

<!-- b006416 | prose | pages [22] -->
m

<!-- b006417 | prose | pages [22] -->
m

<!-- b006418 | prose | pages [22] -->
m

<!-- b006419 | prose | pages [22] -->
m

<!-- b006420 | prose | pages [22] -->
m

<!-- b006421 | prose | pages [22] -->
m

<!-- b006422 | prose | pages [22] -->
m

<!-- b006423 | prose | pages [22] -->
m

<!-- b006424 | prose | pages [22] -->
m

<!-- b006425 | prose | pages [22] -->
m

<!-- b006426 | prose | pages [22] -->
m

<!-- b006427 | prose | pages [22] -->
m

<!-- b006428 | prose | pages [22] -->
m

<!-- b006429 | prose | pages [22] -->
m

<!-- b006430 | prose | pages [22] -->
m

<!-- b006431 | prose | pages [22] -->
m

<!-- b006432 | prose | pages [22] -->
m

<!-- b006433 | prose | pages [22] -->
m

<!-- b006434 | prose | pages [22] -->
m

<!-- b006435 | prose | pages [22] -->
m

<!-- b006436 | prose | pages [22] -->
m

<!-- b006437 | prose | pages [22] -->
m

<!-- b006438 | prose | pages [22] -->
m

<!-- b006439 | prose | pages [22] -->
m

<!-- b006440 | prose | pages [22] -->
m

<!-- b006441 | prose | pages [22] -->
m

<!-- b006442 | prose | pages [22] -->
m

<!-- b006443 | prose | pages [22] -->
m

<!-- b006444 | prose | pages [22] -->
m

<!-- b006445 | prose | pages [22] -->
m

<!-- b006446 | prose | pages [22] -->
m

<!-- b006447 | prose | pages [22] -->
m

<!-- b006448 | prose | pages [22] -->
m

<!-- b006449 | prose | pages [22] -->
m

<!-- b006450 | prose | pages [22] -->
m

<!-- b006451 | prose | pages [22] -->
m

<!-- b006452 | prose | pages [22] -->
m

<!-- b006453 | prose | pages [22] -->
m

<!-- b006454 | prose | pages [22] -->
m

<!-- b006455 | prose | pages [22] -->
m

<!-- b006456 | prose | pages [22] -->
m

<!-- b006457 | prose | pages [22] -->
m

<!-- b006458 | prose | pages [22] -->
m

<!-- b006459 | prose | pages [22] -->
m

<!-- b006460 | prose | pages [22] -->
m

<!-- b006461 | prose | pages [22] -->
m

<!-- b006462 | prose | pages [22] -->
m

<!-- b006463 | prose | pages [22] -->
m

<!-- b006464 | prose | pages [22] -->
m

<!-- b006465 | prose | pages [22] -->
m

<!-- b006466 | prose | pages [22] -->
m

<!-- b006467 | prose | pages [22] -->
m

<!-- b006468 | prose | pages [22] -->
m

<!-- b006469 | prose | pages [22] -->
m

<!-- b006470 | prose | pages [22] -->
m

<!-- b006471 | prose | pages [22] -->
m

<!-- b006472 | prose | pages [22] -->
m

<!-- b006473 | prose | pages [22] -->
m

<!-- b006474 | prose | pages [22] -->
m

<!-- b006475 | prose | pages [22] -->
m

<!-- b006476 | prose | pages [22] -->
m

<!-- b006477 | prose | pages [22] -->
m

<!-- b006478 | prose | pages [22] -->
m

<!-- b006479 | prose | pages [22] -->
m

<!-- b006480 | prose | pages [22] -->
m

<!-- b006481 | prose | pages [22] -->
m

<!-- b006482 | prose | pages [22] -->
m

<!-- b006483 | prose | pages [22] -->
m

<!-- b006484 | prose | pages [22] -->
m

<!-- b006485 | prose | pages [22] -->
m

<!-- b006486 | prose | pages [22] -->
m

<!-- b006487 | prose | pages [22] -->
m

<!-- b006488 | prose | pages [22] -->
m

<!-- b006489 | prose | pages [22] -->
m

<!-- b006490 | prose | pages [22] -->
m

<!-- b006491 | prose | pages [22] -->
m

<!-- b006492 | prose | pages [22] -->
m

<!-- b006493 | prose | pages [22] -->
m

<!-- b006494 | prose | pages [22] -->
m

<!-- b006495 | prose | pages [22] -->
m

<!-- b006496 | prose | pages [22] -->
m

<!-- b006497 | prose | pages [22] -->
m

<!-- b006498 | prose | pages [22] -->
m

<!-- b006499 | prose | pages [22] -->
m

<!-- b006500 | prose | pages [22] -->
m

<!-- b006501 | prose | pages [22] -->
m

<!-- b006502 | prose | pages [22] -->
m

<!-- b006503 | prose | pages [22] -->
m

<!-- b006504 | prose | pages [22] -->
m

<!-- b006505 | prose | pages [22] -->
m

<!-- b006506 | prose | pages [22] -->
m

<!-- b006507 | prose | pages [22] -->
m

<!-- b006508 | prose | pages [22] -->
m

<!-- b006509 | prose | pages [22] -->
m

<!-- b006510 | prose | pages [22] -->
m

<!-- b006511 | prose | pages [22] -->
m

<!-- b006512 | prose | pages [22] -->
m

<!-- b006513 | prose | pages [22] -->
m

<!-- b006514 | prose | pages [22] -->
m

<!-- b006515 | prose | pages [22] -->
m

<!-- b006516 | prose | pages [22] -->
m

<!-- b006517 | prose | pages [22] -->
m

<!-- b006518 | prose | pages [22] -->
m

<!-- b006519 | prose | pages [22] -->
m

<!-- b006520 | prose | pages [22] -->
m

<!-- b006521 | prose | pages [22] -->
m

<!-- b006522 | prose | pages [22] -->
m

<!-- b006523 | prose | pages [22] -->
m

<!-- b006524 | prose | pages [22] -->
m

<!-- b006525 | prose | pages [22] -->
m

<!-- b006526 | prose | pages [22] -->
m

<!-- b006527 | prose | pages [22] -->
m

<!-- b006528 | prose | pages [22] -->
m

<!-- b006529 | prose | pages [22] -->
m

<!-- b006530 | prose | pages [22] -->
m

<!-- b006531 | prose | pages [22] -->
m

<!-- b006532 | prose | pages [22] -->
m

<!-- b006533 | prose | pages [22] -->
m

<!-- b006534 | prose | pages [22] -->
m

<!-- b006535 | prose | pages [22] -->
m

<!-- b006536 | prose | pages [22] -->
m

<!-- b006537 | prose | pages [22] -->
m

<!-- b006538 | prose | pages [22] -->
m

<!-- b006539 | prose | pages [22] -->
m

<!-- b006540 | prose | pages [22] -->
m

<!-- b006541 | prose | pages [22] -->
m

<!-- b006542 | prose | pages [22] -->
m

<!-- b006543 | prose | pages [22] -->
m

<!-- b006544 | prose | pages [22] -->
m

<!-- b006545 | prose | pages [22] -->
m

<!-- b006546 | prose | pages [22] -->
m

<!-- b006547 | prose | pages [22] -->
m

<!-- b006548 | prose | pages [22] -->
We performed 5-fold cross-validation, and the results are shown in Table 6. To further analyze

<!-- b006549 | prose | pages [22] -->
m

<!-- b006550 | prose | pages [22] -->
m

<!-- b006551 | prose | pages [22] -->
m

<!-- b006552 | prose | pages [22] -->
m

<!-- b006553 | prose | pages [22] -->
m

<!-- b006554 | prose | pages [22] -->
m

<!-- b006555 | prose | pages [22] -->
m

<!-- b006556 | prose | pages [22] -->
m

<!-- b006557 | prose | pages [22] -->
m

<!-- b006558 | prose | pages [22] -->
m

<!-- b006559 | prose | pages [22] -->
m

<!-- b006560 | prose | pages [22] -->
m

<!-- b006561 | prose | pages [22] -->
m

<!-- b006562 | prose | pages [22] -->
m

<!-- b006563 | prose | pages [22] -->
m

<!-- b006564 | prose | pages [22] -->
m

<!-- b006565 | prose | pages [22] -->
m

<!-- b006566 | prose | pages [22] -->
m

<!-- b006567 | prose | pages [22] -->
m

<!-- b006568 | prose | pages [22] -->
m

<!-- b006569 | prose | pages [22] -->
m

<!-- b006570 | prose | pages [22] -->
m

<!-- b006571 | prose | pages [22] -->
m

<!-- b006572 | prose | pages [22] -->
m

<!-- b006573 | prose | pages [22] -->
m

<!-- b006574 | prose | pages [22] -->
m

<!-- b006575 | prose | pages [22] -->
m

<!-- b006576 | prose | pages [22] -->
m

<!-- b006577 | prose | pages [22] -->
m

<!-- b006578 | prose | pages [22] -->
m

<!-- b006579 | prose | pages [22] -->
m

<!-- b006580 | prose | pages [22] -->
m

<!-- b006581 | prose | pages [22] -->
m

<!-- b006582 | prose | pages [22] -->
m

<!-- b006583 | prose | pages [22] -->
m

<!-- b006584 | prose | pages [22] -->
m

<!-- b006585 | prose | pages [22] -->
m

<!-- b006586 | prose | pages [22] -->
m

<!-- b006587 | prose | pages [22] -->
m

<!-- b006588 | prose | pages [22] -->
m

<!-- b006589 | prose | pages [22] -->
m

<!-- b006590 | prose | pages [22] -->
m

<!-- b006591 | prose | pages [22] -->
m

<!-- b006592 | prose | pages [22] -->
m

<!-- b006593 | prose | pages [22] -->
m

<!-- b006594 | prose | pages [22] -->
m

<!-- b006595 | prose | pages [22] -->
m

<!-- b006596 | prose | pages [22] -->
m

<!-- b006597 | prose | pages [22] -->
m

<!-- b006598 | prose | pages [22] -->
m

<!-- b006599 | prose | pages [22] -->
m

<!-- b006600 | prose | pages [22] -->
m

<!-- b006601 | prose | pages [22] -->
m

<!-- b006602 | prose | pages [22] -->
m

<!-- b006603 | prose | pages [22] -->
m

<!-- b006604 | prose | pages [22] -->
m

<!-- b006605 | prose | pages [22] -->
m

<!-- b006606 | prose | pages [22] -->
m

<!-- b006607 | prose | pages [22] -->
m

<!-- b006608 | prose | pages [22] -->
m

<!-- b006609 | prose | pages [22] -->
m

<!-- b006610 | prose | pages [22] -->
m

<!-- b006611 | prose | pages [22] -->
m

<!-- b006612 | prose | pages [22] -->
m

<!-- b006613 | prose | pages [22] -->
m

<!-- b006614 | prose | pages [22] -->
m

<!-- b006615 | prose | pages [22] -->
m

<!-- b006616 | prose | pages [22] -->
m

<!-- b006617 | prose | pages [22] -->
m

<!-- b006618 | prose | pages [22] -->
m

<!-- b006619 | prose | pages [22] -->
m

<!-- b006620 | prose | pages [22] -->
m

<!-- b006621 | prose | pages [22] -->
m

<!-- b006622 | prose | pages [22] -->
m

<!-- b006623 | prose | pages [22] -->
m

<!-- b006624 | prose | pages [22] -->
m

<!-- b006625 | prose | pages [22] -->
m

<!-- b006626 | prose | pages [22] -->
m

<!-- b006627 | prose | pages [22] -->
m

<!-- b006628 | prose | pages [22] -->
m

<!-- b006629 | prose | pages [22] -->
m

<!-- b006630 | prose | pages [22] -->
m

<!-- b006631 | prose | pages [22] -->
m

<!-- b006632 | prose | pages [22] -->
m

<!-- b006633 | prose | pages [22] -->
m

<!-- b006634 | prose | pages [22] -->
m

<!-- b006635 | prose | pages [22] -->
m

<!-- b006636 | prose | pages [22] -->
m

<!-- b006637 | prose | pages [22] -->
m

<!-- b006638 | prose | pages [22] -->
m

<!-- b006639 | prose | pages [22] -->
m

<!-- b006640 | prose | pages [22] -->
m

<!-- b006641 | prose | pages [22] -->
m

<!-- b006642 | prose | pages [22] -->
m

<!-- b006643 | prose | pages [22] -->
m

<!-- b006644 | prose | pages [22] -->
m

<!-- b006645 | prose | pages [22] -->
m

<!-- b006646 | prose | pages [22] -->
m

<!-- b006647 | prose | pages [22] -->
m

<!-- b006648 | prose | pages [22] -->
m

<!-- b006649 | prose | pages [22] -->
m

<!-- b006650 | prose | pages [22] -->
m

<!-- b006651 | prose | pages [22] -->
m

<!-- b006652 | prose | pages [22] -->
the sensitivity of our model, we varied the size of the training set by randomly sampling 60%, 70%, and 80% of the original dataset for training and prediction. The resulting fitting curves and changes in information gain are shown in Figure 12 and Figure 13.

<!-- b006653 | prose | pages [22] -->
120

<!-- b006654 | prose | pages [22] -->
100

<!-- b006655 | prose | pages [22] -->
80

<!-- b006656 | prose | pages [22] -->
Total

<!-- b006657 | prose | pages [22] -->
60

<!-- b006658 | prose | pages [22] -->
40

<!-- b006659 | prose | pages [22] -->
20

<!-- b006660 | prose | pages [22] -->
0

<!-- b006661 | prose | pages [22] -->
0 10 20

<!-- b006662 | prose | pages [22] -->
Actual Predicted (80% Train) Predicted (70% Train) Predicted (60% Train)

<!-- b006663 | prose | pages [22] -->
30 40 Different NOC for each Olympic Games

<!-- b006664 | caption | pages [22] -->
Figure 12: Fitting curves of different dataset

<!-- b006665 | prose | pages [22] -->
Changes in the training set size resulted in a slight decrease in predictive performance; however, the magnitude of this decrease was minimal. With training sets comprising 60%, 70%, 75%, and 80% of the original data, the model’s information gain remained relatively stable. Between 70% and 80%, minor fluctuations in the importance of the AAPI and N_E features were observed. Overall, these two features exhibited a tendency towards increased importance compared to the 60% training set. In conclusion, our model demonstrates good robustness.

<!-- b006666 | prose | pages [22] -->
6.2

<!-- b006667 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b006668 | heading | pages [22] -->
Strengths:

<!-- b006669 | prose | pages [22] -->
1. We introduced a novel metric, the Athlete Potential Index (API), to assess athlete perfor- mance. This index played a significant role in model training and improved predictive accu- racy.

<!-- b006670 | prose | pages [22] -->
关注数学模型

<!-- b006671 | furniture | pages [22] -->
2

<!-- b006672 | furniture | pages [22] -->
MATHmodels

<!-- b006673 | furniture | pages [22] -->
获取更多资讯

<!-- b006674 | furniture | pages [23] -->
Team #2510185

<!-- b006675 | furniture | pages [23] -->
Page 23 of 24

<!-- b006676 | prose | pages [23] -->
微信公众号：数学模型

<!-- b006677 | prose | pages [23] -->
微信号：MATHmodels

<!-- b006678 | caption | pages [23] -->
Figure 13: Changes in information gain

<!-- b006679 | prose | pages [23] -->
2. Through a comparative analysis of Linear Regression, XGBoost, and Random Forest mod- els, we selected the optimal model for medal prediction. In the prediction set, our model achieved an R-squared (R²) value exceeding 0.87, indicating a strong goodness of fit.

<!-- b006680 | prose | pages [23] -->
3. Rigorous validation through 5-fold cross-validation and sensitivity analysis demonstrated the robustness of our model to variations in training data.

<!-- b006681 | prose | pages [23] -->
4. For the binary classification task of predicting medal acquisition (yes/no), we employed a BP neural network classifier, achieving an Area Under the ROC Curve (AUC) of 0.94, demonstrating excellent discriminatory power.

<!-- b006682 | prose | pages [23] -->
5. We provided an Event Potential Index (EPI) to guide national Olympic committees in eval- uating the potential return on investment of hiring world-class coaches for specific sports.

<!-- b006683 | heading | pages [23] -->
Weaknesses:

<!-- b006684 | prose | pages [23] -->
1. The performance of the binary classifier could potentially be further enhanced with a larger training dataset, which may lead to more reliable and generalizable results.

<!-- b006685 | prose | pages [23] -->
2. Predicting the “Great Coach” effect presents challenges in definitively identifying and quan- tifying the performance difference between existing coaches and world-class coaches. This inherent difficulty introduces uncertainty into the estimation of the coach’s contribution.

<!-- b006686 | prose | pages [23] -->
3. While we introduced the Event Potential Index (EPI), further research is needed to develop a more precise and quantitative definition of this metric, enabling more accurate and nuanced analysis.

<!-- b006687 | furniture | pages [24] -->
Team #2510185

<!-- b006688 | prose | pages [24] -->
7

<!-- b006689 | heading | pages [24] -->
Conclusions

<!-- b006690 | furniture | pages [24] -->
Page 24 of 24

<!-- b006691 | prose | pages [24] -->
In this paper, we employed a BP neural network classifier and a random forest regression model to predict the medal count for the 2028 Los Angeles Olympic Games, providing predic- tion intervals. We also assessed the key sports contributing to medal acquisition for six specific nations, identifying the sports responsible for the majority of their medals. Our analysis suggests that including locally popular or dominant sports as new Olympic events can positively impact the host nation’s medal count. We provided evidence supporting the “Great Coach” effect, estimating its contribution to be up to 28.8%, and identified potential coaching interventions for three na- tions (China, Jamaica, and Germany) projected to yield an increase of approximately 1.6 medals. Finally, we presented original insights regarding non-medal-winning nations, the importance of specific sports, and the impact of world-class coaches.

<!-- b006692 | heading | pages [24] -->
References

<!-- b006693 | references | pages [24] -->
[1] https://en.wikipedia.org/wiki/Olympic_Games.

<!-- b006694 | references | pages [24] -->
[2] https://olympics.com/en/paris-2024/medals.

<!-- b006695 | references | pages [24] -->
[3] C. Schlembach, S. L. Schmidt, D. Schreyer, and L. Wunderlich, “Forecasting the olympic

<!-- b006696 | references | pages [24] -->
medal distribution – a socioeconomic machine learning model,” Technological Forecasting

<!-- b006697 | references | pages [24] -->
and Social Change, vol. 175, p. 121314, 2022.

<!-- b006698 | references | pages [24] -->
[4] https://www.nielsen.com/news-center/2024/virtual-medal-table-forecast/.

<!-- b006699 | references | pages [24] -->
[5] M. A. Ruiz Estrada, “A new indicator to evaluate any country performance in the olympic

<!-- b006700 | references | pages [24] -->
games: The olympia-index,” Available at SSRN 4920383, 2024.

<!-- b006701 | references | pages [24] -->
[6] https://www.thepaper.cn/newsDetail_forward_16567025.

<!-- b006702 | references | pages [24] -->
[7] J. Luo, “Research on the change of the project setting of the modern summer olympic games

<!-- b006703 | references | pages [24] -->
(1984-2020),” Ph.D. dissertation, Changsha: Hunan Normal University 2020, 2020.

<!-- b006704 | references | pages [24] -->
[8] https://www.olympics.com/zh/athletes/ping-lang.

<!-- b006705 | references | pages [24] -->
关注数学模型

<!-- b006706 | furniture | pages [24] -->
2

<!-- b006707 | furniture | pages [24] -->
MATHmodels

<!-- b006708 | furniture | pages [24] -->
获取更多资讯
