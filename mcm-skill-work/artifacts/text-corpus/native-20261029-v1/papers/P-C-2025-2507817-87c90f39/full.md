# P-C-2025-2507817-87c90f39

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2025

<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | furniture | pages [1] -->
2507817

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | prose | pages [1] -->
Olympic Medals Unveiled:

<!-- b000011 | prose | pages [1] -->
A Mathematical Exploration of Achievement Trends

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | title | pages [1] -->
微信公众号：数学模型

<!-- b000014 | prose | pages [1] -->
In the Olympic Games, the pinnacle of sports competition, the quest for medals reflects not only the physical prowess of athletes but also the overall strength of their countries. As competitive sports evolve, medal rankings shift over time. This paper analyzes the key factors influencing Olympic performance and explores future trends in the medal competition landscape from various perspectives.

<!-- b000015 | prose | pages [1] -->
For Task 1, we developed a Grid-Search Random Forest (GSRF) prediction model

<!-- b000016 | heading | pages [1] -->
using preprocessed data. Through Cross-Validation, we obtained correlation coefficients for

<!-- b000017 | prose | pages [1] -->
predicting the number of gold medals and the total medals, which were 0.710 and 0.784, respectively, validating the model. Based on this model, we projected the gold and total medal standings for the 2028 Olympic Games, concluding that China and the United States are likely

<!-- b000018 | title | pages [1] -->
微信号：MATHmodels

<!-- b000019 | prose | pages [1] -->
to continue leading in both categories. We also calculated prediction intervals using the t- distribution, as shown in Figure 9. Additionally, we identified the countries most likely to advance and regress, which are illustrated in Figure 10.

<!-- b000020 | prose | pages [1] -->
For Task 2, we established a Logistic Regression Model to classify countries that have not yet won medals in the 2028 Olympic Games into two categories: winners and non-winners. This transformed the probability of winning a medal into a binary classification problem. We selected appropriate feature variables and calculated the weights of each feature vector using the maximum likelihood estimation method. By applying the sigmoid function and L1 regularization, we identified countries with a higher likelihood of winning medals among those yet to medal, as shown in Table 11.

<!-- b000021 | prose | pages [1] -->
For Task 3, based on the results of Task 1, we calculated the number of medals won by each country in each event and quantified the significance of each event’s contributions by calculating the ratio of medals in that event to total medals. We noted that some countries (e.g., KOS in Judo) have achieved their only medals through specific programs that are particularly critical for them. Overall, countries tend to prioritize sports in which they have both strengths and potential to optimize their chances of winning more medals.

<!-- b000022 | prose | pages [1] -->
For Task 4, we created a “Great Coach” Model. By quantifying the weights of medals and calculating the scores of each country, we identified that there were “Great Coach” in women's gymnastics in Romania and the United States, and the Spearman's Correlation Coefficient between their scores and the scores of these two countries was 0.874. After building the model by using the Lasso Regression, we selected three countries and identify sports and applied it to them. After the introduction of the “Great Coach” concept, the predicted scores for each country in 2028 are presented in Table 15, with Romania showing a remarkable increase from a score of 3 to 36.65.

<!-- b000023 | prose | pages [1] -->
Finally, we offer original insights for the IOC regarding the host effect and the impact of

<!-- b000024 | heading | pages [1] -->
talented athletes. Additionally, we performed a sensitivity analysis that demonstrated the

<!-- b000025 | prose | pages [1] -->
model's stability and robustness following perturbations.

<!-- b000026 | keywords | pages [1] -->
Keywords: Olympic；GSRF；Logistic Regression；Lasso Regression

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [3] -->
Team#2507817                                                             Page 3 of 25

<!-- b000029 | heading | pages [3] -->
1 Introduction

<!-- b000030 | heading | pages [3] -->
1.1 Background

<!-- b000031 | prose | pages [3] -->
When viewers follow the Summer Olympics, they appreciate the performance of the athletes as well as the medal standings. Since 1896, sports powerhouses such as the United

<!-- b000032 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000033 | prose | pages [3] -->
States have been at the top of the list, demonstrating their strength. Countries that have won many gold medals are globally recognized, and countries that have won their first Olympic medals are celebrated, marking historical milestones. Here are the top 10 medalists for the 2024 Summer Olympics:

<!-- b000034 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000035 | furniture | pages [3] -->


<!-- b000036 | caption | pages [3] -->
Figure 1 Medal list of 2024 Summer Olympic Games

<!-- b000037 | heading | pages [3] -->
1.2 Clarifications and Restatements

<!-- b000038 | prose | pages [3] -->
In this problem, models need to be developed to predict the medal table using relevant event and athlete data. Based on the data of previous years' Summer Olympics medal table, host country, number of events and participants, the analysis deals with the following problems:

<!-- b000039 | prose | pages [3] -->
Task 1 Predicts the medal standings for the 2028 Summer Olympics based on a model, giving

<!-- b000040 | prose | pages [3] -->
prediction intervals that include each statistic, indicating the countries most likely to make progress and regress.

<!-- b000041 | prose | pages [3] -->
 The feature values affecting the number of medals are counted and integrated into a

<!-- b000042 | prose | pages [3] -->
dataset for model training and testing. After model validation, predict the number of gold medals and total medals for each country in 2028 based on 2024 data, calculate prediction intervals and visualize them.

<!-- b000043 | prose | pages [3] -->
Task 2 For countries that have not yet won a medal, predict how many countries will win their

<!-- b000044 | prose | pages [3] -->
first medal at the next Olympic Games and calculate their probability

<!-- b000045 | prose | pages [3] -->
 Essentially, it is a classification problem that categorizes the predicted outcomes of

<!-- b000046 | prose | pages [3] -->
non-winning countries in 2028 into two categories: winning and not winning. Judgment calculates how probable it is that the country falls into the winning category.

<!-- b000047 | prose | pages [3] -->
Task 3 Consider the effect of the number and type of sports in previous Olympic Games on

<!-- b000048 | prose | pages [3] -->
the number of medals won by each country. Determine the most important sport for each country and give reasons. Also consider the effect of the host country's choice of sport on the results.

<!-- b000049 | prose | pages [3] -->
 We sort out the cumulative number of medals for each country and analyze the

<!-- b000050 | prose | pages [3] -->
relationship. Also introduce a concept that can quantify the importance of the program to the country. Use the data to make judgments and explain why.

<!-- b000051 | prose | pages [3] -->
Task 4 Predict the contribution of the "great coach" effect to the number of medals. Select

<!-- b000052 | prose | pages [3] -->
m

<!-- b000053 | prose | pages [3] -->
m

<!-- b000054 | prose | pages [3] -->
m

<!-- b000055 | prose | pages [3] -->
m

<!-- b000056 | prose | pages [3] -->
m

<!-- b000057 | prose | pages [3] -->
m

<!-- b000058 | prose | pages [3] -->
m

<!-- b000059 | prose | pages [3] -->
m

<!-- b000060 | prose | pages [3] -->
m

<!-- b000061 | prose | pages [3] -->
m

<!-- b000062 | prose | pages [3] -->
m

<!-- b000063 | prose | pages [3] -->
m

<!-- b000064 | prose | pages [3] -->
m

<!-- b000065 | prose | pages [3] -->
m

<!-- b000066 | prose | pages [3] -->
m

<!-- b000067 | prose | pages [3] -->
m

<!-- b000068 | prose | pages [3] -->
m

<!-- b000069 | prose | pages [3] -->
m

<!-- b000070 | prose | pages [3] -->
m

<!-- b000071 | prose | pages [3] -->
m

<!-- b000072 | prose | pages [3] -->
m

<!-- b000073 | prose | pages [3] -->
m

<!-- b000074 | prose | pages [3] -->
m

<!-- b000075 | prose | pages [3] -->
m

<!-- b000076 | prose | pages [3] -->
m

<!-- b000077 | prose | pages [3] -->
m

<!-- b000078 | prose | pages [3] -->
m

<!-- b000079 | prose | pages [3] -->
m

<!-- b000080 | prose | pages [3] -->
m

<!-- b000081 | prose | pages [3] -->
m

<!-- b000082 | prose | pages [3] -->
m

<!-- b000083 | prose | pages [3] -->
m

<!-- b000084 | prose | pages [3] -->
m

<!-- b000085 | prose | pages [3] -->
m

<!-- b000086 | prose | pages [3] -->
m

<!-- b000087 | prose | pages [3] -->
m

<!-- b000088 | prose | pages [3] -->
m

<!-- b000089 | prose | pages [3] -->
m

<!-- b000090 | prose | pages [3] -->
m

<!-- b000091 | prose | pages [3] -->
m

<!-- b000092 | prose | pages [3] -->
m

<!-- b000093 | prose | pages [3] -->
m

<!-- b000094 | prose | pages [3] -->
m

<!-- b000095 | prose | pages [3] -->
m

<!-- b000096 | prose | pages [3] -->
m

<!-- b000097 | prose | pages [3] -->
m

<!-- b000098 | prose | pages [3] -->
m

<!-- b000099 | prose | pages [3] -->
m

<!-- b000100 | prose | pages [3] -->
m

<!-- b000101 | prose | pages [3] -->
m

<!-- b000102 | prose | pages [3] -->
m

<!-- b000103 | prose | pages [3] -->
m

<!-- b000104 | prose | pages [3] -->
m

<!-- b000105 | prose | pages [3] -->
m

<!-- b000106 | prose | pages [3] -->
m

<!-- b000107 | prose | pages [3] -->
m

<!-- b000108 | prose | pages [3] -->
m

<!-- b000109 | prose | pages [3] -->
m

<!-- b000110 | prose | pages [3] -->
m

<!-- b000111 | prose | pages [3] -->
m

<!-- b000112 | prose | pages [3] -->
m

<!-- b000113 | prose | pages [3] -->
m

<!-- b000114 | prose | pages [3] -->
m

<!-- b000115 | prose | pages [3] -->
m

<!-- b000116 | prose | pages [3] -->
m

<!-- b000117 | prose | pages [3] -->
m

<!-- b000118 | prose | pages [3] -->
m

<!-- b000119 | prose | pages [3] -->
m

<!-- b000120 | prose | pages [3] -->
m

<!-- b000121 | prose | pages [3] -->
m

<!-- b000122 | prose | pages [3] -->
m

<!-- b000123 | prose | pages [3] -->
m

<!-- b000124 | prose | pages [3] -->
m

<!-- b000125 | prose | pages [3] -->
m

<!-- b000126 | prose | pages [3] -->
m

<!-- b000127 | prose | pages [3] -->
m

<!-- b000128 | prose | pages [3] -->
m

<!-- b000129 | prose | pages [3] -->
m

<!-- b000130 | prose | pages [3] -->
m

<!-- b000131 | prose | pages [3] -->
m

<!-- b000132 | prose | pages [3] -->
m

<!-- b000133 | prose | pages [3] -->
m

<!-- b000134 | prose | pages [3] -->
m

<!-- b000135 | prose | pages [3] -->
m

<!-- b000136 | prose | pages [3] -->
m

<!-- b000137 | prose | pages [3] -->
m

<!-- b000138 | prose | pages [3] -->
m

<!-- b000139 | prose | pages [3] -->
m

<!-- b000140 | prose | pages [3] -->
m

<!-- b000141 | prose | pages [3] -->
m

<!-- b000142 | prose | pages [3] -->
m

<!-- b000143 | prose | pages [3] -->
m

<!-- b000144 | prose | pages [3] -->
m

<!-- b000145 | prose | pages [3] -->
m

<!-- b000146 | prose | pages [3] -->
m

<!-- b000147 | prose | pages [3] -->
m

<!-- b000148 | prose | pages [3] -->
m

<!-- b000149 | prose | pages [3] -->
m

<!-- b000150 | prose | pages [3] -->
m

<!-- b000151 | prose | pages [3] -->
m

<!-- b000152 | prose | pages [3] -->
m

<!-- b000153 | prose | pages [3] -->
m

<!-- b000154 | prose | pages [3] -->
m

<!-- b000155 | prose | pages [3] -->
m

<!-- b000156 | prose | pages [3] -->
m

<!-- b000157 | prose | pages [3] -->
m

<!-- b000158 | prose | pages [3] -->
m

<!-- b000159 | prose | pages [3] -->
m

<!-- b000160 | prose | pages [3] -->
m

<!-- b000161 | prose | pages [3] -->
m

<!-- b000162 | prose | pages [3] -->
m

<!-- b000163 | prose | pages [3] -->
m

<!-- b000164 | prose | pages [3] -->
m

<!-- b000165 | prose | pages [3] -->
m

<!-- b000166 | prose | pages [3] -->
m

<!-- b000167 | prose | pages [3] -->
m

<!-- b000168 | prose | pages [3] -->
m

<!-- b000169 | prose | pages [3] -->
m

<!-- b000170 | prose | pages [3] -->
m

<!-- b000171 | prose | pages [3] -->
m

<!-- b000172 | prose | pages [3] -->
m

<!-- b000173 | prose | pages [3] -->
m

<!-- b000174 | prose | pages [3] -->
m

<!-- b000175 | prose | pages [3] -->
m

<!-- b000176 | prose | pages [3] -->
m

<!-- b000177 | prose | pages [3] -->
m

<!-- b000178 | prose | pages [3] -->
m

<!-- b000179 | prose | pages [3] -->
m

<!-- b000180 | prose | pages [3] -->
m

<!-- b000181 | prose | pages [3] -->
m

<!-- b000182 | furniture | pages [3] -->


<!-- b000183 | prose | pages [3] -->
m

<!-- b000184 | prose | pages [3] -->
m

<!-- b000185 | prose | pages [3] -->
m

<!-- b000186 | prose | pages [3] -->
m

<!-- b000187 | prose | pages [3] -->
m

<!-- b000188 | prose | pages [3] -->
m

<!-- b000189 | prose | pages [3] -->
m

<!-- b000190 | prose | pages [3] -->
m

<!-- b000191 | prose | pages [3] -->
m

<!-- b000192 | prose | pages [3] -->
m

<!-- b000193 | prose | pages [3] -->
m

<!-- b000194 | prose | pages [3] -->
m

<!-- b000195 | prose | pages [3] -->
m

<!-- b000196 | prose | pages [3] -->
m

<!-- b000197 | prose | pages [3] -->
m

<!-- b000198 | prose | pages [3] -->
m

<!-- b000199 | prose | pages [3] -->
m

<!-- b000200 | prose | pages [3] -->
m

<!-- b000201 | prose | pages [3] -->
m

<!-- b000202 | prose | pages [3] -->
m

<!-- b000203 | prose | pages [3] -->
m

<!-- b000204 | prose | pages [3] -->
m

<!-- b000205 | prose | pages [3] -->
m

<!-- b000206 | prose | pages [3] -->
m

<!-- b000207 | prose | pages [3] -->
m

<!-- b000208 | prose | pages [3] -->
m

<!-- b000209 | prose | pages [3] -->
m

<!-- b000210 | prose | pages [3] -->
m

<!-- b000211 | prose | pages [3] -->
m

<!-- b000212 | prose | pages [3] -->
m

<!-- b000213 | prose | pages [3] -->
m

<!-- b000214 | prose | pages [3] -->
m

<!-- b000215 | prose | pages [3] -->
m

<!-- b000216 | prose | pages [3] -->
m

<!-- b000217 | prose | pages [3] -->
m

<!-- b000218 | prose | pages [3] -->
m

<!-- b000219 | prose | pages [3] -->
m

<!-- b000220 | prose | pages [3] -->
m

<!-- b000221 | prose | pages [3] -->
m

<!-- b000222 | prose | pages [3] -->
m

<!-- b000223 | prose | pages [3] -->
m

<!-- b000224 | prose | pages [3] -->
m

<!-- b000225 | prose | pages [3] -->
m

<!-- b000226 | prose | pages [3] -->
m

<!-- b000227 | prose | pages [3] -->
m

<!-- b000228 | prose | pages [3] -->
m

<!-- b000229 | prose | pages [3] -->
m

<!-- b000230 | prose | pages [3] -->
m

<!-- b000231 | prose | pages [3] -->
m

<!-- b000232 | prose | pages [3] -->
m

<!-- b000233 | prose | pages [3] -->
m

<!-- b000234 | prose | pages [3] -->
m

<!-- b000235 | prose | pages [3] -->
m

<!-- b000236 | prose | pages [3] -->
m

<!-- b000237 | prose | pages [3] -->
m

<!-- b000238 | prose | pages [3] -->
m

<!-- b000239 | prose | pages [3] -->
m

<!-- b000240 | prose | pages [3] -->
m

<!-- b000241 | prose | pages [3] -->
m

<!-- b000242 | prose | pages [3] -->
m

<!-- b000243 | prose | pages [3] -->
m

<!-- b000244 | prose | pages [3] -->
m

<!-- b000245 | prose | pages [3] -->
m

<!-- b000246 | prose | pages [3] -->
m

<!-- b000247 | prose | pages [3] -->
m

<!-- b000248 | prose | pages [3] -->
m

<!-- b000249 | prose | pages [3] -->
m

<!-- b000250 | prose | pages [3] -->
m

<!-- b000251 | prose | pages [3] -->
m

<!-- b000252 | prose | pages [3] -->
m

<!-- b000253 | prose | pages [3] -->
m

<!-- b000254 | prose | pages [3] -->
m

<!-- b000255 | prose | pages [3] -->
m

<!-- b000256 | prose | pages [3] -->
m

<!-- b000257 | prose | pages [3] -->
m

<!-- b000258 | prose | pages [3] -->
m

<!-- b000259 | prose | pages [3] -->
m

<!-- b000260 | prose | pages [3] -->
m

<!-- b000261 | prose | pages [3] -->
m

<!-- b000262 | prose | pages [3] -->
m

<!-- b000263 | prose | pages [3] -->
m

<!-- b000264 | prose | pages [3] -->
m

<!-- b000265 | prose | pages [3] -->
m

<!-- b000266 | prose | pages [3] -->
m

<!-- b000267 | prose | pages [3] -->
m

<!-- b000268 | prose | pages [3] -->
m

<!-- b000269 | prose | pages [3] -->
m

<!-- b000270 | prose | pages [3] -->
m

<!-- b000271 | prose | pages [3] -->
m

<!-- b000272 | prose | pages [3] -->
m

<!-- b000273 | prose | pages [3] -->
m

<!-- b000274 | prose | pages [3] -->
m

<!-- b000275 | prose | pages [3] -->
m

<!-- b000276 | prose | pages [3] -->
m

<!-- b000277 | prose | pages [3] -->
m

<!-- b000278 | prose | pages [3] -->
m

<!-- b000279 | prose | pages [3] -->
m

<!-- b000280 | prose | pages [3] -->
m

<!-- b000281 | prose | pages [3] -->
m

<!-- b000282 | prose | pages [3] -->
m

<!-- b000283 | prose | pages [3] -->
m

<!-- b000284 | prose | pages [3] -->
m

<!-- b000285 | prose | pages [3] -->
m

<!-- b000286 | prose | pages [3] -->
m

<!-- b000287 | prose | pages [3] -->
m

<!-- b000288 | prose | pages [3] -->
m

<!-- b000289 | prose | pages [3] -->
m

<!-- b000290 | prose | pages [3] -->
m

<!-- b000291 | prose | pages [3] -->
m

<!-- b000292 | prose | pages [3] -->
m

<!-- b000293 | prose | pages [3] -->
m

<!-- b000294 | prose | pages [3] -->
m

<!-- b000295 | prose | pages [3] -->
m

<!-- b000296 | prose | pages [3] -->
m

<!-- b000297 | prose | pages [3] -->
m

<!-- b000298 | prose | pages [3] -->
m

<!-- b000299 | prose | pages [3] -->
m

<!-- b000300 | prose | pages [3] -->
m

<!-- b000301 | prose | pages [3] -->
m

<!-- b000302 | prose | pages [3] -->
m

<!-- b000303 | prose | pages [3] -->
m

<!-- b000304 | prose | pages [3] -->
m

<!-- b000305 | prose | pages [3] -->
m

<!-- b000306 | prose | pages [3] -->
m

<!-- b000307 | prose | pages [3] -->
m

<!-- b000308 | prose | pages [3] -->
m

<!-- b000309 | prose | pages [3] -->
m

<!-- b000310 | prose | pages [3] -->
m

<!-- b000311 | prose | pages [3] -->
m

<!-- b000312 | prose | pages [3] -->
m

<!-- b000313 | prose | pages [3] -->
m

<!-- b000314 | prose | pages [3] -->
m

<!-- b000315 | prose | pages [3] -->
m

<!-- b000316 | prose | pages [3] -->
m

<!-- b000317 | prose | pages [3] -->
m

<!-- b000318 | prose | pages [3] -->
m

<!-- b000319 | prose | pages [3] -->
m

<!-- b000320 | prose | pages [3] -->
m

<!-- b000321 | prose | pages [3] -->
m

<!-- b000322 | prose | pages [3] -->
m

<!-- b000323 | prose | pages [3] -->
m

<!-- b000324 | prose | pages [3] -->
m

<!-- b000325 | prose | pages [3] -->
m

<!-- b000326 | prose | pages [3] -->
m

<!-- b000327 | prose | pages [3] -->
m

<!-- b000328 | prose | pages [3] -->
m

<!-- b000329 | prose | pages [3] -->
m

<!-- b000330 | prose | pages [3] -->
m

<!-- b000331 | prose | pages [3] -->
m

<!-- b000332 | prose | pages [3] -->
m

<!-- b000333 | prose | pages [3] -->
m

<!-- b000334 | prose | pages [3] -->
m

<!-- b000335 | prose | pages [3] -->
m

<!-- b000336 | prose | pages [3] -->
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

<!-- b000400 | furniture | pages [3] -->
m

<!-- b000401 | furniture | pages [3] -->
m

<!-- b000402 | furniture | pages [3] -->
m

<!-- b000403 | furniture | pages [3] -->
m

<!-- b000404 | furniture | pages [3] -->
m

<!-- b000405 | furniture | pages [3] -->
m

<!-- b000406 | furniture | pages [3] -->
m

<!-- b000407 | furniture | pages [3] -->
m

<!-- b000408 | furniture | pages [3] -->
m

<!-- b000409 | furniture | pages [3] -->
m

<!-- b000410 | furniture | pages [3] -->
m

<!-- b000411 | furniture | pages [3] -->
m

<!-- b000412 | furniture | pages [3] -->
m

<!-- b000413 | furniture | pages [3] -->
m

<!-- b000414 | furniture | pages [3] -->
m

<!-- b000415 | furniture | pages [3] -->
m

<!-- b000416 | furniture | pages [3] -->
m

<!-- b000417 | furniture | pages [3] -->
m

<!-- b000418 | furniture | pages [3] -->
m

<!-- b000419 | furniture | pages [3] -->
m

<!-- b000420 | furniture | pages [3] -->
m

<!-- b000421 | furniture | pages [3] -->
m

<!-- b000422 | furniture | pages [3] -->
m

<!-- b000423 | furniture | pages [3] -->
m

<!-- b000424 | furniture | pages [3] -->
m

<!-- b000425 | furniture | pages [3] -->
m

<!-- b000426 | furniture | pages [3] -->
m

<!-- b000427 | furniture | pages [3] -->
m

<!-- b000428 | furniture | pages [3] -->
m

<!-- b000429 | furniture | pages [3] -->
m

<!-- b000430 | furniture | pages [3] -->
m

<!-- b000431 | furniture | pages [3] -->
m

<!-- b000432 | furniture | pages [3] -->
m

<!-- b000433 | furniture | pages [3] -->
m

<!-- b000434 | furniture | pages [3] -->
m

<!-- b000435 | furniture | pages [3] -->
m

<!-- b000436 | furniture | pages [3] -->
m

<!-- b000437 | furniture | pages [3] -->
m

<!-- b000438 | furniture | pages [3] -->
m

<!-- b000439 | furniture | pages [3] -->
m

<!-- b000440 | furniture | pages [3] -->
m

<!-- b000441 | furniture | pages [3] -->
m

<!-- b000442 | furniture | pages [3] -->
m

<!-- b000443 | furniture | pages [3] -->
m

<!-- b000444 | furniture | pages [3] -->
m

<!-- b000445 | furniture | pages [3] -->
m

<!-- b000446 | furniture | pages [3] -->
m

<!-- b000447 | furniture | pages [3] -->
m

<!-- b000448 | furniture | pages [3] -->
m

<!-- b000449 | furniture | pages [3] -->
m

<!-- b000450 | furniture | pages [3] -->
m

<!-- b000451 | furniture | pages [3] -->
m

<!-- b000452 | furniture | pages [3] -->
m

<!-- b000453 | furniture | pages [3] -->
m

<!-- b000454 | furniture | pages [3] -->
m

<!-- b000455 | furniture | pages [3] -->
m

<!-- b000456 | furniture | pages [3] -->
m

<!-- b000457 | furniture | pages [3] -->
m

<!-- b000458 | furniture | pages [3] -->
m

<!-- b000459 | furniture | pages [3] -->
m

<!-- b000460 | furniture | pages [3] -->
m

<!-- b000461 | furniture | pages [3] -->
m

<!-- b000462 | furniture | pages [3] -->
m

<!-- b000463 | furniture | pages [3] -->
m

<!-- b000464 | furniture | pages [3] -->
m

<!-- b000465 | furniture | pages [3] -->
m

<!-- b000466 | furniture | pages [3] -->
m

<!-- b000467 | furniture | pages [3] -->
m

<!-- b000468 | furniture | pages [3] -->
m

<!-- b000469 | furniture | pages [3] -->
m

<!-- b000470 | furniture | pages [3] -->
m

<!-- b000471 | furniture | pages [3] -->
m

<!-- b000472 | furniture | pages [3] -->
m

<!-- b000473 | furniture | pages [3] -->
m

<!-- b000474 | furniture | pages [3] -->
m

<!-- b000475 | furniture | pages [3] -->
m

<!-- b000476 | furniture | pages [3] -->
m

<!-- b000477 | furniture | pages [3] -->
m

<!-- b000478 | furniture | pages [3] -->
m

<!-- b000479 | furniture | pages [3] -->
m

<!-- b000480 | furniture | pages [3] -->
m

<!-- b000481 | furniture | pages [3] -->
m

<!-- b000482 | furniture | pages [3] -->
m

<!-- b000483 | furniture | pages [3] -->
m

<!-- b000484 | furniture | pages [3] -->
m

<!-- b000485 | furniture | pages [3] -->
m

<!-- b000486 | furniture | pages [3] -->
m

<!-- b000487 | furniture | pages [3] -->
m

<!-- b000488 | furniture | pages [3] -->
m

<!-- b000489 | furniture | pages [3] -->
m

<!-- b000490 | furniture | pages [3] -->
m

<!-- b000491 | furniture | pages [3] -->
m

<!-- b000492 | furniture | pages [3] -->
m

<!-- b000493 | furniture | pages [3] -->
m

<!-- b000494 | furniture | pages [3] -->
m

<!-- b000495 | furniture | pages [3] -->
m

<!-- b000496 | furniture | pages [3] -->
m

<!-- b000497 | furniture | pages [3] -->
m

<!-- b000498 | furniture | pages [3] -->
m

<!-- b000499 | furniture | pages [3] -->
m

<!-- b000500 | furniture | pages [3] -->
m

<!-- b000501 | furniture | pages [3] -->
m

<!-- b000502 | furniture | pages [3] -->
m

<!-- b000503 | furniture | pages [3] -->
m

<!-- b000504 | furniture | pages [3] -->
m

<!-- b000505 | furniture | pages [3] -->
m

<!-- b000506 | furniture | pages [3] -->
m

<!-- b000507 | furniture | pages [3] -->
m

<!-- b000508 | furniture | pages [3] -->
m

<!-- b000509 | furniture | pages [3] -->
m

<!-- b000510 | furniture | pages [3] -->
m

<!-- b000511 | furniture | pages [3] -->
m

<!-- b000512 | furniture | pages [3] -->
m

<!-- b000513 | furniture | pages [3] -->
m

<!-- b000514 | furniture | pages [3] -->
m

<!-- b000515 | furniture | pages [3] -->
m

<!-- b000516 | furniture | pages [3] -->
m

<!-- b000517 | furniture | pages [3] -->
m

<!-- b000518 | furniture | pages [3] -->
m

<!-- b000519 | furniture | pages [3] -->
m

<!-- b000520 | furniture | pages [3] -->
m

<!-- b000521 | furniture | pages [3] -->
m

<!-- b000522 | furniture | pages [3] -->
m

<!-- b000523 | furniture | pages [3] -->
m

<!-- b000524 | furniture | pages [3] -->
m

<!-- b000525 | furniture | pages [3] -->
m

<!-- b000526 | furniture | pages [3] -->
m

<!-- b000527 | furniture | pages [3] -->
m

<!-- b000528 | furniture | pages [3] -->
m

<!-- b000529 | furniture | pages [3] -->
m

<!-- b000530 | furniture | pages [3] -->
m

<!-- b000531 | furniture | pages [3] -->
m

<!-- b000532 | furniture | pages [3] -->
m

<!-- b000533 | furniture | pages [3] -->
m

<!-- b000534 | furniture | pages [3] -->
m

<!-- b000535 | furniture | pages [3] -->
m

<!-- b000536 | furniture | pages [3] -->
m

<!-- b000537 | furniture | pages [3] -->
m

<!-- b000538 | furniture | pages [3] -->
m

<!-- b000539 | furniture | pages [3] -->
m

<!-- b000540 | furniture | pages [3] -->
m

<!-- b000541 | furniture | pages [3] -->
m

<!-- b000542 | furniture | pages [3] -->
m

<!-- b000543 | furniture | pages [3] -->
m

<!-- b000544 | furniture | pages [3] -->
m

<!-- b000545 | furniture | pages [3] -->
m

<!-- b000546 | furniture | pages [3] -->
m

<!-- b000547 | furniture | pages [3] -->
m

<!-- b000548 | furniture | pages [3] -->
m

<!-- b000549 | furniture | pages [3] -->
m

<!-- b000550 | furniture | pages [3] -->
m

<!-- b000551 | furniture | pages [3] -->
m

<!-- b000552 | furniture | pages [3] -->
m

<!-- b000553 | furniture | pages [3] -->
m

<!-- b000554 | furniture | pages [3] -->
m

<!-- b000555 | furniture | pages [3] -->
m

<!-- b000556 | furniture | pages [3] -->
m

<!-- b000557 | furniture | pages [3] -->
m

<!-- b000558 | furniture | pages [3] -->
m

<!-- b000559 | furniture | pages [3] -->
m

<!-- b000560 | furniture | pages [3] -->
m

<!-- b000561 | furniture | pages [3] -->
m

<!-- b000562 | furniture | pages [3] -->
m

<!-- b000563 | furniture | pages [3] -->
m

<!-- b000564 | furniture | pages [3] -->
m

<!-- b000565 | furniture | pages [3] -->
m

<!-- b000566 | furniture | pages [3] -->
m

<!-- b000567 | furniture | pages [3] -->
m

<!-- b000568 | furniture | pages [3] -->
m

<!-- b000569 | furniture | pages [3] -->
m

<!-- b000570 | furniture | pages [3] -->
m

<!-- b000571 | furniture | pages [3] -->
m

<!-- b000572 | furniture | pages [3] -->
m

<!-- b000573 | furniture | pages [3] -->
m

<!-- b000574 | furniture | pages [3] -->
m

<!-- b000575 | furniture | pages [3] -->
m

<!-- b000576 | furniture | pages [3] -->
m

<!-- b000577 | furniture | pages [3] -->
m

<!-- b000578 | furniture | pages [3] -->
m

<!-- b000579 | furniture | pages [3] -->
m

<!-- b000580 | furniture | pages [3] -->
m

<!-- b000581 | furniture | pages [3] -->
m

<!-- b000582 | furniture | pages [3] -->
m

<!-- b000583 | furniture | pages [3] -->
m

<!-- b000584 | furniture | pages [3] -->
m

<!-- b000585 | furniture | pages [3] -->
m

<!-- b000586 | furniture | pages [3] -->
m

<!-- b000587 | furniture | pages [3] -->
m

<!-- b000588 | furniture | pages [3] -->
m

<!-- b000589 | furniture | pages [3] -->
m

<!-- b000590 | furniture | pages [3] -->
m

<!-- b000591 | furniture | pages [3] -->
m

<!-- b000592 | furniture | pages [3] -->
m

<!-- b000593 | furniture | pages [3] -->
m

<!-- b000594 | furniture | pages [3] -->
m

<!-- b000595 | furniture | pages [3] -->
m

<!-- b000596 | furniture | pages [3] -->
m

<!-- b000597 | furniture | pages [3] -->
m

<!-- b000598 | furniture | pages [3] -->
m

<!-- b000599 | furniture | pages [3] -->
m

<!-- b000600 | furniture | pages [3] -->
m

<!-- b000601 | furniture | pages [3] -->
m

<!-- b000602 | furniture | pages [3] -->
m

<!-- b000603 | furniture | pages [3] -->
m

<!-- b000604 | furniture | pages [3] -->
m

<!-- b000605 | furniture | pages [3] -->
m

<!-- b000606 | furniture | pages [3] -->
m

<!-- b000607 | furniture | pages [3] -->
m

<!-- b000608 | furniture | pages [3] -->
m

<!-- b000609 | furniture | pages [3] -->
m

<!-- b000610 | furniture | pages [3] -->
m

<!-- b000611 | furniture | pages [3] -->
m

<!-- b000612 | furniture | pages [3] -->
m

<!-- b000613 | furniture | pages [3] -->
m

<!-- b000614 | furniture | pages [3] -->
m

<!-- b000615 | furniture | pages [3] -->
m

<!-- b000616 | furniture | pages [3] -->
m

<!-- b000617 | furniture | pages [3] -->
m

<!-- b000618 | furniture | pages [3] -->
m

<!-- b000619 | furniture | pages [3] -->
m

<!-- b000620 | furniture | pages [3] -->
m

<!-- b000621 | furniture | pages [3] -->
m

<!-- b000622 | furniture | pages [3] -->
m

<!-- b000623 | furniture | pages [3] -->
m

<!-- b000624 | furniture | pages [3] -->
m

<!-- b000625 | furniture | pages [3] -->
m

<!-- b000626 | furniture | pages [3] -->
m

<!-- b000627 | furniture | pages [3] -->
m

<!-- b000628 | furniture | pages [3] -->
m

<!-- b000629 | furniture | pages [3] -->
m

<!-- b000630 | furniture | pages [3] -->
m

<!-- b000631 | furniture | pages [3] -->
m

<!-- b000632 | furniture | pages [3] -->
m

<!-- b000633 | furniture | pages [3] -->
m

<!-- b000634 | furniture | pages [3] -->
m

<!-- b000635 | furniture | pages [3] -->
m

<!-- b000636 | furniture | pages [3] -->
m

<!-- b000637 | furniture | pages [3] -->
m

<!-- b000638 | furniture | pages [3] -->
m

<!-- b000639 | furniture | pages [3] -->
m

<!-- b000640 | furniture | pages [3] -->
m

<!-- b000641 | furniture | pages [3] -->
m

<!-- b000642 | furniture | pages [3] -->
m

<!-- b000643 | furniture | pages [3] -->
m

<!-- b000644 | furniture | pages [3] -->
m

<!-- b000645 | furniture | pages [3] -->
m

<!-- b000646 | furniture | pages [3] -->
m

<!-- b000647 | furniture | pages [3] -->
m

<!-- b000648 | furniture | pages [3] -->
m

<!-- b000649 | furniture | pages [3] -->
m

<!-- b000650 | furniture | pages [3] -->
m

<!-- b000651 | furniture | pages [3] -->
m

<!-- b000652 | furniture | pages [3] -->
m

<!-- b000653 | furniture | pages [3] -->
m

<!-- b000654 | furniture | pages [3] -->
m

<!-- b000655 | furniture | pages [3] -->
m

<!-- b000656 | furniture | pages [3] -->
m

<!-- b000657 | furniture | pages [3] -->
m

<!-- b000658 | furniture | pages [3] -->
m

<!-- b000659 | furniture | pages [3] -->
m

<!-- b000660 | furniture | pages [3] -->
m

<!-- b000661 | furniture | pages [3] -->
m

<!-- b000662 | furniture | pages [3] -->
m

<!-- b000663 | furniture | pages [3] -->
m

<!-- b000664 | furniture | pages [3] -->
m

<!-- b000665 | furniture | pages [3] -->
m

<!-- b000666 | furniture | pages [3] -->
m

<!-- b000667 | furniture | pages [3] -->
m

<!-- b000668 | furniture | pages [3] -->
m

<!-- b000669 | furniture | pages [3] -->
m

<!-- b000670 | furniture | pages [3] -->
m

<!-- b000671 | furniture | pages [3] -->
m

<!-- b000672 | furniture | pages [3] -->
m

<!-- b000673 | furniture | pages [3] -->
m

<!-- b000674 | furniture | pages [3] -->
m

<!-- b000675 | furniture | pages [3] -->
m

<!-- b000676 | furniture | pages [3] -->
m

<!-- b000677 | furniture | pages [3] -->
m

<!-- b000678 | furniture | pages [3] -->
m

<!-- b000679 | furniture | pages [3] -->
m

<!-- b000680 | furniture | pages [3] -->
m

<!-- b000681 | furniture | pages [3] -->
m

<!-- b000682 | furniture | pages [3] -->
m

<!-- b000683 | furniture | pages [3] -->
m

<!-- b000684 | furniture | pages [3] -->
m

<!-- b000685 | furniture | pages [3] -->
m

<!-- b000686 | furniture | pages [3] -->
m

<!-- b000687 | furniture | pages [3] -->
m

<!-- b000688 | furniture | pages [3] -->
m

<!-- b000689 | furniture | pages [3] -->
m

<!-- b000690 | furniture | pages [3] -->
m

<!-- b000691 | furniture | pages [3] -->
m

<!-- b000692 | furniture | pages [3] -->
m

<!-- b000693 | furniture | pages [3] -->
m

<!-- b000694 | furniture | pages [3] -->
m

<!-- b000695 | furniture | pages [3] -->
m

<!-- b000696 | furniture | pages [3] -->
m

<!-- b000697 | furniture | pages [3] -->
m

<!-- b000698 | furniture | pages [3] -->
m

<!-- b000699 | furniture | pages [3] -->
m

<!-- b000700 | furniture | pages [3] -->
m

<!-- b000701 | furniture | pages [3] -->
m

<!-- b000702 | furniture | pages [3] -->
m

<!-- b000703 | furniture | pages [3] -->
m

<!-- b000704 | furniture | pages [3] -->
m

<!-- b000705 | furniture | pages [3] -->
m

<!-- b000706 | furniture | pages [3] -->
m

<!-- b000707 | furniture | pages [3] -->
m

<!-- b000708 | furniture | pages [3] -->
m

<!-- b000709 | furniture | pages [3] -->
m

<!-- b000710 | furniture | pages [3] -->
m

<!-- b000711 | furniture | pages [3] -->
m

<!-- b000712 | furniture | pages [3] -->
m

<!-- b000713 | furniture | pages [3] -->
m

<!-- b000714 | furniture | pages [3] -->
m

<!-- b000715 | furniture | pages [3] -->
m

<!-- b000716 | furniture | pages [3] -->
m

<!-- b000717 | furniture | pages [3] -->
m

<!-- b000718 | furniture | pages [3] -->
m

<!-- b000719 | furniture | pages [3] -->
m

<!-- b000720 | furniture | pages [3] -->
m

<!-- b000721 | furniture | pages [3] -->
m

<!-- b000722 | furniture | pages [3] -->
m

<!-- b000723 | furniture | pages [3] -->
m

<!-- b000724 | furniture | pages [3] -->
m

<!-- b000725 | furniture | pages [3] -->
m

<!-- b000726 | furniture | pages [3] -->
m

<!-- b000727 | furniture | pages [3] -->
m

<!-- b000728 | furniture | pages [3] -->
m

<!-- b000729 | furniture | pages [3] -->
m

<!-- b000730 | furniture | pages [3] -->
m

<!-- b000731 | furniture | pages [3] -->
m

<!-- b000732 | furniture | pages [3] -->
m

<!-- b000733 | furniture | pages [3] -->
m

<!-- b000734 | furniture | pages [3] -->
m

<!-- b000735 | furniture | pages [3] -->
m

<!-- b000736 | furniture | pages [3] -->
m

<!-- b000737 | furniture | pages [3] -->
m

<!-- b000738 | furniture | pages [3] -->
m

<!-- b000739 | furniture | pages [3] -->
m

<!-- b000740 | furniture | pages [4] -->
Team#2507817                                                             Page 4 of 25

<!-- b000741 | prose | pages [4] -->
three countries and consider the sports in which "great coaches" should be introduced and estimate their impact.

<!-- b000742 | prose | pages [4] -->
 First identify the countries and programs that have been impacted, and then calculate

<!-- b000743 | prose | pages [4] -->
the regression equation between the variables that include the impact of great coaches and the final predicted values. Then identify countries and programs with potential to predict changes in their performance

<!-- b000744 | prose | pages [4] -->
Task 5 Given original insights on Olympic medal counts, analyze the information these

<!-- b000745 | prose | pages [4] -->
insights can provide to the NOC.

<!-- b000746 | prose | pages [4] -->
 Find the eigenvalues from the previous Tasks that have some influence on the number

<!-- b000747 | prose | pages [4] -->
of gold medals & medals, and investigate them

<!-- b000748 | heading | pages [4] -->
1.3 Our work

<!-- b000749 | prose | pages [4] -->
m

<!-- b000750 | prose | pages [4] -->
m

<!-- b000751 | prose | pages [4] -->
m

<!-- b000752 | prose | pages [4] -->
m

<!-- b000753 | prose | pages [4] -->
m

<!-- b000754 | prose | pages [4] -->
m

<!-- b000755 | prose | pages [4] -->
m

<!-- b000756 | prose | pages [4] -->
m

<!-- b000757 | prose | pages [4] -->
m

<!-- b000758 | prose | pages [4] -->
m

<!-- b000759 | prose | pages [4] -->
m

<!-- b000760 | prose | pages [4] -->
m

<!-- b000761 | prose | pages [4] -->
m

<!-- b000762 | prose | pages [4] -->
m

<!-- b000763 | prose | pages [4] -->
m

<!-- b000764 | prose | pages [4] -->
m

<!-- b000765 | prose | pages [4] -->
m

<!-- b000766 | prose | pages [4] -->
m

<!-- b000767 | prose | pages [4] -->
m

<!-- b000768 | prose | pages [4] -->
m

<!-- b000769 | prose | pages [4] -->
m

<!-- b000770 | prose | pages [4] -->
m

<!-- b000771 | prose | pages [4] -->
m

<!-- b000772 | prose | pages [4] -->
m

<!-- b000773 | prose | pages [4] -->
m

<!-- b000774 | prose | pages [4] -->
m

<!-- b000775 | prose | pages [4] -->
m

<!-- b000776 | prose | pages [4] -->
m

<!-- b000777 | prose | pages [4] -->
m

<!-- b000778 | prose | pages [4] -->
m

<!-- b000779 | prose | pages [4] -->
m

<!-- b000780 | prose | pages [4] -->
m

<!-- b000781 | prose | pages [4] -->
m

<!-- b000782 | prose | pages [4] -->
m

<!-- b000783 | prose | pages [4] -->
m

<!-- b000784 | prose | pages [4] -->
m

<!-- b000785 | prose | pages [4] -->
m

<!-- b000786 | prose | pages [4] -->
m

<!-- b000787 | prose | pages [4] -->
m

<!-- b000788 | prose | pages [4] -->
m

<!-- b000789 | prose | pages [4] -->
m

<!-- b000790 | prose | pages [4] -->
m

<!-- b000791 | prose | pages [4] -->
m

<!-- b000792 | prose | pages [4] -->
m

<!-- b000793 | prose | pages [4] -->
m

<!-- b000794 | prose | pages [4] -->
m

<!-- b000795 | prose | pages [4] -->
m

<!-- b000796 | prose | pages [4] -->
m

<!-- b000797 | prose | pages [4] -->
m

<!-- b000798 | prose | pages [4] -->
m

<!-- b000799 | prose | pages [4] -->
m

<!-- b000800 | prose | pages [4] -->
m

<!-- b000801 | prose | pages [4] -->
m

<!-- b000802 | prose | pages [4] -->
m

<!-- b000803 | prose | pages [4] -->
m

<!-- b000804 | prose | pages [4] -->
m

<!-- b000805 | prose | pages [4] -->
m

<!-- b000806 | prose | pages [4] -->
m

<!-- b000807 | prose | pages [4] -->
m

<!-- b000808 | prose | pages [4] -->
m

<!-- b000809 | prose | pages [4] -->
m

<!-- b000810 | prose | pages [4] -->
m

<!-- b000811 | prose | pages [4] -->
m

<!-- b000812 | prose | pages [4] -->
m

<!-- b000813 | prose | pages [4] -->
m

<!-- b000814 | prose | pages [4] -->
m

<!-- b000815 | prose | pages [4] -->
m

<!-- b000816 | prose | pages [4] -->
m

<!-- b000817 | prose | pages [4] -->
m

<!-- b000818 | prose | pages [4] -->
m

<!-- b000819 | prose | pages [4] -->
m

<!-- b000820 | prose | pages [4] -->
m

<!-- b000821 | prose | pages [4] -->
m

<!-- b000822 | prose | pages [4] -->
m

<!-- b000823 | prose | pages [4] -->
m

<!-- b000824 | prose | pages [4] -->
m

<!-- b000825 | prose | pages [4] -->
m

<!-- b000826 | prose | pages [4] -->
m

<!-- b000827 | prose | pages [4] -->
m

<!-- b000828 | prose | pages [4] -->
m

<!-- b000829 | prose | pages [4] -->
m

<!-- b000830 | prose | pages [4] -->
m

<!-- b000831 | prose | pages [4] -->
m

<!-- b000832 | prose | pages [4] -->
m

<!-- b000833 | prose | pages [4] -->
m

<!-- b000834 | prose | pages [4] -->
m

<!-- b000835 | prose | pages [4] -->
m

<!-- b000836 | prose | pages [4] -->
m

<!-- b000837 | prose | pages [4] -->
m

<!-- b000838 | prose | pages [4] -->
m

<!-- b000839 | prose | pages [4] -->
m

<!-- b000840 | prose | pages [4] -->
m

<!-- b000841 | prose | pages [4] -->
m

<!-- b000842 | prose | pages [4] -->
m

<!-- b000843 | prose | pages [4] -->
m

<!-- b000844 | prose | pages [4] -->
m

<!-- b000845 | prose | pages [4] -->
m

<!-- b000846 | prose | pages [4] -->
m

<!-- b000847 | prose | pages [4] -->
m

<!-- b000848 | prose | pages [4] -->
m

<!-- b000849 | prose | pages [4] -->
m

<!-- b000850 | prose | pages [4] -->
m

<!-- b000851 | prose | pages [4] -->
m

<!-- b000852 | prose | pages [4] -->
m

<!-- b000853 | prose | pages [4] -->
m

<!-- b000854 | prose | pages [4] -->
m

<!-- b000855 | prose | pages [4] -->
m

<!-- b000856 | prose | pages [4] -->
m

<!-- b000857 | prose | pages [4] -->
m

<!-- b000858 | prose | pages [4] -->
m

<!-- b000859 | prose | pages [4] -->
m

<!-- b000860 | prose | pages [4] -->
m

<!-- b000861 | prose | pages [4] -->
m

<!-- b000862 | prose | pages [4] -->
m

<!-- b000863 | prose | pages [4] -->
m

<!-- b000864 | prose | pages [4] -->
m

<!-- b000865 | prose | pages [4] -->
m

<!-- b000866 | prose | pages [4] -->
m

<!-- b000867 | prose | pages [4] -->
m

<!-- b000868 | prose | pages [4] -->
m

<!-- b000869 | prose | pages [4] -->
m

<!-- b000870 | prose | pages [4] -->
m

<!-- b000871 | prose | pages [4] -->
m

<!-- b000872 | prose | pages [4] -->
m

<!-- b000873 | prose | pages [4] -->
m

<!-- b000874 | prose | pages [4] -->
m

<!-- b000875 | prose | pages [4] -->
m

<!-- b000876 | prose | pages [4] -->
m

<!-- b000877 | prose | pages [4] -->
m

<!-- b000878 | prose | pages [4] -->
m

<!-- b000879 | prose | pages [4] -->
m

<!-- b000880 | prose | pages [4] -->
m

<!-- b000881 | prose | pages [4] -->
m

<!-- b000882 | prose | pages [4] -->
m

<!-- b000883 | prose | pages [4] -->
m

<!-- b000884 | prose | pages [4] -->
m

<!-- b000885 | prose | pages [4] -->
m

<!-- b000886 | prose | pages [4] -->
m

<!-- b000887 | prose | pages [4] -->
m

<!-- b000888 | prose | pages [4] -->
m

<!-- b000889 | prose | pages [4] -->
m

<!-- b000890 | prose | pages [4] -->
m

<!-- b000891 | prose | pages [4] -->
m

<!-- b000892 | prose | pages [4] -->
m

<!-- b000893 | prose | pages [4] -->
m

<!-- b000894 | prose | pages [4] -->
m

<!-- b000895 | prose | pages [4] -->
m

<!-- b000896 | prose | pages [4] -->
m

<!-- b000897 | prose | pages [4] -->
m

<!-- b000898 | prose | pages [4] -->
m

<!-- b000899 | prose | pages [4] -->
m

<!-- b000900 | prose | pages [4] -->
m

<!-- b000901 | prose | pages [4] -->
m

<!-- b000902 | prose | pages [4] -->
m

<!-- b000903 | prose | pages [4] -->
m

<!-- b000904 | prose | pages [4] -->
m

<!-- b000905 | prose | pages [4] -->
m

<!-- b000906 | prose | pages [4] -->
m

<!-- b000907 | prose | pages [4] -->
m

<!-- b000908 | prose | pages [4] -->
m

<!-- b000909 | prose | pages [4] -->
m

<!-- b000910 | prose | pages [4] -->
m

<!-- b000911 | prose | pages [4] -->
m

<!-- b000912 | prose | pages [4] -->
m

<!-- b000913 | prose | pages [4] -->
m

<!-- b000914 | prose | pages [4] -->
m

<!-- b000915 | prose | pages [4] -->
m

<!-- b000916 | prose | pages [4] -->
m

<!-- b000917 | prose | pages [4] -->
m

<!-- b000918 | prose | pages [4] -->
m

<!-- b000919 | prose | pages [4] -->
m

<!-- b000920 | prose | pages [4] -->
m

<!-- b000921 | prose | pages [4] -->
m

<!-- b000922 | prose | pages [4] -->
m

<!-- b000923 | prose | pages [4] -->
m

<!-- b000924 | prose | pages [4] -->
m

<!-- b000925 | prose | pages [4] -->
m

<!-- b000926 | prose | pages [4] -->
m

<!-- b000927 | prose | pages [4] -->
m

<!-- b000928 | prose | pages [4] -->
m

<!-- b000929 | prose | pages [4] -->
m

<!-- b000930 | prose | pages [4] -->
m

<!-- b000931 | prose | pages [4] -->
m

<!-- b000932 | prose | pages [4] -->
m

<!-- b000933 | prose | pages [4] -->
m

<!-- b000934 | prose | pages [4] -->
m

<!-- b000935 | prose | pages [4] -->
m

<!-- b000936 | prose | pages [4] -->
m

<!-- b000937 | prose | pages [4] -->
m

<!-- b000938 | prose | pages [4] -->
m

<!-- b000939 | prose | pages [4] -->
m

<!-- b000940 | prose | pages [4] -->
m

<!-- b000941 | prose | pages [4] -->
m

<!-- b000942 | prose | pages [4] -->
m

<!-- b000943 | prose | pages [4] -->
m

<!-- b000944 | prose | pages [4] -->
m

<!-- b000945 | prose | pages [4] -->
m

<!-- b000946 | prose | pages [4] -->
m

<!-- b000947 | prose | pages [4] -->
m

<!-- b000948 | prose | pages [4] -->
m

<!-- b000949 | prose | pages [4] -->
m

<!-- b000950 | prose | pages [4] -->
m

<!-- b000951 | prose | pages [4] -->
m

<!-- b000952 | prose | pages [4] -->
m

<!-- b000953 | prose | pages [4] -->
m

<!-- b000954 | prose | pages [4] -->
m

<!-- b000955 | prose | pages [4] -->
m

<!-- b000956 | prose | pages [4] -->
m

<!-- b000957 | prose | pages [4] -->
m

<!-- b000958 | prose | pages [4] -->
m

<!-- b000959 | prose | pages [4] -->
m

<!-- b000960 | prose | pages [4] -->
m

<!-- b000961 | prose | pages [4] -->
m

<!-- b000962 | prose | pages [4] -->
m

<!-- b000963 | prose | pages [4] -->
m

<!-- b000964 | prose | pages [4] -->
m

<!-- b000965 | prose | pages [4] -->
m

<!-- b000966 | prose | pages [4] -->
m

<!-- b000967 | prose | pages [4] -->
m

<!-- b000968 | prose | pages [4] -->
m

<!-- b000969 | prose | pages [4] -->
m

<!-- b000970 | prose | pages [4] -->
m

<!-- b000971 | prose | pages [4] -->
m

<!-- b000972 | prose | pages [4] -->
m

<!-- b000973 | prose | pages [4] -->
m

<!-- b000974 | prose | pages [4] -->
m

<!-- b000975 | prose | pages [4] -->
m

<!-- b000976 | prose | pages [4] -->
m

<!-- b000977 | prose | pages [4] -->
m

<!-- b000978 | prose | pages [4] -->
m

<!-- b000979 | prose | pages [4] -->
m

<!-- b000980 | prose | pages [4] -->
m

<!-- b000981 | prose | pages [4] -->
m

<!-- b000982 | prose | pages [4] -->
m

<!-- b000983 | prose | pages [4] -->
m

<!-- b000984 | prose | pages [4] -->
m

<!-- b000985 | prose | pages [4] -->
m

<!-- b000986 | prose | pages [4] -->
m

<!-- b000987 | prose | pages [4] -->
m

<!-- b000988 | prose | pages [4] -->
m

<!-- b000989 | prose | pages [4] -->
m

<!-- b000990 | prose | pages [4] -->
m

<!-- b000991 | prose | pages [4] -->
m

<!-- b000992 | prose | pages [4] -->
m

<!-- b000993 | prose | pages [4] -->
m

<!-- b000994 | prose | pages [4] -->
m

<!-- b000995 | prose | pages [4] -->
m

<!-- b000996 | prose | pages [4] -->
m

<!-- b000997 | prose | pages [4] -->
m

<!-- b000998 | prose | pages [4] -->
m

<!-- b000999 | prose | pages [4] -->
m

<!-- b001000 | prose | pages [4] -->
m

<!-- b001001 | prose | pages [4] -->
m

<!-- b001002 | prose | pages [4] -->
m

<!-- b001003 | prose | pages [4] -->
m

<!-- b001004 | prose | pages [4] -->
m

<!-- b001005 | prose | pages [4] -->
m

<!-- b001006 | prose | pages [4] -->
m

<!-- b001007 | prose | pages [4] -->
m

<!-- b001008 | prose | pages [4] -->
m

<!-- b001009 | prose | pages [4] -->
m

<!-- b001010 | prose | pages [4] -->
m

<!-- b001011 | prose | pages [4] -->
m

<!-- b001012 | prose | pages [4] -->
m

<!-- b001013 | prose | pages [4] -->
m

<!-- b001014 | prose | pages [4] -->
m

<!-- b001015 | prose | pages [4] -->
m

<!-- b001016 | prose | pages [4] -->
m

<!-- b001017 | prose | pages [4] -->
m

<!-- b001018 | prose | pages [4] -->
m

<!-- b001019 | prose | pages [4] -->
m

<!-- b001020 | prose | pages [4] -->
m

<!-- b001021 | prose | pages [4] -->
m

<!-- b001022 | prose | pages [4] -->
m

<!-- b001023 | prose | pages [4] -->
m

<!-- b001024 | prose | pages [4] -->
m

<!-- b001025 | prose | pages [4] -->
m

<!-- b001026 | prose | pages [4] -->
m

<!-- b001027 | prose | pages [4] -->
m

<!-- b001028 | prose | pages [4] -->
m

<!-- b001029 | prose | pages [4] -->
m

<!-- b001030 | prose | pages [4] -->
m

<!-- b001031 | prose | pages [4] -->
m

<!-- b001032 | prose | pages [4] -->
m

<!-- b001033 | prose | pages [4] -->
m

<!-- b001034 | prose | pages [4] -->
m

<!-- b001035 | prose | pages [4] -->
m

<!-- b001036 | prose | pages [4] -->
m

<!-- b001037 | prose | pages [4] -->
m

<!-- b001038 | prose | pages [4] -->
m

<!-- b001039 | prose | pages [4] -->
m

<!-- b001040 | prose | pages [4] -->
m

<!-- b001041 | prose | pages [4] -->
m

<!-- b001042 | prose | pages [4] -->
m

<!-- b001043 | prose | pages [4] -->
m

<!-- b001044 | prose | pages [4] -->
m

<!-- b001045 | prose | pages [4] -->
m

<!-- b001046 | prose | pages [4] -->
m

<!-- b001047 | prose | pages [4] -->
m

<!-- b001048 | prose | pages [4] -->
m

<!-- b001049 | prose | pages [4] -->
m

<!-- b001050 | prose | pages [4] -->
m

<!-- b001051 | prose | pages [4] -->
m

<!-- b001052 | prose | pages [4] -->
m

<!-- b001053 | prose | pages [4] -->
m

<!-- b001054 | prose | pages [4] -->
m

<!-- b001055 | prose | pages [4] -->
m

<!-- b001056 | prose | pages [4] -->
m

<!-- b001057 | prose | pages [4] -->
m

<!-- b001058 | prose | pages [4] -->
m

<!-- b001059 | prose | pages [4] -->
m

<!-- b001060 | prose | pages [4] -->
m

<!-- b001061 | prose | pages [4] -->
m

<!-- b001062 | prose | pages [4] -->
m

<!-- b001063 | prose | pages [4] -->
m

<!-- b001064 | prose | pages [4] -->
m

<!-- b001065 | prose | pages [4] -->
m

<!-- b001066 | prose | pages [4] -->
m

<!-- b001067 | prose | pages [4] -->
m

<!-- b001068 | prose | pages [4] -->
m

<!-- b001069 | prose | pages [4] -->
m

<!-- b001070 | prose | pages [4] -->
m

<!-- b001071 | prose | pages [4] -->
m

<!-- b001072 | prose | pages [4] -->
m

<!-- b001073 | prose | pages [4] -->
m

<!-- b001074 | prose | pages [4] -->
m

<!-- b001075 | prose | pages [4] -->
m

<!-- b001076 | prose | pages [4] -->
m

<!-- b001077 | prose | pages [4] -->
m

<!-- b001078 | prose | pages [4] -->
m

<!-- b001079 | prose | pages [4] -->
m

<!-- b001080 | prose | pages [4] -->
m

<!-- b001081 | prose | pages [4] -->
m

<!-- b001082 | prose | pages [4] -->
m

<!-- b001083 | prose | pages [4] -->
m

<!-- b001084 | prose | pages [4] -->
m

<!-- b001085 | prose | pages [4] -->
m

<!-- b001086 | prose | pages [4] -->
m

<!-- b001087 | prose | pages [4] -->
m

<!-- b001088 | prose | pages [4] -->
m

<!-- b001089 | prose | pages [4] -->
m

<!-- b001090 | prose | pages [4] -->
m

<!-- b001091 | prose | pages [4] -->
m

<!-- b001092 | prose | pages [4] -->
m

<!-- b001093 | prose | pages [4] -->
m

<!-- b001094 | prose | pages [4] -->
m

<!-- b001095 | prose | pages [4] -->
m

<!-- b001096 | prose | pages [4] -->
m

<!-- b001097 | prose | pages [4] -->
m

<!-- b001098 | prose | pages [4] -->
m

<!-- b001099 | prose | pages [4] -->
m

<!-- b001100 | prose | pages [4] -->
m

<!-- b001101 | prose | pages [4] -->
m

<!-- b001102 | prose | pages [4] -->
m

<!-- b001103 | prose | pages [4] -->
m

<!-- b001104 | prose | pages [4] -->
m

<!-- b001105 | prose | pages [4] -->
m

<!-- b001106 | prose | pages [4] -->
m

<!-- b001107 | prose | pages [4] -->
m

<!-- b001108 | prose | pages [4] -->
m

<!-- b001109 | prose | pages [4] -->
m

<!-- b001110 | prose | pages [4] -->
m

<!-- b001111 | prose | pages [4] -->
m

<!-- b001112 | prose | pages [4] -->
m

<!-- b001113 | prose | pages [4] -->
m

<!-- b001114 | prose | pages [4] -->
m

<!-- b001115 | prose | pages [4] -->
m

<!-- b001116 | prose | pages [4] -->
m

<!-- b001117 | prose | pages [4] -->
m

<!-- b001118 | prose | pages [4] -->
m

<!-- b001119 | prose | pages [4] -->
m

<!-- b001120 | prose | pages [4] -->
m

<!-- b001121 | prose | pages [4] -->
m

<!-- b001122 | prose | pages [4] -->
m

<!-- b001123 | prose | pages [4] -->
m

<!-- b001124 | prose | pages [4] -->
m

<!-- b001125 | prose | pages [4] -->
m

<!-- b001126 | prose | pages [4] -->
m

<!-- b001127 | prose | pages [4] -->
m

<!-- b001128 | prose | pages [4] -->
m

<!-- b001129 | prose | pages [4] -->
m

<!-- b001130 | prose | pages [4] -->
m

<!-- b001131 | prose | pages [4] -->
m

<!-- b001132 | prose | pages [4] -->
m

<!-- b001133 | prose | pages [4] -->
m

<!-- b001134 | prose | pages [4] -->
m

<!-- b001135 | prose | pages [4] -->
m

<!-- b001136 | prose | pages [4] -->
m

<!-- b001137 | prose | pages [4] -->
m

<!-- b001138 | prose | pages [4] -->
m

<!-- b001139 | prose | pages [4] -->
m

<!-- b001140 | prose | pages [4] -->
m

<!-- b001141 | prose | pages [4] -->
m

<!-- b001142 | prose | pages [4] -->
m

<!-- b001143 | prose | pages [4] -->
m

<!-- b001144 | prose | pages [4] -->
m

<!-- b001145 | prose | pages [4] -->
m

<!-- b001146 | prose | pages [4] -->
m

<!-- b001147 | prose | pages [4] -->
m

<!-- b001148 | prose | pages [4] -->
m

<!-- b001149 | prose | pages [4] -->
m

<!-- b001150 | prose | pages [4] -->
m

<!-- b001151 | prose | pages [4] -->
m

<!-- b001152 | prose | pages [4] -->
m

<!-- b001153 | prose | pages [4] -->
m

<!-- b001154 | prose | pages [4] -->
m

<!-- b001155 | prose | pages [4] -->
m

<!-- b001156 | prose | pages [4] -->
m

<!-- b001157 | prose | pages [4] -->
m

<!-- b001158 | prose | pages [4] -->
m

<!-- b001159 | prose | pages [4] -->
m

<!-- b001160 | prose | pages [4] -->
m

<!-- b001161 | prose | pages [4] -->
m

<!-- b001162 | prose | pages [4] -->
m

<!-- b001163 | prose | pages [4] -->
m

<!-- b001164 | prose | pages [4] -->
m

<!-- b001165 | prose | pages [4] -->
m

<!-- b001166 | prose | pages [4] -->
m

<!-- b001167 | prose | pages [4] -->
m

<!-- b001168 | prose | pages [4] -->
m

<!-- b001169 | prose | pages [4] -->
m

<!-- b001170 | prose | pages [4] -->
m

<!-- b001171 | prose | pages [4] -->
m

<!-- b001172 | prose | pages [4] -->
m

<!-- b001173 | prose | pages [4] -->
m

<!-- b001174 | prose | pages [4] -->
m

<!-- b001175 | prose | pages [4] -->
m

<!-- b001176 | prose | pages [4] -->
m

<!-- b001177 | prose | pages [4] -->
m

<!-- b001178 | prose | pages [4] -->
m

<!-- b001179 | prose | pages [4] -->
m

<!-- b001180 | prose | pages [4] -->
m

<!-- b001181 | prose | pages [4] -->
m

<!-- b001182 | prose | pages [4] -->
m

<!-- b001183 | prose | pages [4] -->
m

<!-- b001184 | prose | pages [4] -->
m

<!-- b001185 | prose | pages [4] -->
m

<!-- b001186 | prose | pages [4] -->
m

<!-- b001187 | prose | pages [4] -->
m

<!-- b001188 | prose | pages [4] -->
m

<!-- b001189 | prose | pages [4] -->
m

<!-- b001190 | prose | pages [4] -->
m

<!-- b001191 | prose | pages [4] -->
m

<!-- b001192 | prose | pages [4] -->
m

<!-- b001193 | prose | pages [4] -->
m

<!-- b001194 | prose | pages [4] -->
m

<!-- b001195 | prose | pages [4] -->
m

<!-- b001196 | prose | pages [4] -->
m

<!-- b001197 | prose | pages [4] -->
m

<!-- b001198 | prose | pages [4] -->
m

<!-- b001199 | prose | pages [4] -->
m

<!-- b001200 | prose | pages [4] -->
m

<!-- b001201 | prose | pages [4] -->
m

<!-- b001202 | prose | pages [4] -->
m

<!-- b001203 | prose | pages [4] -->
m

<!-- b001204 | prose | pages [4] -->
m

<!-- b001205 | prose | pages [4] -->
m

<!-- b001206 | prose | pages [4] -->
m

<!-- b001207 | prose | pages [4] -->
m

<!-- b001208 | prose | pages [4] -->
m

<!-- b001209 | prose | pages [4] -->
m

<!-- b001210 | prose | pages [4] -->
m

<!-- b001211 | prose | pages [4] -->
m

<!-- b001212 | prose | pages [4] -->
m

<!-- b001213 | prose | pages [4] -->
m

<!-- b001214 | prose | pages [4] -->
m

<!-- b001215 | prose | pages [4] -->
m

<!-- b001216 | prose | pages [4] -->
m

<!-- b001217 | prose | pages [4] -->
m

<!-- b001218 | prose | pages [4] -->
m

<!-- b001219 | prose | pages [4] -->
m

<!-- b001220 | prose | pages [4] -->
m

<!-- b001221 | prose | pages [4] -->
m

<!-- b001222 | prose | pages [4] -->
m

<!-- b001223 | prose | pages [4] -->
m

<!-- b001224 | prose | pages [4] -->
m

<!-- b001225 | prose | pages [4] -->
m

<!-- b001226 | prose | pages [4] -->
m

<!-- b001227 | prose | pages [4] -->
m

<!-- b001228 | prose | pages [4] -->
m

<!-- b001229 | prose | pages [4] -->
m

<!-- b001230 | prose | pages [4] -->
m

<!-- b001231 | prose | pages [4] -->
m

<!-- b001232 | prose | pages [4] -->
m

<!-- b001233 | prose | pages [4] -->
m

<!-- b001234 | prose | pages [4] -->
m

<!-- b001235 | prose | pages [4] -->
m

<!-- b001236 | prose | pages [4] -->
m

<!-- b001237 | prose | pages [4] -->
m

<!-- b001238 | prose | pages [4] -->
m

<!-- b001239 | prose | pages [4] -->
m

<!-- b001240 | prose | pages [4] -->
m

<!-- b001241 | prose | pages [4] -->
m

<!-- b001242 | prose | pages [4] -->
m

<!-- b001243 | prose | pages [4] -->
m

<!-- b001244 | prose | pages [4] -->
m

<!-- b001245 | prose | pages [4] -->
m

<!-- b001246 | prose | pages [4] -->
m

<!-- b001247 | prose | pages [4] -->
m

<!-- b001248 | prose | pages [4] -->
m

<!-- b001249 | prose | pages [4] -->
m

<!-- b001250 | prose | pages [4] -->
m

<!-- b001251 | prose | pages [4] -->
m

<!-- b001252 | prose | pages [4] -->
m

<!-- b001253 | prose | pages [4] -->
m

<!-- b001254 | prose | pages [4] -->
m

<!-- b001255 | prose | pages [4] -->
m

<!-- b001256 | prose | pages [4] -->
m

<!-- b001257 | prose | pages [4] -->
m

<!-- b001258 | prose | pages [4] -->
m

<!-- b001259 | prose | pages [4] -->
m

<!-- b001260 | prose | pages [4] -->
m

<!-- b001261 | prose | pages [4] -->
m

<!-- b001262 | prose | pages [4] -->
m

<!-- b001263 | prose | pages [4] -->
m

<!-- b001264 | prose | pages [4] -->
m

<!-- b001265 | prose | pages [4] -->
m

<!-- b001266 | prose | pages [4] -->
m

<!-- b001267 | prose | pages [4] -->
m

<!-- b001268 | prose | pages [4] -->
m

<!-- b001269 | prose | pages [4] -->
m

<!-- b001270 | prose | pages [4] -->
m

<!-- b001271 | prose | pages [4] -->
m

<!-- b001272 | prose | pages [4] -->
m

<!-- b001273 | prose | pages [4] -->
m

<!-- b001274 | prose | pages [4] -->
m

<!-- b001275 | prose | pages [4] -->
m

<!-- b001276 | prose | pages [4] -->
m

<!-- b001277 | prose | pages [4] -->
m

<!-- b001278 | prose | pages [4] -->
m

<!-- b001279 | prose | pages [4] -->
m

<!-- b001280 | prose | pages [4] -->
m

<!-- b001281 | prose | pages [4] -->
m

<!-- b001282 | prose | pages [4] -->
m

<!-- b001283 | prose | pages [4] -->
m

<!-- b001284 | prose | pages [4] -->
m

<!-- b001285 | prose | pages [4] -->
m

<!-- b001286 | prose | pages [4] -->
m

<!-- b001287 | prose | pages [4] -->
m

<!-- b001288 | prose | pages [4] -->
m

<!-- b001289 | prose | pages [4] -->
m

<!-- b001290 | prose | pages [4] -->
m

<!-- b001291 | prose | pages [4] -->
m

<!-- b001292 | prose | pages [4] -->
m

<!-- b001293 | prose | pages [4] -->
m

<!-- b001294 | prose | pages [4] -->
m

<!-- b001295 | prose | pages [4] -->
m

<!-- b001296 | prose | pages [4] -->
m

<!-- b001297 | prose | pages [4] -->
m

<!-- b001298 | prose | pages [4] -->
m

<!-- b001299 | prose | pages [4] -->
m

<!-- b001300 | prose | pages [4] -->
m

<!-- b001301 | prose | pages [4] -->
m

<!-- b001302 | prose | pages [4] -->
m

<!-- b001303 | prose | pages [4] -->
m

<!-- b001304 | prose | pages [4] -->
m

<!-- b001305 | prose | pages [4] -->
m

<!-- b001306 | prose | pages [4] -->
m

<!-- b001307 | prose | pages [4] -->
m

<!-- b001308 | prose | pages [4] -->
m

<!-- b001309 | prose | pages [4] -->
m

<!-- b001310 | prose | pages [4] -->
m

<!-- b001311 | prose | pages [4] -->
m

<!-- b001312 | prose | pages [4] -->
m

<!-- b001313 | prose | pages [4] -->
m

<!-- b001314 | prose | pages [4] -->
m

<!-- b001315 | prose | pages [4] -->
m

<!-- b001316 | prose | pages [4] -->
m

<!-- b001317 | prose | pages [4] -->
m

<!-- b001318 | prose | pages [4] -->
m

<!-- b001319 | prose | pages [4] -->
m

<!-- b001320 | prose | pages [4] -->
m

<!-- b001321 | prose | pages [4] -->
m

<!-- b001322 | prose | pages [4] -->
m

<!-- b001323 | prose | pages [4] -->
m

<!-- b001324 | prose | pages [4] -->
m

<!-- b001325 | prose | pages [4] -->
m

<!-- b001326 | prose | pages [4] -->
m

<!-- b001327 | prose | pages [4] -->
m

<!-- b001328 | prose | pages [4] -->
m

<!-- b001329 | prose | pages [4] -->
m

<!-- b001330 | prose | pages [4] -->
m

<!-- b001331 | prose | pages [4] -->
m

<!-- b001332 | prose | pages [4] -->
m

<!-- b001333 | prose | pages [4] -->
m

<!-- b001334 | prose | pages [4] -->
m

<!-- b001335 | prose | pages [4] -->
m

<!-- b001336 | prose | pages [4] -->
m

<!-- b001337 | prose | pages [4] -->
m

<!-- b001338 | prose | pages [4] -->
m

<!-- b001339 | prose | pages [4] -->
m

<!-- b001340 | prose | pages [4] -->
m

<!-- b001341 | prose | pages [4] -->
m

<!-- b001342 | prose | pages [4] -->
m

<!-- b001343 | prose | pages [4] -->
m

<!-- b001344 | prose | pages [4] -->
m

<!-- b001345 | prose | pages [4] -->
m

<!-- b001346 | prose | pages [4] -->
m

<!-- b001347 | prose | pages [4] -->
m

<!-- b001348 | prose | pages [4] -->
m

<!-- b001349 | prose | pages [4] -->
m

<!-- b001350 | prose | pages [4] -->
m

<!-- b001351 | prose | pages [4] -->
m

<!-- b001352 | prose | pages [4] -->
m

<!-- b001353 | prose | pages [4] -->
m

<!-- b001354 | prose | pages [4] -->
m

<!-- b001355 | prose | pages [4] -->
m

<!-- b001356 | prose | pages [4] -->
m

<!-- b001357 | prose | pages [4] -->
m

<!-- b001358 | prose | pages [4] -->
m

<!-- b001359 | prose | pages [4] -->
m

<!-- b001360 | prose | pages [4] -->
m

<!-- b001361 | prose | pages [4] -->
m

<!-- b001362 | prose | pages [4] -->
m

<!-- b001363 | prose | pages [4] -->
m

<!-- b001364 | prose | pages [4] -->
m

<!-- b001365 | prose | pages [4] -->
m

<!-- b001366 | prose | pages [4] -->
m

<!-- b001367 | prose | pages [4] -->
m

<!-- b001368 | prose | pages [4] -->
m

<!-- b001369 | prose | pages [4] -->
m

<!-- b001370 | prose | pages [4] -->
m

<!-- b001371 | prose | pages [4] -->
m

<!-- b001372 | prose | pages [4] -->
m

<!-- b001373 | prose | pages [4] -->
m

<!-- b001374 | prose | pages [4] -->
m

<!-- b001375 | prose | pages [4] -->
m

<!-- b001376 | prose | pages [4] -->
m

<!-- b001377 | prose | pages [4] -->
m

<!-- b001378 | prose | pages [4] -->
m

<!-- b001379 | prose | pages [4] -->
m

<!-- b001380 | prose | pages [4] -->
m

<!-- b001381 | prose | pages [4] -->
m

<!-- b001382 | prose | pages [4] -->
m

<!-- b001383 | prose | pages [4] -->
m

<!-- b001384 | prose | pages [4] -->
m

<!-- b001385 | prose | pages [4] -->
m

<!-- b001386 | prose | pages [4] -->
m

<!-- b001387 | prose | pages [4] -->
m

<!-- b001388 | prose | pages [4] -->
m

<!-- b001389 | prose | pages [4] -->
m

<!-- b001390 | prose | pages [4] -->
m

<!-- b001391 | prose | pages [4] -->
m

<!-- b001392 | prose | pages [4] -->
m

<!-- b001393 | prose | pages [4] -->
m

<!-- b001394 | prose | pages [4] -->
m

<!-- b001395 | prose | pages [4] -->
m

<!-- b001396 | prose | pages [4] -->
m

<!-- b001397 | prose | pages [4] -->
m

<!-- b001398 | prose | pages [4] -->
m

<!-- b001399 | prose | pages [4] -->
m

<!-- b001400 | prose | pages [4] -->
m

<!-- b001401 | prose | pages [4] -->
m

<!-- b001402 | prose | pages [4] -->
m

<!-- b001403 | prose | pages [4] -->
m

<!-- b001404 | prose | pages [4] -->
m

<!-- b001405 | prose | pages [4] -->
m

<!-- b001406 | prose | pages [4] -->
m

<!-- b001407 | prose | pages [4] -->
m

<!-- b001408 | prose | pages [4] -->
m

<!-- b001409 | prose | pages [4] -->
m

<!-- b001410 | prose | pages [4] -->
m

<!-- b001411 | prose | pages [4] -->
m

<!-- b001412 | prose | pages [4] -->
m

<!-- b001413 | prose | pages [4] -->
m

<!-- b001414 | prose | pages [4] -->
m

<!-- b001415 | prose | pages [4] -->
m

<!-- b001416 | prose | pages [4] -->
m

<!-- b001417 | prose | pages [4] -->
m

<!-- b001418 | prose | pages [4] -->
m

<!-- b001419 | prose | pages [4] -->
m

<!-- b001420 | prose | pages [4] -->
m

<!-- b001421 | prose | pages [4] -->
m

<!-- b001422 | prose | pages [4] -->
m

<!-- b001423 | prose | pages [4] -->
m

<!-- b001424 | prose | pages [4] -->
m

<!-- b001425 | prose | pages [4] -->
m

<!-- b001426 | prose | pages [4] -->
m

<!-- b001427 | prose | pages [4] -->
m

<!-- b001428 | prose | pages [4] -->
m

<!-- b001429 | prose | pages [4] -->
m

<!-- b001430 | prose | pages [4] -->
m

<!-- b001431 | prose | pages [4] -->
m

<!-- b001432 | prose | pages [4] -->
m

<!-- b001433 | prose | pages [4] -->
m

<!-- b001434 | prose | pages [4] -->
m

<!-- b001435 | prose | pages [4] -->
m

<!-- b001436 | furniture | pages [4] -->


<!-- b001437 | caption | pages [4] -->
Figure 2 Our Work

<!-- b001438 | furniture | pages [4] -->


<!-- b001439 | prose | pages [4] -->
关注数学模型

<!-- b001440 | furniture | pages [4] -->
2

<!-- b001441 | furniture | pages [4] -->
MATHmodels

<!-- b001442 | furniture | pages [4] -->
获取更多资讯

<!-- b001443 | furniture | pages [5] -->
Team#2507817                                                             Page 5 of 25

<!-- b001444 | heading | pages [5] -->
2 Basic Assumption

<!-- b001445 | prose | pages [5] -->
 Hypothesis 1: Assume that the number of athletes participating in the 2028

<!-- b001446 | prose | pages [5] -->
Olympics, the number of countries, and the number of events held are the same as in 2024.

<!-- b001447 | prose | pages [5] -->
Legitimacy: The data review revealed that the number of countries participating in recent Olympic Games and the number of events held have not changed much. To simplify the calculation of the model, it is assumed that the number remains constant.

<!-- b001448 | prose | pages [5] -->
 Hypothesis 2: The variables are independent of each other and only affect the

<!-- b001449 | prose | pages [5] -->
results.

<!-- b001450 | heading | pages [5] -->
Justification: while these variables interact, considering them in the model adds

<!-- b001451 | prose | pages [5] -->
complexity and unpredictability. For extensive analysis, we focus more on measurable and

<!-- b001452 | prose | pages [5] -->
微信公众号：数学模型

<!-- b001453 | prose | pages [5] -->
consistent factors

<!-- b001454 | heading | pages [5] -->
 Assumption 3: Excluding the cost of investing in great coaches

<!-- b001455 | prose | pages [5] -->
Justification: focuses on the direct impact of coaching quality on athlete performance, team performance, or overall sport system development.

<!-- b001456 | heading | pages [5] -->
3 Symbols

<!-- b001457 | prose | pages [5] -->
Symbols Definition

<!-- b001458 | prose | pages [5] -->
A Total number of athletes from the i-th country in the j-th Olympic Games ij

<!-- b001459 | prose | pages [5] -->
微信号：MATHmodels

<!-- b001460 | prose | pages [5] -->
The number of gold medals won by the i-th country before the j-th Olympic G ij

<!-- b001461 | prose | pages [5] -->
Games

<!-- b001462 | prose | pages [5] -->
The total number of medals won by the i-th country before the j-th Olympic T ij

<!-- b001463 | prose | pages [5] -->
Games

<!-- b001464 | prose | pages [5] -->
E Total number of events in the j Olympic Games ij

<!-- b001465 | prose | pages [5] -->
Y Number of gold medals predicted g

<!-- b001466 | prose | pages [5] -->
tY Total number of medals predicted

<!-- b001467 | prose | pages [5] -->
ka Number of athletes in the kth country

<!-- b001468 | prose | pages [5] -->
ke Number of projects participated by the kth country

<!-- b001469 | prose | pages [5] -->
kp Number of historical entries of the kth country

<!-- b001470 | heading | pages [5] -->
4  Data Preprocessing

<!-- b001471 | prose | pages [5] -->
 Outlier handling: each country may have different teams for the same program, and the

<!-- b001472 | prose | pages [5] -->
names of these teams contain markers representing the order of the teams, and there is garbled code after the name of the country. We dealt with cleaning these outliers.

<!-- b001473 | prose | pages [5] -->
 Data standardization: In forecasting, to ensure that the data have relatively equal weights

<!-- b001474 | prose | pages [5] -->
for each feature value, data standardization is used, where the mean ( x ) and standard deviation (SD) of each feature are to be calculated

<!-- b001475 | prose | pages [5] -->
m

<!-- b001476 | prose | pages [5] -->
m

<!-- b001477 | prose | pages [5] -->
m

<!-- b001478 | prose | pages [5] -->
m

<!-- b001479 | prose | pages [5] -->
m

<!-- b001480 | prose | pages [5] -->
m

<!-- b001481 | prose | pages [5] -->
m

<!-- b001482 | prose | pages [5] -->
m

<!-- b001483 | prose | pages [5] -->
m

<!-- b001484 | prose | pages [5] -->
m

<!-- b001485 | prose | pages [5] -->
m

<!-- b001486 | prose | pages [5] -->
m

<!-- b001487 | prose | pages [5] -->
m

<!-- b001488 | prose | pages [5] -->
m

<!-- b001489 | prose | pages [5] -->
m

<!-- b001490 | prose | pages [5] -->
m

<!-- b001491 | prose | pages [5] -->
m

<!-- b001492 | prose | pages [5] -->
m

<!-- b001493 | prose | pages [5] -->
m

<!-- b001494 | prose | pages [5] -->
m

<!-- b001495 | prose | pages [5] -->
m

<!-- b001496 | prose | pages [5] -->
m

<!-- b001497 | prose | pages [5] -->
m

<!-- b001498 | prose | pages [5] -->
m

<!-- b001499 | prose | pages [5] -->
m

<!-- b001500 | prose | pages [5] -->
m

<!-- b001501 | prose | pages [5] -->
m

<!-- b001502 | prose | pages [5] -->
m

<!-- b001503 | prose | pages [5] -->
m

<!-- b001504 | prose | pages [5] -->
m

<!-- b001505 | prose | pages [5] -->
m

<!-- b001506 | prose | pages [5] -->
m

<!-- b001507 | prose | pages [5] -->
m

<!-- b001508 | prose | pages [5] -->
m

<!-- b001509 | prose | pages [5] -->
m

<!-- b001510 | prose | pages [5] -->
m

<!-- b001511 | prose | pages [5] -->
m

<!-- b001512 | prose | pages [5] -->
m

<!-- b001513 | prose | pages [5] -->
m

<!-- b001514 | prose | pages [5] -->
m

<!-- b001515 | prose | pages [5] -->
m

<!-- b001516 | prose | pages [5] -->
m

<!-- b001517 | prose | pages [5] -->
m

<!-- b001518 | prose | pages [5] -->
m

<!-- b001519 | prose | pages [5] -->
m

<!-- b001520 | prose | pages [5] -->
m

<!-- b001521 | prose | pages [5] -->
m

<!-- b001522 | prose | pages [5] -->
m

<!-- b001523 | prose | pages [5] -->
m

<!-- b001524 | prose | pages [5] -->
m

<!-- b001525 | prose | pages [5] -->
m

<!-- b001526 | prose | pages [5] -->
m

<!-- b001527 | prose | pages [5] -->
m

<!-- b001528 | prose | pages [5] -->
m

<!-- b001529 | prose | pages [5] -->
m

<!-- b001530 | prose | pages [5] -->
m

<!-- b001531 | prose | pages [5] -->
m

<!-- b001532 | prose | pages [5] -->
m

<!-- b001533 | prose | pages [5] -->
m

<!-- b001534 | prose | pages [5] -->
m

<!-- b001535 | prose | pages [5] -->
m

<!-- b001536 | prose | pages [5] -->
m

<!-- b001537 | prose | pages [5] -->
m

<!-- b001538 | prose | pages [5] -->
m

<!-- b001539 | prose | pages [5] -->
m

<!-- b001540 | prose | pages [5] -->
m

<!-- b001541 | prose | pages [5] -->
m

<!-- b001542 | prose | pages [5] -->
m

<!-- b001543 | prose | pages [5] -->
m

<!-- b001544 | prose | pages [5] -->
m

<!-- b001545 | prose | pages [5] -->
m

<!-- b001546 | prose | pages [5] -->
m

<!-- b001547 | prose | pages [5] -->
m

<!-- b001548 | prose | pages [5] -->
m

<!-- b001549 | prose | pages [5] -->
m

<!-- b001550 | prose | pages [5] -->
m

<!-- b001551 | prose | pages [5] -->
m

<!-- b001552 | prose | pages [5] -->
m

<!-- b001553 | prose | pages [5] -->
m

<!-- b001554 | prose | pages [5] -->
m

<!-- b001555 | prose | pages [5] -->
m

<!-- b001556 | prose | pages [5] -->
m

<!-- b001557 | prose | pages [5] -->
m

<!-- b001558 | prose | pages [5] -->
m

<!-- b001559 | prose | pages [5] -->
m

<!-- b001560 | prose | pages [5] -->
m

<!-- b001561 | prose | pages [5] -->
m

<!-- b001562 | prose | pages [5] -->
m

<!-- b001563 | prose | pages [5] -->
m

<!-- b001564 | prose | pages [5] -->
m

<!-- b001565 | prose | pages [5] -->
m

<!-- b001566 | prose | pages [5] -->
m

<!-- b001567 | prose | pages [5] -->
m

<!-- b001568 | prose | pages [5] -->
m

<!-- b001569 | prose | pages [5] -->
m

<!-- b001570 | prose | pages [5] -->
m

<!-- b001571 | prose | pages [5] -->
m

<!-- b001572 | prose | pages [5] -->
m

<!-- b001573 | prose | pages [5] -->
m

<!-- b001574 | prose | pages [5] -->
m

<!-- b001575 | prose | pages [5] -->
m

<!-- b001576 | prose | pages [5] -->
m

<!-- b001577 | prose | pages [5] -->
m

<!-- b001578 | prose | pages [5] -->
m

<!-- b001579 | prose | pages [5] -->
m

<!-- b001580 | prose | pages [5] -->
m

<!-- b001581 | prose | pages [5] -->
m

<!-- b001582 | prose | pages [5] -->
m

<!-- b001583 | prose | pages [5] -->
m

<!-- b001584 | prose | pages [5] -->
m

<!-- b001585 | prose | pages [5] -->
m

<!-- b001586 | prose | pages [5] -->
m

<!-- b001587 | prose | pages [5] -->
m

<!-- b001588 | prose | pages [5] -->
m

<!-- b001589 | prose | pages [5] -->
m

<!-- b001590 | prose | pages [5] -->
m

<!-- b001591 | prose | pages [5] -->
m

<!-- b001592 | prose | pages [5] -->
m

<!-- b001593 | prose | pages [5] -->
m

<!-- b001594 | prose | pages [5] -->
m

<!-- b001595 | prose | pages [5] -->
m

<!-- b001596 | prose | pages [5] -->
m

<!-- b001597 | prose | pages [5] -->
m

<!-- b001598 | prose | pages [5] -->
m

<!-- b001599 | prose | pages [5] -->
m

<!-- b001600 | prose | pages [5] -->
m

<!-- b001601 | prose | pages [5] -->
m

<!-- b001602 | prose | pages [5] -->
m

<!-- b001603 | prose | pages [5] -->
m

<!-- b001604 | prose | pages [5] -->
m

<!-- b001605 | furniture | pages [5] -->


<!-- b001606 | prose | pages [5] -->
m

<!-- b001607 | prose | pages [5] -->
m

<!-- b001608 | prose | pages [5] -->
m

<!-- b001609 | prose | pages [5] -->
m

<!-- b001610 | prose | pages [5] -->
m

<!-- b001611 | prose | pages [5] -->
m

<!-- b001612 | prose | pages [5] -->
m

<!-- b001613 | prose | pages [5] -->
m

<!-- b001614 | prose | pages [5] -->
m

<!-- b001615 | prose | pages [5] -->
m

<!-- b001616 | prose | pages [5] -->
m

<!-- b001617 | prose | pages [5] -->
m

<!-- b001618 | prose | pages [5] -->
m

<!-- b001619 | prose | pages [5] -->
m

<!-- b001620 | prose | pages [5] -->
m

<!-- b001621 | prose | pages [5] -->
m

<!-- b001622 | prose | pages [5] -->
m

<!-- b001623 | prose | pages [5] -->
m

<!-- b001624 | prose | pages [5] -->
m

<!-- b001625 | prose | pages [5] -->
m

<!-- b001626 | prose | pages [5] -->
m

<!-- b001627 | prose | pages [5] -->
m

<!-- b001628 | prose | pages [5] -->
m

<!-- b001629 | prose | pages [5] -->
m

<!-- b001630 | prose | pages [5] -->
m

<!-- b001631 | prose | pages [5] -->
m

<!-- b001632 | prose | pages [5] -->
m

<!-- b001633 | prose | pages [5] -->
m

<!-- b001634 | prose | pages [5] -->
m

<!-- b001635 | prose | pages [5] -->
m

<!-- b001636 | prose | pages [5] -->
m

<!-- b001637 | prose | pages [5] -->
m

<!-- b001638 | prose | pages [5] -->
m

<!-- b001639 | prose | pages [5] -->
m

<!-- b001640 | prose | pages [5] -->
m

<!-- b001641 | prose | pages [5] -->
m

<!-- b001642 | prose | pages [5] -->
m

<!-- b001643 | prose | pages [5] -->
m

<!-- b001644 | prose | pages [5] -->
m

<!-- b001645 | prose | pages [5] -->
m

<!-- b001646 | prose | pages [5] -->
m

<!-- b001647 | prose | pages [5] -->
m

<!-- b001648 | prose | pages [5] -->
m

<!-- b001649 | prose | pages [5] -->
m

<!-- b001650 | prose | pages [5] -->
m

<!-- b001651 | prose | pages [5] -->
m

<!-- b001652 | prose | pages [5] -->
m

<!-- b001653 | prose | pages [5] -->
m

<!-- b001654 | prose | pages [5] -->
m

<!-- b001655 | prose | pages [5] -->
m

<!-- b001656 | prose | pages [5] -->
m

<!-- b001657 | prose | pages [5] -->
m

<!-- b001658 | prose | pages [5] -->
m

<!-- b001659 | prose | pages [5] -->
m

<!-- b001660 | prose | pages [5] -->
m

<!-- b001661 | prose | pages [5] -->
m

<!-- b001662 | prose | pages [5] -->
m

<!-- b001663 | prose | pages [5] -->
m

<!-- b001664 | prose | pages [5] -->
m

<!-- b001665 | prose | pages [5] -->
m

<!-- b001666 | prose | pages [5] -->
m

<!-- b001667 | prose | pages [5] -->
m

<!-- b001668 | prose | pages [5] -->
m

<!-- b001669 | prose | pages [5] -->
m

<!-- b001670 | prose | pages [5] -->
m

<!-- b001671 | prose | pages [5] -->
m

<!-- b001672 | prose | pages [5] -->
m

<!-- b001673 | prose | pages [5] -->
m

<!-- b001674 | prose | pages [5] -->
m

<!-- b001675 | prose | pages [5] -->
m

<!-- b001676 | prose | pages [5] -->
m

<!-- b001677 | prose | pages [5] -->
m

<!-- b001678 | prose | pages [5] -->
m

<!-- b001679 | prose | pages [5] -->
m

<!-- b001680 | prose | pages [5] -->
m

<!-- b001681 | prose | pages [5] -->
m

<!-- b001682 | prose | pages [5] -->
m

<!-- b001683 | prose | pages [5] -->
m

<!-- b001684 | prose | pages [5] -->
m

<!-- b001685 | prose | pages [5] -->
m

<!-- b001686 | prose | pages [5] -->
m

<!-- b001687 | prose | pages [5] -->
m

<!-- b001688 | prose | pages [5] -->
m

<!-- b001689 | prose | pages [5] -->
m

<!-- b001690 | prose | pages [5] -->
m

<!-- b001691 | prose | pages [5] -->
m

<!-- b001692 | prose | pages [5] -->
m

<!-- b001693 | prose | pages [5] -->
m

<!-- b001694 | prose | pages [5] -->
m

<!-- b001695 | prose | pages [5] -->
m

<!-- b001696 | prose | pages [5] -->
m

<!-- b001697 | prose | pages [5] -->
m

<!-- b001698 | prose | pages [5] -->
m

<!-- b001699 | prose | pages [5] -->
m

<!-- b001700 | prose | pages [5] -->
m

<!-- b001701 | prose | pages [5] -->
m

<!-- b001702 | prose | pages [5] -->
m

<!-- b001703 | prose | pages [5] -->
m

<!-- b001704 | prose | pages [5] -->
m

<!-- b001705 | prose | pages [5] -->
m

<!-- b001706 | prose | pages [5] -->
m

<!-- b001707 | prose | pages [5] -->
m

<!-- b001708 | prose | pages [5] -->
m

<!-- b001709 | prose | pages [5] -->
m

<!-- b001710 | prose | pages [5] -->
m

<!-- b001711 | prose | pages [5] -->
m

<!-- b001712 | prose | pages [5] -->
m

<!-- b001713 | prose | pages [5] -->
m

<!-- b001714 | prose | pages [5] -->
m

<!-- b001715 | prose | pages [5] -->
m

<!-- b001716 | prose | pages [5] -->
m

<!-- b001717 | prose | pages [5] -->
m

<!-- b001718 | prose | pages [5] -->
m

<!-- b001719 | prose | pages [5] -->
m

<!-- b001720 | prose | pages [5] -->
m

<!-- b001721 | prose | pages [5] -->
m

<!-- b001722 | prose | pages [5] -->
m

<!-- b001723 | prose | pages [5] -->
m

<!-- b001724 | prose | pages [5] -->
m

<!-- b001725 | prose | pages [5] -->
m

<!-- b001726 | prose | pages [5] -->
m

<!-- b001727 | prose | pages [5] -->
m

<!-- b001728 | prose | pages [5] -->
m

<!-- b001729 | prose | pages [5] -->
m

<!-- b001730 | prose | pages [5] -->
m

<!-- b001731 | prose | pages [5] -->
m

<!-- b001732 | prose | pages [5] -->
m

<!-- b001733 | prose | pages [5] -->
m

<!-- b001734 | prose | pages [5] -->
m

<!-- b001735 | prose | pages [5] -->
m

<!-- b001736 | prose | pages [5] -->
m

<!-- b001737 | prose | pages [5] -->
m

<!-- b001738 | prose | pages [5] -->
m

<!-- b001739 | prose | pages [5] -->
m

<!-- b001740 | prose | pages [5] -->
m

<!-- b001741 | prose | pages [5] -->
m

<!-- b001742 | prose | pages [5] -->
m

<!-- b001743 | prose | pages [5] -->
m

<!-- b001744 | prose | pages [5] -->
m

<!-- b001745 | prose | pages [5] -->
m

<!-- b001746 | prose | pages [5] -->
m

<!-- b001747 | prose | pages [5] -->
m

<!-- b001748 | prose | pages [5] -->
m

<!-- b001749 | prose | pages [5] -->
m

<!-- b001750 | prose | pages [5] -->
m

<!-- b001751 | prose | pages [5] -->
m

<!-- b001752 | prose | pages [5] -->
m

<!-- b001753 | prose | pages [5] -->
m

<!-- b001754 | prose | pages [5] -->
m

<!-- b001755 | prose | pages [5] -->
m

<!-- b001756 | prose | pages [5] -->
m

<!-- b001757 | prose | pages [5] -->
m

<!-- b001758 | prose | pages [5] -->
m

<!-- b001759 | prose | pages [5] -->
m

<!-- b001760 | furniture | pages [5] -->
m

<!-- b001761 | furniture | pages [5] -->
m

<!-- b001762 | furniture | pages [5] -->
m

<!-- b001763 | furniture | pages [5] -->
m

<!-- b001764 | furniture | pages [5] -->
m

<!-- b001765 | furniture | pages [5] -->
m

<!-- b001766 | furniture | pages [5] -->
m

<!-- b001767 | furniture | pages [5] -->
m

<!-- b001768 | furniture | pages [5] -->
m

<!-- b001769 | furniture | pages [5] -->
m

<!-- b001770 | furniture | pages [5] -->
m

<!-- b001771 | furniture | pages [5] -->
m

<!-- b001772 | furniture | pages [5] -->
m

<!-- b001773 | furniture | pages [5] -->
m

<!-- b001774 | furniture | pages [5] -->
m

<!-- b001775 | furniture | pages [5] -->
m

<!-- b001776 | furniture | pages [5] -->
m

<!-- b001777 | furniture | pages [5] -->
m

<!-- b001778 | furniture | pages [5] -->
m

<!-- b001779 | furniture | pages [5] -->
m

<!-- b001780 | furniture | pages [5] -->
m

<!-- b001781 | furniture | pages [5] -->
m

<!-- b001782 | furniture | pages [5] -->
m

<!-- b001783 | furniture | pages [5] -->
m

<!-- b001784 | furniture | pages [5] -->
m

<!-- b001785 | furniture | pages [5] -->
m

<!-- b001786 | furniture | pages [5] -->
m

<!-- b001787 | furniture | pages [5] -->
m

<!-- b001788 | furniture | pages [5] -->
m

<!-- b001789 | furniture | pages [5] -->
m

<!-- b001790 | furniture | pages [5] -->
m

<!-- b001791 | furniture | pages [5] -->
m

<!-- b001792 | furniture | pages [5] -->
m

<!-- b001793 | furniture | pages [5] -->
m

<!-- b001794 | furniture | pages [5] -->
m

<!-- b001795 | furniture | pages [5] -->
m

<!-- b001796 | furniture | pages [5] -->
m

<!-- b001797 | furniture | pages [5] -->
m

<!-- b001798 | furniture | pages [5] -->
m

<!-- b001799 | furniture | pages [5] -->
m

<!-- b001800 | furniture | pages [5] -->
m

<!-- b001801 | furniture | pages [5] -->
m

<!-- b001802 | furniture | pages [5] -->
m

<!-- b001803 | furniture | pages [5] -->
m

<!-- b001804 | furniture | pages [5] -->
m

<!-- b001805 | furniture | pages [5] -->
m

<!-- b001806 | furniture | pages [5] -->
m

<!-- b001807 | furniture | pages [5] -->
m

<!-- b001808 | furniture | pages [5] -->
m

<!-- b001809 | furniture | pages [5] -->
m

<!-- b001810 | furniture | pages [5] -->
m

<!-- b001811 | furniture | pages [5] -->
m

<!-- b001812 | furniture | pages [5] -->
m

<!-- b001813 | furniture | pages [5] -->
m

<!-- b001814 | furniture | pages [5] -->
m

<!-- b001815 | furniture | pages [5] -->
m

<!-- b001816 | furniture | pages [5] -->
m

<!-- b001817 | furniture | pages [5] -->
m

<!-- b001818 | furniture | pages [5] -->
m

<!-- b001819 | furniture | pages [5] -->
m

<!-- b001820 | furniture | pages [5] -->
m

<!-- b001821 | furniture | pages [5] -->
m

<!-- b001822 | furniture | pages [5] -->
m

<!-- b001823 | furniture | pages [5] -->
m

<!-- b001824 | furniture | pages [5] -->
m

<!-- b001825 | furniture | pages [5] -->
m

<!-- b001826 | furniture | pages [5] -->
m

<!-- b001827 | furniture | pages [5] -->
m

<!-- b001828 | furniture | pages [5] -->
m

<!-- b001829 | furniture | pages [5] -->
m

<!-- b001830 | furniture | pages [5] -->
m

<!-- b001831 | furniture | pages [5] -->
m

<!-- b001832 | furniture | pages [5] -->
m

<!-- b001833 | furniture | pages [5] -->
m

<!-- b001834 | furniture | pages [5] -->
m

<!-- b001835 | furniture | pages [5] -->
m

<!-- b001836 | furniture | pages [5] -->
m

<!-- b001837 | furniture | pages [5] -->
m

<!-- b001838 | furniture | pages [5] -->
m

<!-- b001839 | furniture | pages [5] -->
m

<!-- b001840 | furniture | pages [5] -->
m

<!-- b001841 | furniture | pages [5] -->
m

<!-- b001842 | furniture | pages [5] -->
m

<!-- b001843 | furniture | pages [5] -->
m

<!-- b001844 | furniture | pages [5] -->
m

<!-- b001845 | furniture | pages [5] -->
m

<!-- b001846 | furniture | pages [5] -->
m

<!-- b001847 | furniture | pages [5] -->
m

<!-- b001848 | furniture | pages [5] -->
m

<!-- b001849 | furniture | pages [5] -->
m

<!-- b001850 | furniture | pages [5] -->
m

<!-- b001851 | furniture | pages [5] -->
m

<!-- b001852 | furniture | pages [5] -->
m

<!-- b001853 | furniture | pages [5] -->
m

<!-- b001854 | furniture | pages [5] -->
m

<!-- b001855 | furniture | pages [5] -->
m

<!-- b001856 | furniture | pages [5] -->
m

<!-- b001857 | furniture | pages [5] -->
m

<!-- b001858 | furniture | pages [5] -->
m

<!-- b001859 | furniture | pages [5] -->
m

<!-- b001860 | furniture | pages [5] -->
m

<!-- b001861 | furniture | pages [5] -->
m

<!-- b001862 | furniture | pages [5] -->
m

<!-- b001863 | furniture | pages [5] -->
m

<!-- b001864 | furniture | pages [5] -->
m

<!-- b001865 | furniture | pages [5] -->
m

<!-- b001866 | furniture | pages [5] -->
m

<!-- b001867 | furniture | pages [5] -->
m

<!-- b001868 | furniture | pages [5] -->
m

<!-- b001869 | furniture | pages [5] -->
m

<!-- b001870 | furniture | pages [5] -->
m

<!-- b001871 | furniture | pages [5] -->
m

<!-- b001872 | furniture | pages [5] -->
m

<!-- b001873 | furniture | pages [5] -->
m

<!-- b001874 | furniture | pages [5] -->
m

<!-- b001875 | furniture | pages [5] -->
m

<!-- b001876 | furniture | pages [5] -->
m

<!-- b001877 | furniture | pages [5] -->
m

<!-- b001878 | furniture | pages [5] -->
m

<!-- b001879 | furniture | pages [5] -->
m

<!-- b001880 | furniture | pages [5] -->
m

<!-- b001881 | furniture | pages [5] -->
m

<!-- b001882 | furniture | pages [5] -->
m

<!-- b001883 | furniture | pages [5] -->
m

<!-- b001884 | furniture | pages [5] -->
m

<!-- b001885 | furniture | pages [5] -->
m

<!-- b001886 | furniture | pages [5] -->
m

<!-- b001887 | furniture | pages [5] -->
m

<!-- b001888 | furniture | pages [5] -->
m

<!-- b001889 | furniture | pages [5] -->
m

<!-- b001890 | furniture | pages [5] -->
m

<!-- b001891 | furniture | pages [5] -->
m

<!-- b001892 | furniture | pages [5] -->
m

<!-- b001893 | furniture | pages [5] -->
m

<!-- b001894 | furniture | pages [5] -->
m

<!-- b001895 | furniture | pages [5] -->
m

<!-- b001896 | furniture | pages [5] -->
m

<!-- b001897 | furniture | pages [5] -->
m

<!-- b001898 | furniture | pages [5] -->
m

<!-- b001899 | furniture | pages [5] -->
m

<!-- b001900 | furniture | pages [5] -->
m

<!-- b001901 | furniture | pages [5] -->
m

<!-- b001902 | furniture | pages [5] -->
m

<!-- b001903 | furniture | pages [5] -->
m

<!-- b001904 | furniture | pages [5] -->
m

<!-- b001905 | furniture | pages [5] -->
m

<!-- b001906 | furniture | pages [5] -->
m

<!-- b001907 | furniture | pages [5] -->
m

<!-- b001908 | furniture | pages [5] -->
m

<!-- b001909 | furniture | pages [5] -->
m

<!-- b001910 | furniture | pages [5] -->
m

<!-- b001911 | furniture | pages [5] -->
m

<!-- b001912 | furniture | pages [5] -->
m

<!-- b001913 | furniture | pages [5] -->
m

<!-- b001914 | furniture | pages [5] -->
m

<!-- b001915 | furniture | pages [5] -->
m

<!-- b001916 | furniture | pages [5] -->
m

<!-- b001917 | furniture | pages [5] -->
m

<!-- b001918 | furniture | pages [5] -->
m

<!-- b001919 | furniture | pages [5] -->
m

<!-- b001920 | furniture | pages [5] -->
m

<!-- b001921 | furniture | pages [5] -->
m

<!-- b001922 | furniture | pages [5] -->
m

<!-- b001923 | furniture | pages [5] -->
m

<!-- b001924 | furniture | pages [5] -->
m

<!-- b001925 | furniture | pages [5] -->
m

<!-- b001926 | furniture | pages [5] -->
m

<!-- b001927 | furniture | pages [5] -->
m

<!-- b001928 | furniture | pages [5] -->
m

<!-- b001929 | furniture | pages [5] -->
m

<!-- b001930 | furniture | pages [5] -->
m

<!-- b001931 | furniture | pages [5] -->
m

<!-- b001932 | furniture | pages [5] -->
m

<!-- b001933 | furniture | pages [5] -->
m

<!-- b001934 | furniture | pages [5] -->
m

<!-- b001935 | furniture | pages [5] -->
m

<!-- b001936 | furniture | pages [5] -->
m

<!-- b001937 | furniture | pages [5] -->
m

<!-- b001938 | furniture | pages [5] -->
m

<!-- b001939 | furniture | pages [5] -->
m

<!-- b001940 | furniture | pages [5] -->
m

<!-- b001941 | furniture | pages [5] -->
m

<!-- b001942 | furniture | pages [5] -->
m

<!-- b001943 | furniture | pages [5] -->
m

<!-- b001944 | furniture | pages [5] -->
m

<!-- b001945 | furniture | pages [5] -->
m

<!-- b001946 | furniture | pages [5] -->
m

<!-- b001947 | furniture | pages [5] -->
m

<!-- b001948 | furniture | pages [5] -->
m

<!-- b001949 | furniture | pages [5] -->
m

<!-- b001950 | furniture | pages [5] -->
m

<!-- b001951 | furniture | pages [5] -->
m

<!-- b001952 | furniture | pages [5] -->
m

<!-- b001953 | furniture | pages [5] -->
m

<!-- b001954 | furniture | pages [5] -->
m

<!-- b001955 | furniture | pages [5] -->
m

<!-- b001956 | furniture | pages [5] -->
m

<!-- b001957 | furniture | pages [5] -->
m

<!-- b001958 | furniture | pages [5] -->
m

<!-- b001959 | furniture | pages [5] -->
m

<!-- b001960 | furniture | pages [5] -->
m

<!-- b001961 | furniture | pages [5] -->
m

<!-- b001962 | furniture | pages [5] -->
m

<!-- b001963 | furniture | pages [5] -->
m

<!-- b001964 | furniture | pages [5] -->
m

<!-- b001965 | furniture | pages [5] -->
m

<!-- b001966 | furniture | pages [5] -->
m

<!-- b001967 | furniture | pages [5] -->
m

<!-- b001968 | furniture | pages [5] -->
m

<!-- b001969 | furniture | pages [5] -->
m

<!-- b001970 | furniture | pages [5] -->
m

<!-- b001971 | furniture | pages [5] -->
m

<!-- b001972 | furniture | pages [5] -->
m

<!-- b001973 | furniture | pages [5] -->
m

<!-- b001974 | furniture | pages [5] -->
m

<!-- b001975 | furniture | pages [5] -->
m

<!-- b001976 | furniture | pages [5] -->
m

<!-- b001977 | furniture | pages [5] -->
m

<!-- b001978 | furniture | pages [5] -->
m

<!-- b001979 | furniture | pages [5] -->
m

<!-- b001980 | furniture | pages [5] -->
m

<!-- b001981 | furniture | pages [5] -->
m

<!-- b001982 | furniture | pages [5] -->
m

<!-- b001983 | furniture | pages [5] -->
m

<!-- b001984 | furniture | pages [5] -->
m

<!-- b001985 | furniture | pages [5] -->
m

<!-- b001986 | furniture | pages [5] -->
m

<!-- b001987 | furniture | pages [5] -->
m

<!-- b001988 | furniture | pages [5] -->
m

<!-- b001989 | furniture | pages [5] -->
m

<!-- b001990 | furniture | pages [5] -->
m

<!-- b001991 | furniture | pages [5] -->
m

<!-- b001992 | furniture | pages [5] -->
m

<!-- b001993 | furniture | pages [5] -->
m

<!-- b001994 | furniture | pages [5] -->
m

<!-- b001995 | furniture | pages [5] -->
m

<!-- b001996 | furniture | pages [5] -->
m

<!-- b001997 | furniture | pages [5] -->
m

<!-- b001998 | furniture | pages [5] -->
m

<!-- b001999 | furniture | pages [5] -->
m

<!-- b002000 | furniture | pages [5] -->
m

<!-- b002001 | furniture | pages [5] -->
m

<!-- b002002 | furniture | pages [5] -->
m

<!-- b002003 | furniture | pages [5] -->
m

<!-- b002004 | furniture | pages [5] -->
m

<!-- b002005 | furniture | pages [5] -->
m

<!-- b002006 | furniture | pages [5] -->
m

<!-- b002007 | furniture | pages [5] -->
m

<!-- b002008 | furniture | pages [5] -->
m

<!-- b002009 | furniture | pages [5] -->
m

<!-- b002010 | furniture | pages [5] -->
m

<!-- b002011 | furniture | pages [5] -->
m

<!-- b002012 | furniture | pages [5] -->
m

<!-- b002013 | furniture | pages [5] -->
m

<!-- b002014 | furniture | pages [5] -->
m

<!-- b002015 | furniture | pages [5] -->
m

<!-- b002016 | furniture | pages [5] -->
m

<!-- b002017 | furniture | pages [5] -->
m

<!-- b002018 | furniture | pages [5] -->
m

<!-- b002019 | furniture | pages [5] -->
m

<!-- b002020 | furniture | pages [5] -->
m

<!-- b002021 | furniture | pages [5] -->
m

<!-- b002022 | furniture | pages [5] -->
m

<!-- b002023 | furniture | pages [5] -->
m

<!-- b002024 | furniture | pages [5] -->
m

<!-- b002025 | furniture | pages [5] -->
m

<!-- b002026 | furniture | pages [5] -->
m

<!-- b002027 | furniture | pages [5] -->
m

<!-- b002028 | furniture | pages [5] -->
m

<!-- b002029 | furniture | pages [5] -->
m

<!-- b002030 | furniture | pages [5] -->
m

<!-- b002031 | furniture | pages [5] -->
m

<!-- b002032 | furniture | pages [5] -->
m

<!-- b002033 | furniture | pages [5] -->
m

<!-- b002034 | furniture | pages [5] -->
m

<!-- b002035 | furniture | pages [5] -->
m

<!-- b002036 | furniture | pages [5] -->
m

<!-- b002037 | furniture | pages [5] -->
m

<!-- b002038 | furniture | pages [5] -->
m

<!-- b002039 | furniture | pages [5] -->
m

<!-- b002040 | furniture | pages [5] -->
m

<!-- b002041 | furniture | pages [5] -->
m

<!-- b002042 | furniture | pages [5] -->
m

<!-- b002043 | furniture | pages [5] -->
m

<!-- b002044 | furniture | pages [5] -->
m

<!-- b002045 | furniture | pages [5] -->
m

<!-- b002046 | furniture | pages [5] -->
m

<!-- b002047 | furniture | pages [5] -->
m

<!-- b002048 | furniture | pages [5] -->
m

<!-- b002049 | furniture | pages [5] -->
m

<!-- b002050 | furniture | pages [5] -->
m

<!-- b002051 | furniture | pages [5] -->
m

<!-- b002052 | furniture | pages [5] -->
m

<!-- b002053 | furniture | pages [5] -->
m

<!-- b002054 | furniture | pages [5] -->
m

<!-- b002055 | furniture | pages [5] -->
m

<!-- b002056 | furniture | pages [5] -->
m

<!-- b002057 | furniture | pages [5] -->
m

<!-- b002058 | furniture | pages [5] -->
m

<!-- b002059 | furniture | pages [5] -->
m

<!-- b002060 | furniture | pages [5] -->
m

<!-- b002061 | furniture | pages [5] -->
m

<!-- b002062 | furniture | pages [5] -->
m

<!-- b002063 | furniture | pages [5] -->
m

<!-- b002064 | furniture | pages [5] -->
m

<!-- b002065 | furniture | pages [5] -->
m

<!-- b002066 | furniture | pages [5] -->
m

<!-- b002067 | furniture | pages [5] -->
m

<!-- b002068 | furniture | pages [5] -->
m

<!-- b002069 | furniture | pages [5] -->
m

<!-- b002070 | furniture | pages [5] -->
m

<!-- b002071 | furniture | pages [5] -->
m

<!-- b002072 | furniture | pages [5] -->
m

<!-- b002073 | furniture | pages [5] -->
m

<!-- b002074 | furniture | pages [5] -->
m

<!-- b002075 | furniture | pages [5] -->
m

<!-- b002076 | furniture | pages [5] -->
m

<!-- b002077 | furniture | pages [5] -->
m

<!-- b002078 | furniture | pages [5] -->
m

<!-- b002079 | furniture | pages [5] -->
m

<!-- b002080 | furniture | pages [5] -->
m

<!-- b002081 | furniture | pages [5] -->
m

<!-- b002082 | furniture | pages [5] -->
m

<!-- b002083 | furniture | pages [5] -->
m

<!-- b002084 | furniture | pages [5] -->
m

<!-- b002085 | furniture | pages [5] -->
m

<!-- b002086 | furniture | pages [5] -->
m

<!-- b002087 | furniture | pages [5] -->
m

<!-- b002088 | furniture | pages [5] -->
m

<!-- b002089 | furniture | pages [5] -->
m

<!-- b002090 | furniture | pages [5] -->
m

<!-- b002091 | furniture | pages [5] -->
m

<!-- b002092 | furniture | pages [5] -->
m

<!-- b002093 | furniture | pages [5] -->
m

<!-- b002094 | furniture | pages [5] -->
m

<!-- b002095 | furniture | pages [5] -->
m

<!-- b002096 | furniture | pages [5] -->
m

<!-- b002097 | furniture | pages [5] -->
m

<!-- b002098 | furniture | pages [5] -->
m

<!-- b002099 | furniture | pages [5] -->
m

<!-- b002100 | furniture | pages [5] -->
m

<!-- b002101 | furniture | pages [5] -->
m

<!-- b002102 | furniture | pages [5] -->
m

<!-- b002103 | furniture | pages [5] -->
m

<!-- b002104 | furniture | pages [5] -->
m

<!-- b002105 | furniture | pages [5] -->
m

<!-- b002106 | furniture | pages [5] -->
m

<!-- b002107 | furniture | pages [5] -->
m

<!-- b002108 | furniture | pages [5] -->
m

<!-- b002109 | furniture | pages [5] -->
m

<!-- b002110 | furniture | pages [5] -->
m

<!-- b002111 | furniture | pages [5] -->
m

<!-- b002112 | furniture | pages [5] -->
m

<!-- b002113 | furniture | pages [5] -->
m

<!-- b002114 | furniture | pages [5] -->
m

<!-- b002115 | furniture | pages [5] -->
m

<!-- b002116 | furniture | pages [5] -->
m

<!-- b002117 | furniture | pages [5] -->
m

<!-- b002118 | furniture | pages [5] -->
m

<!-- b002119 | furniture | pages [5] -->
m

<!-- b002120 | furniture | pages [5] -->
m

<!-- b002121 | furniture | pages [5] -->
m

<!-- b002122 | furniture | pages [5] -->
m

<!-- b002123 | furniture | pages [5] -->
m

<!-- b002124 | furniture | pages [5] -->
m

<!-- b002125 | furniture | pages [5] -->
m

<!-- b002126 | furniture | pages [5] -->
m

<!-- b002127 | furniture | pages [5] -->
m

<!-- b002128 | furniture | pages [5] -->
m

<!-- b002129 | furniture | pages [5] -->
m

<!-- b002130 | furniture | pages [5] -->
m

<!-- b002131 | furniture | pages [5] -->
m

<!-- b002132 | furniture | pages [5] -->
m

<!-- b002133 | furniture | pages [5] -->
m

<!-- b002134 | furniture | pages [5] -->
m

<!-- b002135 | furniture | pages [5] -->
m

<!-- b002136 | furniture | pages [5] -->
m

<!-- b002137 | furniture | pages [5] -->
m

<!-- b002138 | furniture | pages [5] -->
m

<!-- b002139 | furniture | pages [5] -->
m

<!-- b002140 | furniture | pages [5] -->
m

<!-- b002141 | furniture | pages [5] -->
m

<!-- b002142 | furniture | pages [5] -->
m

<!-- b002143 | furniture | pages [5] -->
m

<!-- b002144 | furniture | pages [5] -->
m

<!-- b002145 | furniture | pages [5] -->
m

<!-- b002146 | furniture | pages [5] -->
m

<!-- b002147 | furniture | pages [5] -->
m

<!-- b002148 | furniture | pages [5] -->
m

<!-- b002149 | furniture | pages [5] -->
m

<!-- b002150 | furniture | pages [5] -->
m

<!-- b002151 | furniture | pages [5] -->
m

<!-- b002152 | furniture | pages [5] -->
m

<!-- b002153 | furniture | pages [5] -->
m

<!-- b002154 | furniture | pages [5] -->
m

<!-- b002155 | furniture | pages [5] -->
m

<!-- b002156 | furniture | pages [5] -->
m

<!-- b002157 | furniture | pages [5] -->
m

<!-- b002158 | furniture | pages [5] -->
m

<!-- b002159 | furniture | pages [5] -->
m

<!-- b002160 | furniture | pages [5] -->
m

<!-- b002161 | furniture | pages [5] -->
m

<!-- b002162 | furniture | pages [5] -->
m

<!-- b002163 | furniture | pages [6] -->
Team#2507817                                                             Page 6 of 25

<!-- b002164 | prose | pages [6] -->


<!-- b002165 | prose | pages [6] -->
'

<!-- b002166 | furniture | pages [6] -->


<!-- b002167 | prose | pages [6] -->
x

<!-- b002168 | prose | pages [6] -->


<!-- b002169 | prose | pages [6] -->
( ( x x x )

<!-- b002170 | furniture | pages [6] -->


<!-- b002171 | prose | pages [6] -->
(0)

<!-- b002172 | prose | pages [6] -->
SD

<!-- b002173 | prose | pages [6] -->
 Conversion of country and region names: To build the model, we utilized two files:

<!-- b002174 | prose | pages [6] -->
"summerOly_medal_counts.csv" and "summerOly_athletes.csv." Since these files represent countries in different formats, we employed an ISO mapping table to convert the full names of all countries and regions into standardized codes prior to data integration. Data for countries that were dissolved or banned, such as the USSR and Russia, was excluded.

<!-- b002175 | prose | pages [6] -->
 Athlete & Event Counts: Athletes and events are categorized by country and year and

<!-- b002176 | prose | pages [6] -->
their total value is calculated. Individual Neutral Athletes (AIN) sport results do not represent any one country and should also be cleared in the forecast.

<!-- b002177 | heading | pages [6] -->
5 Task 1 Predicting Gold & Total Medals Based on GSRF Model

<!-- b002178 | heading | pages [6] -->
5.1 GSRF Prediction Model

<!-- b002179 | heading | pages [6] -->
5.1.1 ARIMA Model Initial Prediction

<!-- b002180 | prose | pages [6] -->
The ARIMA model is widely used in time series analysis for its flexibility and powerful forecasting ability to adapt to a wide range of data characteristics and make accurate predictions.The ARIMA model integrates autoregressive (AR) and moving average (MA) methods and incorporates differencing (I) to enhance data smoothing. By examining autocorrelation in historical data, the model assumes that future trends will mimic historical patterns and thus predicts future data points.ARIMA (p, d, q) can be expressed as equation (2):

<!-- b002181 | prose | pages [6] -->
        

<!-- b002182 | furniture | pages [6] -->


<!-- b002183 | prose | pages [6] -->
X c X X   t 1 t 1 2 t 2 p

<!-- b002184 | prose | pages [6] -->
Among them:

<!-- b002185 | prose | pages [6] -->
         

<!-- b002186 | furniture | pages [6] -->


<!-- b002187 | prose | pages [6] -->
(1) X X     t t p 1 t 1 2 t 2 q t q t

<!-- b002188 | prose | pages [6] -->
X represents the time series data we are considering;  t

<!-- b002189 | prose | pages [6] -->
c is a constant term; 

<!-- b002190 | prose | pages [6] -->
are the parameters of the AR model, which are used to describe the relationship 

<!-- b002191 | prose | pages [6] -->
m

<!-- b002192 | prose | pages [6] -->
m

<!-- b002193 | prose | pages [6] -->
m

<!-- b002194 | prose | pages [6] -->
m

<!-- b002195 | prose | pages [6] -->
m

<!-- b002196 | prose | pages [6] -->
m

<!-- b002197 | prose | pages [6] -->
m

<!-- b002198 | prose | pages [6] -->
m

<!-- b002199 | prose | pages [6] -->
m

<!-- b002200 | prose | pages [6] -->
m

<!-- b002201 | prose | pages [6] -->
m

<!-- b002202 | prose | pages [6] -->
m

<!-- b002203 | prose | pages [6] -->
m

<!-- b002204 | prose | pages [6] -->
m

<!-- b002205 | prose | pages [6] -->
m

<!-- b002206 | prose | pages [6] -->
m

<!-- b002207 | prose | pages [6] -->
m

<!-- b002208 | prose | pages [6] -->
m

<!-- b002209 | prose | pages [6] -->
m

<!-- b002210 | prose | pages [6] -->
m

<!-- b002211 | prose | pages [6] -->
m

<!-- b002212 | prose | pages [6] -->
m

<!-- b002213 | prose | pages [6] -->
, ,...,

<!-- b002214 | prose | pages [6] -->
m

<!-- b002215 | prose | pages [6] -->
m

<!-- b002216 | prose | pages [6] -->
m

<!-- b002217 | prose | pages [6] -->
m

<!-- b002218 | prose | pages [6] -->
m

<!-- b002219 | prose | pages [6] -->
m

<!-- b002220 | prose | pages [6] -->
m

<!-- b002221 | prose | pages [6] -->
m

<!-- b002222 | prose | pages [6] -->
m

<!-- b002223 | prose | pages [6] -->
m

<!-- b002224 | prose | pages [6] -->
m

<!-- b002225 | prose | pages [6] -->
m

<!-- b002226 | prose | pages [6] -->
m

<!-- b002227 | prose | pages [6] -->
m

<!-- b002228 | prose | pages [6] -->
m

<!-- b002229 | prose | pages [6] -->
m

<!-- b002230 | prose | pages [6] -->


<!-- b002231 | prose | pages [6] -->
m

<!-- b002232 | prose | pages [6] -->
m

<!-- b002233 | prose | pages [6] -->
m

<!-- b002234 | prose | pages [6] -->
m

<!-- b002235 | prose | pages [6] -->
m

<!-- b002236 | prose | pages [6] -->
m

<!-- b002237 | prose | pages [6] -->
m

<!-- b002238 | prose | pages [6] -->
m

<!-- b002239 | prose | pages [6] -->
m

<!-- b002240 | prose | pages [6] -->
m

<!-- b002241 | prose | pages [6] -->
m

<!-- b002242 | prose | pages [6] -->
m

<!-- b002243 | prose | pages [6] -->
m

<!-- b002244 | prose | pages [6] -->
m

<!-- b002245 | prose | pages [6] -->
m

<!-- b002246 | prose | pages [6] -->
m

<!-- b002247 | prose | pages [6] -->
m

<!-- b002248 | prose | pages [6] -->
m

<!-- b002249 | prose | pages [6] -->
m

<!-- b002250 | prose | pages [6] -->
m

<!-- b002251 | prose | pages [6] -->
m

<!-- b002252 | prose | pages [6] -->
m

<!-- b002253 | prose | pages [6] -->
m

<!-- b002254 | prose | pages [6] -->
m

<!-- b002255 | prose | pages [6] -->
m

<!-- b002256 | prose | pages [6] -->
m

<!-- b002257 | prose | pages [6] -->
m

<!-- b002258 | prose | pages [6] -->
m

<!-- b002259 | prose | pages [6] -->
m

<!-- b002260 | prose | pages [6] -->
m

<!-- b002261 | prose | pages [6] -->
m

<!-- b002262 | prose | pages [6] -->
m

<!-- b002263 | prose | pages [6] -->
m

<!-- b002264 | prose | pages [6] -->
m

<!-- b002265 | prose | pages [6] -->
m

<!-- b002266 | prose | pages [6] -->
m

<!-- b002267 | prose | pages [6] -->
m

<!-- b002268 | prose | pages [6] -->
m

<!-- b002269 | prose | pages [6] -->
m

<!-- b002270 | prose | pages [6] -->
m

<!-- b002271 | prose | pages [6] -->
m

<!-- b002272 | prose | pages [6] -->
m

<!-- b002273 | prose | pages [6] -->
m

<!-- b002274 | prose | pages [6] -->
m

<!-- b002275 | prose | pages [6] -->
m

<!-- b002276 | prose | pages [6] -->
m

<!-- b002277 | prose | pages [6] -->
m

<!-- b002278 | prose | pages [6] -->
m

<!-- b002279 | prose | pages [6] -->
m

<!-- b002280 | prose | pages [6] -->
m

<!-- b002281 | prose | pages [6] -->
m

<!-- b002282 | prose | pages [6] -->
m

<!-- b002283 | prose | pages [6] -->
m

<!-- b002284 | prose | pages [6] -->
m

<!-- b002285 | prose | pages [6] -->
m

<!-- b002286 | prose | pages [6] -->
m

<!-- b002287 | prose | pages [6] -->
m

<!-- b002288 | prose | pages [6] -->
1 2 p

<!-- b002289 | prose | pages [6] -->
m

<!-- b002290 | prose | pages [6] -->
m

<!-- b002291 | prose | pages [6] -->
m

<!-- b002292 | prose | pages [6] -->
m

<!-- b002293 | prose | pages [6] -->
m

<!-- b002294 | prose | pages [6] -->
m

<!-- b002295 | prose | pages [6] -->
m

<!-- b002296 | prose | pages [6] -->
m

<!-- b002297 | prose | pages [6] -->
m

<!-- b002298 | prose | pages [6] -->
m

<!-- b002299 | prose | pages [6] -->
m

<!-- b002300 | prose | pages [6] -->
m

<!-- b002301 | prose | pages [6] -->
m

<!-- b002302 | prose | pages [6] -->
m

<!-- b002303 | prose | pages [6] -->
m

<!-- b002304 | prose | pages [6] -->
m

<!-- b002305 | prose | pages [6] -->
m

<!-- b002306 | prose | pages [6] -->
m

<!-- b002307 | prose | pages [6] -->
m

<!-- b002308 | prose | pages [6] -->
m

<!-- b002309 | prose | pages [6] -->
m

<!-- b002310 | prose | pages [6] -->
m

<!-- b002311 | prose | pages [6] -->
m

<!-- b002312 | prose | pages [6] -->
m

<!-- b002313 | prose | pages [6] -->
m

<!-- b002314 | prose | pages [6] -->
m

<!-- b002315 | prose | pages [6] -->
m

<!-- b002316 | prose | pages [6] -->
m

<!-- b002317 | prose | pages [6] -->
m

<!-- b002318 | prose | pages [6] -->
m

<!-- b002319 | prose | pages [6] -->
m

<!-- b002320 | prose | pages [6] -->
m

<!-- b002321 | prose | pages [6] -->
m

<!-- b002322 | prose | pages [6] -->
m

<!-- b002323 | prose | pages [6] -->
m

<!-- b002324 | prose | pages [6] -->
m

<!-- b002325 | prose | pages [6] -->
m

<!-- b002326 | prose | pages [6] -->
m

<!-- b002327 | prose | pages [6] -->
m

<!-- b002328 | prose | pages [6] -->
m

<!-- b002329 | prose | pages [6] -->
m

<!-- b002330 | prose | pages [6] -->
m

<!-- b002331 | prose | pages [6] -->
m

<!-- b002332 | prose | pages [6] -->
m

<!-- b002333 | prose | pages [6] -->
m

<!-- b002334 | prose | pages [6] -->
m

<!-- b002335 | prose | pages [6] -->
m

<!-- b002336 | prose | pages [6] -->
m

<!-- b002337 | prose | pages [6] -->
m

<!-- b002338 | prose | pages [6] -->
m

<!-- b002339 | prose | pages [6] -->
m

<!-- b002340 | prose | pages [6] -->
m

<!-- b002341 | prose | pages [6] -->
m

<!-- b002342 | prose | pages [6] -->
m

<!-- b002343 | prose | pages [6] -->
m

<!-- b002344 | prose | pages [6] -->
m

<!-- b002345 | prose | pages [6] -->
m

<!-- b002346 | prose | pages [6] -->
m

<!-- b002347 | prose | pages [6] -->
m

<!-- b002348 | prose | pages [6] -->
m

<!-- b002349 | prose | pages [6] -->
m

<!-- b002350 | prose | pages [6] -->
m

<!-- b002351 | prose | pages [6] -->
m

<!-- b002352 | prose | pages [6] -->
m

<!-- b002353 | prose | pages [6] -->
m

<!-- b002354 | prose | pages [6] -->
m

<!-- b002355 | prose | pages [6] -->
m

<!-- b002356 | prose | pages [6] -->
m

<!-- b002357 | prose | pages [6] -->
m

<!-- b002358 | prose | pages [6] -->
m

<!-- b002359 | prose | pages [6] -->
m

<!-- b002360 | prose | pages [6] -->
m

<!-- b002361 | prose | pages [6] -->
m

<!-- b002362 | prose | pages [6] -->
m

<!-- b002363 | prose | pages [6] -->
m

<!-- b002364 | prose | pages [6] -->
m

<!-- b002365 | prose | pages [6] -->
m

<!-- b002366 | prose | pages [6] -->
m

<!-- b002367 | prose | pages [6] -->
m

<!-- b002368 | prose | pages [6] -->
m

<!-- b002369 | prose | pages [6] -->
m

<!-- b002370 | prose | pages [6] -->
m

<!-- b002371 | prose | pages [6] -->
m

<!-- b002372 | prose | pages [6] -->
m

<!-- b002373 | prose | pages [6] -->
m

<!-- b002374 | prose | pages [6] -->
m

<!-- b002375 | prose | pages [6] -->
m

<!-- b002376 | prose | pages [6] -->
m

<!-- b002377 | prose | pages [6] -->
m

<!-- b002378 | prose | pages [6] -->
m

<!-- b002379 | prose | pages [6] -->
m

<!-- b002380 | prose | pages [6] -->
m

<!-- b002381 | prose | pages [6] -->
m

<!-- b002382 | prose | pages [6] -->
m

<!-- b002383 | prose | pages [6] -->
m

<!-- b002384 | prose | pages [6] -->
m

<!-- b002385 | prose | pages [6] -->
m

<!-- b002386 | prose | pages [6] -->
m

<!-- b002387 | prose | pages [6] -->
m

<!-- b002388 | prose | pages [6] -->
m

<!-- b002389 | prose | pages [6] -->
m

<!-- b002390 | prose | pages [6] -->
m

<!-- b002391 | prose | pages [6] -->
m

<!-- b002392 | prose | pages [6] -->
m

<!-- b002393 | prose | pages [6] -->
m

<!-- b002394 | prose | pages [6] -->
m

<!-- b002395 | prose | pages [6] -->
m

<!-- b002396 | prose | pages [6] -->
m

<!-- b002397 | prose | pages [6] -->
m

<!-- b002398 | prose | pages [6] -->
m

<!-- b002399 | prose | pages [6] -->
m

<!-- b002400 | prose | pages [6] -->
m

<!-- b002401 | prose | pages [6] -->
m

<!-- b002402 | prose | pages [6] -->
m

<!-- b002403 | prose | pages [6] -->
m

<!-- b002404 | prose | pages [6] -->
m

<!-- b002405 | prose | pages [6] -->
m

<!-- b002406 | prose | pages [6] -->
m

<!-- b002407 | prose | pages [6] -->
m

<!-- b002408 | prose | pages [6] -->
m

<!-- b002409 | prose | pages [6] -->
m

<!-- b002410 | prose | pages [6] -->
m

<!-- b002411 | prose | pages [6] -->
m

<!-- b002412 | prose | pages [6] -->
m

<!-- b002413 | prose | pages [6] -->
m

<!-- b002414 | prose | pages [6] -->
m

<!-- b002415 | prose | pages [6] -->
m

<!-- b002416 | prose | pages [6] -->
m

<!-- b002417 | prose | pages [6] -->
m

<!-- b002418 | prose | pages [6] -->
m

<!-- b002419 | prose | pages [6] -->
m

<!-- b002420 | prose | pages [6] -->
m

<!-- b002421 | prose | pages [6] -->
m

<!-- b002422 | prose | pages [6] -->
m

<!-- b002423 | prose | pages [6] -->
m

<!-- b002424 | prose | pages [6] -->
m

<!-- b002425 | prose | pages [6] -->
m

<!-- b002426 | prose | pages [6] -->
m

<!-- b002427 | prose | pages [6] -->
m

<!-- b002428 | prose | pages [6] -->
m

<!-- b002429 | prose | pages [6] -->
m

<!-- b002430 | prose | pages [6] -->
m

<!-- b002431 | prose | pages [6] -->
m

<!-- b002432 | prose | pages [6] -->
m

<!-- b002433 | prose | pages [6] -->
m

<!-- b002434 | prose | pages [6] -->
m

<!-- b002435 | prose | pages [6] -->
m

<!-- b002436 | prose | pages [6] -->
m

<!-- b002437 | prose | pages [6] -->
m

<!-- b002438 | prose | pages [6] -->
m

<!-- b002439 | prose | pages [6] -->
m

<!-- b002440 | prose | pages [6] -->
m

<!-- b002441 | prose | pages [6] -->
m

<!-- b002442 | prose | pages [6] -->
m

<!-- b002443 | prose | pages [6] -->
m

<!-- b002444 | prose | pages [6] -->
m

<!-- b002445 | prose | pages [6] -->
m

<!-- b002446 | prose | pages [6] -->
m

<!-- b002447 | prose | pages [6] -->
m

<!-- b002448 | prose | pages [6] -->
m

<!-- b002449 | prose | pages [6] -->
m

<!-- b002450 | prose | pages [6] -->
m

<!-- b002451 | prose | pages [6] -->
m

<!-- b002452 | prose | pages [6] -->
m

<!-- b002453 | prose | pages [6] -->
m

<!-- b002454 | prose | pages [6] -->
m

<!-- b002455 | prose | pages [6] -->
m

<!-- b002456 | prose | pages [6] -->
between the current value and the value at the past p time points;

<!-- b002457 | prose | pages [6] -->
m

<!-- b002458 | prose | pages [6] -->
m

<!-- b002459 | prose | pages [6] -->
m

<!-- b002460 | prose | pages [6] -->
m

<!-- b002461 | prose | pages [6] -->
m

<!-- b002462 | prose | pages [6] -->
m

<!-- b002463 | prose | pages [6] -->
m

<!-- b002464 | prose | pages [6] -->
m

<!-- b002465 | prose | pages [6] -->
m

<!-- b002466 | prose | pages [6] -->
m

<!-- b002467 | prose | pages [6] -->
m

<!-- b002468 | prose | pages [6] -->
m

<!-- b002469 | prose | pages [6] -->
m

<!-- b002470 | prose | pages [6] -->
m

<!-- b002471 | prose | pages [6] -->
m

<!-- b002472 | prose | pages [6] -->
m

<!-- b002473 | prose | pages [6] -->
m

<!-- b002474 | prose | pages [6] -->
m

<!-- b002475 | prose | pages [6] -->
m

<!-- b002476 | prose | pages [6] -->
m

<!-- b002477 | prose | pages [6] -->
m

<!-- b002478 | prose | pages [6] -->
m

<!-- b002479 | prose | pages [6] -->
m

<!-- b002480 | prose | pages [6] -->
m

<!-- b002481 | prose | pages [6] -->
m

<!-- b002482 | prose | pages [6] -->
m

<!-- b002483 | prose | pages [6] -->
m

<!-- b002484 | prose | pages [6] -->
m

<!-- b002485 | prose | pages [6] -->
m

<!-- b002486 | prose | pages [6] -->
m

<!-- b002487 | prose | pages [6] -->
m

<!-- b002488 | prose | pages [6] -->
m

<!-- b002489 | prose | pages [6] -->
m

<!-- b002490 | prose | pages [6] -->
m

<!-- b002491 | prose | pages [6] -->
m

<!-- b002492 | prose | pages [6] -->
m

<!-- b002493 | prose | pages [6] -->
m

<!-- b002494 | prose | pages [6] -->
m

<!-- b002495 | prose | pages [6] -->
m

<!-- b002496 | prose | pages [6] -->
m

<!-- b002497 | prose | pages [6] -->
m

<!-- b002498 | prose | pages [6] -->
m

<!-- b002499 | prose | pages [6] -->
m

<!-- b002500 | prose | pages [6] -->
m

<!-- b002501 | prose | pages [6] -->
m

<!-- b002502 | prose | pages [6] -->
m

<!-- b002503 | prose | pages [6] -->
m

<!-- b002504 | prose | pages [6] -->
m

<!-- b002505 | prose | pages [6] -->
m

<!-- b002506 | prose | pages [6] -->
m

<!-- b002507 | prose | pages [6] -->
m

<!-- b002508 | prose | pages [6] -->
m

<!-- b002509 | prose | pages [6] -->
m

<!-- b002510 | prose | pages [6] -->
m

<!-- b002511 | prose | pages [6] -->
m

<!-- b002512 | prose | pages [6] -->
m

<!-- b002513 | prose | pages [6] -->
m

<!-- b002514 | prose | pages [6] -->
m

<!-- b002515 | prose | pages [6] -->
m

<!-- b002516 | prose | pages [6] -->
m

<!-- b002517 | prose | pages [6] -->
m

<!-- b002518 | prose | pages [6] -->
m

<!-- b002519 | prose | pages [6] -->
m

<!-- b002520 | prose | pages [6] -->
m

<!-- b002521 | prose | pages [6] -->
m

<!-- b002522 | prose | pages [6] -->
m

<!-- b002523 | prose | pages [6] -->
m

<!-- b002524 | prose | pages [6] -->
m

<!-- b002525 | prose | pages [6] -->
m

<!-- b002526 | prose | pages [6] -->
m

<!-- b002527 | prose | pages [6] -->
m

<!-- b002528 | prose | pages [6] -->
m

<!-- b002529 | prose | pages [6] -->
m

<!-- b002530 | prose | pages [6] -->
m

<!-- b002531 | prose | pages [6] -->
m

<!-- b002532 | prose | pages [6] -->
m

<!-- b002533 | prose | pages [6] -->
m

<!-- b002534 | prose | pages [6] -->
m

<!-- b002535 | prose | pages [6] -->
m

<!-- b002536 | prose | pages [6] -->
m

<!-- b002537 | prose | pages [6] -->
m

<!-- b002538 | prose | pages [6] -->
m

<!-- b002539 | prose | pages [6] -->
m

<!-- b002540 | prose | pages [6] -->
m

<!-- b002541 | prose | pages [6] -->
m

<!-- b002542 | prose | pages [6] -->
m

<!-- b002543 | prose | pages [6] -->
m

<!-- b002544 | prose | pages [6] -->
m

<!-- b002545 | prose | pages [6] -->
m

<!-- b002546 | prose | pages [6] -->
m

<!-- b002547 | prose | pages [6] -->
m

<!-- b002548 | prose | pages [6] -->
m

<!-- b002549 | prose | pages [6] -->
m

<!-- b002550 | prose | pages [6] -->
m

<!-- b002551 | prose | pages [6] -->
m

<!-- b002552 | prose | pages [6] -->
m

<!-- b002553 | prose | pages [6] -->
m

<!-- b002554 | prose | pages [6] -->
m

<!-- b002555 | prose | pages [6] -->
m

<!-- b002556 | prose | pages [6] -->
m

<!-- b002557 | prose | pages [6] -->
m

<!-- b002558 | prose | pages [6] -->
m

<!-- b002559 | prose | pages [6] -->
m

<!-- b002560 | prose | pages [6] -->
m

<!-- b002561 | prose | pages [6] -->
m

<!-- b002562 | prose | pages [6] -->
m

<!-- b002563 | prose | pages [6] -->
m

<!-- b002564 | prose | pages [6] -->
m

<!-- b002565 | prose | pages [6] -->
m

<!-- b002566 | prose | pages [6] -->
m

<!-- b002567 | prose | pages [6] -->
m

<!-- b002568 | prose | pages [6] -->
m

<!-- b002569 | prose | pages [6] -->
m

<!-- b002570 | prose | pages [6] -->
m

<!-- b002571 | prose | pages [6] -->
m

<!-- b002572 | prose | pages [6] -->
m

<!-- b002573 | prose | pages [6] -->
m

<!-- b002574 | prose | pages [6] -->
m

<!-- b002575 | prose | pages [6] -->
m

<!-- b002576 | prose | pages [6] -->
m

<!-- b002577 | prose | pages [6] -->
m

<!-- b002578 | prose | pages [6] -->
m

<!-- b002579 | prose | pages [6] -->
m

<!-- b002580 | prose | pages [6] -->
m

<!-- b002581 | prose | pages [6] -->
m

<!-- b002582 | prose | pages [6] -->
m

<!-- b002583 | prose | pages [6] -->
m

<!-- b002584 | prose | pages [6] -->
m

<!-- b002585 | prose | pages [6] -->
m

<!-- b002586 | prose | pages [6] -->
m

<!-- b002587 | prose | pages [6] -->
m

<!-- b002588 | prose | pages [6] -->
m

<!-- b002589 | prose | pages [6] -->
m

<!-- b002590 | prose | pages [6] -->
m

<!-- b002591 | prose | pages [6] -->
m

<!-- b002592 | prose | pages [6] -->
m

<!-- b002593 | prose | pages [6] -->
m

<!-- b002594 | prose | pages [6] -->
m

<!-- b002595 | prose | pages [6] -->
m

<!-- b002596 | prose | pages [6] -->
m

<!-- b002597 | prose | pages [6] -->
m

<!-- b002598 | prose | pages [6] -->
m

<!-- b002599 | prose | pages [6] -->
m

<!-- b002600 | prose | pages [6] -->
m

<!-- b002601 | prose | pages [6] -->
m

<!-- b002602 | prose | pages [6] -->
m

<!-- b002603 | prose | pages [6] -->
m

<!-- b002604 | prose | pages [6] -->
m

<!-- b002605 | prose | pages [6] -->
m

<!-- b002606 | prose | pages [6] -->
m

<!-- b002607 | prose | pages [6] -->
m

<!-- b002608 | prose | pages [6] -->
m

<!-- b002609 | prose | pages [6] -->
m

<!-- b002610 | prose | pages [6] -->
m

<!-- b002611 | prose | pages [6] -->
m

<!-- b002612 | prose | pages [6] -->
m

<!-- b002613 | prose | pages [6] -->
m

<!-- b002614 | prose | pages [6] -->
m

<!-- b002615 | prose | pages [6] -->
m

<!-- b002616 | prose | pages [6] -->
m

<!-- b002617 | prose | pages [6] -->
m

<!-- b002618 | prose | pages [6] -->
m

<!-- b002619 | prose | pages [6] -->
m

<!-- b002620 | prose | pages [6] -->
m

<!-- b002621 | prose | pages [6] -->
m

<!-- b002622 | prose | pages [6] -->
m

<!-- b002623 | prose | pages [6] -->
m

<!-- b002624 | prose | pages [6] -->
m

<!-- b002625 | prose | pages [6] -->
m

<!-- b002626 | prose | pages [6] -->
m

<!-- b002627 | prose | pages [6] -->
m

<!-- b002628 | prose | pages [6] -->
m

<!-- b002629 | prose | pages [6] -->
m

<!-- b002630 | prose | pages [6] -->
m

<!-- b002631 | prose | pages [6] -->
m

<!-- b002632 | prose | pages [6] -->
m

<!-- b002633 | prose | pages [6] -->
m

<!-- b002634 | prose | pages [6] -->
m

<!-- b002635 | prose | pages [6] -->
m

<!-- b002636 | prose | pages [6] -->
m

<!-- b002637 | prose | pages [6] -->
m

<!-- b002638 | prose | pages [6] -->
m

<!-- b002639 | prose | pages [6] -->
m

<!-- b002640 | prose | pages [6] -->
m

<!-- b002641 | prose | pages [6] -->
m

<!-- b002642 | prose | pages [6] -->
m

<!-- b002643 | prose | pages [6] -->
m

<!-- b002644 | prose | pages [6] -->
m

<!-- b002645 | prose | pages [6] -->
m

<!-- b002646 | prose | pages [6] -->
m

<!-- b002647 | prose | pages [6] -->
m

<!-- b002648 | prose | pages [6] -->
m

<!-- b002649 | prose | pages [6] -->
m

<!-- b002650 | prose | pages [6] -->
m

<!-- b002651 | prose | pages [6] -->
m

<!-- b002652 | prose | pages [6] -->
m

<!-- b002653 | prose | pages [6] -->
m

<!-- b002654 | prose | pages [6] -->
m

<!-- b002655 | prose | pages [6] -->
m

<!-- b002656 | prose | pages [6] -->
m

<!-- b002657 | prose | pages [6] -->
m

<!-- b002658 | prose | pages [6] -->
m

<!-- b002659 | prose | pages [6] -->
m

<!-- b002660 | prose | pages [6] -->
m

<!-- b002661 | prose | pages [6] -->
m

<!-- b002662 | prose | pages [6] -->
m

<!-- b002663 | prose | pages [6] -->
m

<!-- b002664 | prose | pages [6] -->
m

<!-- b002665 | prose | pages [6] -->
m

<!-- b002666 | prose | pages [6] -->
m

<!-- b002667 | prose | pages [6] -->
m

<!-- b002668 | prose | pages [6] -->
m

<!-- b002669 | prose | pages [6] -->
m

<!-- b002670 | prose | pages [6] -->
m

<!-- b002671 | prose | pages [6] -->
m

<!-- b002672 | prose | pages [6] -->
m

<!-- b002673 | prose | pages [6] -->
m

<!-- b002674 | prose | pages [6] -->
m

<!-- b002675 | prose | pages [6] -->
m

<!-- b002676 | prose | pages [6] -->
m

<!-- b002677 | prose | pages [6] -->
m

<!-- b002678 | prose | pages [6] -->
m

<!-- b002679 | prose | pages [6] -->
m

<!-- b002680 | prose | pages [6] -->
m

<!-- b002681 | prose | pages [6] -->
m

<!-- b002682 | prose | pages [6] -->
m

<!-- b002683 | prose | pages [6] -->
m

<!-- b002684 | prose | pages [6] -->
m

<!-- b002685 | prose | pages [6] -->
m

<!-- b002686 | prose | pages [6] -->
m

<!-- b002687 | prose | pages [6] -->
m

<!-- b002688 | prose | pages [6] -->
m

<!-- b002689 | prose | pages [6] -->
m

<!-- b002690 | prose | pages [6] -->
m

<!-- b002691 | prose | pages [6] -->
m

<!-- b002692 | prose | pages [6] -->
m

<!-- b002693 | prose | pages [6] -->
m

<!-- b002694 | prose | pages [6] -->
m

<!-- b002695 | prose | pages [6] -->
m

<!-- b002696 | prose | pages [6] -->


<!-- b002697 | prose | pages [6] -->
m

<!-- b002698 | prose | pages [6] -->
m

<!-- b002699 | prose | pages [6] -->
m

<!-- b002700 | prose | pages [6] -->
m

<!-- b002701 | prose | pages [6] -->
m

<!-- b002702 | prose | pages [6] -->
m

<!-- b002703 | prose | pages [6] -->
m

<!-- b002704 | prose | pages [6] -->
m

<!-- b002705 | prose | pages [6] -->
m

<!-- b002706 | prose | pages [6] -->
m

<!-- b002707 | prose | pages [6] -->
m

<!-- b002708 | prose | pages [6] -->
m

<!-- b002709 | prose | pages [6] -->
m

<!-- b002710 | prose | pages [6] -->
m

<!-- b002711 | prose | pages [6] -->
m

<!-- b002712 | prose | pages [6] -->
 

<!-- b002713 | prose | pages [6] -->
m

<!-- b002714 | prose | pages [6] -->
m

<!-- b002715 | prose | pages [6] -->
m

<!-- b002716 | prose | pages [6] -->
m

<!-- b002717 | prose | pages [6] -->
m

<!-- b002718 | prose | pages [6] -->
m

<!-- b002719 | prose | pages [6] -->
m

<!-- b002720 | prose | pages [6] -->
m

<!-- b002721 | prose | pages [6] -->
m

<!-- b002722 | prose | pages [6] -->
m

<!-- b002723 | prose | pages [6] -->
m

<!-- b002724 | prose | pages [6] -->
m

<!-- b002725 | prose | pages [6] -->
m

<!-- b002726 | prose | pages [6] -->
m

<!-- b002727 | prose | pages [6] -->
m

<!-- b002728 | prose | pages [6] -->
m

<!-- b002729 | prose | pages [6] -->
are the parameters of the MA model that are used to describe the relationship , ,

<!-- b002730 | prose | pages [6] -->
m

<!-- b002731 | prose | pages [6] -->
m

<!-- b002732 | prose | pages [6] -->
m

<!-- b002733 | prose | pages [6] -->
m

<!-- b002734 | prose | pages [6] -->
m

<!-- b002735 | prose | pages [6] -->
m

<!-- b002736 | prose | pages [6] -->
m

<!-- b002737 | prose | pages [6] -->
m

<!-- b002738 | prose | pages [6] -->
m

<!-- b002739 | prose | pages [6] -->


<!-- b002740 | prose | pages [6] -->
m

<!-- b002741 | prose | pages [6] -->
m

<!-- b002742 | prose | pages [6] -->
m

<!-- b002743 | prose | pages [6] -->
m

<!-- b002744 | prose | pages [6] -->
m

<!-- b002745 | prose | pages [6] -->
m

<!-- b002746 | prose | pages [6] -->
m

<!-- b002747 | prose | pages [6] -->
m

<!-- b002748 | prose | pages [6] -->
m

<!-- b002749 | prose | pages [6] -->
m

<!-- b002750 | prose | pages [6] -->
m

<!-- b002751 | prose | pages [6] -->
m

<!-- b002752 | prose | pages [6] -->
m

<!-- b002753 | prose | pages [6] -->
m

<!-- b002754 | prose | pages [6] -->
m

<!-- b002755 | prose | pages [6] -->
m

<!-- b002756 | prose | pages [6] -->
m

<!-- b002757 | prose | pages [6] -->
m

<!-- b002758 | prose | pages [6] -->
m

<!-- b002759 | prose | pages [6] -->
m

<!-- b002760 | prose | pages [6] -->
m

<!-- b002761 | prose | pages [6] -->
m

<!-- b002762 | prose | pages [6] -->
m

<!-- b002763 | prose | pages [6] -->
m

<!-- b002764 | prose | pages [6] -->
m

<!-- b002765 | prose | pages [6] -->
m

<!-- b002766 | prose | pages [6] -->
m

<!-- b002767 | prose | pages [6] -->
m

<!-- b002768 | prose | pages [6] -->
m

<!-- b002769 | prose | pages [6] -->
m

<!-- b002770 | prose | pages [6] -->
m

<!-- b002771 | prose | pages [6] -->
m

<!-- b002772 | prose | pages [6] -->
m

<!-- b002773 | prose | pages [6] -->
m

<!-- b002774 | prose | pages [6] -->
m

<!-- b002775 | prose | pages [6] -->
m

<!-- b002776 | prose | pages [6] -->
m

<!-- b002777 | prose | pages [6] -->
m

<!-- b002778 | prose | pages [6] -->
m

<!-- b002779 | prose | pages [6] -->
m

<!-- b002780 | prose | pages [6] -->
m

<!-- b002781 | prose | pages [6] -->
m

<!-- b002782 | prose | pages [6] -->
m

<!-- b002783 | prose | pages [6] -->
m

<!-- b002784 | prose | pages [6] -->
m

<!-- b002785 | prose | pages [6] -->
m

<!-- b002786 | prose | pages [6] -->
m

<!-- b002787 | prose | pages [6] -->
m

<!-- b002788 | prose | pages [6] -->
m

<!-- b002789 | prose | pages [6] -->
m

<!-- b002790 | prose | pages [6] -->
m

<!-- b002791 | prose | pages [6] -->
m

<!-- b002792 | prose | pages [6] -->
m

<!-- b002793 | prose | pages [6] -->
m

<!-- b002794 | prose | pages [6] -->
m

<!-- b002795 | prose | pages [6] -->
m

<!-- b002796 | prose | pages [6] -->
m

<!-- b002797 | prose | pages [6] -->
m

<!-- b002798 | prose | pages [6] -->
m

<!-- b002799 | prose | pages [6] -->
m

<!-- b002800 | prose | pages [6] -->
m

<!-- b002801 | prose | pages [6] -->
m

<!-- b002802 | prose | pages [6] -->
m

<!-- b002803 | prose | pages [6] -->
m

<!-- b002804 | prose | pages [6] -->
m

<!-- b002805 | prose | pages [6] -->
m

<!-- b002806 | prose | pages [6] -->
m

<!-- b002807 | prose | pages [6] -->
m

<!-- b002808 | prose | pages [6] -->
m

<!-- b002809 | prose | pages [6] -->
1 2 q

<!-- b002810 | prose | pages [6] -->
m

<!-- b002811 | prose | pages [6] -->
m

<!-- b002812 | prose | pages [6] -->
m

<!-- b002813 | prose | pages [6] -->
m

<!-- b002814 | prose | pages [6] -->
m

<!-- b002815 | prose | pages [6] -->
m

<!-- b002816 | prose | pages [6] -->
m

<!-- b002817 | prose | pages [6] -->
m

<!-- b002818 | prose | pages [6] -->
m

<!-- b002819 | prose | pages [6] -->
m

<!-- b002820 | prose | pages [6] -->
m

<!-- b002821 | prose | pages [6] -->
m

<!-- b002822 | prose | pages [6] -->
m

<!-- b002823 | prose | pages [6] -->
m

<!-- b002824 | prose | pages [6] -->
m

<!-- b002825 | prose | pages [6] -->
m

<!-- b002826 | prose | pages [6] -->
m

<!-- b002827 | prose | pages [6] -->
m

<!-- b002828 | prose | pages [6] -->
m

<!-- b002829 | prose | pages [6] -->
m

<!-- b002830 | prose | pages [6] -->
m

<!-- b002831 | prose | pages [6] -->
m

<!-- b002832 | prose | pages [6] -->
m

<!-- b002833 | prose | pages [6] -->
m

<!-- b002834 | prose | pages [6] -->
m

<!-- b002835 | prose | pages [6] -->
m

<!-- b002836 | prose | pages [6] -->
m

<!-- b002837 | prose | pages [6] -->
m

<!-- b002838 | prose | pages [6] -->
m

<!-- b002839 | prose | pages [6] -->
m

<!-- b002840 | prose | pages [6] -->
m

<!-- b002841 | prose | pages [6] -->
m

<!-- b002842 | prose | pages [6] -->
m

<!-- b002843 | prose | pages [6] -->
m

<!-- b002844 | prose | pages [6] -->
m

<!-- b002845 | prose | pages [6] -->
m

<!-- b002846 | prose | pages [6] -->
m

<!-- b002847 | prose | pages [6] -->
m

<!-- b002848 | prose | pages [6] -->
m

<!-- b002849 | prose | pages [6] -->
m

<!-- b002850 | prose | pages [6] -->
m

<!-- b002851 | prose | pages [6] -->
m

<!-- b002852 | prose | pages [6] -->
m

<!-- b002853 | prose | pages [6] -->
m

<!-- b002854 | prose | pages [6] -->
m

<!-- b002855 | prose | pages [6] -->
m

<!-- b002856 | prose | pages [6] -->
m

<!-- b002857 | prose | pages [6] -->
m

<!-- b002858 | prose | pages [6] -->
m

<!-- b002859 | prose | pages [6] -->
m

<!-- b002860 | prose | pages [6] -->
m

<!-- b002861 | prose | pages [6] -->
m

<!-- b002862 | prose | pages [6] -->
m

<!-- b002863 | prose | pages [6] -->
m

<!-- b002864 | prose | pages [6] -->
m

<!-- b002865 | prose | pages [6] -->
m

<!-- b002866 | prose | pages [6] -->
m

<!-- b002867 | prose | pages [6] -->
m

<!-- b002868 | prose | pages [6] -->
m

<!-- b002869 | prose | pages [6] -->
m

<!-- b002870 | prose | pages [6] -->
m

<!-- b002871 | prose | pages [6] -->
m

<!-- b002872 | prose | pages [6] -->
m

<!-- b002873 | prose | pages [6] -->
m

<!-- b002874 | prose | pages [6] -->
m

<!-- b002875 | prose | pages [6] -->
m

<!-- b002876 | prose | pages [6] -->
m

<!-- b002877 | prose | pages [6] -->
m

<!-- b002878 | prose | pages [6] -->
m

<!-- b002879 | prose | pages [6] -->
m

<!-- b002880 | prose | pages [6] -->
m

<!-- b002881 | prose | pages [6] -->
m

<!-- b002882 | prose | pages [6] -->
m

<!-- b002883 | prose | pages [6] -->
m

<!-- b002884 | prose | pages [6] -->
m

<!-- b002885 | prose | pages [6] -->
m

<!-- b002886 | prose | pages [6] -->
m

<!-- b002887 | prose | pages [6] -->
between the current value and the error at the past q time points;

<!-- b002888 | prose | pages [6] -->
tis the error term at time point t. 

<!-- b002889 | prose | pages [6] -->
Our initial ARIMA projections of the number of gold medals and the total number of medals for the United States and China resulted in the projection charts shown below:

<!-- b002890 | furniture | pages [6] -->


<!-- b002891 | prose | pages [6] -->
关注数学模型

<!-- b002892 | furniture | pages [6] -->
2

<!-- b002893 | furniture | pages [6] -->
MATHmodels

<!-- b002894 | furniture | pages [6] -->
获取更多资讯

<!-- b002895 | furniture | pages [7] -->
Team#2507817                                                             Page 7 of 25

<!-- b002896 | prose | pages [7] -->
微信公众号：数学模型

<!-- b002897 | furniture | pages [7] -->


<!-- b002898 | prose | pages [7] -->
a) United States Gold

<!-- b002899 | furniture | pages [7] -->


<!-- b002900 | furniture | pages [7] -->


<!-- b002901 | furniture | pages [7] -->


<!-- b002902 | prose | pages [7] -->
b)  United States Total Predict

<!-- b002903 | prose | pages [7] -->
微信号：MATHmodels

<!-- b002904 | furniture | pages [7] -->


<!-- b002905 | prose | pages [7] -->
c) China Gold Predict

<!-- b002906 | furniture | pages [7] -->


<!-- b002907 | prose | pages [7] -->
d)  China Total Predict

<!-- b002908 | furniture | pages [7] -->


<!-- b002909 | furniture | pages [7] -->


<!-- b002910 | caption | pages [7] -->
Figure 3 Prediction chart of medal numbers for the United States and China

<!-- b002911 | prose | pages [7] -->
The ARIMA (p, d, q) model corresponding to the above predictions and the correlation 2 coefficients R are shown in the table below:

<!-- b002912 | caption | pages [7] -->
Table 1 Relevant data for predictive models

<!-- b002913 | prose | pages [7] -->
ARIMA (p, d, q)

<!-- b002914 | furniture | pages [7] -->


<!-- b002915 | prose | pages [7] -->
2 R ARIMA (2, 0, 2) United States Gold Predict 0.218 ARIMA (2, 1, 1) United States Total Predict 0.257 ARIMA (1, 1, 0) China Gold Predict 0.430 ARIMA (1, 1, 0) China Total Predict 0.494

<!-- b002916 | prose | pages [7] -->
The correlation coefficients derived from the prediction are small not close to 1, proving that the use of ARIMA model to predict the number of medals is not ideal, so we use the GSRF swing prediction model to make predictions

<!-- b002917 | heading | pages [7] -->
5.1.2 GSRF Prediction Modeling

<!-- b002918 | prose | pages [7] -->
First, we need to build a model for predicting the fluctuations in the number of medals for each country, as well as finding the factors that are most relevant to this fluctuation. From this we use the GSRF swing prediction model.

<!-- b002919 | prose | pages [7] -->
In order to predict the number of medals the country will win in the next Olympics, we start with the previous years' awards of the participating athletes and use the network search random forest algorithm to predict the number of gold medals won in the future and the total number of medals, respectively.

<!-- b002920 | prose | pages [7] -->
Next, we describe the selected metrics data and explain the algorithmic process.

<!-- b002921 | heading | pages [7] -->
1) Selected indicators

<!-- b002922 | furniture | pages [7] -->


<!-- b002923 | furniture | pages [8] -->
Team#2507817                                                             Page 8 of 25

<!-- b002924 | prose | pages [8] -->
Using the dataset from previous years, we selected four characteristic input indicators:

<!-- b002925 | prose | pages [8] -->
 Total number of athletes from this country in the current Olympics: more athletes

<!-- b002926 | prose | pages [8] -->
means more opportunities to compete and a wider range of selections, increasing the likelihood of winning medals. We denote the total number of athletes from country i in the jth Olympics as: Aij

<!-- b002927 | prose | pages [8] -->
 The number of gold medals and total medals won by the country up to the current

<!-- b002928 | prose | pages [8] -->
Olympics: The medal table of previous years gives a preliminary idea of the strength of the country and the trend of its strength. We denote the total number of gold medals won by country i before the jth Olympics as Gij and the total number of medals as T(ij).

<!-- b002929 | prose | pages [8] -->
 Current total number of Olympic events: The total number of Olympic events

<!-- b002930 | prose | pages [8] -->
determines the basis of medal distribution, the more events the more medals. The more programs a country participates in, the more chances it has to win. An increase in the number of events results in a wider distribution of medals, with more countries having a chance to win. We denote the total number of events in the jth Olympics as Ej

<!-- b002931 | prose | pages [8] -->
 Is the country hosting the Games: As a host, the country has advantages in terms of

<!-- b002932 | prose | pages [8] -->
venues, facilities and logistics. The host can increase the number of events it specializes in, decrease the number of events it does not specialize in, and automatically get more places, increasing the chances of athletes to participate. If it is the host of the jth Olympic Games, let Hij = 1, and vice versa, let Hij = 0.

<!-- b002933 | heading | pages [8] -->
2) GSRF Algorithm

<!-- b002934 | prose | pages [8] -->
The GSRF algorithm optimizes the random forest model using a grid search algorithm.

<!-- b002935 | prose | pages [8] -->
Random forests are machine learning algorithms trained using multiple decision trees, with a randomly selected subset of features per tree, and voting to integrate the results when classifying. To prevent overfitting or underfitting, grid search optimization is used. The grid search algorithm traverses a grid of predefined parameters, trains and evaluates each combination, and outputs the best set of parameters and model performance.

<!-- b002936 | prose | pages [8] -->
Compared with the standard random forest algorithm, the GSRF algorithm uses an optimal combination of hyperparameters to train and predict the model. This improvement significantly improves the performance of the model and effectively mitigates problems such as overfitting or underfitting. The following figure illustrates the workflow of the GSRF algorithm.

<!-- b002937 | furniture | pages [8] -->


<!-- b002938 | caption | pages [8] -->
Figure 4 GSRF Algorithm Flow Diagram

<!-- b002939 | heading | pages [8] -->
3) Make Predictions on Gold & Total Medals

<!-- b002940 | prose | pages [8] -->
According to the literature, it is known that a series of data such as the number of strengths of athletes, the number of types of events and so on have an impact on the number of medals in the next Olympic Games. Therefore, we use the above four characteristic input indicators as

<!-- b002941 | furniture | pages [8] -->


<!-- b002942 | prose | pages [8] -->
关注数学模型

<!-- b002943 | furniture | pages [8] -->
2

<!-- b002944 | furniture | pages [8] -->
MATHmodels

<!-- b002945 | furniture | pages [8] -->
获取更多资讯

<!-- b002946 | furniture | pages [9] -->
Team#2507817                                                             Page 9 of 25

<!-- b002947 | prose | pages [9] -->
the input parameters of the random forest model to predict the number of medals:

<!-- b002948 | prose | pages [9] -->
(

<!-- b002949 | prose | pages [9] -->
A

<!-- b002950 | prose | pages [9] -->
,

<!-- b002951 | prose | pages [9] -->
G

<!-- b002952 | prose | pages [9] -->
,

<!-- b002953 | prose | pages [9] -->
E

<!-- b002954 | prose | pages [9] -->
,

<!-- b002955 | prose | pages [9] -->
ij g

<!-- b002956 | prose | pages [9] -->
,

<!-- b002957 | prose | pages [9] -->
ij j g

<!-- b002958 | prose | pages [9] -->
,

<!-- b002959 | furniture | pages [9] -->


<!-- b002960 | furniture | pages [9] -->


<!-- b002961 | prose | pages [9] -->
(

<!-- b002962 | prose | pages [9] -->
A

<!-- b002963 | prose | pages [9] -->
,

<!-- b002964 | prose | pages [9] -->
T E

<!-- b002965 | prose | pages [9] -->
, ,

<!-- b002966 | prose | pages [9] -->
ij t

<!-- b002967 | prose | pages [9] -->
,

<!-- b002968 | prose | pages [9] -->
ij j t

<!-- b002969 | prose | pages [9] -->
,

<!-- b002970 | prose | pages [9] -->
Among them.

<!-- b002971 | prose | pages [9] -->


<!-- b002972 | prose | pages [9] -->
GSRF

<!-- b002973 | prose | pages [9] -->
H H

<!-- b002974 | prose | pages [9] -->
)

<!-- b002975 | prose | pages [9] -->
Y

<!-- b002976 | prose | pages [9] -->
ij g

<!-- b002977 | prose | pages [9] -->
,

<!-- b002978 | prose | pages [9] -->
g

<!-- b002979 | furniture | pages [9] -->


<!-- b002980 | prose | pages [9] -->
(2)

<!-- b002981 | prose | pages [9] -->


<!-- b002982 | prose | pages [9] -->
GSRF

<!-- b002983 | prose | pages [9] -->
H H

<!-- b002984 | prose | pages [9] -->
)

<!-- b002985 | prose | pages [9] -->
Y

<!-- b002986 | prose | pages [9] -->
ij t

<!-- b002987 | prose | pages [9] -->
,

<!-- b002988 | prose | pages [9] -->
t

<!-- b002989 | prose | pages [9] -->
represent the total number of athletes from the country in the gold medal A , E , H ij g , j g , ij g ,

<!-- b002990 | prose | pages [9] -->
prediction model, the total number of Olympic events, and whether this country is the host of Y Represents the number of gold medals predicted. this Olympics, respectively.

<!-- b002991 | prose | pages [9] -->
g

<!-- b002992 | prose | pages [9] -->
Represent the total number of athletes from the country in the total medal A , E , H ij t , j t , ij t ,

<!-- b002993 | prose | pages [9] -->
count prediction model, the total number of Olympic events, and whether this country is the

<!-- b002994 | prose | pages [9] -->
微信公众号：数学模型

<!-- b002995 | prose | pages [9] -->
tY Represents the number of gold medals predicted. host of this Olympics, respectively.

<!-- b002996 | prose | pages [9] -->
We use data prior to 2024 as the training set and 2024 as the test set. The k-fold cross- validation method is used, taking k to be 10. The training set is divided equally into 10 equal sized subsets. For each subset, that subset is used as the validation set and the rest use the remaining 9 subsets as the training set. The random forest model is trained on the training set and the model performance is evaluated on the validation set and the evaluation metrics are recorded. Finally, the average evaluation metrics of all the subsets are calculated, giving a comprehensive estimate of the model performance, as a way to assess the stability and generalization ability of the model. The schematic diagram is shown below:

<!-- b002997 | prose | pages [9] -->
微信号：MATHmodels

<!-- b002998 | furniture | pages [9] -->


<!-- b002999 | caption | pages [9] -->
Figure 5 10 Fold Cross Validation Diagram

<!-- b003000 | prose | pages [9] -->
The Random Forest Regressor algorithm from the integration module in the scikit-learn (sklearn) machine learning library[1] and the GridSearchCV algorithm from sklearn were used via . The optimal parameter combination obtained by GridSearchCV is as follows:

<!-- b003001 | caption | pages [9] -->
Table 2 The impact of various indicators on the prediction results

<!-- b003002 | prose | pages [9] -->
Gold Medals

<!-- b003003 | furniture | pages [9] -->


<!-- b003004 | prose | pages [9] -->
G

<!-- b003005 | furniture | pages [9] -->


<!-- b003006 | furniture | pages [9] -->


<!-- b003007 | prose | pages [9] -->
A E H ij g , ij ,j g ij g ,

<!-- b003008 | prose | pages [9] -->
74.10% 1.71% 7.40% 16.90%

<!-- b003009 | prose | pages [9] -->
Total Medal

<!-- b003010 | furniture | pages [9] -->


<!-- b003011 | prose | pages [9] -->
T

<!-- b003012 | furniture | pages [9] -->


<!-- b003013 | furniture | pages [9] -->


<!-- b003014 | prose | pages [9] -->
A E H ij t , ij ,j t ij t ,

<!-- b003015 | prose | pages [9] -->
85.70% 7.20% 6.30% 0.80%

<!-- b003016 | prose | pages [9] -->
We use radar charts to visualize the impact of each indicator on the forecast results as follows:

<!-- b003017 | furniture | pages [9] -->


<!-- b003018 | furniture | pages [12] -->
Team#2507817                                                             Page 12 of 25

<!-- b003019 | prose | pages [12] -->
m

<!-- b003020 | prose | pages [12] -->
m

<!-- b003021 | prose | pages [12] -->
m

<!-- b003022 | prose | pages [12] -->
m

<!-- b003023 | prose | pages [12] -->
m

<!-- b003024 | prose | pages [12] -->
m

<!-- b003025 | prose | pages [12] -->
m

<!-- b003026 | prose | pages [12] -->
m

<!-- b003027 | prose | pages [12] -->
m

<!-- b003028 | prose | pages [12] -->
m

<!-- b003029 | prose | pages [12] -->
m

<!-- b003030 | prose | pages [12] -->
m

<!-- b003031 | prose | pages [12] -->
m

<!-- b003032 | prose | pages [12] -->
m

<!-- b003033 | prose | pages [12] -->
m

<!-- b003034 | prose | pages [12] -->
m

<!-- b003035 | prose | pages [12] -->
m

<!-- b003036 | prose | pages [12] -->
m

<!-- b003037 | prose | pages [12] -->
m

<!-- b003038 | prose | pages [12] -->
m

<!-- b003039 | prose | pages [12] -->
m

<!-- b003040 | prose | pages [12] -->
m

<!-- b003041 | prose | pages [12] -->
m

<!-- b003042 | prose | pages [12] -->
m

<!-- b003043 | prose | pages [12] -->
m

<!-- b003044 | prose | pages [12] -->
m

<!-- b003045 | prose | pages [12] -->
m

<!-- b003046 | prose | pages [12] -->
m

<!-- b003047 | prose | pages [12] -->
m

<!-- b003048 | prose | pages [12] -->
m

<!-- b003049 | prose | pages [12] -->
m

<!-- b003050 | prose | pages [12] -->
m

<!-- b003051 | prose | pages [12] -->
m

<!-- b003052 | prose | pages [12] -->
m

<!-- b003053 | prose | pages [12] -->
m

<!-- b003054 | prose | pages [12] -->
m

<!-- b003055 | prose | pages [12] -->
m

<!-- b003056 | prose | pages [12] -->
m

<!-- b003057 | prose | pages [12] -->
m

<!-- b003058 | prose | pages [12] -->
m

<!-- b003059 | prose | pages [12] -->
m

<!-- b003060 | prose | pages [12] -->
m

<!-- b003061 | prose | pages [12] -->
m

<!-- b003062 | prose | pages [12] -->
m

<!-- b003063 | prose | pages [12] -->
m

<!-- b003064 | prose | pages [12] -->
m

<!-- b003065 | prose | pages [12] -->
m

<!-- b003066 | prose | pages [12] -->
m

<!-- b003067 | prose | pages [12] -->
m

<!-- b003068 | prose | pages [12] -->
m

<!-- b003069 | prose | pages [12] -->
m

<!-- b003070 | prose | pages [12] -->
m

<!-- b003071 | prose | pages [12] -->
m

<!-- b003072 | prose | pages [12] -->
m

<!-- b003073 | prose | pages [12] -->
m

<!-- b003074 | prose | pages [12] -->
m

<!-- b003075 | prose | pages [12] -->
m

<!-- b003076 | prose | pages [12] -->
m

<!-- b003077 | prose | pages [12] -->
m

<!-- b003078 | prose | pages [12] -->
m

<!-- b003079 | prose | pages [12] -->
m

<!-- b003080 | prose | pages [12] -->
m

<!-- b003081 | prose | pages [12] -->
m

<!-- b003082 | prose | pages [12] -->
m

<!-- b003083 | prose | pages [12] -->
m

<!-- b003084 | prose | pages [12] -->
m

<!-- b003085 | prose | pages [12] -->
m

<!-- b003086 | prose | pages [12] -->
m

<!-- b003087 | prose | pages [12] -->
m

<!-- b003088 | prose | pages [12] -->
m

<!-- b003089 | prose | pages [12] -->
m

<!-- b003090 | prose | pages [12] -->
m

<!-- b003091 | prose | pages [12] -->
m

<!-- b003092 | prose | pages [12] -->
The above predictions are only the most likely scenarios, next we solve for the prediction

<!-- b003093 | prose | pages [12] -->
m

<!-- b003094 | prose | pages [12] -->
m

<!-- b003095 | prose | pages [12] -->
m

<!-- b003096 | prose | pages [12] -->
m

<!-- b003097 | prose | pages [12] -->
m

<!-- b003098 | prose | pages [12] -->
m

<!-- b003099 | prose | pages [12] -->
m

<!-- b003100 | prose | pages [12] -->
m

<!-- b003101 | prose | pages [12] -->
m

<!-- b003102 | prose | pages [12] -->
m

<!-- b003103 | prose | pages [12] -->
m

<!-- b003104 | prose | pages [12] -->
m

<!-- b003105 | prose | pages [12] -->
m

<!-- b003106 | prose | pages [12] -->
m

<!-- b003107 | prose | pages [12] -->
m

<!-- b003108 | prose | pages [12] -->
m

<!-- b003109 | prose | pages [12] -->
m

<!-- b003110 | prose | pages [12] -->
m

<!-- b003111 | prose | pages [12] -->
m

<!-- b003112 | prose | pages [12] -->
m

<!-- b003113 | prose | pages [12] -->
m

<!-- b003114 | prose | pages [12] -->
m

<!-- b003115 | prose | pages [12] -->
m

<!-- b003116 | prose | pages [12] -->
m

<!-- b003117 | prose | pages [12] -->
m

<!-- b003118 | prose | pages [12] -->
m

<!-- b003119 | prose | pages [12] -->
m

<!-- b003120 | prose | pages [12] -->
m

<!-- b003121 | prose | pages [12] -->
m

<!-- b003122 | prose | pages [12] -->
m

<!-- b003123 | prose | pages [12] -->
m

<!-- b003124 | prose | pages [12] -->
m

<!-- b003125 | prose | pages [12] -->
m

<!-- b003126 | prose | pages [12] -->
m

<!-- b003127 | prose | pages [12] -->
m

<!-- b003128 | prose | pages [12] -->
m

<!-- b003129 | prose | pages [12] -->
m

<!-- b003130 | prose | pages [12] -->
m

<!-- b003131 | prose | pages [12] -->
m

<!-- b003132 | prose | pages [12] -->
m

<!-- b003133 | prose | pages [12] -->
m

<!-- b003134 | prose | pages [12] -->
m

<!-- b003135 | prose | pages [12] -->
m

<!-- b003136 | prose | pages [12] -->
m

<!-- b003137 | prose | pages [12] -->
m

<!-- b003138 | prose | pages [12] -->
m

<!-- b003139 | prose | pages [12] -->
m

<!-- b003140 | prose | pages [12] -->
m

<!-- b003141 | prose | pages [12] -->
m

<!-- b003142 | prose | pages [12] -->
m

<!-- b003143 | prose | pages [12] -->
m

<!-- b003144 | prose | pages [12] -->
m

<!-- b003145 | prose | pages [12] -->
m

<!-- b003146 | prose | pages [12] -->
m

<!-- b003147 | prose | pages [12] -->
m

<!-- b003148 | prose | pages [12] -->
m

<!-- b003149 | prose | pages [12] -->
m

<!-- b003150 | prose | pages [12] -->
m

<!-- b003151 | prose | pages [12] -->
m

<!-- b003152 | prose | pages [12] -->
m

<!-- b003153 | prose | pages [12] -->
m

<!-- b003154 | prose | pages [12] -->
m

<!-- b003155 | prose | pages [12] -->
m

<!-- b003156 | prose | pages [12] -->
m

<!-- b003157 | prose | pages [12] -->
m

<!-- b003158 | prose | pages [12] -->
m

<!-- b003159 | prose | pages [12] -->
m

<!-- b003160 | prose | pages [12] -->
m

<!-- b003161 | prose | pages [12] -->
m

<!-- b003162 | prose | pages [12] -->
m

<!-- b003163 | prose | pages [12] -->
m

<!-- b003164 | prose | pages [12] -->
m

<!-- b003165 | prose | pages [12] -->
m

<!-- b003166 | prose | pages [12] -->
m

<!-- b003167 | prose | pages [12] -->
m

<!-- b003168 | prose | pages [12] -->
m

<!-- b003169 | prose | pages [12] -->
m

<!-- b003170 | prose | pages [12] -->
m

<!-- b003171 | prose | pages [12] -->
m

<!-- b003172 | prose | pages [12] -->
m

<!-- b003173 | prose | pages [12] -->
m

<!-- b003174 | prose | pages [12] -->
m

<!-- b003175 | prose | pages [12] -->
m

<!-- b003176 | prose | pages [12] -->
m

<!-- b003177 | prose | pages [12] -->
m

<!-- b003178 | prose | pages [12] -->
m

<!-- b003179 | prose | pages [12] -->
m

<!-- b003180 | prose | pages [12] -->
m

<!-- b003181 | prose | pages [12] -->
m

<!-- b003182 | prose | pages [12] -->
m

<!-- b003183 | prose | pages [12] -->
m

<!-- b003184 | prose | pages [12] -->
m

<!-- b003185 | prose | pages [12] -->
m

<!-- b003186 | prose | pages [12] -->
m

<!-- b003187 | prose | pages [12] -->
m

<!-- b003188 | prose | pages [12] -->
m

<!-- b003189 | prose | pages [12] -->
m

<!-- b003190 | prose | pages [12] -->
m

<!-- b003191 | prose | pages [12] -->
m

<!-- b003192 | prose | pages [12] -->
m

<!-- b003193 | prose | pages [12] -->
m

<!-- b003194 | prose | pages [12] -->
m

<!-- b003195 | prose | pages [12] -->
m

<!-- b003196 | prose | pages [12] -->
m

<!-- b003197 | prose | pages [12] -->
m

<!-- b003198 | prose | pages [12] -->
m

<!-- b003199 | prose | pages [12] -->
m

<!-- b003200 | prose | pages [12] -->
m

<!-- b003201 | prose | pages [12] -->
m

<!-- b003202 | prose | pages [12] -->
m

<!-- b003203 | prose | pages [12] -->
m

<!-- b003204 | prose | pages [12] -->
m

<!-- b003205 | prose | pages [12] -->
m

<!-- b003206 | prose | pages [12] -->
m

<!-- b003207 | prose | pages [12] -->
m

<!-- b003208 | prose | pages [12] -->
m

<!-- b003209 | prose | pages [12] -->
m

<!-- b003210 | prose | pages [12] -->
m

<!-- b003211 | prose | pages [12] -->
m

<!-- b003212 | prose | pages [12] -->
m

<!-- b003213 | prose | pages [12] -->
m

<!-- b003214 | prose | pages [12] -->
m

<!-- b003215 | prose | pages [12] -->
m

<!-- b003216 | prose | pages [12] -->
m

<!-- b003217 | prose | pages [12] -->
m

<!-- b003218 | prose | pages [12] -->
m

<!-- b003219 | prose | pages [12] -->
m

<!-- b003220 | prose | pages [12] -->
m

<!-- b003221 | prose | pages [12] -->
m

<!-- b003222 | prose | pages [12] -->
m

<!-- b003223 | prose | pages [12] -->
m

<!-- b003224 | prose | pages [12] -->
m

<!-- b003225 | prose | pages [12] -->
m

<!-- b003226 | prose | pages [12] -->
m

<!-- b003227 | prose | pages [12] -->
m

<!-- b003228 | prose | pages [12] -->
m

<!-- b003229 | prose | pages [12] -->
intervals at the 95% confidence level:

<!-- b003230 | prose | pages [12] -->
m

<!-- b003231 | prose | pages [12] -->
m

<!-- b003232 | prose | pages [12] -->
m

<!-- b003233 | prose | pages [12] -->
m

<!-- b003234 | prose | pages [12] -->
m

<!-- b003235 | prose | pages [12] -->
m

<!-- b003236 | prose | pages [12] -->
m

<!-- b003237 | prose | pages [12] -->
m

<!-- b003238 | prose | pages [12] -->
m

<!-- b003239 | prose | pages [12] -->
m

<!-- b003240 | prose | pages [12] -->
m

<!-- b003241 | prose | pages [12] -->
m

<!-- b003242 | prose | pages [12] -->
m

<!-- b003243 | prose | pages [12] -->
m

<!-- b003244 | prose | pages [12] -->
m

<!-- b003245 | prose | pages [12] -->
m

<!-- b003246 | prose | pages [12] -->
m

<!-- b003247 | prose | pages [12] -->
m

<!-- b003248 | prose | pages [12] -->
m

<!-- b003249 | prose | pages [12] -->
m

<!-- b003250 | prose | pages [12] -->
m

<!-- b003251 | prose | pages [12] -->
m

<!-- b003252 | prose | pages [12] -->
m

<!-- b003253 | prose | pages [12] -->
m

<!-- b003254 | prose | pages [12] -->
m

<!-- b003255 | prose | pages [12] -->
m

<!-- b003256 | prose | pages [12] -->
m

<!-- b003257 | prose | pages [12] -->
m

<!-- b003258 | prose | pages [12] -->
m

<!-- b003259 | prose | pages [12] -->
m

<!-- b003260 | prose | pages [12] -->
m

<!-- b003261 | prose | pages [12] -->
m

<!-- b003262 | prose | pages [12] -->
m

<!-- b003263 | prose | pages [12] -->
m

<!-- b003264 | prose | pages [12] -->
m

<!-- b003265 | prose | pages [12] -->
m

<!-- b003266 | prose | pages [12] -->
m

<!-- b003267 | prose | pages [12] -->
m

<!-- b003268 | prose | pages [12] -->
m

<!-- b003269 | prose | pages [12] -->
m

<!-- b003270 | prose | pages [12] -->
m

<!-- b003271 | prose | pages [12] -->
m

<!-- b003272 | prose | pages [12] -->
m

<!-- b003273 | prose | pages [12] -->
m

<!-- b003274 | prose | pages [12] -->
m

<!-- b003275 | prose | pages [12] -->
m

<!-- b003276 | prose | pages [12] -->
m

<!-- b003277 | prose | pages [12] -->
m

<!-- b003278 | prose | pages [12] -->
m

<!-- b003279 | prose | pages [12] -->
m

<!-- b003280 | prose | pages [12] -->
m

<!-- b003281 | prose | pages [12] -->
m

<!-- b003282 | prose | pages [12] -->
m

<!-- b003283 | prose | pages [12] -->
m

<!-- b003284 | prose | pages [12] -->
m

<!-- b003285 | prose | pages [12] -->
m

<!-- b003286 | prose | pages [12] -->
m

<!-- b003287 | prose | pages [12] -->
m

<!-- b003288 | prose | pages [12] -->
m

<!-- b003289 | prose | pages [12] -->
m

<!-- b003290 | prose | pages [12] -->
m

<!-- b003291 | prose | pages [12] -->
m

<!-- b003292 | prose | pages [12] -->
m

<!-- b003293 | prose | pages [12] -->
m

<!-- b003294 | prose | pages [12] -->
m

<!-- b003295 | prose | pages [12] -->
m

<!-- b003296 | prose | pages [12] -->
m

<!-- b003297 | prose | pages [12] -->
m

<!-- b003298 | prose | pages [12] -->
m

<!-- b003299 | prose | pages [12] -->
m

<!-- b003300 | prose | pages [12] -->
m

<!-- b003301 | prose | pages [12] -->
m

<!-- b003302 | prose | pages [12] -->
m

<!-- b003303 | prose | pages [12] -->
m

<!-- b003304 | prose | pages [12] -->
m

<!-- b003305 | prose | pages [12] -->
m

<!-- b003306 | prose | pages [12] -->
m

<!-- b003307 | prose | pages [12] -->
m

<!-- b003308 | prose | pages [12] -->
m

<!-- b003309 | prose | pages [12] -->
m

<!-- b003310 | prose | pages [12] -->
m

<!-- b003311 | prose | pages [12] -->
m

<!-- b003312 | prose | pages [12] -->
m

<!-- b003313 | prose | pages [12] -->
m

<!-- b003314 | prose | pages [12] -->
m

<!-- b003315 | prose | pages [12] -->
m

<!-- b003316 | prose | pages [12] -->
m

<!-- b003317 | prose | pages [12] -->
m

<!-- b003318 | prose | pages [12] -->
m

<!-- b003319 | prose | pages [12] -->
m

<!-- b003320 | prose | pages [12] -->
m

<!-- b003321 | prose | pages [12] -->
m

<!-- b003322 | prose | pages [12] -->
m

<!-- b003323 | prose | pages [12] -->
m

<!-- b003324 | prose | pages [12] -->
m

<!-- b003325 | prose | pages [12] -->
m

<!-- b003326 | prose | pages [12] -->
m

<!-- b003327 | prose | pages [12] -->
m

<!-- b003328 | prose | pages [12] -->
m

<!-- b003329 | prose | pages [12] -->
m

<!-- b003330 | prose | pages [12] -->
m

<!-- b003331 | prose | pages [12] -->
m

<!-- b003332 | prose | pages [12] -->
m

<!-- b003333 | prose | pages [12] -->
m

<!-- b003334 | prose | pages [12] -->
m

<!-- b003335 | prose | pages [12] -->
m

<!-- b003336 | prose | pages [12] -->
m

<!-- b003337 | prose | pages [12] -->
m

<!-- b003338 | prose | pages [12] -->
m

<!-- b003339 | prose | pages [12] -->
m

<!-- b003340 | prose | pages [12] -->
m

<!-- b003341 | prose | pages [12] -->
m

<!-- b003342 | prose | pages [12] -->
m

<!-- b003343 | prose | pages [12] -->
m

<!-- b003344 | prose | pages [12] -->
m

<!-- b003345 | prose | pages [12] -->
m

<!-- b003346 | prose | pages [12] -->
m

<!-- b003347 | prose | pages [12] -->
m

<!-- b003348 | prose | pages [12] -->
m

<!-- b003349 | prose | pages [12] -->
m

<!-- b003350 | prose | pages [12] -->
m

<!-- b003351 | prose | pages [12] -->
m

<!-- b003352 | prose | pages [12] -->
m

<!-- b003353 | prose | pages [12] -->
m

<!-- b003354 | prose | pages [12] -->
m

<!-- b003355 | prose | pages [12] -->
m

<!-- b003356 | prose | pages [12] -->
m

<!-- b003357 | prose | pages [12] -->
m

<!-- b003358 | prose | pages [12] -->
m

<!-- b003359 | prose | pages [12] -->
m

<!-- b003360 | prose | pages [12] -->
m

<!-- b003361 | prose | pages [12] -->
m

<!-- b003362 | prose | pages [12] -->
m

<!-- b003363 | prose | pages [12] -->
m

<!-- b003364 | prose | pages [12] -->
m

<!-- b003365 | prose | pages [12] -->
m

<!-- b003366 | prose | pages [12] -->
m

<!-- b003367 | prose | pages [12] -->
m

<!-- b003368 | prose | pages [12] -->
m

<!-- b003369 | prose | pages [12] -->
m

<!-- b003370 | prose | pages [12] -->
m

<!-- b003371 | prose | pages [12] -->
m

<!-- b003372 | prose | pages [12] -->
m

<!-- b003373 | prose | pages [12] -->
m

<!-- b003374 | prose | pages [12] -->
m

<!-- b003375 | prose | pages [12] -->
m

<!-- b003376 | prose | pages [12] -->
m

<!-- b003377 | prose | pages [12] -->
m

<!-- b003378 | prose | pages [12] -->
m

<!-- b003379 | prose | pages [12] -->
m

<!-- b003380 | prose | pages [12] -->
m

<!-- b003381 | prose | pages [12] -->
m

<!-- b003382 | prose | pages [12] -->
m

<!-- b003383 | prose | pages [12] -->
m

<!-- b003384 | prose | pages [12] -->
m

<!-- b003385 | prose | pages [12] -->
m

<!-- b003386 | prose | pages [12] -->
m

<!-- b003387 | prose | pages [12] -->
m

<!-- b003388 | prose | pages [12] -->
m

<!-- b003389 | prose | pages [12] -->
m

<!-- b003390 | prose | pages [12] -->
m

<!-- b003391 | prose | pages [12] -->
m

<!-- b003392 | heading | pages [12] -->
5.2.2 Calculate the prediction interval

<!-- b003393 | prose | pages [12] -->
m

<!-- b003394 | prose | pages [12] -->
m

<!-- b003395 | prose | pages [12] -->
m

<!-- b003396 | prose | pages [12] -->
m

<!-- b003397 | prose | pages [12] -->
m

<!-- b003398 | prose | pages [12] -->
m

<!-- b003399 | prose | pages [12] -->
m

<!-- b003400 | prose | pages [12] -->
m

<!-- b003401 | prose | pages [12] -->
m

<!-- b003402 | prose | pages [12] -->
m

<!-- b003403 | prose | pages [12] -->
m

<!-- b003404 | prose | pages [12] -->
m

<!-- b003405 | prose | pages [12] -->
m

<!-- b003406 | prose | pages [12] -->
m

<!-- b003407 | prose | pages [12] -->
m

<!-- b003408 | prose | pages [12] -->
m

<!-- b003409 | prose | pages [12] -->
m

<!-- b003410 | prose | pages [12] -->
m

<!-- b003411 | prose | pages [12] -->
m

<!-- b003412 | prose | pages [12] -->
m

<!-- b003413 | prose | pages [12] -->
m

<!-- b003414 | prose | pages [12] -->
m

<!-- b003415 | prose | pages [12] -->
m

<!-- b003416 | prose | pages [12] -->
m

<!-- b003417 | prose | pages [12] -->
m

<!-- b003418 | prose | pages [12] -->
m

<!-- b003419 | prose | pages [12] -->
m

<!-- b003420 | prose | pages [12] -->
m

<!-- b003421 | prose | pages [12] -->
m

<!-- b003422 | prose | pages [12] -->
m

<!-- b003423 | prose | pages [12] -->
m

<!-- b003424 | prose | pages [12] -->
m

<!-- b003425 | prose | pages [12] -->
m

<!-- b003426 | prose | pages [12] -->
m

<!-- b003427 | prose | pages [12] -->
m

<!-- b003428 | prose | pages [12] -->
m

<!-- b003429 | prose | pages [12] -->
m

<!-- b003430 | prose | pages [12] -->
m

<!-- b003431 | prose | pages [12] -->
m

<!-- b003432 | prose | pages [12] -->
m

<!-- b003433 | prose | pages [12] -->
m

<!-- b003434 | prose | pages [12] -->
m

<!-- b003435 | prose | pages [12] -->
m

<!-- b003436 | prose | pages [12] -->
m

<!-- b003437 | prose | pages [12] -->
m

<!-- b003438 | prose | pages [12] -->
m

<!-- b003439 | prose | pages [12] -->
m

<!-- b003440 | prose | pages [12] -->
m

<!-- b003441 | prose | pages [12] -->
m

<!-- b003442 | prose | pages [12] -->
m

<!-- b003443 | prose | pages [12] -->
m

<!-- b003444 | prose | pages [12] -->
m

<!-- b003445 | prose | pages [12] -->
m

<!-- b003446 | prose | pages [12] -->
m

<!-- b003447 | prose | pages [12] -->
m

<!-- b003448 | prose | pages [12] -->
m

<!-- b003449 | prose | pages [12] -->
m

<!-- b003450 | prose | pages [12] -->
m

<!-- b003451 | prose | pages [12] -->
m

<!-- b003452 | prose | pages [12] -->
m

<!-- b003453 | prose | pages [12] -->
m

<!-- b003454 | prose | pages [12] -->
m

<!-- b003455 | prose | pages [12] -->
m

<!-- b003456 | prose | pages [12] -->
m

<!-- b003457 | prose | pages [12] -->
m

<!-- b003458 | prose | pages [12] -->
m

<!-- b003459 | prose | pages [12] -->
m

<!-- b003460 | prose | pages [12] -->
m

<!-- b003461 | prose | pages [12] -->
m

<!-- b003462 | prose | pages [12] -->
m

<!-- b003463 | prose | pages [12] -->
m

<!-- b003464 | prose | pages [12] -->
m

<!-- b003465 | prose | pages [12] -->
m

<!-- b003466 | prose | pages [12] -->
m

<!-- b003467 | prose | pages [12] -->
m

<!-- b003468 | prose | pages [12] -->
m

<!-- b003469 | prose | pages [12] -->
m

<!-- b003470 | prose | pages [12] -->
m

<!-- b003471 | prose | pages [12] -->
m

<!-- b003472 | prose | pages [12] -->
m

<!-- b003473 | prose | pages [12] -->
m

<!-- b003474 | prose | pages [12] -->
m

<!-- b003475 | prose | pages [12] -->
m

<!-- b003476 | prose | pages [12] -->
m

<!-- b003477 | prose | pages [12] -->
m

<!-- b003478 | prose | pages [12] -->
m

<!-- b003479 | prose | pages [12] -->
m

<!-- b003480 | prose | pages [12] -->
m

<!-- b003481 | prose | pages [12] -->
m

<!-- b003482 | prose | pages [12] -->
m

<!-- b003483 | prose | pages [12] -->
m

<!-- b003484 | prose | pages [12] -->
m

<!-- b003485 | prose | pages [12] -->
m

<!-- b003486 | prose | pages [12] -->
m

<!-- b003487 | prose | pages [12] -->
m

<!-- b003488 | prose | pages [12] -->
m

<!-- b003489 | prose | pages [12] -->
m

<!-- b003490 | prose | pages [12] -->
m

<!-- b003491 | prose | pages [12] -->
m

<!-- b003492 | prose | pages [12] -->
m

<!-- b003493 | prose | pages [12] -->
m

<!-- b003494 | prose | pages [12] -->
m

<!-- b003495 | prose | pages [12] -->
m

<!-- b003496 | prose | pages [12] -->
m

<!-- b003497 | prose | pages [12] -->
m

<!-- b003498 | prose | pages [12] -->
m

<!-- b003499 | prose | pages [12] -->
m

<!-- b003500 | prose | pages [12] -->
m

<!-- b003501 | prose | pages [12] -->
m

<!-- b003502 | prose | pages [12] -->
m

<!-- b003503 | prose | pages [12] -->
m

<!-- b003504 | prose | pages [12] -->
m

<!-- b003505 | prose | pages [12] -->
m

<!-- b003506 | prose | pages [12] -->
m

<!-- b003507 | prose | pages [12] -->
m

<!-- b003508 | prose | pages [12] -->
m

<!-- b003509 | prose | pages [12] -->
m

<!-- b003510 | prose | pages [12] -->
m

<!-- b003511 | prose | pages [12] -->
m

<!-- b003512 | prose | pages [12] -->
m

<!-- b003513 | prose | pages [12] -->
m

<!-- b003514 | prose | pages [12] -->
m

<!-- b003515 | prose | pages [12] -->
m

<!-- b003516 | prose | pages [12] -->
m

<!-- b003517 | prose | pages [12] -->
m

<!-- b003518 | prose | pages [12] -->
m

<!-- b003519 | prose | pages [12] -->
m

<!-- b003520 | prose | pages [12] -->
m

<!-- b003521 | prose | pages [12] -->
m

<!-- b003522 | prose | pages [12] -->
m

<!-- b003523 | prose | pages [12] -->
m

<!-- b003524 | prose | pages [12] -->
m

<!-- b003525 | prose | pages [12] -->
m

<!-- b003526 | prose | pages [12] -->
m

<!-- b003527 | prose | pages [12] -->
m

<!-- b003528 | prose | pages [12] -->
m

<!-- b003529 | prose | pages [12] -->
m

<!-- b003530 | prose | pages [12] -->
m

<!-- b003531 | prose | pages [12] -->
m

<!-- b003532 | prose | pages [12] -->
m

<!-- b003533 | prose | pages [12] -->
m

<!-- b003534 | prose | pages [12] -->
m

<!-- b003535 | prose | pages [12] -->
m

<!-- b003536 | prose | pages [12] -->
m

<!-- b003537 | prose | pages [12] -->
m

<!-- b003538 | prose | pages [12] -->
m

<!-- b003539 | prose | pages [12] -->
m

<!-- b003540 | prose | pages [12] -->
m

<!-- b003541 | prose | pages [12] -->
m

<!-- b003542 | prose | pages [12] -->
m

<!-- b003543 | prose | pages [12] -->
m

<!-- b003544 | prose | pages [12] -->
m

<!-- b003545 | prose | pages [12] -->
m

<!-- b003546 | prose | pages [12] -->
m

<!-- b003547 | prose | pages [12] -->
m

<!-- b003548 | prose | pages [12] -->
m

<!-- b003549 | prose | pages [12] -->
m

<!-- b003550 | prose | pages [12] -->
m

<!-- b003551 | prose | pages [12] -->
m

<!-- b003552 | prose | pages [12] -->
m

<!-- b003553 | prose | pages [12] -->
m

<!-- b003554 | prose | pages [12] -->
m

<!-- b003555 | prose | pages [12] -->
m

<!-- b003556 | prose | pages [12] -->
m

<!-- b003557 | prose | pages [12] -->
m

<!-- b003558 | prose | pages [12] -->
m

<!-- b003559 | prose | pages [12] -->
m

<!-- b003560 | prose | pages [12] -->
m

<!-- b003561 | prose | pages [12] -->
m

<!-- b003562 | prose | pages [12] -->
m

<!-- b003563 | prose | pages [12] -->
m

<!-- b003564 | prose | pages [12] -->
m

<!-- b003565 | prose | pages [12] -->
m

<!-- b003566 | prose | pages [12] -->
m

<!-- b003567 | prose | pages [12] -->
m

<!-- b003568 | prose | pages [12] -->
m

<!-- b003569 | prose | pages [12] -->
m

<!-- b003570 | prose | pages [12] -->
m

<!-- b003571 | prose | pages [12] -->
m

<!-- b003572 | prose | pages [12] -->
m

<!-- b003573 | prose | pages [12] -->
m

<!-- b003574 | prose | pages [12] -->
m

<!-- b003575 | prose | pages [12] -->
m

<!-- b003576 | prose | pages [12] -->
m

<!-- b003577 | prose | pages [12] -->
m

<!-- b003578 | prose | pages [12] -->
m

<!-- b003579 | prose | pages [12] -->
m

<!-- b003580 | prose | pages [12] -->
m

<!-- b003581 | prose | pages [12] -->
m

<!-- b003582 | prose | pages [12] -->
m

<!-- b003583 | prose | pages [12] -->
m

<!-- b003584 | prose | pages [12] -->
m

<!-- b003585 | prose | pages [12] -->
m

<!-- b003586 | prose | pages [12] -->
m

<!-- b003587 | prose | pages [12] -->
m

<!-- b003588 | prose | pages [12] -->
First, we determine whether the residuals of the two prediction models satisfy a normal

<!-- b003589 | prose | pages [12] -->
m

<!-- b003590 | prose | pages [12] -->
m

<!-- b003591 | prose | pages [12] -->
m

<!-- b003592 | prose | pages [12] -->
m

<!-- b003593 | prose | pages [12] -->
m

<!-- b003594 | prose | pages [12] -->
m

<!-- b003595 | prose | pages [12] -->
m

<!-- b003596 | prose | pages [12] -->
m

<!-- b003597 | prose | pages [12] -->
m

<!-- b003598 | prose | pages [12] -->
m

<!-- b003599 | prose | pages [12] -->
m

<!-- b003600 | prose | pages [12] -->
m

<!-- b003601 | prose | pages [12] -->
m

<!-- b003602 | prose | pages [12] -->
m

<!-- b003603 | prose | pages [12] -->
m

<!-- b003604 | prose | pages [12] -->
m

<!-- b003605 | prose | pages [12] -->
m

<!-- b003606 | prose | pages [12] -->
m

<!-- b003607 | prose | pages [12] -->
m

<!-- b003608 | prose | pages [12] -->
m

<!-- b003609 | prose | pages [12] -->
m

<!-- b003610 | prose | pages [12] -->
m

<!-- b003611 | prose | pages [12] -->
m

<!-- b003612 | prose | pages [12] -->
m

<!-- b003613 | prose | pages [12] -->
m

<!-- b003614 | prose | pages [12] -->
m

<!-- b003615 | prose | pages [12] -->
m

<!-- b003616 | prose | pages [12] -->
m

<!-- b003617 | prose | pages [12] -->
m

<!-- b003618 | prose | pages [12] -->
m

<!-- b003619 | prose | pages [12] -->
m

<!-- b003620 | prose | pages [12] -->
m

<!-- b003621 | prose | pages [12] -->
m

<!-- b003622 | prose | pages [12] -->
m

<!-- b003623 | prose | pages [12] -->
m

<!-- b003624 | prose | pages [12] -->
m

<!-- b003625 | prose | pages [12] -->
m

<!-- b003626 | prose | pages [12] -->
m

<!-- b003627 | prose | pages [12] -->
m

<!-- b003628 | prose | pages [12] -->
m

<!-- b003629 | prose | pages [12] -->
m

<!-- b003630 | prose | pages [12] -->
m

<!-- b003631 | prose | pages [12] -->
m

<!-- b003632 | prose | pages [12] -->
m

<!-- b003633 | prose | pages [12] -->
m

<!-- b003634 | prose | pages [12] -->
m

<!-- b003635 | prose | pages [12] -->
m

<!-- b003636 | prose | pages [12] -->
m

<!-- b003637 | prose | pages [12] -->
m

<!-- b003638 | prose | pages [12] -->
m

<!-- b003639 | prose | pages [12] -->
m

<!-- b003640 | prose | pages [12] -->
m

<!-- b003641 | prose | pages [12] -->
m

<!-- b003642 | prose | pages [12] -->
m

<!-- b003643 | prose | pages [12] -->
m

<!-- b003644 | prose | pages [12] -->
m

<!-- b003645 | prose | pages [12] -->
m

<!-- b003646 | prose | pages [12] -->
m

<!-- b003647 | prose | pages [12] -->
m

<!-- b003648 | prose | pages [12] -->
m

<!-- b003649 | prose | pages [12] -->
m

<!-- b003650 | prose | pages [12] -->
m

<!-- b003651 | prose | pages [12] -->
m

<!-- b003652 | prose | pages [12] -->
m

<!-- b003653 | prose | pages [12] -->
m

<!-- b003654 | prose | pages [12] -->
m

<!-- b003655 | prose | pages [12] -->
m

<!-- b003656 | prose | pages [12] -->
m

<!-- b003657 | prose | pages [12] -->
m

<!-- b003658 | prose | pages [12] -->
m

<!-- b003659 | prose | pages [12] -->
m

<!-- b003660 | prose | pages [12] -->
m

<!-- b003661 | prose | pages [12] -->
m

<!-- b003662 | prose | pages [12] -->
m

<!-- b003663 | prose | pages [12] -->
m

<!-- b003664 | prose | pages [12] -->
m

<!-- b003665 | prose | pages [12] -->
m

<!-- b003666 | prose | pages [12] -->
m

<!-- b003667 | prose | pages [12] -->
m

<!-- b003668 | prose | pages [12] -->
m

<!-- b003669 | prose | pages [12] -->
m

<!-- b003670 | prose | pages [12] -->
m

<!-- b003671 | prose | pages [12] -->
m

<!-- b003672 | prose | pages [12] -->
m

<!-- b003673 | prose | pages [12] -->
m

<!-- b003674 | prose | pages [12] -->
m

<!-- b003675 | prose | pages [12] -->
m

<!-- b003676 | prose | pages [12] -->
m

<!-- b003677 | prose | pages [12] -->
m

<!-- b003678 | prose | pages [12] -->
m

<!-- b003679 | prose | pages [12] -->
m

<!-- b003680 | prose | pages [12] -->
m

<!-- b003681 | prose | pages [12] -->
m

<!-- b003682 | prose | pages [12] -->
m

<!-- b003683 | prose | pages [12] -->
m

<!-- b003684 | prose | pages [12] -->
m

<!-- b003685 | prose | pages [12] -->
m

<!-- b003686 | prose | pages [12] -->
m

<!-- b003687 | prose | pages [12] -->
m

<!-- b003688 | prose | pages [12] -->
m

<!-- b003689 | prose | pages [12] -->
m

<!-- b003690 | prose | pages [12] -->
m

<!-- b003691 | prose | pages [12] -->
m

<!-- b003692 | prose | pages [12] -->
m

<!-- b003693 | prose | pages [12] -->
m

<!-- b003694 | prose | pages [12] -->
m

<!-- b003695 | prose | pages [12] -->
m

<!-- b003696 | prose | pages [12] -->
m

<!-- b003697 | prose | pages [12] -->
m

<!-- b003698 | prose | pages [12] -->
m

<!-- b003699 | prose | pages [12] -->
m

<!-- b003700 | prose | pages [12] -->
m

<!-- b003701 | prose | pages [12] -->
m

<!-- b003702 | prose | pages [12] -->
m

<!-- b003703 | prose | pages [12] -->
m

<!-- b003704 | prose | pages [12] -->
m

<!-- b003705 | prose | pages [12] -->
m

<!-- b003706 | prose | pages [12] -->
m

<!-- b003707 | prose | pages [12] -->
m

<!-- b003708 | prose | pages [12] -->
m

<!-- b003709 | prose | pages [12] -->
m

<!-- b003710 | prose | pages [12] -->
distribution:

<!-- b003711 | prose | pages [12] -->
We plotted and fitted a histogram of residuals and also performed a Shapiro-Wilk test on the data, the results of which are shown below:

<!-- b003712 | furniture | pages [12] -->


<!-- b003713 | prose | pages [12] -->
a) Prediction of Gold Medals

<!-- b003714 | furniture | pages [12] -->


<!-- b003715 | prose | pages [12] -->
b) Prediction of Total Medal Count

<!-- b003716 | caption | pages [12] -->
Figure 9 histogram of residuals

<!-- b003717 | caption | pages [12] -->
Table 7 Fitting data and SW test results

<!-- b003718 | prose | pages [12] -->
Standard Deviation Gold Medals 2.908 Total Medals 7.123 Skewness Kurtosis Shapiro-Wilk Test 4.723 35.429 0.438 -4.644 40.523 0.434

<!-- b003719 | prose | pages [12] -->
Based on the above graphs, it can be found that both predictive models have large peaks and skewness, and the significance of the Shapiro-Wilk test on the data is P<0.05, which indicates that both predictive models do not conform to a normal distribution.

<!-- b003720 | prose | pages [12] -->
So we compute the prediction interval using the t distribution

<!-- b003721 | prose | pages [12] -->
Prediction Interval=

<!-- b003722 | furniture | pages [12] -->


<!-- b003723 | prose | pages [12] -->
Among them.

<!-- b003724 | prose | pages [12] -->
y represents the predicted value,

<!-- b003725 | prose | pages [12] -->
    y t SE y

<!-- b003726 | furniture | pages [12] -->


<!-- b003727 | prose | pages [12] -->
(6)   2, n p

<!-- b003728 | prose | pages [12] -->
 is the quantile of the t-distribution, n is the t 2,n p

<!-- b003729 | prose | pages [12] -->
 SE y is the standard number of samples, p is the number of parameters in the model, and

<!-- b003730 | prose | pages [12] -->
error of the prediction. The correlation results were calculated as shown below:

<!-- b003731 | caption | pages [12] -->
Table 8 Prediction Model T-Distribution Related Data

<!-- b003732 | furniture | pages [12] -->


<!-- b003733 | prose | pages [12] -->
 t SE y  2,n p

<!-- b003734 | prose | pages [12] -->
Prediction of Gold Medals 2.404 2.908 Prediction of Total Medal Count 1.993 7.123

<!-- b003735 | prose | pages [12] -->
Then the prediction interval for the number of gold medals at the 95% confidence level is and the total prediction interval for the number of medals is   y  7

<!-- b003736 | furniture | pages [12] -->


<!-- b003737 | prose | pages [12] -->
y 

<!-- b003738 | furniture | pages [12] -->


<!-- b003739 | prose | pages [12] -->
15

<!-- b003740 | prose | pages [12] -->
关注数学模型

<!-- b003741 | furniture | pages [12] -->
2

<!-- b003742 | furniture | pages [12] -->
MATHmodels

<!-- b003743 | furniture | pages [12] -->
获取更多资讯

<!-- b003744 | furniture | pages [13] -->
Team#2507817                                                             Page 13 of 25

<!-- b003745 | prose | pages [13] -->
微信公众号：数学模型

<!-- b003746 | furniture | pages [13] -->


<!-- b003747 | furniture | pages [13] -->


<!-- b003748 | prose | pages [13] -->
(a) Prediction of Gold Medals b)  Prediction of Total Medal Count

<!-- b003749 | caption | pages [13] -->
Figure 10 Error bar chart of prediction model

<!-- b003750 | heading | pages [13] -->
5.2.3 Predicting progress and regressions in national performance

<!-- b003751 | prose | pages [13] -->
The question asked us to predict the countries most likely to advance or retreat, we

<!-- b003752 | prose | pages [13] -->
微信号：MATHmodels

<!-- b003753 | prose | pages [13] -->
calculated the predicted number of gold medals & total medals and the difference between the awards in 2024 to find the change in value, and plotted a histogram as shown below:

<!-- b003754 | furniture | pages [13] -->


<!-- b003755 | furniture | pages [13] -->


<!-- b003756 | prose | pages [13] -->
a) Gold medal, with fluctuations exceeding 2 b) Total medal, with fluctuations exceeding 5

<!-- b003757 | caption | pages [13] -->
Figure 11 Countries with significant fluctuations in medal numbers

<!-- b003758 | prose | pages [13] -->
The graphic shows that Great Britain had the most significant increase in gold medals and Germany had the most significant increase in total medals, both making significant progress. South Korea had the largest decrease in gold medals and China had the largest decrease in total medals. With the exception of the United States, the countries with significant gold medal growth also saw varying degrees of progress in total medals. The U.S. had more gold medal growth, but less significant total medal growth.

<!-- b003759 | heading | pages [13] -->
6 Task 2 Projections for Non-Awarded Countries

<!-- b003760 | prose | pages [13] -->
The question asks us to predict whether or not a country that has never won a medal will win its first medal at the 2028 Summer Olympics and to predict the probability of winning. The question is essentially a binary classification problem. The predicted outcomes are categorized into those that will win and those that will not. Therefore, we build a binary logistic regression model.

<!-- b003761 | heading | pages [13] -->
6.1 Bicategory Logistic Regression Modeling

<!-- b003762 | prose | pages [13] -->
We recorded non-winning countries as Category 1 if they could win at the 2028 Summer Olympics and Category 0 if they could not.

<!-- b003763 | heading | pages [13] -->
6.1.1 Sigmoid Function (math.)

<!-- b003764 | prose | pages [13] -->
Logistic regression is a generalized linear regression that combines a nonlinear function with a linear function to map it. We use the Sigmoid function to map the output value of a linear function to a probability between 0 and 1. The Sigmoid function formula is as follows:

<!-- b003765 | furniture | pages [13] -->


<!-- b003766 | furniture | pages [14] -->
Team#2507817                                                             Page 14 of 25

<!-- b003767 | prose | pages [14] -->


<!-- b003768 | furniture | pages [14] -->


<!-- b003769 | prose | pages [14] -->
( ) z

<!-- b003770 | prose | pages [14] -->
Among them:

<!-- b003771 | prose | pages [14] -->
   

<!-- b003772 | furniture | pages [14] -->


<!-- b003773 | prose | pages [14] -->
z a 1 k

<!-- b003774 | prose | pages [14] -->
 a e , , p is the input eigenvalue k k k

<!-- b003775 | prose | pages [14] -->
1 

<!-- b003776 | furniture | pages [14] -->


<!-- b003777 | prose | pages [14] -->
(7)  z 1 e

<!-- b003778 | prose | pages [14] -->
   e e p b

<!-- b003779 | furniture | pages [14] -->


<!-- b003780 | prose | pages [14] -->
(8) 2 2 k 3 k

<!-- b003781 | prose | pages [14] -->
ka : The number of athletes from the kth country in the 2028 Olympics. More athletes means

<!-- b003782 | prose | pages [14] -->
that more people can compete in more events, or more people can compete in the same event, which greatly increases the probability of winning.

<!-- b003783 | prose | pages [14] -->
ke : The number of events in which the kth country participates in the 2028 Olympics.

<!-- b003784 | prose | pages [14] -->
Participating in more events increases the probability of winning to some extent compared to concentrating on the same event.

<!-- b003785 | prose | pages [14] -->
m

<!-- b003786 | prose | pages [14] -->
m

<!-- b003787 | prose | pages [14] -->
m

<!-- b003788 | prose | pages [14] -->
m

<!-- b003789 | prose | pages [14] -->
m

<!-- b003790 | prose | pages [14] -->
m

<!-- b003791 | prose | pages [14] -->
m

<!-- b003792 | prose | pages [14] -->
m

<!-- b003793 | prose | pages [14] -->
m

<!-- b003794 | prose | pages [14] -->
m

<!-- b003795 | prose | pages [14] -->
m

<!-- b003796 | prose | pages [14] -->
m

<!-- b003797 | prose | pages [14] -->
m

<!-- b003798 | prose | pages [14] -->
m

<!-- b003799 | prose | pages [14] -->
m

<!-- b003800 | prose | pages [14] -->
m

<!-- b003801 | prose | pages [14] -->
m

<!-- b003802 | prose | pages [14] -->
m

<!-- b003803 | prose | pages [14] -->
m

<!-- b003804 | prose | pages [14] -->
m

<!-- b003805 | prose | pages [14] -->
m

<!-- b003806 | prose | pages [14] -->
m

<!-- b003807 | prose | pages [14] -->
m

<!-- b003808 | prose | pages [14] -->
m

<!-- b003809 | prose | pages [14] -->
m

<!-- b003810 | prose | pages [14] -->
m

<!-- b003811 | prose | pages [14] -->
m

<!-- b003812 | prose | pages [14] -->
m

<!-- b003813 | prose | pages [14] -->
m

<!-- b003814 | prose | pages [14] -->
m

<!-- b003815 | prose | pages [14] -->
m

<!-- b003816 | prose | pages [14] -->
m

<!-- b003817 | prose | pages [14] -->
m

<!-- b003818 | prose | pages [14] -->
m

<!-- b003819 | prose | pages [14] -->
m

<!-- b003820 | prose | pages [14] -->
m

<!-- b003821 | prose | pages [14] -->
m

<!-- b003822 | prose | pages [14] -->
m

<!-- b003823 | prose | pages [14] -->
m

<!-- b003824 | prose | pages [14] -->
m

<!-- b003825 | prose | pages [14] -->
m

<!-- b003826 | prose | pages [14] -->
m

<!-- b003827 | prose | pages [14] -->
m

<!-- b003828 | prose | pages [14] -->
m

<!-- b003829 | prose | pages [14] -->
m

<!-- b003830 | prose | pages [14] -->
m

<!-- b003831 | prose | pages [14] -->
m

<!-- b003832 | prose | pages [14] -->
m

<!-- b003833 | prose | pages [14] -->
m

<!-- b003834 | prose | pages [14] -->
m

<!-- b003835 | prose | pages [14] -->
m

<!-- b003836 | prose | pages [14] -->
m

<!-- b003837 | prose | pages [14] -->
m

<!-- b003838 | prose | pages [14] -->
m

<!-- b003839 | prose | pages [14] -->
m

<!-- b003840 | prose | pages [14] -->
m

<!-- b003841 | prose | pages [14] -->
m

<!-- b003842 | prose | pages [14] -->
m

<!-- b003843 | prose | pages [14] -->
m

<!-- b003844 | prose | pages [14] -->
m

<!-- b003845 | prose | pages [14] -->
m

<!-- b003846 | prose | pages [14] -->
m

<!-- b003847 | prose | pages [14] -->
m

<!-- b003848 | prose | pages [14] -->
m

<!-- b003849 | prose | pages [14] -->
m

<!-- b003850 | prose | pages [14] -->
m

<!-- b003851 | prose | pages [14] -->
m

<!-- b003852 | prose | pages [14] -->
m

<!-- b003853 | prose | pages [14] -->
m

<!-- b003854 | prose | pages [14] -->
m

<!-- b003855 | prose | pages [14] -->
m

<!-- b003856 | prose | pages [14] -->
m

<!-- b003857 | prose | pages [14] -->
m

<!-- b003858 | prose | pages [14] -->
m

<!-- b003859 | prose | pages [14] -->
m

<!-- b003860 | prose | pages [14] -->
m

<!-- b003861 | prose | pages [14] -->
m

<!-- b003862 | prose | pages [14] -->
m

<!-- b003863 | prose | pages [14] -->
m

<!-- b003864 | prose | pages [14] -->
m

<!-- b003865 | prose | pages [14] -->
m

<!-- b003866 | prose | pages [14] -->
m

<!-- b003867 | prose | pages [14] -->
m

<!-- b003868 | prose | pages [14] -->
m

<!-- b003869 | prose | pages [14] -->
m

<!-- b003870 | prose | pages [14] -->
m

<!-- b003871 | prose | pages [14] -->
m

<!-- b003872 | prose | pages [14] -->
m

<!-- b003873 | prose | pages [14] -->
m

<!-- b003874 | prose | pages [14] -->
m

<!-- b003875 | prose | pages [14] -->
m

<!-- b003876 | prose | pages [14] -->
m

<!-- b003877 | prose | pages [14] -->
m

<!-- b003878 | prose | pages [14] -->
m

<!-- b003879 | prose | pages [14] -->
m

<!-- b003880 | prose | pages [14] -->
m

<!-- b003881 | prose | pages [14] -->
m

<!-- b003882 | prose | pages [14] -->
m

<!-- b003883 | prose | pages [14] -->
m

<!-- b003884 | prose | pages [14] -->
m

<!-- b003885 | prose | pages [14] -->
m

<!-- b003886 | prose | pages [14] -->
m

<!-- b003887 | prose | pages [14] -->
m

<!-- b003888 | prose | pages [14] -->
m

<!-- b003889 | prose | pages [14] -->
m

<!-- b003890 | prose | pages [14] -->
m

<!-- b003891 | prose | pages [14] -->
m

<!-- b003892 | prose | pages [14] -->
m

<!-- b003893 | prose | pages [14] -->
m

<!-- b003894 | prose | pages [14] -->
m

<!-- b003895 | prose | pages [14] -->
m

<!-- b003896 | prose | pages [14] -->
m

<!-- b003897 | prose | pages [14] -->
m

<!-- b003898 | prose | pages [14] -->
m

<!-- b003899 | prose | pages [14] -->
m

<!-- b003900 | prose | pages [14] -->
m

<!-- b003901 | prose | pages [14] -->
m

<!-- b003902 | prose | pages [14] -->
m

<!-- b003903 | prose | pages [14] -->
m

<!-- b003904 | prose | pages [14] -->
m

<!-- b003905 | prose | pages [14] -->
m

<!-- b003906 | prose | pages [14] -->
m

<!-- b003907 | prose | pages [14] -->
m

<!-- b003908 | prose | pages [14] -->
m

<!-- b003909 | prose | pages [14] -->
m

<!-- b003910 | prose | pages [14] -->
m

<!-- b003911 | prose | pages [14] -->
m

<!-- b003912 | prose | pages [14] -->
m

<!-- b003913 | prose | pages [14] -->
m

<!-- b003914 | prose | pages [14] -->
m

<!-- b003915 | prose | pages [14] -->
m

<!-- b003916 | prose | pages [14] -->
m

<!-- b003917 | prose | pages [14] -->
m

<!-- b003918 | prose | pages [14] -->
m

<!-- b003919 | prose | pages [14] -->
m

<!-- b003920 | prose | pages [14] -->
m

<!-- b003921 | prose | pages [14] -->
m

<!-- b003922 | prose | pages [14] -->
m

<!-- b003923 | prose | pages [14] -->
m

<!-- b003924 | prose | pages [14] -->
m

<!-- b003925 | prose | pages [14] -->
m

<!-- b003926 | prose | pages [14] -->
m

<!-- b003927 | prose | pages [14] -->
m

<!-- b003928 | prose | pages [14] -->
m

<!-- b003929 | prose | pages [14] -->
m

<!-- b003930 | prose | pages [14] -->
m

<!-- b003931 | prose | pages [14] -->
m

<!-- b003932 | prose | pages [14] -->
m

<!-- b003933 | prose | pages [14] -->
m

<!-- b003934 | prose | pages [14] -->
m

<!-- b003935 | prose | pages [14] -->
m

<!-- b003936 | prose | pages [14] -->
m

<!-- b003937 | prose | pages [14] -->
m

<!-- b003938 | prose | pages [14] -->
m

<!-- b003939 | prose | pages [14] -->
m

<!-- b003940 | prose | pages [14] -->
m

<!-- b003941 | prose | pages [14] -->
m

<!-- b003942 | prose | pages [14] -->
m

<!-- b003943 | prose | pages [14] -->
m

<!-- b003944 | prose | pages [14] -->
m

<!-- b003945 | prose | pages [14] -->
m

<!-- b003946 | prose | pages [14] -->
m

<!-- b003947 | prose | pages [14] -->
m

<!-- b003948 | prose | pages [14] -->
m

<!-- b003949 | prose | pages [14] -->
m

<!-- b003950 | prose | pages [14] -->
m

<!-- b003951 | prose | pages [14] -->
m

<!-- b003952 | prose | pages [14] -->
m

<!-- b003953 | prose | pages [14] -->
m

<!-- b003954 | prose | pages [14] -->
m

<!-- b003955 | prose | pages [14] -->
m

<!-- b003956 | prose | pages [14] -->
m

<!-- b003957 | prose | pages [14] -->
m

<!-- b003958 | prose | pages [14] -->
m

<!-- b003959 | prose | pages [14] -->
m

<!-- b003960 | prose | pages [14] -->
m

<!-- b003961 | prose | pages [14] -->
m

<!-- b003962 | prose | pages [14] -->
m

<!-- b003963 | prose | pages [14] -->
m

<!-- b003964 | prose | pages [14] -->
m

<!-- b003965 | prose | pages [14] -->
m

<!-- b003966 | prose | pages [14] -->
m

<!-- b003967 | prose | pages [14] -->
m

<!-- b003968 | prose | pages [14] -->
m

<!-- b003969 | prose | pages [14] -->
m

<!-- b003970 | prose | pages [14] -->
m

<!-- b003971 | prose | pages [14] -->
m

<!-- b003972 | prose | pages [14] -->
m

<!-- b003973 | prose | pages [14] -->
m

<!-- b003974 | prose | pages [14] -->
m

<!-- b003975 | prose | pages [14] -->
m

<!-- b003976 | prose | pages [14] -->
m

<!-- b003977 | prose | pages [14] -->
m

<!-- b003978 | prose | pages [14] -->
m

<!-- b003979 | prose | pages [14] -->
m

<!-- b003980 | prose | pages [14] -->
m

<!-- b003981 | prose | pages [14] -->
m

<!-- b003982 | prose | pages [14] -->
m

<!-- b003983 | prose | pages [14] -->
m

<!-- b003984 | prose | pages [14] -->
m

<!-- b003985 | prose | pages [14] -->
m

<!-- b003986 | prose | pages [14] -->
m

<!-- b003987 | prose | pages [14] -->
m

<!-- b003988 | prose | pages [14] -->
m

<!-- b003989 | prose | pages [14] -->
m

<!-- b003990 | prose | pages [14] -->
m

<!-- b003991 | prose | pages [14] -->
m

<!-- b003992 | prose | pages [14] -->
m

<!-- b003993 | prose | pages [14] -->
m

<!-- b003994 | prose | pages [14] -->
m

<!-- b003995 | prose | pages [14] -->
m

<!-- b003996 | prose | pages [14] -->
m

<!-- b003997 | prose | pages [14] -->
m

<!-- b003998 | prose | pages [14] -->
m

<!-- b003999 | prose | pages [14] -->
m

<!-- b004000 | prose | pages [14] -->
m

<!-- b004001 | prose | pages [14] -->
m

<!-- b004002 | prose | pages [14] -->
m

<!-- b004003 | prose | pages [14] -->
m

<!-- b004004 | prose | pages [14] -->
m

<!-- b004005 | prose | pages [14] -->
m

<!-- b004006 | prose | pages [14] -->
m

<!-- b004007 | prose | pages [14] -->
m

<!-- b004008 | prose | pages [14] -->
m

<!-- b004009 | prose | pages [14] -->
m

<!-- b004010 | prose | pages [14] -->
m

<!-- b004011 | prose | pages [14] -->
m

<!-- b004012 | prose | pages [14] -->
m

<!-- b004013 | prose | pages [14] -->
m

<!-- b004014 | prose | pages [14] -->
m

<!-- b004015 | prose | pages [14] -->
m

<!-- b004016 | prose | pages [14] -->
m

<!-- b004017 | prose | pages [14] -->
m

<!-- b004018 | prose | pages [14] -->
m

<!-- b004019 | prose | pages [14] -->
m

<!-- b004020 | prose | pages [14] -->
m

<!-- b004021 | prose | pages [14] -->
m

<!-- b004022 | prose | pages [14] -->
m

<!-- b004023 | prose | pages [14] -->
m

<!-- b004024 | prose | pages [14] -->
m

<!-- b004025 | prose | pages [14] -->
m

<!-- b004026 | prose | pages [14] -->
m

<!-- b004027 | prose | pages [14] -->
m

<!-- b004028 | prose | pages [14] -->
m

<!-- b004029 | prose | pages [14] -->
m

<!-- b004030 | prose | pages [14] -->
m

<!-- b004031 | prose | pages [14] -->
m

<!-- b004032 | prose | pages [14] -->
m

<!-- b004033 | prose | pages [14] -->
m

<!-- b004034 | prose | pages [14] -->
m

<!-- b004035 | prose | pages [14] -->
m

<!-- b004036 | prose | pages [14] -->
m

<!-- b004037 | prose | pages [14] -->
m

<!-- b004038 | prose | pages [14] -->
m

<!-- b004039 | prose | pages [14] -->
m

<!-- b004040 | prose | pages [14] -->
m

<!-- b004041 | prose | pages [14] -->
m

<!-- b004042 | prose | pages [14] -->
m

<!-- b004043 | prose | pages [14] -->
m

<!-- b004044 | prose | pages [14] -->
m

<!-- b004045 | prose | pages [14] -->
m

<!-- b004046 | prose | pages [14] -->
m

<!-- b004047 | prose | pages [14] -->
m

<!-- b004048 | prose | pages [14] -->
m

<!-- b004049 | prose | pages [14] -->
m

<!-- b004050 | prose | pages [14] -->
m

<!-- b004051 | prose | pages [14] -->
m

<!-- b004052 | prose | pages [14] -->
m

<!-- b004053 | prose | pages [14] -->
m

<!-- b004054 | prose | pages [14] -->
m

<!-- b004055 | prose | pages [14] -->
m

<!-- b004056 | prose | pages [14] -->
m

<!-- b004057 | prose | pages [14] -->
m

<!-- b004058 | prose | pages [14] -->
m

<!-- b004059 | prose | pages [14] -->
m

<!-- b004060 | prose | pages [14] -->
m

<!-- b004061 | prose | pages [14] -->
m

<!-- b004062 | prose | pages [14] -->
m

<!-- b004063 | prose | pages [14] -->
m

<!-- b004064 | prose | pages [14] -->
m

<!-- b004065 | prose | pages [14] -->
m

<!-- b004066 | prose | pages [14] -->
m

<!-- b004067 | prose | pages [14] -->
m

<!-- b004068 | prose | pages [14] -->
m

<!-- b004069 | prose | pages [14] -->
m

<!-- b004070 | prose | pages [14] -->
m

<!-- b004071 | prose | pages [14] -->
m

<!-- b004072 | prose | pages [14] -->
m

<!-- b004073 | prose | pages [14] -->
m

<!-- b004074 | prose | pages [14] -->
m

<!-- b004075 | prose | pages [14] -->
m

<!-- b004076 | prose | pages [14] -->
m

<!-- b004077 | prose | pages [14] -->
m

<!-- b004078 | prose | pages [14] -->
m

<!-- b004079 | prose | pages [14] -->
m

<!-- b004080 | prose | pages [14] -->
m

<!-- b004081 | prose | pages [14] -->
kp : Historical participation of the kth country: the more a country participates in international

<!-- b004082 | prose | pages [14] -->
m

<!-- b004083 | prose | pages [14] -->
m

<!-- b004084 | prose | pages [14] -->
m

<!-- b004085 | prose | pages [14] -->
m

<!-- b004086 | prose | pages [14] -->
m

<!-- b004087 | prose | pages [14] -->
m

<!-- b004088 | prose | pages [14] -->
m

<!-- b004089 | prose | pages [14] -->
m

<!-- b004090 | prose | pages [14] -->
m

<!-- b004091 | prose | pages [14] -->
m

<!-- b004092 | prose | pages [14] -->
m

<!-- b004093 | prose | pages [14] -->
m

<!-- b004094 | prose | pages [14] -->
m

<!-- b004095 | prose | pages [14] -->
m

<!-- b004096 | prose | pages [14] -->
m

<!-- b004097 | prose | pages [14] -->
m

<!-- b004098 | prose | pages [14] -->
m

<!-- b004099 | prose | pages [14] -->
m

<!-- b004100 | prose | pages [14] -->
m

<!-- b004101 | prose | pages [14] -->
m

<!-- b004102 | prose | pages [14] -->
m

<!-- b004103 | prose | pages [14] -->
m

<!-- b004104 | prose | pages [14] -->
m

<!-- b004105 | prose | pages [14] -->
m

<!-- b004106 | prose | pages [14] -->
m

<!-- b004107 | prose | pages [14] -->
m

<!-- b004108 | prose | pages [14] -->
m

<!-- b004109 | prose | pages [14] -->
m

<!-- b004110 | prose | pages [14] -->
m

<!-- b004111 | prose | pages [14] -->
m

<!-- b004112 | prose | pages [14] -->
m

<!-- b004113 | prose | pages [14] -->
m

<!-- b004114 | prose | pages [14] -->
m

<!-- b004115 | prose | pages [14] -->
m

<!-- b004116 | prose | pages [14] -->
m

<!-- b004117 | prose | pages [14] -->
m

<!-- b004118 | prose | pages [14] -->
m

<!-- b004119 | prose | pages [14] -->
m

<!-- b004120 | prose | pages [14] -->
m

<!-- b004121 | prose | pages [14] -->
m

<!-- b004122 | prose | pages [14] -->
m

<!-- b004123 | prose | pages [14] -->
m

<!-- b004124 | prose | pages [14] -->
m

<!-- b004125 | prose | pages [14] -->
m

<!-- b004126 | prose | pages [14] -->
m

<!-- b004127 | prose | pages [14] -->
m

<!-- b004128 | prose | pages [14] -->
m

<!-- b004129 | prose | pages [14] -->
m

<!-- b004130 | prose | pages [14] -->
m

<!-- b004131 | prose | pages [14] -->
m

<!-- b004132 | prose | pages [14] -->
m

<!-- b004133 | prose | pages [14] -->
m

<!-- b004134 | prose | pages [14] -->
m

<!-- b004135 | prose | pages [14] -->
m

<!-- b004136 | prose | pages [14] -->
m

<!-- b004137 | prose | pages [14] -->
m

<!-- b004138 | prose | pages [14] -->
m

<!-- b004139 | prose | pages [14] -->
m

<!-- b004140 | prose | pages [14] -->
m

<!-- b004141 | prose | pages [14] -->
m

<!-- b004142 | prose | pages [14] -->
m

<!-- b004143 | prose | pages [14] -->
m

<!-- b004144 | prose | pages [14] -->
m

<!-- b004145 | prose | pages [14] -->
m

<!-- b004146 | prose | pages [14] -->
m

<!-- b004147 | prose | pages [14] -->
m

<!-- b004148 | prose | pages [14] -->
m

<!-- b004149 | prose | pages [14] -->
m

<!-- b004150 | prose | pages [14] -->
m

<!-- b004151 | prose | pages [14] -->
m

<!-- b004152 | prose | pages [14] -->
m

<!-- b004153 | prose | pages [14] -->
m

<!-- b004154 | prose | pages [14] -->
m

<!-- b004155 | prose | pages [14] -->
m

<!-- b004156 | prose | pages [14] -->
m

<!-- b004157 | prose | pages [14] -->
m

<!-- b004158 | prose | pages [14] -->
m

<!-- b004159 | prose | pages [14] -->
m

<!-- b004160 | prose | pages [14] -->
m

<!-- b004161 | prose | pages [14] -->
m

<!-- b004162 | prose | pages [14] -->
m

<!-- b004163 | prose | pages [14] -->
m

<!-- b004164 | prose | pages [14] -->
m

<!-- b004165 | prose | pages [14] -->
m

<!-- b004166 | prose | pages [14] -->
m

<!-- b004167 | prose | pages [14] -->
m

<!-- b004168 | prose | pages [14] -->
m

<!-- b004169 | prose | pages [14] -->
m

<!-- b004170 | prose | pages [14] -->
m

<!-- b004171 | prose | pages [14] -->
m

<!-- b004172 | prose | pages [14] -->
m

<!-- b004173 | prose | pages [14] -->
m

<!-- b004174 | prose | pages [14] -->
m

<!-- b004175 | prose | pages [14] -->
m

<!-- b004176 | prose | pages [14] -->
m

<!-- b004177 | prose | pages [14] -->
m

<!-- b004178 | prose | pages [14] -->
m

<!-- b004179 | prose | pages [14] -->
m

<!-- b004180 | prose | pages [14] -->
m

<!-- b004181 | prose | pages [14] -->
m

<!-- b004182 | prose | pages [14] -->
m

<!-- b004183 | prose | pages [14] -->
m

<!-- b004184 | prose | pages [14] -->
m

<!-- b004185 | prose | pages [14] -->
m

<!-- b004186 | prose | pages [14] -->
m

<!-- b004187 | prose | pages [14] -->
m

<!-- b004188 | prose | pages [14] -->
m

<!-- b004189 | prose | pages [14] -->
m

<!-- b004190 | prose | pages [14] -->
m

<!-- b004191 | prose | pages [14] -->
m

<!-- b004192 | prose | pages [14] -->
m

<!-- b004193 | prose | pages [14] -->
m

<!-- b004194 | prose | pages [14] -->
m

<!-- b004195 | prose | pages [14] -->
m

<!-- b004196 | prose | pages [14] -->
m

<!-- b004197 | prose | pages [14] -->
m

<!-- b004198 | prose | pages [14] -->
m

<!-- b004199 | prose | pages [14] -->
m

<!-- b004200 | prose | pages [14] -->
m

<!-- b004201 | prose | pages [14] -->
m

<!-- b004202 | prose | pages [14] -->
m

<!-- b004203 | prose | pages [14] -->
m

<!-- b004204 | prose | pages [14] -->
m

<!-- b004205 | prose | pages [14] -->
m

<!-- b004206 | prose | pages [14] -->
m

<!-- b004207 | prose | pages [14] -->
m

<!-- b004208 | prose | pages [14] -->
m

<!-- b004209 | prose | pages [14] -->
m

<!-- b004210 | prose | pages [14] -->
m

<!-- b004211 | prose | pages [14] -->
m

<!-- b004212 | prose | pages [14] -->
m

<!-- b004213 | prose | pages [14] -->
m

<!-- b004214 | prose | pages [14] -->
m

<!-- b004215 | prose | pages [14] -->
m

<!-- b004216 | prose | pages [14] -->
m

<!-- b004217 | prose | pages [14] -->
m

<!-- b004218 | prose | pages [14] -->
m

<!-- b004219 | prose | pages [14] -->
m

<!-- b004220 | prose | pages [14] -->
m

<!-- b004221 | prose | pages [14] -->
m

<!-- b004222 | prose | pages [14] -->
m

<!-- b004223 | prose | pages [14] -->
m

<!-- b004224 | prose | pages [14] -->
m

<!-- b004225 | prose | pages [14] -->
m

<!-- b004226 | prose | pages [14] -->
m

<!-- b004227 | prose | pages [14] -->
m

<!-- b004228 | prose | pages [14] -->
m

<!-- b004229 | prose | pages [14] -->
m

<!-- b004230 | prose | pages [14] -->
m

<!-- b004231 | prose | pages [14] -->
m

<!-- b004232 | prose | pages [14] -->
m

<!-- b004233 | prose | pages [14] -->
m

<!-- b004234 | prose | pages [14] -->
m

<!-- b004235 | prose | pages [14] -->
m

<!-- b004236 | prose | pages [14] -->
m

<!-- b004237 | prose | pages [14] -->
m

<!-- b004238 | prose | pages [14] -->
m

<!-- b004239 | prose | pages [14] -->
m

<!-- b004240 | prose | pages [14] -->
m

<!-- b004241 | prose | pages [14] -->
m

<!-- b004242 | prose | pages [14] -->
m

<!-- b004243 | prose | pages [14] -->
m

<!-- b004244 | prose | pages [14] -->
m

<!-- b004245 | prose | pages [14] -->
m

<!-- b004246 | prose | pages [14] -->
m

<!-- b004247 | prose | pages [14] -->
m

<!-- b004248 | prose | pages [14] -->
m

<!-- b004249 | prose | pages [14] -->
m

<!-- b004250 | prose | pages [14] -->
m

<!-- b004251 | prose | pages [14] -->
m

<!-- b004252 | prose | pages [14] -->
m

<!-- b004253 | prose | pages [14] -->
m

<!-- b004254 | prose | pages [14] -->
m

<!-- b004255 | prose | pages [14] -->
m

<!-- b004256 | prose | pages [14] -->
m

<!-- b004257 | prose | pages [14] -->
m

<!-- b004258 | prose | pages [14] -->
m

<!-- b004259 | prose | pages [14] -->
m

<!-- b004260 | prose | pages [14] -->
m

<!-- b004261 | prose | pages [14] -->
m

<!-- b004262 | prose | pages [14] -->
m

<!-- b004263 | prose | pages [14] -->
m

<!-- b004264 | prose | pages [14] -->
m

<!-- b004265 | prose | pages [14] -->
m

<!-- b004266 | prose | pages [14] -->
m

<!-- b004267 | prose | pages [14] -->
m

<!-- b004268 | prose | pages [14] -->
events, the more experience it accumulates, which can largely increase its probability of winning.

<!-- b004269 | prose | pages [14] -->
   

<!-- b004270 | prose | pages [14] -->
m

<!-- b004271 | prose | pages [14] -->
m

<!-- b004272 | prose | pages [14] -->
m

<!-- b004273 | prose | pages [14] -->
m

<!-- b004274 | prose | pages [14] -->
m

<!-- b004275 | prose | pages [14] -->
m

<!-- b004276 | prose | pages [14] -->
m

<!-- b004277 | prose | pages [14] -->
m

<!-- b004278 | prose | pages [14] -->
m

<!-- b004279 | prose | pages [14] -->
m

<!-- b004280 | prose | pages [14] -->
m

<!-- b004281 | prose | pages [14] -->
m

<!-- b004282 | prose | pages [14] -->
m

<!-- b004283 | prose | pages [14] -->
m

<!-- b004284 | prose | pages [14] -->
m

<!-- b004285 | prose | pages [14] -->
m

<!-- b004286 | prose | pages [14] -->
m

<!-- b004287 | prose | pages [14] -->
m

<!-- b004288 | prose | pages [14] -->
m

<!-- b004289 | prose | pages [14] -->
m

<!-- b004290 | prose | pages [14] -->
m

<!-- b004291 | prose | pages [14] -->
m

<!-- b004292 | prose | pages [14] -->
m

<!-- b004293 | prose | pages [14] -->
m

<!-- b004294 | prose | pages [14] -->
m

<!-- b004295 | prose | pages [14] -->
m

<!-- b004296 | prose | pages [14] -->
m

<!-- b004297 | prose | pages [14] -->
m

<!-- b004298 | prose | pages [14] -->
m

<!-- b004299 | prose | pages [14] -->
m

<!-- b004300 | prose | pages [14] -->
m

<!-- b004301 | prose | pages [14] -->
m

<!-- b004302 | prose | pages [14] -->
m

<!-- b004303 | prose | pages [14] -->
m

<!-- b004304 | prose | pages [14] -->
m

<!-- b004305 | prose | pages [14] -->
m

<!-- b004306 | prose | pages [14] -->
m

<!-- b004307 | prose | pages [14] -->
m

<!-- b004308 | prose | pages [14] -->
m

<!-- b004309 | prose | pages [14] -->
m

<!-- b004310 | prose | pages [14] -->
m

<!-- b004311 | prose | pages [14] -->
m

<!-- b004312 | prose | pages [14] -->
m

<!-- b004313 | prose | pages [14] -->
m

<!-- b004314 | prose | pages [14] -->
m

<!-- b004315 | prose | pages [14] -->
m

<!-- b004316 | prose | pages [14] -->
m

<!-- b004317 | prose | pages [14] -->
m

<!-- b004318 | prose | pages [14] -->
m

<!-- b004319 | prose | pages [14] -->
m

<!-- b004320 | prose | pages [14] -->
m

<!-- b004321 | prose | pages [14] -->
m

<!-- b004322 | prose | pages [14] -->
m

<!-- b004323 | prose | pages [14] -->
m

<!-- b004324 | prose | pages [14] -->
m

<!-- b004325 | prose | pages [14] -->
m

<!-- b004326 | prose | pages [14] -->
m

<!-- b004327 | prose | pages [14] -->
m

<!-- b004328 | prose | pages [14] -->
m

<!-- b004329 | prose | pages [14] -->
m

<!-- b004330 | prose | pages [14] -->
m

<!-- b004331 | prose | pages [14] -->
m

<!-- b004332 | prose | pages [14] -->
m

<!-- b004333 | prose | pages [14] -->
m

<!-- b004334 | prose | pages [14] -->
m

<!-- b004335 | prose | pages [14] -->
m

<!-- b004336 | prose | pages [14] -->
m

<!-- b004337 | prose | pages [14] -->
m

<!-- b004338 | prose | pages [14] -->
m

<!-- b004339 | prose | pages [14] -->
m

<!-- b004340 | prose | pages [14] -->
m

<!-- b004341 | prose | pages [14] -->
m

<!-- b004342 | prose | pages [14] -->
m

<!-- b004343 | prose | pages [14] -->
m

<!-- b004344 | prose | pages [14] -->
m

<!-- b004345 | prose | pages [14] -->
m

<!-- b004346 | prose | pages [14] -->
m

<!-- b004347 | prose | pages [14] -->
m

<!-- b004348 | prose | pages [14] -->
m

<!-- b004349 | prose | pages [14] -->
m

<!-- b004350 | prose | pages [14] -->
m

<!-- b004351 | prose | pages [14] -->
m

<!-- b004352 | prose | pages [14] -->
m

<!-- b004353 | prose | pages [14] -->
m

<!-- b004354 | prose | pages [14] -->
m

<!-- b004355 | prose | pages [14] -->
m

<!-- b004356 | prose | pages [14] -->
m

<!-- b004357 | prose | pages [14] -->
m

<!-- b004358 | prose | pages [14] -->
m

<!-- b004359 | prose | pages [14] -->
m

<!-- b004360 | prose | pages [14] -->
m

<!-- b004361 | prose | pages [14] -->
m

<!-- b004362 | prose | pages [14] -->
m

<!-- b004363 | prose | pages [14] -->
m

<!-- b004364 | prose | pages [14] -->
m

<!-- b004365 | prose | pages [14] -->
m

<!-- b004366 | prose | pages [14] -->
m

<!-- b004367 | prose | pages [14] -->
m

<!-- b004368 | prose | pages [14] -->
m

<!-- b004369 | prose | pages [14] -->
m

<!-- b004370 | prose | pages [14] -->
m

<!-- b004371 | prose | pages [14] -->
m

<!-- b004372 | prose | pages [14] -->
m

<!-- b004373 | prose | pages [14] -->
m

<!-- b004374 | prose | pages [14] -->
m

<!-- b004375 | prose | pages [14] -->
m

<!-- b004376 | prose | pages [14] -->
m

<!-- b004377 | prose | pages [14] -->
m

<!-- b004378 | prose | pages [14] -->
m

<!-- b004379 | prose | pages [14] -->
m

<!-- b004380 | prose | pages [14] -->
m

<!-- b004381 | prose | pages [14] -->
m

<!-- b004382 | prose | pages [14] -->
m

<!-- b004383 | prose | pages [14] -->
m

<!-- b004384 | prose | pages [14] -->
m

<!-- b004385 | prose | pages [14] -->
m

<!-- b004386 | prose | pages [14] -->
m

<!-- b004387 | prose | pages [14] -->
m

<!-- b004388 | prose | pages [14] -->
m

<!-- b004389 | prose | pages [14] -->
m

<!-- b004390 | prose | pages [14] -->
m

<!-- b004391 | prose | pages [14] -->
m

<!-- b004392 | prose | pages [14] -->
m

<!-- b004393 | prose | pages [14] -->
m

<!-- b004394 | prose | pages [14] -->
m

<!-- b004395 | prose | pages [14] -->
m

<!-- b004396 | prose | pages [14] -->
m

<!-- b004397 | prose | pages [14] -->
m

<!-- b004398 | prose | pages [14] -->
m

<!-- b004399 | prose | pages [14] -->
m

<!-- b004400 | prose | pages [14] -->
m

<!-- b004401 | prose | pages [14] -->
m

<!-- b004402 | prose | pages [14] -->
m

<!-- b004403 | prose | pages [14] -->
m

<!-- b004404 | prose | pages [14] -->
m

<!-- b004405 | prose | pages [14] -->
m

<!-- b004406 | prose | pages [14] -->
m

<!-- b004407 | prose | pages [14] -->
m

<!-- b004408 | prose | pages [14] -->
m

<!-- b004409 | prose | pages [14] -->
m

<!-- b004410 | prose | pages [14] -->
m

<!-- b004411 | prose | pages [14] -->
m

<!-- b004412 | prose | pages [14] -->
m

<!-- b004413 | prose | pages [14] -->
m

<!-- b004414 | prose | pages [14] -->
m

<!-- b004415 | prose | pages [14] -->
m

<!-- b004416 | prose | pages [14] -->
m

<!-- b004417 | prose | pages [14] -->
m

<!-- b004418 | prose | pages [14] -->
m

<!-- b004419 | prose | pages [14] -->
m

<!-- b004420 | prose | pages [14] -->
m

<!-- b004421 | prose | pages [14] -->
m

<!-- b004422 | prose | pages [14] -->
m

<!-- b004423 | prose | pages [14] -->
m

<!-- b004424 | prose | pages [14] -->
m

<!-- b004425 | prose | pages [14] -->
m

<!-- b004426 | prose | pages [14] -->
m

<!-- b004427 | prose | pages [14] -->
m

<!-- b004428 | prose | pages [14] -->
m

<!-- b004429 | prose | pages [14] -->
m

<!-- b004430 | prose | pages [14] -->
m

<!-- b004431 | prose | pages [14] -->
m

<!-- b004432 | prose | pages [14] -->
m

<!-- b004433 | prose | pages [14] -->
m

<!-- b004434 | prose | pages [14] -->
m

<!-- b004435 | prose | pages [14] -->
m

<!-- b004436 | prose | pages [14] -->
m

<!-- b004437 | prose | pages [14] -->
m

<!-- b004438 | prose | pages [14] -->
m

<!-- b004439 | prose | pages [14] -->
m

<!-- b004440 | prose | pages [14] -->
m

<!-- b004441 | prose | pages [14] -->
m

<!-- b004442 | prose | pages [14] -->
m

<!-- b004443 | prose | pages [14] -->
m

<!-- b004444 | prose | pages [14] -->
m

<!-- b004445 | prose | pages [14] -->
m

<!-- b004446 | prose | pages [14] -->
m

<!-- b004447 | prose | pages [14] -->
m

<!-- b004448 | prose | pages [14] -->
m

<!-- b004449 | prose | pages [14] -->
m

<!-- b004450 | prose | pages [14] -->
m

<!-- b004451 | prose | pages [14] -->
m

<!-- b004452 | prose | pages [14] -->
m

<!-- b004453 | prose | pages [14] -->
m

<!-- b004454 | prose | pages [14] -->
m

<!-- b004455 | prose | pages [14] -->
m

<!-- b004456 | prose | pages [14] -->
m

<!-- b004457 | prose | pages [14] -->
m

<!-- b004458 | prose | pages [14] -->
m

<!-- b004459 | prose | pages [14] -->
m

<!-- b004460 | prose | pages [14] -->
m

<!-- b004461 | prose | pages [14] -->
m

<!-- b004462 | prose | pages [14] -->
m

<!-- b004463 | prose | pages [14] -->
m

<!-- b004464 | prose | pages [14] -->
m

<!-- b004465 | prose | pages [14] -->
m

<!-- b004466 | prose | pages [14] -->
m

<!-- b004467 | prose | pages [14] -->
m

<!-- b004468 | prose | pages [14] -->
m

<!-- b004469 | prose | pages [14] -->
m

<!-- b004470 | prose | pages [14] -->
m

<!-- b004471 | prose | pages [14] -->
m

<!-- b004472 | prose | pages [14] -->
m

<!-- b004473 | prose | pages [14] -->
m

<!-- b004474 | prose | pages [14] -->
m

<!-- b004475 | prose | pages [14] -->
are the weights and we calculate their values using gradient descent. , , , 1 2 n

<!-- b004476 | prose | pages [14] -->
 b is the bias term

<!-- b004477 | prose | pages [14] -->
When the output of the sigmoid function is close to 1, the probability that the country belongs to category 1 is considered higher, i.e. the probability of winning the prize is higher. When the output value is close to 0, the probability that the country belongs to category 0 is higher, i.e. the probability of not winning the prize is higher.

<!-- b004478 | heading | pages [14] -->
6.1.2 Introducing the Loss Function

<!-- b004479 | prose | pages [14] -->
1      P z 0 | Let , we get p ( ) z i  z 1 e

<!-- b004480 | prose | pages [14] -->
 

<!-- b004481 | furniture | pages [14] -->


<!-- b004482 | prose | pages [14] -->
P y x | , ) （

<!-- b004483 | prose | pages [14] -->
       x x 1 P z 1| x 1 p , then i

<!-- b004484 | prose | pages [14] -->
  y 1 y

<!-- b004485 | furniture | pages [14] -->


<!-- b004486 | prose | pages [14] -->
(9) ( ( p ) (1 p ) i i

<!-- b004487 | prose | pages [14] -->
To further optimize the model, we introduce a cross-entropy loss function (log loss) to measure the gap between the model's predicted probability and the true category, log loss is defined as follows:

<!-- b004488 | prose | pages [14] -->
m

<!-- b004489 | prose | pages [14] -->


<!-- b004490 | prose | pages [14] -->
 

<!-- b004491 | prose | pages [14] -->
 

<!-- b004492 | furniture | pages [14] -->


<!-- b004493 | prose | pages [14] -->
L z

<!-- b004494 | prose | pages [14] -->
ln

<!-- b004495 | prose | pages [14] -->
p

<!-- b004496 | prose | pages [14] -->


<!-- b004497 | prose | pages [14] -->
i i

<!-- b004498 | prose | pages [14] -->


<!-- b004499 | prose | pages [14] -->
i

<!-- b004500 | prose | pages [14] -->
1

<!-- b004501 | prose | pages [14] -->
  

<!-- b004502 | prose | pages [14] -->
    

<!-- b004503 | furniture | pages [14] -->


<!-- b004504 | prose | pages [14] -->
(10)

<!-- b004505 | prose | pages [14] -->
1

<!-- b004506 | prose | pages [14] -->
z

<!-- b004507 | prose | pages [14] -->
ln 1

<!-- b004508 | prose | pages [14] -->
p

<!-- b004509 | prose | pages [14] -->


<!-- b004510 | prose | pages [14] -->
i i

<!-- b004511 | prose | pages [14] -->
ip is the predicted probability of the model; and m is the where iz is the true category; sample size.

<!-- b004512 | prose | pages [14] -->
6.2

<!-- b004513 | heading | pages [14] -->
Bicategory Logistic Regression Results

<!-- b004514 | prose | pages [14] -->
The results of the parameters of the model were calculated using MATLAB as shown in the table below:

<!-- b004515 | furniture | pages [14] -->


<!-- b004516 | furniture | pages [14] -->


<!-- b004517 | furniture | pages [14] -->


<!-- b004518 | furniture | pages [14] -->


<!-- b004519 | prose | pages [14] -->
关注数学模型

<!-- b004520 | furniture | pages [14] -->
2

<!-- b004521 | furniture | pages [14] -->
MATHmodels

<!-- b004522 | furniture | pages [14] -->
获取更多资讯

<!-- b004523 | furniture | pages [15] -->
Team#2507817                                                             Page 15 of 25

<!-- b004524 | caption | pages [15] -->
Table 9 Parameter results of Binary Logistic Regression Model

<!-- b004525 | prose | pages [15] -->
Regression Coefficient b 2.425

<!-- b004526 | prose | pages [15] -->
ka -0.012

<!-- b004527 | prose | pages [15] -->
ke -0.068

<!-- b004528 | prose | pages [15] -->
kp -0.013

<!-- b004529 | prose | pages [15] -->
Standard Error Waid P 0.098 607.134 <0.01

<!-- b004530 | prose | pages [15] -->
0.004 10.62 <0.01

<!-- b004531 | prose | pages [15] -->
0.008 76.036 <0.01

<!-- b004532 | prose | pages [15] -->
0.010 1.665 0.197

<!-- b004533 | prose | pages [15] -->
kp corresponds to P>0.05, which indicates that As can be seen from the table, kp has no effect on the predicted results. We stipulate that a dependent variable of 1 represents that the non-winning country can win at the 2028 Summer Olympics. A dependent variable of 0 represents not being able to win a prize. The regression equation for whether or not the non- winning country wins the 2028 Olympics is derived:

<!-- b004534 | prose | pages [15] -->
  

<!-- b004535 | prose | pages [15] -->
微信公众号：数学模型

<!-- b004536 | furniture | pages [15] -->


<!-- b004537 | prose | pages [15] -->
z 0.012 a k

<!-- b004538 | heading | pages [15] -->
6.2.1 Model Evaluation and Modification

<!-- b004539 | prose | pages [15] -->
0.068 e 2.425

<!-- b004540 | furniture | pages [15] -->


<!-- b004541 | prose | pages [15] -->
(11) k

<!-- b004542 | prose | pages [15] -->
In order to evaluate the classification effectiveness of the model, we start with the sensitivity and specificity of the model:

<!-- b004543 | prose | pages [15] -->
 Sensitivity (TPR): the proportion of results that are actually positive samples that are

<!-- b004544 | prose | pages [15] -->
predicted to be positive samples.

<!-- b004545 | prose | pages [15] -->
 Specificity (FPR): the proportion of results that are actually negative samples that are

<!-- b004546 | prose | pages [15] -->
predicted to be positive samples.

<!-- b004547 | prose | pages [15] -->
 AUC: is the area under the ROC curve and is used to measure the overall performance

<!-- b004548 | prose | pages [15] -->
微信号：MATHmodels

<!-- b004549 | prose | pages [15] -->
of the binary classification model.

<!-- b004550 | prose | pages [15] -->
The ROC curve of the model is plotted as shown below:

<!-- b004551 | furniture | pages [15] -->


<!-- b004552 | furniture | pages [15] -->


<!-- b004553 | caption | pages [15] -->
Figure 13 Hybrid Matrix Thermodynamic Diagram

<!-- b004554 | caption | pages [15] -->
Figure 12 ROC curve

<!-- b004555 | furniture | pages [15] -->


<!-- b004556 | prose | pages [15] -->
The ROC plot combines sensitivity (TPR) and specificity (FPR), which can measure the relationship simultaneously. Ideally, TPR should be close to 1, FPR should be close to 0, and the AUC value should be close to 1. Calculation from the ROC graph shows that AUC = 0.918. It can be seen that the sensitivity of this model is good.

<!-- b004557 | prose | pages [15] -->
To further measure the classification effectiveness of logistic regression through quantitative metrics, a heat map of the confusion matrix was drawn as shown above. Based on this, the classification evaluation metrics of the model are calculated as shown in the table below

<!-- b004558 | furniture | pages [15] -->


<!-- b004559 | furniture | pages [15] -->


<!-- b004560 | furniture | pages [16] -->
Team#2507817                                                             Page 16 of 25

<!-- b004561 | caption | pages [16] -->
Table 10 Classification Evaluation Index

<!-- b004562 | prose | pages [16] -->
Accuracy Recall 0.841 0.841 Precision F1 0.848 0.839

<!-- b004563 | prose | pages [16] -->
 Accuracy:The proportion of positive samples to the total samples, the greater the

<!-- b004564 | prose | pages [16] -->
accuracy, the better.

<!-- b004565 | prose | pages [16] -->
m

<!-- b004566 | prose | pages [16] -->
m

<!-- b004567 | prose | pages [16] -->
m

<!-- b004568 | prose | pages [16] -->
m

<!-- b004569 | prose | pages [16] -->
m

<!-- b004570 | prose | pages [16] -->
m

<!-- b004571 | prose | pages [16] -->
m

<!-- b004572 | prose | pages [16] -->
m

<!-- b004573 | prose | pages [16] -->
m

<!-- b004574 | prose | pages [16] -->
m

<!-- b004575 | prose | pages [16] -->
m

<!-- b004576 | prose | pages [16] -->
m

<!-- b004577 | prose | pages [16] -->
m

<!-- b004578 | prose | pages [16] -->
m

<!-- b004579 | prose | pages [16] -->
m

<!-- b004580 | prose | pages [16] -->
m

<!-- b004581 | prose | pages [16] -->
m

<!-- b004582 | prose | pages [16] -->
m

<!-- b004583 | prose | pages [16] -->
m

<!-- b004584 | prose | pages [16] -->
m

<!-- b004585 | prose | pages [16] -->
m

<!-- b004586 | prose | pages [16] -->
m

<!-- b004587 | prose | pages [16] -->
m

<!-- b004588 | prose | pages [16] -->
m

<!-- b004589 | prose | pages [16] -->
m

<!-- b004590 | prose | pages [16] -->
m

<!-- b004591 | prose | pages [16] -->
m

<!-- b004592 | prose | pages [16] -->
m

<!-- b004593 | prose | pages [16] -->
m

<!-- b004594 | prose | pages [16] -->
m

<!-- b004595 | prose | pages [16] -->
m

<!-- b004596 | prose | pages [16] -->
m

<!-- b004597 | prose | pages [16] -->
m

<!-- b004598 | prose | pages [16] -->
m

<!-- b004599 | prose | pages [16] -->
m

<!-- b004600 | prose | pages [16] -->
m

<!-- b004601 | prose | pages [16] -->
m

<!-- b004602 | prose | pages [16] -->
m

<!-- b004603 | prose | pages [16] -->
m

<!-- b004604 | prose | pages [16] -->
m

<!-- b004605 | prose | pages [16] -->
m

<!-- b004606 | prose | pages [16] -->
m

<!-- b004607 | prose | pages [16] -->
m

<!-- b004608 | prose | pages [16] -->
m

<!-- b004609 | prose | pages [16] -->
m

<!-- b004610 | prose | pages [16] -->
m

<!-- b004611 | prose | pages [16] -->
m

<!-- b004612 | prose | pages [16] -->
m

<!-- b004613 | prose | pages [16] -->
m

<!-- b004614 | prose | pages [16] -->
m

<!-- b004615 | prose | pages [16] -->
m

<!-- b004616 | prose | pages [16] -->
m

<!-- b004617 | prose | pages [16] -->
m

<!-- b004618 | prose | pages [16] -->
m

<!-- b004619 | prose | pages [16] -->
m

<!-- b004620 | prose | pages [16] -->
m

<!-- b004621 | prose | pages [16] -->
m

<!-- b004622 | prose | pages [16] -->
m

<!-- b004623 | prose | pages [16] -->
m

<!-- b004624 | prose | pages [16] -->
m

<!-- b004625 | prose | pages [16] -->
m

<!-- b004626 | prose | pages [16] -->
m

<!-- b004627 | prose | pages [16] -->
m

<!-- b004628 | prose | pages [16] -->
m

<!-- b004629 | prose | pages [16] -->
m

<!-- b004630 | prose | pages [16] -->
m

<!-- b004631 | prose | pages [16] -->
m

<!-- b004632 | prose | pages [16] -->
m

<!-- b004633 | prose | pages [16] -->
m

<!-- b004634 | prose | pages [16] -->
m

<!-- b004635 | prose | pages [16] -->
m

<!-- b004636 | prose | pages [16] -->
m

<!-- b004637 | prose | pages [16] -->
m

<!-- b004638 | prose | pages [16] -->
m

<!-- b004639 | prose | pages [16] -->
m

<!-- b004640 | prose | pages [16] -->
m

<!-- b004641 | prose | pages [16] -->
m

<!-- b004642 | prose | pages [16] -->
m

<!-- b004643 | prose | pages [16] -->
m

<!-- b004644 | prose | pages [16] -->
m

<!-- b004645 | prose | pages [16] -->
m

<!-- b004646 | prose | pages [16] -->
m

<!-- b004647 | prose | pages [16] -->
m

<!-- b004648 | prose | pages [16] -->
m

<!-- b004649 | prose | pages [16] -->
m

<!-- b004650 | prose | pages [16] -->
m

<!-- b004651 | prose | pages [16] -->
m

<!-- b004652 | prose | pages [16] -->
m

<!-- b004653 | prose | pages [16] -->
m

<!-- b004654 | prose | pages [16] -->
m m

<!-- b004655 | prose | pages [16] -->
m m

<!-- b004656 | prose | pages [16] -->
m m

<!-- b004657 | prose | pages [16] -->
m m

<!-- b004658 | prose | pages [16] -->
m m

<!-- b004659 | prose | pages [16] -->
m m

<!-- b004660 | prose | pages [16] -->
m m

<!-- b004661 | prose | pages [16] -->
m m

<!-- b004662 | prose | pages [16] -->
m m

<!-- b004663 | prose | pages [16] -->
m m

<!-- b004664 | prose | pages [16] -->
m m

<!-- b004665 | prose | pages [16] -->
m m

<!-- b004666 | prose | pages [16] -->
m m

<!-- b004667 | prose | pages [16] -->
m m

<!-- b004668 | prose | pages [16] -->
m m

<!-- b004669 | prose | pages [16] -->
m m

<!-- b004670 | prose | pages [16] -->
m m

<!-- b004671 | prose | pages [16] -->
m m

<!-- b004672 | prose | pages [16] -->
m m

<!-- b004673 | prose | pages [16] -->
 Recall:The proportion of results from actual positive samples that predict positive

<!-- b004674 | prose | pages [16] -->
m

<!-- b004675 | prose | pages [16] -->
m

<!-- b004676 | prose | pages [16] -->
m

<!-- b004677 | prose | pages [16] -->
m

<!-- b004678 | prose | pages [16] -->
m

<!-- b004679 | prose | pages [16] -->
m

<!-- b004680 | prose | pages [16] -->
m

<!-- b004681 | prose | pages [16] -->
m

<!-- b004682 | prose | pages [16] -->
m

<!-- b004683 | prose | pages [16] -->
m

<!-- b004684 | prose | pages [16] -->
m

<!-- b004685 | prose | pages [16] -->
m

<!-- b004686 | prose | pages [16] -->
m

<!-- b004687 | prose | pages [16] -->
m

<!-- b004688 | prose | pages [16] -->
m

<!-- b004689 | prose | pages [16] -->
m

<!-- b004690 | prose | pages [16] -->
m

<!-- b004691 | prose | pages [16] -->
m

<!-- b004692 | prose | pages [16] -->
m

<!-- b004693 | prose | pages [16] -->
m

<!-- b004694 | prose | pages [16] -->
m

<!-- b004695 | prose | pages [16] -->
m

<!-- b004696 | prose | pages [16] -->
m

<!-- b004697 | prose | pages [16] -->
m

<!-- b004698 | prose | pages [16] -->
m

<!-- b004699 | prose | pages [16] -->
m

<!-- b004700 | prose | pages [16] -->
m

<!-- b004701 | prose | pages [16] -->
m

<!-- b004702 | prose | pages [16] -->
m

<!-- b004703 | prose | pages [16] -->
m

<!-- b004704 | prose | pages [16] -->
m

<!-- b004705 | prose | pages [16] -->
m

<!-- b004706 | prose | pages [16] -->
m

<!-- b004707 | prose | pages [16] -->
m

<!-- b004708 | prose | pages [16] -->
m

<!-- b004709 | prose | pages [16] -->
m

<!-- b004710 | prose | pages [16] -->
m

<!-- b004711 | prose | pages [16] -->
m

<!-- b004712 | prose | pages [16] -->
m

<!-- b004713 | prose | pages [16] -->
m

<!-- b004714 | prose | pages [16] -->
m

<!-- b004715 | prose | pages [16] -->
m

<!-- b004716 | prose | pages [16] -->
m

<!-- b004717 | prose | pages [16] -->
m

<!-- b004718 | prose | pages [16] -->
m

<!-- b004719 | prose | pages [16] -->
m

<!-- b004720 | prose | pages [16] -->
m

<!-- b004721 | prose | pages [16] -->
m

<!-- b004722 | prose | pages [16] -->
m

<!-- b004723 | prose | pages [16] -->
m

<!-- b004724 | prose | pages [16] -->
m

<!-- b004725 | prose | pages [16] -->
m

<!-- b004726 | prose | pages [16] -->
m

<!-- b004727 | prose | pages [16] -->
m

<!-- b004728 | prose | pages [16] -->
m

<!-- b004729 | prose | pages [16] -->
m

<!-- b004730 | prose | pages [16] -->
m

<!-- b004731 | prose | pages [16] -->
m

<!-- b004732 | prose | pages [16] -->
m

<!-- b004733 | prose | pages [16] -->
m

<!-- b004734 | prose | pages [16] -->
m

<!-- b004735 | prose | pages [16] -->
m

<!-- b004736 | prose | pages [16] -->
m

<!-- b004737 | prose | pages [16] -->
m

<!-- b004738 | prose | pages [16] -->
m

<!-- b004739 | prose | pages [16] -->
m

<!-- b004740 | prose | pages [16] -->
m

<!-- b004741 | prose | pages [16] -->
m

<!-- b004742 | prose | pages [16] -->
m

<!-- b004743 | prose | pages [16] -->
m

<!-- b004744 | prose | pages [16] -->
m

<!-- b004745 | prose | pages [16] -->
m

<!-- b004746 | prose | pages [16] -->
m

<!-- b004747 | prose | pages [16] -->
m

<!-- b004748 | prose | pages [16] -->
m

<!-- b004749 | prose | pages [16] -->
m

<!-- b004750 | prose | pages [16] -->
m

<!-- b004751 | prose | pages [16] -->
m

<!-- b004752 | prose | pages [16] -->
m

<!-- b004753 | prose | pages [16] -->
m

<!-- b004754 | prose | pages [16] -->
m

<!-- b004755 | prose | pages [16] -->
m

<!-- b004756 | prose | pages [16] -->
m

<!-- b004757 | prose | pages [16] -->
m

<!-- b004758 | prose | pages [16] -->
m

<!-- b004759 | prose | pages [16] -->
m

<!-- b004760 | prose | pages [16] -->
m

<!-- b004761 | prose | pages [16] -->
m

<!-- b004762 | prose | pages [16] -->
m

<!-- b004763 | prose | pages [16] -->
m

<!-- b004764 | prose | pages [16] -->
m

<!-- b004765 | prose | pages [16] -->
m

<!-- b004766 | prose | pages [16] -->
m

<!-- b004767 | prose | pages [16] -->
m

<!-- b004768 | prose | pages [16] -->
m

<!-- b004769 | prose | pages [16] -->
m

<!-- b004770 | prose | pages [16] -->
m

<!-- b004771 | prose | pages [16] -->
m

<!-- b004772 | prose | pages [16] -->
m

<!-- b004773 | prose | pages [16] -->
m

<!-- b004774 | prose | pages [16] -->
m

<!-- b004775 | prose | pages [16] -->
m

<!-- b004776 | prose | pages [16] -->
m

<!-- b004777 | prose | pages [16] -->
m

<!-- b004778 | prose | pages [16] -->
m

<!-- b004779 | prose | pages [16] -->
m

<!-- b004780 | prose | pages [16] -->
m

<!-- b004781 | prose | pages [16] -->
m

<!-- b004782 | prose | pages [16] -->
m

<!-- b004783 | prose | pages [16] -->
m

<!-- b004784 | prose | pages [16] -->
m

<!-- b004785 | prose | pages [16] -->
m

<!-- b004786 | prose | pages [16] -->
m

<!-- b004787 | prose | pages [16] -->
m

<!-- b004788 | prose | pages [16] -->
m

<!-- b004789 | prose | pages [16] -->
m

<!-- b004790 | prose | pages [16] -->
m

<!-- b004791 | prose | pages [16] -->
m

<!-- b004792 | prose | pages [16] -->
m

<!-- b004793 | prose | pages [16] -->
m

<!-- b004794 | prose | pages [16] -->
m

<!-- b004795 | prose | pages [16] -->
m

<!-- b004796 | prose | pages [16] -->
m

<!-- b004797 | prose | pages [16] -->
m

<!-- b004798 | prose | pages [16] -->
m

<!-- b004799 | prose | pages [16] -->
m

<!-- b004800 | prose | pages [16] -->
m

<!-- b004801 | prose | pages [16] -->
m

<!-- b004802 | prose | pages [16] -->
m

<!-- b004803 | prose | pages [16] -->
m m

<!-- b004804 | prose | pages [16] -->
m m

<!-- b004805 | prose | pages [16] -->
m m

<!-- b004806 | prose | pages [16] -->
m m

<!-- b004807 | prose | pages [16] -->
m m

<!-- b004808 | prose | pages [16] -->
m m

<!-- b004809 | prose | pages [16] -->
m m

<!-- b004810 | prose | pages [16] -->
m m

<!-- b004811 | prose | pages [16] -->
m m

<!-- b004812 | prose | pages [16] -->
m m

<!-- b004813 | prose | pages [16] -->
m m

<!-- b004814 | prose | pages [16] -->
m m

<!-- b004815 | prose | pages [16] -->
m m

<!-- b004816 | prose | pages [16] -->
m m

<!-- b004817 | prose | pages [16] -->
m m

<!-- b004818 | prose | pages [16] -->
m m

<!-- b004819 | prose | pages [16] -->
m m

<!-- b004820 | prose | pages [16] -->
m m

<!-- b004821 | prose | pages [16] -->
m m

<!-- b004822 | prose | pages [16] -->
m m

<!-- b004823 | prose | pages [16] -->
m m

<!-- b004824 | prose | pages [16] -->
m m

<!-- b004825 | prose | pages [16] -->
m m

<!-- b004826 | prose | pages [16] -->
m m

<!-- b004827 | prose | pages [16] -->
m m

<!-- b004828 | prose | pages [16] -->
samples, the greater the recall the better.

<!-- b004829 | prose | pages [16] -->
m

<!-- b004830 | prose | pages [16] -->
m

<!-- b004831 | prose | pages [16] -->
m

<!-- b004832 | prose | pages [16] -->
m

<!-- b004833 | prose | pages [16] -->
m

<!-- b004834 | prose | pages [16] -->
m

<!-- b004835 | prose | pages [16] -->
m

<!-- b004836 | prose | pages [16] -->
m

<!-- b004837 | prose | pages [16] -->
m

<!-- b004838 | prose | pages [16] -->
m

<!-- b004839 | prose | pages [16] -->
m

<!-- b004840 | prose | pages [16] -->
m

<!-- b004841 | prose | pages [16] -->
m

<!-- b004842 | prose | pages [16] -->
m

<!-- b004843 | prose | pages [16] -->
m

<!-- b004844 | prose | pages [16] -->
m

<!-- b004845 | prose | pages [16] -->
m

<!-- b004846 | prose | pages [16] -->
m

<!-- b004847 | prose | pages [16] -->
m

<!-- b004848 | prose | pages [16] -->
m

<!-- b004849 | prose | pages [16] -->
m

<!-- b004850 | prose | pages [16] -->
m

<!-- b004851 | prose | pages [16] -->
m

<!-- b004852 | prose | pages [16] -->
m

<!-- b004853 | prose | pages [16] -->
m

<!-- b004854 | prose | pages [16] -->
m

<!-- b004855 | prose | pages [16] -->
m

<!-- b004856 | prose | pages [16] -->
m

<!-- b004857 | prose | pages [16] -->
m

<!-- b004858 | prose | pages [16] -->
m

<!-- b004859 | prose | pages [16] -->
m

<!-- b004860 | prose | pages [16] -->
m

<!-- b004861 | prose | pages [16] -->
m

<!-- b004862 | prose | pages [16] -->
m

<!-- b004863 | prose | pages [16] -->
m

<!-- b004864 | prose | pages [16] -->
m

<!-- b004865 | prose | pages [16] -->
m

<!-- b004866 | prose | pages [16] -->
m

<!-- b004867 | prose | pages [16] -->
m

<!-- b004868 | prose | pages [16] -->
m

<!-- b004869 | prose | pages [16] -->
m

<!-- b004870 | prose | pages [16] -->
m

<!-- b004871 | prose | pages [16] -->
m

<!-- b004872 | prose | pages [16] -->
m

<!-- b004873 | prose | pages [16] -->
m

<!-- b004874 | prose | pages [16] -->
m

<!-- b004875 | prose | pages [16] -->
m

<!-- b004876 | prose | pages [16] -->
m

<!-- b004877 | prose | pages [16] -->
m

<!-- b004878 | prose | pages [16] -->
m

<!-- b004879 | prose | pages [16] -->
m

<!-- b004880 | prose | pages [16] -->
m

<!-- b004881 | prose | pages [16] -->
m

<!-- b004882 | prose | pages [16] -->
m

<!-- b004883 | prose | pages [16] -->
m

<!-- b004884 | prose | pages [16] -->
m

<!-- b004885 | prose | pages [16] -->
m

<!-- b004886 | prose | pages [16] -->
m

<!-- b004887 | prose | pages [16] -->
m

<!-- b004888 | prose | pages [16] -->
m

<!-- b004889 | prose | pages [16] -->
m

<!-- b004890 | prose | pages [16] -->
m

<!-- b004891 | prose | pages [16] -->
m

<!-- b004892 | prose | pages [16] -->
m

<!-- b004893 | prose | pages [16] -->
m

<!-- b004894 | prose | pages [16] -->
m

<!-- b004895 | prose | pages [16] -->
m

<!-- b004896 | prose | pages [16] -->
m

<!-- b004897 | prose | pages [16] -->
m

<!-- b004898 | prose | pages [16] -->
m

<!-- b004899 | prose | pages [16] -->
m

<!-- b004900 | prose | pages [16] -->
m

<!-- b004901 | prose | pages [16] -->
m

<!-- b004902 | prose | pages [16] -->
m

<!-- b004903 | prose | pages [16] -->
m

<!-- b004904 | prose | pages [16] -->
m

<!-- b004905 | prose | pages [16] -->
m

<!-- b004906 | prose | pages [16] -->
m

<!-- b004907 | prose | pages [16] -->
m

<!-- b004908 | prose | pages [16] -->
m

<!-- b004909 | prose | pages [16] -->
m

<!-- b004910 | prose | pages [16] -->
m

<!-- b004911 | prose | pages [16] -->
m

<!-- b004912 | prose | pages [16] -->
m

<!-- b004913 | prose | pages [16] -->
m

<!-- b004914 | prose | pages [16] -->
m

<!-- b004915 | prose | pages [16] -->
m

<!-- b004916 | prose | pages [16] -->
m

<!-- b004917 | prose | pages [16] -->
m

<!-- b004918 | prose | pages [16] -->
m

<!-- b004919 | prose | pages [16] -->
m

<!-- b004920 | prose | pages [16] -->
m

<!-- b004921 | prose | pages [16] -->
m

<!-- b004922 | prose | pages [16] -->
m

<!-- b004923 | prose | pages [16] -->
m

<!-- b004924 | prose | pages [16] -->
m

<!-- b004925 | prose | pages [16] -->
m

<!-- b004926 | prose | pages [16] -->
m

<!-- b004927 | prose | pages [16] -->
m

<!-- b004928 | prose | pages [16] -->
m

<!-- b004929 | prose | pages [16] -->
m

<!-- b004930 | prose | pages [16] -->
m

<!-- b004931 | prose | pages [16] -->
m

<!-- b004932 | prose | pages [16] -->
m

<!-- b004933 | prose | pages [16] -->
m

<!-- b004934 | prose | pages [16] -->
m

<!-- b004935 | prose | pages [16] -->
m

<!-- b004936 | prose | pages [16] -->
m

<!-- b004937 | prose | pages [16] -->
m

<!-- b004938 | prose | pages [16] -->
m

<!-- b004939 | prose | pages [16] -->
m

<!-- b004940 | prose | pages [16] -->
m

<!-- b004941 | prose | pages [16] -->
m

<!-- b004942 | prose | pages [16] -->
m

<!-- b004943 | prose | pages [16] -->
m

<!-- b004944 | prose | pages [16] -->
m

<!-- b004945 | prose | pages [16] -->
m

<!-- b004946 | prose | pages [16] -->
m

<!-- b004947 | prose | pages [16] -->
m

<!-- b004948 | prose | pages [16] -->
m

<!-- b004949 | prose | pages [16] -->
m

<!-- b004950 | prose | pages [16] -->
m

<!-- b004951 | prose | pages [16] -->
m

<!-- b004952 | prose | pages [16] -->
m

<!-- b004953 | prose | pages [16] -->
m

<!-- b004954 | prose | pages [16] -->
m

<!-- b004955 | prose | pages [16] -->
m

<!-- b004956 | prose | pages [16] -->
m

<!-- b004957 | prose | pages [16] -->
m

<!-- b004958 | prose | pages [16] -->
m

<!-- b004959 | prose | pages [16] -->
m

<!-- b004960 | prose | pages [16] -->
m

<!-- b004961 | prose | pages [16] -->
m

<!-- b004962 | prose | pages [16] -->
m

<!-- b004963 | prose | pages [16] -->
m

<!-- b004964 | prose | pages [16] -->
m

<!-- b004965 | prose | pages [16] -->
m

<!-- b004966 | prose | pages [16] -->
m

<!-- b004967 | prose | pages [16] -->
m

<!-- b004968 | prose | pages [16] -->
m

<!-- b004969 | prose | pages [16] -->
m

<!-- b004970 | prose | pages [16] -->
m

<!-- b004971 | prose | pages [16] -->
m

<!-- b004972 | prose | pages [16] -->
m

<!-- b004973 | prose | pages [16] -->
m

<!-- b004974 | prose | pages [16] -->
m

<!-- b004975 | prose | pages [16] -->
m

<!-- b004976 | prose | pages [16] -->
m

<!-- b004977 | prose | pages [16] -->
m

<!-- b004978 | prose | pages [16] -->
m m

<!-- b004979 | prose | pages [16] -->
m m

<!-- b004980 | prose | pages [16] -->
m m

<!-- b004981 | prose | pages [16] -->
m m

<!-- b004982 | prose | pages [16] -->
m m

<!-- b004983 | prose | pages [16] -->
m m

<!-- b004984 | prose | pages [16] -->
m m

<!-- b004985 | prose | pages [16] -->
m m

<!-- b004986 | prose | pages [16] -->
m m

<!-- b004987 | prose | pages [16] -->
m m

<!-- b004988 | prose | pages [16] -->
m m

<!-- b004989 | prose | pages [16] -->
m m

<!-- b004990 | prose | pages [16] -->
m m

<!-- b004991 | prose | pages [16] -->
m m

<!-- b004992 | prose | pages [16] -->
m m

<!-- b004993 | prose | pages [16] -->
m m

<!-- b004994 | prose | pages [16] -->
m m

<!-- b004995 | prose | pages [16] -->
m m

<!-- b004996 | prose | pages [16] -->
m m

<!-- b004997 | prose | pages [16] -->
m m

<!-- b004998 | prose | pages [16] -->
m m

<!-- b004999 | prose | pages [16] -->
m m

<!-- b005000 | prose | pages [16] -->
m m

<!-- b005001 | prose | pages [16] -->
m m

<!-- b005002 | prose | pages [16] -->
m m

<!-- b005003 | prose | pages [16] -->
m m

<!-- b005004 | prose | pages [16] -->
m m

<!-- b005005 | prose | pages [16] -->
m m

<!-- b005006 | prose | pages [16] -->
m m

<!-- b005007 | prose | pages [16] -->
m m

<!-- b005008 | prose | pages [16] -->
m m

<!-- b005009 | prose | pages [16] -->
m m

<!-- b005010 | prose | pages [16] -->
m m

<!-- b005011 | prose | pages [16] -->
m m

<!-- b005012 | prose | pages [16] -->
 Precision:The proportion of the results of the predicted positive sample that are

<!-- b005013 | prose | pages [16] -->
m

<!-- b005014 | prose | pages [16] -->
m

<!-- b005015 | prose | pages [16] -->
m

<!-- b005016 | prose | pages [16] -->
m

<!-- b005017 | prose | pages [16] -->
m

<!-- b005018 | prose | pages [16] -->
m

<!-- b005019 | prose | pages [16] -->
m

<!-- b005020 | prose | pages [16] -->
m

<!-- b005021 | prose | pages [16] -->
m

<!-- b005022 | prose | pages [16] -->
m

<!-- b005023 | prose | pages [16] -->
m

<!-- b005024 | prose | pages [16] -->
m

<!-- b005025 | prose | pages [16] -->
m

<!-- b005026 | prose | pages [16] -->
m

<!-- b005027 | prose | pages [16] -->
m

<!-- b005028 | prose | pages [16] -->
m

<!-- b005029 | prose | pages [16] -->
m

<!-- b005030 | prose | pages [16] -->
m

<!-- b005031 | prose | pages [16] -->
m

<!-- b005032 | prose | pages [16] -->
m

<!-- b005033 | prose | pages [16] -->
m

<!-- b005034 | prose | pages [16] -->
m

<!-- b005035 | prose | pages [16] -->
m

<!-- b005036 | prose | pages [16] -->
m

<!-- b005037 | prose | pages [16] -->
m

<!-- b005038 | prose | pages [16] -->
m

<!-- b005039 | prose | pages [16] -->
m

<!-- b005040 | prose | pages [16] -->
m

<!-- b005041 | prose | pages [16] -->
m

<!-- b005042 | prose | pages [16] -->
m

<!-- b005043 | prose | pages [16] -->
m

<!-- b005044 | prose | pages [16] -->
m

<!-- b005045 | prose | pages [16] -->
m

<!-- b005046 | prose | pages [16] -->
m

<!-- b005047 | prose | pages [16] -->
m

<!-- b005048 | prose | pages [16] -->
m

<!-- b005049 | prose | pages [16] -->
m

<!-- b005050 | prose | pages [16] -->
m

<!-- b005051 | prose | pages [16] -->
m

<!-- b005052 | prose | pages [16] -->
m

<!-- b005053 | prose | pages [16] -->
m

<!-- b005054 | prose | pages [16] -->
m

<!-- b005055 | prose | pages [16] -->
m

<!-- b005056 | prose | pages [16] -->
m

<!-- b005057 | prose | pages [16] -->
m

<!-- b005058 | prose | pages [16] -->
m

<!-- b005059 | prose | pages [16] -->
m

<!-- b005060 | prose | pages [16] -->
m

<!-- b005061 | prose | pages [16] -->
m

<!-- b005062 | prose | pages [16] -->
m

<!-- b005063 | prose | pages [16] -->
m

<!-- b005064 | prose | pages [16] -->
m

<!-- b005065 | prose | pages [16] -->
m

<!-- b005066 | prose | pages [16] -->
m

<!-- b005067 | prose | pages [16] -->
m

<!-- b005068 | prose | pages [16] -->
m

<!-- b005069 | prose | pages [16] -->
m

<!-- b005070 | prose | pages [16] -->
m

<!-- b005071 | prose | pages [16] -->
m

<!-- b005072 | prose | pages [16] -->
m

<!-- b005073 | prose | pages [16] -->
m

<!-- b005074 | prose | pages [16] -->
m

<!-- b005075 | prose | pages [16] -->
m

<!-- b005076 | prose | pages [16] -->
m

<!-- b005077 | prose | pages [16] -->
m

<!-- b005078 | prose | pages [16] -->
m

<!-- b005079 | prose | pages [16] -->
m

<!-- b005080 | prose | pages [16] -->
m

<!-- b005081 | prose | pages [16] -->
m

<!-- b005082 | prose | pages [16] -->
m

<!-- b005083 | prose | pages [16] -->
m

<!-- b005084 | prose | pages [16] -->
m

<!-- b005085 | prose | pages [16] -->
m

<!-- b005086 | prose | pages [16] -->
m

<!-- b005087 | prose | pages [16] -->
m

<!-- b005088 | prose | pages [16] -->
m

<!-- b005089 | prose | pages [16] -->
m

<!-- b005090 | prose | pages [16] -->
m

<!-- b005091 | prose | pages [16] -->
m

<!-- b005092 | prose | pages [16] -->
m

<!-- b005093 | prose | pages [16] -->
m

<!-- b005094 | prose | pages [16] -->
m

<!-- b005095 | prose | pages [16] -->
m

<!-- b005096 | prose | pages [16] -->
m

<!-- b005097 | prose | pages [16] -->
m

<!-- b005098 | prose | pages [16] -->
m

<!-- b005099 | prose | pages [16] -->
m

<!-- b005100 | prose | pages [16] -->
m

<!-- b005101 | prose | pages [16] -->
m

<!-- b005102 | prose | pages [16] -->
m

<!-- b005103 | prose | pages [16] -->
m

<!-- b005104 | prose | pages [16] -->
m

<!-- b005105 | prose | pages [16] -->
m

<!-- b005106 | prose | pages [16] -->
m

<!-- b005107 | prose | pages [16] -->
m

<!-- b005108 | prose | pages [16] -->
m

<!-- b005109 | prose | pages [16] -->
m

<!-- b005110 | prose | pages [16] -->
m

<!-- b005111 | prose | pages [16] -->
m

<!-- b005112 | prose | pages [16] -->
m

<!-- b005113 | prose | pages [16] -->
m

<!-- b005114 | prose | pages [16] -->
m

<!-- b005115 | prose | pages [16] -->
m

<!-- b005116 | prose | pages [16] -->
m

<!-- b005117 | prose | pages [16] -->
m

<!-- b005118 | prose | pages [16] -->
m

<!-- b005119 | prose | pages [16] -->
m

<!-- b005120 | prose | pages [16] -->
m

<!-- b005121 | prose | pages [16] -->
m

<!-- b005122 | prose | pages [16] -->
m

<!-- b005123 | prose | pages [16] -->
m

<!-- b005124 | prose | pages [16] -->
m

<!-- b005125 | prose | pages [16] -->
m

<!-- b005126 | prose | pages [16] -->
m

<!-- b005127 | prose | pages [16] -->
m

<!-- b005128 | prose | pages [16] -->
m m

<!-- b005129 | prose | pages [16] -->
m m

<!-- b005130 | prose | pages [16] -->
m m

<!-- b005131 | prose | pages [16] -->
m m

<!-- b005132 | prose | pages [16] -->
m m

<!-- b005133 | prose | pages [16] -->
m m

<!-- b005134 | prose | pages [16] -->
m m

<!-- b005135 | prose | pages [16] -->
m m

<!-- b005136 | prose | pages [16] -->
m m

<!-- b005137 | prose | pages [16] -->
m m

<!-- b005138 | prose | pages [16] -->
m m

<!-- b005139 | prose | pages [16] -->
m m

<!-- b005140 | prose | pages [16] -->
m m

<!-- b005141 | prose | pages [16] -->
m m

<!-- b005142 | prose | pages [16] -->
m m

<!-- b005143 | prose | pages [16] -->
m m

<!-- b005144 | prose | pages [16] -->
m m

<!-- b005145 | prose | pages [16] -->
m m

<!-- b005146 | prose | pages [16] -->
m m

<!-- b005147 | prose | pages [16] -->
m m

<!-- b005148 | prose | pages [16] -->
m m

<!-- b005149 | prose | pages [16] -->
m m

<!-- b005150 | prose | pages [16] -->
m m m m

<!-- b005151 | prose | pages [16] -->
actually positive, the greater the precision the better.

<!-- b005152 | prose | pages [16] -->
m

<!-- b005153 | prose | pages [16] -->
m

<!-- b005154 | prose | pages [16] -->
m

<!-- b005155 | prose | pages [16] -->
m

<!-- b005156 | prose | pages [16] -->
m

<!-- b005157 | prose | pages [16] -->
m

<!-- b005158 | prose | pages [16] -->
m

<!-- b005159 | prose | pages [16] -->
m

<!-- b005160 | prose | pages [16] -->
m

<!-- b005161 | prose | pages [16] -->
m

<!-- b005162 | prose | pages [16] -->
m

<!-- b005163 | prose | pages [16] -->
m

<!-- b005164 | prose | pages [16] -->
m

<!-- b005165 | prose | pages [16] -->
m

<!-- b005166 | prose | pages [16] -->
m

<!-- b005167 | prose | pages [16] -->
m

<!-- b005168 | prose | pages [16] -->
m

<!-- b005169 | prose | pages [16] -->
m

<!-- b005170 | prose | pages [16] -->
m

<!-- b005171 | prose | pages [16] -->
m

<!-- b005172 | prose | pages [16] -->
m

<!-- b005173 | prose | pages [16] -->
m

<!-- b005174 | prose | pages [16] -->
m

<!-- b005175 | prose | pages [16] -->
m

<!-- b005176 | prose | pages [16] -->
m

<!-- b005177 | prose | pages [16] -->
m

<!-- b005178 | prose | pages [16] -->
m

<!-- b005179 | prose | pages [16] -->
m

<!-- b005180 | prose | pages [16] -->
m

<!-- b005181 | prose | pages [16] -->
m

<!-- b005182 | prose | pages [16] -->
m

<!-- b005183 | prose | pages [16] -->
m

<!-- b005184 | prose | pages [16] -->
m

<!-- b005185 | prose | pages [16] -->
m

<!-- b005186 | prose | pages [16] -->
m

<!-- b005187 | prose | pages [16] -->
m

<!-- b005188 | prose | pages [16] -->
m

<!-- b005189 | prose | pages [16] -->
m

<!-- b005190 | prose | pages [16] -->
m

<!-- b005191 | prose | pages [16] -->
m

<!-- b005192 | prose | pages [16] -->
m

<!-- b005193 | prose | pages [16] -->
m

<!-- b005194 | prose | pages [16] -->
m

<!-- b005195 | prose | pages [16] -->
m

<!-- b005196 | prose | pages [16] -->
m

<!-- b005197 | prose | pages [16] -->
m

<!-- b005198 | prose | pages [16] -->
m

<!-- b005199 | prose | pages [16] -->
m

<!-- b005200 | prose | pages [16] -->
m

<!-- b005201 | prose | pages [16] -->
m

<!-- b005202 | prose | pages [16] -->
m

<!-- b005203 | prose | pages [16] -->
m

<!-- b005204 | prose | pages [16] -->
m

<!-- b005205 | prose | pages [16] -->
m

<!-- b005206 | prose | pages [16] -->
m

<!-- b005207 | prose | pages [16] -->
m

<!-- b005208 | prose | pages [16] -->
m

<!-- b005209 | prose | pages [16] -->
m

<!-- b005210 | prose | pages [16] -->
m

<!-- b005211 | prose | pages [16] -->
m

<!-- b005212 | prose | pages [16] -->
m

<!-- b005213 | prose | pages [16] -->
m

<!-- b005214 | prose | pages [16] -->
m

<!-- b005215 | prose | pages [16] -->
m

<!-- b005216 | prose | pages [16] -->
m

<!-- b005217 | prose | pages [16] -->
m

<!-- b005218 | prose | pages [16] -->
m

<!-- b005219 | prose | pages [16] -->
m

<!-- b005220 | prose | pages [16] -->
m

<!-- b005221 | prose | pages [16] -->
m

<!-- b005222 | prose | pages [16] -->
m

<!-- b005223 | prose | pages [16] -->
m

<!-- b005224 | prose | pages [16] -->
m

<!-- b005225 | prose | pages [16] -->
m

<!-- b005226 | prose | pages [16] -->
m

<!-- b005227 | prose | pages [16] -->
m

<!-- b005228 | prose | pages [16] -->
m

<!-- b005229 | prose | pages [16] -->
m

<!-- b005230 | prose | pages [16] -->
m

<!-- b005231 | prose | pages [16] -->
m

<!-- b005232 | prose | pages [16] -->
m

<!-- b005233 | prose | pages [16] -->
m

<!-- b005234 | prose | pages [16] -->
m

<!-- b005235 | prose | pages [16] -->
m

<!-- b005236 | prose | pages [16] -->
m m

<!-- b005237 | prose | pages [16] -->
m m

<!-- b005238 | prose | pages [16] -->
m m

<!-- b005239 | prose | pages [16] -->
m m

<!-- b005240 | prose | pages [16] -->
m m

<!-- b005241 | prose | pages [16] -->
m m

<!-- b005242 | prose | pages [16] -->
m m

<!-- b005243 | prose | pages [16] -->
m m

<!-- b005244 | prose | pages [16] -->
m m

<!-- b005245 | prose | pages [16] -->
m m

<!-- b005246 | prose | pages [16] -->
m m

<!-- b005247 | prose | pages [16] -->
m m m m

<!-- b005248 | prose | pages [16] -->
m m

<!-- b005249 | prose | pages [16] -->
m m

<!-- b005250 | prose | pages [16] -->
m m

<!-- b005251 | prose | pages [16] -->
m m

<!-- b005252 | prose | pages [16] -->
m m

<!-- b005253 | prose | pages [16] -->
m m

<!-- b005254 | prose | pages [16] -->
 F1:A reconciled average of precision and recall, where precision and recall are

<!-- b005255 | prose | pages [16] -->
mutually influential.

<!-- b005256 | prose | pages [16] -->
The above table shows that Accuracy, Recall and Precision are all larger and F1 is also larger, which indicates that this classification model ensures higher accuracy while recall is also high, and the classification effect of this classification model is better.

<!-- b005257 | heading | pages [16] -->
6.2.2 The Classification Results are Given

<!-- b005258 | prose | pages [16] -->
We need to solve for the probability p that the dependent variable is 1:

<!-- b005259 | prose | pages [16] -->
1

<!-- b005260 | prose | pages [16] -->


<!-- b005261 | prose | pages [16] -->
p

<!-- b005262 | furniture | pages [16] -->


<!-- b005263 | prose | pages [16] -->
 

<!-- b005264 | prose | pages [16] -->
z

<!-- b005265 | prose | pages [16] -->
0.012

<!-- b005266 | prose | pages [16] -->
a

<!-- b005267 | prose | pages [16] -->
k

<!-- b005268 | prose | pages [16] -->


<!-- b005269 | prose | pages [16] -->
z

<!-- b005270 | furniture | pages [16] -->


<!-- b005271 | prose | pages [16] -->
(12)

<!-- b005272 | prose | pages [16] -->
1 1

<!-- b005273 | prose | pages [16] -->
e

<!-- b005274 | prose | pages [16] -->


<!-- b005275 | prose | pages [16] -->
0.068

<!-- b005276 | prose | pages [16] -->
e

<!-- b005277 | prose | pages [16] -->
2.425

<!-- b005278 | prose | pages [16] -->
k

<!-- b005279 | prose | pages [16] -->
After calculating the results, we took only the countries with a probability of winning the prize greater than 0.2 as shown in the table below

<!-- b005280 | caption | pages [16] -->
Table 11 Countries and Probability of Winning Medals

<!-- b005281 | prose | pages [16] -->
PLE LBN GUM ANG ESA 0.220 0.290 0.230 0.206 0.201

<!-- b005282 | prose | pages [16] -->
The resulting visualization is shown below:

<!-- b005283 | furniture | pages [16] -->


<!-- b005284 | caption | pages [16] -->
Figure 14 Countries and Probability of Winning Medals

<!-- b005285 | prose | pages [16] -->
We found that these non-winning countries are mainly concentrated in the Middle East, the eastern and southern regions of Asia, sub-Saharan Africa, and some island regions. Some of these countries have suffered from wars due to political issues, while others do not have access to professional training grounds due to natural constraints. Some are economically backward and cannot afford to develop sports. However, they still have a chance to win medals in the 2028 Summer Olympics, and we look forward to their wonderful performance.

<!-- b005286 | furniture | pages [16] -->


<!-- b005287 | prose | pages [16] -->
关注数学模型

<!-- b005288 | furniture | pages [16] -->
2

<!-- b005289 | furniture | pages [16] -->
MATHmodels

<!-- b005290 | furniture | pages [16] -->
获取更多资讯

<!-- b005291 | furniture | pages [17] -->
Team#2507817                                                             Page 17 of 25

<!-- b005292 | heading | pages [17] -->
7 Task 3 Relationship Between Sports and Medals

<!-- b005293 | prose | pages [17] -->
The question requires us to count the number of medals won by each country in each event based on the GSRF prediction model that we have built. Solve for the relationship between the sports and the number of medals won by each country. Identify the sports that are most important to each country and explore why. Host countries usually add events in sports that their country specializes in, and explore the effect of this on the medals won by other countries.

<!-- b005294 | heading | pages [17] -->
7.1 Relationship of the Sports to gold medals & total medals

<!-- b005295 | prose | pages [17] -->
Based on the previously drawn radar Figure 6 , we found that programs have a non- negligible impact on the number of medals. We have selected the countries that have done well in the Olympics, counted the number of medals won, and selected the events in which they have won more medals as shown below:

<!-- b005296 | prose | pages [17] -->
微信公众号：数学模型

<!-- b005297 | caption | pages [17] -->
Table 12 Some Countries and Sports They are Good at

<!-- b005298 | prose | pages [17] -->
NOC Sport Medals

<!-- b005299 | prose | pages [17] -->
Swimming 1206

<!-- b005300 | prose | pages [17] -->
Athletics 1190

<!-- b005301 | prose | pages [17] -->
USA

<!-- b005302 | prose | pages [17] -->
Rowing 388 Basketball 341

<!-- b005303 | prose | pages [17] -->
Gymnastics 166

<!-- b005304 | prose | pages [17] -->
Swimming 127

<!-- b005305 | prose | pages [17] -->
JPN

<!-- b005306 | prose | pages [17] -->
Judo 102 Volleyball 101

<!-- b005307 | prose | pages [17] -->
NOC Sport Medals

<!-- b005308 | prose | pages [17] -->
Swimming 120 Diving 119

<!-- b005309 | prose | pages [17] -->
CHN

<!-- b005310 | prose | pages [17] -->
Gymnastics 109 Table Tennis 94

<!-- b005311 | prose | pages [17] -->
Swimming 505 Hockey 188

<!-- b005312 | prose | pages [17] -->
AUS

<!-- b005313 | prose | pages [17] -->
Rowing 162 Athletics 100

<!-- b005314 | prose | pages [17] -->
微信号：MATHmodels

<!-- b005315 | prose | pages [17] -->
Handball 96 KOR Archery 90 Athletics 393 GBR Rowing 319

<!-- b005316 | prose | pages [17] -->
As can be seen from the table, these countries will win more medals in the events they specialize in

<!-- b005317 | heading | pages [17] -->
7.2 The most Important Sports for the Country

<!-- b005318 | prose | pages [17] -->
To assess the importance of the project for the country, we introduce the project importance I(j):

<!-- b005319 | furniture | pages [17] -->


<!-- b005320 | prose | pages [17] -->
I

<!-- b005321 | prose | pages [17] -->
j

<!-- b005322 | prose | pages [17] -->
Among them:

<!-- b005323 | prose | pages [17] -->
m  

<!-- b005324 | prose | pages [17] -->
k

<!-- b005325 | furniture | pages [17] -->


<!-- b005326 | prose | pages [17] -->
(13) M

<!-- b005327 | prose | pages [17] -->
k

<!-- b005328 | prose | pages [17] -->
mk stands for the number of medals won by the country in this event; Mk stands for the total number of medals won by the country

<!-- b005329 | prose | pages [17] -->
For countries with strong comprehensive sports strength, they will achieve medals in many sports, and their program importance is not a single value, we take the United States and China as an example, calculate the importance of each program to them, and plot the radial histogram as shown below:

<!-- b005330 | furniture | pages [17] -->


<!-- b005331 | furniture | pages [18] -->
Team#2507817                                                             Page 18 of 25

<!-- b005332 | prose | pages [18] -->
a) USA

<!-- b005333 | furniture | pages [18] -->


<!-- b005334 | furniture | pages [18] -->


<!-- b005335 | furniture | pages [18] -->


<!-- b005336 | furniture | pages [18] -->


<!-- b005337 | furniture | pages [18] -->


<!-- b005338 | furniture | pages [18] -->


<!-- b005339 | furniture | pages [18] -->


<!-- b005340 | furniture | pages [18] -->


<!-- b005341 | prose | pages [18] -->
b) CHN

<!-- b005342 | caption | pages [18] -->
Figure 15 Radial Histogram of Sport Importance

<!-- b005343 | prose | pages [18] -->
From the figure we can easily see that the most important sport for both the United States and China is swimming. According to the related literature, it can be seen that China's performance in diving is better than that of swimming[2] , but the importance of swimming is higher than that of diving, which is because swimming has a lot of events, which greatly increases the probability of winning medals. This also aptly reflects the effect of the number of events on the results.

<!-- b005344 | prose | pages [18] -->
For countries that are weak in sports, they may have won medals in only one sport, which is the most important for that country when the importance of that sport is 1 and the importance of the rest of the sports is 0. The countries in this category and their corresponding sports in our statistics office are shown in the following chart.

<!-- b005345 | furniture | pages [18] -->


<!-- b005346 | caption | pages [18] -->
Figure 16 Countries that won medals in only one sport

<!-- b005347 | prose | pages [18] -->
The graph above shows that Athletics is the most important sport for many countries, this is because Athletics has a lot of events, which provides more chances to win prizes for countries that are weaker in sports. These countries are mostly African countries, which have an advantage in Athletics.

<!-- b005348 | heading | pages [18] -->
7.3 Impact of Nationally Selected Sports on results

<!-- b005349 | prose | pages [18] -->
Preparation for the Olympic Games is a long and continuous process of fluctuation and adjustment, and the country will adjust its preparation program based on the combined results of previous Olympic Games and different international events.

<!-- b005350 | prose | pages [18] -->
The country will invest more time and energy in the development of this sport for those who already have an advantage, and more people will participate in this sport, providing more excellent human resources to promote the development of this sport, so as to achieve better

<!-- b005351 | furniture | pages [18] -->


<!-- b005352 | prose | pages [18] -->
关注数学模型

<!-- b005353 | furniture | pages [18] -->
2

<!-- b005354 | furniture | pages [18] -->
MATHmodels

<!-- b005355 | furniture | pages [18] -->
获取更多资讯

<!-- b005356 | furniture | pages [19] -->
Team#2507817                                                             Page 19 of 25

<!-- b005357 | prose | pages [19] -->
results in the Olympic Games.

<!-- b005358 | prose | pages [19] -->
For programs with high potential, which have had mediocre results in the past, the country will increase funding and adopt a strategy appropriate to the program, thus improving Olympic performance.

<!-- b005359 | prose | pages [19] -->
In the case of projects that have never won an award, they are usually not prevalent in the country, or the people of the country are generally not good at them. The country does not invest much time and money in such programs.

<!-- b005360 | heading | pages [19] -->
8 Task 4 The Impact of Great Coach

<!-- b005361 | prose | pages [19] -->
微信公众号：数学模型

<!-- b005362 | prose | pages [19] -->
The question asks us to search for fluctuations in performance due to the hiring of "great coaches" in previous years, to estimate the effect of this effect on the number of medals, and to identify the countries that need to hire great coaches the most. We need to build a regression model to measure the impact of this effect.

<!-- b005363 | heading | pages [19] -->
8.1 Lasso Regression Model

<!-- b005364 | heading | pages [19] -->
8.1.1 Model Preparation

<!-- b005365 | prose | pages [19] -->
In order to further quantify the country's performance at each Olympic Games, we have chosen to assign points to the different medals, with the following rules for assigning points:

<!-- b005366 | prose | pages [19] -->
微信号：MATHmodels

<!-- b005367 | caption | pages [19] -->
Table 13 Score table

<!-- b005368 | prose | pages [19] -->
Gold Medal Silver Medal 10 6 Bronze Medal No Medal 3 0

<!-- b005369 | prose | pages [19] -->
We checked the famous and great coaches of history and found out that women's gymnastics coach Bela Karolyi coached many Olympic champions[3] . He coached in Romania in the 1976 and 1980 Olympics, and in the USA in the Olympics from 1984~2016[4] . We counted the scores of Romania and USA in women's gymnastics in every Olympics between 1952 and 2024, as shown below:

<!-- b005370 | furniture | pages [19] -->


<!-- b005371 | caption | pages [19] -->
Figure 17 ROU vs USA Women's Gymnastics Scores

<!-- b005372 | prose | pages [19] -->
We found a significant improvement in the country's women's gymnastics scores after this coach began coaching. When he left ROU, ROU's scores improved slightly, but generally trended slowly downward. When he came to USA, USA's gymnastics scores still fluctuated significantly, but had an overall upward trend. The Spearman correlation coefficient was then analyzed with the following formula:

<!-- b005373 | prose | pages [19] -->
m

<!-- b005374 | prose | pages [19] -->
m

<!-- b005375 | prose | pages [19] -->
m

<!-- b005376 | prose | pages [19] -->
m

<!-- b005377 | prose | pages [19] -->
m

<!-- b005378 | prose | pages [19] -->
m

<!-- b005379 | prose | pages [19] -->
m

<!-- b005380 | prose | pages [19] -->
m

<!-- b005381 | prose | pages [19] -->
m

<!-- b005382 | prose | pages [19] -->
m

<!-- b005383 | prose | pages [19] -->
m

<!-- b005384 | prose | pages [19] -->
m

<!-- b005385 | prose | pages [19] -->
m

<!-- b005386 | prose | pages [19] -->
m

<!-- b005387 | prose | pages [19] -->
m

<!-- b005388 | prose | pages [19] -->
m

<!-- b005389 | prose | pages [19] -->
m

<!-- b005390 | prose | pages [19] -->
m

<!-- b005391 | prose | pages [19] -->
m

<!-- b005392 | prose | pages [19] -->
m

<!-- b005393 | prose | pages [19] -->
m

<!-- b005394 | prose | pages [19] -->
m

<!-- b005395 | prose | pages [19] -->
m

<!-- b005396 | prose | pages [19] -->
m

<!-- b005397 | prose | pages [19] -->
m

<!-- b005398 | prose | pages [19] -->
m

<!-- b005399 | prose | pages [19] -->
m

<!-- b005400 | prose | pages [19] -->
m

<!-- b005401 | prose | pages [19] -->
m

<!-- b005402 | prose | pages [19] -->
m

<!-- b005403 | prose | pages [19] -->
m

<!-- b005404 | prose | pages [19] -->
m

<!-- b005405 | prose | pages [19] -->
m

<!-- b005406 | prose | pages [19] -->
m

<!-- b005407 | prose | pages [19] -->
m

<!-- b005408 | prose | pages [19] -->
m

<!-- b005409 | prose | pages [19] -->
m

<!-- b005410 | prose | pages [19] -->
m

<!-- b005411 | prose | pages [19] -->
m

<!-- b005412 | prose | pages [19] -->
m

<!-- b005413 | prose | pages [19] -->
m

<!-- b005414 | prose | pages [19] -->
m

<!-- b005415 | prose | pages [19] -->
m

<!-- b005416 | prose | pages [19] -->
m

<!-- b005417 | prose | pages [19] -->
m

<!-- b005418 | prose | pages [19] -->
m

<!-- b005419 | prose | pages [19] -->
m

<!-- b005420 | prose | pages [19] -->
m

<!-- b005421 | prose | pages [19] -->
m

<!-- b005422 | prose | pages [19] -->
m

<!-- b005423 | prose | pages [19] -->
m

<!-- b005424 | prose | pages [19] -->
m

<!-- b005425 | prose | pages [19] -->
m

<!-- b005426 | prose | pages [19] -->
m

<!-- b005427 | prose | pages [19] -->
m

<!-- b005428 | prose | pages [19] -->
m

<!-- b005429 | prose | pages [19] -->
m

<!-- b005430 | prose | pages [19] -->
m

<!-- b005431 | prose | pages [19] -->
m

<!-- b005432 | prose | pages [19] -->
m

<!-- b005433 | prose | pages [19] -->
m

<!-- b005434 | prose | pages [19] -->
m

<!-- b005435 | prose | pages [19] -->
m

<!-- b005436 | prose | pages [19] -->
m

<!-- b005437 | prose | pages [19] -->
m

<!-- b005438 | prose | pages [19] -->
m

<!-- b005439 | prose | pages [19] -->
m

<!-- b005440 | prose | pages [19] -->
m

<!-- b005441 | prose | pages [19] -->
m

<!-- b005442 | prose | pages [19] -->
m

<!-- b005443 | prose | pages [19] -->
m

<!-- b005444 | prose | pages [19] -->
m

<!-- b005445 | prose | pages [19] -->
m

<!-- b005446 | prose | pages [19] -->
m

<!-- b005447 | prose | pages [19] -->
m

<!-- b005448 | prose | pages [19] -->
m

<!-- b005449 | prose | pages [19] -->
m

<!-- b005450 | prose | pages [19] -->
m

<!-- b005451 | prose | pages [19] -->
m

<!-- b005452 | prose | pages [19] -->
m

<!-- b005453 | prose | pages [19] -->
m

<!-- b005454 | prose | pages [19] -->
m

<!-- b005455 | prose | pages [19] -->
m

<!-- b005456 | prose | pages [19] -->
m

<!-- b005457 | prose | pages [19] -->
m

<!-- b005458 | prose | pages [19] -->
m

<!-- b005459 | prose | pages [19] -->
m

<!-- b005460 | prose | pages [19] -->
m

<!-- b005461 | prose | pages [19] -->
m

<!-- b005462 | prose | pages [19] -->
m

<!-- b005463 | prose | pages [19] -->
m

<!-- b005464 | prose | pages [19] -->
m

<!-- b005465 | prose | pages [19] -->
m

<!-- b005466 | prose | pages [19] -->
m

<!-- b005467 | prose | pages [19] -->
m

<!-- b005468 | prose | pages [19] -->
m

<!-- b005469 | prose | pages [19] -->
m

<!-- b005470 | prose | pages [19] -->
m

<!-- b005471 | prose | pages [19] -->
m

<!-- b005472 | prose | pages [19] -->
m

<!-- b005473 | prose | pages [19] -->
m

<!-- b005474 | prose | pages [19] -->
m

<!-- b005475 | prose | pages [19] -->
m

<!-- b005476 | prose | pages [19] -->
m

<!-- b005477 | prose | pages [19] -->
m

<!-- b005478 | prose | pages [19] -->
m

<!-- b005479 | prose | pages [19] -->
m

<!-- b005480 | prose | pages [19] -->
m

<!-- b005481 | prose | pages [19] -->
m

<!-- b005482 | prose | pages [19] -->
m

<!-- b005483 | prose | pages [19] -->
m

<!-- b005484 | prose | pages [19] -->
m

<!-- b005485 | prose | pages [19] -->
m

<!-- b005486 | prose | pages [19] -->
m

<!-- b005487 | prose | pages [19] -->
m

<!-- b005488 | prose | pages [19] -->
m

<!-- b005489 | prose | pages [19] -->
m

<!-- b005490 | prose | pages [19] -->
m

<!-- b005491 | prose | pages [19] -->
m

<!-- b005492 | prose | pages [19] -->
m

<!-- b005493 | prose | pages [19] -->
m

<!-- b005494 | prose | pages [19] -->
m

<!-- b005495 | prose | pages [19] -->
m

<!-- b005496 | prose | pages [19] -->
m

<!-- b005497 | prose | pages [19] -->
m

<!-- b005498 | prose | pages [19] -->
m

<!-- b005499 | prose | pages [19] -->
m

<!-- b005500 | prose | pages [19] -->
m

<!-- b005501 | prose | pages [19] -->
m

<!-- b005502 | prose | pages [19] -->
m

<!-- b005503 | furniture | pages [19] -->


<!-- b005504 | prose | pages [19] -->
m

<!-- b005505 | prose | pages [19] -->
m

<!-- b005506 | prose | pages [19] -->
m

<!-- b005507 | prose | pages [19] -->
m

<!-- b005508 | prose | pages [19] -->
m

<!-- b005509 | prose | pages [19] -->
m

<!-- b005510 | prose | pages [19] -->
m

<!-- b005511 | prose | pages [19] -->
m

<!-- b005512 | prose | pages [19] -->
m

<!-- b005513 | prose | pages [19] -->
m

<!-- b005514 | prose | pages [19] -->
m

<!-- b005515 | prose | pages [19] -->
m

<!-- b005516 | prose | pages [19] -->
m

<!-- b005517 | prose | pages [19] -->
m

<!-- b005518 | prose | pages [19] -->
m

<!-- b005519 | prose | pages [19] -->
m

<!-- b005520 | prose | pages [19] -->
m

<!-- b005521 | prose | pages [19] -->
m

<!-- b005522 | prose | pages [19] -->
m

<!-- b005523 | prose | pages [19] -->
m

<!-- b005524 | prose | pages [19] -->
m

<!-- b005525 | prose | pages [19] -->
m

<!-- b005526 | prose | pages [19] -->
m

<!-- b005527 | prose | pages [19] -->
m

<!-- b005528 | prose | pages [19] -->
m

<!-- b005529 | prose | pages [19] -->
m

<!-- b005530 | prose | pages [19] -->
m

<!-- b005531 | prose | pages [19] -->
m

<!-- b005532 | prose | pages [19] -->
m

<!-- b005533 | prose | pages [19] -->
m

<!-- b005534 | prose | pages [19] -->
m

<!-- b005535 | prose | pages [19] -->
m

<!-- b005536 | prose | pages [19] -->
m

<!-- b005537 | prose | pages [19] -->
m

<!-- b005538 | prose | pages [19] -->
m

<!-- b005539 | prose | pages [19] -->
m

<!-- b005540 | prose | pages [19] -->
m

<!-- b005541 | prose | pages [19] -->
m

<!-- b005542 | prose | pages [19] -->
m

<!-- b005543 | prose | pages [19] -->
m

<!-- b005544 | prose | pages [19] -->
m

<!-- b005545 | prose | pages [19] -->
m

<!-- b005546 | prose | pages [19] -->
m

<!-- b005547 | prose | pages [19] -->
m

<!-- b005548 | prose | pages [19] -->
m

<!-- b005549 | prose | pages [19] -->
m

<!-- b005550 | prose | pages [19] -->
m

<!-- b005551 | prose | pages [19] -->
m

<!-- b005552 | prose | pages [19] -->
m

<!-- b005553 | prose | pages [19] -->
m

<!-- b005554 | prose | pages [19] -->
m

<!-- b005555 | prose | pages [19] -->
m

<!-- b005556 | prose | pages [19] -->
m

<!-- b005557 | prose | pages [19] -->
m

<!-- b005558 | prose | pages [19] -->
m

<!-- b005559 | prose | pages [19] -->
m

<!-- b005560 | prose | pages [19] -->
m

<!-- b005561 | prose | pages [19] -->
m

<!-- b005562 | prose | pages [19] -->
m

<!-- b005563 | prose | pages [19] -->
m

<!-- b005564 | prose | pages [19] -->
m

<!-- b005565 | prose | pages [19] -->
m

<!-- b005566 | prose | pages [19] -->
m

<!-- b005567 | prose | pages [19] -->
m

<!-- b005568 | prose | pages [19] -->
m

<!-- b005569 | prose | pages [19] -->
m

<!-- b005570 | prose | pages [19] -->
m

<!-- b005571 | prose | pages [19] -->
m

<!-- b005572 | prose | pages [19] -->
m

<!-- b005573 | prose | pages [19] -->
m

<!-- b005574 | prose | pages [19] -->
m

<!-- b005575 | prose | pages [19] -->
m

<!-- b005576 | prose | pages [19] -->
m

<!-- b005577 | prose | pages [19] -->
m

<!-- b005578 | prose | pages [19] -->
m

<!-- b005579 | prose | pages [19] -->
m

<!-- b005580 | prose | pages [19] -->
m

<!-- b005581 | prose | pages [19] -->
m

<!-- b005582 | prose | pages [19] -->
m

<!-- b005583 | prose | pages [19] -->
m

<!-- b005584 | prose | pages [19] -->
m

<!-- b005585 | prose | pages [19] -->
m

<!-- b005586 | prose | pages [19] -->
m

<!-- b005587 | prose | pages [19] -->
m

<!-- b005588 | prose | pages [19] -->
m

<!-- b005589 | prose | pages [19] -->
m

<!-- b005590 | prose | pages [19] -->
m

<!-- b005591 | prose | pages [19] -->
m

<!-- b005592 | prose | pages [19] -->
m

<!-- b005593 | prose | pages [19] -->
m

<!-- b005594 | prose | pages [19] -->
m

<!-- b005595 | prose | pages [19] -->
m

<!-- b005596 | prose | pages [19] -->
m

<!-- b005597 | prose | pages [19] -->
m

<!-- b005598 | prose | pages [19] -->
m

<!-- b005599 | prose | pages [19] -->
m

<!-- b005600 | prose | pages [19] -->
m

<!-- b005601 | prose | pages [19] -->
m

<!-- b005602 | prose | pages [19] -->
m

<!-- b005603 | prose | pages [19] -->
m

<!-- b005604 | prose | pages [19] -->
m

<!-- b005605 | prose | pages [19] -->
m

<!-- b005606 | prose | pages [19] -->
m

<!-- b005607 | prose | pages [19] -->
m

<!-- b005608 | prose | pages [19] -->
m

<!-- b005609 | prose | pages [19] -->
m

<!-- b005610 | prose | pages [19] -->
m

<!-- b005611 | prose | pages [19] -->
m

<!-- b005612 | prose | pages [19] -->
m

<!-- b005613 | prose | pages [19] -->
m

<!-- b005614 | prose | pages [19] -->
m

<!-- b005615 | prose | pages [19] -->
m

<!-- b005616 | prose | pages [19] -->
m

<!-- b005617 | prose | pages [19] -->
m

<!-- b005618 | prose | pages [19] -->
m

<!-- b005619 | prose | pages [19] -->
m

<!-- b005620 | prose | pages [19] -->
m

<!-- b005621 | prose | pages [19] -->
m

<!-- b005622 | prose | pages [19] -->
m

<!-- b005623 | prose | pages [19] -->
m

<!-- b005624 | prose | pages [19] -->
m

<!-- b005625 | prose | pages [19] -->
m

<!-- b005626 | prose | pages [19] -->
m

<!-- b005627 | prose | pages [19] -->
m

<!-- b005628 | prose | pages [19] -->
m

<!-- b005629 | prose | pages [19] -->
m

<!-- b005630 | prose | pages [19] -->
m

<!-- b005631 | prose | pages [19] -->
m

<!-- b005632 | prose | pages [19] -->
m

<!-- b005633 | prose | pages [19] -->
m

<!-- b005634 | prose | pages [19] -->
m

<!-- b005635 | prose | pages [19] -->
m

<!-- b005636 | prose | pages [19] -->
m

<!-- b005637 | prose | pages [19] -->
m

<!-- b005638 | prose | pages [19] -->
m

<!-- b005639 | prose | pages [19] -->
m

<!-- b005640 | prose | pages [19] -->
m

<!-- b005641 | prose | pages [19] -->
m

<!-- b005642 | prose | pages [19] -->
m

<!-- b005643 | prose | pages [19] -->
m

<!-- b005644 | prose | pages [19] -->
m

<!-- b005645 | prose | pages [19] -->
m

<!-- b005646 | prose | pages [19] -->
m

<!-- b005647 | prose | pages [19] -->
m

<!-- b005648 | prose | pages [19] -->
m

<!-- b005649 | prose | pages [19] -->
m

<!-- b005650 | prose | pages [19] -->
m

<!-- b005651 | prose | pages [19] -->
m

<!-- b005652 | prose | pages [19] -->
m

<!-- b005653 | prose | pages [19] -->
m

<!-- b005654 | prose | pages [19] -->
m

<!-- b005655 | prose | pages [19] -->
m

<!-- b005656 | prose | pages [19] -->
m

<!-- b005657 | prose | pages [19] -->
m

<!-- b005658 | furniture | pages [19] -->
m

<!-- b005659 | furniture | pages [19] -->
m

<!-- b005660 | furniture | pages [19] -->
m

<!-- b005661 | furniture | pages [19] -->
m

<!-- b005662 | furniture | pages [19] -->
m

<!-- b005663 | furniture | pages [19] -->
m

<!-- b005664 | furniture | pages [19] -->
m

<!-- b005665 | furniture | pages [19] -->
m

<!-- b005666 | furniture | pages [19] -->
m

<!-- b005667 | furniture | pages [19] -->
m

<!-- b005668 | furniture | pages [19] -->
m

<!-- b005669 | furniture | pages [19] -->
m

<!-- b005670 | furniture | pages [19] -->
m

<!-- b005671 | furniture | pages [19] -->
m

<!-- b005672 | furniture | pages [19] -->
m

<!-- b005673 | furniture | pages [19] -->
m

<!-- b005674 | furniture | pages [19] -->
m

<!-- b005675 | furniture | pages [19] -->
m

<!-- b005676 | furniture | pages [19] -->
m

<!-- b005677 | furniture | pages [19] -->
m

<!-- b005678 | furniture | pages [19] -->
m

<!-- b005679 | furniture | pages [19] -->
m

<!-- b005680 | furniture | pages [19] -->
m

<!-- b005681 | furniture | pages [19] -->
m

<!-- b005682 | furniture | pages [19] -->
m

<!-- b005683 | furniture | pages [19] -->
m

<!-- b005684 | furniture | pages [19] -->
m

<!-- b005685 | furniture | pages [19] -->
m

<!-- b005686 | furniture | pages [19] -->
m

<!-- b005687 | furniture | pages [19] -->
m

<!-- b005688 | furniture | pages [19] -->
m

<!-- b005689 | furniture | pages [19] -->
m

<!-- b005690 | furniture | pages [19] -->
m

<!-- b005691 | furniture | pages [19] -->
m

<!-- b005692 | furniture | pages [19] -->
m

<!-- b005693 | furniture | pages [19] -->
m

<!-- b005694 | furniture | pages [19] -->
m

<!-- b005695 | furniture | pages [19] -->
m

<!-- b005696 | furniture | pages [19] -->
m

<!-- b005697 | furniture | pages [19] -->
m

<!-- b005698 | furniture | pages [19] -->
m

<!-- b005699 | furniture | pages [19] -->
m

<!-- b005700 | furniture | pages [19] -->
m

<!-- b005701 | furniture | pages [19] -->
m

<!-- b005702 | furniture | pages [19] -->
m

<!-- b005703 | furniture | pages [19] -->
m

<!-- b005704 | furniture | pages [19] -->
m

<!-- b005705 | furniture | pages [19] -->
m

<!-- b005706 | furniture | pages [19] -->
m

<!-- b005707 | furniture | pages [19] -->
m

<!-- b005708 | furniture | pages [19] -->
m

<!-- b005709 | furniture | pages [19] -->
m

<!-- b005710 | furniture | pages [19] -->
m

<!-- b005711 | furniture | pages [19] -->
m

<!-- b005712 | furniture | pages [19] -->
m

<!-- b005713 | furniture | pages [19] -->
m

<!-- b005714 | furniture | pages [19] -->
m

<!-- b005715 | furniture | pages [19] -->
m

<!-- b005716 | furniture | pages [19] -->
m

<!-- b005717 | furniture | pages [19] -->
m

<!-- b005718 | furniture | pages [19] -->
m

<!-- b005719 | furniture | pages [19] -->
m

<!-- b005720 | furniture | pages [19] -->
m

<!-- b005721 | furniture | pages [19] -->
m

<!-- b005722 | furniture | pages [19] -->
m

<!-- b005723 | furniture | pages [19] -->
m

<!-- b005724 | furniture | pages [19] -->
m

<!-- b005725 | furniture | pages [19] -->
m

<!-- b005726 | furniture | pages [19] -->
m

<!-- b005727 | furniture | pages [19] -->
m

<!-- b005728 | furniture | pages [19] -->
m

<!-- b005729 | furniture | pages [19] -->
m

<!-- b005730 | furniture | pages [19] -->
m

<!-- b005731 | furniture | pages [19] -->
m

<!-- b005732 | furniture | pages [19] -->
m

<!-- b005733 | furniture | pages [19] -->
m

<!-- b005734 | furniture | pages [19] -->
m

<!-- b005735 | furniture | pages [19] -->
m

<!-- b005736 | furniture | pages [19] -->
m

<!-- b005737 | furniture | pages [19] -->
m

<!-- b005738 | furniture | pages [19] -->
m

<!-- b005739 | furniture | pages [19] -->
m

<!-- b005740 | furniture | pages [19] -->
m

<!-- b005741 | furniture | pages [19] -->
m

<!-- b005742 | furniture | pages [19] -->
m

<!-- b005743 | furniture | pages [19] -->
m

<!-- b005744 | furniture | pages [19] -->
m

<!-- b005745 | furniture | pages [19] -->
m

<!-- b005746 | furniture | pages [19] -->
m

<!-- b005747 | furniture | pages [19] -->
m

<!-- b005748 | furniture | pages [19] -->
m

<!-- b005749 | furniture | pages [19] -->
m

<!-- b005750 | furniture | pages [19] -->
m

<!-- b005751 | furniture | pages [19] -->
m

<!-- b005752 | furniture | pages [19] -->
m

<!-- b005753 | furniture | pages [19] -->
m

<!-- b005754 | furniture | pages [19] -->
m

<!-- b005755 | furniture | pages [19] -->
m

<!-- b005756 | furniture | pages [19] -->
m

<!-- b005757 | furniture | pages [19] -->
m

<!-- b005758 | furniture | pages [19] -->
m

<!-- b005759 | furniture | pages [19] -->
m

<!-- b005760 | furniture | pages [19] -->
m

<!-- b005761 | furniture | pages [19] -->
m

<!-- b005762 | furniture | pages [19] -->
m

<!-- b005763 | furniture | pages [19] -->
m

<!-- b005764 | furniture | pages [19] -->
m

<!-- b005765 | furniture | pages [19] -->
m

<!-- b005766 | furniture | pages [19] -->
m

<!-- b005767 | furniture | pages [19] -->
m

<!-- b005768 | furniture | pages [19] -->
m

<!-- b005769 | furniture | pages [19] -->
m

<!-- b005770 | furniture | pages [19] -->
m

<!-- b005771 | furniture | pages [19] -->
m

<!-- b005772 | furniture | pages [19] -->
m

<!-- b005773 | furniture | pages [19] -->
m

<!-- b005774 | furniture | pages [19] -->
m

<!-- b005775 | furniture | pages [19] -->
m

<!-- b005776 | furniture | pages [19] -->
m

<!-- b005777 | furniture | pages [19] -->
m

<!-- b005778 | furniture | pages [19] -->
m

<!-- b005779 | furniture | pages [19] -->
m

<!-- b005780 | furniture | pages [19] -->
m

<!-- b005781 | furniture | pages [19] -->
m

<!-- b005782 | furniture | pages [19] -->
m

<!-- b005783 | furniture | pages [19] -->
m

<!-- b005784 | furniture | pages [19] -->
m

<!-- b005785 | furniture | pages [19] -->
m

<!-- b005786 | furniture | pages [19] -->
m

<!-- b005787 | furniture | pages [19] -->
m

<!-- b005788 | furniture | pages [19] -->
m

<!-- b005789 | furniture | pages [19] -->
m

<!-- b005790 | furniture | pages [19] -->
m

<!-- b005791 | furniture | pages [19] -->
m

<!-- b005792 | furniture | pages [19] -->
m

<!-- b005793 | furniture | pages [19] -->
m

<!-- b005794 | furniture | pages [19] -->
m

<!-- b005795 | furniture | pages [19] -->
m

<!-- b005796 | furniture | pages [19] -->
m

<!-- b005797 | furniture | pages [19] -->
m

<!-- b005798 | furniture | pages [19] -->
m

<!-- b005799 | furniture | pages [19] -->
m

<!-- b005800 | furniture | pages [19] -->
m

<!-- b005801 | furniture | pages [19] -->
m

<!-- b005802 | furniture | pages [19] -->
m

<!-- b005803 | furniture | pages [19] -->
m

<!-- b005804 | furniture | pages [19] -->
m

<!-- b005805 | furniture | pages [19] -->
m

<!-- b005806 | furniture | pages [19] -->
m

<!-- b005807 | furniture | pages [19] -->
m

<!-- b005808 | furniture | pages [19] -->
m

<!-- b005809 | furniture | pages [19] -->
m

<!-- b005810 | furniture | pages [19] -->
m

<!-- b005811 | furniture | pages [19] -->
m

<!-- b005812 | furniture | pages [19] -->
m

<!-- b005813 | furniture | pages [19] -->
m

<!-- b005814 | furniture | pages [19] -->
m

<!-- b005815 | furniture | pages [19] -->
m

<!-- b005816 | furniture | pages [19] -->
m

<!-- b005817 | furniture | pages [19] -->
m

<!-- b005818 | furniture | pages [19] -->
m

<!-- b005819 | furniture | pages [19] -->
m

<!-- b005820 | furniture | pages [19] -->
m

<!-- b005821 | furniture | pages [19] -->
m

<!-- b005822 | furniture | pages [19] -->
m

<!-- b005823 | furniture | pages [19] -->
m

<!-- b005824 | furniture | pages [19] -->
m

<!-- b005825 | furniture | pages [19] -->
m

<!-- b005826 | furniture | pages [19] -->
m

<!-- b005827 | furniture | pages [19] -->
m

<!-- b005828 | furniture | pages [19] -->
m

<!-- b005829 | furniture | pages [19] -->
m

<!-- b005830 | furniture | pages [19] -->
m

<!-- b005831 | furniture | pages [19] -->
m

<!-- b005832 | furniture | pages [19] -->
m

<!-- b005833 | furniture | pages [19] -->
m

<!-- b005834 | furniture | pages [19] -->
m

<!-- b005835 | furniture | pages [19] -->
m

<!-- b005836 | furniture | pages [19] -->
m

<!-- b005837 | furniture | pages [19] -->
m

<!-- b005838 | furniture | pages [19] -->
m

<!-- b005839 | furniture | pages [19] -->
m

<!-- b005840 | furniture | pages [19] -->
m

<!-- b005841 | furniture | pages [19] -->
m

<!-- b005842 | furniture | pages [19] -->
m

<!-- b005843 | furniture | pages [19] -->
m

<!-- b005844 | furniture | pages [19] -->
m

<!-- b005845 | furniture | pages [19] -->
m

<!-- b005846 | furniture | pages [19] -->
m

<!-- b005847 | furniture | pages [19] -->
m

<!-- b005848 | furniture | pages [19] -->
m

<!-- b005849 | furniture | pages [19] -->
m

<!-- b005850 | furniture | pages [19] -->
m

<!-- b005851 | furniture | pages [19] -->
m

<!-- b005852 | furniture | pages [19] -->
m

<!-- b005853 | furniture | pages [19] -->
m

<!-- b005854 | furniture | pages [19] -->
m

<!-- b005855 | furniture | pages [19] -->
m

<!-- b005856 | furniture | pages [19] -->
m

<!-- b005857 | furniture | pages [19] -->
m

<!-- b005858 | furniture | pages [19] -->
m

<!-- b005859 | furniture | pages [19] -->
m

<!-- b005860 | furniture | pages [19] -->
m

<!-- b005861 | furniture | pages [19] -->
m

<!-- b005862 | furniture | pages [19] -->
m

<!-- b005863 | furniture | pages [19] -->
m

<!-- b005864 | furniture | pages [19] -->
m

<!-- b005865 | furniture | pages [19] -->
m

<!-- b005866 | furniture | pages [19] -->
m

<!-- b005867 | furniture | pages [19] -->
m

<!-- b005868 | furniture | pages [19] -->
m

<!-- b005869 | furniture | pages [19] -->
m

<!-- b005870 | furniture | pages [19] -->
m

<!-- b005871 | furniture | pages [19] -->
m

<!-- b005872 | furniture | pages [19] -->
m

<!-- b005873 | furniture | pages [19] -->
m

<!-- b005874 | furniture | pages [19] -->
m

<!-- b005875 | furniture | pages [19] -->
m

<!-- b005876 | furniture | pages [19] -->
m

<!-- b005877 | furniture | pages [19] -->
m

<!-- b005878 | furniture | pages [19] -->
m

<!-- b005879 | furniture | pages [19] -->
m

<!-- b005880 | furniture | pages [19] -->
m

<!-- b005881 | furniture | pages [19] -->
m

<!-- b005882 | furniture | pages [19] -->
m

<!-- b005883 | furniture | pages [19] -->
m

<!-- b005884 | furniture | pages [19] -->
m

<!-- b005885 | furniture | pages [19] -->
m

<!-- b005886 | furniture | pages [19] -->
m

<!-- b005887 | furniture | pages [19] -->
m

<!-- b005888 | furniture | pages [19] -->
m

<!-- b005889 | furniture | pages [19] -->
m

<!-- b005890 | furniture | pages [19] -->
m

<!-- b005891 | furniture | pages [19] -->
m

<!-- b005892 | furniture | pages [19] -->
m

<!-- b005893 | furniture | pages [19] -->
m

<!-- b005894 | furniture | pages [19] -->
m

<!-- b005895 | furniture | pages [19] -->
m

<!-- b005896 | furniture | pages [19] -->
m

<!-- b005897 | furniture | pages [19] -->
m

<!-- b005898 | furniture | pages [19] -->
m

<!-- b005899 | furniture | pages [19] -->
m

<!-- b005900 | furniture | pages [19] -->
m

<!-- b005901 | furniture | pages [19] -->
m

<!-- b005902 | furniture | pages [19] -->
m

<!-- b005903 | furniture | pages [19] -->
m

<!-- b005904 | furniture | pages [19] -->
m

<!-- b005905 | furniture | pages [19] -->
m

<!-- b005906 | furniture | pages [19] -->
m

<!-- b005907 | furniture | pages [19] -->
m

<!-- b005908 | furniture | pages [19] -->
m

<!-- b005909 | furniture | pages [19] -->
m

<!-- b005910 | furniture | pages [19] -->
m

<!-- b005911 | furniture | pages [19] -->
m

<!-- b005912 | furniture | pages [19] -->
m

<!-- b005913 | furniture | pages [19] -->
m

<!-- b005914 | furniture | pages [19] -->
m

<!-- b005915 | furniture | pages [19] -->
m

<!-- b005916 | furniture | pages [19] -->
m

<!-- b005917 | furniture | pages [19] -->
m

<!-- b005918 | furniture | pages [19] -->
m

<!-- b005919 | furniture | pages [19] -->
m

<!-- b005920 | furniture | pages [19] -->
m

<!-- b005921 | furniture | pages [19] -->
m

<!-- b005922 | furniture | pages [19] -->
m

<!-- b005923 | furniture | pages [19] -->
m

<!-- b005924 | furniture | pages [19] -->
m

<!-- b005925 | furniture | pages [19] -->
m

<!-- b005926 | furniture | pages [19] -->
m

<!-- b005927 | furniture | pages [19] -->
m

<!-- b005928 | furniture | pages [19] -->
m

<!-- b005929 | furniture | pages [19] -->
m

<!-- b005930 | furniture | pages [19] -->
m

<!-- b005931 | furniture | pages [19] -->
m

<!-- b005932 | furniture | pages [19] -->
m

<!-- b005933 | furniture | pages [19] -->
m

<!-- b005934 | furniture | pages [19] -->
m

<!-- b005935 | furniture | pages [19] -->
m

<!-- b005936 | furniture | pages [19] -->
m

<!-- b005937 | furniture | pages [19] -->
m

<!-- b005938 | furniture | pages [19] -->
m

<!-- b005939 | furniture | pages [19] -->
m

<!-- b005940 | furniture | pages [19] -->
m

<!-- b005941 | furniture | pages [19] -->
m

<!-- b005942 | furniture | pages [19] -->
m

<!-- b005943 | furniture | pages [19] -->
m

<!-- b005944 | furniture | pages [19] -->
m

<!-- b005945 | furniture | pages [19] -->
m

<!-- b005946 | furniture | pages [19] -->
m

<!-- b005947 | furniture | pages [19] -->
m

<!-- b005948 | furniture | pages [19] -->
m

<!-- b005949 | furniture | pages [19] -->
m

<!-- b005950 | furniture | pages [19] -->
m

<!-- b005951 | furniture | pages [19] -->
m

<!-- b005952 | furniture | pages [19] -->
m

<!-- b005953 | furniture | pages [19] -->
m

<!-- b005954 | furniture | pages [19] -->
m

<!-- b005955 | furniture | pages [19] -->
m

<!-- b005956 | furniture | pages [19] -->
m

<!-- b005957 | furniture | pages [19] -->
m

<!-- b005958 | furniture | pages [19] -->
m

<!-- b005959 | furniture | pages [19] -->
m

<!-- b005960 | furniture | pages [19] -->
m

<!-- b005961 | furniture | pages [19] -->
m

<!-- b005962 | furniture | pages [19] -->
m

<!-- b005963 | furniture | pages [19] -->
m

<!-- b005964 | furniture | pages [19] -->
m

<!-- b005965 | furniture | pages [19] -->
m

<!-- b005966 | furniture | pages [19] -->
m

<!-- b005967 | furniture | pages [19] -->
m

<!-- b005968 | furniture | pages [19] -->
m

<!-- b005969 | furniture | pages [19] -->
m

<!-- b005970 | furniture | pages [19] -->
m

<!-- b005971 | furniture | pages [19] -->
m

<!-- b005972 | furniture | pages [19] -->
m

<!-- b005973 | furniture | pages [19] -->
m

<!-- b005974 | furniture | pages [19] -->
m

<!-- b005975 | furniture | pages [19] -->
m

<!-- b005976 | furniture | pages [19] -->
m

<!-- b005977 | furniture | pages [19] -->
m

<!-- b005978 | furniture | pages [19] -->
m

<!-- b005979 | furniture | pages [19] -->
m

<!-- b005980 | furniture | pages [19] -->
m

<!-- b005981 | furniture | pages [19] -->
m

<!-- b005982 | furniture | pages [19] -->
m

<!-- b005983 | furniture | pages [19] -->
m

<!-- b005984 | furniture | pages [19] -->
m

<!-- b005985 | furniture | pages [19] -->
m

<!-- b005986 | furniture | pages [19] -->
m

<!-- b005987 | furniture | pages [19] -->
m

<!-- b005988 | furniture | pages [19] -->
m

<!-- b005989 | furniture | pages [19] -->
m

<!-- b005990 | furniture | pages [19] -->
m

<!-- b005991 | furniture | pages [19] -->
m

<!-- b005992 | furniture | pages [19] -->
m

<!-- b005993 | furniture | pages [19] -->
m

<!-- b005994 | furniture | pages [19] -->
m

<!-- b005995 | furniture | pages [19] -->
m

<!-- b005996 | furniture | pages [19] -->
m

<!-- b005997 | furniture | pages [19] -->
m

<!-- b005998 | furniture | pages [19] -->
m

<!-- b005999 | furniture | pages [19] -->
m

<!-- b006000 | furniture | pages [19] -->
m

<!-- b006001 | furniture | pages [19] -->
m

<!-- b006002 | furniture | pages [19] -->
m

<!-- b006003 | furniture | pages [19] -->
m

<!-- b006004 | furniture | pages [19] -->
m

<!-- b006005 | furniture | pages [19] -->
m

<!-- b006006 | furniture | pages [19] -->
m

<!-- b006007 | furniture | pages [19] -->
m

<!-- b006008 | furniture | pages [19] -->
m

<!-- b006009 | furniture | pages [19] -->
m

<!-- b006010 | furniture | pages [19] -->
m

<!-- b006011 | furniture | pages [19] -->
m

<!-- b006012 | furniture | pages [19] -->
m

<!-- b006013 | furniture | pages [19] -->
m

<!-- b006014 | furniture | pages [19] -->
m

<!-- b006015 | furniture | pages [19] -->
m

<!-- b006016 | furniture | pages [19] -->
m

<!-- b006017 | furniture | pages [19] -->
m

<!-- b006018 | furniture | pages [19] -->
m

<!-- b006019 | furniture | pages [19] -->
m

<!-- b006020 | furniture | pages [19] -->
m

<!-- b006021 | furniture | pages [19] -->
m

<!-- b006022 | furniture | pages [19] -->
m

<!-- b006023 | furniture | pages [19] -->
m

<!-- b006024 | furniture | pages [19] -->
m

<!-- b006025 | furniture | pages [19] -->
m

<!-- b006026 | furniture | pages [19] -->
m

<!-- b006027 | furniture | pages [19] -->
m

<!-- b006028 | furniture | pages [19] -->
m

<!-- b006029 | furniture | pages [19] -->
m

<!-- b006030 | furniture | pages [19] -->
m

<!-- b006031 | furniture | pages [19] -->
m

<!-- b006032 | furniture | pages [19] -->
m

<!-- b006033 | furniture | pages [19] -->
m

<!-- b006034 | furniture | pages [19] -->
m

<!-- b006035 | furniture | pages [19] -->
m

<!-- b006036 | furniture | pages [19] -->
m

<!-- b006037 | furniture | pages [19] -->
m

<!-- b006038 | furniture | pages [19] -->
m

<!-- b006039 | furniture | pages [19] -->
m

<!-- b006040 | furniture | pages [19] -->
m

<!-- b006041 | furniture | pages [19] -->
m

<!-- b006042 | furniture | pages [19] -->
m

<!-- b006043 | furniture | pages [19] -->
m

<!-- b006044 | furniture | pages [19] -->
m

<!-- b006045 | furniture | pages [19] -->
m

<!-- b006046 | furniture | pages [19] -->
m

<!-- b006047 | furniture | pages [19] -->
m

<!-- b006048 | furniture | pages [19] -->
m

<!-- b006049 | furniture | pages [19] -->
m

<!-- b006050 | furniture | pages [19] -->
m

<!-- b006051 | furniture | pages [19] -->
m

<!-- b006052 | furniture | pages [19] -->
m

<!-- b006053 | furniture | pages [19] -->
m

<!-- b006054 | furniture | pages [19] -->
m

<!-- b006055 | furniture | pages [19] -->
m

<!-- b006056 | furniture | pages [19] -->
m

<!-- b006057 | furniture | pages [19] -->
m

<!-- b006058 | furniture | pages [19] -->
m

<!-- b006059 | furniture | pages [19] -->
m

<!-- b006060 | furniture | pages [19] -->
m

<!-- b006061 | furniture | pages [20] -->
Team#2507817                                                             Page 20 of 25

<!-- b006062 | prose | pages [20] -->


<!-- b006063 | prose | pages [20] -->


<!-- b006064 | prose | pages [20] -->
x

<!-- b006065 | prose | pages [20] -->
i

<!-- b006066 | prose | pages [20] -->


<!-- b006067 | prose | pages [20] -->


<!-- b006068 | furniture | pages [20] -->


<!-- b006069 | furniture | pages [20] -->


<!-- b006070 | prose | pages [20] -->


<!-- b006071 | prose | pages [20] -->


<!-- b006072 | prose | pages [20] -->


<!-- b006073 | prose | pages [20] -->
x

<!-- b006074 | prose | pages [20] -->
i i

<!-- b006075 | prose | pages [20] -->
 

<!-- b006076 | prose | pages [20] -->
  

<!-- b006077 | prose | pages [20] -->
x y y

<!-- b006078 | prose | pages [20] -->
i i i

<!-- b006079 | furniture | pages [20] -->


<!-- b006080 | prose | pages [20] -->
(14)

<!-- b006081 | prose | pages [20] -->
  

<!-- b006082 | prose | pages [20] -->
2 2

<!-- b006083 | prose | pages [20] -->


<!-- b006084 | prose | pages [20] -->


<!-- b006085 | prose | pages [20] -->
x x y y

<!-- b006086 | prose | pages [20] -->
i i

<!-- b006087 | prose | pages [20] -->
The correlation coefficient between "great coaches" and the number of medals was calculated to be 0.874.

<!-- b006088 | prose | pages [20] -->
From the above analysis we can clearly realize that great coaches play a not insignificant role in improving sports performance, so we establish Lasso regression model for quantitative analysis

<!-- b006089 | heading | pages [20] -->
8.1.2 Lasso Regression Modeling

<!-- b006090 | prose | pages [20] -->
Lasso regression is an alternative to least squares for compression estimation, and its main goal is to find a balance between model simplicity and accuracy.

<!-- b006091 | heading | pages [20] -->
1) Linear Regression Model

<!-- b006092 | prose | pages [20] -->
A linear regression model is developed as follows

<!-- b006093 | prose | pages [20] -->
       

<!-- b006094 | furniture | pages [20] -->


<!-- b006095 | furniture | pages [20] -->


<!-- b006096 | prose | pages [20] -->
y I V 0 1 2

<!-- b006097 | prose | pages [20] -->


<!-- b006098 | prose | pages [20] -->
        S S A H C

<!-- b006099 | furniture | pages [20] -->


<!-- b006100 | prose | pages [20] -->
(15) 3 3 4 5 6

<!-- b006101 | prose | pages [20] -->
I,V,S,H,C are the indicators of the regression

<!-- b006102 | prose | pages [20] -->
I: Importance of the program to the state. According to the analysis in Task3, the state will use quality strategies to improve performance in programs of high importance, and these strategies include hiring great coaches.

<!-- b006103 | prose | pages [20] -->
V: Average number of points scored by the country in the last two Olympic Games. This indicator represents the average of the sum of the total points of the two most recent editions and reflects the country's overall performance in the two most recent Olympic Games.

<!-- b006104 | prose | pages [20] -->
S: theoretical points for the country on the program. s=I V is the program importance vs. average points score

<!-- b006105 | prose | pages [20] -->
A: The number of participants from that country in the current Olympic Games. The more athletes that participate, the greater the probability of winning a prize

<!-- b006106 | prose | pages [20] -->
H: The country's historical average points score for the project. This indicator reflects the level of the country's program and can reflect fluctuations in its performance.

<!-- b006107 | prose | pages [20] -->
C: Coaching Impact. To quantify the impact of coaching on performance, we define: coaching the first year of coaching C = 1, the length of each increase in the number of Olympic cycles, the performance has a linear increase of 0.1, when the coach leaves, the performance of the exponential decline,t represents the number of Olympic cycles that have begun & have ceased to coach:

<!-- b006108 | prose | pages [20] -->
 

<!-- b006109 | prose | pages [20] -->
1 0.1

<!-- b006110 | prose | pages [20] -->
t

<!-- b006111 | prose | pages [20] -->


<!-- b006112 | prose | pages [20] -->
C

<!-- b006113 | furniture | pages [20] -->


<!-- b006114 | prose | pages [20] -->
e

<!-- b006115 | prose | pages [20] -->
t

<!-- b006116 | prose | pages [20] -->


<!-- b006117 | prose | pages [20] -->


<!-- b006118 | prose | pages [20] -->
Start Coaching

<!-- b006119 | furniture | pages [20] -->


<!-- b006120 | prose | pages [20] -->
(16)

<!-- b006121 | prose | pages [20] -->
Stop Coaching

<!-- b006122 | prose | pages [20] -->
y is the score obtained from the regression

<!-- b006123 | prose | pages [20] -->
 βi is the coefficient to be estimated and ε is the error term

<!-- b006124 | heading | pages [20] -->
2) L1 Regularization

<!-- b006125 | prose | pages [20] -->
In the regression, we introduce an L1 penalty term so that the regression does not prioritize the reduction of any particular model parameter, retaining a few important features and

<!-- b006126 | furniture | pages [20] -->


<!-- b006127 | prose | pages [20] -->
关注数学模型

<!-- b006128 | furniture | pages [20] -->
2

<!-- b006129 | furniture | pages [20] -->
MATHmodels

<!-- b006130 | furniture | pages [20] -->
获取更多资讯

<!-- b006131 | furniture | pages [23] -->
Team#2507817                                                             Page 23 of 25

<!-- b006132 | prose | pages [23] -->
a) USA

<!-- b006133 | furniture | pages [23] -->


<!-- b006134 | furniture | pages [23] -->


<!-- b006135 | furniture | pages [23] -->


<!-- b006136 | furniture | pages [23] -->


<!-- b006137 | furniture | pages [23] -->


<!-- b006138 | furniture | pages [23] -->


<!-- b006139 | furniture | pages [23] -->


<!-- b006140 | furniture | pages [23] -->


<!-- b006141 | furniture | pages [23] -->


<!-- b006142 | furniture | pages [23] -->


<!-- b006143 | prose | pages [23] -->
b) JPN

<!-- b006144 | caption | pages [23] -->
Figure 21 Change in number of medals

<!-- b006145 | prose | pages [23] -->
微信公众号：数学模型

<!-- b006146 | prose | pages [23] -->
We have found that when the United States and Japan are the hosts, there is a 1.4 to 1.9 times increase in the number of gold medals and the total number of medals . The IOC can encourage countries to apply to host the Olympics based on this phenomenon.

<!-- b006147 | heading | pages [23] -->
9.2 Talented Athletes

<!-- b006148 | prose | pages [23] -->
In competition, there are athletes who train hard and achieve good results, and there are also highly talented competitors. If a country has been competing in an event for a long time and has only won a medal once, the winner can be called a "gifted athlete". For example, in the men's hurdles, China has been competing since 1984, and only Liu Xiang won the title in 2004;

<!-- b006149 | prose | pages [23] -->
微信号：MATHmodels

<!-- b006150 | prose | pages [23] -->
the rest of the athletes have not won a medal.

<!-- b006151 | furniture | pages [23] -->


<!-- b006152 | caption | pages [23] -->
Figure 22 Chinese men's hurdles

<!-- b006153 | prose | pages [23] -->
Accordingly, the IOC could encourage countries to tap talent in such programs and invest more in finding more talented players, who in turn could drive more hard-working players to the Olympic podium.

<!-- b006154 | heading | pages [23] -->
10 Error Analysis and Sensitivity Analysis

<!-- b006155 | prose | pages [23] -->
Based on the GSRF model established in the first problem, the sensitivity of athletes_num, Total event to Model can be obtained by changing athletes_num A , Total event E in the ij ij

<!-- b006156 | prose | pages [23] -->
model and observing the corresponding changes in Model.

<!-- b006157 | heading | pages [23] -->
10.1 Definition of Sensitivity

<!-- b006158 | prose | pages [23] -->
Define the result of this forecast as y , the difference between this result and the previous  , and the average sensitivity is defined forecast as y

<!-- b006159 | prose | pages [23] -->


<!-- b006160 | furniture | pages [23] -->


<!-- b006161 | furniture | pages [23] -->


<!-- b006162 | prose | pages [23] -->
ps

<!-- b006163 | prose | pages [23] -->
ps as:

<!-- b006164 | furniture | pages [23] -->


<!-- b006165 | prose | pages [23] -->
(20) y y

<!-- b006166 | prose | pages [23] -->
This indicator reflects the magnitude of change in the projected number of medals

<!-- b006167 | prose | pages [23] -->
m

<!-- b006168 | prose | pages [23] -->
m

<!-- b006169 | prose | pages [23] -->
m

<!-- b006170 | prose | pages [23] -->
m

<!-- b006171 | prose | pages [23] -->
m

<!-- b006172 | prose | pages [23] -->
m

<!-- b006173 | prose | pages [23] -->
m

<!-- b006174 | prose | pages [23] -->
m

<!-- b006175 | prose | pages [23] -->
m

<!-- b006176 | prose | pages [23] -->
m

<!-- b006177 | prose | pages [23] -->
m

<!-- b006178 | prose | pages [23] -->
m

<!-- b006179 | prose | pages [23] -->
m

<!-- b006180 | prose | pages [23] -->
m

<!-- b006181 | prose | pages [23] -->
m

<!-- b006182 | prose | pages [23] -->
m

<!-- b006183 | prose | pages [23] -->
m

<!-- b006184 | prose | pages [23] -->
m

<!-- b006185 | prose | pages [23] -->
m

<!-- b006186 | prose | pages [23] -->
m

<!-- b006187 | prose | pages [23] -->
m

<!-- b006188 | prose | pages [23] -->
m

<!-- b006189 | prose | pages [23] -->
m

<!-- b006190 | prose | pages [23] -->
m

<!-- b006191 | prose | pages [23] -->
m

<!-- b006192 | prose | pages [23] -->
m

<!-- b006193 | prose | pages [23] -->
m

<!-- b006194 | prose | pages [23] -->
m

<!-- b006195 | prose | pages [23] -->
m

<!-- b006196 | prose | pages [23] -->
m

<!-- b006197 | prose | pages [23] -->
m

<!-- b006198 | prose | pages [23] -->
m

<!-- b006199 | prose | pages [23] -->
m

<!-- b006200 | prose | pages [23] -->
m

<!-- b006201 | prose | pages [23] -->
m

<!-- b006202 | prose | pages [23] -->
m

<!-- b006203 | prose | pages [23] -->
m

<!-- b006204 | prose | pages [23] -->
m

<!-- b006205 | prose | pages [23] -->
m

<!-- b006206 | prose | pages [23] -->
m

<!-- b006207 | prose | pages [23] -->
m

<!-- b006208 | prose | pages [23] -->
m

<!-- b006209 | prose | pages [23] -->
m

<!-- b006210 | prose | pages [23] -->
m

<!-- b006211 | prose | pages [23] -->
m

<!-- b006212 | prose | pages [23] -->
m

<!-- b006213 | prose | pages [23] -->
m

<!-- b006214 | prose | pages [23] -->
m

<!-- b006215 | prose | pages [23] -->
m

<!-- b006216 | prose | pages [23] -->
m

<!-- b006217 | prose | pages [23] -->
m

<!-- b006218 | prose | pages [23] -->
m

<!-- b006219 | prose | pages [23] -->
m

<!-- b006220 | prose | pages [23] -->
m

<!-- b006221 | prose | pages [23] -->
m

<!-- b006222 | prose | pages [23] -->
m

<!-- b006223 | prose | pages [23] -->
m

<!-- b006224 | prose | pages [23] -->
m

<!-- b006225 | prose | pages [23] -->
m

<!-- b006226 | prose | pages [23] -->
m

<!-- b006227 | prose | pages [23] -->
m

<!-- b006228 | prose | pages [23] -->
m

<!-- b006229 | prose | pages [23] -->
m

<!-- b006230 | prose | pages [23] -->
m

<!-- b006231 | prose | pages [23] -->
m

<!-- b006232 | prose | pages [23] -->
m

<!-- b006233 | prose | pages [23] -->
m

<!-- b006234 | prose | pages [23] -->
m

<!-- b006235 | prose | pages [23] -->
m

<!-- b006236 | prose | pages [23] -->
m

<!-- b006237 | prose | pages [23] -->
m

<!-- b006238 | prose | pages [23] -->
m

<!-- b006239 | prose | pages [23] -->
m

<!-- b006240 | prose | pages [23] -->
m

<!-- b006241 | prose | pages [23] -->
m

<!-- b006242 | prose | pages [23] -->
m

<!-- b006243 | prose | pages [23] -->
m

<!-- b006244 | prose | pages [23] -->
m

<!-- b006245 | prose | pages [23] -->
m

<!-- b006246 | prose | pages [23] -->
m

<!-- b006247 | prose | pages [23] -->
m

<!-- b006248 | prose | pages [23] -->
m

<!-- b006249 | prose | pages [23] -->
m

<!-- b006250 | prose | pages [23] -->
m

<!-- b006251 | prose | pages [23] -->
m

<!-- b006252 | prose | pages [23] -->
m

<!-- b006253 | prose | pages [23] -->
m

<!-- b006254 | prose | pages [23] -->
m

<!-- b006255 | prose | pages [23] -->
m

<!-- b006256 | prose | pages [23] -->
m

<!-- b006257 | prose | pages [23] -->
m

<!-- b006258 | prose | pages [23] -->
m

<!-- b006259 | prose | pages [23] -->
m

<!-- b006260 | prose | pages [23] -->
m

<!-- b006261 | prose | pages [23] -->
m

<!-- b006262 | prose | pages [23] -->
m

<!-- b006263 | prose | pages [23] -->
m

<!-- b006264 | prose | pages [23] -->
m

<!-- b006265 | prose | pages [23] -->
m

<!-- b006266 | prose | pages [23] -->
m

<!-- b006267 | prose | pages [23] -->
m

<!-- b006268 | prose | pages [23] -->
m

<!-- b006269 | prose | pages [23] -->
m

<!-- b006270 | prose | pages [23] -->
m

<!-- b006271 | prose | pages [23] -->
m

<!-- b006272 | prose | pages [23] -->
m

<!-- b006273 | prose | pages [23] -->
m

<!-- b006274 | prose | pages [23] -->
m

<!-- b006275 | prose | pages [23] -->
m

<!-- b006276 | prose | pages [23] -->
m

<!-- b006277 | prose | pages [23] -->
m

<!-- b006278 | prose | pages [23] -->
m

<!-- b006279 | prose | pages [23] -->
m

<!-- b006280 | prose | pages [23] -->
m

<!-- b006281 | prose | pages [23] -->
m

<!-- b006282 | prose | pages [23] -->
m

<!-- b006283 | prose | pages [23] -->
m

<!-- b006284 | prose | pages [23] -->
m

<!-- b006285 | prose | pages [23] -->
m

<!-- b006286 | prose | pages [23] -->
m

<!-- b006287 | prose | pages [23] -->
m

<!-- b006288 | prose | pages [23] -->
m

<!-- b006289 | prose | pages [23] -->
m

<!-- b006290 | prose | pages [23] -->
m

<!-- b006291 | prose | pages [23] -->
m

<!-- b006292 | prose | pages [23] -->
m

<!-- b006293 | prose | pages [23] -->
m

<!-- b006294 | prose | pages [23] -->
m

<!-- b006295 | prose | pages [23] -->
m

<!-- b006296 | prose | pages [23] -->
m

<!-- b006297 | furniture | pages [23] -->


<!-- b006298 | prose | pages [23] -->
m

<!-- b006299 | prose | pages [23] -->
m

<!-- b006300 | prose | pages [23] -->
m

<!-- b006301 | prose | pages [23] -->
m

<!-- b006302 | prose | pages [23] -->
m

<!-- b006303 | prose | pages [23] -->
m

<!-- b006304 | prose | pages [23] -->
m

<!-- b006305 | prose | pages [23] -->
m

<!-- b006306 | prose | pages [23] -->
m

<!-- b006307 | prose | pages [23] -->
m

<!-- b006308 | prose | pages [23] -->
m

<!-- b006309 | prose | pages [23] -->
m

<!-- b006310 | prose | pages [23] -->
m

<!-- b006311 | prose | pages [23] -->
m

<!-- b006312 | prose | pages [23] -->
m

<!-- b006313 | prose | pages [23] -->
m

<!-- b006314 | prose | pages [23] -->
m

<!-- b006315 | prose | pages [23] -->
m

<!-- b006316 | prose | pages [23] -->
m

<!-- b006317 | prose | pages [23] -->
m

<!-- b006318 | prose | pages [23] -->
m

<!-- b006319 | prose | pages [23] -->
m

<!-- b006320 | prose | pages [23] -->
m

<!-- b006321 | prose | pages [23] -->
m

<!-- b006322 | prose | pages [23] -->
m

<!-- b006323 | prose | pages [23] -->
m

<!-- b006324 | prose | pages [23] -->
m

<!-- b006325 | prose | pages [23] -->
m

<!-- b006326 | prose | pages [23] -->
m

<!-- b006327 | prose | pages [23] -->
m

<!-- b006328 | prose | pages [23] -->
m

<!-- b006329 | prose | pages [23] -->
m

<!-- b006330 | prose | pages [23] -->
m

<!-- b006331 | prose | pages [23] -->
m

<!-- b006332 | prose | pages [23] -->
m

<!-- b006333 | prose | pages [23] -->
m

<!-- b006334 | prose | pages [23] -->
m

<!-- b006335 | prose | pages [23] -->
m

<!-- b006336 | prose | pages [23] -->
m

<!-- b006337 | prose | pages [23] -->
m

<!-- b006338 | prose | pages [23] -->
m

<!-- b006339 | prose | pages [23] -->
m

<!-- b006340 | prose | pages [23] -->
m

<!-- b006341 | prose | pages [23] -->
m

<!-- b006342 | prose | pages [23] -->
m

<!-- b006343 | prose | pages [23] -->
m

<!-- b006344 | prose | pages [23] -->
m

<!-- b006345 | prose | pages [23] -->
m

<!-- b006346 | prose | pages [23] -->
m

<!-- b006347 | prose | pages [23] -->
m

<!-- b006348 | prose | pages [23] -->
m

<!-- b006349 | prose | pages [23] -->
m

<!-- b006350 | prose | pages [23] -->
m

<!-- b006351 | prose | pages [23] -->
m

<!-- b006352 | prose | pages [23] -->
m

<!-- b006353 | prose | pages [23] -->
m

<!-- b006354 | prose | pages [23] -->
m

<!-- b006355 | prose | pages [23] -->
m

<!-- b006356 | prose | pages [23] -->
m

<!-- b006357 | prose | pages [23] -->
m

<!-- b006358 | prose | pages [23] -->
m

<!-- b006359 | prose | pages [23] -->
m

<!-- b006360 | prose | pages [23] -->
m

<!-- b006361 | prose | pages [23] -->
m

<!-- b006362 | prose | pages [23] -->
m

<!-- b006363 | prose | pages [23] -->
m

<!-- b006364 | prose | pages [23] -->
m

<!-- b006365 | prose | pages [23] -->
m

<!-- b006366 | prose | pages [23] -->
m

<!-- b006367 | prose | pages [23] -->
m

<!-- b006368 | prose | pages [23] -->
m

<!-- b006369 | prose | pages [23] -->
m

<!-- b006370 | prose | pages [23] -->
m

<!-- b006371 | prose | pages [23] -->
m

<!-- b006372 | prose | pages [23] -->
m

<!-- b006373 | prose | pages [23] -->
m

<!-- b006374 | prose | pages [23] -->
m

<!-- b006375 | prose | pages [23] -->
m

<!-- b006376 | prose | pages [23] -->
m

<!-- b006377 | prose | pages [23] -->
m

<!-- b006378 | prose | pages [23] -->
m

<!-- b006379 | prose | pages [23] -->
m

<!-- b006380 | prose | pages [23] -->
m

<!-- b006381 | prose | pages [23] -->
m

<!-- b006382 | prose | pages [23] -->
m

<!-- b006383 | prose | pages [23] -->
m

<!-- b006384 | prose | pages [23] -->
m

<!-- b006385 | prose | pages [23] -->
m

<!-- b006386 | prose | pages [23] -->
m

<!-- b006387 | prose | pages [23] -->
m

<!-- b006388 | prose | pages [23] -->
m

<!-- b006389 | prose | pages [23] -->
m

<!-- b006390 | prose | pages [23] -->
m

<!-- b006391 | prose | pages [23] -->
m

<!-- b006392 | prose | pages [23] -->
m

<!-- b006393 | prose | pages [23] -->
m

<!-- b006394 | prose | pages [23] -->
m

<!-- b006395 | prose | pages [23] -->
m

<!-- b006396 | prose | pages [23] -->
m

<!-- b006397 | prose | pages [23] -->
m

<!-- b006398 | prose | pages [23] -->
m

<!-- b006399 | prose | pages [23] -->
m

<!-- b006400 | prose | pages [23] -->
m

<!-- b006401 | prose | pages [23] -->
m

<!-- b006402 | prose | pages [23] -->
m

<!-- b006403 | prose | pages [23] -->
m

<!-- b006404 | prose | pages [23] -->
m

<!-- b006405 | prose | pages [23] -->
m

<!-- b006406 | prose | pages [23] -->
m

<!-- b006407 | prose | pages [23] -->
m

<!-- b006408 | prose | pages [23] -->
m

<!-- b006409 | prose | pages [23] -->
m

<!-- b006410 | prose | pages [23] -->
m

<!-- b006411 | prose | pages [23] -->
m

<!-- b006412 | prose | pages [23] -->
m

<!-- b006413 | prose | pages [23] -->
m

<!-- b006414 | prose | pages [23] -->
m

<!-- b006415 | prose | pages [23] -->
m

<!-- b006416 | prose | pages [23] -->
m

<!-- b006417 | prose | pages [23] -->
m

<!-- b006418 | prose | pages [23] -->
m

<!-- b006419 | prose | pages [23] -->
m

<!-- b006420 | prose | pages [23] -->
m

<!-- b006421 | prose | pages [23] -->
m

<!-- b006422 | prose | pages [23] -->
m

<!-- b006423 | prose | pages [23] -->
m

<!-- b006424 | prose | pages [23] -->
m

<!-- b006425 | prose | pages [23] -->
m

<!-- b006426 | prose | pages [23] -->
m

<!-- b006427 | prose | pages [23] -->
m

<!-- b006428 | prose | pages [23] -->
m

<!-- b006429 | prose | pages [23] -->
m

<!-- b006430 | prose | pages [23] -->
m

<!-- b006431 | prose | pages [23] -->
m

<!-- b006432 | prose | pages [23] -->
m

<!-- b006433 | prose | pages [23] -->
m

<!-- b006434 | prose | pages [23] -->
m

<!-- b006435 | prose | pages [23] -->
m

<!-- b006436 | prose | pages [23] -->
m

<!-- b006437 | prose | pages [23] -->
m

<!-- b006438 | prose | pages [23] -->
m

<!-- b006439 | prose | pages [23] -->
m

<!-- b006440 | prose | pages [23] -->
m

<!-- b006441 | prose | pages [23] -->
m

<!-- b006442 | prose | pages [23] -->
m

<!-- b006443 | prose | pages [23] -->
m

<!-- b006444 | prose | pages [23] -->
m

<!-- b006445 | prose | pages [23] -->
m

<!-- b006446 | prose | pages [23] -->
m

<!-- b006447 | prose | pages [23] -->
m

<!-- b006448 | prose | pages [23] -->
m

<!-- b006449 | prose | pages [23] -->
m

<!-- b006450 | prose | pages [23] -->
m

<!-- b006451 | prose | pages [23] -->
m

<!-- b006452 | furniture | pages [23] -->
m

<!-- b006453 | furniture | pages [23] -->
m

<!-- b006454 | furniture | pages [23] -->
m

<!-- b006455 | furniture | pages [23] -->
m

<!-- b006456 | furniture | pages [23] -->
m

<!-- b006457 | furniture | pages [23] -->
m

<!-- b006458 | furniture | pages [23] -->
m

<!-- b006459 | furniture | pages [23] -->
m

<!-- b006460 | furniture | pages [23] -->
m

<!-- b006461 | furniture | pages [23] -->
m

<!-- b006462 | furniture | pages [23] -->
m

<!-- b006463 | furniture | pages [23] -->
m

<!-- b006464 | furniture | pages [23] -->
m

<!-- b006465 | furniture | pages [23] -->
m

<!-- b006466 | furniture | pages [23] -->
m

<!-- b006467 | furniture | pages [23] -->
m

<!-- b006468 | furniture | pages [23] -->
m

<!-- b006469 | furniture | pages [23] -->
m

<!-- b006470 | furniture | pages [23] -->
m

<!-- b006471 | furniture | pages [23] -->
m

<!-- b006472 | furniture | pages [23] -->
m

<!-- b006473 | furniture | pages [23] -->
m

<!-- b006474 | furniture | pages [23] -->
m

<!-- b006475 | furniture | pages [23] -->
m

<!-- b006476 | furniture | pages [23] -->
m

<!-- b006477 | furniture | pages [23] -->
m

<!-- b006478 | furniture | pages [23] -->
m

<!-- b006479 | furniture | pages [23] -->
m

<!-- b006480 | furniture | pages [23] -->
m

<!-- b006481 | furniture | pages [23] -->
m

<!-- b006482 | furniture | pages [23] -->
m

<!-- b006483 | furniture | pages [23] -->
m

<!-- b006484 | furniture | pages [23] -->
m

<!-- b006485 | furniture | pages [23] -->
m

<!-- b006486 | furniture | pages [23] -->
m

<!-- b006487 | furniture | pages [23] -->
m

<!-- b006488 | furniture | pages [23] -->
m

<!-- b006489 | furniture | pages [23] -->
m

<!-- b006490 | furniture | pages [23] -->
m

<!-- b006491 | furniture | pages [23] -->
m

<!-- b006492 | furniture | pages [23] -->
m

<!-- b006493 | furniture | pages [23] -->
m

<!-- b006494 | furniture | pages [23] -->
m

<!-- b006495 | furniture | pages [23] -->
m

<!-- b006496 | furniture | pages [23] -->
m

<!-- b006497 | furniture | pages [23] -->
m

<!-- b006498 | furniture | pages [23] -->
m

<!-- b006499 | furniture | pages [23] -->
m

<!-- b006500 | furniture | pages [23] -->
m

<!-- b006501 | furniture | pages [23] -->
m

<!-- b006502 | furniture | pages [23] -->
m

<!-- b006503 | furniture | pages [23] -->
m

<!-- b006504 | furniture | pages [23] -->
m

<!-- b006505 | furniture | pages [23] -->
m

<!-- b006506 | furniture | pages [23] -->
m

<!-- b006507 | furniture | pages [23] -->
m

<!-- b006508 | furniture | pages [23] -->
m

<!-- b006509 | furniture | pages [23] -->
m

<!-- b006510 | furniture | pages [23] -->
m

<!-- b006511 | furniture | pages [23] -->
m

<!-- b006512 | furniture | pages [23] -->
m

<!-- b006513 | furniture | pages [23] -->
m

<!-- b006514 | furniture | pages [23] -->
m

<!-- b006515 | furniture | pages [23] -->
m

<!-- b006516 | furniture | pages [23] -->
m

<!-- b006517 | furniture | pages [23] -->
m

<!-- b006518 | furniture | pages [23] -->
m

<!-- b006519 | furniture | pages [23] -->
m

<!-- b006520 | furniture | pages [23] -->
m

<!-- b006521 | furniture | pages [23] -->
m

<!-- b006522 | furniture | pages [23] -->
m

<!-- b006523 | furniture | pages [23] -->
m

<!-- b006524 | furniture | pages [23] -->
m

<!-- b006525 | furniture | pages [23] -->
m

<!-- b006526 | furniture | pages [23] -->
m

<!-- b006527 | furniture | pages [23] -->
m

<!-- b006528 | furniture | pages [23] -->
m

<!-- b006529 | furniture | pages [23] -->
m

<!-- b006530 | furniture | pages [23] -->
m

<!-- b006531 | furniture | pages [23] -->
m

<!-- b006532 | furniture | pages [23] -->
m

<!-- b006533 | furniture | pages [23] -->
m

<!-- b006534 | furniture | pages [23] -->
m

<!-- b006535 | furniture | pages [23] -->
m

<!-- b006536 | furniture | pages [23] -->
m

<!-- b006537 | furniture | pages [23] -->
m

<!-- b006538 | furniture | pages [23] -->
m

<!-- b006539 | furniture | pages [23] -->
m

<!-- b006540 | furniture | pages [23] -->
m

<!-- b006541 | furniture | pages [23] -->
m

<!-- b006542 | furniture | pages [23] -->
m

<!-- b006543 | furniture | pages [23] -->
m

<!-- b006544 | furniture | pages [23] -->
m

<!-- b006545 | furniture | pages [23] -->
m

<!-- b006546 | furniture | pages [23] -->
m

<!-- b006547 | furniture | pages [23] -->
m

<!-- b006548 | furniture | pages [23] -->
m

<!-- b006549 | furniture | pages [23] -->
m

<!-- b006550 | furniture | pages [23] -->
m

<!-- b006551 | furniture | pages [23] -->
m

<!-- b006552 | furniture | pages [23] -->
m

<!-- b006553 | furniture | pages [23] -->
m

<!-- b006554 | furniture | pages [23] -->
m

<!-- b006555 | furniture | pages [23] -->
m

<!-- b006556 | furniture | pages [23] -->
m

<!-- b006557 | furniture | pages [23] -->
m

<!-- b006558 | furniture | pages [23] -->
m

<!-- b006559 | furniture | pages [23] -->
m

<!-- b006560 | furniture | pages [23] -->
m

<!-- b006561 | furniture | pages [23] -->
m

<!-- b006562 | furniture | pages [23] -->
m

<!-- b006563 | furniture | pages [23] -->
m

<!-- b006564 | furniture | pages [23] -->
m

<!-- b006565 | furniture | pages [23] -->
m

<!-- b006566 | furniture | pages [23] -->
m

<!-- b006567 | furniture | pages [23] -->
m

<!-- b006568 | furniture | pages [23] -->
m

<!-- b006569 | furniture | pages [23] -->
m

<!-- b006570 | furniture | pages [23] -->
m

<!-- b006571 | furniture | pages [23] -->
m

<!-- b006572 | furniture | pages [23] -->
m

<!-- b006573 | furniture | pages [23] -->
m

<!-- b006574 | furniture | pages [23] -->
m

<!-- b006575 | furniture | pages [23] -->
m

<!-- b006576 | furniture | pages [23] -->
m

<!-- b006577 | furniture | pages [23] -->
m

<!-- b006578 | furniture | pages [23] -->
m

<!-- b006579 | furniture | pages [23] -->
m

<!-- b006580 | furniture | pages [23] -->
m

<!-- b006581 | furniture | pages [23] -->
m

<!-- b006582 | furniture | pages [23] -->
m

<!-- b006583 | furniture | pages [23] -->
m

<!-- b006584 | furniture | pages [23] -->
m

<!-- b006585 | furniture | pages [23] -->
m

<!-- b006586 | furniture | pages [23] -->
m

<!-- b006587 | furniture | pages [23] -->
m

<!-- b006588 | furniture | pages [23] -->
m

<!-- b006589 | furniture | pages [23] -->
m

<!-- b006590 | furniture | pages [23] -->
m

<!-- b006591 | furniture | pages [23] -->
m

<!-- b006592 | furniture | pages [23] -->
m

<!-- b006593 | furniture | pages [23] -->
m

<!-- b006594 | furniture | pages [23] -->
m

<!-- b006595 | furniture | pages [23] -->
m

<!-- b006596 | furniture | pages [23] -->
m

<!-- b006597 | furniture | pages [23] -->
m

<!-- b006598 | furniture | pages [23] -->
m

<!-- b006599 | furniture | pages [23] -->
m

<!-- b006600 | furniture | pages [23] -->
m

<!-- b006601 | furniture | pages [23] -->
m

<!-- b006602 | furniture | pages [23] -->
m

<!-- b006603 | furniture | pages [23] -->
m

<!-- b006604 | furniture | pages [23] -->
m

<!-- b006605 | furniture | pages [23] -->
m

<!-- b006606 | furniture | pages [23] -->
m

<!-- b006607 | furniture | pages [23] -->
m

<!-- b006608 | furniture | pages [23] -->
m

<!-- b006609 | furniture | pages [23] -->
m

<!-- b006610 | furniture | pages [23] -->
m

<!-- b006611 | furniture | pages [23] -->
m

<!-- b006612 | furniture | pages [23] -->
m

<!-- b006613 | furniture | pages [23] -->
m

<!-- b006614 | furniture | pages [23] -->
m

<!-- b006615 | furniture | pages [23] -->
m

<!-- b006616 | furniture | pages [23] -->
m

<!-- b006617 | furniture | pages [23] -->
m

<!-- b006618 | furniture | pages [23] -->
m

<!-- b006619 | furniture | pages [23] -->
m

<!-- b006620 | furniture | pages [23] -->
m

<!-- b006621 | furniture | pages [23] -->
m

<!-- b006622 | furniture | pages [23] -->
m

<!-- b006623 | furniture | pages [23] -->
m

<!-- b006624 | furniture | pages [23] -->
m

<!-- b006625 | furniture | pages [23] -->
m

<!-- b006626 | furniture | pages [23] -->
m

<!-- b006627 | furniture | pages [23] -->
m

<!-- b006628 | furniture | pages [23] -->
m

<!-- b006629 | furniture | pages [23] -->
m

<!-- b006630 | furniture | pages [23] -->
m

<!-- b006631 | furniture | pages [23] -->
m

<!-- b006632 | furniture | pages [23] -->
m

<!-- b006633 | furniture | pages [23] -->
m

<!-- b006634 | furniture | pages [23] -->
m

<!-- b006635 | furniture | pages [23] -->
m

<!-- b006636 | furniture | pages [23] -->
m

<!-- b006637 | furniture | pages [23] -->
m

<!-- b006638 | furniture | pages [23] -->
m

<!-- b006639 | furniture | pages [23] -->
m

<!-- b006640 | furniture | pages [23] -->
m

<!-- b006641 | furniture | pages [23] -->
m

<!-- b006642 | furniture | pages [23] -->
m

<!-- b006643 | furniture | pages [23] -->
m

<!-- b006644 | furniture | pages [23] -->
m

<!-- b006645 | furniture | pages [23] -->
m

<!-- b006646 | furniture | pages [23] -->
m

<!-- b006647 | furniture | pages [23] -->
m

<!-- b006648 | furniture | pages [23] -->
m

<!-- b006649 | furniture | pages [23] -->
m

<!-- b006650 | furniture | pages [23] -->
m

<!-- b006651 | furniture | pages [23] -->
m

<!-- b006652 | furniture | pages [23] -->
m

<!-- b006653 | furniture | pages [23] -->
m

<!-- b006654 | furniture | pages [23] -->
m

<!-- b006655 | furniture | pages [23] -->
m

<!-- b006656 | furniture | pages [23] -->
m

<!-- b006657 | furniture | pages [23] -->
m

<!-- b006658 | furniture | pages [23] -->
m

<!-- b006659 | furniture | pages [23] -->
m

<!-- b006660 | furniture | pages [23] -->
m

<!-- b006661 | furniture | pages [23] -->
m

<!-- b006662 | furniture | pages [23] -->
m

<!-- b006663 | furniture | pages [23] -->
m

<!-- b006664 | furniture | pages [23] -->
m

<!-- b006665 | furniture | pages [23] -->
m

<!-- b006666 | furniture | pages [23] -->
m

<!-- b006667 | furniture | pages [23] -->
m

<!-- b006668 | furniture | pages [23] -->
m

<!-- b006669 | furniture | pages [23] -->
m

<!-- b006670 | furniture | pages [23] -->
m

<!-- b006671 | furniture | pages [23] -->
m

<!-- b006672 | furniture | pages [23] -->
m

<!-- b006673 | furniture | pages [23] -->
m

<!-- b006674 | furniture | pages [23] -->
m

<!-- b006675 | furniture | pages [23] -->
m

<!-- b006676 | furniture | pages [23] -->
m

<!-- b006677 | furniture | pages [23] -->
m

<!-- b006678 | furniture | pages [23] -->
m

<!-- b006679 | furniture | pages [23] -->
m

<!-- b006680 | furniture | pages [23] -->
m

<!-- b006681 | furniture | pages [23] -->
m

<!-- b006682 | furniture | pages [23] -->
m

<!-- b006683 | furniture | pages [23] -->
m

<!-- b006684 | furniture | pages [23] -->
m

<!-- b006685 | furniture | pages [23] -->
m

<!-- b006686 | furniture | pages [23] -->
m

<!-- b006687 | furniture | pages [23] -->
m

<!-- b006688 | furniture | pages [23] -->
m

<!-- b006689 | furniture | pages [23] -->
m

<!-- b006690 | furniture | pages [23] -->
m

<!-- b006691 | furniture | pages [23] -->
m

<!-- b006692 | furniture | pages [23] -->
m

<!-- b006693 | furniture | pages [23] -->
m

<!-- b006694 | furniture | pages [23] -->
m

<!-- b006695 | furniture | pages [23] -->
m

<!-- b006696 | furniture | pages [23] -->
m

<!-- b006697 | furniture | pages [23] -->
m

<!-- b006698 | furniture | pages [23] -->
m

<!-- b006699 | furniture | pages [23] -->
m

<!-- b006700 | furniture | pages [23] -->
m

<!-- b006701 | furniture | pages [23] -->
m

<!-- b006702 | furniture | pages [23] -->
m

<!-- b006703 | furniture | pages [23] -->
m

<!-- b006704 | furniture | pages [23] -->
m

<!-- b006705 | furniture | pages [23] -->
m

<!-- b006706 | furniture | pages [23] -->
m

<!-- b006707 | furniture | pages [23] -->
m

<!-- b006708 | furniture | pages [23] -->
m

<!-- b006709 | furniture | pages [23] -->
m

<!-- b006710 | furniture | pages [23] -->
m

<!-- b006711 | furniture | pages [23] -->
m

<!-- b006712 | furniture | pages [23] -->
m

<!-- b006713 | furniture | pages [23] -->
m

<!-- b006714 | furniture | pages [23] -->
m

<!-- b006715 | furniture | pages [23] -->
m

<!-- b006716 | furniture | pages [23] -->
m

<!-- b006717 | furniture | pages [23] -->
m

<!-- b006718 | furniture | pages [23] -->
m

<!-- b006719 | furniture | pages [23] -->
m

<!-- b006720 | furniture | pages [23] -->
m

<!-- b006721 | furniture | pages [23] -->
m

<!-- b006722 | furniture | pages [23] -->
m

<!-- b006723 | furniture | pages [23] -->
m

<!-- b006724 | furniture | pages [23] -->
m

<!-- b006725 | furniture | pages [23] -->
m

<!-- b006726 | furniture | pages [23] -->
m

<!-- b006727 | furniture | pages [23] -->
m

<!-- b006728 | furniture | pages [23] -->
m

<!-- b006729 | furniture | pages [23] -->
m

<!-- b006730 | furniture | pages [23] -->
m

<!-- b006731 | furniture | pages [23] -->
m

<!-- b006732 | furniture | pages [23] -->
m

<!-- b006733 | furniture | pages [23] -->
m

<!-- b006734 | furniture | pages [23] -->
m

<!-- b006735 | furniture | pages [23] -->
m

<!-- b006736 | furniture | pages [23] -->
m

<!-- b006737 | furniture | pages [23] -->
m

<!-- b006738 | furniture | pages [23] -->
m

<!-- b006739 | furniture | pages [23] -->
m

<!-- b006740 | furniture | pages [23] -->
m

<!-- b006741 | furniture | pages [23] -->
m

<!-- b006742 | furniture | pages [23] -->
m

<!-- b006743 | furniture | pages [23] -->
m

<!-- b006744 | furniture | pages [23] -->
m

<!-- b006745 | furniture | pages [23] -->
m

<!-- b006746 | furniture | pages [23] -->
m

<!-- b006747 | furniture | pages [23] -->
m

<!-- b006748 | furniture | pages [23] -->
m

<!-- b006749 | furniture | pages [23] -->
m

<!-- b006750 | furniture | pages [23] -->
m

<!-- b006751 | furniture | pages [23] -->
m

<!-- b006752 | furniture | pages [23] -->
m

<!-- b006753 | furniture | pages [23] -->
m

<!-- b006754 | furniture | pages [23] -->
m

<!-- b006755 | furniture | pages [23] -->
m

<!-- b006756 | furniture | pages [23] -->
m

<!-- b006757 | furniture | pages [23] -->
m

<!-- b006758 | furniture | pages [23] -->
m

<!-- b006759 | furniture | pages [23] -->
m

<!-- b006760 | furniture | pages [23] -->
m

<!-- b006761 | furniture | pages [23] -->
m

<!-- b006762 | furniture | pages [23] -->
m

<!-- b006763 | furniture | pages [23] -->
m

<!-- b006764 | furniture | pages [23] -->
m

<!-- b006765 | furniture | pages [23] -->
m

<!-- b006766 | furniture | pages [23] -->
m

<!-- b006767 | furniture | pages [23] -->
m

<!-- b006768 | furniture | pages [23] -->
m

<!-- b006769 | furniture | pages [23] -->
m

<!-- b006770 | furniture | pages [23] -->
m

<!-- b006771 | furniture | pages [23] -->
m

<!-- b006772 | furniture | pages [23] -->
m

<!-- b006773 | furniture | pages [23] -->
m

<!-- b006774 | furniture | pages [23] -->
m

<!-- b006775 | furniture | pages [23] -->
m

<!-- b006776 | furniture | pages [23] -->
m

<!-- b006777 | furniture | pages [23] -->
m

<!-- b006778 | furniture | pages [23] -->
m

<!-- b006779 | furniture | pages [23] -->
m

<!-- b006780 | furniture | pages [23] -->
m

<!-- b006781 | furniture | pages [23] -->
m

<!-- b006782 | furniture | pages [23] -->
m

<!-- b006783 | furniture | pages [23] -->
m

<!-- b006784 | furniture | pages [23] -->
m

<!-- b006785 | furniture | pages [23] -->
m

<!-- b006786 | furniture | pages [23] -->
m

<!-- b006787 | furniture | pages [23] -->
m

<!-- b006788 | furniture | pages [23] -->
m

<!-- b006789 | furniture | pages [23] -->
m

<!-- b006790 | furniture | pages [23] -->
m

<!-- b006791 | furniture | pages [23] -->
m

<!-- b006792 | furniture | pages [23] -->
m

<!-- b006793 | furniture | pages [23] -->
m

<!-- b006794 | furniture | pages [23] -->
m

<!-- b006795 | furniture | pages [23] -->
m

<!-- b006796 | furniture | pages [23] -->
m

<!-- b006797 | furniture | pages [23] -->
m

<!-- b006798 | furniture | pages [23] -->
m

<!-- b006799 | furniture | pages [23] -->
m

<!-- b006800 | furniture | pages [23] -->
m

<!-- b006801 | furniture | pages [23] -->
m

<!-- b006802 | furniture | pages [23] -->
m

<!-- b006803 | furniture | pages [23] -->
m

<!-- b006804 | furniture | pages [23] -->
m

<!-- b006805 | furniture | pages [23] -->
m

<!-- b006806 | furniture | pages [23] -->
m

<!-- b006807 | furniture | pages [23] -->
m

<!-- b006808 | furniture | pages [23] -->
m

<!-- b006809 | furniture | pages [23] -->
m

<!-- b006810 | furniture | pages [23] -->
m

<!-- b006811 | furniture | pages [23] -->
m

<!-- b006812 | furniture | pages [23] -->
m

<!-- b006813 | furniture | pages [23] -->
m

<!-- b006814 | furniture | pages [23] -->
m

<!-- b006815 | furniture | pages [23] -->
m

<!-- b006816 | furniture | pages [23] -->
m

<!-- b006817 | furniture | pages [23] -->
m

<!-- b006818 | furniture | pages [23] -->
m

<!-- b006819 | furniture | pages [23] -->
m

<!-- b006820 | furniture | pages [23] -->
m

<!-- b006821 | furniture | pages [23] -->
m

<!-- b006822 | furniture | pages [23] -->
m

<!-- b006823 | furniture | pages [23] -->
m

<!-- b006824 | furniture | pages [23] -->
m

<!-- b006825 | furniture | pages [23] -->
m

<!-- b006826 | furniture | pages [23] -->
m

<!-- b006827 | furniture | pages [23] -->
m

<!-- b006828 | furniture | pages [23] -->
m

<!-- b006829 | furniture | pages [23] -->
m

<!-- b006830 | furniture | pages [23] -->
m

<!-- b006831 | furniture | pages [23] -->
m

<!-- b006832 | furniture | pages [23] -->
m

<!-- b006833 | furniture | pages [23] -->
m

<!-- b006834 | furniture | pages [23] -->
m

<!-- b006835 | furniture | pages [23] -->
m

<!-- b006836 | furniture | pages [23] -->
m

<!-- b006837 | furniture | pages [23] -->
m

<!-- b006838 | furniture | pages [23] -->
m

<!-- b006839 | furniture | pages [23] -->
m

<!-- b006840 | furniture | pages [23] -->
m

<!-- b006841 | furniture | pages [23] -->
m

<!-- b006842 | furniture | pages [23] -->
m

<!-- b006843 | furniture | pages [23] -->
m

<!-- b006844 | furniture | pages [23] -->
m

<!-- b006845 | furniture | pages [23] -->
m

<!-- b006846 | furniture | pages [23] -->
m

<!-- b006847 | furniture | pages [23] -->
m

<!-- b006848 | furniture | pages [23] -->
m

<!-- b006849 | furniture | pages [23] -->
m

<!-- b006850 | furniture | pages [23] -->
m

<!-- b006851 | furniture | pages [23] -->
m

<!-- b006852 | furniture | pages [23] -->
m

<!-- b006853 | furniture | pages [23] -->
m

<!-- b006854 | furniture | pages [23] -->
m

<!-- b006855 | furniture | pages [24] -->
Team#2507817                                                             Page 24 of 25

<!-- b006856 | prose | pages [24] -->
following a change in the indicator.

<!-- b006857 | heading | pages [24] -->
10.2 Impact of Athletes Number, Gold & Total Medals on Predicted Results

<!-- b006858 | prose | pages [24] -->
In Task 1, we found that there are many eigenvalues that affect the prediction of the number of gold medals & medals. We control the other eigenvalues unchanged, respectively A , the total number of events change the athletes_num ij E , observe the corresponding ij

<!-- b006859 | prose | pages [24] -->
changes in the predicted number of medals won, and get the average sensitivity: athletes_num: 0.058329%; Total event: -1.2113%.

<!-- b006860 | furniture | pages [24] -->


<!-- b006861 | prose | pages [24] -->
a) Total event

<!-- b006862 | furniture | pages [24] -->


<!-- b006863 | furniture | pages [24] -->


<!-- b006864 | furniture | pages [24] -->


<!-- b006865 | furniture | pages [24] -->


<!-- b006866 | furniture | pages [24] -->


<!-- b006867 | prose | pages [24] -->
b) Athletes number

<!-- b006868 | caption | pages [24] -->
Figure 23 Sentivity analysis

<!-- b006869 | prose | pages [24] -->
From the figure, it is found that the model basically does not fluctuate much after being perturbed, and the average sensitivity is also very low. It shows that our model has strong stability and robustness.

<!-- b006870 | heading | pages [24] -->
11 Evaluation of Model

<!-- b006871 | heading | pages [24] -->
(1) Strengths

<!-- b006872 | prose | pages [24] -->
 GSRF uses an optimal combination of hyperparameters on top of the traditional

<!-- b006873 | prose | pages [24] -->
stochastic model to train and predict the model. It significantly improves the performance of the model and effectively mitigates problems such as overfitting or underfitting

<!-- b006874 | prose | pages [24] -->
 Both the MAE and RMSE of the GSRF model are smaller, proving that the model is

<!-- b006875 | prose | pages [24] -->
more accurate and predicts more credible results

<!-- b006876 | prose | pages [24] -->
 The binary logistic regression model has a larger F1 metric, which ensures that the

<!-- b006877 | prose | pages [24] -->
recall is also high while guaranteeing higher accuracy and better classification.

<!-- b006878 | prose | pages [24] -->
 By changing the eigenvalues of the model, it is found that the model basically does

<!-- b006879 | prose | pages [24] -->
not fluctuate too much after being perturbed, indicating that the model has strong stability and robustness.

<!-- b006880 | prose | pages [24] -->
(2) Possible Improvements

<!-- b006881 | prose | pages [24] -->
 It is assumed that the number of athletes, countries and sports at the 2028 Olympics

<!-- b006882 | prose | pages [24] -->
will be the same as in 2024, but the actual situation may change, which will affect the model's predictions.

<!-- b006883 | prose | pages [24] -->
 There may be interactions between variables, for example, there may be a positive

<!-- b006884 | prose | pages [24] -->
correlation between the number of athletes and the number of programs, which can lead to biased model predictions.

<!-- b006885 | furniture | pages [24] -->


<!-- b006886 | prose | pages [24] -->
关注数学模型

<!-- b006887 | furniture | pages [24] -->
2

<!-- b006888 | furniture | pages [24] -->
MATHmodels

<!-- b006889 | furniture | pages [24] -->
获取更多资讯

<!-- b006890 | furniture | pages [25] -->
Team#2507817                                                             Page 25 of 25

<!-- b006891 | heading | pages [25] -->
12 References

<!-- b006892 | references | pages [25] -->
[1] Christoph S ,L. S S ,Dominik S , et al. Forecasting the Olympic medal distribution - A

<!-- b006893 | references | pages [25] -->
socioeconomic machine learning model[J]. Technological Forecasting &amp; Social

<!-- b006894 | references | pages [25] -->
Change,2022,175

<!-- b006895 | references | pages [25] -->
[2] Tan Kaifeng, Zhang Qingyi. Analysis of World Sports Competition Pattern and China's

<!-- b006896 | references | pages [25] -->
微信公众号：数学模型

<!-- b006897 | references | pages [25] -->
Athletic

<!-- b006898 | references | pages [25] -->
Level

<!-- b006899 | references | pages [25] -->
in

<!-- b006900 | references | pages [25] -->
Paris

<!-- b006901 | references | pages [25] -->
Olympics

<!-- b006902 | references | pages [25] -->
[J].

<!-- b006903 | references | pages [25] -->
Liaoning

<!-- b006904 | references | pages [25] -->
Sports

<!-- b006905 | references | pages [25] -->
Science

<!-- b006906 | references | pages [25] -->
and

<!-- b006907 | references | pages [25] -->
Technology,2025,47(01):56-62.DOI:10.13940/j.cnki.lntykj.2025.01.023.

<!-- b006908 | references | pages [25] -->
[3] Coaching

<!-- b006909 | references | pages [25] -->
Team

<!-- b006910 | references | pages [25] -->
-

<!-- b006911 | references | pages [25] -->
Bela

<!-- b006912 | references | pages [25] -->
and

<!-- b006913 | references | pages [25] -->
Martha

<!-- b006914 | references | pages [25] -->
Karolyi,

<!-- b006915 | references | pages [25] -->
USA

<!-- b006916 | references | pages [25] -->
Gymnastic,

<!-- b006917 | references | pages [25] -->
https://usagym.org/halloffame/inductee/coaching-team-bela-martha- karolyi/

<!-- b006918 | references | pages [25] -->
[4] [Nov 16, 2024] Bela Karolyi, famed yet polarizing U.S. gymnastics coach, dies, ESPN

<!-- b006919 | references | pages [25] -->
News Services, https://www.espn.com/olympics/gymnastics/story /_/id/42433795/bela-

<!-- b006920 | references | pages [25] -->
karolyi-famed-us-gymnastics-coach-dies-82

<!-- b006921 | references | pages [25] -->
微信号：MATHmodels

<!-- b006922 | furniture | pages [25] -->

