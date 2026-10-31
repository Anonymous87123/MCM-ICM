# P-C-2025-2515235-923bb0bb

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
2515235

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
From Models to Medals: The Winning Formula Behind the Data

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Since the inception of the first Olympic Games in history, discussions on predicting the Olympic medal tally have been ongoing. Against this backdrop, we develops an appropriate regression model to predict the medal standings for the 2028 Los Angeles Olympic Games and explores the impact of the "Great Coach Effect" on the performance of countries in Olympic

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
events.

<!-- b000013 | prose | pages [1] -->
Firstly, based on the rich data provided in the study, we conducted data preprocessing, including addressing anomalies caused by historical factors and developing models such as SARIMAX and ARIMA to predict future trends in the number of events. Secondly, to handle truncated data, such as countries with "0 medals," this study constructed the TMH-OMP model, which combines the Mundlak-modified Tobit regression model with the Hurdle model. The model achieved a prediction accuracy of 79.3% for countries winning more than 10 medals annually, and 77.8% for countries winning fewer than 10 medals annually. Addi- tionally, we predict that Andorra and the Maldives will win their first-ever Olympic medals, with probabilities of 0.39 and 0.32, respectively. An analysis of event types and project quantity

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
(participation rate) reveals a Pearson correlation coefficient of 0.416.

<!-- b000016 | prose | pages [1] -->
In order to analyze the "Great Coach" effect, we constructed a logistic regression model for fitting, and incorporated the Event-study method into the conventional Difference-in-Dif- ferences (DID) approach to design a dynamic DID method capable of effectively estimating the effect across multiple treatment groups. To mitigate the bias due to covariate differences, we included the Inverse Probability Weighting (IPW) method for estimating treatment effects, and applied the Double Robust Estimator (DR) framework to develop the DRD-CE model. Performance analysis of this model showed an R-squared value of 0.756, indicating good fit, and a "Great Coach" regression coefficient of 3.1084, highlighting the substantial impact of the "Great Coach" effect on specific countries and projects. Furthermore, we identified signif- icant effects in countries such as the United States in Women's Sabre Fencing, Japan in Women's Gymnastics, Germany in Women's Sabre Fencing, and Field Hockey.

<!-- b000017 | prose | pages [1] -->
Subsequently, we observed that changes in the number of smaller events within major categories had a significant impact on the medal outcomes of some smaller countries. Ap- proximately 104 nations are highly dependent on the variety of sports events to secure gold medals. Based on these findings, we proposed to the National Olympic Committees the pro- tection and expansion of their advantageous sports events.

<!-- b000018 | prose | pages [1] -->
Finally, we assessed and expanded the model's strengths and limitations, as well as ana- lyzed its sensitivity. By conducting error analysis between the total medal count derived from the sum of gold, silver, and bronze medals and the total medal count directly input into the model, we obtained an average error of 8.0783%. This result indicates that our model demonstrates high sensitivity.

<!-- b000019 | keywords | pages [1] -->
Keywords: Olympic Games; Tobit regression; Hurdle model; Great coach effect; Doubly ro-

<!-- b000020 | prose | pages [1] -->
bust estimator; Host country effect

<!-- b000021 | furniture | pages [2] -->
Page 2 of 26

<!-- b000022 | furniture | pages [2] -->
Team # 2515235

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
1 Introduction

<!-- b000025 | contents | pages [2] -->
1.1 Problem Background

<!-- b000026 | contents | pages [2] -->
3

<!-- b000027 | heading | pages [2] -->
1.2 Restatement of the Problem.

<!-- b000028 | prose | pages [2] -->
1.3 Our Work. 4

<!-- b000029 | heading | pages [2] -->
2 Assumptions and Justifications.

<!-- b000030 | prose | pages [2] -->
3Notations

<!-- b000031 | heading | pages [2] -->
4 Data processing.

<!-- b000032 | prose | pages [2] -->
5

<!-- b000033 | prose | pages [2] -->
5 Model 1: Predict Olympic medal counts by TMP-OMP Model... 6

<!-- b000034 | heading | pages [2] -->
5.1 Explanation of the Dynamic Country Characteristies and Constant Country Properties 6

<!-- b000035 | prose | pages [2] -->
5.1.1 Dynamic country characteristics .6 .8

<!-- b000036 | heading | pages [2] -->
5.1.2 Constant country characteristics..

<!-- b000037 | prose | pages [2] -->
.

<!-- b000038 | prose | pages [2] -->
●

<!-- b000039 | caption | pages [2] -->
Table 2: Summary of Constant country characteristics

<!-- b000040 | prose | pages [2] -->
.8

<!-- b000041 | heading | pages [2] -->
5.2 The Establishment of Model 1.

<!-- b000042 | prose | pages [2] -->
.9

<!-- b000043 | heading | pages [2] -->
5.3 The Solution of Problem 1 by Model 1.

<!-- b000044 | prose | pages [2] -->
11

<!-- b000045 | heading | pages [2] -->
5.3.1 Predicting the 2028 Medal Table

<!-- b000046 | prose | pages [2] -->
11

<!-- b000047 | caption | pages [2] -->
Table 3: Predictive results and accuracy of the two models respectively

<!-- b000048 | prose | pages [2] -->
.12

<!-- b000049 | heading | pages [2] -->
6 Model 2: Analysis “great coach" effect by DRD-CE Model..

<!-- b000050 | prose | pages [2] -->
16

<!-- b000051 | heading | pages [2] -->
6.1 The Establishment of Model 2.

<!-- b000052 | prose | pages [2] -->
.16

<!-- b000053 | heading | pages [2] -->
6.2 The Solution of Problem 2 by Model 2.

<!-- b000054 | prose | pages [2] -->
.18

<!-- b000055 | heading | pages [2] -->
6.2.1 Illustrate the impact of the great coaching effect .

<!-- b000056 | prose | pages [2] -->
.18 6.2.2: Selection of three countries and projects, analysis and results. .19 .20 6.2.3: Prediction of the Performance After Hiring a "Great Coach" ● .21

<!-- b000057 | heading | pages [2] -->
7 The Solution of Problem 3.

<!-- b000058 | prose | pages [2] -->
.21

<!-- b000059 | heading | pages [2] -->
7.1 Former host effect and Subsequent host effect.

<!-- b000060 | prose | pages [2] -->
.22 7.2 Strategies to Enhance Olympic Participation and Global Influence.. 8 Sensitivity Analys... .23 24

<!-- b000061 | heading | pages [2] -->
9 Model Evaluation and Further Discussion

<!-- b000062 | heading | pages [2] -->
9.1 Strengths

<!-- b000063 | prose | pages [2] -->
.24

<!-- b000064 | heading | pages [2] -->
9.2 Weaknesses and Further Discussion

<!-- b000065 | prose | pages [2] -->
.25

<!-- b000066 | prose | pages [2] -->
25

<!-- b000067 | heading | pages [2] -->
10 References

<!-- b000068 | references | pages [2] -->
关注数学模型

<!-- b000069 | furniture | pages [2] -->
获取更多资讯

<!-- b000070 | furniture | pages [3] -->
Team # 2515235

<!-- b000071 | furniture | pages [3] -->
Page 3 of 26

<!-- b000072 | heading | pages [3] -->
1 Introduction

<!-- b000073 | heading | pages [3] -->
1.1 Problem Background

<!-- b000074 | prose | pages [3] -->
The Olympic Games have long captured global attention with their diverse events and elite athletes. Each medal reflects not only an athlete's achievement but also the spirit of their country. As a result, predicting Olympic medal standings has become a focus of interest.

<!-- b000075 | prose | pages [3] -->
Time series forecasting, a common prediction method, uses historical medal counts to identify trends [1]. However, this approach is limited as it only considers past data and cannot adapt to sudden changes or uncertainties. The empirical model, which relies on real-world data and statistical analysis, also faces challenges, such as focusing mainly on population and GDP, while neglecting other key variables and time-independent factors like sports culture [2].

<!-- b000076 | prose | pages [3] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000077 | caption | pages [3] -->
Figure 1: Tom Cruise declares see you in LA for 2028 Olympics

<!-- b000078 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000079 | prose | pages [3] -->
Based on the background information and restrictions related to the Olympic Games men- tioned in the problem statement, we need to address the following issues:

<!-- b000080 | heading | pages [3] -->
Problem 1: Medal Prediction Model

<!-- b000081 | prose | pages [3] -->
Develop a model to predict the gold, silver, bronze, and total medal counts for each coun- try. Evaluate the model's performance using relevant metrics.

<!-- b000082 | prose | pages [3] -->
2028 LA Olympics Prediction: Forecast medal rankings, identify countries with improved or declined performance compared to 2024, and predict potential first-time medalists.

<!-- b000083 | prose | pages [3] -->
Event-Medal Relationship: Analyze how the number and types of events influence medal distribution, considering the host country's event choices and their impact on medals.

<!-- b000084 | prose | pages [3] -->
Problem 2: Great Coach Effect Analysis Evaluate the impact of the "great coach effect" on medal distribution and estimate its con- tribution to the total medal count.

<!-- b000085 | prose | pages [3] -->
Coach Selection: Identify three countries and recommend which sports they should focus on to hire a "great coach," predicting the potential impact. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

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

<!-- b000410 | furniture | pages [4] -->
Team # 2515235

<!-- b000411 | furniture | pages [4] -->
Page 4 of 26

<!-- b000412 | heading | pages [4] -->
Problem 3: Insights from the Model

<!-- b000413 | prose | pages [4] -->
Present unique insights on medal distribution, highlighting practical recommendations for national Olympic committees.

<!-- b000414 | heading | pages [4] -->
1.3 Our Work

<!-- b000415 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000416 | caption | pages [4] -->
Figure 2: The overview of Our Work.

<!-- b000417 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000418 | prose | pages [4] -->
Assumption 1: This paper assumes that all athletes active after 2020 are at the peak of their athletic performance and will compete in subsequent Olympic Games. Additionally, their performance will be predicted solely based on their medal-winning capabilities.

<!-- b000419 | prose | pages [4, 5] -->
关注数学模型 Assumption 2: This paper assumes that the number of events in the 2028 and 2032 Olym- pic Games will be determined solely by the host country effect and international trends, without being influenced by other external factors or unforeseen circumstances.

<!-- b000420 | furniture | pages [4] -->
2

<!-- b000421 | furniture | pages [4] -->
MATHmodels

<!-- b000422 | furniture | pages [4] -->
获取更多资讯

<!-- b000423 | furniture | pages [5] -->
Page 5 of 26

<!-- b000424 | furniture | pages [5] -->
Team # 2515235

<!-- b000426 | prose | pages [5] -->
Assumption 3: It is assumed that the achievements of countries undergoing regime changes or other special organizations (such as those competing on behalf of two countries or as independent entities) are reasonably incorporated into the current legitimate countries, based on historical and geographical factors.

<!-- b000427 | heading | pages [5] -->
3 Notations

<!-- b000428 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000429 | prose | pages [5] -->
Description

<!-- b000430 | heading | pages [5] -->
Symbol

<!-- b000431 | prose | pages [5] -->
HEi,t Host effect ERi,t Event participation rate APi,t Athletic performance ERi Average Event participation rate NM Normalized Medal Average NAi,t Total country participants Mi,t Number of potential medals (untruncated values) ATH Mi,t Number of medals actually observed

<!-- b000432 | prose | pages [5] -->
First, we addressed outliers in the dataset, such as formatting errors and missing data, and took into account the impact of special events on the data, such as the cancellation of the Olympics during World War II, justifying the retention of missing values in those years.

<!-- b000433 | prose | pages [5] -->
We then reviewed the historical context of the Olympics, assessing past events, and con- cluded that they had minimal impact on the overall predictive task. Therefore, we disregarded these effects and proceeded with normal data handling.

<!-- b000434 | prose | pages [5] -->
Considering global circumstances and political changes, we consolidated the data of the former Soviet Union into Russia and merged East and West Germany into a unified Germany, retaining the results. For countries that emerged after the dissolution of the Soviet Union (e.g., Lithuania, Kazakhstan), we used their respective results.

<!-- b000435 | prose | pages [5] -->
we provided additional notes on data processing and usage: we combined the results of a country's first and second teams; due to the suspension of Russia and Belarus and the missing data, we did not forecast the medal counts for these two countries; data from mixed teams were excluded from medal predictions; dual-nationality athletes' medals were counted for both countries; and following Assumption 2, we removed data for athletes who competed be- fore 2020 and created a separate new dataset for future use.

<!-- b000436 | furniture | pages [6] -->
Team # 2515235

<!-- b000437 | furniture | pages [6] -->
Page 6 of 26

<!-- b000438 | prose | pages [6] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000439 | caption | pages [6] -->
Figure 3. Data processing steps

<!-- b000440 | prose | pages [6] -->
Finally, for the other datasets, after encoding the variables, we used the median to fill in outliers and missing values, ensuring the completeness and accuracy of the data. Through these steps, we ensured the data's standardization and consistency, laying a solid foundation for subsequent analysis and modeling.

<!-- b000441 | heading | pages [6] -->
5 Model 1: Predict Olympic medal counts by TMP-OMP Model.

<!-- b000442 | heading | pages [6] -->
5.1 Explanation of the Dynamic Country Characteristics and Constant

<!-- b000443 | prose | pages [6] -->
Country Properties

<!-- b000444 | heading | pages [6] -->
5.1.1 Dynamic country characteristics

<!-- b000445 | prose | pages [6] -->
In the context of the Olympic Games, dynamic country characteristics refer to factors that have a significant impact in the short term and change over time. For example, the host country effect (𝑯𝑬), the proportion of events participated in by each country (𝑵𝑬) and athletes’ per- formance in recent Olympic Games ( 𝑨𝑷 𝒊), Number of athlete participants (𝐍𝐀𝐢,𝐭) and so on.

<!-- b000446 | prose | pages [6, 7] -->
关注数学模型 To construct dynamic national characteristics, we first need to predict the types and quan- tities of future projects for 2028 and 2032. As shown in the figure, considering that the number of future projects is closely related to historical quantities, and project types are often related 微信公众号：数学模型 to the host country, we can divide them into: host country's advantageous projects, disadvanta- geous projects, and neutral projects. For advantageous and disadvantageous projects, we con- sider that the host country effect may lead to an increase in advantageous projects and a de- crease in disadvantageous projects, so we choose the SARIMAX model, which takes into ac- count exogenous variables. Neutral projects are often not affected by the host country effect, so the ARIMA model is used for prediction. In addition, we have used the same method to analyze the host country of 2032, Australia. Where the pie chart in the flowchart shows the percentage of advantaged items in orange, the percentage of neutral items in purple and the percentage of disadvantaged items in blue.

<!-- b000447 | furniture | pages [6] -->
2

<!-- b000448 | furniture | pages [6] -->
MATHmodels

<!-- b000449 | furniture | pages [6] -->
获取更多资讯

<!-- b000450 | furniture | pages [7] -->
Team # 2515235

<!-- b000451 | furniture | pages [7] -->
Page 7 of 26

<!-- b000453 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000454 | caption | pages [7] -->
Figure 4. Data processing steps

<!-- b000455 | prose | pages [7] -->
These characteristics reflect a country's variations across different Olympic cycles and the temporary performance of its athletes, significantly influencing the prediction of medal counts. Therefore, in the modeling process, we selected 𝑯𝑬𝒊,𝒕 , 𝑬𝑹𝒊,𝒕 and  𝑨𝑷 𝒊,𝒕 as the three dy- namic country characteristics to more accurately capture the immediate impact of country traits on medal outcomes.

<!-- b000456 | furniture | pages [8] -->
Team # 2515235

<!-- b000457 | furniture | pages [8] -->
Page 8 of 26

<!-- b000458 | caption | pages [8] -->
Table 1: Summary of Dynamic country characteristics

<!-- b000459 | prose | pages [8] -->
Characteristic Equation range of values

<!-- b000460 | prose | pages [8] -->
Host effect (𝑯𝑬𝒊,𝒕) Based on whether the previous and next sessions 0, 1 were hosted

<!-- b000461 | prose | pages [8] -->
Event participation Annual projects participated by country i  /An- [0,1] rate (𝑬𝑹𝒊,𝒕) nual total projects×100%

<!-- b000462 | prose | pages [8] -->
Athletic perfor- Sum of ability scores in the last two editions. [-1,1] mance (𝑨𝑷𝒊,𝒕)

<!-- b000463 | prose | pages [8] -->
𝐍𝐀𝐢,𝐭 Total country participants

<!-- b000464 | caption | pages [8] -->
Table 2 outlines the formulas for calculating the three indicators. For 𝑯𝑬𝒊,𝒕, if a country

<!-- b000465 | prose | pages [8] -->
is the host for the predicted Olympic Games, the value is set to 1. For all other countries, the value is 0. The calculation for  𝑨𝑷 𝒊 defines Ability scores as follows: When the prediction task is for gold medals, gold = 3, silver = 2, bronze = 1, and no medal =0. When the prediction task is for silver medals, both gold and bronze = 1，and silver =2. When the prediction task is for bronze medals, gold= 1, silver = 2, and bronze = 3. The total score for all athletes from a country is summed and standardized to obtain the overall athlete performance for that country. It is important to note that, due to age limitations, only the performance from the previous two Olympic Games of each athlete is considered.

<!-- b000466 | heading | pages [8] -->
5.1.2 Constant country characteristics

<!-- b000467 | prose | pages [8] -->
In the context of the Olympic Games, constant country characteristics refer to factors that remain relatively stable over long periods and do not fluctuate over time. These include sports of countries traditions, long-term policy support, infrastructure development, and historical strengths in certain events. These factors have a lasting impact on a country’s overall Olympic performance, thus providing long-term guidance for predicting medal counts. In the modeling process, constant country characteristics help us better understand a country’s performance trends across multiple Olympic cycles, rather than just changes within a single cycle. Based on the information provided in the dataset, we selected the country’s long-term event participation rate  𝑵Ē 𝒕, Normalized Medal Average  𝑵𝑴̅̅̅̅̅𝒊, to measure the long-term impact of a country’s sports culture and policies.

<!-- b000468 | caption | pages [8] -->
Table 2: Summary of Constant country characteristics

<!-- b000469 | prose | pages [8] -->
Characteristic Equation Range of values

<!-- b000470 | prose | pages [8] -->
Average Event partici- The sum of 𝑬𝑹𝒊,𝒕/ Number of participants [0,1] pation rate ( 𝑬𝑹̅̅̅̅𝒊)

<!-- b000471 | prose | pages [8] -->
Normalized Medal Normalized average number of medals [0,1] won Average ( 𝑵𝑴̅̅̅̅̅𝒊)

<!-- b000472 | prose | pages [8, 9] -->
关注数学模型 The number of times a country participates in the Olympic Games not only reflects its level of engagement but also implies its long-term athletic strength. To quantify this,  𝑵𝑴̅̅̅̅̅𝒊 is calculated by dividing the total number of Olympics a country has participated in by the total number of Olympic Games since the first edition, thereby measuring the country’s sustained involvement in the Olympics throughout history.

<!-- b000473 | furniture | pages [8] -->
2

<!-- b000474 | furniture | pages [8] -->
MATHmodels

<!-- b000475 | furniture | pages [8] -->
获取更多资讯

<!-- b000476 | furniture | pages [9] -->
Team # 2515235

<!-- b000477 | furniture | pages [9] -->
Page 9 of 26

<!-- b000479 | heading | pages [9] -->
5.2 The Establishment of Model 1

<!-- b000480 | prose | pages [9] -->
微信公众号：数学模型 Inspired by the works of [3,4], we developed the Tobit-Mundlak- Hurdle Olympic

<!-- b000481 | heading | pages [9] -->
Medal Prediction Model (TMH-OMP) to provide accurate forecasts of Olympic medal

<!-- b000482 | prose | pages [9] -->
counts. In the dataset, we observed a large number of countries that have yet to win any med- als. To mitigate the impact of data from countries without medals on the predictions for coun- tries with medals, we employed the Tobit regression model to address the truncation issue in medal counts. Meanwhile, recognizing that a country's Olympic performance may be pro- foundly influenced by constant, country-specific factors, we incorporated the Mundlak cor- rection. By adding the time averages of country-specific variables, we capture these time-in- variant effects. Finally, to predict the country that will win a medal for the first time, and the 微信号：MATHmodels probability of winning a medal. Hurdle models for countries are constructed that have histor- ically won fewer than ten total medals.As shown in the figure 5.

<!-- b000483 | caption | pages [9] -->
Figure 5: The overview of TMP-OMP Model.

<!-- b000484 | prose | pages [9, 10] -->
Tobit Regression: When predicting Olympic medal counts, the medal count is a non- negative integer and can be zero (i.e., some countries may not win medals in certain events). This leads to truncation issues in traditional regression models. A simple linear regression model assumes the dependent variable is continuous and does not account for the possibility of zero values, leading to inaccurate predictions for countries with no medals. The Tobit re- gression model is specifically designed to handle data issues with truncated or censored de- pendent variables. In this case, the medal count is a truncated variable[3]. The Tobit model introduces latent variables to model the potential score for medal counts, assuming that the medal count can only be observed when the latent score is greater than zero. Based on dy- namic time characteristics such as the host country effect (𝑯𝑬𝒊,𝒕), the proportion of events each country participates in (𝑵𝑬𝒊,𝒕), and athlete performance in recent Olympic Games ( 𝑨𝑷 𝒊), we conduct an initial construction of the Tobit regression model.

<!-- b000485 | furniture | pages [10] -->
Team # 2515235

<!-- b000486 | furniture | pages [10] -->
Page 10 of 26

<!-- b000488 | prose | pages [10] -->
∗= 𝛂+ 𝛃𝟏𝐇𝐄𝐢,𝐭+ 𝛃𝟐𝐍𝐄𝐢,𝐭+ 𝛃𝟑 𝐀𝐏 𝐢,𝐭+ 𝛌𝐭+ 𝛜𝐢,𝐭 (1) 𝐌𝐢,𝐭

