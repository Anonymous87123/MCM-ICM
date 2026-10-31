# P-C-2025-2507817-87c90f39

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2025

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2507817

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Olympic Medals Unveiled:

<!-- b000009 | title | pages [1] -->
A Mathematical Exploration of Achievement Trends

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
In the Olympic Games, the pinnacle of sports competition, the quest for medals reflects not only the physical prowess of athletes but also the overall strength of their countries. As competitive sports evolve, medal rankings shift over time. This paper analyzes the key factors influencing Olympic performance and explores future trends in the medal competition landscape from various perspectives.

<!-- b000013 | prose | pages [1] -->
For Task 1, we developed a Grid-Search Random Forest (GSRF) prediction model using preprocessed data. Through Cross-Validation, we obtained correlation coefficients for predicting the number of gold medals and the total medals, which were 0.710 and 0.784, respectively, validating the model. Based on this model, we projected the gold and total medal standings for the 2028 Olympic Games, concluding that China and the United States are likely

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
to continue leading in both categories. We also calculated prediction intervals using the t- distribution, as shown in Figure 9. Additionally, we identified the countries most likely to advance and regress, which are illustrated in Figure 10.

<!-- b000016 | prose | pages [1] -->
For Task 2, we established a Logistic Regression Model to classify countries that have not yet won medals in the 2028 Olympic Games into two categories: winners and non-winners. This transformed the probability of winning a medal into a binary classification problem. We selected appropriate feature variables and calculated the weights of each feature vector using the maximum likelihood estimation method. By applying the sigmoid function and L1 regularization, we identified countries with a higher likelihood of winning medals among those yet to medal, as shown in Table 11.

<!-- b000017 | prose | pages [1] -->
For Task 3, based on the results of Task 1, we calculated the number of medals won by each country in each event and quantified the significance of each event’s contributions by calculating the ratio of medals in that event to total medals. We noted that some countries (e.g., KOS in Judo) have achieved their only medals through specific programs that are particularly critical for them. Overall, countries tend to prioritize sports in which they have both strengths and potential to optimize their chances of winning more medals.

<!-- b000018 | prose | pages [1] -->
For Task 4, we created a “Great Coach” Model. By quantifying the weights of medals and calculating the scores of each country, we identified that there were “Great Coach” in women's gymnastics in Romania and the United States, and the Spearman's Correlation Coefficient between their scores and the scores of these two countries was 0.874. After building the model by using the Lasso Regression, we selected three countries and identify sports and applied it to them. After the introduction of the “Great Coach” concept, the predicted scores for each country in 2028 are presented in Table 15, with Romania showing a remarkable increase from a score of 3 to 36.65.

<!-- b000019 | prose | pages [1] -->
Finally, we offer original insights for the IOC regarding the host effect and the impact of talented athletes. Additionally, we performed a sensitivity analysis that demonstrated the model's stability and robustness following perturbations.

<!-- b000020 | keywords | pages [1] -->
Keywords: Olympic；GSRF；Logistic Regression；Lasso Regression

<!-- b000021 | furniture | pages [2] -->
Page 2 of 25

<!-- b000022 | furniture | pages [2] -->
Team#2507817

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
Introduction.

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
1.1 Background.

<!-- b000027 | prose | pages [2] -->
.3

<!-- b000028 | heading | pages [2] -->
1.2 Clarifications and Restatements..

<!-- b000029 | prose | pages [2] -->
.3

<!-- b000030 | prose | pages [2] -->
1.3 Our work.

<!-- b000031 | heading | pages [2] -->
Basic Assumption

<!-- b000032 | prose | pages [2] -->
2

<!-- b000033 | prose | pages [2] -->
Symbols. 3 5

<!-- b000034 | prose | pages [2] -->
4 Data Preprocessing Task 1 Predicting Gold & Total Medals Based on GSRF Model.... 5 6

<!-- b000035 | heading | pages [2] -->
5.1 GSRF Prediction Model..

<!-- b000036 | heading | pages [2] -->
5.2 Predicting the 2028 Gold & Medal Tables .

<!-- b000037 | prose | pages [2] -->
.11

<!-- b000038 | prose | pages [2] -->
Task 2 Projections for Non-Awarded Countries 13 6

<!-- b000039 | prose | pages [2] -->
.13

<!-- b000040 | heading | pages [2] -->
6.1 Bicategory Logistic Regression Modeling

<!-- b000041 | prose | pages [2] -->
●

<!-- b000042 | heading | pages [2] -->
6.2 Bicategory Logistic Regression Results

<!-- b000043 | prose | pages [2] -->
.14 Task 3 Relationship Between Sports and Medals .17 7

<!-- b000044 | prose | pages [2] -->
.17

<!-- b000045 | heading | pages [2] -->
7.1 Relationship of the Sports to gold medals & total medals..

<!-- b000046 | heading | pages [2] -->
7.2 The most Important Sports for the Country.

<!-- b000047 | prose | pages [2] -->
.17

<!-- b000048 | heading | pages [2] -->
7.3 Impact of Nationally Selected Sports on results ..,

<!-- b000049 | prose | pages [2] -->
.18 Task 4 The Impact of Great Coach 19 8

<!-- b000050 | heading | pages [2] -->
8.1 Lasso Regression Model.

<!-- b000051 | prose | pages [2] -->
.19 .21

<!-- b000052 | heading | pages [2] -->
8.2 Lasso Regression Results.

<!-- b000053 | prose | pages [2] -->
Task 5 Original Opinion... 22 9

<!-- b000054 | heading | pages [2] -->
9.1 Host Effect

<!-- b000055 | prose | pages [2] -->
.22

<!-- b000056 | heading | pages [2] -->
9.2 Talented Athletes

<!-- b000057 | prose | pages [2] -->
.23 Error Analysis and Sensitivity Analysis. .23 10 ● .23

<!-- b000058 | heading | pages [2] -->
10.1 Definition of Sensitivity.

<!-- b000059 | prose | pages [2] -->
.24

<!-- b000060 | heading | pages [2] -->
10.2 Impact of Athletes Number, Gold & Total Medals on Predicted Results

<!-- b000061 | prose | pages [2] -->
11 .24 Evaluation of Model. 12 25

<!-- b000062 | heading | pages [2] -->
References

<!-- b000063 | references | pages [2] -->
关注数学模型

<!-- b000064 | furniture | pages [2] -->
获取更多资讯

<!-- b000065 | furniture | pages [3] -->
Team#2507817                                                             Page 3 of 25

<!-- b000066 | heading | pages [3] -->
1 Introduction

<!-- b000067 | heading | pages [3] -->
1.1 Background

<!-- b000068 | prose | pages [3] -->
When viewers follow the Summer Olympics, they appreciate the performance of the athletes as well as the medal standings. Since 1896, sports powerhouses such as the United 微信公众号：数学模型 States have been at the top of the list, demonstrating their strength. Countries that have won many gold medals are globally recognized, and countries that have won their first Olympic medals are celebrated, marking historical milestones. Here are the top 10 medalists for the 2024 Summer Olympics:

<!-- b000069 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000070 | caption | pages [3] -->
Figure 1 Medal list of 2024 Summer Olympic Games

<!-- b000071 | heading | pages [3] -->
1.2 Clarifications and Restatements

<!-- b000072 | prose | pages [3] -->
In this problem, models need to be developed to predict the medal table using relevant event and athlete data. Based on the data of previous years' Summer Olympics medal table, host country, number of events and participants, the analysis deals with the following problems: Task 1 Predicts the medal standings for the 2028 Summer Olympics based on a model, giving prediction intervals that include each statistic, indicating the countries most likely to make progress and regress.

<!-- b000073 | prose | pages [3] -->
 The feature values affecting the number of medals are counted and integrated into a dataset for model training and testing. After model validation, predict the number of gold medals and total medals for each country in 2028 based on 2024 data, calculate prediction intervals and visualize them. Task 2 For countries that have not yet won a medal, predict how many countries will win their first medal at the next Olympic Games and calculate their probability  Essentially, it is a classification problem that categorizes the predicted outcomes of non-winning countries in 2028 into two categories: winning and not winning.

<!-- b000074 | prose | pages [3] -->
Judgment calculates how probable it is that the country falls into the winning category. Task 3 Consider the effect of the number and type of sports in previous Olympic Games on the number of medals won by each country. Determine the most important sport for each country and give reasons. Also consider the effect of the host country's choice of sport on the results.

<!-- b000075 | prose | pages [3, 4] -->
 We sort out the cumulative number of medals for each country and analyze the relationship. Also introduce a concept that can quantify the importance of the program to the country. Use the data to make judgments and explain why. Task 4 Predict the contribution of the "great coach" effect to the number of medals. Select m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m three countries and consider the sports in which "great coaches" should be introduced and estimate their impact.

<!-- b000076 | furniture | pages [3] -->
m

<!-- b000077 | furniture | pages [3] -->
m

<!-- b000078 | furniture | pages [3] -->
m

<!-- b000079 | furniture | pages [3] -->
m

<!-- b000080 | furniture | pages [3] -->
m

<!-- b000081 | furniture | pages [3] -->
m

<!-- b000082 | furniture | pages [3] -->
m

<!-- b000083 | furniture | pages [3] -->
m

<!-- b000084 | furniture | pages [3] -->
m

<!-- b000085 | furniture | pages [3] -->
m

<!-- b000086 | furniture | pages [3] -->
m

<!-- b000087 | furniture | pages [3] -->
m

<!-- b000088 | furniture | pages [3] -->
m

<!-- b000089 | furniture | pages [3] -->
m

<!-- b000090 | furniture | pages [3] -->
m

<!-- b000091 | furniture | pages [3] -->
m

<!-- b000092 | furniture | pages [3] -->
m

<!-- b000093 | furniture | pages [3] -->
m

<!-- b000094 | furniture | pages [3] -->
m

<!-- b000095 | furniture | pages [3] -->
m

<!-- b000096 | furniture | pages [3] -->
m

<!-- b000097 | furniture | pages [3] -->
m

<!-- b000098 | furniture | pages [3] -->
m

<!-- b000099 | furniture | pages [3] -->
m

<!-- b000100 | furniture | pages [3] -->
m

<!-- b000101 | furniture | pages [3] -->
m

<!-- b000102 | furniture | pages [3] -->
m

<!-- b000103 | furniture | pages [3] -->
m

<!-- b000104 | furniture | pages [3] -->
m

<!-- b000105 | furniture | pages [3] -->
m

<!-- b000106 | furniture | pages [3] -->
m

<!-- b000107 | furniture | pages [3] -->
m

<!-- b000108 | furniture | pages [3] -->
m

<!-- b000109 | furniture | pages [3] -->
m

<!-- b000110 | furniture | pages [3] -->
m

<!-- b000111 | furniture | pages [3] -->
m

<!-- b000112 | furniture | pages [3] -->
m

<!-- b000113 | furniture | pages [3] -->
m

<!-- b000114 | furniture | pages [3] -->
m

<!-- b000115 | furniture | pages [3] -->
m

<!-- b000116 | furniture | pages [3] -->
m

<!-- b000117 | furniture | pages [3] -->
m

<!-- b000118 | furniture | pages [3] -->
m

<!-- b000119 | furniture | pages [3] -->
m

<!-- b000120 | furniture | pages [3] -->
m

<!-- b000121 | furniture | pages [3] -->
m

<!-- b000122 | furniture | pages [3] -->
m

<!-- b000123 | furniture | pages [3] -->
m

<!-- b000124 | furniture | pages [3] -->
m

<!-- b000125 | furniture | pages [3] -->
m

<!-- b000126 | furniture | pages [3] -->
m

<!-- b000127 | furniture | pages [3] -->
m

<!-- b000128 | furniture | pages [3] -->
m

<!-- b000129 | furniture | pages [3] -->
m

<!-- b000130 | furniture | pages [3] -->
m

<!-- b000131 | furniture | pages [3] -->
m

<!-- b000132 | furniture | pages [3] -->
m

<!-- b000133 | furniture | pages [3] -->
m

<!-- b000134 | furniture | pages [3] -->
m

<!-- b000135 | furniture | pages [3] -->
m

<!-- b000136 | furniture | pages [3] -->
m

<!-- b000137 | furniture | pages [3] -->
m

<!-- b000138 | furniture | pages [3] -->
m

<!-- b000139 | furniture | pages [3] -->
m

<!-- b000140 | furniture | pages [3] -->
m

<!-- b000141 | furniture | pages [3] -->
m

<!-- b000142 | furniture | pages [3] -->
m

<!-- b000143 | furniture | pages [3] -->
m

<!-- b000144 | furniture | pages [3] -->
m

<!-- b000145 | furniture | pages [3] -->
m

<!-- b000146 | furniture | pages [3] -->
m

<!-- b000147 | furniture | pages [3] -->
m

<!-- b000148 | furniture | pages [3] -->
m

<!-- b000149 | furniture | pages [3] -->
m

<!-- b000150 | furniture | pages [3] -->
m

<!-- b000151 | furniture | pages [3] -->
m

<!-- b000152 | furniture | pages [3] -->
m

<!-- b000153 | furniture | pages [3] -->
m

<!-- b000154 | furniture | pages [3] -->
m

<!-- b000155 | furniture | pages [3] -->
m

<!-- b000156 | furniture | pages [3] -->
m

<!-- b000157 | furniture | pages [3] -->
m

<!-- b000158 | furniture | pages [3] -->
m

<!-- b000159 | furniture | pages [3] -->
m

<!-- b000160 | furniture | pages [3] -->
m

<!-- b000161 | furniture | pages [3] -->
m

<!-- b000162 | furniture | pages [3] -->
m

<!-- b000163 | furniture | pages [3] -->
m

<!-- b000164 | furniture | pages [3] -->
m

<!-- b000165 | furniture | pages [3] -->
m

<!-- b000166 | furniture | pages [3] -->
m

<!-- b000167 | furniture | pages [3] -->
m

<!-- b000168 | furniture | pages [3] -->
m

<!-- b000169 | furniture | pages [3] -->
m

<!-- b000170 | furniture | pages [3] -->
m

<!-- b000171 | furniture | pages [3] -->
m

<!-- b000172 | furniture | pages [3] -->
m

<!-- b000173 | furniture | pages [3] -->
m

<!-- b000174 | furniture | pages [3] -->
m

<!-- b000175 | furniture | pages [3] -->
m

<!-- b000176 | furniture | pages [3] -->
m

<!-- b000177 | furniture | pages [3] -->
m

<!-- b000178 | furniture | pages [3] -->
m

<!-- b000179 | furniture | pages [3] -->
m

<!-- b000180 | furniture | pages [3] -->
m

<!-- b000181 | furniture | pages [3] -->
m

<!-- b000182 | furniture | pages [3] -->
m

