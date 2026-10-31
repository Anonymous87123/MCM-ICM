# P-C-2025-2503389-d13d77af

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
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

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | heading | pages [2] -->
Introduction

<!-- b000025 | prose | pages [2] -->
3 1

<!-- b000026 | heading | pages [2] -->
Background

<!-- b000027 | prose | pages [2] -->
1.1 3 1.2

<!-- b000028 | heading | pages [2] -->
Restatement of the Problem

<!-- b000029 | prose | pages [2] -->
3 Our work 1.3 4

<!-- b000030 | prose | pages [2] -->
2 Assumptions and Justification 5

<!-- b000031 | heading | pages [2] -->
Notations

<!-- b000032 | prose | pages [2] -->
3 Data Preprocessing 5 4 Data Cleaning and Adjustments 5 4.1 4.2 Data Exploration 5 Multiple Linear Regression-Feedforward Neural Network Bootstrap Ensemble 5 Interval Prediction Model with Host Effect 6

<!-- b000033 | heading | pages [2] -->
Reasons for Model Selection

<!-- b000034 | prose | pages [2] -->
5.1 6

<!-- b000035 | heading | pages [2] -->
Model Construction and Fusion

<!-- b000036 | prose | pages [2] -->
5.2 6 5.3

<!-- b000037 | heading | pages [2] -->
Forecast Results and Insights

<!-- b000038 | prose | pages [2] -->
9 Uncertainty and Evaluation Analysis 10 5.4

<!-- b000039 | heading | pages [2] -->
Logistic Regression and Random Forest Prediction Model for First-Time Medal-

<!-- b000040 | prose | pages [2] -->
6 11 ist Countries 6.1 11 Reasons for Model Selection Feature Engineering . 6.2 12 6.3 Analysis of Conditions for Countries Winning Medals for the First Time 12

<!-- b000041 | heading | pages [2] -->
Model Formulation and Prediction Results

<!-- b000042 | prose | pages [2] -->
6.4 13 6.5 Estimate odds 14

<!-- b000043 | heading | pages [2] -->
Strategic ImportanceAssessment Model for Olympic Sports (SIAMOS)

<!-- b000044 | prose | pages [2] -->
15 7 15

<!-- b000045 | heading | pages [2] -->
Model Development and Evaluation Framework

<!-- b000046 | prose | pages [2] -->
7.1

<!-- b000047 | heading | pages [2] -->
Result 1: Relationship Between Events and Medal Counts

<!-- b000048 | prose | pages [2] -->
16 7.2 Result 2: Sport-Specific Importance Across Nations. 16 7.3 7.4 Result 3: Impact of Host Nation's Event Selection on Medal Outcomes . 17 18 Contribution of the Great Coach 8 8.1 18 Definition of Great Coach . 8.2

<!-- b000049 | heading | pages [2] -->
Data Processing Framework

<!-- b000050 | prose | pages [2] -->
18 Calculation of Coefficients Based on Breakpoint Regression Model . 8.3 18 8.4 Case Study Analysis (Focusing on Three Key Sports) 19 The Practical Application of the "Great Coach" Effect 22 9 Selection of Sports Needing a Great Coach 22 9.1

<!-- b000051 | heading | pages [2] -->
Results

<!-- b000052 | prose | pages [2] -->
22 9.2

<!-- b000053 | heading | pages [2] -->
10 Other Insights: Host Country Spillover Effect on Medal Rates of Neighboring

<!-- b000054 | prose | pages [2] -->
_ 22 Countries

<!-- b000055 | heading | pages [2] -->
10.1 Analysis and Results

<!-- b000056 | prose | pages [2] -->
22

<!-- b000057 | heading | pages [2] -->
10.2 Strategic Recommendation for National Olympic Committees

<!-- b000058 | prose | pages [2] -->
23

<!-- b000059 | heading | pages [2] -->
11 Sensitivity Analysis

<!-- b000060 | prose | pages [2] -->
23

<!-- b000061 | heading | pages [2] -->
12 Strengths and Weaknesses

<!-- b000062 | prose | pages [2] -->
24

<!-- b000063 | heading | pages [2] -->
References

<!-- b000064 | references | pages [2] -->
25

<!-- b000065 | references | pages [2] -->
关注数学模型

<!-- b000066 | furniture | pages [2] -->
获取更多资讯

<!-- b000067 | furniture | pages [3] -->
Team # 2503389

<!-- b000068 | furniture | pages [3] -->
Page 3 of 26

<!-- b000069 | heading | pages [3] -->
1 Introduction

<!-- b000070 | heading | pages [3] -->
1.1 Background

<!-- b000071 | prose | pages [3] -->
The 2024 Paris Olympics concluded with notable highlights, including the United States leading the medal tally with 126 medals and sharing the top spot for gold medals with China at 微信公众号：数学模型 40 each.

<!-- b000072 | prose | pages [3] -->
As the world’s focus shifts toward the 2028 Los Angeles Olympics, the city’s vibrant energy and cultural diversity set the stage for the historic Games.

<!-- b000073 | prose | pages [3] -->
By analysing historical data and designing predictive modeling, we aim to forecast the 2028 Olympic medal standings. The host nation, the United States, potentially reinforcing its domi- nance. Simultaneously, countries that have yet to secure an Olympic medal will strive to achieve their first victories, marking historic milestones.

<!-- b000074 | prose | pages [3] -->
Additionally, the influence of great coaches and strategic investments may significantly shift 微信号：MATHmodels outcomes, offering valuable insights into medal prospects and performance optimization for countries worldwide.

<!-- b000075 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000076 | prose | pages [3] -->
Based on the analysis of the background, the key tasks are as follows:

<!-- b000077 | prose | pages [3] -->
Problem 1. Develop a predictive model for Olympic medal counts by country. The model should incorporate uncertainty estimates, evaluate prediction accuracy, and provide com- prehensive performance metrics.

<!-- b000078 | prose | pages [3] -->
Task 1.1 Use the model to forecast the medal table for the 2028 Los Angeles Summer Olympics.

<!-- b000079 | prose | pages [3] -->
Provide prediction intervals for all outcomes. Additionally, identify countries most likely to improve and those at risk of underperforming compared to their 2024 results.

<!-- b000080 | prose | pages [3] -->
Task 1.2 Identify nations that have yet to win an Olympic medal and forecast how many are likely to achieve their first medal in the upcoming Games. Estimate the probability of countries earning their first Olympic medal.

<!-- b000081 | prose | pages [3] -->
Task 1.3 Integrate event numbers and types into the model to analyze their relationship with medal counts by country. Identify influential sports for specific nations, their significance, and the impact of host nation event selection on results.

<!-- b000082 | prose | pages [3] -->
Problem 2. Coaches, unlike athletes, can freely move between countries, creating the potential for a significant “great coach” effect.

<!-- b000083 | prose | pages [3] -->
Task 2.1 Analyze data for evidence of changes that may be attributed to the influence of excep- tional coaches.Quantify the contribution of this “great coach” effect to medal counts.

<!-- b000084 | prose | pages [3] -->
Task 2.2 Select three countries and determine the sports in which they should invest in recruit- ing a “great coach.” Estimate the potential impact of such strategic coaching investments on medal performance.

<!-- b000085 | prose | pages [3] -->
Problem 3. Identify additional, original insights revealed by the model regarding Olympic medal counts. Provide actionable recommendations to country Olympic committees based on these findings.

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
m

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
Team # 2503389

<!-- b000397 | furniture | pages [4] -->
Page 4 of 26

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

<!-- b000642 | furniture | pages [4] -->
m

<!-- b000643 | furniture | pages [4] -->
m

<!-- b000644 | furniture | pages [4] -->
m

<!-- b000645 | furniture | pages [4] -->
m

<!-- b000646 | furniture | pages [4] -->
m

<!-- b000647 | furniture | pages [4] -->
m

<!-- b000648 | furniture | pages [4] -->
m

<!-- b000649 | furniture | pages [4] -->
m

<!-- b000650 | furniture | pages [4] -->
m

<!-- b000651 | furniture | pages [4] -->
m

<!-- b000652 | furniture | pages [4] -->
m

<!-- b000653 | furniture | pages [4] -->
m

<!-- b000654 | furniture | pages [4] -->
m

<!-- b000655 | furniture | pages [4] -->
m

<!-- b000656 | furniture | pages [4] -->
m

<!-- b000657 | furniture | pages [4] -->
m

<!-- b000658 | furniture | pages [4] -->
m

<!-- b000659 | furniture | pages [4] -->
m

<!-- b000660 | furniture | pages [4] -->
m

<!-- b000661 | furniture | pages [4] -->
m

<!-- b000662 | furniture | pages [4] -->
m

<!-- b000663 | furniture | pages [4] -->
m

<!-- b000664 | furniture | pages [4] -->
m

<!-- b000665 | furniture | pages [4] -->
m

<!-- b000666 | furniture | pages [4] -->
m

<!-- b000667 | furniture | pages [4] -->
m

<!-- b000668 | furniture | pages [4] -->
m

<!-- b000669 | furniture | pages [4] -->
m

<!-- b000670 | furniture | pages [4] -->
m

<!-- b000671 | furniture | pages [4] -->
m

<!-- b000672 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000673 | heading | pages [4] -->
1.3 Our work

<!-- b000674 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000675 | heading | pages [4] -->
2 Assumptions and Justification

<!-- b000676 | prose | pages [4] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified.

<!-- b000677 | prose | pages [4] -->
• The analysis and models are exclusively based on the provided datasets from the 2016, 2020, and 2024 Olympic Games. The three latest Olympic Games provide the most current and relevant data for insights into performance trends, ensuring the analysis is based on representative and applicable information.

<!-- b000678 | prose | pages [4] -->
• The performance of new entrants in their first Olympic participation is on par with that of athletes who will not compete in future Olympic Games. Olympic debuts and retirements are similar in that they both involve challenges such as inexperience or the end of a career, ensuring consistent participation by athletes.

<!-- b000679 | prose | pages [4] -->
• Russia and Belarus are excluded from the medal table in 2028. Athletes from Russia and Belarus competed without their national flags at the 2024 Olympics, indicating they will likely face the same restrictions in 2028.

<!-- b000680 | prose | pages [4] -->
• The disturbance terms in both the multiple regression and regression discontinuity models follow independent normal distributions. The errors are normally distributed with a mean of zero and constant variance, ensuring valid statistical tests and reliable model estimates.

<!-- b000681 | prose | pages [4] -->
• The assumption is made that the 2028 Olympic Games will proceed without signifi- cant global disruptions. “This assumption expects no major global disruptions, ensuring the 2028 Games proceed as planned and the analysis aligns with historical trends.”

<!-- b000682 | prose | pages [4, 5] -->
关注数学模型 • Medal counts are analyzed at the sports level, inferring event-level data. We aggre- gate the data from individual events within each sport to mitigate variability from fluctu- ations in the number of events.

<!-- b000683 | furniture | pages [4] -->
2

<!-- b000684 | furniture | pages [4] -->
MATHmodels

<!-- b000685 | furniture | pages [4] -->
获取更多资讯

<!-- b000686 | furniture | pages [5] -->
Team # 2503389

<!-- b000687 | furniture | pages [5] -->
Page 5 of 26

<!-- b000689 | heading | pages [5] -->
3 Notations

<!-- b000690 | heading | pages [5] -->
Symbols

<!-- b000691 | prose | pages [5] -->
Description Unit

<!-- b000692 | prose | pages [5] -->
Y1, Y2 Predicted medal count (total medals or gold medals) Medals 微信公众号：数学模型 XComp Competitiveness index Dimensionless Athlete pool Dimensionless XAth XHost Host boost indicator Binary Historical momentum Dimensionless XHist AWR Award-winning rate Percentage (%) β0, β1, β2, β3, β4 Regression coefficients - ˆPi Combined prediction for i-th instance Medals Weights for MLR and NN models - wMLR, wNN PE2 MLR, PE2 Mean squared prediction errors for MLR and NN - NN 微信号：MATHmodels where we define the main parameters while specific value of those parameters will be given later.

<!-- b000693 | heading | pages [5] -->
4 Data Preprocessing

<!-- b000694 | heading | pages [5] -->
4.1 Data Cleaning and Adjustments

<!-- b000695 | heading | pages [5] -->
4.1.1 Replacement Examples

<!-- b000696 | caption | pages [5] -->
Table 1: Standardized Olympic Data Adjustments Table

<!-- b000697 | prose | pages [5] -->
Category Original Name Standardized Name

<!-- b000698 | prose | pages [5] -->
Country Name Changes Great Britain United Kingdom Macedonia North Macedonia

<!-- b000699 | prose | pages [5] -->
Language Substitutions Cote d’Ivoire Ivory Coast Cape Verde Cabo Verde

<!-- b000700 | prose | pages [5] -->
Individual Olympic AthletesIOC2025 Synonym Replacements Independent Olympic Athletes Refugee AthletesIOC2025 Refugee Olympic Team

<!-- b000701 | prose | pages [5] -->
NOC Consistency ROC (Russia, 2020) Russia RUS (Russia, pre-2020) Russia

<!-- b000702 | prose | pages [5] -->
Sports Merging (2016) Cycling (as a single Sport) Split into Events Canoeing (as a single Sport) Split into Events

<!-- b000703 | heading | pages [5] -->
4.2 Data Exploration

<!-- b000704 | heading | pages [5] -->
4.2.1 Medal Flow Analysis Across Countries

<!-- b000705 | caption | pages [5] -->
Figure 1 presents a Sankey diagram highlighting key medal flow patterns during the 2024

<!-- b000706 | prose | pages [5] -->
Olympics:

<!-- b000707 | furniture | pages [6] -->
Team # 2503389

<!-- b000708 | furniture | pages [6] -->
Page 6 of 26

<!-- b000709 | prose | pages [6] -->
• Dominant Sports and Nations: Swimming and athletics contribute significantly to medal tallies in nations like the United States and China.

<!-- b000710 | prose | pages [6] -->
• Strategic Focus: Italy and Australia excel in niche sports, showcasing tailored investment strategies.

<!-- b000711 | prose | pages [6] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000712 | caption | pages [6] -->
Figure 1: Sankey Diagram Representing Medal Flow Across Countries and Sports (2024

<!-- b000713 | prose | pages [6] -->
Olympics)

<!-- b000714 | heading | pages [6] -->
5 Multiple Linear Regression-Feedforward Neural Network

<!-- b000715 | heading | pages [6] -->
Bootstrap Ensemble Interval Prediction Model with Host

<!-- b000716 | prose | pages [6] -->
Effect

<!-- b000717 | heading | pages [6] -->
5.1 Reasons for Model Selection

<!-- b000718 | prose | pages [6] -->
Predicting Olympic medal distributions is a complex regression task. The Multiple Lin- ear Regression (MLR) model is simple and interpretable, effective for linear relationships but limited in capturing non-linear dynamics like the host effect. To address this, the Feedforward

<!-- b000719 | heading | pages [6] -->
Neural Network (FNN) model excels in capturing non-linear patterns and handling diverse

<!-- b000720 | prose | pages [6] -->
datasets with high accuracy. Combining MLR’s simplicity with FNN’s adaptability, we pro- pose a hybrid approach for enhanced medal prediction.

<!-- b000721 | heading | pages [6] -->
5.2 Model Construction and Fusion

<!-- b000722 | heading | pages [6] -->
5.2.1 MLR-Model Construction

<!-- b000723 | prose | pages [6] -->
Multiple Linear Regression Formulation

<!-- b000724 | prose | pages [6] -->
The model is formulated as:

<!-- b000725 | prose | pages [6] -->
Yi = β0 + β1XComp + β2XAth + β3XHost + β4XHist + ϵ, (i = 1, 2)

<!-- b000726 | prose | pages [6] -->
Feature Selection

<!-- b000727 | prose | pages [6, 7] -->
关注数学模型 Feature Interpretation Mathematical Formula

<!-- b000728 | furniture | pages [6] -->
2

<!-- b000729 | furniture | pages [6] -->
MATHmodels

<!-- b000730 | furniture | pages [6] -->
获取更多资讯

<!-- b000731 | furniture | pages [7] -->
Team # 2503389

<!-- b000732 | furniture | pages [7] -->
Page 7 of 26

<!-- b000733 | caption | pages [7] -->
Table 2: Key Predictive Features and Their Mathematical Definitions