<!-- b000489 | prose | pages [10] -->
𝒊 represents different countries, and 𝒕 represents different years. 𝜶 is the constant term, and 𝜷𝟏, 𝜷𝟐, and 𝜷𝟑 are the model coefficients, corresponding to the host country ef- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m fect and the number of events, respectively. 𝝀𝒕 is the time fixed effect, which controls for m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m variations across different years. 𝝐𝒊,𝒕 is the error term. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ∗ ∗> 𝟎 m m m m m m m m m m m m m m 𝐌𝐢,𝐭= {𝐌𝐢,𝐭 𝐢𝐟 𝐌𝐢,𝐭 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (2) ∗≤𝟎 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝟎 𝐢𝐟 𝐌𝐢,𝐭

<!-- b000490 | prose | pages [10] -->
𝑴𝒊,𝒕 represents the actual observed medal count. It is used to estimate the probability of zero medals and accurately predict the number of non-zero medals.

<!-- b000491 | prose | pages [10] -->
Mundlak Correction: The Olympic performance of many countries may be influenced by constant, country-specific factors, such as hosting the Games multiple times, the long-term average performance of its athletes, and the country's sustained participation in certain events. Failing to account for these time-invariant factors could lead to estimation bias, par- ticularly when handling long-term country characteristics. The Mundlak correction is a technique used to address bias between fixed and random effects by introducing the mean of constant country-specific factors into the model. This allows the model to account for the im- pact of each constant country factor on medal counts. We combine the aforementioned con- stant country factors, long-term event participation rate ( 𝑬𝑹̅̅̅̅𝒊), and Normalized Medal Average ( 𝑵𝑴̅̅̅̅̅𝒊), with the Mundlak correction.

<!-- b000492 | prose | pages [10] -->
∗= 𝜶+ 𝜷𝟏𝑯𝑬𝒊,𝒕+ 𝜷𝟐𝑵𝑬𝒊,𝒕+ 𝜷𝟑 𝑨𝑷 𝒊,𝒕+ 𝒅𝟏 𝑬𝑹̅̅̅̅𝒊 + 𝒅𝟐 𝑵𝑴̅̅̅̅̅𝒊+ 𝝀𝒕+ 𝝐𝒊,𝒕 (3) 𝑴𝒊,𝒕

<!-- b000493 | prose | pages [10] -->
𝒅𝟏 and 𝒅𝟐 are the coefficients for the mean variables, representing the influence of long-term event participation rate and normalized medal average on medal counts, respec- tively. By introducing these time-invariant constant factors, the Mundlak correction effec- tively adjusts the model, providing more accurate medal predictions.

<!-- b000494 | prose | pages [10] -->
The Hurdle model typically consists of two stages: Step 1: Determining zero versus non-zero values: A binary choice model is used to predict whether an observation is zero. This stage focuses on whether the event occurs, i.e., whether the "hurdle" is crossed. Step 2: Quantifying non-zero values: For non-zero observations, an appropriate distribution is used to model the magnitude of these values. This part focuses on the quantity or degree of the obser- vation once the event has occurred. For the task of predicting first-time medalists, we devel- oped the following formula.

<!-- b000495 | prose | pages [10, 11] -->
关注数学模型 (4) P(Mi,t > 0) = φ(Xi,tΘ + ui + ∈i,t)

<!-- b000496 | furniture | pages [10] -->
2

<!-- b000497 | furniture | pages [10] -->
MATHmodels

<!-- b000498 | furniture | pages [10] -->
获取更多资讯

<!-- b000499 | furniture | pages [11] -->
Team # 2515235

<!-- b000500 | furniture | pages [11] -->
Page 11 of 26

<!-- b000502 | prose | pages [11] -->
To allow more countries that have never won a medal to cross the "hurdle", we predict that a country will win a medal in a given Olympics if P(Mi,t > 0) > 0.3. Φ is the cumu- lative distribution function (CDF) of the standard normal distribution, mapping the results of a linear combination to the [0, 1] interval, representing the probability that a country will win a medal. Xi,t is the matrix of explanatory variables for country i in year t. Θ is the regres- sion coefficient, representing the impact of each variable on the likelihood of winning a medal. ui is the country-specific effect, typically assumed to follow a normal distribution. €,t is the error term, usually assumed to be normally distributed. The definition of X,tΘ is as follows:

<!-- b000503 | prose | pages [11] -->
(5) exp (α + β1HEi,t + β2NEi,t + β3APi,t +t+ vNA,t + λt + ∈i,t)

<!-- b000504 | prose | pages [11] -->
Since the main goal of the Hurdle model is to predict first-time medal winners, we focus more on fitting countries that have won few medals in previous years, as this relationship is difficult to capture using linear models. Therefore, we employ Poisson regression. We also found that for countries with no medals, their athletes' performance APi,t is zero, and their participation rate NEi,t is extremely low. As a result, we introduce the number of participants each year NAi,t as a new variable. v is the coefficient for NAi,t.

<!-- b000505 | prose | pages [11] -->
In summary, the Mundlak-modified Tobit regression model helps mitigate the impact of non-medal-winning countries on predictions for medal-winning countries, while improving the accuracy of medal predictions for countries that haye won. The Hurdle model expands the study by identifying countries likely to win their first medal, accurately predicting those breaking the "zero medal" barrier. Although it slightly affects predictions for medal-winning countries, its main advantage lies in forecasting potential breakthroughs. Combining Tobit and Hurdle models allows for accurate predictions for both existing medal winners and emerging countries. Finally, Particle Swarm Optimization (PSO) is used to optimize pre- dictions for truncated data, commonly applied in economics and social sciences.

<!-- b000506 | prose | pages [11] -->
● ●

<!-- b000507 | heading | pages [11] -->
5.3 The Solution of Problem 1 by Model 1.

<!-- b000508 | prose | pages [11] -->
5.3.1 Predicting the 2028 Medal Table

<!-- b000509 | prose | pages [11] -->
Prior to the 2028 medal table, we used the existing data to predict the medal count for the 2024 Paris Olympics in order to evaluate the accuracy of our model. Due to the limitations of table space, and given that countries winning their first medals typically struggle to secure gold, we focus on analyzing and evaluating the total medal count for each country, rather than the specific breakdown of gold, silver, and bronze. It is worth noting that, for the athlete per- formance indicator (APi,t), all medals (gold, silver, and bronze) are assigned a score of 1 point.

<!-- b000510 | furniture | pages [12] -->
Page 12 of 26

<!-- b000511 | furniture | pages [12] -->
Team # 2515235

<!-- b000512 | caption | pages [12] -->
Table 3: Predictive results and accuracy of the two models respectively

<!-- b000513 | prose | pages [12] -->
Hurble Tobit Mundlak Actual Upper CI Upper CI Lower CI Forecast Lower CI Forecast number Countries 126 130 138 121 117 126 122 United States 91 94 90 97 90 87 83 China 63 65 66 72 62 59 67 Korea 57 69 64 62 58 61 65 France 50 47 53 57 50 59 54 Australia 43 41 45 46 53 46 51 Japan Italy 40 47 42 51 44 42 46 35 32 32 34 34 39 30 Netherlands 28 33 29 35 29 Germany 32 38 28 32 30 34 29 28 38 Great Britain Accuracy of Hurble Accuracy of Tobit Mundlak 72.9% 63.3% All countries (+ or -3) Countries with at least 79.3% 41.9% 10 medal (+ or -3) Countries with Less 62.9% 77.8% than 10 medal(+ or -1) 0% 37.5% First-time medalists

<!-- b000514 | prose | pages [12] -->
Overall Accuracy: The Tobit Mundlak model achieved an accuracy of 72.9% in pre- dicting medal counts within a margin of ±3 medals for all countries, outperforming the Hur- dle model's accuracy of 63.3%. This indicates that the Tobit Mundlak model provides more stable performance overall.

<!-- b000515 | prose | pages [12] -->
Countries with at least 10 medals: For countries winning at least 10 medals, the Tobit Mundlak model achieved an accuracy of 79.3%, significantly higher than the Hurdle model. This highlights the Tobit Mundlak model's predictive advantage for countries with medium to large medal counts. Countries with fewer than 10 medals: In countries with fewer than 10 medals, the Hurdle model's accuracy of 62.9% was higher than that of the Tobit Mundlak model. This suggests that the Hurdle model performs better for countries with smaller medal counts. Countries winning medals for the first time: For countries winning medals for the first time, the Tobit Mundlak model had an accuracy of 0%, whereas the Hurdle model achieved an accuracy of 37.5%. Of the eight countries predicted by the Hurdle model to win their first medals, three actually did. This indicates that the Hurdle model has some advantage in predicting first-time medal winners.

<!-- b000516 | prose | pages [12] -->
We combined the predictions from both the Tobit Mundlak and Hurdle models for countries with at least 10 medals and those with fewer than 10 medals. We predicted the gold, silver, and bronze medal counts separately, then summed the results to obtain the total medal count. The final rankings were determined according to the Olympic ranking rules.

<!-- b000517 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000518 | furniture | pages [12] -->
获取更多资讯

<!-- b000519 | furniture | pages [13] -->
Team # 2515235

<!-- b000520 | furniture | pages [13] -->
Page 13 of 26

<!-- b000522 | caption | pages [13] -->
Figure 6. 2024-2028 Medal table changes

<!-- b000523 | prose | pages [13] -->
The grey numbers in the graph represent the intervals in which the number of medals is predicted. According to the analysis, the top two positions (USA and China) remained stable. However, Canada and the United Kingdom saw significant improvements in their rankings, rising to third and fourth, respectively. Although their total medal counts may still be lower than some other traditional powerhouses, this shift likely reflects notable progress by Canada and the UK in events with strengths similar to those of the United States. Specifically, these countries increased their participation in these events, boosting their gold medal counts. As a result, they surpassed several countries with higher total medal counts and secured higher po- sitions in the rankings. On the other hand, France's ranking declined, suggesting that the ad- vantage it gained from the host nation effect has almost diminished.

<!-- b000524 | heading | pages [13] -->
5.3.2 Visualizing the progress of countries in the Olympics

<!-- b000525 | prose | pages [13] -->
The bar chart below visually presents the predicted medal counts for each country based on the applied forecasting model, while the heatmap below reveals the dynamic changes in Olympic medal performance across countries. The deep red regions indicate countries that have withdrawn from the Olympics for specific reasons, such as Russia and Belarus. The var- iation in other colors reflects the trend of changes in medal performance: the closer the color is to red, the more significant the progress indicated by the prediction; conversely, the closer the color is to blue, the more it suggests a decline in the country's predicted performance. No- tably, the yellow-green regions on the heatmap highlight countries predicted to win medals for the first time, such as the Maldives and Andorra, with predicted probabilities of 0.32 and 0.39, respectively.

<!-- b000526 | furniture | pages [14] -->
Team # 2515235

<!-- b000527 | furniture | pages [14] -->
Page 14 of 26

<!-- b000528 | caption | pages [14] -->
Figure 7. Number of medals won by countries in the world and progress made by coun-tries

<!-- b000529 | prose | pages [14] -->
These countries may achieve their first medals due to emerging potential in certain sports (e.g., swimming, athletics) that are similar to events where the United States excels, thereby increasing their participation rate and number of athletes, which in turn enhances the likeli- hood of winning medals. From the chart, it can be observed that most countries in Africa, South America, and Europe are facing a trend of decline, suggesting that these regions may struggle to maintain or improve their medal performances in future Olympic Games. In con- trast, countries in North America generally show a significant upward trend. Progress in other continents is more scattered, with no clear regional clustering of improvements.5.3.3：Ana- lyzing event relevance and giving advice.

<!-- b000530 | prose | pages [14] -->
To analyze the contribution of individual sports to a country's total medal count, we in- troduce the Sport Contribution Score (SCS). This indicator quantifies the impact of each country's performance in different Olympic events on its overall medal tally. The formula is as follows:

<!-- b000531 | prose | pages [14] -->
∑ 𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔× 𝒔𝒄𝒐𝒓𝒆𝒎 𝒎∈𝑴 (6) 𝒔𝒄𝒔𝒊,𝒔= 𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔′ × 𝒔𝒄𝒐𝒓𝒆𝒎 ∑ ∑ 𝒔 ∈𝑺 𝒎∈𝑴

<!-- b000532 | prose | pages [14, 15] -->
关注数学模型 𝒔𝒄𝒔𝒊,𝒔 represents the contribution score of country i in sport s. M includes gold, silver, and bronze medals，𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔 refers to the number of medals won by country i in sport s. 𝒔𝒄𝒐𝒓𝒆𝒎 denotes the score assigned to each type of medal in event m. Consistent with the previous definitions, the scores for gold, silver, and bronze medals are 3, 2, and 1, respec- tively. However, unlike before, not winning any medals counts as 0. 𝒔′ represents all events, and 𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔′is the total number of medals won by country i across all events. The SCS score reflects the impact of each sport on the country's total medal count; a value close to 1 indicates a significant contribution, while a lower value suggests a smaller impact. Specifi- 微信公众号：数学模型 cally, the SCS value for the sport with the highest medal proportion for a country reflects that sport’s dominant impact on the country's overall medal performance. The pseudo-code is as follows：

<!-- b000533 | furniture | pages [14] -->
2

<!-- b000534 | furniture | pages [14] -->
MATHmodels

<!-- b000535 | furniture | pages [14] -->
获取更多资讯

<!-- b000536 | furniture | pages [15] -->
Team # 2515235

<!-- b000537 | furniture | pages [15] -->
Page 15 of 26

<!-- b000539 | heading | pages [15] -->
Algorithm 1 Calculate the contribution of Sport Contribution Score

<!-- b000540 | prose | pages [15] -->
For each country i in the countries of dataset: For each sport category s in the sport categories of dataset: medals_s = Get all medal data for sport category s in country c total_score_s = 0 For each medal type m in {Gold, Silver, Bronze}: 微信号：MATHmodels count_m_s = Number of medals of type m in sport category s for country c total_score_s += count_m_s * (Gold if m = Gold, Silver if m = Silver, Bronze if m = Bronze) sport_contributions[c, s] = total_score_s / total_scores[c] Return sport_contributions

<!-- b000541 | prose | pages [15] -->
Across countries, the highest SCS value represents the degree of influence from that par- ticular sport. For example, if a country’s highest SCS corresponds to water sports, a reduction in water sports events at the Olympics would significantly affect that country's medal count. Thus, the SCS of the sport with the highest medal proportion in each country represents the impact of that sport on the country's medal performance. After calculating the SCS for all sports, the sport with the highest SCS for each country is selected for further analysis.

<!-- b000542 | caption | pages [15] -->
Figure 8: Pearson correlation analysis of project participation rates and SCS line graphs

<!-- b000543 | prose | pages [15, 16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Effects of sport types: The x-axis represents 206 countries which participate the Olympics, and the y-axis represents the SCS score. A score of 0 indicates countries with no medals, while lower scores suggest that countries are more susceptible to the influence of event types. Countries least affected by this influence include China, Russia, and the United States, while countries most affected include the Niger, and Togo. In this part Niger and Togo are very susceptible to track and field events. More details are shown in problem 3.

<!-- b000544 | furniture | pages [15] -->
m

<!-- b000545 | furniture | pages [15] -->
m

<!-- b000546 | furniture | pages [15] -->
m

<!-- b000547 | furniture | pages [15] -->
m

<!-- b000548 | furniture | pages [15] -->
m

<!-- b000549 | furniture | pages [15] -->
m

<!-- b000550 | furniture | pages [15] -->
m

<!-- b000551 | furniture | pages [15] -->
m

<!-- b000552 | furniture | pages [15] -->
m

<!-- b000553 | furniture | pages [15] -->
m

<!-- b000554 | furniture | pages [15] -->
m

<!-- b000555 | furniture | pages [15] -->
m

<!-- b000556 | furniture | pages [15] -->
m

<!-- b000557 | furniture | pages [15] -->
m

<!-- b000558 | furniture | pages [15] -->
m

<!-- b000559 | furniture | pages [15] -->
m

<!-- b000560 | furniture | pages [15] -->
m

<!-- b000561 | furniture | pages [15] -->
m

<!-- b000562 | furniture | pages [15] -->
m

<!-- b000563 | furniture | pages [15] -->
m

<!-- b000564 | furniture | pages [15] -->
m

<!-- b000565 | furniture | pages [15] -->
m

<!-- b000566 | furniture | pages [15] -->
m

<!-- b000567 | furniture | pages [15] -->
m

<!-- b000568 | furniture | pages [15] -->
m

<!-- b000569 | furniture | pages [15] -->
m

<!-- b000570 | furniture | pages [15] -->
m

<!-- b000571 | furniture | pages [15] -->
m

<!-- b000572 | furniture | pages [15] -->
m

<!-- b000573 | furniture | pages [15] -->
m

<!-- b000574 | furniture | pages [15] -->
m

<!-- b000575 | furniture | pages [15] -->
m

<!-- b000576 | furniture | pages [15] -->
m

<!-- b000577 | furniture | pages [15] -->
m

<!-- b000578 | furniture | pages [15] -->
m

<!-- b000579 | furniture | pages [15] -->
m

<!-- b000580 | furniture | pages [15] -->
m

<!-- b000581 | furniture | pages [15] -->
m

<!-- b000582 | furniture | pages [15] -->
m

<!-- b000583 | furniture | pages [15] -->
m

<!-- b000584 | furniture | pages [15] -->
m

<!-- b000585 | furniture | pages [15] -->
m

<!-- b000586 | furniture | pages [15] -->
m

<!-- b000587 | furniture | pages [15] -->
m

<!-- b000588 | furniture | pages [15] -->
m

<!-- b000589 | furniture | pages [15] -->
m

<!-- b000590 | furniture | pages [15] -->
m

<!-- b000591 | furniture | pages [15] -->
m

<!-- b000592 | furniture | pages [15] -->
m

<!-- b000593 | furniture | pages [15] -->
m

<!-- b000594 | furniture | pages [15] -->
m

<!-- b000595 | furniture | pages [15] -->
m

<!-- b000596 | furniture | pages [15] -->
m

<!-- b000597 | furniture | pages [15] -->
m

<!-- b000598 | furniture | pages [15] -->
m

<!-- b000599 | furniture | pages [15] -->
m

<!-- b000600 | furniture | pages [15] -->
m

<!-- b000601 | furniture | pages [15] -->
m

<!-- b000602 | furniture | pages [15] -->
m

<!-- b000603 | furniture | pages [15] -->
m

<!-- b000604 | furniture | pages [15] -->
m

<!-- b000605 | furniture | pages [15] -->
m

<!-- b000606 | furniture | pages [15] -->
m

<!-- b000607 | furniture | pages [15] -->
m

<!-- b000608 | furniture | pages [15] -->
m

<!-- b000609 | furniture | pages [15] -->
m

<!-- b000610 | furniture | pages [15] -->
m

<!-- b000611 | furniture | pages [15] -->
m

<!-- b000612 | furniture | pages [15] -->
m

<!-- b000613 | furniture | pages [15] -->
m

<!-- b000614 | furniture | pages [15] -->
m

<!-- b000615 | furniture | pages [15] -->
m

<!-- b000616 | furniture | pages [15] -->
m

<!-- b000617 | furniture | pages [15] -->
m

<!-- b000618 | furniture | pages [15] -->
m

<!-- b000619 | furniture | pages [15] -->
m

<!-- b000620 | furniture | pages [15] -->
m

<!-- b000621 | furniture | pages [15] -->
m

<!-- b000622 | furniture | pages [15] -->
m

<!-- b000623 | furniture | pages [15] -->
m

<!-- b000624 | furniture | pages [15] -->
m

<!-- b000625 | furniture | pages [15] -->
m

<!-- b000626 | furniture | pages [15] -->
m

<!-- b000627 | furniture | pages [15] -->
m

<!-- b000628 | furniture | pages [15] -->
m

<!-- b000629 | furniture | pages [15] -->
m

<!-- b000630 | furniture | pages [15] -->
m

<!-- b000631 | furniture | pages [15] -->
m

<!-- b000632 | furniture | pages [15] -->
m

<!-- b000633 | furniture | pages [15] -->
m

<!-- b000634 | furniture | pages [15] -->
m

<!-- b000635 | furniture | pages [15] -->
m

<!-- b000636 | furniture | pages [15] -->
m

<!-- b000637 | furniture | pages [15] -->
m

<!-- b000638 | furniture | pages [15] -->
m

<!-- b000639 | furniture | pages [15] -->
m

<!-- b000640 | furniture | pages [15] -->
m

<!-- b000641 | furniture | pages [15] -->
m

<!-- b000642 | furniture | pages [15] -->
m

<!-- b000643 | furniture | pages [15] -->
m

<!-- b000644 | furniture | pages [15] -->
m

<!-- b000645 | furniture | pages [15] -->
m

<!-- b000646 | furniture | pages [15] -->
m

<!-- b000647 | furniture | pages [15] -->
m

<!-- b000648 | furniture | pages [15] -->
m

<!-- b000649 | furniture | pages [15] -->
m

<!-- b000650 | furniture | pages [15] -->
m

<!-- b000651 | furniture | pages [15] -->
m

<!-- b000652 | furniture | pages [15] -->
m

<!-- b000653 | furniture | pages [15] -->
m

<!-- b000654 | furniture | pages [15] -->
m

<!-- b000655 | furniture | pages [15] -->
m

<!-- b000656 | furniture | pages [15] -->
m

<!-- b000657 | furniture | pages [15] -->
m

<!-- b000658 | furniture | pages [15] -->
m

<!-- b000659 | furniture | pages [15] -->
m

<!-- b000660 | furniture | pages [15] -->
m

<!-- b000661 | furniture | pages [15] -->
m

<!-- b000662 | furniture | pages [15] -->
m

<!-- b000663 | furniture | pages [15] -->
m

<!-- b000664 | furniture | pages [15] -->
m

<!-- b000665 | furniture | pages [15] -->
m

<!-- b000666 | furniture | pages [15] -->
m

<!-- b000667 | furniture | pages [15] -->
m

<!-- b000668 | furniture | pages [15] -->
m

<!-- b000669 | furniture | pages [15] -->
m

<!-- b000670 | furniture | pages [15] -->
m

<!-- b000671 | furniture | pages [15] -->
m

<!-- b000672 | furniture | pages [15] -->
m

<!-- b000673 | furniture | pages [15] -->
m

<!-- b000674 | furniture | pages [15] -->
m

<!-- b000675 | furniture | pages [15] -->
m

<!-- b000676 | furniture | pages [15] -->
m

<!-- b000677 | furniture | pages [15] -->
m

<!-- b000678 | furniture | pages [15] -->
m

<!-- b000679 | furniture | pages [15] -->
m

<!-- b000680 | furniture | pages [15] -->
m

<!-- b000681 | furniture | pages [15] -->
m

<!-- b000682 | furniture | pages [15] -->
m

<!-- b000683 | furniture | pages [15] -->
m

<!-- b000684 | furniture | pages [15] -->
m

<!-- b000685 | furniture | pages [15] -->
m

<!-- b000686 | furniture | pages [15] -->
m

<!-- b000687 | furniture | pages [15] -->
m

<!-- b000688 | furniture | pages [15] -->
m

<!-- b000689 | furniture | pages [15] -->
m

<!-- b000690 | furniture | pages [15] -->
m

<!-- b000691 | furniture | pages [15] -->
m

<!-- b000692 | furniture | pages [15] -->
m

<!-- b000693 | furniture | pages [15] -->
m

<!-- b000694 | furniture | pages [15] -->
m

<!-- b000695 | furniture | pages [15] -->
m

<!-- b000696 | furniture | pages [15] -->
m

<!-- b000697 | furniture | pages [15] -->
m

<!-- b000698 | furniture | pages [15] -->
m

<!-- b000699 | furniture | pages [15] -->
m

<!-- b000700 | furniture | pages [15] -->
m

<!-- b000701 | furniture | pages [15] -->
m

<!-- b000702 | furniture | pages [15] -->
m

<!-- b000703 | furniture | pages [15] -->
m

<!-- b000704 | furniture | pages [15] -->
m

<!-- b000705 | furniture | pages [15] -->
m

<!-- b000706 | furniture | pages [15] -->
m

<!-- b000707 | furniture | pages [15] -->
m

<!-- b000708 | furniture | pages [15] -->
m

<!-- b000709 | furniture | pages [15] -->
m

<!-- b000710 | furniture | pages [15] -->
m

<!-- b000711 | furniture | pages [15] -->
m

<!-- b000712 | furniture | pages [15] -->
m

<!-- b000713 | furniture | pages [15] -->
m

<!-- b000714 | furniture | pages [15] -->
m

<!-- b000715 | furniture | pages [15] -->
m

<!-- b000716 | furniture | pages [15] -->
m

<!-- b000717 | furniture | pages [15] -->
m

<!-- b000718 | furniture | pages [15] -->
m

<!-- b000719 | furniture | pages [15] -->
m

<!-- b000720 | furniture | pages [15] -->
m

<!-- b000721 | furniture | pages [15] -->
m

<!-- b000722 | furniture | pages [15] -->
m

<!-- b000723 | furniture | pages [15] -->
m

<!-- b000724 | furniture | pages [15] -->
m

<!-- b000725 | furniture | pages [15] -->
m

<!-- b000726 | furniture | pages [15] -->
m

<!-- b000727 | furniture | pages [15] -->
m

<!-- b000728 | furniture | pages [15] -->
m

<!-- b000729 | furniture | pages [15] -->
m

<!-- b000730 | furniture | pages [15] -->
m

<!-- b000731 | furniture | pages [15] -->
m

<!-- b000732 | furniture | pages [15] -->
m

<!-- b000733 | furniture | pages [15] -->
m

<!-- b000734 | furniture | pages [15] -->
m

<!-- b000735 | furniture | pages [15] -->
m

<!-- b000736 | furniture | pages [15] -->
m

<!-- b000737 | furniture | pages [15] -->
m

<!-- b000738 | furniture | pages [15] -->
m

<!-- b000739 | furniture | pages [15] -->
m

<!-- b000740 | furniture | pages [15] -->
m

<!-- b000741 | furniture | pages [15] -->
m

<!-- b000742 | furniture | pages [15] -->
m

<!-- b000743 | furniture | pages [15] -->
m

<!-- b000744 | furniture | pages [15] -->
m

<!-- b000745 | furniture | pages [15] -->
m

<!-- b000746 | furniture | pages [15] -->
m

<!-- b000747 | furniture | pages [15] -->
m

<!-- b000748 | furniture | pages [15] -->
m

<!-- b000749 | furniture | pages [15] -->
m

<!-- b000750 | furniture | pages [15] -->
m

<!-- b000751 | furniture | pages [15] -->
m

<!-- b000752 | furniture | pages [15] -->
m

<!-- b000753 | furniture | pages [15] -->
m

<!-- b000754 | furniture | pages [15] -->
m

<!-- b000755 | furniture | pages [15] -->
m

<!-- b000756 | furniture | pages [15] -->
m

<!-- b000757 | furniture | pages [15] -->
m

<!-- b000758 | furniture | pages [15] -->
m

<!-- b000759 | furniture | pages [15] -->
m

<!-- b000760 | furniture | pages [15] -->
m

<!-- b000761 | furniture | pages [15] -->
m

<!-- b000762 | furniture | pages [15] -->
m

<!-- b000763 | furniture | pages [15] -->
m

<!-- b000764 | furniture | pages [15] -->
m

<!-- b000765 | furniture | pages [15] -->
m

<!-- b000766 | furniture | pages [15] -->
m

<!-- b000767 | furniture | pages [15] -->
m

<!-- b000768 | furniture | pages [15] -->
m

<!-- b000769 | furniture | pages [15] -->
m

<!-- b000770 | furniture | pages [15] -->
m

<!-- b000771 | furniture | pages [15] -->
m

<!-- b000772 | furniture | pages [15] -->
m

<!-- b000773 | furniture | pages [15] -->
m

<!-- b000774 | furniture | pages [15] -->
m

<!-- b000775 | furniture | pages [15] -->
m

<!-- b000776 | furniture | pages [15] -->
m

<!-- b000777 | furniture | pages [15] -->
m

<!-- b000778 | furniture | pages [15] -->
m

<!-- b000779 | furniture | pages [15] -->
m

<!-- b000780 | furniture | pages [15] -->
m

<!-- b000781 | furniture | pages [15] -->
m

<!-- b000782 | furniture | pages [15] -->
m

<!-- b000783 | furniture | pages [15] -->
m

<!-- b000784 | furniture | pages [15] -->
m

<!-- b000785 | furniture | pages [15] -->
m

<!-- b000786 | furniture | pages [15] -->
m

<!-- b000787 | furniture | pages [15] -->
m

<!-- b000788 | furniture | pages [15] -->
m

<!-- b000789 | furniture | pages [15] -->
m

<!-- b000790 | furniture | pages [15] -->
m

<!-- b000791 | furniture | pages [15] -->
m

<!-- b000792 | furniture | pages [15] -->
m

<!-- b000793 | furniture | pages [15] -->
m

<!-- b000794 | furniture | pages [15] -->
m

<!-- b000795 | furniture | pages [15] -->
m

<!-- b000796 | furniture | pages [15] -->
m

<!-- b000797 | furniture | pages [15] -->
m

<!-- b000798 | furniture | pages [15] -->
m

<!-- b000799 | furniture | pages [15] -->
m

<!-- b000800 | furniture | pages [15] -->
m

<!-- b000801 | furniture | pages [15] -->
m

<!-- b000802 | furniture | pages [15] -->
m

<!-- b000803 | furniture | pages [15] -->
m

<!-- b000804 | furniture | pages [15] -->
m

<!-- b000805 | furniture | pages [15] -->
m

<!-- b000806 | furniture | pages [15] -->
m

<!-- b000807 | furniture | pages [15] -->
m

<!-- b000808 | furniture | pages [15] -->
m

<!-- b000809 | furniture | pages [15] -->
m

<!-- b000810 | furniture | pages [15] -->
m

<!-- b000811 | furniture | pages [15] -->
m

<!-- b000812 | furniture | pages [15] -->
m

<!-- b000813 | furniture | pages [15] -->
m

<!-- b000814 | furniture | pages [15] -->
m

<!-- b000815 | furniture | pages [15] -->
m

<!-- b000816 | furniture | pages [15] -->
m

<!-- b000817 | furniture | pages [15] -->
m

<!-- b000818 | furniture | pages [15] -->
m

<!-- b000819 | furniture | pages [15] -->
m

<!-- b000820 | furniture | pages [15] -->
m

<!-- b000821 | furniture | pages [15] -->
m

<!-- b000822 | furniture | pages [15] -->
m

<!-- b000823 | furniture | pages [15] -->
m

<!-- b000824 | furniture | pages [15] -->
m

<!-- b000825 | furniture | pages [15] -->
m

<!-- b000826 | furniture | pages [15] -->
m

<!-- b000827 | furniture | pages [15] -->
m

<!-- b000828 | furniture | pages [15] -->
m

<!-- b000829 | furniture | pages [15] -->
m

<!-- b000830 | furniture | pages [15] -->
m

<!-- b000831 | furniture | pages [15] -->
m

<!-- b000832 | furniture | pages [15] -->
m

<!-- b000833 | furniture | pages [15] -->
m

<!-- b000834 | furniture | pages [15] -->
m

<!-- b000835 | furniture | pages [15] -->
m

<!-- b000836 | furniture | pages [15] -->
m

<!-- b000837 | furniture | pages [15] -->
m

<!-- b000838 | furniture | pages [15] -->
m

<!-- b000839 | furniture | pages [15] -->
m

<!-- b000840 | furniture | pages [15] -->
m

<!-- b000841 | furniture | pages [15] -->
m

<!-- b000842 | furniture | pages [15] -->
m

<!-- b000843 | furniture | pages [15] -->
m

<!-- b000844 | furniture | pages [15] -->
m

<!-- b000845 | furniture | pages [15] -->
m

<!-- b000846 | furniture | pages [15] -->
m

<!-- b000847 | furniture | pages [15] -->
m

<!-- b000848 | furniture | pages [15] -->
m

<!-- b000849 | furniture | pages [15] -->
m

<!-- b000850 | furniture | pages [15] -->
m

<!-- b000851 | furniture | pages [15] -->
m

<!-- b000852 | furniture | pages [15] -->
m

<!-- b000853 | furniture | pages [15] -->
m

<!-- b000854 | furniture | pages [15] -->
m

<!-- b000855 | furniture | pages [15] -->
m

<!-- b000856 | furniture | pages [15] -->
m

<!-- b000857 | furniture | pages [15] -->
m

<!-- b000858 | furniture | pages [15] -->
m

<!-- b000859 | furniture | pages [15] -->
m

<!-- b000860 | furniture | pages [15] -->
m

<!-- b000861 | furniture | pages [15] -->
m

<!-- b000862 | furniture | pages [15] -->
m

<!-- b000863 | furniture | pages [15] -->
m

<!-- b000864 | furniture | pages [15] -->
m

<!-- b000865 | furniture | pages [15] -->
m

<!-- b000866 | furniture | pages [15] -->
m

<!-- b000867 | furniture | pages [15] -->
m

<!-- b000868 | furniture | pages [16] -->
Team # 2515235

<!-- b000869 | furniture | pages [16] -->
Page 16 of 26

<!-- b000871 | prose | pages [16] -->
Effects of event number：The participation rate reflects the number of events a country par- ticipates in at each Olympic Games. Therefore, we conducted a Pearson correlation analysis on the two models we developed and averaged the resulting coefficients. As shown in the confusion matrix below, there is a significant positive correlation between the event participa- tion rate and the total medal count, with a correlation coefficient of approximately 0.416. This indicates that the event participation rate significantly contributes to the growth of a country's medal count, with a notable positive impact. It suggests that a country's active participation in more events may increase its chances, and the total number of medals won.

<!-- b000872 | heading | pages [16] -->
6 Model 2: Analysis “great coach” effect by DRD-CE Model.

<!-- b000873 | prose | pages [16] -->
The "Great Coach Effect" can be defined as the phenomenon where a coach signifi- cantly improves an athlete's performance through exceptional expertise, tactical guidance, and motivational methods, leading the team to achieve outstanding results in international competitions. Inspired by the work of [4,5,6], a great coach's impact can be compared to a significant policy change in a country's sports programs. Therefore, mathematical models used to analyze policy changes, such as the Difference-in-Differences (DID) method and dy- namic panel data models, are appropriate choices for this analysis. This study combines the Difference-in-Differences (DID) method with a double robust estimator to construct a spe- cialized model for analyzing the "Great Coach Effect." This model is referred to as the Du- rable Robust Coach Effect Model (DRD-CE Model).

<!-- b000874 | heading | pages [16] -->
6.1 The Establishment of Model 2

<!-- b000875 | prose | pages [16] -->
Dynamic Difference-in-Differences (DID): The standard DID method typically as- sumes a comparison between treatment and control groups at two time points. However, when treatment occurs at different time points across multiple groups (i.e., different countries or regions receiving treatment at different times), the standard DID method may fail to accu- rately capture the treatment effect. The "Great Coach Effect" typically occurs at different time points. To address this challenge, we designed a dynamic DID method by incorporating an event-study approach. This allows us to effectively estimate the "Great Coach Effect" across multiple time periods and treatment groups, even when each group experiences treat- ment at different times. The formula is as follows:

<!-- b000876 | prose | pages [16, 17] -->
关注数学模型 𝑲 (7) ⋅ 𝑷𝑪 𝒊𝒕+𝒌+ 𝜸⋅𝑿𝒊+ 𝜹⋅ 𝒀 𝒕+ 𝝐𝒊𝒕 𝑴𝒊,𝒕= 𝜶+ ∑𝜷𝒌 𝒌=−𝑲 𝑷𝑪 𝒊𝒕+𝒌 is a binary variable indicating whether country i experienced a coach change at time t. If a coach change occurred at time t, then  𝑷𝒐𝒔𝒕𝑪𝒐𝒂𝒄𝒉 𝒊𝒕+𝒌= 𝟏; otherwise, it is 0. 𝑿𝒊 represents country i's covariates, which include dynamic national characteristics such as Host Effect (𝑯𝑬), participation ratio in events (𝑵𝑬) and athlete performance in recent Olym- pics( 𝑨𝑷 𝒊).  𝒀 𝒕 represents constant national characteristics, including long-term project par- ticipation rate( 𝑵Ē 𝒕) and Normalized Medal Average( 𝑵𝑴̅̅̅̅̅𝒊).

<!-- b000877 | furniture | pages [16] -->
2

<!-- b000878 | furniture | pages [16] -->
MATHmodels

<!-- b000879 | furniture | pages [16] -->
获取更多资讯

<!-- b000880 | furniture | pages [17] -->
Team # 2515235

<!-- b000881 | furniture | pages [17] -->
Page 17 of 26

<!-- b000883 | prose | pages [17] -->
Inverse Probability Weighting (IPW): The IPW method estimates treatment effects by 微信公众号：数学模型 weighting each individual's probability of receiving treatment. These weights are calculated based on the likelihood of receiving treatment, helping to correct for bias caused by imbal- anced covariates. By using weighted samples, IPW ensures that treatment effects between different groups are comparable, thus avoiding bias caused by differences in covariates.

<!-- b000884 | prose | pages [17] -->
𝑵 𝑵 𝑰𝑷𝑾= 𝟏 𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅𝑴𝒊,𝒕] −𝟏 𝑷𝑪𝒊𝒕 𝟏−𝑷𝑪𝒊𝒕 ^ (8) 𝟏−𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅𝑴𝒊,𝒕] 𝝉 𝑵∑[ 𝑵∑[ 𝒊=𝟏 𝒊=𝟏 ^ represents the treatment effect, which reflects the causal impact of an intervention (e.g., 𝝉 微信号：MATHmodels coach impact) on an outcome (e.g., Olympic medal count). 𝑷(𝑮𝒊𝒕∣𝑿𝒊) is the probability that 𝑮𝒊𝒕 𝟏−𝑮𝒊𝒕 country i receives a great coach at time t, based on the covariates . 𝑷(𝑮𝒊𝒕∣𝑿𝒊) and 𝟏−𝑷(𝑮𝒊𝒕∣𝑿𝒊) are the weighting factors for each country, indicating the weighted probabilities for the treatment and control groups, respectively. 𝑷(𝑮𝒊𝒕∣𝑿𝒊) is predicted using logistic regression based on the covariates, and the simplified formula is as follows:

<!-- b000885 | prose | pages [17] -->
𝟏 𝟏+ 𝐞𝐱𝐩 (−(𝒄𝒕+ 𝒅𝑿𝒊)) (9) 𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) =

<!-- b000886 | prose | pages [17] -->
𝒄𝒕 is the time fixed effect at time t, representing the time effect of the treatment. d is the regression coefficient of covariates 𝑿𝒊, indicating the influence of covariates on the probability of treatment.

<!-- b000887 | prose | pages [17] -->
Double Robust Estimator: The double robust estimator combines the advantages of outcome regression and inverse probability weighting. It estimates treatment effects by simul- taneously using a regression model for covariates and a weighted model for treatment proba- bilities. The double robust estimator provides consistent estimates as long as at least one of the estimation methods is correctly specified.

<!-- b000888 | prose | pages [17] -->
𝑵 𝑫𝑹= 𝟏 𝑷𝑪𝒊𝒕 ^ ^(𝑿𝒊)) + 𝝁 ^(𝑿𝒊)] 𝝉 𝑵∑[ 𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅(𝑴𝒊𝒕−𝝁 𝒊=𝟏

<!-- b000889 | prose | pages [17, 18] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝑵 −𝟏 𝟏−𝑮𝒊𝒕 ^(𝑿𝒊)) + 𝝁 ^(𝑿𝒊)] 𝑵∑[ 𝟏−𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅(𝑴𝒊𝒕−𝝁 (10) 𝒊=𝟏

<!-- b000890 | furniture | pages [17] -->
m

<!-- b000891 | furniture | pages [17] -->
m

<!-- b000892 | furniture | pages [17] -->
m

<!-- b000893 | furniture | pages [17] -->
m

<!-- b000894 | furniture | pages [17] -->
m

<!-- b000895 | furniture | pages [17] -->
m

<!-- b000896 | furniture | pages [17] -->
m

<!-- b000897 | furniture | pages [17] -->
m

<!-- b000898 | furniture | pages [17] -->
m

<!-- b000899 | furniture | pages [17] -->
m

<!-- b000900 | furniture | pages [17] -->
m

<!-- b000901 | furniture | pages [17] -->
m

<!-- b000902 | furniture | pages [17] -->
m

<!-- b000903 | furniture | pages [17] -->
m

<!-- b000904 | furniture | pages [17] -->
m

<!-- b000905 | furniture | pages [17] -->
m

<!-- b000906 | furniture | pages [17] -->
m

<!-- b000907 | furniture | pages [17] -->
m

<!-- b000908 | furniture | pages [17] -->
m

<!-- b000909 | furniture | pages [17] -->
m

<!-- b000910 | furniture | pages [17] -->
m

<!-- b000911 | furniture | pages [17] -->
m

<!-- b000912 | furniture | pages [17] -->
m

<!-- b000913 | furniture | pages [17] -->
m

<!-- b000914 | furniture | pages [17] -->
m

<!-- b000915 | furniture | pages [17] -->
m

<!-- b000916 | furniture | pages [17] -->
m

<!-- b000917 | furniture | pages [17] -->
m

<!-- b000918 | furniture | pages [17] -->
m

<!-- b000919 | furniture | pages [17] -->
m

<!-- b000920 | furniture | pages [17] -->
m

<!-- b000921 | furniture | pages [17] -->
m

<!-- b000922 | furniture | pages [17] -->
m

<!-- b000923 | furniture | pages [17] -->
m

<!-- b000924 | furniture | pages [17] -->
m

<!-- b000925 | furniture | pages [17] -->
m

<!-- b000926 | furniture | pages [17] -->
m

<!-- b000927 | furniture | pages [17] -->
m

<!-- b000928 | furniture | pages [17] -->
m

<!-- b000929 | furniture | pages [17] -->
m

<!-- b000930 | furniture | pages [17] -->
m

<!-- b000931 | furniture | pages [17] -->
m

<!-- b000932 | furniture | pages [17] -->
m

<!-- b000933 | furniture | pages [17] -->
m

<!-- b000934 | furniture | pages [17] -->
m

<!-- b000935 | furniture | pages [17] -->
m

<!-- b000936 | furniture | pages [17] -->
m

<!-- b000937 | furniture | pages [17] -->
m

<!-- b000938 | furniture | pages [17] -->
m

<!-- b000939 | furniture | pages [17] -->
m

<!-- b000940 | furniture | pages [17] -->
m

<!-- b000941 | furniture | pages [17] -->
m

<!-- b000942 | furniture | pages [17] -->
m

<!-- b000943 | furniture | pages [17] -->
m

<!-- b000944 | furniture | pages [17] -->
m

<!-- b000945 | furniture | pages [17] -->
m

<!-- b000946 | furniture | pages [17] -->
m

<!-- b000947 | furniture | pages [17] -->
m

<!-- b000948 | furniture | pages [17] -->
m

<!-- b000949 | furniture | pages [17] -->
m

<!-- b000950 | furniture | pages [17] -->
m

<!-- b000951 | furniture | pages [17] -->
m

<!-- b000952 | furniture | pages [17] -->
m

<!-- b000953 | furniture | pages [17] -->
m

<!-- b000954 | furniture | pages [17] -->
m

<!-- b000955 | furniture | pages [17] -->
m

<!-- b000956 | furniture | pages [17] -->
m

<!-- b000957 | furniture | pages [17] -->
m

<!-- b000958 | furniture | pages [17] -->
m

<!-- b000959 | furniture | pages [17] -->
m

<!-- b000960 | furniture | pages [17] -->
m

<!-- b000961 | furniture | pages [17] -->
m

<!-- b000962 | furniture | pages [17] -->
m

<!-- b000963 | furniture | pages [17] -->
m

<!-- b000964 | furniture | pages [17] -->
m

<!-- b000965 | furniture | pages [17] -->
m

<!-- b000966 | furniture | pages [17] -->
m

<!-- b000967 | furniture | pages [17] -->
m

<!-- b000968 | furniture | pages [17] -->
m

<!-- b000969 | furniture | pages [17] -->
m

<!-- b000970 | furniture | pages [17] -->
m

<!-- b000971 | furniture | pages [17] -->
m

<!-- b000972 | furniture | pages [17] -->
m

<!-- b000973 | furniture | pages [17] -->
m

<!-- b000974 | furniture | pages [17] -->
m

<!-- b000975 | furniture | pages [17] -->
m

<!-- b000976 | furniture | pages [17] -->
m

<!-- b000977 | furniture | pages [17] -->
m

<!-- b000978 | furniture | pages [17] -->
m

<!-- b000979 | furniture | pages [17] -->
m

<!-- b000980 | furniture | pages [17] -->
m

<!-- b000981 | furniture | pages [17] -->
m

<!-- b000982 | furniture | pages [17] -->
m

<!-- b000983 | furniture | pages [17] -->
m

<!-- b000984 | furniture | pages [17] -->
m

<!-- b000985 | furniture | pages [17] -->
m

<!-- b000986 | furniture | pages [17] -->
m

<!-- b000987 | furniture | pages [17] -->
m

<!-- b000988 | furniture | pages [17] -->
m

<!-- b000989 | furniture | pages [17] -->
m

<!-- b000990 | furniture | pages [17] -->
m

<!-- b000991 | furniture | pages [17] -->
m

<!-- b000992 | furniture | pages [17] -->
m

<!-- b000993 | furniture | pages [17] -->
m

<!-- b000994 | furniture | pages [17] -->
m

<!-- b000995 | furniture | pages [17] -->
m

<!-- b000996 | furniture | pages [17] -->
m

<!-- b000997 | furniture | pages [17] -->
m

<!-- b000998 | furniture | pages [17] -->
m

<!-- b000999 | furniture | pages [17] -->
m

<!-- b001000 | furniture | pages [17] -->
m

<!-- b001001 | furniture | pages [17] -->
m

<!-- b001002 | furniture | pages [17] -->
m

<!-- b001003 | furniture | pages [17] -->
m

<!-- b001004 | furniture | pages [17] -->
m

<!-- b001005 | furniture | pages [17] -->
m

<!-- b001006 | furniture | pages [17] -->
m

<!-- b001007 | furniture | pages [17] -->
m

<!-- b001008 | furniture | pages [17] -->
m

<!-- b001009 | furniture | pages [17] -->
m

<!-- b001010 | furniture | pages [17] -->
m

<!-- b001011 | furniture | pages [17] -->
m

<!-- b001012 | furniture | pages [17] -->
m

<!-- b001013 | furniture | pages [17] -->
m

<!-- b001014 | furniture | pages [17] -->
m

<!-- b001015 | furniture | pages [17] -->
m

<!-- b001016 | furniture | pages [17] -->
m

<!-- b001017 | furniture | pages [17] -->
m

<!-- b001018 | furniture | pages [17] -->
m

<!-- b001019 | furniture | pages [17] -->
m

<!-- b001020 | furniture | pages [17] -->
m

<!-- b001021 | furniture | pages [17] -->
m

<!-- b001022 | furniture | pages [17] -->
m

<!-- b001023 | furniture | pages [17] -->
m

<!-- b001024 | furniture | pages [17] -->
m

<!-- b001025 | furniture | pages [17] -->
m

<!-- b001026 | furniture | pages [17] -->
m

<!-- b001027 | furniture | pages [17] -->
m

<!-- b001028 | furniture | pages [17] -->
m

<!-- b001029 | furniture | pages [17] -->
m

<!-- b001030 | furniture | pages [17] -->
m

<!-- b001031 | furniture | pages [17] -->
m

<!-- b001032 | furniture | pages [17] -->
m

<!-- b001033 | furniture | pages [17] -->
m

<!-- b001034 | furniture | pages [17] -->
m

<!-- b001035 | furniture | pages [17] -->
m

<!-- b001036 | furniture | pages [17] -->
m

<!-- b001037 | furniture | pages [17] -->
m

<!-- b001038 | furniture | pages [17] -->
m

<!-- b001039 | furniture | pages [17] -->
m

<!-- b001040 | furniture | pages [17] -->
m

<!-- b001041 | furniture | pages [17] -->
m

<!-- b001042 | furniture | pages [17] -->
m

<!-- b001043 | furniture | pages [17] -->
m

<!-- b001044 | furniture | pages [17] -->
m

<!-- b001045 | furniture | pages [17] -->
m

<!-- b001046 | furniture | pages [17] -->
m

<!-- b001047 | furniture | pages [17] -->
m

<!-- b001048 | furniture | pages [17] -->
m

<!-- b001049 | furniture | pages [17] -->
m

<!-- b001050 | furniture | pages [17] -->
m

<!-- b001051 | furniture | pages [17] -->
m

<!-- b001052 | furniture | pages [17] -->
m

<!-- b001053 | furniture | pages [17] -->
m

<!-- b001054 | furniture | pages [17] -->
m

<!-- b001055 | furniture | pages [17] -->
m

<!-- b001056 | furniture | pages [17] -->
m

<!-- b001057 | furniture | pages [17] -->
m

<!-- b001058 | furniture | pages [17] -->
m

<!-- b001059 | furniture | pages [17] -->
m

<!-- b001060 | furniture | pages [17] -->
m

<!-- b001061 | furniture | pages [17] -->
m

<!-- b001062 | furniture | pages [17] -->
m

<!-- b001063 | furniture | pages [17] -->
m

<!-- b001064 | furniture | pages [17] -->
m

<!-- b001065 | furniture | pages [17] -->
m

<!-- b001066 | furniture | pages [17] -->
m

<!-- b001067 | furniture | pages [17] -->
m

<!-- b001068 | furniture | pages [17] -->
m

<!-- b001069 | furniture | pages [17] -->
m

<!-- b001070 | furniture | pages [17] -->
m

<!-- b001071 | furniture | pages [17] -->
m

<!-- b001072 | furniture | pages [17] -->
m

<!-- b001073 | furniture | pages [17] -->
m

<!-- b001074 | furniture | pages [17] -->
m

<!-- b001075 | furniture | pages [17] -->
m

<!-- b001076 | furniture | pages [17] -->
m

<!-- b001077 | furniture | pages [17] -->
m

<!-- b001078 | furniture | pages [17] -->
m

<!-- b001079 | furniture | pages [17] -->
m

<!-- b001080 | furniture | pages [17] -->
m

<!-- b001081 | furniture | pages [17] -->
m

<!-- b001082 | furniture | pages [17] -->
m

<!-- b001083 | furniture | pages [17] -->
m

<!-- b001084 | furniture | pages [17] -->
m

<!-- b001085 | furniture | pages [17] -->
m

<!-- b001086 | furniture | pages [17] -->
m

<!-- b001087 | furniture | pages [17] -->
m

<!-- b001088 | furniture | pages [17] -->
m

<!-- b001089 | furniture | pages [17] -->
m

<!-- b001090 | furniture | pages [17] -->
m

<!-- b001091 | furniture | pages [17] -->
m

<!-- b001092 | furniture | pages [17] -->
m

<!-- b001093 | furniture | pages [17] -->
m

<!-- b001094 | furniture | pages [17] -->
m

<!-- b001095 | furniture | pages [17] -->
m

<!-- b001096 | furniture | pages [17] -->
m

<!-- b001097 | furniture | pages [17] -->
m

<!-- b001098 | furniture | pages [17] -->
m

<!-- b001099 | furniture | pages [17] -->
m

<!-- b001100 | furniture | pages [17] -->
m

<!-- b001101 | furniture | pages [17] -->
m

<!-- b001102 | furniture | pages [17] -->
m

<!-- b001103 | furniture | pages [17] -->
m

<!-- b001104 | furniture | pages [17] -->
m

<!-- b001105 | furniture | pages [17] -->
m

<!-- b001106 | furniture | pages [17] -->
m

<!-- b001107 | furniture | pages [17] -->
m

<!-- b001108 | furniture | pages [17] -->
m

<!-- b001109 | furniture | pages [17] -->
m

<!-- b001110 | furniture | pages [17] -->
m

<!-- b001111 | furniture | pages [17] -->
m

<!-- b001112 | furniture | pages [17] -->
m

<!-- b001113 | furniture | pages [17] -->
m

<!-- b001114 | furniture | pages [17] -->
m

<!-- b001115 | furniture | pages [17] -->
m

<!-- b001116 | furniture | pages [17] -->
m

<!-- b001117 | furniture | pages [17] -->
m

<!-- b001118 | furniture | pages [17] -->
m

<!-- b001119 | furniture | pages [17] -->
m

<!-- b001120 | furniture | pages [17] -->
m

<!-- b001121 | furniture | pages [17] -->
m

<!-- b001122 | furniture | pages [17] -->
m

<!-- b001123 | furniture | pages [17] -->
m

<!-- b001124 | furniture | pages [17] -->
m

<!-- b001125 | furniture | pages [17] -->
m

<!-- b001126 | furniture | pages [17] -->
m

<!-- b001127 | furniture | pages [17] -->
m

<!-- b001128 | furniture | pages [17] -->
m

<!-- b001129 | furniture | pages [17] -->
m

<!-- b001130 | furniture | pages [17] -->
m

<!-- b001131 | furniture | pages [17] -->
m

<!-- b001132 | furniture | pages [17] -->
m

<!-- b001133 | furniture | pages [17] -->
m

<!-- b001134 | furniture | pages [17] -->
m

<!-- b001135 | furniture | pages [17] -->
m

<!-- b001136 | furniture | pages [17] -->
m

<!-- b001137 | furniture | pages [17] -->
m

<!-- b001138 | furniture | pages [17] -->
m

<!-- b001139 | furniture | pages [17] -->
m

<!-- b001140 | furniture | pages [17] -->
m

<!-- b001141 | furniture | pages [17] -->
m

<!-- b001142 | furniture | pages [17] -->
m

<!-- b001143 | furniture | pages [17] -->
m

<!-- b001144 | furniture | pages [17] -->
m

<!-- b001145 | furniture | pages [17] -->
m

<!-- b001146 | furniture | pages [17] -->
m

<!-- b001147 | furniture | pages [17] -->
m

<!-- b001148 | furniture | pages [17] -->
m

<!-- b001149 | furniture | pages [17] -->
m

<!-- b001150 | furniture | pages [17] -->
m

<!-- b001151 | furniture | pages [17] -->
m

<!-- b001152 | furniture | pages [17] -->
m

<!-- b001153 | furniture | pages [17] -->
m

<!-- b001154 | furniture | pages [17] -->
m

<!-- b001155 | furniture | pages [17] -->
m

<!-- b001156 | furniture | pages [17] -->
m

<!-- b001157 | furniture | pages [17] -->
m

<!-- b001158 | furniture | pages [17] -->
m

<!-- b001159 | furniture | pages [17] -->
m

<!-- b001160 | furniture | pages [17] -->
m

<!-- b001161 | furniture | pages [17] -->
m

<!-- b001162 | furniture | pages [17] -->
m

<!-- b001163 | furniture | pages [17] -->
m

<!-- b001164 | furniture | pages [17] -->
m

<!-- b001165 | furniture | pages [17] -->
m

<!-- b001166 | furniture | pages [17] -->
m

<!-- b001167 | furniture | pages [17] -->
m

<!-- b001168 | furniture | pages [17] -->
m

<!-- b001169 | furniture | pages [17] -->
m

<!-- b001170 | furniture | pages [17] -->
m

<!-- b001171 | furniture | pages [17] -->
m

<!-- b001172 | furniture | pages [17] -->
m

<!-- b001173 | furniture | pages [17] -->
m

<!-- b001174 | furniture | pages [17] -->
m

<!-- b001175 | furniture | pages [17] -->
m

<!-- b001176 | furniture | pages [17] -->
m

<!-- b001177 | furniture | pages [17] -->
m

<!-- b001178 | furniture | pages [17] -->
m

<!-- b001179 | furniture | pages [17] -->
m

<!-- b001180 | furniture | pages [17] -->
m

<!-- b001181 | furniture | pages [17] -->
m

<!-- b001182 | furniture | pages [17] -->
m

<!-- b001183 | furniture | pages [17] -->
m

<!-- b001184 | furniture | pages [17] -->
m

<!-- b001185 | furniture | pages [17] -->
m

<!-- b001186 | furniture | pages [17] -->
m

<!-- b001187 | furniture | pages [17] -->
m

<!-- b001188 | furniture | pages [17] -->
m

<!-- b001189 | furniture | pages [17] -->
m

<!-- b001190 | furniture | pages [17] -->
m

<!-- b001191 | furniture | pages [17] -->
m

<!-- b001192 | furniture | pages [17] -->
m

<!-- b001193 | furniture | pages [17] -->
m

<!-- b001194 | furniture | pages [17] -->
m

<!-- b001195 | furniture | pages [17] -->
m

<!-- b001196 | furniture | pages [17] -->
m

<!-- b001197 | furniture | pages [17] -->
m

<!-- b001198 | furniture | pages [17] -->
m

<!-- b001199 | furniture | pages [17] -->
m

<!-- b001200 | furniture | pages [17] -->
m

<!-- b001201 | furniture | pages [17] -->
m

<!-- b001202 | furniture | pages [17] -->
m

<!-- b001203 | furniture | pages [17] -->
m

<!-- b001204 | furniture | pages [17] -->
m

<!-- b001205 | furniture | pages [17] -->
m

<!-- b001206 | furniture | pages [17] -->
m

<!-- b001207 | furniture | pages [17] -->
m

<!-- b001208 | furniture | pages [17] -->
m

<!-- b001209 | furniture | pages [17] -->
m

<!-- b001210 | furniture | pages [17] -->
m

<!-- b001211 | furniture | pages [17] -->
m

<!-- b001212 | furniture | pages [17] -->
m

<!-- b001213 | furniture | pages [17] -->
m

<!-- b001214 | furniture | pages [18] -->
Team # 2515235

<!-- b001215 | furniture | pages [18] -->
Page 18 of 26

<!-- b001217 | prose | pages [18] -->
^(𝑿𝒊) represents the predicted outcome for country i’s covariates 𝑿𝒊, which reflects the 𝝁 counterfactual or untreated potential outcome. The double robust estimator provides dual pro- tection: it controls covariates through regression on one hand and adjusts for covariate imbal- ances using weights on the other. Therefore, even if one model (regression or weighting) has errors, the other model ensures consistent estimation.

<!-- b001218 | prose | pages [18] -->
In summary, this model, tailored to the context of the Olympics, overcomes the limitations of traditional Difference-in-Differences (DID) methods—such as self-selection bias, covariate imbalance, and omitted variable bias—by integrating inverse probability weighting (IPW) and the double robust estimator (DR). IPW adjusts for covariate differences between treat- ment and control groups by applying weights to each individual, reducing bias. On the other hand, DR combines weighting and regression models to ensure that, even if one model is mis specified, the other can still provide consistent estimates.

<!-- b001219 | heading | pages [18] -->
6.2 The Solution of Problem 2 by Model 2

<!-- b001220 | heading | pages [18] -->
6.2.1 Illustrate the impact of the great coaching effect

<!-- b001221 | prose | pages [18] -->
Initially, we visualized the "summerOly_athletes.csv" dataset and identified certain pe- riods where countries experienced a sharp increase in medal counts for specific events. This raised the hypothesis that the "great coach effect" might have influenced these periods. Sub- sequently, we examined the history of "great coaches" in these events and their corresponding coaching tenures as a background, to assess whether these periods overlapped with the identi- fied increases in medal counts.

<!-- b001222 | prose | pages [18] -->
We identified several instances in the dataset, such as the Japanese men's saber team, which, after the introduction of "great coach" Erwan Le Pechoux in 2021, saw a remarkable performance improvement, rising from no medals to winning gold in 2024. Additionally, we analyzed three other representative cases: the U.S. women's gymnastics medal data from 1984 to 1996, China's women's field hockey data from 2008 to 2024, and China's women's epee data from 2000 to 2016. In all these cases, the introduction of a "great coach" during the respective periods led to noticeable changes in medal counts. In this context, we extracted the medal data of athletes from the corresponding events during the significant periods of change, where a "great coach" was involved, from the dataset. We then applied the "DRD-CE" model to analyze these data. After testing the relevant model parameters, we confirmed the existence of the "great coach effect".

<!-- b001223 | prose | pages [18] -->
As shown in Table 4, the coefficients of 𝑷𝑪𝒊𝒕 and 𝑷𝑪𝒊𝒕+𝟏 are significantly positive, in- dicating that after the appointment of a new coach, the country's medal count shows a signifi- cant increase during the current and next Olympic cycle. The estimated coefficient of 𝑷𝑪𝒊𝒕−𝟏 is positive but does not reach significance, which may suggest that the effect of medal count improvement after the coach change has not fully manifested in the previous cycle (or imme-

<!-- b001224 | prose | pages [18, 19] -->
关注数学模型 diately after the coach's appointment). Other covariates, such as the home advantage, compe- tition depth, and recent performance, are positively correlated with the increase in medal counts, which aligns with the expected results.  From Table 5, it can be observed that the model fits well, with an R-squared value of 0.756, indicating that the model explains most of the variation in the dependent variable. The F-statistic and the corresponding p-value suggest that the model is overall significant. The AIC and BIC values indicate that the model strikes a good balance

<!-- b001225 | furniture | pages [18] -->
2

<!-- b001226 | furniture | pages [18] -->
MATHmodels

<!-- b001227 | furniture | pages [18] -->
获取更多资讯

<!-- b001228 | furniture | pages [19] -->
Team # 2515235

<!-- b001229 | furniture | pages [19] -->
Page 19 of 26

<!-- b001231 | prose | pages [19] -->
微信公众号：数学模型 微信号：MATHmodels between complexity and fit. The Durbin-Watson value is close to 2, suggesting that there is no significant autocorrelation in the model's residuals. As shown in Table 6, using the doubly robust estimation method, the effect estimates of the "Great Coach Effect" becomes more sig- nificant. In contrast, using the traditional (simple) DID method alone may underestimate the effect or result in insignificant effect estimates due to sample imbalance.

<!-- b001232 | prose | pages [19] -->
6.2.2：Selection of three countries and projects, analysis and results

<!-- b001233 | prose | pages [19, 20] -->
We ultimately selected Japan, Germany, and the United States for analysis, and identi- fied the corresponding projects where investment in "great coaches" could be beneficial. Spe- cifically, Japan could invest in women's gymnastics etc, the United States in women's epee etc, and Germany in women's field hockey and women's epee etc. We recommend that these countries invest in hiring "great coaches" for these specific events to improve their medal counts. The analysis is as follows:

<!-- b001234 | furniture | pages [20] -->
Team # 2515235

<!-- b001235 | furniture | pages [20] -->
Page 20 of 26

<!-- b001237 | prose | pages [20] -->
In terms of country and event selection, we first consider the overall economic strength. We focus only on developed countries and developing countries with the financial capacity to support the costs associated with hiring "great coaches."  Furthermore, using this data, we identify countries in the past three Olympic Games whose rankings in the event were similar to those of the coached country prior to the coach’s involvement. To ensure that the data used for predictions is sufficiently broad and that the "great coach effect" is clearly evident, we selected eight sports with a large number of events or high popularity (e.g., volleyball). Using the aforementioned method, we narrowed the scope to eight countries—Japan, Italy, France, the United Kingdom, Germany, the United States, and China—that can be linked to five spe- cific events: women’s volleyball, men’s saber, women’s gymnastics, women’s epee, and women’s field hockey. We also identified the corresponding "great coaches" for these events, such as Daniel Levavasseur, the coach of China’s women’s epee team who had a notable "great coach effect," and Alyson Annan, the coach of the Netherlands women’s field hockey team. This ensures the relevance and credibility of our results.

<!-- b001238 | prose | pages [20] -->
6.2.3：Prediction of the Performance After Hiring a "Great Coach"

<!-- b001239 | caption | pages [20] -->
Figure 9: Projected line graph after getting the great coaching effect

<!-- b001240 | prose | pages [20] -->
Based on our analysis of the identified events and the coaching tenures of historically successful "great coaches," we found that significant improvements typically occur within a coaching period of four to eight years, which coincides with the Olympic cycle. Therefore, we focused on the subsequent two Olympic Games. According to the results derived from the DRD-CE model, if these three countries introduce the respective "great coaches" for the iden- tified events and undergo a similar coaching period, the performance (expected outcome) in these events is expected to show a noticeable improvement. In the end, it turns out that in their

<!-- b001241 | prose | pages [20, 21] -->
关注数学模型 corresponding events in 2028 and 2032, respectively, the U.S. and Germany are likely to achieve silver, while Japan is expected to win gold.

<!-- b001242 | furniture | pages [20] -->
2

<!-- b001243 | furniture | pages [20] -->
MATHmodels

<!-- b001244 | furniture | pages [20] -->
获取更多资讯

<!-- b001245 | furniture | pages [21] -->
Team # 2515235

<!-- b001246 | furniture | pages [21] -->
Page 21 of 26

<!-- b001248 | heading | pages [21] -->
7 The Solution of Problem 3

<!-- b001249 | heading | pages [21] -->
7.1 Former host effect and Subsequent host effect.

<!-- b001250 | prose | pages [21] -->
In the previous experiments, we identified the "former host effect" and the "subsequent 微信公众号：数学模型 host effect." The "former host effect" refers to the phenomenon where a country, upon learn- ing that it will host the upcoming Olympic Games, performs above its average level in the subsequent Olympic Games until the country hosts its own Olympic Games. The "subsequent host effect" refers to the significant decline in the host country's performance in the following Olympic Games, indicating that the competitive sports strength not only reverts from the "home advantage" to the normal level, but may also drop one or more levels below the nor- mal level. For example, in our previous prediction, Japan, as the host of the 2021 Olympic Games, showed an improvement in performance during the 2016 Rio Olympics. Similarly, as the host of the 2024 Olympics, France experienced a certain degree of performance decline in 微信号：MATHmodels the 2028 Olympic Games.

<!-- b001251 | prose | pages [21] -->
Therefore, in constructing the model, we introduced two new variables,  BE i,t, AF i,t , which represent the impact of the former host effect and the subsequent host effect on the pre- diction results, respectively, and developed a new model.

<!-- b001252 | prose | pages [21] -->
∗= 𝜶+ 𝜷𝟏𝑯𝑬𝒊,𝒕+ 𝜷𝟐𝑵𝑬𝒊,𝒕+ 𝜷𝟑𝑨𝑷𝒊,𝒕+ 𝜷𝟒 𝑩𝑬 𝒊,𝒕+ 𝜷𝟓𝑨𝑭𝒊,𝒕 𝑴𝒊,𝒕 (11) + 𝒅𝟏 𝑬𝑹̅̅̅̅𝒊 + 𝒅𝟐 𝑵𝑴̅̅̅̅̅𝒊+ 𝝀𝒕+ 𝝐𝒊,𝒕

<!-- b001253 | prose | pages [21] -->
For BE i,t, since countries typically know whether they will host the Olympic Games one cycle in advance (on average, 7 years), this variable only impacts the previous Olympic Games. Therefore, we set the value of this variable to 1 if it applies, and 0 if it does not.

<!-- b001254 | prose | pages [21] -->
𝑩𝑭 𝒊,𝒕= {𝟎,    (𝐢𝐬 𝐧𝐨𝐭  𝐭𝐡𝐞 𝐡𝐨𝐬𝐭 𝐨𝐟 𝐭𝐡𝐞 𝐧𝐞𝐱𝐭 𝐆𝐚𝐦𝐞𝐬) (12) 𝟏,    (𝐢𝐬 𝐭𝐡𝐞 𝐡𝐨𝐬𝐭 𝐨𝐟 𝐭𝐡𝐞 𝐧𝐞𝐱𝐭 𝐆𝐚𝐦𝐞𝐬)

<!-- b001255 | prose | pages [21] -->
For  AF i,t, we introduced a "decay factor" to quantify its impact on the subsequent Olym- pic Games after a country becomes the host. The definition is as follows:

<!-- b001256 | prose | pages [21] -->
𝑨𝑭 𝒊,𝒕= 𝐌𝐢,𝐭+𝛍−𝐌𝐢,𝐭 × 𝛅𝛍     (𝛍= 𝟏, 𝟐, 𝟑) (13) 𝐌𝐢,𝐭

<!-- b001257 | prose | pages [21, 22] -->
In this context,𝛅𝛍 represents the decay factor for the μ-th Olympic Games after a country becomes the host, with decreasing values𝜹𝟏= 𝟏 𝜹𝝁= 𝟎. 𝟔  𝜹𝝁= 𝟎. 𝟑 indicating that the per- formance gradually declines in subsequent Olympic Games.After constructing the model, we applied it to predict the results using our original data. We found that, in our prediction for the 2028 Olympic Games, Australia's total medal count increased from the original 45 to 66, which is higher than the 53 medals predicted for the 2024 Paris Olympics. This result further validates the rationale behind the "former host effect" and similar effects from another perspective.

<!-- b001258 | furniture | pages [22] -->
Team # 2515235

<!-- b001259 | furniture | pages [22] -->
Page 22 of 26

<!-- b001261 | caption | pages [22] -->
Figure 10: Host effect influences trends.

<!-- b001262 | heading | pages [22] -->
7.2 Strategies to Enhance Olympic Participation and Global Influence.

<!-- b001263 | prose | pages [22] -->
Using the above method in section 1.3. We derived the most dominant sports for each country along with their respective SCS. The study finds that the fewer the medals, the higher the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m SCS may be. Based on the values of the sport_contribution_score, we categorize countries m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m into groups: Sporting Power Nation (0, 0.25): These countries typically have more than 4 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m dominant sports, indicating strong performance across multiple events with stable overall per- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m formance. Sports Middle-tier Nation [0.25, 0.75): These nations excel in some sports but m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001264 | prose | pages [22] -->
lack consistent competitiveness, resulting in a balanced performance influenced by multiple events. Sports Lagging Nation [0.75, 1]: These countries have a higher SCS, with medals concentrated in a few sports, leading to more specialized performance and weaker overall re- sults. Sports Emerging Nation (0): These countries have an SCS of 0, indicating a lack of significant medal-winning potential and being in the early stages of sports development with limited capacity to compete internationally.To promote the participation of Sports Emerging Nations and Sports Lagging Nations in the Olympics and enhance the global influence of the Games, we propose the following two recommendations to the organizers:

<!-- b001265 | prose | pages [22] -->
Protection of Advantageous Events: For Sports Lagging Nations, we suggest preserving their advantages in specific events and ensuring these countries have more opportunities to participate in those events. By protecting these countries' strong events, their medal perfor- mance can be improved, encouraging more investment in their areas of strength and enhanc- ing overall competitiveness.

<!-- b001266 | prose | pages [22] -->
Addition or Expansion of Events: Based on the traditional strengths and potential of Sports Emerging Nations and Sports Lagging Nations, we recommend adding new Olympic events or increasing the number of entries for these countries in existing events. This would allow

<!-- b001267 | prose | pages [22, 23] -->
关注数学模型 these nations to showcase their advantages in more fields, providing more opportunities for medal contention and motivating more athletes to participate in the Games.

<!-- b001268 | furniture | pages [22] -->
2

<!-- b001269 | furniture | pages [22] -->
MATHmodels

<!-- b001270 | furniture | pages [22] -->
获取更多资讯

<!-- b001271 | furniture | pages [23] -->
Team # 2515235

<!-- b001272 | furniture | pages [23] -->
Page 23 of 26

<!-- b001274 | prose | pages [23] -->
微信公众号：数学模型 微信号：MATHmodels Figure 11．Classification of countries and recommendations.

<!-- b001275 | heading | pages [23] -->
8 Sensitivity Analysis

<!-- b001276 | prose | pages [23] -->
The content you described is primarily intended to test the sensitivity of the model and to ver- ify its accuracy and stability by comparing the medal predictions with different weight set- tings. Here is a more professional expression:In solving Question 1, for the calculation of the total number of medals, we first calculated the number of gold, silver, and bronze medals sep- arately using the TMP-OMP model, and then summed these to obtain the total number of medals. To further validate the model's sensitivity, we could set the weights for gold, silver, and bronze to 1 and re-run the model to obtain a new total medal count. We then compare the two methods to test the model's sensitivity to changes in medal weights.

<!-- b001277 | prose | pages [23] -->
Taking the United States as an example, in the solution to Question 1, we obtained the num- ber of gold medals as 51, silver medals as 50, and bronze medals as 47, resulting in a total of 148 medals. After performing the sensitivity test by setting the weights for all medal types to 1, the recalculated total number of medals for the United States was 142, with an error of 4.054% (compared to the original result of 148 medals). This error indicates that the model has a high sensitivity to changes in medal weights, and the results remain relatively stable, suggesting that the model performs well in predicting total medal counts. To further verify the

<!-- b001278 | prose | pages [23, 24] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m stability of the model, we conducted a sensitivity analysis for the top 10 countries. The re- sults showed that the error values for all countries were less than 0.16, indicating that the

<!-- b001279 | furniture | pages [23] -->
m

<!-- b001280 | furniture | pages [23] -->
m

<!-- b001281 | furniture | pages [23] -->
m

<!-- b001282 | furniture | pages [23] -->
m

<!-- b001283 | furniture | pages [23] -->
m

<!-- b001284 | furniture | pages [23] -->
m

<!-- b001285 | furniture | pages [23] -->
m

<!-- b001286 | furniture | pages [23] -->
m

<!-- b001287 | furniture | pages [23] -->
m

<!-- b001288 | furniture | pages [23] -->
m

<!-- b001289 | furniture | pages [23] -->
m

<!-- b001290 | furniture | pages [23] -->
m

<!-- b001291 | furniture | pages [23] -->
m

<!-- b001292 | furniture | pages [23] -->
m

<!-- b001293 | furniture | pages [23] -->
m

<!-- b001294 | furniture | pages [23] -->
m

<!-- b001295 | furniture | pages [23] -->
m

<!-- b001296 | furniture | pages [23] -->
m

<!-- b001297 | furniture | pages [23] -->
m

<!-- b001298 | furniture | pages [23] -->
m

<!-- b001299 | furniture | pages [23] -->
m

<!-- b001300 | furniture | pages [23] -->
m

<!-- b001301 | furniture | pages [23] -->
m

<!-- b001302 | furniture | pages [23] -->
m

<!-- b001303 | furniture | pages [23] -->
m

<!-- b001304 | furniture | pages [23] -->
m

<!-- b001305 | furniture | pages [23] -->
m

<!-- b001306 | furniture | pages [23] -->
m

<!-- b001307 | furniture | pages [23] -->
m

<!-- b001308 | furniture | pages [23] -->
m

<!-- b001309 | furniture | pages [23] -->
m

<!-- b001310 | furniture | pages [23] -->
m

<!-- b001311 | furniture | pages [23] -->
m

<!-- b001312 | furniture | pages [23] -->
m

<!-- b001313 | furniture | pages [23] -->
m

<!-- b001314 | furniture | pages [23] -->
m

<!-- b001315 | furniture | pages [23] -->
m

<!-- b001316 | furniture | pages [23] -->
m

<!-- b001317 | furniture | pages [23] -->
m

<!-- b001318 | furniture | pages [23] -->
m

<!-- b001319 | furniture | pages [23] -->
m

<!-- b001320 | furniture | pages [23] -->
m

<!-- b001321 | furniture | pages [23] -->
m

<!-- b001322 | furniture | pages [23] -->
m

<!-- b001323 | furniture | pages [23] -->
m

<!-- b001324 | furniture | pages [23] -->
m

<!-- b001325 | furniture | pages [23] -->
m

<!-- b001326 | furniture | pages [23] -->
m

<!-- b001327 | furniture | pages [23] -->
m

<!-- b001328 | furniture | pages [23] -->
m

<!-- b001329 | furniture | pages [23] -->
m

<!-- b001330 | furniture | pages [23] -->
m

<!-- b001331 | furniture | pages [23] -->
m

<!-- b001332 | furniture | pages [23] -->
m

<!-- b001333 | furniture | pages [23] -->
m

<!-- b001334 | furniture | pages [23] -->
m

<!-- b001335 | furniture | pages [23] -->
m

<!-- b001336 | furniture | pages [23] -->
m

<!-- b001337 | furniture | pages [23] -->
m

<!-- b001338 | furniture | pages [23] -->
m

<!-- b001339 | furniture | pages [23] -->
m

<!-- b001340 | furniture | pages [23] -->
m

<!-- b001341 | furniture | pages [23] -->
m

<!-- b001342 | furniture | pages [23] -->
m

<!-- b001343 | furniture | pages [23] -->
m

<!-- b001344 | furniture | pages [23] -->
m

<!-- b001345 | furniture | pages [23] -->
m

<!-- b001346 | furniture | pages [23] -->
m

<!-- b001347 | furniture | pages [23] -->
m

<!-- b001348 | furniture | pages [23] -->
m

<!-- b001349 | furniture | pages [23] -->
m

<!-- b001350 | furniture | pages [23] -->
m

<!-- b001351 | furniture | pages [23] -->
m

<!-- b001352 | furniture | pages [23] -->
m

<!-- b001353 | furniture | pages [23] -->
m

<!-- b001354 | furniture | pages [23] -->
m

<!-- b001355 | furniture | pages [23] -->
m

<!-- b001356 | furniture | pages [23] -->
m

<!-- b001357 | furniture | pages [23] -->
m

<!-- b001358 | furniture | pages [23] -->
m

<!-- b001359 | furniture | pages [23] -->
m

<!-- b001360 | furniture | pages [23] -->
m

<!-- b001361 | furniture | pages [23] -->
m

<!-- b001362 | furniture | pages [23] -->
m

<!-- b001363 | furniture | pages [23] -->
m

<!-- b001364 | furniture | pages [23] -->
m

<!-- b001365 | furniture | pages [23] -->
m

<!-- b001366 | furniture | pages [23] -->
m

<!-- b001367 | furniture | pages [23] -->
m

<!-- b001368 | furniture | pages [23] -->
m

<!-- b001369 | furniture | pages [23] -->
m

<!-- b001370 | furniture | pages [23] -->
m

<!-- b001371 | furniture | pages [23] -->
m

<!-- b001372 | furniture | pages [23] -->
m

<!-- b001373 | furniture | pages [23] -->
m

<!-- b001374 | furniture | pages [23] -->
m

<!-- b001375 | furniture | pages [23] -->
m

<!-- b001376 | furniture | pages [23] -->
m

<!-- b001377 | furniture | pages [23] -->
m

<!-- b001378 | furniture | pages [23] -->
m

<!-- b001379 | furniture | pages [23] -->
m

<!-- b001380 | furniture | pages [23] -->
m

<!-- b001381 | furniture | pages [23] -->
m

<!-- b001382 | furniture | pages [23] -->
m

<!-- b001383 | furniture | pages [23] -->
m

<!-- b001384 | furniture | pages [23] -->
m

<!-- b001385 | furniture | pages [23] -->
m

<!-- b001386 | furniture | pages [23] -->
m

<!-- b001387 | furniture | pages [23] -->
m

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

<!-- b001603 | furniture | pages [24] -->
Team # 2515235

<!-- b001604 | furniture | pages [24] -->
Page 24 of 26

<!-- b001606 | caption | pages [24] -->
Figure 12: Sensitivity analysis results

<!-- b001607 | prose | pages [24] -->
model has high prediction accuracy for different countries, with a small error range, demon- strating good stability and reliability. The final results, as shown in the following chart, fur- ther validate the model's accuracy and sensitivity under different weight settings.

<!-- b001608 | heading | pages [24] -->
9 Model Evaluation and Further Discussion

<!-- b001609 | heading | pages [24] -->
9.1 Strengths

<!-- b001610 | heading | pages [24] -->
The Advantages of Two Model:

<!-- b001611 | prose | pages [24] -->
⚫ Medal Censoring Handling: The Tobit regression is used to address the censoring prob- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m lem of countries with zero medal counts, improving prediction accuracy for nations with- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m out medals. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ⚫ Control of Country-Specific Effects: The Mundlak correction is applied, integrating m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m long-term country features (such as host nation effects, participation rate, average medal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001612 | prose | pages [24] -->
count, etc.) to effectively control for time-invariant country characteristics and enhance prediction accuracy. ⚫

<!-- b001613 | heading | pages [24] -->
Double Robust Estimation (DR): Combines regression and weighting models to pro-

<!-- b001614 | prose | pages [24] -->
vide consistent estimates even if one model is misspecified, enhancing the model's relia- bility. ⚫ Flexibility: The dynamic DID approach accommodates varying time points and multiple treatment groups, making the analysis both precise and widely applicable.

<!-- b001615 | prose | pages [24] -->
关注数学模型

<!-- b001616 | furniture | pages [24] -->
2

<!-- b001617 | furniture | pages [24] -->
MATHmodels

<!-- b001618 | furniture | pages [24] -->
获取更多资讯

<!-- b001619 | furniture | pages [25] -->
Team # 2515235

<!-- b001620 | furniture | pages [25] -->
Page 25 of 26

<!-- b001621 | heading | pages [25] -->
9.2 Weaknesses and Further Discussion

<!-- b001622 | prose | pages [25] -->
⚫ While the current model’s accuracy can still be improved, future efforts could focus on incorporating additional country-level data, such as population size and GDP. These macroeconomic indicators can provide a more comprehensive understanding of a na- tion's overall strength and its potential impact on Olympic medal performance, thereby 微信公众号：数学模型 improving prediction accuracy. ⚫ The model currently relies on medal counts to evaluate athlete performance and predict future medal outcomes. To better assess athletes' true performance, future data collection should focus on athletes in the top 16, which will allow for a more nuanced analysis of their capabilities and provide more professional insights for medal predictions.

<!-- b001623 | heading | pages [25] -->
10 References

<!-- b001624 | references | pages [25] -->
微信号：MATHmodels

<!-- b001625 | references | pages [25] -->
[1]. S. Seiler, "Evaluating the (your country here) Olympic medal count," Int. J. Sports Phys-

<!-- b001626 | references | pages [25] -->
iol. Perform., vol. 8, no. 2, pp. 203-210, 2013.

<!-- b001627 | references | pages [25] -->
[2]. X. Bian, "Predicting Olympic medal counts: The effects of economic development on

<!-- b001628 | references | pages [25] -->
Olympic performance," The Park Place Economist, vol. 13, no. 1, pp. 37-44, 2005.

<!-- b001629 | references | pages [25] -->
[3]. C. Schlembach, S. L. Schmidt, D. Schreyer, et al., "Forecasting the Olympic medal dis-

<!-- b001630 | references | pages [25] -->
tribution–a socioeconomic machine learning model," Technol. Forecast. Soc. Change,

<!-- b001631 | references | pages [25] -->
vol. 175, p. 121314, 2022.

<!-- b001632 | references | pages [25] -->
[4]. F. Fan and X. Zhang, "Transformation effect of resource-based cities based on PSM-DID

<!-- b001633 | references | pages [25] -->
model: An empirical analysis from China," Environ. Impact Assess. Rev., vol. 91, p.

<!-- b001634 | references | pages [25] -->
106648, 2021.

<!-- b001635 | references | pages [25] -->
[5]. A. Xu, M. Song, Y. Wu, et al., "Effects of new urbanization on China's carbon emissions:

<!-- b001636 | references | pages [25] -->
A quasi-natural experiment based on the improved PSM-DID model," Technol. Forecast.

<!-- b001637 | references | pages [25] -->
Soc. Change, vol. 200, p. 123164, 2024.

<!-- b001638 | references | pages [25] -->
[6]. T. E. Thiele and M. Navarro, "Drinking in the dark (DID) procedures: A model of binge-

<!-- b001639 | references | pages [25] -->
like ethanol drinking in non-dependent mice," Alcohol, vol. 48, no. 3, pp. 235-241, 2014.

<!-- b001640 | references | pages [25] -->
m

<!-- b001641 | references | pages [25] -->
m

<!-- b001642 | references | pages [25] -->
m

<!-- b001643 | references | pages [25] -->
m

<!-- b001644 | references | pages [25] -->
m

<!-- b001645 | references | pages [25] -->
m

<!-- b001646 | references | pages [25] -->
m

<!-- b001647 | references | pages [25] -->
m

<!-- b001648 | references | pages [25] -->
m

<!-- b001649 | references | pages [25] -->
m

<!-- b001650 | references | pages [25] -->
m

<!-- b001651 | references | pages [25] -->
m

<!-- b001652 | references | pages [25] -->
m

<!-- b001653 | references | pages [25] -->
m

<!-- b001654 | references | pages [25] -->
m

<!-- b001655 | references | pages [25] -->
m

<!-- b001656 | references | pages [25] -->
m

<!-- b001657 | references | pages [25] -->
m

<!-- b001658 | references | pages [25] -->
m

<!-- b001659 | references | pages [25] -->
m

<!-- b001660 | references | pages [25] -->
m

<!-- b001661 | references | pages [25] -->
m

<!-- b001662 | references | pages [25] -->
m

<!-- b001663 | references | pages [25] -->
m

<!-- b001664 | references | pages [25] -->
m

<!-- b001665 | references | pages [25] -->
m

<!-- b001666 | references | pages [25] -->
m

<!-- b001667 | references | pages [25] -->
m

<!-- b001668 | references | pages [25] -->
m

<!-- b001669 | references | pages [25] -->
m

<!-- b001670 | references | pages [25] -->
m

<!-- b001671 | references | pages [25] -->
m

<!-- b001672 | references | pages [25] -->
m

<!-- b001673 | references | pages [25] -->
m

<!-- b001674 | references | pages [25] -->
m

<!-- b001675 | references | pages [25] -->
m

<!-- b001676 | references | pages [25] -->
m

<!-- b001677 | references | pages [25] -->
m

<!-- b001678 | references | pages [25] -->
m

<!-- b001679 | references | pages [25] -->
m

<!-- b001680 | references | pages [25] -->
m

<!-- b001681 | references | pages [25] -->
m

<!-- b001682 | references | pages [25] -->
m

<!-- b001683 | references | pages [25] -->
m

<!-- b001684 | references | pages [25] -->
m

<!-- b001685 | references | pages [25] -->
m

<!-- b001686 | references | pages [25] -->
m

<!-- b001687 | references | pages [25] -->
m

<!-- b001688 | references | pages [25] -->
m

<!-- b001689 | references | pages [25] -->
m

<!-- b001690 | references | pages [25] -->
m

<!-- b001691 | references | pages [25] -->
m

<!-- b001692 | references | pages [25] -->
m

<!-- b001693 | references | pages [25] -->
m

<!-- b001694 | references | pages [25] -->
m

<!-- b001695 | references | pages [25] -->
m

<!-- b001696 | references | pages [25] -->
m

<!-- b001697 | references | pages [25] -->
m

<!-- b001698 | references | pages [25] -->
m

<!-- b001699 | references | pages [25] -->
m

<!-- b001700 | references | pages [25] -->
m

<!-- b001701 | references | pages [25] -->
m

<!-- b001702 | references | pages [25] -->
m

<!-- b001703 | references | pages [25] -->
m

<!-- b001704 | references | pages [25] -->
m

<!-- b001705 | references | pages [25] -->
m

<!-- b001706 | references | pages [25] -->
m

<!-- b001707 | references | pages [25] -->
m

<!-- b001708 | references | pages [25] -->
m

<!-- b001709 | references | pages [25] -->
m

<!-- b001710 | references | pages [25] -->
m

<!-- b001711 | references | pages [25] -->
m

<!-- b001712 | references | pages [25] -->
m

<!-- b001713 | references | pages [25] -->
m

<!-- b001714 | references | pages [25] -->
m

<!-- b001715 | references | pages [25] -->
m

<!-- b001716 | references | pages [25] -->
m

<!-- b001717 | references | pages [25] -->
m

<!-- b001718 | references | pages [25] -->
m

<!-- b001719 | references | pages [25] -->
m

<!-- b001720 | references | pages [25] -->
m

<!-- b001721 | references | pages [25] -->
m

<!-- b001722 | references | pages [25] -->
m

<!-- b001723 | references | pages [25] -->
m

<!-- b001724 | references | pages [25] -->
m

<!-- b001725 | references | pages [25] -->
m

<!-- b001726 | references | pages [25] -->
m

<!-- b001727 | references | pages [25] -->
m

<!-- b001728 | references | pages [25] -->
m

<!-- b001729 | references | pages [25] -->
m

<!-- b001730 | references | pages [25] -->
m

<!-- b001731 | references | pages [25] -->
m

<!-- b001732 | references | pages [25] -->
m

<!-- b001733 | references | pages [25] -->
m

<!-- b001734 | references | pages [25] -->
m

<!-- b001735 | references | pages [25] -->
m

<!-- b001736 | references | pages [25] -->
m

<!-- b001737 | references | pages [25] -->
m

<!-- b001738 | references | pages [25] -->
m

<!-- b001739 | references | pages [25] -->
m

<!-- b001740 | references | pages [25] -->
m

<!-- b001741 | references | pages [25] -->
m

<!-- b001742 | references | pages [25] -->
m

<!-- b001743 | references | pages [25] -->
m

<!-- b001744 | references | pages [25] -->
m

<!-- b001745 | references | pages [25] -->
m

<!-- b001746 | references | pages [25] -->
m

<!-- b001747 | references | pages [25] -->
m

<!-- b001748 | references | pages [25] -->
m

<!-- b001749 | references | pages [25] -->
m

<!-- b001750 | references | pages [25] -->
m

<!-- b001751 | references | pages [25] -->
m

<!-- b001752 | references | pages [25] -->
m

<!-- b001753 | references | pages [25] -->
m

<!-- b001754 | references | pages [25] -->
m

<!-- b001755 | references | pages [25] -->
m

<!-- b001756 | references | pages [25] -->
m

<!-- b001757 | references | pages [25] -->
m

<!-- b001758 | references | pages [25] -->
m

<!-- b001759 | references | pages [25] -->
m

<!-- b001760 | references | pages [25] -->
m

<!-- b001761 | references | pages [25] -->
m

<!-- b001762 | references | pages [25] -->
m

<!-- b001763 | references | pages [25] -->
m

<!-- b001764 | references | pages [25] -->
m

<!-- b001765 | references | pages [25] -->
m

<!-- b001766 | references | pages [25] -->
m

<!-- b001767 | references | pages [25] -->
m

<!-- b001768 | references | pages [25] -->
m

<!-- b001769 | references | pages [25] -->
m

<!-- b001770 | references | pages [25] -->
m

<!-- b001771 | references | pages [25] -->
m

<!-- b001772 | references | pages [25] -->
m

<!-- b001773 | references | pages [25] -->
m

<!-- b001774 | references | pages [25] -->
m

<!-- b001775 | references | pages [25] -->
m

<!-- b001776 | references | pages [25] -->
m

<!-- b001777 | references | pages [25] -->
m

<!-- b001778 | references | pages [25] -->
m

<!-- b001779 | references | pages [25] -->
m

<!-- b001780 | references | pages [25] -->
m

<!-- b001781 | references | pages [25] -->
m

<!-- b001782 | references | pages [25] -->
m

<!-- b001783 | references | pages [25] -->
m

<!-- b001784 | references | pages [25] -->
m

<!-- b001785 | references | pages [25] -->
m

<!-- b001786 | references | pages [25] -->
m

<!-- b001787 | references | pages [25] -->
m

<!-- b001788 | references | pages [25] -->
m

<!-- b001789 | references | pages [25] -->
m

<!-- b001790 | references | pages [25] -->
m

<!-- b001791 | references | pages [25] -->
m

<!-- b001792 | references | pages [25] -->
m

<!-- b001793 | references | pages [25] -->
m

<!-- b001794 | references | pages [25] -->
m

<!-- b001795 | references | pages [25] -->
m

<!-- b001796 | references | pages [25] -->
m

<!-- b001797 | references | pages [25] -->
m

<!-- b001798 | references | pages [25] -->
m

<!-- b001799 | references | pages [25] -->
m

<!-- b001800 | references | pages [25] -->
m

<!-- b001801 | references | pages [25] -->
m

<!-- b001802 | references | pages [25] -->
m

<!-- b001803 | references | pages [25] -->
m

<!-- b001804 | references | pages [25] -->
m

<!-- b001805 | references | pages [25] -->
m

<!-- b001806 | references | pages [25] -->
m

<!-- b001807 | references | pages [25] -->
m

<!-- b001808 | references | pages [25] -->
m

<!-- b001809 | references | pages [25] -->
m

<!-- b001810 | references | pages [25] -->
m

<!-- b001811 | references | pages [25] -->
m

<!-- b001812 | references | pages [25] -->
m

<!-- b001813 | references | pages [25] -->
m

<!-- b001814 | references | pages [25] -->
m

<!-- b001815 | references | pages [25] -->
m

<!-- b001816 | references | pages [25] -->
m

<!-- b001817 | references | pages [25] -->
m

<!-- b001818 | references | pages [25] -->
m

<!-- b001819 | references | pages [25] -->
m

<!-- b001820 | references | pages [25] -->
m

<!-- b001821 | references | pages [25] -->
m

<!-- b001822 | references | pages [25] -->
m

<!-- b001823 | references | pages [25] -->
m

<!-- b001824 | references | pages [25] -->
m

<!-- b001825 | references | pages [25] -->
m

<!-- b001826 | references | pages [25] -->
m

<!-- b001827 | references | pages [25] -->
m

<!-- b001828 | references | pages [25] -->
m

<!-- b001829 | references | pages [25] -->
m

<!-- b001830 | references | pages [25] -->
m

<!-- b001831 | references | pages [25] -->
m

<!-- b001832 | references | pages [25] -->
m

<!-- b001833 | references | pages [25] -->
m

<!-- b001834 | references | pages [25] -->
m

<!-- b001835 | references | pages [25] -->
m

<!-- b001836 | references | pages [25] -->
m

<!-- b001837 | references | pages [25] -->
m

<!-- b001838 | references | pages [25] -->
m

<!-- b001839 | references | pages [25] -->
m

<!-- b001840 | references | pages [25] -->
m

<!-- b001841 | references | pages [25] -->
m

<!-- b001842 | references | pages [25] -->
m

<!-- b001843 | references | pages [25] -->
m

<!-- b001844 | references | pages [25] -->
m

<!-- b001845 | references | pages [25] -->
m

<!-- b001846 | references | pages [25] -->
m

<!-- b001847 | references | pages [25] -->
m

<!-- b001848 | references | pages [25] -->
m

<!-- b001849 | references | pages [25] -->
m

<!-- b001850 | references | pages [25] -->
m

<!-- b001851 | references | pages [25] -->
m

<!-- b001852 | references | pages [25] -->
m

<!-- b001853 | references | pages [25] -->
m

<!-- b001854 | references | pages [25] -->
m

<!-- b001855 | references | pages [25] -->
m

<!-- b001856 | references | pages [25] -->
m

<!-- b001857 | references | pages [25] -->
m

<!-- b001858 | references | pages [25] -->
m

<!-- b001859 | references | pages [25] -->
m

<!-- b001860 | references | pages [25] -->
m

<!-- b001861 | references | pages [25] -->
m

<!-- b001862 | references | pages [25] -->
m

<!-- b001863 | references | pages [25] -->
m

<!-- b001864 | references | pages [25] -->
m

<!-- b001865 | references | pages [25] -->
m

<!-- b001866 | references | pages [25] -->
m

<!-- b001867 | references | pages [25] -->
m

<!-- b001868 | references | pages [25] -->
m

<!-- b001869 | references | pages [25] -->
m

<!-- b001870 | furniture | pages [25] -->
m

<!-- b001871 | furniture | pages [25] -->
m

<!-- b001872 | furniture | pages [25] -->
m

<!-- b001873 | furniture | pages [25] -->
m

<!-- b001874 | furniture | pages [25] -->
m

<!-- b001875 | furniture | pages [25] -->
m

<!-- b001876 | furniture | pages [25] -->
m

<!-- b001877 | furniture | pages [25] -->
m

<!-- b001878 | furniture | pages [25] -->
m

<!-- b001879 | furniture | pages [25] -->
m

<!-- b001880 | furniture | pages [25] -->
m

<!-- b001881 | furniture | pages [25] -->
m

<!-- b001882 | furniture | pages [25] -->
m

<!-- b001883 | furniture | pages [25] -->
m

<!-- b001884 | furniture | pages [25] -->
m

<!-- b001885 | furniture | pages [25] -->
m

<!-- b001886 | furniture | pages [25] -->
m

<!-- b001887 | furniture | pages [25] -->
m

<!-- b001888 | furniture | pages [25] -->
m

<!-- b001889 | furniture | pages [25] -->
m

<!-- b001890 | furniture | pages [25] -->
m

<!-- b001891 | furniture | pages [25] -->
m

<!-- b001892 | furniture | pages [25] -->
m

<!-- b001893 | furniture | pages [25] -->
m

<!-- b001894 | furniture | pages [25] -->
m

<!-- b001895 | furniture | pages [25] -->
m

<!-- b001896 | furniture | pages [25] -->
m

<!-- b001897 | furniture | pages [25] -->
m

<!-- b001898 | furniture | pages [25] -->
m

<!-- b001899 | furniture | pages [25] -->
m

<!-- b001900 | furniture | pages [25] -->
m

<!-- b001901 | furniture | pages [25] -->
m

<!-- b001902 | furniture | pages [25] -->
m

<!-- b001903 | furniture | pages [25] -->
m

<!-- b001904 | furniture | pages [25] -->
m

<!-- b001905 | furniture | pages [25] -->
m

<!-- b001906 | furniture | pages [25] -->
m

<!-- b001907 | furniture | pages [25] -->
m

<!-- b001908 | furniture | pages [25] -->
m

<!-- b001909 | furniture | pages [25] -->
m

<!-- b001910 | furniture | pages [25] -->
m

<!-- b001911 | furniture | pages [25] -->
m

<!-- b001912 | furniture | pages [25] -->
m

<!-- b001913 | furniture | pages [25] -->
m

<!-- b001914 | furniture | pages [25] -->
m

<!-- b001915 | furniture | pages [25] -->
m

<!-- b001916 | furniture | pages [25] -->
m

<!-- b001917 | furniture | pages [25] -->
m

<!-- b001918 | furniture | pages [25] -->
m

<!-- b001919 | furniture | pages [25] -->
m

<!-- b001920 | furniture | pages [25] -->
m

<!-- b001921 | furniture | pages [25] -->
m

<!-- b001922 | furniture | pages [25] -->
m

<!-- b001923 | furniture | pages [25] -->
m

<!-- b001924 | furniture | pages [25] -->
m

<!-- b001925 | furniture | pages [25] -->
m

<!-- b001926 | furniture | pages [25] -->
m

<!-- b001927 | furniture | pages [25] -->
m

<!-- b001928 | furniture | pages [25] -->
m

<!-- b001929 | furniture | pages [25] -->
m

<!-- b001930 | furniture | pages [25] -->
m

<!-- b001931 | furniture | pages [25] -->
m

<!-- b001932 | furniture | pages [25] -->
m

<!-- b001933 | furniture | pages [25] -->
m

<!-- b001934 | furniture | pages [25] -->
m

<!-- b001935 | furniture | pages [25] -->
m

<!-- b001936 | furniture | pages [25] -->
m

<!-- b001937 | furniture | pages [25] -->
m

<!-- b001938 | furniture | pages [25] -->
m

<!-- b001939 | furniture | pages [25] -->
m

<!-- b001940 | furniture | pages [25] -->
m

<!-- b001941 | furniture | pages [25] -->
m

<!-- b001942 | furniture | pages [25] -->
m

<!-- b001943 | furniture | pages [25] -->
m

<!-- b001944 | furniture | pages [25] -->
m

<!-- b001945 | furniture | pages [25] -->
m

<!-- b001946 | furniture | pages [25] -->
m

<!-- b001947 | furniture | pages [25] -->
m

<!-- b001948 | furniture | pages [25] -->
m

<!-- b001949 | furniture | pages [25] -->
m

<!-- b001950 | furniture | pages [25] -->
m

<!-- b001951 | furniture | pages [25] -->
m

<!-- b001952 | furniture | pages [25] -->
m

<!-- b001953 | furniture | pages [25] -->
m

<!-- b001954 | furniture | pages [25] -->
m

<!-- b001955 | furniture | pages [25] -->
m

<!-- b001956 | furniture | pages [25] -->
m

<!-- b001957 | furniture | pages [25] -->
m

<!-- b001958 | furniture | pages [25] -->
m

<!-- b001959 | furniture | pages [25] -->
m

<!-- b001960 | furniture | pages [25] -->
m

<!-- b001961 | furniture | pages [25] -->
m

<!-- b001962 | furniture | pages [25] -->
m

<!-- b001963 | furniture | pages [25] -->
m

<!-- b001964 | furniture | pages [25] -->
m

<!-- b001965 | furniture | pages [25] -->
m

<!-- b001966 | furniture | pages [25] -->
m

<!-- b001967 | furniture | pages [25] -->
m

<!-- b001968 | furniture | pages [25] -->
m

<!-- b001969 | furniture | pages [25] -->
m

<!-- b001970 | furniture | pages [25] -->
m

<!-- b001971 | furniture | pages [25] -->
m

<!-- b001972 | furniture | pages [25] -->
m

<!-- b001973 | furniture | pages [25] -->
m

<!-- b001974 | furniture | pages [25] -->
m

<!-- b001975 | furniture | pages [25] -->
m

<!-- b001976 | furniture | pages [25] -->
m

<!-- b001977 | furniture | pages [25] -->
m

<!-- b001978 | furniture | pages [25] -->
m

<!-- b001979 | furniture | pages [25] -->
m

<!-- b001980 | furniture | pages [25] -->
m

<!-- b001981 | furniture | pages [25] -->
m

<!-- b001982 | furniture | pages [25] -->
m

<!-- b001983 | furniture | pages [25] -->
m

<!-- b001984 | furniture | pages [25] -->
m

<!-- b001985 | furniture | pages [25] -->
m

<!-- b001986 | furniture | pages [25] -->
m

<!-- b001987 | furniture | pages [25] -->
m

<!-- b001988 | furniture | pages [25] -->
m

<!-- b001989 | furniture | pages [25] -->
m

<!-- b001990 | furniture | pages [25] -->
m

<!-- b001991 | furniture | pages [25] -->
m

<!-- b001992 | furniture | pages [25] -->
m

<!-- b001993 | furniture | pages [25] -->
m

<!-- b001994 | furniture | pages [25] -->
m

<!-- b001995 | furniture | pages [25] -->
m

<!-- b001996 | furniture | pages [25] -->
m

<!-- b001997 | furniture | pages [25] -->
m

<!-- b001998 | furniture | pages [25] -->
m

<!-- b001999 | furniture | pages [25] -->
m

<!-- b002000 | furniture | pages [25] -->
m

<!-- b002001 | furniture | pages [25] -->
m

<!-- b002002 | furniture | pages [25] -->
m

<!-- b002003 | furniture | pages [25] -->
m

<!-- b002004 | furniture | pages [25] -->
m

<!-- b002005 | furniture | pages [25] -->
m

<!-- b002006 | furniture | pages [25] -->
m

<!-- b002007 | furniture | pages [25] -->
m

<!-- b002008 | furniture | pages [25] -->
m

<!-- b002009 | furniture | pages [25] -->
m

<!-- b002010 | furniture | pages [25] -->
m

<!-- b002011 | furniture | pages [25] -->
m

<!-- b002012 | furniture | pages [25] -->
m

<!-- b002013 | furniture | pages [25] -->
m

<!-- b002014 | furniture | pages [25] -->
m

<!-- b002015 | furniture | pages [25] -->
m

<!-- b002016 | furniture | pages [25] -->
m

<!-- b002017 | furniture | pages [25] -->
m

<!-- b002018 | furniture | pages [25] -->
m

<!-- b002019 | furniture | pages [25] -->
m

<!-- b002020 | furniture | pages [25] -->
m

<!-- b002021 | furniture | pages [25] -->
m

<!-- b002022 | furniture | pages [25] -->
m

<!-- b002023 | furniture | pages [25] -->
m

<!-- b002024 | furniture | pages [25] -->
m

<!-- b002025 | furniture | pages [25] -->
m

<!-- b002026 | furniture | pages [25] -->
m

<!-- b002027 | furniture | pages [25] -->
m

<!-- b002028 | furniture | pages [25] -->
m

<!-- b002029 | furniture | pages [25] -->
m

<!-- b002030 | furniture | pages [25] -->
m

<!-- b002031 | furniture | pages [25] -->
m

<!-- b002032 | furniture | pages [25] -->
m

<!-- b002033 | furniture | pages [25] -->
m

<!-- b002034 | furniture | pages [25] -->
m

<!-- b002035 | furniture | pages [25] -->
m

<!-- b002036 | furniture | pages [25] -->
m

<!-- b002037 | furniture | pages [25] -->
m

<!-- b002038 | furniture | pages [25] -->
m

<!-- b002039 | furniture | pages [25] -->
m

<!-- b002040 | furniture | pages [25] -->
m

<!-- b002041 | furniture | pages [25] -->
m

<!-- b002042 | furniture | pages [25] -->
m

<!-- b002043 | furniture | pages [25] -->
m

<!-- b002044 | furniture | pages [25] -->
m

<!-- b002045 | furniture | pages [25] -->
m

<!-- b002046 | furniture | pages [25] -->
m

<!-- b002047 | furniture | pages [25] -->
m

<!-- b002048 | furniture | pages [25] -->
m

<!-- b002049 | furniture | pages [25] -->
m

<!-- b002050 | furniture | pages [25] -->
m

<!-- b002051 | furniture | pages [25] -->
m

<!-- b002052 | furniture | pages [25] -->
m

<!-- b002053 | furniture | pages [25] -->
m

<!-- b002054 | furniture | pages [25] -->
m

<!-- b002055 | furniture | pages [25] -->
m

<!-- b002056 | furniture | pages [25] -->
m

<!-- b002057 | furniture | pages [25] -->
m

<!-- b002058 | furniture | pages [25] -->
m

<!-- b002059 | furniture | pages [25] -->
m

<!-- b002060 | furniture | pages [25] -->
m

<!-- b002061 | furniture | pages [25] -->
m

<!-- b002062 | furniture | pages [25] -->
m

<!-- b002063 | furniture | pages [25] -->
m

<!-- b002064 | furniture | pages [25] -->
m

<!-- b002065 | furniture | pages [25] -->
m

<!-- b002066 | furniture | pages [25] -->
m

<!-- b002067 | furniture | pages [25] -->
m

<!-- b002068 | furniture | pages [25] -->
m

<!-- b002069 | furniture | pages [25] -->
m

<!-- b002070 | furniture | pages [25] -->
m

<!-- b002071 | furniture | pages [25] -->
m

<!-- b002072 | furniture | pages [25] -->
m

<!-- b002073 | furniture | pages [25] -->
m

<!-- b002074 | furniture | pages [25] -->
m

<!-- b002075 | furniture | pages [25] -->
m

<!-- b002076 | furniture | pages [25] -->
m

<!-- b002077 | furniture | pages [25] -->
m

<!-- b002078 | furniture | pages [25] -->
m

<!-- b002079 | furniture | pages [25] -->
m

<!-- b002080 | furniture | pages [25] -->
m

<!-- b002081 | furniture | pages [25] -->
m

<!-- b002082 | furniture | pages [25] -->
m

<!-- b002083 | furniture | pages [25] -->
m

<!-- b002084 | furniture | pages [25] -->
m

<!-- b002085 | furniture | pages [25] -->
m

<!-- b002086 | furniture | pages [25] -->
m

<!-- b002087 | furniture | pages [25] -->
m

<!-- b002088 | furniture | pages [25] -->
m

<!-- b002089 | furniture | pages [25] -->
m

<!-- b002090 | furniture | pages [25] -->
m

<!-- b002091 | furniture | pages [25] -->
m

<!-- b002092 | furniture | pages [25] -->
m

<!-- b002093 | furniture | pages [25] -->
m

<!-- b002094 | furniture | pages [25] -->
m

<!-- b002095 | furniture | pages [25] -->
m

<!-- b002096 | furniture | pages [25] -->
m

<!-- b002097 | furniture | pages [25] -->
m

<!-- b002098 | furniture | pages [25] -->
m

<!-- b002099 | furniture | pages [25] -->
m

<!-- b002100 | furniture | pages [25] -->
m

<!-- b002101 | furniture | pages [25] -->
m

<!-- b002102 | furniture | pages [25] -->
m

<!-- b002103 | furniture | pages [25] -->
m

<!-- b002104 | furniture | pages [25] -->
m

<!-- b002105 | furniture | pages [25] -->
m

<!-- b002106 | furniture | pages [25] -->
m

<!-- b002107 | furniture | pages [25] -->
m

<!-- b002108 | furniture | pages [25] -->
m

<!-- b002109 | furniture | pages [25] -->
m

<!-- b002110 | furniture | pages [25] -->
m

<!-- b002111 | furniture | pages [25] -->
m

<!-- b002112 | furniture | pages [25] -->
m

<!-- b002113 | furniture | pages [25] -->
m

<!-- b002114 | furniture | pages [25] -->
m

<!-- b002115 | furniture | pages [25] -->
m

<!-- b002116 | furniture | pages [25] -->
m

<!-- b002117 | furniture | pages [25] -->
m

<!-- b002118 | furniture | pages [25] -->
m

<!-- b002119 | furniture | pages [25] -->
m

<!-- b002120 | furniture | pages [25] -->
m

<!-- b002121 | furniture | pages [25] -->
m

<!-- b002122 | furniture | pages [25] -->
m

<!-- b002123 | furniture | pages [25] -->
m

<!-- b002124 | furniture | pages [25] -->
m

<!-- b002125 | furniture | pages [25] -->
m

<!-- b002126 | furniture | pages [25] -->
m

<!-- b002127 | furniture | pages [25] -->
m

<!-- b002128 | furniture | pages [25] -->
m

<!-- b002129 | furniture | pages [25] -->
m

<!-- b002130 | furniture | pages [25] -->
m

<!-- b002131 | furniture | pages [25] -->
m

<!-- b002132 | furniture | pages [25] -->
m

<!-- b002133 | furniture | pages [25] -->
m

<!-- b002134 | furniture | pages [25] -->
m

<!-- b002135 | furniture | pages [25] -->
m

<!-- b002136 | furniture | pages [25] -->
m

<!-- b002137 | furniture | pages [25] -->
m

<!-- b002138 | furniture | pages [25] -->
m

<!-- b002139 | furniture | pages [25] -->
m

<!-- b002140 | furniture | pages [25] -->
m

<!-- b002141 | furniture | pages [25] -->
m

<!-- b002142 | furniture | pages [25] -->
m

<!-- b002143 | furniture | pages [25] -->
m

<!-- b002144 | furniture | pages [25] -->
m

<!-- b002145 | furniture | pages [25] -->
m

<!-- b002146 | furniture | pages [25] -->
m

<!-- b002147 | furniture | pages [25] -->
m

<!-- b002148 | furniture | pages [25] -->
m

<!-- b002149 | furniture | pages [25] -->
m

<!-- b002150 | furniture | pages [25] -->
m

<!-- b002151 | furniture | pages [25] -->
m

<!-- b002152 | furniture | pages [25] -->
m

<!-- b002153 | furniture | pages [25] -->
m

<!-- b002154 | furniture | pages [25] -->
m

<!-- b002155 | furniture | pages [25] -->
m

<!-- b002156 | furniture | pages [25] -->
m

<!-- b002157 | furniture | pages [25] -->
m

<!-- b002158 | furniture | pages [25] -->
m

<!-- b002159 | furniture | pages [25] -->
m

<!-- b002160 | furniture | pages [25] -->
m

<!-- b002161 | furniture | pages [25] -->
m

<!-- b002162 | furniture | pages [25] -->
m

<!-- b002163 | furniture | pages [25] -->
m

<!-- b002164 | furniture | pages [25] -->
m

<!-- b002165 | furniture | pages [25] -->
m

<!-- b002166 | furniture | pages [25] -->
m

<!-- b002167 | furniture | pages [25] -->
m

<!-- b002168 | furniture | pages [25] -->
m

<!-- b002169 | furniture | pages [25] -->
m

<!-- b002170 | furniture | pages [25] -->
m

<!-- b002171 | furniture | pages [25] -->
m

<!-- b002172 | furniture | pages [25] -->
m

<!-- b002173 | furniture | pages [25] -->
m

<!-- b002174 | furniture | pages [25] -->
m

<!-- b002175 | furniture | pages [25] -->
m

<!-- b002176 | furniture | pages [25] -->
m

<!-- b002177 | furniture | pages [25] -->
m

<!-- b002178 | furniture | pages [25] -->
m

<!-- b002179 | furniture | pages [25] -->
m

<!-- b002180 | furniture | pages [25] -->
m

<!-- b002181 | furniture | pages [25] -->
m

<!-- b002182 | furniture | pages [25] -->
m

<!-- b002183 | furniture | pages [25] -->
m

<!-- b002184 | furniture | pages [25] -->
m

<!-- b002185 | furniture | pages [25] -->
m

<!-- b002186 | furniture | pages [25] -->
m

<!-- b002187 | furniture | pages [25] -->
m

<!-- b002188 | furniture | pages [25] -->
m

<!-- b002189 | furniture | pages [25] -->
m

<!-- b002190 | furniture | pages [25] -->
m

<!-- b002191 | furniture | pages [25] -->
m

<!-- b002192 | furniture | pages [25] -->
m

<!-- b002193 | furniture | pages [25] -->
m

<!-- b002194 | furniture | pages [26] -->
Team # 2515235

<!-- b002195 | furniture | pages [26] -->
Page 26 of 26

<!-- b002196 | references | pages [26] -->
m

<!-- b002197 | references | pages [26] -->
m

<!-- b002198 | references | pages [26] -->
m

<!-- b002199 | references | pages [26] -->
m

<!-- b002200 | references | pages [26] -->
m

<!-- b002201 | references | pages [26] -->
m

<!-- b002202 | references | pages [26] -->
m

<!-- b002203 | references | pages [26] -->
m

<!-- b002204 | references | pages [26] -->
m

<!-- b002205 | references | pages [26] -->
m

<!-- b002206 | references | pages [26] -->
m

<!-- b002207 | references | pages [26] -->
m

<!-- b002208 | references | pages [26] -->
m

<!-- b002209 | references | pages [26] -->
m

<!-- b002210 | references | pages [26] -->
m

<!-- b002211 | references | pages [26] -->
m

<!-- b002212 | references | pages [26] -->
m

<!-- b002213 | references | pages [26] -->
m

<!-- b002214 | references | pages [26] -->
m

<!-- b002215 | references | pages [26] -->
m

<!-- b002216 | references | pages [26] -->
m

<!-- b002217 | references | pages [26] -->
m

<!-- b002218 | references | pages [26] -->
m

<!-- b002219 | references | pages [26] -->
m

<!-- b002220 | references | pages [26] -->
m

<!-- b002221 | references | pages [26] -->
m

<!-- b002222 | references | pages [26] -->
m

<!-- b002223 | references | pages [26] -->
m

<!-- b002224 | references | pages [26] -->
m

<!-- b002225 | references | pages [26] -->
m

<!-- b002226 | references | pages [26] -->
m

<!-- b002227 | references | pages [26] -->
m

<!-- b002228 | references | pages [26] -->
m

<!-- b002229 | references | pages [26] -->
m

<!-- b002230 | references | pages [26] -->
m

<!-- b002231 | references | pages [26] -->
m

<!-- b002232 | references | pages [26] -->
m

<!-- b002233 | references | pages [26] -->
m

<!-- b002234 | references | pages [26] -->
m

<!-- b002235 | references | pages [26] -->
m

<!-- b002236 | references | pages [26] -->
m

<!-- b002237 | references | pages [26] -->
m

<!-- b002238 | references | pages [26] -->
m

<!-- b002239 | references | pages [26] -->
m

<!-- b002240 | references | pages [26] -->
m

<!-- b002241 | references | pages [26] -->
m

<!-- b002242 | references | pages [26] -->
m

<!-- b002243 | references | pages [26] -->
m

<!-- b002244 | references | pages [26] -->
m

<!-- b002245 | references | pages [26] -->
m

<!-- b002246 | references | pages [26] -->
m

<!-- b002247 | references | pages [26] -->
m

<!-- b002248 | references | pages [26] -->
m

<!-- b002249 | references | pages [26] -->
m

<!-- b002250 | references | pages [26] -->
m

<!-- b002251 | references | pages [26] -->
m

<!-- b002252 | references | pages [26] -->
m

<!-- b002253 | references | pages [26] -->
m

<!-- b002254 | references | pages [26] -->
m

<!-- b002255 | references | pages [26] -->
m

<!-- b002256 | references | pages [26] -->
m

<!-- b002257 | references | pages [26] -->
m

<!-- b002258 | references | pages [26] -->
m

<!-- b002259 | references | pages [26] -->
m

<!-- b002260 | references | pages [26] -->
m

<!-- b002261 | references | pages [26] -->
m

<!-- b002262 | references | pages [26] -->
m

<!-- b002263 | references | pages [26] -->
m

<!-- b002264 | references | pages [26] -->
m

<!-- b002265 | references | pages [26] -->
m

<!-- b002266 | references | pages [26] -->
m

<!-- b002267 | references | pages [26] -->
m

<!-- b002268 | references | pages [26] -->
m

<!-- b002269 | heading | pages [26] -->
Report on Use of AI

<!-- b002270 | ai_disclosure | pages [26] -->
m

<!-- b002271 | ai_disclosure | pages [26] -->
m

<!-- b002272 | ai_disclosure | pages [26] -->
m

<!-- b002273 | ai_disclosure | pages [26] -->
m

<!-- b002274 | ai_disclosure | pages [26] -->
m

<!-- b002275 | ai_disclosure | pages [26] -->
m

<!-- b002276 | ai_disclosure | pages [26] -->
m

<!-- b002277 | ai_disclosure | pages [26] -->
m

<!-- b002278 | ai_disclosure | pages [26] -->
m

<!-- b002279 | ai_disclosure | pages [26] -->
m

<!-- b002280 | ai_disclosure | pages [26] -->
m

<!-- b002281 | ai_disclosure | pages [26] -->
m

<!-- b002282 | ai_disclosure | pages [26] -->
m

<!-- b002283 | ai_disclosure | pages [26] -->
m

<!-- b002284 | ai_disclosure | pages [26] -->
m

<!-- b002285 | ai_disclosure | pages [26] -->
m

<!-- b002286 | ai_disclosure | pages [26] -->
m

<!-- b002287 | ai_disclosure | pages [26] -->
m

<!-- b002288 | ai_disclosure | pages [26] -->
m

<!-- b002289 | ai_disclosure | pages [26] -->
m

<!-- b002290 | ai_disclosure | pages [26] -->
m

<!-- b002291 | ai_disclosure | pages [26] -->
m

<!-- b002292 | ai_disclosure | pages [26] -->
m

<!-- b002293 | ai_disclosure | pages [26] -->
m

<!-- b002294 | ai_disclosure | pages [26] -->
m

<!-- b002295 | ai_disclosure | pages [26] -->
m

<!-- b002296 | ai_disclosure | pages [26] -->
m

<!-- b002297 | ai_disclosure | pages [26] -->
m

<!-- b002298 | ai_disclosure | pages [26] -->
m

<!-- b002299 | ai_disclosure | pages [26] -->
m

<!-- b002300 | ai_disclosure | pages [26] -->
m

<!-- b002301 | ai_disclosure | pages [26] -->
m

<!-- b002302 | ai_disclosure | pages [26] -->
m

<!-- b002303 | ai_disclosure | pages [26] -->
m

<!-- b002304 | ai_disclosure | pages [26] -->
m

<!-- b002305 | ai_disclosure | pages [26] -->
m

<!-- b002306 | ai_disclosure | pages [26] -->
m

<!-- b002307 | ai_disclosure | pages [26] -->
m

<!-- b002308 | ai_disclosure | pages [26] -->
m

<!-- b002309 | ai_disclosure | pages [26] -->
m

<!-- b002310 | ai_disclosure | pages [26] -->
m

<!-- b002311 | ai_disclosure | pages [26] -->
m

<!-- b002312 | ai_disclosure | pages [26] -->
m

<!-- b002313 | ai_disclosure | pages [26] -->
m

<!-- b002314 | ai_disclosure | pages [26] -->
m

<!-- b002315 | ai_disclosure | pages [26] -->
m

<!-- b002316 | ai_disclosure | pages [26] -->
m

<!-- b002317 | ai_disclosure | pages [26] -->
m

<!-- b002318 | ai_disclosure | pages [26] -->
m

<!-- b002319 | ai_disclosure | pages [26] -->
m

<!-- b002320 | ai_disclosure | pages [26] -->
m

<!-- b002321 | ai_disclosure | pages [26] -->
m

<!-- b002322 | ai_disclosure | pages [26] -->
m

<!-- b002323 | ai_disclosure | pages [26] -->
m

<!-- b002324 | ai_disclosure | pages [26] -->
m

<!-- b002325 | ai_disclosure | pages [26] -->
m

<!-- b002326 | ai_disclosure | pages [26] -->
m

<!-- b002327 | ai_disclosure | pages [26] -->
m

<!-- b002328 | ai_disclosure | pages [26] -->
m

<!-- b002329 | ai_disclosure | pages [26] -->
m

<!-- b002330 | ai_disclosure | pages [26] -->
m

<!-- b002331 | ai_disclosure | pages [26] -->
m

<!-- b002332 | ai_disclosure | pages [26] -->
m

<!-- b002333 | ai_disclosure | pages [26] -->
m

<!-- b002334 | ai_disclosure | pages [26] -->
m

<!-- b002335 | ai_disclosure | pages [26] -->
m

<!-- b002336 | ai_disclosure | pages [26] -->
m

<!-- b002337 | ai_disclosure | pages [26] -->
m

<!-- b002338 | ai_disclosure | pages [26] -->
m

<!-- b002339 | ai_disclosure | pages [26] -->
m

<!-- b002340 | ai_disclosure | pages [26] -->
m

<!-- b002341 | ai_disclosure | pages [26] -->
m

<!-- b002342 | ai_disclosure | pages [26] -->
m

<!-- b002343 | ai_disclosure | pages [26] -->
m

<!-- b002344 | ai_disclosure | pages [26] -->
m

<!-- b002345 | ai_disclosure | pages [26] -->
m

<!-- b002346 | ai_disclosure | pages [26] -->
m

<!-- b002347 | ai_disclosure | pages [26] -->
m

<!-- b002348 | ai_disclosure | pages [26] -->
m

<!-- b002349 | ai_disclosure | pages [26] -->
m

<!-- b002350 | ai_disclosure | pages [26] -->
m

<!-- b002351 | ai_disclosure | pages [26] -->
m

<!-- b002352 | ai_disclosure | pages [26] -->
m

<!-- b002353 | ai_disclosure | pages [26] -->
m

<!-- b002354 | ai_disclosure | pages [26] -->
m

<!-- b002355 | ai_disclosure | pages [26] -->
m

<!-- b002356 | ai_disclosure | pages [26] -->
m

<!-- b002357 | ai_disclosure | pages [26] -->
m

<!-- b002358 | ai_disclosure | pages [26] -->
m

<!-- b002359 | ai_disclosure | pages [26] -->
m

<!-- b002360 | ai_disclosure | pages [26] -->
m

<!-- b002361 | ai_disclosure | pages [26] -->
m

<!-- b002362 | ai_disclosure | pages [26] -->
m

<!-- b002363 | ai_disclosure | pages [26] -->
m

<!-- b002364 | ai_disclosure | pages [26] -->
m

<!-- b002365 | ai_disclosure | pages [26] -->
m

<!-- b002366 | ai_disclosure | pages [26] -->
m

<!-- b002367 | ai_disclosure | pages [26] -->
m

<!-- b002368 | ai_disclosure | pages [26] -->
m

<!-- b002369 | ai_disclosure | pages [26] -->
m

<!-- b002370 | ai_disclosure | pages [26] -->
m

<!-- b002371 | ai_disclosure | pages [26] -->
m

<!-- b002372 | ai_disclosure | pages [26] -->
m

<!-- b002373 | ai_disclosure | pages [26] -->
m

<!-- b002374 | ai_disclosure | pages [26] -->
m

<!-- b002375 | ai_disclosure | pages [26] -->
m

<!-- b002376 | ai_disclosure | pages [26] -->
m

<!-- b002377 | ai_disclosure | pages [26] -->
m

<!-- b002378 | ai_disclosure | pages [26] -->
m

<!-- b002379 | ai_disclosure | pages [26] -->
m

<!-- b002380 | ai_disclosure | pages [26] -->
m

<!-- b002381 | ai_disclosure | pages [26] -->
m

<!-- b002382 | ai_disclosure | pages [26] -->
m

<!-- b002383 | ai_disclosure | pages [26] -->
m

<!-- b002384 | ai_disclosure | pages [26] -->
m

<!-- b002385 | ai_disclosure | pages [26] -->
m

<!-- b002386 | ai_disclosure | pages [26] -->
m

<!-- b002387 | ai_disclosure | pages [26] -->
m

<!-- b002388 | ai_disclosure | pages [26] -->
m

<!-- b002389 | ai_disclosure | pages [26] -->
m

<!-- b002390 | ai_disclosure | pages [26] -->
m

<!-- b002391 | ai_disclosure | pages [26] -->
m

<!-- b002392 | ai_disclosure | pages [26] -->
m

<!-- b002393 | ai_disclosure | pages [26] -->
m

<!-- b002394 | ai_disclosure | pages [26] -->
m

<!-- b002395 | ai_disclosure | pages [26] -->
m

<!-- b002396 | ai_disclosure | pages [26] -->
m

<!-- b002397 | ai_disclosure | pages [26] -->
m

<!-- b002398 | ai_disclosure | pages [26] -->
m

<!-- b002399 | ai_disclosure | pages [26] -->
m

<!-- b002400 | ai_disclosure | pages [26] -->
m

<!-- b002401 | ai_disclosure | pages [26] -->
m

<!-- b002402 | ai_disclosure | pages [26] -->
m

<!-- b002403 | ai_disclosure | pages [26] -->
m

<!-- b002404 | ai_disclosure | pages [26] -->
m

<!-- b002405 | ai_disclosure | pages [26] -->
m

<!-- b002406 | ai_disclosure | pages [26] -->
m

<!-- b002407 | ai_disclosure | pages [26] -->
m

<!-- b002408 | ai_disclosure | pages [26] -->
m

<!-- b002409 | ai_disclosure | pages [26] -->
m

<!-- b002410 | ai_disclosure | pages [26] -->
m

<!-- b002411 | ai_disclosure | pages [26] -->
m

<!-- b002412 | ai_disclosure | pages [26] -->
m

<!-- b002413 | ai_disclosure | pages [26] -->
m

<!-- b002414 | ai_disclosure | pages [26] -->
m

<!-- b002415 | ai_disclosure | pages [26] -->
m

<!-- b002416 | ai_disclosure | pages [26] -->
m

<!-- b002417 | ai_disclosure | pages [26] -->
m

<!-- b002418 | ai_disclosure | pages [26] -->
m

<!-- b002419 | ai_disclosure | pages [26] -->
m

<!-- b002420 | ai_disclosure | pages [26] -->
m

<!-- b002421 | ai_disclosure | pages [26] -->
m

<!-- b002422 | ai_disclosure | pages [26] -->
m

<!-- b002423 | ai_disclosure | pages [26] -->
m

<!-- b002424 | ai_disclosure | pages [26] -->
m

<!-- b002425 | ai_disclosure | pages [26] -->
m

<!-- b002426 | ai_disclosure | pages [26] -->
m

<!-- b002427 | ai_disclosure | pages [26] -->
m

<!-- b002428 | ai_disclosure | pages [26] -->
m

<!-- b002429 | ai_disclosure | pages [26] -->
m

<!-- b002430 | ai_disclosure | pages [26] -->
m

<!-- b002431 | ai_disclosure | pages [26] -->
m

<!-- b002432 | ai_disclosure | pages [26] -->
m

<!-- b002433 | ai_disclosure | pages [26] -->
m

<!-- b002434 | ai_disclosure | pages [26] -->
m

<!-- b002435 | ai_disclosure | pages [26] -->
m

<!-- b002436 | ai_disclosure | pages [26] -->
m

<!-- b002437 | ai_disclosure | pages [26] -->
m

<!-- b002438 | ai_disclosure | pages [26] -->
m

<!-- b002439 | ai_disclosure | pages [26] -->
m

<!-- b002440 | ai_disclosure | pages [26] -->
m

<!-- b002441 | ai_disclosure | pages [26] -->
m

<!-- b002442 | ai_disclosure | pages [26] -->
m

<!-- b002443 | ai_disclosure | pages [26] -->
m

<!-- b002444 | ai_disclosure | pages [26] -->
m

<!-- b002445 | ai_disclosure | pages [26] -->
m

<!-- b002446 | ai_disclosure | pages [26] -->
m

<!-- b002447 | ai_disclosure | pages [26] -->
m

<!-- b002448 | ai_disclosure | pages [26] -->
m

<!-- b002449 | ai_disclosure | pages [26] -->
m

<!-- b002450 | ai_disclosure | pages [26] -->
m

<!-- b002451 | ai_disclosure | pages [26] -->
m

<!-- b002452 | ai_disclosure | pages [26] -->
m

<!-- b002453 | ai_disclosure | pages [26] -->
m

<!-- b002454 | ai_disclosure | pages [26] -->
m

<!-- b002455 | ai_disclosure | pages [26] -->
m

<!-- b002456 | ai_disclosure | pages [26] -->
m

<!-- b002457 | ai_disclosure | pages [26] -->
m

<!-- b002458 | ai_disclosure | pages [26] -->
m

<!-- b002459 | ai_disclosure | pages [26] -->
m

<!-- b002460 | ai_disclosure | pages [26] -->
m

<!-- b002461 | ai_disclosure | pages [26] -->
m

<!-- b002462 | ai_disclosure | pages [26] -->
m

<!-- b002463 | ai_disclosure | pages [26] -->
m

<!-- b002464 | ai_disclosure | pages [26] -->
m

<!-- b002465 | ai_disclosure | pages [26] -->
m

<!-- b002466 | ai_disclosure | pages [26] -->
m

<!-- b002467 | ai_disclosure | pages [26] -->
m

<!-- b002468 | ai_disclosure | pages [26] -->
m

<!-- b002469 | ai_disclosure | pages [26] -->
m

<!-- b002470 | ai_disclosure | pages [26] -->
m

<!-- b002471 | ai_disclosure | pages [26] -->
m

<!-- b002472 | ai_disclosure | pages [26] -->
m

<!-- b002473 | ai_disclosure | pages [26] -->
m

<!-- b002474 | ai_disclosure | pages [26] -->
m

<!-- b002475 | ai_disclosure | pages [26] -->
m

<!-- b002476 | ai_disclosure | pages [26] -->
m

<!-- b002477 | ai_disclosure | pages [26] -->
m

<!-- b002478 | ai_disclosure | pages [26] -->
m

<!-- b002479 | ai_disclosure | pages [26] -->
m

<!-- b002480 | ai_disclosure | pages [26] -->
m

<!-- b002481 | ai_disclosure | pages [26] -->
m

<!-- b002482 | ai_disclosure | pages [26] -->
m

<!-- b002483 | ai_disclosure | pages [26] -->
m

<!-- b002484 | ai_disclosure | pages [26] -->
m

<!-- b002485 | ai_disclosure | pages [26] -->
m

<!-- b002486 | ai_disclosure | pages [26] -->
m

<!-- b002487 | ai_disclosure | pages [26] -->
m

<!-- b002488 | ai_disclosure | pages [26] -->
m

<!-- b002489 | ai_disclosure | pages [26] -->
m

<!-- b002490 | ai_disclosure | pages [26] -->
m

<!-- b002491 | ai_disclosure | pages [26] -->
m

<!-- b002492 | ai_disclosure | pages [26] -->
m

<!-- b002493 | ai_disclosure | pages [26] -->
m

<!-- b002494 | ai_disclosure | pages [26] -->
m

<!-- b002495 | ai_disclosure | pages [26] -->
m

<!-- b002496 | ai_disclosure | pages [26] -->
m

<!-- b002497 | ai_disclosure | pages [26] -->
m

<!-- b002498 | ai_disclosure | pages [26] -->
m

<!-- b002499 | ai_disclosure | pages [26] -->
m

<!-- b002500 | ai_disclosure | pages [26] -->
m

<!-- b002501 | ai_disclosure | pages [26] -->
m

<!-- b002502 | ai_disclosure | pages [26] -->
m

<!-- b002503 | ai_disclosure | pages [26] -->
m

<!-- b002504 | ai_disclosure | pages [26] -->
m

<!-- b002505 | ai_disclosure | pages [26] -->
m

<!-- b002506 | ai_disclosure | pages [26] -->
m

<!-- b002507 | ai_disclosure | pages [26] -->
m

<!-- b002508 | ai_disclosure | pages [26] -->
m

<!-- b002509 | ai_disclosure | pages [26] -->
m

<!-- b002510 | ai_disclosure | pages [26] -->
m

<!-- b002511 | ai_disclosure | pages [26] -->
m

<!-- b002512 | ai_disclosure | pages [26] -->
m

<!-- b002513 | ai_disclosure | pages [26] -->
m

<!-- b002514 | ai_disclosure | pages [26] -->
m

<!-- b002515 | ai_disclosure | pages [26] -->
m

<!-- b002516 | ai_disclosure | pages [26] -->
m

<!-- b002517 | ai_disclosure | pages [26] -->
m

<!-- b002518 | ai_disclosure | pages [26] -->
m

<!-- b002519 | ai_disclosure | pages [26] -->
m

<!-- b002520 | ai_disclosure | pages [26] -->
m

<!-- b002521 | ai_disclosure | pages [26] -->
m

<!-- b002522 | ai_disclosure | pages [26] -->
m

<!-- b002523 | ai_disclosure | pages [26] -->
m

<!-- b002524 | ai_disclosure | pages [26] -->
m

<!-- b002525 | ai_disclosure | pages [26] -->
m

<!-- b002526 | ai_disclosure | pages [26] -->
m

<!-- b002527 | ai_disclosure | pages [26] -->
m

<!-- b002528 | ai_disclosure | pages [26] -->
m

<!-- b002529 | ai_disclosure | pages [26] -->
m

<!-- b002530 | ai_disclosure | pages [26] -->
m

<!-- b002531 | ai_disclosure | pages [26] -->
m

<!-- b002532 | ai_disclosure | pages [26] -->
m

<!-- b002533 | ai_disclosure | pages [26] -->
m

<!-- b002534 | ai_disclosure | pages [26] -->
m

<!-- b002535 | ai_disclosure | pages [26] -->
m

<!-- b002536 | ai_disclosure | pages [26] -->
m

<!-- b002537 | ai_disclosure | pages [26] -->
m

<!-- b002538 | ai_disclosure | pages [26] -->
m

<!-- b002539 | ai_disclosure | pages [26] -->
m

<!-- b002540 | ai_disclosure | pages [26] -->
m

<!-- b002541 | ai_disclosure | pages [26] -->
m

<!-- b002542 | ai_disclosure | pages [26] -->
m

<!-- b002543 | ai_disclosure | pages [26] -->
m

<!-- b002544 | ai_disclosure | pages [26] -->
m

<!-- b002545 | ai_disclosure | pages [26] -->
m

<!-- b002546 | ai_disclosure | pages [26] -->
m

<!-- b002547 | ai_disclosure | pages [26] -->
m

<!-- b002548 | ai_disclosure | pages [26] -->
m

<!-- b002549 | ai_disclosure | pages [26] -->
m

<!-- b002550 | ai_disclosure | pages [26] -->
m

<!-- b002551 | ai_disclosure | pages [26] -->
m

<!-- b002552 | ai_disclosure | pages [26] -->
m

<!-- b002553 | ai_disclosure | pages [26] -->
m

<!-- b002554 | ai_disclosure | pages [26] -->
m

<!-- b002555 | ai_disclosure | pages [26] -->
m

<!-- b002556 | ai_disclosure | pages [26] -->
m

<!-- b002557 | ai_disclosure | pages [26] -->
m

<!-- b002558 | ai_disclosure | pages [26] -->
m

<!-- b002559 | ai_disclosure | pages [26] -->
m

<!-- b002560 | ai_disclosure | pages [26] -->
m

<!-- b002561 | ai_disclosure | pages [26] -->
m

<!-- b002562 | ai_disclosure | pages [26] -->
m

<!-- b002563 | ai_disclosure | pages [26] -->
m

<!-- b002564 | ai_disclosure | pages [26] -->
m

<!-- b002565 | ai_disclosure | pages [26] -->
m

<!-- b002566 | ai_disclosure | pages [26] -->
m

<!-- b002567 | ai_disclosure | pages [26] -->
m

<!-- b002568 | ai_disclosure | pages [26] -->
1. OpenAl ChatGPT (Nov 30, 2024 version, ChatGPT-4,)

<!-- b002569 | ai_disclosure | pages [26] -->
m

<!-- b002570 | ai_disclosure | pages [26] -->
m

<!-- b002571 | ai_disclosure | pages [26] -->
m

<!-- b002572 | ai_disclosure | pages [26] -->
m

<!-- b002573 | ai_disclosure | pages [26] -->
m

<!-- b002574 | ai_disclosure | pages [26] -->
m

<!-- b002575 | ai_disclosure | pages [26] -->
m

<!-- b002576 | ai_disclosure | pages [26] -->
m

<!-- b002577 | ai_disclosure | pages [26] -->
m

<!-- b002578 | ai_disclosure | pages [26] -->
m

<!-- b002579 | ai_disclosure | pages [26] -->
m

<!-- b002580 | ai_disclosure | pages [26] -->
m

<!-- b002581 | ai_disclosure | pages [26] -->
m

<!-- b002582 | ai_disclosure | pages [26] -->
m

<!-- b002583 | ai_disclosure | pages [26] -->
m

<!-- b002584 | ai_disclosure | pages [26] -->
m

<!-- b002585 | ai_disclosure | pages [26] -->
m

<!-- b002586 | ai_disclosure | pages [26] -->
m

<!-- b002587 | ai_disclosure | pages [26] -->
m

<!-- b002588 | ai_disclosure | pages [26] -->
m

<!-- b002589 | ai_disclosure | pages [26] -->
m

<!-- b002590 | ai_disclosure | pages [26] -->
m

<!-- b002591 | ai_disclosure | pages [26] -->
m

<!-- b002592 | ai_disclosure | pages [26] -->
m

<!-- b002593 | ai_disclosure | pages [26] -->
m

<!-- b002594 | ai_disclosure | pages [26] -->
m

<!-- b002595 | ai_disclosure | pages [26] -->
m

<!-- b002596 | ai_disclosure | pages [26] -->
m

<!-- b002597 | ai_disclosure | pages [26] -->
m

<!-- b002598 | ai_disclosure | pages [26] -->
m

<!-- b002599 | ai_disclosure | pages [26] -->
m

<!-- b002600 | ai_disclosure | pages [26] -->
m

<!-- b002601 | ai_disclosure | pages [26] -->
m

<!-- b002602 | ai_disclosure | pages [26] -->
m

<!-- b002603 | ai_disclosure | pages [26] -->
m

<!-- b002604 | ai_disclosure | pages [26] -->
m

<!-- b002605 | ai_disclosure | pages [26] -->
m

<!-- b002606 | ai_disclosure | pages [26] -->
m

<!-- b002607 | ai_disclosure | pages [26] -->
m

<!-- b002608 | ai_disclosure | pages [26] -->
m

<!-- b002609 | ai_disclosure | pages [26] -->
m

<!-- b002610 | ai_disclosure | pages [26] -->
m

<!-- b002611 | ai_disclosure | pages [26] -->
m

<!-- b002612 | ai_disclosure | pages [26] -->
m

<!-- b002613 | ai_disclosure | pages [26] -->
m

<!-- b002614 | ai_disclosure | pages [26] -->
m

<!-- b002615 | ai_disclosure | pages [26] -->
m

<!-- b002616 | ai_disclosure | pages [26] -->
m

<!-- b002617 | ai_disclosure | pages [26] -->
m

<!-- b002618 | ai_disclosure | pages [26] -->
m

<!-- b002619 | ai_disclosure | pages [26] -->
m

<!-- b002620 | ai_disclosure | pages [26] -->
m

<!-- b002621 | ai_disclosure | pages [26] -->
m

<!-- b002622 | ai_disclosure | pages [26] -->
m

<!-- b002623 | ai_disclosure | pages [26] -->
m

<!-- b002624 | ai_disclosure | pages [26] -->
m

<!-- b002625 | ai_disclosure | pages [26] -->
m

<!-- b002626 | ai_disclosure | pages [26] -->
m

<!-- b002627 | ai_disclosure | pages [26] -->
m

<!-- b002628 | ai_disclosure | pages [26] -->
m

<!-- b002629 | ai_disclosure | pages [26] -->
m

<!-- b002630 | ai_disclosure | pages [26] -->
m

<!-- b002631 | ai_disclosure | pages [26] -->
m

<!-- b002632 | ai_disclosure | pages [26] -->
m

<!-- b002633 | ai_disclosure | pages [26] -->
m

<!-- b002634 | ai_disclosure | pages [26] -->
m

<!-- b002635 | ai_disclosure | pages [26] -->
m

<!-- b002636 | ai_disclosure | pages [26] -->
m

<!-- b002637 | ai_disclosure | pages [26] -->
m

<!-- b002638 | ai_disclosure | pages [26] -->
m

<!-- b002639 | ai_disclosure | pages [26] -->
m

<!-- b002640 | ai_disclosure | pages [26] -->
m

<!-- b002641 | ai_disclosure | pages [26] -->
m

<!-- b002642 | ai_disclosure | pages [26] -->
m

<!-- b002643 | ai_disclosure | pages [26] -->
m

<!-- b002644 | ai_disclosure | pages [26] -->
m

<!-- b002645 | ai_disclosure | pages [26] -->
m

<!-- b002646 | ai_disclosure | pages [26] -->
m

<!-- b002647 | ai_disclosure | pages [26] -->
m

<!-- b002648 | ai_disclosure | pages [26] -->
m

<!-- b002649 | ai_disclosure | pages [26] -->
m

<!-- b002650 | ai_disclosure | pages [26] -->
m

<!-- b002651 | ai_disclosure | pages [26] -->
m

<!-- b002652 | ai_disclosure | pages [26] -->
m

<!-- b002653 | ai_disclosure | pages [26] -->
m

<!-- b002654 | ai_disclosure | pages [26] -->
m

<!-- b002655 | ai_disclosure | pages [26] -->
m

<!-- b002656 | ai_disclosure | pages [26] -->
m

<!-- b002657 | ai_disclosure | pages [26] -->
m

<!-- b002658 | ai_disclosure | pages [26] -->
m

<!-- b002659 | ai_disclosure | pages [26] -->
m

<!-- b002660 | ai_disclosure | pages [26] -->
m

<!-- b002661 | ai_disclosure | pages [26] -->
m

<!-- b002662 | ai_disclosure | pages [26] -->
m

<!-- b002663 | ai_disclosure | pages [26] -->
m

<!-- b002664 | ai_disclosure | pages [26] -->
m

<!-- b002665 | ai_disclosure | pages [26] -->
m

<!-- b002666 | ai_disclosure | pages [26] -->
m

<!-- b002667 | ai_disclosure | pages [26] -->
m

<!-- b002668 | ai_disclosure | pages [26] -->
m

<!-- b002669 | ai_disclosure | pages [26] -->
m

<!-- b002670 | ai_disclosure | pages [26] -->
m

<!-- b002671 | ai_disclosure | pages [26] -->
m

<!-- b002672 | ai_disclosure | pages [26] -->
m

<!-- b002673 | ai_disclosure | pages [26] -->
m

<!-- b002674 | ai_disclosure | pages [26] -->
m

<!-- b002675 | ai_disclosure | pages [26] -->
m

<!-- b002676 | ai_disclosure | pages [26] -->
m

<!-- b002677 | ai_disclosure | pages [26] -->
m

<!-- b002678 | ai_disclosure | pages [26] -->
m

<!-- b002679 | ai_disclosure | pages [26] -->
m

<!-- b002680 | ai_disclosure | pages [26] -->
m

<!-- b002681 | ai_disclosure | pages [26] -->
m

<!-- b002682 | ai_disclosure | pages [26] -->
m

<!-- b002683 | ai_disclosure | pages [26] -->
m

<!-- b002684 | ai_disclosure | pages [26] -->
m

<!-- b002685 | ai_disclosure | pages [26] -->
m

<!-- b002686 | ai_disclosure | pages [26] -->
m

<!-- b002687 | ai_disclosure | pages [26] -->
m

<!-- b002688 | ai_disclosure | pages [26] -->
m

<!-- b002689 | ai_disclosure | pages [26] -->
m

<!-- b002690 | ai_disclosure | pages [26] -->
m

<!-- b002691 | ai_disclosure | pages [26] -->
m

<!-- b002692 | ai_disclosure | pages [26] -->
m

<!-- b002693 | ai_disclosure | pages [26] -->
m

<!-- b002694 | ai_disclosure | pages [26] -->
m

<!-- b002695 | ai_disclosure | pages [26] -->
m

<!-- b002696 | ai_disclosure | pages [26] -->
m

<!-- b002697 | ai_disclosure | pages [26] -->
m

<!-- b002698 | ai_disclosure | pages [26] -->
m

<!-- b002699 | ai_disclosure | pages [26] -->
m

<!-- b002700 | ai_disclosure | pages [26] -->
m

<!-- b002701 | ai_disclosure | pages [26] -->
m

<!-- b002702 | ai_disclosure | pages [26] -->
m

<!-- b002703 | ai_disclosure | pages [26] -->
m

<!-- b002704 | ai_disclosure | pages [26] -->
m

<!-- b002705 | ai_disclosure | pages [26] -->
m

<!-- b002706 | ai_disclosure | pages [26] -->
m

<!-- b002707 | ai_disclosure | pages [26] -->
m

<!-- b002708 | ai_disclosure | pages [26] -->
m

<!-- b002709 | ai_disclosure | pages [26] -->
m

<!-- b002710 | ai_disclosure | pages [26] -->
m

<!-- b002711 | ai_disclosure | pages [26] -->
m

<!-- b002712 | ai_disclosure | pages [26] -->
m

<!-- b002713 | ai_disclosure | pages [26] -->
m

<!-- b002714 | ai_disclosure | pages [26] -->
m

<!-- b002715 | ai_disclosure | pages [26] -->
m

<!-- b002716 | ai_disclosure | pages [26] -->
m

<!-- b002717 | ai_disclosure | pages [26] -->
m

<!-- b002718 | ai_disclosure | pages [26] -->
m

<!-- b002719 | ai_disclosure | pages [26] -->
m

<!-- b002720 | ai_disclosure | pages [26] -->
m

<!-- b002721 | ai_disclosure | pages [26] -->
m

<!-- b002722 | ai_disclosure | pages [26] -->
m

<!-- b002723 | ai_disclosure | pages [26] -->
m

<!-- b002724 | ai_disclosure | pages [26] -->
m

<!-- b002725 | ai_disclosure | pages [26] -->
m

<!-- b002726 | ai_disclosure | pages [26] -->
m

<!-- b002727 | ai_disclosure | pages [26] -->
m

<!-- b002728 | ai_disclosure | pages [26] -->
m

<!-- b002729 | ai_disclosure | pages [26] -->
m

<!-- b002730 | ai_disclosure | pages [26] -->
Query1:<What is the Pearson correlation coefficient>

<!-- b002731 | ai_disclosure | pages [26] -->
m

<!-- b002732 | ai_disclosure | pages [26] -->
m

<!-- b002733 | ai_disclosure | pages [26] -->
m

<!-- b002734 | ai_disclosure | pages [26] -->
m

<!-- b002735 | ai_disclosure | pages [26] -->
m

<!-- b002736 | ai_disclosure | pages [26] -->
m

<!-- b002737 | ai_disclosure | pages [26] -->
m

<!-- b002738 | ai_disclosure | pages [26] -->
m

<!-- b002739 | ai_disclosure | pages [26] -->
m

<!-- b002740 | ai_disclosure | pages [26] -->
m

<!-- b002741 | ai_disclosure | pages [26] -->
m

<!-- b002742 | ai_disclosure | pages [26] -->
m

<!-- b002743 | ai_disclosure | pages [26] -->
m

<!-- b002744 | ai_disclosure | pages [26] -->
m

<!-- b002745 | ai_disclosure | pages [26] -->
m

<!-- b002746 | ai_disclosure | pages [26] -->
m

<!-- b002747 | ai_disclosure | pages [26] -->
m

<!-- b002748 | ai_disclosure | pages [26] -->
m

<!-- b002749 | ai_disclosure | pages [26] -->
m

<!-- b002750 | ai_disclosure | pages [26] -->
m

<!-- b002751 | ai_disclosure | pages [26] -->
m

<!-- b002752 | ai_disclosure | pages [26] -->
m

<!-- b002753 | ai_disclosure | pages [26] -->
m

<!-- b002754 | ai_disclosure | pages [26] -->
m

<!-- b002755 | ai_disclosure | pages [26] -->
m

<!-- b002756 | ai_disclosure | pages [26] -->
m

<!-- b002757 | ai_disclosure | pages [26] -->
m

<!-- b002758 | ai_disclosure | pages [26] -->
m

<!-- b002759 | ai_disclosure | pages [26] -->
m

<!-- b002760 | ai_disclosure | pages [26] -->
m

<!-- b002761 | ai_disclosure | pages [26] -->
m

<!-- b002762 | ai_disclosure | pages [26] -->
m

<!-- b002763 | ai_disclosure | pages [26] -->
m

<!-- b002764 | ai_disclosure | pages [26] -->
m

<!-- b002765 | ai_disclosure | pages [26] -->
m

<!-- b002766 | ai_disclosure | pages [26] -->
m

<!-- b002767 | ai_disclosure | pages [26] -->
m

<!-- b002768 | ai_disclosure | pages [26] -->
m

<!-- b002769 | ai_disclosure | pages [26] -->
m

<!-- b002770 | ai_disclosure | pages [26] -->
m

<!-- b002771 | ai_disclosure | pages [26] -->
m

<!-- b002772 | ai_disclosure | pages [26] -->
m

<!-- b002773 | ai_disclosure | pages [26] -->
m

<!-- b002774 | ai_disclosure | pages [26] -->
m

<!-- b002775 | ai_disclosure | pages [26] -->
m

<!-- b002776 | ai_disclosure | pages [26] -->
m

<!-- b002777 | ai_disclosure | pages [26] -->
m

<!-- b002778 | ai_disclosure | pages [26] -->
m

<!-- b002779 | ai_disclosure | pages [26] -->
m

<!-- b002780 | ai_disclosure | pages [26] -->
m

<!-- b002781 | ai_disclosure | pages [26] -->
m

<!-- b002782 | ai_disclosure | pages [26] -->
m

<!-- b002783 | ai_disclosure | pages [26] -->
m

<!-- b002784 | ai_disclosure | pages [26] -->
m

<!-- b002785 | ai_disclosure | pages [26] -->
m

<!-- b002786 | ai_disclosure | pages [26] -->
m

<!-- b002787 | ai_disclosure | pages [26] -->
m

<!-- b002788 | ai_disclosure | pages [26] -->
m

<!-- b002789 | ai_disclosure | pages [26] -->
m

<!-- b002790 | ai_disclosure | pages [26] -->
m

<!-- b002791 | ai_disclosure | pages [26] -->
m

<!-- b002792 | ai_disclosure | pages [26] -->
m

<!-- b002793 | ai_disclosure | pages [26] -->
m

<!-- b002794 | ai_disclosure | pages [26] -->
m

<!-- b002795 | ai_disclosure | pages [26] -->
m

<!-- b002796 | ai_disclosure | pages [26] -->
m

<!-- b002797 | ai_disclosure | pages [26] -->
m

<!-- b002798 | ai_disclosure | pages [26] -->
m

<!-- b002799 | ai_disclosure | pages [26] -->
m

<!-- b002800 | ai_disclosure | pages [26] -->
m

<!-- b002801 | ai_disclosure | pages [26] -->
m

<!-- b002802 | ai_disclosure | pages [26] -->
m

<!-- b002803 | ai_disclosure | pages [26] -->
m

<!-- b002804 | ai_disclosure | pages [26] -->
m

<!-- b002805 | ai_disclosure | pages [26] -->
m

<!-- b002806 | ai_disclosure | pages [26] -->
m

<!-- b002807 | ai_disclosure | pages [26] -->
m

<!-- b002808 | ai_disclosure | pages [26] -->
m

<!-- b002809 | ai_disclosure | pages [26] -->
m

<!-- b002810 | ai_disclosure | pages [26] -->
m

<!-- b002811 | ai_disclosure | pages [26] -->
m

<!-- b002812 | ai_disclosure | pages [26] -->
m

<!-- b002813 | ai_disclosure | pages [26] -->
m

<!-- b002814 | ai_disclosure | pages [26] -->
m

<!-- b002815 | ai_disclosure | pages [26] -->
m

<!-- b002816 | ai_disclosure | pages [26] -->
m

<!-- b002817 | ai_disclosure | pages [26] -->
m

<!-- b002818 | ai_disclosure | pages [26] -->
m

<!-- b002819 | ai_disclosure | pages [26] -->
m

<!-- b002820 | ai_disclosure | pages [26] -->
m

<!-- b002821 | ai_disclosure | pages [26] -->
m

<!-- b002822 | ai_disclosure | pages [26] -->
m

<!-- b002823 | ai_disclosure | pages [26] -->
m

<!-- b002824 | ai_disclosure | pages [26] -->
m

<!-- b002825 | ai_disclosure | pages [26] -->
m

<!-- b002826 | ai_disclosure | pages [26] -->
m

<!-- b002827 | ai_disclosure | pages [26] -->
m

<!-- b002828 | ai_disclosure | pages [26] -->
m

<!-- b002829 | ai_disclosure | pages [26] -->
m

<!-- b002830 | ai_disclosure | pages [26] -->
m

<!-- b002831 | ai_disclosure | pages [26] -->
m

<!-- b002832 | ai_disclosure | pages [26] -->
m

<!-- b002833 | ai_disclosure | pages [26] -->
m

<!-- b002834 | ai_disclosure | pages [26] -->
m

<!-- b002835 | ai_disclosure | pages [26] -->
m

<!-- b002836 | ai_disclosure | pages [26] -->
m

<!-- b002837 | ai_disclosure | pages [26] -->
m

<!-- b002838 | ai_disclosure | pages [26] -->
m

<!-- b002839 | ai_disclosure | pages [26] -->
m

<!-- b002840 | ai_disclosure | pages [26] -->
m

<!-- b002841 | ai_disclosure | pages [26] -->
m

<!-- b002842 | ai_disclosure | pages [26] -->
m

<!-- b002843 | ai_disclosure | pages [26] -->
m

<!-- b002844 | ai_disclosure | pages [26] -->
m

<!-- b002845 | ai_disclosure | pages [26] -->
m

<!-- b002846 | ai_disclosure | pages [26] -->
m

<!-- b002847 | ai_disclosure | pages [26] -->
m

<!-- b002848 | ai_disclosure | pages [26] -->
m

<!-- b002849 | ai_disclosure | pages [26] -->
m

<!-- b002850 | ai_disclosure | pages [26] -->
m

<!-- b002851 | ai_disclosure | pages [26] -->
m

<!-- b002852 | ai_disclosure | pages [26] -->
m

<!-- b002853 | ai_disclosure | pages [26] -->
m

<!-- b002854 | ai_disclosure | pages [26] -->
m

<!-- b002855 | ai_disclosure | pages [26] -->
m

<!-- b002856 | ai_disclosure | pages [26] -->
m

<!-- b002857 | ai_disclosure | pages [26] -->
m

<!-- b002858 | ai_disclosure | pages [26] -->
m

<!-- b002859 | ai_disclosure | pages [26] -->
m

<!-- b002860 | ai_disclosure | pages [26] -->
m

<!-- b002861 | ai_disclosure | pages [26] -->
m

<!-- b002862 | ai_disclosure | pages [26] -->
m

<!-- b002863 | ai_disclosure | pages [26] -->
m

<!-- b002864 | ai_disclosure | pages [26] -->
m

<!-- b002865 | ai_disclosure | pages [26] -->
m

<!-- b002866 | ai_disclosure | pages [26] -->
m

<!-- b002867 | ai_disclosure | pages [26] -->
m

<!-- b002868 | ai_disclosure | pages [26] -->
m

<!-- b002869 | ai_disclosure | pages [26] -->
m

<!-- b002870 | ai_disclosure | pages [26] -->
m

<!-- b002871 | ai_disclosure | pages [26] -->
m

<!-- b002872 | ai_disclosure | pages [26] -->
m

<!-- b002873 | ai_disclosure | pages [26] -->
m

<!-- b002874 | ai_disclosure | pages [26] -->
m

<!-- b002875 | ai_disclosure | pages [26] -->
m

<!-- b002876 | ai_disclosure | pages [26] -->
m

<!-- b002877 | ai_disclosure | pages [26] -->
m

<!-- b002878 | ai_disclosure | pages [26] -->
m

<!-- b002879 | ai_disclosure | pages [26] -->
m

<!-- b002880 | ai_disclosure | pages [26] -->
m

<!-- b002881 | ai_disclosure | pages [26] -->
m

<!-- b002882 | ai_disclosure | pages [26] -->
m

<!-- b002883 | ai_disclosure | pages [26] -->
m

<!-- b002884 | ai_disclosure | pages [26] -->
m

<!-- b002885 | ai_disclosure | pages [26] -->
m

<!-- b002886 | ai_disclosure | pages [26] -->
Output:<The Pearson correlation coefficient is a statistical measure that quantifies the

<!-- b002887 | ai_disclosure | pages [26] -->
linear relationship between two variables. It ranges from -1 to +1, where +1 indicates a per-

<!-- b002888 | ai_disclosure | pages [26] -->
fect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indi-

<!-- b002889 | ai_disclosure | pages [26] -->
cates no linear relationship. The formula for calculating it is the covariance of the two varia-

<!-- b002890 | ai_disclosure | pages [26] -->
bles divided by the product of their standard deviations. It is commonly used in statistics and

<!-- b002891 | ai_disclosure | pages [26] -->
data analysis to assess how strongly two variables are related.>

<!-- b002892 | ai_disclosure | pages [26] -->
2. OpenAl ChatGPT (Nov 30, 2024 version, ChatGPT-4,)

<!-- b002893 | ai_disclosure | pages [26] -->
Query2:<What are some Python functions to normalize an array>

<!-- b002894 | ai_disclosure | pages [26] -->
Output:<In Python, common methods to normalize an array include: 1) Min-Max Nor-

<!-- b002895 | ai_disclosure | pages [26] -->
malization: scale data between 0 and 1 using (arr - arr.min()) / (arr.max() - arr.min()); 2) Z-

<!-- b002896 | ai_disclosure | pages [26] -->
Score Normalization: standardize data to have a mean of 0 and standard deviation of 1 using

<!-- b002897 | ai_disclosure | pages [26] -->
(arr - arr.mean()) / arr.std(); 3) Use MinMaxScaler and StandardScaler from sklearn for nor-

