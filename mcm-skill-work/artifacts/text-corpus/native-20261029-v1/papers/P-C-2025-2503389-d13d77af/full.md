# P-C-2025-2503389-d13d77af

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2025

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | furniture | pages [1] -->
2503389

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Olympic Medal Prediction Model Based on

<!-- b000009 | title | pages [1] -->
Regression and Machine Learning

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
In Olympic sports, accurately predicting medal outcomes and understanding the factors driving national performance are essential for effective strategic planning. Based on the given dataset, we developed multiple mathematical models to forecast medal counts, identified nations likely to win their first medals, evaluated the strategic importance of specific sports, quantified the influence of Great Coaches, and analyzed the spillover effects of host countries. Findings include:

<!-- b000012 | title | pages [1] -->
微信公众号：数学模型

<!-- b000013 | prose | pages [1] -->
Medal Forecasting: We developed a Multiple Linear Regression–Feedforward Neural Network Bootstrap Ensemble Interval Model incorporating features such as the host boost, athlete pool, historical momentum, and competitive index. The model predicts that the United States will dominate the 2028 Los Angeles Olympics with an estimated total of 143 medals, followed by China with 76.Furthermore, the model suggests improvements for the United States and Germany, while China and the United Kingdom may experience declines.

<!-- b000014 | prose | pages [1] -->
First-Time Medalists: We developed a hybrid Logistic Regression–Random Forest model to predict First-Time Medalists. The key features analyzed included Number of Programs At- tended, Athlete Participation Experience, and Program Competition Intensity.Three countries— Angola, El Salvador, and Papua New Guinea—are identified as the most likely to win their first

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
Olympic medal, with probabilities of 88.09% (LR) and 94.12% (RF). This prediction is further validated by Monte Carlo simulations, with a 95% confidence interval of 1.00–8.00.

<!-- b000017 | prose | pages [1] -->
Strategic Sport Prioritization: The Strategic Importance Assessment Model for Olympic Sports (SIAMOS) model assesses the relationship between event characteristics (quantity, va- riety) and national medal potential. Key metrics—National Medal Proportion, Global Competi- tive Presence, Long-term Achievement Stability, and Athlete Sport Distribution—were weighted via Principal Component Analysis. Results identified swimming (USA, IS = 39.8) and diving (China, IS = 33.1) as the highest-impact disciplines. Host nations can optimize medal outcomes by focusing on sports with strong historical performance and competitive advantage.

<!-- b000018 | prose | pages [1] -->
Coach Impact Analysis: Breakpoint regression quantified the impact of Great Coaches, including Keiko Kageyama (China, Artistic Swimming), Dave Brailsford (UK, Cycling), and Béla and Marta Károlyi (US, Gymnastics), with a median post/pre-coach medal ratio of 1.7.

<!-- b000019 | prose | pages [1] -->
Great Coach Effect Application: Poland(athletics, canoe sprint, sailing), Nigeria (foot- ball), and India(badminton, weightlifting, wrestling) were identified as high-potential nations for elite coaching. Adjusted regression coefficients and medal weights—gold (0.9), silver (0.6), bronze (0.4), no medal (0.1)—highlight how elite coaching could improve medal prospects and weighted scores.

<!-- b000020 | prose | pages [1] -->
Host Spillover Effect: Further exploration of the data reveals that the ”Host Boost” signif- icantly increases the medal rates of neighboring countries.

<!-- b000021 | keywords | pages [1] -->
Keywords: Olympic medal prediction;Strategic Importance Assessment Model for Olympic

<!-- b000022 | prose | pages [1] -->
Sports;Logistic Regression-Random Forest;Multivariate Linear Regression-Feedforward Neu- ral Network

<!-- b000023 | furniture | pages [3] -->
Team # 2503389

<!-- b000024 | furniture | pages [3] -->
Page 3 of 26

<!-- b000025 | prose | pages [3] -->
1

<!-- b000026 | heading | pages [3] -->
Introduction

<!-- b000027 | prose | pages [3] -->
1.1

<!-- b000028 | heading | pages [3] -->
Background

<!-- b000029 | prose | pages [3] -->
The 2024 Paris Olympics concluded with notable highlights, including the United States leading the medal tally with 126 medals and sharing the top spot for gold medals with China at

<!-- b000030 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000031 | prose | pages [3] -->
40 each.

<!-- b000032 | prose | pages [3] -->
As the world’s focus shifts toward the 2028 Los Angeles Olympics, the city’s vibrant energy and cultural diversity set the stage for the historic Games.

<!-- b000033 | prose | pages [3] -->
By analysing historical data and designing predictive modeling, we aim to forecast the 2028 Olympic medal standings. The host nation, the United States, potentially reinforcing its domi- nance. Simultaneously, countries that have yet to secure an Olympic medal will strive to achieve their first victories, marking historic milestones.

<!-- b000034 | prose | pages [3] -->
Additionally, the influence of great coaches and strategic investments may significantly shift

<!-- b000035 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000036 | prose | pages [3] -->
outcomes, offering valuable insights into medal prospects and performance optimization for countries worldwide.

<!-- b000037 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000038 | prose | pages [3] -->
Based on the analysis of the background, the key tasks are as follows:

<!-- b000039 | prose | pages [3] -->
Problem 1. Develop a predictive model for Olympic medal counts by country. The model

<!-- b000040 | prose | pages [3] -->
should incorporate uncertainty estimates, evaluate prediction accuracy, and provide com- prehensive performance metrics.

<!-- b000041 | prose | pages [3] -->
Task 1.1 Use the model to forecast the medal table for the 2028 Los Angeles Summer Olympics.

<!-- b000042 | prose | pages [3] -->
Provide prediction intervals for all outcomes. Additionally, identify countries most likely to improve and those at risk of underperforming compared to their 2024 results.

<!-- b000043 | prose | pages [3] -->
Task 1.2 Identify nations that have yet to win an Olympic medal and forecast how many are

<!-- b000044 | prose | pages [3] -->
likely to achieve their first medal in the upcoming Games. Estimate the probability of countries earning their first Olympic medal.

<!-- b000045 | prose | pages [3] -->
Task 1.3 Integrate event numbers and types into the model to analyze their relationship with

<!-- b000046 | prose | pages [3] -->
medal counts by country. Identify influential sports for specific nations, their significance, and the impact of host nation event selection on results.

<!-- b000047 | prose | pages [3] -->
Problem 2. Coaches, unlike athletes, can freely move between countries, creating the potential

<!-- b000048 | prose | pages [3] -->
for a significant “great coach” effect.

<!-- b000049 | prose | pages [3] -->
Task 2.1 Analyze data for evidence of changes that may be attributed to the influence of excep-

<!-- b000050 | prose | pages [3] -->
tional coaches.Quantify the contribution of this “great coach” effect to medal counts.

<!-- b000051 | prose | pages [3] -->
Task 2.2 Select three countries and determine the sports in which they should invest in recruit-

<!-- b000052 | prose | pages [3] -->
ing a “great coach.” Estimate the potential impact of such strategic coaching investments on medal performance.

<!-- b000053 | heading | pages [3] -->
Problem 3. Identify additional, original insights revealed by the model regarding Olympic

<!-- b000054 | prose | pages [3] -->
medal counts. Provide actionable recommendations to country Olympic committees based on these findings.

<!-- b000055 | furniture | pages [4] -->
Team # 2503389

<!-- b000056 | prose | pages [4] -->
1.3 Our work

<!-- b000057 | furniture | pages [4] -->
m

<!-- b000058 | furniture | pages [4] -->
m

<!-- b000059 | furniture | pages [4] -->
m

<!-- b000060 | furniture | pages [4] -->
m

<!-- b000061 | furniture | pages [4] -->
m

<!-- b000062 | furniture | pages [4] -->
m

<!-- b000063 | furniture | pages [4] -->
m

<!-- b000064 | furniture | pages [4] -->
m

<!-- b000065 | furniture | pages [4] -->
m

<!-- b000066 | furniture | pages [4] -->
m

<!-- b000067 | furniture | pages [4] -->
m

<!-- b000068 | furniture | pages [4] -->
m

<!-- b000069 | furniture | pages [4] -->
m

<!-- b000070 | furniture | pages [4] -->
m

<!-- b000071 | furniture | pages [4] -->
m

<!-- b000072 | furniture | pages [4] -->
m

<!-- b000073 | furniture | pages [4] -->
m

<!-- b000074 | furniture | pages [4] -->
m

<!-- b000075 | furniture | pages [4] -->
m

<!-- b000076 | furniture | pages [4] -->
m

<!-- b000077 | furniture | pages [4] -->
m

<!-- b000078 | furniture | pages [4] -->
m

<!-- b000079 | furniture | pages [4] -->
m

<!-- b000080 | furniture | pages [4] -->
m

<!-- b000081 | furniture | pages [4] -->
m

<!-- b000082 | furniture | pages [4] -->
m

<!-- b000083 | furniture | pages [4] -->
m

<!-- b000084 | furniture | pages [4] -->
m

<!-- b000085 | furniture | pages [4] -->
m

<!-- b000086 | furniture | pages [4] -->
m

<!-- b000087 | furniture | pages [4] -->
m

<!-- b000088 | furniture | pages [4] -->
m

<!-- b000089 | furniture | pages [4] -->
m

<!-- b000090 | furniture | pages [4] -->
m

<!-- b000091 | furniture | pages [4] -->
m

<!-- b000092 | furniture | pages [4] -->
m

<!-- b000093 | furniture | pages [4] -->
m

<!-- b000094 | furniture | pages [4] -->
m

<!-- b000095 | furniture | pages [4] -->
m

<!-- b000096 | furniture | pages [4] -->
m

<!-- b000097 | furniture | pages [4] -->
m

<!-- b000098 | furniture | pages [4] -->
m

<!-- b000099 | furniture | pages [4] -->
m

<!-- b000100 | furniture | pages [4] -->
m

<!-- b000101 | furniture | pages [4] -->
m

<!-- b000102 | furniture | pages [4] -->
m

<!-- b000103 | furniture | pages [4] -->
m

<!-- b000104 | furniture | pages [4] -->
m

<!-- b000105 | furniture | pages [4] -->
m

<!-- b000106 | furniture | pages [4] -->
m

<!-- b000107 | furniture | pages [4] -->
m

<!-- b000108 | furniture | pages [4] -->
m

<!-- b000109 | furniture | pages [4] -->
m

<!-- b000110 | furniture | pages [4] -->
m

<!-- b000111 | furniture | pages [4] -->
m

<!-- b000112 | furniture | pages [4] -->
m

<!-- b000113 | furniture | pages [4] -->
m

<!-- b000114 | furniture | pages [4] -->
m

<!-- b000115 | furniture | pages [4] -->
m

<!-- b000116 | furniture | pages [4] -->
m

<!-- b000117 | furniture | pages [4] -->
m

<!-- b000118 | furniture | pages [4] -->
m

<!-- b000119 | furniture | pages [4] -->
m

<!-- b000120 | furniture | pages [4] -->
m

<!-- b000121 | furniture | pages [4] -->
m

<!-- b000122 | furniture | pages [4] -->
m

<!-- b000123 | furniture | pages [4] -->
m

<!-- b000124 | furniture | pages [4] -->
m

<!-- b000125 | furniture | pages [4] -->
m

<!-- b000126 | furniture | pages [4] -->
m

<!-- b000127 | furniture | pages [4] -->
m

<!-- b000128 | furniture | pages [4] -->
m

<!-- b000129 | furniture | pages [4] -->
m

<!-- b000130 | furniture | pages [4] -->
m

<!-- b000131 | furniture | pages [4] -->
m

<!-- b000132 | furniture | pages [4] -->
m

<!-- b000133 | furniture | pages [4] -->
m

<!-- b000134 | furniture | pages [4] -->
m

<!-- b000135 | furniture | pages [4] -->
m

<!-- b000136 | furniture | pages [4] -->
m

<!-- b000137 | furniture | pages [4] -->
m

<!-- b000138 | furniture | pages [4] -->
m

<!-- b000139 | furniture | pages [4] -->
m

<!-- b000140 | furniture | pages [4] -->
m

<!-- b000141 | furniture | pages [4] -->
m

<!-- b000142 | furniture | pages [4] -->
m

<!-- b000143 | furniture | pages [4] -->
m

<!-- b000144 | furniture | pages [4] -->
m

<!-- b000145 | furniture | pages [4] -->
m

<!-- b000146 | furniture | pages [4] -->
m

<!-- b000147 | furniture | pages [4] -->
m

<!-- b000148 | furniture | pages [4] -->
m

<!-- b000149 | furniture | pages [4] -->
m

<!-- b000150 | furniture | pages [4] -->
m

<!-- b000151 | furniture | pages [4] -->
m

<!-- b000152 | furniture | pages [4] -->
m

<!-- b000153 | furniture | pages [4] -->
m

<!-- b000154 | furniture | pages [4] -->
m

<!-- b000155 | furniture | pages [4] -->
m

<!-- b000156 | furniture | pages [4] -->
m

<!-- b000157 | furniture | pages [4] -->
m

<!-- b000158 | furniture | pages [4] -->
m

<!-- b000159 | furniture | pages [4] -->
m

<!-- b000160 | furniture | pages [4] -->
m

<!-- b000161 | furniture | pages [4] -->
m

<!-- b000162 | furniture | pages [4] -->
m

<!-- b000163 | furniture | pages [4] -->
m

<!-- b000164 | furniture | pages [4] -->
m

<!-- b000165 | furniture | pages [4] -->
m

<!-- b000166 | furniture | pages [4] -->
m

<!-- b000167 | furniture | pages [4] -->
m

<!-- b000168 | furniture | pages [4] -->
m

<!-- b000169 | furniture | pages [4] -->
m

<!-- b000170 | furniture | pages [4] -->
m

<!-- b000171 | furniture | pages [4] -->
m

<!-- b000172 | furniture | pages [4] -->
m

<!-- b000173 | furniture | pages [4] -->
m

<!-- b000174 | furniture | pages [4] -->
m

<!-- b000175 | furniture | pages [4] -->
m

<!-- b000176 | furniture | pages [4] -->
m

<!-- b000177 | furniture | pages [4] -->
m

<!-- b000178 | furniture | pages [4] -->
m

<!-- b000179 | furniture | pages [4] -->
m

<!-- b000180 | furniture | pages [4] -->
m

<!-- b000181 | furniture | pages [4] -->
m

<!-- b000182 | furniture | pages [4] -->
m

<!-- b000183 | furniture | pages [4] -->
m

<!-- b000184 | furniture | pages [4] -->
m

<!-- b000185 | furniture | pages [4] -->
m

<!-- b000186 | furniture | pages [4] -->
m

<!-- b000187 | furniture | pages [4] -->
m

<!-- b000188 | furniture | pages [4] -->
m

<!-- b000189 | furniture | pages [4] -->
m

<!-- b000190 | furniture | pages [4] -->
m

<!-- b000191 | furniture | pages [4] -->
m

<!-- b000192 | furniture | pages [4] -->
m

<!-- b000193 | furniture | pages [4] -->
m

<!-- b000194 | furniture | pages [4] -->
m

<!-- b000195 | furniture | pages [4] -->
m

<!-- b000196 | furniture | pages [4] -->
m

<!-- b000197 | furniture | pages [4] -->
m

<!-- b000198 | furniture | pages [4] -->
m

<!-- b000199 | furniture | pages [4] -->
m

<!-- b000200 | furniture | pages [4] -->
m

<!-- b000201 | furniture | pages [4] -->
m

<!-- b000202 | furniture | pages [4] -->
m

<!-- b000203 | furniture | pages [4] -->
m

<!-- b000204 | furniture | pages [4] -->
m

<!-- b000205 | furniture | pages [4] -->
m

<!-- b000206 | furniture | pages [4] -->
m

<!-- b000207 | furniture | pages [4] -->
m

<!-- b000208 | furniture | pages [4] -->
m

<!-- b000209 | furniture | pages [4] -->
m

<!-- b000210 | furniture | pages [4] -->
m

<!-- b000211 | furniture | pages [4] -->
m

<!-- b000212 | furniture | pages [4] -->
m

<!-- b000213 | furniture | pages [4] -->
m

<!-- b000214 | furniture | pages [4] -->
m

<!-- b000215 | furniture | pages [4] -->
m

<!-- b000216 | furniture | pages [4] -->
m

<!-- b000217 | furniture | pages [4] -->
m

<!-- b000218 | furniture | pages [4] -->
m

<!-- b000219 | furniture | pages [4] -->
m

<!-- b000220 | furniture | pages [4] -->
m

<!-- b000221 | furniture | pages [4] -->
m

<!-- b000222 | furniture | pages [4] -->
m

<!-- b000223 | furniture | pages [4] -->
m

<!-- b000224 | furniture | pages [4] -->
m

<!-- b000225 | furniture | pages [4] -->
m

<!-- b000226 | furniture | pages [4] -->
m

<!-- b000227 | furniture | pages [4] -->
m

<!-- b000228 | furniture | pages [4] -->
m

<!-- b000229 | furniture | pages [4] -->
m

<!-- b000230 | furniture | pages [4] -->
m

<!-- b000231 | furniture | pages [4] -->
m

<!-- b000232 | furniture | pages [4] -->
m

<!-- b000233 | furniture | pages [4] -->
m

<!-- b000234 | furniture | pages [4] -->
m

<!-- b000235 | furniture | pages [4] -->
m

<!-- b000236 | furniture | pages [4] -->
m

<!-- b000237 | furniture | pages [4] -->
m

<!-- b000238 | furniture | pages [4] -->
m

<!-- b000239 | furniture | pages [4] -->
m

<!-- b000240 | furniture | pages [4] -->
m

<!-- b000241 | furniture | pages [4] -->
m

<!-- b000242 | furniture | pages [4] -->
m

<!-- b000243 | furniture | pages [4] -->
m

<!-- b000244 | furniture | pages [4] -->
m

<!-- b000245 | furniture | pages [4] -->
m

<!-- b000246 | furniture | pages [4] -->
m

<!-- b000247 | furniture | pages [4] -->
m

<!-- b000248 | furniture | pages [4] -->
m

<!-- b000249 | furniture | pages [4] -->
m

<!-- b000250 | furniture | pages [4] -->
m

<!-- b000251 | furniture | pages [4] -->
m

<!-- b000252 | furniture | pages [4] -->
m

<!-- b000253 | furniture | pages [4] -->
m

<!-- b000254 | furniture | pages [4] -->
m

<!-- b000255 | furniture | pages [4] -->
m

<!-- b000256 | furniture | pages [4] -->
m

<!-- b000257 | furniture | pages [4] -->
m

<!-- b000258 | furniture | pages [4] -->
m

<!-- b000259 | furniture | pages [4] -->
m

<!-- b000260 | furniture | pages [4] -->
m

<!-- b000261 | furniture | pages [4] -->
m

<!-- b000262 | furniture | pages [4] -->
m

<!-- b000263 | furniture | pages [4] -->
m

<!-- b000264 | furniture | pages [4] -->
m

<!-- b000265 | furniture | pages [4] -->
m

<!-- b000266 | furniture | pages [4] -->
m

<!-- b000267 | furniture | pages [4] -->
m

<!-- b000268 | furniture | pages [4] -->
m

<!-- b000269 | furniture | pages [4] -->
m

<!-- b000270 | furniture | pages [4] -->
m

<!-- b000271 | furniture | pages [4] -->
m

<!-- b000272 | furniture | pages [4] -->
m

<!-- b000273 | furniture | pages [4] -->
m

<!-- b000274 | furniture | pages [4] -->
m

<!-- b000275 | furniture | pages [4] -->
m

<!-- b000276 | furniture | pages [4] -->
m

<!-- b000277 | furniture | pages [4] -->
m

<!-- b000278 | furniture | pages [4] -->
m

<!-- b000279 | furniture | pages [4] -->
m

<!-- b000280 | furniture | pages [4] -->
m

<!-- b000281 | furniture | pages [4] -->
m

<!-- b000282 | furniture | pages [4] -->
m

<!-- b000283 | furniture | pages [4] -->
m

<!-- b000284 | furniture | pages [4] -->
m

<!-- b000285 | furniture | pages [4] -->
m

<!-- b000286 | furniture | pages [4] -->
m

<!-- b000287 | furniture | pages [4] -->
m

<!-- b000288 | furniture | pages [4] -->
m

<!-- b000289 | furniture | pages [4] -->
m

<!-- b000290 | furniture | pages [4] -->
m

<!-- b000291 | furniture | pages [4] -->
m

<!-- b000292 | furniture | pages [4] -->
m

<!-- b000293 | furniture | pages [4] -->
m

<!-- b000294 | furniture | pages [4] -->
m

<!-- b000295 | furniture | pages [4] -->
m

<!-- b000296 | furniture | pages [4] -->
m

<!-- b000297 | furniture | pages [4] -->
m

<!-- b000298 | furniture | pages [4] -->
m

<!-- b000299 | furniture | pages [4] -->
m

<!-- b000300 | furniture | pages [4] -->
m

<!-- b000301 | furniture | pages [4] -->
m

<!-- b000302 | furniture | pages [4] -->
m

<!-- b000303 | furniture | pages [4] -->
m

<!-- b000304 | furniture | pages [4] -->
m

<!-- b000305 | furniture | pages [4] -->
m

<!-- b000306 | furniture | pages [4] -->
m

<!-- b000307 | furniture | pages [4] -->
m

<!-- b000308 | furniture | pages [4] -->
m

<!-- b000309 | furniture | pages [4] -->
m

<!-- b000310 | furniture | pages [4] -->
m

<!-- b000311 | furniture | pages [4] -->
m

<!-- b000312 | furniture | pages [4] -->
m

<!-- b000313 | furniture | pages [4] -->
m

<!-- b000314 | furniture | pages [4] -->
m

<!-- b000315 | furniture | pages [4] -->
m

<!-- b000316 | furniture | pages [4] -->
m

<!-- b000317 | furniture | pages [4] -->
m

<!-- b000318 | furniture | pages [4] -->
m

<!-- b000319 | furniture | pages [4] -->
m

<!-- b000320 | furniture | pages [4] -->
m

<!-- b000321 | furniture | pages [4] -->
m

<!-- b000322 | furniture | pages [4] -->
m

<!-- b000323 | furniture | pages [4] -->
m

<!-- b000324 | furniture | pages [4] -->
m

<!-- b000325 | furniture | pages [4] -->
m

<!-- b000326 | furniture | pages [4] -->
m

<!-- b000327 | furniture | pages [4] -->
m

<!-- b000328 | furniture | pages [4] -->
m

<!-- b000329 | furniture | pages [4] -->
m

<!-- b000330 | furniture | pages [4] -->
m

<!-- b000331 | furniture | pages [4] -->
m

<!-- b000332 | furniture | pages [4] -->
m

<!-- b000333 | furniture | pages [4] -->
m

<!-- b000334 | furniture | pages [4] -->
m

<!-- b000335 | furniture | pages [4] -->
m

<!-- b000336 | furniture | pages [4] -->
m

<!-- b000337 | furniture | pages [4] -->
m

<!-- b000338 | furniture | pages [4] -->
m

<!-- b000339 | furniture | pages [4] -->
m

<!-- b000340 | furniture | pages [4] -->
m

<!-- b000341 | furniture | pages [4] -->
m

<!-- b000342 | furniture | pages [4] -->
m

<!-- b000343 | furniture | pages [4] -->
m

<!-- b000344 | furniture | pages [4] -->
m

<!-- b000345 | furniture | pages [4] -->
m

<!-- b000346 | furniture | pages [4] -->
m

<!-- b000347 | furniture | pages [4] -->
m

<!-- b000348 | furniture | pages [4] -->
m

<!-- b000349 | furniture | pages [4] -->
m

<!-- b000350 | furniture | pages [4] -->
m

<!-- b000351 | furniture | pages [4] -->
m

<!-- b000352 | furniture | pages [4] -->
m

<!-- b000353 | furniture | pages [4] -->
m

<!-- b000354 | furniture | pages [4] -->
m

<!-- b000355 | furniture | pages [4] -->
m

<!-- b000356 | furniture | pages [4] -->
m

<!-- b000357 | furniture | pages [4] -->
m

<!-- b000358 | furniture | pages [4] -->
m

<!-- b000359 | furniture | pages [4] -->
m

<!-- b000360 | furniture | pages [4] -->
m

<!-- b000361 | furniture | pages [4] -->
m

<!-- b000362 | furniture | pages [4] -->
m

<!-- b000363 | furniture | pages [4] -->
m

<!-- b000364 | furniture | pages [4] -->
m

<!-- b000365 | furniture | pages [4] -->
m

<!-- b000366 | furniture | pages [4] -->
m

<!-- b000367 | furniture | pages [4] -->
Page 4 of 26

<!-- b000368 | furniture | pages [4] -->
m

<!-- b000369 | furniture | pages [4] -->
m

<!-- b000370 | furniture | pages [4] -->
m

<!-- b000371 | furniture | pages [4] -->
m

<!-- b000372 | furniture | pages [4] -->
m

<!-- b000373 | furniture | pages [4] -->
m

<!-- b000374 | furniture | pages [4] -->
m

<!-- b000375 | furniture | pages [4] -->
m

<!-- b000376 | furniture | pages [4] -->
m

<!-- b000377 | furniture | pages [4] -->
m

<!-- b000378 | furniture | pages [4] -->
m

<!-- b000379 | furniture | pages [4] -->
m

<!-- b000380 | furniture | pages [4] -->
m

<!-- b000381 | furniture | pages [4] -->
m

<!-- b000382 | furniture | pages [4] -->
m

<!-- b000383 | furniture | pages [4] -->
m

<!-- b000384 | furniture | pages [4] -->
m

<!-- b000385 | furniture | pages [4] -->
m

<!-- b000386 | furniture | pages [4] -->
m

<!-- b000387 | furniture | pages [4] -->
m

<!-- b000388 | furniture | pages [4] -->
m

<!-- b000389 | furniture | pages [4] -->
m

<!-- b000390 | furniture | pages [4] -->
m

<!-- b000391 | furniture | pages [4] -->
m

<!-- b000392 | furniture | pages [4] -->
m

<!-- b000393 | furniture | pages [4] -->
m

<!-- b000394 | furniture | pages [4] -->
m

<!-- b000395 | furniture | pages [4] -->
m

<!-- b000396 | furniture | pages [4] -->
m

<!-- b000397 | furniture | pages [4] -->
m

<!-- b000398 | furniture | pages [4] -->
m

<!-- b000399 | furniture | pages [4] -->
m

<!-- b000400 | furniture | pages [4] -->
m

<!-- b000401 | furniture | pages [4] -->
m

<!-- b000402 | furniture | pages [4] -->
m

<!-- b000403 | furniture | pages [4] -->
m

<!-- b000404 | furniture | pages [4] -->
m

<!-- b000405 | furniture | pages [4] -->
m

<!-- b000406 | furniture | pages [4] -->
m

<!-- b000407 | furniture | pages [4] -->
m

<!-- b000408 | furniture | pages [4] -->
m

<!-- b000409 | furniture | pages [4] -->
m

<!-- b000410 | furniture | pages [4] -->
m

<!-- b000411 | furniture | pages [4] -->
m

<!-- b000412 | furniture | pages [4] -->
m

<!-- b000413 | furniture | pages [4] -->
m

<!-- b000414 | furniture | pages [4] -->
m

<!-- b000415 | furniture | pages [4] -->
m

<!-- b000416 | furniture | pages [4] -->
m

<!-- b000417 | furniture | pages [4] -->
m

<!-- b000418 | furniture | pages [4] -->
m

<!-- b000419 | furniture | pages [4] -->
m

<!-- b000420 | furniture | pages [4] -->
m

<!-- b000421 | furniture | pages [4] -->
m

<!-- b000422 | furniture | pages [4] -->
m

<!-- b000423 | furniture | pages [4] -->
m

<!-- b000424 | furniture | pages [4] -->
m

<!-- b000425 | furniture | pages [4] -->
m

<!-- b000426 | furniture | pages [4] -->
m

<!-- b000427 | furniture | pages [4] -->
m

<!-- b000428 | furniture | pages [4] -->
m

<!-- b000429 | furniture | pages [4] -->
m

<!-- b000430 | furniture | pages [4] -->
m

<!-- b000431 | furniture | pages [4] -->
m

<!-- b000432 | furniture | pages [4] -->
m

<!-- b000433 | furniture | pages [4] -->
m

<!-- b000434 | furniture | pages [4] -->
m

<!-- b000435 | furniture | pages [4] -->
m

<!-- b000436 | furniture | pages [4] -->
m

<!-- b000437 | furniture | pages [4] -->
m

<!-- b000438 | furniture | pages [4] -->
m

<!-- b000439 | furniture | pages [4] -->
m

<!-- b000440 | furniture | pages [4] -->
m

<!-- b000441 | furniture | pages [4] -->
m

<!-- b000442 | furniture | pages [4] -->
m

<!-- b000443 | furniture | pages [4] -->
m

<!-- b000444 | furniture | pages [4] -->
m

<!-- b000445 | furniture | pages [4] -->
m

<!-- b000446 | furniture | pages [4] -->
m

<!-- b000447 | furniture | pages [4] -->
m

<!-- b000448 | furniture | pages [4] -->
m

<!-- b000449 | furniture | pages [4] -->
m

<!-- b000450 | furniture | pages [4] -->
m

<!-- b000451 | furniture | pages [4] -->
m

<!-- b000452 | furniture | pages [4] -->
m

<!-- b000453 | furniture | pages [4] -->
m

<!-- b000454 | furniture | pages [4] -->
m

<!-- b000455 | furniture | pages [4] -->
m

<!-- b000456 | furniture | pages [4] -->
m

<!-- b000457 | furniture | pages [4] -->
m

<!-- b000458 | furniture | pages [4] -->
m

<!-- b000459 | furniture | pages [4] -->
m

<!-- b000460 | furniture | pages [4] -->
m

<!-- b000461 | furniture | pages [4] -->
m

<!-- b000462 | furniture | pages [4] -->
m

<!-- b000463 | furniture | pages [4] -->
m

<!-- b000464 | furniture | pages [4] -->
m

<!-- b000465 | furniture | pages [4] -->
m

<!-- b000466 | furniture | pages [4] -->
m

<!-- b000467 | furniture | pages [4] -->
m

<!-- b000468 | furniture | pages [4] -->
m

<!-- b000469 | furniture | pages [4] -->
m

<!-- b000470 | furniture | pages [4] -->
m

<!-- b000471 | furniture | pages [4] -->
m

<!-- b000472 | furniture | pages [4] -->
m

<!-- b000473 | furniture | pages [4] -->
m

<!-- b000474 | furniture | pages [4] -->
m

<!-- b000475 | furniture | pages [4] -->
m

<!-- b000476 | furniture | pages [4] -->
m

<!-- b000477 | furniture | pages [4] -->
m

<!-- b000478 | furniture | pages [4] -->
m

<!-- b000479 | furniture | pages [4] -->
m

<!-- b000480 | furniture | pages [4] -->
m

<!-- b000481 | furniture | pages [4] -->
m

<!-- b000482 | furniture | pages [4] -->
m

<!-- b000483 | furniture | pages [4] -->
m

<!-- b000484 | furniture | pages [4] -->
m

<!-- b000485 | furniture | pages [4] -->
m

<!-- b000486 | furniture | pages [4] -->
m

<!-- b000487 | furniture | pages [4] -->
m

<!-- b000488 | furniture | pages [4] -->
m

<!-- b000489 | furniture | pages [4] -->
m

<!-- b000490 | furniture | pages [4] -->
m

<!-- b000491 | furniture | pages [4] -->
m

<!-- b000492 | furniture | pages [4] -->
m

<!-- b000493 | furniture | pages [4] -->
m

<!-- b000494 | furniture | pages [4] -->
m

<!-- b000495 | furniture | pages [4] -->
m

<!-- b000496 | furniture | pages [4] -->
m

<!-- b000497 | furniture | pages [4] -->
m

<!-- b000498 | furniture | pages [4] -->
m

<!-- b000499 | furniture | pages [4] -->
m

<!-- b000500 | furniture | pages [4] -->
m

<!-- b000501 | furniture | pages [4] -->
m

<!-- b000502 | furniture | pages [4] -->
m

<!-- b000503 | furniture | pages [4] -->
m

<!-- b000504 | furniture | pages [4] -->
m

<!-- b000505 | furniture | pages [4] -->
m

<!-- b000506 | furniture | pages [4] -->
m

<!-- b000507 | furniture | pages [4] -->
m

<!-- b000508 | furniture | pages [4] -->
m

<!-- b000509 | furniture | pages [4] -->
m

<!-- b000510 | furniture | pages [4] -->
m

<!-- b000511 | furniture | pages [4] -->
m

<!-- b000512 | furniture | pages [4] -->
m

<!-- b000513 | furniture | pages [4] -->
m

<!-- b000514 | furniture | pages [4] -->
m

<!-- b000515 | furniture | pages [4] -->
m

<!-- b000516 | furniture | pages [4] -->
m

<!-- b000517 | furniture | pages [4] -->
m

<!-- b000518 | furniture | pages [4] -->
m

<!-- b000519 | furniture | pages [4] -->
m

<!-- b000520 | furniture | pages [4] -->
m

<!-- b000521 | furniture | pages [4] -->
m

<!-- b000522 | furniture | pages [4] -->
m

<!-- b000523 | furniture | pages [4] -->
m

<!-- b000524 | furniture | pages [4] -->
m

<!-- b000525 | furniture | pages [4] -->
m

<!-- b000526 | furniture | pages [4] -->
m

<!-- b000527 | furniture | pages [4] -->
m

<!-- b000528 | furniture | pages [4] -->
m

<!-- b000529 | furniture | pages [4] -->
m

<!-- b000530 | furniture | pages [4] -->
m

<!-- b000531 | furniture | pages [4] -->
m

<!-- b000532 | furniture | pages [4] -->
m

<!-- b000533 | furniture | pages [4] -->
m

<!-- b000534 | furniture | pages [4] -->
m

<!-- b000535 | furniture | pages [4] -->
m

<!-- b000536 | furniture | pages [4] -->
m

<!-- b000537 | furniture | pages [4] -->
m

<!-- b000538 | furniture | pages [4] -->
m

<!-- b000539 | furniture | pages [4] -->
m

<!-- b000540 | furniture | pages [4] -->
m

<!-- b000541 | furniture | pages [4] -->
m

<!-- b000542 | furniture | pages [4] -->
m

<!-- b000543 | furniture | pages [4] -->
m

<!-- b000544 | furniture | pages [4] -->
m

<!-- b000545 | furniture | pages [4] -->
m

<!-- b000546 | furniture | pages [4] -->
m

<!-- b000547 | furniture | pages [4] -->
m

<!-- b000548 | furniture | pages [4] -->
m

<!-- b000549 | furniture | pages [4] -->
m

<!-- b000550 | furniture | pages [4] -->
m

<!-- b000551 | furniture | pages [4] -->
m

<!-- b000552 | furniture | pages [4] -->
m

<!-- b000553 | furniture | pages [4] -->
m

<!-- b000554 | furniture | pages [4] -->
m

<!-- b000555 | furniture | pages [4] -->
m

<!-- b000556 | furniture | pages [4] -->
m

<!-- b000557 | furniture | pages [4] -->
m

<!-- b000558 | furniture | pages [4] -->
m

<!-- b000559 | furniture | pages [4] -->
m

<!-- b000560 | furniture | pages [4] -->
m

<!-- b000561 | furniture | pages [4] -->
m

<!-- b000562 | furniture | pages [4] -->
m

<!-- b000563 | furniture | pages [4] -->
m

<!-- b000564 | furniture | pages [4] -->
m

<!-- b000565 | furniture | pages [4] -->
m

<!-- b000566 | furniture | pages [4] -->
m

<!-- b000567 | furniture | pages [4] -->
m

<!-- b000568 | furniture | pages [4] -->
m

<!-- b000569 | furniture | pages [4] -->
m

<!-- b000570 | furniture | pages [4] -->
m

<!-- b000571 | furniture | pages [4] -->
m

<!-- b000572 | furniture | pages [4] -->
m

<!-- b000573 | furniture | pages [4] -->
m

<!-- b000574 | furniture | pages [4] -->
m

<!-- b000575 | furniture | pages [4] -->
m

<!-- b000576 | furniture | pages [4] -->
m

<!-- b000577 | furniture | pages [4] -->
m

<!-- b000578 | furniture | pages [4] -->
m

<!-- b000579 | furniture | pages [4] -->
m

<!-- b000580 | furniture | pages [4] -->
m

<!-- b000581 | furniture | pages [4] -->
m

<!-- b000582 | furniture | pages [4] -->
m

<!-- b000583 | furniture | pages [4] -->
m

<!-- b000584 | furniture | pages [4] -->
m

<!-- b000585 | furniture | pages [4] -->
m

<!-- b000586 | furniture | pages [4] -->
m

<!-- b000587 | furniture | pages [4] -->
m

<!-- b000588 | furniture | pages [4] -->
m

<!-- b000589 | furniture | pages [4] -->
m

<!-- b000590 | furniture | pages [4] -->
m

<!-- b000591 | furniture | pages [4] -->
m

<!-- b000592 | furniture | pages [4] -->
m

<!-- b000593 | furniture | pages [4] -->
m

<!-- b000594 | furniture | pages [4] -->
m

<!-- b000595 | furniture | pages [4] -->
m

<!-- b000596 | furniture | pages [4] -->
m

<!-- b000597 | furniture | pages [4] -->
m

<!-- b000598 | furniture | pages [4] -->
m

<!-- b000599 | furniture | pages [4] -->
m

<!-- b000600 | furniture | pages [4] -->
m

<!-- b000601 | furniture | pages [4] -->
m

<!-- b000602 | furniture | pages [4] -->
m

<!-- b000603 | furniture | pages [4] -->
m

<!-- b000604 | furniture | pages [4] -->
m

<!-- b000605 | furniture | pages [4] -->
m

<!-- b000606 | furniture | pages [4] -->
m

<!-- b000607 | furniture | pages [4] -->
m

<!-- b000608 | furniture | pages [4] -->
m

<!-- b000609 | furniture | pages [4] -->
m

<!-- b000610 | furniture | pages [4] -->
m

<!-- b000611 | furniture | pages [4] -->
m

<!-- b000612 | furniture | pages [4] -->
m

<!-- b000613 | furniture | pages [4] -->
m

<!-- b000614 | furniture | pages [4] -->
m

<!-- b000615 | furniture | pages [4] -->
m

<!-- b000616 | furniture | pages [4] -->
m

<!-- b000617 | furniture | pages [4] -->
m

<!-- b000618 | furniture | pages [4] -->
m

<!-- b000619 | furniture | pages [4] -->
m

<!-- b000620 | furniture | pages [4] -->
m

<!-- b000621 | furniture | pages [4] -->
m

<!-- b000622 | furniture | pages [4] -->
m

<!-- b000623 | furniture | pages [4] -->
m

<!-- b000624 | furniture | pages [4] -->
m

<!-- b000625 | furniture | pages [4] -->
m

<!-- b000626 | furniture | pages [4] -->
m

<!-- b000627 | furniture | pages [4] -->
m

<!-- b000628 | furniture | pages [4] -->
m

<!-- b000629 | furniture | pages [4] -->
m

<!-- b000630 | furniture | pages [4] -->
m

<!-- b000631 | furniture | pages [4] -->
m

<!-- b000632 | furniture | pages [4] -->
m

<!-- b000633 | furniture | pages [4] -->
m

<!-- b000634 | furniture | pages [4] -->
m

<!-- b000635 | furniture | pages [4] -->
m

<!-- b000636 | furniture | pages [4] -->
m

<!-- b000637 | furniture | pages [4] -->
m

<!-- b000638 | furniture | pages [4] -->
m

<!-- b000639 | furniture | pages [4] -->
m

<!-- b000640 | furniture | pages [4] -->
m

<!-- b000641 | furniture | pages [4] -->
m

<!-- b000642 | prose | pages [4] -->
m

<!-- b000643 | prose | pages [4] -->
m

<!-- b000644 | prose | pages [4] -->
m

<!-- b000645 | prose | pages [4] -->
m

<!-- b000646 | prose | pages [4] -->
m

<!-- b000647 | prose | pages [4] -->
m

<!-- b000648 | prose | pages [4] -->
m

<!-- b000649 | prose | pages [4] -->
m

<!-- b000650 | prose | pages [4] -->
m

<!-- b000651 | prose | pages [4] -->
m

<!-- b000652 | prose | pages [4] -->
m

<!-- b000653 | prose | pages [4] -->
m

<!-- b000654 | prose | pages [4] -->
m

<!-- b000655 | prose | pages [4] -->
m

<!-- b000656 | prose | pages [4] -->
m

<!-- b000657 | prose | pages [4] -->
m

<!-- b000658 | prose | pages [4] -->
m

<!-- b000659 | prose | pages [4] -->
m

<!-- b000660 | prose | pages [4] -->
m

<!-- b000661 | prose | pages [4] -->
m

<!-- b000662 | prose | pages [4] -->
m

<!-- b000663 | prose | pages [4] -->
m

<!-- b000664 | prose | pages [4] -->
m

<!-- b000665 | prose | pages [4] -->
m

<!-- b000666 | prose | pages [4] -->
m

<!-- b000667 | prose | pages [4] -->
m

<!-- b000668 | prose | pages [4] -->
m

<!-- b000669 | prose | pages [4] -->
m

<!-- b000670 | prose | pages [4] -->
m

<!-- b000671 | prose | pages [4] -->
m

<!-- b000672 | prose | pages [4] -->
m

<!-- b000673 | prose | pages [4] -->
m

<!-- b000674 | prose | pages [4] -->
m

<!-- b000675 | prose | pages [4] -->
m

<!-- b000676 | prose | pages [4] -->
m

<!-- b000677 | prose | pages [4] -->
m

<!-- b000678 | prose | pages [4] -->
m

<!-- b000679 | prose | pages [4] -->
m

<!-- b000680 | prose | pages [4] -->
m

<!-- b000681 | prose | pages [4] -->
m

<!-- b000682 | prose | pages [4] -->
m

<!-- b000683 | prose | pages [4] -->
m

<!-- b000684 | prose | pages [4] -->
m

<!-- b000685 | prose | pages [4] -->
m

<!-- b000686 | prose | pages [4] -->
m

<!-- b000687 | prose | pages [4] -->
m

<!-- b000688 | prose | pages [4] -->
m

<!-- b000689 | prose | pages [4] -->
m

<!-- b000690 | prose | pages [4] -->
m

<!-- b000691 | prose | pages [4] -->
m

<!-- b000692 | prose | pages [4] -->
m

<!-- b000693 | prose | pages [4] -->
m

<!-- b000694 | prose | pages [4] -->
m

<!-- b000695 | prose | pages [4] -->
m

<!-- b000696 | prose | pages [4] -->
m

<!-- b000697 | prose | pages [4] -->
m

<!-- b000698 | prose | pages [4] -->
m

<!-- b000699 | prose | pages [4] -->
m

<!-- b000700 | prose | pages [4] -->
m

<!-- b000701 | prose | pages [4] -->
m

<!-- b000702 | prose | pages [4] -->
m

<!-- b000703 | prose | pages [4] -->
m

<!-- b000704 | prose | pages [4] -->
m

<!-- b000705 | prose | pages [4] -->
m

<!-- b000706 | prose | pages [4] -->
m

<!-- b000707 | prose | pages [4] -->
m

<!-- b000708 | prose | pages [4] -->
m

<!-- b000709 | prose | pages [4] -->
m

<!-- b000710 | prose | pages [4] -->
m

<!-- b000711 | prose | pages [4] -->
m

<!-- b000712 | prose | pages [4] -->
m

<!-- b000713 | prose | pages [4] -->
m

<!-- b000714 | prose | pages [4] -->
m

<!-- b000715 | prose | pages [4] -->
m

<!-- b000716 | prose | pages [4] -->
m

<!-- b000717 | prose | pages [4] -->
m

<!-- b000718 | prose | pages [4] -->
m

<!-- b000719 | prose | pages [4] -->
m

<!-- b000720 | prose | pages [4] -->
m

<!-- b000721 | prose | pages [4] -->
m

<!-- b000722 | prose | pages [4] -->
m

<!-- b000723 | prose | pages [4] -->
m

<!-- b000724 | prose | pages [4] -->
m

<!-- b000725 | prose | pages [4] -->
m

<!-- b000726 | prose | pages [4] -->
m

<!-- b000727 | prose | pages [4] -->
m

<!-- b000728 | prose | pages [4] -->
m

<!-- b000729 | prose | pages [4] -->
m

<!-- b000730 | prose | pages [4] -->
m

<!-- b000731 | prose | pages [4] -->
m

<!-- b000732 | prose | pages [4] -->
m

<!-- b000733 | prose | pages [4] -->
m

<!-- b000734 | prose | pages [4] -->
m

<!-- b000735 | prose | pages [4] -->
m

<!-- b000736 | prose | pages [4] -->
m

<!-- b000737 | prose | pages [4] -->
m

<!-- b000738 | prose | pages [4] -->
m

<!-- b000739 | prose | pages [4] -->
m

<!-- b000740 | prose | pages [4] -->
m

<!-- b000741 | prose | pages [4] -->
m

<!-- b000742 | prose | pages [4] -->
m

<!-- b000743 | prose | pages [4] -->
m

<!-- b000744 | prose | pages [4] -->
m

<!-- b000745 | heading | pages [4] -->
Assumptions and Justification

<!-- b000746 | prose | pages [4] -->
2

<!-- b000747 | prose | pages [4] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified.

<!-- b000748 | prose | pages [4] -->
• The analysis and models are exclusively based on the provided datasets from the 2016, 2020, and 2024 Olympic Games. The three latest Olympic Games provide the most current and relevant data for insights into performance trends, ensuring the analysis is based on representative and applicable information.

<!-- b000749 | prose | pages [4] -->
• The performance of new entrants in their first Olympic participation is on par with that of athletes who will not compete in future Olympic Games. Olympic debuts and retirements are similar in that they both involve challenges such as inexperience or the end of a career, ensuring consistent participation by athletes.

<!-- b000750 | prose | pages [4] -->
• Russia and Belarus are excluded from the medal table in 2028. Athletes from Russia and Belarus competed without their national flags at the 2024 Olympics, indicating they will likely face the same restrictions in 2028.

<!-- b000751 | prose | pages [4] -->
• The disturbance terms in both the multiple regression and regression discontinuity

<!-- b000752 | heading | pages [4] -->
models follow independent normal distributions. The errors are normally distributed

<!-- b000753 | prose | pages [4] -->
with a mean of zero and constant variance, ensuring valid statistical tests and reliable model estimates.

<!-- b000754 | prose | pages [4] -->
• The assumption is made that the 2028 Olympic Games will proceed without signifi-

<!-- b000755 | heading | pages [4] -->
cant global disruptions. “This assumption expects no major global disruptions, ensuring

<!-- b000756 | prose | pages [4] -->
the 2028 Games proceed as planned and the analysis aligns with historical trends.”

<!-- b000757 | prose | pages [4] -->
关注数学模型

<!-- b000758 | furniture | pages [4] -->
2

<!-- b000759 | furniture | pages [4] -->
MATHmodels

<!-- b000760 | furniture | pages [4] -->
获取更多资讯

<!-- b000761 | furniture | pages [5] -->
Team # 2503389

<!-- b000762 | furniture | pages [5] -->
Page 5 of 26

<!-- b000763 | prose | pages [5] -->
• Medal counts are analyzed at the sports level, inferring event-level data. We aggre- gate the data from individual events within each sport to mitigate variability from fluctu- ations in the number of events.

<!-- b000764 | prose | pages [5] -->
3

<!-- b000765 | heading | pages [5] -->
Notations

<!-- b000766 | heading | pages [5] -->
Symbols

<!-- b000767 | prose | pages [5] -->
Description Unit

<!-- b000768 | prose | pages [5] -->
Predicted medal count (total medals or gold medals) Y1, Y2 Medals

<!-- b000769 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000770 | prose | pages [5] -->
Competitiveness index XComp Athlete pool XAth Host boost indicator XHost Historical momentum XHist Award-winning rate AWR Regression coefficients β0, β1, β2, β3, β4 ˆPi Dimensionless Dimensionless Binary Dimensionless Percentage (%) - Combined prediction for i-th instance Medals Weights for MLR and NN models wMLR, wNN PE2

<!-- b000771 | prose | pages [5] -->
MLR, PE2

<!-- b000772 | prose | pages [5] -->
-

<!-- b000773 | prose | pages [5] -->
Mean squared prediction errors for MLR and NN NN -

<!-- b000774 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000775 | prose | pages [5] -->
where we define the main parameters while specific value of those parameters will be given later.

<!-- b000776 | prose | pages [5] -->
4 Data Preprocessing

<!-- b000777 | prose | pages [5] -->
4.1 Data Cleaning and Adjustments

<!-- b000778 | prose | pages [5] -->
4.1.1 Replacement Examples

<!-- b000779 | caption | pages [5] -->
Table 1: Standardized Olympic Data Adjustments Table

<!-- b000780 | prose | pages [5] -->
Category Original Name

<!-- b000781 | prose | pages [5] -->
Country Name Changes Great Britain Macedonia

<!-- b000782 | prose | pages [5] -->
Language Substitutions Cote d’Ivoire Cape Verde

<!-- b000783 | prose | pages [5] -->
Standardized Name

<!-- b000784 | prose | pages [5] -->
United Kingdom North Macedonia

<!-- b000785 | prose | pages [5] -->
Ivory Coast Cabo Verde

<!-- b000786 | prose | pages [5] -->
Individual Olympic AthletesIOC2025 Independent Olympic Athletes Synonym Replacements

<!-- b000787 | prose | pages [5] -->
Refugee AthletesIOC2025 Refugee Olympic Team

<!-- b000788 | prose | pages [5] -->
NOC Consistency ROC (Russia, 2020) Russia RUS (Russia, pre-2020) Russia

<!-- b000789 | prose | pages [5] -->
Cycling (as a single Sport) Sports Merging (2016) Split into Events Canoeing (as a single Sport)

<!-- b000790 | prose | pages [5] -->
4.2 Data Exploration

<!-- b000791 | prose | pages [5] -->
4.2.1 Medal Flow Analysis Across Countries

<!-- b000792 | prose | pages [5] -->
Split into Events

<!-- b000793 | caption | pages [5] -->
Figure 1 presents a Sankey diagram highlighting key medal flow patterns during the 2024

<!-- b000794 | prose | pages [5] -->
Olympics:

<!-- b000795 | furniture | pages [6] -->
Team # 2503389

<!-- b000796 | furniture | pages [6] -->
Page 6 of 26

<!-- b000797 | prose | pages [6] -->
• Dominant Sports and Nations: Swimming and athletics contribute significantly to medal tallies in nations like the United States and China.

<!-- b000798 | prose | pages [6] -->
• Strategic Focus: Italy and Australia excel in niche sports, showcasing tailored investment strategies.

<!-- b000799 | prose | pages [6] -->
m

<!-- b000800 | prose | pages [6] -->
m

<!-- b000801 | prose | pages [6] -->
m

<!-- b000802 | prose | pages [6] -->
m

<!-- b000803 | prose | pages [6] -->
m

<!-- b000804 | prose | pages [6] -->
m

<!-- b000805 | prose | pages [6] -->
m

<!-- b000806 | prose | pages [6] -->
m

<!-- b000807 | prose | pages [6] -->
m

<!-- b000808 | prose | pages [6] -->
m

<!-- b000809 | prose | pages [6] -->
m

<!-- b000810 | prose | pages [6] -->
m

<!-- b000811 | prose | pages [6] -->
m

<!-- b000812 | prose | pages [6] -->
m

<!-- b000813 | prose | pages [6] -->
m

<!-- b000814 | prose | pages [6] -->
m

<!-- b000815 | prose | pages [6] -->
m

<!-- b000816 | prose | pages [6] -->
m

<!-- b000817 | prose | pages [6] -->
m

<!-- b000818 | prose | pages [6] -->
m

<!-- b000819 | prose | pages [6] -->
m

<!-- b000820 | prose | pages [6] -->
m

<!-- b000821 | prose | pages [6] -->
m

<!-- b000822 | prose | pages [6] -->
m

<!-- b000823 | prose | pages [6] -->
m

<!-- b000824 | prose | pages [6] -->
m

<!-- b000825 | prose | pages [6] -->
m

<!-- b000826 | prose | pages [6] -->
m

<!-- b000827 | prose | pages [6] -->
m

<!-- b000828 | prose | pages [6] -->
m

<!-- b000829 | prose | pages [6] -->
m

<!-- b000830 | prose | pages [6] -->
m

<!-- b000831 | prose | pages [6] -->
m

<!-- b000832 | prose | pages [6] -->
m

<!-- b000833 | prose | pages [6] -->
m

<!-- b000834 | prose | pages [6] -->
m

<!-- b000835 | prose | pages [6] -->
m

<!-- b000836 | prose | pages [6] -->
m

<!-- b000837 | prose | pages [6] -->
m

<!-- b000838 | prose | pages [6] -->
m

<!-- b000839 | prose | pages [6] -->
m

<!-- b000840 | prose | pages [6] -->
m

<!-- b000841 | prose | pages [6] -->
m

<!-- b000842 | prose | pages [6] -->
m

<!-- b000843 | prose | pages [6] -->
m

<!-- b000844 | prose | pages [6] -->
m

<!-- b000845 | prose | pages [6] -->
m

<!-- b000846 | prose | pages [6] -->
m

<!-- b000847 | prose | pages [6] -->
m

<!-- b000848 | prose | pages [6] -->
m

<!-- b000849 | prose | pages [6] -->
m

<!-- b000850 | prose | pages [6] -->
m

<!-- b000851 | prose | pages [6] -->
m

<!-- b000852 | prose | pages [6] -->
m

<!-- b000853 | prose | pages [6] -->
m

<!-- b000854 | prose | pages [6] -->
m

<!-- b000855 | prose | pages [6] -->
m

<!-- b000856 | prose | pages [6] -->
m

<!-- b000857 | prose | pages [6] -->
m

<!-- b000858 | prose | pages [6] -->
m

<!-- b000859 | prose | pages [6] -->
m

<!-- b000860 | prose | pages [6] -->
m

<!-- b000861 | prose | pages [6] -->
m

<!-- b000862 | prose | pages [6] -->
m

<!-- b000863 | prose | pages [6] -->
m

<!-- b000864 | prose | pages [6] -->
m

<!-- b000865 | prose | pages [6] -->
m

<!-- b000866 | prose | pages [6] -->
m

<!-- b000867 | prose | pages [6] -->
m

<!-- b000868 | prose | pages [6] -->
m

<!-- b000869 | prose | pages [6] -->
m

<!-- b000870 | prose | pages [6] -->
m

<!-- b000871 | prose | pages [6] -->
m

<!-- b000872 | prose | pages [6] -->
m

<!-- b000873 | prose | pages [6] -->
m

<!-- b000874 | prose | pages [6] -->
m

<!-- b000875 | prose | pages [6] -->
m

<!-- b000876 | prose | pages [6] -->
m

<!-- b000877 | prose | pages [6] -->
m

<!-- b000878 | prose | pages [6] -->
m

<!-- b000879 | prose | pages [6] -->
m

<!-- b000880 | prose | pages [6] -->
m

<!-- b000881 | prose | pages [6] -->
m

<!-- b000882 | prose | pages [6] -->
m

<!-- b000883 | prose | pages [6] -->
m

<!-- b000884 | prose | pages [6] -->
m

<!-- b000885 | prose | pages [6] -->
m

<!-- b000886 | prose | pages [6] -->
m

<!-- b000887 | prose | pages [6] -->
m

<!-- b000888 | prose | pages [6] -->
m

<!-- b000889 | prose | pages [6] -->
m

<!-- b000890 | prose | pages [6] -->
m

<!-- b000891 | prose | pages [6] -->
m

<!-- b000892 | prose | pages [6] -->
m

<!-- b000893 | prose | pages [6] -->
m

<!-- b000894 | prose | pages [6] -->
m

<!-- b000895 | prose | pages [6] -->
m

<!-- b000896 | prose | pages [6] -->
m

<!-- b000897 | prose | pages [6] -->
m

<!-- b000898 | prose | pages [6] -->
m

<!-- b000899 | prose | pages [6] -->
m

<!-- b000900 | prose | pages [6] -->
m

<!-- b000901 | prose | pages [6] -->
m

<!-- b000902 | prose | pages [6] -->
m

<!-- b000903 | prose | pages [6] -->
m

<!-- b000904 | prose | pages [6] -->
m

<!-- b000905 | prose | pages [6] -->
m

<!-- b000906 | prose | pages [6] -->
m

<!-- b000907 | prose | pages [6] -->
m

<!-- b000908 | prose | pages [6] -->
m

<!-- b000909 | prose | pages [6] -->
m

<!-- b000910 | prose | pages [6] -->
m

<!-- b000911 | prose | pages [6] -->
m

<!-- b000912 | prose | pages [6] -->
m

<!-- b000913 | prose | pages [6] -->
m

<!-- b000914 | prose | pages [6] -->
m

<!-- b000915 | prose | pages [6] -->
m

<!-- b000916 | prose | pages [6] -->
m

<!-- b000917 | prose | pages [6] -->
m

<!-- b000918 | prose | pages [6] -->
m

<!-- b000919 | prose | pages [6] -->
m

<!-- b000920 | prose | pages [6] -->
m

<!-- b000921 | prose | pages [6] -->
m

<!-- b000922 | prose | pages [6] -->
m

<!-- b000923 | prose | pages [6] -->
m

<!-- b000924 | prose | pages [6] -->
m

<!-- b000925 | prose | pages [6] -->
m

<!-- b000926 | prose | pages [6] -->
m

<!-- b000927 | prose | pages [6] -->
m

<!-- b000928 | prose | pages [6] -->
m

<!-- b000929 | prose | pages [6] -->
m

<!-- b000930 | prose | pages [6] -->
m

<!-- b000931 | prose | pages [6] -->
m

<!-- b000932 | prose | pages [6] -->
m

<!-- b000933 | prose | pages [6] -->
m

<!-- b000934 | prose | pages [6] -->
m

<!-- b000935 | prose | pages [6] -->
m

<!-- b000936 | prose | pages [6] -->
m

<!-- b000937 | prose | pages [6] -->
m

<!-- b000938 | prose | pages [6] -->
m

<!-- b000939 | prose | pages [6] -->
m

<!-- b000940 | prose | pages [6] -->
m

<!-- b000941 | prose | pages [6] -->
m

<!-- b000942 | prose | pages [6] -->
m

<!-- b000943 | prose | pages [6] -->
m

<!-- b000944 | prose | pages [6] -->
m

<!-- b000945 | prose | pages [6] -->
m

<!-- b000946 | prose | pages [6] -->
m

<!-- b000947 | prose | pages [6] -->
m

<!-- b000948 | prose | pages [6] -->
m

<!-- b000949 | prose | pages [6] -->
m

<!-- b000950 | prose | pages [6] -->
m

<!-- b000951 | prose | pages [6] -->
m

<!-- b000952 | prose | pages [6] -->
m

<!-- b000953 | prose | pages [6] -->
m

<!-- b000954 | prose | pages [6] -->
m

<!-- b000955 | prose | pages [6] -->
m

<!-- b000956 | prose | pages [6] -->
m

<!-- b000957 | prose | pages [6] -->
m

<!-- b000958 | prose | pages [6] -->
m

<!-- b000959 | prose | pages [6] -->
m

<!-- b000960 | prose | pages [6] -->
m

<!-- b000961 | prose | pages [6] -->
m

<!-- b000962 | prose | pages [6] -->
m

<!-- b000963 | prose | pages [6] -->
m

<!-- b000964 | prose | pages [6] -->
m

<!-- b000965 | prose | pages [6] -->
m

<!-- b000966 | prose | pages [6] -->
m

<!-- b000967 | prose | pages [6] -->
m

<!-- b000968 | prose | pages [6] -->
m

<!-- b000969 | prose | pages [6] -->
m

<!-- b000970 | prose | pages [6] -->
m

<!-- b000971 | prose | pages [6] -->
m

<!-- b000972 | prose | pages [6] -->
m

<!-- b000973 | prose | pages [6] -->
m

<!-- b000974 | prose | pages [6] -->
m

<!-- b000975 | prose | pages [6] -->
m

<!-- b000976 | prose | pages [6] -->
m

<!-- b000977 | prose | pages [6] -->
m

<!-- b000978 | prose | pages [6] -->
m

<!-- b000979 | prose | pages [6] -->
m

<!-- b000980 | prose | pages [6] -->
m

<!-- b000981 | prose | pages [6] -->
m

<!-- b000982 | prose | pages [6] -->
m

<!-- b000983 | prose | pages [6] -->
m

<!-- b000984 | prose | pages [6] -->
m

<!-- b000985 | prose | pages [6] -->
m

<!-- b000986 | prose | pages [6] -->
m

<!-- b000987 | prose | pages [6] -->
m

<!-- b000988 | prose | pages [6] -->
m

<!-- b000989 | prose | pages [6] -->
m

<!-- b000990 | prose | pages [6] -->
m

<!-- b000991 | prose | pages [6] -->
m

<!-- b000992 | prose | pages [6] -->
m

<!-- b000993 | prose | pages [6] -->
m

<!-- b000994 | prose | pages [6] -->
m

<!-- b000995 | prose | pages [6] -->
m

<!-- b000996 | prose | pages [6] -->
m

<!-- b000997 | prose | pages [6] -->
m

<!-- b000998 | prose | pages [6] -->
m

<!-- b000999 | prose | pages [6] -->
m

<!-- b001000 | prose | pages [6] -->
m

<!-- b001001 | prose | pages [6] -->
m

<!-- b001002 | prose | pages [6] -->
m

<!-- b001003 | prose | pages [6] -->
m

<!-- b001004 | prose | pages [6] -->
m

<!-- b001005 | prose | pages [6] -->
m

<!-- b001006 | prose | pages [6] -->
m

<!-- b001007 | prose | pages [6] -->
m

<!-- b001008 | prose | pages [6] -->
m

<!-- b001009 | prose | pages [6] -->
m

<!-- b001010 | prose | pages [6] -->
m

<!-- b001011 | prose | pages [6] -->
m

<!-- b001012 | prose | pages [6] -->
m

<!-- b001013 | prose | pages [6] -->
m

<!-- b001014 | prose | pages [6] -->
m

<!-- b001015 | prose | pages [6] -->
m

<!-- b001016 | prose | pages [6] -->
m

<!-- b001017 | prose | pages [6] -->
m

<!-- b001018 | prose | pages [6] -->
m

<!-- b001019 | prose | pages [6] -->
m

<!-- b001020 | prose | pages [6] -->
m

<!-- b001021 | prose | pages [6] -->
m

<!-- b001022 | prose | pages [6] -->
m

<!-- b001023 | prose | pages [6] -->
m

<!-- b001024 | prose | pages [6] -->
m

<!-- b001025 | prose | pages [6] -->
m

<!-- b001026 | prose | pages [6] -->
m

<!-- b001027 | prose | pages [6] -->
m

<!-- b001028 | prose | pages [6] -->
m

<!-- b001029 | prose | pages [6] -->
m

<!-- b001030 | prose | pages [6] -->
m

<!-- b001031 | prose | pages [6] -->
m

<!-- b001032 | prose | pages [6] -->
m

<!-- b001033 | prose | pages [6] -->
m

<!-- b001034 | prose | pages [6] -->
m

<!-- b001035 | prose | pages [6] -->
m

<!-- b001036 | prose | pages [6] -->
m

<!-- b001037 | prose | pages [6] -->
m

<!-- b001038 | prose | pages [6] -->
m

<!-- b001039 | prose | pages [6] -->
m

<!-- b001040 | prose | pages [6] -->
m

<!-- b001041 | prose | pages [6] -->
m

<!-- b001042 | prose | pages [6] -->
m

<!-- b001043 | prose | pages [6] -->
m

<!-- b001044 | prose | pages [6] -->
m

<!-- b001045 | prose | pages [6] -->
m

<!-- b001046 | prose | pages [6] -->
m

<!-- b001047 | prose | pages [6] -->
m

<!-- b001048 | prose | pages [6] -->
m

<!-- b001049 | prose | pages [6] -->
m

<!-- b001050 | prose | pages [6] -->
m

<!-- b001051 | prose | pages [6] -->
m

<!-- b001052 | prose | pages [6] -->
m

<!-- b001053 | prose | pages [6] -->
m

<!-- b001054 | prose | pages [6] -->
m

<!-- b001055 | prose | pages [6] -->
m

<!-- b001056 | prose | pages [6] -->
m

<!-- b001057 | prose | pages [6] -->
m

<!-- b001058 | prose | pages [6] -->
m

<!-- b001059 | prose | pages [6] -->
m

<!-- b001060 | prose | pages [6] -->
m

<!-- b001061 | prose | pages [6] -->
m

<!-- b001062 | prose | pages [6] -->
m

<!-- b001063 | prose | pages [6] -->
m

<!-- b001064 | prose | pages [6] -->
m

<!-- b001065 | prose | pages [6] -->
m

<!-- b001066 | prose | pages [6] -->
m

<!-- b001067 | prose | pages [6] -->
m

<!-- b001068 | prose | pages [6] -->
m

<!-- b001069 | prose | pages [6] -->
m

<!-- b001070 | prose | pages [6] -->
m

<!-- b001071 | prose | pages [6] -->
m

<!-- b001072 | prose | pages [6] -->
m

<!-- b001073 | prose | pages [6] -->
m

<!-- b001074 | prose | pages [6] -->
m

<!-- b001075 | prose | pages [6] -->
m

<!-- b001076 | prose | pages [6] -->
m

<!-- b001077 | prose | pages [6] -->
m

<!-- b001078 | prose | pages [6] -->
m

<!-- b001079 | prose | pages [6] -->
m

<!-- b001080 | prose | pages [6] -->
m

<!-- b001081 | prose | pages [6] -->
m

<!-- b001082 | prose | pages [6] -->
m

<!-- b001083 | prose | pages [6] -->
m

<!-- b001084 | prose | pages [6] -->
m

<!-- b001085 | prose | pages [6] -->
m

<!-- b001086 | prose | pages [6] -->
m

<!-- b001087 | prose | pages [6] -->
m

<!-- b001088 | prose | pages [6] -->
m

<!-- b001089 | prose | pages [6] -->
m

<!-- b001090 | prose | pages [6] -->
m

<!-- b001091 | prose | pages [6] -->
m

<!-- b001092 | prose | pages [6] -->
m

<!-- b001093 | prose | pages [6] -->
m

<!-- b001094 | prose | pages [6] -->
m

<!-- b001095 | prose | pages [6] -->
m

<!-- b001096 | prose | pages [6] -->
m

<!-- b001097 | prose | pages [6] -->
m

<!-- b001098 | prose | pages [6] -->
m

<!-- b001099 | prose | pages [6] -->
m

<!-- b001100 | prose | pages [6] -->
m

<!-- b001101 | prose | pages [6] -->
m

<!-- b001102 | prose | pages [6] -->
m

<!-- b001103 | prose | pages [6] -->
m

<!-- b001104 | prose | pages [6] -->
m

<!-- b001105 | prose | pages [6] -->
m

<!-- b001106 | prose | pages [6] -->
m

<!-- b001107 | prose | pages [6] -->
m

<!-- b001108 | prose | pages [6] -->
m

<!-- b001109 | prose | pages [6] -->
m

<!-- b001110 | prose | pages [6] -->
m

<!-- b001111 | prose | pages [6] -->
m

<!-- b001112 | prose | pages [6] -->
m

<!-- b001113 | prose | pages [6] -->
m

<!-- b001114 | prose | pages [6] -->
m

<!-- b001115 | prose | pages [6] -->
m

<!-- b001116 | prose | pages [6] -->
m

<!-- b001117 | prose | pages [6] -->
m

<!-- b001118 | prose | pages [6] -->
m

<!-- b001119 | prose | pages [6] -->
m

<!-- b001120 | prose | pages [6] -->
m

<!-- b001121 | prose | pages [6] -->
m

<!-- b001122 | prose | pages [6] -->
m

<!-- b001123 | prose | pages [6] -->
m

<!-- b001124 | prose | pages [6] -->
m

<!-- b001125 | prose | pages [6] -->
m

<!-- b001126 | prose | pages [6] -->
m

<!-- b001127 | prose | pages [6] -->
m

<!-- b001128 | prose | pages [6] -->
m

<!-- b001129 | prose | pages [6] -->
m

<!-- b001130 | prose | pages [6] -->
m

<!-- b001131 | prose | pages [6] -->
m

<!-- b001132 | prose | pages [6] -->
m

<!-- b001133 | prose | pages [6] -->
m

<!-- b001134 | prose | pages [6] -->
m

<!-- b001135 | prose | pages [6] -->
m

<!-- b001136 | prose | pages [6] -->
m

<!-- b001137 | prose | pages [6] -->
m

<!-- b001138 | prose | pages [6] -->
m

<!-- b001139 | prose | pages [6] -->
m

<!-- b001140 | prose | pages [6] -->
m

<!-- b001141 | prose | pages [6] -->
m

<!-- b001142 | prose | pages [6] -->
m

<!-- b001143 | prose | pages [6] -->
m

<!-- b001144 | prose | pages [6] -->
m

<!-- b001145 | prose | pages [6] -->
m

<!-- b001146 | prose | pages [6] -->
m

<!-- b001147 | prose | pages [6] -->
m

<!-- b001148 | prose | pages [6] -->
m

<!-- b001149 | prose | pages [6] -->
m

<!-- b001150 | prose | pages [6] -->
m

<!-- b001151 | prose | pages [6] -->
m

<!-- b001152 | prose | pages [6] -->
m

<!-- b001153 | prose | pages [6] -->
m

<!-- b001154 | prose | pages [6] -->
m

<!-- b001155 | prose | pages [6] -->
m

<!-- b001156 | prose | pages [6] -->
m

<!-- b001157 | prose | pages [6] -->
m

<!-- b001158 | prose | pages [6] -->
m

<!-- b001159 | prose | pages [6] -->
m

<!-- b001160 | prose | pages [6] -->
m

<!-- b001161 | prose | pages [6] -->
m

<!-- b001162 | prose | pages [6] -->
m

<!-- b001163 | prose | pages [6] -->
m

<!-- b001164 | prose | pages [6] -->
m

<!-- b001165 | prose | pages [6] -->
m

<!-- b001166 | prose | pages [6] -->
m

<!-- b001167 | prose | pages [6] -->
m

<!-- b001168 | prose | pages [6] -->
m

<!-- b001169 | prose | pages [6] -->
m

<!-- b001170 | prose | pages [6] -->
m

<!-- b001171 | prose | pages [6] -->
m

<!-- b001172 | prose | pages [6] -->
m

<!-- b001173 | prose | pages [6] -->
m

<!-- b001174 | prose | pages [6] -->
m

<!-- b001175 | prose | pages [6] -->
m

<!-- b001176 | prose | pages [6] -->
m

<!-- b001177 | prose | pages [6] -->
m

<!-- b001178 | prose | pages [6] -->
m

<!-- b001179 | prose | pages [6] -->
m

<!-- b001180 | prose | pages [6] -->
m

<!-- b001181 | prose | pages [6] -->
m

<!-- b001182 | prose | pages [6] -->
m

<!-- b001183 | prose | pages [6] -->
m

<!-- b001184 | prose | pages [6] -->
m

<!-- b001185 | prose | pages [6] -->
m

<!-- b001186 | prose | pages [6] -->
m

<!-- b001187 | prose | pages [6] -->
m

<!-- b001188 | prose | pages [6] -->
m

<!-- b001189 | prose | pages [6] -->
m

<!-- b001190 | prose | pages [6] -->
m

<!-- b001191 | prose | pages [6] -->
m

<!-- b001192 | prose | pages [6] -->
m

<!-- b001193 | prose | pages [6] -->
m

<!-- b001194 | prose | pages [6] -->
m

<!-- b001195 | prose | pages [6] -->
m

<!-- b001196 | prose | pages [6] -->
m

<!-- b001197 | prose | pages [6] -->
m

<!-- b001198 | prose | pages [6] -->
m

<!-- b001199 | prose | pages [6] -->
m

<!-- b001200 | prose | pages [6] -->
m

<!-- b001201 | prose | pages [6] -->
m

<!-- b001202 | prose | pages [6] -->
m

<!-- b001203 | prose | pages [6] -->
m

<!-- b001204 | prose | pages [6] -->
m

<!-- b001205 | prose | pages [6] -->
m

<!-- b001206 | prose | pages [6] -->
m

<!-- b001207 | prose | pages [6] -->
m

<!-- b001208 | prose | pages [6] -->
m

<!-- b001209 | prose | pages [6] -->
m

<!-- b001210 | prose | pages [6] -->
m

<!-- b001211 | prose | pages [6] -->
m

<!-- b001212 | prose | pages [6] -->
m

<!-- b001213 | prose | pages [6] -->
m

<!-- b001214 | prose | pages [6] -->
m

<!-- b001215 | prose | pages [6] -->
m

<!-- b001216 | prose | pages [6] -->
m

<!-- b001217 | prose | pages [6] -->
m

<!-- b001218 | prose | pages [6] -->
m

<!-- b001219 | prose | pages [6] -->
m

<!-- b001220 | prose | pages [6] -->
m

<!-- b001221 | prose | pages [6] -->
m

<!-- b001222 | prose | pages [6] -->
m

<!-- b001223 | prose | pages [6] -->
m

<!-- b001224 | prose | pages [6] -->
m

<!-- b001225 | prose | pages [6] -->
m

<!-- b001226 | prose | pages [6] -->
m

<!-- b001227 | prose | pages [6] -->
m

<!-- b001228 | prose | pages [6] -->
m

<!-- b001229 | prose | pages [6] -->
m

<!-- b001230 | prose | pages [6] -->
m

<!-- b001231 | prose | pages [6] -->
m

<!-- b001232 | prose | pages [6] -->
m

<!-- b001233 | prose | pages [6] -->
m

<!-- b001234 | prose | pages [6] -->
m

<!-- b001235 | prose | pages [6] -->
m

<!-- b001236 | prose | pages [6] -->
m

<!-- b001237 | prose | pages [6] -->
m

<!-- b001238 | prose | pages [6] -->
m

<!-- b001239 | prose | pages [6] -->
m

<!-- b001240 | prose | pages [6] -->
m

<!-- b001241 | prose | pages [6] -->
m

<!-- b001242 | prose | pages [6] -->
m

<!-- b001243 | prose | pages [6] -->
m

<!-- b001244 | prose | pages [6] -->
m

<!-- b001245 | prose | pages [6] -->
m

<!-- b001246 | prose | pages [6] -->
m

<!-- b001247 | prose | pages [6] -->
m

<!-- b001248 | prose | pages [6] -->
m

<!-- b001249 | prose | pages [6] -->
m

<!-- b001250 | prose | pages [6] -->
m

<!-- b001251 | prose | pages [6] -->
m

<!-- b001252 | prose | pages [6] -->
m

<!-- b001253 | prose | pages [6] -->
m

<!-- b001254 | prose | pages [6] -->
m

<!-- b001255 | prose | pages [6] -->
m

<!-- b001256 | prose | pages [6] -->
m

<!-- b001257 | prose | pages [6] -->
m

<!-- b001258 | prose | pages [6] -->
m

<!-- b001259 | prose | pages [6] -->
m

<!-- b001260 | prose | pages [6] -->
m

<!-- b001261 | prose | pages [6] -->
m

<!-- b001262 | prose | pages [6] -->
m

<!-- b001263 | prose | pages [6] -->
m

<!-- b001264 | prose | pages [6] -->
m

<!-- b001265 | prose | pages [6] -->
m

<!-- b001266 | prose | pages [6] -->
m

<!-- b001267 | prose | pages [6] -->
m

<!-- b001268 | prose | pages [6] -->
m

<!-- b001269 | prose | pages [6] -->
m

<!-- b001270 | prose | pages [6] -->
m

<!-- b001271 | prose | pages [6] -->
m

<!-- b001272 | prose | pages [6] -->
m

<!-- b001273 | prose | pages [6] -->
m

<!-- b001274 | prose | pages [6] -->
m

<!-- b001275 | prose | pages [6] -->
m

<!-- b001276 | prose | pages [6] -->
m

<!-- b001277 | prose | pages [6] -->
m

<!-- b001278 | prose | pages [6] -->
m

<!-- b001279 | prose | pages [6] -->
m

<!-- b001280 | prose | pages [6] -->
m

<!-- b001281 | prose | pages [6] -->
m

<!-- b001282 | prose | pages [6] -->
m

<!-- b001283 | prose | pages [6] -->
m

<!-- b001284 | prose | pages [6] -->
m

<!-- b001285 | prose | pages [6] -->
m

<!-- b001286 | prose | pages [6] -->
m

<!-- b001287 | prose | pages [6] -->
m

<!-- b001288 | prose | pages [6] -->
m

<!-- b001289 | prose | pages [6] -->
m

<!-- b001290 | prose | pages [6] -->
m

<!-- b001291 | prose | pages [6] -->
m

<!-- b001292 | prose | pages [6] -->
m

<!-- b001293 | prose | pages [6] -->
m

<!-- b001294 | prose | pages [6] -->
m

<!-- b001295 | prose | pages [6] -->
m

<!-- b001296 | prose | pages [6] -->
m

<!-- b001297 | prose | pages [6] -->
m

<!-- b001298 | prose | pages [6] -->
m

<!-- b001299 | prose | pages [6] -->
m

<!-- b001300 | prose | pages [6] -->
m

<!-- b001301 | prose | pages [6] -->
m

<!-- b001302 | prose | pages [6] -->
m

<!-- b001303 | prose | pages [6] -->
m

<!-- b001304 | prose | pages [6] -->
m

<!-- b001305 | prose | pages [6] -->
m

<!-- b001306 | prose | pages [6] -->
m

<!-- b001307 | prose | pages [6] -->
m

<!-- b001308 | prose | pages [6] -->
m

<!-- b001309 | prose | pages [6] -->
m

<!-- b001310 | prose | pages [6] -->
m

<!-- b001311 | prose | pages [6] -->
m

<!-- b001312 | prose | pages [6] -->
m

<!-- b001313 | prose | pages [6] -->
m

<!-- b001314 | prose | pages [6] -->
m

<!-- b001315 | prose | pages [6] -->
m

<!-- b001316 | prose | pages [6] -->
m

<!-- b001317 | prose | pages [6] -->
m

<!-- b001318 | prose | pages [6] -->
m

<!-- b001319 | prose | pages [6] -->
m

<!-- b001320 | prose | pages [6] -->
m

<!-- b001321 | prose | pages [6] -->
m

<!-- b001322 | prose | pages [6] -->
m

<!-- b001323 | prose | pages [6] -->
m

<!-- b001324 | prose | pages [6] -->
m

<!-- b001325 | prose | pages [6] -->
m

<!-- b001326 | prose | pages [6] -->
m

<!-- b001327 | prose | pages [6] -->
m

<!-- b001328 | prose | pages [6] -->
m

<!-- b001329 | prose | pages [6] -->
m

<!-- b001330 | prose | pages [6] -->
m

<!-- b001331 | prose | pages [6] -->
m

<!-- b001332 | prose | pages [6] -->
m

<!-- b001333 | prose | pages [6] -->
m

<!-- b001334 | prose | pages [6] -->
m

<!-- b001335 | prose | pages [6] -->
m

<!-- b001336 | prose | pages [6] -->
m

<!-- b001337 | prose | pages [6] -->
m

<!-- b001338 | prose | pages [6] -->
m

<!-- b001339 | prose | pages [6] -->
m

<!-- b001340 | prose | pages [6] -->
m

<!-- b001341 | prose | pages [6] -->
m

<!-- b001342 | prose | pages [6] -->
m

<!-- b001343 | prose | pages [6] -->
m

<!-- b001344 | prose | pages [6] -->
m

<!-- b001345 | prose | pages [6] -->
m

<!-- b001346 | prose | pages [6] -->
m

<!-- b001347 | prose | pages [6] -->
m

<!-- b001348 | prose | pages [6] -->
m

<!-- b001349 | prose | pages [6] -->
m

<!-- b001350 | prose | pages [6] -->
m

<!-- b001351 | prose | pages [6] -->
m

<!-- b001352 | prose | pages [6] -->
m

<!-- b001353 | prose | pages [6] -->
m

<!-- b001354 | prose | pages [6] -->
m

<!-- b001355 | prose | pages [6] -->
m

<!-- b001356 | prose | pages [6] -->
m

<!-- b001357 | prose | pages [6] -->
m

<!-- b001358 | prose | pages [6] -->
m

<!-- b001359 | prose | pages [6] -->
m

<!-- b001360 | prose | pages [6] -->
m

<!-- b001361 | prose | pages [6] -->
m

<!-- b001362 | prose | pages [6] -->
m

<!-- b001363 | prose | pages [6] -->
m

<!-- b001364 | prose | pages [6] -->
m

<!-- b001365 | prose | pages [6] -->
m

<!-- b001366 | prose | pages [6] -->
m

<!-- b001367 | prose | pages [6] -->
m

<!-- b001368 | prose | pages [6] -->
m

<!-- b001369 | prose | pages [6] -->
m

<!-- b001370 | prose | pages [6] -->
m

<!-- b001371 | prose | pages [6] -->
m

<!-- b001372 | prose | pages [6] -->
m

<!-- b001373 | prose | pages [6] -->
m

<!-- b001374 | prose | pages [6] -->
m

<!-- b001375 | prose | pages [6] -->
m

<!-- b001376 | prose | pages [6] -->
m

<!-- b001377 | prose | pages [6] -->
m

<!-- b001378 | prose | pages [6] -->
m

<!-- b001379 | prose | pages [6] -->
m

<!-- b001380 | prose | pages [6] -->
m

<!-- b001381 | prose | pages [6] -->
m

<!-- b001382 | prose | pages [6] -->
m

<!-- b001383 | prose | pages [6] -->
m

<!-- b001384 | prose | pages [6] -->
m

<!-- b001385 | prose | pages [6] -->
m

<!-- b001386 | prose | pages [6] -->
m

<!-- b001387 | prose | pages [6] -->
m

<!-- b001388 | prose | pages [6] -->
m

<!-- b001389 | prose | pages [6] -->
m

<!-- b001390 | prose | pages [6] -->
m

<!-- b001391 | prose | pages [6] -->
m

<!-- b001392 | prose | pages [6] -->
m

<!-- b001393 | prose | pages [6] -->
m

<!-- b001394 | prose | pages [6] -->
m

<!-- b001395 | prose | pages [6] -->
m

<!-- b001396 | prose | pages [6] -->
m

<!-- b001397 | prose | pages [6] -->
m

<!-- b001398 | prose | pages [6] -->
m

<!-- b001399 | prose | pages [6] -->
m

<!-- b001400 | prose | pages [6] -->
m

<!-- b001401 | prose | pages [6] -->
m

<!-- b001402 | prose | pages [6] -->
m

<!-- b001403 | prose | pages [6] -->
m

<!-- b001404 | prose | pages [6] -->
m

<!-- b001405 | prose | pages [6] -->
m

<!-- b001406 | prose | pages [6] -->
m

<!-- b001407 | prose | pages [6] -->
m

<!-- b001408 | prose | pages [6] -->
m

<!-- b001409 | prose | pages [6] -->
m

<!-- b001410 | prose | pages [6] -->
m

<!-- b001411 | prose | pages [6] -->
m

<!-- b001412 | prose | pages [6] -->
m

<!-- b001413 | prose | pages [6] -->
m

<!-- b001414 | prose | pages [6] -->
m

<!-- b001415 | prose | pages [6] -->
m

<!-- b001416 | prose | pages [6] -->
m

<!-- b001417 | prose | pages [6] -->
m

<!-- b001418 | prose | pages [6] -->
m

<!-- b001419 | prose | pages [6] -->
m

<!-- b001420 | prose | pages [6] -->
m

<!-- b001421 | prose | pages [6] -->
m

<!-- b001422 | prose | pages [6] -->
m

<!-- b001423 | prose | pages [6] -->
m

<!-- b001424 | prose | pages [6] -->
m

<!-- b001425 | prose | pages [6] -->
m

<!-- b001426 | prose | pages [6] -->
m

<!-- b001427 | prose | pages [6] -->
m

<!-- b001428 | prose | pages [6] -->
m

<!-- b001429 | prose | pages [6] -->
m

<!-- b001430 | prose | pages [6] -->
m

<!-- b001431 | prose | pages [6] -->
m

<!-- b001432 | prose | pages [6] -->
m

<!-- b001433 | prose | pages [6] -->
m

<!-- b001434 | prose | pages [6] -->
m

<!-- b001435 | prose | pages [6] -->
m

<!-- b001436 | prose | pages [6] -->
m

<!-- b001437 | prose | pages [6] -->
m

<!-- b001438 | prose | pages [6] -->
m

<!-- b001439 | prose | pages [6] -->
m

<!-- b001440 | prose | pages [6] -->
m

<!-- b001441 | prose | pages [6] -->
m

<!-- b001442 | prose | pages [6] -->
m

<!-- b001443 | prose | pages [6] -->
m

<!-- b001444 | prose | pages [6] -->
m

<!-- b001445 | prose | pages [6] -->
m

<!-- b001446 | prose | pages [6] -->
m

<!-- b001447 | prose | pages [6] -->
m

<!-- b001448 | prose | pages [6] -->
m

<!-- b001449 | prose | pages [6] -->
m

<!-- b001450 | prose | pages [6] -->
m

<!-- b001451 | prose | pages [6] -->
m

<!-- b001452 | prose | pages [6] -->
m

<!-- b001453 | prose | pages [6] -->
m

<!-- b001454 | prose | pages [6] -->
m

<!-- b001455 | prose | pages [6] -->
m

<!-- b001456 | prose | pages [6] -->
m

<!-- b001457 | prose | pages [6] -->
m

<!-- b001458 | prose | pages [6] -->
m

<!-- b001459 | prose | pages [6] -->
m

<!-- b001460 | prose | pages [6] -->
m

<!-- b001461 | prose | pages [6] -->
m

<!-- b001462 | prose | pages [6] -->
m

<!-- b001463 | prose | pages [6] -->
m

<!-- b001464 | prose | pages [6] -->
m

<!-- b001465 | prose | pages [6] -->
m

<!-- b001466 | prose | pages [6] -->
m

<!-- b001467 | prose | pages [6] -->
m

<!-- b001468 | prose | pages [6] -->
m

<!-- b001469 | prose | pages [6] -->
m

<!-- b001470 | prose | pages [6] -->
m

<!-- b001471 | prose | pages [6] -->
m

<!-- b001472 | prose | pages [6] -->
m

<!-- b001473 | prose | pages [6] -->
m

<!-- b001474 | prose | pages [6] -->
m

<!-- b001475 | prose | pages [6] -->
m

<!-- b001476 | prose | pages [6] -->
m

<!-- b001477 | prose | pages [6] -->
m

<!-- b001478 | prose | pages [6] -->
m

<!-- b001479 | prose | pages [6] -->
m

<!-- b001480 | prose | pages [6] -->
m

<!-- b001481 | prose | pages [6] -->
m

<!-- b001482 | prose | pages [6] -->
m

<!-- b001483 | prose | pages [6] -->
m

<!-- b001484 | prose | pages [6] -->
m

<!-- b001485 | prose | pages [6] -->
m

<!-- b001486 | caption | pages [6] -->
Figure 1: Sankey Diagram Representing Medal Flow Across Countries and Sports (2024

<!-- b001487 | prose | pages [6] -->
Olympics)

<!-- b001488 | prose | pages [6] -->
Multiple Linear Regression-Feedforward Neural Network 5

<!-- b001489 | heading | pages [6] -->
Bootstrap Ensemble Interval Prediction Model with Host

<!-- b001490 | prose | pages [6] -->
Effect

<!-- b001491 | prose | pages [6] -->
5.1

<!-- b001492 | heading | pages [6] -->
Reasons for Model Selection

<!-- b001493 | prose | pages [6] -->
Predicting Olympic medal distributions is a complex regression task. The Multiple Lin- ear Regression (MLR) model is simple and interpretable, effective for linear relationships but limited in capturing non-linear dynamics like the host effect. To address this, the Feedforward

<!-- b001494 | heading | pages [6] -->
Neural Network (FNN) model excels in capturing non-linear patterns and handling diverse

<!-- b001495 | prose | pages [6] -->
datasets with high accuracy. Combining MLR’s simplicity with FNN’s adaptability, we pro- pose a hybrid approach for enhanced medal prediction.

<!-- b001496 | prose | pages [6] -->
5.2

<!-- b001497 | heading | pages [6] -->
Model Construction and Fusion

<!-- b001498 | prose | pages [6] -->
5.2.1

<!-- b001499 | heading | pages [6] -->
MLR-Model Construction

<!-- b001500 | prose | pages [6] -->
Multiple Linear Regression Formulation

<!-- b001501 | prose | pages [6] -->
The model is formulated as:

<!-- b001502 | prose | pages [6] -->
Yi = β0 + β1XComp + β2XAth + β3XHost + β4XHist + ϵ,

<!-- b001503 | prose | pages [6] -->
Feature Selection

<!-- b001504 | prose | pages [6] -->
(i = 1, 2)

<!-- b001505 | prose | pages [6] -->
关注数学模型

<!-- b001506 | furniture | pages [6] -->
2

<!-- b001507 | furniture | pages [6] -->
MATHmodels

<!-- b001508 | furniture | pages [6] -->
获取更多资讯

<!-- b001509 | furniture | pages [7] -->
Team # 2503389

<!-- b001510 | furniture | pages [7] -->
Page 7 of 26

<!-- b001511 | caption | pages [7] -->
Table 2: Key Predictive Features and Their Mathematical Definitions

<!-- b001512 | prose | pages [7] -->
Feature Interpretation Mathematical Formula

<!-- b001513 | prose | pages [7] -->
Boost from hosting the

<!-- b001514 | prose | pages [7] -->
Host Boost

<!-- b001515 | prose | pages [7] -->
Olympics, quantified as

<!-- b001516 | prose | pages [7] -->
(XHost)

<!-- b001517 | prose | pages [7] -->
{

<!-- b001518 | prose | pages [7] -->
)

<!-- b001519 | prose | pages [7] -->
( Rh −¯Rn

<!-- b001520 | prose | pages [7] -->
if Host Nation 1 + ∆R,

<!-- b001521 | prose | pages [7] -->
an additional medal im- provement rate.

<!-- b001522 | prose | pages [7] -->
∆R = median

<!-- b001523 | prose | pages [7] -->
XHost =

<!-- b001524 | prose | pages [7] -->
,

<!-- b001525 | prose | pages [7] -->
¯Rn

<!-- b001526 | prose | pages [7] -->
Otherwise 0,

<!-- b001527 | prose | pages [7] -->
Rh: Host medal rate, ¯Rn: Non-host

<!-- b001528 | prose | pages [7] -->
微信公众号：数学模型

<!-- b001529 | prose | pages [7] -->
avg. rate.

<!-- b001530 | prose | pages [7] -->
Reflects athlete partici-

<!-- b001531 | prose | pages [7] -->
Athlete Pool

<!-- b001532 | prose | pages [7] -->
2 X

<!-- b001533 | prose | pages [7] -->
pation trends, adjusted

<!-- b001534 | prose | pages [7] -->
(XAth)

<!-- b001535 | prose | pages [7] -->
XAth =

<!-- b001536 | prose | pages [7] -->
NT−t

<!-- b001537 | prose | pages [7] -->
for Olympic debutants.

<!-- b001538 | prose | pages [7] -->
t=0

<!-- b001539 | prose | pages [7] -->
NT−t: Number of athletes in the (T −t)-th Olympic cycle.

<!-- b001540 | prose | pages [7] -->
nation-

<!-- b001541 | prose | pages [7] -->
Competitiveness

<!-- b001542 | prose | pages [7] -->
Captures

<!-- b001543 | prose | pages [7] -->
!

<!-- b001544 | furniture | pages [7] -->


<!-- b001545 | prose | pages [7] -->
specific strength across

<!-- b001546 | prose | pages [7] -->
Index (XComp)

<!-- b001547 | prose | pages [7] -->
3

<!-- b001548 | prose | pages [7] -->
K

<!-- b001549 | prose | pages [7] -->
X

<!-- b001550 | prose | pages [7] -->
X

<!-- b001551 | prose | pages [7] -->
mk

<!-- b001552 | prose | pages [7] -->
微信号：MATHmodels

<!-- b001553 | prose | pages [7] -->
sports, adjusted temporal decay.

<!-- b001554 | prose | pages [7] -->
for

<!-- b001555 | prose | pages [7] -->
pk,t · e−0.2t

<!-- b001556 | prose | pages [7] -->
·

<!-- b001557 | prose | pages [7] -->
XComp =

<!-- b001558 | prose | pages [7] -->
Mtotal

<!-- b001559 | prose | pages [7] -->
t=1

<!-- b001560 | prose | pages [7] -->
k=1

<!-- b001561 | prose | pages [7] -->
mk: Medals in sport k, pk,t: Medals at T −t, Mtotal: Total medals.

<!-- b001562 | prose | pages [7] -->
Weighted sum of past

<!-- b001563 | prose | pages [7] -->
Historical Mo-

<!-- b001564 | prose | pages [7] -->
3 X

<!-- b001565 | prose | pages [7] -->
higher

<!-- b001566 | prose | pages [7] -->
mentum (XHist)

<!-- b001567 | prose | pages [7] -->
medals, with

<!-- b001568 | prose | pages [7] -->
MT−t · e−0.2t

<!-- b001569 | prose | pages [7] -->
XHist =

<!-- b001570 | prose | pages [7] -->
recent weights for performances.

<!-- b001571 | prose | pages [7] -->
Correlation Analysis

<!-- b001572 | prose | pages [7] -->
t=1

<!-- b001573 | prose | pages [7] -->
MT−t: Total medals at T −t.

<!-- b001574 | prose | pages [7] -->
To explore the relationships between features and target variables, we calculate Pearson corre- lation coefficients.

<!-- b001575 | caption | pages [7] -->
Figure 2: Correlation Matrix(XComp, XAth, and XHist)

<!-- b001576 | prose | pages [7] -->
m

<!-- b001577 | prose | pages [7] -->
m

<!-- b001578 | prose | pages [7] -->
m

<!-- b001579 | prose | pages [7] -->
m

<!-- b001580 | prose | pages [7] -->
m

<!-- b001581 | prose | pages [7] -->
m

<!-- b001582 | prose | pages [7] -->
m

<!-- b001583 | prose | pages [7] -->
m

<!-- b001584 | prose | pages [7] -->
m

<!-- b001585 | prose | pages [7] -->
m

<!-- b001586 | prose | pages [7] -->
m

<!-- b001587 | prose | pages [7] -->
m

<!-- b001588 | prose | pages [7] -->
m

<!-- b001589 | prose | pages [7] -->
m

<!-- b001590 | prose | pages [7] -->
m

<!-- b001591 | prose | pages [7] -->
m

<!-- b001592 | prose | pages [7] -->
m

<!-- b001593 | prose | pages [7] -->
m

<!-- b001594 | prose | pages [7] -->
m

<!-- b001595 | prose | pages [7] -->
m

<!-- b001596 | prose | pages [7] -->
m

<!-- b001597 | prose | pages [7] -->
m

<!-- b001598 | prose | pages [7] -->
m

<!-- b001599 | prose | pages [7] -->
m

<!-- b001600 | prose | pages [7] -->
m

<!-- b001601 | prose | pages [7] -->
m

<!-- b001602 | prose | pages [7] -->
m

<!-- b001603 | prose | pages [7] -->
m

<!-- b001604 | prose | pages [7] -->
m

<!-- b001605 | prose | pages [7] -->
m

<!-- b001606 | prose | pages [7] -->
m

<!-- b001607 | prose | pages [7] -->
m

<!-- b001608 | prose | pages [7] -->
m

<!-- b001609 | prose | pages [7] -->
m

<!-- b001610 | prose | pages [7] -->
m

<!-- b001611 | prose | pages [7] -->
m

<!-- b001612 | prose | pages [7] -->
m

<!-- b001613 | prose | pages [7] -->
m

<!-- b001614 | prose | pages [7] -->
m

<!-- b001615 | prose | pages [7] -->
m

<!-- b001616 | prose | pages [7] -->
m

<!-- b001617 | prose | pages [7] -->
m

<!-- b001618 | prose | pages [7] -->
m

<!-- b001619 | prose | pages [7] -->
m

<!-- b001620 | prose | pages [7] -->
m

<!-- b001621 | prose | pages [7] -->
m

<!-- b001622 | prose | pages [7] -->
m

<!-- b001623 | prose | pages [7] -->
m

<!-- b001624 | prose | pages [7] -->
m

<!-- b001625 | prose | pages [7] -->
m

<!-- b001626 | prose | pages [7] -->
m

<!-- b001627 | prose | pages [7] -->
m

<!-- b001628 | prose | pages [7] -->
m

<!-- b001629 | prose | pages [7] -->
m

<!-- b001630 | prose | pages [7] -->
m

<!-- b001631 | prose | pages [7] -->
m

<!-- b001632 | prose | pages [7] -->
m

<!-- b001633 | prose | pages [7] -->
m

<!-- b001634 | prose | pages [7] -->
m

<!-- b001635 | prose | pages [7] -->
m

<!-- b001636 | prose | pages [7] -->
m

<!-- b001637 | prose | pages [7] -->
m

<!-- b001638 | prose | pages [7] -->
m

<!-- b001639 | prose | pages [7] -->
m

<!-- b001640 | prose | pages [7] -->
m

<!-- b001641 | prose | pages [7] -->
m

<!-- b001642 | prose | pages [7] -->
m

<!-- b001643 | prose | pages [7] -->
m

<!-- b001644 | prose | pages [7] -->
m

<!-- b001645 | prose | pages [7] -->
m

<!-- b001646 | prose | pages [7] -->
m

<!-- b001647 | prose | pages [7] -->
m

<!-- b001648 | prose | pages [7] -->
m

<!-- b001649 | prose | pages [7] -->
m

<!-- b001650 | prose | pages [7] -->
m

<!-- b001651 | prose | pages [7] -->
m

<!-- b001652 | prose | pages [7] -->
m

<!-- b001653 | prose | pages [7] -->
m

<!-- b001654 | prose | pages [7] -->
m

<!-- b001655 | prose | pages [7] -->
m

<!-- b001656 | prose | pages [7] -->
m

<!-- b001657 | prose | pages [7] -->
m

<!-- b001658 | prose | pages [7] -->
m

<!-- b001659 | prose | pages [7] -->
m

<!-- b001660 | prose | pages [7] -->
m

<!-- b001661 | prose | pages [7] -->
m

<!-- b001662 | prose | pages [7] -->
m

<!-- b001663 | prose | pages [7] -->
m

<!-- b001664 | prose | pages [7] -->
m

<!-- b001665 | prose | pages [7] -->
m

<!-- b001666 | prose | pages [7] -->
m

<!-- b001667 | prose | pages [7] -->
m

<!-- b001668 | prose | pages [7] -->
m

<!-- b001669 | prose | pages [7] -->
m

<!-- b001670 | prose | pages [7] -->
m

<!-- b001671 | prose | pages [7] -->
m

<!-- b001672 | prose | pages [7] -->
m

<!-- b001673 | prose | pages [7] -->
m

<!-- b001674 | prose | pages [7] -->
m

<!-- b001675 | prose | pages [7] -->
m

<!-- b001676 | prose | pages [7] -->
m

<!-- b001677 | prose | pages [7] -->
m

<!-- b001678 | prose | pages [7] -->
m

<!-- b001679 | prose | pages [7] -->
m

<!-- b001680 | prose | pages [7] -->
m

<!-- b001681 | prose | pages [7] -->
m

<!-- b001682 | prose | pages [7] -->
m

<!-- b001683 | prose | pages [7] -->
m

<!-- b001684 | prose | pages [7] -->
m

<!-- b001685 | prose | pages [7] -->
m

<!-- b001686 | prose | pages [7] -->
m

<!-- b001687 | prose | pages [7] -->
m

<!-- b001688 | prose | pages [7] -->
m

<!-- b001689 | prose | pages [7] -->
m

<!-- b001690 | prose | pages [7] -->
m

<!-- b001691 | prose | pages [7] -->
m

<!-- b001692 | prose | pages [7] -->
m

<!-- b001693 | prose | pages [7] -->
m

<!-- b001694 | prose | pages [7] -->
m

<!-- b001695 | prose | pages [7] -->
m

<!-- b001696 | prose | pages [7] -->
m

<!-- b001697 | prose | pages [7] -->
m

<!-- b001698 | prose | pages [7] -->
m

<!-- b001699 | prose | pages [7] -->
m

<!-- b001700 | prose | pages [7] -->
m

<!-- b001701 | prose | pages [7] -->
m

<!-- b001702 | prose | pages [7] -->
m

<!-- b001703 | prose | pages [7] -->
m

<!-- b001704 | prose | pages [7] -->
m

<!-- b001705 | prose | pages [7] -->
m

<!-- b001706 | prose | pages [7] -->
m

<!-- b001707 | prose | pages [7] -->
m

<!-- b001708 | prose | pages [7] -->
m

<!-- b001709 | prose | pages [7] -->
m

<!-- b001710 | prose | pages [7] -->
m

<!-- b001711 | prose | pages [7] -->
m

<!-- b001712 | prose | pages [7] -->
m

<!-- b001713 | prose | pages [7] -->
m

<!-- b001714 | prose | pages [7] -->
m

<!-- b001715 | prose | pages [7] -->
m

<!-- b001716 | prose | pages [7] -->
m

<!-- b001717 | prose | pages [7] -->
m

<!-- b001718 | prose | pages [7] -->
m

<!-- b001719 | prose | pages [7] -->
m

<!-- b001720 | prose | pages [7] -->
m

<!-- b001721 | prose | pages [7] -->
m

<!-- b001722 | prose | pages [7] -->
m

<!-- b001723 | prose | pages [7] -->
m

<!-- b001724 | prose | pages [7] -->
m

<!-- b001725 | prose | pages [7] -->
m

<!-- b001726 | prose | pages [7] -->
m

<!-- b001727 | prose | pages [7] -->
m

<!-- b001728 | prose | pages [7] -->
m

<!-- b001729 | prose | pages [7] -->
m

<!-- b001730 | prose | pages [7] -->
m

<!-- b001731 | prose | pages [7] -->
m

<!-- b001732 | prose | pages [7] -->
m

<!-- b001733 | prose | pages [7] -->
m

<!-- b001734 | prose | pages [7] -->
m

<!-- b001735 | prose | pages [7] -->
m

<!-- b001736 | prose | pages [7] -->
m

<!-- b001737 | prose | pages [7] -->
m

<!-- b001738 | prose | pages [7] -->
m

<!-- b001739 | prose | pages [7] -->
m

<!-- b001740 | prose | pages [7] -->
m

<!-- b001741 | prose | pages [7] -->
m

<!-- b001742 | prose | pages [7] -->
m

<!-- b001743 | prose | pages [7] -->
m

<!-- b001744 | prose | pages [7] -->
m

<!-- b001745 | prose | pages [7] -->
m

<!-- b001746 | prose | pages [7] -->
m

<!-- b001747 | prose | pages [7] -->
m

<!-- b001748 | prose | pages [7] -->
m

<!-- b001749 | prose | pages [7] -->
m

<!-- b001750 | prose | pages [7] -->
m

<!-- b001751 | prose | pages [7] -->
m

<!-- b001752 | prose | pages [7] -->
m

<!-- b001753 | prose | pages [7] -->
m

<!-- b001754 | prose | pages [7] -->
m

<!-- b001755 | prose | pages [7] -->
m

<!-- b001756 | prose | pages [7] -->
m

<!-- b001757 | prose | pages [7] -->
m

<!-- b001758 | prose | pages [7] -->
m

<!-- b001759 | prose | pages [7] -->
m

<!-- b001760 | prose | pages [7] -->
m

<!-- b001761 | prose | pages [7] -->
m

<!-- b001762 | prose | pages [7] -->
m

<!-- b001763 | prose | pages [7] -->
m

<!-- b001764 | prose | pages [7] -->
m

<!-- b001765 | prose | pages [7] -->
m

<!-- b001766 | prose | pages [7] -->
m

<!-- b001767 | prose | pages [7] -->
m

<!-- b001768 | prose | pages [7] -->
m

<!-- b001769 | prose | pages [7] -->
m

<!-- b001770 | prose | pages [7] -->
m

<!-- b001771 | prose | pages [7] -->
m

<!-- b001772 | prose | pages [7] -->
m

<!-- b001773 | prose | pages [7] -->
m

<!-- b001774 | prose | pages [7] -->
m

<!-- b001775 | prose | pages [7] -->
m

<!-- b001776 | prose | pages [7] -->
m

<!-- b001777 | prose | pages [7] -->
m

<!-- b001778 | prose | pages [7] -->
m

<!-- b001779 | prose | pages [7] -->
m

<!-- b001780 | prose | pages [7] -->
m

<!-- b001781 | prose | pages [7] -->
m

<!-- b001782 | prose | pages [7] -->
m

<!-- b001783 | prose | pages [7] -->
m

<!-- b001784 | prose | pages [7] -->
m

<!-- b001785 | prose | pages [7] -->
m

<!-- b001786 | prose | pages [7] -->
m

<!-- b001787 | prose | pages [7] -->
m

<!-- b001788 | prose | pages [7] -->
m

<!-- b001789 | prose | pages [7] -->
m

<!-- b001790 | prose | pages [7] -->
m

<!-- b001791 | prose | pages [7] -->
m

<!-- b001792 | prose | pages [7] -->
m

<!-- b001793 | prose | pages [7] -->
m

<!-- b001794 | prose | pages [7] -->
m

<!-- b001795 | prose | pages [7] -->
m

<!-- b001796 | prose | pages [7] -->
m

<!-- b001797 | prose | pages [7] -->
m

<!-- b001798 | prose | pages [7] -->
m

<!-- b001799 | prose | pages [7] -->
m

<!-- b001800 | prose | pages [7] -->
m

<!-- b001801 | prose | pages [7] -->
m

<!-- b001802 | prose | pages [7] -->
m

<!-- b001803 | prose | pages [7] -->
m

<!-- b001804 | prose | pages [7] -->
m

<!-- b001805 | prose | pages [7] -->
m

<!-- b001806 | prose | pages [7] -->
m

<!-- b001807 | prose | pages [7] -->
m

<!-- b001808 | prose | pages [7] -->
m

<!-- b001809 | prose | pages [7] -->
m

<!-- b001810 | prose | pages [7] -->
m

<!-- b001811 | prose | pages [7] -->
m

<!-- b001812 | prose | pages [7] -->
m

<!-- b001813 | prose | pages [7] -->
m

<!-- b001814 | prose | pages [7] -->
m

<!-- b001815 | prose | pages [7] -->
m

<!-- b001816 | prose | pages [7] -->
m

<!-- b001817 | prose | pages [7] -->
m

<!-- b001818 | prose | pages [7] -->
m

<!-- b001819 | prose | pages [7] -->
m

<!-- b001820 | prose | pages [7] -->
m

<!-- b001821 | prose | pages [7] -->
m

<!-- b001822 | prose | pages [7] -->
m

<!-- b001823 | prose | pages [7] -->
m

<!-- b001824 | prose | pages [7] -->
m

<!-- b001825 | prose | pages [7] -->
m

<!-- b001826 | prose | pages [7] -->
m

<!-- b001827 | prose | pages [7] -->
m

<!-- b001828 | prose | pages [7] -->
m

<!-- b001829 | prose | pages [7] -->
m

<!-- b001830 | prose | pages [7] -->
m

<!-- b001831 | prose | pages [7] -->
m

<!-- b001832 | prose | pages [7] -->
m

<!-- b001833 | prose | pages [7] -->
m

<!-- b001834 | prose | pages [7] -->
m

<!-- b001835 | prose | pages [7] -->
m

<!-- b001836 | prose | pages [7] -->
m

<!-- b001837 | prose | pages [7] -->
m

<!-- b001838 | prose | pages [7] -->
m

<!-- b001839 | prose | pages [7] -->
m

<!-- b001840 | prose | pages [7] -->
m

<!-- b001841 | prose | pages [7] -->
m

<!-- b001842 | prose | pages [7] -->
m

<!-- b001843 | prose | pages [7] -->
m

<!-- b001844 | prose | pages [7] -->
m

<!-- b001845 | prose | pages [7] -->
m

<!-- b001846 | prose | pages [7] -->
m

<!-- b001847 | prose | pages [7] -->
m

<!-- b001848 | prose | pages [7] -->
m

<!-- b001849 | prose | pages [7] -->
m

<!-- b001850 | prose | pages [7] -->
m

<!-- b001851 | prose | pages [7] -->
m

<!-- b001852 | prose | pages [7] -->
m

<!-- b001853 | prose | pages [7] -->
m

<!-- b001854 | prose | pages [7] -->
m

<!-- b001855 | prose | pages [7] -->
m

<!-- b001856 | prose | pages [7] -->
m

<!-- b001857 | prose | pages [7] -->
m

<!-- b001858 | prose | pages [7] -->
m

<!-- b001859 | prose | pages [7] -->
m

<!-- b001860 | furniture | pages [7] -->
m

<!-- b001861 | furniture | pages [7] -->
m

<!-- b001862 | furniture | pages [7] -->
m

<!-- b001863 | furniture | pages [7] -->
m

<!-- b001864 | furniture | pages [7] -->
m

<!-- b001865 | furniture | pages [7] -->
m

<!-- b001866 | furniture | pages [7] -->
m

<!-- b001867 | furniture | pages [7] -->
m

<!-- b001868 | furniture | pages [7] -->
m

<!-- b001869 | furniture | pages [7] -->
m

<!-- b001870 | furniture | pages [7] -->
m

<!-- b001871 | furniture | pages [7] -->
m

<!-- b001872 | furniture | pages [7] -->
m

<!-- b001873 | furniture | pages [7] -->
m

<!-- b001874 | furniture | pages [7] -->
m

<!-- b001875 | furniture | pages [7] -->
m

<!-- b001876 | furniture | pages [7] -->
m

<!-- b001877 | furniture | pages [7] -->
m

<!-- b001878 | furniture | pages [7] -->
m

<!-- b001879 | furniture | pages [7] -->
m

<!-- b001880 | furniture | pages [7] -->
m

<!-- b001881 | furniture | pages [7] -->
m

<!-- b001882 | furniture | pages [7] -->
m

<!-- b001883 | furniture | pages [7] -->
m

<!-- b001884 | furniture | pages [7] -->
m

<!-- b001885 | furniture | pages [7] -->
m

<!-- b001886 | furniture | pages [7] -->
m

<!-- b001887 | furniture | pages [7] -->
m

<!-- b001888 | furniture | pages [7] -->
m

<!-- b001889 | furniture | pages [7] -->
m

<!-- b001890 | furniture | pages [7] -->
m

<!-- b001891 | furniture | pages [7] -->
m

<!-- b001892 | furniture | pages [7] -->
m

<!-- b001893 | furniture | pages [7] -->
m

<!-- b001894 | furniture | pages [7] -->
m

<!-- b001895 | furniture | pages [7] -->
m

<!-- b001896 | furniture | pages [7] -->
m

<!-- b001897 | furniture | pages [7] -->
m

<!-- b001898 | furniture | pages [7] -->
m

<!-- b001899 | furniture | pages [7] -->
m

<!-- b001900 | furniture | pages [7] -->
m

<!-- b001901 | furniture | pages [7] -->
m

<!-- b001902 | furniture | pages [7] -->
m

<!-- b001903 | furniture | pages [7] -->
m

<!-- b001904 | furniture | pages [7] -->
m

<!-- b001905 | furniture | pages [7] -->
m

<!-- b001906 | furniture | pages [7] -->
m

<!-- b001907 | furniture | pages [7] -->
m

<!-- b001908 | furniture | pages [7] -->
m

<!-- b001909 | furniture | pages [7] -->
m

<!-- b001910 | furniture | pages [7] -->
m

<!-- b001911 | furniture | pages [7] -->
m

<!-- b001912 | furniture | pages [7] -->
m

<!-- b001913 | furniture | pages [7] -->
m

<!-- b001914 | furniture | pages [7] -->
m

<!-- b001915 | furniture | pages [7] -->
m

<!-- b001916 | furniture | pages [7] -->
m

<!-- b001917 | furniture | pages [7] -->
m

<!-- b001918 | furniture | pages [7] -->
m

<!-- b001919 | furniture | pages [7] -->
m

<!-- b001920 | furniture | pages [7] -->
m

<!-- b001921 | furniture | pages [7] -->
m

<!-- b001922 | furniture | pages [7] -->
m

<!-- b001923 | furniture | pages [7] -->
m

<!-- b001924 | furniture | pages [7] -->
m

<!-- b001925 | furniture | pages [7] -->
m

<!-- b001926 | furniture | pages [7] -->
m

<!-- b001927 | furniture | pages [7] -->
m

<!-- b001928 | furniture | pages [7] -->
m

<!-- b001929 | furniture | pages [7] -->
m

<!-- b001930 | furniture | pages [7] -->
m

<!-- b001931 | furniture | pages [7] -->
m

<!-- b001932 | furniture | pages [7] -->
m

<!-- b001933 | furniture | pages [7] -->
m

<!-- b001934 | furniture | pages [7] -->
m

<!-- b001935 | furniture | pages [7] -->
m

<!-- b001936 | furniture | pages [7] -->
m

<!-- b001937 | furniture | pages [7] -->
m

<!-- b001938 | furniture | pages [7] -->
m

<!-- b001939 | furniture | pages [7] -->
m

<!-- b001940 | furniture | pages [7] -->
m

<!-- b001941 | furniture | pages [7] -->
m

<!-- b001942 | furniture | pages [7] -->
m

<!-- b001943 | furniture | pages [7] -->
m

<!-- b001944 | furniture | pages [7] -->
m

<!-- b001945 | furniture | pages [7] -->
m

<!-- b001946 | furniture | pages [7] -->
m

<!-- b001947 | furniture | pages [7] -->
m

<!-- b001948 | furniture | pages [7] -->
m

<!-- b001949 | furniture | pages [7] -->
m

<!-- b001950 | furniture | pages [7] -->
m

<!-- b001951 | furniture | pages [7] -->
m

<!-- b001952 | furniture | pages [7] -->
m

<!-- b001953 | furniture | pages [7] -->
m

<!-- b001954 | furniture | pages [7] -->
m

<!-- b001955 | furniture | pages [7] -->
m

<!-- b001956 | furniture | pages [7] -->
m

<!-- b001957 | furniture | pages [7] -->
m

<!-- b001958 | furniture | pages [7] -->
m

<!-- b001959 | furniture | pages [7] -->
m

<!-- b001960 | furniture | pages [7] -->
m

<!-- b001961 | furniture | pages [7] -->
m

<!-- b001962 | furniture | pages [7] -->
m

<!-- b001963 | furniture | pages [7] -->
m

<!-- b001964 | furniture | pages [7] -->
m

<!-- b001965 | furniture | pages [7] -->
m

<!-- b001966 | furniture | pages [7] -->
m

<!-- b001967 | furniture | pages [7] -->
m

<!-- b001968 | furniture | pages [7] -->
m

<!-- b001969 | furniture | pages [7] -->
m

<!-- b001970 | furniture | pages [7] -->
m

<!-- b001971 | furniture | pages [7] -->
m

<!-- b001972 | furniture | pages [7] -->
m

<!-- b001973 | furniture | pages [7] -->
m

<!-- b001974 | furniture | pages [7] -->
m

<!-- b001975 | furniture | pages [7] -->
m

<!-- b001976 | furniture | pages [7] -->
m

<!-- b001977 | furniture | pages [7] -->
m

<!-- b001978 | furniture | pages [7] -->
m

<!-- b001979 | furniture | pages [7] -->
m

<!-- b001980 | furniture | pages [7] -->
m

<!-- b001981 | furniture | pages [7] -->
m

<!-- b001982 | furniture | pages [7] -->
m

<!-- b001983 | furniture | pages [7] -->
m

<!-- b001984 | furniture | pages [7] -->
m

<!-- b001985 | furniture | pages [7] -->
m

<!-- b001986 | furniture | pages [7] -->
m

<!-- b001987 | furniture | pages [7] -->
m

<!-- b001988 | furniture | pages [7] -->
m

<!-- b001989 | furniture | pages [7] -->
m

<!-- b001990 | furniture | pages [7] -->
m

<!-- b001991 | furniture | pages [7] -->
m

<!-- b001992 | furniture | pages [7] -->
m

<!-- b001993 | furniture | pages [7] -->
m

<!-- b001994 | furniture | pages [7] -->
m

<!-- b001995 | furniture | pages [7] -->
m

<!-- b001996 | furniture | pages [7] -->
m

<!-- b001997 | furniture | pages [7] -->
m

<!-- b001998 | furniture | pages [7] -->
m

<!-- b001999 | furniture | pages [7] -->
m

<!-- b002000 | furniture | pages [7] -->
m

<!-- b002001 | furniture | pages [7] -->
m

<!-- b002002 | furniture | pages [7] -->
m

<!-- b002003 | furniture | pages [7] -->
m

<!-- b002004 | furniture | pages [7] -->
m

<!-- b002005 | furniture | pages [7] -->
m

<!-- b002006 | furniture | pages [7] -->
m

<!-- b002007 | furniture | pages [7] -->
m

<!-- b002008 | furniture | pages [7] -->
m

<!-- b002009 | furniture | pages [7] -->
m

<!-- b002010 | furniture | pages [7] -->
m

<!-- b002011 | furniture | pages [7] -->
m

<!-- b002012 | furniture | pages [7] -->
m

<!-- b002013 | furniture | pages [7] -->
m

<!-- b002014 | furniture | pages [7] -->
m

<!-- b002015 | furniture | pages [7] -->
m

<!-- b002016 | furniture | pages [7] -->
m

<!-- b002017 | furniture | pages [7] -->
m

<!-- b002018 | furniture | pages [7] -->
m

<!-- b002019 | furniture | pages [7] -->
m

<!-- b002020 | furniture | pages [7] -->
m

<!-- b002021 | furniture | pages [7] -->
m

<!-- b002022 | furniture | pages [7] -->
m

<!-- b002023 | furniture | pages [7] -->
m

<!-- b002024 | furniture | pages [7] -->
m

<!-- b002025 | furniture | pages [7] -->
m

<!-- b002026 | furniture | pages [7] -->
m

<!-- b002027 | furniture | pages [7] -->
m

<!-- b002028 | furniture | pages [7] -->
m

<!-- b002029 | furniture | pages [7] -->
m

<!-- b002030 | furniture | pages [7] -->
m

<!-- b002031 | furniture | pages [7] -->
m

<!-- b002032 | furniture | pages [7] -->
m

<!-- b002033 | furniture | pages [7] -->
m

<!-- b002034 | furniture | pages [7] -->
m

<!-- b002035 | furniture | pages [7] -->
m

<!-- b002036 | furniture | pages [7] -->
m

<!-- b002037 | furniture | pages [7] -->
m

<!-- b002038 | furniture | pages [7] -->
m

<!-- b002039 | furniture | pages [7] -->
m

<!-- b002040 | furniture | pages [7] -->
m

<!-- b002041 | furniture | pages [7] -->
m

<!-- b002042 | furniture | pages [7] -->
m

<!-- b002043 | furniture | pages [7] -->
m

<!-- b002044 | furniture | pages [7] -->
m

<!-- b002045 | furniture | pages [7] -->
m

<!-- b002046 | furniture | pages [7] -->
m

<!-- b002047 | furniture | pages [7] -->
m

<!-- b002048 | furniture | pages [7] -->
m

<!-- b002049 | furniture | pages [7] -->
m

<!-- b002050 | furniture | pages [7] -->
m

<!-- b002051 | furniture | pages [7] -->
m

<!-- b002052 | furniture | pages [7] -->
m

<!-- b002053 | furniture | pages [7] -->
m

<!-- b002054 | furniture | pages [7] -->
m

<!-- b002055 | furniture | pages [7] -->
m

<!-- b002056 | furniture | pages [7] -->
m

<!-- b002057 | furniture | pages [7] -->
m

<!-- b002058 | furniture | pages [7] -->
m

<!-- b002059 | furniture | pages [7] -->
m

<!-- b002060 | furniture | pages [7] -->
m

<!-- b002061 | furniture | pages [7] -->
m

<!-- b002062 | furniture | pages [7] -->
m

<!-- b002063 | furniture | pages [7] -->
m

<!-- b002064 | furniture | pages [7] -->
m

<!-- b002065 | furniture | pages [7] -->
m

<!-- b002066 | furniture | pages [7] -->
m

<!-- b002067 | furniture | pages [7] -->
m

<!-- b002068 | furniture | pages [7] -->
m

<!-- b002069 | furniture | pages [7] -->
m

<!-- b002070 | furniture | pages [7] -->
m

<!-- b002071 | furniture | pages [7] -->
m

<!-- b002072 | furniture | pages [7] -->
m

<!-- b002073 | furniture | pages [7] -->
m

<!-- b002074 | furniture | pages [7] -->
m

<!-- b002075 | furniture | pages [7] -->
m

<!-- b002076 | furniture | pages [7] -->
m

<!-- b002077 | furniture | pages [7] -->
m

<!-- b002078 | furniture | pages [7] -->
m

<!-- b002079 | furniture | pages [7] -->
m

<!-- b002080 | furniture | pages [7] -->
m

<!-- b002081 | furniture | pages [7] -->
m

<!-- b002082 | furniture | pages [7] -->
m

<!-- b002083 | furniture | pages [7] -->
m

<!-- b002084 | furniture | pages [7] -->
m

<!-- b002085 | furniture | pages [7] -->
m

<!-- b002086 | furniture | pages [7] -->
m

<!-- b002087 | furniture | pages [7] -->
m

<!-- b002088 | furniture | pages [7] -->
m

<!-- b002089 | furniture | pages [7] -->
m

<!-- b002090 | furniture | pages [7] -->
m

<!-- b002091 | furniture | pages [7] -->
m

<!-- b002092 | furniture | pages [7] -->
m

<!-- b002093 | furniture | pages [7] -->
m

<!-- b002094 | furniture | pages [7] -->
m

<!-- b002095 | furniture | pages [7] -->
m

<!-- b002096 | furniture | pages [7] -->
m

<!-- b002097 | furniture | pages [7] -->
m

<!-- b002098 | furniture | pages [7] -->
m

<!-- b002099 | furniture | pages [7] -->
m

<!-- b002100 | furniture | pages [7] -->
m

<!-- b002101 | furniture | pages [7] -->
m

<!-- b002102 | furniture | pages [7] -->
m

<!-- b002103 | furniture | pages [7] -->
m

<!-- b002104 | furniture | pages [7] -->
m

<!-- b002105 | furniture | pages [7] -->
m

<!-- b002106 | furniture | pages [7] -->
m

<!-- b002107 | furniture | pages [7] -->
m

<!-- b002108 | furniture | pages [7] -->
m

<!-- b002109 | furniture | pages [7] -->
m

<!-- b002110 | furniture | pages [7] -->
m

<!-- b002111 | furniture | pages [7] -->
m

<!-- b002112 | furniture | pages [7] -->
m

<!-- b002113 | furniture | pages [7] -->
m

<!-- b002114 | furniture | pages [7] -->
m

<!-- b002115 | furniture | pages [7] -->
m

<!-- b002116 | furniture | pages [7] -->
m

<!-- b002117 | furniture | pages [7] -->
m

<!-- b002118 | furniture | pages [7] -->
m

<!-- b002119 | furniture | pages [7] -->
m

<!-- b002120 | furniture | pages [7] -->
m

<!-- b002121 | furniture | pages [7] -->
m

<!-- b002122 | furniture | pages [7] -->
m

<!-- b002123 | furniture | pages [7] -->
m

<!-- b002124 | furniture | pages [7] -->
m

<!-- b002125 | furniture | pages [7] -->
m

<!-- b002126 | furniture | pages [7] -->
m

<!-- b002127 | furniture | pages [7] -->
m

<!-- b002128 | furniture | pages [7] -->
m

<!-- b002129 | furniture | pages [7] -->
m

<!-- b002130 | furniture | pages [7] -->
m

<!-- b002131 | furniture | pages [7] -->
m

<!-- b002132 | furniture | pages [7] -->
m

<!-- b002133 | furniture | pages [7] -->
m

<!-- b002134 | furniture | pages [7] -->
m

<!-- b002135 | furniture | pages [7] -->
m

<!-- b002136 | furniture | pages [7] -->
m

<!-- b002137 | furniture | pages [7] -->
m

<!-- b002138 | furniture | pages [7] -->
m

<!-- b002139 | furniture | pages [7] -->
m

<!-- b002140 | furniture | pages [7] -->
m

<!-- b002141 | furniture | pages [7] -->
m

<!-- b002142 | furniture | pages [7] -->
m

<!-- b002143 | furniture | pages [7] -->
m

<!-- b002144 | furniture | pages [7] -->
m

<!-- b002145 | furniture | pages [7] -->
m

<!-- b002146 | furniture | pages [7] -->
m

<!-- b002147 | furniture | pages [7] -->
m

<!-- b002148 | furniture | pages [7] -->
m

<!-- b002149 | furniture | pages [7] -->
m

<!-- b002150 | furniture | pages [7] -->
m

<!-- b002151 | furniture | pages [7] -->
m

<!-- b002152 | furniture | pages [7] -->
m

<!-- b002153 | furniture | pages [7] -->
m

<!-- b002154 | furniture | pages [7] -->
m

<!-- b002155 | furniture | pages [7] -->
m

<!-- b002156 | furniture | pages [7] -->
m

<!-- b002157 | furniture | pages [7] -->
m

<!-- b002158 | furniture | pages [7] -->
m

<!-- b002159 | furniture | pages [7] -->
m

<!-- b002160 | furniture | pages [7] -->
m

<!-- b002161 | furniture | pages [7] -->
m

<!-- b002162 | furniture | pages [7] -->
m

<!-- b002163 | furniture | pages [7] -->
m

<!-- b002164 | furniture | pages [7] -->
m

<!-- b002165 | furniture | pages [7] -->
m

<!-- b002166 | furniture | pages [7] -->
m

<!-- b002167 | furniture | pages [7] -->
m

<!-- b002168 | furniture | pages [7] -->
m

<!-- b002169 | furniture | pages [7] -->
m

<!-- b002170 | furniture | pages [7] -->
m

<!-- b002171 | furniture | pages [7] -->
m

<!-- b002172 | furniture | pages [7] -->
m

<!-- b002173 | furniture | pages [7] -->
m

<!-- b002174 | furniture | pages [7] -->
m

<!-- b002175 | furniture | pages [7] -->
m

<!-- b002176 | furniture | pages [7] -->
m

<!-- b002177 | furniture | pages [7] -->
m

<!-- b002178 | furniture | pages [7] -->
m

<!-- b002179 | furniture | pages [7] -->
m

<!-- b002180 | furniture | pages [7] -->
m

<!-- b002181 | furniture | pages [7] -->
m

<!-- b002182 | furniture | pages [7] -->
m

<!-- b002183 | furniture | pages [7] -->
m

<!-- b002184 | furniture | pages [7] -->
m

<!-- b002185 | furniture | pages [7] -->
m

<!-- b002186 | furniture | pages [7] -->
m

<!-- b002187 | furniture | pages [7] -->
m

<!-- b002188 | furniture | pages [7] -->
m

<!-- b002189 | furniture | pages [7] -->
m

<!-- b002190 | furniture | pages [7] -->
m

<!-- b002191 | furniture | pages [7] -->
m

<!-- b002192 | furniture | pages [7] -->
m

<!-- b002193 | furniture | pages [7] -->
m

<!-- b002194 | furniture | pages [7] -->
m

<!-- b002195 | furniture | pages [7] -->
m

<!-- b002196 | furniture | pages [7] -->
m

<!-- b002197 | furniture | pages [7] -->
m

<!-- b002198 | furniture | pages [7] -->
m

<!-- b002199 | furniture | pages [7] -->
m

<!-- b002200 | furniture | pages [7] -->
m

<!-- b002201 | furniture | pages [7] -->
m

<!-- b002202 | furniture | pages [7] -->
m

<!-- b002203 | furniture | pages [7] -->
m

<!-- b002204 | furniture | pages [7] -->
m

<!-- b002205 | furniture | pages [7] -->
m

<!-- b002206 | furniture | pages [7] -->
m

<!-- b002207 | furniture | pages [7] -->
m

<!-- b002208 | furniture | pages [7] -->
m

<!-- b002209 | furniture | pages [7] -->
m

<!-- b002210 | furniture | pages [7] -->
m

<!-- b002211 | furniture | pages [7] -->
m

<!-- b002212 | furniture | pages [7] -->
m

<!-- b002213 | furniture | pages [7] -->
m

<!-- b002214 | furniture | pages [7] -->
m

<!-- b002215 | furniture | pages [7] -->
m

<!-- b002216 | furniture | pages [7] -->
m

<!-- b002217 | furniture | pages [7] -->
m

<!-- b002218 | furniture | pages [7] -->
m

<!-- b002219 | furniture | pages [7] -->
m

<!-- b002220 | furniture | pages [7] -->
m

<!-- b002221 | furniture | pages [7] -->
m

<!-- b002222 | furniture | pages [7] -->
m

<!-- b002223 | furniture | pages [7] -->
m

<!-- b002224 | furniture | pages [7] -->
m

<!-- b002225 | furniture | pages [7] -->
m

<!-- b002226 | furniture | pages [7] -->
m

<!-- b002227 | furniture | pages [7] -->
m

<!-- b002228 | furniture | pages [7] -->
m

<!-- b002229 | furniture | pages [7] -->
m

<!-- b002230 | furniture | pages [7] -->
m

<!-- b002231 | furniture | pages [7] -->
m

<!-- b002232 | furniture | pages [7] -->
m

<!-- b002233 | furniture | pages [7] -->
m

<!-- b002234 | furniture | pages [7] -->
m

<!-- b002235 | furniture | pages [7] -->
m

<!-- b002236 | furniture | pages [7] -->
m

<!-- b002237 | furniture | pages [7] -->
m

<!-- b002238 | furniture | pages [7] -->
m

<!-- b002239 | furniture | pages [7] -->
m

<!-- b002240 | furniture | pages [7] -->
m

<!-- b002241 | furniture | pages [7] -->
m

<!-- b002242 | furniture | pages [7] -->
m

<!-- b002243 | furniture | pages [7] -->
m

<!-- b002244 | furniture | pages [7] -->
m

<!-- b002245 | furniture | pages [7] -->
m

<!-- b002246 | furniture | pages [7] -->
m

<!-- b002247 | furniture | pages [7] -->
m

<!-- b002248 | furniture | pages [7] -->
m

<!-- b002249 | furniture | pages [7] -->
m

<!-- b002250 | furniture | pages [7] -->
m

<!-- b002251 | furniture | pages [7] -->
m

<!-- b002252 | furniture | pages [7] -->
m

<!-- b002253 | furniture | pages [7] -->
m

<!-- b002254 | furniture | pages [7] -->
m

<!-- b002255 | furniture | pages [7] -->
m

<!-- b002256 | furniture | pages [7] -->
m

<!-- b002257 | furniture | pages [7] -->
m

<!-- b002258 | furniture | pages [7] -->
m

<!-- b002259 | furniture | pages [7] -->
m

<!-- b002260 | furniture | pages [7] -->
m

<!-- b002261 | furniture | pages [7] -->
m

<!-- b002262 | furniture | pages [7] -->
m

<!-- b002263 | furniture | pages [8] -->
Team # 2503389

<!-- b002264 | furniture | pages [8] -->
Page 8 of 26

<!-- b002265 | prose | pages [8] -->
As shown in Figure 2, the award-winning rate exhibits significant correlations with the pre- dictive features XComp, XAth, and XHist, with correlation coefficients of 0.92, 0.86, and 1.00, respectively. These values highlight the strong relationships between competitiveness, athlete pool size, and historical momentum in predicting a nation’s award-winning performance.

<!-- b002266 | caption | pages [8] -->
Figure 3: Host Boost

<!-- b002267 | prose | pages [8] -->
Since the host boost is a discrete variable, while other features change continuously, the host boost shows weak linear correlation with the other three indicators. Therefore, it is necessary to analyze the host boost separately. As illustrated in Figure 3, the total medal count for a nation significantly increases during its host year, highlighting the “Host Boost” as a crucial feature.

<!-- b002268 | heading | pages [8] -->
Feedforward Neural Network-Model Construction

<!-- b002269 | prose | pages [8] -->
5.2.2

<!-- b002270 | prose | pages [8] -->
m

<!-- b002271 | prose | pages [8] -->
m

<!-- b002272 | prose | pages [8] -->
m

<!-- b002273 | prose | pages [8] -->
m

<!-- b002274 | prose | pages [8] -->
m

<!-- b002275 | prose | pages [8] -->
m

<!-- b002276 | prose | pages [8] -->
m

<!-- b002277 | prose | pages [8] -->
m

<!-- b002278 | prose | pages [8] -->
m

<!-- b002279 | prose | pages [8] -->
m

<!-- b002280 | prose | pages [8] -->
m

<!-- b002281 | prose | pages [8] -->
m

<!-- b002282 | prose | pages [8] -->
m

<!-- b002283 | prose | pages [8] -->
m

<!-- b002284 | prose | pages [8] -->
m

<!-- b002285 | prose | pages [8] -->
m

<!-- b002286 | prose | pages [8] -->
m

<!-- b002287 | prose | pages [8] -->
m

<!-- b002288 | prose | pages [8] -->
m

<!-- b002289 | prose | pages [8] -->
m

<!-- b002290 | prose | pages [8] -->
m

<!-- b002291 | prose | pages [8] -->
m

<!-- b002292 | prose | pages [8] -->
m

<!-- b002293 | prose | pages [8] -->
m

<!-- b002294 | prose | pages [8] -->
m

<!-- b002295 | prose | pages [8] -->
m

<!-- b002296 | prose | pages [8] -->
m

<!-- b002297 | prose | pages [8] -->
m

<!-- b002298 | prose | pages [8] -->
m

<!-- b002299 | prose | pages [8] -->
m

<!-- b002300 | prose | pages [8] -->
m

<!-- b002301 | prose | pages [8] -->
m

<!-- b002302 | prose | pages [8] -->
m

<!-- b002303 | prose | pages [8] -->
m

<!-- b002304 | prose | pages [8] -->
m

<!-- b002305 | prose | pages [8] -->
m

<!-- b002306 | prose | pages [8] -->
m

<!-- b002307 | prose | pages [8] -->
m

<!-- b002308 | prose | pages [8] -->
m

<!-- b002309 | prose | pages [8] -->
m

<!-- b002310 | prose | pages [8] -->
m

<!-- b002311 | prose | pages [8] -->
m

<!-- b002312 | prose | pages [8] -->
m

<!-- b002313 | prose | pages [8] -->
m

<!-- b002314 | prose | pages [8] -->
m

<!-- b002315 | prose | pages [8] -->
m

<!-- b002316 | prose | pages [8] -->
m

<!-- b002317 | prose | pages [8] -->
m

<!-- b002318 | prose | pages [8] -->
m

<!-- b002319 | prose | pages [8] -->
m

<!-- b002320 | prose | pages [8] -->
m

<!-- b002321 | prose | pages [8] -->
m

<!-- b002322 | prose | pages [8] -->
m

<!-- b002323 | prose | pages [8] -->
m

<!-- b002324 | prose | pages [8] -->
m

<!-- b002325 | prose | pages [8] -->
m

<!-- b002326 | prose | pages [8] -->
m

<!-- b002327 | prose | pages [8] -->
m

<!-- b002328 | prose | pages [8] -->
m

<!-- b002329 | prose | pages [8] -->
m

<!-- b002330 | prose | pages [8] -->
m

<!-- b002331 | prose | pages [8] -->
m

<!-- b002332 | prose | pages [8] -->
m

<!-- b002333 | prose | pages [8] -->
m

<!-- b002334 | prose | pages [8] -->
m

<!-- b002335 | prose | pages [8] -->
m

<!-- b002336 | prose | pages [8] -->
m

<!-- b002337 | prose | pages [8] -->
m

<!-- b002338 | prose | pages [8] -->
m

<!-- b002339 | prose | pages [8] -->
m

<!-- b002340 | prose | pages [8] -->
m

<!-- b002341 | prose | pages [8] -->
m

<!-- b002342 | prose | pages [8] -->
m

<!-- b002343 | prose | pages [8] -->
m

<!-- b002344 | prose | pages [8] -->
m

<!-- b002345 | prose | pages [8] -->
m

<!-- b002346 | prose | pages [8] -->
m

<!-- b002347 | prose | pages [8] -->
m

<!-- b002348 | prose | pages [8] -->
m

<!-- b002349 | prose | pages [8] -->
m

<!-- b002350 | prose | pages [8] -->
m

<!-- b002351 | prose | pages [8] -->
m

<!-- b002352 | prose | pages [8] -->
m

<!-- b002353 | prose | pages [8] -->
m

<!-- b002354 | prose | pages [8] -->
m

<!-- b002355 | prose | pages [8] -->
m

<!-- b002356 | prose | pages [8] -->
m

<!-- b002357 | prose | pages [8] -->
m

<!-- b002358 | prose | pages [8] -->
m

<!-- b002359 | prose | pages [8] -->
m

<!-- b002360 | prose | pages [8] -->
m

<!-- b002361 | prose | pages [8] -->
m

<!-- b002362 | prose | pages [8] -->
m

<!-- b002363 | prose | pages [8] -->
m

<!-- b002364 | prose | pages [8] -->
m

<!-- b002365 | prose | pages [8] -->
m

<!-- b002366 | prose | pages [8] -->
m

<!-- b002367 | prose | pages [8] -->
m

<!-- b002368 | prose | pages [8] -->
m

<!-- b002369 | prose | pages [8] -->
m

<!-- b002370 | prose | pages [8] -->
m

<!-- b002371 | prose | pages [8] -->
m

<!-- b002372 | prose | pages [8] -->
m

<!-- b002373 | prose | pages [8] -->
m

<!-- b002374 | prose | pages [8] -->
m

<!-- b002375 | prose | pages [8] -->
m

<!-- b002376 | prose | pages [8] -->
m

<!-- b002377 | prose | pages [8] -->
m

<!-- b002378 | prose | pages [8] -->
m

<!-- b002379 | prose | pages [8] -->
m

<!-- b002380 | prose | pages [8] -->
m

<!-- b002381 | prose | pages [8] -->
m

<!-- b002382 | prose | pages [8] -->
m

<!-- b002383 | prose | pages [8] -->
m

<!-- b002384 | prose | pages [8] -->
m

<!-- b002385 | prose | pages [8] -->
m

<!-- b002386 | prose | pages [8] -->
m

<!-- b002387 | prose | pages [8] -->
m

<!-- b002388 | prose | pages [8] -->
m

<!-- b002389 | prose | pages [8] -->
m

<!-- b002390 | prose | pages [8] -->
m

<!-- b002391 | prose | pages [8] -->
m

<!-- b002392 | prose | pages [8] -->
m

<!-- b002393 | prose | pages [8] -->
m

<!-- b002394 | prose | pages [8] -->
m

<!-- b002395 | prose | pages [8] -->
m

<!-- b002396 | prose | pages [8] -->
m

<!-- b002397 | prose | pages [8] -->
m

<!-- b002398 | prose | pages [8] -->
m

<!-- b002399 | prose | pages [8] -->
m

<!-- b002400 | prose | pages [8] -->
m

<!-- b002401 | prose | pages [8] -->
m

<!-- b002402 | prose | pages [8] -->
m

<!-- b002403 | prose | pages [8] -->
m

<!-- b002404 | prose | pages [8] -->
m

<!-- b002405 | prose | pages [8] -->
m

<!-- b002406 | prose | pages [8] -->
m

<!-- b002407 | prose | pages [8] -->
m

<!-- b002408 | prose | pages [8] -->
m

<!-- b002409 | prose | pages [8] -->
m

<!-- b002410 | prose | pages [8] -->
m

<!-- b002411 | prose | pages [8] -->
m

<!-- b002412 | prose | pages [8] -->
m

<!-- b002413 | prose | pages [8] -->
m

<!-- b002414 | prose | pages [8] -->
m

<!-- b002415 | prose | pages [8] -->
m

<!-- b002416 | prose | pages [8] -->
m

<!-- b002417 | prose | pages [8] -->
m

<!-- b002418 | prose | pages [8] -->
m

<!-- b002419 | prose | pages [8] -->
m

<!-- b002420 | prose | pages [8] -->
m

<!-- b002421 | prose | pages [8] -->
m

<!-- b002422 | prose | pages [8] -->
m

<!-- b002423 | prose | pages [8] -->
m

<!-- b002424 | prose | pages [8] -->
m

<!-- b002425 | prose | pages [8] -->
m

<!-- b002426 | prose | pages [8] -->
m

<!-- b002427 | prose | pages [8] -->
m

<!-- b002428 | prose | pages [8] -->
m

<!-- b002429 | prose | pages [8] -->
m

<!-- b002430 | prose | pages [8] -->
m

<!-- b002431 | prose | pages [8] -->
m

<!-- b002432 | prose | pages [8] -->
m

<!-- b002433 | prose | pages [8] -->
m

<!-- b002434 | prose | pages [8] -->
m

<!-- b002435 | prose | pages [8] -->
m

<!-- b002436 | prose | pages [8] -->
m

<!-- b002437 | prose | pages [8] -->
m

<!-- b002438 | prose | pages [8] -->
m

<!-- b002439 | prose | pages [8] -->
m

<!-- b002440 | prose | pages [8] -->
m

<!-- b002441 | prose | pages [8] -->
m

<!-- b002442 | prose | pages [8] -->
m

<!-- b002443 | prose | pages [8] -->
m

<!-- b002444 | prose | pages [8] -->
m

<!-- b002445 | prose | pages [8] -->
m

<!-- b002446 | prose | pages [8] -->
m

<!-- b002447 | prose | pages [8] -->
m

<!-- b002448 | prose | pages [8] -->
m

<!-- b002449 | prose | pages [8] -->
m

<!-- b002450 | prose | pages [8] -->
m

<!-- b002451 | prose | pages [8] -->
m

<!-- b002452 | prose | pages [8] -->
m

<!-- b002453 | prose | pages [8] -->
m

<!-- b002454 | prose | pages [8] -->
m

<!-- b002455 | prose | pages [8] -->
m

<!-- b002456 | prose | pages [8] -->
m

<!-- b002457 | prose | pages [8] -->
m

<!-- b002458 | prose | pages [8] -->
m

<!-- b002459 | prose | pages [8] -->
m

<!-- b002460 | prose | pages [8] -->
m

<!-- b002461 | prose | pages [8] -->
m

<!-- b002462 | prose | pages [8] -->
m

<!-- b002463 | prose | pages [8] -->
m

<!-- b002464 | prose | pages [8] -->
m

<!-- b002465 | prose | pages [8] -->
m

<!-- b002466 | prose | pages [8] -->
m

<!-- b002467 | prose | pages [8] -->
m

<!-- b002468 | prose | pages [8] -->
m

<!-- b002469 | prose | pages [8] -->
m

<!-- b002470 | prose | pages [8] -->
m

<!-- b002471 | prose | pages [8] -->
m

<!-- b002472 | prose | pages [8] -->
m

<!-- b002473 | prose | pages [8] -->
m

<!-- b002474 | prose | pages [8] -->
m

<!-- b002475 | prose | pages [8] -->
m

<!-- b002476 | prose | pages [8] -->
m

<!-- b002477 | prose | pages [8] -->
m

<!-- b002478 | prose | pages [8] -->
m

<!-- b002479 | prose | pages [8] -->
m

<!-- b002480 | prose | pages [8] -->
m

<!-- b002481 | prose | pages [8] -->
m

<!-- b002482 | prose | pages [8] -->
m

<!-- b002483 | prose | pages [8] -->
m

<!-- b002484 | prose | pages [8] -->
m

<!-- b002485 | prose | pages [8] -->
m

<!-- b002486 | prose | pages [8] -->
m

<!-- b002487 | prose | pages [8] -->
m

<!-- b002488 | prose | pages [8] -->
m

<!-- b002489 | prose | pages [8] -->
m

<!-- b002490 | prose | pages [8] -->
m

<!-- b002491 | prose | pages [8] -->
m

<!-- b002492 | prose | pages [8] -->
m

<!-- b002493 | prose | pages [8] -->
m

<!-- b002494 | prose | pages [8] -->
m

<!-- b002495 | prose | pages [8] -->
m

<!-- b002496 | prose | pages [8] -->
m

<!-- b002497 | prose | pages [8] -->
m

<!-- b002498 | prose | pages [8] -->
m

<!-- b002499 | prose | pages [8] -->
m

<!-- b002500 | prose | pages [8] -->
m

<!-- b002501 | prose | pages [8] -->
m

<!-- b002502 | prose | pages [8] -->
m

<!-- b002503 | prose | pages [8] -->
m

<!-- b002504 | prose | pages [8] -->
m

<!-- b002505 | prose | pages [8] -->
m

<!-- b002506 | prose | pages [8] -->
m

<!-- b002507 | prose | pages [8] -->
m

<!-- b002508 | prose | pages [8] -->
m

<!-- b002509 | prose | pages [8] -->
m

<!-- b002510 | prose | pages [8] -->
m

<!-- b002511 | prose | pages [8] -->
m

<!-- b002512 | prose | pages [8] -->
m

<!-- b002513 | prose | pages [8] -->
m

<!-- b002514 | prose | pages [8] -->
m

<!-- b002515 | prose | pages [8] -->
m

<!-- b002516 | prose | pages [8] -->
m

<!-- b002517 | prose | pages [8] -->
m

<!-- b002518 | prose | pages [8] -->
m

<!-- b002519 | prose | pages [8] -->
m

<!-- b002520 | prose | pages [8] -->
m

<!-- b002521 | prose | pages [8] -->
m

<!-- b002522 | prose | pages [8] -->
m

<!-- b002523 | prose | pages [8] -->
m

<!-- b002524 | prose | pages [8] -->
m

<!-- b002525 | prose | pages [8] -->
m

<!-- b002526 | prose | pages [8] -->
m

<!-- b002527 | prose | pages [8] -->
m

<!-- b002528 | prose | pages [8] -->
m

<!-- b002529 | prose | pages [8] -->
m

<!-- b002530 | prose | pages [8] -->
m

<!-- b002531 | prose | pages [8] -->
m

<!-- b002532 | prose | pages [8] -->
m

<!-- b002533 | prose | pages [8] -->
m

<!-- b002534 | prose | pages [8] -->
m

<!-- b002535 | prose | pages [8] -->
m

<!-- b002536 | prose | pages [8] -->
m

<!-- b002537 | prose | pages [8] -->
m

<!-- b002538 | prose | pages [8] -->
m

<!-- b002539 | prose | pages [8] -->
m

<!-- b002540 | prose | pages [8] -->
m

<!-- b002541 | prose | pages [8] -->
m

<!-- b002542 | prose | pages [8] -->
m

<!-- b002543 | prose | pages [8] -->
m

<!-- b002544 | prose | pages [8] -->
m

<!-- b002545 | prose | pages [8] -->
m

<!-- b002546 | prose | pages [8] -->
m

<!-- b002547 | prose | pages [8] -->
m

<!-- b002548 | prose | pages [8] -->
m

<!-- b002549 | prose | pages [8] -->
m

<!-- b002550 | prose | pages [8] -->
m

<!-- b002551 | prose | pages [8] -->
m

<!-- b002552 | prose | pages [8] -->
m

<!-- b002553 | prose | pages [8] -->
m

<!-- b002554 | prose | pages [8] -->
m

<!-- b002555 | prose | pages [8] -->
m

<!-- b002556 | prose | pages [8] -->
m

<!-- b002557 | prose | pages [8] -->
m

<!-- b002558 | prose | pages [8] -->
m

<!-- b002559 | prose | pages [8] -->
m

<!-- b002560 | prose | pages [8] -->
m

<!-- b002561 | prose | pages [8] -->
m

<!-- b002562 | prose | pages [8] -->
m

<!-- b002563 | prose | pages [8] -->
m

<!-- b002564 | prose | pages [8] -->
m

<!-- b002565 | prose | pages [8] -->
m

<!-- b002566 | prose | pages [8] -->
m

<!-- b002567 | prose | pages [8] -->
m

<!-- b002568 | prose | pages [8] -->
m

<!-- b002569 | prose | pages [8] -->
m

<!-- b002570 | prose | pages [8] -->
m

<!-- b002571 | prose | pages [8] -->
m

<!-- b002572 | prose | pages [8] -->
m

<!-- b002573 | prose | pages [8] -->
m

<!-- b002574 | prose | pages [8] -->
m

<!-- b002575 | prose | pages [8] -->
m

<!-- b002576 | prose | pages [8] -->
m

<!-- b002577 | prose | pages [8] -->
m

<!-- b002578 | prose | pages [8] -->
m

<!-- b002579 | prose | pages [8] -->
m

<!-- b002580 | prose | pages [8] -->
m

<!-- b002581 | prose | pages [8] -->
m

<!-- b002582 | prose | pages [8] -->
m

<!-- b002583 | prose | pages [8] -->
m

<!-- b002584 | prose | pages [8] -->
m

<!-- b002585 | prose | pages [8] -->
m

<!-- b002586 | prose | pages [8] -->
m

<!-- b002587 | prose | pages [8] -->
m

<!-- b002588 | prose | pages [8] -->
m

<!-- b002589 | prose | pages [8] -->
m

<!-- b002590 | prose | pages [8] -->
m

<!-- b002591 | prose | pages [8] -->
m

<!-- b002592 | prose | pages [8] -->
m

<!-- b002593 | prose | pages [8] -->
m

<!-- b002594 | prose | pages [8] -->
m

<!-- b002595 | prose | pages [8] -->
m

<!-- b002596 | prose | pages [8] -->
m

<!-- b002597 | prose | pages [8] -->
m

<!-- b002598 | prose | pages [8] -->
m

<!-- b002599 | prose | pages [8] -->
m

<!-- b002600 | prose | pages [8] -->
m

<!-- b002601 | prose | pages [8] -->
m

<!-- b002602 | prose | pages [8] -->
m

<!-- b002603 | prose | pages [8] -->
m

<!-- b002604 | prose | pages [8] -->
m

<!-- b002605 | prose | pages [8] -->
m

<!-- b002606 | prose | pages [8] -->
m

<!-- b002607 | prose | pages [8] -->
m

<!-- b002608 | prose | pages [8] -->
m

<!-- b002609 | prose | pages [8] -->
m

<!-- b002610 | prose | pages [8] -->
m

<!-- b002611 | prose | pages [8] -->
m

<!-- b002612 | prose | pages [8] -->
m

<!-- b002613 | prose | pages [8] -->
m

<!-- b002614 | prose | pages [8] -->
m

<!-- b002615 | prose | pages [8] -->
m

<!-- b002616 | prose | pages [8] -->
m

<!-- b002617 | prose | pages [8] -->
m

<!-- b002618 | prose | pages [8] -->
m

<!-- b002619 | prose | pages [8] -->
m

<!-- b002620 | prose | pages [8] -->
m

<!-- b002621 | prose | pages [8] -->
m

<!-- b002622 | prose | pages [8] -->
m

<!-- b002623 | prose | pages [8] -->
m

<!-- b002624 | prose | pages [8] -->
m

<!-- b002625 | prose | pages [8] -->
m

<!-- b002626 | prose | pages [8] -->
m

<!-- b002627 | prose | pages [8] -->
m

<!-- b002628 | prose | pages [8] -->
m

<!-- b002629 | prose | pages [8] -->
m

<!-- b002630 | prose | pages [8] -->
m

<!-- b002631 | prose | pages [8] -->
m

<!-- b002632 | prose | pages [8] -->
m

<!-- b002633 | prose | pages [8] -->
m

<!-- b002634 | prose | pages [8] -->
m

<!-- b002635 | prose | pages [8] -->
m

<!-- b002636 | prose | pages [8] -->
m

<!-- b002637 | prose | pages [8] -->
m

<!-- b002638 | prose | pages [8] -->
m

<!-- b002639 | prose | pages [8] -->
m

<!-- b002640 | prose | pages [8] -->
m

<!-- b002641 | prose | pages [8] -->
m

<!-- b002642 | prose | pages [8] -->
m

<!-- b002643 | prose | pages [8] -->
m

<!-- b002644 | prose | pages [8] -->
m

<!-- b002645 | prose | pages [8] -->
m

<!-- b002646 | prose | pages [8] -->
m

<!-- b002647 | prose | pages [8] -->
m

<!-- b002648 | prose | pages [8] -->
m

<!-- b002649 | prose | pages [8] -->
m

<!-- b002650 | prose | pages [8] -->
m

<!-- b002651 | prose | pages [8] -->
m

<!-- b002652 | prose | pages [8] -->
m

<!-- b002653 | prose | pages [8] -->
m

<!-- b002654 | prose | pages [8] -->
m

<!-- b002655 | prose | pages [8] -->
m

<!-- b002656 | prose | pages [8] -->
m

<!-- b002657 | prose | pages [8] -->
m

<!-- b002658 | prose | pages [8] -->
m

<!-- b002659 | prose | pages [8] -->
m

<!-- b002660 | prose | pages [8] -->
m

<!-- b002661 | prose | pages [8] -->
m

<!-- b002662 | prose | pages [8] -->
m

<!-- b002663 | prose | pages [8] -->
m

<!-- b002664 | prose | pages [8] -->
m

<!-- b002665 | prose | pages [8] -->
m

<!-- b002666 | prose | pages [8] -->
m

<!-- b002667 | prose | pages [8] -->
m

<!-- b002668 | prose | pages [8] -->
m

<!-- b002669 | prose | pages [8] -->
m

<!-- b002670 | prose | pages [8] -->
m

<!-- b002671 | prose | pages [8] -->
m

<!-- b002672 | prose | pages [8] -->
m

<!-- b002673 | prose | pages [8] -->
m

<!-- b002674 | prose | pages [8] -->
m

<!-- b002675 | prose | pages [8] -->
m

<!-- b002676 | prose | pages [8] -->
m

<!-- b002677 | prose | pages [8] -->
m

<!-- b002678 | prose | pages [8] -->
m

<!-- b002679 | prose | pages [8] -->
m

<!-- b002680 | prose | pages [8] -->
m

<!-- b002681 | prose | pages [8] -->
m

<!-- b002682 | prose | pages [8] -->
m

<!-- b002683 | prose | pages [8] -->
m

<!-- b002684 | prose | pages [8] -->
m

<!-- b002685 | prose | pages [8] -->
m

<!-- b002686 | prose | pages [8] -->
m

<!-- b002687 | prose | pages [8] -->
m

<!-- b002688 | prose | pages [8] -->
m

<!-- b002689 | prose | pages [8] -->
m

<!-- b002690 | prose | pages [8] -->
m

<!-- b002691 | prose | pages [8] -->
m

<!-- b002692 | prose | pages [8] -->
m

<!-- b002693 | prose | pages [8] -->
m

<!-- b002694 | prose | pages [8] -->
m

<!-- b002695 | prose | pages [8] -->
m

<!-- b002696 | prose | pages [8] -->
m

<!-- b002697 | prose | pages [8] -->
m

<!-- b002698 | prose | pages [8] -->
m

<!-- b002699 | prose | pages [8] -->
m

<!-- b002700 | prose | pages [8] -->
m

<!-- b002701 | prose | pages [8] -->
m

<!-- b002702 | prose | pages [8] -->
m

<!-- b002703 | prose | pages [8] -->
m

<!-- b002704 | prose | pages [8] -->
m

<!-- b002705 | prose | pages [8] -->
m

<!-- b002706 | prose | pages [8] -->
m

<!-- b002707 | prose | pages [8] -->
m

<!-- b002708 | prose | pages [8] -->
m

<!-- b002709 | prose | pages [8] -->
m

<!-- b002710 | prose | pages [8] -->
m

<!-- b002711 | prose | pages [8] -->
m

<!-- b002712 | prose | pages [8] -->
m

<!-- b002713 | prose | pages [8] -->
m

<!-- b002714 | prose | pages [8] -->
m

<!-- b002715 | prose | pages [8] -->
m

<!-- b002716 | prose | pages [8] -->
m

<!-- b002717 | prose | pages [8] -->
m

<!-- b002718 | prose | pages [8] -->
m

<!-- b002719 | prose | pages [8] -->
m

<!-- b002720 | prose | pages [8] -->
m

<!-- b002721 | prose | pages [8] -->
m

<!-- b002722 | prose | pages [8] -->
m

<!-- b002723 | prose | pages [8] -->
m

<!-- b002724 | prose | pages [8] -->
m

<!-- b002725 | prose | pages [8] -->
m

<!-- b002726 | prose | pages [8] -->
m

<!-- b002727 | prose | pages [8] -->
m

<!-- b002728 | prose | pages [8] -->
m

<!-- b002729 | prose | pages [8] -->
m

<!-- b002730 | prose | pages [8] -->
m

<!-- b002731 | prose | pages [8] -->
m

<!-- b002732 | prose | pages [8] -->
m

<!-- b002733 | prose | pages [8] -->
m

<!-- b002734 | prose | pages [8] -->
m

<!-- b002735 | prose | pages [8] -->
m

<!-- b002736 | prose | pages [8] -->
m

<!-- b002737 | prose | pages [8] -->
m

<!-- b002738 | prose | pages [8] -->
m

<!-- b002739 | prose | pages [8] -->
m

<!-- b002740 | prose | pages [8] -->
m

<!-- b002741 | prose | pages [8] -->
m

<!-- b002742 | prose | pages [8] -->
m

<!-- b002743 | prose | pages [8] -->
m

<!-- b002744 | prose | pages [8] -->
m

<!-- b002745 | prose | pages [8] -->
m

<!-- b002746 | prose | pages [8] -->
m

<!-- b002747 | prose | pages [8] -->
m

<!-- b002748 | prose | pages [8] -->
m

<!-- b002749 | prose | pages [8] -->
m

<!-- b002750 | prose | pages [8] -->
m

<!-- b002751 | prose | pages [8] -->
m

<!-- b002752 | prose | pages [8] -->
m

<!-- b002753 | prose | pages [8] -->
m

<!-- b002754 | prose | pages [8] -->
m

<!-- b002755 | prose | pages [8] -->
m

<!-- b002756 | prose | pages [8] -->
m

<!-- b002757 | prose | pages [8] -->
m

<!-- b002758 | prose | pages [8] -->
m

<!-- b002759 | prose | pages [8] -->
m

<!-- b002760 | prose | pages [8] -->
m

<!-- b002761 | prose | pages [8] -->
m

<!-- b002762 | prose | pages [8] -->
m

<!-- b002763 | prose | pages [8] -->
m

<!-- b002764 | prose | pages [8] -->
m

<!-- b002765 | prose | pages [8] -->
m

<!-- b002766 | prose | pages [8] -->
m

<!-- b002767 | prose | pages [8] -->
m

<!-- b002768 | prose | pages [8] -->
m

<!-- b002769 | prose | pages [8] -->
m

<!-- b002770 | prose | pages [8] -->
m

<!-- b002771 | prose | pages [8] -->
m

<!-- b002772 | prose | pages [8] -->
m

<!-- b002773 | prose | pages [8] -->
m

<!-- b002774 | prose | pages [8] -->
m

<!-- b002775 | prose | pages [8] -->
m

<!-- b002776 | prose | pages [8] -->
m

<!-- b002777 | prose | pages [8] -->
m

<!-- b002778 | prose | pages [8] -->
m

<!-- b002779 | prose | pages [8] -->
m

<!-- b002780 | prose | pages [8] -->
m

<!-- b002781 | prose | pages [8] -->
m

<!-- b002782 | prose | pages [8] -->
m

<!-- b002783 | prose | pages [8] -->
m

<!-- b002784 | prose | pages [8] -->
m

<!-- b002785 | prose | pages [8] -->
m

<!-- b002786 | prose | pages [8] -->
m

<!-- b002787 | prose | pages [8] -->
m

<!-- b002788 | prose | pages [8] -->
m

<!-- b002789 | prose | pages [8] -->
m

<!-- b002790 | prose | pages [8] -->
m

<!-- b002791 | prose | pages [8] -->
m

<!-- b002792 | prose | pages [8] -->
m

<!-- b002793 | prose | pages [8] -->
m

<!-- b002794 | prose | pages [8] -->
m

<!-- b002795 | prose | pages [8] -->
m

<!-- b002796 | prose | pages [8] -->
m

<!-- b002797 | prose | pages [8] -->
m

<!-- b002798 | prose | pages [8] -->
m

<!-- b002799 | prose | pages [8] -->
m

<!-- b002800 | prose | pages [8] -->
m

<!-- b002801 | prose | pages [8] -->
m

<!-- b002802 | prose | pages [8] -->
m

<!-- b002803 | prose | pages [8] -->
m

<!-- b002804 | prose | pages [8] -->
m

<!-- b002805 | prose | pages [8] -->
m

<!-- b002806 | prose | pages [8] -->
m

<!-- b002807 | prose | pages [8] -->
m

<!-- b002808 | prose | pages [8] -->
m

<!-- b002809 | prose | pages [8] -->
m

<!-- b002810 | prose | pages [8] -->
m

<!-- b002811 | prose | pages [8] -->
m

<!-- b002812 | prose | pages [8] -->
m

<!-- b002813 | prose | pages [8] -->
m

<!-- b002814 | prose | pages [8] -->
m

<!-- b002815 | prose | pages [8] -->
m

<!-- b002816 | prose | pages [8] -->
m

<!-- b002817 | prose | pages [8] -->
m

<!-- b002818 | prose | pages [8] -->
m

<!-- b002819 | prose | pages [8] -->
m

<!-- b002820 | prose | pages [8] -->
m

<!-- b002821 | prose | pages [8] -->
m

<!-- b002822 | prose | pages [8] -->
m

<!-- b002823 | prose | pages [8] -->
m

<!-- b002824 | prose | pages [8] -->
m

<!-- b002825 | prose | pages [8] -->
m

<!-- b002826 | prose | pages [8] -->
m

<!-- b002827 | prose | pages [8] -->
m

<!-- b002828 | prose | pages [8] -->
m

<!-- b002829 | prose | pages [8] -->
m

<!-- b002830 | prose | pages [8] -->
m

<!-- b002831 | prose | pages [8] -->
m

<!-- b002832 | prose | pages [8] -->
m

<!-- b002833 | prose | pages [8] -->
m

<!-- b002834 | prose | pages [8] -->
m

<!-- b002835 | prose | pages [8] -->
m

<!-- b002836 | prose | pages [8] -->
m

<!-- b002837 | prose | pages [8] -->
m

<!-- b002838 | prose | pages [8] -->
m

<!-- b002839 | prose | pages [8] -->
m

<!-- b002840 | prose | pages [8] -->
m

<!-- b002841 | prose | pages [8] -->
m

<!-- b002842 | prose | pages [8] -->
m

<!-- b002843 | prose | pages [8] -->
m

<!-- b002844 | prose | pages [8] -->
m

<!-- b002845 | prose | pages [8] -->
m

<!-- b002846 | prose | pages [8] -->
m

<!-- b002847 | prose | pages [8] -->
m

<!-- b002848 | prose | pages [8] -->
m

<!-- b002849 | prose | pages [8] -->
m

<!-- b002850 | prose | pages [8] -->
m

<!-- b002851 | prose | pages [8] -->
m

<!-- b002852 | prose | pages [8] -->
m

<!-- b002853 | prose | pages [8] -->
m

<!-- b002854 | prose | pages [8] -->
m

<!-- b002855 | prose | pages [8] -->
m

<!-- b002856 | prose | pages [8] -->
m

<!-- b002857 | prose | pages [8] -->
m

<!-- b002858 | prose | pages [8] -->
m

<!-- b002859 | prose | pages [8] -->
m

<!-- b002860 | prose | pages [8] -->
m

<!-- b002861 | prose | pages [8] -->
m

<!-- b002862 | prose | pages [8] -->
m

<!-- b002863 | prose | pages [8] -->
m

<!-- b002864 | prose | pages [8] -->
m

<!-- b002865 | prose | pages [8] -->
m

<!-- b002866 | prose | pages [8] -->
m

<!-- b002867 | prose | pages [8] -->
m

<!-- b002868 | prose | pages [8] -->
m

<!-- b002869 | prose | pages [8] -->
m

<!-- b002870 | prose | pages [8] -->
m

<!-- b002871 | prose | pages [8] -->
m

<!-- b002872 | prose | pages [8] -->
m

<!-- b002873 | prose | pages [8] -->
m

<!-- b002874 | prose | pages [8] -->
m

<!-- b002875 | prose | pages [8] -->
m

<!-- b002876 | prose | pages [8] -->
m

<!-- b002877 | prose | pages [8] -->
m

<!-- b002878 | prose | pages [8] -->
m

<!-- b002879 | prose | pages [8] -->
m

<!-- b002880 | prose | pages [8] -->
m

<!-- b002881 | prose | pages [8] -->
m

<!-- b002882 | prose | pages [8] -->
m

<!-- b002883 | prose | pages [8] -->
m

<!-- b002884 | prose | pages [8] -->
m

<!-- b002885 | prose | pages [8] -->
m

<!-- b002886 | prose | pages [8] -->
m

<!-- b002887 | prose | pages [8] -->
m

<!-- b002888 | prose | pages [8] -->
m

<!-- b002889 | prose | pages [8] -->
m

<!-- b002890 | prose | pages [8] -->
m

<!-- b002891 | prose | pages [8] -->
m

<!-- b002892 | prose | pages [8] -->
m

<!-- b002893 | prose | pages [8] -->
m

<!-- b002894 | prose | pages [8] -->
m

<!-- b002895 | prose | pages [8] -->
m

<!-- b002896 | prose | pages [8] -->
m

<!-- b002897 | prose | pages [8] -->
m

<!-- b002898 | prose | pages [8] -->
m

<!-- b002899 | prose | pages [8] -->
m

<!-- b002900 | prose | pages [8] -->
m

<!-- b002901 | prose | pages [8] -->
m

<!-- b002902 | prose | pages [8] -->
m

<!-- b002903 | prose | pages [8] -->
m

<!-- b002904 | prose | pages [8] -->
m

<!-- b002905 | prose | pages [8] -->
m

<!-- b002906 | prose | pages [8] -->
m

<!-- b002907 | prose | pages [8] -->
m

<!-- b002908 | prose | pages [8] -->
m

<!-- b002909 | prose | pages [8] -->
m

<!-- b002910 | prose | pages [8] -->
m

<!-- b002911 | prose | pages [8] -->
m

<!-- b002912 | prose | pages [8] -->
m

<!-- b002913 | prose | pages [8] -->
m

<!-- b002914 | prose | pages [8] -->
m

<!-- b002915 | prose | pages [8] -->
m

<!-- b002916 | prose | pages [8] -->
m

<!-- b002917 | prose | pages [8] -->
m

<!-- b002918 | prose | pages [8] -->
m

<!-- b002919 | prose | pages [8] -->
m

<!-- b002920 | prose | pages [8] -->
m

<!-- b002921 | prose | pages [8] -->
m

<!-- b002922 | prose | pages [8] -->
m

<!-- b002923 | prose | pages [8] -->
m

<!-- b002924 | prose | pages [8] -->
m

<!-- b002925 | prose | pages [8] -->
m

<!-- b002926 | prose | pages [8] -->
m

<!-- b002927 | prose | pages [8] -->
m

<!-- b002928 | prose | pages [8] -->
m

<!-- b002929 | prose | pages [8] -->
m

<!-- b002930 | prose | pages [8] -->
m

<!-- b002931 | prose | pages [8] -->
m

<!-- b002932 | prose | pages [8] -->
m

<!-- b002933 | prose | pages [8] -->
m

<!-- b002934 | prose | pages [8] -->
m

<!-- b002935 | prose | pages [8] -->
m

<!-- b002936 | prose | pages [8] -->
m

<!-- b002937 | prose | pages [8] -->
m

<!-- b002938 | prose | pages [8] -->
m

<!-- b002939 | prose | pages [8] -->
m

<!-- b002940 | prose | pages [8] -->
m

<!-- b002941 | prose | pages [8] -->
m

<!-- b002942 | prose | pages [8] -->
m

<!-- b002943 | prose | pages [8] -->
m

<!-- b002944 | prose | pages [8] -->
m

<!-- b002945 | prose | pages [8] -->
m

<!-- b002946 | prose | pages [8] -->
m

<!-- b002947 | prose | pages [8] -->
m

<!-- b002948 | prose | pages [8] -->
m

<!-- b002949 | prose | pages [8] -->
m

<!-- b002950 | prose | pages [8] -->
m

<!-- b002951 | prose | pages [8] -->
m

<!-- b002952 | prose | pages [8] -->
m

<!-- b002953 | prose | pages [8] -->
m

<!-- b002954 | prose | pages [8] -->
m

<!-- b002955 | prose | pages [8] -->
m

<!-- b002956 | prose | pages [8] -->
m

<!-- b002957 | caption | pages [8] -->
Figure 4: Feedforward Neural Network-Model Construction

<!-- b002958 | prose | pages [8] -->
From Figure 4, the model follows a typical Feedforward Neural Network (FNN) structure, which includes an input layer, two hidden layers with ReLU activation functions, and an output layer with a linear activation function. The raw dataset is split into training and test sets, with the training set further divided into training data and validation data (20% of the training set). The model is trained using the Adam optimizer with a learning rate of 0.01. Validation loss is tracked during the training process to assess the model’s performance.

<!-- b002959 | prose | pages [8] -->
5.2.3 Weighted Fusion of Predictions

<!-- b002960 | caption | pages [8] -->
Figure 5: Weighted Fusion Construction

<!-- b002961 | prose | pages [8] -->
关注数学模型

<!-- b002962 | furniture | pages [8] -->
2

<!-- b002963 | furniture | pages [8] -->
MATHmodels

<!-- b002964 | furniture | pages [8] -->
获取更多资讯

<!-- b002965 | furniture | pages [9] -->
Team # 2503389

<!-- b002966 | furniture | pages [9] -->
Page 9 of 26

<!-- b002967 | prose | pages [9] -->
To enhance the accuracy and robustness of medal count predictions, we utilize a weighted fusion approach to combine the outputs of the Multiple Linear Regression (MLR) and Feedforward Neural Network (FNN) models.

<!-- b002968 | prose | pages [9] -->
First, the mean squared prediction errors (MSE) for the two models are calculated:

<!-- b002969 | prose | pages [9] -->
N X

<!-- b002970 | prose | pages [9] -->
MLR = 1

<!-- b002971 | prose | pages [9] -->
(Ri −PMLR,i)2 ,

<!-- b002972 | prose | pages [9] -->
PE2

<!-- b002973 | prose | pages [9] -->
N X

<!-- b002974 | prose | pages [9] -->
NN = 1

<!-- b002975 | prose | pages [9] -->
(Ri −PNN,i)2

<!-- b002976 | prose | pages [9] -->
PE2

<!-- b002977 | prose | pages [9] -->
微信公众号：数学模型

<!-- b002978 | prose | pages [9] -->
N

<!-- b002979 | prose | pages [9] -->
i=1

<!-- b002980 | prose | pages [9] -->
N

<!-- b002981 | prose | pages [9] -->
i=1

<!-- b002982 | prose | pages [9] -->
The weights for each model are derived based on their relative errors:

<!-- b002983 | prose | pages [9] -->
PE2

<!-- b002984 | prose | pages [9] -->
NN

<!-- b002985 | prose | pages [9] -->
≈0.6,

<!-- b002986 | prose | pages [9] -->
wMLR =

<!-- b002987 | prose | pages [9] -->
PE2

<!-- b002988 | prose | pages [9] -->
MLR + PE2

<!-- b002989 | prose | pages [9] -->
NN

<!-- b002990 | prose | pages [9] -->
PE2

<!-- b002991 | prose | pages [9] -->
MLR

<!-- b002992 | prose | pages [9] -->
≈0.4

<!-- b002993 | prose | pages [9] -->
wNN =

<!-- b002994 | prose | pages [9] -->
PE2

<!-- b002995 | prose | pages [9] -->
MLR + PE2

<!-- b002996 | prose | pages [9] -->
NN

<!-- b002997 | prose | pages [9] -->
Finally, the combined prediction for observation i is calculated as:

<!-- b002998 | prose | pages [9] -->
ˆPi = wMLR · PMLR,i + wNN · PNN,i

<!-- b002999 | prose | pages [9] -->
微信号：MATHmodels

<!-- b003000 | prose | pages [9] -->
Through analyzing prediction errors, it is clear that the MLP model suffers from higher errors, while the FNN model risks overfitting. The combined MLP-NN model addresses these issues, enhancing both accuracy and robustness for reliable predictions.

<!-- b003001 | prose | pages [9] -->
5.3

<!-- b003002 | heading | pages [9] -->
Forecast Results and Insights

<!-- b003003 | prose | pages [9] -->
Total Medals Gold Medals NOC

<!-- b003004 | prose | pages [9] -->
Pred.

<!-- b003005 | prose | pages [9] -->
Δ Rank Δ Pred.

<!-- b003006 | prose | pages [9] -->
Δ Rank

<!-- b003007 | prose | pages [9] -->
United States 143 ↑17 1 – 59 ↑19 China 76 ↓15 2 – 32 ↓8 United Kingdom 62 ↓3 3 – 21 ↑7 France 60 ↓4 4 – 16 – Australia 54 ↑1 5 – 21 ↑3 Japan 43 ↓2 6 – 16 ↓4 Italy 40 – 7 – 12 – Germany 36 ↑3 8 ↑1 12 – Netherlands 35 ↑1 9 ↓1 15 – Canada 30 ↑3 10 ↑1 10 ↑1

<!-- b003008 | prose | pages [9] -->
Confidence Intervals (95%)

<!-- b003009 | prose | pages [9] -->
Δ Total Lower Total Upper Gold Lower Gold Upper

<!-- b003010 | prose | pages [9] -->
1 1 – 110 192 50 68 2 2 ↓1 61 94 27 37 3 3 ↑4 56 85 17 25 5 5 – 50 73 13 19 3 3 ↑1 49 70 17 25 5 5 ↓2 35 51 13 19 8 8 ↑1 34 48 10 14 8 8 ↑2 31 44 10 14 7 7 ↓1 31 43 12 18 10 10 ↑2 27 37 8 12

<!-- b003011 | caption | pages [9] -->
Table 3: 2024 Olympic Medal Predictions with Rankings, Changes, and Confidence Intervals

<!-- b003012 | prose | pages [9] -->
Countries Likely to Improve: America (+17 medals) and Canada (+3 medals) show up- ward trends, may due to increased investment in athlete development and enhanced coaching strategies.

<!-- b003013 | prose | pages [9] -->
Countries Likely to Decline: France (60 medals vs. 64 in 2024) may experience a decline after hosting, while China (76 medals vs. 91 in 2024) faces challenges as its strong event, weightlifting1, will no longer be held.

<!-- b003014 | prose | pages [9] -->
Key Uncertainty: The U.S. medal interval highlights variability in team sports, while smaller nations like Slovenia (1 gold, CI: 0–2) exhibit greater volatility due to dependence on individual athletes.

<!-- b003015 | prose | pages [9] -->
m

<!-- b003016 | prose | pages [9] -->
m

<!-- b003017 | prose | pages [9] -->
m

<!-- b003018 | prose | pages [9] -->
m

<!-- b003019 | prose | pages [9] -->
m

<!-- b003020 | prose | pages [9] -->
m

<!-- b003021 | prose | pages [9] -->
m

<!-- b003022 | prose | pages [9] -->
m

<!-- b003023 | prose | pages [9] -->
m

<!-- b003024 | prose | pages [9] -->
m

<!-- b003025 | prose | pages [9] -->
m

<!-- b003026 | prose | pages [9] -->
m

<!-- b003027 | prose | pages [9] -->
m

<!-- b003028 | prose | pages [9] -->
m

<!-- b003029 | prose | pages [9] -->
m

<!-- b003030 | prose | pages [9] -->
m

<!-- b003031 | prose | pages [9] -->
m

<!-- b003032 | prose | pages [9] -->
m

<!-- b003033 | prose | pages [9] -->
m

<!-- b003034 | prose | pages [9] -->
m

<!-- b003035 | prose | pages [9] -->
m

<!-- b003036 | prose | pages [9] -->
m

<!-- b003037 | prose | pages [9] -->
m

<!-- b003038 | prose | pages [9] -->
m

<!-- b003039 | prose | pages [9] -->
m

<!-- b003040 | prose | pages [9] -->
m

<!-- b003041 | prose | pages [9] -->
m

<!-- b003042 | prose | pages [9] -->
m

<!-- b003043 | prose | pages [9] -->
m

<!-- b003044 | prose | pages [9] -->
m

<!-- b003045 | prose | pages [9] -->
m

<!-- b003046 | prose | pages [9] -->
m

<!-- b003047 | prose | pages [9] -->
m

<!-- b003048 | prose | pages [9] -->
m

<!-- b003049 | prose | pages [9] -->
m

<!-- b003050 | prose | pages [9] -->
m

<!-- b003051 | prose | pages [9] -->
m

<!-- b003052 | prose | pages [9] -->
m

<!-- b003053 | prose | pages [9] -->
m

<!-- b003054 | prose | pages [9] -->
m

<!-- b003055 | prose | pages [9] -->
m

<!-- b003056 | prose | pages [9] -->
m

<!-- b003057 | prose | pages [9] -->
m

<!-- b003058 | prose | pages [9] -->
m

<!-- b003059 | prose | pages [9] -->
m

<!-- b003060 | prose | pages [9] -->
m

<!-- b003061 | prose | pages [9] -->
m

<!-- b003062 | prose | pages [9] -->
m

<!-- b003063 | prose | pages [9] -->
m

<!-- b003064 | prose | pages [9] -->
m

<!-- b003065 | prose | pages [9] -->
m

<!-- b003066 | prose | pages [9] -->
m

<!-- b003067 | prose | pages [9] -->
m

<!-- b003068 | prose | pages [9] -->
m

<!-- b003069 | prose | pages [9] -->
m

<!-- b003070 | prose | pages [9] -->
m

<!-- b003071 | prose | pages [9] -->
m

<!-- b003072 | prose | pages [9] -->
m

<!-- b003073 | prose | pages [9] -->
m

<!-- b003074 | prose | pages [9] -->
m

<!-- b003075 | prose | pages [9] -->
m

<!-- b003076 | prose | pages [9] -->
m

<!-- b003077 | prose | pages [9] -->
m

<!-- b003078 | prose | pages [9] -->
m

<!-- b003079 | prose | pages [9] -->
m

<!-- b003080 | prose | pages [9] -->
m

<!-- b003081 | prose | pages [9] -->
m

<!-- b003082 | prose | pages [9] -->
m

<!-- b003083 | prose | pages [9] -->
m

<!-- b003084 | prose | pages [9] -->
m

<!-- b003085 | prose | pages [9] -->
m

<!-- b003086 | prose | pages [9] -->
m

<!-- b003087 | prose | pages [9] -->
m

<!-- b003088 | prose | pages [9] -->
m

<!-- b003089 | prose | pages [9] -->
m

<!-- b003090 | prose | pages [9] -->
m

<!-- b003091 | prose | pages [9] -->
m

<!-- b003092 | prose | pages [9] -->
m

<!-- b003093 | prose | pages [9] -->
m

<!-- b003094 | prose | pages [9] -->
m

<!-- b003095 | prose | pages [9] -->
m

<!-- b003096 | prose | pages [9] -->
m

<!-- b003097 | prose | pages [9] -->
m

<!-- b003098 | prose | pages [9] -->
m

<!-- b003099 | prose | pages [9] -->
m

<!-- b003100 | prose | pages [9] -->
m

<!-- b003101 | prose | pages [9] -->
m

<!-- b003102 | prose | pages [9] -->
m

<!-- b003103 | prose | pages [9] -->
m

<!-- b003104 | prose | pages [9] -->
m

<!-- b003105 | prose | pages [9] -->
m

<!-- b003106 | prose | pages [9] -->
m

<!-- b003107 | prose | pages [9] -->
m

<!-- b003108 | prose | pages [9] -->
m

<!-- b003109 | prose | pages [9] -->
m

<!-- b003110 | prose | pages [9] -->
m

<!-- b003111 | prose | pages [9] -->
m

<!-- b003112 | prose | pages [9] -->
m

<!-- b003113 | prose | pages [9] -->
m

<!-- b003114 | prose | pages [9] -->
m

<!-- b003115 | prose | pages [9] -->
m

<!-- b003116 | prose | pages [9] -->
m

<!-- b003117 | prose | pages [9] -->
m

<!-- b003118 | prose | pages [9] -->
m

<!-- b003119 | prose | pages [9] -->
m

<!-- b003120 | prose | pages [9] -->
m

<!-- b003121 | prose | pages [9] -->
m

<!-- b003122 | prose | pages [9] -->
m

<!-- b003123 | prose | pages [9] -->
m

<!-- b003124 | prose | pages [9] -->
m

<!-- b003125 | prose | pages [9] -->
m

<!-- b003126 | prose | pages [9] -->
m

<!-- b003127 | prose | pages [9] -->
m

<!-- b003128 | prose | pages [9] -->
m

<!-- b003129 | prose | pages [9] -->
m

<!-- b003130 | prose | pages [9] -->
m

<!-- b003131 | prose | pages [9] -->
m

<!-- b003132 | prose | pages [9] -->
m

<!-- b003133 | prose | pages [9] -->
m

<!-- b003134 | prose | pages [9] -->
m

<!-- b003135 | prose | pages [9] -->
m

<!-- b003136 | prose | pages [9] -->
m

<!-- b003137 | prose | pages [9] -->
m

<!-- b003138 | prose | pages [9] -->
m

<!-- b003139 | prose | pages [9] -->
m

<!-- b003140 | prose | pages [9] -->
m

<!-- b003141 | prose | pages [9] -->
m

<!-- b003142 | prose | pages [9] -->
m

<!-- b003143 | prose | pages [9] -->
m

<!-- b003144 | prose | pages [9] -->
m

<!-- b003145 | prose | pages [9] -->
m

<!-- b003146 | prose | pages [9] -->
m

<!-- b003147 | prose | pages [9] -->
m

<!-- b003148 | prose | pages [9] -->
m

<!-- b003149 | prose | pages [9] -->
m

<!-- b003150 | prose | pages [9] -->
m

<!-- b003151 | prose | pages [9] -->
m

<!-- b003152 | prose | pages [9] -->
m

<!-- b003153 | prose | pages [9] -->
m

<!-- b003154 | prose | pages [9] -->
m

<!-- b003155 | prose | pages [9] -->
m

<!-- b003156 | prose | pages [9] -->
m

<!-- b003157 | prose | pages [9] -->
m

<!-- b003158 | prose | pages [9] -->
m

<!-- b003159 | prose | pages [9] -->
m

<!-- b003160 | prose | pages [9] -->
m

<!-- b003161 | prose | pages [9] -->
m

<!-- b003162 | prose | pages [9] -->
m

<!-- b003163 | prose | pages [9] -->
m

<!-- b003164 | prose | pages [9] -->
m

<!-- b003165 | prose | pages [9] -->
m

<!-- b003166 | prose | pages [9] -->
m

<!-- b003167 | prose | pages [9] -->
m

<!-- b003168 | prose | pages [9] -->
m

<!-- b003169 | prose | pages [9] -->
m

<!-- b003170 | prose | pages [9] -->
m

<!-- b003171 | prose | pages [9] -->
m

<!-- b003172 | prose | pages [9] -->
m

<!-- b003173 | prose | pages [9] -->
m

<!-- b003174 | prose | pages [9] -->
m

<!-- b003175 | prose | pages [9] -->
m

<!-- b003176 | prose | pages [9] -->
m

<!-- b003177 | prose | pages [9] -->
m

<!-- b003178 | prose | pages [9] -->
m

<!-- b003179 | prose | pages [9] -->
m

<!-- b003180 | prose | pages [9] -->
m

<!-- b003181 | prose | pages [9] -->
m

<!-- b003182 | prose | pages [9] -->
m

<!-- b003183 | prose | pages [9] -->
m

<!-- b003184 | prose | pages [9] -->
m

<!-- b003185 | prose | pages [9] -->
m

<!-- b003186 | prose | pages [9] -->
m

<!-- b003187 | prose | pages [9] -->
m

<!-- b003188 | prose | pages [9] -->
m

<!-- b003189 | prose | pages [9] -->
m

<!-- b003190 | prose | pages [9] -->
m

<!-- b003191 | prose | pages [9] -->
m

<!-- b003192 | prose | pages [9] -->
m

<!-- b003193 | prose | pages [9] -->
m

<!-- b003194 | prose | pages [9] -->
m

<!-- b003195 | prose | pages [9] -->
m

<!-- b003196 | prose | pages [9] -->
m

<!-- b003197 | prose | pages [9] -->
m

<!-- b003198 | prose | pages [9] -->
m

<!-- b003199 | prose | pages [9] -->
m

<!-- b003200 | prose | pages [9] -->
m

<!-- b003201 | prose | pages [9] -->
m

<!-- b003202 | prose | pages [9] -->
m

<!-- b003203 | prose | pages [9] -->
m

<!-- b003204 | prose | pages [9] -->
m

<!-- b003205 | prose | pages [9] -->
m

<!-- b003206 | prose | pages [9] -->
m

<!-- b003207 | prose | pages [9] -->
m

<!-- b003208 | prose | pages [9] -->
m

<!-- b003209 | prose | pages [9] -->
m

<!-- b003210 | prose | pages [9] -->
m

<!-- b003211 | prose | pages [9] -->
m

<!-- b003212 | prose | pages [9] -->
m

<!-- b003213 | prose | pages [9] -->
m

<!-- b003214 | prose | pages [9] -->
m

<!-- b003215 | prose | pages [9] -->
m

<!-- b003216 | prose | pages [9] -->
m

<!-- b003217 | prose | pages [9] -->
m

<!-- b003218 | prose | pages [9] -->
m

<!-- b003219 | prose | pages [9] -->
m

<!-- b003220 | prose | pages [9] -->
m

<!-- b003221 | prose | pages [9] -->
m

<!-- b003222 | prose | pages [9] -->
m

<!-- b003223 | prose | pages [9] -->
m

<!-- b003224 | prose | pages [9] -->
m

<!-- b003225 | prose | pages [9] -->
m

<!-- b003226 | prose | pages [9] -->
m

<!-- b003227 | prose | pages [9] -->
m

<!-- b003228 | prose | pages [9] -->
m

<!-- b003229 | prose | pages [9] -->
m

<!-- b003230 | prose | pages [9] -->
m

<!-- b003231 | prose | pages [9] -->
m

<!-- b003232 | prose | pages [9] -->
m

<!-- b003233 | prose | pages [9] -->
m

<!-- b003234 | prose | pages [9] -->
m

<!-- b003235 | prose | pages [9] -->
m

<!-- b003236 | prose | pages [9] -->
m

<!-- b003237 | prose | pages [9] -->
m

<!-- b003238 | prose | pages [9] -->
m

<!-- b003239 | prose | pages [9] -->
m

<!-- b003240 | prose | pages [9] -->
m

<!-- b003241 | prose | pages [9] -->
m

<!-- b003242 | prose | pages [9] -->
m

<!-- b003243 | prose | pages [9] -->
m

<!-- b003244 | prose | pages [9] -->
m

<!-- b003245 | prose | pages [9] -->
m

<!-- b003246 | prose | pages [9] -->
m

<!-- b003247 | prose | pages [9] -->
m

<!-- b003248 | prose | pages [9] -->
m

<!-- b003249 | prose | pages [9] -->
m

<!-- b003250 | prose | pages [9] -->
m

<!-- b003251 | prose | pages [9] -->
m

<!-- b003252 | prose | pages [9] -->
m

<!-- b003253 | prose | pages [9] -->
m

<!-- b003254 | prose | pages [9] -->
m

<!-- b003255 | prose | pages [9] -->
m

<!-- b003256 | prose | pages [9] -->
m

<!-- b003257 | prose | pages [9] -->
m

<!-- b003258 | prose | pages [9] -->
m

<!-- b003259 | prose | pages [9] -->
m

<!-- b003260 | prose | pages [9] -->
m

<!-- b003261 | prose | pages [9] -->
m

<!-- b003262 | prose | pages [9] -->
m

<!-- b003263 | prose | pages [9] -->
m

<!-- b003264 | prose | pages [9] -->
m

<!-- b003265 | prose | pages [9] -->
m

<!-- b003266 | prose | pages [9] -->
m

<!-- b003267 | prose | pages [9] -->
m

<!-- b003268 | prose | pages [9] -->
m

<!-- b003269 | prose | pages [9] -->
m

<!-- b003270 | prose | pages [9] -->
m

<!-- b003271 | prose | pages [9] -->
m

<!-- b003272 | prose | pages [9] -->
m

<!-- b003273 | prose | pages [9] -->
m

<!-- b003274 | prose | pages [9] -->
m

<!-- b003275 | prose | pages [9] -->
m

<!-- b003276 | prose | pages [9] -->
m

<!-- b003277 | prose | pages [9] -->
m

<!-- b003278 | prose | pages [9] -->
m

<!-- b003279 | prose | pages [9] -->
m

<!-- b003280 | prose | pages [9] -->
m

<!-- b003281 | prose | pages [9] -->
m

<!-- b003282 | prose | pages [9] -->
m

<!-- b003283 | prose | pages [9] -->
m

<!-- b003284 | prose | pages [9] -->
m

<!-- b003285 | prose | pages [9] -->
m

<!-- b003286 | prose | pages [9] -->
m

<!-- b003287 | prose | pages [9] -->
m

<!-- b003288 | prose | pages [9] -->
m

<!-- b003289 | prose | pages [9] -->
m

<!-- b003290 | prose | pages [9] -->
m

<!-- b003291 | prose | pages [9] -->
m

<!-- b003292 | prose | pages [9] -->
m

<!-- b003293 | prose | pages [9] -->
m

<!-- b003294 | prose | pages [9] -->
m

<!-- b003295 | prose | pages [9] -->
m

<!-- b003296 | prose | pages [9] -->
m

<!-- b003297 | prose | pages [9] -->
m

<!-- b003298 | prose | pages [9] -->
m

<!-- b003299 | furniture | pages [9] -->
m

<!-- b003300 | furniture | pages [9] -->
m

<!-- b003301 | furniture | pages [9] -->
m

<!-- b003302 | furniture | pages [9] -->
m

<!-- b003303 | furniture | pages [9] -->
m

<!-- b003304 | furniture | pages [9] -->
m

<!-- b003305 | furniture | pages [9] -->
m

<!-- b003306 | furniture | pages [9] -->
m

<!-- b003307 | furniture | pages [9] -->
m

<!-- b003308 | furniture | pages [9] -->
m

<!-- b003309 | furniture | pages [9] -->
m

<!-- b003310 | furniture | pages [9] -->
m

<!-- b003311 | furniture | pages [9] -->
m

<!-- b003312 | furniture | pages [9] -->
m

<!-- b003313 | furniture | pages [9] -->
m

<!-- b003314 | furniture | pages [9] -->
m

<!-- b003315 | furniture | pages [9] -->
m

<!-- b003316 | furniture | pages [9] -->
m

<!-- b003317 | furniture | pages [9] -->
m

<!-- b003318 | furniture | pages [9] -->
m

<!-- b003319 | furniture | pages [9] -->
m

<!-- b003320 | furniture | pages [9] -->
m

<!-- b003321 | furniture | pages [9] -->
m

<!-- b003322 | furniture | pages [9] -->
m

<!-- b003323 | furniture | pages [9] -->
m

<!-- b003324 | furniture | pages [9] -->
m

<!-- b003325 | furniture | pages [9] -->
m

<!-- b003326 | furniture | pages [9] -->
m

<!-- b003327 | furniture | pages [9] -->
m

<!-- b003328 | furniture | pages [9] -->
m

<!-- b003329 | furniture | pages [9] -->
m

<!-- b003330 | furniture | pages [9] -->
m

<!-- b003331 | furniture | pages [9] -->
m

<!-- b003332 | furniture | pages [9] -->
m

<!-- b003333 | furniture | pages [9] -->
m

<!-- b003334 | furniture | pages [9] -->
m

<!-- b003335 | furniture | pages [9] -->
m

<!-- b003336 | furniture | pages [9] -->
m

<!-- b003337 | furniture | pages [9] -->
m

<!-- b003338 | furniture | pages [9] -->
m

<!-- b003339 | furniture | pages [9] -->
m

<!-- b003340 | furniture | pages [9] -->
m

<!-- b003341 | furniture | pages [9] -->
m

<!-- b003342 | furniture | pages [9] -->
m

<!-- b003343 | furniture | pages [9] -->
m

<!-- b003344 | furniture | pages [9] -->
m

<!-- b003345 | furniture | pages [9] -->
m

<!-- b003346 | furniture | pages [9] -->
m

<!-- b003347 | furniture | pages [9] -->
m

<!-- b003348 | furniture | pages [9] -->
m

<!-- b003349 | furniture | pages [9] -->
m

<!-- b003350 | furniture | pages [9] -->
m

<!-- b003351 | furniture | pages [9] -->
m

<!-- b003352 | furniture | pages [9] -->
m

<!-- b003353 | furniture | pages [9] -->
m

<!-- b003354 | furniture | pages [9] -->
m

<!-- b003355 | furniture | pages [9] -->
m

<!-- b003356 | furniture | pages [9] -->
m

<!-- b003357 | furniture | pages [9] -->
m

<!-- b003358 | furniture | pages [9] -->
m

<!-- b003359 | furniture | pages [9] -->
m

<!-- b003360 | furniture | pages [9] -->
m

<!-- b003361 | furniture | pages [9] -->
m

<!-- b003362 | furniture | pages [9] -->
m

<!-- b003363 | furniture | pages [9] -->
m

<!-- b003364 | furniture | pages [9] -->
m

<!-- b003365 | furniture | pages [9] -->
m

<!-- b003366 | furniture | pages [9] -->
m

<!-- b003367 | furniture | pages [9] -->
m

<!-- b003368 | furniture | pages [9] -->
m

<!-- b003369 | furniture | pages [9] -->
m

<!-- b003370 | furniture | pages [9] -->
m

<!-- b003371 | furniture | pages [9] -->
m

<!-- b003372 | furniture | pages [9] -->
m

<!-- b003373 | furniture | pages [9] -->
m

<!-- b003374 | furniture | pages [9] -->
m

<!-- b003375 | furniture | pages [9] -->
m

<!-- b003376 | furniture | pages [9] -->
m

<!-- b003377 | furniture | pages [9] -->
m

<!-- b003378 | furniture | pages [9] -->
m

<!-- b003379 | furniture | pages [9] -->
m

<!-- b003380 | furniture | pages [9] -->
m

<!-- b003381 | furniture | pages [9] -->
m

<!-- b003382 | furniture | pages [9] -->
m

<!-- b003383 | furniture | pages [9] -->
m

<!-- b003384 | furniture | pages [9] -->
m

<!-- b003385 | furniture | pages [9] -->
m

<!-- b003386 | furniture | pages [9] -->
m

<!-- b003387 | furniture | pages [9] -->
m

<!-- b003388 | furniture | pages [9] -->
m

<!-- b003389 | furniture | pages [9] -->
m

<!-- b003390 | furniture | pages [9] -->
m

<!-- b003391 | furniture | pages [9] -->
m

<!-- b003392 | furniture | pages [9] -->
m

<!-- b003393 | furniture | pages [9] -->
m

<!-- b003394 | furniture | pages [9] -->
m

<!-- b003395 | furniture | pages [9] -->
m

<!-- b003396 | furniture | pages [9] -->
m

<!-- b003397 | furniture | pages [9] -->
m

<!-- b003398 | furniture | pages [9] -->
m

<!-- b003399 | furniture | pages [9] -->
m

<!-- b003400 | furniture | pages [9] -->
m

<!-- b003401 | furniture | pages [9] -->
m

<!-- b003402 | furniture | pages [9] -->
m

<!-- b003403 | furniture | pages [9] -->
m

<!-- b003404 | furniture | pages [9] -->
m

<!-- b003405 | furniture | pages [9] -->
m

<!-- b003406 | furniture | pages [9] -->
m

<!-- b003407 | furniture | pages [9] -->
m

<!-- b003408 | furniture | pages [9] -->
m

<!-- b003409 | furniture | pages [9] -->
m

<!-- b003410 | furniture | pages [9] -->
m

<!-- b003411 | furniture | pages [9] -->
m

<!-- b003412 | furniture | pages [9] -->
m

<!-- b003413 | furniture | pages [9] -->
m

<!-- b003414 | furniture | pages [9] -->
m

<!-- b003415 | furniture | pages [9] -->
m

<!-- b003416 | furniture | pages [9] -->
m

<!-- b003417 | furniture | pages [9] -->
m

<!-- b003418 | furniture | pages [9] -->
m

<!-- b003419 | furniture | pages [9] -->
m

<!-- b003420 | furniture | pages [9] -->
m

<!-- b003421 | furniture | pages [9] -->
m

<!-- b003422 | furniture | pages [9] -->
m

<!-- b003423 | furniture | pages [9] -->
m

<!-- b003424 | furniture | pages [9] -->
m

<!-- b003425 | furniture | pages [9] -->
m

<!-- b003426 | furniture | pages [9] -->
m

<!-- b003427 | furniture | pages [9] -->
m

<!-- b003428 | furniture | pages [9] -->
m

<!-- b003429 | furniture | pages [9] -->
m

<!-- b003430 | furniture | pages [9] -->
m

<!-- b003431 | furniture | pages [9] -->
m

<!-- b003432 | furniture | pages [9] -->
m

<!-- b003433 | furniture | pages [9] -->
m

<!-- b003434 | furniture | pages [9] -->
m

<!-- b003435 | furniture | pages [9] -->
m

<!-- b003436 | furniture | pages [9] -->
m

<!-- b003437 | furniture | pages [9] -->
m

<!-- b003438 | furniture | pages [9] -->
m

<!-- b003439 | furniture | pages [9] -->
m

<!-- b003440 | furniture | pages [9] -->
m

<!-- b003441 | furniture | pages [9] -->
m

<!-- b003442 | furniture | pages [9] -->
m

<!-- b003443 | furniture | pages [9] -->
m

<!-- b003444 | furniture | pages [9] -->
m

<!-- b003445 | furniture | pages [9] -->
m

<!-- b003446 | furniture | pages [9] -->
m

<!-- b003447 | furniture | pages [9] -->
m

<!-- b003448 | furniture | pages [9] -->
m

<!-- b003449 | furniture | pages [9] -->
m

<!-- b003450 | furniture | pages [9] -->
m

<!-- b003451 | furniture | pages [9] -->
m

<!-- b003452 | furniture | pages [9] -->
m

<!-- b003453 | furniture | pages [9] -->
m

<!-- b003454 | furniture | pages [9] -->
m

<!-- b003455 | furniture | pages [9] -->
m

<!-- b003456 | furniture | pages [9] -->
m

<!-- b003457 | furniture | pages [9] -->
m

<!-- b003458 | furniture | pages [9] -->
m

<!-- b003459 | furniture | pages [9] -->
m

<!-- b003460 | furniture | pages [9] -->
m

<!-- b003461 | furniture | pages [9] -->
m

<!-- b003462 | furniture | pages [9] -->
m

<!-- b003463 | furniture | pages [9] -->
m

<!-- b003464 | furniture | pages [9] -->
m

<!-- b003465 | furniture | pages [9] -->
m

<!-- b003466 | furniture | pages [9] -->
m

<!-- b003467 | furniture | pages [9] -->
m

<!-- b003468 | furniture | pages [9] -->
m

<!-- b003469 | furniture | pages [9] -->
m

<!-- b003470 | furniture | pages [9] -->
m

<!-- b003471 | furniture | pages [9] -->
m

<!-- b003472 | furniture | pages [9] -->
m

<!-- b003473 | furniture | pages [9] -->
m

<!-- b003474 | furniture | pages [9] -->
m

<!-- b003475 | furniture | pages [9] -->
m

<!-- b003476 | furniture | pages [9] -->
m

<!-- b003477 | furniture | pages [9] -->
m

<!-- b003478 | furniture | pages [9] -->
m

<!-- b003479 | furniture | pages [9] -->
m

<!-- b003480 | furniture | pages [9] -->
m

<!-- b003481 | furniture | pages [9] -->
m

<!-- b003482 | furniture | pages [9] -->
m

<!-- b003483 | furniture | pages [9] -->
m

<!-- b003484 | furniture | pages [9] -->
m

<!-- b003485 | furniture | pages [9] -->
m

<!-- b003486 | furniture | pages [9] -->
m

<!-- b003487 | furniture | pages [9] -->
m

<!-- b003488 | furniture | pages [9] -->
m

<!-- b003489 | furniture | pages [9] -->
m

<!-- b003490 | furniture | pages [9] -->
m

<!-- b003491 | furniture | pages [9] -->
m

<!-- b003492 | furniture | pages [9] -->
m

<!-- b003493 | furniture | pages [9] -->
m

<!-- b003494 | furniture | pages [9] -->
m

<!-- b003495 | furniture | pages [9] -->
m

<!-- b003496 | furniture | pages [9] -->
m

<!-- b003497 | furniture | pages [9] -->
m

<!-- b003498 | furniture | pages [9] -->
m

<!-- b003499 | furniture | pages [9] -->
m

<!-- b003500 | furniture | pages [9] -->
m

<!-- b003501 | furniture | pages [9] -->
m

<!-- b003502 | furniture | pages [9] -->
m

<!-- b003503 | furniture | pages [9] -->
m

<!-- b003504 | furniture | pages [9] -->
m

<!-- b003505 | furniture | pages [9] -->
m

<!-- b003506 | furniture | pages [9] -->
m

<!-- b003507 | furniture | pages [9] -->
m

<!-- b003508 | furniture | pages [9] -->
m

<!-- b003509 | furniture | pages [9] -->
m

<!-- b003510 | furniture | pages [9] -->
m

<!-- b003511 | furniture | pages [9] -->
m

<!-- b003512 | furniture | pages [9] -->
m

<!-- b003513 | furniture | pages [9] -->
m

<!-- b003514 | furniture | pages [9] -->
m

<!-- b003515 | furniture | pages [9] -->
m

<!-- b003516 | furniture | pages [9] -->
m

<!-- b003517 | furniture | pages [9] -->
m

<!-- b003518 | furniture | pages [9] -->
m

<!-- b003519 | furniture | pages [9] -->
m

<!-- b003520 | furniture | pages [9] -->
m

<!-- b003521 | furniture | pages [9] -->
m

<!-- b003522 | furniture | pages [9] -->
m

<!-- b003523 | furniture | pages [9] -->
m

<!-- b003524 | furniture | pages [9] -->
m

<!-- b003525 | furniture | pages [9] -->
m

<!-- b003526 | furniture | pages [9] -->
m

<!-- b003527 | furniture | pages [9] -->
m

<!-- b003528 | furniture | pages [9] -->
m

<!-- b003529 | furniture | pages [9] -->
m

<!-- b003530 | furniture | pages [9] -->
m

<!-- b003531 | furniture | pages [9] -->
m

<!-- b003532 | furniture | pages [9] -->
m

<!-- b003533 | furniture | pages [9] -->
m

<!-- b003534 | furniture | pages [9] -->
m

<!-- b003535 | furniture | pages [9] -->
m

<!-- b003536 | furniture | pages [9] -->
m

<!-- b003537 | furniture | pages [9] -->
m

<!-- b003538 | furniture | pages [9] -->
m

<!-- b003539 | furniture | pages [9] -->
m

<!-- b003540 | furniture | pages [9] -->
m

<!-- b003541 | furniture | pages [9] -->
m

<!-- b003542 | furniture | pages [9] -->
m

<!-- b003543 | furniture | pages [9] -->
m

<!-- b003544 | furniture | pages [9] -->
m

<!-- b003545 | furniture | pages [9] -->
m

<!-- b003546 | furniture | pages [9] -->
m

<!-- b003547 | furniture | pages [9] -->
m

<!-- b003548 | furniture | pages [9] -->
m

<!-- b003549 | furniture | pages [9] -->
m

<!-- b003550 | furniture | pages [9] -->
m

<!-- b003551 | furniture | pages [9] -->
m

<!-- b003552 | furniture | pages [9] -->
m

<!-- b003553 | furniture | pages [9] -->
m

<!-- b003554 | furniture | pages [9] -->
m

<!-- b003555 | furniture | pages [9] -->
m

<!-- b003556 | furniture | pages [9] -->
m

<!-- b003557 | furniture | pages [9] -->
m

<!-- b003558 | furniture | pages [9] -->
m

<!-- b003559 | furniture | pages [9] -->
m

<!-- b003560 | furniture | pages [9] -->
m

<!-- b003561 | furniture | pages [9] -->
m

<!-- b003562 | furniture | pages [9] -->
m

<!-- b003563 | furniture | pages [9] -->
m

<!-- b003564 | furniture | pages [9] -->
m

<!-- b003565 | furniture | pages [9] -->
m

<!-- b003566 | furniture | pages [9] -->
m

<!-- b003567 | furniture | pages [9] -->
m

<!-- b003568 | furniture | pages [9] -->
m

<!-- b003569 | furniture | pages [9] -->
m

<!-- b003570 | furniture | pages [9] -->
m

<!-- b003571 | furniture | pages [9] -->
m

<!-- b003572 | furniture | pages [9] -->
m

<!-- b003573 | furniture | pages [9] -->
m

<!-- b003574 | furniture | pages [9] -->
m

<!-- b003575 | furniture | pages [9] -->
m

<!-- b003576 | furniture | pages [9] -->
m

<!-- b003577 | furniture | pages [9] -->
m

<!-- b003578 | furniture | pages [9] -->
m

<!-- b003579 | furniture | pages [9] -->
m

<!-- b003580 | furniture | pages [9] -->
m

<!-- b003581 | furniture | pages [9] -->
m

<!-- b003582 | furniture | pages [9] -->
m

<!-- b003583 | furniture | pages [9] -->
m

<!-- b003584 | furniture | pages [9] -->
m

<!-- b003585 | furniture | pages [9] -->
m

<!-- b003586 | furniture | pages [9] -->
m

<!-- b003587 | furniture | pages [9] -->
m

<!-- b003588 | furniture | pages [9] -->
m

<!-- b003589 | furniture | pages [9] -->
m

<!-- b003590 | furniture | pages [9] -->
m

<!-- b003591 | furniture | pages [9] -->
m

<!-- b003592 | furniture | pages [9] -->
m

<!-- b003593 | furniture | pages [9] -->
m

<!-- b003594 | furniture | pages [9] -->
m

<!-- b003595 | furniture | pages [9] -->
m

<!-- b003596 | furniture | pages [9] -->
m

<!-- b003597 | furniture | pages [9] -->
m

<!-- b003598 | furniture | pages [9] -->
m

<!-- b003599 | furniture | pages [9] -->
m

<!-- b003600 | furniture | pages [9] -->
m

<!-- b003601 | furniture | pages [9] -->
m

<!-- b003602 | furniture | pages [9] -->
m

<!-- b003603 | furniture | pages [9] -->
m

<!-- b003604 | furniture | pages [9] -->
m

<!-- b003605 | furniture | pages [9] -->
m

<!-- b003606 | furniture | pages [9] -->
m

<!-- b003607 | furniture | pages [9] -->
m

<!-- b003608 | furniture | pages [9] -->
m

<!-- b003609 | furniture | pages [9] -->
m

<!-- b003610 | furniture | pages [9] -->
m

<!-- b003611 | furniture | pages [9] -->
m

<!-- b003612 | furniture | pages [9] -->
m

<!-- b003613 | furniture | pages [9] -->
m

<!-- b003614 | furniture | pages [9] -->
m

<!-- b003615 | furniture | pages [9] -->
m

<!-- b003616 | furniture | pages [9] -->
m

<!-- b003617 | furniture | pages [9] -->
m

<!-- b003618 | furniture | pages [9] -->
m

<!-- b003619 | furniture | pages [9] -->
m

<!-- b003620 | furniture | pages [9] -->
m

<!-- b003621 | furniture | pages [9] -->
m

<!-- b003622 | furniture | pages [9] -->
m

<!-- b003623 | furniture | pages [9] -->
m

<!-- b003624 | furniture | pages [9] -->
m

<!-- b003625 | furniture | pages [9] -->
m

<!-- b003626 | furniture | pages [9] -->
m

<!-- b003627 | furniture | pages [9] -->
m

<!-- b003628 | furniture | pages [9] -->
m

<!-- b003629 | furniture | pages [9] -->
m

<!-- b003630 | furniture | pages [9] -->
m

<!-- b003631 | furniture | pages [9] -->
m

<!-- b003632 | furniture | pages [9] -->
m

<!-- b003633 | furniture | pages [9] -->
m

<!-- b003634 | furniture | pages [9] -->
m

<!-- b003635 | furniture | pages [9] -->
m

<!-- b003636 | furniture | pages [9] -->
m

<!-- b003637 | furniture | pages [9] -->
m

<!-- b003638 | furniture | pages [9] -->
m

<!-- b003639 | furniture | pages [9] -->
m

<!-- b003640 | furniture | pages [9] -->
m

<!-- b003641 | furniture | pages [9] -->
m

<!-- b003642 | furniture | pages [9] -->
m

<!-- b003643 | furniture | pages [9] -->
m

<!-- b003644 | furniture | pages [9] -->
m

<!-- b003645 | furniture | pages [9] -->
m

<!-- b003646 | furniture | pages [9] -->
m

<!-- b003647 | furniture | pages [9] -->
m

<!-- b003648 | furniture | pages [9] -->
m

<!-- b003649 | furniture | pages [9] -->
m

<!-- b003650 | furniture | pages [9] -->
m

<!-- b003651 | furniture | pages [9] -->
m

<!-- b003652 | furniture | pages [9] -->
m

<!-- b003653 | furniture | pages [9] -->
m

<!-- b003654 | furniture | pages [9] -->
m

<!-- b003655 | furniture | pages [9] -->
m

<!-- b003656 | furniture | pages [9] -->
m

<!-- b003657 | furniture | pages [9] -->
m

<!-- b003658 | furniture | pages [9] -->
m

<!-- b003659 | furniture | pages [9] -->
m

<!-- b003660 | furniture | pages [9] -->
m

<!-- b003661 | furniture | pages [9] -->
m

<!-- b003662 | furniture | pages [9] -->
m

<!-- b003663 | furniture | pages [9] -->
m

<!-- b003664 | furniture | pages [9] -->
m

<!-- b003665 | furniture | pages [9] -->
m

<!-- b003666 | furniture | pages [9] -->
m

<!-- b003667 | furniture | pages [9] -->
m

<!-- b003668 | furniture | pages [9] -->
m

<!-- b003669 | furniture | pages [9] -->
m

<!-- b003670 | furniture | pages [9] -->
m

<!-- b003671 | furniture | pages [9] -->
m

<!-- b003672 | furniture | pages [9] -->
m

<!-- b003673 | furniture | pages [9] -->
m

<!-- b003674 | furniture | pages [9] -->
m

<!-- b003675 | furniture | pages [9] -->
m

<!-- b003676 | furniture | pages [9] -->
m

<!-- b003677 | furniture | pages [9] -->
m

<!-- b003678 | furniture | pages [9] -->
m

<!-- b003679 | furniture | pages [9] -->
m

<!-- b003680 | furniture | pages [9] -->
m

<!-- b003681 | furniture | pages [9] -->
m

<!-- b003682 | furniture | pages [9] -->
m

<!-- b003683 | furniture | pages [9] -->
m

<!-- b003684 | furniture | pages [9] -->
m

<!-- b003685 | furniture | pages [9] -->
m

<!-- b003686 | furniture | pages [9] -->
m

<!-- b003687 | furniture | pages [9] -->
m

<!-- b003688 | furniture | pages [9] -->
m

<!-- b003689 | furniture | pages [9] -->
m

<!-- b003690 | furniture | pages [9] -->
m

<!-- b003691 | furniture | pages [9] -->
m

<!-- b003692 | furniture | pages [9] -->
m

<!-- b003693 | furniture | pages [9] -->
m

<!-- b003694 | furniture | pages [9] -->
m

<!-- b003695 | furniture | pages [9] -->
m

<!-- b003696 | furniture | pages [9] -->
m

<!-- b003697 | furniture | pages [9] -->
m

<!-- b003698 | furniture | pages [9] -->
m

<!-- b003699 | furniture | pages [9] -->
m

<!-- b003700 | furniture | pages [9] -->
m

<!-- b003701 | furniture | pages [9] -->
m

<!-- b003702 | furniture | pages [11] -->
Team # 2503389

<!-- b003703 | furniture | pages [11] -->
Page 11 of 26

<!-- b003704 | caption | pages [11] -->
Table 4: Regression Coefficients for the Multivariate Linear Model

<!-- b003705 | prose | pages [11] -->
Variable Coeﬀicient

<!-- b003706 | prose | pages [11] -->
Host Boost (XHost) 13.10 Athlete Pool (XAth) 0.004

<!-- b003707 | prose | pages [11] -->
Standard Error t-Statistic P-Value(P>|t|)

<!-- b003708 | prose | pages [11] -->
2.88 4.55 <0.001 0.003 1.33 0.188

<!-- b003709 | prose | pages [11] -->
微信公众号：数学模型

<!-- b003710 | prose | pages [11] -->
Competitiveness Index (XComp) 2.18 Historical Momentum (XHist) 0.59 0.71 3.06 0.003 0.09 6.42 <0.001

<!-- b003711 | prose | pages [11] -->
• Competitiveness Index (XComp) and Historical Momentum (XHist): Both have signifi- cant positive effects, with coefficients of 2.18 and 0.59 (p < 0.01). Historical Momentum has the highest t-value (6.42) and the lowest standard error (0.09), highlighting its strong influence on medal performance.

<!-- b003712 | prose | pages [11] -->
• Athlete Pool (XAth): The coefficient (0.004) is not statistically significant (p = 0.188), suggesting that athlete pool size alone does not fully explain medal outcomes.

<!-- b003713 | prose | pages [11] -->
微信号：MATHmodels

<!-- b003714 | prose | pages [11] -->
Overall, the model effectively captures the primary drivers of medal distribution, with sig- nificant contributions from host status, competitiveness, and historical momentum.

<!-- b003715 | caption | pages [11] -->
Table 5: Key Metrics and Results of Regression Analysis

<!-- b003716 | prose | pages [11] -->
Metric Formula

<!-- b003717 | prose | pages [11] -->
Mean Squared Error (MSE) MSE = 1

<!-- b003718 | prose | pages [11] -->
N

<!-- b003719 | prose | pages [11] -->
Root Mean Squared Er-

<!-- b003720 | prose | pages [11] -->
v u

<!-- b003721 | prose | pages [11] -->
ror (RMSE)

<!-- b003722 | prose | pages [11] -->
u t 1

<!-- b003723 | prose | pages [11] -->
RMSE =

<!-- b003724 | prose | pages [11] -->
Mean Absolute Per- centage Error (MAPE) MAPE = 100

<!-- b003725 | prose | pages [11] -->
N

<!-- b003726 | heading | pages [11] -->
Result

<!-- b003727 | prose | pages [11] -->
7.115

<!-- b003728 | prose | pages [11] -->
N X

<!-- b003729 | prose | pages [11] -->
(yi −ˆyi)2

<!-- b003730 | prose | pages [11] -->
i=1

<!-- b003731 | prose | pages [11] -->
2.667

<!-- b003732 | prose | pages [11] -->
N X

<!-- b003733 | prose | pages [11] -->
(yi −ˆyi)2

<!-- b003734 | prose | pages [11] -->
N N

<!-- b003735 | prose | pages [11] -->
i=1

<!-- b003736 | prose | pages [11] -->
51.099%

<!-- b003737 | furniture | pages [11] -->


<!-- b003738 | furniture | pages [11] -->


<!-- b003739 | prose | pages [11] -->
N X

<!-- b003740 | prose | pages [11] -->
yi −ˆyi

<!-- b003741 | prose | pages [11] -->
yi

<!-- b003742 | prose | pages [11] -->
i=1

<!-- b003743 | prose | pages [11] -->
The metrics in Table 5 indicate that the model controls absolute errors well, with an RMSE of 2.667 (average deviation of 2.7 medals). However, the high MAPE of 51.1% reveals challenges in accurately predicting countries with low medal counts, suggesting room for improvement.

<!-- b003744 | heading | pages [11] -->
Logistic Regression and Random Forest Prediction Model

<!-- b003745 | prose | pages [11] -->
6 for First-Time Medalist Countries

<!-- b003746 | prose | pages [11] -->
6.1

<!-- b003747 | heading | pages [11] -->
Reasons for Model Selection

<!-- b003748 | prose | pages [11] -->
Predicting the probability of countries winning their first Olympic medal is a complicated classification task. Logistic regression (LR) is a widely used model that excels in simplicity and

<!-- b003749 | prose | pages [11] -->
m

<!-- b003750 | prose | pages [11] -->
m

<!-- b003751 | prose | pages [11] -->
m

<!-- b003752 | prose | pages [11] -->
m

<!-- b003753 | prose | pages [11] -->
m

<!-- b003754 | prose | pages [11] -->
m

<!-- b003755 | prose | pages [11] -->
m

<!-- b003756 | prose | pages [11] -->
m

<!-- b003757 | prose | pages [11] -->
m

<!-- b003758 | prose | pages [11] -->
m

<!-- b003759 | prose | pages [11] -->
m

<!-- b003760 | prose | pages [11] -->
m

<!-- b003761 | prose | pages [11] -->
m

<!-- b003762 | prose | pages [11] -->
m

<!-- b003763 | prose | pages [11] -->
m

<!-- b003764 | prose | pages [11] -->
m

<!-- b003765 | prose | pages [11] -->
m

<!-- b003766 | prose | pages [11] -->
m

<!-- b003767 | prose | pages [11] -->
m

<!-- b003768 | prose | pages [11] -->
m

<!-- b003769 | prose | pages [11] -->
m

<!-- b003770 | prose | pages [11] -->
m

<!-- b003771 | prose | pages [11] -->
m

<!-- b003772 | prose | pages [11] -->
m

<!-- b003773 | prose | pages [11] -->
m

<!-- b003774 | prose | pages [11] -->
m

<!-- b003775 | prose | pages [11] -->
m

<!-- b003776 | prose | pages [11] -->
m

<!-- b003777 | prose | pages [11] -->
m

<!-- b003778 | prose | pages [11] -->
m

<!-- b003779 | prose | pages [11] -->
m

<!-- b003780 | prose | pages [11] -->
m

<!-- b003781 | prose | pages [11] -->
m

<!-- b003782 | prose | pages [11] -->
m

<!-- b003783 | prose | pages [11] -->
m

<!-- b003784 | prose | pages [11] -->
m

<!-- b003785 | prose | pages [11] -->
m

<!-- b003786 | prose | pages [11] -->
m

<!-- b003787 | prose | pages [11] -->
m

<!-- b003788 | prose | pages [11] -->
m

<!-- b003789 | prose | pages [11] -->
m

<!-- b003790 | prose | pages [11] -->
m

<!-- b003791 | prose | pages [11] -->
m

<!-- b003792 | prose | pages [11] -->
m

<!-- b003793 | prose | pages [11] -->
m

<!-- b003794 | prose | pages [11] -->
m

<!-- b003795 | prose | pages [11] -->
m

<!-- b003796 | prose | pages [11] -->
m

<!-- b003797 | prose | pages [11] -->
m

<!-- b003798 | prose | pages [11] -->
m

<!-- b003799 | prose | pages [11] -->
m

<!-- b003800 | prose | pages [11] -->
m

<!-- b003801 | prose | pages [11] -->
m

<!-- b003802 | prose | pages [11] -->
m

<!-- b003803 | prose | pages [11] -->
m

<!-- b003804 | prose | pages [11] -->
m

<!-- b003805 | prose | pages [11] -->
m

<!-- b003806 | prose | pages [11] -->
m

<!-- b003807 | prose | pages [11] -->
m

<!-- b003808 | prose | pages [11] -->
m

<!-- b003809 | prose | pages [11] -->
m

<!-- b003810 | prose | pages [11] -->
m

<!-- b003811 | prose | pages [11] -->
m

<!-- b003812 | prose | pages [11] -->
m

<!-- b003813 | prose | pages [11] -->
m

<!-- b003814 | prose | pages [11] -->
m

<!-- b003815 | prose | pages [11] -->
m

<!-- b003816 | prose | pages [11] -->
m

<!-- b003817 | prose | pages [11] -->
m

<!-- b003818 | prose | pages [11] -->
m

<!-- b003819 | prose | pages [11] -->
m

<!-- b003820 | prose | pages [11] -->
m

<!-- b003821 | prose | pages [11] -->
m

<!-- b003822 | prose | pages [11] -->
m

<!-- b003823 | prose | pages [11] -->
m

<!-- b003824 | prose | pages [11] -->
m

<!-- b003825 | prose | pages [11] -->
m

<!-- b003826 | prose | pages [11] -->
m

<!-- b003827 | prose | pages [11] -->
m

<!-- b003828 | prose | pages [11] -->
m

<!-- b003829 | prose | pages [11] -->
m

<!-- b003830 | prose | pages [11] -->
m

<!-- b003831 | prose | pages [11] -->
m

<!-- b003832 | prose | pages [11] -->
m

<!-- b003833 | prose | pages [11] -->
m

<!-- b003834 | prose | pages [11] -->
m

<!-- b003835 | prose | pages [11] -->
m

<!-- b003836 | prose | pages [11] -->
m

<!-- b003837 | prose | pages [11] -->
m

<!-- b003838 | prose | pages [11] -->
m

<!-- b003839 | prose | pages [11] -->
m

<!-- b003840 | prose | pages [11] -->
m

<!-- b003841 | prose | pages [11] -->
m

<!-- b003842 | prose | pages [11] -->
m

<!-- b003843 | prose | pages [11] -->
m

<!-- b003844 | prose | pages [11] -->
m

<!-- b003845 | prose | pages [11] -->
m

<!-- b003846 | prose | pages [11] -->
m

<!-- b003847 | prose | pages [11] -->
m

<!-- b003848 | prose | pages [11] -->
m

<!-- b003849 | prose | pages [11] -->
m

<!-- b003850 | prose | pages [11] -->
m

<!-- b003851 | prose | pages [11] -->
m

<!-- b003852 | prose | pages [11] -->
m

<!-- b003853 | prose | pages [11] -->
m

<!-- b003854 | prose | pages [11] -->
m

<!-- b003855 | prose | pages [11] -->
m

<!-- b003856 | prose | pages [11] -->
m

<!-- b003857 | prose | pages [11] -->
m

<!-- b003858 | prose | pages [11] -->
m

<!-- b003859 | prose | pages [11] -->
m

<!-- b003860 | prose | pages [11] -->
m

<!-- b003861 | prose | pages [11] -->
m

<!-- b003862 | prose | pages [11] -->
m

<!-- b003863 | prose | pages [11] -->
m

<!-- b003864 | prose | pages [11] -->
m

<!-- b003865 | prose | pages [11] -->
m

<!-- b003866 | prose | pages [11] -->
m

<!-- b003867 | prose | pages [11] -->
m

<!-- b003868 | prose | pages [11] -->
m

<!-- b003869 | prose | pages [11] -->
m

<!-- b003870 | prose | pages [11] -->
m

<!-- b003871 | prose | pages [11] -->
m

<!-- b003872 | prose | pages [11] -->
m

<!-- b003873 | prose | pages [11] -->
m

<!-- b003874 | prose | pages [11] -->
m

<!-- b003875 | prose | pages [11] -->
m

<!-- b003876 | prose | pages [11] -->
m

<!-- b003877 | prose | pages [11] -->
m

<!-- b003878 | prose | pages [11] -->
m

<!-- b003879 | prose | pages [11] -->
m

<!-- b003880 | prose | pages [11] -->
m

<!-- b003881 | prose | pages [11] -->
m

<!-- b003882 | prose | pages [11] -->
m

<!-- b003883 | prose | pages [11] -->
m

<!-- b003884 | prose | pages [11] -->
m

<!-- b003885 | prose | pages [11] -->
m

<!-- b003886 | prose | pages [11] -->
m

<!-- b003887 | prose | pages [11] -->
m

<!-- b003888 | prose | pages [11] -->
m

<!-- b003889 | prose | pages [11] -->
m

<!-- b003890 | prose | pages [11] -->
m

<!-- b003891 | prose | pages [11] -->
m

<!-- b003892 | prose | pages [11] -->
m

<!-- b003893 | prose | pages [11] -->
m

<!-- b003894 | prose | pages [11] -->
m

<!-- b003895 | prose | pages [11] -->
m

<!-- b003896 | prose | pages [11] -->
m

<!-- b003897 | prose | pages [11] -->
m

<!-- b003898 | prose | pages [11] -->
m

<!-- b003899 | prose | pages [11] -->
m

<!-- b003900 | prose | pages [11] -->
m

<!-- b003901 | prose | pages [11] -->
m

<!-- b003902 | prose | pages [11] -->
m

<!-- b003903 | prose | pages [11] -->
m

<!-- b003904 | prose | pages [11] -->
m

<!-- b003905 | prose | pages [11] -->
m

<!-- b003906 | prose | pages [11] -->
m

<!-- b003907 | prose | pages [11] -->
m

<!-- b003908 | prose | pages [11] -->
m

<!-- b003909 | prose | pages [11] -->
m

<!-- b003910 | prose | pages [11] -->
m

<!-- b003911 | prose | pages [11] -->
m

<!-- b003912 | prose | pages [11] -->
m

<!-- b003913 | prose | pages [11] -->
m

<!-- b003914 | prose | pages [11] -->
m

<!-- b003915 | prose | pages [11] -->
m

<!-- b003916 | prose | pages [11] -->
m

<!-- b003917 | prose | pages [11] -->
m

<!-- b003918 | prose | pages [11] -->
m

<!-- b003919 | prose | pages [11] -->
m

<!-- b003920 | prose | pages [11] -->
m

<!-- b003921 | prose | pages [11] -->
m

<!-- b003922 | prose | pages [11] -->
m

<!-- b003923 | prose | pages [11] -->
m

<!-- b003924 | prose | pages [11] -->
m

<!-- b003925 | prose | pages [11] -->
m

<!-- b003926 | prose | pages [11] -->
m

<!-- b003927 | prose | pages [11] -->
m

<!-- b003928 | prose | pages [11] -->
m

<!-- b003929 | prose | pages [11] -->
m

<!-- b003930 | prose | pages [11] -->
m

<!-- b003931 | prose | pages [11] -->
m

<!-- b003932 | prose | pages [11] -->
m

<!-- b003933 | prose | pages [11] -->
m

<!-- b003934 | prose | pages [11] -->
m

<!-- b003935 | prose | pages [11] -->
m

<!-- b003936 | prose | pages [11] -->
m

<!-- b003937 | prose | pages [11] -->
m

<!-- b003938 | prose | pages [11] -->
m

<!-- b003939 | prose | pages [11] -->
m

<!-- b003940 | prose | pages [11] -->
m

<!-- b003941 | prose | pages [11] -->
m

<!-- b003942 | prose | pages [11] -->
m

<!-- b003943 | prose | pages [11] -->
m

<!-- b003944 | prose | pages [11] -->
m

<!-- b003945 | prose | pages [11] -->
m

<!-- b003946 | prose | pages [11] -->
m

<!-- b003947 | prose | pages [11] -->
m

<!-- b003948 | prose | pages [11] -->
m

<!-- b003949 | prose | pages [11] -->
m

<!-- b003950 | prose | pages [11] -->
m

<!-- b003951 | prose | pages [11] -->
m

<!-- b003952 | prose | pages [11] -->
m

<!-- b003953 | prose | pages [11] -->
m

<!-- b003954 | prose | pages [11] -->
m

<!-- b003955 | prose | pages [11] -->
m

<!-- b003956 | prose | pages [11] -->
m

<!-- b003957 | prose | pages [11] -->
m

<!-- b003958 | prose | pages [11] -->
m

<!-- b003959 | prose | pages [11] -->
m

<!-- b003960 | prose | pages [11] -->
m

<!-- b003961 | prose | pages [11] -->
m

<!-- b003962 | prose | pages [11] -->
m

<!-- b003963 | prose | pages [11] -->
m

<!-- b003964 | prose | pages [11] -->
m

<!-- b003965 | prose | pages [11] -->
m

<!-- b003966 | prose | pages [11] -->
m

<!-- b003967 | prose | pages [11] -->
m

<!-- b003968 | prose | pages [11] -->
m

<!-- b003969 | prose | pages [11] -->
m

<!-- b003970 | prose | pages [11] -->
m

<!-- b003971 | prose | pages [11] -->
m

<!-- b003972 | prose | pages [11] -->
m

<!-- b003973 | prose | pages [11] -->
m

<!-- b003974 | prose | pages [11] -->
m

<!-- b003975 | prose | pages [11] -->
m

<!-- b003976 | prose | pages [11] -->
m

<!-- b003977 | prose | pages [11] -->
m

<!-- b003978 | prose | pages [11] -->
m

<!-- b003979 | prose | pages [11] -->
m

<!-- b003980 | prose | pages [11] -->
m

<!-- b003981 | prose | pages [11] -->
m

<!-- b003982 | prose | pages [11] -->
m

<!-- b003983 | prose | pages [11] -->
m

<!-- b003984 | prose | pages [11] -->
m

<!-- b003985 | prose | pages [11] -->
m

<!-- b003986 | prose | pages [11] -->
m

<!-- b003987 | prose | pages [11] -->
m

<!-- b003988 | prose | pages [11] -->
m

<!-- b003989 | prose | pages [11] -->
m

<!-- b003990 | prose | pages [11] -->
m

<!-- b003991 | prose | pages [11] -->
m

<!-- b003992 | prose | pages [11] -->
m

<!-- b003993 | prose | pages [11] -->
m

<!-- b003994 | prose | pages [11] -->
m

<!-- b003995 | prose | pages [11] -->
m

<!-- b003996 | prose | pages [11] -->
m

<!-- b003997 | prose | pages [11] -->
m

<!-- b003998 | prose | pages [11] -->
m

<!-- b003999 | prose | pages [11] -->
m

<!-- b004000 | prose | pages [11] -->
m

<!-- b004001 | prose | pages [11] -->
m

<!-- b004002 | prose | pages [11] -->
m

<!-- b004003 | prose | pages [11] -->
m

<!-- b004004 | prose | pages [11] -->
m

<!-- b004005 | prose | pages [11] -->
m

<!-- b004006 | prose | pages [11] -->
m

<!-- b004007 | prose | pages [11] -->
m

<!-- b004008 | prose | pages [11] -->
m

<!-- b004009 | prose | pages [11] -->
m

<!-- b004010 | prose | pages [11] -->
m

<!-- b004011 | prose | pages [11] -->
m

<!-- b004012 | prose | pages [11] -->
m

<!-- b004013 | prose | pages [11] -->
m

<!-- b004014 | prose | pages [11] -->
m

<!-- b004015 | prose | pages [11] -->
m

<!-- b004016 | prose | pages [11] -->
m

<!-- b004017 | prose | pages [11] -->
m

<!-- b004018 | prose | pages [11] -->
m

<!-- b004019 | prose | pages [11] -->
m

<!-- b004020 | prose | pages [11] -->
m

<!-- b004021 | prose | pages [11] -->
m

<!-- b004022 | prose | pages [11] -->
m

<!-- b004023 | prose | pages [11] -->
m

<!-- b004024 | prose | pages [11] -->
m

<!-- b004025 | prose | pages [11] -->
m

<!-- b004026 | prose | pages [11] -->
m

<!-- b004027 | prose | pages [11] -->
m

<!-- b004028 | prose | pages [11] -->
m

<!-- b004029 | prose | pages [11] -->
m

<!-- b004030 | prose | pages [11] -->
m

<!-- b004031 | prose | pages [11] -->
m

<!-- b004032 | prose | pages [11] -->
m

<!-- b004033 | furniture | pages [11] -->
m

<!-- b004034 | furniture | pages [11] -->
m

<!-- b004035 | furniture | pages [11] -->
m

<!-- b004036 | furniture | pages [11] -->
m

<!-- b004037 | furniture | pages [11] -->
m

<!-- b004038 | furniture | pages [11] -->
m

<!-- b004039 | furniture | pages [11] -->
m

<!-- b004040 | furniture | pages [11] -->
m

<!-- b004041 | furniture | pages [11] -->
m

<!-- b004042 | furniture | pages [11] -->
m

<!-- b004043 | furniture | pages [11] -->
m

<!-- b004044 | furniture | pages [11] -->
m

<!-- b004045 | furniture | pages [11] -->
m

<!-- b004046 | furniture | pages [11] -->
m

<!-- b004047 | furniture | pages [11] -->
m

<!-- b004048 | furniture | pages [11] -->
m

<!-- b004049 | furniture | pages [11] -->
m

<!-- b004050 | furniture | pages [11] -->
m

<!-- b004051 | furniture | pages [11] -->
m

<!-- b004052 | furniture | pages [11] -->
m

<!-- b004053 | furniture | pages [11] -->
m

<!-- b004054 | furniture | pages [11] -->
m

<!-- b004055 | furniture | pages [11] -->
m

<!-- b004056 | furniture | pages [11] -->
m

<!-- b004057 | furniture | pages [11] -->
m

<!-- b004058 | furniture | pages [11] -->
m

<!-- b004059 | furniture | pages [11] -->
m

<!-- b004060 | furniture | pages [11] -->
m

<!-- b004061 | furniture | pages [11] -->
m

<!-- b004062 | furniture | pages [11] -->
m

<!-- b004063 | furniture | pages [11] -->
m

<!-- b004064 | furniture | pages [11] -->
m

<!-- b004065 | furniture | pages [11] -->
m

<!-- b004066 | furniture | pages [11] -->
m

<!-- b004067 | furniture | pages [11] -->
m

<!-- b004068 | furniture | pages [11] -->
m

<!-- b004069 | furniture | pages [11] -->
m

<!-- b004070 | furniture | pages [11] -->
m

<!-- b004071 | furniture | pages [11] -->
m

<!-- b004072 | furniture | pages [11] -->
m

<!-- b004073 | furniture | pages [11] -->
m

<!-- b004074 | furniture | pages [11] -->
m

<!-- b004075 | furniture | pages [11] -->
m

<!-- b004076 | furniture | pages [11] -->
m

<!-- b004077 | furniture | pages [11] -->
m

<!-- b004078 | furniture | pages [11] -->
m

<!-- b004079 | furniture | pages [11] -->
m

<!-- b004080 | furniture | pages [11] -->
m

<!-- b004081 | furniture | pages [11] -->
m

<!-- b004082 | furniture | pages [11] -->
m

<!-- b004083 | furniture | pages [11] -->
m

<!-- b004084 | furniture | pages [11] -->
m

<!-- b004085 | furniture | pages [11] -->
m

<!-- b004086 | furniture | pages [11] -->
m

<!-- b004087 | furniture | pages [11] -->
m

<!-- b004088 | furniture | pages [11] -->
m

<!-- b004089 | furniture | pages [11] -->
m

<!-- b004090 | furniture | pages [11] -->
m

<!-- b004091 | furniture | pages [11] -->
m

<!-- b004092 | furniture | pages [11] -->
m

<!-- b004093 | furniture | pages [11] -->
m

<!-- b004094 | furniture | pages [11] -->
m

<!-- b004095 | furniture | pages [11] -->
m

<!-- b004096 | furniture | pages [11] -->
m

<!-- b004097 | furniture | pages [11] -->
m

<!-- b004098 | furniture | pages [11] -->
m

<!-- b004099 | furniture | pages [11] -->
m

<!-- b004100 | furniture | pages [11] -->
m

<!-- b004101 | furniture | pages [11] -->
m

<!-- b004102 | furniture | pages [11] -->
m

<!-- b004103 | furniture | pages [11] -->
m

<!-- b004104 | furniture | pages [11] -->
m

<!-- b004105 | furniture | pages [11] -->
m

<!-- b004106 | furniture | pages [11] -->
m

<!-- b004107 | furniture | pages [11] -->
m

<!-- b004108 | furniture | pages [11] -->
m

<!-- b004109 | furniture | pages [11] -->
m

<!-- b004110 | furniture | pages [11] -->
m

<!-- b004111 | furniture | pages [11] -->
m

<!-- b004112 | furniture | pages [11] -->
m

<!-- b004113 | furniture | pages [11] -->
m

<!-- b004114 | furniture | pages [11] -->
m

<!-- b004115 | furniture | pages [11] -->
m

<!-- b004116 | furniture | pages [11] -->
m

<!-- b004117 | furniture | pages [11] -->
m

<!-- b004118 | furniture | pages [11] -->
m

<!-- b004119 | furniture | pages [11] -->
m

<!-- b004120 | furniture | pages [11] -->
m

<!-- b004121 | furniture | pages [11] -->
m

<!-- b004122 | furniture | pages [11] -->
m

<!-- b004123 | furniture | pages [11] -->
m

<!-- b004124 | furniture | pages [11] -->
m

<!-- b004125 | furniture | pages [11] -->
m

<!-- b004126 | furniture | pages [11] -->
m

<!-- b004127 | furniture | pages [11] -->
m

<!-- b004128 | furniture | pages [11] -->
m

<!-- b004129 | furniture | pages [11] -->
m

<!-- b004130 | furniture | pages [11] -->
m

<!-- b004131 | furniture | pages [11] -->
m

<!-- b004132 | furniture | pages [11] -->
m

<!-- b004133 | furniture | pages [11] -->
m

<!-- b004134 | furniture | pages [11] -->
m

<!-- b004135 | furniture | pages [11] -->
m

<!-- b004136 | furniture | pages [11] -->
m

<!-- b004137 | furniture | pages [11] -->
m

<!-- b004138 | furniture | pages [11] -->
m

<!-- b004139 | furniture | pages [11] -->
m

<!-- b004140 | furniture | pages [11] -->
m

<!-- b004141 | furniture | pages [11] -->
m

<!-- b004142 | furniture | pages [11] -->
m

<!-- b004143 | furniture | pages [11] -->
m

<!-- b004144 | furniture | pages [11] -->
m

<!-- b004145 | furniture | pages [11] -->
m

<!-- b004146 | furniture | pages [11] -->
m

<!-- b004147 | furniture | pages [11] -->
m

<!-- b004148 | furniture | pages [11] -->
m

<!-- b004149 | furniture | pages [11] -->
m

<!-- b004150 | furniture | pages [11] -->
m

<!-- b004151 | furniture | pages [11] -->
m

<!-- b004152 | furniture | pages [11] -->
m

<!-- b004153 | furniture | pages [11] -->
m

<!-- b004154 | furniture | pages [11] -->
m

<!-- b004155 | furniture | pages [11] -->
m

<!-- b004156 | furniture | pages [11] -->
m

<!-- b004157 | furniture | pages [11] -->
m

<!-- b004158 | furniture | pages [11] -->
m

<!-- b004159 | furniture | pages [11] -->
m

<!-- b004160 | furniture | pages [11] -->
m

<!-- b004161 | furniture | pages [11] -->
m

<!-- b004162 | furniture | pages [11] -->
m

<!-- b004163 | furniture | pages [11] -->
m

<!-- b004164 | furniture | pages [11] -->
m

<!-- b004165 | furniture | pages [11] -->
m

<!-- b004166 | furniture | pages [11] -->
m

<!-- b004167 | furniture | pages [11] -->
m

<!-- b004168 | furniture | pages [11] -->
m

<!-- b004169 | furniture | pages [11] -->
m

<!-- b004170 | furniture | pages [11] -->
m

<!-- b004171 | furniture | pages [11] -->
m

<!-- b004172 | furniture | pages [11] -->
m

<!-- b004173 | furniture | pages [11] -->
m

<!-- b004174 | furniture | pages [11] -->
m

<!-- b004175 | furniture | pages [11] -->
m

<!-- b004176 | furniture | pages [11] -->
m

<!-- b004177 | furniture | pages [11] -->
m

<!-- b004178 | furniture | pages [11] -->
m

<!-- b004179 | furniture | pages [11] -->
m

<!-- b004180 | furniture | pages [11] -->
m

<!-- b004181 | furniture | pages [11] -->
m

<!-- b004182 | furniture | pages [11] -->
m

<!-- b004183 | furniture | pages [11] -->
m

<!-- b004184 | furniture | pages [11] -->
m

<!-- b004185 | furniture | pages [11] -->
m

<!-- b004186 | furniture | pages [11] -->
m

<!-- b004187 | furniture | pages [11] -->
m

<!-- b004188 | furniture | pages [11] -->
m

<!-- b004189 | furniture | pages [11] -->
m

<!-- b004190 | furniture | pages [11] -->
m

<!-- b004191 | furniture | pages [11] -->
m

<!-- b004192 | furniture | pages [11] -->
m

<!-- b004193 | furniture | pages [11] -->
m

<!-- b004194 | furniture | pages [11] -->
m

<!-- b004195 | furniture | pages [11] -->
m

<!-- b004196 | furniture | pages [11] -->
m

<!-- b004197 | furniture | pages [11] -->
m

<!-- b004198 | furniture | pages [11] -->
m

<!-- b004199 | furniture | pages [11] -->
m

<!-- b004200 | furniture | pages [11] -->
m

<!-- b004201 | furniture | pages [11] -->
m

<!-- b004202 | furniture | pages [11] -->
m

<!-- b004203 | furniture | pages [11] -->
m

<!-- b004204 | furniture | pages [11] -->
m

<!-- b004205 | furniture | pages [11] -->
m

<!-- b004206 | furniture | pages [11] -->
m

<!-- b004207 | furniture | pages [11] -->
m

<!-- b004208 | furniture | pages [11] -->
m

<!-- b004209 | furniture | pages [11] -->
m

<!-- b004210 | furniture | pages [11] -->
m

<!-- b004211 | furniture | pages [11] -->
m

<!-- b004212 | furniture | pages [11] -->
m

<!-- b004213 | furniture | pages [11] -->
m

<!-- b004214 | furniture | pages [11] -->
m

<!-- b004215 | furniture | pages [11] -->
m

<!-- b004216 | furniture | pages [11] -->
m

<!-- b004217 | furniture | pages [11] -->
m

<!-- b004218 | furniture | pages [11] -->
m

<!-- b004219 | furniture | pages [11] -->
m

<!-- b004220 | furniture | pages [11] -->
m

<!-- b004221 | furniture | pages [11] -->
m

<!-- b004222 | furniture | pages [11] -->
m

<!-- b004223 | furniture | pages [11] -->
m

<!-- b004224 | furniture | pages [11] -->
m

<!-- b004225 | furniture | pages [11] -->
m

<!-- b004226 | furniture | pages [11] -->
m

<!-- b004227 | furniture | pages [11] -->
m

<!-- b004228 | furniture | pages [11] -->
m

<!-- b004229 | furniture | pages [11] -->
m

<!-- b004230 | furniture | pages [11] -->
m

<!-- b004231 | furniture | pages [11] -->
m

<!-- b004232 | furniture | pages [11] -->
m

<!-- b004233 | furniture | pages [11] -->
m

<!-- b004234 | furniture | pages [11] -->
m

<!-- b004235 | furniture | pages [11] -->
m

<!-- b004236 | furniture | pages [11] -->
m

<!-- b004237 | furniture | pages [11] -->
m

<!-- b004238 | furniture | pages [11] -->
m

<!-- b004239 | furniture | pages [11] -->
m

<!-- b004240 | furniture | pages [11] -->
m

<!-- b004241 | furniture | pages [11] -->
m

<!-- b004242 | furniture | pages [11] -->
m

<!-- b004243 | furniture | pages [11] -->
m

<!-- b004244 | furniture | pages [11] -->
m

<!-- b004245 | furniture | pages [11] -->
m

<!-- b004246 | furniture | pages [11] -->
m

<!-- b004247 | furniture | pages [11] -->
m

<!-- b004248 | furniture | pages [11] -->
m

<!-- b004249 | furniture | pages [11] -->
m

<!-- b004250 | furniture | pages [11] -->
m

<!-- b004251 | furniture | pages [11] -->
m

<!-- b004252 | furniture | pages [11] -->
m

<!-- b004253 | furniture | pages [11] -->
m

<!-- b004254 | furniture | pages [11] -->
m

<!-- b004255 | furniture | pages [11] -->
m

<!-- b004256 | furniture | pages [11] -->
m

<!-- b004257 | furniture | pages [11] -->
m

<!-- b004258 | furniture | pages [11] -->
m

<!-- b004259 | furniture | pages [11] -->
m

<!-- b004260 | furniture | pages [11] -->
m

<!-- b004261 | furniture | pages [11] -->
m

<!-- b004262 | furniture | pages [11] -->
m

<!-- b004263 | furniture | pages [11] -->
m

<!-- b004264 | furniture | pages [11] -->
m

<!-- b004265 | furniture | pages [11] -->
m

<!-- b004266 | furniture | pages [11] -->
m

<!-- b004267 | furniture | pages [11] -->
m

<!-- b004268 | furniture | pages [11] -->
m

<!-- b004269 | furniture | pages [11] -->
m

<!-- b004270 | furniture | pages [11] -->
m

<!-- b004271 | furniture | pages [11] -->
m

<!-- b004272 | furniture | pages [11] -->
m

<!-- b004273 | furniture | pages [11] -->
m

<!-- b004274 | furniture | pages [11] -->
m

<!-- b004275 | furniture | pages [11] -->
m

<!-- b004276 | furniture | pages [11] -->
m

<!-- b004277 | furniture | pages [11] -->
m

<!-- b004278 | furniture | pages [11] -->
m

<!-- b004279 | furniture | pages [11] -->
m

<!-- b004280 | furniture | pages [11] -->
m

<!-- b004281 | furniture | pages [11] -->
m

<!-- b004282 | furniture | pages [11] -->
m

<!-- b004283 | furniture | pages [11] -->
m

<!-- b004284 | furniture | pages [11] -->
m

<!-- b004285 | furniture | pages [11] -->
m

<!-- b004286 | furniture | pages [11] -->
m

<!-- b004287 | furniture | pages [11] -->
m

<!-- b004288 | furniture | pages [11] -->
m

<!-- b004289 | furniture | pages [11] -->
m

<!-- b004290 | furniture | pages [11] -->
m

<!-- b004291 | furniture | pages [11] -->
m

<!-- b004292 | furniture | pages [11] -->
m

<!-- b004293 | furniture | pages [11] -->
m

<!-- b004294 | furniture | pages [11] -->
m

<!-- b004295 | furniture | pages [11] -->
m

<!-- b004296 | furniture | pages [11] -->
m

<!-- b004297 | furniture | pages [11] -->
m

<!-- b004298 | furniture | pages [11] -->
m

<!-- b004299 | furniture | pages [11] -->
m

<!-- b004300 | furniture | pages [11] -->
m

<!-- b004301 | furniture | pages [11] -->
m

<!-- b004302 | furniture | pages [11] -->
m

<!-- b004303 | furniture | pages [11] -->
m

<!-- b004304 | furniture | pages [11] -->
m

<!-- b004305 | furniture | pages [11] -->
m

<!-- b004306 | furniture | pages [11] -->
m

<!-- b004307 | furniture | pages [11] -->
m

<!-- b004308 | furniture | pages [11] -->
m

<!-- b004309 | furniture | pages [11] -->
m

<!-- b004310 | furniture | pages [11] -->
m

<!-- b004311 | furniture | pages [11] -->
m

<!-- b004312 | furniture | pages [11] -->
m

<!-- b004313 | furniture | pages [11] -->
m

<!-- b004314 | furniture | pages [11] -->
m

<!-- b004315 | furniture | pages [11] -->
m

<!-- b004316 | furniture | pages [11] -->
m

<!-- b004317 | furniture | pages [11] -->
m

<!-- b004318 | furniture | pages [11] -->
m

<!-- b004319 | furniture | pages [11] -->
m

<!-- b004320 | furniture | pages [11] -->
m

<!-- b004321 | furniture | pages [11] -->
m

<!-- b004322 | furniture | pages [11] -->
m

<!-- b004323 | furniture | pages [11] -->
m

<!-- b004324 | furniture | pages [11] -->
m

<!-- b004325 | furniture | pages [11] -->
m

<!-- b004326 | furniture | pages [11] -->
m

<!-- b004327 | furniture | pages [11] -->
m

<!-- b004328 | furniture | pages [11] -->
m

<!-- b004329 | furniture | pages [11] -->
m

<!-- b004330 | furniture | pages [11] -->
m

<!-- b004331 | furniture | pages [11] -->
m

<!-- b004332 | furniture | pages [11] -->
m

<!-- b004333 | furniture | pages [11] -->
m

<!-- b004334 | furniture | pages [11] -->
m

<!-- b004335 | furniture | pages [11] -->
m

<!-- b004336 | furniture | pages [11] -->
m

<!-- b004337 | furniture | pages [11] -->
m

<!-- b004338 | furniture | pages [11] -->
m

<!-- b004339 | furniture | pages [11] -->
m

<!-- b004340 | furniture | pages [11] -->
m

<!-- b004341 | furniture | pages [11] -->
m

<!-- b004342 | furniture | pages [11] -->
m

<!-- b004343 | furniture | pages [11] -->
m

<!-- b004344 | furniture | pages [11] -->
m

<!-- b004345 | furniture | pages [11] -->
m

<!-- b004346 | furniture | pages [11] -->
m

<!-- b004347 | furniture | pages [11] -->
m

<!-- b004348 | furniture | pages [11] -->
m

<!-- b004349 | furniture | pages [11] -->
m

<!-- b004350 | furniture | pages [11] -->
m

<!-- b004351 | furniture | pages [11] -->
m

<!-- b004352 | furniture | pages [11] -->
m

<!-- b004353 | furniture | pages [11] -->
m

<!-- b004354 | furniture | pages [11] -->
m

<!-- b004355 | furniture | pages [11] -->
m

<!-- b004356 | furniture | pages [11] -->
m

<!-- b004357 | furniture | pages [11] -->
m

<!-- b004358 | furniture | pages [11] -->
m

<!-- b004359 | furniture | pages [11] -->
m

<!-- b004360 | furniture | pages [11] -->
m

<!-- b004361 | furniture | pages [11] -->
m

<!-- b004362 | furniture | pages [11] -->
m

<!-- b004363 | furniture | pages [11] -->
m

<!-- b004364 | furniture | pages [11] -->
m

<!-- b004365 | furniture | pages [11] -->
m

<!-- b004366 | furniture | pages [11] -->
m

<!-- b004367 | furniture | pages [11] -->
m

<!-- b004368 | furniture | pages [11] -->
m

<!-- b004369 | furniture | pages [11] -->
m

<!-- b004370 | furniture | pages [11] -->
m

<!-- b004371 | furniture | pages [11] -->
m

<!-- b004372 | furniture | pages [11] -->
m

<!-- b004373 | furniture | pages [11] -->
m

<!-- b004374 | furniture | pages [11] -->
m

<!-- b004375 | furniture | pages [11] -->
m

<!-- b004376 | furniture | pages [11] -->
m

<!-- b004377 | furniture | pages [11] -->
m

<!-- b004378 | furniture | pages [11] -->
m

<!-- b004379 | furniture | pages [11] -->
m

<!-- b004380 | furniture | pages [11] -->
m

<!-- b004381 | furniture | pages [11] -->
m

<!-- b004382 | furniture | pages [11] -->
m

<!-- b004383 | furniture | pages [11] -->
m

<!-- b004384 | furniture | pages [11] -->
m

<!-- b004385 | furniture | pages [11] -->
m

<!-- b004386 | furniture | pages [11] -->
m

<!-- b004387 | furniture | pages [11] -->
m

<!-- b004388 | furniture | pages [11] -->
m

<!-- b004389 | furniture | pages [11] -->
m

<!-- b004390 | furniture | pages [11] -->
m

<!-- b004391 | furniture | pages [11] -->
m

<!-- b004392 | furniture | pages [11] -->
m

<!-- b004393 | furniture | pages [11] -->
m

<!-- b004394 | furniture | pages [11] -->
m

<!-- b004395 | furniture | pages [11] -->
m

<!-- b004396 | furniture | pages [11] -->
m

<!-- b004397 | furniture | pages [11] -->
m

<!-- b004398 | furniture | pages [11] -->
m

<!-- b004399 | furniture | pages [11] -->
m

<!-- b004400 | furniture | pages [11] -->
m

<!-- b004401 | furniture | pages [11] -->
m

<!-- b004402 | furniture | pages [11] -->
m

<!-- b004403 | furniture | pages [11] -->
m

<!-- b004404 | furniture | pages [11] -->
m

<!-- b004405 | furniture | pages [11] -->
m

<!-- b004406 | furniture | pages [11] -->
m

<!-- b004407 | furniture | pages [11] -->
m

<!-- b004408 | furniture | pages [11] -->
m

<!-- b004409 | furniture | pages [11] -->
m

<!-- b004410 | furniture | pages [11] -->
m

<!-- b004411 | furniture | pages [11] -->
m

<!-- b004412 | furniture | pages [11] -->
m

<!-- b004413 | furniture | pages [11] -->
m

<!-- b004414 | furniture | pages [11] -->
m

<!-- b004415 | furniture | pages [11] -->
m

<!-- b004416 | furniture | pages [11] -->
m

<!-- b004417 | furniture | pages [11] -->
m

<!-- b004418 | furniture | pages [11] -->
m

<!-- b004419 | furniture | pages [11] -->
m

<!-- b004420 | furniture | pages [11] -->
m

<!-- b004421 | furniture | pages [11] -->
m

<!-- b004422 | furniture | pages [11] -->
m

<!-- b004423 | furniture | pages [11] -->
m

<!-- b004424 | furniture | pages [11] -->
m

<!-- b004425 | furniture | pages [11] -->
m

<!-- b004426 | furniture | pages [11] -->
m

<!-- b004427 | furniture | pages [11] -->
m

<!-- b004428 | furniture | pages [11] -->
m

<!-- b004429 | furniture | pages [11] -->
m

<!-- b004430 | furniture | pages [11] -->
m

<!-- b004431 | furniture | pages [11] -->
m

<!-- b004432 | furniture | pages [11] -->
m

<!-- b004433 | furniture | pages [11] -->
m

<!-- b004434 | furniture | pages [11] -->
m

<!-- b004435 | furniture | pages [11] -->
m

<!-- b004436 | furniture | pages [12] -->
Team # 2503389

<!-- b004437 | furniture | pages [12] -->
Page 12 of 26

<!-- b004438 | prose | pages [12] -->
interpretability, effectively estimating probabilities when the relationships between predictors and outcomes are linear. However, it struggles with non-linear patterns and complex feature interactions that are often present in Olympic data, such as historical variability or regional effects.

<!-- b004439 | prose | pages [12] -->
To overcome these limitations, Random Forest (RF) offers a robust alternative. As an en- semble learning method, RF captures non-linear relationships and complex interactions while ranking feature importance, making it suitable for diverse datasets. However, RF can overfit and lacks the transparency of LR.

<!-- b004440 | prose | pages [12] -->
To leverage the strengths of both models, we adopted a hybrid approach that combines the interpretability of LR with the flexibility of RF. This strikes a balance between simplicity and robustness, allowing for more accurate and comprehensive predictions of which countries will win their first Olympic medal.

<!-- b004441 | prose | pages [12] -->
6.2 Feature Engineering

<!-- b004442 | prose | pages [12] -->
To identify countries that have never won medals, we process the table summerOly_athletes.csv to identify athletes who have won medals, then filter the countries they represented in the com- petition. From the list of all countries, we exclude those that have won at least one medal.

<!-- b004443 | prose | pages [12] -->
The core principal here is to simplify the process by counting only unique countries, so duplicates are considered only once.

<!-- b004444 | prose | pages [12] -->
This results in a list of countries that have never won a medal, along with features:

<!-- b004445 | prose | pages [12] -->
• Number of Programs Attended. Count the total number of programs attended by these countries.

<!-- b004446 | prose | pages [12] -->
• Athlete Participation Experience. Calculate the average number of sessions an athlete has participated in.

<!-- b004447 | prose | pages [12] -->
• Program Competition Intensity. Calculate the formula:

<!-- b004448 | prose | pages [12] -->
1 −Number of Medals in the Program , Number of Participants

<!-- b004449 | prose | pages [12] -->
where a value closer to 1 indicates more intense competition.

<!-- b004450 | prose | pages [12] -->
Analysis of Conditions for Countries Winning Medals for the First 6.3 Time

<!-- b004451 | prose | pages [12] -->
We calculate the number of countries that won medals for the first time in each Olympic Games (e.g. 5 countries in the 2020 Tokyo Olympics and 3 countries in the 2016 Rio Olympics) and also analyze the distribution of these countries based on features, including statistics like the mean, variance, and trends.

<!-- b004452 | prose | pages [12] -->
关注数学模型

<!-- b004453 | furniture | pages [12] -->
2

<!-- b004454 | furniture | pages [12] -->
MATHmodels

<!-- b004455 | furniture | pages [12] -->
获取更多资讯

<!-- b004456 | furniture | pages [13] -->
Team # 2503389

<!-- b004457 | caption | pages [13] -->
Figure 7: Mean and Variance

<!-- b004458 | furniture | pages [13] -->
Page 13 of 26

<!-- b004459 | caption | pages [13] -->
Figure 8: The number of First-

<!-- b004460 | prose | pages [13] -->
time Medalist Countries

<!-- b004461 | prose | pages [13] -->
微信公众号：数学模型

<!-- b004462 | prose | pages [13] -->
As shown in Figure 7 and 8, there is a notable fluctuation in the number of first-time medal- winning countries across different Olympic years. For instance, in the 2020 Tokyo Olympics, 5 countries won their first-ever medals, while in 2016, there were only 3 such countries.

<!-- b004463 | heading | pages [13] -->
Model Formulation and Prediction Results

<!-- b004464 | prose | pages [13] -->
6.4

<!-- b004465 | prose | pages [13] -->
We utilized two predictive models—Logistic Regression and Random Forest—to estimate the likelihood of countries earning their first medal in the next Olympics.

<!-- b004466 | prose | pages [13] -->
微信号：MATHmodels

<!-- b004467 | prose | pages [13] -->
6.4.1

<!-- b004468 | heading | pages [13] -->
Logistic Regression Model

<!-- b004469 | prose | pages [13] -->
The Logistic Regression model predicts the probability of a country earning a medal for the first time based on key features. The model is given by:

<!-- b004470 | prose | pages [13] -->
P(Target = 1|X) = 1 1 + e−(β0+β1·Experience+β2·Programs Attended+β3·Competition Intensity),

<!-- b004471 | prose | pages [13] -->
where P(Target = 1|X) is the probability of earning a first medal, and β0, β1, β2, β3 are the model coefficients for each feature (Experience, Programs Attended, and Competition Inten- sity).

<!-- b004472 | prose | pages [13] -->
6.4.2

<!-- b004473 | heading | pages [13] -->
Random Forest Model

<!-- b004474 | prose | pages [13] -->
The Random Forest model aggregates the predictions of multiple decision trees. The final pre- diction is the average of all tree predictions:

<!-- b004475 | prose | pages [13] -->
ˆy = 1

<!-- b004476 | prose | pages [13] -->
N

<!-- b004477 | prose | pages [13] -->
N X

<!-- b004478 | prose | pages [13] -->
ˆyi

<!-- b004479 | prose | pages [13] -->
i=1

<!-- b004480 | prose | pages [13] -->
where ˆy is the predicted probability, N is the number of trees, and ˆyi is the prediction of the i-th tree.

<!-- b004481 | prose | pages [13] -->
6.4.3

<!-- b004482 | heading | pages [13] -->
Prediction Results

<!-- b004483 | prose | pages [13] -->
The prediction results from the two models are as follows:

<!-- b004484 | prose | pages [13] -->
• Logistic Regression Prediction: Angola, El Salvador, Papua New Guinea

<!-- b004485 | prose | pages [13] -->
• Random Forest Prediction: Angola

<!-- b004486 | furniture | pages [14] -->
Team # 2503389

<!-- b004487 | furniture | pages [14] -->
Page 14 of 26

<!-- b004488 | prose | pages [14] -->
We then utilized the Poisson binomial distribution combined with Monte Carlo simulations to estimate the expected number of countries likely to win their first Olympic medal and their confidence intervals. The simulation results, shown in Figure 9, indicate that the probability is highest when the number of first-time medal-winning countries is exactly 3.

<!-- b004489 | caption | pages [14] -->
Figure 9: Monte Carlo Simulation of First-Time Medal-Winning Countries

<!-- b004490 | prose | pages [14] -->
Based on these findings, we conclude that 3 countries are the most likely to win their first Olympic medal in the next Games.The simulation results align well with our predictions, con- firming the robustness of the model’s estimates. The Monte Carlo simulation not only validated the expected outcomes but also provided a probabilistic range for the number of countries likely to win their first medal in the next Olympics.

<!-- b004491 | prose | pages [14] -->
These predictions reflect the model’s output probabilities, with Angola appearing as a com-

<!-- b004492 | prose | pages [14] -->
m

<!-- b004493 | prose | pages [14] -->
m

<!-- b004494 | prose | pages [14] -->
m

<!-- b004495 | prose | pages [14] -->
m

<!-- b004496 | prose | pages [14] -->
m

<!-- b004497 | prose | pages [14] -->
m

<!-- b004498 | prose | pages [14] -->
m

<!-- b004499 | prose | pages [14] -->
m

<!-- b004500 | prose | pages [14] -->
m

<!-- b004501 | prose | pages [14] -->
m

<!-- b004502 | prose | pages [14] -->
m

<!-- b004503 | prose | pages [14] -->
m

<!-- b004504 | prose | pages [14] -->
m

<!-- b004505 | prose | pages [14] -->
m

<!-- b004506 | prose | pages [14] -->
m

<!-- b004507 | prose | pages [14] -->
m

<!-- b004508 | prose | pages [14] -->
m

<!-- b004509 | prose | pages [14] -->
m

<!-- b004510 | prose | pages [14] -->
m

<!-- b004511 | prose | pages [14] -->
m

<!-- b004512 | prose | pages [14] -->
m

<!-- b004513 | prose | pages [14] -->
m

<!-- b004514 | prose | pages [14] -->
mon prediction in both models, suggesting a strong likelihood of this country earning its first

<!-- b004515 | prose | pages [14] -->
m

<!-- b004516 | prose | pages [14] -->
m

<!-- b004517 | prose | pages [14] -->
m

<!-- b004518 | prose | pages [14] -->
m

<!-- b004519 | prose | pages [14] -->
m

<!-- b004520 | prose | pages [14] -->
m

<!-- b004521 | prose | pages [14] -->
m

<!-- b004522 | prose | pages [14] -->
m

<!-- b004523 | prose | pages [14] -->
m

<!-- b004524 | prose | pages [14] -->
m

<!-- b004525 | prose | pages [14] -->
m

<!-- b004526 | prose | pages [14] -->
m

<!-- b004527 | prose | pages [14] -->
m

<!-- b004528 | prose | pages [14] -->
m

<!-- b004529 | prose | pages [14] -->
m

<!-- b004530 | prose | pages [14] -->
m

<!-- b004531 | prose | pages [14] -->
m

<!-- b004532 | prose | pages [14] -->
m

<!-- b004533 | prose | pages [14] -->
m

<!-- b004534 | prose | pages [14] -->
m

<!-- b004535 | prose | pages [14] -->
m

<!-- b004536 | prose | pages [14] -->
m

<!-- b004537 | prose | pages [14] -->
m

<!-- b004538 | prose | pages [14] -->
m

<!-- b004539 | prose | pages [14] -->
m

<!-- b004540 | prose | pages [14] -->
m

<!-- b004541 | prose | pages [14] -->
m

<!-- b004542 | prose | pages [14] -->
m

<!-- b004543 | prose | pages [14] -->
m

<!-- b004544 | prose | pages [14] -->
m

<!-- b004545 | prose | pages [14] -->
m

<!-- b004546 | prose | pages [14] -->
m

<!-- b004547 | prose | pages [14] -->
m

<!-- b004548 | prose | pages [14] -->
m

<!-- b004549 | prose | pages [14] -->
m

<!-- b004550 | prose | pages [14] -->
m

<!-- b004551 | prose | pages [14] -->
m

<!-- b004552 | prose | pages [14] -->
m

<!-- b004553 | prose | pages [14] -->
m

<!-- b004554 | prose | pages [14] -->
m

<!-- b004555 | prose | pages [14] -->
m

<!-- b004556 | prose | pages [14] -->
m

<!-- b004557 | prose | pages [14] -->
m

<!-- b004558 | prose | pages [14] -->
m

<!-- b004559 | prose | pages [14] -->
m

<!-- b004560 | prose | pages [14] -->
m

<!-- b004561 | prose | pages [14] -->
m

<!-- b004562 | prose | pages [14] -->
m

<!-- b004563 | prose | pages [14] -->
m

<!-- b004564 | prose | pages [14] -->
m

<!-- b004565 | prose | pages [14] -->
m

<!-- b004566 | prose | pages [14] -->
m

<!-- b004567 | prose | pages [14] -->
m

<!-- b004568 | prose | pages [14] -->
m

<!-- b004569 | prose | pages [14] -->
m

<!-- b004570 | prose | pages [14] -->
m

<!-- b004571 | prose | pages [14] -->
m

<!-- b004572 | prose | pages [14] -->
m

<!-- b004573 | prose | pages [14] -->
m

<!-- b004574 | prose | pages [14] -->
m

<!-- b004575 | prose | pages [14] -->
m

<!-- b004576 | prose | pages [14] -->
m

<!-- b004577 | prose | pages [14] -->
m

<!-- b004578 | prose | pages [14] -->
m

<!-- b004579 | prose | pages [14] -->
m

<!-- b004580 | prose | pages [14] -->
m

<!-- b004581 | prose | pages [14] -->
m

<!-- b004582 | prose | pages [14] -->
m

<!-- b004583 | prose | pages [14] -->
m

<!-- b004584 | prose | pages [14] -->
m

<!-- b004585 | prose | pages [14] -->
m

<!-- b004586 | prose | pages [14] -->
m

<!-- b004587 | prose | pages [14] -->
m

<!-- b004588 | prose | pages [14] -->
m

<!-- b004589 | prose | pages [14] -->
m

<!-- b004590 | prose | pages [14] -->
m

<!-- b004591 | prose | pages [14] -->
m

<!-- b004592 | prose | pages [14] -->
m

<!-- b004593 | prose | pages [14] -->
m

<!-- b004594 | prose | pages [14] -->
m

<!-- b004595 | prose | pages [14] -->
m

<!-- b004596 | prose | pages [14] -->
m

<!-- b004597 | prose | pages [14] -->
m

<!-- b004598 | prose | pages [14] -->
m

<!-- b004599 | prose | pages [14] -->
m

<!-- b004600 | prose | pages [14] -->
m

<!-- b004601 | prose | pages [14] -->
m

<!-- b004602 | prose | pages [14] -->
m

<!-- b004603 | prose | pages [14] -->
m

<!-- b004604 | prose | pages [14] -->
m

<!-- b004605 | prose | pages [14] -->
m

<!-- b004606 | prose | pages [14] -->
m

<!-- b004607 | prose | pages [14] -->
m

<!-- b004608 | prose | pages [14] -->
m

<!-- b004609 | prose | pages [14] -->
m

<!-- b004610 | prose | pages [14] -->
m

<!-- b004611 | prose | pages [14] -->
m

<!-- b004612 | prose | pages [14] -->
m

<!-- b004613 | prose | pages [14] -->
m

<!-- b004614 | prose | pages [14] -->
m

<!-- b004615 | prose | pages [14] -->
m

<!-- b004616 | prose | pages [14] -->
m

<!-- b004617 | prose | pages [14] -->
m

<!-- b004618 | prose | pages [14] -->
m

<!-- b004619 | prose | pages [14] -->
m

<!-- b004620 | prose | pages [14] -->
m

<!-- b004621 | prose | pages [14] -->
m

<!-- b004622 | prose | pages [14] -->
m

<!-- b004623 | prose | pages [14] -->
m

<!-- b004624 | prose | pages [14] -->
m

<!-- b004625 | prose | pages [14] -->
m

<!-- b004626 | prose | pages [14] -->
m

<!-- b004627 | prose | pages [14] -->
m

<!-- b004628 | prose | pages [14] -->
m

<!-- b004629 | prose | pages [14] -->
m

<!-- b004630 | prose | pages [14] -->
m

<!-- b004631 | prose | pages [14] -->
m

<!-- b004632 | prose | pages [14] -->
m

<!-- b004633 | prose | pages [14] -->
m

<!-- b004634 | prose | pages [14] -->
m

<!-- b004635 | prose | pages [14] -->
m

<!-- b004636 | prose | pages [14] -->
m

<!-- b004637 | prose | pages [14] -->
m

<!-- b004638 | prose | pages [14] -->
m

<!-- b004639 | prose | pages [14] -->
m

<!-- b004640 | prose | pages [14] -->
m

<!-- b004641 | prose | pages [14] -->
m

<!-- b004642 | prose | pages [14] -->
m

<!-- b004643 | prose | pages [14] -->
m

<!-- b004644 | prose | pages [14] -->
m

<!-- b004645 | prose | pages [14] -->
m

<!-- b004646 | prose | pages [14] -->
m

<!-- b004647 | prose | pages [14] -->
m

<!-- b004648 | prose | pages [14] -->
m

<!-- b004649 | prose | pages [14] -->
m

<!-- b004650 | prose | pages [14] -->
m

<!-- b004651 | prose | pages [14] -->
m

<!-- b004652 | prose | pages [14] -->
m

<!-- b004653 | prose | pages [14] -->
m

<!-- b004654 | prose | pages [14] -->
m

<!-- b004655 | prose | pages [14] -->
m

<!-- b004656 | prose | pages [14] -->
m

<!-- b004657 | prose | pages [14] -->
m

<!-- b004658 | prose | pages [14] -->
m

<!-- b004659 | prose | pages [14] -->
m

<!-- b004660 | prose | pages [14] -->
medal.

<!-- b004661 | prose | pages [14] -->
m

<!-- b004662 | prose | pages [14] -->
m

<!-- b004663 | prose | pages [14] -->
m

<!-- b004664 | prose | pages [14] -->
m

<!-- b004665 | prose | pages [14] -->
m

<!-- b004666 | prose | pages [14] -->
m

<!-- b004667 | prose | pages [14] -->
m

<!-- b004668 | prose | pages [14] -->
m

<!-- b004669 | prose | pages [14] -->
m

<!-- b004670 | prose | pages [14] -->
m

<!-- b004671 | prose | pages [14] -->
m

<!-- b004672 | prose | pages [14] -->
m

<!-- b004673 | prose | pages [14] -->
m

<!-- b004674 | prose | pages [14] -->
m

<!-- b004675 | prose | pages [14] -->
m

<!-- b004676 | prose | pages [14] -->
m

<!-- b004677 | prose | pages [14] -->
m

<!-- b004678 | prose | pages [14] -->
m

<!-- b004679 | prose | pages [14] -->
m

<!-- b004680 | prose | pages [14] -->
m

<!-- b004681 | prose | pages [14] -->
m

<!-- b004682 | prose | pages [14] -->
m

<!-- b004683 | prose | pages [14] -->
m

<!-- b004684 | prose | pages [14] -->
m

<!-- b004685 | prose | pages [14] -->
m

<!-- b004686 | prose | pages [14] -->
m

<!-- b004687 | prose | pages [14] -->
m

<!-- b004688 | prose | pages [14] -->
m

<!-- b004689 | prose | pages [14] -->
m

<!-- b004690 | prose | pages [14] -->
m

<!-- b004691 | prose | pages [14] -->
m

<!-- b004692 | prose | pages [14] -->
m

<!-- b004693 | prose | pages [14] -->
m

<!-- b004694 | prose | pages [14] -->
m

<!-- b004695 | prose | pages [14] -->
m

<!-- b004696 | prose | pages [14] -->
m

<!-- b004697 | prose | pages [14] -->
m

<!-- b004698 | prose | pages [14] -->
m

<!-- b004699 | prose | pages [14] -->
m

<!-- b004700 | prose | pages [14] -->
m

<!-- b004701 | prose | pages [14] -->
m

<!-- b004702 | prose | pages [14] -->
m

<!-- b004703 | prose | pages [14] -->
m

<!-- b004704 | prose | pages [14] -->
m

<!-- b004705 | prose | pages [14] -->
m

<!-- b004706 | prose | pages [14] -->
m

<!-- b004707 | prose | pages [14] -->
m

<!-- b004708 | prose | pages [14] -->
m

<!-- b004709 | prose | pages [14] -->
m

<!-- b004710 | prose | pages [14] -->
m

<!-- b004711 | prose | pages [14] -->
m

<!-- b004712 | prose | pages [14] -->
m

<!-- b004713 | prose | pages [14] -->
m

<!-- b004714 | prose | pages [14] -->
m

<!-- b004715 | prose | pages [14] -->
m

<!-- b004716 | prose | pages [14] -->
m

<!-- b004717 | prose | pages [14] -->
m

<!-- b004718 | prose | pages [14] -->
m

<!-- b004719 | prose | pages [14] -->
m

<!-- b004720 | prose | pages [14] -->
m

<!-- b004721 | prose | pages [14] -->
m

<!-- b004722 | prose | pages [14] -->
m

<!-- b004723 | prose | pages [14] -->
m

<!-- b004724 | prose | pages [14] -->
m

<!-- b004725 | prose | pages [14] -->
m

<!-- b004726 | prose | pages [14] -->
m

<!-- b004727 | prose | pages [14] -->
m

<!-- b004728 | prose | pages [14] -->
m

<!-- b004729 | prose | pages [14] -->
m

<!-- b004730 | prose | pages [14] -->
m

<!-- b004731 | prose | pages [14] -->
m

<!-- b004732 | prose | pages [14] -->
m

<!-- b004733 | prose | pages [14] -->
m

<!-- b004734 | prose | pages [14] -->
m

<!-- b004735 | prose | pages [14] -->
m

<!-- b004736 | prose | pages [14] -->
m

<!-- b004737 | prose | pages [14] -->
m

<!-- b004738 | prose | pages [14] -->
m

<!-- b004739 | prose | pages [14] -->
m

<!-- b004740 | prose | pages [14] -->
m

<!-- b004741 | prose | pages [14] -->
m

<!-- b004742 | prose | pages [14] -->
m

<!-- b004743 | prose | pages [14] -->
m

<!-- b004744 | prose | pages [14] -->
m

<!-- b004745 | prose | pages [14] -->
m

<!-- b004746 | prose | pages [14] -->
m

<!-- b004747 | prose | pages [14] -->
m

<!-- b004748 | prose | pages [14] -->
m

<!-- b004749 | prose | pages [14] -->
m

<!-- b004750 | prose | pages [14] -->
m

<!-- b004751 | prose | pages [14] -->
m

<!-- b004752 | prose | pages [14] -->
m

<!-- b004753 | prose | pages [14] -->
m

<!-- b004754 | prose | pages [14] -->
m

<!-- b004755 | prose | pages [14] -->
m

<!-- b004756 | prose | pages [14] -->
m

<!-- b004757 | prose | pages [14] -->
m

<!-- b004758 | prose | pages [14] -->
m

<!-- b004759 | prose | pages [14] -->
m

<!-- b004760 | prose | pages [14] -->
m

<!-- b004761 | prose | pages [14] -->
m

<!-- b004762 | prose | pages [14] -->
m

<!-- b004763 | prose | pages [14] -->
m

<!-- b004764 | prose | pages [14] -->
m

<!-- b004765 | prose | pages [14] -->
m

<!-- b004766 | prose | pages [14] -->
m

<!-- b004767 | prose | pages [14] -->
m

<!-- b004768 | prose | pages [14] -->
m

<!-- b004769 | prose | pages [14] -->
m

<!-- b004770 | prose | pages [14] -->
m

<!-- b004771 | prose | pages [14] -->
m

<!-- b004772 | prose | pages [14] -->
m

<!-- b004773 | prose | pages [14] -->
m

<!-- b004774 | prose | pages [14] -->
m

<!-- b004775 | prose | pages [14] -->
m

<!-- b004776 | prose | pages [14] -->
m

<!-- b004777 | prose | pages [14] -->
m

<!-- b004778 | prose | pages [14] -->
m

<!-- b004779 | prose | pages [14] -->
m

<!-- b004780 | prose | pages [14] -->
m

<!-- b004781 | prose | pages [14] -->
m

<!-- b004782 | prose | pages [14] -->
m

<!-- b004783 | prose | pages [14] -->
m

<!-- b004784 | prose | pages [14] -->
m

<!-- b004785 | prose | pages [14] -->
m

<!-- b004786 | prose | pages [14] -->
m

<!-- b004787 | prose | pages [14] -->
m

<!-- b004788 | prose | pages [14] -->
m

<!-- b004789 | prose | pages [14] -->
m

<!-- b004790 | prose | pages [14] -->
m

<!-- b004791 | prose | pages [14] -->
m

<!-- b004792 | prose | pages [14] -->
m

<!-- b004793 | prose | pages [14] -->
m

<!-- b004794 | prose | pages [14] -->
m

<!-- b004795 | prose | pages [14] -->
m

<!-- b004796 | prose | pages [14] -->
m

<!-- b004797 | prose | pages [14] -->
m

<!-- b004798 | prose | pages [14] -->
m

<!-- b004799 | prose | pages [14] -->
m

<!-- b004800 | prose | pages [14] -->
m

<!-- b004801 | prose | pages [14] -->
m

<!-- b004802 | prose | pages [14] -->
m

<!-- b004803 | prose | pages [14] -->
m

<!-- b004804 | prose | pages [14] -->
m

<!-- b004805 | prose | pages [14] -->
m

<!-- b004806 | prose | pages [14] -->
m

<!-- b004807 | prose | pages [14] -->
m

<!-- b004808 | prose | pages [14] -->
m

<!-- b004809 | prose | pages [14] -->
m

<!-- b004810 | prose | pages [14] -->
m

<!-- b004811 | prose | pages [14] -->
m

<!-- b004812 | prose | pages [14] -->
m

<!-- b004813 | prose | pages [14] -->
m

<!-- b004814 | prose | pages [14] -->
m

<!-- b004815 | prose | pages [14] -->
m

<!-- b004816 | prose | pages [14] -->
m

<!-- b004817 | prose | pages [14] -->
m

<!-- b004818 | prose | pages [14] -->
m

<!-- b004819 | prose | pages [14] -->
m

<!-- b004820 | prose | pages [14] -->
m

<!-- b004821 | prose | pages [14] -->
m

<!-- b004822 | prose | pages [14] -->
m

<!-- b004823 | prose | pages [14] -->
m

<!-- b004824 | prose | pages [14] -->
m

<!-- b004825 | prose | pages [14] -->
m

<!-- b004826 | prose | pages [14] -->
m

<!-- b004827 | prose | pages [14] -->
m

<!-- b004828 | prose | pages [14] -->
m

<!-- b004829 | prose | pages [14] -->
m

<!-- b004830 | prose | pages [14] -->
m

<!-- b004831 | prose | pages [14] -->
m

<!-- b004832 | prose | pages [14] -->
m

<!-- b004833 | prose | pages [14] -->
m

<!-- b004834 | prose | pages [14] -->
m

<!-- b004835 | prose | pages [14] -->
m

<!-- b004836 | prose | pages [14] -->
m

<!-- b004837 | prose | pages [14] -->
m

<!-- b004838 | prose | pages [14] -->
m

<!-- b004839 | prose | pages [14] -->
m

<!-- b004840 | prose | pages [14] -->
m

<!-- b004841 | prose | pages [14] -->
m

<!-- b004842 | prose | pages [14] -->
m

<!-- b004843 | prose | pages [14] -->
m

<!-- b004844 | prose | pages [14] -->
m

<!-- b004845 | prose | pages [14] -->
m

<!-- b004846 | prose | pages [14] -->
m

<!-- b004847 | prose | pages [14] -->
m

<!-- b004848 | prose | pages [14] -->
m

<!-- b004849 | prose | pages [14] -->
m

<!-- b004850 | prose | pages [14] -->
m

<!-- b004851 | prose | pages [14] -->
m

<!-- b004852 | prose | pages [14] -->
m

<!-- b004853 | prose | pages [14] -->
m

<!-- b004854 | prose | pages [14] -->
m

<!-- b004855 | prose | pages [14] -->
m

<!-- b004856 | prose | pages [14] -->
m

<!-- b004857 | prose | pages [14] -->
m

<!-- b004858 | prose | pages [14] -->
m

<!-- b004859 | prose | pages [14] -->
m

<!-- b004860 | prose | pages [14] -->
m

<!-- b004861 | prose | pages [14] -->
m

<!-- b004862 | prose | pages [14] -->
m

<!-- b004863 | prose | pages [14] -->
m

<!-- b004864 | prose | pages [14] -->
m

<!-- b004865 | prose | pages [14] -->
m

<!-- b004866 | prose | pages [14] -->
m

<!-- b004867 | prose | pages [14] -->
m

<!-- b004868 | prose | pages [14] -->
m

<!-- b004869 | prose | pages [14] -->
m

<!-- b004870 | prose | pages [14] -->
m

<!-- b004871 | prose | pages [14] -->
m

<!-- b004872 | prose | pages [14] -->
m

<!-- b004873 | prose | pages [14] -->
m

<!-- b004874 | prose | pages [14] -->
m

<!-- b004875 | prose | pages [14] -->
m

<!-- b004876 | prose | pages [14] -->
m

<!-- b004877 | prose | pages [14] -->
m

<!-- b004878 | prose | pages [14] -->
m

<!-- b004879 | prose | pages [14] -->
m

<!-- b004880 | prose | pages [14] -->
m

<!-- b004881 | prose | pages [14] -->
6.5 Estimate odds

<!-- b004882 | prose | pages [14] -->
m

<!-- b004883 | prose | pages [14] -->
m

<!-- b004884 | prose | pages [14] -->
m

<!-- b004885 | prose | pages [14] -->
m

<!-- b004886 | prose | pages [14] -->
m

<!-- b004887 | prose | pages [14] -->
m

<!-- b004888 | prose | pages [14] -->
m

<!-- b004889 | prose | pages [14] -->
m

<!-- b004890 | prose | pages [14] -->
m

<!-- b004891 | prose | pages [14] -->
m

<!-- b004892 | prose | pages [14] -->
m

<!-- b004893 | prose | pages [14] -->
m

<!-- b004894 | prose | pages [14] -->
m

<!-- b004895 | prose | pages [14] -->
m

<!-- b004896 | prose | pages [14] -->
m

<!-- b004897 | prose | pages [14] -->
m

<!-- b004898 | prose | pages [14] -->
m

<!-- b004899 | prose | pages [14] -->
m

<!-- b004900 | prose | pages [14] -->
m

<!-- b004901 | prose | pages [14] -->
m

<!-- b004902 | prose | pages [14] -->
m

<!-- b004903 | prose | pages [14] -->
m

<!-- b004904 | prose | pages [14] -->
m

<!-- b004905 | prose | pages [14] -->
m

<!-- b004906 | prose | pages [14] -->
m

<!-- b004907 | prose | pages [14] -->
m

<!-- b004908 | prose | pages [14] -->
m

<!-- b004909 | prose | pages [14] -->
m

<!-- b004910 | prose | pages [14] -->
m

<!-- b004911 | prose | pages [14] -->
m

<!-- b004912 | prose | pages [14] -->
m

<!-- b004913 | prose | pages [14] -->
m

<!-- b004914 | prose | pages [14] -->
m

<!-- b004915 | prose | pages [14] -->
m

<!-- b004916 | prose | pages [14] -->
m

<!-- b004917 | prose | pages [14] -->
m

<!-- b004918 | prose | pages [14] -->
m

<!-- b004919 | prose | pages [14] -->
m

<!-- b004920 | prose | pages [14] -->
m

<!-- b004921 | prose | pages [14] -->
m

<!-- b004922 | prose | pages [14] -->
m

<!-- b004923 | prose | pages [14] -->
m

<!-- b004924 | prose | pages [14] -->
m

<!-- b004925 | prose | pages [14] -->
m

<!-- b004926 | prose | pages [14] -->
m

<!-- b004927 | prose | pages [14] -->
m

<!-- b004928 | prose | pages [14] -->
m

<!-- b004929 | prose | pages [14] -->
m

<!-- b004930 | prose | pages [14] -->
m

<!-- b004931 | prose | pages [14] -->
m

<!-- b004932 | prose | pages [14] -->
m

<!-- b004933 | prose | pages [14] -->
m

<!-- b004934 | prose | pages [14] -->
m

<!-- b004935 | prose | pages [14] -->
m

<!-- b004936 | prose | pages [14] -->
m

<!-- b004937 | prose | pages [14] -->
m

<!-- b004938 | prose | pages [14] -->
m

<!-- b004939 | prose | pages [14] -->
m

<!-- b004940 | prose | pages [14] -->
m

<!-- b004941 | prose | pages [14] -->
m

<!-- b004942 | prose | pages [14] -->
m

<!-- b004943 | prose | pages [14] -->
m

<!-- b004944 | prose | pages [14] -->
m

<!-- b004945 | prose | pages [14] -->
m

<!-- b004946 | prose | pages [14] -->
m

<!-- b004947 | prose | pages [14] -->
m

<!-- b004948 | prose | pages [14] -->
m

<!-- b004949 | prose | pages [14] -->
m

<!-- b004950 | prose | pages [14] -->
m

<!-- b004951 | prose | pages [14] -->
m

<!-- b004952 | prose | pages [14] -->
m

<!-- b004953 | prose | pages [14] -->
m

<!-- b004954 | prose | pages [14] -->
m

<!-- b004955 | prose | pages [14] -->
m

<!-- b004956 | prose | pages [14] -->
m

<!-- b004957 | prose | pages [14] -->
m

<!-- b004958 | prose | pages [14] -->
m

<!-- b004959 | prose | pages [14] -->
m

<!-- b004960 | prose | pages [14] -->
m

<!-- b004961 | prose | pages [14] -->
m

<!-- b004962 | prose | pages [14] -->
m

<!-- b004963 | prose | pages [14] -->
m

<!-- b004964 | prose | pages [14] -->
m

<!-- b004965 | prose | pages [14] -->
m

<!-- b004966 | prose | pages [14] -->
m

<!-- b004967 | prose | pages [14] -->
m

<!-- b004968 | prose | pages [14] -->
m

<!-- b004969 | prose | pages [14] -->
m

<!-- b004970 | prose | pages [14] -->
m

<!-- b004971 | prose | pages [14] -->
m

<!-- b004972 | prose | pages [14] -->
m

<!-- b004973 | prose | pages [14] -->
m

<!-- b004974 | prose | pages [14] -->
m

<!-- b004975 | prose | pages [14] -->
m

<!-- b004976 | prose | pages [14] -->
m

<!-- b004977 | prose | pages [14] -->
m

<!-- b004978 | prose | pages [14] -->
m

<!-- b004979 | prose | pages [14] -->
m

<!-- b004980 | prose | pages [14] -->
m

<!-- b004981 | prose | pages [14] -->
m

<!-- b004982 | prose | pages [14] -->
m

<!-- b004983 | prose | pages [14] -->
m

<!-- b004984 | prose | pages [14] -->
m

<!-- b004985 | prose | pages [14] -->
m

<!-- b004986 | prose | pages [14] -->
m

<!-- b004987 | prose | pages [14] -->
m

<!-- b004988 | prose | pages [14] -->
m

<!-- b004989 | prose | pages [14] -->
m

<!-- b004990 | prose | pages [14] -->
m

<!-- b004991 | prose | pages [14] -->
m

<!-- b004992 | prose | pages [14] -->
m

<!-- b004993 | prose | pages [14] -->
m

<!-- b004994 | prose | pages [14] -->
m

<!-- b004995 | prose | pages [14] -->
m

<!-- b004996 | prose | pages [14] -->
m

<!-- b004997 | prose | pages [14] -->
m

<!-- b004998 | prose | pages [14] -->
m

<!-- b004999 | prose | pages [14] -->
m

<!-- b005000 | prose | pages [14] -->
m

<!-- b005001 | prose | pages [14] -->
m

<!-- b005002 | prose | pages [14] -->
m

<!-- b005003 | prose | pages [14] -->
m

<!-- b005004 | prose | pages [14] -->
m

<!-- b005005 | prose | pages [14] -->
m

<!-- b005006 | prose | pages [14] -->
m

<!-- b005007 | prose | pages [14] -->
m

<!-- b005008 | prose | pages [14] -->
m

<!-- b005009 | prose | pages [14] -->
m

<!-- b005010 | prose | pages [14] -->
m

<!-- b005011 | prose | pages [14] -->
m

<!-- b005012 | prose | pages [14] -->
m

<!-- b005013 | prose | pages [14] -->
m

<!-- b005014 | prose | pages [14] -->
m

<!-- b005015 | prose | pages [14] -->
m

<!-- b005016 | prose | pages [14] -->
m

<!-- b005017 | prose | pages [14] -->
m

<!-- b005018 | prose | pages [14] -->
m

<!-- b005019 | prose | pages [14] -->
m

<!-- b005020 | prose | pages [14] -->
m

<!-- b005021 | prose | pages [14] -->
m

<!-- b005022 | prose | pages [14] -->
m

<!-- b005023 | prose | pages [14] -->
m

<!-- b005024 | prose | pages [14] -->
m

<!-- b005025 | prose | pages [14] -->
m

<!-- b005026 | prose | pages [14] -->
m

<!-- b005027 | prose | pages [14] -->
m

<!-- b005028 | prose | pages [14] -->
m

<!-- b005029 | prose | pages [14] -->
m

<!-- b005030 | prose | pages [14] -->
m

<!-- b005031 | prose | pages [14] -->
m

<!-- b005032 | prose | pages [14] -->
m

<!-- b005033 | prose | pages [14] -->
m

<!-- b005034 | prose | pages [14] -->
m

<!-- b005035 | prose | pages [14] -->
m

<!-- b005036 | prose | pages [14] -->
m

<!-- b005037 | prose | pages [14] -->
m

<!-- b005038 | prose | pages [14] -->
m

<!-- b005039 | prose | pages [14] -->
m

<!-- b005040 | prose | pages [14] -->
m

<!-- b005041 | prose | pages [14] -->
m

<!-- b005042 | prose | pages [14] -->
m

<!-- b005043 | prose | pages [14] -->
m

<!-- b005044 | prose | pages [14] -->
m

<!-- b005045 | prose | pages [14] -->
m

<!-- b005046 | prose | pages [14] -->
m

<!-- b005047 | prose | pages [14] -->
m

<!-- b005048 | prose | pages [14] -->
m

<!-- b005049 | prose | pages [14] -->
m

<!-- b005050 | prose | pages [14] -->
m

<!-- b005051 | prose | pages [14] -->
m

<!-- b005052 | prose | pages [14] -->
m

<!-- b005053 | prose | pages [14] -->
m

<!-- b005054 | prose | pages [14] -->
m

<!-- b005055 | prose | pages [14] -->
m

<!-- b005056 | prose | pages [14] -->
m

<!-- b005057 | prose | pages [14] -->
m

<!-- b005058 | prose | pages [14] -->
m

<!-- b005059 | prose | pages [14] -->
m

<!-- b005060 | prose | pages [14] -->
m

<!-- b005061 | prose | pages [14] -->
m

<!-- b005062 | prose | pages [14] -->
m

<!-- b005063 | prose | pages [14] -->
m

<!-- b005064 | prose | pages [14] -->
m

<!-- b005065 | prose | pages [14] -->
m

<!-- b005066 | prose | pages [14] -->
m

<!-- b005067 | prose | pages [14] -->
m

<!-- b005068 | prose | pages [14] -->
m

<!-- b005069 | prose | pages [14] -->
m

<!-- b005070 | prose | pages [14] -->
m

<!-- b005071 | prose | pages [14] -->
m

<!-- b005072 | prose | pages [14] -->
m

<!-- b005073 | prose | pages [14] -->
m

<!-- b005074 | prose | pages [14] -->
m

<!-- b005075 | prose | pages [14] -->
m

<!-- b005076 | prose | pages [14] -->
m

<!-- b005077 | prose | pages [14] -->
m

<!-- b005078 | prose | pages [14] -->
m

<!-- b005079 | prose | pages [14] -->
m

<!-- b005080 | prose | pages [14] -->
m

<!-- b005081 | prose | pages [14] -->
m

<!-- b005082 | prose | pages [14] -->
m

<!-- b005083 | prose | pages [14] -->
m

<!-- b005084 | prose | pages [14] -->
m

<!-- b005085 | prose | pages [14] -->
m

<!-- b005086 | prose | pages [14] -->
m

<!-- b005087 | prose | pages [14] -->
m

<!-- b005088 | prose | pages [14] -->
m

<!-- b005089 | prose | pages [14] -->
m

<!-- b005090 | prose | pages [14] -->
m

<!-- b005091 | prose | pages [14] -->
m

<!-- b005092 | prose | pages [14] -->
m

<!-- b005093 | prose | pages [14] -->
m

<!-- b005094 | prose | pages [14] -->
m

<!-- b005095 | prose | pages [14] -->
m

<!-- b005096 | prose | pages [14] -->
m

<!-- b005097 | prose | pages [14] -->
m

<!-- b005098 | prose | pages [14] -->
m

<!-- b005099 | prose | pages [14] -->
m

<!-- b005100 | prose | pages [14] -->
m

<!-- b005101 | prose | pages [14] -->
m

<!-- b005102 | prose | pages [14] -->
m

<!-- b005103 | prose | pages [14] -->
m

<!-- b005104 | prose | pages [14] -->
m

<!-- b005105 | prose | pages [14] -->
m

<!-- b005106 | prose | pages [14] -->
m

<!-- b005107 | prose | pages [14] -->
m

<!-- b005108 | prose | pages [14] -->
m

<!-- b005109 | prose | pages [14] -->
m

<!-- b005110 | prose | pages [14] -->
m

<!-- b005111 | prose | pages [14] -->
m

<!-- b005112 | prose | pages [14] -->
m

<!-- b005113 | prose | pages [14] -->
m

<!-- b005114 | prose | pages [14] -->
m

<!-- b005115 | prose | pages [14] -->
m

<!-- b005116 | prose | pages [14] -->
m

<!-- b005117 | prose | pages [14] -->
m

<!-- b005118 | prose | pages [14] -->
m

<!-- b005119 | prose | pages [14] -->
m

<!-- b005120 | prose | pages [14] -->
m

<!-- b005121 | prose | pages [14] -->
m

<!-- b005122 | prose | pages [14] -->
The odds of predicting which countries will earn their first medal in the next Olympics are

<!-- b005123 | prose | pages [14] -->
m

<!-- b005124 | prose | pages [14] -->
m

<!-- b005125 | prose | pages [14] -->
m

<!-- b005126 | prose | pages [14] -->
m

<!-- b005127 | prose | pages [14] -->
m

<!-- b005128 | prose | pages [14] -->
m

<!-- b005129 | prose | pages [14] -->
m

<!-- b005130 | prose | pages [14] -->
m

<!-- b005131 | prose | pages [14] -->
m

<!-- b005132 | prose | pages [14] -->
m

<!-- b005133 | prose | pages [14] -->
m

<!-- b005134 | prose | pages [14] -->
m

<!-- b005135 | prose | pages [14] -->
m

<!-- b005136 | prose | pages [14] -->
m

<!-- b005137 | prose | pages [14] -->
m

<!-- b005138 | prose | pages [14] -->
m

<!-- b005139 | prose | pages [14] -->
m

<!-- b005140 | prose | pages [14] -->
m

<!-- b005141 | prose | pages [14] -->
m

<!-- b005142 | prose | pages [14] -->
m

<!-- b005143 | prose | pages [14] -->
m

<!-- b005144 | prose | pages [14] -->
m

<!-- b005145 | prose | pages [14] -->
m

<!-- b005146 | prose | pages [14] -->
m

<!-- b005147 | prose | pages [14] -->
m

<!-- b005148 | prose | pages [14] -->
m

<!-- b005149 | prose | pages [14] -->
m

<!-- b005150 | prose | pages [14] -->
m

<!-- b005151 | prose | pages [14] -->
m

<!-- b005152 | prose | pages [14] -->
m

<!-- b005153 | prose | pages [14] -->
m

<!-- b005154 | prose | pages [14] -->
m

<!-- b005155 | prose | pages [14] -->
m

<!-- b005156 | prose | pages [14] -->
m

<!-- b005157 | prose | pages [14] -->
m

<!-- b005158 | prose | pages [14] -->
m

<!-- b005159 | prose | pages [14] -->
m

<!-- b005160 | prose | pages [14] -->
m

<!-- b005161 | prose | pages [14] -->
m

<!-- b005162 | prose | pages [14] -->
m

<!-- b005163 | prose | pages [14] -->
m

<!-- b005164 | prose | pages [14] -->
m

<!-- b005165 | prose | pages [14] -->
m

<!-- b005166 | prose | pages [14] -->
m

<!-- b005167 | prose | pages [14] -->
m

<!-- b005168 | prose | pages [14] -->
m

<!-- b005169 | prose | pages [14] -->
m

<!-- b005170 | prose | pages [14] -->
m

<!-- b005171 | prose | pages [14] -->
m

<!-- b005172 | prose | pages [14] -->
m

<!-- b005173 | prose | pages [14] -->
m

<!-- b005174 | prose | pages [14] -->
m

<!-- b005175 | prose | pages [14] -->
m

<!-- b005176 | prose | pages [14] -->
m

<!-- b005177 | prose | pages [14] -->
m

<!-- b005178 | prose | pages [14] -->
m

<!-- b005179 | prose | pages [14] -->
m

<!-- b005180 | prose | pages [14] -->
m

<!-- b005181 | prose | pages [14] -->
m

<!-- b005182 | prose | pages [14] -->
m

<!-- b005183 | prose | pages [14] -->
estimated using their respective cross-validation accuracies. The table below summarizes the estimated odds for each model:

<!-- b005184 | heading | pages [14] -->
Cross-Validation Accuracy

<!-- b005185 | heading | pages [14] -->
Model

<!-- b005186 | prose | pages [14] -->
Logistic Regression 88.09% Random Forest 94.12% Estimated Odds (Correctness) 4:1 (80% chance) 16:1 (94% chance)

<!-- b005187 | caption | pages [14] -->
Table 6: Estimated Odds for Predicting First Medal Winning Countries

<!-- b005188 | prose | pages [14] -->
关注数学模型

<!-- b005189 | furniture | pages [14] -->
2

<!-- b005190 | furniture | pages [14] -->
MATHmodels

<!-- b005191 | furniture | pages [14] -->
获取更多资讯

<!-- b005192 | furniture | pages [15] -->
Team # 2503389

<!-- b005193 | furniture | pages [15] -->
Page 15 of 26

<!-- b005194 | heading | pages [15] -->
Strategic Importance Assessment Model for Olympic Sports

<!-- b005195 | prose | pages [15] -->
7 (SIAMOS)

<!-- b005196 | prose | pages [15] -->
To measure the strategic importance of a specific sport s for a given country c, we establish a comprehensive evaluation framework based on four key indicators.

<!-- b005197 | heading | pages [15] -->
Model Development and Evaluation Framework

<!-- b005198 | prose | pages [15] -->
7.1

<!-- b005199 | prose | pages [15] -->
微信公众号：数学模型

<!-- b005200 | prose | pages [15] -->
Description of Indicators to Evaluate the Importance of Sport 7.1.1

<!-- b005201 | prose | pages [15] -->
The four key indicators used to evaluate the importance of a sport in the context of Olympic performance are:

<!-- b005202 | prose | pages [15] -->
• NMP (National Medal Proportion): Proportion of medals a sport contributes to a na- tion’s total medals.

<!-- b005203 | prose | pages [15] -->
• GCP (Global Competitive Presence): A country’s competitive strength in a sport rela- tive to global performanceBernard2004.

<!-- b005204 | prose | pages [15] -->
微信号：MATHmodels

<!-- b005205 | prose | pages [15] -->
• LAS (Long-term Achievement Stability): Stability of performance in a sport over the last five Olympics.

<!-- b005206 | prose | pages [15] -->
• ASD (Athlete Sport Distribution): Proportion of athletes allocated to a specific sport relative to the total number of athletes.

<!-- b005207 | prose | pages [15] -->
Each indicator is standardized using Min-Max normalization to ensure cross-country com- parability. A hybrid weighting scheme, integrating Principal Component Analysis (PCA) with expert validation, assigns weights of 40%, 30%, 20%, and 10%, respectively. This reflects the relative importance of each indicator in evaluating a sport’s strategic significance.

<!-- b005208 | caption | pages [15] -->
Table 7: Evaluation Indicators, Weights, and Formulas

<!-- b005209 | prose | pages [15] -->
Indicator

<!-- b005210 | prose | pages [15] -->
Formula

<!-- b005211 | prose | pages [15] -->
(Weight)

<!-- b005212 | prose | pages [15] -->
Medalsc,s Total Medalsc × 100% NMP (40%)

<!-- b005213 | prose | pages [15] -->
Medalsc,s

<!-- b005214 | prose | pages [15] -->
Standardization

<!-- b005215 | prose | pages [15] -->
Min-Max nor- malization Global Medalss × 100% GCP (30%)

<!-- b005216 | prose | pages [15] -->
1 −σ LAS (20%) µ

<!-- b005217 | prose | pages [15] -->
Athletesc,s Total Athletesc × 100% ASD (10%)

<!-- b005218 | prose | pages [15] -->
7.1.2

<!-- b005219 | heading | pages [15] -->
Model Construction

<!-- b005220 | prose | pages [15] -->
Min-Max nor- malization Min-Max nor- malization Min-Max nor- malization

<!-- b005221 | prose | pages [15] -->
The SIAMOS model integrates the four indicators to compute the importance score (ISc,s) for each sport s in each country c:

<!-- b005222 | prose | pages [15] -->
ISc,s = α · NMPnorm + β · GCPnorm + γ · LASnorm + δ · ASDnorm

<!-- b005223 | prose | pages [15] -->
where α : β : γ : δ = 4 : 3 : 2 : 1 (40%, 30%, 20%, 10%).

<!-- b005224 | prose | pages [15] -->
m

<!-- b005225 | prose | pages [15] -->
m

<!-- b005226 | prose | pages [15] -->
m

<!-- b005227 | prose | pages [15] -->
m

<!-- b005228 | prose | pages [15] -->
m

<!-- b005229 | prose | pages [15] -->
m

<!-- b005230 | prose | pages [15] -->
m

<!-- b005231 | prose | pages [15] -->
m

<!-- b005232 | prose | pages [15] -->
m

<!-- b005233 | prose | pages [15] -->
m

<!-- b005234 | prose | pages [15] -->
m

<!-- b005235 | prose | pages [15] -->
m

<!-- b005236 | prose | pages [15] -->
m

<!-- b005237 | prose | pages [15] -->
m

<!-- b005238 | prose | pages [15] -->
m

<!-- b005239 | prose | pages [15] -->
m

<!-- b005240 | prose | pages [15] -->
m

<!-- b005241 | prose | pages [15] -->
m

<!-- b005242 | prose | pages [15] -->
m

<!-- b005243 | prose | pages [15] -->
m

<!-- b005244 | prose | pages [15] -->
m

<!-- b005245 | prose | pages [15] -->
m

<!-- b005246 | prose | pages [15] -->
m

<!-- b005247 | prose | pages [15] -->
m

<!-- b005248 | prose | pages [15] -->
m

<!-- b005249 | prose | pages [15] -->
m

<!-- b005250 | prose | pages [15] -->
m

<!-- b005251 | prose | pages [15] -->
m

<!-- b005252 | prose | pages [15] -->
m

<!-- b005253 | prose | pages [15] -->
m

<!-- b005254 | prose | pages [15] -->
m

<!-- b005255 | prose | pages [15] -->
m

<!-- b005256 | prose | pages [15] -->
m

<!-- b005257 | prose | pages [15] -->
m

<!-- b005258 | prose | pages [15] -->
m

<!-- b005259 | prose | pages [15] -->
m

<!-- b005260 | prose | pages [15] -->
m

<!-- b005261 | prose | pages [15] -->
m

<!-- b005262 | prose | pages [15] -->
m

<!-- b005263 | prose | pages [15] -->
m

<!-- b005264 | prose | pages [15] -->
m

<!-- b005265 | prose | pages [15] -->
m

<!-- b005266 | prose | pages [15] -->
m

<!-- b005267 | prose | pages [15] -->
m

<!-- b005268 | prose | pages [15] -->
m

<!-- b005269 | prose | pages [15] -->
m

<!-- b005270 | prose | pages [15] -->
m

<!-- b005271 | prose | pages [15] -->
m

<!-- b005272 | prose | pages [15] -->
m

<!-- b005273 | prose | pages [15] -->
m

<!-- b005274 | prose | pages [15] -->
m

<!-- b005275 | prose | pages [15] -->
m

<!-- b005276 | prose | pages [15] -->
m

<!-- b005277 | prose | pages [15] -->
m

<!-- b005278 | prose | pages [15] -->
m

<!-- b005279 | prose | pages [15] -->
m

<!-- b005280 | prose | pages [15] -->
m

<!-- b005281 | prose | pages [15] -->
m

<!-- b005282 | prose | pages [15] -->
m

<!-- b005283 | prose | pages [15] -->
m

<!-- b005284 | prose | pages [15] -->
m

<!-- b005285 | prose | pages [15] -->
m

<!-- b005286 | prose | pages [15] -->
m

<!-- b005287 | prose | pages [15] -->
m

<!-- b005288 | prose | pages [15] -->
m

<!-- b005289 | prose | pages [15] -->
m

<!-- b005290 | prose | pages [15] -->
m

<!-- b005291 | prose | pages [15] -->
m

<!-- b005292 | prose | pages [15] -->
m

<!-- b005293 | prose | pages [15] -->
m

<!-- b005294 | prose | pages [15] -->
m

<!-- b005295 | prose | pages [15] -->
m

<!-- b005296 | prose | pages [15] -->
m

<!-- b005297 | prose | pages [15] -->
m

<!-- b005298 | prose | pages [15] -->
m

<!-- b005299 | prose | pages [15] -->
m

<!-- b005300 | prose | pages [15] -->
m

<!-- b005301 | prose | pages [15] -->
m

<!-- b005302 | prose | pages [15] -->
m

<!-- b005303 | prose | pages [15] -->
m

<!-- b005304 | prose | pages [15] -->
m

<!-- b005305 | prose | pages [15] -->
m

<!-- b005306 | prose | pages [15] -->
m

<!-- b005307 | prose | pages [15] -->
m

<!-- b005308 | prose | pages [15] -->
m

<!-- b005309 | prose | pages [15] -->
m

<!-- b005310 | prose | pages [15] -->
m

<!-- b005311 | prose | pages [15] -->
m

<!-- b005312 | prose | pages [15] -->
m

<!-- b005313 | prose | pages [15] -->
m

<!-- b005314 | prose | pages [15] -->
m

<!-- b005315 | prose | pages [15] -->
m

<!-- b005316 | prose | pages [15] -->
m

<!-- b005317 | prose | pages [15] -->
m

<!-- b005318 | prose | pages [15] -->
m

<!-- b005319 | prose | pages [15] -->
m

<!-- b005320 | prose | pages [15] -->
m

<!-- b005321 | prose | pages [15] -->
m

<!-- b005322 | prose | pages [15] -->
m

<!-- b005323 | prose | pages [15] -->
m

<!-- b005324 | prose | pages [15] -->
m

<!-- b005325 | prose | pages [15] -->
m

<!-- b005326 | prose | pages [15] -->
m

<!-- b005327 | prose | pages [15] -->
m

<!-- b005328 | prose | pages [15] -->
m

<!-- b005329 | prose | pages [15] -->
m

<!-- b005330 | prose | pages [15] -->
m

<!-- b005331 | prose | pages [15] -->
m

<!-- b005332 | prose | pages [15] -->
m

<!-- b005333 | prose | pages [15] -->
m

<!-- b005334 | prose | pages [15] -->
m

<!-- b005335 | prose | pages [15] -->
m

<!-- b005336 | prose | pages [15] -->
m

<!-- b005337 | prose | pages [15] -->
m

<!-- b005338 | prose | pages [15] -->
m

<!-- b005339 | prose | pages [15] -->
m

<!-- b005340 | prose | pages [15] -->
m

<!-- b005341 | prose | pages [15] -->
m

<!-- b005342 | prose | pages [15] -->
m

<!-- b005343 | prose | pages [15] -->
m

<!-- b005344 | prose | pages [15] -->
m

<!-- b005345 | prose | pages [15] -->
m

<!-- b005346 | prose | pages [15] -->
m

<!-- b005347 | prose | pages [15] -->
m

<!-- b005348 | prose | pages [15] -->
m

<!-- b005349 | prose | pages [15] -->
m

<!-- b005350 | prose | pages [15] -->
m

<!-- b005351 | prose | pages [15] -->
m

<!-- b005352 | prose | pages [15] -->
m

<!-- b005353 | prose | pages [15] -->
m

<!-- b005354 | prose | pages [15] -->
m

<!-- b005355 | prose | pages [15] -->
m

<!-- b005356 | prose | pages [15] -->
m

<!-- b005357 | prose | pages [15] -->
m

<!-- b005358 | prose | pages [15] -->
m

<!-- b005359 | prose | pages [15] -->
m

<!-- b005360 | prose | pages [15] -->
m

<!-- b005361 | prose | pages [15] -->
m

<!-- b005362 | prose | pages [15] -->
m

<!-- b005363 | prose | pages [15] -->
m

<!-- b005364 | prose | pages [15] -->
m

<!-- b005365 | prose | pages [15] -->
m

<!-- b005366 | prose | pages [15] -->
m

<!-- b005367 | prose | pages [15] -->
m

<!-- b005368 | prose | pages [15] -->
m

<!-- b005369 | prose | pages [15] -->
m

<!-- b005370 | prose | pages [15] -->
m

<!-- b005371 | prose | pages [15] -->
m

<!-- b005372 | prose | pages [15] -->
m

<!-- b005373 | prose | pages [15] -->
m

<!-- b005374 | prose | pages [15] -->
m

<!-- b005375 | prose | pages [15] -->
m

<!-- b005376 | prose | pages [15] -->
m

<!-- b005377 | prose | pages [15] -->
m

<!-- b005378 | prose | pages [15] -->
m

<!-- b005379 | prose | pages [15] -->
m

<!-- b005380 | prose | pages [15] -->
m

<!-- b005381 | prose | pages [15] -->
m

<!-- b005382 | prose | pages [15] -->
m

<!-- b005383 | prose | pages [15] -->
m

<!-- b005384 | prose | pages [15] -->
m

<!-- b005385 | prose | pages [15] -->
m

<!-- b005386 | prose | pages [15] -->
m

<!-- b005387 | prose | pages [15] -->
m

<!-- b005388 | prose | pages [15] -->
m

<!-- b005389 | prose | pages [15] -->
m

<!-- b005390 | prose | pages [15] -->
m

<!-- b005391 | prose | pages [15] -->
m

<!-- b005392 | prose | pages [15] -->
m

<!-- b005393 | prose | pages [15] -->
m

<!-- b005394 | prose | pages [15] -->
m

<!-- b005395 | prose | pages [15] -->
m

<!-- b005396 | prose | pages [15] -->
m

<!-- b005397 | prose | pages [15] -->
m

<!-- b005398 | prose | pages [15] -->
m

<!-- b005399 | prose | pages [15] -->
m

<!-- b005400 | prose | pages [15] -->
m

<!-- b005401 | prose | pages [15] -->
m

<!-- b005402 | prose | pages [15] -->
m

<!-- b005403 | prose | pages [15] -->
m

<!-- b005404 | prose | pages [15] -->
m

<!-- b005405 | prose | pages [15] -->
m

<!-- b005406 | prose | pages [15] -->
m

<!-- b005407 | prose | pages [15] -->
m

<!-- b005408 | prose | pages [15] -->
m

<!-- b005409 | prose | pages [15] -->
m

<!-- b005410 | prose | pages [15] -->
m

<!-- b005411 | prose | pages [15] -->
m

<!-- b005412 | prose | pages [15] -->
m

<!-- b005413 | prose | pages [15] -->
m

<!-- b005414 | prose | pages [15] -->
m

<!-- b005415 | prose | pages [15] -->
m

<!-- b005416 | prose | pages [15] -->
m

<!-- b005417 | prose | pages [15] -->
m

<!-- b005418 | prose | pages [15] -->
m

<!-- b005419 | prose | pages [15] -->
m

<!-- b005420 | prose | pages [15] -->
m

<!-- b005421 | prose | pages [15] -->
m

<!-- b005422 | prose | pages [15] -->
m

<!-- b005423 | prose | pages [15] -->
m

<!-- b005424 | prose | pages [15] -->
m

<!-- b005425 | prose | pages [15] -->
m

<!-- b005426 | prose | pages [15] -->
m

<!-- b005427 | prose | pages [15] -->
m

<!-- b005428 | prose | pages [15] -->
m

<!-- b005429 | prose | pages [15] -->
m

<!-- b005430 | prose | pages [15] -->
m

<!-- b005431 | prose | pages [15] -->
m

<!-- b005432 | prose | pages [15] -->
m

<!-- b005433 | prose | pages [15] -->
m

<!-- b005434 | prose | pages [15] -->
m

<!-- b005435 | prose | pages [15] -->
m

<!-- b005436 | prose | pages [15] -->
m

<!-- b005437 | prose | pages [15] -->
m

<!-- b005438 | prose | pages [15] -->
m

<!-- b005439 | prose | pages [15] -->
m

<!-- b005440 | prose | pages [15] -->
m

<!-- b005441 | prose | pages [15] -->
m

<!-- b005442 | prose | pages [15] -->
m

<!-- b005443 | prose | pages [15] -->
m

<!-- b005444 | prose | pages [15] -->
m

<!-- b005445 | prose | pages [15] -->
m

<!-- b005446 | prose | pages [15] -->
m

<!-- b005447 | prose | pages [15] -->
m

<!-- b005448 | prose | pages [15] -->
m

<!-- b005449 | prose | pages [15] -->
m

<!-- b005450 | prose | pages [15] -->
m

<!-- b005451 | prose | pages [15] -->
m

<!-- b005452 | prose | pages [15] -->
m

<!-- b005453 | prose | pages [15] -->
m

<!-- b005454 | prose | pages [15] -->
m

<!-- b005455 | prose | pages [15] -->
m

<!-- b005456 | prose | pages [15] -->
m

<!-- b005457 | prose | pages [15] -->
m

<!-- b005458 | prose | pages [15] -->
m

<!-- b005459 | prose | pages [15] -->
m

<!-- b005460 | prose | pages [15] -->
m

<!-- b005461 | prose | pages [15] -->
m

<!-- b005462 | prose | pages [15] -->
m

<!-- b005463 | prose | pages [15] -->
m

<!-- b005464 | prose | pages [15] -->
m

<!-- b005465 | prose | pages [15] -->
m

<!-- b005466 | prose | pages [15] -->
m

<!-- b005467 | prose | pages [15] -->
m

<!-- b005468 | prose | pages [15] -->
m

<!-- b005469 | prose | pages [15] -->
m

<!-- b005470 | prose | pages [15] -->
m

<!-- b005471 | prose | pages [15] -->
m

<!-- b005472 | prose | pages [15] -->
m

<!-- b005473 | prose | pages [15] -->
m

<!-- b005474 | prose | pages [15] -->
m

<!-- b005475 | prose | pages [15] -->
m

<!-- b005476 | prose | pages [15] -->
m

<!-- b005477 | prose | pages [15] -->
m

<!-- b005478 | prose | pages [15] -->
m

<!-- b005479 | prose | pages [15] -->
m

<!-- b005480 | prose | pages [15] -->
m

<!-- b005481 | prose | pages [15] -->
m

<!-- b005482 | prose | pages [15] -->
m

<!-- b005483 | prose | pages [15] -->
m

<!-- b005484 | prose | pages [15] -->
m

<!-- b005485 | prose | pages [15] -->
m

<!-- b005486 | prose | pages [15] -->
m

<!-- b005487 | prose | pages [15] -->
m

<!-- b005488 | prose | pages [15] -->
m

<!-- b005489 | prose | pages [15] -->
m

<!-- b005490 | prose | pages [15] -->
m

<!-- b005491 | prose | pages [15] -->
m

<!-- b005492 | prose | pages [15] -->
m

<!-- b005493 | prose | pages [15] -->
m

<!-- b005494 | prose | pages [15] -->
m

<!-- b005495 | prose | pages [15] -->
m

<!-- b005496 | prose | pages [15] -->
m

<!-- b005497 | prose | pages [15] -->
m

<!-- b005498 | prose | pages [15] -->
m

<!-- b005499 | prose | pages [15] -->
m

<!-- b005500 | prose | pages [15] -->
m

<!-- b005501 | prose | pages [15] -->
m

<!-- b005502 | prose | pages [15] -->
m

<!-- b005503 | prose | pages [15] -->
m

<!-- b005504 | prose | pages [15] -->
m

<!-- b005505 | prose | pages [15] -->
m

<!-- b005506 | prose | pages [15] -->
m

<!-- b005507 | prose | pages [15] -->
m

<!-- b005508 | furniture | pages [15] -->
m

<!-- b005509 | furniture | pages [15] -->
m

<!-- b005510 | furniture | pages [15] -->
m

<!-- b005511 | furniture | pages [15] -->
m

<!-- b005512 | furniture | pages [15] -->
m

<!-- b005513 | furniture | pages [15] -->
m

<!-- b005514 | furniture | pages [15] -->
m

<!-- b005515 | furniture | pages [15] -->
m

<!-- b005516 | furniture | pages [15] -->
m

<!-- b005517 | furniture | pages [15] -->
m

<!-- b005518 | furniture | pages [15] -->
m

<!-- b005519 | furniture | pages [15] -->
m

<!-- b005520 | furniture | pages [15] -->
m

<!-- b005521 | furniture | pages [15] -->
m

<!-- b005522 | furniture | pages [15] -->
m

<!-- b005523 | furniture | pages [15] -->
m

<!-- b005524 | furniture | pages [15] -->
m

<!-- b005525 | furniture | pages [15] -->
m

<!-- b005526 | furniture | pages [15] -->
m

<!-- b005527 | furniture | pages [15] -->
m

<!-- b005528 | furniture | pages [15] -->
m

<!-- b005529 | furniture | pages [15] -->
m

<!-- b005530 | furniture | pages [15] -->
m

<!-- b005531 | furniture | pages [15] -->
m

<!-- b005532 | furniture | pages [15] -->
m

<!-- b005533 | furniture | pages [15] -->
m

<!-- b005534 | furniture | pages [15] -->
m

<!-- b005535 | furniture | pages [15] -->
m

<!-- b005536 | furniture | pages [15] -->
m

<!-- b005537 | furniture | pages [15] -->
m

<!-- b005538 | furniture | pages [15] -->
m

<!-- b005539 | furniture | pages [15] -->
m

<!-- b005540 | furniture | pages [15] -->
m

<!-- b005541 | furniture | pages [15] -->
m

<!-- b005542 | furniture | pages [15] -->
m

<!-- b005543 | furniture | pages [15] -->
m

<!-- b005544 | furniture | pages [15] -->
m

<!-- b005545 | furniture | pages [15] -->
m

<!-- b005546 | furniture | pages [15] -->
m

<!-- b005547 | furniture | pages [15] -->
m

<!-- b005548 | furniture | pages [15] -->
m

<!-- b005549 | furniture | pages [15] -->
m

<!-- b005550 | furniture | pages [15] -->
m

<!-- b005551 | furniture | pages [15] -->
m

<!-- b005552 | furniture | pages [15] -->
m

<!-- b005553 | furniture | pages [15] -->
m

<!-- b005554 | furniture | pages [15] -->
m

<!-- b005555 | furniture | pages [15] -->
m

<!-- b005556 | furniture | pages [15] -->
m

<!-- b005557 | furniture | pages [15] -->
m

<!-- b005558 | furniture | pages [15] -->
m

<!-- b005559 | furniture | pages [15] -->
m

<!-- b005560 | furniture | pages [15] -->
m

<!-- b005561 | furniture | pages [15] -->
m

<!-- b005562 | furniture | pages [15] -->
m

<!-- b005563 | furniture | pages [15] -->
m

<!-- b005564 | furniture | pages [15] -->
m

<!-- b005565 | furniture | pages [15] -->
m

<!-- b005566 | furniture | pages [15] -->
m

<!-- b005567 | furniture | pages [15] -->
m

<!-- b005568 | furniture | pages [15] -->
m

<!-- b005569 | furniture | pages [15] -->
m

<!-- b005570 | furniture | pages [15] -->
m

<!-- b005571 | furniture | pages [15] -->
m

<!-- b005572 | furniture | pages [15] -->
m

<!-- b005573 | furniture | pages [15] -->
m

<!-- b005574 | furniture | pages [15] -->
m

<!-- b005575 | furniture | pages [15] -->
m

<!-- b005576 | furniture | pages [15] -->
m

<!-- b005577 | furniture | pages [15] -->
m

<!-- b005578 | furniture | pages [15] -->
m

<!-- b005579 | furniture | pages [15] -->
m

<!-- b005580 | furniture | pages [15] -->
m

<!-- b005581 | furniture | pages [15] -->
m

<!-- b005582 | furniture | pages [15] -->
m

<!-- b005583 | furniture | pages [15] -->
m

<!-- b005584 | furniture | pages [15] -->
m

<!-- b005585 | furniture | pages [15] -->
m

<!-- b005586 | furniture | pages [15] -->
m

<!-- b005587 | furniture | pages [15] -->
m

<!-- b005588 | furniture | pages [15] -->
m

<!-- b005589 | furniture | pages [15] -->
m

<!-- b005590 | furniture | pages [15] -->
m

<!-- b005591 | furniture | pages [15] -->
m

<!-- b005592 | furniture | pages [15] -->
m

<!-- b005593 | furniture | pages [15] -->
m

<!-- b005594 | furniture | pages [15] -->
m

<!-- b005595 | furniture | pages [15] -->
m

<!-- b005596 | furniture | pages [15] -->
m

<!-- b005597 | furniture | pages [15] -->
m

<!-- b005598 | furniture | pages [15] -->
m

<!-- b005599 | furniture | pages [15] -->
m

<!-- b005600 | furniture | pages [15] -->
m

<!-- b005601 | furniture | pages [15] -->
m

<!-- b005602 | furniture | pages [15] -->
m

<!-- b005603 | furniture | pages [15] -->
m

<!-- b005604 | furniture | pages [15] -->
m

<!-- b005605 | furniture | pages [15] -->
m

<!-- b005606 | furniture | pages [15] -->
m

<!-- b005607 | furniture | pages [15] -->
m

<!-- b005608 | furniture | pages [15] -->
m

<!-- b005609 | furniture | pages [15] -->
m

<!-- b005610 | furniture | pages [15] -->
m

<!-- b005611 | furniture | pages [15] -->
m

<!-- b005612 | furniture | pages [15] -->
m

<!-- b005613 | furniture | pages [15] -->
m

<!-- b005614 | furniture | pages [15] -->
m

<!-- b005615 | furniture | pages [15] -->
m

<!-- b005616 | furniture | pages [15] -->
m

<!-- b005617 | furniture | pages [15] -->
m

<!-- b005618 | furniture | pages [15] -->
m

<!-- b005619 | furniture | pages [15] -->
m

<!-- b005620 | furniture | pages [15] -->
m

<!-- b005621 | furniture | pages [15] -->
m

<!-- b005622 | furniture | pages [15] -->
m

<!-- b005623 | furniture | pages [15] -->
m

<!-- b005624 | furniture | pages [15] -->
m

<!-- b005625 | furniture | pages [15] -->
m

<!-- b005626 | furniture | pages [15] -->
m

<!-- b005627 | furniture | pages [15] -->
m

<!-- b005628 | furniture | pages [15] -->
m

<!-- b005629 | furniture | pages [15] -->
m

<!-- b005630 | furniture | pages [15] -->
m

<!-- b005631 | furniture | pages [15] -->
m

<!-- b005632 | furniture | pages [15] -->
m

<!-- b005633 | furniture | pages [15] -->
m

<!-- b005634 | furniture | pages [15] -->
m

<!-- b005635 | furniture | pages [15] -->
m

<!-- b005636 | furniture | pages [15] -->
m

<!-- b005637 | furniture | pages [15] -->
m

<!-- b005638 | furniture | pages [15] -->
m

<!-- b005639 | furniture | pages [15] -->
m

<!-- b005640 | furniture | pages [15] -->
m

<!-- b005641 | furniture | pages [15] -->
m

<!-- b005642 | furniture | pages [15] -->
m

<!-- b005643 | furniture | pages [15] -->
m

<!-- b005644 | furniture | pages [15] -->
m

<!-- b005645 | furniture | pages [15] -->
m

<!-- b005646 | furniture | pages [15] -->
m

<!-- b005647 | furniture | pages [15] -->
m

<!-- b005648 | furniture | pages [15] -->
m

<!-- b005649 | furniture | pages [15] -->
m

<!-- b005650 | furniture | pages [15] -->
m

<!-- b005651 | furniture | pages [15] -->
m

<!-- b005652 | furniture | pages [15] -->
m

<!-- b005653 | furniture | pages [15] -->
m

<!-- b005654 | furniture | pages [15] -->
m

<!-- b005655 | furniture | pages [15] -->
m

<!-- b005656 | furniture | pages [15] -->
m

<!-- b005657 | furniture | pages [15] -->
m

<!-- b005658 | furniture | pages [15] -->
m

<!-- b005659 | furniture | pages [15] -->
m

<!-- b005660 | furniture | pages [15] -->
m

<!-- b005661 | furniture | pages [15] -->
m

<!-- b005662 | furniture | pages [15] -->
m

<!-- b005663 | furniture | pages [15] -->
m

<!-- b005664 | furniture | pages [15] -->
m

<!-- b005665 | furniture | pages [15] -->
m

<!-- b005666 | furniture | pages [15] -->
m

<!-- b005667 | furniture | pages [15] -->
m

<!-- b005668 | furniture | pages [15] -->
m

<!-- b005669 | furniture | pages [15] -->
m

<!-- b005670 | furniture | pages [15] -->
m

<!-- b005671 | furniture | pages [15] -->
m

<!-- b005672 | furniture | pages [15] -->
m

<!-- b005673 | furniture | pages [15] -->
m

<!-- b005674 | furniture | pages [15] -->
m

<!-- b005675 | furniture | pages [15] -->
m

<!-- b005676 | furniture | pages [15] -->
m

<!-- b005677 | furniture | pages [15] -->
m

<!-- b005678 | furniture | pages [15] -->
m

<!-- b005679 | furniture | pages [15] -->
m

<!-- b005680 | furniture | pages [15] -->
m

<!-- b005681 | furniture | pages [15] -->
m

<!-- b005682 | furniture | pages [15] -->
m

<!-- b005683 | furniture | pages [15] -->
m

<!-- b005684 | furniture | pages [15] -->
m

<!-- b005685 | furniture | pages [15] -->
m

<!-- b005686 | furniture | pages [15] -->
m

<!-- b005687 | furniture | pages [15] -->
m

<!-- b005688 | furniture | pages [15] -->
m

<!-- b005689 | furniture | pages [15] -->
m

<!-- b005690 | furniture | pages [15] -->
m

<!-- b005691 | furniture | pages [15] -->
m

<!-- b005692 | furniture | pages [15] -->
m

<!-- b005693 | furniture | pages [15] -->
m

<!-- b005694 | furniture | pages [15] -->
m

<!-- b005695 | furniture | pages [15] -->
m

<!-- b005696 | furniture | pages [15] -->
m

<!-- b005697 | furniture | pages [15] -->
m

<!-- b005698 | furniture | pages [15] -->
m

<!-- b005699 | furniture | pages [15] -->
m

<!-- b005700 | furniture | pages [15] -->
m

<!-- b005701 | furniture | pages [15] -->
m

<!-- b005702 | furniture | pages [15] -->
m

<!-- b005703 | furniture | pages [15] -->
m

<!-- b005704 | furniture | pages [15] -->
m

<!-- b005705 | furniture | pages [15] -->
m

<!-- b005706 | furniture | pages [15] -->
m

<!-- b005707 | furniture | pages [15] -->
m

<!-- b005708 | furniture | pages [15] -->
m

<!-- b005709 | furniture | pages [15] -->
m

<!-- b005710 | furniture | pages [15] -->
m

<!-- b005711 | furniture | pages [15] -->
m

<!-- b005712 | furniture | pages [15] -->
m

<!-- b005713 | furniture | pages [15] -->
m

<!-- b005714 | furniture | pages [15] -->
m

<!-- b005715 | furniture | pages [15] -->
m

<!-- b005716 | furniture | pages [15] -->
m

<!-- b005717 | furniture | pages [15] -->
m

<!-- b005718 | furniture | pages [15] -->
m

<!-- b005719 | furniture | pages [15] -->
m

<!-- b005720 | furniture | pages [15] -->
m

<!-- b005721 | furniture | pages [15] -->
m

<!-- b005722 | furniture | pages [15] -->
m

<!-- b005723 | furniture | pages [15] -->
m

<!-- b005724 | furniture | pages [15] -->
m

<!-- b005725 | furniture | pages [15] -->
m

<!-- b005726 | furniture | pages [15] -->
m

<!-- b005727 | furniture | pages [15] -->
m

<!-- b005728 | furniture | pages [15] -->
m

<!-- b005729 | furniture | pages [15] -->
m

<!-- b005730 | furniture | pages [15] -->
m

<!-- b005731 | furniture | pages [15] -->
m

<!-- b005732 | furniture | pages [15] -->
m

<!-- b005733 | furniture | pages [15] -->
m

<!-- b005734 | furniture | pages [15] -->
m

<!-- b005735 | furniture | pages [15] -->
m

<!-- b005736 | furniture | pages [15] -->
m

<!-- b005737 | furniture | pages [15] -->
m

<!-- b005738 | furniture | pages [15] -->
m

<!-- b005739 | furniture | pages [15] -->
m

<!-- b005740 | furniture | pages [15] -->
m

<!-- b005741 | furniture | pages [15] -->
m

<!-- b005742 | furniture | pages [15] -->
m

<!-- b005743 | furniture | pages [15] -->
m

<!-- b005744 | furniture | pages [15] -->
m

<!-- b005745 | furniture | pages [15] -->
m

<!-- b005746 | furniture | pages [15] -->
m

<!-- b005747 | furniture | pages [15] -->
m

<!-- b005748 | furniture | pages [15] -->
m

<!-- b005749 | furniture | pages [15] -->
m

<!-- b005750 | furniture | pages [15] -->
m

<!-- b005751 | furniture | pages [15] -->
m

<!-- b005752 | furniture | pages [15] -->
m

<!-- b005753 | furniture | pages [15] -->
m

<!-- b005754 | furniture | pages [15] -->
m

<!-- b005755 | furniture | pages [15] -->
m

<!-- b005756 | furniture | pages [15] -->
m

<!-- b005757 | furniture | pages [15] -->
m

<!-- b005758 | furniture | pages [15] -->
m

<!-- b005759 | furniture | pages [15] -->
m

<!-- b005760 | furniture | pages [15] -->
m

<!-- b005761 | furniture | pages [15] -->
m

<!-- b005762 | furniture | pages [15] -->
m

<!-- b005763 | furniture | pages [15] -->
m

<!-- b005764 | furniture | pages [15] -->
m

<!-- b005765 | furniture | pages [15] -->
m

<!-- b005766 | furniture | pages [15] -->
m

<!-- b005767 | furniture | pages [15] -->
m

<!-- b005768 | furniture | pages [15] -->
m

<!-- b005769 | furniture | pages [15] -->
m

<!-- b005770 | furniture | pages [15] -->
m

<!-- b005771 | furniture | pages [15] -->
m

<!-- b005772 | furniture | pages [15] -->
m

<!-- b005773 | furniture | pages [15] -->
m

<!-- b005774 | furniture | pages [15] -->
m

<!-- b005775 | furniture | pages [15] -->
m

<!-- b005776 | furniture | pages [15] -->
m

<!-- b005777 | furniture | pages [15] -->
m

<!-- b005778 | furniture | pages [15] -->
m

<!-- b005779 | furniture | pages [15] -->
m

<!-- b005780 | furniture | pages [15] -->
m

<!-- b005781 | furniture | pages [15] -->
m

<!-- b005782 | furniture | pages [15] -->
m

<!-- b005783 | furniture | pages [15] -->
m

<!-- b005784 | furniture | pages [15] -->
m

<!-- b005785 | furniture | pages [15] -->
m

<!-- b005786 | furniture | pages [15] -->
m

<!-- b005787 | furniture | pages [15] -->
m

<!-- b005788 | furniture | pages [15] -->
m

<!-- b005789 | furniture | pages [15] -->
m

<!-- b005790 | furniture | pages [15] -->
m

<!-- b005791 | furniture | pages [15] -->
m

<!-- b005792 | furniture | pages [15] -->
m

<!-- b005793 | furniture | pages [15] -->
m

<!-- b005794 | furniture | pages [15] -->
m

<!-- b005795 | furniture | pages [15] -->
m

<!-- b005796 | furniture | pages [15] -->
m

<!-- b005797 | furniture | pages [15] -->
m

<!-- b005798 | furniture | pages [15] -->
m

<!-- b005799 | furniture | pages [15] -->
m

<!-- b005800 | furniture | pages [15] -->
m

<!-- b005801 | furniture | pages [15] -->
m

<!-- b005802 | furniture | pages [15] -->
m

<!-- b005803 | furniture | pages [15] -->
m

<!-- b005804 | furniture | pages [15] -->
m

<!-- b005805 | furniture | pages [15] -->
m

<!-- b005806 | furniture | pages [15] -->
m

<!-- b005807 | furniture | pages [15] -->
m

<!-- b005808 | furniture | pages [15] -->
m

<!-- b005809 | furniture | pages [15] -->
m

<!-- b005810 | furniture | pages [15] -->
m

<!-- b005811 | furniture | pages [15] -->
m

<!-- b005812 | furniture | pages [15] -->
m

<!-- b005813 | furniture | pages [15] -->
m

<!-- b005814 | furniture | pages [15] -->
m

<!-- b005815 | furniture | pages [15] -->
m

<!-- b005816 | furniture | pages [15] -->
m

<!-- b005817 | furniture | pages [15] -->
m

<!-- b005818 | furniture | pages [15] -->
m

<!-- b005819 | furniture | pages [15] -->
m

<!-- b005820 | furniture | pages [15] -->
m

<!-- b005821 | furniture | pages [15] -->
m

<!-- b005822 | furniture | pages [15] -->
m

<!-- b005823 | furniture | pages [15] -->
m

<!-- b005824 | furniture | pages [15] -->
m

<!-- b005825 | furniture | pages [15] -->
m

<!-- b005826 | furniture | pages [15] -->
m

<!-- b005827 | furniture | pages [15] -->
m

<!-- b005828 | furniture | pages [15] -->
m

<!-- b005829 | furniture | pages [15] -->
m

<!-- b005830 | furniture | pages [15] -->
m

<!-- b005831 | furniture | pages [15] -->
m

<!-- b005832 | furniture | pages [15] -->
m

<!-- b005833 | furniture | pages [15] -->
m

<!-- b005834 | furniture | pages [15] -->
m

<!-- b005835 | furniture | pages [15] -->
m

<!-- b005836 | furniture | pages [15] -->
m

<!-- b005837 | furniture | pages [15] -->
m

<!-- b005838 | furniture | pages [15] -->
m

<!-- b005839 | furniture | pages [15] -->
m

<!-- b005840 | furniture | pages [15] -->
m

<!-- b005841 | furniture | pages [15] -->
m

<!-- b005842 | furniture | pages [15] -->
m

<!-- b005843 | furniture | pages [15] -->
m

<!-- b005844 | furniture | pages [15] -->
m

<!-- b005845 | furniture | pages [15] -->
m

<!-- b005846 | furniture | pages [15] -->
m

<!-- b005847 | furniture | pages [15] -->
m

<!-- b005848 | furniture | pages [15] -->
m

<!-- b005849 | furniture | pages [15] -->
m

<!-- b005850 | furniture | pages [15] -->
m

<!-- b005851 | furniture | pages [15] -->
m

<!-- b005852 | furniture | pages [15] -->
m

<!-- b005853 | furniture | pages [15] -->
m

<!-- b005854 | furniture | pages [15] -->
m

<!-- b005855 | furniture | pages [15] -->
m

<!-- b005856 | furniture | pages [15] -->
m

<!-- b005857 | furniture | pages [15] -->
m

<!-- b005858 | furniture | pages [15] -->
m

<!-- b005859 | furniture | pages [15] -->
m

<!-- b005860 | furniture | pages [15] -->
m

<!-- b005861 | furniture | pages [15] -->
m

<!-- b005862 | furniture | pages [15] -->
m

<!-- b005863 | furniture | pages [15] -->
m

<!-- b005864 | furniture | pages [15] -->
m

<!-- b005865 | furniture | pages [15] -->
m

<!-- b005866 | furniture | pages [15] -->
m

<!-- b005867 | furniture | pages [15] -->
m

<!-- b005868 | furniture | pages [15] -->
m

<!-- b005869 | furniture | pages [15] -->
m

<!-- b005870 | furniture | pages [15] -->
m

<!-- b005871 | furniture | pages [15] -->
m

<!-- b005872 | furniture | pages [15] -->
m

<!-- b005873 | furniture | pages [15] -->
m

<!-- b005874 | furniture | pages [15] -->
m

<!-- b005875 | furniture | pages [15] -->
m

<!-- b005876 | furniture | pages [15] -->
m

<!-- b005877 | furniture | pages [15] -->
m

<!-- b005878 | furniture | pages [15] -->
m

<!-- b005879 | furniture | pages [15] -->
m

<!-- b005880 | furniture | pages [15] -->
m

<!-- b005881 | furniture | pages [15] -->
m

<!-- b005882 | furniture | pages [15] -->
m

<!-- b005883 | furniture | pages [15] -->
m

<!-- b005884 | furniture | pages [15] -->
m

<!-- b005885 | furniture | pages [15] -->
m

<!-- b005886 | furniture | pages [15] -->
m

<!-- b005887 | furniture | pages [15] -->
m

<!-- b005888 | furniture | pages [15] -->
m

<!-- b005889 | furniture | pages [15] -->
m

<!-- b005890 | furniture | pages [15] -->
m

<!-- b005891 | furniture | pages [15] -->
m

<!-- b005892 | furniture | pages [15] -->
m

<!-- b005893 | furniture | pages [15] -->
m

<!-- b005894 | furniture | pages [15] -->
m

<!-- b005895 | furniture | pages [15] -->
m

<!-- b005896 | furniture | pages [15] -->
m

<!-- b005897 | furniture | pages [15] -->
m

<!-- b005898 | furniture | pages [15] -->
m

<!-- b005899 | furniture | pages [15] -->
m

<!-- b005900 | furniture | pages [15] -->
m

<!-- b005901 | furniture | pages [15] -->
m

<!-- b005902 | furniture | pages [15] -->
m

<!-- b005903 | furniture | pages [15] -->
m

<!-- b005904 | furniture | pages [15] -->
m

<!-- b005905 | furniture | pages [15] -->
m

<!-- b005906 | furniture | pages [15] -->
m

<!-- b005907 | furniture | pages [15] -->
m

<!-- b005908 | furniture | pages [15] -->
m

<!-- b005909 | furniture | pages [15] -->
m

<!-- b005910 | furniture | pages [15] -->
m

<!-- b005911 | furniture | pages [16] -->
Team # 2503389

<!-- b005912 | furniture | pages [16] -->
Page 16 of 26

<!-- b005913 | heading | pages [16] -->
Result 1: Relationship Between Events and Medal Counts

<!-- b005914 | prose | pages [16] -->
7.2

<!-- b005915 | caption | pages [16] -->
Figure 10: Correlation analysis: (a) shows the impact of the number of events, while (b) high-

<!-- b005916 | prose | pages [16] -->
lights the influence of sports on medal counts.

<!-- b005917 | prose | pages [16] -->
Conclusion: As shown in Figure 10, the number of events is positively correlated with the medal counts of participating countries. Similarly, the diversity of events also demonstrates a positive correlation with medal counts. These findings indicate that both the quantity and variety of events positively impact a nation’s medal-winning potential.

<!-- b005918 | heading | pages [16] -->
Result 2: Sport-Specific Importance Across Nations

<!-- b005919 | prose | pages [16] -->
7.3

<!-- b005920 | prose | pages [16] -->
7.3.1 Calculated Scores

<!-- b005921 | prose | pages [16] -->
The following table presents the calculated importance scores for selected countries and sports:

<!-- b005922 | caption | pages [16] -->
Table 8: Importance Scores for Selected Countries and Sports

<!-- b005923 | prose | pages [16] -->
Importance Score (IS) Country Sport China Diving China Table Tennis USA Swimming USA Basketball Korea Archery Korea Badminton Japan Judo Japan Gymnastics Australia Swimming Australia Cycling

<!-- b005924 | prose | pages [16] -->
7.3.2

<!-- b005925 | heading | pages [16] -->
Insights and Recommendations

<!-- b005926 | prose | pages [16] -->
Ranking 33.1 1 29.6 2 39.8 1 27.8 2 37.4 1 31.8 2 36.5 1 30.2 2 38.6 1 29.7 2

<!-- b005927 | prose | pages [16] -->
m

<!-- b005928 | prose | pages [16] -->
m

<!-- b005929 | prose | pages [16] -->
m

<!-- b005930 | prose | pages [16] -->
m

<!-- b005931 | prose | pages [16] -->
m

<!-- b005932 | prose | pages [16] -->
m

<!-- b005933 | prose | pages [16] -->
m

<!-- b005934 | prose | pages [16] -->
m

<!-- b005935 | prose | pages [16] -->
m

<!-- b005936 | prose | pages [16] -->
m

<!-- b005937 | prose | pages [16] -->
m

<!-- b005938 | prose | pages [16] -->
m

<!-- b005939 | prose | pages [16] -->
m

<!-- b005940 | prose | pages [16] -->
m

<!-- b005941 | prose | pages [16] -->
m

<!-- b005942 | prose | pages [16] -->
m

<!-- b005943 | prose | pages [16] -->
m

<!-- b005944 | prose | pages [16] -->
m

<!-- b005945 | prose | pages [16] -->
m

<!-- b005946 | prose | pages [16] -->
m

<!-- b005947 | prose | pages [16] -->
m

<!-- b005948 | prose | pages [16] -->
m

<!-- b005949 | prose | pages [16] -->
m

<!-- b005950 | prose | pages [16] -->
m

<!-- b005951 | prose | pages [16] -->
m

<!-- b005952 | prose | pages [16] -->
m

<!-- b005953 | prose | pages [16] -->
m

<!-- b005954 | prose | pages [16] -->
m

<!-- b005955 | prose | pages [16] -->
m

<!-- b005956 | prose | pages [16] -->
m

<!-- b005957 | prose | pages [16] -->
m

<!-- b005958 | prose | pages [16] -->
m

<!-- b005959 | prose | pages [16] -->
m

<!-- b005960 | prose | pages [16] -->
m

<!-- b005961 | prose | pages [16] -->
m

<!-- b005962 | prose | pages [16] -->
m

<!-- b005963 | prose | pages [16] -->
m

<!-- b005964 | prose | pages [16] -->
m

<!-- b005965 | prose | pages [16] -->
m

<!-- b005966 | prose | pages [16] -->
m

<!-- b005967 | prose | pages [16] -->
m

<!-- b005968 | prose | pages [16] -->
m

<!-- b005969 | prose | pages [16] -->
m

<!-- b005970 | prose | pages [16] -->
m

<!-- b005971 | prose | pages [16] -->
m

<!-- b005972 | prose | pages [16] -->
m

<!-- b005973 | prose | pages [16] -->
m

<!-- b005974 | prose | pages [16] -->
m

<!-- b005975 | prose | pages [16] -->
m

<!-- b005976 | prose | pages [16] -->
m

<!-- b005977 | prose | pages [16] -->
m

<!-- b005978 | prose | pages [16] -->
m

<!-- b005979 | prose | pages [16] -->
m

<!-- b005980 | prose | pages [16] -->
m

<!-- b005981 | prose | pages [16] -->
m

<!-- b005982 | prose | pages [16] -->
m

<!-- b005983 | prose | pages [16] -->
m

<!-- b005984 | prose | pages [16] -->
m

<!-- b005985 | prose | pages [16] -->
m

<!-- b005986 | prose | pages [16] -->
m

<!-- b005987 | prose | pages [16] -->
m

<!-- b005988 | prose | pages [16] -->
m

<!-- b005989 | prose | pages [16] -->
m

<!-- b005990 | prose | pages [16] -->
m

<!-- b005991 | prose | pages [16] -->
m

<!-- b005992 | prose | pages [16] -->
m

<!-- b005993 | prose | pages [16] -->
m

<!-- b005994 | prose | pages [16] -->
m

<!-- b005995 | prose | pages [16] -->
m

<!-- b005996 | prose | pages [16] -->
m

<!-- b005997 | prose | pages [16] -->
m

<!-- b005998 | prose | pages [16] -->
m

<!-- b005999 | prose | pages [16] -->
m

<!-- b006000 | prose | pages [16] -->
m

<!-- b006001 | prose | pages [16] -->
m

<!-- b006002 | prose | pages [16] -->
m

<!-- b006003 | prose | pages [16] -->
m

<!-- b006004 | prose | pages [16] -->
m

<!-- b006005 | prose | pages [16] -->
m

<!-- b006006 | prose | pages [16] -->
m

<!-- b006007 | prose | pages [16] -->
m

<!-- b006008 | prose | pages [16] -->
m

<!-- b006009 | prose | pages [16] -->
m

<!-- b006010 | prose | pages [16] -->
m

<!-- b006011 | prose | pages [16] -->
m

<!-- b006012 | prose | pages [16] -->
m

<!-- b006013 | prose | pages [16] -->
m

<!-- b006014 | prose | pages [16] -->
m

<!-- b006015 | prose | pages [16] -->
m

<!-- b006016 | prose | pages [16] -->
m

<!-- b006017 | prose | pages [16] -->
m

<!-- b006018 | prose | pages [16] -->
m

<!-- b006019 | prose | pages [16] -->
m

<!-- b006020 | prose | pages [16] -->
m

<!-- b006021 | prose | pages [16] -->
m

<!-- b006022 | prose | pages [16] -->
m

<!-- b006023 | prose | pages [16] -->
m

<!-- b006024 | prose | pages [16] -->
m

<!-- b006025 | prose | pages [16] -->
m

<!-- b006026 | prose | pages [16] -->
m

<!-- b006027 | prose | pages [16] -->
m

<!-- b006028 | prose | pages [16] -->
m

<!-- b006029 | prose | pages [16] -->
m

<!-- b006030 | prose | pages [16] -->
m

<!-- b006031 | prose | pages [16] -->
m

<!-- b006032 | prose | pages [16] -->
m

<!-- b006033 | prose | pages [16] -->
m

<!-- b006034 | prose | pages [16] -->
m

<!-- b006035 | prose | pages [16] -->
m

<!-- b006036 | prose | pages [16] -->
m

<!-- b006037 | prose | pages [16] -->
m

<!-- b006038 | prose | pages [16] -->
m

<!-- b006039 | prose | pages [16] -->
m

<!-- b006040 | prose | pages [16] -->
m

<!-- b006041 | prose | pages [16] -->
m

<!-- b006042 | prose | pages [16] -->
m

<!-- b006043 | prose | pages [16] -->
m

<!-- b006044 | prose | pages [16] -->
m

<!-- b006045 | prose | pages [16] -->
m

<!-- b006046 | prose | pages [16] -->
m

<!-- b006047 | prose | pages [16] -->
m

<!-- b006048 | prose | pages [16] -->
m

<!-- b006049 | prose | pages [16] -->
m

<!-- b006050 | prose | pages [16] -->
m

<!-- b006051 | prose | pages [16] -->
m

<!-- b006052 | prose | pages [16] -->
m

<!-- b006053 | prose | pages [16] -->
m

<!-- b006054 | prose | pages [16] -->
m

<!-- b006055 | prose | pages [16] -->
m

<!-- b006056 | prose | pages [16] -->
m

<!-- b006057 | prose | pages [16] -->
• China: Diving (IS = 33.1) and Table Tennis (IS = 29.6) dominate, reflecting historical strengths.

<!-- b006058 | prose | pages [16] -->
m

<!-- b006059 | prose | pages [16] -->
m

<!-- b006060 | prose | pages [16] -->
m

<!-- b006061 | prose | pages [16] -->
m

<!-- b006062 | prose | pages [16] -->
m

<!-- b006063 | prose | pages [16] -->
m

<!-- b006064 | prose | pages [16] -->
m

<!-- b006065 | prose | pages [16] -->
m

<!-- b006066 | prose | pages [16] -->
m

<!-- b006067 | prose | pages [16] -->
m

<!-- b006068 | prose | pages [16] -->
m

<!-- b006069 | prose | pages [16] -->
m

<!-- b006070 | prose | pages [16] -->
m

<!-- b006071 | prose | pages [16] -->
m

<!-- b006072 | prose | pages [16] -->
m

<!-- b006073 | prose | pages [16] -->
m

<!-- b006074 | prose | pages [16] -->
m

<!-- b006075 | prose | pages [16] -->
m

<!-- b006076 | prose | pages [16] -->
m

<!-- b006077 | prose | pages [16] -->
m

<!-- b006078 | prose | pages [16] -->
m

<!-- b006079 | prose | pages [16] -->
m

<!-- b006080 | prose | pages [16] -->
m

<!-- b006081 | prose | pages [16] -->
m

<!-- b006082 | prose | pages [16] -->
m

<!-- b006083 | prose | pages [16] -->
m

<!-- b006084 | prose | pages [16] -->
m

<!-- b006085 | prose | pages [16] -->
m

<!-- b006086 | prose | pages [16] -->
m

<!-- b006087 | prose | pages [16] -->
m

<!-- b006088 | prose | pages [16] -->
m

<!-- b006089 | prose | pages [16] -->
m

<!-- b006090 | prose | pages [16] -->
m

<!-- b006091 | prose | pages [16] -->
m

<!-- b006092 | prose | pages [16] -->
m

<!-- b006093 | prose | pages [16] -->
m

<!-- b006094 | prose | pages [16] -->
m

<!-- b006095 | prose | pages [16] -->
m

<!-- b006096 | prose | pages [16] -->
m

<!-- b006097 | prose | pages [16] -->
m

<!-- b006098 | prose | pages [16] -->
m

<!-- b006099 | prose | pages [16] -->
m

<!-- b006100 | prose | pages [16] -->
m

<!-- b006101 | prose | pages [16] -->
m

<!-- b006102 | prose | pages [16] -->
m

<!-- b006103 | prose | pages [16] -->
m

<!-- b006104 | prose | pages [16] -->
m

<!-- b006105 | prose | pages [16] -->
m

<!-- b006106 | prose | pages [16] -->
m

<!-- b006107 | prose | pages [16] -->
m

<!-- b006108 | prose | pages [16] -->
m

<!-- b006109 | prose | pages [16] -->
m

<!-- b006110 | prose | pages [16] -->
m

<!-- b006111 | prose | pages [16] -->
m

<!-- b006112 | prose | pages [16] -->
m

<!-- b006113 | prose | pages [16] -->
m

<!-- b006114 | prose | pages [16] -->
m

<!-- b006115 | prose | pages [16] -->
m

<!-- b006116 | prose | pages [16] -->
m

<!-- b006117 | prose | pages [16] -->
m

<!-- b006118 | prose | pages [16] -->
m

<!-- b006119 | prose | pages [16] -->
m

<!-- b006120 | prose | pages [16] -->
m

<!-- b006121 | prose | pages [16] -->
m

<!-- b006122 | prose | pages [16] -->
m

<!-- b006123 | prose | pages [16] -->
m

<!-- b006124 | prose | pages [16] -->
m

<!-- b006125 | prose | pages [16] -->
m

<!-- b006126 | prose | pages [16] -->
m

<!-- b006127 | prose | pages [16] -->
m

<!-- b006128 | prose | pages [16] -->
m

<!-- b006129 | prose | pages [16] -->
m

<!-- b006130 | prose | pages [16] -->
m

<!-- b006131 | prose | pages [16] -->
m

<!-- b006132 | prose | pages [16] -->
m

<!-- b006133 | prose | pages [16] -->
m

<!-- b006134 | prose | pages [16] -->
m

<!-- b006135 | prose | pages [16] -->
m

<!-- b006136 | prose | pages [16] -->
m

<!-- b006137 | prose | pages [16] -->
m

<!-- b006138 | prose | pages [16] -->
m

<!-- b006139 | prose | pages [16] -->
m

<!-- b006140 | prose | pages [16] -->
m

<!-- b006141 | prose | pages [16] -->
m

<!-- b006142 | prose | pages [16] -->
m

<!-- b006143 | prose | pages [16] -->
m

<!-- b006144 | prose | pages [16] -->
m

<!-- b006145 | prose | pages [16] -->
m

<!-- b006146 | prose | pages [16] -->
m

<!-- b006147 | prose | pages [16] -->
m

<!-- b006148 | prose | pages [16] -->
m

<!-- b006149 | prose | pages [16] -->
m

<!-- b006150 | prose | pages [16] -->
m

<!-- b006151 | prose | pages [16] -->
m

<!-- b006152 | prose | pages [16] -->
m

<!-- b006153 | prose | pages [16] -->
m

<!-- b006154 | prose | pages [16] -->
m

<!-- b006155 | prose | pages [16] -->
m

<!-- b006156 | prose | pages [16] -->
m

<!-- b006157 | prose | pages [16] -->
m

<!-- b006158 | prose | pages [16] -->
m

<!-- b006159 | prose | pages [16] -->
m

<!-- b006160 | prose | pages [16] -->
m

<!-- b006161 | prose | pages [16] -->
m

<!-- b006162 | prose | pages [16] -->
m

<!-- b006163 | prose | pages [16] -->
m

<!-- b006164 | prose | pages [16] -->
m

<!-- b006165 | prose | pages [16] -->
m

<!-- b006166 | prose | pages [16] -->
m

<!-- b006167 | prose | pages [16] -->
m

<!-- b006168 | prose | pages [16] -->
m

<!-- b006169 | prose | pages [16] -->
m

<!-- b006170 | prose | pages [16] -->
m

<!-- b006171 | prose | pages [16] -->
m

<!-- b006172 | prose | pages [16] -->
m

<!-- b006173 | prose | pages [16] -->
m

<!-- b006174 | prose | pages [16] -->
m

<!-- b006175 | prose | pages [16] -->
m

<!-- b006176 | prose | pages [16] -->
m

<!-- b006177 | prose | pages [16] -->
m

<!-- b006178 | prose | pages [16] -->
m

<!-- b006179 | prose | pages [16] -->
m

<!-- b006180 | prose | pages [16] -->
m

<!-- b006181 | prose | pages [16] -->
m

<!-- b006182 | prose | pages [16] -->
m

<!-- b006183 | prose | pages [16] -->
m

<!-- b006184 | prose | pages [16] -->
m

<!-- b006185 | prose | pages [16] -->
m

<!-- b006186 | prose | pages [16] -->
m

<!-- b006187 | prose | pages [16] -->
m

<!-- b006188 | prose | pages [16] -->
m

<!-- b006189 | prose | pages [16] -->
m

<!-- b006190 | prose | pages [16] -->
m

<!-- b006191 | prose | pages [16] -->
m

<!-- b006192 | prose | pages [16] -->
m

<!-- b006193 | prose | pages [16] -->
m

<!-- b006194 | prose | pages [16] -->
m

<!-- b006195 | prose | pages [16] -->
m

<!-- b006196 | prose | pages [16] -->
m

<!-- b006197 | prose | pages [16] -->
m

<!-- b006198 | prose | pages [16] -->
m

<!-- b006199 | prose | pages [16] -->
m

<!-- b006200 | prose | pages [16] -->
m

<!-- b006201 | prose | pages [16] -->
m

<!-- b006202 | prose | pages [16] -->
m

<!-- b006203 | prose | pages [16] -->
m

<!-- b006204 | prose | pages [16] -->
m

<!-- b006205 | prose | pages [16] -->
m

<!-- b006206 | prose | pages [16] -->
m

<!-- b006207 | prose | pages [16] -->
m

<!-- b006208 | prose | pages [16] -->
m

<!-- b006209 | prose | pages [16] -->
m

<!-- b006210 | prose | pages [16] -->
m

<!-- b006211 | prose | pages [16] -->
m

<!-- b006212 | prose | pages [16] -->
m

<!-- b006213 | prose | pages [16] -->
m

<!-- b006214 | prose | pages [16] -->
m

<!-- b006215 | prose | pages [16] -->
m

<!-- b006216 | prose | pages [16] -->
m

<!-- b006217 | prose | pages [16] -->
m

<!-- b006218 | prose | pages [16] -->
m

<!-- b006219 | prose | pages [16] -->
m

<!-- b006220 | prose | pages [16] -->
m

<!-- b006221 | prose | pages [16] -->
m

<!-- b006222 | prose | pages [16] -->
m

<!-- b006223 | prose | pages [16] -->
m

<!-- b006224 | prose | pages [16] -->
m

<!-- b006225 | prose | pages [16] -->
m

<!-- b006226 | prose | pages [16] -->
m

<!-- b006227 | prose | pages [16] -->
m

<!-- b006228 | prose | pages [16] -->
m

<!-- b006229 | prose | pages [16] -->
m

<!-- b006230 | prose | pages [16] -->
m

<!-- b006231 | prose | pages [16] -->
m

<!-- b006232 | prose | pages [16] -->
m

<!-- b006233 | prose | pages [16] -->
m

<!-- b006234 | prose | pages [16] -->
m

<!-- b006235 | prose | pages [16] -->
m

<!-- b006236 | prose | pages [16] -->
m

<!-- b006237 | prose | pages [16] -->
m

<!-- b006238 | prose | pages [16] -->
m

<!-- b006239 | prose | pages [16] -->
m

<!-- b006240 | prose | pages [16] -->
m

<!-- b006241 | prose | pages [16] -->
m

<!-- b006242 | prose | pages [16] -->
m

<!-- b006243 | prose | pages [16] -->
m

<!-- b006244 | prose | pages [16] -->
m

<!-- b006245 | prose | pages [16] -->
m

<!-- b006246 | prose | pages [16] -->
m

<!-- b006247 | prose | pages [16] -->
m

<!-- b006248 | prose | pages [16] -->
m

<!-- b006249 | prose | pages [16] -->
m

<!-- b006250 | prose | pages [16] -->
m

<!-- b006251 | prose | pages [16] -->
m

<!-- b006252 | prose | pages [16] -->
m

<!-- b006253 | prose | pages [16] -->
m

<!-- b006254 | prose | pages [16] -->
m

<!-- b006255 | prose | pages [16] -->
m

<!-- b006256 | prose | pages [16] -->
m

<!-- b006257 | prose | pages [16] -->
m

<!-- b006258 | prose | pages [16] -->
m

<!-- b006259 | prose | pages [16] -->
m

<!-- b006260 | prose | pages [16] -->
m

<!-- b006261 | prose | pages [16] -->
m

<!-- b006262 | prose | pages [16] -->
m

<!-- b006263 | prose | pages [16] -->
m

<!-- b006264 | prose | pages [16] -->
m

<!-- b006265 | prose | pages [16] -->
m

<!-- b006266 | prose | pages [16] -->
m

<!-- b006267 | prose | pages [16] -->
m

<!-- b006268 | prose | pages [16] -->
m

<!-- b006269 | prose | pages [16] -->
m

<!-- b006270 | prose | pages [16] -->
m

<!-- b006271 | prose | pages [16] -->
m

<!-- b006272 | prose | pages [16] -->
m

<!-- b006273 | prose | pages [16] -->
m

<!-- b006274 | prose | pages [16] -->
m

<!-- b006275 | prose | pages [16] -->
m

<!-- b006276 | prose | pages [16] -->
m

<!-- b006277 | prose | pages [16] -->
m

<!-- b006278 | prose | pages [16] -->
m

<!-- b006279 | prose | pages [16] -->
m

<!-- b006280 | prose | pages [16] -->
m

<!-- b006281 | prose | pages [16] -->
m

<!-- b006282 | prose | pages [16] -->
m

<!-- b006283 | prose | pages [16] -->
m

<!-- b006284 | prose | pages [16] -->
m

<!-- b006285 | prose | pages [16] -->
m

<!-- b006286 | prose | pages [16] -->
m

<!-- b006287 | prose | pages [16] -->
m

<!-- b006288 | prose | pages [16] -->
m

<!-- b006289 | prose | pages [16] -->
m

<!-- b006290 | prose | pages [16] -->
m

<!-- b006291 | prose | pages [16] -->
m

<!-- b006292 | prose | pages [16] -->
m

<!-- b006293 | prose | pages [16] -->
m

<!-- b006294 | prose | pages [16] -->
m

<!-- b006295 | prose | pages [16] -->
m

<!-- b006296 | prose | pages [16] -->
m

<!-- b006297 | prose | pages [16] -->
m

<!-- b006298 | prose | pages [16] -->
m

<!-- b006299 | prose | pages [16] -->
m

<!-- b006300 | prose | pages [16] -->
m

<!-- b006301 | prose | pages [16] -->
m

<!-- b006302 | prose | pages [16] -->
m

<!-- b006303 | prose | pages [16] -->
m

<!-- b006304 | prose | pages [16] -->
m

<!-- b006305 | prose | pages [16] -->
m

<!-- b006306 | prose | pages [16] -->
m

<!-- b006307 | prose | pages [16] -->
m

<!-- b006308 | prose | pages [16] -->
m

<!-- b006309 | prose | pages [16] -->
m

<!-- b006310 | prose | pages [16] -->
m

<!-- b006311 | prose | pages [16] -->
m

<!-- b006312 | prose | pages [16] -->
m

<!-- b006313 | prose | pages [16] -->
m

<!-- b006314 | prose | pages [16] -->
m

<!-- b006315 | prose | pages [16] -->
m

<!-- b006316 | prose | pages [16] -->
m

<!-- b006317 | prose | pages [16] -->
m

<!-- b006318 | prose | pages [16] -->
m

<!-- b006319 | prose | pages [16] -->
m

<!-- b006320 | prose | pages [16] -->
m

<!-- b006321 | prose | pages [16] -->
m

<!-- b006322 | prose | pages [16] -->
m

<!-- b006323 | prose | pages [16] -->
m

<!-- b006324 | prose | pages [16] -->
m

<!-- b006325 | prose | pages [16] -->
m

<!-- b006326 | prose | pages [16] -->
m

<!-- b006327 | prose | pages [16] -->
m

<!-- b006328 | prose | pages [16] -->
m

<!-- b006329 | prose | pages [16] -->
m

<!-- b006330 | prose | pages [16] -->
m

<!-- b006331 | prose | pages [16] -->
m

<!-- b006332 | prose | pages [16] -->
m

<!-- b006333 | prose | pages [16] -->
m

<!-- b006334 | prose | pages [16] -->
m

<!-- b006335 | prose | pages [16] -->
m

<!-- b006336 | prose | pages [16] -->
m

<!-- b006337 | prose | pages [16] -->
m

<!-- b006338 | prose | pages [16] -->
m

<!-- b006339 | prose | pages [16] -->
m

<!-- b006340 | prose | pages [16] -->
m

<!-- b006341 | prose | pages [16] -->
m

<!-- b006342 | prose | pages [16] -->
m

<!-- b006343 | prose | pages [16] -->
m

<!-- b006344 | prose | pages [16] -->
m

<!-- b006345 | prose | pages [16] -->
m

<!-- b006346 | prose | pages [16] -->
m

<!-- b006347 | prose | pages [16] -->
m

<!-- b006348 | prose | pages [16] -->
m

<!-- b006349 | prose | pages [16] -->
m

<!-- b006350 | prose | pages [16] -->
m

<!-- b006351 | prose | pages [16] -->
m

<!-- b006352 | prose | pages [16] -->
m

<!-- b006353 | prose | pages [16] -->
m

<!-- b006354 | prose | pages [16] -->
m

<!-- b006355 | prose | pages [16] -->
m

<!-- b006356 | prose | pages [16] -->
m

<!-- b006357 | prose | pages [16] -->
m

<!-- b006358 | prose | pages [16] -->
m

<!-- b006359 | prose | pages [16] -->
m

<!-- b006360 | prose | pages [16] -->
m

<!-- b006361 | prose | pages [16] -->
m

<!-- b006362 | prose | pages [16] -->
m

<!-- b006363 | prose | pages [16] -->
m

<!-- b006364 | prose | pages [16] -->
m

<!-- b006365 | prose | pages [16] -->
m

<!-- b006366 | prose | pages [16] -->
m

<!-- b006367 | prose | pages [16] -->
m

<!-- b006368 | prose | pages [16] -->
m

<!-- b006369 | prose | pages [16] -->
m

<!-- b006370 | prose | pages [16] -->
m

<!-- b006371 | prose | pages [16] -->
m

<!-- b006372 | prose | pages [16] -->
m

<!-- b006373 | prose | pages [16] -->
m

<!-- b006374 | prose | pages [16] -->
m

<!-- b006375 | prose | pages [16] -->
m

<!-- b006376 | prose | pages [16] -->
m

<!-- b006377 | prose | pages [16] -->
m

<!-- b006378 | prose | pages [16] -->
m

<!-- b006379 | prose | pages [16] -->
m

<!-- b006380 | prose | pages [16] -->
m

<!-- b006381 | prose | pages [16] -->
m

<!-- b006382 | prose | pages [16] -->
m

<!-- b006383 | prose | pages [16] -->
m

<!-- b006384 | prose | pages [16] -->
m

<!-- b006385 | prose | pages [16] -->
m

<!-- b006386 | prose | pages [16] -->
m

<!-- b006387 | prose | pages [16] -->
m

<!-- b006388 | prose | pages [16] -->
m

<!-- b006389 | prose | pages [16] -->
m

<!-- b006390 | prose | pages [16] -->
m

<!-- b006391 | prose | pages [16] -->
m

<!-- b006392 | prose | pages [16] -->
m

<!-- b006393 | prose | pages [16] -->
m

<!-- b006394 | prose | pages [16] -->
m

<!-- b006395 | prose | pages [16] -->
m

<!-- b006396 | prose | pages [16] -->
m

<!-- b006397 | prose | pages [16] -->
m

<!-- b006398 | prose | pages [16] -->
m

<!-- b006399 | prose | pages [16] -->
m

<!-- b006400 | prose | pages [16] -->
m

<!-- b006401 | prose | pages [16] -->
m

<!-- b006402 | prose | pages [16] -->
m

<!-- b006403 | prose | pages [16] -->
m

<!-- b006404 | prose | pages [16] -->
m

<!-- b006405 | prose | pages [16] -->
m

<!-- b006406 | prose | pages [16] -->
m

<!-- b006407 | prose | pages [16] -->
m

<!-- b006408 | prose | pages [16] -->
m

<!-- b006409 | prose | pages [16] -->
m

<!-- b006410 | prose | pages [16] -->
m

<!-- b006411 | prose | pages [16] -->
m

<!-- b006412 | prose | pages [16] -->
m

<!-- b006413 | prose | pages [16] -->
m

<!-- b006414 | prose | pages [16] -->
m

<!-- b006415 | prose | pages [16] -->
m

<!-- b006416 | prose | pages [16] -->
m

<!-- b006417 | prose | pages [16] -->
m

<!-- b006418 | prose | pages [16] -->
m

<!-- b006419 | prose | pages [16] -->
m

<!-- b006420 | prose | pages [16] -->
m

<!-- b006421 | prose | pages [16] -->
m

<!-- b006422 | prose | pages [16] -->
m

<!-- b006423 | prose | pages [16] -->
m

<!-- b006424 | prose | pages [16] -->
m

<!-- b006425 | prose | pages [16] -->
m

<!-- b006426 | prose | pages [16] -->
m

<!-- b006427 | prose | pages [16] -->
m

<!-- b006428 | prose | pages [16] -->
m

<!-- b006429 | prose | pages [16] -->
m

<!-- b006430 | prose | pages [16] -->
m

<!-- b006431 | prose | pages [16] -->
m

<!-- b006432 | prose | pages [16] -->
m

<!-- b006433 | prose | pages [16] -->
m

<!-- b006434 | prose | pages [16] -->
m

<!-- b006435 | prose | pages [16] -->
m

<!-- b006436 | prose | pages [16] -->
m

<!-- b006437 | prose | pages [16] -->
m

<!-- b006438 | prose | pages [16] -->
m

<!-- b006439 | prose | pages [16] -->
m

<!-- b006440 | prose | pages [16] -->
m

<!-- b006441 | prose | pages [16] -->
m

<!-- b006442 | prose | pages [16] -->
m

<!-- b006443 | prose | pages [16] -->
m

<!-- b006444 | prose | pages [16] -->
• USA: Swimming (IS = 39.8) and Basketball (IS = 27.8) remain priorities.

<!-- b006445 | prose | pages [16] -->
m

<!-- b006446 | prose | pages [16] -->
m

<!-- b006447 | prose | pages [16] -->
m

<!-- b006448 | prose | pages [16] -->
m

<!-- b006449 | prose | pages [16] -->
m

<!-- b006450 | prose | pages [16] -->
m

<!-- b006451 | prose | pages [16] -->
m

<!-- b006452 | prose | pages [16] -->
m

<!-- b006453 | prose | pages [16] -->
m

<!-- b006454 | prose | pages [16] -->
m

<!-- b006455 | prose | pages [16] -->
m

<!-- b006456 | prose | pages [16] -->
m

<!-- b006457 | prose | pages [16] -->
m

<!-- b006458 | prose | pages [16] -->
m

<!-- b006459 | prose | pages [16] -->
m

<!-- b006460 | prose | pages [16] -->
m

<!-- b006461 | prose | pages [16] -->
m

<!-- b006462 | prose | pages [16] -->
m

<!-- b006463 | prose | pages [16] -->
m

<!-- b006464 | prose | pages [16] -->
m

<!-- b006465 | prose | pages [16] -->
m

<!-- b006466 | prose | pages [16] -->
m

<!-- b006467 | prose | pages [16] -->
m

<!-- b006468 | prose | pages [16] -->
m

<!-- b006469 | prose | pages [16] -->
m

<!-- b006470 | prose | pages [16] -->
m

<!-- b006471 | prose | pages [16] -->
m

<!-- b006472 | prose | pages [16] -->
m

<!-- b006473 | prose | pages [16] -->
m

<!-- b006474 | prose | pages [16] -->
m

<!-- b006475 | prose | pages [16] -->
m

<!-- b006476 | prose | pages [16] -->
m

<!-- b006477 | prose | pages [16] -->
m

<!-- b006478 | prose | pages [16] -->
m

<!-- b006479 | prose | pages [16] -->
m

<!-- b006480 | prose | pages [16] -->
m

<!-- b006481 | prose | pages [16] -->
m

<!-- b006482 | prose | pages [16] -->
m

<!-- b006483 | prose | pages [16] -->
m

<!-- b006484 | prose | pages [16] -->
m

<!-- b006485 | prose | pages [16] -->
m

<!-- b006486 | prose | pages [16] -->
m

<!-- b006487 | prose | pages [16] -->
m

<!-- b006488 | prose | pages [16] -->
m

<!-- b006489 | prose | pages [16] -->
m

<!-- b006490 | prose | pages [16] -->
m

<!-- b006491 | prose | pages [16] -->
m

<!-- b006492 | prose | pages [16] -->
m

<!-- b006493 | prose | pages [16] -->
m

<!-- b006494 | prose | pages [16] -->
m

<!-- b006495 | prose | pages [16] -->
m

<!-- b006496 | prose | pages [16] -->
m

<!-- b006497 | prose | pages [16] -->
m

<!-- b006498 | prose | pages [16] -->
m

<!-- b006499 | prose | pages [16] -->
m

<!-- b006500 | prose | pages [16] -->
m

<!-- b006501 | prose | pages [16] -->
m

<!-- b006502 | prose | pages [16] -->
m

<!-- b006503 | prose | pages [16] -->
m

<!-- b006504 | prose | pages [16] -->
m

<!-- b006505 | prose | pages [16] -->
m

<!-- b006506 | prose | pages [16] -->
m

<!-- b006507 | prose | pages [16] -->
m

<!-- b006508 | prose | pages [16] -->
m

<!-- b006509 | prose | pages [16] -->
m

<!-- b006510 | prose | pages [16] -->
m

<!-- b006511 | prose | pages [16] -->
m

<!-- b006512 | prose | pages [16] -->
m

<!-- b006513 | prose | pages [16] -->
m

<!-- b006514 | prose | pages [16] -->
m

<!-- b006515 | prose | pages [16] -->
m

<!-- b006516 | prose | pages [16] -->
m

<!-- b006517 | prose | pages [16] -->
m

<!-- b006518 | prose | pages [16] -->
m

<!-- b006519 | prose | pages [16] -->
m

<!-- b006520 | prose | pages [16] -->
m

<!-- b006521 | prose | pages [16] -->
m

<!-- b006522 | prose | pages [16] -->
m

<!-- b006523 | prose | pages [16] -->
m

<!-- b006524 | prose | pages [16] -->
m

<!-- b006525 | prose | pages [16] -->
m

<!-- b006526 | prose | pages [16] -->
m

<!-- b006527 | prose | pages [16] -->
m

<!-- b006528 | prose | pages [16] -->
m

<!-- b006529 | prose | pages [16] -->
m

<!-- b006530 | prose | pages [16] -->
m

<!-- b006531 | prose | pages [16] -->
m

<!-- b006532 | prose | pages [16] -->
m

<!-- b006533 | prose | pages [16] -->
m

<!-- b006534 | prose | pages [16] -->
m

<!-- b006535 | prose | pages [16] -->
m

<!-- b006536 | prose | pages [16] -->
m

<!-- b006537 | prose | pages [16] -->
m

<!-- b006538 | prose | pages [16] -->
m

<!-- b006539 | prose | pages [16] -->
m

<!-- b006540 | prose | pages [16] -->
m

<!-- b006541 | prose | pages [16] -->
m

<!-- b006542 | prose | pages [16] -->
m

<!-- b006543 | prose | pages [16] -->
m

<!-- b006544 | prose | pages [16] -->
m

<!-- b006545 | prose | pages [16] -->
m

<!-- b006546 | prose | pages [16] -->
m

<!-- b006547 | prose | pages [16] -->
m

<!-- b006548 | prose | pages [16] -->
m

<!-- b006549 | prose | pages [16] -->
m

<!-- b006550 | prose | pages [16] -->
m

<!-- b006551 | prose | pages [16] -->
m

<!-- b006552 | prose | pages [16] -->
m

<!-- b006553 | prose | pages [16] -->
m

<!-- b006554 | prose | pages [16] -->
m

<!-- b006555 | prose | pages [16] -->
m

<!-- b006556 | prose | pages [16] -->
m

<!-- b006557 | prose | pages [16] -->
m

<!-- b006558 | prose | pages [16] -->
m

<!-- b006559 | prose | pages [16] -->
m

<!-- b006560 | prose | pages [16] -->
m

<!-- b006561 | prose | pages [16] -->
m

<!-- b006562 | prose | pages [16] -->
m

<!-- b006563 | prose | pages [16] -->
m

<!-- b006564 | prose | pages [16] -->
m

<!-- b006565 | prose | pages [16] -->
m

<!-- b006566 | prose | pages [16] -->
m

<!-- b006567 | prose | pages [16] -->
m

<!-- b006568 | prose | pages [16] -->
m

<!-- b006569 | prose | pages [16] -->
m

<!-- b006570 | prose | pages [16] -->
m

<!-- b006571 | prose | pages [16] -->
m

<!-- b006572 | prose | pages [16] -->
m

<!-- b006573 | prose | pages [16] -->
m

<!-- b006574 | prose | pages [16] -->
m

<!-- b006575 | prose | pages [16] -->
m

<!-- b006576 | prose | pages [16] -->
m

<!-- b006577 | prose | pages [16] -->
m

<!-- b006578 | prose | pages [16] -->
m

<!-- b006579 | prose | pages [16] -->
m

<!-- b006580 | prose | pages [16] -->
m

<!-- b006581 | prose | pages [16] -->
m

<!-- b006582 | prose | pages [16] -->
m

<!-- b006583 | prose | pages [16] -->
m

<!-- b006584 | prose | pages [16] -->
m

<!-- b006585 | prose | pages [16] -->
m

<!-- b006586 | prose | pages [16] -->
m

<!-- b006587 | prose | pages [16] -->
m

<!-- b006588 | prose | pages [16] -->
m

<!-- b006589 | prose | pages [16] -->
m

<!-- b006590 | prose | pages [16] -->
m

<!-- b006591 | prose | pages [16] -->
m

<!-- b006592 | prose | pages [16] -->
m

<!-- b006593 | prose | pages [16] -->
m

<!-- b006594 | prose | pages [16] -->
m

<!-- b006595 | prose | pages [16] -->
m

<!-- b006596 | prose | pages [16] -->
m

<!-- b006597 | prose | pages [16] -->
m

<!-- b006598 | prose | pages [16] -->
m

<!-- b006599 | prose | pages [16] -->
m

<!-- b006600 | prose | pages [16] -->
m

<!-- b006601 | prose | pages [16] -->
m

<!-- b006602 | prose | pages [16] -->
m

<!-- b006603 | prose | pages [16] -->
m

<!-- b006604 | prose | pages [16] -->
m

<!-- b006605 | prose | pages [16] -->
m

<!-- b006606 | prose | pages [16] -->
m

<!-- b006607 | prose | pages [16] -->
m

<!-- b006608 | prose | pages [16] -->
m

<!-- b006609 | prose | pages [16] -->
m

<!-- b006610 | prose | pages [16] -->
m

<!-- b006611 | prose | pages [16] -->
m

<!-- b006612 | prose | pages [16] -->
m

<!-- b006613 | prose | pages [16] -->
m

<!-- b006614 | prose | pages [16] -->
m

<!-- b006615 | prose | pages [16] -->
m

<!-- b006616 | prose | pages [16] -->
关注数学模型

<!-- b006617 | furniture | pages [16] -->
2

<!-- b006618 | furniture | pages [16] -->
MATHmodels

<!-- b006619 | furniture | pages [16] -->
获取更多资讯

<!-- b006620 | furniture | pages [19] -->
Team # 2503389

<!-- b006621 | furniture | pages [19] -->
Page 19 of 26

<!-- b006622 | prose | pages [19] -->
MedalCounts = β0 + β1 · Year + β2 · is_great_coach + β3 · (is_great_coach × Year) + ϵ

<!-- b006623 | prose | pages [19] -->
微信公众号：数学模型

<!-- b006624 | prose | pages [19] -->
Key Steps in the Analysis:

<!-- b006625 | heading | pages [19] -->
1. Time Period Division: Divide the Olympic data into three periods based on the coaching

<!-- b006626 | prose | pages [19] -->
situation:

<!-- b006627 | prose | pages [19] -->
• Pre-coaching: The three Olympic Games before the coach took over.

<!-- b006628 | prose | pages [19] -->
• Coaching Period: The period during which the great coach was actively coaching.

<!-- b006629 | prose | pages [19] -->
• Post-coaching: The period after the coach left.

<!-- b006630 | prose | pages [19] -->
微信号：MATHmodels

<!-- b006631 | heading | pages [19] -->
2. Metric Calculation:

<!-- b006632 | prose | pages [19] -->
• Medal Score: Averaged by country and event.

<!-- b006633 | prose | pages [19] -->
• Total Medals: Summed by country and event.

<!-- b006634 | heading | pages [19] -->
3. Model Fitting and Robustness Check: Use the breakpoint regression model to assess

<!-- b006635 | prose | pages [19] -->
the impact of the Great Coach on medal counts. Test the significance of the interaction term coefficient (β3) to determine whether the coach effect varies with years. Then, re- place the dependent variable with “medal score” and refit the model. Finally, compare results across different countries and events.

<!-- b006636 | prose | pages [19] -->
Case Study Analysis (Focusing on Three Key Sports) 8.4

<!-- b006637 | prose | pages [19] -->
8.4.1

<!-- b006638 | heading | pages [19] -->
Introduction:3 Representative Case

<!-- b006639 | prose | pages [19] -->
To analyze the “great coach” effect on medal counts, we analyzed data on medal changes and identified three representative countries aligned with its :

<!-- b006640 | prose | pages [19] -->
Country Sport Coach Artistic Swimming China United Kingdom Cycling Keiko Kageyama Dave Brailsford Women’s Gymnastics United States Béla and Marta Károlyi

<!-- b006641 | caption | pages [19] -->
Table 10: Countries, Sports, and Corresponding Coaches

<!-- b006642 | prose | pages [19] -->
8.4.2

<!-- b006643 | heading | pages [19] -->
Results Analysis

<!-- b006644 | prose | pages [19] -->
To quantify the impact of exceptional coaches on medal counts, we calculated the contribution value (Ci) for each coach using the following formula:

<!-- b006645 | prose | pages [19] -->
Ci = βi

<!-- b006646 | prose | pages [19] -->
where:

<!-- b006647 | prose | pages [19] -->
Di

<!-- b006648 | prose | pages [19] -->
• βi: The direct effect of the coach on medal counts (regression coefficient).

<!-- b006649 | furniture | pages [20] -->
Team # 2503389

<!-- b006650 | furniture | pages [20] -->
Page 20 of 26

<!-- b006651 | prose | pages [20] -->
• Di: The weighted average difference in total medals between the two Olympic Games before and after the coach’s tenure.

<!-- b006652 | prose | pages [20] -->
By analyzing significant changes in medal counts and referencing relevant data, three ex- emplary cases of the ”Great Coach Effect” were identified:

<!-- b006653 | heading | pages [20] -->
1. Béla and Marta Károlyi (USA Women’s Gymnastics): Regression coefficient (βi) =

<!-- b006654 | prose | pages [20] -->
0.3.

<!-- b006655 | heading | pages [20] -->
2. Keiko Kageyama (UK Cycling): Regression coefficient (βi) = 6.9.

<!-- b006656 | heading | pages [20] -->
3. Keiko Kageyama (China Artistic Swimming): Regression coefficient (βi) = 1.3.

<!-- b006657 | prose | pages [20] -->
Using the formula above, the contribution values (Ci) were computed for each coach:

<!-- b006658 | prose | pages [20] -->
0.3 • Béla and Marta Károlyi: Contribution value (Ci) = DUSA = 1.7.

<!-- b006659 | prose | pages [20] -->
6.9 • Keiko Kageyama (UK Cycling): Contribution value (Ci) = DUK = 1.7.

<!-- b006660 | prose | pages [20] -->
1.3 • Keiko Kageyama (China Artistic Swimming): Contribution value (Ci) = DCHN = 1.7.

<!-- b006661 | prose | pages [20] -->
The results demonstrate that despite varying regression coefficients (βi), the adjusted contri- bution values across these cases converge to 1.7. This highlights the consistent and measurable impact of exceptional coaching on improving medal outcomes, offering actionable insights for strategic investments in coaching talent.

<!-- b006662 | caption | pages [20] -->
Figure 11: Caption for Britain

<!-- b006663 | caption | pages [20] -->
Figure 12: Caption for USA

<!-- b006664 | prose | pages [20] -->
m

<!-- b006665 | prose | pages [20] -->
m

<!-- b006666 | prose | pages [20] -->
m

<!-- b006667 | prose | pages [20] -->
m

<!-- b006668 | prose | pages [20] -->
m

<!-- b006669 | prose | pages [20] -->
m

<!-- b006670 | prose | pages [20] -->
m

<!-- b006671 | prose | pages [20] -->
m

<!-- b006672 | prose | pages [20] -->
m

<!-- b006673 | prose | pages [20] -->
m

<!-- b006674 | prose | pages [20] -->
m

<!-- b006675 | prose | pages [20] -->
m

<!-- b006676 | prose | pages [20] -->
m

<!-- b006677 | prose | pages [20] -->
m

<!-- b006678 | prose | pages [20] -->
m

<!-- b006679 | prose | pages [20] -->
m

<!-- b006680 | prose | pages [20] -->
m

<!-- b006681 | prose | pages [20] -->
m

<!-- b006682 | prose | pages [20] -->
m

<!-- b006683 | prose | pages [20] -->
m

<!-- b006684 | prose | pages [20] -->
m

<!-- b006685 | prose | pages [20] -->
m

<!-- b006686 | prose | pages [20] -->
m

<!-- b006687 | prose | pages [20] -->
m

<!-- b006688 | prose | pages [20] -->
m

<!-- b006689 | prose | pages [20] -->
m

<!-- b006690 | prose | pages [20] -->
m

<!-- b006691 | prose | pages [20] -->
m

<!-- b006692 | prose | pages [20] -->
m

<!-- b006693 | prose | pages [20] -->
m

<!-- b006694 | prose | pages [20] -->
m

<!-- b006695 | prose | pages [20] -->
m

<!-- b006696 | prose | pages [20] -->
m

<!-- b006697 | prose | pages [20] -->
m

<!-- b006698 | prose | pages [20] -->
m

<!-- b006699 | prose | pages [20] -->
m

<!-- b006700 | prose | pages [20] -->
m

<!-- b006701 | prose | pages [20] -->
m

<!-- b006702 | prose | pages [20] -->
m

<!-- b006703 | prose | pages [20] -->
m

<!-- b006704 | prose | pages [20] -->
m

<!-- b006705 | prose | pages [20] -->
m

<!-- b006706 | prose | pages [20] -->
m

<!-- b006707 | prose | pages [20] -->
m

<!-- b006708 | prose | pages [20] -->
m

<!-- b006709 | prose | pages [20] -->
m

<!-- b006710 | prose | pages [20] -->
m

<!-- b006711 | prose | pages [20] -->
m

<!-- b006712 | prose | pages [20] -->
m

<!-- b006713 | prose | pages [20] -->
m

<!-- b006714 | prose | pages [20] -->
m

<!-- b006715 | prose | pages [20] -->
m

<!-- b006716 | prose | pages [20] -->
m

<!-- b006717 | prose | pages [20] -->
m

<!-- b006718 | prose | pages [20] -->
m

<!-- b006719 | prose | pages [20] -->
m

<!-- b006720 | prose | pages [20] -->
m

<!-- b006721 | prose | pages [20] -->
m

<!-- b006722 | prose | pages [20] -->
m

<!-- b006723 | prose | pages [20] -->
m

<!-- b006724 | prose | pages [20] -->
m

<!-- b006725 | prose | pages [20] -->
m

<!-- b006726 | prose | pages [20] -->
m

<!-- b006727 | prose | pages [20] -->
m

<!-- b006728 | prose | pages [20] -->
m

<!-- b006729 | prose | pages [20] -->
m

<!-- b006730 | prose | pages [20] -->
m

<!-- b006731 | prose | pages [20] -->
m

<!-- b006732 | prose | pages [20] -->
m

<!-- b006733 | prose | pages [20] -->
m

<!-- b006734 | prose | pages [20] -->
m

<!-- b006735 | prose | pages [20] -->
m

<!-- b006736 | prose | pages [20] -->
m

<!-- b006737 | prose | pages [20] -->
m

<!-- b006738 | prose | pages [20] -->
m

<!-- b006739 | prose | pages [20] -->
m

<!-- b006740 | prose | pages [20] -->
m

<!-- b006741 | prose | pages [20] -->
m

<!-- b006742 | prose | pages [20] -->
m

<!-- b006743 | prose | pages [20] -->
m

<!-- b006744 | prose | pages [20] -->
m

<!-- b006745 | prose | pages [20] -->
m

<!-- b006746 | prose | pages [20] -->
m

<!-- b006747 | prose | pages [20] -->
m

<!-- b006748 | prose | pages [20] -->
m

<!-- b006749 | prose | pages [20] -->
m

<!-- b006750 | prose | pages [20] -->
m

<!-- b006751 | prose | pages [20] -->
m

<!-- b006752 | prose | pages [20] -->
m

<!-- b006753 | prose | pages [20] -->
m

<!-- b006754 | prose | pages [20] -->
m

<!-- b006755 | prose | pages [20] -->
m

<!-- b006756 | prose | pages [20] -->
m

<!-- b006757 | prose | pages [20] -->
m

<!-- b006758 | prose | pages [20] -->
m

<!-- b006759 | prose | pages [20] -->
m

<!-- b006760 | prose | pages [20] -->
m

<!-- b006761 | prose | pages [20] -->
m

<!-- b006762 | prose | pages [20] -->
m

<!-- b006763 | prose | pages [20] -->
m

<!-- b006764 | prose | pages [20] -->
m

<!-- b006765 | prose | pages [20] -->
m

<!-- b006766 | prose | pages [20] -->
m

<!-- b006767 | prose | pages [20] -->
m

<!-- b006768 | prose | pages [20] -->
m

<!-- b006769 | prose | pages [20] -->
m

<!-- b006770 | prose | pages [20] -->
m

<!-- b006771 | prose | pages [20] -->
m

<!-- b006772 | prose | pages [20] -->
m

<!-- b006773 | prose | pages [20] -->
m

<!-- b006774 | prose | pages [20] -->
m

<!-- b006775 | prose | pages [20] -->
m

<!-- b006776 | prose | pages [20] -->
m

<!-- b006777 | prose | pages [20] -->
m

<!-- b006778 | prose | pages [20] -->
m

<!-- b006779 | prose | pages [20] -->
m

<!-- b006780 | prose | pages [20] -->
m

<!-- b006781 | prose | pages [20] -->
m

<!-- b006782 | prose | pages [20] -->
m

<!-- b006783 | prose | pages [20] -->
m

<!-- b006784 | prose | pages [20] -->
m

<!-- b006785 | prose | pages [20] -->
m

<!-- b006786 | prose | pages [20] -->
m

<!-- b006787 | prose | pages [20] -->
m

<!-- b006788 | prose | pages [20] -->
m

<!-- b006789 | prose | pages [20] -->
m

<!-- b006790 | prose | pages [20] -->
m

<!-- b006791 | prose | pages [20] -->
m

<!-- b006792 | prose | pages [20] -->
m

<!-- b006793 | prose | pages [20] -->
m

<!-- b006794 | prose | pages [20] -->
m

<!-- b006795 | prose | pages [20] -->
m

<!-- b006796 | prose | pages [20] -->
m

<!-- b006797 | prose | pages [20] -->
m

<!-- b006798 | prose | pages [20] -->
m

<!-- b006799 | prose | pages [20] -->
m

<!-- b006800 | prose | pages [20] -->
m

<!-- b006801 | prose | pages [20] -->
m

<!-- b006802 | prose | pages [20] -->
m

<!-- b006803 | prose | pages [20] -->
m

<!-- b006804 | prose | pages [20] -->
m

<!-- b006805 | prose | pages [20] -->
m

<!-- b006806 | prose | pages [20] -->
m

<!-- b006807 | prose | pages [20] -->
m

<!-- b006808 | prose | pages [20] -->
m

<!-- b006809 | prose | pages [20] -->
m

<!-- b006810 | prose | pages [20] -->
m

<!-- b006811 | prose | pages [20] -->
m

<!-- b006812 | prose | pages [20] -->
m

<!-- b006813 | prose | pages [20] -->
m

<!-- b006814 | prose | pages [20] -->
m

<!-- b006815 | prose | pages [20] -->
m

<!-- b006816 | prose | pages [20] -->
m

<!-- b006817 | prose | pages [20] -->
m

<!-- b006818 | prose | pages [20] -->
m

<!-- b006819 | prose | pages [20] -->
m

<!-- b006820 | prose | pages [20] -->
m

<!-- b006821 | prose | pages [20] -->
m

<!-- b006822 | prose | pages [20] -->
m

<!-- b006823 | prose | pages [20] -->
m

<!-- b006824 | prose | pages [20] -->
m

<!-- b006825 | prose | pages [20] -->
m

<!-- b006826 | prose | pages [20] -->
m

<!-- b006827 | prose | pages [20] -->
m

<!-- b006828 | prose | pages [20] -->
m

<!-- b006829 | prose | pages [20] -->
m

<!-- b006830 | prose | pages [20] -->
m

<!-- b006831 | prose | pages [20] -->
m

<!-- b006832 | prose | pages [20] -->
m

<!-- b006833 | prose | pages [20] -->
m

<!-- b006834 | prose | pages [20] -->
m

<!-- b006835 | prose | pages [20] -->
m

<!-- b006836 | prose | pages [20] -->
m

<!-- b006837 | prose | pages [20] -->
m

<!-- b006838 | prose | pages [20] -->
m

<!-- b006839 | prose | pages [20] -->
m

<!-- b006840 | prose | pages [20] -->
m

<!-- b006841 | prose | pages [20] -->
m

<!-- b006842 | prose | pages [20] -->
m

<!-- b006843 | prose | pages [20] -->
m

<!-- b006844 | prose | pages [20] -->
m

<!-- b006845 | prose | pages [20] -->
m

<!-- b006846 | prose | pages [20] -->
m

<!-- b006847 | prose | pages [20] -->
m

<!-- b006848 | prose | pages [20] -->
m

<!-- b006849 | prose | pages [20] -->
m

<!-- b006850 | prose | pages [20] -->
m

<!-- b006851 | prose | pages [20] -->
m

<!-- b006852 | prose | pages [20] -->
m

<!-- b006853 | prose | pages [20] -->
m

<!-- b006854 | prose | pages [20] -->
m

<!-- b006855 | prose | pages [20] -->
m

<!-- b006856 | prose | pages [20] -->
m

<!-- b006857 | prose | pages [20] -->
m

<!-- b006858 | prose | pages [20] -->
m

<!-- b006859 | prose | pages [20] -->
m

<!-- b006860 | prose | pages [20] -->
m

<!-- b006861 | prose | pages [20] -->
m

<!-- b006862 | prose | pages [20] -->
m

<!-- b006863 | prose | pages [20] -->
m

<!-- b006864 | prose | pages [20] -->
m

<!-- b006865 | prose | pages [20] -->
m

<!-- b006866 | prose | pages [20] -->
m

<!-- b006867 | prose | pages [20] -->
m

<!-- b006868 | prose | pages [20] -->
m

<!-- b006869 | prose | pages [20] -->
m

<!-- b006870 | prose | pages [20] -->
m

<!-- b006871 | prose | pages [20] -->
m

<!-- b006872 | prose | pages [20] -->
m

<!-- b006873 | prose | pages [20] -->
m

<!-- b006874 | prose | pages [20] -->
m

<!-- b006875 | prose | pages [20] -->
m

<!-- b006876 | prose | pages [20] -->
m

<!-- b006877 | prose | pages [20] -->
m

<!-- b006878 | prose | pages [20] -->
m

<!-- b006879 | prose | pages [20] -->
m

<!-- b006880 | prose | pages [20] -->
m

<!-- b006881 | prose | pages [20] -->
m

<!-- b006882 | prose | pages [20] -->
m

<!-- b006883 | prose | pages [20] -->
m

<!-- b006884 | prose | pages [20] -->
m

<!-- b006885 | prose | pages [20] -->
m

<!-- b006886 | prose | pages [20] -->
m

<!-- b006887 | prose | pages [20] -->
m

<!-- b006888 | prose | pages [20] -->
m

<!-- b006889 | prose | pages [20] -->
m

<!-- b006890 | prose | pages [20] -->
m

<!-- b006891 | prose | pages [20] -->
m

<!-- b006892 | prose | pages [20] -->
m

<!-- b006893 | prose | pages [20] -->
m

<!-- b006894 | prose | pages [20] -->
m

<!-- b006895 | prose | pages [20] -->
m

<!-- b006896 | prose | pages [20] -->
m

<!-- b006897 | prose | pages [20] -->
m

<!-- b006898 | prose | pages [20] -->
m

<!-- b006899 | prose | pages [20] -->
m

<!-- b006900 | prose | pages [20] -->
m

<!-- b006901 | prose | pages [20] -->
m

<!-- b006902 | prose | pages [20] -->
m

<!-- b006903 | prose | pages [20] -->
m

<!-- b006904 | prose | pages [20] -->
m

<!-- b006905 | prose | pages [20] -->
m

<!-- b006906 | prose | pages [20] -->
m

<!-- b006907 | prose | pages [20] -->
m

<!-- b006908 | prose | pages [20] -->
m

<!-- b006909 | prose | pages [20] -->
m

<!-- b006910 | prose | pages [20] -->
m

<!-- b006911 | prose | pages [20] -->
m

<!-- b006912 | prose | pages [20] -->
m

<!-- b006913 | prose | pages [20] -->
m

<!-- b006914 | prose | pages [20] -->
m

<!-- b006915 | prose | pages [20] -->
m

<!-- b006916 | prose | pages [20] -->
m

<!-- b006917 | prose | pages [20] -->
m

<!-- b006918 | prose | pages [20] -->
m

<!-- b006919 | prose | pages [20] -->
m

<!-- b006920 | prose | pages [20] -->
m

<!-- b006921 | prose | pages [20] -->
m

<!-- b006922 | prose | pages [20] -->
m

<!-- b006923 | prose | pages [20] -->
m

<!-- b006924 | prose | pages [20] -->
m

<!-- b006925 | prose | pages [20] -->
m

<!-- b006926 | prose | pages [20] -->
m

<!-- b006927 | prose | pages [20] -->
m

<!-- b006928 | prose | pages [20] -->
m

<!-- b006929 | prose | pages [20] -->
m

<!-- b006930 | prose | pages [20] -->
m

<!-- b006931 | prose | pages [20] -->
m

<!-- b006932 | prose | pages [20] -->
m

<!-- b006933 | prose | pages [20] -->
m

<!-- b006934 | prose | pages [20] -->
m

<!-- b006935 | prose | pages [20] -->
m

<!-- b006936 | prose | pages [20] -->
m

<!-- b006937 | prose | pages [20] -->
m

<!-- b006938 | prose | pages [20] -->
m

<!-- b006939 | prose | pages [20] -->
m

<!-- b006940 | prose | pages [20] -->
m

<!-- b006941 | prose | pages [20] -->
m

<!-- b006942 | prose | pages [20] -->
m

<!-- b006943 | prose | pages [20] -->
m

<!-- b006944 | prose | pages [20] -->
m

<!-- b006945 | prose | pages [20] -->
m

<!-- b006946 | prose | pages [20] -->
m

<!-- b006947 | prose | pages [20] -->
m

<!-- b006948 | prose | pages [20] -->
m

<!-- b006949 | prose | pages [20] -->
m

<!-- b006950 | prose | pages [20] -->
m

<!-- b006951 | prose | pages [20] -->
m

<!-- b006952 | prose | pages [20] -->
m

<!-- b006953 | prose | pages [20] -->
m

<!-- b006954 | prose | pages [20] -->
m

<!-- b006955 | prose | pages [20] -->
m

<!-- b006956 | prose | pages [20] -->
m

<!-- b006957 | prose | pages [20] -->
m

<!-- b006958 | prose | pages [20] -->
m

<!-- b006959 | prose | pages [20] -->
m

<!-- b006960 | prose | pages [20] -->
m

<!-- b006961 | prose | pages [20] -->
m

<!-- b006962 | prose | pages [20] -->
m

<!-- b006963 | prose | pages [20] -->
m

<!-- b006964 | prose | pages [20] -->
m

<!-- b006965 | prose | pages [20] -->
m

<!-- b006966 | prose | pages [20] -->
m

<!-- b006967 | prose | pages [20] -->
m

<!-- b006968 | prose | pages [20] -->
m

<!-- b006969 | prose | pages [20] -->
m

<!-- b006970 | prose | pages [20] -->
m

<!-- b006971 | prose | pages [20] -->
m

<!-- b006972 | prose | pages [20] -->
m

<!-- b006973 | prose | pages [20] -->
m

<!-- b006974 | prose | pages [20] -->
m

<!-- b006975 | prose | pages [20] -->
m

<!-- b006976 | prose | pages [20] -->
m

<!-- b006977 | prose | pages [20] -->
m

<!-- b006978 | prose | pages [20] -->
m

<!-- b006979 | prose | pages [20] -->
m

<!-- b006980 | prose | pages [20] -->
m

<!-- b006981 | prose | pages [20] -->
m

<!-- b006982 | prose | pages [20] -->
m

<!-- b006983 | prose | pages [20] -->
m

<!-- b006984 | prose | pages [20] -->
m

<!-- b006985 | prose | pages [20] -->
m

<!-- b006986 | prose | pages [20] -->
m

<!-- b006987 | prose | pages [20] -->
m

<!-- b006988 | prose | pages [20] -->
m

<!-- b006989 | prose | pages [20] -->
m

<!-- b006990 | prose | pages [20] -->
m

<!-- b006991 | prose | pages [20] -->
m

<!-- b006992 | prose | pages [20] -->
m

<!-- b006993 | prose | pages [20] -->
m

<!-- b006994 | prose | pages [20] -->
m

<!-- b006995 | prose | pages [20] -->
m

<!-- b006996 | prose | pages [20] -->
m

<!-- b006997 | prose | pages [20] -->
m

<!-- b006998 | prose | pages [20] -->
m

<!-- b006999 | prose | pages [20] -->
m

<!-- b007000 | prose | pages [20] -->
m

<!-- b007001 | prose | pages [20] -->
m

<!-- b007002 | prose | pages [20] -->
m

<!-- b007003 | prose | pages [20] -->
m

<!-- b007004 | prose | pages [20] -->
m

<!-- b007005 | prose | pages [20] -->
m

<!-- b007006 | prose | pages [20] -->
m

<!-- b007007 | prose | pages [20] -->
m

<!-- b007008 | prose | pages [20] -->
m

<!-- b007009 | prose | pages [20] -->
m

<!-- b007010 | prose | pages [20] -->
m

<!-- b007011 | prose | pages [20] -->
m

<!-- b007012 | prose | pages [20] -->
m

<!-- b007013 | prose | pages [20] -->
m

<!-- b007014 | prose | pages [20] -->
m

<!-- b007015 | prose | pages [20] -->
m

<!-- b007016 | prose | pages [20] -->
m

<!-- b007017 | prose | pages [20] -->
m

<!-- b007018 | prose | pages [20] -->
m

<!-- b007019 | prose | pages [20] -->
m

<!-- b007020 | prose | pages [20] -->
m

<!-- b007021 | prose | pages [20] -->
m

<!-- b007022 | prose | pages [20] -->
m

<!-- b007023 | prose | pages [20] -->
m

<!-- b007024 | prose | pages [20] -->
m

<!-- b007025 | prose | pages [20] -->
m

<!-- b007026 | prose | pages [20] -->
m

<!-- b007027 | prose | pages [20] -->
m

<!-- b007028 | prose | pages [20] -->
m

<!-- b007029 | prose | pages [20] -->
m

<!-- b007030 | prose | pages [20] -->
m

<!-- b007031 | prose | pages [20] -->
m

<!-- b007032 | prose | pages [20] -->
m

<!-- b007033 | prose | pages [20] -->
m

<!-- b007034 | prose | pages [20] -->
m

<!-- b007035 | prose | pages [20] -->
m

<!-- b007036 | prose | pages [20] -->
m

<!-- b007037 | prose | pages [20] -->
m

<!-- b007038 | prose | pages [20] -->
m

<!-- b007039 | prose | pages [20] -->
m

<!-- b007040 | prose | pages [20] -->
m

<!-- b007041 | prose | pages [20] -->
m

<!-- b007042 | prose | pages [20] -->
m

<!-- b007043 | prose | pages [20] -->
m

<!-- b007044 | prose | pages [20] -->
m

<!-- b007045 | prose | pages [20] -->
m

<!-- b007046 | prose | pages [20] -->
m

<!-- b007047 | prose | pages [20] -->
m

<!-- b007048 | prose | pages [20] -->
m

<!-- b007049 | prose | pages [20] -->
m

<!-- b007050 | prose | pages [20] -->
m

<!-- b007051 | prose | pages [20] -->
m

<!-- b007052 | prose | pages [20] -->
m

<!-- b007053 | prose | pages [20] -->
m

<!-- b007054 | prose | pages [20] -->
m

<!-- b007055 | prose | pages [20] -->
m

<!-- b007056 | prose | pages [20] -->
m

<!-- b007057 | prose | pages [20] -->
m

<!-- b007058 | prose | pages [20] -->
m

<!-- b007059 | prose | pages [20] -->
m

<!-- b007060 | prose | pages [20] -->
m

<!-- b007061 | prose | pages [20] -->
m

<!-- b007062 | prose | pages [20] -->
m

<!-- b007063 | prose | pages [20] -->
m

<!-- b007064 | prose | pages [20] -->
m

<!-- b007065 | prose | pages [20] -->
m

<!-- b007066 | prose | pages [20] -->
m

<!-- b007067 | prose | pages [20] -->
m

<!-- b007068 | prose | pages [20] -->
m

<!-- b007069 | prose | pages [20] -->
m

<!-- b007070 | prose | pages [20] -->
m

<!-- b007071 | prose | pages [20] -->
m

<!-- b007072 | prose | pages [20] -->
m

<!-- b007073 | prose | pages [20] -->
m

<!-- b007074 | prose | pages [20] -->
m

<!-- b007075 | prose | pages [20] -->
m

<!-- b007076 | prose | pages [20] -->
m

<!-- b007077 | prose | pages [20] -->
m

<!-- b007078 | prose | pages [20] -->
m

<!-- b007079 | prose | pages [20] -->
m

<!-- b007080 | prose | pages [20] -->
m

<!-- b007081 | prose | pages [20] -->
m

<!-- b007082 | prose | pages [20] -->
m

<!-- b007083 | prose | pages [20] -->
m

<!-- b007084 | prose | pages [20] -->
m

<!-- b007085 | prose | pages [20] -->
m

<!-- b007086 | prose | pages [20] -->
m

<!-- b007087 | prose | pages [20] -->
m

<!-- b007088 | prose | pages [20] -->
m

<!-- b007089 | prose | pages [20] -->
m

<!-- b007090 | prose | pages [20] -->
m

<!-- b007091 | prose | pages [20] -->
m

<!-- b007092 | prose | pages [20] -->
m

<!-- b007093 | prose | pages [20] -->
m

<!-- b007094 | prose | pages [20] -->
m

<!-- b007095 | prose | pages [20] -->
m

<!-- b007096 | prose | pages [20] -->
m

<!-- b007097 | prose | pages [20] -->
m

<!-- b007098 | prose | pages [20] -->
m

<!-- b007099 | prose | pages [20] -->
m

<!-- b007100 | prose | pages [20] -->
m

<!-- b007101 | prose | pages [20] -->
m

<!-- b007102 | prose | pages [20] -->
m

<!-- b007103 | prose | pages [20] -->
m

<!-- b007104 | prose | pages [20] -->
m

<!-- b007105 | prose | pages [20] -->
m

<!-- b007106 | prose | pages [20] -->
m

<!-- b007107 | prose | pages [20] -->
m

<!-- b007108 | prose | pages [20] -->
m

<!-- b007109 | prose | pages [20] -->
m

<!-- b007110 | prose | pages [20] -->
m

<!-- b007111 | prose | pages [20] -->
m

<!-- b007112 | prose | pages [20] -->
m

<!-- b007113 | prose | pages [20] -->
m

<!-- b007114 | prose | pages [20] -->
m

<!-- b007115 | prose | pages [20] -->
m

<!-- b007116 | prose | pages [20] -->
m

<!-- b007117 | prose | pages [20] -->
m

<!-- b007118 | prose | pages [20] -->
m

<!-- b007119 | prose | pages [20] -->
m

<!-- b007120 | prose | pages [20] -->
m

<!-- b007121 | prose | pages [20] -->
m

<!-- b007122 | prose | pages [20] -->
m

<!-- b007123 | prose | pages [20] -->
m

<!-- b007124 | prose | pages [20] -->
m

<!-- b007125 | prose | pages [20] -->
m

<!-- b007126 | prose | pages [20] -->
m

<!-- b007127 | prose | pages [20] -->
m

<!-- b007128 | prose | pages [20] -->
m

<!-- b007129 | prose | pages [20] -->
m

<!-- b007130 | prose | pages [20] -->
m

<!-- b007131 | prose | pages [20] -->
m

<!-- b007132 | prose | pages [20] -->
m

<!-- b007133 | prose | pages [20] -->
m

<!-- b007134 | prose | pages [20] -->
m

<!-- b007135 | prose | pages [20] -->
m

<!-- b007136 | prose | pages [20] -->
m

<!-- b007137 | prose | pages [20] -->
m

<!-- b007138 | prose | pages [20] -->
m

<!-- b007139 | prose | pages [20] -->
m

<!-- b007140 | prose | pages [20] -->
m

<!-- b007141 | prose | pages [20] -->
m

<!-- b007142 | prose | pages [20] -->
m

<!-- b007143 | prose | pages [20] -->
m

<!-- b007144 | prose | pages [20] -->
m

<!-- b007145 | prose | pages [20] -->
m

<!-- b007146 | prose | pages [20] -->
m

<!-- b007147 | prose | pages [20] -->
m

<!-- b007148 | prose | pages [20] -->
m

<!-- b007149 | prose | pages [20] -->
m

<!-- b007150 | prose | pages [20] -->
m

<!-- b007151 | prose | pages [20] -->
m

<!-- b007152 | prose | pages [20] -->
m

<!-- b007153 | prose | pages [20] -->
m

<!-- b007154 | prose | pages [20] -->
m

<!-- b007155 | prose | pages [20] -->
m

<!-- b007156 | prose | pages [20] -->
m

<!-- b007157 | prose | pages [20] -->
m

<!-- b007158 | prose | pages [20] -->
m

<!-- b007159 | prose | pages [20] -->
m

<!-- b007160 | prose | pages [20] -->
m

<!-- b007161 | prose | pages [20] -->
m

<!-- b007162 | prose | pages [20] -->
m

<!-- b007163 | prose | pages [20] -->
m

<!-- b007164 | prose | pages [20] -->
m

<!-- b007165 | prose | pages [20] -->
m

<!-- b007166 | prose | pages [20] -->
m

<!-- b007167 | prose | pages [20] -->
m

<!-- b007168 | prose | pages [20] -->
m

<!-- b007169 | prose | pages [20] -->
m

<!-- b007170 | prose | pages [20] -->
m

<!-- b007171 | prose | pages [20] -->
m

<!-- b007172 | prose | pages [20] -->
m

<!-- b007173 | prose | pages [20] -->
m

<!-- b007174 | prose | pages [20] -->
m

<!-- b007175 | prose | pages [20] -->
m

<!-- b007176 | prose | pages [20] -->
m

<!-- b007177 | prose | pages [20] -->
m

<!-- b007178 | prose | pages [20] -->
m

<!-- b007179 | prose | pages [20] -->
m

<!-- b007180 | prose | pages [20] -->
m

<!-- b007181 | prose | pages [20] -->
m

<!-- b007182 | prose | pages [20] -->
m

<!-- b007183 | prose | pages [20] -->
m

<!-- b007184 | prose | pages [20] -->
m

<!-- b007185 | prose | pages [20] -->
m

<!-- b007186 | prose | pages [20] -->
m

<!-- b007187 | prose | pages [20] -->
m

<!-- b007188 | prose | pages [20] -->
m

<!-- b007189 | prose | pages [20] -->
m

<!-- b007190 | prose | pages [20] -->
m

<!-- b007191 | prose | pages [20] -->
m

<!-- b007192 | prose | pages [20] -->
m

<!-- b007193 | prose | pages [20] -->
m

<!-- b007194 | prose | pages [20] -->
m

<!-- b007195 | prose | pages [20] -->
m

<!-- b007196 | prose | pages [20] -->
m

<!-- b007197 | prose | pages [20] -->
m

<!-- b007198 | prose | pages [20] -->
m

<!-- b007199 | prose | pages [20] -->
m

<!-- b007200 | prose | pages [20] -->
m

<!-- b007201 | prose | pages [20] -->
m

<!-- b007202 | prose | pages [20] -->
m

<!-- b007203 | prose | pages [20] -->
m

<!-- b007204 | prose | pages [20] -->
m

<!-- b007205 | prose | pages [20] -->
m

<!-- b007206 | prose | pages [20] -->
m

<!-- b007207 | prose | pages [20] -->
m

<!-- b007208 | prose | pages [20] -->
m

<!-- b007209 | prose | pages [20] -->
m

<!-- b007210 | prose | pages [20] -->
m

<!-- b007211 | prose | pages [20] -->
m

<!-- b007212 | prose | pages [20] -->
m

<!-- b007213 | prose | pages [20] -->
m

<!-- b007214 | prose | pages [20] -->
m

<!-- b007215 | prose | pages [20] -->
m

<!-- b007216 | prose | pages [20] -->
m

<!-- b007217 | prose | pages [20] -->
m

<!-- b007218 | prose | pages [20] -->
m

<!-- b007219 | prose | pages [20] -->
m

<!-- b007220 | prose | pages [20] -->
m

<!-- b007221 | prose | pages [20] -->
m

<!-- b007222 | prose | pages [20] -->
m

<!-- b007223 | prose | pages [20] -->
m

<!-- b007224 | prose | pages [20] -->
m

<!-- b007225 | prose | pages [20] -->
m

<!-- b007226 | prose | pages [20] -->
m

<!-- b007227 | prose | pages [20] -->
m

<!-- b007228 | prose | pages [20] -->
m

<!-- b007229 | prose | pages [20] -->
m

<!-- b007230 | prose | pages [20] -->
m

<!-- b007231 | prose | pages [20] -->
m

<!-- b007232 | prose | pages [20] -->
m

<!-- b007233 | prose | pages [20] -->
m

<!-- b007234 | prose | pages [20] -->
m

<!-- b007235 | prose | pages [20] -->
m

<!-- b007236 | prose | pages [20] -->
m

<!-- b007237 | prose | pages [20] -->
m

<!-- b007238 | prose | pages [20] -->
m

<!-- b007239 | prose | pages [20] -->
m

<!-- b007240 | prose | pages [20] -->
m

<!-- b007241 | prose | pages [20] -->
m

<!-- b007242 | prose | pages [20] -->
m

<!-- b007243 | prose | pages [20] -->
m

<!-- b007244 | prose | pages [20] -->
m

<!-- b007245 | prose | pages [20] -->
m

<!-- b007246 | prose | pages [20] -->
m

<!-- b007247 | prose | pages [20] -->
m

<!-- b007248 | prose | pages [20] -->
m

<!-- b007249 | prose | pages [20] -->
m

<!-- b007250 | prose | pages [20] -->
m

<!-- b007251 | prose | pages [20] -->
m

<!-- b007252 | prose | pages [20] -->
m

<!-- b007253 | prose | pages [20] -->
m

<!-- b007254 | prose | pages [20] -->
m

<!-- b007255 | prose | pages [20] -->
m

<!-- b007256 | prose | pages [20] -->
m

<!-- b007257 | prose | pages [20] -->
m

<!-- b007258 | prose | pages [20] -->
m

<!-- b007259 | prose | pages [20] -->
m

<!-- b007260 | prose | pages [20] -->
m

<!-- b007261 | prose | pages [20] -->
m

<!-- b007262 | prose | pages [20] -->
m

<!-- b007263 | prose | pages [20] -->
m

<!-- b007264 | prose | pages [20] -->
m

<!-- b007265 | prose | pages [20] -->
m

<!-- b007266 | prose | pages [20] -->
m

<!-- b007267 | prose | pages [20] -->
m

<!-- b007268 | prose | pages [20] -->
m

<!-- b007269 | prose | pages [20] -->
m

<!-- b007270 | prose | pages [20] -->
m

<!-- b007271 | prose | pages [20] -->
m

<!-- b007272 | prose | pages [20] -->
m

<!-- b007273 | prose | pages [20] -->
m

<!-- b007274 | prose | pages [20] -->
m

<!-- b007275 | prose | pages [20] -->
m

<!-- b007276 | prose | pages [20] -->
m

<!-- b007277 | prose | pages [20] -->
m

<!-- b007278 | prose | pages [20] -->
m

<!-- b007279 | prose | pages [20] -->
m

<!-- b007280 | prose | pages [20] -->
m

<!-- b007281 | prose | pages [20] -->
m

<!-- b007282 | prose | pages [20] -->
m

<!-- b007283 | prose | pages [20] -->
m

<!-- b007284 | prose | pages [20] -->
m

<!-- b007285 | prose | pages [20] -->
m

<!-- b007286 | prose | pages [20] -->
m

<!-- b007287 | prose | pages [20] -->
m

<!-- b007288 | prose | pages [20] -->
m

<!-- b007289 | prose | pages [20] -->
m

<!-- b007290 | prose | pages [20] -->
m

<!-- b007291 | prose | pages [20] -->
m

<!-- b007292 | prose | pages [20] -->
m

<!-- b007293 | prose | pages [20] -->
m

<!-- b007294 | prose | pages [20] -->
m

<!-- b007295 | prose | pages [20] -->
m

<!-- b007296 | prose | pages [20] -->
m

<!-- b007297 | prose | pages [20] -->
m

<!-- b007298 | prose | pages [20] -->
m

<!-- b007299 | prose | pages [20] -->
m

<!-- b007300 | prose | pages [20] -->
m

<!-- b007301 | prose | pages [20] -->
m

<!-- b007302 | prose | pages [20] -->
m

<!-- b007303 | prose | pages [20] -->
m

<!-- b007304 | prose | pages [20] -->
m

<!-- b007305 | prose | pages [20] -->
m

<!-- b007306 | prose | pages [20] -->
m

<!-- b007307 | prose | pages [20] -->
m

<!-- b007308 | prose | pages [20] -->
m

<!-- b007309 | prose | pages [20] -->
m

<!-- b007310 | prose | pages [20] -->
m

<!-- b007311 | prose | pages [20] -->
m

<!-- b007312 | prose | pages [20] -->
m

<!-- b007313 | prose | pages [20] -->
m

<!-- b007314 | prose | pages [20] -->
m

<!-- b007315 | prose | pages [20] -->
m

<!-- b007316 | prose | pages [20] -->
m

<!-- b007317 | prose | pages [20] -->
m

<!-- b007318 | prose | pages [20] -->
m

<!-- b007319 | prose | pages [20] -->
m

<!-- b007320 | prose | pages [20] -->
m

<!-- b007321 | prose | pages [20] -->
m

<!-- b007322 | prose | pages [20] -->
m

<!-- b007323 | prose | pages [20] -->
m

<!-- b007324 | prose | pages [20] -->
m

<!-- b007325 | prose | pages [20] -->
m

<!-- b007326 | prose | pages [20] -->
m

<!-- b007327 | prose | pages [20] -->
m

<!-- b007328 | prose | pages [20] -->
m

<!-- b007329 | prose | pages [20] -->
m

<!-- b007330 | prose | pages [20] -->
m

<!-- b007331 | prose | pages [20] -->
m

<!-- b007332 | prose | pages [20] -->
m

<!-- b007333 | prose | pages [20] -->
m

<!-- b007334 | prose | pages [20] -->
m

<!-- b007335 | prose | pages [20] -->
m

<!-- b007336 | prose | pages [20] -->
m

<!-- b007337 | prose | pages [20] -->
m

<!-- b007338 | prose | pages [20] -->
m

<!-- b007339 | prose | pages [20] -->
m

<!-- b007340 | prose | pages [20] -->
m

<!-- b007341 | prose | pages [20] -->
m

<!-- b007342 | prose | pages [20] -->
m

<!-- b007343 | prose | pages [20] -->
m

<!-- b007344 | prose | pages [20] -->
m

<!-- b007345 | prose | pages [20] -->
m

<!-- b007346 | prose | pages [20] -->
m

<!-- b007347 | prose | pages [20] -->
m

<!-- b007348 | prose | pages [20] -->
m

<!-- b007349 | prose | pages [20] -->
m

<!-- b007350 | prose | pages [20] -->
m

<!-- b007351 | caption | pages [20] -->
Figure 13: Caption for China

<!-- b007352 | prose | pages [20] -->
关注数学模型

<!-- b007353 | furniture | pages [20] -->
2

<!-- b007354 | furniture | pages [20] -->
MATHmodels

<!-- b007355 | furniture | pages [20] -->
获取更多资讯

<!-- b007356 | furniture | pages [21] -->
Team # 2503389

<!-- b007357 | furniture | pages [21] -->
Page 21 of 26

<!-- b007358 | prose | pages [21] -->
As shown in 11, 12 and 13, the medal count for the sport is analyzed around the appointment of a Great Coach. The red line marks the boundary: to the left are the medal counts before the coach’s appointment, and to the right, after the coach’s appointment until they left the country. The average number of medals post-appointment significantly exceeds pre-appointment counts, illustrating the “Great Coach Effect.”

<!-- b007359 | prose | pages [21] -->
8.4.3 Reasons for Country and Sport Selection

<!-- b007360 | prose | pages [21] -->
The selection of three countries (China, UK, US) and three sports (Artistic Swimming, Cycling, Women’s Gymnastics) creates a framework to represent global sports. It looks at differences in political systems and types of athletics.

<!-- b007361 | prose | pages [21] -->
National Archetypes

<!-- b007362 | prose | pages [21] -->
微信公众号：数学模型

<!-- b007363 | heading | pages [21] -->
• China: Embodies state-centralized athleticism – a model prevalent in 37

<!-- b007364 | prose | pages [21] -->
– Top-down talent identification pipelines

<!-- b007365 | prose | pages [21] -->
– Integrated sports-education-political apparatus

<!-- b007366 | prose | pages [21] -->
– Cultural soft power through medal diplomacy

<!-- b007367 | prose | pages [21] -->
• United Kingdom: Represents technocratic hybrid systems adopted by 28% of developed nations (e.g., Germany, Japan). Defining features:

<!-- b007368 | prose | pages [21] -->
– Public-private R&D consortia (e.g., UK Sport’s “Marginal Gains” program)

<!-- b007369 | prose | pages [21] -->
微信号：MATHmodels

<!-- b007370 | prose | pages [21] -->
– University-based athlete development ecosystems

<!-- b007371 | prose | pages [21] -->
– Precision analytics in training optimization

<!-- b007372 | prose | pages [21] -->
• United States: Exemplifies market-driven pluralism dominant in 35% of Western democ- racies (e.g., Australia, Canada). Characteristics:

<!-- b007373 | prose | pages [21] -->
– Decentralized collegiate sports infrastructure

<!-- b007374 | heading | pages [21] -->
– Commercial sponsorship-driven funding models

<!-- b007375 | prose | pages [21] -->
– Individual athlete brand economies

<!-- b007376 | prose | pages [21] -->
Sport Typology Representation

<!-- b007377 | prose | pages [21] -->
• Artistic Swimming:

<!-- b007378 | prose | pages [21] -->
– Category: Judged team sport (22% of Olympic events)

<!-- b007379 | prose | pages [21] -->
– Analysis Focus: Collective synchronization metrics, subjective scoring biases

<!-- b007380 | prose | pages [21] -->
• Cycling:

<!-- b007381 | prose | pages [21] -->
– Category: Technology-intensive endurance sport (18% of Olympic disciplines)

<!-- b007382 | prose | pages [21] -->
– Analysis Focus: Equipment R&D ROI, aerodynamic efficiency thresholds

<!-- b007383 | prose | pages [21] -->
• Women’s Gymnastics:

<!-- b007384 | prose | pages [21] -->
– Category: Biomechanically complex skill sport (26% of Olympic events)

<!-- b007385 | prose | pages [21] -->
– Analysis Focus: Rule change adaptation rates, injury risk management

<!-- b007386 | prose | pages [21] -->
m

<!-- b007387 | prose | pages [21] -->
m

<!-- b007388 | prose | pages [21] -->
m

<!-- b007389 | prose | pages [21] -->
m

<!-- b007390 | prose | pages [21] -->
m

<!-- b007391 | prose | pages [21] -->
m

<!-- b007392 | prose | pages [21] -->
m

<!-- b007393 | prose | pages [21] -->
m

<!-- b007394 | prose | pages [21] -->
m

<!-- b007395 | prose | pages [21] -->
m

<!-- b007396 | prose | pages [21] -->
m

<!-- b007397 | prose | pages [21] -->
m

<!-- b007398 | prose | pages [21] -->
m

<!-- b007399 | prose | pages [21] -->
m

<!-- b007400 | prose | pages [21] -->
m

<!-- b007401 | prose | pages [21] -->
m

<!-- b007402 | prose | pages [21] -->
m

<!-- b007403 | prose | pages [21] -->
m

<!-- b007404 | prose | pages [21] -->
m

<!-- b007405 | prose | pages [21] -->
m

<!-- b007406 | prose | pages [21] -->
m

<!-- b007407 | prose | pages [21] -->
m

<!-- b007408 | prose | pages [21] -->
m

<!-- b007409 | prose | pages [21] -->
m

<!-- b007410 | prose | pages [21] -->
m

<!-- b007411 | prose | pages [21] -->
m

<!-- b007412 | prose | pages [21] -->
m

<!-- b007413 | prose | pages [21] -->
m

<!-- b007414 | prose | pages [21] -->
m

<!-- b007415 | prose | pages [21] -->
m

<!-- b007416 | prose | pages [21] -->
m

<!-- b007417 | prose | pages [21] -->
m

<!-- b007418 | prose | pages [21] -->
m

<!-- b007419 | prose | pages [21] -->
m

<!-- b007420 | prose | pages [21] -->
m

<!-- b007421 | prose | pages [21] -->
m

<!-- b007422 | prose | pages [21] -->
m

<!-- b007423 | prose | pages [21] -->
m

<!-- b007424 | prose | pages [21] -->
m

<!-- b007425 | prose | pages [21] -->
m

<!-- b007426 | prose | pages [21] -->
m

<!-- b007427 | prose | pages [21] -->
m

<!-- b007428 | prose | pages [21] -->
m

<!-- b007429 | prose | pages [21] -->
m

<!-- b007430 | prose | pages [21] -->
m

<!-- b007431 | prose | pages [21] -->
m

<!-- b007432 | prose | pages [21] -->
m

<!-- b007433 | prose | pages [21] -->
m

<!-- b007434 | prose | pages [21] -->
m

<!-- b007435 | prose | pages [21] -->
m

<!-- b007436 | prose | pages [21] -->
m

<!-- b007437 | prose | pages [21] -->
m

<!-- b007438 | prose | pages [21] -->
m

<!-- b007439 | prose | pages [21] -->
m

<!-- b007440 | prose | pages [21] -->
m

<!-- b007441 | prose | pages [21] -->
m

<!-- b007442 | prose | pages [21] -->
m

<!-- b007443 | prose | pages [21] -->
m

<!-- b007444 | prose | pages [21] -->
m

<!-- b007445 | prose | pages [21] -->
m

<!-- b007446 | prose | pages [21] -->
m

<!-- b007447 | prose | pages [21] -->
m

<!-- b007448 | prose | pages [21] -->
m

<!-- b007449 | prose | pages [21] -->
m

<!-- b007450 | prose | pages [21] -->
m

<!-- b007451 | prose | pages [21] -->
m

<!-- b007452 | prose | pages [21] -->
m

<!-- b007453 | prose | pages [21] -->
m

<!-- b007454 | prose | pages [21] -->
m

<!-- b007455 | prose | pages [21] -->
m

<!-- b007456 | prose | pages [21] -->
m

<!-- b007457 | prose | pages [21] -->
m

<!-- b007458 | prose | pages [21] -->
m

<!-- b007459 | prose | pages [21] -->
m

<!-- b007460 | prose | pages [21] -->
m

<!-- b007461 | prose | pages [21] -->
m

<!-- b007462 | prose | pages [21] -->
m

<!-- b007463 | prose | pages [21] -->
m

<!-- b007464 | prose | pages [21] -->
m

<!-- b007465 | prose | pages [21] -->
m

<!-- b007466 | prose | pages [21] -->
m

<!-- b007467 | prose | pages [21] -->
m

<!-- b007468 | prose | pages [21] -->
m

<!-- b007469 | prose | pages [21] -->
m

<!-- b007470 | prose | pages [21] -->
m

<!-- b007471 | prose | pages [21] -->
m

<!-- b007472 | prose | pages [21] -->
m

<!-- b007473 | prose | pages [21] -->
m

<!-- b007474 | prose | pages [21] -->
m

<!-- b007475 | prose | pages [21] -->
m

<!-- b007476 | prose | pages [21] -->
m

<!-- b007477 | prose | pages [21] -->
m

<!-- b007478 | prose | pages [21] -->
m

<!-- b007479 | prose | pages [21] -->
m

<!-- b007480 | prose | pages [21] -->
m

<!-- b007481 | prose | pages [21] -->
m

<!-- b007482 | prose | pages [21] -->
m

<!-- b007483 | prose | pages [21] -->
m

<!-- b007484 | prose | pages [21] -->
m

<!-- b007485 | prose | pages [21] -->
m

<!-- b007486 | prose | pages [21] -->
m

<!-- b007487 | prose | pages [21] -->
m

<!-- b007488 | prose | pages [21] -->
m

<!-- b007489 | prose | pages [21] -->
m

<!-- b007490 | prose | pages [21] -->
m

<!-- b007491 | prose | pages [21] -->
m

<!-- b007492 | prose | pages [21] -->
m

<!-- b007493 | prose | pages [21] -->
m

<!-- b007494 | prose | pages [21] -->
m

<!-- b007495 | prose | pages [21] -->
m

<!-- b007496 | prose | pages [21] -->
m

<!-- b007497 | prose | pages [21] -->
m

<!-- b007498 | prose | pages [21] -->
m

<!-- b007499 | prose | pages [21] -->
m

<!-- b007500 | prose | pages [21] -->
m

<!-- b007501 | prose | pages [21] -->
m

<!-- b007502 | prose | pages [21] -->
m

<!-- b007503 | prose | pages [21] -->
m

<!-- b007504 | prose | pages [21] -->
m

<!-- b007505 | prose | pages [21] -->
m

<!-- b007506 | prose | pages [21] -->
m

<!-- b007507 | prose | pages [21] -->
m

<!-- b007508 | prose | pages [21] -->
m

<!-- b007509 | prose | pages [21] -->
m

<!-- b007510 | prose | pages [21] -->
m

<!-- b007511 | prose | pages [21] -->
m

<!-- b007512 | prose | pages [21] -->
m

<!-- b007513 | prose | pages [21] -->
m

<!-- b007514 | prose | pages [21] -->
m

<!-- b007515 | prose | pages [21] -->
m

<!-- b007516 | prose | pages [21] -->
m

<!-- b007517 | prose | pages [21] -->
m

<!-- b007518 | prose | pages [21] -->
m

<!-- b007519 | prose | pages [21] -->
m

<!-- b007520 | prose | pages [21] -->
m

<!-- b007521 | prose | pages [21] -->
m

<!-- b007522 | prose | pages [21] -->
m

<!-- b007523 | prose | pages [21] -->
m

<!-- b007524 | prose | pages [21] -->
m

<!-- b007525 | prose | pages [21] -->
m

<!-- b007526 | prose | pages [21] -->
m

<!-- b007527 | prose | pages [21] -->
m

<!-- b007528 | prose | pages [21] -->
m

<!-- b007529 | prose | pages [21] -->
m

<!-- b007530 | prose | pages [21] -->
m

<!-- b007531 | prose | pages [21] -->
m

<!-- b007532 | prose | pages [21] -->
m

<!-- b007533 | prose | pages [21] -->
m

<!-- b007534 | prose | pages [21] -->
m

<!-- b007535 | prose | pages [21] -->
m

<!-- b007536 | prose | pages [21] -->
m

<!-- b007537 | prose | pages [21] -->
m

<!-- b007538 | prose | pages [21] -->
m

<!-- b007539 | prose | pages [21] -->
m

<!-- b007540 | prose | pages [21] -->
m

<!-- b007541 | prose | pages [21] -->
m

<!-- b007542 | prose | pages [21] -->
m

<!-- b007543 | prose | pages [21] -->
m

<!-- b007544 | prose | pages [21] -->
m

<!-- b007545 | prose | pages [21] -->
m

<!-- b007546 | prose | pages [21] -->
m

<!-- b007547 | prose | pages [21] -->
m

<!-- b007548 | prose | pages [21] -->
m

<!-- b007549 | prose | pages [21] -->
m

<!-- b007550 | prose | pages [21] -->
m

<!-- b007551 | prose | pages [21] -->
m

<!-- b007552 | prose | pages [21] -->
m

<!-- b007553 | prose | pages [21] -->
m

<!-- b007554 | prose | pages [21] -->
m

<!-- b007555 | prose | pages [21] -->
m

<!-- b007556 | prose | pages [21] -->
m

<!-- b007557 | prose | pages [21] -->
m

<!-- b007558 | prose | pages [21] -->
m

<!-- b007559 | prose | pages [21] -->
m

<!-- b007560 | prose | pages [21] -->
m

<!-- b007561 | prose | pages [21] -->
m

<!-- b007562 | prose | pages [21] -->
m

<!-- b007563 | prose | pages [21] -->
m

<!-- b007564 | prose | pages [21] -->
m

<!-- b007565 | prose | pages [21] -->
m

<!-- b007566 | prose | pages [21] -->
m

<!-- b007567 | prose | pages [21] -->
m

<!-- b007568 | prose | pages [21] -->
m

<!-- b007569 | prose | pages [21] -->
m

<!-- b007570 | prose | pages [21] -->
m

<!-- b007571 | prose | pages [21] -->
m

<!-- b007572 | prose | pages [21] -->
m

<!-- b007573 | prose | pages [21] -->
m

<!-- b007574 | prose | pages [21] -->
m

<!-- b007575 | prose | pages [21] -->
m

<!-- b007576 | prose | pages [21] -->
m

<!-- b007577 | prose | pages [21] -->
m

<!-- b007578 | prose | pages [21] -->
m

<!-- b007579 | prose | pages [21] -->
m

<!-- b007580 | prose | pages [21] -->
m

<!-- b007581 | prose | pages [21] -->
m

<!-- b007582 | prose | pages [21] -->
m

<!-- b007583 | prose | pages [21] -->
m

<!-- b007584 | prose | pages [21] -->
m

<!-- b007585 | prose | pages [21] -->
m

<!-- b007586 | prose | pages [21] -->
m

<!-- b007587 | prose | pages [21] -->
m

<!-- b007588 | prose | pages [21] -->
m

<!-- b007589 | prose | pages [21] -->
m

<!-- b007590 | prose | pages [21] -->
m

<!-- b007591 | prose | pages [21] -->
m

<!-- b007592 | prose | pages [21] -->
m

<!-- b007593 | prose | pages [21] -->
m

<!-- b007594 | prose | pages [21] -->
m

<!-- b007595 | prose | pages [21] -->
m

<!-- b007596 | prose | pages [21] -->
m

<!-- b007597 | prose | pages [21] -->
m

<!-- b007598 | prose | pages [21] -->
m

<!-- b007599 | prose | pages [21] -->
m

<!-- b007600 | prose | pages [21] -->
m

<!-- b007601 | prose | pages [21] -->
m

<!-- b007602 | prose | pages [21] -->
m

<!-- b007603 | prose | pages [21] -->
m

<!-- b007604 | prose | pages [21] -->
m

<!-- b007605 | prose | pages [21] -->
m

<!-- b007606 | prose | pages [21] -->
m

<!-- b007607 | prose | pages [21] -->
m

<!-- b007608 | prose | pages [21] -->
m

<!-- b007609 | prose | pages [21] -->
m

<!-- b007610 | prose | pages [21] -->
m

<!-- b007611 | prose | pages [21] -->
m

<!-- b007612 | prose | pages [21] -->
m

<!-- b007613 | prose | pages [21] -->
m

<!-- b007614 | prose | pages [21] -->
m

<!-- b007615 | prose | pages [21] -->
m

<!-- b007616 | prose | pages [21] -->
m

<!-- b007617 | prose | pages [21] -->
m

<!-- b007618 | prose | pages [21] -->
m

<!-- b007619 | prose | pages [21] -->
m

<!-- b007620 | prose | pages [21] -->
m

<!-- b007621 | prose | pages [21] -->
m

<!-- b007622 | prose | pages [21] -->
m

<!-- b007623 | prose | pages [21] -->
m

<!-- b007624 | prose | pages [21] -->
m

<!-- b007625 | prose | pages [21] -->
m

<!-- b007626 | prose | pages [21] -->
m

<!-- b007627 | prose | pages [21] -->
m

<!-- b007628 | prose | pages [21] -->
m

<!-- b007629 | prose | pages [21] -->
m

<!-- b007630 | prose | pages [21] -->
m

<!-- b007631 | prose | pages [21] -->
m

<!-- b007632 | prose | pages [21] -->
m

<!-- b007633 | prose | pages [21] -->
m

<!-- b007634 | prose | pages [21] -->
m

<!-- b007635 | prose | pages [21] -->
m

<!-- b007636 | prose | pages [21] -->
m

<!-- b007637 | prose | pages [21] -->
m

<!-- b007638 | prose | pages [21] -->
m

<!-- b007639 | prose | pages [21] -->
m

<!-- b007640 | prose | pages [21] -->
m

<!-- b007641 | prose | pages [21] -->
m

<!-- b007642 | prose | pages [21] -->
m

<!-- b007643 | prose | pages [21] -->
m

<!-- b007644 | prose | pages [21] -->
m

<!-- b007645 | prose | pages [21] -->
m

<!-- b007646 | prose | pages [21] -->
m

<!-- b007647 | prose | pages [21] -->
m

<!-- b007648 | prose | pages [21] -->
m

<!-- b007649 | prose | pages [21] -->
m

<!-- b007650 | prose | pages [21] -->
m

<!-- b007651 | prose | pages [21] -->
m

<!-- b007652 | prose | pages [21] -->
m

<!-- b007653 | prose | pages [21] -->
m

<!-- b007654 | prose | pages [21] -->
m

<!-- b007655 | prose | pages [21] -->
m

<!-- b007656 | prose | pages [21] -->
m

<!-- b007657 | prose | pages [21] -->
m

<!-- b007658 | prose | pages [21] -->
m

<!-- b007659 | prose | pages [21] -->
m

<!-- b007660 | prose | pages [21] -->
m

<!-- b007661 | prose | pages [21] -->
m

<!-- b007662 | prose | pages [21] -->
m

<!-- b007663 | prose | pages [21] -->
m

<!-- b007664 | prose | pages [21] -->
m

<!-- b007665 | prose | pages [21] -->
m

<!-- b007666 | prose | pages [21] -->
m

<!-- b007667 | prose | pages [21] -->
m

<!-- b007668 | prose | pages [21] -->
m

<!-- b007669 | prose | pages [21] -->
m

<!-- b007670 | furniture | pages [21] -->
m

<!-- b007671 | furniture | pages [21] -->
m

<!-- b007672 | furniture | pages [21] -->
m

<!-- b007673 | furniture | pages [21] -->
m

<!-- b007674 | furniture | pages [21] -->
m

<!-- b007675 | furniture | pages [21] -->
m

<!-- b007676 | furniture | pages [21] -->
m

<!-- b007677 | furniture | pages [21] -->
m

<!-- b007678 | furniture | pages [21] -->
m

<!-- b007679 | furniture | pages [21] -->
m

<!-- b007680 | furniture | pages [21] -->
m

<!-- b007681 | furniture | pages [21] -->
m

<!-- b007682 | furniture | pages [21] -->
m

<!-- b007683 | furniture | pages [21] -->
m

<!-- b007684 | furniture | pages [21] -->
m

<!-- b007685 | furniture | pages [21] -->
m

<!-- b007686 | furniture | pages [21] -->
m

<!-- b007687 | furniture | pages [21] -->
m

<!-- b007688 | furniture | pages [21] -->
m

<!-- b007689 | furniture | pages [21] -->
m

<!-- b007690 | furniture | pages [21] -->
m

<!-- b007691 | furniture | pages [21] -->
m

<!-- b007692 | furniture | pages [21] -->
m

<!-- b007693 | furniture | pages [21] -->
m

<!-- b007694 | furniture | pages [21] -->
m

<!-- b007695 | furniture | pages [21] -->
m

<!-- b007696 | furniture | pages [21] -->
m

<!-- b007697 | furniture | pages [21] -->
m

<!-- b007698 | furniture | pages [21] -->
m

<!-- b007699 | furniture | pages [21] -->
m

<!-- b007700 | furniture | pages [21] -->
m

<!-- b007701 | furniture | pages [21] -->
m

<!-- b007702 | furniture | pages [21] -->
m

<!-- b007703 | furniture | pages [21] -->
m

<!-- b007704 | furniture | pages [21] -->
m

<!-- b007705 | furniture | pages [21] -->
m

<!-- b007706 | furniture | pages [21] -->
m

<!-- b007707 | furniture | pages [21] -->
m

<!-- b007708 | furniture | pages [21] -->
m

<!-- b007709 | furniture | pages [21] -->
m

<!-- b007710 | furniture | pages [21] -->
m

<!-- b007711 | furniture | pages [21] -->
m

<!-- b007712 | furniture | pages [21] -->
m

<!-- b007713 | furniture | pages [21] -->
m

<!-- b007714 | furniture | pages [21] -->
m

<!-- b007715 | furniture | pages [21] -->
m

<!-- b007716 | furniture | pages [21] -->
m

<!-- b007717 | furniture | pages [21] -->
m

<!-- b007718 | furniture | pages [21] -->
m

<!-- b007719 | furniture | pages [21] -->
m

<!-- b007720 | furniture | pages [21] -->
m

<!-- b007721 | furniture | pages [21] -->
m

<!-- b007722 | furniture | pages [21] -->
m

<!-- b007723 | furniture | pages [21] -->
m

<!-- b007724 | furniture | pages [21] -->
m

<!-- b007725 | furniture | pages [21] -->
m

<!-- b007726 | furniture | pages [21] -->
m

<!-- b007727 | furniture | pages [21] -->
m

<!-- b007728 | furniture | pages [21] -->
m

<!-- b007729 | furniture | pages [21] -->
m

<!-- b007730 | furniture | pages [21] -->
m

<!-- b007731 | furniture | pages [21] -->
m

<!-- b007732 | furniture | pages [21] -->
m

<!-- b007733 | furniture | pages [21] -->
m

<!-- b007734 | furniture | pages [21] -->
m

<!-- b007735 | furniture | pages [21] -->
m

<!-- b007736 | furniture | pages [21] -->
m

<!-- b007737 | furniture | pages [21] -->
m

<!-- b007738 | furniture | pages [21] -->
m

<!-- b007739 | furniture | pages [21] -->
m

<!-- b007740 | furniture | pages [21] -->
m

<!-- b007741 | furniture | pages [21] -->
m

<!-- b007742 | furniture | pages [21] -->
m

<!-- b007743 | furniture | pages [21] -->
m

<!-- b007744 | furniture | pages [21] -->
m

<!-- b007745 | furniture | pages [21] -->
m

<!-- b007746 | furniture | pages [21] -->
m

<!-- b007747 | furniture | pages [21] -->
m

<!-- b007748 | furniture | pages [21] -->
m

<!-- b007749 | furniture | pages [21] -->
m

<!-- b007750 | furniture | pages [21] -->
m

<!-- b007751 | furniture | pages [21] -->
m

<!-- b007752 | furniture | pages [21] -->
m

<!-- b007753 | furniture | pages [21] -->
m

<!-- b007754 | furniture | pages [21] -->
m

<!-- b007755 | furniture | pages [21] -->
m

<!-- b007756 | furniture | pages [21] -->
m

<!-- b007757 | furniture | pages [21] -->
m

<!-- b007758 | furniture | pages [21] -->
m

<!-- b007759 | furniture | pages [21] -->
m

<!-- b007760 | furniture | pages [21] -->
m

<!-- b007761 | furniture | pages [21] -->
m

<!-- b007762 | furniture | pages [21] -->
m

<!-- b007763 | furniture | pages [21] -->
m

<!-- b007764 | furniture | pages [21] -->
m

<!-- b007765 | furniture | pages [21] -->
m

<!-- b007766 | furniture | pages [21] -->
m

<!-- b007767 | furniture | pages [21] -->
m

<!-- b007768 | furniture | pages [21] -->
m

<!-- b007769 | furniture | pages [21] -->
m

<!-- b007770 | furniture | pages [21] -->
m

<!-- b007771 | furniture | pages [21] -->
m

<!-- b007772 | furniture | pages [21] -->
m

<!-- b007773 | furniture | pages [21] -->
m

<!-- b007774 | furniture | pages [21] -->
m

<!-- b007775 | furniture | pages [21] -->
m

<!-- b007776 | furniture | pages [21] -->
m

<!-- b007777 | furniture | pages [21] -->
m

<!-- b007778 | furniture | pages [21] -->
m

<!-- b007779 | furniture | pages [21] -->
m

<!-- b007780 | furniture | pages [21] -->
m

<!-- b007781 | furniture | pages [21] -->
m

<!-- b007782 | furniture | pages [21] -->
m

<!-- b007783 | furniture | pages [21] -->
m

<!-- b007784 | furniture | pages [21] -->
m

<!-- b007785 | furniture | pages [21] -->
m

<!-- b007786 | furniture | pages [21] -->
m

<!-- b007787 | furniture | pages [21] -->
m

<!-- b007788 | furniture | pages [21] -->
m

<!-- b007789 | furniture | pages [21] -->
m

<!-- b007790 | furniture | pages [21] -->
m

<!-- b007791 | furniture | pages [21] -->
m

<!-- b007792 | furniture | pages [21] -->
m

<!-- b007793 | furniture | pages [21] -->
m

<!-- b007794 | furniture | pages [21] -->
m

<!-- b007795 | furniture | pages [21] -->
m

<!-- b007796 | furniture | pages [21] -->
m

<!-- b007797 | furniture | pages [21] -->
m

<!-- b007798 | furniture | pages [21] -->
m

<!-- b007799 | furniture | pages [21] -->
m

<!-- b007800 | furniture | pages [21] -->
m

<!-- b007801 | furniture | pages [21] -->
m

<!-- b007802 | furniture | pages [21] -->
m

<!-- b007803 | furniture | pages [21] -->
m

<!-- b007804 | furniture | pages [21] -->
m

<!-- b007805 | furniture | pages [21] -->
m

<!-- b007806 | furniture | pages [21] -->
m

<!-- b007807 | furniture | pages [21] -->
m

<!-- b007808 | furniture | pages [21] -->
m

<!-- b007809 | furniture | pages [21] -->
m

<!-- b007810 | furniture | pages [21] -->
m

<!-- b007811 | furniture | pages [21] -->
m

<!-- b007812 | furniture | pages [21] -->
m

<!-- b007813 | furniture | pages [21] -->
m

<!-- b007814 | furniture | pages [21] -->
m

<!-- b007815 | furniture | pages [21] -->
m

<!-- b007816 | furniture | pages [21] -->
m

<!-- b007817 | furniture | pages [21] -->
m

<!-- b007818 | furniture | pages [21] -->
m

<!-- b007819 | furniture | pages [21] -->
m

<!-- b007820 | furniture | pages [21] -->
m

<!-- b007821 | furniture | pages [21] -->
m

<!-- b007822 | furniture | pages [21] -->
m

<!-- b007823 | furniture | pages [21] -->
m

<!-- b007824 | furniture | pages [21] -->
m

<!-- b007825 | furniture | pages [21] -->
m

<!-- b007826 | furniture | pages [21] -->
m

<!-- b007827 | furniture | pages [21] -->
m

<!-- b007828 | furniture | pages [21] -->
m

<!-- b007829 | furniture | pages [21] -->
m

<!-- b007830 | furniture | pages [21] -->
m

<!-- b007831 | furniture | pages [21] -->
m

<!-- b007832 | furniture | pages [21] -->
m

<!-- b007833 | furniture | pages [21] -->
m

<!-- b007834 | furniture | pages [21] -->
m

<!-- b007835 | furniture | pages [21] -->
m

<!-- b007836 | furniture | pages [21] -->
m

<!-- b007837 | furniture | pages [21] -->
m

<!-- b007838 | furniture | pages [21] -->
m

<!-- b007839 | furniture | pages [21] -->
m

<!-- b007840 | furniture | pages [21] -->
m

<!-- b007841 | furniture | pages [21] -->
m

<!-- b007842 | furniture | pages [21] -->
m

<!-- b007843 | furniture | pages [21] -->
m

<!-- b007844 | furniture | pages [21] -->
m

<!-- b007845 | furniture | pages [21] -->
m

<!-- b007846 | furniture | pages [21] -->
m

<!-- b007847 | furniture | pages [21] -->
m

<!-- b007848 | furniture | pages [21] -->
m

<!-- b007849 | furniture | pages [21] -->
m

<!-- b007850 | furniture | pages [21] -->
m

<!-- b007851 | furniture | pages [21] -->
m

<!-- b007852 | furniture | pages [21] -->
m

<!-- b007853 | furniture | pages [21] -->
m

<!-- b007854 | furniture | pages [21] -->
m

<!-- b007855 | furniture | pages [21] -->
m

<!-- b007856 | furniture | pages [21] -->
m

<!-- b007857 | furniture | pages [21] -->
m

<!-- b007858 | furniture | pages [21] -->
m

<!-- b007859 | furniture | pages [21] -->
m

<!-- b007860 | furniture | pages [21] -->
m

<!-- b007861 | furniture | pages [21] -->
m

<!-- b007862 | furniture | pages [21] -->
m

<!-- b007863 | furniture | pages [21] -->
m

<!-- b007864 | furniture | pages [21] -->
m

<!-- b007865 | furniture | pages [21] -->
m

<!-- b007866 | furniture | pages [21] -->
m

<!-- b007867 | furniture | pages [21] -->
m

<!-- b007868 | furniture | pages [21] -->
m

<!-- b007869 | furniture | pages [21] -->
m

<!-- b007870 | furniture | pages [21] -->
m

<!-- b007871 | furniture | pages [21] -->
m

<!-- b007872 | furniture | pages [21] -->
m

<!-- b007873 | furniture | pages [21] -->
m

<!-- b007874 | furniture | pages [21] -->
m

<!-- b007875 | furniture | pages [21] -->
m

<!-- b007876 | furniture | pages [21] -->
m

<!-- b007877 | furniture | pages [21] -->
m

<!-- b007878 | furniture | pages [21] -->
m

<!-- b007879 | furniture | pages [21] -->
m

<!-- b007880 | furniture | pages [21] -->
m

<!-- b007881 | furniture | pages [21] -->
m

<!-- b007882 | furniture | pages [21] -->
m

<!-- b007883 | furniture | pages [21] -->
m

<!-- b007884 | furniture | pages [21] -->
m

<!-- b007885 | furniture | pages [21] -->
m

<!-- b007886 | furniture | pages [21] -->
m

<!-- b007887 | furniture | pages [21] -->
m

<!-- b007888 | furniture | pages [21] -->
m

<!-- b007889 | furniture | pages [21] -->
m

<!-- b007890 | furniture | pages [21] -->
m

<!-- b007891 | furniture | pages [21] -->
m

<!-- b007892 | furniture | pages [21] -->
m

<!-- b007893 | furniture | pages [21] -->
m

<!-- b007894 | furniture | pages [21] -->
m

<!-- b007895 | furniture | pages [21] -->
m

<!-- b007896 | furniture | pages [21] -->
m

<!-- b007897 | furniture | pages [21] -->
m

<!-- b007898 | furniture | pages [21] -->
m

<!-- b007899 | furniture | pages [21] -->
m

<!-- b007900 | furniture | pages [21] -->
m

<!-- b007901 | furniture | pages [21] -->
m

<!-- b007902 | furniture | pages [21] -->
m

<!-- b007903 | furniture | pages [21] -->
m

<!-- b007904 | furniture | pages [21] -->
m

<!-- b007905 | furniture | pages [21] -->
m

<!-- b007906 | furniture | pages [21] -->
m

<!-- b007907 | furniture | pages [21] -->
m

<!-- b007908 | furniture | pages [21] -->
m

<!-- b007909 | furniture | pages [21] -->
m

<!-- b007910 | furniture | pages [21] -->
m

<!-- b007911 | furniture | pages [21] -->
m

<!-- b007912 | furniture | pages [21] -->
m

<!-- b007913 | furniture | pages [21] -->
m

<!-- b007914 | furniture | pages [21] -->
m

<!-- b007915 | furniture | pages [21] -->
m

<!-- b007916 | furniture | pages [21] -->
m

<!-- b007917 | furniture | pages [21] -->
m

<!-- b007918 | furniture | pages [21] -->
m

<!-- b007919 | furniture | pages [21] -->
m

<!-- b007920 | furniture | pages [21] -->
m

<!-- b007921 | furniture | pages [21] -->
m

<!-- b007922 | furniture | pages [21] -->
m

<!-- b007923 | furniture | pages [21] -->
m

<!-- b007924 | furniture | pages [21] -->
m

<!-- b007925 | furniture | pages [21] -->
m

<!-- b007926 | furniture | pages [21] -->
m

<!-- b007927 | furniture | pages [21] -->
m

<!-- b007928 | furniture | pages [21] -->
m

<!-- b007929 | furniture | pages [21] -->
m

<!-- b007930 | furniture | pages [21] -->
m

<!-- b007931 | furniture | pages [21] -->
m

<!-- b007932 | furniture | pages [21] -->
m

<!-- b007933 | furniture | pages [21] -->
m

<!-- b007934 | furniture | pages [21] -->
m

<!-- b007935 | furniture | pages [21] -->
m

<!-- b007936 | furniture | pages [21] -->
m

<!-- b007937 | furniture | pages [21] -->
m

<!-- b007938 | furniture | pages [21] -->
m

<!-- b007939 | furniture | pages [21] -->
m

<!-- b007940 | furniture | pages [21] -->
m

<!-- b007941 | furniture | pages [21] -->
m

<!-- b007942 | furniture | pages [21] -->
m

<!-- b007943 | furniture | pages [21] -->
m

<!-- b007944 | furniture | pages [21] -->
m

<!-- b007945 | furniture | pages [21] -->
m

<!-- b007946 | furniture | pages [21] -->
m

<!-- b007947 | furniture | pages [21] -->
m

<!-- b007948 | furniture | pages [21] -->
m

<!-- b007949 | furniture | pages [21] -->
m

<!-- b007950 | furniture | pages [21] -->
m

<!-- b007951 | furniture | pages [21] -->
m

<!-- b007952 | furniture | pages [21] -->
m

<!-- b007953 | furniture | pages [21] -->
m

<!-- b007954 | furniture | pages [21] -->
m

<!-- b007955 | furniture | pages [21] -->
m

<!-- b007956 | furniture | pages [21] -->
m

<!-- b007957 | furniture | pages [21] -->
m

<!-- b007958 | furniture | pages [21] -->
m

<!-- b007959 | furniture | pages [21] -->
m

<!-- b007960 | furniture | pages [21] -->
m

<!-- b007961 | furniture | pages [21] -->
m

<!-- b007962 | furniture | pages [21] -->
m

<!-- b007963 | furniture | pages [21] -->
m

<!-- b007964 | furniture | pages [21] -->
m

<!-- b007965 | furniture | pages [21] -->
m

<!-- b007966 | furniture | pages [21] -->
m

<!-- b007967 | furniture | pages [21] -->
m

<!-- b007968 | furniture | pages [21] -->
m

<!-- b007969 | furniture | pages [21] -->
m

<!-- b007970 | furniture | pages [21] -->
m

<!-- b007971 | furniture | pages [21] -->
m

<!-- b007972 | furniture | pages [21] -->
m

<!-- b007973 | furniture | pages [21] -->
m

<!-- b007974 | furniture | pages [21] -->
m

<!-- b007975 | furniture | pages [21] -->
m

<!-- b007976 | furniture | pages [21] -->
m

<!-- b007977 | furniture | pages [21] -->
m

<!-- b007978 | furniture | pages [21] -->
m

<!-- b007979 | furniture | pages [21] -->
m

<!-- b007980 | furniture | pages [21] -->
m

<!-- b007981 | furniture | pages [21] -->
m

<!-- b007982 | furniture | pages [21] -->
m

<!-- b007983 | furniture | pages [21] -->
m

<!-- b007984 | furniture | pages [21] -->
m

<!-- b007985 | furniture | pages [21] -->
m

<!-- b007986 | furniture | pages [21] -->
m

<!-- b007987 | furniture | pages [21] -->
m

<!-- b007988 | furniture | pages [21] -->
m

<!-- b007989 | furniture | pages [21] -->
m

<!-- b007990 | furniture | pages [21] -->
m

<!-- b007991 | furniture | pages [21] -->
m

<!-- b007992 | furniture | pages [21] -->
m

<!-- b007993 | furniture | pages [21] -->
m

<!-- b007994 | furniture | pages [21] -->
m

<!-- b007995 | furniture | pages [21] -->
m

<!-- b007996 | furniture | pages [21] -->
m

<!-- b007997 | furniture | pages [21] -->
m

<!-- b007998 | furniture | pages [21] -->
m

<!-- b007999 | furniture | pages [21] -->
m

<!-- b008000 | furniture | pages [21] -->
m

<!-- b008001 | furniture | pages [21] -->
m

<!-- b008002 | furniture | pages [21] -->
m

<!-- b008003 | furniture | pages [21] -->
m

<!-- b008004 | furniture | pages [21] -->
m

<!-- b008005 | furniture | pages [21] -->
m

<!-- b008006 | furniture | pages [21] -->
m

<!-- b008007 | furniture | pages [21] -->
m

<!-- b008008 | furniture | pages [21] -->
m

<!-- b008009 | furniture | pages [21] -->
m

<!-- b008010 | furniture | pages [21] -->
m

<!-- b008011 | furniture | pages [21] -->
m

<!-- b008012 | furniture | pages [21] -->
m

<!-- b008013 | furniture | pages [21] -->
m

<!-- b008014 | furniture | pages [21] -->
m

<!-- b008015 | furniture | pages [21] -->
m

<!-- b008016 | furniture | pages [21] -->
m

<!-- b008017 | furniture | pages [21] -->
m

<!-- b008018 | furniture | pages [21] -->
m

<!-- b008019 | furniture | pages [21] -->
m

<!-- b008020 | furniture | pages [21] -->
m

<!-- b008021 | furniture | pages [21] -->
m

<!-- b008022 | furniture | pages [21] -->
m

<!-- b008023 | furniture | pages [21] -->
m

<!-- b008024 | furniture | pages [21] -->
m

<!-- b008025 | furniture | pages [21] -->
m

<!-- b008026 | furniture | pages [21] -->
m

<!-- b008027 | furniture | pages [21] -->
m

<!-- b008028 | furniture | pages [21] -->
m

<!-- b008029 | furniture | pages [21] -->
m

<!-- b008030 | furniture | pages [21] -->
m

<!-- b008031 | furniture | pages [21] -->
m

<!-- b008032 | furniture | pages [21] -->
m

<!-- b008033 | furniture | pages [21] -->
m

<!-- b008034 | furniture | pages [21] -->
m

<!-- b008035 | furniture | pages [21] -->
m

<!-- b008036 | furniture | pages [21] -->
m

<!-- b008037 | furniture | pages [21] -->
m

<!-- b008038 | furniture | pages [21] -->
m

<!-- b008039 | furniture | pages [21] -->
m

<!-- b008040 | furniture | pages [21] -->
m

<!-- b008041 | furniture | pages [21] -->
m

<!-- b008042 | furniture | pages [21] -->
m

<!-- b008043 | furniture | pages [21] -->
m

<!-- b008044 | furniture | pages [21] -->
m

<!-- b008045 | furniture | pages [21] -->
m

<!-- b008046 | furniture | pages [21] -->
m

<!-- b008047 | furniture | pages [21] -->
m

<!-- b008048 | furniture | pages [21] -->
m

<!-- b008049 | furniture | pages [21] -->
m

<!-- b008050 | furniture | pages [21] -->
m

<!-- b008051 | furniture | pages [21] -->
m

<!-- b008052 | furniture | pages [21] -->
m

<!-- b008053 | furniture | pages [21] -->
m

<!-- b008054 | furniture | pages [21] -->
m

<!-- b008055 | furniture | pages [21] -->
m

<!-- b008056 | furniture | pages [21] -->
m

<!-- b008057 | furniture | pages [21] -->
m

<!-- b008058 | furniture | pages [21] -->
m

<!-- b008059 | furniture | pages [21] -->
m

<!-- b008060 | furniture | pages [21] -->
m

<!-- b008061 | furniture | pages [21] -->
m

<!-- b008062 | furniture | pages [21] -->
m

<!-- b008063 | furniture | pages [21] -->
m

<!-- b008064 | furniture | pages [21] -->
m

<!-- b008065 | furniture | pages [21] -->
m

<!-- b008066 | furniture | pages [21] -->
m

<!-- b008067 | furniture | pages [21] -->
m

<!-- b008068 | furniture | pages [21] -->
m

<!-- b008069 | furniture | pages [21] -->
m

<!-- b008070 | furniture | pages [21] -->
m

<!-- b008071 | furniture | pages [21] -->
m

<!-- b008072 | furniture | pages [21] -->
m

<!-- b008073 | furniture | pages [22] -->
Team # 2503389

<!-- b008074 | furniture | pages [22] -->
Page 22 of 26

<!-- b008075 | prose | pages [22] -->
The Practical Application of the ”Great Coach” Effect 9

<!-- b008076 | prose | pages [22] -->
Selection of Sports Needing a Great Coach 9.1

<!-- b008077 | prose | pages [22] -->
9.1.1 Data Utilization

<!-- b008078 | prose | pages [22] -->
1. Aggregate the Score data from 2016 and 2020, calculating the mean and standard devia- tion for each year.

<!-- b008079 | prose | pages [22] -->
2. Select the 20th percentile, with a threshold of 0.15.

<!-- b008080 | prose | pages [22] -->
3. Check the proportion of sports in the distribution with scores close to 0.15 to ensure it aligns with actual observations.

<!-- b008081 | prose | pages [22] -->
Selection Criteria:

<!-- b008082 | prose | pages [22] -->
• A sport’s Score in both 2016 and 2020 must be greater than 0.15.

<!-- b008083 | prose | pages [22] -->
• The Score for 2024 must be less than 0.15.

<!-- b008084 | prose | pages [22] -->
9.2

<!-- b008085 | heading | pages [22] -->
Results

<!-- b008086 | prose | pages [22] -->
After the preliminary screening, Nigeria, Poland, and India were selected as the countries of interest. According to the above criteria, the sports that require the introduction of a Great Coach were selected. The final list of potential sports for a Great Coach includes:

<!-- b008087 | prose | pages [22] -->
• Poland: Athletics, Canoe Sprint, Sailing

<!-- b008088 | prose | pages [22] -->
• Nigeria: Football

<!-- b008089 | prose | pages [22] -->
• India: Badminton, Weightlifting, Wrestling

<!-- b008090 | heading | pages [22] -->
Validation of the Conclusion: Coach’s Impact Calculation

<!-- b008091 | prose | pages [22] -->
9.2.1

<!-- b008092 | prose | pages [22] -->
From Section 2.1, it is determined that the contribution rate of the coach to the sport is u = 1.7. This means that after introducing the coach, the Score for 2024 increases by u× the pre-coaching Score. By comparing the results, we find that the likelihood of winning medals in these sports for the selected countries has increased after the introduction of the coach.

<!-- b008093 | prose | pages [22] -->
Other Insights: Host Country Spillover Effect on Medal 10 Rates of Neighboring Countries

<!-- b008094 | prose | pages [22] -->
10.1

<!-- b008095 | heading | pages [22] -->
Analysis and Results

<!-- b008096 | prose | pages [22] -->
We analyzed the medal rates of various countries in the 2016, 2020, and 2024 Olympic Games, focusing on the differences in medal rates for neighboring countries of the host na- tion (land-bordering countries). Specifically, we compared the medal rate of these neighboring countries in the current Olympics to the average medal rate from the previous two Olympic Games. We identified countries with a positive difference in medal rates and mapped these im- provements. The results from these maps 17 clearly demonstrate that the ”Host Country Effect”

<!-- b008097 | prose | pages [22] -->
关注数学模型

<!-- b008098 | furniture | pages [22] -->
2

<!-- b008099 | furniture | pages [22] -->
MATHmodels

<!-- b008100 | furniture | pages [22] -->
获取更多资讯

<!-- b008101 | furniture | pages [24] -->
Team # 2503389

<!-- b008102 | heading | pages [24] -->
Results and Observations

<!-- b008103 | caption | pages [24] -->
Figure 18: Impact of His-

<!-- b008104 | furniture | pages [24] -->
Page 24 of 26

<!-- b008105 | caption | pages [24] -->
Figure 20: Impact of Com-

<!-- b008106 | caption | pages [24] -->
Figure 19: Impact of Ath-

<!-- b008107 | prose | pages [24] -->
torical Momentum on Pre-

<!-- b008108 | prose | pages [24] -->
petitiveness Index on Pre-

<!-- b008109 | prose | pages [24] -->
letes on Predicted Medals

<!-- b008110 | prose | pages [24] -->
dicted Medals

<!-- b008111 | prose | pages [24] -->
dicted Medals

<!-- b008112 | prose | pages [24] -->
All three factors features are positively correlated with predicted medals. The slope of the regression lines shows a steady increase in medals as each factor rises. The shaded areas indicate potential fluctuations in predictions, providing insights into the model’s accuracy and reliability.

<!-- b008113 | prose | pages [24] -->
12

<!-- b008114 | heading | pages [24] -->
Strengths and Weaknesses

<!-- b008115 | heading | pages [24] -->
Strengths

<!-- b008116 | heading | pages [24] -->
• Comprehensive Feature Integration (MLR-FNN): The MLR-FNN model combines

<!-- b008117 | prose | pages [24] -->
feature extraction and relationship learning to predict the 2028 medal table. It includes factors like participant numbers, host nation effects, historical medal counts, and compet- itiveness, providing strong predictions with confidence intervals that reflect real-world situations.

<!-- b008118 | heading | pages [24] -->
• Balanced Interpretability and Complexity (LR-RF): The LR-RF model mixes logistic

<!-- b008119 | prose | pages [24] -->
regression’s clear results with random forest’s ability to handle complex relationships and rank factors. This makes it a powerful tool for analyzing Olympic data.

<!-- b008120 | heading | pages [24] -->
• Strategic Sports Evaluation (SIAMOS): The SIAMOS model looks at sports’ impor-

<!-- b008121 | prose | pages [24] -->
tance using four factors: National Medal Proportion (NMP), Global Competitive Pro- portion (GCP), Long-term Achievement Stability (LAS), and Athlete Sport Distribution (ASD). It gives useful insights to help focus resources and improve Olympic performance.

<!-- b008122 | heading | pages [24] -->
• Causal Analysis of Coaching Impact (RDD): The regression discontinuity model mea-

<!-- b008123 | prose | pages [24] -->
sures the “great coach effect” by looking at natural breaks in data and considering cross- country and time changes. It provides clear advice on how to invest in coaching to improve medal results.

<!-- b008124 | heading | pages [24] -->
Weaknesses

<!-- b008125 | prose | pages [24] -->
• Limited Feature Scope: Some models, like the MLR-FNN, do not include important factors such as the Host Country Spillover Effect, limiting the analysis.

<!-- b008126 | prose | pages [24] -->
• Subjective Design Choices: Some formulas were chosen without calculation, making the model more subjective and possibly less generalizable. For example, it is assumed that the performance of new athletes is the same as athletes who no longer compete. This keeps the number and composition of athletes the same.

<!-- b008127 | prose | pages [24] -->
关注数学模型

<!-- b008128 | furniture | pages [24] -->
2

<!-- b008129 | furniture | pages [24] -->
MATHmodels

<!-- b008130 | furniture | pages [24] -->
获取更多资讯

<!-- b008131 | furniture | pages [25] -->
Team # 2503389

<!-- b008132 | furniture | pages [25] -->
Page 25 of 26

<!-- b008133 | heading | pages [25] -->
References

<!-- b008134 | references | pages [25] -->
[1] International Olympic Committee, National Olympic Committees, https://www.olympics.

<!-- b008135 | references | pages [25] -->
com/ioc/national-olympic-committees?os=__&ref=app, accessed 27 Jan. 2025.

<!-- b008136 | references | pages [25] -->
[2] Mancini, Simona, and Triki, [First Name]. ”Optimal Selection of Touristic Packages Based

<!-- b008137 | references | pages [25] -->
微信公众号：数学模型

<!-- b008138 | references | pages [25] -->
on User Preferences During Sports Mega-Events.” European Journal of Operational Re-

<!-- b008139 | references | pages [25] -->
search, vol. 302, no. 3, Nov. 2022, pp. 819-830.

<!-- b008140 | references | pages [25] -->
[3] Bernard, A. B., and Busse, M. R. (2004). ”Who Wins the Olympic Games: Economic

<!-- b008141 | references | pages [25] -->
Resources and Medal Totals.” Review of Economics and Statistics, vol. 86, no. 1, pp. 413–

<!-- b008142 | references | pages [25] -->
417. https://doi.org/10.1162/003465304774201824.

<!-- b008143 | references | pages [25] -->
[4] Jay Belanger, William P. Fox, Wang Jie Mao, and Zi Yang. (2017). Correct Writing for the

<!-- b008144 | references | pages [25] -->
Mathematical Contest in Modeling (MCM). Higher Education Press.

<!-- b008145 | references | pages [25] -->
[5] Olympics. (2024). ”2024 Paris Olympic Games Artistic Swimming: Chinese Team Sets

<!-- b008146 | references | pages [25] -->
微信号：MATHmodels

<!-- b008147 | references | pages [25] -->
New Historical High in Team Free Routine.” Retrieved from https://www.olympics.com/

<!-- b008148 | references | pages [25] -->
zh/news/paris-2024-results-artistic-swimming-team-free-routine-wrap-up.

<!-- b008149 | references | pages [25] -->
[6] Way We Do. (2024). ”The Marginal Gains Strategy: British Cycling’s Road to Victory.”

<!-- b008150 | references | pages [25] -->
Retrieved from https://www.waywedo.com/blog/marginal-gains-strategy/.

<!-- b008151 | references | pages [25] -->
[7] Wikipedia. (2024). ”Béla Károlyi.” Retrieved from https://en.wikipedia.org/wiki/B%C3%

<!-- b008152 | references | pages [25] -->
A9la_K%C3%A1rolyi.

<!-- b008153 | references | pages [25] -->
m

<!-- b008154 | references | pages [25] -->
m

<!-- b008155 | references | pages [25] -->
m

<!-- b008156 | references | pages [25] -->
m

<!-- b008157 | references | pages [25] -->
m

<!-- b008158 | references | pages [25] -->
m

<!-- b008159 | references | pages [25] -->
m

<!-- b008160 | references | pages [25] -->
m

<!-- b008161 | references | pages [25] -->
m

<!-- b008162 | references | pages [25] -->
m

<!-- b008163 | references | pages [25] -->
m

<!-- b008164 | references | pages [25] -->
m

<!-- b008165 | references | pages [25] -->
m

<!-- b008166 | references | pages [25] -->
m

<!-- b008167 | references | pages [25] -->
m

<!-- b008168 | references | pages [25] -->
m

<!-- b008169 | references | pages [25] -->
m

<!-- b008170 | references | pages [25] -->
m

<!-- b008171 | references | pages [25] -->
m

<!-- b008172 | references | pages [25] -->
m

<!-- b008173 | references | pages [25] -->
m

<!-- b008174 | references | pages [25] -->
m

<!-- b008175 | references | pages [25] -->
m

<!-- b008176 | references | pages [25] -->
m

<!-- b008177 | references | pages [25] -->
m

<!-- b008178 | references | pages [25] -->
m

<!-- b008179 | references | pages [25] -->
m

<!-- b008180 | references | pages [25] -->
m

<!-- b008181 | references | pages [25] -->
m

<!-- b008182 | references | pages [25] -->
m

<!-- b008183 | references | pages [25] -->
m

<!-- b008184 | references | pages [25] -->
m

<!-- b008185 | references | pages [25] -->
m

<!-- b008186 | references | pages [25] -->
m

<!-- b008187 | references | pages [25] -->
m

<!-- b008188 | references | pages [25] -->
m

<!-- b008189 | references | pages [25] -->
m

<!-- b008190 | references | pages [25] -->
m

<!-- b008191 | references | pages [25] -->
m

<!-- b008192 | references | pages [25] -->
m

<!-- b008193 | references | pages [25] -->
m

<!-- b008194 | references | pages [25] -->
m

<!-- b008195 | references | pages [25] -->
m

<!-- b008196 | references | pages [25] -->
m

<!-- b008197 | references | pages [25] -->
m

<!-- b008198 | references | pages [25] -->
m

<!-- b008199 | references | pages [25] -->
m

<!-- b008200 | references | pages [25] -->
m

<!-- b008201 | references | pages [25] -->
m

<!-- b008202 | references | pages [25] -->
m

<!-- b008203 | references | pages [25] -->
m

<!-- b008204 | references | pages [25] -->
m

<!-- b008205 | references | pages [25] -->
m

<!-- b008206 | references | pages [25] -->
m

<!-- b008207 | references | pages [25] -->
m

<!-- b008208 | references | pages [25] -->
m

<!-- b008209 | references | pages [25] -->
m

<!-- b008210 | references | pages [25] -->
m

<!-- b008211 | references | pages [25] -->
m

<!-- b008212 | references | pages [25] -->
m

<!-- b008213 | references | pages [25] -->
m

<!-- b008214 | references | pages [25] -->
m

<!-- b008215 | references | pages [25] -->
m

<!-- b008216 | references | pages [25] -->
m

<!-- b008217 | references | pages [25] -->
m

<!-- b008218 | references | pages [25] -->
m

<!-- b008219 | references | pages [25] -->
m

<!-- b008220 | references | pages [25] -->
m

<!-- b008221 | references | pages [25] -->
m

<!-- b008222 | references | pages [25] -->
m

<!-- b008223 | references | pages [25] -->
m

<!-- b008224 | references | pages [25] -->
m

<!-- b008225 | references | pages [25] -->
m

<!-- b008226 | references | pages [25] -->
m

<!-- b008227 | references | pages [25] -->
m

<!-- b008228 | references | pages [25] -->
m

<!-- b008229 | references | pages [25] -->
m

<!-- b008230 | references | pages [25] -->
m

<!-- b008231 | references | pages [25] -->
m

<!-- b008232 | references | pages [25] -->
m

<!-- b008233 | references | pages [25] -->
m

<!-- b008234 | references | pages [25] -->
m

<!-- b008235 | references | pages [25] -->
m

<!-- b008236 | references | pages [25] -->
m

<!-- b008237 | references | pages [25] -->
m

<!-- b008238 | references | pages [25] -->
m

<!-- b008239 | references | pages [25] -->
m

<!-- b008240 | references | pages [25] -->
m

<!-- b008241 | references | pages [25] -->
m

<!-- b008242 | references | pages [25] -->
m

<!-- b008243 | references | pages [25] -->
m

<!-- b008244 | references | pages [25] -->
m

<!-- b008245 | references | pages [25] -->
m

<!-- b008246 | references | pages [25] -->
m

<!-- b008247 | references | pages [25] -->
m

<!-- b008248 | references | pages [25] -->
m

<!-- b008249 | references | pages [25] -->
m

<!-- b008250 | references | pages [25] -->
m

<!-- b008251 | references | pages [25] -->
m

<!-- b008252 | references | pages [25] -->
m

<!-- b008253 | references | pages [25] -->
m

<!-- b008254 | references | pages [25] -->
m

<!-- b008255 | references | pages [25] -->
m

<!-- b008256 | references | pages [25] -->
m

<!-- b008257 | references | pages [25] -->
m

<!-- b008258 | references | pages [25] -->
m

<!-- b008259 | references | pages [25] -->
m

<!-- b008260 | references | pages [25] -->
m

<!-- b008261 | references | pages [25] -->
m

<!-- b008262 | references | pages [25] -->
m

<!-- b008263 | references | pages [25] -->
m

<!-- b008264 | references | pages [25] -->
m

<!-- b008265 | references | pages [25] -->
m

<!-- b008266 | references | pages [25] -->
m

<!-- b008267 | references | pages [25] -->
m

<!-- b008268 | references | pages [25] -->
m

<!-- b008269 | references | pages [25] -->
m

<!-- b008270 | references | pages [25] -->
m

<!-- b008271 | references | pages [25] -->
m

<!-- b008272 | references | pages [25] -->
m

<!-- b008273 | references | pages [25] -->
m

<!-- b008274 | references | pages [25] -->
m

<!-- b008275 | references | pages [25] -->
m

<!-- b008276 | references | pages [25] -->
m

<!-- b008277 | references | pages [25] -->
m

<!-- b008278 | references | pages [25] -->
m

<!-- b008279 | references | pages [25] -->
m

<!-- b008280 | references | pages [25] -->
m

<!-- b008281 | references | pages [25] -->
m

<!-- b008282 | references | pages [25] -->
m

<!-- b008283 | references | pages [25] -->
m

<!-- b008284 | references | pages [25] -->
m

<!-- b008285 | references | pages [25] -->
m

<!-- b008286 | references | pages [25] -->
m

<!-- b008287 | references | pages [25] -->
m

<!-- b008288 | references | pages [25] -->
m

<!-- b008289 | references | pages [25] -->
m

<!-- b008290 | references | pages [25] -->
m

<!-- b008291 | references | pages [25] -->
m

<!-- b008292 | references | pages [25] -->
m

<!-- b008293 | references | pages [25] -->
m

<!-- b008294 | references | pages [25] -->
m

<!-- b008295 | references | pages [25] -->
m

<!-- b008296 | references | pages [25] -->
m

<!-- b008297 | references | pages [25] -->
m

<!-- b008298 | references | pages [25] -->
m

<!-- b008299 | references | pages [25] -->
m

<!-- b008300 | references | pages [25] -->
m

<!-- b008301 | references | pages [25] -->
m

<!-- b008302 | references | pages [25] -->
m

<!-- b008303 | references | pages [25] -->
m

<!-- b008304 | references | pages [25] -->
m

<!-- b008305 | references | pages [25] -->
m

<!-- b008306 | references | pages [25] -->
m

<!-- b008307 | references | pages [25] -->
m

<!-- b008308 | references | pages [25] -->
m

<!-- b008309 | references | pages [25] -->
m

<!-- b008310 | references | pages [25] -->
m

<!-- b008311 | references | pages [25] -->
m

<!-- b008312 | references | pages [25] -->
m

<!-- b008313 | references | pages [25] -->
m

<!-- b008314 | references | pages [25] -->
m

<!-- b008315 | references | pages [25] -->
m

<!-- b008316 | references | pages [25] -->
m

<!-- b008317 | references | pages [25] -->
m

<!-- b008318 | references | pages [25] -->
m

<!-- b008319 | references | pages [25] -->
m

<!-- b008320 | references | pages [25] -->
m

<!-- b008321 | references | pages [25] -->
m

<!-- b008322 | references | pages [25] -->
m

<!-- b008323 | references | pages [25] -->
m

<!-- b008324 | references | pages [25] -->
m

<!-- b008325 | references | pages [25] -->
m

<!-- b008326 | references | pages [25] -->
m

<!-- b008327 | references | pages [25] -->
m

<!-- b008328 | references | pages [25] -->
m

<!-- b008329 | references | pages [25] -->
m

<!-- b008330 | references | pages [25] -->
m

<!-- b008331 | references | pages [25] -->
m

<!-- b008332 | references | pages [25] -->
m

<!-- b008333 | references | pages [25] -->
m

<!-- b008334 | references | pages [25] -->
m

<!-- b008335 | references | pages [25] -->
m

<!-- b008336 | references | pages [25] -->
m

<!-- b008337 | references | pages [25] -->
m

<!-- b008338 | references | pages [25] -->
m

<!-- b008339 | references | pages [25] -->
m

<!-- b008340 | references | pages [25] -->
m

<!-- b008341 | references | pages [25] -->
m

<!-- b008342 | references | pages [25] -->
m

<!-- b008343 | references | pages [25] -->
m

<!-- b008344 | references | pages [25] -->
m

<!-- b008345 | references | pages [25] -->
m

<!-- b008346 | references | pages [25] -->
m

<!-- b008347 | references | pages [25] -->
m

<!-- b008348 | references | pages [25] -->
m

<!-- b008349 | references | pages [25] -->
m

<!-- b008350 | references | pages [25] -->
m

<!-- b008351 | references | pages [25] -->
m

<!-- b008352 | references | pages [25] -->
m

<!-- b008353 | references | pages [25] -->
m

<!-- b008354 | references | pages [25] -->
m

<!-- b008355 | references | pages [25] -->
m

<!-- b008356 | references | pages [25] -->
m

<!-- b008357 | references | pages [25] -->
m

<!-- b008358 | references | pages [25] -->
m

<!-- b008359 | references | pages [25] -->
m

<!-- b008360 | references | pages [25] -->
m

<!-- b008361 | references | pages [25] -->
m

<!-- b008362 | references | pages [25] -->
m

<!-- b008363 | references | pages [25] -->
m

<!-- b008364 | references | pages [25] -->
m

<!-- b008365 | references | pages [25] -->
m

<!-- b008366 | references | pages [25] -->
m

<!-- b008367 | references | pages [25] -->
m

<!-- b008368 | references | pages [25] -->
m

<!-- b008369 | references | pages [25] -->
m

<!-- b008370 | references | pages [25] -->
m

<!-- b008371 | references | pages [25] -->
m

<!-- b008372 | references | pages [25] -->
m

<!-- b008373 | references | pages [25] -->
m

<!-- b008374 | references | pages [25] -->
m

<!-- b008375 | references | pages [25] -->
m

<!-- b008376 | references | pages [25] -->
m

<!-- b008377 | references | pages [25] -->
m

<!-- b008378 | references | pages [25] -->
m

<!-- b008379 | references | pages [25] -->
m

<!-- b008380 | references | pages [25] -->
m

<!-- b008381 | references | pages [25] -->
m

<!-- b008382 | references | pages [25] -->
m

<!-- b008383 | references | pages [25] -->
m

<!-- b008384 | references | pages [25] -->
m

<!-- b008385 | references | pages [25] -->
m

<!-- b008386 | references | pages [25] -->
m

<!-- b008387 | references | pages [25] -->
m

<!-- b008388 | references | pages [25] -->
m

<!-- b008389 | references | pages [25] -->
m

<!-- b008390 | references | pages [25] -->
m

<!-- b008391 | references | pages [25] -->
m

<!-- b008392 | references | pages [25] -->
m

<!-- b008393 | references | pages [25] -->
m

<!-- b008394 | references | pages [25] -->
m

<!-- b008395 | references | pages [25] -->
m

<!-- b008396 | references | pages [25] -->
m

<!-- b008397 | references | pages [25] -->
m

<!-- b008398 | references | pages [25] -->
m

<!-- b008399 | references | pages [25] -->
m

<!-- b008400 | references | pages [25] -->
m

<!-- b008401 | references | pages [25] -->
m

<!-- b008402 | references | pages [25] -->
m

<!-- b008403 | references | pages [25] -->
m

<!-- b008404 | references | pages [25] -->
m

<!-- b008405 | references | pages [25] -->
m

<!-- b008406 | references | pages [25] -->
m

<!-- b008407 | references | pages [25] -->
m

<!-- b008408 | references | pages [25] -->
m

<!-- b008409 | references | pages [25] -->
m

<!-- b008410 | references | pages [25] -->
m

<!-- b008411 | references | pages [25] -->
m

<!-- b008412 | references | pages [25] -->
m

<!-- b008413 | references | pages [25] -->
m

<!-- b008414 | references | pages [25] -->
m

<!-- b008415 | references | pages [25] -->
m

<!-- b008416 | references | pages [25] -->
m

<!-- b008417 | references | pages [25] -->
m

<!-- b008418 | references | pages [25] -->
m

<!-- b008419 | references | pages [25] -->
m

<!-- b008420 | references | pages [25] -->
m

<!-- b008421 | references | pages [25] -->
m

<!-- b008422 | references | pages [25] -->
m

<!-- b008423 | references | pages [25] -->
m

<!-- b008424 | references | pages [25] -->
m

<!-- b008425 | references | pages [25] -->
m

<!-- b008426 | references | pages [25] -->
m

<!-- b008427 | references | pages [25] -->
m

<!-- b008428 | references | pages [25] -->
m

<!-- b008429 | references | pages [25] -->
m

<!-- b008430 | references | pages [25] -->
m

<!-- b008431 | references | pages [25] -->
m

<!-- b008432 | references | pages [25] -->
m

<!-- b008433 | references | pages [25] -->
m

<!-- b008434 | references | pages [25] -->
m

<!-- b008435 | references | pages [25] -->
m

<!-- b008436 | references | pages [25] -->
m

<!-- b008437 | furniture | pages [25] -->
m

<!-- b008438 | furniture | pages [25] -->
m

<!-- b008439 | furniture | pages [25] -->
m

<!-- b008440 | furniture | pages [25] -->
m

<!-- b008441 | furniture | pages [25] -->
m

<!-- b008442 | furniture | pages [25] -->
m

<!-- b008443 | furniture | pages [25] -->
m

<!-- b008444 | furniture | pages [25] -->
m

<!-- b008445 | furniture | pages [25] -->
m

<!-- b008446 | furniture | pages [25] -->
m

<!-- b008447 | furniture | pages [25] -->
m

<!-- b008448 | furniture | pages [25] -->
m

<!-- b008449 | furniture | pages [25] -->
m

<!-- b008450 | furniture | pages [25] -->
m

<!-- b008451 | furniture | pages [25] -->
m

<!-- b008452 | furniture | pages [25] -->
m

<!-- b008453 | furniture | pages [25] -->
m

<!-- b008454 | furniture | pages [25] -->
m

<!-- b008455 | furniture | pages [25] -->
m

<!-- b008456 | furniture | pages [25] -->
m

<!-- b008457 | furniture | pages [25] -->
m

<!-- b008458 | furniture | pages [25] -->
m

<!-- b008459 | furniture | pages [25] -->
m

<!-- b008460 | furniture | pages [25] -->
m

<!-- b008461 | furniture | pages [25] -->
m

<!-- b008462 | furniture | pages [25] -->
m

<!-- b008463 | furniture | pages [25] -->
m

<!-- b008464 | furniture | pages [25] -->
m

<!-- b008465 | furniture | pages [25] -->
m

<!-- b008466 | furniture | pages [25] -->
m

<!-- b008467 | furniture | pages [25] -->
m

<!-- b008468 | furniture | pages [25] -->
m

<!-- b008469 | furniture | pages [25] -->
m

<!-- b008470 | furniture | pages [25] -->
m

<!-- b008471 | furniture | pages [25] -->
m

<!-- b008472 | furniture | pages [25] -->
m

<!-- b008473 | furniture | pages [25] -->
m

<!-- b008474 | furniture | pages [25] -->
m

<!-- b008475 | furniture | pages [25] -->
m

<!-- b008476 | furniture | pages [25] -->
m

<!-- b008477 | furniture | pages [25] -->
m

<!-- b008478 | furniture | pages [25] -->
m

<!-- b008479 | furniture | pages [25] -->
m

<!-- b008480 | furniture | pages [25] -->
m

<!-- b008481 | furniture | pages [25] -->
m

<!-- b008482 | furniture | pages [25] -->
m

<!-- b008483 | furniture | pages [25] -->
m

<!-- b008484 | furniture | pages [25] -->
m

<!-- b008485 | furniture | pages [25] -->
m

<!-- b008486 | furniture | pages [25] -->
m

<!-- b008487 | furniture | pages [25] -->
m

<!-- b008488 | furniture | pages [25] -->
m

<!-- b008489 | furniture | pages [25] -->
m

<!-- b008490 | furniture | pages [25] -->
m

<!-- b008491 | furniture | pages [25] -->
m

<!-- b008492 | furniture | pages [25] -->
m

<!-- b008493 | furniture | pages [25] -->
m

<!-- b008494 | furniture | pages [25] -->
m

<!-- b008495 | furniture | pages [25] -->
m

<!-- b008496 | furniture | pages [25] -->
m

<!-- b008497 | furniture | pages [25] -->
m

<!-- b008498 | furniture | pages [25] -->
m

<!-- b008499 | furniture | pages [25] -->
m

<!-- b008500 | furniture | pages [25] -->
m

<!-- b008501 | furniture | pages [25] -->
m

<!-- b008502 | furniture | pages [25] -->
m

<!-- b008503 | furniture | pages [25] -->
m

<!-- b008504 | furniture | pages [25] -->
m

<!-- b008505 | furniture | pages [25] -->
m

<!-- b008506 | furniture | pages [25] -->
m

<!-- b008507 | furniture | pages [25] -->
m

<!-- b008508 | furniture | pages [25] -->
m

<!-- b008509 | furniture | pages [25] -->
m

<!-- b008510 | furniture | pages [25] -->
m

<!-- b008511 | furniture | pages [25] -->
m

<!-- b008512 | furniture | pages [25] -->
m

<!-- b008513 | furniture | pages [25] -->
m

<!-- b008514 | furniture | pages [25] -->
m

<!-- b008515 | furniture | pages [25] -->
m

<!-- b008516 | furniture | pages [25] -->
m

<!-- b008517 | furniture | pages [25] -->
m

<!-- b008518 | furniture | pages [25] -->
m

<!-- b008519 | furniture | pages [25] -->
m

<!-- b008520 | furniture | pages [25] -->
m

<!-- b008521 | furniture | pages [25] -->
m

<!-- b008522 | furniture | pages [25] -->
m

<!-- b008523 | furniture | pages [25] -->
m

<!-- b008524 | furniture | pages [25] -->
m

<!-- b008525 | furniture | pages [25] -->
m

<!-- b008526 | furniture | pages [25] -->
m

<!-- b008527 | furniture | pages [25] -->
m

<!-- b008528 | furniture | pages [25] -->
m

<!-- b008529 | furniture | pages [25] -->
m

<!-- b008530 | furniture | pages [25] -->
m

<!-- b008531 | furniture | pages [25] -->
m

<!-- b008532 | furniture | pages [25] -->
m

<!-- b008533 | furniture | pages [25] -->
m

<!-- b008534 | furniture | pages [25] -->
m

<!-- b008535 | furniture | pages [25] -->
m

<!-- b008536 | furniture | pages [25] -->
m

<!-- b008537 | furniture | pages [25] -->
m

<!-- b008538 | furniture | pages [25] -->
m

<!-- b008539 | furniture | pages [25] -->
m

<!-- b008540 | furniture | pages [25] -->
m

<!-- b008541 | furniture | pages [25] -->
m

<!-- b008542 | furniture | pages [25] -->
m

<!-- b008543 | furniture | pages [25] -->
m

<!-- b008544 | furniture | pages [25] -->
m

<!-- b008545 | furniture | pages [25] -->
m

<!-- b008546 | furniture | pages [25] -->
m

<!-- b008547 | furniture | pages [25] -->
m

<!-- b008548 | furniture | pages [25] -->
m

<!-- b008549 | furniture | pages [25] -->
m

<!-- b008550 | furniture | pages [25] -->
m

<!-- b008551 | furniture | pages [25] -->
m

<!-- b008552 | furniture | pages [25] -->
m

<!-- b008553 | furniture | pages [25] -->
m

<!-- b008554 | furniture | pages [25] -->
m

<!-- b008555 | furniture | pages [25] -->
m

<!-- b008556 | furniture | pages [25] -->
m

<!-- b008557 | furniture | pages [25] -->
m

<!-- b008558 | furniture | pages [25] -->
m

<!-- b008559 | furniture | pages [25] -->
m

<!-- b008560 | furniture | pages [25] -->
m

<!-- b008561 | furniture | pages [25] -->
m

<!-- b008562 | furniture | pages [25] -->
m

<!-- b008563 | furniture | pages [25] -->
m

<!-- b008564 | furniture | pages [25] -->
m

<!-- b008565 | furniture | pages [25] -->
m

<!-- b008566 | furniture | pages [25] -->
m

<!-- b008567 | furniture | pages [25] -->
m

<!-- b008568 | furniture | pages [25] -->
m

<!-- b008569 | furniture | pages [25] -->
m

<!-- b008570 | furniture | pages [25] -->
m

<!-- b008571 | furniture | pages [25] -->
m

<!-- b008572 | furniture | pages [25] -->
m

<!-- b008573 | furniture | pages [25] -->
m

<!-- b008574 | furniture | pages [25] -->
m

<!-- b008575 | furniture | pages [25] -->
m

<!-- b008576 | furniture | pages [25] -->
m

<!-- b008577 | furniture | pages [25] -->
m

<!-- b008578 | furniture | pages [25] -->
m

<!-- b008579 | furniture | pages [25] -->
m

<!-- b008580 | furniture | pages [25] -->
m

<!-- b008581 | furniture | pages [25] -->
m

<!-- b008582 | furniture | pages [25] -->
m

<!-- b008583 | furniture | pages [25] -->
m

<!-- b008584 | furniture | pages [25] -->
m

<!-- b008585 | furniture | pages [25] -->
m

<!-- b008586 | furniture | pages [25] -->
m

<!-- b008587 | furniture | pages [25] -->
m

<!-- b008588 | furniture | pages [25] -->
m

<!-- b008589 | furniture | pages [25] -->
m

<!-- b008590 | furniture | pages [25] -->
m

<!-- b008591 | furniture | pages [25] -->
m

<!-- b008592 | furniture | pages [25] -->
m

<!-- b008593 | furniture | pages [25] -->
m

<!-- b008594 | furniture | pages [25] -->
m

<!-- b008595 | furniture | pages [25] -->
m

<!-- b008596 | furniture | pages [25] -->
m

<!-- b008597 | furniture | pages [25] -->
m

<!-- b008598 | furniture | pages [25] -->
m

<!-- b008599 | furniture | pages [25] -->
m

<!-- b008600 | furniture | pages [25] -->
m

<!-- b008601 | furniture | pages [25] -->
m

<!-- b008602 | furniture | pages [25] -->
m

<!-- b008603 | furniture | pages [25] -->
m

<!-- b008604 | furniture | pages [25] -->
m

<!-- b008605 | furniture | pages [25] -->
m

<!-- b008606 | furniture | pages [25] -->
m

<!-- b008607 | furniture | pages [25] -->
m

<!-- b008608 | furniture | pages [25] -->
m

<!-- b008609 | furniture | pages [25] -->
m

<!-- b008610 | furniture | pages [25] -->
m

<!-- b008611 | furniture | pages [25] -->
m

<!-- b008612 | furniture | pages [25] -->
m

<!-- b008613 | furniture | pages [25] -->
m

<!-- b008614 | furniture | pages [25] -->
m

<!-- b008615 | furniture | pages [25] -->
m

<!-- b008616 | furniture | pages [25] -->
m

<!-- b008617 | furniture | pages [25] -->
m

<!-- b008618 | furniture | pages [25] -->
m

<!-- b008619 | furniture | pages [25] -->
m

<!-- b008620 | furniture | pages [25] -->
m

<!-- b008621 | furniture | pages [25] -->
m

<!-- b008622 | furniture | pages [25] -->
m

<!-- b008623 | furniture | pages [25] -->
m

<!-- b008624 | furniture | pages [25] -->
m

<!-- b008625 | furniture | pages [25] -->
m

<!-- b008626 | furniture | pages [25] -->
m

<!-- b008627 | furniture | pages [25] -->
m

<!-- b008628 | furniture | pages [25] -->
m

<!-- b008629 | furniture | pages [25] -->
m

<!-- b008630 | furniture | pages [25] -->
m

<!-- b008631 | furniture | pages [25] -->
m

<!-- b008632 | furniture | pages [25] -->
m

<!-- b008633 | furniture | pages [25] -->
m

<!-- b008634 | furniture | pages [25] -->
m

<!-- b008635 | furniture | pages [25] -->
m

<!-- b008636 | furniture | pages [25] -->
m

<!-- b008637 | furniture | pages [25] -->
m

<!-- b008638 | furniture | pages [25] -->
m

<!-- b008639 | furniture | pages [25] -->
m

<!-- b008640 | furniture | pages [25] -->
m

<!-- b008641 | furniture | pages [25] -->
m

<!-- b008642 | furniture | pages [25] -->
m

<!-- b008643 | furniture | pages [25] -->
m

<!-- b008644 | furniture | pages [25] -->
m

<!-- b008645 | furniture | pages [25] -->
m

<!-- b008646 | furniture | pages [25] -->
m

<!-- b008647 | furniture | pages [25] -->
m

<!-- b008648 | furniture | pages [25] -->
m

<!-- b008649 | furniture | pages [25] -->
m

<!-- b008650 | furniture | pages [25] -->
m

<!-- b008651 | furniture | pages [25] -->
m

<!-- b008652 | furniture | pages [25] -->
m

<!-- b008653 | furniture | pages [25] -->
m

<!-- b008654 | furniture | pages [25] -->
m

<!-- b008655 | furniture | pages [25] -->
m

<!-- b008656 | furniture | pages [25] -->
m

<!-- b008657 | furniture | pages [25] -->
m

<!-- b008658 | furniture | pages [25] -->
m

<!-- b008659 | furniture | pages [25] -->
m

<!-- b008660 | furniture | pages [25] -->
m

<!-- b008661 | furniture | pages [25] -->
m

<!-- b008662 | furniture | pages [25] -->
m

<!-- b008663 | furniture | pages [25] -->
m

<!-- b008664 | furniture | pages [25] -->
m

<!-- b008665 | furniture | pages [25] -->
m

<!-- b008666 | furniture | pages [25] -->
m

<!-- b008667 | furniture | pages [25] -->
m

<!-- b008668 | furniture | pages [25] -->
m

<!-- b008669 | furniture | pages [25] -->
m

<!-- b008670 | furniture | pages [25] -->
m

<!-- b008671 | furniture | pages [25] -->
m

<!-- b008672 | furniture | pages [25] -->
m

<!-- b008673 | furniture | pages [25] -->
m

<!-- b008674 | furniture | pages [25] -->
m

<!-- b008675 | furniture | pages [25] -->
m

<!-- b008676 | furniture | pages [25] -->
m

<!-- b008677 | furniture | pages [25] -->
m

<!-- b008678 | furniture | pages [25] -->
m

<!-- b008679 | furniture | pages [25] -->
m

<!-- b008680 | furniture | pages [25] -->
m

<!-- b008681 | furniture | pages [25] -->
m

<!-- b008682 | furniture | pages [25] -->
m

<!-- b008683 | furniture | pages [25] -->
m

<!-- b008684 | furniture | pages [25] -->
m

<!-- b008685 | furniture | pages [25] -->
m

<!-- b008686 | furniture | pages [25] -->
m

<!-- b008687 | furniture | pages [25] -->
m

<!-- b008688 | furniture | pages [25] -->
m

<!-- b008689 | furniture | pages [25] -->
m

<!-- b008690 | furniture | pages [25] -->
m

<!-- b008691 | furniture | pages [25] -->
m

<!-- b008692 | furniture | pages [25] -->
m

<!-- b008693 | furniture | pages [25] -->
m

<!-- b008694 | furniture | pages [25] -->
m

<!-- b008695 | furniture | pages [25] -->
m

<!-- b008696 | furniture | pages [25] -->
m

<!-- b008697 | furniture | pages [25] -->
m

<!-- b008698 | furniture | pages [25] -->
m

<!-- b008699 | furniture | pages [25] -->
m

<!-- b008700 | furniture | pages [25] -->
m

<!-- b008701 | furniture | pages [25] -->
m

<!-- b008702 | furniture | pages [25] -->
m

<!-- b008703 | furniture | pages [25] -->
m

<!-- b008704 | furniture | pages [25] -->
m

<!-- b008705 | furniture | pages [25] -->
m

<!-- b008706 | furniture | pages [25] -->
m

<!-- b008707 | furniture | pages [25] -->
m

<!-- b008708 | furniture | pages [25] -->
m

<!-- b008709 | furniture | pages [25] -->
m

<!-- b008710 | furniture | pages [25] -->
m

<!-- b008711 | furniture | pages [25] -->
m

<!-- b008712 | furniture | pages [25] -->
m

<!-- b008713 | furniture | pages [25] -->
m

<!-- b008714 | furniture | pages [25] -->
m

<!-- b008715 | furniture | pages [25] -->
m

<!-- b008716 | furniture | pages [25] -->
m

<!-- b008717 | furniture | pages [25] -->
m

<!-- b008718 | furniture | pages [25] -->
m

<!-- b008719 | furniture | pages [25] -->
m

<!-- b008720 | furniture | pages [25] -->
m

<!-- b008721 | furniture | pages [25] -->
m

<!-- b008722 | furniture | pages [25] -->
m

<!-- b008723 | furniture | pages [25] -->
m

<!-- b008724 | furniture | pages [25] -->
m

<!-- b008725 | furniture | pages [25] -->
m

<!-- b008726 | furniture | pages [25] -->
m

<!-- b008727 | furniture | pages [25] -->
m

<!-- b008728 | furniture | pages [25] -->
m

<!-- b008729 | furniture | pages [25] -->
m

<!-- b008730 | furniture | pages [25] -->
m

<!-- b008731 | furniture | pages [25] -->
m

<!-- b008732 | furniture | pages [25] -->
m

<!-- b008733 | furniture | pages [25] -->
m

<!-- b008734 | furniture | pages [25] -->
m

<!-- b008735 | furniture | pages [25] -->
m

<!-- b008736 | furniture | pages [25] -->
m

<!-- b008737 | furniture | pages [25] -->
m

<!-- b008738 | furniture | pages [25] -->
m

<!-- b008739 | furniture | pages [25] -->
m

<!-- b008740 | furniture | pages [25] -->
m

<!-- b008741 | furniture | pages [25] -->
m

<!-- b008742 | furniture | pages [25] -->
m

<!-- b008743 | furniture | pages [25] -->
m

<!-- b008744 | furniture | pages [25] -->
m

<!-- b008745 | furniture | pages [25] -->
m

<!-- b008746 | furniture | pages [25] -->
m

<!-- b008747 | furniture | pages [25] -->
m

<!-- b008748 | furniture | pages [25] -->
m

<!-- b008749 | furniture | pages [25] -->
m

<!-- b008750 | furniture | pages [25] -->
m

<!-- b008751 | furniture | pages [25] -->
m

<!-- b008752 | furniture | pages [25] -->
m

<!-- b008753 | furniture | pages [25] -->
m

<!-- b008754 | furniture | pages [25] -->
m

<!-- b008755 | furniture | pages [25] -->
m

<!-- b008756 | furniture | pages [25] -->
m

<!-- b008757 | furniture | pages [25] -->
m

<!-- b008758 | furniture | pages [25] -->
m

<!-- b008759 | furniture | pages [25] -->
m

<!-- b008760 | furniture | pages [25] -->
m

<!-- b008761 | furniture | pages [25] -->
m

<!-- b008762 | furniture | pages [25] -->
m

<!-- b008763 | furniture | pages [25] -->
m

<!-- b008764 | furniture | pages [25] -->
m

<!-- b008765 | furniture | pages [25] -->
m

<!-- b008766 | furniture | pages [25] -->
m

<!-- b008767 | furniture | pages [25] -->
m

<!-- b008768 | furniture | pages [25] -->
m

<!-- b008769 | furniture | pages [25] -->
m

<!-- b008770 | furniture | pages [25] -->
m

<!-- b008771 | furniture | pages [25] -->
m

<!-- b008772 | furniture | pages [25] -->
m

<!-- b008773 | furniture | pages [25] -->
m

<!-- b008774 | furniture | pages [25] -->
m

<!-- b008775 | furniture | pages [25] -->
m

<!-- b008776 | furniture | pages [25] -->
m

<!-- b008777 | furniture | pages [25] -->
m

<!-- b008778 | furniture | pages [25] -->
m

<!-- b008779 | furniture | pages [25] -->
m

<!-- b008780 | furniture | pages [25] -->
m

<!-- b008781 | furniture | pages [25] -->
m

<!-- b008782 | furniture | pages [25] -->
m

<!-- b008783 | furniture | pages [25] -->
m

<!-- b008784 | furniture | pages [25] -->
m

<!-- b008785 | furniture | pages [25] -->
m

<!-- b008786 | furniture | pages [25] -->
m

<!-- b008787 | furniture | pages [25] -->
m

<!-- b008788 | furniture | pages [25] -->
m

<!-- b008789 | furniture | pages [25] -->
m

<!-- b008790 | furniture | pages [25] -->
m

<!-- b008791 | furniture | pages [25] -->
m

<!-- b008792 | furniture | pages [25] -->
m

<!-- b008793 | furniture | pages [25] -->
m

<!-- b008794 | furniture | pages [25] -->
m

<!-- b008795 | furniture | pages [25] -->
m

<!-- b008796 | furniture | pages [25] -->
m

<!-- b008797 | furniture | pages [25] -->
m

<!-- b008798 | furniture | pages [25] -->
m

<!-- b008799 | furniture | pages [25] -->
m

<!-- b008800 | furniture | pages [25] -->
m

<!-- b008801 | furniture | pages [25] -->
m

<!-- b008802 | furniture | pages [25] -->
m

<!-- b008803 | furniture | pages [25] -->
m

<!-- b008804 | furniture | pages [25] -->
m

<!-- b008805 | furniture | pages [25] -->
m

<!-- b008806 | furniture | pages [25] -->
m

<!-- b008807 | furniture | pages [25] -->
m

<!-- b008808 | furniture | pages [25] -->
m

<!-- b008809 | furniture | pages [25] -->
m

<!-- b008810 | furniture | pages [25] -->
m

<!-- b008811 | furniture | pages [25] -->
m

<!-- b008812 | furniture | pages [25] -->
m

<!-- b008813 | furniture | pages [25] -->
m

<!-- b008814 | furniture | pages [25] -->
m

<!-- b008815 | furniture | pages [25] -->
m

<!-- b008816 | furniture | pages [25] -->
m

<!-- b008817 | furniture | pages [25] -->
m

<!-- b008818 | furniture | pages [25] -->
m

<!-- b008819 | furniture | pages [25] -->
m

<!-- b008820 | furniture | pages [25] -->
m

<!-- b008821 | furniture | pages [25] -->
m

<!-- b008822 | furniture | pages [25] -->
m

<!-- b008823 | furniture | pages [25] -->
m

<!-- b008824 | furniture | pages [25] -->
m

<!-- b008825 | furniture | pages [25] -->
m

<!-- b008826 | furniture | pages [25] -->
m

<!-- b008827 | furniture | pages [25] -->
m

<!-- b008828 | furniture | pages [25] -->
m

<!-- b008829 | furniture | pages [25] -->
m

<!-- b008830 | furniture | pages [25] -->
m

<!-- b008831 | furniture | pages [25] -->
m

<!-- b008832 | furniture | pages [25] -->
m

<!-- b008833 | furniture | pages [25] -->
m

<!-- b008834 | furniture | pages [25] -->
m

<!-- b008835 | furniture | pages [25] -->
m

<!-- b008836 | furniture | pages [25] -->
m

<!-- b008837 | furniture | pages [25] -->
m

<!-- b008838 | furniture | pages [25] -->
m

<!-- b008839 | furniture | pages [25] -->
m

<!-- b008840 | furniture | pages [26] -->
Team # 2503389

<!-- b008841 | furniture | pages [26] -->
Page 26 of 26

<!-- b008842 | heading | pages [26] -->
Report on Use of AI

<!-- b008843 | ai_disclosure | pages [26] -->
1. OpenAI ChatGPT (Nov 5, 2023 version, ChatGPT-4o)

<!-- b008844 | ai_disclosure | pages [26] -->
Query1: <Please provide the citation format for the report about United States Women’s

<!-- b008845 | ai_disclosure | pages [26] -->
Gymnastics and Béla and Marta Károlyi>

<!-- b008846 | ai_disclosure | pages [26] -->
Output: <Here is the citation format for the Wikipedia article on Béla Károlyi:Béla

<!-- b008847 | ai_disclosure | pages [26] -->
Károlyi. (2024, November 23). In Wikipedia, The Free Encyclopedia. Retrieved

<!-- b008848 | ai_disclosure | pages [26] -->
from https://en.wikipedia.org/wiki/BThis format includes the title of the article, the

<!-- b008849 | ai_disclosure | pages [26] -->
date of the last update, the source, and the URL for reference.>

<!-- b008850 | ai_disclosure | pages [26] -->
2. OpenAI ChatGPT (Nov 5, 2023 version, ChatGPT-4o)

<!-- b008851 | ai_disclosure | pages [26] -->
m

<!-- b008852 | ai_disclosure | pages [26] -->
m

<!-- b008853 | ai_disclosure | pages [26] -->
m

<!-- b008854 | ai_disclosure | pages [26] -->
m

<!-- b008855 | ai_disclosure | pages [26] -->
m

<!-- b008856 | ai_disclosure | pages [26] -->
m

<!-- b008857 | ai_disclosure | pages [26] -->
m

<!-- b008858 | ai_disclosure | pages [26] -->
m

<!-- b008859 | ai_disclosure | pages [26] -->
m

<!-- b008860 | ai_disclosure | pages [26] -->
m

<!-- b008861 | ai_disclosure | pages [26] -->
m

<!-- b008862 | ai_disclosure | pages [26] -->
m

<!-- b008863 | ai_disclosure | pages [26] -->
m

<!-- b008864 | ai_disclosure | pages [26] -->
m

<!-- b008865 | ai_disclosure | pages [26] -->
m

<!-- b008866 | ai_disclosure | pages [26] -->
m

<!-- b008867 | ai_disclosure | pages [26] -->
m

<!-- b008868 | ai_disclosure | pages [26] -->
m

<!-- b008869 | ai_disclosure | pages [26] -->
m

<!-- b008870 | ai_disclosure | pages [26] -->
m

<!-- b008871 | ai_disclosure | pages [26] -->
m

<!-- b008872 | ai_disclosure | pages [26] -->
m

<!-- b008873 | ai_disclosure | pages [26] -->
m

<!-- b008874 | ai_disclosure | pages [26] -->
m

<!-- b008875 | ai_disclosure | pages [26] -->
m

<!-- b008876 | ai_disclosure | pages [26] -->
m

<!-- b008877 | ai_disclosure | pages [26] -->
m

<!-- b008878 | ai_disclosure | pages [26] -->
m

<!-- b008879 | ai_disclosure | pages [26] -->
m

<!-- b008880 | ai_disclosure | pages [26] -->
m

<!-- b008881 | ai_disclosure | pages [26] -->
m

<!-- b008882 | ai_disclosure | pages [26] -->
m

<!-- b008883 | ai_disclosure | pages [26] -->
m

<!-- b008884 | ai_disclosure | pages [26] -->
m

<!-- b008885 | ai_disclosure | pages [26] -->
m

<!-- b008886 | ai_disclosure | pages [26] -->
m

<!-- b008887 | ai_disclosure | pages [26] -->
m

<!-- b008888 | ai_disclosure | pages [26] -->
m

<!-- b008889 | ai_disclosure | pages [26] -->
m

<!-- b008890 | ai_disclosure | pages [26] -->
m

<!-- b008891 | ai_disclosure | pages [26] -->
m

<!-- b008892 | ai_disclosure | pages [26] -->
m

<!-- b008893 | ai_disclosure | pages [26] -->
m

<!-- b008894 | ai_disclosure | pages [26] -->
m

<!-- b008895 | ai_disclosure | pages [26] -->
m

<!-- b008896 | ai_disclosure | pages [26] -->
m

<!-- b008897 | ai_disclosure | pages [26] -->
m

<!-- b008898 | ai_disclosure | pages [26] -->
m

<!-- b008899 | ai_disclosure | pages [26] -->
m

<!-- b008900 | ai_disclosure | pages [26] -->
m

<!-- b008901 | ai_disclosure | pages [26] -->
m

<!-- b008902 | ai_disclosure | pages [26] -->
m

<!-- b008903 | ai_disclosure | pages [26] -->
m

<!-- b008904 | ai_disclosure | pages [26] -->
Query1: <Please briefly explain the differences and similarities between MLR and FNN>

<!-- b008905 | ai_disclosure | pages [26] -->
m

<!-- b008906 | ai_disclosure | pages [26] -->
m

<!-- b008907 | ai_disclosure | pages [26] -->
m

<!-- b008908 | ai_disclosure | pages [26] -->
m

<!-- b008909 | ai_disclosure | pages [26] -->
m

<!-- b008910 | ai_disclosure | pages [26] -->
m

<!-- b008911 | ai_disclosure | pages [26] -->
m

<!-- b008912 | ai_disclosure | pages [26] -->
m

<!-- b008913 | ai_disclosure | pages [26] -->
m

<!-- b008914 | ai_disclosure | pages [26] -->
m

<!-- b008915 | ai_disclosure | pages [26] -->
m

<!-- b008916 | ai_disclosure | pages [26] -->
m

<!-- b008917 | ai_disclosure | pages [26] -->
m

<!-- b008918 | ai_disclosure | pages [26] -->
m

<!-- b008919 | ai_disclosure | pages [26] -->
m

<!-- b008920 | ai_disclosure | pages [26] -->
m

<!-- b008921 | ai_disclosure | pages [26] -->
m

<!-- b008922 | ai_disclosure | pages [26] -->
m

<!-- b008923 | ai_disclosure | pages [26] -->
m

<!-- b008924 | ai_disclosure | pages [26] -->
m

<!-- b008925 | ai_disclosure | pages [26] -->
m

<!-- b008926 | ai_disclosure | pages [26] -->
m

<!-- b008927 | ai_disclosure | pages [26] -->
m

<!-- b008928 | ai_disclosure | pages [26] -->
m

<!-- b008929 | ai_disclosure | pages [26] -->
m

<!-- b008930 | ai_disclosure | pages [26] -->
m

<!-- b008931 | ai_disclosure | pages [26] -->
m

<!-- b008932 | ai_disclosure | pages [26] -->
m

<!-- b008933 | ai_disclosure | pages [26] -->
m

<!-- b008934 | ai_disclosure | pages [26] -->
m

<!-- b008935 | ai_disclosure | pages [26] -->
m

<!-- b008936 | ai_disclosure | pages [26] -->
m

<!-- b008937 | ai_disclosure | pages [26] -->
m

<!-- b008938 | ai_disclosure | pages [26] -->
m

<!-- b008939 | ai_disclosure | pages [26] -->
m

<!-- b008940 | ai_disclosure | pages [26] -->
m

<!-- b008941 | ai_disclosure | pages [26] -->
m

<!-- b008942 | ai_disclosure | pages [26] -->
m

<!-- b008943 | ai_disclosure | pages [26] -->
m

<!-- b008944 | ai_disclosure | pages [26] -->
m

<!-- b008945 | ai_disclosure | pages [26] -->
m

<!-- b008946 | ai_disclosure | pages [26] -->
m

<!-- b008947 | ai_disclosure | pages [26] -->
m

<!-- b008948 | ai_disclosure | pages [26] -->
m

<!-- b008949 | ai_disclosure | pages [26] -->
m

<!-- b008950 | ai_disclosure | pages [26] -->
m

<!-- b008951 | ai_disclosure | pages [26] -->
m

<!-- b008952 | ai_disclosure | pages [26] -->
m

<!-- b008953 | ai_disclosure | pages [26] -->
m

<!-- b008954 | ai_disclosure | pages [26] -->
m

<!-- b008955 | ai_disclosure | pages [26] -->
m

<!-- b008956 | ai_disclosure | pages [26] -->
m

<!-- b008957 | ai_disclosure | pages [26] -->
m

<!-- b008958 | ai_disclosure | pages [26] -->
m

<!-- b008959 | ai_disclosure | pages [26] -->
m

<!-- b008960 | ai_disclosure | pages [26] -->
m

<!-- b008961 | ai_disclosure | pages [26] -->
m

<!-- b008962 | ai_disclosure | pages [26] -->
m

<!-- b008963 | ai_disclosure | pages [26] -->
m

<!-- b008964 | ai_disclosure | pages [26] -->
m

<!-- b008965 | ai_disclosure | pages [26] -->
m

<!-- b008966 | ai_disclosure | pages [26] -->
m

<!-- b008967 | ai_disclosure | pages [26] -->
m

<!-- b008968 | ai_disclosure | pages [26] -->
m

<!-- b008969 | ai_disclosure | pages [26] -->
m

<!-- b008970 | ai_disclosure | pages [26] -->
m

<!-- b008971 | ai_disclosure | pages [26] -->
m

<!-- b008972 | ai_disclosure | pages [26] -->
m

<!-- b008973 | ai_disclosure | pages [26] -->
m

<!-- b008974 | ai_disclosure | pages [26] -->
m

<!-- b008975 | ai_disclosure | pages [26] -->
m

<!-- b008976 | ai_disclosure | pages [26] -->
m

<!-- b008977 | ai_disclosure | pages [26] -->
m

<!-- b008978 | ai_disclosure | pages [26] -->
m

<!-- b008979 | ai_disclosure | pages [26] -->
m

<!-- b008980 | ai_disclosure | pages [26] -->
m

<!-- b008981 | ai_disclosure | pages [26] -->
m

<!-- b008982 | ai_disclosure | pages [26] -->
m

<!-- b008983 | ai_disclosure | pages [26] -->
m

<!-- b008984 | ai_disclosure | pages [26] -->
m

<!-- b008985 | ai_disclosure | pages [26] -->
m

<!-- b008986 | ai_disclosure | pages [26] -->
m

<!-- b008987 | ai_disclosure | pages [26] -->
m

<!-- b008988 | ai_disclosure | pages [26] -->
m

<!-- b008989 | ai_disclosure | pages [26] -->
m

<!-- b008990 | ai_disclosure | pages [26] -->
m

<!-- b008991 | ai_disclosure | pages [26] -->
m

<!-- b008992 | ai_disclosure | pages [26] -->
m

<!-- b008993 | ai_disclosure | pages [26] -->
m

<!-- b008994 | ai_disclosure | pages [26] -->
m

<!-- b008995 | ai_disclosure | pages [26] -->
m

<!-- b008996 | ai_disclosure | pages [26] -->
m

<!-- b008997 | ai_disclosure | pages [26] -->
m

<!-- b008998 | ai_disclosure | pages [26] -->
m

<!-- b008999 | ai_disclosure | pages [26] -->
m

<!-- b009000 | ai_disclosure | pages [26] -->
m

<!-- b009001 | ai_disclosure | pages [26] -->
m

<!-- b009002 | ai_disclosure | pages [26] -->
m

<!-- b009003 | ai_disclosure | pages [26] -->
m

<!-- b009004 | ai_disclosure | pages [26] -->
m

<!-- b009005 | ai_disclosure | pages [26] -->
m

<!-- b009006 | ai_disclosure | pages [26] -->
m

<!-- b009007 | ai_disclosure | pages [26] -->
m

<!-- b009008 | ai_disclosure | pages [26] -->
m

<!-- b009009 | ai_disclosure | pages [26] -->
m

<!-- b009010 | ai_disclosure | pages [26] -->
m

<!-- b009011 | ai_disclosure | pages [26] -->
m

<!-- b009012 | ai_disclosure | pages [26] -->
m

<!-- b009013 | ai_disclosure | pages [26] -->
m

<!-- b009014 | ai_disclosure | pages [26] -->
m

<!-- b009015 | ai_disclosure | pages [26] -->
m

<!-- b009016 | ai_disclosure | pages [26] -->
m

<!-- b009017 | ai_disclosure | pages [26] -->
m

<!-- b009018 | ai_disclosure | pages [26] -->
m

<!-- b009019 | ai_disclosure | pages [26] -->
m

<!-- b009020 | ai_disclosure | pages [26] -->
m

<!-- b009021 | ai_disclosure | pages [26] -->
m

<!-- b009022 | ai_disclosure | pages [26] -->
m

<!-- b009023 | ai_disclosure | pages [26] -->
m

<!-- b009024 | ai_disclosure | pages [26] -->
m

<!-- b009025 | ai_disclosure | pages [26] -->
m

<!-- b009026 | ai_disclosure | pages [26] -->
m

<!-- b009027 | ai_disclosure | pages [26] -->
m

<!-- b009028 | ai_disclosure | pages [26] -->
m

<!-- b009029 | ai_disclosure | pages [26] -->
m

<!-- b009030 | ai_disclosure | pages [26] -->
m

<!-- b009031 | ai_disclosure | pages [26] -->
m

<!-- b009032 | ai_disclosure | pages [26] -->
m

<!-- b009033 | ai_disclosure | pages [26] -->
m

<!-- b009034 | ai_disclosure | pages [26] -->
m

<!-- b009035 | ai_disclosure | pages [26] -->
m

<!-- b009036 | ai_disclosure | pages [26] -->
m

<!-- b009037 | ai_disclosure | pages [26] -->
m

<!-- b009038 | ai_disclosure | pages [26] -->
m

<!-- b009039 | ai_disclosure | pages [26] -->
m

<!-- b009040 | ai_disclosure | pages [26] -->
m

<!-- b009041 | ai_disclosure | pages [26] -->
m

<!-- b009042 | ai_disclosure | pages [26] -->
m

<!-- b009043 | ai_disclosure | pages [26] -->
m

<!-- b009044 | ai_disclosure | pages [26] -->
m

<!-- b009045 | ai_disclosure | pages [26] -->
m

<!-- b009046 | ai_disclosure | pages [26] -->
m

<!-- b009047 | ai_disclosure | pages [26] -->
m

<!-- b009048 | ai_disclosure | pages [26] -->
m

<!-- b009049 | ai_disclosure | pages [26] -->
m

<!-- b009050 | ai_disclosure | pages [26] -->
m

<!-- b009051 | ai_disclosure | pages [26] -->
m

<!-- b009052 | ai_disclosure | pages [26] -->
m

<!-- b009053 | ai_disclosure | pages [26] -->
m

<!-- b009054 | ai_disclosure | pages [26] -->
m

<!-- b009055 | ai_disclosure | pages [26] -->
m

<!-- b009056 | ai_disclosure | pages [26] -->
m

<!-- b009057 | ai_disclosure | pages [26] -->
m

<!-- b009058 | ai_disclosure | pages [26] -->
m

<!-- b009059 | ai_disclosure | pages [26] -->
m

<!-- b009060 | ai_disclosure | pages [26] -->
m

<!-- b009061 | ai_disclosure | pages [26] -->
m

<!-- b009062 | ai_disclosure | pages [26] -->
m

<!-- b009063 | ai_disclosure | pages [26] -->
m

<!-- b009064 | ai_disclosure | pages [26] -->
m

<!-- b009065 | ai_disclosure | pages [26] -->
m

<!-- b009066 | ai_disclosure | pages [26] -->
m

<!-- b009067 | ai_disclosure | pages [26] -->
m

<!-- b009068 | ai_disclosure | pages [26] -->
m

<!-- b009069 | ai_disclosure | pages [26] -->
m

<!-- b009070 | ai_disclosure | pages [26] -->
m

<!-- b009071 | ai_disclosure | pages [26] -->
m

<!-- b009072 | ai_disclosure | pages [26] -->
m

<!-- b009073 | ai_disclosure | pages [26] -->
m

<!-- b009074 | ai_disclosure | pages [26] -->
m

<!-- b009075 | ai_disclosure | pages [26] -->
m

<!-- b009076 | ai_disclosure | pages [26] -->
m

<!-- b009077 | ai_disclosure | pages [26] -->
m

<!-- b009078 | ai_disclosure | pages [26] -->
m

<!-- b009079 | ai_disclosure | pages [26] -->
m

<!-- b009080 | ai_disclosure | pages [26] -->
m

<!-- b009081 | ai_disclosure | pages [26] -->
m

<!-- b009082 | ai_disclosure | pages [26] -->
m

<!-- b009083 | ai_disclosure | pages [26] -->
m

<!-- b009084 | ai_disclosure | pages [26] -->
m

<!-- b009085 | ai_disclosure | pages [26] -->
m

<!-- b009086 | ai_disclosure | pages [26] -->
m

<!-- b009087 | ai_disclosure | pages [26] -->
m

<!-- b009088 | ai_disclosure | pages [26] -->
m

<!-- b009089 | ai_disclosure | pages [26] -->
m

<!-- b009090 | ai_disclosure | pages [26] -->
m

<!-- b009091 | ai_disclosure | pages [26] -->
m

<!-- b009092 | ai_disclosure | pages [26] -->
m

<!-- b009093 | ai_disclosure | pages [26] -->
m

<!-- b009094 | ai_disclosure | pages [26] -->
m

<!-- b009095 | ai_disclosure | pages [26] -->
m

<!-- b009096 | ai_disclosure | pages [26] -->
Output: <Both Multiple Linear Regression (MLR) and Feedforward Neural Networks

<!-- b009097 | ai_disclosure | pages [26] -->
m

<!-- b009098 | ai_disclosure | pages [26] -->
m

<!-- b009099 | ai_disclosure | pages [26] -->
m

<!-- b009100 | ai_disclosure | pages [26] -->
m

<!-- b009101 | ai_disclosure | pages [26] -->
m

<!-- b009102 | ai_disclosure | pages [26] -->
m

<!-- b009103 | ai_disclosure | pages [26] -->
m

<!-- b009104 | ai_disclosure | pages [26] -->
m

<!-- b009105 | ai_disclosure | pages [26] -->
m

<!-- b009106 | ai_disclosure | pages [26] -->
m

<!-- b009107 | ai_disclosure | pages [26] -->
m

<!-- b009108 | ai_disclosure | pages [26] -->
m

<!-- b009109 | ai_disclosure | pages [26] -->
m

<!-- b009110 | ai_disclosure | pages [26] -->
m

<!-- b009111 | ai_disclosure | pages [26] -->
m

<!-- b009112 | ai_disclosure | pages [26] -->
m

<!-- b009113 | ai_disclosure | pages [26] -->
m

<!-- b009114 | ai_disclosure | pages [26] -->
m

<!-- b009115 | ai_disclosure | pages [26] -->
m

<!-- b009116 | ai_disclosure | pages [26] -->
m

<!-- b009117 | ai_disclosure | pages [26] -->
m

<!-- b009118 | ai_disclosure | pages [26] -->
m

<!-- b009119 | ai_disclosure | pages [26] -->
m

<!-- b009120 | ai_disclosure | pages [26] -->
m

<!-- b009121 | ai_disclosure | pages [26] -->
m

<!-- b009122 | ai_disclosure | pages [26] -->
m

<!-- b009123 | ai_disclosure | pages [26] -->
m

<!-- b009124 | ai_disclosure | pages [26] -->
m

<!-- b009125 | ai_disclosure | pages [26] -->
m

<!-- b009126 | ai_disclosure | pages [26] -->
m

<!-- b009127 | ai_disclosure | pages [26] -->
m

<!-- b009128 | ai_disclosure | pages [26] -->
m

<!-- b009129 | ai_disclosure | pages [26] -->
m

<!-- b009130 | ai_disclosure | pages [26] -->
m

<!-- b009131 | ai_disclosure | pages [26] -->
m

<!-- b009132 | ai_disclosure | pages [26] -->
m

<!-- b009133 | ai_disclosure | pages [26] -->
m

<!-- b009134 | ai_disclosure | pages [26] -->
m

<!-- b009135 | ai_disclosure | pages [26] -->
m

<!-- b009136 | ai_disclosure | pages [26] -->
m

<!-- b009137 | ai_disclosure | pages [26] -->
m

<!-- b009138 | ai_disclosure | pages [26] -->
m

<!-- b009139 | ai_disclosure | pages [26] -->
m

<!-- b009140 | ai_disclosure | pages [26] -->
m

<!-- b009141 | ai_disclosure | pages [26] -->
m

<!-- b009142 | ai_disclosure | pages [26] -->
m

<!-- b009143 | ai_disclosure | pages [26] -->
m

<!-- b009144 | ai_disclosure | pages [26] -->
m

<!-- b009145 | ai_disclosure | pages [26] -->
m

<!-- b009146 | ai_disclosure | pages [26] -->
m

<!-- b009147 | ai_disclosure | pages [26] -->
m

<!-- b009148 | ai_disclosure | pages [26] -->
m

<!-- b009149 | ai_disclosure | pages [26] -->
m

<!-- b009150 | ai_disclosure | pages [26] -->
m

<!-- b009151 | ai_disclosure | pages [26] -->
m

<!-- b009152 | ai_disclosure | pages [26] -->
m

<!-- b009153 | ai_disclosure | pages [26] -->
m

<!-- b009154 | ai_disclosure | pages [26] -->
m

<!-- b009155 | ai_disclosure | pages [26] -->
m

<!-- b009156 | ai_disclosure | pages [26] -->
m

<!-- b009157 | ai_disclosure | pages [26] -->
m

<!-- b009158 | ai_disclosure | pages [26] -->
m

<!-- b009159 | ai_disclosure | pages [26] -->
m

<!-- b009160 | ai_disclosure | pages [26] -->
m

<!-- b009161 | ai_disclosure | pages [26] -->
m

<!-- b009162 | ai_disclosure | pages [26] -->
m

<!-- b009163 | ai_disclosure | pages [26] -->
m

<!-- b009164 | ai_disclosure | pages [26] -->
m

<!-- b009165 | ai_disclosure | pages [26] -->
m

<!-- b009166 | ai_disclosure | pages [26] -->
m

<!-- b009167 | ai_disclosure | pages [26] -->
m

<!-- b009168 | ai_disclosure | pages [26] -->
m

<!-- b009169 | ai_disclosure | pages [26] -->
m

<!-- b009170 | ai_disclosure | pages [26] -->
m

<!-- b009171 | ai_disclosure | pages [26] -->
m

<!-- b009172 | ai_disclosure | pages [26] -->
m

<!-- b009173 | ai_disclosure | pages [26] -->
m

<!-- b009174 | ai_disclosure | pages [26] -->
m

<!-- b009175 | ai_disclosure | pages [26] -->
m

<!-- b009176 | ai_disclosure | pages [26] -->
m

<!-- b009177 | ai_disclosure | pages [26] -->
m

<!-- b009178 | ai_disclosure | pages [26] -->
m

<!-- b009179 | ai_disclosure | pages [26] -->
m

<!-- b009180 | ai_disclosure | pages [26] -->
m

<!-- b009181 | ai_disclosure | pages [26] -->
m

<!-- b009182 | ai_disclosure | pages [26] -->
m

<!-- b009183 | ai_disclosure | pages [26] -->
m

<!-- b009184 | ai_disclosure | pages [26] -->
m

<!-- b009185 | ai_disclosure | pages [26] -->
m

<!-- b009186 | ai_disclosure | pages [26] -->
m

<!-- b009187 | ai_disclosure | pages [26] -->
m

<!-- b009188 | ai_disclosure | pages [26] -->
m

<!-- b009189 | ai_disclosure | pages [26] -->
m

<!-- b009190 | ai_disclosure | pages [26] -->
m

<!-- b009191 | ai_disclosure | pages [26] -->
m

<!-- b009192 | ai_disclosure | pages [26] -->
m

<!-- b009193 | ai_disclosure | pages [26] -->
m

<!-- b009194 | ai_disclosure | pages [26] -->
m

<!-- b009195 | ai_disclosure | pages [26] -->
m

<!-- b009196 | ai_disclosure | pages [26] -->
m

<!-- b009197 | ai_disclosure | pages [26] -->
m

<!-- b009198 | ai_disclosure | pages [26] -->
m

<!-- b009199 | ai_disclosure | pages [26] -->
m

<!-- b009200 | ai_disclosure | pages [26] -->
m

<!-- b009201 | ai_disclosure | pages [26] -->
m

<!-- b009202 | ai_disclosure | pages [26] -->
m

<!-- b009203 | ai_disclosure | pages [26] -->
m

<!-- b009204 | ai_disclosure | pages [26] -->
m

<!-- b009205 | ai_disclosure | pages [26] -->
m

<!-- b009206 | ai_disclosure | pages [26] -->
m

<!-- b009207 | ai_disclosure | pages [26] -->
m

<!-- b009208 | ai_disclosure | pages [26] -->
m

<!-- b009209 | ai_disclosure | pages [26] -->
m

<!-- b009210 | ai_disclosure | pages [26] -->
m

<!-- b009211 | ai_disclosure | pages [26] -->
m

<!-- b009212 | ai_disclosure | pages [26] -->
m

<!-- b009213 | ai_disclosure | pages [26] -->
m

<!-- b009214 | ai_disclosure | pages [26] -->
m

<!-- b009215 | ai_disclosure | pages [26] -->
m

<!-- b009216 | ai_disclosure | pages [26] -->
m

<!-- b009217 | ai_disclosure | pages [26] -->
m

<!-- b009218 | ai_disclosure | pages [26] -->
m

<!-- b009219 | ai_disclosure | pages [26] -->
m

<!-- b009220 | ai_disclosure | pages [26] -->
m

<!-- b009221 | ai_disclosure | pages [26] -->
m

<!-- b009222 | ai_disclosure | pages [26] -->
m

<!-- b009223 | ai_disclosure | pages [26] -->
m

<!-- b009224 | ai_disclosure | pages [26] -->
m

<!-- b009225 | ai_disclosure | pages [26] -->
m

<!-- b009226 | ai_disclosure | pages [26] -->
m

<!-- b009227 | ai_disclosure | pages [26] -->
m

<!-- b009228 | ai_disclosure | pages [26] -->
m

<!-- b009229 | ai_disclosure | pages [26] -->
m

<!-- b009230 | ai_disclosure | pages [26] -->
m

<!-- b009231 | ai_disclosure | pages [26] -->
m

<!-- b009232 | ai_disclosure | pages [26] -->
m

<!-- b009233 | ai_disclosure | pages [26] -->
m

<!-- b009234 | ai_disclosure | pages [26] -->
m

<!-- b009235 | ai_disclosure | pages [26] -->
m

<!-- b009236 | ai_disclosure | pages [26] -->
m

<!-- b009237 | ai_disclosure | pages [26] -->
m

<!-- b009238 | ai_disclosure | pages [26] -->
m

<!-- b009239 | ai_disclosure | pages [26] -->
m

<!-- b009240 | ai_disclosure | pages [26] -->
(FNN) are supervised learning methods that aim to model the relationship between

<!-- b009241 | ai_disclosure | pages [26] -->
m

<!-- b009242 | ai_disclosure | pages [26] -->
m

<!-- b009243 | ai_disclosure | pages [26] -->
m

<!-- b009244 | ai_disclosure | pages [26] -->
m

<!-- b009245 | ai_disclosure | pages [26] -->
m

<!-- b009246 | ai_disclosure | pages [26] -->
m

<!-- b009247 | ai_disclosure | pages [26] -->
m

<!-- b009248 | ai_disclosure | pages [26] -->
m

<!-- b009249 | ai_disclosure | pages [26] -->
m

<!-- b009250 | ai_disclosure | pages [26] -->
m

<!-- b009251 | ai_disclosure | pages [26] -->
m

<!-- b009252 | ai_disclosure | pages [26] -->
m

<!-- b009253 | ai_disclosure | pages [26] -->
m

<!-- b009254 | ai_disclosure | pages [26] -->
m

<!-- b009255 | ai_disclosure | pages [26] -->
m

<!-- b009256 | ai_disclosure | pages [26] -->
m

<!-- b009257 | ai_disclosure | pages [26] -->
m

<!-- b009258 | ai_disclosure | pages [26] -->
m

<!-- b009259 | ai_disclosure | pages [26] -->
m

<!-- b009260 | ai_disclosure | pages [26] -->
m

<!-- b009261 | ai_disclosure | pages [26] -->
m

<!-- b009262 | ai_disclosure | pages [26] -->
m

<!-- b009263 | ai_disclosure | pages [26] -->
m

<!-- b009264 | ai_disclosure | pages [26] -->
m

<!-- b009265 | ai_disclosure | pages [26] -->
m

<!-- b009266 | ai_disclosure | pages [26] -->
m

<!-- b009267 | ai_disclosure | pages [26] -->
m

<!-- b009268 | ai_disclosure | pages [26] -->
m

<!-- b009269 | ai_disclosure | pages [26] -->
m

<!-- b009270 | ai_disclosure | pages [26] -->
m

<!-- b009271 | ai_disclosure | pages [26] -->
m

<!-- b009272 | ai_disclosure | pages [26] -->
m

<!-- b009273 | ai_disclosure | pages [26] -->
m

<!-- b009274 | ai_disclosure | pages [26] -->
m

<!-- b009275 | ai_disclosure | pages [26] -->
m

<!-- b009276 | ai_disclosure | pages [26] -->
m

<!-- b009277 | ai_disclosure | pages [26] -->
m

<!-- b009278 | ai_disclosure | pages [26] -->
m

<!-- b009279 | ai_disclosure | pages [26] -->
m

<!-- b009280 | ai_disclosure | pages [26] -->
m

<!-- b009281 | ai_disclosure | pages [26] -->
m

<!-- b009282 | ai_disclosure | pages [26] -->
m

<!-- b009283 | ai_disclosure | pages [26] -->
m

<!-- b009284 | ai_disclosure | pages [26] -->
m

<!-- b009285 | ai_disclosure | pages [26] -->
m

<!-- b009286 | ai_disclosure | pages [26] -->
m

<!-- b009287 | ai_disclosure | pages [26] -->
m

<!-- b009288 | ai_disclosure | pages [26] -->
m

<!-- b009289 | ai_disclosure | pages [26] -->
m

<!-- b009290 | ai_disclosure | pages [26] -->
m

<!-- b009291 | ai_disclosure | pages [26] -->
m

<!-- b009292 | ai_disclosure | pages [26] -->
m

<!-- b009293 | ai_disclosure | pages [26] -->
m

<!-- b009294 | ai_disclosure | pages [26] -->
m

<!-- b009295 | ai_disclosure | pages [26] -->
m

<!-- b009296 | ai_disclosure | pages [26] -->
m

<!-- b009297 | ai_disclosure | pages [26] -->
m

<!-- b009298 | ai_disclosure | pages [26] -->
m

<!-- b009299 | ai_disclosure | pages [26] -->
m

<!-- b009300 | ai_disclosure | pages [26] -->
m

<!-- b009301 | ai_disclosure | pages [26] -->
m

<!-- b009302 | ai_disclosure | pages [26] -->
m

<!-- b009303 | ai_disclosure | pages [26] -->
m

<!-- b009304 | ai_disclosure | pages [26] -->
m

<!-- b009305 | ai_disclosure | pages [26] -->
m

<!-- b009306 | ai_disclosure | pages [26] -->
m

<!-- b009307 | ai_disclosure | pages [26] -->
m

<!-- b009308 | ai_disclosure | pages [26] -->
m

<!-- b009309 | ai_disclosure | pages [26] -->
m

<!-- b009310 | ai_disclosure | pages [26] -->
m

<!-- b009311 | ai_disclosure | pages [26] -->
m

<!-- b009312 | ai_disclosure | pages [26] -->
m

<!-- b009313 | ai_disclosure | pages [26] -->
m

<!-- b009314 | ai_disclosure | pages [26] -->
m

<!-- b009315 | ai_disclosure | pages [26] -->
m

<!-- b009316 | ai_disclosure | pages [26] -->
m

<!-- b009317 | ai_disclosure | pages [26] -->
m

<!-- b009318 | ai_disclosure | pages [26] -->
m

<!-- b009319 | ai_disclosure | pages [26] -->
m

<!-- b009320 | ai_disclosure | pages [26] -->
m

<!-- b009321 | ai_disclosure | pages [26] -->
m

<!-- b009322 | ai_disclosure | pages [26] -->
m

<!-- b009323 | ai_disclosure | pages [26] -->
m

<!-- b009324 | ai_disclosure | pages [26] -->
m

<!-- b009325 | ai_disclosure | pages [26] -->
m

<!-- b009326 | ai_disclosure | pages [26] -->
m

<!-- b009327 | ai_disclosure | pages [26] -->
m

<!-- b009328 | ai_disclosure | pages [26] -->
m

<!-- b009329 | ai_disclosure | pages [26] -->
m

<!-- b009330 | ai_disclosure | pages [26] -->
m

<!-- b009331 | ai_disclosure | pages [26] -->
m

<!-- b009332 | ai_disclosure | pages [26] -->
m

<!-- b009333 | ai_disclosure | pages [26] -->
m

<!-- b009334 | ai_disclosure | pages [26] -->
m

<!-- b009335 | ai_disclosure | pages [26] -->
m

<!-- b009336 | ai_disclosure | pages [26] -->
m

<!-- b009337 | ai_disclosure | pages [26] -->
m

<!-- b009338 | ai_disclosure | pages [26] -->
m

<!-- b009339 | ai_disclosure | pages [26] -->
m

<!-- b009340 | ai_disclosure | pages [26] -->
m

<!-- b009341 | ai_disclosure | pages [26] -->
m

<!-- b009342 | ai_disclosure | pages [26] -->
m

<!-- b009343 | ai_disclosure | pages [26] -->
m

<!-- b009344 | ai_disclosure | pages [26] -->
m

<!-- b009345 | ai_disclosure | pages [26] -->
m

<!-- b009346 | ai_disclosure | pages [26] -->
m

<!-- b009347 | ai_disclosure | pages [26] -->
m

<!-- b009348 | ai_disclosure | pages [26] -->
m

<!-- b009349 | ai_disclosure | pages [26] -->
m

<!-- b009350 | ai_disclosure | pages [26] -->
m

<!-- b009351 | ai_disclosure | pages [26] -->
m

<!-- b009352 | ai_disclosure | pages [26] -->
m

<!-- b009353 | ai_disclosure | pages [26] -->
m

<!-- b009354 | ai_disclosure | pages [26] -->
m

<!-- b009355 | ai_disclosure | pages [26] -->
m

<!-- b009356 | ai_disclosure | pages [26] -->
m

<!-- b009357 | ai_disclosure | pages [26] -->
m

<!-- b009358 | ai_disclosure | pages [26] -->
m

<!-- b009359 | ai_disclosure | pages [26] -->
m

<!-- b009360 | ai_disclosure | pages [26] -->
m

<!-- b009361 | ai_disclosure | pages [26] -->
m

<!-- b009362 | ai_disclosure | pages [26] -->
m

<!-- b009363 | ai_disclosure | pages [26] -->
m

<!-- b009364 | ai_disclosure | pages [26] -->
m

<!-- b009365 | ai_disclosure | pages [26] -->
m

<!-- b009366 | ai_disclosure | pages [26] -->
m

<!-- b009367 | ai_disclosure | pages [26] -->
m

<!-- b009368 | ai_disclosure | pages [26] -->
m

<!-- b009369 | ai_disclosure | pages [26] -->
m

<!-- b009370 | ai_disclosure | pages [26] -->
input and output variables. They support multiple input variables and benefit from

<!-- b009371 | ai_disclosure | pages [26] -->
m

<!-- b009372 | ai_disclosure | pages [26] -->
m

<!-- b009373 | ai_disclosure | pages [26] -->
m

<!-- b009374 | ai_disclosure | pages [26] -->
m

<!-- b009375 | ai_disclosure | pages [26] -->
m

<!-- b009376 | ai_disclosure | pages [26] -->
m

<!-- b009377 | ai_disclosure | pages [26] -->
m

<!-- b009378 | ai_disclosure | pages [26] -->
m

<!-- b009379 | ai_disclosure | pages [26] -->
m

<!-- b009380 | ai_disclosure | pages [26] -->
m

<!-- b009381 | ai_disclosure | pages [26] -->
m

<!-- b009382 | ai_disclosure | pages [26] -->
m

<!-- b009383 | ai_disclosure | pages [26] -->
m

<!-- b009384 | ai_disclosure | pages [26] -->
m

<!-- b009385 | ai_disclosure | pages [26] -->
m

<!-- b009386 | ai_disclosure | pages [26] -->
m

<!-- b009387 | ai_disclosure | pages [26] -->
m

<!-- b009388 | ai_disclosure | pages [26] -->
m

<!-- b009389 | ai_disclosure | pages [26] -->
m

<!-- b009390 | ai_disclosure | pages [26] -->
m

<!-- b009391 | ai_disclosure | pages [26] -->
m

<!-- b009392 | ai_disclosure | pages [26] -->
m

<!-- b009393 | ai_disclosure | pages [26] -->
m

<!-- b009394 | ai_disclosure | pages [26] -->
m

<!-- b009395 | ai_disclosure | pages [26] -->
m

<!-- b009396 | ai_disclosure | pages [26] -->
m

<!-- b009397 | ai_disclosure | pages [26] -->
m

<!-- b009398 | ai_disclosure | pages [26] -->
m

<!-- b009399 | ai_disclosure | pages [26] -->
m

<!-- b009400 | ai_disclosure | pages [26] -->
m

<!-- b009401 | ai_disclosure | pages [26] -->
m

<!-- b009402 | ai_disclosure | pages [26] -->
m

<!-- b009403 | ai_disclosure | pages [26] -->
m

<!-- b009404 | ai_disclosure | pages [26] -->
m

<!-- b009405 | ai_disclosure | pages [26] -->
m

<!-- b009406 | ai_disclosure | pages [26] -->
m

<!-- b009407 | ai_disclosure | pages [26] -->
m

<!-- b009408 | ai_disclosure | pages [26] -->
m

<!-- b009409 | ai_disclosure | pages [26] -->
m

<!-- b009410 | ai_disclosure | pages [26] -->
m

<!-- b009411 | ai_disclosure | pages [26] -->
m

<!-- b009412 | ai_disclosure | pages [26] -->
m

<!-- b009413 | ai_disclosure | pages [26] -->
m

<!-- b009414 | ai_disclosure | pages [26] -->
m

<!-- b009415 | ai_disclosure | pages [26] -->
m

<!-- b009416 | ai_disclosure | pages [26] -->
m

<!-- b009417 | ai_disclosure | pages [26] -->
m

<!-- b009418 | ai_disclosure | pages [26] -->
m

<!-- b009419 | ai_disclosure | pages [26] -->
m

<!-- b009420 | ai_disclosure | pages [26] -->
m

<!-- b009421 | ai_disclosure | pages [26] -->
m

<!-- b009422 | ai_disclosure | pages [26] -->
m

<!-- b009423 | ai_disclosure | pages [26] -->
m

<!-- b009424 | ai_disclosure | pages [26] -->
m

<!-- b009425 | ai_disclosure | pages [26] -->
m

<!-- b009426 | ai_disclosure | pages [26] -->
m

<!-- b009427 | ai_disclosure | pages [26] -->
m

<!-- b009428 | ai_disclosure | pages [26] -->
m

<!-- b009429 | ai_disclosure | pages [26] -->
m

<!-- b009430 | ai_disclosure | pages [26] -->
m

<!-- b009431 | ai_disclosure | pages [26] -->
m

<!-- b009432 | ai_disclosure | pages [26] -->
m

<!-- b009433 | ai_disclosure | pages [26] -->
m

<!-- b009434 | ai_disclosure | pages [26] -->
m

<!-- b009435 | ai_disclosure | pages [26] -->
m

<!-- b009436 | ai_disclosure | pages [26] -->
m

<!-- b009437 | ai_disclosure | pages [26] -->
m

<!-- b009438 | ai_disclosure | pages [26] -->
m

<!-- b009439 | ai_disclosure | pages [26] -->
m

<!-- b009440 | ai_disclosure | pages [26] -->
m

<!-- b009441 | ai_disclosure | pages [26] -->
m

<!-- b009442 | ai_disclosure | pages [26] -->
m

<!-- b009443 | ai_disclosure | pages [26] -->
m

<!-- b009444 | ai_disclosure | pages [26] -->
m

<!-- b009445 | ai_disclosure | pages [26] -->
m

<!-- b009446 | ai_disclosure | pages [26] -->
m

<!-- b009447 | ai_disclosure | pages [26] -->
m

<!-- b009448 | ai_disclosure | pages [26] -->
m

<!-- b009449 | ai_disclosure | pages [26] -->
m

<!-- b009450 | ai_disclosure | pages [26] -->
m

<!-- b009451 | ai_disclosure | pages [26] -->
m

<!-- b009452 | ai_disclosure | pages [26] -->
m

<!-- b009453 | ai_disclosure | pages [26] -->
m

<!-- b009454 | ai_disclosure | pages [26] -->
m

<!-- b009455 | ai_disclosure | pages [26] -->
m

<!-- b009456 | ai_disclosure | pages [26] -->
m

<!-- b009457 | ai_disclosure | pages [26] -->
m

<!-- b009458 | ai_disclosure | pages [26] -->
m

<!-- b009459 | ai_disclosure | pages [26] -->
m

<!-- b009460 | ai_disclosure | pages [26] -->
m

<!-- b009461 | ai_disclosure | pages [26] -->
m

<!-- b009462 | ai_disclosure | pages [26] -->
m

<!-- b009463 | ai_disclosure | pages [26] -->
m

<!-- b009464 | ai_disclosure | pages [26] -->
m

<!-- b009465 | ai_disclosure | pages [26] -->
m

<!-- b009466 | ai_disclosure | pages [26] -->
m

<!-- b009467 | ai_disclosure | pages [26] -->
m

<!-- b009468 | ai_disclosure | pages [26] -->
m

<!-- b009469 | ai_disclosure | pages [26] -->
m

<!-- b009470 | ai_disclosure | pages [26] -->
m

<!-- b009471 | ai_disclosure | pages [26] -->
m

<!-- b009472 | ai_disclosure | pages [26] -->
m

<!-- b009473 | ai_disclosure | pages [26] -->
m

<!-- b009474 | ai_disclosure | pages [26] -->
m

<!-- b009475 | ai_disclosure | pages [26] -->
m

<!-- b009476 | ai_disclosure | pages [26] -->
m

<!-- b009477 | ai_disclosure | pages [26] -->
m

<!-- b009478 | ai_disclosure | pages [26] -->
m

<!-- b009479 | ai_disclosure | pages [26] -->
m

<!-- b009480 | ai_disclosure | pages [26] -->
m

<!-- b009481 | ai_disclosure | pages [26] -->
m

<!-- b009482 | ai_disclosure | pages [26] -->
m

<!-- b009483 | ai_disclosure | pages [26] -->
m

<!-- b009484 | ai_disclosure | pages [26] -->
m

<!-- b009485 | ai_disclosure | pages [26] -->
m

<!-- b009486 | ai_disclosure | pages [26] -->
m

<!-- b009487 | ai_disclosure | pages [26] -->
m

<!-- b009488 | ai_disclosure | pages [26] -->
m

<!-- b009489 | ai_disclosure | pages [26] -->
m

<!-- b009490 | ai_disclosure | pages [26] -->
m

<!-- b009491 | ai_disclosure | pages [26] -->
m

<!-- b009492 | ai_disclosure | pages [26] -->
m

<!-- b009493 | ai_disclosure | pages [26] -->
m

<!-- b009494 | ai_disclosure | pages [26] -->
m

<!-- b009495 | ai_disclosure | pages [26] -->
m

<!-- b009496 | ai_disclosure | pages [26] -->
m

<!-- b009497 | ai_disclosure | pages [26] -->
m

<!-- b009498 | ai_disclosure | pages [26] -->
m

<!-- b009499 | ai_disclosure | pages [26] -->
m

<!-- b009500 | ai_disclosure | pages [26] -->
m

<!-- b009501 | ai_disclosure | pages [26] -->
m

<!-- b009502 | ai_disclosure | pages [26] -->
m

<!-- b009503 | ai_disclosure | pages [26] -->
m

<!-- b009504 | ai_disclosure | pages [26] -->
m

<!-- b009505 | ai_disclosure | pages [26] -->
m

<!-- b009506 | ai_disclosure | pages [26] -->
m

<!-- b009507 | ai_disclosure | pages [26] -->
m

<!-- b009508 | ai_disclosure | pages [26] -->
m

<!-- b009509 | ai_disclosure | pages [26] -->
m

<!-- b009510 | ai_disclosure | pages [26] -->
m

<!-- b009511 | ai_disclosure | pages [26] -->
m

<!-- b009512 | ai_disclosure | pages [26] -->
m

<!-- b009513 | ai_disclosure | pages [26] -->
m

<!-- b009514 | ai_disclosure | pages [26] -->
m

<!-- b009515 | ai_disclosure | pages [26] -->
m

<!-- b009516 | ai_disclosure | pages [26] -->
m

<!-- b009517 | ai_disclosure | pages [26] -->
preprocessing techniques like normalization to improve performance. However,

<!-- b009518 | ai_disclosure | pages [26] -->
m

<!-- b009519 | ai_disclosure | pages [26] -->
m

<!-- b009520 | ai_disclosure | pages [26] -->
m

<!-- b009521 | ai_disclosure | pages [26] -->
m

<!-- b009522 | ai_disclosure | pages [26] -->
m

<!-- b009523 | ai_disclosure | pages [26] -->
m

<!-- b009524 | ai_disclosure | pages [26] -->
m

<!-- b009525 | ai_disclosure | pages [26] -->
m

<!-- b009526 | ai_disclosure | pages [26] -->
m

<!-- b009527 | ai_disclosure | pages [26] -->
m

<!-- b009528 | ai_disclosure | pages [26] -->
m

<!-- b009529 | ai_disclosure | pages [26] -->
m

<!-- b009530 | ai_disclosure | pages [26] -->
m

<!-- b009531 | ai_disclosure | pages [26] -->
m

<!-- b009532 | ai_disclosure | pages [26] -->
m

<!-- b009533 | ai_disclosure | pages [26] -->
m

<!-- b009534 | ai_disclosure | pages [26] -->
m

<!-- b009535 | ai_disclosure | pages [26] -->
m

<!-- b009536 | ai_disclosure | pages [26] -->
m

<!-- b009537 | ai_disclosure | pages [26] -->
m

<!-- b009538 | ai_disclosure | pages [26] -->
m

<!-- b009539 | ai_disclosure | pages [26] -->
m

<!-- b009540 | ai_disclosure | pages [26] -->
m

<!-- b009541 | ai_disclosure | pages [26] -->
m

<!-- b009542 | ai_disclosure | pages [26] -->
m

<!-- b009543 | ai_disclosure | pages [26] -->
while MLR is a statistical model that assumes linear relationships and offers inter-

<!-- b009544 | ai_disclosure | pages [26] -->
pretability through coefficients, FNN is a computational model capable of learning

<!-- b009545 | ai_disclosure | pages [26] -->
non-linear and complex patterns, often regarded as a ”black box.” MLR is simpler,

<!-- b009546 | ai_disclosure | pages [26] -->
requiring fewer data points and involving direct analytical solutions, whereas FNN is

<!-- b009547 | ai_disclosure | pages [26] -->
more flexible but computationally intensive, relying on iterative optimization meth-

<!-- b009548 | ai_disclosure | pages [26] -->
ods like backpropagation.>

<!-- b009549 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b009550 | furniture | pages [26] -->
2

<!-- b009551 | furniture | pages [26] -->
MATHmodels

<!-- b009552 | furniture | pages [26] -->
获取更多资讯