<!-- b000183 | furniture | pages [3] -->
m

<!-- b000184 | furniture | pages [3] -->
m

<!-- b000185 | furniture | pages [3] -->
m

<!-- b000186 | furniture | pages [3] -->
m

<!-- b000187 | furniture | pages [3] -->
m

<!-- b000188 | furniture | pages [3] -->
m

<!-- b000189 | furniture | pages [3] -->
m

<!-- b000190 | furniture | pages [3] -->
m

<!-- b000191 | furniture | pages [3] -->
m

<!-- b000192 | furniture | pages [3] -->
m

<!-- b000193 | furniture | pages [3] -->
m

<!-- b000194 | furniture | pages [3] -->
m

<!-- b000195 | furniture | pages [3] -->
m

<!-- b000196 | furniture | pages [3] -->
m

<!-- b000197 | furniture | pages [3] -->
m

<!-- b000198 | furniture | pages [3] -->
m

<!-- b000199 | furniture | pages [3] -->
m

<!-- b000200 | furniture | pages [3] -->
m

<!-- b000201 | furniture | pages [3] -->
m

<!-- b000202 | furniture | pages [3] -->
m

<!-- b000203 | furniture | pages [3] -->
m

<!-- b000204 | furniture | pages [3] -->
m

<!-- b000205 | furniture | pages [3] -->
m

<!-- b000206 | furniture | pages [3] -->
m

<!-- b000207 | furniture | pages [3] -->
m

<!-- b000208 | furniture | pages [3] -->
m

<!-- b000209 | furniture | pages [3] -->
m

<!-- b000210 | furniture | pages [3] -->
m

<!-- b000211 | furniture | pages [3] -->
m

<!-- b000212 | furniture | pages [3] -->
m

<!-- b000213 | furniture | pages [3] -->
m

<!-- b000214 | furniture | pages [3] -->
m

<!-- b000215 | furniture | pages [3] -->
m

<!-- b000216 | furniture | pages [3] -->
m

<!-- b000217 | furniture | pages [3] -->
m

<!-- b000218 | furniture | pages [3] -->
m

<!-- b000219 | furniture | pages [3] -->
m

<!-- b000220 | furniture | pages [3] -->
m

<!-- b000221 | furniture | pages [3] -->
m

<!-- b000222 | furniture | pages [3] -->
m

<!-- b000223 | furniture | pages [3] -->
m

<!-- b000224 | furniture | pages [3] -->
m

<!-- b000225 | furniture | pages [3] -->
m

<!-- b000226 | furniture | pages [3] -->
m

<!-- b000227 | furniture | pages [3] -->
m

<!-- b000228 | furniture | pages [3] -->
m

<!-- b000229 | furniture | pages [3] -->
m

<!-- b000230 | furniture | pages [3] -->
m

<!-- b000231 | furniture | pages [3] -->
m

<!-- b000232 | furniture | pages [3] -->
m

<!-- b000233 | furniture | pages [3] -->
m

<!-- b000234 | furniture | pages [3] -->
m

<!-- b000235 | furniture | pages [3] -->
m

<!-- b000236 | furniture | pages [3] -->
m

<!-- b000237 | furniture | pages [3] -->
m

<!-- b000238 | furniture | pages [3] -->
m

<!-- b000239 | furniture | pages [3] -->
m

<!-- b000240 | furniture | pages [3] -->
m

<!-- b000241 | furniture | pages [3] -->
m

<!-- b000242 | furniture | pages [3] -->
m

<!-- b000243 | furniture | pages [3] -->
m

<!-- b000244 | furniture | pages [3] -->
m

<!-- b000245 | furniture | pages [3] -->
m

<!-- b000246 | furniture | pages [3] -->
m

<!-- b000247 | furniture | pages [3] -->
m

<!-- b000248 | furniture | pages [3] -->
m

<!-- b000249 | furniture | pages [3] -->
m

<!-- b000250 | furniture | pages [3] -->
m

<!-- b000251 | furniture | pages [3] -->
m

<!-- b000252 | furniture | pages [3] -->
m

<!-- b000253 | furniture | pages [3] -->
m

<!-- b000254 | furniture | pages [3] -->
m

<!-- b000255 | furniture | pages [3] -->
m

<!-- b000256 | furniture | pages [3] -->
m

<!-- b000257 | furniture | pages [3] -->
m

<!-- b000258 | furniture | pages [3] -->
m

<!-- b000259 | furniture | pages [3] -->
m

<!-- b000260 | furniture | pages [3] -->
m

<!-- b000261 | furniture | pages [3] -->
m

<!-- b000262 | furniture | pages [3] -->
m

<!-- b000263 | furniture | pages [3] -->
m

<!-- b000264 | furniture | pages [3] -->
m

<!-- b000265 | furniture | pages [3] -->
m

<!-- b000266 | furniture | pages [3] -->
m

<!-- b000267 | furniture | pages [3] -->
m

<!-- b000268 | furniture | pages [3] -->
m

<!-- b000269 | furniture | pages [3] -->
m

<!-- b000270 | furniture | pages [3] -->
m

<!-- b000271 | furniture | pages [3] -->
m

<!-- b000272 | furniture | pages [3] -->
m

<!-- b000273 | furniture | pages [3] -->
m

<!-- b000274 | furniture | pages [3] -->
m

<!-- b000275 | furniture | pages [3] -->
m

<!-- b000276 | furniture | pages [3] -->
m

<!-- b000277 | furniture | pages [3] -->
m

<!-- b000278 | furniture | pages [3] -->
m

<!-- b000279 | furniture | pages [3] -->
m

<!-- b000280 | furniture | pages [3] -->
m

<!-- b000281 | furniture | pages [3] -->
m

<!-- b000282 | furniture | pages [3] -->
m

<!-- b000283 | furniture | pages [3] -->
m

<!-- b000284 | furniture | pages [3] -->
m

<!-- b000285 | furniture | pages [3] -->
m

<!-- b000286 | furniture | pages [3] -->
m

<!-- b000287 | furniture | pages [3] -->
m

<!-- b000288 | furniture | pages [3] -->
m

<!-- b000289 | furniture | pages [3] -->
m

<!-- b000290 | furniture | pages [3] -->
m

<!-- b000291 | furniture | pages [3] -->
m

<!-- b000292 | furniture | pages [3] -->
m

<!-- b000293 | furniture | pages [3] -->
m

<!-- b000294 | furniture | pages [3] -->
m

<!-- b000295 | furniture | pages [3] -->
m

<!-- b000296 | furniture | pages [3] -->
m

<!-- b000297 | furniture | pages [3] -->
m

<!-- b000298 | furniture | pages [3] -->
m

<!-- b000299 | furniture | pages [3] -->
m

<!-- b000300 | furniture | pages [3] -->
m

<!-- b000301 | furniture | pages [3] -->
m

<!-- b000302 | furniture | pages [3] -->
m

<!-- b000303 | furniture | pages [3] -->
m

<!-- b000304 | furniture | pages [3] -->
m

<!-- b000305 | furniture | pages [3] -->
m

<!-- b000306 | furniture | pages [3] -->
m

<!-- b000307 | furniture | pages [3] -->
m

<!-- b000308 | furniture | pages [3] -->
m

<!-- b000309 | furniture | pages [3] -->
m

<!-- b000310 | furniture | pages [3] -->
m

<!-- b000311 | furniture | pages [3] -->
m

<!-- b000312 | furniture | pages [3] -->
m

<!-- b000313 | furniture | pages [3] -->
m

<!-- b000314 | furniture | pages [3] -->
m

<!-- b000315 | furniture | pages [3] -->
m

<!-- b000316 | furniture | pages [3] -->
m

<!-- b000317 | furniture | pages [3] -->
m

<!-- b000318 | furniture | pages [3] -->
m

<!-- b000319 | furniture | pages [3] -->
m

<!-- b000320 | furniture | pages [3] -->
m

<!-- b000321 | furniture | pages [3] -->
m

<!-- b000322 | furniture | pages [3] -->
m

<!-- b000323 | furniture | pages [3] -->
m

<!-- b000324 | furniture | pages [3] -->
m

<!-- b000325 | furniture | pages [3] -->
m

<!-- b000326 | furniture | pages [3] -->
m

<!-- b000327 | furniture | pages [3] -->
m

<!-- b000328 | furniture | pages [3] -->
m

<!-- b000329 | furniture | pages [3] -->
m

<!-- b000330 | furniture | pages [3] -->
m

<!-- b000331 | furniture | pages [3] -->
m

<!-- b000332 | furniture | pages [3] -->
m

<!-- b000333 | furniture | pages [3] -->
m

<!-- b000334 | furniture | pages [3] -->
m

<!-- b000335 | furniture | pages [3] -->
m

<!-- b000336 | furniture | pages [3] -->
m

<!-- b000337 | furniture | pages [3] -->
m

<!-- b000338 | furniture | pages [3] -->
m

<!-- b000339 | furniture | pages [3] -->
m

<!-- b000340 | furniture | pages [3] -->
m

<!-- b000341 | furniture | pages [3] -->
m

<!-- b000342 | furniture | pages [3] -->
m

<!-- b000343 | furniture | pages [3] -->
m

<!-- b000344 | furniture | pages [3] -->
m

<!-- b000345 | furniture | pages [3] -->
m

<!-- b000346 | furniture | pages [3] -->
m

<!-- b000347 | furniture | pages [3] -->
m

<!-- b000348 | furniture | pages [3] -->
m

<!-- b000349 | furniture | pages [3] -->
m

<!-- b000350 | furniture | pages [3] -->
m

<!-- b000351 | furniture | pages [3] -->
m

<!-- b000352 | furniture | pages [3] -->
m

<!-- b000353 | furniture | pages [3] -->
m

<!-- b000354 | furniture | pages [3] -->
m

<!-- b000355 | furniture | pages [3] -->
m

<!-- b000356 | furniture | pages [3] -->
m

<!-- b000357 | furniture | pages [3] -->
m

<!-- b000358 | furniture | pages [3] -->
m

<!-- b000359 | furniture | pages [3] -->
m

<!-- b000360 | furniture | pages [3] -->
m

<!-- b000361 | furniture | pages [3] -->
m

<!-- b000362 | furniture | pages [3] -->
m

<!-- b000363 | furniture | pages [3] -->
m

<!-- b000364 | furniture | pages [3] -->
m

<!-- b000365 | furniture | pages [3] -->
m

<!-- b000366 | furniture | pages [3] -->
m

<!-- b000367 | furniture | pages [3] -->
m

<!-- b000368 | furniture | pages [3] -->
m

<!-- b000369 | furniture | pages [3] -->
m

<!-- b000370 | furniture | pages [3] -->
m

<!-- b000371 | furniture | pages [3] -->
m

<!-- b000372 | furniture | pages [3] -->
m

<!-- b000373 | furniture | pages [3] -->
m

<!-- b000374 | furniture | pages [3] -->
m

<!-- b000375 | furniture | pages [3] -->
m

<!-- b000376 | furniture | pages [3] -->
m

<!-- b000377 | furniture | pages [3] -->
m

<!-- b000378 | furniture | pages [3] -->
m

<!-- b000379 | furniture | pages [3] -->
m

<!-- b000380 | furniture | pages [3] -->
m

<!-- b000381 | furniture | pages [3] -->
m

<!-- b000382 | furniture | pages [3] -->
m

<!-- b000383 | furniture | pages [3] -->
m

<!-- b000384 | furniture | pages [3] -->
m

<!-- b000385 | furniture | pages [3] -->
m

<!-- b000386 | furniture | pages [3] -->
m

<!-- b000387 | furniture | pages [3] -->
m

<!-- b000388 | furniture | pages [3] -->
m

<!-- b000389 | furniture | pages [3] -->
m

<!-- b000390 | furniture | pages [3] -->
m

<!-- b000391 | furniture | pages [3] -->
m

<!-- b000392 | furniture | pages [3] -->
m

<!-- b000393 | furniture | pages [3] -->
m

<!-- b000394 | furniture | pages [3] -->
m

<!-- b000395 | furniture | pages [3] -->
m

<!-- b000396 | furniture | pages [3] -->
m

<!-- b000397 | furniture | pages [3] -->
m

<!-- b000398 | furniture | pages [3] -->
m

<!-- b000399 | furniture | pages [3] -->
m

<!-- b000400 | furniture | pages [4] -->
Team#2507817                                                             Page 4 of 25

<!-- b000402 | prose | pages [4] -->
 First identify the countries and programs that have been impacted, and then calculate the regression equation between the variables that include the impact of great coaches and the final predicted values. Then identify countries and programs with potential to predict changes in their performance Task 5 Given original insights on Olympic medal counts, analyze the information these insights can provide to the NOC.

<!-- b000403 | prose | pages [4] -->
 Find the eigenvalues from the previous Tasks that have some influence on the number of gold medals & medals, and investigate them

<!-- b000404 | heading | pages [4] -->
1.3 Our work

<!-- b000405 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000406 | caption | pages [4] -->
Figure 2 Our Work

<!-- b000407 | prose | pages [4] -->
关注数学模型

<!-- b000408 | furniture | pages [4] -->
2

<!-- b000409 | furniture | pages [4] -->
MATHmodels

<!-- b000410 | furniture | pages [4] -->
获取更多资讯

<!-- b000411 | furniture | pages [5] -->
Team#2507817                                                             Page 5 of 25

<!-- b000412 | heading | pages [5] -->
2 Basic Assumption

<!-- b000413 | prose | pages [5] -->
 Hypothesis 1: Assume that the number of athletes participating in the 2028 Olympics, the number of countries, and the number of events held are the same as in 2024.

<!-- b000414 | prose | pages [5] -->
Legitimacy: The data review revealed that the number of countries participating in recent Olympic Games and the number of events held have not changed much. To simplify the calculation of the model, it is assumed that the number remains constant.

<!-- b000415 | prose | pages [5] -->
 Hypothesis 2: The variables are independent of each other and only affect the results.

<!-- b000416 | heading | pages [5] -->
Justification: while these variables interact, considering them in the model adds

<!-- b000417 | prose | pages [5] -->
complexity and unpredictability. For extensive analysis, we focus more on measurable and 微信公众号：数学模型 consistent factors

<!-- b000418 | heading | pages [5] -->
 Assumption 3: Excluding the cost of investing in great coaches

<!-- b000419 | prose | pages [5] -->
Justification: focuses on the direct impact of coaching quality on athlete performance, team performance, or overall sport system development.

<!-- b000420 | heading | pages [5] -->
3 Symbols

<!-- b000421 | prose | pages [5] -->
Symbols Definition