<!-- b000735 | prose | pages [7] -->
Host Boost Boost from hosting the (XHost) Olympics, quantified as { ( Rh −¯Rn ) if Host Nation 1 + ∆R, an additional medal im- ∆R = median XHost = , ¯Rn 0, Otherwise provement rate.

<!-- b000736 | prose | pages [7] -->
Rh: Host medal rate, ¯Rn: Non-host 微信公众号：数学模型 avg. rate.

<!-- b000737 | prose | pages [7] -->
Athlete Pool Reflects athlete partici- 2 X (XAth) pation trends, adjusted XAth = NT−t for Olympic debutants.

<!-- b000738 | prose | pages [7] -->
t=0 NT−t: Number of athletes in the (T −t)-th Olympic cycle.

<!-- b000739 | prose | pages [7] -->
Competitiveness Captures nation- ! Index (XComp) specific strength across K 3 X X mk 微信号：MATHmodels sports, adjusted for pk,t · e−0.2t · XComp = Mtotal temporal decay. t=1 k=1

<!-- b000740 | prose | pages [7] -->
mk: Medals in sport k, pk,t: Medals at T −t, Mtotal: Total medals.

<!-- b000741 | prose | pages [7] -->
Historical Mo- Weighted sum of past 3 X mentum (XHist) medals, with higher MT−t · e−0.2t XHist = weights for recent t=1 performances. MT−t: Total medals at T −t.

<!-- b000742 | prose | pages [7] -->
Correlation Analysis

<!-- b000743 | prose | pages [7] -->
To explore the relationships between features and target variables, we calculate Pearson corre- lation coefficients.

<!-- b000744 | caption | pages [7] -->
Figure 2: Correlation Matrix(XComp, XAth, and XHist)

<!-- b000745 | prose | pages [7, 8] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m As shown in Figure 2, the award-winning rate exhibits significant correlations with the pre- dictive features XComp, XAth, and XHist, with correlation coefficients of 0.92, 0.86, and 1.00, respectively. These values highlight the strong relationships between competitiveness, athlete pool size, and historical momentum in predicting a nation’s award-winning performance.

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

<!-- b000806 | furniture | pages [7] -->
m

<!-- b000807 | furniture | pages [7] -->
m

<!-- b000808 | furniture | pages [7] -->
m

<!-- b000809 | furniture | pages [7] -->
m

<!-- b000810 | furniture | pages [7] -->
m

<!-- b000811 | furniture | pages [7] -->
m

<!-- b000812 | furniture | pages [7] -->
m

<!-- b000813 | furniture | pages [7] -->
m

<!-- b000814 | furniture | pages [7] -->
m

<!-- b000815 | furniture | pages [7] -->
m

<!-- b000816 | furniture | pages [7] -->
m

<!-- b000817 | furniture | pages [7] -->
m

<!-- b000818 | furniture | pages [7] -->
m

<!-- b000819 | furniture | pages [7] -->
m

<!-- b000820 | furniture | pages [7] -->
m

<!-- b000821 | furniture | pages [7] -->
m

<!-- b000822 | furniture | pages [7] -->
m

<!-- b000823 | furniture | pages [7] -->
m

<!-- b000824 | furniture | pages [7] -->
m

<!-- b000825 | furniture | pages [7] -->
m

<!-- b000826 | furniture | pages [7] -->
m

<!-- b000827 | furniture | pages [7] -->
m

<!-- b000828 | furniture | pages [7] -->
m

<!-- b000829 | furniture | pages [7] -->
m

<!-- b000830 | furniture | pages [7] -->
m

<!-- b000831 | furniture | pages [7] -->
m

<!-- b000832 | furniture | pages [7] -->
m

<!-- b000833 | furniture | pages [7] -->
m

<!-- b000834 | furniture | pages [7] -->
m

<!-- b000835 | furniture | pages [7] -->
m

<!-- b000836 | furniture | pages [7] -->
m

<!-- b000837 | furniture | pages [7] -->
m

<!-- b000838 | furniture | pages [7] -->
m

<!-- b000839 | furniture | pages [7] -->
m

<!-- b000840 | furniture | pages [7] -->
m

<!-- b000841 | furniture | pages [7] -->
m

<!-- b000842 | furniture | pages [7] -->
m

<!-- b000843 | furniture | pages [7] -->
m

<!-- b000844 | furniture | pages [7] -->
m

<!-- b000845 | furniture | pages [7] -->
m

<!-- b000846 | furniture | pages [7] -->
m

<!-- b000847 | furniture | pages [7] -->
m

<!-- b000848 | furniture | pages [7] -->
m

<!-- b000849 | furniture | pages [7] -->
m

<!-- b000850 | furniture | pages [7] -->
m

<!-- b000851 | furniture | pages [7] -->
m

<!-- b000852 | furniture | pages [7] -->
m

<!-- b000853 | furniture | pages [7] -->
m

<!-- b000854 | furniture | pages [7] -->
m

<!-- b000855 | furniture | pages [7] -->
m

<!-- b000856 | furniture | pages [7] -->
m

<!-- b000857 | furniture | pages [7] -->
m

<!-- b000858 | furniture | pages [7] -->
m

<!-- b000859 | furniture | pages [7] -->
m

<!-- b000860 | furniture | pages [7] -->
m

<!-- b000861 | furniture | pages [7] -->
m

<!-- b000862 | furniture | pages [7] -->
m

<!-- b000863 | furniture | pages [7] -->
m

<!-- b000864 | furniture | pages [7] -->
m

<!-- b000865 | furniture | pages [7] -->
m

<!-- b000866 | furniture | pages [7] -->
m

<!-- b000867 | furniture | pages [7] -->
m

<!-- b000868 | furniture | pages [7] -->
m

<!-- b000869 | furniture | pages [7] -->
m

<!-- b000870 | furniture | pages [7] -->
m

<!-- b000871 | furniture | pages [7] -->
m

<!-- b000872 | furniture | pages [7] -->
m

<!-- b000873 | furniture | pages [7] -->
m

<!-- b000874 | furniture | pages [7] -->
m

<!-- b000875 | furniture | pages [7] -->
m

<!-- b000876 | furniture | pages [7] -->
m

<!-- b000877 | furniture | pages [7] -->
m

<!-- b000878 | furniture | pages [7] -->
m

<!-- b000879 | furniture | pages [7] -->
m

<!-- b000880 | furniture | pages [7] -->
m

<!-- b000881 | furniture | pages [7] -->
m

<!-- b000882 | furniture | pages [7] -->
m

<!-- b000883 | furniture | pages [7] -->
m

<!-- b000884 | furniture | pages [7] -->
m

<!-- b000885 | furniture | pages [7] -->
m

<!-- b000886 | furniture | pages [7] -->
m

<!-- b000887 | furniture | pages [7] -->
m

<!-- b000888 | furniture | pages [7] -->
m

<!-- b000889 | furniture | pages [7] -->
m

<!-- b000890 | furniture | pages [7] -->
m

<!-- b000891 | furniture | pages [7] -->
m

<!-- b000892 | furniture | pages [7] -->
m

<!-- b000893 | furniture | pages [7] -->
m

<!-- b000894 | furniture | pages [7] -->
m

<!-- b000895 | furniture | pages [7] -->
m

<!-- b000896 | furniture | pages [7] -->
m

<!-- b000897 | furniture | pages [7] -->
m

<!-- b000898 | furniture | pages [7] -->
m

<!-- b000899 | furniture | pages [7] -->
m

<!-- b000900 | furniture | pages [7] -->
m

<!-- b000901 | furniture | pages [7] -->
m

<!-- b000902 | furniture | pages [7] -->
m

<!-- b000903 | furniture | pages [7] -->
m

<!-- b000904 | furniture | pages [7] -->
m

<!-- b000905 | furniture | pages [7] -->
m

<!-- b000906 | furniture | pages [7] -->
m

<!-- b000907 | furniture | pages [7] -->
m

<!-- b000908 | furniture | pages [7] -->
m

<!-- b000909 | furniture | pages [7] -->
m

<!-- b000910 | furniture | pages [7] -->
m

<!-- b000911 | furniture | pages [7] -->
m

<!-- b000912 | furniture | pages [7] -->
m

<!-- b000913 | furniture | pages [7] -->
m

<!-- b000914 | furniture | pages [7] -->
m

<!-- b000915 | furniture | pages [7] -->
m

<!-- b000916 | furniture | pages [7] -->
m

<!-- b000917 | furniture | pages [7] -->
m

<!-- b000918 | furniture | pages [7] -->
m

<!-- b000919 | furniture | pages [7] -->
m

<!-- b000920 | furniture | pages [7] -->
m

<!-- b000921 | furniture | pages [7] -->
m

<!-- b000922 | furniture | pages [7] -->
m

<!-- b000923 | furniture | pages [7] -->
m

<!-- b000924 | furniture | pages [7] -->
m

<!-- b000925 | furniture | pages [7] -->
m

<!-- b000926 | furniture | pages [7] -->
m

<!-- b000927 | furniture | pages [7] -->
m

<!-- b000928 | furniture | pages [7] -->
m

<!-- b000929 | furniture | pages [7] -->
m

<!-- b000930 | furniture | pages [7] -->
m

<!-- b000931 | furniture | pages [7] -->
m

<!-- b000932 | furniture | pages [7] -->
m

<!-- b000933 | furniture | pages [7] -->
m

<!-- b000934 | furniture | pages [7] -->
m

<!-- b000935 | furniture | pages [7] -->
m

<!-- b000936 | furniture | pages [7] -->
m

<!-- b000937 | furniture | pages [7] -->
m

<!-- b000938 | furniture | pages [7] -->
m

<!-- b000939 | furniture | pages [7] -->
m

<!-- b000940 | furniture | pages [7] -->
m

<!-- b000941 | furniture | pages [7] -->
m

<!-- b000942 | furniture | pages [7] -->
m

<!-- b000943 | furniture | pages [7] -->
m

<!-- b000944 | furniture | pages [7] -->
m

<!-- b000945 | furniture | pages [7] -->
m

<!-- b000946 | furniture | pages [7] -->
m

<!-- b000947 | furniture | pages [7] -->
m

<!-- b000948 | furniture | pages [7] -->
m

<!-- b000949 | furniture | pages [7] -->
m

<!-- b000950 | furniture | pages [7] -->
m

<!-- b000951 | furniture | pages [7] -->
m

<!-- b000952 | furniture | pages [7] -->
m

<!-- b000953 | furniture | pages [7] -->
m

<!-- b000954 | furniture | pages [7] -->
m

<!-- b000955 | furniture | pages [7] -->
m

<!-- b000956 | furniture | pages [7] -->
m

<!-- b000957 | furniture | pages [7] -->
m

<!-- b000958 | furniture | pages [7] -->
m

<!-- b000959 | furniture | pages [7] -->
m

<!-- b000960 | furniture | pages [7] -->
m

<!-- b000961 | furniture | pages [7] -->
m

<!-- b000962 | furniture | pages [7] -->
m

<!-- b000963 | furniture | pages [7] -->
m

<!-- b000964 | furniture | pages [7] -->
m

<!-- b000965 | furniture | pages [7] -->
m

<!-- b000966 | furniture | pages [7] -->
m

<!-- b000967 | furniture | pages [7] -->
m

<!-- b000968 | furniture | pages [7] -->
m

<!-- b000969 | furniture | pages [7] -->
m

<!-- b000970 | furniture | pages [7] -->
m

<!-- b000971 | furniture | pages [7] -->
m

<!-- b000972 | furniture | pages [7] -->
m

<!-- b000973 | furniture | pages [7] -->
m

<!-- b000974 | furniture | pages [7] -->
m

<!-- b000975 | furniture | pages [7] -->
m

<!-- b000976 | furniture | pages [7] -->
m

<!-- b000977 | furniture | pages [7] -->
m

<!-- b000978 | furniture | pages [7] -->
m

<!-- b000979 | furniture | pages [7] -->
m

<!-- b000980 | furniture | pages [7] -->
m

<!-- b000981 | furniture | pages [7] -->
m

<!-- b000982 | furniture | pages [7] -->
m

<!-- b000983 | furniture | pages [7] -->
m

<!-- b000984 | furniture | pages [7] -->
m

<!-- b000985 | furniture | pages [7] -->
m

<!-- b000986 | furniture | pages [7] -->
m

<!-- b000987 | furniture | pages [7] -->
m

<!-- b000988 | furniture | pages [7] -->
m

<!-- b000989 | furniture | pages [7] -->
m

<!-- b000990 | furniture | pages [7] -->
m

<!-- b000991 | furniture | pages [7] -->
m

<!-- b000992 | furniture | pages [7] -->
m

<!-- b000993 | furniture | pages [7] -->
m

<!-- b000994 | furniture | pages [7] -->
m

<!-- b000995 | furniture | pages [7] -->
m

<!-- b000996 | furniture | pages [7] -->
m

<!-- b000997 | furniture | pages [7] -->
m

<!-- b000998 | furniture | pages [7] -->
m

<!-- b000999 | furniture | pages [7] -->
m

<!-- b001000 | furniture | pages [7] -->
m

<!-- b001001 | furniture | pages [7] -->
m

<!-- b001002 | furniture | pages [7] -->
m

<!-- b001003 | furniture | pages [7] -->
m

<!-- b001004 | furniture | pages [7] -->
m

<!-- b001005 | furniture | pages [7] -->
m

<!-- b001006 | furniture | pages [7] -->
m

<!-- b001007 | furniture | pages [7] -->
m

<!-- b001008 | furniture | pages [7] -->
m

<!-- b001009 | furniture | pages [7] -->
m

<!-- b001010 | furniture | pages [7] -->
m

<!-- b001011 | furniture | pages [7] -->
m

<!-- b001012 | furniture | pages [7] -->
m

<!-- b001013 | furniture | pages [7] -->
m

<!-- b001014 | furniture | pages [7] -->
m

<!-- b001015 | furniture | pages [7] -->
m

<!-- b001016 | furniture | pages [7] -->
m

<!-- b001017 | furniture | pages [7] -->
m

<!-- b001018 | furniture | pages [7] -->
m

<!-- b001019 | furniture | pages [7] -->
m

<!-- b001020 | furniture | pages [7] -->
m

<!-- b001021 | furniture | pages [7] -->
m

<!-- b001022 | furniture | pages [7] -->
m

<!-- b001023 | furniture | pages [7] -->
m

<!-- b001024 | furniture | pages [7] -->
m

<!-- b001025 | furniture | pages [7] -->
m

<!-- b001026 | furniture | pages [7] -->
m

<!-- b001027 | furniture | pages [7] -->
m

<!-- b001028 | furniture | pages [7] -->
m

<!-- b001029 | furniture | pages [7] -->
m

<!-- b001030 | furniture | pages [7] -->
m

<!-- b001031 | furniture | pages [7] -->
m

<!-- b001032 | furniture | pages [7] -->
m

<!-- b001033 | furniture | pages [7] -->
m

<!-- b001034 | furniture | pages [7] -->
m

<!-- b001035 | furniture | pages [7] -->
m

<!-- b001036 | furniture | pages [7] -->
m

<!-- b001037 | furniture | pages [7] -->
m

<!-- b001038 | furniture | pages [7] -->
m

<!-- b001039 | furniture | pages [7] -->
m

<!-- b001040 | furniture | pages [7] -->
m

<!-- b001041 | furniture | pages [7] -->
m

<!-- b001042 | furniture | pages [7] -->
m

<!-- b001043 | furniture | pages [7] -->
m

<!-- b001044 | furniture | pages [7] -->
m

<!-- b001045 | furniture | pages [7] -->
m

<!-- b001046 | furniture | pages [7] -->
m

<!-- b001047 | furniture | pages [7] -->
m

<!-- b001048 | furniture | pages [7] -->
m

<!-- b001049 | furniture | pages [7] -->
m

<!-- b001050 | furniture | pages [7] -->
m

<!-- b001051 | furniture | pages [7] -->
m

<!-- b001052 | furniture | pages [7] -->
m

<!-- b001053 | furniture | pages [7] -->
m

<!-- b001054 | furniture | pages [7] -->
m

<!-- b001055 | furniture | pages [7] -->
m

<!-- b001056 | furniture | pages [7] -->
m

<!-- b001057 | furniture | pages [7] -->
m

<!-- b001058 | furniture | pages [7] -->
m

<!-- b001059 | furniture | pages [7] -->
m

<!-- b001060 | furniture | pages [7] -->
m

<!-- b001061 | furniture | pages [7] -->
m

<!-- b001062 | furniture | pages [7] -->
m

<!-- b001063 | furniture | pages [7] -->
m

<!-- b001064 | furniture | pages [7] -->
m

<!-- b001065 | furniture | pages [7] -->
m

<!-- b001066 | furniture | pages [7] -->
m

<!-- b001067 | furniture | pages [7] -->
m

<!-- b001068 | furniture | pages [7] -->
m

<!-- b001069 | furniture | pages [7] -->
m

<!-- b001070 | furniture | pages [8] -->
Team # 2503389

<!-- b001071 | furniture | pages [8] -->
Page 8 of 26

<!-- b001073 | caption | pages [8] -->
Figure 3: Host Boost

<!-- b001074 | prose | pages [8] -->
Since the host boost is a discrete variable, while other features change continuously, the host boost shows weak linear correlation with the other three indicators. Therefore, it is necessary to analyze the host boost separately. As illustrated in Figure 3, the total medal count for a nation significantly increases during its host year, highlighting the “Host Boost” as a crucial feature.

<!-- b001075 | heading | pages [8] -->
5.2.2 Feedforward Neural Network-Model Construction

<!-- b001076 | prose | pages [8] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001077 | caption | pages [8] -->
Figure 4: Feedforward Neural Network-Model Construction

<!-- b001078 | prose | pages [8] -->
From Figure 4, the model follows a typical Feedforward Neural Network (FNN) structure, which includes an input layer, two hidden layers with ReLU activation functions, and an output layer with a linear activation function. The raw dataset is split into training and test sets, with the training set further divided into training data and validation data (20% of the training set). The model is trained using the Adam optimizer with a learning rate of 0.01. Validation loss is tracked during the training process to assess the model’s performance.

<!-- b001079 | heading | pages [8] -->
5.2.3 Weighted Fusion of Predictions

<!-- b001080 | caption | pages [8] -->
Figure 5: Weighted Fusion Construction

<!-- b001081 | prose | pages [8, 9] -->
关注数学模型 To enhance the accuracy and robustness of medal count predictions, we utilize a weighted fusion approach to combine the outputs of the Multiple Linear Regression (MLR) and Feedforward Neural Network (FNN) models.

<!-- b001082 | furniture | pages [8] -->
2

<!-- b001083 | furniture | pages [8] -->
MATHmodels

<!-- b001084 | furniture | pages [8] -->
获取更多资讯

<!-- b001085 | furniture | pages [9] -->
Team # 2503389

<!-- b001086 | furniture | pages [9] -->
Page 9 of 26

<!-- b001088 | prose | pages [9] -->
First, the mean squared prediction errors (MSE) for the two models are calculated:

<!-- b001089 | prose | pages [9] -->
N N X X MLR = 1 NN = 1 (Ri −PMLR,i)2 , (Ri −PNN,i)2 PE2 PE2 微信公众号：数学模型 N N i=1 i=1

<!-- b001090 | prose | pages [9] -->
The weights for each model are derived based on their relative errors:

<!-- b001091 | prose | pages [9] -->
PE2 PE2 NN MLR ≈0.6, ≈0.4 wMLR = wNN = PE2 MLR + PE2 PE2 MLR + PE2 NN NN

<!-- b001092 | prose | pages [9] -->
Finally, the combined prediction for observation i is calculated as:

<!-- b001093 | prose | pages [9] -->
ˆPi = wMLR · PMLR,i + wNN · PNN,i 微信号：MATHmodels Through analyzing prediction errors, it is clear that the MLP model suffers from higher errors, while the FNN model risks overfitting. The combined MLP-NN model addresses these issues, enhancing both accuracy and robustness for reliable predictions.

<!-- b001094 | heading | pages [9] -->
5.3 Forecast Results and Insights

<!-- b001095 | prose | pages [9] -->
Total Medals Gold Medals Confidence Intervals (95%) NOC Pred. Δ Rank Δ Pred. Δ Rank Δ Total Lower Total Upper Gold Lower Gold Upper United States 143 ↑17 1 – 59 ↑19 1 – 110 192 50 68 China 76 ↓15 2 – 32 ↓8 2 ↓1 61 94 27 37 United Kingdom 62 ↓3 3 – 21 ↑7 3 ↑4 56 85 17 25 France 60 ↓4 4 – 16 – 5 – 50 73 13 19 Australia 54 ↑1 5 – 21 ↑3 3 ↑1 49 70 17 25 Japan 43 ↓2 6 – 16 ↓4 5 ↓2 35 51 13 19 Italy 40 – 7 – 12 – 8 ↑1 34 48 10 14 Germany 36 ↑3 8 ↑1 12 – 8 ↑2 31 44 10 14 Netherlands 35 ↑1 9 ↓1 15 – 7 ↓1 31 43 12 18 Canada 30 ↑3 10 ↑1 10 ↑1 10 ↑2 27 37 8 12

<!-- b001096 | caption | pages [9] -->
Table 3: 2024 Olympic Medal Predictions with Rankings, Changes, and Confidence Intervals

<!-- b001097 | prose | pages [9] -->
Countries Likely to Improve: America (+17 medals) and Canada (+3 medals) show up- ward trends, may due to increased investment in athlete development and enhanced coaching strategies.

<!-- b001098 | prose | pages [9] -->
Countries Likely to Decline: France (60 medals vs. 64 in 2024) may experience a decline after hosting, while China (76 medals vs. 91 in 2024) faces challenges as its strong event, weightlifting1, will no longer be held.

<!-- b001099 | prose | pages [9] -->
Key Uncertainty: The U.S. medal interval highlights variability in team sports, while smaller nations like Slovenia (1 gold, CI: 0–2) exhibit greater volatility due to dependence on individual athletes.

<!-- b001100 | prose | pages [9, 10] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Australia Australia Canada Canada China Log-Scaled Share▼ China Frence Medals France 141 (Max) Germany Germany Great Britain Great Britain Naiion Country Italy Itally 57 Japan Japan 39 Netherlands Netherlands Russia Russia 0 (Min) Russla (ROC) Russia (ROC) 0% South Koret South Korea United States United States Tokyo 2020 Rio 2016 Paris 2024 LA 2028 2016 2020 2024 2028 Olympic Year Olympic Year

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

<!-- b001162 | furniture | pages [9] -->
m

<!-- b001163 | furniture | pages [9] -->
m

<!-- b001164 | furniture | pages [9] -->
m

<!-- b001165 | furniture | pages [9] -->
m

<!-- b001166 | furniture | pages [9] -->
m

<!-- b001167 | furniture | pages [9] -->
m

<!-- b001168 | furniture | pages [9] -->
m

<!-- b001169 | furniture | pages [9] -->
m

<!-- b001170 | furniture | pages [9] -->
m

<!-- b001171 | furniture | pages [9] -->
m

<!-- b001172 | furniture | pages [9] -->
m

<!-- b001173 | furniture | pages [9] -->
m

<!-- b001174 | furniture | pages [9] -->
m

<!-- b001175 | furniture | pages [9] -->
m

<!-- b001176 | furniture | pages [9] -->
m

<!-- b001177 | furniture | pages [9] -->
m

<!-- b001178 | furniture | pages [9] -->
m

<!-- b001179 | furniture | pages [9] -->
m

<!-- b001180 | furniture | pages [9] -->
m

<!-- b001181 | furniture | pages [9] -->
m

<!-- b001182 | furniture | pages [9] -->
m

<!-- b001183 | furniture | pages [9] -->
m

<!-- b001184 | furniture | pages [9] -->
m

<!-- b001185 | furniture | pages [9] -->
m

<!-- b001186 | furniture | pages [9] -->
m

<!-- b001187 | furniture | pages [9] -->
m

<!-- b001188 | furniture | pages [9] -->
m

<!-- b001189 | furniture | pages [9] -->
m

<!-- b001190 | furniture | pages [9] -->
m

<!-- b001191 | furniture | pages [9] -->
m

<!-- b001192 | furniture | pages [9] -->
m

<!-- b001193 | furniture | pages [9] -->
m

<!-- b001194 | furniture | pages [9] -->
m

<!-- b001195 | furniture | pages [9] -->
m

<!-- b001196 | furniture | pages [9] -->
m

<!-- b001197 | furniture | pages [9] -->
m

<!-- b001198 | furniture | pages [9] -->
m

<!-- b001199 | furniture | pages [9] -->
m

<!-- b001200 | furniture | pages [9] -->
m

<!-- b001201 | furniture | pages [9] -->
m

<!-- b001202 | furniture | pages [9] -->
m

<!-- b001203 | furniture | pages [9] -->
m

<!-- b001204 | furniture | pages [9] -->
m

<!-- b001205 | furniture | pages [9] -->
m

<!-- b001206 | furniture | pages [9] -->
m

<!-- b001207 | furniture | pages [9] -->
m

<!-- b001208 | furniture | pages [9] -->
m

<!-- b001209 | furniture | pages [9] -->
m

<!-- b001210 | furniture | pages [9] -->
m

<!-- b001211 | furniture | pages [9] -->
m

<!-- b001212 | furniture | pages [9] -->
m

<!-- b001213 | furniture | pages [9] -->
m

<!-- b001214 | furniture | pages [9] -->
m

<!-- b001215 | furniture | pages [9] -->
m

<!-- b001216 | furniture | pages [9] -->
m

<!-- b001217 | furniture | pages [9] -->
m

<!-- b001218 | furniture | pages [9] -->
m

<!-- b001219 | furniture | pages [9] -->
m

<!-- b001220 | furniture | pages [9] -->
m

<!-- b001221 | furniture | pages [9] -->
m

<!-- b001222 | furniture | pages [9] -->
m

<!-- b001223 | furniture | pages [9] -->
m

<!-- b001224 | furniture | pages [9] -->
m

<!-- b001225 | furniture | pages [9] -->
m

<!-- b001226 | furniture | pages [9] -->
m

<!-- b001227 | furniture | pages [9] -->
m

<!-- b001228 | furniture | pages [9] -->
m

<!-- b001229 | furniture | pages [9] -->
m

<!-- b001230 | furniture | pages [9] -->
m

<!-- b001231 | furniture | pages [9] -->
m

<!-- b001232 | furniture | pages [9] -->
m

<!-- b001233 | furniture | pages [9] -->
m

<!-- b001234 | furniture | pages [9] -->
m

<!-- b001235 | furniture | pages [9] -->
m

<!-- b001236 | furniture | pages [9] -->
m

<!-- b001237 | furniture | pages [9] -->
m

<!-- b001238 | furniture | pages [9] -->
m

<!-- b001239 | furniture | pages [9] -->
m

<!-- b001240 | furniture | pages [9] -->
m

<!-- b001241 | furniture | pages [9] -->
m

<!-- b001242 | furniture | pages [9] -->
m

<!-- b001243 | furniture | pages [9] -->
m

<!-- b001244 | furniture | pages [9] -->
m

<!-- b001245 | furniture | pages [9] -->
m

<!-- b001246 | furniture | pages [9] -->
m

<!-- b001247 | furniture | pages [9] -->
m

<!-- b001248 | furniture | pages [9] -->
m

<!-- b001249 | furniture | pages [9] -->
m

<!-- b001250 | furniture | pages [9] -->
m

<!-- b001251 | furniture | pages [9] -->
m

<!-- b001252 | furniture | pages [9] -->
m

<!-- b001253 | furniture | pages [9] -->
m

<!-- b001254 | furniture | pages [9] -->
m

<!-- b001255 | furniture | pages [9] -->
m

<!-- b001256 | furniture | pages [9] -->
m

<!-- b001257 | furniture | pages [9] -->
m

<!-- b001258 | furniture | pages [9] -->
m

<!-- b001259 | furniture | pages [9] -->
m

<!-- b001260 | furniture | pages [9] -->
m

<!-- b001261 | furniture | pages [9] -->
m

<!-- b001262 | furniture | pages [9] -->
m

<!-- b001263 | furniture | pages [9] -->
m

<!-- b001264 | furniture | pages [9] -->
m

<!-- b001265 | furniture | pages [9] -->
m

<!-- b001266 | furniture | pages [9] -->
m

<!-- b001267 | furniture | pages [9] -->
m

<!-- b001268 | furniture | pages [9] -->
m

<!-- b001269 | furniture | pages [9] -->
m

<!-- b001270 | furniture | pages [9] -->
m

<!-- b001271 | furniture | pages [9] -->
m

<!-- b001272 | furniture | pages [9] -->
m

<!-- b001273 | furniture | pages [9] -->
m

<!-- b001274 | furniture | pages [9] -->
m

<!-- b001275 | furniture | pages [9] -->
m

<!-- b001276 | furniture | pages [9] -->
m

<!-- b001277 | furniture | pages [9] -->
m

<!-- b001278 | furniture | pages [9] -->
m

<!-- b001279 | furniture | pages [9] -->
m

<!-- b001280 | furniture | pages [9] -->
m

<!-- b001281 | furniture | pages [9] -->
m

<!-- b001282 | furniture | pages [9] -->
m

<!-- b001283 | furniture | pages [9] -->
m

<!-- b001284 | furniture | pages [9] -->
m

<!-- b001285 | furniture | pages [9] -->
m

<!-- b001286 | furniture | pages [9] -->
m

<!-- b001287 | furniture | pages [9] -->
m

<!-- b001288 | furniture | pages [9] -->
m

<!-- b001289 | furniture | pages [9] -->
m

<!-- b001290 | furniture | pages [9] -->
m

<!-- b001291 | furniture | pages [9] -->
m

<!-- b001292 | furniture | pages [9] -->
m

<!-- b001293 | furniture | pages [9] -->
m

<!-- b001294 | furniture | pages [9] -->
m

<!-- b001295 | furniture | pages [9] -->
m

<!-- b001296 | furniture | pages [9] -->
m

<!-- b001297 | furniture | pages [9] -->
m

<!-- b001298 | furniture | pages [9] -->
m

<!-- b001299 | furniture | pages [9] -->
m

<!-- b001300 | furniture | pages [9] -->
m

<!-- b001301 | furniture | pages [9] -->
m

<!-- b001302 | furniture | pages [9] -->
m

<!-- b001303 | furniture | pages [9] -->
m

<!-- b001304 | furniture | pages [9] -->
m

<!-- b001305 | furniture | pages [9] -->
m

<!-- b001306 | furniture | pages [9] -->
m

<!-- b001307 | furniture | pages [9] -->
m

<!-- b001308 | furniture | pages [9] -->
m

<!-- b001309 | furniture | pages [9] -->
m

<!-- b001310 | furniture | pages [9] -->
m

<!-- b001311 | furniture | pages [9] -->
m

<!-- b001312 | furniture | pages [9] -->
m

<!-- b001313 | furniture | pages [9] -->
m

<!-- b001314 | furniture | pages [9] -->
m

<!-- b001315 | furniture | pages [9] -->
m

<!-- b001316 | furniture | pages [9] -->
m

<!-- b001317 | furniture | pages [9] -->
m

<!-- b001318 | furniture | pages [9] -->
m

<!-- b001319 | furniture | pages [9] -->
m

<!-- b001320 | furniture | pages [9] -->
m

<!-- b001321 | furniture | pages [9] -->
m

<!-- b001322 | furniture | pages [9] -->
m

<!-- b001323 | furniture | pages [9] -->
m

<!-- b001324 | furniture | pages [9] -->
m

<!-- b001325 | furniture | pages [9] -->
m

<!-- b001326 | furniture | pages [9] -->
m

<!-- b001327 | furniture | pages [9] -->
m

<!-- b001328 | furniture | pages [9] -->
m

<!-- b001329 | furniture | pages [9] -->
m

<!-- b001330 | furniture | pages [9] -->
m

<!-- b001331 | furniture | pages [9] -->
m

<!-- b001332 | furniture | pages [9] -->
m

<!-- b001333 | furniture | pages [9] -->
m

<!-- b001334 | furniture | pages [9] -->
m

<!-- b001335 | furniture | pages [9] -->
m

<!-- b001336 | furniture | pages [9] -->
m

<!-- b001337 | furniture | pages [9] -->
m

<!-- b001338 | furniture | pages [9] -->
m

<!-- b001339 | furniture | pages [9] -->
m

<!-- b001340 | furniture | pages [9] -->
m

<!-- b001341 | furniture | pages [9] -->
m

<!-- b001342 | furniture | pages [9] -->
m

<!-- b001343 | furniture | pages [9] -->
m

<!-- b001344 | furniture | pages [9] -->
m

<!-- b001345 | furniture | pages [9] -->
m

<!-- b001346 | furniture | pages [9] -->
m

<!-- b001347 | furniture | pages [9] -->
m

<!-- b001348 | furniture | pages [9] -->
m

<!-- b001349 | furniture | pages [9] -->
m

<!-- b001350 | furniture | pages [9] -->
m

<!-- b001351 | furniture | pages [9] -->
m

<!-- b001352 | furniture | pages [9] -->
m

<!-- b001353 | furniture | pages [9] -->
m

<!-- b001354 | furniture | pages [9] -->
m

<!-- b001355 | furniture | pages [9] -->
m

<!-- b001356 | furniture | pages [9] -->
m

<!-- b001357 | furniture | pages [9] -->
m

<!-- b001358 | furniture | pages [9] -->
m

<!-- b001359 | furniture | pages [9] -->
m

<!-- b001360 | furniture | pages [9] -->
m

<!-- b001361 | furniture | pages [9] -->
m

<!-- b001362 | furniture | pages [9] -->
m

<!-- b001363 | furniture | pages [9] -->
m

<!-- b001364 | furniture | pages [9] -->
m

<!-- b001365 | furniture | pages [9] -->
m

<!-- b001366 | furniture | pages [9] -->
m

<!-- b001367 | furniture | pages [9] -->
m

<!-- b001368 | furniture | pages [9] -->
m

<!-- b001369 | furniture | pages [9] -->
m

<!-- b001370 | furniture | pages [9] -->
m

<!-- b001371 | furniture | pages [9] -->
m

<!-- b001372 | furniture | pages [9] -->
m

<!-- b001373 | furniture | pages [9] -->
m

<!-- b001374 | furniture | pages [9] -->
m

<!-- b001375 | furniture | pages [9] -->
m

<!-- b001376 | furniture | pages [9] -->
m

<!-- b001377 | furniture | pages [9] -->
m

<!-- b001378 | furniture | pages [9] -->
m

<!-- b001379 | furniture | pages [9] -->
m

<!-- b001380 | furniture | pages [9] -->
m

<!-- b001381 | furniture | pages [9] -->
m

<!-- b001382 | furniture | pages [9] -->
m

<!-- b001383 | furniture | pages [9] -->
m

<!-- b001384 | furniture | pages [9] -->
m

<!-- b001385 | furniture | pages [9] -->
m

<!-- b001386 | furniture | pages [9] -->
m

<!-- b001387 | furniture | pages [9] -->
m

<!-- b001388 | furniture | pages [9] -->
m

<!-- b001389 | furniture | pages [9] -->
m

<!-- b001390 | furniture | pages [9] -->
m

<!-- b001391 | furniture | pages [9] -->
m

<!-- b001392 | furniture | pages [9] -->
m

<!-- b001393 | furniture | pages [9] -->
m

<!-- b001394 | furniture | pages [9] -->
m

<!-- b001395 | furniture | pages [9] -->
m

<!-- b001396 | furniture | pages [9] -->
m

<!-- b001397 | furniture | pages [9] -->
m

<!-- b001398 | furniture | pages [9] -->
m

<!-- b001399 | furniture | pages [9] -->
m

<!-- b001400 | furniture | pages [9] -->
m

<!-- b001401 | furniture | pages [9] -->
m

<!-- b001402 | furniture | pages [9] -->
m

<!-- b001403 | furniture | pages [9] -->
m

<!-- b001404 | furniture | pages [9] -->
m

<!-- b001405 | furniture | pages [9] -->
m

<!-- b001406 | furniture | pages [9] -->
m

<!-- b001407 | furniture | pages [9] -->
m

<!-- b001408 | furniture | pages [9] -->
m

<!-- b001409 | furniture | pages [9] -->
m

<!-- b001410 | furniture | pages [9] -->
m

<!-- b001411 | furniture | pages [9] -->
m

<!-- b001412 | furniture | pages [9] -->
m

<!-- b001413 | furniture | pages [9] -->
m

<!-- b001414 | furniture | pages [9] -->
m

<!-- b001415 | furniture | pages [9] -->
m

<!-- b001416 | furniture | pages [9] -->
m

<!-- b001417 | furniture | pages [9] -->
m

<!-- b001418 | furniture | pages [9] -->
m

<!-- b001419 | furniture | pages [9] -->
m

<!-- b001420 | furniture | pages [9] -->
m

<!-- b001421 | furniture | pages [9] -->
m

<!-- b001422 | furniture | pages [9] -->
m

<!-- b001423 | furniture | pages [9] -->
m

<!-- b001424 | furniture | pages [9] -->
m

<!-- b001425 | furniture | pages [10] -->
Team# 2503389

<!-- b001426 | furniture | pages [10] -->
Page 10 of 26

<!-- b001428 | prose | pages [10] -->
(a) Medal Proportion (Logarithmic) (b) Medal Counts (Absolute)

<!-- b001429 | caption | pages [10] -->
Figure 6: Comparative Visualization of Olympic Medal Performance

<!-- b001430 | prose | pages [10] -->
As shown in Figure 6, the heatmap depicts the progression of the top 10 nations' medal counts from 2016 to 2028 using our prediction results . Color intensity indicates medal totals, with deeper blue shades signifying higher counts.

<!-- b001431 | prose | pages [10] -->
Key trends include the United States and China consistently dominating medal counts, re- flecting their robust athletic programs. Host nations tend to achieve significant medal boosts. Emerging nations like Japan and the Netherlands display upward trends, signaling strategic investments. In contrast, nations such as Italy, Russia, and South Korea show variable per- formances. Western countries like Great Britain, Italy, and Germany maintain stable medal tallies.

<!-- b001432 | heading | pages [10] -->
5.4 Uncertainty and Evaluation Analysis

<!-- b001433 | heading | pages [10] -->
5.4.1 Uncertainty Analysis with Bootstrap

<!-- b001434 | prose | pages [10] -->
A Bootstrap method (500 iterations) was used to quantify the uncertainty of medal predictions for both total medals and gold medals. The process includes: The final 95% prediction intervals were derived from the aggregated results:

<!-- b001435 | prose | pages [10] -->
Lower Bound = Percentile(2.5), Upper Bound = Percentile(97.5)

<!-- b001436 | prose | pages [10] -->
For example, the U.S. total medal interval [116, 193] reflects high uncertainty due to variable team sports performance, while China's narrower gold interval [27, 37] (from 32 predicted) indicates more stable strengths in diving and table tennis.

<!-- b001437 | heading | pages [10] -->
5.4.2 Prediction evaluation analysis

<!-- b001438 | heading | pages [10] -->
From Table 4, the selected model variables demonstrate both significance and explanatory

<!-- b001439 | prose | pages [10] -->
power:

<!-- b001440 | prose | pages [10] -->
• Host Boost (XHost): A coefficient of 13.10 (p < 0.001) indicates a strong positive impact of hosting the Olympics on medal counts, despite a high standard error (2.88) due to cross-country variability.

<!-- b001441 | prose | pages [10, 11] -->
关注数学模型 Variable Coeﬀicient Standard Error t-Statistic P-Value(P>|t|)

<!-- b001442 | furniture | pages [10] -->
获取更多资讯

<!-- b001443 | furniture | pages [11] -->
Team # 2503389

<!-- b001444 | furniture | pages [11] -->
Page 11 of 26

<!-- b001445 | caption | pages [11] -->
Table 4: Regression Coefficients for the Multivariate Linear Model

<!-- b001447 | prose | pages [11] -->
Host Boost (XHost) 13.10 2.88 4.55 <0.001 Athlete Pool (XAth) 0.004 0.003 1.33 0.188 微信公众号：数学模型 Competitiveness Index (XComp) 2.18 0.71 3.06 0.003 Historical Momentum (XHist) 0.59 0.09 6.42 <0.001

<!-- b001448 | prose | pages [11] -->
• Competitiveness Index (XComp) and Historical Momentum (XHist): Both have signifi- cant positive effects, with coefficients of 2.18 and 0.59 (p < 0.01). Historical Momentum has the highest t-value (6.42) and the lowest standard error (0.09), highlighting its strong influence on medal performance.

<!-- b001449 | prose | pages [11] -->
• Athlete Pool (XAth): The coefficient (0.004) is not statistically significant (p = 0.188), suggesting that athlete pool size alone does not fully explain medal outcomes.

<!-- b001450 | prose | pages [11] -->
微信号：MATHmodels Overall, the model effectively captures the primary drivers of medal distribution, with sig- nificant contributions from host status, competitiveness, and historical momentum.

<!-- b001451 | caption | pages [11] -->
Table 5: Key Metrics and Results of Regression Analysis

<!-- b001452 | prose | pages [11] -->
Metric Formula

<!-- b001453 | heading | pages [11] -->
Result

<!-- b001454 | prose | pages [11] -->
Mean Squared Error 7.115 N X (MSE) MSE = 1 (yi −ˆyi)2 N i=1

<!-- b001455 | prose | pages [11] -->
Root Mean Squared Er- 2.667 v u ror (RMSE) u N X t 1 (yi −ˆyi)2 RMSE = N i=1

<!-- b001456 | prose | pages [11] -->
Mean Absolute Per- 51.099% N X yi −ˆyi centage Error (MAPE) MAPE = 100 N yi i=1

<!-- b001457 | prose | pages [11] -->
The metrics in Table 5 indicate that the model controls absolute errors well, with an RMSE of 2.667 (average deviation of 2.7 medals). However, the high MAPE of 51.1% reveals challenges in accurately predicting countries with low medal counts, suggesting room for improvement.

<!-- b001458 | heading | pages [11] -->
6 Logistic Regression and Random Forest Prediction Model

<!-- b001459 | prose | pages [11] -->
for First-Time Medalist Countries

<!-- b001460 | heading | pages [11] -->
6.1 Reasons for Model Selection

<!-- b001461 | prose | pages [11, 12] -->
Predicting the probability of countries winning their first Olympic medal is a complicated classification task. Logistic regression (LR) is a widely used model that excels in simplicity and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m interpretability, effectively estimating probabilities when the relationships between predictors and outcomes are linear. However, it struggles with non-linear patterns and complex feature interactions that are often present in Olympic data, such as historical variability or regional effects.

<!-- b001462 | furniture | pages [11] -->
m

<!-- b001463 | furniture | pages [11] -->
m

<!-- b001464 | furniture | pages [11] -->
m

<!-- b001465 | furniture | pages [11] -->
m

<!-- b001466 | furniture | pages [11] -->
m

<!-- b001467 | furniture | pages [11] -->
m

<!-- b001468 | furniture | pages [11] -->
m

<!-- b001469 | furniture | pages [11] -->
m

<!-- b001470 | furniture | pages [11] -->
m

<!-- b001471 | furniture | pages [11] -->
m

<!-- b001472 | furniture | pages [11] -->
m

<!-- b001473 | furniture | pages [11] -->
m

<!-- b001474 | furniture | pages [11] -->
m

<!-- b001475 | furniture | pages [11] -->
m

<!-- b001476 | furniture | pages [11] -->
m

<!-- b001477 | furniture | pages [11] -->
m

<!-- b001478 | furniture | pages [11] -->
m

<!-- b001479 | furniture | pages [11] -->
m

<!-- b001480 | furniture | pages [11] -->
m

<!-- b001481 | furniture | pages [11] -->
m

<!-- b001482 | furniture | pages [11] -->
m

<!-- b001483 | furniture | pages [11] -->
m

<!-- b001484 | furniture | pages [11] -->
m

<!-- b001485 | furniture | pages [11] -->
m

<!-- b001486 | furniture | pages [11] -->
m

<!-- b001487 | furniture | pages [11] -->
m

<!-- b001488 | furniture | pages [11] -->
m

<!-- b001489 | furniture | pages [11] -->
m

<!-- b001490 | furniture | pages [11] -->
m

<!-- b001491 | furniture | pages [11] -->
m

<!-- b001492 | furniture | pages [11] -->
m

<!-- b001493 | furniture | pages [11] -->
m

<!-- b001494 | furniture | pages [11] -->
m

<!-- b001495 | furniture | pages [11] -->
m

<!-- b001496 | furniture | pages [11] -->
m

<!-- b001497 | furniture | pages [11] -->
m

<!-- b001498 | furniture | pages [11] -->
m

<!-- b001499 | furniture | pages [11] -->
m

<!-- b001500 | furniture | pages [11] -->
m

<!-- b001501 | furniture | pages [11] -->
m

<!-- b001502 | furniture | pages [11] -->
m

<!-- b001503 | furniture | pages [11] -->
m

<!-- b001504 | furniture | pages [11] -->
m

<!-- b001505 | furniture | pages [11] -->
m

<!-- b001506 | furniture | pages [11] -->
m

<!-- b001507 | furniture | pages [11] -->
m

<!-- b001508 | furniture | pages [11] -->
m

<!-- b001509 | furniture | pages [11] -->
m

<!-- b001510 | furniture | pages [11] -->
m

<!-- b001511 | furniture | pages [11] -->
m

<!-- b001512 | furniture | pages [11] -->
m

<!-- b001513 | furniture | pages [11] -->
m

<!-- b001514 | furniture | pages [11] -->
m

<!-- b001515 | furniture | pages [11] -->
m

<!-- b001516 | furniture | pages [11] -->
m

<!-- b001517 | furniture | pages [11] -->
m

<!-- b001518 | furniture | pages [11] -->
m

<!-- b001519 | furniture | pages [11] -->
m

<!-- b001520 | furniture | pages [11] -->
m

<!-- b001521 | furniture | pages [11] -->
m

<!-- b001522 | furniture | pages [11] -->
m

<!-- b001523 | furniture | pages [11] -->
m

<!-- b001524 | furniture | pages [11] -->
m

<!-- b001525 | furniture | pages [11] -->
m

<!-- b001526 | furniture | pages [11] -->
m

<!-- b001527 | furniture | pages [11] -->
m

<!-- b001528 | furniture | pages [11] -->
m

<!-- b001529 | furniture | pages [11] -->
m

<!-- b001530 | furniture | pages [11] -->
m

<!-- b001531 | furniture | pages [11] -->
m

<!-- b001532 | furniture | pages [11] -->
m

<!-- b001533 | furniture | pages [11] -->
m

<!-- b001534 | furniture | pages [11] -->
m

<!-- b001535 | furniture | pages [11] -->
m

<!-- b001536 | furniture | pages [11] -->
m

<!-- b001537 | furniture | pages [11] -->
m

<!-- b001538 | furniture | pages [11] -->
m

<!-- b001539 | furniture | pages [11] -->
m

<!-- b001540 | furniture | pages [11] -->
m

<!-- b001541 | furniture | pages [11] -->
m

<!-- b001542 | furniture | pages [11] -->
m

<!-- b001543 | furniture | pages [11] -->
m

<!-- b001544 | furniture | pages [11] -->
m

<!-- b001545 | furniture | pages [11] -->
m

<!-- b001546 | furniture | pages [11] -->
m

<!-- b001547 | furniture | pages [11] -->
m

<!-- b001548 | furniture | pages [11] -->
m

<!-- b001549 | furniture | pages [11] -->
m

<!-- b001550 | furniture | pages [11] -->
m

<!-- b001551 | furniture | pages [11] -->
m

<!-- b001552 | furniture | pages [11] -->
m

<!-- b001553 | furniture | pages [11] -->
m

<!-- b001554 | furniture | pages [11] -->
m

<!-- b001555 | furniture | pages [11] -->
m

<!-- b001556 | furniture | pages [11] -->
m

<!-- b001557 | furniture | pages [11] -->
m

<!-- b001558 | furniture | pages [11] -->
m

<!-- b001559 | furniture | pages [11] -->
m

<!-- b001560 | furniture | pages [11] -->
m

<!-- b001561 | furniture | pages [11] -->
m

<!-- b001562 | furniture | pages [11] -->
m

<!-- b001563 | furniture | pages [11] -->
m

<!-- b001564 | furniture | pages [11] -->
m

<!-- b001565 | furniture | pages [11] -->
m

<!-- b001566 | furniture | pages [11] -->
m

<!-- b001567 | furniture | pages [11] -->
m

<!-- b001568 | furniture | pages [11] -->
m

<!-- b001569 | furniture | pages [11] -->
m

<!-- b001570 | furniture | pages [11] -->
m

<!-- b001571 | furniture | pages [11] -->
m

<!-- b001572 | furniture | pages [11] -->
m

<!-- b001573 | furniture | pages [11] -->
m

<!-- b001574 | furniture | pages [11] -->
m

<!-- b001575 | furniture | pages [11] -->
m

<!-- b001576 | furniture | pages [11] -->
m

<!-- b001577 | furniture | pages [11] -->
m

<!-- b001578 | furniture | pages [11] -->
m

<!-- b001579 | furniture | pages [11] -->
m

<!-- b001580 | furniture | pages [11] -->
m

<!-- b001581 | furniture | pages [11] -->
m

<!-- b001582 | furniture | pages [11] -->
m

<!-- b001583 | furniture | pages [11] -->
m

<!-- b001584 | furniture | pages [11] -->
m

<!-- b001585 | furniture | pages [11] -->
m

<!-- b001586 | furniture | pages [11] -->
m

<!-- b001587 | furniture | pages [11] -->
m

<!-- b001588 | furniture | pages [11] -->
m

<!-- b001589 | furniture | pages [11] -->
m

<!-- b001590 | furniture | pages [11] -->
m

<!-- b001591 | furniture | pages [11] -->
m

<!-- b001592 | furniture | pages [11] -->
m

<!-- b001593 | furniture | pages [11] -->
m

<!-- b001594 | furniture | pages [11] -->
m

<!-- b001595 | furniture | pages [11] -->
m

<!-- b001596 | furniture | pages [11] -->
m

<!-- b001597 | furniture | pages [11] -->
m

<!-- b001598 | furniture | pages [11] -->
m

<!-- b001599 | furniture | pages [11] -->
m

<!-- b001600 | furniture | pages [11] -->
m

<!-- b001601 | furniture | pages [11] -->
m

<!-- b001602 | furniture | pages [11] -->
m

<!-- b001603 | furniture | pages [11] -->
m

<!-- b001604 | furniture | pages [11] -->
m

<!-- b001605 | furniture | pages [11] -->
m

<!-- b001606 | furniture | pages [11] -->
m

<!-- b001607 | furniture | pages [11] -->
m

<!-- b001608 | furniture | pages [11] -->
m

<!-- b001609 | furniture | pages [11] -->
m

<!-- b001610 | furniture | pages [11] -->
m

<!-- b001611 | furniture | pages [11] -->
m

<!-- b001612 | furniture | pages [11] -->
m

<!-- b001613 | furniture | pages [11] -->
m

<!-- b001614 | furniture | pages [11] -->
m

<!-- b001615 | furniture | pages [11] -->
m

<!-- b001616 | furniture | pages [11] -->
m

<!-- b001617 | furniture | pages [11] -->
m

<!-- b001618 | furniture | pages [11] -->
m

<!-- b001619 | furniture | pages [11] -->
m

<!-- b001620 | furniture | pages [11] -->
m

<!-- b001621 | furniture | pages [11] -->
m

<!-- b001622 | furniture | pages [11] -->
m

<!-- b001623 | furniture | pages [11] -->
m

<!-- b001624 | furniture | pages [11] -->
m

<!-- b001625 | furniture | pages [11] -->
m

<!-- b001626 | furniture | pages [11] -->
m

<!-- b001627 | furniture | pages [11] -->
m

<!-- b001628 | furniture | pages [11] -->
m

<!-- b001629 | furniture | pages [11] -->
m

<!-- b001630 | furniture | pages [11] -->
m

<!-- b001631 | furniture | pages [11] -->
m

<!-- b001632 | furniture | pages [11] -->
m

<!-- b001633 | furniture | pages [11] -->
m

<!-- b001634 | furniture | pages [11] -->
m

<!-- b001635 | furniture | pages [11] -->
m

<!-- b001636 | furniture | pages [11] -->
m

<!-- b001637 | furniture | pages [11] -->
m

<!-- b001638 | furniture | pages [11] -->
m

<!-- b001639 | furniture | pages [11] -->
m

<!-- b001640 | furniture | pages [11] -->
m

<!-- b001641 | furniture | pages [11] -->
m

<!-- b001642 | furniture | pages [11] -->
m

<!-- b001643 | furniture | pages [11] -->
m

<!-- b001644 | furniture | pages [11] -->
m

<!-- b001645 | furniture | pages [11] -->
m

<!-- b001646 | furniture | pages [11] -->
m

<!-- b001647 | furniture | pages [11] -->
m

<!-- b001648 | furniture | pages [11] -->
m

<!-- b001649 | furniture | pages [11] -->
m

<!-- b001650 | furniture | pages [11] -->
m

<!-- b001651 | furniture | pages [11] -->
m

<!-- b001652 | furniture | pages [11] -->
m

<!-- b001653 | furniture | pages [11] -->
m

<!-- b001654 | furniture | pages [11] -->
m

<!-- b001655 | furniture | pages [11] -->
m

<!-- b001656 | furniture | pages [11] -->
m

<!-- b001657 | furniture | pages [11] -->
m

<!-- b001658 | furniture | pages [11] -->
m

<!-- b001659 | furniture | pages [11] -->
m

<!-- b001660 | furniture | pages [11] -->
m

<!-- b001661 | furniture | pages [11] -->
m

<!-- b001662 | furniture | pages [11] -->
m

<!-- b001663 | furniture | pages [11] -->
m

<!-- b001664 | furniture | pages [11] -->
m

<!-- b001665 | furniture | pages [11] -->
m

<!-- b001666 | furniture | pages [11] -->
m

<!-- b001667 | furniture | pages [11] -->
m

<!-- b001668 | furniture | pages [11] -->
m

<!-- b001669 | furniture | pages [11] -->
m

<!-- b001670 | furniture | pages [11] -->
m

<!-- b001671 | furniture | pages [11] -->
m

<!-- b001672 | furniture | pages [11] -->
m

<!-- b001673 | furniture | pages [11] -->
m

<!-- b001674 | furniture | pages [11] -->
m

<!-- b001675 | furniture | pages [11] -->
m

<!-- b001676 | furniture | pages [11] -->
m

<!-- b001677 | furniture | pages [11] -->
m

<!-- b001678 | furniture | pages [11] -->
m

<!-- b001679 | furniture | pages [11] -->
m

<!-- b001680 | furniture | pages [11] -->
m

<!-- b001681 | furniture | pages [11] -->
m

<!-- b001682 | furniture | pages [11] -->
m

<!-- b001683 | furniture | pages [11] -->
m

<!-- b001684 | furniture | pages [11] -->
m

<!-- b001685 | furniture | pages [11] -->
m

<!-- b001686 | furniture | pages [11] -->
m

<!-- b001687 | furniture | pages [11] -->
m

<!-- b001688 | furniture | pages [11] -->
m

<!-- b001689 | furniture | pages [11] -->
m

<!-- b001690 | furniture | pages [11] -->
m

<!-- b001691 | furniture | pages [11] -->
m

<!-- b001692 | furniture | pages [11] -->
m

<!-- b001693 | furniture | pages [11] -->
m

<!-- b001694 | furniture | pages [11] -->
m

<!-- b001695 | furniture | pages [11] -->
m

<!-- b001696 | furniture | pages [11] -->
m

<!-- b001697 | furniture | pages [11] -->
m

<!-- b001698 | furniture | pages [11] -->
m

<!-- b001699 | furniture | pages [11] -->
m

<!-- b001700 | furniture | pages [11] -->
m

<!-- b001701 | furniture | pages [11] -->
m

<!-- b001702 | furniture | pages [11] -->
m

<!-- b001703 | furniture | pages [11] -->
m

<!-- b001704 | furniture | pages [11] -->
m

<!-- b001705 | furniture | pages [11] -->
m

<!-- b001706 | furniture | pages [11] -->
m

<!-- b001707 | furniture | pages [11] -->
m

<!-- b001708 | furniture | pages [11] -->
m

<!-- b001709 | furniture | pages [11] -->
m

<!-- b001710 | furniture | pages [11] -->
m

<!-- b001711 | furniture | pages [11] -->
m

<!-- b001712 | furniture | pages [11] -->
m

<!-- b001713 | furniture | pages [11] -->
m

<!-- b001714 | furniture | pages [11] -->
m

<!-- b001715 | furniture | pages [11] -->
m

<!-- b001716 | furniture | pages [11] -->
m

<!-- b001717 | furniture | pages [11] -->
m

<!-- b001718 | furniture | pages [11] -->
m

<!-- b001719 | furniture | pages [11] -->
m

<!-- b001720 | furniture | pages [11] -->
m

<!-- b001721 | furniture | pages [11] -->
m

<!-- b001722 | furniture | pages [11] -->
m

<!-- b001723 | furniture | pages [11] -->
m

<!-- b001724 | furniture | pages [11] -->
m

<!-- b001725 | furniture | pages [11] -->
m

<!-- b001726 | furniture | pages [11] -->
m

<!-- b001727 | furniture | pages [11] -->
m

<!-- b001728 | furniture | pages [11] -->
m

<!-- b001729 | furniture | pages [11] -->
m

<!-- b001730 | furniture | pages [11] -->
m

<!-- b001731 | furniture | pages [11] -->
m

<!-- b001732 | furniture | pages [11] -->
m

<!-- b001733 | furniture | pages [11] -->
m

<!-- b001734 | furniture | pages [11] -->
m

<!-- b001735 | furniture | pages [11] -->
m

<!-- b001736 | furniture | pages [11] -->
m

<!-- b001737 | furniture | pages [11] -->
m

<!-- b001738 | furniture | pages [11] -->
m

<!-- b001739 | furniture | pages [11] -->
m

<!-- b001740 | furniture | pages [11] -->
m

<!-- b001741 | furniture | pages [11] -->
m

<!-- b001742 | furniture | pages [11] -->
m

<!-- b001743 | furniture | pages [11] -->
m

<!-- b001744 | furniture | pages [11] -->
m

<!-- b001745 | furniture | pages [11] -->
m

<!-- b001746 | furniture | pages [11] -->
m

<!-- b001747 | furniture | pages [11] -->
m

<!-- b001748 | furniture | pages [11] -->
m

<!-- b001749 | furniture | pages [11] -->
m

<!-- b001750 | furniture | pages [11] -->
m

<!-- b001751 | furniture | pages [11] -->
m

<!-- b001752 | furniture | pages [11] -->
m

<!-- b001753 | furniture | pages [11] -->
m

<!-- b001754 | furniture | pages [11] -->
m

<!-- b001755 | furniture | pages [11] -->
m

<!-- b001756 | furniture | pages [11] -->
m

<!-- b001757 | furniture | pages [11] -->
m

<!-- b001758 | furniture | pages [11] -->
m

<!-- b001759 | furniture | pages [11] -->
m

<!-- b001760 | furniture | pages [11] -->
m

<!-- b001761 | furniture | pages [11] -->
m

<!-- b001762 | furniture | pages [11] -->
m

<!-- b001763 | furniture | pages [11] -->
m

<!-- b001764 | furniture | pages [11] -->
m

<!-- b001765 | furniture | pages [11] -->
m

<!-- b001766 | furniture | pages [11] -->
m

<!-- b001767 | furniture | pages [11] -->
m

<!-- b001768 | furniture | pages [11] -->
m

<!-- b001769 | furniture | pages [11] -->
m

<!-- b001770 | furniture | pages [11] -->
m

<!-- b001771 | furniture | pages [11] -->
m

<!-- b001772 | furniture | pages [11] -->
m

<!-- b001773 | furniture | pages [11] -->
m

<!-- b001774 | furniture | pages [11] -->
m

<!-- b001775 | furniture | pages [11] -->
m

<!-- b001776 | furniture | pages [11] -->
m

<!-- b001777 | furniture | pages [11] -->
m

<!-- b001778 | furniture | pages [11] -->
m

<!-- b001779 | furniture | pages [11] -->
m

<!-- b001780 | furniture | pages [11] -->
m

<!-- b001781 | furniture | pages [11] -->
m

<!-- b001782 | furniture | pages [11] -->
m

<!-- b001783 | furniture | pages [11] -->
m

<!-- b001784 | furniture | pages [11] -->
m

<!-- b001785 | furniture | pages [11] -->
m

<!-- b001786 | furniture | pages [12] -->
Team # 2503389

<!-- b001787 | furniture | pages [12] -->
Page 12 of 26

<!-- b001789 | prose | pages [12] -->
To overcome these limitations, Random Forest (RF) offers a robust alternative. As an en- semble learning method, RF captures non-linear relationships and complex interactions while ranking feature importance, making it suitable for diverse datasets. However, RF can overfit and lacks the transparency of LR.

<!-- b001790 | prose | pages [12] -->
To leverage the strengths of both models, we adopted a hybrid approach that combines the interpretability of LR with the flexibility of RF. This strikes a balance between simplicity and robustness, allowing for more accurate and comprehensive predictions of which countries will win their first Olympic medal.

<!-- b001791 | heading | pages [12] -->
6.2 Feature Engineering

<!-- b001792 | prose | pages [12] -->
To identify countries that have never won medals, we process the table summerOly_athletes.csv to identify athletes who have won medals, then filter the countries they represented in the com- petition. From the list of all countries, we exclude those that have won at least one medal.

<!-- b001793 | prose | pages [12] -->
The core principal here is to simplify the process by counting only unique countries, so duplicates are considered only once.

<!-- b001794 | prose | pages [12] -->
This results in a list of countries that have never won a medal, along with features:

<!-- b001795 | prose | pages [12] -->
• Number of Programs Attended. Count the total number of programs attended by these countries.

<!-- b001796 | prose | pages [12] -->
• Athlete Participation Experience. Calculate the average number of sessions an athlete has participated in.

<!-- b001797 | prose | pages [12] -->
• Program Competition Intensity. Calculate the formula:

<!-- b001798 | prose | pages [12] -->
1 −Number of Medals in the Program , Number of Participants

<!-- b001799 | prose | pages [12] -->
where a value closer to 1 indicates more intense competition.

<!-- b001800 | heading | pages [12] -->
6.3 Analysis of Conditions for Countries Winning Medals for the First

<!-- b001801 | prose | pages [12] -->
Time

<!-- b001802 | prose | pages [12] -->
We calculate the number of countries that won medals for the first time in each Olympic Games (e.g. 5 countries in the 2020 Tokyo Olympics and 3 countries in the 2016 Rio Olympics) and also analyze the distribution of these countries based on features, including statistics like the mean, variance, and trends.

<!-- b001803 | prose | pages [12, 13] -->
关注数学模型 time Medalist Countries 微信公众号：数学模型 As shown in Figure 7 and 8, there is a notable fluctuation in the number of first-time medal- winning countries across different Olympic years. For instance, in the 2020 Tokyo Olympics, 5 countries won their first-ever medals, while in 2016, there were only 3 such countries.

<!-- b001804 | furniture | pages [12] -->
2

<!-- b001805 | furniture | pages [12] -->
MATHmodels

<!-- b001806 | furniture | pages [12] -->
获取更多资讯

<!-- b001807 | furniture | pages [13] -->
Team # 2503389

<!-- b001808 | furniture | pages [13] -->
Page 13 of 26

<!-- b001809 | caption | pages [13] -->
Figure 8: The number of First-

<!-- b001810 | caption | pages [13] -->
Figure 7: Mean and Variance

<!-- b001812 | heading | pages [13] -->
6.4 Model Formulation and Prediction Results

<!-- b001813 | prose | pages [13] -->
We utilized two predictive models—Logistic Regression and Random Forest—to estimate the likelihood of countries earning their first medal in the next Olympics.

<!-- b001814 | prose | pages [13] -->
微信号：MATHmodels

<!-- b001815 | heading | pages [13] -->
6.4.1 Logistic Regression Model

<!-- b001816 | prose | pages [13] -->
The Logistic Regression model predicts the probability of a country earning a medal for the first time based on key features. The model is given by:

<!-- b001817 | prose | pages [13] -->
1 P(Target = 1|X) = 1 + e−(β0+β1·Experience+β2·Programs Attended+β3·Competition Intensity),

<!-- b001818 | prose | pages [13] -->
where P(Target = 1|X) is the probability of earning a first medal, and β0, β1, β2, β3 are the model coefficients for each feature (Experience, Programs Attended, and Competition Inten- sity).

<!-- b001819 | heading | pages [13] -->
6.4.2 Random Forest Model

<!-- b001820 | prose | pages [13] -->
The Random Forest model aggregates the predictions of multiple decision trees. The final pre- diction is the average of all tree predictions:

<!-- b001821 | prose | pages [13] -->
N X ˆy = 1 ˆyi N i=1

<!-- b001822 | prose | pages [13] -->
where ˆy is the predicted probability, N is the number of trees, and ˆyi is the prediction of the i-th tree.

<!-- b001823 | heading | pages [13] -->
6.4.3 Prediction Results

<!-- b001824 | prose | pages [13] -->
The prediction results from the two models are as follows:

<!-- b001825 | prose | pages [13] -->
• Logistic Regression Prediction: Angola, El Salvador, Papua New Guinea

<!-- b001826 | prose | pages [13, 14] -->
• Random Forest Prediction: Angola We then utilized the Poisson binomial distribution combined with Monte Carlo simulations to estimate the expected number of countries likely to win their first Olympic medal and their confidence intervals. The simulation results, shown in Figure 9, indicate that the probability is highest when the number of first-time medal-winning countries is exactly 3.

<!-- b001827 | furniture | pages [14] -->
Team # 2503389

<!-- b001828 | furniture | pages [14] -->
Page 14 of 26

<!-- b001830 | caption | pages [14] -->
Figure 9: Monte Carlo Simulation of First-Time Medal-Winning Countries

<!-- b001831 | prose | pages [14] -->
Based on these findings, we conclude that 3 countries are the most likely to win their first Olympic medal in the next Games.The simulation results align well with our predictions, con- firming the robustness of the model’s estimates. The Monte Carlo simulation not only validated the expected outcomes but also provided a probabilistic range for the number of countries likely to win their first medal in the next Olympics.

<!-- b001832 | prose | pages [14] -->
These predictions reflect the model’s output probabilities, with Angola appearing as a com- m m m m m m m m m m m m m m m m m m m m m m mon prediction in both models, suggesting a strong likelihood of this country earning its first m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m medal. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001833 | heading | pages [14] -->
6.5 Estimate odds

<!-- b001834 | prose | pages [14] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The odds of predicting which countries will earn their first medal in the next Olympics are m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001835 | prose | pages [14] -->
estimated using their respective cross-validation accuracies. The table below summarizes the estimated odds for each model:

<!-- b001836 | heading | pages [14] -->
Model

<!-- b001837 | heading | pages [14] -->
Cross-Validation Accuracy

<!-- b001838 | prose | pages [14] -->
Estimated Odds (Correctness) Logistic Regression 88.09% 4:1 (80% chance) Random Forest 94.12% 16:1 (94% chance)

<!-- b001839 | caption | pages [14] -->
Table 6: Estimated Odds for Predicting First Medal Winning Countries

<!-- b001840 | prose | pages [14] -->
关注数学模型

<!-- b001841 | furniture | pages [14] -->
2

<!-- b001842 | furniture | pages [14] -->
MATHmodels

<!-- b001843 | furniture | pages [14] -->
获取更多资讯

<!-- b001844 | furniture | pages [15] -->
Team # 2503389

<!-- b001845 | furniture | pages [15] -->
Page 15 of 26

<!-- b001846 | heading | pages [15] -->
7 Strategic Importance Assessment Model for Olympic Sports

<!-- b001847 | prose | pages [15] -->
(SIAMOS)

<!-- b001848 | prose | pages [15] -->
To measure the strategic importance of a specific sport s for a given country c, we establish a comprehensive evaluation framework based on four key indicators.

<!-- b001849 | heading | pages [15] -->
7.1 Model Development and Evaluation Framework

<!-- b001850 | prose | pages [15] -->
微信公众号：数学模型

<!-- b001851 | heading | pages [15] -->
7.1.1 Description of Indicators to Evaluate the Importance of Sport

<!-- b001852 | prose | pages [15] -->
The four key indicators used to evaluate the importance of a sport in the context of Olympic performance are:

<!-- b001853 | prose | pages [15] -->
• NMP (National Medal Proportion): Proportion of medals a sport contributes to a na- tion’s total medals.

<!-- b001854 | prose | pages [15] -->
• GCP (Global Competitive Presence): A country’s competitive strength in a sport rela- tive to global performanceBernard2004.

<!-- b001855 | prose | pages [15] -->
微信号：MATHmodels

<!-- b001856 | prose | pages [15] -->
• LAS (Long-term Achievement Stability): Stability of performance in a sport over the last five Olympics.

<!-- b001857 | prose | pages [15] -->
• ASD (Athlete Sport Distribution): Proportion of athletes allocated to a specific sport relative to the total number of athletes.

<!-- b001858 | prose | pages [15] -->
Each indicator is standardized using Min-Max normalization to ensure cross-country com- parability. A hybrid weighting scheme, integrating Principal Component Analysis (PCA) with expert validation, assigns weights of 40%, 30%, 20%, and 10%, respectively. This reflects the relative importance of each indicator in evaluating a sport’s strategic significance.

<!-- b001859 | caption | pages [15] -->
Table 7: Evaluation Indicators, Weights, and Formulas

<!-- b001860 | prose | pages [15] -->
Indicator Formula Standardization (Weight) Medalsc,s Total Medalsc × 100% NMP (40%) Min-Max nor- malization Medalsc,s Global Medalss × 100% GCP (30%) Min-Max nor- malization 1 −σ LAS (20%) Min-Max nor- µ malization Athletesc,s ASD (10%) Total Athletesc × 100% Min-Max nor- malization

<!-- b001861 | heading | pages [15] -->
7.1.2 Model Construction

<!-- b001862 | prose | pages [15] -->
The SIAMOS model integrates the four indicators to compute the importance score (ISc,s) for each sport s in each country c:

<!-- b001863 | prose | pages [15] -->
ISc,s = α · NMPnorm + β · GCPnorm + γ · LASnorm + δ · ASDnorm

<!-- b001864 | prose | pages [15] -->
where α : β : γ : δ = 4 : 3 : 2 : 1 (40%, 30%, 20%, 10%). m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001865 | furniture | pages [15] -->
m

<!-- b001866 | furniture | pages [15] -->
m

<!-- b001867 | furniture | pages [15] -->
m

<!-- b001868 | furniture | pages [15] -->
m

<!-- b001869 | furniture | pages [15] -->
m

<!-- b001870 | furniture | pages [15] -->
m

<!-- b001871 | furniture | pages [15] -->
m

<!-- b001872 | furniture | pages [15] -->
m

<!-- b001873 | furniture | pages [15] -->
m

<!-- b001874 | furniture | pages [15] -->
m

<!-- b001875 | furniture | pages [15] -->
m

<!-- b001876 | furniture | pages [15] -->
m

<!-- b001877 | furniture | pages [15] -->
m

<!-- b001878 | furniture | pages [15] -->
m

<!-- b001879 | furniture | pages [15] -->
m

<!-- b001880 | furniture | pages [15] -->
m

<!-- b001881 | furniture | pages [15] -->
m

<!-- b001882 | furniture | pages [15] -->
m

<!-- b001883 | furniture | pages [15] -->
m

<!-- b001884 | furniture | pages [15] -->
m

<!-- b001885 | furniture | pages [15] -->
m

<!-- b001886 | furniture | pages [15] -->
m

<!-- b001887 | furniture | pages [15] -->
m

<!-- b001888 | furniture | pages [15] -->
m

<!-- b001889 | furniture | pages [15] -->
m

<!-- b001890 | furniture | pages [15] -->
m

<!-- b001891 | furniture | pages [15] -->
m

<!-- b001892 | furniture | pages [15] -->
m

<!-- b001893 | furniture | pages [15] -->
m

<!-- b001894 | furniture | pages [15] -->
m

<!-- b001895 | furniture | pages [15] -->
m

<!-- b001896 | furniture | pages [15] -->
m

<!-- b001897 | furniture | pages [15] -->
m

<!-- b001898 | furniture | pages [15] -->
m

<!-- b001899 | furniture | pages [15] -->
m

<!-- b001900 | furniture | pages [15] -->
m

<!-- b001901 | furniture | pages [15] -->
m

<!-- b001902 | furniture | pages [15] -->
m

<!-- b001903 | furniture | pages [15] -->
m

<!-- b001904 | furniture | pages [15] -->
m

<!-- b001905 | furniture | pages [15] -->
m

<!-- b001906 | furniture | pages [15] -->
m

<!-- b001907 | furniture | pages [15] -->
m

<!-- b001908 | furniture | pages [15] -->
m

<!-- b001909 | furniture | pages [15] -->
m

<!-- b001910 | furniture | pages [15] -->
m

<!-- b001911 | furniture | pages [15] -->
m

<!-- b001912 | furniture | pages [15] -->
m

<!-- b001913 | furniture | pages [15] -->
m

<!-- b001914 | furniture | pages [15] -->
m

<!-- b001915 | furniture | pages [15] -->
m

<!-- b001916 | furniture | pages [15] -->
m

<!-- b001917 | furniture | pages [15] -->
m

<!-- b001918 | furniture | pages [15] -->
m

<!-- b001919 | furniture | pages [15] -->
m

<!-- b001920 | furniture | pages [15] -->
m

<!-- b001921 | furniture | pages [15] -->
m

<!-- b001922 | furniture | pages [15] -->
m

<!-- b001923 | furniture | pages [15] -->
m

<!-- b001924 | furniture | pages [15] -->
m

<!-- b001925 | furniture | pages [15] -->
m

<!-- b001926 | furniture | pages [15] -->
m

<!-- b001927 | furniture | pages [15] -->
m

<!-- b001928 | furniture | pages [15] -->
m

<!-- b001929 | furniture | pages [15] -->
m

<!-- b001930 | furniture | pages [15] -->
m

<!-- b001931 | furniture | pages [15] -->
m

<!-- b001932 | furniture | pages [15] -->
m

<!-- b001933 | furniture | pages [15] -->
m

<!-- b001934 | furniture | pages [15] -->
m

<!-- b001935 | furniture | pages [15] -->
m

<!-- b001936 | furniture | pages [15] -->
m

<!-- b001937 | furniture | pages [15] -->
m

<!-- b001938 | furniture | pages [15] -->
m

<!-- b001939 | furniture | pages [15] -->
m

<!-- b001940 | furniture | pages [15] -->
m

<!-- b001941 | furniture | pages [15] -->
m

<!-- b001942 | furniture | pages [15] -->
m

<!-- b001943 | furniture | pages [15] -->
m

<!-- b001944 | furniture | pages [15] -->
m

<!-- b001945 | furniture | pages [15] -->
m

<!-- b001946 | furniture | pages [15] -->
m

<!-- b001947 | furniture | pages [15] -->
m

<!-- b001948 | furniture | pages [15] -->
m

<!-- b001949 | furniture | pages [15] -->
m

<!-- b001950 | furniture | pages [15] -->
m

<!-- b001951 | furniture | pages [15] -->
m

<!-- b001952 | furniture | pages [15] -->
m

<!-- b001953 | furniture | pages [15] -->
m

<!-- b001954 | furniture | pages [15] -->
m

<!-- b001955 | furniture | pages [15] -->
m

<!-- b001956 | furniture | pages [15] -->
m

<!-- b001957 | furniture | pages [15] -->
m

<!-- b001958 | furniture | pages [15] -->
m

<!-- b001959 | furniture | pages [15] -->
m

<!-- b001960 | furniture | pages [15] -->
m

<!-- b001961 | furniture | pages [15] -->
m

<!-- b001962 | furniture | pages [15] -->
m

<!-- b001963 | furniture | pages [15] -->
m

<!-- b001964 | furniture | pages [15] -->
m

<!-- b001965 | furniture | pages [15] -->
m

<!-- b001966 | furniture | pages [15] -->
m

<!-- b001967 | furniture | pages [15] -->
m

<!-- b001968 | furniture | pages [15] -->
m

<!-- b001969 | furniture | pages [15] -->
m

<!-- b001970 | furniture | pages [15] -->
m

<!-- b001971 | furniture | pages [15] -->
m

<!-- b001972 | furniture | pages [15] -->
m

<!-- b001973 | furniture | pages [15] -->
m

<!-- b001974 | furniture | pages [15] -->
m

<!-- b001975 | furniture | pages [15] -->
m

<!-- b001976 | furniture | pages [15] -->
m

<!-- b001977 | furniture | pages [15] -->
m

<!-- b001978 | furniture | pages [15] -->
m

<!-- b001979 | furniture | pages [15] -->
m

<!-- b001980 | furniture | pages [15] -->
m

<!-- b001981 | furniture | pages [15] -->
m

<!-- b001982 | furniture | pages [15] -->
m

<!-- b001983 | furniture | pages [15] -->
m

<!-- b001984 | furniture | pages [15] -->
m

<!-- b001985 | furniture | pages [15] -->
m

<!-- b001986 | furniture | pages [15] -->
m

<!-- b001987 | furniture | pages [15] -->
m

<!-- b001988 | furniture | pages [15] -->
m

<!-- b001989 | furniture | pages [15] -->
m

<!-- b001990 | furniture | pages [15] -->
m

<!-- b001991 | furniture | pages [15] -->
m

<!-- b001992 | furniture | pages [15] -->
m

<!-- b001993 | furniture | pages [15] -->
m

<!-- b001994 | furniture | pages [15] -->
m

<!-- b001995 | furniture | pages [15] -->
m

<!-- b001996 | furniture | pages [15] -->
m

<!-- b001997 | furniture | pages [15] -->
m

<!-- b001998 | furniture | pages [15] -->
m

<!-- b001999 | furniture | pages [15] -->
m

<!-- b002000 | furniture | pages [15] -->
m

<!-- b002001 | furniture | pages [15] -->
m

<!-- b002002 | furniture | pages [15] -->
m

<!-- b002003 | furniture | pages [15] -->
m

<!-- b002004 | furniture | pages [15] -->
m

<!-- b002005 | furniture | pages [15] -->
m

<!-- b002006 | furniture | pages [15] -->
m

<!-- b002007 | furniture | pages [15] -->
m

<!-- b002008 | furniture | pages [15] -->
m

<!-- b002009 | furniture | pages [15] -->
m

<!-- b002010 | furniture | pages [15] -->
m

<!-- b002011 | furniture | pages [15] -->
m

<!-- b002012 | furniture | pages [15] -->
m

<!-- b002013 | furniture | pages [15] -->
m

<!-- b002014 | furniture | pages [15] -->
m

<!-- b002015 | furniture | pages [15] -->
m

<!-- b002016 | furniture | pages [15] -->
m

<!-- b002017 | furniture | pages [15] -->
m

<!-- b002018 | furniture | pages [15] -->
m

<!-- b002019 | furniture | pages [15] -->
m

<!-- b002020 | furniture | pages [15] -->
m

<!-- b002021 | furniture | pages [15] -->
m

<!-- b002022 | furniture | pages [15] -->
m

<!-- b002023 | furniture | pages [15] -->
m

<!-- b002024 | furniture | pages [15] -->
m

<!-- b002025 | furniture | pages [15] -->
m

<!-- b002026 | furniture | pages [15] -->
m

<!-- b002027 | furniture | pages [15] -->
m

<!-- b002028 | furniture | pages [15] -->
m

<!-- b002029 | furniture | pages [15] -->
m

<!-- b002030 | furniture | pages [15] -->
m

<!-- b002031 | furniture | pages [15] -->
m

<!-- b002032 | furniture | pages [15] -->
m

<!-- b002033 | furniture | pages [15] -->
m

<!-- b002034 | furniture | pages [15] -->
m

<!-- b002035 | furniture | pages [15] -->
m

<!-- b002036 | furniture | pages [15] -->
m

<!-- b002037 | furniture | pages [15] -->
m

<!-- b002038 | furniture | pages [15] -->
m

<!-- b002039 | furniture | pages [15] -->
m

<!-- b002040 | furniture | pages [15] -->
m

<!-- b002041 | furniture | pages [15] -->
m

<!-- b002042 | furniture | pages [15] -->
m

<!-- b002043 | furniture | pages [15] -->
m

<!-- b002044 | furniture | pages [15] -->
m

<!-- b002045 | furniture | pages [15] -->
m

<!-- b002046 | furniture | pages [15] -->
m

<!-- b002047 | furniture | pages [15] -->
m

<!-- b002048 | furniture | pages [15] -->
m

<!-- b002049 | furniture | pages [15] -->
m

<!-- b002050 | furniture | pages [15] -->
m

<!-- b002051 | furniture | pages [15] -->
m

<!-- b002052 | furniture | pages [15] -->
m

<!-- b002053 | furniture | pages [15] -->
m

<!-- b002054 | furniture | pages [15] -->
m

<!-- b002055 | furniture | pages [15] -->
m

<!-- b002056 | furniture | pages [15] -->
m

<!-- b002057 | furniture | pages [15] -->
m

<!-- b002058 | furniture | pages [15] -->
m

<!-- b002059 | furniture | pages [15] -->
m

<!-- b002060 | furniture | pages [15] -->
m

<!-- b002061 | furniture | pages [15] -->
m

<!-- b002062 | furniture | pages [15] -->
m

<!-- b002063 | furniture | pages [15] -->
m

<!-- b002064 | furniture | pages [15] -->
m

<!-- b002065 | furniture | pages [15] -->
m

<!-- b002066 | furniture | pages [15] -->
m

<!-- b002067 | furniture | pages [15] -->
m

<!-- b002068 | furniture | pages [15] -->
m

<!-- b002069 | furniture | pages [15] -->
m

<!-- b002070 | furniture | pages [15] -->
m

<!-- b002071 | furniture | pages [15] -->
m

<!-- b002072 | furniture | pages [15] -->
m

<!-- b002073 | furniture | pages [15] -->
m

<!-- b002074 | furniture | pages [15] -->
m

<!-- b002075 | furniture | pages [15] -->
m

<!-- b002076 | furniture | pages [15] -->
m

<!-- b002077 | furniture | pages [15] -->
m

<!-- b002078 | furniture | pages [15] -->
m

<!-- b002079 | furniture | pages [15] -->
m

<!-- b002080 | furniture | pages [15] -->
m

<!-- b002081 | furniture | pages [15] -->
m

<!-- b002082 | furniture | pages [15] -->
m

<!-- b002083 | furniture | pages [15] -->
m

<!-- b002084 | furniture | pages [15] -->
m

<!-- b002085 | furniture | pages [15] -->
m

<!-- b002086 | furniture | pages [15] -->
m

<!-- b002087 | furniture | pages [15] -->
m

<!-- b002088 | furniture | pages [15] -->
m

<!-- b002089 | furniture | pages [15] -->
m

<!-- b002090 | furniture | pages [15] -->
m

<!-- b002091 | furniture | pages [15] -->
m

<!-- b002092 | furniture | pages [15] -->
m

<!-- b002093 | furniture | pages [15] -->
m

<!-- b002094 | furniture | pages [15] -->
m

<!-- b002095 | furniture | pages [15] -->
m

<!-- b002096 | furniture | pages [15] -->
m

<!-- b002097 | furniture | pages [15] -->
m

<!-- b002098 | furniture | pages [15] -->
m

<!-- b002099 | furniture | pages [15] -->
m

<!-- b002100 | furniture | pages [15] -->
m

<!-- b002101 | furniture | pages [15] -->
m

<!-- b002102 | furniture | pages [15] -->
m

<!-- b002103 | furniture | pages [15] -->
m

<!-- b002104 | furniture | pages [15] -->
m

<!-- b002105 | furniture | pages [15] -->
m

<!-- b002106 | furniture | pages [15] -->
m

<!-- b002107 | furniture | pages [15] -->
m

<!-- b002108 | furniture | pages [15] -->
m

<!-- b002109 | furniture | pages [15] -->
m

<!-- b002110 | furniture | pages [15] -->
m

<!-- b002111 | furniture | pages [15] -->
m

<!-- b002112 | furniture | pages [15] -->
m

<!-- b002113 | furniture | pages [15] -->
m

<!-- b002114 | furniture | pages [15] -->
m

<!-- b002115 | furniture | pages [15] -->
m

<!-- b002116 | furniture | pages [15] -->
m

<!-- b002117 | furniture | pages [15] -->
m

<!-- b002118 | furniture | pages [15] -->
m

<!-- b002119 | furniture | pages [15] -->
m

<!-- b002120 | furniture | pages [15] -->
m

<!-- b002121 | furniture | pages [15] -->
m

<!-- b002122 | furniture | pages [15] -->
m

<!-- b002123 | furniture | pages [15] -->
m

<!-- b002124 | furniture | pages [15] -->
m

<!-- b002125 | furniture | pages [15] -->
m

<!-- b002126 | furniture | pages [15] -->
m

<!-- b002127 | furniture | pages [15] -->
m

<!-- b002128 | furniture | pages [15] -->
m

<!-- b002129 | furniture | pages [15] -->
m

<!-- b002130 | furniture | pages [15] -->
m

<!-- b002131 | furniture | pages [15] -->
m

<!-- b002132 | furniture | pages [15] -->
m

<!-- b002133 | furniture | pages [15] -->
m

<!-- b002134 | furniture | pages [15] -->
m

<!-- b002135 | furniture | pages [15] -->
m

<!-- b002136 | furniture | pages [15] -->
m

<!-- b002137 | furniture | pages [15] -->
m

<!-- b002138 | furniture | pages [15] -->
m

<!-- b002139 | furniture | pages [15] -->
m

<!-- b002140 | furniture | pages [15] -->
m

<!-- b002141 | furniture | pages [15] -->
m

<!-- b002142 | furniture | pages [15] -->
m

<!-- b002143 | furniture | pages [15] -->
m

<!-- b002144 | furniture | pages [15] -->
m

<!-- b002145 | furniture | pages [15] -->
m

<!-- b002146 | furniture | pages [15] -->
m

<!-- b002147 | furniture | pages [15] -->
m

<!-- b002148 | furniture | pages [15] -->
m

<!-- b002149 | furniture | pages [15] -->
m

<!-- b002150 | furniture | pages [15] -->
m

<!-- b002151 | furniture | pages [15] -->
m

<!-- b002152 | furniture | pages [15] -->
m

<!-- b002153 | furniture | pages [15] -->
m

<!-- b002154 | furniture | pages [15] -->
m

<!-- b002155 | furniture | pages [15] -->
m

<!-- b002156 | furniture | pages [15] -->
m

<!-- b002157 | furniture | pages [15] -->
m

<!-- b002158 | furniture | pages [15] -->
m

<!-- b002159 | furniture | pages [15] -->
m

<!-- b002160 | furniture | pages [15] -->
m

<!-- b002161 | furniture | pages [15] -->
m

<!-- b002162 | furniture | pages [15] -->
m

<!-- b002163 | furniture | pages [15] -->
m

<!-- b002164 | furniture | pages [15] -->
m

<!-- b002165 | furniture | pages [15] -->
m

<!-- b002166 | furniture | pages [15] -->
m

<!-- b002167 | furniture | pages [15] -->
m

<!-- b002168 | furniture | pages [15] -->
m

<!-- b002169 | furniture | pages [15] -->
m

<!-- b002170 | furniture | pages [15] -->
m

<!-- b002171 | furniture | pages [15] -->
m

<!-- b002172 | furniture | pages [15] -->
m

<!-- b002173 | furniture | pages [15] -->
m

<!-- b002174 | furniture | pages [15] -->
m

<!-- b002175 | furniture | pages [15] -->
m

<!-- b002176 | furniture | pages [15] -->
m

<!-- b002177 | furniture | pages [15] -->
m

<!-- b002178 | furniture | pages [15] -->
m

<!-- b002179 | furniture | pages [15] -->
m

<!-- b002180 | furniture | pages [15] -->
m

<!-- b002181 | furniture | pages [15] -->
m

<!-- b002182 | furniture | pages [15] -->
m

<!-- b002183 | furniture | pages [15] -->
m

<!-- b002184 | furniture | pages [15] -->
m

<!-- b002185 | furniture | pages [15] -->
m

<!-- b002186 | furniture | pages [15] -->
m

<!-- b002187 | furniture | pages [15] -->
m

<!-- b002188 | furniture | pages [15] -->
m

<!-- b002189 | furniture | pages [16] -->
Team # 2503389

<!-- b002190 | furniture | pages [16] -->
Page 16 of 26

<!-- b002191 | heading | pages [16] -->
7.2 Result 1: Relationship Between Events and Medal Counts

<!-- b002192 | caption | pages [16] -->
Figure 10: Correlation analysis: (a) shows the impact of the number of events, while (b) high-

<!-- b002193 | prose | pages [16] -->
lights the influence of sports on medal counts.

<!-- b002194 | prose | pages [16] -->
Conclusion: As shown in Figure 10, the number of events is positively correlated with the medal counts of participating countries. Similarly, the diversity of events also demonstrates a positive correlation with medal counts. These findings indicate that both the quantity and variety of events positively impact a nation’s medal-winning potential.

<!-- b002195 | heading | pages [16] -->
7.3 Result 2: Sport-Specific Importance Across Nations

<!-- b002196 | heading | pages [16] -->
7.3.1 Calculated Scores

<!-- b002197 | prose | pages [16] -->
The following table presents the calculated importance scores for selected countries and sports:

<!-- b002198 | caption | pages [16] -->
Table 8: Importance Scores for Selected Countries and Sports

<!-- b002199 | prose | pages [16] -->
Country Sport Importance Score (IS) Ranking China Diving 33.1 1 China Table Tennis 29.6 2 USA Swimming 39.8 1 USA Basketball 27.8 2 Korea Archery 37.4 1 Korea Badminton 31.8 2 Japan Judo 36.5 1 Japan Gymnastics 30.2 2 Australia Swimming 38.6 1 Australia Cycling 29.7 2

<!-- b002200 | heading | pages [16] -->
7.3.2 Insights and Recommendations

<!-- b002201 | prose | pages [16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002202 | prose | pages [16] -->
• China: Diving (IS = 33.1) and Table Tennis (IS = 29.6) dominate, reflecting historical m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m strengths. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002203 | prose | pages [16] -->
• USA: Swimming (IS = 39.8) and Basketball (IS = 27.8) remain priorities. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002204 | prose | pages [16, 17] -->
关注数学模型 • Korea: Archery (IS = 37.4) and Badminton (IS = 31.8) highlight focused investments.

<!-- b002205 | furniture | pages [16] -->
2

<!-- b002206 | furniture | pages [16] -->
MATHmodels

<!-- b002207 | furniture | pages [16] -->
获取更多资讯

<!-- b002208 | furniture | pages [17] -->
Page 17 of 26

<!-- b002209 | furniture | pages [17] -->
Team# 2503389

<!-- b002211 | prose | pages [17] -->
• Others: Japan: Judo (IS = 36.5), Gymnastics (IS = 30.2); Australia: Swimming (IS = 38.6), Cycling (IS = 29.7).

<!-- b002212 | prose | pages [17] -->
These insights aid strategic planning to maximize medal potential in future Olympics.

<!-- b002213 | heading | pages [17] -->
7.4 Result 3: Impact of Host Nation's Event Selection on Medal Outcomes

<!-- b002214 | prose | pages [17] -->
To evaluate the impact of a host nation's event selection on medal outcomes, we use the

<!-- b002215 | heading | pages [17] -->
Global Competitive Proportion (GCP) metric, which quantifies a country's competitive strength

<!-- b002216 | prose | pages [17] -->
in a sport relative to global performanceBernard2004. Table 9 provides the GCP scores for selected countries and sports.

<!-- b002217 | caption | pages [17] -->
Table 9: Global Competitive Proportion (GCP) Scores for Selected Countries and Sports

<!-- b002218 | prose | pages [17] -->
Cycling Country Swimming Track and Field Taekwondo Shooting 0.1085 USA 0.3214 0.2841 0.0962 0.0523 CHN 0.1263 0.1435 0.2782 0.2648 0.0712 0.0823 0.1274 0.2167 0.1354 JPN 0.0896 AUS 0.3645 0.0912 0.0438 0.1824 0.0417 KOR 0.0374 0.3084 0.0512 0.0856 0.0685

<!-- b002219 | heading | pages [17] -->
7.4.1 Impact of Host Nation Event Selection

<!-- b002220 | prose | pages [17] -->
By examining the host nation's choice of events, we identify two key effects:

<!-- b002221 | heading | pages [17] -->
1. Enhancement of Strong Sports: Host nations often add events in their strongest sports

<!-- b002222 | prose | pages [17] -->
to maximize medal outcomes. For example:

<!-- b002223 | prose | pages [17] -->
The USA increased swimming and track events during the 1996 Atlanta Olympics, securing multiple gold medals.

<!-- b002224 | prose | pages [17] -->
China introduced additional shooting events in the 2008 Beijing Olympics, signifi- cantly boosting their medal tally in the sport.

<!-- b002225 | prose | pages [17] -->
●

<!-- b002226 | heading | pages [17] -->
2. Increased Competitiveness in Targeted Events: Hosting provides advantages in prepa-

<!-- b002227 | prose | pages [17] -->
ration, venue familiarity, and public support, making host nations more competitive in traditionally weaker events. For instance:

<!-- b002228 | prose | pages [17] -->
Australia leveraged its host status in 2000 to achieve unexpected medals in cycling and field events.

<!-- b002229 | prose | pages [17] -->
Korea used the 1988 Seoul Olympics to establish dominance in Taekwondo, a sport that was newly introduced at the time.

<!-- b002230 | prose | pages [17] -->
These findings underscore the strategic role of host nation event selection in shaping medal outcomes and highlight opportunities for future host countries to optimize their strategies.

<!-- b002231 | furniture | pages [18] -->
Team# 2503389

<!-- b002232 | furniture | pages [18] -->
Page 18 of 26

<!-- b002233 | heading | pages [18] -->
8 Contribution of the Great Coach

<!-- b002234 | heading | pages [18] -->
8.1 Definition of Great Coach

<!-- b002235 | prose | pages [18] -->
A Great Coach (GC) is defined as a coaching professional whose recruitment results in a statistically significant increase (p < 0.05) in medal attainment within the targeted Olympic sport, measured through pre- and post-appointment performance. The criteria for a Great Coach include:

<!-- b002236 | prose | pages [18] -->
Immediate Impact: ≥15% medal growth within the first Olympic cycle, improved on his- torical performance.

<!-- b002237 | prose | pages [18] -->
Sustained Improvement: Maintaining ≥80% of peak performance for at least two subse- quent Olympic Games.

<!-- b002238 | prose | pages [18] -->
Sport-Level Considerations:

<!-- b002239 | prose | pages [18] -->
• When a coach is introduced, whether as a sport head coach or an event-specific coach, they influence other events within the same sport through collaboration and athlete interaction.

<!-- b002240 | prose | pages [18] -->
• The number of events within each sport may vary between Olympic Games, so consider- ing the sport level helps mitigate instability caused by this factor.

<!-- b002241 | prose | pages [18] -->
• Focusing only on individual event data may result in small sample sizes, increasing the likelihood of randomness and potentially biasing the conclusions.

<!-- b002242 | heading | pages [18] -->
8.2 Data Processing Framework

<!-- b002243 | heading | pages [18] -->
8.2.1 Medal Weighting System

<!-- b002244 | prose | pages [18] -->
• Medal Weight Assignment: Defined weights (No Medal=0.1, Bronze=0.4, Silver=0.6, Gold=0.9) to quantify performance quality

<!-- b002245 | prose | pages [18] -->
• National Performance Metric: Calculated weighted scores per country-sport-year triad:

<!-- b002246 | prose | pages [18] -->
4 Φc,s,y = ∑wi · Ni, w ∈ {0.1, 0.4, 0.6, 0.9} i=1

<!-- b002247 | prose | pages [18] -->
where Ni counts medal type i occurrences

<!-- b002248 | prose | pages [18] -->
8.2.2 Medal Data Standardization

<!-- b002249 | prose | pages [18] -->
• Binary Medal Encoding: Transformed medal outcomes into Boolean indicators (1=medal earned, 0=otherwise) for cross-event aggregation

<!-- b002250 | prose | pages [18] -->
• Sport Taxonomy Harmonization: Unified historical records of equivalent disciplines (e.g., Artistic/Synchronized Swimming) using IOC nomenclature

<!-- b002251 | heading | pages [18] -->
8.3 Calculation of Coefficients Based on Breakpoint Regression Model

<!-- b002252 | prose | pages [18] -->
To analyze the impact of a Great Coach on medal counts, we use the following model:

<!-- b002253 | prose | pages [18, 19] -->
关注数学模型 MedalCounts = β0 + β1 · Year + β2 · is_great_coach + β3 · (is_great_coach × Year) + ϵ 微信公众号：数学模型 Key Steps in the Analysis:

<!-- b002254 | furniture | pages [18] -->
获取更多资讯

<!-- b002255 | furniture | pages [19] -->
Team # 2503389

<!-- b002256 | furniture | pages [19] -->
Page 19 of 26

<!-- b002258 | heading | pages [19] -->
1. Time Period Division: Divide the Olympic data into three periods based on the coaching

<!-- b002259 | prose | pages [19] -->
situation:

<!-- b002260 | prose | pages [19] -->
• Pre-coaching: The three Olympic Games before the coach took over.

<!-- b002261 | prose | pages [19] -->
• Coaching Period: The period during which the great coach was actively coaching.

<!-- b002262 | prose | pages [19] -->
• Post-coaching: The period after the coach left.

<!-- b002263 | prose | pages [19] -->
微信号：MATHmodels

<!-- b002264 | heading | pages [19] -->
2. Metric Calculation:

<!-- b002265 | prose | pages [19] -->
• Medal Score: Averaged by country and event.

<!-- b002266 | prose | pages [19] -->
• Total Medals: Summed by country and event.

<!-- b002267 | heading | pages [19] -->
3. Model Fitting and Robustness Check: Use the breakpoint regression model to assess

<!-- b002268 | prose | pages [19] -->
the impact of the Great Coach on medal counts. Test the significance of the interaction term coefficient (β3) to determine whether the coach effect varies with years. Then, re- place the dependent variable with “medal score” and refit the model. Finally, compare results across different countries and events.

<!-- b002269 | heading | pages [19] -->
8.4 Case Study Analysis (Focusing on Three Key Sports)

<!-- b002270 | heading | pages [19] -->
8.4.1 Introduction:3 Representative Case

<!-- b002271 | prose | pages [19] -->
To analyze the “great coach” effect on medal counts, we analyzed data on medal changes and identified three representative countries aligned with its :

<!-- b002272 | prose | pages [19] -->
Country Sport Coach China Artistic Swimming Keiko Kageyama United Kingdom Cycling Dave Brailsford United States Women’s Gymnastics Béla and Marta Károlyi

<!-- b002273 | caption | pages [19] -->
Table 10: Countries, Sports, and Corresponding Coaches

<!-- b002274 | heading | pages [19] -->
8.4.2 Results Analysis

<!-- b002275 | prose | pages [19] -->
To quantify the impact of exceptional coaches on medal counts, we calculated the contribution value (Ci) for each coach using the following formula:

<!-- b002276 | prose | pages [19] -->
Ci = βi Di

<!-- b002277 | prose | pages [19] -->
where:

<!-- b002278 | prose | pages [19] -->
• βi: The direct effect of the coach on medal counts (regression coefficient).

<!-- b002279 | furniture | pages [20] -->
Team # 2503389

<!-- b002280 | furniture | pages [20] -->
Page 20 of 26

<!-- b002281 | prose | pages [20] -->
• Di: The weighted average difference in total medals between the two Olympic Games before and after the coach’s tenure.

<!-- b002282 | prose | pages [20] -->
By analyzing significant changes in medal counts and referencing relevant data, three ex- emplary cases of the ”Great Coach Effect” were identified:

<!-- b002283 | heading | pages [20] -->
1. Béla and Marta Károlyi (USA Women’s Gymnastics): Regression coefficient (βi) =

<!-- b002284 | prose | pages [20] -->
0.3.

<!-- b002285 | heading | pages [20] -->
2. Keiko Kageyama (UK Cycling): Regression coefficient (βi) = 6.9.

<!-- b002286 | heading | pages [20] -->
3. Keiko Kageyama (China Artistic Swimming): Regression coefficient (βi) = 1.3.

<!-- b002287 | prose | pages [20] -->
Using the formula above, the contribution values (Ci) were computed for each coach:

<!-- b002288 | prose | pages [20] -->
0.3

<!-- b002289 | prose | pages [20] -->
• Béla and Marta Károlyi: Contribution value (Ci) = DUSA = 1.7.

<!-- b002290 | prose | pages [20] -->
6.9

<!-- b002291 | prose | pages [20] -->
• Keiko Kageyama (UK Cycling): Contribution value (Ci) = DUK = 1.7.

<!-- b002292 | prose | pages [20] -->
1.3

<!-- b002293 | prose | pages [20] -->
• Keiko Kageyama (China Artistic Swimming): Contribution value (Ci) = DCHN = 1.7.

<!-- b002294 | prose | pages [20] -->
The results demonstrate that despite varying regression coefficients (βi), the adjusted contri- bution values across these cases converge to 1.7. This highlights the consistent and measurable impact of exceptional coaching on improving medal outcomes, offering actionable insights for strategic investments in coaching talent.

<!-- b002295 | caption | pages [20] -->
Figure 11: Caption for Britain

<!-- b002296 | caption | pages [20] -->
Figure 12: Caption for USA

<!-- b002297 | prose | pages [20] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002298 | caption | pages [20] -->
Figure 13: Caption for China

<!-- b002299 | prose | pages [20, 21] -->
关注数学模型 As shown in 11, 12 and 13, the medal count for the sport is analyzed around the appointment of a Great Coach. The red line marks the boundary: to the left are the medal counts before the coach’s appointment, and to the right, after the coach’s appointment until they left the country. The average number of medals post-appointment significantly exceeds pre-appointment counts, illustrating the “Great Coach Effect.”

<!-- b002300 | furniture | pages [20] -->
2

<!-- b002301 | furniture | pages [20] -->
MATHmodels

<!-- b002302 | furniture | pages [20] -->
获取更多资讯

<!-- b002303 | furniture | pages [21] -->
Team # 2503389

<!-- b002304 | furniture | pages [21] -->
Page 21 of 26

<!-- b002306 | heading | pages [21] -->
8.4.3 Reasons for Country and Sport Selection

<!-- b002307 | prose | pages [21] -->
The selection of three countries (China, UK, US) and three sports (Artistic Swimming, Cycling, Women’s Gymnastics) creates a framework to represent global sports. It looks at differences in political systems and types of athletics.

<!-- b002308 | prose | pages [21] -->
National Archetypes 微信公众号：数学模型

<!-- b002309 | prose | pages [21] -->
• China: Embodies state-centralized athleticism – a model prevalent in 37

<!-- b002310 | prose | pages [21] -->
– Top-down talent identification pipelines – Integrated sports-education-political apparatus – Cultural soft power through medal diplomacy

<!-- b002311 | prose | pages [21] -->
• United Kingdom: Represents technocratic hybrid systems adopted by 28% of developed nations (e.g., Germany, Japan). Defining features:

<!-- b002312 | prose | pages [21] -->
– Public-private R&D consortia (e.g., UK Sport’s “Marginal Gains” program) 微信号：MATHmodels – University-based athlete development ecosystems – Precision analytics in training optimization

<!-- b002313 | prose | pages [21] -->
• United States: Exemplifies market-driven pluralism dominant in 35% of Western democ- racies (e.g., Australia, Canada). Characteristics:

<!-- b002314 | prose | pages [21] -->
– Decentralized collegiate sports infrastructure – Commercial sponsorship-driven funding models – Individual athlete brand economies

<!-- b002315 | prose | pages [21] -->
Sport Typology Representation

<!-- b002316 | prose | pages [21] -->
• Artistic Swimming:

<!-- b002317 | prose | pages [21] -->
– Category: Judged team sport (22% of Olympic events) – Analysis Focus: Collective synchronization metrics, subjective scoring biases

<!-- b002318 | prose | pages [21] -->
• Cycling:

<!-- b002319 | prose | pages [21] -->
– Category: Technology-intensive endurance sport (18% of Olympic disciplines) – Analysis Focus: Equipment R&D ROI, aerodynamic efficiency thresholds

<!-- b002320 | prose | pages [21] -->
• Women’s Gymnastics:

<!-- b002321 | prose | pages [21] -->
– Category: Biomechanically complex skill sport (26% of Olympic events) – Analysis Focus: Rule change adaptation rates, injury risk management m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002322 | furniture | pages [21] -->
m

<!-- b002323 | furniture | pages [21] -->
m

<!-- b002324 | furniture | pages [21] -->
m

<!-- b002325 | furniture | pages [21] -->
m

<!-- b002326 | furniture | pages [21] -->
m

<!-- b002327 | furniture | pages [21] -->
m

<!-- b002328 | furniture | pages [21] -->
m

<!-- b002329 | furniture | pages [21] -->
m

<!-- b002330 | furniture | pages [21] -->
m

<!-- b002331 | furniture | pages [21] -->
m

<!-- b002332 | furniture | pages [21] -->
m

<!-- b002333 | furniture | pages [21] -->
m

<!-- b002334 | furniture | pages [21] -->
m

<!-- b002335 | furniture | pages [21] -->
m

<!-- b002336 | furniture | pages [21] -->
m

<!-- b002337 | furniture | pages [21] -->
m

<!-- b002338 | furniture | pages [21] -->
m

<!-- b002339 | furniture | pages [21] -->
m

<!-- b002340 | furniture | pages [21] -->
m

<!-- b002341 | furniture | pages [21] -->
m

<!-- b002342 | furniture | pages [21] -->
m

<!-- b002343 | furniture | pages [21] -->
m

<!-- b002344 | furniture | pages [21] -->
m

<!-- b002345 | furniture | pages [21] -->
m

<!-- b002346 | furniture | pages [21] -->
m

<!-- b002347 | furniture | pages [21] -->
m

<!-- b002348 | furniture | pages [21] -->
m

<!-- b002349 | furniture | pages [21] -->
m

<!-- b002350 | furniture | pages [21] -->
m

<!-- b002351 | furniture | pages [21] -->
m

<!-- b002352 | furniture | pages [21] -->
m

<!-- b002353 | furniture | pages [21] -->
m

<!-- b002354 | furniture | pages [21] -->
m

<!-- b002355 | furniture | pages [21] -->
m

<!-- b002356 | furniture | pages [21] -->
m

<!-- b002357 | furniture | pages [21] -->
m

<!-- b002358 | furniture | pages [21] -->
m

<!-- b002359 | furniture | pages [21] -->
m

<!-- b002360 | furniture | pages [21] -->
m

<!-- b002361 | furniture | pages [21] -->
m

<!-- b002362 | furniture | pages [21] -->
m

<!-- b002363 | furniture | pages [21] -->
m

<!-- b002364 | furniture | pages [21] -->
m

<!-- b002365 | furniture | pages [21] -->
m

<!-- b002366 | furniture | pages [21] -->
m

<!-- b002367 | furniture | pages [21] -->
m

<!-- b002368 | furniture | pages [21] -->
m

<!-- b002369 | furniture | pages [21] -->
m

<!-- b002370 | furniture | pages [21] -->
m

<!-- b002371 | furniture | pages [21] -->
m

<!-- b002372 | furniture | pages [21] -->
m

<!-- b002373 | furniture | pages [21] -->
m

<!-- b002374 | furniture | pages [21] -->
m

<!-- b002375 | furniture | pages [21] -->
m

<!-- b002376 | furniture | pages [21] -->
m

<!-- b002377 | furniture | pages [21] -->
m

<!-- b002378 | furniture | pages [21] -->
m

<!-- b002379 | furniture | pages [21] -->
m

<!-- b002380 | furniture | pages [21] -->
m

<!-- b002381 | furniture | pages [21] -->
m

<!-- b002382 | furniture | pages [21] -->
m

<!-- b002383 | furniture | pages [21] -->
m

<!-- b002384 | furniture | pages [21] -->
m

<!-- b002385 | furniture | pages [21] -->
m

<!-- b002386 | furniture | pages [21] -->
m

<!-- b002387 | furniture | pages [21] -->
m

<!-- b002388 | furniture | pages [21] -->
m

<!-- b002389 | furniture | pages [21] -->
m

<!-- b002390 | furniture | pages [21] -->
m

<!-- b002391 | furniture | pages [21] -->
m

<!-- b002392 | furniture | pages [21] -->
m

<!-- b002393 | furniture | pages [21] -->
m

<!-- b002394 | furniture | pages [21] -->
m

<!-- b002395 | furniture | pages [21] -->
m

<!-- b002396 | furniture | pages [21] -->
m

<!-- b002397 | furniture | pages [21] -->
m

<!-- b002398 | furniture | pages [21] -->
m

<!-- b002399 | furniture | pages [21] -->
m

<!-- b002400 | furniture | pages [21] -->
m

<!-- b002401 | furniture | pages [21] -->
m

<!-- b002402 | furniture | pages [21] -->
m

<!-- b002403 | furniture | pages [21] -->
m

<!-- b002404 | furniture | pages [21] -->
m

<!-- b002405 | furniture | pages [21] -->
m

<!-- b002406 | furniture | pages [21] -->
m

<!-- b002407 | furniture | pages [21] -->
m

<!-- b002408 | furniture | pages [21] -->
m

<!-- b002409 | furniture | pages [21] -->
m

<!-- b002410 | furniture | pages [21] -->
m

<!-- b002411 | furniture | pages [21] -->
m

<!-- b002412 | furniture | pages [21] -->
m

<!-- b002413 | furniture | pages [21] -->
m

<!-- b002414 | furniture | pages [21] -->
m

<!-- b002415 | furniture | pages [21] -->
m

<!-- b002416 | furniture | pages [21] -->
m

<!-- b002417 | furniture | pages [21] -->
m

<!-- b002418 | furniture | pages [21] -->
m

<!-- b002419 | furniture | pages [21] -->
m

<!-- b002420 | furniture | pages [21] -->
m

<!-- b002421 | furniture | pages [21] -->
m

<!-- b002422 | furniture | pages [21] -->
m

<!-- b002423 | furniture | pages [21] -->
m

<!-- b002424 | furniture | pages [21] -->
m

<!-- b002425 | furniture | pages [21] -->
m

<!-- b002426 | furniture | pages [21] -->
m

<!-- b002427 | furniture | pages [21] -->
m

<!-- b002428 | furniture | pages [21] -->
m

<!-- b002429 | furniture | pages [21] -->
m

<!-- b002430 | furniture | pages [21] -->
m

<!-- b002431 | furniture | pages [21] -->
m

<!-- b002432 | furniture | pages [21] -->
m

<!-- b002433 | furniture | pages [21] -->
m

<!-- b002434 | furniture | pages [21] -->
m

<!-- b002435 | furniture | pages [21] -->
m

<!-- b002436 | furniture | pages [21] -->
m

<!-- b002437 | furniture | pages [21] -->
m

<!-- b002438 | furniture | pages [21] -->
m

<!-- b002439 | furniture | pages [21] -->
m

<!-- b002440 | furniture | pages [21] -->
m

<!-- b002441 | furniture | pages [21] -->
m

<!-- b002442 | furniture | pages [21] -->
m

<!-- b002443 | furniture | pages [21] -->
m

<!-- b002444 | furniture | pages [21] -->
m

<!-- b002445 | furniture | pages [21] -->
m

<!-- b002446 | furniture | pages [21] -->
m

<!-- b002447 | furniture | pages [21] -->
m

<!-- b002448 | furniture | pages [21] -->
m

<!-- b002449 | furniture | pages [21] -->
m

<!-- b002450 | furniture | pages [21] -->
m

<!-- b002451 | furniture | pages [21] -->
m

<!-- b002452 | furniture | pages [21] -->
m

<!-- b002453 | furniture | pages [21] -->
m

<!-- b002454 | furniture | pages [21] -->
m

<!-- b002455 | furniture | pages [21] -->
m

<!-- b002456 | furniture | pages [21] -->
m

<!-- b002457 | furniture | pages [21] -->
m

<!-- b002458 | furniture | pages [21] -->
m

<!-- b002459 | furniture | pages [21] -->
m

<!-- b002460 | furniture | pages [21] -->
m

<!-- b002461 | furniture | pages [21] -->
m

<!-- b002462 | furniture | pages [21] -->
m

<!-- b002463 | furniture | pages [21] -->
m

<!-- b002464 | furniture | pages [21] -->
m

<!-- b002465 | furniture | pages [21] -->
m

<!-- b002466 | furniture | pages [21] -->
m

<!-- b002467 | furniture | pages [21] -->
m

<!-- b002468 | furniture | pages [21] -->
m

<!-- b002469 | furniture | pages [21] -->
m

<!-- b002470 | furniture | pages [21] -->
m

<!-- b002471 | furniture | pages [21] -->
m

<!-- b002472 | furniture | pages [21] -->
m

<!-- b002473 | furniture | pages [21] -->
m

<!-- b002474 | furniture | pages [21] -->
m

<!-- b002475 | furniture | pages [21] -->
m

<!-- b002476 | furniture | pages [21] -->
m

<!-- b002477 | furniture | pages [21] -->
m

<!-- b002478 | furniture | pages [21] -->
m

<!-- b002479 | furniture | pages [21] -->
m

<!-- b002480 | furniture | pages [21] -->
m

<!-- b002481 | furniture | pages [21] -->
m

<!-- b002482 | furniture | pages [21] -->
m

<!-- b002483 | furniture | pages [21] -->
m

<!-- b002484 | furniture | pages [21] -->
m

<!-- b002485 | furniture | pages [21] -->
m

<!-- b002486 | furniture | pages [21] -->
m

<!-- b002487 | furniture | pages [21] -->
m

<!-- b002488 | furniture | pages [21] -->
m

<!-- b002489 | furniture | pages [21] -->
m

<!-- b002490 | furniture | pages [21] -->
m

<!-- b002491 | furniture | pages [21] -->
m

<!-- b002492 | furniture | pages [21] -->
m

<!-- b002493 | furniture | pages [21] -->
m

<!-- b002494 | furniture | pages [21] -->
m

<!-- b002495 | furniture | pages [21] -->
m

<!-- b002496 | furniture | pages [21] -->
m

<!-- b002497 | furniture | pages [21] -->
m

<!-- b002498 | furniture | pages [21] -->
m

<!-- b002499 | furniture | pages [21] -->
m

<!-- b002500 | furniture | pages [21] -->
m

<!-- b002501 | furniture | pages [21] -->
m

<!-- b002502 | furniture | pages [21] -->
m

<!-- b002503 | furniture | pages [21] -->
m

<!-- b002504 | furniture | pages [21] -->
m

<!-- b002505 | furniture | pages [21] -->
m

<!-- b002506 | furniture | pages [21] -->
m

<!-- b002507 | furniture | pages [21] -->
m

<!-- b002508 | furniture | pages [21] -->
m

<!-- b002509 | furniture | pages [21] -->
m

<!-- b002510 | furniture | pages [21] -->
m

<!-- b002511 | furniture | pages [21] -->
m

<!-- b002512 | furniture | pages [21] -->
m

<!-- b002513 | furniture | pages [21] -->
m

<!-- b002514 | furniture | pages [21] -->
m

<!-- b002515 | furniture | pages [21] -->
m

<!-- b002516 | furniture | pages [21] -->
m

<!-- b002517 | furniture | pages [21] -->
m

<!-- b002518 | furniture | pages [21] -->
m

<!-- b002519 | furniture | pages [21] -->
m

<!-- b002520 | furniture | pages [21] -->
m

<!-- b002521 | furniture | pages [21] -->
m

<!-- b002522 | furniture | pages [21] -->
m

<!-- b002523 | furniture | pages [21] -->
m

<!-- b002524 | furniture | pages [21] -->
m

<!-- b002525 | furniture | pages [21] -->
m

<!-- b002526 | furniture | pages [21] -->
m

<!-- b002527 | furniture | pages [21] -->
m

<!-- b002528 | furniture | pages [21] -->
m

<!-- b002529 | furniture | pages [21] -->
m

<!-- b002530 | furniture | pages [21] -->
m

<!-- b002531 | furniture | pages [21] -->
m

<!-- b002532 | furniture | pages [21] -->
m

<!-- b002533 | furniture | pages [21] -->
m

<!-- b002534 | furniture | pages [21] -->
m

<!-- b002535 | furniture | pages [21] -->
m

<!-- b002536 | furniture | pages [21] -->
m

<!-- b002537 | furniture | pages [21] -->
m

<!-- b002538 | furniture | pages [21] -->
m

<!-- b002539 | furniture | pages [21] -->
m

<!-- b002540 | furniture | pages [21] -->
m

<!-- b002541 | furniture | pages [21] -->
m

<!-- b002542 | furniture | pages [21] -->
m

<!-- b002543 | furniture | pages [21] -->
m

<!-- b002544 | furniture | pages [21] -->
m

<!-- b002545 | furniture | pages [21] -->
m

<!-- b002546 | furniture | pages [21] -->
m

<!-- b002547 | furniture | pages [21] -->
m

<!-- b002548 | furniture | pages [21] -->
m

<!-- b002549 | furniture | pages [21] -->
m

<!-- b002550 | furniture | pages [21] -->
m

<!-- b002551 | furniture | pages [21] -->
m

<!-- b002552 | furniture | pages [21] -->
m

<!-- b002553 | furniture | pages [21] -->
m

<!-- b002554 | furniture | pages [21] -->
m

<!-- b002555 | furniture | pages [21] -->
m

<!-- b002556 | furniture | pages [21] -->
m

<!-- b002557 | furniture | pages [21] -->
m

<!-- b002558 | furniture | pages [21] -->
m

<!-- b002559 | furniture | pages [21] -->
m

<!-- b002560 | furniture | pages [21] -->
m

<!-- b002561 | furniture | pages [21] -->
m

<!-- b002562 | furniture | pages [21] -->
m

<!-- b002563 | furniture | pages [21] -->
m

<!-- b002564 | furniture | pages [21] -->
m

<!-- b002565 | furniture | pages [21] -->
m

<!-- b002566 | furniture | pages [21] -->
m

<!-- b002567 | furniture | pages [21] -->
m

<!-- b002568 | furniture | pages [21] -->
m

<!-- b002569 | furniture | pages [21] -->
m

<!-- b002570 | furniture | pages [21] -->
m

<!-- b002571 | furniture | pages [21] -->
m

<!-- b002572 | furniture | pages [21] -->
m

<!-- b002573 | furniture | pages [21] -->
m

<!-- b002574 | furniture | pages [21] -->
m

<!-- b002575 | furniture | pages [21] -->
m

<!-- b002576 | furniture | pages [21] -->
m

<!-- b002577 | furniture | pages [21] -->
m

<!-- b002578 | furniture | pages [21] -->
m

<!-- b002579 | furniture | pages [21] -->
m

<!-- b002580 | furniture | pages [21] -->
m

<!-- b002581 | furniture | pages [21] -->
m

<!-- b002582 | furniture | pages [21] -->
m

<!-- b002583 | furniture | pages [21] -->
m

<!-- b002584 | furniture | pages [21] -->
m

<!-- b002585 | furniture | pages [21] -->
m

<!-- b002586 | furniture | pages [21] -->
m

<!-- b002587 | furniture | pages [21] -->
m

<!-- b002588 | furniture | pages [21] -->
m

<!-- b002589 | furniture | pages [21] -->
m

<!-- b002590 | furniture | pages [21] -->
m

<!-- b002591 | furniture | pages [21] -->
m

<!-- b002592 | furniture | pages [21] -->
m

<!-- b002593 | furniture | pages [21] -->
m

<!-- b002594 | furniture | pages [21] -->
m

<!-- b002595 | furniture | pages [21] -->
m

<!-- b002596 | furniture | pages [21] -->
m

<!-- b002597 | furniture | pages [21] -->
m

<!-- b002598 | furniture | pages [21] -->
m

<!-- b002599 | furniture | pages [21] -->
m

<!-- b002600 | furniture | pages [21] -->
m

<!-- b002601 | furniture | pages [21] -->
m

<!-- b002602 | furniture | pages [21] -->
m

<!-- b002603 | furniture | pages [21] -->
m

<!-- b002604 | furniture | pages [21] -->
m

<!-- b002605 | furniture | pages [21] -->
m

<!-- b002606 | furniture | pages [21] -->
m

<!-- b002607 | furniture | pages [21] -->
m

<!-- b002608 | furniture | pages [21] -->
m

<!-- b002609 | furniture | pages [21] -->
m

<!-- b002610 | furniture | pages [21] -->
m

<!-- b002611 | furniture | pages [21] -->
m

<!-- b002612 | furniture | pages [21] -->
m

<!-- b002613 | furniture | pages [21] -->
m

<!-- b002614 | furniture | pages [21] -->
m

<!-- b002615 | furniture | pages [21] -->
m

<!-- b002616 | furniture | pages [21] -->
m

<!-- b002617 | furniture | pages [21] -->
m

<!-- b002618 | furniture | pages [21] -->
m

<!-- b002619 | furniture | pages [21] -->
m

<!-- b002620 | furniture | pages [21] -->
m

<!-- b002621 | furniture | pages [21] -->
m

<!-- b002622 | furniture | pages [21] -->
m

<!-- b002623 | furniture | pages [21] -->
m

<!-- b002624 | furniture | pages [21] -->
m

<!-- b002625 | furniture | pages [21] -->
m

<!-- b002626 | furniture | pages [21] -->
m

<!-- b002627 | furniture | pages [21] -->
m

<!-- b002628 | furniture | pages [21] -->
m

<!-- b002629 | furniture | pages [21] -->
m

<!-- b002630 | furniture | pages [21] -->
m

<!-- b002631 | furniture | pages [21] -->
m

<!-- b002632 | furniture | pages [21] -->
m

<!-- b002633 | furniture | pages [21] -->
m

<!-- b002634 | furniture | pages [21] -->
m

<!-- b002635 | furniture | pages [21] -->
m

<!-- b002636 | furniture | pages [21] -->
m

<!-- b002637 | furniture | pages [21] -->
m

<!-- b002638 | furniture | pages [21] -->
m

<!-- b002639 | furniture | pages [21] -->
m

<!-- b002640 | furniture | pages [21] -->
m

<!-- b002641 | furniture | pages [21] -->
m

<!-- b002642 | furniture | pages [21] -->
m

<!-- b002643 | furniture | pages [21] -->
m

<!-- b002644 | furniture | pages [21] -->
m

<!-- b002645 | furniture | pages [21] -->
m

<!-- b002646 | furniture | pages [22] -->
Team # 2503389

<!-- b002647 | furniture | pages [22] -->
Page 22 of 26

<!-- b002648 | heading | pages [22] -->
9 The Practical Application of the ”Great Coach” Effect

<!-- b002649 | heading | pages [22] -->
9.1 Selection of Sports Needing a Great Coach

<!-- b002650 | heading | pages [22] -->
9.1.1 Data Utilization

<!-- b002651 | prose | pages [22] -->
1. Aggregate the Score data from 2016 and 2020, calculating the mean and standard devia- tion for each year.

<!-- b002652 | prose | pages [22] -->
2. Select the 20th percentile, with a threshold of 0.15.

<!-- b002653 | prose | pages [22] -->
3. Check the proportion of sports in the distribution with scores close to 0.15 to ensure it aligns with actual observations.

<!-- b002654 | prose | pages [22] -->
Selection Criteria:

<!-- b002655 | prose | pages [22] -->
• A sport’s Score in both 2016 and 2020 must be greater than 0.15.

<!-- b002656 | prose | pages [22] -->
• The Score for 2024 must be less than 0.15.

<!-- b002657 | heading | pages [22] -->
9.2 Results

<!-- b002658 | prose | pages [22] -->
After the preliminary screening, Nigeria, Poland, and India were selected as the countries of interest. According to the above criteria, the sports that require the introduction of a Great Coach were selected. The final list of potential sports for a Great Coach includes:

<!-- b002659 | prose | pages [22] -->
• Poland: Athletics, Canoe Sprint, Sailing

<!-- b002660 | prose | pages [22] -->
• Nigeria: Football

<!-- b002661 | prose | pages [22] -->
• India: Badminton, Weightlifting, Wrestling

<!-- b002662 | heading | pages [22] -->
9.2.1 Validation of the Conclusion: Coach’s Impact Calculation

<!-- b002663 | prose | pages [22] -->
From Section 2.1, it is determined that the contribution rate of the coach to the sport is u = 1.7. This means that after introducing the coach, the Score for 2024 increases by u× the pre-coaching Score. By comparing the results, we find that the likelihood of winning medals in these sports for the selected countries has increased after the introduction of the coach.

<!-- b002664 | heading | pages [22] -->
10 Other Insights: Host Country Spillover Effect on Medal

<!-- b002665 | prose | pages [22] -->
Rates of Neighboring Countries

<!-- b002666 | heading | pages [22] -->
10.1 Analysis and Results

<!-- b002667 | prose | pages [22] -->
We analyzed the medal rates of various countries in the 2016, 2020, and 2024 Olympic Games, focusing on the differences in medal rates for neighboring countries of the host na- tion (land-bordering countries). Specifically, we compared the medal rate of these neighboring countries in the current Olympics to the average medal rate from the previous two Olympic Games. We identified countries with a positive difference in medal rates and mapped these im- provements. The results from these maps 17 clearly demonstrate that the ”Host Country Effect”

<!-- b002668 | prose | pages [22, 23] -->
关注数学模型 not only boosts the medal rate of the host country but also positively impacts the medal rates of neighboring countries.

<!-- b002669 | furniture | pages [22] -->
2

<!-- b002670 | furniture | pages [22] -->
MATHmodels

<!-- b002671 | furniture | pages [22] -->
获取更多资讯

<!-- b002672 | furniture | pages [23] -->
Team# 2503389

<!-- b002673 | furniture | pages [23] -->
Page 23 of 26

<!-- b002675 | prose | pages [23] -->
Increase 0.024714974 0.00399071

<!-- b002676 | prose | pages [23] -->
0.000498065

<!-- b002677 | caption | pages [23] -->
Figure 16: Spillover Effect

<!-- b002678 | caption | pages [23] -->
Figure 15: Spillover Effect

<!-- b002679 | prose | pages [23] -->
around Japan

<!-- b002680 | caption | pages [23] -->
Figure 14: Spillover Effect

<!-- b002681 | prose | pages [23] -->
around Brazil around France

<!-- b002682 | caption | pages [23] -->
Figure 17: Spillover Effect

<!-- b002683 | prose | pages [23] -->
Our analysis confirms that the "Host Country Effect" contributes to an increase in the medal rates of neighboring countries.

<!-- b002684 | prose | pages [23] -->
10.2

<!-- b002685 | heading | pages [23] -->
Strategic Recommendation for National Olympic Committees

<!-- b002686 | prose | pages [23] -->
dels

<!-- b002687 | heading | pages [23] -->
10.2.1 Pre-Games Optimization Plan

<!-- b002688 | prose | pages [23] -->
● ● · Phase-Based Adaptation Training:

<!-- b002689 | heading | pages [23] -->
1. Phase 1 (12 months before competition): Simulate host city altitude and climate.

<!-- b002690 | heading | pages [23] -->
2. Phase 2 (6 months before competition): Practice at official venues.

<!-- b002691 | prose | pages [23] -->
• Cross-Border Training Clusters:

<!-- b002692 | prose | pages [23] -->
– Set up joint training centers for athletes within 500 km of the host city.

<!-- b002693 | prose | pages [23] -->
– Share the host country's anti-doping labs and rehabilitation facilities.

<!-- b002694 | heading | pages [23] -->
11 Sensitivity Analysis

<!-- b002695 | prose | pages [23] -->
In Task 1.1, we analyzed four key features: Host Boost (XHost), Athlete Pool (XAth), Compet- itiveness Index (XComp), and Historical Momentum (XHist). Since XHost is a binary variable (0 or 1), it was fixed at XHost = 1 (host scenario) for sensitivity analysis. The remaining features were varied by ±10% from their initial values to evaluate their impact on the model's predictions.

<!-- b002696 | heading | pages [23] -->
Initial Feature Values and Sensitivity Ranges

<!-- b002697 | prose | pages [23] -->
The initial values and sensitivity ranges for each feature are listed below:

<!-- b002698 | caption | pages [23] -->
Table 11: Initial Values and Sensitivity Ranges

<!-- b002699 | prose | pages [23] -->
Feature Initial Value Range (-10%) Range (+10%) 719 647 Athlete Pool (XAth) 791 Competitiveness Index (XComp) 17.85 16.07 19.64 Historical Momentum (XHist) 121 109 133

<!-- b002700 | furniture | pages [24] -->
Team # 2503389

<!-- b002701 | furniture | pages [24] -->
Page 24 of 26

<!-- b002702 | heading | pages [24] -->
Results and Observations

<!-- b002703 | caption | pages [24] -->
Figure 18: Impact of His-

<!-- b002704 | caption | pages [24] -->
Figure 20: Impact of Com-

<!-- b002705 | caption | pages [24] -->
Figure 19: Impact of Ath-

<!-- b002706 | prose | pages [24] -->
torical Momentum on Pre- petitiveness Index on Pre- letes on Predicted Medals dicted Medals dicted Medals

<!-- b002707 | prose | pages [24] -->
All three factors features are positively correlated with predicted medals. The slope of the regression lines shows a steady increase in medals as each factor rises. The shaded areas indicate potential fluctuations in predictions, providing insights into the model’s accuracy and reliability.

<!-- b002708 | heading | pages [24] -->
12 Strengths and Weaknesses

<!-- b002709 | heading | pages [24] -->
Strengths

<!-- b002710 | prose | pages [24] -->
• Comprehensive Feature Integration (MLR-FNN): The MLR-FNN model combines feature extraction and relationship learning to predict the 2028 medal table. It includes factors like participant numbers, host nation effects, historical medal counts, and compet- itiveness, providing strong predictions with confidence intervals that reflect real-world situations.

<!-- b002711 | prose | pages [24] -->
• Balanced Interpretability and Complexity (LR-RF): The LR-RF model mixes logistic regression’s clear results with random forest’s ability to handle complex relationships and rank factors. This makes it a powerful tool for analyzing Olympic data.

<!-- b002712 | prose | pages [24] -->
• Strategic Sports Evaluation (SIAMOS): The SIAMOS model looks at sports’ impor- tance using four factors: National Medal Proportion (NMP), Global Competitive Pro- portion (GCP), Long-term Achievement Stability (LAS), and Athlete Sport Distribution (ASD). It gives useful insights to help focus resources and improve Olympic performance.

<!-- b002713 | prose | pages [24] -->
• Causal Analysis of Coaching Impact (RDD): The regression discontinuity model mea- sures the “great coach effect” by looking at natural breaks in data and considering cross- country and time changes. It provides clear advice on how to invest in coaching to improve medal results.

<!-- b002714 | heading | pages [24] -->
Weaknesses

<!-- b002715 | prose | pages [24] -->
• Limited Feature Scope: Some models, like the MLR-FNN, do not include important factors such as the Host Country Spillover Effect, limiting the analysis.

<!-- b002716 | prose | pages [24] -->
• Subjective Design Choices: Some formulas were chosen without calculation, making the model more subjective and possibly less generalizable. For example, it is assumed that the performance of new athletes is the same as athletes who no longer compete. This keeps the number and composition of athletes the same.

<!-- b002717 | prose | pages [24] -->
关注数学模型

<!-- b002718 | furniture | pages [24] -->
2

<!-- b002719 | furniture | pages [24] -->
MATHmodels

<!-- b002720 | furniture | pages [24] -->
获取更多资讯

<!-- b002721 | furniture | pages [25] -->
Team # 2503389

<!-- b002722 | furniture | pages [25] -->
Page 25 of 26

<!-- b002723 | heading | pages [25] -->
References

<!-- b002724 | references | pages [25] -->
[1] International Olympic Committee, National Olympic Committees, https://www.olympics.

<!-- b002725 | references | pages [25] -->
com/ioc/national-olympic-committees?os=__&ref=app, accessed 27 Jan. 2025.

<!-- b002726 | references | pages [25] -->
[2] Mancini, Simona, and Triki, [First Name]. ”Optimal Selection of Touristic Packages Based

<!-- b002727 | references | pages [25] -->
微信公众号：数学模型

<!-- b002728 | references | pages [25] -->
on User Preferences During Sports Mega-Events.” European Journal of Operational Re-

<!-- b002729 | references | pages [25] -->
search, vol. 302, no. 3, Nov. 2022, pp. 819-830.

<!-- b002730 | references | pages [25] -->
[3] Bernard, A. B., and Busse, M. R. (2004). ”Who Wins the Olympic Games: Economic

<!-- b002731 | references | pages [25] -->
Resources and Medal Totals.” Review of Economics and Statistics, vol. 86, no. 1, pp. 413–

<!-- b002732 | references | pages [25] -->
417. https://doi.org/10.1162/003465304774201824.

<!-- b002733 | references | pages [25] -->
[4] Jay Belanger, William P. Fox, Wang Jie Mao, and Zi Yang. (2017). Correct Writing for the

<!-- b002734 | references | pages [25] -->
Mathematical Contest in Modeling (MCM). Higher Education Press.

<!-- b002735 | references | pages [25] -->
[5] Olympics. (2024). ”2024 Paris Olympic Games Artistic Swimming: Chinese Team Sets

<!-- b002736 | references | pages [25] -->
微信号：MATHmodels

<!-- b002737 | references | pages [25] -->
New Historical High in Team Free Routine.” Retrieved from https://www.olympics.com/

<!-- b002738 | references | pages [25] -->
zh/news/paris-2024-results-artistic-swimming-team-free-routine-wrap-up.

<!-- b002739 | references | pages [25] -->
[6] Way We Do. (2024). ”The Marginal Gains Strategy: British Cycling’s Road to Victory.”

<!-- b002740 | references | pages [25] -->
Retrieved from https://www.waywedo.com/blog/marginal-gains-strategy/.

<!-- b002741 | references | pages [25] -->
[7] Wikipedia. (2024). ”Béla Károlyi.” Retrieved from https://en.wikipedia.org/wiki/B%C3%

<!-- b002742 | references | pages [25] -->
A9la_K%C3%A1rolyi.

<!-- b002743 | references | pages [25] -->
m

<!-- b002744 | references | pages [25] -->
m

<!-- b002745 | references | pages [25] -->
m

<!-- b002746 | references | pages [25] -->
m

<!-- b002747 | references | pages [25] -->
m

<!-- b002748 | references | pages [25] -->
m

<!-- b002749 | references | pages [25] -->
m

<!-- b002750 | references | pages [25] -->
m

<!-- b002751 | references | pages [25] -->
m

<!-- b002752 | references | pages [25] -->
m

<!-- b002753 | references | pages [25] -->
m

<!-- b002754 | references | pages [25] -->
m

<!-- b002755 | references | pages [25] -->
m

<!-- b002756 | references | pages [25] -->
m

<!-- b002757 | references | pages [25] -->
m

<!-- b002758 | references | pages [25] -->
m

<!-- b002759 | references | pages [25] -->
m

<!-- b002760 | references | pages [25] -->
m

<!-- b002761 | references | pages [25] -->
m

<!-- b002762 | references | pages [25] -->
m

<!-- b002763 | references | pages [25] -->
m

<!-- b002764 | references | pages [25] -->
m

<!-- b002765 | references | pages [25] -->
m

<!-- b002766 | references | pages [25] -->
m

<!-- b002767 | references | pages [25] -->
m

<!-- b002768 | references | pages [25] -->
m

<!-- b002769 | references | pages [25] -->
m

<!-- b002770 | references | pages [25] -->
m

<!-- b002771 | references | pages [25] -->
m

<!-- b002772 | references | pages [25] -->
m

<!-- b002773 | references | pages [25] -->
m

<!-- b002774 | references | pages [25] -->
m

<!-- b002775 | references | pages [25] -->
m

<!-- b002776 | references | pages [25] -->
m

<!-- b002777 | references | pages [25] -->
m

<!-- b002778 | references | pages [25] -->
m

<!-- b002779 | references | pages [25] -->
m

<!-- b002780 | references | pages [25] -->
m

<!-- b002781 | references | pages [25] -->
m

<!-- b002782 | references | pages [25] -->
m

<!-- b002783 | references | pages [25] -->
m

<!-- b002784 | references | pages [25] -->
m

<!-- b002785 | references | pages [25] -->
m

<!-- b002786 | references | pages [25] -->
m

<!-- b002787 | references | pages [25] -->
m

<!-- b002788 | references | pages [25] -->
m

<!-- b002789 | references | pages [25] -->
m

<!-- b002790 | references | pages [25] -->
m

<!-- b002791 | references | pages [25] -->
m

<!-- b002792 | references | pages [25] -->
m

<!-- b002793 | references | pages [25] -->
m

<!-- b002794 | references | pages [25] -->
m

<!-- b002795 | references | pages [25] -->
m

<!-- b002796 | references | pages [25] -->
m

<!-- b002797 | references | pages [25] -->
m

<!-- b002798 | references | pages [25] -->
m

<!-- b002799 | references | pages [25] -->
m

<!-- b002800 | references | pages [25] -->
m

<!-- b002801 | references | pages [25] -->
m

<!-- b002802 | references | pages [25] -->
m

<!-- b002803 | references | pages [25] -->
m

<!-- b002804 | references | pages [25] -->
m

<!-- b002805 | references | pages [25] -->
m

<!-- b002806 | references | pages [25] -->
m

<!-- b002807 | references | pages [25] -->
m

<!-- b002808 | references | pages [25] -->
m

<!-- b002809 | references | pages [25] -->
m

<!-- b002810 | references | pages [25] -->
m

<!-- b002811 | references | pages [25] -->
m

<!-- b002812 | references | pages [25] -->
m

<!-- b002813 | references | pages [25] -->
m

<!-- b002814 | references | pages [25] -->
m

<!-- b002815 | references | pages [25] -->
m

<!-- b002816 | references | pages [25] -->
m

<!-- b002817 | references | pages [25] -->
m

<!-- b002818 | references | pages [25] -->
m

<!-- b002819 | references | pages [25] -->
m

<!-- b002820 | references | pages [25] -->
m

<!-- b002821 | references | pages [25] -->
m

<!-- b002822 | references | pages [25] -->
m

<!-- b002823 | references | pages [25] -->
m

<!-- b002824 | references | pages [25] -->
m

<!-- b002825 | references | pages [25] -->
m

<!-- b002826 | references | pages [25] -->
m

<!-- b002827 | references | pages [25] -->
m

<!-- b002828 | references | pages [25] -->
m

<!-- b002829 | references | pages [25] -->
m

<!-- b002830 | references | pages [25] -->
m

<!-- b002831 | references | pages [25] -->
m

<!-- b002832 | references | pages [25] -->
m

<!-- b002833 | references | pages [25] -->
m

<!-- b002834 | references | pages [25] -->
m

<!-- b002835 | references | pages [25] -->
m

<!-- b002836 | references | pages [25] -->
m

<!-- b002837 | references | pages [25] -->
m

<!-- b002838 | references | pages [25] -->
m

<!-- b002839 | references | pages [25] -->
m

<!-- b002840 | references | pages [25] -->
m

<!-- b002841 | references | pages [25] -->
m

<!-- b002842 | references | pages [25] -->
m

<!-- b002843 | references | pages [25] -->
m

<!-- b002844 | references | pages [25] -->
m

<!-- b002845 | references | pages [25] -->
m

<!-- b002846 | references | pages [25] -->
m

<!-- b002847 | references | pages [25] -->
m

<!-- b002848 | references | pages [25] -->
m

<!-- b002849 | references | pages [25] -->
m

<!-- b002850 | references | pages [25] -->
m

<!-- b002851 | references | pages [25] -->
m

<!-- b002852 | references | pages [25] -->
m

<!-- b002853 | references | pages [25] -->
m

<!-- b002854 | references | pages [25] -->
m

<!-- b002855 | references | pages [25] -->
m

<!-- b002856 | references | pages [25] -->
m

<!-- b002857 | references | pages [25] -->
m

<!-- b002858 | references | pages [25] -->
m

<!-- b002859 | references | pages [25] -->
m

<!-- b002860 | references | pages [25] -->
m

<!-- b002861 | references | pages [25] -->
m

<!-- b002862 | references | pages [25] -->
m

<!-- b002863 | references | pages [25] -->
m

<!-- b002864 | references | pages [25] -->
m

<!-- b002865 | references | pages [25] -->
m

<!-- b002866 | references | pages [25] -->
m

<!-- b002867 | references | pages [25] -->
m

<!-- b002868 | references | pages [25] -->
m

<!-- b002869 | references | pages [25] -->
m

<!-- b002870 | references | pages [25] -->
m

<!-- b002871 | references | pages [25] -->
m

<!-- b002872 | references | pages [25] -->
m

<!-- b002873 | references | pages [25] -->
m

<!-- b002874 | references | pages [25] -->
m

<!-- b002875 | references | pages [25] -->
m

<!-- b002876 | references | pages [25] -->
m

<!-- b002877 | references | pages [25] -->
m

<!-- b002878 | references | pages [25] -->
m

<!-- b002879 | references | pages [25] -->
m

<!-- b002880 | references | pages [25] -->
m

<!-- b002881 | references | pages [25] -->
m

<!-- b002882 | references | pages [25] -->
m

<!-- b002883 | references | pages [25] -->
m

<!-- b002884 | references | pages [25] -->
m

<!-- b002885 | references | pages [25] -->
m

<!-- b002886 | references | pages [25] -->
m

<!-- b002887 | references | pages [25] -->
m

<!-- b002888 | references | pages [25] -->
m

<!-- b002889 | references | pages [25] -->
m

<!-- b002890 | references | pages [25] -->
m

<!-- b002891 | references | pages [25] -->
m

<!-- b002892 | references | pages [25] -->
m

<!-- b002893 | references | pages [25] -->
m

<!-- b002894 | references | pages [25] -->
m

<!-- b002895 | references | pages [25] -->
m

<!-- b002896 | references | pages [25] -->
m

<!-- b002897 | references | pages [25] -->
m

<!-- b002898 | references | pages [25] -->
m

<!-- b002899 | references | pages [25] -->
m

<!-- b002900 | references | pages [25] -->
m

<!-- b002901 | references | pages [25] -->
m

<!-- b002902 | references | pages [25] -->
m

<!-- b002903 | references | pages [25] -->
m

<!-- b002904 | references | pages [25] -->
m

<!-- b002905 | references | pages [25] -->
m

<!-- b002906 | references | pages [25] -->
m

<!-- b002907 | references | pages [25] -->
m

<!-- b002908 | references | pages [25] -->
m

<!-- b002909 | references | pages [25] -->
m

<!-- b002910 | references | pages [25] -->
m

<!-- b002911 | references | pages [25] -->
m

<!-- b002912 | references | pages [25] -->
m

<!-- b002913 | references | pages [25] -->
m

<!-- b002914 | references | pages [25] -->
m

<!-- b002915 | references | pages [25] -->
m

<!-- b002916 | references | pages [25] -->
m

<!-- b002917 | references | pages [25] -->
m

<!-- b002918 | references | pages [25] -->
m

<!-- b002919 | references | pages [25] -->
m

<!-- b002920 | references | pages [25] -->
m

<!-- b002921 | references | pages [25] -->
m

<!-- b002922 | references | pages [25] -->
m

<!-- b002923 | references | pages [25] -->
m

<!-- b002924 | references | pages [25] -->
m

<!-- b002925 | references | pages [25] -->
m

<!-- b002926 | references | pages [25] -->
m

<!-- b002927 | references | pages [25] -->
m

<!-- b002928 | references | pages [25] -->
m

<!-- b002929 | references | pages [25] -->
m

<!-- b002930 | references | pages [25] -->
m

<!-- b002931 | references | pages [25] -->
m

<!-- b002932 | references | pages [25] -->
m

<!-- b002933 | references | pages [25] -->
m

<!-- b002934 | references | pages [25] -->
m

<!-- b002935 | references | pages [25] -->
m

<!-- b002936 | references | pages [25] -->
m

<!-- b002937 | references | pages [25] -->
m

<!-- b002938 | references | pages [25] -->
m

<!-- b002939 | references | pages [25] -->
m

<!-- b002940 | references | pages [25] -->
m

<!-- b002941 | references | pages [25] -->
m

<!-- b002942 | references | pages [25] -->
m

<!-- b002943 | references | pages [25] -->
m

<!-- b002944 | references | pages [25] -->
m

<!-- b002945 | references | pages [25] -->
m

<!-- b002946 | references | pages [25] -->
m

<!-- b002947 | references | pages [25] -->
m

<!-- b002948 | references | pages [25] -->
m

<!-- b002949 | references | pages [25] -->
m

<!-- b002950 | references | pages [25] -->
m

<!-- b002951 | references | pages [25] -->
m

<!-- b002952 | references | pages [25] -->
m

<!-- b002953 | references | pages [25] -->
m

<!-- b002954 | references | pages [25] -->
m

<!-- b002955 | references | pages [25] -->
m

<!-- b002956 | references | pages [25] -->
m

<!-- b002957 | references | pages [25] -->
m

<!-- b002958 | references | pages [25] -->
m

<!-- b002959 | references | pages [25] -->
m

<!-- b002960 | references | pages [25] -->
m

<!-- b002961 | references | pages [25] -->
m

<!-- b002962 | references | pages [25] -->
m

<!-- b002963 | references | pages [25] -->
m

<!-- b002964 | references | pages [25] -->
m

<!-- b002965 | references | pages [25] -->
m

<!-- b002966 | references | pages [25] -->
m

<!-- b002967 | references | pages [25] -->
m

<!-- b002968 | references | pages [25] -->
m

<!-- b002969 | references | pages [25] -->
m

<!-- b002970 | references | pages [25] -->
m

<!-- b002971 | references | pages [25] -->
m

<!-- b002972 | references | pages [25] -->
m

<!-- b002973 | furniture | pages [25] -->
m

<!-- b002974 | furniture | pages [25] -->
m

<!-- b002975 | furniture | pages [25] -->
m

<!-- b002976 | furniture | pages [25] -->
m

<!-- b002977 | furniture | pages [25] -->
m

<!-- b002978 | furniture | pages [25] -->
m

<!-- b002979 | furniture | pages [25] -->
m

<!-- b002980 | furniture | pages [25] -->
m

<!-- b002981 | furniture | pages [25] -->
m

<!-- b002982 | furniture | pages [25] -->
m

<!-- b002983 | furniture | pages [25] -->
m

<!-- b002984 | furniture | pages [25] -->
m

<!-- b002985 | furniture | pages [25] -->
m

<!-- b002986 | furniture | pages [25] -->
m

<!-- b002987 | furniture | pages [25] -->
m

<!-- b002988 | furniture | pages [25] -->
m

<!-- b002989 | furniture | pages [25] -->
m

<!-- b002990 | furniture | pages [25] -->
m

<!-- b002991 | furniture | pages [25] -->
m

<!-- b002992 | furniture | pages [25] -->
m

<!-- b002993 | furniture | pages [25] -->
m

<!-- b002994 | furniture | pages [25] -->
m

<!-- b002995 | furniture | pages [25] -->
m

<!-- b002996 | furniture | pages [25] -->
m

<!-- b002997 | furniture | pages [25] -->
m

<!-- b002998 | furniture | pages [25] -->
m

<!-- b002999 | furniture | pages [25] -->
m

<!-- b003000 | furniture | pages [25] -->
m

<!-- b003001 | furniture | pages [25] -->
m

<!-- b003002 | furniture | pages [25] -->
m

<!-- b003003 | furniture | pages [25] -->
m

<!-- b003004 | furniture | pages [25] -->
m

<!-- b003005 | furniture | pages [25] -->
m

<!-- b003006 | furniture | pages [25] -->
m

<!-- b003007 | furniture | pages [25] -->
m

<!-- b003008 | furniture | pages [25] -->
m

<!-- b003009 | furniture | pages [25] -->
m

<!-- b003010 | furniture | pages [25] -->
m

<!-- b003011 | furniture | pages [25] -->
m

<!-- b003012 | furniture | pages [25] -->
m

<!-- b003013 | furniture | pages [25] -->
m

<!-- b003014 | furniture | pages [25] -->
m

<!-- b003015 | furniture | pages [25] -->
m

<!-- b003016 | furniture | pages [25] -->
m

<!-- b003017 | furniture | pages [25] -->
m

<!-- b003018 | furniture | pages [25] -->
m

<!-- b003019 | furniture | pages [25] -->
m

<!-- b003020 | furniture | pages [25] -->
m

<!-- b003021 | furniture | pages [25] -->
m

<!-- b003022 | furniture | pages [25] -->
m

<!-- b003023 | furniture | pages [25] -->
m

<!-- b003024 | furniture | pages [25] -->
m

<!-- b003025 | furniture | pages [25] -->
m

<!-- b003026 | furniture | pages [25] -->
m

<!-- b003027 | furniture | pages [25] -->
m

<!-- b003028 | furniture | pages [25] -->
m

<!-- b003029 | furniture | pages [25] -->
m

<!-- b003030 | furniture | pages [25] -->
m

<!-- b003031 | furniture | pages [25] -->
m

<!-- b003032 | furniture | pages [25] -->
m

<!-- b003033 | furniture | pages [25] -->
m

<!-- b003034 | furniture | pages [25] -->
m

<!-- b003035 | furniture | pages [25] -->
m

<!-- b003036 | furniture | pages [25] -->
m

<!-- b003037 | furniture | pages [25] -->
m

<!-- b003038 | furniture | pages [25] -->
m

<!-- b003039 | furniture | pages [25] -->
m

<!-- b003040 | furniture | pages [25] -->
m

<!-- b003041 | furniture | pages [25] -->
m

<!-- b003042 | furniture | pages [25] -->
m

<!-- b003043 | furniture | pages [25] -->
m

<!-- b003044 | furniture | pages [25] -->
m

<!-- b003045 | furniture | pages [25] -->
m

<!-- b003046 | furniture | pages [25] -->
m

<!-- b003047 | furniture | pages [25] -->
m

<!-- b003048 | furniture | pages [25] -->
m

<!-- b003049 | furniture | pages [25] -->
m

<!-- b003050 | furniture | pages [25] -->
m

<!-- b003051 | furniture | pages [25] -->
m

<!-- b003052 | furniture | pages [25] -->
m

<!-- b003053 | furniture | pages [25] -->
m

<!-- b003054 | furniture | pages [25] -->
m

<!-- b003055 | furniture | pages [25] -->
m

<!-- b003056 | furniture | pages [25] -->
m

<!-- b003057 | furniture | pages [25] -->
m

<!-- b003058 | furniture | pages [25] -->
m

<!-- b003059 | furniture | pages [25] -->
m

<!-- b003060 | furniture | pages [25] -->
m

<!-- b003061 | furniture | pages [25] -->
m

<!-- b003062 | furniture | pages [25] -->
m

<!-- b003063 | furniture | pages [25] -->
m

<!-- b003064 | furniture | pages [25] -->
m

<!-- b003065 | furniture | pages [25] -->
m

<!-- b003066 | furniture | pages [25] -->
m

<!-- b003067 | furniture | pages [25] -->
m

<!-- b003068 | furniture | pages [25] -->
m

<!-- b003069 | furniture | pages [25] -->
m

<!-- b003070 | furniture | pages [25] -->
m

<!-- b003071 | furniture | pages [25] -->
m

<!-- b003072 | furniture | pages [25] -->
m

<!-- b003073 | furniture | pages [25] -->
m

<!-- b003074 | furniture | pages [25] -->
m

<!-- b003075 | furniture | pages [25] -->
m

<!-- b003076 | furniture | pages [25] -->
m

<!-- b003077 | furniture | pages [25] -->
m

<!-- b003078 | furniture | pages [25] -->
m

<!-- b003079 | furniture | pages [25] -->
m

<!-- b003080 | furniture | pages [25] -->
m

<!-- b003081 | furniture | pages [25] -->
m

<!-- b003082 | furniture | pages [25] -->
m

<!-- b003083 | furniture | pages [25] -->
m

<!-- b003084 | furniture | pages [25] -->
m

<!-- b003085 | furniture | pages [25] -->
m

<!-- b003086 | furniture | pages [25] -->
m

<!-- b003087 | furniture | pages [25] -->
m

<!-- b003088 | furniture | pages [25] -->
m

<!-- b003089 | furniture | pages [25] -->
m

<!-- b003090 | furniture | pages [25] -->
m

<!-- b003091 | furniture | pages [25] -->
m

<!-- b003092 | furniture | pages [25] -->
m

<!-- b003093 | furniture | pages [25] -->
m

<!-- b003094 | furniture | pages [25] -->
m

<!-- b003095 | furniture | pages [25] -->
m

<!-- b003096 | furniture | pages [25] -->
m

<!-- b003097 | furniture | pages [25] -->
m

<!-- b003098 | furniture | pages [25] -->
m

<!-- b003099 | furniture | pages [25] -->
m

<!-- b003100 | furniture | pages [25] -->
m

<!-- b003101 | furniture | pages [25] -->
m

<!-- b003102 | furniture | pages [25] -->
m

<!-- b003103 | furniture | pages [25] -->
m

<!-- b003104 | furniture | pages [25] -->
m

<!-- b003105 | furniture | pages [25] -->
m

<!-- b003106 | furniture | pages [25] -->
m

<!-- b003107 | furniture | pages [25] -->
m

<!-- b003108 | furniture | pages [25] -->
m

<!-- b003109 | furniture | pages [25] -->
m

<!-- b003110 | furniture | pages [25] -->
m

<!-- b003111 | furniture | pages [25] -->
m

<!-- b003112 | furniture | pages [25] -->
m

<!-- b003113 | furniture | pages [25] -->
m

<!-- b003114 | furniture | pages [25] -->
m

<!-- b003115 | furniture | pages [25] -->
m

<!-- b003116 | furniture | pages [25] -->
m

<!-- b003117 | furniture | pages [25] -->
m

<!-- b003118 | furniture | pages [25] -->
m

<!-- b003119 | furniture | pages [25] -->
m

<!-- b003120 | furniture | pages [25] -->
m

<!-- b003121 | furniture | pages [25] -->
m

<!-- b003122 | furniture | pages [25] -->
m

<!-- b003123 | furniture | pages [25] -->
m

<!-- b003124 | furniture | pages [25] -->
m

<!-- b003125 | furniture | pages [25] -->
m

<!-- b003126 | furniture | pages [25] -->
m

<!-- b003127 | furniture | pages [25] -->
m

<!-- b003128 | furniture | pages [25] -->
m

<!-- b003129 | furniture | pages [25] -->
m

<!-- b003130 | furniture | pages [25] -->
m

<!-- b003131 | furniture | pages [25] -->
m

<!-- b003132 | furniture | pages [25] -->
m

<!-- b003133 | furniture | pages [25] -->
m

<!-- b003134 | furniture | pages [25] -->
m

<!-- b003135 | furniture | pages [25] -->
m

<!-- b003136 | furniture | pages [25] -->
m

<!-- b003137 | furniture | pages [25] -->
m

<!-- b003138 | furniture | pages [25] -->
m

<!-- b003139 | furniture | pages [25] -->
m

<!-- b003140 | furniture | pages [25] -->
m

<!-- b003141 | furniture | pages [25] -->
m

<!-- b003142 | furniture | pages [25] -->
m

<!-- b003143 | furniture | pages [25] -->
m

<!-- b003144 | furniture | pages [25] -->
m

<!-- b003145 | furniture | pages [25] -->
m

<!-- b003146 | furniture | pages [25] -->
m

<!-- b003147 | furniture | pages [25] -->
m

<!-- b003148 | furniture | pages [25] -->
m

<!-- b003149 | furniture | pages [25] -->
m

<!-- b003150 | furniture | pages [25] -->
m

<!-- b003151 | furniture | pages [25] -->
m

<!-- b003152 | furniture | pages [25] -->
m

<!-- b003153 | furniture | pages [25] -->
m

<!-- b003154 | furniture | pages [25] -->
m

<!-- b003155 | furniture | pages [25] -->
m

<!-- b003156 | furniture | pages [25] -->
m

<!-- b003157 | furniture | pages [25] -->
m

<!-- b003158 | furniture | pages [25] -->
m

<!-- b003159 | furniture | pages [25] -->
m

<!-- b003160 | furniture | pages [25] -->
m

<!-- b003161 | furniture | pages [25] -->
m

<!-- b003162 | furniture | pages [25] -->
m

<!-- b003163 | furniture | pages [25] -->
m

<!-- b003164 | furniture | pages [25] -->
m

<!-- b003165 | furniture | pages [25] -->
m

<!-- b003166 | furniture | pages [25] -->
m

<!-- b003167 | furniture | pages [25] -->
m

<!-- b003168 | furniture | pages [25] -->
m

<!-- b003169 | furniture | pages [25] -->
m

<!-- b003170 | furniture | pages [25] -->
m

<!-- b003171 | furniture | pages [25] -->
m

<!-- b003172 | furniture | pages [25] -->
m

<!-- b003173 | furniture | pages [25] -->
m

<!-- b003174 | furniture | pages [25] -->
m

<!-- b003175 | furniture | pages [25] -->
m

<!-- b003176 | furniture | pages [25] -->
m

<!-- b003177 | furniture | pages [25] -->
m

<!-- b003178 | furniture | pages [25] -->
m

<!-- b003179 | furniture | pages [25] -->
m

<!-- b003180 | furniture | pages [25] -->
m

<!-- b003181 | furniture | pages [25] -->
m

<!-- b003182 | furniture | pages [25] -->
m

<!-- b003183 | furniture | pages [25] -->
m

<!-- b003184 | furniture | pages [25] -->
m

<!-- b003185 | furniture | pages [25] -->
m

<!-- b003186 | furniture | pages [25] -->
m

<!-- b003187 | furniture | pages [25] -->
m

<!-- b003188 | furniture | pages [25] -->
m

<!-- b003189 | furniture | pages [25] -->
m

<!-- b003190 | furniture | pages [25] -->
m

<!-- b003191 | furniture | pages [25] -->
m

<!-- b003192 | furniture | pages [25] -->
m

<!-- b003193 | furniture | pages [25] -->
m

<!-- b003194 | furniture | pages [25] -->
m

<!-- b003195 | furniture | pages [25] -->
m

<!-- b003196 | furniture | pages [25] -->
m

<!-- b003197 | furniture | pages [25] -->
m

<!-- b003198 | furniture | pages [25] -->
m

<!-- b003199 | furniture | pages [25] -->
m

<!-- b003200 | furniture | pages [25] -->
m

<!-- b003201 | furniture | pages [25] -->
m

<!-- b003202 | furniture | pages [25] -->
m

<!-- b003203 | furniture | pages [25] -->
m

<!-- b003204 | furniture | pages [25] -->
m

<!-- b003205 | furniture | pages [25] -->
m

<!-- b003206 | furniture | pages [25] -->
m

<!-- b003207 | furniture | pages [25] -->
m

<!-- b003208 | furniture | pages [25] -->
m

<!-- b003209 | furniture | pages [25] -->
m

<!-- b003210 | furniture | pages [25] -->
m

<!-- b003211 | furniture | pages [25] -->
m

<!-- b003212 | furniture | pages [25] -->
m

<!-- b003213 | furniture | pages [25] -->
m

<!-- b003214 | furniture | pages [25] -->
m

<!-- b003215 | furniture | pages [25] -->
m

<!-- b003216 | furniture | pages [25] -->
m

<!-- b003217 | furniture | pages [25] -->
m

<!-- b003218 | furniture | pages [25] -->
m

<!-- b003219 | furniture | pages [25] -->
m

<!-- b003220 | furniture | pages [25] -->
m

<!-- b003221 | furniture | pages [25] -->
m

<!-- b003222 | furniture | pages [25] -->
m

<!-- b003223 | furniture | pages [25] -->
m

<!-- b003224 | furniture | pages [25] -->
m

<!-- b003225 | furniture | pages [25] -->
m

<!-- b003226 | furniture | pages [25] -->
m

<!-- b003227 | furniture | pages [25] -->
m

<!-- b003228 | furniture | pages [25] -->
m

<!-- b003229 | furniture | pages [25] -->
m

<!-- b003230 | furniture | pages [25] -->
m

<!-- b003231 | furniture | pages [25] -->
m

<!-- b003232 | furniture | pages [25] -->
m

<!-- b003233 | furniture | pages [25] -->
m

<!-- b003234 | furniture | pages [25] -->
m

<!-- b003235 | furniture | pages [25] -->
m

<!-- b003236 | furniture | pages [25] -->
m

<!-- b003237 | furniture | pages [25] -->
m

<!-- b003238 | furniture | pages [25] -->
m

<!-- b003239 | furniture | pages [25] -->
m

<!-- b003240 | furniture | pages [25] -->
m

<!-- b003241 | furniture | pages [25] -->
m

<!-- b003242 | furniture | pages [25] -->
m

<!-- b003243 | furniture | pages [25] -->
m

<!-- b003244 | furniture | pages [25] -->
m

<!-- b003245 | furniture | pages [25] -->
m

<!-- b003246 | furniture | pages [25] -->
m

<!-- b003247 | furniture | pages [25] -->
m

<!-- b003248 | furniture | pages [25] -->
m

<!-- b003249 | furniture | pages [25] -->
m

<!-- b003250 | furniture | pages [25] -->
m

<!-- b003251 | furniture | pages [25] -->
m

<!-- b003252 | furniture | pages [25] -->
m

<!-- b003253 | furniture | pages [25] -->
m

<!-- b003254 | furniture | pages [25] -->
m

<!-- b003255 | furniture | pages [25] -->
m

<!-- b003256 | furniture | pages [25] -->
m

<!-- b003257 | furniture | pages [25] -->
m

<!-- b003258 | furniture | pages [25] -->
m

<!-- b003259 | furniture | pages [25] -->
m

<!-- b003260 | furniture | pages [25] -->
m

<!-- b003261 | furniture | pages [25] -->
m

<!-- b003262 | furniture | pages [25] -->
m

<!-- b003263 | furniture | pages [25] -->
m

<!-- b003264 | furniture | pages [25] -->
m

<!-- b003265 | furniture | pages [25] -->
m

<!-- b003266 | furniture | pages [25] -->
m

<!-- b003267 | furniture | pages [25] -->
m

<!-- b003268 | furniture | pages [25] -->
m

<!-- b003269 | furniture | pages [25] -->
m

<!-- b003270 | furniture | pages [25] -->
m

<!-- b003271 | furniture | pages [25] -->
m

<!-- b003272 | furniture | pages [25] -->
m

<!-- b003273 | furniture | pages [25] -->
m

<!-- b003274 | furniture | pages [25] -->
m

<!-- b003275 | furniture | pages [25] -->
m

<!-- b003276 | furniture | pages [25] -->
m

<!-- b003277 | furniture | pages [25] -->
m

<!-- b003278 | furniture | pages [25] -->
m

<!-- b003279 | furniture | pages [25] -->
m

<!-- b003280 | furniture | pages [25] -->
m

<!-- b003281 | furniture | pages [25] -->
m

<!-- b003282 | furniture | pages [25] -->
m

<!-- b003283 | furniture | pages [25] -->
m

<!-- b003284 | furniture | pages [25] -->
m

<!-- b003285 | furniture | pages [25] -->
m

<!-- b003286 | furniture | pages [25] -->
m

<!-- b003287 | furniture | pages [25] -->
m

<!-- b003288 | furniture | pages [25] -->
m

<!-- b003289 | furniture | pages [25] -->
m

<!-- b003290 | furniture | pages [25] -->
m

<!-- b003291 | furniture | pages [25] -->
m

<!-- b003292 | furniture | pages [25] -->
m

<!-- b003293 | furniture | pages [25] -->
m

<!-- b003294 | furniture | pages [25] -->
m

<!-- b003295 | furniture | pages [25] -->
m

<!-- b003296 | furniture | pages [25] -->
m

<!-- b003297 | furniture | pages [26] -->
Team # 2503389

<!-- b003298 | furniture | pages [26] -->
Page 26 of 26

<!-- b003299 | heading | pages [26] -->
Report on Use of AI

<!-- b003300 | ai_disclosure | pages [26] -->
1. OpenAI ChatGPT (Nov 5, 2023 version, ChatGPT-4o)

<!-- b003301 | ai_disclosure | pages [26] -->
Query1: <Please provide the citation format for the report about United States Women’s

<!-- b003302 | ai_disclosure | pages [26] -->
Gymnastics and Béla and Marta Károlyi>

<!-- b003303 | ai_disclosure | pages [26] -->
Output: <Here is the citation format for the Wikipedia article on Béla Károlyi:Béla

<!-- b003304 | ai_disclosure | pages [26] -->
Károlyi. (2024, November 23). In Wikipedia, The Free Encyclopedia. Retrieved

<!-- b003305 | ai_disclosure | pages [26] -->
from https://en.wikipedia.org/wiki/BThis format includes the title of the article, the

<!-- b003306 | ai_disclosure | pages [26] -->
date of the last update, the source, and the URL for reference.>

<!-- b003307 | ai_disclosure | pages [26] -->
2. OpenAI ChatGPT (Nov 5, 2023 version, ChatGPT-4o)

<!-- b003308 | ai_disclosure | pages [26] -->
m

<!-- b003309 | ai_disclosure | pages [26] -->
m

<!-- b003310 | ai_disclosure | pages [26] -->
m

<!-- b003311 | ai_disclosure | pages [26] -->
m

<!-- b003312 | ai_disclosure | pages [26] -->
m

<!-- b003313 | ai_disclosure | pages [26] -->
m

<!-- b003314 | ai_disclosure | pages [26] -->
m

<!-- b003315 | ai_disclosure | pages [26] -->
m

<!-- b003316 | ai_disclosure | pages [26] -->
m

<!-- b003317 | ai_disclosure | pages [26] -->
m

<!-- b003318 | ai_disclosure | pages [26] -->
m

<!-- b003319 | ai_disclosure | pages [26] -->
m

<!-- b003320 | ai_disclosure | pages [26] -->
m

<!-- b003321 | ai_disclosure | pages [26] -->
m

<!-- b003322 | ai_disclosure | pages [26] -->
m

<!-- b003323 | ai_disclosure | pages [26] -->
m

<!-- b003324 | ai_disclosure | pages [26] -->
m

<!-- b003325 | ai_disclosure | pages [26] -->
m

<!-- b003326 | ai_disclosure | pages [26] -->
m

<!-- b003327 | ai_disclosure | pages [26] -->
m

<!-- b003328 | ai_disclosure | pages [26] -->
m

<!-- b003329 | ai_disclosure | pages [26] -->
m

<!-- b003330 | ai_disclosure | pages [26] -->
m

<!-- b003331 | ai_disclosure | pages [26] -->
m

<!-- b003332 | ai_disclosure | pages [26] -->
m

<!-- b003333 | ai_disclosure | pages [26] -->
m

<!-- b003334 | ai_disclosure | pages [26] -->
m

<!-- b003335 | ai_disclosure | pages [26] -->
m

<!-- b003336 | ai_disclosure | pages [26] -->
m

<!-- b003337 | ai_disclosure | pages [26] -->
m

<!-- b003338 | ai_disclosure | pages [26] -->
m

<!-- b003339 | ai_disclosure | pages [26] -->
m

<!-- b003340 | ai_disclosure | pages [26] -->
m

<!-- b003341 | ai_disclosure | pages [26] -->
m

<!-- b003342 | ai_disclosure | pages [26] -->
m

<!-- b003343 | ai_disclosure | pages [26] -->
m

<!-- b003344 | ai_disclosure | pages [26] -->
m

<!-- b003345 | ai_disclosure | pages [26] -->
m

<!-- b003346 | ai_disclosure | pages [26] -->
m

<!-- b003347 | ai_disclosure | pages [26] -->
m

<!-- b003348 | ai_disclosure | pages [26] -->
m

<!-- b003349 | ai_disclosure | pages [26] -->
m

<!-- b003350 | ai_disclosure | pages [26] -->
m

<!-- b003351 | ai_disclosure | pages [26] -->
m

<!-- b003352 | ai_disclosure | pages [26] -->
m

<!-- b003353 | ai_disclosure | pages [26] -->
m

<!-- b003354 | ai_disclosure | pages [26] -->
m

<!-- b003355 | ai_disclosure | pages [26] -->
m

<!-- b003356 | ai_disclosure | pages [26] -->
m

<!-- b003357 | ai_disclosure | pages [26] -->
m

<!-- b003358 | ai_disclosure | pages [26] -->
m

<!-- b003359 | ai_disclosure | pages [26] -->
m

<!-- b003360 | ai_disclosure | pages [26] -->
m

<!-- b003361 | ai_disclosure | pages [26] -->
Query1: <Please briefly explain the differences and similarities between MLR and FNN>

<!-- b003362 | ai_disclosure | pages [26] -->
m

<!-- b003363 | ai_disclosure | pages [26] -->
m

<!-- b003364 | ai_disclosure | pages [26] -->
m

<!-- b003365 | ai_disclosure | pages [26] -->
m

<!-- b003366 | ai_disclosure | pages [26] -->
m

<!-- b003367 | ai_disclosure | pages [26] -->
m

<!-- b003368 | ai_disclosure | pages [26] -->
m

<!-- b003369 | ai_disclosure | pages [26] -->
m

<!-- b003370 | ai_disclosure | pages [26] -->
m

<!-- b003371 | ai_disclosure | pages [26] -->
m

<!-- b003372 | ai_disclosure | pages [26] -->
m

<!-- b003373 | ai_disclosure | pages [26] -->
m

<!-- b003374 | ai_disclosure | pages [26] -->
m

<!-- b003375 | ai_disclosure | pages [26] -->
m

<!-- b003376 | ai_disclosure | pages [26] -->
m

<!-- b003377 | ai_disclosure | pages [26] -->
m

<!-- b003378 | ai_disclosure | pages [26] -->
m

<!-- b003379 | ai_disclosure | pages [26] -->
m

<!-- b003380 | ai_disclosure | pages [26] -->
m

<!-- b003381 | ai_disclosure | pages [26] -->
m

<!-- b003382 | ai_disclosure | pages [26] -->
m

<!-- b003383 | ai_disclosure | pages [26] -->
m

<!-- b003384 | ai_disclosure | pages [26] -->
m

<!-- b003385 | ai_disclosure | pages [26] -->
m

<!-- b003386 | ai_disclosure | pages [26] -->
m

<!-- b003387 | ai_disclosure | pages [26] -->
m

<!-- b003388 | ai_disclosure | pages [26] -->
m

<!-- b003389 | ai_disclosure | pages [26] -->
m

<!-- b003390 | ai_disclosure | pages [26] -->
m

<!-- b003391 | ai_disclosure | pages [26] -->
m

<!-- b003392 | ai_disclosure | pages [26] -->
m

<!-- b003393 | ai_disclosure | pages [26] -->
m

<!-- b003394 | ai_disclosure | pages [26] -->
m

<!-- b003395 | ai_disclosure | pages [26] -->
m

<!-- b003396 | ai_disclosure | pages [26] -->
m

<!-- b003397 | ai_disclosure | pages [26] -->
m

<!-- b003398 | ai_disclosure | pages [26] -->
m

<!-- b003399 | ai_disclosure | pages [26] -->
m

<!-- b003400 | ai_disclosure | pages [26] -->
m

<!-- b003401 | ai_disclosure | pages [26] -->
m

<!-- b003402 | ai_disclosure | pages [26] -->
m

<!-- b003403 | ai_disclosure | pages [26] -->
m

<!-- b003404 | ai_disclosure | pages [26] -->
m

<!-- b003405 | ai_disclosure | pages [26] -->
m

<!-- b003406 | ai_disclosure | pages [26] -->
m

<!-- b003407 | ai_disclosure | pages [26] -->
m

<!-- b003408 | ai_disclosure | pages [26] -->
m

<!-- b003409 | ai_disclosure | pages [26] -->
m

<!-- b003410 | ai_disclosure | pages [26] -->
m

<!-- b003411 | ai_disclosure | pages [26] -->
m

<!-- b003412 | ai_disclosure | pages [26] -->
m

<!-- b003413 | ai_disclosure | pages [26] -->
m

<!-- b003414 | ai_disclosure | pages [26] -->
m

<!-- b003415 | ai_disclosure | pages [26] -->
m

<!-- b003416 | ai_disclosure | pages [26] -->
m

<!-- b003417 | ai_disclosure | pages [26] -->
m

<!-- b003418 | ai_disclosure | pages [26] -->
m

<!-- b003419 | ai_disclosure | pages [26] -->
m

<!-- b003420 | ai_disclosure | pages [26] -->
m

<!-- b003421 | ai_disclosure | pages [26] -->
m

<!-- b003422 | ai_disclosure | pages [26] -->
m

<!-- b003423 | ai_disclosure | pages [26] -->
m

<!-- b003424 | ai_disclosure | pages [26] -->
m

<!-- b003425 | ai_disclosure | pages [26] -->
m

<!-- b003426 | ai_disclosure | pages [26] -->
m

<!-- b003427 | ai_disclosure | pages [26] -->
m

<!-- b003428 | ai_disclosure | pages [26] -->
m

<!-- b003429 | ai_disclosure | pages [26] -->
m

<!-- b003430 | ai_disclosure | pages [26] -->
m

<!-- b003431 | ai_disclosure | pages [26] -->
m

<!-- b003432 | ai_disclosure | pages [26] -->
m

<!-- b003433 | ai_disclosure | pages [26] -->
m

<!-- b003434 | ai_disclosure | pages [26] -->
m

<!-- b003435 | ai_disclosure | pages [26] -->
m

<!-- b003436 | ai_disclosure | pages [26] -->
m

<!-- b003437 | ai_disclosure | pages [26] -->
m

<!-- b003438 | ai_disclosure | pages [26] -->
m

<!-- b003439 | ai_disclosure | pages [26] -->
m

<!-- b003440 | ai_disclosure | pages [26] -->
m

<!-- b003441 | ai_disclosure | pages [26] -->
m

<!-- b003442 | ai_disclosure | pages [26] -->
m

<!-- b003443 | ai_disclosure | pages [26] -->
m

<!-- b003444 | ai_disclosure | pages [26] -->
m

<!-- b003445 | ai_disclosure | pages [26] -->
m

<!-- b003446 | ai_disclosure | pages [26] -->
m

<!-- b003447 | ai_disclosure | pages [26] -->
m

<!-- b003448 | ai_disclosure | pages [26] -->
m

<!-- b003449 | ai_disclosure | pages [26] -->
m

<!-- b003450 | ai_disclosure | pages [26] -->
m

<!-- b003451 | ai_disclosure | pages [26] -->
m

<!-- b003452 | ai_disclosure | pages [26] -->
m

<!-- b003453 | ai_disclosure | pages [26] -->
m

<!-- b003454 | ai_disclosure | pages [26] -->
m

<!-- b003455 | ai_disclosure | pages [26] -->
m

<!-- b003456 | ai_disclosure | pages [26] -->
m

<!-- b003457 | ai_disclosure | pages [26] -->
m

<!-- b003458 | ai_disclosure | pages [26] -->
m

<!-- b003459 | ai_disclosure | pages [26] -->
m

<!-- b003460 | ai_disclosure | pages [26] -->
m

<!-- b003461 | ai_disclosure | pages [26] -->
m

<!-- b003462 | ai_disclosure | pages [26] -->
m

<!-- b003463 | ai_disclosure | pages [26] -->
m

<!-- b003464 | ai_disclosure | pages [26] -->
m

<!-- b003465 | ai_disclosure | pages [26] -->
m

<!-- b003466 | ai_disclosure | pages [26] -->
m

<!-- b003467 | ai_disclosure | pages [26] -->
m

<!-- b003468 | ai_disclosure | pages [26] -->
m

<!-- b003469 | ai_disclosure | pages [26] -->
m

<!-- b003470 | ai_disclosure | pages [26] -->
m

<!-- b003471 | ai_disclosure | pages [26] -->
m

<!-- b003472 | ai_disclosure | pages [26] -->
m

<!-- b003473 | ai_disclosure | pages [26] -->
m

<!-- b003474 | ai_disclosure | pages [26] -->
m

<!-- b003475 | ai_disclosure | pages [26] -->
m

<!-- b003476 | ai_disclosure | pages [26] -->
m

<!-- b003477 | ai_disclosure | pages [26] -->
m

<!-- b003478 | ai_disclosure | pages [26] -->
m

<!-- b003479 | ai_disclosure | pages [26] -->
m

<!-- b003480 | ai_disclosure | pages [26] -->
m

<!-- b003481 | ai_disclosure | pages [26] -->
m

<!-- b003482 | ai_disclosure | pages [26] -->
m

<!-- b003483 | ai_disclosure | pages [26] -->
m

<!-- b003484 | ai_disclosure | pages [26] -->
m

<!-- b003485 | ai_disclosure | pages [26] -->
m

<!-- b003486 | ai_disclosure | pages [26] -->
m

<!-- b003487 | ai_disclosure | pages [26] -->
m

<!-- b003488 | ai_disclosure | pages [26] -->
m

<!-- b003489 | ai_disclosure | pages [26] -->
m

<!-- b003490 | ai_disclosure | pages [26] -->
m

<!-- b003491 | ai_disclosure | pages [26] -->
m

<!-- b003492 | ai_disclosure | pages [26] -->
m

<!-- b003493 | ai_disclosure | pages [26] -->
m

<!-- b003494 | ai_disclosure | pages [26] -->
m

<!-- b003495 | ai_disclosure | pages [26] -->
m

<!-- b003496 | ai_disclosure | pages [26] -->
m

<!-- b003497 | ai_disclosure | pages [26] -->
m

<!-- b003498 | ai_disclosure | pages [26] -->
m

<!-- b003499 | ai_disclosure | pages [26] -->
m

<!-- b003500 | ai_disclosure | pages [26] -->
m

<!-- b003501 | ai_disclosure | pages [26] -->
m

<!-- b003502 | ai_disclosure | pages [26] -->
m

<!-- b003503 | ai_disclosure | pages [26] -->
m

<!-- b003504 | ai_disclosure | pages [26] -->
m

<!-- b003505 | ai_disclosure | pages [26] -->
m

<!-- b003506 | ai_disclosure | pages [26] -->
m

<!-- b003507 | ai_disclosure | pages [26] -->
m

<!-- b003508 | ai_disclosure | pages [26] -->
m

<!-- b003509 | ai_disclosure | pages [26] -->
m

<!-- b003510 | ai_disclosure | pages [26] -->
m

<!-- b003511 | ai_disclosure | pages [26] -->
m

<!-- b003512 | ai_disclosure | pages [26] -->
m

<!-- b003513 | ai_disclosure | pages [26] -->
m

<!-- b003514 | ai_disclosure | pages [26] -->
m

<!-- b003515 | ai_disclosure | pages [26] -->
m

<!-- b003516 | ai_disclosure | pages [26] -->
m

<!-- b003517 | ai_disclosure | pages [26] -->
m

<!-- b003518 | ai_disclosure | pages [26] -->
m

<!-- b003519 | ai_disclosure | pages [26] -->
m

<!-- b003520 | ai_disclosure | pages [26] -->
m

<!-- b003521 | ai_disclosure | pages [26] -->
m

<!-- b003522 | ai_disclosure | pages [26] -->
m

<!-- b003523 | ai_disclosure | pages [26] -->
m

<!-- b003524 | ai_disclosure | pages [26] -->
m

<!-- b003525 | ai_disclosure | pages [26] -->
m

<!-- b003526 | ai_disclosure | pages [26] -->
m

<!-- b003527 | ai_disclosure | pages [26] -->
m

<!-- b003528 | ai_disclosure | pages [26] -->
m

<!-- b003529 | ai_disclosure | pages [26] -->
m

<!-- b003530 | ai_disclosure | pages [26] -->
m

<!-- b003531 | ai_disclosure | pages [26] -->
m

<!-- b003532 | ai_disclosure | pages [26] -->
m

<!-- b003533 | ai_disclosure | pages [26] -->
m

<!-- b003534 | ai_disclosure | pages [26] -->
m

<!-- b003535 | ai_disclosure | pages [26] -->
m

<!-- b003536 | ai_disclosure | pages [26] -->
m

<!-- b003537 | ai_disclosure | pages [26] -->
m

<!-- b003538 | ai_disclosure | pages [26] -->
m

<!-- b003539 | ai_disclosure | pages [26] -->
m

<!-- b003540 | ai_disclosure | pages [26] -->
m

<!-- b003541 | ai_disclosure | pages [26] -->
m

<!-- b003542 | ai_disclosure | pages [26] -->
m

<!-- b003543 | ai_disclosure | pages [26] -->
m

<!-- b003544 | ai_disclosure | pages [26] -->
m

<!-- b003545 | ai_disclosure | pages [26] -->
m

<!-- b003546 | ai_disclosure | pages [26] -->
m

<!-- b003547 | ai_disclosure | pages [26] -->
m

<!-- b003548 | ai_disclosure | pages [26] -->
m

<!-- b003549 | ai_disclosure | pages [26] -->
m

<!-- b003550 | ai_disclosure | pages [26] -->
m

<!-- b003551 | ai_disclosure | pages [26] -->
m

<!-- b003552 | ai_disclosure | pages [26] -->
m

<!-- b003553 | ai_disclosure | pages [26] -->
Output: <Both Multiple Linear Regression (MLR) and Feedforward Neural Networks

<!-- b003554 | ai_disclosure | pages [26] -->
m

<!-- b003555 | ai_disclosure | pages [26] -->
m

<!-- b003556 | ai_disclosure | pages [26] -->
m

<!-- b003557 | ai_disclosure | pages [26] -->
m

<!-- b003558 | ai_disclosure | pages [26] -->
m

<!-- b003559 | ai_disclosure | pages [26] -->
m

<!-- b003560 | ai_disclosure | pages [26] -->
m

<!-- b003561 | ai_disclosure | pages [26] -->
m

<!-- b003562 | ai_disclosure | pages [26] -->
m

<!-- b003563 | ai_disclosure | pages [26] -->
m

<!-- b003564 | ai_disclosure | pages [26] -->
m

<!-- b003565 | ai_disclosure | pages [26] -->
m

<!-- b003566 | ai_disclosure | pages [26] -->
m

<!-- b003567 | ai_disclosure | pages [26] -->
m

<!-- b003568 | ai_disclosure | pages [26] -->
m

<!-- b003569 | ai_disclosure | pages [26] -->
m

<!-- b003570 | ai_disclosure | pages [26] -->
m

<!-- b003571 | ai_disclosure | pages [26] -->
m

<!-- b003572 | ai_disclosure | pages [26] -->
m

<!-- b003573 | ai_disclosure | pages [26] -->
m

<!-- b003574 | ai_disclosure | pages [26] -->
m

<!-- b003575 | ai_disclosure | pages [26] -->
m

<!-- b003576 | ai_disclosure | pages [26] -->
m

<!-- b003577 | ai_disclosure | pages [26] -->
m

<!-- b003578 | ai_disclosure | pages [26] -->
m

<!-- b003579 | ai_disclosure | pages [26] -->
m

<!-- b003580 | ai_disclosure | pages [26] -->
m

<!-- b003581 | ai_disclosure | pages [26] -->
m

<!-- b003582 | ai_disclosure | pages [26] -->
m

<!-- b003583 | ai_disclosure | pages [26] -->
m

<!-- b003584 | ai_disclosure | pages [26] -->
m

<!-- b003585 | ai_disclosure | pages [26] -->
m

<!-- b003586 | ai_disclosure | pages [26] -->
m

<!-- b003587 | ai_disclosure | pages [26] -->
m

<!-- b003588 | ai_disclosure | pages [26] -->
m

<!-- b003589 | ai_disclosure | pages [26] -->
m

<!-- b003590 | ai_disclosure | pages [26] -->
m

<!-- b003591 | ai_disclosure | pages [26] -->
m

<!-- b003592 | ai_disclosure | pages [26] -->
m

<!-- b003593 | ai_disclosure | pages [26] -->
m

<!-- b003594 | ai_disclosure | pages [26] -->
m

<!-- b003595 | ai_disclosure | pages [26] -->
m

<!-- b003596 | ai_disclosure | pages [26] -->
m

<!-- b003597 | ai_disclosure | pages [26] -->
m

<!-- b003598 | ai_disclosure | pages [26] -->
m

<!-- b003599 | ai_disclosure | pages [26] -->
m

<!-- b003600 | ai_disclosure | pages [26] -->
m

<!-- b003601 | ai_disclosure | pages [26] -->
m

<!-- b003602 | ai_disclosure | pages [26] -->
m

<!-- b003603 | ai_disclosure | pages [26] -->
m

<!-- b003604 | ai_disclosure | pages [26] -->
m

<!-- b003605 | ai_disclosure | pages [26] -->
m

<!-- b003606 | ai_disclosure | pages [26] -->
m

<!-- b003607 | ai_disclosure | pages [26] -->
m

<!-- b003608 | ai_disclosure | pages [26] -->
m

<!-- b003609 | ai_disclosure | pages [26] -->
m

<!-- b003610 | ai_disclosure | pages [26] -->
m

<!-- b003611 | ai_disclosure | pages [26] -->
m

<!-- b003612 | ai_disclosure | pages [26] -->
m

<!-- b003613 | ai_disclosure | pages [26] -->
m

<!-- b003614 | ai_disclosure | pages [26] -->
m

<!-- b003615 | ai_disclosure | pages [26] -->
m

<!-- b003616 | ai_disclosure | pages [26] -->
m

<!-- b003617 | ai_disclosure | pages [26] -->
m

<!-- b003618 | ai_disclosure | pages [26] -->
m

<!-- b003619 | ai_disclosure | pages [26] -->
m

<!-- b003620 | ai_disclosure | pages [26] -->
m

<!-- b003621 | ai_disclosure | pages [26] -->
m

<!-- b003622 | ai_disclosure | pages [26] -->
m

<!-- b003623 | ai_disclosure | pages [26] -->
m

<!-- b003624 | ai_disclosure | pages [26] -->
m

<!-- b003625 | ai_disclosure | pages [26] -->
m

<!-- b003626 | ai_disclosure | pages [26] -->
m

<!-- b003627 | ai_disclosure | pages [26] -->
m

<!-- b003628 | ai_disclosure | pages [26] -->
m

<!-- b003629 | ai_disclosure | pages [26] -->
m

<!-- b003630 | ai_disclosure | pages [26] -->
m

<!-- b003631 | ai_disclosure | pages [26] -->
m

<!-- b003632 | ai_disclosure | pages [26] -->
m

<!-- b003633 | ai_disclosure | pages [26] -->
m

<!-- b003634 | ai_disclosure | pages [26] -->
m

<!-- b003635 | ai_disclosure | pages [26] -->
m

<!-- b003636 | ai_disclosure | pages [26] -->
m

<!-- b003637 | ai_disclosure | pages [26] -->
m

<!-- b003638 | ai_disclosure | pages [26] -->
m

<!-- b003639 | ai_disclosure | pages [26] -->
m

<!-- b003640 | ai_disclosure | pages [26] -->
m

<!-- b003641 | ai_disclosure | pages [26] -->
m

<!-- b003642 | ai_disclosure | pages [26] -->
m

<!-- b003643 | ai_disclosure | pages [26] -->
m

<!-- b003644 | ai_disclosure | pages [26] -->
m

<!-- b003645 | ai_disclosure | pages [26] -->
m

<!-- b003646 | ai_disclosure | pages [26] -->
m

<!-- b003647 | ai_disclosure | pages [26] -->
m

<!-- b003648 | ai_disclosure | pages [26] -->
m

<!-- b003649 | ai_disclosure | pages [26] -->
m

<!-- b003650 | ai_disclosure | pages [26] -->
m

<!-- b003651 | ai_disclosure | pages [26] -->
m

<!-- b003652 | ai_disclosure | pages [26] -->
m

<!-- b003653 | ai_disclosure | pages [26] -->
m

<!-- b003654 | ai_disclosure | pages [26] -->
m

<!-- b003655 | ai_disclosure | pages [26] -->
m

<!-- b003656 | ai_disclosure | pages [26] -->
m

<!-- b003657 | ai_disclosure | pages [26] -->
m

<!-- b003658 | ai_disclosure | pages [26] -->
m

<!-- b003659 | ai_disclosure | pages [26] -->
m

<!-- b003660 | ai_disclosure | pages [26] -->
m

<!-- b003661 | ai_disclosure | pages [26] -->
m

<!-- b003662 | ai_disclosure | pages [26] -->
m

<!-- b003663 | ai_disclosure | pages [26] -->
m

<!-- b003664 | ai_disclosure | pages [26] -->
m

<!-- b003665 | ai_disclosure | pages [26] -->
m

<!-- b003666 | ai_disclosure | pages [26] -->
m

<!-- b003667 | ai_disclosure | pages [26] -->
m

<!-- b003668 | ai_disclosure | pages [26] -->
m

<!-- b003669 | ai_disclosure | pages [26] -->
m

<!-- b003670 | ai_disclosure | pages [26] -->
m

<!-- b003671 | ai_disclosure | pages [26] -->
m

<!-- b003672 | ai_disclosure | pages [26] -->
m

<!-- b003673 | ai_disclosure | pages [26] -->
m

<!-- b003674 | ai_disclosure | pages [26] -->
m

<!-- b003675 | ai_disclosure | pages [26] -->
m

<!-- b003676 | ai_disclosure | pages [26] -->
m

<!-- b003677 | ai_disclosure | pages [26] -->
m

<!-- b003678 | ai_disclosure | pages [26] -->
m

<!-- b003679 | ai_disclosure | pages [26] -->
m

<!-- b003680 | ai_disclosure | pages [26] -->
m

<!-- b003681 | ai_disclosure | pages [26] -->
m

<!-- b003682 | ai_disclosure | pages [26] -->
m

<!-- b003683 | ai_disclosure | pages [26] -->
m

<!-- b003684 | ai_disclosure | pages [26] -->
m

<!-- b003685 | ai_disclosure | pages [26] -->
m

<!-- b003686 | ai_disclosure | pages [26] -->
m

<!-- b003687 | ai_disclosure | pages [26] -->
m

<!-- b003688 | ai_disclosure | pages [26] -->
m

<!-- b003689 | ai_disclosure | pages [26] -->
m

<!-- b003690 | ai_disclosure | pages [26] -->
m

<!-- b003691 | ai_disclosure | pages [26] -->
m

<!-- b003692 | ai_disclosure | pages [26] -->
m

<!-- b003693 | ai_disclosure | pages [26] -->
m

<!-- b003694 | ai_disclosure | pages [26] -->
m

<!-- b003695 | ai_disclosure | pages [26] -->
m

<!-- b003696 | ai_disclosure | pages [26] -->
m

<!-- b003697 | ai_disclosure | pages [26] -->
(FNN) are supervised learning methods that aim to model the relationship between

<!-- b003698 | ai_disclosure | pages [26] -->
m

<!-- b003699 | ai_disclosure | pages [26] -->
m

<!-- b003700 | ai_disclosure | pages [26] -->
m

<!-- b003701 | ai_disclosure | pages [26] -->
m

<!-- b003702 | ai_disclosure | pages [26] -->
m

<!-- b003703 | ai_disclosure | pages [26] -->
m

<!-- b003704 | ai_disclosure | pages [26] -->
m

<!-- b003705 | ai_disclosure | pages [26] -->
m

<!-- b003706 | ai_disclosure | pages [26] -->
m

<!-- b003707 | ai_disclosure | pages [26] -->
m

<!-- b003708 | ai_disclosure | pages [26] -->
m

<!-- b003709 | ai_disclosure | pages [26] -->
m

<!-- b003710 | ai_disclosure | pages [26] -->
m

<!-- b003711 | ai_disclosure | pages [26] -->
m

<!-- b003712 | ai_disclosure | pages [26] -->
m

<!-- b003713 | ai_disclosure | pages [26] -->
m

<!-- b003714 | ai_disclosure | pages [26] -->
m

<!-- b003715 | ai_disclosure | pages [26] -->
m

<!-- b003716 | ai_disclosure | pages [26] -->
m

<!-- b003717 | ai_disclosure | pages [26] -->
m

<!-- b003718 | ai_disclosure | pages [26] -->
m

<!-- b003719 | ai_disclosure | pages [26] -->
m

<!-- b003720 | ai_disclosure | pages [26] -->
m

<!-- b003721 | ai_disclosure | pages [26] -->
m

<!-- b003722 | ai_disclosure | pages [26] -->
m

<!-- b003723 | ai_disclosure | pages [26] -->
m

<!-- b003724 | ai_disclosure | pages [26] -->
m

<!-- b003725 | ai_disclosure | pages [26] -->
m

<!-- b003726 | ai_disclosure | pages [26] -->
m

<!-- b003727 | ai_disclosure | pages [26] -->
m

<!-- b003728 | ai_disclosure | pages [26] -->
m

<!-- b003729 | ai_disclosure | pages [26] -->
m

<!-- b003730 | ai_disclosure | pages [26] -->
m

<!-- b003731 | ai_disclosure | pages [26] -->
m

<!-- b003732 | ai_disclosure | pages [26] -->
m

<!-- b003733 | ai_disclosure | pages [26] -->
m

<!-- b003734 | ai_disclosure | pages [26] -->
m

<!-- b003735 | ai_disclosure | pages [26] -->
m

<!-- b003736 | ai_disclosure | pages [26] -->
m

<!-- b003737 | ai_disclosure | pages [26] -->
m

<!-- b003738 | ai_disclosure | pages [26] -->
m

<!-- b003739 | ai_disclosure | pages [26] -->
m

<!-- b003740 | ai_disclosure | pages [26] -->
m

<!-- b003741 | ai_disclosure | pages [26] -->
m

<!-- b003742 | ai_disclosure | pages [26] -->
m

<!-- b003743 | ai_disclosure | pages [26] -->
m

<!-- b003744 | ai_disclosure | pages [26] -->
m

<!-- b003745 | ai_disclosure | pages [26] -->
m

<!-- b003746 | ai_disclosure | pages [26] -->
m

<!-- b003747 | ai_disclosure | pages [26] -->
m

<!-- b003748 | ai_disclosure | pages [26] -->
m

<!-- b003749 | ai_disclosure | pages [26] -->
m

<!-- b003750 | ai_disclosure | pages [26] -->
m

<!-- b003751 | ai_disclosure | pages [26] -->
m

<!-- b003752 | ai_disclosure | pages [26] -->
m

<!-- b003753 | ai_disclosure | pages [26] -->
m

<!-- b003754 | ai_disclosure | pages [26] -->
m

<!-- b003755 | ai_disclosure | pages [26] -->
m

<!-- b003756 | ai_disclosure | pages [26] -->
m

<!-- b003757 | ai_disclosure | pages [26] -->
m

<!-- b003758 | ai_disclosure | pages [26] -->
m

<!-- b003759 | ai_disclosure | pages [26] -->
m

<!-- b003760 | ai_disclosure | pages [26] -->
m

<!-- b003761 | ai_disclosure | pages [26] -->
m

<!-- b003762 | ai_disclosure | pages [26] -->
m

<!-- b003763 | ai_disclosure | pages [26] -->
m

<!-- b003764 | ai_disclosure | pages [26] -->
m

<!-- b003765 | ai_disclosure | pages [26] -->
m

<!-- b003766 | ai_disclosure | pages [26] -->
m

<!-- b003767 | ai_disclosure | pages [26] -->
m

<!-- b003768 | ai_disclosure | pages [26] -->
m

<!-- b003769 | ai_disclosure | pages [26] -->
m

<!-- b003770 | ai_disclosure | pages [26] -->
m

<!-- b003771 | ai_disclosure | pages [26] -->
m

<!-- b003772 | ai_disclosure | pages [26] -->
m

<!-- b003773 | ai_disclosure | pages [26] -->
m

<!-- b003774 | ai_disclosure | pages [26] -->
m

<!-- b003775 | ai_disclosure | pages [26] -->
m

<!-- b003776 | ai_disclosure | pages [26] -->
m

<!-- b003777 | ai_disclosure | pages [26] -->
m

<!-- b003778 | ai_disclosure | pages [26] -->
m

<!-- b003779 | ai_disclosure | pages [26] -->
m

<!-- b003780 | ai_disclosure | pages [26] -->
m

<!-- b003781 | ai_disclosure | pages [26] -->
m

<!-- b003782 | ai_disclosure | pages [26] -->
m

<!-- b003783 | ai_disclosure | pages [26] -->
m

<!-- b003784 | ai_disclosure | pages [26] -->
m

<!-- b003785 | ai_disclosure | pages [26] -->
m

<!-- b003786 | ai_disclosure | pages [26] -->
m

<!-- b003787 | ai_disclosure | pages [26] -->
m

<!-- b003788 | ai_disclosure | pages [26] -->
m

<!-- b003789 | ai_disclosure | pages [26] -->
m

<!-- b003790 | ai_disclosure | pages [26] -->
m

<!-- b003791 | ai_disclosure | pages [26] -->
m

<!-- b003792 | ai_disclosure | pages [26] -->
m

<!-- b003793 | ai_disclosure | pages [26] -->
m

<!-- b003794 | ai_disclosure | pages [26] -->
m

<!-- b003795 | ai_disclosure | pages [26] -->
m

<!-- b003796 | ai_disclosure | pages [26] -->
m

<!-- b003797 | ai_disclosure | pages [26] -->
m

<!-- b003798 | ai_disclosure | pages [26] -->
m

<!-- b003799 | ai_disclosure | pages [26] -->
m

<!-- b003800 | ai_disclosure | pages [26] -->
m

<!-- b003801 | ai_disclosure | pages [26] -->
m

<!-- b003802 | ai_disclosure | pages [26] -->
m

<!-- b003803 | ai_disclosure | pages [26] -->
m

<!-- b003804 | ai_disclosure | pages [26] -->
m

<!-- b003805 | ai_disclosure | pages [26] -->
m

<!-- b003806 | ai_disclosure | pages [26] -->
m

<!-- b003807 | ai_disclosure | pages [26] -->
m

<!-- b003808 | ai_disclosure | pages [26] -->
m

<!-- b003809 | ai_disclosure | pages [26] -->
m

<!-- b003810 | ai_disclosure | pages [26] -->
m

<!-- b003811 | ai_disclosure | pages [26] -->
m

<!-- b003812 | ai_disclosure | pages [26] -->
m

<!-- b003813 | ai_disclosure | pages [26] -->
m

<!-- b003814 | ai_disclosure | pages [26] -->
m

<!-- b003815 | ai_disclosure | pages [26] -->
m

<!-- b003816 | ai_disclosure | pages [26] -->
m

<!-- b003817 | ai_disclosure | pages [26] -->
m

<!-- b003818 | ai_disclosure | pages [26] -->
m

<!-- b003819 | ai_disclosure | pages [26] -->
m

<!-- b003820 | ai_disclosure | pages [26] -->
m

<!-- b003821 | ai_disclosure | pages [26] -->
m

<!-- b003822 | ai_disclosure | pages [26] -->
m

<!-- b003823 | ai_disclosure | pages [26] -->
m

<!-- b003824 | ai_disclosure | pages [26] -->
m

<!-- b003825 | ai_disclosure | pages [26] -->
m

<!-- b003826 | ai_disclosure | pages [26] -->
m

<!-- b003827 | ai_disclosure | pages [26] -->
input and output variables. They support multiple input variables and benefit from

<!-- b003828 | ai_disclosure | pages [26] -->
m

<!-- b003829 | ai_disclosure | pages [26] -->
m

<!-- b003830 | ai_disclosure | pages [26] -->
m

<!-- b003831 | ai_disclosure | pages [26] -->
m

<!-- b003832 | ai_disclosure | pages [26] -->
m

<!-- b003833 | ai_disclosure | pages [26] -->
m

<!-- b003834 | ai_disclosure | pages [26] -->
m

<!-- b003835 | ai_disclosure | pages [26] -->
m

<!-- b003836 | ai_disclosure | pages [26] -->
m

<!-- b003837 | ai_disclosure | pages [26] -->
m

<!-- b003838 | ai_disclosure | pages [26] -->
m

<!-- b003839 | ai_disclosure | pages [26] -->
m

<!-- b003840 | ai_disclosure | pages [26] -->
m

<!-- b003841 | ai_disclosure | pages [26] -->
m

<!-- b003842 | ai_disclosure | pages [26] -->
m

<!-- b003843 | ai_disclosure | pages [26] -->
m

<!-- b003844 | ai_disclosure | pages [26] -->
m

<!-- b003845 | ai_disclosure | pages [26] -->
m

<!-- b003846 | ai_disclosure | pages [26] -->
m

<!-- b003847 | ai_disclosure | pages [26] -->
m

<!-- b003848 | ai_disclosure | pages [26] -->
m

<!-- b003849 | ai_disclosure | pages [26] -->
m

<!-- b003850 | ai_disclosure | pages [26] -->
m

<!-- b003851 | ai_disclosure | pages [26] -->
m

<!-- b003852 | ai_disclosure | pages [26] -->
m

<!-- b003853 | ai_disclosure | pages [26] -->
m

<!-- b003854 | ai_disclosure | pages [26] -->
m

<!-- b003855 | ai_disclosure | pages [26] -->
m

<!-- b003856 | ai_disclosure | pages [26] -->
m

<!-- b003857 | ai_disclosure | pages [26] -->
m

<!-- b003858 | ai_disclosure | pages [26] -->
m

<!-- b003859 | ai_disclosure | pages [26] -->
m

<!-- b003860 | ai_disclosure | pages [26] -->
m

<!-- b003861 | ai_disclosure | pages [26] -->
m

<!-- b003862 | ai_disclosure | pages [26] -->
m

<!-- b003863 | ai_disclosure | pages [26] -->
m

<!-- b003864 | ai_disclosure | pages [26] -->
m

<!-- b003865 | ai_disclosure | pages [26] -->
m

<!-- b003866 | ai_disclosure | pages [26] -->
m

<!-- b003867 | ai_disclosure | pages [26] -->
m

<!-- b003868 | ai_disclosure | pages [26] -->
m

<!-- b003869 | ai_disclosure | pages [26] -->
m

<!-- b003870 | ai_disclosure | pages [26] -->
m

<!-- b003871 | ai_disclosure | pages [26] -->
m

<!-- b003872 | ai_disclosure | pages [26] -->
m

<!-- b003873 | ai_disclosure | pages [26] -->
m

<!-- b003874 | ai_disclosure | pages [26] -->
m

<!-- b003875 | ai_disclosure | pages [26] -->
m

<!-- b003876 | ai_disclosure | pages [26] -->
m

<!-- b003877 | ai_disclosure | pages [26] -->
m

<!-- b003878 | ai_disclosure | pages [26] -->
m

<!-- b003879 | ai_disclosure | pages [26] -->
m

<!-- b003880 | ai_disclosure | pages [26] -->
m

<!-- b003881 | ai_disclosure | pages [26] -->
m

<!-- b003882 | ai_disclosure | pages [26] -->
m

<!-- b003883 | ai_disclosure | pages [26] -->
m

<!-- b003884 | ai_disclosure | pages [26] -->
m

<!-- b003885 | ai_disclosure | pages [26] -->
m

<!-- b003886 | ai_disclosure | pages [26] -->
m

<!-- b003887 | ai_disclosure | pages [26] -->
m

<!-- b003888 | ai_disclosure | pages [26] -->
m

<!-- b003889 | ai_disclosure | pages [26] -->
m

<!-- b003890 | ai_disclosure | pages [26] -->
m

<!-- b003891 | ai_disclosure | pages [26] -->
m

<!-- b003892 | ai_disclosure | pages [26] -->
m

<!-- b003893 | ai_disclosure | pages [26] -->
m

<!-- b003894 | ai_disclosure | pages [26] -->
m

<!-- b003895 | ai_disclosure | pages [26] -->
m

<!-- b003896 | ai_disclosure | pages [26] -->
m

<!-- b003897 | ai_disclosure | pages [26] -->
m

<!-- b003898 | ai_disclosure | pages [26] -->
m

<!-- b003899 | ai_disclosure | pages [26] -->
m

<!-- b003900 | ai_disclosure | pages [26] -->
m

<!-- b003901 | ai_disclosure | pages [26] -->
m

<!-- b003902 | ai_disclosure | pages [26] -->
m

<!-- b003903 | ai_disclosure | pages [26] -->
m

<!-- b003904 | ai_disclosure | pages [26] -->
m

<!-- b003905 | ai_disclosure | pages [26] -->
m

<!-- b003906 | ai_disclosure | pages [26] -->
m

<!-- b003907 | ai_disclosure | pages [26] -->
m

<!-- b003908 | ai_disclosure | pages [26] -->
m

<!-- b003909 | ai_disclosure | pages [26] -->
m

<!-- b003910 | ai_disclosure | pages [26] -->
m

<!-- b003911 | ai_disclosure | pages [26] -->
m

<!-- b003912 | ai_disclosure | pages [26] -->
m

<!-- b003913 | ai_disclosure | pages [26] -->
m

<!-- b003914 | ai_disclosure | pages [26] -->
m

<!-- b003915 | ai_disclosure | pages [26] -->
m

<!-- b003916 | ai_disclosure | pages [26] -->
m

<!-- b003917 | ai_disclosure | pages [26] -->
m

<!-- b003918 | ai_disclosure | pages [26] -->
m

<!-- b003919 | ai_disclosure | pages [26] -->
m

<!-- b003920 | ai_disclosure | pages [26] -->
m

<!-- b003921 | ai_disclosure | pages [26] -->
m

<!-- b003922 | ai_disclosure | pages [26] -->
m

<!-- b003923 | ai_disclosure | pages [26] -->
m

<!-- b003924 | ai_disclosure | pages [26] -->
m

<!-- b003925 | ai_disclosure | pages [26] -->
m

<!-- b003926 | ai_disclosure | pages [26] -->
m

<!-- b003927 | ai_disclosure | pages [26] -->
m

<!-- b003928 | ai_disclosure | pages [26] -->
m

<!-- b003929 | ai_disclosure | pages [26] -->
m

<!-- b003930 | ai_disclosure | pages [26] -->
m

<!-- b003931 | ai_disclosure | pages [26] -->
m

<!-- b003932 | ai_disclosure | pages [26] -->
m

<!-- b003933 | ai_disclosure | pages [26] -->
m

<!-- b003934 | ai_disclosure | pages [26] -->
m

<!-- b003935 | ai_disclosure | pages [26] -->
m

<!-- b003936 | ai_disclosure | pages [26] -->
m

<!-- b003937 | ai_disclosure | pages [26] -->
m

<!-- b003938 | ai_disclosure | pages [26] -->
m

<!-- b003939 | ai_disclosure | pages [26] -->
m

<!-- b003940 | ai_disclosure | pages [26] -->
m

<!-- b003941 | ai_disclosure | pages [26] -->
m

<!-- b003942 | ai_disclosure | pages [26] -->
m

<!-- b003943 | ai_disclosure | pages [26] -->
m

<!-- b003944 | ai_disclosure | pages [26] -->
m

<!-- b003945 | ai_disclosure | pages [26] -->
m

<!-- b003946 | ai_disclosure | pages [26] -->
m

<!-- b003947 | ai_disclosure | pages [26] -->
m

<!-- b003948 | ai_disclosure | pages [26] -->
m

<!-- b003949 | ai_disclosure | pages [26] -->
m

<!-- b003950 | ai_disclosure | pages [26] -->
m

<!-- b003951 | ai_disclosure | pages [26] -->
m

<!-- b003952 | ai_disclosure | pages [26] -->
m

<!-- b003953 | ai_disclosure | pages [26] -->
m

<!-- b003954 | ai_disclosure | pages [26] -->
m

<!-- b003955 | ai_disclosure | pages [26] -->
m

<!-- b003956 | ai_disclosure | pages [26] -->
m

<!-- b003957 | ai_disclosure | pages [26] -->
m

<!-- b003958 | ai_disclosure | pages [26] -->
m

<!-- b003959 | ai_disclosure | pages [26] -->
m

<!-- b003960 | ai_disclosure | pages [26] -->
m

<!-- b003961 | ai_disclosure | pages [26] -->
m

<!-- b003962 | ai_disclosure | pages [26] -->
m

<!-- b003963 | ai_disclosure | pages [26] -->
m

<!-- b003964 | ai_disclosure | pages [26] -->
m

<!-- b003965 | ai_disclosure | pages [26] -->
m

<!-- b003966 | ai_disclosure | pages [26] -->
m

<!-- b003967 | ai_disclosure | pages [26] -->
m

<!-- b003968 | ai_disclosure | pages [26] -->
m

<!-- b003969 | ai_disclosure | pages [26] -->
m

<!-- b003970 | ai_disclosure | pages [26] -->
m

<!-- b003971 | ai_disclosure | pages [26] -->
m

<!-- b003972 | ai_disclosure | pages [26] -->
m

<!-- b003973 | ai_disclosure | pages [26] -->
m

<!-- b003974 | ai_disclosure | pages [26] -->
preprocessing techniques like normalization to improve performance. However,

<!-- b003975 | ai_disclosure | pages [26] -->
m

<!-- b003976 | ai_disclosure | pages [26] -->
m

<!-- b003977 | ai_disclosure | pages [26] -->
m

<!-- b003978 | ai_disclosure | pages [26] -->
m

<!-- b003979 | ai_disclosure | pages [26] -->
m

<!-- b003980 | ai_disclosure | pages [26] -->
m

<!-- b003981 | ai_disclosure | pages [26] -->
m

<!-- b003982 | ai_disclosure | pages [26] -->
m

<!-- b003983 | ai_disclosure | pages [26] -->
m

<!-- b003984 | ai_disclosure | pages [26] -->
m

<!-- b003985 | ai_disclosure | pages [26] -->
m

<!-- b003986 | ai_disclosure | pages [26] -->
m

<!-- b003987 | ai_disclosure | pages [26] -->
m

<!-- b003988 | ai_disclosure | pages [26] -->
m

<!-- b003989 | ai_disclosure | pages [26] -->
m

<!-- b003990 | ai_disclosure | pages [26] -->
m

<!-- b003991 | ai_disclosure | pages [26] -->
m

<!-- b003992 | ai_disclosure | pages [26] -->
m

<!-- b003993 | ai_disclosure | pages [26] -->
m

<!-- b003994 | ai_disclosure | pages [26] -->
m

<!-- b003995 | ai_disclosure | pages [26] -->
m

<!-- b003996 | ai_disclosure | pages [26] -->
m

<!-- b003997 | ai_disclosure | pages [26] -->
m

<!-- b003998 | ai_disclosure | pages [26] -->
m

<!-- b003999 | ai_disclosure | pages [26] -->
m

<!-- b004000 | ai_disclosure | pages [26] -->
while MLR is a statistical model that assumes linear relationships and offers inter-

<!-- b004001 | ai_disclosure | pages [26] -->
pretability through coefficients, FNN is a computational model capable of learning

<!-- b004002 | ai_disclosure | pages [26] -->
non-linear and complex patterns, often regarded as a ”black box.” MLR is simpler,

<!-- b004003 | ai_disclosure | pages [26] -->
requiring fewer data points and involving direct analytical solutions, whereas FNN is

<!-- b004004 | ai_disclosure | pages [26] -->
more flexible but computationally intensive, relying on iterative optimization meth-

<!-- b004005 | ai_disclosure | pages [26] -->
ods like backpropagation.>

<!-- b004006 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b004007 | furniture | pages [26] -->
2

<!-- b004008 | furniture | pages [26] -->
MATHmodels

<!-- b004009 | furniture | pages [26] -->
获取更多资讯
