# P-C-2025-2517690-93ab5dac

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
2517690

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Who will dominate the 2028 Olympic Games?

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Predicting Olympic medal counts is a hot topic in the sports world. Based on the data of previous Olympic Games, we constructed a Random Forest regression model for predicting the number of medals in future Olympic Games, offering a new approach to medal prediction.

<!-- b000011 | prose | pages [1] -->
In the first part of Problem 1, we constructed a medal prediction model by considering factors such as the level of athletes, the number and types of events, and the identity of the host country. Through ten-fold cross-validation, we compared Random Forest Regression, Lasso

<!-- b000012 | title | pages [1] -->
微信公众号：数学模型

<!-- b000013 | prose | pages [1] -->
Regression, XGBoost Regression and Neural Network Regression models respectively, and evaluated model performance using metrics such as R2 and MSE. The results show that the Random Forest Regression model performed best with an R²of 0.92 on the test set. Based on the predictions from this model, the three countries with the highest total medal counts at the 2028 Los Angeles Olympics are projected to be the United States, China, and the United Kingdom. Compared to previous Olympic Games, the United States is expected to see a 10% increase in the number of gold medals, while Japan is predicted to experience a 5% decrease in its gold medal count.

<!-- b000014 | prose | pages [1] -->
In the second part of Problem 1, for countries that have never won a medal, we constructed

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
the Logistic Regression Model to predict their probability of winning, and the results show that four countries may win for the first time, with Angola's probability of winning for the first time being 0.81, making it the most likely to win for the first time. Subsequently, we explored the correlation between the events and the total number of medals by the Gray Cor- relation Analysis Model and found that there is a significant correlation between some of the events and the medal performance of specific countries.

<!-- b000017 | prose | pages [1] -->
For Problem 2, in order to explore the impact of the “great coach” effect on medal out- comes, we conducted the Two-sample mean hypothesis testing and the Chi-square test to examine the influence of great coaches on Olympic medal performance. The Logistic Regres- sion Model was also applied to quantify the coach effect. The results show that the impact lies between athlete skill and the number of participants. Based on the results of the model analysis, we suggest that the United States, China and Japan should focus on investing in sports with great coaches.

<!-- b000018 | prose | pages [1] -->
For Problem 3, we explored the impact of host advantage on Olympic medal potential from a game-theoretic perspective. By utilizing the N-player Game Theory and analyzing the Nash Equilibrium, we revealed the interplay of medal distributions across countries and fur- ther elucidated the key role of host advantage in Olympic medal prediction.

<!-- b000019 | prose | pages [1] -->
Finally, we performed error evaluation and sensitivity analysis of the Cross-validation folds, verified the higher prediction accuracy and model robustness.

<!-- b000020 | keywords | pages [1] -->
Keywords: Olympics ; medal prediction ; Machine Learning ;“great coach” effect

<!-- b000021 | furniture | pages [2] -->
Page 2 of 25

<!-- b000022 | furniture | pages [2] -->
Team 2517690

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
1 Introduction.

<!-- b000025 | contents | pages [2] -->
1.1 Problem Background

<!-- b000026 | contents | pages [2] -->
.3

<!-- b000027 | contents | pages [2] -->
1.2 Restatement of the Problem.

<!-- b000028 | contents | pages [2] -->
.3

<!-- b000029 | contents | pages [2] -->
1.3 Literature Review..

<!-- b000030 | contents | pages [2] -->
4

<!-- b000031 | contents | pages [2] -->
1.4 Our Work..

<!-- b000032 | contents | pages [2] -->
4

<!-- b000033 | contents | pages [2] -->
2 Assumptions and Justifications.

<!-- b000034 | contents | pages [2] -->
5

<!-- b000035 | contents | pages [2] -->
3Notations

<!-- b000036 | contents | pages [2] -->
5

<!-- b000037 | contents | pages [2] -->
4 Data Pre-processing and Visual Analytics

<!-- b000038 | contents | pages [2] -->
6

<!-- b000039 | contents | pages [2] -->
5 Olympic Medal Prediction Based on Machine Learning.

<!-- b000040 | contents | pages [2] -->
8

<!-- b000041 | contents | pages [2] -->
5.1 Medal Table Prediction Model Based on Random Forest ....

<!-- b000042 | contents | pages [2] -->
.8

<!-- b000043 | contents | pages [2] -->
5.2 Prediction of First Medal Wins for Medal-less Countries ...

<!-- b000044 | contents | pages [2] -->
.12

<!-- b000045 | contents | pages [2] -->
14

<!-- b000046 | contents | pages [2] -->
5.3 Analysis of Factors Influencing Country Medal Counts..

<!-- b000047 | contents | pages [2] -->
6 The Study of a "Great Coach" Effect.

<!-- b000048 | contents | pages [2] -->
.17

<!-- b000049 | contents | pages [2] -->
mO

<!-- b000050 | contents | pages [2] -->
.17

<!-- b000051 | contents | pages [2] -->
6.1 Analysis of the “great coach” effect ..

<!-- b000052 | contents | pages [2] -->
6.2 Contribution of “great coach"Based on the Logistic.

<!-- b000053 | contents | pages [2] -->
19

<!-- b000054 | contents | pages [2] -->
.20

<!-- b000055 | contents | pages [2] -->
6.3 Investment in “great coach"

<!-- b000056 | contents | pages [2] -->
7 Predicting Olympic Medals: Insights and Strategies

<!-- b000057 | contents | pages [2] -->
.21

<!-- b000058 | contents | pages [2] -->
7.1 The Number of Participating Athletes and the Potential to Win Medals

<!-- b000059 | contents | pages [2] -->
.21

<!-- b000060 | contents | pages [2] -->
7.2 Medal Distribution of Different Countries in Various Events

<!-- b000061 | contents | pages [2] -->
.21

<!-- b000062 | contents | pages [2] -->
.21

<!-- b000063 | contents | pages [2] -->
7.3 Set Advantageous Events

<!-- b000064 | contents | pages [2] -->
8 Sensitivity Analysis and Error Analysis..

<!-- b000065 | contents | pages [2] -->
.22

<!-- b000066 | contents | pages [2] -->
8.1 Sensitivity Analysis..

<!-- b000067 | contents | pages [2] -->
.22

<!-- b000068 | contents | pages [2] -->
8.2 Error Analysis

<!-- b000069 | contents | pages [2] -->
.23

<!-- b000070 | contents | pages [2] -->
O

<!-- b000071 | contents | pages [2] -->
.24

<!-- b000072 | contents | pages [2] -->
9 Strengths and Weaknesses....

<!-- b000073 | contents | pages [2] -->
●

<!-- b000074 | contents | pages [2] -->
9.1 Strengths

<!-- b000075 | contents | pages [2] -->
.24

<!-- b000076 | contents | pages [2] -->
.24

<!-- b000077 | contents | pages [2] -->
9.2 Weaknesses

<!-- b000078 | contents | pages [2] -->
.25

<!-- b000079 | contents | pages [2] -->
10 Conclusion.

<!-- b000080 | contents | pages [2] -->
References ...

<!-- b000081 | contents | pages [2] -->
.25

<!-- b000082 | contents | pages [2] -->
关注数学模型

<!-- b000083 | furniture | pages [2] -->
获取更多资讯

<!-- b000084 | furniture | pages [3] -->
Team 2517690

<!-- b000085 | furniture | pages [3] -->
Page 3 of 25

<!-- b000086 | heading | pages [3] -->
1 Introduction

<!-- b000087 | heading | pages [3] -->
1.1 Problem Background

<!-- b000088 | prose | pages [3] -->
The Olympic medal table measures countries' sporting prowess and informs their preparations for the Games. In the 2024 Paris Olympics, the United States, China, France, and the United Kingdom ex- celled, with the U.S. leading with 126 medals and China tying for the most golds. Several countries, in- cluding Albania, Cape Verde, Dominica, and St. Lu- 微信公众号：数学模型 cia, won medals for the first time, highlighting global competitiveness. However, over 60 countries still haven't won an Olympic medal, showing disparities

<!-- b000089 | caption | pages [3] -->
Figure 1: Paris 2024 Olympic Games

<!-- b000090 | prose | pages [3] -->
in the global distribution of sports resources.

<!-- b000091 | prose | pages [3] -->
Predicting the number of Olympic medals has always been an important research problem, and traditional methods mostly rely on historical medal data. However, with the advance an- nouncement of athlete lists and program settings, medal prediction based on more data and factors is gradually becoming a trend. By taking into account the strength of athletes, the types of events and other key factors, medal prediction can not only provide decision support for 微信号：MATHmodels national Olympic committees but also help event organizations and related departments to op- timize the allocation of resources.

<!-- b000092 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000093 | prose | pages [3] -->
Based on the given data, we specifically address the following questions:

<!-- b000094 | prose | pages [3] -->
Question1: Build a model using the given data to predict the number of gold medals and total medals for each country. Evaluate the model's uncertainty, accuracy, and performance.

<!-- b000095 | prose | pages [3] -->
⚫ Based on the model, predict the medal standings for the 2028 Los Angeles Summer Olympics. Provide prediction intervals for all results and analyze which countries may show improvement and which countries may decline in performance.

<!-- b000096 | prose | pages [3] -->
⚫ Estimate the number of countries that have not won a medal yet, and predict the like- lihood of these countries winning their first medal in the next Olympic Games.

<!-- b000097 | prose | pages [3] -->
⚫ Explore the relationship between the number and type of Olympic events and medal counts, and analyze how different sports matter to countries and how the host coun- try's event selection affects competition results.

<!-- b000098 | prose | pages [3] -->
Question2: Analyze the impact of the "Great coach" Effect on medal counts, estimate its contribution, and recommend sports for three countries to invest in great coaches, along with the expected impact.

<!-- b000099 | heading | pages [3] -->
Question3: Present the novel insights revealed by the model regarding Olympic medal

<!-- b000100 | prose | pages [3] -->
counts and explain how these insights can serve as valuable reference information for national Olympic committees.