<!-- b000422 | prose | pages [5] -->
A Total number of athletes from the i-th country in the j-th Olympic Games ij 微信号：MATHmodels The number of gold medals won by the i-th country before the j-th Olympic G ij Games The total number of medals won by the i-th country before the j-th Olympic T ij Games

<!-- b000423 | prose | pages [5] -->
E Total number of events in the j Olympic Games ij

<!-- b000424 | prose | pages [5] -->
Y Number of gold medals predicted g

<!-- b000425 | prose | pages [5] -->
tY Total number of medals predicted

<!-- b000426 | prose | pages [5] -->
ka Number of athletes in the kth country

<!-- b000427 | prose | pages [5] -->
ke Number of projects participated by the kth country

<!-- b000428 | prose | pages [5] -->
kp Number of historical entries of the kth country

<!-- b000429 | heading | pages [5] -->
4  Data Preprocessing

<!-- b000430 | prose | pages [5] -->
 Outlier handling: each country may have different teams for the same program, and the names of these teams contain markers representing the order of the teams, and there is garbled code after the name of the country. We dealt with cleaning these outliers.  Data standardization: In forecasting, to ensure that the data have relatively equal weights for each feature value, data standardization is used, where the mean ( x ) and standard deviation (SD) of each feature are to be calculated

<!-- b000431 | prose | pages [5, 6] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m  ( x x )  ' x (0) SD  Conversion of country and region names: To build the model, we utilized two files:

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

<!-- b000756 | furniture | pages [6] -->
Team#2507817                                                             Page 6 of 25

<!-- b000758 | prose | pages [6] -->
"summerOly_medal_counts.csv" and "summerOly_athletes.csv." Since these files represent countries in different formats, we employed an ISO mapping table to convert the full names of all countries and regions into standardized codes prior to data integration.

<!-- b000759 | prose | pages [6] -->
Data for countries that were dissolved or banned, such as the USSR and Russia, was excluded.  Athlete & Event Counts: Athletes and events are categorized by country and year and their total value is calculated. Individual Neutral Athletes (AIN) sport results do not represent any one country and should also be cleared in the forecast.

<!-- b000760 | heading | pages [6] -->
5 Task 1 Predicting Gold & Total Medals Based on GSRF Model

<!-- b000761 | heading | pages [6] -->
5.1 GSRF Prediction Model

<!-- b000762 | heading | pages [6] -->
5.1.1 ARIMA Model Initial Prediction

<!-- b000763 | prose | pages [6] -->
The ARIMA model is widely used in time series analysis for its flexibility and powerful forecasting ability to adapt to a wide range of data characteristics and make accurate predictions.The ARIMA model integrates autoregressive (AR) and moving average (MA) methods and incorporates differencing (I) to enhance data smoothing. By examining autocorrelation in historical data, the model assumes that future trends will mimic historical patterns and thus predicts future data points.ARIMA (p, d, q) can be expressed as equation (2):

<!-- b000764 | prose | pages [6] -->
                   (1) X c X X X       t 1 t 1 2 t 2 p t p 1 t 1 2 t 2 q t q t

<!-- b000765 | prose | pages [6] -->
Among them:

<!-- b000766 | prose | pages [6] -->
X represents the time series data we are considering;  t

<!-- b000767 | prose | pages [6] -->
c is a constant term; 

<!-- b000768 | prose | pages [6] -->
 are the parameters of the AR model, which are used to describe the relationship m m m m m m m m m m m m m m m m m m m m m m , ,..., m m m m m m m m m m m m m m m m  m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1 2 p m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m between the current value and the value at the past p time points; m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m  m m m m m m m m m m m m m m m   m m m m m m m m m m m m m m m m are the parameters of the MA model that are used to describe the relationship , , m m m m m m m m m  m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1 2 q m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000769 | prose | pages [6] -->
between the current value and the error at the past q time points;

<!-- b000770 | prose | pages [6] -->
tis the error term at time point t. 

<!-- b000771 | prose | pages [6] -->
Our initial ARIMA projections of the number of gold medals and the total number of medals for the United States and China resulted in the projection charts shown below:

<!-- b000772 | prose | pages [6, 7] -->
关注数学模型 微信公众号：数学模型 b)  United States Total Predict a) United States Gold

<!-- b000773 | furniture | pages [6] -->
2

<!-- b000774 | furniture | pages [6] -->
MATHmodels

<!-- b000775 | furniture | pages [6] -->
获取更多资讯

<!-- b000776 | furniture | pages [7] -->
Team#2507817                                                             Page 7 of 25

<!-- b000778 | prose | pages [7] -->
微信号：MATHmodels c) China Gold Predict d)  China Total Predict

<!-- b000779 | caption | pages [7] -->
Figure 3 Prediction chart of medal numbers for the United States and China

<!-- b000780 | prose | pages [7] -->
The ARIMA (p, d, q) model corresponding to the above predictions and the correlation 2 coefficients R are shown in the table below:

<!-- b000781 | caption | pages [7] -->
Table 1 Relevant data for predictive models

<!-- b000782 | prose | pages [7] -->
ARIMA (p, d, q) 2 R United States Gold Predict ARIMA (2, 0, 2) 0.218 United States Total Predict ARIMA (2, 1, 1) 0.257 China Gold Predict ARIMA (1, 1, 0) 0.430 China Total Predict ARIMA (1, 1, 0) 0.494

<!-- b000783 | prose | pages [7] -->
The correlation coefficients derived from the prediction are small not close to 1, proving that the use of ARIMA model to predict the number of medals is not ideal, so we use the GSRF swing prediction model to make predictions

<!-- b000784 | heading | pages [7] -->
5.1.2 GSRF Prediction Modeling

<!-- b000785 | prose | pages [7] -->
First, we need to build a model for predicting the fluctuations in the number of medals for each country, as well as finding the factors that are most relevant to this fluctuation. From this we use the GSRF swing prediction model.

<!-- b000786 | prose | pages [7] -->
In order to predict the number of medals the country will win in the next Olympics, we start with the previous years' awards of the participating athletes and use the network search random forest algorithm to predict the number of gold medals won in the future and the total number of medals, respectively.

<!-- b000787 | prose | pages [7] -->
Next, we describe the selected metrics data and explain the algorithmic process.

<!-- b000788 | heading | pages [7] -->
1) Selected indicators

<!-- b000789 | furniture | pages [8] -->
Team#2507817                                                             Page 8 of 25

<!-- b000790 | prose | pages [8] -->
Using the dataset from previous years, we selected four characteristic input indicators:  Total number of athletes from this country in the current Olympics: more athletes means more opportunities to compete and a wider range of selections, increasing the likelihood of winning medals. We denote the total number of athletes from country i in the jth Olympics as: Aij  The number of gold medals and total medals won by the country up to the current Olympics: The medal table of previous years gives a preliminary idea of the strength of the country and the trend of its strength. We denote the total number of gold medals won by country i before the jth Olympics as Gij and the total number of medals as T(ij).  Current total number of Olympic events: The total number of Olympic events determines the basis of medal distribution, the more events the more medals. The more programs a country participates in, the more chances it has to win. An increase in the number of events results in a wider distribution of medals, with more countries having a chance to win. We denote the total number of events in the jth Olympics as Ej  Is the country hosting the Games: As a host, the country has advantages in terms of venues, facilities and logistics. The host can increase the number of events it specializes in, decrease the number of events it does not specialize in, and automatically get more places, increasing the chances of athletes to participate. If it is the host of the jth Olympic Games, let Hij = 1, and vice versa, let Hij = 0.

<!-- b000791 | heading | pages [8] -->
2) GSRF Algorithm

<!-- b000792 | prose | pages [8] -->
The GSRF algorithm optimizes the random forest model using a grid search algorithm.

<!-- b000793 | prose | pages [8] -->
Random forests are machine learning algorithms trained using multiple decision trees, with a randomly selected subset of features per tree, and voting to integrate the results when classifying. To prevent overfitting or underfitting, grid search optimization is used. The grid search algorithm traverses a grid of predefined parameters, trains and evaluates each combination, and outputs the best set of parameters and model performance.

<!-- b000794 | prose | pages [8] -->
Compared with the standard random forest algorithm, the GSRF algorithm uses an optimal combination of hyperparameters to train and predict the model. This improvement significantly improves the performance of the model and effectively mitigates problems such as overfitting or underfitting. The following figure illustrates the workflow of the GSRF algorithm.

<!-- b000795 | caption | pages [8] -->
Figure 4 GSRF Algorithm Flow Diagram

<!-- b000796 | heading | pages [8] -->
3) Make Predictions on Gold & Total Medals

<!-- b000797 | prose | pages [8] -->
According to the literature, it is known that a series of data such as the number of strengths of athletes, the number of types of events and so on have an impact on the number of medals in the next Olympic Games. Therefore, we use the above four characteristic input indicators as

<!-- b000798 | prose | pages [8, 9] -->
关注数学模型 the input parameters of the random forest model to predict the number of medals:

<!-- b000799 | furniture | pages [8] -->
2

<!-- b000800 | furniture | pages [8] -->
MATHmodels

<!-- b000801 | furniture | pages [8] -->
获取更多资讯

<!-- b000802 | furniture | pages [9] -->
Team#2507817                                                             Page 9 of 25

<!-- b000804 | prose | pages [9] -->
 GSRF ( A , G , E , H ) Y ij g , ij j g , ij g , g (2)  GSRF ( A , T E , , H ) Y ij t , ij j t , ij t , t

<!-- b000805 | prose | pages [9] -->
Among them.

<!-- b000806 | prose | pages [9] -->
A , E , H represent the total number of athletes from the country in the gold medal ij g , j g , ij g , prediction model, the total number of Olympic events, and whether this country is the host of this Olympics, respectively. Y Represents the number of gold medals predicted. g

<!-- b000807 | prose | pages [9] -->
Represent the total number of athletes from the country in the total medal A , E , H ij t , j t , ij t , count prediction model, the total number of Olympic events, and whether this country is the 微信公众号：数学模型 host of this Olympics, respectively. tY Represents the number of gold medals predicted.

<!-- b000808 | prose | pages [9] -->
We use data prior to 2024 as the training set and 2024 as the test set. The k-fold cross- validation method is used, taking k to be 10. The training set is divided equally into 10 equal sized subsets. For each subset, that subset is used as the validation set and the rest use the remaining 9 subsets as the training set. The random forest model is trained on the training set and the model performance is evaluated on the validation set and the evaluation metrics are recorded. Finally, the average evaluation metrics of all the subsets are calculated, giving a comprehensive estimate of the model performance, as a way to assess the stability and generalization ability of the model. The schematic diagram is shown below:

<!-- b000809 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000810 | caption | pages [9] -->
Figure 5 10 Fold Cross Validation Diagram

<!-- b000811 | prose | pages [9] -->
The Random Forest Regressor algorithm from the integration module in the scikit-learn (sklearn) machine learning library[1] and the GridSearchCV algorithm from sklearn were used via . The optimal parameter combination obtained by GridSearchCV is as follows:

<!-- b000812 | caption | pages [9] -->
Table 2 The impact of various indicators on the prediction results

<!-- b000813 | prose | pages [9] -->
Gold Medals Total Medal

<!-- b000814 | prose | pages [9] -->
G T A E H A E H ij g , ij ,j g ij g , ij t , ij ,j t ij t ,

<!-- b000815 | prose | pages [9] -->
74.10% 1.71% 7.40% 16.90% 85.70% 7.20% 6.30% 0.80%

<!-- b000816 | prose | pages [9] -->
We use radar charts to visualize the impact of each indicator on the forecast results as follows:

<!-- b000817 | furniture | pages [10] -->
Page 10 of 25

<!-- b000818 | furniture | pages [10] -->
Team#2507817

<!-- b000819 | prose | pages [10] -->
Athletes_num(4) Athletes_num(4) 1.01 —Importance of Features 1.01 —Importance of Features 0.8

<!-- b000820 | prose | pages [10] -->
0.0 History History Host Host 0.2 (τv) (H) (II) (G)

<!-- b000821 | prose | pages [10] -->
Total events(E,) Total events (Ej) a) Prediction of Gold b) Prediction of Total Medal Count

<!-- b000822 | caption | pages [10] -->
Figure 6 Feature Importance Radar Chart

<!-- b000823 | prose | pages [10] -->
The graph shows that the number of athletes has the greatest impact on gold and total medal predictions. Host status has a significant impact on gold medal predictions and a small impact on total medal predictions. The total number of Olympic events has some impact on the number of medals, but not significant.

<!-- b000824 | prose | pages [10] -->
The comparison between the predicted and actual values for some of the test sets is obtained as shown below:

<!-- b000825 | prose | pages [10] -->
Predicted Predicted TRUE 140 4 403530 2520151050 120 100 80 60 40 20 0 New Zealand Cuba United States Great Britain Austratia Netheriands Sweden Hungary Greece Germany Korean Brazil Romania New Zealand Greece United States Great Britain Netherlands Korean France Australia Germany Hungary Sweden Canada

<!-- b000826 | prose | pages [10] -->
(a) Prediction of Gold b) Prediction of Total Medal Count

<!-- b000827 | caption | pages [10] -->
Figure 7 Comparison Chart of Actual and Predicted Values for Some Countries in 2024

<!-- b000828 | heading | pages [10] -->
5.1.3 Model Prediction Effectiveness and Performance Evaluation

<!-- b000829 | prose | pages [10] -->
We trained the random forest model using the first 80% of the data and tested it using the second 20% of the data. Based on the predicted and true values, the coefficient of determination (R²), Mean Absolute Error (MAE), Root Mean Square Error (RMSE) of this model are calculated as follows:

<!-- b000830 | heading | pages [10] -->
Correlation coefficient R2: comparing the predictions obtained using the model with the

<!-- b000831 | prose | pages [10] -->
predictions using only the mean, the closer R² is to 1 the more accurate the model is.

<!-- b000832 | prose | pages [10] -->
∑(Y -Y)2 R2 =1− (3) -3 Mean Absolute Error MAE: The average value of the absolute error, which can reflect the actual situation of the prediction value error. The smaller the value, the higher the accuracy of the model.

<!-- b000833 | prose | pages [10] -->
MAE =⊥∑|Y- (4) n=1 Root Mean Square Error RMSE: the square root of the MSE, the smaller the RMSE, the more accurate the model is

<!-- b000834 | prose | pages [10, 11] -->
关注数学模型 ∑( − Y)2 (5) RMSE = n曰1 The model evaluation results obtained from the calculations are as follows:

<!-- b000835 | furniture | pages [10] -->
获取更多资讯

<!-- b000836 | furniture | pages [11] -->
Page 11 of 25

<!-- b000837 | furniture | pages [11] -->
Team#2507817

<!-- b000839 | caption | pages [11] -->
Table 3 Evaluation Results of Gold Medal Prediction Model

