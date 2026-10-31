# P-C-2025-2514461-4da6b888

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
2514461

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Sketch an Olympic Vision

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
The Olympic Games is no doubt the most grand and prevalent sporting event on this planet. The medal counts represent the countries’ dedication and development in sports and physical wellbeing. Specifically, outstanding coaches have led many teams to great success. However, their presence are typically hidden behind the numbers.

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
In this essay, we mainly discussed the methods of utilizing limited data, predicting the countries’ performance in 2028, honoring the coaches and predicting future numbers based on the effect of potential great coaches.

<!-- b000013 | prose | pages [1] -->
In model I, we predicted the number of events in every discipline at the 2028 Games. We first preprocessed the data, grouping the players by their teams and countries. We chose to analyze the data on disciplines, summing up their events since events in the same discipline are similar and tend to develop simultaneously, also avoiding overgeneralizing to the level of sports. We employed Support Vector Regression (SVR) instead of Linear Regression, which cannot interpret the complex structure of the data. SVR captured the nonlinear patterns in the data, with MSE equals 1.744 and R-squared 0.634, doing nicely for recent years. We also analyzed the importance of different sports for different countries using weighted sums of medals, and visualized it using rose plots.

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
In Model II, based on the event number predictions in Model I, we predicted the medal numbers in 2028. We first attempted at a plain Long Short Term Memory (LSTM) model. We employed the technique of the Adam optimizer and plateau-detection schedulers. We also added punishment terms, forcing the model to predict equal numbers for all medal types. However, results showed clear underfitting and overfitting. Therefore, we turned to an advanced XGBoost model. In this model, we predicted fractions instead of numbers, and multiplied the fractions with results in model I to yield final medal counts. Noting that 90% of host countries witnessed significant improvement, we averaged the increase as 15%, multiplied to the 2028 host USA, and normalized the results. USA topped the board with 47 golds, 45 silvers and 36 bronzes, China followed with 35, 24, 15, and then Japan with 18, 9 and 10. We evaluated the soundness of this model on year 2024. The 95% confidence intervals were calculated for 9 typical countries, and all predicted results lied in the intervals, proving high reliability.

<!-- b000016 | prose | pages [1] -->
In Model III, we addressed the cases where a country that had never earned an Olympic medal earned its first at 2028. We employed the Cox Proportional Hazard Model, with its risk function representing the possibility that a country switched from the no-medal status to first-medal status. By fitting the model, normalizing the results, and Monte-Carlo simulations, we predicted the potential number of first-time medalists by 2028. 3 is the most likely with probability 22.73%, and the three most likely first-time medalists are Monaco, Liechtenstein and Myanmar.

<!-- b000017 | prose | pages [1] -->
In Model IV, we addressed the Great Coach Effect (GCE). We developed a Threshold Method, filtering first- order difference and first-order ratio of score, where scores are calculated by a weighted sum of medal counts. An ensemble-learning anomaly detection method, Isolation Forest, was also employed to cross-validate the choice of weights. We ended up choosing 3, 2 and 1. There was a 89% correspondence between the two methods. We selected the thresholds accordingly. Detection was an OR-logic with the two thresholds. Summing up all years and teams, we measured GCE influence on every sport. We chose USA, CHN and TPE for analysis, and identified the most GCE-influenced sports that they play. We yielded that Taekwondo for USA, Archery for CHN and Swimming for TPE, are their most coach-needing sports. We then used our own ensemble learning by averaging the prediction results of Linear Regression and Random Forest. The data for fitting are all the threshold-activated points for the sport. We predicted that CHN Archery would go from 2 in 2024 to 7 in 2028, USA Taekwondo from 5 to 8, and TPE Swimming from 0 to 9, after hiring great coaches.

<!-- b000018 | prose | pages [1] -->
Finally, we looked into the male-female score ratio to provide insights on gender-equality since data showed that the stronger countries are more gender-balanced. We visualized our results, showing the predicted medals, the fitted lines, random forests and coach effects. Meanwhile, strengths and weaknesses of the models were analyzed, insights were visualized and discussed, and sensitivity analysis was done.

<!-- b000019 | keywords | pages [1] -->
Keywords: Threshold Method, SVR, XGBoost, LSTM, Mann-Kendall, Cox, Isolation Forest, Linear Regression,

<!-- b000020 | prose | pages [1] -->
Random Forest

<!-- b000021 | heading | pages [2] -->
Contents

<!-- b000022 | heading | pages [2] -->
Introduction

<!-- b000023 | prose | pages [2] -->
3 1

<!-- b000024 | heading | pages [2] -->
Background

<!-- b000025 | prose | pages [2] -->
3 1.1 Literature Review 3 1.2 1.3

<!-- b000026 | heading | pages [2] -->
Problem Restatement

<!-- b000027 | prose | pages [2] -->
3 1.4 4 Our Work 5

<!-- b000028 | heading | pages [2] -->
Assumptions and Justification

<!-- b000029 | prose | pages [2] -->
2

<!-- b000030 | heading | pages [2] -->
Notations

<!-- b000031 | prose | pages [2] -->
5 3

<!-- b000032 | prose | pages [2] -->
6 Model I : Event Prediction based on SVR 4 6 Model Overview . 4.1

<!-- b000033 | heading | pages [2] -->
Model Establishment

<!-- b000034 | prose | pages [2] -->
4.2 6 Results . 7 4.3 Analysis of the importance of different sports 8 4.4

<!-- b000035 | heading | pages [2] -->
Model II : Medal Prediction based on LSTM and XGBoost

<!-- b000036 | prose | pages [2] -->
9 5 Model Overview . 9 5.1 Data Preparation . 9 5.2 10 5.3 Baseline: LSTM model 10 5.3.1 Model Overview 5.3.2 Training Process 10 5.3.3

<!-- b000037 | heading | pages [2] -->
Results

<!-- b000038 | prose | pages [2] -->
10 5.4 11 Advanced: XGBoost model

<!-- b000039 | heading | pages [2] -->
5.4.1 Model Establishment

<!-- b000040 | prose | pages [2] -->
11 12 5.5 Examining the confidence of the prediction interval A Mann-Kendall-based analysis to project significant change in medal acquisi- 5.6 tion 13

<!-- b000041 | heading | pages [2] -->
Model III: First-time Medalist Prediction based on Cox Proportional Hazard

<!-- b000042 | prose | pages [2] -->
6 15

<!-- b000043 | heading | pages [2] -->
Model

<!-- b000044 | heading | pages [2] -->
6.1 Model Overview

<!-- b000045 | prose | pages [2] -->
15

<!-- b000046 | heading | pages [2] -->
6.2 Theoretical Basis

<!-- b000047 | prose | pages [2] -->
15 Key Predictors of First-time Medalists 16 6.3

<!-- b000048 | heading | pages [2] -->
Model establishment

<!-- b000049 | prose | pages [2] -->
16 6.4

<!-- b000050 | heading | pages [2] -->
Model Fitting and Prediction

<!-- b000051 | prose | pages [2] -->
6.5 16 Monte Carlo Simulation 6.6 17 0 17 Model IV: Great Coach Effect 7 Model Overview.. 17 7.1 18 7.2 Effect Evidence Threshold Method 7.2.1 18

<!-- b000052 | heading | pages [2] -->
7.2.2 Isolation Forest

<!-- b000053 | prose | pages [2] -->
19 7.3 GCE contribution to medal counts 19 GCE influence on certain sports 19 7.4 Application and Estimation 20 7.5 7.5.1 20 choosing countries and sports 7.5.2 Great Coach Effect Prediction 20

<!-- b000054 | heading | pages [2] -->
Results

<!-- b000055 | prose | pages [2] -->
7.5.3 21

<!-- b000056 | prose | pages [2] -->
关注数学模型

<!-- b000057 | furniture | pages [2] -->
1

<!-- b000058 | furniture | pages [2] -->
获取更多资讯

<!-- b000059 | heading | pages [3] -->
8 Insights

<!-- b000060 | prose | pages [3] -->
22 8.1 From Models Above . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 8.2 Extra Study: Impact of Gender Ratio . . . . . . . . . . . . . . . . . . . . . . . 23

<!-- b000061 | heading | pages [3] -->
9 Sensitivity Analysis

<!-- b000062 | prose | pages [3] -->
23

<!-- b000063 | heading | pages [3] -->
10 Strength and Weakness

<!-- b000064 | prose | pages [3] -->
24 10.1 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 微信公众号：数学模型 10.2 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 10.3 Room for Improvement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

<!-- b000065 | heading | pages [3] -->
Reference

<!-- b000066 | references | pages [3] -->
25

<!-- b000067 | heading | pages [3] -->
Appendices

<!-- b000068 | prose | pages [3] -->
1

<!-- b000069 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000070 | prose | pages [3] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000071 | furniture | pages [3] -->
m

<!-- b000072 | furniture | pages [3] -->
m

<!-- b000073 | furniture | pages [3] -->
m

<!-- b000074 | furniture | pages [3] -->
m

<!-- b000075 | furniture | pages [3] -->
m

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

<!-- b000395 | furniture | pages [4] -->
Team # 2514461

<!-- b000396 | furniture | pages [4] -->
Page 3 of 25

<!-- b000397 | heading | pages [4] -->
1 Introduction

<!-- b000398 | heading | pages [4] -->
1.1 Background

<!-- b000399 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Following the conclusion of the 2024 Paris Olympics, nations are turning to the 2028 Los m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Angeles Games. As a globally celebrated sporting event, the Olympics serves as not only a m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m world stage for athletes to showcase their exceptional sportsmanship, but also a platform for m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m cultural exchange and fostering friendship among nations. Consequently, accurately forecasting m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000400 | prose | pages [4] -->
a nation’s medal count at the Olympics is of paramount importance to sports governing bodies and athletes alike.

<!-- b000401 | prose | pages [4] -->
Historically, Olympicmedalprojectionshavelargelyreliedonthefinalathleteroster.However, with globalization and the evolution of sports, numerous unforeseen factors, such as the emer- gence of a great coach or new talent, regional sports culture and home-field advantage can significantly impact medal tallies. Despite these challenges, early predictions are crucial for informed strategic planning and resource allocation within the sporting landscape.

<!-- b000402 | heading | pages [4] -->
1.2 Literature Review

<!-- b000403 | prose | pages [4] -->
The Olympic Games is an international sporting event, the medal tally of which has always been a focal point of attention and analysis. There now exists an extensive body of research pertaining to medal and result projection. For example, Zhang Bo predicted the gold-medal result of women’s shot put in 2012 based on GM(1,1) prediction model in Gray System Theory, a more applicable solution when there is lack of data [1]. More methods on the basis of machine learning algorithms were provided by Jhankar Moolchandani et al. [2] including Linear Regression, Random Forest, Support Vector Machines and Neural Networks. They are more useful for forecasting the medal count according to the athlete’s attributes and country information. Among them, Random Forest and SVM stood out. Noviyanti T M Sagala and Muhammad Amien Ibrahim compared XGBoost, LightGBM and CatBoost and found that XGBoost had the highest accuracy [3]. Since Python has numerous libraries that facilitate machine learning tasks, it is convenient for predicting events and medals. XGBoost, which outperforms Random Forest through iterative optimization of trees, can be a reliable choice for our medal ranking prediction.

<!-- b000404 | prose | pages [4] -->
For the prediction of first medal wins, work by Nisreen Osman Abdelsalam et al. on applying Cox proportional hazards models to time-to-event data provided profound inspiration. Similar to survival time, there are numerous factors contributing to the duration of a country going without winning a medal, which can be analyzed by multivariable Cox regression [4].

<!-- b000405 | prose | pages [4] -->
For the problem of Great Coach Effect, we conceptualize differential points to detect the occurrence of the effect. This can be understood through Anomaly Detection. There exist many calculation methods to do so when handling time series data [5]. Yu Qin and YuanSheng Lou used Isolation Forest algorithm to detect the anomaly points of the hydrological time series data, which is more efficient and stable method than traditional ones [6].

<!-- b000406 | heading | pages [4] -->
1.3 Problem Restatement

<!-- b000407 | heading | pages [4] -->
1. Data Preparation

<!-- b000408 | prose | pages [4] -->
Preprocessing the 5 datasets about all the history Olympic Games based on appropriate assumptions and decisions for different predictions.

<!-- b000409 | heading | pages [4] -->
2. Model Construction

<!-- b000410 | prose | pages [4, 5] -->
关注数学模型 Building prediction models for medal counts for each country, including prediction of event count and types and first-time medalists.

<!-- b000411 | furniture | pages [4] -->
2

<!-- b000412 | furniture | pages [4] -->
MATHmodels

<!-- b000413 | furniture | pages [4] -->
获取更多资讯

<!-- b000414 | furniture | pages [5] -->
Page 4 of 25

<!-- b000415 | furniture | pages [5] -->
Team # 2514461

<!-- b000417 | prose | pages [5] -->
Also, establishing a model to evaluate Great Coach Effect. Using this quantifier to build another model predicting the results of introducing a coach.

<!-- b000418 | prose | pages [5] -->
3. Model Application Applying our models to the history data and making projections for the event count and medal table in the Los Angeles, USA 2028 Olympics. Analyzing countries that will do better or worse and the prevailing sports for different countries, which leads to different possible results due to the varying of the events chosen by the home country and their numbers. Determining how many countries are likely to pick up their first Olympic medal in 2028.

<!-- b000419 | prose | pages [5] -->
For Great Coach Effect, choosing three countries and applying our model to find sports where coaching investment pays off. Predicting their performance improvement brought by a coach.

<!-- b000420 | prose | pages [5] -->
Offering innovative insights found in our model to country Olympic committees.

<!-- b000421 | prose | pages [5] -->
4. Model testing and sensitivity analysis Evaluating the precision and reliability of our models with prediction intervals, probabil- ities, errors, etc. Performing the sensitivity analysis.

<!-- b000422 | prose | pages [5] -->
● ● 1.4 Our Work

<!-- b000423 | heading | pages [5] -->
1. For data preparation, we set some basic assumptions to mathematize the real-life problem

<!-- b000424 | prose | pages [5] -->
and conducted data curation, including cleaning, filtering, and establishing relationships between events, disciplines, and sports in different ways for further usage.

<!-- b000425 | heading | pages [5] -->
2. For model construction, we

<!-- b000426 | prose | pages [5] -->
(a) built a SVR model to predict event count, projected medal count from LSTM baseline model to XGBoost model, and established Mann-Kendall-based method for performance change prediction.

<!-- b000427 | prose | pages [5] -->
(b) constructed a Cox proportion hazard model for first-time medalists prediction.

<!-- b000428 | prose | pages [5] -->
(c) quantified medal score system and Contribution Factor and Influence Factor of coach effect, identified threshold method and Isolation Forest method to capture the evidence of Great Coach Effect and used both Linear Regression and Random Forest to estimate the ● impact on specific sports.

<!-- b000429 | heading | pages [5] -->
3. For model application, we applied our models to predict the event count, medal count,

<!-- b000430 | prose | pages [5] -->
number of first-medalists, and the probable outcomes of the three countries we chose to introduce a coach in 2028 Olympic Games. We found some insights offering practical reference based on our model and gender ratio analysis.

<!-- b000431 | heading | pages [5] -->
4. For model testing and sensitivity analysis, we assessed the precision of our models by

<!-- b000432 | prose | pages [5] -->
mean squared error, R-squared value and prediction intervals. Sensitivity analysis on threshold of coach effect exhibited robustness.

<!-- b000433 | prose | pages [5] -->
5. For further discussion and evaluation, we discussed the strengths and weaknesses of our models and found room for improvement.

<!-- b000434 | furniture | pages [6] -->
Team # 2514461

<!-- b000435 | furniture | pages [6] -->
Page 5 of 25

<!-- b000436 | heading | pages [6] -->
2 Assumptions and Justification

<!-- b000437 | prose | pages [6] -->
• A country’s medal count is only determined by the trend of its performance in past Olympic Games.

<!-- b000438 | prose | pages [6] -->
Abrupt changes caused by external factors such as sudden events are not taken into account.

<!-- b000439 | prose | pages [6] -->
• We attribute all performance improvements exceeding a specific threshold to the coaches.

<!-- b000440 | prose | pages [6] -->
For a country’s Olympic team, improvements within a certain range are attributed to individual athlete performance, while those exceeding this threshold are attributed to additional efforts, specifically the introductions of coaches.

<!-- b000441 | prose | pages [6] -->
• The probabilities of countries that have yet to earn a medal becoming a first-time medalist in a given year are mutually independent.

<!-- b000442 | prose | pages [6] -->
Each country’s performance is influenced by a unique set of factors like athletes and training. Additionally, the outcome of one particular country has little to no bearing on the outcome of another particular country given the multitude of countries participating.

<!-- b000443 | prose | pages [6] -->
• The differences between great coaches from various countries can be neglected.

<!-- b000444 | prose | pages [6] -->
When a coach who moves internationally is considered great, his ability is independent to his nationality.

<!-- b000445 | prose | pages [6] -->
• The impact pattern of a coach on a specific sport is consistent across different nations.

<!-- b000446 | prose | pages [6] -->
The enhancement of athletic performance due to the introduction of a coach is solely historical, meaning that as long as athletes from different countries have the same baseline, the improvement results will be identical.

<!-- b000447 | heading | pages [6] -->
3 Notations

<!-- b000448 | heading | pages [6] -->
Symbol

<!-- b000449 | prose | pages [6] -->
Definition N′ predicted number of events E N′ predicted total number of medals M R′ predicted ratio of gold medals G R′ predicted ratio of silver medals S R′ predicted ratio of bronze medals B P probability of winning the first medal Xa number of athletes Xp number of participations Xe number of events NG number of gold medals NS number of silver medals NB number of bronze medals m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000450 | heading | pages [6] -->
Symbol

