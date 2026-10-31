# P-C-2025-2522820-7a254095

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
2522820

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
The Best of the Best: Olympic Medal Tables

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Winning at the Olympics is the pinnacle of physical achievement for any athlete. It is an honor to even be invited to the Olympics, and it is a global spectacle for weeks to see the best athletes of the modern age compete to be the best in the world in a large variety of sports. As developing countries rise in the athletic scene, we are seeing a large increase in the number of participants and countries who achieve their first Olympic medal despite

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
multitudes more setbacks than traditionally competing countries.

<!-- b000013 | prose | pages [1] -->
As modelers, we have been tasked with predicting the outcome of the 2028 Summer Olympics held in Los Angeles, United States. Olympic medal data exhibits censorship in the form of zero inflation, so we first consider a Tobit Model that considers random noise and unobserved random effects, optimized with a Maximum Likelihood Estimate. From regression analysis on the Tobit Model, we discovered it suffered from heteroscedasticity, which is detrimental to the Tobit model. So, we implement a Hierarchical Mixed Linear Effects Model to predict medal counts based on Host Status, Number of Athletes, and Past Performance. Country performance was split into clusters using Density-Based Spatial Clustering of Applications with Noise (DBSCAN), splitting the countries into three clusters. The Mixed Linear Effects Model is then used to perform a Negative Binomial Regression based on the predictors, as well as a Probit Regression in the low-performing cluster to determine probability of earning 0 medals.

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
We predicted the Top 3 (in gold count) countries in the 2028 Summer Olympics to be the United States (48), Germany (28), and China (25), each with a 95% confidence interval range of around 30. The top three countries that we predict will improve the most in terms of ranking is Jamaica (+27), Germany (+8), and Ukraine (+8), and the worst performance changes in ranking we predict are Canada (-99), the Netherlands (-31), and South Korea (-10). Finally, our model also predicts that the countries that will earn their first Olympic medal in 2028 are Angola and Saar, with odds of 32.54% and 40.08%, respectively.

<!-- b000016 | prose | pages [1] -->
After analyzing the dynamics of the rankings, we wanted to understand the impact of events and sports on the rankings. To do this, we created a ranking system of Gold 6 points, Silver 3 Points, and Bronze 2 points. Then, through Singular Value Decomposition, Sport-Point Efficiency, and Revealed Comparative Advantage, we were able to understand the influence sports and events had on the ranking of various countries.

<!-- b000017 | prose | pages [1] -->
We also analyzed past performances at the Games to identify possible instances of the great coach effect, or the influence of a great coach in leading teams to anomalous successes. To build our model, we noticed that performances at the Games are time series, so we used a time series analysis incorporating a moving average. We found that the 1976 Romanian Handball team, the 2008 Canadian trampolining team, and the 2000 Russian diving team were the most likely to have experienced the great coach effect.

<!-- b000018 | prose | pages [1] -->
By using a contribution metric, we used the same model to find the country-sport pairs where the great coach effect was likely to have made the greatest impact on the country’s performance. We found that the 1992-2012 Swedish handball teams, the 1984-2004 United States synchronized swimming teams, and the 2000-2016 Russian modern pentathlon athletes likely benefited the most from the great coach effect, with the Swedish handball and United States synchronized swimming athletes earning 100% of their medals during segments where they were led by great coaches, according to our model. Similarly, by using a relative contribution metric, we suggested that Russia invest in a great weightlifting coach, China invest in a great trampolining coach, and Hungary invest in a great weightlifting coach. Based on their performances under great coaches, these investments could lead to up to 20 points for Russia, 14 points for China, and 6.8 points for Hungary.

<!-- b000019 | prose | pages [1] -->
All of these results were cross-referenced with historical Olympic coaches, and many of our findings lined up with the leadership of coaches that may be considered great.

<!-- b000020 | prose | pages [1] -->
There are a multitude of benefits in this research—such as understanding how to best allocate resources—but more than that, just as the Games represent the human desire for unity in excellence, these models represent our fundamental desire to understand the world.

<!-- b000021 | furniture | pages [2] -->
Team 2522820

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
模型

<!-- b000024 | heading | pages [2] -->
Introduction

<!-- b000025 | prose | pages [2] -->
3 1

<!-- b000026 | heading | pages [2] -->
1.1 Problem Restatement

<!-- b000027 | prose | pages [2] -->
3

<!-- b000028 | prose | pages [2] -->
Data Pre-Processing 3 2

<!-- b000029 | prose | pages [2] -->
Problem 1: Medal Forecasting 4 3 4 Variable Definitions 3.1 5 3.2

<!-- b000030 | heading | pages [2] -->
General Assumptions

<!-- b000031 | prose | pages [2] -->
3.3

<!-- b000032 | heading | pages [2] -->
Tobit Model

<!-- b000033 | prose | pages [2] -->
5 6 3.3.1 Maximum Likelihood Estimate (MLE) 3.3.2 7 Predictor Analysis and Issues with Tobit .

<!-- b000034 | heading | pages [2] -->
Mixed Linear Models (MLMs) in a Hierarchical Framework

<!-- b000035 | prose | pages [2] -->
3.4 8 3.4.1 Clusters with DBSCAN 8 3.4.2

<!-- b000036 | heading | pages [2] -->
Mixed Linear Models and Hurdle Model

<!-- b000037 | prose | pages [2] -->
9 3.4.3

<!-- b000038 | heading | pages [2] -->
Results, Model Fit, and Uncertainty

<!-- b000039 | prose | pages [2] -->
10 3.5 Projections for Countries Yet to Earn Medals 11 11 3.6 Analyzing Impacts of Events and Sports IImO

<!-- b000040 | heading | pages [2] -->
Data Processing (Ceiling-Proportion Approximation)

<!-- b000041 | prose | pages [2] -->
12 3.6.1 3.6.2 14

<!-- b000042 | heading | pages [2] -->
Data Processing (Event Limitation Approximation)

<!-- b000043 | prose | pages [2] -->
3.6.3 15 Selecting a Processing Method 3.6.4 15 Event Impact: Singular Value Decomposition (SVD) 3.6.5 Analyzing Impact of Sports 15 3.6.6 Home Country Effects 18

<!-- b000044 | prose | pages [2] -->
Problem 2: Detecting and Utilizing the Great Coach Effect 18 4

<!-- b000045 | heading | pages [2] -->
4.1 Detecting the Great Coach Effect .

<!-- b000046 | prose | pages [2] -->
18

<!-- b000047 | heading | pages [2] -->
4.1.1Time Series Analysis Setup

<!-- b000048 | prose | pages [2] -->
19 Variable Definitions 19 4.1.2 20

<!-- b000049 | heading | pages [2] -->
4.1.3Results and Notable Findings

<!-- b000050 | heading | pages [2] -->
4.2 Estimating Impacts of Great Coaches

<!-- b000051 | prose | pages [2] -->
21 22 Identifying Country-Sport Pairs Fit for Great Coaches and Estimating Impacts 4.3

<!-- b000052 | prose | pages [2] -->
Problem 3: Insights into Olympic Medal Counts 22 5

<!-- b000053 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000054 | prose | pages [2] -->
23 6

<!-- b000055 | heading | pages [2] -->
Hierarchical Regression Model

<!-- b000056 | prose | pages [2] -->
6.1 23

<!-- b000057 | heading | pages [2] -->
Time Series Analysis with Moving Average Model

<!-- b000058 | prose | pages [2] -->
23 6.2

<!-- b000059 | heading | pages [2] -->
Conclusion

<!-- b000060 | prose | pages [2] -->
24 7

<!-- b000061 | heading | pages [2] -->
Works Cited

<!-- b000062 | references | pages [2] -->
25

<!-- b000063 | references | pages [2] -->
8

<!-- b000064 | references | pages [2] -->
关注数学模型

<!-- b000065 | furniture | pages [2] -->
获取更多资讯

<!-- b000066 | furniture | pages [3] -->
Team 2522820

<!-- b000067 | furniture | pages [3] -->
Page 3

<!-- b000068 | heading | pages [3] -->
1 Introduction

<!-- b000069 | prose | pages [3] -->
“The Olympics remain the most compelling search for excellence that exists in sport, and maybe in life itself.” —Dawn Fraser, eight-time Olympic medalist.

<!-- b000070 | prose | pages [3] -->
The Olympic tradition traces back almost three millennia to Olympia in Ancient Greece. Even in an era of 微信公众号：数学模型 constant conflict between the city-states, the ancient Games represented humanity’s unified pursuit of excellence. The Ancient Greeks even established a temporary Olympic Truce to ensure the safety of the athletes: unity in competition took precedence.[1] The modern Olympic Games, established in 1896, have inherited this humanistic spirit. The modern Games have gathered the best athletes from around the world in their common pursuit not just of athletic excellence, but of reaching the limits of human potential and bringing our culturally diverse world closer together in the process. The models we present in this paper aim to understand the factors behind these competitions.

<!-- b000071 | heading | pages [3] -->
1.1 Problem Restatement

<!-- b000072 | prose | pages [3] -->
1. (a) Predict the medal table for the Los Angeles 2028 Summer Olympics. Provide prediction intervals for 微信号：MATHmodels all medal predictions, and predict which countries will improve the most and worsen the most based on their 2024 performance.

<!-- b000073 | prose | pages [3] -->
(b) Then, predict which countries will earn their first Olympic medal ever in the 2028 Olympics, providing odds for the estimate.

<!-- b000074 | prose | pages [3] -->
(c) Consider how different sports and sports specialties play into country performance in a given Olympics and explore how events chosen by hosting countries affect results.

<!-- b000075 | prose | pages [3] -->
2. (a) Create a mathematical model that finds potential cases of the “great coach effect,” or the positive influence of a great coach on a country’s performance in a discipline.

<!-- b000076 | prose | pages [3] -->
(b) Use this model to estimate the impact of such potential great coaches on their countries’ performances.

<!-- b000077 | prose | pages [3] -->
(c) Interpret the results of this model to identify three country-sport pairs that great coaches would bring most value to, and estimate the potential impact of hiring great coaches for these three country-sport pairs.

<!-- b000078 | prose | pages [3] -->
3. (a) Discuss original insights about Olympic medal counts, and explain how these insights can be used to inform Olympic Committee decisions for future Olympics.

<!-- b000079 | heading | pages [3] -->
2 Data Pre-Processing

<!-- b000080 | prose | pages [3] -->
To easily analyze the given data, the CSV files datasets given by the International Olympic Committee (IOC) were converted to SQLite tables. Using Python 3, we were able to easily request, insert, and update relevant information provided by the IOC.

<!-- b000081 | prose | pages [3] -->
Before using any of the given datasets, we adjusted some of the files for easy processing.

<!-- b000082 | prose | pages [3] -->
• summerOly athletes.csv - From 1896 to 2024, many countries changed their official names. This is reflected within the [Team] column of this CSV. To account for naming discrepancies, the [Name of Country (NOC)] column was utilized. The three-letter NOC code was consistent throughout the sheet, so a dictionary of {code : country} was used to associate the NOC code with the country name.

<!-- b000083 | prose | pages [3, 4] -->
• summerOly medal counts.csv - Due to minor discrepancies in spacing and naming conventions, slight changes were made to country names for convenience. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • summerOly_hosts.csv - Due to minor discrepancies in the naming conventions, slight changes were made to the host names for convenience.

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

<!-- b000408 | furniture | pages [4] -->
Page 4

<!-- b000409 | furniture | pages [4] -->
Team 2522820

<!-- b000411 | prose | pages [4] -->
• summerOly_programs.csv - For all columns that began with a year, all empty cells and non-numerical cells were filled with 0. Those columns otherwise indicated the discontinuation of sports; however, a 0 would likewise indicate that an event is not being offered. This was more convenient for setting up our SQLite table.

<!-- b000412 | heading | pages [4] -->
3 Problem 1: Medal Forecasting

<!-- b000413 | prose | pages [4] -->
We are tasked with forecasting the total medal counts and gold medal counts for countries in the 2028 Summer Olympics. Given past data since 1896 of country performance in terms of medal counts, broken down into gold, silver, and bronze, as well as athletes in each event, it is reasonable to frame this as a regression problem.

<!-- b000414 | prose | pages [4] -->
The factors we believe can be used to predict performance are Host Status, Number of Athletes, and Past Performance. Host Status can be directly obtained from the given data. We will also consider if host status has some residual effect on country performance, so if a country is set to host in 4 years or hosted 4 years prior, it is possible this has an effect on performance as that country will put more funds into preparing competitors. Number of Athletes and past performance (in terms of medal counts) can also be directly obtained from the given data. Obviously, there are other factors that can have a major effect such as the amount of money a country puts into training Olympic competitors, but this is data we do not have access to.

<!-- b000415 | prose | pages [4] -->
If we tried direct regression on the data, we'd run into some interesting issues. By nature, it is impossible for countries to win less than 0 medals at the Games. We are attempting to use regression to predict future performance, and thus forecast the skill of a country's competitors. There is an overwhelming number of zeroes in the dataset, but these zeroes represent countries at very different skill levels. A country could be capable but simply unable to break into 3rd place at any events, or it could be placing last at every event it participates in. This means our data is censored with a lower bound of 0, and this is something we must take into account when performing regression.

<!-- b000416 | prose | pages [4] -->
From our literature review, a Tobit model has been historically used and verified to predict Olympic medal counts. Besides using it to compare with previous models, a Tobit model is also fitting as it assumes the driving mechanism(s) that determine if a country wins medals affects how many medals they win in the same fashion.[2] Therefore, in line with previous research, we will first consider a Tobit model with our predictors.

<!-- b000417 | heading | pages [4] -->
3.1 Variable Definitions

<!-- b000418 | caption | pages [4] -->
Table 1: Variable definitions

<!-- b000419 | prose | pages [4] -->
Variable Definition Observed Variable y y* Latent Variable (on censored data) X Predictor Data Matrix β Vector of Linear Combination Coefficients for X Error term (€ ∼ N(0, σ2)) € Standard Deviation of Error σ Random Noise Standard Deviation σn Unobserved Random Effects Standard Deviation σu L(β, σ) Likelihood Function P(A|B) Probability of event A given event B (P is the probability measure)

<!-- b000420 | prose | pages [4, 5] -->
关注数学模型 微信公众号：数学模型 Φ Standard Normal Cumulative Density Function (CDF) ϕ Standard Normal Probability Density Function (PDF) ℓ(β, σ) Observed Variable ti T-statistic SE( ˆβi) Standard Error of Fitted Coefficient ˆβi µ Mean for Negative Binomial Distribution θ Dispersion Factor for Negative Binomial Distribution Z Random Effects Design Matrix b Vector of Linear Combination Coefficients for Z ˆy Predicted y value 微信号：MATHmodels

<!-- b000421 | furniture | pages [4] -->
获取更多资讯

<!-- b000422 | furniture | pages [5] -->
Team 2522820

<!-- b000423 | furniture | pages [5] -->
Page 5

<!-- b000425 | heading | pages [5] -->
3.2 General Assumptions

<!-- b000426 | prose | pages [5] -->
1. We assume that the provided data is fully accurate to the results of the Olympics each year.

<!-- b000427 | prose | pages [5] -->
Justification: We plan on using regression to predict the 2028 results, and this regression will be usable only if the data we apply it to is accurate.

<!-- b000428 | heading | pages [5] -->
2. We assume that country performance can be reasonably estimated using predictive factors associated

<!-- b000429 | prose | pages [5] -->
with Host Status, Number of Athletes, and Past Performance.

<!-- b000430 | prose | pages [5] -->
Justification: We have access to limited data for this problem, and do not have access to (for example) expenditures on Olympic training. Therefore, we should be able to use the data presented to us to predict performance, and these are the main factors that we can extract from the data tables that we think can predict performance.

<!-- b000431 | prose | pages [5] -->
3. We assume that the participating countries in the 2028 Summer Olympics are identical to that in the 2024 Olympics.

<!-- b000432 | prose | pages [5] -->
Justification: We do not have data on participating countries in the 2028 Olympics, so we assume all countries that participated in 2024 will also participate (with the exception of Russia, which has had some controversy about participation due to the Ukraine War).

<!-- b000433 | heading | pages [5] -->
3.3 Tobit Model

<!-- b000434 | prose | pages [5] -->
The Tobit model accounts for censorship by predicting a latent variable, y∗, instead of directly predicting the observed variable y with the given predictors and previous data. The values y∗and y are related as follows:

<!-- b000435 | prose | pages [5] -->
( if y∗≤0, 0 y = y∗ if y∗> 0.

<!-- b000436 | prose | pages [5] -->
The Tobit model attempts to predict the uncensored data itself given only censored data. This fits the framework of Olympic medal counts since, as discussed, zero medal counts can be thought of as censored data. The Tobit model assumes this relationship can be captured from the predictors linearly with the equation

<!-- b000437 | prose | pages [5] -->
y∗= Xβ + ϵ

<!-- b000438 | prose | pages [5] -->
Where X is a matrix with the predictor data and β is a column vector of coefficients (so Xβ is some linear combination of the predictor variables) and ϵ is an error term which is normally distributed with variance σ2.

<!-- b000439 | furniture | pages [6] -->
Team 2522820

<!-- b000440 | furniture | pages [6] -->
Page 6

<!-- b000441 | prose | pages [6] -->
This is usually written as ϵ ∼N(0, σ2). Since our data is limited, we expect that there are discrepancies between what they can predict given the complicated nature of why countries win olympic medals. Generally, ϵ is usually used as a ’noise’ term, but in our implementation we extend this to account for unobserved random effects. To do this, we have both σn (noise) and σu (unobserved effects) that contribute to the variance of ϵ as follows:

<!-- b000442 | prose | pages [6] -->
σ2 = σ2 n + σ2 u.

<!-- b000443 | prose | pages [6] -->
This ensures that we can capture unobserved effects from factors that we cannot add into linear predictors. From here, our implementation of the Tobit model fits coefficients in β based on previous data to be able to predict y∗ given predictors X.

<!-- b000444 | heading | pages [6] -->
3.3.1 Maximum Likelihood Estimate (MLE)

<!-- b000445 | prose | pages [6] -->
Our implementation of the Tobit Model optimizes fit using the Maximum Likelihood Estimate (MLE), which is standard for Tobit models since it can account for both observed and unobserved (censored) parts of the data. Essentially, MLE aims to maximize the likelihood function, which is the probability that y is observed given values of β and σ. Maximizing the likelihood means the fitted coefficients for β and σ yield the largest probability of the actual observed data being observed, which allows us to accurately predict y∗given only predictors X.

<!-- b000446 | prose | pages [6] -->
L(β, σ) = P(y|β, σ)

<!-- b000447 | prose | pages [6] -->
Across many observations (yi) this becomes

<!-- b000448 | prose | pages [6] -->
n Y L(β, σ) = P(y1, y2, . . . yn|β, σ) = P(yi|β, σ) i=1

<!-- b000449 | prose | pages [6] -->
The likelihood function can then be split up into values where yi = 0 (censored) and yi > 0 (uncensored). The Tobit model generally assumes y∗is normally distributed, which is a restricting assumption but can be altered if necessary. When yi = 0, we want to compute P(yi = 0|β, σ) = P(y∗≤0|β, σ), which can be found with the normal cumulative density function (CDF), Φ. When yi > 0, we just want P(y∗= yi|β, σ), which can be found with the normal probability density function (PDF), ϕ. Mathematically this becomes

<!-- b000450 | prose | pages [6] -->
−Xiβ  P(y∗≤0|β, σ) = Φ σ yi −Xiβ  P(y∗= yi|β, σ) = ϕ σ n −Xiβ  Y yi −Xiβ  Y Y =⇒ P(yi|β, σ) = Φ ϕ . σ σ yi=0 yi>0 i=1

<!-- b000451 | prose | pages [6] -->
Aiming to maximize, it helps to take the logarithm of the likelihood function. This helps the function in terms of differentiability (to be maximized), and whatever maximum is achieved for the log of the likelihood function will correspond to a maximum of the likelihood function itself.

<!-- b000452 | prose | pages [6] -->
 yi −Xiβ   0 −Xiβ  X X ℓ(β, σ) = log(L(β, σ)) = log ϕ + log Φ σ σ yi>0 yi=0

<!-- b000453 | prose | pages [6] -->
Maximizing this (using various numerical methods) give us fitted parameters β and σ for the Tobit model.

<!-- b000454 | prose | pages [6] -->
关注数学模型

<!-- b000455 | furniture | pages [6] -->
2

<!-- b000456 | furniture | pages [6] -->
MATHmodels

<!-- b000457 | furniture | pages [6] -->
获取更多资讯

<!-- b000458 | furniture | pages [7] -->
Team 2522820

<!-- b000459 | furniture | pages [7] -->
Page 7

<!-- b000460 | heading | pages [7] -->
3.3.2 Predictor Analysis and Issues with Tobit

<!-- b000461 | prose | pages [7] -->
We are given limited data on countries to make this prediction, namely only past performance, number of athletes, and host status. Therefore, it is important that we figure out which are influential/significant in predicting medal count. For each year, we first consider the variables Host Status, Num Athletes, Host 4 Years Ago, Host in 4 Years, Past 4 Years Total Medals, and Past 8 Years Total Medals. The Host Status variables 微信公众号：数学模型 are implemented as binary components. It’s reasonable to think that host status can have a delayed or anticipatory effect, as host countries can prepare for hosting by training their athletes and increasing funding to a higher level than usual. We consider past performance as the last two Olympic performances, since these are likely most indicative of future performance rather than performances further in the past.

<!-- b000462 | prose | pages [7] -->
First, we check for multicollinearity. If two predictors are highly correlated, it’s not very useful to use them both so we can either combine them or only use one. We check this with a heat map of a correlation matrix between predictors over all country performances. We can see a high correlation between Past 4 Years Total Medals and Past 8 Years Total Medals and also Num Athletes in the bottom right 3×3 square. Otherwise, there is not a high correlation with other predictors.

<!-- b000463 | prose | pages [7] -->
Another thing we must check, especially for the Tobit model, is homoscedasticity. The Tobit model relies 微信号：MATHmodels on the assumption of homoscedasticity, which means that the variance of the residuals is constant, which can be checked in a residual plot as in Figure 1. As we can see, the variance of the residuals is not constant, so we have a heteroscedastic error. The reason this is an issue is because after fitting our variance for the error term σ, we are assuming error terms follow a constant variance, however we see here that this is not the case. This is particularly bad for the Tobit model since it can make the probability of censoring (getting 0 medals) very inaccurate.

<!-- b000464 | caption | pages [7] -->
Figure 1: Predictor/Regression Analysis

<!-- b000465 | prose | pages [7] -->
Further, we perform regression analysis to see which predictors are most significant. After fitting, each variable gets a T-Stat and p-value, defined as

<!-- b000466 | prose | pages [7] -->
ˆβi ti = SE( ˆβi)

<!-- b000467 | prose | pages [7, 8] -->
Here, βi is the fitted parameter for predictor i and SE(βi) is the standard error, or an uncertainty metric for βi (which can be computed in a few ways, we used the covariance matrix).The p-value is calculated using the t-statistic and the degrees of freedom (excess data to predict on), and it is essentially the probability of that t-statistic being obtained. To determine a statistically significant predictor, it should have a low p-value, generally we want p ≤.05. As we can see, the predictors that have this are Num Athletes, Host in 4 Years, and Past 4 Years Total Medals. From this, we can reasonably eliminate Past 8 Years Total Medals due to multicollinearity and low statistical significance and Host 4 Years Ago for low statistical significance. Though Host Status isn’t statistically significant in this analysis, we may still consider it in the model improvement to see if anything has changed.

<!-- b000468 | furniture | pages [8] -->
Team 2522820

<!-- b000469 | furniture | pages [8] -->
Page 8

<!-- b000471 | prose | pages [8] -->
Variable Coefficient T-Stat P-Value Host Status -4.370 -0.642 0.521 Num Athletes 18.356 17.246 0.00 Host 4 Years Ago 0.092 0.000 0.99 Host in 4 Years -13.225 -12.608 0.00 Past 4 Years Total Medals 3.733 3.683 0.00023 Past 8 Years Total Medals 0.453 0.003 .997

<!-- b000472 | caption | pages [8] -->
Table 2: Regression Analysis Results

<!-- b000473 | heading | pages [8] -->
3.4 Mixed Linear Models (MLMs) in a Hierarchical Framework

<!-- b000474 | prose | pages [8] -->
We intend to refine the Tobit model by attempting to account for differing levels of variance. The purpose of the random variable is to account for unobserved effects, and there’s no reason to assume this is the same across all countries (in fact, that is quite a bad assumption). We decided to fix this by splitting countries into clusters based on general performance, including separate random variables for each cluster as well as each individual country. This is done in attempt to capture important effects on a country-level and cluster-level scale. These underlying effects could possibly be socioeconomic or geographic, for example low performance can be due to countries that do not have the money to put towards Olympic training.

<!-- b000475 | heading | pages [8] -->
3.4.1 Clusters with DBSCAN

<!-- b000476 | prose | pages [8] -->
First, to form clusters, we used a Density-Based Spatial Clustering of Applications with Noise (DBSCAN) model. DBSCAN is a useful method for us since it specifically designates outliers (noise) as high performing countries are in this data. To get a general metric for country performance, we define ’Points’ as a weighted sum of the number of Gold, Silver, and Bronze medals, with weights 6, 3, and 2 respectively. All weightings are arbitrary—different reputable sources use different weighting systems—but we decided to use this weighting because, to some extent, it has a natural justification, as it follows Zipf’s law. That is,

<!-- b000477 | prose | pages [8] -->
Points = 6 · Gold + 3 · Silver + 2 · Bronze.

<!-- b000478 | prose | pages [8] -->
Then, countries are ranked by their average number of points over the years they competed. The DBSCAN algorithm takes two inputs: eps and min points. min points is the minimum number of points that can be in a cluster, and eps is a distance threshold to define a neighborhood around a ’core points’. A core point has at least min points within distance eps of it, and boundary points to each cluster are points within eps of a core point. DBSCAN algorithmically goes through all points and forms clusters.

<!-- b000479 | prose | pages [8] -->
We wanted to split countries into clusters large enough to perform regression on but also have enough clusters to model some inter-cluster unobserved effect difference. In the end, we decided on 3 clusters (including outliers). Our code took min points = 8 and with a target number of (non-outlier) clusters of 2, we found a fitting eps value through iteration shown in Figure 2.

<!-- b000480 | prose | pages [8] -->
After finding the clusters, we applied a Mixed Effects Linear Model to each cluster, taking special care of Cluster 1 (which included all of the countries that get close to 0 medals).

<!-- b000481 | prose | pages [8, 9] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000482 | furniture | pages [8] -->
2

<!-- b000483 | furniture | pages [8] -->
MATHmodels

<!-- b000484 | furniture | pages [8] -->
获取更多资讯

<!-- b000485 | furniture | pages [9] -->
Team 2522820

<!-- b000486 | furniture | pages [9] -->
Page 9

<!-- b000488 | caption | pages [9] -->
Figure 2: DBSCAN Cluster Results

<!-- b000489 | heading | pages [9] -->
3.4.2 Mixed Linear Models and Hurdle Model

<!-- b000490 | prose | pages [9] -->
We will first describe the model for clusters 0 and -1, then for cluster 1. The Tobit model was a continuous regression model, however since medal counts are discrete we chose to use a Negative Binomial Regression. A Negative Binomial distribution is chosen over a Poisson since the Negative Binomial can account for cases where the variance is greater than the meain (Poisson is too restrictive). For countries in these clusters, we assumed there was close to negligible chance of them getting 0 medals. The Mixed Effects Model takes the following form:

<!-- b000491 | prose | pages [9] -->
yij ∼NBinom(µij, θ) µij = exp(Xijβj + Zijbj)

<!-- b000492 | prose | pages [9] -->
Here i is the index for individual country and j is the index for cluster. θ is a dispersion factor for the negative Now, Zijbj is implementing group-wise random effects for each binomial distribution that is also fitted. parameter in attempt to reduce heteroscedasticity (though this model suffers less from it since we are using Negative Binomial). bj is a vector of random coefficients to apply to each cluster, and these random terms are normally distributed. The matrix Zij is the random-effects design matrix, with predictor inputs that get multiplied with the random effects variables in bj (so Zij is similar to Xij in this manner). This is a ’mixed’ effects model as Xijβj is the fixed part and Zijbj is the random part of the model. Cluster 0 and -1 were fitted this way, with a slightly different process for Cluster 1.

<!-- b000493 | prose | pages [9] -->
The purpose of choosing the Tobit model was to account for censorship, but another way to deal with this is a Hurdle model. It is very similar, first using binary regression (Probit) to determine the probability a country gets 0 medals, and then a Negative Binomial model as previously described for the positive count model. The random effects modeling is identical for the Probit regression, but instead a different link function is used. This is implemented mathematically as follows:

<!-- b000494 | prose | pages [9] -->
P(Yij = 1|Xij, Zij) = Φ(Xijβj + Zijbj)

<!-- b000495 | prose | pages [9, 10] -->
The value P(Yij = 1) is what we are trying to predict in the binary regression (the probability a country gets any medals at all), and we take the cumulative normal distribution of the linear predictor for the probit model. In these mixed linear effects models, it’s useful to think of a link function that relates the linear predictor to the desired value. In the probit model, the link is the inverse CDF, and in the negative binomial, it is the logarithm. That is, we have

<!-- b000496 | furniture | pages [10] -->
Page 10

<!-- b000497 | furniture | pages [10] -->
Team 2522820

<!-- b000499 | prose | pages [10] -->
Φ−1(P(Yij = 1)) = Xijβj + Zijbj log(µij) = Xijβj + Zijbj

<!-- b000500 | prose | pages [10] -->
Now the right side is the same, as the base for these models is a linear predictor, and changing the link function allows us to model different scenarios. For Cluster -1, we combine the probit binary regression and the negative binomial as follows:

<!-- b000501 | prose | pages [10] -->
Predicted Number of Medals = (1 − P(Yij = 0)) · ¯ij Where for clusters 0 and -1 the predicted number of medals is just Îij. The optimization method here was also MLE, though a different one could have led to a better fitting model.

<!-- b000502 | heading | pages [10] -->
3.4.3 Results, Model Fit, and Uncertainty

<!-- b000503 | prose | pages [10] -->
We decided to use Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) as well as the log likelihood value to determine the quality of our model's fit to the data. Both AIC and BIC are based on the log likelihood as well as number of parameters and sample size. Generally lower AIC/BIC and higher log likelihood is desired for a well fitted model. In fitting the mixed effects models, we experimented with different methods to determine one that would optimize these metrics of fit. The one that worked the best was Powell's method, which is just one of many optimization methods but happened to fit best. However, it may be due to the nature of the data that MLE never quite converged and our fit metrics ended up subpar. Checking again for heteroscedasticity showed us that this model did not improve it as much either, however this model is less susceptible to the inaccuracies Tobit would face from heteroscedasticity.

<!-- b000504 | prose | pages [10] -->
For each of the cluster models, here are our final results (for total medals): Originally, even with the best

<!-- b000505 | prose | pages [10] -->
Metric Cluster 1 Cluster 0 Cluster -1

<!-- b000506 | heading | pages [10] -->
Zero Model (Cluster 1 only)

<!-- b000507 | prose | pages [10] -->
-746.77 Log-likelihood AIC 1523.55 BIC 1609.37

<!-- b000508 | heading | pages [10] -->
Positive Model / Full Model

<!-- b000509 | prose | pages [10] -->
-590.75 -1083.85 Log-likelihood -1018.16 AIC 2058.32 1211.51 2195.71 BIC 2105.87 1262.55 2259.12

<!-- b000510 | caption | pages [10] -->
Table 3: Model Fit Statistics by Cluster