<!-- b000840 | prose | pages [11] -->
R2 MAE RMSE 1.829 0.903 0.626 Training set 0.710 0.994 3.145 Cross validation set 0.795 0.914 2.574 Test set

<!-- b000841 | caption | pages [11] -->
Table 4 Evaluation Results of the Prediction Model for the Total Number of Medals

<!-- b000842 | prose | pages [11] -->
R2 MAE RMSE Training set 0.933 1.947 4.11 7.162 0.784 2.744 Cross validation set 0.736 7.145 2.430 Test set The R² of both prediction models is very close to 1, and the MAE and RMSE are small. This indicates that the accuracy of the prediction models we constructed is higher and the model performance is better.

<!-- b000843 | heading | pages [11] -->
5.2 Predicting the 2028 Gold & Medal Tables

<!-- b000844 | prose | pages [11] -->
5.2.1 Predicting the 2028 Gold & Medal Tables Based on the GSRF prediction model we established in the previous section, this paper predicts the medal table of the 2028 Summer Olympics in Los Angeles, U.S.A. We predict the top ten gold medals won and the top ten total medals won at the 2028 Los Angeles Olympics corresponding to the countries and the number of countries in the following table.

<!-- b000845 | prose | pages [11] -->
Table 5Top 10 Predicted Gold Medals for the 2028 Olympic Games Country USA CHN GBR GBR JPN CAN FRA GER ITA AUS 51 29 15 34 28 26 26 19 15 old medals 20 Table 6Top 10 Predicted Medals for the 2028 Olympic Games Country USA CHN GBR AUS CAN BRA FRA ITA NED GER JPN 8174 124 72 65 61 55 52 35 34 34 Total medals

<!-- b000846 | prose | pages [11] -->
We visualized the results using plotting software as shown below:

<!-- b000847 | prose | pages [11] -->
United States China

<!-- b000848 | prose | pages [11] -->
Canada Japan

<!-- b000849 | prose | pages [11] -->
20 100 120 140 40 60

<!-- b000850 | caption | pages [11] -->
Figure 8 Predicted Gold&Total Medals Table for 2028 Los Angeles Olympics

<!-- b000851 | prose | pages [11] -->
USA tops the table in both gold and total medals, France is second in total medals but not many gold medals, China is second in gold medals and third in total medals. Predicting the 2028 gold medal table, Canada is on the list and South Korea is out, the rest of the countries have changed their rankings.

<!-- b000852 | furniture | pages [12] -->
Team#2507817                                                             Page 12 of 25

<!-- b000853 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The above predictions are only the most likely scenarios, next we solve for the prediction m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m intervals at the 95% confidence level: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000854 | heading | pages [12] -->
5.2.2 Calculate the prediction interval

<!-- b000855 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m First, we determine whether the residuals of the two prediction models satisfy a normal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m distribution:

<!-- b000856 | prose | pages [12] -->
We plotted and fitted a histogram of residuals and also performed a Shapiro-Wilk test on the data, the results of which are shown below:

<!-- b000857 | prose | pages [12] -->
a) Prediction of Gold Medals b) Prediction of Total Medal Count

<!-- b000858 | caption | pages [12] -->
Figure 9 histogram of residuals

<!-- b000859 | caption | pages [12] -->
Table 7 Fitting data and SW test results

<!-- b000860 | prose | pages [12] -->
Standard Deviation Skewness Kurtosis Shapiro-Wilk Test Gold Medals 2.908 4.723 35.429 0.438 Total Medals 7.123 -4.644 40.523 0.434

<!-- b000861 | prose | pages [12] -->
Based on the above graphs, it can be found that both predictive models have large peaks and skewness, and the significance of the Shapiro-Wilk test on the data is P<0.05, which indicates that both predictive models do not conform to a normal distribution.

<!-- b000862 | prose | pages [12] -->
So we compute the prediction interval using the t distribution     Prediction Interval= y t SE y (6)   2, n p

<!-- b000863 | prose | pages [12] -->
Among them.

<!-- b000864 | prose | pages [12] -->
y represents the predicted value, t  is the quantile of the t-distribution, n is the 2,n p  number of samples, p is the number of parameters in the model, and SE y is the standard

<!-- b000865 | prose | pages [12] -->
error of the prediction. The correlation results were calculated as shown below:

<!-- b000866 | caption | pages [12] -->
Table 8 Prediction Model T-Distribution Related Data

<!-- b000867 | prose | pages [12] -->
 t SE y  2,n p Prediction of Gold Medals 2.404 2.908 Prediction of Total Medal Count 1.993 7.123

<!-- b000868 | prose | pages [12] -->
Then the prediction interval for the number of gold medals at the 95% confidence level is  and the total prediction interval for the number of medals is  y  y  7 15

<!-- b000869 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型 (a) Prediction of Gold Medals b)  Prediction of Total Medal Count

<!-- b000870 | furniture | pages [12] -->
2

<!-- b000871 | furniture | pages [12] -->
MATHmodels

<!-- b000872 | furniture | pages [12] -->
获取更多资讯

<!-- b000873 | furniture | pages [13] -->
Team#2507817                                                             Page 13 of 25

<!-- b000875 | caption | pages [13] -->
Figure 10 Error bar chart of prediction model

<!-- b000876 | heading | pages [13] -->
5.2.3 Predicting progress and regressions in national performance

<!-- b000877 | prose | pages [13] -->
The question asked us to predict the countries most likely to advance or retreat, we 微信号：MATHmodels calculated the predicted number of gold medals & total medals and the difference between the awards in 2024 to find the change in value, and plotted a histogram as shown below:

<!-- b000878 | prose | pages [13] -->
a) Gold medal, with fluctuations exceeding 2 b) Total medal, with fluctuations exceeding 5

<!-- b000879 | caption | pages [13] -->
Figure 11 Countries with significant fluctuations in medal numbers

<!-- b000880 | prose | pages [13] -->
The graphic shows that Great Britain had the most significant increase in gold medals and Germany had the most significant increase in total medals, both making significant progress. South Korea had the largest decrease in gold medals and China had the largest decrease in total medals. With the exception of the United States, the countries with significant gold medal growth also saw varying degrees of progress in total medals. The U.S. had more gold medal growth, but less significant total medal growth.

<!-- b000881 | heading | pages [13] -->
6 Task 2 Projections for Non-Awarded Countries

<!-- b000882 | prose | pages [13] -->
The question asks us to predict whether or not a country that has never won a medal will win its first medal at the 2028 Summer Olympics and to predict the probability of winning. The question is essentially a binary classification problem. The predicted outcomes are categorized into those that will win and those that will not. Therefore, we build a binary logistic regression model.

<!-- b000883 | heading | pages [13] -->
6.1 Bicategory Logistic Regression Modeling

<!-- b000884 | prose | pages [13] -->
We recorded non-winning countries as Category 1 if they could win at the 2028 Summer Olympics and Category 0 if they could not.

<!-- b000885 | heading | pages [13] -->
6.1.1 Sigmoid Function (math.)

<!-- b000886 | prose | pages [13] -->
Logistic regression is a generalized linear regression that combines a nonlinear function with a linear function to map it. We use the Sigmoid function to map the output value of a linear function to a probability between 0 and 1. The Sigmoid function formula is as follows:

<!-- b000887 | furniture | pages [14] -->
Team#2507817                                                             Page 14 of 25

<!-- b000888 | prose | pages [14] -->
1   ( ) z (7)  z 1 e Among them:

<!-- b000889 | prose | pages [14] -->
       z a e p b (8) 1 k 2 k 3 k

<!-- b000890 | prose | pages [14] -->
 a e , , p is the input eigenvalue k k k

<!-- b000891 | prose | pages [14] -->
ka : The number of athletes from the kth country in the 2028 Olympics. More athletes means that more people can compete in more events, or more people can compete in the same event, which greatly increases the probability of winning.

<!-- b000892 | prose | pages [14] -->
ke : The number of events in which the kth country participates in the 2028 Olympics.

<!-- b000893 | prose | pages [14] -->
Participating in more events increases the probability of winning to some extent compared m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to concentrating on the same event. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m kp : Historical participation of the kth country: the more a country participates in international m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m events, the more experience it accumulates, which can largely increase its probability of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m winning. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000894 | prose | pages [14] -->
    , , , are the weights and we calculate their values using gradient descent. 1 2 n

<!-- b000895 | prose | pages [14] -->
 b is the bias term When the output of the sigmoid function is close to 1, the probability that the country belongs to category 1 is considered higher, i.e. the probability of winning the prize is higher. When the output value is close to 0, the probability that the country belongs to category 0 is higher, i.e. the probability of not winning the prize is higher.

<!-- b000896 | heading | pages [14] -->
6.1.2 Introducing the Loss Function

<!-- b000897 | prose | pages [14] -->
1            Let , we get P z 0 | x 1 P z 1| x 1 p , then p ( ) z i i  z 1 e     y 1 y P y x | , ) ( p ) (1 p ) (9) （ i i

<!-- b000898 | prose | pages [14] -->
To further optimize the model, we introduce a cross-entropy loss function (log loss) to measure the gap between the model's predicted probability and the true category, log loss is defined as follows:

<!-- b000899 | prose | pages [14] -->
m             (10) L z ln p 1 z ln 1 p   i i i i  i 1

<!-- b000900 | prose | pages [14] -->
where iz is the true category; ip is the predicted probability of the model; and m is the sample size.

<!-- b000901 | heading | pages [14] -->
6.2 Bicategory Logistic Regression Results

<!-- b000902 | prose | pages [14] -->
The results of the parameters of the model were calculated using MATLAB as shown in the table below:

<!-- b000903 | prose | pages [14, 15] -->
关注数学模型 Regression Coefficient Standard Error Waid P b 2.425 0.098 607.134 <0.01 ka -0.012 0.004 10.62 <0.01 ke -0.068 0.008 76.036 <0.01 kp -0.013 0.010 1.665 0.197

<!-- b000904 | furniture | pages [14] -->
2

<!-- b000905 | furniture | pages [14] -->
MATHmodels

<!-- b000906 | furniture | pages [14] -->
获取更多资讯

<!-- b000907 | furniture | pages [15] -->
Team#2507817                                                             Page 15 of 25

<!-- b000908 | caption | pages [15] -->
Table 9 Parameter results of Binary Logistic Regression Model

<!-- b000910 | prose | pages [15] -->
As can be seen from the table, kp corresponds to P>0.05, which indicates that kp has no effect on the predicted results. We stipulate that a dependent variable of 1 represents that the non-winning country can win at the 2028 Summer Olympics. A dependent variable of 0 represents not being able to win a prize. The regression equation for whether or not the non- winning country wins the 2028 Olympics is derived:

<!-- b000911 | prose | pages [15] -->
   微信公众号：数学模型 z 0.012 a 0.068 e 2.425 (11) k k

<!-- b000912 | heading | pages [15] -->
6.2.1 Model Evaluation and Modification

<!-- b000913 | prose | pages [15] -->
In order to evaluate the classification effectiveness of the model, we start with the sensitivity and specificity of the model:

<!-- b000914 | prose | pages [15] -->
 Sensitivity (TPR): the proportion of results that are actually positive samples that are predicted to be positive samples.

<!-- b000915 | prose | pages [15] -->
 Specificity (FPR): the proportion of results that are actually negative samples that are predicted to be positive samples.

<!-- b000916 | prose | pages [15] -->
 AUC: is the area under the ROC curve and is used to measure the overall performance 微信号：MATHmodels of the binary classification model.

<!-- b000917 | prose | pages [15] -->
The ROC curve of the model is plotted as shown below:

<!-- b000918 | caption | pages [15] -->
Figure 12 ROC curve

<!-- b000919 | caption | pages [15] -->
Figure 13 Hybrid Matrix Thermodynamic Diagram

<!-- b000920 | prose | pages [15] -->
The ROC plot combines sensitivity (TPR) and specificity (FPR), which can measure the relationship simultaneously. Ideally, TPR should be close to 1, FPR should be close to 0, and the AUC value should be close to 1. Calculation from the ROC graph shows that AUC = 0.918. It can be seen that the sensitivity of this model is good.

<!-- b000921 | prose | pages [15, 16] -->
To further measure the classification effectiveness of logistic regression through quantitative metrics, a heat map of the confusion matrix was drawn as shown above. Based on this, the classification evaluation metrics of the model are calculated as shown in the table below Accuracy Recall Precision F1 0.841 0.841 0.848 0.839

<!-- b000922 | furniture | pages [16] -->
Team#2507817                                                             Page 16 of 25

<!-- b000923 | caption | pages [16] -->
Table 10 Classification Evaluation Index

<!-- b000925 | prose | pages [16] -->
 Accuracy:The proportion of positive samples to the total samples, the greater the accuracy, the better. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m  Recall:The proportion of results from actual positive samples that predict positive m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m samples, the greater the recall the better. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m  Precision:The proportion of the results of the predicted positive sample that are m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m actually positive, the greater the precision the better. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000926 | prose | pages [16] -->
 F1:A reconciled average of precision and recall, where precision and recall are mutually influential.

<!-- b000927 | prose | pages [16] -->
The above table shows that Accuracy, Recall and Precision are all larger and F1 is also larger, which indicates that this classification model ensures higher accuracy while recall is also high, and the classification effect of this classification model is better. 6.2.2 The Classification Results are Given We need to solve for the probability p that the dependent variable is 1:

<!-- b000928 | prose | pages [16] -->
1  p  z (12) 1 e    z 0.012 a 0.068 e 2.425 k k

<!-- b000929 | prose | pages [16] -->
After calculating the results, we took only the countries with a probability of winning the prize greater than 0.2 as shown in the table below

<!-- b000930 | caption | pages [16] -->
Table 11 Countries and Probability of Winning Medals

<!-- b000931 | prose | pages [16] -->
LBN GUM PLE ANG ESA 0.290 0.230 0.220 0.206 0.201

<!-- b000932 | prose | pages [16] -->
The resulting visualization is shown below:

<!-- b000933 | caption | pages [16] -->
Figure 14 Countries and Probability of Winning Medals

<!-- b000934 | prose | pages [16] -->
We found that these non-winning countries are mainly concentrated in the Middle East, the eastern and southern regions of Asia, sub-Saharan Africa, and some island regions. Some of these countries have suffered from wars due to political issues, while others do not have access to professional training grounds due to natural constraints. Some are economically backward and cannot afford to develop sports. However, they still have a chance to win medals in the 2028 Summer Olympics, and we look forward to their wonderful performance.

<!-- b000935 | prose | pages [16] -->
关注数学模型

<!-- b000936 | furniture | pages [16] -->
2

<!-- b000937 | furniture | pages [16] -->
MATHmodels