<!-- b000101 | prose | pages [3, 4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1.3 Literature Review

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

<!-- b000426 | furniture | pages [4] -->
Page 4 of 25

<!-- b000427 | furniture | pages [4] -->
Team 2517690

<!-- b000429 | prose | pages [4] -->
The prediction of Olympic medals has always been a hot topic in sports science research. [1]The research of Nagpal P, Gupta K and Verma Y et al predicted the medal table through various regression methods (such as linear regression, polynomial regression, ridge regression, etc.). They found that socio-economic factors (such as GDP and population) have a significant impact on the number of medals. [2]Zicheng Song's research predicted the number of Olympic medals of various countries based on a neural network model, emphasizing the advantages of deep learning in dealing with complex non-linear relationships. [3]J. Moolchandani, V. Chole, and S. Sahu et al used machine learning methods to predict the medal distribution of the 2024 Summer Olympics. They used models such as linear regression, random forest, and support vector machine for prediction. The results showed that the random forest model had the highest accuracy, reaching 99%. Based on their research, this paper will further discuss and predict the medals of the 2028 Olympic Games. 1.4 Our Work

<!-- b000430 | prose | pages [4] -->
Question 1 Task 1 Task 2 Task 3 Number of Sports Host Mother Types of Athlete's Subsequence: Number of Numberof Olympic events & country's sequence: Medal counts sports level athletes Games athletes quantities advantages participated Total medals per sport participated per country

<!-- b000431 | prose | pages [4] -->
Input variable

<!-- b000432 | prose | pages [4] -->
Random Forest Trained logistic regression Cross - validation Grey XGBoost Lasso correlation Neural Network

<!-- b000433 | prose | pages [4] -->
Compare R² etc Probability of winning Random Host - selected the first medal Forest event - medal relationshíp

<!-- b000434 | prose | pages [4] -->
Event - medal Prediction Performance Medal table relationship prediction interval comparison

<!-- b000435 | prose | pages [4] -->
Question 3 Question 2 Coaching Medals won Number of duration of in event event excellent hístory participants coaches Invest in Concentrate emerging resources projects Trained logistic regression Two-sample Chí-square test mean test The host sets up Event medal- Regression advantageous winning coefficient projects probability Significantl y affected Optimal Coach investment contribution event

<!-- b000436 | caption | pages [4] -->
Figure 2: Our Work Diagram

<!-- b000437 | prose | pages [4] -->
关注数学模型

<!-- b000438 | furniture | pages [4] -->
获取更多资讯

<!-- b000439 | furniture | pages [5] -->
Team 2517690

<!-- b000440 | furniture | pages [5] -->
Page 5 of 25

<!-- b000441 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000442 | prose | pages [5] -->
微信公众号：数学模型 To simplify the problem, we make the following basic assumptions, each of which is properly justified. Additional, more specific assumptions will be introduced as needed to refine our models. ⚫ Assumption 1: There will be no changes to the list of sports announced for the 2028 Los Angeles Olympics.

<!-- b000443 | prose | pages [5] -->
Justification: This assumption means that we assume that all new or existing Olympic sports will not undergo any changes before the 2028 Los Angeles Olympics, i.e. no new sports will be added and no existing sports will be deleted or canceled. This assumption helps us to simplify the model and to focus on existing data and known changes to the Olympic sports. 微信号：MATHmodels ⚫ Assumption 2: New projects will have less impact on non-winning countries Justification: We assume that for countries that have not yet won an Olympic medal, the addition of new sport will not immediately change their chances of winning a medal. These countries may be able to compete for medals in some of the new sports, but given their overall strength and athlete pool, the impact of the new sports is expected to be small, especially in the short term. ⚫ Assumption 3: Assuming that the level of sports in each country remains stable.

<!-- b000444 | prose | pages [5] -->
Justification: This assumption means that we assume that there will be no significant changes in the level of athletes ( including skill, fitness, athleticism, etc. ) in the different Olympic sports in each country. ⚫ Assumption 4: U.S will be competitive with home-field advantage in additional events at the 2028 Los Angeles Olympics.

<!-- b000445 | prose | pages [5] -->
Justification: With this assumption, we believe that the United States may be in a more favorable position than other countries to compete for medals in the five additional Olym- pic sports, especially since it has a clear competitive advantage in terms of technological accumulation and resource investment.

<!-- b000446 | heading | pages [5] -->
3 Notations

<!-- b000447 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000448 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000449 | heading | pages [5] -->
Symbol

<!-- b000450 | prose | pages [5] -->
Description Number of gold medals won in the j-th event of the i-th sport Number of silver medals won in the j-th event of the i-th sport Number of bronze medals won in the j-th event of the i-th sport Non-medal participants in the j-th event of the ith sport Number of athletes who did not win a medal Number of participation in the programme Number of sessions of participation Number of hours of great coaching in the sport Historical medal count Number of participating athletes

<!-- b000451 | furniture | pages [6] -->
Team 2517690

<!-- b000452 | furniture | pages [6] -->
Page 6 of 25

<!-- b000453 | heading | pages [6] -->
4 Data Pre-processing and Visual Analytics

<!-- b000454 | heading | pages [6] -->
4.1 Data Pre-processing

<!-- b000455 | prose | pages [6] -->
Analyzing the given data reveals redundancy and scatter, so we first perform outlier re- moval, data complementation, integration, and collection to prepare for model construction later in the paper.

<!-- b000456 | prose | pages [6] -->
◆ Outlier Handling The 1906 data in the summerOly_athletes attachment pertains to the unofficial Olympic Games and should be removed as outliers. Additionally, data from several Olympic Games affected by international situations and other factors will be deleted to prevent negative impact on the model.

<!-- b000457 | prose | pages [6] -->
◆ Data Completion The summerOly_programs annex contains some missing data. After review, the missing values are filled in to ensure completeness and avoid affecting subsequent analysis.

<!-- b000458 | prose | pages [6] -->
◆ Data Consolidation （1）Text Data Processing Gold medals are coded as 1, silver as 2, bronze as 3, and no medals as 0. The host country for each year is labeled as 1, while all others are labeled as 0.

<!-- b000459 | prose | pages [6] -->
（2）Data Aggregation Data aggregation is performed based on country, event, and year, with the following ag- gregation rules:

<!-- b000460 | prose | pages [6] -->
①Each event is categorized by sport, and the number of gold, silver, and bronze medals, as well as the number of participants, are calculated.

<!-- b000461 | prose | pages [6] -->
②If an event is missing in a certain year, all countries will have a value of 0 for that event.

<!-- b000462 | prose | pages [6] -->
（3）Data Encoding Countries are sorted in ascending order by name, and each country is assigned a numerical code starting from 1 to replace the country name.

<!-- b000463 | prose | pages [6] -->
（4）Standardization of region names In the annex 'summerOly_medal_counts', add a column with the Olympic Games country abbreviation in the NOC column to facilitate subsequent modeling.

<!-- b000464 | heading | pages [6] -->
◆ Data Collection

<!-- b000465 | prose | pages [6] -->
Given that the total number of medals depends entirely on the events included in the Sum- mer Olympics and that countries specialize in different sports, it is crucial to know the events scheduled for the 2028 Games. Relevant event details have been compiled and recorded in the annex 'summerOly_programs' for unified processing. Below are the data sources：

<!-- b000466 | caption | pages [6] -->
Table 2:Data source website

<!-- b000467 | prose | pages [6] -->
Database Names Database Websites Data 2028 Olympic sports https://la28.org/ Countries participating in the 2028 Olympic Games https://www.olympics.com/en/ International Coach Council https://coachfederation.org/ Entertainment Sports Programming Network https://www.espn.com/

<!-- b000468 | prose | pages [6] -->
关注数学模型

<!-- b000469 | furniture | pages [6] -->
2

<!-- b000470 | furniture | pages [6] -->
MATHmodels

<!-- b000471 | furniture | pages [6] -->
获取更多资讯

<!-- b000472 | furniture | pages [7] -->
Team 2517690

<!-- b000473 | furniture | pages [7] -->
Page 7 of 25

<!-- b000474 | heading | pages [7] -->
4.2 Visual Analytics

<!-- b000475 | prose | pages [7] -->
This section presents a visual analysis of Olympic medal counts through statistical charts, offering insights into the distribution of medals across countries and highlighting their compet- itive strengths over time and in different sports.

<!-- b000476 | prose | pages [7] -->
◆ Number of medals by country Analyze the data and draw the following statistical graphs：

<!-- b000477 | prose | pages [7] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000478 | caption | pages [7] -->
Figure 3: Number of medals by country

<!-- b000479 | prose | pages [7] -->
Analysis of the graph reveals that the United States leads in both gold medals (1,027) and total medals (2,583), demonstrating its strong competitiveness. The USSR and China rank sec- ond and third with 352 and 303 gold medals, respectively, though China surpasses the USSR in total medals (727 vs. 907). Countries like Great Britain, France, and Germany show more balanced performances, with Great Britain achieving 292 gold medals and 944 total medals. In conclusion, the United States remains dominant in Olympic performance, while other nations show varying strengths in gold and total medal counts.

<!-- b000480 | prose | pages [7] -->
◆ Time series chart of the number of medals in each event Under normal circumstances, the number of medals won by each country should follow a stable trend, either gradually increasing or decreasing, with no abrupt fluctuations. This is due to each country's unique geographical position and specialization in specific events, with per- formance trends accumulating over time. Taking the United States as an example, the medal count for each edition of the Games and the four disciplines where it performed most promi- nently were selected and analyzed, as shown in the chart below:

<!-- b000481 | prose | pages [7, 8] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m cantly over the years. Notably, the U.S. reached peak medal counts in 1904 and 1984, likely due to its role as host. During both World Wars, U.S. medal counts declined, possibly reflecting the disruption caused by the wars. Since the 21st century, while fluctuations have occurred, the U.S. has maintained a generally high medal count.

<!-- b000482 | furniture | pages [7] -->
m

<!-- b000483 | furniture | pages [7] -->
m

<!-- b000484 | furniture | pages [7] -->
m

<!-- b000485 | furniture | pages [7] -->
m

<!-- b000486 | furniture | pages [7] -->
m

<!-- b000487 | furniture | pages [7] -->
m

<!-- b000488 | furniture | pages [7] -->
m

<!-- b000489 | furniture | pages [7] -->
m

<!-- b000490 | furniture | pages [7] -->
m

<!-- b000491 | furniture | pages [7] -->
m

<!-- b000492 | furniture | pages [7] -->
m

<!-- b000493 | furniture | pages [7] -->
m

<!-- b000494 | furniture | pages [7] -->
m

<!-- b000495 | furniture | pages [7] -->
m

<!-- b000496 | furniture | pages [7] -->
m

<!-- b000497 | furniture | pages [7] -->
m

<!-- b000498 | furniture | pages [7] -->
m

<!-- b000499 | furniture | pages [7] -->
m

<!-- b000500 | furniture | pages [7] -->
m

<!-- b000501 | furniture | pages [7] -->
m

<!-- b000502 | furniture | pages [7] -->
m

<!-- b000503 | furniture | pages [7] -->
m

<!-- b000504 | furniture | pages [7] -->
m

<!-- b000505 | furniture | pages [7] -->
m

<!-- b000506 | furniture | pages [7] -->
m

<!-- b000507 | furniture | pages [7] -->
m

<!-- b000508 | furniture | pages [7] -->
m

<!-- b000509 | furniture | pages [7] -->
m

<!-- b000510 | furniture | pages [7] -->
m

<!-- b000511 | furniture | pages [7] -->
m

<!-- b000512 | furniture | pages [7] -->
m

<!-- b000513 | furniture | pages [7] -->
m

<!-- b000514 | furniture | pages [7] -->
m

<!-- b000515 | furniture | pages [7] -->
m

<!-- b000516 | furniture | pages [7] -->
m

<!-- b000517 | furniture | pages [7] -->
m

<!-- b000518 | furniture | pages [7] -->
m

<!-- b000519 | furniture | pages [7] -->
m

<!-- b000520 | furniture | pages [7] -->
m

<!-- b000521 | furniture | pages [7] -->
m

<!-- b000522 | furniture | pages [7] -->
m

<!-- b000523 | furniture | pages [7] -->
m

<!-- b000524 | furniture | pages [7] -->
m

<!-- b000525 | furniture | pages [7] -->
m

<!-- b000526 | furniture | pages [7] -->
m

<!-- b000527 | furniture | pages [7] -->
m

<!-- b000528 | furniture | pages [7] -->
m

<!-- b000529 | furniture | pages [7] -->
m

<!-- b000530 | furniture | pages [7] -->
m

<!-- b000531 | furniture | pages [7] -->
m

<!-- b000532 | furniture | pages [7] -->
m

<!-- b000533 | furniture | pages [7] -->
m

<!-- b000534 | furniture | pages [7] -->
m

<!-- b000535 | furniture | pages [7] -->
m

<!-- b000536 | furniture | pages [7] -->
m

<!-- b000537 | furniture | pages [7] -->
m

<!-- b000538 | furniture | pages [7] -->
m

<!-- b000539 | furniture | pages [7] -->
m

<!-- b000540 | furniture | pages [7] -->
m

<!-- b000541 | furniture | pages [7] -->
m

<!-- b000542 | furniture | pages [7] -->
m

<!-- b000543 | furniture | pages [7] -->
m

<!-- b000544 | furniture | pages [7] -->
m

<!-- b000545 | furniture | pages [7] -->
m

<!-- b000546 | furniture | pages [7] -->
m

<!-- b000547 | furniture | pages [7] -->
m

<!-- b000548 | furniture | pages [7] -->
m

<!-- b000549 | furniture | pages [7] -->
m

<!-- b000550 | furniture | pages [7] -->
m

<!-- b000551 | furniture | pages [7] -->
m

<!-- b000552 | furniture | pages [7] -->
m

<!-- b000553 | furniture | pages [7] -->
m

<!-- b000554 | furniture | pages [7] -->
m

<!-- b000555 | furniture | pages [7] -->
m

<!-- b000556 | furniture | pages [7] -->
m

<!-- b000557 | furniture | pages [7] -->
m

<!-- b000558 | furniture | pages [7] -->
m

<!-- b000559 | furniture | pages [7] -->
m

<!-- b000560 | furniture | pages [7] -->
m

<!-- b000561 | furniture | pages [7] -->
m

<!-- b000562 | furniture | pages [7] -->
m

<!-- b000563 | furniture | pages [7] -->
m

<!-- b000564 | furniture | pages [7] -->
m

<!-- b000565 | furniture | pages [7] -->
m

<!-- b000566 | furniture | pages [7] -->
m

<!-- b000567 | furniture | pages [7] -->
m

<!-- b000568 | furniture | pages [7] -->
m

<!-- b000569 | furniture | pages [7] -->
m

<!-- b000570 | furniture | pages [7] -->
m

<!-- b000571 | furniture | pages [7] -->
m

<!-- b000572 | furniture | pages [7] -->
m

<!-- b000573 | furniture | pages [7] -->
m

<!-- b000574 | furniture | pages [7] -->
m

<!-- b000575 | furniture | pages [7] -->
m

<!-- b000576 | furniture | pages [7] -->
m

<!-- b000577 | furniture | pages [7] -->
m

<!-- b000578 | furniture | pages [7] -->
m

<!-- b000579 | furniture | pages [7] -->
m

<!-- b000580 | furniture | pages [7] -->
m

<!-- b000581 | furniture | pages [7] -->
m

<!-- b000582 | furniture | pages [7] -->
m

<!-- b000583 | furniture | pages [7] -->
m

<!-- b000584 | furniture | pages [7] -->
m

<!-- b000585 | furniture | pages [7] -->
m

<!-- b000586 | furniture | pages [7] -->
m

<!-- b000587 | furniture | pages [7] -->
m

<!-- b000588 | furniture | pages [7] -->
m

<!-- b000589 | furniture | pages [7] -->
m

<!-- b000590 | furniture | pages [7] -->
m

<!-- b000591 | furniture | pages [7] -->
m

<!-- b000592 | furniture | pages [7] -->
m

<!-- b000593 | furniture | pages [7] -->
m

<!-- b000594 | furniture | pages [7] -->
m

<!-- b000595 | furniture | pages [7] -->
m

<!-- b000596 | furniture | pages [7] -->
m

<!-- b000597 | furniture | pages [7] -->
m

<!-- b000598 | furniture | pages [7] -->
m

<!-- b000599 | furniture | pages [7] -->
m

<!-- b000600 | furniture | pages [7] -->
m

<!-- b000601 | furniture | pages [7] -->
m

<!-- b000602 | furniture | pages [7] -->
m

<!-- b000603 | furniture | pages [7] -->
m

<!-- b000604 | furniture | pages [7] -->
m

<!-- b000605 | furniture | pages [7] -->
m

<!-- b000606 | furniture | pages [7] -->
m

<!-- b000607 | furniture | pages [7] -->
m

<!-- b000608 | furniture | pages [7] -->
m

<!-- b000609 | furniture | pages [7] -->
m

<!-- b000610 | furniture | pages [7] -->
m

<!-- b000611 | furniture | pages [7] -->
m

<!-- b000612 | furniture | pages [7] -->
m

<!-- b000613 | furniture | pages [7] -->
m

<!-- b000614 | furniture | pages [7] -->
m

<!-- b000615 | furniture | pages [7] -->
m

<!-- b000616 | furniture | pages [7] -->
m

<!-- b000617 | furniture | pages [7] -->
m

<!-- b000618 | furniture | pages [7] -->
m

<!-- b000619 | furniture | pages [7] -->
m

<!-- b000620 | furniture | pages [7] -->
m

<!-- b000621 | furniture | pages [7] -->
m

<!-- b000622 | furniture | pages [7] -->
m

<!-- b000623 | furniture | pages [7] -->
m

<!-- b000624 | furniture | pages [7] -->
m

<!-- b000625 | furniture | pages [7] -->
m

<!-- b000626 | furniture | pages [7] -->
m

<!-- b000627 | furniture | pages [7] -->
m

<!-- b000628 | furniture | pages [7] -->
m

<!-- b000629 | furniture | pages [7] -->
m

<!-- b000630 | furniture | pages [7] -->
m

<!-- b000631 | furniture | pages [7] -->
m

<!-- b000632 | furniture | pages [7] -->
m

<!-- b000633 | furniture | pages [7] -->
m

<!-- b000634 | furniture | pages [7] -->
m

<!-- b000635 | furniture | pages [7] -->
m

<!-- b000636 | furniture | pages [7] -->
m

<!-- b000637 | furniture | pages [7] -->
m

<!-- b000638 | furniture | pages [7] -->
m

<!-- b000639 | furniture | pages [7] -->
m

<!-- b000640 | furniture | pages [7] -->
m

<!-- b000641 | furniture | pages [7] -->
m

<!-- b000642 | furniture | pages [7] -->
m

<!-- b000643 | furniture | pages [7] -->
m

<!-- b000644 | furniture | pages [7] -->
m

<!-- b000645 | furniture | pages [7] -->
m

<!-- b000646 | furniture | pages [7] -->
m

<!-- b000647 | furniture | pages [7] -->
m

<!-- b000648 | furniture | pages [7] -->
m

<!-- b000649 | furniture | pages [7] -->
m

<!-- b000650 | furniture | pages [7] -->
m

<!-- b000651 | furniture | pages [7] -->
m

<!-- b000652 | furniture | pages [7] -->
m

<!-- b000653 | furniture | pages [7] -->
m

<!-- b000654 | furniture | pages [7] -->
m

<!-- b000655 | furniture | pages [7] -->
m

<!-- b000656 | furniture | pages [7] -->
m

<!-- b000657 | furniture | pages [7] -->
m

<!-- b000658 | furniture | pages [7] -->
m

<!-- b000659 | furniture | pages [7] -->
m

<!-- b000660 | furniture | pages [7] -->
m

<!-- b000661 | furniture | pages [7] -->
m

<!-- b000662 | furniture | pages [7] -->
m

<!-- b000663 | furniture | pages [7] -->
m

<!-- b000664 | furniture | pages [7] -->
m

<!-- b000665 | furniture | pages [7] -->
m

<!-- b000666 | furniture | pages [7] -->
m

<!-- b000667 | furniture | pages [7] -->
m

<!-- b000668 | furniture | pages [7] -->
m

<!-- b000669 | furniture | pages [7] -->
m

<!-- b000670 | furniture | pages [7] -->
m

<!-- b000671 | furniture | pages [7] -->
m

<!-- b000672 | furniture | pages [7] -->
m

<!-- b000673 | furniture | pages [7] -->
m

<!-- b000674 | furniture | pages [7] -->
m

<!-- b000675 | furniture | pages [7] -->
m

<!-- b000676 | furniture | pages [7] -->
m

<!-- b000677 | furniture | pages [7] -->
m

<!-- b000678 | furniture | pages [7] -->
m

<!-- b000679 | furniture | pages [7] -->
m

<!-- b000680 | furniture | pages [7] -->
m

<!-- b000681 | furniture | pages [7] -->
m

<!-- b000682 | furniture | pages [7] -->
m

<!-- b000683 | furniture | pages [7] -->
m

<!-- b000684 | furniture | pages [7] -->
m

<!-- b000685 | furniture | pages [7] -->
m

<!-- b000686 | furniture | pages [7] -->
m

<!-- b000687 | furniture | pages [7] -->
m

<!-- b000688 | furniture | pages [7] -->
m

<!-- b000689 | furniture | pages [7] -->
m

<!-- b000690 | furniture | pages [7] -->
m

<!-- b000691 | furniture | pages [7] -->
m

<!-- b000692 | furniture | pages [7] -->
m

<!-- b000693 | furniture | pages [7] -->
m

<!-- b000694 | furniture | pages [7] -->
m

<!-- b000695 | furniture | pages [7] -->
m

<!-- b000696 | furniture | pages [7] -->
m

<!-- b000697 | furniture | pages [7] -->
m

<!-- b000698 | furniture | pages [7] -->
m

<!-- b000699 | furniture | pages [7] -->
m

<!-- b000700 | furniture | pages [7] -->
m

<!-- b000701 | furniture | pages [7] -->
m

<!-- b000702 | furniture | pages [7] -->
m

<!-- b000703 | furniture | pages [7] -->
m

<!-- b000704 | furniture | pages [7] -->
m

<!-- b000705 | furniture | pages [7] -->
m

<!-- b000706 | furniture | pages [7] -->
m

<!-- b000707 | furniture | pages [7] -->
m

<!-- b000708 | furniture | pages [7] -->
m

<!-- b000709 | furniture | pages [7] -->
m

<!-- b000710 | furniture | pages [7] -->
m

<!-- b000711 | furniture | pages [7] -->
m

<!-- b000712 | furniture | pages [7] -->
m

<!-- b000713 | furniture | pages [7] -->
m

<!-- b000714 | furniture | pages [7] -->
m

<!-- b000715 | furniture | pages [7] -->
m

<!-- b000716 | furniture | pages [7] -->
m

<!-- b000717 | furniture | pages [7] -->
m

<!-- b000718 | furniture | pages [7] -->
m

<!-- b000719 | furniture | pages [7] -->
m

<!-- b000720 | furniture | pages [7] -->
m

<!-- b000721 | furniture | pages [7] -->
m

<!-- b000722 | furniture | pages [7] -->
m

<!-- b000723 | furniture | pages [7] -->
m

<!-- b000724 | furniture | pages [7] -->
m

<!-- b000725 | furniture | pages [7] -->
m

<!-- b000726 | furniture | pages [7] -->
m

<!-- b000727 | furniture | pages [7] -->
m

<!-- b000728 | furniture | pages [7] -->
m

<!-- b000729 | furniture | pages [7] -->
m

<!-- b000730 | furniture | pages [7] -->
m

<!-- b000731 | furniture | pages [7] -->
m

<!-- b000732 | furniture | pages [7] -->
m

<!-- b000733 | furniture | pages [7] -->
m

<!-- b000734 | furniture | pages [7] -->
m

<!-- b000735 | furniture | pages [7] -->
m

<!-- b000736 | furniture | pages [7] -->
m

<!-- b000737 | furniture | pages [7] -->
m

<!-- b000738 | furniture | pages [7] -->
m

<!-- b000739 | furniture | pages [7] -->
m

<!-- b000740 | furniture | pages [7] -->
m

<!-- b000741 | furniture | pages [7] -->
m

<!-- b000742 | furniture | pages [7] -->
m

<!-- b000743 | furniture | pages [7] -->
m

<!-- b000744 | furniture | pages [7] -->
m

<!-- b000745 | furniture | pages [7] -->
m

<!-- b000746 | furniture | pages [7] -->
m

<!-- b000747 | furniture | pages [7] -->
m

<!-- b000748 | furniture | pages [7] -->
m

<!-- b000749 | furniture | pages [7] -->
m

<!-- b000750 | furniture | pages [7] -->
m

<!-- b000751 | furniture | pages [7] -->
m

<!-- b000752 | furniture | pages [7] -->
m

<!-- b000753 | furniture | pages [7] -->
m

<!-- b000754 | furniture | pages [7] -->
m

<!-- b000755 | furniture | pages [7] -->
m

<!-- b000756 | furniture | pages [7] -->
m

<!-- b000757 | furniture | pages [7] -->
m

<!-- b000758 | furniture | pages [7] -->
m

<!-- b000759 | furniture | pages [7] -->
m

<!-- b000760 | furniture | pages [7] -->
m

<!-- b000761 | furniture | pages [7] -->
m

<!-- b000762 | furniture | pages [7] -->
m

<!-- b000763 | furniture | pages [7] -->
m

<!-- b000764 | furniture | pages [7] -->
m

<!-- b000765 | furniture | pages [7] -->
m

<!-- b000766 | furniture | pages [7] -->
m

<!-- b000767 | furniture | pages [7] -->
m

<!-- b000768 | furniture | pages [7] -->
m

<!-- b000769 | furniture | pages [7] -->
m

<!-- b000770 | furniture | pages [7] -->
m

<!-- b000771 | furniture | pages [7] -->
m

<!-- b000772 | furniture | pages [7] -->
m

<!-- b000773 | furniture | pages [7] -->
m

<!-- b000774 | furniture | pages [7] -->
m

<!-- b000775 | furniture | pages [7] -->
m

<!-- b000776 | furniture | pages [7] -->
m

<!-- b000777 | furniture | pages [7] -->
m

<!-- b000778 | furniture | pages [7] -->
m

<!-- b000779 | furniture | pages [7] -->
m

<!-- b000780 | furniture | pages [7] -->
m

<!-- b000781 | furniture | pages [7] -->
m

<!-- b000782 | furniture | pages [7] -->
m

<!-- b000783 | furniture | pages [7] -->
m

<!-- b000784 | furniture | pages [7] -->
m

<!-- b000785 | furniture | pages [7] -->
m

<!-- b000786 | furniture | pages [7] -->
m

<!-- b000787 | furniture | pages [7] -->
m

<!-- b000788 | furniture | pages [7] -->
m

<!-- b000789 | furniture | pages [7] -->
m

<!-- b000790 | furniture | pages [7] -->
m

<!-- b000791 | furniture | pages [7] -->
m

<!-- b000792 | furniture | pages [7] -->
m

<!-- b000793 | furniture | pages [7] -->
m

<!-- b000794 | furniture | pages [7] -->
m

<!-- b000795 | furniture | pages [7] -->
m

<!-- b000796 | furniture | pages [7] -->
m

<!-- b000797 | furniture | pages [7] -->
m

<!-- b000798 | furniture | pages [7] -->
m

<!-- b000799 | furniture | pages [7] -->
m

<!-- b000800 | furniture | pages [7] -->
m

<!-- b000801 | furniture | pages [7] -->
m

<!-- b000802 | furniture | pages [7] -->
m

<!-- b000803 | furniture | pages [7] -->
m

<!-- b000804 | furniture | pages [7] -->
m

<!-- b000805 | furniture | pages [7] -->
m

<!-- b000806 | furniture | pages [8] -->
Team 2517690

<!-- b000807 | furniture | pages [8] -->
Page 8 of 25

<!-- b000808 | caption | pages [8] -->
Figure 4: The number of medals in each event       Figure 5:U.S. Medal Count

<!-- b000809 | caption | pages [8] -->
Figure 4 shows that the number of medals won by the United States fluctuated signifi-

<!-- b000811 | caption | pages [8] -->
Figure 5 highlights that swimming has been a traditional strength for the United States,

<!-- b000812 | prose | pages [8] -->
with high medal counts sustained over most years. Basketball, since its Olympic debut in 1936, has been another stable area of success, reflecting the U.S.'s continued dominance, particularly through professional leagues like the NBA, which has kept U.S. basketball at the forefront globally.

<!-- b000813 | heading | pages [8] -->
5 Olympic Medal Prediction Based on Machine Learning

<!-- b000814 | caption | pages [8] -->
Figure 6: Flowchart of part 1 of question 1

<!-- b000815 | heading | pages [8] -->
5.1 Medal Table Prediction Model Based on Random Forest

<!-- b000816 | heading | pages [8] -->
5.1.1 Determination of Input Variables

<!-- b000817 | prose | pages [8] -->
⚫ The level of athletes in various sports: Different countries have significant advantages in certain Olympic events. Usually, this is because the athletes in these countries have undergone long-term training and possess high-level technical and tactical capabili- ties as well as excellent physical fitness.

<!-- b000818 | prose | pages [8] -->
⚫ The number and types of competition events: The number and types of events in each

<!-- b000819 | prose | pages [8, 9] -->
关注数学模型 Olympic Games affect a country's chances of winning medals. Some countries may have traditional advantages in the events that are added or removed from the Olym- pics, which will impact the number of medals they can obtain.

<!-- b000820 | furniture | pages [8] -->
2

<!-- b000821 | furniture | pages [8] -->
MATHmodels

<!-- b000822 | furniture | pages [8] -->
获取更多资讯

<!-- b000823 | furniture | pages [9] -->
Team 2517690

<!-- b000824 | furniture | pages [9] -->
Page 9 of 25

<!-- b000826 | prose | pages [9] -->
⚫ The impact of being the host country on medal performance: The host country usually has certain advantages in terms of psychology, resources, funding, and audience sup- port. This may enhance its performance in some events, and this is a typical 0 - 1 variable.

<!-- b000827 | prose | pages [9] -->
⚫ The number of athletes a country sends to the Olympics: Countries with a larger num- ber of participating athletes can usually compete in multiple events, thus increasing their chances of winning medals. More athletes mean more opportunities to perform 微信公众号：数学模型 and greater potential to increase the number of medals.

<!-- b000828 | heading | pages [9] -->
5.1.2 Comprehensive Strength Evaluation of Each Event

<!-- b000829 | prose | pages [9] -->
By analyzing the medal distribution of each event in the previous Olympic Games and the number of non-winning participants, a quantitative indicator was constructed to measure the comprehensive competitive strength of each country in that event. Based on the total number of historical medals of athletes, it is possible to effectively evaluate a country's performance and competitiveness in the event, providing a reliable reference for medal predictions in future Olympic Games.

<!-- b000830 | prose | pages [9] -->
微信号：MATHmodels Step1: Determine variables Let be the number of gold medals won in the j-th event of the i-th sport, be the number of silver medals won in the j-th event of the i-th sport, be the number of bronze medals won in the j-th event of the i-th sport, and be the non-medal participants in the j-th Event of the i-th Sport Step 2: Subjectively assign weights Each indicator (such as the number of gold medals, silver medals, bronze medals, and the number of non-medalists) contributes differently to the comprehensive strength. Therefore, we assign the following weights:

<!-- b000831 | caption | pages [9] -->
Table 3:Weighting of award indicators

<!-- b000832 | heading | pages [9] -->
Step3: Quantification of the comprehensive strength of each country in each event

<!-- b000833 | prose | pages [9] -->
Let the comprehensive strength of the i-th event of the m-th country be , which can

<!-- b000834 | prose | pages [9] -->
be expressed as:

<!-- b000835 | prose | pages [9] -->
(1)

<!-- b000836 | heading | pages [9] -->
5.1.3 Establishment of the National Medal Quantity Prediction Model

<!-- b000837 | prose | pages [9, 10] -->
Predicting the number of Olympic medals is a complex regression problem that involves multiple factors. To accurately predict the number of medals for each country, choosing an m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m appropriate machine-learning model is of great significance. Especially when dealing with multiple features and complex data relationships, different regression models have different advantages and applicable scenarios.

<!-- b000838 | furniture | pages [9] -->
m

<!-- b000839 | furniture | pages [9] -->
m

<!-- b000840 | furniture | pages [9] -->
m

<!-- b000841 | furniture | pages [9] -->
m

<!-- b000842 | furniture | pages [9] -->
m

<!-- b000843 | furniture | pages [9] -->
m

<!-- b000844 | furniture | pages [9] -->
m

<!-- b000845 | furniture | pages [9] -->
m

<!-- b000846 | furniture | pages [9] -->
m

<!-- b000847 | furniture | pages [9] -->
m

<!-- b000848 | furniture | pages [9] -->
m

<!-- b000849 | furniture | pages [9] -->
m

<!-- b000850 | furniture | pages [9] -->
m

<!-- b000851 | furniture | pages [9] -->
m

<!-- b000852 | furniture | pages [9] -->
m

<!-- b000853 | furniture | pages [9] -->
m

<!-- b000854 | furniture | pages [9] -->
m

<!-- b000855 | furniture | pages [9] -->
m

<!-- b000856 | furniture | pages [9] -->
m

<!-- b000857 | furniture | pages [9] -->
m

<!-- b000858 | furniture | pages [9] -->
m

<!-- b000859 | furniture | pages [9] -->
m

<!-- b000860 | furniture | pages [9] -->
m

<!-- b000861 | furniture | pages [9] -->
m

<!-- b000862 | furniture | pages [9] -->
m

<!-- b000863 | furniture | pages [9] -->
m

<!-- b000864 | furniture | pages [9] -->
m

<!-- b000865 | furniture | pages [9] -->
m

<!-- b000866 | furniture | pages [9] -->
m

<!-- b000867 | furniture | pages [9] -->
m

<!-- b000868 | furniture | pages [9] -->
m

<!-- b000869 | furniture | pages [9] -->
m

<!-- b000870 | furniture | pages [9] -->
m

<!-- b000871 | furniture | pages [9] -->
m

<!-- b000872 | furniture | pages [9] -->
m

<!-- b000873 | furniture | pages [9] -->
m

<!-- b000874 | furniture | pages [9] -->
m

<!-- b000875 | furniture | pages [9] -->
m

<!-- b000876 | furniture | pages [9] -->
m

<!-- b000877 | furniture | pages [9] -->
m

<!-- b000878 | furniture | pages [9] -->
m

<!-- b000879 | furniture | pages [9] -->
m

<!-- b000880 | furniture | pages [9] -->
m

<!-- b000881 | furniture | pages [9] -->
m

<!-- b000882 | furniture | pages [9] -->
m

<!-- b000883 | furniture | pages [9] -->
m

<!-- b000884 | furniture | pages [9] -->
m

<!-- b000885 | furniture | pages [9] -->
m

<!-- b000886 | furniture | pages [9] -->
m

<!-- b000887 | furniture | pages [9] -->
m

<!-- b000888 | furniture | pages [9] -->
m

<!-- b000889 | furniture | pages [9] -->
m

<!-- b000890 | furniture | pages [9] -->
m

<!-- b000891 | furniture | pages [9] -->
m

<!-- b000892 | furniture | pages [9] -->
m

<!-- b000893 | furniture | pages [9] -->
m

<!-- b000894 | furniture | pages [9] -->
m

<!-- b000895 | furniture | pages [9] -->
m

<!-- b000896 | furniture | pages [9] -->
m

<!-- b000897 | furniture | pages [9] -->
m

<!-- b000898 | furniture | pages [9] -->
m

<!-- b000899 | furniture | pages [9] -->
m

<!-- b000900 | furniture | pages [9] -->
m

<!-- b000901 | furniture | pages [9] -->
m

<!-- b000902 | furniture | pages [9] -->
m

<!-- b000903 | furniture | pages [9] -->
m

<!-- b000904 | furniture | pages [9] -->
m

<!-- b000905 | furniture | pages [9] -->
m

<!-- b000906 | furniture | pages [9] -->
m

<!-- b000907 | furniture | pages [9] -->
m

<!-- b000908 | furniture | pages [9] -->
m

<!-- b000909 | furniture | pages [9] -->
m

<!-- b000910 | furniture | pages [9] -->
m

<!-- b000911 | furniture | pages [9] -->
m

<!-- b000912 | furniture | pages [9] -->
m

<!-- b000913 | furniture | pages [9] -->
m

<!-- b000914 | furniture | pages [9] -->
m

<!-- b000915 | furniture | pages [9] -->
m

<!-- b000916 | furniture | pages [9] -->
m

<!-- b000917 | furniture | pages [9] -->
m

<!-- b000918 | furniture | pages [9] -->
m

<!-- b000919 | furniture | pages [9] -->
m

<!-- b000920 | furniture | pages [9] -->
m

<!-- b000921 | furniture | pages [9] -->
m

<!-- b000922 | furniture | pages [9] -->
m

<!-- b000923 | furniture | pages [9] -->
m

<!-- b000924 | furniture | pages [9] -->
m

<!-- b000925 | furniture | pages [9] -->
m

<!-- b000926 | furniture | pages [9] -->
m

<!-- b000927 | furniture | pages [9] -->
m

<!-- b000928 | furniture | pages [9] -->
m

<!-- b000929 | furniture | pages [9] -->
m

<!-- b000930 | furniture | pages [9] -->
m

<!-- b000931 | furniture | pages [9] -->
m

<!-- b000932 | furniture | pages [9] -->
m

<!-- b000933 | furniture | pages [9] -->
m

<!-- b000934 | furniture | pages [9] -->
m

<!-- b000935 | furniture | pages [9] -->
m

<!-- b000936 | furniture | pages [9] -->
m

<!-- b000937 | furniture | pages [9] -->
m

<!-- b000938 | furniture | pages [9] -->
m

<!-- b000939 | furniture | pages [9] -->
m

<!-- b000940 | furniture | pages [9] -->
m

<!-- b000941 | furniture | pages [9] -->
m

<!-- b000942 | furniture | pages [9] -->
m

<!-- b000943 | furniture | pages [9] -->
m

<!-- b000944 | furniture | pages [9] -->
m

<!-- b000945 | furniture | pages [9] -->
m

<!-- b000946 | furniture | pages [9] -->
m

<!-- b000947 | furniture | pages [9] -->
m

<!-- b000948 | furniture | pages [9] -->
m

<!-- b000949 | furniture | pages [9] -->
m

<!-- b000950 | furniture | pages [9] -->
m

<!-- b000951 | furniture | pages [9] -->
m

<!-- b000952 | furniture | pages [9] -->
m

<!-- b000953 | furniture | pages [9] -->
m

<!-- b000954 | furniture | pages [9] -->
m

<!-- b000955 | furniture | pages [9] -->
m

<!-- b000956 | furniture | pages [9] -->
m

<!-- b000957 | furniture | pages [9] -->
m

<!-- b000958 | furniture | pages [9] -->
m

<!-- b000959 | furniture | pages [9] -->
m

<!-- b000960 | furniture | pages [9] -->
m

<!-- b000961 | furniture | pages [9] -->
m

<!-- b000962 | furniture | pages [9] -->
m

<!-- b000963 | furniture | pages [9] -->
m

<!-- b000964 | furniture | pages [9] -->
m

<!-- b000965 | furniture | pages [9] -->
m

<!-- b000966 | furniture | pages [9] -->
m

<!-- b000967 | furniture | pages [9] -->
m

<!-- b000968 | furniture | pages [9] -->
m

<!-- b000969 | furniture | pages [9] -->
m

<!-- b000970 | furniture | pages [9] -->
m

<!-- b000971 | furniture | pages [9] -->
m

<!-- b000972 | furniture | pages [9] -->
m

<!-- b000973 | furniture | pages [9] -->
m

<!-- b000974 | furniture | pages [9] -->
m

<!-- b000975 | furniture | pages [9] -->
m

<!-- b000976 | furniture | pages [9] -->
m

<!-- b000977 | furniture | pages [9] -->
m

<!-- b000978 | furniture | pages [9] -->
m

<!-- b000979 | furniture | pages [9] -->
m

<!-- b000980 | furniture | pages [9] -->
m

<!-- b000981 | furniture | pages [9] -->
m

<!-- b000982 | furniture | pages [9] -->
m

<!-- b000983 | furniture | pages [9] -->
m

<!-- b000984 | furniture | pages [9] -->
m

<!-- b000985 | furniture | pages [9] -->
m

<!-- b000986 | furniture | pages [9] -->
m

<!-- b000987 | furniture | pages [9] -->
m

<!-- b000988 | furniture | pages [9] -->
m

<!-- b000989 | furniture | pages [9] -->
m

<!-- b000990 | furniture | pages [9] -->
m

<!-- b000991 | furniture | pages [9] -->
m

<!-- b000992 | furniture | pages [9] -->
m

<!-- b000993 | furniture | pages [9] -->
m

<!-- b000994 | furniture | pages [9] -->
m

<!-- b000995 | furniture | pages [9] -->
m

<!-- b000996 | furniture | pages [9] -->
m

<!-- b000997 | furniture | pages [9] -->
m

<!-- b000998 | furniture | pages [9] -->
m

<!-- b000999 | furniture | pages [9] -->
m

<!-- b001000 | furniture | pages [9] -->
m

<!-- b001001 | furniture | pages [9] -->
m

<!-- b001002 | furniture | pages [9] -->
m

<!-- b001003 | furniture | pages [9] -->
m

<!-- b001004 | furniture | pages [9] -->
m

<!-- b001005 | furniture | pages [9] -->
m

<!-- b001006 | furniture | pages [9] -->
m

<!-- b001007 | furniture | pages [9] -->
m

<!-- b001008 | furniture | pages [9] -->
m

<!-- b001009 | furniture | pages [9] -->
m

<!-- b001010 | furniture | pages [9] -->
m

<!-- b001011 | furniture | pages [9] -->
m

<!-- b001012 | furniture | pages [9] -->
m

<!-- b001013 | furniture | pages [9] -->
m

<!-- b001014 | furniture | pages [9] -->
m

<!-- b001015 | furniture | pages [9] -->
m

<!-- b001016 | furniture | pages [9] -->
m

<!-- b001017 | furniture | pages [9] -->
m

<!-- b001018 | furniture | pages [9] -->
m

<!-- b001019 | furniture | pages [9] -->
m

<!-- b001020 | furniture | pages [9] -->
m

<!-- b001021 | furniture | pages [9] -->
m

<!-- b001022 | furniture | pages [9] -->
m

<!-- b001023 | furniture | pages [9] -->
m

<!-- b001024 | furniture | pages [9] -->
m

<!-- b001025 | furniture | pages [9] -->
m

<!-- b001026 | furniture | pages [9] -->
m

<!-- b001027 | furniture | pages [9] -->
m

<!-- b001028 | furniture | pages [9] -->
m

<!-- b001029 | furniture | pages [9] -->
m

<!-- b001030 | furniture | pages [9] -->
m

<!-- b001031 | furniture | pages [9] -->
m

<!-- b001032 | furniture | pages [9] -->
m

<!-- b001033 | furniture | pages [9] -->
m

<!-- b001034 | furniture | pages [9] -->
m

<!-- b001035 | furniture | pages [9] -->
m

<!-- b001036 | furniture | pages [9] -->
m

<!-- b001037 | furniture | pages [9] -->
m

<!-- b001038 | furniture | pages [9] -->
m

<!-- b001039 | furniture | pages [9] -->
m

<!-- b001040 | furniture | pages [9] -->
m

<!-- b001041 | furniture | pages [9] -->
m

<!-- b001042 | furniture | pages [9] -->
m

<!-- b001043 | furniture | pages [9] -->
m

<!-- b001044 | furniture | pages [9] -->
m

<!-- b001045 | furniture | pages [9] -->
m

<!-- b001046 | furniture | pages [9] -->
m

<!-- b001047 | furniture | pages [9] -->
m

<!-- b001048 | furniture | pages [9] -->
m

<!-- b001049 | furniture | pages [9] -->
m

<!-- b001050 | furniture | pages [9] -->
m

<!-- b001051 | furniture | pages [9] -->
m

<!-- b001052 | furniture | pages [9] -->
m

<!-- b001053 | furniture | pages [9] -->
m

<!-- b001054 | furniture | pages [9] -->
m

<!-- b001055 | furniture | pages [9] -->
m

<!-- b001056 | furniture | pages [9] -->
m

<!-- b001057 | furniture | pages [9] -->
m

<!-- b001058 | furniture | pages [9] -->
m

<!-- b001059 | furniture | pages [9] -->
m

<!-- b001060 | furniture | pages [9] -->
m

<!-- b001061 | furniture | pages [9] -->
m

<!-- b001062 | furniture | pages [9] -->
m

<!-- b001063 | furniture | pages [9] -->
m

<!-- b001064 | furniture | pages [9] -->
m

<!-- b001065 | furniture | pages [9] -->
m

<!-- b001066 | furniture | pages [9] -->
m

<!-- b001067 | furniture | pages [9] -->
m

<!-- b001068 | furniture | pages [9] -->
m

<!-- b001069 | furniture | pages [9] -->
m

<!-- b001070 | furniture | pages [9] -->
m

<!-- b001071 | furniture | pages [9] -->
m

<!-- b001072 | furniture | pages [9] -->
m

<!-- b001073 | furniture | pages [9] -->
m

<!-- b001074 | furniture | pages [9] -->
m

<!-- b001075 | furniture | pages [9] -->
m

<!-- b001076 | furniture | pages [9] -->
m

<!-- b001077 | furniture | pages [9] -->
m

<!-- b001078 | furniture | pages [9] -->
m

<!-- b001079 | furniture | pages [9] -->
m

<!-- b001080 | furniture | pages [9] -->
m

<!-- b001081 | furniture | pages [9] -->
m

<!-- b001082 | furniture | pages [9] -->
m

<!-- b001083 | furniture | pages [9] -->
m

<!-- b001084 | furniture | pages [9] -->
m

<!-- b001085 | furniture | pages [9] -->
m

<!-- b001086 | furniture | pages [9] -->
m

<!-- b001087 | furniture | pages [9] -->
m

<!-- b001088 | furniture | pages [9] -->
m

<!-- b001089 | furniture | pages [9] -->
m

<!-- b001090 | furniture | pages [9] -->
m

<!-- b001091 | furniture | pages [9] -->
m

<!-- b001092 | furniture | pages [9] -->
m

<!-- b001093 | furniture | pages [9] -->
m

<!-- b001094 | furniture | pages [9] -->
m

<!-- b001095 | furniture | pages [9] -->
m

<!-- b001096 | furniture | pages [9] -->
m

<!-- b001097 | furniture | pages [9] -->
m

<!-- b001098 | furniture | pages [9] -->
m

<!-- b001099 | furniture | pages [9] -->
m

<!-- b001100 | furniture | pages [9] -->
m

<!-- b001101 | furniture | pages [9] -->
m

<!-- b001102 | furniture | pages [9] -->
m

<!-- b001103 | furniture | pages [9] -->
m

<!-- b001104 | furniture | pages [9] -->
m

<!-- b001105 | furniture | pages [9] -->
m

<!-- b001106 | furniture | pages [9] -->
m

<!-- b001107 | furniture | pages [9] -->
m

<!-- b001108 | furniture | pages [9] -->
m

<!-- b001109 | furniture | pages [9] -->
m

<!-- b001110 | furniture | pages [9] -->
m

<!-- b001111 | furniture | pages [9] -->
m

<!-- b001112 | furniture | pages [9] -->
m

<!-- b001113 | furniture | pages [9] -->
m

<!-- b001114 | furniture | pages [9] -->
m

<!-- b001115 | furniture | pages [9] -->
m

<!-- b001116 | furniture | pages [9] -->
m

<!-- b001117 | furniture | pages [9] -->
m

<!-- b001118 | furniture | pages [9] -->
m

<!-- b001119 | furniture | pages [9] -->
m

<!-- b001120 | furniture | pages [9] -->
m

<!-- b001121 | furniture | pages [9] -->
m

<!-- b001122 | furniture | pages [9] -->
m

<!-- b001123 | furniture | pages [9] -->
m

<!-- b001124 | furniture | pages [9] -->
m

<!-- b001125 | furniture | pages [9] -->
m

<!-- b001126 | furniture | pages [9] -->
m

<!-- b001127 | furniture | pages [9] -->
m

<!-- b001128 | furniture | pages [9] -->
m

<!-- b001129 | furniture | pages [9] -->
m

<!-- b001130 | furniture | pages [9] -->
m

<!-- b001131 | furniture | pages [9] -->
m

<!-- b001132 | furniture | pages [9] -->
m

<!-- b001133 | furniture | pages [9] -->
m

<!-- b001134 | furniture | pages [9] -->
m

<!-- b001135 | furniture | pages [9] -->
m

<!-- b001136 | furniture | pages [9] -->
m

<!-- b001137 | furniture | pages [9] -->
m

<!-- b001138 | furniture | pages [9] -->
m

<!-- b001139 | furniture | pages [9] -->
m

<!-- b001140 | furniture | pages [9] -->
m

<!-- b001141 | furniture | pages [9] -->
m

<!-- b001142 | furniture | pages [9] -->
m

<!-- b001143 | furniture | pages [9] -->
m

<!-- b001144 | furniture | pages [9] -->
m

<!-- b001145 | furniture | pages [9] -->
m

<!-- b001146 | furniture | pages [9] -->
m

<!-- b001147 | furniture | pages [9] -->
m

<!-- b001148 | furniture | pages [9] -->
m

<!-- b001149 | furniture | pages [9] -->
m

<!-- b001150 | furniture | pages [9] -->
m

<!-- b001151 | furniture | pages [9] -->
m

<!-- b001152 | furniture | pages [9] -->
m

<!-- b001153 | furniture | pages [9] -->
m

<!-- b001154 | furniture | pages [9] -->
m

<!-- b001155 | furniture | pages [9] -->
m

<!-- b001156 | furniture | pages [9] -->
m

<!-- b001157 | furniture | pages [9] -->
m

<!-- b001158 | furniture | pages [9] -->
m

<!-- b001159 | furniture | pages [9] -->
m

<!-- b001160 | furniture | pages [9] -->
m

<!-- b001161 | furniture | pages [9] -->
m

<!-- b001162 | furniture | pages [10] -->
Team 2517690

<!-- b001163 | furniture | pages [10] -->
Page 10 of 25

<!-- b001165 | prose | pages [10] -->
For this reason, this paper will compare four machine learning models widely used in regression problems: Random Forest regression, Lasso regression, XGBoost regression, and Neural Network regression. By comparing the prediction effects of these models, the aim is to find the model most suitable for the task of predicting the number of Olympic medals. To improve the accuracy of the regression models, this paper uses ten-fold cross-validation. The hold-out method is adopted, with 90% of the samples used as the training set and 10% of the samples used as the test set. The evaluation metrics of the four regression models are calculated, as shown in the following table：

<!-- b001166 | caption | pages [10] -->
Table 4:Results of regression model evaluation

<!-- b001167 | prose | pages [10] -->
During the comparison of multiple regression models, after comprehensive evaluation and verification, the Random Forest regression model outperforms other models in evaluation metrics such as , MSE and MAE. Therefore, based on its high prediction accuracy and strong generalization ability, this study finally selects the Random Forest regression model as the main tool for predicting the number of medals in the 2028 Olympic Games.

<!-- b001168 | heading | pages [10] -->
5.1.4 Medal Table Prediction Results Based on Random Forest

<!-- b001169 | prose | pages [10] -->
In order to accurately predict the number of medals of each country in the 2028 Olympic Games, we adopt the Random Forest regres- sion model. This model achieves efficient pre- diction by integrating multiple decision trees m m m m m m m m m m m m m m m m m m m m m m and is particularly suitable for dealing with data m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m with complex non-linear relationships and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m multi-dimensional features. The advantages of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the random forest regression model lie in its m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m strong feature selection ability, low risk of over- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m fitting, and excellent generalization ability. Through multiple trainings and evaluations, it has been confirmed that this model performs outstandingly when dealing with the task of Olympic medal prediction.

<!-- b001170 | caption | pages [10] -->
Figure 7: Random Forest mechanism diagram

<!-- b001171 | prose | pages [10] -->
Based on the collected data of the 2028 Olympic Games, the trained Random Forest regression model is used for prediction. The model predicts the number of medals each coun- try will win in the Olympics based on features such as the level and quantity of athletes from

<!-- b001172 | prose | pages [10, 11] -->
关注数学模型 each country, as well as the number of competition events. Due to space limitations, this paper only presents the prediction results of some countries. The specific prediction results are as follows (all values are integers):

<!-- b001173 | furniture | pages [10] -->
2

<!-- b001174 | furniture | pages [10] -->
MATHmodels

<!-- b001175 | furniture | pages [10] -->
获取更多资讯

<!-- b001176 | furniture | pages [11] -->
Team 2517690

<!-- b001177 | furniture | pages [11] -->
Page 11 of 25

<!-- b001179 | caption | pages [11] -->
Table 5:2028 Medal Table Prediction

<!-- b001180 | prose | pages [11] -->
Gold Silver Total Bronze

<!-- b001181 | prose | pages [11] -->
44 132 46 United States 42

<!-- b001182 | prose | pages [11] -->
96 China 40 30 26

<!-- b001183 | prose | pages [11] -->
69 25 30 14 Great Britain

<!-- b001184 | prose | pages [11] -->
20 16 56 Australia 20

<!-- b001185 | prose | pages [11] -->
Japan 11 46 19 16

<!-- b001186 | prose | pages [11] -->
From the analysis, it can be seen that in the prediction for the 2028 Olympic Games, the number of gold medals won by the United States will increase by 10%, and it will still rank first in the total number of medals. The number of gold medals won by China remains un- changed, but the total number of medals will increase by 5%. The number of gold medals won by Japan will decrease by 5%.

<!-- b001187 | heading | pages [11] -->
5.1.5 Confidence Interval

<!-- b001188 | prose | pages [11] -->
● ● To further evaluate the reliability and uncertainty of the model's predictions, this study also calculated the upper and lower limit intervals for the predicted medal counts of each country. By introducing the prediction interval, the upper and lower limits of each predicted value can be given, thereby indicating the possible range of the true medal count under a certain confidence level. The following figure shows the prediction results of some countries and their corresponding upper and lower limitintervals of the predictions. All values are integers.

<!-- b001189 | prose | pages [11] -->
Total Gold lower confidence bound lower confidence bound 138.9 Higher confidence bound 46.9 50 40 Higher-confidence-bound 42.6 30 45 20 40 104.2 125.1 10 35 42.1 38.4 D 00 30 22.1 25 20.4 90 99.8 72.9 15.8 20 80 15 70 59.6 17.6 17.9 12.2 10 60 48.8 65.1 5 50 52.4 40 0 China Great Britain Australia Japan United States United States China Great Britain Australia Japan

<!-- b001190 | caption | pages [11] -->
Figure 8:Line graph of confidence limits on the number of medals predicted

<!-- b001191 | prose | pages [11] -->
As shown above, introducing the prediction interval can present the possible range of each country's true medal count at a certain confidence level. This not only enhances the transpar- ency of prediction results but also offers more reliable information for decision-makers to eval- uate potential uncertainties and risks.

<!-- b001192 | furniture | pages [12] -->
Team 2517690

<!-- b001193 | furniture | pages [12] -->
Page 12 of 25

<!-- b001194 | heading | pages [12] -->
5.2  Prediction of First Medal Wins for Medal-less Countries

<!-- b001195 | heading | pages [12] -->
5.2.1 Model Preparation

<!-- b001196 | prose | pages [12] -->
(1) Determination of independent and dependent variables ⚫ Independent variables：

<!-- b001197 | prose | pages [12] -->
X The number of medal - less athletes （ ） 1 X The number of events participated in （ ） 2 The number of Olympic Games participated X （ ） in 3

<!-- b001198 | prose | pages [12] -->
⚫ Dependent variable:

<!-- b001199 | prose | pages [12] -->
Figure 9：Flowchart of part 2 of question 1

<!-- b001200 | heading | pages [12] -->
(2) Establish a Logistic regression model

<!-- b001201 | prose | pages [12] -->
[4]Logistic regression is a statistical model widely used for classification problems, mainly for binary classification . It linearly combines features and uses the Sigmoid function to map the result to a probability value between 0 and 1 to address binary classification issues. The model uses maximum likelihood estimation to optimize parameters and interprets the impact of features on the probability of an event occurring through regression coefficients. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The steps of Logistic regression are as follows: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001202 | heading | pages [12] -->
Step1: Data preparation

<!-- b001203 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Collect a dataset that includes multiple features and a target variable , m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m which is a binary classification variable (0 or 1). Then standardize or normalize the data. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001204 | heading | pages [12] -->
Step2: Define the Logistic regression model

<!-- b001205 | prose | pages [12] -->
Express the linear combination of input features as:

<!-- b001206 | prose | pages [12] -->
=  +  +  +  z X X X (2) 0 1 1 2 2 3 3

<!-- b001207 | prose | pages [12] -->
Map the linear combination to the interval [0, 1] through the Sigmoid function. The probability of the event occurring is 1 1 = = −= P ( Y 1 X ) (3) −  +  +  +  + ( X X X ) z 1 e e 0 1 1 2 2 3 3

<!-- b001208 | heading | pages [12] -->
Step3: Model training

<!-- b001209 | prose | pages [12] -->
Based on the training data, define the likelihood function of Logistic regression, which represents the probability of observing the data given the parameter :

<!-- b001210 | prose | pages [12] -->
m = − ( − Y 1 Y L ) P ( Y X ) 1( P ( Y X )) (4) i i i i i i = i 1

<!-- b001211 | prose | pages [12] -->
To simplify the calculation, take the logarithm to obtain the log-likelihood function:

<!-- b001212 | prose | pages [12] -->
  m   = + − − log L ( ) Y log P ( Y X ) 1( Y ) log( 1 P ( Y X )) (5) i i i i i i = i 1

<!-- b001213 | prose | pages [12, 13] -->
关注数学模型 Estimate the parameter of the model by maximizing the log-likelihood function:

<!-- b001214 | furniture | pages [12] -->
2

<!-- b001215 | furniture | pages [12] -->
MATHmodels

<!-- b001216 | furniture | pages [12] -->
获取更多资讯

<!-- b001217 | furniture | pages [13] -->
Team 2517690

<!-- b001218 | furniture | pages [13] -->
Page 13 of 25

<!-- b001220 | prose | pages [13] -->
ˆ  =  arg max log L ( ) (6)

<!-- b001221 | prose | pages [13] -->
Step4: Calculate the predicted probability and make a classification decision For each sample in the test set, calculate the probability that its class is 1:

<!-- b001222 | prose | pages [13] -->
1 (ˆ = = P Y 1 X ) (7) ˆ ˆ ˆ −  +  + +  + ( X ... nX ) 1 e 0 1 1 n

<!-- b001223 | prose | pages [13] -->
Based on the probability value, classify the sample as 0 or 1, setting the threshold at 0.5:

<!-- b001224 | prose | pages [13] -->
𝑌̂ = {1, 𝑖𝑓 𝑃̂(𝑌= 1|𝑋) ≥0.5 (8) 0, 𝑖𝑓 𝑃̂(𝑌= 1|𝑋) < 0.5

<!-- b001225 | heading | pages [13] -->
5.2.2 Model results

<!-- b001226 | prose | pages [13] -->
微信公众号：数学模型 We trained the model using 10-fold cross-validation. The final regression model obtained is:

<!-- b001227 | prose | pages [13] -->
1 (9) (ˆ = = P Y 1 X ) − + + + + ( .0 006 .0 14 X .0 28 X .0 34 X ) 1 e 1 2 3

<!-- b001228 | prose | pages [13] -->
In a logistic regression model, the odds ratio is the ratio of the probability of an event occurring to the probability of the event not occurring, that is:

<!-- b001229 | prose | pages [13] -->
P = 1 (10) Odds − P 微信号：MATHmodels Solving based on the data, the results are as shown in the following table:

<!-- b001230 | caption | pages [13] -->
Table 6:Forecast of first-time winners

<!-- b001231 | prose | pages [13] -->
Team P Odds Whether to win a medal

<!-- b001232 | prose | pages [13] -->
Angola 0.81 4.26 1

<!-- b001233 | prose | pages [13] -->
EI Salvador 0.72 2.57 1

<!-- b001234 | prose | pages [13] -->
Honduras 0.69 2.23 1

<!-- b001235 | prose | pages [13] -->
Nicaragua 0.67 2.03 1

<!-- b001236 | prose | pages [13] -->
Calculations show that only the p-values of the above four countries are all greater than 0.5 and the odds ratios are relatively large. That is, these countries have a relatively high pos- sibility of winning their first medals at the 2028 Olympic Games. Among them, Angola has the largest p-value of 0.81, meaning it is the most likely to win its first medal.

<!-- b001237 | prose | pages [13] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001238 | furniture | pages [13] -->
m

<!-- b001239 | furniture | pages [13] -->
m

<!-- b001240 | furniture | pages [13] -->
m

<!-- b001241 | furniture | pages [13] -->
m

<!-- b001242 | furniture | pages [13] -->
m

<!-- b001243 | furniture | pages [13] -->
m

<!-- b001244 | furniture | pages [13] -->
m

<!-- b001245 | furniture | pages [13] -->
m

<!-- b001246 | furniture | pages [13] -->
m

<!-- b001247 | furniture | pages [13] -->
m

<!-- b001248 | furniture | pages [13] -->
m

<!-- b001249 | furniture | pages [13] -->
m

<!-- b001250 | furniture | pages [13] -->
m

<!-- b001251 | furniture | pages [13] -->
m

<!-- b001252 | furniture | pages [13] -->
m

<!-- b001253 | furniture | pages [13] -->
m

<!-- b001254 | furniture | pages [13] -->
m

<!-- b001255 | furniture | pages [13] -->
m

<!-- b001256 | furniture | pages [13] -->
m

<!-- b001257 | furniture | pages [13] -->
m

<!-- b001258 | furniture | pages [13] -->
m

<!-- b001259 | furniture | pages [13] -->
m

<!-- b001260 | furniture | pages [13] -->
m

<!-- b001261 | furniture | pages [13] -->
m

<!-- b001262 | furniture | pages [13] -->
m

<!-- b001263 | furniture | pages [13] -->
m

<!-- b001264 | furniture | pages [13] -->
m

<!-- b001265 | furniture | pages [13] -->
m

<!-- b001266 | furniture | pages [13] -->
m

<!-- b001267 | furniture | pages [13] -->
m

<!-- b001268 | furniture | pages [13] -->
m

<!-- b001269 | furniture | pages [13] -->
m

<!-- b001270 | furniture | pages [13] -->
m

<!-- b001271 | furniture | pages [13] -->
m

<!-- b001272 | furniture | pages [13] -->
m

<!-- b001273 | furniture | pages [13] -->
m

<!-- b001274 | furniture | pages [13] -->
m

<!-- b001275 | furniture | pages [13] -->
m

<!-- b001276 | furniture | pages [13] -->
m

<!-- b001277 | furniture | pages [13] -->
m

<!-- b001278 | furniture | pages [13] -->
m

<!-- b001279 | furniture | pages [13] -->
m

<!-- b001280 | furniture | pages [13] -->
m

<!-- b001281 | furniture | pages [13] -->
m

<!-- b001282 | furniture | pages [13] -->
m

<!-- b001283 | furniture | pages [13] -->
m

<!-- b001284 | furniture | pages [13] -->
m

<!-- b001285 | furniture | pages [13] -->
m

<!-- b001286 | furniture | pages [13] -->
m

<!-- b001287 | furniture | pages [13] -->
m

<!-- b001288 | furniture | pages [13] -->
m

<!-- b001289 | furniture | pages [13] -->
m

<!-- b001290 | furniture | pages [13] -->
m

<!-- b001291 | furniture | pages [13] -->
m

<!-- b001292 | furniture | pages [13] -->
m

<!-- b001293 | furniture | pages [13] -->
m

<!-- b001294 | furniture | pages [13] -->
m

<!-- b001295 | furniture | pages [13] -->
m

<!-- b001296 | furniture | pages [13] -->
m

<!-- b001297 | furniture | pages [13] -->
m

<!-- b001298 | furniture | pages [13] -->
m

<!-- b001299 | furniture | pages [13] -->
m

<!-- b001300 | furniture | pages [13] -->
m

<!-- b001301 | furniture | pages [13] -->
m

<!-- b001302 | furniture | pages [13] -->
m

<!-- b001303 | furniture | pages [13] -->
m

<!-- b001304 | furniture | pages [13] -->
m

<!-- b001305 | furniture | pages [13] -->
m

<!-- b001306 | furniture | pages [13] -->
m

<!-- b001307 | furniture | pages [13] -->
m

<!-- b001308 | furniture | pages [13] -->
m

<!-- b001309 | furniture | pages [13] -->
m

<!-- b001310 | furniture | pages [13] -->
m

<!-- b001311 | furniture | pages [13] -->
m

<!-- b001312 | furniture | pages [13] -->
m

<!-- b001313 | furniture | pages [13] -->
m

<!-- b001314 | furniture | pages [13] -->
m

<!-- b001315 | furniture | pages [13] -->
m

<!-- b001316 | furniture | pages [13] -->
m

<!-- b001317 | furniture | pages [13] -->
m

<!-- b001318 | furniture | pages [13] -->
m

<!-- b001319 | furniture | pages [13] -->
m

<!-- b001320 | furniture | pages [13] -->
m

<!-- b001321 | furniture | pages [13] -->
m

<!-- b001322 | furniture | pages [13] -->
m

<!-- b001323 | furniture | pages [13] -->
m

<!-- b001324 | furniture | pages [13] -->
m

<!-- b001325 | furniture | pages [13] -->
m

<!-- b001326 | furniture | pages [13] -->
m

<!-- b001327 | furniture | pages [13] -->
m

<!-- b001328 | furniture | pages [13] -->
m

<!-- b001329 | furniture | pages [13] -->
m

<!-- b001330 | furniture | pages [13] -->
m

<!-- b001331 | furniture | pages [13] -->
m

<!-- b001332 | furniture | pages [13] -->
m

<!-- b001333 | furniture | pages [13] -->
m

<!-- b001334 | furniture | pages [13] -->
m

<!-- b001335 | furniture | pages [13] -->
m

<!-- b001336 | furniture | pages [13] -->
m

<!-- b001337 | furniture | pages [13] -->
m

<!-- b001338 | furniture | pages [13] -->
m

<!-- b001339 | furniture | pages [13] -->
m

<!-- b001340 | furniture | pages [13] -->
m

<!-- b001341 | furniture | pages [13] -->
m

<!-- b001342 | furniture | pages [13] -->
m

<!-- b001343 | furniture | pages [13] -->
m

<!-- b001344 | furniture | pages [13] -->
m

<!-- b001345 | furniture | pages [13] -->
m

<!-- b001346 | furniture | pages [13] -->
m

<!-- b001347 | furniture | pages [13] -->
m

<!-- b001348 | furniture | pages [13] -->
m

<!-- b001349 | furniture | pages [13] -->
m

<!-- b001350 | furniture | pages [13] -->
m

<!-- b001351 | furniture | pages [13] -->
m

<!-- b001352 | furniture | pages [13] -->
m

<!-- b001353 | furniture | pages [13] -->
m

<!-- b001354 | furniture | pages [13] -->
m

<!-- b001355 | furniture | pages [13] -->
m

<!-- b001356 | furniture | pages [13] -->
m

<!-- b001357 | furniture | pages [13] -->
m

<!-- b001358 | furniture | pages [13] -->
m

<!-- b001359 | furniture | pages [13] -->
m

<!-- b001360 | furniture | pages [13] -->
m

<!-- b001361 | furniture | pages [13] -->
m

<!-- b001362 | furniture | pages [13] -->
m

<!-- b001363 | furniture | pages [13] -->
m

<!-- b001364 | furniture | pages [13] -->
m

<!-- b001365 | furniture | pages [13] -->
m

<!-- b001366 | furniture | pages [13] -->
m

<!-- b001367 | furniture | pages [13] -->
m

<!-- b001368 | furniture | pages [13] -->
m

<!-- b001369 | furniture | pages [13] -->
m

<!-- b001370 | furniture | pages [13] -->
m

<!-- b001371 | furniture | pages [13] -->
m

<!-- b001372 | furniture | pages [13] -->
m

<!-- b001373 | furniture | pages [13] -->
m

<!-- b001374 | furniture | pages [13] -->
m

<!-- b001375 | furniture | pages [13] -->
m

<!-- b001376 | furniture | pages [13] -->
m

<!-- b001377 | furniture | pages [13] -->
m

<!-- b001378 | furniture | pages [13] -->
m

<!-- b001379 | furniture | pages [13] -->
m

<!-- b001380 | furniture | pages [13] -->
m

<!-- b001381 | furniture | pages [13] -->
m

<!-- b001382 | furniture | pages [13] -->
m

<!-- b001383 | furniture | pages [13] -->
m

<!-- b001384 | furniture | pages [13] -->
m

<!-- b001385 | furniture | pages [13] -->
m

<!-- b001386 | furniture | pages [13] -->
m

<!-- b001387 | furniture | pages [13] -->
m

<!-- b001388 | furniture | pages [13] -->
m

<!-- b001389 | furniture | pages [13] -->
m

<!-- b001390 | furniture | pages [13] -->
m

<!-- b001391 | furniture | pages [13] -->
m

<!-- b001392 | furniture | pages [13] -->
m

<!-- b001393 | furniture | pages [13] -->
m

<!-- b001394 | furniture | pages [13] -->
m

<!-- b001395 | furniture | pages [13] -->
m

<!-- b001396 | furniture | pages [13] -->
m

<!-- b001397 | furniture | pages [13] -->
m

<!-- b001398 | furniture | pages [13] -->
m

<!-- b001399 | furniture | pages [13] -->
m

<!-- b001400 | furniture | pages [13] -->
m

<!-- b001401 | furniture | pages [13] -->
m

<!-- b001402 | furniture | pages [13] -->
m

<!-- b001403 | furniture | pages [13] -->
m

<!-- b001404 | furniture | pages [13] -->
m

<!-- b001405 | furniture | pages [13] -->
m

<!-- b001406 | furniture | pages [13] -->
m

<!-- b001407 | furniture | pages [13] -->
m

<!-- b001408 | furniture | pages [13] -->
m

<!-- b001409 | furniture | pages [13] -->
m

<!-- b001410 | furniture | pages [13] -->
m

<!-- b001411 | furniture | pages [13] -->
m

<!-- b001412 | furniture | pages [13] -->
m

<!-- b001413 | furniture | pages [13] -->
m

<!-- b001414 | furniture | pages [13] -->
m

<!-- b001415 | furniture | pages [13] -->
m

<!-- b001416 | furniture | pages [13] -->
m

<!-- b001417 | furniture | pages [13] -->
m

<!-- b001418 | furniture | pages [13] -->
m

<!-- b001419 | furniture | pages [13] -->
m

<!-- b001420 | furniture | pages [13] -->
m

<!-- b001421 | furniture | pages [13] -->
m

<!-- b001422 | furniture | pages [13] -->
m

<!-- b001423 | furniture | pages [13] -->
m

<!-- b001424 | furniture | pages [13] -->
m

<!-- b001425 | furniture | pages [13] -->
m

<!-- b001426 | furniture | pages [13] -->
m

<!-- b001427 | furniture | pages [13] -->
m

<!-- b001428 | furniture | pages [13] -->
m

<!-- b001429 | furniture | pages [13] -->
m

<!-- b001430 | furniture | pages [13] -->
m

<!-- b001431 | furniture | pages [13] -->
m

<!-- b001432 | furniture | pages [13] -->
m

<!-- b001433 | furniture | pages [13] -->
m

<!-- b001434 | furniture | pages [13] -->
m

<!-- b001435 | furniture | pages [13] -->
m

<!-- b001436 | furniture | pages [13] -->
m

<!-- b001437 | furniture | pages [13] -->
m

<!-- b001438 | furniture | pages [13] -->
m

<!-- b001439 | furniture | pages [13] -->
m

<!-- b001440 | furniture | pages [13] -->
m

<!-- b001441 | furniture | pages [13] -->
m

<!-- b001442 | furniture | pages [13] -->
m

<!-- b001443 | furniture | pages [13] -->
m

<!-- b001444 | furniture | pages [13] -->
m

<!-- b001445 | furniture | pages [13] -->
m

<!-- b001446 | furniture | pages [13] -->
m

<!-- b001447 | furniture | pages [13] -->
m

<!-- b001448 | furniture | pages [13] -->
m

<!-- b001449 | furniture | pages [13] -->
m

<!-- b001450 | furniture | pages [13] -->
m

<!-- b001451 | furniture | pages [13] -->
m

<!-- b001452 | furniture | pages [13] -->
m

<!-- b001453 | furniture | pages [13] -->
m

<!-- b001454 | furniture | pages [13] -->
m

<!-- b001455 | furniture | pages [13] -->
m

<!-- b001456 | furniture | pages [13] -->
m

<!-- b001457 | furniture | pages [13] -->
m

<!-- b001458 | furniture | pages [13] -->
m

<!-- b001459 | furniture | pages [13] -->
m

<!-- b001460 | furniture | pages [13] -->
m

<!-- b001461 | furniture | pages [13] -->
m

<!-- b001462 | furniture | pages [13] -->
m

<!-- b001463 | furniture | pages [13] -->
m

<!-- b001464 | furniture | pages [13] -->
m

<!-- b001465 | furniture | pages [13] -->
m

<!-- b001466 | furniture | pages [13] -->
m

<!-- b001467 | furniture | pages [13] -->
m

<!-- b001468 | furniture | pages [13] -->
m

<!-- b001469 | furniture | pages [13] -->
m

<!-- b001470 | furniture | pages [13] -->
m

<!-- b001471 | furniture | pages [13] -->
m

<!-- b001472 | furniture | pages [13] -->
m

<!-- b001473 | furniture | pages [13] -->
m

<!-- b001474 | furniture | pages [13] -->
m

<!-- b001475 | furniture | pages [13] -->
m

<!-- b001476 | furniture | pages [13] -->
m

<!-- b001477 | furniture | pages [13] -->
m

<!-- b001478 | furniture | pages [13] -->
m

<!-- b001479 | furniture | pages [13] -->
m

<!-- b001480 | furniture | pages [13] -->
m

<!-- b001481 | furniture | pages [13] -->
m

<!-- b001482 | furniture | pages [13] -->
m

<!-- b001483 | furniture | pages [13] -->
m

<!-- b001484 | furniture | pages [13] -->
m

<!-- b001485 | furniture | pages [13] -->
m

<!-- b001486 | furniture | pages [13] -->
m

<!-- b001487 | furniture | pages [13] -->
m

<!-- b001488 | furniture | pages [13] -->
m

<!-- b001489 | furniture | pages [13] -->
m

<!-- b001490 | furniture | pages [13] -->
m

<!-- b001491 | furniture | pages [13] -->
m

<!-- b001492 | furniture | pages [13] -->
m

<!-- b001493 | furniture | pages [13] -->
m

<!-- b001494 | furniture | pages [13] -->
m

<!-- b001495 | furniture | pages [13] -->
m

<!-- b001496 | furniture | pages [13] -->
m

<!-- b001497 | furniture | pages [13] -->
m

<!-- b001498 | furniture | pages [13] -->
m

<!-- b001499 | furniture | pages [13] -->
m

<!-- b001500 | furniture | pages [13] -->
m

<!-- b001501 | furniture | pages [13] -->
m

<!-- b001502 | furniture | pages [13] -->
m

<!-- b001503 | furniture | pages [13] -->
m

<!-- b001504 | furniture | pages [13] -->
m

<!-- b001505 | furniture | pages [13] -->
m

<!-- b001506 | furniture | pages [13] -->
m

<!-- b001507 | furniture | pages [13] -->
m

<!-- b001508 | furniture | pages [13] -->
m

<!-- b001509 | furniture | pages [13] -->
m

<!-- b001510 | furniture | pages [13] -->
m

<!-- b001511 | furniture | pages [13] -->
m

<!-- b001512 | furniture | pages [13] -->
m

<!-- b001513 | furniture | pages [13] -->
m

<!-- b001514 | furniture | pages [13] -->
m

<!-- b001515 | furniture | pages [13] -->
m

<!-- b001516 | furniture | pages [13] -->
m

<!-- b001517 | furniture | pages [13] -->
m

<!-- b001518 | furniture | pages [13] -->
m

<!-- b001519 | furniture | pages [13] -->
m

<!-- b001520 | furniture | pages [13] -->
m

<!-- b001521 | furniture | pages [13] -->
m

<!-- b001522 | furniture | pages [13] -->
m

<!-- b001523 | furniture | pages [13] -->
m

<!-- b001524 | furniture | pages [13] -->
m

<!-- b001525 | furniture | pages [13] -->
m

<!-- b001526 | furniture | pages [13] -->
m

<!-- b001527 | furniture | pages [13] -->
m

<!-- b001528 | furniture | pages [13] -->
m

<!-- b001529 | furniture | pages [13] -->
m

<!-- b001530 | furniture | pages [13] -->
m

<!-- b001531 | furniture | pages [13] -->
m

<!-- b001532 | furniture | pages [13] -->
m

<!-- b001533 | furniture | pages [13] -->
m

<!-- b001534 | furniture | pages [13] -->
m

<!-- b001535 | furniture | pages [13] -->
m

<!-- b001536 | furniture | pages [13] -->
m

<!-- b001537 | furniture | pages [13] -->
m

<!-- b001538 | furniture | pages [13] -->
m

<!-- b001539 | furniture | pages [13] -->
m

<!-- b001540 | furniture | pages [13] -->
m

<!-- b001541 | furniture | pages [13] -->
m

<!-- b001542 | furniture | pages [13] -->
m

<!-- b001543 | furniture | pages [13] -->
m

<!-- b001544 | furniture | pages [13] -->
m

<!-- b001545 | furniture | pages [13] -->
m

<!-- b001546 | furniture | pages [13] -->
m

<!-- b001547 | furniture | pages [13] -->
m

<!-- b001548 | furniture | pages [13] -->
m

<!-- b001549 | furniture | pages [13] -->
m

<!-- b001550 | furniture | pages [13] -->
m

<!-- b001551 | furniture | pages [13] -->
m

<!-- b001552 | furniture | pages [13] -->
m

<!-- b001553 | furniture | pages [13] -->
m

<!-- b001554 | furniture | pages [13] -->
m

<!-- b001555 | furniture | pages [13] -->
m

<!-- b001556 | furniture | pages [13] -->
m

<!-- b001557 | furniture | pages [13] -->
m

<!-- b001558 | furniture | pages [13] -->
m

<!-- b001559 | furniture | pages [13] -->
m

<!-- b001560 | furniture | pages [13] -->
m

<!-- b001561 | furniture | pages [13] -->
m

<!-- b001562 | furniture | pages [14] -->
Team 2517690

<!-- b001563 | furniture | pages [14] -->
Page 14 of 25

<!-- b001564 | heading | pages [14] -->
5.3 Analysis of Factors Influencing Country Medal Counts

<!-- b001565 | caption | pages [14] -->
Figure 10:Analysis of factors influencing the number of medals

<!-- b001566 | heading | pages [14] -->
5.3.1 Analysis of the Influence of Olympic Events

<!-- b001567 | prose | pages [14] -->
(1) Analysis of the Medal Distribution of Olympic Events for Each Country Based on Radar Charts To more intuitively display the medal distribution of each country in different Olympic events, this study uses radar charts as a visualization tool. Radar charts can effectively present multi-dimensional data and help compare the advantages and disadvantages of each country in various events. Taking the United States, China, and France as examples, the drawn radar charts are as follows:

<!-- b001568 | caption | pages [14] -->
Figure 11:Radar chart analysing levels in selected sports

<!-- b001569 | prose | pages [14] -->
The above figure shows the performance differences among China, the United States, and France in five Olympic events. China stands out in swimming, wrestling, and diving, with par- ticularly obvious advantages in diving and wrestling. The United States takes a dominant po- sition in track and field and swimming, demonstrating its strong competitiveness in multiple events. France shows a relatively balanced performance, with certain advantages in shooting and swimming. Overall, it reflects the differences in competitiveness of the three countries in their respective advantageous events.

<!-- b001570 | prose | pages [14, 15] -->
关注数学模型 (2) Grey Relational Analysis Grey Relational Analysis quantifies the degree of association between different factors by comparing their changing trends[5]. It is particularly suitable for situations with incomplete in- formation or uncertainty. This method identifies key influencing factors or conducts pattern recognition by calculating the degree of association. In this study, the number of medals in each sports event is regarded as a subsequence, and the total number of medals of each country is 微信公众号：数学模型 regarded as the mother sequence. The degree of association between each event and the total number of medals of each country is calculated, and the strength of their correlation is meas- ured by the value of the degree of association.

<!-- b001571 | furniture | pages [14] -->
2

<!-- b001572 | furniture | pages [14] -->
MATHmodels

<!-- b001573 | furniture | pages [14] -->
获取更多资讯

<!-- b001574 | furniture | pages [15] -->
Team 2517690

<!-- b001575 | furniture | pages [15] -->
Page 15 of 25

<!-- b001577 | prose | pages [15] -->
The analysis steps are as follows:： Step1: Determine the mother sequence and subsequences Suppose there are evaluation objects and evaluation indicators. The mother sequence = = = = x x ( k ) k 2,1 ,..., n x x ( k ) k 2,1 ,..., m is , and the subsequences are . 0 0 i i Step2: Preprocess the variables Pre-process each indicator in the mother sequence and subsequences respectively. First, 微信号：MATHmodels calculate the mean of each indicator, and then divide each element in the indicator by its mean. This can eliminate the influence of dimensions and narrow the range of variables to simplify calculations. Let the standardized matrix be Z, and the elements in Z be denoted as , The calculation formula is as follows:

<!-- b001578 | prose | pages [15] -->
x i j = Z (11) i j x i j

<!-- b001579 | prose | pages [15] -->
Obtain the standardized matrix: Z   Z Z Z 11 12 1 m   Z Z Z (12)   21 22 2 m     Z Z Z   n 1 n 2 nm

<!-- b001580 | prose | pages [15] -->
Step3: Calculate the correlation coefficients between each indicator in the subse- quences and the mother sequence

<!-- b001581 | prose | pages [15] -->
+  a b (13) = = = y x k ( ( ), x k ( )) ( i 1,2, m k , 1,2, n ) 0 i − +  | x k ( ) x k ( ) | b 0 i

<!-- b001582 | prose | pages [15] -->
Among them, is the distinguishing coefficient, usually taken as 0.5. is the mini- mum difference of the two levels, and is the maximum difference of the two levels. The calculation formulas are as follows:

<!-- b001583 | prose | pages [15, 16] -->
= − a min min | x k ( ) x k ( ) | (14) 0 i i k = − b max max | x k ( ) x k ( ) | 0 i i k Step4: Calculate the grey relational degree +  n n 1 1 a b (15)   = = y x x ( , ) y x k ( ( ), x k ( )) 0 i 0 i − +  n n | x k ( ) x k ( ) | b = = k 1 k 1 0 i

<!-- b001584 | furniture | pages [16] -->
Team 2517690

<!-- b001585 | furniture | pages [16] -->
Page 16 of 25

<!-- b001587 | prose | pages [16] -->
This study uses the grey relational analysis model to quantify the degree of association between each sports event and the total number of medals, and further explore their correlation. The following table shows the degree of association between some events and the total number of medals of some countries:

<!-- b001588 | caption | pages [16] -->
Table 7:Correlation between sports and medals

<!-- b001589 | prose | pages [16] -->
Athletics Swimming Diving Volleyball Triathlon

<!-- b001590 | prose | pages [16] -->
United 0.84 0.83 0.45 0.67 0.51 States

<!-- b001591 | prose | pages [16] -->
China 0.54 0.65 0.87 0.79 0.21

<!-- b001592 | prose | pages [16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Great m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 0.45 0.66 0.12 0.34 0.82 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Britain m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Australia 0.5 0.54 0.56 0.21 0.56 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001593 | prose | pages [16] -->
Japan 0.44 0.32 0.45 0.45 0.11

<!-- b001594 | prose | pages [16] -->
By analyzing the above table, it can be seen that the United States has a high degree of association with track and field and swimming events, which are 0.84 and 0.83 respectively. This indicates that these two events are crucial to the number of its medals. China has the highest degree of association with the diving event (0.87), highlighting the dominant position of diving in its Olympic performance. The degree of association of the United Kingdom with the triathlon is 0.82, showing the significant impact of this emerging event on the total number of its medals. In contrast, Japan has a generally low degree of association with various events, indicating its relatively balanced overall competitiveness in multiple events.

<!-- b001595 | heading | pages [16] -->
5.3.2 Influence of the Events Chosen by the Host Country on the Results

<!-- b001596 | prose | pages [16] -->
(1) Visual analysis To visually display the changes in the medal performances of various countries in succes- sive Olympic Games, the following chart shows the number of medals of different countries in each Olympic Games. The horizontal axis represents the year of the Olympic Games, the ver- tical axis represents the number of medals, and each line represents the number of medals of a particular country.

<!-- b001597 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型

<!-- b001598 | furniture | pages [16] -->
2

<!-- b001599 | furniture | pages [16] -->
MATHmodels

<!-- b001600 | furniture | pages [16] -->
获取更多资讯

<!-- b001601 | furniture | pages [17] -->
Team 2517690

<!-- b001602 | furniture | pages [17] -->
Page 17 of 25

<!-- b001604 | caption | pages [17] -->
Figure 12:Time series chart of the number of medals

<!-- b001605 | prose | pages [17] -->
From the graph, it can be observed that the total number of medals of the United States reached its peak in 1984, and this phenomenon is closely related to the fact that the Olympic Games were held in the United States that year. Similarly, China also achieved a record-high number of medals in 2008, reflecting the positive impact of the host status on its performance. In 2020, the total number of medals of France also reached its peak, which is inseparable from 微信号：MATHmodels Paris being the host city. Thus, it can be seen that the host status significantly promotes the medal performance of the host country in the Olympic Games.

<!-- b001606 | prose | pages [17] -->
(2) The potential impact of the United States' host status on its medal performance in 2028 The five new sports added to the 2028 Los Angeles Olympics - baseball/softball, lacrosse, cricket, squash, and flag football - will enhance the United States' medal potential. Baseball and lacrosse, as traditional strong suits of the United States, are expected to contribute a large number of medals. Although cricket and squash are relatively niche sports, their inclusion is expected to boost the United States' performance in these events. Flag football provides new opportunities for the young population, further increasing the United States' competitiveness in the Olympics.

<!-- b001607 | heading | pages [17] -->
6 The Study of a “Great Coach” Effect

<!-- b001608 | heading | pages [17] -->
6.1 Analysis of the “great coach” effect

<!-- b001609 | heading | pages [17] -->
6.1.1 Two-sample Mean Hypothesis Testing

<!-- b001610 | prose | pages [17] -->
To explore whether the "great coach" effect has an impact on Olympic medal performance, we selected the two-sample mean hypothesis testing method. This method is applicable for comparing whether there is a significant difference between the means of two independent samples. In this study, we defined the two samples as follows: one set of data represents the perfor-

<!-- b001611 | caption | pages [17] -->
Figure 13:Test Method

<!-- b001612 | prose | pages [17, 18] -->
mance before a great coach took charge, and the other represents the performance after the coach started coaching. By examining the differences in the number of Olympic medals between the two groups of countries, we can evaluate the potential impact of the "great coach" effect. Step1: Formulate hypotheses

<!-- b001613 | furniture | pages [18] -->
Page 18 of 25

<!-- b001614 | furniture | pages [18] -->
Team 2517690

<!-- b001616 | prose | pages [18] -->
Null Hypothesis H0 :µ1 = µ2 (16) Alternative Hypothesis H1 :µ1 ≠μµ2

<!-- b001617 | prose | pages [18] -->
Set the confidence level at 95%. Step2: Calculate the P – value According to the results of the hypothesis test, when the P-value is less than the set sig- nificance level, we reject the null hypothesis and conclude that the coach's coaching has a sig- nificant impact on the country's performance. If the P-value is greater than 0.05, it indicates that there is no significant change in performance before and after the coach takes charge.

<!-- b001618 | prose | pages [18] -->
For the convenience of statistics, we record the total number of medals as follows:

<!-- b001619 | prose | pages [18] -->
Total = 4× Gold + 2× Silver + Bronze We use SPSS for significance testing, and the results are shown in the following table (both Pre - coaching medals and Post - coaching medals in the table below are average values):

<!-- b001620 | caption | pages [18] -->
Table 8:Significance test results

<!-- b001621 | prose | pages [18] -->
Pre-coaching Post-coaching Sport Coach Time Team P medals medals US 0.5 0.05 Volleyball 2005-2008 2 Lang Ping US 0.71 0.01 Gymnastics 1981-2016 3 Martha Karolyi CHI Volleyball 2013-2016 1.5 0.007 Lang Ping 4 JAP Béla Károlyi 2000-2012 1.16 0.09 2.67 Gymnastics

<!-- b001622 | prose | pages [18] -->
In the table, based on the analysis of the P - values, Lang Ping's coaching of the US wom- en's volleyball team and the Chinese women's volleyball team significantly increased the medal counts of both teams. The P - values are 0.05 and 0.007 respectively, indicating her significant influence. Martha Karolyi's coaching of the US gymnastics team also significantly increased the medal count, with a P-value of 0.01, demonstrating her significant contribution. Although Béla Károlyi's influence on the Japanese gymnastics team led to an increase, the P-value is 0.07, indicating that the change is not significant. This shows that the "great coach" effect has played a key role in some teams. 6.1.2 Chi-square Test The chi-square test is used to determine whether two categorical variables are related or independent[6]. By comparing the differences between the actual observed frequencies and the expected frequencies, if the p-value is significantly small, it indicates that there is a statistical association between the variables; otherwise, they are considered independent. In this paper, the frequency data of multiple categorical characteristics were analyzed, and contingency ta- bles were constructed for the test.

<!-- b001623 | prose | pages [18] -->
First, when analyzing whether there is a relationship between great coaches and the award results, take Coach Lang Ping's guidance of the Chinese team and the US team as an example, by organizing the award-winning situations of the Chinese and US women's volleyball teams in 2008 and 2016, the following two - dimensional contingency table can be obtained:

<!-- b001624 | prose | pages [18, 19] -->
关注数学模型 Presence of an excellent coach Total Yes No 12 CHI 13 1 USA 4 5 1 Total 16 2 18 Set up the null hypothesis H0 : There is no relationship between the presence of a great coach and the number of medals won, that is, they are independent, which can be expressed as follows:

<!-- b001625 | furniture | pages [18] -->
获取更多资讯

<!-- b001626 | furniture | pages [19] -->
Page 19 of 25

<!-- b001627 | furniture | pages [19] -->
Team 2517690

<!-- b001628 | caption | pages [19] -->
Table 9:chi-square test series

<!-- b001630 | prose | pages [19] -->
(17) H0 : pij = Pi.p.j Next, under the condition that the null hypothesis holds, the maximum likelihood esti- 模型 mates of each parameter can be obtained:

<!-- b001631 | prose | pages [19] -->
ni. (i = 1,2) pi. = (18) n n.j (j =1,2) p.j n Its test statistic is:

<!-- b001632 | prose | pages [19] -->
(nij −npij 2 x²=∑∑ (19) npij j=1 i=1 Finally, the calculated p-value is 0.009, which is less than the significance level of 0.05. There is sufficient evidence to reject the null hypothesis H0 . Therefore, it can be concluded that the guidance of a great coach has a significant impact on the award-winning situation of this event.

<!-- b001633 | heading | pages [19] -->
6.2 Contribution of “great coach" Based on the Logistic

<!-- b001634 | prose | pages [19] -->
1mc Input Ouput

<!-- b001635 | prose | pages [19] -->
Coaching duration of excellent coaches Coach Regression contribution coefficient Medals won in Trained logistic event history regression Event medal- Optimal winning investment probability event ● Number of event ● participants

<!-- b001636 | caption | pages [19] -->
Figure 14: Coaching contribution analysis

<!-- b001637 | prose | pages [19] -->
In order to deeply explore the potential impact of "great coaches" on Olympic perfor- mance and provide guidance for countries in sports investment decisions, this study will use the Logistic regression model to test whether great coaches have significantly increased the medal counts of certain countries and explore the investment directions in which great coaches should be prioritized when different countries select sports events.

<!-- b001638 | prose | pages [19, 20] -->
Let the coaching time of a great coach be x1 (if there is no great coach for a certain event, x1 = 0), the number of medals won in the history of this event be x2 (x2 has been converted.), 3x , and y be a 0 - 1 the number of athletes participating in this event for this country be variable indicating whether the sports event wins an award.

<!-- b001639 | furniture | pages [20] -->
Team 2517690

<!-- b001640 | furniture | pages [20] -->
Page 20 of 25

<!-- b001642 | prose | pages [20] -->
After substituting the standardized data into the logistic regression model and estimating the model parameters, the regression model is obtained as follows:

<!-- b001643 | prose | pages [20] -->
1 (ˆ = = P y 1 x ) − + + + + ( .2 12 4.14 x 7.25 x .1 98 x ) 1 e 1 2 3 (20) p = + + + ln( ) .2 12 .4 14 x .7 25 x .1 98 x 1 2 3 − 1 p A significance test was conducted on the regression coefficients, and the results are as follows:

<!-- b001644 | caption | pages [20] -->
Table 10:Logistic Re-regression Significance Test Results

<!-- b001645 | prose | pages [20] -->
Varible Standard Error P

<!-- b001646 | prose | pages [20] -->
Coaching Duration 4.14 0.67 0.04

<!-- b001647 | prose | pages [20] -->
Historical medal tally 7.25 0.91 0.006

<!-- b001648 | prose | pages [20] -->
Number of participants 1.98 0.39 0.05

<!-- b001649 | prose | pages [20] -->
As can be seen from the above table, the influence of the coaching time of a great coach on whether the sports event wins an award is significant, and it shows a positive correlation. Based on the values of the regression coefficients, it can be seen that the contribution of the coaching duration to the award-winning result lies between the level of the athletes in this event and the number of participating athletes.

<!-- b001650 | heading | pages [20] -->
6.3 Investment in “great coach”

<!-- b001651 | prose | pages [20] -->
We select China, the United States, and Japan as the research objects.

<!-- b001652 | prose | pages [20] -->
(1) Screen out the events in which each country has not won any medals in the past four Olympic Games.

<!-- b001653 | prose | pages [20] -->
We believe that the events that have won medals in the past four Olympic Games are already mature enough. We also believe that there is greater room for improvement in the events in which countries have not won medals in the past four Olympic Games, and these events are in more urgent need of the guidance of great coaches.

<!-- b001654 | prose | pages [20] -->
(2) Selection of investment projects 1x =4, input it into the trained Change the guidance time of the already selected events, set logistic regression model, and select the projects for investment by comparing the probabilities of these projects winning awards. Take the Chinese team as an example:

<!-- b001655 | caption | pages [20] -->
Table 11:Investment projects and probability

<!-- b001656 | prose | pages [20, 21] -->
关注数学模型 According to the analysis of the logistic regression model, the men's volleyball event has the highest probability of the Chinese team winning an award. Therefore, it is recommended to prioritize investment in "great coaches" to increase the winning chances of this event. In contrast, the probability of the Chinese men's football team winning an award is relatively low, 微信公众号：数学模型 and it may not be the main investment direction.

<!-- b001657 | furniture | pages [20] -->
2

<!-- b001658 | furniture | pages [20] -->
MATHmodels

<!-- b001659 | furniture | pages [20] -->
获取更多资讯

<!-- b001660 | furniture | pages [21] -->
Team 2517690

<!-- b001661 | furniture | pages [21] -->
Page 21 of 25

<!-- b001663 | prose | pages [21] -->
For the United States, the probabilities of winning awards in badminton and table tennis events are relatively high. It is recommended to allocate "great coach" resources to these two events. The Japanese team should increase its investment in coaches for the swimming event to enhance its competitiveness and medal potential in this field.

<!-- b001664 | heading | pages [21] -->
7 Predicting Olympic Medals: Insights and Strategies

<!-- b001665 | heading | pages [21] -->
7.1 The Number of Participating Athletes and the Potential to Win Medals

<!-- b001666 | prose | pages [21] -->
微信号：MATHmodels The model demonstrates the impact of the number of participating athletes on the number of medals. More athletes mean more competition opportunities and potential medal opportuni- ties. Specifically, countries with a large number of participants, such as the United States and China, usually have strong competitiveness in multiple events.

<!-- b001667 | prose | pages [21] -->
National Olympic Committees can increase the overall number of medals by expanding the scope of athlete selection and increasing the number of participating athletes in certain events. Diversify the events of participation: In addition to traditional dominant events, Na- tional Olympic Committees can also encourage athletes to participate in more emerging or less popular events to increase the chances of winning awards in these events.

<!-- b001668 | heading | pages [21] -->
7.2 Medal Distribution of Different Countries in Various Events

<!-- b001669 | prose | pages [21] -->
We used the grey relational analysis model to reveal the medal distribution of different countries in various events. For example, the United States has a high degree of correlation with track and field and swimming events, indicating that these events have a significant impact on its total medal count; China has the highest correlation with the diving event, demonstrating the decisive role of diving in China's medal performance.

<!-- b001670 | prose | pages [21] -->
Based on this insight, countries can adopt the following strategies: ⚫ Concentrate resources: National Olympic Committees can use grey relational analysis to identify the events that contribute the most to their total medal count. Then, they can concentrate resources on training and selection in these events to enhance their competi- tiveness in them. ⚫ Invest in emerging events: At the same time, grey relational analysis can also help iden- tify those potentially overlooked and underdeveloped events, providing countries with more potential medal opportunities.

<!-- b001671 | heading | pages [21] -->
7.3 Set Advantageous Events

<!-- b001672 | prose | pages [21] -->
The advantages of the host country in the Olympic Games come not only from factors such as psychology, resources, and audience support but also from its influence on event set- ting, schedule arrangement and rule adjustment, which can further enhance this advantage.

<!-- b001673 | prose | pages [21, 22] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m From the perspective of game theory, the status of the host country actually provides a unique strategic gaming opportunity for the host nation.

<!-- b001674 | furniture | pages [21] -->
m

<!-- b001675 | furniture | pages [21] -->
m

<!-- b001676 | furniture | pages [21] -->
m

<!-- b001677 | furniture | pages [21] -->
m

<!-- b001678 | furniture | pages [21] -->
m

<!-- b001679 | furniture | pages [21] -->
m

<!-- b001680 | furniture | pages [21] -->
m

<!-- b001681 | furniture | pages [21] -->
m

<!-- b001682 | furniture | pages [21] -->
m

<!-- b001683 | furniture | pages [21] -->
m

<!-- b001684 | furniture | pages [21] -->
m

<!-- b001685 | furniture | pages [21] -->
m

<!-- b001686 | furniture | pages [21] -->
m

<!-- b001687 | furniture | pages [21] -->
m

<!-- b001688 | furniture | pages [21] -->
m

<!-- b001689 | furniture | pages [21] -->
m

<!-- b001690 | furniture | pages [21] -->
m

<!-- b001691 | furniture | pages [21] -->
m

<!-- b001692 | furniture | pages [21] -->
m

<!-- b001693 | furniture | pages [21] -->
m

<!-- b001694 | furniture | pages [21] -->
m

<!-- b001695 | furniture | pages [21] -->
m

<!-- b001696 | furniture | pages [21] -->
m

<!-- b001697 | furniture | pages [21] -->
m

<!-- b001698 | furniture | pages [21] -->
m

<!-- b001699 | furniture | pages [21] -->
m

<!-- b001700 | furniture | pages [21] -->
m

<!-- b001701 | furniture | pages [21] -->
m

<!-- b001702 | furniture | pages [21] -->
m

<!-- b001703 | furniture | pages [21] -->
m

<!-- b001704 | furniture | pages [21] -->
m

<!-- b001705 | furniture | pages [21] -->
m

<!-- b001706 | furniture | pages [21] -->
m

<!-- b001707 | furniture | pages [21] -->
m

<!-- b001708 | furniture | pages [21] -->
m

<!-- b001709 | furniture | pages [21] -->
m

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

<!-- b001998 | furniture | pages [22] -->
Team 2517690

<!-- b001999 | furniture | pages [22] -->
Page 22 of 25

<!-- b002001 | heading | pages [22] -->
7.3.1 N-player game

<!-- b002002 | prose | pages [22] -->
In a multi-party game[7], the goal of each player is usually to maximize their own utility (such as winning more medals), and the strategic choices of each player will affect the outcomes of other players. Therefore, the overall outcome of the game depends not only on the strategy of each individual player but also on the combination of strategies of all players. This requires us to take into account the interaction of the strategies of each player during the analysis. Suppose there are multiple countries involved, in- cluding the host country and other participating countries. Each country has its own "strategy space", that is, choosing which events to compete for medals and maximizing its own interests (the number of medals) through strategic choices. Figure 15：N-Player Game Composition

<!-- b002003 | heading | pages [22] -->
7.3.2 The strategies chosen by the host country and

<!-- b002004 | prose | pages [22] -->
other countries ⚫ Strategies of the host country: The host country can create more medal opportunities in its own advantageous events. For example, it can increase the number of matches in certain competitions or optimize the competition format to enhance the probability of its own ath- letes winning medals. The host country can also use its control over the schedule to reduce the competition pressure on foreign athletes or increase the training time for its own ath- letes.

<!-- b002005 | prose | pages [22] -->
Strategies of other countries: Other countries will decide their investment in certain ⚫ events based on the choices made by the host country. If the host country dominates in certain events, other countries may choose to avoid these events and instead allocate more resources to other events, especially those in which the host country may not have an edge.

<!-- b002006 | heading | pages [22] -->
7.3.3 Nash Equilibrium

<!-- b002007 | prose | pages [22] -->
Ultimately, this game will tend towards an equilibrium state[8]. In this state, each country's strategy reaches its best response strategy. That is, considering the choices of other countries, neither the host country nor other participating countries can increase their medal counts by unilaterally changing their own strategies. Under this equilibrium, the strategic choices of countries will influence each other and jointly determine the final medal distribution.

<!-- b002008 | heading | pages [22] -->
8 Sensitivity Analysis and Error Analysis

<!-- b002009 | heading | pages [22] -->
8.1 Sensitivity Analysis

<!-- b002010 | prose | pages [22] -->
We examined the sensitivity of the classification results by changing the number of folds for cross-validation of the logistic regression model. The number of folds for cross-testing is set to be 8, 9, 10, 11, respectively. The coefficient of variation of the classification results is detected to judge whether the model is robust or not.

<!-- b002011 | prose | pages [22] -->
Introducing the coefficient of variation , define：

<!-- b002012 | prose | pages [22, 23] -->
关注数学模型  (21)  =  Where  represents the accuracy of the model cross-validated at 10 fold of the original scheme， indicates the absolute value of the change in the accuracy rate after changing the number of folds.

<!-- b002013 | furniture | pages [22] -->
2

<!-- b002014 | furniture | pages [22] -->
MATHmodels

<!-- b002015 | furniture | pages [22] -->
获取更多资讯

<!-- b002016 | furniture | pages [23] -->
Team 2517690

<!-- b002017 | furniture | pages [23] -->
Page 23 of 25

<!-- b002019 | caption | pages [23] -->
Table12  Relationship between cross-test and coefficient of variation

<!-- b002020 | prose | pages [23] -->
coefficient of variatio  Cross-checking Folds 8 5% 微信公众号：数学模型 9 0 11 3.46% From the above table, we can see that changing the number of cross folds changes the accuracy of the trained model within 5%, which indicates that the change in accuracy is not significant. Thus, this model is robust.

<!-- b002021 | heading | pages [23] -->
8.2 Error Analysis

<!-- b002022 | prose | pages [23] -->
In order to assess the prediction accuracy of the Random Forest regression model used in this study, a detailed error analysis was performed. By analyzing the performance of the model 微信号：MATHmodels on the test set, it is possible to get a better understanding of the generalization ability and sta- bility of the model under different conditions. And in this section, the error of the model is presented through visual graphs.

<!-- b002023 | prose | pages [23] -->
Firstly, we assessed the prediction accuracy of the model by plotting the true values of the test set against the fitted values of the model as follows：

<!-- b002024 | prose | pages [23] -->
Figure 16：Comparision of test set prediction results

<!-- b002025 | prose | pages [23] -->
As can be seen from the figure, the model performs relatively accurately in predicting the number of medals for most countries, with small errors between the true and fitted values. However, some countries have relatively large prediction errors, which may be related to the characteristics of some specific events, data noise, or underfitting of the model to some varia- bles.

<!-- b002026 | furniture | pages [24] -->
Team 2517690

<!-- b002027 | furniture | pages [24] -->
Page 24 of 25

<!-- b002028 | prose | pages [24] -->
To further analyze the performance of the Random Forest regression model, we explored the effect of the number of decision trees on the model error. We plotted the relationship be- tween the number of decision trees and the error as follows：

<!-- b002029 | prose | pages [24] -->
Figure 17：Plot of the relationship between the number of decision trees and error

<!-- b002030 | prose | pages [24] -->
It can be observed from the figure that the error of the model gradually decreases as the number of decision trees increases, indicating that more decision trees help to improve the stability and accuracy of the model. When the number of decision trees reaches a certain value, the decrease of the error tends to level off, indicating that the fitting ability of the model is close to saturation at this point, and further increasing the number of decision trees has a limited effect on the improvement of the error.

<!-- b002031 | heading | pages [24] -->
9 Strengths and Weaknesses

<!-- b002032 | heading | pages [24] -->
9.1 Strengths

<!-- b002033 | prose | pages [24] -->
⚫ The model we proposed makes full use of official data and analyses the data in depth, and the results of the study are highly informative and can be applied to future predictions about Olympic medals. ⚫ Random forests are more accurate, robust, and less prone to overfitting, and are used to predict the 2028 Olympic medal table with less error. ⚫ We use logistic regression to predict the probability of first-time winners for non-winning countries, taking full account of relevant factors, and is relatively robust to outliers, with reliable results. ⚫ The use of two-sample mean hypothesis tests and chi-square tests to simultaneously ana- lyse the “great coach” effect reduces chance error and produces convincing results.

<!-- b002034 | heading | pages [24] -->
9.2 Weaknesses

<!-- b002035 | prose | pages [24] -->
⚫ The model we presented is very comprehensive in its consideration of the problem indi- cators, but the lack of data for some of the indicators may make the results subject to some errors.

<!-- b002036 | prose | pages [24] -->
关注数学模型

<!-- b002037 | furniture | pages [24] -->
2

<!-- b002038 | furniture | pages [24] -->
MATHmodels

<!-- b002039 | furniture | pages [24] -->
获取更多资讯

<!-- b002040 | furniture | pages [25] -->
Team 2517690

<!-- b002041 | furniture | pages [25] -->
Page 25 of 25

<!-- b002042 | heading | pages [25] -->
10 Conclusion

<!-- b002043 | prose | pages [25] -->
We performed a multi-dimensional analysis of factors affecting Olympic medal counts and developed a machine learning prediction model. Key factors such as athlete performance, event types, host status, and participation were found to influence medal outcomes. The Ran- dom Forest regression model demonstrated high accuracy, with predictions for the 2028 Olym- pics indicating continued dominance by the U.S. and China, while Japan's gold medal count may decline.

<!-- b002044 | prose | pages [25] -->
Grey correlation analysis reveals performance differences across disciplines, helping countries identify competitive areas. The study emphasizes the impact of host status on medal 微信公众号：数学模型 counts, particularly for the U.S. at the 2028 Los Angeles Olympics, where new sports may boost medal potential. Overall, the findings offer a scientific basis for the Olympic Committee to optimize training and resource allocation strategies.

<!-- b002045 | heading | pages [25] -->
References

<!-- b002046 | references | pages [25] -->
[1] Nagpal P , Gupta K , Verma Y ,et al.Paris Olympic (2024) Medal Tally Predic-

<!-- b002047 | references | pages [25] -->
tion[C]//International Conference on Data Management, Analytics & Innovation.Springer, Sin-

<!-- b002048 | references | pages [25] -->
gapore, 2023.

<!-- b002049 | references | pages [25] -->
微信号：MATHmodels

<!-- b002050 | references | pages [25] -->
[2] Song, Z. (2024).Prediction of the Number and Trend of Olympic Medals Won by Var-

<!-- b002051 | references | pages [25] -->
ious Countries Based on Neural Networks.Applied and Computational Engineering,109,87-91.

<!-- b002052 | references | pages [25] -->
[3] J. Moolchandani, V. Chole, S. Sahu, R. Kumar, A. Shukla and A. Kumar, "Predictive

<!-- b002053 | references | pages [25] -->
Analytics in Sports: Using Machine Learning to Forecast Outcomes and Medal Tally Trends at

<!-- b002054 | references | pages [25] -->
the 2024 Summer Olympics," 2024 4th International Conference on Technological Advance-

<!-- b002055 | references | pages [25] -->
ments in Computational Sciences (ICTACS), Tashkent, Uzbekistan, 2024, pp. 1987-1992.

<!-- b002056 | references | pages [25] -->
[4]Tomz M , King G , Zeng L .ReLogit: Rare Events Logistic Regression[J].Journal of

<!-- b002057 | references | pages [25] -->
Statistical Software, 2003, 008.

<!-- b002058 | references | pages [25] -->
[5]Zhou L, Wang Y, An G, et al. Multi-objective grey correlation analysis based on CFRP

<!-- b002059 | references | pages [25] -->
Helical Milling simulation model[J]. The International Journal of Advanced Manufacturing

<!-- b002060 | references | pages [25] -->
Technology, 2024: 1-21.

<!-- b002061 | references | pages [25] -->
[6]Lugo-Armenta J G, Pino-Fan L R. An approach to inferential reasoning levels on the

<!-- b002062 | references | pages [25] -->
Chi-square statistic[J]. EURASIA Journal of Mathematics, Science and Technology Education,

<!-- b002063 | references | pages [25] -->
2024, 20(1): em2388.

<!-- b002064 | references | pages [25] -->
[7]Liu Z, Wang J, Li X. Evolutionary dynamics of networked N-player trust games with

<!-- b002065 | references | pages [25] -->
exclusion strategy[J]. Chaos, Solitons & Fractals, 2024, 186: 115214.

<!-- b002066 | references | pages [25] -->
[8]Wei S, Wang L, Evans P C, et al. NAFLD and NASH: etiology, targets and emerging

<!-- b002067 | references | pages [25] -->
therapies[J]. Drug Discovery Today, 2024: 103910.

<!-- b002068 | references | pages [25] -->
[9] https://coachfederation.org/

<!-- b002069 | references | pages [25] -->
[10] https://www.bleacherreport.com/

<!-- b002070 | references | pages [25] -->
m

<!-- b002071 | references | pages [25] -->
m

<!-- b002072 | references | pages [25] -->
m

<!-- b002073 | references | pages [25] -->
m

<!-- b002074 | references | pages [25] -->
m

<!-- b002075 | references | pages [25] -->
m

<!-- b002076 | references | pages [25] -->
m

<!-- b002077 | references | pages [25] -->
m

<!-- b002078 | references | pages [25] -->
m

<!-- b002079 | references | pages [25] -->
m

<!-- b002080 | references | pages [25] -->
m

<!-- b002081 | references | pages [25] -->
m

<!-- b002082 | references | pages [25] -->
m

<!-- b002083 | references | pages [25] -->
m

<!-- b002084 | references | pages [25] -->
m

<!-- b002085 | references | pages [25] -->
m

<!-- b002086 | references | pages [25] -->
m

<!-- b002087 | references | pages [25] -->
m

<!-- b002088 | references | pages [25] -->
m

<!-- b002089 | references | pages [25] -->
m

<!-- b002090 | references | pages [25] -->
m

<!-- b002091 | references | pages [25] -->
m

<!-- b002092 | references | pages [25] -->
m

<!-- b002093 | references | pages [25] -->
m

<!-- b002094 | references | pages [25] -->
m

<!-- b002095 | references | pages [25] -->
m

<!-- b002096 | references | pages [25] -->
m

<!-- b002097 | references | pages [25] -->
m

<!-- b002098 | references | pages [25] -->
m

<!-- b002099 | references | pages [25] -->
m

<!-- b002100 | references | pages [25] -->
m

<!-- b002101 | references | pages [25] -->
m

<!-- b002102 | references | pages [25] -->
m

<!-- b002103 | references | pages [25] -->
m

<!-- b002104 | references | pages [25] -->
m

<!-- b002105 | references | pages [25] -->
m

<!-- b002106 | references | pages [25] -->
m

<!-- b002107 | references | pages [25] -->
m

<!-- b002108 | references | pages [25] -->
m

<!-- b002109 | references | pages [25] -->
m

<!-- b002110 | references | pages [25] -->
m

<!-- b002111 | references | pages [25] -->
m

<!-- b002112 | references | pages [25] -->
m

<!-- b002113 | references | pages [25] -->
m

<!-- b002114 | references | pages [25] -->
m

<!-- b002115 | references | pages [25] -->
m

<!-- b002116 | references | pages [25] -->
m

<!-- b002117 | references | pages [25] -->
m

<!-- b002118 | references | pages [25] -->
m

<!-- b002119 | references | pages [25] -->
m

<!-- b002120 | references | pages [25] -->
m

<!-- b002121 | references | pages [25] -->
m

<!-- b002122 | references | pages [25] -->
m

<!-- b002123 | references | pages [25] -->
m

<!-- b002124 | references | pages [25] -->
m

<!-- b002125 | references | pages [25] -->
m

<!-- b002126 | references | pages [25] -->
m

<!-- b002127 | references | pages [25] -->
m

<!-- b002128 | references | pages [25] -->
m

<!-- b002129 | references | pages [25] -->
m

<!-- b002130 | references | pages [25] -->
m

<!-- b002131 | references | pages [25] -->
m

<!-- b002132 | references | pages [25] -->
m

<!-- b002133 | references | pages [25] -->
m

<!-- b002134 | references | pages [25] -->
m

<!-- b002135 | references | pages [25] -->
m

<!-- b002136 | references | pages [25] -->
m

<!-- b002137 | references | pages [25] -->
m

<!-- b002138 | references | pages [25] -->
m

<!-- b002139 | references | pages [25] -->
m

<!-- b002140 | references | pages [25] -->
m

<!-- b002141 | references | pages [25] -->
m

<!-- b002142 | references | pages [25] -->
m

<!-- b002143 | references | pages [25] -->
m

<!-- b002144 | references | pages [25] -->
m

<!-- b002145 | references | pages [25] -->
m

<!-- b002146 | references | pages [25] -->
m

<!-- b002147 | references | pages [25] -->
m

<!-- b002148 | references | pages [25] -->
m

<!-- b002149 | references | pages [25] -->
m

<!-- b002150 | references | pages [25] -->
m

<!-- b002151 | references | pages [25] -->
m

<!-- b002152 | references | pages [25] -->
m

<!-- b002153 | references | pages [25] -->
m

<!-- b002154 | references | pages [25] -->
m

<!-- b002155 | references | pages [25] -->
m

<!-- b002156 | references | pages [25] -->
m

<!-- b002157 | references | pages [25] -->
m

<!-- b002158 | references | pages [25] -->
m

<!-- b002159 | references | pages [25] -->
m

<!-- b002160 | references | pages [25] -->
m

<!-- b002161 | references | pages [25] -->
m

<!-- b002162 | references | pages [25] -->
m

<!-- b002163 | references | pages [25] -->
m

<!-- b002164 | references | pages [25] -->
m

<!-- b002165 | references | pages [25] -->
m

<!-- b002166 | references | pages [25] -->
m

<!-- b002167 | references | pages [25] -->
m

<!-- b002168 | references | pages [25] -->
m

<!-- b002169 | references | pages [25] -->
m

<!-- b002170 | references | pages [25] -->
m

<!-- b002171 | references | pages [25] -->
m

<!-- b002172 | references | pages [25] -->
m

<!-- b002173 | references | pages [25] -->
m

<!-- b002174 | references | pages [25] -->
m

<!-- b002175 | references | pages [25] -->
m

<!-- b002176 | references | pages [25] -->
m

<!-- b002177 | references | pages [25] -->
m

<!-- b002178 | references | pages [25] -->
m

<!-- b002179 | references | pages [25] -->
m

<!-- b002180 | references | pages [25] -->
m

<!-- b002181 | references | pages [25] -->
m

<!-- b002182 | references | pages [25] -->
m

<!-- b002183 | references | pages [25] -->
m

<!-- b002184 | references | pages [25] -->
m

<!-- b002185 | references | pages [25] -->
m

<!-- b002186 | references | pages [25] -->
m

<!-- b002187 | references | pages [25] -->
m

<!-- b002188 | references | pages [25] -->
m

<!-- b002189 | references | pages [25] -->
m

<!-- b002190 | references | pages [25] -->
m

<!-- b002191 | references | pages [25] -->
m

<!-- b002192 | references | pages [25] -->
m

<!-- b002193 | references | pages [25] -->
m

<!-- b002194 | references | pages [25] -->
m

<!-- b002195 | references | pages [25] -->
m

<!-- b002196 | references | pages [25] -->
m

<!-- b002197 | references | pages [25] -->
m

<!-- b002198 | references | pages [25] -->
m

<!-- b002199 | references | pages [25] -->
m

<!-- b002200 | references | pages [25] -->
m

<!-- b002201 | references | pages [25] -->
m

<!-- b002202 | references | pages [25] -->
m

<!-- b002203 | references | pages [25] -->
m

<!-- b002204 | references | pages [25] -->
m

<!-- b002205 | references | pages [25] -->
m

<!-- b002206 | references | pages [25] -->
m

<!-- b002207 | references | pages [25] -->
m

<!-- b002208 | references | pages [25] -->
m

<!-- b002209 | references | pages [25] -->
m

<!-- b002210 | references | pages [25] -->
m

<!-- b002211 | references | pages [25] -->
m

<!-- b002212 | references | pages [25] -->
m

<!-- b002213 | references | pages [25] -->
m

<!-- b002214 | references | pages [25] -->
m

<!-- b002215 | references | pages [25] -->
m

<!-- b002216 | references | pages [25] -->
m

<!-- b002217 | references | pages [25] -->
m

<!-- b002218 | references | pages [25] -->
m

<!-- b002219 | references | pages [25] -->
m

<!-- b002220 | references | pages [25] -->
m

<!-- b002221 | references | pages [25] -->
m

<!-- b002222 | references | pages [25] -->
m

<!-- b002223 | references | pages [25] -->
m

<!-- b002224 | references | pages [25] -->
m

<!-- b002225 | references | pages [25] -->
m

<!-- b002226 | references | pages [25] -->
m

<!-- b002227 | references | pages [25] -->
m

<!-- b002228 | references | pages [25] -->
m

<!-- b002229 | references | pages [25] -->
m

<!-- b002230 | references | pages [25] -->
m

<!-- b002231 | references | pages [25] -->
m

<!-- b002232 | references | pages [25] -->
m

<!-- b002233 | references | pages [25] -->
m

<!-- b002234 | references | pages [25] -->
m

<!-- b002235 | references | pages [25] -->
m

<!-- b002236 | references | pages [25] -->
m

<!-- b002237 | references | pages [25] -->
m

<!-- b002238 | references | pages [25] -->
m

<!-- b002239 | references | pages [25] -->
m

<!-- b002240 | references | pages [25] -->
m

<!-- b002241 | references | pages [25] -->
m

<!-- b002242 | references | pages [25] -->
m

<!-- b002243 | references | pages [25] -->
m

<!-- b002244 | references | pages [25] -->
m

<!-- b002245 | references | pages [25] -->
m

<!-- b002246 | references | pages [25] -->
m

<!-- b002247 | references | pages [25] -->
m

<!-- b002248 | references | pages [25] -->
m

<!-- b002249 | references | pages [25] -->
m

<!-- b002250 | references | pages [25] -->
m

<!-- b002251 | references | pages [25] -->
m

<!-- b002252 | references | pages [25] -->
m

<!-- b002253 | references | pages [25] -->
m

<!-- b002254 | references | pages [25] -->
m

<!-- b002255 | references | pages [25] -->
m

<!-- b002256 | references | pages [25] -->
m

<!-- b002257 | references | pages [25] -->
m

<!-- b002258 | references | pages [25] -->
m

<!-- b002259 | references | pages [25] -->
m

<!-- b002260 | references | pages [25] -->
m

<!-- b002261 | references | pages [25] -->
m

<!-- b002262 | references | pages [25] -->
m

<!-- b002263 | references | pages [25] -->
m

<!-- b002264 | references | pages [25] -->
m

<!-- b002265 | references | pages [25] -->
m

<!-- b002266 | references | pages [25] -->
m

<!-- b002267 | references | pages [25] -->
m

<!-- b002268 | references | pages [25] -->
m

<!-- b002269 | references | pages [25] -->
m

<!-- b002270 | references | pages [25] -->
m

<!-- b002271 | references | pages [25] -->
m

<!-- b002272 | references | pages [25] -->
m

<!-- b002273 | references | pages [25] -->
m

<!-- b002274 | references | pages [25] -->
m

<!-- b002275 | references | pages [25] -->
m

<!-- b002276 | references | pages [25] -->
m

<!-- b002277 | references | pages [25] -->
m

<!-- b002278 | references | pages [25] -->
m

<!-- b002279 | references | pages [25] -->
m

<!-- b002280 | references | pages [25] -->
m

<!-- b002281 | references | pages [25] -->
m

<!-- b002282 | references | pages [25] -->
m

<!-- b002283 | references | pages [25] -->
m

<!-- b002284 | references | pages [25] -->
m

<!-- b002285 | references | pages [25] -->
m

<!-- b002286 | references | pages [25] -->
m

<!-- b002287 | references | pages [25] -->
m

<!-- b002288 | references | pages [25] -->
m

<!-- b002289 | references | pages [25] -->
m

<!-- b002290 | references | pages [25] -->
m

<!-- b002291 | references | pages [25] -->
m

<!-- b002292 | references | pages [25] -->
m

<!-- b002293 | references | pages [25] -->
m

<!-- b002294 | references | pages [25] -->
m

<!-- b002295 | references | pages [25] -->
m

<!-- b002296 | references | pages [25] -->
m

<!-- b002297 | references | pages [25] -->
m

<!-- b002298 | references | pages [25] -->
m

<!-- b002299 | references | pages [25] -->
m

<!-- b002300 | furniture | pages [25] -->
m

<!-- b002301 | furniture | pages [25] -->
m

<!-- b002302 | furniture | pages [25] -->
m

<!-- b002303 | furniture | pages [25] -->
m

<!-- b002304 | furniture | pages [25] -->
m

<!-- b002305 | furniture | pages [25] -->
m

<!-- b002306 | furniture | pages [25] -->
m

<!-- b002307 | furniture | pages [25] -->
m

<!-- b002308 | furniture | pages [25] -->
m

<!-- b002309 | furniture | pages [25] -->
m

<!-- b002310 | furniture | pages [25] -->
m

<!-- b002311 | furniture | pages [25] -->
m

<!-- b002312 | furniture | pages [25] -->
m

<!-- b002313 | furniture | pages [25] -->
m

<!-- b002314 | furniture | pages [25] -->
m

<!-- b002315 | furniture | pages [25] -->
m

<!-- b002316 | furniture | pages [25] -->
m

<!-- b002317 | furniture | pages [25] -->
m

<!-- b002318 | furniture | pages [25] -->
m

<!-- b002319 | furniture | pages [25] -->
m

<!-- b002320 | furniture | pages [25] -->
m

<!-- b002321 | furniture | pages [25] -->
m

<!-- b002322 | furniture | pages [25] -->
m

<!-- b002323 | furniture | pages [25] -->
m

<!-- b002324 | furniture | pages [25] -->
m

<!-- b002325 | furniture | pages [25] -->
m

<!-- b002326 | furniture | pages [25] -->
m

<!-- b002327 | furniture | pages [25] -->
m

<!-- b002328 | furniture | pages [25] -->
m

<!-- b002329 | furniture | pages [25] -->
m

<!-- b002330 | furniture | pages [25] -->
m

<!-- b002331 | furniture | pages [25] -->
m

<!-- b002332 | furniture | pages [25] -->
m

<!-- b002333 | furniture | pages [25] -->
m

<!-- b002334 | furniture | pages [25] -->
m

<!-- b002335 | furniture | pages [25] -->
m

<!-- b002336 | furniture | pages [25] -->
m

<!-- b002337 | furniture | pages [25] -->
m

<!-- b002338 | furniture | pages [25] -->
m

<!-- b002339 | furniture | pages [25] -->
m

<!-- b002340 | furniture | pages [25] -->
m

<!-- b002341 | furniture | pages [25] -->
m

<!-- b002342 | furniture | pages [25] -->
m

<!-- b002343 | furniture | pages [25] -->
m

<!-- b002344 | furniture | pages [25] -->
m

<!-- b002345 | furniture | pages [25] -->
m

<!-- b002346 | furniture | pages [25] -->
m

<!-- b002347 | furniture | pages [25] -->
m

<!-- b002348 | furniture | pages [25] -->
m

<!-- b002349 | furniture | pages [25] -->
m

<!-- b002350 | furniture | pages [25] -->
m

<!-- b002351 | furniture | pages [25] -->
m

<!-- b002352 | furniture | pages [25] -->
m

<!-- b002353 | furniture | pages [25] -->
m

<!-- b002354 | furniture | pages [25] -->
m

<!-- b002355 | furniture | pages [25] -->
m

<!-- b002356 | furniture | pages [25] -->
m

<!-- b002357 | furniture | pages [25] -->
m

<!-- b002358 | furniture | pages [25] -->
m

<!-- b002359 | furniture | pages [25] -->
m

<!-- b002360 | furniture | pages [25] -->
m

<!-- b002361 | furniture | pages [25] -->
m

<!-- b002362 | furniture | pages [25] -->
m

<!-- b002363 | furniture | pages [25] -->
m

<!-- b002364 | furniture | pages [25] -->
m

<!-- b002365 | furniture | pages [25] -->
m

<!-- b002366 | furniture | pages [25] -->
m

<!-- b002367 | furniture | pages [25] -->
m

<!-- b002368 | furniture | pages [25] -->
m

<!-- b002369 | furniture | pages [25] -->
m

<!-- b002370 | furniture | pages [25] -->
m

<!-- b002371 | furniture | pages [25] -->
m

<!-- b002372 | furniture | pages [25] -->
m

<!-- b002373 | furniture | pages [25] -->
m

<!-- b002374 | furniture | pages [25] -->
m

<!-- b002375 | furniture | pages [25] -->
m

<!-- b002376 | furniture | pages [25] -->
m

<!-- b002377 | furniture | pages [25] -->
m

<!-- b002378 | furniture | pages [25] -->
m

<!-- b002379 | furniture | pages [25] -->
m

<!-- b002380 | furniture | pages [25] -->
m

<!-- b002381 | furniture | pages [25] -->
m

<!-- b002382 | furniture | pages [25] -->
m

<!-- b002383 | furniture | pages [25] -->
m

<!-- b002384 | furniture | pages [25] -->
m

<!-- b002385 | furniture | pages [25] -->
m

<!-- b002386 | furniture | pages [25] -->
m

<!-- b002387 | furniture | pages [25] -->
m

<!-- b002388 | furniture | pages [25] -->
m

<!-- b002389 | furniture | pages [25] -->
m

<!-- b002390 | furniture | pages [25] -->
m

<!-- b002391 | furniture | pages [25] -->
m

<!-- b002392 | furniture | pages [25] -->
m

<!-- b002393 | furniture | pages [25] -->
m

<!-- b002394 | furniture | pages [25] -->
m

<!-- b002395 | furniture | pages [25] -->
m

<!-- b002396 | furniture | pages [25] -->
m

<!-- b002397 | furniture | pages [25] -->
m

<!-- b002398 | furniture | pages [25] -->
m

<!-- b002399 | furniture | pages [25] -->
m

<!-- b002400 | furniture | pages [25] -->
m

<!-- b002401 | furniture | pages [25] -->
m

<!-- b002402 | furniture | pages [25] -->
m

<!-- b002403 | furniture | pages [25] -->
m

<!-- b002404 | furniture | pages [25] -->
m

<!-- b002405 | furniture | pages [25] -->
m

<!-- b002406 | furniture | pages [25] -->
m

<!-- b002407 | furniture | pages [25] -->
m

<!-- b002408 | furniture | pages [25] -->
m

<!-- b002409 | furniture | pages [25] -->
m

<!-- b002410 | furniture | pages [25] -->
m

<!-- b002411 | furniture | pages [25] -->
m

<!-- b002412 | furniture | pages [25] -->
m

<!-- b002413 | furniture | pages [25] -->
m

<!-- b002414 | furniture | pages [25] -->
m

<!-- b002415 | furniture | pages [25] -->
m

<!-- b002416 | furniture | pages [25] -->
m

<!-- b002417 | furniture | pages [25] -->
m

<!-- b002418 | furniture | pages [25] -->
m

<!-- b002419 | furniture | pages [25] -->
m

<!-- b002420 | furniture | pages [25] -->
m

<!-- b002421 | furniture | pages [25] -->
m

<!-- b002422 | furniture | pages [25] -->
m

<!-- b002423 | furniture | pages [25] -->
m

<!-- b002424 | furniture | pages [25] -->
m

<!-- b002425 | furniture | pages [25] -->
m

<!-- b002426 | furniture | pages [25] -->
m

<!-- b002427 | furniture | pages [25] -->
m

<!-- b002428 | furniture | pages [25] -->
m

<!-- b002429 | furniture | pages [25] -->
m

<!-- b002430 | furniture | pages [25] -->
m

<!-- b002431 | furniture | pages [25] -->
m

<!-- b002432 | furniture | pages [25] -->
m

<!-- b002433 | furniture | pages [25] -->
m

<!-- b002434 | furniture | pages [25] -->
m

<!-- b002435 | furniture | pages [25] -->
m

<!-- b002436 | furniture | pages [25] -->
m

<!-- b002437 | furniture | pages [25] -->
m

<!-- b002438 | furniture | pages [25] -->
m

<!-- b002439 | furniture | pages [25] -->
m

<!-- b002440 | furniture | pages [25] -->
m

<!-- b002441 | furniture | pages [25] -->
m

<!-- b002442 | furniture | pages [25] -->
m

<!-- b002443 | furniture | pages [25] -->
m

<!-- b002444 | furniture | pages [25] -->
m

<!-- b002445 | furniture | pages [25] -->
m

<!-- b002446 | furniture | pages [25] -->
m

<!-- b002447 | furniture | pages [25] -->
m

<!-- b002448 | furniture | pages [25] -->
m

<!-- b002449 | furniture | pages [25] -->
m

<!-- b002450 | furniture | pages [25] -->
m

<!-- b002451 | furniture | pages [25] -->
m

<!-- b002452 | furniture | pages [25] -->
m

<!-- b002453 | furniture | pages [25] -->
m

<!-- b002454 | furniture | pages [25] -->
m

<!-- b002455 | furniture | pages [25] -->
m

<!-- b002456 | furniture | pages [25] -->
m

<!-- b002457 | furniture | pages [25] -->
m

<!-- b002458 | furniture | pages [25] -->
m

<!-- b002459 | furniture | pages [25] -->
m

<!-- b002460 | furniture | pages [25] -->
m

<!-- b002461 | furniture | pages [25] -->
m

<!-- b002462 | furniture | pages [25] -->
m

<!-- b002463 | furniture | pages [25] -->
m

<!-- b002464 | furniture | pages [25] -->
m

<!-- b002465 | furniture | pages [25] -->
m

<!-- b002466 | furniture | pages [25] -->
m

<!-- b002467 | furniture | pages [25] -->
m

<!-- b002468 | furniture | pages [25] -->
m

<!-- b002469 | furniture | pages [25] -->
m

<!-- b002470 | furniture | pages [25] -->
m

<!-- b002471 | furniture | pages [25] -->
m

<!-- b002472 | furniture | pages [25] -->
m

<!-- b002473 | furniture | pages [25] -->
m

<!-- b002474 | furniture | pages [25] -->
m

<!-- b002475 | furniture | pages [25] -->
m

<!-- b002476 | furniture | pages [25] -->
m

<!-- b002477 | furniture | pages [25] -->
m

<!-- b002478 | furniture | pages [25] -->
m

<!-- b002479 | furniture | pages [25] -->
m

<!-- b002480 | furniture | pages [25] -->
m

<!-- b002481 | furniture | pages [25] -->
m

<!-- b002482 | furniture | pages [25] -->
m

<!-- b002483 | furniture | pages [25] -->
m

<!-- b002484 | furniture | pages [25] -->
m

<!-- b002485 | furniture | pages [25] -->
m

<!-- b002486 | furniture | pages [25] -->
m

<!-- b002487 | furniture | pages [25] -->
m

<!-- b002488 | furniture | pages [25] -->
m

<!-- b002489 | furniture | pages [25] -->
m

<!-- b002490 | furniture | pages [25] -->
m

<!-- b002491 | furniture | pages [25] -->
m

<!-- b002492 | furniture | pages [25] -->
m

<!-- b002493 | furniture | pages [25] -->
m

<!-- b002494 | furniture | pages [25] -->
m

<!-- b002495 | furniture | pages [25] -->
m

<!-- b002496 | furniture | pages [25] -->
m

<!-- b002497 | furniture | pages [25] -->
m

<!-- b002498 | furniture | pages [25] -->
m

<!-- b002499 | furniture | pages [25] -->
m

<!-- b002500 | furniture | pages [25] -->
m

<!-- b002501 | furniture | pages [25] -->
m

<!-- b002502 | furniture | pages [25] -->
m

<!-- b002503 | furniture | pages [25] -->
m

<!-- b002504 | furniture | pages [25] -->
m

<!-- b002505 | furniture | pages [25] -->
m

<!-- b002506 | furniture | pages [25] -->
m

<!-- b002507 | furniture | pages [25] -->
m

<!-- b002508 | furniture | pages [25] -->
m

<!-- b002509 | furniture | pages [25] -->
m

<!-- b002510 | furniture | pages [25] -->
m

<!-- b002511 | furniture | pages [25] -->
m

<!-- b002512 | furniture | pages [25] -->
m

<!-- b002513 | furniture | pages [25] -->
m

<!-- b002514 | furniture | pages [25] -->
m

<!-- b002515 | furniture | pages [25] -->
m

<!-- b002516 | furniture | pages [25] -->
m

<!-- b002517 | furniture | pages [25] -->
m

<!-- b002518 | furniture | pages [25] -->
m

<!-- b002519 | furniture | pages [25] -->
m

<!-- b002520 | furniture | pages [25] -->
m

<!-- b002521 | furniture | pages [25] -->
m

<!-- b002522 | furniture | pages [25] -->
m

<!-- b002523 | furniture | pages [25] -->
m

<!-- b002524 | furniture | pages [25] -->
m

<!-- b002525 | furniture | pages [25] -->
m

<!-- b002526 | furniture | pages [25] -->
m

<!-- b002527 | furniture | pages [25] -->
m

<!-- b002528 | furniture | pages [25] -->
m

<!-- b002529 | furniture | pages [25] -->
m

<!-- b002530 | furniture | pages [25] -->
m

<!-- b002531 | furniture | pages [25] -->
m

<!-- b002532 | furniture | pages [25] -->
m

<!-- b002533 | furniture | pages [25] -->
m

<!-- b002534 | furniture | pages [25] -->
m

<!-- b002535 | furniture | pages [25] -->
m

<!-- b002536 | furniture | pages [25] -->
m

<!-- b002537 | furniture | pages [25] -->
m

<!-- b002538 | furniture | pages [25] -->
m

<!-- b002539 | furniture | pages [25] -->
m

<!-- b002540 | furniture | pages [25] -->
m

<!-- b002541 | furniture | pages [25] -->
m

<!-- b002542 | furniture | pages [25] -->
m

<!-- b002543 | furniture | pages [25] -->
m

<!-- b002544 | furniture | pages [25] -->
m

<!-- b002545 | furniture | pages [25] -->
m

<!-- b002546 | furniture | pages [25] -->
m

<!-- b002547 | furniture | pages [25] -->
m

<!-- b002548 | furniture | pages [25] -->
m

<!-- b002549 | furniture | pages [25] -->
m

<!-- b002550 | furniture | pages [25] -->
m

<!-- b002551 | furniture | pages [25] -->
m

<!-- b002552 | furniture | pages [25] -->
m

<!-- b002553 | furniture | pages [25] -->
m

<!-- b002554 | furniture | pages [25] -->
m

<!-- b002555 | furniture | pages [25] -->
m

<!-- b002556 | furniture | pages [25] -->
m

<!-- b002557 | furniture | pages [25] -->
m

<!-- b002558 | furniture | pages [25] -->
m

<!-- b002559 | furniture | pages [25] -->
m

<!-- b002560 | furniture | pages [25] -->
m

<!-- b002561 | furniture | pages [25] -->
m

<!-- b002562 | furniture | pages [25] -->
m

<!-- b002563 | furniture | pages [25] -->
m

<!-- b002564 | furniture | pages [25] -->
m

<!-- b002565 | furniture | pages [25] -->
m

<!-- b002566 | furniture | pages [25] -->
m

<!-- b002567 | furniture | pages [25] -->
m

<!-- b002568 | furniture | pages [25] -->
m

<!-- b002569 | furniture | pages [25] -->
m

<!-- b002570 | furniture | pages [25] -->
m

<!-- b002571 | furniture | pages [25] -->
m

<!-- b002572 | furniture | pages [25] -->
m

<!-- b002573 | furniture | pages [25] -->
m

<!-- b002574 | furniture | pages [25] -->
m

<!-- b002575 | furniture | pages [25] -->
m

<!-- b002576 | furniture | pages [25] -->
m

<!-- b002577 | furniture | pages [25] -->
m

<!-- b002578 | furniture | pages [25] -->
m

<!-- b002579 | furniture | pages [25] -->
m

<!-- b002580 | furniture | pages [25] -->
m

<!-- b002581 | furniture | pages [25] -->
m

<!-- b002582 | furniture | pages [25] -->
m

<!-- b002583 | furniture | pages [25] -->
m

<!-- b002584 | furniture | pages [25] -->
m

<!-- b002585 | furniture | pages [25] -->
m

<!-- b002586 | furniture | pages [25] -->
m

<!-- b002587 | furniture | pages [25] -->
m

<!-- b002588 | furniture | pages [25] -->
m

<!-- b002589 | furniture | pages [25] -->
m

<!-- b002590 | furniture | pages [25] -->
m

<!-- b002591 | furniture | pages [25] -->
m

<!-- b002592 | furniture | pages [25] -->
m

<!-- b002593 | furniture | pages [25] -->
m

<!-- b002594 | furniture | pages [25] -->
m

<!-- b002595 | furniture | pages [25] -->
m

<!-- b002596 | furniture | pages [25] -->
m

<!-- b002597 | furniture | pages [25] -->
m

<!-- b002598 | furniture | pages [25] -->
m

<!-- b002599 | furniture | pages [25] -->
m

<!-- b002600 | furniture | pages [25] -->
m

<!-- b002601 | furniture | pages [25] -->
m

<!-- b002602 | furniture | pages [25] -->
m

<!-- b002603 | furniture | pages [25] -->
m

<!-- b002604 | furniture | pages [25] -->
m

<!-- b002605 | furniture | pages [25] -->
m

<!-- b002606 | furniture | pages [25] -->
m

<!-- b002607 | furniture | pages [25] -->
m

<!-- b002608 | furniture | pages [25] -->
m

<!-- b002609 | furniture | pages [25] -->
m

<!-- b002610 | furniture | pages [25] -->
m

<!-- b002611 | furniture | pages [25] -->
m

<!-- b002612 | furniture | pages [25] -->
m

<!-- b002613 | furniture | pages [25] -->
m

<!-- b002614 | furniture | pages [25] -->
m

<!-- b002615 | furniture | pages [25] -->
m

<!-- b002616 | furniture | pages [25] -->
m

<!-- b002617 | furniture | pages [25] -->
m

<!-- b002618 | furniture | pages [25] -->
m

<!-- b002619 | furniture | pages [25] -->
m

<!-- b002620 | furniture | pages [25] -->
m

<!-- b002621 | furniture | pages [25] -->
m

<!-- b002622 | furniture | pages [25] -->
m

<!-- b002623 | furniture | pages [25] -->
m
