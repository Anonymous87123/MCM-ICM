# P-C-2025-2517690-93ab5dac

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2025

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | furniture | pages [1] -->
2517690

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | prose | pages [1] -->
Who will dominate the 2028 Olympic Games?

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
Predicting Olympic medal counts is a hot topic in the sports world. Based on the data of previous Olympic Games, we constructed a Random Forest regression model for predicting the number of medals in future Olympic Games, offering a new approach to medal prediction.

<!-- b000013 | prose | pages [1] -->
In the first part of Problem 1, we constructed a medal prediction model by considering factors such as the level of athletes, the number and types of events, and the identity of the host

<!-- b000014 | heading | pages [1] -->
country. Through ten-fold cross-validation, we compared Random Forest Regression, Lasso

<!-- b000015 | title | pages [1] -->
微信公众号：数学模型

<!-- b000016 | prose | pages [1] -->
Regression, XGBoost Regression and Neural Network Regression models respectively, and evaluated model performance using metrics such as R2 and MSE. The results show that the Random Forest Regression model performed best with an R²of 0.92 on the test set. Based on the predictions from this model, the three countries with the highest total medal counts at the

<!-- b000017 | heading | pages [1] -->
2028 Los Angeles Olympics are projected to be the United States, China, and the United

<!-- b000018 | prose | pages [1] -->
Kingdom. Compared to previous Olympic Games, the United States is expected to see a 10% increase in the number of gold medals, while Japan is predicted to experience a 5% decrease in its gold medal count.

<!-- b000019 | prose | pages [1] -->
In the second part of Problem 1, for countries that have never won a medal, we constructed

<!-- b000020 | title | pages [1] -->
微信号：MATHmodels

<!-- b000021 | prose | pages [1] -->
the Logistic Regression Model to predict their probability of winning, and the results show that four countries may win for the first time, with Angola's probability of winning for the first time being 0.81, making it the most likely to win for the first time. Subsequently, we explored the correlation between the events and the total number of medals by the Gray Cor- relation Analysis Model and found that there is a significant correlation between some of the events and the medal performance of specific countries.

<!-- b000022 | prose | pages [1] -->
For Problem 2, in order to explore the impact of the “great coach” effect on medal out- comes, we conducted the Two-sample mean hypothesis testing and the Chi-square test to examine the influence of great coaches on Olympic medal performance. The Logistic Regres- sion Model was also applied to quantify the coach effect. The results show that the impact lies between athlete skill and the number of participants. Based on the results of the model analysis, we suggest that the United States, China and Japan should focus on investing in sports with great coaches.

<!-- b000023 | prose | pages [1] -->
For Problem 3, we explored the impact of host advantage on Olympic medal potential from a game-theoretic perspective. By utilizing the N-player Game Theory and analyzing the Nash Equilibrium, we revealed the interplay of medal distributions across countries and fur- ther elucidated the key role of host advantage in Olympic medal prediction.

<!-- b000024 | prose | pages [1] -->
Finally, we performed error evaluation and sensitivity analysis of the Cross-validation folds, verified the higher prediction accuracy and model robustness.

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | keywords | pages [1] -->
Keywords: Olympics ; medal prediction ; Machine Learning ;“great coach” effect

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [3] -->
Team 2517690

<!-- b000029 | furniture | pages [3] -->


<!-- b000030 | furniture | pages [3] -->


<!-- b000031 | furniture | pages [3] -->


<!-- b000032 | furniture | pages [3] -->


<!-- b000033 | furniture | pages [3] -->


<!-- b000034 | furniture | pages [3] -->


<!-- b000035 | furniture | pages [3] -->


<!-- b000036 | heading | pages [3] -->
1 Introduction

<!-- b000037 | heading | pages [3] -->
1.1 Problem Background

<!-- b000038 | furniture | pages [3] -->


<!-- b000039 | furniture | pages [3] -->


<!-- b000040 | furniture | pages [3] -->


<!-- b000041 | furniture | pages [3] -->


<!-- b000042 | furniture | pages [3] -->


<!-- b000043 | furniture | pages [3] -->


<!-- b000044 | furniture | pages [3] -->


<!-- b000045 | furniture | pages [3] -->
Page 3 of 25

<!-- b000046 | prose | pages [3] -->
The Olympic medal table measures countries' sporting prowess and informs their preparations for the Games. In the 2024 Paris Olympics, the United States, China, France, and the United Kingdom ex- celled, with the U.S. leading with 126 medals and China tying for the most golds. Several countries, in- cluding Albania, Cape Verde, Dominica, and St. Lu-

<!-- b000047 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000048 | prose | pages [3] -->
cia, won medals for the first time, highlighting global competitiveness. However, over 60 countries still haven't won an Olympic medal, showing disparities in the global distribution of sports resources.

<!-- b000049 | caption | pages [3] -->
Figure 1: Paris 2024 Olympic Games

<!-- b000050 | prose | pages [3] -->
Predicting the number of Olympic medals has always been an important research problem, and traditional methods mostly rely on historical medal data. However, with the advance an- nouncement of athlete lists and program settings, medal prediction based on more data and factors is gradually becoming a trend. By taking into account the strength of athletes, the types of events and other key factors, medal prediction can not only provide decision support for

<!-- b000051 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000052 | prose | pages [3] -->
national Olympic committees but also help event organizations and related departments to op- timize the allocation of resources.

<!-- b000053 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000054 | prose | pages [3] -->
Based on the given data, we specifically address the following questions: Question1: Build a model using the given data to predict the number of gold medals and total medals for each country. Evaluate the model's uncertainty, accuracy, and performance.

<!-- b000055 | prose | pages [3] -->
⚫ Based on the model, predict the medal standings for the 2028 Los Angeles Summer Olympics. Provide prediction intervals for all results and analyze which countries may show improvement and which countries may decline in performance. ⚫ Estimate the number of countries that have not won a medal yet, and predict the like- lihood of these countries winning their first medal in the next Olympic Games. ⚫ Explore the relationship between the number and type of Olympic events and medal counts, and analyze how different sports matter to countries and how the host coun- try's event selection affects competition results. Question2: Analyze the impact of the "Great coach" Effect on medal counts, estimate its contribution, and recommend sports for three countries to invest in great coaches, along with the expected impact.

<!-- b000056 | heading | pages [3] -->
Question3: Present the novel insights revealed by the model regarding Olympic medal

<!-- b000057 | prose | pages [3] -->
counts and explain how these insights can serve as valuable reference information for national Olympic committees.

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

<!-- b000182 | prose | pages [3] -->
m

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

<!-- b000225 | furniture | pages [3] -->


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

<!-- b000337 | prose | pages [3] -->
m

<!-- b000338 | prose | pages [3] -->
m

<!-- b000339 | prose | pages [3] -->
m

<!-- b000340 | prose | pages [3] -->
m

<!-- b000341 | prose | pages [3] -->
m

<!-- b000342 | prose | pages [3] -->
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

<!-- b000740 | furniture | pages [3] -->
m

<!-- b000741 | furniture | pages [3] -->
m

<!-- b000742 | furniture | pages [3] -->
m

<!-- b000743 | furniture | pages [3] -->
m

<!-- b000744 | furniture | pages [3] -->
m

<!-- b000745 | furniture | pages [3] -->
m

<!-- b000746 | furniture | pages [5] -->
Team 2517690

<!-- b000747 | furniture | pages [5] -->


<!-- b000748 | furniture | pages [5] -->


<!-- b000749 | furniture | pages [5] -->


<!-- b000750 | furniture | pages [5] -->


<!-- b000751 | furniture | pages [5] -->


<!-- b000752 | furniture | pages [5] -->


<!-- b000753 | furniture | pages [5] -->


<!-- b000754 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000755 | furniture | pages [5] -->


<!-- b000756 | furniture | pages [5] -->


<!-- b000757 | furniture | pages [5] -->


<!-- b000758 | furniture | pages [5] -->


<!-- b000759 | furniture | pages [5] -->


<!-- b000760 | furniture | pages [5] -->


<!-- b000761 | furniture | pages [5] -->


<!-- b000762 | furniture | pages [5] -->
Page 5 of 25

<!-- b000763 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000764 | prose | pages [5] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified. Additional, more specific assumptions will be introduced as needed to refine our models. ⚫ Assumption 1: There will be no changes to the list of sports announced for the 2028 Los

<!-- b000765 | prose | pages [5] -->
Angeles Olympics. Justification: This assumption means that we assume that all new or existing Olympic sports will not undergo any changes before the 2028 Los Angeles Olympics, i.e. no new sports will be added and no existing sports will be deleted or canceled. This assumption helps us to simplify the model and to focus on existing data and known changes to the Olympic sports.

<!-- b000766 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000767 | heading | pages [5] -->
⚫ Assumption 2: New projects will have less impact on non-winning countries

<!-- b000768 | prose | pages [5] -->
Justification: We assume that for countries that have not yet won an Olympic medal, the addition of new sport will not immediately change their chances of winning a medal. These countries may be able to compete for medals in some of the new sports, but given their overall strength and athlete pool, the impact of the new sports is expected to be small, especially in the short term. ⚫ Assumption 3: Assuming that the level of sports in each country remains stable.

<!-- b000769 | prose | pages [5] -->
Justification: This assumption means that we assume that there will be no significant changes in the level of athletes ( including skill, fitness, athleticism, etc. ) in the different Olympic sports in each country. ⚫ Assumption 4: U.S will be competitive with home-field advantage in additional events at

<!-- b000770 | prose | pages [5] -->
the 2028 Los Angeles Olympics. Justification: With this assumption, we believe that the United States may be in a more favorable position than other countries to compete for medals in the five additional Olym- pic sports, especially since it has a clear competitive advantage in terms of technological accumulation and resource investment.

<!-- b000771 | heading | pages [5] -->
3 Notations

<!-- b000772 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000773 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000774 | heading | pages [5] -->
Symbol

<!-- b000775 | furniture | pages [5] -->


<!-- b000776 | prose | pages [5] -->
Description Number of gold medals won in the j-th event of the i-th sport

<!-- b000777 | furniture | pages [5] -->


<!-- b000778 | prose | pages [5] -->
Number of silver medals won in the j-th event of the i-th sport

<!-- b000779 | furniture | pages [5] -->


<!-- b000780 | prose | pages [5] -->
Number of bronze medals won in the j-th event of the i-th sport

<!-- b000781 | furniture | pages [5] -->


<!-- b000782 | prose | pages [5] -->
Non-medal participants in the j-th event of the ith sport

<!-- b000783 | furniture | pages [5] -->


<!-- b000784 | prose | pages [5] -->
Number of athletes who did not win a medal

<!-- b000785 | furniture | pages [5] -->


<!-- b000786 | prose | pages [5] -->
Number of participation in the programme

<!-- b000787 | furniture | pages [5] -->


<!-- b000788 | prose | pages [5] -->
Number of sessions of participation

<!-- b000789 | furniture | pages [5] -->


<!-- b000790 | prose | pages [5] -->
Number of hours of great coaching in the sport

<!-- b000791 | furniture | pages [5] -->


<!-- b000792 | prose | pages [5] -->
Historical medal count

<!-- b000793 | furniture | pages [5] -->


<!-- b000794 | prose | pages [5] -->
Number of participating athletes

<!-- b000795 | furniture | pages [5] -->


<!-- b000796 | furniture | pages [6] -->
Team 2517690

<!-- b000797 | furniture | pages [6] -->


<!-- b000798 | furniture | pages [6] -->


<!-- b000799 | furniture | pages [6] -->


<!-- b000800 | furniture | pages [6] -->


<!-- b000801 | furniture | pages [6] -->


<!-- b000802 | furniture | pages [6] -->


<!-- b000803 | furniture | pages [6] -->


<!-- b000804 | furniture | pages [6] -->


<!-- b000805 | furniture | pages [6] -->


<!-- b000806 | furniture | pages [6] -->


<!-- b000807 | furniture | pages [6] -->


<!-- b000808 | furniture | pages [6] -->


<!-- b000809 | furniture | pages [6] -->


<!-- b000810 | furniture | pages [6] -->


<!-- b000811 | furniture | pages [6] -->
Page 6 of 25

<!-- b000812 | heading | pages [6] -->
4 Data Pre-processing and Visual Analytics

<!-- b000813 | heading | pages [6] -->
4.1 Data Pre-processing

<!-- b000814 | prose | pages [6] -->
Analyzing the given data reveals redundancy and scatter, so we first perform outlier re- moval, data complementation, integration, and collection to prepare for model construction later in the paper.

<!-- b000815 | prose | pages [6] -->
◆ Outlier Handling The 1906 data in the summerOly_athletes attachment pertains to the unofficial Olympic Games and should be removed as outliers. Additionally, data from several Olympic Games affected by international situations and other factors will be deleted to prevent negative impact on the model.

<!-- b000816 | prose | pages [6] -->
◆ Data Completion The summerOly_programs annex contains some missing data. After review, the missing values are filled in to ensure completeness and avoid affecting subsequent analysis.

<!-- b000817 | prose | pages [6] -->
◆ Data Consolidation （1）Text Data Processing

<!-- b000818 | prose | pages [6] -->
Gold medals are coded as 1, silver as 2, bronze as 3, and no medals as 0. The host country for each year is labeled as 1, while all others are labeled as 0.

<!-- b000819 | prose | pages [6] -->
（2）Data Aggregation

<!-- b000820 | prose | pages [6] -->
Data aggregation is performed based on country, event, and year, with the following ag- gregation rules:

<!-- b000821 | prose | pages [6] -->
①Each event is categorized by sport, and the number of gold, silver, and bronze medals, as well as the number of participants, are calculated.

<!-- b000822 | prose | pages [6] -->
②If an event is missing in a certain year, all countries will have a value of 0 for that event. （3）Data Encoding

<!-- b000823 | prose | pages [6] -->
Countries are sorted in ascending order by name, and each country is assigned a numerical code starting from 1 to replace the country name.

<!-- b000824 | prose | pages [6] -->
（4）Standardization of region names

<!-- b000825 | prose | pages [6] -->
In the annex 'summerOly_medal_counts', add a column with the Olympic Games country abbreviation in the NOC column to facilitate subsequent modeling.

<!-- b000826 | heading | pages [6] -->
◆ Data Collection

<!-- b000827 | prose | pages [6] -->
Given that the total number of medals depends entirely on the events included in the Sum- mer Olympics and that countries specialize in different sports, it is crucial to know the events scheduled for the 2028 Games. Relevant event details have been compiled and recorded in the annex 'summerOly_programs' for unified processing. Below are the data sources：

<!-- b000828 | caption | pages [6] -->
Table 2:Data source website

<!-- b000829 | prose | pages [6] -->
Database Names 2028 Olympic sports Database Websites Data https://la28.org/ Countries participating in the 2028 Olympic Games International Coach Council https://www.olympics.com/en/ https://coachfederation.org/ Entertainment Sports Programming Network

<!-- b000830 | furniture | pages [6] -->


<!-- b000831 | prose | pages [6] -->
https://www.espn.com/

<!-- b000832 | prose | pages [6] -->
关注数学模型

<!-- b000833 | furniture | pages [6] -->
2

<!-- b000834 | furniture | pages [6] -->
MATHmodels

<!-- b000835 | furniture | pages [6] -->
获取更多资讯

<!-- b000836 | furniture | pages [7] -->
Team 2517690

<!-- b000837 | furniture | pages [7] -->


<!-- b000838 | furniture | pages [7] -->


<!-- b000839 | furniture | pages [7] -->


<!-- b000840 | furniture | pages [7] -->


<!-- b000841 | furniture | pages [7] -->


<!-- b000842 | furniture | pages [7] -->


<!-- b000843 | furniture | pages [7] -->


<!-- b000844 | heading | pages [7] -->
4.2 Visual Analytics

<!-- b000845 | furniture | pages [7] -->


<!-- b000846 | furniture | pages [7] -->


<!-- b000847 | furniture | pages [7] -->


<!-- b000848 | furniture | pages [7] -->


<!-- b000849 | furniture | pages [7] -->


<!-- b000850 | furniture | pages [7] -->


<!-- b000851 | furniture | pages [7] -->


<!-- b000852 | furniture | pages [7] -->
Page 7 of 25

<!-- b000853 | prose | pages [7] -->
This section presents a visual analysis of Olympic medal counts through statistical charts, offering insights into the distribution of medals across countries and highlighting their compet- itive strengths over time and in different sports.

<!-- b000854 | prose | pages [7] -->
◆ Number of medals by country Analyze the data and draw the following statistical graphs：

<!-- b000855 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000856 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000857 | furniture | pages [7] -->


<!-- b000858 | caption | pages [7] -->
Figure 3: Number of medals by country

<!-- b000859 | prose | pages [7] -->
Analysis of the graph reveals that the United States leads in both gold medals (1,027) and total medals (2,583), demonstrating its strong competitiveness. The USSR and China rank sec- ond and third with 352 and 303 gold medals, respectively, though China surpasses the USSR in total medals (727 vs. 907). Countries like Great Britain, France, and Germany show more balanced performances, with Great Britain achieving 292 gold medals and 944 total medals. In conclusion, the United States remains dominant in Olympic performance, while other nations show varying strengths in gold and total medal counts.

<!-- b000860 | prose | pages [7] -->
◆ Time series chart of the number of medals in each event Under normal circumstances, the number of medals won by each country should follow a stable trend, either gradually increasing or decreasing, with no abrupt fluctuations. This is due to each country's unique geographical position and specialization in specific events, with per- formance trends accumulating over time. Taking the United States as an example, the medal count for each edition of the Games and the four disciplines where it performed most promi- nently were selected and analyzed, as shown in the chart below:

<!-- b000861 | prose | pages [7] -->
m

<!-- b000862 | prose | pages [7] -->
m

<!-- b000863 | prose | pages [7] -->
m

<!-- b000864 | prose | pages [7] -->
m

<!-- b000865 | prose | pages [7] -->
m

<!-- b000866 | prose | pages [7] -->
m

<!-- b000867 | prose | pages [7] -->
m

<!-- b000868 | prose | pages [7] -->
m

<!-- b000869 | prose | pages [7] -->
m

<!-- b000870 | prose | pages [7] -->
m

<!-- b000871 | prose | pages [7] -->
m

<!-- b000872 | prose | pages [7] -->
m

<!-- b000873 | prose | pages [7] -->
m

<!-- b000874 | prose | pages [7] -->
m

<!-- b000875 | prose | pages [7] -->
m

<!-- b000876 | prose | pages [7] -->
m

<!-- b000877 | prose | pages [7] -->
m

<!-- b000878 | prose | pages [7] -->
m

<!-- b000879 | prose | pages [7] -->
m

<!-- b000880 | prose | pages [7] -->
m

<!-- b000881 | prose | pages [7] -->
m

<!-- b000882 | prose | pages [7] -->
m

<!-- b000883 | prose | pages [7] -->
m

<!-- b000884 | prose | pages [7] -->
m

<!-- b000885 | prose | pages [7] -->
m

<!-- b000886 | prose | pages [7] -->
m

<!-- b000887 | prose | pages [7] -->
m

<!-- b000888 | prose | pages [7] -->
m

<!-- b000889 | prose | pages [7] -->
m

<!-- b000890 | prose | pages [7] -->
m

<!-- b000891 | prose | pages [7] -->
m

<!-- b000892 | prose | pages [7] -->
m

<!-- b000893 | prose | pages [7] -->
m

<!-- b000894 | prose | pages [7] -->
m

<!-- b000895 | prose | pages [7] -->
m

<!-- b000896 | prose | pages [7] -->
m

<!-- b000897 | prose | pages [7] -->
m

<!-- b000898 | prose | pages [7] -->
m

<!-- b000899 | prose | pages [7] -->
m

<!-- b000900 | prose | pages [7] -->
m

<!-- b000901 | prose | pages [7] -->
m

<!-- b000902 | prose | pages [7] -->
m

<!-- b000903 | prose | pages [7] -->
m

<!-- b000904 | prose | pages [7] -->
m

<!-- b000905 | prose | pages [7] -->
m

<!-- b000906 | prose | pages [7] -->
m

<!-- b000907 | prose | pages [7] -->
m

<!-- b000908 | prose | pages [7] -->
m

<!-- b000909 | prose | pages [7] -->
m

<!-- b000910 | prose | pages [7] -->
m

<!-- b000911 | prose | pages [7] -->
m

<!-- b000912 | prose | pages [7] -->
m

<!-- b000913 | prose | pages [7] -->
m

<!-- b000914 | prose | pages [7] -->
m

<!-- b000915 | prose | pages [7] -->
m

<!-- b000916 | prose | pages [7] -->
m

<!-- b000917 | prose | pages [7] -->
m

<!-- b000918 | prose | pages [7] -->
m

<!-- b000919 | prose | pages [7] -->
m

<!-- b000920 | prose | pages [7] -->
m

<!-- b000921 | prose | pages [7] -->
m

<!-- b000922 | prose | pages [7] -->
m

<!-- b000923 | prose | pages [7] -->
m

<!-- b000924 | prose | pages [7] -->
m

<!-- b000925 | prose | pages [7] -->
m

<!-- b000926 | prose | pages [7] -->
m

<!-- b000927 | prose | pages [7] -->
m

<!-- b000928 | prose | pages [7] -->
m

<!-- b000929 | prose | pages [7] -->
m

<!-- b000930 | prose | pages [7] -->
m

<!-- b000931 | prose | pages [7] -->
m

<!-- b000932 | prose | pages [7] -->
m

<!-- b000933 | prose | pages [7] -->
m

<!-- b000934 | prose | pages [7] -->
m

<!-- b000935 | prose | pages [7] -->
m

<!-- b000936 | prose | pages [7] -->
m

<!-- b000937 | prose | pages [7] -->
m

<!-- b000938 | prose | pages [7] -->
m

<!-- b000939 | prose | pages [7] -->
m

<!-- b000940 | prose | pages [7] -->
m

<!-- b000941 | prose | pages [7] -->
m

<!-- b000942 | prose | pages [7] -->
m

<!-- b000943 | prose | pages [7] -->
m

<!-- b000944 | prose | pages [7] -->
m

<!-- b000945 | prose | pages [7] -->
m

<!-- b000946 | prose | pages [7] -->
m

<!-- b000947 | prose | pages [7] -->
m

<!-- b000948 | prose | pages [7] -->
m

<!-- b000949 | prose | pages [7] -->
m

<!-- b000950 | prose | pages [7] -->
m

<!-- b000951 | prose | pages [7] -->
m

<!-- b000952 | prose | pages [7] -->
m

<!-- b000953 | prose | pages [7] -->
m

<!-- b000954 | prose | pages [7] -->
m

<!-- b000955 | prose | pages [7] -->
m

<!-- b000956 | prose | pages [7] -->
m

<!-- b000957 | prose | pages [7] -->
m

<!-- b000958 | prose | pages [7] -->
m

<!-- b000959 | prose | pages [7] -->
m

<!-- b000960 | prose | pages [7] -->
m

<!-- b000961 | prose | pages [7] -->
m

<!-- b000962 | prose | pages [7] -->
m

<!-- b000963 | prose | pages [7] -->
m

<!-- b000964 | prose | pages [7] -->
m

<!-- b000965 | prose | pages [7] -->
m

<!-- b000966 | prose | pages [7] -->
m

<!-- b000967 | prose | pages [7] -->
m

<!-- b000968 | prose | pages [7] -->
m

<!-- b000969 | prose | pages [7] -->
m

<!-- b000970 | prose | pages [7] -->
m

<!-- b000971 | prose | pages [7] -->
m

<!-- b000972 | prose | pages [7] -->
m

<!-- b000973 | prose | pages [7] -->
m

<!-- b000974 | prose | pages [7] -->
m

<!-- b000975 | prose | pages [7] -->
m

<!-- b000976 | prose | pages [7] -->
m

<!-- b000977 | prose | pages [7] -->
m

<!-- b000978 | prose | pages [7] -->
m

<!-- b000979 | prose | pages [7] -->
m

<!-- b000980 | prose | pages [7] -->
m

<!-- b000981 | prose | pages [7] -->
m

<!-- b000982 | prose | pages [7] -->
m

<!-- b000983 | prose | pages [7] -->
m

<!-- b000984 | prose | pages [7] -->
m

<!-- b000985 | prose | pages [7] -->
m

<!-- b000986 | prose | pages [7] -->
m

<!-- b000987 | prose | pages [7] -->
m

<!-- b000988 | prose | pages [7] -->
m

<!-- b000989 | prose | pages [7] -->
m

<!-- b000990 | prose | pages [7] -->
m

<!-- b000991 | prose | pages [7] -->
m

<!-- b000992 | prose | pages [7] -->
m

<!-- b000993 | prose | pages [7] -->
m

<!-- b000994 | prose | pages [7] -->
m

<!-- b000995 | prose | pages [7] -->
m

<!-- b000996 | prose | pages [7] -->
m

<!-- b000997 | prose | pages [7] -->
m

<!-- b000998 | prose | pages [7] -->
m

<!-- b000999 | prose | pages [7] -->
m

<!-- b001000 | prose | pages [7] -->
m

<!-- b001001 | prose | pages [7] -->
m

<!-- b001002 | prose | pages [7] -->
m

<!-- b001003 | prose | pages [7] -->
m

<!-- b001004 | prose | pages [7] -->
m

<!-- b001005 | prose | pages [7] -->
m

<!-- b001006 | prose | pages [7] -->
m

<!-- b001007 | prose | pages [7] -->
m

<!-- b001008 | prose | pages [7] -->
m

<!-- b001009 | prose | pages [7] -->
m

<!-- b001010 | prose | pages [7] -->
m

<!-- b001011 | prose | pages [7] -->
m

<!-- b001012 | prose | pages [7] -->
m

<!-- b001013 | prose | pages [7] -->
m

<!-- b001014 | prose | pages [7] -->
m

<!-- b001015 | prose | pages [7] -->
m

<!-- b001016 | prose | pages [7] -->
m

<!-- b001017 | prose | pages [7] -->
m

<!-- b001018 | prose | pages [7] -->
m

<!-- b001019 | prose | pages [7] -->
m

<!-- b001020 | prose | pages [7] -->
m

<!-- b001021 | prose | pages [7] -->
m

<!-- b001022 | prose | pages [7] -->
m

<!-- b001023 | prose | pages [7] -->
m

<!-- b001024 | prose | pages [7] -->
m

<!-- b001025 | prose | pages [7] -->
m

<!-- b001026 | prose | pages [7] -->
m

<!-- b001027 | prose | pages [7] -->
m

<!-- b001028 | furniture | pages [7] -->


<!-- b001029 | prose | pages [7] -->
m

<!-- b001030 | prose | pages [7] -->
m

<!-- b001031 | prose | pages [7] -->
m

<!-- b001032 | prose | pages [7] -->
m

<!-- b001033 | prose | pages [7] -->
m

<!-- b001034 | prose | pages [7] -->
m

<!-- b001035 | prose | pages [7] -->
m

<!-- b001036 | prose | pages [7] -->
m

<!-- b001037 | prose | pages [7] -->
m

<!-- b001038 | prose | pages [7] -->
m

<!-- b001039 | prose | pages [7] -->
m

<!-- b001040 | prose | pages [7] -->
m

<!-- b001041 | prose | pages [7] -->
m

<!-- b001042 | prose | pages [7] -->
m

<!-- b001043 | prose | pages [7] -->
m

<!-- b001044 | prose | pages [7] -->
m

<!-- b001045 | prose | pages [7] -->
m

<!-- b001046 | prose | pages [7] -->
m

<!-- b001047 | prose | pages [7] -->
m

<!-- b001048 | prose | pages [7] -->
m

<!-- b001049 | prose | pages [7] -->
m

<!-- b001050 | prose | pages [7] -->
m

<!-- b001051 | prose | pages [7] -->
m

<!-- b001052 | prose | pages [7] -->
m

<!-- b001053 | prose | pages [7] -->
m

<!-- b001054 | prose | pages [7] -->
m

<!-- b001055 | prose | pages [7] -->
m

<!-- b001056 | prose | pages [7] -->
m

<!-- b001057 | prose | pages [7] -->
m

<!-- b001058 | prose | pages [7] -->
m

<!-- b001059 | prose | pages [7] -->
m

<!-- b001060 | prose | pages [7] -->
m

<!-- b001061 | prose | pages [7] -->
m

<!-- b001062 | prose | pages [7] -->
m

<!-- b001063 | prose | pages [7] -->
m

<!-- b001064 | prose | pages [7] -->
m

<!-- b001065 | prose | pages [7] -->
m

<!-- b001066 | prose | pages [7] -->
m

<!-- b001067 | prose | pages [7] -->
m

<!-- b001068 | prose | pages [7] -->
m

<!-- b001069 | prose | pages [7] -->
m

<!-- b001070 | prose | pages [7] -->
m

<!-- b001071 | prose | pages [7] -->
m

<!-- b001072 | prose | pages [7] -->
m

<!-- b001073 | prose | pages [7] -->
m

<!-- b001074 | prose | pages [7] -->
m

<!-- b001075 | prose | pages [7] -->
m

<!-- b001076 | prose | pages [7] -->
m

<!-- b001077 | prose | pages [7] -->
m

<!-- b001078 | prose | pages [7] -->
m

<!-- b001079 | prose | pages [7] -->
m

<!-- b001080 | prose | pages [7] -->
m

<!-- b001081 | prose | pages [7] -->
m

<!-- b001082 | prose | pages [7] -->
m

<!-- b001083 | prose | pages [7] -->
m

<!-- b001084 | prose | pages [7] -->
m

<!-- b001085 | prose | pages [7] -->
m

<!-- b001086 | prose | pages [7] -->
m

<!-- b001087 | prose | pages [7] -->
m

<!-- b001088 | prose | pages [7] -->
m

<!-- b001089 | prose | pages [7] -->
m

<!-- b001090 | prose | pages [7] -->
m

<!-- b001091 | prose | pages [7] -->
m

<!-- b001092 | prose | pages [7] -->
m

<!-- b001093 | prose | pages [7] -->
m

<!-- b001094 | prose | pages [7] -->
m

<!-- b001095 | prose | pages [7] -->
m

<!-- b001096 | prose | pages [7] -->
m

<!-- b001097 | prose | pages [7] -->
m

<!-- b001098 | prose | pages [7] -->
m

<!-- b001099 | prose | pages [7] -->
m

<!-- b001100 | prose | pages [7] -->
m

<!-- b001101 | prose | pages [7] -->
m

<!-- b001102 | prose | pages [7] -->
m

<!-- b001103 | prose | pages [7] -->
m

<!-- b001104 | prose | pages [7] -->
m

<!-- b001105 | prose | pages [7] -->
m

<!-- b001106 | prose | pages [7] -->
m

<!-- b001107 | prose | pages [7] -->
m

<!-- b001108 | prose | pages [7] -->
m

<!-- b001109 | prose | pages [7] -->
m

<!-- b001110 | prose | pages [7] -->
m

<!-- b001111 | prose | pages [7] -->
m

<!-- b001112 | prose | pages [7] -->
m

<!-- b001113 | prose | pages [7] -->
m

<!-- b001114 | prose | pages [7] -->
m

<!-- b001115 | prose | pages [7] -->
m

<!-- b001116 | prose | pages [7] -->
m

<!-- b001117 | prose | pages [7] -->
m

<!-- b001118 | prose | pages [7] -->
m

<!-- b001119 | prose | pages [7] -->
m

<!-- b001120 | prose | pages [7] -->
m

<!-- b001121 | prose | pages [7] -->
m

<!-- b001122 | prose | pages [7] -->
m

<!-- b001123 | prose | pages [7] -->
m

<!-- b001124 | prose | pages [7] -->
m

<!-- b001125 | prose | pages [7] -->
m

<!-- b001126 | prose | pages [7] -->
m

<!-- b001127 | prose | pages [7] -->
m

<!-- b001128 | prose | pages [7] -->
m

<!-- b001129 | prose | pages [7] -->
m

<!-- b001130 | prose | pages [7] -->
m

<!-- b001131 | prose | pages [7] -->
m

<!-- b001132 | prose | pages [7] -->
m

<!-- b001133 | prose | pages [7] -->
m

<!-- b001134 | prose | pages [7] -->
m

<!-- b001135 | prose | pages [7] -->
m

<!-- b001136 | prose | pages [7] -->
m

<!-- b001137 | prose | pages [7] -->
m

<!-- b001138 | prose | pages [7] -->
m

<!-- b001139 | prose | pages [7] -->
m

<!-- b001140 | prose | pages [7] -->
m

<!-- b001141 | prose | pages [7] -->
m

<!-- b001142 | prose | pages [7] -->
m

<!-- b001143 | prose | pages [7] -->
m

<!-- b001144 | prose | pages [7] -->
m

<!-- b001145 | prose | pages [7] -->
m

<!-- b001146 | furniture | pages [7] -->
m

<!-- b001147 | furniture | pages [7] -->
m

<!-- b001148 | furniture | pages [7] -->
m

<!-- b001149 | furniture | pages [7] -->
m

<!-- b001150 | furniture | pages [7] -->
m

<!-- b001151 | furniture | pages [7] -->
m

<!-- b001152 | furniture | pages [7] -->
m

<!-- b001153 | furniture | pages [7] -->
m

<!-- b001154 | furniture | pages [7] -->
m

<!-- b001155 | furniture | pages [7] -->
m

<!-- b001156 | furniture | pages [7] -->
m

<!-- b001157 | furniture | pages [7] -->
m

<!-- b001158 | furniture | pages [7] -->
m

<!-- b001159 | furniture | pages [7] -->
m

<!-- b001160 | furniture | pages [7] -->
m

<!-- b001161 | furniture | pages [7] -->
m

<!-- b001162 | furniture | pages [7] -->
m

<!-- b001163 | furniture | pages [7] -->
m

<!-- b001164 | furniture | pages [7] -->
m

<!-- b001165 | furniture | pages [7] -->
m

<!-- b001166 | furniture | pages [7] -->
m

<!-- b001167 | furniture | pages [7] -->
m

<!-- b001168 | furniture | pages [7] -->
m

<!-- b001169 | furniture | pages [7] -->
m

<!-- b001170 | furniture | pages [7] -->
m

<!-- b001171 | furniture | pages [7] -->
m

<!-- b001172 | furniture | pages [7] -->
m

<!-- b001173 | furniture | pages [7] -->
m

<!-- b001174 | furniture | pages [7] -->
m

<!-- b001175 | furniture | pages [7] -->
m

<!-- b001176 | furniture | pages [7] -->
m

<!-- b001177 | furniture | pages [7] -->
m

<!-- b001178 | furniture | pages [7] -->
m

<!-- b001179 | furniture | pages [7] -->
m

<!-- b001180 | furniture | pages [7] -->
m

<!-- b001181 | furniture | pages [7] -->
m

<!-- b001182 | furniture | pages [7] -->
m

<!-- b001183 | furniture | pages [7] -->
m

<!-- b001184 | furniture | pages [7] -->
m

<!-- b001185 | furniture | pages [7] -->
m

<!-- b001186 | furniture | pages [7] -->
m

<!-- b001187 | furniture | pages [7] -->
m

<!-- b001188 | furniture | pages [7] -->
m

<!-- b001189 | furniture | pages [7] -->
m

<!-- b001190 | furniture | pages [7] -->
m

<!-- b001191 | furniture | pages [7] -->
m

<!-- b001192 | furniture | pages [7] -->
m

<!-- b001193 | furniture | pages [7] -->
m

<!-- b001194 | furniture | pages [7] -->
m

<!-- b001195 | furniture | pages [7] -->
m

<!-- b001196 | furniture | pages [7] -->
m

<!-- b001197 | furniture | pages [7] -->
m

<!-- b001198 | furniture | pages [7] -->
m

<!-- b001199 | furniture | pages [7] -->
m

<!-- b001200 | furniture | pages [7] -->
m

<!-- b001201 | furniture | pages [7] -->
m

<!-- b001202 | furniture | pages [7] -->
m

<!-- b001203 | furniture | pages [7] -->
m

<!-- b001204 | furniture | pages [7] -->
m

<!-- b001205 | furniture | pages [7] -->
m

<!-- b001206 | furniture | pages [7] -->
m

<!-- b001207 | furniture | pages [7] -->
m

<!-- b001208 | furniture | pages [7] -->
m

<!-- b001209 | furniture | pages [7] -->
m

<!-- b001210 | furniture | pages [7] -->
m

<!-- b001211 | furniture | pages [7] -->
m

<!-- b001212 | furniture | pages [7] -->
m

<!-- b001213 | furniture | pages [7] -->
m

<!-- b001214 | furniture | pages [7] -->
m

<!-- b001215 | furniture | pages [7] -->
m

<!-- b001216 | furniture | pages [7] -->
m

<!-- b001217 | furniture | pages [7] -->
m

<!-- b001218 | furniture | pages [7] -->
m

<!-- b001219 | furniture | pages [7] -->
m

<!-- b001220 | furniture | pages [7] -->
m

<!-- b001221 | furniture | pages [7] -->
m

<!-- b001222 | furniture | pages [7] -->
m

<!-- b001223 | furniture | pages [7] -->
m

<!-- b001224 | furniture | pages [7] -->
m

<!-- b001225 | furniture | pages [7] -->
m

<!-- b001226 | furniture | pages [7] -->
m

<!-- b001227 | furniture | pages [7] -->
m

<!-- b001228 | furniture | pages [7] -->
m

<!-- b001229 | furniture | pages [7] -->
m

<!-- b001230 | furniture | pages [7] -->
m

<!-- b001231 | furniture | pages [7] -->
m

<!-- b001232 | furniture | pages [7] -->
m

<!-- b001233 | furniture | pages [7] -->
m

<!-- b001234 | furniture | pages [7] -->
m

<!-- b001235 | furniture | pages [7] -->
m

<!-- b001236 | furniture | pages [7] -->
m

<!-- b001237 | furniture | pages [7] -->
m

<!-- b001238 | furniture | pages [7] -->
m

<!-- b001239 | furniture | pages [7] -->
m

<!-- b001240 | furniture | pages [7] -->
m

<!-- b001241 | furniture | pages [7] -->
m

<!-- b001242 | furniture | pages [7] -->
m

<!-- b001243 | furniture | pages [7] -->
m

<!-- b001244 | furniture | pages [7] -->
m

<!-- b001245 | furniture | pages [7] -->
m

<!-- b001246 | furniture | pages [7] -->
m

<!-- b001247 | furniture | pages [7] -->
m

<!-- b001248 | furniture | pages [7] -->
m

<!-- b001249 | furniture | pages [7] -->
m

<!-- b001250 | furniture | pages [7] -->
m

<!-- b001251 | furniture | pages [7] -->
m

<!-- b001252 | furniture | pages [7] -->
m

<!-- b001253 | furniture | pages [7] -->
m

<!-- b001254 | furniture | pages [7] -->
m

<!-- b001255 | furniture | pages [7] -->
m

<!-- b001256 | furniture | pages [7] -->
m

<!-- b001257 | furniture | pages [7] -->
m

<!-- b001258 | furniture | pages [7] -->
m

<!-- b001259 | furniture | pages [7] -->
m

<!-- b001260 | furniture | pages [7] -->
m

<!-- b001261 | furniture | pages [7] -->
m

<!-- b001262 | furniture | pages [7] -->
m

<!-- b001263 | furniture | pages [7] -->
m

<!-- b001264 | furniture | pages [7] -->
m

<!-- b001265 | furniture | pages [7] -->
m

<!-- b001266 | furniture | pages [7] -->
m

<!-- b001267 | furniture | pages [7] -->
m

<!-- b001268 | furniture | pages [7] -->
m

<!-- b001269 | furniture | pages [7] -->
m

<!-- b001270 | furniture | pages [7] -->
m

<!-- b001271 | furniture | pages [7] -->
m

<!-- b001272 | furniture | pages [7] -->
m

<!-- b001273 | furniture | pages [7] -->
m

<!-- b001274 | furniture | pages [7] -->
m

<!-- b001275 | furniture | pages [7] -->
m

<!-- b001276 | furniture | pages [7] -->
m

<!-- b001277 | furniture | pages [7] -->
m

<!-- b001278 | furniture | pages [7] -->
m

<!-- b001279 | furniture | pages [7] -->
m

<!-- b001280 | furniture | pages [7] -->
m

<!-- b001281 | furniture | pages [7] -->
m

<!-- b001282 | furniture | pages [7] -->
m

<!-- b001283 | furniture | pages [7] -->
m

<!-- b001284 | furniture | pages [7] -->
m

<!-- b001285 | furniture | pages [7] -->
m

<!-- b001286 | furniture | pages [7] -->
m

<!-- b001287 | furniture | pages [7] -->
m

<!-- b001288 | furniture | pages [7] -->
m

<!-- b001289 | furniture | pages [7] -->
m

<!-- b001290 | furniture | pages [7] -->
m

<!-- b001291 | furniture | pages [7] -->
m

<!-- b001292 | furniture | pages [7] -->
m

<!-- b001293 | furniture | pages [7] -->
m

<!-- b001294 | furniture | pages [7] -->
m

<!-- b001295 | furniture | pages [7] -->
m

<!-- b001296 | furniture | pages [7] -->
m

<!-- b001297 | furniture | pages [7] -->
m

<!-- b001298 | furniture | pages [7] -->
m

<!-- b001299 | furniture | pages [7] -->
m

<!-- b001300 | furniture | pages [7] -->
m

<!-- b001301 | furniture | pages [7] -->
m

<!-- b001302 | furniture | pages [7] -->
m

<!-- b001303 | furniture | pages [7] -->
m

<!-- b001304 | furniture | pages [7] -->
m

<!-- b001305 | furniture | pages [7] -->
m

<!-- b001306 | furniture | pages [7] -->
m

<!-- b001307 | furniture | pages [7] -->
m

<!-- b001308 | furniture | pages [7] -->
m

<!-- b001309 | furniture | pages [7] -->
m

<!-- b001310 | furniture | pages [7] -->
m

<!-- b001311 | furniture | pages [7] -->
m

<!-- b001312 | furniture | pages [7] -->
m

<!-- b001313 | furniture | pages [7] -->
m

<!-- b001314 | furniture | pages [7] -->
m

<!-- b001315 | furniture | pages [7] -->
m

<!-- b001316 | furniture | pages [7] -->
m

<!-- b001317 | furniture | pages [7] -->
m

<!-- b001318 | furniture | pages [7] -->
m

<!-- b001319 | furniture | pages [7] -->
m

<!-- b001320 | furniture | pages [7] -->
m

<!-- b001321 | furniture | pages [7] -->
m

<!-- b001322 | furniture | pages [7] -->
m

<!-- b001323 | furniture | pages [7] -->
m

<!-- b001324 | furniture | pages [7] -->
m

<!-- b001325 | furniture | pages [7] -->
m

<!-- b001326 | furniture | pages [7] -->
m

<!-- b001327 | furniture | pages [7] -->
m

<!-- b001328 | furniture | pages [7] -->
m

<!-- b001329 | furniture | pages [7] -->
m

<!-- b001330 | furniture | pages [7] -->
m

<!-- b001331 | furniture | pages [7] -->
m

<!-- b001332 | furniture | pages [7] -->
m

<!-- b001333 | furniture | pages [7] -->
m

<!-- b001334 | furniture | pages [7] -->
m

<!-- b001335 | furniture | pages [7] -->
m

<!-- b001336 | furniture | pages [7] -->
m

<!-- b001337 | furniture | pages [7] -->
m

<!-- b001338 | furniture | pages [7] -->
m

<!-- b001339 | furniture | pages [7] -->
m

<!-- b001340 | furniture | pages [7] -->
m

<!-- b001341 | furniture | pages [7] -->
m

<!-- b001342 | furniture | pages [7] -->
m

<!-- b001343 | furniture | pages [7] -->
m

<!-- b001344 | furniture | pages [7] -->
m

<!-- b001345 | furniture | pages [7] -->
m

<!-- b001346 | furniture | pages [7] -->
m

<!-- b001347 | furniture | pages [7] -->
m

<!-- b001348 | furniture | pages [7] -->
m

<!-- b001349 | furniture | pages [7] -->
m

<!-- b001350 | furniture | pages [7] -->
m

<!-- b001351 | furniture | pages [7] -->
m

<!-- b001352 | furniture | pages [7] -->
m

<!-- b001353 | furniture | pages [7] -->
m

<!-- b001354 | furniture | pages [7] -->
m

<!-- b001355 | furniture | pages [7] -->
m

<!-- b001356 | furniture | pages [7] -->
m

<!-- b001357 | furniture | pages [7] -->
m

<!-- b001358 | furniture | pages [7] -->
m

<!-- b001359 | furniture | pages [7] -->
m

<!-- b001360 | furniture | pages [7] -->
m

<!-- b001361 | furniture | pages [7] -->
m

<!-- b001362 | furniture | pages [7] -->
m

<!-- b001363 | furniture | pages [7] -->
m

<!-- b001364 | furniture | pages [7] -->
m

<!-- b001365 | furniture | pages [7] -->
m

<!-- b001366 | furniture | pages [7] -->
m

<!-- b001367 | furniture | pages [7] -->
m

<!-- b001368 | furniture | pages [7] -->
m

<!-- b001369 | furniture | pages [7] -->
m

<!-- b001370 | furniture | pages [7] -->
m

<!-- b001371 | furniture | pages [7] -->
m

<!-- b001372 | furniture | pages [7] -->
m

<!-- b001373 | furniture | pages [7] -->
m

<!-- b001374 | furniture | pages [7] -->
m

<!-- b001375 | furniture | pages [7] -->
m

<!-- b001376 | furniture | pages [7] -->
m

<!-- b001377 | furniture | pages [7] -->
m

<!-- b001378 | furniture | pages [7] -->
m

<!-- b001379 | furniture | pages [7] -->
m

<!-- b001380 | furniture | pages [7] -->
m

<!-- b001381 | furniture | pages [7] -->
m

<!-- b001382 | furniture | pages [7] -->
m

<!-- b001383 | furniture | pages [7] -->
m

<!-- b001384 | furniture | pages [7] -->
m

<!-- b001385 | furniture | pages [7] -->
m

<!-- b001386 | furniture | pages [7] -->
m

<!-- b001387 | furniture | pages [7] -->
m

<!-- b001388 | furniture | pages [7] -->
m

<!-- b001389 | furniture | pages [7] -->
m

<!-- b001390 | furniture | pages [7] -->
m

<!-- b001391 | furniture | pages [7] -->
m

<!-- b001392 | furniture | pages [7] -->
m

<!-- b001393 | furniture | pages [7] -->
m

<!-- b001394 | furniture | pages [7] -->
m

<!-- b001395 | furniture | pages [7] -->
m

<!-- b001396 | furniture | pages [7] -->
m

<!-- b001397 | furniture | pages [7] -->
m

<!-- b001398 | furniture | pages [7] -->
m

<!-- b001399 | furniture | pages [7] -->
m

<!-- b001400 | furniture | pages [7] -->
m

<!-- b001401 | furniture | pages [7] -->
m

<!-- b001402 | furniture | pages [7] -->
m

<!-- b001403 | furniture | pages [7] -->
m

<!-- b001404 | furniture | pages [7] -->
m

<!-- b001405 | furniture | pages [7] -->
m

<!-- b001406 | furniture | pages [7] -->
m

<!-- b001407 | furniture | pages [7] -->
m

<!-- b001408 | furniture | pages [7] -->
m

<!-- b001409 | furniture | pages [7] -->
m

<!-- b001410 | furniture | pages [7] -->
m

<!-- b001411 | furniture | pages [7] -->
m

<!-- b001412 | furniture | pages [7] -->
m

<!-- b001413 | furniture | pages [7] -->
m

<!-- b001414 | furniture | pages [7] -->
m

<!-- b001415 | furniture | pages [7] -->
m

<!-- b001416 | furniture | pages [7] -->
m

<!-- b001417 | furniture | pages [7] -->
m

<!-- b001418 | furniture | pages [7] -->
m

<!-- b001419 | furniture | pages [7] -->
m

<!-- b001420 | furniture | pages [7] -->
m

<!-- b001421 | furniture | pages [7] -->
m

<!-- b001422 | furniture | pages [7] -->
m

<!-- b001423 | furniture | pages [7] -->
m

<!-- b001424 | furniture | pages [7] -->
m

<!-- b001425 | furniture | pages [7] -->
m

<!-- b001426 | furniture | pages [7] -->
m

<!-- b001427 | furniture | pages [7] -->
m

<!-- b001428 | furniture | pages [7] -->
m

<!-- b001429 | furniture | pages [7] -->
m

<!-- b001430 | furniture | pages [7] -->
m

<!-- b001431 | furniture | pages [7] -->
m

<!-- b001432 | furniture | pages [7] -->
m

<!-- b001433 | furniture | pages [7] -->
m

<!-- b001434 | furniture | pages [7] -->
m

<!-- b001435 | furniture | pages [7] -->
m

<!-- b001436 | furniture | pages [7] -->
m

<!-- b001437 | furniture | pages [7] -->
m

<!-- b001438 | furniture | pages [7] -->
m

<!-- b001439 | furniture | pages [7] -->
m

<!-- b001440 | furniture | pages [7] -->
m

<!-- b001441 | furniture | pages [7] -->
m

<!-- b001442 | furniture | pages [7] -->
m

<!-- b001443 | furniture | pages [7] -->
m

<!-- b001444 | furniture | pages [7] -->
m

<!-- b001445 | furniture | pages [7] -->
m

<!-- b001446 | furniture | pages [7] -->
m

<!-- b001447 | furniture | pages [7] -->
m

<!-- b001448 | furniture | pages [7] -->
m

<!-- b001449 | furniture | pages [7] -->
m

<!-- b001450 | furniture | pages [7] -->
m

<!-- b001451 | furniture | pages [7] -->
m

<!-- b001452 | furniture | pages [7] -->
m

<!-- b001453 | furniture | pages [7] -->
m

<!-- b001454 | furniture | pages [7] -->
m

<!-- b001455 | furniture | pages [7] -->
m

<!-- b001456 | furniture | pages [7] -->
m

<!-- b001457 | furniture | pages [7] -->
m

<!-- b001458 | furniture | pages [7] -->
m

<!-- b001459 | furniture | pages [7] -->
m

<!-- b001460 | furniture | pages [7] -->
m

<!-- b001461 | furniture | pages [7] -->
m

<!-- b001462 | furniture | pages [7] -->
m

<!-- b001463 | furniture | pages [7] -->
m

<!-- b001464 | furniture | pages [7] -->
m

<!-- b001465 | furniture | pages [7] -->
m

<!-- b001466 | furniture | pages [7] -->
m

<!-- b001467 | furniture | pages [7] -->
m

<!-- b001468 | furniture | pages [7] -->
m

<!-- b001469 | furniture | pages [7] -->
m

<!-- b001470 | furniture | pages [7] -->
m

<!-- b001471 | furniture | pages [7] -->
m

<!-- b001472 | furniture | pages [7] -->
m

<!-- b001473 | furniture | pages [7] -->
m

<!-- b001474 | furniture | pages [7] -->
m

<!-- b001475 | furniture | pages [7] -->
m

<!-- b001476 | furniture | pages [7] -->
m

<!-- b001477 | furniture | pages [7] -->
m

<!-- b001478 | furniture | pages [7] -->
m

<!-- b001479 | furniture | pages [7] -->
m

<!-- b001480 | furniture | pages [7] -->
m

<!-- b001481 | furniture | pages [7] -->
m

<!-- b001482 | furniture | pages [7] -->
m

<!-- b001483 | furniture | pages [7] -->
m

<!-- b001484 | furniture | pages [7] -->
m

<!-- b001485 | furniture | pages [7] -->
m

<!-- b001486 | furniture | pages [7] -->
m

<!-- b001487 | furniture | pages [7] -->
m

<!-- b001488 | furniture | pages [7] -->
m

<!-- b001489 | furniture | pages [7] -->
m

<!-- b001490 | furniture | pages [7] -->
m

<!-- b001491 | furniture | pages [7] -->
m

<!-- b001492 | furniture | pages [7] -->
m

<!-- b001493 | furniture | pages [7] -->
m

<!-- b001494 | furniture | pages [7] -->
m

<!-- b001495 | furniture | pages [7] -->
m

<!-- b001496 | furniture | pages [7] -->
m

<!-- b001497 | furniture | pages [7] -->
m

<!-- b001498 | furniture | pages [7] -->
m

<!-- b001499 | furniture | pages [7] -->
m

<!-- b001500 | furniture | pages [7] -->
m

<!-- b001501 | furniture | pages [7] -->
m

<!-- b001502 | furniture | pages [7] -->
m

<!-- b001503 | furniture | pages [7] -->
m

<!-- b001504 | furniture | pages [7] -->
m

<!-- b001505 | furniture | pages [7] -->
m

<!-- b001506 | furniture | pages [7] -->
m

<!-- b001507 | furniture | pages [7] -->
m

<!-- b001508 | furniture | pages [7] -->
m

<!-- b001509 | furniture | pages [7] -->
m

<!-- b001510 | furniture | pages [7] -->
m

<!-- b001511 | furniture | pages [7] -->
m

<!-- b001512 | furniture | pages [7] -->
m

<!-- b001513 | furniture | pages [7] -->
m

<!-- b001514 | furniture | pages [7] -->
m

<!-- b001515 | furniture | pages [7] -->
m

<!-- b001516 | furniture | pages [7] -->
m

<!-- b001517 | furniture | pages [7] -->
m

<!-- b001518 | furniture | pages [7] -->
m

<!-- b001519 | furniture | pages [7] -->
m

<!-- b001520 | furniture | pages [7] -->
m

<!-- b001521 | furniture | pages [7] -->
m

<!-- b001522 | furniture | pages [7] -->
m

<!-- b001523 | furniture | pages [7] -->
m

<!-- b001524 | furniture | pages [7] -->
m

<!-- b001525 | furniture | pages [7] -->
m

<!-- b001526 | furniture | pages [7] -->
m

<!-- b001527 | furniture | pages [7] -->
m

<!-- b001528 | furniture | pages [7] -->
m

<!-- b001529 | furniture | pages [7] -->
m

<!-- b001530 | furniture | pages [7] -->
m

<!-- b001531 | furniture | pages [7] -->
m

<!-- b001532 | furniture | pages [7] -->
m

<!-- b001533 | furniture | pages [7] -->
m

<!-- b001534 | furniture | pages [7] -->
m

<!-- b001535 | furniture | pages [7] -->
m

<!-- b001536 | furniture | pages [7] -->
m

<!-- b001537 | furniture | pages [7] -->
m

<!-- b001538 | furniture | pages [7] -->
m

<!-- b001539 | furniture | pages [7] -->
m

<!-- b001540 | furniture | pages [7] -->
m

<!-- b001541 | furniture | pages [7] -->
m

<!-- b001542 | furniture | pages [7] -->
m

<!-- b001543 | furniture | pages [7] -->
m

<!-- b001544 | furniture | pages [7] -->
m

<!-- b001545 | furniture | pages [7] -->
m

<!-- b001546 | furniture | pages [7] -->
m

<!-- b001547 | furniture | pages [7] -->
m

<!-- b001548 | furniture | pages [7] -->
m

<!-- b001549 | furniture | pages [8] -->
Team 2517690

<!-- b001550 | furniture | pages [8] -->


<!-- b001551 | furniture | pages [8] -->


<!-- b001552 | furniture | pages [8] -->


<!-- b001553 | furniture | pages [8] -->


<!-- b001554 | furniture | pages [8] -->


<!-- b001555 | furniture | pages [8] -->


<!-- b001556 | furniture | pages [8] -->


<!-- b001557 | furniture | pages [8] -->


<!-- b001558 | furniture | pages [8] -->


<!-- b001559 | furniture | pages [8] -->


<!-- b001560 | furniture | pages [8] -->


<!-- b001561 | furniture | pages [8] -->


<!-- b001562 | furniture | pages [8] -->


<!-- b001563 | furniture | pages [8] -->


<!-- b001564 | furniture | pages [8] -->
Page 8 of 25

<!-- b001565 | caption | pages [8] -->
Figure 4: The number of medals in each event       Figure 5:U.S. Medal Count

<!-- b001566 | caption | pages [8] -->
Figure 4 shows that the number of medals won by the United States fluctuated signifi-

<!-- b001567 | prose | pages [8] -->
cantly over the years. Notably, the U.S. reached peak medal counts in 1904 and 1984, likely due to its role as host. During both World Wars, U.S. medal counts declined, possibly reflecting the disruption caused by the wars. Since the 21st century, while fluctuations have occurred, the U.S. has maintained a generally high medal count.

<!-- b001568 | caption | pages [8] -->
Figure 5 highlights that swimming has been a traditional strength for the United States,

<!-- b001569 | prose | pages [8] -->
with high medal counts sustained over most years. Basketball, since its Olympic debut in 1936, has been another stable area of success, reflecting the U.S.'s continued dominance, particularly through professional leagues like the NBA, which has kept U.S. basketball at the forefront globally.

<!-- b001570 | heading | pages [8] -->
5 Olympic Medal Prediction Based on Machine Learning

<!-- b001571 | furniture | pages [8] -->


<!-- b001572 | caption | pages [8] -->
Figure 6: Flowchart of part 1 of question 1

<!-- b001573 | heading | pages [8] -->
5.1 Medal Table Prediction Model Based on Random Forest

<!-- b001574 | heading | pages [8] -->
5.1.1 Determination of Input Variables

<!-- b001575 | prose | pages [8] -->
⚫ The level of athletes in various sports: Different countries have significant advantages in certain Olympic events. Usually, this is because the athletes in these countries have undergone long-term training and possess high-level technical and tactical capabili- ties as well as excellent physical fitness. ⚫ The number and types of competition events: The number and types of events in each

<!-- b001576 | furniture | pages [8] -->


<!-- b001577 | prose | pages [8] -->
关注数学模型

<!-- b001578 | furniture | pages [8] -->
2

<!-- b001579 | furniture | pages [8] -->
MATHmodels

<!-- b001580 | furniture | pages [8] -->
获取更多资讯

<!-- b001581 | furniture | pages [9] -->
Team 2517690

<!-- b001582 | furniture | pages [9] -->


<!-- b001583 | furniture | pages [9] -->


<!-- b001584 | furniture | pages [9] -->


<!-- b001585 | furniture | pages [9] -->


<!-- b001586 | furniture | pages [9] -->


<!-- b001587 | furniture | pages [9] -->


<!-- b001588 | furniture | pages [9] -->


<!-- b001589 | furniture | pages [9] -->


<!-- b001590 | furniture | pages [9] -->


<!-- b001591 | furniture | pages [9] -->


<!-- b001592 | furniture | pages [9] -->


<!-- b001593 | furniture | pages [9] -->


<!-- b001594 | furniture | pages [9] -->


<!-- b001595 | furniture | pages [9] -->


<!-- b001596 | furniture | pages [9] -->
Page 9 of 25

<!-- b001597 | prose | pages [9] -->
Olympic Games affect a country's chances of winning medals. Some countries may have traditional advantages in the events that are added or removed from the Olym- pics, which will impact the number of medals they can obtain. ⚫ The impact of being the host country on medal performance: The host country usually has certain advantages in terms of psychology, resources, funding, and audience sup- port. This may enhance its performance in some events, and this is a typical 0 - 1 variable. ⚫ The number of athletes a country sends to the Olympics: Countries with a larger num- ber of participating athletes can usually compete in multiple events, thus increasing their chances of winning medals. More athletes mean more opportunities to perform

<!-- b001598 | prose | pages [9] -->
微信公众号：数学模型

<!-- b001599 | prose | pages [9] -->
and greater potential to increase the number of medals.

<!-- b001600 | heading | pages [9] -->
5.1.2 Comprehensive Strength Evaluation of Each Event

<!-- b001601 | prose | pages [9] -->
By analyzing the medal distribution of each event in the previous Olympic Games and the number of non-winning participants, a quantitative indicator was constructed to measure the comprehensive competitive strength of each country in that event. Based on the total number of historical medals of athletes, it is possible to effectively evaluate a country's performance and competitiveness in the event, providing a reliable reference for medal predictions in future Olympic Games.

<!-- b001602 | prose | pages [9] -->
微信号：MATHmodels

<!-- b001603 | prose | pages [9] -->
Step1: Determine variables be the number of gold medals won in the j-th event of the i-th sport, Let be the

<!-- b001604 | prose | pages [9] -->
number of silver medals won in the j-th event of the i-th sport, be the number of bronze medals won in the j-th event of the i-th sport, and Event of the i-th Sport

<!-- b001605 | prose | pages [9] -->
Step 2: Subjectively assign weights

<!-- b001606 | prose | pages [9] -->
be the non-medal participants in the j-th

<!-- b001607 | prose | pages [9] -->
Each indicator (such as the number of gold medals, silver medals, bronze medals, and the number of non-medalists) contributes differently to the comprehensive strength. Therefore, we assign the following weights:

<!-- b001608 | caption | pages [9] -->
Table 3:Weighting of award indicators

<!-- b001609 | furniture | pages [9] -->


<!-- b001610 | heading | pages [9] -->
Step3: Quantification of the comprehensive strength of each country in each event

<!-- b001611 | prose | pages [9] -->
Let the comprehensive strength of the i-th event of the m-th country be

<!-- b001612 | prose | pages [9] -->
be expressed as:

<!-- b001613 | prose | pages [9] -->
, which can

<!-- b001614 | furniture | pages [9] -->


<!-- b001615 | prose | pages [9] -->
(1)

<!-- b001616 | heading | pages [9] -->
5.1.3 Establishment of the National Medal Quantity Prediction Model

<!-- b001617 | prose | pages [9] -->
Predicting the number of Olympic medals is a complex regression problem that involves multiple factors. To accurately predict the number of medals for each country, choosing an

<!-- b001618 | prose | pages [9] -->
m

<!-- b001619 | prose | pages [9] -->
m

<!-- b001620 | prose | pages [9] -->
m

<!-- b001621 | prose | pages [9] -->
m

<!-- b001622 | prose | pages [9] -->
m

<!-- b001623 | prose | pages [9] -->
m

<!-- b001624 | prose | pages [9] -->
m

<!-- b001625 | prose | pages [9] -->
m

<!-- b001626 | prose | pages [9] -->
m

<!-- b001627 | prose | pages [9] -->
m

<!-- b001628 | prose | pages [9] -->
m

<!-- b001629 | prose | pages [9] -->
m

<!-- b001630 | prose | pages [9] -->
m

<!-- b001631 | prose | pages [9] -->
m

<!-- b001632 | prose | pages [9] -->
m

<!-- b001633 | prose | pages [9] -->
m

<!-- b001634 | prose | pages [9] -->
m

<!-- b001635 | prose | pages [9] -->
m

<!-- b001636 | prose | pages [9] -->
m

<!-- b001637 | prose | pages [9] -->
m

<!-- b001638 | prose | pages [9] -->
m

<!-- b001639 | prose | pages [9] -->
m

<!-- b001640 | prose | pages [9] -->
m

<!-- b001641 | prose | pages [9] -->
m

<!-- b001642 | prose | pages [9] -->
m

<!-- b001643 | prose | pages [9] -->
m

<!-- b001644 | prose | pages [9] -->
m

<!-- b001645 | prose | pages [9] -->
m

<!-- b001646 | prose | pages [9] -->
m

<!-- b001647 | prose | pages [9] -->
m

<!-- b001648 | prose | pages [9] -->
m

<!-- b001649 | prose | pages [9] -->
m

<!-- b001650 | prose | pages [9] -->
m

<!-- b001651 | prose | pages [9] -->
m

<!-- b001652 | prose | pages [9] -->
m

<!-- b001653 | prose | pages [9] -->
m

<!-- b001654 | prose | pages [9] -->
m

<!-- b001655 | prose | pages [9] -->
m

<!-- b001656 | prose | pages [9] -->
m

<!-- b001657 | prose | pages [9] -->
m

<!-- b001658 | prose | pages [9] -->
m

<!-- b001659 | prose | pages [9] -->
m

<!-- b001660 | prose | pages [9] -->
m

<!-- b001661 | prose | pages [9] -->
m

<!-- b001662 | prose | pages [9] -->
m

<!-- b001663 | prose | pages [9] -->
m

<!-- b001664 | prose | pages [9] -->
m

<!-- b001665 | prose | pages [9] -->
m

<!-- b001666 | prose | pages [9] -->
m

<!-- b001667 | prose | pages [9] -->
m

<!-- b001668 | prose | pages [9] -->
m

<!-- b001669 | prose | pages [9] -->
m

<!-- b001670 | prose | pages [9] -->
m

<!-- b001671 | prose | pages [9] -->
m

<!-- b001672 | prose | pages [9] -->
m

<!-- b001673 | prose | pages [9] -->
m

<!-- b001674 | prose | pages [9] -->
m

<!-- b001675 | prose | pages [9] -->
m

<!-- b001676 | prose | pages [9] -->
m

<!-- b001677 | prose | pages [9] -->
m

<!-- b001678 | prose | pages [9] -->
m

<!-- b001679 | prose | pages [9] -->
m

<!-- b001680 | prose | pages [9] -->
m

<!-- b001681 | prose | pages [9] -->
m

<!-- b001682 | prose | pages [9] -->
m

<!-- b001683 | prose | pages [9] -->
m

<!-- b001684 | prose | pages [9] -->
m

<!-- b001685 | prose | pages [9] -->
m

<!-- b001686 | prose | pages [9] -->
m

<!-- b001687 | prose | pages [9] -->
m

<!-- b001688 | prose | pages [9] -->
m

<!-- b001689 | prose | pages [9] -->
m

<!-- b001690 | prose | pages [9] -->
m

<!-- b001691 | prose | pages [9] -->
m

<!-- b001692 | prose | pages [9] -->
m

<!-- b001693 | prose | pages [9] -->
m

<!-- b001694 | prose | pages [9] -->
m

<!-- b001695 | prose | pages [9] -->
m

<!-- b001696 | prose | pages [9] -->
m

<!-- b001697 | prose | pages [9] -->
m

<!-- b001698 | prose | pages [9] -->
m

<!-- b001699 | prose | pages [9] -->
m

<!-- b001700 | prose | pages [9] -->
m

<!-- b001701 | prose | pages [9] -->
m

<!-- b001702 | prose | pages [9] -->
m

<!-- b001703 | prose | pages [9] -->
m

<!-- b001704 | prose | pages [9] -->
m

<!-- b001705 | prose | pages [9] -->
m

<!-- b001706 | prose | pages [9] -->
m

<!-- b001707 | prose | pages [9] -->
m

<!-- b001708 | prose | pages [9] -->
m

<!-- b001709 | prose | pages [9] -->
m

<!-- b001710 | prose | pages [9] -->
m

<!-- b001711 | prose | pages [9] -->
m

<!-- b001712 | prose | pages [9] -->
m

<!-- b001713 | prose | pages [9] -->
m

<!-- b001714 | prose | pages [9] -->
m

<!-- b001715 | prose | pages [9] -->
m

<!-- b001716 | prose | pages [9] -->
m

<!-- b001717 | prose | pages [9] -->
m

<!-- b001718 | prose | pages [9] -->
m

<!-- b001719 | prose | pages [9] -->
m

<!-- b001720 | prose | pages [9] -->
m

<!-- b001721 | prose | pages [9] -->
m

<!-- b001722 | prose | pages [9] -->
m

<!-- b001723 | prose | pages [9] -->
m

<!-- b001724 | prose | pages [9] -->
m

<!-- b001725 | prose | pages [9] -->
m

<!-- b001726 | prose | pages [9] -->
m

<!-- b001727 | prose | pages [9] -->
m

<!-- b001728 | prose | pages [9] -->
m

<!-- b001729 | prose | pages [9] -->
m

<!-- b001730 | prose | pages [9] -->
m

<!-- b001731 | prose | pages [9] -->
m

<!-- b001732 | prose | pages [9] -->
m

<!-- b001733 | prose | pages [9] -->
m

<!-- b001734 | prose | pages [9] -->
m

<!-- b001735 | prose | pages [9] -->
m

<!-- b001736 | prose | pages [9] -->
m

<!-- b001737 | prose | pages [9] -->
m

<!-- b001738 | prose | pages [9] -->
m

<!-- b001739 | prose | pages [9] -->
m

<!-- b001740 | prose | pages [9] -->
m

<!-- b001741 | prose | pages [9] -->
m

<!-- b001742 | prose | pages [9] -->
m

<!-- b001743 | prose | pages [9] -->
m

<!-- b001744 | prose | pages [9] -->
m

<!-- b001745 | prose | pages [9] -->
m

<!-- b001746 | prose | pages [9] -->
m

<!-- b001747 | prose | pages [9] -->
m

<!-- b001748 | prose | pages [9] -->
m

<!-- b001749 | prose | pages [9] -->
m

<!-- b001750 | prose | pages [9] -->
m

<!-- b001751 | prose | pages [9] -->
m

<!-- b001752 | prose | pages [9] -->
m

<!-- b001753 | prose | pages [9] -->
m

<!-- b001754 | prose | pages [9] -->
m

<!-- b001755 | prose | pages [9] -->
m

<!-- b001756 | prose | pages [9] -->
m

<!-- b001757 | prose | pages [9] -->
m

<!-- b001758 | prose | pages [9] -->
m

<!-- b001759 | prose | pages [9] -->
m

<!-- b001760 | prose | pages [9] -->
m

<!-- b001761 | prose | pages [9] -->
m

<!-- b001762 | prose | pages [9] -->
m

<!-- b001763 | prose | pages [9] -->
m

<!-- b001764 | prose | pages [9] -->
m

<!-- b001765 | prose | pages [9] -->
m

<!-- b001766 | prose | pages [9] -->
m

<!-- b001767 | prose | pages [9] -->
m

<!-- b001768 | prose | pages [9] -->
m

<!-- b001769 | prose | pages [9] -->
m

<!-- b001770 | prose | pages [9] -->
m

<!-- b001771 | prose | pages [9] -->
m

<!-- b001772 | prose | pages [9] -->
m

<!-- b001773 | prose | pages [9] -->
m

<!-- b001774 | prose | pages [9] -->
m

<!-- b001775 | prose | pages [9] -->
m

<!-- b001776 | prose | pages [9] -->
m

<!-- b001777 | prose | pages [9] -->
m

<!-- b001778 | prose | pages [9] -->
m

<!-- b001779 | prose | pages [9] -->
m

<!-- b001780 | prose | pages [9] -->
m

<!-- b001781 | prose | pages [9] -->
m

<!-- b001782 | prose | pages [9] -->
m

<!-- b001783 | prose | pages [9] -->
m

<!-- b001784 | prose | pages [9] -->
m

<!-- b001785 | furniture | pages [9] -->


<!-- b001786 | prose | pages [9] -->
m

<!-- b001787 | prose | pages [9] -->
m

<!-- b001788 | prose | pages [9] -->
m

<!-- b001789 | prose | pages [9] -->
m

<!-- b001790 | prose | pages [9] -->
m

<!-- b001791 | prose | pages [9] -->
m

<!-- b001792 | prose | pages [9] -->
m

<!-- b001793 | prose | pages [9] -->
m

<!-- b001794 | prose | pages [9] -->
m

<!-- b001795 | prose | pages [9] -->
m

<!-- b001796 | prose | pages [9] -->
m

<!-- b001797 | prose | pages [9] -->
m

<!-- b001798 | prose | pages [9] -->
m

<!-- b001799 | prose | pages [9] -->
m

<!-- b001800 | prose | pages [9] -->
m

<!-- b001801 | prose | pages [9] -->
m

<!-- b001802 | prose | pages [9] -->
m

<!-- b001803 | prose | pages [9] -->
m

<!-- b001804 | prose | pages [9] -->
m

<!-- b001805 | prose | pages [9] -->
m

<!-- b001806 | prose | pages [9] -->
m

<!-- b001807 | prose | pages [9] -->
m

<!-- b001808 | prose | pages [9] -->
m

<!-- b001809 | prose | pages [9] -->
m

<!-- b001810 | prose | pages [9] -->
m

<!-- b001811 | prose | pages [9] -->
m

<!-- b001812 | prose | pages [9] -->
m

<!-- b001813 | prose | pages [9] -->
m

<!-- b001814 | prose | pages [9] -->
m

<!-- b001815 | prose | pages [9] -->
m

<!-- b001816 | prose | pages [9] -->
m

<!-- b001817 | prose | pages [9] -->
m

<!-- b001818 | prose | pages [9] -->
m

<!-- b001819 | prose | pages [9] -->
m

<!-- b001820 | prose | pages [9] -->
m

<!-- b001821 | prose | pages [9] -->
m

<!-- b001822 | prose | pages [9] -->
m

<!-- b001823 | prose | pages [9] -->
m

<!-- b001824 | prose | pages [9] -->
m

<!-- b001825 | prose | pages [9] -->
m

<!-- b001826 | prose | pages [9] -->
m

<!-- b001827 | prose | pages [9] -->
m

<!-- b001828 | prose | pages [9] -->
m

<!-- b001829 | prose | pages [9] -->
m

<!-- b001830 | prose | pages [9] -->
m

<!-- b001831 | prose | pages [9] -->
m

<!-- b001832 | prose | pages [9] -->
m

<!-- b001833 | prose | pages [9] -->
m

<!-- b001834 | prose | pages [9] -->
m

<!-- b001835 | prose | pages [9] -->
m

<!-- b001836 | prose | pages [9] -->
m

<!-- b001837 | prose | pages [9] -->
m

<!-- b001838 | prose | pages [9] -->
m

<!-- b001839 | prose | pages [9] -->
m

<!-- b001840 | prose | pages [9] -->
m

<!-- b001841 | prose | pages [9] -->
m

<!-- b001842 | prose | pages [9] -->
m

<!-- b001843 | prose | pages [9] -->
m

<!-- b001844 | prose | pages [9] -->
m

<!-- b001845 | prose | pages [9] -->
m

<!-- b001846 | prose | pages [9] -->
m

<!-- b001847 | prose | pages [9] -->
m

<!-- b001848 | prose | pages [9] -->
m

<!-- b001849 | prose | pages [9] -->
m

<!-- b001850 | prose | pages [9] -->
m

<!-- b001851 | prose | pages [9] -->
m

<!-- b001852 | prose | pages [9] -->
m

<!-- b001853 | prose | pages [9] -->
m

<!-- b001854 | prose | pages [9] -->
m

<!-- b001855 | prose | pages [9] -->
m

<!-- b001856 | prose | pages [9] -->
m

<!-- b001857 | prose | pages [9] -->
m

<!-- b001858 | prose | pages [9] -->
m

<!-- b001859 | prose | pages [9] -->
m

<!-- b001860 | prose | pages [9] -->
m

<!-- b001861 | prose | pages [9] -->
m

<!-- b001862 | prose | pages [9] -->
m

<!-- b001863 | prose | pages [9] -->
m

<!-- b001864 | prose | pages [9] -->
m

<!-- b001865 | prose | pages [9] -->
m

<!-- b001866 | prose | pages [9] -->
m

<!-- b001867 | prose | pages [9] -->
m

<!-- b001868 | prose | pages [9] -->
m

<!-- b001869 | prose | pages [9] -->
m

<!-- b001870 | prose | pages [9] -->
m

<!-- b001871 | prose | pages [9] -->
m

<!-- b001872 | prose | pages [9] -->
m

<!-- b001873 | prose | pages [9] -->
m

<!-- b001874 | prose | pages [9] -->
m

<!-- b001875 | prose | pages [9] -->
m

<!-- b001876 | prose | pages [9] -->
m

<!-- b001877 | prose | pages [9] -->
m

<!-- b001878 | prose | pages [9] -->
m

<!-- b001879 | prose | pages [9] -->
m

<!-- b001880 | prose | pages [9] -->
m

<!-- b001881 | prose | pages [9] -->
m

<!-- b001882 | prose | pages [9] -->
m

<!-- b001883 | prose | pages [9] -->
m

<!-- b001884 | prose | pages [9] -->
m

<!-- b001885 | prose | pages [9] -->
m

<!-- b001886 | prose | pages [9] -->
m

<!-- b001887 | prose | pages [9] -->
m

<!-- b001888 | prose | pages [9] -->
m

<!-- b001889 | prose | pages [9] -->
m

<!-- b001890 | prose | pages [9] -->
m

<!-- b001891 | prose | pages [9] -->
m

<!-- b001892 | prose | pages [9] -->
m

<!-- b001893 | prose | pages [9] -->
m

<!-- b001894 | prose | pages [9] -->
m

<!-- b001895 | prose | pages [9] -->
m

<!-- b001896 | prose | pages [9] -->
m

<!-- b001897 | prose | pages [9] -->
m

<!-- b001898 | prose | pages [9] -->
m

<!-- b001899 | prose | pages [9] -->
m

<!-- b001900 | prose | pages [9] -->
m

<!-- b001901 | prose | pages [9] -->
m

<!-- b001902 | prose | pages [9] -->
m

<!-- b001903 | furniture | pages [9] -->
m

<!-- b001904 | furniture | pages [9] -->
m

<!-- b001905 | furniture | pages [9] -->
m

<!-- b001906 | furniture | pages [9] -->
m

<!-- b001907 | furniture | pages [9] -->
m

<!-- b001908 | furniture | pages [9] -->
m

<!-- b001909 | furniture | pages [9] -->
m

<!-- b001910 | furniture | pages [9] -->
m

<!-- b001911 | furniture | pages [9] -->
m

<!-- b001912 | furniture | pages [9] -->
m

<!-- b001913 | furniture | pages [9] -->
m

<!-- b001914 | furniture | pages [9] -->
m

<!-- b001915 | furniture | pages [9] -->
m

<!-- b001916 | furniture | pages [9] -->
m

<!-- b001917 | furniture | pages [9] -->
m

<!-- b001918 | furniture | pages [9] -->
m

<!-- b001919 | furniture | pages [9] -->
m

<!-- b001920 | furniture | pages [9] -->
m

<!-- b001921 | furniture | pages [9] -->
m

<!-- b001922 | furniture | pages [9] -->
m

<!-- b001923 | furniture | pages [9] -->
m

<!-- b001924 | furniture | pages [9] -->
m

<!-- b001925 | furniture | pages [9] -->
m

<!-- b001926 | furniture | pages [9] -->
m

<!-- b001927 | furniture | pages [9] -->
m

<!-- b001928 | furniture | pages [9] -->
m

<!-- b001929 | furniture | pages [9] -->
m

<!-- b001930 | furniture | pages [9] -->
m

<!-- b001931 | furniture | pages [9] -->
m

<!-- b001932 | furniture | pages [9] -->
m

<!-- b001933 | furniture | pages [9] -->
m

<!-- b001934 | furniture | pages [9] -->
m

<!-- b001935 | furniture | pages [9] -->
m

<!-- b001936 | furniture | pages [9] -->
m

<!-- b001937 | furniture | pages [9] -->
m

<!-- b001938 | furniture | pages [9] -->
m

<!-- b001939 | furniture | pages [9] -->
m

<!-- b001940 | furniture | pages [9] -->
m

<!-- b001941 | furniture | pages [9] -->
m

<!-- b001942 | furniture | pages [9] -->
m

<!-- b001943 | furniture | pages [9] -->
m

<!-- b001944 | furniture | pages [9] -->
m

<!-- b001945 | furniture | pages [9] -->
m

<!-- b001946 | furniture | pages [9] -->
m

<!-- b001947 | furniture | pages [9] -->
m

<!-- b001948 | furniture | pages [9] -->
m

<!-- b001949 | furniture | pages [9] -->
m

<!-- b001950 | furniture | pages [9] -->
m

<!-- b001951 | furniture | pages [9] -->
m

<!-- b001952 | furniture | pages [9] -->
m

<!-- b001953 | furniture | pages [9] -->
m

<!-- b001954 | furniture | pages [9] -->
m

<!-- b001955 | furniture | pages [9] -->
m

<!-- b001956 | furniture | pages [9] -->
m

<!-- b001957 | furniture | pages [9] -->
m

<!-- b001958 | furniture | pages [9] -->
m

<!-- b001959 | furniture | pages [9] -->
m

<!-- b001960 | furniture | pages [9] -->
m

<!-- b001961 | furniture | pages [9] -->
m

<!-- b001962 | furniture | pages [9] -->
m

<!-- b001963 | furniture | pages [9] -->
m

<!-- b001964 | furniture | pages [9] -->
m

<!-- b001965 | furniture | pages [9] -->
m

<!-- b001966 | furniture | pages [9] -->
m

<!-- b001967 | furniture | pages [9] -->
m

<!-- b001968 | furniture | pages [9] -->
m

<!-- b001969 | furniture | pages [9] -->
m

<!-- b001970 | furniture | pages [9] -->
m

<!-- b001971 | furniture | pages [9] -->
m

<!-- b001972 | furniture | pages [9] -->
m

<!-- b001973 | furniture | pages [9] -->
m

<!-- b001974 | furniture | pages [9] -->
m

<!-- b001975 | furniture | pages [9] -->
m

<!-- b001976 | furniture | pages [9] -->
m

<!-- b001977 | furniture | pages [9] -->
m

<!-- b001978 | furniture | pages [9] -->
m

<!-- b001979 | furniture | pages [9] -->
m

<!-- b001980 | furniture | pages [9] -->
m

<!-- b001981 | furniture | pages [9] -->
m

<!-- b001982 | furniture | pages [9] -->
m

<!-- b001983 | furniture | pages [9] -->
m

<!-- b001984 | furniture | pages [9] -->
m

<!-- b001985 | furniture | pages [9] -->
m

<!-- b001986 | furniture | pages [9] -->
m

<!-- b001987 | furniture | pages [9] -->
m

<!-- b001988 | furniture | pages [9] -->
m

<!-- b001989 | furniture | pages [9] -->
m

<!-- b001990 | furniture | pages [9] -->
m

<!-- b001991 | furniture | pages [9] -->
m

<!-- b001992 | furniture | pages [9] -->
m

<!-- b001993 | furniture | pages [9] -->
m

<!-- b001994 | furniture | pages [9] -->
m

<!-- b001995 | furniture | pages [9] -->
m

<!-- b001996 | furniture | pages [9] -->
m

<!-- b001997 | furniture | pages [9] -->
m

<!-- b001998 | furniture | pages [9] -->
m

<!-- b001999 | furniture | pages [9] -->
m

<!-- b002000 | furniture | pages [9] -->
m

<!-- b002001 | furniture | pages [9] -->
m

<!-- b002002 | furniture | pages [9] -->
m

<!-- b002003 | furniture | pages [9] -->
m

<!-- b002004 | furniture | pages [9] -->
m

<!-- b002005 | furniture | pages [9] -->
m

<!-- b002006 | furniture | pages [9] -->
m

<!-- b002007 | furniture | pages [9] -->
m

<!-- b002008 | furniture | pages [9] -->
m

<!-- b002009 | furniture | pages [9] -->
m

<!-- b002010 | furniture | pages [9] -->
m

<!-- b002011 | furniture | pages [9] -->
m

<!-- b002012 | furniture | pages [9] -->
m

<!-- b002013 | furniture | pages [9] -->
m

<!-- b002014 | furniture | pages [9] -->
m

<!-- b002015 | furniture | pages [9] -->
m

<!-- b002016 | furniture | pages [9] -->
m

<!-- b002017 | furniture | pages [9] -->
m

<!-- b002018 | furniture | pages [9] -->
m

<!-- b002019 | furniture | pages [9] -->
m

<!-- b002020 | furniture | pages [9] -->
m

<!-- b002021 | furniture | pages [9] -->
m

<!-- b002022 | furniture | pages [9] -->
m

<!-- b002023 | furniture | pages [9] -->
m

<!-- b002024 | furniture | pages [9] -->
m

<!-- b002025 | furniture | pages [9] -->
m

<!-- b002026 | furniture | pages [9] -->
m

<!-- b002027 | furniture | pages [9] -->
m

<!-- b002028 | furniture | pages [9] -->
m

<!-- b002029 | furniture | pages [9] -->
m

<!-- b002030 | furniture | pages [9] -->
m

<!-- b002031 | furniture | pages [9] -->
m

<!-- b002032 | furniture | pages [9] -->
m

<!-- b002033 | furniture | pages [9] -->
m

<!-- b002034 | furniture | pages [9] -->
m

<!-- b002035 | furniture | pages [9] -->
m

<!-- b002036 | furniture | pages [9] -->
m

<!-- b002037 | furniture | pages [9] -->
m

<!-- b002038 | furniture | pages [9] -->
m

<!-- b002039 | furniture | pages [9] -->
m

<!-- b002040 | furniture | pages [9] -->
m

<!-- b002041 | furniture | pages [9] -->
m

<!-- b002042 | furniture | pages [9] -->
m

<!-- b002043 | furniture | pages [9] -->
m

<!-- b002044 | furniture | pages [9] -->
m

<!-- b002045 | furniture | pages [9] -->
m

<!-- b002046 | furniture | pages [9] -->
m

<!-- b002047 | furniture | pages [9] -->
m

<!-- b002048 | furniture | pages [9] -->
m

<!-- b002049 | furniture | pages [9] -->
m

<!-- b002050 | furniture | pages [9] -->
m

<!-- b002051 | furniture | pages [9] -->
m

<!-- b002052 | furniture | pages [9] -->
m

<!-- b002053 | furniture | pages [9] -->
m

<!-- b002054 | furniture | pages [9] -->
m

<!-- b002055 | furniture | pages [9] -->
m

<!-- b002056 | furniture | pages [9] -->
m

<!-- b002057 | furniture | pages [9] -->
m

<!-- b002058 | furniture | pages [9] -->
m

<!-- b002059 | furniture | pages [9] -->
m

<!-- b002060 | furniture | pages [9] -->
m

<!-- b002061 | furniture | pages [9] -->
m

<!-- b002062 | furniture | pages [9] -->
m

<!-- b002063 | furniture | pages [9] -->
m

<!-- b002064 | furniture | pages [9] -->
m

<!-- b002065 | furniture | pages [9] -->
m

<!-- b002066 | furniture | pages [9] -->
m

<!-- b002067 | furniture | pages [9] -->
m

<!-- b002068 | furniture | pages [9] -->
m

<!-- b002069 | furniture | pages [9] -->
m

<!-- b002070 | furniture | pages [9] -->
m

<!-- b002071 | furniture | pages [9] -->
m

<!-- b002072 | furniture | pages [9] -->
m

<!-- b002073 | furniture | pages [9] -->
m

<!-- b002074 | furniture | pages [9] -->
m

<!-- b002075 | furniture | pages [9] -->
m

<!-- b002076 | furniture | pages [9] -->
m

<!-- b002077 | furniture | pages [9] -->
m

<!-- b002078 | furniture | pages [9] -->
m

<!-- b002079 | furniture | pages [9] -->
m

<!-- b002080 | furniture | pages [9] -->
m

<!-- b002081 | furniture | pages [9] -->
m

<!-- b002082 | furniture | pages [9] -->
m

<!-- b002083 | furniture | pages [9] -->
m

<!-- b002084 | furniture | pages [9] -->
m

<!-- b002085 | furniture | pages [9] -->
m

<!-- b002086 | furniture | pages [9] -->
m

<!-- b002087 | furniture | pages [9] -->
m

<!-- b002088 | furniture | pages [9] -->
m

<!-- b002089 | furniture | pages [9] -->
m

<!-- b002090 | furniture | pages [9] -->
m

<!-- b002091 | furniture | pages [9] -->
m

<!-- b002092 | furniture | pages [9] -->
m

<!-- b002093 | furniture | pages [9] -->
m

<!-- b002094 | furniture | pages [9] -->
m

<!-- b002095 | furniture | pages [9] -->
m

<!-- b002096 | furniture | pages [9] -->
m

<!-- b002097 | furniture | pages [9] -->
m

<!-- b002098 | furniture | pages [9] -->
m

<!-- b002099 | furniture | pages [9] -->
m

<!-- b002100 | furniture | pages [9] -->
m

<!-- b002101 | furniture | pages [9] -->
m

<!-- b002102 | furniture | pages [9] -->
m

<!-- b002103 | furniture | pages [9] -->
m

<!-- b002104 | furniture | pages [9] -->
m

<!-- b002105 | furniture | pages [9] -->
m

<!-- b002106 | furniture | pages [9] -->
m

<!-- b002107 | furniture | pages [9] -->
m

<!-- b002108 | furniture | pages [9] -->
m

<!-- b002109 | furniture | pages [9] -->
m

<!-- b002110 | furniture | pages [9] -->
m

<!-- b002111 | furniture | pages [9] -->
m

<!-- b002112 | furniture | pages [9] -->
m

<!-- b002113 | furniture | pages [9] -->
m

<!-- b002114 | furniture | pages [9] -->
m

<!-- b002115 | furniture | pages [9] -->
m

<!-- b002116 | furniture | pages [9] -->
m

<!-- b002117 | furniture | pages [9] -->
m

<!-- b002118 | furniture | pages [9] -->
m

<!-- b002119 | furniture | pages [9] -->
m

<!-- b002120 | furniture | pages [9] -->
m

<!-- b002121 | furniture | pages [9] -->
m

<!-- b002122 | furniture | pages [9] -->
m

<!-- b002123 | furniture | pages [9] -->
m

<!-- b002124 | furniture | pages [9] -->
m

<!-- b002125 | furniture | pages [9] -->
m

<!-- b002126 | furniture | pages [9] -->
m

<!-- b002127 | furniture | pages [9] -->
m

<!-- b002128 | furniture | pages [9] -->
m

<!-- b002129 | furniture | pages [9] -->
m

<!-- b002130 | furniture | pages [9] -->
m

<!-- b002131 | furniture | pages [9] -->
m

<!-- b002132 | furniture | pages [9] -->
m

<!-- b002133 | furniture | pages [9] -->
m

<!-- b002134 | furniture | pages [9] -->
m

<!-- b002135 | furniture | pages [9] -->
m

<!-- b002136 | furniture | pages [9] -->
m

<!-- b002137 | furniture | pages [9] -->
m

<!-- b002138 | furniture | pages [9] -->
m

<!-- b002139 | furniture | pages [9] -->
m

<!-- b002140 | furniture | pages [9] -->
m

<!-- b002141 | furniture | pages [9] -->
m

<!-- b002142 | furniture | pages [9] -->
m

<!-- b002143 | furniture | pages [9] -->
m

<!-- b002144 | furniture | pages [9] -->
m

<!-- b002145 | furniture | pages [9] -->
m

<!-- b002146 | furniture | pages [9] -->
m

<!-- b002147 | furniture | pages [9] -->
m

<!-- b002148 | furniture | pages [9] -->
m

<!-- b002149 | furniture | pages [9] -->
m

<!-- b002150 | furniture | pages [9] -->
m

<!-- b002151 | furniture | pages [9] -->
m

<!-- b002152 | furniture | pages [9] -->
m

<!-- b002153 | furniture | pages [9] -->
m

<!-- b002154 | furniture | pages [9] -->
m

<!-- b002155 | furniture | pages [9] -->
m

<!-- b002156 | furniture | pages [9] -->
m

<!-- b002157 | furniture | pages [9] -->
m

<!-- b002158 | furniture | pages [9] -->
m

<!-- b002159 | furniture | pages [9] -->
m

<!-- b002160 | furniture | pages [9] -->
m

<!-- b002161 | furniture | pages [9] -->
m

<!-- b002162 | furniture | pages [9] -->
m

<!-- b002163 | furniture | pages [9] -->
m

<!-- b002164 | furniture | pages [9] -->
m

<!-- b002165 | furniture | pages [9] -->
m

<!-- b002166 | furniture | pages [9] -->
m

<!-- b002167 | furniture | pages [9] -->
m

<!-- b002168 | furniture | pages [9] -->
m

<!-- b002169 | furniture | pages [9] -->
m

<!-- b002170 | furniture | pages [9] -->
m

<!-- b002171 | furniture | pages [9] -->
m

<!-- b002172 | furniture | pages [9] -->
m

<!-- b002173 | furniture | pages [9] -->
m

<!-- b002174 | furniture | pages [9] -->
m

<!-- b002175 | furniture | pages [9] -->
m

<!-- b002176 | furniture | pages [9] -->
m

<!-- b002177 | furniture | pages [9] -->
m

<!-- b002178 | furniture | pages [9] -->
m

<!-- b002179 | furniture | pages [9] -->
m

<!-- b002180 | furniture | pages [9] -->
m

<!-- b002181 | furniture | pages [9] -->
m

<!-- b002182 | furniture | pages [9] -->
m

<!-- b002183 | furniture | pages [9] -->
m

<!-- b002184 | furniture | pages [9] -->
m

<!-- b002185 | furniture | pages [9] -->
m

<!-- b002186 | furniture | pages [9] -->
m

<!-- b002187 | furniture | pages [9] -->
m

<!-- b002188 | furniture | pages [9] -->
m

<!-- b002189 | furniture | pages [9] -->
m

<!-- b002190 | furniture | pages [9] -->
m

<!-- b002191 | furniture | pages [9] -->
m

<!-- b002192 | furniture | pages [9] -->
m

<!-- b002193 | furniture | pages [9] -->
m

<!-- b002194 | furniture | pages [9] -->
m

<!-- b002195 | furniture | pages [9] -->
m

<!-- b002196 | furniture | pages [9] -->
m

<!-- b002197 | furniture | pages [9] -->
m

<!-- b002198 | furniture | pages [9] -->
m

<!-- b002199 | furniture | pages [9] -->
m

<!-- b002200 | furniture | pages [9] -->
m

<!-- b002201 | furniture | pages [9] -->
m

<!-- b002202 | furniture | pages [9] -->
m

<!-- b002203 | furniture | pages [9] -->
m

<!-- b002204 | furniture | pages [9] -->
m

<!-- b002205 | furniture | pages [9] -->
m

<!-- b002206 | furniture | pages [9] -->
m

<!-- b002207 | furniture | pages [9] -->
m

<!-- b002208 | furniture | pages [9] -->
m

<!-- b002209 | furniture | pages [9] -->
m

<!-- b002210 | furniture | pages [9] -->
m

<!-- b002211 | furniture | pages [9] -->
m

<!-- b002212 | furniture | pages [9] -->
m

<!-- b002213 | furniture | pages [9] -->
m

<!-- b002214 | furniture | pages [9] -->
m

<!-- b002215 | furniture | pages [9] -->
m

<!-- b002216 | furniture | pages [9] -->
m

<!-- b002217 | furniture | pages [9] -->
m

<!-- b002218 | furniture | pages [9] -->
m

<!-- b002219 | furniture | pages [9] -->
m

<!-- b002220 | furniture | pages [9] -->
m

<!-- b002221 | furniture | pages [9] -->
m

<!-- b002222 | furniture | pages [9] -->
m

<!-- b002223 | furniture | pages [9] -->
m

<!-- b002224 | furniture | pages [9] -->
m

<!-- b002225 | furniture | pages [9] -->
m

<!-- b002226 | furniture | pages [9] -->
m

<!-- b002227 | furniture | pages [9] -->
m

<!-- b002228 | furniture | pages [9] -->
m

<!-- b002229 | furniture | pages [9] -->
m

<!-- b002230 | furniture | pages [9] -->
m

<!-- b002231 | furniture | pages [9] -->
m

<!-- b002232 | furniture | pages [9] -->
m

<!-- b002233 | furniture | pages [9] -->
m

<!-- b002234 | furniture | pages [9] -->
m

<!-- b002235 | furniture | pages [9] -->
m

<!-- b002236 | furniture | pages [9] -->
m

<!-- b002237 | furniture | pages [9] -->
m

<!-- b002238 | furniture | pages [9] -->
m

<!-- b002239 | furniture | pages [9] -->
m

<!-- b002240 | furniture | pages [9] -->
m

<!-- b002241 | furniture | pages [9] -->
m

<!-- b002242 | furniture | pages [9] -->
m

<!-- b002243 | furniture | pages [9] -->
m

<!-- b002244 | furniture | pages [9] -->
m

<!-- b002245 | furniture | pages [9] -->
m

<!-- b002246 | furniture | pages [9] -->
m

<!-- b002247 | furniture | pages [9] -->
m

<!-- b002248 | furniture | pages [9] -->
m

<!-- b002249 | furniture | pages [9] -->
m

<!-- b002250 | furniture | pages [9] -->
m

<!-- b002251 | furniture | pages [9] -->
m

<!-- b002252 | furniture | pages [9] -->
m

<!-- b002253 | furniture | pages [9] -->
m

<!-- b002254 | furniture | pages [9] -->
m

<!-- b002255 | furniture | pages [9] -->
m

<!-- b002256 | furniture | pages [9] -->
m

<!-- b002257 | furniture | pages [9] -->
m

<!-- b002258 | furniture | pages [9] -->
m

<!-- b002259 | furniture | pages [9] -->
m

<!-- b002260 | furniture | pages [9] -->
m

<!-- b002261 | furniture | pages [9] -->
m

<!-- b002262 | furniture | pages [9] -->
m

<!-- b002263 | furniture | pages [9] -->
m

<!-- b002264 | furniture | pages [9] -->
m

<!-- b002265 | furniture | pages [9] -->
m

<!-- b002266 | furniture | pages [9] -->
m

<!-- b002267 | furniture | pages [9] -->
m

<!-- b002268 | furniture | pages [9] -->
m

<!-- b002269 | furniture | pages [9] -->
m

<!-- b002270 | furniture | pages [9] -->
m

<!-- b002271 | furniture | pages [9] -->
m

<!-- b002272 | furniture | pages [9] -->
m

<!-- b002273 | furniture | pages [9] -->
m

<!-- b002274 | furniture | pages [9] -->
m

<!-- b002275 | furniture | pages [9] -->
m

<!-- b002276 | furniture | pages [9] -->
m

<!-- b002277 | furniture | pages [9] -->
m

<!-- b002278 | furniture | pages [9] -->
m

<!-- b002279 | furniture | pages [9] -->
m

<!-- b002280 | furniture | pages [9] -->
m

<!-- b002281 | furniture | pages [9] -->
m

<!-- b002282 | furniture | pages [9] -->
m

<!-- b002283 | furniture | pages [9] -->
m

<!-- b002284 | furniture | pages [9] -->
m

<!-- b002285 | furniture | pages [9] -->
m

<!-- b002286 | furniture | pages [9] -->
m

<!-- b002287 | furniture | pages [9] -->
m

<!-- b002288 | furniture | pages [9] -->
m

<!-- b002289 | furniture | pages [9] -->
m

<!-- b002290 | furniture | pages [9] -->
m

<!-- b002291 | furniture | pages [9] -->
m

<!-- b002292 | furniture | pages [9] -->
m

<!-- b002293 | furniture | pages [9] -->
m

<!-- b002294 | furniture | pages [9] -->
m

<!-- b002295 | furniture | pages [9] -->
m

<!-- b002296 | furniture | pages [9] -->
m

<!-- b002297 | furniture | pages [9] -->
m

<!-- b002298 | furniture | pages [9] -->
m

<!-- b002299 | furniture | pages [9] -->
m

<!-- b002300 | furniture | pages [9] -->
m

<!-- b002301 | furniture | pages [9] -->
m

<!-- b002302 | furniture | pages [9] -->
m

<!-- b002303 | furniture | pages [9] -->
m

<!-- b002304 | furniture | pages [9] -->
m

<!-- b002305 | furniture | pages [9] -->
m

<!-- b002306 | furniture | pages [10] -->
Team 2517690

<!-- b002307 | furniture | pages [10] -->


<!-- b002308 | furniture | pages [10] -->


<!-- b002309 | furniture | pages [10] -->


<!-- b002310 | furniture | pages [10] -->


<!-- b002311 | furniture | pages [10] -->


<!-- b002312 | furniture | pages [10] -->


<!-- b002313 | furniture | pages [10] -->


<!-- b002314 | furniture | pages [10] -->


<!-- b002315 | furniture | pages [10] -->


<!-- b002316 | furniture | pages [10] -->


<!-- b002317 | furniture | pages [10] -->


<!-- b002318 | furniture | pages [10] -->


<!-- b002319 | furniture | pages [10] -->


<!-- b002320 | furniture | pages [10] -->


<!-- b002321 | furniture | pages [10] -->
Page 10 of 25

<!-- b002322 | prose | pages [10] -->
appropriate machine-learning model is of great significance. Especially when dealing with multiple features and complex data relationships, different regression models have different advantages and applicable scenarios.

<!-- b002323 | prose | pages [10] -->
For this reason, this paper will compare four machine learning models widely used in regression problems: Random Forest regression, Lasso regression, XGBoost regression, and Neural Network regression. By comparing the prediction effects of these models, the aim is to find the model most suitable for the task of predicting the number of Olympic medals. To improve the accuracy of the regression models, this paper uses ten-fold cross-validation. The hold-out method is adopted, with 90% of the samples used as the training set and 10% of the samples used as the test set. The evaluation metrics of the four regression models are calculated, as shown in the following table：

<!-- b002324 | caption | pages [10] -->
Table 4:Results of regression model evaluation

<!-- b002325 | furniture | pages [10] -->


<!-- b002326 | prose | pages [10] -->
During the comparison of multiple regression models, after comprehensive evaluation and

<!-- b002327 | heading | pages [10] -->
verification, the Random Forest regression model outperforms other models in evaluation

<!-- b002328 | prose | pages [10] -->
, MSE and MAE. Therefore, based on its high prediction accuracy and metrics such as strong generalization ability, this study finally selects the Random Forest regression model as the main tool for predicting the number of medals in the 2028 Olympic Games.

<!-- b002329 | heading | pages [10] -->
5.1.4 Medal Table Prediction Results Based on Random Forest

<!-- b002330 | prose | pages [10] -->
In order to accurately predict the number of medals of each country in the 2028 Olympic Games, we adopt the Random Forest regres- sion model. This model achieves efficient pre- diction by integrating multiple decision trees and is particularly suitable for dealing with data with complex non-linear relationships and multi-dimensional features. The advantages of the random forest regression model lie in its strong feature selection ability, low risk of over- fitting, and excellent generalization ability. Through multiple trainings and evaluations, it has been confirmed that this model performs outstandingly when dealing with the task of Olympic medal prediction.

<!-- b002331 | furniture | pages [10] -->


<!-- b002332 | prose | pages [10] -->
m

<!-- b002333 | prose | pages [10] -->
m

<!-- b002334 | prose | pages [10] -->
m

<!-- b002335 | prose | pages [10] -->
m

<!-- b002336 | prose | pages [10] -->
m

<!-- b002337 | prose | pages [10] -->
m

<!-- b002338 | prose | pages [10] -->
m

<!-- b002339 | prose | pages [10] -->
m

<!-- b002340 | prose | pages [10] -->
m

<!-- b002341 | prose | pages [10] -->
m

<!-- b002342 | prose | pages [10] -->
m

<!-- b002343 | prose | pages [10] -->
m

<!-- b002344 | prose | pages [10] -->
m

<!-- b002345 | prose | pages [10] -->
m

<!-- b002346 | prose | pages [10] -->
m

<!-- b002347 | prose | pages [10] -->
m

<!-- b002348 | prose | pages [10] -->
m

<!-- b002349 | prose | pages [10] -->
m

<!-- b002350 | prose | pages [10] -->
m

<!-- b002351 | prose | pages [10] -->
m

<!-- b002352 | prose | pages [10] -->
m

<!-- b002353 | prose | pages [10] -->
m

<!-- b002354 | prose | pages [10] -->
m

<!-- b002355 | prose | pages [10] -->
m

<!-- b002356 | prose | pages [10] -->
m

<!-- b002357 | prose | pages [10] -->
m

<!-- b002358 | prose | pages [10] -->
m

<!-- b002359 | prose | pages [10] -->
m

<!-- b002360 | prose | pages [10] -->
m

<!-- b002361 | prose | pages [10] -->
m

<!-- b002362 | prose | pages [10] -->
m

<!-- b002363 | prose | pages [10] -->
m

<!-- b002364 | prose | pages [10] -->
m

<!-- b002365 | prose | pages [10] -->
m

<!-- b002366 | prose | pages [10] -->
m

<!-- b002367 | prose | pages [10] -->
m

<!-- b002368 | prose | pages [10] -->
m

<!-- b002369 | prose | pages [10] -->
m

<!-- b002370 | prose | pages [10] -->
m

<!-- b002371 | prose | pages [10] -->
m

<!-- b002372 | prose | pages [10] -->
m

<!-- b002373 | prose | pages [10] -->
m

<!-- b002374 | prose | pages [10] -->
m

<!-- b002375 | prose | pages [10] -->
m

<!-- b002376 | prose | pages [10] -->
m

<!-- b002377 | prose | pages [10] -->
m

<!-- b002378 | prose | pages [10] -->
m

<!-- b002379 | prose | pages [10] -->
m

<!-- b002380 | prose | pages [10] -->
m

<!-- b002381 | prose | pages [10] -->
m

<!-- b002382 | prose | pages [10] -->
m

<!-- b002383 | prose | pages [10] -->
m

<!-- b002384 | prose | pages [10] -->
m

<!-- b002385 | prose | pages [10] -->
m

<!-- b002386 | prose | pages [10] -->
m

<!-- b002387 | prose | pages [10] -->
m

<!-- b002388 | prose | pages [10] -->
m

<!-- b002389 | prose | pages [10] -->
m

<!-- b002390 | prose | pages [10] -->
m

<!-- b002391 | prose | pages [10] -->
m

<!-- b002392 | prose | pages [10] -->
m

<!-- b002393 | prose | pages [10] -->
m

<!-- b002394 | prose | pages [10] -->
m

<!-- b002395 | prose | pages [10] -->
m

<!-- b002396 | prose | pages [10] -->
m

<!-- b002397 | prose | pages [10] -->
m

<!-- b002398 | prose | pages [10] -->
m

<!-- b002399 | prose | pages [10] -->
m

<!-- b002400 | prose | pages [10] -->
m

<!-- b002401 | prose | pages [10] -->
m

<!-- b002402 | prose | pages [10] -->
m

<!-- b002403 | prose | pages [10] -->
m

<!-- b002404 | prose | pages [10] -->
m

<!-- b002405 | prose | pages [10] -->
m

<!-- b002406 | prose | pages [10] -->
m

<!-- b002407 | prose | pages [10] -->
m

<!-- b002408 | prose | pages [10] -->
m

<!-- b002409 | prose | pages [10] -->
m

<!-- b002410 | prose | pages [10] -->
m

<!-- b002411 | prose | pages [10] -->
m

<!-- b002412 | prose | pages [10] -->
m

<!-- b002413 | prose | pages [10] -->
m

<!-- b002414 | prose | pages [10] -->
m

<!-- b002415 | prose | pages [10] -->
m

<!-- b002416 | prose | pages [10] -->
m

<!-- b002417 | prose | pages [10] -->
m

<!-- b002418 | prose | pages [10] -->
m

<!-- b002419 | prose | pages [10] -->
m

<!-- b002420 | prose | pages [10] -->
m

<!-- b002421 | prose | pages [10] -->
m

<!-- b002422 | prose | pages [10] -->
m

<!-- b002423 | prose | pages [10] -->
m

<!-- b002424 | prose | pages [10] -->
m

<!-- b002425 | prose | pages [10] -->
m

<!-- b002426 | prose | pages [10] -->
m

<!-- b002427 | prose | pages [10] -->
m

<!-- b002428 | prose | pages [10] -->
m

<!-- b002429 | prose | pages [10] -->
m

<!-- b002430 | prose | pages [10] -->
m

<!-- b002431 | prose | pages [10] -->
m

<!-- b002432 | prose | pages [10] -->
m

<!-- b002433 | prose | pages [10] -->
m

<!-- b002434 | prose | pages [10] -->
m

<!-- b002435 | prose | pages [10] -->
m

<!-- b002436 | prose | pages [10] -->
m

<!-- b002437 | prose | pages [10] -->
m

<!-- b002438 | prose | pages [10] -->
m

<!-- b002439 | prose | pages [10] -->
m

<!-- b002440 | prose | pages [10] -->
m

<!-- b002441 | prose | pages [10] -->
m

<!-- b002442 | prose | pages [10] -->
m

<!-- b002443 | prose | pages [10] -->
m

<!-- b002444 | prose | pages [10] -->
m

<!-- b002445 | prose | pages [10] -->
m

<!-- b002446 | prose | pages [10] -->
m

<!-- b002447 | prose | pages [10] -->
m

<!-- b002448 | prose | pages [10] -->
m

<!-- b002449 | prose | pages [10] -->
m

<!-- b002450 | prose | pages [10] -->
m

<!-- b002451 | prose | pages [10] -->
m

<!-- b002452 | prose | pages [10] -->
m

<!-- b002453 | prose | pages [10] -->
m

<!-- b002454 | prose | pages [10] -->
m

<!-- b002455 | prose | pages [10] -->
m

<!-- b002456 | prose | pages [10] -->
m

<!-- b002457 | prose | pages [10] -->
m

<!-- b002458 | prose | pages [10] -->
m

<!-- b002459 | prose | pages [10] -->
m

<!-- b002460 | prose | pages [10] -->
m

<!-- b002461 | prose | pages [10] -->
m

<!-- b002462 | prose | pages [10] -->
m

<!-- b002463 | prose | pages [10] -->
m

<!-- b002464 | prose | pages [10] -->
m

<!-- b002465 | prose | pages [10] -->
m

<!-- b002466 | prose | pages [10] -->
m

<!-- b002467 | prose | pages [10] -->
m

<!-- b002468 | prose | pages [10] -->
m

<!-- b002469 | prose | pages [10] -->
m

<!-- b002470 | prose | pages [10] -->
m

<!-- b002471 | prose | pages [10] -->
m

<!-- b002472 | prose | pages [10] -->
m

<!-- b002473 | prose | pages [10] -->
m

<!-- b002474 | prose | pages [10] -->
m

<!-- b002475 | prose | pages [10] -->
m

<!-- b002476 | prose | pages [10] -->
m

<!-- b002477 | prose | pages [10] -->
m

<!-- b002478 | prose | pages [10] -->
m

<!-- b002479 | prose | pages [10] -->
m

<!-- b002480 | prose | pages [10] -->
m

<!-- b002481 | prose | pages [10] -->
m

<!-- b002482 | prose | pages [10] -->
m

<!-- b002483 | prose | pages [10] -->
m

<!-- b002484 | prose | pages [10] -->
m

<!-- b002485 | prose | pages [10] -->
m

<!-- b002486 | prose | pages [10] -->
m

<!-- b002487 | prose | pages [10] -->
m

<!-- b002488 | prose | pages [10] -->
m

<!-- b002489 | prose | pages [10] -->
m

<!-- b002490 | prose | pages [10] -->
m

<!-- b002491 | prose | pages [10] -->
m

<!-- b002492 | prose | pages [10] -->
m

<!-- b002493 | prose | pages [10] -->
m

<!-- b002494 | prose | pages [10] -->
m

<!-- b002495 | prose | pages [10] -->
m

<!-- b002496 | prose | pages [10] -->
m

<!-- b002497 | prose | pages [10] -->
m

<!-- b002498 | prose | pages [10] -->
m

<!-- b002499 | prose | pages [10] -->
m

<!-- b002500 | prose | pages [10] -->
m

<!-- b002501 | prose | pages [10] -->
m

<!-- b002502 | prose | pages [10] -->
m

<!-- b002503 | prose | pages [10] -->
m

<!-- b002504 | prose | pages [10] -->
m

<!-- b002505 | prose | pages [10] -->
m

<!-- b002506 | prose | pages [10] -->
m

<!-- b002507 | prose | pages [10] -->
m

<!-- b002508 | prose | pages [10] -->
m

<!-- b002509 | prose | pages [10] -->
m

<!-- b002510 | prose | pages [10] -->
m

<!-- b002511 | prose | pages [10] -->
m

<!-- b002512 | prose | pages [10] -->
m

<!-- b002513 | prose | pages [10] -->
m

<!-- b002514 | prose | pages [10] -->
m

<!-- b002515 | prose | pages [10] -->
m

<!-- b002516 | prose | pages [10] -->
m

<!-- b002517 | prose | pages [10] -->
m

<!-- b002518 | prose | pages [10] -->
m

<!-- b002519 | prose | pages [10] -->
m

<!-- b002520 | prose | pages [10] -->
m

<!-- b002521 | prose | pages [10] -->
m

<!-- b002522 | prose | pages [10] -->
m

<!-- b002523 | prose | pages [10] -->
m

<!-- b002524 | prose | pages [10] -->
m

<!-- b002525 | prose | pages [10] -->
m

<!-- b002526 | prose | pages [10] -->
m

<!-- b002527 | prose | pages [10] -->
m

<!-- b002528 | prose | pages [10] -->
m

<!-- b002529 | prose | pages [10] -->
m

<!-- b002530 | prose | pages [10] -->
m

<!-- b002531 | prose | pages [10] -->
m

<!-- b002532 | prose | pages [10] -->
m

<!-- b002533 | prose | pages [10] -->
m

<!-- b002534 | prose | pages [10] -->
m

<!-- b002535 | prose | pages [10] -->
m

<!-- b002536 | prose | pages [10] -->
m

<!-- b002537 | prose | pages [10] -->
m

<!-- b002538 | prose | pages [10] -->
m

<!-- b002539 | prose | pages [10] -->
m

<!-- b002540 | prose | pages [10] -->
m

<!-- b002541 | prose | pages [10] -->
m

<!-- b002542 | prose | pages [10] -->
m

<!-- b002543 | prose | pages [10] -->
m

<!-- b002544 | prose | pages [10] -->
m

<!-- b002545 | prose | pages [10] -->
m

<!-- b002546 | prose | pages [10] -->
m

<!-- b002547 | prose | pages [10] -->
m

<!-- b002548 | prose | pages [10] -->
m

<!-- b002549 | prose | pages [10] -->
m

<!-- b002550 | prose | pages [10] -->
m

<!-- b002551 | prose | pages [10] -->
m

<!-- b002552 | prose | pages [10] -->
m

<!-- b002553 | prose | pages [10] -->
m

<!-- b002554 | prose | pages [10] -->
m

<!-- b002555 | prose | pages [10] -->
m

<!-- b002556 | prose | pages [10] -->
m

<!-- b002557 | prose | pages [10] -->
m

<!-- b002558 | prose | pages [10] -->
m

<!-- b002559 | prose | pages [10] -->
m

<!-- b002560 | prose | pages [10] -->
m

<!-- b002561 | prose | pages [10] -->
m

<!-- b002562 | prose | pages [10] -->
m

<!-- b002563 | prose | pages [10] -->
m

<!-- b002564 | prose | pages [10] -->
m

<!-- b002565 | prose | pages [10] -->
m

<!-- b002566 | prose | pages [10] -->
m

<!-- b002567 | prose | pages [10] -->
m

<!-- b002568 | prose | pages [10] -->
m

<!-- b002569 | prose | pages [10] -->
m

<!-- b002570 | prose | pages [10] -->
m

<!-- b002571 | prose | pages [10] -->
m

<!-- b002572 | prose | pages [10] -->
m

<!-- b002573 | prose | pages [10] -->
m

<!-- b002574 | prose | pages [10] -->
m

<!-- b002575 | prose | pages [10] -->
m

<!-- b002576 | prose | pages [10] -->
m

<!-- b002577 | prose | pages [10] -->
m

<!-- b002578 | prose | pages [10] -->
m

<!-- b002579 | prose | pages [10] -->
m

<!-- b002580 | prose | pages [10] -->
m

<!-- b002581 | prose | pages [10] -->
m

<!-- b002582 | prose | pages [10] -->
m

<!-- b002583 | prose | pages [10] -->
m

<!-- b002584 | prose | pages [10] -->
m

<!-- b002585 | prose | pages [10] -->
m

<!-- b002586 | prose | pages [10] -->
m

<!-- b002587 | prose | pages [10] -->
m

<!-- b002588 | prose | pages [10] -->
m

<!-- b002589 | prose | pages [10] -->
m

<!-- b002590 | prose | pages [10] -->
m

<!-- b002591 | prose | pages [10] -->
m

<!-- b002592 | prose | pages [10] -->
m

<!-- b002593 | prose | pages [10] -->
m

<!-- b002594 | prose | pages [10] -->
m

<!-- b002595 | prose | pages [10] -->
m

<!-- b002596 | prose | pages [10] -->
m

<!-- b002597 | prose | pages [10] -->
m

<!-- b002598 | prose | pages [10] -->
m

<!-- b002599 | prose | pages [10] -->
m

<!-- b002600 | prose | pages [10] -->
m

<!-- b002601 | prose | pages [10] -->
m

<!-- b002602 | prose | pages [10] -->
m

<!-- b002603 | prose | pages [10] -->
m

<!-- b002604 | prose | pages [10] -->
m

<!-- b002605 | prose | pages [10] -->
m

<!-- b002606 | prose | pages [10] -->
m

<!-- b002607 | prose | pages [10] -->
m

<!-- b002608 | prose | pages [10] -->
m

<!-- b002609 | prose | pages [10] -->
m

<!-- b002610 | prose | pages [10] -->
m

<!-- b002611 | prose | pages [10] -->
m

<!-- b002612 | prose | pages [10] -->
m

<!-- b002613 | prose | pages [10] -->
m

<!-- b002614 | prose | pages [10] -->
m

<!-- b002615 | prose | pages [10] -->
m

<!-- b002616 | prose | pages [10] -->
m

<!-- b002617 | prose | pages [10] -->
m

<!-- b002618 | prose | pages [10] -->
m

<!-- b002619 | prose | pages [10] -->
m

<!-- b002620 | prose | pages [10] -->
m

<!-- b002621 | prose | pages [10] -->
m

<!-- b002622 | prose | pages [10] -->
m

<!-- b002623 | prose | pages [10] -->
m

<!-- b002624 | prose | pages [10] -->
m

<!-- b002625 | prose | pages [10] -->
m

<!-- b002626 | prose | pages [10] -->
m

<!-- b002627 | prose | pages [10] -->
m

<!-- b002628 | prose | pages [10] -->
m

<!-- b002629 | prose | pages [10] -->
m

<!-- b002630 | prose | pages [10] -->
m

<!-- b002631 | prose | pages [10] -->
m

<!-- b002632 | prose | pages [10] -->
m

<!-- b002633 | prose | pages [10] -->
m

<!-- b002634 | prose | pages [10] -->
m

<!-- b002635 | prose | pages [10] -->
m

<!-- b002636 | prose | pages [10] -->
m

<!-- b002637 | prose | pages [10] -->
m

<!-- b002638 | prose | pages [10] -->
m

<!-- b002639 | prose | pages [10] -->
m

<!-- b002640 | prose | pages [10] -->
m

<!-- b002641 | prose | pages [10] -->
m

<!-- b002642 | prose | pages [10] -->
m

<!-- b002643 | prose | pages [10] -->
m

<!-- b002644 | prose | pages [10] -->
m

<!-- b002645 | prose | pages [10] -->
m

<!-- b002646 | prose | pages [10] -->
m

<!-- b002647 | prose | pages [10] -->
m

<!-- b002648 | prose | pages [10] -->
m

<!-- b002649 | prose | pages [10] -->
m

<!-- b002650 | prose | pages [10] -->
m

<!-- b002651 | prose | pages [10] -->
m

<!-- b002652 | prose | pages [10] -->
m

<!-- b002653 | prose | pages [10] -->
m

<!-- b002654 | prose | pages [10] -->
m

<!-- b002655 | prose | pages [10] -->
m

<!-- b002656 | prose | pages [10] -->
m

<!-- b002657 | prose | pages [10] -->
m

<!-- b002658 | prose | pages [10] -->
m

<!-- b002659 | prose | pages [10] -->
m

<!-- b002660 | prose | pages [10] -->
m

<!-- b002661 | prose | pages [10] -->
m

<!-- b002662 | prose | pages [10] -->
m

<!-- b002663 | prose | pages [10] -->
m

<!-- b002664 | prose | pages [10] -->
m

<!-- b002665 | prose | pages [10] -->
m

<!-- b002666 | prose | pages [10] -->
m

<!-- b002667 | prose | pages [10] -->
m

<!-- b002668 | prose | pages [10] -->
m

<!-- b002669 | prose | pages [10] -->
m

<!-- b002670 | prose | pages [10] -->
m

<!-- b002671 | prose | pages [10] -->
m

<!-- b002672 | prose | pages [10] -->
m

<!-- b002673 | prose | pages [10] -->
m

<!-- b002674 | prose | pages [10] -->
m

<!-- b002675 | prose | pages [10] -->
m

<!-- b002676 | prose | pages [10] -->
m

<!-- b002677 | prose | pages [10] -->
m

<!-- b002678 | prose | pages [10] -->
m

<!-- b002679 | prose | pages [10] -->
m

<!-- b002680 | prose | pages [10] -->
m

<!-- b002681 | prose | pages [10] -->
m

<!-- b002682 | prose | pages [10] -->
m

<!-- b002683 | prose | pages [10] -->
m

<!-- b002684 | prose | pages [10] -->
m

<!-- b002685 | prose | pages [10] -->
m

<!-- b002686 | prose | pages [10] -->
m

<!-- b002687 | prose | pages [10] -->
m

<!-- b002688 | prose | pages [10] -->
m

<!-- b002689 | prose | pages [10] -->
m

<!-- b002690 | prose | pages [10] -->
m

<!-- b002691 | prose | pages [10] -->
m

<!-- b002692 | prose | pages [10] -->
m

<!-- b002693 | prose | pages [10] -->
m

<!-- b002694 | prose | pages [10] -->
m

<!-- b002695 | prose | pages [10] -->
m

<!-- b002696 | prose | pages [10] -->
m

<!-- b002697 | prose | pages [10] -->
m

<!-- b002698 | prose | pages [10] -->
m

<!-- b002699 | prose | pages [10] -->
m

<!-- b002700 | prose | pages [10] -->
m

<!-- b002701 | prose | pages [10] -->
m

<!-- b002702 | prose | pages [10] -->
m

<!-- b002703 | prose | pages [10] -->
m

<!-- b002704 | prose | pages [10] -->
m

<!-- b002705 | prose | pages [10] -->
m

<!-- b002706 | prose | pages [10] -->
m

<!-- b002707 | prose | pages [10] -->
m

<!-- b002708 | prose | pages [10] -->
m

<!-- b002709 | prose | pages [10] -->
m

<!-- b002710 | prose | pages [10] -->
m

<!-- b002711 | prose | pages [10] -->
m

<!-- b002712 | prose | pages [10] -->
m

<!-- b002713 | prose | pages [10] -->
m

<!-- b002714 | prose | pages [10] -->
m

<!-- b002715 | prose | pages [10] -->
m

<!-- b002716 | prose | pages [10] -->
m

<!-- b002717 | prose | pages [10] -->
m

<!-- b002718 | prose | pages [10] -->
m

<!-- b002719 | prose | pages [10] -->
m

<!-- b002720 | prose | pages [10] -->
m

<!-- b002721 | prose | pages [10] -->
m

<!-- b002722 | prose | pages [10] -->
m

<!-- b002723 | prose | pages [10] -->
m

<!-- b002724 | prose | pages [10] -->
m

<!-- b002725 | prose | pages [10] -->
m

<!-- b002726 | prose | pages [10] -->
m

<!-- b002727 | prose | pages [10] -->
m

<!-- b002728 | prose | pages [10] -->
m

<!-- b002729 | prose | pages [10] -->
m

<!-- b002730 | prose | pages [10] -->
m

<!-- b002731 | prose | pages [10] -->
m

<!-- b002732 | prose | pages [10] -->
m

<!-- b002733 | prose | pages [10] -->
m

<!-- b002734 | prose | pages [10] -->
m

<!-- b002735 | prose | pages [10] -->
m

<!-- b002736 | prose | pages [10] -->
m

<!-- b002737 | prose | pages [10] -->
m

<!-- b002738 | prose | pages [10] -->
m

<!-- b002739 | prose | pages [10] -->
m

<!-- b002740 | prose | pages [10] -->
m

<!-- b002741 | prose | pages [10] -->
m

<!-- b002742 | prose | pages [10] -->
m

<!-- b002743 | prose | pages [10] -->
m

<!-- b002744 | prose | pages [10] -->
m

<!-- b002745 | prose | pages [10] -->
m

<!-- b002746 | prose | pages [10] -->
m

<!-- b002747 | prose | pages [10] -->
m

<!-- b002748 | prose | pages [10] -->
m

<!-- b002749 | prose | pages [10] -->
m

<!-- b002750 | prose | pages [10] -->
m

<!-- b002751 | prose | pages [10] -->
m

<!-- b002752 | prose | pages [10] -->
m

<!-- b002753 | prose | pages [10] -->
m

<!-- b002754 | prose | pages [10] -->
m

<!-- b002755 | prose | pages [10] -->
m

<!-- b002756 | prose | pages [10] -->
m

<!-- b002757 | prose | pages [10] -->
m

<!-- b002758 | prose | pages [10] -->
m

<!-- b002759 | prose | pages [10] -->
m

<!-- b002760 | prose | pages [10] -->
m

<!-- b002761 | prose | pages [10] -->
m

<!-- b002762 | prose | pages [10] -->
m

<!-- b002763 | prose | pages [10] -->
m

<!-- b002764 | prose | pages [10] -->
m

<!-- b002765 | prose | pages [10] -->
m

<!-- b002766 | prose | pages [10] -->
m

<!-- b002767 | prose | pages [10] -->
m

<!-- b002768 | prose | pages [10] -->
m

<!-- b002769 | prose | pages [10] -->
m

<!-- b002770 | prose | pages [10] -->
m

<!-- b002771 | prose | pages [10] -->
m

<!-- b002772 | prose | pages [10] -->
m

<!-- b002773 | prose | pages [10] -->
m

<!-- b002774 | prose | pages [10] -->
m

<!-- b002775 | prose | pages [10] -->
m

<!-- b002776 | prose | pages [10] -->
m

<!-- b002777 | prose | pages [10] -->
m

<!-- b002778 | prose | pages [10] -->
m

<!-- b002779 | prose | pages [10] -->
m

<!-- b002780 | prose | pages [10] -->
m

<!-- b002781 | prose | pages [10] -->
m

<!-- b002782 | prose | pages [10] -->
m

<!-- b002783 | prose | pages [10] -->
m

<!-- b002784 | prose | pages [10] -->
m

<!-- b002785 | prose | pages [10] -->
m

<!-- b002786 | prose | pages [10] -->
m

<!-- b002787 | prose | pages [10] -->
m

<!-- b002788 | prose | pages [10] -->
m

<!-- b002789 | prose | pages [10] -->
m

<!-- b002790 | prose | pages [10] -->
m

<!-- b002791 | prose | pages [10] -->
m

<!-- b002792 | prose | pages [10] -->
m

<!-- b002793 | prose | pages [10] -->
m

<!-- b002794 | prose | pages [10] -->
m

<!-- b002795 | prose | pages [10] -->
m

<!-- b002796 | prose | pages [10] -->
m

<!-- b002797 | prose | pages [10] -->
m

<!-- b002798 | prose | pages [10] -->
m

<!-- b002799 | prose | pages [10] -->
m

<!-- b002800 | prose | pages [10] -->
m

<!-- b002801 | prose | pages [10] -->
m

<!-- b002802 | prose | pages [10] -->
m

<!-- b002803 | prose | pages [10] -->
m

<!-- b002804 | prose | pages [10] -->
m

<!-- b002805 | prose | pages [10] -->
m

<!-- b002806 | prose | pages [10] -->
m

<!-- b002807 | prose | pages [10] -->
m

<!-- b002808 | prose | pages [10] -->
m

<!-- b002809 | prose | pages [10] -->
m

<!-- b002810 | prose | pages [10] -->
m

<!-- b002811 | prose | pages [10] -->
m

<!-- b002812 | prose | pages [10] -->
m

<!-- b002813 | prose | pages [10] -->
m

<!-- b002814 | prose | pages [10] -->
m

<!-- b002815 | prose | pages [10] -->
m

<!-- b002816 | prose | pages [10] -->
m

<!-- b002817 | prose | pages [10] -->
m

<!-- b002818 | prose | pages [10] -->
m

<!-- b002819 | prose | pages [10] -->
m

<!-- b002820 | prose | pages [10] -->
m

<!-- b002821 | prose | pages [10] -->
m

<!-- b002822 | prose | pages [10] -->
m

<!-- b002823 | prose | pages [10] -->
m

<!-- b002824 | prose | pages [10] -->
m

<!-- b002825 | prose | pages [10] -->
m

<!-- b002826 | prose | pages [10] -->
m

<!-- b002827 | prose | pages [10] -->
m

<!-- b002828 | prose | pages [10] -->
m

<!-- b002829 | prose | pages [10] -->
m

<!-- b002830 | prose | pages [10] -->
m

<!-- b002831 | prose | pages [10] -->
m

<!-- b002832 | prose | pages [10] -->
m

<!-- b002833 | prose | pages [10] -->
m

<!-- b002834 | prose | pages [10] -->
m

<!-- b002835 | prose | pages [10] -->
m

<!-- b002836 | prose | pages [10] -->
m

<!-- b002837 | prose | pages [10] -->
m

<!-- b002838 | prose | pages [10] -->
m

<!-- b002839 | prose | pages [10] -->
m

<!-- b002840 | prose | pages [10] -->
m

<!-- b002841 | prose | pages [10] -->
m

<!-- b002842 | prose | pages [10] -->
m

<!-- b002843 | prose | pages [10] -->
m

<!-- b002844 | prose | pages [10] -->
m

<!-- b002845 | prose | pages [10] -->
m

<!-- b002846 | prose | pages [10] -->
m

<!-- b002847 | prose | pages [10] -->
m

<!-- b002848 | prose | pages [10] -->
m

<!-- b002849 | prose | pages [10] -->
m

<!-- b002850 | prose | pages [10] -->
m

<!-- b002851 | prose | pages [10] -->
m

<!-- b002852 | prose | pages [10] -->
m

<!-- b002853 | prose | pages [10] -->
m

<!-- b002854 | prose | pages [10] -->
m

<!-- b002855 | prose | pages [10] -->
m

<!-- b002856 | prose | pages [10] -->
m

<!-- b002857 | prose | pages [10] -->
m

<!-- b002858 | prose | pages [10] -->
m

<!-- b002859 | prose | pages [10] -->
m

<!-- b002860 | prose | pages [10] -->
m

<!-- b002861 | prose | pages [10] -->
m

<!-- b002862 | prose | pages [10] -->
m

<!-- b002863 | prose | pages [10] -->
m

<!-- b002864 | prose | pages [10] -->
m

<!-- b002865 | prose | pages [10] -->
m

<!-- b002866 | prose | pages [10] -->
m

<!-- b002867 | prose | pages [10] -->
m

<!-- b002868 | prose | pages [10] -->
m

<!-- b002869 | prose | pages [10] -->
m

<!-- b002870 | prose | pages [10] -->
m

<!-- b002871 | prose | pages [10] -->
m

<!-- b002872 | prose | pages [10] -->
m

<!-- b002873 | prose | pages [10] -->
m

<!-- b002874 | prose | pages [10] -->
m

<!-- b002875 | prose | pages [10] -->
m

<!-- b002876 | prose | pages [10] -->
m

<!-- b002877 | prose | pages [10] -->
m

<!-- b002878 | prose | pages [10] -->
m

<!-- b002879 | prose | pages [10] -->
m

<!-- b002880 | prose | pages [10] -->
m

<!-- b002881 | prose | pages [10] -->
m

<!-- b002882 | prose | pages [10] -->
m

<!-- b002883 | prose | pages [10] -->
m

<!-- b002884 | prose | pages [10] -->
m

<!-- b002885 | prose | pages [10] -->
m

<!-- b002886 | prose | pages [10] -->
m

<!-- b002887 | prose | pages [10] -->
m

<!-- b002888 | prose | pages [10] -->
m

<!-- b002889 | prose | pages [10] -->
m

<!-- b002890 | prose | pages [10] -->
m

<!-- b002891 | prose | pages [10] -->
m

<!-- b002892 | prose | pages [10] -->
m

<!-- b002893 | prose | pages [10] -->
m

<!-- b002894 | prose | pages [10] -->
m

<!-- b002895 | prose | pages [10] -->
m

<!-- b002896 | prose | pages [10] -->
m

<!-- b002897 | prose | pages [10] -->
m

<!-- b002898 | prose | pages [10] -->
m

<!-- b002899 | prose | pages [10] -->
m

<!-- b002900 | prose | pages [10] -->
m

<!-- b002901 | prose | pages [10] -->
m

<!-- b002902 | prose | pages [10] -->
m

<!-- b002903 | prose | pages [10] -->
m

<!-- b002904 | prose | pages [10] -->
m

<!-- b002905 | prose | pages [10] -->
m

<!-- b002906 | prose | pages [10] -->
m

<!-- b002907 | prose | pages [10] -->
m

<!-- b002908 | prose | pages [10] -->
m

<!-- b002909 | prose | pages [10] -->
m

<!-- b002910 | prose | pages [10] -->
m

<!-- b002911 | prose | pages [10] -->
m

<!-- b002912 | prose | pages [10] -->
m

<!-- b002913 | prose | pages [10] -->
m

<!-- b002914 | prose | pages [10] -->
m

<!-- b002915 | prose | pages [10] -->
m

<!-- b002916 | prose | pages [10] -->
m

<!-- b002917 | prose | pages [10] -->
m

<!-- b002918 | prose | pages [10] -->
m

<!-- b002919 | prose | pages [10] -->
m

<!-- b002920 | prose | pages [10] -->
m

<!-- b002921 | prose | pages [10] -->
m

<!-- b002922 | prose | pages [10] -->
m

<!-- b002923 | prose | pages [10] -->
m

<!-- b002924 | prose | pages [10] -->
m

<!-- b002925 | prose | pages [10] -->
m

<!-- b002926 | prose | pages [10] -->
m

<!-- b002927 | prose | pages [10] -->
m

<!-- b002928 | prose | pages [10] -->
m

<!-- b002929 | prose | pages [10] -->
m

<!-- b002930 | prose | pages [10] -->
m

<!-- b002931 | prose | pages [10] -->
m

<!-- b002932 | prose | pages [10] -->
m

<!-- b002933 | prose | pages [10] -->
m

<!-- b002934 | prose | pages [10] -->
m

<!-- b002935 | prose | pages [10] -->
m

<!-- b002936 | prose | pages [10] -->
m

<!-- b002937 | prose | pages [10] -->
m

<!-- b002938 | prose | pages [10] -->
m

<!-- b002939 | prose | pages [10] -->
m

<!-- b002940 | prose | pages [10] -->
m

<!-- b002941 | prose | pages [10] -->
m

<!-- b002942 | prose | pages [10] -->
m

<!-- b002943 | prose | pages [10] -->
m

<!-- b002944 | prose | pages [10] -->
m

<!-- b002945 | prose | pages [10] -->
m

<!-- b002946 | prose | pages [10] -->
m

<!-- b002947 | prose | pages [10] -->
m

<!-- b002948 | prose | pages [10] -->
m

<!-- b002949 | prose | pages [10] -->
m

<!-- b002950 | prose | pages [10] -->
m

<!-- b002951 | prose | pages [10] -->
m

<!-- b002952 | prose | pages [10] -->
m

<!-- b002953 | prose | pages [10] -->
m

<!-- b002954 | prose | pages [10] -->
m

<!-- b002955 | prose | pages [10] -->
m

<!-- b002956 | prose | pages [10] -->
m

<!-- b002957 | prose | pages [10] -->
m

<!-- b002958 | prose | pages [10] -->
m

<!-- b002959 | prose | pages [10] -->
m

<!-- b002960 | prose | pages [10] -->
m

<!-- b002961 | prose | pages [10] -->
m

<!-- b002962 | prose | pages [10] -->
m

<!-- b002963 | prose | pages [10] -->
m

<!-- b002964 | prose | pages [10] -->
m

<!-- b002965 | prose | pages [10] -->
m

<!-- b002966 | prose | pages [10] -->
m

<!-- b002967 | prose | pages [10] -->
m

<!-- b002968 | prose | pages [10] -->
m

<!-- b002969 | prose | pages [10] -->
m

<!-- b002970 | prose | pages [10] -->
m

<!-- b002971 | prose | pages [10] -->
m

<!-- b002972 | prose | pages [10] -->
m

<!-- b002973 | prose | pages [10] -->
m

<!-- b002974 | prose | pages [10] -->
m

<!-- b002975 | prose | pages [10] -->
m

<!-- b002976 | prose | pages [10] -->
m

<!-- b002977 | prose | pages [10] -->
m

<!-- b002978 | prose | pages [10] -->
m

<!-- b002979 | prose | pages [10] -->
m

<!-- b002980 | prose | pages [10] -->
m

<!-- b002981 | prose | pages [10] -->
m

<!-- b002982 | prose | pages [10] -->
m

<!-- b002983 | prose | pages [10] -->
m

<!-- b002984 | prose | pages [10] -->
m

<!-- b002985 | prose | pages [10] -->
m

<!-- b002986 | prose | pages [10] -->
m

<!-- b002987 | prose | pages [10] -->
m

<!-- b002988 | prose | pages [10] -->
m

<!-- b002989 | prose | pages [10] -->
m

<!-- b002990 | prose | pages [10] -->
m

<!-- b002991 | prose | pages [10] -->
m

<!-- b002992 | prose | pages [10] -->
m

<!-- b002993 | prose | pages [10] -->
m

<!-- b002994 | prose | pages [10] -->
m

<!-- b002995 | prose | pages [10] -->
m

<!-- b002996 | prose | pages [10] -->
m

<!-- b002997 | prose | pages [10] -->
m

<!-- b002998 | prose | pages [10] -->
m

<!-- b002999 | prose | pages [10] -->
m

<!-- b003000 | prose | pages [10] -->
m

<!-- b003001 | prose | pages [10] -->
m

<!-- b003002 | prose | pages [10] -->
m

<!-- b003003 | prose | pages [10] -->
m

<!-- b003004 | prose | pages [10] -->
m

<!-- b003005 | prose | pages [10] -->
m

<!-- b003006 | prose | pages [10] -->
m

<!-- b003007 | prose | pages [10] -->
m

<!-- b003008 | prose | pages [10] -->
m

<!-- b003009 | prose | pages [10] -->
m

<!-- b003010 | prose | pages [10] -->
m

<!-- b003011 | prose | pages [10] -->
m

<!-- b003012 | prose | pages [10] -->
m

<!-- b003013 | prose | pages [10] -->
m

<!-- b003014 | prose | pages [10] -->
m

<!-- b003015 | prose | pages [10] -->
m

<!-- b003016 | prose | pages [10] -->
m

<!-- b003017 | prose | pages [10] -->
m

<!-- b003018 | prose | pages [10] -->
m

<!-- b003019 | caption | pages [10] -->
Figure 7: Random Forest mechanism diagram

<!-- b003020 | prose | pages [10] -->
Based on the collected data of the 2028 Olympic Games, the trained Random Forest regression model is used for prediction. The model predicts the number of medals each coun- try will win in the Olympics based on features such as the level and quantity of athletes from

<!-- b003021 | furniture | pages [10] -->


<!-- b003022 | prose | pages [10] -->
关注数学模型

<!-- b003023 | furniture | pages [10] -->
2

<!-- b003024 | furniture | pages [10] -->
MATHmodels

<!-- b003025 | furniture | pages [10] -->
获取更多资讯

<!-- b003026 | furniture | pages [12] -->
Team 2517690

<!-- b003027 | furniture | pages [12] -->


<!-- b003028 | furniture | pages [12] -->


<!-- b003029 | furniture | pages [12] -->


<!-- b003030 | furniture | pages [12] -->


<!-- b003031 | furniture | pages [12] -->


<!-- b003032 | furniture | pages [12] -->


<!-- b003033 | furniture | pages [12] -->


<!-- b003034 | furniture | pages [12] -->


<!-- b003035 | furniture | pages [12] -->


<!-- b003036 | furniture | pages [12] -->


<!-- b003037 | furniture | pages [12] -->


<!-- b003038 | furniture | pages [12] -->


<!-- b003039 | furniture | pages [12] -->


<!-- b003040 | furniture | pages [12] -->


<!-- b003041 | furniture | pages [12] -->
Page 12 of 25

<!-- b003042 | heading | pages [12] -->
5.2  Prediction of First Medal Wins for Medal-less Countries

<!-- b003043 | heading | pages [12] -->
5.2.1 Model Preparation

<!-- b003044 | prose | pages [12] -->
(1) Determination of independent and dependent variables ⚫ Independent variables：

<!-- b003045 | furniture | pages [12] -->


<!-- b003046 | prose | pages [12] -->
X The number of medal - less athletes （ ）

<!-- b003047 | furniture | pages [12] -->


<!-- b003048 | prose | pages [12] -->
1 X The number of events participated in （

<!-- b003049 | furniture | pages [12] -->


<!-- b003050 | furniture | pages [12] -->


<!-- b003051 | furniture | pages [12] -->


<!-- b003052 | prose | pages [12] -->
） ）

<!-- b003053 | furniture | pages [12] -->


<!-- b003054 | prose | pages [12] -->
2 2 The number of Olympic Games participated

<!-- b003055 | furniture | pages [12] -->


<!-- b003056 | prose | pages [12] -->
X （ ） in

<!-- b003057 | furniture | pages [12] -->


<!-- b003058 | furniture | pages [12] -->


<!-- b003059 | prose | pages [12] -->
3

<!-- b003060 | furniture | pages [12] -->


<!-- b003061 | prose | pages [12] -->
⚫ Dependent variable:

<!-- b003062 | heading | pages [12] -->
(2) Establish a Logistic regression model

<!-- b003063 | furniture | pages [12] -->


<!-- b003064 | prose | pages [12] -->
Figure 9：Flowchart of part 2 of question 1

<!-- b003065 | prose | pages [12] -->
[4]Logistic regression is a statistical model widely used for classification problems, mainly for binary classification . It linearly combines features and uses the Sigmoid function to map the result to a probability value between 0 and 1 to address binary classification issues. The model uses maximum likelihood estimation to optimize parameters and interprets the impact of features on the probability of an event occurring through regression coefficients.

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
m

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
The steps of Logistic regression are as follows:

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
m

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

<!-- b003329 | heading | pages [12] -->
Step1: Data preparation

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

<!-- b003392 | prose | pages [12] -->
m

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
Collect a dataset that includes multiple features

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
m

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
and a target variable ,

<!-- b003654 | prose | pages [12] -->
is a binary classification variable (0 or 1). Then standardize or normalize the data. which

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
m

<!-- b003711 | prose | pages [12] -->
m

<!-- b003712 | prose | pages [12] -->
m

<!-- b003713 | prose | pages [12] -->
m

<!-- b003714 | prose | pages [12] -->
m

<!-- b003715 | prose | pages [12] -->
m

<!-- b003716 | prose | pages [12] -->
m

<!-- b003717 | prose | pages [12] -->
m

<!-- b003718 | prose | pages [12] -->
m

<!-- b003719 | prose | pages [12] -->
m

<!-- b003720 | prose | pages [12] -->
m

<!-- b003721 | prose | pages [12] -->
m

<!-- b003722 | prose | pages [12] -->
m

<!-- b003723 | prose | pages [12] -->
m

<!-- b003724 | prose | pages [12] -->
m

<!-- b003725 | prose | pages [12] -->
m

<!-- b003726 | prose | pages [12] -->
m

<!-- b003727 | prose | pages [12] -->
m

<!-- b003728 | prose | pages [12] -->
m

<!-- b003729 | prose | pages [12] -->
m

<!-- b003730 | prose | pages [12] -->
m

<!-- b003731 | prose | pages [12] -->
m

<!-- b003732 | prose | pages [12] -->
m

<!-- b003733 | prose | pages [12] -->
m

<!-- b003734 | prose | pages [12] -->
m

<!-- b003735 | prose | pages [12] -->
m

<!-- b003736 | prose | pages [12] -->
m

<!-- b003737 | prose | pages [12] -->
m

<!-- b003738 | prose | pages [12] -->
m

<!-- b003739 | prose | pages [12] -->
m

<!-- b003740 | prose | pages [12] -->
m

<!-- b003741 | prose | pages [12] -->
m

<!-- b003742 | prose | pages [12] -->
m

<!-- b003743 | prose | pages [12] -->
m

<!-- b003744 | prose | pages [12] -->
m

<!-- b003745 | prose | pages [12] -->
m

<!-- b003746 | prose | pages [12] -->
m

<!-- b003747 | prose | pages [12] -->
m

<!-- b003748 | prose | pages [12] -->
m

<!-- b003749 | prose | pages [12] -->
m

<!-- b003750 | prose | pages [12] -->
m

<!-- b003751 | prose | pages [12] -->
m

<!-- b003752 | prose | pages [12] -->
m

<!-- b003753 | prose | pages [12] -->
m

<!-- b003754 | prose | pages [12] -->
m

<!-- b003755 | prose | pages [12] -->
m

<!-- b003756 | prose | pages [12] -->
m

<!-- b003757 | prose | pages [12] -->
m

<!-- b003758 | heading | pages [12] -->
Step2: Define the Logistic regression model

<!-- b003759 | prose | pages [12] -->
Express the linear combination of input features as:

<!-- b003760 | prose | pages [12] -->
=  +  z X 0 1 1 + +  +  X X

<!-- b003761 | prose | pages [12] -->
(2)

<!-- b003762 | prose | pages [12] -->
2 2 3 3

<!-- b003763 | furniture | pages [12] -->


<!-- b003764 | prose | pages [12] -->
to the interval [0, 1] through the Sigmoid function. The Map the linear combination

<!-- b003765 | prose | pages [12] -->
probability of the event occurring is

<!-- b003766 | prose | pages [12] -->
1 = = −= P ( Y 1 X ) + 1 e

<!-- b003767 | heading | pages [12] -->
Step3: Model training

<!-- b003768 | prose | pages [12] -->
1

<!-- b003769 | prose | pages [12] -->
(3)

<!-- b003770 | prose | pages [12] -->
−  +  +  +  ( X X X ) z z e 0 1 1 2 2 3 3

<!-- b003771 | furniture | pages [12] -->


<!-- b003772 | prose | pages [12] -->
Based on the training data, define the likelihood function of Logistic regression, which represents the probability of observing the data given the parameter

<!-- b003773 | prose | pages [12] -->
m

<!-- b003774 | prose | pages [12] -->
=

<!-- b003775 | prose | pages [12] -->
(

<!-- b003776 | prose | pages [12] -->
L

<!-- b003777 | prose | pages [12] -->
)

<!-- b003778 | prose | pages [12] -->
P

<!-- b003779 | prose | pages [12] -->
(

<!-- b003780 | prose | pages [12] -->
Y X i

<!-- b003781 | prose | pages [12] -->
=

<!-- b003782 | prose | pages [12] -->
i

<!-- b003783 | prose | pages [12] -->
1

<!-- b003784 | prose | pages [12] -->
:

<!-- b003785 | prose | pages [12] -->
−

<!-- b003786 | prose | pages [12] -->
−

<!-- b003787 | prose | pages [12] -->
Y

<!-- b003788 | prose | pages [12] -->
1

<!-- b003789 | prose | pages [12] -->
Y

<!-- b003790 | prose | pages [12] -->
) ) 1(

<!-- b003791 | prose | pages [12] -->
P

<!-- b003792 | prose | pages [12] -->
(

<!-- b003793 | prose | pages [12] -->
Y X

<!-- b003794 | prose | pages [12] -->
))

<!-- b003795 | prose | pages [12] -->
(4)

<!-- b003796 | prose | pages [12] -->
i i i i i i

<!-- b003797 | furniture | pages [12] -->


<!-- b003798 | prose | pages [12] -->
To simplify the calculation, take the logarithm to obtain the log-likelihood function:

<!-- b003799 | prose | pages [12] -->


<!-- b003800 | prose | pages [12] -->
m

<!-- b003801 | prose | pages [12] -->


<!-- b003802 | prose | pages [12] -->


<!-- b003803 | prose | pages [12] -->
=

<!-- b003804 | prose | pages [12] -->
log

<!-- b003805 | prose | pages [12] -->
L

<!-- b003806 | prose | pages [12] -->
( )

<!-- b003807 | prose | pages [12] -->
Y

<!-- b003808 | prose | pages [12] -->
log

<!-- b003809 | prose | pages [12] -->
P

<!-- b003810 | prose | pages [12] -->
(

<!-- b003811 | prose | pages [12] -->
Y X i i

<!-- b003812 | prose | pages [12] -->
=

<!-- b003813 | prose | pages [12] -->
i

<!-- b003814 | prose | pages [12] -->
1

<!-- b003815 | furniture | pages [12] -->


<!-- b003816 | prose | pages [12] -->


<!-- b003817 | prose | pages [12] -->
+ − −

<!-- b003818 | prose | pages [12] -->
) ) 1(

<!-- b003819 | prose | pages [12] -->
Y

<!-- b003820 | prose | pages [12] -->
) log( 1

<!-- b003821 | prose | pages [12] -->
P

<!-- b003822 | prose | pages [12] -->
(

<!-- b003823 | prose | pages [12] -->
Y X

<!-- b003824 | prose | pages [12] -->
))

<!-- b003825 | prose | pages [12] -->
(5)

<!-- b003826 | prose | pages [12] -->
i i i i i

<!-- b003827 | furniture | pages [12] -->


<!-- b003828 | prose | pages [12] -->
关注数学模型

<!-- b003829 | furniture | pages [12] -->
2

<!-- b003830 | furniture | pages [12] -->
MATHmodels

<!-- b003831 | furniture | pages [12] -->
获取更多资讯

<!-- b003832 | furniture | pages [13] -->
Team 2517690

<!-- b003833 | furniture | pages [13] -->


<!-- b003834 | furniture | pages [13] -->


<!-- b003835 | furniture | pages [13] -->


<!-- b003836 | furniture | pages [13] -->


<!-- b003837 | furniture | pages [13] -->


<!-- b003838 | furniture | pages [13] -->


<!-- b003839 | furniture | pages [13] -->


<!-- b003840 | furniture | pages [13] -->


<!-- b003841 | furniture | pages [13] -->


<!-- b003842 | furniture | pages [13] -->


<!-- b003843 | furniture | pages [13] -->


<!-- b003844 | furniture | pages [13] -->


<!-- b003845 | furniture | pages [13] -->


<!-- b003846 | furniture | pages [13] -->


<!-- b003847 | furniture | pages [13] -->
Page 13 of 25

<!-- b003848 | prose | pages [13] -->
of the model by maximizing the log-likelihood function: Estimate the parameter

<!-- b003849 | prose | pages [13] -->
ˆ  = arg max  log L ( )

<!-- b003850 | prose | pages [13] -->
(6)

<!-- b003851 | furniture | pages [13] -->


<!-- b003852 | prose | pages [13] -->
Step4: Calculate the predicted probability and make a classification decision For each sample in the test set, calculate the probability that its class is 1:

<!-- b003853 | prose | pages [13] -->
(ˆ

<!-- b003854 | prose | pages [13] -->
= = P Y

<!-- b003855 | prose | pages [13] -->
1

<!-- b003856 | prose | pages [13] -->
X

<!-- b003857 | prose | pages [13] -->
)

<!-- b003858 | prose | pages [13] -->
1

<!-- b003859 | prose | pages [13] -->
1

<!-- b003860 | prose | pages [13] -->
(7)

<!-- b003861 | prose | pages [13] -->
ˆ ˆ ˆ

<!-- b003862 | prose | pages [13] -->
−  +  + +  + +

<!-- b003863 | prose | pages [13] -->
(

<!-- b003864 | prose | pages [13] -->
X

<!-- b003865 | prose | pages [13] -->
...

<!-- b003866 | prose | pages [13] -->
nX

<!-- b003867 | prose | pages [13] -->
)

<!-- b003868 | prose | pages [13] -->
e e

<!-- b003869 | prose | pages [13] -->
0 1 1

<!-- b003870 | prose | pages [13] -->
n

<!-- b003871 | furniture | pages [13] -->


<!-- b003872 | prose | pages [13] -->
Based on the probability value, classify the sample as 0 or 1, setting the threshold at 0.5:

<!-- b003873 | prose | pages [13] -->
𝑌̂ = {1, 𝑖𝑓 𝑃̂(𝑌= 1|𝑋) ≥0.5

<!-- b003874 | prose | pages [13] -->
(8)

<!-- b003875 | prose | pages [13] -->
0, 𝑖𝑓 𝑃̂(𝑌= 1|𝑋) < 0.5

<!-- b003876 | heading | pages [13] -->
5.2.2 Model results

<!-- b003877 | prose | pages [13] -->
微信公众号：数学模型

<!-- b003878 | prose | pages [13] -->
We trained the model using 10-fold cross-validation. The final regression model obtained is:

<!-- b003879 | prose | pages [13] -->
(ˆ

<!-- b003880 | prose | pages [13] -->
= = P Y

<!-- b003881 | prose | pages [13] -->
1

<!-- b003882 | prose | pages [13] -->
X

<!-- b003883 | prose | pages [13] -->
)

<!-- b003884 | prose | pages [13] -->
+

<!-- b003885 | prose | pages [13] -->
1 1

<!-- b003886 | prose | pages [13] -->
(9)

<!-- b003887 | furniture | pages [13] -->


<!-- b003888 | prose | pages [13] -->
− − + + +

<!-- b003889 | prose | pages [13] -->
( .0 006 .0 14

<!-- b003890 | prose | pages [13] -->
X

<!-- b003891 | prose | pages [13] -->
.0 28

<!-- b003892 | prose | pages [13] -->
X

<!-- b003893 | prose | pages [13] -->
.0 34

<!-- b003894 | prose | pages [13] -->
X

<!-- b003895 | prose | pages [13] -->
)

<!-- b003896 | prose | pages [13] -->
e e

<!-- b003897 | prose | pages [13] -->
1 2 3

<!-- b003898 | prose | pages [13] -->
In a logistic regression model, the odds ratio is the ratio of the probability of an event occurring to the probability of the event not occurring, that is:

<!-- b003899 | prose | pages [13] -->
Odds P = 1

<!-- b003900 | prose | pages [13] -->
(10)

<!-- b003901 | prose | pages [13] -->
− P

<!-- b003902 | furniture | pages [13] -->


<!-- b003903 | prose | pages [13] -->
微信号：MATHmodels

<!-- b003904 | prose | pages [13] -->
Solving based on the data, the results are as shown in the following table:

<!-- b003905 | caption | pages [13] -->
Table 6:Forecast of first-time winners

<!-- b003906 | prose | pages [13] -->
Team P

<!-- b003907 | prose | pages [13] -->
Angola 0.81

<!-- b003908 | prose | pages [13] -->
EI Salvador 0.72

<!-- b003909 | prose | pages [13] -->
Honduras 0.69

<!-- b003910 | prose | pages [13] -->
Nicaragua 0.67

<!-- b003911 | prose | pages [13] -->
Odds Whether to win a medal

<!-- b003912 | prose | pages [13] -->
4.26 1

<!-- b003913 | prose | pages [13] -->
2.57 1

<!-- b003914 | prose | pages [13] -->
2.23 1

<!-- b003915 | prose | pages [13] -->
2.03 1

<!-- b003916 | furniture | pages [13] -->


<!-- b003917 | prose | pages [13] -->
Calculations show that only the p-values of the above four countries are all greater than 0.5 and the odds ratios are relatively large. That is, these countries have a relatively high pos- sibility of winning their first medals at the 2028 Olympic Games. Among them, Angola has the largest p-value of 0.81, meaning it is the most likely to win its first medal.

<!-- b003918 | prose | pages [13] -->
m

<!-- b003919 | prose | pages [13] -->
m

<!-- b003920 | prose | pages [13] -->
m

<!-- b003921 | prose | pages [13] -->
m

<!-- b003922 | prose | pages [13] -->
m

<!-- b003923 | prose | pages [13] -->
m

<!-- b003924 | prose | pages [13] -->
m

<!-- b003925 | prose | pages [13] -->
m

<!-- b003926 | prose | pages [13] -->
m

<!-- b003927 | prose | pages [13] -->
m

<!-- b003928 | prose | pages [13] -->
m

<!-- b003929 | prose | pages [13] -->
m

<!-- b003930 | prose | pages [13] -->
m

<!-- b003931 | prose | pages [13] -->
m

<!-- b003932 | prose | pages [13] -->
m

<!-- b003933 | prose | pages [13] -->
m

<!-- b003934 | prose | pages [13] -->
m

<!-- b003935 | prose | pages [13] -->
m

<!-- b003936 | prose | pages [13] -->
m

<!-- b003937 | prose | pages [13] -->
m

<!-- b003938 | prose | pages [13] -->
m

<!-- b003939 | prose | pages [13] -->
m

<!-- b003940 | prose | pages [13] -->
m

<!-- b003941 | prose | pages [13] -->
m

<!-- b003942 | prose | pages [13] -->
m

<!-- b003943 | prose | pages [13] -->
m

<!-- b003944 | prose | pages [13] -->
m

<!-- b003945 | prose | pages [13] -->
m

<!-- b003946 | prose | pages [13] -->
m

<!-- b003947 | prose | pages [13] -->
m

<!-- b003948 | prose | pages [13] -->
m

<!-- b003949 | prose | pages [13] -->
m

<!-- b003950 | prose | pages [13] -->
m

<!-- b003951 | prose | pages [13] -->
m

<!-- b003952 | prose | pages [13] -->
m

<!-- b003953 | prose | pages [13] -->
m

<!-- b003954 | prose | pages [13] -->
m

<!-- b003955 | prose | pages [13] -->
m

<!-- b003956 | prose | pages [13] -->
m

<!-- b003957 | prose | pages [13] -->
m

<!-- b003958 | prose | pages [13] -->
m

<!-- b003959 | prose | pages [13] -->
m

<!-- b003960 | prose | pages [13] -->
m

<!-- b003961 | prose | pages [13] -->
m

<!-- b003962 | prose | pages [13] -->
m

<!-- b003963 | prose | pages [13] -->
m

<!-- b003964 | prose | pages [13] -->
m

<!-- b003965 | prose | pages [13] -->
m

<!-- b003966 | prose | pages [13] -->
m

<!-- b003967 | prose | pages [13] -->
m

<!-- b003968 | prose | pages [13] -->
m

<!-- b003969 | prose | pages [13] -->
m

<!-- b003970 | prose | pages [13] -->
m

<!-- b003971 | prose | pages [13] -->
m

<!-- b003972 | prose | pages [13] -->
m

<!-- b003973 | prose | pages [13] -->
m

<!-- b003974 | prose | pages [13] -->
m

<!-- b003975 | prose | pages [13] -->
m

<!-- b003976 | prose | pages [13] -->
m

<!-- b003977 | prose | pages [13] -->
m

<!-- b003978 | prose | pages [13] -->
m

<!-- b003979 | prose | pages [13] -->
m

<!-- b003980 | prose | pages [13] -->
m

<!-- b003981 | prose | pages [13] -->
m

<!-- b003982 | prose | pages [13] -->
m

<!-- b003983 | prose | pages [13] -->
m

<!-- b003984 | prose | pages [13] -->
m

<!-- b003985 | prose | pages [13] -->
m

<!-- b003986 | prose | pages [13] -->
m

<!-- b003987 | prose | pages [13] -->
m

<!-- b003988 | prose | pages [13] -->
m

<!-- b003989 | prose | pages [13] -->
m

<!-- b003990 | prose | pages [13] -->
m

<!-- b003991 | prose | pages [13] -->
m

<!-- b003992 | prose | pages [13] -->
m

<!-- b003993 | prose | pages [13] -->
m

<!-- b003994 | prose | pages [13] -->
m

<!-- b003995 | prose | pages [13] -->
m

<!-- b003996 | prose | pages [13] -->
m

<!-- b003997 | prose | pages [13] -->
m

<!-- b003998 | prose | pages [13] -->
m

<!-- b003999 | prose | pages [13] -->
m

<!-- b004000 | prose | pages [13] -->
m

<!-- b004001 | prose | pages [13] -->
m

<!-- b004002 | prose | pages [13] -->
m

<!-- b004003 | prose | pages [13] -->
m

<!-- b004004 | prose | pages [13] -->
m

<!-- b004005 | prose | pages [13] -->
m

<!-- b004006 | prose | pages [13] -->
m

<!-- b004007 | prose | pages [13] -->
m

<!-- b004008 | prose | pages [13] -->
m

<!-- b004009 | prose | pages [13] -->
m

<!-- b004010 | prose | pages [13] -->
m

<!-- b004011 | prose | pages [13] -->
m

<!-- b004012 | prose | pages [13] -->
m

<!-- b004013 | prose | pages [13] -->
m

<!-- b004014 | prose | pages [13] -->
m

<!-- b004015 | prose | pages [13] -->
m

<!-- b004016 | prose | pages [13] -->
m

<!-- b004017 | prose | pages [13] -->
m

<!-- b004018 | prose | pages [13] -->
m

<!-- b004019 | prose | pages [13] -->
m

<!-- b004020 | prose | pages [13] -->
m

<!-- b004021 | prose | pages [13] -->
m

<!-- b004022 | prose | pages [13] -->
m

<!-- b004023 | prose | pages [13] -->
m

<!-- b004024 | prose | pages [13] -->
m

<!-- b004025 | prose | pages [13] -->
m

<!-- b004026 | prose | pages [13] -->
m

<!-- b004027 | prose | pages [13] -->
m

<!-- b004028 | prose | pages [13] -->
m

<!-- b004029 | prose | pages [13] -->
m

<!-- b004030 | prose | pages [13] -->
m

<!-- b004031 | prose | pages [13] -->
m

<!-- b004032 | prose | pages [13] -->
m

<!-- b004033 | prose | pages [13] -->
m

<!-- b004034 | prose | pages [13] -->
m

<!-- b004035 | prose | pages [13] -->
m

<!-- b004036 | prose | pages [13] -->
m

<!-- b004037 | prose | pages [13] -->
m

<!-- b004038 | prose | pages [13] -->
m

<!-- b004039 | prose | pages [13] -->
m

<!-- b004040 | prose | pages [13] -->
m

<!-- b004041 | prose | pages [13] -->
m

<!-- b004042 | prose | pages [13] -->
m

<!-- b004043 | prose | pages [13] -->
m

<!-- b004044 | prose | pages [13] -->
m

<!-- b004045 | prose | pages [13] -->
m

<!-- b004046 | prose | pages [13] -->
m

<!-- b004047 | prose | pages [13] -->
m

<!-- b004048 | prose | pages [13] -->
m

<!-- b004049 | prose | pages [13] -->
m

<!-- b004050 | prose | pages [13] -->
m

<!-- b004051 | prose | pages [13] -->
m

<!-- b004052 | prose | pages [13] -->
m

<!-- b004053 | prose | pages [13] -->
m

<!-- b004054 | prose | pages [13] -->
m

<!-- b004055 | prose | pages [13] -->
m

<!-- b004056 | prose | pages [13] -->
m

<!-- b004057 | prose | pages [13] -->
m

<!-- b004058 | prose | pages [13] -->
m

<!-- b004059 | prose | pages [13] -->
m

<!-- b004060 | prose | pages [13] -->
m

<!-- b004061 | prose | pages [13] -->
m

<!-- b004062 | prose | pages [13] -->
m

<!-- b004063 | prose | pages [13] -->
m

<!-- b004064 | prose | pages [13] -->
m

<!-- b004065 | prose | pages [13] -->
m

<!-- b004066 | prose | pages [13] -->
m

<!-- b004067 | prose | pages [13] -->
m

<!-- b004068 | prose | pages [13] -->
m

<!-- b004069 | prose | pages [13] -->
m

<!-- b004070 | prose | pages [13] -->
m

<!-- b004071 | prose | pages [13] -->
m

<!-- b004072 | prose | pages [13] -->
m

<!-- b004073 | prose | pages [13] -->
m

<!-- b004074 | prose | pages [13] -->
m

<!-- b004075 | prose | pages [13] -->
m

<!-- b004076 | prose | pages [13] -->
m

<!-- b004077 | prose | pages [13] -->
m

<!-- b004078 | prose | pages [13] -->
m

<!-- b004079 | prose | pages [13] -->
m

<!-- b004080 | prose | pages [13] -->
m

<!-- b004081 | prose | pages [13] -->
m

<!-- b004082 | prose | pages [13] -->
m

<!-- b004083 | prose | pages [13] -->
m

<!-- b004084 | prose | pages [13] -->
m

<!-- b004085 | furniture | pages [13] -->


<!-- b004086 | prose | pages [13] -->
m

<!-- b004087 | prose | pages [13] -->
m

<!-- b004088 | prose | pages [13] -->
m

<!-- b004089 | prose | pages [13] -->
m

<!-- b004090 | prose | pages [13] -->
m

<!-- b004091 | prose | pages [13] -->
m

<!-- b004092 | prose | pages [13] -->
m

<!-- b004093 | prose | pages [13] -->
m

<!-- b004094 | prose | pages [13] -->
m

<!-- b004095 | prose | pages [13] -->
m

<!-- b004096 | prose | pages [13] -->
m

<!-- b004097 | prose | pages [13] -->
m

<!-- b004098 | prose | pages [13] -->
m

<!-- b004099 | prose | pages [13] -->
m

<!-- b004100 | prose | pages [13] -->
m

<!-- b004101 | prose | pages [13] -->
m

<!-- b004102 | prose | pages [13] -->
m

<!-- b004103 | prose | pages [13] -->
m

<!-- b004104 | prose | pages [13] -->
m

<!-- b004105 | prose | pages [13] -->
m

<!-- b004106 | prose | pages [13] -->
m

<!-- b004107 | prose | pages [13] -->
m

<!-- b004108 | prose | pages [13] -->
m

<!-- b004109 | prose | pages [13] -->
m

<!-- b004110 | prose | pages [13] -->
m

<!-- b004111 | prose | pages [13] -->
m

<!-- b004112 | prose | pages [13] -->
m

<!-- b004113 | prose | pages [13] -->
m

<!-- b004114 | prose | pages [13] -->
m

<!-- b004115 | prose | pages [13] -->
m

<!-- b004116 | prose | pages [13] -->
m

<!-- b004117 | prose | pages [13] -->
m

<!-- b004118 | prose | pages [13] -->
m

<!-- b004119 | prose | pages [13] -->
m

<!-- b004120 | prose | pages [13] -->
m

<!-- b004121 | prose | pages [13] -->
m

<!-- b004122 | prose | pages [13] -->
m

<!-- b004123 | prose | pages [13] -->
m

<!-- b004124 | prose | pages [13] -->
m

<!-- b004125 | prose | pages [13] -->
m

<!-- b004126 | prose | pages [13] -->
m

<!-- b004127 | prose | pages [13] -->
m

<!-- b004128 | prose | pages [13] -->
m

<!-- b004129 | prose | pages [13] -->
m

<!-- b004130 | prose | pages [13] -->
m

<!-- b004131 | prose | pages [13] -->
m

<!-- b004132 | prose | pages [13] -->
m

<!-- b004133 | prose | pages [13] -->
m

<!-- b004134 | prose | pages [13] -->
m

<!-- b004135 | prose | pages [13] -->
m

<!-- b004136 | prose | pages [13] -->
m

<!-- b004137 | prose | pages [13] -->
m

<!-- b004138 | prose | pages [13] -->
m

<!-- b004139 | prose | pages [13] -->
m

<!-- b004140 | prose | pages [13] -->
m

<!-- b004141 | prose | pages [13] -->
m

<!-- b004142 | prose | pages [13] -->
m

<!-- b004143 | prose | pages [13] -->
m

<!-- b004144 | prose | pages [13] -->
m

<!-- b004145 | prose | pages [13] -->
m

<!-- b004146 | prose | pages [13] -->
m

<!-- b004147 | prose | pages [13] -->
m

<!-- b004148 | prose | pages [13] -->
m

<!-- b004149 | prose | pages [13] -->
m

<!-- b004150 | prose | pages [13] -->
m

<!-- b004151 | prose | pages [13] -->
m

<!-- b004152 | prose | pages [13] -->
m

<!-- b004153 | prose | pages [13] -->
m

<!-- b004154 | prose | pages [13] -->
m

<!-- b004155 | prose | pages [13] -->
m

<!-- b004156 | prose | pages [13] -->
m

<!-- b004157 | prose | pages [13] -->
m

<!-- b004158 | prose | pages [13] -->
m

<!-- b004159 | prose | pages [13] -->
m

<!-- b004160 | prose | pages [13] -->
m

<!-- b004161 | prose | pages [13] -->
m

<!-- b004162 | prose | pages [13] -->
m

<!-- b004163 | prose | pages [13] -->
m

<!-- b004164 | prose | pages [13] -->
m

<!-- b004165 | prose | pages [13] -->
m

<!-- b004166 | prose | pages [13] -->
m

<!-- b004167 | prose | pages [13] -->
m

<!-- b004168 | prose | pages [13] -->
m

<!-- b004169 | prose | pages [13] -->
m

<!-- b004170 | prose | pages [13] -->
m

<!-- b004171 | prose | pages [13] -->
m

<!-- b004172 | prose | pages [13] -->
m

<!-- b004173 | prose | pages [13] -->
m

<!-- b004174 | prose | pages [13] -->
m

<!-- b004175 | prose | pages [13] -->
m

<!-- b004176 | prose | pages [13] -->
m

<!-- b004177 | prose | pages [13] -->
m

<!-- b004178 | prose | pages [13] -->
m

<!-- b004179 | prose | pages [13] -->
m

<!-- b004180 | prose | pages [13] -->
m

<!-- b004181 | prose | pages [13] -->
m

<!-- b004182 | prose | pages [13] -->
m

<!-- b004183 | prose | pages [13] -->
m

<!-- b004184 | prose | pages [13] -->
m

<!-- b004185 | prose | pages [13] -->
m

<!-- b004186 | prose | pages [13] -->
m

<!-- b004187 | prose | pages [13] -->
m

<!-- b004188 | prose | pages [13] -->
m

<!-- b004189 | prose | pages [13] -->
m

<!-- b004190 | prose | pages [13] -->
m

<!-- b004191 | prose | pages [13] -->
m

<!-- b004192 | prose | pages [13] -->
m

<!-- b004193 | prose | pages [13] -->
m

<!-- b004194 | prose | pages [13] -->
m

<!-- b004195 | prose | pages [13] -->
m

<!-- b004196 | prose | pages [13] -->
m

<!-- b004197 | prose | pages [13] -->
m

<!-- b004198 | prose | pages [13] -->
m

<!-- b004199 | prose | pages [13] -->
m

<!-- b004200 | prose | pages [13] -->
m

<!-- b004201 | prose | pages [13] -->
m

<!-- b004202 | prose | pages [13] -->
m

<!-- b004203 | furniture | pages [13] -->
m

<!-- b004204 | furniture | pages [13] -->
m

<!-- b004205 | furniture | pages [13] -->
m

<!-- b004206 | furniture | pages [13] -->
m

<!-- b004207 | furniture | pages [13] -->
m

<!-- b004208 | furniture | pages [13] -->
m

<!-- b004209 | furniture | pages [13] -->
m

<!-- b004210 | furniture | pages [13] -->
m

<!-- b004211 | furniture | pages [13] -->
m

<!-- b004212 | furniture | pages [13] -->
m

<!-- b004213 | furniture | pages [13] -->
m

<!-- b004214 | furniture | pages [13] -->
m

<!-- b004215 | furniture | pages [13] -->
m

<!-- b004216 | furniture | pages [13] -->
m

<!-- b004217 | furniture | pages [13] -->
m

<!-- b004218 | furniture | pages [13] -->
m

<!-- b004219 | furniture | pages [13] -->
m

<!-- b004220 | furniture | pages [13] -->
m

<!-- b004221 | furniture | pages [13] -->
m

<!-- b004222 | furniture | pages [13] -->
m

<!-- b004223 | furniture | pages [13] -->
m

<!-- b004224 | furniture | pages [13] -->
m

<!-- b004225 | furniture | pages [13] -->
m

<!-- b004226 | furniture | pages [13] -->
m

<!-- b004227 | furniture | pages [13] -->
m

<!-- b004228 | furniture | pages [13] -->
m

<!-- b004229 | furniture | pages [13] -->
m

<!-- b004230 | furniture | pages [13] -->
m

<!-- b004231 | furniture | pages [13] -->
m

<!-- b004232 | furniture | pages [13] -->
m

<!-- b004233 | furniture | pages [13] -->
m

<!-- b004234 | furniture | pages [13] -->
m

<!-- b004235 | furniture | pages [13] -->
m

<!-- b004236 | furniture | pages [13] -->
m

<!-- b004237 | furniture | pages [13] -->
m

<!-- b004238 | furniture | pages [13] -->
m

<!-- b004239 | furniture | pages [13] -->
m

<!-- b004240 | furniture | pages [13] -->
m

<!-- b004241 | furniture | pages [13] -->
m

<!-- b004242 | furniture | pages [13] -->
m

<!-- b004243 | furniture | pages [13] -->
m

<!-- b004244 | furniture | pages [13] -->
m

<!-- b004245 | furniture | pages [13] -->
m

<!-- b004246 | furniture | pages [13] -->
m

<!-- b004247 | furniture | pages [13] -->
m

<!-- b004248 | furniture | pages [13] -->
m

<!-- b004249 | furniture | pages [13] -->
m

<!-- b004250 | furniture | pages [13] -->
m

<!-- b004251 | furniture | pages [13] -->
m

<!-- b004252 | furniture | pages [13] -->
m

<!-- b004253 | furniture | pages [13] -->
m

<!-- b004254 | furniture | pages [13] -->
m

<!-- b004255 | furniture | pages [13] -->
m

<!-- b004256 | furniture | pages [13] -->
m

<!-- b004257 | furniture | pages [13] -->
m

<!-- b004258 | furniture | pages [13] -->
m

<!-- b004259 | furniture | pages [13] -->
m

<!-- b004260 | furniture | pages [13] -->
m

<!-- b004261 | furniture | pages [13] -->
m

<!-- b004262 | furniture | pages [13] -->
m

<!-- b004263 | furniture | pages [13] -->
m

<!-- b004264 | furniture | pages [13] -->
m

<!-- b004265 | furniture | pages [13] -->
m

<!-- b004266 | furniture | pages [13] -->
m

<!-- b004267 | furniture | pages [13] -->
m

<!-- b004268 | furniture | pages [13] -->
m

<!-- b004269 | furniture | pages [13] -->
m

<!-- b004270 | furniture | pages [13] -->
m

<!-- b004271 | furniture | pages [13] -->
m

<!-- b004272 | furniture | pages [13] -->
m

<!-- b004273 | furniture | pages [13] -->
m

<!-- b004274 | furniture | pages [13] -->
m

<!-- b004275 | furniture | pages [13] -->
m

<!-- b004276 | furniture | pages [13] -->
m

<!-- b004277 | furniture | pages [13] -->
m

<!-- b004278 | furniture | pages [13] -->
m

<!-- b004279 | furniture | pages [13] -->
m

<!-- b004280 | furniture | pages [13] -->
m

<!-- b004281 | furniture | pages [13] -->
m

<!-- b004282 | furniture | pages [13] -->
m

<!-- b004283 | furniture | pages [13] -->
m

<!-- b004284 | furniture | pages [13] -->
m

<!-- b004285 | furniture | pages [13] -->
m

<!-- b004286 | furniture | pages [13] -->
m

<!-- b004287 | furniture | pages [13] -->
m

<!-- b004288 | furniture | pages [13] -->
m

<!-- b004289 | furniture | pages [13] -->
m

<!-- b004290 | furniture | pages [13] -->
m

<!-- b004291 | furniture | pages [13] -->
m

<!-- b004292 | furniture | pages [13] -->
m

<!-- b004293 | furniture | pages [13] -->
m

<!-- b004294 | furniture | pages [13] -->
m

<!-- b004295 | furniture | pages [13] -->
m

<!-- b004296 | furniture | pages [13] -->
m

<!-- b004297 | furniture | pages [13] -->
m

<!-- b004298 | furniture | pages [13] -->
m

<!-- b004299 | furniture | pages [13] -->
m

<!-- b004300 | furniture | pages [13] -->
m

<!-- b004301 | furniture | pages [13] -->
m

<!-- b004302 | furniture | pages [13] -->
m

<!-- b004303 | furniture | pages [13] -->
m

<!-- b004304 | furniture | pages [13] -->
m

<!-- b004305 | furniture | pages [13] -->
m

<!-- b004306 | furniture | pages [13] -->
m

<!-- b004307 | furniture | pages [13] -->
m

<!-- b004308 | furniture | pages [13] -->
m

<!-- b004309 | furniture | pages [13] -->
m

<!-- b004310 | furniture | pages [13] -->
m

<!-- b004311 | furniture | pages [13] -->
m

<!-- b004312 | furniture | pages [13] -->
m

<!-- b004313 | furniture | pages [13] -->
m

<!-- b004314 | furniture | pages [13] -->
m

<!-- b004315 | furniture | pages [13] -->
m

<!-- b004316 | furniture | pages [13] -->
m

<!-- b004317 | furniture | pages [13] -->
m

<!-- b004318 | furniture | pages [13] -->
m

<!-- b004319 | furniture | pages [13] -->
m

<!-- b004320 | furniture | pages [13] -->
m

<!-- b004321 | furniture | pages [13] -->
m

<!-- b004322 | furniture | pages [13] -->
m

<!-- b004323 | furniture | pages [13] -->
m

<!-- b004324 | furniture | pages [13] -->
m

<!-- b004325 | furniture | pages [13] -->
m

<!-- b004326 | furniture | pages [13] -->
m

<!-- b004327 | furniture | pages [13] -->
m

<!-- b004328 | furniture | pages [13] -->
m

<!-- b004329 | furniture | pages [13] -->
m

<!-- b004330 | furniture | pages [13] -->
m

<!-- b004331 | furniture | pages [13] -->
m

<!-- b004332 | furniture | pages [13] -->
m

<!-- b004333 | furniture | pages [13] -->
m

<!-- b004334 | furniture | pages [13] -->
m

<!-- b004335 | furniture | pages [13] -->
m

<!-- b004336 | furniture | pages [13] -->
m

<!-- b004337 | furniture | pages [13] -->
m

<!-- b004338 | furniture | pages [13] -->
m

<!-- b004339 | furniture | pages [13] -->
m

<!-- b004340 | furniture | pages [13] -->
m

<!-- b004341 | furniture | pages [13] -->
m

<!-- b004342 | furniture | pages [13] -->
m

<!-- b004343 | furniture | pages [13] -->
m

<!-- b004344 | furniture | pages [13] -->
m

<!-- b004345 | furniture | pages [13] -->
m

<!-- b004346 | furniture | pages [13] -->
m

<!-- b004347 | furniture | pages [13] -->
m

<!-- b004348 | furniture | pages [13] -->
m

<!-- b004349 | furniture | pages [13] -->
m

<!-- b004350 | furniture | pages [13] -->
m

<!-- b004351 | furniture | pages [13] -->
m

<!-- b004352 | furniture | pages [13] -->
m

<!-- b004353 | furniture | pages [13] -->
m

<!-- b004354 | furniture | pages [13] -->
m

<!-- b004355 | furniture | pages [13] -->
m

<!-- b004356 | furniture | pages [13] -->
m

<!-- b004357 | furniture | pages [13] -->
m

<!-- b004358 | furniture | pages [13] -->
m

<!-- b004359 | furniture | pages [13] -->
m

<!-- b004360 | furniture | pages [13] -->
m

<!-- b004361 | furniture | pages [13] -->
m

<!-- b004362 | furniture | pages [13] -->
m

<!-- b004363 | furniture | pages [13] -->
m

<!-- b004364 | furniture | pages [13] -->
m

<!-- b004365 | furniture | pages [13] -->
m

<!-- b004366 | furniture | pages [13] -->
m

<!-- b004367 | furniture | pages [13] -->
m

<!-- b004368 | furniture | pages [13] -->
m

<!-- b004369 | furniture | pages [13] -->
m

<!-- b004370 | furniture | pages [13] -->
m

<!-- b004371 | furniture | pages [13] -->
m

<!-- b004372 | furniture | pages [13] -->
m

<!-- b004373 | furniture | pages [13] -->
m

<!-- b004374 | furniture | pages [13] -->
m

<!-- b004375 | furniture | pages [13] -->
m

<!-- b004376 | furniture | pages [13] -->
m

<!-- b004377 | furniture | pages [13] -->
m

<!-- b004378 | furniture | pages [13] -->
m

<!-- b004379 | furniture | pages [13] -->
m

<!-- b004380 | furniture | pages [13] -->
m

<!-- b004381 | furniture | pages [13] -->
m

<!-- b004382 | furniture | pages [13] -->
m

<!-- b004383 | furniture | pages [13] -->
m

<!-- b004384 | furniture | pages [13] -->
m

<!-- b004385 | furniture | pages [13] -->
m

<!-- b004386 | furniture | pages [13] -->
m

<!-- b004387 | furniture | pages [13] -->
m

<!-- b004388 | furniture | pages [13] -->
m

<!-- b004389 | furniture | pages [13] -->
m

<!-- b004390 | furniture | pages [13] -->
m

<!-- b004391 | furniture | pages [13] -->
m

<!-- b004392 | furniture | pages [13] -->
m

<!-- b004393 | furniture | pages [13] -->
m

<!-- b004394 | furniture | pages [13] -->
m

<!-- b004395 | furniture | pages [13] -->
m

<!-- b004396 | furniture | pages [13] -->
m

<!-- b004397 | furniture | pages [13] -->
m

<!-- b004398 | furniture | pages [13] -->
m

<!-- b004399 | furniture | pages [13] -->
m

<!-- b004400 | furniture | pages [13] -->
m

<!-- b004401 | furniture | pages [13] -->
m

<!-- b004402 | furniture | pages [13] -->
m

<!-- b004403 | furniture | pages [13] -->
m

<!-- b004404 | furniture | pages [13] -->
m

<!-- b004405 | furniture | pages [13] -->
m

<!-- b004406 | furniture | pages [13] -->
m

<!-- b004407 | furniture | pages [13] -->
m

<!-- b004408 | furniture | pages [13] -->
m

<!-- b004409 | furniture | pages [13] -->
m

<!-- b004410 | furniture | pages [13] -->
m

<!-- b004411 | furniture | pages [13] -->
m

<!-- b004412 | furniture | pages [13] -->
m

<!-- b004413 | furniture | pages [13] -->
m

<!-- b004414 | furniture | pages [13] -->
m

<!-- b004415 | furniture | pages [13] -->
m

<!-- b004416 | furniture | pages [13] -->
m

<!-- b004417 | furniture | pages [13] -->
m

<!-- b004418 | furniture | pages [13] -->
m

<!-- b004419 | furniture | pages [13] -->
m

<!-- b004420 | furniture | pages [13] -->
m

<!-- b004421 | furniture | pages [13] -->
m

<!-- b004422 | furniture | pages [13] -->
m

<!-- b004423 | furniture | pages [13] -->
m

<!-- b004424 | furniture | pages [13] -->
m

<!-- b004425 | furniture | pages [13] -->
m

<!-- b004426 | furniture | pages [13] -->
m

<!-- b004427 | furniture | pages [13] -->
m

<!-- b004428 | furniture | pages [13] -->
m

<!-- b004429 | furniture | pages [13] -->
m

<!-- b004430 | furniture | pages [13] -->
m

<!-- b004431 | furniture | pages [13] -->
m

<!-- b004432 | furniture | pages [13] -->
m

<!-- b004433 | furniture | pages [13] -->
m

<!-- b004434 | furniture | pages [13] -->
m

<!-- b004435 | furniture | pages [13] -->
m

<!-- b004436 | furniture | pages [13] -->
m

<!-- b004437 | furniture | pages [13] -->
m

<!-- b004438 | furniture | pages [13] -->
m

<!-- b004439 | furniture | pages [13] -->
m

<!-- b004440 | furniture | pages [13] -->
m

<!-- b004441 | furniture | pages [13] -->
m

<!-- b004442 | furniture | pages [13] -->
m

<!-- b004443 | furniture | pages [13] -->
m

<!-- b004444 | furniture | pages [13] -->
m

<!-- b004445 | furniture | pages [13] -->
m

<!-- b004446 | furniture | pages [13] -->
m

<!-- b004447 | furniture | pages [13] -->
m

<!-- b004448 | furniture | pages [13] -->
m

<!-- b004449 | furniture | pages [13] -->
m

<!-- b004450 | furniture | pages [13] -->
m

<!-- b004451 | furniture | pages [13] -->
m

<!-- b004452 | furniture | pages [13] -->
m

<!-- b004453 | furniture | pages [13] -->
m

<!-- b004454 | furniture | pages [13] -->
m

<!-- b004455 | furniture | pages [13] -->
m

<!-- b004456 | furniture | pages [13] -->
m

<!-- b004457 | furniture | pages [13] -->
m

<!-- b004458 | furniture | pages [13] -->
m

<!-- b004459 | furniture | pages [13] -->
m

<!-- b004460 | furniture | pages [13] -->
m

<!-- b004461 | furniture | pages [13] -->
m

<!-- b004462 | furniture | pages [13] -->
m

<!-- b004463 | furniture | pages [13] -->
m

<!-- b004464 | furniture | pages [13] -->
m

<!-- b004465 | furniture | pages [13] -->
m

<!-- b004466 | furniture | pages [13] -->
m

<!-- b004467 | furniture | pages [13] -->
m

<!-- b004468 | furniture | pages [13] -->
m

<!-- b004469 | furniture | pages [13] -->
m

<!-- b004470 | furniture | pages [13] -->
m

<!-- b004471 | furniture | pages [13] -->
m

<!-- b004472 | furniture | pages [13] -->
m

<!-- b004473 | furniture | pages [13] -->
m

<!-- b004474 | furniture | pages [13] -->
m

<!-- b004475 | furniture | pages [13] -->
m

<!-- b004476 | furniture | pages [13] -->
m

<!-- b004477 | furniture | pages [13] -->
m

<!-- b004478 | furniture | pages [13] -->
m

<!-- b004479 | furniture | pages [13] -->
m

<!-- b004480 | furniture | pages [13] -->
m

<!-- b004481 | furniture | pages [13] -->
m

<!-- b004482 | furniture | pages [13] -->
m

<!-- b004483 | furniture | pages [13] -->
m

<!-- b004484 | furniture | pages [13] -->
m

<!-- b004485 | furniture | pages [13] -->
m

<!-- b004486 | furniture | pages [13] -->
m

<!-- b004487 | furniture | pages [13] -->
m

<!-- b004488 | furniture | pages [13] -->
m

<!-- b004489 | furniture | pages [13] -->
m

<!-- b004490 | furniture | pages [13] -->
m

<!-- b004491 | furniture | pages [13] -->
m

<!-- b004492 | furniture | pages [13] -->
m

<!-- b004493 | furniture | pages [13] -->
m

<!-- b004494 | furniture | pages [13] -->
m

<!-- b004495 | furniture | pages [13] -->
m

<!-- b004496 | furniture | pages [13] -->
m

<!-- b004497 | furniture | pages [13] -->
m

<!-- b004498 | furniture | pages [13] -->
m

<!-- b004499 | furniture | pages [13] -->
m

<!-- b004500 | furniture | pages [13] -->
m

<!-- b004501 | furniture | pages [13] -->
m

<!-- b004502 | furniture | pages [13] -->
m

<!-- b004503 | furniture | pages [13] -->
m

<!-- b004504 | furniture | pages [13] -->
m

<!-- b004505 | furniture | pages [13] -->
m

<!-- b004506 | furniture | pages [13] -->
m

<!-- b004507 | furniture | pages [13] -->
m

<!-- b004508 | furniture | pages [13] -->
m

<!-- b004509 | furniture | pages [13] -->
m

<!-- b004510 | furniture | pages [13] -->
m

<!-- b004511 | furniture | pages [13] -->
m

<!-- b004512 | furniture | pages [13] -->
m

<!-- b004513 | furniture | pages [13] -->
m

<!-- b004514 | furniture | pages [13] -->
m

<!-- b004515 | furniture | pages [13] -->
m

<!-- b004516 | furniture | pages [13] -->
m

<!-- b004517 | furniture | pages [13] -->
m

<!-- b004518 | furniture | pages [13] -->
m

<!-- b004519 | furniture | pages [13] -->
m

<!-- b004520 | furniture | pages [13] -->
m

<!-- b004521 | furniture | pages [13] -->
m

<!-- b004522 | furniture | pages [13] -->
m

<!-- b004523 | furniture | pages [13] -->
m

<!-- b004524 | furniture | pages [13] -->
m

<!-- b004525 | furniture | pages [13] -->
m

<!-- b004526 | furniture | pages [13] -->
m

<!-- b004527 | furniture | pages [13] -->
m

<!-- b004528 | furniture | pages [13] -->
m

<!-- b004529 | furniture | pages [13] -->
m

<!-- b004530 | furniture | pages [13] -->
m

<!-- b004531 | furniture | pages [13] -->
m

<!-- b004532 | furniture | pages [13] -->
m

<!-- b004533 | furniture | pages [13] -->
m

<!-- b004534 | furniture | pages [13] -->
m

<!-- b004535 | furniture | pages [13] -->
m

<!-- b004536 | furniture | pages [13] -->
m

<!-- b004537 | furniture | pages [13] -->
m

<!-- b004538 | furniture | pages [13] -->
m

<!-- b004539 | furniture | pages [13] -->
m

<!-- b004540 | furniture | pages [13] -->
m

<!-- b004541 | furniture | pages [13] -->
m

<!-- b004542 | furniture | pages [13] -->
m

<!-- b004543 | furniture | pages [13] -->
m

<!-- b004544 | furniture | pages [13] -->
m

<!-- b004545 | furniture | pages [13] -->
m

<!-- b004546 | furniture | pages [13] -->
m

<!-- b004547 | furniture | pages [13] -->
m

<!-- b004548 | furniture | pages [13] -->
m

<!-- b004549 | furniture | pages [13] -->
m

<!-- b004550 | furniture | pages [13] -->
m

<!-- b004551 | furniture | pages [13] -->
m

<!-- b004552 | furniture | pages [13] -->
m

<!-- b004553 | furniture | pages [13] -->
m

<!-- b004554 | furniture | pages [13] -->
m

<!-- b004555 | furniture | pages [13] -->
m

<!-- b004556 | furniture | pages [13] -->
m

<!-- b004557 | furniture | pages [13] -->
m

<!-- b004558 | furniture | pages [13] -->
m

<!-- b004559 | furniture | pages [13] -->
m

<!-- b004560 | furniture | pages [13] -->
m

<!-- b004561 | furniture | pages [13] -->
m

<!-- b004562 | furniture | pages [13] -->
m

<!-- b004563 | furniture | pages [13] -->
m

<!-- b004564 | furniture | pages [13] -->
m

<!-- b004565 | furniture | pages [13] -->
m

<!-- b004566 | furniture | pages [13] -->
m

<!-- b004567 | furniture | pages [13] -->
m

<!-- b004568 | furniture | pages [13] -->
m

<!-- b004569 | furniture | pages [13] -->
m

<!-- b004570 | furniture | pages [13] -->
m

<!-- b004571 | furniture | pages [13] -->
m

<!-- b004572 | furniture | pages [13] -->
m

<!-- b004573 | furniture | pages [13] -->
m

<!-- b004574 | furniture | pages [13] -->
m

<!-- b004575 | furniture | pages [13] -->
m

<!-- b004576 | furniture | pages [13] -->
m

<!-- b004577 | furniture | pages [13] -->
m

<!-- b004578 | furniture | pages [13] -->
m

<!-- b004579 | furniture | pages [13] -->
m

<!-- b004580 | furniture | pages [13] -->
m

<!-- b004581 | furniture | pages [13] -->
m

<!-- b004582 | furniture | pages [13] -->
m

<!-- b004583 | furniture | pages [13] -->
m

<!-- b004584 | furniture | pages [13] -->
m

<!-- b004585 | furniture | pages [13] -->
m

<!-- b004586 | furniture | pages [13] -->
m

<!-- b004587 | furniture | pages [13] -->
m

<!-- b004588 | furniture | pages [13] -->
m

<!-- b004589 | furniture | pages [13] -->
m

<!-- b004590 | furniture | pages [13] -->
m

<!-- b004591 | furniture | pages [13] -->
m

<!-- b004592 | furniture | pages [13] -->
m

<!-- b004593 | furniture | pages [13] -->
m

<!-- b004594 | furniture | pages [13] -->
m

<!-- b004595 | furniture | pages [13] -->
m

<!-- b004596 | furniture | pages [13] -->
m

<!-- b004597 | furniture | pages [13] -->
m

<!-- b004598 | furniture | pages [13] -->
m

<!-- b004599 | furniture | pages [13] -->
m

<!-- b004600 | furniture | pages [13] -->
m

<!-- b004601 | furniture | pages [13] -->
m

<!-- b004602 | furniture | pages [13] -->
m

<!-- b004603 | furniture | pages [13] -->
m

<!-- b004604 | furniture | pages [13] -->
m

<!-- b004605 | furniture | pages [13] -->
m

<!-- b004606 | furniture | pages [14] -->
Team 2517690

<!-- b004607 | furniture | pages [14] -->


<!-- b004608 | furniture | pages [14] -->


<!-- b004609 | furniture | pages [14] -->


<!-- b004610 | furniture | pages [14] -->


<!-- b004611 | furniture | pages [14] -->


<!-- b004612 | furniture | pages [14] -->


<!-- b004613 | furniture | pages [14] -->


<!-- b004614 | furniture | pages [14] -->


<!-- b004615 | furniture | pages [14] -->


<!-- b004616 | furniture | pages [14] -->


<!-- b004617 | furniture | pages [14] -->


<!-- b004618 | furniture | pages [14] -->


<!-- b004619 | furniture | pages [14] -->


<!-- b004620 | furniture | pages [14] -->


<!-- b004621 | furniture | pages [14] -->
Page 14 of 25

<!-- b004622 | heading | pages [14] -->
5.3 Analysis of Factors Influencing Country Medal Counts

<!-- b004623 | furniture | pages [14] -->


<!-- b004624 | caption | pages [14] -->
Figure 10:Analysis of factors influencing the number of medals

<!-- b004625 | heading | pages [14] -->
5.3.1 Analysis of the Influence of Olympic Events

<!-- b004626 | prose | pages [14] -->
(1) Analysis of the Medal Distribution of Olympic Events for Each Country Based on Radar Charts

<!-- b004627 | prose | pages [14] -->
To more intuitively display the medal distribution of each country in different Olympic events, this study uses radar charts as a visualization tool. Radar charts can effectively present multi-dimensional data and help compare the advantages and disadvantages of each country in various events. Taking the United States, China, and France as examples, the drawn radar charts are as follows:

<!-- b004628 | furniture | pages [14] -->


<!-- b004629 | caption | pages [14] -->
Figure 11:Radar chart analysing levels in selected sports

<!-- b004630 | prose | pages [14] -->
The above figure shows the performance differences among China, the United States, and France in five Olympic events. China stands out in swimming, wrestling, and diving, with par- ticularly obvious advantages in diving and wrestling. The United States takes a dominant po- sition in track and field and swimming, demonstrating its strong competitiveness in multiple events. France shows a relatively balanced performance, with certain advantages in shooting and swimming. Overall, it reflects the differences in competitiveness of the three countries in their respective advantageous events.

<!-- b004631 | furniture | pages [14] -->


<!-- b004632 | prose | pages [14] -->
关注数学模型

<!-- b004633 | furniture | pages [14] -->
2

<!-- b004634 | furniture | pages [14] -->
MATHmodels

<!-- b004635 | furniture | pages [14] -->
获取更多资讯

<!-- b004636 | furniture | pages [15] -->
Team 2517690

<!-- b004637 | furniture | pages [15] -->


<!-- b004638 | furniture | pages [15] -->


<!-- b004639 | furniture | pages [15] -->


<!-- b004640 | furniture | pages [15] -->


<!-- b004641 | furniture | pages [15] -->


<!-- b004642 | furniture | pages [15] -->


<!-- b004643 | furniture | pages [15] -->


<!-- b004644 | prose | pages [15] -->
(2) Grey Relational Analysis

<!-- b004645 | furniture | pages [15] -->


<!-- b004646 | furniture | pages [15] -->


<!-- b004647 | furniture | pages [15] -->


<!-- b004648 | furniture | pages [15] -->


<!-- b004649 | furniture | pages [15] -->


<!-- b004650 | furniture | pages [15] -->


<!-- b004651 | furniture | pages [15] -->


<!-- b004652 | furniture | pages [15] -->
Page 15 of 25

<!-- b004653 | prose | pages [15] -->
Grey Relational Analysis quantifies the degree of association between different factors by comparing their changing trends[5]. It is particularly suitable for situations with incomplete in- formation or uncertainty. This method identifies key influencing factors or conducts pattern recognition by calculating the degree of association. In this study, the number of medals in each sports event is regarded as a subsequence, and the total number of medals of each country is

<!-- b004654 | prose | pages [15] -->
微信公众号：数学模型

<!-- b004655 | prose | pages [15] -->
regarded as the mother sequence. The degree of association between each event and the total number of medals of each country is calculated, and the strength of their correlation is meas- ured by the value of the degree of association.

<!-- b004656 | prose | pages [15] -->
The analysis steps are as follows:： Step1: Determine the mother sequence and subsequences Suppose there are evaluation objects and

<!-- b004657 | prose | pages [15] -->
= = x x ( k ) k 2,1 ,..., n

<!-- b004658 | prose | pages [15] -->
evaluation indicators. The mother sequence

<!-- b004659 | prose | pages [15] -->
= = x x ( k ) k 2,1 ,..., m , and the subsequences are is 0 0

<!-- b004660 | prose | pages [15] -->
Step2: Preprocess the variables

<!-- b004661 | prose | pages [15] -->
. i i

<!-- b004662 | prose | pages [15] -->
Pre-process each indicator in the mother sequence and subsequences respectively. First,

<!-- b004663 | prose | pages [15] -->
微信号：MATHmodels

<!-- b004664 | prose | pages [15] -->
calculate the mean of each indicator, and then divide each element in the indicator by its mean. This can eliminate the influence of dimensions and narrow the range of variables to simplify calculations. Let the standardized matrix be Z, and the elements in Z be denoted as calculation formula is as follows:

<!-- b004665 | prose | pages [15] -->
Obtain the standardized matrix: Z

<!-- b004666 | prose | pages [15] -->


<!-- b004667 | prose | pages [15] -->
Z

<!-- b004668 | prose | pages [15] -->
11

<!-- b004669 | prose | pages [15] -->


<!-- b004670 | prose | pages [15] -->
Z

<!-- b004671 | prose | pages [15] -->


<!-- b004672 | prose | pages [15] -->
21

<!-- b004673 | prose | pages [15] -->
 

<!-- b004674 | prose | pages [15] -->
Z Z

<!-- b004675 | prose | pages [15] -->


<!-- b004676 | prose | pages [15] -->
n

<!-- b004677 | prose | pages [15] -->
1

<!-- b004678 | prose | pages [15] -->
, The

<!-- b004679 | prose | pages [15] -->
x

<!-- b004680 | prose | pages [15] -->
i

<!-- b004681 | prose | pages [15] -->
j

<!-- b004682 | prose | pages [15] -->
= Z Z

<!-- b004683 | prose | pages [15] -->
(11)

<!-- b004684 | furniture | pages [15] -->


<!-- b004685 | prose | pages [15] -->
i i

<!-- b004686 | prose | pages [15] -->
j j

<!-- b004687 | prose | pages [15] -->
x

<!-- b004688 | prose | pages [15] -->
i

<!-- b004689 | prose | pages [15] -->
j

<!-- b004690 | prose | pages [15] -->


<!-- b004691 | prose | pages [15] -->
Z Z Z

<!-- b004692 | prose | pages [15] -->
12 12 1

<!-- b004693 | prose | pages [15] -->
m

<!-- b004694 | prose | pages [15] -->


<!-- b004695 | prose | pages [15] -->
Z Z Z

<!-- b004696 | prose | pages [15] -->
(12)

<!-- b004697 | prose | pages [15] -->


<!-- b004698 | prose | pages [15] -->
22 22 2

<!-- b004699 | prose | pages [15] -->
m

<!-- b004700 | prose | pages [15] -->
 

<!-- b004701 | prose | pages [15] -->
Z

<!-- b004702 | prose | pages [15] -->


<!-- b004703 | prose | pages [15] -->
n n

<!-- b004704 | prose | pages [15] -->
2 2

<!-- b004705 | prose | pages [15] -->
nm

<!-- b004706 | prose | pages [15] -->
Step3: Calculate the correlation coefficients between each indicator in the subse- quences and the mother sequence

<!-- b004707 | furniture | pages [15] -->


<!-- b004708 | prose | pages [15] -->
+

<!-- b004709 | prose | pages [15] -->
 a b

<!-- b004710 | prose | pages [15] -->
=

<!-- b004711 | prose | pages [15] -->
y x k

<!-- b004712 | prose | pages [15] -->
( ( ),

<!-- b004713 | prose | pages [15] -->
x k

<!-- b004714 | prose | pages [15] -->
( )) 0 i

<!-- b004715 | prose | pages [15] -->
−

<!-- b004716 | prose | pages [15] -->
|

<!-- b004717 | prose | pages [15] -->
x k

<!-- b004718 | prose | pages [15] -->
( )

<!-- b004719 | prose | pages [15] -->
x k

<!-- b004720 | prose | pages [15] -->
( ) | 0

<!-- b004721 | prose | pages [15] -->
i

<!-- b004722 | prose | pages [15] -->
(13)

<!-- b004723 | prose | pages [15] -->
= =

<!-- b004724 | prose | pages [15] -->
(

<!-- b004725 | prose | pages [15] -->
i

<!-- b004726 | prose | pages [15] -->
1,2,

<!-- b004727 | prose | pages [15] -->
m k

<!-- b004728 | prose | pages [15] -->
, 1,2,

<!-- b004729 | prose | pages [15] -->
n

<!-- b004730 | prose | pages [15] -->
)

<!-- b004731 | prose | pages [15] -->
+ 

<!-- b004732 | prose | pages [15] -->
b

<!-- b004733 | furniture | pages [15] -->


<!-- b004734 | furniture | pages [15] -->


<!-- b004735 | prose | pages [15] -->
is the distinguishing coefficient, usually taken as 0.5. Among them, is the mini-

<!-- b004736 | prose | pages [15] -->
is the maximum difference of the two levels. The mum difference of the two levels, and calculation formulas are as follows:

<!-- b004737 | furniture | pages [15] -->


<!-- b004738 | prose | pages [15] -->
= −

<!-- b004739 | prose | pages [15] -->
min min |

<!-- b004740 | prose | pages [15] -->
a

<!-- b004741 | prose | pages [15] -->
i

<!-- b004742 | prose | pages [15] -->
=

<!-- b004743 | prose | pages [15] -->
x k

<!-- b004744 | prose | pages [15] -->
( )

<!-- b004745 | prose | pages [15] -->
x k

<!-- b004746 | prose | pages [15] -->
( ) |

<!-- b004747 | prose | pages [15] -->
(14)

<!-- b004748 | prose | pages [15] -->
0

<!-- b004749 | prose | pages [15] -->
i k k

<!-- b004750 | prose | pages [15] -->
−

<!-- b004751 | prose | pages [15] -->
max max |

<!-- b004752 | prose | pages [15] -->
b

<!-- b004753 | prose | pages [15] -->
i

<!-- b004754 | prose | pages [15] -->
x k

<!-- b004755 | prose | pages [15] -->
( )

<!-- b004756 | prose | pages [15] -->
x k

<!-- b004757 | prose | pages [15] -->
( ) |

<!-- b004758 | prose | pages [15] -->
0

<!-- b004759 | prose | pages [15] -->
i

<!-- b004760 | furniture | pages [15] -->


<!-- b004761 | prose | pages [15] -->
k k

<!-- b004762 | prose | pages [15] -->
Step4: Calculate the grey relational degree

<!-- b004763 | furniture | pages [15] -->


<!-- b004764 | furniture | pages [16] -->
Team 2517690

<!-- b004765 | furniture | pages [16] -->


<!-- b004766 | furniture | pages [16] -->


<!-- b004767 | furniture | pages [16] -->


<!-- b004768 | furniture | pages [16] -->


<!-- b004769 | furniture | pages [16] -->


<!-- b004770 | furniture | pages [16] -->


<!-- b004771 | furniture | pages [16] -->


<!-- b004772 | prose | pages [16] -->
n

<!-- b004773 | prose | pages [16] -->
1

<!-- b004774 | prose | pages [16] -->
 =

<!-- b004775 | prose | pages [16] -->
y x x

<!-- b004776 | prose | pages [16] -->
( , )

<!-- b004777 | prose | pages [16] -->
y x k

<!-- b004778 | prose | pages [16] -->
( ( ),

<!-- b004779 | furniture | pages [16] -->


<!-- b004780 | furniture | pages [16] -->


<!-- b004781 | furniture | pages [16] -->


<!-- b004782 | furniture | pages [16] -->


<!-- b004783 | furniture | pages [16] -->


<!-- b004784 | furniture | pages [16] -->


<!-- b004785 | furniture | pages [16] -->


<!-- b004786 | furniture | pages [16] -->
Page 16 of 25

<!-- b004787 | prose | pages [16] -->
+

<!-- b004788 | prose | pages [16] -->


<!-- b004789 | prose | pages [16] -->
n

<!-- b004790 | prose | pages [16] -->
1

<!-- b004791 | prose | pages [16] -->
a b

<!-- b004792 | prose | pages [16] -->
(15)

<!-- b004793 | prose | pages [16] -->
 =

<!-- b004794 | prose | pages [16] -->
x k

<!-- b004795 | prose | pages [16] -->
0

<!-- b004796 | prose | pages [16] -->
i

<!-- b004797 | prose | pages [16] -->
0

<!-- b004798 | prose | pages [16] -->
n

<!-- b004799 | prose | pages [16] -->
=

<!-- b004800 | prose | pages [16] -->
k

<!-- b004801 | prose | pages [16] -->
1

<!-- b004802 | prose | pages [16] -->
( ))

<!-- b004803 | prose | pages [16] -->
i i

<!-- b004804 | prose | pages [16] -->
− +

<!-- b004805 | prose | pages [16] -->


<!-- b004806 | prose | pages [16] -->
n

<!-- b004807 | prose | pages [16] -->
|

<!-- b004808 | prose | pages [16] -->
x k

<!-- b004809 | prose | pages [16] -->
( )

<!-- b004810 | prose | pages [16] -->
x k

<!-- b004811 | prose | pages [16] -->
( ) |

<!-- b004812 | prose | pages [16] -->
b

<!-- b004813 | furniture | pages [16] -->


<!-- b004814 | prose | pages [16] -->
=

<!-- b004815 | prose | pages [16] -->
k

<!-- b004816 | prose | pages [16] -->
1 0

<!-- b004817 | prose | pages [16] -->
i

<!-- b004818 | prose | pages [16] -->
This study uses the grey relational analysis model to quantify the degree of association between each sports event and the total number of medals, and further explore their correlation. The following table shows the degree of association between some events and the total number of medals of some countries:

<!-- b004819 | caption | pages [16] -->
Table 7:Correlation between sports and medals

<!-- b004820 | prose | pages [16] -->
Athletics Swimming

<!-- b004821 | prose | pages [16] -->
United

<!-- b004822 | prose | pages [16] -->
0.84 0.83 States

<!-- b004823 | prose | pages [16] -->
China 0.54 0.65

<!-- b004824 | prose | pages [16] -->
m

<!-- b004825 | prose | pages [16] -->
m

<!-- b004826 | prose | pages [16] -->
m

<!-- b004827 | prose | pages [16] -->
m

<!-- b004828 | prose | pages [16] -->
m

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
Great

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
m

<!-- b004979 | prose | pages [16] -->
m

<!-- b004980 | prose | pages [16] -->
m

<!-- b004981 | prose | pages [16] -->
m

<!-- b004982 | prose | pages [16] -->
m

<!-- b004983 | prose | pages [16] -->
m

<!-- b004984 | prose | pages [16] -->
m

<!-- b004985 | prose | pages [16] -->
m

<!-- b004986 | prose | pages [16] -->
m

<!-- b004987 | prose | pages [16] -->
m

<!-- b004988 | prose | pages [16] -->
m

<!-- b004989 | prose | pages [16] -->
m

<!-- b004990 | prose | pages [16] -->
m

<!-- b004991 | prose | pages [16] -->
m

<!-- b004992 | prose | pages [16] -->
m

<!-- b004993 | prose | pages [16] -->
m

<!-- b004994 | prose | pages [16] -->
m

<!-- b004995 | prose | pages [16] -->
m

<!-- b004996 | prose | pages [16] -->
m

<!-- b004997 | prose | pages [16] -->
m

<!-- b004998 | prose | pages [16] -->
m

<!-- b004999 | prose | pages [16] -->
m

<!-- b005000 | prose | pages [16] -->
m

<!-- b005001 | prose | pages [16] -->
m

<!-- b005002 | prose | pages [16] -->
m

<!-- b005003 | prose | pages [16] -->
m

<!-- b005004 | prose | pages [16] -->
m

<!-- b005005 | prose | pages [16] -->
m

<!-- b005006 | prose | pages [16] -->
m

<!-- b005007 | prose | pages [16] -->
m

<!-- b005008 | prose | pages [16] -->
m

<!-- b005009 | prose | pages [16] -->
m

<!-- b005010 | prose | pages [16] -->
m

<!-- b005011 | prose | pages [16] -->
m

<!-- b005012 | prose | pages [16] -->
0.45 0.66

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
Britain

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
m

<!-- b005129 | prose | pages [16] -->
m

<!-- b005130 | prose | pages [16] -->
m

<!-- b005131 | prose | pages [16] -->
m

<!-- b005132 | prose | pages [16] -->
m

<!-- b005133 | prose | pages [16] -->
m

<!-- b005134 | prose | pages [16] -->
m

<!-- b005135 | prose | pages [16] -->
m

<!-- b005136 | prose | pages [16] -->
m

<!-- b005137 | prose | pages [16] -->
m

<!-- b005138 | prose | pages [16] -->
m

<!-- b005139 | prose | pages [16] -->
m

<!-- b005140 | prose | pages [16] -->
m

<!-- b005141 | prose | pages [16] -->
m

<!-- b005142 | prose | pages [16] -->
m

<!-- b005143 | prose | pages [16] -->
m

<!-- b005144 | prose | pages [16] -->
m

<!-- b005145 | prose | pages [16] -->
m

<!-- b005146 | prose | pages [16] -->
m

<!-- b005147 | prose | pages [16] -->
m

<!-- b005148 | prose | pages [16] -->
m

<!-- b005149 | prose | pages [16] -->
m

<!-- b005150 | prose | pages [16] -->
m

<!-- b005151 | prose | pages [16] -->
m

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
m

<!-- b005237 | prose | pages [16] -->
m

<!-- b005238 | prose | pages [16] -->
m

<!-- b005239 | prose | pages [16] -->
m

<!-- b005240 | prose | pages [16] -->
m

<!-- b005241 | prose | pages [16] -->
m

<!-- b005242 | prose | pages [16] -->
m

<!-- b005243 | prose | pages [16] -->
m

<!-- b005244 | prose | pages [16] -->
m

<!-- b005245 | prose | pages [16] -->
m

<!-- b005246 | prose | pages [16] -->
m

<!-- b005247 | prose | pages [16] -->
m

<!-- b005248 | prose | pages [16] -->
m

<!-- b005249 | prose | pages [16] -->
m

<!-- b005250 | prose | pages [16] -->
m

<!-- b005251 | prose | pages [16] -->
m

<!-- b005252 | prose | pages [16] -->
m

<!-- b005253 | prose | pages [16] -->
m

<!-- b005254 | prose | pages [16] -->
m

<!-- b005255 | prose | pages [16] -->
m

<!-- b005256 | prose | pages [16] -->
m

<!-- b005257 | prose | pages [16] -->
m

<!-- b005258 | prose | pages [16] -->
m

<!-- b005259 | prose | pages [16] -->
m

<!-- b005260 | prose | pages [16] -->
m

<!-- b005261 | prose | pages [16] -->
m

<!-- b005262 | prose | pages [16] -->
m

<!-- b005263 | prose | pages [16] -->
m

<!-- b005264 | prose | pages [16] -->
m

<!-- b005265 | prose | pages [16] -->
m

<!-- b005266 | prose | pages [16] -->
m

<!-- b005267 | prose | pages [16] -->
m

<!-- b005268 | prose | pages [16] -->
m

<!-- b005269 | prose | pages [16] -->
m

<!-- b005270 | prose | pages [16] -->
m

<!-- b005271 | prose | pages [16] -->
m

<!-- b005272 | prose | pages [16] -->
m

<!-- b005273 | prose | pages [16] -->
m

<!-- b005274 | prose | pages [16] -->
m

<!-- b005275 | prose | pages [16] -->
m

<!-- b005276 | prose | pages [16] -->
m

<!-- b005277 | prose | pages [16] -->
m

<!-- b005278 | prose | pages [16] -->
m

<!-- b005279 | prose | pages [16] -->
m

<!-- b005280 | prose | pages [16] -->
m

<!-- b005281 | prose | pages [16] -->
m

<!-- b005282 | prose | pages [16] -->
m

<!-- b005283 | prose | pages [16] -->
m

<!-- b005284 | prose | pages [16] -->
m

<!-- b005285 | prose | pages [16] -->
m

<!-- b005286 | prose | pages [16] -->
m

<!-- b005287 | prose | pages [16] -->
m

<!-- b005288 | prose | pages [16] -->
m

<!-- b005289 | prose | pages [16] -->
m

<!-- b005290 | prose | pages [16] -->
m

<!-- b005291 | prose | pages [16] -->
m

<!-- b005292 | prose | pages [16] -->
m

<!-- b005293 | prose | pages [16] -->
m

<!-- b005294 | prose | pages [16] -->
m

<!-- b005295 | prose | pages [16] -->
m

<!-- b005296 | prose | pages [16] -->
m

<!-- b005297 | prose | pages [16] -->
m

<!-- b005298 | prose | pages [16] -->
m

<!-- b005299 | prose | pages [16] -->
m

<!-- b005300 | prose | pages [16] -->
m

<!-- b005301 | prose | pages [16] -->
m

<!-- b005302 | prose | pages [16] -->
m

<!-- b005303 | prose | pages [16] -->
m

<!-- b005304 | prose | pages [16] -->
m

<!-- b005305 | prose | pages [16] -->
m

<!-- b005306 | prose | pages [16] -->
m

<!-- b005307 | prose | pages [16] -->
m

<!-- b005308 | prose | pages [16] -->
m

<!-- b005309 | prose | pages [16] -->
m

<!-- b005310 | prose | pages [16] -->
m

<!-- b005311 | prose | pages [16] -->
m

<!-- b005312 | prose | pages [16] -->
m

<!-- b005313 | prose | pages [16] -->
m

<!-- b005314 | prose | pages [16] -->
m

<!-- b005315 | prose | pages [16] -->
m

<!-- b005316 | prose | pages [16] -->
m

<!-- b005317 | prose | pages [16] -->
m

<!-- b005318 | prose | pages [16] -->
m

<!-- b005319 | prose | pages [16] -->
m

<!-- b005320 | prose | pages [16] -->
m

<!-- b005321 | prose | pages [16] -->
m

<!-- b005322 | prose | pages [16] -->
m

<!-- b005323 | prose | pages [16] -->
m

<!-- b005324 | prose | pages [16] -->
m

<!-- b005325 | prose | pages [16] -->
m

<!-- b005326 | prose | pages [16] -->
m

<!-- b005327 | prose | pages [16] -->
m

<!-- b005328 | prose | pages [16] -->
m

<!-- b005329 | prose | pages [16] -->
m

<!-- b005330 | prose | pages [16] -->
m

<!-- b005331 | prose | pages [16] -->
m

<!-- b005332 | prose | pages [16] -->
m

<!-- b005333 | prose | pages [16] -->
m

<!-- b005334 | prose | pages [16] -->
m

<!-- b005335 | prose | pages [16] -->
m

<!-- b005336 | prose | pages [16] -->
m

<!-- b005337 | prose | pages [16] -->
m

<!-- b005338 | prose | pages [16] -->
m

<!-- b005339 | prose | pages [16] -->
m

<!-- b005340 | prose | pages [16] -->
m

<!-- b005341 | prose | pages [16] -->
m

<!-- b005342 | prose | pages [16] -->
m

<!-- b005343 | prose | pages [16] -->
m

<!-- b005344 | prose | pages [16] -->
m

<!-- b005345 | prose | pages [16] -->
m

<!-- b005346 | prose | pages [16] -->
m

<!-- b005347 | prose | pages [16] -->
m

<!-- b005348 | prose | pages [16] -->
m

<!-- b005349 | prose | pages [16] -->
m

<!-- b005350 | prose | pages [16] -->
m

<!-- b005351 | prose | pages [16] -->
m

<!-- b005352 | prose | pages [16] -->
m

<!-- b005353 | prose | pages [16] -->
m

<!-- b005354 | prose | pages [16] -->
m

<!-- b005355 | prose | pages [16] -->
m

<!-- b005356 | prose | pages [16] -->
m

<!-- b005357 | prose | pages [16] -->
m

<!-- b005358 | prose | pages [16] -->
m

<!-- b005359 | prose | pages [16] -->
m

<!-- b005360 | prose | pages [16] -->
m

<!-- b005361 | prose | pages [16] -->
m

<!-- b005362 | prose | pages [16] -->
m

<!-- b005363 | prose | pages [16] -->
m

<!-- b005364 | prose | pages [16] -->
m

<!-- b005365 | prose | pages [16] -->
m

<!-- b005366 | prose | pages [16] -->
m

<!-- b005367 | prose | pages [16] -->
m

<!-- b005368 | prose | pages [16] -->
m

<!-- b005369 | prose | pages [16] -->
m

<!-- b005370 | prose | pages [16] -->
m

<!-- b005371 | prose | pages [16] -->
m

<!-- b005372 | prose | pages [16] -->
m

<!-- b005373 | prose | pages [16] -->
m

<!-- b005374 | prose | pages [16] -->
m

<!-- b005375 | prose | pages [16] -->
m

<!-- b005376 | prose | pages [16] -->
m

<!-- b005377 | prose | pages [16] -->
m

<!-- b005378 | prose | pages [16] -->
m

<!-- b005379 | prose | pages [16] -->
m

<!-- b005380 | prose | pages [16] -->
m

<!-- b005381 | prose | pages [16] -->
m

<!-- b005382 | prose | pages [16] -->
m

<!-- b005383 | prose | pages [16] -->
m

<!-- b005384 | prose | pages [16] -->
m

<!-- b005385 | prose | pages [16] -->
m

<!-- b005386 | prose | pages [16] -->
m

<!-- b005387 | prose | pages [16] -->
m

<!-- b005388 | prose | pages [16] -->
m

<!-- b005389 | prose | pages [16] -->
m

<!-- b005390 | prose | pages [16] -->
m

<!-- b005391 | prose | pages [16] -->
m

<!-- b005392 | prose | pages [16] -->
m

<!-- b005393 | prose | pages [16] -->
m

<!-- b005394 | prose | pages [16] -->
m

<!-- b005395 | prose | pages [16] -->
m

<!-- b005396 | prose | pages [16] -->
m

<!-- b005397 | prose | pages [16] -->
m

<!-- b005398 | prose | pages [16] -->
m

<!-- b005399 | prose | pages [16] -->
m

<!-- b005400 | prose | pages [16] -->
m

<!-- b005401 | prose | pages [16] -->
m

<!-- b005402 | prose | pages [16] -->
m

<!-- b005403 | prose | pages [16] -->
m

<!-- b005404 | prose | pages [16] -->
m

<!-- b005405 | prose | pages [16] -->
m

<!-- b005406 | prose | pages [16] -->
m

<!-- b005407 | prose | pages [16] -->
m

<!-- b005408 | prose | pages [16] -->
m

<!-- b005409 | prose | pages [16] -->
m

<!-- b005410 | prose | pages [16] -->
m

<!-- b005411 | prose | pages [16] -->
m

<!-- b005412 | prose | pages [16] -->
m

<!-- b005413 | prose | pages [16] -->
m

<!-- b005414 | prose | pages [16] -->
m

<!-- b005415 | prose | pages [16] -->
m

<!-- b005416 | prose | pages [16] -->
m

<!-- b005417 | prose | pages [16] -->
m

<!-- b005418 | prose | pages [16] -->
m

<!-- b005419 | prose | pages [16] -->
m

<!-- b005420 | prose | pages [16] -->
m

<!-- b005421 | prose | pages [16] -->
m

<!-- b005422 | prose | pages [16] -->
m

<!-- b005423 | prose | pages [16] -->
m

<!-- b005424 | prose | pages [16] -->
m

<!-- b005425 | prose | pages [16] -->
m

<!-- b005426 | prose | pages [16] -->
m

<!-- b005427 | prose | pages [16] -->
m

<!-- b005428 | prose | pages [16] -->
m

<!-- b005429 | prose | pages [16] -->
m

<!-- b005430 | prose | pages [16] -->
m

<!-- b005431 | prose | pages [16] -->
m

<!-- b005432 | prose | pages [16] -->
m

<!-- b005433 | prose | pages [16] -->
m

<!-- b005434 | prose | pages [16] -->
m

<!-- b005435 | prose | pages [16] -->
m

<!-- b005436 | prose | pages [16] -->
m

<!-- b005437 | prose | pages [16] -->
Australia 0.5 0.54

<!-- b005438 | prose | pages [16] -->
m

<!-- b005439 | prose | pages [16] -->
m

<!-- b005440 | prose | pages [16] -->
m

<!-- b005441 | prose | pages [16] -->
m

<!-- b005442 | prose | pages [16] -->
m

<!-- b005443 | prose | pages [16] -->
m

<!-- b005444 | prose | pages [16] -->
m

<!-- b005445 | prose | pages [16] -->
m

<!-- b005446 | prose | pages [16] -->
m

<!-- b005447 | prose | pages [16] -->
m

<!-- b005448 | prose | pages [16] -->
m

<!-- b005449 | prose | pages [16] -->
m

<!-- b005450 | prose | pages [16] -->
m

<!-- b005451 | prose | pages [16] -->
m

<!-- b005452 | prose | pages [16] -->
m

<!-- b005453 | prose | pages [16] -->
m

<!-- b005454 | prose | pages [16] -->
m

<!-- b005455 | prose | pages [16] -->
m

<!-- b005456 | prose | pages [16] -->
m

<!-- b005457 | prose | pages [16] -->
m

<!-- b005458 | prose | pages [16] -->
m

<!-- b005459 | prose | pages [16] -->
m

<!-- b005460 | prose | pages [16] -->
m

<!-- b005461 | prose | pages [16] -->
m

<!-- b005462 | prose | pages [16] -->
m

<!-- b005463 | prose | pages [16] -->
m

<!-- b005464 | prose | pages [16] -->
m

<!-- b005465 | prose | pages [16] -->
m

<!-- b005466 | prose | pages [16] -->
m

<!-- b005467 | prose | pages [16] -->
m

<!-- b005468 | prose | pages [16] -->
m

<!-- b005469 | prose | pages [16] -->
m

<!-- b005470 | prose | pages [16] -->
m

<!-- b005471 | prose | pages [16] -->
m

<!-- b005472 | prose | pages [16] -->
m

<!-- b005473 | prose | pages [16] -->
m

<!-- b005474 | prose | pages [16] -->
m

<!-- b005475 | prose | pages [16] -->
m

<!-- b005476 | prose | pages [16] -->
m

<!-- b005477 | prose | pages [16] -->
m

<!-- b005478 | prose | pages [16] -->
m

<!-- b005479 | prose | pages [16] -->
m

<!-- b005480 | prose | pages [16] -->
m

<!-- b005481 | prose | pages [16] -->
m

<!-- b005482 | prose | pages [16] -->
m

<!-- b005483 | prose | pages [16] -->
m

<!-- b005484 | prose | pages [16] -->
m

<!-- b005485 | prose | pages [16] -->
m

<!-- b005486 | prose | pages [16] -->
m

<!-- b005487 | prose | pages [16] -->
m

<!-- b005488 | prose | pages [16] -->
m

<!-- b005489 | prose | pages [16] -->
m

<!-- b005490 | prose | pages [16] -->
m

<!-- b005491 | prose | pages [16] -->
m

<!-- b005492 | prose | pages [16] -->
m

<!-- b005493 | prose | pages [16] -->
m

<!-- b005494 | prose | pages [16] -->
m

<!-- b005495 | prose | pages [16] -->
m

<!-- b005496 | prose | pages [16] -->
m

<!-- b005497 | prose | pages [16] -->
m

<!-- b005498 | prose | pages [16] -->
m

<!-- b005499 | prose | pages [16] -->
m

<!-- b005500 | prose | pages [16] -->
m

<!-- b005501 | prose | pages [16] -->
m

<!-- b005502 | prose | pages [16] -->
m

<!-- b005503 | prose | pages [16] -->
m

<!-- b005504 | prose | pages [16] -->
m

<!-- b005505 | prose | pages [16] -->
m

<!-- b005506 | prose | pages [16] -->
m

<!-- b005507 | prose | pages [16] -->
m

<!-- b005508 | prose | pages [16] -->
m

<!-- b005509 | prose | pages [16] -->
m

<!-- b005510 | prose | pages [16] -->
m

<!-- b005511 | prose | pages [16] -->
m

<!-- b005512 | prose | pages [16] -->
m

<!-- b005513 | prose | pages [16] -->
m

<!-- b005514 | prose | pages [16] -->
m

<!-- b005515 | prose | pages [16] -->
Japan 0.44 0.32

<!-- b005516 | furniture | pages [16] -->


<!-- b005517 | prose | pages [16] -->
Diving Volleyball Triathlon

<!-- b005518 | prose | pages [16] -->
0.45 0.67 0.51

<!-- b005519 | prose | pages [16] -->
0.87 0.79 0.21

<!-- b005520 | prose | pages [16] -->
0.12 0.34 0.82

<!-- b005521 | prose | pages [16] -->
0.56 0.21 0.56

<!-- b005522 | prose | pages [16] -->
0.45 0.45 0.11

<!-- b005523 | furniture | pages [16] -->


<!-- b005524 | prose | pages [16] -->
By analyzing the above table, it can be seen that the United States has a high degree of association with track and field and swimming events, which are 0.84 and 0.83 respectively. This indicates that these two events are crucial to the number of its medals. China has the highest degree of association with the diving event (0.87), highlighting the dominant position of diving in its Olympic performance. The degree of association of the United Kingdom with the triathlon is 0.82, showing the significant impact of this emerging event on the total number of its medals. In contrast, Japan has a generally low degree of association with various events, indicating its relatively balanced overall competitiveness in multiple events.

<!-- b005525 | heading | pages [16] -->
5.3.2 Influence of the Events Chosen by the Host Country on the Results

<!-- b005526 | prose | pages [16] -->
(1) Visual analysis

<!-- b005527 | prose | pages [16] -->
To visually display the changes in the medal performances of various countries in succes- sive Olympic Games, the following chart shows the number of medals of different countries in each Olympic Games. The horizontal axis represents the year of the Olympic Games, the ver- tical axis represents the number of medals, and each line represents the number of medals of a particular country.

<!-- b005528 | furniture | pages [16] -->


<!-- b005529 | prose | pages [16] -->
关注数学模型

<!-- b005530 | furniture | pages [16] -->
2

<!-- b005531 | furniture | pages [16] -->
MATHmodels

<!-- b005532 | furniture | pages [16] -->
获取更多资讯

<!-- b005533 | furniture | pages [17] -->
Team 2517690

<!-- b005534 | furniture | pages [17] -->


<!-- b005535 | furniture | pages [17] -->


<!-- b005536 | furniture | pages [17] -->


<!-- b005537 | furniture | pages [17] -->


<!-- b005538 | furniture | pages [17] -->


<!-- b005539 | furniture | pages [17] -->


<!-- b005540 | furniture | pages [17] -->


<!-- b005541 | furniture | pages [17] -->


<!-- b005542 | furniture | pages [17] -->


<!-- b005543 | furniture | pages [17] -->


<!-- b005544 | furniture | pages [17] -->


<!-- b005545 | furniture | pages [17] -->


<!-- b005546 | furniture | pages [17] -->


<!-- b005547 | furniture | pages [17] -->


<!-- b005548 | furniture | pages [17] -->
Page 17 of 25

<!-- b005549 | prose | pages [17] -->
微信公众号：数学模型

<!-- b005550 | furniture | pages [17] -->


<!-- b005551 | caption | pages [17] -->
Figure 12:Time series chart of the number of medals

<!-- b005552 | prose | pages [17] -->
From the graph, it can be observed that the total number of medals of the United States reached its peak in 1984, and this phenomenon is closely related to the fact that the Olympic Games were held in the United States that year. Similarly, China also achieved a record-high number of medals in 2008, reflecting the positive impact of the host status on its performance. In 2020, the total number of medals of France also reached its peak, which is inseparable from

<!-- b005553 | prose | pages [17] -->
微信号：MATHmodels

<!-- b005554 | prose | pages [17] -->
Paris being the host city. Thus, it can be seen that the host status significantly promotes the medal performance of the host country in the Olympic Games.

<!-- b005555 | prose | pages [17] -->
(2) The potential impact of the United States' host status on its medal performance in 2028

<!-- b005556 | prose | pages [17] -->
The five new sports added to the 2028 Los Angeles Olympics - baseball/softball, lacrosse, cricket, squash, and flag football - will enhance the United States' medal potential. Baseball and lacrosse, as traditional strong suits of the United States, are expected to contribute a large number of medals. Although cricket and squash are relatively niche sports, their inclusion is expected to boost the United States' performance in these events. Flag football provides new opportunities for the young population, further increasing the United States' competitiveness in the Olympics.

<!-- b005557 | heading | pages [17] -->
6 The Study of a “Great Coach” Effect

<!-- b005558 | heading | pages [17] -->
6.1 Analysis of the “great coach” effect

<!-- b005559 | heading | pages [17] -->
6.1.1 Two-sample Mean Hypothesis Testing

<!-- b005560 | prose | pages [17] -->
To explore whether the "great coach" effect has an impact on Olympic medal performance, we selected the two-sample mean hypothesis testing method. This method is applicable for comparing whether there is a significant difference between the means of two independent samples. In this study, we defined the two samples as follows: one set of data represents the perfor-

<!-- b005561 | caption | pages [17] -->
Figure 13:Test Method

<!-- b005562 | prose | pages [17] -->
mance before a great coach took charge, and the other represents

<!-- b005563 | furniture | pages [17] -->


<!-- b005564 | furniture | pages [20] -->
Team 2517690

<!-- b005565 | furniture | pages [20] -->


<!-- b005566 | furniture | pages [20] -->


<!-- b005567 | furniture | pages [20] -->


<!-- b005568 | furniture | pages [20] -->


<!-- b005569 | furniture | pages [20] -->


<!-- b005570 | furniture | pages [20] -->


<!-- b005571 | furniture | pages [20] -->


<!-- b005572 | furniture | pages [20] -->


<!-- b005573 | furniture | pages [20] -->


<!-- b005574 | furniture | pages [20] -->


<!-- b005575 | furniture | pages [20] -->


<!-- b005576 | furniture | pages [20] -->


<!-- b005577 | furniture | pages [20] -->


<!-- b005578 | furniture | pages [20] -->


<!-- b005579 | furniture | pages [20] -->
Page 20 of 25

<!-- b005580 | prose | pages [20] -->
3x , and y be a 0 - 1 the number of athletes participating in this event for this country be variable indicating whether the sports event wins an award.

<!-- b005581 | prose | pages [20] -->
After substituting the standardized data into the logistic regression model and estimating the model parameters, the regression model is obtained as follows:

<!-- b005582 | prose | pages [20] -->
(ˆ

<!-- b005583 | prose | pages [20] -->
= = P y

<!-- b005584 | prose | pages [20] -->
1

<!-- b005585 | prose | pages [20] -->
x

<!-- b005586 | prose | pages [20] -->
)

<!-- b005587 | prose | pages [20] -->
+

<!-- b005588 | prose | pages [20] -->
1

<!-- b005589 | prose | pages [20] -->
p = + ln( ) .2 12 − 1 p

<!-- b005590 | prose | pages [20] -->
1

<!-- b005591 | prose | pages [20] -->
− + + +

<!-- b005592 | prose | pages [20] -->
( .2 12 4.14

<!-- b005593 | prose | pages [20] -->
x

<!-- b005594 | prose | pages [20] -->
7.25

<!-- b005595 | prose | pages [20] -->
x

<!-- b005596 | prose | pages [20] -->
.1 98

<!-- b005597 | prose | pages [20] -->
x

<!-- b005598 | prose | pages [20] -->
)

<!-- b005599 | prose | pages [20] -->
e e

<!-- b005600 | prose | pages [20] -->
1 2 3

<!-- b005601 | furniture | pages [20] -->


<!-- b005602 | prose | pages [20] -->
(20)

<!-- b005603 | prose | pages [20] -->
+ + .4 .4 14 x .7 25 x .1 98 x 1 2 3

<!-- b005604 | furniture | pages [20] -->


<!-- b005605 | prose | pages [20] -->
A significance test was conducted on the regression coefficients, and the results are as follows:

<!-- b005606 | caption | pages [20] -->
Table 10:Logistic Re-regression Significance Test Results

<!-- b005607 | prose | pages [20] -->
Varible

<!-- b005608 | furniture | pages [20] -->


<!-- b005609 | prose | pages [20] -->
Coaching Duration 4.14

<!-- b005610 | prose | pages [20] -->
Historical medal tally 7.25

<!-- b005611 | prose | pages [20] -->
Number of participants 1.98

<!-- b005612 | prose | pages [20] -->
Standard Error P

<!-- b005613 | prose | pages [20] -->
0.67 0.04

<!-- b005614 | prose | pages [20] -->
0.91 0.006

<!-- b005615 | prose | pages [20] -->
0.39 0.05

<!-- b005616 | furniture | pages [20] -->


<!-- b005617 | prose | pages [20] -->
As can be seen from the above table, the influence of the coaching time of a great coach on whether the sports event wins an award is significant, and it shows a positive correlation. Based on the values of the regression coefficients, it can be seen that the contribution of the coaching duration to the award-winning result lies between the level of the athletes in this event and the number of participating athletes.

<!-- b005618 | heading | pages [20] -->
6.3 Investment in “great coach”

<!-- b005619 | prose | pages [20] -->
We select China, the United States, and Japan as the research objects. (1) Screen out the events in which each country has not won any medals in the past four Olympic Games.

<!-- b005620 | prose | pages [20] -->
We believe that the events that have won medals in the past four Olympic Games are already mature enough. We also believe that there is greater room for improvement in the events in which countries have not won medals in the past four Olympic Games, and these events are in more urgent need of the guidance of great coaches.

<!-- b005621 | prose | pages [20] -->
(2) Selection of investment projects 1x =4, input it into the trained Change the guidance time of the already selected events, set logistic regression model, and select the projects for investment by comparing the probabilities of these projects winning awards. Take the Chinese team as an example:

<!-- b005622 | caption | pages [20] -->
Table 11:Investment projects and probability

<!-- b005623 | furniture | pages [20] -->


<!-- b005624 | furniture | pages [20] -->


<!-- b005625 | prose | pages [20] -->
关注数学模型

<!-- b005626 | furniture | pages [20] -->
2

<!-- b005627 | furniture | pages [20] -->
MATHmodels

<!-- b005628 | furniture | pages [20] -->
获取更多资讯

<!-- b005629 | furniture | pages [21] -->
Team 2517690

<!-- b005630 | furniture | pages [21] -->


<!-- b005631 | furniture | pages [21] -->


<!-- b005632 | furniture | pages [21] -->


<!-- b005633 | furniture | pages [21] -->


<!-- b005634 | furniture | pages [21] -->


<!-- b005635 | furniture | pages [21] -->


<!-- b005636 | furniture | pages [21] -->


<!-- b005637 | furniture | pages [21] -->


<!-- b005638 | furniture | pages [21] -->


<!-- b005639 | furniture | pages [21] -->


<!-- b005640 | furniture | pages [21] -->


<!-- b005641 | furniture | pages [21] -->


<!-- b005642 | furniture | pages [21] -->


<!-- b005643 | furniture | pages [21] -->


<!-- b005644 | furniture | pages [21] -->
Page 21 of 25

<!-- b005645 | prose | pages [21] -->
According to the analysis of the logistic regression model, the men's volleyball event has the highest probability of the Chinese team winning an award. Therefore, it is recommended to prioritize investment in "great coaches" to increase the winning chances of this event. In contrast, the probability of the Chinese men's football team winning an award is relatively low,

<!-- b005646 | prose | pages [21] -->
微信公众号：数学模型

<!-- b005647 | prose | pages [21] -->
and it may not be the main investment direction.

<!-- b005648 | prose | pages [21] -->
For the United States, the probabilities of winning awards in badminton and table tennis events are relatively high. It is recommended to allocate "great coach" resources to these two events. The Japanese team should increase its investment in coaches for the swimming event to enhance its competitiveness and medal potential in this field.

<!-- b005649 | heading | pages [21] -->
7 Predicting Olympic Medals: Insights and Strategies

<!-- b005650 | heading | pages [21] -->
7.1 The Number of Participating Athletes and the Potential to Win Medals

<!-- b005651 | prose | pages [21] -->
微信号：MATHmodels

<!-- b005652 | prose | pages [21] -->
The model demonstrates the impact of the number of participating athletes on the number of medals. More athletes mean more competition opportunities and potential medal opportuni- ties. Specifically, countries with a large number of participants, such as the United States and China, usually have strong competitiveness in multiple events.

<!-- b005653 | prose | pages [21] -->
National Olympic Committees can increase the overall number of medals by expanding the scope of athlete selection and increasing the number of participating athletes in certain events. Diversify the events of participation: In addition to traditional dominant events, Na- tional Olympic Committees can also encourage athletes to participate in more emerging or less popular events to increase the chances of winning awards in these events.

<!-- b005654 | heading | pages [21] -->
7.2 Medal Distribution of Different Countries in Various Events

<!-- b005655 | prose | pages [21] -->
We used the grey relational analysis model to reveal the medal distribution of different countries in various events. For example, the United States has a high degree of correlation with track and field and swimming events, indicating that these events have a significant impact on its total medal count; China has the highest correlation with the diving event, demonstrating the decisive role of diving in China's medal performance.

<!-- b005656 | prose | pages [21] -->
Based on this insight, countries can adopt the following strategies: ⚫ Concentrate resources: National Olympic Committees can use grey relational analysis to identify the events that contribute the most to their total medal count. Then, they can concentrate resources on training and selection in these events to enhance their competi- tiveness in them. ⚫ Invest in emerging events: At the same time, grey relational analysis can also help iden- tify those potentially overlooked and underdeveloped events, providing countries with more potential medal opportunities.

<!-- b005657 | heading | pages [21] -->
7.3 Set Advantageous Events

<!-- b005658 | prose | pages [21] -->
The advantages of the host country in the Olympic Games come not only from factors such as psychology, resources, and audience support but also from its influence on event set- ting, schedule arrangement and rule adjustment, which can further enhance this advantage.

<!-- b005659 | prose | pages [21] -->
m

<!-- b005660 | prose | pages [21] -->
m

<!-- b005661 | prose | pages [21] -->
m

<!-- b005662 | prose | pages [21] -->
m

<!-- b005663 | prose | pages [21] -->
m

<!-- b005664 | prose | pages [21] -->
m

<!-- b005665 | prose | pages [21] -->
m

<!-- b005666 | prose | pages [21] -->
m

<!-- b005667 | prose | pages [21] -->
m

<!-- b005668 | prose | pages [21] -->
m

<!-- b005669 | prose | pages [21] -->
m

<!-- b005670 | prose | pages [21] -->
m

<!-- b005671 | prose | pages [21] -->
m

<!-- b005672 | prose | pages [21] -->
m

<!-- b005673 | prose | pages [21] -->
m

<!-- b005674 | prose | pages [21] -->
m

<!-- b005675 | prose | pages [21] -->
m

<!-- b005676 | prose | pages [21] -->
m

<!-- b005677 | prose | pages [21] -->
m

<!-- b005678 | prose | pages [21] -->
m

<!-- b005679 | prose | pages [21] -->
m

<!-- b005680 | prose | pages [21] -->
m

<!-- b005681 | prose | pages [21] -->
m

<!-- b005682 | prose | pages [21] -->
m

<!-- b005683 | prose | pages [21] -->
m

<!-- b005684 | prose | pages [21] -->
m

<!-- b005685 | prose | pages [21] -->
m

<!-- b005686 | prose | pages [21] -->
m

<!-- b005687 | prose | pages [21] -->
m

<!-- b005688 | prose | pages [21] -->
m

<!-- b005689 | prose | pages [21] -->
m

<!-- b005690 | prose | pages [21] -->
m

<!-- b005691 | prose | pages [21] -->
m

<!-- b005692 | prose | pages [21] -->
m

<!-- b005693 | prose | pages [21] -->
m

<!-- b005694 | prose | pages [21] -->
m

<!-- b005695 | prose | pages [21] -->
m

<!-- b005696 | prose | pages [21] -->
m

<!-- b005697 | prose | pages [21] -->
m

<!-- b005698 | prose | pages [21] -->
m

<!-- b005699 | prose | pages [21] -->
m

<!-- b005700 | prose | pages [21] -->
m

<!-- b005701 | prose | pages [21] -->
m

<!-- b005702 | prose | pages [21] -->
m

<!-- b005703 | prose | pages [21] -->
m

<!-- b005704 | prose | pages [21] -->
m

<!-- b005705 | prose | pages [21] -->
m

<!-- b005706 | prose | pages [21] -->
m

<!-- b005707 | prose | pages [21] -->
m

<!-- b005708 | prose | pages [21] -->
m

<!-- b005709 | prose | pages [21] -->
m

<!-- b005710 | prose | pages [21] -->
m

<!-- b005711 | prose | pages [21] -->
m

<!-- b005712 | prose | pages [21] -->
m

<!-- b005713 | prose | pages [21] -->
m

<!-- b005714 | prose | pages [21] -->
m

<!-- b005715 | prose | pages [21] -->
m

<!-- b005716 | prose | pages [21] -->
m

<!-- b005717 | prose | pages [21] -->
m

<!-- b005718 | prose | pages [21] -->
m

<!-- b005719 | prose | pages [21] -->
m

<!-- b005720 | prose | pages [21] -->
m

<!-- b005721 | prose | pages [21] -->
m

<!-- b005722 | prose | pages [21] -->
m

<!-- b005723 | prose | pages [21] -->
m

<!-- b005724 | prose | pages [21] -->
m

<!-- b005725 | prose | pages [21] -->
m

<!-- b005726 | prose | pages [21] -->
m

<!-- b005727 | prose | pages [21] -->
m

<!-- b005728 | prose | pages [21] -->
m

<!-- b005729 | prose | pages [21] -->
m

<!-- b005730 | prose | pages [21] -->
m

<!-- b005731 | prose | pages [21] -->
m

<!-- b005732 | prose | pages [21] -->
m

<!-- b005733 | prose | pages [21] -->
m

<!-- b005734 | prose | pages [21] -->
m

<!-- b005735 | prose | pages [21] -->
m

<!-- b005736 | prose | pages [21] -->
m

<!-- b005737 | prose | pages [21] -->
m

<!-- b005738 | prose | pages [21] -->
m

<!-- b005739 | prose | pages [21] -->
m

<!-- b005740 | prose | pages [21] -->
m

<!-- b005741 | prose | pages [21] -->
m

<!-- b005742 | prose | pages [21] -->
m

<!-- b005743 | prose | pages [21] -->
m

<!-- b005744 | prose | pages [21] -->
m

<!-- b005745 | prose | pages [21] -->
m

<!-- b005746 | prose | pages [21] -->
m

<!-- b005747 | prose | pages [21] -->
m

<!-- b005748 | prose | pages [21] -->
m

<!-- b005749 | prose | pages [21] -->
m

<!-- b005750 | prose | pages [21] -->
m

<!-- b005751 | prose | pages [21] -->
m

<!-- b005752 | prose | pages [21] -->
m

<!-- b005753 | prose | pages [21] -->
m

<!-- b005754 | prose | pages [21] -->
m

<!-- b005755 | prose | pages [21] -->
m

<!-- b005756 | prose | pages [21] -->
m

<!-- b005757 | prose | pages [21] -->
m

<!-- b005758 | prose | pages [21] -->
m

<!-- b005759 | prose | pages [21] -->
m

<!-- b005760 | prose | pages [21] -->
m

<!-- b005761 | prose | pages [21] -->
m

<!-- b005762 | prose | pages [21] -->
m

<!-- b005763 | prose | pages [21] -->
m

<!-- b005764 | prose | pages [21] -->
m

<!-- b005765 | prose | pages [21] -->
m

<!-- b005766 | prose | pages [21] -->
m

<!-- b005767 | prose | pages [21] -->
m

<!-- b005768 | prose | pages [21] -->
m

<!-- b005769 | prose | pages [21] -->
m

<!-- b005770 | prose | pages [21] -->
m

<!-- b005771 | prose | pages [21] -->
m

<!-- b005772 | prose | pages [21] -->
m

<!-- b005773 | prose | pages [21] -->
m

<!-- b005774 | prose | pages [21] -->
m

<!-- b005775 | prose | pages [21] -->
m

<!-- b005776 | prose | pages [21] -->
m

<!-- b005777 | prose | pages [21] -->
m

<!-- b005778 | prose | pages [21] -->
m

<!-- b005779 | prose | pages [21] -->
m

<!-- b005780 | prose | pages [21] -->
m

<!-- b005781 | prose | pages [21] -->
m

<!-- b005782 | prose | pages [21] -->
m

<!-- b005783 | prose | pages [21] -->
m

<!-- b005784 | prose | pages [21] -->
m

<!-- b005785 | prose | pages [21] -->
m

<!-- b005786 | prose | pages [21] -->
m

<!-- b005787 | prose | pages [21] -->
m

<!-- b005788 | prose | pages [21] -->
m

<!-- b005789 | prose | pages [21] -->
m

<!-- b005790 | prose | pages [21] -->
m

<!-- b005791 | prose | pages [21] -->
m

<!-- b005792 | prose | pages [21] -->
m

<!-- b005793 | prose | pages [21] -->
m

<!-- b005794 | prose | pages [21] -->
m

<!-- b005795 | prose | pages [21] -->
m

<!-- b005796 | prose | pages [21] -->
m

<!-- b005797 | prose | pages [21] -->
m

<!-- b005798 | prose | pages [21] -->
m

<!-- b005799 | prose | pages [21] -->
m

<!-- b005800 | prose | pages [21] -->
m

<!-- b005801 | prose | pages [21] -->
m

<!-- b005802 | prose | pages [21] -->
m

<!-- b005803 | prose | pages [21] -->
m

<!-- b005804 | prose | pages [21] -->
m

<!-- b005805 | prose | pages [21] -->
m

<!-- b005806 | prose | pages [21] -->
m

<!-- b005807 | prose | pages [21] -->
m

<!-- b005808 | prose | pages [21] -->
m

<!-- b005809 | prose | pages [21] -->
m

<!-- b005810 | prose | pages [21] -->
m

<!-- b005811 | prose | pages [21] -->
m

<!-- b005812 | prose | pages [21] -->
m

<!-- b005813 | prose | pages [21] -->
m

<!-- b005814 | prose | pages [21] -->
m

<!-- b005815 | prose | pages [21] -->
m

<!-- b005816 | prose | pages [21] -->
m

<!-- b005817 | prose | pages [21] -->
m

<!-- b005818 | prose | pages [21] -->
m

<!-- b005819 | prose | pages [21] -->
m

<!-- b005820 | prose | pages [21] -->
m

<!-- b005821 | prose | pages [21] -->
m

<!-- b005822 | prose | pages [21] -->
m

<!-- b005823 | prose | pages [21] -->
m

<!-- b005824 | prose | pages [21] -->
m

<!-- b005825 | prose | pages [21] -->
m

<!-- b005826 | furniture | pages [21] -->


<!-- b005827 | prose | pages [21] -->
m

<!-- b005828 | prose | pages [21] -->
m

<!-- b005829 | prose | pages [21] -->
m

<!-- b005830 | prose | pages [21] -->
m

<!-- b005831 | prose | pages [21] -->
m

<!-- b005832 | prose | pages [21] -->
m

<!-- b005833 | prose | pages [21] -->
m

<!-- b005834 | prose | pages [21] -->
m

<!-- b005835 | prose | pages [21] -->
m

<!-- b005836 | prose | pages [21] -->
m

<!-- b005837 | prose | pages [21] -->
m

<!-- b005838 | prose | pages [21] -->
m

<!-- b005839 | prose | pages [21] -->
m

<!-- b005840 | prose | pages [21] -->
m

<!-- b005841 | prose | pages [21] -->
m

<!-- b005842 | prose | pages [21] -->
m

<!-- b005843 | prose | pages [21] -->
m

<!-- b005844 | prose | pages [21] -->
m

<!-- b005845 | prose | pages [21] -->
m

<!-- b005846 | prose | pages [21] -->
m

<!-- b005847 | prose | pages [21] -->
m

<!-- b005848 | prose | pages [21] -->
m

<!-- b005849 | prose | pages [21] -->
m

<!-- b005850 | prose | pages [21] -->
m

<!-- b005851 | prose | pages [21] -->
m

<!-- b005852 | prose | pages [21] -->
m

<!-- b005853 | prose | pages [21] -->
m

<!-- b005854 | prose | pages [21] -->
m

<!-- b005855 | prose | pages [21] -->
m

<!-- b005856 | prose | pages [21] -->
m

<!-- b005857 | prose | pages [21] -->
m

<!-- b005858 | prose | pages [21] -->
m

<!-- b005859 | prose | pages [21] -->
m

<!-- b005860 | prose | pages [21] -->
m

<!-- b005861 | prose | pages [21] -->
m

<!-- b005862 | prose | pages [21] -->
m

<!-- b005863 | prose | pages [21] -->
m

<!-- b005864 | prose | pages [21] -->
m

<!-- b005865 | prose | pages [21] -->
m

<!-- b005866 | prose | pages [21] -->
m

<!-- b005867 | prose | pages [21] -->
m

<!-- b005868 | prose | pages [21] -->
m

<!-- b005869 | prose | pages [21] -->
m

<!-- b005870 | prose | pages [21] -->
m

<!-- b005871 | prose | pages [21] -->
m

<!-- b005872 | prose | pages [21] -->
m

<!-- b005873 | prose | pages [21] -->
m

<!-- b005874 | prose | pages [21] -->
m

<!-- b005875 | prose | pages [21] -->
m

<!-- b005876 | prose | pages [21] -->
m

<!-- b005877 | prose | pages [21] -->
m

<!-- b005878 | prose | pages [21] -->
m

<!-- b005879 | prose | pages [21] -->
m

<!-- b005880 | prose | pages [21] -->
m

<!-- b005881 | prose | pages [21] -->
m

<!-- b005882 | prose | pages [21] -->
m

<!-- b005883 | prose | pages [21] -->
m

<!-- b005884 | prose | pages [21] -->
m

<!-- b005885 | prose | pages [21] -->
m

<!-- b005886 | prose | pages [21] -->
m

<!-- b005887 | prose | pages [21] -->
m

<!-- b005888 | prose | pages [21] -->
m

<!-- b005889 | prose | pages [21] -->
m

<!-- b005890 | prose | pages [21] -->
m

<!-- b005891 | prose | pages [21] -->
m

<!-- b005892 | prose | pages [21] -->
m

<!-- b005893 | prose | pages [21] -->
m

<!-- b005894 | prose | pages [21] -->
m

<!-- b005895 | prose | pages [21] -->
m

<!-- b005896 | prose | pages [21] -->
m

<!-- b005897 | prose | pages [21] -->
m

<!-- b005898 | prose | pages [21] -->
m

<!-- b005899 | prose | pages [21] -->
m

<!-- b005900 | prose | pages [21] -->
m

<!-- b005901 | prose | pages [21] -->
m

<!-- b005902 | prose | pages [21] -->
m

<!-- b005903 | prose | pages [21] -->
m

<!-- b005904 | prose | pages [21] -->
m

<!-- b005905 | prose | pages [21] -->
m

<!-- b005906 | prose | pages [21] -->
m

<!-- b005907 | prose | pages [21] -->
m

<!-- b005908 | prose | pages [21] -->
m

<!-- b005909 | prose | pages [21] -->
m

<!-- b005910 | prose | pages [21] -->
m

<!-- b005911 | prose | pages [21] -->
m

<!-- b005912 | prose | pages [21] -->
m

<!-- b005913 | prose | pages [21] -->
m

<!-- b005914 | prose | pages [21] -->
m

<!-- b005915 | prose | pages [21] -->
m

<!-- b005916 | prose | pages [21] -->
m

<!-- b005917 | prose | pages [21] -->
m

<!-- b005918 | prose | pages [21] -->
m

<!-- b005919 | prose | pages [21] -->
m

<!-- b005920 | prose | pages [21] -->
m

<!-- b005921 | prose | pages [21] -->
m

<!-- b005922 | prose | pages [21] -->
m

<!-- b005923 | prose | pages [21] -->
m

<!-- b005924 | prose | pages [21] -->
m

<!-- b005925 | prose | pages [21] -->
m

<!-- b005926 | prose | pages [21] -->
m

<!-- b005927 | prose | pages [21] -->
m

<!-- b005928 | prose | pages [21] -->
m

<!-- b005929 | prose | pages [21] -->
m

<!-- b005930 | prose | pages [21] -->
m

<!-- b005931 | prose | pages [21] -->
m

<!-- b005932 | prose | pages [21] -->
m

<!-- b005933 | prose | pages [21] -->
m

<!-- b005934 | prose | pages [21] -->
m

<!-- b005935 | prose | pages [21] -->
m

<!-- b005936 | prose | pages [21] -->
m

<!-- b005937 | prose | pages [21] -->
m

<!-- b005938 | prose | pages [21] -->
m

<!-- b005939 | prose | pages [21] -->
m

<!-- b005940 | prose | pages [21] -->
m

<!-- b005941 | prose | pages [21] -->
m

<!-- b005942 | prose | pages [21] -->
m

<!-- b005943 | prose | pages [21] -->
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

<!-- b005957 | furniture | pages [21] -->
m

<!-- b005958 | furniture | pages [21] -->
m

<!-- b005959 | furniture | pages [21] -->
m

<!-- b005960 | furniture | pages [21] -->
m

<!-- b005961 | furniture | pages [21] -->
m

<!-- b005962 | furniture | pages [21] -->
m

<!-- b005963 | furniture | pages [21] -->
m

<!-- b005964 | furniture | pages [21] -->
m

<!-- b005965 | furniture | pages [21] -->
m

<!-- b005966 | furniture | pages [21] -->
m

<!-- b005967 | furniture | pages [21] -->
m

<!-- b005968 | furniture | pages [21] -->
m

<!-- b005969 | furniture | pages [21] -->
m

<!-- b005970 | furniture | pages [21] -->
m

<!-- b005971 | furniture | pages [21] -->
m

<!-- b005972 | furniture | pages [21] -->
m

<!-- b005973 | furniture | pages [21] -->
m

<!-- b005974 | furniture | pages [21] -->
m

<!-- b005975 | furniture | pages [21] -->
m

<!-- b005976 | furniture | pages [21] -->
m

<!-- b005977 | furniture | pages [21] -->
m

<!-- b005978 | furniture | pages [21] -->
m

<!-- b005979 | furniture | pages [21] -->
m

<!-- b005980 | furniture | pages [21] -->
m

<!-- b005981 | furniture | pages [21] -->
m

<!-- b005982 | furniture | pages [21] -->
m

<!-- b005983 | furniture | pages [21] -->
m

<!-- b005984 | furniture | pages [21] -->
m

<!-- b005985 | furniture | pages [21] -->
m

<!-- b005986 | furniture | pages [21] -->
m

<!-- b005987 | furniture | pages [21] -->
m

<!-- b005988 | furniture | pages [21] -->
m

<!-- b005989 | furniture | pages [21] -->
m

<!-- b005990 | furniture | pages [21] -->
m

<!-- b005991 | furniture | pages [21] -->
m

<!-- b005992 | furniture | pages [21] -->
m

<!-- b005993 | furniture | pages [21] -->
m

<!-- b005994 | furniture | pages [21] -->
m

<!-- b005995 | furniture | pages [21] -->
m

<!-- b005996 | furniture | pages [21] -->
m

<!-- b005997 | furniture | pages [21] -->
m

<!-- b005998 | furniture | pages [21] -->
m

<!-- b005999 | furniture | pages [21] -->
m

<!-- b006000 | furniture | pages [21] -->
m

<!-- b006001 | furniture | pages [21] -->
m

<!-- b006002 | furniture | pages [21] -->
m

<!-- b006003 | furniture | pages [21] -->
m

<!-- b006004 | furniture | pages [21] -->
m

<!-- b006005 | furniture | pages [21] -->
m

<!-- b006006 | furniture | pages [21] -->
m

<!-- b006007 | furniture | pages [21] -->
m

<!-- b006008 | furniture | pages [21] -->
m

<!-- b006009 | furniture | pages [21] -->
m

<!-- b006010 | furniture | pages [21] -->
m

<!-- b006011 | furniture | pages [21] -->
m

<!-- b006012 | furniture | pages [21] -->
m

<!-- b006013 | furniture | pages [21] -->
m

<!-- b006014 | furniture | pages [21] -->
m

<!-- b006015 | furniture | pages [21] -->
m

<!-- b006016 | furniture | pages [21] -->
m

<!-- b006017 | furniture | pages [21] -->
m

<!-- b006018 | furniture | pages [21] -->
m

<!-- b006019 | furniture | pages [21] -->
m

<!-- b006020 | furniture | pages [21] -->
m

<!-- b006021 | furniture | pages [21] -->
m

<!-- b006022 | furniture | pages [21] -->
m

<!-- b006023 | furniture | pages [21] -->
m

<!-- b006024 | furniture | pages [21] -->
m

<!-- b006025 | furniture | pages [21] -->
m

<!-- b006026 | furniture | pages [21] -->
m

<!-- b006027 | furniture | pages [21] -->
m

<!-- b006028 | furniture | pages [21] -->
m

<!-- b006029 | furniture | pages [21] -->
m

<!-- b006030 | furniture | pages [21] -->
m

<!-- b006031 | furniture | pages [21] -->
m

<!-- b006032 | furniture | pages [21] -->
m

<!-- b006033 | furniture | pages [21] -->
m

<!-- b006034 | furniture | pages [21] -->
m

<!-- b006035 | furniture | pages [21] -->
m

<!-- b006036 | furniture | pages [21] -->
m

<!-- b006037 | furniture | pages [21] -->
m

<!-- b006038 | furniture | pages [21] -->
m

<!-- b006039 | furniture | pages [21] -->
m

<!-- b006040 | furniture | pages [21] -->
m

<!-- b006041 | furniture | pages [21] -->
m

<!-- b006042 | furniture | pages [21] -->
m

<!-- b006043 | furniture | pages [21] -->
m

<!-- b006044 | furniture | pages [21] -->
m

<!-- b006045 | furniture | pages [21] -->
m

<!-- b006046 | furniture | pages [21] -->
m

<!-- b006047 | furniture | pages [21] -->
m

<!-- b006048 | furniture | pages [21] -->
m

<!-- b006049 | furniture | pages [21] -->
m

<!-- b006050 | furniture | pages [21] -->
m

<!-- b006051 | furniture | pages [21] -->
m

<!-- b006052 | furniture | pages [21] -->
m

<!-- b006053 | furniture | pages [21] -->
m

<!-- b006054 | furniture | pages [21] -->
m

<!-- b006055 | furniture | pages [21] -->
m

<!-- b006056 | furniture | pages [21] -->
m

<!-- b006057 | furniture | pages [21] -->
m

<!-- b006058 | furniture | pages [21] -->
m

<!-- b006059 | furniture | pages [21] -->
m

<!-- b006060 | furniture | pages [21] -->
m

<!-- b006061 | furniture | pages [21] -->
m

<!-- b006062 | furniture | pages [21] -->
m

<!-- b006063 | furniture | pages [21] -->
m

<!-- b006064 | furniture | pages [21] -->
m

<!-- b006065 | furniture | pages [21] -->
m

<!-- b006066 | furniture | pages [21] -->
m

<!-- b006067 | furniture | pages [21] -->
m

<!-- b006068 | furniture | pages [21] -->
m

<!-- b006069 | furniture | pages [21] -->
m

<!-- b006070 | furniture | pages [21] -->
m

<!-- b006071 | furniture | pages [21] -->
m

<!-- b006072 | furniture | pages [21] -->
m

<!-- b006073 | furniture | pages [21] -->
m

<!-- b006074 | furniture | pages [21] -->
m

<!-- b006075 | furniture | pages [21] -->
m

<!-- b006076 | furniture | pages [21] -->
m

<!-- b006077 | furniture | pages [21] -->
m

<!-- b006078 | furniture | pages [21] -->
m

<!-- b006079 | furniture | pages [21] -->
m

<!-- b006080 | furniture | pages [21] -->
m

<!-- b006081 | furniture | pages [21] -->
m

<!-- b006082 | furniture | pages [21] -->
m

<!-- b006083 | furniture | pages [21] -->
m

<!-- b006084 | furniture | pages [21] -->
m

<!-- b006085 | furniture | pages [21] -->
m

<!-- b006086 | furniture | pages [21] -->
m

<!-- b006087 | furniture | pages [21] -->
m

<!-- b006088 | furniture | pages [21] -->
m

<!-- b006089 | furniture | pages [21] -->
m

<!-- b006090 | furniture | pages [21] -->
m

<!-- b006091 | furniture | pages [21] -->
m

<!-- b006092 | furniture | pages [21] -->
m

<!-- b006093 | furniture | pages [21] -->
m

<!-- b006094 | furniture | pages [21] -->
m

<!-- b006095 | furniture | pages [21] -->
m

<!-- b006096 | furniture | pages [21] -->
m

<!-- b006097 | furniture | pages [21] -->
m

<!-- b006098 | furniture | pages [21] -->
m

<!-- b006099 | furniture | pages [21] -->
m

<!-- b006100 | furniture | pages [21] -->
m

<!-- b006101 | furniture | pages [21] -->
m

<!-- b006102 | furniture | pages [21] -->
m

<!-- b006103 | furniture | pages [21] -->
m

<!-- b006104 | furniture | pages [21] -->
m

<!-- b006105 | furniture | pages [21] -->
m

<!-- b006106 | furniture | pages [21] -->
m

<!-- b006107 | furniture | pages [21] -->
m

<!-- b006108 | furniture | pages [21] -->
m

<!-- b006109 | furniture | pages [21] -->
m

<!-- b006110 | furniture | pages [21] -->
m

<!-- b006111 | furniture | pages [21] -->
m

<!-- b006112 | furniture | pages [21] -->
m

<!-- b006113 | furniture | pages [21] -->
m

<!-- b006114 | furniture | pages [21] -->
m

<!-- b006115 | furniture | pages [21] -->
m

<!-- b006116 | furniture | pages [21] -->
m

<!-- b006117 | furniture | pages [21] -->
m

<!-- b006118 | furniture | pages [21] -->
m

<!-- b006119 | furniture | pages [21] -->
m

<!-- b006120 | furniture | pages [21] -->
m

<!-- b006121 | furniture | pages [21] -->
m

<!-- b006122 | furniture | pages [21] -->
m

<!-- b006123 | furniture | pages [21] -->
m

<!-- b006124 | furniture | pages [21] -->
m

<!-- b006125 | furniture | pages [21] -->
m

<!-- b006126 | furniture | pages [21] -->
m

<!-- b006127 | furniture | pages [21] -->
m

<!-- b006128 | furniture | pages [21] -->
m

<!-- b006129 | furniture | pages [21] -->
m

<!-- b006130 | furniture | pages [21] -->
m

<!-- b006131 | furniture | pages [21] -->
m

<!-- b006132 | furniture | pages [21] -->
m

<!-- b006133 | furniture | pages [21] -->
m

<!-- b006134 | furniture | pages [21] -->
m

<!-- b006135 | furniture | pages [21] -->
m

<!-- b006136 | furniture | pages [21] -->
m

<!-- b006137 | furniture | pages [21] -->
m

<!-- b006138 | furniture | pages [21] -->
m

<!-- b006139 | furniture | pages [21] -->
m

<!-- b006140 | furniture | pages [21] -->
m

<!-- b006141 | furniture | pages [21] -->
m

<!-- b006142 | furniture | pages [21] -->
m

<!-- b006143 | furniture | pages [21] -->
m

<!-- b006144 | furniture | pages [21] -->
m

<!-- b006145 | furniture | pages [21] -->
m

<!-- b006146 | furniture | pages [21] -->
m

<!-- b006147 | furniture | pages [21] -->
m

<!-- b006148 | furniture | pages [21] -->
m

<!-- b006149 | furniture | pages [21] -->
m

<!-- b006150 | furniture | pages [21] -->
m

<!-- b006151 | furniture | pages [21] -->
m

<!-- b006152 | furniture | pages [21] -->
m

<!-- b006153 | furniture | pages [21] -->
m

<!-- b006154 | furniture | pages [21] -->
m

<!-- b006155 | furniture | pages [21] -->
m

<!-- b006156 | furniture | pages [21] -->
m

<!-- b006157 | furniture | pages [21] -->
m

<!-- b006158 | furniture | pages [21] -->
m

<!-- b006159 | furniture | pages [21] -->
m

<!-- b006160 | furniture | pages [21] -->
m

<!-- b006161 | furniture | pages [21] -->
m

<!-- b006162 | furniture | pages [21] -->
m

<!-- b006163 | furniture | pages [21] -->
m

<!-- b006164 | furniture | pages [21] -->
m

<!-- b006165 | furniture | pages [21] -->
m

<!-- b006166 | furniture | pages [21] -->
m

<!-- b006167 | furniture | pages [21] -->
m

<!-- b006168 | furniture | pages [21] -->
m

<!-- b006169 | furniture | pages [21] -->
m

<!-- b006170 | furniture | pages [21] -->
m

<!-- b006171 | furniture | pages [21] -->
m

<!-- b006172 | furniture | pages [21] -->
m

<!-- b006173 | furniture | pages [21] -->
m

<!-- b006174 | furniture | pages [21] -->
m

<!-- b006175 | furniture | pages [21] -->
m

<!-- b006176 | furniture | pages [21] -->
m

<!-- b006177 | furniture | pages [21] -->
m

<!-- b006178 | furniture | pages [21] -->
m

<!-- b006179 | furniture | pages [21] -->
m

<!-- b006180 | furniture | pages [21] -->
m

<!-- b006181 | furniture | pages [21] -->
m

<!-- b006182 | furniture | pages [21] -->
m

<!-- b006183 | furniture | pages [21] -->
m

<!-- b006184 | furniture | pages [21] -->
m

<!-- b006185 | furniture | pages [21] -->
m

<!-- b006186 | furniture | pages [21] -->
m

<!-- b006187 | furniture | pages [21] -->
m

<!-- b006188 | furniture | pages [21] -->
m

<!-- b006189 | furniture | pages [21] -->
m

<!-- b006190 | furniture | pages [21] -->
m

<!-- b006191 | furniture | pages [21] -->
m

<!-- b006192 | furniture | pages [21] -->
m

<!-- b006193 | furniture | pages [21] -->
m

<!-- b006194 | furniture | pages [21] -->
m

<!-- b006195 | furniture | pages [21] -->
m

<!-- b006196 | furniture | pages [21] -->
m

<!-- b006197 | furniture | pages [21] -->
m

<!-- b006198 | furniture | pages [21] -->
m

<!-- b006199 | furniture | pages [21] -->
m

<!-- b006200 | furniture | pages [21] -->
m

<!-- b006201 | furniture | pages [21] -->
m

<!-- b006202 | furniture | pages [21] -->
m

<!-- b006203 | furniture | pages [21] -->
m

<!-- b006204 | furniture | pages [21] -->
m

<!-- b006205 | furniture | pages [21] -->
m

<!-- b006206 | furniture | pages [21] -->
m

<!-- b006207 | furniture | pages [21] -->
m

<!-- b006208 | furniture | pages [21] -->
m

<!-- b006209 | furniture | pages [21] -->
m

<!-- b006210 | furniture | pages [21] -->
m

<!-- b006211 | furniture | pages [21] -->
m

<!-- b006212 | furniture | pages [21] -->
m

<!-- b006213 | furniture | pages [21] -->
m

<!-- b006214 | furniture | pages [21] -->
m

<!-- b006215 | furniture | pages [21] -->
m

<!-- b006216 | furniture | pages [21] -->
m

<!-- b006217 | furniture | pages [21] -->
m

<!-- b006218 | furniture | pages [21] -->
m

<!-- b006219 | furniture | pages [21] -->
m

<!-- b006220 | furniture | pages [21] -->
m

<!-- b006221 | furniture | pages [21] -->
m

<!-- b006222 | furniture | pages [21] -->
m

<!-- b006223 | furniture | pages [21] -->
m

<!-- b006224 | furniture | pages [21] -->
m

<!-- b006225 | furniture | pages [21] -->
m

<!-- b006226 | furniture | pages [21] -->
m

<!-- b006227 | furniture | pages [21] -->
m

<!-- b006228 | furniture | pages [21] -->
m

<!-- b006229 | furniture | pages [21] -->
m

<!-- b006230 | furniture | pages [21] -->
m

<!-- b006231 | furniture | pages [21] -->
m

<!-- b006232 | furniture | pages [21] -->
m

<!-- b006233 | furniture | pages [21] -->
m

<!-- b006234 | furniture | pages [21] -->
m

<!-- b006235 | furniture | pages [21] -->
m

<!-- b006236 | furniture | pages [21] -->
m

<!-- b006237 | furniture | pages [21] -->
m

<!-- b006238 | furniture | pages [21] -->
m

<!-- b006239 | furniture | pages [21] -->
m

<!-- b006240 | furniture | pages [21] -->
m

<!-- b006241 | furniture | pages [21] -->
m

<!-- b006242 | furniture | pages [21] -->
m

<!-- b006243 | furniture | pages [21] -->
m

<!-- b006244 | furniture | pages [21] -->
m

<!-- b006245 | furniture | pages [21] -->
m

<!-- b006246 | furniture | pages [21] -->
m

<!-- b006247 | furniture | pages [21] -->
m

<!-- b006248 | furniture | pages [21] -->
m

<!-- b006249 | furniture | pages [21] -->
m

<!-- b006250 | furniture | pages [21] -->
m

<!-- b006251 | furniture | pages [21] -->
m

<!-- b006252 | furniture | pages [21] -->
m

<!-- b006253 | furniture | pages [21] -->
m

<!-- b006254 | furniture | pages [21] -->
m

<!-- b006255 | furniture | pages [21] -->
m

<!-- b006256 | furniture | pages [21] -->
m

<!-- b006257 | furniture | pages [21] -->
m

<!-- b006258 | furniture | pages [21] -->
m

<!-- b006259 | furniture | pages [21] -->
m

<!-- b006260 | furniture | pages [21] -->
m

<!-- b006261 | furniture | pages [21] -->
m

<!-- b006262 | furniture | pages [21] -->
m

<!-- b006263 | furniture | pages [21] -->
m

<!-- b006264 | furniture | pages [21] -->
m

<!-- b006265 | furniture | pages [21] -->
m

<!-- b006266 | furniture | pages [21] -->
m

<!-- b006267 | furniture | pages [21] -->
m

<!-- b006268 | furniture | pages [21] -->
m

<!-- b006269 | furniture | pages [21] -->
m

<!-- b006270 | furniture | pages [21] -->
m

<!-- b006271 | furniture | pages [21] -->
m

<!-- b006272 | furniture | pages [21] -->
m

<!-- b006273 | furniture | pages [21] -->
m

<!-- b006274 | furniture | pages [21] -->
m

<!-- b006275 | furniture | pages [21] -->
m

<!-- b006276 | furniture | pages [21] -->
m

<!-- b006277 | furniture | pages [21] -->
m

<!-- b006278 | furniture | pages [21] -->
m

<!-- b006279 | furniture | pages [21] -->
m

<!-- b006280 | furniture | pages [21] -->
m

<!-- b006281 | furniture | pages [21] -->
m

<!-- b006282 | furniture | pages [21] -->
m

<!-- b006283 | furniture | pages [21] -->
m

<!-- b006284 | furniture | pages [21] -->
m

<!-- b006285 | furniture | pages [21] -->
m

<!-- b006286 | furniture | pages [21] -->
m

<!-- b006287 | furniture | pages [21] -->
m

<!-- b006288 | furniture | pages [21] -->
m

<!-- b006289 | furniture | pages [21] -->
m

<!-- b006290 | furniture | pages [21] -->
m

<!-- b006291 | furniture | pages [21] -->
m

<!-- b006292 | furniture | pages [21] -->
m

<!-- b006293 | furniture | pages [21] -->
m

<!-- b006294 | furniture | pages [21] -->
m

<!-- b006295 | furniture | pages [21] -->
m

<!-- b006296 | furniture | pages [21] -->
m

<!-- b006297 | furniture | pages [21] -->
m

<!-- b006298 | furniture | pages [21] -->
m

<!-- b006299 | furniture | pages [21] -->
m

<!-- b006300 | furniture | pages [21] -->
m

<!-- b006301 | furniture | pages [21] -->
m

<!-- b006302 | furniture | pages [21] -->
m

<!-- b006303 | furniture | pages [21] -->
m

<!-- b006304 | furniture | pages [21] -->
m

<!-- b006305 | furniture | pages [21] -->
m

<!-- b006306 | furniture | pages [21] -->
m

<!-- b006307 | furniture | pages [21] -->
m

<!-- b006308 | furniture | pages [21] -->
m

<!-- b006309 | furniture | pages [21] -->
m

<!-- b006310 | furniture | pages [21] -->
m

<!-- b006311 | furniture | pages [21] -->
m

<!-- b006312 | furniture | pages [21] -->
m

<!-- b006313 | furniture | pages [21] -->
m

<!-- b006314 | furniture | pages [21] -->
m

<!-- b006315 | furniture | pages [21] -->
m

<!-- b006316 | furniture | pages [21] -->
m

<!-- b006317 | furniture | pages [21] -->
m

<!-- b006318 | furniture | pages [21] -->
m

<!-- b006319 | furniture | pages [21] -->
m

<!-- b006320 | furniture | pages [21] -->
m

<!-- b006321 | furniture | pages [21] -->
m

<!-- b006322 | furniture | pages [21] -->
m

<!-- b006323 | furniture | pages [21] -->
m

<!-- b006324 | furniture | pages [21] -->
m

<!-- b006325 | furniture | pages [21] -->
m

<!-- b006326 | furniture | pages [21] -->
m

<!-- b006327 | furniture | pages [21] -->
m

<!-- b006328 | furniture | pages [21] -->
m

<!-- b006329 | furniture | pages [21] -->
m

<!-- b006330 | furniture | pages [21] -->
m

<!-- b006331 | furniture | pages [21] -->
m

<!-- b006332 | furniture | pages [21] -->
m

<!-- b006333 | furniture | pages [21] -->
m

<!-- b006334 | furniture | pages [21] -->
m

<!-- b006335 | furniture | pages [21] -->
m

<!-- b006336 | furniture | pages [21] -->
m

<!-- b006337 | furniture | pages [21] -->
m

<!-- b006338 | furniture | pages [21] -->
m

<!-- b006339 | furniture | pages [21] -->
m

<!-- b006340 | furniture | pages [21] -->
m

<!-- b006341 | furniture | pages [21] -->
m

<!-- b006342 | furniture | pages [21] -->
m

<!-- b006343 | furniture | pages [21] -->
m

<!-- b006344 | furniture | pages [21] -->
m

<!-- b006345 | furniture | pages [21] -->
m

<!-- b006346 | furniture | pages [21] -->
m

<!-- b006347 | furniture | pages [22] -->
Team 2517690

<!-- b006348 | furniture | pages [22] -->


<!-- b006349 | furniture | pages [22] -->


<!-- b006350 | furniture | pages [22] -->


<!-- b006351 | furniture | pages [22] -->


<!-- b006352 | furniture | pages [22] -->


<!-- b006353 | furniture | pages [22] -->


<!-- b006354 | furniture | pages [22] -->


<!-- b006355 | furniture | pages [22] -->


<!-- b006356 | furniture | pages [22] -->


<!-- b006357 | furniture | pages [22] -->


<!-- b006358 | furniture | pages [22] -->


<!-- b006359 | furniture | pages [22] -->


<!-- b006360 | furniture | pages [22] -->


<!-- b006361 | furniture | pages [22] -->


<!-- b006362 | furniture | pages [22] -->
Page 22 of 25

<!-- b006363 | prose | pages [22] -->
From the perspective of game theory, the status of the host country actually provides a unique strategic gaming opportunity for the host nation.

<!-- b006364 | heading | pages [22] -->
7.3.1 N-player game

<!-- b006365 | prose | pages [22] -->
In a multi-party game[7], the goal of each player is usually to maximize their own utility (such as winning more medals), and the strategic choices of each player will affect the outcomes of other players. Therefore, the overall outcome of the game depends not only on the strategy of each individual player but also on the combination of strategies of all players. This requires us to take into account the interaction of the strategies of each player during the analysis. Suppose there are multiple countries involved, in- cluding the host country and other participating countries. Each country has its own "strategy space", that is, choosing which events to compete for medals and maximizing its own interests (the number of medals) through strategic choices.

<!-- b006366 | prose | pages [22] -->
Figure 15：N-Player Game Composition

<!-- b006367 | heading | pages [22] -->
7.3.2 The strategies chosen by the host country and

<!-- b006368 | prose | pages [22] -->
other countries

<!-- b006369 | prose | pages [22] -->
⚫ Strategies of the host country: The host country can create more medal opportunities in

<!-- b006370 | prose | pages [22] -->
its own advantageous events. For example, it can increase the number of matches in certain competitions or optimize the competition format to enhance the probability of its own ath- letes winning medals. The host country can also use its control over the schedule to reduce the competition pressure on foreign athletes or increase the training time for its own ath- letes. Strategies of other countries: Other countries will decide their investment in certain ⚫ events based on the choices made by the host country. If the host country dominates in certain events, other countries may choose to avoid these events and instead allocate more resources to other events, especially those in which the host country may not have an edge.

<!-- b006371 | heading | pages [22] -->
7.3.3 Nash Equilibrium

<!-- b006372 | prose | pages [22] -->
Ultimately, this game will tend towards an equilibrium state[8]. In this state, each country's strategy reaches its best response strategy. That is, considering the choices of other countries, neither the host country nor other participating countries can increase their medal counts by unilaterally changing their own strategies. Under this equilibrium, the strategic choices of countries will influence each other and jointly determine the final medal distribution.

<!-- b006373 | heading | pages [22] -->
8 Sensitivity Analysis and Error Analysis

<!-- b006374 | heading | pages [22] -->
8.1 Sensitivity Analysis

<!-- b006375 | prose | pages [22] -->
We examined the sensitivity of the classification results by changing the number of folds for cross-validation of the logistic regression model. The number of folds for cross-testing is set to be 8, 9, 10, 11, respectively. The coefficient of variation of the classification results is detected to judge whether the model is robust or not.

<!-- b006376 | prose | pages [22] -->
Introducing the coefficient of variation , define：

<!-- b006377 | furniture | pages [22] -->


<!-- b006378 | prose | pages [22] -->
关注数学模型

<!-- b006379 | furniture | pages [22] -->
2

<!-- b006380 | furniture | pages [22] -->
MATHmodels

<!-- b006381 | furniture | pages [22] -->
获取更多资讯

<!-- b006382 | furniture | pages [23] -->
Team 2517690

<!-- b006383 | furniture | pages [23] -->


<!-- b006384 | furniture | pages [23] -->


<!-- b006385 | furniture | pages [23] -->


<!-- b006386 | furniture | pages [23] -->


<!-- b006387 | furniture | pages [23] -->


<!-- b006388 | furniture | pages [23] -->


<!-- b006389 | furniture | pages [23] -->


<!-- b006390 | prose | pages [23] -->


<!-- b006391 | furniture | pages [23] -->


<!-- b006392 | furniture | pages [23] -->


<!-- b006393 | furniture | pages [23] -->


<!-- b006394 | furniture | pages [23] -->


<!-- b006395 | furniture | pages [23] -->


<!-- b006396 | furniture | pages [23] -->


<!-- b006397 | furniture | pages [23] -->


<!-- b006398 | furniture | pages [23] -->


<!-- b006399 | furniture | pages [23] -->
Page 23 of 25

<!-- b006400 | prose | pages [23] -->


<!-- b006401 | prose | pages [23] -->
(21)

<!-- b006402 | prose | pages [23] -->
= =

<!-- b006403 | furniture | pages [23] -->


<!-- b006404 | furniture | pages [23] -->


<!-- b006405 | prose | pages [23] -->


<!-- b006406 | prose | pages [23] -->
Where  represents the accuracy of the model cross-validated at 10 fold of the original scheme， indicates the absolute value of the change in the accuracy rate after changing the number of folds.

<!-- b006407 | caption | pages [23] -->
Table12  Relationship between cross-test and coefficient of variation

<!-- b006408 | prose | pages [23] -->
Cross-checking Folds

<!-- b006409 | prose | pages [23] -->
8

<!-- b006410 | prose | pages [23] -->
coefficient of variatio 

<!-- b006411 | prose | pages [23] -->
5%

<!-- b006412 | prose | pages [23] -->
微信公众号：数学模型

<!-- b006413 | prose | pages [23] -->
9 11 0 3.46% From the above table, we can see that changing the number of cross folds changes the accuracy of the trained model within 5%, which indicates that the change in accuracy is not significant. Thus, this model is robust.

<!-- b006414 | heading | pages [23] -->
8.2 Error Analysis

<!-- b006415 | prose | pages [23] -->
In order to assess the prediction accuracy of the Random Forest regression model used in this study, a detailed error analysis was performed. By analyzing the performance of the model

<!-- b006416 | prose | pages [23] -->
微信号：MATHmodels

<!-- b006417 | prose | pages [23] -->
on the test set, it is possible to get a better understanding of the generalization ability and sta- bility of the model under different conditions. And in this section, the error of the model is presented through visual graphs.

<!-- b006418 | prose | pages [23] -->
Firstly, we assessed the prediction accuracy of the model by plotting the true values of the test set against the fitted values of the model as follows：

<!-- b006419 | furniture | pages [23] -->


<!-- b006420 | prose | pages [23] -->
Figure 16：Comparision of test set prediction results

<!-- b006421 | prose | pages [23] -->
As can be seen from the figure, the model performs relatively accurately in predicting the number of medals for most countries, with small errors between the true and fitted values. However, some countries have relatively large prediction errors, which may be related to the characteristics of some specific events, data noise, or underfitting of the model to some varia- bles.

<!-- b006422 | furniture | pages [23] -->


<!-- b006423 | furniture | pages [24] -->
Team 2517690

<!-- b006424 | furniture | pages [24] -->


<!-- b006425 | furniture | pages [24] -->


<!-- b006426 | furniture | pages [24] -->


<!-- b006427 | furniture | pages [24] -->


<!-- b006428 | furniture | pages [24] -->


<!-- b006429 | furniture | pages [24] -->


<!-- b006430 | furniture | pages [24] -->


<!-- b006431 | furniture | pages [24] -->


<!-- b006432 | furniture | pages [24] -->


<!-- b006433 | furniture | pages [24] -->


<!-- b006434 | furniture | pages [24] -->


<!-- b006435 | furniture | pages [24] -->


<!-- b006436 | furniture | pages [24] -->


<!-- b006437 | furniture | pages [24] -->


<!-- b006438 | furniture | pages [24] -->
Page 24 of 25

<!-- b006439 | prose | pages [24] -->
To further analyze the performance of the Random Forest regression model, we explored the effect of the number of decision trees on the model error. We plotted the relationship be- tween the number of decision trees and the error as follows：

<!-- b006440 | furniture | pages [24] -->


<!-- b006441 | prose | pages [24] -->
Figure 17：Plot of the relationship between the number of decision trees and error

<!-- b006442 | prose | pages [24] -->
It can be observed from the figure that the error of the model gradually decreases as the number of decision trees increases, indicating that more decision trees help to improve the stability and accuracy of the model. When the number of decision trees reaches a certain value, the decrease of the error tends to level off, indicating that the fitting ability of the model is close to saturation at this point, and further increasing the number of decision trees has a limited effect on the improvement of the error.

<!-- b006443 | heading | pages [24] -->
9 Strengths and Weaknesses

<!-- b006444 | heading | pages [24] -->
9.1 Strengths

<!-- b006445 | prose | pages [24] -->
⚫ The model we proposed makes full use of official data and analyses the data in depth, and the results of the study are highly informative and can be applied to future predictions about Olympic medals. ⚫ Random forests are more accurate, robust, and less prone to overfitting, and are used to predict the 2028 Olympic medal table with less error. ⚫ We use logistic regression to predict the probability of first-time winners for non-winning countries, taking full account of relevant factors, and is relatively robust to outliers, with reliable results. ⚫ The use of two-sample mean hypothesis tests and chi-square tests to simultaneously ana- lyse the “great coach” effect reduces chance error and produces convincing results.

<!-- b006446 | heading | pages [24] -->
9.2 Weaknesses

<!-- b006447 | prose | pages [24] -->
⚫ The model we presented is very comprehensive in its consideration of the problem indi- cators, but the lack of data for some of the indicators may make the results subject to some errors.

<!-- b006448 | furniture | pages [24] -->


<!-- b006449 | prose | pages [24] -->
关注数学模型

<!-- b006450 | furniture | pages [24] -->
2

<!-- b006451 | furniture | pages [24] -->
MATHmodels

<!-- b006452 | furniture | pages [24] -->
获取更多资讯

<!-- b006453 | furniture | pages [25] -->
Team 2517690

<!-- b006454 | furniture | pages [25] -->


<!-- b006455 | furniture | pages [25] -->


<!-- b006456 | furniture | pages [25] -->


<!-- b006457 | furniture | pages [25] -->


<!-- b006458 | furniture | pages [25] -->


<!-- b006459 | furniture | pages [25] -->


<!-- b006460 | furniture | pages [25] -->


<!-- b006461 | furniture | pages [25] -->


<!-- b006462 | furniture | pages [25] -->


<!-- b006463 | furniture | pages [25] -->


<!-- b006464 | furniture | pages [25] -->


<!-- b006465 | furniture | pages [25] -->


<!-- b006466 | furniture | pages [25] -->


<!-- b006467 | furniture | pages [25] -->


<!-- b006468 | furniture | pages [25] -->
Page 25 of 25

<!-- b006469 | heading | pages [25] -->
10 Conclusion

<!-- b006470 | prose | pages [25] -->
We performed a multi-dimensional analysis of factors affecting Olympic medal counts and developed a machine learning prediction model. Key factors such as athlete performance, event types, host status, and participation were found to influence medal outcomes. The Ran- dom Forest regression model demonstrated high accuracy, with predictions for the 2028 Olym- pics indicating continued dominance by the U.S. and China, while Japan's gold medal count may decline.

<!-- b006471 | prose | pages [25] -->
Grey correlation analysis reveals performance differences across disciplines, helping countries identify competitive areas. The study emphasizes the impact of host status on medal

<!-- b006472 | prose | pages [25] -->
微信公众号：数学模型

<!-- b006473 | prose | pages [25] -->
counts, particularly for the U.S. at the 2028 Los Angeles Olympics, where new sports may boost medal potential. Overall, the findings offer a scientific basis for the Olympic Committee to optimize training and resource allocation strategies.

<!-- b006474 | heading | pages [25] -->
References

<!-- b006475 | references | pages [25] -->
[1] Nagpal P , Gupta K , Verma Y ,et al.Paris Olympic (2024) Medal Tally Predic-

<!-- b006476 | references | pages [25] -->
tion[C]//International Conference on Data Management, Analytics & Innovation.Springer, Sin-

<!-- b006477 | references | pages [25] -->
gapore, 2023.

<!-- b006478 | references | pages [25] -->
微信号：MATHmodels

<!-- b006479 | references | pages [25] -->
[2] Song, Z. (2024).Prediction of the Number and Trend of Olympic Medals Won by Var-

<!-- b006480 | references | pages [25] -->
ious Countries Based on Neural Networks.Applied and Computational Engineering,109,87-91.

<!-- b006481 | references | pages [25] -->
[3] J. Moolchandani, V. Chole, S. Sahu, R. Kumar, A. Shukla and A. Kumar, "Predictive

<!-- b006482 | references | pages [25] -->
Analytics in Sports: Using Machine Learning to Forecast Outcomes and Medal Tally Trends at

<!-- b006483 | references | pages [25] -->
the 2024 Summer Olympics," 2024 4th International Conference on Technological Advance-

<!-- b006484 | references | pages [25] -->
ments in Computational Sciences (ICTACS), Tashkent, Uzbekistan, 2024, pp. 1987-1992.

<!-- b006485 | references | pages [25] -->
[4]Tomz M , King G , Zeng L .ReLogit: Rare Events Logistic Regression[J].Journal of

<!-- b006486 | references | pages [25] -->
Statistical Software, 2003, 008.

<!-- b006487 | references | pages [25] -->
[5]Zhou L, Wang Y, An G, et al. Multi-objective grey correlation analysis based on CFRP

<!-- b006488 | references | pages [25] -->
Helical Milling simulation model[J]. The International Journal of Advanced Manufacturing

<!-- b006489 | references | pages [25] -->
Technology, 2024: 1-21.

<!-- b006490 | references | pages [25] -->
[6]Lugo-Armenta J G, Pino-Fan L R. An approach to inferential reasoning levels on the

<!-- b006491 | references | pages [25] -->
Chi-square statistic[J]. EURASIA Journal of Mathematics, Science and Technology Education,

<!-- b006492 | references | pages [25] -->
2024, 20(1): em2388.

<!-- b006493 | references | pages [25] -->
[7]Liu Z, Wang J, Li X. Evolutionary dynamics of networked N-player trust games with

<!-- b006494 | references | pages [25] -->
exclusion strategy[J]. Chaos, Solitons & Fractals, 2024, 186: 115214.

<!-- b006495 | references | pages [25] -->
[8]Wei S, Wang L, Evans P C, et al. NAFLD and NASH: etiology, targets and emerging

<!-- b006496 | references | pages [25] -->
therapies[J]. Drug Discovery Today, 2024: 103910.

<!-- b006497 | references | pages [25] -->
[9] https://coachfederation.org/

<!-- b006498 | references | pages [25] -->
[10] https://www.bleacherreport.com/

<!-- b006499 | references | pages [25] -->
m

<!-- b006500 | references | pages [25] -->
m

<!-- b006501 | references | pages [25] -->
m

<!-- b006502 | references | pages [25] -->
m

<!-- b006503 | references | pages [25] -->
m

<!-- b006504 | references | pages [25] -->
m

<!-- b006505 | references | pages [25] -->
m

<!-- b006506 | references | pages [25] -->
m

<!-- b006507 | references | pages [25] -->
m

<!-- b006508 | references | pages [25] -->
m

<!-- b006509 | references | pages [25] -->
m

<!-- b006510 | references | pages [25] -->
m

<!-- b006511 | references | pages [25] -->
m

<!-- b006512 | references | pages [25] -->
m

<!-- b006513 | references | pages [25] -->
m

<!-- b006514 | references | pages [25] -->
m

<!-- b006515 | references | pages [25] -->
m

<!-- b006516 | references | pages [25] -->
m

<!-- b006517 | references | pages [25] -->
m

<!-- b006518 | references | pages [25] -->
m

<!-- b006519 | references | pages [25] -->
m

<!-- b006520 | references | pages [25] -->
m

<!-- b006521 | references | pages [25] -->
m

<!-- b006522 | references | pages [25] -->
m

<!-- b006523 | references | pages [25] -->
m

<!-- b006524 | references | pages [25] -->
m

<!-- b006525 | references | pages [25] -->
m

<!-- b006526 | references | pages [25] -->
m

<!-- b006527 | references | pages [25] -->
m

<!-- b006528 | references | pages [25] -->
m

<!-- b006529 | references | pages [25] -->
m

<!-- b006530 | references | pages [25] -->
m

<!-- b006531 | references | pages [25] -->
m

<!-- b006532 | references | pages [25] -->
m

<!-- b006533 | references | pages [25] -->
m

<!-- b006534 | references | pages [25] -->
m

<!-- b006535 | references | pages [25] -->
m

<!-- b006536 | references | pages [25] -->
m

<!-- b006537 | references | pages [25] -->
m

<!-- b006538 | references | pages [25] -->
m

<!-- b006539 | references | pages [25] -->
m

<!-- b006540 | references | pages [25] -->
m

<!-- b006541 | references | pages [25] -->
m

<!-- b006542 | references | pages [25] -->
m

<!-- b006543 | references | pages [25] -->
m

<!-- b006544 | references | pages [25] -->
m

<!-- b006545 | references | pages [25] -->
m

<!-- b006546 | references | pages [25] -->
m

<!-- b006547 | references | pages [25] -->
m

<!-- b006548 | references | pages [25] -->
m

<!-- b006549 | references | pages [25] -->
m

<!-- b006550 | references | pages [25] -->
m

<!-- b006551 | references | pages [25] -->
m

<!-- b006552 | references | pages [25] -->
m

<!-- b006553 | references | pages [25] -->
m

<!-- b006554 | references | pages [25] -->
m

<!-- b006555 | references | pages [25] -->
m

<!-- b006556 | references | pages [25] -->
m

<!-- b006557 | references | pages [25] -->
m

<!-- b006558 | references | pages [25] -->
m

<!-- b006559 | references | pages [25] -->
m

<!-- b006560 | references | pages [25] -->
m

<!-- b006561 | references | pages [25] -->
m

<!-- b006562 | references | pages [25] -->
m

<!-- b006563 | references | pages [25] -->
m

<!-- b006564 | references | pages [25] -->
m

<!-- b006565 | references | pages [25] -->
m

<!-- b006566 | references | pages [25] -->
m

<!-- b006567 | references | pages [25] -->
m

<!-- b006568 | references | pages [25] -->
m

<!-- b006569 | references | pages [25] -->
m

<!-- b006570 | references | pages [25] -->
m

<!-- b006571 | references | pages [25] -->
m

<!-- b006572 | references | pages [25] -->
m

<!-- b006573 | references | pages [25] -->
m

<!-- b006574 | references | pages [25] -->
m

<!-- b006575 | references | pages [25] -->
m

<!-- b006576 | references | pages [25] -->
m

<!-- b006577 | references | pages [25] -->
m

<!-- b006578 | references | pages [25] -->
m

<!-- b006579 | references | pages [25] -->
m

<!-- b006580 | references | pages [25] -->
m

<!-- b006581 | references | pages [25] -->
m

<!-- b006582 | references | pages [25] -->
m

<!-- b006583 | references | pages [25] -->
m

<!-- b006584 | references | pages [25] -->
m

<!-- b006585 | references | pages [25] -->
m

<!-- b006586 | references | pages [25] -->
m

<!-- b006587 | references | pages [25] -->
m

<!-- b006588 | references | pages [25] -->
m

<!-- b006589 | references | pages [25] -->
m

<!-- b006590 | references | pages [25] -->
m

<!-- b006591 | references | pages [25] -->
m

<!-- b006592 | references | pages [25] -->
m

<!-- b006593 | references | pages [25] -->
m

<!-- b006594 | references | pages [25] -->
m

<!-- b006595 | references | pages [25] -->
m

<!-- b006596 | references | pages [25] -->
m

<!-- b006597 | references | pages [25] -->
m

<!-- b006598 | references | pages [25] -->
m

<!-- b006599 | references | pages [25] -->
m

<!-- b006600 | references | pages [25] -->
m

<!-- b006601 | references | pages [25] -->
m

<!-- b006602 | references | pages [25] -->
m

<!-- b006603 | references | pages [25] -->
m

<!-- b006604 | references | pages [25] -->
m

<!-- b006605 | references | pages [25] -->
m

<!-- b006606 | references | pages [25] -->
m

<!-- b006607 | references | pages [25] -->
m

<!-- b006608 | references | pages [25] -->
m

<!-- b006609 | references | pages [25] -->
m

<!-- b006610 | references | pages [25] -->
m

<!-- b006611 | references | pages [25] -->
m

<!-- b006612 | references | pages [25] -->
m

<!-- b006613 | references | pages [25] -->
m

<!-- b006614 | references | pages [25] -->
m

<!-- b006615 | references | pages [25] -->
m

<!-- b006616 | references | pages [25] -->
m

<!-- b006617 | references | pages [25] -->
m

<!-- b006618 | references | pages [25] -->
m

<!-- b006619 | references | pages [25] -->
m

<!-- b006620 | references | pages [25] -->
m

<!-- b006621 | references | pages [25] -->
m

<!-- b006622 | references | pages [25] -->
m

<!-- b006623 | references | pages [25] -->
m

<!-- b006624 | references | pages [25] -->
m

<!-- b006625 | references | pages [25] -->
m

<!-- b006626 | references | pages [25] -->
m

<!-- b006627 | references | pages [25] -->
m

<!-- b006628 | references | pages [25] -->
m

<!-- b006629 | references | pages [25] -->
m

<!-- b006630 | references | pages [25] -->
m

<!-- b006631 | references | pages [25] -->
m

<!-- b006632 | references | pages [25] -->
m

<!-- b006633 | references | pages [25] -->
m

<!-- b006634 | references | pages [25] -->
m

<!-- b006635 | references | pages [25] -->
m

<!-- b006636 | references | pages [25] -->
m

<!-- b006637 | references | pages [25] -->
m

<!-- b006638 | references | pages [25] -->
m

<!-- b006639 | references | pages [25] -->
m

<!-- b006640 | references | pages [25] -->
m

<!-- b006641 | references | pages [25] -->
m

<!-- b006642 | references | pages [25] -->
m

<!-- b006643 | references | pages [25] -->
m

<!-- b006644 | references | pages [25] -->
m

<!-- b006645 | references | pages [25] -->
m

<!-- b006646 | references | pages [25] -->
m

<!-- b006647 | references | pages [25] -->
m

<!-- b006648 | references | pages [25] -->
m

<!-- b006649 | references | pages [25] -->
m

<!-- b006650 | references | pages [25] -->
m

<!-- b006651 | references | pages [25] -->
m

<!-- b006652 | references | pages [25] -->
m

<!-- b006653 | references | pages [25] -->
m

<!-- b006654 | references | pages [25] -->
m

<!-- b006655 | references | pages [25] -->
m

<!-- b006656 | references | pages [25] -->
m

<!-- b006657 | references | pages [25] -->
m

<!-- b006658 | references | pages [25] -->
m

<!-- b006659 | references | pages [25] -->
m

<!-- b006660 | references | pages [25] -->
m

<!-- b006661 | references | pages [25] -->
m

<!-- b006662 | references | pages [25] -->
m

<!-- b006663 | references | pages [25] -->
m

<!-- b006664 | references | pages [25] -->
m

<!-- b006665 | references | pages [25] -->
m

<!-- b006666 | furniture | pages [25] -->


<!-- b006667 | references | pages [25] -->
m

<!-- b006668 | references | pages [25] -->
m

<!-- b006669 | references | pages [25] -->
m

<!-- b006670 | references | pages [25] -->
m

<!-- b006671 | references | pages [25] -->
m

<!-- b006672 | references | pages [25] -->
m

<!-- b006673 | references | pages [25] -->
m

<!-- b006674 | references | pages [25] -->
m

<!-- b006675 | references | pages [25] -->
m

<!-- b006676 | references | pages [25] -->
m

<!-- b006677 | references | pages [25] -->
m

<!-- b006678 | references | pages [25] -->
m

<!-- b006679 | references | pages [25] -->
m

<!-- b006680 | references | pages [25] -->
m

<!-- b006681 | references | pages [25] -->
m

<!-- b006682 | references | pages [25] -->
m

<!-- b006683 | references | pages [25] -->
m

<!-- b006684 | references | pages [25] -->
m

<!-- b006685 | references | pages [25] -->
m

<!-- b006686 | references | pages [25] -->
m

<!-- b006687 | references | pages [25] -->
m

<!-- b006688 | references | pages [25] -->
m

<!-- b006689 | references | pages [25] -->
m

<!-- b006690 | references | pages [25] -->
m

<!-- b006691 | references | pages [25] -->
m

<!-- b006692 | references | pages [25] -->
m

<!-- b006693 | references | pages [25] -->
m

<!-- b006694 | references | pages [25] -->
m

<!-- b006695 | references | pages [25] -->
m

<!-- b006696 | references | pages [25] -->
m

<!-- b006697 | references | pages [25] -->
m

<!-- b006698 | references | pages [25] -->
m

<!-- b006699 | references | pages [25] -->
m

<!-- b006700 | references | pages [25] -->
m

<!-- b006701 | references | pages [25] -->
m

<!-- b006702 | references | pages [25] -->
m

<!-- b006703 | references | pages [25] -->
m

<!-- b006704 | references | pages [25] -->
m

<!-- b006705 | references | pages [25] -->
m

<!-- b006706 | references | pages [25] -->
m

<!-- b006707 | references | pages [25] -->
m

<!-- b006708 | references | pages [25] -->
m

<!-- b006709 | references | pages [25] -->
m

<!-- b006710 | references | pages [25] -->
m

<!-- b006711 | references | pages [25] -->
m

<!-- b006712 | references | pages [25] -->
m

<!-- b006713 | references | pages [25] -->
m

<!-- b006714 | references | pages [25] -->
m

<!-- b006715 | references | pages [25] -->
m

<!-- b006716 | references | pages [25] -->
m

<!-- b006717 | references | pages [25] -->
m

<!-- b006718 | references | pages [25] -->
m

<!-- b006719 | references | pages [25] -->
m

<!-- b006720 | references | pages [25] -->
m

<!-- b006721 | references | pages [25] -->
m

<!-- b006722 | references | pages [25] -->
m

<!-- b006723 | references | pages [25] -->
m

<!-- b006724 | references | pages [25] -->
m

<!-- b006725 | references | pages [25] -->
m

<!-- b006726 | references | pages [25] -->
m

<!-- b006727 | references | pages [25] -->
m

<!-- b006728 | references | pages [25] -->
m

<!-- b006729 | references | pages [25] -->
m

<!-- b006730 | references | pages [25] -->
m

<!-- b006731 | references | pages [25] -->
m

<!-- b006732 | references | pages [25] -->
m

<!-- b006733 | references | pages [25] -->
m

<!-- b006734 | references | pages [25] -->
m

<!-- b006735 | references | pages [25] -->
m

<!-- b006736 | references | pages [25] -->
m

<!-- b006737 | references | pages [25] -->
m

<!-- b006738 | references | pages [25] -->
m

<!-- b006739 | references | pages [25] -->
m

<!-- b006740 | references | pages [25] -->
m

<!-- b006741 | references | pages [25] -->
m

<!-- b006742 | references | pages [25] -->
m

<!-- b006743 | references | pages [25] -->
m

<!-- b006744 | references | pages [25] -->
m

<!-- b006745 | references | pages [25] -->
m

<!-- b006746 | references | pages [25] -->
m

<!-- b006747 | references | pages [25] -->
m

<!-- b006748 | references | pages [25] -->
m

<!-- b006749 | references | pages [25] -->
m

<!-- b006750 | references | pages [25] -->
m

<!-- b006751 | references | pages [25] -->
m

<!-- b006752 | references | pages [25] -->
m

<!-- b006753 | references | pages [25] -->
m

<!-- b006754 | references | pages [25] -->
m

<!-- b006755 | references | pages [25] -->
m

<!-- b006756 | references | pages [25] -->
m

<!-- b006757 | references | pages [25] -->
m

<!-- b006758 | references | pages [25] -->
m

<!-- b006759 | references | pages [25] -->
m

<!-- b006760 | references | pages [25] -->
m

<!-- b006761 | references | pages [25] -->
m

<!-- b006762 | references | pages [25] -->
m

<!-- b006763 | references | pages [25] -->
m

<!-- b006764 | references | pages [25] -->
m

<!-- b006765 | references | pages [25] -->
m

<!-- b006766 | references | pages [25] -->
m

<!-- b006767 | references | pages [25] -->
m

<!-- b006768 | references | pages [25] -->
m

<!-- b006769 | references | pages [25] -->
m

<!-- b006770 | references | pages [25] -->
m

<!-- b006771 | references | pages [25] -->
m

<!-- b006772 | references | pages [25] -->
m

<!-- b006773 | references | pages [25] -->
m

<!-- b006774 | references | pages [25] -->
m

<!-- b006775 | references | pages [25] -->
m

<!-- b006776 | references | pages [25] -->
m

<!-- b006777 | references | pages [25] -->
m

<!-- b006778 | references | pages [25] -->
m

<!-- b006779 | references | pages [25] -->
m

<!-- b006780 | references | pages [25] -->
m

<!-- b006781 | references | pages [25] -->
m

<!-- b006782 | references | pages [25] -->
m

<!-- b006783 | references | pages [25] -->
m

<!-- b006784 | furniture | pages [25] -->
m

<!-- b006785 | furniture | pages [25] -->
m

<!-- b006786 | furniture | pages [25] -->
m

<!-- b006787 | furniture | pages [25] -->
m

<!-- b006788 | furniture | pages [25] -->
m

<!-- b006789 | furniture | pages [25] -->
m

<!-- b006790 | furniture | pages [25] -->
m

<!-- b006791 | furniture | pages [25] -->
m

<!-- b006792 | furniture | pages [25] -->
m

<!-- b006793 | furniture | pages [25] -->
m

<!-- b006794 | furniture | pages [25] -->
m

<!-- b006795 | furniture | pages [25] -->
m

<!-- b006796 | furniture | pages [25] -->
m

<!-- b006797 | furniture | pages [25] -->
m

<!-- b006798 | furniture | pages [25] -->
m

<!-- b006799 | furniture | pages [25] -->
m

<!-- b006800 | furniture | pages [25] -->
m

<!-- b006801 | furniture | pages [25] -->
m

<!-- b006802 | furniture | pages [25] -->
m

<!-- b006803 | furniture | pages [25] -->
m

<!-- b006804 | furniture | pages [25] -->
m

<!-- b006805 | furniture | pages [25] -->
m

<!-- b006806 | furniture | pages [25] -->
m

<!-- b006807 | furniture | pages [25] -->
m

<!-- b006808 | furniture | pages [25] -->
m

<!-- b006809 | furniture | pages [25] -->
m

<!-- b006810 | furniture | pages [25] -->
m

<!-- b006811 | furniture | pages [25] -->
m

<!-- b006812 | furniture | pages [25] -->
m

<!-- b006813 | furniture | pages [25] -->
m

<!-- b006814 | furniture | pages [25] -->
m

<!-- b006815 | furniture | pages [25] -->
m

<!-- b006816 | furniture | pages [25] -->
m

<!-- b006817 | furniture | pages [25] -->
m

<!-- b006818 | furniture | pages [25] -->
m

<!-- b006819 | furniture | pages [25] -->
m

<!-- b006820 | furniture | pages [25] -->
m

<!-- b006821 | furniture | pages [25] -->
m

<!-- b006822 | furniture | pages [25] -->
m

<!-- b006823 | furniture | pages [25] -->
m

<!-- b006824 | furniture | pages [25] -->
m

<!-- b006825 | furniture | pages [25] -->
m

<!-- b006826 | furniture | pages [25] -->
m

<!-- b006827 | furniture | pages [25] -->
m

<!-- b006828 | furniture | pages [25] -->
m

<!-- b006829 | furniture | pages [25] -->
m

<!-- b006830 | furniture | pages [25] -->
m

<!-- b006831 | furniture | pages [25] -->
m

<!-- b006832 | furniture | pages [25] -->
m

<!-- b006833 | furniture | pages [25] -->
m

<!-- b006834 | furniture | pages [25] -->
m

<!-- b006835 | furniture | pages [25] -->
m

<!-- b006836 | furniture | pages [25] -->
m

<!-- b006837 | furniture | pages [25] -->
m

<!-- b006838 | furniture | pages [25] -->
m

<!-- b006839 | furniture | pages [25] -->
m

<!-- b006840 | furniture | pages [25] -->
m

<!-- b006841 | furniture | pages [25] -->
m

<!-- b006842 | furniture | pages [25] -->
m

<!-- b006843 | furniture | pages [25] -->
m

<!-- b006844 | furniture | pages [25] -->
m

<!-- b006845 | furniture | pages [25] -->
m

<!-- b006846 | furniture | pages [25] -->
m

<!-- b006847 | furniture | pages [25] -->
m

<!-- b006848 | furniture | pages [25] -->
m

<!-- b006849 | furniture | pages [25] -->
m

<!-- b006850 | furniture | pages [25] -->
m

<!-- b006851 | furniture | pages [25] -->
m

<!-- b006852 | furniture | pages [25] -->
m

<!-- b006853 | furniture | pages [25] -->
m

<!-- b006854 | furniture | pages [25] -->
m

<!-- b006855 | furniture | pages [25] -->
m

<!-- b006856 | furniture | pages [25] -->
m

<!-- b006857 | furniture | pages [25] -->
m

<!-- b006858 | furniture | pages [25] -->
m

<!-- b006859 | furniture | pages [25] -->
m

<!-- b006860 | furniture | pages [25] -->
m

<!-- b006861 | furniture | pages [25] -->
m

<!-- b006862 | furniture | pages [25] -->
m

<!-- b006863 | furniture | pages [25] -->
m

<!-- b006864 | furniture | pages [25] -->
m

<!-- b006865 | furniture | pages [25] -->
m

<!-- b006866 | furniture | pages [25] -->
m

<!-- b006867 | furniture | pages [25] -->
m

<!-- b006868 | furniture | pages [25] -->
m

<!-- b006869 | furniture | pages [25] -->
m

<!-- b006870 | furniture | pages [25] -->
m

<!-- b006871 | furniture | pages [25] -->
m

<!-- b006872 | furniture | pages [25] -->
m

<!-- b006873 | furniture | pages [25] -->
m

<!-- b006874 | furniture | pages [25] -->
m

<!-- b006875 | furniture | pages [25] -->
m

<!-- b006876 | furniture | pages [25] -->
m

<!-- b006877 | furniture | pages [25] -->
m

<!-- b006878 | furniture | pages [25] -->
m

<!-- b006879 | furniture | pages [25] -->
m

<!-- b006880 | furniture | pages [25] -->
m

<!-- b006881 | furniture | pages [25] -->
m

<!-- b006882 | furniture | pages [25] -->
m

<!-- b006883 | furniture | pages [25] -->
m

<!-- b006884 | furniture | pages [25] -->
m

<!-- b006885 | furniture | pages [25] -->
m

<!-- b006886 | furniture | pages [25] -->
m

<!-- b006887 | furniture | pages [25] -->
m

<!-- b006888 | furniture | pages [25] -->
m

<!-- b006889 | furniture | pages [25] -->
m

<!-- b006890 | furniture | pages [25] -->
m

<!-- b006891 | furniture | pages [25] -->
m

<!-- b006892 | furniture | pages [25] -->
m

<!-- b006893 | furniture | pages [25] -->
m

<!-- b006894 | furniture | pages [25] -->
m

<!-- b006895 | furniture | pages [25] -->
m

<!-- b006896 | furniture | pages [25] -->
m

<!-- b006897 | furniture | pages [25] -->
m

<!-- b006898 | furniture | pages [25] -->
m

<!-- b006899 | furniture | pages [25] -->
m

<!-- b006900 | furniture | pages [25] -->
m

<!-- b006901 | furniture | pages [25] -->
m

<!-- b006902 | furniture | pages [25] -->
m

<!-- b006903 | furniture | pages [25] -->
m

<!-- b006904 | furniture | pages [25] -->
m

<!-- b006905 | furniture | pages [25] -->
m

<!-- b006906 | furniture | pages [25] -->
m

<!-- b006907 | furniture | pages [25] -->
m

<!-- b006908 | furniture | pages [25] -->
m

<!-- b006909 | furniture | pages [25] -->
m

<!-- b006910 | furniture | pages [25] -->
m

<!-- b006911 | furniture | pages [25] -->
m

<!-- b006912 | furniture | pages [25] -->
m

<!-- b006913 | furniture | pages [25] -->
m

<!-- b006914 | furniture | pages [25] -->
m

<!-- b006915 | furniture | pages [25] -->
m

<!-- b006916 | furniture | pages [25] -->
m

<!-- b006917 | furniture | pages [25] -->
m

<!-- b006918 | furniture | pages [25] -->
m

<!-- b006919 | furniture | pages [25] -->
m

<!-- b006920 | furniture | pages [25] -->
m

<!-- b006921 | furniture | pages [25] -->
m

<!-- b006922 | furniture | pages [25] -->
m

<!-- b006923 | furniture | pages [25] -->
m

<!-- b006924 | furniture | pages [25] -->
m

<!-- b006925 | furniture | pages [25] -->
m

<!-- b006926 | furniture | pages [25] -->
m

<!-- b006927 | furniture | pages [25] -->
m

<!-- b006928 | furniture | pages [25] -->
m

<!-- b006929 | furniture | pages [25] -->
m

<!-- b006930 | furniture | pages [25] -->
m

<!-- b006931 | furniture | pages [25] -->
m

<!-- b006932 | furniture | pages [25] -->
m

<!-- b006933 | furniture | pages [25] -->
m

<!-- b006934 | furniture | pages [25] -->
m

<!-- b006935 | furniture | pages [25] -->
m

<!-- b006936 | furniture | pages [25] -->
m

<!-- b006937 | furniture | pages [25] -->
m

<!-- b006938 | furniture | pages [25] -->
m

<!-- b006939 | furniture | pages [25] -->
m

<!-- b006940 | furniture | pages [25] -->
m

<!-- b006941 | furniture | pages [25] -->
m

<!-- b006942 | furniture | pages [25] -->
m

<!-- b006943 | furniture | pages [25] -->
m

<!-- b006944 | furniture | pages [25] -->
m

<!-- b006945 | furniture | pages [25] -->
m

<!-- b006946 | furniture | pages [25] -->
m

<!-- b006947 | furniture | pages [25] -->
m

<!-- b006948 | furniture | pages [25] -->
m

<!-- b006949 | furniture | pages [25] -->
m

<!-- b006950 | furniture | pages [25] -->
m

<!-- b006951 | furniture | pages [25] -->
m

<!-- b006952 | furniture | pages [25] -->
m

<!-- b006953 | furniture | pages [25] -->
m

<!-- b006954 | furniture | pages [25] -->
m

<!-- b006955 | furniture | pages [25] -->
m

<!-- b006956 | furniture | pages [25] -->
m

<!-- b006957 | furniture | pages [25] -->
m

<!-- b006958 | furniture | pages [25] -->
m

<!-- b006959 | furniture | pages [25] -->
m

<!-- b006960 | furniture | pages [25] -->
m

<!-- b006961 | furniture | pages [25] -->
m

<!-- b006962 | furniture | pages [25] -->
m

<!-- b006963 | furniture | pages [25] -->
m

<!-- b006964 | furniture | pages [25] -->
m

<!-- b006965 | furniture | pages [25] -->
m

<!-- b006966 | furniture | pages [25] -->
m

<!-- b006967 | furniture | pages [25] -->
m

<!-- b006968 | furniture | pages [25] -->
m

<!-- b006969 | furniture | pages [25] -->
m

<!-- b006970 | furniture | pages [25] -->
m

<!-- b006971 | furniture | pages [25] -->
m

<!-- b006972 | furniture | pages [25] -->
m

<!-- b006973 | furniture | pages [25] -->
m

<!-- b006974 | furniture | pages [25] -->
m

<!-- b006975 | furniture | pages [25] -->
m

<!-- b006976 | furniture | pages [25] -->
m

<!-- b006977 | furniture | pages [25] -->
m

<!-- b006978 | furniture | pages [25] -->
m

<!-- b006979 | furniture | pages [25] -->
m

<!-- b006980 | furniture | pages [25] -->
m

<!-- b006981 | furniture | pages [25] -->
m

<!-- b006982 | furniture | pages [25] -->
m

<!-- b006983 | furniture | pages [25] -->
m

<!-- b006984 | furniture | pages [25] -->
m

<!-- b006985 | furniture | pages [25] -->
m

<!-- b006986 | furniture | pages [25] -->
m

<!-- b006987 | furniture | pages [25] -->
m

<!-- b006988 | furniture | pages [25] -->
m

<!-- b006989 | furniture | pages [25] -->
m

<!-- b006990 | furniture | pages [25] -->
m

<!-- b006991 | furniture | pages [25] -->
m

<!-- b006992 | furniture | pages [25] -->
m

<!-- b006993 | furniture | pages [25] -->
m

<!-- b006994 | furniture | pages [25] -->
m

<!-- b006995 | furniture | pages [25] -->
m

<!-- b006996 | furniture | pages [25] -->
m

<!-- b006997 | furniture | pages [25] -->
m

<!-- b006998 | furniture | pages [25] -->
m

<!-- b006999 | furniture | pages [25] -->
m

<!-- b007000 | furniture | pages [25] -->
m

<!-- b007001 | furniture | pages [25] -->
m

<!-- b007002 | furniture | pages [25] -->
m

<!-- b007003 | furniture | pages [25] -->
m

<!-- b007004 | furniture | pages [25] -->
m

<!-- b007005 | furniture | pages [25] -->
m

<!-- b007006 | furniture | pages [25] -->
m

<!-- b007007 | furniture | pages [25] -->
m

<!-- b007008 | furniture | pages [25] -->
m

<!-- b007009 | furniture | pages [25] -->
m

<!-- b007010 | furniture | pages [25] -->
m

<!-- b007011 | furniture | pages [25] -->
m

<!-- b007012 | furniture | pages [25] -->
m

<!-- b007013 | furniture | pages [25] -->
m

<!-- b007014 | furniture | pages [25] -->
m

<!-- b007015 | furniture | pages [25] -->
m

<!-- b007016 | furniture | pages [25] -->
m

<!-- b007017 | furniture | pages [25] -->
m

<!-- b007018 | furniture | pages [25] -->
m

<!-- b007019 | furniture | pages [25] -->
m

<!-- b007020 | furniture | pages [25] -->
m

<!-- b007021 | furniture | pages [25] -->
m

<!-- b007022 | furniture | pages [25] -->
m

<!-- b007023 | furniture | pages [25] -->
m

<!-- b007024 | furniture | pages [25] -->
m

<!-- b007025 | furniture | pages [25] -->
m

<!-- b007026 | furniture | pages [25] -->
m

<!-- b007027 | furniture | pages [25] -->
m

<!-- b007028 | furniture | pages [25] -->
m

<!-- b007029 | furniture | pages [25] -->
m

<!-- b007030 | furniture | pages [25] -->
m

<!-- b007031 | furniture | pages [25] -->
m

<!-- b007032 | furniture | pages [25] -->
m

<!-- b007033 | furniture | pages [25] -->
m

<!-- b007034 | furniture | pages [25] -->
m

<!-- b007035 | furniture | pages [25] -->
m

<!-- b007036 | furniture | pages [25] -->
m

<!-- b007037 | furniture | pages [25] -->
m

<!-- b007038 | furniture | pages [25] -->
m

<!-- b007039 | furniture | pages [25] -->
m

<!-- b007040 | furniture | pages [25] -->
m

<!-- b007041 | furniture | pages [25] -->
m

<!-- b007042 | furniture | pages [25] -->
m

<!-- b007043 | furniture | pages [25] -->
m

<!-- b007044 | furniture | pages [25] -->
m

<!-- b007045 | furniture | pages [25] -->
m

<!-- b007046 | furniture | pages [25] -->
m

<!-- b007047 | furniture | pages [25] -->
m

<!-- b007048 | furniture | pages [25] -->
m

<!-- b007049 | furniture | pages [25] -->
m

<!-- b007050 | furniture | pages [25] -->
m

<!-- b007051 | furniture | pages [25] -->
m

<!-- b007052 | furniture | pages [25] -->
m

<!-- b007053 | furniture | pages [25] -->
m

<!-- b007054 | furniture | pages [25] -->
m

<!-- b007055 | furniture | pages [25] -->
m

<!-- b007056 | furniture | pages [25] -->
m

<!-- b007057 | furniture | pages [25] -->
m

<!-- b007058 | furniture | pages [25] -->
m

<!-- b007059 | furniture | pages [25] -->
m

<!-- b007060 | furniture | pages [25] -->
m

<!-- b007061 | furniture | pages [25] -->
m

<!-- b007062 | furniture | pages [25] -->
m

<!-- b007063 | furniture | pages [25] -->
m

<!-- b007064 | furniture | pages [25] -->
m

<!-- b007065 | furniture | pages [25] -->
m

<!-- b007066 | furniture | pages [25] -->
m

<!-- b007067 | furniture | pages [25] -->
m

<!-- b007068 | furniture | pages [25] -->
m

<!-- b007069 | furniture | pages [25] -->
m

<!-- b007070 | furniture | pages [25] -->
m

<!-- b007071 | furniture | pages [25] -->
m

<!-- b007072 | furniture | pages [25] -->
m

<!-- b007073 | furniture | pages [25] -->
m

<!-- b007074 | furniture | pages [25] -->
m

<!-- b007075 | furniture | pages [25] -->
m

<!-- b007076 | furniture | pages [25] -->
m

<!-- b007077 | furniture | pages [25] -->
m

<!-- b007078 | furniture | pages [25] -->
m

<!-- b007079 | furniture | pages [25] -->
m

<!-- b007080 | furniture | pages [25] -->
m

<!-- b007081 | furniture | pages [25] -->
m

<!-- b007082 | furniture | pages [25] -->
m

<!-- b007083 | furniture | pages [25] -->
m

<!-- b007084 | furniture | pages [25] -->
m

<!-- b007085 | furniture | pages [25] -->
m

<!-- b007086 | furniture | pages [25] -->
m

<!-- b007087 | furniture | pages [25] -->
m

<!-- b007088 | furniture | pages [25] -->
m

<!-- b007089 | furniture | pages [25] -->
m

<!-- b007090 | furniture | pages [25] -->
m

<!-- b007091 | furniture | pages [25] -->
m

<!-- b007092 | furniture | pages [25] -->
m

<!-- b007093 | furniture | pages [25] -->
m

<!-- b007094 | furniture | pages [25] -->
m

<!-- b007095 | furniture | pages [25] -->
m

<!-- b007096 | furniture | pages [25] -->
m

<!-- b007097 | furniture | pages [25] -->
m

<!-- b007098 | furniture | pages [25] -->
m

<!-- b007099 | furniture | pages [25] -->
m

<!-- b007100 | furniture | pages [25] -->
m

<!-- b007101 | furniture | pages [25] -->
m

<!-- b007102 | furniture | pages [25] -->
m

<!-- b007103 | furniture | pages [25] -->
m

<!-- b007104 | furniture | pages [25] -->
m

<!-- b007105 | furniture | pages [25] -->
m

<!-- b007106 | furniture | pages [25] -->
m

<!-- b007107 | furniture | pages [25] -->
m

<!-- b007108 | furniture | pages [25] -->
m

<!-- b007109 | furniture | pages [25] -->
m

<!-- b007110 | furniture | pages [25] -->
m

<!-- b007111 | furniture | pages [25] -->
m

<!-- b007112 | furniture | pages [25] -->
m

<!-- b007113 | furniture | pages [25] -->
m

<!-- b007114 | furniture | pages [25] -->
m

<!-- b007115 | furniture | pages [25] -->
m

<!-- b007116 | furniture | pages [25] -->
m

<!-- b007117 | furniture | pages [25] -->
m

<!-- b007118 | furniture | pages [25] -->
m

<!-- b007119 | furniture | pages [25] -->
m

<!-- b007120 | furniture | pages [25] -->
m

<!-- b007121 | furniture | pages [25] -->
m

<!-- b007122 | furniture | pages [25] -->
m

<!-- b007123 | furniture | pages [25] -->
m

<!-- b007124 | furniture | pages [25] -->
m

<!-- b007125 | furniture | pages [25] -->
m

<!-- b007126 | furniture | pages [25] -->
m

<!-- b007127 | furniture | pages [25] -->
m

<!-- b007128 | furniture | pages [25] -->
m

<!-- b007129 | furniture | pages [25] -->
m

<!-- b007130 | furniture | pages [25] -->
m

<!-- b007131 | furniture | pages [25] -->
m

<!-- b007132 | furniture | pages [25] -->
m

<!-- b007133 | furniture | pages [25] -->
m

<!-- b007134 | furniture | pages [25] -->
m

<!-- b007135 | furniture | pages [25] -->
m

<!-- b007136 | furniture | pages [25] -->
m

<!-- b007137 | furniture | pages [25] -->
m

<!-- b007138 | furniture | pages [25] -->
m

<!-- b007139 | furniture | pages [25] -->
m

<!-- b007140 | furniture | pages [25] -->
m

<!-- b007141 | furniture | pages [25] -->
m

<!-- b007142 | furniture | pages [25] -->
m

<!-- b007143 | furniture | pages [25] -->
m

<!-- b007144 | furniture | pages [25] -->
m

<!-- b007145 | furniture | pages [25] -->
m

<!-- b007146 | furniture | pages [25] -->
m

<!-- b007147 | furniture | pages [25] -->
m

<!-- b007148 | furniture | pages [25] -->
m

<!-- b007149 | furniture | pages [25] -->
m

<!-- b007150 | furniture | pages [25] -->
m

<!-- b007151 | furniture | pages [25] -->
m

<!-- b007152 | furniture | pages [25] -->
m

<!-- b007153 | furniture | pages [25] -->
m

<!-- b007154 | furniture | pages [25] -->
m

<!-- b007155 | furniture | pages [25] -->
m

<!-- b007156 | furniture | pages [25] -->
m

<!-- b007157 | furniture | pages [25] -->
m

<!-- b007158 | furniture | pages [25] -->
m

<!-- b007159 | furniture | pages [25] -->
m

<!-- b007160 | furniture | pages [25] -->
m

<!-- b007161 | furniture | pages [25] -->
m

<!-- b007162 | furniture | pages [25] -->
m

<!-- b007163 | furniture | pages [25] -->
m

<!-- b007164 | furniture | pages [25] -->
m

<!-- b007165 | furniture | pages [25] -->
m

<!-- b007166 | furniture | pages [25] -->
m

<!-- b007167 | furniture | pages [25] -->
m

<!-- b007168 | furniture | pages [25] -->
m

<!-- b007169 | furniture | pages [25] -->
m

<!-- b007170 | furniture | pages [25] -->
m

<!-- b007171 | furniture | pages [25] -->
m

<!-- b007172 | furniture | pages [25] -->
m

<!-- b007173 | furniture | pages [25] -->
m

<!-- b007174 | furniture | pages [25] -->
m

<!-- b007175 | furniture | pages [25] -->
m

<!-- b007176 | furniture | pages [25] -->
m

<!-- b007177 | furniture | pages [25] -->
m

<!-- b007178 | furniture | pages [25] -->
m

<!-- b007179 | furniture | pages [25] -->
m

<!-- b007180 | furniture | pages [25] -->
m

<!-- b007181 | furniture | pages [25] -->
m

<!-- b007182 | furniture | pages [25] -->
m

<!-- b007183 | furniture | pages [25] -->
m

<!-- b007184 | furniture | pages [25] -->
m

<!-- b007185 | furniture | pages [25] -->
m

<!-- b007186 | furniture | pages [25] -->
m