<!-- b000938 | furniture | pages [16] -->
获取更多资讯

<!-- b000939 | furniture | pages [17] -->
Team#2507817                                                             Page 17 of 25

<!-- b000940 | heading | pages [17] -->
7 Task 3 Relationship Between Sports and Medals

<!-- b000941 | prose | pages [17] -->
The question requires us to count the number of medals won by each country in each event based on the GSRF prediction model that we have built. Solve for the relationship between the sports and the number of medals won by each country. Identify the sports that are most important to each country and explore why. Host countries usually add events in sports that their country specializes in, and explore the effect of this on the medals won by other countries.

<!-- b000942 | heading | pages [17] -->
7.1 Relationship of the Sports to gold medals & total medals

<!-- b000943 | prose | pages [17] -->
Based on the previously drawn radar Figure 6 , we found that programs have a non- negligible impact on the number of medals. We have selected the countries that have done well in the Olympics, counted the number of medals won, and selected the events in which they have won more medals as shown below: 微信公众号：数学模型

<!-- b000944 | caption | pages [17] -->
Table 12 Some Countries and Sports They are Good at

<!-- b000945 | prose | pages [17] -->
NOC Sport Medals NOC Sport Medals Swimming 1206 Swimming 120 Athletics 1190 Diving 119 USA CHN Rowing 388 Gymnastics 109 Basketball 341 Table Tennis 94 Gymnastics 166 Swimming 505 Swimming 127 Hockey 188 JPN AUS Judo 102 Rowing 162 Volleyball 101 Athletics 100 微信号：MATHmodels Handball 96 Athletics 393 KOR GBR Archery 90 Rowing 319

<!-- b000946 | prose | pages [17] -->
As can be seen from the table, these countries will win more medals in the events they specialize in

<!-- b000947 | heading | pages [17] -->
7.2 The most Important Sports for the Country

<!-- b000948 | prose | pages [17] -->
To assess the importance of the project for the country, we introduce the project importance I(j):

<!-- b000949 | prose | pages [17] -->
m  I k (13) j M k

<!-- b000950 | prose | pages [17] -->
Among them:

<!-- b000951 | prose | pages [17] -->
mk stands for the number of medals won by the country in this event; Mk stands for the total number of medals won by the country For countries with strong comprehensive sports strength, they will achieve medals in many sports, and their program importance is not a single value, we take the United States and China as an example, calculate the importance of each program to them, and plot the radial histogram as shown below:

<!-- b000952 | furniture | pages [18] -->
Team#2507817                                                             Page 18 of 25

<!-- b000953 | prose | pages [18] -->
a) USA b) CHN

<!-- b000954 | caption | pages [18] -->
Figure 15 Radial Histogram of Sport Importance

<!-- b000955 | prose | pages [18] -->
From the figure we can easily see that the most important sport for both the United States and China is swimming. According to the related literature, it can be seen that China's performance in diving is better than that of swimming[2] , but the importance of swimming is higher than that of diving, which is because swimming has a lot of events, which greatly increases the probability of winning medals. This also aptly reflects the effect of the number of events on the results.

<!-- b000956 | prose | pages [18] -->
For countries that are weak in sports, they may have won medals in only one sport, which is the most important for that country when the importance of that sport is 1 and the importance of the rest of the sports is 0. The countries in this category and their corresponding sports in our statistics office are shown in the following chart.

<!-- b000957 | caption | pages [18] -->
Figure 16 Countries that won medals in only one sport

<!-- b000958 | prose | pages [18] -->
The graph above shows that Athletics is the most important sport for many countries, this is because Athletics has a lot of events, which provides more chances to win prizes for countries that are weaker in sports. These countries are mostly African countries, which have an advantage in Athletics.

<!-- b000959 | heading | pages [18] -->
7.3 Impact of Nationally Selected Sports on results

<!-- b000960 | prose | pages [18] -->
Preparation for the Olympic Games is a long and continuous process of fluctuation and adjustment, and the country will adjust its preparation program based on the combined results of previous Olympic Games and different international events.

<!-- b000961 | prose | pages [18] -->
The country will invest more time and energy in the development of this sport for those who already have an advantage, and more people will participate in this sport, providing more excellent human resources to promote the development of this sport, so as to achieve better

<!-- b000962 | prose | pages [18, 19] -->
关注数学模型 results in the Olympic Games.

<!-- b000963 | furniture | pages [18] -->
2

<!-- b000964 | furniture | pages [18] -->
MATHmodels

<!-- b000965 | furniture | pages [18] -->
获取更多资讯

<!-- b000966 | furniture | pages [19] -->
Team#2507817                                                             Page 19 of 25

<!-- b000968 | prose | pages [19] -->
For programs with high potential, which have had mediocre results in the past, the country will increase funding and adopt a strategy appropriate to the program, thus improving Olympic performance.

<!-- b000969 | prose | pages [19] -->
In the case of projects that have never won an award, they are usually not prevalent in the country, or the people of the country are generally not good at them. The country does not invest much time and money in such programs.

<!-- b000970 | heading | pages [19] -->
8 Task 4 The Impact of Great Coach

<!-- b000971 | prose | pages [19] -->
微信公众号：数学模型 The question asks us to search for fluctuations in performance due to the hiring of "great coaches" in previous years, to estimate the effect of this effect on the number of medals, and to identify the countries that need to hire great coaches the most. We need to build a regression model to measure the impact of this effect.

<!-- b000972 | heading | pages [19] -->
8.1 Lasso Regression Model

<!-- b000973 | heading | pages [19] -->
8.1.1 Model Preparation

<!-- b000974 | prose | pages [19] -->
In order to further quantify the country's performance at each Olympic Games, we have chosen to assign points to the different medals, with the following rules for assigning points: 微信号：MATHmodels

<!-- b000975 | caption | pages [19] -->
Table 13 Score table

<!-- b000976 | prose | pages [19] -->
Gold Medal Silver Medal Bronze Medal No Medal 10 6 3 0

<!-- b000977 | prose | pages [19] -->
We checked the famous and great coaches of history and found out that women's gymnastics coach Bela Karolyi coached many Olympic champions[3] . He coached in Romania in the 1976 and 1980 Olympics, and in the USA in the Olympics from 1984~2016[4] . We counted the scores of Romania and USA in women's gymnastics in every Olympics between 1952 and 2024, as shown below:

<!-- b000978 | caption | pages [19] -->
Figure 17 ROU vs USA Women's Gymnastics Scores

<!-- b000979 | prose | pages [19] -->
We found a significant improvement in the country's women's gymnastics scores after this coach began coaching. When he left ROU, ROU's scores improved slightly, but generally trended slowly downward. When he came to USA, USA's gymnastics scores still fluctuated significantly, but had an overall upward trend. The Spearman correlation coefficient was then analyzed with the following formula:

<!-- b000980 | prose | pages [19, 20] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m       x x y y i i i   (14)     2 2     x x y y i i i i

<!-- b000981 | furniture | pages [19] -->
m

<!-- b000982 | furniture | pages [19] -->
m

<!-- b000983 | furniture | pages [19] -->
m

<!-- b000984 | furniture | pages [19] -->
m

<!-- b000985 | furniture | pages [19] -->
m

<!-- b000986 | furniture | pages [19] -->
m

<!-- b000987 | furniture | pages [19] -->
m

<!-- b000988 | furniture | pages [19] -->
m

<!-- b000989 | furniture | pages [19] -->
m

<!-- b000990 | furniture | pages [19] -->
m

<!-- b000991 | furniture | pages [19] -->
m

<!-- b000992 | furniture | pages [19] -->
m

<!-- b000993 | furniture | pages [19] -->
m

<!-- b000994 | furniture | pages [19] -->
m

<!-- b000995 | furniture | pages [19] -->
m

<!-- b000996 | furniture | pages [19] -->
m

<!-- b000997 | furniture | pages [19] -->
m

<!-- b000998 | furniture | pages [19] -->
m

<!-- b000999 | furniture | pages [19] -->
m

<!-- b001000 | furniture | pages [19] -->
m

<!-- b001001 | furniture | pages [19] -->
m

<!-- b001002 | furniture | pages [19] -->
m

<!-- b001003 | furniture | pages [19] -->
m

<!-- b001004 | furniture | pages [19] -->
m

<!-- b001005 | furniture | pages [19] -->
m

<!-- b001006 | furniture | pages [19] -->
m

<!-- b001007 | furniture | pages [19] -->
m

<!-- b001008 | furniture | pages [19] -->
m

<!-- b001009 | furniture | pages [19] -->
m

<!-- b001010 | furniture | pages [19] -->
m

<!-- b001011 | furniture | pages [19] -->
m

<!-- b001012 | furniture | pages [19] -->
m

<!-- b001013 | furniture | pages [19] -->
m

<!-- b001014 | furniture | pages [19] -->
m

<!-- b001015 | furniture | pages [19] -->
m

<!-- b001016 | furniture | pages [19] -->
m

<!-- b001017 | furniture | pages [19] -->
m

<!-- b001018 | furniture | pages [19] -->
m

<!-- b001019 | furniture | pages [19] -->
m

<!-- b001020 | furniture | pages [19] -->
m

<!-- b001021 | furniture | pages [19] -->
m

<!-- b001022 | furniture | pages [19] -->
m

<!-- b001023 | furniture | pages [19] -->
m

<!-- b001024 | furniture | pages [19] -->
m

<!-- b001025 | furniture | pages [19] -->
m

<!-- b001026 | furniture | pages [19] -->
m

<!-- b001027 | furniture | pages [19] -->
m

<!-- b001028 | furniture | pages [19] -->
m

<!-- b001029 | furniture | pages [19] -->
m

<!-- b001030 | furniture | pages [19] -->
m

<!-- b001031 | furniture | pages [19] -->
m

<!-- b001032 | furniture | pages [19] -->
m

<!-- b001033 | furniture | pages [19] -->
m

<!-- b001034 | furniture | pages [19] -->
m

<!-- b001035 | furniture | pages [19] -->
m

<!-- b001036 | furniture | pages [19] -->
m

<!-- b001037 | furniture | pages [19] -->
m

<!-- b001038 | furniture | pages [19] -->
m

<!-- b001039 | furniture | pages [19] -->
m

<!-- b001040 | furniture | pages [19] -->
m

<!-- b001041 | furniture | pages [19] -->
m

<!-- b001042 | furniture | pages [19] -->
m

<!-- b001043 | furniture | pages [19] -->
m

<!-- b001044 | furniture | pages [19] -->
m

<!-- b001045 | furniture | pages [19] -->
m

<!-- b001046 | furniture | pages [19] -->
m

<!-- b001047 | furniture | pages [19] -->
m

<!-- b001048 | furniture | pages [19] -->
m

<!-- b001049 | furniture | pages [19] -->
m

<!-- b001050 | furniture | pages [19] -->
m

<!-- b001051 | furniture | pages [19] -->
m

<!-- b001052 | furniture | pages [19] -->
m

<!-- b001053 | furniture | pages [19] -->
m

<!-- b001054 | furniture | pages [19] -->
m

<!-- b001055 | furniture | pages [19] -->
m

<!-- b001056 | furniture | pages [19] -->
m

<!-- b001057 | furniture | pages [19] -->
m

<!-- b001058 | furniture | pages [19] -->
m

<!-- b001059 | furniture | pages [19] -->
m

<!-- b001060 | furniture | pages [19] -->
m

<!-- b001061 | furniture | pages [19] -->
m

<!-- b001062 | furniture | pages [19] -->
m

<!-- b001063 | furniture | pages [19] -->
m

<!-- b001064 | furniture | pages [19] -->
m

<!-- b001065 | furniture | pages [19] -->
m

<!-- b001066 | furniture | pages [19] -->
m

<!-- b001067 | furniture | pages [19] -->
m

<!-- b001068 | furniture | pages [19] -->
m

<!-- b001069 | furniture | pages [19] -->
m

<!-- b001070 | furniture | pages [19] -->
m

<!-- b001071 | furniture | pages [19] -->
m

<!-- b001072 | furniture | pages [19] -->
m

<!-- b001073 | furniture | pages [19] -->
m

<!-- b001074 | furniture | pages [19] -->
m

<!-- b001075 | furniture | pages [19] -->
m

<!-- b001076 | furniture | pages [19] -->
m

<!-- b001077 | furniture | pages [19] -->
m

<!-- b001078 | furniture | pages [19] -->
m

<!-- b001079 | furniture | pages [19] -->
m

<!-- b001080 | furniture | pages [19] -->
m

<!-- b001081 | furniture | pages [19] -->
m

<!-- b001082 | furniture | pages [19] -->
m

<!-- b001083 | furniture | pages [19] -->
m

<!-- b001084 | furniture | pages [19] -->
m

<!-- b001085 | furniture | pages [19] -->
m

<!-- b001086 | furniture | pages [19] -->
m

<!-- b001087 | furniture | pages [19] -->
m

<!-- b001088 | furniture | pages [19] -->
m

<!-- b001089 | furniture | pages [19] -->
m

<!-- b001090 | furniture | pages [19] -->
m

<!-- b001091 | furniture | pages [19] -->
m

<!-- b001092 | furniture | pages [19] -->
m

<!-- b001093 | furniture | pages [19] -->
m

<!-- b001094 | furniture | pages [19] -->
m

<!-- b001095 | furniture | pages [19] -->
m

<!-- b001096 | furniture | pages [19] -->
m

<!-- b001097 | furniture | pages [19] -->
m

<!-- b001098 | furniture | pages [19] -->
m

<!-- b001099 | furniture | pages [19] -->
m

<!-- b001100 | furniture | pages [19] -->
m

<!-- b001101 | furniture | pages [19] -->
m

<!-- b001102 | furniture | pages [19] -->
m

<!-- b001103 | furniture | pages [19] -->
m

<!-- b001104 | furniture | pages [19] -->
m

<!-- b001105 | furniture | pages [19] -->
m

<!-- b001106 | furniture | pages [19] -->
m

<!-- b001107 | furniture | pages [19] -->
m

<!-- b001108 | furniture | pages [19] -->
m

<!-- b001109 | furniture | pages [19] -->
m

<!-- b001110 | furniture | pages [19] -->
m

<!-- b001111 | furniture | pages [19] -->
m

<!-- b001112 | furniture | pages [19] -->
m

<!-- b001113 | furniture | pages [19] -->
m

<!-- b001114 | furniture | pages [19] -->
m

<!-- b001115 | furniture | pages [19] -->
m

<!-- b001116 | furniture | pages [19] -->
m

<!-- b001117 | furniture | pages [19] -->
m

<!-- b001118 | furniture | pages [19] -->
m

<!-- b001119 | furniture | pages [19] -->
m

<!-- b001120 | furniture | pages [19] -->
m