<!-- b000451 | prose | pages [6] -->
Definition m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ωG m m m m m m m m m m m m m m weight of gold medal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ωS weight of silver medal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ωB weight of bronze medal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m S score △S first-order difference of score γS first-order ratio of score threshold of △S ST△ STγ threshold of γS Contribution Factor at the ith Games Ci Is Influence Factor of sport s score at the ith Games Si score of sport j at the ith Games. Sij

<!-- b000452 | prose | pages [6] -->
关注数学模型

<!-- b000453 | furniture | pages [6] -->
2

<!-- b000454 | furniture | pages [6] -->
MATHmodels

<!-- b000455 | furniture | pages [6] -->
获取更多资讯

<!-- b000456 | furniture | pages [7] -->
Page 6 of 25

<!-- b000457 | furniture | pages [7] -->
Team # 2514461

<!-- b000458 | heading | pages [7] -->
Model I : Event Prediction based on SVR

<!-- b000459 | prose | pages [7] -->
4

<!-- b000460 | prose | pages [7] -->
As a preliminary step in predicting the overall medal count at the 2028 USA Olympic Games, we first forecast the number of events using the Support Vector Machine , utilizing its ability of handling complex and nonlinear data.

<!-- b000461 | prose | pages [7] -->
4.1 Model Overview

<!-- b000462 | prose | pages [7] -->
In this model, we employed Support Vector Regression to predict the number of events in various disciplines at the 2028 Olympic Games based on history event counts. Given the nonlinearity of the time series data, SVR was selected due to its ability to effectively capture nonlinear patterns. By training and tuning the model on the dataset, we successfully forecast the event count for each discipline in 2028. Evaluation results proved outstanding performance, especially for disciplines with relatively stable event counts in recent years. We also calculated medal weighted score S to measure the significance of different sports to each country.

<!-- b000463 | prose | pages [7] -->
● ●

<!-- b000464 | heading | pages [7] -->
4.2 Model Establishment

<!-- b000465 | prose | pages [7] -->
Given the varying event number in each Games shown in the provided dataset, regression methods can be employed to forecast the number of events in the 2028 Games. While ARIMA models are commonly used for time series forecasting since they're suitable for linear data, Support Vector Regression (SVR) model offers a more robust approach with its ability to capture nonlinear patterns. [7]

<!-- b000466 | heading | pages [7] -->
Support Vector Regression (SVR), an extension of Support Vector Machines (SVM) for

<!-- b000467 | prose | pages [7] -->
regression problems, aims to find a function that minimizes the prediction error on the target variable while satisfying certain constraints. The optimization problem for constructing the model is:

<!-- b000468 | prose | pages [7] -->
n min −∥ω|2 + C ∑(ξi + ξ i) (1) w,b,ξ,ξ* 2" i=1 ● subject to:

<!-- b000469 | prose | pages [7] -->
yi − (w, xi〉 − b ≤ ∈ + ξi (2) (w, xi> + b − yi ≤ ∈ + ξi (3) ?A 0  32 (4)

<!-- b000470 | prose | pages [7] -->
By solving the optimization problem outlined above, the optimal weight vector w and bias b are determined. For non-linear SVR, a kernel function is employed to map the input data into a higher-dimensional feature space, thereby allowing for a linear regression model to be fitted. This can be expressed as:

<!-- b000471 | prose | pages [7] -->
n f(x) = ∑(αi − αi)K (xi, x) + b (5) i=1

<!-- b000472 | prose | pages [7] -->
Due to the obvious nonlinear characteristics of the prediction, we adopt a Gaussian kernel, expressed as:

<!-- b000473 | prose | pages [7] -->
K(xi, xj) = exp(−γ||xi − xj|2) (6)

<!-- b000474 | prose | pages [7] -->
Subsequent parameter tuning and model training enable the prediction of the event count for the 2028 Olympics.

<!-- b000475 | furniture | pages [8] -->
Team # 2514461

<!-- b000476 | furniture | pages [8] -->
Page 7 of 25

<!-- b000477 | prose | pages [8] -->
We conductedregressionanalysisonthenumberofpasteventsinsummerOly_programs.csv to predict the event count in certain discipline for the 2028 Olympics. The modeling steps are shown in Fig. 1. For each discipline, a time series of event counts was constructed, saved as a two-dimensional array. This series was divided into training and testing sets in an 8:2 ratio and subsequently standardized. An SVR model wass instantiated and its hyperparameters tuned via Grid Search coupled with 5-fold Cross-Validation. The trained model was then employed to predict future event counts.

<!-- b000478 | heading | pages [8] -->
4.3 Results

<!-- b000479 | prose | pages [8] -->
Taking artistic gymnastics as an example, the SVR model predicted 14 events in 2028, with a mean squared error(MSE) of 1.744 and an R-squared value of 0.634 as shown in Fig. 2. This relatively high error is due to significant fluctuations in the number of events for this discipline in early years. Despite this, this SVR model performs well when predicting disciplines with a more stable number of events in recent years.

<!-- b000480 | prose | pages [8] -->
Ultimately, We can roll up the results to determine the overall event count for each sport. They are shown in table 1.

<!-- b000481 | caption | pages [8] -->
Figure 2: Event count prediction of artistic gymnastics

<!-- b000482 | caption | pages [8] -->
Figure 1:

<!-- b000483 | prose | pages [8] -->
Flow chart of event count prediction

<!-- b000484 | prose | pages [8, 9] -->
关注数学模型 Sport Discipline Code Discipline Event Sport Event Sport Discipline Code Discipline Event Sport Event Artistic Swimming SWA 2 Indoor HBL 2 Handball 2 Diving DIV 8 Field HBL 0 Aquatics Marathon Swimming OWS 2 49 Jeu de Paume Jeu de Paume 0 0 Swimming SWM 35 Water Polo WPO 2 Judo Judo JUD 16 16 Archery Archery ARC 5 5 Karate Karate KTE 0 0 Athletics Athletics ATH 48 48 Sixes LAX 0 Lacrosse 0 Field LAX 0 Badminton Badminton BDM 6 6 Modern Pentathlon MPN 2 2 Baseball BSB 1 Baseball and Softball 2 微信公众号：数学模型 Softball SBL 1 Polo Polo POL 0 0 3x3 BK3 1 Basketball 3 Rackets Rackets RQT 0 0 Basketball BKB 2 Roque Roque 0 0 Basque Pelota Basque Pelota PEL 0 0 Coastal ROC 0 Boxing Boxing BOX 13 13 Rowing 14 Rowing ROW 14 Breaking Breaking BKG 0 0 Sevens RU7 1 Rugby 0 Union RUG 0 Sprint CSP 11 Canoeing 16 Slalom CSL 5 Sailing Sailing SAL 10 10 Cricket Cricket CKT 0 0 Shooting Shooting SHO 15 15 Croquet Croquet CQT 0 0 Skateboarding Skateboarding SKB 0 0 BMX Freestyle BMF 1 Sport Climbing Sport Climbing CLB 2 2 BMX Racing BMX 2 Cycling Mountain Bike MTB 2 21 Squash Squash SQU 0 0 Road CRD 4 微信号：MATHmodels Track CTR 12 Surfing Surfing SRF 0 0 Dressage EDR 2 Table Tennis Table Tennis TTE 5 5 Eventing EVE 2 Equestrian 6 Jumping EJP 2 Taekwondo Taekwondo TKW 8 8 Vaulting EVL 0 Tennis Tennis TEN 6 6 Fencing Fencing FEN 11 11 Triathlon Triathlon TRI 3 3 Field hockey Field hockey HOC 2 2 Tug of War Tug of War TOW 0 0 Flag football Flag football AFB 0 0 Beach VBV 2 Volleyball 4 Football Football FBL 2 2 Indoor VVO 2 Golf Golf GLF 1 1 Water Motorsports PBT 0 0 Artistic GAR 14 Weightlifting Weightlifting WLF 16 16 Gymnastics Rhythmic GRY 2 18 Freestyle WRF 12 Trampoline GTR 2 Wrestling 18 Greco-Roman WRG 6

<!-- b000485 | furniture | pages [8] -->
2

<!-- b000486 | furniture | pages [8] -->
MATHmodels

<!-- b000487 | furniture | pages [8] -->
获取更多资讯

<!-- b000488 | furniture | pages [9] -->
Team # 2514461

<!-- b000489 | furniture | pages [9] -->
Page 8 of 25

<!-- b000490 | caption | pages [9] -->
Table 1: Predicted event count in 2028 Olympics

<!-- b000492 | heading | pages [9] -->
4.4 Analysis of the importance of different sports

<!-- b000493 | prose | pages [9] -->
Firstly, we quantified a country’s performance in a specific sport at a certain Games as score S, which is the sum of gold, silver and bronze medal counts NG, NS and NB assigned with different weights ωG, ωS and ωB.

<!-- b000494 | prose | pages [9] -->
S = NGωG + NSωS + NBωB (7)

<!-- b000495 | prose | pages [9] -->
For the sake of simplicity, we let

<!-- b000496 | prose | pages [9] -->
ωG = 3, ωS = 2, ωB = 1. (8)

<!-- b000497 | prose | pages [9, 10] -->
We calculated the proportion of scores in various sports for different countries in 2024 relative to their total scores, to measure the significance of different sports to each country. We Games

<!-- b000498 | furniture | pages [10] -->
Team # 2514461

<!-- b000499 | furniture | pages [10] -->
Page 9 of 25

<!-- b000500 | caption | pages [10] -->
Figure 3: The score percentage of various sports for different countries at the 2024 Olympic

<!-- b000502 | prose | pages [10] -->
assumed that the higher the proportion of a sport in a country, the more important that sport is to that country.

<!-- b000503 | prose | pages [10] -->
From Fig. 3, it can be seen that for the United States, Athletics and Aquatics have the largest proportions and are the most significant; for China, Japan, and the United Kingdom, Aquatics, Wrestling, and Aquatics are the most important, respectively.

<!-- b000504 | heading | pages [10] -->
5 Model II : Medal Prediction based on LSTM and XGBoost

<!-- b000505 | heading | pages [10] -->
5.1 Model Overview

<!-- b000506 | prose | pages [10] -->
To capture the intricate relationship between a country’s medal count and the specific disciplines, we first tallied the gold, silver and bronze medals won by each country in each discipline every year, then divided by the total number of medals awarded in that discipline for that year to obtain the country’s medal winning percentage. We then used the ratios from previous years to train an LSTM model as baseline and conducting a more accurate model based on XGBoost algorithm. The results we predicted were the percentages of medals won by each country out of the total medals awarded in each discipline in 2028. The predicted number of gold, silver, and bronze medals can be calculated by multiplying them by the predicted event numbers and suming up the products. Furthermore, we calculated the 95% confidence intervals for the predicted medal counts by using residuals from the XGBoost model and the properties of the normal distribution. Analysis based on Mann-Kendall test forecast whether a country would do better or worse depending on its performance of the past 5 Games.

<!-- b000507 | heading | pages [10] -->
5.2 Data Preparation

<!-- b000508 | prose | pages [10] -->
A country’s medal count is closely tied to its proficiency in various sports. Accounting for the relationship between events and medals, we proposed predicting the probability of a country m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m winning a medal in each discipline and then multiplying it by the number of events so that we m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000509 | furniture | pages [10] -->
2

<!-- b000510 | prose | pages [10, 11] -->
m m m m m m m m m m m m m m m could provide a more granular and realistic analysis prediction.

<!-- b000511 | furniture | pages [10] -->
m

<!-- b000512 | furniture | pages [10] -->
m

<!-- b000513 | furniture | pages [10] -->
m

<!-- b000514 | furniture | pages [10] -->
m

<!-- b000515 | furniture | pages [10] -->
m

<!-- b000516 | furniture | pages [10] -->
m

<!-- b000517 | furniture | pages [10] -->
m

<!-- b000518 | furniture | pages [10] -->
m

<!-- b000519 | furniture | pages [10] -->
m

<!-- b000520 | furniture | pages [10] -->
m

<!-- b000521 | furniture | pages [10] -->
m

<!-- b000522 | furniture | pages [10] -->
m

<!-- b000523 | furniture | pages [10] -->
m

<!-- b000524 | furniture | pages [10] -->
m

<!-- b000525 | furniture | pages [10] -->
m

<!-- b000526 | furniture | pages [10] -->
m

<!-- b000527 | furniture | pages [10] -->
m

<!-- b000528 | furniture | pages [10] -->
m

<!-- b000529 | furniture | pages [10] -->
m

<!-- b000530 | furniture | pages [10] -->
m

<!-- b000531 | furniture | pages [10] -->
m

<!-- b000532 | furniture | pages [10] -->
m

<!-- b000533 | furniture | pages [10] -->
m

<!-- b000534 | furniture | pages [10] -->
m

<!-- b000535 | furniture | pages [10] -->
m

<!-- b000536 | furniture | pages [10] -->
m

<!-- b000537 | furniture | pages [10] -->
m

<!-- b000538 | furniture | pages [10] -->
m

<!-- b000539 | furniture | pages [10] -->
m

<!-- b000540 | furniture | pages [10] -->
m

<!-- b000541 | furniture | pages [10] -->
m

<!-- b000542 | furniture | pages [10] -->
m

<!-- b000543 | furniture | pages [10] -->
m

<!-- b000544 | furniture | pages [10] -->
m

<!-- b000545 | furniture | pages [10] -->
m

<!-- b000546 | furniture | pages [10] -->
m

<!-- b000547 | furniture | pages [10] -->
m

<!-- b000548 | furniture | pages [10] -->
m

<!-- b000549 | furniture | pages [10] -->
m

<!-- b000550 | furniture | pages [10] -->
m

<!-- b000551 | furniture | pages [10] -->
m

<!-- b000552 | furniture | pages [10] -->
m

<!-- b000553 | furniture | pages [10] -->
m

<!-- b000554 | furniture | pages [10] -->
m

<!-- b000555 | furniture | pages [10] -->
m

<!-- b000556 | furniture | pages [10] -->
m

<!-- b000557 | furniture | pages [10] -->
m

<!-- b000558 | furniture | pages [10] -->
m

<!-- b000559 | furniture | pages [10] -->
m

<!-- b000560 | furniture | pages [10] -->
m

<!-- b000561 | furniture | pages [10] -->
m

<!-- b000562 | furniture | pages [10] -->
m

<!-- b000563 | furniture | pages [10] -->
m

<!-- b000564 | furniture | pages [10] -->
m

<!-- b000565 | furniture | pages [10] -->
m

<!-- b000566 | furniture | pages [10] -->
m

<!-- b000567 | furniture | pages [10] -->
m

<!-- b000568 | furniture | pages [10] -->
m

<!-- b000569 | furniture | pages [10] -->
m

<!-- b000570 | furniture | pages [10] -->
m

<!-- b000571 | furniture | pages [10] -->
m

<!-- b000572 | furniture | pages [10] -->
m

<!-- b000573 | furniture | pages [10] -->
m

<!-- b000574 | furniture | pages [10] -->
m

<!-- b000575 | furniture | pages [10] -->
m

<!-- b000576 | furniture | pages [10] -->
m

<!-- b000577 | furniture | pages [10] -->
m

<!-- b000578 | furniture | pages [10] -->
m

<!-- b000579 | furniture | pages [10] -->
m

<!-- b000580 | furniture | pages [10] -->
m

<!-- b000581 | furniture | pages [10] -->
m

<!-- b000582 | furniture | pages [10] -->
m

<!-- b000583 | furniture | pages [10] -->
m

<!-- b000584 | furniture | pages [10] -->
m

<!-- b000585 | furniture | pages [10] -->
m

<!-- b000586 | furniture | pages [10] -->
m

<!-- b000587 | furniture | pages [10] -->
m

<!-- b000588 | furniture | pages [10] -->
m

<!-- b000589 | furniture | pages [10] -->
m

<!-- b000590 | furniture | pages [10] -->
m

<!-- b000591 | furniture | pages [10] -->
m

<!-- b000592 | furniture | pages [10] -->
m

<!-- b000593 | furniture | pages [10] -->
m

<!-- b000594 | furniture | pages [10] -->
m

<!-- b000595 | furniture | pages [10] -->
m

<!-- b000596 | furniture | pages [10] -->
m

<!-- b000597 | furniture | pages [10] -->
m

<!-- b000598 | furniture | pages [10] -->
m

<!-- b000599 | furniture | pages [10] -->
m

<!-- b000600 | furniture | pages [10] -->
m

<!-- b000601 | furniture | pages [10] -->
m

<!-- b000602 | furniture | pages [10] -->
m

<!-- b000603 | furniture | pages [10] -->
m

<!-- b000604 | furniture | pages [10] -->
m

<!-- b000605 | furniture | pages [10] -->
MATHmodels

<!-- b000606 | furniture | pages [10] -->
m

<!-- b000607 | furniture | pages [10] -->
m

<!-- b000608 | furniture | pages [10] -->
m

<!-- b000609 | furniture | pages [10] -->
m

<!-- b000610 | furniture | pages [10] -->
m

<!-- b000611 | furniture | pages [10] -->
m

<!-- b000612 | furniture | pages [10] -->
m

<!-- b000613 | furniture | pages [10] -->
m

<!-- b000614 | furniture | pages [10] -->
m

<!-- b000615 | furniture | pages [10] -->
m

<!-- b000616 | furniture | pages [10] -->
m

<!-- b000617 | furniture | pages [10] -->
m

<!-- b000618 | furniture | pages [10] -->
m

<!-- b000619 | furniture | pages [10] -->
m

<!-- b000620 | furniture | pages [10] -->
m

<!-- b000621 | furniture | pages [10] -->
m

<!-- b000622 | furniture | pages [10] -->
m

<!-- b000623 | furniture | pages [10] -->
获取更多资讯

<!-- b000624 | furniture | pages [10] -->
m

<!-- b000625 | furniture | pages [10] -->
m

<!-- b000626 | furniture | pages [10] -->
m

<!-- b000627 | furniture | pages [10] -->
m

<!-- b000628 | furniture | pages [10] -->
m

<!-- b000629 | furniture | pages [10] -->
m

<!-- b000630 | furniture | pages [10] -->
m

<!-- b000631 | furniture | pages [10] -->
m

<!-- b000632 | furniture | pages [10] -->
m

<!-- b000633 | furniture | pages [10] -->
m

<!-- b000634 | furniture | pages [10] -->
m

<!-- b000635 | furniture | pages [10] -->
m

<!-- b000636 | furniture | pages [10] -->
m

<!-- b000637 | furniture | pages [10] -->
m

<!-- b000638 | furniture | pages [10] -->
m

<!-- b000639 | furniture | pages [10] -->
m

<!-- b000640 | furniture | pages [10] -->
m

<!-- b000641 | furniture | pages [10] -->
m

<!-- b000642 | furniture | pages [10] -->
m

<!-- b000643 | furniture | pages [10] -->
m

<!-- b000644 | furniture | pages [10] -->
m

<!-- b000645 | furniture | pages [10] -->
m

<!-- b000646 | furniture | pages [10] -->
m

<!-- b000647 | furniture | pages [10] -->
m

<!-- b000648 | furniture | pages [10] -->
m

<!-- b000649 | furniture | pages [10] -->
m

<!-- b000650 | furniture | pages [10] -->
m

<!-- b000651 | furniture | pages [10] -->
m

<!-- b000652 | furniture | pages [10] -->
m

<!-- b000653 | furniture | pages [10] -->
m

<!-- b000654 | furniture | pages [10] -->
m

<!-- b000655 | furniture | pages [10] -->
m

<!-- b000656 | furniture | pages [10] -->
m

<!-- b000657 | furniture | pages [10] -->
m

<!-- b000658 | furniture | pages [10] -->
m

<!-- b000659 | furniture | pages [10] -->
m

<!-- b000660 | furniture | pages [10] -->
m

<!-- b000661 | furniture | pages [10] -->
m

<!-- b000662 | furniture | pages [10] -->
m

<!-- b000663 | furniture | pages [10] -->
m

<!-- b000664 | furniture | pages [10] -->
m

<!-- b000665 | furniture | pages [10] -->
m

<!-- b000666 | furniture | pages [10] -->
m

<!-- b000667 | furniture | pages [10] -->
m

<!-- b000668 | furniture | pages [10] -->
m

<!-- b000669 | furniture | pages [10] -->
m

<!-- b000670 | furniture | pages [10] -->
m

<!-- b000671 | furniture | pages [10] -->
m

<!-- b000672 | furniture | pages [10] -->
m

<!-- b000673 | furniture | pages [10] -->
m

<!-- b000674 | furniture | pages [10] -->
m

<!-- b000675 | furniture | pages [10] -->
m

<!-- b000676 | furniture | pages [10] -->
m

<!-- b000677 | furniture | pages [10] -->
m

<!-- b000678 | furniture | pages [10] -->
m

<!-- b000679 | furniture | pages [10] -->
m

<!-- b000680 | furniture | pages [10] -->
m

<!-- b000681 | furniture | pages [10] -->
m

<!-- b000682 | furniture | pages [10] -->
m

<!-- b000683 | furniture | pages [10] -->
m

<!-- b000684 | furniture | pages [11] -->
Team # 2514461

<!-- b000685 | furniture | pages [11] -->
Page 10 of 25

<!-- b000687 | prose | pages [11] -->
First, wetriedeverymeanstocategorizeeacheventwithindataset summerOly_athletes.csv under its respective discipline. Subsequently, the gold, silver, and bronze medal counts for each country within each discipline were calculated and converted into percentages, representing the likelihood of each country achieving correlative medal success. This approach considered the overall performance within each discipline while also acknowledging the significant differences between disciplines within the same sport (e.g., Swimming and Diving under Aquatics), thus avoiding overgeneralization.

<!-- b000688 | heading | pages [11] -->
5.3 Baseline: LSTM model

<!-- b000689 | heading | pages [11] -->
5.3.1 Model Overview

<!-- b000690 | prose | pages [11] -->
微信公众号：数学模型 In this section, a baseline LSTM model was built and trained using Pytorch. The model took as input all the gold / silver / bronze medal counts of all countries before the 2024 Games, and was fitted to the medal counts in 2024. For the loss function, instead of the typically-used MSE loss, we added a punishment term, punishing deviations of the sum of medal counts of all countries for a certain discipline from the discipline’s known event count. In the predict step, all past years’ data were fed into the model to predict the medal counts for all countries in all disciplines. Summing up the disciplines, we yielded the medal count for all countries.

<!-- b000691 | heading | pages [11] -->
5.3.2 Training Process

<!-- b000692 | prose | pages [11] -->
微信号：MATHmodels The training process used the Adam optimizer with the following parameters: learning rate lrinitial = 0.001, β1 = 0.9, β2 = 0.999, and ϵ = 1 × 10−8. The One Cycle Learning Rate Scheduler was applied with a maximum learning rate max_lr = 0.001 for a total of 100,000 epochs. The learning rate was gradually increased and then decreased in a cyclical manner during training.

<!-- b000693 | heading | pages [11] -->
5.3.3 Results

<!-- b000694 | prose | pages [11] -->
The final loss dropped to 0.0058, indicating good convergence, however, plain LSTM yielded poor results, as indicated in the following two figures. Fig. 4 repeated the medal count in 2024, and is a clear overfit, while Fig. 5 predicts that China will earn 8 Olympic Gold medals in Table Tennis in 2028, while we know that there are only 5, and China can earn at most 5 (as it did in 2024). Therefore, we must take into consideration varying in the number of events held in each discipline, and avoid overfitting. Also, we should consider host effect. All of these will be addressed in our advanced XGBoost Model in the following section.

<!-- b000695 | caption | pages [11] -->
Figure 4: China’s Diving, Overfitting

<!-- b000696 | caption | pages [11] -->
Figure 5: China’s Table Tennis, Underfitting

<!-- b000697 | prose | pages [11] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000698 | furniture | pages [11] -->
m

<!-- b000699 | furniture | pages [11] -->
m

<!-- b000700 | furniture | pages [11] -->
m

<!-- b000701 | furniture | pages [11] -->
m

<!-- b000702 | furniture | pages [11] -->
m

<!-- b000703 | furniture | pages [11] -->
m

<!-- b000704 | furniture | pages [11] -->
m

<!-- b000705 | furniture | pages [11] -->
m

<!-- b000706 | furniture | pages [11] -->
m

<!-- b000707 | furniture | pages [11] -->
m

<!-- b000708 | furniture | pages [11] -->
m

<!-- b000709 | furniture | pages [11] -->
m

<!-- b000710 | furniture | pages [11] -->
m

<!-- b000711 | furniture | pages [11] -->
m

<!-- b000712 | furniture | pages [11] -->
m

<!-- b000713 | furniture | pages [11] -->
m

<!-- b000714 | furniture | pages [11] -->
m

<!-- b000715 | furniture | pages [11] -->
m

<!-- b000716 | furniture | pages [11] -->
m

<!-- b000717 | furniture | pages [11] -->
m

<!-- b000718 | furniture | pages [11] -->
m

<!-- b000719 | furniture | pages [11] -->
m

<!-- b000720 | furniture | pages [11] -->
m

<!-- b000721 | furniture | pages [11] -->
m

<!-- b000722 | furniture | pages [11] -->
m

<!-- b000723 | furniture | pages [11] -->
m

<!-- b000724 | furniture | pages [11] -->
m

<!-- b000725 | furniture | pages [11] -->
m

<!-- b000726 | furniture | pages [11] -->
m

<!-- b000727 | furniture | pages [11] -->
m

<!-- b000728 | furniture | pages [11] -->
m

<!-- b000729 | furniture | pages [11] -->
m

<!-- b000730 | furniture | pages [11] -->
m

<!-- b000731 | furniture | pages [11] -->
m

<!-- b000732 | furniture | pages [11] -->
m

<!-- b000733 | furniture | pages [11] -->
m

<!-- b000734 | furniture | pages [11] -->
m

<!-- b000735 | furniture | pages [11] -->
m

<!-- b000736 | furniture | pages [11] -->
m

<!-- b000737 | furniture | pages [11] -->
m

<!-- b000738 | furniture | pages [11] -->
m

<!-- b000739 | furniture | pages [11] -->
m

<!-- b000740 | furniture | pages [11] -->
m

<!-- b000741 | furniture | pages [11] -->
m

<!-- b000742 | furniture | pages [11] -->
m

<!-- b000743 | furniture | pages [11] -->
m

<!-- b000744 | furniture | pages [11] -->
m

<!-- b000745 | furniture | pages [11] -->
m

<!-- b000746 | furniture | pages [11] -->
m

<!-- b000747 | furniture | pages [11] -->
m

<!-- b000748 | furniture | pages [11] -->
m

<!-- b000749 | furniture | pages [11] -->
m

<!-- b000750 | furniture | pages [11] -->
m

<!-- b000751 | furniture | pages [11] -->
m

<!-- b000752 | furniture | pages [11] -->
m

<!-- b000753 | furniture | pages [11] -->
m

<!-- b000754 | furniture | pages [11] -->
m

<!-- b000755 | furniture | pages [11] -->
m

<!-- b000756 | furniture | pages [11] -->
m

<!-- b000757 | furniture | pages [11] -->
m

<!-- b000758 | furniture | pages [11] -->
m

<!-- b000759 | furniture | pages [11] -->
m

<!-- b000760 | furniture | pages [11] -->
m

<!-- b000761 | furniture | pages [11] -->
m

<!-- b000762 | furniture | pages [11] -->
m

<!-- b000763 | furniture | pages [11] -->
m

<!-- b000764 | furniture | pages [11] -->
m

<!-- b000765 | furniture | pages [11] -->
m

<!-- b000766 | furniture | pages [11] -->
m

<!-- b000767 | furniture | pages [11] -->
m

<!-- b000768 | furniture | pages [11] -->
m

<!-- b000769 | furniture | pages [11] -->
m

<!-- b000770 | furniture | pages [11] -->
m

<!-- b000771 | furniture | pages [11] -->
m

<!-- b000772 | furniture | pages [11] -->
m

<!-- b000773 | furniture | pages [11] -->
m

<!-- b000774 | furniture | pages [11] -->
m

<!-- b000775 | furniture | pages [11] -->
m

<!-- b000776 | furniture | pages [11] -->
m

<!-- b000777 | furniture | pages [11] -->
m

<!-- b000778 | furniture | pages [11] -->
m

<!-- b000779 | furniture | pages [11] -->
m

<!-- b000780 | furniture | pages [11] -->
m

<!-- b000781 | furniture | pages [11] -->
m

<!-- b000782 | furniture | pages [11] -->
m

<!-- b000783 | furniture | pages [11] -->
m

<!-- b000784 | furniture | pages [11] -->
m

<!-- b000785 | furniture | pages [11] -->
m

<!-- b000786 | furniture | pages [11] -->
m

<!-- b000787 | furniture | pages [11] -->
m

<!-- b000788 | furniture | pages [11] -->
m

<!-- b000789 | furniture | pages [11] -->
m

<!-- b000790 | furniture | pages [11] -->
m

<!-- b000791 | furniture | pages [11] -->
m

<!-- b000792 | furniture | pages [11] -->
m

<!-- b000793 | furniture | pages [11] -->
m

<!-- b000794 | furniture | pages [11] -->
m

<!-- b000795 | furniture | pages [11] -->
m

<!-- b000796 | furniture | pages [11] -->
m

<!-- b000797 | furniture | pages [11] -->
m

<!-- b000798 | furniture | pages [11] -->
m

<!-- b000799 | furniture | pages [11] -->
m

<!-- b000800 | furniture | pages [11] -->
m

<!-- b000801 | furniture | pages [11] -->
m

<!-- b000802 | furniture | pages [11] -->
m

<!-- b000803 | furniture | pages [11] -->
m

<!-- b000804 | furniture | pages [11] -->
m

<!-- b000805 | furniture | pages [11] -->
m

<!-- b000806 | furniture | pages [11] -->
m

<!-- b000807 | furniture | pages [11] -->
m

<!-- b000808 | furniture | pages [11] -->
m

<!-- b000809 | furniture | pages [11] -->
m

<!-- b000810 | furniture | pages [11] -->
m

<!-- b000811 | furniture | pages [11] -->
m

<!-- b000812 | furniture | pages [11] -->
m

<!-- b000813 | furniture | pages [11] -->
m

<!-- b000814 | furniture | pages [11] -->
m

<!-- b000815 | furniture | pages [11] -->
m

<!-- b000816 | furniture | pages [11] -->
m

<!-- b000817 | furniture | pages [11] -->
m

<!-- b000818 | furniture | pages [11] -->
m

<!-- b000819 | furniture | pages [11] -->
m

<!-- b000820 | furniture | pages [11] -->
m

<!-- b000821 | furniture | pages [11] -->
m

<!-- b000822 | furniture | pages [11] -->
m

<!-- b000823 | furniture | pages [11] -->
m

<!-- b000824 | furniture | pages [11] -->
m

<!-- b000825 | furniture | pages [11] -->
m

<!-- b000826 | furniture | pages [11] -->
m

<!-- b000827 | furniture | pages [11] -->
m

<!-- b000828 | furniture | pages [11] -->
m

<!-- b000829 | furniture | pages [11] -->
m

<!-- b000830 | furniture | pages [11] -->
m

<!-- b000831 | furniture | pages [11] -->
m

<!-- b000832 | furniture | pages [11] -->
m

<!-- b000833 | furniture | pages [11] -->
m

<!-- b000834 | furniture | pages [11] -->
m

<!-- b000835 | furniture | pages [11] -->
m

<!-- b000836 | furniture | pages [11] -->
m

<!-- b000837 | furniture | pages [11] -->
m

<!-- b000838 | furniture | pages [11] -->
m

<!-- b000839 | furniture | pages [11] -->
m

<!-- b000840 | furniture | pages [11] -->
m

<!-- b000841 | furniture | pages [11] -->
m

<!-- b000842 | furniture | pages [11] -->
m

<!-- b000843 | furniture | pages [11] -->
m

<!-- b000844 | furniture | pages [11] -->
m

<!-- b000845 | furniture | pages [11] -->
m

<!-- b000846 | furniture | pages [11] -->
m

<!-- b000847 | furniture | pages [11] -->
m

<!-- b000848 | furniture | pages [11] -->
m

<!-- b000849 | furniture | pages [11] -->
m

<!-- b000850 | furniture | pages [11] -->
m

<!-- b000851 | furniture | pages [11] -->
m

<!-- b000852 | furniture | pages [11] -->
m

<!-- b000853 | furniture | pages [11] -->
m

<!-- b000854 | furniture | pages [11] -->
m

<!-- b000855 | furniture | pages [11] -->
m

<!-- b000856 | furniture | pages [11] -->
m

<!-- b000857 | furniture | pages [11] -->
m

<!-- b000858 | furniture | pages [11] -->
m

<!-- b000859 | furniture | pages [11] -->
m

<!-- b000860 | furniture | pages [11] -->
m

<!-- b000861 | furniture | pages [11] -->
m

<!-- b000862 | furniture | pages [11] -->
m

<!-- b000863 | furniture | pages [11] -->
m

<!-- b000864 | furniture | pages [11] -->
m

<!-- b000865 | furniture | pages [11] -->
m

<!-- b000866 | furniture | pages [11] -->
m

<!-- b000867 | furniture | pages [11] -->
m

<!-- b000868 | furniture | pages [11] -->
m

<!-- b000869 | furniture | pages [11] -->
m

<!-- b000870 | furniture | pages [11] -->
m

<!-- b000871 | furniture | pages [11] -->
m

<!-- b000872 | furniture | pages [11] -->
m

<!-- b000873 | furniture | pages [11] -->
m

<!-- b000874 | furniture | pages [11] -->
m

<!-- b000875 | furniture | pages [11] -->
m

<!-- b000876 | furniture | pages [11] -->
m

<!-- b000877 | furniture | pages [11] -->
m

<!-- b000878 | furniture | pages [11] -->
m

<!-- b000879 | furniture | pages [11] -->
m

<!-- b000880 | furniture | pages [11] -->
m

<!-- b000881 | furniture | pages [11] -->
m

<!-- b000882 | furniture | pages [11] -->
m

<!-- b000883 | furniture | pages [11] -->
m

<!-- b000884 | furniture | pages [11] -->
m

<!-- b000885 | furniture | pages [11] -->
m

<!-- b000886 | furniture | pages [11] -->
m

<!-- b000887 | furniture | pages [11] -->
m

<!-- b000888 | furniture | pages [11] -->
m

<!-- b000889 | furniture | pages [11] -->
m

<!-- b000890 | furniture | pages [11] -->
m

<!-- b000891 | furniture | pages [11] -->
m

<!-- b000892 | furniture | pages [11] -->
m

<!-- b000893 | furniture | pages [11] -->
m

<!-- b000894 | furniture | pages [11] -->
m

<!-- b000895 | furniture | pages [11] -->
m

<!-- b000896 | furniture | pages [11] -->
m

<!-- b000897 | furniture | pages [11] -->
m

<!-- b000898 | furniture | pages [11] -->
m

<!-- b000899 | furniture | pages [11] -->
m

<!-- b000900 | furniture | pages [11] -->
m

<!-- b000901 | furniture | pages [11] -->
m

<!-- b000902 | furniture | pages [11] -->
m

<!-- b000903 | furniture | pages [11] -->
m

<!-- b000904 | furniture | pages [11] -->
m

<!-- b000905 | furniture | pages [11] -->
m

<!-- b000906 | furniture | pages [11] -->
m

<!-- b000907 | furniture | pages [11] -->
m

<!-- b000908 | furniture | pages [11] -->
m

<!-- b000909 | furniture | pages [11] -->
m

<!-- b000910 | furniture | pages [11] -->
m

<!-- b000911 | furniture | pages [11] -->
m

<!-- b000912 | furniture | pages [11] -->
m

<!-- b000913 | furniture | pages [11] -->
m

<!-- b000914 | furniture | pages [11] -->
m

<!-- b000915 | furniture | pages [11] -->
m

<!-- b000916 | furniture | pages [11] -->
m

<!-- b000917 | furniture | pages [11] -->
m

<!-- b000918 | furniture | pages [11] -->
m

<!-- b000919 | furniture | pages [11] -->
m

<!-- b000920 | furniture | pages [11] -->
m

<!-- b000921 | furniture | pages [11] -->
m

<!-- b000922 | furniture | pages [11] -->
m

<!-- b000923 | furniture | pages [11] -->
m

<!-- b000924 | furniture | pages [11] -->
m

<!-- b000925 | furniture | pages [11] -->
m

<!-- b000926 | furniture | pages [11] -->
m

<!-- b000927 | furniture | pages [11] -->
m

<!-- b000928 | furniture | pages [11] -->
m

<!-- b000929 | furniture | pages [11] -->
m

<!-- b000930 | furniture | pages [11] -->
m

<!-- b000931 | furniture | pages [11] -->
m

<!-- b000932 | furniture | pages [11] -->
m

<!-- b000933 | furniture | pages [11] -->
m

<!-- b000934 | furniture | pages [11] -->
m

<!-- b000935 | furniture | pages [11] -->
m

<!-- b000936 | furniture | pages [11] -->
m

<!-- b000937 | furniture | pages [11] -->
m

<!-- b000938 | furniture | pages [11] -->
m

<!-- b000939 | furniture | pages [11] -->
m

<!-- b000940 | furniture | pages [11] -->
m

<!-- b000941 | furniture | pages [11] -->
m

<!-- b000942 | furniture | pages [11] -->
m

<!-- b000943 | furniture | pages [11] -->
m

<!-- b000944 | furniture | pages [11] -->
m

<!-- b000945 | furniture | pages [11] -->
m

<!-- b000946 | furniture | pages [11] -->
m

<!-- b000947 | furniture | pages [11] -->
m

<!-- b000948 | furniture | pages [11] -->
m

<!-- b000949 | furniture | pages [11] -->
m

<!-- b000950 | furniture | pages [11] -->
m

<!-- b000951 | furniture | pages [11] -->
m

<!-- b000952 | furniture | pages [11] -->
m

<!-- b000953 | furniture | pages [11] -->
m

<!-- b000954 | furniture | pages [11] -->
m

<!-- b000955 | furniture | pages [11] -->
m

<!-- b000956 | furniture | pages [11] -->
m

<!-- b000957 | furniture | pages [11] -->
m

<!-- b000958 | furniture | pages [11] -->
m

<!-- b000959 | furniture | pages [11] -->
m

<!-- b000960 | furniture | pages [11] -->
m

<!-- b000961 | furniture | pages [11] -->
m

<!-- b000962 | furniture | pages [11] -->
m

<!-- b000963 | furniture | pages [11] -->
m

<!-- b000964 | furniture | pages [11] -->
m

<!-- b000965 | furniture | pages [11] -->
m

<!-- b000966 | furniture | pages [11] -->
m

<!-- b000967 | furniture | pages [11] -->
m

<!-- b000968 | furniture | pages [11] -->
m

<!-- b000969 | furniture | pages [11] -->
m

<!-- b000970 | furniture | pages [11] -->
m

<!-- b000971 | furniture | pages [11] -->
m

<!-- b000972 | furniture | pages [11] -->
m

<!-- b000973 | furniture | pages [11] -->
m

<!-- b000974 | furniture | pages [11] -->
m

<!-- b000975 | furniture | pages [11] -->
m

<!-- b000976 | furniture | pages [11] -->
m

<!-- b000977 | furniture | pages [11] -->
m

<!-- b000978 | furniture | pages [11] -->
m

<!-- b000979 | furniture | pages [11] -->
m

<!-- b000980 | furniture | pages [11] -->
m

<!-- b000981 | furniture | pages [11] -->
m

<!-- b000982 | furniture | pages [11] -->
m

<!-- b000983 | furniture | pages [11] -->
m

<!-- b000984 | furniture | pages [11] -->
m

<!-- b000985 | furniture | pages [11] -->
m

<!-- b000986 | furniture | pages [11] -->
m

<!-- b000987 | furniture | pages [11] -->
m

<!-- b000988 | furniture | pages [11] -->
m

<!-- b000989 | furniture | pages [11] -->
m

<!-- b000990 | furniture | pages [11] -->
m

<!-- b000991 | furniture | pages [11] -->
m

<!-- b000992 | furniture | pages [11] -->
m

<!-- b000993 | furniture | pages [11] -->
m

<!-- b000994 | furniture | pages [11] -->
m

<!-- b000995 | furniture | pages [11] -->
m

<!-- b000996 | furniture | pages [11] -->
m

<!-- b000997 | furniture | pages [11] -->
m

<!-- b000998 | furniture | pages [11] -->
m

<!-- b000999 | furniture | pages [11] -->
m

<!-- b001000 | furniture | pages [11] -->
m

<!-- b001001 | furniture | pages [11] -->
m

<!-- b001002 | furniture | pages [11] -->
m

<!-- b001003 | furniture | pages [11] -->
m

<!-- b001004 | furniture | pages [11] -->
m

<!-- b001005 | furniture | pages [11] -->
m

<!-- b001006 | furniture | pages [11] -->
m

<!-- b001007 | furniture | pages [11] -->
m

<!-- b001008 | furniture | pages [11] -->
m

<!-- b001009 | furniture | pages [11] -->
m

<!-- b001010 | furniture | pages [11] -->
m

<!-- b001011 | furniture | pages [11] -->
m

<!-- b001012 | furniture | pages [11] -->
m

<!-- b001013 | furniture | pages [11] -->
m

<!-- b001014 | furniture | pages [11] -->
m

<!-- b001015 | furniture | pages [11] -->
m

<!-- b001016 | furniture | pages [11] -->
m

<!-- b001017 | furniture | pages [11] -->
m

<!-- b001018 | furniture | pages [11] -->
m

<!-- b001019 | furniture | pages [11] -->
m

<!-- b001020 | furniture | pages [11] -->
m

<!-- b001021 | furniture | pages [11] -->
m

<!-- b001022 | furniture | pages [12] -->
Team # 2514461

<!-- b001023 | furniture | pages [12] -->
Page 11 of 25

<!-- b001024 | heading | pages [12] -->
5.4 Advanced: XGBoost model

<!-- b001025 | heading | pages [12] -->
5.4.1 Model Establishment

<!-- b001026 | prose | pages [12] -->
Since we had got all the history medal winning ratios, we then employed regression analysis using XGBoost model, combined with cross-validation and randomized search optimization.

<!-- b001027 | prose | pages [12] -->
XGBoost, an ensemble learning algorithm based on gradient boosting, is renowned for its efficiency in making predictions and generating rankings on small to medium-sized structured datasets. The inclusion of 5-fold cross-validation and grid search optimization can further enhance the model’s performance and ensures robust results. [3]

<!-- b001028 | prose | pages [12] -->
XGBoost is an efficient implementation of the gradient boosting algorithm that iteratively adds decision trees to optimize an objective function composed of a loss function for prediction errors and a regularization term for model complexity. In the tth iteration, the model attempts to learn a decision tree ft that fits the residuals r(t−1) = yi −ˆy(t−1) from the previous iteration, i i where yi is the true value and ˆy(t−1) is the predicted value from the previous iteration. The i objective function is defined as:

<!-- b001029 | prose | pages [12] -->
n l(r(t−1) X Obj = + ft(xi)) + Ω(ft)) (9) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m i m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m i=1 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Here, l is the loss function, and Ω(ft) is the regularization term, which penalizes large leaf m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m node weights and an excessive number of leaf nodes to prevent overfitting. In this way, XGBoost m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m can control the complexity of the model while maintaining its performance. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001030 | prose | pages [12] -->
We first collected statistics on the number of gold, silver and bronze medals each country won in each discipline every year, then divided by the total number of medals awarded in that discipline for that year to obtain the medal ratio of that country. By running an XGBoost model with the ratios from past years, we predicted medal ratios in 2028.

<!-- b001031 | caption | pages [12] -->
Figure 7: Probability prediction of Chinese diving gold and

<!-- b001032 | prose | pages [12] -->
Silver MEDALS in 2028 Olympic Games

<!-- b001033 | caption | pages [12] -->
Figure 6: Flow chart of medal

<!-- b001034 | prose | pages [12] -->
count based on XGBoost

<!-- b001035 | prose | pages [12] -->
Based on predictions, we took into account the host country effect, where athletes may

<!-- b001036 | prose | pages [12, 13] -->
关注数学模型 perform better when competing in their own country due to familiarity with the environment, reduced travel fatigue, easier adjustment to time zones and climate, and other factors. We calculated the score increases of the host countries in recent Olympic Games, measuring the host country effect by the ratio of this Game’s scores to last Game’s scores.

<!-- b001037 | furniture | pages [12] -->
2

<!-- b001038 | furniture | pages [12] -->
MATHmodels

<!-- b001039 | furniture | pages [12] -->
获取更多资讯

<!-- b001040 | furniture | pages [13] -->
Team # 2514461

<!-- b001041 | furniture | pages [13] -->
Page 12 of 25

<!-- b001043 | prose | pages [13] -->
We observed that approximately 90% of countries exhibit an improvement in their perfor- mance during the Olympics hosted in their own nation. Specifically, 77% of these countries have seen an increase exceeding 20%, and 44% have experienced an increase of more than 50%. However, the countries with increases over 50% tend to be those with relatively fewer points (the Soviet Union is excluded from this analysis as it has since transitioned into Russia and other countries). Therefore, it is unreasonable to anticipate a substantial increase for the United States, a major scoring country and the host of the 2028 Olympics. Considering that the U.S. 微信公众号：数学模型 has previously observed a decrease of 7% in scores when hosting, we deemed it reasonable to predict that the U.S. will have a hosting nation increase between 0% and 20% for the year 2024. In our predictive model, we incorporated a scoring increase of 15%.

<!-- b001044 | prose | pages [13] -->
微信号：MATHmodels

<!-- b001045 | caption | pages [13] -->
Figure 8: Analysis of the advantages of the host country. The light yellow score indicates the

<!-- b001046 | prose | pages [13] -->
score when the country was the host country, and the score ratio indicates the score when the country is the host country divided by the score of the previous Olympics Game.

<!-- b001047 | prose | pages [13] -->
After obtaining the medal winning ratios for each country in 2028 using the XGBoost model and considering the host country effect, we normalized these ratios and multiplied them by the number of events in each discipline as predicted by the SVR model discussed in the fourth section. This process ultimately yielded the predicted medal count, which we then displayed in a medal ranking table as Fig.10 shows.

<!-- b001048 | heading | pages [13] -->
5.5 Examining the confidence of the prediction interval

<!-- b001049 | prose | pages [13] -->
Since the XGBoost model can only return predicted values and not directly provide con- fidence intervals, we can use the predicted values given by XGBoost and the real number of medals to calculate the standard deviation of the residuals between the predicted and real values in the first step. In the second step, we can estimate the prediction interval by calculating the confidence interval using the predicted and actual values. Below is a detailed explanation of the approach.

<!-- b001050 | prose | pages [13, 14] -->
We used the sampling distribution theory in statistics to estimate the confidence intervals of prediction results. Due to the randomness of sampling, different samples may produce different m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001051 | furniture | pages [13] -->
m

<!-- b001052 | furniture | pages [13] -->
m

<!-- b001053 | furniture | pages [13] -->
m

<!-- b001054 | furniture | pages [13] -->
m

<!-- b001055 | furniture | pages [13] -->
m

<!-- b001056 | furniture | pages [13] -->
m

<!-- b001057 | furniture | pages [13] -->
m

<!-- b001058 | furniture | pages [13] -->
m

<!-- b001059 | furniture | pages [13] -->
m

<!-- b001060 | furniture | pages [13] -->
m

<!-- b001061 | furniture | pages [13] -->
m

<!-- b001062 | furniture | pages [13] -->
m

<!-- b001063 | furniture | pages [13] -->
m

<!-- b001064 | furniture | pages [13] -->
m

<!-- b001065 | furniture | pages [13] -->
m

<!-- b001066 | furniture | pages [13] -->
m

<!-- b001067 | furniture | pages [13] -->
m

<!-- b001068 | furniture | pages [13] -->
m

<!-- b001069 | furniture | pages [13] -->
m

<!-- b001070 | furniture | pages [13] -->
m

<!-- b001071 | furniture | pages [13] -->
m

<!-- b001072 | furniture | pages [13] -->
m

<!-- b001073 | furniture | pages [13] -->
m

<!-- b001074 | furniture | pages [13] -->
m

<!-- b001075 | furniture | pages [13] -->
m

<!-- b001076 | furniture | pages [13] -->
m

<!-- b001077 | furniture | pages [13] -->
m

<!-- b001078 | furniture | pages [13] -->
m

<!-- b001079 | furniture | pages [13] -->
m

<!-- b001080 | furniture | pages [13] -->
m

<!-- b001081 | furniture | pages [13] -->
m

<!-- b001082 | furniture | pages [13] -->
m

<!-- b001083 | furniture | pages [13] -->
m

<!-- b001084 | furniture | pages [13] -->
m

<!-- b001085 | furniture | pages [13] -->
m

<!-- b001086 | furniture | pages [13] -->
m

<!-- b001087 | furniture | pages [13] -->
m

<!-- b001088 | furniture | pages [13] -->
m

<!-- b001089 | furniture | pages [13] -->
m

<!-- b001090 | furniture | pages [13] -->
m

<!-- b001091 | furniture | pages [13] -->
m

<!-- b001092 | furniture | pages [13] -->
m

<!-- b001093 | furniture | pages [13] -->
m

<!-- b001094 | furniture | pages [13] -->
m

<!-- b001095 | furniture | pages [13] -->
m

<!-- b001096 | furniture | pages [13] -->
m

<!-- b001097 | furniture | pages [13] -->
m

<!-- b001098 | furniture | pages [13] -->
m

<!-- b001099 | furniture | pages [13] -->
m

<!-- b001100 | furniture | pages [13] -->
m

<!-- b001101 | furniture | pages [13] -->
m

<!-- b001102 | furniture | pages [13] -->
m

<!-- b001103 | furniture | pages [13] -->
m

<!-- b001104 | furniture | pages [13] -->
m

<!-- b001105 | furniture | pages [13] -->
m

<!-- b001106 | furniture | pages [13] -->
m

<!-- b001107 | furniture | pages [13] -->
m

<!-- b001108 | furniture | pages [13] -->
m

<!-- b001109 | furniture | pages [13] -->
m

<!-- b001110 | furniture | pages [13] -->
m

<!-- b001111 | furniture | pages [13] -->
m

<!-- b001112 | furniture | pages [13] -->
m

<!-- b001113 | furniture | pages [13] -->
m

<!-- b001114 | furniture | pages [13] -->
m

<!-- b001115 | furniture | pages [13] -->
m

<!-- b001116 | furniture | pages [13] -->
m

<!-- b001117 | furniture | pages [13] -->
m

<!-- b001118 | furniture | pages [13] -->
m

<!-- b001119 | furniture | pages [13] -->
m

<!-- b001120 | furniture | pages [13] -->
m

<!-- b001121 | furniture | pages [13] -->
m

<!-- b001122 | furniture | pages [13] -->
m

<!-- b001123 | furniture | pages [13] -->
m

<!-- b001124 | furniture | pages [13] -->
m

<!-- b001125 | furniture | pages [13] -->
m

<!-- b001126 | furniture | pages [13] -->
m

<!-- b001127 | furniture | pages [13] -->
m

<!-- b001128 | furniture | pages [13] -->
m

<!-- b001129 | furniture | pages [13] -->
m

<!-- b001130 | furniture | pages [13] -->
m

<!-- b001131 | furniture | pages [13] -->
m

<!-- b001132 | furniture | pages [13] -->
m

<!-- b001133 | furniture | pages [13] -->
m

<!-- b001134 | furniture | pages [13] -->
m

<!-- b001135 | furniture | pages [13] -->
m

<!-- b001136 | furniture | pages [13] -->
m

<!-- b001137 | furniture | pages [13] -->
m

<!-- b001138 | furniture | pages [13] -->
m

<!-- b001139 | furniture | pages [13] -->
m

<!-- b001140 | furniture | pages [13] -->
m

<!-- b001141 | furniture | pages [13] -->
m

<!-- b001142 | furniture | pages [13] -->
m

<!-- b001143 | furniture | pages [13] -->
m

<!-- b001144 | furniture | pages [13] -->
m

<!-- b001145 | furniture | pages [13] -->
m

<!-- b001146 | furniture | pages [13] -->
m

<!-- b001147 | furniture | pages [13] -->
m

<!-- b001148 | furniture | pages [13] -->
m

<!-- b001149 | furniture | pages [13] -->
m

<!-- b001150 | furniture | pages [13] -->
m

<!-- b001151 | furniture | pages [13] -->
m

<!-- b001152 | furniture | pages [13] -->
m

<!-- b001153 | furniture | pages [13] -->
m

<!-- b001154 | furniture | pages [13] -->
m

<!-- b001155 | furniture | pages [13] -->
m

<!-- b001156 | furniture | pages [13] -->
m

<!-- b001157 | furniture | pages [13] -->
m

<!-- b001158 | furniture | pages [13] -->
m

<!-- b001159 | furniture | pages [13] -->
m

<!-- b001160 | furniture | pages [13] -->
m

<!-- b001161 | furniture | pages [13] -->
m

<!-- b001162 | furniture | pages [13] -->
m

<!-- b001163 | furniture | pages [13] -->
m

<!-- b001164 | furniture | pages [13] -->
m

<!-- b001165 | furniture | pages [13] -->
m

<!-- b001166 | furniture | pages [13] -->
m

<!-- b001167 | furniture | pages [13] -->
m

<!-- b001168 | furniture | pages [13] -->
m

<!-- b001169 | furniture | pages [13] -->
m

<!-- b001170 | furniture | pages [13] -->
m

<!-- b001171 | furniture | pages [13] -->
m

<!-- b001172 | furniture | pages [13] -->
m

<!-- b001173 | furniture | pages [13] -->
m

<!-- b001174 | furniture | pages [13] -->
m

<!-- b001175 | furniture | pages [13] -->
m

<!-- b001176 | furniture | pages [13] -->
m

<!-- b001177 | furniture | pages [13] -->
m

<!-- b001178 | furniture | pages [13] -->
m

<!-- b001179 | furniture | pages [13] -->
m

<!-- b001180 | furniture | pages [13] -->
m

<!-- b001181 | furniture | pages [13] -->
m

<!-- b001182 | furniture | pages [13] -->
m

<!-- b001183 | furniture | pages [13] -->
m

<!-- b001184 | furniture | pages [13] -->
m

<!-- b001185 | furniture | pages [13] -->
m

<!-- b001186 | furniture | pages [13] -->
m

<!-- b001187 | furniture | pages [13] -->
m

<!-- b001188 | furniture | pages [13] -->
m

<!-- b001189 | furniture | pages [13] -->
m

<!-- b001190 | furniture | pages [13] -->
m

<!-- b001191 | furniture | pages [13] -->
m

<!-- b001192 | furniture | pages [13] -->
m

<!-- b001193 | furniture | pages [13] -->
m

<!-- b001194 | furniture | pages [13] -->
m

<!-- b001195 | furniture | pages [13] -->
m

<!-- b001196 | furniture | pages [13] -->
m

<!-- b001197 | furniture | pages [13] -->
m

<!-- b001198 | furniture | pages [13] -->
m

<!-- b001199 | furniture | pages [13] -->
m

<!-- b001200 | furniture | pages [13] -->
m

<!-- b001201 | furniture | pages [13] -->
m

<!-- b001202 | furniture | pages [13] -->
m

<!-- b001203 | furniture | pages [13] -->
m

<!-- b001204 | furniture | pages [13] -->
m

<!-- b001205 | furniture | pages [13] -->
m

<!-- b001206 | furniture | pages [13] -->
m

<!-- b001207 | furniture | pages [13] -->
m

<!-- b001208 | furniture | pages [13] -->
m

<!-- b001209 | furniture | pages [13] -->
m

<!-- b001210 | furniture | pages [13] -->
m

<!-- b001211 | furniture | pages [13] -->
m

<!-- b001212 | furniture | pages [13] -->
m

<!-- b001213 | furniture | pages [13] -->
m

<!-- b001214 | furniture | pages [13] -->
m

<!-- b001215 | furniture | pages [13] -->
m

<!-- b001216 | furniture | pages [13] -->
m

<!-- b001217 | furniture | pages [13] -->
m

<!-- b001218 | furniture | pages [13] -->
m

<!-- b001219 | furniture | pages [13] -->
m

<!-- b001220 | furniture | pages [13] -->
m

<!-- b001221 | furniture | pages [13] -->
m

<!-- b001222 | furniture | pages [13] -->
m

<!-- b001223 | furniture | pages [13] -->
m

<!-- b001224 | furniture | pages [13] -->
m

<!-- b001225 | furniture | pages [13] -->
m

<!-- b001226 | furniture | pages [13] -->
m

<!-- b001227 | furniture | pages [13] -->
m

<!-- b001228 | furniture | pages [13] -->
m

<!-- b001229 | furniture | pages [13] -->
m

<!-- b001230 | furniture | pages [13] -->
m

<!-- b001231 | furniture | pages [13] -->
m

<!-- b001232 | furniture | pages [13] -->
m

<!-- b001233 | furniture | pages [13] -->
m

<!-- b001234 | furniture | pages [13] -->
m

<!-- b001235 | furniture | pages [13] -->
m

<!-- b001236 | furniture | pages [13] -->
m

<!-- b001237 | furniture | pages [13] -->
m

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

<!-- b001375 | furniture | pages [14] -->
Team # 2514461

<!-- b001376 | furniture | pages [14] -->
Page 13 of 25

<!-- b001378 | caption | pages [14] -->
Figure 10: Top 10 of predicted 2028 medal

<!-- b001379 | prose | pages [14] -->
m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001380 | caption | pages [14] -->
Figure 9: Top 10 of predicted 2028 medal

<!-- b001381 | prose | pages [14] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m table with host country effect m m m m m m m m m m m m m m m table m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001382 | prose | pages [14] -->
statistics. The confidence interval provides a range within which we can say with certainty that the population parameter is included, usually at a 95% level. For this problem, we predicted the number of gold medals for each country in 2024, and compared it with the actual gold medal results of each country in 2024, we can calculate the mean and standard deviation of the residuals of the gold medal results in 2024.

<!-- b001383 | prose | pages [14] -->
n ¯e = 1 X ei (10) n i=1

<!-- b001384 | prose | pages [14] -->
v n u 1 X u (ei −¯e)2 σe = (11) t n −1 i=1

<!-- b001385 | prose | pages [14] -->
Assuming that the residuals ei follows a normal distribution N(¯e, σ2 e), we can use the properties of the normal distribution to calculate the prediction intervals at different confidence levels. For a given confidence level α (for example, 95%), the corresponding z-score zα/2 can be found (for a 95% confidence level, z0.025 ≈1.96). For each predicted value ˆyi, its prediction interval can be expressed as:

<!-- b001386 | prose | pages [14] -->
   ˆyi −zα/2 · σe, ˆyi + zα/2 · σe (12)

<!-- b001387 | prose | pages [14] -->
As shown in the Fig. 11, the pink dots represent the estimates of the number of gold medals for the top 9 countries in the 2024 Olympics, predicted by the XGBoost model with France as the host country in 2024. These are the predicted values for the number of gold medals for each country in 2024. Since we already knew the actual number of gold medals for each country in 2024, we can calculate the standard deviation of the residuals between the predicted and actual values. By combining the Z-score for a 95% confidence interval, we can calculate the upper and lower bounds of the 95% confidence interval for the prediction interval, as shown by the lavender legend in the figure.

<!-- b001388 | heading | pages [14] -->
5.6 A Mann-Kendall-based analysis to project significant change in medal

<!-- b001389 | prose | pages [14] -->
acquisition

<!-- b001390 | prose | pages [14] -->
Mann-Kendall test, a non-parametric method for identifying trends in time series data, is used to analyze the performance of each country in the past 5 Olympic Games [9]. The aim is to forecast which nations will exhibit substantial fluctuations in their medal tallies.

<!-- b001391 | prose | pages [14] -->
For a specific country’s time series of Olympic medal counts X = {x1, x2, ..., xn}, Mann-

<!-- b001392 | prose | pages [14, 15] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b001393 | furniture | pages [14] -->
2

<!-- b001394 | furniture | pages [14] -->
MATHmodels

<!-- b001395 | furniture | pages [14] -->
获取更多资讯

<!-- b001396 | furniture | pages [15] -->
Team # 2514461

<!-- b001397 | furniture | pages [15] -->
Page 14 of 25

<!-- b001399 | caption | pages [15] -->
Figure 11: Taking the 2024 gold medal predictions as an example, the confidence interval of

<!-- b001400 | prose | pages [15] -->
the XGBoost model is analyzed.

<!-- b001401 | prose | pages [15] -->
Kendall test first calculate the S statistic:

<!-- b001402 | prose | pages [15] -->
n−1 n X X sgn(xj −xi) S = (13) i=1 j=i+1

<!-- b001403 | prose | pages [15] -->
where sgn() is the sign function.

<!-- b001404 | prose | pages [15] -->
When there are ties in the data (i.e., repeated values), the variance of the S statistic needs to be adjusted. The variance of S is calculated as:

<!-- b001405 | prose | pages [15] -->
V ar(S) = n(n −1)(2n + 5) −Pm i=1 ti(ti −1)(2ti + 5) (14) 18 where m is the number of unique values in the data and ti is the number of times the ith unique value appears.

<!-- b001406 | prose | pages [15] -->
To standardize the S statistic, a Z statistic is calculated as:

<!-- b001407 | prose | pages [15] -->
Z = [S −E(S)] (15) p V ar(S)

<!-- b001408 | prose | pages [15] -->
where E(S) is the expected value of S. For a trend-free time series, E(S) is typically close to 0. Then, assuming that the z-value follows a standard normal distribution, we can perform a p-parameter test on the z-value that follows a standard normal distribution to identify data with a p-value less than 0.05, which allows us to determine whether there is a significant upward or downward trend.

<!-- b001409 | prose | pages [15, 16] -->
( if (z > 0) may improve if p < 0.05 if (z < 0) may worse Based on the analysis of the past twenty years, that is, the performance of the past five Olympic Games, we analyzed whether these countries would have a significantly better or worse performance in the 2028 Olympic Games. Since we considered that data from 20 years ago has less impact on the next Olympic Games than data from the past 20 years, which can better reflect the trend of a country’s Olympic level in recent years.

<!-- b001410 | furniture | pages [16] -->
Team # 2514461

<!-- b001411 | furniture | pages [16] -->
Page 15 of 25

<!-- b001413 | prose | pages [16] -->
We converted the gold, silver, and bronze medals of the countries in the past five Olympic Games into scores. Then we used the Mann-Kendall model to analyze the upward and downward trends of the countries. Finally, it is analyzed that four countries have a significant trend of improvement: NZL, ITA, NED, SWE, and one country has a significant downward trend, which is BLR.

<!-- b001414 | caption | pages [16] -->
Figure 12: The scores of countries with obvious upward or downward trend in the past 5

<!-- b001415 | prose | pages [16] -->
Olympic Games

<!-- b001416 | heading | pages [16] -->
6 Model III: First-time Medalist Prediction based on Cox

<!-- b001417 | heading | pages [16] -->
Proportional Hazard Model

<!-- b001418 | heading | pages [16] -->
6.1 Model Overview

<!-- b001419 | prose | pages [16] -->
This part utilizes a Cox proportional hazards model to predict the probability of a country winning its first Olympic medal. Key predictors taken into account include the number of athletes developed, Olympic participation history, and the diversity of sports culture. The model treats a country’s journey towards its first medal as a survival process, excluding data from countries that have already won medals. By fitting the model and conducting Monte Carlo simulations, we predicted the potential number of first-time medalists by 2028.

<!-- b001420 | heading | pages [16] -->
6.2 Theoretical Basis

<!-- b001421 | prose | pages [16] -->
The objective of Cox proportional hazard model is to estimate the hazard function, which represents the instantaneous risk of an event occurring at a specific time, given a set of predictor variables. It incorporates the proportional hazards assumption, which posits that the hazard ratios between any two individuals remain constant over time. Here, we can conceptualize probability for countries to picking up their very first medal as a measure of risk. The model utilizes a semi-parametric approach, modeling the baseline hazard function non-parametrically

<!-- b001422 | prose | pages [16, 17] -->
关注数学模型 while estimating the effects of predictor variables through coefficients in a linear predictor. This approach allows for flexibility in capturing complex relationships between covariates and the risk of the event. 微信公众号：数学模型

<!-- b001423 | furniture | pages [16] -->
2

<!-- b001424 | furniture | pages [16] -->
MATHmodels

<!-- b001425 | furniture | pages [16] -->
获取更多资讯

<!-- b001426 | furniture | pages [17] -->
Team # 2514461

<!-- b001427 | furniture | pages [17] -->
Page 16 of 25

<!-- b001429 | heading | pages [17] -->
6.3 Key Predictors of First-time Medalists

<!-- b001430 | prose | pages [17] -->
For countries that have yet to earn medals, their chance to make a landmark moment can be derived according to the features listed as below:

<!-- b001431 | prose | pages [17] -->
• Quantity of athletes developed The total number of athletes a country has sent to the Games through history is a strong indicator of its sports development levels, reflecting the depth and breadth of its sports talent pool.

<!-- b001432 | prose | pages [17] -->
• Olympic participation history How many times a nation has participated in the Olympics 微信号：MATHmodels reflects its engagement with the global sporting community and experience in competing with other teams in such a grand sport event.

<!-- b001433 | prose | pages [17] -->
• Diversity of sports culture The number of event categories a country has participated in over the past Games showcases the abundance of coaching resources and how rich its sports culture is, also contributing to its medal prospects.

<!-- b001434 | heading | pages [17] -->
6.4 Model establishment

<!-- b001435 | prose | pages [17] -->
The moment a country makes its first breakthrough and graduates from the Olympic Village for newcomers represents the time when our event of interest occurs, similar to a risk event studied in clinical medicine. Based on the hazard function, we defined the probability for a country to win the first medal at the Games in year t as P(t). Given the covariates we have discussed above, a Cox model can be established to estimate the probability of a country achieving its first medal win at a specific time point.

<!-- b001436 | prose | pages [17] -->
P(t, X) = P0(t)eβaXa(t)+βpXp(t)+βeXe(t) (16)

<!-- b001437 | prose | pages [17] -->
Xa(t) is the total number of unique athletes registered for Olympics from the first Games in 1896 to the Games before year t. Xp(t) is the number of the country’s participations in Olympics. Xe(t) is the total number of unique events the country participated in from the first Games to the Games before year t. P0(t) is the baseline hazard function reflecting the risk of an event occurring in the absence of other risk factors, namely the probability for a country that has never competed in a single Olympic Games to win the first medal in year t.

<!-- b001438 | heading | pages [17] -->
6.5 Model Fitting and Prediction

<!-- b001439 | prose | pages [17] -->
The function P(t, X) aims to model the trend in first-medal-winning probability for countries and then predict this probability for a certain country based on its characteristics in a certain year. Therefore, the data we used for fitting is the feature vector X = [Xa(t), Xp(t), Xe(t)] of each country up to and including the year of its first medal win, namely the process of the country stays in Olympic Village for newcomers, rather than including the data after a country wins its first medal. So we marked countries that had already won medals in each Games and conduct a survival analysis, treating Year as duration time and winning as the event. After excluding the data of countries with prior wins, we fitted a model and successfully forecast the likelihood of first-time winning for various countries in a given year such as 2028.

<!-- b001440 | furniture | pages [18] -->
Team # 2514461

<!-- b001441 | furniture | pages [18] -->
Page 17 of 25

<!-- b001442 | heading | pages [18] -->
6.6 Monte Carlo Simulation

<!-- b001443 | prose | pages [18] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Since we assumed independence between countries’ probabilities of obtaining their first m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m medal, if we conducted n repeated Olympic trials in year t and Y represents the number of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m times this country wins a medal for the first time, then Y will follow a binomial distribution. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Y (t) ∼(n(t), P(t)) (17) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001444 | prose | pages [18] -->
To simulate potential outcomes, we applied Monte Carlo simulations based on the predicted probabilities. After 100 million trials, we obtained the following distribution of the possible number of first-time medalists by 2028.

<!-- b001445 | caption | pages [18] -->
Figure 13: The distribution of the possible number of 2028 first-time medalists

<!-- b001446 | prose | pages [18] -->
As Fig. 13 shows, with a probability of 0.2273, 3 nations are projected to earn their first medal in 2028. The countries with the highest probability of achieving their first-ever medals in 2028 are Monaco (MON), Liechtenstein (LIE), and Myanmar (MYA) respectively.

<!-- b001447 | caption | pages [18] -->
Table 3 provides a breakthrough probability ranking of countries that have never won a

<!-- b001448 | prose | pages [18] -->
medal. The right column is the corresponding probability after exponential normalization.

<!-- b001449 | heading | pages [18] -->
7 Model IV: Great Coach Effect

<!-- b001450 | heading | pages [18] -->
7.1 Model Overview

<!-- b001451 | prose | pages [18] -->
This section quantifies the impact of coaches on a country’s Olympic performance. By developing a scoring system and applying a threshold method and Isolation Forest, we identified time points where significant performance improvements occur due to the introduction of a coach, namely differential points. The contribution and influence of coaches on specific countries and sports are quantified as factors to reflect the impact of coaches directly. These serve as the basis for us to select sports benefiting most from coaching for chosen countries. By applying both Linear Regression and Random Forest to handling the data of differential points we captured, we predicted the prospects of introducing coaches for specific sports in specific countries.

<!-- b001452 | prose | pages [18, 19] -->
关注数学模型 NOC Extrapolated Values Exponential Values MON 0.6995 0.0503 LIE 0.6434 0.0476 微信公众号：数学模型 MYA 0.6297 0.0469 MLT 0.6215 0.0465 BOL 0.5682 0.0441 MLI 0.5519 0.0434 NEP 0.5464 0.0432 CHA 0.5452 0.0431 LBR 0.5343 0.0427 BIZ 0.5309 0.0425 CGO 0.5203 0.0421 AND 0.5163 0.0419 微信号：MATHmodels MAD 0.5066 0.0415 LES 0.5045 0.0414 GUI 0.4990 0.0412 BEN 0.4957 0.0410 NCA 0.4946 0.0410 SLE 0.4851 0.0406 CAY 0.4747 0.0402 CAF 0.4733 0.0401

<!-- b001453 | furniture | pages [18] -->
2

<!-- b001454 | furniture | pages [18] -->
MATHmodels

<!-- b001455 | furniture | pages [18] -->
获取更多资讯

<!-- b001456 | furniture | pages [19] -->
Team # 2514461

<!-- b001457 | furniture | pages [19] -->
Page 18 of 25

<!-- b001458 | caption | pages [19] -->
Table 3: Extrapolated and Exponential Values for top 20 first-time medalists in 2028

<!-- b001460 | prose | pages [19] -->
It’s worth noting that only in this part, sport is essentially a discipline, given the significant differences between various disciplines in practice and the fact that a coach often specializes in a single discipline. While the analysis at this level shares the same principles as at the sport level, it will be more accurate and detailed.

<!-- b001461 | heading | pages [19] -->
7.2 Effect Evidence

<!-- b001462 | prose | pages [19] -->
A coach plays a pivotal role in a country’s Olympic performance. If a country introduces a coach in a specific sport, it is highly likely that the country’s performance in that will see a significant improvement in the following years. For instance, in China in 2003, after introducing Coach Guoliang Liu to table tennis, the country’s performance improved markedly. Therefore, we can estimate the impact of coaches (Great Coach Effect, GCE) by examining the changes in performance over time. We can identify differential points as those where we conclude that a coaching effect took place.

<!-- b001463 | heading | pages [19] -->
7.2.1 Threshold Method

<!-- b001464 | prose | pages [19] -->
The first-order difference and first-order ratio of score S are defined as

<!-- b001465 | prose | pages [19] -->
△S = Si −Si−1 (18)

<!-- b001466 | prose | pages [19] -->
Si γS = (19) Si−1

<!-- b001467 | prose | pages [19, 20] -->
The larger △S and γS are, the greater progress the country have made in ith Olympics. The first method to determine whether GCE has happened is to set a threshold value ST△for the first-order difference and STγ for the first-order ratio of scores between consecutive Olympic Games and compare the actual △S and γS with them.

<!-- b001468 | furniture | pages [20] -->
Team # 2514461

<!-- b001469 | furniture | pages [20] -->
Page 19 of 25

<!-- b001471 | prose | pages [20] -->
( if △S ≥ST || γS ≥STγ, 1 GCE = (20) 0 else.

<!-- b001472 | prose | pages [20] -->
Points with a GCE value of 1 are defined as differential points.

<!-- b001473 | prose | pages [20] -->
These threshold values are established to minimize the variance in a country’s total score due to the exceptional performance by certain individuals and consider the progress of small nations. A △S or γS exceeding the threshold indicates a statistically significant improvement in the country’s overall performance, suggesting a substantial coaching effect.

<!-- b001474 | heading | pages [20] -->
7.2.2 Isolation Forest

<!-- b001475 | prose | pages [20] -->
We also employed the Isolation Forest method to capture the differences in Score S.

<!-- b001476 | prose | pages [20] -->
Isolation Forest is an ensemble-based method for anomaly detection. It identifies outliers by randomly selecting features and feature values to build multiple isolation trees, each of which isolates data points by randomly choosing features and split points. The anomaly score for a data point is typically given by the negative exponential of its average path length in the isolation tree, i.e., score(x) = −2−E(h(x)) , where E(h(x)) is the average path length of data point x in c the isolation tree, and c is the average path length of the tree. The shorter the path length, the higher the anomaly score, making it easier to identify outliers.

<!-- b001477 | prose | pages [20] -->
For instance, ifcountry’sdifferentialvaluesovertheyearsarerepresentedas[X1, X2, . . . , Xn], where Xn is the largest, then Xn will be closest to the root node in the isolation tree. By ex- tracting these points, we can identify some of the larger differential points in Score.

<!-- b001478 | heading | pages [20] -->
7.3 GCE contribution to medal counts

<!-- b001479 | prose | pages [20] -->
To measure the contribution of great coaches to a country’s performance at the ith Games, we defined a contribution factor Ci.

<!-- b001480 | prose | pages [20] -->
P j∈sports αij△Sij Ci = (21) P j∈sports Sij If △Sij > ST, αij = 1; else αij = 0.

<!-- b001481 | prose | pages [20] -->
This factor quantifies how much the great coaches of a whole country contributes to its medal counts. It’s different from country to country. The data we calculated are listed in table 4 in order.

<!-- b001482 | heading | pages [20] -->
7.4 GCE influence on certain sports

<!-- b001483 | prose | pages [20] -->
To measure the influence of a coach to any country’s performance in a certain sport s, we defined an influence factor Is.

<!-- b001484 | prose | pages [20] -->
P P countries△Ssk>ST αsk△Ssk k∈years Is = (22) P P countries△Ssk>ST Ssk k∈years

<!-- b001485 | prose | pages [20] -->
If △Ssk > ST, αsk = 1; else αsk = 0. This factor mirror the relationship between coach and sports. It’s different from sport to sport. Because the mobility of coaches is global, we assumed the Is is the same for each country. We ranked Is in table 5.

<!-- b001486 | prose | pages [20, 21] -->
关注数学模型 NOC and their corresponding

<!-- b001487 | furniture | pages [20] -->
2

<!-- b001488 | furniture | pages [20] -->
MATHmodels

<!-- b001489 | furniture | pages [20] -->
获取更多资讯

<!-- b001490 | furniture | pages [21] -->
Team # 2514461

<!-- b001491 | furniture | pages [21] -->
Page 20 of 25

<!-- b001492 | caption | pages [21] -->
Table 4:

<!-- b001494 | caption | pages [21] -->
Table 5: Sports and their corresponding

<!-- b001495 | prose | pages [21] -->
Contribution Factor Influence Factor C2024 Is NOC Sport VIE 1.0000 Cycling Mountain Bike 1.0000 SGP 1.0000 3x3 Basketball 1.0000 CIV 1.0000 Cycling BMX Racing 1.0000 TTO 1.0000 Cycling BMX Freestyle 1.0000 ISL 1.0000 Golf 0.8690 微信公众号：数学模型 MAR 0.9318 Surfing 0.8333 CHI 0.9167 Triathlon 0.8161 IRL 0.8635 Sport Climbing 0.8125 POR 0.8590 Trampolining 0.8077 SMR 0.8333 Tug-Of-War 0.8068 Canoe Slalom 0.8065 ANZ 0.8182 EST 0.8034 Modern Pentathlon 0.8063 Cycling Road 0.8000 BOT 0.8000 BRN 0.8000 Art Competitions 0.7850 Beach Volleyball 0.7692 BAH 0.7894 MEX 0.7843 Handball 0.7590 微信号：MATHmodels Trampoline Gymnastics 0.7500 MGL 0.7500 NGR 0.7159 Football 0.7399 Water Polo 0.7358 PHI 0.6875 URU 0.6778 Tennis 0.7324 Softball 0.7238 ETH 0.6691 SLO 0.6666 Volleyball 0.7211 HKG 0.6666 Hockey 0.7124 ESP 0.6611 Rhythmic Gymnastics 0.7063 DOM 0.6538 Sailing 0.7058 RSA 0.6427 Baseball 0.6989 ECU 0.6306 Archery 0.6987 KEN 0.6266 Artistic Swimming 0.6970 PAK 0.6242 Shooting 0.6814 CRO 0.6306 Taekwondo 0.6777

<!-- b001496 | heading | pages [21] -->
7.5 Application and Estimation

<!-- b001497 | prose | pages [21] -->
7.5.1 choosing countries and sports

<!-- b001498 | prose | pages [21] -->
In order to specify the sports where coaching investment would yield the better returns for them, we ranked sports based on their coaching influence factor Is to identify those most susceptible to coaching effects. Then, we determined whether their historical performance in each sport falls within a promising range(Smin, Smax), which means they have enough potential and room for improvement both. If so, we would consider introducing a great coach.

<!-- b001499 | heading | pages [21] -->
7.5.2 Great Coach Effect Prediction

<!-- b001500 | prose | pages [21] -->
Our goal is to build a model to forecast the impact of introducing a coach in a particular sport. By extracting differential data points that exhibit a coaching effect and plotting the previous Game’s scores against the subsequent Game’s scores, we discovered a discernible pattern.

<!-- b001501 | furniture | pages [22] -->
Team # 2514461

<!-- b001502 | furniture | pages [22] -->
Page 21 of 25

<!-- b001503 | prose | pages [22] -->
So we employed both Regression Analysis and Random Forest to fit a function, which we denoted as F, where the previous Game's score Si-1 is the independent variable and the following Game's score Si is the dependent variable.

<!-- b001504 | prose | pages [22] -->
(23) F(Si−1) = Si

<!-- b001505 | prose | pages [22] -->
F reflects the pattern of score improvement under Great Coach Effect. Once the sport and the previous score Si–1 are determined, the following year's score Si can be predicted regardless of the country or year.

<!-- b001506 | heading | pages [22] -->
7.5.3 Results

<!-- b001507 | prose | pages [22] -->
We choose CHN, USA and TPE for case study and recommend 2 sports for each of them in

<!-- b001508 | caption | pages [22] -->
table 6. The rank is the Is rank of corresponding sports.

<!-- b001509 | caption | pages [22] -->
Table 6: Sports choosen for specific countries

<!-- b001510 | prose | pages [22] -->
NOC Sport IsRank Sailing 26 CHN Archery 28 Canoe Slalom 12 USA 31 Taekwondo Surfing 7 TPE 29 Artistic Swimming

<!-- b001511 | prose | pages [22] -->
By inputting each country's score S2024 of this sport into the fitted models (linear regression and random forest respectively), we can predict its winning outcomes S2028 if they introduce a great coach. The results are shown as follows:

<!-- b001512 | prose | pages [22] -->
Linear Regression for Archery Random Forest Regression for Archery 120 Actual Data 120 Actual Data ● 0 Random Forest Prediction 0 Linear Regression Prediction for x=2 (y=3.19) ★ Prediction for x=2 (y=10.15) ★ 100 100

<!-- b001513 | prose | pages [22] -->
Score in Coach Year 80 80 Score in Coach Year 60 60

<!-- b001514 | prose | pages [22] -->
e 40 40 8 o 20 0 0 20 8 0C 8 0 20 25 10 15 5 0 25 20 5 15 10 0 Score in Previous Year Score in Previous Year

<!-- b001515 | caption | pages [22] -->
Figure 14: CHN Archery S prediction

<!-- b001516 | caption | pages [22] -->
Figure 15: CHN Archery S prediction

<!-- b001517 | prose | pages [22] -->
-Linear Regression -Random Forest

<!-- b001518 | prose | pages [22, 23] -->
关注数学模型 Linear Regression for Taekwondo 12 Actual Data ● Linear Regression Prediction for x=5 (y=7.37) ★ 10 Score in Coach Year o 8 O O ★ o O

<!-- b001519 | furniture | pages [22] -->
获取更多资讯

<!-- b001520 | furniture | pages [23] -->
Team # 2514461

<!-- b001522 | prose | pages [23] -->
● ● O 4 ● ● o ● o 2 ● 6 0 2 5 7 8 1 ε 4 Score in Previous Year

<!-- b001523 | caption | pages [23] -->
Figure 16: USA Taekwondo S prediction

<!-- b001524 | prose | pages [23] -->
-Linear Regression

<!-- b001525 | prose | pages [23] -->
Linear Regression for Swimming Actual Data 200 Linear Regression Prediction for x=0 (y=9.76) O ★ 175 o 150 Score in Coach Year 125 100 O 0 O 75 O 50 25 0 150 25 125 100 50 75 Score in Previous Year V

<!-- b001526 | caption | pages [23] -->
Figure 18: TPE Swimming S prediction

<!-- b001527 | prose | pages [23] -->
-Linear Regression

<!-- b001528 | furniture | pages [23] -->
Page 22 of 25

<!-- b001529 | prose | pages [23] -->
Random Forest Regression for Taekwondo 12 Actual Data e Random Forest Prediction 0 Prediction for x=5 (y=8.14) ￥ 0 10

<!-- b001530 | prose | pages [23] -->
Score in Coach Year ★ 8 0 0 00 ● o e

<!-- b001531 | prose | pages [23] -->
e 0 00

<!-- b001532 | prose | pages [23] -->
8 6 0 2 score in Previous Year

<!-- b001533 | caption | pages [23] -->
Figure 17: USA Taekwondo S prediction

<!-- b001534 | prose | pages [23] -->
-Random Forest

<!-- b001535 | prose | pages [23] -->
Random Forest Regression for Swimming Actual Data 200 Random Forest Prediction 0 Prediction for x=0 (y=8.59) ★ 0 175 00 00 150 e 8 Score in Coach Year 125 o 8 e 100 e

<!-- b001536 | prose | pages [23] -->
75

<!-- b001537 | prose | pages [23] -->
50

<!-- b001538 | prose | pages [23] -->
25

<!-- b001539 | prose | pages [23] -->
125 150 25 50 75 100 Score in Previous Year

<!-- b001540 | caption | pages [23] -->
Figure 19: TPE Swimming S prediction

<!-- b001541 | prose | pages [23] -->
-Random Forest

<!-- b001542 | prose | pages [23] -->
By averaging the two results, we obtained the predicted score S2o28.In the case of CHN archery, the score increases from 2 to 7. For USA Taekwondo, the score increases from 5 to 8, and for TPE swimming, it increases from 0 to 9.

<!-- b001543 | prose | pages [23] -->
Insights 8

<!-- b001544 | heading | pages [23] -->
8.1 From Models Above

<!-- b001545 | prose | pages [23] -->
• We have successfully predicted the percentage of medals each country will win in each discipline based solely on historical data. This can serve as a reference for each country to set breakthrough goals. The extent to which the number of medals changes under the influence of the host country's venue has been predicted, which can inspire each country's Olympic Committee to determine the extent to which they should enhance their training to adapt to the venue.

<!-- b001546 | prose | pages [23] -->
• For countries that have not won any medals, we have provided the probability of achieving a breakthrough in the next Olympic Games, which can to some extent boost the confi- dence of countries with a high probability of winning medals, as they have provided a breakthrough trajectory from zero to one.

<!-- b001547 | furniture | pages [24] -->
Team # 2514461

<!-- b001548 | furniture | pages [24] -->
Page 23 of 25

<!-- b001549 | furniture | pages [24] -->
m

<!-- b001550 | furniture | pages [24] -->
m

<!-- b001551 | furniture | pages [24] -->
m

<!-- b001552 | furniture | pages [24] -->
m

<!-- b001553 | furniture | pages [24] -->
m

<!-- b001554 | furniture | pages [24] -->
m

<!-- b001555 | furniture | pages [24] -->
m

<!-- b001556 | furniture | pages [24] -->
m

<!-- b001557 | furniture | pages [24] -->
m

<!-- b001558 | furniture | pages [24] -->
m

<!-- b001559 | furniture | pages [24] -->
m

<!-- b001560 | furniture | pages [24] -->
m

<!-- b001561 | furniture | pages [24] -->
m

<!-- b001562 | furniture | pages [24] -->
m

<!-- b001563 | furniture | pages [24] -->
m

<!-- b001564 | furniture | pages [24] -->
m

<!-- b001565 | furniture | pages [24] -->
m

<!-- b001566 | furniture | pages [24] -->
m

<!-- b001567 | furniture | pages [24] -->
m

<!-- b001568 | furniture | pages [24] -->
m

<!-- b001569 | furniture | pages [24] -->
m

<!-- b001570 | furniture | pages [24] -->
m

<!-- b001571 | furniture | pages [24] -->
m

<!-- b001572 | furniture | pages [24] -->
m

<!-- b001573 | furniture | pages [24] -->
m

<!-- b001574 | furniture | pages [24] -->
m

<!-- b001575 | furniture | pages [24] -->
m

<!-- b001576 | furniture | pages [24] -->
m

<!-- b001577 | furniture | pages [24] -->
m

<!-- b001578 | furniture | pages [24] -->
m

<!-- b001579 | furniture | pages [24] -->
m

<!-- b001580 | furniture | pages [24] -->
m

<!-- b001581 | furniture | pages [24] -->
m

<!-- b001582 | furniture | pages [24] -->
m

<!-- b001583 | furniture | pages [24] -->
m

<!-- b001584 | furniture | pages [24] -->
m

<!-- b001585 | furniture | pages [24] -->
m

<!-- b001586 | furniture | pages [24] -->
m

<!-- b001587 | furniture | pages [24] -->
m

<!-- b001588 | furniture | pages [24] -->
m

<!-- b001589 | furniture | pages [24] -->
m

<!-- b001590 | furniture | pages [24] -->
m

<!-- b001591 | furniture | pages [24] -->
m

<!-- b001592 | furniture | pages [24] -->
m

<!-- b001593 | furniture | pages [24] -->
m

<!-- b001594 | furniture | pages [24] -->
m

<!-- b001595 | furniture | pages [24] -->
m

<!-- b001596 | furniture | pages [24] -->
m

<!-- b001597 | furniture | pages [24] -->
m

<!-- b001598 | furniture | pages [24] -->
m

<!-- b001599 | furniture | pages [24] -->
m

<!-- b001600 | furniture | pages [24] -->
m

<!-- b001601 | furniture | pages [24] -->
m

<!-- b001602 | furniture | pages [24] -->
m

<!-- b001603 | furniture | pages [24] -->
m

<!-- b001604 | furniture | pages [24] -->
m

<!-- b001605 | furniture | pages [24] -->
m

<!-- b001606 | furniture | pages [24] -->
m

<!-- b001607 | furniture | pages [24] -->
m

<!-- b001608 | furniture | pages [24] -->
m

<!-- b001609 | furniture | pages [24] -->
m

<!-- b001610 | furniture | pages [24] -->
m

<!-- b001611 | furniture | pages [24] -->
m

<!-- b001612 | furniture | pages [24] -->
m

<!-- b001613 | furniture | pages [24] -->
m

<!-- b001614 | furniture | pages [24] -->
m

<!-- b001615 | furniture | pages [24] -->
m

<!-- b001616 | furniture | pages [24] -->
m

<!-- b001617 | furniture | pages [24] -->
m

<!-- b001618 | furniture | pages [24] -->
m

<!-- b001619 | furniture | pages [24] -->
m

<!-- b001620 | furniture | pages [24] -->
m

<!-- b001621 | furniture | pages [24] -->
m

<!-- b001622 | furniture | pages [24] -->
m

<!-- b001623 | furniture | pages [24] -->
m

<!-- b001624 | furniture | pages [24] -->
m

<!-- b001625 | furniture | pages [24] -->
m

<!-- b001626 | furniture | pages [24] -->
m

<!-- b001627 | furniture | pages [24] -->
m

<!-- b001628 | furniture | pages [24] -->
m

<!-- b001629 | furniture | pages [24] -->
m

<!-- b001630 | furniture | pages [24] -->
m

<!-- b001631 | furniture | pages [24] -->
m

<!-- b001632 | furniture | pages [24] -->
m

<!-- b001633 | furniture | pages [24] -->
m

<!-- b001634 | furniture | pages [24] -->
m

<!-- b001635 | furniture | pages [24] -->
m

<!-- b001636 | furniture | pages [24] -->
m

<!-- b001637 | furniture | pages [24] -->
m

<!-- b001638 | furniture | pages [24] -->
m

<!-- b001639 | furniture | pages [24] -->
m

<!-- b001640 | furniture | pages [24] -->
m

<!-- b001641 | furniture | pages [24] -->
m

<!-- b001642 | furniture | pages [24] -->
m

<!-- b001643 | furniture | pages [24] -->
m

<!-- b001644 | furniture | pages [24] -->
m

<!-- b001645 | furniture | pages [24] -->
m

<!-- b001646 | furniture | pages [24] -->
m

<!-- b001647 | furniture | pages [24] -->
m

<!-- b001648 | furniture | pages [24] -->
m

<!-- b001649 | furniture | pages [24] -->
m

<!-- b001650 | furniture | pages [24] -->
m

<!-- b001651 | furniture | pages [24] -->
m

<!-- b001652 | furniture | pages [24] -->
m

<!-- b001653 | furniture | pages [24] -->
m

<!-- b001654 | furniture | pages [24] -->
m

<!-- b001655 | furniture | pages [24] -->
m

<!-- b001656 | furniture | pages [24] -->
m

<!-- b001657 | prose | pages [24] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001658 | prose | pages [24] -->
• In the study of GCE, we provided the Olympic Committees with a list of sports that would m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m most easily improved with the help of coaches through impact factors. It is important to m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m select coaches for introduction based on the specific circumstances of different countries. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Blindly choosing to improve weaknesses may not yield good returns. In addition, our m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001659 | prose | pages [24] -->
fitted prediction model can also map out a blueprint for their progress.

<!-- b001660 | heading | pages [24] -->
8.2 Extra Study: Impact of Gender Ratio

<!-- b001661 | prose | pages [24] -->
We analyzed the proportion of women’s points in the Olympics from 1986 to 2024. It was found that from 1896 to 2014, the proportion of women’s points in the Olympics continued to increase, from 5% in 1986 to nearly 50% in 2024, reflecting the increasingly important role of female athletes in international Olympic competitions.

<!-- b001662 | prose | pages [24] -->
We then analyzed countries that performed well at the Olympics, such as the United States and China, and found that the proportion of points scored by female athletes in their Olympic scores was close to 60%, higher than the world average. This indicates that they place great emphasis on the role of female athletes in the overall Olympic performance of their countries.

<!-- b001663 | prose | pages [24] -->
We also analyzed Japan and the UK, two countries with decent Olympic performances, and found that the proportion of points scored by female athletes in their Olympic scores was slightly below 50%. For CUB and UZB, two countries with less than ideal Olympic performances, the proportion of female athletes was only 30%. Therefore, our suggestion is to pay more attention to and cultivate female athletes, which can help to further explore the potential for better national performance in Olympic events.

<!-- b001664 | caption | pages [24] -->
Figure 20: Relationship between predicted score after hiring a coach and the thresholds

<!-- b001665 | heading | pages [24] -->
9 Sensitivity Analysis

<!-- b001666 | prose | pages [24] -->
We performed sensitivity analysis for the two thresholds, namely the score difference thresh- old and the score increase rate threshold, which we calculated and employed to detect where great coaches played an important role in sports.

<!-- b001667 | prose | pages [24] -->
We yield the following key observations:

<!-- b001668 | prose | pages [24, 25] -->
关注数学模型 微信公众号：数学模型

<!-- b001669 | furniture | pages [24] -->
2

<!-- b001670 | furniture | pages [24] -->
MATHmodels

<!-- b001671 | furniture | pages [24] -->
获取更多资讯

<!-- b001672 | furniture | pages [25] -->
Team # 2514461

<!-- b001673 | furniture | pages [25] -->
Page 24 of 25

<!-- b001675 | caption | pages [25] -->
Figure 21: Relationship between predicted score after hiring a coach and the thresholds

<!-- b001676 | prose | pages [25] -->
• As the rate threshold increases, there is a slight increase in the predicted score, especially 微信号：MATHmodels when the score threshold is low. Nevertheless, our model is relatively robust to rate threshold.

<!-- b001677 | prose | pages [25] -->
• The score threshold has a significant impact on the predicted score, especially when set to higher values. A sharp increase in the predicted score is observed as the score threshold approaches higher values, particularly above 7. This suggests that the model is highly sensitive to changes in the score threshold at this range. However, we set rate threshold to 1.2 in the calculations, where the model is not that sensitive to the score threshold.

<!-- b001678 | prose | pages [25] -->
• The shape of the 3D surface agreed to our intuitions, that is, as the threshold is increased, "greater" coaches remain, and these coaches would help the athletes win more medals, and also the more precious ones, leading to a greater increase in predicted scores.

<!-- b001679 | prose | pages [25] -->
• Overall, given that one Gold medal would contribute 3 to the score, our model is rather stable in reasonable ranges of thresholds, which is, 1.2 ≤rate-threshold ≤4, and 3 ≤ score-threshold ≤7.

<!-- b001680 | heading | pages [25] -->
10 Strength and Weakness

<!-- b001681 | heading | pages [25] -->
10.1 Strength

<!-- b001682 | prose | pages [25] -->
• Reasoning. Our model is constructed from a logical foundation, allowing us to provide more granular details such as the medal count of each country in different disciplines and the winning probability of each first-time medalists, enhancing the accuracy and reliability of our overall predictions.

<!-- b001683 | prose | pages [25] -->
• Comprehensiveness. We took many factors into account like the impact of the host country effect and the association between event count and medal count. In addition, we finished comparative analysis and found better model.

<!-- b001684 | prose | pages [25] -->
• Stability. Our model demonstrates robust stability when thresholds are set within the optimal range, highly adaptable to potential changes in various history data. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001685 | furniture | pages [25] -->
m

<!-- b001686 | furniture | pages [25] -->
m

<!-- b001687 | furniture | pages [25] -->
m

<!-- b001688 | furniture | pages [25] -->
m

<!-- b001689 | furniture | pages [25] -->
m

<!-- b001690 | furniture | pages [25] -->
m

<!-- b001691 | furniture | pages [25] -->
m

<!-- b001692 | furniture | pages [25] -->
m

<!-- b001693 | furniture | pages [25] -->
m

<!-- b001694 | furniture | pages [25] -->
m

<!-- b001695 | furniture | pages [25] -->
m

<!-- b001696 | furniture | pages [25] -->
m

<!-- b001697 | furniture | pages [25] -->
m

<!-- b001698 | furniture | pages [25] -->
m

<!-- b001699 | furniture | pages [25] -->
m

<!-- b001700 | furniture | pages [25] -->
m

<!-- b001701 | furniture | pages [25] -->
m

<!-- b001702 | furniture | pages [25] -->
m

<!-- b001703 | furniture | pages [25] -->
m

<!-- b001704 | furniture | pages [25] -->
m

<!-- b001705 | furniture | pages [25] -->
m

<!-- b001706 | furniture | pages [25] -->
m

<!-- b001707 | furniture | pages [25] -->
m

<!-- b001708 | furniture | pages [25] -->
m

<!-- b001709 | furniture | pages [25] -->
m

<!-- b001710 | furniture | pages [25] -->
m

<!-- b001711 | furniture | pages [25] -->
m

<!-- b001712 | furniture | pages [25] -->
m

<!-- b001713 | furniture | pages [25] -->
m

<!-- b001714 | furniture | pages [25] -->
m

<!-- b001715 | furniture | pages [25] -->
m

<!-- b001716 | furniture | pages [25] -->
m

<!-- b001717 | furniture | pages [25] -->
m

<!-- b001718 | furniture | pages [25] -->
m

<!-- b001719 | furniture | pages [25] -->
m

<!-- b001720 | furniture | pages [25] -->
m

<!-- b001721 | furniture | pages [25] -->
m

<!-- b001722 | furniture | pages [25] -->
m

<!-- b001723 | furniture | pages [25] -->
m

<!-- b001724 | furniture | pages [25] -->
m

<!-- b001725 | furniture | pages [25] -->
m

<!-- b001726 | furniture | pages [25] -->
m

<!-- b001727 | furniture | pages [25] -->
m

<!-- b001728 | furniture | pages [25] -->
m

<!-- b001729 | furniture | pages [25] -->
m

<!-- b001730 | furniture | pages [25] -->
m

<!-- b001731 | furniture | pages [25] -->
m

<!-- b001732 | furniture | pages [25] -->
m

<!-- b001733 | furniture | pages [25] -->
m

<!-- b001734 | furniture | pages [25] -->
m

<!-- b001735 | furniture | pages [25] -->
m

<!-- b001736 | furniture | pages [25] -->
m

<!-- b001737 | furniture | pages [25] -->
m

<!-- b001738 | furniture | pages [25] -->
m

<!-- b001739 | furniture | pages [25] -->
m

<!-- b001740 | furniture | pages [25] -->
m

<!-- b001741 | furniture | pages [25] -->
m

<!-- b001742 | furniture | pages [25] -->
m

<!-- b001743 | furniture | pages [25] -->
m

<!-- b001744 | furniture | pages [25] -->
m

<!-- b001745 | furniture | pages [25] -->
m

<!-- b001746 | furniture | pages [25] -->
m

<!-- b001747 | furniture | pages [25] -->
m

<!-- b001748 | furniture | pages [25] -->
m

<!-- b001749 | furniture | pages [25] -->
m

<!-- b001750 | furniture | pages [25] -->
m

<!-- b001751 | furniture | pages [25] -->
m

<!-- b001752 | furniture | pages [25] -->
m

<!-- b001753 | furniture | pages [25] -->
m

<!-- b001754 | furniture | pages [25] -->
m

<!-- b001755 | furniture | pages [25] -->
m

<!-- b001756 | furniture | pages [25] -->
m

<!-- b001757 | furniture | pages [25] -->
m

<!-- b001758 | furniture | pages [25] -->
m

<!-- b001759 | furniture | pages [25] -->
m

<!-- b001760 | furniture | pages [25] -->
m

<!-- b001761 | furniture | pages [25] -->
m

<!-- b001762 | furniture | pages [25] -->
m

<!-- b001763 | furniture | pages [25] -->
m

<!-- b001764 | furniture | pages [25] -->
m

<!-- b001765 | furniture | pages [25] -->
m

<!-- b001766 | furniture | pages [25] -->
m

<!-- b001767 | furniture | pages [25] -->
m

<!-- b001768 | furniture | pages [25] -->
m

<!-- b001769 | furniture | pages [25] -->
m

<!-- b001770 | furniture | pages [25] -->
m

<!-- b001771 | furniture | pages [25] -->
m

<!-- b001772 | furniture | pages [25] -->
m

<!-- b001773 | furniture | pages [25] -->
m

<!-- b001774 | furniture | pages [25] -->
m

<!-- b001775 | furniture | pages [25] -->
m

<!-- b001776 | furniture | pages [25] -->
m

<!-- b001777 | furniture | pages [25] -->
m

<!-- b001778 | furniture | pages [25] -->
m

<!-- b001779 | furniture | pages [25] -->
m

<!-- b001780 | furniture | pages [25] -->
m

<!-- b001781 | furniture | pages [25] -->
m

<!-- b001782 | furniture | pages [25] -->
m

<!-- b001783 | furniture | pages [25] -->
m

<!-- b001784 | furniture | pages [25] -->
m

<!-- b001785 | furniture | pages [25] -->
m

<!-- b001786 | furniture | pages [25] -->
m

<!-- b001787 | furniture | pages [25] -->
m

<!-- b001788 | furniture | pages [25] -->
m

<!-- b001789 | furniture | pages [25] -->
m

<!-- b001790 | furniture | pages [25] -->
m

<!-- b001791 | furniture | pages [25] -->
m

<!-- b001792 | furniture | pages [25] -->
m

<!-- b001793 | furniture | pages [25] -->
m

<!-- b001794 | furniture | pages [25] -->
m

<!-- b001795 | furniture | pages [25] -->
m

<!-- b001796 | furniture | pages [25] -->
m

<!-- b001797 | furniture | pages [25] -->
m

<!-- b001798 | furniture | pages [25] -->
m

<!-- b001799 | furniture | pages [25] -->
m

<!-- b001800 | furniture | pages [25] -->
m

<!-- b001801 | furniture | pages [25] -->
m

<!-- b001802 | furniture | pages [25] -->
m

<!-- b001803 | furniture | pages [25] -->
m

<!-- b001804 | furniture | pages [25] -->
m

<!-- b001805 | furniture | pages [25] -->
m

<!-- b001806 | furniture | pages [25] -->
m

<!-- b001807 | furniture | pages [25] -->
m

<!-- b001808 | furniture | pages [25] -->
m

<!-- b001809 | furniture | pages [25] -->
m

<!-- b001810 | furniture | pages [25] -->
m

<!-- b001811 | furniture | pages [25] -->
m

<!-- b001812 | furniture | pages [25] -->
m

<!-- b001813 | furniture | pages [25] -->
m

<!-- b001814 | furniture | pages [25] -->
m

<!-- b001815 | furniture | pages [25] -->
m

<!-- b001816 | furniture | pages [25] -->
m

<!-- b001817 | furniture | pages [25] -->
m

<!-- b001818 | furniture | pages [25] -->
m

<!-- b001819 | furniture | pages [25] -->
m

<!-- b001820 | furniture | pages [25] -->
m

<!-- b001821 | furniture | pages [25] -->
m

<!-- b001822 | furniture | pages [25] -->
m

<!-- b001823 | furniture | pages [25] -->
m

<!-- b001824 | furniture | pages [25] -->
m

<!-- b001825 | furniture | pages [25] -->
m

<!-- b001826 | furniture | pages [25] -->
m

<!-- b001827 | furniture | pages [25] -->
m

<!-- b001828 | furniture | pages [25] -->
m

<!-- b001829 | furniture | pages [25] -->
m

<!-- b001830 | furniture | pages [25] -->
m

<!-- b001831 | furniture | pages [25] -->
m

<!-- b001832 | furniture | pages [25] -->
m

<!-- b001833 | furniture | pages [25] -->
m

<!-- b001834 | furniture | pages [25] -->
m

<!-- b001835 | furniture | pages [25] -->
m

<!-- b001836 | furniture | pages [25] -->
m

<!-- b001837 | furniture | pages [25] -->
m

<!-- b001838 | furniture | pages [25] -->
m

<!-- b001839 | furniture | pages [25] -->
m

<!-- b001840 | furniture | pages [25] -->
m

<!-- b001841 | furniture | pages [25] -->
m

<!-- b001842 | furniture | pages [25] -->
m

<!-- b001843 | furniture | pages [25] -->
m

<!-- b001844 | furniture | pages [25] -->
m

<!-- b001845 | furniture | pages [25] -->
m

<!-- b001846 | furniture | pages [25] -->
m

<!-- b001847 | furniture | pages [25] -->
m

<!-- b001848 | furniture | pages [25] -->
m

<!-- b001849 | furniture | pages [25] -->
m

<!-- b001850 | furniture | pages [25] -->
m

<!-- b001851 | furniture | pages [25] -->
m

<!-- b001852 | furniture | pages [25] -->
m

<!-- b001853 | furniture | pages [25] -->
m

<!-- b001854 | furniture | pages [25] -->
m

<!-- b001855 | furniture | pages [25] -->
m

<!-- b001856 | furniture | pages [25] -->
m

<!-- b001857 | furniture | pages [25] -->
m

<!-- b001858 | furniture | pages [25] -->
m

<!-- b001859 | furniture | pages [25] -->
m

<!-- b001860 | furniture | pages [25] -->
m

<!-- b001861 | furniture | pages [25] -->
m

<!-- b001862 | furniture | pages [25] -->
m

<!-- b001863 | furniture | pages [25] -->
m

<!-- b001864 | furniture | pages [25] -->
m

<!-- b001865 | furniture | pages [25] -->
m

<!-- b001866 | furniture | pages [25] -->
m

<!-- b001867 | furniture | pages [25] -->
m

<!-- b001868 | furniture | pages [25] -->
m

<!-- b001869 | furniture | pages [25] -->
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

<!-- b002009 | furniture | pages [26] -->
Team # 2514461

<!-- b002010 | furniture | pages [26] -->
Page 25 of 25

<!-- b002011 | heading | pages [26] -->
10.2 Weakness

<!-- b002012 | prose | pages [26] -->
• Idealization. Despite the fact that we have already conducted a detailed analysis of datasets and fitted a prediction model relying solely on historical by using relatively advanced methods,a few, such as GDPs, population resources and geographical locations were still neglected, leading to the limitations of our model.

<!-- b002013 | heading | pages [26] -->
10.3 Room for Improvement

<!-- b002014 | prose | pages [26] -->
• There are more details worth exploring such as the growth rate of performance. Extra information about economic development and population can be used to optimize the model for more practical use.

<!-- b002015 | heading | pages [26] -->
References

<!-- b002016 | references | pages [26] -->
[1] Z. Bo, Q. Chaoling, X. Xiaoli and Z. Fanbo, "GM (1,1) Model Gray Prediction for the

<!-- b002017 | references | pages [26] -->
Gold-Medal Result of Women’s Put Shot in the 30th Olympic Games," 2011 International

<!-- b002018 | references | pages [26] -->
Conference on Future Computer Science and Education, Xi’an, China, 2011.

<!-- b002019 | references | pages [26] -->
[2] J. Moolchandani, V. Chole, S. Sahu, R. Kumar, A. Shukla and A. Kumar, "Predictive An-

<!-- b002020 | references | pages [26] -->
alytics in Sports: Using Machine Learning to Forecast Outcomes and Medal Tally Trends

<!-- b002021 | references | pages [26] -->
at the 2024 Summer Olympics," 2024 4th International Conference on Technological

<!-- b002022 | references | pages [26] -->
Advancements in Computational Sciences (ICTACS), Tashkent, Uzbekistan, 2024.

<!-- b002023 | references | pages [26] -->
[3] N. T. M. Sagala and M. Amien Ibrahim, "A Comparative Study of Different Boosting

<!-- b002024 | references | pages [26] -->
Algorithms for Predicting Olympic Medal," 2022 IEEE 8th International Conference on

<!-- b002025 | references | pages [26] -->
Computing, Engineering and Design (ICCED), Sukabumi, Indonesia, 2022.

<!-- b002026 | references | pages [26] -->
[4] N. O. Abdelsalam, M. K. Elbashir and S. M. SaadEldeen, "Applying Cox Regression in

<!-- b002027 | references | pages [26] -->
Time to Event Data," 2018 International Conference on Computer, Control, Electrical,

<!-- b002028 | references | pages [26] -->
and Electronics Engineering (ICCCEEE), Khartoum, Sudan, 2018.

<!-- b002029 | references | pages [26] -->
[5] Z. Zhao, Y. Zhang, X. Zhu and J. Zuo, "Research on Time Series Anomaly Detection

<!-- b002030 | references | pages [26] -->
Algorithm and Application," 2019 IEEE 4th Advanced Information Technology, Electronic

<!-- b002031 | references | pages [26] -->
and Automation Control Conference (IAEAC), Chengdu, China, 2019.

<!-- b002032 | references | pages [26] -->
[6] Y. Qin and Y. Lou, "Hydrological Time Series Anomaly Pattern Detection based on

<!-- b002033 | references | pages [26] -->
Isolation Forest," 2019 IEEE 3rd Information Technology, Networking, Electronic and

<!-- b002034 | references | pages [26] -->
Automation Control Conference (ITNEC), Chengdu, China, 2019.

<!-- b002035 | references | pages [26] -->
[7] Poongadan, S., Lineesh, M.C. Non-linear Time Series Prediction using Improved CEEM-

<!-- b002036 | references | pages [26] -->
DAN, SVD and LSTM. Neural Process Lett 56, 164 (2024).

<!-- b002037 | references | pages [26] -->
[8] Kamal, Neel and Sanjay Pachauri. “Mann-Kendall Test - A Novel Approach for Statistical

<!-- b002038 | references | pages [26] -->
Trend Analysis.” International Journal of Computer Trends and Technology (2018): n.

<!-- b002039 | references | pages [26] -->
pag.

<!-- b002040 | references | pages [26] -->
关注数学模型

<!-- b002041 | furniture | pages [26] -->
2

<!-- b002042 | furniture | pages [26] -->
MATHmodels

<!-- b002043 | furniture | pages [26] -->
获取更多资讯

<!-- b002044 | furniture | pages [27] -->
Team # 2514461

<!-- b002045 | furniture | pages [27] -->
Page 1 of 25

<!-- b002046 | heading | pages [27] -->
Appendices

<!-- b002047 | prose | pages [27] -->
Country Gold Silver Bronze Total Country Gold Silver Bronze Total USA 47 45 36 128 COL 0 4 0 4 CHN 35 24 15 74 KAZ 0 1 3 4 GBR 16 21 21 58 RSA 1 2 1 4 FRA 13 16 14 43 TUR 0 1 3 4 微信公众号：数学模型 AUS 14 11 16 41 ECU 1 1 1 3 JPN 18 9 10 37 GDR 1 1 1 3 ITA 11 9 15 35 GRE 1 0 2 3 GER 11 11 12 34 INA 1 0 2 3 NED 9 8 10 27 IND 0 1 2 3 KOR 9 7 6 22 IRL 2 0 1 3 ROC 6 10 6 22 MEX 0 1 2 3 CAN 6 6 9 21 THA 1 1 1 3 HUN 6 8 5 19 ARM 0 2 0 2 NZL 7 5 4 16 AZE 0 1 1 2 微信号：MATHmodels BRA 3 4 5 12 BLR 0 1 1 2 ESP 3 5 4 12 ETH 0 1 1 2 SWE 3 5 3 11 FIN 0 0 2 2 POL 2 4 4 10 FRG 0 1 1 2 SUI 2 3 5 10 HKG 1 0 1 2 CUB 4 2 3 9 ISR 1 1 0 2 UKR 1 4 4 9 SLO 2 0 0 2 DEN 2 3 3 8 AIN 0 1 0 1 KEN 3 2 3 8 ARG 0 0 1 1 ROU 2 4 1 7 DOM 0 1 0 1 BEL 2 1 3 6 EGY 0 0 1 1 CZE 3 1 2 6 GRN 0 0 1 1 IRI 2 3 1 6 KGZ 0 1 0 1 TPE 2 1 3 6 MAS 0 0 1 1 UZB 4 1 1 6 MDA 0 0 1 1 BUL 2 1 2 5 MGL 0 1 0 1 CRO 2 2 1 5 PHI 1 0 0 1 GEO 2 3 0 5 POR 0 1 0 1 JAM 2 1 2 5 PRK 0 0 1 1 NOR 3 1 1 5 RUS 0 0 1 1 SRB 2 1 2 5 UGA 1 0 0 1 URS 2 1 2 5 VEN 0 1 0 1 AUT 1 1 2 4 others 0 0 0 0

<!-- b002048 | caption | pages [27] -->
Table 7: All the countries that are predicted to earn medals in 2028 USA Olympic Games based

<!-- b002049 | prose | pages [27] -->
on XGBoost model (considering home country effect

<!-- b002050 | furniture | pages [28] -->
Team # 2514461

<!-- b002051 | furniture | pages [28] -->
Page 2 of 25

<!-- b002052 | heading | pages [28] -->
Report on Use of AI

<!-- b002053 | ai_disclosure | pages [28] -->
1. OpenAI ChatGPT (Jan 27, 2025 version, ChatGPT-4)

<!-- b002054 | ai_disclosure | pages [28] -->
Query1: Is there a contradiction between satisfying the proportional hazards assumption

<!-- b002055 | ai_disclosure | pages [28] -->
and the independence of two individuals?

<!-- b002056 | ai_disclosure | pages [28] -->
Output: The proportional hazards assumption and the independence of individuals are

<!-- b002057 | ai_disclosure | pages [28] -->
different concepts and are not contradictory. Let's explain these two concepts

<!-- b002058 | ai_disclosure | pages [28] -->
separately:

<!-- b002059 | ai_disclosure | pages [28] -->
In the Cox regression model, the proportional hazards assumption requires that the

<!-- b002060 | ai_disclosure | pages [28] -->
hazard ratios between different individuals remain constant over the entire observa-

<!-- b002061 | ai_disclosure | pages [28] -->
tion period. This means that, relative to a baseline individual, the hazard ratio (i.e.,

<!-- b002062 | ai_disclosure | pages [28] -->
the rate at which an event occurs) between different individuals is fixed and does not

<!-- b002063 | ai_disclosure | pages [28] -->
depend on time. This assumption does not require the independence of individuals.

<!-- b002064 | ai_disclosure | pages [28] -->
In other words, even if there are dependencies between individuals, the proportional

<!-- b002065 | ai_disclosure | pages [28] -->
hazards assumption can still hold.

<!-- b002066 | ai_disclosure | pages [28] -->
Independence of Individuals: Independence of individuals typically refers to the

<!-- b002067 | ai_disclosure | pages [28] -->
assumption that the survival time of one individual is not related to the survival time

<!-- b002068 | ai_disclosure | pages [28] -->
of another individual. For example, the survival time of two individuals does not

<!-- b002069 | ai_disclosure | pages [28] -->
influence each other, and the occurrence of an event for one individual does not alter

<!-- b002070 | ai_disclosure | pages [28] -->
the probability of the event occurring for another individual. In the Cox regression

<!-- b002071 | ai_disclosure | pages [28] -->
model, individuals in the dataset are typically assumed to be independent, meaning

<!-- b002072 | ai_disclosure | pages [28] -->
that the occurrence of an event for one individual is independent of others, even

<!-- b002073 | ai_disclosure | pages [28] -->
though their survival times may be affected by some common risk factors.

<!-- b002074 | ai_disclosure | pages [28] -->
Relationship between the Two: The proportional hazards assumption and the

<!-- b002075 | ai_disclosure | pages [28] -->
independence of individuals are not mutually exclusive. In the Cox regression model,

<!-- b002076 | ai_disclosure | pages [28] -->
the assumption is that the hazard ratio for each individual is fixed, but this does not

<!-- b002077 | ai_disclosure | pages [28] -->
require complete independence between individuals. In practice, individuals may

<!-- b002078 | ai_disclosure | pages [28] -->
share common factors (e.g., environment, treatment, genetic factors) that influence

<!-- b002079 | ai_disclosure | pages [28] -->
their survival risk, but as long as the influence of these factors remains consistent

<!-- b002080 | ai_disclosure | pages [28] -->
and the proportional hazards assumption holds, complete independence between

<!-- b002081 | ai_disclosure | pages [28] -->
individuals is not necessary.

<!-- b002082 | ai_disclosure | pages [28] -->
If there is some form of dependency between individuals in the data (e.g., family

<!-- b002083 | ai_disclosure | pages [28] -->
members or individuals in the same experimental group), caution is needed in

<!-- b002084 | ai_disclosure | pages [28] -->
modeling. In such cases, adjustments may be required, such as using more complex

<!-- b002085 | ai_disclosure | pages [28] -->
models like group or cluster analysis methods to account for these dependencies.

<!-- b002086 | ai_disclosure | pages [28] -->
Therefore, the proportional hazards assumption and the independence of individuals

<!-- b002087 | ai_disclosure | pages [28] -->
do not conflict. The Cox regression model mainly relies on the proportional hazards

<!-- b002088 | ai_disclosure | pages [28] -->
assumption, which requires that the hazard ratios within the same group remain

<!-- b002089 | ai_disclosure | pages [28] -->
constant, while the independence between individuals depends on the actual data

<!-- b002090 | ai_disclosure | pages [28] -->
situation.

<!-- b002091 | heading | pages [28] -->
Query2: Summarize the article A Comparative Study of Different Boosting Algorithms

<!-- b002092 | prose | pages [28] -->
for Predicting Olympic Medal.

<!-- b002093 | prose | pages [28] -->
Output: The article "A Comparative Study of Different Boosting Algorithms for Pre- dicting Olympic Medal" explores various boosting algorithms used to predict the likelihood of countries winning Olympic medals. The main points of the article are:

<!-- b002094 | heading | pages [28] -->
Boosting Algorithms Overview: The study compares different boosting algo-

<!-- b002095 | prose | pages [28] -->
rithms, including AdaBoost, Gradient Boosting, and XGBoost, highlighting their

<!-- b002096 | prose | pages [28, 29] -->
关注数学模型 ability to improve prediction accuracy by combining weak learners (models that perform slightly better than random guessing) into a stronger, more robust model.

<!-- b002097 | furniture | pages [28] -->
获取更多资讯

<!-- b002098 | furniture | pages [29] -->
Team # 2514461

<!-- b002099 | furniture | pages [29] -->
Page 3 of 25

<!-- b002101 | prose | pages [29] -->
Data and Features: The authors use historical Olympic data, such as athletes’ per- formance, country-specific features, and external factors like economic conditions and political stability, to train the models. They preprocess the data by handling missing values and normalizing features to enhance model performance.

<!-- b002102 | heading | pages [29] -->
Model Evaluation: The article assesses the performance of each boosting algorithm

<!-- b002103 | prose | pages [29] -->
using various evaluation metrics such as accuracy, precision, recall, and F1-score.

<!-- b002104 | prose | pages [29] -->
The results show that XGBoost outperforms other algorithms in terms of prediction accuracy, likely due to its advanced regularization techniques and tree-based model optimizations.

<!-- b002105 | prose | pages [29] -->
Key Findings: XGBoost was found to be the most effective algorithm for predicting 微信公众号：数学模型 Olympic medal outcomes, while AdaBoost showed slightly lower performance. The study emphasizes the importance of tuning hyperparameters and cross-validation for boosting models to avoid overfitting and improve generalizability.

<!-- b002106 | prose | pages [29] -->
In conclusion, the article demonstrates the effectiveness of boosting algorithms, par- ticularly XGBoost, in predicting Olympic medal outcomes based on a combination of performance data and country-related features.

<!-- b002107 | prose | pages [29] -->
Query3: Is the Basis of Monte Carlo Simulation the Binomial Distribution?

<!-- b002108 | prose | pages [29] -->
Output: The basis of Monte Carlo simulation is not specifically the binomial distribution.

<!-- b002109 | prose | pages [29] -->
It is a statistical method that uses random sampling to simulate and compute the 微信号：MATHmodels solutions to complex problems. Monte Carlo simulations can use various probability distributions, including the binomial distribution, but it is not limited to it.

<!-- b002110 | prose | pages [29] -->
Basic Concept of Monte Carlo Simulation Monte Carlo simulation is a technique used to estimate the statistical properties of complex problems or systems by gen- erating a large number of random samples. The core idea of this method is to use a computer to generate random data and approximate solutions to real-world problems based on that data. Its foundation does not rely on any specific probability distribution but instead utilizes various distributions to simulate the behavior of systems.

<!-- b002111 | prose | pages [29] -->
Binomial Distribution and Monte Carlo Simulation The binomial distribution can serve as one possible random distribution in Monte Carlo simulation, especially when simulating Bernoulli trials (e.g., events of success or failure). For example, if we needed to simulate multiple independent binomial trials (such as multiple coin tosses), we can use the binomial distribution to model the random variables.

<!-- b002112 | prose | pages [29] -->
However, the strength of Monte Carlo simulation lies in its flexibility. It is not confined to a single distribution. Any suitable probability distribution can be chosen for the simulation, and common distributions include:

<!-- b002113 | prose | pages [29] -->
Uniform Distribution: When each outcome has an equal probability. Normal Distribution: When the variation of the variables follows a normal distribution (e.g., stock price movements). Exponential Distribution: Used to model the time intervals between events (e.g., the arrival time of phone calls).

<!-- b002114 | heading | pages [29] -->
Poisson Distribution: Used to model the number of events happening within a

<!-- b002115 | prose | pages [29] -->
fixed period (e.g., machine failures).

<!-- b002116 | prose | pages [29, 30] -->
Binomial Distribution: Used to model a fixed number of Bernoulli trials (e.g., the result of tossing a coin). Steps in Monte Carlo Simulation Define the Model and Objective: First, define the random process that needs to be simulated and the objective to be estimated. For example, this might involve calculating the expected value, probability, etc., of a complex problem. Choose the Appropriate Probability Distribution: Based on the nature of the problem, select an appropriate probability distribution to generate the random vari- ables. For instance, if simulating a coin toss, the binomial distribution might be used to model the result of each toss. Generate Random Samples: Use a computer to generate a large number of random samples, each following the selected probability distribution. Run the Simulation: Run multiple simulations based on the generated random samples and perform the necessary calculations. Each simulation represents a possible state of the system.

<!-- b002117 | furniture | pages [30] -->
Page 4 of 25

<!-- b002118 | furniture | pages [30] -->
Team # 2514461

<!-- b002120 | heading | pages [30] -->
Analyze the Results: Perform statistical analysis on the simulation results, typically

<!-- b002121 | prose | pages [30] -->
calculating averages, variances, probabilities, etc., to estimate the performance of the model or solve the problem. Applications of Monte Carlo Simulation Monte Carlo simulation can be widely applied in various fields, such as: Financial Modeling: Estimating stock prices, option pricing, etc. Physical Simu- lations: Modeling the movement of particles in a physical field. Engineering Design: Assessing the reliability of system designs. Operations Research: Optimizing decision-making processes in complex systems. Risk As- sessment: Evaluating the risks of decisions under uncertainty.

<!-- b002122 | prose | pages [30] -->
关注数学模型

<!-- b002123 | furniture | pages [30] -->
获取更多资讯