<!-- b000511 | prose | pages [10] -->
method (Powell's), cluster -1 had exceptionally bad metrics (likely since it is a group of outliers). To fix this, we weighted all of the predictive factors by the variance in an attempt to reduce heteroscedasticity and fit better when optimizing with MLE. This worked, cutting the AIC/BIC factors in half and increasing the log-likelihood level to one similar to the other models. Generally, our model accounts for random effects on multiple scales and attempts to combat heteroscedasticity, and we have chosen the best methods to fit the data (despite convergence issues). To predict the number of athletes for each country in 2028, we used a simple linear regression. Finally, we applied this model to Total Medal count, Gold, Silver, and Bronze. We will provide the top 7 countries ordered by Gold medals, but our code predicts full Olympic results.

<!-- b000512 | prose | pages [10] -->
Likely in line with the fit metrics not being the best, there is a large confidence interval margin. However, these results do have some reasonable conclusions.

<!-- b000513 | prose | pages [10, 11] -->
关注数学模型 Rank Country Gold Silver Bronze Total 1 United States 48 [33, 63] 43 [32, 54] 45 [13, 77] 136 [108, 164] 2 Germany 28 [13, 43] 23 [12, 34] 22 [0, 44] 73 [45, 101] 3 China 25 [10, 40] 18 [7, 29] 27 [0, 54] 70 [42, 98] 4 Great Britain 17 [2, 32] 19 [8, 30] 17 [0, 38] 53 [25, 81] 微信公众号：数学模型 5 Japan 16 [1, 31] 9 [0, 20] 13 [0, 35] 38 [10, 38] 6 Australia 13 [0, 28] 17 [6, 28] 19 [0, 41] 49 [21, 77] 7 Italy 11 [0, 26] 10 [0, 21] 20 [0, 43] 41 [13, 69]

<!-- b000514 | furniture | pages [10] -->
获取更多资讯

<!-- b000515 | furniture | pages [11] -->
Team 2522820

<!-- b000516 | furniture | pages [11] -->
Page 11

<!-- b000518 | caption | pages [11] -->
Table 4: Predicted Medal Counts for Top 7 Gold Medal Countries in 2028 Olympics (with 95% Confidence

<!-- b000519 | prose | pages [11] -->
Intervals)

<!-- b000520 | prose | pages [11] -->
We are also tasked with looking for countries that have improved or gotten worse since the 2024 Olympics. We did this by looking at rank change, setting a minimum medal change threshold of 3 so that it wasn’t just countries that changed a lot even though they all got 0 or low counts.

<!-- b000521 | prose | pages [11] -->
微信号：MATHmodels Country Rank 2024 Gold 2024 Rank 2028 Gold 2028 Rank Change Medal Change Most Improved Jamaica 43 1 16 7 +27 +6 Germany 10 12 2 28 +8 +16 Ukraine 23 3 15 7 +8 +4 Spain 15 5 8 11 +7 +6 Most Declined Canada 12 9 111 0 -99 -9 Netherlands 6 15 37 2 -31 -13 South Korea 8 13 18 6 -10 -7 France 5 16 11 10 -6 -6

<!-- b000522 | caption | pages [11] -->
Table 5: Countries with Most Significant Changes in Olympic Performance (2024 vs 2028)

<!-- b000523 | heading | pages [11] -->
3.5 Projections for Countries Yet to Earn Medals

<!-- b000524 | prose | pages [11] -->
Our model accounted for countries that generally don’t medal through clustering and a specific binary regression model to determine if those countries do medal in a certain year or not. Our model predicted these values as stated previously in the paper as

<!-- b000525 | prose | pages [11] -->
Predicted Number of Medals = (1 −P(Yij = 0)) · ˆyij

<!-- b000526 | prose | pages [11] -->
Here ˆyij is the number of medals they would earn if they medalled at all, and it is multiplied by the probability of earning a medal. We looked at the list of countries that have never medalled in Olympic history and compared it to our predictions for 2028. We assigned odds to these estimates as the probability these countries medalled at all from our regression (the odds are P(Yij = 1)). We found that two countries, Angola and Saar, are predicted to win 1 medal in the 2028 Olympics and have never won a medal previously, with odds 32.54% and 40.08% respectively.

<!-- b000527 | heading | pages [11] -->
3.6 Analyzing Impacts of Events and Sports

<!-- b000528 | prose | pages [11] -->
Through the information in the data sets, two deciding factors in the performance of a country at the Games were the amount of medals they obtained and the distribution of medals among Gold, Silver, and Bronze.

<!-- b000529 | furniture | pages [12] -->
Team 2522820

<!-- b000530 | furniture | pages [12] -->
Page 12

<!-- b000531 | prose | pages [12] -->
However, before analyzing the impacts of events and sports on the performance of a country at the Games, a lot of processing wasa done to create viable connections between the datasets.

<!-- b000532 | heading | pages [12] -->
3.6.1 Data Processing (Ceiling-Proportion Approximation)

<!-- b000533 | prose | pages [12] -->
1. The medal counts.csv file provided the total amount of medals obtained by each country (that wins at least 1 medal) and the distribution of those medals during all the Games. However, there is no clear connection to the distribution of those medals to sports and events.

<!-- b000534 | prose | pages [12] -->
2. By using athletes.csv to process specific athletes, this CSV file could be used to total the amount of medals obtained in a specific sport or event (with other parameters like country, year, etc). This was beneficial as it created a distribution of medals to events and sports. However, this created another issue. There was an over counting of medals due to overlapping events. Due to the existence of team events, even if many athletes obtain a medal, it may only be 1 medal for the country. To account for this, programs.csv provided helpful data.

<!-- b000535 | prose | pages [12] -->
3. programs.csv contains information regarding the number of sports per discipline. This meant that there’s a known ceiling to the amount of medals that could be obtained per sport.

<!-- b000536 | prose | pages [12] -->
Since there is a known ceiling, the next step was creating a proportion that could multiply with the ceiling to approximate the medal distribution in sports. Going back to athletes.csv, we were able to find the amount of athletes from a country that obtained a medal in a specific sport. By removing one of the parameters, we could also find the amount of athletes that obtained a medal in a specific sport. These two different values (different in country specification), allowed us to create a proportion between a country’s total athlete medal count in a sport to the total athlete medal count in a sport. Ceiling-Proportion Approximation = Country’s total athlete medal count in a sport · 3 · Total Events per Sport Total athlete medal count in a sport m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m This Ceiling-Proportion Approximation would yield an estimate of the amount of medals in a given sport m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (note that we multiply by 3 as there are typically 3 medals to be obtained per event). This gave us two different m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m approximations for medal distribution in sports: the distribution solely from the amount of athletes from a m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m country that obtained a medal in a specific sport and the distribution based on the ceiling multiped by a related m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m proportion. To test the accuracy of the two different approximations, we isolated the sports in each year, then m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m summed the applied approximation of medal counts in every sport offered to get a total medal count. Then, we analyzed the accuracy of the total medal count approximations over time on the United States and the Netherlands. This can be seen in Figures 3a and 3b.

<!-- b000537 | prose | pages [12] -->
The figures demonstrated that the approximation of total medal counts using the ceiling-proportion approx- imation was much more accurate than just using the total medals obtained by all of a country’s athletes in a sport. We verified this by taking the average percent error of both approximations and comparing them. In the Netherlands, the ceiling-proportion approximation had a percent error of 20% while the athlete total approximation returned 198%. Similarly for the United States, our program returned 10% and 107% error respectively for the ceiling-proportion and athlete-total approximations.

<!-- b000538 | prose | pages [12] -->
By using the ceiling-proportion approximations for total medal count that were built on approximations for medal distribution in sports, we could get reasonable estimates for the medal counts in various sports and disciplines. However, there was one more issue before we could start analyzing the distribution of medals in sports. Not all medals are the same. This approximation gave us estimates for the total amount of medals, but not for the distribution among Gold, Silver, and Bronze. Luckily, we were able to apply a similar approximation as before: Ceiling-Proportion Approximation = Country’s total athlete specific medal count in a sport ·Total Events per Sport Total athlete specific medal count in a sport

<!-- b000539 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型 (a) Total medal approximations in Netherlands compared (b) Total medal approximations in United States compared to actual medal counts to actual medal counts

<!-- b000540 | furniture | pages [12] -->
2

<!-- b000541 | furniture | pages [12] -->
MATHmodels

<!-- b000542 | furniture | pages [12] -->
获取更多资讯

<!-- b000543 | furniture | pages [13] -->
Team 2522820

<!-- b000544 | furniture | pages [13] -->
Page 13

<!-- b000546 | caption | pages [13] -->
Figure 3: Black Marks: The actual total medal counts, Blue Marks: ceiling-proportion approximation, Red

<!-- b000547 | prose | pages [13] -->
Marks: athlete total approximation . 微信号：MATHmodels Notice that in this Ceiling-Proportion Approximation, we removed the scalar of 3. This scalar acted to account for all medal types earlier, but now that we are giving a specific medal, we no longer need to multiply by a factor of 3. Instead, we will apply this Ceiling-Proportion Approximation to each medal type. With three approximations for Gold, Silver, and Bronze, we can build a new approximation for the total medal count. This time giving us the distribution of medal types. We can see this in Figures 4a and 4b.

<!-- b000548 | prose | pages [13] -->
(a) Total medal approximations in Netherlands compared (b) Total medal approximations in United States compared to actual medal counts to actual medal counts

<!-- b000549 | caption | pages [13] -->
Figure 4: Black line: Ceiling-Proportion Approximation from Figure 3, Brown Region: The Bronze medal

<!-- b000550 | prose | pages [13] -->
count estimate, Grey Region: Silver medal count estimate, Yellow Region: Gold medal count estimate

<!-- b000551 | prose | pages [13] -->
These approximations for total medal counts (with respect to our initial Ceiling-Proportion Approximations from Figure 1) were promising as there was only 2.8% and 1.1% average percent error respectively for the Netherlands and United States. However, it’s important to keep in mind that this approximation is still problematic as it creates the assumption that if the medal distributions sum to a reasonably accurate total medal count, then the medal distribution will also be accurate.

<!-- b000552 | furniture | pages [14] -->
Team 2522820

<!-- b000553 | furniture | pages [14] -->
Page 14

<!-- b000554 | heading | pages [14] -->
3.6.2 Data Processing (Event Limitation Approximation)

<!-- b000555 | prose | pages [14] -->
While the Ceiling-Proportion Approximation provided a fairly reasonable estimation of the medal distribution among sports/disciplines, we lacked a method of associating sports/disciplines to events. This inspired our Event Limitation Approximation approach. This approximation works as in almost all cases, an event only has 1 medalist in Gold, Silver, and Bronze. By creating a Python dictionary to store all isolated unique events that a country obtained a medal in, the length of that dictionary would tell us how many Gold, Silver, or Bronze medals they received and its distribution among sports and events.

<!-- b000556 | prose | pages [14] -->
This method parses through all of the data within athletes.csv and collects every single entry that has a specified year. Then, we reduced the data to only give us the country code, sport, event, and medal type. A dictionary proved useful here to distinguish unique events. We required three separate dictionaries for each medal type as it was possible for a key of (country code, sport, event) to be associated to Bronze, Silver, or Gold (which is not allowed by Python dictionaries). By searching each dictionary for a unique country code (ie. USA for United States), we could create subsets per country that allow us to know how many Gold, Silver, and Bronze medals they got as well as in what events. This satisfied our need for associating medals to events. To test the accuracy of this approximation, we ran our code for the United States and Netherlands again. The results are shown in Figures 5a and 5b.

<!-- b000557 | prose | pages [14] -->
(a) Total medal approximations in Netherlands compared (b) Total medal approximations in United States compared to actual medal counts to actual medal counts

<!-- b000558 | caption | pages [14] -->
Figure 5: Red: Actual values given by IOC, Blue: Our Event Limitation Approximation

<!-- b000559 | prose | pages [14] -->
This was very accurate with average percent errors of 2.4% and 1% for the Netherlands and United States respectively. Now, we want to compare our distribution of medal types with the IOC’s distribution. We can see this below in Figures 6a, 6b, and 6c.

<!-- b000560 | prose | pages [14] -->
(a) Gold Medal Distribution Compar- (b) Silver Medal Distribution Compar- (c) Bronze Medal Distribution Com- ison in United States ison in United States parison in United States

<!-- b000561 | caption | pages [14] -->
Figure 6: Red: Actual values given by IOC, Blue: Our Event Limitation Approximation

<!-- b000562 | prose | pages [14, 15] -->
关注数学模型 This was very promising as we only found 0.85%, 1.6%, and 1% error for gold distribution, silver distribution, and bronze distribution respectively.

<!-- b000563 | furniture | pages [14] -->
2

<!-- b000564 | furniture | pages [14] -->
MATHmodels

<!-- b000565 | furniture | pages [14] -->
获取更多资讯

<!-- b000566 | furniture | pages [15] -->
Page 15

<!-- b000567 | furniture | pages [15] -->
Team 2522820

<!-- b000569 | prose | pages [15] -->
3.6.3 Selecting a Processing Method

<!-- b000570 | prose | pages [15] -->
When choosing between our Ceiling-Proportion Approximation and Event Limitation Approximation, we considered three factors:

<!-- b000571 | prose | pages [15] -->
1. Accuracy of Total Amount of Medals: Comparing the percent errors from Figure 1 and Figure 3, the Ceiling-Proportion Approximation found percent errors of 20% and 10% while our Event Limitation Approximation found percent errors of 2.4% and 1% for the Netherlands and United States respectively.

<!-- b000572 | prose | pages [15] -->
2. Accuracy of Medal Distribution into Gold, Silver, and Bronze: As described earlier, there is a huge flaw in our Ceiling-Proportion Approximation for medal distribution as its an approximation of an approximation. This assumes the behavior of various factors like team events that we're simply unable to account for. Alternatively, our Event Limitation Approximation found percent errors lower and on- par with the percent errors from our Ceiling-Proportion Approximation. However, the Event Limitation Approximation found these percent errors with respect to the IOC data. This removed all assumptions made when comparing medal distribution while maintaining a low percent error.

<!-- b000573 | heading | pages [15] -->
3. Computation Time: The Ceiling-Proportion Approximation takes approximately 3-5 minutes per coun-

<!-- b000574 | prose | pages [15] -->
try while our Event Limitation Approximation takes approximately 3-5 seconds per country. This was another clear indicator to choose the Event Limitation Approximation as it allowed us to process data for large groups of countries.

<!-- b000575 | prose | pages [15] -->
Our Event Limitation Approximation out-performed our Ceiling-Proportion Approximation in all three faeng  s    s  ons  sond e s  s s as ont Limitation Approximation.

<!-- b000576 | heading | pages [15] -->
3.6.4 Event Impact: Singular Value Decomposition (SVD)

<!-- b000577 | prose | pages [15] -->
O We will look at the data for all events competed in 2024, and create a matrix with medal counts for each country by event. Then, we perform Singular Value Decomposition (SVD) on this matrix A, represented as

<!-- b000578 | prose | pages [15] -->
A = UΣVT

<!-- b000579 | prose | pages [15] -->
Where Σ is a diagonal matrix with the singular values (square root of the eigenvalues of A). The magnitude of these eigenvalues indicates the strength of the scaling in the direction of their associated column vectors. The singular values in the diagonal matrix Σ determine how much each corresponding singular vector contributes to the overall transformation of the matrix, with larger singular values indicating stronger influence in the corresponding direction.

<!-- b000580 | prose | pages [15] -->
Based on the data from the United States in 2024, we were able to isolate the Top 10 influential events in medal counts. And by applying the SVD to further countries, we could understand how each event plays a role in the medal counts of all countries competing in the Games.

<!-- b000581 | prose | pages [15] -->
3.6.5 Analyzing Impact of Sports

<!-- b000582 | prose | pages [15] -->
It is important to note that the naming systems in the files are inconsistent: we analyzed performances in categories classified as “sports" in athletes.csv, even though this category includes both sports and disciplines as designated in programs.csv.

<!-- b000583 | furniture | pages [16] -->
Team 2522820

<!-- b000584 | furniture | pages [16] -->
Page 16

<!-- b000585 | prose | pages [16] -->
Rank Singular Value Event 1 3838.9080 Men’s Greco-Roman 97kg 2 2664.5821 Men’s Greco-Roman 77kg 3 2397.0722 Men’s Greco-Roman 67kg 4 2042.4828 Men’s Freestyle 57kg 5 1903.1633 Men’s Freestyle 65kg 6 1819.0644 Women’s 20km Race Walk 7 1666.6152 Marathon Race Walk Relay Mixed 8 1533.8462 Women’s 100m 9 1468.2113 Women’s 200m 10 1296.5435 Men’s 100m

<!-- b000586 | caption | pages [16] -->
Table 6: Ranked Singular Values and Associated Events

<!-- b000587 | prose | pages [16] -->
Here, we are tasked with understanding what sports are most important to various countries. We deviate from 4.6.4 as we will now consider the previous ranking point system instead of total medals. Each gold medal is worth 6 points, each silver medal is worth 3 points, and each bronze medal is worth 2 points. By totaling up the points, we can weigh the effect of the medal distribution on the total medal count. To quantify the impact of sports, we will consider the following three factors:

<!-- b000588 | prose | pages [16] -->
1. Sport-Point Efficiency: A proportion between the points a country obtains in one sport and how many athletes from that same country competed in that sport.

<!-- b000589 | prose | pages [16] -->
2. Sport-Point Share: A proportion between how many points a country obtains in one sport and how many points a country obtains at one Olympic Game.

<!-- b000590 | prose | pages [16] -->
3. Revealed Comparative Advantage (RCA) Index: While the RCA Index is typically applied to reveal a country’s advantage in producing goods and services, we can extend this to the Games. The RCA Index here will tell us if a country has an advantage in a sport when compared with other countries’ data given by the IOC.

<!-- b000591 | prose | pages [16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Variable Definition Unit m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Pcs Number of points won by country c in sport s. Count m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Acs Number of athletes by country c in sport s. Count m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m P s Pcs Total points won in the Games by country c. Count m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m P c Pcs Total points won in the Games in sport s. m m m m m m m m m m m m m m m m m m Count m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m P c,s Pcs Total points won in the Games across all countries and all sports. Count RCAIcs Revealed Comparative Advantage Index by country c in sport s. Unitless (Index) SPE Sport-Point Efficiency. Unitless SPSc Sport-Point Share for country c. Unitless

<!-- b000592 | caption | pages [16] -->
Table 7: Variable Definitions

<!-- b000593 | prose | pages [16] -->
We will apply each of these indicators of a sport’s importance to the United States and Netherlands in the most recent Olympic game: Paris Olympics, 2024. Additionally, since there were too many unique “sports”, we will only consider the top 10 per country.

<!-- b000594 | heading | pages [16] -->
1. Sport-Points Efficiency

<!-- b000595 | prose | pages [16] -->
SPE = Pcs Acs

<!-- b000596 | heading | pages [16] -->
2. Sport-Points Share

<!-- b000597 | prose | pages [16] -->
Pcs SPSc = P c Pcs

<!-- b000598 | heading | pages [16] -->
3. Revealed Comparative Advantage (RCA)

<!-- b000599 | prose | pages [16] -->
关注数学模型

<!-- b000600 | furniture | pages [16] -->
2

<!-- b000601 | prose | pages [16] -->
Pcs P c,s Pcs P s Pcs

<!-- b000602 | furniture | pages [16] -->
MATHmodels

<!-- b000603 | furniture | pages [16] -->
获取更多资讯

<!-- b000604 | prose | pages [16, 17] -->
RCAIcs = = SPSc P c Pcs P s Pcs P c,s Pcs Pcs Acs SPE Pcs Acs SPE Sport Sport Weightlifting 8.00 5 1.600 Sailing 15.71 11 1.429 Wrestling 21.00 16 1.313 Rowing 32.96 33 0.999 微信公众号：数学模型 Athletics 164.34 126 1.304 Athletics 43.3 46 0.941 Surfing 6.00 5 1.200 Equestrian 0.8 12 0.067 Basketball 25.03 24 1.043 Volleyball 0.0 13 0.000 Shooting 16.67 17 0.980 Triathlon 0.0 4 0.000 Archery 3.50 4 0.875 Tennis 0.0 6 0 Golf 6.00 7 0.857 Handball 0 10 0 Fencing 14.00 20 0.700 Judo 0 10 0 Skateboarding 8.00 12 0.667 Archery 0 4 0

<!-- b000605 | furniture | pages [17] -->
Team 2522820

<!-- b000606 | furniture | pages [17] -->
Page 17

<!-- b000608 | caption | pages [17] -->
Table 8: Top 10 SPE Values for Sports in the

<!-- b000609 | caption | pages [17] -->
Table 9: Top 10 SPE Values for Sports in the

<!-- b000610 | prose | pages [17] -->
United States Netherlands 微信号：MATHmodels P P Pcs c Pcs SPSc Pcs c Pcs SPSc Sport Sport Basketball 25 44 0.57 Rowing 32.96 154 0.214 Athletics 164 528 0.31 Sailing 15.71 110 0.143 Surfing 6 22 0.27 Cycling 30.64 242 0.127 Golf 6 22 0.27 Athletics 43.30 528 0.082 Football 6 22 0.26 Basketball 3.00 44 0.068 Aquatics 137 539 0.25 Aquatics 16.51 539 0.031 Volleyball 10 44 22.7 Equestrian 0.80 66 0.012 Gymnastics 38 198 0.19 ————- — — 0 Skateboarding 8 44 0.18 ————- — — 0 Tennis 6.25 55 0.11 ————- — — 0

<!-- b000611 | caption | pages [17] -->
Table 10: Top 10 SPSc Values for Sports in the

<!-- b000612 | caption | pages [17] -->
Table 11: Top 10 SPSc Values for Sports in the

<!-- b000613 | prose | pages [17] -->
United States Netherlands

<!-- b000614 | prose | pages [17] -->
P P SPSc c,s Pcs s Pcs RCAIcs Sport P P SPSc c,s Pcs s Pcs RCAIcs Sport Rowing 0.214 3619 143 5.42 Basketball 0.57 3619 525 3.92 Sailing 0.143 3619 143 3.62 Athletics 0.31 3619 525 2.15 Cycling 0.127 3619 143 3.21 Surfing 0.27 3619 525 1.9 Athletics 0.082 3619 143 2.08 Golf 0.27 3619 525 1.9 Basketball 0.068 3619 143 1.73 Football 0.26 3619 525 1.79 Aquatics 0.25 3619 525 1.75 Aquatics 0.031 3619 143 0.78 Volleyball 22.7 3619 525 1.57 Equestrian 0.012 3619 143 0.31 Gymnastics 0.19 3619 525 1.30 ————- — — — 0 Skateboarding 0.18 3619 525 1.25 ————- — — — 0 Tennis 0.11 3619 525 0.78 ————- — — — 0

<!-- b000615 | caption | pages [17] -->
Table 12: Top 10 RCAIcs Values for Sports in the

<!-- b000616 | caption | pages [17] -->
Table 13: Top 10 RCAIcs Values for Sports in the

<!-- b000617 | prose | pages [17] -->
United States Netherlands

<!-- b000618 | prose | pages [17] -->
Since SPSc is a building block of RCAIcs, we chose to only consider the data from the top 10 SPE and top 10 RCAIcs.

<!-- b000619 | prose | pages [17, 18] -->
SPE by definition tells us the return on investment. If we expect each athlete to contribute at least 1 ranking point, then SPE > 1, tells us that there were more points won in a sport than the amount of athletes. This means that for a lower use of resources on athlete expenditures and training, countries get a higher return of points. This may suggest to countries the importance of sports that have a high return of ranking points. So, for the United States, they may consider investing more in their Top 5 in Table 8. And for the Netherlands, they may consider investing more in Sailing.

<!-- b000620 | furniture | pages [18] -->
Team 2522820

<!-- b000621 | furniture | pages [18] -->
Page 18

<!-- b000623 | prose | pages [18] -->
If RCAIcs > 1, then that sport is considered to have a competitive advantage against the other countries competing in the same sports. This value is integral for determining the importance of sports as it allows a country to know what sports they are outperforming others in. For the United States, this means almost all of the sports in Table 12. While for the Netherlands, this would be their Top 5 within Table 13.

<!-- b000624 | heading | pages [18] -->
3.6.6 Home Country Effects

<!-- b000625 | prose | pages [18] -->
It’s a well-known fact that the host country often has a competitive advantage whether it’s due to psychological factors or a country’s ability to select sports (like in the Games). We can see preliminary evidence of a home country advantage just by looking at the increase in medal counts for all host countries.

<!-- b000626 | caption | pages [18] -->
Table 14: ∆Total Medal Count between host year and previous competition year for last 6 Host Countries

<!-- b000627 | prose | pages [18] -->
∆Total Medal Count Host Year France 2024 31 Japan 2020 17 Brazil 2016 2 Great Britain 2012 14 China 2008 37 Greece 2004 3

<!-- b000628 | prose | pages [18] -->
Now that we know this hosting advantage is present at the Games, we want to understand how the events chosen affect this advantage. According to the IOC, host countries have only been allowed to propose (influence the choosing) of events since the 2020 Tokyo Olympics. This means that to understand how the events chosen impact home country results, we are limited to data from the 2020 Tokyo Olympics and 2024 Paris Olympics.

<!-- b000629 | prose | pages [18] -->
By applying the RCA index from 3.6.5 on each unique event offered to the host country each year, we could understand the influence of events that the host country selected. Again, an RCAIcs > 1 would indicate that the event affects results more than they would for a majority of the other competing countries. However, we could not apply this in the given time.

<!-- b000630 | heading | pages [18] -->
4 Problem 2: Detecting and Utilizing the Great Coach Effect

<!-- b000631 | heading | pages [18] -->
4.1 Detecting the Great Coach Effect

<!-- b000632 | prose | pages [18] -->
m m m m m m m m m m m m m m m m m m m m m m Our primary consideration when developing a model to detect great coach effects was the fact that we had m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m very limited data: the only accessible data that was relevant to our model were the point distributions by nation m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and by sport, which we found by using the event limit approximation method from 4.6.2. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Many other factors—such as outstanding individual athletes or increased government investment in athletic m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m programs—could affect performances, and because of our limited data, it is impossible to show that any changes m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m in the point distributions for a given country and sport are directly due to the influence of a great coach, as they could be (and likely are) results of a combination of factors. In other words, the most we could accomplish with the provided data was finding possible instances of the great coach effect. However, we can examine the results of this model in the context of the history of great coaches to see how accurate it is.

<!-- b000633 | prose | pages [18] -->
关注数学模型

<!-- b000634 | furniture | pages [18] -->
2

<!-- b000635 | furniture | pages [18] -->
MATHmodels

<!-- b000636 | furniture | pages [18] -->
获取更多资讯

<!-- b000637 | furniture | pages [19] -->
Team 2522820

<!-- b000638 | furniture | pages [19] -->
Page 19

<!-- b000639 | heading | pages [19] -->
4.1.1 Time Series Analysis Setup

<!-- b000640 | prose | pages [19] -->
The general strategy behind our model to detect potential great coach effects is identifying a given coun- try’s performances in a given sport that are anomalously successful in the context of that country’s historical performances in the same sport. To do this, we applied time series analysis to the data.

<!-- b000641 | prose | pages [19] -->
A time series is a series of data that are equally spaced apart. Aside from a few notable exceptions—the 1916, 1940, and 1944 Games were canceled because of the World Wars—the regular four-year timing of the Games means that performances at the Games are suitable for time series analysis.

<!-- b000642 | prose | pages [19] -->
Many countries have been competing in the same sport for well over a century. Over this time, the influence of individual great coaches is greatly outweighed by a multitude of other factors. So, if we were to calculate the z-scores of each performance in the context of the country’s entire historical performance, the z-scores would be 微信公众号：数学模型 less meaningful. To more accurately interpret variations, we needed to calculate the z-scores of each performance in only the context of the Games immediately preceding and succeeding it. For this, we used a rolling window of four Games at a time (more detail provided in the outline).

<!-- b000643 | heading | pages [19] -->
4.1.2 Variable Definitions

<!-- b000644 | caption | pages [19] -->
Table 14: Variable Definitions

<!-- b000645 | prose | pages [19] -->
Variable Definition Formula N The total number of Games a given country has competed 微信号：MATHmodels in for a given sport L Number of Games included in the segment for a given country and sport Ps Number of points earned in the segment for a given country and sport PN 1 µ i=1 xi Population mean points for a given country and sport over N all Games q PN 1 i=k(xi −µ)2 σ Population standard deviation of points for a given country N and sport over all Games Pk+3 1 x i=k xi, Sample mean points for a given country and sport over a 4 where k ∈{1, 2, ..., N −3} rolling set of four Games q Pk+3 1 i=k (xi −x)2, s Sample standard deviation of points for a given country and 4 sport over a rolling set of four Games where k ∈{1, 2, ..., N −3} (Ps −µ · L) · 100% C Relative contribution of great coaches for a given country and sport C ∆Pnorm Normalized relative contribution of great coaches for a L given country and sport

<!-- b000646 | prose | pages [19] -->
For a given country and sport, this was the outline of the model:

<!-- b000647 | prose | pages [19] -->
1. Calculate x and s in a rolling window of four Games at a time over the history of the country’s participation in that sport.

<!-- b000648 | prose | pages [19, 20] -->
(a) E.g. for a country that has participated in a sport since 1896, the windows for that country-sport pair would start from [1896, 1900, 1904, 1908], then [1900, 1904, 1908, 1912], and so on. The means and sample standard deviations of the country’s points in each of these sets of years are calculated. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2. When the difference in points between performances at consecutive games is at least 2s, call these positive change points.

<!-- b000649 | furniture | pages [19] -->
m

<!-- b000650 | furniture | pages [19] -->
m

<!-- b000651 | furniture | pages [19] -->
m

<!-- b000652 | furniture | pages [19] -->
m

<!-- b000653 | furniture | pages [19] -->
m

<!-- b000654 | furniture | pages [19] -->
m

<!-- b000655 | furniture | pages [19] -->
m

<!-- b000656 | furniture | pages [19] -->
m

<!-- b000657 | furniture | pages [19] -->
m

<!-- b000658 | furniture | pages [19] -->
m

<!-- b000659 | furniture | pages [19] -->
m

<!-- b000660 | furniture | pages [19] -->
m

<!-- b000661 | furniture | pages [19] -->
m

<!-- b000662 | furniture | pages [19] -->
m

<!-- b000663 | furniture | pages [19] -->
m

<!-- b000664 | furniture | pages [19] -->
m

<!-- b000665 | furniture | pages [19] -->
m

<!-- b000666 | furniture | pages [19] -->
m

<!-- b000667 | furniture | pages [19] -->
m

<!-- b000668 | furniture | pages [19] -->
m

<!-- b000669 | furniture | pages [19] -->
m

<!-- b000670 | furniture | pages [19] -->
m

<!-- b000671 | furniture | pages [19] -->
m

<!-- b000672 | furniture | pages [19] -->
m

<!-- b000673 | furniture | pages [19] -->
m

<!-- b000674 | furniture | pages [19] -->
m

<!-- b000675 | furniture | pages [19] -->
m

<!-- b000676 | furniture | pages [19] -->
m

<!-- b000677 | furniture | pages [19] -->
m

<!-- b000678 | furniture | pages [19] -->
m

<!-- b000679 | furniture | pages [19] -->
m

<!-- b000680 | furniture | pages [19] -->
m

<!-- b000681 | furniture | pages [19] -->
m

<!-- b000682 | furniture | pages [19] -->
m

<!-- b000683 | furniture | pages [19] -->
m

<!-- b000684 | furniture | pages [19] -->
m

<!-- b000685 | furniture | pages [19] -->
m

<!-- b000686 | furniture | pages [19] -->
m

<!-- b000687 | furniture | pages [19] -->
m

<!-- b000688 | furniture | pages [19] -->
m

<!-- b000689 | furniture | pages [19] -->
m

<!-- b000690 | furniture | pages [19] -->
m

<!-- b000691 | furniture | pages [19] -->
m

<!-- b000692 | furniture | pages [19] -->
m

<!-- b000693 | furniture | pages [19] -->
m

<!-- b000694 | furniture | pages [19] -->
m

<!-- b000695 | furniture | pages [19] -->
m

<!-- b000696 | furniture | pages [19] -->
m

<!-- b000697 | furniture | pages [19] -->
m

<!-- b000698 | furniture | pages [19] -->
m

<!-- b000699 | furniture | pages [19] -->
m

<!-- b000700 | furniture | pages [19] -->
m

<!-- b000701 | furniture | pages [19] -->
m

<!-- b000702 | furniture | pages [19] -->
m

<!-- b000703 | furniture | pages [19] -->
m

<!-- b000704 | furniture | pages [19] -->
m

<!-- b000705 | furniture | pages [19] -->
m

<!-- b000706 | furniture | pages [19] -->
m

<!-- b000707 | furniture | pages [19] -->
m

<!-- b000708 | furniture | pages [19] -->
m

<!-- b000709 | furniture | pages [19] -->
m

<!-- b000710 | furniture | pages [19] -->
m

<!-- b000711 | furniture | pages [19] -->
m

<!-- b000712 | furniture | pages [19] -->
m

<!-- b000713 | furniture | pages [19] -->
m

<!-- b000714 | furniture | pages [19] -->
m

<!-- b000715 | furniture | pages [19] -->
m

<!-- b000716 | furniture | pages [19] -->
m

<!-- b000717 | furniture | pages [19] -->
m

<!-- b000718 | furniture | pages [19] -->
m

<!-- b000719 | furniture | pages [19] -->
m

<!-- b000720 | furniture | pages [19] -->
m

<!-- b000721 | furniture | pages [19] -->
m

<!-- b000722 | furniture | pages [19] -->
m

<!-- b000723 | furniture | pages [19] -->
m

<!-- b000724 | furniture | pages [19] -->
m

<!-- b000725 | furniture | pages [19] -->
m

<!-- b000726 | furniture | pages [19] -->
m

<!-- b000727 | furniture | pages [19] -->
m

<!-- b000728 | furniture | pages [19] -->
m

<!-- b000729 | furniture | pages [19] -->
m

<!-- b000730 | furniture | pages [19] -->
m

<!-- b000731 | furniture | pages [19] -->
m

<!-- b000732 | furniture | pages [19] -->
m

<!-- b000733 | furniture | pages [19] -->
m

<!-- b000734 | furniture | pages [19] -->
m

<!-- b000735 | furniture | pages [19] -->
m

<!-- b000736 | furniture | pages [19] -->
m

<!-- b000737 | furniture | pages [19] -->
m

<!-- b000738 | furniture | pages [19] -->
m

<!-- b000739 | furniture | pages [19] -->
m

<!-- b000740 | furniture | pages [19] -->
m

<!-- b000741 | furniture | pages [19] -->
m

<!-- b000742 | furniture | pages [19] -->
m

<!-- b000743 | furniture | pages [19] -->
m

<!-- b000744 | furniture | pages [19] -->
m

<!-- b000745 | furniture | pages [19] -->
m

<!-- b000746 | furniture | pages [19] -->
m

<!-- b000747 | furniture | pages [19] -->
m

<!-- b000748 | furniture | pages [19] -->
m

<!-- b000749 | furniture | pages [19] -->
m

<!-- b000750 | furniture | pages [19] -->
m

<!-- b000751 | furniture | pages [19] -->
m

<!-- b000752 | furniture | pages [19] -->
m

<!-- b000753 | furniture | pages [19] -->
m

<!-- b000754 | furniture | pages [19] -->
m

<!-- b000755 | furniture | pages [19] -->
m

<!-- b000756 | furniture | pages [19] -->
m

<!-- b000757 | furniture | pages [19] -->
m

<!-- b000758 | furniture | pages [19] -->
m

<!-- b000759 | furniture | pages [19] -->
m

<!-- b000760 | furniture | pages [19] -->
m

<!-- b000761 | furniture | pages [19] -->
m

<!-- b000762 | furniture | pages [19] -->
m

<!-- b000763 | furniture | pages [19] -->
m

<!-- b000764 | furniture | pages [19] -->
m

<!-- b000765 | furniture | pages [19] -->
m

<!-- b000766 | furniture | pages [19] -->
m

<!-- b000767 | furniture | pages [19] -->
m

<!-- b000768 | furniture | pages [19] -->
m

<!-- b000769 | furniture | pages [19] -->
m

<!-- b000770 | furniture | pages [19] -->
m

<!-- b000771 | furniture | pages [19] -->
m

<!-- b000772 | furniture | pages [19] -->
m

<!-- b000773 | furniture | pages [19] -->
m

<!-- b000774 | furniture | pages [19] -->
m

<!-- b000775 | furniture | pages [19] -->
m

<!-- b000776 | furniture | pages [19] -->
m

<!-- b000777 | furniture | pages [19] -->
m

<!-- b000778 | furniture | pages [19] -->
m

<!-- b000779 | furniture | pages [19] -->
m

<!-- b000780 | furniture | pages [19] -->
m

<!-- b000781 | furniture | pages [19] -->
m

<!-- b000782 | furniture | pages [19] -->
m

<!-- b000783 | furniture | pages [19] -->
m

<!-- b000784 | furniture | pages [19] -->
m

<!-- b000785 | furniture | pages [19] -->
m

<!-- b000786 | furniture | pages [19] -->
m

<!-- b000787 | furniture | pages [19] -->
m

<!-- b000788 | furniture | pages [19] -->
m

<!-- b000789 | furniture | pages [19] -->
m

<!-- b000790 | furniture | pages [19] -->
m

<!-- b000791 | furniture | pages [19] -->
m

<!-- b000792 | furniture | pages [19] -->
m

<!-- b000793 | furniture | pages [19] -->
m

<!-- b000794 | furniture | pages [19] -->
m

<!-- b000795 | furniture | pages [19] -->
m

<!-- b000796 | furniture | pages [19] -->
m

<!-- b000797 | furniture | pages [19] -->
m

<!-- b000798 | furniture | pages [19] -->
m

<!-- b000799 | furniture | pages [19] -->
m

<!-- b000800 | furniture | pages [19] -->
m

<!-- b000801 | furniture | pages [19] -->
m

<!-- b000802 | furniture | pages [19] -->
m

<!-- b000803 | furniture | pages [19] -->
m

<!-- b000804 | furniture | pages [19] -->
m

<!-- b000805 | furniture | pages [19] -->
m

<!-- b000806 | furniture | pages [19] -->
m

<!-- b000807 | furniture | pages [19] -->
m

<!-- b000808 | furniture | pages [19] -->
m

<!-- b000809 | furniture | pages [19] -->
m

<!-- b000810 | furniture | pages [19] -->
m

<!-- b000811 | furniture | pages [19] -->
m

<!-- b000812 | furniture | pages [19] -->
m

<!-- b000813 | furniture | pages [19] -->
m

<!-- b000814 | furniture | pages [19] -->
m

<!-- b000815 | furniture | pages [19] -->
m

<!-- b000816 | furniture | pages [19] -->
m

<!-- b000817 | furniture | pages [19] -->
m

<!-- b000818 | furniture | pages [19] -->
m

<!-- b000819 | furniture | pages [19] -->
m

<!-- b000820 | furniture | pages [19] -->
m

<!-- b000821 | furniture | pages [19] -->
m

<!-- b000822 | furniture | pages [19] -->
m

<!-- b000823 | furniture | pages [19] -->
m

<!-- b000824 | furniture | pages [19] -->
m

<!-- b000825 | furniture | pages [19] -->
m

<!-- b000826 | furniture | pages [19] -->
m

<!-- b000827 | furniture | pages [19] -->
m

<!-- b000828 | furniture | pages [19] -->
m

<!-- b000829 | furniture | pages [19] -->
m

<!-- b000830 | furniture | pages [19] -->
m

<!-- b000831 | furniture | pages [19] -->
m

<!-- b000832 | furniture | pages [19] -->
m

<!-- b000833 | furniture | pages [19] -->
m

<!-- b000834 | furniture | pages [19] -->
m

<!-- b000835 | furniture | pages [19] -->
m

<!-- b000836 | furniture | pages [19] -->
m

<!-- b000837 | furniture | pages [19] -->
m

<!-- b000838 | furniture | pages [19] -->
m

<!-- b000839 | furniture | pages [19] -->
m

<!-- b000840 | furniture | pages [19] -->
m

<!-- b000841 | furniture | pages [19] -->
m

<!-- b000842 | furniture | pages [19] -->
m

<!-- b000843 | furniture | pages [19] -->
m

<!-- b000844 | furniture | pages [19] -->
m

<!-- b000845 | furniture | pages [19] -->
m

<!-- b000846 | furniture | pages [19] -->
m

<!-- b000847 | furniture | pages [19] -->
m

<!-- b000848 | furniture | pages [19] -->
m

<!-- b000849 | furniture | pages [19] -->
m

<!-- b000850 | furniture | pages [19] -->
m

<!-- b000851 | furniture | pages [19] -->
m

<!-- b000852 | furniture | pages [19] -->
m

<!-- b000853 | furniture | pages [19] -->
m

<!-- b000854 | furniture | pages [19] -->
m

<!-- b000855 | furniture | pages [19] -->
m

<!-- b000856 | furniture | pages [19] -->
m

<!-- b000857 | furniture | pages [19] -->
m

<!-- b000858 | furniture | pages [19] -->
m

<!-- b000859 | furniture | pages [19] -->
m

<!-- b000860 | furniture | pages [19] -->
m

<!-- b000861 | furniture | pages [19] -->
m

<!-- b000862 | furniture | pages [19] -->
m

<!-- b000863 | furniture | pages [19] -->
m

<!-- b000864 | furniture | pages [19] -->
m

<!-- b000865 | furniture | pages [19] -->
m

<!-- b000866 | furniture | pages [19] -->
m

<!-- b000867 | furniture | pages [19] -->
m

<!-- b000868 | furniture | pages [19] -->
m

<!-- b000869 | furniture | pages [19] -->
m

<!-- b000870 | furniture | pages [19] -->
m

<!-- b000871 | furniture | pages [19] -->
m

<!-- b000872 | furniture | pages [19] -->
m

<!-- b000873 | furniture | pages [19] -->
m

<!-- b000874 | furniture | pages [19] -->
m

<!-- b000875 | furniture | pages [19] -->
m

<!-- b000876 | furniture | pages [19] -->
m

<!-- b000877 | furniture | pages [19] -->
m

<!-- b000878 | furniture | pages [19] -->
m

<!-- b000879 | furniture | pages [19] -->
m

<!-- b000880 | furniture | pages [19] -->
m

<!-- b000881 | furniture | pages [19] -->
m

<!-- b000882 | furniture | pages [19] -->
m

<!-- b000883 | furniture | pages [19] -->
m

<!-- b000884 | furniture | pages [19] -->
m

<!-- b000885 | furniture | pages [19] -->
m

<!-- b000886 | furniture | pages [19] -->
m

<!-- b000887 | furniture | pages [19] -->
m

<!-- b000888 | furniture | pages [19] -->
m

<!-- b000889 | furniture | pages [19] -->
m

<!-- b000890 | furniture | pages [19] -->
m

<!-- b000891 | furniture | pages [19] -->
m

<!-- b000892 | furniture | pages [19] -->
m

<!-- b000893 | furniture | pages [19] -->
m

<!-- b000894 | furniture | pages [19] -->
m

<!-- b000895 | furniture | pages [19] -->
m

<!-- b000896 | furniture | pages [19] -->
m

<!-- b000897 | furniture | pages [19] -->
m

<!-- b000898 | furniture | pages [19] -->
m

<!-- b000899 | furniture | pages [19] -->
m

<!-- b000900 | furniture | pages [19] -->
m

<!-- b000901 | furniture | pages [19] -->
m

<!-- b000902 | furniture | pages [19] -->
m

<!-- b000903 | furniture | pages [19] -->
m

<!-- b000904 | furniture | pages [19] -->
m

<!-- b000905 | furniture | pages [19] -->
m

<!-- b000906 | furniture | pages [19] -->
m

<!-- b000907 | furniture | pages [19] -->
m

<!-- b000908 | furniture | pages [19] -->
m

<!-- b000909 | furniture | pages [19] -->
m

<!-- b000910 | furniture | pages [19] -->
m

<!-- b000911 | furniture | pages [19] -->
m

<!-- b000912 | furniture | pages [19] -->
m

<!-- b000913 | furniture | pages [19] -->
m

<!-- b000914 | furniture | pages [19] -->
m

<!-- b000915 | furniture | pages [19] -->
m

<!-- b000916 | furniture | pages [19] -->
m

<!-- b000917 | furniture | pages [19] -->
m

<!-- b000918 | furniture | pages [19] -->
m

<!-- b000919 | furniture | pages [19] -->
m

<!-- b000920 | furniture | pages [19] -->
m

<!-- b000921 | furniture | pages [19] -->
m

<!-- b000922 | furniture | pages [19] -->
m

<!-- b000923 | furniture | pages [19] -->
m

<!-- b000924 | furniture | pages [19] -->
m

<!-- b000925 | furniture | pages [19] -->
m

<!-- b000926 | furniture | pages [19] -->
m

<!-- b000927 | furniture | pages [19] -->
m

<!-- b000928 | furniture | pages [19] -->
m

<!-- b000929 | furniture | pages [19] -->
m

<!-- b000930 | furniture | pages [19] -->
m

<!-- b000931 | furniture | pages [19] -->
m

<!-- b000932 | furniture | pages [19] -->
m

<!-- b000933 | furniture | pages [19] -->
m

<!-- b000934 | furniture | pages [19] -->
m

<!-- b000935 | furniture | pages [19] -->
m

<!-- b000936 | furniture | pages [19] -->
m

<!-- b000937 | furniture | pages [19] -->
m

<!-- b000938 | furniture | pages [19] -->
m

<!-- b000939 | furniture | pages [19] -->
m

<!-- b000940 | furniture | pages [19] -->
m

<!-- b000941 | furniture | pages [19] -->
m

<!-- b000942 | furniture | pages [19] -->
m

<!-- b000943 | furniture | pages [19] -->
m

<!-- b000944 | furniture | pages [19] -->
m

<!-- b000945 | furniture | pages [19] -->
m

<!-- b000946 | furniture | pages [19] -->
m

<!-- b000947 | furniture | pages [19] -->
m

<!-- b000948 | furniture | pages [19] -->
m

<!-- b000949 | furniture | pages [19] -->
m

<!-- b000950 | furniture | pages [19] -->
m

<!-- b000951 | furniture | pages [19] -->
m

<!-- b000952 | furniture | pages [19] -->
m

<!-- b000953 | furniture | pages [19] -->
m

<!-- b000954 | furniture | pages [19] -->
m

<!-- b000955 | furniture | pages [19] -->
m

<!-- b000956 | furniture | pages [19] -->
m

<!-- b000957 | furniture | pages [19] -->
m

<!-- b000958 | furniture | pages [19] -->
m

<!-- b000959 | furniture | pages [19] -->
m

<!-- b000960 | furniture | pages [19] -->
m

<!-- b000961 | furniture | pages [19] -->
m

<!-- b000962 | furniture | pages [19] -->
m

<!-- b000963 | furniture | pages [19] -->
m

<!-- b000964 | furniture | pages [19] -->
m

<!-- b000965 | furniture | pages [19] -->
m

<!-- b000966 | furniture | pages [19] -->
m

<!-- b000967 | furniture | pages [19] -->
m

<!-- b000968 | furniture | pages [19] -->
m

<!-- b000969 | furniture | pages [19] -->
m

<!-- b000970 | furniture | pages [19] -->
m

<!-- b000971 | furniture | pages [19] -->
m

<!-- b000972 | furniture | pages [19] -->
m

<!-- b000973 | furniture | pages [20] -->
Team 2522820

<!-- b000974 | furniture | pages [20] -->
Page 20

<!-- b000976 | prose | pages [20] -->
3. When the difference in points between consecutive games is less than or equal to −3s, call these negative change points.

<!-- b000977 | prose | pages [20] -->
4. Let segments be the years between positive and negative change points.

<!-- b000978 | prose | pages [20] -->
5. If a positive change point is followed by another positive change point before a negative change point appears, combine the segments.

<!-- b000979 | prose | pages [20] -->
6. For each segment, calculate the z-score of x compared to the population distribution of points: x−µ σ .

<!-- b000980 | prose | pages [20] -->
7. Choose segments with x that have z-scores greater than or equal to 1.5—these indicate the great coach effect.

<!-- b000981 | prose | pages [20] -->
8. For each of these chosen segments, calculate the coefficient of variation: s x.

<!-- b000982 | heading | pages [20] -->
4.1.3 Results and Notable Findings

<!-- b000983 | prose | pages [20] -->
It was impractical to apply this analysis to all pairs of countries and sports, so we chose the 20 countries with the highest points over the history of the Games. Though many great coaches have coached teams outside of these top 20 countries, it is reasonable to assume that many of these top-performing countries have achieved such success at least partly due to the great coach effect, making it more likely that our model detects instances of the effect for these countries’ performances.

<!-- b000984 | prose | pages [20] -->
The table below shows the top 10 segments, ranked by order of decreasing z-score.

<!-- b000985 | caption | pages [20] -->
Table 16: Analysis of Significant Performance Changes in Olympic Sports

<!-- b000986 | prose | pages [20] -->
Year Z-Score Coefficient Country (Sport)

<!-- b000987 | prose | pages [20] -->
Start End of Variation

<!-- b000988 | prose | pages [20] -->
1972 1976 2.497 0.222 Romania (Handball) 2004 2008 2.284 0.286 Canada (Trampolining) 1996 2000 2.264 0.353 Russia (Diving) 2004 2008 2.207 0.622 China (Trampolining) 2000 2004 2.167 0.667 Russia (Basketball) 2000 2004 2.146 0.374 Russia (Weightlifting) 1984 2004 2.143 0.547 South Korea (Handball) 1996 2016 2.100 0.286 Russia (Modern Pentathlon) 1908 1912 2.076 0.766 Netherlands (Fencing) 1996 2000 2.070 0.182 Australia (Basketball)

<!-- b000989 | prose | pages [20] -->
Here, the start year is the year before the potential great coach effect, and the end year is the last year of the potential great coach effect. Matching with known information about coaches, many of these results line up with the leadership of coaches who may be considered “great”: the 1976 Romanian handball team was coached by Radu Voina, who won the world championship and three Olympic medals himself;[3] the 2008 Canadian trampolining team was coached by David Ross, whose club athletes have won seven Olympic medals;[4] and so on. Many of these coaches had very successful coaching careers and may be considered particularly great coaches, even among the exceedingly high standards that Olympic coaches are held to.

<!-- b000990 | prose | pages [20] -->
Most of these great coach effects last only for one Games, but this makes sense when considering the fact that it is common for coaches to switch teams: in a particularly notable case, Lang Ping, the “great” volleyball

<!-- b000991 | prose | pages [20, 21] -->
关注数学模型 coach, coached the Chinese team to silver in 1996, the American team to silver in 2008, and the Chinese team to 微信公众号：数学模型 gold in 2016.

<!-- b000992 | furniture | pages [20] -->
2

<!-- b000993 | furniture | pages [20] -->
MATHmodels

<!-- b000994 | furniture | pages [20] -->
获取更多资讯

<!-- b000995 | furniture | pages [21] -->
Team 2522820

<!-- b000996 | furniture | pages [21] -->
Page 21

<!-- b000998 | prose | pages [21] -->
This is why we did not use the coefficient of variation as a variable in determining whether a segment of successful performances was likely to be due to the great coach effect: it would disqualify some segments with high coefficients of variation even though they were no less likely than other segments with lower coefficients of variation to be due to the great coach effect. However, we still included it in the table because it allows for greater interpretability of the data. For instance, we can tell that Australia consistently performed well around 1996 to 2000 because of its relatively low coefficient of variation value of 0.182, even though it did not reach our requirements to extend the segment.

<!-- b000999 | heading | pages [21] -->
4.2 Estimating Impacts of Great Coaches

<!-- b001000 | prose | pages [21] -->
微信号：MATHmodels Our model from 4.1 gave us many valuable insights that can be used not only to find potential instances of the great coach effect but also to estimate the impacts of these great coaches. For each of the top 20 country-sport pairs we found with the highest z-scores, we calculated C:

<!-- b001001 | prose | pages [21] -->
C = (Ps −µ · L) · 100%.

<!-- b001002 | prose | pages [21] -->
This is the percentage of points that can be assumed to be due to the great coach effect out of the country’s historical point count for that sport.

<!-- b001003 | caption | pages [21] -->
Table 17: Top 10 Countries with Highest Contributions in Olympic Sports

<!-- b001004 | prose | pages [21] -->
Year Contribution (%) Country (Sport)

<!-- b001005 | prose | pages [21] -->
Start End

<!-- b001006 | prose | pages [21] -->
1988 2012 100.0 Sweden (Handball) 1980 2004 100.0 United States (Synchronized Swimming) 1996 2016 88.9 Russia (Modern Pentathlon) 1984 2004 80.8 South Korea (Handball) 1968 1988 59.6 Hungary (Weightlifting) 1904 1908 55.0 Great Britain (Tug-Of-War) 1924 1928 50.0 Germany (Water Polo) 1908 1912 40.0 Netherlands (Fencing) 2004 2008 38.9 China (Trampolining) 1972 1976 33.3 Romania (Handball)

<!-- b001007 | prose | pages [21] -->
Based on this table, we can see that the dominance of the United States’ synchronized swimming teams from 1984 to 2004 and of Sweden’s handball teams from 1992 to 2012 accounted for 100% of their points over their entire history competing at the Games for those sports. Indeed, great coaches had a hand in these dominant runs: Gail Emery—whose athletes won 14 gold and silver medals in the Olympics and 23 gold and silver medals in World Championships[5]—coached the United States synchronized swimming team from 1988 to 1996, and Bengt Johansson coached the Swedish handball team from 1988 to 2004. In fact, Johansson’s coaching ability was so influential that, under his leadership, the Swedish handball team were known as the Bengan Boys, after his first name.[6] Another notable detail is that, as soon as these great coaches left their positions, their teams experienced a negative change point, immediately ending their segments of increased performance. This suggests that the influence of coaches may only last during their direct involvement and that great coaches have limited influence in improving their teams to the extent that they continue to improve even after the coaches have left.

<!-- b001008 | prose | pages [21] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001009 | furniture | pages [21] -->
m

<!-- b001010 | furniture | pages [21] -->
m

<!-- b001011 | furniture | pages [21] -->
m

<!-- b001012 | furniture | pages [21] -->
m

<!-- b001013 | furniture | pages [21] -->
m

<!-- b001014 | furniture | pages [21] -->
m

<!-- b001015 | furniture | pages [21] -->
m

<!-- b001016 | furniture | pages [21] -->
m

<!-- b001017 | furniture | pages [21] -->
m

<!-- b001018 | furniture | pages [21] -->
m

<!-- b001019 | furniture | pages [21] -->
m

<!-- b001020 | furniture | pages [21] -->
m

<!-- b001021 | furniture | pages [21] -->
m

<!-- b001022 | furniture | pages [21] -->
m

<!-- b001023 | furniture | pages [21] -->
m

<!-- b001024 | furniture | pages [21] -->
m

<!-- b001025 | furniture | pages [21] -->
m

<!-- b001026 | furniture | pages [21] -->
m

<!-- b001027 | furniture | pages [21] -->
m

<!-- b001028 | furniture | pages [21] -->
m

<!-- b001029 | furniture | pages [21] -->
m

<!-- b001030 | furniture | pages [21] -->
m

<!-- b001031 | furniture | pages [21] -->
m

<!-- b001032 | furniture | pages [21] -->
m

<!-- b001033 | furniture | pages [21] -->
m

<!-- b001034 | furniture | pages [21] -->
m

<!-- b001035 | furniture | pages [21] -->
m

<!-- b001036 | furniture | pages [21] -->
m

<!-- b001037 | furniture | pages [21] -->
m

<!-- b001038 | furniture | pages [21] -->
m

<!-- b001039 | furniture | pages [21] -->
m

<!-- b001040 | furniture | pages [21] -->
m

<!-- b001041 | furniture | pages [21] -->
m

<!-- b001042 | furniture | pages [21] -->
m

<!-- b001043 | furniture | pages [21] -->
m

<!-- b001044 | furniture | pages [21] -->
m

<!-- b001045 | furniture | pages [21] -->
m

<!-- b001046 | furniture | pages [21] -->
m

<!-- b001047 | furniture | pages [21] -->
m

<!-- b001048 | furniture | pages [21] -->
m

<!-- b001049 | furniture | pages [21] -->
m

<!-- b001050 | furniture | pages [21] -->
m

<!-- b001051 | furniture | pages [21] -->
m

<!-- b001052 | furniture | pages [21] -->
m

<!-- b001053 | furniture | pages [21] -->
m

<!-- b001054 | furniture | pages [21] -->
m

<!-- b001055 | furniture | pages [21] -->
m

<!-- b001056 | furniture | pages [21] -->
m

<!-- b001057 | furniture | pages [21] -->
m

<!-- b001058 | furniture | pages [21] -->
m

<!-- b001059 | furniture | pages [21] -->
m

<!-- b001060 | furniture | pages [21] -->
m

<!-- b001061 | furniture | pages [21] -->
m

<!-- b001062 | furniture | pages [21] -->
m

<!-- b001063 | furniture | pages [21] -->
m

<!-- b001064 | furniture | pages [21] -->
m

<!-- b001065 | furniture | pages [21] -->
m

<!-- b001066 | furniture | pages [21] -->
m

<!-- b001067 | furniture | pages [21] -->
m

<!-- b001068 | furniture | pages [21] -->
m

<!-- b001069 | furniture | pages [21] -->
m

<!-- b001070 | furniture | pages [21] -->
m

<!-- b001071 | furniture | pages [21] -->
m

<!-- b001072 | furniture | pages [21] -->
m

<!-- b001073 | furniture | pages [21] -->
m

<!-- b001074 | furniture | pages [21] -->
m

<!-- b001075 | furniture | pages [21] -->
m

<!-- b001076 | furniture | pages [21] -->
m

<!-- b001077 | furniture | pages [21] -->
m

<!-- b001078 | furniture | pages [21] -->
m

<!-- b001079 | furniture | pages [21] -->
m

<!-- b001080 | furniture | pages [21] -->
m

<!-- b001081 | furniture | pages [21] -->
m

<!-- b001082 | furniture | pages [21] -->
m

<!-- b001083 | furniture | pages [21] -->
m

<!-- b001084 | furniture | pages [21] -->
m

<!-- b001085 | furniture | pages [21] -->
m

<!-- b001086 | furniture | pages [21] -->
m

<!-- b001087 | furniture | pages [21] -->
m

<!-- b001088 | furniture | pages [21] -->
m

<!-- b001089 | furniture | pages [21] -->
m

<!-- b001090 | furniture | pages [21] -->
m

<!-- b001091 | furniture | pages [21] -->
m

<!-- b001092 | furniture | pages [21] -->
m

<!-- b001093 | furniture | pages [21] -->
m

<!-- b001094 | furniture | pages [21] -->
m

<!-- b001095 | furniture | pages [21] -->
m

<!-- b001096 | furniture | pages [21] -->
m

<!-- b001097 | furniture | pages [21] -->
m

<!-- b001098 | furniture | pages [21] -->
m

<!-- b001099 | furniture | pages [21] -->
m

<!-- b001100 | furniture | pages [21] -->
m

<!-- b001101 | furniture | pages [21] -->
m

<!-- b001102 | furniture | pages [21] -->
m

<!-- b001103 | furniture | pages [21] -->
m

<!-- b001104 | furniture | pages [21] -->
m

<!-- b001105 | furniture | pages [21] -->
m

<!-- b001106 | furniture | pages [21] -->
m

<!-- b001107 | furniture | pages [21] -->
m

<!-- b001108 | furniture | pages [21] -->
m

<!-- b001109 | furniture | pages [21] -->
m

<!-- b001110 | furniture | pages [21] -->
m

<!-- b001111 | furniture | pages [21] -->
m

<!-- b001112 | furniture | pages [21] -->
m

<!-- b001113 | furniture | pages [21] -->
m

<!-- b001114 | furniture | pages [21] -->
m

<!-- b001115 | furniture | pages [21] -->
m

<!-- b001116 | furniture | pages [21] -->
m

<!-- b001117 | furniture | pages [21] -->
m

<!-- b001118 | furniture | pages [21] -->
m

<!-- b001119 | furniture | pages [21] -->
m

<!-- b001120 | furniture | pages [21] -->
m

<!-- b001121 | furniture | pages [21] -->
m

<!-- b001122 | furniture | pages [21] -->
m

<!-- b001123 | furniture | pages [21] -->
m

<!-- b001124 | furniture | pages [21] -->
m

<!-- b001125 | furniture | pages [21] -->
m

<!-- b001126 | furniture | pages [21] -->
m

<!-- b001127 | furniture | pages [21] -->
m

<!-- b001128 | furniture | pages [21] -->
m

<!-- b001129 | furniture | pages [21] -->
m

<!-- b001130 | furniture | pages [21] -->
m

<!-- b001131 | furniture | pages [21] -->
m

<!-- b001132 | furniture | pages [21] -->
m

<!-- b001133 | furniture | pages [21] -->
m

<!-- b001134 | furniture | pages [21] -->
m

<!-- b001135 | furniture | pages [21] -->
m

<!-- b001136 | furniture | pages [21] -->
m

<!-- b001137 | furniture | pages [21] -->
m

<!-- b001138 | furniture | pages [21] -->
m

<!-- b001139 | furniture | pages [21] -->
m

<!-- b001140 | furniture | pages [21] -->
m

<!-- b001141 | furniture | pages [21] -->
m

<!-- b001142 | furniture | pages [21] -->
m

<!-- b001143 | furniture | pages [21] -->
m

<!-- b001144 | furniture | pages [21] -->
m

<!-- b001145 | furniture | pages [21] -->
m

<!-- b001146 | furniture | pages [21] -->
m

<!-- b001147 | furniture | pages [21] -->
m

<!-- b001148 | furniture | pages [21] -->
m

<!-- b001149 | furniture | pages [21] -->
m

<!-- b001150 | furniture | pages [21] -->
m

<!-- b001151 | furniture | pages [21] -->
m

<!-- b001152 | furniture | pages [21] -->
m

<!-- b001153 | furniture | pages [21] -->
m

<!-- b001154 | furniture | pages [21] -->
m

<!-- b001155 | furniture | pages [21] -->
m

<!-- b001156 | furniture | pages [21] -->
m

<!-- b001157 | furniture | pages [21] -->
m

<!-- b001158 | furniture | pages [21] -->
m

<!-- b001159 | furniture | pages [21] -->
m

<!-- b001160 | furniture | pages [21] -->
m

<!-- b001161 | furniture | pages [21] -->
m

<!-- b001162 | furniture | pages [21] -->
m

<!-- b001163 | furniture | pages [21] -->
m

<!-- b001164 | furniture | pages [21] -->
m

<!-- b001165 | furniture | pages [21] -->
m

<!-- b001166 | furniture | pages [21] -->
m

<!-- b001167 | furniture | pages [21] -->
m

<!-- b001168 | furniture | pages [21] -->
m

<!-- b001169 | furniture | pages [21] -->
m

<!-- b001170 | furniture | pages [21] -->
m

<!-- b001171 | furniture | pages [21] -->
m

<!-- b001172 | furniture | pages [21] -->
m

<!-- b001173 | furniture | pages [21] -->
m

<!-- b001174 | furniture | pages [21] -->
m

<!-- b001175 | furniture | pages [21] -->
m

<!-- b001176 | furniture | pages [21] -->
m

<!-- b001177 | furniture | pages [21] -->
m

<!-- b001178 | furniture | pages [21] -->
m

<!-- b001179 | furniture | pages [21] -->
m

<!-- b001180 | furniture | pages [21] -->
m

<!-- b001181 | furniture | pages [21] -->
m

<!-- b001182 | furniture | pages [21] -->
m

<!-- b001183 | furniture | pages [21] -->
m

<!-- b001184 | furniture | pages [21] -->
m

<!-- b001185 | furniture | pages [21] -->
m

<!-- b001186 | furniture | pages [21] -->
m

<!-- b001187 | furniture | pages [21] -->
m

<!-- b001188 | furniture | pages [21] -->
m

<!-- b001189 | furniture | pages [21] -->
m

<!-- b001190 | furniture | pages [21] -->
m

<!-- b001191 | furniture | pages [21] -->
m

<!-- b001192 | furniture | pages [21] -->
m

<!-- b001193 | furniture | pages [21] -->
m

<!-- b001194 | furniture | pages [21] -->
m

<!-- b001195 | furniture | pages [21] -->
m

<!-- b001196 | furniture | pages [21] -->
m

<!-- b001197 | furniture | pages [21] -->
m

<!-- b001198 | furniture | pages [21] -->
m

<!-- b001199 | furniture | pages [21] -->
m

<!-- b001200 | furniture | pages [21] -->
m

<!-- b001201 | furniture | pages [21] -->
m

<!-- b001202 | furniture | pages [21] -->
m

<!-- b001203 | furniture | pages [21] -->
m

<!-- b001204 | furniture | pages [21] -->
m

<!-- b001205 | furniture | pages [21] -->
m

<!-- b001206 | furniture | pages [21] -->
m

<!-- b001207 | furniture | pages [21] -->
m

<!-- b001208 | furniture | pages [21] -->
m

<!-- b001209 | furniture | pages [21] -->
m

<!-- b001210 | furniture | pages [21] -->
m

<!-- b001211 | furniture | pages [21] -->
m

<!-- b001212 | furniture | pages [21] -->
m

<!-- b001213 | furniture | pages [21] -->
m

<!-- b001214 | furniture | pages [21] -->
m

<!-- b001215 | furniture | pages [21] -->
m

<!-- b001216 | furniture | pages [21] -->
m

<!-- b001217 | furniture | pages [21] -->
m

<!-- b001218 | furniture | pages [21] -->
m

<!-- b001219 | furniture | pages [21] -->
m

<!-- b001220 | furniture | pages [21] -->
m

<!-- b001221 | furniture | pages [21] -->
m

<!-- b001222 | furniture | pages [21] -->
m

<!-- b001223 | furniture | pages [21] -->
m

<!-- b001224 | furniture | pages [21] -->
m

<!-- b001225 | furniture | pages [21] -->
m

<!-- b001226 | furniture | pages [21] -->
m

<!-- b001227 | furniture | pages [21] -->
m

<!-- b001228 | furniture | pages [21] -->
m

<!-- b001229 | furniture | pages [21] -->
m

<!-- b001230 | furniture | pages [21] -->
m

<!-- b001231 | furniture | pages [21] -->
m

<!-- b001232 | furniture | pages [21] -->
m

<!-- b001233 | furniture | pages [21] -->
m

<!-- b001234 | furniture | pages [21] -->
m

<!-- b001235 | furniture | pages [21] -->
m

<!-- b001236 | furniture | pages [21] -->
m

<!-- b001237 | furniture | pages [21] -->
m

<!-- b001238 | furniture | pages [21] -->
m

<!-- b001239 | furniture | pages [21] -->
m

<!-- b001240 | furniture | pages [21] -->
m

<!-- b001241 | furniture | pages [21] -->
m

<!-- b001242 | furniture | pages [21] -->
m

<!-- b001243 | furniture | pages [21] -->
m

<!-- b001244 | furniture | pages [21] -->
m

<!-- b001245 | furniture | pages [21] -->
m

<!-- b001246 | furniture | pages [21] -->
m

<!-- b001247 | furniture | pages [21] -->
m

<!-- b001248 | furniture | pages [21] -->
m

<!-- b001249 | furniture | pages [21] -->
m

<!-- b001250 | furniture | pages [21] -->
m

<!-- b001251 | furniture | pages [21] -->
m

<!-- b001252 | furniture | pages [21] -->
m

<!-- b001253 | furniture | pages [21] -->
m

<!-- b001254 | furniture | pages [21] -->
m

<!-- b001255 | furniture | pages [21] -->
m

<!-- b001256 | furniture | pages [21] -->
m

<!-- b001257 | furniture | pages [21] -->
m

<!-- b001258 | furniture | pages [21] -->
m

<!-- b001259 | furniture | pages [21] -->
m

<!-- b001260 | furniture | pages [21] -->
m

<!-- b001261 | furniture | pages [21] -->
m

<!-- b001262 | furniture | pages [21] -->
m

<!-- b001263 | furniture | pages [21] -->
m

<!-- b001264 | furniture | pages [21] -->
m

<!-- b001265 | furniture | pages [21] -->
m

<!-- b001266 | furniture | pages [21] -->
m

<!-- b001267 | furniture | pages [21] -->
m

<!-- b001268 | furniture | pages [21] -->
m

<!-- b001269 | furniture | pages [21] -->
m

<!-- b001270 | furniture | pages [21] -->
m

<!-- b001271 | furniture | pages [21] -->
m

<!-- b001272 | furniture | pages [21] -->
m

<!-- b001273 | furniture | pages [21] -->
m

<!-- b001274 | furniture | pages [21] -->
m

<!-- b001275 | furniture | pages [21] -->
m

<!-- b001276 | furniture | pages [21] -->
m

<!-- b001277 | furniture | pages [21] -->
m

<!-- b001278 | furniture | pages [21] -->
m

<!-- b001279 | furniture | pages [21] -->
m

<!-- b001280 | furniture | pages [21] -->
m

<!-- b001281 | furniture | pages [21] -->
m

<!-- b001282 | furniture | pages [21] -->
m

<!-- b001283 | furniture | pages [21] -->
m

<!-- b001284 | furniture | pages [21] -->
m

<!-- b001285 | furniture | pages [21] -->
m

<!-- b001286 | furniture | pages [21] -->
m

<!-- b001287 | furniture | pages [21] -->
m

<!-- b001288 | furniture | pages [21] -->
m

<!-- b001289 | furniture | pages [21] -->
m

<!-- b001290 | furniture | pages [21] -->
m

<!-- b001291 | furniture | pages [21] -->
m

<!-- b001292 | furniture | pages [21] -->
m

<!-- b001293 | furniture | pages [21] -->
m

<!-- b001294 | furniture | pages [21] -->
m

<!-- b001295 | furniture | pages [21] -->
m

<!-- b001296 | furniture | pages [21] -->
m

<!-- b001297 | furniture | pages [21] -->
m

<!-- b001298 | furniture | pages [21] -->
m

<!-- b001299 | furniture | pages [21] -->
m

<!-- b001300 | furniture | pages [21] -->
m

<!-- b001301 | furniture | pages [21] -->
m

<!-- b001302 | furniture | pages [21] -->
m

<!-- b001303 | furniture | pages [21] -->
m

<!-- b001304 | furniture | pages [21] -->
m

<!-- b001305 | furniture | pages [21] -->
m

<!-- b001306 | furniture | pages [21] -->
m

<!-- b001307 | furniture | pages [21] -->
m

<!-- b001308 | furniture | pages [21] -->
m

<!-- b001309 | furniture | pages [21] -->
m

<!-- b001310 | furniture | pages [21] -->
m

<!-- b001311 | furniture | pages [21] -->
m

<!-- b001312 | furniture | pages [21] -->
m

<!-- b001313 | furniture | pages [21] -->
m

<!-- b001314 | furniture | pages [21] -->
m

<!-- b001315 | furniture | pages [21] -->
m

<!-- b001316 | furniture | pages [21] -->
m

<!-- b001317 | furniture | pages [21] -->
m

<!-- b001318 | furniture | pages [21] -->
m

<!-- b001319 | furniture | pages [21] -->
m

<!-- b001320 | furniture | pages [21] -->
m

<!-- b001321 | furniture | pages [21] -->
m

<!-- b001322 | furniture | pages [21] -->
m

<!-- b001323 | furniture | pages [21] -->
m

<!-- b001324 | furniture | pages [21] -->
m

<!-- b001325 | furniture | pages [21] -->
m

<!-- b001326 | furniture | pages [21] -->
m

<!-- b001327 | furniture | pages [21] -->
m

<!-- b001328 | furniture | pages [21] -->
m

<!-- b001329 | furniture | pages [21] -->
m

<!-- b001330 | furniture | pages [21] -->
m

<!-- b001331 | furniture | pages [21] -->
m

<!-- b001332 | furniture | pages [21] -->
m

<!-- b001333 | furniture | pages [22] -->
Team 2522820

<!-- b001334 | furniture | pages [22] -->
Page 22

<!-- b001335 | heading | pages [22] -->
4.3 Identifying Country-Sport Pairs Fit for Great Coaches and Estimating Impacts

<!-- b001336 | prose | pages [22] -->
Similarly, we can interpret the results of our model from 4.1 yet another way to identify country-sport pairs that would particularly benefit from investing in great coaches. For the same set of the top 20 country-sport pairs we found with the highest z-scores that we used in 4.2, we calculated ∆Pnorm:

<!-- b001337 | prose | pages [22] -->
L = Ps −µ · L ∆Pnorm = C . L This is the value that great coaches add to the given sport, normalized per Games so they can be compared with values for different sports. Countries should invest in coaches for sports where performances have been shown to be greatly affected by great coaches. It is also reasonable for countries to invest in great coaches for sports that they have previously excelled in under the leadership of great coaches in hopes of replicating previous success.

<!-- b001338 | caption | pages [22] -->
Table 18: Top 10 Countries with Highest ∆Pnorm in Olympic Sports

<!-- b001339 | prose | pages [22] -->
∆Pnorm Year Country (Sport)

<!-- b001340 | prose | pages [22] -->
Start End

<!-- b001341 | prose | pages [22] -->
1980 1984 42.0 Romania (Rowing) 2000 2004 20.0 Russia (Weightlifting) 1996 2000 19.0 Russia (Diving) 2004 2008 14.0 China (Trampolining) 2000 2004 12.0 China (Taekwondo) 1904 1908 11.0 Great Britain (Tug-Of-War) 1968 1988 6.8 Hungary (Weightlifting) 1980 2004 6.7 United States (Synchronized Swimming) 2004 2008 6.0 Canada (Trampolining) 1992 1996 6.0 United States (Softball)

<!-- b001342 | prose | pages [22] -->
From this table, it is important to note that the 1984 Olympics were an anomaly because it took place in Los Angeles and was the target of boycotts from many of the Eastern Bloc nations, which played a major role in the anomalous success of the Romanian rowing teams.[7] Aside from this outlier, Russia could benefit from investing in a great coach for weightlifting: in 2004, Russia’s weightlifting athletes were coached by David Rigert, who set 65 world records and won an Olympic m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m gold himself.[8] m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m China could benefit from investing in a great coach for trampolining, based on the success of its 2008 athletes. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Hungary could benefit from investing in a great coach for weightlifting, based on the success of its athletes m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m from 1972 to 1988. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Outside of these three countries, it seems that weightlifting and trampolining are especially high return-on- m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001343 | prose | pages [22] -->
interest investments for great coaches, as they both appeared twice in this list of the highest values added by great coaches.

<!-- b001344 | prose | pages [22] -->
Conveniently, these ∆Pnorm are precisely the predicted points that these countries would gain if they invested in great coaches: we predict that Russia’s investing in a great weightlifting coach could lead to up to 20 points, that China’s investing in a great trampolining coach could lead to up to 14 points, and that Hungary’s investing in a great weightlifting coach could lead to up to 6.8 points.

<!-- b001345 | heading | pages [22] -->
5 Problem 3: Insights into Olympic Medal Counts

<!-- b001346 | prose | pages [22] -->
Purely based on the regression results, it is clear that the United States dominating is sensible given their previous record and their host status in 2028. Some unexpected results include Germany and China’s performance,

<!-- b001347 | prose | pages [22, 23] -->
关注数学模型 as China worsened in medal count quite a bit from 2024 and Germany came out of nowhere to take second place in gold medals. There are multitudes more observations like this to make, and they can be predicted to be due to any amount of reasons. Since the model accounts for unobserved effects, it’s entirely possible that this is representative of some culture change or effect of China’s governmental policy, or really anything under the sun 微信公众号：数学模型 that can be thought up.

<!-- b001348 | furniture | pages [22] -->
2

<!-- b001349 | furniture | pages [22] -->
MATHmodels

<!-- b001350 | furniture | pages [22] -->
获取更多资讯

<!-- b001351 | furniture | pages [23] -->
Team 2522820

<!-- b001352 | furniture | pages [23] -->
Page 23

<!-- b001354 | prose | pages [23] -->
Though we tried our best to predict the medal counts, there is a large confidence interval associated with the predictions, so in the end it is likely true that Number of Athletes, Host Status, and Past Performance are not sufficient indicators (at least through our method of regression) of Olympic medal performance. We suspect this is due to a lack of an economic/political factor, since that understandably has a major impact and there has been many cases where politics (such as political regimes) have affected the outcome of the Olympics much more than these predictors have. In addition, for developing countries (especially ones on track to earn their first medal), economic factors are many times more important than number of athletes or past performance, and countries at this level will definitely not be hosting. There is a large discrepancy in the number of countries performing poorly at the Olympics. An interesting question is whether this is a good thing or a bad thing: does the dominance of the United States and other developed countries motivate or demotivate developing countries 微信号：MATHmodels to try to place in future Olympics? From a first world perspective, it may seem like we are giving them a chance to participate, and we are definitely doing so for the select few great talents from these countries. However, resources are overwhelmingly skewed for developed countries as are medal counts, as is especially highlighted in our 2028 predictions. Is it not in the interest of both high caliber players and coaches to gravitate towards where these resources are concentrated? The Olympic Committee should carefully consider how sports are chosen and how resources are allocated (to the extent they can), as this is very influential to the medal distribution.

<!-- b001355 | heading | pages [23] -->
6 Strengths and Weaknesses

<!-- b001356 | heading | pages [23] -->
6.1 Hierarchical Regression Model

<!-- b001357 | prose | pages [23] -->
A strength of our model is that, by implementing mixed effects and clusters, it is able to account for various levels of unobserved random effects that can influence medal counts. There are many factors that influence how a country performs at the individual competitor level or national level, so many that we cannot account for them all. So, our model implements random variables at the cluster and individual country level for each parameter to attempt to account for this, allowing for a more realistic prediction that isn’t just purely data driven. In addition, our model appropriately accounts for the zero-inflation/censoring of Olympic medal data by using a Hurdle model approach with a probit regression to find probability of earning 0 medals or not.

<!-- b001358 | prose | pages [23] -->
One weakness about this model is it’s fit. Maximizing the Log Likelihood function would lead to a good fit, but during implementation the optimization did not converge for many methods of optimization. This inevitably led to log likelihoods and AIC/BIC fits that were subpar. Though we tried to account for this by weighting one of the clusters to reduce heteroscedasticity, it didn’t help the convergence issue. This may imply the nature of the data is different from how our model assumes it to be (in fact it is, since we tested the data to still be heteroscedastic even after improvements). One improvement we explored was to use a Hamiltonian Monte Carlo optimization to replace MLE, but this approach did not end up working. Some approach that accounts for the heteroscedasticity error would improve the model significantly.

<!-- b001359 | heading | pages [23] -->
6.2 Time Series Analysis with Moving Average Model

<!-- b001360 | prose | pages [23] -->
Our model’s main strength lies in its moving average, which allowed us to interpret anomalous performances in the context of performances immediately before and after it. This, in turn, allowed us to create segments of increased performance, which we interpreted as possible signs of the great coach effect. This was much

<!-- b001361 | prose | pages [23, 24] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m more effective than identifying individual anomalous performances by considering only the population mean and standard deviation instead of the rolling statistics we used.

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

<!-- b001686 | furniture | pages [24] -->
m

<!-- b001687 | furniture | pages [24] -->
m

<!-- b001688 | furniture | pages [24] -->
m

<!-- b001689 | furniture | pages [24] -->
m

<!-- b001690 | furniture | pages [24] -->
m

<!-- b001691 | furniture | pages [24] -->
m

<!-- b001692 | furniture | pages [24] -->
m

<!-- b001693 | furniture | pages [24] -->
m

<!-- b001694 | furniture | pages [24] -->
m

<!-- b001695 | furniture | pages [24] -->
m

<!-- b001696 | furniture | pages [24] -->
m

<!-- b001697 | furniture | pages [24] -->
m

<!-- b001698 | furniture | pages [24] -->
m

<!-- b001699 | furniture | pages [24] -->
m

<!-- b001700 | furniture | pages [24] -->
m

<!-- b001701 | furniture | pages [24] -->
m

<!-- b001702 | furniture | pages [24] -->
m

<!-- b001703 | furniture | pages [24] -->
m

<!-- b001704 | furniture | pages [24] -->
m

<!-- b001705 | furniture | pages [24] -->
m

<!-- b001706 | furniture | pages [24] -->
m

<!-- b001707 | furniture | pages [24] -->
m

<!-- b001708 | furniture | pages [24] -->
m

<!-- b001709 | furniture | pages [24] -->
m

<!-- b001710 | furniture | pages [24] -->
m

<!-- b001711 | furniture | pages [24] -->
m

<!-- b001712 | furniture | pages [24] -->
m

<!-- b001713 | furniture | pages [24] -->
m

<!-- b001714 | furniture | pages [24] -->
m

<!-- b001715 | furniture | pages [24] -->
m

<!-- b001716 | furniture | pages [24] -->
m

<!-- b001717 | furniture | pages [24] -->
m

<!-- b001718 | furniture | pages [24] -->
m

<!-- b001719 | furniture | pages [24] -->
m

<!-- b001720 | furniture | pages [24] -->
m

<!-- b001721 | furniture | pages [24] -->
m

<!-- b001722 | furniture | pages [24] -->
m

<!-- b001723 | furniture | pages [24] -->
m

<!-- b001724 | furniture | pages [24] -->
m

<!-- b001725 | furniture | pages [24] -->
m

<!-- b001726 | furniture | pages [24] -->
m

<!-- b001727 | furniture | pages [24] -->
m

<!-- b001728 | furniture | pages [24] -->
m

<!-- b001729 | furniture | pages [24] -->
m

<!-- b001730 | furniture | pages [24] -->
m

<!-- b001731 | furniture | pages [24] -->
m

<!-- b001732 | furniture | pages [24] -->
m

<!-- b001733 | furniture | pages [24] -->
m

<!-- b001734 | furniture | pages [24] -->
m

<!-- b001735 | furniture | pages [24] -->
m

<!-- b001736 | furniture | pages [24] -->
m

<!-- b001737 | furniture | pages [24] -->
m

<!-- b001738 | furniture | pages [24] -->
m

<!-- b001739 | furniture | pages [24] -->
m

<!-- b001740 | furniture | pages [24] -->
m

<!-- b001741 | furniture | pages [24] -->
m

<!-- b001742 | furniture | pages [24] -->
m

<!-- b001743 | furniture | pages [24] -->
m

<!-- b001744 | furniture | pages [24] -->
m

<!-- b001745 | furniture | pages [24] -->
m

<!-- b001746 | furniture | pages [24] -->
m

<!-- b001747 | furniture | pages [24] -->
m

<!-- b001748 | furniture | pages [24] -->
m

<!-- b001749 | furniture | pages [24] -->
m

<!-- b001750 | furniture | pages [24] -->
m

<!-- b001751 | furniture | pages [24] -->
m

<!-- b001752 | furniture | pages [24] -->
m

<!-- b001753 | furniture | pages [24] -->
m

<!-- b001754 | furniture | pages [24] -->
m

<!-- b001755 | furniture | pages [24] -->
m

<!-- b001756 | furniture | pages [24] -->
m

<!-- b001757 | furniture | pages [24] -->
m

<!-- b001758 | furniture | pages [24] -->
m

<!-- b001759 | furniture | pages [24] -->
m

<!-- b001760 | furniture | pages [24] -->
m

<!-- b001761 | furniture | pages [24] -->
m

<!-- b001762 | furniture | pages [24] -->
m

<!-- b001763 | furniture | pages [24] -->
m

<!-- b001764 | furniture | pages [24] -->
m

<!-- b001765 | furniture | pages [24] -->
m

<!-- b001766 | furniture | pages [24] -->
m

<!-- b001767 | furniture | pages [24] -->
m

<!-- b001768 | furniture | pages [24] -->
m

<!-- b001769 | furniture | pages [24] -->
m

<!-- b001770 | furniture | pages [24] -->
m

<!-- b001771 | furniture | pages [24] -->
m

<!-- b001772 | furniture | pages [24] -->
m

<!-- b001773 | furniture | pages [24] -->
m

<!-- b001774 | furniture | pages [24] -->
m

<!-- b001775 | furniture | pages [24] -->
m

<!-- b001776 | furniture | pages [24] -->
m

<!-- b001777 | furniture | pages [24] -->
m

<!-- b001778 | furniture | pages [24] -->
m

<!-- b001779 | furniture | pages [24] -->
m

<!-- b001780 | furniture | pages [24] -->
m

<!-- b001781 | furniture | pages [24] -->
m

<!-- b001782 | furniture | pages [24] -->
m

<!-- b001783 | furniture | pages [24] -->
m

<!-- b001784 | furniture | pages [24] -->
m

<!-- b001785 | furniture | pages [24] -->
m

<!-- b001786 | furniture | pages [24] -->
m

<!-- b001787 | furniture | pages [24] -->
m

<!-- b001788 | furniture | pages [24] -->
m

<!-- b001789 | furniture | pages [24] -->
m

<!-- b001790 | furniture | pages [24] -->
m

<!-- b001791 | furniture | pages [24] -->
m

<!-- b001792 | furniture | pages [24] -->
m

<!-- b001793 | furniture | pages [24] -->
m

<!-- b001794 | furniture | pages [24] -->
m

<!-- b001795 | furniture | pages [24] -->
m

<!-- b001796 | furniture | pages [24] -->
m

<!-- b001797 | furniture | pages [24] -->
m

<!-- b001798 | furniture | pages [24] -->
m

<!-- b001799 | furniture | pages [24] -->
m

<!-- b001800 | furniture | pages [24] -->
m

<!-- b001801 | furniture | pages [24] -->
m

<!-- b001802 | furniture | pages [24] -->
m

<!-- b001803 | furniture | pages [24] -->
m

<!-- b001804 | furniture | pages [24] -->
m

<!-- b001805 | furniture | pages [24] -->
m

<!-- b001806 | furniture | pages [24] -->
m

<!-- b001807 | furniture | pages [24] -->
m

<!-- b001808 | furniture | pages [24] -->
m

<!-- b001809 | furniture | pages [24] -->
m

<!-- b001810 | furniture | pages [24] -->
m

<!-- b001811 | furniture | pages [24] -->
m

<!-- b001812 | furniture | pages [24] -->
m

<!-- b001813 | furniture | pages [24] -->
m

<!-- b001814 | furniture | pages [24] -->
m

<!-- b001815 | furniture | pages [24] -->
m

<!-- b001816 | furniture | pages [24] -->
m

<!-- b001817 | furniture | pages [24] -->
m

<!-- b001818 | furniture | pages [24] -->
m

<!-- b001819 | furniture | pages [24] -->
m

<!-- b001820 | furniture | pages [24] -->
m

<!-- b001821 | furniture | pages [24] -->
m

<!-- b001822 | furniture | pages [24] -->
m

<!-- b001823 | furniture | pages [24] -->
m

<!-- b001824 | furniture | pages [24] -->
m

<!-- b001825 | furniture | pages [24] -->
m

<!-- b001826 | furniture | pages [24] -->
m

<!-- b001827 | furniture | pages [24] -->
m

<!-- b001828 | furniture | pages [24] -->
m

<!-- b001829 | furniture | pages [24] -->
m

<!-- b001830 | furniture | pages [24] -->
m

<!-- b001831 | furniture | pages [24] -->
m

<!-- b001832 | furniture | pages [24] -->
m

<!-- b001833 | furniture | pages [24] -->
m

<!-- b001834 | furniture | pages [24] -->
m

<!-- b001835 | furniture | pages [24] -->
m

<!-- b001836 | furniture | pages [24] -->
m

<!-- b001837 | furniture | pages [24] -->
m

<!-- b001838 | furniture | pages [24] -->
m

<!-- b001839 | furniture | pages [24] -->
m

<!-- b001840 | furniture | pages [24] -->
m

<!-- b001841 | furniture | pages [24] -->
m

<!-- b001842 | furniture | pages [24] -->
m

<!-- b001843 | furniture | pages [24] -->
m

<!-- b001844 | furniture | pages [24] -->
m

<!-- b001845 | furniture | pages [24] -->
m

<!-- b001846 | furniture | pages [24] -->
m

<!-- b001847 | furniture | pages [24] -->
m

<!-- b001848 | furniture | pages [24] -->
m

<!-- b001849 | furniture | pages [24] -->
m

<!-- b001850 | furniture | pages [24] -->
m

<!-- b001851 | furniture | pages [24] -->
m

<!-- b001852 | furniture | pages [24] -->
m

<!-- b001853 | furniture | pages [24] -->
m

<!-- b001854 | furniture | pages [24] -->
m

<!-- b001855 | furniture | pages [24] -->
m

<!-- b001856 | furniture | pages [24] -->
m

<!-- b001857 | furniture | pages [24] -->
m

<!-- b001858 | furniture | pages [24] -->
m

<!-- b001859 | furniture | pages [24] -->
m

<!-- b001860 | furniture | pages [24] -->
m

<!-- b001861 | furniture | pages [24] -->
m

<!-- b001862 | furniture | pages [24] -->
m

<!-- b001863 | furniture | pages [24] -->
m

<!-- b001864 | furniture | pages [24] -->
m

<!-- b001865 | furniture | pages [24] -->
m

<!-- b001866 | furniture | pages [24] -->
m

<!-- b001867 | furniture | pages [24] -->
m

<!-- b001868 | furniture | pages [24] -->
m

<!-- b001869 | furniture | pages [24] -->
m

<!-- b001870 | furniture | pages [24] -->
m

<!-- b001871 | furniture | pages [24] -->
m

<!-- b001872 | furniture | pages [24] -->
m

<!-- b001873 | furniture | pages [24] -->
m

<!-- b001874 | furniture | pages [24] -->
m

<!-- b001875 | furniture | pages [24] -->
m

<!-- b001876 | furniture | pages [24] -->
m

<!-- b001877 | furniture | pages [24] -->
m

<!-- b001878 | furniture | pages [24] -->
m

<!-- b001879 | furniture | pages [24] -->
m

<!-- b001880 | furniture | pages [24] -->
m

<!-- b001881 | furniture | pages [24] -->
m

<!-- b001882 | furniture | pages [24] -->
m

<!-- b001883 | furniture | pages [24] -->
m

<!-- b001884 | furniture | pages [24] -->
m

<!-- b001885 | furniture | pages [24] -->
m

<!-- b001886 | furniture | pages [24] -->
m

<!-- b001887 | furniture | pages [24] -->
m

<!-- b001888 | furniture | pages [24] -->
m

<!-- b001889 | furniture | pages [24] -->
m

<!-- b001890 | furniture | pages [24] -->
m

<!-- b001891 | furniture | pages [24] -->
m

<!-- b001892 | furniture | pages [24] -->
m

<!-- b001893 | furniture | pages [24] -->
m

<!-- b001894 | furniture | pages [24] -->
m

<!-- b001895 | furniture | pages [24] -->
m

<!-- b001896 | furniture | pages [24] -->
m

<!-- b001897 | furniture | pages [24] -->
m

<!-- b001898 | furniture | pages [24] -->
m

<!-- b001899 | furniture | pages [24] -->
m

<!-- b001900 | furniture | pages [24] -->
m

<!-- b001901 | furniture | pages [24] -->
m

<!-- b001902 | furniture | pages [24] -->
m

<!-- b001903 | furniture | pages [24] -->
m

<!-- b001904 | furniture | pages [24] -->
m

<!-- b001905 | furniture | pages [24] -->
m

<!-- b001906 | furniture | pages [24] -->
m

<!-- b001907 | furniture | pages [24] -->
m

<!-- b001908 | furniture | pages [24] -->
m

<!-- b001909 | furniture | pages [24] -->
m

<!-- b001910 | furniture | pages [24] -->
m

<!-- b001911 | furniture | pages [24] -->
m

<!-- b001912 | furniture | pages [24] -->
m

<!-- b001913 | furniture | pages [24] -->
m

<!-- b001914 | furniture | pages [24] -->
m

<!-- b001915 | furniture | pages [24] -->
m

<!-- b001916 | furniture | pages [24] -->
m

<!-- b001917 | furniture | pages [24] -->
m

<!-- b001918 | furniture | pages [24] -->
m

<!-- b001919 | furniture | pages [24] -->
m

<!-- b001920 | furniture | pages [24] -->
m

<!-- b001921 | furniture | pages [24] -->
m

<!-- b001922 | furniture | pages [24] -->
m

<!-- b001923 | furniture | pages [24] -->
m

<!-- b001924 | furniture | pages [24] -->
m

<!-- b001925 | furniture | pages [24] -->
m

<!-- b001926 | furniture | pages [24] -->
m

<!-- b001927 | furniture | pages [24] -->
m

<!-- b001928 | furniture | pages [24] -->
m

<!-- b001929 | furniture | pages [24] -->
m

<!-- b001930 | furniture | pages [24] -->
m

<!-- b001931 | furniture | pages [24] -->
m

<!-- b001932 | furniture | pages [24] -->
m

<!-- b001933 | furniture | pages [24] -->
m

<!-- b001934 | furniture | pages [24] -->
m

<!-- b001935 | furniture | pages [24] -->
m

<!-- b001936 | furniture | pages [24] -->
m

<!-- b001937 | furniture | pages [24] -->
m

<!-- b001938 | furniture | pages [24] -->
m

<!-- b001939 | furniture | pages [24] -->
m

<!-- b001940 | furniture | pages [24] -->
m

<!-- b001941 | furniture | pages [24] -->
m

<!-- b001942 | furniture | pages [24] -->
m

<!-- b001943 | furniture | pages [24] -->
m

<!-- b001944 | furniture | pages [24] -->
m

<!-- b001945 | furniture | pages [24] -->
m

<!-- b001946 | furniture | pages [24] -->
m

<!-- b001947 | furniture | pages [24] -->
m

<!-- b001948 | furniture | pages [24] -->
m

<!-- b001949 | furniture | pages [24] -->
m

<!-- b001950 | furniture | pages [24] -->
m

<!-- b001951 | furniture | pages [24] -->
m

<!-- b001952 | furniture | pages [24] -->
m

<!-- b001953 | furniture | pages [24] -->
m

<!-- b001954 | furniture | pages [24] -->
m

<!-- b001955 | furniture | pages [24] -->
m

<!-- b001956 | furniture | pages [24] -->
m

<!-- b001957 | furniture | pages [24] -->
m

<!-- b001958 | furniture | pages [24] -->
m

<!-- b001959 | furniture | pages [24] -->
m

<!-- b001960 | furniture | pages [24] -->
m

<!-- b001961 | furniture | pages [24] -->
m

<!-- b001962 | furniture | pages [24] -->
m

<!-- b001963 | furniture | pages [24] -->
m

<!-- b001964 | furniture | pages [24] -->
m

<!-- b001965 | furniture | pages [24] -->
m

<!-- b001966 | furniture | pages [24] -->
m

<!-- b001967 | furniture | pages [24] -->
m

<!-- b001968 | furniture | pages [24] -->
m

<!-- b001969 | furniture | pages [24] -->
m

<!-- b001970 | furniture | pages [24] -->
m

<!-- b001971 | furniture | pages [24] -->
m

<!-- b001972 | furniture | pages [24] -->
m

<!-- b001973 | furniture | pages [24] -->
m

<!-- b001974 | furniture | pages [24] -->
m

<!-- b001975 | furniture | pages [24] -->
m

<!-- b001976 | furniture | pages [24] -->
m

<!-- b001977 | furniture | pages [24] -->
m

<!-- b001978 | furniture | pages [24] -->
m

<!-- b001979 | furniture | pages [24] -->
m

<!-- b001980 | furniture | pages [24] -->
m

<!-- b001981 | furniture | pages [24] -->
m

<!-- b001982 | furniture | pages [24] -->
m

<!-- b001983 | furniture | pages [24] -->
m

<!-- b001984 | furniture | pages [24] -->
m

<!-- b001985 | furniture | pages [24] -->
m

<!-- b001986 | furniture | pages [24] -->
Team 2522820

<!-- b001987 | furniture | pages [24] -->
Page 24

<!-- b001989 | prose | pages [24] -->
The main weakness of our model is that there is no way to determine whether anomalous performances were due to the great coach effect or any number of outside influences without manually comparing our findings to historical great coaches. Because of the limited data, this is inevitable.

<!-- b001990 | heading | pages [24] -->
7 Conclusion

<!-- b001991 | prose | pages [24] -->
The Olympics is not only a stage for athletes to show off their skills, but for countries to establish their presence in the world. Developing countries are increasingly entering the Olympics, and their participation adds a new layer of competition and uncertainty to the Games. As the Olympics continue to grow in scope and diversity, the ability to predict medal counts becomes increasingly complex. By leveraging statistical models to investigate data on Olympic medal distributions, we have explored the nature of such data and how it is affected by great coaches.

<!-- b001992 | prose | pages [24] -->
关注数学模型

<!-- b001993 | furniture | pages [24] -->
2

<!-- b001994 | furniture | pages [24] -->
MATHmodels

<!-- b001995 | furniture | pages [24] -->
获取更多资讯

<!-- b001996 | furniture | pages [25] -->
Page 25

<!-- b001997 | furniture | pages [25] -->
Team 2522820

<!-- b001998 | heading | pages [25] -->
8 Works Cited

<!-- b001999 | heading | pages [25] -->
1. Swaddling, J., & British Museum. Trustees. (2008). The ancient Olympic games (2nd ed., rev.updated.).

<!-- b002000 | prose | pages [25] -->
University of Texas Press.

<!-- b002001 | prose | pages [25] -->
2. Scelles, N., Andreff, W., Bonnal, L., Andreff, M. and Favard, P. (2020), Forecasting National Medal Totals at the Summer Olympic Games Reconsidered. Social Science Quarterly, 101: 697-711. https:

<!-- b002002 | prose | pages [25] -->
//doi.org/10.1111/ssqu.12782

<!-- b002003 | prose | pages [25] -->
3. Costeiu, A. (2012, May 30). Voina's Last Two Games for Romania. European Handball Federation.

<!-- b002004 | prose | pages [25] -->
https://www.eurohandball.com/en/news/en/voina-s-last-two-games-for-romania/

<!-- b002005 | prose | pages [25] -->
4. Patience Is the Key to Talent Identification and Development: Olympic Trampoline Coach. (2021, October 14). Sport for Life.https://sportforlife.ca/blog/ patience-is-the-key-to-talent-identification-and-development-olympic-trampoline-coach/

<!-- b002006 | heading | pages [25] -->
5. Gail Emery. (2024, March 25). International Swimming Hall of Fame. https: //ishof.org/honoree/

<!-- b002007 | prose | pages [25] -->
honoree-gail-emery/ S 6. Bruun, P. (2013, September 9). Memories of a “Bengan Boy." European Handball Federation. https:

<!-- b002008 | prose | pages [25] -->
//www.eurohandball.com/en/news/en/memories-of-a-bengan-boy/

<!-- b002009 | prose | pages [25] -->
7. Kobierecki, Micha 1. (2015). Boycott of the Los Angeles 1984 Olympic Games as an Exam- ple of Political Play-Acting of the Cold War Superpowers. Polish Political Science Yearbook. 44.

<!-- b002010 | prose | pages [25] -->
10.15804/ppsy2015008. MATHm 1 /     r  t ) e r ./ liftup/1_galleryResult.asp?a_id=217

<!-- b002011 | prose | pages [25] -->
微信 ● ● 微信