<!-- b001121 | furniture | pages [19] -->
m

<!-- b001122 | furniture | pages [19] -->
m

<!-- b001123 | furniture | pages [19] -->
m

<!-- b001124 | furniture | pages [19] -->
m

<!-- b001125 | furniture | pages [19] -->
m

<!-- b001126 | furniture | pages [19] -->
m

<!-- b001127 | furniture | pages [19] -->
m

<!-- b001128 | furniture | pages [19] -->
m

<!-- b001129 | furniture | pages [19] -->
m

<!-- b001130 | furniture | pages [19] -->
m

<!-- b001131 | furniture | pages [19] -->
m

<!-- b001132 | furniture | pages [19] -->
m

<!-- b001133 | furniture | pages [19] -->
m

<!-- b001134 | furniture | pages [19] -->
m

<!-- b001135 | furniture | pages [19] -->
m

<!-- b001136 | furniture | pages [19] -->
m

<!-- b001137 | furniture | pages [19] -->
m

<!-- b001138 | furniture | pages [19] -->
m

<!-- b001139 | furniture | pages [19] -->
m

<!-- b001140 | furniture | pages [19] -->
m

<!-- b001141 | furniture | pages [19] -->
m

<!-- b001142 | furniture | pages [19] -->
m

<!-- b001143 | furniture | pages [19] -->
m

<!-- b001144 | furniture | pages [19] -->
m

<!-- b001145 | furniture | pages [19] -->
m

<!-- b001146 | furniture | pages [19] -->
m

<!-- b001147 | furniture | pages [19] -->
m

<!-- b001148 | furniture | pages [19] -->
m

<!-- b001149 | furniture | pages [19] -->
m

<!-- b001150 | furniture | pages [19] -->
m

<!-- b001151 | furniture | pages [19] -->
m

<!-- b001152 | furniture | pages [19] -->
m

<!-- b001153 | furniture | pages [19] -->
m

<!-- b001154 | furniture | pages [19] -->
m

<!-- b001155 | furniture | pages [19] -->
m

<!-- b001156 | furniture | pages [19] -->
m

<!-- b001157 | furniture | pages [19] -->
m

<!-- b001158 | furniture | pages [19] -->
m

<!-- b001159 | furniture | pages [19] -->
m

<!-- b001160 | furniture | pages [19] -->
m

<!-- b001161 | furniture | pages [19] -->
m

<!-- b001162 | furniture | pages [19] -->
m

<!-- b001163 | furniture | pages [19] -->
m

<!-- b001164 | furniture | pages [19] -->
m

<!-- b001165 | furniture | pages [19] -->
m

<!-- b001166 | furniture | pages [19] -->
m

<!-- b001167 | furniture | pages [19] -->
m

<!-- b001168 | furniture | pages [19] -->
m

<!-- b001169 | furniture | pages [19] -->
m

<!-- b001170 | furniture | pages [19] -->
m

<!-- b001171 | furniture | pages [19] -->
m

<!-- b001172 | furniture | pages [19] -->
m

<!-- b001173 | furniture | pages [19] -->
m

<!-- b001174 | furniture | pages [19] -->
m

<!-- b001175 | furniture | pages [19] -->
m

<!-- b001176 | furniture | pages [19] -->
m

<!-- b001177 | furniture | pages [19] -->
m

<!-- b001178 | furniture | pages [19] -->
m

<!-- b001179 | furniture | pages [19] -->
m

<!-- b001180 | furniture | pages [19] -->
m

<!-- b001181 | furniture | pages [19] -->
m

<!-- b001182 | furniture | pages [19] -->
m

<!-- b001183 | furniture | pages [19] -->
m

<!-- b001184 | furniture | pages [19] -->
m

<!-- b001185 | furniture | pages [19] -->
m

<!-- b001186 | furniture | pages [19] -->
m

<!-- b001187 | furniture | pages [19] -->
m

<!-- b001188 | furniture | pages [19] -->
m

<!-- b001189 | furniture | pages [19] -->
m

<!-- b001190 | furniture | pages [19] -->
m

<!-- b001191 | furniture | pages [19] -->
m

<!-- b001192 | furniture | pages [19] -->
m

<!-- b001193 | furniture | pages [19] -->
m

<!-- b001194 | furniture | pages [19] -->
m

<!-- b001195 | furniture | pages [19] -->
m

<!-- b001196 | furniture | pages [19] -->
m

<!-- b001197 | furniture | pages [19] -->
m

<!-- b001198 | furniture | pages [19] -->
m

<!-- b001199 | furniture | pages [19] -->
m

<!-- b001200 | furniture | pages [19] -->
m

<!-- b001201 | furniture | pages [19] -->
m

<!-- b001202 | furniture | pages [19] -->
m

<!-- b001203 | furniture | pages [19] -->
m

<!-- b001204 | furniture | pages [19] -->
m

<!-- b001205 | furniture | pages [19] -->
m

<!-- b001206 | furniture | pages [19] -->
m

<!-- b001207 | furniture | pages [19] -->
m

<!-- b001208 | furniture | pages [19] -->
m

<!-- b001209 | furniture | pages [19] -->
m

<!-- b001210 | furniture | pages [19] -->
m

<!-- b001211 | furniture | pages [19] -->
m

<!-- b001212 | furniture | pages [19] -->
m

<!-- b001213 | furniture | pages [19] -->
m

<!-- b001214 | furniture | pages [19] -->
m

<!-- b001215 | furniture | pages [19] -->
m

<!-- b001216 | furniture | pages [19] -->
m

<!-- b001217 | furniture | pages [19] -->
m

<!-- b001218 | furniture | pages [19] -->
m

<!-- b001219 | furniture | pages [19] -->
m

<!-- b001220 | furniture | pages [19] -->
m

<!-- b001221 | furniture | pages [19] -->
m

<!-- b001222 | furniture | pages [19] -->
m

<!-- b001223 | furniture | pages [19] -->
m

<!-- b001224 | furniture | pages [19] -->
m

<!-- b001225 | furniture | pages [19] -->
m

<!-- b001226 | furniture | pages [19] -->
m

<!-- b001227 | furniture | pages [19] -->
m

<!-- b001228 | furniture | pages [19] -->
m

<!-- b001229 | furniture | pages [19] -->
m

<!-- b001230 | furniture | pages [19] -->
m

<!-- b001231 | furniture | pages [19] -->
m

<!-- b001232 | furniture | pages [19] -->
m

<!-- b001233 | furniture | pages [19] -->
m

<!-- b001234 | furniture | pages [19] -->
m

<!-- b001235 | furniture | pages [19] -->
m

<!-- b001236 | furniture | pages [19] -->
m

<!-- b001237 | furniture | pages [19] -->
m

<!-- b001238 | furniture | pages [19] -->
m

<!-- b001239 | furniture | pages [19] -->
m

<!-- b001240 | furniture | pages [19] -->
m

<!-- b001241 | furniture | pages [19] -->
m

<!-- b001242 | furniture | pages [19] -->
m

<!-- b001243 | furniture | pages [19] -->
m

<!-- b001244 | furniture | pages [19] -->
m

<!-- b001245 | furniture | pages [19] -->
m

<!-- b001246 | furniture | pages [19] -->
m

<!-- b001247 | furniture | pages [19] -->
m

<!-- b001248 | furniture | pages [19] -->
m

<!-- b001249 | furniture | pages [19] -->
m

<!-- b001250 | furniture | pages [19] -->
m

<!-- b001251 | furniture | pages [19] -->
m

<!-- b001252 | furniture | pages [19] -->
m

<!-- b001253 | furniture | pages [19] -->
m

<!-- b001254 | furniture | pages [19] -->
m

<!-- b001255 | furniture | pages [19] -->
m

<!-- b001256 | furniture | pages [19] -->
m

<!-- b001257 | furniture | pages [19] -->
m

<!-- b001258 | furniture | pages [19] -->
m

<!-- b001259 | furniture | pages [19] -->
m

<!-- b001260 | furniture | pages [19] -->
m

<!-- b001261 | furniture | pages [19] -->
m

<!-- b001262 | furniture | pages [19] -->
m

<!-- b001263 | furniture | pages [19] -->
m

<!-- b001264 | furniture | pages [19] -->
m

<!-- b001265 | furniture | pages [19] -->
m

<!-- b001266 | furniture | pages [19] -->
m

<!-- b001267 | furniture | pages [19] -->
m

<!-- b001268 | furniture | pages [19] -->
m

<!-- b001269 | furniture | pages [19] -->
m

<!-- b001270 | furniture | pages [19] -->
m

<!-- b001271 | furniture | pages [19] -->
m

<!-- b001272 | furniture | pages [19] -->
m

<!-- b001273 | furniture | pages [19] -->
m

<!-- b001274 | furniture | pages [19] -->
m

<!-- b001275 | furniture | pages [19] -->
m

<!-- b001276 | furniture | pages [19] -->
m

<!-- b001277 | furniture | pages [19] -->
m

<!-- b001278 | furniture | pages [19] -->
m

<!-- b001279 | furniture | pages [19] -->
m

<!-- b001280 | furniture | pages [19] -->
m

<!-- b001281 | furniture | pages [19] -->
m

<!-- b001282 | furniture | pages [19] -->
m

<!-- b001283 | furniture | pages [19] -->
m

<!-- b001284 | furniture | pages [19] -->
m

<!-- b001285 | furniture | pages [19] -->
m

<!-- b001286 | furniture | pages [19] -->
m

<!-- b001287 | furniture | pages [19] -->
m

<!-- b001288 | furniture | pages [19] -->
m

<!-- b001289 | furniture | pages [19] -->
m

<!-- b001290 | furniture | pages [19] -->
m

<!-- b001291 | furniture | pages [19] -->
m

<!-- b001292 | furniture | pages [19] -->
m

<!-- b001293 | furniture | pages [19] -->
m

<!-- b001294 | furniture | pages [19] -->
m

<!-- b001295 | furniture | pages [19] -->
m

<!-- b001296 | furniture | pages [19] -->
m

<!-- b001297 | furniture | pages [19] -->
m

<!-- b001298 | furniture | pages [19] -->
m

<!-- b001299 | furniture | pages [19] -->
m

<!-- b001300 | furniture | pages [19] -->
m

<!-- b001301 | furniture | pages [19] -->
m

<!-- b001302 | furniture | pages [19] -->
m

<!-- b001303 | furniture | pages [19] -->
m

<!-- b001304 | furniture | pages [19] -->
m

<!-- b001305 | furniture | pages [20] -->
Team#2507817                                                             Page 20 of 25

<!-- b001307 | prose | pages [20] -->
The correlation coefficient between "great coaches" and the number of medals was calculated to be 0.874.

<!-- b001308 | prose | pages [20] -->
From the above analysis we can clearly realize that great coaches play a not insignificant role in improving sports performance, so we establish Lasso regression model for quantitative analysis

<!-- b001309 | heading | pages [20] -->
8.1.2 Lasso Regression Modeling

<!-- b001310 | prose | pages [20] -->
Lasso regression is an alternative to least squares for compression estimation, and its main goal is to find a balance between model simplicity and accuracy.

<!-- b001311 | heading | pages [20] -->
1) Linear Regression Model

<!-- b001312 | prose | pages [20] -->
A linear regression model is developed as follows                 y I V S A H C (15) 0 1 2 3 4 5 6

<!-- b001313 | prose | pages [20] -->
 I,V,S,H,C are the indicators of the regression I: Importance of the program to the state. According to the analysis in Task3, the state will use quality strategies to improve performance in programs of high importance, and these strategies include hiring great coaches.

<!-- b001314 | prose | pages [20] -->
V: Average number of points scored by the country in the last two Olympic Games.

<!-- b001315 | prose | pages [20] -->
This indicator represents the average of the sum of the total points of the two most recent editions and reflects the country's overall performance in the two most recent Olympic Games.

<!-- b001316 | prose | pages [20] -->
S: theoretical points for the country on the program. s=I V is the program importance vs. average points score A: The number of participants from that country in the current Olympic Games. The more athletes that participate, the greater the probability of winning a prize H: The country's historical average points score for the project. This indicator reflects the level of the country's program and can reflect fluctuations in its performance.

<!-- b001317 | prose | pages [20] -->
C: Coaching Impact. To quantify the impact of coaching on performance, we define:

<!-- b001318 | prose | pages [20] -->
coaching the first year of coaching C = 1, the length of each increase in the number of Olympic cycles, the performance has a linear increase of 0.1, when the coach leaves, the performance of the exponential decline,t represents the number of Olympic cycles that have begun & have ceased to coach:

<!-- b001319 | prose | pages [20] -->
  1 0.1 t Start Coaching  C (16) e t Stop Coaching   y is the score obtained from the regression  βi is the coefficient to be estimated and ε is the error term

<!-- b001320 | heading | pages [20] -->
2) L1 Regularization

<!-- b001321 | prose | pages [20] -->
In the regression, we introduce an L1 penalty term so that the regression does not prioritize the reduction of any particular model parameter, retaining a few important features and

<!-- b001322 | prose | pages [20, 21] -->
关注数学模型 promoting model sparsity:

<!-- b001323 | furniture | pages [20] -->
2

<!-- b001324 | furniture | pages [20] -->
MATHmodels

<!-- b001325 | furniture | pages [20] -->
获取更多资讯

<!-- b001326 | furniture | pages [21] -->
Page 21 of 25

<!-- b001327 | furniture | pages [21] -->
Team#2507817

<!-- b001329 | prose | pages [21] -->
6 L1 = λ∑|βi| (17) i=1 where is used to control the degree of regularization:

<!-- b001330 | prose | pages [21] -->
When = 0, all features are considered and the effect of regularization disappears, which is equivalent to ordinary linear regression When tends to infinity, no features are considered and some coefficients are pushed to exactly zero,which will gradually eliminate more features. Effectively control the model complexity.

<!-- b001331 | prose | pages [21] -->
The resulting Lasso regression shrinks the coefficients toward 0, with the deviation increasing with and the variance increasing with decreasing .

<!-- b001332 | heading | pages [21] -->
3) Objective Function

<!-- b001333 | prose | pages [21] -->
Hmodels Our goal with Lasso regression is to find the coefficients that minimize the sum of squared differences between the predicted and true values:

<!-- b001334 | prose | pages [21] -->
● RSS = Σ(yi yi) (18) i=1 Objective Function=min(RSS+L1)

<!-- b001335 | heading | pages [21] -->
8.2 Lasso Regression Results

<!-- b001336 | prose | pages [21] -->
8.2.1 The Regression Equation is Given We use cross-validation to select . The selected should minimize the model mean square error (MSE), and the following figure visualizes the process of selecting :

<!-- b001337 | prose | pages [21] -->
0.14 -0- history_ave -O- athlete_num -- imp*ave -0- importance -0- coach

