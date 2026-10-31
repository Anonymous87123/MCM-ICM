# P-C-2025-2514461-4da6b888

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
In model I, we predicted the number of events in every discipline at the 2028 Games. We first preprocessed the data, grouping the players by their teams and countries.

<!-- b000014 | prose | pages [1] -->
We chose to analyze the data on disciplines, summing up their events since events in the same discipline are similar and tend to develop simultaneously, also avoiding overgeneralizing to the level of sports. We employed Support Vector Regression (SVR) instead of Linear Regression, which cannot interpret the complex structure of the data. SVR captured the nonlinear patterns in the data, with MSE equals 1.744 and R-squared 0.634, doing nicely for recent years. We also analyzed the importance of different sports for different countries using weighted sums of medals, and visualized it using rose plots.

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
In Model II, based on the event number predictions in Model I, we predicted the medal numbers in 2028. We first attempted at a plain Long Short Term Memory (LSTM) model. We employed the technique of the Adam optimizer and plateau-detection schedulers. We also added punishment terms, forcing the model to predict equal numbers for all medal types. However, results showed clear underfitting and overfitting. Therefore, we turned to an advanced XGBoost model. In this model, we predicted fractions instead of numbers, and multiplied the fractions with results in model I to yield final medal counts. Noting that 90% of host countries witnessed significant improvement, we averaged the increase as 15%, multiplied to the 2028 host USA, and normalized the results. USA topped the board with 47 golds, 45 silvers and 36 bronzes, China followed with 35, 24, 15, and then Japan with 18, 9 and 10. We evaluated the soundness of this model on year 2024. The 95% confidence intervals were calculated for 9 typical countries, and all predicted results lied in the intervals, proving high reliability.

<!-- b000017 | prose | pages [1] -->
In Model III, we addressed the cases where a country that had never earned an Olympic medal earned its first at 2028. We employed the Cox Proportional Hazard Model, with its risk function representing the possibility that a country switched from the no-medal status to first-medal status. By fitting the model, normalizing the results, and Monte-Carlo simulations, we predicted the potential number of first-time medalists by 2028. 3 is the most likely with probability 22.73%, and the three most likely first-time medalists are Monaco, Liechtenstein and Myanmar.

<!-- b000018 | prose | pages [1] -->
In Model IV, we addressed the Great Coach Effect (GCE). We developed a Threshold Method, filtering first- order difference and first-order ratio of score, where scores are calculated by a weighted sum of medal counts. An ensemble-learning anomaly detection method, Isolation Forest, was also employed to cross-validate the choice of weights. We ended up choosing 3, 2 and 1. There was a 89% correspondence between the two methods. We selected the thresholds accordingly. Detection was an OR-logic with the two thresholds. Summing up all years and teams, we measured GCE influence on every sport. We chose USA, CHN and TPE for analysis, and identified the most GCE-influenced sports that they play. We yielded that Taekwondo for USA, Archery for CHN and Swimming for TPE, are their most coach-needing sports. We then used our own ensemble learning by averaging the prediction results of Linear Regression and Random Forest. The data for fitting are all the threshold-activated points for the sport. We predicted that CHN Archery would go from 2 in 2024 to 7 in 2028, USA Taekwondo from 5 to 8, and TPE Swimming from 0 to 9, after hiring great coaches.

<!-- b000019 | prose | pages [1] -->
Finally, we looked into the male-female score ratio to provide insights on gender-equality since data showed that the stronger countries are more gender-balanced. We visualized our results, showing the predicted medals, the fitted lines, random forests and coach effects. Meanwhile, strengths and weaknesses of the models were analyzed, insights were visualized and discussed, and sensitivity analysis was done.

<!-- b000020 | keywords | pages [1] -->
Keywords: Threshold Method, SVR, XGBoost, LSTM, Mann-Kendall, Cox, Isolation Forest, Linear Regression,

<!-- b000021 | prose | pages [1] -->
Random Forest

<!-- b000022 | prose | pages [3] -->
8 Insights 22 From Models Above . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 22 Extra Study: Impact of Gender Ratio . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000023 | prose | pages [3] -->
9

<!-- b000024 | heading | pages [3] -->
Sensitivity Analysis

<!-- b000025 | heading | pages [3] -->
10 Strength and Weakness

<!-- b000026 | prose | pages [3] -->
23

<!-- b000027 | prose | pages [3] -->
23

<!-- b000028 | prose | pages [3] -->
24 10.1 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | prose | pages [3] -->
24

<!-- b000030 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000031 | prose | pages [3] -->
10.2 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | prose | pages [3] -->
25 10.3 Room for Improvement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | prose | pages [3] -->
Reference

<!-- b000034 | heading | pages [3] -->
Appendices

<!-- b000035 | prose | pages [3] -->
25

<!-- b000036 | prose | pages [3] -->
25

<!-- b000037 | prose | pages [3] -->
1

<!-- b000038 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000039 | prose | pages [3] -->
m

<!-- b000040 | prose | pages [3] -->
m

<!-- b000041 | prose | pages [3] -->
m

<!-- b000042 | prose | pages [3] -->
m

<!-- b000043 | prose | pages [3] -->
m

<!-- b000044 | prose | pages [3] -->
m

<!-- b000045 | prose | pages [3] -->
m

<!-- b000046 | prose | pages [3] -->
m

<!-- b000047 | prose | pages [3] -->
m

<!-- b000048 | prose | pages [3] -->
m

<!-- b000049 | prose | pages [3] -->
m

<!-- b000050 | prose | pages [3] -->
m

<!-- b000051 | prose | pages [3] -->
m

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

<!-- b000726 | furniture | pages [4] -->
Team # 2514461

<!-- b000727 | prose | pages [4] -->
1

<!-- b000728 | heading | pages [4] -->
Introduction

<!-- b000729 | prose | pages [4] -->
1.1

<!-- b000730 | heading | pages [4] -->
Background

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

<!-- b000745 | prose | pages [4] -->
m

<!-- b000746 | prose | pages [4] -->
m

<!-- b000747 | prose | pages [4] -->
m

<!-- b000748 | prose | pages [4] -->
m

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

<!-- b000962 | furniture | pages [4] -->
Page 3 of 25

<!-- b000963 | prose | pages [4] -->
Following the conclusion of the 2024 Paris Olympics, nations are turning to the 2028 Los

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
Angeles Games. As a globally celebrated sporting event, the Olympics serves as not only a

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
world stage for athletes to showcase their exceptional sportsmanship, but also a platform for

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
cultural exchange and fostering friendship among nations. Consequently, accurately forecasting

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
a nation’s medal count at the Olympics is of paramount importance to sports governing bodies and athletes alike.

<!-- b001424 | prose | pages [4] -->
Historically, Olympicmedalprojectionshavelargelyreliedonthefinalathleteroster.However, with globalization and the evolution of sports, numerous unforeseen factors, such as the emer- gence of a great coach or new talent, regional sports culture and home-field advantage can significantly impact medal tallies. Despite these challenges, early predictions are crucial for informed strategic planning and resource allocation within the sporting landscape.

<!-- b001425 | prose | pages [4] -->
1.2 Literature Review

<!-- b001426 | prose | pages [4] -->
The Olympic Games is an international sporting event, the medal tally of which has always been a focal point of attention and analysis. There now exists an extensive body of research pertaining to medal and result projection. For example, Zhang Bo predicted the gold-medal result of women’s shot put in 2012 based on GM(1,1) prediction model in Gray System Theory, a more applicable solution when there is lack of data [1].

<!-- b001427 | prose | pages [4] -->
More methods on the basis of

<!-- b001428 | heading | pages [4] -->
machine learning algorithms were provided by Jhankar Moolchandani et al. [2] including

<!-- b001429 | prose | pages [4] -->
Linear Regression, Random Forest, Support Vector Machines and Neural Networks. They are more useful for forecasting the medal count according to the athlete’s attributes and country information. Among them, Random Forest and SVM stood out. Noviyanti T M Sagala and Muhammad Amien Ibrahim compared XGBoost, LightGBM and CatBoost and found that XGBoost had the highest accuracy [3]. Since Python has numerous libraries that facilitate machine learning tasks, it is convenient for predicting events and medals. XGBoost, which outperforms Random Forest through iterative optimization of trees, can be a reliable choice for our medal ranking prediction.

<!-- b001430 | prose | pages [4] -->
For the prediction of first medal wins, work by Nisreen Osman Abdelsalam et al. on applying Cox proportional hazards models to time-to-event data provided profound inspiration. Similar to survival time, there are numerous factors contributing to the duration of a country going without winning a medal, which can be analyzed by multivariable Cox regression [4].

<!-- b001431 | prose | pages [4] -->
For the problem of Great Coach Effect, we conceptualize differential points to detect the occurrence of the effect. This can be understood through Anomaly Detection. There exist many calculation methods to do so when handling time series data [5]. Yu Qin and YuanSheng Lou used Isolation Forest algorithm to detect the anomaly points of the hydrological time series data, which is more efficient and stable method than traditional ones [6].

<!-- b001432 | prose | pages [4] -->
1.3

<!-- b001433 | heading | pages [4] -->
Problem Restatement

<!-- b001434 | heading | pages [4] -->
1. Data Preparation

<!-- b001435 | prose | pages [4] -->
Preprocessing the 5 datasets about all the history Olympic Games based on appropriate assumptions and decisions for different predictions.

<!-- b001436 | heading | pages [4] -->
2. Model Construction

<!-- b001437 | prose | pages [4] -->
关注数学模型

<!-- b001438 | furniture | pages [4] -->
2

<!-- b001439 | furniture | pages [4] -->
MATHmodels

<!-- b001440 | furniture | pages [4] -->
获取更多资讯

<!-- b001441 | furniture | pages [6] -->
Team # 2514461

<!-- b001442 | furniture | pages [6] -->
Page 5 of 25

<!-- b001443 | heading | pages [6] -->
Assumptions and Justification

<!-- b001444 | prose | pages [6] -->
2

<!-- b001445 | prose | pages [6] -->
• A country’s medal count is only determined by the trend of its performance in past Olympic Games.

<!-- b001446 | prose | pages [6] -->
Abrupt changes caused by external factors such as sudden events are not taken into account.

<!-- b001447 | prose | pages [6] -->
• We attribute all performance improvements exceeding a specific threshold to the coaches.

<!-- b001448 | prose | pages [6] -->
For a country’s Olympic team, improvements within a certain range are attributed to individual athlete performance, while those exceeding this threshold are attributed to additional efforts, specifically the introductions of coaches.

<!-- b001449 | prose | pages [6] -->
• The probabilities of countries that have yet to earn a medal becoming a first-time medalist in a given year are mutually independent.

<!-- b001450 | prose | pages [6] -->
Each country’s performance is influenced by a unique set of factors like athletes and training. Additionally, the outcome of one particular country has little to no bearing on the outcome of another particular country given the multitude of countries participating.

<!-- b001451 | prose | pages [6] -->
• The differences between great coaches from various countries can be neglected.

<!-- b001452 | prose | pages [6] -->
When a coach who moves internationally is considered great, his ability is independent to his nationality.

<!-- b001453 | prose | pages [6] -->
• The impact pattern of a coach on a specific sport is consistent across different nations.

<!-- b001454 | prose | pages [6] -->
The enhancement of athletic performance due to the introduction of a coach is solely historical, meaning that as long as athletes from different countries have the same baseline, the improvement results will be identical.

<!-- b001455 | prose | pages [6] -->
3

<!-- b001456 | heading | pages [6] -->
Notations

<!-- b001457 | heading | pages [6] -->
Symbol

<!-- b001458 | prose | pages [6] -->
Definition N′

<!-- b001459 | prose | pages [6] -->
predicted number of events E N′

<!-- b001460 | prose | pages [6] -->
predicted total number of medals M R′

<!-- b001461 | prose | pages [6] -->
predicted ratio of gold medals G R′

<!-- b001462 | prose | pages [6] -->
predicted ratio of silver medals S R′

<!-- b001463 | prose | pages [6] -->
predicted ratio of bronze medals B P probability of winning the first medal Xa number of athletes Xp number of participations Xe number of events NG number of gold medals NS number of silver medals NB number of bronze medals

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

<!-- b001486 | prose | pages [6] -->
m

<!-- b001487 | prose | pages [6] -->
m

<!-- b001488 | prose | pages [6] -->
m

<!-- b001489 | prose | pages [6] -->
m

<!-- b001490 | prose | pages [6] -->
m

<!-- b001491 | prose | pages [6] -->
m

<!-- b001492 | prose | pages [6] -->
m

<!-- b001493 | prose | pages [6] -->
m

<!-- b001494 | prose | pages [6] -->
m

<!-- b001495 | prose | pages [6] -->
m

<!-- b001496 | prose | pages [6] -->
m

<!-- b001497 | prose | pages [6] -->
m

<!-- b001498 | prose | pages [6] -->
m

<!-- b001499 | prose | pages [6] -->
m

<!-- b001500 | prose | pages [6] -->
m

<!-- b001501 | prose | pages [6] -->
m

<!-- b001502 | prose | pages [6] -->
m

<!-- b001503 | prose | pages [6] -->
m

<!-- b001504 | prose | pages [6] -->
m

<!-- b001505 | prose | pages [6] -->
m

<!-- b001506 | prose | pages [6] -->
m

<!-- b001507 | prose | pages [6] -->
m

<!-- b001508 | prose | pages [6] -->
m

<!-- b001509 | prose | pages [6] -->
m

<!-- b001510 | prose | pages [6] -->
m

<!-- b001511 | prose | pages [6] -->
m

<!-- b001512 | prose | pages [6] -->
m

<!-- b001513 | prose | pages [6] -->
m

<!-- b001514 | prose | pages [6] -->
m

<!-- b001515 | prose | pages [6] -->
m

<!-- b001516 | prose | pages [6] -->
m

<!-- b001517 | prose | pages [6] -->
m

<!-- b001518 | prose | pages [6] -->
m

<!-- b001519 | prose | pages [6] -->
m

<!-- b001520 | prose | pages [6] -->
m

<!-- b001521 | prose | pages [6] -->
m

<!-- b001522 | prose | pages [6] -->
m

<!-- b001523 | prose | pages [6] -->
m

<!-- b001524 | prose | pages [6] -->
m

<!-- b001525 | prose | pages [6] -->
m

<!-- b001526 | prose | pages [6] -->
m

<!-- b001527 | prose | pages [6] -->
m

<!-- b001528 | prose | pages [6] -->
m

<!-- b001529 | prose | pages [6] -->
m

<!-- b001530 | prose | pages [6] -->
m

<!-- b001531 | prose | pages [6] -->
m

<!-- b001532 | prose | pages [6] -->
m

<!-- b001533 | prose | pages [6] -->
m

<!-- b001534 | prose | pages [6] -->
m

<!-- b001535 | prose | pages [6] -->
m

<!-- b001536 | prose | pages [6] -->
m

<!-- b001537 | prose | pages [6] -->
m

<!-- b001538 | prose | pages [6] -->
m

<!-- b001539 | prose | pages [6] -->
m

<!-- b001540 | prose | pages [6] -->
m

<!-- b001541 | prose | pages [6] -->
m

<!-- b001542 | prose | pages [6] -->
m

<!-- b001543 | prose | pages [6] -->
m

<!-- b001544 | prose | pages [6] -->
m

<!-- b001545 | prose | pages [6] -->
m

<!-- b001546 | prose | pages [6] -->
m

<!-- b001547 | prose | pages [6] -->
m

<!-- b001548 | prose | pages [6] -->
m

<!-- b001549 | prose | pages [6] -->
m

<!-- b001550 | prose | pages [6] -->
m

<!-- b001551 | prose | pages [6] -->
m

<!-- b001552 | prose | pages [6] -->
m

<!-- b001553 | prose | pages [6] -->
m

<!-- b001554 | prose | pages [6] -->
m

<!-- b001555 | prose | pages [6] -->
m

<!-- b001556 | prose | pages [6] -->
m

<!-- b001557 | prose | pages [6] -->
m

<!-- b001558 | prose | pages [6] -->
m

<!-- b001559 | prose | pages [6] -->
m

<!-- b001560 | prose | pages [6] -->
m

<!-- b001561 | prose | pages [6] -->
m

<!-- b001562 | prose | pages [6] -->
m

<!-- b001563 | prose | pages [6] -->
m

<!-- b001564 | prose | pages [6] -->
m

<!-- b001565 | prose | pages [6] -->
m

<!-- b001566 | prose | pages [6] -->
m

<!-- b001567 | prose | pages [6] -->
m

<!-- b001568 | prose | pages [6] -->
m

<!-- b001569 | prose | pages [6] -->
m

<!-- b001570 | prose | pages [6] -->
m

<!-- b001571 | prose | pages [6] -->
m

<!-- b001572 | prose | pages [6] -->
m

<!-- b001573 | prose | pages [6] -->
m

<!-- b001574 | prose | pages [6] -->
m

<!-- b001575 | prose | pages [6] -->
m

<!-- b001576 | prose | pages [6] -->
m

<!-- b001577 | prose | pages [6] -->
m

<!-- b001578 | prose | pages [6] -->
m

<!-- b001579 | prose | pages [6] -->
m

<!-- b001580 | prose | pages [6] -->
m

<!-- b001581 | prose | pages [6] -->
m

<!-- b001582 | prose | pages [6] -->
m

<!-- b001583 | prose | pages [6] -->
m

<!-- b001584 | prose | pages [6] -->
m

<!-- b001585 | prose | pages [6] -->
m

<!-- b001586 | prose | pages [6] -->
m

<!-- b001587 | prose | pages [6] -->
m

<!-- b001588 | prose | pages [6] -->
m

<!-- b001589 | prose | pages [6] -->
m

<!-- b001590 | prose | pages [6] -->
m

<!-- b001591 | prose | pages [6] -->
m

<!-- b001592 | prose | pages [6] -->
m

<!-- b001593 | prose | pages [6] -->
m

<!-- b001594 | prose | pages [6] -->
m

<!-- b001595 | prose | pages [6] -->
m

<!-- b001596 | prose | pages [6] -->
m

<!-- b001597 | prose | pages [6] -->
m

<!-- b001598 | prose | pages [6] -->
m

<!-- b001599 | prose | pages [6] -->
m

<!-- b001600 | prose | pages [6] -->
m

<!-- b001601 | prose | pages [6] -->
m

<!-- b001602 | prose | pages [6] -->
m

<!-- b001603 | prose | pages [6] -->
m

<!-- b001604 | prose | pages [6] -->
m

<!-- b001605 | prose | pages [6] -->
m

<!-- b001606 | prose | pages [6] -->
m

<!-- b001607 | prose | pages [6] -->
m

<!-- b001608 | prose | pages [6] -->
m

<!-- b001609 | prose | pages [6] -->
m

<!-- b001610 | prose | pages [6] -->
m

<!-- b001611 | prose | pages [6] -->
m

<!-- b001612 | prose | pages [6] -->
m

<!-- b001613 | prose | pages [6] -->
m

<!-- b001614 | prose | pages [6] -->
m

<!-- b001615 | prose | pages [6] -->
m

<!-- b001616 | prose | pages [6] -->
m

<!-- b001617 | prose | pages [6] -->
m

<!-- b001618 | prose | pages [6] -->
m

<!-- b001619 | prose | pages [6] -->
m

<!-- b001620 | prose | pages [6] -->
m

<!-- b001621 | prose | pages [6] -->
m

<!-- b001622 | prose | pages [6] -->
m

<!-- b001623 | prose | pages [6] -->
m

<!-- b001624 | prose | pages [6] -->
m

<!-- b001625 | prose | pages [6] -->
m

<!-- b001626 | prose | pages [6] -->
m

<!-- b001627 | prose | pages [6] -->
m

<!-- b001628 | prose | pages [6] -->
m

<!-- b001629 | prose | pages [6] -->
m

<!-- b001630 | prose | pages [6] -->
m

<!-- b001631 | heading | pages [6] -->
Symbol

<!-- b001632 | prose | pages [6] -->
Definition

<!-- b001633 | prose | pages [6] -->
m

<!-- b001634 | prose | pages [6] -->
m

<!-- b001635 | prose | pages [6] -->
m

<!-- b001636 | prose | pages [6] -->
m

<!-- b001637 | prose | pages [6] -->
m

<!-- b001638 | prose | pages [6] -->
m

<!-- b001639 | prose | pages [6] -->
m

<!-- b001640 | prose | pages [6] -->
m

<!-- b001641 | prose | pages [6] -->
m

<!-- b001642 | prose | pages [6] -->
m

<!-- b001643 | prose | pages [6] -->
m

<!-- b001644 | prose | pages [6] -->
m

<!-- b001645 | prose | pages [6] -->
m

<!-- b001646 | prose | pages [6] -->
m

<!-- b001647 | prose | pages [6] -->
m

<!-- b001648 | prose | pages [6] -->
m

<!-- b001649 | prose | pages [6] -->
m

<!-- b001650 | prose | pages [6] -->
m

<!-- b001651 | prose | pages [6] -->
m

<!-- b001652 | prose | pages [6] -->
m

<!-- b001653 | prose | pages [6] -->
m

<!-- b001654 | prose | pages [6] -->
m

<!-- b001655 | prose | pages [6] -->
m

<!-- b001656 | prose | pages [6] -->
m

<!-- b001657 | prose | pages [6] -->
m

<!-- b001658 | prose | pages [6] -->
m

<!-- b001659 | prose | pages [6] -->
m

<!-- b001660 | prose | pages [6] -->
m

<!-- b001661 | prose | pages [6] -->
m

<!-- b001662 | prose | pages [6] -->
m

<!-- b001663 | prose | pages [6] -->
m

<!-- b001664 | prose | pages [6] -->
m

<!-- b001665 | prose | pages [6] -->
m

<!-- b001666 | prose | pages [6] -->
m

<!-- b001667 | prose | pages [6] -->
m

<!-- b001668 | prose | pages [6] -->
m

<!-- b001669 | prose | pages [6] -->
m

<!-- b001670 | prose | pages [6] -->
m

<!-- b001671 | prose | pages [6] -->
m

<!-- b001672 | prose | pages [6] -->
m

<!-- b001673 | prose | pages [6] -->
m

<!-- b001674 | prose | pages [6] -->
m

<!-- b001675 | prose | pages [6] -->
m

<!-- b001676 | prose | pages [6] -->
m

<!-- b001677 | prose | pages [6] -->
m

<!-- b001678 | prose | pages [6] -->
m

<!-- b001679 | prose | pages [6] -->
m

<!-- b001680 | prose | pages [6] -->
m

<!-- b001681 | prose | pages [6] -->
m

<!-- b001682 | prose | pages [6] -->
m

<!-- b001683 | prose | pages [6] -->
m

<!-- b001684 | prose | pages [6] -->
m

<!-- b001685 | prose | pages [6] -->
m

<!-- b001686 | prose | pages [6] -->
m

<!-- b001687 | prose | pages [6] -->
m

<!-- b001688 | prose | pages [6] -->
m

<!-- b001689 | prose | pages [6] -->
m

<!-- b001690 | prose | pages [6] -->
m

<!-- b001691 | prose | pages [6] -->
m

<!-- b001692 | prose | pages [6] -->
m

<!-- b001693 | prose | pages [6] -->
m

<!-- b001694 | prose | pages [6] -->
m

<!-- b001695 | prose | pages [6] -->
m

<!-- b001696 | prose | pages [6] -->
m

<!-- b001697 | prose | pages [6] -->
m

<!-- b001698 | prose | pages [6] -->
m

<!-- b001699 | prose | pages [6] -->
m

<!-- b001700 | prose | pages [6] -->
m

<!-- b001701 | prose | pages [6] -->
m

<!-- b001702 | prose | pages [6] -->
m

<!-- b001703 | prose | pages [6] -->
m

<!-- b001704 | prose | pages [6] -->
m

<!-- b001705 | prose | pages [6] -->
m

<!-- b001706 | prose | pages [6] -->
m

<!-- b001707 | prose | pages [6] -->
m

<!-- b001708 | prose | pages [6] -->
m

<!-- b001709 | prose | pages [6] -->
m

<!-- b001710 | prose | pages [6] -->
m

<!-- b001711 | prose | pages [6] -->
m

<!-- b001712 | prose | pages [6] -->
m

<!-- b001713 | prose | pages [6] -->
m

<!-- b001714 | prose | pages [6] -->
m

<!-- b001715 | prose | pages [6] -->
m

<!-- b001716 | prose | pages [6] -->
m

<!-- b001717 | prose | pages [6] -->
m

<!-- b001718 | prose | pages [6] -->
m

<!-- b001719 | prose | pages [6] -->
m

<!-- b001720 | prose | pages [6] -->
m

<!-- b001721 | prose | pages [6] -->
m

<!-- b001722 | prose | pages [6] -->
m

<!-- b001723 | prose | pages [6] -->
m

<!-- b001724 | prose | pages [6] -->
m

<!-- b001725 | prose | pages [6] -->
m

<!-- b001726 | prose | pages [6] -->
m

<!-- b001727 | prose | pages [6] -->
m

<!-- b001728 | prose | pages [6] -->
m

<!-- b001729 | prose | pages [6] -->
m

<!-- b001730 | prose | pages [6] -->
m

<!-- b001731 | prose | pages [6] -->
m

<!-- b001732 | prose | pages [6] -->
m

<!-- b001733 | prose | pages [6] -->
m

<!-- b001734 | prose | pages [6] -->
m

<!-- b001735 | prose | pages [6] -->
m

<!-- b001736 | prose | pages [6] -->
m

<!-- b001737 | prose | pages [6] -->
m

<!-- b001738 | prose | pages [6] -->
m

<!-- b001739 | prose | pages [6] -->
m

<!-- b001740 | prose | pages [6] -->
m

<!-- b001741 | prose | pages [6] -->
m

<!-- b001742 | prose | pages [6] -->
m

<!-- b001743 | prose | pages [6] -->
m

<!-- b001744 | prose | pages [6] -->
m

<!-- b001745 | prose | pages [6] -->
m

<!-- b001746 | prose | pages [6] -->
m

<!-- b001747 | prose | pages [6] -->
m

<!-- b001748 | prose | pages [6] -->
m

<!-- b001749 | prose | pages [6] -->
m

<!-- b001750 | prose | pages [6] -->
m

<!-- b001751 | prose | pages [6] -->
m

<!-- b001752 | prose | pages [6] -->
m

<!-- b001753 | prose | pages [6] -->
m

<!-- b001754 | prose | pages [6] -->
m

<!-- b001755 | prose | pages [6] -->
m

<!-- b001756 | prose | pages [6] -->
m

<!-- b001757 | prose | pages [6] -->
m

<!-- b001758 | prose | pages [6] -->
m

<!-- b001759 | prose | pages [6] -->
m

<!-- b001760 | prose | pages [6] -->
m

<!-- b001761 | prose | pages [6] -->
m

<!-- b001762 | prose | pages [6] -->
ωG

<!-- b001763 | prose | pages [6] -->
m

<!-- b001764 | prose | pages [6] -->
m

<!-- b001765 | prose | pages [6] -->
m

<!-- b001766 | prose | pages [6] -->
m

<!-- b001767 | prose | pages [6] -->
m

<!-- b001768 | prose | pages [6] -->
m

<!-- b001769 | prose | pages [6] -->
m

<!-- b001770 | prose | pages [6] -->
m

<!-- b001771 | prose | pages [6] -->
m

<!-- b001772 | prose | pages [6] -->
m

<!-- b001773 | prose | pages [6] -->
m

<!-- b001774 | prose | pages [6] -->
m

<!-- b001775 | prose | pages [6] -->
m

<!-- b001776 | prose | pages [6] -->
m

<!-- b001777 | prose | pages [6] -->
weight of gold medal

<!-- b001778 | prose | pages [6] -->
m

<!-- b001779 | prose | pages [6] -->
m

<!-- b001780 | prose | pages [6] -->
m

<!-- b001781 | prose | pages [6] -->
m

<!-- b001782 | prose | pages [6] -->
m

<!-- b001783 | prose | pages [6] -->
m

<!-- b001784 | prose | pages [6] -->
m

<!-- b001785 | prose | pages [6] -->
m

<!-- b001786 | prose | pages [6] -->
m

<!-- b001787 | prose | pages [6] -->
m

<!-- b001788 | prose | pages [6] -->
m

<!-- b001789 | prose | pages [6] -->
m

<!-- b001790 | prose | pages [6] -->
m

<!-- b001791 | prose | pages [6] -->
m

<!-- b001792 | prose | pages [6] -->
m

<!-- b001793 | prose | pages [6] -->
m

<!-- b001794 | prose | pages [6] -->
m

<!-- b001795 | prose | pages [6] -->
m

<!-- b001796 | prose | pages [6] -->
m

<!-- b001797 | prose | pages [6] -->
m

<!-- b001798 | prose | pages [6] -->
m

<!-- b001799 | prose | pages [6] -->
m

<!-- b001800 | prose | pages [6] -->
m

<!-- b001801 | prose | pages [6] -->
m

<!-- b001802 | prose | pages [6] -->
m

<!-- b001803 | prose | pages [6] -->
m

<!-- b001804 | prose | pages [6] -->
m

<!-- b001805 | prose | pages [6] -->
m

<!-- b001806 | prose | pages [6] -->
m

<!-- b001807 | prose | pages [6] -->
m

<!-- b001808 | prose | pages [6] -->
m

<!-- b001809 | prose | pages [6] -->
m

<!-- b001810 | prose | pages [6] -->
m

<!-- b001811 | prose | pages [6] -->
m

<!-- b001812 | prose | pages [6] -->
m

<!-- b001813 | prose | pages [6] -->
m

<!-- b001814 | prose | pages [6] -->
m

<!-- b001815 | prose | pages [6] -->
m

<!-- b001816 | prose | pages [6] -->
m

<!-- b001817 | prose | pages [6] -->
m

<!-- b001818 | prose | pages [6] -->
m

<!-- b001819 | prose | pages [6] -->
m

<!-- b001820 | prose | pages [6] -->
m

<!-- b001821 | prose | pages [6] -->
m

<!-- b001822 | prose | pages [6] -->
m

<!-- b001823 | prose | pages [6] -->
m

<!-- b001824 | prose | pages [6] -->
m

<!-- b001825 | prose | pages [6] -->
m

<!-- b001826 | prose | pages [6] -->
m

<!-- b001827 | prose | pages [6] -->
m

<!-- b001828 | prose | pages [6] -->
m

<!-- b001829 | prose | pages [6] -->
m

<!-- b001830 | prose | pages [6] -->
m

<!-- b001831 | prose | pages [6] -->
m

<!-- b001832 | prose | pages [6] -->
m

<!-- b001833 | prose | pages [6] -->
m

<!-- b001834 | prose | pages [6] -->
m

<!-- b001835 | prose | pages [6] -->
m

<!-- b001836 | prose | pages [6] -->
m

<!-- b001837 | prose | pages [6] -->
m

<!-- b001838 | prose | pages [6] -->
m

<!-- b001839 | prose | pages [6] -->
m

<!-- b001840 | prose | pages [6] -->
m

<!-- b001841 | prose | pages [6] -->
m

<!-- b001842 | prose | pages [6] -->
m

<!-- b001843 | prose | pages [6] -->
m

<!-- b001844 | prose | pages [6] -->
m

<!-- b001845 | prose | pages [6] -->
m

<!-- b001846 | prose | pages [6] -->
m

<!-- b001847 | prose | pages [6] -->
m

<!-- b001848 | prose | pages [6] -->
m

<!-- b001849 | prose | pages [6] -->
m

<!-- b001850 | prose | pages [6] -->
m

<!-- b001851 | prose | pages [6] -->
m

<!-- b001852 | prose | pages [6] -->
m

<!-- b001853 | prose | pages [6] -->
m

<!-- b001854 | prose | pages [6] -->
m

<!-- b001855 | prose | pages [6] -->
m

<!-- b001856 | prose | pages [6] -->
m

<!-- b001857 | prose | pages [6] -->
m

<!-- b001858 | prose | pages [6] -->
m

<!-- b001859 | prose | pages [6] -->
m

<!-- b001860 | prose | pages [6] -->
m

<!-- b001861 | prose | pages [6] -->
m

<!-- b001862 | prose | pages [6] -->
m

<!-- b001863 | prose | pages [6] -->
m

<!-- b001864 | prose | pages [6] -->
m

<!-- b001865 | prose | pages [6] -->
m

<!-- b001866 | prose | pages [6] -->
m

<!-- b001867 | prose | pages [6] -->
m

<!-- b001868 | prose | pages [6] -->
m

<!-- b001869 | prose | pages [6] -->
m

<!-- b001870 | prose | pages [6] -->
m

<!-- b001871 | prose | pages [6] -->
m

<!-- b001872 | prose | pages [6] -->
m

<!-- b001873 | prose | pages [6] -->
m

<!-- b001874 | prose | pages [6] -->
m

<!-- b001875 | prose | pages [6] -->
m

<!-- b001876 | prose | pages [6] -->
m

<!-- b001877 | prose | pages [6] -->
m

<!-- b001878 | prose | pages [6] -->
m

<!-- b001879 | prose | pages [6] -->
m

<!-- b001880 | prose | pages [6] -->
m

<!-- b001881 | prose | pages [6] -->
m

<!-- b001882 | prose | pages [6] -->
m

<!-- b001883 | prose | pages [6] -->
m

<!-- b001884 | prose | pages [6] -->
m

<!-- b001885 | prose | pages [6] -->
m

<!-- b001886 | prose | pages [6] -->
m

<!-- b001887 | prose | pages [6] -->
m

<!-- b001888 | prose | pages [6] -->
m

<!-- b001889 | prose | pages [6] -->
m

<!-- b001890 | prose | pages [6] -->
m

<!-- b001891 | prose | pages [6] -->
m

<!-- b001892 | prose | pages [6] -->
m

<!-- b001893 | prose | pages [6] -->
m

<!-- b001894 | prose | pages [6] -->
m

<!-- b001895 | prose | pages [6] -->
m

<!-- b001896 | prose | pages [6] -->
m

<!-- b001897 | prose | pages [6] -->
m

<!-- b001898 | prose | pages [6] -->
m

<!-- b001899 | prose | pages [6] -->
m

<!-- b001900 | prose | pages [6] -->
m

<!-- b001901 | prose | pages [6] -->
m

<!-- b001902 | prose | pages [6] -->
m

<!-- b001903 | prose | pages [6] -->
m

<!-- b001904 | prose | pages [6] -->
m

<!-- b001905 | prose | pages [6] -->
m

<!-- b001906 | prose | pages [6] -->
m

<!-- b001907 | prose | pages [6] -->
m

<!-- b001908 | prose | pages [6] -->
m

<!-- b001909 | prose | pages [6] -->
m

<!-- b001910 | prose | pages [6] -->
m

<!-- b001911 | prose | pages [6] -->
m

<!-- b001912 | prose | pages [6] -->
m

<!-- b001913 | prose | pages [6] -->
ωS weight of silver medal

<!-- b001914 | prose | pages [6] -->
m

<!-- b001915 | prose | pages [6] -->
m

<!-- b001916 | prose | pages [6] -->
m

<!-- b001917 | prose | pages [6] -->
m

<!-- b001918 | prose | pages [6] -->
m

<!-- b001919 | prose | pages [6] -->
m

<!-- b001920 | prose | pages [6] -->
m

<!-- b001921 | prose | pages [6] -->
m

<!-- b001922 | prose | pages [6] -->
m

<!-- b001923 | prose | pages [6] -->
m

<!-- b001924 | prose | pages [6] -->
m

<!-- b001925 | prose | pages [6] -->
m

<!-- b001926 | prose | pages [6] -->
m

<!-- b001927 | prose | pages [6] -->
m

<!-- b001928 | prose | pages [6] -->
m

<!-- b001929 | prose | pages [6] -->
m

<!-- b001930 | prose | pages [6] -->
m

<!-- b001931 | prose | pages [6] -->
m

<!-- b001932 | prose | pages [6] -->
m

<!-- b001933 | prose | pages [6] -->
m

<!-- b001934 | prose | pages [6] -->
m

<!-- b001935 | prose | pages [6] -->
m

<!-- b001936 | prose | pages [6] -->
m

<!-- b001937 | prose | pages [6] -->
m

<!-- b001938 | prose | pages [6] -->
m

<!-- b001939 | prose | pages [6] -->
m

<!-- b001940 | prose | pages [6] -->
m

<!-- b001941 | prose | pages [6] -->
m

<!-- b001942 | prose | pages [6] -->
m

<!-- b001943 | prose | pages [6] -->
m

<!-- b001944 | prose | pages [6] -->
m

<!-- b001945 | prose | pages [6] -->
m

<!-- b001946 | prose | pages [6] -->
m

<!-- b001947 | prose | pages [6] -->
m

<!-- b001948 | prose | pages [6] -->
m

<!-- b001949 | prose | pages [6] -->
m

<!-- b001950 | prose | pages [6] -->
m

<!-- b001951 | prose | pages [6] -->
m

<!-- b001952 | prose | pages [6] -->
m

<!-- b001953 | prose | pages [6] -->
m

<!-- b001954 | prose | pages [6] -->
m

<!-- b001955 | prose | pages [6] -->
m

<!-- b001956 | prose | pages [6] -->
m

<!-- b001957 | prose | pages [6] -->
m

<!-- b001958 | prose | pages [6] -->
m

<!-- b001959 | prose | pages [6] -->
m

<!-- b001960 | prose | pages [6] -->
m

<!-- b001961 | prose | pages [6] -->
m

<!-- b001962 | prose | pages [6] -->
m

<!-- b001963 | prose | pages [6] -->
m

<!-- b001964 | prose | pages [6] -->
m

<!-- b001965 | prose | pages [6] -->
m

<!-- b001966 | prose | pages [6] -->
m

<!-- b001967 | prose | pages [6] -->
m

<!-- b001968 | prose | pages [6] -->
m

<!-- b001969 | prose | pages [6] -->
m

<!-- b001970 | prose | pages [6] -->
m

<!-- b001971 | prose | pages [6] -->
m

<!-- b001972 | prose | pages [6] -->
m

<!-- b001973 | prose | pages [6] -->
m

<!-- b001974 | prose | pages [6] -->
m

<!-- b001975 | prose | pages [6] -->
m

<!-- b001976 | prose | pages [6] -->
m

<!-- b001977 | prose | pages [6] -->
m

<!-- b001978 | prose | pages [6] -->
m

<!-- b001979 | prose | pages [6] -->
m

<!-- b001980 | prose | pages [6] -->
m

<!-- b001981 | prose | pages [6] -->
m

<!-- b001982 | prose | pages [6] -->
m

<!-- b001983 | prose | pages [6] -->
m

<!-- b001984 | prose | pages [6] -->
m

<!-- b001985 | prose | pages [6] -->
m

<!-- b001986 | prose | pages [6] -->
m

<!-- b001987 | prose | pages [6] -->
m

<!-- b001988 | prose | pages [6] -->
m

<!-- b001989 | prose | pages [6] -->
m

<!-- b001990 | prose | pages [6] -->
m

<!-- b001991 | prose | pages [6] -->
m

<!-- b001992 | prose | pages [6] -->
m

<!-- b001993 | prose | pages [6] -->
m

<!-- b001994 | prose | pages [6] -->
m

<!-- b001995 | prose | pages [6] -->
m

<!-- b001996 | prose | pages [6] -->
m

<!-- b001997 | prose | pages [6] -->
m

<!-- b001998 | prose | pages [6] -->
m

<!-- b001999 | prose | pages [6] -->
m

<!-- b002000 | prose | pages [6] -->
m

<!-- b002001 | prose | pages [6] -->
m

<!-- b002002 | prose | pages [6] -->
m

<!-- b002003 | prose | pages [6] -->
m

<!-- b002004 | prose | pages [6] -->
m

<!-- b002005 | prose | pages [6] -->
m

<!-- b002006 | prose | pages [6] -->
m

<!-- b002007 | prose | pages [6] -->
m

<!-- b002008 | prose | pages [6] -->
m

<!-- b002009 | prose | pages [6] -->
m

<!-- b002010 | prose | pages [6] -->
m

<!-- b002011 | prose | pages [6] -->
m

<!-- b002012 | prose | pages [6] -->
m

<!-- b002013 | prose | pages [6] -->
m

<!-- b002014 | prose | pages [6] -->
m

<!-- b002015 | prose | pages [6] -->
m

<!-- b002016 | prose | pages [6] -->
m

<!-- b002017 | prose | pages [6] -->
m

<!-- b002018 | prose | pages [6] -->
m

<!-- b002019 | prose | pages [6] -->
m

<!-- b002020 | prose | pages [6] -->
m

<!-- b002021 | prose | pages [6] -->
m

<!-- b002022 | prose | pages [6] -->
m

<!-- b002023 | prose | pages [6] -->
m

<!-- b002024 | prose | pages [6] -->
m

<!-- b002025 | prose | pages [6] -->
m

<!-- b002026 | prose | pages [6] -->
m

<!-- b002027 | prose | pages [6] -->
m

<!-- b002028 | prose | pages [6] -->
m

<!-- b002029 | prose | pages [6] -->
m

<!-- b002030 | prose | pages [6] -->
m

<!-- b002031 | prose | pages [6] -->
m

<!-- b002032 | prose | pages [6] -->
m

<!-- b002033 | prose | pages [6] -->
m

<!-- b002034 | prose | pages [6] -->
m

<!-- b002035 | prose | pages [6] -->
ωB weight of bronze medal

<!-- b002036 | prose | pages [6] -->
m

<!-- b002037 | prose | pages [6] -->
m

<!-- b002038 | prose | pages [6] -->
m

<!-- b002039 | prose | pages [6] -->
m

<!-- b002040 | prose | pages [6] -->
m

<!-- b002041 | prose | pages [6] -->
m

<!-- b002042 | prose | pages [6] -->
m

<!-- b002043 | prose | pages [6] -->
m

<!-- b002044 | prose | pages [6] -->
m

<!-- b002045 | prose | pages [6] -->
m

<!-- b002046 | prose | pages [6] -->
m

<!-- b002047 | prose | pages [6] -->
m

<!-- b002048 | prose | pages [6] -->
m

<!-- b002049 | prose | pages [6] -->
m

<!-- b002050 | prose | pages [6] -->
m

<!-- b002051 | prose | pages [6] -->
m

<!-- b002052 | prose | pages [6] -->
m

<!-- b002053 | prose | pages [6] -->
m

<!-- b002054 | prose | pages [6] -->
m

<!-- b002055 | prose | pages [6] -->
m

<!-- b002056 | prose | pages [6] -->
m

<!-- b002057 | prose | pages [6] -->
m

<!-- b002058 | prose | pages [6] -->
m

<!-- b002059 | prose | pages [6] -->
m

<!-- b002060 | prose | pages [6] -->
m

<!-- b002061 | prose | pages [6] -->
m

<!-- b002062 | prose | pages [6] -->
m

<!-- b002063 | prose | pages [6] -->
m

<!-- b002064 | prose | pages [6] -->
m

<!-- b002065 | prose | pages [6] -->
m

<!-- b002066 | prose | pages [6] -->
m

<!-- b002067 | prose | pages [6] -->
m

<!-- b002068 | prose | pages [6] -->
m

<!-- b002069 | prose | pages [6] -->
m

<!-- b002070 | prose | pages [6] -->
m

<!-- b002071 | prose | pages [6] -->
m

<!-- b002072 | prose | pages [6] -->
m

<!-- b002073 | prose | pages [6] -->
m

<!-- b002074 | prose | pages [6] -->
m

<!-- b002075 | prose | pages [6] -->
m

<!-- b002076 | prose | pages [6] -->
m

<!-- b002077 | prose | pages [6] -->
m

<!-- b002078 | prose | pages [6] -->
m

<!-- b002079 | prose | pages [6] -->
m

<!-- b002080 | prose | pages [6] -->
m

<!-- b002081 | prose | pages [6] -->
m

<!-- b002082 | prose | pages [6] -->
m

<!-- b002083 | prose | pages [6] -->
m

<!-- b002084 | prose | pages [6] -->
m

<!-- b002085 | prose | pages [6] -->
m

<!-- b002086 | prose | pages [6] -->
m

<!-- b002087 | prose | pages [6] -->
m

<!-- b002088 | prose | pages [6] -->
m

<!-- b002089 | prose | pages [6] -->
m

<!-- b002090 | prose | pages [6] -->
m

<!-- b002091 | prose | pages [6] -->
m

<!-- b002092 | prose | pages [6] -->
m

<!-- b002093 | prose | pages [6] -->
m

<!-- b002094 | prose | pages [6] -->
m

<!-- b002095 | prose | pages [6] -->
m

<!-- b002096 | prose | pages [6] -->
m

<!-- b002097 | prose | pages [6] -->
m

<!-- b002098 | prose | pages [6] -->
m

<!-- b002099 | prose | pages [6] -->
m

<!-- b002100 | prose | pages [6] -->
m

<!-- b002101 | prose | pages [6] -->
m

<!-- b002102 | prose | pages [6] -->
m

<!-- b002103 | prose | pages [6] -->
m

<!-- b002104 | prose | pages [6] -->
m

<!-- b002105 | prose | pages [6] -->
m

<!-- b002106 | prose | pages [6] -->
m

<!-- b002107 | prose | pages [6] -->
m

<!-- b002108 | prose | pages [6] -->
m

<!-- b002109 | prose | pages [6] -->
m

<!-- b002110 | prose | pages [6] -->
m

<!-- b002111 | prose | pages [6] -->
m

<!-- b002112 | prose | pages [6] -->
m

<!-- b002113 | prose | pages [6] -->
m

<!-- b002114 | prose | pages [6] -->
m

<!-- b002115 | prose | pages [6] -->
m

<!-- b002116 | prose | pages [6] -->
m

<!-- b002117 | prose | pages [6] -->
m

<!-- b002118 | prose | pages [6] -->
m

<!-- b002119 | prose | pages [6] -->
m

<!-- b002120 | prose | pages [6] -->
m

<!-- b002121 | prose | pages [6] -->
m

<!-- b002122 | prose | pages [6] -->
m

<!-- b002123 | prose | pages [6] -->
m

<!-- b002124 | prose | pages [6] -->
m

<!-- b002125 | prose | pages [6] -->
m

<!-- b002126 | prose | pages [6] -->
m

<!-- b002127 | prose | pages [6] -->
m

<!-- b002128 | prose | pages [6] -->
m

<!-- b002129 | prose | pages [6] -->
m

<!-- b002130 | prose | pages [6] -->
m

<!-- b002131 | prose | pages [6] -->
m

<!-- b002132 | prose | pages [6] -->
m

<!-- b002133 | prose | pages [6] -->
m

<!-- b002134 | prose | pages [6] -->
m

<!-- b002135 | prose | pages [6] -->
m

<!-- b002136 | prose | pages [6] -->
m

<!-- b002137 | prose | pages [6] -->
m

<!-- b002138 | prose | pages [6] -->
m

<!-- b002139 | prose | pages [6] -->
m

<!-- b002140 | prose | pages [6] -->
m

<!-- b002141 | prose | pages [6] -->
m

<!-- b002142 | prose | pages [6] -->
m

<!-- b002143 | prose | pages [6] -->
m

<!-- b002144 | prose | pages [6] -->
m

<!-- b002145 | prose | pages [6] -->
m

<!-- b002146 | prose | pages [6] -->
m

<!-- b002147 | prose | pages [6] -->
m

<!-- b002148 | prose | pages [6] -->
m

<!-- b002149 | prose | pages [6] -->
m

<!-- b002150 | prose | pages [6] -->
m

<!-- b002151 | prose | pages [6] -->
m

<!-- b002152 | prose | pages [6] -->
m

<!-- b002153 | prose | pages [6] -->
m

<!-- b002154 | prose | pages [6] -->
m

<!-- b002155 | prose | pages [6] -->
m

<!-- b002156 | prose | pages [6] -->
m

<!-- b002157 | prose | pages [6] -->
S score

<!-- b002158 | prose | pages [6] -->
△S first-order difference of score γS first-order ratio of score threshold of △S ST△ STγ threshold of γS Contribution Factor at the ith Games Ci Is Influence Factor of sport s score at the ith Games Si score of sport j at the ith Games. Sij

<!-- b002159 | prose | pages [6] -->
关注数学模型

<!-- b002160 | furniture | pages [6] -->
2

<!-- b002161 | furniture | pages [6] -->
MATHmodels

<!-- b002162 | furniture | pages [6] -->
获取更多资讯

<!-- b002163 | furniture | pages [8] -->
Team # 2514461

<!-- b002164 | furniture | pages [8] -->
Page 7 of 25

<!-- b002165 | prose | pages [8] -->
We conductedregressionanalysisonthenumberofpasteventsinsummerOly_programs.csv to predict the event count in certain discipline for the 2028 Olympics. The modeling steps are shown in Fig. 1. For each discipline, a time series of event counts was constructed, saved as a two-dimensional array. This series was divided into training and testing sets in an 8:2 ratio and subsequently standardized. An SVR model wass instantiated and its hyperparameters tuned via Grid Search coupled with 5-fold Cross-Validation. The trained model was then employed to predict future event counts.

<!-- b002166 | prose | pages [8] -->
4.3

<!-- b002167 | heading | pages [8] -->
Results

<!-- b002168 | prose | pages [8] -->
Taking artistic gymnastics as an example, the SVR model predicted 14 events in 2028, with a mean squared error(MSE) of 1.744 and an R-squared value of 0.634 as shown in Fig. 2. This relatively high error is due to significant fluctuations in the number of events for this discipline in early years. Despite this, this SVR model performs well when predicting disciplines with a more stable number of events in recent years.

<!-- b002169 | prose | pages [8] -->
Ultimately, We can roll up the results to determine the overall event count for each sport. They are shown in table 1.

<!-- b002170 | caption | pages [8] -->
Figure 2: Event count prediction of artistic gymnastics

<!-- b002171 | caption | pages [8] -->
Figure 1:

<!-- b002172 | prose | pages [8] -->
Flow chart of event count prediction

<!-- b002173 | prose | pages [8] -->
关注数学模型

<!-- b002174 | furniture | pages [8] -->
2

<!-- b002175 | furniture | pages [8] -->
MATHmodels

<!-- b002176 | furniture | pages [8] -->
获取更多资讯

<!-- b002177 | furniture | pages [9] -->
Team # 2514461

<!-- b002178 | furniture | pages [9] -->
Page 8 of 25

<!-- b002179 | caption | pages [9] -->
Table 1: Predicted event count in 2028 Olympics

<!-- b002180 | prose | pages [9] -->
Sport Discipline Code Discipline Event Sport Event

<!-- b002181 | prose | pages [9] -->
Artistic Swimming SWA 2

<!-- b002182 | prose | pages [9] -->
Diving DIV 8

<!-- b002183 | prose | pages [9] -->
Aquatics

<!-- b002184 | prose | pages [9] -->
Marathon Swimming OWS 2 49 Swimming SWM 35 Water Polo WPO 2

<!-- b002185 | prose | pages [9] -->
Archery Archery ARC 5 5

<!-- b002186 | prose | pages [9] -->
Athletics Athletics ATH 48 48

<!-- b002187 | prose | pages [9] -->
Badminton Badminton BDM 6 6

<!-- b002188 | prose | pages [9] -->
Baseball BSB 1 Baseball and Softball 2

<!-- b002189 | prose | pages [9] -->
Sport Discipline Code Discipline Event Sport Event

<!-- b002190 | prose | pages [9] -->
Indoor HBL 2 Handball 2 Field HBL 0

<!-- b002191 | prose | pages [9] -->
Jeu de Paume Jeu de Paume 0 0

<!-- b002192 | prose | pages [9] -->
Judo Judo JUD 16 16

<!-- b002193 | prose | pages [9] -->
Karate Karate KTE 0 0

<!-- b002194 | prose | pages [9] -->
Sixes LAX 0 Lacrosse 0 Field LAX 0

<!-- b002195 | prose | pages [9] -->
Modern Pentathlon MPN 2 2

<!-- b002196 | prose | pages [9] -->
微信公众号：数学模型

<!-- b002197 | prose | pages [9] -->
Softball SBL 1

<!-- b002198 | prose | pages [9] -->
3x3 BK3 1 Basketball 3 Basketball BKB 2

<!-- b002199 | prose | pages [9] -->
Basque Pelota Basque Pelota PEL 0 0

<!-- b002200 | prose | pages [9] -->
Boxing Boxing BOX 13 13

<!-- b002201 | prose | pages [9] -->
Breaking Breaking BKG 0 0

<!-- b002202 | prose | pages [9] -->
Sprint CSP 11 Canoeing 16 Slalom CSL 5

<!-- b002203 | prose | pages [9] -->
Cricket Cricket CKT 0 0

<!-- b002204 | prose | pages [9] -->
Croquet Croquet CQT 0 0

<!-- b002205 | prose | pages [9] -->
BMX Freestyle BMF 1

<!-- b002206 | prose | pages [9] -->
BMX Racing BMX 2

<!-- b002207 | prose | pages [9] -->
Cycling

<!-- b002208 | prose | pages [9] -->
Mountain Bike MTB 2 21 Road CRD 4

<!-- b002209 | prose | pages [9] -->
Polo Polo POL 0 0

<!-- b002210 | prose | pages [9] -->
Rackets Rackets RQT 0 0

<!-- b002211 | prose | pages [9] -->
Roque Roque 0 0

<!-- b002212 | prose | pages [9] -->
Coastal ROC 0 Rowing 14 Rowing ROW 14

<!-- b002213 | prose | pages [9] -->
Sevens RU7 1 Rugby 0 Union RUG 0

<!-- b002214 | prose | pages [9] -->
Sailing Sailing SAL 10 10

<!-- b002215 | prose | pages [9] -->
Shooting Shooting SHO 15 15

<!-- b002216 | prose | pages [9] -->
Skateboarding Skateboarding SKB 0 0

<!-- b002217 | prose | pages [9] -->
Sport Climbing Sport Climbing CLB 2 2

<!-- b002218 | prose | pages [9] -->
Squash Squash SQU 0 0

<!-- b002219 | prose | pages [9] -->
微信号：MATHmodels

<!-- b002220 | prose | pages [9] -->
Track CTR 12

<!-- b002221 | prose | pages [9] -->
Dressage EDR 2

<!-- b002222 | prose | pages [9] -->
Eventing EVE 2

<!-- b002223 | prose | pages [9] -->
Equestrian

<!-- b002224 | prose | pages [9] -->
6 Jumping EJP 2 Vaulting EVL 0

<!-- b002225 | prose | pages [9] -->
Fencing Fencing FEN 11 11

<!-- b002226 | prose | pages [9] -->
Field hockey Field hockey HOC 2 2

<!-- b002227 | prose | pages [9] -->
Flag football Flag football AFB 0 0

<!-- b002228 | prose | pages [9] -->
Football Football FBL 2 2

<!-- b002229 | prose | pages [9] -->
Golf Golf GLF 1 1

<!-- b002230 | prose | pages [9] -->
Artistic GAR 14

<!-- b002231 | prose | pages [9] -->
Gymnastics

<!-- b002232 | prose | pages [9] -->
Rhythmic GRY 2 18 Trampoline GTR 2

<!-- b002233 | prose | pages [9] -->
Surfing Surfing SRF 0 0

<!-- b002234 | prose | pages [9] -->
Table Tennis Table Tennis TTE 5 5

<!-- b002235 | prose | pages [9] -->
Taekwondo Taekwondo TKW 8 8

<!-- b002236 | prose | pages [9] -->
Tennis Tennis TEN 6 6

<!-- b002237 | prose | pages [9] -->
Triathlon Triathlon TRI 3 3

<!-- b002238 | prose | pages [9] -->
Tug of War Tug of War TOW 0 0

<!-- b002239 | prose | pages [9] -->
Beach VBV 2 Volleyball 4 Indoor VVO 2

<!-- b002240 | prose | pages [9] -->
Water Motorsports PBT 0 0

<!-- b002241 | prose | pages [9] -->
Weightlifting Weightlifting WLF 16 16

<!-- b002242 | prose | pages [9] -->
Freestyle WRF 12 Wrestling 18 Greco-Roman WRG 6

<!-- b002243 | prose | pages [9] -->
Analysis of the importance of different sports 4.4

<!-- b002244 | prose | pages [9] -->
Firstly, we quantified a country’s performance in a specific sport at a certain Games as score S, which is the sum of gold, silver and bronze medal counts NG, NS and NB assigned with different weights ωG, ωS and ωB.

<!-- b002245 | prose | pages [9] -->
S = NGωG + NSωS + NBωB

<!-- b002246 | prose | pages [9] -->
For the sake of simplicity, we let

<!-- b002247 | prose | pages [9] -->
(7)

<!-- b002248 | prose | pages [9] -->
ωS = 2, ωG = 3, ωB = 1.

<!-- b002249 | prose | pages [9] -->
(8)

<!-- b002250 | prose | pages [9] -->
We calculated the proportion of scores in various sports for different countries in 2024 relative to their total scores, to measure the significance of different sports to each country. We

<!-- b002251 | furniture | pages [10] -->
Team # 2514461

<!-- b002252 | furniture | pages [10] -->
Page 9 of 25

<!-- b002253 | caption | pages [10] -->
Figure 3: The score percentage of various sports for different countries at the 2024 Olympic

<!-- b002254 | prose | pages [10] -->
Games

<!-- b002255 | prose | pages [10] -->
assumed that the higher the proportion of a sport in a country, the more important that sport is to that country.

<!-- b002256 | prose | pages [10] -->
From Fig. 3, it can be seen that for the United States, Athletics and Aquatics have the largest proportions and are the most significant; for China, Japan, and the United Kingdom, Aquatics, Wrestling, and Aquatics are the most important, respectively.

<!-- b002257 | heading | pages [10] -->
Model II : Medal Prediction based on LSTM and XGBoost

<!-- b002258 | prose | pages [10] -->
5

<!-- b002259 | prose | pages [10] -->
5.1

<!-- b002260 | heading | pages [10] -->
Model Overview

<!-- b002261 | prose | pages [10] -->
To capture the intricate relationship between a country’s medal count and the specific disciplines, we first tallied the gold, silver and bronze medals won by each country in each discipline every year, then divided by the total number of medals awarded in that discipline for that year to obtain the country’s medal winning percentage. We then used the ratios from previous years to train an LSTM model as baseline and conducting a more accurate model based on XGBoost algorithm. The results we predicted were the percentages of medals won by each country out of the total medals awarded in each discipline in 2028. The predicted number of gold, silver, and bronze medals can be calculated by multiplying them by the predicted event numbers and suming up the products. Furthermore, we calculated the 95% confidence intervals for the predicted medal counts by using residuals from the XGBoost model and the properties of the normal distribution. Analysis based on Mann-Kendall test forecast whether a country would do better or worse depending on its performance of the past 5 Games.

<!-- b002262 | prose | pages [10] -->
5.2

<!-- b002263 | heading | pages [10] -->
Data Preparation

<!-- b002264 | prose | pages [10] -->
A country’s medal count is closely tied to its proficiency in various sports. Accounting for the relationship between events and medals, we proposed predicting the probability of a country

<!-- b002265 | prose | pages [10] -->
m

<!-- b002266 | prose | pages [10] -->
m

<!-- b002267 | prose | pages [10] -->
m

<!-- b002268 | prose | pages [10] -->
m

<!-- b002269 | prose | pages [10] -->
m

<!-- b002270 | prose | pages [10] -->
m

<!-- b002271 | prose | pages [10] -->
m

<!-- b002272 | prose | pages [10] -->
m

<!-- b002273 | prose | pages [10] -->
m

<!-- b002274 | prose | pages [10] -->
m

<!-- b002275 | prose | pages [10] -->
m

<!-- b002276 | prose | pages [10] -->
m

<!-- b002277 | prose | pages [10] -->
m

<!-- b002278 | prose | pages [10] -->
m

<!-- b002279 | prose | pages [10] -->
m

<!-- b002280 | prose | pages [10] -->
m

<!-- b002281 | prose | pages [10] -->
m

<!-- b002282 | prose | pages [10] -->
m

<!-- b002283 | prose | pages [10] -->
m

<!-- b002284 | prose | pages [10] -->
m

<!-- b002285 | prose | pages [10] -->
m

<!-- b002286 | prose | pages [10] -->
m

<!-- b002287 | prose | pages [10] -->
m

<!-- b002288 | prose | pages [10] -->
m

<!-- b002289 | prose | pages [10] -->
m

<!-- b002290 | prose | pages [10] -->
m

<!-- b002291 | prose | pages [10] -->
m

<!-- b002292 | prose | pages [10] -->
m

<!-- b002293 | prose | pages [10] -->
m

<!-- b002294 | prose | pages [10] -->
m

<!-- b002295 | prose | pages [10] -->
m

<!-- b002296 | prose | pages [10] -->
m

<!-- b002297 | prose | pages [10] -->
m

<!-- b002298 | prose | pages [10] -->
m

<!-- b002299 | prose | pages [10] -->
m

<!-- b002300 | prose | pages [10] -->
m

<!-- b002301 | prose | pages [10] -->
m

<!-- b002302 | prose | pages [10] -->
m

<!-- b002303 | prose | pages [10] -->
m

<!-- b002304 | prose | pages [10] -->
m

<!-- b002305 | prose | pages [10] -->
m

<!-- b002306 | prose | pages [10] -->
m

<!-- b002307 | prose | pages [10] -->
m

<!-- b002308 | prose | pages [10] -->
m

<!-- b002309 | prose | pages [10] -->
m

<!-- b002310 | prose | pages [10] -->
m

<!-- b002311 | prose | pages [10] -->
m

<!-- b002312 | prose | pages [10] -->
m

<!-- b002313 | prose | pages [10] -->
m

<!-- b002314 | prose | pages [10] -->
m

<!-- b002315 | prose | pages [10] -->
m

<!-- b002316 | prose | pages [10] -->
m

<!-- b002317 | prose | pages [10] -->
m

<!-- b002318 | prose | pages [10] -->
m

<!-- b002319 | prose | pages [10] -->
m

<!-- b002320 | prose | pages [10] -->
m

<!-- b002321 | prose | pages [10] -->
m

<!-- b002322 | prose | pages [10] -->
m

<!-- b002323 | prose | pages [10] -->
m

<!-- b002324 | prose | pages [10] -->
m

<!-- b002325 | prose | pages [10] -->
m

<!-- b002326 | prose | pages [10] -->
m

<!-- b002327 | prose | pages [10] -->
m

<!-- b002328 | prose | pages [10] -->
m

<!-- b002329 | prose | pages [10] -->
m

<!-- b002330 | prose | pages [10] -->
m

<!-- b002331 | prose | pages [10] -->
m

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
winning a medal in each discipline and then multiplying it by the number of events so that we

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
关注数学模型

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

<!-- b002768 | furniture | pages [10] -->
2

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

<!-- b002784 | furniture | pages [10] -->
m

<!-- b002785 | furniture | pages [10] -->
m

<!-- b002786 | furniture | pages [10] -->
m

<!-- b002787 | furniture | pages [10] -->
m

<!-- b002788 | furniture | pages [10] -->
m

<!-- b002789 | furniture | pages [10] -->
m

<!-- b002790 | furniture | pages [10] -->
m

<!-- b002791 | furniture | pages [10] -->
m

<!-- b002792 | furniture | pages [10] -->
m

<!-- b002793 | furniture | pages [10] -->
m

<!-- b002794 | furniture | pages [10] -->
m

<!-- b002795 | furniture | pages [10] -->
m

<!-- b002796 | furniture | pages [10] -->
m

<!-- b002797 | furniture | pages [10] -->
m

<!-- b002798 | furniture | pages [10] -->
m

<!-- b002799 | furniture | pages [10] -->
m

<!-- b002800 | furniture | pages [10] -->
m

<!-- b002801 | furniture | pages [10] -->
m

<!-- b002802 | furniture | pages [10] -->
m

<!-- b002803 | furniture | pages [10] -->
m

<!-- b002804 | furniture | pages [10] -->
m

<!-- b002805 | furniture | pages [10] -->
m

<!-- b002806 | furniture | pages [10] -->
m

<!-- b002807 | furniture | pages [10] -->
m

<!-- b002808 | furniture | pages [10] -->
m

<!-- b002809 | furniture | pages [10] -->
m

<!-- b002810 | furniture | pages [10] -->
m

<!-- b002811 | furniture | pages [10] -->
m

<!-- b002812 | furniture | pages [10] -->
m

<!-- b002813 | furniture | pages [10] -->
m

<!-- b002814 | furniture | pages [10] -->
m

<!-- b002815 | furniture | pages [10] -->
m

<!-- b002816 | furniture | pages [10] -->
m

<!-- b002817 | furniture | pages [10] -->
m

<!-- b002818 | furniture | pages [10] -->
m

<!-- b002819 | furniture | pages [10] -->
m

<!-- b002820 | furniture | pages [10] -->
m

<!-- b002821 | furniture | pages [10] -->
m

<!-- b002822 | furniture | pages [10] -->
m

<!-- b002823 | furniture | pages [10] -->
m

<!-- b002824 | furniture | pages [10] -->
m

<!-- b002825 | furniture | pages [10] -->
m

<!-- b002826 | furniture | pages [10] -->
m

<!-- b002827 | furniture | pages [10] -->
m

<!-- b002828 | furniture | pages [10] -->
m

<!-- b002829 | furniture | pages [10] -->
m

<!-- b002830 | furniture | pages [10] -->
m

<!-- b002831 | furniture | pages [10] -->
m

<!-- b002832 | furniture | pages [10] -->
m

<!-- b002833 | furniture | pages [10] -->
m

<!-- b002834 | furniture | pages [10] -->
m

<!-- b002835 | furniture | pages [10] -->
m

<!-- b002836 | furniture | pages [10] -->
m

<!-- b002837 | furniture | pages [10] -->
m

<!-- b002838 | furniture | pages [10] -->
m

<!-- b002839 | furniture | pages [10] -->
m

<!-- b002840 | furniture | pages [10] -->
m

<!-- b002841 | furniture | pages [10] -->
m

<!-- b002842 | furniture | pages [10] -->
m

<!-- b002843 | furniture | pages [10] -->
m

<!-- b002844 | furniture | pages [10] -->
m

<!-- b002845 | furniture | pages [10] -->
m

<!-- b002846 | furniture | pages [10] -->
m

<!-- b002847 | furniture | pages [10] -->
m

<!-- b002848 | furniture | pages [10] -->
m

<!-- b002849 | furniture | pages [10] -->
m

<!-- b002850 | furniture | pages [10] -->
m

<!-- b002851 | furniture | pages [10] -->
m

<!-- b002852 | furniture | pages [10] -->
m

<!-- b002853 | furniture | pages [10] -->
m

<!-- b002854 | furniture | pages [10] -->
m

<!-- b002855 | furniture | pages [10] -->
m

<!-- b002856 | furniture | pages [10] -->
m

<!-- b002857 | furniture | pages [10] -->
m

<!-- b002858 | furniture | pages [10] -->
m

<!-- b002859 | furniture | pages [10] -->
m

<!-- b002860 | furniture | pages [10] -->
m

<!-- b002861 | furniture | pages [10] -->
m

<!-- b002862 | furniture | pages [10] -->
m

<!-- b002863 | furniture | pages [10] -->
m

<!-- b002864 | furniture | pages [10] -->
m

<!-- b002865 | furniture | pages [10] -->
m

<!-- b002866 | furniture | pages [10] -->
m

<!-- b002867 | furniture | pages [10] -->
m

<!-- b002868 | furniture | pages [10] -->
m

<!-- b002869 | furniture | pages [10] -->
m

<!-- b002870 | furniture | pages [10] -->
m

<!-- b002871 | furniture | pages [10] -->
m

<!-- b002872 | furniture | pages [10] -->
m

<!-- b002873 | furniture | pages [10] -->
m

<!-- b002874 | furniture | pages [10] -->
m

<!-- b002875 | furniture | pages [10] -->
m

<!-- b002876 | furniture | pages [10] -->
m

<!-- b002877 | furniture | pages [10] -->
m

<!-- b002878 | furniture | pages [10] -->
MATHmodels

<!-- b002879 | furniture | pages [10] -->
m

<!-- b002880 | furniture | pages [10] -->
m

<!-- b002881 | furniture | pages [10] -->
m

<!-- b002882 | furniture | pages [10] -->
m

<!-- b002883 | furniture | pages [10] -->
m

<!-- b002884 | furniture | pages [10] -->
m

<!-- b002885 | furniture | pages [10] -->
m

<!-- b002886 | furniture | pages [10] -->
m

<!-- b002887 | furniture | pages [10] -->
m

<!-- b002888 | furniture | pages [10] -->
m

<!-- b002889 | furniture | pages [10] -->
m

<!-- b002890 | furniture | pages [10] -->
m

<!-- b002891 | furniture | pages [10] -->
m

<!-- b002892 | furniture | pages [10] -->
m

<!-- b002893 | furniture | pages [10] -->
m

<!-- b002894 | furniture | pages [10] -->
m

<!-- b002895 | furniture | pages [10] -->
m

<!-- b002896 | furniture | pages [10] -->
获取更多资讯

<!-- b002897 | furniture | pages [10] -->
m

<!-- b002898 | furniture | pages [10] -->
m

<!-- b002899 | furniture | pages [10] -->
m

<!-- b002900 | furniture | pages [10] -->
m

<!-- b002901 | furniture | pages [10] -->
m

<!-- b002902 | furniture | pages [10] -->
m

<!-- b002903 | furniture | pages [10] -->
m

<!-- b002904 | furniture | pages [10] -->
m

<!-- b002905 | furniture | pages [10] -->
m

<!-- b002906 | furniture | pages [10] -->
m

<!-- b002907 | furniture | pages [10] -->
m

<!-- b002908 | furniture | pages [10] -->
m

<!-- b002909 | furniture | pages [10] -->
m

<!-- b002910 | furniture | pages [10] -->
m

<!-- b002911 | furniture | pages [10] -->
m

<!-- b002912 | furniture | pages [10] -->
m

<!-- b002913 | furniture | pages [10] -->
m

<!-- b002914 | furniture | pages [10] -->
m

<!-- b002915 | furniture | pages [10] -->
m

<!-- b002916 | furniture | pages [10] -->
m

<!-- b002917 | furniture | pages [10] -->
m

<!-- b002918 | furniture | pages [10] -->
m

<!-- b002919 | furniture | pages [10] -->
m

<!-- b002920 | furniture | pages [10] -->
m

<!-- b002921 | furniture | pages [10] -->
m

<!-- b002922 | furniture | pages [10] -->
m

<!-- b002923 | furniture | pages [10] -->
m

<!-- b002924 | furniture | pages [10] -->
m

<!-- b002925 | furniture | pages [10] -->
m

<!-- b002926 | furniture | pages [10] -->
m

<!-- b002927 | furniture | pages [10] -->
m

<!-- b002928 | furniture | pages [10] -->
m

<!-- b002929 | furniture | pages [10] -->
m

<!-- b002930 | furniture | pages [10] -->
m

<!-- b002931 | furniture | pages [10] -->
m

<!-- b002932 | furniture | pages [10] -->
m

<!-- b002933 | furniture | pages [10] -->
m

<!-- b002934 | furniture | pages [10] -->
m

<!-- b002935 | furniture | pages [10] -->
m

<!-- b002936 | furniture | pages [10] -->
m

<!-- b002937 | furniture | pages [10] -->
m

<!-- b002938 | furniture | pages [10] -->
m

<!-- b002939 | furniture | pages [10] -->
m

<!-- b002940 | furniture | pages [10] -->
m

<!-- b002941 | furniture | pages [10] -->
m

<!-- b002942 | furniture | pages [10] -->
m

<!-- b002943 | furniture | pages [10] -->
m

<!-- b002944 | furniture | pages [10] -->
m

<!-- b002945 | furniture | pages [10] -->
m

<!-- b002946 | furniture | pages [10] -->
m

<!-- b002947 | furniture | pages [10] -->
m

<!-- b002948 | furniture | pages [10] -->
m

<!-- b002949 | furniture | pages [10] -->
m

<!-- b002950 | furniture | pages [10] -->
m

<!-- b002951 | furniture | pages [10] -->
m

<!-- b002952 | furniture | pages [10] -->
m

<!-- b002953 | furniture | pages [10] -->
m

<!-- b002954 | furniture | pages [10] -->
m

<!-- b002955 | furniture | pages [10] -->
m

<!-- b002956 | furniture | pages [10] -->
m

<!-- b002957 | furniture | pages [11] -->
Team # 2514461

<!-- b002958 | furniture | pages [11] -->
Page 10 of 25

<!-- b002959 | prose | pages [11] -->
could provide a more granular and realistic analysis prediction.

<!-- b002960 | prose | pages [11] -->
First, wetriedeverymeanstocategorizeeacheventwithindataset summerOly_athletes.csv under its respective discipline. Subsequently, the gold, silver, and bronze medal counts for each country within each discipline were calculated and converted into percentages, representing the likelihood of each country achieving correlative medal success. This approach considered the overall performance within each discipline while also acknowledging the significant differences between disciplines within the same sport (e.g., Swimming and Diving under Aquatics), thus avoiding overgeneralization.

<!-- b002961 | prose | pages [11] -->
5.3

<!-- b002962 | heading | pages [11] -->
Baseline: LSTM model

<!-- b002963 | prose | pages [11] -->
5.3.1

<!-- b002964 | heading | pages [11] -->
Model Overview

<!-- b002965 | prose | pages [11] -->
微信公众号：数学模型

<!-- b002966 | prose | pages [11] -->
In this section, a baseline LSTM model was built and trained using Pytorch. The model took as input all the gold / silver / bronze medal counts of all countries before the 2024 Games, and was fitted to the medal counts in 2024. For the loss function, instead of the typically-used MSE loss, we added a punishment term, punishing deviations of the sum of medal counts of all countries for a certain discipline from the discipline’s known event count. In the predict step, all past years’ data were fed into the model to predict the medal counts for all countries in all disciplines. Summing up the disciplines, we yielded the medal count for all countries.

<!-- b002967 | prose | pages [11] -->
5.3.2 Training Process

<!-- b002968 | prose | pages [11] -->
微信号：MATHmodels

<!-- b002969 | prose | pages [11] -->
The training process used the Adam optimizer with the following parameters: learning rate lrinitial = 0.001, β1 = 0.9, β2 = 0.999, and ϵ = 1 × 10−8. The One Cycle Learning Rate Scheduler was applied with a maximum learning rate max_lr = 0.001 for a total of 100,000 epochs. The learning rate was gradually increased and then decreased in a cyclical manner during training.

<!-- b002970 | prose | pages [11] -->
5.3.3

<!-- b002971 | heading | pages [11] -->
Results

<!-- b002972 | prose | pages [11] -->
The final loss dropped to 0.0058, indicating good convergence, however, plain LSTM yielded poor results, as indicated in the following two figures. Fig. 4 repeated the medal count in 2024, and is a clear overfit, while Fig. 5 predicts that China will earn 8 Olympic Gold medals in Table Tennis in 2028, while we know that there are only 5, and China can earn at most 5 (as it did in 2024). Therefore, we must take into consideration varying in the number of events held in each discipline, and avoid overfitting. Also, we should consider host effect. All of these will be addressed in our advanced XGBoost Model in the following section.

<!-- b002973 | caption | pages [11] -->
Figure 4: China’s Diving, Overfitting

<!-- b002974 | caption | pages [11] -->
Figure 5: China’s Table Tennis, Underfitting

<!-- b002975 | prose | pages [11] -->
m

<!-- b002976 | prose | pages [11] -->
m

<!-- b002977 | prose | pages [11] -->
m

<!-- b002978 | prose | pages [11] -->
m

<!-- b002979 | prose | pages [11] -->
m

<!-- b002980 | prose | pages [11] -->
m

<!-- b002981 | prose | pages [11] -->
m

<!-- b002982 | prose | pages [11] -->
m

<!-- b002983 | prose | pages [11] -->
m

<!-- b002984 | prose | pages [11] -->
m

<!-- b002985 | prose | pages [11] -->
m

<!-- b002986 | prose | pages [11] -->
m

<!-- b002987 | prose | pages [11] -->
m

<!-- b002988 | prose | pages [11] -->
m

<!-- b002989 | prose | pages [11] -->
m

<!-- b002990 | prose | pages [11] -->
m

<!-- b002991 | prose | pages [11] -->
m

<!-- b002992 | prose | pages [11] -->
m

<!-- b002993 | prose | pages [11] -->
m

<!-- b002994 | prose | pages [11] -->
m

<!-- b002995 | prose | pages [11] -->
m

<!-- b002996 | prose | pages [11] -->
m

<!-- b002997 | prose | pages [11] -->
m

<!-- b002998 | prose | pages [11] -->
m

<!-- b002999 | prose | pages [11] -->
m

<!-- b003000 | prose | pages [11] -->
m

<!-- b003001 | prose | pages [11] -->
m

<!-- b003002 | prose | pages [11] -->
m

<!-- b003003 | prose | pages [11] -->
m

<!-- b003004 | prose | pages [11] -->
m

<!-- b003005 | prose | pages [11] -->
m

<!-- b003006 | prose | pages [11] -->
m

<!-- b003007 | prose | pages [11] -->
m

<!-- b003008 | prose | pages [11] -->
m

<!-- b003009 | prose | pages [11] -->
m

<!-- b003010 | prose | pages [11] -->
m

<!-- b003011 | prose | pages [11] -->
m

<!-- b003012 | prose | pages [11] -->
m

<!-- b003013 | prose | pages [11] -->
m

<!-- b003014 | prose | pages [11] -->
m

<!-- b003015 | prose | pages [11] -->
m

<!-- b003016 | prose | pages [11] -->
m

<!-- b003017 | prose | pages [11] -->
m

<!-- b003018 | prose | pages [11] -->
m

<!-- b003019 | prose | pages [11] -->
m

<!-- b003020 | prose | pages [11] -->
m

<!-- b003021 | prose | pages [11] -->
m

<!-- b003022 | prose | pages [11] -->
m

<!-- b003023 | prose | pages [11] -->
m

<!-- b003024 | prose | pages [11] -->
m

<!-- b003025 | prose | pages [11] -->
m

<!-- b003026 | prose | pages [11] -->
m

<!-- b003027 | prose | pages [11] -->
m

<!-- b003028 | prose | pages [11] -->
m

<!-- b003029 | prose | pages [11] -->
m

<!-- b003030 | prose | pages [11] -->
m

<!-- b003031 | prose | pages [11] -->
m

<!-- b003032 | prose | pages [11] -->
m

<!-- b003033 | prose | pages [11] -->
m

<!-- b003034 | prose | pages [11] -->
m

<!-- b003035 | prose | pages [11] -->
m

<!-- b003036 | prose | pages [11] -->
m

<!-- b003037 | prose | pages [11] -->
m

<!-- b003038 | prose | pages [11] -->
m

<!-- b003039 | prose | pages [11] -->
m

<!-- b003040 | prose | pages [11] -->
m

<!-- b003041 | prose | pages [11] -->
m

<!-- b003042 | prose | pages [11] -->
m

<!-- b003043 | prose | pages [11] -->
m

<!-- b003044 | prose | pages [11] -->
m

<!-- b003045 | prose | pages [11] -->
m

<!-- b003046 | prose | pages [11] -->
m

<!-- b003047 | prose | pages [11] -->
m

<!-- b003048 | prose | pages [11] -->
m

<!-- b003049 | prose | pages [11] -->
m

<!-- b003050 | prose | pages [11] -->
m

<!-- b003051 | prose | pages [11] -->
m

<!-- b003052 | prose | pages [11] -->
m

<!-- b003053 | prose | pages [11] -->
m

<!-- b003054 | prose | pages [11] -->
m

<!-- b003055 | prose | pages [11] -->
m

<!-- b003056 | prose | pages [11] -->
m

<!-- b003057 | prose | pages [11] -->
m

<!-- b003058 | prose | pages [11] -->
m

<!-- b003059 | prose | pages [11] -->
m

<!-- b003060 | prose | pages [11] -->
m

<!-- b003061 | prose | pages [11] -->
m

<!-- b003062 | prose | pages [11] -->
m

<!-- b003063 | prose | pages [11] -->
m

<!-- b003064 | prose | pages [11] -->
m

<!-- b003065 | prose | pages [11] -->
m

<!-- b003066 | prose | pages [11] -->
m

<!-- b003067 | prose | pages [11] -->
m

<!-- b003068 | prose | pages [11] -->
m

<!-- b003069 | prose | pages [11] -->
m

<!-- b003070 | prose | pages [11] -->
m

<!-- b003071 | prose | pages [11] -->
m

<!-- b003072 | prose | pages [11] -->
m

<!-- b003073 | prose | pages [11] -->
m

<!-- b003074 | prose | pages [11] -->
m

<!-- b003075 | prose | pages [11] -->
m

<!-- b003076 | prose | pages [11] -->
m

<!-- b003077 | prose | pages [11] -->
m

<!-- b003078 | prose | pages [11] -->
m

<!-- b003079 | prose | pages [11] -->
m

<!-- b003080 | prose | pages [11] -->
m

<!-- b003081 | prose | pages [11] -->
m

<!-- b003082 | prose | pages [11] -->
m

<!-- b003083 | prose | pages [11] -->
m

<!-- b003084 | prose | pages [11] -->
m

<!-- b003085 | prose | pages [11] -->
m

<!-- b003086 | prose | pages [11] -->
m

<!-- b003087 | prose | pages [11] -->
m

<!-- b003088 | prose | pages [11] -->
m

<!-- b003089 | prose | pages [11] -->
m

<!-- b003090 | prose | pages [11] -->
m

<!-- b003091 | prose | pages [11] -->
m

<!-- b003092 | prose | pages [11] -->
m

<!-- b003093 | prose | pages [11] -->
m

<!-- b003094 | prose | pages [11] -->
m

<!-- b003095 | prose | pages [11] -->
m

<!-- b003096 | prose | pages [11] -->
m

<!-- b003097 | prose | pages [11] -->
m

<!-- b003098 | prose | pages [11] -->
m

<!-- b003099 | prose | pages [11] -->
m

<!-- b003100 | prose | pages [11] -->
m

<!-- b003101 | prose | pages [11] -->
m

<!-- b003102 | prose | pages [11] -->
m

<!-- b003103 | prose | pages [11] -->
m

<!-- b003104 | prose | pages [11] -->
m

<!-- b003105 | prose | pages [11] -->
m

<!-- b003106 | prose | pages [11] -->
m

<!-- b003107 | prose | pages [11] -->
m

<!-- b003108 | prose | pages [11] -->
m

<!-- b003109 | prose | pages [11] -->
m

<!-- b003110 | prose | pages [11] -->
m

<!-- b003111 | prose | pages [11] -->
m

<!-- b003112 | prose | pages [11] -->
m

<!-- b003113 | prose | pages [11] -->
m

<!-- b003114 | prose | pages [11] -->
m

<!-- b003115 | prose | pages [11] -->
m

<!-- b003116 | prose | pages [11] -->
m

<!-- b003117 | prose | pages [11] -->
m

<!-- b003118 | prose | pages [11] -->
m

<!-- b003119 | prose | pages [11] -->
m

<!-- b003120 | prose | pages [11] -->
m

<!-- b003121 | prose | pages [11] -->
m

<!-- b003122 | prose | pages [11] -->
m

<!-- b003123 | prose | pages [11] -->
m

<!-- b003124 | prose | pages [11] -->
m

<!-- b003125 | prose | pages [11] -->
m

<!-- b003126 | prose | pages [11] -->
m

<!-- b003127 | prose | pages [11] -->
m

<!-- b003128 | prose | pages [11] -->
m

<!-- b003129 | prose | pages [11] -->
m

<!-- b003130 | prose | pages [11] -->
m

<!-- b003131 | prose | pages [11] -->
m

<!-- b003132 | prose | pages [11] -->
m

<!-- b003133 | prose | pages [11] -->
m

<!-- b003134 | prose | pages [11] -->
m

<!-- b003135 | prose | pages [11] -->
m

<!-- b003136 | prose | pages [11] -->
m

<!-- b003137 | prose | pages [11] -->
m

<!-- b003138 | prose | pages [11] -->
m

<!-- b003139 | prose | pages [11] -->
m

<!-- b003140 | prose | pages [11] -->
m

<!-- b003141 | prose | pages [11] -->
m

<!-- b003142 | prose | pages [11] -->
m

<!-- b003143 | prose | pages [11] -->
m

<!-- b003144 | prose | pages [11] -->
m

<!-- b003145 | prose | pages [11] -->
m

<!-- b003146 | prose | pages [11] -->
m

<!-- b003147 | prose | pages [11] -->
m

<!-- b003148 | prose | pages [11] -->
m

<!-- b003149 | prose | pages [11] -->
m

<!-- b003150 | prose | pages [11] -->
m

<!-- b003151 | prose | pages [11] -->
m

<!-- b003152 | prose | pages [11] -->
m

<!-- b003153 | prose | pages [11] -->
m

<!-- b003154 | prose | pages [11] -->
m

<!-- b003155 | prose | pages [11] -->
m

<!-- b003156 | prose | pages [11] -->
m

<!-- b003157 | prose | pages [11] -->
m

<!-- b003158 | prose | pages [11] -->
m

<!-- b003159 | prose | pages [11] -->
m

<!-- b003160 | prose | pages [11] -->
m

<!-- b003161 | prose | pages [11] -->
m

<!-- b003162 | prose | pages [11] -->
m

<!-- b003163 | prose | pages [11] -->
m

<!-- b003164 | prose | pages [11] -->
m

<!-- b003165 | prose | pages [11] -->
m

<!-- b003166 | prose | pages [11] -->
m

<!-- b003167 | prose | pages [11] -->
m

<!-- b003168 | prose | pages [11] -->
m

<!-- b003169 | prose | pages [11] -->
m

<!-- b003170 | prose | pages [11] -->
m

<!-- b003171 | prose | pages [11] -->
m

<!-- b003172 | prose | pages [11] -->
m

<!-- b003173 | prose | pages [11] -->
m

<!-- b003174 | prose | pages [11] -->
m

<!-- b003175 | prose | pages [11] -->
m

<!-- b003176 | prose | pages [11] -->
m

<!-- b003177 | prose | pages [11] -->
m

<!-- b003178 | prose | pages [11] -->
m

<!-- b003179 | prose | pages [11] -->
m

<!-- b003180 | prose | pages [11] -->
m

<!-- b003181 | prose | pages [11] -->
m

<!-- b003182 | prose | pages [11] -->
m

<!-- b003183 | prose | pages [11] -->
m

<!-- b003184 | prose | pages [11] -->
m

<!-- b003185 | prose | pages [11] -->
m

<!-- b003186 | prose | pages [11] -->
m

<!-- b003187 | prose | pages [11] -->
m

<!-- b003188 | prose | pages [11] -->
m

<!-- b003189 | prose | pages [11] -->
m

<!-- b003190 | prose | pages [11] -->
m

<!-- b003191 | prose | pages [11] -->
m

<!-- b003192 | prose | pages [11] -->
m

<!-- b003193 | prose | pages [11] -->
m

<!-- b003194 | prose | pages [11] -->
m

<!-- b003195 | prose | pages [11] -->
m

<!-- b003196 | prose | pages [11] -->
m

<!-- b003197 | prose | pages [11] -->
m

<!-- b003198 | prose | pages [11] -->
m

<!-- b003199 | prose | pages [11] -->
m

<!-- b003200 | prose | pages [11] -->
m

<!-- b003201 | prose | pages [11] -->
m

<!-- b003202 | prose | pages [11] -->
m

<!-- b003203 | prose | pages [11] -->
m

<!-- b003204 | prose | pages [11] -->
m

<!-- b003205 | prose | pages [11] -->
m

<!-- b003206 | prose | pages [11] -->
m

<!-- b003207 | prose | pages [11] -->
m

<!-- b003208 | prose | pages [11] -->
m

<!-- b003209 | prose | pages [11] -->
m

<!-- b003210 | prose | pages [11] -->
m

<!-- b003211 | prose | pages [11] -->
m

<!-- b003212 | prose | pages [11] -->
m

<!-- b003213 | prose | pages [11] -->
m

<!-- b003214 | prose | pages [11] -->
m

<!-- b003215 | prose | pages [11] -->
m

<!-- b003216 | prose | pages [11] -->
m

<!-- b003217 | prose | pages [11] -->
m

<!-- b003218 | prose | pages [11] -->
m

<!-- b003219 | prose | pages [11] -->
m

<!-- b003220 | prose | pages [11] -->
m

<!-- b003221 | prose | pages [11] -->
m

<!-- b003222 | prose | pages [11] -->
m

<!-- b003223 | prose | pages [11] -->
m

<!-- b003224 | prose | pages [11] -->
m

<!-- b003225 | prose | pages [11] -->
m

<!-- b003226 | prose | pages [11] -->
m

<!-- b003227 | prose | pages [11] -->
m

<!-- b003228 | prose | pages [11] -->
m

<!-- b003229 | prose | pages [11] -->
m

<!-- b003230 | prose | pages [11] -->
m

<!-- b003231 | prose | pages [11] -->
m

<!-- b003232 | prose | pages [11] -->
m

<!-- b003233 | prose | pages [11] -->
m

<!-- b003234 | prose | pages [11] -->
m

<!-- b003235 | prose | pages [11] -->
m

<!-- b003236 | prose | pages [11] -->
m

<!-- b003237 | prose | pages [11] -->
m

<!-- b003238 | prose | pages [11] -->
m

<!-- b003239 | prose | pages [11] -->
m

<!-- b003240 | prose | pages [11] -->
m

<!-- b003241 | prose | pages [11] -->
m

<!-- b003242 | prose | pages [11] -->
m

<!-- b003243 | prose | pages [11] -->
m

<!-- b003244 | prose | pages [11] -->
m

<!-- b003245 | prose | pages [11] -->
m

<!-- b003246 | prose | pages [11] -->
m

<!-- b003247 | prose | pages [11] -->
m

<!-- b003248 | prose | pages [11] -->
m

<!-- b003249 | prose | pages [11] -->
m

<!-- b003250 | prose | pages [11] -->
m

<!-- b003251 | prose | pages [11] -->
m

<!-- b003252 | prose | pages [11] -->
m

<!-- b003253 | prose | pages [11] -->
m

<!-- b003254 | prose | pages [11] -->
m

<!-- b003255 | prose | pages [11] -->
m

<!-- b003256 | prose | pages [11] -->
m

<!-- b003257 | prose | pages [11] -->
m

<!-- b003258 | prose | pages [11] -->
m

<!-- b003259 | furniture | pages [11] -->
m

<!-- b003260 | furniture | pages [11] -->
m

<!-- b003261 | furniture | pages [11] -->
m

<!-- b003262 | furniture | pages [11] -->
m

<!-- b003263 | furniture | pages [11] -->
m

<!-- b003264 | furniture | pages [11] -->
m

<!-- b003265 | furniture | pages [11] -->
m

<!-- b003266 | furniture | pages [11] -->
m

<!-- b003267 | furniture | pages [11] -->
m

<!-- b003268 | furniture | pages [11] -->
m

<!-- b003269 | furniture | pages [11] -->
m

<!-- b003270 | furniture | pages [11] -->
m

<!-- b003271 | furniture | pages [11] -->
m

<!-- b003272 | furniture | pages [11] -->
m

<!-- b003273 | furniture | pages [11] -->
m

<!-- b003274 | furniture | pages [11] -->
m

<!-- b003275 | furniture | pages [11] -->
m

<!-- b003276 | furniture | pages [11] -->
m

<!-- b003277 | furniture | pages [11] -->
m

<!-- b003278 | furniture | pages [11] -->
m

<!-- b003279 | furniture | pages [11] -->
m

<!-- b003280 | furniture | pages [11] -->
m

<!-- b003281 | furniture | pages [11] -->
m

<!-- b003282 | furniture | pages [11] -->
m

<!-- b003283 | furniture | pages [11] -->
m

<!-- b003284 | furniture | pages [11] -->
m

<!-- b003285 | furniture | pages [11] -->
m

<!-- b003286 | furniture | pages [11] -->
m

<!-- b003287 | furniture | pages [11] -->
m

<!-- b003288 | furniture | pages [11] -->
m

<!-- b003289 | furniture | pages [11] -->
m

<!-- b003290 | furniture | pages [11] -->
m

<!-- b003291 | furniture | pages [11] -->
m

<!-- b003292 | furniture | pages [11] -->
m

<!-- b003293 | furniture | pages [11] -->
m

<!-- b003294 | furniture | pages [11] -->
m

<!-- b003295 | furniture | pages [11] -->
m

<!-- b003296 | furniture | pages [11] -->
m

<!-- b003297 | furniture | pages [11] -->
m

<!-- b003298 | furniture | pages [11] -->
m

<!-- b003299 | furniture | pages [11] -->
m

<!-- b003300 | furniture | pages [11] -->
m

<!-- b003301 | furniture | pages [11] -->
m

<!-- b003302 | furniture | pages [11] -->
m

<!-- b003303 | furniture | pages [11] -->
m

<!-- b003304 | furniture | pages [11] -->
m

<!-- b003305 | furniture | pages [11] -->
m

<!-- b003306 | furniture | pages [11] -->
m

<!-- b003307 | furniture | pages [11] -->
m

<!-- b003308 | furniture | pages [11] -->
m

<!-- b003309 | furniture | pages [11] -->
m

<!-- b003310 | furniture | pages [11] -->
m

<!-- b003311 | furniture | pages [11] -->
m

<!-- b003312 | furniture | pages [11] -->
m

<!-- b003313 | furniture | pages [11] -->
m

<!-- b003314 | furniture | pages [11] -->
m

<!-- b003315 | furniture | pages [11] -->
m

<!-- b003316 | furniture | pages [11] -->
m

<!-- b003317 | furniture | pages [11] -->
m

<!-- b003318 | furniture | pages [11] -->
m

<!-- b003319 | furniture | pages [11] -->
m

<!-- b003320 | furniture | pages [11] -->
m

<!-- b003321 | furniture | pages [11] -->
m

<!-- b003322 | furniture | pages [11] -->
m

<!-- b003323 | furniture | pages [11] -->
m

<!-- b003324 | furniture | pages [11] -->
m

<!-- b003325 | furniture | pages [11] -->
m

<!-- b003326 | furniture | pages [11] -->
m

<!-- b003327 | furniture | pages [11] -->
m

<!-- b003328 | furniture | pages [11] -->
m

<!-- b003329 | furniture | pages [11] -->
m

<!-- b003330 | furniture | pages [11] -->
m

<!-- b003331 | furniture | pages [11] -->
m

<!-- b003332 | furniture | pages [11] -->
m

<!-- b003333 | furniture | pages [11] -->
m

<!-- b003334 | furniture | pages [11] -->
m

<!-- b003335 | furniture | pages [11] -->
m

<!-- b003336 | furniture | pages [11] -->
m

<!-- b003337 | furniture | pages [11] -->
m

<!-- b003338 | furniture | pages [11] -->
m

<!-- b003339 | furniture | pages [11] -->
m

<!-- b003340 | furniture | pages [11] -->
m

<!-- b003341 | furniture | pages [11] -->
m

<!-- b003342 | furniture | pages [11] -->
m

<!-- b003343 | furniture | pages [11] -->
m

<!-- b003344 | furniture | pages [11] -->
m

<!-- b003345 | furniture | pages [11] -->
m

<!-- b003346 | furniture | pages [11] -->
m

<!-- b003347 | furniture | pages [11] -->
m

<!-- b003348 | furniture | pages [11] -->
m

<!-- b003349 | furniture | pages [11] -->
m

<!-- b003350 | furniture | pages [11] -->
m

<!-- b003351 | furniture | pages [11] -->
m

<!-- b003352 | furniture | pages [11] -->
m

<!-- b003353 | furniture | pages [11] -->
m

<!-- b003354 | furniture | pages [11] -->
m

<!-- b003355 | furniture | pages [11] -->
m

<!-- b003356 | furniture | pages [11] -->
m

<!-- b003357 | furniture | pages [11] -->
m

<!-- b003358 | furniture | pages [11] -->
m

<!-- b003359 | furniture | pages [11] -->
m

<!-- b003360 | furniture | pages [11] -->
m

<!-- b003361 | furniture | pages [11] -->
m

<!-- b003362 | furniture | pages [11] -->
m

<!-- b003363 | furniture | pages [11] -->
m

<!-- b003364 | furniture | pages [11] -->
m

<!-- b003365 | furniture | pages [11] -->
m

<!-- b003366 | furniture | pages [11] -->
m

<!-- b003367 | furniture | pages [11] -->
m

<!-- b003368 | furniture | pages [11] -->
m

<!-- b003369 | furniture | pages [11] -->
m

<!-- b003370 | furniture | pages [11] -->
m

<!-- b003371 | furniture | pages [11] -->
m

<!-- b003372 | furniture | pages [11] -->
m

<!-- b003373 | furniture | pages [11] -->
m

<!-- b003374 | furniture | pages [11] -->
m

<!-- b003375 | furniture | pages [11] -->
m

<!-- b003376 | furniture | pages [11] -->
m

<!-- b003377 | furniture | pages [11] -->
m

<!-- b003378 | furniture | pages [11] -->
m

<!-- b003379 | furniture | pages [11] -->
m

<!-- b003380 | furniture | pages [11] -->
m

<!-- b003381 | furniture | pages [11] -->
m

<!-- b003382 | furniture | pages [11] -->
m

<!-- b003383 | furniture | pages [11] -->
m

<!-- b003384 | furniture | pages [11] -->
m

<!-- b003385 | furniture | pages [11] -->
m

<!-- b003386 | furniture | pages [11] -->
m

<!-- b003387 | furniture | pages [11] -->
m

<!-- b003388 | furniture | pages [11] -->
m

<!-- b003389 | furniture | pages [11] -->
m

<!-- b003390 | furniture | pages [11] -->
m

<!-- b003391 | furniture | pages [11] -->
m

<!-- b003392 | furniture | pages [11] -->
m

<!-- b003393 | furniture | pages [11] -->
m

<!-- b003394 | furniture | pages [11] -->
m

<!-- b003395 | furniture | pages [11] -->
m

<!-- b003396 | furniture | pages [11] -->
m

<!-- b003397 | furniture | pages [11] -->
m

<!-- b003398 | furniture | pages [11] -->
m

<!-- b003399 | furniture | pages [11] -->
m

<!-- b003400 | furniture | pages [11] -->
m

<!-- b003401 | furniture | pages [11] -->
m

<!-- b003402 | furniture | pages [11] -->
m

<!-- b003403 | furniture | pages [11] -->
m

<!-- b003404 | furniture | pages [11] -->
m

<!-- b003405 | furniture | pages [11] -->
m

<!-- b003406 | furniture | pages [11] -->
m

<!-- b003407 | furniture | pages [11] -->
m

<!-- b003408 | furniture | pages [11] -->
m

<!-- b003409 | furniture | pages [11] -->
m

<!-- b003410 | furniture | pages [11] -->
m

<!-- b003411 | furniture | pages [11] -->
m

<!-- b003412 | furniture | pages [11] -->
m

<!-- b003413 | furniture | pages [11] -->
m

<!-- b003414 | furniture | pages [11] -->
m

<!-- b003415 | furniture | pages [11] -->
m

<!-- b003416 | furniture | pages [11] -->
m

<!-- b003417 | furniture | pages [11] -->
m

<!-- b003418 | furniture | pages [11] -->
m

<!-- b003419 | furniture | pages [11] -->
m

<!-- b003420 | furniture | pages [11] -->
m

<!-- b003421 | furniture | pages [11] -->
m

<!-- b003422 | furniture | pages [11] -->
m

<!-- b003423 | furniture | pages [11] -->
m

<!-- b003424 | furniture | pages [11] -->
m

<!-- b003425 | furniture | pages [11] -->
m

<!-- b003426 | furniture | pages [11] -->
m

<!-- b003427 | furniture | pages [11] -->
m

<!-- b003428 | furniture | pages [11] -->
m

<!-- b003429 | furniture | pages [11] -->
m

<!-- b003430 | furniture | pages [11] -->
m

<!-- b003431 | furniture | pages [11] -->
m

<!-- b003432 | furniture | pages [11] -->
m

<!-- b003433 | furniture | pages [11] -->
m

<!-- b003434 | furniture | pages [11] -->
m

<!-- b003435 | furniture | pages [11] -->
m

<!-- b003436 | furniture | pages [11] -->
m

<!-- b003437 | furniture | pages [11] -->
m

<!-- b003438 | furniture | pages [11] -->
m

<!-- b003439 | furniture | pages [11] -->
m

<!-- b003440 | furniture | pages [11] -->
m

<!-- b003441 | furniture | pages [11] -->
m

<!-- b003442 | furniture | pages [11] -->
m

<!-- b003443 | furniture | pages [11] -->
m

<!-- b003444 | furniture | pages [11] -->
m

<!-- b003445 | furniture | pages [11] -->
m

<!-- b003446 | furniture | pages [11] -->
m

<!-- b003447 | furniture | pages [11] -->
m

<!-- b003448 | furniture | pages [11] -->
m

<!-- b003449 | furniture | pages [11] -->
m

<!-- b003450 | furniture | pages [11] -->
m

<!-- b003451 | furniture | pages [11] -->
m

<!-- b003452 | furniture | pages [11] -->
m

<!-- b003453 | furniture | pages [11] -->
m

<!-- b003454 | furniture | pages [11] -->
m

<!-- b003455 | furniture | pages [11] -->
m

<!-- b003456 | furniture | pages [11] -->
m

<!-- b003457 | furniture | pages [11] -->
m

<!-- b003458 | furniture | pages [11] -->
m

<!-- b003459 | furniture | pages [11] -->
m

<!-- b003460 | furniture | pages [11] -->
m

<!-- b003461 | furniture | pages [11] -->
m

<!-- b003462 | furniture | pages [11] -->
m

<!-- b003463 | furniture | pages [11] -->
m

<!-- b003464 | furniture | pages [11] -->
m

<!-- b003465 | furniture | pages [11] -->
m

<!-- b003466 | furniture | pages [11] -->
m

<!-- b003467 | furniture | pages [11] -->
m

<!-- b003468 | furniture | pages [11] -->
m

<!-- b003469 | furniture | pages [11] -->
m

<!-- b003470 | furniture | pages [11] -->
m

<!-- b003471 | furniture | pages [11] -->
m

<!-- b003472 | furniture | pages [11] -->
m

<!-- b003473 | furniture | pages [11] -->
m

<!-- b003474 | furniture | pages [11] -->
m

<!-- b003475 | furniture | pages [11] -->
m

<!-- b003476 | furniture | pages [11] -->
m

<!-- b003477 | furniture | pages [11] -->
m

<!-- b003478 | furniture | pages [11] -->
m

<!-- b003479 | furniture | pages [11] -->
m

<!-- b003480 | furniture | pages [11] -->
m

<!-- b003481 | furniture | pages [11] -->
m

<!-- b003482 | furniture | pages [11] -->
m

<!-- b003483 | furniture | pages [11] -->
m

<!-- b003484 | furniture | pages [11] -->
m

<!-- b003485 | furniture | pages [11] -->
m

<!-- b003486 | furniture | pages [11] -->
m

<!-- b003487 | furniture | pages [11] -->
m

<!-- b003488 | furniture | pages [11] -->
m

<!-- b003489 | furniture | pages [11] -->
m

<!-- b003490 | furniture | pages [11] -->
m

<!-- b003491 | furniture | pages [11] -->
m

<!-- b003492 | furniture | pages [11] -->
m

<!-- b003493 | furniture | pages [11] -->
m

<!-- b003494 | furniture | pages [11] -->
m

<!-- b003495 | furniture | pages [11] -->
m

<!-- b003496 | furniture | pages [11] -->
m

<!-- b003497 | furniture | pages [11] -->
m

<!-- b003498 | furniture | pages [11] -->
m

<!-- b003499 | furniture | pages [11] -->
m

<!-- b003500 | furniture | pages [11] -->
m

<!-- b003501 | furniture | pages [11] -->
m

<!-- b003502 | furniture | pages [11] -->
m

<!-- b003503 | furniture | pages [11] -->
m

<!-- b003504 | furniture | pages [11] -->
m

<!-- b003505 | furniture | pages [11] -->
m

<!-- b003506 | furniture | pages [11] -->
m

<!-- b003507 | furniture | pages [11] -->
m

<!-- b003508 | furniture | pages [11] -->
m

<!-- b003509 | furniture | pages [11] -->
m

<!-- b003510 | furniture | pages [11] -->
m

<!-- b003511 | furniture | pages [11] -->
m

<!-- b003512 | furniture | pages [11] -->
m

<!-- b003513 | furniture | pages [11] -->
m

<!-- b003514 | furniture | pages [11] -->
m

<!-- b003515 | furniture | pages [11] -->
m

<!-- b003516 | furniture | pages [11] -->
m

<!-- b003517 | furniture | pages [11] -->
m

<!-- b003518 | furniture | pages [11] -->
m

<!-- b003519 | furniture | pages [11] -->
m

<!-- b003520 | furniture | pages [11] -->
m

<!-- b003521 | furniture | pages [11] -->
m

<!-- b003522 | furniture | pages [11] -->
m

<!-- b003523 | furniture | pages [11] -->
m

<!-- b003524 | furniture | pages [11] -->
m

<!-- b003525 | furniture | pages [11] -->
m

<!-- b003526 | furniture | pages [11] -->
m

<!-- b003527 | furniture | pages [11] -->
m

<!-- b003528 | furniture | pages [11] -->
m

<!-- b003529 | furniture | pages [11] -->
m

<!-- b003530 | furniture | pages [11] -->
m

<!-- b003531 | furniture | pages [11] -->
m

<!-- b003532 | furniture | pages [11] -->
m

<!-- b003533 | furniture | pages [11] -->
m

<!-- b003534 | furniture | pages [11] -->
m

<!-- b003535 | furniture | pages [11] -->
m

<!-- b003536 | furniture | pages [11] -->
m

<!-- b003537 | furniture | pages [11] -->
m

<!-- b003538 | furniture | pages [11] -->
m

<!-- b003539 | furniture | pages [11] -->
m

<!-- b003540 | furniture | pages [11] -->
m

<!-- b003541 | furniture | pages [11] -->
m

<!-- b003542 | furniture | pages [11] -->
m

<!-- b003543 | furniture | pages [11] -->
m

<!-- b003544 | furniture | pages [11] -->
m

<!-- b003545 | furniture | pages [11] -->
m

<!-- b003546 | furniture | pages [11] -->
m

<!-- b003547 | furniture | pages [11] -->
m

<!-- b003548 | furniture | pages [11] -->
m

<!-- b003549 | furniture | pages [11] -->
m

<!-- b003550 | furniture | pages [11] -->
m

<!-- b003551 | furniture | pages [11] -->
m

<!-- b003552 | furniture | pages [11] -->
m

<!-- b003553 | furniture | pages [11] -->
m

<!-- b003554 | furniture | pages [11] -->
m

<!-- b003555 | furniture | pages [11] -->
m

<!-- b003556 | furniture | pages [11] -->
m

<!-- b003557 | furniture | pages [11] -->
m

<!-- b003558 | furniture | pages [11] -->
m

<!-- b003559 | furniture | pages [11] -->
m

<!-- b003560 | furniture | pages [11] -->
m

<!-- b003561 | furniture | pages [11] -->
m

<!-- b003562 | furniture | pages [11] -->
m

<!-- b003563 | furniture | pages [11] -->
m

<!-- b003564 | furniture | pages [11] -->
m

<!-- b003565 | furniture | pages [11] -->
m

<!-- b003566 | furniture | pages [11] -->
m

<!-- b003567 | furniture | pages [11] -->
m

<!-- b003568 | furniture | pages [11] -->
m

<!-- b003569 | furniture | pages [11] -->
m

<!-- b003570 | furniture | pages [11] -->
m

<!-- b003571 | furniture | pages [11] -->
m

<!-- b003572 | furniture | pages [11] -->
m

<!-- b003573 | furniture | pages [11] -->
m

<!-- b003574 | furniture | pages [11] -->
m

<!-- b003575 | furniture | pages [11] -->
m

<!-- b003576 | furniture | pages [11] -->
m

<!-- b003577 | furniture | pages [11] -->
m

<!-- b003578 | furniture | pages [11] -->
m

<!-- b003579 | furniture | pages [11] -->
m

<!-- b003580 | furniture | pages [11] -->
m

<!-- b003581 | furniture | pages [11] -->
m

<!-- b003582 | furniture | pages [11] -->
m

<!-- b003583 | furniture | pages [11] -->
m

<!-- b003584 | furniture | pages [11] -->
m

<!-- b003585 | furniture | pages [11] -->
m

<!-- b003586 | furniture | pages [11] -->
m

<!-- b003587 | furniture | pages [11] -->
m

<!-- b003588 | furniture | pages [11] -->
m

<!-- b003589 | furniture | pages [11] -->
m

<!-- b003590 | furniture | pages [11] -->
m

<!-- b003591 | furniture | pages [11] -->
m

<!-- b003592 | furniture | pages [11] -->
m

<!-- b003593 | furniture | pages [11] -->
m

<!-- b003594 | furniture | pages [11] -->
m

<!-- b003595 | furniture | pages [11] -->
m

<!-- b003596 | furniture | pages [11] -->
m

<!-- b003597 | furniture | pages [11] -->
m

<!-- b003598 | furniture | pages [11] -->
m

<!-- b003599 | furniture | pages [11] -->
m

<!-- b003600 | furniture | pages [11] -->
m

<!-- b003601 | furniture | pages [11] -->
m

<!-- b003602 | furniture | pages [11] -->
m

<!-- b003603 | furniture | pages [11] -->
m

<!-- b003604 | furniture | pages [11] -->
m

<!-- b003605 | furniture | pages [11] -->
m

<!-- b003606 | furniture | pages [11] -->
m

<!-- b003607 | furniture | pages [11] -->
m

<!-- b003608 | furniture | pages [11] -->
m

<!-- b003609 | furniture | pages [11] -->
m

<!-- b003610 | furniture | pages [11] -->
m

<!-- b003611 | furniture | pages [11] -->
m

<!-- b003612 | furniture | pages [11] -->
m

<!-- b003613 | furniture | pages [11] -->
m

<!-- b003614 | furniture | pages [11] -->
m

<!-- b003615 | furniture | pages [11] -->
m

<!-- b003616 | furniture | pages [11] -->
m

<!-- b003617 | furniture | pages [11] -->
m

<!-- b003618 | furniture | pages [11] -->
m

<!-- b003619 | furniture | pages [11] -->
m

<!-- b003620 | furniture | pages [11] -->
m

<!-- b003621 | furniture | pages [11] -->
m

<!-- b003622 | furniture | pages [11] -->
m

<!-- b003623 | furniture | pages [11] -->
m

<!-- b003624 | furniture | pages [11] -->
m

<!-- b003625 | furniture | pages [11] -->
m

<!-- b003626 | furniture | pages [11] -->
m

<!-- b003627 | furniture | pages [11] -->
m

<!-- b003628 | furniture | pages [11] -->
m

<!-- b003629 | furniture | pages [11] -->
m

<!-- b003630 | furniture | pages [11] -->
m

<!-- b003631 | furniture | pages [11] -->
m

<!-- b003632 | furniture | pages [11] -->
m

<!-- b003633 | furniture | pages [11] -->
m

<!-- b003634 | furniture | pages [11] -->
m

<!-- b003635 | furniture | pages [11] -->
m

<!-- b003636 | furniture | pages [11] -->
m

<!-- b003637 | furniture | pages [11] -->
m

<!-- b003638 | furniture | pages [11] -->
m

<!-- b003639 | furniture | pages [11] -->
m

<!-- b003640 | furniture | pages [11] -->
m

<!-- b003641 | furniture | pages [11] -->
m

<!-- b003642 | furniture | pages [11] -->
m

<!-- b003643 | furniture | pages [11] -->
m

<!-- b003644 | furniture | pages [11] -->
m

<!-- b003645 | furniture | pages [11] -->
m

<!-- b003646 | furniture | pages [11] -->
m

<!-- b003647 | furniture | pages [11] -->
m

<!-- b003648 | furniture | pages [11] -->
m

<!-- b003649 | furniture | pages [11] -->
m

<!-- b003650 | furniture | pages [11] -->
m

<!-- b003651 | furniture | pages [11] -->
m

<!-- b003652 | furniture | pages [11] -->
m

<!-- b003653 | furniture | pages [11] -->
m

<!-- b003654 | furniture | pages [11] -->
m

<!-- b003655 | furniture | pages [11] -->
m

<!-- b003656 | furniture | pages [11] -->
m

<!-- b003657 | furniture | pages [11] -->
m

<!-- b003658 | furniture | pages [11] -->
m

<!-- b003659 | furniture | pages [11] -->
m

<!-- b003660 | furniture | pages [11] -->
m

<!-- b003661 | furniture | pages [11] -->
m

<!-- b003662 | furniture | pages [12] -->
Team # 2514461

<!-- b003663 | prose | pages [12] -->
5.4

<!-- b003664 | heading | pages [12] -->
Advanced: XGBoost model

<!-- b003665 | prose | pages [12] -->
5.4.1

<!-- b003666 | heading | pages [12] -->
Model Establishment

<!-- b003667 | furniture | pages [12] -->
Page 11 of 25

<!-- b003668 | prose | pages [12] -->
Since we had got all the history medal winning ratios, we then employed regression analysis using XGBoost model, combined with cross-validation and randomized search optimization.

<!-- b003669 | prose | pages [12] -->
XGBoost, an ensemble learning algorithm based on gradient boosting, is renowned for its efficiency in making predictions and generating rankings on small to medium-sized structured datasets. The inclusion of 5-fold cross-validation and grid search optimization can further

<!-- b003670 | heading | pages [12] -->
enhance the model’s performance and ensures robust results. [3]

<!-- b003671 | prose | pages [12] -->
XGBoost is an efficient implementation of the gradient boosting algorithm that iteratively adds decision trees to optimize an objective function composed of a loss function for prediction errors and a regularization term for model complexity. In the tth iteration, the model attempts to learn a decision tree ft that fits the residuals r(t−1)

<!-- b003672 | prose | pages [12] -->
where yi is the true value and ˆy(t−1)

<!-- b003673 | prose | pages [12] -->
= yi −ˆy(t−1)

<!-- b003674 | prose | pages [12] -->
from the previous iteration,

<!-- b003675 | prose | pages [12] -->
i i

<!-- b003676 | prose | pages [12] -->
i

<!-- b003677 | prose | pages [12] -->
is the predicted value from the previous iteration. The i objective function is defined as:

<!-- b003678 | prose | pages [12] -->
n

<!-- b003679 | prose | pages [12] -->
l(r(t−1)

<!-- b003680 | prose | pages [12] -->
X

<!-- b003681 | prose | pages [12] -->
Obj =

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
i

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

<!-- b003758 | prose | pages [12] -->
m

<!-- b003759 | prose | pages [12] -->
m

<!-- b003760 | prose | pages [12] -->
m

<!-- b003761 | prose | pages [12] -->
m

<!-- b003762 | prose | pages [12] -->
m

<!-- b003763 | prose | pages [12] -->
m

<!-- b003764 | prose | pages [12] -->
m

<!-- b003765 | prose | pages [12] -->
m

<!-- b003766 | prose | pages [12] -->
m

<!-- b003767 | prose | pages [12] -->
m

<!-- b003768 | prose | pages [12] -->
m

<!-- b003769 | prose | pages [12] -->
m

<!-- b003770 | prose | pages [12] -->
m

<!-- b003771 | prose | pages [12] -->
m

<!-- b003772 | prose | pages [12] -->
m

<!-- b003773 | prose | pages [12] -->
m

<!-- b003774 | prose | pages [12] -->
m

<!-- b003775 | prose | pages [12] -->
m

<!-- b003776 | prose | pages [12] -->
m

<!-- b003777 | prose | pages [12] -->
m

<!-- b003778 | prose | pages [12] -->
m

<!-- b003779 | prose | pages [12] -->
m

<!-- b003780 | prose | pages [12] -->
m

<!-- b003781 | prose | pages [12] -->
m

<!-- b003782 | prose | pages [12] -->
m

<!-- b003783 | prose | pages [12] -->
m

<!-- b003784 | prose | pages [12] -->
m

<!-- b003785 | prose | pages [12] -->
m

<!-- b003786 | prose | pages [12] -->
m

<!-- b003787 | prose | pages [12] -->
m

<!-- b003788 | prose | pages [12] -->
m

<!-- b003789 | prose | pages [12] -->
m

<!-- b003790 | prose | pages [12] -->
m

<!-- b003791 | prose | pages [12] -->
m

<!-- b003792 | prose | pages [12] -->
m

<!-- b003793 | prose | pages [12] -->
m

<!-- b003794 | prose | pages [12] -->
m

<!-- b003795 | prose | pages [12] -->
m

<!-- b003796 | prose | pages [12] -->
m

<!-- b003797 | prose | pages [12] -->
m

<!-- b003798 | prose | pages [12] -->
m

<!-- b003799 | prose | pages [12] -->
m

<!-- b003800 | prose | pages [12] -->
m

<!-- b003801 | prose | pages [12] -->
m

<!-- b003802 | prose | pages [12] -->
m

<!-- b003803 | prose | pages [12] -->
m

<!-- b003804 | prose | pages [12] -->
m

<!-- b003805 | prose | pages [12] -->
m

<!-- b003806 | prose | pages [12] -->
m

<!-- b003807 | prose | pages [12] -->
m

<!-- b003808 | prose | pages [12] -->
m

<!-- b003809 | prose | pages [12] -->
m

<!-- b003810 | prose | pages [12] -->
m

<!-- b003811 | prose | pages [12] -->
m

<!-- b003812 | prose | pages [12] -->
m

<!-- b003813 | prose | pages [12] -->
m

<!-- b003814 | prose | pages [12] -->
m

<!-- b003815 | prose | pages [12] -->
m

<!-- b003816 | prose | pages [12] -->
m

<!-- b003817 | prose | pages [12] -->
m

<!-- b003818 | prose | pages [12] -->
m

<!-- b003819 | prose | pages [12] -->
m

<!-- b003820 | prose | pages [12] -->
m

<!-- b003821 | prose | pages [12] -->
m

<!-- b003822 | prose | pages [12] -->
m

<!-- b003823 | prose | pages [12] -->
m

<!-- b003824 | prose | pages [12] -->
m

<!-- b003825 | prose | pages [12] -->
m

<!-- b003826 | prose | pages [12] -->
m

<!-- b003827 | prose | pages [12] -->
m

<!-- b003828 | prose | pages [12] -->
m

<!-- b003829 | prose | pages [12] -->
i=1

<!-- b003830 | prose | pages [12] -->
m

<!-- b003831 | prose | pages [12] -->
m

<!-- b003832 | prose | pages [12] -->
m

<!-- b003833 | prose | pages [12] -->
m

<!-- b003834 | prose | pages [12] -->
m

<!-- b003835 | prose | pages [12] -->
m

<!-- b003836 | prose | pages [12] -->
m

<!-- b003837 | prose | pages [12] -->
m

<!-- b003838 | prose | pages [12] -->
m

<!-- b003839 | prose | pages [12] -->
m

<!-- b003840 | prose | pages [12] -->
m

<!-- b003841 | prose | pages [12] -->
m

<!-- b003842 | prose | pages [12] -->
m

<!-- b003843 | prose | pages [12] -->
m

<!-- b003844 | prose | pages [12] -->
m

<!-- b003845 | prose | pages [12] -->
m

<!-- b003846 | prose | pages [12] -->
m

<!-- b003847 | prose | pages [12] -->
m

<!-- b003848 | prose | pages [12] -->
m

<!-- b003849 | prose | pages [12] -->
m

<!-- b003850 | prose | pages [12] -->
m

<!-- b003851 | prose | pages [12] -->
m

<!-- b003852 | prose | pages [12] -->
m

<!-- b003853 | prose | pages [12] -->
m

<!-- b003854 | prose | pages [12] -->
m

<!-- b003855 | prose | pages [12] -->
m

<!-- b003856 | prose | pages [12] -->
m

<!-- b003857 | prose | pages [12] -->
m

<!-- b003858 | prose | pages [12] -->
m

<!-- b003859 | prose | pages [12] -->
m

<!-- b003860 | prose | pages [12] -->
m

<!-- b003861 | prose | pages [12] -->
m

<!-- b003862 | prose | pages [12] -->
m

<!-- b003863 | prose | pages [12] -->
m

<!-- b003864 | prose | pages [12] -->
m

<!-- b003865 | prose | pages [12] -->
m

<!-- b003866 | prose | pages [12] -->
m

<!-- b003867 | prose | pages [12] -->
m

<!-- b003868 | prose | pages [12] -->
m

<!-- b003869 | prose | pages [12] -->
m

<!-- b003870 | prose | pages [12] -->
m

<!-- b003871 | prose | pages [12] -->
m

<!-- b003872 | prose | pages [12] -->
m

<!-- b003873 | prose | pages [12] -->
m

<!-- b003874 | prose | pages [12] -->
m

<!-- b003875 | prose | pages [12] -->
m

<!-- b003876 | prose | pages [12] -->
m

<!-- b003877 | prose | pages [12] -->
m

<!-- b003878 | prose | pages [12] -->
m

<!-- b003879 | prose | pages [12] -->
m

<!-- b003880 | prose | pages [12] -->
m

<!-- b003881 | prose | pages [12] -->
m

<!-- b003882 | prose | pages [12] -->
m

<!-- b003883 | prose | pages [12] -->
m

<!-- b003884 | prose | pages [12] -->
m

<!-- b003885 | prose | pages [12] -->
m

<!-- b003886 | prose | pages [12] -->
m

<!-- b003887 | prose | pages [12] -->
m

<!-- b003888 | prose | pages [12] -->
m

<!-- b003889 | prose | pages [12] -->
m

<!-- b003890 | prose | pages [12] -->
m

<!-- b003891 | prose | pages [12] -->
m

<!-- b003892 | prose | pages [12] -->
m

<!-- b003893 | prose | pages [12] -->
m

<!-- b003894 | prose | pages [12] -->
m

<!-- b003895 | prose | pages [12] -->
m

<!-- b003896 | prose | pages [12] -->
m

<!-- b003897 | prose | pages [12] -->
m

<!-- b003898 | prose | pages [12] -->
m

<!-- b003899 | prose | pages [12] -->
m

<!-- b003900 | prose | pages [12] -->
m

<!-- b003901 | prose | pages [12] -->
m

<!-- b003902 | prose | pages [12] -->
m

<!-- b003903 | prose | pages [12] -->
m

<!-- b003904 | prose | pages [12] -->
m

<!-- b003905 | prose | pages [12] -->
m

<!-- b003906 | prose | pages [12] -->
m

<!-- b003907 | prose | pages [12] -->
m

<!-- b003908 | prose | pages [12] -->
m

<!-- b003909 | prose | pages [12] -->
m

<!-- b003910 | prose | pages [12] -->
m

<!-- b003911 | prose | pages [12] -->
m

<!-- b003912 | prose | pages [12] -->
m

<!-- b003913 | prose | pages [12] -->
m

<!-- b003914 | prose | pages [12] -->
m

<!-- b003915 | prose | pages [12] -->
m

<!-- b003916 | prose | pages [12] -->
m

<!-- b003917 | prose | pages [12] -->
m

<!-- b003918 | prose | pages [12] -->
m

<!-- b003919 | prose | pages [12] -->
m

<!-- b003920 | prose | pages [12] -->
m

<!-- b003921 | prose | pages [12] -->
m

<!-- b003922 | prose | pages [12] -->
m

<!-- b003923 | prose | pages [12] -->
m

<!-- b003924 | prose | pages [12] -->
m

<!-- b003925 | prose | pages [12] -->
m

<!-- b003926 | prose | pages [12] -->
m

<!-- b003927 | prose | pages [12] -->
m

<!-- b003928 | prose | pages [12] -->
m

<!-- b003929 | prose | pages [12] -->
m

<!-- b003930 | prose | pages [12] -->
m

<!-- b003931 | prose | pages [12] -->
m

<!-- b003932 | prose | pages [12] -->
m

<!-- b003933 | prose | pages [12] -->
m

<!-- b003934 | prose | pages [12] -->
m

<!-- b003935 | prose | pages [12] -->
m

<!-- b003936 | prose | pages [12] -->
m

<!-- b003937 | prose | pages [12] -->
m

<!-- b003938 | prose | pages [12] -->
m

<!-- b003939 | prose | pages [12] -->
m

<!-- b003940 | prose | pages [12] -->
m

<!-- b003941 | prose | pages [12] -->
m

<!-- b003942 | prose | pages [12] -->
m

<!-- b003943 | prose | pages [12] -->
m

<!-- b003944 | prose | pages [12] -->
m

<!-- b003945 | prose | pages [12] -->
m

<!-- b003946 | prose | pages [12] -->
m

<!-- b003947 | prose | pages [12] -->
m

<!-- b003948 | prose | pages [12] -->
m

<!-- b003949 | prose | pages [12] -->
m

<!-- b003950 | prose | pages [12] -->
m

<!-- b003951 | prose | pages [12] -->
m

<!-- b003952 | prose | pages [12] -->
m

<!-- b003953 | prose | pages [12] -->
m

<!-- b003954 | prose | pages [12] -->
m

<!-- b003955 | prose | pages [12] -->
m

<!-- b003956 | prose | pages [12] -->
m

<!-- b003957 | prose | pages [12] -->
m

<!-- b003958 | prose | pages [12] -->
m

<!-- b003959 | prose | pages [12] -->
m

<!-- b003960 | prose | pages [12] -->
m

<!-- b003961 | prose | pages [12] -->
m

<!-- b003962 | prose | pages [12] -->
m

<!-- b003963 | prose | pages [12] -->
m

<!-- b003964 | prose | pages [12] -->
m

<!-- b003965 | prose | pages [12] -->
m

<!-- b003966 | prose | pages [12] -->
m

<!-- b003967 | prose | pages [12] -->
m

<!-- b003968 | prose | pages [12] -->
m

<!-- b003969 | prose | pages [12] -->
m

<!-- b003970 | prose | pages [12] -->
m

<!-- b003971 | prose | pages [12] -->
m

<!-- b003972 | prose | pages [12] -->
m

<!-- b003973 | prose | pages [12] -->
m

<!-- b003974 | prose | pages [12] -->
m

<!-- b003975 | prose | pages [12] -->
m

<!-- b003976 | prose | pages [12] -->
m

<!-- b003977 | prose | pages [12] -->
m

<!-- b003978 | prose | pages [12] -->
m

<!-- b003979 | prose | pages [12] -->
m

<!-- b003980 | prose | pages [12] -->
m

<!-- b003981 | prose | pages [12] -->
m

<!-- b003982 | prose | pages [12] -->
m

<!-- b003983 | prose | pages [12] -->
m

<!-- b003984 | prose | pages [12] -->
m

<!-- b003985 | prose | pages [12] -->
m

<!-- b003986 | prose | pages [12] -->
m

<!-- b003987 | prose | pages [12] -->
m

<!-- b003988 | prose | pages [12] -->
m

<!-- b003989 | prose | pages [12] -->
m

<!-- b003990 | prose | pages [12] -->
m

<!-- b003991 | prose | pages [12] -->
m

<!-- b003992 | prose | pages [12] -->
m

<!-- b003993 | prose | pages [12] -->
m

<!-- b003994 | prose | pages [12] -->
m

<!-- b003995 | prose | pages [12] -->
m

<!-- b003996 | prose | pages [12] -->
m

<!-- b003997 | prose | pages [12] -->
m

<!-- b003998 | prose | pages [12] -->
m

<!-- b003999 | prose | pages [12] -->
m

<!-- b004000 | prose | pages [12] -->
m

<!-- b004001 | prose | pages [12] -->
m

<!-- b004002 | prose | pages [12] -->
m

<!-- b004003 | prose | pages [12] -->
m

<!-- b004004 | prose | pages [12] -->
m

<!-- b004005 | prose | pages [12] -->
m

<!-- b004006 | prose | pages [12] -->
m

<!-- b004007 | prose | pages [12] -->
m

<!-- b004008 | prose | pages [12] -->
m

<!-- b004009 | prose | pages [12] -->
m

<!-- b004010 | prose | pages [12] -->
m

<!-- b004011 | prose | pages [12] -->
m

<!-- b004012 | prose | pages [12] -->
m

<!-- b004013 | prose | pages [12] -->
m

<!-- b004014 | prose | pages [12] -->
m

<!-- b004015 | prose | pages [12] -->
m

<!-- b004016 | prose | pages [12] -->
m

<!-- b004017 | prose | pages [12] -->
m

<!-- b004018 | prose | pages [12] -->
m

<!-- b004019 | prose | pages [12] -->
m

<!-- b004020 | prose | pages [12] -->
m

<!-- b004021 | prose | pages [12] -->
m

<!-- b004022 | prose | pages [12] -->
m

<!-- b004023 | prose | pages [12] -->
m

<!-- b004024 | prose | pages [12] -->
m

<!-- b004025 | prose | pages [12] -->
m

<!-- b004026 | prose | pages [12] -->
m

<!-- b004027 | prose | pages [12] -->
m

<!-- b004028 | prose | pages [12] -->
m

<!-- b004029 | prose | pages [12] -->
m

<!-- b004030 | prose | pages [12] -->
m

<!-- b004031 | prose | pages [12] -->
m

<!-- b004032 | prose | pages [12] -->
+ ft(xi)) + Ω(ft)) (9)

<!-- b004033 | prose | pages [12] -->
Here, l is the loss function, and Ω(ft) is the regularization term, which penalizes large leaf

<!-- b004034 | prose | pages [12] -->
m

<!-- b004035 | prose | pages [12] -->
m

<!-- b004036 | prose | pages [12] -->
m

<!-- b004037 | prose | pages [12] -->
m

<!-- b004038 | prose | pages [12] -->
m

<!-- b004039 | prose | pages [12] -->
m

<!-- b004040 | prose | pages [12] -->
m

<!-- b004041 | prose | pages [12] -->
m

<!-- b004042 | prose | pages [12] -->
m

<!-- b004043 | prose | pages [12] -->
m

<!-- b004044 | prose | pages [12] -->
m

<!-- b004045 | prose | pages [12] -->
m

<!-- b004046 | prose | pages [12] -->
m

<!-- b004047 | prose | pages [12] -->
m

<!-- b004048 | prose | pages [12] -->
m

<!-- b004049 | prose | pages [12] -->
m

<!-- b004050 | prose | pages [12] -->
m

<!-- b004051 | prose | pages [12] -->
m

<!-- b004052 | prose | pages [12] -->
m

<!-- b004053 | prose | pages [12] -->
m

<!-- b004054 | prose | pages [12] -->
m

<!-- b004055 | prose | pages [12] -->
m

<!-- b004056 | prose | pages [12] -->
m

<!-- b004057 | prose | pages [12] -->
m

<!-- b004058 | prose | pages [12] -->
m

<!-- b004059 | prose | pages [12] -->
m

<!-- b004060 | prose | pages [12] -->
m

<!-- b004061 | prose | pages [12] -->
m

<!-- b004062 | prose | pages [12] -->
m

<!-- b004063 | prose | pages [12] -->
m

<!-- b004064 | prose | pages [12] -->
m

<!-- b004065 | prose | pages [12] -->
m

<!-- b004066 | prose | pages [12] -->
m

<!-- b004067 | prose | pages [12] -->
m

<!-- b004068 | prose | pages [12] -->
m

<!-- b004069 | prose | pages [12] -->
m

<!-- b004070 | prose | pages [12] -->
m

<!-- b004071 | prose | pages [12] -->
m

<!-- b004072 | prose | pages [12] -->
m

<!-- b004073 | prose | pages [12] -->
m

<!-- b004074 | prose | pages [12] -->
m

<!-- b004075 | prose | pages [12] -->
m

<!-- b004076 | prose | pages [12] -->
m

<!-- b004077 | prose | pages [12] -->
m

<!-- b004078 | prose | pages [12] -->
m

<!-- b004079 | prose | pages [12] -->
m

<!-- b004080 | prose | pages [12] -->
m

<!-- b004081 | prose | pages [12] -->
m

<!-- b004082 | prose | pages [12] -->
m

<!-- b004083 | prose | pages [12] -->
m

<!-- b004084 | prose | pages [12] -->
m

<!-- b004085 | prose | pages [12] -->
m

<!-- b004086 | prose | pages [12] -->
m

<!-- b004087 | prose | pages [12] -->
m

<!-- b004088 | prose | pages [12] -->
m

<!-- b004089 | prose | pages [12] -->
m

<!-- b004090 | prose | pages [12] -->
m

<!-- b004091 | prose | pages [12] -->
m

<!-- b004092 | prose | pages [12] -->
m

<!-- b004093 | prose | pages [12] -->
m

<!-- b004094 | prose | pages [12] -->
m

<!-- b004095 | prose | pages [12] -->
m

<!-- b004096 | prose | pages [12] -->
m

<!-- b004097 | prose | pages [12] -->
m

<!-- b004098 | prose | pages [12] -->
m

<!-- b004099 | prose | pages [12] -->
m

<!-- b004100 | prose | pages [12] -->
m

<!-- b004101 | prose | pages [12] -->
m

<!-- b004102 | prose | pages [12] -->
m

<!-- b004103 | prose | pages [12] -->
m

<!-- b004104 | prose | pages [12] -->
m

<!-- b004105 | prose | pages [12] -->
m

<!-- b004106 | prose | pages [12] -->
m

<!-- b004107 | prose | pages [12] -->
m

<!-- b004108 | prose | pages [12] -->
m

<!-- b004109 | prose | pages [12] -->
m

<!-- b004110 | prose | pages [12] -->
m

<!-- b004111 | prose | pages [12] -->
m

<!-- b004112 | prose | pages [12] -->
m

<!-- b004113 | prose | pages [12] -->
m

<!-- b004114 | prose | pages [12] -->
m

<!-- b004115 | prose | pages [12] -->
m

<!-- b004116 | prose | pages [12] -->
m

<!-- b004117 | prose | pages [12] -->
m

<!-- b004118 | prose | pages [12] -->
m

<!-- b004119 | prose | pages [12] -->
m

<!-- b004120 | prose | pages [12] -->
m

<!-- b004121 | prose | pages [12] -->
m

<!-- b004122 | prose | pages [12] -->
m

<!-- b004123 | prose | pages [12] -->
m

<!-- b004124 | prose | pages [12] -->
m

<!-- b004125 | prose | pages [12] -->
m

<!-- b004126 | prose | pages [12] -->
m

<!-- b004127 | prose | pages [12] -->
m

<!-- b004128 | prose | pages [12] -->
m

<!-- b004129 | prose | pages [12] -->
m

<!-- b004130 | prose | pages [12] -->
m

<!-- b004131 | prose | pages [12] -->
m

<!-- b004132 | prose | pages [12] -->
m

<!-- b004133 | prose | pages [12] -->
m

<!-- b004134 | prose | pages [12] -->
m

<!-- b004135 | prose | pages [12] -->
m

<!-- b004136 | prose | pages [12] -->
m

<!-- b004137 | prose | pages [12] -->
m

<!-- b004138 | prose | pages [12] -->
m

<!-- b004139 | prose | pages [12] -->
m

<!-- b004140 | prose | pages [12] -->
m

<!-- b004141 | prose | pages [12] -->
m

<!-- b004142 | prose | pages [12] -->
m

<!-- b004143 | prose | pages [12] -->
m

<!-- b004144 | prose | pages [12] -->
m

<!-- b004145 | prose | pages [12] -->
m

<!-- b004146 | prose | pages [12] -->
m

<!-- b004147 | prose | pages [12] -->
m

<!-- b004148 | prose | pages [12] -->
m

<!-- b004149 | prose | pages [12] -->
m

<!-- b004150 | prose | pages [12] -->
m

<!-- b004151 | prose | pages [12] -->
m

<!-- b004152 | prose | pages [12] -->
m

<!-- b004153 | prose | pages [12] -->
m

<!-- b004154 | prose | pages [12] -->
m

<!-- b004155 | prose | pages [12] -->
m

<!-- b004156 | prose | pages [12] -->
m

<!-- b004157 | prose | pages [12] -->
m

<!-- b004158 | prose | pages [12] -->
m

<!-- b004159 | prose | pages [12] -->
m

<!-- b004160 | prose | pages [12] -->
m

<!-- b004161 | prose | pages [12] -->
m

<!-- b004162 | prose | pages [12] -->
m

<!-- b004163 | prose | pages [12] -->
m

<!-- b004164 | prose | pages [12] -->
m

<!-- b004165 | prose | pages [12] -->
m

<!-- b004166 | prose | pages [12] -->
m

<!-- b004167 | prose | pages [12] -->
m

<!-- b004168 | prose | pages [12] -->
m

<!-- b004169 | prose | pages [12] -->
m

<!-- b004170 | prose | pages [12] -->
m

<!-- b004171 | prose | pages [12] -->
m

<!-- b004172 | prose | pages [12] -->
m

<!-- b004173 | prose | pages [12] -->
m

<!-- b004174 | prose | pages [12] -->
m

<!-- b004175 | prose | pages [12] -->
m

<!-- b004176 | prose | pages [12] -->
m

<!-- b004177 | prose | pages [12] -->
m

<!-- b004178 | prose | pages [12] -->
m

<!-- b004179 | prose | pages [12] -->
m

<!-- b004180 | prose | pages [12] -->
m

<!-- b004181 | prose | pages [12] -->
m

<!-- b004182 | prose | pages [12] -->
m

<!-- b004183 | prose | pages [12] -->
m

<!-- b004184 | prose | pages [12] -->
m

<!-- b004185 | prose | pages [12] -->
m

<!-- b004186 | prose | pages [12] -->
m

<!-- b004187 | prose | pages [12] -->
node weights and an excessive number of leaf nodes to prevent overfitting. In this way, XGBoost

<!-- b004188 | prose | pages [12] -->
m

<!-- b004189 | prose | pages [12] -->
m

<!-- b004190 | prose | pages [12] -->
m

<!-- b004191 | prose | pages [12] -->
m

<!-- b004192 | prose | pages [12] -->
m

<!-- b004193 | prose | pages [12] -->
m

<!-- b004194 | prose | pages [12] -->
m

<!-- b004195 | prose | pages [12] -->
m

<!-- b004196 | prose | pages [12] -->
m

<!-- b004197 | prose | pages [12] -->
m

<!-- b004198 | prose | pages [12] -->
m

<!-- b004199 | prose | pages [12] -->
m

<!-- b004200 | prose | pages [12] -->
m

<!-- b004201 | prose | pages [12] -->
m

<!-- b004202 | prose | pages [12] -->
m

<!-- b004203 | prose | pages [12] -->
m

<!-- b004204 | prose | pages [12] -->
m

<!-- b004205 | prose | pages [12] -->
m

<!-- b004206 | prose | pages [12] -->
m

<!-- b004207 | prose | pages [12] -->
m

<!-- b004208 | prose | pages [12] -->
m

<!-- b004209 | prose | pages [12] -->
m

<!-- b004210 | prose | pages [12] -->
m

<!-- b004211 | prose | pages [12] -->
m

<!-- b004212 | prose | pages [12] -->
m

<!-- b004213 | prose | pages [12] -->
m

<!-- b004214 | prose | pages [12] -->
m

<!-- b004215 | prose | pages [12] -->
m

<!-- b004216 | prose | pages [12] -->
m

<!-- b004217 | prose | pages [12] -->
m

<!-- b004218 | prose | pages [12] -->
m

<!-- b004219 | prose | pages [12] -->
m

<!-- b004220 | prose | pages [12] -->
m

<!-- b004221 | prose | pages [12] -->
m

<!-- b004222 | prose | pages [12] -->
m

<!-- b004223 | prose | pages [12] -->
m

<!-- b004224 | prose | pages [12] -->
m

<!-- b004225 | prose | pages [12] -->
m

<!-- b004226 | prose | pages [12] -->
m

<!-- b004227 | prose | pages [12] -->
m

<!-- b004228 | prose | pages [12] -->
m

<!-- b004229 | prose | pages [12] -->
m

<!-- b004230 | prose | pages [12] -->
m

<!-- b004231 | prose | pages [12] -->
m

<!-- b004232 | prose | pages [12] -->
m

<!-- b004233 | prose | pages [12] -->
m

<!-- b004234 | prose | pages [12] -->
m

<!-- b004235 | prose | pages [12] -->
m

<!-- b004236 | prose | pages [12] -->
m

<!-- b004237 | prose | pages [12] -->
m

<!-- b004238 | prose | pages [12] -->
m

<!-- b004239 | prose | pages [12] -->
m

<!-- b004240 | prose | pages [12] -->
m

<!-- b004241 | prose | pages [12] -->
m

<!-- b004242 | prose | pages [12] -->
m

<!-- b004243 | prose | pages [12] -->
m

<!-- b004244 | prose | pages [12] -->
m

<!-- b004245 | prose | pages [12] -->
m

<!-- b004246 | prose | pages [12] -->
m

<!-- b004247 | prose | pages [12] -->
m

<!-- b004248 | prose | pages [12] -->
m

<!-- b004249 | prose | pages [12] -->
m

<!-- b004250 | prose | pages [12] -->
m

<!-- b004251 | prose | pages [12] -->
m

<!-- b004252 | prose | pages [12] -->
m

<!-- b004253 | prose | pages [12] -->
m

<!-- b004254 | prose | pages [12] -->
m

<!-- b004255 | prose | pages [12] -->
m

<!-- b004256 | prose | pages [12] -->
m

<!-- b004257 | prose | pages [12] -->
m

<!-- b004258 | prose | pages [12] -->
m

<!-- b004259 | prose | pages [12] -->
m

<!-- b004260 | prose | pages [12] -->
m

<!-- b004261 | prose | pages [12] -->
m

<!-- b004262 | prose | pages [12] -->
m

<!-- b004263 | prose | pages [12] -->
m

<!-- b004264 | prose | pages [12] -->
m

<!-- b004265 | prose | pages [12] -->
m

<!-- b004266 | prose | pages [12] -->
m

<!-- b004267 | prose | pages [12] -->
m

<!-- b004268 | prose | pages [12] -->
m

<!-- b004269 | prose | pages [12] -->
m

<!-- b004270 | prose | pages [12] -->
m

<!-- b004271 | prose | pages [12] -->
m

<!-- b004272 | prose | pages [12] -->
m

<!-- b004273 | prose | pages [12] -->
m

<!-- b004274 | prose | pages [12] -->
m

<!-- b004275 | prose | pages [12] -->
m

<!-- b004276 | prose | pages [12] -->
m

<!-- b004277 | prose | pages [12] -->
m

<!-- b004278 | prose | pages [12] -->
m

<!-- b004279 | prose | pages [12] -->
m

<!-- b004280 | prose | pages [12] -->
m

<!-- b004281 | prose | pages [12] -->
m

<!-- b004282 | prose | pages [12] -->
m

<!-- b004283 | prose | pages [12] -->
m

<!-- b004284 | prose | pages [12] -->
m

<!-- b004285 | prose | pages [12] -->
m

<!-- b004286 | prose | pages [12] -->
m

<!-- b004287 | prose | pages [12] -->
m

<!-- b004288 | prose | pages [12] -->
m

<!-- b004289 | prose | pages [12] -->
m

<!-- b004290 | prose | pages [12] -->
m

<!-- b004291 | prose | pages [12] -->
m

<!-- b004292 | prose | pages [12] -->
m

<!-- b004293 | prose | pages [12] -->
m

<!-- b004294 | prose | pages [12] -->
m

<!-- b004295 | prose | pages [12] -->
m

<!-- b004296 | prose | pages [12] -->
m

<!-- b004297 | prose | pages [12] -->
m

<!-- b004298 | prose | pages [12] -->
m

<!-- b004299 | prose | pages [12] -->
m

<!-- b004300 | prose | pages [12] -->
m

<!-- b004301 | prose | pages [12] -->
m

<!-- b004302 | prose | pages [12] -->
m

<!-- b004303 | prose | pages [12] -->
m

<!-- b004304 | prose | pages [12] -->
m

<!-- b004305 | prose | pages [12] -->
m

<!-- b004306 | prose | pages [12] -->
m

<!-- b004307 | prose | pages [12] -->
m

<!-- b004308 | prose | pages [12] -->
m

<!-- b004309 | prose | pages [12] -->
m

<!-- b004310 | prose | pages [12] -->
m

<!-- b004311 | prose | pages [12] -->
m

<!-- b004312 | prose | pages [12] -->
m

<!-- b004313 | prose | pages [12] -->
m

<!-- b004314 | prose | pages [12] -->
m

<!-- b004315 | prose | pages [12] -->
m

<!-- b004316 | prose | pages [12] -->
m

<!-- b004317 | prose | pages [12] -->
m

<!-- b004318 | prose | pages [12] -->
m

<!-- b004319 | prose | pages [12] -->
m

<!-- b004320 | prose | pages [12] -->
m

<!-- b004321 | prose | pages [12] -->
m

<!-- b004322 | prose | pages [12] -->
m

<!-- b004323 | prose | pages [12] -->
m

<!-- b004324 | prose | pages [12] -->
m

<!-- b004325 | prose | pages [12] -->
m

<!-- b004326 | prose | pages [12] -->
m

<!-- b004327 | prose | pages [12] -->
m

<!-- b004328 | prose | pages [12] -->
m

<!-- b004329 | prose | pages [12] -->
m

<!-- b004330 | prose | pages [12] -->
m

<!-- b004331 | prose | pages [12] -->
m

<!-- b004332 | prose | pages [12] -->
can control the complexity of the model while maintaining its performance.

<!-- b004333 | prose | pages [12] -->
m

<!-- b004334 | prose | pages [12] -->
m

<!-- b004335 | prose | pages [12] -->
m

<!-- b004336 | prose | pages [12] -->
m

<!-- b004337 | prose | pages [12] -->
m

<!-- b004338 | prose | pages [12] -->
m

<!-- b004339 | prose | pages [12] -->
m

<!-- b004340 | prose | pages [12] -->
m

<!-- b004341 | prose | pages [12] -->
m

<!-- b004342 | prose | pages [12] -->
m

<!-- b004343 | prose | pages [12] -->
m

<!-- b004344 | prose | pages [12] -->
m

<!-- b004345 | prose | pages [12] -->
m

<!-- b004346 | prose | pages [12] -->
m

<!-- b004347 | prose | pages [12] -->
m

<!-- b004348 | prose | pages [12] -->
m

<!-- b004349 | prose | pages [12] -->
m

<!-- b004350 | prose | pages [12] -->
m

<!-- b004351 | prose | pages [12] -->
m

<!-- b004352 | prose | pages [12] -->
m

<!-- b004353 | prose | pages [12] -->
m

<!-- b004354 | prose | pages [12] -->
m

<!-- b004355 | prose | pages [12] -->
m

<!-- b004356 | prose | pages [12] -->
m

<!-- b004357 | prose | pages [12] -->
m

<!-- b004358 | prose | pages [12] -->
m

<!-- b004359 | prose | pages [12] -->
m

<!-- b004360 | prose | pages [12] -->
m

<!-- b004361 | prose | pages [12] -->
m

<!-- b004362 | prose | pages [12] -->
m

<!-- b004363 | prose | pages [12] -->
m

<!-- b004364 | prose | pages [12] -->
m

<!-- b004365 | prose | pages [12] -->
m

<!-- b004366 | prose | pages [12] -->
m

<!-- b004367 | prose | pages [12] -->
m

<!-- b004368 | prose | pages [12] -->
m

<!-- b004369 | prose | pages [12] -->
m

<!-- b004370 | prose | pages [12] -->
m

<!-- b004371 | prose | pages [12] -->
m

<!-- b004372 | prose | pages [12] -->
m

<!-- b004373 | prose | pages [12] -->
m

<!-- b004374 | prose | pages [12] -->
m

<!-- b004375 | prose | pages [12] -->
We first collected statistics on the number of gold, silver and bronze medals each country won in each discipline every year, then divided by the total number of medals awarded in that discipline for that year to obtain the medal ratio of that country. By running an XGBoost model with the ratios from past years, we predicted medal ratios in 2028.

<!-- b004376 | caption | pages [12] -->
Figure 7: Probability prediction of Chinese diving gold and

<!-- b004377 | prose | pages [12] -->
Silver MEDALS in 2028 Olympic Games

<!-- b004378 | caption | pages [12] -->
Figure 6: Flow chart of medal

<!-- b004379 | prose | pages [12] -->
count based on XGBoost

<!-- b004380 | prose | pages [12] -->
Based on predictions, we took into account the host country effect, where athletes may

<!-- b004381 | prose | pages [12] -->
关注数学模型

<!-- b004382 | furniture | pages [12] -->
2

<!-- b004383 | furniture | pages [12] -->
MATHmodels

<!-- b004384 | furniture | pages [12] -->
获取更多资讯

<!-- b004385 | furniture | pages [13] -->
Team # 2514461

<!-- b004386 | furniture | pages [13] -->
Page 12 of 25

<!-- b004387 | prose | pages [13] -->
perform better when competing in their own country due to familiarity with the environment, reduced travel fatigue, easier adjustment to time zones and climate, and other factors. We calculated the score increases of the host countries in recent Olympic Games, measuring the host country effect by the ratio of this Game’s scores to last Game’s scores.

<!-- b004388 | prose | pages [13] -->
We observed that approximately 90% of countries exhibit an improvement in their perfor- mance during the Olympics hosted in their own nation. Specifically, 77% of these countries have seen an increase exceeding 20%, and 44% have experienced an increase of more than 50%. However, the countries with increases over 50% tend to be those with relatively fewer points (the Soviet Union is excluded from this analysis as it has since transitioned into Russia and other countries). Therefore, it is unreasonable to anticipate a substantial increase for the United States, a major scoring country and the host of the 2028 Olympics. Considering that the U.S.

<!-- b004389 | prose | pages [13] -->
微信公众号：数学模型

<!-- b004390 | prose | pages [13] -->
has previously observed a decrease of 7% in scores when hosting, we deemed it reasonable to predict that the U.S. will have a hosting nation increase between 0% and 20% for the year 2024. In our predictive model, we incorporated a scoring increase of 15%.

<!-- b004391 | prose | pages [13] -->
微信号：MATHmodels

<!-- b004392 | caption | pages [13] -->
Figure 8: Analysis of the advantages of the host country. The light yellow score indicates the

<!-- b004393 | prose | pages [13] -->
score when the country was the host country, and the score ratio indicates the score when the country is the host country divided by the score of the previous Olympics Game.

<!-- b004394 | prose | pages [13] -->
After obtaining the medal winning ratios for each country in 2028 using the XGBoost model and considering the host country effect, we normalized these ratios and multiplied them by the number of events in each discipline as predicted by the SVR model discussed in the fourth section. This process ultimately yielded the predicted medal count, which we then displayed in a medal ranking table as Fig.10 shows.

<!-- b004395 | prose | pages [13] -->
5.5 Examining the confidence of the prediction interval

<!-- b004396 | prose | pages [13] -->
Since the XGBoost model can only return predicted values and not directly provide con- fidence intervals, we can use the predicted values given by XGBoost and the real number of medals to calculate the standard deviation of the residuals between the predicted and real values in the first step. In the second step, we can estimate the prediction interval by calculating the confidence interval using the predicted and actual values. Below is a detailed explanation of the approach.

<!-- b004397 | prose | pages [13] -->
We used the sampling distribution theory in statistics to estimate the confidence intervals of prediction results. Due to the randomness of sampling, different samples may produce different

<!-- b004398 | prose | pages [13] -->
m

<!-- b004399 | prose | pages [13] -->
m

<!-- b004400 | prose | pages [13] -->
m

<!-- b004401 | prose | pages [13] -->
m

<!-- b004402 | prose | pages [13] -->
m

<!-- b004403 | prose | pages [13] -->
m

<!-- b004404 | prose | pages [13] -->
m

<!-- b004405 | prose | pages [13] -->
m

<!-- b004406 | prose | pages [13] -->
m

<!-- b004407 | prose | pages [13] -->
m

<!-- b004408 | prose | pages [13] -->
m

<!-- b004409 | prose | pages [13] -->
m

<!-- b004410 | prose | pages [13] -->
m

<!-- b004411 | prose | pages [13] -->
m

<!-- b004412 | prose | pages [13] -->
m

<!-- b004413 | prose | pages [13] -->
m

<!-- b004414 | prose | pages [13] -->
m

<!-- b004415 | prose | pages [13] -->
m

<!-- b004416 | prose | pages [13] -->
m

<!-- b004417 | prose | pages [13] -->
m

<!-- b004418 | prose | pages [13] -->
m

<!-- b004419 | prose | pages [13] -->
m

<!-- b004420 | prose | pages [13] -->
m

<!-- b004421 | prose | pages [13] -->
m

<!-- b004422 | prose | pages [13] -->
m

<!-- b004423 | prose | pages [13] -->
m

<!-- b004424 | prose | pages [13] -->
m

<!-- b004425 | prose | pages [13] -->
m

<!-- b004426 | prose | pages [13] -->
m

<!-- b004427 | prose | pages [13] -->
m

<!-- b004428 | prose | pages [13] -->
m

<!-- b004429 | prose | pages [13] -->
m

<!-- b004430 | prose | pages [13] -->
m

<!-- b004431 | prose | pages [13] -->
m

<!-- b004432 | prose | pages [13] -->
m

<!-- b004433 | prose | pages [13] -->
m

<!-- b004434 | prose | pages [13] -->
m

<!-- b004435 | prose | pages [13] -->
m

<!-- b004436 | prose | pages [13] -->
m

<!-- b004437 | prose | pages [13] -->
m

<!-- b004438 | prose | pages [13] -->
m

<!-- b004439 | prose | pages [13] -->
m

<!-- b004440 | prose | pages [13] -->
m

<!-- b004441 | prose | pages [13] -->
m

<!-- b004442 | prose | pages [13] -->
m

<!-- b004443 | prose | pages [13] -->
m

<!-- b004444 | prose | pages [13] -->
m

<!-- b004445 | prose | pages [13] -->
m

<!-- b004446 | prose | pages [13] -->
m

<!-- b004447 | prose | pages [13] -->
m

<!-- b004448 | prose | pages [13] -->
m

<!-- b004449 | prose | pages [13] -->
m

<!-- b004450 | prose | pages [13] -->
m

<!-- b004451 | prose | pages [13] -->
m

<!-- b004452 | prose | pages [13] -->
m

<!-- b004453 | prose | pages [13] -->
m

<!-- b004454 | prose | pages [13] -->
m

<!-- b004455 | prose | pages [13] -->
m

<!-- b004456 | prose | pages [13] -->
m

<!-- b004457 | prose | pages [13] -->
m

<!-- b004458 | prose | pages [13] -->
m

<!-- b004459 | prose | pages [13] -->
m

<!-- b004460 | prose | pages [13] -->
m

<!-- b004461 | prose | pages [13] -->
m

<!-- b004462 | prose | pages [13] -->
m

<!-- b004463 | prose | pages [13] -->
m

<!-- b004464 | prose | pages [13] -->
m

<!-- b004465 | prose | pages [13] -->
m

<!-- b004466 | prose | pages [13] -->
m

<!-- b004467 | prose | pages [13] -->
m

<!-- b004468 | prose | pages [13] -->
m

<!-- b004469 | prose | pages [13] -->
m

<!-- b004470 | prose | pages [13] -->
m

<!-- b004471 | prose | pages [13] -->
m

<!-- b004472 | prose | pages [13] -->
m

<!-- b004473 | prose | pages [13] -->
m

<!-- b004474 | prose | pages [13] -->
m

<!-- b004475 | prose | pages [13] -->
m

<!-- b004476 | prose | pages [13] -->
m

<!-- b004477 | prose | pages [13] -->
m

<!-- b004478 | prose | pages [13] -->
m

<!-- b004479 | prose | pages [13] -->
m

<!-- b004480 | prose | pages [13] -->
m

<!-- b004481 | prose | pages [13] -->
m

<!-- b004482 | prose | pages [13] -->
m

<!-- b004483 | prose | pages [13] -->
m

<!-- b004484 | prose | pages [13] -->
m

<!-- b004485 | prose | pages [13] -->
m

<!-- b004486 | prose | pages [13] -->
m

<!-- b004487 | prose | pages [13] -->
m

<!-- b004488 | prose | pages [13] -->
m

<!-- b004489 | prose | pages [13] -->
m

<!-- b004490 | prose | pages [13] -->
m

<!-- b004491 | prose | pages [13] -->
m

<!-- b004492 | prose | pages [13] -->
m

<!-- b004493 | prose | pages [13] -->
m

<!-- b004494 | prose | pages [13] -->
m

<!-- b004495 | prose | pages [13] -->
m

<!-- b004496 | prose | pages [13] -->
m

<!-- b004497 | prose | pages [13] -->
m

<!-- b004498 | prose | pages [13] -->
m

<!-- b004499 | prose | pages [13] -->
m

<!-- b004500 | prose | pages [13] -->
m

<!-- b004501 | prose | pages [13] -->
m

<!-- b004502 | prose | pages [13] -->
m

<!-- b004503 | prose | pages [13] -->
m

<!-- b004504 | prose | pages [13] -->
m

<!-- b004505 | prose | pages [13] -->
m

<!-- b004506 | prose | pages [13] -->
m

<!-- b004507 | prose | pages [13] -->
m

<!-- b004508 | prose | pages [13] -->
m

<!-- b004509 | prose | pages [13] -->
m

<!-- b004510 | prose | pages [13] -->
m

<!-- b004511 | prose | pages [13] -->
m

<!-- b004512 | prose | pages [13] -->
m

<!-- b004513 | prose | pages [13] -->
m

<!-- b004514 | prose | pages [13] -->
m

<!-- b004515 | prose | pages [13] -->
m

<!-- b004516 | prose | pages [13] -->
m

<!-- b004517 | prose | pages [13] -->
m

<!-- b004518 | prose | pages [13] -->
m

<!-- b004519 | prose | pages [13] -->
m

<!-- b004520 | prose | pages [13] -->
m

<!-- b004521 | prose | pages [13] -->
m

<!-- b004522 | prose | pages [13] -->
m

<!-- b004523 | prose | pages [13] -->
m

<!-- b004524 | prose | pages [13] -->
m

<!-- b004525 | prose | pages [13] -->
m

<!-- b004526 | prose | pages [13] -->
m

<!-- b004527 | prose | pages [13] -->
m

<!-- b004528 | prose | pages [13] -->
m

<!-- b004529 | prose | pages [13] -->
m

<!-- b004530 | prose | pages [13] -->
m

<!-- b004531 | prose | pages [13] -->
m

<!-- b004532 | prose | pages [13] -->
m

<!-- b004533 | prose | pages [13] -->
m

<!-- b004534 | prose | pages [13] -->
m

<!-- b004535 | prose | pages [13] -->
m

<!-- b004536 | prose | pages [13] -->
m

<!-- b004537 | prose | pages [13] -->
m

<!-- b004538 | prose | pages [13] -->
m

<!-- b004539 | prose | pages [13] -->
m

<!-- b004540 | prose | pages [13] -->
m

<!-- b004541 | prose | pages [13] -->
m

<!-- b004542 | prose | pages [13] -->
m

<!-- b004543 | prose | pages [13] -->
m

<!-- b004544 | prose | pages [13] -->
m

<!-- b004545 | prose | pages [13] -->
m

<!-- b004546 | prose | pages [13] -->
m

<!-- b004547 | prose | pages [13] -->
m

<!-- b004548 | prose | pages [13] -->
m

<!-- b004549 | prose | pages [13] -->
m

<!-- b004550 | prose | pages [13] -->
m

<!-- b004551 | prose | pages [13] -->
m

<!-- b004552 | prose | pages [13] -->
m

<!-- b004553 | prose | pages [13] -->
m

<!-- b004554 | prose | pages [13] -->
m

<!-- b004555 | prose | pages [13] -->
m

<!-- b004556 | prose | pages [13] -->
m

<!-- b004557 | prose | pages [13] -->
m

<!-- b004558 | prose | pages [13] -->
m

<!-- b004559 | prose | pages [13] -->
m

<!-- b004560 | prose | pages [13] -->
m

<!-- b004561 | prose | pages [13] -->
m

<!-- b004562 | prose | pages [13] -->
m

<!-- b004563 | prose | pages [13] -->
m

<!-- b004564 | prose | pages [13] -->
m

<!-- b004565 | prose | pages [13] -->
m

<!-- b004566 | prose | pages [13] -->
m

<!-- b004567 | prose | pages [13] -->
m

<!-- b004568 | prose | pages [13] -->
m

<!-- b004569 | prose | pages [13] -->
m

<!-- b004570 | prose | pages [13] -->
m

<!-- b004571 | prose | pages [13] -->
m

<!-- b004572 | prose | pages [13] -->
m

<!-- b004573 | prose | pages [13] -->
m

<!-- b004574 | prose | pages [13] -->
m

<!-- b004575 | prose | pages [13] -->
m

<!-- b004576 | prose | pages [13] -->
m

<!-- b004577 | prose | pages [13] -->
m

<!-- b004578 | prose | pages [13] -->
m

<!-- b004579 | prose | pages [13] -->
m

<!-- b004580 | prose | pages [13] -->
m

<!-- b004581 | prose | pages [13] -->
m

<!-- b004582 | prose | pages [13] -->
m

<!-- b004583 | prose | pages [13] -->
m

<!-- b004584 | prose | pages [13] -->
m

<!-- b004585 | prose | pages [13] -->
m

<!-- b004586 | prose | pages [13] -->
m

<!-- b004587 | prose | pages [13] -->
m

<!-- b004588 | prose | pages [13] -->
m

<!-- b004589 | prose | pages [13] -->
m

<!-- b004590 | prose | pages [13] -->
m

<!-- b004591 | prose | pages [13] -->
m

<!-- b004592 | prose | pages [13] -->
m

<!-- b004593 | prose | pages [13] -->
m

<!-- b004594 | prose | pages [13] -->
m

<!-- b004595 | prose | pages [13] -->
m

<!-- b004596 | prose | pages [13] -->
m

<!-- b004597 | prose | pages [13] -->
m

<!-- b004598 | prose | pages [13] -->
m

<!-- b004599 | prose | pages [13] -->
m

<!-- b004600 | prose | pages [13] -->
m

<!-- b004601 | prose | pages [13] -->
m

<!-- b004602 | prose | pages [13] -->
m

<!-- b004603 | prose | pages [13] -->
m

<!-- b004604 | prose | pages [13] -->
m

<!-- b004605 | prose | pages [13] -->
m

<!-- b004606 | prose | pages [13] -->
m

<!-- b004607 | prose | pages [13] -->
m

<!-- b004608 | prose | pages [13] -->
m

<!-- b004609 | prose | pages [13] -->
m

<!-- b004610 | prose | pages [13] -->
m

<!-- b004611 | prose | pages [13] -->
m

<!-- b004612 | prose | pages [13] -->
m

<!-- b004613 | prose | pages [13] -->
m

<!-- b004614 | prose | pages [13] -->
m

<!-- b004615 | prose | pages [13] -->
m

<!-- b004616 | prose | pages [13] -->
m

<!-- b004617 | prose | pages [13] -->
m

<!-- b004618 | prose | pages [13] -->
m

<!-- b004619 | prose | pages [13] -->
m

<!-- b004620 | prose | pages [13] -->
m

<!-- b004621 | prose | pages [13] -->
m

<!-- b004622 | prose | pages [13] -->
m

<!-- b004623 | prose | pages [13] -->
m

<!-- b004624 | prose | pages [13] -->
m

<!-- b004625 | prose | pages [13] -->
m

<!-- b004626 | prose | pages [13] -->
m

<!-- b004627 | prose | pages [13] -->
m

<!-- b004628 | prose | pages [13] -->
m

<!-- b004629 | prose | pages [13] -->
m

<!-- b004630 | prose | pages [13] -->
m

<!-- b004631 | prose | pages [13] -->
m

<!-- b004632 | prose | pages [13] -->
m

<!-- b004633 | prose | pages [13] -->
m

<!-- b004634 | prose | pages [13] -->
m

<!-- b004635 | prose | pages [13] -->
m

<!-- b004636 | prose | pages [13] -->
m

<!-- b004637 | prose | pages [13] -->
m

<!-- b004638 | prose | pages [13] -->
m

<!-- b004639 | prose | pages [13] -->
m

<!-- b004640 | prose | pages [13] -->
m

<!-- b004641 | prose | pages [13] -->
m

<!-- b004642 | prose | pages [13] -->
m

<!-- b004643 | prose | pages [13] -->
m

<!-- b004644 | prose | pages [13] -->
m

<!-- b004645 | prose | pages [13] -->
m

<!-- b004646 | prose | pages [13] -->
m

<!-- b004647 | prose | pages [13] -->
m

<!-- b004648 | prose | pages [13] -->
m

<!-- b004649 | prose | pages [13] -->
m

<!-- b004650 | prose | pages [13] -->
m

<!-- b004651 | prose | pages [13] -->
m

<!-- b004652 | prose | pages [13] -->
m

<!-- b004653 | prose | pages [13] -->
m

<!-- b004654 | prose | pages [13] -->
m

<!-- b004655 | prose | pages [13] -->
m

<!-- b004656 | prose | pages [13] -->
m

<!-- b004657 | prose | pages [13] -->
m

<!-- b004658 | prose | pages [13] -->
m

<!-- b004659 | prose | pages [13] -->
m

<!-- b004660 | prose | pages [13] -->
m

<!-- b004661 | prose | pages [13] -->
m

<!-- b004662 | prose | pages [13] -->
m

<!-- b004663 | prose | pages [13] -->
m

<!-- b004664 | prose | pages [13] -->
m

<!-- b004665 | prose | pages [13] -->
m

<!-- b004666 | prose | pages [13] -->
m

<!-- b004667 | prose | pages [13] -->
m

<!-- b004668 | prose | pages [13] -->
m

<!-- b004669 | prose | pages [13] -->
m

<!-- b004670 | prose | pages [13] -->
m

<!-- b004671 | prose | pages [13] -->
m

<!-- b004672 | prose | pages [13] -->
m

<!-- b004673 | prose | pages [13] -->
m

<!-- b004674 | prose | pages [13] -->
m

<!-- b004675 | prose | pages [13] -->
m

<!-- b004676 | prose | pages [13] -->
m

<!-- b004677 | prose | pages [13] -->
m

<!-- b004678 | prose | pages [13] -->
m

<!-- b004679 | prose | pages [13] -->
m

<!-- b004680 | prose | pages [13] -->
m

<!-- b004681 | prose | pages [13] -->
m

<!-- b004682 | furniture | pages [13] -->
m

<!-- b004683 | furniture | pages [13] -->
m

<!-- b004684 | furniture | pages [13] -->
m

<!-- b004685 | furniture | pages [13] -->
m

<!-- b004686 | furniture | pages [13] -->
m

<!-- b004687 | furniture | pages [13] -->
m

<!-- b004688 | furniture | pages [13] -->
m

<!-- b004689 | furniture | pages [13] -->
m

<!-- b004690 | furniture | pages [13] -->
m

<!-- b004691 | furniture | pages [13] -->
m

<!-- b004692 | furniture | pages [13] -->
m

<!-- b004693 | furniture | pages [13] -->
m

<!-- b004694 | furniture | pages [13] -->
m

<!-- b004695 | furniture | pages [13] -->
m

<!-- b004696 | furniture | pages [13] -->
m

<!-- b004697 | furniture | pages [13] -->
m

<!-- b004698 | furniture | pages [13] -->
m

<!-- b004699 | furniture | pages [13] -->
m

<!-- b004700 | furniture | pages [13] -->
m

<!-- b004701 | furniture | pages [13] -->
m

<!-- b004702 | furniture | pages [13] -->
m

<!-- b004703 | furniture | pages [13] -->
m

<!-- b004704 | furniture | pages [13] -->
m

<!-- b004705 | furniture | pages [13] -->
m

<!-- b004706 | furniture | pages [13] -->
m

<!-- b004707 | furniture | pages [13] -->
m

<!-- b004708 | furniture | pages [13] -->
m

<!-- b004709 | furniture | pages [13] -->
m

<!-- b004710 | furniture | pages [13] -->
m

<!-- b004711 | furniture | pages [13] -->
m

<!-- b004712 | furniture | pages [13] -->
m

<!-- b004713 | furniture | pages [13] -->
m

<!-- b004714 | furniture | pages [13] -->
m

<!-- b004715 | furniture | pages [13] -->
m

<!-- b004716 | furniture | pages [13] -->
m

<!-- b004717 | furniture | pages [13] -->
m

<!-- b004718 | furniture | pages [13] -->
m

<!-- b004719 | furniture | pages [13] -->
m

<!-- b004720 | furniture | pages [13] -->
m

<!-- b004721 | furniture | pages [13] -->
m

<!-- b004722 | furniture | pages [13] -->
m

<!-- b004723 | furniture | pages [13] -->
m

<!-- b004724 | furniture | pages [13] -->
m

<!-- b004725 | furniture | pages [13] -->
m

<!-- b004726 | furniture | pages [13] -->
m

<!-- b004727 | furniture | pages [13] -->
m

<!-- b004728 | furniture | pages [13] -->
m

<!-- b004729 | furniture | pages [13] -->
m

<!-- b004730 | furniture | pages [13] -->
m

<!-- b004731 | furniture | pages [13] -->
m

<!-- b004732 | furniture | pages [13] -->
m

<!-- b004733 | furniture | pages [13] -->
m

<!-- b004734 | furniture | pages [13] -->
m

<!-- b004735 | furniture | pages [13] -->
m

<!-- b004736 | furniture | pages [13] -->
m

<!-- b004737 | furniture | pages [13] -->
m

<!-- b004738 | furniture | pages [13] -->
m

<!-- b004739 | furniture | pages [13] -->
m

<!-- b004740 | furniture | pages [13] -->
m

<!-- b004741 | furniture | pages [13] -->
m

<!-- b004742 | furniture | pages [13] -->
m

<!-- b004743 | furniture | pages [13] -->
m

<!-- b004744 | furniture | pages [13] -->
m

<!-- b004745 | furniture | pages [13] -->
m

<!-- b004746 | furniture | pages [13] -->
m

<!-- b004747 | furniture | pages [13] -->
m

<!-- b004748 | furniture | pages [13] -->
m

<!-- b004749 | furniture | pages [13] -->
m

<!-- b004750 | furniture | pages [13] -->
m

<!-- b004751 | furniture | pages [13] -->
m

<!-- b004752 | furniture | pages [13] -->
m

<!-- b004753 | furniture | pages [13] -->
m

<!-- b004754 | furniture | pages [13] -->
m

<!-- b004755 | furniture | pages [13] -->
m

<!-- b004756 | furniture | pages [13] -->
m

<!-- b004757 | furniture | pages [13] -->
m

<!-- b004758 | furniture | pages [13] -->
m

<!-- b004759 | furniture | pages [13] -->
m

<!-- b004760 | furniture | pages [13] -->
m

<!-- b004761 | furniture | pages [13] -->
m

<!-- b004762 | furniture | pages [13] -->
m

<!-- b004763 | furniture | pages [13] -->
m

<!-- b004764 | furniture | pages [13] -->
m

<!-- b004765 | furniture | pages [13] -->
m

<!-- b004766 | furniture | pages [13] -->
m

<!-- b004767 | furniture | pages [13] -->
m

<!-- b004768 | furniture | pages [13] -->
m

<!-- b004769 | furniture | pages [13] -->
m

<!-- b004770 | furniture | pages [13] -->
m

<!-- b004771 | furniture | pages [13] -->
m

<!-- b004772 | furniture | pages [13] -->
m

<!-- b004773 | furniture | pages [13] -->
m

<!-- b004774 | furniture | pages [13] -->
m

<!-- b004775 | furniture | pages [13] -->
m

<!-- b004776 | furniture | pages [13] -->
m

<!-- b004777 | furniture | pages [13] -->
m

<!-- b004778 | furniture | pages [13] -->
m

<!-- b004779 | furniture | pages [13] -->
m

<!-- b004780 | furniture | pages [13] -->
m

<!-- b004781 | furniture | pages [13] -->
m

<!-- b004782 | furniture | pages [13] -->
m

<!-- b004783 | furniture | pages [13] -->
m

<!-- b004784 | furniture | pages [13] -->
m

<!-- b004785 | furniture | pages [13] -->
m

<!-- b004786 | furniture | pages [13] -->
m

<!-- b004787 | furniture | pages [13] -->
m

<!-- b004788 | furniture | pages [13] -->
m

<!-- b004789 | furniture | pages [13] -->
m

<!-- b004790 | furniture | pages [13] -->
m

<!-- b004791 | furniture | pages [13] -->
m

<!-- b004792 | furniture | pages [13] -->
m

<!-- b004793 | furniture | pages [13] -->
m

<!-- b004794 | furniture | pages [13] -->
m

<!-- b004795 | furniture | pages [13] -->
m

<!-- b004796 | furniture | pages [13] -->
m

<!-- b004797 | furniture | pages [13] -->
m

<!-- b004798 | furniture | pages [13] -->
m

<!-- b004799 | furniture | pages [13] -->
m

<!-- b004800 | furniture | pages [13] -->
m

<!-- b004801 | furniture | pages [13] -->
m

<!-- b004802 | furniture | pages [13] -->
m

<!-- b004803 | furniture | pages [13] -->
m

<!-- b004804 | furniture | pages [13] -->
m

<!-- b004805 | furniture | pages [13] -->
m

<!-- b004806 | furniture | pages [13] -->
m

<!-- b004807 | furniture | pages [13] -->
m

<!-- b004808 | furniture | pages [13] -->
m

<!-- b004809 | furniture | pages [13] -->
m

<!-- b004810 | furniture | pages [13] -->
m

<!-- b004811 | furniture | pages [13] -->
m

<!-- b004812 | furniture | pages [13] -->
m

<!-- b004813 | furniture | pages [13] -->
m

<!-- b004814 | furniture | pages [13] -->
m

<!-- b004815 | furniture | pages [13] -->
m

<!-- b004816 | furniture | pages [13] -->
m

<!-- b004817 | furniture | pages [13] -->
m

<!-- b004818 | furniture | pages [13] -->
m

<!-- b004819 | furniture | pages [13] -->
m

<!-- b004820 | furniture | pages [13] -->
m

<!-- b004821 | furniture | pages [13] -->
m

<!-- b004822 | furniture | pages [13] -->
m

<!-- b004823 | furniture | pages [13] -->
m

<!-- b004824 | furniture | pages [13] -->
m

<!-- b004825 | furniture | pages [13] -->
m

<!-- b004826 | furniture | pages [13] -->
m

<!-- b004827 | furniture | pages [13] -->
m

<!-- b004828 | furniture | pages [13] -->
m

<!-- b004829 | furniture | pages [13] -->
m

<!-- b004830 | furniture | pages [13] -->
m

<!-- b004831 | furniture | pages [13] -->
m

<!-- b004832 | furniture | pages [13] -->
m

<!-- b004833 | furniture | pages [13] -->
m

<!-- b004834 | furniture | pages [13] -->
m

<!-- b004835 | furniture | pages [13] -->
m

<!-- b004836 | furniture | pages [13] -->
m

<!-- b004837 | furniture | pages [13] -->
m

<!-- b004838 | furniture | pages [13] -->
m

<!-- b004839 | furniture | pages [13] -->
m

<!-- b004840 | furniture | pages [13] -->
m

<!-- b004841 | furniture | pages [13] -->
m

<!-- b004842 | furniture | pages [13] -->
m

<!-- b004843 | furniture | pages [13] -->
m

<!-- b004844 | furniture | pages [13] -->
m

<!-- b004845 | furniture | pages [13] -->
m

<!-- b004846 | furniture | pages [13] -->
m

<!-- b004847 | furniture | pages [13] -->
m

<!-- b004848 | furniture | pages [13] -->
m

<!-- b004849 | furniture | pages [13] -->
m

<!-- b004850 | furniture | pages [13] -->
m

<!-- b004851 | furniture | pages [13] -->
m

<!-- b004852 | furniture | pages [13] -->
m

<!-- b004853 | furniture | pages [13] -->
m

<!-- b004854 | furniture | pages [13] -->
m

<!-- b004855 | furniture | pages [13] -->
m

<!-- b004856 | furniture | pages [13] -->
m

<!-- b004857 | furniture | pages [13] -->
m

<!-- b004858 | furniture | pages [13] -->
m

<!-- b004859 | furniture | pages [13] -->
m

<!-- b004860 | furniture | pages [13] -->
m

<!-- b004861 | furniture | pages [13] -->
m

<!-- b004862 | furniture | pages [13] -->
m

<!-- b004863 | furniture | pages [13] -->
m

<!-- b004864 | furniture | pages [13] -->
m

<!-- b004865 | furniture | pages [13] -->
m

<!-- b004866 | furniture | pages [13] -->
m

<!-- b004867 | furniture | pages [13] -->
m

<!-- b004868 | furniture | pages [13] -->
m

<!-- b004869 | furniture | pages [13] -->
m

<!-- b004870 | furniture | pages [13] -->
m

<!-- b004871 | furniture | pages [13] -->
m

<!-- b004872 | furniture | pages [13] -->
m

<!-- b004873 | furniture | pages [13] -->
m

<!-- b004874 | furniture | pages [13] -->
m

<!-- b004875 | furniture | pages [13] -->
m

<!-- b004876 | furniture | pages [13] -->
m

<!-- b004877 | furniture | pages [13] -->
m

<!-- b004878 | furniture | pages [13] -->
m

<!-- b004879 | furniture | pages [13] -->
m

<!-- b004880 | furniture | pages [13] -->
m

<!-- b004881 | furniture | pages [13] -->
m

<!-- b004882 | furniture | pages [13] -->
m

<!-- b004883 | furniture | pages [13] -->
m

<!-- b004884 | furniture | pages [13] -->
m

<!-- b004885 | furniture | pages [13] -->
m

<!-- b004886 | furniture | pages [13] -->
m

<!-- b004887 | furniture | pages [13] -->
m

<!-- b004888 | furniture | pages [13] -->
m

<!-- b004889 | furniture | pages [13] -->
m

<!-- b004890 | furniture | pages [13] -->
m

<!-- b004891 | furniture | pages [13] -->
m

<!-- b004892 | furniture | pages [13] -->
m

<!-- b004893 | furniture | pages [13] -->
m

<!-- b004894 | furniture | pages [13] -->
m

<!-- b004895 | furniture | pages [13] -->
m

<!-- b004896 | furniture | pages [13] -->
m

<!-- b004897 | furniture | pages [13] -->
m

<!-- b004898 | furniture | pages [13] -->
m

<!-- b004899 | furniture | pages [13] -->
m

<!-- b004900 | furniture | pages [13] -->
m

<!-- b004901 | furniture | pages [13] -->
m

<!-- b004902 | furniture | pages [13] -->
m

<!-- b004903 | furniture | pages [13] -->
m

<!-- b004904 | furniture | pages [13] -->
m

<!-- b004905 | furniture | pages [13] -->
m

<!-- b004906 | furniture | pages [13] -->
m

<!-- b004907 | furniture | pages [13] -->
m

<!-- b004908 | furniture | pages [13] -->
m

<!-- b004909 | furniture | pages [13] -->
m

<!-- b004910 | furniture | pages [13] -->
m

<!-- b004911 | furniture | pages [13] -->
m

<!-- b004912 | furniture | pages [13] -->
m

<!-- b004913 | furniture | pages [13] -->
m

<!-- b004914 | furniture | pages [13] -->
m

<!-- b004915 | furniture | pages [13] -->
m

<!-- b004916 | furniture | pages [13] -->
m

<!-- b004917 | furniture | pages [13] -->
m

<!-- b004918 | furniture | pages [13] -->
m

<!-- b004919 | furniture | pages [13] -->
m

<!-- b004920 | furniture | pages [13] -->
m

<!-- b004921 | furniture | pages [13] -->
m

<!-- b004922 | furniture | pages [13] -->
m

<!-- b004923 | furniture | pages [13] -->
m

<!-- b004924 | furniture | pages [13] -->
m

<!-- b004925 | furniture | pages [13] -->
m

<!-- b004926 | furniture | pages [13] -->
m

<!-- b004927 | furniture | pages [13] -->
m

<!-- b004928 | furniture | pages [13] -->
m

<!-- b004929 | furniture | pages [13] -->
m

<!-- b004930 | furniture | pages [13] -->
m

<!-- b004931 | furniture | pages [13] -->
m

<!-- b004932 | furniture | pages [13] -->
m

<!-- b004933 | furniture | pages [13] -->
m

<!-- b004934 | furniture | pages [13] -->
m

<!-- b004935 | furniture | pages [13] -->
m

<!-- b004936 | furniture | pages [13] -->
m

<!-- b004937 | furniture | pages [13] -->
m

<!-- b004938 | furniture | pages [13] -->
m

<!-- b004939 | furniture | pages [13] -->
m

<!-- b004940 | furniture | pages [13] -->
m

<!-- b004941 | furniture | pages [13] -->
m

<!-- b004942 | furniture | pages [13] -->
m

<!-- b004943 | furniture | pages [13] -->
m

<!-- b004944 | furniture | pages [13] -->
m

<!-- b004945 | furniture | pages [13] -->
m

<!-- b004946 | furniture | pages [13] -->
m

<!-- b004947 | furniture | pages [13] -->
m

<!-- b004948 | furniture | pages [13] -->
m

<!-- b004949 | furniture | pages [13] -->
m

<!-- b004950 | furniture | pages [13] -->
m

<!-- b004951 | furniture | pages [13] -->
m

<!-- b004952 | furniture | pages [13] -->
m

<!-- b004953 | furniture | pages [13] -->
m

<!-- b004954 | furniture | pages [13] -->
m

<!-- b004955 | furniture | pages [13] -->
m

<!-- b004956 | furniture | pages [13] -->
m

<!-- b004957 | furniture | pages [13] -->
m

<!-- b004958 | furniture | pages [13] -->
m

<!-- b004959 | furniture | pages [13] -->
m

<!-- b004960 | furniture | pages [13] -->
m

<!-- b004961 | furniture | pages [13] -->
m

<!-- b004962 | furniture | pages [13] -->
m

<!-- b004963 | furniture | pages [13] -->
m

<!-- b004964 | furniture | pages [13] -->
m

<!-- b004965 | furniture | pages [13] -->
m

<!-- b004966 | furniture | pages [13] -->
m

<!-- b004967 | furniture | pages [13] -->
m

<!-- b004968 | furniture | pages [13] -->
m

<!-- b004969 | furniture | pages [13] -->
m

<!-- b004970 | furniture | pages [13] -->
m

<!-- b004971 | furniture | pages [13] -->
m

<!-- b004972 | furniture | pages [13] -->
m

<!-- b004973 | furniture | pages [13] -->
m

<!-- b004974 | furniture | pages [13] -->
m

<!-- b004975 | furniture | pages [13] -->
m

<!-- b004976 | furniture | pages [13] -->
m

<!-- b004977 | furniture | pages [13] -->
m

<!-- b004978 | furniture | pages [13] -->
m

<!-- b004979 | furniture | pages [13] -->
m

<!-- b004980 | furniture | pages [13] -->
m

<!-- b004981 | furniture | pages [13] -->
m

<!-- b004982 | furniture | pages [13] -->
m

<!-- b004983 | furniture | pages [13] -->
m

<!-- b004984 | furniture | pages [13] -->
m

<!-- b004985 | furniture | pages [13] -->
m

<!-- b004986 | furniture | pages [13] -->
m

<!-- b004987 | furniture | pages [13] -->
m

<!-- b004988 | furniture | pages [13] -->
m

<!-- b004989 | furniture | pages [13] -->
m

<!-- b004990 | furniture | pages [13] -->
m

<!-- b004991 | furniture | pages [13] -->
m

<!-- b004992 | furniture | pages [13] -->
m

<!-- b004993 | furniture | pages [13] -->
m

<!-- b004994 | furniture | pages [13] -->
m

<!-- b004995 | furniture | pages [13] -->
m

<!-- b004996 | furniture | pages [13] -->
m

<!-- b004997 | furniture | pages [13] -->
m

<!-- b004998 | furniture | pages [13] -->
m

<!-- b004999 | furniture | pages [13] -->
m

<!-- b005000 | furniture | pages [13] -->
m

<!-- b005001 | furniture | pages [13] -->
m

<!-- b005002 | furniture | pages [13] -->
m

<!-- b005003 | furniture | pages [13] -->
m

<!-- b005004 | furniture | pages [13] -->
m

<!-- b005005 | furniture | pages [13] -->
m

<!-- b005006 | furniture | pages [13] -->
m

<!-- b005007 | furniture | pages [13] -->
m

<!-- b005008 | furniture | pages [13] -->
m

<!-- b005009 | furniture | pages [13] -->
m

<!-- b005010 | furniture | pages [13] -->
m

<!-- b005011 | furniture | pages [13] -->
m

<!-- b005012 | furniture | pages [13] -->
m

<!-- b005013 | furniture | pages [13] -->
m

<!-- b005014 | furniture | pages [13] -->
m

<!-- b005015 | furniture | pages [13] -->
m

<!-- b005016 | furniture | pages [13] -->
m

<!-- b005017 | furniture | pages [13] -->
m

<!-- b005018 | furniture | pages [13] -->
m

<!-- b005019 | furniture | pages [13] -->
m

<!-- b005020 | furniture | pages [13] -->
m

<!-- b005021 | furniture | pages [13] -->
m

<!-- b005022 | furniture | pages [13] -->
m

<!-- b005023 | furniture | pages [13] -->
m

<!-- b005024 | furniture | pages [13] -->
m

<!-- b005025 | furniture | pages [13] -->
m

<!-- b005026 | furniture | pages [13] -->
m

<!-- b005027 | furniture | pages [13] -->
m

<!-- b005028 | furniture | pages [13] -->
m

<!-- b005029 | furniture | pages [13] -->
m

<!-- b005030 | furniture | pages [13] -->
m

<!-- b005031 | furniture | pages [13] -->
m

<!-- b005032 | furniture | pages [13] -->
m

<!-- b005033 | furniture | pages [13] -->
m

<!-- b005034 | furniture | pages [13] -->
m

<!-- b005035 | furniture | pages [13] -->
m

<!-- b005036 | furniture | pages [13] -->
m

<!-- b005037 | furniture | pages [13] -->
m

<!-- b005038 | furniture | pages [13] -->
m

<!-- b005039 | furniture | pages [13] -->
m

<!-- b005040 | furniture | pages [13] -->
m

<!-- b005041 | furniture | pages [13] -->
m

<!-- b005042 | furniture | pages [13] -->
m

<!-- b005043 | furniture | pages [13] -->
m

<!-- b005044 | furniture | pages [13] -->
m

<!-- b005045 | furniture | pages [13] -->
m

<!-- b005046 | furniture | pages [13] -->
m

<!-- b005047 | furniture | pages [13] -->
m

<!-- b005048 | furniture | pages [13] -->
m

<!-- b005049 | furniture | pages [13] -->
m

<!-- b005050 | furniture | pages [13] -->
m

<!-- b005051 | furniture | pages [13] -->
m

<!-- b005052 | furniture | pages [13] -->
m

<!-- b005053 | furniture | pages [13] -->
m

<!-- b005054 | furniture | pages [13] -->
m

<!-- b005055 | furniture | pages [13] -->
m

<!-- b005056 | furniture | pages [13] -->
m

<!-- b005057 | furniture | pages [13] -->
m

<!-- b005058 | furniture | pages [13] -->
m

<!-- b005059 | furniture | pages [13] -->
m

<!-- b005060 | furniture | pages [13] -->
m

<!-- b005061 | furniture | pages [13] -->
m

<!-- b005062 | furniture | pages [13] -->
m

<!-- b005063 | furniture | pages [13] -->
m

<!-- b005064 | furniture | pages [13] -->
m

<!-- b005065 | furniture | pages [13] -->
m

<!-- b005066 | furniture | pages [13] -->
m

<!-- b005067 | furniture | pages [13] -->
m

<!-- b005068 | furniture | pages [13] -->
m

<!-- b005069 | furniture | pages [13] -->
m

<!-- b005070 | furniture | pages [13] -->
m

<!-- b005071 | furniture | pages [13] -->
m

<!-- b005072 | furniture | pages [13] -->
m

<!-- b005073 | furniture | pages [13] -->
m

<!-- b005074 | furniture | pages [13] -->
m

<!-- b005075 | furniture | pages [13] -->
m

<!-- b005076 | furniture | pages [13] -->
m

<!-- b005077 | furniture | pages [13] -->
m

<!-- b005078 | furniture | pages [13] -->
m

<!-- b005079 | furniture | pages [13] -->
m

<!-- b005080 | furniture | pages [13] -->
m

<!-- b005081 | furniture | pages [13] -->
m

<!-- b005082 | furniture | pages [13] -->
m

<!-- b005083 | furniture | pages [13] -->
m

<!-- b005084 | furniture | pages [13] -->
m

<!-- b005085 | furniture | pages [14] -->
Team # 2514461

<!-- b005086 | caption | pages [14] -->
Figure 9: Top 10 of predicted 2028 medal

<!-- b005087 | prose | pages [14] -->
table

<!-- b005088 | furniture | pages [14] -->
Page 13 of 25

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
m

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
m

<!-- b005184 | prose | pages [14] -->
m

<!-- b005185 | prose | pages [14] -->
m

<!-- b005186 | prose | pages [14] -->
m

<!-- b005187 | prose | pages [14] -->
m

<!-- b005188 | prose | pages [14] -->
m

<!-- b005189 | prose | pages [14] -->
m

<!-- b005190 | prose | pages [14] -->
m

<!-- b005191 | prose | pages [14] -->
m

<!-- b005192 | prose | pages [14] -->
m

<!-- b005193 | prose | pages [14] -->
m

<!-- b005194 | prose | pages [14] -->
m

<!-- b005195 | prose | pages [14] -->
m

<!-- b005196 | prose | pages [14] -->
m

<!-- b005197 | prose | pages [14] -->
m

<!-- b005198 | prose | pages [14] -->
m

<!-- b005199 | prose | pages [14] -->
m

<!-- b005200 | prose | pages [14] -->
m

<!-- b005201 | prose | pages [14] -->
m

<!-- b005202 | prose | pages [14] -->
m

<!-- b005203 | prose | pages [14] -->
m

<!-- b005204 | prose | pages [14] -->
m

<!-- b005205 | prose | pages [14] -->
m

<!-- b005206 | prose | pages [14] -->
m

<!-- b005207 | prose | pages [14] -->
m

<!-- b005208 | prose | pages [14] -->
m

<!-- b005209 | prose | pages [14] -->
m

<!-- b005210 | prose | pages [14] -->
m

<!-- b005211 | prose | pages [14] -->
m

<!-- b005212 | prose | pages [14] -->
m

<!-- b005213 | prose | pages [14] -->
m

<!-- b005214 | prose | pages [14] -->
m

<!-- b005215 | prose | pages [14] -->
m

<!-- b005216 | prose | pages [14] -->
m

<!-- b005217 | prose | pages [14] -->
m

<!-- b005218 | prose | pages [14] -->
m

<!-- b005219 | prose | pages [14] -->
m

<!-- b005220 | prose | pages [14] -->
m

<!-- b005221 | prose | pages [14] -->
m

<!-- b005222 | prose | pages [14] -->
m

<!-- b005223 | prose | pages [14] -->
m

<!-- b005224 | prose | pages [14] -->
m

<!-- b005225 | prose | pages [14] -->
m

<!-- b005226 | prose | pages [14] -->
m

<!-- b005227 | prose | pages [14] -->
m

<!-- b005228 | prose | pages [14] -->
m

<!-- b005229 | prose | pages [14] -->
m

<!-- b005230 | prose | pages [14] -->
m

<!-- b005231 | prose | pages [14] -->
m

<!-- b005232 | prose | pages [14] -->
m

<!-- b005233 | prose | pages [14] -->
m

<!-- b005234 | prose | pages [14] -->
m

<!-- b005235 | prose | pages [14] -->
m

<!-- b005236 | prose | pages [14] -->
m

<!-- b005237 | prose | pages [14] -->
m

<!-- b005238 | prose | pages [14] -->
m

<!-- b005239 | prose | pages [14] -->
m

<!-- b005240 | prose | pages [14] -->
m

<!-- b005241 | prose | pages [14] -->
m

<!-- b005242 | prose | pages [14] -->
m

<!-- b005243 | prose | pages [14] -->
m

<!-- b005244 | prose | pages [14] -->
m

<!-- b005245 | prose | pages [14] -->
m

<!-- b005246 | prose | pages [14] -->
m

<!-- b005247 | prose | pages [14] -->
m

<!-- b005248 | prose | pages [14] -->
m

<!-- b005249 | prose | pages [14] -->
m

<!-- b005250 | prose | pages [14] -->
m

<!-- b005251 | prose | pages [14] -->
m

<!-- b005252 | prose | pages [14] -->
m

<!-- b005253 | prose | pages [14] -->
m

<!-- b005254 | prose | pages [14] -->
m

<!-- b005255 | prose | pages [14] -->
m

<!-- b005256 | prose | pages [14] -->
m

<!-- b005257 | prose | pages [14] -->
m

<!-- b005258 | prose | pages [14] -->
m

<!-- b005259 | prose | pages [14] -->
m

<!-- b005260 | prose | pages [14] -->
m

<!-- b005261 | prose | pages [14] -->
m

<!-- b005262 | prose | pages [14] -->
m

<!-- b005263 | prose | pages [14] -->
m

<!-- b005264 | prose | pages [14] -->
m

<!-- b005265 | prose | pages [14] -->
m

<!-- b005266 | prose | pages [14] -->
m

<!-- b005267 | prose | pages [14] -->
m

<!-- b005268 | prose | pages [14] -->
m

<!-- b005269 | prose | pages [14] -->
m

<!-- b005270 | prose | pages [14] -->
m

<!-- b005271 | prose | pages [14] -->
m

<!-- b005272 | prose | pages [14] -->
m

<!-- b005273 | prose | pages [14] -->
m

<!-- b005274 | prose | pages [14] -->
m

<!-- b005275 | prose | pages [14] -->
m

<!-- b005276 | prose | pages [14] -->
m

<!-- b005277 | prose | pages [14] -->
m

<!-- b005278 | prose | pages [14] -->
m

<!-- b005279 | prose | pages [14] -->
m

<!-- b005280 | prose | pages [14] -->
m

<!-- b005281 | prose | pages [14] -->
m

<!-- b005282 | prose | pages [14] -->
m

<!-- b005283 | prose | pages [14] -->
m

<!-- b005284 | prose | pages [14] -->
m

<!-- b005285 | prose | pages [14] -->
m

<!-- b005286 | prose | pages [14] -->
m

<!-- b005287 | prose | pages [14] -->
m

<!-- b005288 | prose | pages [14] -->
m

<!-- b005289 | prose | pages [14] -->
m

<!-- b005290 | prose | pages [14] -->
m

<!-- b005291 | prose | pages [14] -->
m

<!-- b005292 | prose | pages [14] -->
m

<!-- b005293 | prose | pages [14] -->
m

<!-- b005294 | prose | pages [14] -->
m

<!-- b005295 | prose | pages [14] -->
m

<!-- b005296 | prose | pages [14] -->
m

<!-- b005297 | prose | pages [14] -->
m

<!-- b005298 | prose | pages [14] -->
m

<!-- b005299 | prose | pages [14] -->
m

<!-- b005300 | prose | pages [14] -->
m

<!-- b005301 | prose | pages [14] -->
m

<!-- b005302 | prose | pages [14] -->
m

<!-- b005303 | prose | pages [14] -->
m

<!-- b005304 | prose | pages [14] -->
m

<!-- b005305 | prose | pages [14] -->
m

<!-- b005306 | prose | pages [14] -->
m

<!-- b005307 | prose | pages [14] -->
m

<!-- b005308 | prose | pages [14] -->
m

<!-- b005309 | prose | pages [14] -->
m

<!-- b005310 | prose | pages [14] -->
m

<!-- b005311 | prose | pages [14] -->
m

<!-- b005312 | prose | pages [14] -->
m

<!-- b005313 | prose | pages [14] -->
m

<!-- b005314 | prose | pages [14] -->
m

<!-- b005315 | prose | pages [14] -->
m

<!-- b005316 | prose | pages [14] -->
m

<!-- b005317 | prose | pages [14] -->
m

<!-- b005318 | prose | pages [14] -->
m

<!-- b005319 | prose | pages [14] -->
m

<!-- b005320 | prose | pages [14] -->
m

<!-- b005321 | prose | pages [14] -->
m

<!-- b005322 | prose | pages [14] -->
m

<!-- b005323 | prose | pages [14] -->
m

<!-- b005324 | prose | pages [14] -->
m

<!-- b005325 | prose | pages [14] -->
m

<!-- b005326 | prose | pages [14] -->
m

<!-- b005327 | prose | pages [14] -->
m

<!-- b005328 | prose | pages [14] -->
m

<!-- b005329 | prose | pages [14] -->
m

<!-- b005330 | prose | pages [14] -->
m

<!-- b005331 | prose | pages [14] -->
m

<!-- b005332 | prose | pages [14] -->
m

<!-- b005333 | prose | pages [14] -->
m

<!-- b005334 | prose | pages [14] -->
m

<!-- b005335 | prose | pages [14] -->
m

<!-- b005336 | prose | pages [14] -->
m

<!-- b005337 | prose | pages [14] -->
m

<!-- b005338 | prose | pages [14] -->
m

<!-- b005339 | prose | pages [14] -->
m

<!-- b005340 | prose | pages [14] -->
m

<!-- b005341 | prose | pages [14] -->
m

<!-- b005342 | prose | pages [14] -->
m

<!-- b005343 | prose | pages [14] -->
m

<!-- b005344 | prose | pages [14] -->
m

<!-- b005345 | prose | pages [14] -->
m

<!-- b005346 | prose | pages [14] -->
m

<!-- b005347 | prose | pages [14] -->
m

<!-- b005348 | prose | pages [14] -->
m

<!-- b005349 | prose | pages [14] -->
m

<!-- b005350 | prose | pages [14] -->
m

<!-- b005351 | prose | pages [14] -->
m

<!-- b005352 | prose | pages [14] -->
m

<!-- b005353 | prose | pages [14] -->
m

<!-- b005354 | prose | pages [14] -->
m

<!-- b005355 | prose | pages [14] -->
m

<!-- b005356 | prose | pages [14] -->
m

<!-- b005357 | prose | pages [14] -->
m

<!-- b005358 | prose | pages [14] -->
m

<!-- b005359 | prose | pages [14] -->
m

<!-- b005360 | prose | pages [14] -->
m

<!-- b005361 | prose | pages [14] -->
m

<!-- b005362 | prose | pages [14] -->
m

<!-- b005363 | prose | pages [14] -->
m

<!-- b005364 | prose | pages [14] -->
m

<!-- b005365 | prose | pages [14] -->
m

<!-- b005366 | prose | pages [14] -->
m

<!-- b005367 | prose | pages [14] -->
m

<!-- b005368 | prose | pages [14] -->
m

<!-- b005369 | prose | pages [14] -->
m

<!-- b005370 | prose | pages [14] -->
m

<!-- b005371 | prose | pages [14] -->
m

<!-- b005372 | prose | pages [14] -->
m

<!-- b005373 | prose | pages [14] -->
m

<!-- b005374 | prose | pages [14] -->
m

<!-- b005375 | prose | pages [14] -->
m

<!-- b005376 | prose | pages [14] -->
m

<!-- b005377 | prose | pages [14] -->
m

<!-- b005378 | prose | pages [14] -->
m

<!-- b005379 | prose | pages [14] -->
m

<!-- b005380 | prose | pages [14] -->
m

<!-- b005381 | prose | pages [14] -->
m

<!-- b005382 | prose | pages [14] -->
m

<!-- b005383 | prose | pages [14] -->
m

<!-- b005384 | prose | pages [14] -->
m

<!-- b005385 | prose | pages [14] -->
m

<!-- b005386 | prose | pages [14] -->
m

<!-- b005387 | prose | pages [14] -->
m

<!-- b005388 | prose | pages [14] -->
m

<!-- b005389 | prose | pages [14] -->
m

<!-- b005390 | prose | pages [14] -->
m

<!-- b005391 | prose | pages [14] -->
m

<!-- b005392 | prose | pages [14] -->
m

<!-- b005393 | prose | pages [14] -->
m

<!-- b005394 | prose | pages [14] -->
m

<!-- b005395 | prose | pages [14] -->
m

<!-- b005396 | prose | pages [14] -->
m

<!-- b005397 | prose | pages [14] -->
m

<!-- b005398 | prose | pages [14] -->
m

<!-- b005399 | prose | pages [14] -->
m

<!-- b005400 | prose | pages [14] -->
m

<!-- b005401 | prose | pages [14] -->
m

<!-- b005402 | prose | pages [14] -->
m

<!-- b005403 | prose | pages [14] -->
m

<!-- b005404 | prose | pages [14] -->
m

<!-- b005405 | prose | pages [14] -->
m

<!-- b005406 | prose | pages [14] -->
m

<!-- b005407 | prose | pages [14] -->
m

<!-- b005408 | prose | pages [14] -->
m

<!-- b005409 | prose | pages [14] -->
m

<!-- b005410 | prose | pages [14] -->
m

<!-- b005411 | prose | pages [14] -->
m

<!-- b005412 | prose | pages [14] -->
m

<!-- b005413 | prose | pages [14] -->
m

<!-- b005414 | prose | pages [14] -->
m

<!-- b005415 | prose | pages [14] -->
m

<!-- b005416 | prose | pages [14] -->
m

<!-- b005417 | prose | pages [14] -->
m

<!-- b005418 | prose | pages [14] -->
m

<!-- b005419 | prose | pages [14] -->
m

<!-- b005420 | prose | pages [14] -->
m

<!-- b005421 | prose | pages [14] -->
m

<!-- b005422 | prose | pages [14] -->
m

<!-- b005423 | prose | pages [14] -->
m

<!-- b005424 | prose | pages [14] -->
m

<!-- b005425 | prose | pages [14] -->
m

<!-- b005426 | prose | pages [14] -->
m

<!-- b005427 | prose | pages [14] -->
m

<!-- b005428 | prose | pages [14] -->
m

<!-- b005429 | prose | pages [14] -->
m

<!-- b005430 | prose | pages [14] -->
m

<!-- b005431 | prose | pages [14] -->
m

<!-- b005432 | prose | pages [14] -->
m

<!-- b005433 | prose | pages [14] -->
m

<!-- b005434 | prose | pages [14] -->
m

<!-- b005435 | prose | pages [14] -->
m

<!-- b005436 | prose | pages [14] -->
m

<!-- b005437 | caption | pages [14] -->
Figure 10: Top 10 of predicted 2028 medal

<!-- b005438 | prose | pages [14] -->
m

<!-- b005439 | prose | pages [14] -->
m

<!-- b005440 | prose | pages [14] -->
m

<!-- b005441 | prose | pages [14] -->
m

<!-- b005442 | prose | pages [14] -->
m

<!-- b005443 | prose | pages [14] -->
m

<!-- b005444 | prose | pages [14] -->
m

<!-- b005445 | prose | pages [14] -->
m

<!-- b005446 | prose | pages [14] -->
m

<!-- b005447 | prose | pages [14] -->
m

<!-- b005448 | prose | pages [14] -->
m

<!-- b005449 | prose | pages [14] -->
m

<!-- b005450 | prose | pages [14] -->
m

<!-- b005451 | prose | pages [14] -->
m

<!-- b005452 | prose | pages [14] -->
m

<!-- b005453 | prose | pages [14] -->
m

<!-- b005454 | prose | pages [14] -->
m

<!-- b005455 | prose | pages [14] -->
m

<!-- b005456 | prose | pages [14] -->
m

<!-- b005457 | prose | pages [14] -->
m

<!-- b005458 | prose | pages [14] -->
m

<!-- b005459 | prose | pages [14] -->
m

<!-- b005460 | prose | pages [14] -->
m

<!-- b005461 | prose | pages [14] -->
m

<!-- b005462 | prose | pages [14] -->
m

<!-- b005463 | prose | pages [14] -->
m

<!-- b005464 | prose | pages [14] -->
m

<!-- b005465 | prose | pages [14] -->
m

<!-- b005466 | prose | pages [14] -->
m

<!-- b005467 | prose | pages [14] -->
m

<!-- b005468 | prose | pages [14] -->
m

<!-- b005469 | prose | pages [14] -->
m

<!-- b005470 | prose | pages [14] -->
m

<!-- b005471 | prose | pages [14] -->
m

<!-- b005472 | prose | pages [14] -->
m

<!-- b005473 | prose | pages [14] -->
m

<!-- b005474 | prose | pages [14] -->
m

<!-- b005475 | prose | pages [14] -->
m

<!-- b005476 | prose | pages [14] -->
m

<!-- b005477 | prose | pages [14] -->
m

<!-- b005478 | prose | pages [14] -->
m

<!-- b005479 | prose | pages [14] -->
m

<!-- b005480 | prose | pages [14] -->
m

<!-- b005481 | prose | pages [14] -->
m

<!-- b005482 | prose | pages [14] -->
m

<!-- b005483 | prose | pages [14] -->
m

<!-- b005484 | prose | pages [14] -->
m

<!-- b005485 | prose | pages [14] -->
m

<!-- b005486 | prose | pages [14] -->
m

<!-- b005487 | prose | pages [14] -->
m

<!-- b005488 | prose | pages [14] -->
m

<!-- b005489 | prose | pages [14] -->
m

<!-- b005490 | prose | pages [14] -->
m

<!-- b005491 | prose | pages [14] -->
m

<!-- b005492 | prose | pages [14] -->
m

<!-- b005493 | prose | pages [14] -->
m

<!-- b005494 | prose | pages [14] -->
m

<!-- b005495 | prose | pages [14] -->
m

<!-- b005496 | prose | pages [14] -->
m

<!-- b005497 | prose | pages [14] -->
m

<!-- b005498 | prose | pages [14] -->
m

<!-- b005499 | prose | pages [14] -->
m

<!-- b005500 | prose | pages [14] -->
m

<!-- b005501 | prose | pages [14] -->
m

<!-- b005502 | prose | pages [14] -->
m

<!-- b005503 | prose | pages [14] -->
m

<!-- b005504 | prose | pages [14] -->
m

<!-- b005505 | prose | pages [14] -->
m

<!-- b005506 | prose | pages [14] -->
m

<!-- b005507 | prose | pages [14] -->
m

<!-- b005508 | prose | pages [14] -->
m

<!-- b005509 | prose | pages [14] -->
m

<!-- b005510 | prose | pages [14] -->
m

<!-- b005511 | prose | pages [14] -->
m

<!-- b005512 | prose | pages [14] -->
m

<!-- b005513 | prose | pages [14] -->
m

<!-- b005514 | prose | pages [14] -->
m

<!-- b005515 | prose | pages [14] -->
m

<!-- b005516 | prose | pages [14] -->
m

<!-- b005517 | prose | pages [14] -->
m

<!-- b005518 | prose | pages [14] -->
m

<!-- b005519 | prose | pages [14] -->
m

<!-- b005520 | prose | pages [14] -->
m

<!-- b005521 | prose | pages [14] -->
m

<!-- b005522 | prose | pages [14] -->
m

<!-- b005523 | prose | pages [14] -->
m

<!-- b005524 | prose | pages [14] -->
m

<!-- b005525 | prose | pages [14] -->
m

<!-- b005526 | prose | pages [14] -->
m

<!-- b005527 | prose | pages [14] -->
m

<!-- b005528 | prose | pages [14] -->
m

<!-- b005529 | prose | pages [14] -->
m

<!-- b005530 | prose | pages [14] -->
m

<!-- b005531 | prose | pages [14] -->
m

<!-- b005532 | prose | pages [14] -->
m

<!-- b005533 | prose | pages [14] -->
m

<!-- b005534 | prose | pages [14] -->
m

<!-- b005535 | prose | pages [14] -->
m

<!-- b005536 | prose | pages [14] -->
m

<!-- b005537 | prose | pages [14] -->
m

<!-- b005538 | prose | pages [14] -->
m

<!-- b005539 | prose | pages [14] -->
m

<!-- b005540 | prose | pages [14] -->
m

<!-- b005541 | prose | pages [14] -->
m

<!-- b005542 | prose | pages [14] -->
m

<!-- b005543 | prose | pages [14] -->
m

<!-- b005544 | prose | pages [14] -->
m

<!-- b005545 | prose | pages [14] -->
m

<!-- b005546 | prose | pages [14] -->
m

<!-- b005547 | prose | pages [14] -->
m

<!-- b005548 | prose | pages [14] -->
m

<!-- b005549 | prose | pages [14] -->
m

<!-- b005550 | prose | pages [14] -->
m

<!-- b005551 | prose | pages [14] -->
m

<!-- b005552 | prose | pages [14] -->
m

<!-- b005553 | prose | pages [14] -->
m

<!-- b005554 | prose | pages [14] -->
m

<!-- b005555 | prose | pages [14] -->
m

<!-- b005556 | prose | pages [14] -->
m

<!-- b005557 | prose | pages [14] -->
m

<!-- b005558 | prose | pages [14] -->
m

<!-- b005559 | prose | pages [14] -->
m

<!-- b005560 | prose | pages [14] -->
m

<!-- b005561 | prose | pages [14] -->
m

<!-- b005562 | prose | pages [14] -->
m

<!-- b005563 | prose | pages [14] -->
m

<!-- b005564 | prose | pages [14] -->
m

<!-- b005565 | prose | pages [14] -->
m

<!-- b005566 | prose | pages [14] -->
m

<!-- b005567 | prose | pages [14] -->
m

<!-- b005568 | prose | pages [14] -->
m

<!-- b005569 | prose | pages [14] -->
m

<!-- b005570 | prose | pages [14] -->
m

<!-- b005571 | prose | pages [14] -->
m

<!-- b005572 | prose | pages [14] -->
m

<!-- b005573 | prose | pages [14] -->
m

<!-- b005574 | prose | pages [14] -->
m

<!-- b005575 | prose | pages [14] -->
m

<!-- b005576 | prose | pages [14] -->
m

<!-- b005577 | prose | pages [14] -->
m

<!-- b005578 | prose | pages [14] -->
m

<!-- b005579 | prose | pages [14] -->
m

<!-- b005580 | prose | pages [14] -->
m

<!-- b005581 | prose | pages [14] -->
m

<!-- b005582 | prose | pages [14] -->
m

<!-- b005583 | prose | pages [14] -->
m

<!-- b005584 | prose | pages [14] -->
m

<!-- b005585 | prose | pages [14] -->
m

<!-- b005586 | prose | pages [14] -->
m

<!-- b005587 | prose | pages [14] -->
m

<!-- b005588 | prose | pages [14] -->
m

<!-- b005589 | prose | pages [14] -->
m

<!-- b005590 | prose | pages [14] -->
m

<!-- b005591 | prose | pages [14] -->
table with host country effect

<!-- b005592 | prose | pages [14] -->
m

<!-- b005593 | prose | pages [14] -->
m

<!-- b005594 | prose | pages [14] -->
m

<!-- b005595 | prose | pages [14] -->
m

<!-- b005596 | prose | pages [14] -->
m

<!-- b005597 | prose | pages [14] -->
m

<!-- b005598 | prose | pages [14] -->
m

<!-- b005599 | prose | pages [14] -->
m

<!-- b005600 | prose | pages [14] -->
m

<!-- b005601 | prose | pages [14] -->
m

<!-- b005602 | prose | pages [14] -->
m

<!-- b005603 | prose | pages [14] -->
m

<!-- b005604 | prose | pages [14] -->
m

<!-- b005605 | prose | pages [14] -->
m

<!-- b005606 | prose | pages [14] -->
m

<!-- b005607 | prose | pages [14] -->
m

<!-- b005608 | prose | pages [14] -->
m

<!-- b005609 | prose | pages [14] -->
m

<!-- b005610 | prose | pages [14] -->
m

<!-- b005611 | prose | pages [14] -->
m

<!-- b005612 | prose | pages [14] -->
m

<!-- b005613 | prose | pages [14] -->
m

<!-- b005614 | prose | pages [14] -->
m

<!-- b005615 | prose | pages [14] -->
m

<!-- b005616 | prose | pages [14] -->
m

<!-- b005617 | prose | pages [14] -->
m

<!-- b005618 | prose | pages [14] -->
m

<!-- b005619 | prose | pages [14] -->
m

<!-- b005620 | prose | pages [14] -->
m

<!-- b005621 | prose | pages [14] -->
m

<!-- b005622 | prose | pages [14] -->
m

<!-- b005623 | prose | pages [14] -->
m

<!-- b005624 | prose | pages [14] -->
m

<!-- b005625 | prose | pages [14] -->
m

<!-- b005626 | prose | pages [14] -->
m

<!-- b005627 | prose | pages [14] -->
m

<!-- b005628 | prose | pages [14] -->
m

<!-- b005629 | prose | pages [14] -->
m

<!-- b005630 | prose | pages [14] -->
m

<!-- b005631 | prose | pages [14] -->
m

<!-- b005632 | prose | pages [14] -->
m

<!-- b005633 | prose | pages [14] -->
m

<!-- b005634 | prose | pages [14] -->
m

<!-- b005635 | prose | pages [14] -->
m

<!-- b005636 | prose | pages [14] -->
m

<!-- b005637 | prose | pages [14] -->
m

<!-- b005638 | prose | pages [14] -->
m

<!-- b005639 | prose | pages [14] -->
m

<!-- b005640 | prose | pages [14] -->
m

<!-- b005641 | prose | pages [14] -->
m

<!-- b005642 | prose | pages [14] -->
m

<!-- b005643 | prose | pages [14] -->
m

<!-- b005644 | prose | pages [14] -->
m

<!-- b005645 | prose | pages [14] -->
m

<!-- b005646 | prose | pages [14] -->
m

<!-- b005647 | prose | pages [14] -->
m

<!-- b005648 | prose | pages [14] -->
m

<!-- b005649 | prose | pages [14] -->
m

<!-- b005650 | prose | pages [14] -->
m

<!-- b005651 | prose | pages [14] -->
m

<!-- b005652 | prose | pages [14] -->
m

<!-- b005653 | prose | pages [14] -->
m

<!-- b005654 | prose | pages [14] -->
m

<!-- b005655 | prose | pages [14] -->
m

<!-- b005656 | prose | pages [14] -->
m

<!-- b005657 | prose | pages [14] -->
m

<!-- b005658 | prose | pages [14] -->
m

<!-- b005659 | prose | pages [14] -->
m

<!-- b005660 | prose | pages [14] -->
m

<!-- b005661 | prose | pages [14] -->
m

<!-- b005662 | prose | pages [14] -->
m

<!-- b005663 | prose | pages [14] -->
m

<!-- b005664 | prose | pages [14] -->
m

<!-- b005665 | prose | pages [14] -->
m

<!-- b005666 | prose | pages [14] -->
m

<!-- b005667 | prose | pages [14] -->
m

<!-- b005668 | prose | pages [14] -->
m

<!-- b005669 | prose | pages [14] -->
m

<!-- b005670 | prose | pages [14] -->
m

<!-- b005671 | prose | pages [14] -->
m

<!-- b005672 | prose | pages [14] -->
m

<!-- b005673 | prose | pages [14] -->
m

<!-- b005674 | prose | pages [14] -->
m

<!-- b005675 | prose | pages [14] -->
m

<!-- b005676 | prose | pages [14] -->
m

<!-- b005677 | prose | pages [14] -->
m

<!-- b005678 | prose | pages [14] -->
m

<!-- b005679 | prose | pages [14] -->
m

<!-- b005680 | prose | pages [14] -->
m

<!-- b005681 | prose | pages [14] -->
m

<!-- b005682 | prose | pages [14] -->
m

<!-- b005683 | prose | pages [14] -->
m

<!-- b005684 | prose | pages [14] -->
m

<!-- b005685 | prose | pages [14] -->
m

<!-- b005686 | prose | pages [14] -->
m

<!-- b005687 | prose | pages [14] -->
m

<!-- b005688 | prose | pages [14] -->
m

<!-- b005689 | prose | pages [14] -->
m

<!-- b005690 | prose | pages [14] -->
m

<!-- b005691 | prose | pages [14] -->
m

<!-- b005692 | prose | pages [14] -->
m

<!-- b005693 | prose | pages [14] -->
m

<!-- b005694 | prose | pages [14] -->
m

<!-- b005695 | prose | pages [14] -->
m

<!-- b005696 | prose | pages [14] -->
m

<!-- b005697 | prose | pages [14] -->
m

<!-- b005698 | prose | pages [14] -->
m

<!-- b005699 | prose | pages [14] -->
m

<!-- b005700 | prose | pages [14] -->
m

<!-- b005701 | prose | pages [14] -->
m

<!-- b005702 | prose | pages [14] -->
m

<!-- b005703 | prose | pages [14] -->
m

<!-- b005704 | prose | pages [14] -->
m

<!-- b005705 | prose | pages [14] -->
m

<!-- b005706 | prose | pages [14] -->
m

<!-- b005707 | prose | pages [14] -->
m

<!-- b005708 | prose | pages [14] -->
m

<!-- b005709 | prose | pages [14] -->
m

<!-- b005710 | prose | pages [14] -->
m

<!-- b005711 | prose | pages [14] -->
m

<!-- b005712 | prose | pages [14] -->
m

<!-- b005713 | prose | pages [14] -->
m

<!-- b005714 | prose | pages [14] -->
m

<!-- b005715 | prose | pages [14] -->
m

<!-- b005716 | prose | pages [14] -->
m

<!-- b005717 | prose | pages [14] -->
m

<!-- b005718 | prose | pages [14] -->
m

<!-- b005719 | prose | pages [14] -->
m

<!-- b005720 | prose | pages [14] -->
m

<!-- b005721 | prose | pages [14] -->
m

<!-- b005722 | prose | pages [14] -->
m

<!-- b005723 | prose | pages [14] -->
m

<!-- b005724 | prose | pages [14] -->
m

<!-- b005725 | prose | pages [14] -->
m

<!-- b005726 | prose | pages [14] -->
m

<!-- b005727 | prose | pages [14] -->
m

<!-- b005728 | prose | pages [14] -->
m

<!-- b005729 | prose | pages [14] -->
m

<!-- b005730 | prose | pages [14] -->
m

<!-- b005731 | prose | pages [14] -->
m

<!-- b005732 | prose | pages [14] -->
m

<!-- b005733 | prose | pages [14] -->
m

<!-- b005734 | prose | pages [14] -->
m

<!-- b005735 | prose | pages [14] -->
m

<!-- b005736 | prose | pages [14] -->
m

<!-- b005737 | prose | pages [14] -->
m

<!-- b005738 | prose | pages [14] -->
m

<!-- b005739 | prose | pages [14] -->
m

<!-- b005740 | prose | pages [14] -->
m

<!-- b005741 | prose | pages [14] -->
m

<!-- b005742 | prose | pages [14] -->
m

<!-- b005743 | prose | pages [14] -->
m

<!-- b005744 | prose | pages [14] -->
m

<!-- b005745 | prose | pages [14] -->
m

<!-- b005746 | prose | pages [14] -->
m

<!-- b005747 | prose | pages [14] -->
m

<!-- b005748 | prose | pages [14] -->
m

<!-- b005749 | prose | pages [14] -->
m

<!-- b005750 | prose | pages [14] -->
m

<!-- b005751 | prose | pages [14] -->
m

<!-- b005752 | prose | pages [14] -->
m

<!-- b005753 | prose | pages [14] -->
m

<!-- b005754 | prose | pages [14] -->
m

<!-- b005755 | prose | pages [14] -->
m

<!-- b005756 | prose | pages [14] -->
m

<!-- b005757 | prose | pages [14] -->
m

<!-- b005758 | prose | pages [14] -->
m

<!-- b005759 | prose | pages [14] -->
m

<!-- b005760 | prose | pages [14] -->
m

<!-- b005761 | prose | pages [14] -->
m

<!-- b005762 | prose | pages [14] -->
m

<!-- b005763 | prose | pages [14] -->
m

<!-- b005764 | prose | pages [14] -->
m

<!-- b005765 | prose | pages [14] -->
m

<!-- b005766 | prose | pages [14] -->
m

<!-- b005767 | prose | pages [14] -->
m

<!-- b005768 | prose | pages [14] -->
m

<!-- b005769 | prose | pages [14] -->
m

<!-- b005770 | prose | pages [14] -->
m

<!-- b005771 | prose | pages [14] -->
m

<!-- b005772 | prose | pages [14] -->
m

<!-- b005773 | prose | pages [14] -->
m

<!-- b005774 | prose | pages [14] -->
m

<!-- b005775 | prose | pages [14] -->
m

<!-- b005776 | prose | pages [14] -->
m

<!-- b005777 | prose | pages [14] -->
m

<!-- b005778 | prose | pages [14] -->
statistics. The confidence interval provides a range within which we can say with certainty that the population parameter is included, usually at a 95% level. For this problem, we predicted the number of gold medals for each country in 2024, and compared it with the actual gold medal results of each country in 2024, we can calculate the mean and standard deviation of the residuals of the gold medal results in 2024.

<!-- b005779 | prose | pages [14] -->
¯e = 1

<!-- b005780 | prose | pages [14] -->
v u 1 u

<!-- b005781 | prose | pages [14] -->
σe =

<!-- b005782 | prose | pages [14] -->
t n −1

<!-- b005783 | prose | pages [14] -->
n X

<!-- b005784 | prose | pages [14] -->
ei (10)

<!-- b005785 | prose | pages [14] -->
n n

<!-- b005786 | prose | pages [14] -->
i=1

<!-- b005787 | prose | pages [14] -->
n X

<!-- b005788 | prose | pages [14] -->
(ei −¯e)2 (11)

<!-- b005789 | prose | pages [14] -->
i=1

<!-- b005790 | prose | pages [14] -->
Assuming that the residuals ei follows a normal distribution N(¯e, σ2

<!-- b005791 | prose | pages [14] -->
e), we can use the properties of the normal distribution to calculate the prediction intervals at different confidence levels. For a given confidence level α (for example, 95%), the corresponding z-score zα/2 can be found (for a 95% confidence level, z0.025 ≈1.96). For each predicted value ˆyi, its prediction interval can be expressed as:

<!-- b005792 | prose | pages [14] -->
 

<!-- b005793 | prose | pages [14] -->


<!-- b005794 | prose | pages [14] -->
ˆyi −zα/2 · σe, ˆyi + zα/2 · σe

<!-- b005795 | prose | pages [14] -->
(12)

<!-- b005796 | prose | pages [14] -->
As shown in the Fig. 11, the pink dots represent the estimates of the number of gold medals for the top 9 countries in the 2024 Olympics, predicted by the XGBoost model with France as the host country in 2024. These are the predicted values for the number of gold medals for each country in 2024. Since we already knew the actual number of gold medals for each country in 2024, we can calculate the standard deviation of the residuals between the predicted and actual values. By combining the Z-score for a 95% confidence interval, we can calculate the upper and lower bounds of the 95% confidence interval for the prediction interval, as shown by the lavender legend in the figure.

<!-- b005797 | prose | pages [14] -->
A Mann-Kendall-based analysis to project significant change in medal 5.6 acquisition

<!-- b005798 | prose | pages [14] -->
Mann-Kendall test, a non-parametric method for identifying trends in time series data, is used to analyze the performance of each country in the past 5 Olympic Games [9]. The aim is to forecast which nations will exhibit substantial fluctuations in their medal tallies.

<!-- b005799 | prose | pages [14] -->
For a specific country’s time series of Olympic medal counts X = {x1, x2, ..., xn}, Mann-

<!-- b005800 | prose | pages [14] -->
关注数学模型

<!-- b005801 | furniture | pages [14] -->
2

<!-- b005802 | furniture | pages [14] -->
MATHmodels

<!-- b005803 | furniture | pages [14] -->
获取更多资讯

<!-- b005804 | furniture | pages [15] -->
Team # 2514461

<!-- b005805 | furniture | pages [15] -->
Page 14 of 25

<!-- b005806 | prose | pages [15] -->
微信公众号：数学模型

<!-- b005807 | prose | pages [15] -->
微信号：MATHmodels

<!-- b005808 | caption | pages [15] -->
Figure 11: Taking the 2024 gold medal predictions as an example, the confidence interval of

<!-- b005809 | prose | pages [15] -->
the XGBoost model is analyzed.

<!-- b005810 | prose | pages [15] -->
Kendall test first calculate the S statistic:

<!-- b005811 | prose | pages [15] -->
n−1

<!-- b005812 | prose | pages [15] -->
n

<!-- b005813 | prose | pages [15] -->
X

<!-- b005814 | prose | pages [15] -->
X

<!-- b005815 | prose | pages [15] -->
S =

<!-- b005816 | prose | pages [15] -->
i=1

<!-- b005817 | prose | pages [15] -->
j=i+1

<!-- b005818 | prose | pages [15] -->
where sgn() is the sign function.

<!-- b005819 | prose | pages [15] -->
sgn(xj −xi) (13)

<!-- b005820 | prose | pages [15] -->
When there are ties in the data (i.e., repeated values), the variance of the S statistic needs to be adjusted. The variance of S is calculated as:

<!-- b005821 | prose | pages [15] -->
V ar(S) = n(n −1)(2n + 5) −Pm

<!-- b005822 | prose | pages [15] -->
i=1 ti(ti −1)(2ti + 5) (14) 18

<!-- b005823 | prose | pages [15] -->
where m is the number of unique values in the data and ti is the number of times the ith unique value appears.

<!-- b005824 | prose | pages [15] -->
To standardize the S statistic, a Z statistic is calculated as:

<!-- b005825 | prose | pages [15] -->
Z = [S −E(S)] p

<!-- b005826 | prose | pages [15] -->
(15)

<!-- b005827 | prose | pages [15] -->
V ar(S)

<!-- b005828 | prose | pages [15] -->
where E(S) is the expected value of S. For a trend-free time series, E(S) is typically close to 0. Then, assuming that the z-value follows a standard normal distribution, we can perform a p-parameter test on the z-value that follows a standard normal distribution to identify data with a p-value less than 0.05, which allows us to determine whether there is a significant upward or downward trend.

<!-- b005829 | prose | pages [15] -->
(

<!-- b005830 | prose | pages [15] -->
if (z > 0) may improve

<!-- b005831 | prose | pages [15] -->
if p < 0.05

<!-- b005832 | prose | pages [15] -->
if (z < 0) may worse

<!-- b005833 | furniture | pages [16] -->
Team # 2514461

<!-- b005834 | furniture | pages [16] -->
Page 15 of 25

<!-- b005835 | prose | pages [16] -->
Based on the analysis of the past twenty years, that is, the performance of the past five Olympic Games, we analyzed whether these countries would have a significantly better or worse performance in the 2028 Olympic Games. Since we considered that data from 20 years ago has less impact on the next Olympic Games than data from the past 20 years, which can better reflect the trend of a country’s Olympic level in recent years.

<!-- b005836 | prose | pages [16] -->
We converted the gold, silver, and bronze medals of the countries in the past five Olympic Games into scores. Then we used the Mann-Kendall model to analyze the upward and downward trends of the countries. Finally, it is analyzed that four countries have a significant trend of improvement: NZL, ITA, NED, SWE, and one country has a significant downward trend, which is BLR.

<!-- b005837 | caption | pages [16] -->
Figure 12: The scores of countries with obvious upward or downward trend in the past 5

<!-- b005838 | prose | pages [16] -->
Olympic Games

<!-- b005839 | heading | pages [16] -->
Model III: First-time Medalist Prediction based on Cox

<!-- b005840 | prose | pages [16] -->
6

<!-- b005841 | heading | pages [16] -->
Proportional Hazard Model

<!-- b005842 | prose | pages [16] -->
6.1

<!-- b005843 | heading | pages [16] -->
Model Overview

<!-- b005844 | prose | pages [16] -->
This part utilizes a Cox proportional hazards model to predict the probability of a country winning its first Olympic medal. Key predictors taken into account include the number of athletes developed, Olympic participation history, and the diversity of sports culture.

<!-- b005845 | prose | pages [16] -->
The model treats a country’s journey towards its first medal as a survival process, excluding data from countries that have already won medals. By fitting the model and conducting Monte Carlo simulations, we predicted the potential number of first-time medalists by 2028.

<!-- b005846 | prose | pages [16] -->
6.2 Theoretical Basis

<!-- b005847 | prose | pages [16] -->
The objective of Cox proportional hazard model is to estimate the hazard function, which represents the instantaneous risk of an event occurring at a specific time, given a set of predictor variables. It incorporates the proportional hazards assumption, which posits that the hazard ratios between any two individuals remain constant over time. Here, we can conceptualize probability for countries to picking up their very first medal as a measure of risk. The model utilizes a semi-parametric approach, modeling the baseline hazard function non-parametrically

<!-- b005848 | prose | pages [16] -->
关注数学模型

<!-- b005849 | furniture | pages [16] -->
2

<!-- b005850 | furniture | pages [16] -->
MATHmodels

<!-- b005851 | furniture | pages [16] -->
获取更多资讯

<!-- b005852 | furniture | pages [17] -->
Team # 2514461

<!-- b005853 | furniture | pages [17] -->
Page 16 of 25

<!-- b005854 | prose | pages [17] -->
while estimating the effects of predictor variables through coefficients in a linear predictor. This approach allows for flexibility in capturing complex relationships between covariates and the risk of the event.

<!-- b005855 | prose | pages [17] -->
微信公众号：数学模型

<!-- b005856 | prose | pages [17] -->
6.3 Key Predictors of First-time Medalists

<!-- b005857 | prose | pages [17] -->
For countries that have yet to earn medals, their chance to make a landmark moment can be derived according to the features listed as below:

<!-- b005858 | prose | pages [17] -->
• Quantity of athletes developed The total number of athletes a country has sent to the Games through history is a strong indicator of its sports development levels, reflecting the depth and breadth of its sports talent pool.

<!-- b005859 | prose | pages [17] -->
• Olympic participation history How many times a nation has participated in the Olympics

<!-- b005860 | prose | pages [17] -->
微信号：MATHmodels

<!-- b005861 | prose | pages [17] -->
reflects its engagement with the global sporting community and experience in competing with other teams in such a grand sport event.

<!-- b005862 | prose | pages [17] -->
• Diversity of sports culture The number of event categories a country has participated in over the past Games showcases the abundance of coaching resources and how rich its sports culture is, also contributing to its medal prospects.

<!-- b005863 | prose | pages [17] -->
6.4

<!-- b005864 | heading | pages [17] -->
Model establishment

<!-- b005865 | prose | pages [17] -->
The moment a country makes its first breakthrough and graduates from the Olympic Village for newcomers represents the time when our event of interest occurs, similar to a risk event studied in clinical medicine. Based on the hazard function, we defined the probability for a country to win the first medal at the Games in year t as P(t). Given the covariates we have discussed above, a Cox model can be established to estimate the probability of a country achieving its first medal win at a specific time point.

<!-- b005866 | prose | pages [17] -->
P(t, X) = P0(t)eβaXa(t)+βpXp(t)+βeXe(t) (16)

<!-- b005867 | prose | pages [17] -->
Xa(t) is the total number of unique athletes registered for Olympics from the first Games in 1896 to the Games before year t. Xp(t) is the number of the country’s participations in Olympics. Xe(t) is the total number of unique events the country participated in from the first Games to the Games before year t. P0(t) is the baseline hazard function reflecting the risk of an event occurring in the absence of other risk factors, namely the probability for a country that has never competed in a single Olympic Games to win the first medal in year t.

<!-- b005868 | prose | pages [17] -->
6.5

<!-- b005869 | heading | pages [17] -->
Model Fitting and Prediction

<!-- b005870 | prose | pages [17] -->
The function P(t, X) aims to model the trend in first-medal-winning probability for countries and then predict this probability for a certain country based on its characteristics in a certain year. Therefore, the data we used for fitting is the feature vector X = [Xa(t), Xp(t), Xe(t)] of each country up to and including the year of its first medal win, namely the process of the country stays in Olympic Village for newcomers, rather than including the data after a country wins its first medal. So we marked countries that had already won medals in each Games and conduct a survival analysis, treating Year as duration time and winning as the event. After excluding the data of countries with prior wins, we fitted a model and successfully forecast the likelihood of first-time winning for various countries in a given year such as 2028.

<!-- b005871 | furniture | pages [18] -->
Team # 2514461

<!-- b005872 | prose | pages [18] -->
6.6 Monte Carlo Simulation

<!-- b005873 | prose | pages [18] -->
m

<!-- b005874 | prose | pages [18] -->
m

<!-- b005875 | prose | pages [18] -->
m

<!-- b005876 | prose | pages [18] -->
m

<!-- b005877 | prose | pages [18] -->
m

<!-- b005878 | prose | pages [18] -->
m

<!-- b005879 | prose | pages [18] -->
m

<!-- b005880 | prose | pages [18] -->
m

<!-- b005881 | prose | pages [18] -->
m

<!-- b005882 | prose | pages [18] -->
m

<!-- b005883 | prose | pages [18] -->
m

<!-- b005884 | prose | pages [18] -->
m

<!-- b005885 | prose | pages [18] -->
m

<!-- b005886 | prose | pages [18] -->
m

<!-- b005887 | prose | pages [18] -->
m

<!-- b005888 | prose | pages [18] -->
m

<!-- b005889 | prose | pages [18] -->
m

<!-- b005890 | prose | pages [18] -->
m

<!-- b005891 | prose | pages [18] -->
m

<!-- b005892 | prose | pages [18] -->
m

<!-- b005893 | prose | pages [18] -->
m

<!-- b005894 | prose | pages [18] -->
m

<!-- b005895 | prose | pages [18] -->
m

<!-- b005896 | prose | pages [18] -->
m

<!-- b005897 | prose | pages [18] -->
m

<!-- b005898 | prose | pages [18] -->
m

<!-- b005899 | prose | pages [18] -->
m

<!-- b005900 | prose | pages [18] -->
m

<!-- b005901 | prose | pages [18] -->
m

<!-- b005902 | prose | pages [18] -->
m

<!-- b005903 | prose | pages [18] -->
m

<!-- b005904 | prose | pages [18] -->
m

<!-- b005905 | prose | pages [18] -->
m

<!-- b005906 | prose | pages [18] -->
m

<!-- b005907 | prose | pages [18] -->
m

<!-- b005908 | prose | pages [18] -->
m

<!-- b005909 | prose | pages [18] -->
m

<!-- b005910 | prose | pages [18] -->
m

<!-- b005911 | prose | pages [18] -->
m

<!-- b005912 | prose | pages [18] -->
m

<!-- b005913 | prose | pages [18] -->
m

<!-- b005914 | prose | pages [18] -->
m

<!-- b005915 | prose | pages [18] -->
m

<!-- b005916 | prose | pages [18] -->
m

<!-- b005917 | prose | pages [18] -->
m

<!-- b005918 | prose | pages [18] -->
m

<!-- b005919 | prose | pages [18] -->
m

<!-- b005920 | prose | pages [18] -->
m

<!-- b005921 | prose | pages [18] -->
m

<!-- b005922 | prose | pages [18] -->
m

<!-- b005923 | prose | pages [18] -->
m

<!-- b005924 | prose | pages [18] -->
m

<!-- b005925 | prose | pages [18] -->
m

<!-- b005926 | prose | pages [18] -->
m

<!-- b005927 | prose | pages [18] -->
m

<!-- b005928 | prose | pages [18] -->
m

<!-- b005929 | prose | pages [18] -->
m

<!-- b005930 | prose | pages [18] -->
m

<!-- b005931 | prose | pages [18] -->
m

<!-- b005932 | prose | pages [18] -->
m

<!-- b005933 | prose | pages [18] -->
m

<!-- b005934 | prose | pages [18] -->
m

<!-- b005935 | prose | pages [18] -->
m

<!-- b005936 | prose | pages [18] -->
m

<!-- b005937 | prose | pages [18] -->
m

<!-- b005938 | prose | pages [18] -->
m

<!-- b005939 | prose | pages [18] -->
m

<!-- b005940 | prose | pages [18] -->
m

<!-- b005941 | prose | pages [18] -->
m

<!-- b005942 | prose | pages [18] -->
m

<!-- b005943 | prose | pages [18] -->
m

<!-- b005944 | prose | pages [18] -->
m

<!-- b005945 | prose | pages [18] -->
m

<!-- b005946 | furniture | pages [18] -->
Page 17 of 25

<!-- b005947 | prose | pages [18] -->
Since we assumed independence between countries’ probabilities of obtaining their first

<!-- b005948 | prose | pages [18] -->
m

<!-- b005949 | prose | pages [18] -->
m

<!-- b005950 | prose | pages [18] -->
m

<!-- b005951 | prose | pages [18] -->
m

<!-- b005952 | prose | pages [18] -->
m

<!-- b005953 | prose | pages [18] -->
m

<!-- b005954 | prose | pages [18] -->
m

<!-- b005955 | prose | pages [18] -->
m

<!-- b005956 | prose | pages [18] -->
m

<!-- b005957 | prose | pages [18] -->
m

<!-- b005958 | prose | pages [18] -->
m

<!-- b005959 | prose | pages [18] -->
m

<!-- b005960 | prose | pages [18] -->
m

<!-- b005961 | prose | pages [18] -->
m

<!-- b005962 | prose | pages [18] -->
m

<!-- b005963 | prose | pages [18] -->
m

<!-- b005964 | prose | pages [18] -->
m

<!-- b005965 | prose | pages [18] -->
m

<!-- b005966 | prose | pages [18] -->
m

<!-- b005967 | prose | pages [18] -->
m

<!-- b005968 | prose | pages [18] -->
m

<!-- b005969 | prose | pages [18] -->
m

<!-- b005970 | prose | pages [18] -->
m

<!-- b005971 | prose | pages [18] -->
m

<!-- b005972 | prose | pages [18] -->
m

<!-- b005973 | prose | pages [18] -->
m

<!-- b005974 | prose | pages [18] -->
m

<!-- b005975 | prose | pages [18] -->
m

<!-- b005976 | prose | pages [18] -->
m

<!-- b005977 | prose | pages [18] -->
m

<!-- b005978 | prose | pages [18] -->
m

<!-- b005979 | prose | pages [18] -->
m

<!-- b005980 | prose | pages [18] -->
m

<!-- b005981 | prose | pages [18] -->
m

<!-- b005982 | prose | pages [18] -->
m

<!-- b005983 | prose | pages [18] -->
m

<!-- b005984 | prose | pages [18] -->
m

<!-- b005985 | prose | pages [18] -->
m

<!-- b005986 | prose | pages [18] -->
m

<!-- b005987 | prose | pages [18] -->
m

<!-- b005988 | prose | pages [18] -->
m

<!-- b005989 | prose | pages [18] -->
m

<!-- b005990 | prose | pages [18] -->
m

<!-- b005991 | prose | pages [18] -->
m

<!-- b005992 | prose | pages [18] -->
m

<!-- b005993 | prose | pages [18] -->
m

<!-- b005994 | prose | pages [18] -->
m

<!-- b005995 | prose | pages [18] -->
m

<!-- b005996 | prose | pages [18] -->
m

<!-- b005997 | prose | pages [18] -->
m

<!-- b005998 | prose | pages [18] -->
m

<!-- b005999 | prose | pages [18] -->
m

<!-- b006000 | prose | pages [18] -->
m

<!-- b006001 | prose | pages [18] -->
m

<!-- b006002 | prose | pages [18] -->
m

<!-- b006003 | prose | pages [18] -->
m

<!-- b006004 | prose | pages [18] -->
m

<!-- b006005 | prose | pages [18] -->
m

<!-- b006006 | prose | pages [18] -->
m

<!-- b006007 | prose | pages [18] -->
m

<!-- b006008 | prose | pages [18] -->
m

<!-- b006009 | prose | pages [18] -->
m

<!-- b006010 | prose | pages [18] -->
m

<!-- b006011 | prose | pages [18] -->
m

<!-- b006012 | prose | pages [18] -->
m

<!-- b006013 | prose | pages [18] -->
m

<!-- b006014 | prose | pages [18] -->
m

<!-- b006015 | prose | pages [18] -->
m

<!-- b006016 | prose | pages [18] -->
m

<!-- b006017 | prose | pages [18] -->
m

<!-- b006018 | prose | pages [18] -->
m

<!-- b006019 | prose | pages [18] -->
m

<!-- b006020 | prose | pages [18] -->
m

<!-- b006021 | prose | pages [18] -->
m

<!-- b006022 | prose | pages [18] -->
m

<!-- b006023 | prose | pages [18] -->
m

<!-- b006024 | prose | pages [18] -->
m

<!-- b006025 | prose | pages [18] -->
m

<!-- b006026 | prose | pages [18] -->
m

<!-- b006027 | prose | pages [18] -->
m

<!-- b006028 | prose | pages [18] -->
m

<!-- b006029 | prose | pages [18] -->
m

<!-- b006030 | prose | pages [18] -->
m

<!-- b006031 | prose | pages [18] -->
m

<!-- b006032 | prose | pages [18] -->
m

<!-- b006033 | prose | pages [18] -->
m

<!-- b006034 | prose | pages [18] -->
m

<!-- b006035 | prose | pages [18] -->
m

<!-- b006036 | prose | pages [18] -->
m

<!-- b006037 | prose | pages [18] -->
m

<!-- b006038 | prose | pages [18] -->
m

<!-- b006039 | prose | pages [18] -->
m

<!-- b006040 | prose | pages [18] -->
m

<!-- b006041 | prose | pages [18] -->
m

<!-- b006042 | prose | pages [18] -->
m

<!-- b006043 | prose | pages [18] -->
m

<!-- b006044 | prose | pages [18] -->
m

<!-- b006045 | prose | pages [18] -->
m

<!-- b006046 | prose | pages [18] -->
m

<!-- b006047 | prose | pages [18] -->
m

<!-- b006048 | prose | pages [18] -->
m

<!-- b006049 | prose | pages [18] -->
m

<!-- b006050 | prose | pages [18] -->
m

<!-- b006051 | prose | pages [18] -->
m

<!-- b006052 | prose | pages [18] -->
m

<!-- b006053 | prose | pages [18] -->
m

<!-- b006054 | prose | pages [18] -->
m

<!-- b006055 | prose | pages [18] -->
m

<!-- b006056 | prose | pages [18] -->
m

<!-- b006057 | prose | pages [18] -->
m

<!-- b006058 | prose | pages [18] -->
m

<!-- b006059 | prose | pages [18] -->
m

<!-- b006060 | prose | pages [18] -->
m

<!-- b006061 | prose | pages [18] -->
m

<!-- b006062 | prose | pages [18] -->
m

<!-- b006063 | prose | pages [18] -->
m

<!-- b006064 | prose | pages [18] -->
m

<!-- b006065 | prose | pages [18] -->
m

<!-- b006066 | prose | pages [18] -->
m

<!-- b006067 | prose | pages [18] -->
m

<!-- b006068 | prose | pages [18] -->
m

<!-- b006069 | prose | pages [18] -->
m

<!-- b006070 | prose | pages [18] -->
m

<!-- b006071 | prose | pages [18] -->
m

<!-- b006072 | prose | pages [18] -->
m

<!-- b006073 | prose | pages [18] -->
m

<!-- b006074 | prose | pages [18] -->
m

<!-- b006075 | prose | pages [18] -->
m

<!-- b006076 | prose | pages [18] -->
m

<!-- b006077 | prose | pages [18] -->
m

<!-- b006078 | prose | pages [18] -->
m

<!-- b006079 | prose | pages [18] -->
m

<!-- b006080 | prose | pages [18] -->
m

<!-- b006081 | prose | pages [18] -->
m

<!-- b006082 | prose | pages [18] -->
m

<!-- b006083 | prose | pages [18] -->
m

<!-- b006084 | prose | pages [18] -->
medal, if we conducted n repeated Olympic trials in year t and Y represents the number of

<!-- b006085 | prose | pages [18] -->
m

<!-- b006086 | prose | pages [18] -->
m

<!-- b006087 | prose | pages [18] -->
m

<!-- b006088 | prose | pages [18] -->
m

<!-- b006089 | prose | pages [18] -->
m

<!-- b006090 | prose | pages [18] -->
m

<!-- b006091 | prose | pages [18] -->
m

<!-- b006092 | prose | pages [18] -->
m

<!-- b006093 | prose | pages [18] -->
m

<!-- b006094 | prose | pages [18] -->
m

<!-- b006095 | prose | pages [18] -->
m

<!-- b006096 | prose | pages [18] -->
m

<!-- b006097 | prose | pages [18] -->
m

<!-- b006098 | prose | pages [18] -->
m

<!-- b006099 | prose | pages [18] -->
m

<!-- b006100 | prose | pages [18] -->
m

<!-- b006101 | prose | pages [18] -->
m

<!-- b006102 | prose | pages [18] -->
m

<!-- b006103 | prose | pages [18] -->
m

<!-- b006104 | prose | pages [18] -->
m

<!-- b006105 | prose | pages [18] -->
m

<!-- b006106 | prose | pages [18] -->
m

<!-- b006107 | prose | pages [18] -->
m

<!-- b006108 | prose | pages [18] -->
m

<!-- b006109 | prose | pages [18] -->
m

<!-- b006110 | prose | pages [18] -->
m

<!-- b006111 | prose | pages [18] -->
m

<!-- b006112 | prose | pages [18] -->
m

<!-- b006113 | prose | pages [18] -->
m

<!-- b006114 | prose | pages [18] -->
m

<!-- b006115 | prose | pages [18] -->
m

<!-- b006116 | prose | pages [18] -->
m

<!-- b006117 | prose | pages [18] -->
m

<!-- b006118 | prose | pages [18] -->
m

<!-- b006119 | prose | pages [18] -->
m

<!-- b006120 | prose | pages [18] -->
m

<!-- b006121 | prose | pages [18] -->
m

<!-- b006122 | prose | pages [18] -->
m

<!-- b006123 | prose | pages [18] -->
m

<!-- b006124 | prose | pages [18] -->
m

<!-- b006125 | prose | pages [18] -->
m

<!-- b006126 | prose | pages [18] -->
m

<!-- b006127 | prose | pages [18] -->
m

<!-- b006128 | prose | pages [18] -->
m

<!-- b006129 | prose | pages [18] -->
m

<!-- b006130 | prose | pages [18] -->
m

<!-- b006131 | prose | pages [18] -->
m

<!-- b006132 | prose | pages [18] -->
m

<!-- b006133 | prose | pages [18] -->
m

<!-- b006134 | prose | pages [18] -->
m

<!-- b006135 | prose | pages [18] -->
m

<!-- b006136 | prose | pages [18] -->
m

<!-- b006137 | prose | pages [18] -->
m

<!-- b006138 | prose | pages [18] -->
m

<!-- b006139 | prose | pages [18] -->
m

<!-- b006140 | prose | pages [18] -->
m

<!-- b006141 | prose | pages [18] -->
m

<!-- b006142 | prose | pages [18] -->
m

<!-- b006143 | prose | pages [18] -->
m

<!-- b006144 | prose | pages [18] -->
m

<!-- b006145 | prose | pages [18] -->
m

<!-- b006146 | prose | pages [18] -->
m

<!-- b006147 | prose | pages [18] -->
m

<!-- b006148 | prose | pages [18] -->
m

<!-- b006149 | prose | pages [18] -->
m

<!-- b006150 | prose | pages [18] -->
m

<!-- b006151 | prose | pages [18] -->
m

<!-- b006152 | prose | pages [18] -->
m

<!-- b006153 | prose | pages [18] -->
m

<!-- b006154 | prose | pages [18] -->
m

<!-- b006155 | prose | pages [18] -->
m

<!-- b006156 | prose | pages [18] -->
m

<!-- b006157 | prose | pages [18] -->
m

<!-- b006158 | prose | pages [18] -->
m

<!-- b006159 | prose | pages [18] -->
m

<!-- b006160 | prose | pages [18] -->
m

<!-- b006161 | prose | pages [18] -->
m

<!-- b006162 | prose | pages [18] -->
m

<!-- b006163 | prose | pages [18] -->
m

<!-- b006164 | prose | pages [18] -->
m

<!-- b006165 | prose | pages [18] -->
m

<!-- b006166 | prose | pages [18] -->
m

<!-- b006167 | prose | pages [18] -->
m

<!-- b006168 | prose | pages [18] -->
m

<!-- b006169 | prose | pages [18] -->
m

<!-- b006170 | prose | pages [18] -->
m

<!-- b006171 | prose | pages [18] -->
m

<!-- b006172 | prose | pages [18] -->
m

<!-- b006173 | prose | pages [18] -->
m

<!-- b006174 | prose | pages [18] -->
m

<!-- b006175 | prose | pages [18] -->
m

<!-- b006176 | prose | pages [18] -->
m

<!-- b006177 | prose | pages [18] -->
m

<!-- b006178 | prose | pages [18] -->
m

<!-- b006179 | prose | pages [18] -->
m

<!-- b006180 | prose | pages [18] -->
m

<!-- b006181 | prose | pages [18] -->
m

<!-- b006182 | prose | pages [18] -->
m

<!-- b006183 | prose | pages [18] -->
m

<!-- b006184 | prose | pages [18] -->
m

<!-- b006185 | prose | pages [18] -->
m

<!-- b006186 | prose | pages [18] -->
m

<!-- b006187 | prose | pages [18] -->
m

<!-- b006188 | prose | pages [18] -->
m

<!-- b006189 | prose | pages [18] -->
m

<!-- b006190 | prose | pages [18] -->
m

<!-- b006191 | prose | pages [18] -->
m

<!-- b006192 | prose | pages [18] -->
m

<!-- b006193 | prose | pages [18] -->
m

<!-- b006194 | prose | pages [18] -->
m

<!-- b006195 | prose | pages [18] -->
m

<!-- b006196 | prose | pages [18] -->
m

<!-- b006197 | prose | pages [18] -->
m

<!-- b006198 | prose | pages [18] -->
m

<!-- b006199 | prose | pages [18] -->
m

<!-- b006200 | prose | pages [18] -->
m

<!-- b006201 | prose | pages [18] -->
m

<!-- b006202 | prose | pages [18] -->
m

<!-- b006203 | prose | pages [18] -->
m

<!-- b006204 | prose | pages [18] -->
m

<!-- b006205 | prose | pages [18] -->
m

<!-- b006206 | prose | pages [18] -->
m

<!-- b006207 | prose | pages [18] -->
m

<!-- b006208 | prose | pages [18] -->
m

<!-- b006209 | prose | pages [18] -->
m

<!-- b006210 | prose | pages [18] -->
m

<!-- b006211 | prose | pages [18] -->
m

<!-- b006212 | prose | pages [18] -->
m

<!-- b006213 | prose | pages [18] -->
m

<!-- b006214 | prose | pages [18] -->
m

<!-- b006215 | prose | pages [18] -->
m

<!-- b006216 | prose | pages [18] -->
m

<!-- b006217 | prose | pages [18] -->
m

<!-- b006218 | prose | pages [18] -->
m

<!-- b006219 | prose | pages [18] -->
m

<!-- b006220 | prose | pages [18] -->
m

<!-- b006221 | prose | pages [18] -->
m

<!-- b006222 | prose | pages [18] -->
m

<!-- b006223 | prose | pages [18] -->
m

<!-- b006224 | prose | pages [18] -->
times this country wins a medal for the first time, then Y will follow a binomial distribution.

<!-- b006225 | prose | pages [18] -->
m

<!-- b006226 | prose | pages [18] -->
m

<!-- b006227 | prose | pages [18] -->
m

<!-- b006228 | prose | pages [18] -->
m

<!-- b006229 | prose | pages [18] -->
m

<!-- b006230 | prose | pages [18] -->
m

<!-- b006231 | prose | pages [18] -->
m

<!-- b006232 | prose | pages [18] -->
m

<!-- b006233 | prose | pages [18] -->
m

<!-- b006234 | prose | pages [18] -->
m

<!-- b006235 | prose | pages [18] -->
m

<!-- b006236 | prose | pages [18] -->
m

<!-- b006237 | prose | pages [18] -->
m

<!-- b006238 | prose | pages [18] -->
m

<!-- b006239 | prose | pages [18] -->
m

<!-- b006240 | prose | pages [18] -->
m

<!-- b006241 | prose | pages [18] -->
m

<!-- b006242 | prose | pages [18] -->
m

<!-- b006243 | prose | pages [18] -->
m

<!-- b006244 | prose | pages [18] -->
m

<!-- b006245 | prose | pages [18] -->
m

<!-- b006246 | prose | pages [18] -->
m

<!-- b006247 | prose | pages [18] -->
m

<!-- b006248 | prose | pages [18] -->
m

<!-- b006249 | prose | pages [18] -->
m

<!-- b006250 | prose | pages [18] -->
m

<!-- b006251 | prose | pages [18] -->
m

<!-- b006252 | prose | pages [18] -->
m

<!-- b006253 | prose | pages [18] -->
m

<!-- b006254 | prose | pages [18] -->
m

<!-- b006255 | prose | pages [18] -->
m

<!-- b006256 | prose | pages [18] -->
m

<!-- b006257 | prose | pages [18] -->
m

<!-- b006258 | prose | pages [18] -->
m

<!-- b006259 | prose | pages [18] -->
m

<!-- b006260 | prose | pages [18] -->
m

<!-- b006261 | prose | pages [18] -->
m

<!-- b006262 | prose | pages [18] -->
m

<!-- b006263 | prose | pages [18] -->
m

<!-- b006264 | prose | pages [18] -->
m

<!-- b006265 | prose | pages [18] -->
m

<!-- b006266 | prose | pages [18] -->
m

<!-- b006267 | prose | pages [18] -->
m

<!-- b006268 | prose | pages [18] -->
m

<!-- b006269 | prose | pages [18] -->
m

<!-- b006270 | prose | pages [18] -->
m

<!-- b006271 | prose | pages [18] -->
m

<!-- b006272 | prose | pages [18] -->
m

<!-- b006273 | prose | pages [18] -->
m

<!-- b006274 | prose | pages [18] -->
m

<!-- b006275 | prose | pages [18] -->
m

<!-- b006276 | prose | pages [18] -->
m

<!-- b006277 | prose | pages [18] -->
m

<!-- b006278 | prose | pages [18] -->
m

<!-- b006279 | prose | pages [18] -->
m

<!-- b006280 | prose | pages [18] -->
m

<!-- b006281 | prose | pages [18] -->
m

<!-- b006282 | prose | pages [18] -->
m

<!-- b006283 | prose | pages [18] -->
m

<!-- b006284 | prose | pages [18] -->
m

<!-- b006285 | prose | pages [18] -->
m

<!-- b006286 | prose | pages [18] -->
m

<!-- b006287 | prose | pages [18] -->
m

<!-- b006288 | prose | pages [18] -->
m

<!-- b006289 | prose | pages [18] -->
m

<!-- b006290 | prose | pages [18] -->
m

<!-- b006291 | prose | pages [18] -->
m

<!-- b006292 | prose | pages [18] -->
m

<!-- b006293 | prose | pages [18] -->
m

<!-- b006294 | prose | pages [18] -->
m

<!-- b006295 | prose | pages [18] -->
m

<!-- b006296 | prose | pages [18] -->
m

<!-- b006297 | prose | pages [18] -->
m

<!-- b006298 | prose | pages [18] -->
m

<!-- b006299 | prose | pages [18] -->
m

<!-- b006300 | prose | pages [18] -->
m

<!-- b006301 | prose | pages [18] -->
m

<!-- b006302 | prose | pages [18] -->
m

<!-- b006303 | prose | pages [18] -->
m

<!-- b006304 | prose | pages [18] -->
m

<!-- b006305 | prose | pages [18] -->
m

<!-- b006306 | prose | pages [18] -->
m

<!-- b006307 | prose | pages [18] -->
m

<!-- b006308 | prose | pages [18] -->
m

<!-- b006309 | prose | pages [18] -->
m

<!-- b006310 | prose | pages [18] -->
m

<!-- b006311 | prose | pages [18] -->
m

<!-- b006312 | prose | pages [18] -->
m

<!-- b006313 | prose | pages [18] -->
m

<!-- b006314 | prose | pages [18] -->
m

<!-- b006315 | prose | pages [18] -->
m

<!-- b006316 | prose | pages [18] -->
m

<!-- b006317 | prose | pages [18] -->
m

<!-- b006318 | prose | pages [18] -->
m

<!-- b006319 | prose | pages [18] -->
m

<!-- b006320 | prose | pages [18] -->
m

<!-- b006321 | prose | pages [18] -->
m

<!-- b006322 | prose | pages [18] -->
m

<!-- b006323 | prose | pages [18] -->
m

<!-- b006324 | prose | pages [18] -->
m

<!-- b006325 | prose | pages [18] -->
m

<!-- b006326 | prose | pages [18] -->
m

<!-- b006327 | prose | pages [18] -->
m

<!-- b006328 | prose | pages [18] -->
m

<!-- b006329 | prose | pages [18] -->
m

<!-- b006330 | prose | pages [18] -->
m

<!-- b006331 | prose | pages [18] -->
m

<!-- b006332 | prose | pages [18] -->
m

<!-- b006333 | prose | pages [18] -->
m

<!-- b006334 | prose | pages [18] -->
m

<!-- b006335 | prose | pages [18] -->
m

<!-- b006336 | prose | pages [18] -->
m

<!-- b006337 | prose | pages [18] -->
m

<!-- b006338 | prose | pages [18] -->
m

<!-- b006339 | prose | pages [18] -->
m

<!-- b006340 | prose | pages [18] -->
m

<!-- b006341 | prose | pages [18] -->
m

<!-- b006342 | prose | pages [18] -->
m

<!-- b006343 | prose | pages [18] -->
m

<!-- b006344 | prose | pages [18] -->
m

<!-- b006345 | prose | pages [18] -->
m

<!-- b006346 | prose | pages [18] -->
m

<!-- b006347 | prose | pages [18] -->
m

<!-- b006348 | prose | pages [18] -->
m

<!-- b006349 | prose | pages [18] -->
m

<!-- b006350 | prose | pages [18] -->
m

<!-- b006351 | prose | pages [18] -->
m

<!-- b006352 | prose | pages [18] -->
m

<!-- b006353 | prose | pages [18] -->
m

<!-- b006354 | prose | pages [18] -->
m

<!-- b006355 | prose | pages [18] -->
m

<!-- b006356 | prose | pages [18] -->
m

<!-- b006357 | prose | pages [18] -->
m

<!-- b006358 | prose | pages [18] -->
m

<!-- b006359 | prose | pages [18] -->
m

<!-- b006360 | prose | pages [18] -->
m

<!-- b006361 | prose | pages [18] -->
m

<!-- b006362 | prose | pages [18] -->
m

<!-- b006363 | prose | pages [18] -->
m

<!-- b006364 | prose | pages [18] -->
m

<!-- b006365 | prose | pages [18] -->
m

<!-- b006366 | prose | pages [18] -->
m

<!-- b006367 | prose | pages [18] -->
m

<!-- b006368 | prose | pages [18] -->
m

<!-- b006369 | prose | pages [18] -->
m

<!-- b006370 | prose | pages [18] -->
m

<!-- b006371 | prose | pages [18] -->
m

<!-- b006372 | prose | pages [18] -->
m

<!-- b006373 | prose | pages [18] -->
m

<!-- b006374 | prose | pages [18] -->
m

<!-- b006375 | prose | pages [18] -->
m

<!-- b006376 | prose | pages [18] -->
m

<!-- b006377 | prose | pages [18] -->
m

<!-- b006378 | prose | pages [18] -->
m

<!-- b006379 | prose | pages [18] -->
m

<!-- b006380 | prose | pages [18] -->
m

<!-- b006381 | prose | pages [18] -->
m

<!-- b006382 | prose | pages [18] -->
m

<!-- b006383 | prose | pages [18] -->
m

<!-- b006384 | prose | pages [18] -->
m

<!-- b006385 | prose | pages [18] -->
m

<!-- b006386 | prose | pages [18] -->
m

<!-- b006387 | prose | pages [18] -->
m

<!-- b006388 | prose | pages [18] -->
m

<!-- b006389 | prose | pages [18] -->
m

<!-- b006390 | prose | pages [18] -->
m

<!-- b006391 | prose | pages [18] -->
m

<!-- b006392 | prose | pages [18] -->
m

<!-- b006393 | prose | pages [18] -->
m

<!-- b006394 | prose | pages [18] -->
m

<!-- b006395 | prose | pages [18] -->
m

<!-- b006396 | prose | pages [18] -->
m

<!-- b006397 | prose | pages [18] -->
m

<!-- b006398 | prose | pages [18] -->
m

<!-- b006399 | prose | pages [18] -->
m

<!-- b006400 | prose | pages [18] -->
m

<!-- b006401 | prose | pages [18] -->
m

<!-- b006402 | prose | pages [18] -->
m

<!-- b006403 | prose | pages [18] -->
m

<!-- b006404 | prose | pages [18] -->
m

<!-- b006405 | prose | pages [18] -->
m

<!-- b006406 | prose | pages [18] -->
m

<!-- b006407 | prose | pages [18] -->
m

<!-- b006408 | prose | pages [18] -->
m

<!-- b006409 | prose | pages [18] -->
m

<!-- b006410 | prose | pages [18] -->
m

<!-- b006411 | prose | pages [18] -->
m

<!-- b006412 | prose | pages [18] -->
m

<!-- b006413 | prose | pages [18] -->
m

<!-- b006414 | prose | pages [18] -->
m

<!-- b006415 | prose | pages [18] -->
m

<!-- b006416 | prose | pages [18] -->
m

<!-- b006417 | prose | pages [18] -->
m

<!-- b006418 | prose | pages [18] -->
m

<!-- b006419 | prose | pages [18] -->
m

<!-- b006420 | prose | pages [18] -->
m

<!-- b006421 | prose | pages [18] -->
m

<!-- b006422 | prose | pages [18] -->
m

<!-- b006423 | prose | pages [18] -->
m

<!-- b006424 | prose | pages [18] -->
m

<!-- b006425 | prose | pages [18] -->
m

<!-- b006426 | prose | pages [18] -->
m

<!-- b006427 | prose | pages [18] -->
m

<!-- b006428 | prose | pages [18] -->
m

<!-- b006429 | prose | pages [18] -->
m

<!-- b006430 | prose | pages [18] -->
m

<!-- b006431 | prose | pages [18] -->
m

<!-- b006432 | prose | pages [18] -->
m

<!-- b006433 | prose | pages [18] -->
m

<!-- b006434 | prose | pages [18] -->
m

<!-- b006435 | prose | pages [18] -->
m

<!-- b006436 | prose | pages [18] -->
m

<!-- b006437 | prose | pages [18] -->
m

<!-- b006438 | prose | pages [18] -->
m

<!-- b006439 | prose | pages [18] -->
m

<!-- b006440 | prose | pages [18] -->
m

<!-- b006441 | prose | pages [18] -->
m

<!-- b006442 | prose | pages [18] -->
m

<!-- b006443 | prose | pages [18] -->
m

<!-- b006444 | prose | pages [18] -->
m

<!-- b006445 | prose | pages [18] -->
m

<!-- b006446 | prose | pages [18] -->
m

<!-- b006447 | prose | pages [18] -->
m

<!-- b006448 | prose | pages [18] -->
m

<!-- b006449 | prose | pages [18] -->
m

<!-- b006450 | prose | pages [18] -->
m

<!-- b006451 | prose | pages [18] -->
m

<!-- b006452 | prose | pages [18] -->
m

<!-- b006453 | prose | pages [18] -->
m

<!-- b006454 | prose | pages [18] -->
m

<!-- b006455 | prose | pages [18] -->
m

<!-- b006456 | prose | pages [18] -->
m

<!-- b006457 | prose | pages [18] -->
m

<!-- b006458 | prose | pages [18] -->
m

<!-- b006459 | prose | pages [18] -->
m

<!-- b006460 | prose | pages [18] -->
m

<!-- b006461 | prose | pages [18] -->
m

<!-- b006462 | prose | pages [18] -->
m

<!-- b006463 | prose | pages [18] -->
m

<!-- b006464 | prose | pages [18] -->
m

<!-- b006465 | prose | pages [18] -->
m

<!-- b006466 | prose | pages [18] -->
m

<!-- b006467 | prose | pages [18] -->
m

<!-- b006468 | prose | pages [18] -->
m

<!-- b006469 | prose | pages [18] -->
m

<!-- b006470 | prose | pages [18] -->
m

<!-- b006471 | prose | pages [18] -->
m

<!-- b006472 | prose | pages [18] -->
m

<!-- b006473 | prose | pages [18] -->
m

<!-- b006474 | prose | pages [18] -->
m

<!-- b006475 | prose | pages [18] -->
m

<!-- b006476 | prose | pages [18] -->
m

<!-- b006477 | prose | pages [18] -->
m

<!-- b006478 | prose | pages [18] -->
m

<!-- b006479 | prose | pages [18] -->
m

<!-- b006480 | prose | pages [18] -->
m

<!-- b006481 | prose | pages [18] -->
m

<!-- b006482 | prose | pages [18] -->
m

<!-- b006483 | prose | pages [18] -->
m

<!-- b006484 | prose | pages [18] -->
m

<!-- b006485 | prose | pages [18] -->
m

<!-- b006486 | prose | pages [18] -->
m

<!-- b006487 | prose | pages [18] -->
Y (t) ∼(n(t), P(t))

<!-- b006488 | prose | pages [18] -->
m

<!-- b006489 | prose | pages [18] -->
m

<!-- b006490 | prose | pages [18] -->
m

<!-- b006491 | prose | pages [18] -->
m

<!-- b006492 | prose | pages [18] -->
m

<!-- b006493 | prose | pages [18] -->
m

<!-- b006494 | prose | pages [18] -->
m

<!-- b006495 | prose | pages [18] -->
m

<!-- b006496 | prose | pages [18] -->
m

<!-- b006497 | prose | pages [18] -->
m

<!-- b006498 | prose | pages [18] -->
m

<!-- b006499 | prose | pages [18] -->
m

<!-- b006500 | prose | pages [18] -->
m

<!-- b006501 | prose | pages [18] -->
m

<!-- b006502 | prose | pages [18] -->
m

<!-- b006503 | prose | pages [18] -->
m

<!-- b006504 | prose | pages [18] -->
m

<!-- b006505 | prose | pages [18] -->
m

<!-- b006506 | prose | pages [18] -->
m

<!-- b006507 | prose | pages [18] -->
m

<!-- b006508 | prose | pages [18] -->
m

<!-- b006509 | prose | pages [18] -->
m

<!-- b006510 | prose | pages [18] -->
m

<!-- b006511 | prose | pages [18] -->
m

<!-- b006512 | prose | pages [18] -->
m

<!-- b006513 | prose | pages [18] -->
m

<!-- b006514 | prose | pages [18] -->
m

<!-- b006515 | prose | pages [18] -->
m

<!-- b006516 | prose | pages [18] -->
m

<!-- b006517 | prose | pages [18] -->
m

<!-- b006518 | prose | pages [18] -->
m

<!-- b006519 | prose | pages [18] -->
m

<!-- b006520 | prose | pages [18] -->
m

<!-- b006521 | prose | pages [18] -->
m

<!-- b006522 | prose | pages [18] -->
m

<!-- b006523 | prose | pages [18] -->
m

<!-- b006524 | prose | pages [18] -->
m

<!-- b006525 | prose | pages [18] -->
m

<!-- b006526 | prose | pages [18] -->
m

<!-- b006527 | prose | pages [18] -->
m

<!-- b006528 | prose | pages [18] -->
m

<!-- b006529 | prose | pages [18] -->
m

<!-- b006530 | prose | pages [18] -->
m

<!-- b006531 | prose | pages [18] -->
m

<!-- b006532 | prose | pages [18] -->
m

<!-- b006533 | prose | pages [18] -->
m

<!-- b006534 | prose | pages [18] -->
m

<!-- b006535 | prose | pages [18] -->
m

<!-- b006536 | prose | pages [18] -->
m

<!-- b006537 | prose | pages [18] -->
m

<!-- b006538 | prose | pages [18] -->
m

<!-- b006539 | prose | pages [18] -->
m

<!-- b006540 | prose | pages [18] -->
m

<!-- b006541 | prose | pages [18] -->
m

<!-- b006542 | prose | pages [18] -->
m

<!-- b006543 | prose | pages [18] -->
m

<!-- b006544 | prose | pages [18] -->
m

<!-- b006545 | prose | pages [18] -->
m

<!-- b006546 | prose | pages [18] -->
m

<!-- b006547 | prose | pages [18] -->
m

<!-- b006548 | prose | pages [18] -->
m

<!-- b006549 | prose | pages [18] -->
m

<!-- b006550 | prose | pages [18] -->
m

<!-- b006551 | prose | pages [18] -->
m

<!-- b006552 | prose | pages [18] -->
m

<!-- b006553 | prose | pages [18] -->
m

<!-- b006554 | prose | pages [18] -->
m

<!-- b006555 | prose | pages [18] -->
m

<!-- b006556 | prose | pages [18] -->
m

<!-- b006557 | prose | pages [18] -->
m

<!-- b006558 | prose | pages [18] -->
m

<!-- b006559 | prose | pages [18] -->
m

<!-- b006560 | prose | pages [18] -->
m

<!-- b006561 | prose | pages [18] -->
m

<!-- b006562 | prose | pages [18] -->
m

<!-- b006563 | prose | pages [18] -->
m

<!-- b006564 | prose | pages [18] -->
m

<!-- b006565 | prose | pages [18] -->
(17)

<!-- b006566 | prose | pages [18] -->
To simulate potential outcomes, we applied Monte Carlo simulations based on the predicted probabilities. After 100 million trials, we obtained the following distribution of the possible number of first-time medalists by 2028.

<!-- b006567 | caption | pages [18] -->
Figure 13: The distribution of the possible number of 2028 first-time medalists

<!-- b006568 | prose | pages [18] -->
As Fig. 13 shows, with a probability of 0.2273, 3 nations are projected to earn their first medal in 2028. The countries with the highest probability of achieving their first-ever medals in 2028 are Monaco (MON), Liechtenstein (LIE), and Myanmar (MYA) respectively.

<!-- b006569 | caption | pages [18] -->
Table 3 provides a breakthrough probability ranking of countries that have never won a

<!-- b006570 | prose | pages [18] -->
medal. The right column is the corresponding probability after exponential normalization.

<!-- b006571 | heading | pages [18] -->
Model IV: Great Coach Effect

<!-- b006572 | prose | pages [18] -->
7

<!-- b006573 | prose | pages [18] -->
7.1

<!-- b006574 | heading | pages [18] -->
Model Overview

<!-- b006575 | prose | pages [18] -->
This section quantifies the impact of coaches on a country’s Olympic performance. By developing a scoring system and applying a threshold method and Isolation Forest, we identified time points where significant performance improvements occur due to the introduction of a coach, namely differential points. The contribution and influence of coaches on specific countries and sports are quantified as factors to reflect the impact of coaches directly. These serve as the basis for us to select sports benefiting most from coaching for chosen countries. By applying both Linear Regression and Random Forest to handling the data of differential points we captured, we predicted the prospects of introducing coaches for specific sports in specific countries.

<!-- b006576 | prose | pages [18] -->
关注数学模型

<!-- b006577 | furniture | pages [18] -->
2

<!-- b006578 | furniture | pages [18] -->
MATHmodels

<!-- b006579 | furniture | pages [18] -->
获取更多资讯

<!-- b006580 | furniture | pages [19] -->
Team # 2514461

<!-- b006581 | furniture | pages [19] -->
Page 18 of 25

<!-- b006582 | caption | pages [19] -->
Table 3: Extrapolated and Exponential Values for top 20 first-time medalists in 2028

<!-- b006583 | prose | pages [19] -->
NOC Extrapolated Values Exponential Values MON 0.6995 LIE 0.6434 0.0503 0.0476

<!-- b006584 | prose | pages [19] -->
微信公众号：数学模型

<!-- b006585 | prose | pages [19] -->
MYA 0.6297 MLT 0.6215 BOL 0.5682 MLI 0.5519 NEP 0.5464 CHA 0.5452 LBR 0.5343 BIZ 0.5309 CGO 0.5203 AND 0.5163 0.0469 0.0465 0.0441 0.0434 0.0432 0.0431 0.0427 0.0425 0.0421 0.0419

<!-- b006586 | prose | pages [19] -->
微信号：MATHmodels

<!-- b006587 | prose | pages [19] -->
MAD 0.5066 LES 0.5045 GUI 0.4990 BEN 0.4957 NCA 0.4946 SLE 0.4851 CAY 0.4747 CAF 0.4733 0.0415 0.0414 0.0412 0.0410 0.0410 0.0406 0.0402 0.0401

<!-- b006588 | prose | pages [19] -->
It’s worth noting that only in this part, sport is essentially a discipline, given the significant differences between various disciplines in practice and the fact that a coach often specializes in a single discipline. While the analysis at this level shares the same principles as at the sport level, it will be more accurate and detailed.

<!-- b006589 | prose | pages [19] -->
7.2 Effect Evidence

<!-- b006590 | prose | pages [19] -->
A coach plays a pivotal role in a country’s Olympic performance. If a country introduces a coach in a specific sport, it is highly likely that the country’s performance in that will see a significant improvement in the following years. For instance, in China in 2003, after introducing Coach Guoliang Liu to table tennis, the country’s performance improved markedly. Therefore, we can estimate the impact of coaches (Great Coach Effect, GCE) by examining the changes in performance over time. We can identify differential points as those where we conclude that a coaching effect took place.

<!-- b006591 | prose | pages [19] -->
7.2.1 Threshold Method

<!-- b006592 | prose | pages [19] -->
The first-order difference and first-order ratio of score S are defined as

<!-- b006593 | prose | pages [19] -->
△S = Si −Si−1

<!-- b006594 | prose | pages [19] -->
γS =

<!-- b006595 | prose | pages [19] -->
(18)

<!-- b006596 | prose | pages [19] -->
Si

<!-- b006597 | prose | pages [19] -->
(19)

<!-- b006598 | prose | pages [19] -->
Si−1

<!-- b006599 | prose | pages [19] -->
The larger △S and γS are, the greater progress the country have made in ith Olympics. The first method to determine whether GCE has happened is to set a threshold value ST△for the

<!-- b006600 | furniture | pages [20] -->
Team # 2514461

<!-- b006601 | furniture | pages [20] -->
Page 19 of 25

<!-- b006602 | prose | pages [20] -->
first-order difference and STγ for the first-order ratio of scores between consecutive Olympic Games and compare the actual △S and γS with them.

<!-- b006603 | prose | pages [20] -->
(

<!-- b006604 | prose | pages [20] -->
if △S ≥ST || γS ≥STγ, 1

<!-- b006605 | prose | pages [20] -->
GCE =

<!-- b006606 | prose | pages [20] -->
0 else.

<!-- b006607 | prose | pages [20] -->
(20)

<!-- b006608 | prose | pages [20] -->
Points with a GCE value of 1 are defined as differential points.

<!-- b006609 | prose | pages [20] -->
These threshold values are established to minimize the variance in a country’s total score due to the exceptional performance by certain individuals and consider the progress of small nations. A △S or γS exceeding the threshold indicates a statistically significant improvement in the country’s overall performance, suggesting a substantial coaching effect.

<!-- b006610 | prose | pages [20] -->
7.2.2 Isolation Forest

<!-- b006611 | prose | pages [20] -->
We also employed the Isolation Forest method to capture the differences in Score S.

<!-- b006612 | prose | pages [20] -->
Isolation Forest is an ensemble-based method for anomaly detection. It identifies outliers by randomly selecting features and feature values to build multiple isolation trees, each of which isolates data points by randomly choosing features and split points. The anomaly score for a data point is typically given by the negative exponential of its average path length in the isolation tree, i.e., score(x) = −2−E(h(x))

<!-- b006613 | prose | pages [20] -->
, where E(h(x)) is the average path length of data point x in c the isolation tree, and c is the average path length of the tree. The shorter the path length, the higher the anomaly score, making it easier to identify outliers.

<!-- b006614 | prose | pages [20] -->
For instance, ifcountry’sdifferentialvaluesovertheyearsarerepresentedas[X1, X2, . . . , Xn], where Xn is the largest, then Xn will be closest to the root node in the isolation tree. By ex- tracting these points, we can identify some of the larger differential points in Score.

<!-- b006615 | prose | pages [20] -->
GCE contribution to medal counts 7.3

<!-- b006616 | prose | pages [20] -->
To measure the contribution of great coaches to a country’s performance at the ith Games, we defined a contribution factor Ci.

<!-- b006617 | prose | pages [20] -->
P

<!-- b006618 | prose | pages [20] -->
j∈sports αij△Sij

<!-- b006619 | prose | pages [20] -->
Ci =

<!-- b006620 | prose | pages [20] -->
P

<!-- b006621 | prose | pages [20] -->
If △Sij > ST, αij = 1; else αij = 0.

<!-- b006622 | prose | pages [20] -->
(21)

<!-- b006623 | prose | pages [20] -->
j∈sports Sij

<!-- b006624 | prose | pages [20] -->
This factor quantifies how much the great coaches of a whole country contributes to its medal counts. It’s different from country to country. The data we calculated are listed in table 4 in order.

<!-- b006625 | prose | pages [20] -->
7.4 GCE influence on certain sports

<!-- b006626 | prose | pages [20] -->
To measure the influence of a coach to any country’s performance in a certain sport s, we defined an influence factor Is.

<!-- b006627 | prose | pages [20] -->
P

<!-- b006628 | prose | pages [20] -->
P

<!-- b006629 | prose | pages [20] -->
countries△Ssk>ST αsk△Ssk

<!-- b006630 | prose | pages [20] -->
k∈years

<!-- b006631 | prose | pages [20] -->
Is =

<!-- b006632 | prose | pages [20] -->
P

<!-- b006633 | prose | pages [20] -->
P

<!-- b006634 | prose | pages [20] -->
k∈years

<!-- b006635 | prose | pages [20] -->
(22)

<!-- b006636 | prose | pages [20] -->
countries△Ssk>ST Ssk

<!-- b006637 | prose | pages [20] -->
If △Ssk > ST, αsk = 1; else αsk = 0. This factor mirror the relationship between coach and sports. It’s different from sport to sport. Because the mobility of coaches is global, we assumed the Is is the same for each country. We ranked Is in table 5.

<!-- b006638 | prose | pages [20] -->
关注数学模型

<!-- b006639 | furniture | pages [20] -->
2

<!-- b006640 | furniture | pages [20] -->
MATHmodels

<!-- b006641 | furniture | pages [20] -->
获取更多资讯

<!-- b006642 | furniture | pages [21] -->
Team # 2514461

<!-- b006643 | caption | pages [21] -->
Table 4:

<!-- b006644 | prose | pages [21] -->
NOC and their corresponding Contribution Factor

<!-- b006645 | prose | pages [21] -->
C2024 NOC VIE 1.0000 SGP 1.0000 CIV 1.0000 TTO 1.0000 ISL 1.0000

<!-- b006646 | furniture | pages [21] -->
Page 20 of 25

<!-- b006647 | caption | pages [21] -->
Table 5: Sports and their corresponding

<!-- b006648 | prose | pages [21] -->
Influence Factor

<!-- b006649 | prose | pages [21] -->
Is Sport Cycling Mountain Bike 1.0000 3x3 Basketball 1.0000 Cycling BMX Racing 1.0000 Cycling BMX Freestyle 1.0000 Golf 0.8690

<!-- b006650 | prose | pages [21] -->
微信公众号：数学模型

<!-- b006651 | prose | pages [21] -->
MAR 0.9318 CHI 0.9167 IRL 0.8635 POR 0.8590 SMR 0.8333 ANZ 0.8182 EST 0.8034 BOT 0.8000 BRN 0.8000 BAH 0.7894 MEX 0.7843

<!-- b006652 | prose | pages [21] -->
Surfing 0.8333 Triathlon 0.8161 Sport Climbing 0.8125 Trampolining 0.8077 Tug-Of-War 0.8068 Canoe Slalom 0.8065 Modern Pentathlon 0.8063 Cycling Road 0.8000 Art Competitions 0.7850 Beach Volleyball 0.7692 Handball 0.7590

<!-- b006653 | prose | pages [21] -->
微信号：MATHmodels

<!-- b006654 | prose | pages [21] -->
MGL 0.7500 NGR 0.7159 PHI 0.6875 URU 0.6778 ETH 0.6691 SLO 0.6666 HKG 0.6666 ESP 0.6611 DOM 0.6538 RSA 0.6427 ECU 0.6306 KEN 0.6266 PAK 0.6242 CRO 0.6306

<!-- b006655 | prose | pages [21] -->
7.5 Application and Estimation

<!-- b006656 | prose | pages [21] -->
7.5.1 choosing countries and sports

<!-- b006657 | prose | pages [21] -->
Trampoline Gymnastics 0.7500 Football 0.7399 Water Polo 0.7358 Tennis 0.7324 Softball 0.7238 Volleyball 0.7211 Hockey 0.7124 Rhythmic Gymnastics 0.7063 Sailing 0.7058 Baseball 0.6989 Archery 0.6987 Artistic Swimming 0.6970 Shooting 0.6814 Taekwondo 0.6777

<!-- b006658 | prose | pages [21] -->
In order to specify the sports where coaching investment would yield the better returns for them, we ranked sports based on their coaching influence factor Is to identify those most susceptible to coaching effects. Then, we determined whether their historical performance in each sport falls within a promising range(Smin, Smax), which means they have enough potential and room for improvement both. If so, we would consider introducing a great coach.

<!-- b006659 | prose | pages [21] -->
7.5.2 Great Coach Effect Prediction

<!-- b006660 | prose | pages [21] -->
Our goal is to build a model to forecast the impact of introducing a coach in a particular sport. By extracting differential data points that exhibit a coaching effect and plotting the previous Game’s scores against the subsequent Game’s scores, we discovered a discernible pattern.

<!-- b006661 | furniture | pages [24] -->
Team # 2514461

<!-- b006662 | furniture | pages [24] -->
m

<!-- b006663 | furniture | pages [24] -->
m

<!-- b006664 | furniture | pages [24] -->
m

<!-- b006665 | furniture | pages [24] -->
m

<!-- b006666 | furniture | pages [24] -->
m

<!-- b006667 | furniture | pages [24] -->
m

<!-- b006668 | furniture | pages [24] -->
m

<!-- b006669 | furniture | pages [24] -->
m

<!-- b006670 | furniture | pages [24] -->
m

<!-- b006671 | furniture | pages [24] -->
m

<!-- b006672 | furniture | pages [24] -->
m

<!-- b006673 | furniture | pages [24] -->
m

<!-- b006674 | furniture | pages [24] -->
m

<!-- b006675 | furniture | pages [24] -->
m

<!-- b006676 | furniture | pages [24] -->
m

<!-- b006677 | furniture | pages [24] -->
m

<!-- b006678 | furniture | pages [24] -->
m

<!-- b006679 | furniture | pages [24] -->
m

<!-- b006680 | furniture | pages [24] -->
m

<!-- b006681 | furniture | pages [24] -->
m

<!-- b006682 | furniture | pages [24] -->
m

<!-- b006683 | furniture | pages [24] -->
m

<!-- b006684 | furniture | pages [24] -->
m

<!-- b006685 | furniture | pages [24] -->
m

<!-- b006686 | furniture | pages [24] -->
m

<!-- b006687 | furniture | pages [24] -->
m

<!-- b006688 | furniture | pages [24] -->
m

<!-- b006689 | furniture | pages [24] -->
m

<!-- b006690 | furniture | pages [24] -->
m

<!-- b006691 | furniture | pages [24] -->
m

<!-- b006692 | furniture | pages [24] -->
m

<!-- b006693 | furniture | pages [24] -->
m

<!-- b006694 | furniture | pages [24] -->
m

<!-- b006695 | furniture | pages [24] -->
m

<!-- b006696 | furniture | pages [24] -->
m

<!-- b006697 | furniture | pages [24] -->
m

<!-- b006698 | furniture | pages [24] -->
m

<!-- b006699 | furniture | pages [24] -->
m

<!-- b006700 | furniture | pages [24] -->
m

<!-- b006701 | furniture | pages [24] -->
m

<!-- b006702 | furniture | pages [24] -->
m

<!-- b006703 | furniture | pages [24] -->
m

<!-- b006704 | furniture | pages [24] -->
m

<!-- b006705 | furniture | pages [24] -->
m

<!-- b006706 | furniture | pages [24] -->
m

<!-- b006707 | furniture | pages [24] -->
m

<!-- b006708 | furniture | pages [24] -->
m

<!-- b006709 | furniture | pages [24] -->
m

<!-- b006710 | furniture | pages [24] -->
m

<!-- b006711 | furniture | pages [24] -->
m

<!-- b006712 | furniture | pages [24] -->
m

<!-- b006713 | furniture | pages [24] -->
m

<!-- b006714 | furniture | pages [24] -->
m

<!-- b006715 | furniture | pages [24] -->
m

<!-- b006716 | furniture | pages [24] -->
m

<!-- b006717 | furniture | pages [24] -->
m

<!-- b006718 | furniture | pages [24] -->
m

<!-- b006719 | furniture | pages [24] -->
m

<!-- b006720 | furniture | pages [24] -->
m

<!-- b006721 | furniture | pages [24] -->
m

<!-- b006722 | furniture | pages [24] -->
m

<!-- b006723 | furniture | pages [24] -->
m

<!-- b006724 | furniture | pages [24] -->
m

<!-- b006725 | furniture | pages [24] -->
m

<!-- b006726 | furniture | pages [24] -->
m

<!-- b006727 | furniture | pages [24] -->
m

<!-- b006728 | furniture | pages [24] -->
m

<!-- b006729 | furniture | pages [24] -->
m

<!-- b006730 | furniture | pages [24] -->
m

<!-- b006731 | furniture | pages [24] -->
m

<!-- b006732 | furniture | pages [24] -->
m

<!-- b006733 | furniture | pages [24] -->
m

<!-- b006734 | furniture | pages [24] -->
m

<!-- b006735 | furniture | pages [24] -->
m

<!-- b006736 | furniture | pages [24] -->
m

<!-- b006737 | furniture | pages [24] -->
m

<!-- b006738 | furniture | pages [24] -->
m

<!-- b006739 | furniture | pages [24] -->
m

<!-- b006740 | furniture | pages [24] -->
m

<!-- b006741 | furniture | pages [24] -->
m

<!-- b006742 | furniture | pages [24] -->
m

<!-- b006743 | furniture | pages [24] -->
m

<!-- b006744 | furniture | pages [24] -->
m

<!-- b006745 | furniture | pages [24] -->
m

<!-- b006746 | furniture | pages [24] -->
m

<!-- b006747 | furniture | pages [24] -->
m

<!-- b006748 | furniture | pages [24] -->
m

<!-- b006749 | furniture | pages [24] -->
m

<!-- b006750 | furniture | pages [24] -->
m

<!-- b006751 | furniture | pages [24] -->
m

<!-- b006752 | furniture | pages [24] -->
m

<!-- b006753 | furniture | pages [24] -->
m

<!-- b006754 | furniture | pages [24] -->
m

<!-- b006755 | furniture | pages [24] -->
m

<!-- b006756 | furniture | pages [24] -->
m

<!-- b006757 | furniture | pages [24] -->
m

<!-- b006758 | furniture | pages [24] -->
m

<!-- b006759 | furniture | pages [24] -->
m

<!-- b006760 | furniture | pages [24] -->
m

<!-- b006761 | furniture | pages [24] -->
m

<!-- b006762 | furniture | pages [24] -->
m

<!-- b006763 | furniture | pages [24] -->
m

<!-- b006764 | prose | pages [24] -->
m

<!-- b006765 | prose | pages [24] -->
m

<!-- b006766 | prose | pages [24] -->
m

<!-- b006767 | prose | pages [24] -->
m

<!-- b006768 | prose | pages [24] -->
m

<!-- b006769 | prose | pages [24] -->
m

<!-- b006770 | prose | pages [24] -->
m

<!-- b006771 | prose | pages [24] -->
m

<!-- b006772 | prose | pages [24] -->
m

<!-- b006773 | prose | pages [24] -->
m

<!-- b006774 | prose | pages [24] -->
m

<!-- b006775 | prose | pages [24] -->
m

<!-- b006776 | prose | pages [24] -->
m

<!-- b006777 | prose | pages [24] -->
m

<!-- b006778 | prose | pages [24] -->
m

<!-- b006779 | prose | pages [24] -->
m

<!-- b006780 | prose | pages [24] -->
m

<!-- b006781 | prose | pages [24] -->
m

<!-- b006782 | prose | pages [24] -->
m

<!-- b006783 | prose | pages [24] -->
m

<!-- b006784 | prose | pages [24] -->
m

<!-- b006785 | prose | pages [24] -->
m

<!-- b006786 | prose | pages [24] -->
m

<!-- b006787 | prose | pages [24] -->
m

<!-- b006788 | prose | pages [24] -->
m

<!-- b006789 | prose | pages [24] -->
m

<!-- b006790 | prose | pages [24] -->
m

<!-- b006791 | prose | pages [24] -->
m

<!-- b006792 | prose | pages [24] -->
m

<!-- b006793 | prose | pages [24] -->
m

<!-- b006794 | prose | pages [24] -->
m

<!-- b006795 | prose | pages [24] -->
m

<!-- b006796 | prose | pages [24] -->
m

<!-- b006797 | prose | pages [24] -->
m

<!-- b006798 | prose | pages [24] -->
m

<!-- b006799 | prose | pages [24] -->
m

<!-- b006800 | prose | pages [24] -->
m

<!-- b006801 | prose | pages [24] -->
m

<!-- b006802 | prose | pages [24] -->
m

<!-- b006803 | prose | pages [24] -->
m

<!-- b006804 | prose | pages [24] -->
m

<!-- b006805 | prose | pages [24] -->
m

<!-- b006806 | prose | pages [24] -->
m

<!-- b006807 | prose | pages [24] -->
m

<!-- b006808 | prose | pages [24] -->
m

<!-- b006809 | prose | pages [24] -->
m

<!-- b006810 | prose | pages [24] -->
m

<!-- b006811 | prose | pages [24] -->
m

<!-- b006812 | prose | pages [24] -->
m

<!-- b006813 | prose | pages [24] -->
m

<!-- b006814 | prose | pages [24] -->
m

<!-- b006815 | prose | pages [24] -->
m

<!-- b006816 | prose | pages [24] -->
m

<!-- b006817 | prose | pages [24] -->
m

<!-- b006818 | prose | pages [24] -->
m

<!-- b006819 | prose | pages [24] -->
m

<!-- b006820 | prose | pages [24] -->
m

<!-- b006821 | prose | pages [24] -->
m

<!-- b006822 | prose | pages [24] -->
m

<!-- b006823 | prose | pages [24] -->
m

<!-- b006824 | prose | pages [24] -->
m

<!-- b006825 | prose | pages [24] -->
m

<!-- b006826 | prose | pages [24] -->
m

<!-- b006827 | prose | pages [24] -->
m

<!-- b006828 | prose | pages [24] -->
m

<!-- b006829 | prose | pages [24] -->
m

<!-- b006830 | prose | pages [24] -->
m

<!-- b006831 | prose | pages [24] -->
m

<!-- b006832 | prose | pages [24] -->
m

<!-- b006833 | prose | pages [24] -->
m

<!-- b006834 | prose | pages [24] -->
m

<!-- b006835 | prose | pages [24] -->
m

<!-- b006836 | prose | pages [24] -->
m

<!-- b006837 | prose | pages [24] -->
m

<!-- b006838 | prose | pages [24] -->
m

<!-- b006839 | prose | pages [24] -->
m

<!-- b006840 | prose | pages [24] -->
m

<!-- b006841 | prose | pages [24] -->
m

<!-- b006842 | prose | pages [24] -->
m

<!-- b006843 | prose | pages [24] -->
m

<!-- b006844 | prose | pages [24] -->
m

<!-- b006845 | prose | pages [24] -->
m

<!-- b006846 | prose | pages [24] -->
m

<!-- b006847 | prose | pages [24] -->
m

<!-- b006848 | prose | pages [24] -->
m

<!-- b006849 | prose | pages [24] -->
m

<!-- b006850 | prose | pages [24] -->
m

<!-- b006851 | prose | pages [24] -->
m

<!-- b006852 | prose | pages [24] -->
m

<!-- b006853 | prose | pages [24] -->
m

<!-- b006854 | prose | pages [24] -->
m

<!-- b006855 | prose | pages [24] -->
m

<!-- b006856 | prose | pages [24] -->
m

<!-- b006857 | prose | pages [24] -->
m

<!-- b006858 | furniture | pages [24] -->
Page 23 of 25

<!-- b006859 | furniture | pages [24] -->
m

<!-- b006860 | furniture | pages [24] -->
m

<!-- b006861 | furniture | pages [24] -->
m

<!-- b006862 | furniture | pages [24] -->
m

<!-- b006863 | furniture | pages [24] -->
m

<!-- b006864 | furniture | pages [24] -->
m

<!-- b006865 | furniture | pages [24] -->
m

<!-- b006866 | furniture | pages [24] -->
m

<!-- b006867 | furniture | pages [24] -->
m

<!-- b006868 | furniture | pages [24] -->
m

<!-- b006869 | furniture | pages [24] -->
m

<!-- b006870 | furniture | pages [24] -->
m

<!-- b006871 | prose | pages [24] -->
m m

<!-- b006872 | prose | pages [24] -->
m m

<!-- b006873 | prose | pages [24] -->
m m

<!-- b006874 | prose | pages [24] -->
m m

<!-- b006875 | prose | pages [24] -->
m m

<!-- b006876 | prose | pages [24] -->
m m m m

<!-- b006877 | prose | pages [24] -->
• In the study of GCE, we provided the Olympic Committees with a list of sports that would

<!-- b006878 | prose | pages [24] -->
m

<!-- b006879 | prose | pages [24] -->
m

<!-- b006880 | prose | pages [24] -->
m

<!-- b006881 | prose | pages [24] -->
m

<!-- b006882 | prose | pages [24] -->
m

<!-- b006883 | prose | pages [24] -->
m

<!-- b006884 | prose | pages [24] -->
m

<!-- b006885 | prose | pages [24] -->
m

<!-- b006886 | prose | pages [24] -->
m

<!-- b006887 | prose | pages [24] -->
m

<!-- b006888 | prose | pages [24] -->
m

<!-- b006889 | prose | pages [24] -->
m

<!-- b006890 | prose | pages [24] -->
m

<!-- b006891 | prose | pages [24] -->
m

<!-- b006892 | prose | pages [24] -->
m

<!-- b006893 | prose | pages [24] -->
m

<!-- b006894 | prose | pages [24] -->
m

<!-- b006895 | prose | pages [24] -->
m

<!-- b006896 | prose | pages [24] -->
m

<!-- b006897 | prose | pages [24] -->
m

<!-- b006898 | prose | pages [24] -->
m

<!-- b006899 | prose | pages [24] -->
m

<!-- b006900 | prose | pages [24] -->
m

<!-- b006901 | prose | pages [24] -->
m

<!-- b006902 | prose | pages [24] -->
m

<!-- b006903 | prose | pages [24] -->
m

<!-- b006904 | prose | pages [24] -->
m

<!-- b006905 | prose | pages [24] -->
m

<!-- b006906 | prose | pages [24] -->
m

<!-- b006907 | prose | pages [24] -->
m

<!-- b006908 | prose | pages [24] -->
m

<!-- b006909 | prose | pages [24] -->
m

<!-- b006910 | prose | pages [24] -->
m

<!-- b006911 | prose | pages [24] -->
m

<!-- b006912 | prose | pages [24] -->
m

<!-- b006913 | prose | pages [24] -->
m

<!-- b006914 | prose | pages [24] -->
m

<!-- b006915 | prose | pages [24] -->
m

<!-- b006916 | prose | pages [24] -->
m

<!-- b006917 | prose | pages [24] -->
m

<!-- b006918 | prose | pages [24] -->
m

<!-- b006919 | prose | pages [24] -->
m

<!-- b006920 | prose | pages [24] -->
m

<!-- b006921 | prose | pages [24] -->
m

<!-- b006922 | prose | pages [24] -->
m

<!-- b006923 | prose | pages [24] -->
m

<!-- b006924 | prose | pages [24] -->
m

<!-- b006925 | prose | pages [24] -->
m

<!-- b006926 | prose | pages [24] -->
m

<!-- b006927 | prose | pages [24] -->
m

<!-- b006928 | prose | pages [24] -->
m

<!-- b006929 | prose | pages [24] -->
m

<!-- b006930 | prose | pages [24] -->
m

<!-- b006931 | prose | pages [24] -->
m

<!-- b006932 | prose | pages [24] -->
m

<!-- b006933 | prose | pages [24] -->
m

<!-- b006934 | prose | pages [24] -->
m

<!-- b006935 | prose | pages [24] -->
m

<!-- b006936 | prose | pages [24] -->
m

<!-- b006937 | prose | pages [24] -->
m

<!-- b006938 | prose | pages [24] -->
m

<!-- b006939 | prose | pages [24] -->
m

<!-- b006940 | prose | pages [24] -->
m

<!-- b006941 | prose | pages [24] -->
m

<!-- b006942 | prose | pages [24] -->
m

<!-- b006943 | prose | pages [24] -->
m

<!-- b006944 | prose | pages [24] -->
m

<!-- b006945 | prose | pages [24] -->
m

<!-- b006946 | prose | pages [24] -->
m

<!-- b006947 | prose | pages [24] -->
m

<!-- b006948 | prose | pages [24] -->
m

<!-- b006949 | prose | pages [24] -->
m

<!-- b006950 | prose | pages [24] -->
m

<!-- b006951 | prose | pages [24] -->
m

<!-- b006952 | prose | pages [24] -->
m

<!-- b006953 | prose | pages [24] -->
m

<!-- b006954 | prose | pages [24] -->
m

<!-- b006955 | prose | pages [24] -->
m

<!-- b006956 | prose | pages [24] -->
m

<!-- b006957 | prose | pages [24] -->
m

<!-- b006958 | prose | pages [24] -->
m

<!-- b006959 | prose | pages [24] -->
m

<!-- b006960 | prose | pages [24] -->
m

<!-- b006961 | prose | pages [24] -->
m

<!-- b006962 | prose | pages [24] -->
m

<!-- b006963 | prose | pages [24] -->
m

<!-- b006964 | prose | pages [24] -->
m

<!-- b006965 | prose | pages [24] -->
m

<!-- b006966 | prose | pages [24] -->
m

<!-- b006967 | prose | pages [24] -->
m

<!-- b006968 | prose | pages [24] -->
m

<!-- b006969 | prose | pages [24] -->
m

<!-- b006970 | prose | pages [24] -->
m

<!-- b006971 | prose | pages [24] -->
m

<!-- b006972 | prose | pages [24] -->
m

<!-- b006973 | prose | pages [24] -->
m

<!-- b006974 | prose | pages [24] -->
m

<!-- b006975 | prose | pages [24] -->
m

<!-- b006976 | prose | pages [24] -->
m

<!-- b006977 | prose | pages [24] -->
m

<!-- b006978 | prose | pages [24] -->
m

<!-- b006979 | prose | pages [24] -->
m

<!-- b006980 | prose | pages [24] -->
m

<!-- b006981 | prose | pages [24] -->
m

<!-- b006982 | prose | pages [24] -->
m

<!-- b006983 | prose | pages [24] -->
m

<!-- b006984 | prose | pages [24] -->
m

<!-- b006985 | prose | pages [24] -->
m

<!-- b006986 | prose | pages [24] -->
m

<!-- b006987 | prose | pages [24] -->
m

<!-- b006988 | prose | pages [24] -->
m

<!-- b006989 | prose | pages [24] -->
m

<!-- b006990 | prose | pages [24] -->
m

<!-- b006991 | prose | pages [24] -->
m

<!-- b006992 | prose | pages [24] -->
m

<!-- b006993 | prose | pages [24] -->
m

<!-- b006994 | prose | pages [24] -->
m

<!-- b006995 | prose | pages [24] -->
m

<!-- b006996 | prose | pages [24] -->
m

<!-- b006997 | prose | pages [24] -->
m

<!-- b006998 | prose | pages [24] -->
m

<!-- b006999 | prose | pages [24] -->
m

<!-- b007000 | prose | pages [24] -->
m

<!-- b007001 | prose | pages [24] -->
m

<!-- b007002 | prose | pages [24] -->
m

<!-- b007003 | prose | pages [24] -->
m

<!-- b007004 | prose | pages [24] -->
m

<!-- b007005 | prose | pages [24] -->
m

<!-- b007006 | prose | pages [24] -->
m

<!-- b007007 | prose | pages [24] -->
m

<!-- b007008 | prose | pages [24] -->
m m

<!-- b007009 | prose | pages [24] -->
m m

<!-- b007010 | prose | pages [24] -->
m m

<!-- b007011 | prose | pages [24] -->
m m

<!-- b007012 | prose | pages [24] -->
m m

<!-- b007013 | prose | pages [24] -->
m m

<!-- b007014 | prose | pages [24] -->
m m

<!-- b007015 | prose | pages [24] -->
m m

<!-- b007016 | prose | pages [24] -->
m m

<!-- b007017 | prose | pages [24] -->
most easily improved with the help of coaches through impact factors. It is important to

<!-- b007018 | prose | pages [24] -->
m

<!-- b007019 | prose | pages [24] -->
m

<!-- b007020 | prose | pages [24] -->
m

<!-- b007021 | prose | pages [24] -->
m

<!-- b007022 | prose | pages [24] -->
m

<!-- b007023 | prose | pages [24] -->
m

<!-- b007024 | prose | pages [24] -->
m

<!-- b007025 | prose | pages [24] -->
m

<!-- b007026 | prose | pages [24] -->
m

<!-- b007027 | prose | pages [24] -->
m

<!-- b007028 | prose | pages [24] -->
m

<!-- b007029 | prose | pages [24] -->
m

<!-- b007030 | prose | pages [24] -->
m

<!-- b007031 | prose | pages [24] -->
m

<!-- b007032 | prose | pages [24] -->
m

<!-- b007033 | prose | pages [24] -->
m

<!-- b007034 | prose | pages [24] -->
m

<!-- b007035 | prose | pages [24] -->
m

<!-- b007036 | prose | pages [24] -->
m

<!-- b007037 | prose | pages [24] -->
m

<!-- b007038 | prose | pages [24] -->
m

<!-- b007039 | prose | pages [24] -->
m

<!-- b007040 | prose | pages [24] -->
m

<!-- b007041 | prose | pages [24] -->
m

<!-- b007042 | prose | pages [24] -->
m

<!-- b007043 | prose | pages [24] -->
m

<!-- b007044 | prose | pages [24] -->
m

<!-- b007045 | prose | pages [24] -->
m

<!-- b007046 | prose | pages [24] -->
m

<!-- b007047 | prose | pages [24] -->
m

<!-- b007048 | prose | pages [24] -->
m

<!-- b007049 | prose | pages [24] -->
m

<!-- b007050 | prose | pages [24] -->
m

<!-- b007051 | prose | pages [24] -->
m

<!-- b007052 | prose | pages [24] -->
m

<!-- b007053 | prose | pages [24] -->
m

<!-- b007054 | prose | pages [24] -->
m

<!-- b007055 | prose | pages [24] -->
m

<!-- b007056 | prose | pages [24] -->
m

<!-- b007057 | prose | pages [24] -->
m

<!-- b007058 | prose | pages [24] -->
m

<!-- b007059 | prose | pages [24] -->
m

<!-- b007060 | prose | pages [24] -->
m

<!-- b007061 | prose | pages [24] -->
m

<!-- b007062 | prose | pages [24] -->
m

<!-- b007063 | prose | pages [24] -->
m

<!-- b007064 | prose | pages [24] -->
m

<!-- b007065 | prose | pages [24] -->
m

<!-- b007066 | prose | pages [24] -->
m

<!-- b007067 | prose | pages [24] -->
m

<!-- b007068 | prose | pages [24] -->
m

<!-- b007069 | prose | pages [24] -->
m

<!-- b007070 | prose | pages [24] -->
m

<!-- b007071 | prose | pages [24] -->
m

<!-- b007072 | prose | pages [24] -->
m

<!-- b007073 | prose | pages [24] -->
m

<!-- b007074 | prose | pages [24] -->
m

<!-- b007075 | prose | pages [24] -->
m

<!-- b007076 | prose | pages [24] -->
m

<!-- b007077 | prose | pages [24] -->
m

<!-- b007078 | prose | pages [24] -->
m

<!-- b007079 | prose | pages [24] -->
m

<!-- b007080 | prose | pages [24] -->
m

<!-- b007081 | prose | pages [24] -->
m

<!-- b007082 | prose | pages [24] -->
m

<!-- b007083 | prose | pages [24] -->
m

<!-- b007084 | prose | pages [24] -->
m

<!-- b007085 | prose | pages [24] -->
m

<!-- b007086 | prose | pages [24] -->
m

<!-- b007087 | prose | pages [24] -->
m

<!-- b007088 | prose | pages [24] -->
m

<!-- b007089 | prose | pages [24] -->
m

<!-- b007090 | prose | pages [24] -->
m

<!-- b007091 | prose | pages [24] -->
m

<!-- b007092 | prose | pages [24] -->
m

<!-- b007093 | prose | pages [24] -->
m

<!-- b007094 | prose | pages [24] -->
m

<!-- b007095 | prose | pages [24] -->
m

<!-- b007096 | prose | pages [24] -->
m

<!-- b007097 | prose | pages [24] -->
m

<!-- b007098 | prose | pages [24] -->
m

<!-- b007099 | prose | pages [24] -->
m

<!-- b007100 | prose | pages [24] -->
m

<!-- b007101 | prose | pages [24] -->
m

<!-- b007102 | prose | pages [24] -->
m

<!-- b007103 | prose | pages [24] -->
m

<!-- b007104 | prose | pages [24] -->
m

<!-- b007105 | prose | pages [24] -->
m

<!-- b007106 | prose | pages [24] -->
m

<!-- b007107 | prose | pages [24] -->
m

<!-- b007108 | prose | pages [24] -->
m

<!-- b007109 | prose | pages [24] -->
m

<!-- b007110 | prose | pages [24] -->
m

<!-- b007111 | prose | pages [24] -->
m

<!-- b007112 | prose | pages [24] -->
m

<!-- b007113 | prose | pages [24] -->
m

<!-- b007114 | prose | pages [24] -->
m

<!-- b007115 | prose | pages [24] -->
m

<!-- b007116 | prose | pages [24] -->
m

<!-- b007117 | prose | pages [24] -->
m

<!-- b007118 | prose | pages [24] -->
m

<!-- b007119 | prose | pages [24] -->
m

<!-- b007120 | prose | pages [24] -->
m

<!-- b007121 | prose | pages [24] -->
m

<!-- b007122 | prose | pages [24] -->
m

<!-- b007123 | prose | pages [24] -->
m

<!-- b007124 | prose | pages [24] -->
m

<!-- b007125 | prose | pages [24] -->
m

<!-- b007126 | prose | pages [24] -->
m

<!-- b007127 | prose | pages [24] -->
m

<!-- b007128 | prose | pages [24] -->
m

<!-- b007129 | prose | pages [24] -->
m

<!-- b007130 | prose | pages [24] -->
m

<!-- b007131 | prose | pages [24] -->
m

<!-- b007132 | prose | pages [24] -->
m

<!-- b007133 | prose | pages [24] -->
m

<!-- b007134 | prose | pages [24] -->
m

<!-- b007135 | prose | pages [24] -->
m

<!-- b007136 | prose | pages [24] -->
m

<!-- b007137 | prose | pages [24] -->
m

<!-- b007138 | prose | pages [24] -->
m

<!-- b007139 | prose | pages [24] -->
m

<!-- b007140 | prose | pages [24] -->
m

<!-- b007141 | prose | pages [24] -->
m

<!-- b007142 | prose | pages [24] -->
m

<!-- b007143 | prose | pages [24] -->
m

<!-- b007144 | prose | pages [24] -->
m

<!-- b007145 | prose | pages [24] -->
m m

<!-- b007146 | prose | pages [24] -->
m m

<!-- b007147 | prose | pages [24] -->
m m

<!-- b007148 | prose | pages [24] -->
m m

<!-- b007149 | prose | pages [24] -->
m m m m m m

<!-- b007150 | prose | pages [24] -->
select coaches for introduction based on the specific circumstances of different countries.

<!-- b007151 | prose | pages [24] -->
m

<!-- b007152 | prose | pages [24] -->
m

<!-- b007153 | prose | pages [24] -->
m

<!-- b007154 | prose | pages [24] -->
m

<!-- b007155 | prose | pages [24] -->
m

<!-- b007156 | prose | pages [24] -->
m

<!-- b007157 | prose | pages [24] -->
m

<!-- b007158 | prose | pages [24] -->
m

<!-- b007159 | prose | pages [24] -->
m

<!-- b007160 | prose | pages [24] -->
m

<!-- b007161 | prose | pages [24] -->
m

<!-- b007162 | prose | pages [24] -->
m

<!-- b007163 | prose | pages [24] -->
m

<!-- b007164 | prose | pages [24] -->
m

<!-- b007165 | prose | pages [24] -->
m

<!-- b007166 | prose | pages [24] -->
m

<!-- b007167 | prose | pages [24] -->
m

<!-- b007168 | prose | pages [24] -->
m

<!-- b007169 | prose | pages [24] -->
m

<!-- b007170 | prose | pages [24] -->
m

<!-- b007171 | prose | pages [24] -->
m

<!-- b007172 | prose | pages [24] -->
m

<!-- b007173 | prose | pages [24] -->
m

<!-- b007174 | prose | pages [24] -->
m

<!-- b007175 | prose | pages [24] -->
m

<!-- b007176 | prose | pages [24] -->
m

<!-- b007177 | prose | pages [24] -->
m

<!-- b007178 | prose | pages [24] -->
m

<!-- b007179 | prose | pages [24] -->
m

<!-- b007180 | prose | pages [24] -->
m

<!-- b007181 | prose | pages [24] -->
m

<!-- b007182 | prose | pages [24] -->
m

<!-- b007183 | prose | pages [24] -->
m

<!-- b007184 | prose | pages [24] -->
m

<!-- b007185 | prose | pages [24] -->
m

<!-- b007186 | prose | pages [24] -->
m

<!-- b007187 | prose | pages [24] -->
m

<!-- b007188 | prose | pages [24] -->
m

<!-- b007189 | prose | pages [24] -->
m

<!-- b007190 | prose | pages [24] -->
m

<!-- b007191 | prose | pages [24] -->
m

<!-- b007192 | prose | pages [24] -->
m

<!-- b007193 | prose | pages [24] -->
m

<!-- b007194 | prose | pages [24] -->
m

<!-- b007195 | prose | pages [24] -->
m

<!-- b007196 | prose | pages [24] -->
m

<!-- b007197 | prose | pages [24] -->
m

<!-- b007198 | prose | pages [24] -->
m

<!-- b007199 | prose | pages [24] -->
m

<!-- b007200 | prose | pages [24] -->
m

<!-- b007201 | prose | pages [24] -->
m

<!-- b007202 | prose | pages [24] -->
m

<!-- b007203 | prose | pages [24] -->
m

<!-- b007204 | prose | pages [24] -->
m

<!-- b007205 | prose | pages [24] -->
m

<!-- b007206 | prose | pages [24] -->
m

<!-- b007207 | prose | pages [24] -->
m

<!-- b007208 | prose | pages [24] -->
m

<!-- b007209 | prose | pages [24] -->
m

<!-- b007210 | prose | pages [24] -->
m

<!-- b007211 | prose | pages [24] -->
m

<!-- b007212 | prose | pages [24] -->
m

<!-- b007213 | prose | pages [24] -->
m

<!-- b007214 | prose | pages [24] -->
m

<!-- b007215 | prose | pages [24] -->
m

<!-- b007216 | prose | pages [24] -->
m

<!-- b007217 | prose | pages [24] -->
m

<!-- b007218 | prose | pages [24] -->
m

<!-- b007219 | prose | pages [24] -->
m

<!-- b007220 | prose | pages [24] -->
m

<!-- b007221 | prose | pages [24] -->
m

<!-- b007222 | prose | pages [24] -->
m

<!-- b007223 | prose | pages [24] -->
m

<!-- b007224 | prose | pages [24] -->
m

<!-- b007225 | prose | pages [24] -->
m

<!-- b007226 | prose | pages [24] -->
m

<!-- b007227 | prose | pages [24] -->
m

<!-- b007228 | prose | pages [24] -->
m

<!-- b007229 | prose | pages [24] -->
m

<!-- b007230 | prose | pages [24] -->
m

<!-- b007231 | prose | pages [24] -->
m

<!-- b007232 | prose | pages [24] -->
m

<!-- b007233 | prose | pages [24] -->
m

<!-- b007234 | prose | pages [24] -->
m

<!-- b007235 | prose | pages [24] -->
m

<!-- b007236 | prose | pages [24] -->
m

<!-- b007237 | prose | pages [24] -->
m

<!-- b007238 | prose | pages [24] -->
m

<!-- b007239 | prose | pages [24] -->
m

<!-- b007240 | prose | pages [24] -->
m

<!-- b007241 | prose | pages [24] -->
m

<!-- b007242 | prose | pages [24] -->
m

<!-- b007243 | prose | pages [24] -->
m

<!-- b007244 | prose | pages [24] -->
m

<!-- b007245 | prose | pages [24] -->
m

<!-- b007246 | prose | pages [24] -->
m

<!-- b007247 | prose | pages [24] -->
m

<!-- b007248 | prose | pages [24] -->
m

<!-- b007249 | prose | pages [24] -->
m

<!-- b007250 | prose | pages [24] -->
m

<!-- b007251 | prose | pages [24] -->
m

<!-- b007252 | prose | pages [24] -->
m

<!-- b007253 | prose | pages [24] -->
m

<!-- b007254 | prose | pages [24] -->
m

<!-- b007255 | prose | pages [24] -->
m

<!-- b007256 | prose | pages [24] -->
m

<!-- b007257 | prose | pages [24] -->
m

<!-- b007258 | prose | pages [24] -->
m

<!-- b007259 | prose | pages [24] -->
m

<!-- b007260 | prose | pages [24] -->
m

<!-- b007261 | prose | pages [24] -->
m

<!-- b007262 | prose | pages [24] -->
m

<!-- b007263 | prose | pages [24] -->
m

<!-- b007264 | prose | pages [24] -->
m

<!-- b007265 | prose | pages [24] -->
m

<!-- b007266 | prose | pages [24] -->
m

<!-- b007267 | prose | pages [24] -->
m

<!-- b007268 | prose | pages [24] -->
m

<!-- b007269 | prose | pages [24] -->
m

<!-- b007270 | prose | pages [24] -->
m

<!-- b007271 | prose | pages [24] -->
m

<!-- b007272 | prose | pages [24] -->
m

<!-- b007273 | prose | pages [24] -->
m

<!-- b007274 | prose | pages [24] -->
m

<!-- b007275 | prose | pages [24] -->
m

<!-- b007276 | prose | pages [24] -->
m

<!-- b007277 | prose | pages [24] -->
m

<!-- b007278 | prose | pages [24] -->
m

<!-- b007279 | prose | pages [24] -->
m

<!-- b007280 | prose | pages [24] -->
m

<!-- b007281 | prose | pages [24] -->
m

<!-- b007282 | prose | pages [24] -->
m

<!-- b007283 | prose | pages [24] -->
m

<!-- b007284 | prose | pages [24] -->
m

<!-- b007285 | prose | pages [24] -->
m

<!-- b007286 | prose | pages [24] -->
m m

<!-- b007287 | prose | pages [24] -->
m m

<!-- b007288 | prose | pages [24] -->
m m

<!-- b007289 | prose | pages [24] -->
m m

<!-- b007290 | prose | pages [24] -->
m m

<!-- b007291 | prose | pages [24] -->
m m

<!-- b007292 | prose | pages [24] -->
m m m m m m m m

<!-- b007293 | prose | pages [24] -->
Blindly choosing to improve weaknesses may not yield good returns. In addition, our

<!-- b007294 | prose | pages [24] -->
m

<!-- b007295 | prose | pages [24] -->
m

<!-- b007296 | prose | pages [24] -->
m

<!-- b007297 | prose | pages [24] -->
m

<!-- b007298 | prose | pages [24] -->
m

<!-- b007299 | prose | pages [24] -->
m

<!-- b007300 | prose | pages [24] -->
m

<!-- b007301 | prose | pages [24] -->
m

<!-- b007302 | prose | pages [24] -->
m

<!-- b007303 | prose | pages [24] -->
m

<!-- b007304 | prose | pages [24] -->
m

<!-- b007305 | prose | pages [24] -->
m

<!-- b007306 | prose | pages [24] -->
m

<!-- b007307 | prose | pages [24] -->
m

<!-- b007308 | prose | pages [24] -->
m

<!-- b007309 | prose | pages [24] -->
m

<!-- b007310 | prose | pages [24] -->
m

<!-- b007311 | prose | pages [24] -->
m

<!-- b007312 | prose | pages [24] -->
m

<!-- b007313 | prose | pages [24] -->
m

<!-- b007314 | prose | pages [24] -->
m

<!-- b007315 | prose | pages [24] -->
m

<!-- b007316 | prose | pages [24] -->
m

<!-- b007317 | prose | pages [24] -->
m

<!-- b007318 | prose | pages [24] -->
m

<!-- b007319 | prose | pages [24] -->
m

<!-- b007320 | prose | pages [24] -->
m

<!-- b007321 | prose | pages [24] -->
m

<!-- b007322 | prose | pages [24] -->
m

<!-- b007323 | prose | pages [24] -->
m

<!-- b007324 | prose | pages [24] -->
m

<!-- b007325 | prose | pages [24] -->
m

<!-- b007326 | prose | pages [24] -->
m

<!-- b007327 | prose | pages [24] -->
m

<!-- b007328 | prose | pages [24] -->
m

<!-- b007329 | prose | pages [24] -->
m

<!-- b007330 | prose | pages [24] -->
m

<!-- b007331 | prose | pages [24] -->
m

<!-- b007332 | prose | pages [24] -->
m

<!-- b007333 | prose | pages [24] -->
m

<!-- b007334 | prose | pages [24] -->
m

<!-- b007335 | prose | pages [24] -->
m

<!-- b007336 | prose | pages [24] -->
m

<!-- b007337 | prose | pages [24] -->
m

<!-- b007338 | prose | pages [24] -->
m

<!-- b007339 | prose | pages [24] -->
m

<!-- b007340 | prose | pages [24] -->
m

<!-- b007341 | prose | pages [24] -->
m

<!-- b007342 | prose | pages [24] -->
m

<!-- b007343 | prose | pages [24] -->
m

<!-- b007344 | prose | pages [24] -->
m

<!-- b007345 | prose | pages [24] -->
m

<!-- b007346 | prose | pages [24] -->
m

<!-- b007347 | prose | pages [24] -->
m

<!-- b007348 | prose | pages [24] -->
m

<!-- b007349 | prose | pages [24] -->
m

<!-- b007350 | prose | pages [24] -->
m m m m

<!-- b007351 | prose | pages [24] -->
m m

<!-- b007352 | prose | pages [24] -->
m m

<!-- b007353 | prose | pages [24] -->
fitted prediction model can also map out a blueprint for their progress.

<!-- b007354 | prose | pages [24] -->
Extra Study: Impact of Gender Ratio 8.2

<!-- b007355 | prose | pages [24] -->
We analyzed the proportion of women’s points in the Olympics from 1986 to 2024. It was found that from 1896 to 2014, the proportion of women’s points in the Olympics continued to increase, from 5% in 1986 to nearly 50% in 2024, reflecting the increasingly important role of female athletes in international Olympic competitions.

<!-- b007356 | prose | pages [24] -->
We then analyzed countries that performed well at the Olympics, such as the United States and China, and found that the proportion of points scored by female athletes in their Olympic scores was close to 60%, higher than the world average. This indicates that they place great emphasis on the role of female athletes in the overall Olympic performance of their countries.

<!-- b007357 | prose | pages [24] -->
We also analyzed Japan and the UK, two countries with decent Olympic performances, and found that the proportion of points scored by female athletes in their Olympic scores was slightly below 50%. For CUB and UZB, two countries with less than ideal Olympic performances, the proportion of female athletes was only 30%. Therefore, our suggestion is to pay more attention to and cultivate female athletes, which can help to further explore the potential for better national performance in Olympic events.

<!-- b007358 | caption | pages [24] -->
Figure 20: Relationship between predicted score after hiring a coach and the thresholds

<!-- b007359 | prose | pages [24] -->
9

<!-- b007360 | heading | pages [24] -->
Sensitivity Analysis

<!-- b007361 | prose | pages [24] -->
We performed sensitivity analysis for the two thresholds, namely the score difference thresh- old and the score increase rate threshold, which we calculated and employed to detect where great coaches played an important role in sports.

<!-- b007362 | prose | pages [24] -->
We yield the following key observations:

<!-- b007363 | prose | pages [24] -->
关注数学模型

<!-- b007364 | furniture | pages [24] -->
2

<!-- b007365 | furniture | pages [24] -->
MATHmodels

<!-- b007366 | furniture | pages [24] -->
获取更多资讯

<!-- b007367 | furniture | pages [25] -->
Team # 2514461

<!-- b007368 | furniture | pages [25] -->
Page 24 of 25

<!-- b007369 | prose | pages [25] -->
微信公众号：数学模型

<!-- b007370 | caption | pages [25] -->
Figure 21: Relationship between predicted score after hiring a coach and the thresholds

<!-- b007371 | prose | pages [25] -->
• As the rate threshold increases, there is a slight increase in the predicted score, especially

<!-- b007372 | prose | pages [25] -->
微信号：MATHmodels

<!-- b007373 | prose | pages [25] -->
when the score threshold is low. Nevertheless, our model is relatively robust to rate threshold.

<!-- b007374 | prose | pages [25] -->
• The score threshold has a significant impact on the predicted score, especially when set to higher values. A sharp increase in the predicted score is observed as the score threshold approaches higher values, particularly above 7. This suggests that the model is highly sensitive to changes in the score threshold at this range. However, we set rate threshold to 1.2 in the calculations, where the model is not that sensitive to the score threshold.

<!-- b007375 | prose | pages [25] -->
• The shape of the 3D surface agreed to our intuitions, that is, as the threshold is increased, "greater" coaches remain, and these coaches would help the athletes win more medals, and also the more precious ones, leading to a greater increase in predicted scores.

<!-- b007376 | prose | pages [25] -->
• Overall, given that one Gold medal would contribute 3 to the score, our model is rather stable in reasonable ranges of thresholds, which is, 1.2 ≤rate-threshold ≤4, and 3 ≤ score-threshold ≤7.

<!-- b007377 | prose | pages [25] -->
10

<!-- b007378 | heading | pages [25] -->
Strength and Weakness

<!-- b007379 | prose | pages [25] -->
10.1

<!-- b007380 | heading | pages [25] -->
Strength

<!-- b007381 | prose | pages [25] -->
• Reasoning. Our model is constructed from a logical foundation, allowing us to provide more granular details such as the medal count of each country in different disciplines and the winning probability of each first-time medalists, enhancing the accuracy and reliability of our overall predictions.

<!-- b007382 | prose | pages [25] -->
• Comprehensiveness. We took many factors into account like the impact of the host country effect and the association between event count and medal count. In addition, we finished comparative analysis and found better model.

<!-- b007383 | prose | pages [25] -->
• Stability. Our model demonstrates robust stability when thresholds are set within the optimal range, highly adaptable to potential changes in various history data.

<!-- b007384 | prose | pages [25] -->
m

<!-- b007385 | prose | pages [25] -->
m

<!-- b007386 | prose | pages [25] -->
m

<!-- b007387 | prose | pages [25] -->
m

<!-- b007388 | prose | pages [25] -->
m

<!-- b007389 | prose | pages [25] -->
m

<!-- b007390 | prose | pages [25] -->
m

<!-- b007391 | prose | pages [25] -->
m

<!-- b007392 | prose | pages [25] -->
m

<!-- b007393 | prose | pages [25] -->
m

<!-- b007394 | prose | pages [25] -->
m

<!-- b007395 | prose | pages [25] -->
m

<!-- b007396 | prose | pages [25] -->
m

<!-- b007397 | prose | pages [25] -->
m

<!-- b007398 | prose | pages [25] -->
m

<!-- b007399 | prose | pages [25] -->
m

<!-- b007400 | prose | pages [25] -->
m

<!-- b007401 | prose | pages [25] -->
m

<!-- b007402 | prose | pages [25] -->
m

<!-- b007403 | prose | pages [25] -->
m

<!-- b007404 | prose | pages [25] -->
m

<!-- b007405 | prose | pages [25] -->
m

<!-- b007406 | prose | pages [25] -->
m

<!-- b007407 | prose | pages [25] -->
m

<!-- b007408 | prose | pages [25] -->
m

<!-- b007409 | prose | pages [25] -->
m

<!-- b007410 | prose | pages [25] -->
m

<!-- b007411 | prose | pages [25] -->
m

<!-- b007412 | prose | pages [25] -->
m

<!-- b007413 | prose | pages [25] -->
m

<!-- b007414 | prose | pages [25] -->
m

<!-- b007415 | prose | pages [25] -->
m

<!-- b007416 | prose | pages [25] -->
m

<!-- b007417 | prose | pages [25] -->
m

<!-- b007418 | prose | pages [25] -->
m

<!-- b007419 | prose | pages [25] -->
m

<!-- b007420 | prose | pages [25] -->
m

<!-- b007421 | prose | pages [25] -->
m

<!-- b007422 | prose | pages [25] -->
m

<!-- b007423 | prose | pages [25] -->
m

<!-- b007424 | prose | pages [25] -->
m

<!-- b007425 | prose | pages [25] -->
m

<!-- b007426 | prose | pages [25] -->
m

<!-- b007427 | prose | pages [25] -->
m

<!-- b007428 | prose | pages [25] -->
m

<!-- b007429 | prose | pages [25] -->
m

<!-- b007430 | prose | pages [25] -->
m

<!-- b007431 | prose | pages [25] -->
m

<!-- b007432 | prose | pages [25] -->
m

<!-- b007433 | prose | pages [25] -->
m

<!-- b007434 | prose | pages [25] -->
m

<!-- b007435 | prose | pages [25] -->
m

<!-- b007436 | prose | pages [25] -->
m

<!-- b007437 | prose | pages [25] -->
m

<!-- b007438 | prose | pages [25] -->
m

<!-- b007439 | prose | pages [25] -->
m

<!-- b007440 | prose | pages [25] -->
m

<!-- b007441 | prose | pages [25] -->
m

<!-- b007442 | prose | pages [25] -->
m

<!-- b007443 | prose | pages [25] -->
m

<!-- b007444 | prose | pages [25] -->
m

<!-- b007445 | prose | pages [25] -->
m

<!-- b007446 | prose | pages [25] -->
m

<!-- b007447 | prose | pages [25] -->
m

<!-- b007448 | prose | pages [25] -->
m

<!-- b007449 | prose | pages [25] -->
m

<!-- b007450 | prose | pages [25] -->
m

<!-- b007451 | prose | pages [25] -->
m

<!-- b007452 | prose | pages [25] -->
m

<!-- b007453 | prose | pages [25] -->
m

<!-- b007454 | prose | pages [25] -->
m

<!-- b007455 | prose | pages [25] -->
m

<!-- b007456 | prose | pages [25] -->
m

<!-- b007457 | prose | pages [25] -->
m

<!-- b007458 | prose | pages [25] -->
m

<!-- b007459 | prose | pages [25] -->
m

<!-- b007460 | prose | pages [25] -->
m

<!-- b007461 | prose | pages [25] -->
m

<!-- b007462 | prose | pages [25] -->
m

<!-- b007463 | prose | pages [25] -->
m

<!-- b007464 | prose | pages [25] -->
m

<!-- b007465 | prose | pages [25] -->
m

<!-- b007466 | prose | pages [25] -->
m

<!-- b007467 | prose | pages [25] -->
m

<!-- b007468 | prose | pages [25] -->
m

<!-- b007469 | prose | pages [25] -->
m

<!-- b007470 | prose | pages [25] -->
m

<!-- b007471 | prose | pages [25] -->
m

<!-- b007472 | prose | pages [25] -->
m

<!-- b007473 | prose | pages [25] -->
m

<!-- b007474 | prose | pages [25] -->
m

<!-- b007475 | prose | pages [25] -->
m

<!-- b007476 | prose | pages [25] -->
m

<!-- b007477 | prose | pages [25] -->
m

<!-- b007478 | prose | pages [25] -->
m

<!-- b007479 | prose | pages [25] -->
m

<!-- b007480 | prose | pages [25] -->
m

<!-- b007481 | prose | pages [25] -->
m

<!-- b007482 | prose | pages [25] -->
m

<!-- b007483 | prose | pages [25] -->
m

<!-- b007484 | prose | pages [25] -->
m

<!-- b007485 | prose | pages [25] -->
m

<!-- b007486 | prose | pages [25] -->
m

<!-- b007487 | prose | pages [25] -->
m

<!-- b007488 | prose | pages [25] -->
m

<!-- b007489 | prose | pages [25] -->
m

<!-- b007490 | prose | pages [25] -->
m

<!-- b007491 | prose | pages [25] -->
m

<!-- b007492 | prose | pages [25] -->
m

<!-- b007493 | prose | pages [25] -->
m

<!-- b007494 | prose | pages [25] -->
m

<!-- b007495 | prose | pages [25] -->
m

<!-- b007496 | prose | pages [25] -->
m

<!-- b007497 | prose | pages [25] -->
m

<!-- b007498 | prose | pages [25] -->
m

<!-- b007499 | prose | pages [25] -->
m

<!-- b007500 | prose | pages [25] -->
m

<!-- b007501 | prose | pages [25] -->
m

<!-- b007502 | prose | pages [25] -->
m

<!-- b007503 | prose | pages [25] -->
m

<!-- b007504 | prose | pages [25] -->
m

<!-- b007505 | prose | pages [25] -->
m

<!-- b007506 | prose | pages [25] -->
m

<!-- b007507 | prose | pages [25] -->
m

<!-- b007508 | prose | pages [25] -->
m

<!-- b007509 | prose | pages [25] -->
m

<!-- b007510 | prose | pages [25] -->
m

<!-- b007511 | prose | pages [25] -->
m

<!-- b007512 | prose | pages [25] -->
m

<!-- b007513 | prose | pages [25] -->
m

<!-- b007514 | prose | pages [25] -->
m

<!-- b007515 | prose | pages [25] -->
m

<!-- b007516 | prose | pages [25] -->
m

<!-- b007517 | prose | pages [25] -->
m

<!-- b007518 | prose | pages [25] -->
m

<!-- b007519 | prose | pages [25] -->
m

<!-- b007520 | prose | pages [25] -->
m

<!-- b007521 | prose | pages [25] -->
m

<!-- b007522 | prose | pages [25] -->
m

<!-- b007523 | prose | pages [25] -->
m

<!-- b007524 | prose | pages [25] -->
m

<!-- b007525 | prose | pages [25] -->
m

<!-- b007526 | prose | pages [25] -->
m

<!-- b007527 | prose | pages [25] -->
m

<!-- b007528 | prose | pages [25] -->
m

<!-- b007529 | prose | pages [25] -->
m

<!-- b007530 | prose | pages [25] -->
m

<!-- b007531 | prose | pages [25] -->
m

<!-- b007532 | prose | pages [25] -->
m

<!-- b007533 | prose | pages [25] -->
m

<!-- b007534 | prose | pages [25] -->
m

<!-- b007535 | prose | pages [25] -->
m

<!-- b007536 | prose | pages [25] -->
m

<!-- b007537 | prose | pages [25] -->
m

<!-- b007538 | prose | pages [25] -->
m

<!-- b007539 | prose | pages [25] -->
m

<!-- b007540 | prose | pages [25] -->
m

<!-- b007541 | prose | pages [25] -->
m

<!-- b007542 | prose | pages [25] -->
m

<!-- b007543 | prose | pages [25] -->
m

<!-- b007544 | prose | pages [25] -->
m

<!-- b007545 | prose | pages [25] -->
m

<!-- b007546 | prose | pages [25] -->
m

<!-- b007547 | prose | pages [25] -->
m

<!-- b007548 | prose | pages [25] -->
m

<!-- b007549 | prose | pages [25] -->
m

<!-- b007550 | prose | pages [25] -->
m

<!-- b007551 | prose | pages [25] -->
m

<!-- b007552 | prose | pages [25] -->
m

<!-- b007553 | prose | pages [25] -->
m

<!-- b007554 | prose | pages [25] -->
m

<!-- b007555 | prose | pages [25] -->
m

<!-- b007556 | prose | pages [25] -->
m

<!-- b007557 | prose | pages [25] -->
m

<!-- b007558 | prose | pages [25] -->
m

<!-- b007559 | prose | pages [25] -->
m

<!-- b007560 | prose | pages [25] -->
m

<!-- b007561 | prose | pages [25] -->
m

<!-- b007562 | prose | pages [25] -->
m

<!-- b007563 | prose | pages [25] -->
m

<!-- b007564 | prose | pages [25] -->
m

<!-- b007565 | prose | pages [25] -->
m

<!-- b007566 | prose | pages [25] -->
m

<!-- b007567 | prose | pages [25] -->
m

<!-- b007568 | prose | pages [25] -->
m

<!-- b007569 | prose | pages [25] -->
m

<!-- b007570 | prose | pages [25] -->
m

<!-- b007571 | prose | pages [25] -->
m

<!-- b007572 | prose | pages [25] -->
m

<!-- b007573 | prose | pages [25] -->
m

<!-- b007574 | prose | pages [25] -->
m

<!-- b007575 | prose | pages [25] -->
m

<!-- b007576 | prose | pages [25] -->
m

<!-- b007577 | prose | pages [25] -->
m

<!-- b007578 | prose | pages [25] -->
m

<!-- b007579 | prose | pages [25] -->
m

<!-- b007580 | prose | pages [25] -->
m

<!-- b007581 | prose | pages [25] -->
m

<!-- b007582 | prose | pages [25] -->
m

<!-- b007583 | prose | pages [25] -->
m

<!-- b007584 | prose | pages [25] -->
m

<!-- b007585 | prose | pages [25] -->
m

<!-- b007586 | prose | pages [25] -->
m

<!-- b007587 | prose | pages [25] -->
m

<!-- b007588 | prose | pages [25] -->
m

<!-- b007589 | prose | pages [25] -->
m

<!-- b007590 | prose | pages [25] -->
m

<!-- b007591 | prose | pages [25] -->
m

<!-- b007592 | prose | pages [25] -->
m

<!-- b007593 | prose | pages [25] -->
m

<!-- b007594 | prose | pages [25] -->
m

<!-- b007595 | prose | pages [25] -->
m

<!-- b007596 | prose | pages [25] -->
m

<!-- b007597 | prose | pages [25] -->
m

<!-- b007598 | prose | pages [25] -->
m

<!-- b007599 | prose | pages [25] -->
m

<!-- b007600 | prose | pages [25] -->
m

<!-- b007601 | prose | pages [25] -->
m

<!-- b007602 | prose | pages [25] -->
m

<!-- b007603 | prose | pages [25] -->
m

<!-- b007604 | prose | pages [25] -->
m

<!-- b007605 | prose | pages [25] -->
m

<!-- b007606 | prose | pages [25] -->
m

<!-- b007607 | prose | pages [25] -->
m

<!-- b007608 | prose | pages [25] -->
m

<!-- b007609 | prose | pages [25] -->
m

<!-- b007610 | prose | pages [25] -->
m

<!-- b007611 | prose | pages [25] -->
m

<!-- b007612 | prose | pages [25] -->
m

<!-- b007613 | prose | pages [25] -->
m

<!-- b007614 | prose | pages [25] -->
m

<!-- b007615 | prose | pages [25] -->
m

<!-- b007616 | prose | pages [25] -->
m

<!-- b007617 | prose | pages [25] -->
m

<!-- b007618 | prose | pages [25] -->
m

<!-- b007619 | prose | pages [25] -->
m

<!-- b007620 | prose | pages [25] -->
m

<!-- b007621 | prose | pages [25] -->
m

<!-- b007622 | prose | pages [25] -->
m

<!-- b007623 | prose | pages [25] -->
m

<!-- b007624 | prose | pages [25] -->
m

<!-- b007625 | prose | pages [25] -->
m

<!-- b007626 | prose | pages [25] -->
m

<!-- b007627 | prose | pages [25] -->
m

<!-- b007628 | prose | pages [25] -->
m

<!-- b007629 | prose | pages [25] -->
m

<!-- b007630 | prose | pages [25] -->
m

<!-- b007631 | prose | pages [25] -->
m

<!-- b007632 | prose | pages [25] -->
m

<!-- b007633 | prose | pages [25] -->
m

<!-- b007634 | prose | pages [25] -->
m

<!-- b007635 | prose | pages [25] -->
m

<!-- b007636 | prose | pages [25] -->
m

<!-- b007637 | prose | pages [25] -->
m

<!-- b007638 | prose | pages [25] -->
m

<!-- b007639 | prose | pages [25] -->
m

<!-- b007640 | prose | pages [25] -->
m

<!-- b007641 | prose | pages [25] -->
m

<!-- b007642 | prose | pages [25] -->
m

<!-- b007643 | prose | pages [25] -->
m

<!-- b007644 | prose | pages [25] -->
m

<!-- b007645 | prose | pages [25] -->
m

<!-- b007646 | prose | pages [25] -->
m

<!-- b007647 | prose | pages [25] -->
m

<!-- b007648 | prose | pages [25] -->
m

<!-- b007649 | prose | pages [25] -->
m

<!-- b007650 | prose | pages [25] -->
m

<!-- b007651 | prose | pages [25] -->
m

<!-- b007652 | prose | pages [25] -->
m

<!-- b007653 | prose | pages [25] -->
m

<!-- b007654 | prose | pages [25] -->
m

<!-- b007655 | prose | pages [25] -->
m

<!-- b007656 | prose | pages [25] -->
m

<!-- b007657 | prose | pages [25] -->
m

<!-- b007658 | prose | pages [25] -->
m

<!-- b007659 | prose | pages [25] -->
m

<!-- b007660 | prose | pages [25] -->
m

<!-- b007661 | prose | pages [25] -->
m

<!-- b007662 | prose | pages [25] -->
m

<!-- b007663 | prose | pages [25] -->
m

<!-- b007664 | prose | pages [25] -->
m

<!-- b007665 | prose | pages [25] -->
m

<!-- b007666 | prose | pages [25] -->
m

<!-- b007667 | prose | pages [25] -->
m

<!-- b007668 | furniture | pages [25] -->
m

<!-- b007669 | furniture | pages [25] -->
m

<!-- b007670 | furniture | pages [25] -->
m

<!-- b007671 | furniture | pages [25] -->
m

<!-- b007672 | furniture | pages [25] -->
m

<!-- b007673 | furniture | pages [25] -->
m

<!-- b007674 | furniture | pages [25] -->
m

<!-- b007675 | furniture | pages [25] -->
m

<!-- b007676 | furniture | pages [25] -->
m

<!-- b007677 | furniture | pages [25] -->
m

<!-- b007678 | furniture | pages [25] -->
m

<!-- b007679 | furniture | pages [25] -->
m

<!-- b007680 | furniture | pages [25] -->
m

<!-- b007681 | furniture | pages [25] -->
m

<!-- b007682 | furniture | pages [25] -->
m

<!-- b007683 | furniture | pages [25] -->
m

<!-- b007684 | furniture | pages [25] -->
m

<!-- b007685 | furniture | pages [25] -->
m

<!-- b007686 | furniture | pages [25] -->
m

<!-- b007687 | furniture | pages [25] -->
m

<!-- b007688 | furniture | pages [25] -->
m

<!-- b007689 | furniture | pages [25] -->
m

<!-- b007690 | furniture | pages [25] -->
m

<!-- b007691 | furniture | pages [25] -->
m

<!-- b007692 | furniture | pages [25] -->
m

<!-- b007693 | furniture | pages [25] -->
m

<!-- b007694 | furniture | pages [25] -->
m

<!-- b007695 | furniture | pages [25] -->
m

<!-- b007696 | furniture | pages [25] -->
m

<!-- b007697 | furniture | pages [25] -->
m

<!-- b007698 | furniture | pages [25] -->
m

<!-- b007699 | furniture | pages [25] -->
m

<!-- b007700 | furniture | pages [25] -->
m

<!-- b007701 | furniture | pages [25] -->
m

<!-- b007702 | furniture | pages [25] -->
m

<!-- b007703 | furniture | pages [25] -->
m

<!-- b007704 | furniture | pages [25] -->
m

<!-- b007705 | furniture | pages [25] -->
m

<!-- b007706 | furniture | pages [25] -->
m

<!-- b007707 | furniture | pages [25] -->
m

<!-- b007708 | furniture | pages [25] -->
m

<!-- b007709 | furniture | pages [25] -->
m

<!-- b007710 | furniture | pages [25] -->
m

<!-- b007711 | furniture | pages [25] -->
m

<!-- b007712 | furniture | pages [25] -->
m

<!-- b007713 | furniture | pages [25] -->
m

<!-- b007714 | furniture | pages [25] -->
m

<!-- b007715 | furniture | pages [25] -->
m

<!-- b007716 | furniture | pages [25] -->
m

<!-- b007717 | furniture | pages [25] -->
m

<!-- b007718 | furniture | pages [25] -->
m

<!-- b007719 | furniture | pages [25] -->
m

<!-- b007720 | furniture | pages [25] -->
m

<!-- b007721 | furniture | pages [25] -->
m

<!-- b007722 | furniture | pages [25] -->
m

<!-- b007723 | furniture | pages [25] -->
m

<!-- b007724 | furniture | pages [25] -->
m

<!-- b007725 | furniture | pages [25] -->
m

<!-- b007726 | furniture | pages [25] -->
m

<!-- b007727 | furniture | pages [25] -->
m

<!-- b007728 | furniture | pages [25] -->
m

<!-- b007729 | furniture | pages [25] -->
m

<!-- b007730 | furniture | pages [25] -->
m

<!-- b007731 | furniture | pages [25] -->
m

<!-- b007732 | furniture | pages [25] -->
m

<!-- b007733 | furniture | pages [25] -->
m

<!-- b007734 | furniture | pages [25] -->
m

<!-- b007735 | furniture | pages [25] -->
m

<!-- b007736 | furniture | pages [25] -->
m

<!-- b007737 | furniture | pages [25] -->
m

<!-- b007738 | furniture | pages [25] -->
m

<!-- b007739 | furniture | pages [25] -->
m

<!-- b007740 | furniture | pages [25] -->
m

<!-- b007741 | furniture | pages [25] -->
m

<!-- b007742 | furniture | pages [25] -->
m

<!-- b007743 | furniture | pages [25] -->
m

<!-- b007744 | furniture | pages [25] -->
m

<!-- b007745 | furniture | pages [25] -->
m

<!-- b007746 | furniture | pages [25] -->
m

<!-- b007747 | furniture | pages [25] -->
m

<!-- b007748 | furniture | pages [25] -->
m

<!-- b007749 | furniture | pages [25] -->
m

<!-- b007750 | furniture | pages [25] -->
m

<!-- b007751 | furniture | pages [25] -->
m

<!-- b007752 | furniture | pages [25] -->
m

<!-- b007753 | furniture | pages [25] -->
m

<!-- b007754 | furniture | pages [25] -->
m

<!-- b007755 | furniture | pages [25] -->
m

<!-- b007756 | furniture | pages [25] -->
m

<!-- b007757 | furniture | pages [25] -->
m

<!-- b007758 | furniture | pages [25] -->
m

<!-- b007759 | furniture | pages [25] -->
m

<!-- b007760 | furniture | pages [25] -->
m

<!-- b007761 | furniture | pages [25] -->
m

<!-- b007762 | furniture | pages [25] -->
m

<!-- b007763 | furniture | pages [25] -->
m

<!-- b007764 | furniture | pages [25] -->
m

<!-- b007765 | furniture | pages [25] -->
m

<!-- b007766 | furniture | pages [25] -->
m

<!-- b007767 | furniture | pages [25] -->
m

<!-- b007768 | furniture | pages [25] -->
m

<!-- b007769 | furniture | pages [25] -->
m

<!-- b007770 | furniture | pages [25] -->
m

<!-- b007771 | furniture | pages [25] -->
m

<!-- b007772 | furniture | pages [25] -->
m

<!-- b007773 | furniture | pages [25] -->
m

<!-- b007774 | furniture | pages [25] -->
m

<!-- b007775 | furniture | pages [25] -->
m

<!-- b007776 | furniture | pages [25] -->
m

<!-- b007777 | furniture | pages [25] -->
m

<!-- b007778 | furniture | pages [25] -->
m

<!-- b007779 | furniture | pages [25] -->
m

<!-- b007780 | furniture | pages [25] -->
m

<!-- b007781 | furniture | pages [25] -->
m

<!-- b007782 | furniture | pages [25] -->
m

<!-- b007783 | furniture | pages [25] -->
m

<!-- b007784 | furniture | pages [25] -->
m

<!-- b007785 | furniture | pages [25] -->
m

<!-- b007786 | furniture | pages [25] -->
m

<!-- b007787 | furniture | pages [25] -->
m

<!-- b007788 | furniture | pages [25] -->
m

<!-- b007789 | furniture | pages [25] -->
m

<!-- b007790 | furniture | pages [25] -->
m

<!-- b007791 | furniture | pages [25] -->
m

<!-- b007792 | furniture | pages [25] -->
m

<!-- b007793 | furniture | pages [25] -->
m

<!-- b007794 | furniture | pages [25] -->
m

<!-- b007795 | furniture | pages [25] -->
m

<!-- b007796 | furniture | pages [25] -->
m

<!-- b007797 | furniture | pages [25] -->
m

<!-- b007798 | furniture | pages [25] -->
m

<!-- b007799 | furniture | pages [25] -->
m

<!-- b007800 | furniture | pages [25] -->
m

<!-- b007801 | furniture | pages [25] -->
m

<!-- b007802 | furniture | pages [25] -->
m

<!-- b007803 | furniture | pages [25] -->
m

<!-- b007804 | furniture | pages [25] -->
m

<!-- b007805 | furniture | pages [25] -->
m

<!-- b007806 | furniture | pages [25] -->
m

<!-- b007807 | furniture | pages [25] -->
m

<!-- b007808 | furniture | pages [25] -->
m

<!-- b007809 | furniture | pages [25] -->
m

<!-- b007810 | furniture | pages [25] -->
m

<!-- b007811 | furniture | pages [25] -->
m

<!-- b007812 | furniture | pages [25] -->
m

<!-- b007813 | furniture | pages [25] -->
m

<!-- b007814 | furniture | pages [25] -->
m

<!-- b007815 | furniture | pages [25] -->
m

<!-- b007816 | furniture | pages [25] -->
m

<!-- b007817 | furniture | pages [25] -->
m

<!-- b007818 | furniture | pages [25] -->
m

<!-- b007819 | furniture | pages [25] -->
m

<!-- b007820 | furniture | pages [25] -->
m

<!-- b007821 | furniture | pages [25] -->
m

<!-- b007822 | furniture | pages [25] -->
m

<!-- b007823 | furniture | pages [25] -->
m

<!-- b007824 | furniture | pages [25] -->
m

<!-- b007825 | furniture | pages [25] -->
m

<!-- b007826 | furniture | pages [25] -->
m

<!-- b007827 | furniture | pages [25] -->
m

<!-- b007828 | furniture | pages [25] -->
m

<!-- b007829 | furniture | pages [25] -->
m

<!-- b007830 | furniture | pages [25] -->
m

<!-- b007831 | furniture | pages [25] -->
m

<!-- b007832 | furniture | pages [25] -->
m

<!-- b007833 | furniture | pages [25] -->
m

<!-- b007834 | furniture | pages [25] -->
m

<!-- b007835 | furniture | pages [25] -->
m

<!-- b007836 | furniture | pages [25] -->
m

<!-- b007837 | furniture | pages [25] -->
m

<!-- b007838 | furniture | pages [25] -->
m

<!-- b007839 | furniture | pages [25] -->
m

<!-- b007840 | furniture | pages [25] -->
m

<!-- b007841 | furniture | pages [25] -->
m

<!-- b007842 | furniture | pages [25] -->
m

<!-- b007843 | furniture | pages [25] -->
m

<!-- b007844 | furniture | pages [25] -->
m

<!-- b007845 | furniture | pages [25] -->
m

<!-- b007846 | furniture | pages [25] -->
m

<!-- b007847 | furniture | pages [25] -->
m

<!-- b007848 | furniture | pages [25] -->
m

<!-- b007849 | furniture | pages [25] -->
m

<!-- b007850 | furniture | pages [25] -->
m

<!-- b007851 | furniture | pages [25] -->
m

<!-- b007852 | furniture | pages [25] -->
m

<!-- b007853 | furniture | pages [25] -->
m

<!-- b007854 | furniture | pages [25] -->
m

<!-- b007855 | furniture | pages [25] -->
m

<!-- b007856 | furniture | pages [25] -->
m

<!-- b007857 | furniture | pages [25] -->
m

<!-- b007858 | furniture | pages [25] -->
m

<!-- b007859 | furniture | pages [25] -->
m

<!-- b007860 | furniture | pages [25] -->
m

<!-- b007861 | furniture | pages [25] -->
m

<!-- b007862 | furniture | pages [25] -->
m

<!-- b007863 | furniture | pages [25] -->
m

<!-- b007864 | furniture | pages [25] -->
m

<!-- b007865 | furniture | pages [25] -->
m

<!-- b007866 | furniture | pages [25] -->
m

<!-- b007867 | furniture | pages [25] -->
m

<!-- b007868 | furniture | pages [25] -->
m

<!-- b007869 | furniture | pages [25] -->
m

<!-- b007870 | furniture | pages [25] -->
m

<!-- b007871 | furniture | pages [25] -->
m

<!-- b007872 | furniture | pages [25] -->
m

<!-- b007873 | furniture | pages [25] -->
m

<!-- b007874 | furniture | pages [25] -->
m

<!-- b007875 | furniture | pages [25] -->
m

<!-- b007876 | furniture | pages [25] -->
m

<!-- b007877 | furniture | pages [25] -->
m

<!-- b007878 | furniture | pages [25] -->
m

<!-- b007879 | furniture | pages [25] -->
m

<!-- b007880 | furniture | pages [25] -->
m

<!-- b007881 | furniture | pages [25] -->
m

<!-- b007882 | furniture | pages [25] -->
m

<!-- b007883 | furniture | pages [25] -->
m

<!-- b007884 | furniture | pages [25] -->
m

<!-- b007885 | furniture | pages [25] -->
m

<!-- b007886 | furniture | pages [25] -->
m

<!-- b007887 | furniture | pages [25] -->
m

<!-- b007888 | furniture | pages [25] -->
m

<!-- b007889 | furniture | pages [25] -->
m

<!-- b007890 | furniture | pages [25] -->
m

<!-- b007891 | furniture | pages [25] -->
m

<!-- b007892 | furniture | pages [25] -->
m

<!-- b007893 | furniture | pages [25] -->
m

<!-- b007894 | furniture | pages [25] -->
m

<!-- b007895 | furniture | pages [25] -->
m

<!-- b007896 | furniture | pages [25] -->
m

<!-- b007897 | furniture | pages [25] -->
m

<!-- b007898 | furniture | pages [25] -->
m

<!-- b007899 | furniture | pages [25] -->
m

<!-- b007900 | furniture | pages [25] -->
m

<!-- b007901 | furniture | pages [25] -->
m

<!-- b007902 | furniture | pages [25] -->
m

<!-- b007903 | furniture | pages [25] -->
m

<!-- b007904 | furniture | pages [25] -->
m

<!-- b007905 | furniture | pages [25] -->
m

<!-- b007906 | furniture | pages [25] -->
m

<!-- b007907 | furniture | pages [25] -->
m

<!-- b007908 | furniture | pages [25] -->
m

<!-- b007909 | furniture | pages [25] -->
m

<!-- b007910 | furniture | pages [25] -->
m

<!-- b007911 | furniture | pages [25] -->
m

<!-- b007912 | furniture | pages [25] -->
m

<!-- b007913 | furniture | pages [25] -->
m

<!-- b007914 | furniture | pages [25] -->
m

<!-- b007915 | furniture | pages [25] -->
m

<!-- b007916 | furniture | pages [25] -->
m

<!-- b007917 | furniture | pages [25] -->
m

<!-- b007918 | furniture | pages [25] -->
m

<!-- b007919 | furniture | pages [25] -->
m

<!-- b007920 | furniture | pages [25] -->
m

<!-- b007921 | furniture | pages [25] -->
m

<!-- b007922 | furniture | pages [25] -->
m

<!-- b007923 | furniture | pages [25] -->
m

<!-- b007924 | furniture | pages [25] -->
m

<!-- b007925 | furniture | pages [25] -->
m

<!-- b007926 | furniture | pages [25] -->
m

<!-- b007927 | furniture | pages [25] -->
m

<!-- b007928 | furniture | pages [25] -->
m

<!-- b007929 | furniture | pages [25] -->
m

<!-- b007930 | furniture | pages [25] -->
m

<!-- b007931 | furniture | pages [25] -->
m

<!-- b007932 | furniture | pages [25] -->
m

<!-- b007933 | furniture | pages [25] -->
m

<!-- b007934 | furniture | pages [25] -->
m

<!-- b007935 | furniture | pages [25] -->
m

<!-- b007936 | furniture | pages [25] -->
m

<!-- b007937 | furniture | pages [25] -->
m

<!-- b007938 | furniture | pages [25] -->
m

<!-- b007939 | furniture | pages [25] -->
m

<!-- b007940 | furniture | pages [25] -->
m

<!-- b007941 | furniture | pages [25] -->
m

<!-- b007942 | furniture | pages [25] -->
m

<!-- b007943 | furniture | pages [25] -->
m

<!-- b007944 | furniture | pages [25] -->
m

<!-- b007945 | furniture | pages [25] -->
m

<!-- b007946 | furniture | pages [25] -->
m

<!-- b007947 | furniture | pages [25] -->
m

<!-- b007948 | furniture | pages [25] -->
m

<!-- b007949 | furniture | pages [25] -->
m

<!-- b007950 | furniture | pages [25] -->
m

<!-- b007951 | furniture | pages [25] -->
m

<!-- b007952 | furniture | pages [25] -->
m

<!-- b007953 | furniture | pages [25] -->
m

<!-- b007954 | furniture | pages [25] -->
m

<!-- b007955 | furniture | pages [25] -->
m

<!-- b007956 | furniture | pages [25] -->
m

<!-- b007957 | furniture | pages [25] -->
m

<!-- b007958 | furniture | pages [25] -->
m

<!-- b007959 | furniture | pages [25] -->
m

<!-- b007960 | furniture | pages [25] -->
m

<!-- b007961 | furniture | pages [25] -->
m

<!-- b007962 | furniture | pages [25] -->
m

<!-- b007963 | furniture | pages [25] -->
m

<!-- b007964 | furniture | pages [25] -->
m

<!-- b007965 | furniture | pages [25] -->
m

<!-- b007966 | furniture | pages [25] -->
m

<!-- b007967 | furniture | pages [25] -->
m

<!-- b007968 | furniture | pages [25] -->
m

<!-- b007969 | furniture | pages [25] -->
m

<!-- b007970 | furniture | pages [25] -->
m

<!-- b007971 | furniture | pages [25] -->
m

<!-- b007972 | furniture | pages [25] -->
m

<!-- b007973 | furniture | pages [25] -->
m

<!-- b007974 | furniture | pages [25] -->
m

<!-- b007975 | furniture | pages [25] -->
m

<!-- b007976 | furniture | pages [25] -->
m

<!-- b007977 | furniture | pages [25] -->
m

<!-- b007978 | furniture | pages [25] -->
m

<!-- b007979 | furniture | pages [25] -->
m

<!-- b007980 | furniture | pages [25] -->
m

<!-- b007981 | furniture | pages [25] -->
m

<!-- b007982 | furniture | pages [25] -->
m

<!-- b007983 | furniture | pages [25] -->
m

<!-- b007984 | furniture | pages [25] -->
m

<!-- b007985 | furniture | pages [25] -->
m

<!-- b007986 | furniture | pages [25] -->
m

<!-- b007987 | furniture | pages [25] -->
m

<!-- b007988 | furniture | pages [25] -->
m

<!-- b007989 | furniture | pages [25] -->
m

<!-- b007990 | furniture | pages [25] -->
m

<!-- b007991 | furniture | pages [25] -->
m

<!-- b007992 | furniture | pages [25] -->
m

<!-- b007993 | furniture | pages [25] -->
m

<!-- b007994 | furniture | pages [25] -->
m

<!-- b007995 | furniture | pages [25] -->
m

<!-- b007996 | furniture | pages [25] -->
m

<!-- b007997 | furniture | pages [25] -->
m

<!-- b007998 | furniture | pages [25] -->
m

<!-- b007999 | furniture | pages [25] -->
m

<!-- b008000 | furniture | pages [25] -->
m

<!-- b008001 | furniture | pages [25] -->
m

<!-- b008002 | furniture | pages [25] -->
m

<!-- b008003 | furniture | pages [25] -->
m

<!-- b008004 | furniture | pages [25] -->
m

<!-- b008005 | furniture | pages [25] -->
m

<!-- b008006 | furniture | pages [25] -->
m

<!-- b008007 | furniture | pages [25] -->
m

<!-- b008008 | furniture | pages [25] -->
m

<!-- b008009 | furniture | pages [25] -->
m

<!-- b008010 | furniture | pages [25] -->
m

<!-- b008011 | furniture | pages [25] -->
m

<!-- b008012 | furniture | pages [25] -->
m

<!-- b008013 | furniture | pages [25] -->
m

<!-- b008014 | furniture | pages [25] -->
m

<!-- b008015 | furniture | pages [25] -->
m

<!-- b008016 | furniture | pages [25] -->
m

<!-- b008017 | furniture | pages [25] -->
m

<!-- b008018 | furniture | pages [25] -->
m

<!-- b008019 | furniture | pages [25] -->
m

<!-- b008020 | furniture | pages [25] -->
m

<!-- b008021 | furniture | pages [25] -->
m

<!-- b008022 | furniture | pages [25] -->
m

<!-- b008023 | furniture | pages [25] -->
m

<!-- b008024 | furniture | pages [25] -->
m

<!-- b008025 | furniture | pages [25] -->
m

<!-- b008026 | furniture | pages [25] -->
m

<!-- b008027 | furniture | pages [25] -->
m

<!-- b008028 | furniture | pages [25] -->
m

<!-- b008029 | furniture | pages [25] -->
m

<!-- b008030 | furniture | pages [25] -->
m

<!-- b008031 | furniture | pages [25] -->
m

<!-- b008032 | furniture | pages [25] -->
m

<!-- b008033 | furniture | pages [25] -->
m

<!-- b008034 | furniture | pages [25] -->
m

<!-- b008035 | furniture | pages [25] -->
m

<!-- b008036 | furniture | pages [25] -->
m

<!-- b008037 | furniture | pages [25] -->
m

<!-- b008038 | furniture | pages [25] -->
m

<!-- b008039 | furniture | pages [25] -->
m

<!-- b008040 | furniture | pages [25] -->
m

<!-- b008041 | furniture | pages [25] -->
m

<!-- b008042 | furniture | pages [25] -->
m

<!-- b008043 | furniture | pages [25] -->
m

<!-- b008044 | furniture | pages [25] -->
m

<!-- b008045 | furniture | pages [25] -->
m

<!-- b008046 | furniture | pages [25] -->
m

<!-- b008047 | furniture | pages [25] -->
m

<!-- b008048 | furniture | pages [25] -->
m

<!-- b008049 | furniture | pages [25] -->
m

<!-- b008050 | furniture | pages [25] -->
m

<!-- b008051 | furniture | pages [25] -->
m

<!-- b008052 | furniture | pages [25] -->
m

<!-- b008053 | furniture | pages [25] -->
m

<!-- b008054 | furniture | pages [25] -->
m

<!-- b008055 | furniture | pages [25] -->
m

<!-- b008056 | furniture | pages [25] -->
m

<!-- b008057 | furniture | pages [25] -->
m

<!-- b008058 | furniture | pages [25] -->
m

<!-- b008059 | furniture | pages [25] -->
m

<!-- b008060 | furniture | pages [25] -->
m

<!-- b008061 | furniture | pages [25] -->
m

<!-- b008062 | furniture | pages [25] -->
m

<!-- b008063 | furniture | pages [25] -->
m

<!-- b008064 | furniture | pages [25] -->
m

<!-- b008065 | furniture | pages [25] -->
m

<!-- b008066 | furniture | pages [25] -->
m

<!-- b008067 | furniture | pages [25] -->
m

<!-- b008068 | furniture | pages [25] -->
m

<!-- b008069 | furniture | pages [25] -->
m

<!-- b008070 | furniture | pages [25] -->
m

<!-- b008071 | furniture | pages [26] -->
Team # 2514461

<!-- b008072 | prose | pages [26] -->
10.2

<!-- b008073 | heading | pages [26] -->
Weakness

<!-- b008074 | furniture | pages [26] -->
Page 25 of 25

<!-- b008075 | prose | pages [26] -->
• Idealization. Despite the fact that we have already conducted a detailed analysis of datasets and fitted a prediction model relying solely on historical by using relatively advanced methods,a few, such as GDPs, population resources and geographical locations were still neglected, leading to the limitations of our model.

<!-- b008076 | prose | pages [26] -->
10.3 Room for Improvement

<!-- b008077 | prose | pages [26] -->
• There are more details worth exploring such as the growth rate of performance. Extra information about economic development and population can be used to optimize the model for more practical use.

<!-- b008078 | heading | pages [26] -->
References

<!-- b008079 | references | pages [26] -->
[1] Z. Bo, Q. Chaoling, X. Xiaoli and Z. Fanbo, "GM (1,1) Model Gray Prediction for the

<!-- b008080 | references | pages [26] -->
Gold-Medal Result of Women’s Put Shot in the 30th Olympic Games," 2011 International

<!-- b008081 | references | pages [26] -->
Conference on Future Computer Science and Education, Xi’an, China, 2011.

<!-- b008082 | references | pages [26] -->
[2] J. Moolchandani, V. Chole, S. Sahu, R. Kumar, A. Shukla and A. Kumar, "Predictive An-

<!-- b008083 | references | pages [26] -->
alytics in Sports: Using Machine Learning to Forecast Outcomes and Medal Tally Trends

<!-- b008084 | references | pages [26] -->
at the 2024 Summer Olympics," 2024 4th International Conference on Technological

<!-- b008085 | references | pages [26] -->
Advancements in Computational Sciences (ICTACS), Tashkent, Uzbekistan, 2024.

<!-- b008086 | references | pages [26] -->
[3] N. T. M. Sagala and M. Amien Ibrahim, "A Comparative Study of Different Boosting

<!-- b008087 | references | pages [26] -->
Algorithms for Predicting Olympic Medal," 2022 IEEE 8th International Conference on

<!-- b008088 | references | pages [26] -->
Computing, Engineering and Design (ICCED), Sukabumi, Indonesia, 2022.

<!-- b008089 | references | pages [26] -->
[4] N. O. Abdelsalam, M. K. Elbashir and S. M. SaadEldeen, "Applying Cox Regression in

<!-- b008090 | references | pages [26] -->
Time to Event Data," 2018 International Conference on Computer, Control, Electrical,

<!-- b008091 | references | pages [26] -->
and Electronics Engineering (ICCCEEE), Khartoum, Sudan, 2018.

<!-- b008092 | references | pages [26] -->
[5] Z. Zhao, Y. Zhang, X. Zhu and J. Zuo, "Research on Time Series Anomaly Detection

<!-- b008093 | references | pages [26] -->
Algorithm and Application," 2019 IEEE 4th Advanced Information Technology, Electronic

<!-- b008094 | references | pages [26] -->
and Automation Control Conference (IAEAC), Chengdu, China, 2019.

<!-- b008095 | references | pages [26] -->
[6] Y. Qin and Y. Lou, "Hydrological Time Series Anomaly Pattern Detection based on

<!-- b008096 | references | pages [26] -->
Isolation Forest," 2019 IEEE 3rd Information Technology, Networking, Electronic and

<!-- b008097 | references | pages [26] -->
Automation Control Conference (ITNEC), Chengdu, China, 2019.

<!-- b008098 | references | pages [26] -->
[7] Poongadan, S., Lineesh, M.C. Non-linear Time Series Prediction using Improved CEEM-

<!-- b008099 | references | pages [26] -->
DAN, SVD and LSTM. Neural Process Lett 56, 164 (2024).

<!-- b008100 | references | pages [26] -->
[8] Kamal, Neel and Sanjay Pachauri. “Mann-Kendall Test - A Novel Approach for Statistical

<!-- b008101 | references | pages [26] -->
Trend Analysis.” International Journal of Computer Trends and Technology (2018): n.

<!-- b008102 | references | pages [26] -->
pag.

<!-- b008103 | references | pages [26] -->
关注数学模型

<!-- b008104 | furniture | pages [26] -->
2

<!-- b008105 | furniture | pages [26] -->
MATHmodels

<!-- b008106 | furniture | pages [26] -->
获取更多资讯

<!-- b008107 | furniture | pages [27] -->
Team # 2514461

<!-- b008108 | heading | pages [27] -->
Appendices

<!-- b008109 | prose | pages [27] -->
Country Gold Silver Bronze Total USA 47 45 36 128 CHN 35 24 15 74 GBR 16 21 21 58 FRA 13 16 14 43

<!-- b008110 | furniture | pages [27] -->
Page 1 of 25

<!-- b008111 | prose | pages [27] -->
Country Gold Silver Bronze Total COL 0 4 0 4 KAZ 0 1 3 4 RSA 1 2 1 4 TUR 0 1 3 4

<!-- b008112 | prose | pages [27] -->
微信公众号：数学模型

<!-- b008113 | prose | pages [27] -->
AUS 14 11 16 41 JPN 18 9 10 37 ITA 11 9 15 35 GER 11 11 12 34 NED 9 8 10 27 KOR 9 7 6 22 ROC 6 10 6 22 CAN 6 6 9 21 HUN 6 8 5 19 NZL 7 5 4 16

<!-- b008114 | prose | pages [27] -->
ECU 1 1 1 3 GDR 1 1 1 3 GRE 1 0 2 3 INA 1 0 2 3 IND 0 1 2 3 IRL 2 0 1 3 MEX 0 1 2 3 THA 1 1 1 3 ARM 0 2 0 2 AZE 0 1 1 2

<!-- b008115 | prose | pages [27] -->
微信号：MATHmodels

<!-- b008116 | prose | pages [27] -->
BRA 3 4 5 12 ESP 3 5 4 12 SWE 3 5 3 11 POL 2 4 4 10 SUI 2 3 5 10 CUB 4 2 3 9 UKR 1 4 4 9 DEN 2 3 3 8 KEN 3 2 3 8 ROU 2 4 1 7 BEL 2 1 3 6 CZE 3 1 2 6 IRI 2 3 1 6 TPE 2 1 3 6 UZB 4 1 1 6 BUL 2 1 2 5 CRO 2 2 1 5 GEO 2 3 0 5 JAM 2 1 2 5 NOR 3 1 1 5 SRB 2 1 2 5 URS 2 1 2 5 AUT 1 1 2 4

<!-- b008117 | prose | pages [27] -->
BLR 0 1 1 2 ETH 0 1 1 2 FIN 0 0 2 2 FRG 0 1 1 2 HKG 1 0 1 2 ISR 1 1 0 2 SLO 2 0 0 2 AIN 0 1 0 1 ARG 0 0 1 1 DOM 0 1 0 1 EGY 0 0 1 1 GRN 0 0 1 1 KGZ 0 1 0 1 MAS 0 0 1 1 MDA 0 0 1 1 MGL 0 1 0 1 PHI 1 0 0 1 POR 0 1 0 1 PRK 0 0 1 1 RUS 0 0 1 1 UGA 1 0 0 1 VEN 0 1 0 1 others 0 0 0 0

<!-- b008118 | caption | pages [27] -->
Table 7: All the countries that are predicted to earn medals in 2028 USA Olympic Games based

<!-- b008119 | prose | pages [27] -->
on XGBoost model (considering home country effect

<!-- b008120 | furniture | pages [29] -->
Team # 2514461

<!-- b008121 | furniture | pages [29] -->
Page 3 of 25

<!-- b008122 | prose | pages [29] -->
ability to improve prediction accuracy by combining weak learners (models that perform slightly better than random guessing) into a stronger, more robust model. Data and Features: The authors use historical Olympic data, such as athletes’ per- formance, country-specific features, and external factors like economic conditions and political stability, to train the models. They preprocess the data by handling missing values and normalizing features to enhance model performance.

<!-- b008123 | heading | pages [29] -->
Model Evaluation: The article assesses the performance of each boosting algorithm

<!-- b008124 | prose | pages [29] -->
using various evaluation metrics such as accuracy, precision, recall, and F1-score. The results show that XGBoost outperforms other algorithms in terms of prediction accuracy, likely due to its advanced regularization techniques and tree-based model optimizations. Key Findings: XGBoost was found to be the most effective algorithm for predicting

<!-- b008125 | prose | pages [29] -->
微信公众号：数学模型

<!-- b008126 | prose | pages [29] -->
Olympic medal outcomes, while AdaBoost showed slightly lower performance. The study emphasizes the importance of tuning hyperparameters and cross-validation for boosting models to avoid overfitting and improve generalizability. In conclusion, the article demonstrates the effectiveness of boosting algorithms, par- ticularly XGBoost, in predicting Olympic medal outcomes based on a combination of performance data and country-related features.

<!-- b008127 | prose | pages [29] -->
Query3: Is the Basis of Monte Carlo Simulation the Binomial Distribution?

<!-- b008128 | prose | pages [29] -->
Output: The basis of Monte Carlo simulation is not specifically the binomial distribution.

<!-- b008129 | prose | pages [29] -->
It is a statistical method that uses random sampling to simulate and compute the

<!-- b008130 | prose | pages [29] -->
微信号：MATHmodels

<!-- b008131 | prose | pages [29] -->
solutions to complex problems. Monte Carlo simulations can use various probability distributions, including the binomial distribution, but it is not limited to it. Basic Concept of Monte Carlo Simulation Monte Carlo simulation is a technique used to estimate the statistical properties of complex problems or systems by gen- erating a large number of random samples. The core idea of this method is to use a computer to generate random data and approximate solutions to real-world problems based on that data. Its foundation does not rely on any specific probability distribution but instead utilizes various distributions to simulate the behavior of systems. Binomial Distribution and Monte Carlo Simulation The binomial distribution can serve as one possible random distribution in Monte Carlo simulation, especially when simulating Bernoulli trials (e.g., events of success or failure). For example, if we needed to simulate multiple independent binomial trials (such as multiple coin tosses), we can use the binomial distribution to model the random variables. However, the strength of Monte Carlo simulation lies in its flexibility. It is not confined to a single distribution. Any suitable probability distribution can be chosen for the simulation, and common distributions include: Uniform Distribution: When each outcome has an equal probability.

<!-- b008132 | prose | pages [29] -->
Normal Distribution: When the variation of the variables follows a normal distribution

<!-- b008133 | heading | pages [29] -->
(e.g., stock price movements). Exponential Distribution: Used to model the time

<!-- b008134 | prose | pages [29] -->
intervals between events (e.g., the arrival time of phone calls).

<!-- b008135 | heading | pages [29] -->
Poisson Distribution: Used to model the number of events happening within a

<!-- b008136 | prose | pages [29] -->
fixed period (e.g., machine failures). Binomial Distribution: Used to model a fixed number of Bernoulli trials (e.g., the result of tossing a coin). Steps in Monte Carlo Simulation