<!-- b002898 | ai_disclosure | pages [26] -->
malization; 4) Max Normalization: divide each element by the maximum value using arr /

<!-- b002899 | ai_disclosure | pages [26] -->
arr.max(); 5) L2 Normalization: convert data to a unit vector using arr / np.linalg.norm(arr).

<!-- b002900 | ai_disclosure | pages [26] -->
Choose the method based on your specific needs.>

<!-- b002901 | ai_disclosure | pages [26] -->
3. OpenAl ChatGPT (Nov 30, 2024 version, ChatGPT-4o,)

<!-- b002902 | ai_disclosure | pages [26] -->
Query3:<How to plot a scatter plot in Python?>

<!-- b002903 | ai_disclosure | pages [26] -->
Output:<To plot a scatter plot in Python, you can use the matplotlib library. Here’s a basic ex-

<!-- b002904 | ai_disclosure | pages [26] -->
ample:

<!-- b002905 | ai_disclosure | pages [26] -->
In this code:

<!-- b002906 | ai_disclosure | pages [26] -->
plt.scatter(x, y) creates the scatter plot with x and y values.

<!-- b002907 | ai_disclosure | pages [26] -->
plt.title(), plt.xlabel(), and plt.ylabel() add a title and labels to the axes.

<!-- b002908 | ai_disclosure | pages [26] -->
plt.show() displays the plot.

<!-- b002909 | ai_disclosure | pages [26] -->
Let me know if you need further customization!>

<!-- b002910 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b002911 | furniture | pages [26] -->
2

<!-- b002912 | furniture | pages [26] -->
MATHmodels

<!-- b002913 | furniture | pages [26] -->
获取更多资讯