<!-- b001338 | prose | pages [21] -->
2.5 0.5

<!-- b001339 | heading | pages [21] -->
Model coefficients

<!-- b001340 | prose | pages [21] -->
1.5 MSE

<!-- b001341 | prose | pages [21] -->
0.5

<!-- b001342 | prose | pages [21] -->
logλ logλ

<!-- b001343 | caption | pages [21] -->
Figure 18 Cross-Validation Diagram

<!-- b001344 | caption | pages [21] -->
Figure 19 Plot of vs. Model Coefficients

<!-- b001345 | caption | pages [21] -->
Figure 18 shows that as the logarithmic value of changes, the coefficients of the individual

<!-- b001346 | prose | pages [21] -->
variables also change, and can be considered to be excluded from the model when they become zero.

<!-- b001347 | prose | pages [21] -->
The coefficients of the regression equation were calculated using Python as shown in the table below:

<!-- b001348 | caption | pages [21] -->
Table 14 Coefficient of regression equation

<!-- b001349 | prose | pages [21] -->
H Intercept V S A C I Variable Names 0.906 0.027 Standardized coefficient 2.721 -0.046 0.144 26.944 0 R² 0.708

<!-- b001350 | prose | pages [21, 22] -->
When the coefficient of the standardized variable in the model is 0, it means that this variable is excluded from the model. It can be seen that the coefficient of the importance of the project to the country (I) is 0, which proves that this variable does not have an impact on the results of the model and is excluded from the model. The regression equation is as follows:

<!-- b001351 | furniture | pages [22] -->
Page 22 of 25

<!-- b001352 | furniture | pages [22] -->
Team#2507817

<!-- b001354 | prose | pages [22] -->
y = 2.721− 0.046V + 0.906S + 0.027A + 0.144H + 26.944C (61) 8.2.2 Advice on Investing in "Great Coach"

<!-- b001355 | prose | pages [22] -->
After in-depth analysis and data visualization, we have selected the following sports with great potential: Chinese women's volleyball, Brazilian women's soccer and Romanian women's gymnastics. These programs have been excellent in the past, but are now average and of high importance:

<!-- b001356 | prose | pages [22] -->
60

<!-- b001357 | prose | pages [22] -->
50

<!-- b001358 | prose | pages [22] -->
40

<!-- b001359 | prose | pages [22] -->
30

<!-- b001360 | prose | pages [22] -->
20

<!-- b001361 | prose | pages [22] -->
10

<!-- b001362 | prose | pages [22] -->
0 2000 2024 1984 1988 1992 1996 2004 2008 2012 2016 2020 ROU,Women's Gymnastics CHN,Women's Volleyball BRA,Women's Soccer

<!-- b001363 | caption | pages [22] -->
Figure 20 Fluctuations in the Country's Score on the Item

<!-- b001364 | prose | pages [22] -->
Based on Lasso's regression model, we predict that if these three countries invest in the "Great Coach" program in their respective sports, then their 2028 Olympic scores in this sport will be as shown in the table below:

<!-- b001365 | caption | pages [22] -->
Table 15 2024 Scores vs 2028 Scores

<!-- b001366 | prose | pages [22] -->
CHN, Women's Volleyball BRA, Women's Soccer ROU, Women's Gymnastics 2024 0 6 3 5.33 8.86 2028 36.65

<!-- b001367 | prose | pages [22] -->
We have found that after investing in Great Coaching, countries have seen significant improvements in the performance of these potential programs, thus proving the importance of Great Coaching for these countries and programs.

<!-- b001368 | prose | pages [22] -->
Task 5 Original Opinion 9

<!-- b001369 | prose | pages [22] -->
9.1 Host Effect

<!-- b001370 | prose | pages [22] -->
In Task 1 we found that being a host has an advantage in terms of getting more medals, so we picked two countries, the United States and Japan, and compared the change in the number of gold medals and the total number of medals when they were hosts and non-hosts:

<!-- b001371 | prose | pages [22, 23] -->
关注数学模型 a) USA b) JPN

<!-- b001372 | furniture | pages [22] -->
获取更多资讯

<!-- b001373 | furniture | pages [23] -->
Team#2507817                                                             Page 23 of 25

<!-- b001375 | caption | pages [23] -->
Figure 21 Change in number of medals

<!-- b001376 | prose | pages [23] -->
微信公众号：数学模型 We have found that when the United States and Japan are the hosts, there is a 1.4 to 1.9 times increase in the number of gold medals and the total number of medals . The IOC can encourage countries to apply to host the Olympics based on this phenomenon.

<!-- b001377 | heading | pages [23] -->
9.2 Talented Athletes

<!-- b001378 | prose | pages [23] -->
In competition, there are athletes who train hard and achieve good results, and there are also highly talented competitors. If a country has been competing in an event for a long time and has only won a medal once, the winner can be called a "gifted athlete". For example, in the men's hurdles, China has been competing since 1984, and only Liu Xiang won the title in 2004;

<!-- b001379 | prose | pages [23] -->
微信号：MATHmodels the rest of the athletes have not won a medal.

<!-- b001380 | caption | pages [23] -->
Figure 22 Chinese men's hurdles

<!-- b001381 | prose | pages [23] -->
Accordingly, the IOC could encourage countries to tap talent in such programs and invest more in finding more talented players, who in turn could drive more hard-working players to the Olympic podium.

<!-- b001382 | heading | pages [23] -->
10 Error Analysis and Sensitivity Analysis

<!-- b001383 | prose | pages [23] -->
Based on the GSRF model established in the first problem, the sensitivity of athletes_num, Total event to Model can be obtained by changing athletes_num A , Total event E in the ij ij model and observing the corresponding changes in Model.

<!-- b001384 | heading | pages [23] -->
10.1 Definition of Sensitivity

<!-- b001385 | prose | pages [23] -->
Define the result of this forecast as y , the difference between this result and the previous  , and the average sensitivity is defined forecast as y ps as:

<!-- b001386 | prose | pages [23] -->
 ps y y (20)

<!-- b001387 | prose | pages [23, 24] -->
This indicator reflects the magnitude of change in the projected number of medals m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m following a change in the indicator.

<!-- b001388 | furniture | pages [23] -->
m

<!-- b001389 | furniture | pages [23] -->
m

<!-- b001390 | furniture | pages [23] -->
m

<!-- b001391 | furniture | pages [23] -->
m

<!-- b001392 | furniture | pages [23] -->
m

<!-- b001393 | furniture | pages [23] -->
m

<!-- b001394 | furniture | pages [23] -->
m

<!-- b001395 | furniture | pages [23] -->
m

<!-- b001396 | furniture | pages [23] -->
m

<!-- b001397 | furniture | pages [23] -->
m

<!-- b001398 | furniture | pages [23] -->
m

<!-- b001399 | furniture | pages [23] -->
m

<!-- b001400 | furniture | pages [23] -->
m

<!-- b001401 | furniture | pages [23] -->
m

<!-- b001402 | furniture | pages [23] -->
m

<!-- b001403 | furniture | pages [23] -->
m

<!-- b001404 | furniture | pages [23] -->
m

<!-- b001405 | furniture | pages [23] -->
m

<!-- b001406 | furniture | pages [23] -->
m

<!-- b001407 | furniture | pages [23] -->
m

<!-- b001408 | furniture | pages [23] -->
m

<!-- b001409 | furniture | pages [23] -->
m

<!-- b001410 | furniture | pages [23] -->
m

<!-- b001411 | furniture | pages [23] -->
m

<!-- b001412 | furniture | pages [23] -->
m

<!-- b001413 | furniture | pages [23] -->
m

<!-- b001414 | furniture | pages [23] -->
m

<!-- b001415 | furniture | pages [23] -->
m

<!-- b001416 | furniture | pages [23] -->
m

<!-- b001417 | furniture | pages [23] -->
m

<!-- b001418 | furniture | pages [23] -->
m

<!-- b001419 | furniture | pages [23] -->
m

<!-- b001420 | furniture | pages [23] -->
m

<!-- b001421 | furniture | pages [23] -->
m

<!-- b001422 | furniture | pages [23] -->
m

<!-- b001423 | furniture | pages [23] -->
m

<!-- b001424 | furniture | pages [23] -->
m

<!-- b001425 | furniture | pages [23] -->
m

<!-- b001426 | furniture | pages [23] -->
m

<!-- b001427 | furniture | pages [23] -->
m

<!-- b001428 | furniture | pages [23] -->
m

<!-- b001429 | furniture | pages [23] -->
m

<!-- b001430 | furniture | pages [23] -->
m

<!-- b001431 | furniture | pages [23] -->
m

<!-- b001432 | furniture | pages [23] -->
m

<!-- b001433 | furniture | pages [23] -->
m

<!-- b001434 | furniture | pages [23] -->
m

<!-- b001435 | furniture | pages [23] -->
m

<!-- b001436 | furniture | pages [23] -->
m

<!-- b001437 | furniture | pages [23] -->
m

<!-- b001438 | furniture | pages [23] -->
m

<!-- b001439 | furniture | pages [23] -->
m

<!-- b001440 | furniture | pages [23] -->
m

<!-- b001441 | furniture | pages [23] -->
m

<!-- b001442 | furniture | pages [23] -->
m

<!-- b001443 | furniture | pages [23] -->
m

<!-- b001444 | furniture | pages [23] -->
m

<!-- b001445 | furniture | pages [23] -->
m

<!-- b001446 | furniture | pages [23] -->
m

<!-- b001447 | furniture | pages [23] -->
m

<!-- b001448 | furniture | pages [23] -->
m

<!-- b001449 | furniture | pages [23] -->
m

<!-- b001450 | furniture | pages [23] -->
m

<!-- b001451 | furniture | pages [23] -->
m

<!-- b001452 | furniture | pages [23] -->
m

<!-- b001453 | furniture | pages [23] -->
m

<!-- b001454 | furniture | pages [23] -->
m

<!-- b001455 | furniture | pages [23] -->
m

<!-- b001456 | furniture | pages [23] -->
m

<!-- b001457 | furniture | pages [23] -->
m

<!-- b001458 | furniture | pages [23] -->
m

<!-- b001459 | furniture | pages [23] -->
m

<!-- b001460 | furniture | pages [23] -->
m

<!-- b001461 | furniture | pages [23] -->
m

<!-- b001462 | furniture | pages [23] -->
m

<!-- b001463 | furniture | pages [23] -->
m

<!-- b001464 | furniture | pages [23] -->
m

<!-- b001465 | furniture | pages [23] -->
m

<!-- b001466 | furniture | pages [23] -->
m

<!-- b001467 | furniture | pages [23] -->
m

<!-- b001468 | furniture | pages [23] -->
m

<!-- b001469 | furniture | pages [23] -->
m

<!-- b001470 | furniture | pages [23] -->
m

<!-- b001471 | furniture | pages [23] -->
m

<!-- b001472 | furniture | pages [23] -->
m

<!-- b001473 | furniture | pages [23] -->
m

<!-- b001474 | furniture | pages [23] -->
m

<!-- b001475 | furniture | pages [23] -->
m

<!-- b001476 | furniture | pages [23] -->
m

<!-- b001477 | furniture | pages [23] -->
m

<!-- b001478 | furniture | pages [23] -->
m

<!-- b001479 | furniture | pages [23] -->
m

<!-- b001480 | furniture | pages [23] -->
m

<!-- b001481 | furniture | pages [23] -->
m

<!-- b001482 | furniture | pages [23] -->
m

<!-- b001483 | furniture | pages [23] -->
m

<!-- b001484 | furniture | pages [23] -->
m

<!-- b001485 | furniture | pages [23] -->
m

<!-- b001486 | furniture | pages [23] -->
m

<!-- b001487 | furniture | pages [23] -->
m

<!-- b001488 | furniture | pages [23] -->
m

<!-- b001489 | furniture | pages [23] -->
m

<!-- b001490 | furniture | pages [23] -->
m

<!-- b001491 | furniture | pages [23] -->
m

<!-- b001492 | furniture | pages [23] -->
m

<!-- b001493 | furniture | pages [23] -->
m

<!-- b001494 | furniture | pages [23] -->
m

<!-- b001495 | furniture | pages [23] -->
m

<!-- b001496 | furniture | pages [23] -->
m

<!-- b001497 | furniture | pages [23] -->
m

<!-- b001498 | furniture | pages [23] -->
m

<!-- b001499 | furniture | pages [23] -->
m

<!-- b001500 | furniture | pages [23] -->
m

<!-- b001501 | furniture | pages [23] -->
m

<!-- b001502 | furniture | pages [23] -->
m

<!-- b001503 | furniture | pages [23] -->
m

<!-- b001504 | furniture | pages [23] -->
m

<!-- b001505 | furniture | pages [23] -->
m

<!-- b001506 | furniture | pages [23] -->
m

<!-- b001507 | furniture | pages [23] -->
m

<!-- b001508 | furniture | pages [23] -->
m

<!-- b001509 | furniture | pages [23] -->
m

<!-- b001510 | furniture | pages [23] -->
m

<!-- b001511 | furniture | pages [23] -->
m

<!-- b001512 | furniture | pages [23] -->
m

<!-- b001513 | furniture | pages [23] -->
m

<!-- b001514 | furniture | pages [23] -->
m

<!-- b001515 | furniture | pages [23] -->
m

<!-- b001516 | furniture | pages [23] -->
m

<!-- b001517 | furniture | pages [23] -->
m

<!-- b001518 | furniture | pages [23] -->
m

<!-- b001519 | furniture | pages [23] -->
m

<!-- b001520 | furniture | pages [23] -->
m

<!-- b001521 | furniture | pages [23] -->
m

<!-- b001522 | furniture | pages [23] -->
m

<!-- b001523 | furniture | pages [23] -->
m

<!-- b001524 | furniture | pages [23] -->
m

<!-- b001525 | furniture | pages [23] -->
m

<!-- b001526 | furniture | pages [23] -->
m

<!-- b001527 | furniture | pages [23] -->
m

<!-- b001528 | furniture | pages [23] -->
m

<!-- b001529 | furniture | pages [23] -->
m

<!-- b001530 | furniture | pages [23] -->
m

<!-- b001531 | furniture | pages [23] -->
m

<!-- b001532 | furniture | pages [23] -->
m

<!-- b001533 | furniture | pages [23] -->
m

<!-- b001534 | furniture | pages [23] -->
m

<!-- b001535 | furniture | pages [23] -->
m

<!-- b001536 | furniture | pages [23] -->
m

<!-- b001537 | furniture | pages [23] -->
m

<!-- b001538 | furniture | pages [23] -->
m

<!-- b001539 | furniture | pages [23] -->
m

<!-- b001540 | furniture | pages [23] -->
m

<!-- b001541 | furniture | pages [23] -->
m

<!-- b001542 | furniture | pages [23] -->
m

<!-- b001543 | furniture | pages [23] -->
m

<!-- b001544 | furniture | pages [23] -->
m

<!-- b001545 | furniture | pages [23] -->
m

<!-- b001546 | furniture | pages [23] -->
m

<!-- b001547 | furniture | pages [23] -->
m

<!-- b001548 | furniture | pages [23] -->
m

<!-- b001549 | furniture | pages [23] -->
m

<!-- b001550 | furniture | pages [23] -->
m

<!-- b001551 | furniture | pages [23] -->
m

<!-- b001552 | furniture | pages [23] -->
m

<!-- b001553 | furniture | pages [23] -->
m

<!-- b001554 | furniture | pages [23] -->
m

<!-- b001555 | furniture | pages [23] -->
m

<!-- b001556 | furniture | pages [23] -->
m

<!-- b001557 | furniture | pages [23] -->
m

<!-- b001558 | furniture | pages [23] -->
m

<!-- b001559 | furniture | pages [23] -->
m

<!-- b001560 | furniture | pages [23] -->
m

<!-- b001561 | furniture | pages [23] -->
m

<!-- b001562 | furniture | pages [23] -->
m

<!-- b001563 | furniture | pages [23] -->
m

<!-- b001564 | furniture | pages [23] -->
m

<!-- b001565 | furniture | pages [23] -->
m

<!-- b001566 | furniture | pages [23] -->
m

<!-- b001567 | furniture | pages [23] -->
m

<!-- b001568 | furniture | pages [23] -->
m

<!-- b001569 | furniture | pages [23] -->
m

<!-- b001570 | furniture | pages [23] -->
m

<!-- b001571 | furniture | pages [23] -->
m

<!-- b001572 | furniture | pages [23] -->
m

<!-- b001573 | furniture | pages [23] -->
m

<!-- b001574 | furniture | pages [23] -->
m

<!-- b001575 | furniture | pages [23] -->
m

<!-- b001576 | furniture | pages [23] -->
m

<!-- b001577 | furniture | pages [23] -->
m

<!-- b001578 | furniture | pages [23] -->
m

<!-- b001579 | furniture | pages [23] -->
m

<!-- b001580 | furniture | pages [23] -->
m

<!-- b001581 | furniture | pages [23] -->
m

<!-- b001582 | furniture | pages [23] -->
m

<!-- b001583 | furniture | pages [23] -->
m

<!-- b001584 | furniture | pages [23] -->
m

<!-- b001585 | furniture | pages [23] -->
m

<!-- b001586 | furniture | pages [23] -->
m

<!-- b001587 | furniture | pages [23] -->
m

<!-- b001588 | furniture | pages [23] -->
m

<!-- b001589 | furniture | pages [23] -->
m

<!-- b001590 | furniture | pages [23] -->
m

<!-- b001591 | furniture | pages [23] -->
m

<!-- b001592 | furniture | pages [23] -->
m

<!-- b001593 | furniture | pages [23] -->
m

<!-- b001594 | furniture | pages [23] -->
m

<!-- b001595 | furniture | pages [23] -->
m

<!-- b001596 | furniture | pages [23] -->
m

<!-- b001597 | furniture | pages [23] -->
m

<!-- b001598 | furniture | pages [23] -->
m

<!-- b001599 | furniture | pages [23] -->
m

<!-- b001600 | furniture | pages [23] -->
m

<!-- b001601 | furniture | pages [23] -->
m

<!-- b001602 | furniture | pages [23] -->
m

<!-- b001603 | furniture | pages [23] -->
m

<!-- b001604 | furniture | pages [23] -->
m

<!-- b001605 | furniture | pages [23] -->
m

<!-- b001606 | furniture | pages [23] -->
m

<!-- b001607 | furniture | pages [23] -->
m

<!-- b001608 | furniture | pages [23] -->
m

<!-- b001609 | furniture | pages [23] -->
m

<!-- b001610 | furniture | pages [23] -->
m

<!-- b001611 | furniture | pages [23] -->
m

<!-- b001612 | furniture | pages [23] -->
m

<!-- b001613 | furniture | pages [23] -->
m

<!-- b001614 | furniture | pages [23] -->
m

<!-- b001615 | furniture | pages [23] -->
m

<!-- b001616 | furniture | pages [23] -->
m

<!-- b001617 | furniture | pages [23] -->
m

<!-- b001618 | furniture | pages [23] -->
m

<!-- b001619 | furniture | pages [23] -->
m

<!-- b001620 | furniture | pages [23] -->
m

<!-- b001621 | furniture | pages [23] -->
m

<!-- b001622 | furniture | pages [23] -->
m

<!-- b001623 | furniture | pages [23] -->
m

<!-- b001624 | furniture | pages [23] -->
m

<!-- b001625 | furniture | pages [23] -->
m

<!-- b001626 | furniture | pages [23] -->
m

<!-- b001627 | furniture | pages [23] -->
m

<!-- b001628 | furniture | pages [23] -->
m

<!-- b001629 | furniture | pages [23] -->
m

<!-- b001630 | furniture | pages [23] -->
m

<!-- b001631 | furniture | pages [23] -->
m

<!-- b001632 | furniture | pages [23] -->
m

<!-- b001633 | furniture | pages [23] -->
m

<!-- b001634 | furniture | pages [23] -->
m

<!-- b001635 | furniture | pages [23] -->
m

<!-- b001636 | furniture | pages [23] -->
m

<!-- b001637 | furniture | pages [23] -->
m

<!-- b001638 | furniture | pages [23] -->
m

<!-- b001639 | furniture | pages [23] -->
m

<!-- b001640 | furniture | pages [23] -->
m

<!-- b001641 | furniture | pages [23] -->
m

<!-- b001642 | furniture | pages [23] -->
m

<!-- b001643 | furniture | pages [23] -->
m

<!-- b001644 | furniture | pages [23] -->
m

<!-- b001645 | furniture | pages [23] -->
m

<!-- b001646 | furniture | pages [23] -->
m

<!-- b001647 | furniture | pages [23] -->
m

<!-- b001648 | furniture | pages [23] -->
m

<!-- b001649 | furniture | pages [23] -->
m

<!-- b001650 | furniture | pages [23] -->
m

<!-- b001651 | furniture | pages [23] -->
m

<!-- b001652 | furniture | pages [23] -->
m

<!-- b001653 | furniture | pages [23] -->
m

<!-- b001654 | furniture | pages [23] -->
m

<!-- b001655 | furniture | pages [23] -->
m

<!-- b001656 | furniture | pages [23] -->
m

<!-- b001657 | furniture | pages [23] -->
m

<!-- b001658 | furniture | pages [23] -->
m

<!-- b001659 | furniture | pages [23] -->
m

<!-- b001660 | furniture | pages [23] -->
m

<!-- b001661 | furniture | pages [23] -->
m

<!-- b001662 | furniture | pages [23] -->
m

<!-- b001663 | furniture | pages [23] -->
m

<!-- b001664 | furniture | pages [23] -->
m

<!-- b001665 | furniture | pages [23] -->
m

<!-- b001666 | furniture | pages [23] -->
m

<!-- b001667 | furniture | pages [23] -->
m

<!-- b001668 | furniture | pages [23] -->
m

<!-- b001669 | furniture | pages [23] -->
m

<!-- b001670 | furniture | pages [23] -->
m

<!-- b001671 | furniture | pages [23] -->
m

<!-- b001672 | furniture | pages [23] -->
m

<!-- b001673 | furniture | pages [23] -->
m

<!-- b001674 | furniture | pages [23] -->
m

<!-- b001675 | furniture | pages [23] -->
m

<!-- b001676 | furniture | pages [23] -->
m

<!-- b001677 | furniture | pages [23] -->
m

<!-- b001678 | furniture | pages [23] -->
m

<!-- b001679 | furniture | pages [23] -->
m

<!-- b001680 | furniture | pages [23] -->
m

<!-- b001681 | furniture | pages [23] -->
m

<!-- b001682 | furniture | pages [23] -->
m

<!-- b001683 | furniture | pages [23] -->
m

<!-- b001684 | furniture | pages [23] -->
m

<!-- b001685 | furniture | pages [23] -->
m

<!-- b001686 | furniture | pages [23] -->
m

<!-- b001687 | furniture | pages [23] -->
m

<!-- b001688 | furniture | pages [23] -->
m

<!-- b001689 | furniture | pages [23] -->
m

<!-- b001690 | furniture | pages [23] -->
m

<!-- b001691 | furniture | pages [23] -->
m

<!-- b001692 | furniture | pages [23] -->
m

<!-- b001693 | furniture | pages [23] -->
m

<!-- b001694 | furniture | pages [23] -->
m

<!-- b001695 | furniture | pages [23] -->
m

<!-- b001696 | furniture | pages [23] -->
m

<!-- b001697 | furniture | pages [23] -->
m

<!-- b001698 | furniture | pages [23] -->
m

<!-- b001699 | furniture | pages [23] -->
m

<!-- b001700 | furniture | pages [23] -->
m

<!-- b001701 | furniture | pages [23] -->
m

<!-- b001702 | furniture | pages [23] -->
m

<!-- b001703 | furniture | pages [23] -->
m

<!-- b001704 | furniture | pages [23] -->
m

<!-- b001705 | furniture | pages [23] -->
m

<!-- b001706 | furniture | pages [23] -->
m

<!-- b001707 | furniture | pages [23] -->
m

<!-- b001708 | furniture | pages [23] -->
m

<!-- b001709 | furniture | pages [23] -->
m

<!-- b001710 | furniture | pages [23] -->
m

<!-- b001711 | furniture | pages [23] -->
m

<!-- b001712 | furniture | pages [24] -->
Team#2507817                                                             Page 24 of 25

<!-- b001714 | heading | pages [24] -->
10.2 Impact of Athletes Number, Gold & Total Medals on Predicted Results

<!-- b001715 | prose | pages [24] -->
In Task 1, we found that there are many eigenvalues that affect the prediction of the number of gold medals & medals. We control the other eigenvalues unchanged, respectively change the athletes_num A , the total number of events E , observe the corresponding ij ij changes in the predicted number of medals won, and get the average sensitivity: athletes_num: 0.058329%; Total event: -1.2113%.

<!-- b001716 | prose | pages [24] -->
a) Total event b) Athletes number

<!-- b001717 | caption | pages [24] -->
Figure 23 Sentivity analysis

<!-- b001718 | prose | pages [24] -->
From the figure, it is found that the model basically does not fluctuate much after being perturbed, and the average sensitivity is also very low. It shows that our model has strong stability and robustness.

<!-- b001719 | heading | pages [24] -->
11 Evaluation of Model

<!-- b001720 | heading | pages [24] -->
(1) Strengths

<!-- b001721 | prose | pages [24] -->
 GSRF uses an optimal combination of hyperparameters on top of the traditional stochastic model to train and predict the model. It significantly improves the performance of the model and effectively mitigates problems such as overfitting or underfitting  Both the MAE and RMSE of the GSRF model are smaller, proving that the model is more accurate and predicts more credible results  The binary logistic regression model has a larger F1 metric, which ensures that the recall is also high while guaranteeing higher accuracy and better classification.

<!-- b001722 | prose | pages [24] -->
 By changing the eigenvalues of the model, it is found that the model basically does not fluctuate too much after being perturbed, indicating that the model has strong stability and robustness.

<!-- b001723 | heading | pages [24] -->
(2) Possible Improvements

<!-- b001724 | prose | pages [24] -->
 It is assumed that the number of athletes, countries and sports at the 2028 Olympics will be the same as in 2024, but the actual situation may change, which will affect the model's predictions.

<!-- b001725 | prose | pages [24] -->
 There may be interactions between variables, for example, there may be a positive correlation between the number of athletes and the number of programs, which can lead to biased model predictions.

<!-- b001726 | prose | pages [24] -->
关注数学模型

<!-- b001727 | furniture | pages [24] -->
2

<!-- b001728 | furniture | pages [24] -->
MATHmodels

<!-- b001729 | furniture | pages [24] -->
获取更多资讯

<!-- b001730 | furniture | pages [25] -->
Team#2507817                                                             Page 25 of 25

<!-- b001731 | heading | pages [25] -->
12 References

<!-- b001732 | references | pages [25] -->
[1] Christoph S ,L. S S ,Dominik S , et al. Forecasting the Olympic medal distribution - A

<!-- b001733 | references | pages [25] -->
socioeconomic machine learning model[J]. Technological Forecasting &amp; Social

<!-- b001734 | references | pages [25] -->
Change,2022,175

<!-- b001735 | references | pages [25] -->
[2] Tan Kaifeng, Zhang Qingyi. Analysis of World Sports Competition Pattern and China's

<!-- b001736 | references | pages [25] -->
微信公众号：数学模型

<!-- b001737 | references | pages [25] -->
Athletic

<!-- b001738 | references | pages [25] -->
Level

<!-- b001739 | references | pages [25] -->
in

<!-- b001740 | references | pages [25] -->
Paris

<!-- b001741 | references | pages [25] -->
Olympics

<!-- b001742 | references | pages [25] -->
[J].

<!-- b001743 | references | pages [25] -->
Liaoning

<!-- b001744 | references | pages [25] -->
Sports

<!-- b001745 | references | pages [25] -->
Science

<!-- b001746 | references | pages [25] -->
and

<!-- b001747 | references | pages [25] -->
Technology,2025,47(01):56-62.DOI:10.13940/j.cnki.lntykj.2025.01.023.

<!-- b001748 | references | pages [25] -->
[3] Coaching

<!-- b001749 | references | pages [25] -->
Team

<!-- b001750 | references | pages [25] -->
-

<!-- b001751 | references | pages [25] -->
Bela

<!-- b001752 | references | pages [25] -->
and

<!-- b001753 | references | pages [25] -->
Martha

<!-- b001754 | references | pages [25] -->
Karolyi,

<!-- b001755 | references | pages [25] -->
USA

<!-- b001756 | references | pages [25] -->
Gymnastic,

<!-- b001757 | references | pages [25] -->
https://usagym.org/halloffame/inductee/coaching-team-bela-martha- karolyi/

<!-- b001758 | references | pages [25] -->
[4] [Nov 16, 2024] Bela Karolyi, famed yet polarizing U.S. gymnastics coach, dies, ESPN

<!-- b001759 | references | pages [25] -->
News Services, https://www.espn.com/olympics/gymnastics/story /_/id/42433795/bela-

<!-- b001760 | references | pages [25] -->
karolyi-famed-us-gymnastics-coach-dies-82

<!-- b001761 | references | pages [25] -->
微信号：MATHmodels
