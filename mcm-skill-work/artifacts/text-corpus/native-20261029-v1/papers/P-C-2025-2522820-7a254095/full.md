# P-C-2025-2522820-7a254095

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2025

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | prose | pages [1] -->
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
As modelers, we have been tasked with predicting the outcome of the 2028 Summer Olympics held in Los Angeles, United States.

<!-- b000014 | prose | pages [1] -->
Olympic medal data exhibits censorship in the form of zero inflation, so we first consider a Tobit Model that considers random noise and unobserved random effects, optimized with a Maximum Likelihood Estimate. From regression analysis on the Tobit Model, we discovered it suffered from heteroscedasticity, which is detrimental to the Tobit model. So, we implement a Hierarchical Mixed Linear Effects Model to predict medal counts based on Host Status, Number of Athletes, and Past Performance. Country performance was split into clusters using Density-Based Spatial Clustering of Applications with Noise (DBSCAN), splitting the countries into three clusters. The Mixed Linear Effects Model is then used to perform a Negative Binomial Regression based on the predictors, as well as a Probit Regression in the low-performing cluster to determine probability of earning 0 medals.

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
We predicted the Top 3 (in gold count) countries in the 2028 Summer Olympics to be the United States (48), Germany (28), and China (25), each with a 95% confidence interval range of around 30. The top three countries that we predict will improve the most in terms of ranking is Jamaica (+27), Germany (+8), and Ukraine (+8), and the worst performance changes in ranking we predict are Canada (-99), the Netherlands (-31), and South Korea (-10). Finally, our model also predicts that the countries that will earn their first Olympic medal in 2028 are Angola and Saar, with odds of 32.54% and 40.08%, respectively.

<!-- b000017 | prose | pages [1] -->
After analyzing the dynamics of the rankings, we wanted to understand the impact of events and sports on the rankings. To do this, we created a ranking system of Gold 6 points, Silver 3 Points, and Bronze 2 points. Then, through Singular Value Decomposition, Sport-Point Efficiency, and Revealed Comparative Advantage, we were able to understand the influence sports and events had on the ranking of various countries.

<!-- b000018 | prose | pages [1] -->
We also analyzed past performances at the Games to identify possible instances of the great coach effect, or the influence of a great coach in leading teams to anomalous successes. To build our model, we noticed that performances at the Games are time series, so we used a time series analysis incorporating a moving average. We found that the 1976 Romanian Handball team, the 2008 Canadian trampolining team, and the 2000 Russian diving team were the most likely to have experienced the great coach effect.

<!-- b000019 | prose | pages [1] -->
By using a contribution metric, we used the same model to find the country-sport pairs where the great coach effect was likely to have made the greatest impact on the country’s performance. We found that the 1992-2012 Swedish handball teams, the 1984-2004 United States synchronized swimming teams, and the 2000-2016 Russian modern pentathlon athletes likely benefited the most from the great coach effect, with the Swedish handball and United States synchronized swimming athletes earning 100% of their medals during segments where they were led by great coaches, according to our model. Similarly, by using a relative contribution metric, we suggested that Russia invest in a great weightlifting coach, China invest in a great trampolining coach, and Hungary invest in a great weightlifting coach. Based on their performances under great coaches, these investments could lead to up to 20 points for Russia, 14 points for China, and 6.8 points for Hungary.

<!-- b000020 | prose | pages [1] -->
All of these results were cross-referenced with historical Olympic coaches, and many of our findings lined up with the leadership of coaches that may be considered great.

<!-- b000021 | prose | pages [1] -->
There are a multitude of benefits in this research—such as understanding how to best allocate resources—but more than that, just as the Games represent the human desire for unity in excellence, these models represent our fundamental desire to understand the world.

<!-- b000022 | furniture | pages [3] -->
Team 2522820

<!-- b000023 | furniture | pages [3] -->
Page 3

<!-- b000024 | prose | pages [3] -->
1

<!-- b000025 | heading | pages [3] -->
Introduction

<!-- b000026 | prose | pages [3] -->
“The Olympics remain the most compelling search for excellence that exists in sport, and maybe in life itself.” —Dawn Fraser, eight-time Olympic medalist.

<!-- b000027 | prose | pages [3] -->
The Olympic tradition traces back almost three millennia to Olympia in Ancient Greece. Even in an era of

<!-- b000028 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000029 | prose | pages [3] -->
constant conflict between the city-states, the ancient Games represented humanity’s unified pursuit of excellence. The Ancient Greeks even established a temporary Olympic Truce to ensure the safety of the athletes: unity in competition took precedence.[1]

<!-- b000030 | prose | pages [3] -->
The modern Olympic Games, established in 1896, have inherited this humanistic spirit. The modern Games have gathered the best athletes from around the world in their common pursuit not just of athletic excellence, but of reaching the limits of human potential and bringing our culturally diverse world closer together in the process. The models we present in this paper aim to understand the factors behind these competitions.

<!-- b000031 | prose | pages [3] -->
1.1

<!-- b000032 | heading | pages [3] -->
Problem Restatement

<!-- b000033 | prose | pages [3] -->
1.

<!-- b000034 | prose | pages [3] -->
(a) Predict the medal table for the Los Angeles 2028 Summer Olympics. Provide prediction intervals for

<!-- b000035 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000036 | prose | pages [3] -->
all medal predictions, and predict which countries will improve the most and worsen the most based on their 2024 performance.

<!-- b000037 | prose | pages [3] -->
(b) Then, predict which countries will earn their first Olympic medal ever in the 2028 Olympics, providing

<!-- b000038 | prose | pages [3] -->
odds for the estimate.

<!-- b000039 | prose | pages [3] -->
(c) Consider how different sports and sports specialties play into country performance in a given

<!-- b000040 | prose | pages [3] -->
Olympics and explore how events chosen by hosting countries affect results.

<!-- b000041 | prose | pages [3] -->
2.

<!-- b000042 | prose | pages [3] -->
(a) Create a mathematical model that finds potential cases of the “great coach effect,” or the positive

<!-- b000043 | prose | pages [3] -->
influence of a great coach on a country’s performance in a discipline.

<!-- b000044 | prose | pages [3] -->
(b) Use this model to estimate the impact of such potential great coaches on their countries’ performances.

<!-- b000045 | prose | pages [3] -->
(c) Interpret the results of this model to identify three country-sport pairs that great coaches would bring

<!-- b000046 | prose | pages [3] -->
most value to, and estimate the potential impact of hiring great coaches for these three country-sport pairs.

<!-- b000047 | prose | pages [3] -->
3.

<!-- b000048 | prose | pages [3] -->
(a) Discuss original insights about Olympic medal counts, and explain how these insights can be used

<!-- b000049 | prose | pages [3] -->
to inform Olympic Committee decisions for future Olympics.

<!-- b000050 | prose | pages [3] -->
2 Data Pre-Processing

<!-- b000051 | prose | pages [3] -->
To easily analyze the given data, the CSV files datasets given by the International Olympic Committee (IOC) were converted to SQLite tables. Using Python 3, we were able to easily request, insert, and update relevant information provided by the IOC.

<!-- b000052 | prose | pages [3] -->
Before using any of the given datasets, we adjusted some of the files for easy processing.

<!-- b000053 | prose | pages [3] -->
• summerOly athletes.csv - From 1896 to 2024, many countries changed their official names. This is reflected within the [Team] column of this CSV. To account for naming discrepancies, the [Name of Country (NOC)] column was utilized. The three-letter NOC code was consistent throughout the sheet, so a dictionary of {code : country} was used to associate the NOC code with the country name.

<!-- b000054 | prose | pages [3] -->
• summerOly medal counts.csv - Due to minor discrepancies in spacing and naming conventions, slight changes were made to country names for convenience.

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

<!-- b000740 | furniture | pages [3] -->
m

<!-- b000741 | furniture | pages [3] -->
m

<!-- b000742 | furniture | pages [5] -->
Team 2522820

<!-- b000743 | furniture | pages [5] -->
Page 5

<!-- b000744 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000745 | prose | pages [5] -->
Φ Standard Normal Cumulative Density Function (CDF) ϕ Standard Normal Probability Density Function (PDF) ℓ(β, σ) Observed Variable ti T-statistic SE( ˆβi) Standard Error of Fitted Coefficient ˆβi µ Mean for Negative Binomial Distribution θ Dispersion Factor for Negative Binomial Distribution Z Random Effects Design Matrix b Vector of Linear Combination Coefficients for Z ˆy Predicted y value

<!-- b000746 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000747 | prose | pages [5] -->
3.2

<!-- b000748 | heading | pages [5] -->
General Assumptions

<!-- b000749 | heading | pages [5] -->
1. We assume that the provided data is fully accurate to the results of the Olympics each year.

<!-- b000750 | prose | pages [5] -->
Justification: We plan on using regression to predict the 2028 results, and this regression will be usable only if the data we apply it to is accurate.

<!-- b000751 | heading | pages [5] -->
2. We assume that country performance can be reasonably estimated using predictive factors associated

<!-- b000752 | prose | pages [5] -->
with Host Status, Number of Athletes, and Past Performance.

<!-- b000753 | prose | pages [5] -->
Justification: We have access to limited data for this problem, and do not have access to (for example) expenditures on Olympic training. Therefore, we should be able to use the data presented to us to predict performance, and these are the main factors that we can extract from the data tables that we think can predict performance.

<!-- b000754 | heading | pages [5] -->
3. We assume that the participating countries in the 2028 Summer Olympics are identical to that in

<!-- b000755 | prose | pages [5] -->
the 2024 Olympics.

<!-- b000756 | prose | pages [5] -->
Justification: We do not have data on participating countries in the 2028 Olympics, so we assume all countries that participated in 2024 will also participate (with the exception of Russia, which has had some controversy about participation due to the Ukraine War).

<!-- b000757 | prose | pages [5] -->
3.3

<!-- b000758 | heading | pages [5] -->
Tobit Model

<!-- b000759 | prose | pages [5] -->
The Tobit model accounts for censorship by predicting a latent variable, y∗, instead of directly predicting the observed variable y with the given predictors and previous data. The values y∗and y are related as follows:

<!-- b000760 | prose | pages [5] -->
(

<!-- b000761 | prose | pages [5] -->
if y∗≤0, 0

<!-- b000762 | prose | pages [5] -->
y =

<!-- b000763 | prose | pages [5] -->
y∗ if y∗> 0.

<!-- b000764 | prose | pages [5] -->
The Tobit model attempts to predict the uncensored data itself given only censored data. This fits the framework of Olympic medal counts since, as discussed, zero medal counts can be thought of as censored data. The Tobit model assumes this relationship can be captured from the predictors linearly with the equation

<!-- b000765 | prose | pages [5] -->
y∗= Xβ + ϵ

<!-- b000766 | prose | pages [5] -->
Where X is a matrix with the predictor data and β is a column vector of coefficients (so Xβ is some linear combination of the predictor variables) and ϵ is an error term which is normally distributed with variance σ2.

<!-- b000767 | furniture | pages [6] -->
Team 2522820

<!-- b000768 | furniture | pages [6] -->
Page 6

<!-- b000769 | prose | pages [6] -->
This is usually written as ϵ ∼N(0, σ2). Since our data is limited, we expect that there are discrepancies between what they can predict given the complicated nature of why countries win olympic medals. Generally, ϵ is usually used as a ’noise’ term, but in our implementation we extend this to account for unobserved random effects. To do this, we have both σn (noise) and σu (unobserved effects) that contribute to the variance of ϵ as follows:

<!-- b000770 | prose | pages [6] -->
σ2 = σ2

<!-- b000771 | prose | pages [6] -->
n + σ2

<!-- b000772 | prose | pages [6] -->
u.

<!-- b000773 | prose | pages [6] -->
This ensures that we can capture unobserved effects from factors that we cannot add into linear predictors. From here, our implementation of the Tobit model fits coefficients in β based on previous data to be able to predict y∗

<!-- b000774 | prose | pages [6] -->
given predictors X.

<!-- b000775 | prose | pages [6] -->
3.3.1 Maximum Likelihood Estimate (MLE)

<!-- b000776 | prose | pages [6] -->
Our implementation of the Tobit Model optimizes fit using the Maximum Likelihood Estimate (MLE), which is standard for Tobit models since it can account for both observed and unobserved (censored) parts of the data. Essentially, MLE aims to maximize the likelihood function, which is the probability that y is observed given values of β and σ. Maximizing the likelihood means the fitted coefficients for β and σ yield the largest probability of the actual observed data being observed, which allows us to accurately predict y∗given only predictors X.

<!-- b000777 | prose | pages [6] -->
L(β, σ) = P(y|β, σ)

<!-- b000778 | prose | pages [6] -->
Across many observations (yi) this becomes

<!-- b000779 | prose | pages [6] -->
n Y

<!-- b000780 | prose | pages [6] -->
L(β, σ) = P(y1, y2, . . . yn|β, σ) =

<!-- b000781 | prose | pages [6] -->
P(yi|β, σ)

<!-- b000782 | prose | pages [6] -->
i=1

<!-- b000783 | prose | pages [6] -->
The likelihood function can then be split up into values where yi = 0 (censored) and yi > 0 (uncensored). The Tobit model generally assumes y∗is normally distributed, which is a restricting assumption but can be altered if necessary. When yi = 0, we want to compute P(yi = 0|β, σ) = P(y∗≤0|β, σ), which can be found with the normal cumulative density function (CDF), Φ. When yi > 0, we just want P(y∗= yi|β, σ), which can be found with the normal probability density function (PDF), ϕ. Mathematically this becomes

<!-- b000784 | prose | pages [6] -->
−Xiβ

<!-- b000785 | prose | pages [6] -->
P(y∗≤0|β, σ) = Φ

<!-- b000786 | prose | pages [6] -->


<!-- b000787 | prose | pages [6] -->
σ

<!-- b000788 | prose | pages [6] -->
yi −Xiβ

<!-- b000789 | prose | pages [6] -->
P(y∗= yi|β, σ) = ϕ

<!-- b000790 | prose | pages [6] -->
n Y

<!-- b000791 | prose | pages [6] -->
Y

<!-- b000792 | prose | pages [6] -->
=⇒

<!-- b000793 | prose | pages [6] -->
P(yi|β, σ) =

<!-- b000794 | prose | pages [6] -->
yi=0

<!-- b000795 | prose | pages [6] -->
i=1

<!-- b000796 | prose | pages [6] -->


<!-- b000797 | prose | pages [6] -->
σ

<!-- b000798 | prose | pages [6] -->
−Xiβ

<!-- b000799 | prose | pages [6] -->
 Y

<!-- b000800 | prose | pages [6] -->
yi −Xiβ

<!-- b000801 | prose | pages [6] -->


<!-- b000802 | prose | pages [6] -->
Φ Φ

<!-- b000803 | prose | pages [6] -->
ϕ

<!-- b000804 | prose | pages [6] -->
.

<!-- b000805 | prose | pages [6] -->
σ

<!-- b000806 | prose | pages [6] -->
σ

<!-- b000807 | prose | pages [6] -->
yi>0

<!-- b000808 | prose | pages [6] -->
Aiming to maximize, it helps to take the logarithm of the likelihood function. This helps the function in terms of differentiability (to be maximized), and whatever maximum is achieved for the log of the likelihood function will correspond to a maximum of the likelihood function itself.

<!-- b000809 | prose | pages [6] -->


<!-- b000810 | prose | pages [6] -->
X

<!-- b000811 | prose | pages [6] -->
ℓ(β, σ) = log(L(β, σ)) =

<!-- b000812 | prose | pages [6] -->
log

<!-- b000813 | prose | pages [6] -->
ϕ

<!-- b000814 | prose | pages [6] -->
yi>0

<!-- b000815 | prose | pages [6] -->
yi −Xiβ

<!-- b000816 | prose | pages [6] -->


<!-- b000817 | prose | pages [6] -->


<!-- b000818 | prose | pages [6] -->
0 −Xiβ

<!-- b000819 | prose | pages [6] -->


<!-- b000820 | prose | pages [6] -->
X

<!-- b000821 | prose | pages [6] -->
+

<!-- b000822 | prose | pages [6] -->
log

<!-- b000823 | prose | pages [6] -->
Φ

<!-- b000824 | prose | pages [6] -->
σ

<!-- b000825 | prose | pages [6] -->
σ

<!-- b000826 | prose | pages [6] -->
yi=0

<!-- b000827 | prose | pages [6] -->
Maximizing this (using various numerical methods) give us fitted parameters β and σ for the Tobit model.

<!-- b000828 | prose | pages [6] -->
关注数学模型

<!-- b000829 | furniture | pages [6] -->
2

<!-- b000830 | furniture | pages [6] -->
MATHmodels

<!-- b000831 | furniture | pages [6] -->
获取更多资讯

<!-- b000832 | furniture | pages [7] -->
Team 2522820

<!-- b000833 | furniture | pages [7] -->
Page 7

<!-- b000834 | prose | pages [7] -->
3.3.2 Predictor Analysis and Issues with Tobit

<!-- b000835 | prose | pages [7] -->
We are given limited data on countries to make this prediction, namely only past performance, number of athletes, and host status. Therefore, it is important that we figure out which are influential/significant in predicting medal count. For each year, we first consider the variables Host Status, Num Athletes, Host 4 Years Ago, Host in 4 Years, Past 4 Years Total Medals, and Past 8 Years Total Medals. The Host Status variables

<!-- b000836 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000837 | prose | pages [7] -->
are implemented as binary components. It’s reasonable to think that host status can have a delayed or anticipatory effect, as host countries can prepare for hosting by training their athletes and increasing funding to a higher level than usual. We consider past performance as the last two Olympic performances, since these are likely most indicative of future performance rather than performances further in the past.

<!-- b000838 | prose | pages [7] -->
First, we check for multicollinearity. If two predictors are highly correlated, it’s not very useful to use them both so we can either combine them or only use one. We check this with a heat map of a correlation matrix between predictors over all country performances. We can see a high correlation between Past 4 Years Total Medals and Past 8 Years Total Medals and also Num Athletes in the bottom right 3×3 square. Otherwise, there is not a high correlation with other predictors.

<!-- b000839 | prose | pages [7] -->
Another thing we must check, especially for the Tobit model, is homoscedasticity. The Tobit model relies

<!-- b000840 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000841 | prose | pages [7] -->
on the assumption of homoscedasticity, which means that the variance of the residuals is constant, which can be checked in a residual plot as in Figure 1. As we can see, the variance of the residuals is not constant, so we have a heteroscedastic error. The reason this is an issue is because after fitting our variance for the error term σ, we are assuming error terms follow a constant variance, however we see here that this is not the case. This is particularly bad for the Tobit model since it can make the probability of censoring (getting 0 medals) very inaccurate.

<!-- b000842 | caption | pages [7] -->
Figure 1: Predictor/Regression Analysis

<!-- b000843 | prose | pages [7] -->
Further, we perform regression analysis to see which predictors are most significant. After fitting, each variable gets a T-Stat and p-value, defined as

<!-- b000844 | prose | pages [7] -->
ˆβi

<!-- b000845 | prose | pages [7] -->
ti =

<!-- b000846 | prose | pages [7] -->
SE( ˆβi)

<!-- b000847 | prose | pages [7] -->
Here, βi is the fitted parameter for predictor i and SE(βi) is the standard error, or an uncertainty metric for βi (which can be computed in a few ways, we used the covariance matrix).The p-value is calculated using the t-statistic and the degrees of freedom (excess data to predict on), and it is essentially the probability of

<!-- b000848 | furniture | pages [8] -->
Team 2522820

<!-- b000849 | furniture | pages [8] -->
Page 8

<!-- b000850 | prose | pages [8] -->
that t-statistic being obtained. To determine a statistically significant predictor, it should have a low p-value, generally we want p ≤.05. As we can see, the predictors that have this are Num Athletes, Host in 4 Years, and Past 4 Years Total Medals. From this, we can reasonably eliminate Past 8 Years Total Medals due to multicollinearity and low statistical significance and Host 4 Years Ago for low statistical significance. Though Host Status isn’t statistically significant in this analysis, we may still consider it in the model improvement to see if anything has changed.

<!-- b000851 | prose | pages [8] -->
Variable Host Status Num Athletes Host 4 Years Ago Host in 4 Years Past 4 Years Total Medals Past 8 Years Total Medals Coefficient T-Stat P-Value -4.370 -0.642 0.521 18.356 17.246 0.00 0.092 0.000 0.99 -13.225 -12.608 0.00 3.733 3.683 0.00023 0.453 0.003 .997

<!-- b000852 | caption | pages [8] -->
Table 2: Regression Analysis Results

<!-- b000853 | heading | pages [8] -->
Mixed Linear Models (MLMs) in a Hierarchical Framework

<!-- b000854 | prose | pages [8] -->
3.4

<!-- b000855 | prose | pages [8] -->
We intend to refine the Tobit model by attempting to account for differing levels of variance. The purpose of the random variable is to account for unobserved effects, and there’s no reason to assume this is the same across all countries (in fact, that is quite a bad assumption). We decided to fix this by splitting countries into clusters based on general performance, including separate random variables for each cluster as well as each individual country. This is done in attempt to capture important effects on a country-level and cluster-level scale. These underlying effects could possibly be socioeconomic or geographic, for example low performance can be due to countries that do not have the money to put towards Olympic training.

<!-- b000856 | prose | pages [8] -->
3.4.1 Clusters with DBSCAN

<!-- b000857 | prose | pages [8] -->
First, to form clusters, we used a Density-Based Spatial Clustering of Applications with Noise (DBSCAN) model. DBSCAN is a useful method for us since it specifically designates outliers (noise) as high performing countries are in this data. To get a general metric for country performance, we define ’Points’ as a weighted sum of the number of Gold, Silver, and Bronze medals, with weights 6, 3, and 2 respectively. All weightings are arbitrary—different reputable sources use different weighting systems—but we decided to use this weighting because, to some extent, it has a natural justification, as it follows Zipf’s law. That is,

<!-- b000858 | prose | pages [8] -->
Points = 6 · Gold + 3 · Silver + 2 · Bronze.

<!-- b000859 | prose | pages [8] -->
Then, countries are ranked by their average number of points over the years they competed. The DBSCAN algorithm takes two inputs: eps and min points. min points is the minimum number of points that can be in a cluster, and eps is a distance threshold to define a neighborhood around a ’core points’. A core point has at least min points within distance eps of it, and boundary points to each cluster are points within eps of a core point. DBSCAN algorithmically goes through all points and forms clusters.

<!-- b000860 | prose | pages [8] -->
We wanted to split countries into clusters large enough to perform regression on but also have enough clusters to model some inter-cluster unobserved effect difference. In the end, we decided on 3 clusters (including outliers). Our code took min points = 8 and with a target number of (non-outlier) clusters of 2, we found a fitting eps value through iteration shown in Figure 2.

<!-- b000861 | prose | pages [8] -->
After finding the clusters, we applied a Mixed Effects Linear Model to each cluster, taking special care of Cluster 1 (which included all of the countries that get close to 0 medals).

<!-- b000862 | prose | pages [8] -->
关注数学模型

<!-- b000863 | furniture | pages [8] -->
2

<!-- b000864 | furniture | pages [8] -->
MATHmodels

<!-- b000865 | furniture | pages [8] -->
获取更多资讯

<!-- b000866 | furniture | pages [9] -->
Team 2522820

<!-- b000867 | furniture | pages [9] -->
Page 9

<!-- b000868 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000869 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000870 | caption | pages [9] -->
Figure 2: DBSCAN Cluster Results

<!-- b000871 | prose | pages [9] -->
3.4.2

<!-- b000872 | heading | pages [9] -->
Mixed Linear Models and Hurdle Model

<!-- b000873 | prose | pages [9] -->
We will first describe the model for clusters 0 and -1, then for cluster 1. The Tobit model was a continuous regression model, however since medal counts are discrete we chose to use a Negative Binomial Regression. A Negative Binomial distribution is chosen over a Poisson since the Negative Binomial can account for cases where the variance is greater than the meain (Poisson is too restrictive). For countries in these clusters, we assumed there was close to negligible chance of them getting 0 medals. The Mixed Effects Model takes the following form:

<!-- b000874 | prose | pages [9] -->
yij ∼NBinom(µij, θ)

<!-- b000875 | prose | pages [9] -->
µij = exp(Xijβj + Zijbj)

<!-- b000876 | prose | pages [9] -->
Here i is the index for individual country and j is the index for cluster. θ is a dispersion factor for the negative Now, Zijbj is implementing group-wise random effects for each binomial distribution that is also fitted. parameter in attempt to reduce heteroscedasticity (though this model suffers less from it since we are using Negative Binomial). bj is a vector of random coefficients to apply to each cluster, and these random terms are normally distributed. The matrix Zij is the random-effects design matrix, with predictor inputs that get multiplied with the random effects variables in bj (so Zij is similar to Xij in this manner). This is a ’mixed’ effects model as Xijβj is the fixed part and Zijbj is the random part of the model. Cluster 0 and -1 were fitted this way, with a slightly different process for Cluster 1.

<!-- b000877 | prose | pages [9] -->
The purpose of choosing the Tobit model was to account for censorship, but another way to deal with this is a Hurdle model. It is very similar, first using binary regression (Probit) to determine the probability a country gets 0 medals, and then a Negative Binomial model as previously described for the positive count model. The random effects modeling is identical for the Probit regression, but instead a different link function is used. This is implemented mathematically as follows:

<!-- b000878 | prose | pages [9] -->
P(Yij = 1|Xij, Zij) = Φ(Xijβj + Zijbj)

<!-- b000879 | prose | pages [9] -->
The value P(Yij = 1) is what we are trying to predict in the binary regression (the probability a country gets any medals at all), and we take the cumulative normal distribution of the linear predictor for the probit model. In these mixed linear effects models, it’s useful to think of a link function that relates the linear predictor to the

<!-- b000880 | furniture | pages [11] -->
Team 2522820

<!-- b000881 | prose | pages [11] -->
Rank Country Gold 1 United States 48 [33, 63] 2 Germany 28 [13, 43] 3 China 25 [10, 40] 4 Great Britain 17 [2, 32]

<!-- b000882 | furniture | pages [11] -->
Page 11

<!-- b000883 | prose | pages [11] -->
Silver Bronze Total 43 [32, 54] 45 [13, 77] 136 [108, 164] 23 [12, 34] 22 [0, 44] 73 [45, 101] 18 [7, 29] 27 [0, 54] 70 [42, 98] 19 [8, 30] 17 [0, 38] 53 [25, 81]

<!-- b000884 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000885 | prose | pages [11] -->
5 Japan 16 [1, 31] 6 Australia 13 [0, 28] 7 Italy 11 [0, 26] 9 [0, 20] 13 [0, 35] 38 [10, 38] 17 [6, 28] 19 [0, 41] 49 [21, 77] 10 [0, 21] 20 [0, 43] 41 [13, 69]

<!-- b000886 | caption | pages [11] -->
Table 4: Predicted Medal Counts for Top 7 Gold Medal Countries in 2028 Olympics (with 95% Confidence

<!-- b000887 | prose | pages [11] -->
Intervals)

<!-- b000888 | prose | pages [11] -->
We are also tasked with looking for countries that have improved or gotten worse since the 2024 Olympics. We did this by looking at rank change, setting a minimum medal change threshold of 3 so that it wasn’t just countries that changed a lot even though they all got 0 or low counts.

<!-- b000889 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000890 | prose | pages [11] -->
Rank 2028 Country Rank 2024 Gold 2024 Gold 2028 Rank Change Medal Change Most Improved Jamaica 43 1 16 Germany 10 12 Ukraine 23 3 15 Spain 15 5 7 +27 +6 2 2 28 +8 +16 7 +8 +4 8 8 11 +7 +6 Most Declined Canada 12 9 111 Netherlands 6 15 37 South Korea 8 13 18 France 5 16 11 0 -99 -9 2 -31 -13 6 -10 -7 10 -6 -6

<!-- b000891 | caption | pages [11] -->
Table 5: Countries with Most Significant Changes in Olympic Performance (2024 vs 2028)

<!-- b000892 | prose | pages [11] -->
Projections for Countries Yet to Earn Medals 3.5

<!-- b000893 | prose | pages [11] -->
Our model accounted for countries that generally don’t medal through clustering and a specific binary regression model to determine if those countries do medal in a certain year or not. Our model predicted these values as stated previously in the paper as

<!-- b000894 | prose | pages [11] -->
Predicted Number of Medals = (1 −P(Yij = 0)) · ˆyij

<!-- b000895 | prose | pages [11] -->
Here ˆyij is the number of medals they would earn if they medalled at all, and it is multiplied by the probability of earning a medal. We looked at the list of countries that have never medalled in Olympic history and compared it to our predictions for 2028. We assigned odds to these estimates as the probability these countries medalled at all from our regression (the odds are P(Yij = 1)). We found that two countries, Angola and Saar, are predicted to win 1 medal in the 2028 Olympics and have never won a medal previously, with odds 32.54% and 40.08% respectively.

<!-- b000896 | prose | pages [11] -->
3.6 Analyzing Impacts of Events and Sports

<!-- b000897 | prose | pages [11] -->
Through the information in the data sets, two deciding factors in the performance of a country at the Games were the amount of medals they obtained and the distribution of medals among Gold, Silver, and Bronze.

<!-- b000898 | furniture | pages [12] -->
Team 2522820

<!-- b000899 | furniture | pages [12] -->
Page 12

<!-- b000900 | prose | pages [12] -->
However, before analyzing the impacts of events and sports on the performance of a country at the Games, a lot of processing wasa done to create viable connections between the datasets.

<!-- b000901 | heading | pages [12] -->
Data Processing (Ceiling-Proportion Approximation)

<!-- b000902 | prose | pages [12] -->
3.6.1

<!-- b000903 | prose | pages [12] -->
1. The medal counts.csv file provided the total amount of medals obtained by each country (that wins at least

<!-- b000904 | heading | pages [12] -->
1 medal) and the distribution of those medals during all the Games. However, there is no clear connection

<!-- b000905 | prose | pages [12] -->
to the distribution of those medals to sports and events.

<!-- b000906 | prose | pages [12] -->
2. By using athletes.csv to process specific athletes, this CSV file could be used to total the amount of medals obtained in a specific sport or event (with other parameters like country, year, etc). This was beneficial as it created a distribution of medals to events and sports. However, this created another issue. There was an over counting of medals due to overlapping events. Due to the existence of team events, even if many athletes obtain a medal, it may only be 1 medal for the country. To account for this, programs.csv provided helpful data.

<!-- b000907 | prose | pages [12] -->
3. programs.csv contains information regarding the number of sports per discipline. This meant that there’s a known ceiling to the amount of medals that could be obtained per sport.

<!-- b000908 | prose | pages [12] -->
Since there is a known ceiling, the next step was creating a proportion that could multiply with the ceiling to approximate the medal distribution in sports. Going back to athletes.csv, we were able to find the amount of athletes from a country that obtained a medal in a specific sport. By removing one of the parameters, we could also find the amount of athletes that obtained a medal in a specific sport. These two different values (different in country specification), allowed us to create a proportion between a country’s total athlete medal count in a sport to the total athlete medal count in a sport.

<!-- b000909 | prose | pages [12] -->
Ceiling-Proportion Approximation = Country’s total athlete medal count in a sport

<!-- b000910 | prose | pages [12] -->
· 3 · Total Events per Sport Total athlete medal count in a sport

<!-- b000911 | prose | pages [12] -->
m

<!-- b000912 | prose | pages [12] -->
m

<!-- b000913 | prose | pages [12] -->
m

<!-- b000914 | prose | pages [12] -->
m

<!-- b000915 | prose | pages [12] -->
m

<!-- b000916 | prose | pages [12] -->
m

<!-- b000917 | prose | pages [12] -->
m

<!-- b000918 | prose | pages [12] -->
m

<!-- b000919 | prose | pages [12] -->
m

<!-- b000920 | prose | pages [12] -->
m

<!-- b000921 | prose | pages [12] -->
m

<!-- b000922 | prose | pages [12] -->
m

<!-- b000923 | prose | pages [12] -->
m

<!-- b000924 | prose | pages [12] -->
m

<!-- b000925 | prose | pages [12] -->
m

<!-- b000926 | prose | pages [12] -->
m

<!-- b000927 | prose | pages [12] -->
m

<!-- b000928 | prose | pages [12] -->
m

<!-- b000929 | prose | pages [12] -->
m

<!-- b000930 | prose | pages [12] -->
m

<!-- b000931 | prose | pages [12] -->
m

<!-- b000932 | prose | pages [12] -->
m

<!-- b000933 | prose | pages [12] -->
m

<!-- b000934 | prose | pages [12] -->
m

<!-- b000935 | prose | pages [12] -->
m

<!-- b000936 | prose | pages [12] -->
m

<!-- b000937 | prose | pages [12] -->
m

<!-- b000938 | prose | pages [12] -->
m

<!-- b000939 | prose | pages [12] -->
m

<!-- b000940 | prose | pages [12] -->
m

<!-- b000941 | prose | pages [12] -->
m

<!-- b000942 | prose | pages [12] -->
m

<!-- b000943 | prose | pages [12] -->
m

<!-- b000944 | prose | pages [12] -->
m

<!-- b000945 | prose | pages [12] -->
m

<!-- b000946 | prose | pages [12] -->
m

<!-- b000947 | prose | pages [12] -->
m

<!-- b000948 | prose | pages [12] -->
m

<!-- b000949 | prose | pages [12] -->
m

<!-- b000950 | prose | pages [12] -->
m

<!-- b000951 | prose | pages [12] -->
m

<!-- b000952 | prose | pages [12] -->
m

<!-- b000953 | prose | pages [12] -->
m

<!-- b000954 | prose | pages [12] -->
m

<!-- b000955 | prose | pages [12] -->
m

<!-- b000956 | prose | pages [12] -->
m

<!-- b000957 | prose | pages [12] -->
m

<!-- b000958 | prose | pages [12] -->
m

<!-- b000959 | prose | pages [12] -->
m

<!-- b000960 | prose | pages [12] -->
m

<!-- b000961 | prose | pages [12] -->
m

<!-- b000962 | prose | pages [12] -->
m

<!-- b000963 | prose | pages [12] -->
m

<!-- b000964 | prose | pages [12] -->
This Ceiling-Proportion Approximation would yield an estimate of the amount of medals in a given sport

<!-- b000965 | prose | pages [12] -->
m

<!-- b000966 | prose | pages [12] -->
m

<!-- b000967 | prose | pages [12] -->
m

<!-- b000968 | prose | pages [12] -->
m

<!-- b000969 | prose | pages [12] -->
m

<!-- b000970 | prose | pages [12] -->
m

<!-- b000971 | prose | pages [12] -->
m

<!-- b000972 | prose | pages [12] -->
m

<!-- b000973 | prose | pages [12] -->
m

<!-- b000974 | prose | pages [12] -->
m

<!-- b000975 | prose | pages [12] -->
m

<!-- b000976 | prose | pages [12] -->
m

<!-- b000977 | prose | pages [12] -->
m

<!-- b000978 | prose | pages [12] -->
m

<!-- b000979 | prose | pages [12] -->
m

<!-- b000980 | prose | pages [12] -->
m

<!-- b000981 | prose | pages [12] -->
m

<!-- b000982 | prose | pages [12] -->
m

<!-- b000983 | prose | pages [12] -->
m

<!-- b000984 | prose | pages [12] -->
m

<!-- b000985 | prose | pages [12] -->
m

<!-- b000986 | prose | pages [12] -->
m

<!-- b000987 | prose | pages [12] -->
m

<!-- b000988 | prose | pages [12] -->
m

<!-- b000989 | prose | pages [12] -->
m

<!-- b000990 | prose | pages [12] -->
m

<!-- b000991 | prose | pages [12] -->
m

<!-- b000992 | prose | pages [12] -->
m

<!-- b000993 | prose | pages [12] -->
m

<!-- b000994 | prose | pages [12] -->
m

<!-- b000995 | prose | pages [12] -->
m

<!-- b000996 | prose | pages [12] -->
m

<!-- b000997 | prose | pages [12] -->
m

<!-- b000998 | prose | pages [12] -->
m

<!-- b000999 | prose | pages [12] -->
m

<!-- b001000 | prose | pages [12] -->
m

<!-- b001001 | prose | pages [12] -->
m

<!-- b001002 | prose | pages [12] -->
m

<!-- b001003 | prose | pages [12] -->
m

<!-- b001004 | prose | pages [12] -->
m

<!-- b001005 | prose | pages [12] -->
m

<!-- b001006 | prose | pages [12] -->
m

<!-- b001007 | prose | pages [12] -->
m

<!-- b001008 | prose | pages [12] -->
m

<!-- b001009 | prose | pages [12] -->
m

<!-- b001010 | prose | pages [12] -->
m

<!-- b001011 | prose | pages [12] -->
m

<!-- b001012 | prose | pages [12] -->
m

<!-- b001013 | prose | pages [12] -->
m

<!-- b001014 | prose | pages [12] -->
m

<!-- b001015 | prose | pages [12] -->
m

<!-- b001016 | prose | pages [12] -->
m

<!-- b001017 | prose | pages [12] -->
m

<!-- b001018 | prose | pages [12] -->
m

<!-- b001019 | prose | pages [12] -->
m

<!-- b001020 | prose | pages [12] -->
m

<!-- b001021 | prose | pages [12] -->
m

<!-- b001022 | prose | pages [12] -->
m

<!-- b001023 | prose | pages [12] -->
m

<!-- b001024 | prose | pages [12] -->
m

<!-- b001025 | prose | pages [12] -->
m

<!-- b001026 | prose | pages [12] -->
m

<!-- b001027 | prose | pages [12] -->
m

<!-- b001028 | prose | pages [12] -->
m

<!-- b001029 | prose | pages [12] -->
m

<!-- b001030 | prose | pages [12] -->
m

<!-- b001031 | prose | pages [12] -->
m

<!-- b001032 | prose | pages [12] -->
m

<!-- b001033 | prose | pages [12] -->
m

<!-- b001034 | prose | pages [12] -->
m

<!-- b001035 | prose | pages [12] -->
m

<!-- b001036 | prose | pages [12] -->
m

<!-- b001037 | prose | pages [12] -->
m

<!-- b001038 | prose | pages [12] -->
m

<!-- b001039 | prose | pages [12] -->
m

<!-- b001040 | prose | pages [12] -->
m

<!-- b001041 | prose | pages [12] -->
m

<!-- b001042 | prose | pages [12] -->
m

<!-- b001043 | prose | pages [12] -->
m

<!-- b001044 | prose | pages [12] -->
m

<!-- b001045 | prose | pages [12] -->
m

<!-- b001046 | prose | pages [12] -->
m

<!-- b001047 | prose | pages [12] -->
m

<!-- b001048 | prose | pages [12] -->
m

<!-- b001049 | prose | pages [12] -->
m

<!-- b001050 | prose | pages [12] -->
m

<!-- b001051 | prose | pages [12] -->
m

<!-- b001052 | prose | pages [12] -->
m

<!-- b001053 | prose | pages [12] -->
m

<!-- b001054 | prose | pages [12] -->
m

<!-- b001055 | prose | pages [12] -->
m

<!-- b001056 | prose | pages [12] -->
m

<!-- b001057 | prose | pages [12] -->
m

<!-- b001058 | prose | pages [12] -->
m

<!-- b001059 | prose | pages [12] -->
m

<!-- b001060 | prose | pages [12] -->
m

<!-- b001061 | prose | pages [12] -->
m

<!-- b001062 | prose | pages [12] -->
m

<!-- b001063 | prose | pages [12] -->
m

<!-- b001064 | prose | pages [12] -->
m

<!-- b001065 | prose | pages [12] -->
m

<!-- b001066 | prose | pages [12] -->
m

<!-- b001067 | prose | pages [12] -->
m

<!-- b001068 | prose | pages [12] -->
m

<!-- b001069 | prose | pages [12] -->
m

<!-- b001070 | prose | pages [12] -->
m

<!-- b001071 | prose | pages [12] -->
m

<!-- b001072 | prose | pages [12] -->
m

<!-- b001073 | prose | pages [12] -->
m

<!-- b001074 | prose | pages [12] -->
m

<!-- b001075 | prose | pages [12] -->
m

<!-- b001076 | prose | pages [12] -->
m

<!-- b001077 | prose | pages [12] -->
m

<!-- b001078 | prose | pages [12] -->
m

<!-- b001079 | prose | pages [12] -->
m

<!-- b001080 | prose | pages [12] -->
m

<!-- b001081 | prose | pages [12] -->
m

<!-- b001082 | prose | pages [12] -->
m

<!-- b001083 | prose | pages [12] -->
m

<!-- b001084 | prose | pages [12] -->
m

<!-- b001085 | prose | pages [12] -->
m

<!-- b001086 | prose | pages [12] -->
m

<!-- b001087 | prose | pages [12] -->
m

<!-- b001088 | prose | pages [12] -->
m

<!-- b001089 | prose | pages [12] -->
m

<!-- b001090 | prose | pages [12] -->
m

<!-- b001091 | prose | pages [12] -->
m

<!-- b001092 | prose | pages [12] -->
m

<!-- b001093 | prose | pages [12] -->
m

<!-- b001094 | prose | pages [12] -->
m

<!-- b001095 | prose | pages [12] -->
m

<!-- b001096 | prose | pages [12] -->
m

<!-- b001097 | prose | pages [12] -->
m

<!-- b001098 | prose | pages [12] -->
m

<!-- b001099 | prose | pages [12] -->
(note that we multiply by 3 as there are typically 3 medals to be obtained per event). This gave us two different

<!-- b001100 | prose | pages [12] -->
m

<!-- b001101 | prose | pages [12] -->
m

<!-- b001102 | prose | pages [12] -->
m

<!-- b001103 | prose | pages [12] -->
m

<!-- b001104 | prose | pages [12] -->
m

<!-- b001105 | prose | pages [12] -->
m

<!-- b001106 | prose | pages [12] -->
m

<!-- b001107 | prose | pages [12] -->
m

<!-- b001108 | prose | pages [12] -->
m

<!-- b001109 | prose | pages [12] -->
m

<!-- b001110 | prose | pages [12] -->
m

<!-- b001111 | prose | pages [12] -->
m

<!-- b001112 | prose | pages [12] -->
m

<!-- b001113 | prose | pages [12] -->
m

<!-- b001114 | prose | pages [12] -->
m

<!-- b001115 | prose | pages [12] -->
m

<!-- b001116 | prose | pages [12] -->
m

<!-- b001117 | prose | pages [12] -->
m

<!-- b001118 | prose | pages [12] -->
m

<!-- b001119 | prose | pages [12] -->
m

<!-- b001120 | prose | pages [12] -->
m

<!-- b001121 | prose | pages [12] -->
m

<!-- b001122 | prose | pages [12] -->
m

<!-- b001123 | prose | pages [12] -->
m

<!-- b001124 | prose | pages [12] -->
m

<!-- b001125 | prose | pages [12] -->
m

<!-- b001126 | prose | pages [12] -->
m

<!-- b001127 | prose | pages [12] -->
m

<!-- b001128 | prose | pages [12] -->
m

<!-- b001129 | prose | pages [12] -->
m

<!-- b001130 | prose | pages [12] -->
m

<!-- b001131 | prose | pages [12] -->
m

<!-- b001132 | prose | pages [12] -->
m

<!-- b001133 | prose | pages [12] -->
m

<!-- b001134 | prose | pages [12] -->
m

<!-- b001135 | prose | pages [12] -->
m

<!-- b001136 | prose | pages [12] -->
m

<!-- b001137 | prose | pages [12] -->
m

<!-- b001138 | prose | pages [12] -->
m

<!-- b001139 | prose | pages [12] -->
m

<!-- b001140 | prose | pages [12] -->
m

<!-- b001141 | prose | pages [12] -->
m

<!-- b001142 | prose | pages [12] -->
m

<!-- b001143 | prose | pages [12] -->
m

<!-- b001144 | prose | pages [12] -->
m

<!-- b001145 | prose | pages [12] -->
m

<!-- b001146 | prose | pages [12] -->
m

<!-- b001147 | prose | pages [12] -->
m

<!-- b001148 | prose | pages [12] -->
m

<!-- b001149 | prose | pages [12] -->
m

<!-- b001150 | prose | pages [12] -->
m

<!-- b001151 | prose | pages [12] -->
m

<!-- b001152 | prose | pages [12] -->
m

<!-- b001153 | prose | pages [12] -->
m

<!-- b001154 | prose | pages [12] -->
m

<!-- b001155 | prose | pages [12] -->
m

<!-- b001156 | prose | pages [12] -->
m

<!-- b001157 | prose | pages [12] -->
m

<!-- b001158 | prose | pages [12] -->
m

<!-- b001159 | prose | pages [12] -->
m

<!-- b001160 | prose | pages [12] -->
m

<!-- b001161 | prose | pages [12] -->
m

<!-- b001162 | prose | pages [12] -->
m

<!-- b001163 | prose | pages [12] -->
m

<!-- b001164 | prose | pages [12] -->
m

<!-- b001165 | prose | pages [12] -->
m

<!-- b001166 | prose | pages [12] -->
m

<!-- b001167 | prose | pages [12] -->
m

<!-- b001168 | prose | pages [12] -->
m

<!-- b001169 | prose | pages [12] -->
m

<!-- b001170 | prose | pages [12] -->
m

<!-- b001171 | prose | pages [12] -->
m

<!-- b001172 | prose | pages [12] -->
m

<!-- b001173 | prose | pages [12] -->
m

<!-- b001174 | prose | pages [12] -->
m

<!-- b001175 | prose | pages [12] -->
m

<!-- b001176 | prose | pages [12] -->
m

<!-- b001177 | prose | pages [12] -->
m

<!-- b001178 | prose | pages [12] -->
m

<!-- b001179 | prose | pages [12] -->
m

<!-- b001180 | prose | pages [12] -->
m

<!-- b001181 | prose | pages [12] -->
m

<!-- b001182 | prose | pages [12] -->
m

<!-- b001183 | prose | pages [12] -->
m

<!-- b001184 | prose | pages [12] -->
m

<!-- b001185 | prose | pages [12] -->
m

<!-- b001186 | prose | pages [12] -->
m

<!-- b001187 | prose | pages [12] -->
m

<!-- b001188 | prose | pages [12] -->
m

<!-- b001189 | prose | pages [12] -->
m

<!-- b001190 | prose | pages [12] -->
m

<!-- b001191 | prose | pages [12] -->
m

<!-- b001192 | prose | pages [12] -->
m

<!-- b001193 | prose | pages [12] -->
m

<!-- b001194 | prose | pages [12] -->
m

<!-- b001195 | prose | pages [12] -->
m

<!-- b001196 | prose | pages [12] -->
m

<!-- b001197 | prose | pages [12] -->
m

<!-- b001198 | prose | pages [12] -->
m

<!-- b001199 | prose | pages [12] -->
m

<!-- b001200 | prose | pages [12] -->
m

<!-- b001201 | prose | pages [12] -->
m

<!-- b001202 | prose | pages [12] -->
m

<!-- b001203 | prose | pages [12] -->
m

<!-- b001204 | prose | pages [12] -->
m

<!-- b001205 | prose | pages [12] -->
m

<!-- b001206 | prose | pages [12] -->
m

<!-- b001207 | prose | pages [12] -->
m

<!-- b001208 | prose | pages [12] -->
m

<!-- b001209 | prose | pages [12] -->
m

<!-- b001210 | prose | pages [12] -->
m

<!-- b001211 | prose | pages [12] -->
m

<!-- b001212 | prose | pages [12] -->
m

<!-- b001213 | prose | pages [12] -->
m

<!-- b001214 | prose | pages [12] -->
m

<!-- b001215 | prose | pages [12] -->
m

<!-- b001216 | prose | pages [12] -->
m

<!-- b001217 | prose | pages [12] -->
m

<!-- b001218 | prose | pages [12] -->
m

<!-- b001219 | prose | pages [12] -->
m

<!-- b001220 | prose | pages [12] -->
m

<!-- b001221 | prose | pages [12] -->
m

<!-- b001222 | prose | pages [12] -->
m

<!-- b001223 | prose | pages [12] -->
approximations for medal distribution in sports: the distribution solely from the amount of athletes from a

<!-- b001224 | prose | pages [12] -->
m

<!-- b001225 | prose | pages [12] -->
m

<!-- b001226 | prose | pages [12] -->
m

<!-- b001227 | prose | pages [12] -->
m

<!-- b001228 | prose | pages [12] -->
m

<!-- b001229 | prose | pages [12] -->
m

<!-- b001230 | prose | pages [12] -->
m

<!-- b001231 | prose | pages [12] -->
m

<!-- b001232 | prose | pages [12] -->
m

<!-- b001233 | prose | pages [12] -->
m

<!-- b001234 | prose | pages [12] -->
m

<!-- b001235 | prose | pages [12] -->
m

<!-- b001236 | prose | pages [12] -->
m

<!-- b001237 | prose | pages [12] -->
m

<!-- b001238 | prose | pages [12] -->
m

<!-- b001239 | prose | pages [12] -->
m

<!-- b001240 | prose | pages [12] -->
m

<!-- b001241 | prose | pages [12] -->
m

<!-- b001242 | prose | pages [12] -->
m

<!-- b001243 | prose | pages [12] -->
m

<!-- b001244 | prose | pages [12] -->
m

<!-- b001245 | prose | pages [12] -->
m

<!-- b001246 | prose | pages [12] -->
m

<!-- b001247 | prose | pages [12] -->
m

<!-- b001248 | prose | pages [12] -->
m

<!-- b001249 | prose | pages [12] -->
m

<!-- b001250 | prose | pages [12] -->
m

<!-- b001251 | prose | pages [12] -->
m

<!-- b001252 | prose | pages [12] -->
m

<!-- b001253 | prose | pages [12] -->
m

<!-- b001254 | prose | pages [12] -->
m

<!-- b001255 | prose | pages [12] -->
m

<!-- b001256 | prose | pages [12] -->
m

<!-- b001257 | prose | pages [12] -->
m

<!-- b001258 | prose | pages [12] -->
m

<!-- b001259 | prose | pages [12] -->
m

<!-- b001260 | prose | pages [12] -->
m

<!-- b001261 | prose | pages [12] -->
m

<!-- b001262 | prose | pages [12] -->
m

<!-- b001263 | prose | pages [12] -->
m

<!-- b001264 | prose | pages [12] -->
m

<!-- b001265 | prose | pages [12] -->
m

<!-- b001266 | prose | pages [12] -->
m

<!-- b001267 | prose | pages [12] -->
m

<!-- b001268 | prose | pages [12] -->
m

<!-- b001269 | prose | pages [12] -->
m

<!-- b001270 | prose | pages [12] -->
m

<!-- b001271 | prose | pages [12] -->
m

<!-- b001272 | prose | pages [12] -->
m

<!-- b001273 | prose | pages [12] -->
m

<!-- b001274 | prose | pages [12] -->
m

<!-- b001275 | prose | pages [12] -->
m

<!-- b001276 | prose | pages [12] -->
m

<!-- b001277 | prose | pages [12] -->
m

<!-- b001278 | prose | pages [12] -->
m

<!-- b001279 | prose | pages [12] -->
m

<!-- b001280 | prose | pages [12] -->
m

<!-- b001281 | prose | pages [12] -->
m

<!-- b001282 | prose | pages [12] -->
m

<!-- b001283 | prose | pages [12] -->
m

<!-- b001284 | prose | pages [12] -->
m

<!-- b001285 | prose | pages [12] -->
m

<!-- b001286 | prose | pages [12] -->
m

<!-- b001287 | prose | pages [12] -->
m

<!-- b001288 | prose | pages [12] -->
m

<!-- b001289 | prose | pages [12] -->
m

<!-- b001290 | prose | pages [12] -->
m

<!-- b001291 | prose | pages [12] -->
m

<!-- b001292 | prose | pages [12] -->
m

<!-- b001293 | prose | pages [12] -->
m

<!-- b001294 | prose | pages [12] -->
m

<!-- b001295 | prose | pages [12] -->
m

<!-- b001296 | prose | pages [12] -->
m

<!-- b001297 | prose | pages [12] -->
m

<!-- b001298 | prose | pages [12] -->
m

<!-- b001299 | prose | pages [12] -->
m

<!-- b001300 | prose | pages [12] -->
m

<!-- b001301 | prose | pages [12] -->
m

<!-- b001302 | prose | pages [12] -->
m

<!-- b001303 | prose | pages [12] -->
m

<!-- b001304 | prose | pages [12] -->
m

<!-- b001305 | prose | pages [12] -->
m

<!-- b001306 | prose | pages [12] -->
m

<!-- b001307 | prose | pages [12] -->
m

<!-- b001308 | prose | pages [12] -->
m

<!-- b001309 | prose | pages [12] -->
m

<!-- b001310 | prose | pages [12] -->
m

<!-- b001311 | prose | pages [12] -->
m

<!-- b001312 | prose | pages [12] -->
m

<!-- b001313 | prose | pages [12] -->
m

<!-- b001314 | prose | pages [12] -->
m

<!-- b001315 | prose | pages [12] -->
m

<!-- b001316 | prose | pages [12] -->
m

<!-- b001317 | prose | pages [12] -->
m

<!-- b001318 | prose | pages [12] -->
m

<!-- b001319 | prose | pages [12] -->
m

<!-- b001320 | prose | pages [12] -->
m

<!-- b001321 | prose | pages [12] -->
m

<!-- b001322 | prose | pages [12] -->
m

<!-- b001323 | prose | pages [12] -->
m

<!-- b001324 | prose | pages [12] -->
m

<!-- b001325 | prose | pages [12] -->
m

<!-- b001326 | prose | pages [12] -->
m

<!-- b001327 | prose | pages [12] -->
m

<!-- b001328 | prose | pages [12] -->
m

<!-- b001329 | prose | pages [12] -->
m

<!-- b001330 | prose | pages [12] -->
m

<!-- b001331 | prose | pages [12] -->
m

<!-- b001332 | prose | pages [12] -->
m

<!-- b001333 | prose | pages [12] -->
m

<!-- b001334 | prose | pages [12] -->
m

<!-- b001335 | prose | pages [12] -->
m

<!-- b001336 | prose | pages [12] -->
m

<!-- b001337 | prose | pages [12] -->
m

<!-- b001338 | prose | pages [12] -->
m

<!-- b001339 | prose | pages [12] -->
m

<!-- b001340 | prose | pages [12] -->
m

<!-- b001341 | prose | pages [12] -->
m

<!-- b001342 | prose | pages [12] -->
m

<!-- b001343 | prose | pages [12] -->
m

<!-- b001344 | prose | pages [12] -->
m

<!-- b001345 | prose | pages [12] -->
m

<!-- b001346 | prose | pages [12] -->
m

<!-- b001347 | prose | pages [12] -->
m

<!-- b001348 | prose | pages [12] -->
m

<!-- b001349 | prose | pages [12] -->
m

<!-- b001350 | prose | pages [12] -->
m

<!-- b001351 | prose | pages [12] -->
m

<!-- b001352 | prose | pages [12] -->
m

<!-- b001353 | prose | pages [12] -->
m

<!-- b001354 | prose | pages [12] -->
m

<!-- b001355 | prose | pages [12] -->
m

<!-- b001356 | prose | pages [12] -->
m

<!-- b001357 | prose | pages [12] -->
m

<!-- b001358 | prose | pages [12] -->
m

<!-- b001359 | prose | pages [12] -->
country that obtained a medal in a specific sport and the distribution based on the ceiling multiped by a related

<!-- b001360 | prose | pages [12] -->
m

<!-- b001361 | prose | pages [12] -->
m

<!-- b001362 | prose | pages [12] -->
m

<!-- b001363 | prose | pages [12] -->
m

<!-- b001364 | prose | pages [12] -->
m

<!-- b001365 | prose | pages [12] -->
m

<!-- b001366 | prose | pages [12] -->
m

<!-- b001367 | prose | pages [12] -->
m

<!-- b001368 | prose | pages [12] -->
m

<!-- b001369 | prose | pages [12] -->
m

<!-- b001370 | prose | pages [12] -->
m

<!-- b001371 | prose | pages [12] -->
m

<!-- b001372 | prose | pages [12] -->
m

<!-- b001373 | prose | pages [12] -->
m

<!-- b001374 | prose | pages [12] -->
m

<!-- b001375 | prose | pages [12] -->
m

<!-- b001376 | prose | pages [12] -->
m

<!-- b001377 | prose | pages [12] -->
m

<!-- b001378 | prose | pages [12] -->
m

<!-- b001379 | prose | pages [12] -->
m

<!-- b001380 | prose | pages [12] -->
m

<!-- b001381 | prose | pages [12] -->
m

<!-- b001382 | prose | pages [12] -->
m

<!-- b001383 | prose | pages [12] -->
m

<!-- b001384 | prose | pages [12] -->
m

<!-- b001385 | prose | pages [12] -->
m

<!-- b001386 | prose | pages [12] -->
m

<!-- b001387 | prose | pages [12] -->
m

<!-- b001388 | prose | pages [12] -->
m

<!-- b001389 | prose | pages [12] -->
m

<!-- b001390 | prose | pages [12] -->
m

<!-- b001391 | prose | pages [12] -->
m

<!-- b001392 | prose | pages [12] -->
m

<!-- b001393 | prose | pages [12] -->
m

<!-- b001394 | prose | pages [12] -->
m

<!-- b001395 | prose | pages [12] -->
m

<!-- b001396 | prose | pages [12] -->
m

<!-- b001397 | prose | pages [12] -->
m

<!-- b001398 | prose | pages [12] -->
m

<!-- b001399 | prose | pages [12] -->
m

<!-- b001400 | prose | pages [12] -->
m

<!-- b001401 | prose | pages [12] -->
m

<!-- b001402 | prose | pages [12] -->
m

<!-- b001403 | prose | pages [12] -->
m

<!-- b001404 | prose | pages [12] -->
m

<!-- b001405 | prose | pages [12] -->
m

<!-- b001406 | prose | pages [12] -->
m

<!-- b001407 | prose | pages [12] -->
m

<!-- b001408 | prose | pages [12] -->
m

<!-- b001409 | prose | pages [12] -->
m

<!-- b001410 | prose | pages [12] -->
m

<!-- b001411 | prose | pages [12] -->
m

<!-- b001412 | prose | pages [12] -->
m

<!-- b001413 | prose | pages [12] -->
m

<!-- b001414 | prose | pages [12] -->
m

<!-- b001415 | prose | pages [12] -->
m

<!-- b001416 | prose | pages [12] -->
m

<!-- b001417 | prose | pages [12] -->
m

<!-- b001418 | prose | pages [12] -->
m

<!-- b001419 | prose | pages [12] -->
m

<!-- b001420 | prose | pages [12] -->
m

<!-- b001421 | prose | pages [12] -->
m

<!-- b001422 | prose | pages [12] -->
m

<!-- b001423 | prose | pages [12] -->
m

<!-- b001424 | prose | pages [12] -->
m

<!-- b001425 | prose | pages [12] -->
m

<!-- b001426 | prose | pages [12] -->
m

<!-- b001427 | prose | pages [12] -->
m

<!-- b001428 | prose | pages [12] -->
m

<!-- b001429 | prose | pages [12] -->
m

<!-- b001430 | prose | pages [12] -->
m

<!-- b001431 | prose | pages [12] -->
m

<!-- b001432 | prose | pages [12] -->
m

<!-- b001433 | prose | pages [12] -->
m

<!-- b001434 | prose | pages [12] -->
m

<!-- b001435 | prose | pages [12] -->
m

<!-- b001436 | prose | pages [12] -->
m

<!-- b001437 | prose | pages [12] -->
m

<!-- b001438 | prose | pages [12] -->
m

<!-- b001439 | prose | pages [12] -->
m

<!-- b001440 | prose | pages [12] -->
m

<!-- b001441 | prose | pages [12] -->
m

<!-- b001442 | prose | pages [12] -->
m

<!-- b001443 | prose | pages [12] -->
m

<!-- b001444 | prose | pages [12] -->
m

<!-- b001445 | prose | pages [12] -->
m

<!-- b001446 | prose | pages [12] -->
m

<!-- b001447 | prose | pages [12] -->
m

<!-- b001448 | prose | pages [12] -->
m

<!-- b001449 | prose | pages [12] -->
m

<!-- b001450 | prose | pages [12] -->
m

<!-- b001451 | prose | pages [12] -->
m

<!-- b001452 | prose | pages [12] -->
m

<!-- b001453 | prose | pages [12] -->
m

<!-- b001454 | prose | pages [12] -->
m

<!-- b001455 | prose | pages [12] -->
m

<!-- b001456 | prose | pages [12] -->
m

<!-- b001457 | prose | pages [12] -->
m

<!-- b001458 | prose | pages [12] -->
m

<!-- b001459 | prose | pages [12] -->
m

<!-- b001460 | prose | pages [12] -->
m

<!-- b001461 | prose | pages [12] -->
m

<!-- b001462 | prose | pages [12] -->
m

<!-- b001463 | prose | pages [12] -->
m

<!-- b001464 | prose | pages [12] -->
m

<!-- b001465 | prose | pages [12] -->
m

<!-- b001466 | prose | pages [12] -->
m

<!-- b001467 | prose | pages [12] -->
m

<!-- b001468 | prose | pages [12] -->
m

<!-- b001469 | prose | pages [12] -->
m

<!-- b001470 | prose | pages [12] -->
m

<!-- b001471 | prose | pages [12] -->
m

<!-- b001472 | prose | pages [12] -->
m

<!-- b001473 | prose | pages [12] -->
m

<!-- b001474 | prose | pages [12] -->
m

<!-- b001475 | prose | pages [12] -->
m

<!-- b001476 | prose | pages [12] -->
m

<!-- b001477 | prose | pages [12] -->
m

<!-- b001478 | prose | pages [12] -->
m

<!-- b001479 | prose | pages [12] -->
m

<!-- b001480 | prose | pages [12] -->
m

<!-- b001481 | prose | pages [12] -->
proportion. To test the accuracy of the two different approximations, we isolated the sports in each year, then

<!-- b001482 | prose | pages [12] -->
m

<!-- b001483 | prose | pages [12] -->
m

<!-- b001484 | prose | pages [12] -->
m

<!-- b001485 | prose | pages [12] -->
m

<!-- b001486 | prose | pages [12] -->
m

<!-- b001487 | prose | pages [12] -->
m

<!-- b001488 | prose | pages [12] -->
m

<!-- b001489 | prose | pages [12] -->
m

<!-- b001490 | prose | pages [12] -->
m

<!-- b001491 | prose | pages [12] -->
m

<!-- b001492 | prose | pages [12] -->
m

<!-- b001493 | prose | pages [12] -->
m

<!-- b001494 | prose | pages [12] -->
m

<!-- b001495 | prose | pages [12] -->
m

<!-- b001496 | prose | pages [12] -->
m

<!-- b001497 | prose | pages [12] -->
m

<!-- b001498 | prose | pages [12] -->
m

<!-- b001499 | prose | pages [12] -->
m

<!-- b001500 | prose | pages [12] -->
m

<!-- b001501 | prose | pages [12] -->
m

<!-- b001502 | prose | pages [12] -->
m

<!-- b001503 | prose | pages [12] -->
m

<!-- b001504 | prose | pages [12] -->
m

<!-- b001505 | prose | pages [12] -->
m

<!-- b001506 | prose | pages [12] -->
m

<!-- b001507 | prose | pages [12] -->
m

<!-- b001508 | prose | pages [12] -->
m

<!-- b001509 | prose | pages [12] -->
m

<!-- b001510 | prose | pages [12] -->
m

<!-- b001511 | prose | pages [12] -->
m

<!-- b001512 | prose | pages [12] -->
m

<!-- b001513 | prose | pages [12] -->
m

<!-- b001514 | prose | pages [12] -->
m

<!-- b001515 | prose | pages [12] -->
m

<!-- b001516 | prose | pages [12] -->
m

<!-- b001517 | prose | pages [12] -->
m

<!-- b001518 | prose | pages [12] -->
m

<!-- b001519 | prose | pages [12] -->
m

<!-- b001520 | prose | pages [12] -->
m

<!-- b001521 | prose | pages [12] -->
m

<!-- b001522 | prose | pages [12] -->
m

<!-- b001523 | prose | pages [12] -->
m

<!-- b001524 | prose | pages [12] -->
m

<!-- b001525 | prose | pages [12] -->
m

<!-- b001526 | prose | pages [12] -->
m

<!-- b001527 | prose | pages [12] -->
m

<!-- b001528 | prose | pages [12] -->
m

<!-- b001529 | prose | pages [12] -->
m

<!-- b001530 | prose | pages [12] -->
m

<!-- b001531 | prose | pages [12] -->
m

<!-- b001532 | prose | pages [12] -->
m

<!-- b001533 | prose | pages [12] -->
m

<!-- b001534 | prose | pages [12] -->
m

<!-- b001535 | prose | pages [12] -->
m

<!-- b001536 | prose | pages [12] -->
m

<!-- b001537 | prose | pages [12] -->
m

<!-- b001538 | prose | pages [12] -->
m

<!-- b001539 | prose | pages [12] -->
m

<!-- b001540 | prose | pages [12] -->
m

<!-- b001541 | prose | pages [12] -->
m

<!-- b001542 | prose | pages [12] -->
m

<!-- b001543 | prose | pages [12] -->
m

<!-- b001544 | prose | pages [12] -->
m

<!-- b001545 | prose | pages [12] -->
m

<!-- b001546 | prose | pages [12] -->
m

<!-- b001547 | prose | pages [12] -->
m

<!-- b001548 | prose | pages [12] -->
m

<!-- b001549 | prose | pages [12] -->
m

<!-- b001550 | prose | pages [12] -->
m

<!-- b001551 | prose | pages [12] -->
m

<!-- b001552 | prose | pages [12] -->
m

<!-- b001553 | prose | pages [12] -->
m

<!-- b001554 | prose | pages [12] -->
m

<!-- b001555 | prose | pages [12] -->
m

<!-- b001556 | prose | pages [12] -->
m

<!-- b001557 | prose | pages [12] -->
m

<!-- b001558 | prose | pages [12] -->
m

<!-- b001559 | prose | pages [12] -->
m

<!-- b001560 | prose | pages [12] -->
m

<!-- b001561 | prose | pages [12] -->
m

<!-- b001562 | prose | pages [12] -->
m

<!-- b001563 | prose | pages [12] -->
m

<!-- b001564 | prose | pages [12] -->
m

<!-- b001565 | prose | pages [12] -->
m

<!-- b001566 | prose | pages [12] -->
m

<!-- b001567 | prose | pages [12] -->
m

<!-- b001568 | prose | pages [12] -->
m

<!-- b001569 | prose | pages [12] -->
m

<!-- b001570 | prose | pages [12] -->
m

<!-- b001571 | prose | pages [12] -->
m

<!-- b001572 | prose | pages [12] -->
m

<!-- b001573 | prose | pages [12] -->
m

<!-- b001574 | prose | pages [12] -->
m

<!-- b001575 | prose | pages [12] -->
m

<!-- b001576 | prose | pages [12] -->
m

<!-- b001577 | prose | pages [12] -->
m

<!-- b001578 | prose | pages [12] -->
m

<!-- b001579 | prose | pages [12] -->
m

<!-- b001580 | prose | pages [12] -->
m

<!-- b001581 | prose | pages [12] -->
m

<!-- b001582 | prose | pages [12] -->
m

<!-- b001583 | prose | pages [12] -->
m

<!-- b001584 | prose | pages [12] -->
m

<!-- b001585 | prose | pages [12] -->
m

<!-- b001586 | prose | pages [12] -->
m

<!-- b001587 | prose | pages [12] -->
m

<!-- b001588 | prose | pages [12] -->
m

<!-- b001589 | prose | pages [12] -->
m

<!-- b001590 | prose | pages [12] -->
m

<!-- b001591 | prose | pages [12] -->
m

<!-- b001592 | prose | pages [12] -->
m

<!-- b001593 | prose | pages [12] -->
m

<!-- b001594 | prose | pages [12] -->
m

<!-- b001595 | prose | pages [12] -->
m

<!-- b001596 | prose | pages [12] -->
m

<!-- b001597 | prose | pages [12] -->
m

<!-- b001598 | prose | pages [12] -->
m

<!-- b001599 | prose | pages [12] -->
m

<!-- b001600 | prose | pages [12] -->
m

<!-- b001601 | prose | pages [12] -->
m

<!-- b001602 | prose | pages [12] -->
m

<!-- b001603 | prose | pages [12] -->
summed the applied approximation of medal counts in every sport offered to get a total medal count. Then, we analyzed the accuracy of the total medal count approximations over time on the United States and the Netherlands. This can be seen in Figures 3a and 3b.

<!-- b001604 | prose | pages [12] -->
The figures demonstrated that the approximation of total medal counts using the ceiling-proportion approx- imation was much more accurate than just using the total medals obtained by all of a country’s athletes in a sport. We verified this by taking the average percent error of both approximations and comparing them. In the Netherlands, the ceiling-proportion approximation had a percent error of 20% while the athlete total approximation returned 198%. Similarly for the United States, our program returned 10% and 107% error respectively for the ceiling-proportion and athlete-total approximations.

<!-- b001605 | prose | pages [12] -->
By using the ceiling-proportion approximations for total medal count that were built on approximations for medal distribution in sports, we could get reasonable estimates for the medal counts in various sports and disciplines. However, there was one more issue before we could start analyzing the distribution of medals in sports. Not all medals are the same. This approximation gave us estimates for the total amount of medals, but not for the distribution among Gold, Silver, and Bronze. Luckily, we were able to apply a similar approximation as before:

<!-- b001606 | prose | pages [12] -->
Ceiling-Proportion Approximation = Country’s total athlete specific medal count in a sport

<!-- b001607 | prose | pages [12] -->
·Total Events per Sport Total athlete specific medal count in a sport

<!-- b001608 | prose | pages [12] -->
关注数学模型

<!-- b001609 | furniture | pages [12] -->
2

<!-- b001610 | furniture | pages [12] -->
MATHmodels

<!-- b001611 | furniture | pages [12] -->
获取更多资讯

<!-- b001612 | furniture | pages [13] -->
Team 2522820

<!-- b001613 | furniture | pages [13] -->
Page 13

<!-- b001614 | prose | pages [13] -->
微信公众号：数学模型

<!-- b001615 | prose | pages [13] -->
(a) Total medal approximations in Netherlands compared to actual medal counts

<!-- b001616 | prose | pages [13] -->
(b) Total medal approximations in United States compared to actual medal counts

<!-- b001617 | caption | pages [13] -->
Figure 3: Black Marks: The actual total medal counts, Blue Marks: ceiling-proportion approximation, Red

<!-- b001618 | prose | pages [13] -->
Marks: athlete total approximation .

<!-- b001619 | prose | pages [13] -->
微信号：MATHmodels

<!-- b001620 | prose | pages [13] -->
Notice that in this Ceiling-Proportion Approximation, we removed the scalar of 3. This scalar acted to account for all medal types earlier, but now that we are giving a specific medal, we no longer need to multiply by a factor of 3. Instead, we will apply this Ceiling-Proportion Approximation to each medal type. With three approximations for Gold, Silver, and Bronze, we can build a new approximation for the total medal count. This time giving us the distribution of medal types. We can see this in Figures 4a and 4b.

<!-- b001621 | prose | pages [13] -->
(a) Total medal approximations in Netherlands compared to actual medal counts

<!-- b001622 | prose | pages [13] -->
(b) Total medal approximations in United States compared to actual medal counts

<!-- b001623 | caption | pages [13] -->
Figure 4: Black line: Ceiling-Proportion Approximation from Figure 3, Brown Region: The Bronze medal

<!-- b001624 | prose | pages [13] -->
count estimate, Grey Region: Silver medal count estimate, Yellow Region: Gold medal count estimate

<!-- b001625 | prose | pages [13] -->
These approximations for total medal counts (with respect to our initial Ceiling-Proportion Approximations from Figure 1) were promising as there was only 2.8% and 1.1% average percent error respectively for the Netherlands and United States. However, it’s important to keep in mind that this approximation is still problematic as it creates the assumption that if the medal distributions sum to a reasonably accurate total medal count, then the medal distribution will also be accurate.

<!-- b001626 | furniture | pages [14] -->
Team 2522820

<!-- b001627 | furniture | pages [14] -->
Page 14

<!-- b001628 | heading | pages [14] -->
Data Processing (Event Limitation Approximation)

<!-- b001629 | prose | pages [14] -->
3.6.2

<!-- b001630 | prose | pages [14] -->
While the Ceiling-Proportion Approximation provided a fairly reasonable estimation of the medal distribution among sports/disciplines, we lacked a method of associating sports/disciplines to events. This inspired our Event Limitation Approximation approach. This approximation works as in almost all cases, an event only has

<!-- b001631 | heading | pages [14] -->
1 medalist in Gold, Silver, and Bronze. By creating a Python dictionary to store all isolated unique events

<!-- b001632 | prose | pages [14] -->
that a country obtained a medal in, the length of that dictionary would tell us how many Gold, Silver, or Bronze medals they received and its distribution among sports and events.

<!-- b001633 | prose | pages [14] -->
This method parses through all of the data within athletes.csv and collects every single entry that has a specified year. Then, we reduced the data to only give us the country code, sport, event, and medal type. A dictionary proved useful here to distinguish unique events. We required three separate dictionaries for each medal type as it was possible for a key of (country code, sport, event) to be associated to Bronze, Silver, or Gold (which is not allowed by Python dictionaries). By searching each dictionary for a unique country code (ie. USA for United States), we could create subsets per country that allow us to know how many Gold, Silver, and Bronze medals they got as well as in what events. This satisfied our need for associating medals to events. To test the accuracy of this approximation, we ran our code for the United States and Netherlands again. The results are shown in Figures 5a and 5b.

<!-- b001634 | prose | pages [14] -->
(a) Total medal approximations in Netherlands compared to actual medal counts

<!-- b001635 | prose | pages [14] -->
(b) Total medal approximations in United States compared to actual medal counts

<!-- b001636 | caption | pages [14] -->
Figure 5: Red: Actual values given by IOC, Blue: Our Event Limitation Approximation

<!-- b001637 | prose | pages [14] -->
This was very accurate with average percent errors of 2.4% and 1% for the Netherlands and United States respectively. Now, we want to compare our distribution of medal types with the IOC’s distribution. We can see this below in Figures 6a, 6b, and 6c.

<!-- b001638 | prose | pages [14] -->
(b) Silver Medal Distribution Compar-

<!-- b001639 | prose | pages [14] -->
(a) Gold Medal Distribution Compar-

<!-- b001640 | prose | pages [14] -->
(c) Bronze Medal Distribution Com-

<!-- b001641 | prose | pages [14] -->
ison in United States

<!-- b001642 | prose | pages [14] -->
ison in United States

<!-- b001643 | prose | pages [14] -->
parison in United States

<!-- b001644 | caption | pages [14] -->
Figure 6: Red: Actual values given by IOC, Blue: Our Event Limitation Approximation

<!-- b001645 | prose | pages [14] -->
关注数学模型

<!-- b001646 | furniture | pages [14] -->
2

<!-- b001647 | furniture | pages [14] -->
MATHmodels

<!-- b001648 | furniture | pages [14] -->
获取更多资讯

<!-- b001649 | furniture | pages [16] -->
Team 2522820

<!-- b001650 | prose | pages [16] -->
Rank Singular Value 1 3838.9080 2 2664.5821 3 2397.0722 4 2042.4828 5 1903.1633 6 1819.0644 7 1666.6152 8 1533.8462 9 1468.2113 10 1296.5435

<!-- b001651 | furniture | pages [16] -->
Page 16

<!-- b001652 | prose | pages [16] -->
Event Men’s Greco-Roman 97kg Men’s Greco-Roman 77kg Men’s Greco-Roman 67kg Men’s Freestyle 57kg Men’s Freestyle 65kg Women’s 20km Race Walk Marathon Race Walk Relay Mixed Women’s 100m Women’s 200m Men’s 100m

<!-- b001653 | caption | pages [16] -->
Table 6: Ranked Singular Values and Associated Events

<!-- b001654 | prose | pages [16] -->
Here, we are tasked with understanding what sports are most important to various countries. We deviate from 4.6.4 as we will now consider the previous ranking point system instead of total medals. Each gold medal is worth 6 points, each silver medal is worth 3 points, and each bronze medal is worth 2 points. By totaling up the points, we can weigh the effect of the medal distribution on the total medal count. To quantify the impact of sports, we will consider the following three factors:

<!-- b001655 | prose | pages [16] -->
1. Sport-Point Efficiency: A proportion between the points a country obtains in one sport and how many athletes from that same country competed in that sport.

<!-- b001656 | prose | pages [16] -->
2. Sport-Point Share: A proportion between how many points a country obtains in one sport and how many points a country obtains at one Olympic Game.

<!-- b001657 | prose | pages [16] -->
3. Revealed Comparative Advantage (RCA) Index: While the RCA Index is typically applied to reveal a country’s advantage in producing goods and services, we can extend this to the Games. The RCA Index here will tell us if a country has an advantage in a sport when compared with other countries’ data given by the IOC.

<!-- b001658 | prose | pages [16] -->
m

<!-- b001659 | prose | pages [16] -->
m

<!-- b001660 | prose | pages [16] -->
m

<!-- b001661 | prose | pages [16] -->
m

<!-- b001662 | prose | pages [16] -->
m

<!-- b001663 | prose | pages [16] -->
m

<!-- b001664 | prose | pages [16] -->
m

<!-- b001665 | prose | pages [16] -->
m

<!-- b001666 | prose | pages [16] -->
m

<!-- b001667 | prose | pages [16] -->
m

<!-- b001668 | prose | pages [16] -->
m

<!-- b001669 | prose | pages [16] -->
m

<!-- b001670 | prose | pages [16] -->
m

<!-- b001671 | prose | pages [16] -->
m

<!-- b001672 | prose | pages [16] -->
m

<!-- b001673 | prose | pages [16] -->
m

<!-- b001674 | prose | pages [16] -->
m

<!-- b001675 | prose | pages [16] -->
m

<!-- b001676 | prose | pages [16] -->
m

<!-- b001677 | prose | pages [16] -->
m

<!-- b001678 | prose | pages [16] -->
m

<!-- b001679 | prose | pages [16] -->
m

<!-- b001680 | prose | pages [16] -->
m

<!-- b001681 | prose | pages [16] -->
m

<!-- b001682 | prose | pages [16] -->
m

<!-- b001683 | prose | pages [16] -->
m

<!-- b001684 | prose | pages [16] -->
m

<!-- b001685 | prose | pages [16] -->
m

<!-- b001686 | prose | pages [16] -->
m

<!-- b001687 | prose | pages [16] -->
m

<!-- b001688 | prose | pages [16] -->
m

<!-- b001689 | prose | pages [16] -->
m

<!-- b001690 | prose | pages [16] -->
m

<!-- b001691 | prose | pages [16] -->
m

<!-- b001692 | prose | pages [16] -->
m

<!-- b001693 | prose | pages [16] -->
m

<!-- b001694 | prose | pages [16] -->
m

<!-- b001695 | prose | pages [16] -->
m

<!-- b001696 | prose | pages [16] -->
Variable Definition

<!-- b001697 | prose | pages [16] -->
m

<!-- b001698 | prose | pages [16] -->
m

<!-- b001699 | prose | pages [16] -->
m

<!-- b001700 | prose | pages [16] -->
m

<!-- b001701 | prose | pages [16] -->
m

<!-- b001702 | prose | pages [16] -->
m

<!-- b001703 | prose | pages [16] -->
m

<!-- b001704 | prose | pages [16] -->
m

<!-- b001705 | prose | pages [16] -->
m

<!-- b001706 | prose | pages [16] -->
m

<!-- b001707 | prose | pages [16] -->
m

<!-- b001708 | prose | pages [16] -->
m

<!-- b001709 | prose | pages [16] -->
m

<!-- b001710 | prose | pages [16] -->
m

<!-- b001711 | prose | pages [16] -->
m

<!-- b001712 | prose | pages [16] -->
m

<!-- b001713 | prose | pages [16] -->
m

<!-- b001714 | prose | pages [16] -->
m

<!-- b001715 | prose | pages [16] -->
m

<!-- b001716 | prose | pages [16] -->
m

<!-- b001717 | prose | pages [16] -->
m

<!-- b001718 | prose | pages [16] -->
m

<!-- b001719 | prose | pages [16] -->
m

<!-- b001720 | prose | pages [16] -->
m

<!-- b001721 | prose | pages [16] -->
m

<!-- b001722 | prose | pages [16] -->
m

<!-- b001723 | prose | pages [16] -->
m

<!-- b001724 | prose | pages [16] -->
m

<!-- b001725 | prose | pages [16] -->
m

<!-- b001726 | prose | pages [16] -->
m

<!-- b001727 | prose | pages [16] -->
m

<!-- b001728 | prose | pages [16] -->
m

<!-- b001729 | prose | pages [16] -->
m

<!-- b001730 | prose | pages [16] -->
m

<!-- b001731 | prose | pages [16] -->
m

<!-- b001732 | prose | pages [16] -->
m

<!-- b001733 | prose | pages [16] -->
m

<!-- b001734 | prose | pages [16] -->
m

<!-- b001735 | prose | pages [16] -->
m

<!-- b001736 | prose | pages [16] -->
m

<!-- b001737 | prose | pages [16] -->
m

<!-- b001738 | prose | pages [16] -->
m

<!-- b001739 | prose | pages [16] -->
m

<!-- b001740 | prose | pages [16] -->
m

<!-- b001741 | prose | pages [16] -->
m

<!-- b001742 | prose | pages [16] -->
m

<!-- b001743 | prose | pages [16] -->
m

<!-- b001744 | prose | pages [16] -->
m

<!-- b001745 | prose | pages [16] -->
m

<!-- b001746 | prose | pages [16] -->
m

<!-- b001747 | prose | pages [16] -->
m

<!-- b001748 | prose | pages [16] -->
m

<!-- b001749 | prose | pages [16] -->
m

<!-- b001750 | prose | pages [16] -->
m

<!-- b001751 | prose | pages [16] -->
m

<!-- b001752 | prose | pages [16] -->
m

<!-- b001753 | prose | pages [16] -->
m

<!-- b001754 | prose | pages [16] -->
m

<!-- b001755 | prose | pages [16] -->
m

<!-- b001756 | prose | pages [16] -->
m

<!-- b001757 | prose | pages [16] -->
m

<!-- b001758 | prose | pages [16] -->
m

<!-- b001759 | prose | pages [16] -->
m

<!-- b001760 | prose | pages [16] -->
m

<!-- b001761 | prose | pages [16] -->
m

<!-- b001762 | prose | pages [16] -->
m

<!-- b001763 | prose | pages [16] -->
m

<!-- b001764 | prose | pages [16] -->
m

<!-- b001765 | prose | pages [16] -->
m

<!-- b001766 | prose | pages [16] -->
m

<!-- b001767 | prose | pages [16] -->
m

<!-- b001768 | prose | pages [16] -->
m

<!-- b001769 | prose | pages [16] -->
m

<!-- b001770 | prose | pages [16] -->
m

<!-- b001771 | prose | pages [16] -->
m

<!-- b001772 | prose | pages [16] -->
m

<!-- b001773 | prose | pages [16] -->
m

<!-- b001774 | prose | pages [16] -->
m

<!-- b001775 | prose | pages [16] -->
m

<!-- b001776 | prose | pages [16] -->
m

<!-- b001777 | prose | pages [16] -->
m

<!-- b001778 | prose | pages [16] -->
m

<!-- b001779 | prose | pages [16] -->
m

<!-- b001780 | prose | pages [16] -->
m

<!-- b001781 | prose | pages [16] -->
m

<!-- b001782 | prose | pages [16] -->
m

<!-- b001783 | prose | pages [16] -->
m

<!-- b001784 | prose | pages [16] -->
m

<!-- b001785 | prose | pages [16] -->
m

<!-- b001786 | prose | pages [16] -->
m

<!-- b001787 | prose | pages [16] -->
m

<!-- b001788 | prose | pages [16] -->
m

<!-- b001789 | prose | pages [16] -->
m

<!-- b001790 | prose | pages [16] -->
m

<!-- b001791 | prose | pages [16] -->
m

<!-- b001792 | prose | pages [16] -->
m

<!-- b001793 | prose | pages [16] -->
m

<!-- b001794 | prose | pages [16] -->
m

<!-- b001795 | prose | pages [16] -->
m

<!-- b001796 | prose | pages [16] -->
m

<!-- b001797 | prose | pages [16] -->
m

<!-- b001798 | prose | pages [16] -->
m

<!-- b001799 | prose | pages [16] -->
m

<!-- b001800 | prose | pages [16] -->
m

<!-- b001801 | prose | pages [16] -->
m

<!-- b001802 | prose | pages [16] -->
m

<!-- b001803 | prose | pages [16] -->
m

<!-- b001804 | prose | pages [16] -->
m

<!-- b001805 | prose | pages [16] -->
m

<!-- b001806 | prose | pages [16] -->
m

<!-- b001807 | prose | pages [16] -->
m

<!-- b001808 | prose | pages [16] -->
m

<!-- b001809 | prose | pages [16] -->
m

<!-- b001810 | prose | pages [16] -->
m

<!-- b001811 | prose | pages [16] -->
m

<!-- b001812 | prose | pages [16] -->
m

<!-- b001813 | prose | pages [16] -->
m

<!-- b001814 | prose | pages [16] -->
m

<!-- b001815 | prose | pages [16] -->
m

<!-- b001816 | prose | pages [16] -->
m

<!-- b001817 | prose | pages [16] -->
m

<!-- b001818 | prose | pages [16] -->
m

<!-- b001819 | prose | pages [16] -->
m

<!-- b001820 | prose | pages [16] -->
m

<!-- b001821 | prose | pages [16] -->
m

<!-- b001822 | prose | pages [16] -->
m

<!-- b001823 | prose | pages [16] -->
m

<!-- b001824 | prose | pages [16] -->
m

<!-- b001825 | prose | pages [16] -->
m

<!-- b001826 | prose | pages [16] -->
Unit Number of points won by country c in sport s. Pcs

<!-- b001827 | prose | pages [16] -->
m

<!-- b001828 | prose | pages [16] -->
m

<!-- b001829 | prose | pages [16] -->
m

<!-- b001830 | prose | pages [16] -->
m

<!-- b001831 | prose | pages [16] -->
m

<!-- b001832 | prose | pages [16] -->
m

<!-- b001833 | prose | pages [16] -->
m

<!-- b001834 | prose | pages [16] -->
m

<!-- b001835 | prose | pages [16] -->
m

<!-- b001836 | prose | pages [16] -->
m

<!-- b001837 | prose | pages [16] -->
m

<!-- b001838 | prose | pages [16] -->
m

<!-- b001839 | prose | pages [16] -->
m

<!-- b001840 | prose | pages [16] -->
m

<!-- b001841 | prose | pages [16] -->
m

<!-- b001842 | prose | pages [16] -->
m

<!-- b001843 | prose | pages [16] -->
m

<!-- b001844 | prose | pages [16] -->
m

<!-- b001845 | prose | pages [16] -->
m

<!-- b001846 | prose | pages [16] -->
m

<!-- b001847 | prose | pages [16] -->
m

<!-- b001848 | prose | pages [16] -->
m

<!-- b001849 | prose | pages [16] -->
m

<!-- b001850 | prose | pages [16] -->
m

<!-- b001851 | prose | pages [16] -->
m

<!-- b001852 | prose | pages [16] -->
m

<!-- b001853 | prose | pages [16] -->
m

<!-- b001854 | prose | pages [16] -->
m

<!-- b001855 | prose | pages [16] -->
m

<!-- b001856 | prose | pages [16] -->
m

<!-- b001857 | prose | pages [16] -->
m

<!-- b001858 | prose | pages [16] -->
m

<!-- b001859 | prose | pages [16] -->
m

<!-- b001860 | prose | pages [16] -->
m

<!-- b001861 | prose | pages [16] -->
m

<!-- b001862 | prose | pages [16] -->
m

<!-- b001863 | prose | pages [16] -->
m

<!-- b001864 | prose | pages [16] -->
m

<!-- b001865 | prose | pages [16] -->
m

<!-- b001866 | prose | pages [16] -->
m

<!-- b001867 | prose | pages [16] -->
m

<!-- b001868 | prose | pages [16] -->
m

<!-- b001869 | prose | pages [16] -->
m

<!-- b001870 | prose | pages [16] -->
m

<!-- b001871 | prose | pages [16] -->
m

<!-- b001872 | prose | pages [16] -->
m

<!-- b001873 | prose | pages [16] -->
m

<!-- b001874 | prose | pages [16] -->
m

<!-- b001875 | prose | pages [16] -->
m

<!-- b001876 | prose | pages [16] -->
m

<!-- b001877 | prose | pages [16] -->
m

<!-- b001878 | prose | pages [16] -->
m

<!-- b001879 | prose | pages [16] -->
m

<!-- b001880 | prose | pages [16] -->
m

<!-- b001881 | prose | pages [16] -->
m

<!-- b001882 | prose | pages [16] -->
m

<!-- b001883 | prose | pages [16] -->
m

<!-- b001884 | prose | pages [16] -->
m

<!-- b001885 | prose | pages [16] -->
m

<!-- b001886 | prose | pages [16] -->
m

<!-- b001887 | prose | pages [16] -->
m

<!-- b001888 | prose | pages [16] -->
m

<!-- b001889 | prose | pages [16] -->
m

<!-- b001890 | prose | pages [16] -->
m

<!-- b001891 | prose | pages [16] -->
m

<!-- b001892 | prose | pages [16] -->
m

<!-- b001893 | prose | pages [16] -->
m

<!-- b001894 | prose | pages [16] -->
m

<!-- b001895 | prose | pages [16] -->
m

<!-- b001896 | prose | pages [16] -->
m

<!-- b001897 | prose | pages [16] -->
m

<!-- b001898 | prose | pages [16] -->
m

<!-- b001899 | prose | pages [16] -->
m

<!-- b001900 | prose | pages [16] -->
m

<!-- b001901 | prose | pages [16] -->
m

<!-- b001902 | prose | pages [16] -->
m

<!-- b001903 | prose | pages [16] -->
m

<!-- b001904 | prose | pages [16] -->
m

<!-- b001905 | prose | pages [16] -->
m

<!-- b001906 | prose | pages [16] -->
m

<!-- b001907 | prose | pages [16] -->
m

<!-- b001908 | prose | pages [16] -->
m

<!-- b001909 | prose | pages [16] -->
m

<!-- b001910 | prose | pages [16] -->
m

<!-- b001911 | prose | pages [16] -->
m

<!-- b001912 | prose | pages [16] -->
m

<!-- b001913 | prose | pages [16] -->
m

<!-- b001914 | prose | pages [16] -->
m

<!-- b001915 | prose | pages [16] -->
m

<!-- b001916 | prose | pages [16] -->
m

<!-- b001917 | prose | pages [16] -->
m

<!-- b001918 | prose | pages [16] -->
m

<!-- b001919 | prose | pages [16] -->
m

<!-- b001920 | prose | pages [16] -->
m

<!-- b001921 | prose | pages [16] -->
m

<!-- b001922 | prose | pages [16] -->
m

<!-- b001923 | prose | pages [16] -->
m

<!-- b001924 | prose | pages [16] -->
m

<!-- b001925 | prose | pages [16] -->
m

<!-- b001926 | prose | pages [16] -->
m

<!-- b001927 | prose | pages [16] -->
m

<!-- b001928 | prose | pages [16] -->
m

<!-- b001929 | prose | pages [16] -->
m

<!-- b001930 | prose | pages [16] -->
m

<!-- b001931 | prose | pages [16] -->
m

<!-- b001932 | prose | pages [16] -->
m

<!-- b001933 | prose | pages [16] -->
m

<!-- b001934 | prose | pages [16] -->
m

<!-- b001935 | prose | pages [16] -->
m

<!-- b001936 | prose | pages [16] -->
m

<!-- b001937 | prose | pages [16] -->
m

<!-- b001938 | prose | pages [16] -->
m

<!-- b001939 | prose | pages [16] -->
m

<!-- b001940 | prose | pages [16] -->
m

<!-- b001941 | prose | pages [16] -->
m

<!-- b001942 | prose | pages [16] -->
m

<!-- b001943 | prose | pages [16] -->
m

<!-- b001944 | prose | pages [16] -->
m

<!-- b001945 | prose | pages [16] -->
m

<!-- b001946 | prose | pages [16] -->
m

<!-- b001947 | prose | pages [16] -->
m

<!-- b001948 | prose | pages [16] -->
m

<!-- b001949 | prose | pages [16] -->
m

<!-- b001950 | prose | pages [16] -->
m

<!-- b001951 | prose | pages [16] -->
m

<!-- b001952 | prose | pages [16] -->
m

<!-- b001953 | prose | pages [16] -->
m

<!-- b001954 | prose | pages [16] -->
m

<!-- b001955 | prose | pages [16] -->
m

<!-- b001956 | prose | pages [16] -->
m

<!-- b001957 | prose | pages [16] -->
m

<!-- b001958 | prose | pages [16] -->
m

<!-- b001959 | prose | pages [16] -->
m

<!-- b001960 | prose | pages [16] -->
m

<!-- b001961 | prose | pages [16] -->
m

<!-- b001962 | prose | pages [16] -->
m

<!-- b001963 | prose | pages [16] -->
m

<!-- b001964 | prose | pages [16] -->
m

<!-- b001965 | prose | pages [16] -->
m

<!-- b001966 | prose | pages [16] -->
m

<!-- b001967 | prose | pages [16] -->
m

<!-- b001968 | prose | pages [16] -->
m

<!-- b001969 | prose | pages [16] -->
m

<!-- b001970 | prose | pages [16] -->
Count Number of athletes by country c in sport s. Acs

<!-- b001971 | prose | pages [16] -->
m

<!-- b001972 | prose | pages [16] -->
m

<!-- b001973 | prose | pages [16] -->
m

<!-- b001974 | prose | pages [16] -->
m

<!-- b001975 | prose | pages [16] -->
m

<!-- b001976 | prose | pages [16] -->
m

<!-- b001977 | prose | pages [16] -->
m

<!-- b001978 | prose | pages [16] -->
m

<!-- b001979 | prose | pages [16] -->
m

<!-- b001980 | prose | pages [16] -->
m

<!-- b001981 | prose | pages [16] -->
m

<!-- b001982 | prose | pages [16] -->
m

<!-- b001983 | prose | pages [16] -->
m

<!-- b001984 | prose | pages [16] -->
m

<!-- b001985 | prose | pages [16] -->
m

<!-- b001986 | prose | pages [16] -->
m

<!-- b001987 | prose | pages [16] -->
m

<!-- b001988 | prose | pages [16] -->
m

<!-- b001989 | prose | pages [16] -->
m

<!-- b001990 | prose | pages [16] -->
m

<!-- b001991 | prose | pages [16] -->
m

<!-- b001992 | prose | pages [16] -->
m

<!-- b001993 | prose | pages [16] -->
m

<!-- b001994 | prose | pages [16] -->
m

<!-- b001995 | prose | pages [16] -->
m

<!-- b001996 | prose | pages [16] -->
m

<!-- b001997 | prose | pages [16] -->
m

<!-- b001998 | prose | pages [16] -->
m

<!-- b001999 | prose | pages [16] -->
m

<!-- b002000 | prose | pages [16] -->
m

<!-- b002001 | prose | pages [16] -->
m

<!-- b002002 | prose | pages [16] -->
m

<!-- b002003 | prose | pages [16] -->
m

<!-- b002004 | prose | pages [16] -->
m

<!-- b002005 | prose | pages [16] -->
m

<!-- b002006 | prose | pages [16] -->
m

<!-- b002007 | prose | pages [16] -->
m

<!-- b002008 | prose | pages [16] -->
m

<!-- b002009 | prose | pages [16] -->
m

<!-- b002010 | prose | pages [16] -->
m

<!-- b002011 | prose | pages [16] -->
m

<!-- b002012 | prose | pages [16] -->
m

<!-- b002013 | prose | pages [16] -->
m

<!-- b002014 | prose | pages [16] -->
m

<!-- b002015 | prose | pages [16] -->
m

<!-- b002016 | prose | pages [16] -->
m

<!-- b002017 | prose | pages [16] -->
m

<!-- b002018 | prose | pages [16] -->
m

<!-- b002019 | prose | pages [16] -->
m

<!-- b002020 | prose | pages [16] -->
m

<!-- b002021 | prose | pages [16] -->
m

<!-- b002022 | prose | pages [16] -->
m

<!-- b002023 | prose | pages [16] -->
m

<!-- b002024 | prose | pages [16] -->
m

<!-- b002025 | prose | pages [16] -->
m

<!-- b002026 | prose | pages [16] -->
m

<!-- b002027 | prose | pages [16] -->
m

<!-- b002028 | prose | pages [16] -->
m

<!-- b002029 | prose | pages [16] -->
m

<!-- b002030 | prose | pages [16] -->
m

<!-- b002031 | prose | pages [16] -->
m

<!-- b002032 | prose | pages [16] -->
m

<!-- b002033 | prose | pages [16] -->
m

<!-- b002034 | prose | pages [16] -->
m

<!-- b002035 | prose | pages [16] -->
m

<!-- b002036 | prose | pages [16] -->
m

<!-- b002037 | prose | pages [16] -->
m

<!-- b002038 | prose | pages [16] -->
m

<!-- b002039 | prose | pages [16] -->
m

<!-- b002040 | prose | pages [16] -->
m

<!-- b002041 | prose | pages [16] -->
m

<!-- b002042 | prose | pages [16] -->
m

<!-- b002043 | prose | pages [16] -->
m

<!-- b002044 | prose | pages [16] -->
m

<!-- b002045 | prose | pages [16] -->
m

<!-- b002046 | prose | pages [16] -->
m

<!-- b002047 | prose | pages [16] -->
m

<!-- b002048 | prose | pages [16] -->
m

<!-- b002049 | prose | pages [16] -->
m

<!-- b002050 | prose | pages [16] -->
m

<!-- b002051 | prose | pages [16] -->
m

<!-- b002052 | prose | pages [16] -->
m

<!-- b002053 | prose | pages [16] -->
m

<!-- b002054 | prose | pages [16] -->
m

<!-- b002055 | prose | pages [16] -->
m

<!-- b002056 | prose | pages [16] -->
m

<!-- b002057 | prose | pages [16] -->
m

<!-- b002058 | prose | pages [16] -->
m

<!-- b002059 | prose | pages [16] -->
m

<!-- b002060 | prose | pages [16] -->
m

<!-- b002061 | prose | pages [16] -->
m

<!-- b002062 | prose | pages [16] -->
m

<!-- b002063 | prose | pages [16] -->
m

<!-- b002064 | prose | pages [16] -->
m

<!-- b002065 | prose | pages [16] -->
m

<!-- b002066 | prose | pages [16] -->
m

<!-- b002067 | prose | pages [16] -->
m

<!-- b002068 | prose | pages [16] -->
m

<!-- b002069 | prose | pages [16] -->
m

<!-- b002070 | prose | pages [16] -->
m

<!-- b002071 | prose | pages [16] -->
m

<!-- b002072 | prose | pages [16] -->
m

<!-- b002073 | prose | pages [16] -->
m

<!-- b002074 | prose | pages [16] -->
m

<!-- b002075 | prose | pages [16] -->
m

<!-- b002076 | prose | pages [16] -->
m

<!-- b002077 | prose | pages [16] -->
m

<!-- b002078 | prose | pages [16] -->
m

<!-- b002079 | prose | pages [16] -->
m

<!-- b002080 | prose | pages [16] -->
m

<!-- b002081 | prose | pages [16] -->
m

<!-- b002082 | prose | pages [16] -->
m

<!-- b002083 | prose | pages [16] -->
m

<!-- b002084 | prose | pages [16] -->
m

<!-- b002085 | prose | pages [16] -->
m

<!-- b002086 | prose | pages [16] -->
m

<!-- b002087 | prose | pages [16] -->
m

<!-- b002088 | prose | pages [16] -->
m

<!-- b002089 | prose | pages [16] -->
m

<!-- b002090 | prose | pages [16] -->
m

<!-- b002091 | prose | pages [16] -->
m

<!-- b002092 | prose | pages [16] -->
m

<!-- b002093 | prose | pages [16] -->
m

<!-- b002094 | prose | pages [16] -->
m

<!-- b002095 | prose | pages [16] -->
m

<!-- b002096 | prose | pages [16] -->
m

<!-- b002097 | prose | pages [16] -->
m

<!-- b002098 | prose | pages [16] -->
m

<!-- b002099 | prose | pages [16] -->
m

<!-- b002100 | prose | pages [16] -->
m

<!-- b002101 | prose | pages [16] -->
m

<!-- b002102 | prose | pages [16] -->
m

<!-- b002103 | prose | pages [16] -->
m

<!-- b002104 | prose | pages [16] -->
m

<!-- b002105 | prose | pages [16] -->
m

<!-- b002106 | prose | pages [16] -->
P Count

<!-- b002107 | prose | pages [16] -->
Total points won in the Games by country c. s Pcs

<!-- b002108 | prose | pages [16] -->
m

<!-- b002109 | prose | pages [16] -->
m

<!-- b002110 | prose | pages [16] -->
m

<!-- b002111 | prose | pages [16] -->
m

<!-- b002112 | prose | pages [16] -->
m

<!-- b002113 | prose | pages [16] -->
m

<!-- b002114 | prose | pages [16] -->
m

<!-- b002115 | prose | pages [16] -->
m

<!-- b002116 | prose | pages [16] -->
m

<!-- b002117 | prose | pages [16] -->
m

<!-- b002118 | prose | pages [16] -->
m

<!-- b002119 | prose | pages [16] -->
m

<!-- b002120 | prose | pages [16] -->
m

<!-- b002121 | prose | pages [16] -->
m

<!-- b002122 | prose | pages [16] -->
m

<!-- b002123 | prose | pages [16] -->
m

<!-- b002124 | prose | pages [16] -->
m

<!-- b002125 | prose | pages [16] -->
m

<!-- b002126 | prose | pages [16] -->
m

<!-- b002127 | prose | pages [16] -->
m

<!-- b002128 | prose | pages [16] -->
m

<!-- b002129 | prose | pages [16] -->
m

<!-- b002130 | prose | pages [16] -->
m

<!-- b002131 | prose | pages [16] -->
m

<!-- b002132 | prose | pages [16] -->
m

<!-- b002133 | prose | pages [16] -->
m

<!-- b002134 | prose | pages [16] -->
m

<!-- b002135 | prose | pages [16] -->
m

<!-- b002136 | prose | pages [16] -->
m

<!-- b002137 | prose | pages [16] -->
m

<!-- b002138 | prose | pages [16] -->
m

<!-- b002139 | prose | pages [16] -->
m

<!-- b002140 | prose | pages [16] -->
m

<!-- b002141 | prose | pages [16] -->
m

<!-- b002142 | prose | pages [16] -->
m

<!-- b002143 | prose | pages [16] -->
m

<!-- b002144 | prose | pages [16] -->
m

<!-- b002145 | prose | pages [16] -->
m

<!-- b002146 | prose | pages [16] -->
m

<!-- b002147 | prose | pages [16] -->
m

<!-- b002148 | prose | pages [16] -->
m

<!-- b002149 | prose | pages [16] -->
m

<!-- b002150 | prose | pages [16] -->
m

<!-- b002151 | prose | pages [16] -->
m

<!-- b002152 | prose | pages [16] -->
m

<!-- b002153 | prose | pages [16] -->
m

<!-- b002154 | prose | pages [16] -->
m

<!-- b002155 | prose | pages [16] -->
m

<!-- b002156 | prose | pages [16] -->
m

<!-- b002157 | prose | pages [16] -->
m

<!-- b002158 | prose | pages [16] -->
m

<!-- b002159 | prose | pages [16] -->
m

<!-- b002160 | prose | pages [16] -->
m

<!-- b002161 | prose | pages [16] -->
m

<!-- b002162 | prose | pages [16] -->
m

<!-- b002163 | prose | pages [16] -->
m

<!-- b002164 | prose | pages [16] -->
m

<!-- b002165 | prose | pages [16] -->
m

<!-- b002166 | prose | pages [16] -->
m

<!-- b002167 | prose | pages [16] -->
m

<!-- b002168 | prose | pages [16] -->
m

<!-- b002169 | prose | pages [16] -->
m

<!-- b002170 | prose | pages [16] -->
m

<!-- b002171 | prose | pages [16] -->
m

<!-- b002172 | prose | pages [16] -->
m

<!-- b002173 | prose | pages [16] -->
m

<!-- b002174 | prose | pages [16] -->
m

<!-- b002175 | prose | pages [16] -->
m

<!-- b002176 | prose | pages [16] -->
m

<!-- b002177 | prose | pages [16] -->
m

<!-- b002178 | prose | pages [16] -->
m

<!-- b002179 | prose | pages [16] -->
m

<!-- b002180 | prose | pages [16] -->
m

<!-- b002181 | prose | pages [16] -->
m

<!-- b002182 | prose | pages [16] -->
m

<!-- b002183 | prose | pages [16] -->
m

<!-- b002184 | prose | pages [16] -->
m

<!-- b002185 | prose | pages [16] -->
m

<!-- b002186 | prose | pages [16] -->
m

<!-- b002187 | prose | pages [16] -->
m

<!-- b002188 | prose | pages [16] -->
m

<!-- b002189 | prose | pages [16] -->
m

<!-- b002190 | prose | pages [16] -->
m

<!-- b002191 | prose | pages [16] -->
m

<!-- b002192 | prose | pages [16] -->
m

<!-- b002193 | prose | pages [16] -->
m

<!-- b002194 | prose | pages [16] -->
m

<!-- b002195 | prose | pages [16] -->
m

<!-- b002196 | prose | pages [16] -->
m

<!-- b002197 | prose | pages [16] -->
m

<!-- b002198 | prose | pages [16] -->
m

<!-- b002199 | prose | pages [16] -->
m

<!-- b002200 | prose | pages [16] -->
m

<!-- b002201 | prose | pages [16] -->
m

<!-- b002202 | prose | pages [16] -->
m

<!-- b002203 | prose | pages [16] -->
m

<!-- b002204 | prose | pages [16] -->
m

<!-- b002205 | prose | pages [16] -->
m

<!-- b002206 | prose | pages [16] -->
m

<!-- b002207 | prose | pages [16] -->
m

<!-- b002208 | prose | pages [16] -->
m

<!-- b002209 | prose | pages [16] -->
m

<!-- b002210 | prose | pages [16] -->
m

<!-- b002211 | prose | pages [16] -->
m

<!-- b002212 | prose | pages [16] -->
m

<!-- b002213 | prose | pages [16] -->
m

<!-- b002214 | prose | pages [16] -->
m

<!-- b002215 | prose | pages [16] -->
m

<!-- b002216 | prose | pages [16] -->
m

<!-- b002217 | prose | pages [16] -->
m

<!-- b002218 | prose | pages [16] -->
m

<!-- b002219 | prose | pages [16] -->
m

<!-- b002220 | prose | pages [16] -->
m

<!-- b002221 | prose | pages [16] -->
m

<!-- b002222 | prose | pages [16] -->
m

<!-- b002223 | prose | pages [16] -->
m

<!-- b002224 | prose | pages [16] -->
m

<!-- b002225 | prose | pages [16] -->
m

<!-- b002226 | prose | pages [16] -->
m

<!-- b002227 | prose | pages [16] -->
m

<!-- b002228 | prose | pages [16] -->
m

<!-- b002229 | prose | pages [16] -->
P Count

<!-- b002230 | prose | pages [16] -->
Total points won in the Games in sport s. c Pcs

<!-- b002231 | prose | pages [16] -->
m

<!-- b002232 | prose | pages [16] -->
m

<!-- b002233 | prose | pages [16] -->
m

<!-- b002234 | prose | pages [16] -->
m

<!-- b002235 | prose | pages [16] -->
m

<!-- b002236 | prose | pages [16] -->
m

<!-- b002237 | prose | pages [16] -->
m

<!-- b002238 | prose | pages [16] -->
m

<!-- b002239 | prose | pages [16] -->
m

<!-- b002240 | prose | pages [16] -->
m

<!-- b002241 | prose | pages [16] -->
m

<!-- b002242 | prose | pages [16] -->
m

<!-- b002243 | prose | pages [16] -->
m

<!-- b002244 | prose | pages [16] -->
m

<!-- b002245 | prose | pages [16] -->
m

<!-- b002246 | prose | pages [16] -->
m

<!-- b002247 | prose | pages [16] -->
m

<!-- b002248 | prose | pages [16] -->
m

<!-- b002249 | prose | pages [16] -->
m

<!-- b002250 | prose | pages [16] -->
m

<!-- b002251 | prose | pages [16] -->
m

<!-- b002252 | prose | pages [16] -->
m

<!-- b002253 | prose | pages [16] -->
m

<!-- b002254 | prose | pages [16] -->
m

<!-- b002255 | prose | pages [16] -->
m

<!-- b002256 | prose | pages [16] -->
m

<!-- b002257 | prose | pages [16] -->
m

<!-- b002258 | prose | pages [16] -->
m

<!-- b002259 | prose | pages [16] -->
m

<!-- b002260 | prose | pages [16] -->
m

<!-- b002261 | prose | pages [16] -->
m

<!-- b002262 | prose | pages [16] -->
m

<!-- b002263 | prose | pages [16] -->
m

<!-- b002264 | prose | pages [16] -->
m

<!-- b002265 | prose | pages [16] -->
m

<!-- b002266 | prose | pages [16] -->
m

<!-- b002267 | prose | pages [16] -->
m

<!-- b002268 | prose | pages [16] -->
m

<!-- b002269 | prose | pages [16] -->
m

<!-- b002270 | prose | pages [16] -->
m

<!-- b002271 | prose | pages [16] -->
m

<!-- b002272 | prose | pages [16] -->
m

<!-- b002273 | prose | pages [16] -->
m

<!-- b002274 | prose | pages [16] -->
m

<!-- b002275 | prose | pages [16] -->
m

<!-- b002276 | prose | pages [16] -->
m

<!-- b002277 | prose | pages [16] -->
m

<!-- b002278 | prose | pages [16] -->
m

<!-- b002279 | prose | pages [16] -->
m

<!-- b002280 | prose | pages [16] -->
m

<!-- b002281 | prose | pages [16] -->
m

<!-- b002282 | prose | pages [16] -->
m

<!-- b002283 | prose | pages [16] -->
m

<!-- b002284 | prose | pages [16] -->
m

<!-- b002285 | prose | pages [16] -->
m

<!-- b002286 | prose | pages [16] -->
m

<!-- b002287 | prose | pages [16] -->
m

<!-- b002288 | prose | pages [16] -->
m

<!-- b002289 | prose | pages [16] -->
m

<!-- b002290 | prose | pages [16] -->
m

<!-- b002291 | prose | pages [16] -->
m

<!-- b002292 | prose | pages [16] -->
m

<!-- b002293 | prose | pages [16] -->
m

<!-- b002294 | prose | pages [16] -->
m

<!-- b002295 | prose | pages [16] -->
m

<!-- b002296 | prose | pages [16] -->
m

<!-- b002297 | prose | pages [16] -->
m

<!-- b002298 | prose | pages [16] -->
m

<!-- b002299 | prose | pages [16] -->
m

<!-- b002300 | prose | pages [16] -->
m

<!-- b002301 | prose | pages [16] -->
m

<!-- b002302 | prose | pages [16] -->
m

<!-- b002303 | prose | pages [16] -->
m

<!-- b002304 | prose | pages [16] -->
m

<!-- b002305 | prose | pages [16] -->
m

<!-- b002306 | prose | pages [16] -->
m

<!-- b002307 | prose | pages [16] -->
m

<!-- b002308 | prose | pages [16] -->
m

<!-- b002309 | prose | pages [16] -->
m

<!-- b002310 | prose | pages [16] -->
m

<!-- b002311 | prose | pages [16] -->
m

<!-- b002312 | prose | pages [16] -->
m

<!-- b002313 | prose | pages [16] -->
m

<!-- b002314 | prose | pages [16] -->
m

<!-- b002315 | prose | pages [16] -->
m

<!-- b002316 | prose | pages [16] -->
m

<!-- b002317 | prose | pages [16] -->
m

<!-- b002318 | prose | pages [16] -->
m

<!-- b002319 | prose | pages [16] -->
m

<!-- b002320 | prose | pages [16] -->
m

<!-- b002321 | prose | pages [16] -->
m

<!-- b002322 | prose | pages [16] -->
m

<!-- b002323 | prose | pages [16] -->
m

<!-- b002324 | prose | pages [16] -->
m

<!-- b002325 | prose | pages [16] -->
m

<!-- b002326 | prose | pages [16] -->
m

<!-- b002327 | prose | pages [16] -->
m

<!-- b002328 | prose | pages [16] -->
m

<!-- b002329 | prose | pages [16] -->
m

<!-- b002330 | prose | pages [16] -->
m

<!-- b002331 | prose | pages [16] -->
m

<!-- b002332 | prose | pages [16] -->
m

<!-- b002333 | prose | pages [16] -->
m

<!-- b002334 | prose | pages [16] -->
m

<!-- b002335 | prose | pages [16] -->
m

<!-- b002336 | prose | pages [16] -->
m

<!-- b002337 | prose | pages [16] -->
m

<!-- b002338 | prose | pages [16] -->
m

<!-- b002339 | prose | pages [16] -->
m

<!-- b002340 | prose | pages [16] -->
m

<!-- b002341 | prose | pages [16] -->
m

<!-- b002342 | prose | pages [16] -->
m

<!-- b002343 | prose | pages [16] -->
m

<!-- b002344 | prose | pages [16] -->
m

<!-- b002345 | prose | pages [16] -->
m

<!-- b002346 | prose | pages [16] -->
m

<!-- b002347 | prose | pages [16] -->
m

<!-- b002348 | prose | pages [16] -->
m

<!-- b002349 | prose | pages [16] -->
m

<!-- b002350 | prose | pages [16] -->
m

<!-- b002351 | prose | pages [16] -->
m

<!-- b002352 | prose | pages [16] -->
P

<!-- b002353 | prose | pages [16] -->
c,s Pcs

<!-- b002354 | prose | pages [16] -->
Count

<!-- b002355 | prose | pages [16] -->
Total points won in the Games across all countries and all sports.

<!-- b002356 | prose | pages [16] -->
Count Revealed Comparative Advantage Index by country c in sport s. RCAIcs SPE Sport-Point Efficiency.

<!-- b002357 | prose | pages [16] -->
Unitless (Index) Unitless Sport-Point Share for country c. SPSc Unitless

<!-- b002358 | caption | pages [16] -->
Table 7: Variable Definitions

<!-- b002359 | prose | pages [16] -->
We will apply each of these indicators of a sport’s importance to the United States and Netherlands in the most recent Olympic game: Paris Olympics, 2024. Additionally, since there were too many unique “sports”, we will only consider the top 10 per country.

<!-- b002360 | heading | pages [16] -->
1. Sport-Points Efficiency

<!-- b002361 | prose | pages [16] -->
SPE = Pcs

<!-- b002362 | heading | pages [16] -->
2. Sport-Points Share

<!-- b002363 | prose | pages [16] -->
Acs

<!-- b002364 | prose | pages [16] -->
Pcs SPSc =

<!-- b002365 | heading | pages [16] -->
3. Revealed Comparative Advantage (RCA)

<!-- b002366 | prose | pages [16] -->
Pcs P

<!-- b002367 | prose | pages [16] -->
s Pcs

<!-- b002368 | prose | pages [16] -->
RCAIcs =

<!-- b002369 | prose | pages [16] -->
P

<!-- b002370 | prose | pages [16] -->
c Pcs P

<!-- b002371 | prose | pages [16] -->
P

<!-- b002372 | prose | pages [16] -->
c Pcs

<!-- b002373 | prose | pages [16] -->
关注数学模型

<!-- b002374 | furniture | pages [16] -->
2

<!-- b002375 | prose | pages [16] -->
P

<!-- b002376 | prose | pages [16] -->
c,s Pcs

<!-- b002377 | furniture | pages [16] -->
MATHmodels

<!-- b002378 | furniture | pages [16] -->
获取更多资讯

<!-- b002379 | prose | pages [16] -->
= SPSc

<!-- b002380 | prose | pages [16] -->
P

<!-- b002381 | prose | pages [16] -->
s Pcs

<!-- b002382 | prose | pages [16] -->
c,s Pcs

<!-- b002383 | furniture | pages [17] -->
Team 2522820

<!-- b002384 | prose | pages [17] -->
Pcs Acs SPE Sport Weightlifting 8.00 5 1.600 Wrestling 21.00 16 1.313

<!-- b002385 | furniture | pages [17] -->
Page 17

<!-- b002386 | prose | pages [17] -->
Pcs Acs SPE Sport Sailing 15.71 11 1.429 Rowing 32.96 33 0.999

<!-- b002387 | prose | pages [17] -->
微信公众号：数学模型

<!-- b002388 | prose | pages [17] -->
Athletics 164.34 126 1.304 Surfing 6.00 5 1.200 Basketball 25.03 24 1.043 Shooting 16.67 17 0.980 Archery 3.50 4 0.875 Golf 6.00 7 0.857 Fencing 14.00 20 0.700 Skateboarding 8.00 12 0.667

<!-- b002389 | caption | pages [17] -->
Table 8: Top 10 SPE Values for Sports in the

<!-- b002390 | prose | pages [17] -->
United States

<!-- b002391 | prose | pages [17] -->
Athletics 43.3 46 0.941 Equestrian 0.8 12 0.067 Volleyball 0.0 13 0.000 Triathlon 0.0 4 0.000 Tennis 0.0 6 0 Handball 0 10 0 Judo 0 10 0 Archery 0 4 0

<!-- b002392 | caption | pages [17] -->
Table 9: Top 10 SPE Values for Sports in the

<!-- b002393 | prose | pages [17] -->
Netherlands

<!-- b002394 | prose | pages [17] -->
微信号：MATHmodels

<!-- b002395 | prose | pages [17] -->
P

<!-- b002396 | prose | pages [17] -->
Pcs

<!-- b002397 | prose | pages [17] -->
c Pcs SPSc

<!-- b002398 | prose | pages [17] -->
Sport

<!-- b002399 | prose | pages [17] -->
Basketball 25 44 0.57 Athletics 164 528 0.31 Surfing 6 22 0.27 Golf 6 22 0.27 Football 6 22 0.26 Aquatics 137 539 0.25 Volleyball 10 44 22.7 Gymnastics 38 198 0.19 Skateboarding 8 44 0.18 Tennis 6.25 55 0.11

<!-- b002400 | caption | pages [17] -->
Table 10: Top 10 SPSc Values for Sports in the

<!-- b002401 | prose | pages [17] -->
United States

<!-- b002402 | prose | pages [17] -->
P

<!-- b002403 | prose | pages [17] -->
P

<!-- b002404 | prose | pages [17] -->
SPSc

<!-- b002405 | prose | pages [17] -->
c,s Pcs

<!-- b002406 | prose | pages [17] -->
s Pcs RCAIcs

<!-- b002407 | prose | pages [17] -->
Sport

<!-- b002408 | prose | pages [17] -->
Basketball 0.57 3619 525 3.92 Athletics 0.31 3619 525 2.15 Surfing 0.27 3619 525 1.9 Golf 0.27 3619 525 1.9 Football 0.26 3619 525 1.79 Aquatics 0.25 3619 525 1.75 Volleyball 22.7 3619 525 1.57 Gymnastics 0.19 3619 525 1.30 Skateboarding 0.18 3619 525 1.25 Tennis 0.11 3619 525 0.78

<!-- b002409 | caption | pages [17] -->
Table 12: Top 10 RCAIcs Values for Sports in the

<!-- b002410 | prose | pages [17] -->
United States

<!-- b002411 | prose | pages [17] -->
P

<!-- b002412 | prose | pages [17] -->
Pcs

<!-- b002413 | prose | pages [17] -->
c Pcs SPSc

<!-- b002414 | prose | pages [17] -->
Sport

<!-- b002415 | prose | pages [17] -->
Rowing 32.96 154 0.214 Sailing 15.71 110 0.143 Cycling 30.64 242 0.127 Athletics 43.30 528 0.082 Basketball 3.00 44 0.068 Aquatics 16.51 539 0.031 Equestrian 0.80 66 0.012 ————- — — 0 ————- — — 0 ————- — — 0

<!-- b002416 | caption | pages [17] -->
Table 11: Top 10 SPSc Values for Sports in the

<!-- b002417 | prose | pages [17] -->
Netherlands

<!-- b002418 | prose | pages [17] -->
P

<!-- b002419 | prose | pages [17] -->
P

<!-- b002420 | prose | pages [17] -->
c,s Pcs

<!-- b002421 | prose | pages [17] -->
s Pcs

<!-- b002422 | prose | pages [17] -->
SPSc

<!-- b002423 | prose | pages [17] -->
RCAIcs

<!-- b002424 | prose | pages [17] -->
Sport

<!-- b002425 | prose | pages [17] -->
Rowing 0.214 3619 143 5.42 Sailing 0.143 3619 143 3.62 Cycling 0.127 3619 143 3.21 Athletics 0.082 3619 143 2.08 Basketball 0.068 3619 143 1.73 Aquatics 0.031 3619 143 0.78 Equestrian 0.012 3619 143 0.31 ————- — — — 0 ————- — — — 0 ————- — — — 0

<!-- b002426 | caption | pages [17] -->
Table 13: Top 10 RCAIcs Values for Sports in the

<!-- b002427 | prose | pages [17] -->
Netherlands

<!-- b002428 | prose | pages [17] -->
Since SPSc is a building block of RCAIcs, we chose to only consider the data from the top 10 SPE and top 10 RCAIcs.

<!-- b002429 | prose | pages [17] -->
SPE by definition tells us the return on investment. If we expect each athlete to contribute at least 1 ranking

<!-- b002430 | furniture | pages [18] -->
Team 2522820

<!-- b002431 | furniture | pages [18] -->
Page 18

<!-- b002432 | prose | pages [18] -->
point, then SPE > 1, tells us that there were more points won in a sport than the amount of athletes. This means that for a lower use of resources on athlete expenditures and training, countries get a higher return of points. This may suggest to countries the importance of sports that have a high return of ranking points. So, for the United States, they may consider investing more in their Top 5 in Table 8. And for the Netherlands, they may consider investing more in Sailing.

<!-- b002433 | prose | pages [18] -->
If RCAIcs > 1, then that sport is considered to have a competitive advantage against the other countries competing in the same sports. This value is integral for determining the importance of sports as it allows a country to know what sports they are outperforming others in. For the United States, this means almost all of the sports in Table 12. While for the Netherlands, this would be their Top 5 within Table 13.

<!-- b002434 | prose | pages [18] -->
3.6.6 Home Country Effects

<!-- b002435 | prose | pages [18] -->
It’s a well-known fact that the host country often has a competitive advantage whether it’s due to psychological factors or a country’s ability to select sports (like in the Games). We can see preliminary evidence of a home country advantage just by looking at the increase in medal counts for all host countries.

<!-- b002436 | caption | pages [18] -->
Table 14: ∆Total Medal Count between host year and previous competition year for last 6 Host Countries

<!-- b002437 | prose | pages [18] -->
Host Year France 2024 Japan 2020 Brazil 2016 Great Britain 2012 China 2008 Greece 2004 ∆Total Medal Count 31 17 2 14 37 3

<!-- b002438 | prose | pages [18] -->
Now that we know this hosting advantage is present at the Games, we want to understand how the events chosen affect this advantage. According to the IOC, host countries have only been allowed to propose (influence the choosing) of events since the 2020 Tokyo Olympics. This means that to understand how the events chosen impact home country results, we are limited to data from the 2020 Tokyo Olympics and 2024 Paris Olympics.

<!-- b002439 | prose | pages [18] -->
By applying the RCA index from 3.6.5 on each unique event offered to the host country each year, we could understand the influence of events that the host country selected. Again, an RCAIcs > 1 would indicate that the event affects results more than they would for a majority of the other competing countries. However, we could not apply this in the given time.

<!-- b002440 | prose | pages [18] -->
Problem 2: Detecting and Utilizing the Great Coach Effect 4

<!-- b002441 | prose | pages [18] -->
4.1 Detecting the Great Coach Effect

<!-- b002442 | prose | pages [18] -->
m

<!-- b002443 | prose | pages [18] -->
m

<!-- b002444 | prose | pages [18] -->
m

<!-- b002445 | prose | pages [18] -->
m

<!-- b002446 | prose | pages [18] -->
m

<!-- b002447 | prose | pages [18] -->
m

<!-- b002448 | prose | pages [18] -->
m

<!-- b002449 | prose | pages [18] -->
m

<!-- b002450 | prose | pages [18] -->
m

<!-- b002451 | prose | pages [18] -->
m

<!-- b002452 | prose | pages [18] -->
m

<!-- b002453 | prose | pages [18] -->
m

<!-- b002454 | prose | pages [18] -->
m

<!-- b002455 | prose | pages [18] -->
m

<!-- b002456 | prose | pages [18] -->
m

<!-- b002457 | prose | pages [18] -->
m

<!-- b002458 | prose | pages [18] -->
m

<!-- b002459 | prose | pages [18] -->
m

<!-- b002460 | prose | pages [18] -->
m

<!-- b002461 | prose | pages [18] -->
m

<!-- b002462 | prose | pages [18] -->
m

<!-- b002463 | prose | pages [18] -->
m

<!-- b002464 | prose | pages [18] -->
Our primary consideration when developing a model to detect great coach effects was the fact that we had

<!-- b002465 | prose | pages [18] -->
m

<!-- b002466 | prose | pages [18] -->
m

<!-- b002467 | prose | pages [18] -->
m

<!-- b002468 | prose | pages [18] -->
m

<!-- b002469 | prose | pages [18] -->
m

<!-- b002470 | prose | pages [18] -->
m

<!-- b002471 | prose | pages [18] -->
m

<!-- b002472 | prose | pages [18] -->
m

<!-- b002473 | prose | pages [18] -->
m

<!-- b002474 | prose | pages [18] -->
m

<!-- b002475 | prose | pages [18] -->
m

<!-- b002476 | prose | pages [18] -->
m

<!-- b002477 | prose | pages [18] -->
m

<!-- b002478 | prose | pages [18] -->
m

<!-- b002479 | prose | pages [18] -->
m

<!-- b002480 | prose | pages [18] -->
m

<!-- b002481 | prose | pages [18] -->
m

<!-- b002482 | prose | pages [18] -->
m

<!-- b002483 | prose | pages [18] -->
m

<!-- b002484 | prose | pages [18] -->
m

<!-- b002485 | prose | pages [18] -->
m

<!-- b002486 | prose | pages [18] -->
m

<!-- b002487 | prose | pages [18] -->
m

<!-- b002488 | prose | pages [18] -->
m

<!-- b002489 | prose | pages [18] -->
m

<!-- b002490 | prose | pages [18] -->
m

<!-- b002491 | prose | pages [18] -->
m

<!-- b002492 | prose | pages [18] -->
m

<!-- b002493 | prose | pages [18] -->
m

<!-- b002494 | prose | pages [18] -->
m

<!-- b002495 | prose | pages [18] -->
m

<!-- b002496 | prose | pages [18] -->
m

<!-- b002497 | prose | pages [18] -->
m

<!-- b002498 | prose | pages [18] -->
m

<!-- b002499 | prose | pages [18] -->
m

<!-- b002500 | prose | pages [18] -->
m

<!-- b002501 | prose | pages [18] -->
m

<!-- b002502 | prose | pages [18] -->
m

<!-- b002503 | prose | pages [18] -->
m

<!-- b002504 | prose | pages [18] -->
m

<!-- b002505 | prose | pages [18] -->
m

<!-- b002506 | prose | pages [18] -->
m

<!-- b002507 | prose | pages [18] -->
m

<!-- b002508 | prose | pages [18] -->
m

<!-- b002509 | prose | pages [18] -->
m

<!-- b002510 | prose | pages [18] -->
m

<!-- b002511 | prose | pages [18] -->
m

<!-- b002512 | prose | pages [18] -->
m

<!-- b002513 | prose | pages [18] -->
m

<!-- b002514 | prose | pages [18] -->
m

<!-- b002515 | prose | pages [18] -->
m

<!-- b002516 | prose | pages [18] -->
m

<!-- b002517 | prose | pages [18] -->
m

<!-- b002518 | prose | pages [18] -->
m

<!-- b002519 | prose | pages [18] -->
m

<!-- b002520 | prose | pages [18] -->
m

<!-- b002521 | prose | pages [18] -->
m

<!-- b002522 | prose | pages [18] -->
m

<!-- b002523 | prose | pages [18] -->
m

<!-- b002524 | prose | pages [18] -->
m

<!-- b002525 | prose | pages [18] -->
m

<!-- b002526 | prose | pages [18] -->
m

<!-- b002527 | prose | pages [18] -->
m

<!-- b002528 | prose | pages [18] -->
m

<!-- b002529 | prose | pages [18] -->
m

<!-- b002530 | prose | pages [18] -->
m

<!-- b002531 | prose | pages [18] -->
m

<!-- b002532 | prose | pages [18] -->
m

<!-- b002533 | prose | pages [18] -->
m

<!-- b002534 | prose | pages [18] -->
m

<!-- b002535 | prose | pages [18] -->
m

<!-- b002536 | prose | pages [18] -->
m

<!-- b002537 | prose | pages [18] -->
m

<!-- b002538 | prose | pages [18] -->
m

<!-- b002539 | prose | pages [18] -->
m

<!-- b002540 | prose | pages [18] -->
m

<!-- b002541 | prose | pages [18] -->
m

<!-- b002542 | prose | pages [18] -->
m

<!-- b002543 | prose | pages [18] -->
m

<!-- b002544 | prose | pages [18] -->
m

<!-- b002545 | prose | pages [18] -->
m

<!-- b002546 | prose | pages [18] -->
m

<!-- b002547 | prose | pages [18] -->
m

<!-- b002548 | prose | pages [18] -->
m

<!-- b002549 | prose | pages [18] -->
m

<!-- b002550 | prose | pages [18] -->
m

<!-- b002551 | prose | pages [18] -->
m

<!-- b002552 | prose | pages [18] -->
m

<!-- b002553 | prose | pages [18] -->
m

<!-- b002554 | prose | pages [18] -->
m

<!-- b002555 | prose | pages [18] -->
m

<!-- b002556 | prose | pages [18] -->
m

<!-- b002557 | prose | pages [18] -->
m

<!-- b002558 | prose | pages [18] -->
m

<!-- b002559 | prose | pages [18] -->
m

<!-- b002560 | prose | pages [18] -->
m

<!-- b002561 | prose | pages [18] -->
m

<!-- b002562 | prose | pages [18] -->
m

<!-- b002563 | prose | pages [18] -->
m

<!-- b002564 | prose | pages [18] -->
m

<!-- b002565 | prose | pages [18] -->
m

<!-- b002566 | prose | pages [18] -->
m

<!-- b002567 | prose | pages [18] -->
m

<!-- b002568 | prose | pages [18] -->
m

<!-- b002569 | prose | pages [18] -->
m

<!-- b002570 | prose | pages [18] -->
m

<!-- b002571 | prose | pages [18] -->
m

<!-- b002572 | prose | pages [18] -->
m

<!-- b002573 | prose | pages [18] -->
m

<!-- b002574 | prose | pages [18] -->
m

<!-- b002575 | prose | pages [18] -->
m

<!-- b002576 | prose | pages [18] -->
m

<!-- b002577 | prose | pages [18] -->
m

<!-- b002578 | prose | pages [18] -->
m

<!-- b002579 | prose | pages [18] -->
m

<!-- b002580 | prose | pages [18] -->
m

<!-- b002581 | prose | pages [18] -->
m

<!-- b002582 | prose | pages [18] -->
m

<!-- b002583 | prose | pages [18] -->
m

<!-- b002584 | prose | pages [18] -->
m

<!-- b002585 | prose | pages [18] -->
m

<!-- b002586 | prose | pages [18] -->
m

<!-- b002587 | prose | pages [18] -->
m

<!-- b002588 | prose | pages [18] -->
m

<!-- b002589 | prose | pages [18] -->
very limited data: the only accessible data that was relevant to our model were the point distributions by nation

<!-- b002590 | prose | pages [18] -->
m

<!-- b002591 | prose | pages [18] -->
m

<!-- b002592 | prose | pages [18] -->
m

<!-- b002593 | prose | pages [18] -->
m

<!-- b002594 | prose | pages [18] -->
m

<!-- b002595 | prose | pages [18] -->
m

<!-- b002596 | prose | pages [18] -->
m

<!-- b002597 | prose | pages [18] -->
m

<!-- b002598 | prose | pages [18] -->
m

<!-- b002599 | prose | pages [18] -->
m

<!-- b002600 | prose | pages [18] -->
m

<!-- b002601 | prose | pages [18] -->
m

<!-- b002602 | prose | pages [18] -->
m

<!-- b002603 | prose | pages [18] -->
m

<!-- b002604 | prose | pages [18] -->
m

<!-- b002605 | prose | pages [18] -->
m

<!-- b002606 | prose | pages [18] -->
m

<!-- b002607 | prose | pages [18] -->
m

<!-- b002608 | prose | pages [18] -->
m

<!-- b002609 | prose | pages [18] -->
m

<!-- b002610 | prose | pages [18] -->
m

<!-- b002611 | prose | pages [18] -->
m

<!-- b002612 | prose | pages [18] -->
m

<!-- b002613 | prose | pages [18] -->
m

<!-- b002614 | prose | pages [18] -->
m

<!-- b002615 | prose | pages [18] -->
m

<!-- b002616 | prose | pages [18] -->
m

<!-- b002617 | prose | pages [18] -->
m

<!-- b002618 | prose | pages [18] -->
m

<!-- b002619 | prose | pages [18] -->
m

<!-- b002620 | prose | pages [18] -->
m

<!-- b002621 | prose | pages [18] -->
m

<!-- b002622 | prose | pages [18] -->
m

<!-- b002623 | prose | pages [18] -->
m

<!-- b002624 | prose | pages [18] -->
m

<!-- b002625 | prose | pages [18] -->
m

<!-- b002626 | prose | pages [18] -->
m

<!-- b002627 | prose | pages [18] -->
m

<!-- b002628 | prose | pages [18] -->
m

<!-- b002629 | prose | pages [18] -->
m

<!-- b002630 | prose | pages [18] -->
m

<!-- b002631 | prose | pages [18] -->
m

<!-- b002632 | prose | pages [18] -->
m

<!-- b002633 | prose | pages [18] -->
m

<!-- b002634 | prose | pages [18] -->
m

<!-- b002635 | prose | pages [18] -->
m

<!-- b002636 | prose | pages [18] -->
m

<!-- b002637 | prose | pages [18] -->
m

<!-- b002638 | prose | pages [18] -->
m

<!-- b002639 | prose | pages [18] -->
m

<!-- b002640 | prose | pages [18] -->
m

<!-- b002641 | prose | pages [18] -->
m

<!-- b002642 | prose | pages [18] -->
m

<!-- b002643 | prose | pages [18] -->
m

<!-- b002644 | prose | pages [18] -->
m

<!-- b002645 | prose | pages [18] -->
m

<!-- b002646 | prose | pages [18] -->
m

<!-- b002647 | prose | pages [18] -->
m

<!-- b002648 | prose | pages [18] -->
m

<!-- b002649 | prose | pages [18] -->
m

<!-- b002650 | prose | pages [18] -->
m

<!-- b002651 | prose | pages [18] -->
m

<!-- b002652 | prose | pages [18] -->
m

<!-- b002653 | prose | pages [18] -->
m

<!-- b002654 | prose | pages [18] -->
m

<!-- b002655 | prose | pages [18] -->
m

<!-- b002656 | prose | pages [18] -->
m

<!-- b002657 | prose | pages [18] -->
m

<!-- b002658 | prose | pages [18] -->
m

<!-- b002659 | prose | pages [18] -->
m

<!-- b002660 | prose | pages [18] -->
m

<!-- b002661 | prose | pages [18] -->
m

<!-- b002662 | prose | pages [18] -->
m

<!-- b002663 | prose | pages [18] -->
m

<!-- b002664 | prose | pages [18] -->
m

<!-- b002665 | prose | pages [18] -->
m

<!-- b002666 | prose | pages [18] -->
m

<!-- b002667 | prose | pages [18] -->
m

<!-- b002668 | prose | pages [18] -->
m

<!-- b002669 | prose | pages [18] -->
m

<!-- b002670 | prose | pages [18] -->
m

<!-- b002671 | prose | pages [18] -->
m

<!-- b002672 | prose | pages [18] -->
m

<!-- b002673 | prose | pages [18] -->
m

<!-- b002674 | prose | pages [18] -->
m

<!-- b002675 | prose | pages [18] -->
m

<!-- b002676 | prose | pages [18] -->
m

<!-- b002677 | prose | pages [18] -->
m

<!-- b002678 | prose | pages [18] -->
m

<!-- b002679 | prose | pages [18] -->
m

<!-- b002680 | prose | pages [18] -->
m

<!-- b002681 | prose | pages [18] -->
m

<!-- b002682 | prose | pages [18] -->
m

<!-- b002683 | prose | pages [18] -->
m

<!-- b002684 | prose | pages [18] -->
m

<!-- b002685 | prose | pages [18] -->
m

<!-- b002686 | prose | pages [18] -->
m

<!-- b002687 | prose | pages [18] -->
m

<!-- b002688 | prose | pages [18] -->
m

<!-- b002689 | prose | pages [18] -->
m

<!-- b002690 | prose | pages [18] -->
m

<!-- b002691 | prose | pages [18] -->
m

<!-- b002692 | prose | pages [18] -->
m

<!-- b002693 | prose | pages [18] -->
m

<!-- b002694 | prose | pages [18] -->
m

<!-- b002695 | prose | pages [18] -->
m

<!-- b002696 | prose | pages [18] -->
m

<!-- b002697 | prose | pages [18] -->
m

<!-- b002698 | prose | pages [18] -->
m

<!-- b002699 | prose | pages [18] -->
m

<!-- b002700 | prose | pages [18] -->
m

<!-- b002701 | prose | pages [18] -->
m

<!-- b002702 | prose | pages [18] -->
m

<!-- b002703 | prose | pages [18] -->
m

<!-- b002704 | prose | pages [18] -->
m

<!-- b002705 | prose | pages [18] -->
m

<!-- b002706 | prose | pages [18] -->
m

<!-- b002707 | prose | pages [18] -->
m

<!-- b002708 | prose | pages [18] -->
m

<!-- b002709 | prose | pages [18] -->
m

<!-- b002710 | prose | pages [18] -->
m

<!-- b002711 | prose | pages [18] -->
m

<!-- b002712 | prose | pages [18] -->
m

<!-- b002713 | prose | pages [18] -->
m

<!-- b002714 | prose | pages [18] -->
m

<!-- b002715 | prose | pages [18] -->
m

<!-- b002716 | prose | pages [18] -->
m

<!-- b002717 | prose | pages [18] -->
m

<!-- b002718 | prose | pages [18] -->
m

<!-- b002719 | prose | pages [18] -->
m

<!-- b002720 | prose | pages [18] -->
m

<!-- b002721 | prose | pages [18] -->
m

<!-- b002722 | prose | pages [18] -->
m

<!-- b002723 | prose | pages [18] -->
m

<!-- b002724 | prose | pages [18] -->
m

<!-- b002725 | prose | pages [18] -->
m

<!-- b002726 | prose | pages [18] -->
m

<!-- b002727 | prose | pages [18] -->
m

<!-- b002728 | prose | pages [18] -->
and by sport, which we found by using the event limit approximation method from 4.6.2.

<!-- b002729 | prose | pages [18] -->
m

<!-- b002730 | prose | pages [18] -->
m

<!-- b002731 | prose | pages [18] -->
m

<!-- b002732 | prose | pages [18] -->
m

<!-- b002733 | prose | pages [18] -->
m

<!-- b002734 | prose | pages [18] -->
m

<!-- b002735 | prose | pages [18] -->
m

<!-- b002736 | prose | pages [18] -->
m

<!-- b002737 | prose | pages [18] -->
m

<!-- b002738 | prose | pages [18] -->
m

<!-- b002739 | prose | pages [18] -->
m

<!-- b002740 | prose | pages [18] -->
m

<!-- b002741 | prose | pages [18] -->
m

<!-- b002742 | prose | pages [18] -->
m

<!-- b002743 | prose | pages [18] -->
m

<!-- b002744 | prose | pages [18] -->
m

<!-- b002745 | prose | pages [18] -->
m

<!-- b002746 | prose | pages [18] -->
m

<!-- b002747 | prose | pages [18] -->
m

<!-- b002748 | prose | pages [18] -->
m

<!-- b002749 | prose | pages [18] -->
m

<!-- b002750 | prose | pages [18] -->
m

<!-- b002751 | prose | pages [18] -->
m

<!-- b002752 | prose | pages [18] -->
m

<!-- b002753 | prose | pages [18] -->
m

<!-- b002754 | prose | pages [18] -->
m

<!-- b002755 | prose | pages [18] -->
m

<!-- b002756 | prose | pages [18] -->
m

<!-- b002757 | prose | pages [18] -->
m

<!-- b002758 | prose | pages [18] -->
m

<!-- b002759 | prose | pages [18] -->
m

<!-- b002760 | prose | pages [18] -->
m

<!-- b002761 | prose | pages [18] -->
m

<!-- b002762 | prose | pages [18] -->
m

<!-- b002763 | prose | pages [18] -->
m

<!-- b002764 | prose | pages [18] -->
m

<!-- b002765 | prose | pages [18] -->
m

<!-- b002766 | prose | pages [18] -->
m

<!-- b002767 | prose | pages [18] -->
m

<!-- b002768 | prose | pages [18] -->
m

<!-- b002769 | prose | pages [18] -->
m

<!-- b002770 | prose | pages [18] -->
m

<!-- b002771 | prose | pages [18] -->
m

<!-- b002772 | prose | pages [18] -->
m

<!-- b002773 | prose | pages [18] -->
m

<!-- b002774 | prose | pages [18] -->
m

<!-- b002775 | prose | pages [18] -->
m

<!-- b002776 | prose | pages [18] -->
m

<!-- b002777 | prose | pages [18] -->
m

<!-- b002778 | prose | pages [18] -->
m

<!-- b002779 | prose | pages [18] -->
m

<!-- b002780 | prose | pages [18] -->
m

<!-- b002781 | prose | pages [18] -->
m

<!-- b002782 | prose | pages [18] -->
m

<!-- b002783 | prose | pages [18] -->
m

<!-- b002784 | prose | pages [18] -->
m

<!-- b002785 | prose | pages [18] -->
m

<!-- b002786 | prose | pages [18] -->
m

<!-- b002787 | prose | pages [18] -->
m

<!-- b002788 | prose | pages [18] -->
m

<!-- b002789 | prose | pages [18] -->
m

<!-- b002790 | prose | pages [18] -->
m

<!-- b002791 | prose | pages [18] -->
m

<!-- b002792 | prose | pages [18] -->
m

<!-- b002793 | prose | pages [18] -->
m

<!-- b002794 | prose | pages [18] -->
m

<!-- b002795 | prose | pages [18] -->
m

<!-- b002796 | prose | pages [18] -->
m

<!-- b002797 | prose | pages [18] -->
m

<!-- b002798 | prose | pages [18] -->
m

<!-- b002799 | prose | pages [18] -->
m

<!-- b002800 | prose | pages [18] -->
m

<!-- b002801 | prose | pages [18] -->
m

<!-- b002802 | prose | pages [18] -->
m

<!-- b002803 | prose | pages [18] -->
m

<!-- b002804 | prose | pages [18] -->
m

<!-- b002805 | prose | pages [18] -->
m

<!-- b002806 | prose | pages [18] -->
m

<!-- b002807 | prose | pages [18] -->
m

<!-- b002808 | prose | pages [18] -->
m

<!-- b002809 | prose | pages [18] -->
m

<!-- b002810 | prose | pages [18] -->
m

<!-- b002811 | prose | pages [18] -->
m

<!-- b002812 | prose | pages [18] -->
m

<!-- b002813 | prose | pages [18] -->
m

<!-- b002814 | prose | pages [18] -->
m

<!-- b002815 | prose | pages [18] -->
m

<!-- b002816 | prose | pages [18] -->
m

<!-- b002817 | prose | pages [18] -->
m

<!-- b002818 | prose | pages [18] -->
m

<!-- b002819 | prose | pages [18] -->
m

<!-- b002820 | prose | pages [18] -->
m

<!-- b002821 | prose | pages [18] -->
m

<!-- b002822 | prose | pages [18] -->
m

<!-- b002823 | prose | pages [18] -->
m

<!-- b002824 | prose | pages [18] -->
m

<!-- b002825 | prose | pages [18] -->
m

<!-- b002826 | prose | pages [18] -->
m

<!-- b002827 | prose | pages [18] -->
m

<!-- b002828 | prose | pages [18] -->
m

<!-- b002829 | prose | pages [18] -->
m

<!-- b002830 | prose | pages [18] -->
m

<!-- b002831 | prose | pages [18] -->
m

<!-- b002832 | prose | pages [18] -->
m

<!-- b002833 | prose | pages [18] -->
m

<!-- b002834 | prose | pages [18] -->
m

<!-- b002835 | prose | pages [18] -->
m

<!-- b002836 | prose | pages [18] -->
m

<!-- b002837 | prose | pages [18] -->
m

<!-- b002838 | prose | pages [18] -->
m

<!-- b002839 | prose | pages [18] -->
m

<!-- b002840 | prose | pages [18] -->
m

<!-- b002841 | prose | pages [18] -->
m

<!-- b002842 | prose | pages [18] -->
m

<!-- b002843 | prose | pages [18] -->
m

<!-- b002844 | prose | pages [18] -->
m

<!-- b002845 | prose | pages [18] -->
m

<!-- b002846 | prose | pages [18] -->
m

<!-- b002847 | prose | pages [18] -->
m

<!-- b002848 | prose | pages [18] -->
m

<!-- b002849 | prose | pages [18] -->
m

<!-- b002850 | prose | pages [18] -->
m

<!-- b002851 | prose | pages [18] -->
m

<!-- b002852 | prose | pages [18] -->
m

<!-- b002853 | prose | pages [18] -->
m

<!-- b002854 | prose | pages [18] -->
m

<!-- b002855 | prose | pages [18] -->
m

<!-- b002856 | prose | pages [18] -->
m

<!-- b002857 | prose | pages [18] -->
m

<!-- b002858 | prose | pages [18] -->
m

<!-- b002859 | prose | pages [18] -->
m

<!-- b002860 | prose | pages [18] -->
m

<!-- b002861 | prose | pages [18] -->
m

<!-- b002862 | prose | pages [18] -->
m

<!-- b002863 | prose | pages [18] -->
m

<!-- b002864 | prose | pages [18] -->
m

<!-- b002865 | prose | pages [18] -->
m

<!-- b002866 | prose | pages [18] -->
m

<!-- b002867 | prose | pages [18] -->
m

<!-- b002868 | prose | pages [18] -->
m

<!-- b002869 | prose | pages [18] -->
m

<!-- b002870 | prose | pages [18] -->
m

<!-- b002871 | prose | pages [18] -->
m

<!-- b002872 | prose | pages [18] -->
m

<!-- b002873 | prose | pages [18] -->
m

<!-- b002874 | prose | pages [18] -->
Many other factors—such as outstanding individual athletes or increased government investment in athletic

<!-- b002875 | prose | pages [18] -->
m

<!-- b002876 | prose | pages [18] -->
m

<!-- b002877 | prose | pages [18] -->
m

<!-- b002878 | prose | pages [18] -->
m

<!-- b002879 | prose | pages [18] -->
m

<!-- b002880 | prose | pages [18] -->
m

<!-- b002881 | prose | pages [18] -->
m

<!-- b002882 | prose | pages [18] -->
m

<!-- b002883 | prose | pages [18] -->
m

<!-- b002884 | prose | pages [18] -->
m

<!-- b002885 | prose | pages [18] -->
m

<!-- b002886 | prose | pages [18] -->
m

<!-- b002887 | prose | pages [18] -->
m

<!-- b002888 | prose | pages [18] -->
m

<!-- b002889 | prose | pages [18] -->
m

<!-- b002890 | prose | pages [18] -->
m

<!-- b002891 | prose | pages [18] -->
m

<!-- b002892 | prose | pages [18] -->
m

<!-- b002893 | prose | pages [18] -->
m

<!-- b002894 | prose | pages [18] -->
m

<!-- b002895 | prose | pages [18] -->
m

<!-- b002896 | prose | pages [18] -->
m

<!-- b002897 | prose | pages [18] -->
m

<!-- b002898 | prose | pages [18] -->
m

<!-- b002899 | prose | pages [18] -->
m

<!-- b002900 | prose | pages [18] -->
m

<!-- b002901 | prose | pages [18] -->
m

<!-- b002902 | prose | pages [18] -->
m

<!-- b002903 | prose | pages [18] -->
m

<!-- b002904 | prose | pages [18] -->
m

<!-- b002905 | prose | pages [18] -->
m

<!-- b002906 | prose | pages [18] -->
m

<!-- b002907 | prose | pages [18] -->
m

<!-- b002908 | prose | pages [18] -->
m

<!-- b002909 | prose | pages [18] -->
m

<!-- b002910 | prose | pages [18] -->
m

<!-- b002911 | prose | pages [18] -->
m

<!-- b002912 | prose | pages [18] -->
m

<!-- b002913 | prose | pages [18] -->
m

<!-- b002914 | prose | pages [18] -->
m

<!-- b002915 | prose | pages [18] -->
m

<!-- b002916 | prose | pages [18] -->
m

<!-- b002917 | prose | pages [18] -->
m

<!-- b002918 | prose | pages [18] -->
m

<!-- b002919 | prose | pages [18] -->
m

<!-- b002920 | prose | pages [18] -->
m

<!-- b002921 | prose | pages [18] -->
m

<!-- b002922 | prose | pages [18] -->
m

<!-- b002923 | prose | pages [18] -->
m

<!-- b002924 | prose | pages [18] -->
m

<!-- b002925 | prose | pages [18] -->
m

<!-- b002926 | prose | pages [18] -->
m

<!-- b002927 | prose | pages [18] -->
m

<!-- b002928 | prose | pages [18] -->
m

<!-- b002929 | prose | pages [18] -->
m

<!-- b002930 | prose | pages [18] -->
m

<!-- b002931 | prose | pages [18] -->
m

<!-- b002932 | prose | pages [18] -->
m

<!-- b002933 | prose | pages [18] -->
m

<!-- b002934 | prose | pages [18] -->
m

<!-- b002935 | prose | pages [18] -->
m

<!-- b002936 | prose | pages [18] -->
m

<!-- b002937 | prose | pages [18] -->
m

<!-- b002938 | prose | pages [18] -->
m

<!-- b002939 | prose | pages [18] -->
m

<!-- b002940 | prose | pages [18] -->
m

<!-- b002941 | prose | pages [18] -->
m

<!-- b002942 | prose | pages [18] -->
m

<!-- b002943 | prose | pages [18] -->
m

<!-- b002944 | prose | pages [18] -->
m

<!-- b002945 | prose | pages [18] -->
m

<!-- b002946 | prose | pages [18] -->
m

<!-- b002947 | prose | pages [18] -->
m

<!-- b002948 | prose | pages [18] -->
m

<!-- b002949 | prose | pages [18] -->
m

<!-- b002950 | prose | pages [18] -->
m

<!-- b002951 | prose | pages [18] -->
m

<!-- b002952 | prose | pages [18] -->
m

<!-- b002953 | prose | pages [18] -->
m

<!-- b002954 | prose | pages [18] -->
m

<!-- b002955 | prose | pages [18] -->
m

<!-- b002956 | prose | pages [18] -->
m

<!-- b002957 | prose | pages [18] -->
m

<!-- b002958 | prose | pages [18] -->
m

<!-- b002959 | prose | pages [18] -->
m

<!-- b002960 | prose | pages [18] -->
m

<!-- b002961 | prose | pages [18] -->
m

<!-- b002962 | prose | pages [18] -->
m

<!-- b002963 | prose | pages [18] -->
m

<!-- b002964 | prose | pages [18] -->
m

<!-- b002965 | prose | pages [18] -->
m

<!-- b002966 | prose | pages [18] -->
m

<!-- b002967 | prose | pages [18] -->
m

<!-- b002968 | prose | pages [18] -->
m

<!-- b002969 | prose | pages [18] -->
m

<!-- b002970 | prose | pages [18] -->
m

<!-- b002971 | prose | pages [18] -->
m

<!-- b002972 | prose | pages [18] -->
m

<!-- b002973 | prose | pages [18] -->
m

<!-- b002974 | prose | pages [18] -->
m

<!-- b002975 | prose | pages [18] -->
m

<!-- b002976 | prose | pages [18] -->
m

<!-- b002977 | prose | pages [18] -->
m

<!-- b002978 | prose | pages [18] -->
m

<!-- b002979 | prose | pages [18] -->
m

<!-- b002980 | prose | pages [18] -->
m

<!-- b002981 | prose | pages [18] -->
m

<!-- b002982 | prose | pages [18] -->
m

<!-- b002983 | prose | pages [18] -->
m

<!-- b002984 | prose | pages [18] -->
m

<!-- b002985 | prose | pages [18] -->
m

<!-- b002986 | prose | pages [18] -->
m

<!-- b002987 | prose | pages [18] -->
programs—could affect performances, and because of our limited data, it is impossible to show that any changes

<!-- b002988 | prose | pages [18] -->
m

<!-- b002989 | prose | pages [18] -->
m

<!-- b002990 | prose | pages [18] -->
m

<!-- b002991 | prose | pages [18] -->
m

<!-- b002992 | prose | pages [18] -->
m

<!-- b002993 | prose | pages [18] -->
m

<!-- b002994 | prose | pages [18] -->
m

<!-- b002995 | prose | pages [18] -->
m

<!-- b002996 | prose | pages [18] -->
m

<!-- b002997 | prose | pages [18] -->
m

<!-- b002998 | prose | pages [18] -->
m

<!-- b002999 | prose | pages [18] -->
m

<!-- b003000 | prose | pages [18] -->
m

<!-- b003001 | prose | pages [18] -->
m

<!-- b003002 | prose | pages [18] -->
m

<!-- b003003 | prose | pages [18] -->
m

<!-- b003004 | prose | pages [18] -->
m

<!-- b003005 | prose | pages [18] -->
m

<!-- b003006 | prose | pages [18] -->
m

<!-- b003007 | prose | pages [18] -->
m

<!-- b003008 | prose | pages [18] -->
m

<!-- b003009 | prose | pages [18] -->
m

<!-- b003010 | prose | pages [18] -->
m

<!-- b003011 | prose | pages [18] -->
m

<!-- b003012 | prose | pages [18] -->
m

<!-- b003013 | prose | pages [18] -->
m

<!-- b003014 | prose | pages [18] -->
m

<!-- b003015 | prose | pages [18] -->
m

<!-- b003016 | prose | pages [18] -->
m

<!-- b003017 | prose | pages [18] -->
m

<!-- b003018 | prose | pages [18] -->
m

<!-- b003019 | prose | pages [18] -->
m

<!-- b003020 | prose | pages [18] -->
m

<!-- b003021 | prose | pages [18] -->
m

<!-- b003022 | prose | pages [18] -->
m

<!-- b003023 | prose | pages [18] -->
m

<!-- b003024 | prose | pages [18] -->
m

<!-- b003025 | prose | pages [18] -->
m

<!-- b003026 | prose | pages [18] -->
m

<!-- b003027 | prose | pages [18] -->
m

<!-- b003028 | prose | pages [18] -->
m

<!-- b003029 | prose | pages [18] -->
m

<!-- b003030 | prose | pages [18] -->
m

<!-- b003031 | prose | pages [18] -->
m

<!-- b003032 | prose | pages [18] -->
m

<!-- b003033 | prose | pages [18] -->
m

<!-- b003034 | prose | pages [18] -->
m

<!-- b003035 | prose | pages [18] -->
m

<!-- b003036 | prose | pages [18] -->
m

<!-- b003037 | prose | pages [18] -->
m

<!-- b003038 | prose | pages [18] -->
m

<!-- b003039 | prose | pages [18] -->
m

<!-- b003040 | prose | pages [18] -->
m

<!-- b003041 | prose | pages [18] -->
m

<!-- b003042 | prose | pages [18] -->
m

<!-- b003043 | prose | pages [18] -->
m

<!-- b003044 | prose | pages [18] -->
m

<!-- b003045 | prose | pages [18] -->
m

<!-- b003046 | prose | pages [18] -->
m

<!-- b003047 | prose | pages [18] -->
m

<!-- b003048 | prose | pages [18] -->
m

<!-- b003049 | prose | pages [18] -->
m

<!-- b003050 | prose | pages [18] -->
m

<!-- b003051 | prose | pages [18] -->
m

<!-- b003052 | prose | pages [18] -->
m

<!-- b003053 | prose | pages [18] -->
m

<!-- b003054 | prose | pages [18] -->
m

<!-- b003055 | prose | pages [18] -->
m

<!-- b003056 | prose | pages [18] -->
m

<!-- b003057 | prose | pages [18] -->
m

<!-- b003058 | prose | pages [18] -->
m

<!-- b003059 | prose | pages [18] -->
m

<!-- b003060 | prose | pages [18] -->
m

<!-- b003061 | prose | pages [18] -->
m

<!-- b003062 | prose | pages [18] -->
m

<!-- b003063 | prose | pages [18] -->
m

<!-- b003064 | prose | pages [18] -->
m

<!-- b003065 | prose | pages [18] -->
m

<!-- b003066 | prose | pages [18] -->
m

<!-- b003067 | prose | pages [18] -->
m

<!-- b003068 | prose | pages [18] -->
m

<!-- b003069 | prose | pages [18] -->
m

<!-- b003070 | prose | pages [18] -->
m

<!-- b003071 | prose | pages [18] -->
m

<!-- b003072 | prose | pages [18] -->
m

<!-- b003073 | prose | pages [18] -->
m

<!-- b003074 | prose | pages [18] -->
m

<!-- b003075 | prose | pages [18] -->
m

<!-- b003076 | prose | pages [18] -->
m

<!-- b003077 | prose | pages [18] -->
m

<!-- b003078 | prose | pages [18] -->
m

<!-- b003079 | prose | pages [18] -->
m

<!-- b003080 | prose | pages [18] -->
m

<!-- b003081 | prose | pages [18] -->
m

<!-- b003082 | prose | pages [18] -->
m

<!-- b003083 | prose | pages [18] -->
m

<!-- b003084 | prose | pages [18] -->
m

<!-- b003085 | prose | pages [18] -->
m

<!-- b003086 | prose | pages [18] -->
m

<!-- b003087 | prose | pages [18] -->
m

<!-- b003088 | prose | pages [18] -->
m

<!-- b003089 | prose | pages [18] -->
m

<!-- b003090 | prose | pages [18] -->
m

<!-- b003091 | prose | pages [18] -->
m

<!-- b003092 | prose | pages [18] -->
m

<!-- b003093 | prose | pages [18] -->
m

<!-- b003094 | prose | pages [18] -->
m

<!-- b003095 | prose | pages [18] -->
m

<!-- b003096 | prose | pages [18] -->
m

<!-- b003097 | prose | pages [18] -->
m

<!-- b003098 | prose | pages [18] -->
m

<!-- b003099 | prose | pages [18] -->
m

<!-- b003100 | prose | pages [18] -->
m

<!-- b003101 | prose | pages [18] -->
m

<!-- b003102 | prose | pages [18] -->
m

<!-- b003103 | prose | pages [18] -->
m

<!-- b003104 | prose | pages [18] -->
m

<!-- b003105 | prose | pages [18] -->
m

<!-- b003106 | prose | pages [18] -->
m

<!-- b003107 | prose | pages [18] -->
m

<!-- b003108 | prose | pages [18] -->
m

<!-- b003109 | prose | pages [18] -->
m

<!-- b003110 | prose | pages [18] -->
m

<!-- b003111 | prose | pages [18] -->
m

<!-- b003112 | prose | pages [18] -->
m

<!-- b003113 | prose | pages [18] -->
m

<!-- b003114 | prose | pages [18] -->
m

<!-- b003115 | prose | pages [18] -->
m

<!-- b003116 | prose | pages [18] -->
m

<!-- b003117 | prose | pages [18] -->
m

<!-- b003118 | prose | pages [18] -->
m

<!-- b003119 | prose | pages [18] -->
m

<!-- b003120 | prose | pages [18] -->
m

<!-- b003121 | prose | pages [18] -->
m

<!-- b003122 | prose | pages [18] -->
m

<!-- b003123 | prose | pages [18] -->
m

<!-- b003124 | prose | pages [18] -->
m

<!-- b003125 | prose | pages [18] -->
m

<!-- b003126 | prose | pages [18] -->
m

<!-- b003127 | prose | pages [18] -->
m

<!-- b003128 | prose | pages [18] -->
m

<!-- b003129 | prose | pages [18] -->
m

<!-- b003130 | prose | pages [18] -->
m

<!-- b003131 | prose | pages [18] -->
m

<!-- b003132 | prose | pages [18] -->
m

<!-- b003133 | prose | pages [18] -->
m

<!-- b003134 | prose | pages [18] -->
in the point distributions for a given country and sport are directly due to the influence of a great coach, as they could be (and likely are) results of a combination of factors. In other words, the most we could accomplish with the provided data was finding possible instances of the great coach effect. However, we can examine the results of this model in the context of the history of great coaches to see how accurate it is.

<!-- b003135 | prose | pages [18] -->
关注数学模型

<!-- b003136 | furniture | pages [18] -->
2

<!-- b003137 | furniture | pages [18] -->
MATHmodels

<!-- b003138 | furniture | pages [18] -->
获取更多资讯

<!-- b003139 | furniture | pages [19] -->
Team 2522820

<!-- b003140 | prose | pages [19] -->
4.1.1 Time Series Analysis Setup

<!-- b003141 | furniture | pages [19] -->
Page 19

<!-- b003142 | prose | pages [19] -->
The general strategy behind our model to detect potential great coach effects is identifying a given coun- try’s performances in a given sport that are anomalously successful in the context of that country’s historical performances in the same sport. To do this, we applied time series analysis to the data.

<!-- b003143 | prose | pages [19] -->
A time series is a series of data that are equally spaced apart. Aside from a few notable exceptions—the 1916, 1940, and 1944 Games were canceled because of the World Wars—the regular four-year timing of the Games means that performances at the Games are suitable for time series analysis.

<!-- b003144 | prose | pages [19] -->
Many countries have been competing in the same sport for well over a century. Over this time, the influence of individual great coaches is greatly outweighed by a multitude of other factors. So, if we were to calculate the z-scores of each performance in the context of the country’s entire historical performance, the z-scores would be

<!-- b003145 | prose | pages [19] -->
微信公众号：数学模型

<!-- b003146 | prose | pages [19] -->
less meaningful. To more accurately interpret variations, we needed to calculate the z-scores of each performance in only the context of the Games immediately preceding and succeeding it. For this, we used a rolling window of four Games at a time (more detail provided in the outline).

<!-- b003147 | prose | pages [19] -->
4.1.2 Variable Definitions

<!-- b003148 | caption | pages [19] -->
Table 14: Variable Definitions

<!-- b003149 | prose | pages [19] -->
Variable Definition N Formula The total number of Games a given country has competed

<!-- b003150 | prose | pages [19] -->
微信号：MATHmodels

<!-- b003151 | prose | pages [19] -->
in for a given sport L Number of Games included in the segment for a given country and sport Ps Number of points earned in the segment for a given country and sport µ

<!-- b003152 | prose | pages [19] -->
PN

<!-- b003153 | prose | pages [19] -->
1

<!-- b003154 | prose | pages [19] -->
i=1 xi

<!-- b003155 | prose | pages [19] -->
Population mean points for a given country and sport over all Games

<!-- b003156 | prose | pages [19] -->
σ

<!-- b003157 | prose | pages [19] -->
N

<!-- b003158 | prose | pages [19] -->
q

<!-- b003159 | prose | pages [19] -->
PN

<!-- b003160 | prose | pages [19] -->
1

<!-- b003161 | prose | pages [19] -->
i=k(xi −µ)2

<!-- b003162 | prose | pages [19] -->
Population standard deviation of points for a given country and sport over all Games

<!-- b003163 | prose | pages [19] -->
x

<!-- b003164 | prose | pages [19] -->
N

<!-- b003165 | prose | pages [19] -->
Pk+3 1

<!-- b003166 | prose | pages [19] -->
i=k xi,

<!-- b003167 | prose | pages [19] -->
Sample mean points for a given country and sport over a rolling set of four Games

<!-- b003168 | prose | pages [19] -->
s

<!-- b003169 | prose | pages [19] -->
4

<!-- b003170 | prose | pages [19] -->
where k ∈{1, 2, ..., N −3}

<!-- b003171 | prose | pages [19] -->
q

<!-- b003172 | prose | pages [19] -->
Pk+3 1

<!-- b003173 | prose | pages [19] -->
i=k (xi −x)2,

<!-- b003174 | prose | pages [19] -->
Sample standard deviation of points for a given country and sport over a rolling set of four Games

<!-- b003175 | prose | pages [19] -->
C

<!-- b003176 | prose | pages [19] -->
4

<!-- b003177 | prose | pages [19] -->
where k ∈{1, 2, ..., N −3}

<!-- b003178 | prose | pages [19] -->
(Ps −µ · L) · 100%

<!-- b003179 | prose | pages [19] -->
Relative contribution of great coaches for a given country and sport

<!-- b003180 | prose | pages [19] -->
∆Pnorm

<!-- b003181 | prose | pages [19] -->
C

<!-- b003182 | prose | pages [19] -->
Normalized relative contribution of great coaches for a given country and sport

<!-- b003183 | prose | pages [19] -->
L

<!-- b003184 | prose | pages [19] -->
For a given country and sport, this was the outline of the model:

<!-- b003185 | prose | pages [19] -->
1. Calculate x and s in a rolling window of four Games at a time over the history of the country’s participation in that sport.

<!-- b003186 | prose | pages [19] -->
(a) E.g. for a country that has participated in a sport since 1896, the windows for that country-sport pair

<!-- b003187 | prose | pages [19] -->
would start from [1896, 1900, 1904, 1908], then [1900, 1904, 1908, 1912], and so on. The means and sample standard deviations of the country’s points in each of these sets of years are calculated.

<!-- b003188 | prose | pages [19] -->
m

<!-- b003189 | prose | pages [19] -->
m

<!-- b003190 | prose | pages [19] -->
m

<!-- b003191 | prose | pages [19] -->
m

<!-- b003192 | prose | pages [19] -->
m

<!-- b003193 | prose | pages [19] -->
m

<!-- b003194 | prose | pages [19] -->
m

<!-- b003195 | prose | pages [19] -->
m

<!-- b003196 | prose | pages [19] -->
m

<!-- b003197 | prose | pages [19] -->
m

<!-- b003198 | prose | pages [19] -->
m

<!-- b003199 | prose | pages [19] -->
m

<!-- b003200 | prose | pages [19] -->
m

<!-- b003201 | prose | pages [19] -->
m

<!-- b003202 | prose | pages [19] -->
m

<!-- b003203 | prose | pages [19] -->
m

<!-- b003204 | prose | pages [19] -->
m

<!-- b003205 | prose | pages [19] -->
m

<!-- b003206 | prose | pages [19] -->
m

<!-- b003207 | prose | pages [19] -->
m

<!-- b003208 | prose | pages [19] -->
m

<!-- b003209 | prose | pages [19] -->
m

<!-- b003210 | prose | pages [19] -->
m

<!-- b003211 | prose | pages [19] -->
m

<!-- b003212 | prose | pages [19] -->
m

<!-- b003213 | prose | pages [19] -->
m

<!-- b003214 | prose | pages [19] -->
m

<!-- b003215 | prose | pages [19] -->
m

<!-- b003216 | prose | pages [19] -->
m

<!-- b003217 | prose | pages [19] -->
m

<!-- b003218 | prose | pages [19] -->
m

<!-- b003219 | prose | pages [19] -->
m

<!-- b003220 | prose | pages [19] -->
m

<!-- b003221 | prose | pages [19] -->
m

<!-- b003222 | prose | pages [19] -->
m

<!-- b003223 | prose | pages [19] -->
m

<!-- b003224 | prose | pages [19] -->
m

<!-- b003225 | prose | pages [19] -->
m

<!-- b003226 | prose | pages [19] -->
m

<!-- b003227 | prose | pages [19] -->
m

<!-- b003228 | prose | pages [19] -->
m

<!-- b003229 | prose | pages [19] -->
m

<!-- b003230 | prose | pages [19] -->
m

<!-- b003231 | prose | pages [19] -->
m

<!-- b003232 | prose | pages [19] -->
m

<!-- b003233 | prose | pages [19] -->
m

<!-- b003234 | prose | pages [19] -->
m

<!-- b003235 | prose | pages [19] -->
m

<!-- b003236 | prose | pages [19] -->
m

<!-- b003237 | prose | pages [19] -->
m

<!-- b003238 | prose | pages [19] -->
m

<!-- b003239 | prose | pages [19] -->
m

<!-- b003240 | prose | pages [19] -->
m

<!-- b003241 | prose | pages [19] -->
m

<!-- b003242 | prose | pages [19] -->
m

<!-- b003243 | prose | pages [19] -->
m

<!-- b003244 | prose | pages [19] -->
m

<!-- b003245 | prose | pages [19] -->
m

<!-- b003246 | prose | pages [19] -->
m

<!-- b003247 | prose | pages [19] -->
m

<!-- b003248 | prose | pages [19] -->
m

<!-- b003249 | prose | pages [19] -->
m

<!-- b003250 | prose | pages [19] -->
m

<!-- b003251 | prose | pages [19] -->
m

<!-- b003252 | prose | pages [19] -->
m

<!-- b003253 | prose | pages [19] -->
m

<!-- b003254 | prose | pages [19] -->
m

<!-- b003255 | prose | pages [19] -->
m

<!-- b003256 | prose | pages [19] -->
m

<!-- b003257 | prose | pages [19] -->
m

<!-- b003258 | prose | pages [19] -->
m

<!-- b003259 | prose | pages [19] -->
m

<!-- b003260 | prose | pages [19] -->
m

<!-- b003261 | prose | pages [19] -->
m

<!-- b003262 | prose | pages [19] -->
m

<!-- b003263 | prose | pages [19] -->
m

<!-- b003264 | prose | pages [19] -->
m

<!-- b003265 | prose | pages [19] -->
m

<!-- b003266 | prose | pages [19] -->
m

<!-- b003267 | prose | pages [19] -->
m

<!-- b003268 | prose | pages [19] -->
m

<!-- b003269 | prose | pages [19] -->
m

<!-- b003270 | prose | pages [19] -->
m

<!-- b003271 | prose | pages [19] -->
m

<!-- b003272 | prose | pages [19] -->
m

<!-- b003273 | prose | pages [19] -->
m

<!-- b003274 | prose | pages [19] -->
m

<!-- b003275 | prose | pages [19] -->
m

<!-- b003276 | prose | pages [19] -->
m

<!-- b003277 | prose | pages [19] -->
m

<!-- b003278 | prose | pages [19] -->
m

<!-- b003279 | prose | pages [19] -->
m

<!-- b003280 | prose | pages [19] -->
m

<!-- b003281 | prose | pages [19] -->
m

<!-- b003282 | prose | pages [19] -->
m

<!-- b003283 | prose | pages [19] -->
m

<!-- b003284 | prose | pages [19] -->
m

<!-- b003285 | prose | pages [19] -->
m

<!-- b003286 | prose | pages [19] -->
m

<!-- b003287 | prose | pages [19] -->
m

<!-- b003288 | prose | pages [19] -->
m

<!-- b003289 | prose | pages [19] -->
m

<!-- b003290 | prose | pages [19] -->
m

<!-- b003291 | prose | pages [19] -->
m

<!-- b003292 | prose | pages [19] -->
m

<!-- b003293 | prose | pages [19] -->
m

<!-- b003294 | prose | pages [19] -->
m

<!-- b003295 | prose | pages [19] -->
m

<!-- b003296 | prose | pages [19] -->
m

<!-- b003297 | prose | pages [19] -->
m

<!-- b003298 | prose | pages [19] -->
m

<!-- b003299 | prose | pages [19] -->
m

<!-- b003300 | prose | pages [19] -->
m

<!-- b003301 | prose | pages [19] -->
m

<!-- b003302 | prose | pages [19] -->
m

<!-- b003303 | prose | pages [19] -->
m

<!-- b003304 | prose | pages [19] -->
m

<!-- b003305 | prose | pages [19] -->
m

<!-- b003306 | prose | pages [19] -->
m

<!-- b003307 | prose | pages [19] -->
m

<!-- b003308 | prose | pages [19] -->
m

<!-- b003309 | prose | pages [19] -->
m

<!-- b003310 | prose | pages [19] -->
m

<!-- b003311 | prose | pages [19] -->
m

<!-- b003312 | prose | pages [19] -->
m

<!-- b003313 | prose | pages [19] -->
m

<!-- b003314 | prose | pages [19] -->
m

<!-- b003315 | prose | pages [19] -->
m

<!-- b003316 | prose | pages [19] -->
m

<!-- b003317 | prose | pages [19] -->
m

<!-- b003318 | prose | pages [19] -->
m

<!-- b003319 | prose | pages [19] -->
m

<!-- b003320 | prose | pages [19] -->
m

<!-- b003321 | prose | pages [19] -->
m

<!-- b003322 | prose | pages [19] -->
m

<!-- b003323 | prose | pages [19] -->
m

<!-- b003324 | prose | pages [19] -->
m

<!-- b003325 | prose | pages [19] -->
m

<!-- b003326 | prose | pages [19] -->
m

<!-- b003327 | prose | pages [19] -->
m

<!-- b003328 | prose | pages [19] -->
m

<!-- b003329 | prose | pages [19] -->
m

<!-- b003330 | prose | pages [19] -->
m

<!-- b003331 | prose | pages [19] -->
m

<!-- b003332 | prose | pages [19] -->
m

<!-- b003333 | prose | pages [19] -->
m

<!-- b003334 | prose | pages [19] -->
m

<!-- b003335 | prose | pages [19] -->
m

<!-- b003336 | prose | pages [19] -->
m

<!-- b003337 | prose | pages [19] -->
m

<!-- b003338 | prose | pages [19] -->
m

<!-- b003339 | prose | pages [19] -->
m

<!-- b003340 | prose | pages [19] -->
m

<!-- b003341 | prose | pages [19] -->
m

<!-- b003342 | prose | pages [19] -->
m

<!-- b003343 | prose | pages [19] -->
m

<!-- b003344 | prose | pages [19] -->
m

<!-- b003345 | prose | pages [19] -->
m

<!-- b003346 | prose | pages [19] -->
m

<!-- b003347 | prose | pages [19] -->
m

<!-- b003348 | prose | pages [19] -->
m

<!-- b003349 | prose | pages [19] -->
m

<!-- b003350 | prose | pages [19] -->
m

<!-- b003351 | prose | pages [19] -->
m

<!-- b003352 | prose | pages [19] -->
m

<!-- b003353 | prose | pages [19] -->
m

<!-- b003354 | prose | pages [19] -->
m

<!-- b003355 | prose | pages [19] -->
m

<!-- b003356 | prose | pages [19] -->
m

<!-- b003357 | prose | pages [19] -->
m

<!-- b003358 | prose | pages [19] -->
m

<!-- b003359 | prose | pages [19] -->
m

<!-- b003360 | prose | pages [19] -->
m

<!-- b003361 | prose | pages [19] -->
m

<!-- b003362 | prose | pages [19] -->
m

<!-- b003363 | prose | pages [19] -->
m

<!-- b003364 | prose | pages [19] -->
m

<!-- b003365 | prose | pages [19] -->
m

<!-- b003366 | prose | pages [19] -->
m

<!-- b003367 | prose | pages [19] -->
m

<!-- b003368 | prose | pages [19] -->
m

<!-- b003369 | prose | pages [19] -->
m

<!-- b003370 | prose | pages [19] -->
m

<!-- b003371 | prose | pages [19] -->
m

<!-- b003372 | prose | pages [19] -->
m

<!-- b003373 | prose | pages [19] -->
m

<!-- b003374 | prose | pages [19] -->
m

<!-- b003375 | prose | pages [19] -->
m

<!-- b003376 | prose | pages [19] -->
m

<!-- b003377 | prose | pages [19] -->
m

<!-- b003378 | prose | pages [19] -->
m

<!-- b003379 | prose | pages [19] -->
m

<!-- b003380 | prose | pages [19] -->
m

<!-- b003381 | prose | pages [19] -->
m

<!-- b003382 | prose | pages [19] -->
m

<!-- b003383 | prose | pages [19] -->
m

<!-- b003384 | prose | pages [19] -->
m

<!-- b003385 | prose | pages [19] -->
m

<!-- b003386 | prose | pages [19] -->
m

<!-- b003387 | prose | pages [19] -->
m

<!-- b003388 | prose | pages [19] -->
m

<!-- b003389 | prose | pages [19] -->
m

<!-- b003390 | prose | pages [19] -->
m

<!-- b003391 | prose | pages [19] -->
m

<!-- b003392 | prose | pages [19] -->
m

<!-- b003393 | prose | pages [19] -->
m

<!-- b003394 | prose | pages [19] -->
m

<!-- b003395 | prose | pages [19] -->
m

<!-- b003396 | prose | pages [19] -->
m

<!-- b003397 | prose | pages [19] -->
m

<!-- b003398 | prose | pages [19] -->
m

<!-- b003399 | prose | pages [19] -->
m

<!-- b003400 | prose | pages [19] -->
m

<!-- b003401 | prose | pages [19] -->
m

<!-- b003402 | prose | pages [19] -->
m

<!-- b003403 | prose | pages [19] -->
m

<!-- b003404 | prose | pages [19] -->
m

<!-- b003405 | prose | pages [19] -->
m

<!-- b003406 | prose | pages [19] -->
m

<!-- b003407 | prose | pages [19] -->
m

<!-- b003408 | prose | pages [19] -->
m

<!-- b003409 | prose | pages [19] -->
m

<!-- b003410 | prose | pages [19] -->
m

<!-- b003411 | prose | pages [19] -->
m

<!-- b003412 | prose | pages [19] -->
m

<!-- b003413 | prose | pages [19] -->
m

<!-- b003414 | prose | pages [19] -->
m

<!-- b003415 | prose | pages [19] -->
m

<!-- b003416 | prose | pages [19] -->
m

<!-- b003417 | prose | pages [19] -->
m

<!-- b003418 | prose | pages [19] -->
m

<!-- b003419 | prose | pages [19] -->
m

<!-- b003420 | prose | pages [19] -->
m

<!-- b003421 | prose | pages [19] -->
m

<!-- b003422 | prose | pages [19] -->
m

<!-- b003423 | prose | pages [19] -->
m

<!-- b003424 | prose | pages [19] -->
m

<!-- b003425 | prose | pages [19] -->
m

<!-- b003426 | prose | pages [19] -->
m

<!-- b003427 | prose | pages [19] -->
m

<!-- b003428 | prose | pages [19] -->
m

<!-- b003429 | prose | pages [19] -->
m

<!-- b003430 | prose | pages [19] -->
m

<!-- b003431 | prose | pages [19] -->
m

<!-- b003432 | prose | pages [19] -->
m

<!-- b003433 | prose | pages [19] -->
m

<!-- b003434 | prose | pages [19] -->
m

<!-- b003435 | prose | pages [19] -->
m

<!-- b003436 | prose | pages [19] -->
m

<!-- b003437 | prose | pages [19] -->
m

<!-- b003438 | prose | pages [19] -->
m

<!-- b003439 | prose | pages [19] -->
m

<!-- b003440 | prose | pages [19] -->
m

<!-- b003441 | prose | pages [19] -->
m

<!-- b003442 | prose | pages [19] -->
m

<!-- b003443 | prose | pages [19] -->
m

<!-- b003444 | prose | pages [19] -->
m

<!-- b003445 | prose | pages [19] -->
m

<!-- b003446 | prose | pages [19] -->
m

<!-- b003447 | prose | pages [19] -->
m

<!-- b003448 | prose | pages [19] -->
m

<!-- b003449 | prose | pages [19] -->
m

<!-- b003450 | prose | pages [19] -->
m

<!-- b003451 | prose | pages [19] -->
m

<!-- b003452 | prose | pages [19] -->
m

<!-- b003453 | prose | pages [19] -->
m

<!-- b003454 | prose | pages [19] -->
m

<!-- b003455 | prose | pages [19] -->
m

<!-- b003456 | prose | pages [19] -->
m

<!-- b003457 | prose | pages [19] -->
m

<!-- b003458 | prose | pages [19] -->
m

<!-- b003459 | prose | pages [19] -->
m

<!-- b003460 | prose | pages [19] -->
m

<!-- b003461 | prose | pages [19] -->
m

<!-- b003462 | prose | pages [19] -->
m

<!-- b003463 | prose | pages [19] -->
m

<!-- b003464 | prose | pages [19] -->
m

<!-- b003465 | prose | pages [19] -->
m

<!-- b003466 | prose | pages [19] -->
m

<!-- b003467 | prose | pages [19] -->
m

<!-- b003468 | prose | pages [19] -->
m

<!-- b003469 | prose | pages [19] -->
m

<!-- b003470 | prose | pages [19] -->
m

<!-- b003471 | prose | pages [19] -->
m

<!-- b003472 | furniture | pages [19] -->
m

<!-- b003473 | furniture | pages [19] -->
m

<!-- b003474 | furniture | pages [19] -->
m

<!-- b003475 | furniture | pages [19] -->
m

<!-- b003476 | furniture | pages [19] -->
m

<!-- b003477 | furniture | pages [19] -->
m

<!-- b003478 | furniture | pages [19] -->
m

<!-- b003479 | furniture | pages [19] -->
m

<!-- b003480 | furniture | pages [19] -->
m

<!-- b003481 | furniture | pages [19] -->
m

<!-- b003482 | furniture | pages [19] -->
m

<!-- b003483 | furniture | pages [19] -->
m

<!-- b003484 | furniture | pages [19] -->
m

<!-- b003485 | furniture | pages [19] -->
m

<!-- b003486 | furniture | pages [19] -->
m

<!-- b003487 | furniture | pages [19] -->
m

<!-- b003488 | furniture | pages [19] -->
m

<!-- b003489 | furniture | pages [19] -->
m

<!-- b003490 | furniture | pages [19] -->
m

<!-- b003491 | furniture | pages [19] -->
m

<!-- b003492 | furniture | pages [19] -->
m

<!-- b003493 | furniture | pages [19] -->
m

<!-- b003494 | furniture | pages [19] -->
m

<!-- b003495 | furniture | pages [19] -->
m

<!-- b003496 | furniture | pages [19] -->
m

<!-- b003497 | furniture | pages [19] -->
m

<!-- b003498 | furniture | pages [19] -->
m

<!-- b003499 | furniture | pages [19] -->
m

<!-- b003500 | furniture | pages [19] -->
m

<!-- b003501 | furniture | pages [19] -->
m

<!-- b003502 | furniture | pages [19] -->
m

<!-- b003503 | furniture | pages [19] -->
m

<!-- b003504 | furniture | pages [19] -->
m

<!-- b003505 | furniture | pages [19] -->
m

<!-- b003506 | furniture | pages [19] -->
m

<!-- b003507 | furniture | pages [19] -->
m

<!-- b003508 | furniture | pages [19] -->
m

<!-- b003509 | furniture | pages [19] -->
m

<!-- b003510 | furniture | pages [19] -->
m

<!-- b003511 | furniture | pages [19] -->
m

<!-- b003512 | furniture | pages [19] -->
m

<!-- b003513 | furniture | pages [19] -->
m

<!-- b003514 | furniture | pages [19] -->
m

<!-- b003515 | furniture | pages [19] -->
m

<!-- b003516 | furniture | pages [19] -->
m

<!-- b003517 | furniture | pages [19] -->
m

<!-- b003518 | furniture | pages [19] -->
m

<!-- b003519 | furniture | pages [19] -->
m

<!-- b003520 | furniture | pages [19] -->
m

<!-- b003521 | furniture | pages [19] -->
m

<!-- b003522 | furniture | pages [19] -->
m

<!-- b003523 | furniture | pages [19] -->
m

<!-- b003524 | furniture | pages [19] -->
m

<!-- b003525 | furniture | pages [19] -->
m

<!-- b003526 | furniture | pages [19] -->
m

<!-- b003527 | furniture | pages [19] -->
m

<!-- b003528 | furniture | pages [19] -->
m

<!-- b003529 | furniture | pages [19] -->
m

<!-- b003530 | furniture | pages [19] -->
m

<!-- b003531 | furniture | pages [19] -->
m

<!-- b003532 | furniture | pages [19] -->
m

<!-- b003533 | furniture | pages [19] -->
m

<!-- b003534 | furniture | pages [19] -->
m

<!-- b003535 | furniture | pages [19] -->
m

<!-- b003536 | furniture | pages [19] -->
m

<!-- b003537 | furniture | pages [19] -->
m

<!-- b003538 | furniture | pages [19] -->
m

<!-- b003539 | furniture | pages [19] -->
m

<!-- b003540 | furniture | pages [19] -->
m

<!-- b003541 | furniture | pages [19] -->
m

<!-- b003542 | furniture | pages [19] -->
m

<!-- b003543 | furniture | pages [19] -->
m

<!-- b003544 | furniture | pages [19] -->
m

<!-- b003545 | furniture | pages [19] -->
m

<!-- b003546 | furniture | pages [19] -->
m

<!-- b003547 | furniture | pages [19] -->
m

<!-- b003548 | furniture | pages [19] -->
m

<!-- b003549 | furniture | pages [19] -->
m

<!-- b003550 | furniture | pages [19] -->
m

<!-- b003551 | furniture | pages [19] -->
m

<!-- b003552 | furniture | pages [19] -->
m

<!-- b003553 | furniture | pages [19] -->
m

<!-- b003554 | furniture | pages [19] -->
m

<!-- b003555 | furniture | pages [19] -->
m

<!-- b003556 | furniture | pages [19] -->
m

<!-- b003557 | furniture | pages [19] -->
m

<!-- b003558 | furniture | pages [19] -->
m

<!-- b003559 | furniture | pages [19] -->
m

<!-- b003560 | furniture | pages [19] -->
m

<!-- b003561 | furniture | pages [19] -->
m

<!-- b003562 | furniture | pages [19] -->
m

<!-- b003563 | furniture | pages [19] -->
m

<!-- b003564 | furniture | pages [19] -->
m

<!-- b003565 | furniture | pages [19] -->
m

<!-- b003566 | furniture | pages [19] -->
m

<!-- b003567 | furniture | pages [19] -->
m

<!-- b003568 | furniture | pages [19] -->
m

<!-- b003569 | furniture | pages [19] -->
m

<!-- b003570 | furniture | pages [19] -->
m

<!-- b003571 | furniture | pages [19] -->
m

<!-- b003572 | furniture | pages [19] -->
m

<!-- b003573 | furniture | pages [19] -->
m

<!-- b003574 | furniture | pages [19] -->
m

<!-- b003575 | furniture | pages [19] -->
m

<!-- b003576 | furniture | pages [19] -->
m

<!-- b003577 | furniture | pages [19] -->
m

<!-- b003578 | furniture | pages [19] -->
m

<!-- b003579 | furniture | pages [19] -->
m

<!-- b003580 | furniture | pages [19] -->
m

<!-- b003581 | furniture | pages [19] -->
m

<!-- b003582 | furniture | pages [19] -->
m

<!-- b003583 | furniture | pages [19] -->
m

<!-- b003584 | furniture | pages [19] -->
m

<!-- b003585 | furniture | pages [19] -->
m

<!-- b003586 | furniture | pages [19] -->
m

<!-- b003587 | furniture | pages [19] -->
m

<!-- b003588 | furniture | pages [19] -->
m

<!-- b003589 | furniture | pages [19] -->
m

<!-- b003590 | furniture | pages [19] -->
m

<!-- b003591 | furniture | pages [19] -->
m

<!-- b003592 | furniture | pages [19] -->
m

<!-- b003593 | furniture | pages [19] -->
m

<!-- b003594 | furniture | pages [19] -->
m

<!-- b003595 | furniture | pages [19] -->
m

<!-- b003596 | furniture | pages [19] -->
m

<!-- b003597 | furniture | pages [19] -->
m

<!-- b003598 | furniture | pages [19] -->
m

<!-- b003599 | furniture | pages [19] -->
m

<!-- b003600 | furniture | pages [19] -->
m

<!-- b003601 | furniture | pages [19] -->
m

<!-- b003602 | furniture | pages [19] -->
m

<!-- b003603 | furniture | pages [19] -->
m

<!-- b003604 | furniture | pages [19] -->
m

<!-- b003605 | furniture | pages [19] -->
m

<!-- b003606 | furniture | pages [19] -->
m

<!-- b003607 | furniture | pages [19] -->
m

<!-- b003608 | furniture | pages [19] -->
m

<!-- b003609 | furniture | pages [19] -->
m

<!-- b003610 | furniture | pages [19] -->
m

<!-- b003611 | furniture | pages [19] -->
m

<!-- b003612 | furniture | pages [19] -->
m

<!-- b003613 | furniture | pages [19] -->
m

<!-- b003614 | furniture | pages [19] -->
m

<!-- b003615 | furniture | pages [19] -->
m

<!-- b003616 | furniture | pages [19] -->
m

<!-- b003617 | furniture | pages [19] -->
m

<!-- b003618 | furniture | pages [19] -->
m

<!-- b003619 | furniture | pages [19] -->
m

<!-- b003620 | furniture | pages [19] -->
m

<!-- b003621 | furniture | pages [19] -->
m

<!-- b003622 | furniture | pages [19] -->
m

<!-- b003623 | furniture | pages [19] -->
m

<!-- b003624 | furniture | pages [19] -->
m

<!-- b003625 | furniture | pages [19] -->
m

<!-- b003626 | furniture | pages [19] -->
m

<!-- b003627 | furniture | pages [19] -->
m

<!-- b003628 | furniture | pages [19] -->
m

<!-- b003629 | furniture | pages [19] -->
m

<!-- b003630 | furniture | pages [19] -->
m

<!-- b003631 | furniture | pages [19] -->
m

<!-- b003632 | furniture | pages [19] -->
m

<!-- b003633 | furniture | pages [19] -->
m

<!-- b003634 | furniture | pages [19] -->
m

<!-- b003635 | furniture | pages [19] -->
m

<!-- b003636 | furniture | pages [19] -->
m

<!-- b003637 | furniture | pages [19] -->
m

<!-- b003638 | furniture | pages [19] -->
m

<!-- b003639 | furniture | pages [19] -->
m

<!-- b003640 | furniture | pages [19] -->
m

<!-- b003641 | furniture | pages [19] -->
m

<!-- b003642 | furniture | pages [19] -->
m

<!-- b003643 | furniture | pages [19] -->
m

<!-- b003644 | furniture | pages [19] -->
m

<!-- b003645 | furniture | pages [19] -->
m

<!-- b003646 | furniture | pages [19] -->
m

<!-- b003647 | furniture | pages [19] -->
m

<!-- b003648 | furniture | pages [19] -->
m

<!-- b003649 | furniture | pages [19] -->
m

<!-- b003650 | furniture | pages [19] -->
m

<!-- b003651 | furniture | pages [19] -->
m

<!-- b003652 | furniture | pages [19] -->
m

<!-- b003653 | furniture | pages [19] -->
m

<!-- b003654 | furniture | pages [19] -->
m

<!-- b003655 | furniture | pages [19] -->
m

<!-- b003656 | furniture | pages [19] -->
m

<!-- b003657 | furniture | pages [19] -->
m

<!-- b003658 | furniture | pages [19] -->
m

<!-- b003659 | furniture | pages [19] -->
m

<!-- b003660 | furniture | pages [19] -->
m

<!-- b003661 | furniture | pages [19] -->
m

<!-- b003662 | furniture | pages [19] -->
m

<!-- b003663 | furniture | pages [19] -->
m

<!-- b003664 | furniture | pages [19] -->
m

<!-- b003665 | furniture | pages [19] -->
m

<!-- b003666 | furniture | pages [19] -->
m

<!-- b003667 | furniture | pages [19] -->
m

<!-- b003668 | furniture | pages [19] -->
m

<!-- b003669 | furniture | pages [19] -->
m

<!-- b003670 | furniture | pages [19] -->
m

<!-- b003671 | furniture | pages [19] -->
m

<!-- b003672 | furniture | pages [19] -->
m

<!-- b003673 | furniture | pages [19] -->
m

<!-- b003674 | furniture | pages [19] -->
m

<!-- b003675 | furniture | pages [19] -->
m

<!-- b003676 | furniture | pages [19] -->
m

<!-- b003677 | furniture | pages [19] -->
m

<!-- b003678 | furniture | pages [19] -->
m

<!-- b003679 | furniture | pages [19] -->
m

<!-- b003680 | furniture | pages [19] -->
m

<!-- b003681 | furniture | pages [19] -->
m

<!-- b003682 | furniture | pages [19] -->
m

<!-- b003683 | furniture | pages [19] -->
m

<!-- b003684 | furniture | pages [19] -->
m

<!-- b003685 | furniture | pages [19] -->
m

<!-- b003686 | furniture | pages [19] -->
m

<!-- b003687 | furniture | pages [19] -->
m

<!-- b003688 | furniture | pages [19] -->
m

<!-- b003689 | furniture | pages [19] -->
m

<!-- b003690 | furniture | pages [19] -->
m

<!-- b003691 | furniture | pages [19] -->
m

<!-- b003692 | furniture | pages [19] -->
m

<!-- b003693 | furniture | pages [19] -->
m

<!-- b003694 | furniture | pages [19] -->
m

<!-- b003695 | furniture | pages [19] -->
m

<!-- b003696 | furniture | pages [19] -->
m

<!-- b003697 | furniture | pages [19] -->
m

<!-- b003698 | furniture | pages [19] -->
m

<!-- b003699 | furniture | pages [19] -->
m

<!-- b003700 | furniture | pages [19] -->
m

<!-- b003701 | furniture | pages [19] -->
m

<!-- b003702 | furniture | pages [19] -->
m

<!-- b003703 | furniture | pages [19] -->
m

<!-- b003704 | furniture | pages [19] -->
m

<!-- b003705 | furniture | pages [19] -->
m

<!-- b003706 | furniture | pages [19] -->
m

<!-- b003707 | furniture | pages [19] -->
m

<!-- b003708 | furniture | pages [19] -->
m

<!-- b003709 | furniture | pages [19] -->
m

<!-- b003710 | furniture | pages [19] -->
m

<!-- b003711 | furniture | pages [19] -->
m

<!-- b003712 | furniture | pages [19] -->
m

<!-- b003713 | furniture | pages [19] -->
m

<!-- b003714 | furniture | pages [19] -->
m

<!-- b003715 | furniture | pages [19] -->
m

<!-- b003716 | furniture | pages [19] -->
m

<!-- b003717 | furniture | pages [19] -->
m

<!-- b003718 | furniture | pages [19] -->
m

<!-- b003719 | furniture | pages [19] -->
m

<!-- b003720 | furniture | pages [19] -->
m

<!-- b003721 | furniture | pages [19] -->
m

<!-- b003722 | furniture | pages [19] -->
m

<!-- b003723 | furniture | pages [19] -->
m

<!-- b003724 | furniture | pages [19] -->
m

<!-- b003725 | furniture | pages [19] -->
m

<!-- b003726 | furniture | pages [19] -->
m

<!-- b003727 | furniture | pages [19] -->
m

<!-- b003728 | furniture | pages [19] -->
m

<!-- b003729 | furniture | pages [19] -->
m

<!-- b003730 | furniture | pages [19] -->
m

<!-- b003731 | furniture | pages [19] -->
m

<!-- b003732 | furniture | pages [19] -->
m

<!-- b003733 | furniture | pages [19] -->
m

<!-- b003734 | furniture | pages [19] -->
m

<!-- b003735 | furniture | pages [19] -->
m

<!-- b003736 | furniture | pages [19] -->
m

<!-- b003737 | furniture | pages [19] -->
m

<!-- b003738 | furniture | pages [19] -->
m

<!-- b003739 | furniture | pages [19] -->
m

<!-- b003740 | furniture | pages [19] -->
m

<!-- b003741 | furniture | pages [19] -->
m

<!-- b003742 | furniture | pages [19] -->
m

<!-- b003743 | furniture | pages [19] -->
m

<!-- b003744 | furniture | pages [19] -->
m

<!-- b003745 | furniture | pages [19] -->
m

<!-- b003746 | furniture | pages [19] -->
m

<!-- b003747 | furniture | pages [19] -->
m

<!-- b003748 | furniture | pages [19] -->
m

<!-- b003749 | furniture | pages [19] -->
m

<!-- b003750 | furniture | pages [19] -->
m

<!-- b003751 | furniture | pages [19] -->
m

<!-- b003752 | furniture | pages [19] -->
m

<!-- b003753 | furniture | pages [19] -->
m

<!-- b003754 | furniture | pages [19] -->
m

<!-- b003755 | furniture | pages [19] -->
m

<!-- b003756 | furniture | pages [19] -->
m

<!-- b003757 | furniture | pages [19] -->
m

<!-- b003758 | furniture | pages [19] -->
m

<!-- b003759 | furniture | pages [19] -->
m

<!-- b003760 | furniture | pages [19] -->
m

<!-- b003761 | furniture | pages [19] -->
m

<!-- b003762 | furniture | pages [19] -->
m

<!-- b003763 | furniture | pages [19] -->
m

<!-- b003764 | furniture | pages [19] -->
m

<!-- b003765 | furniture | pages [19] -->
m

<!-- b003766 | furniture | pages [19] -->
m

<!-- b003767 | furniture | pages [19] -->
m

<!-- b003768 | furniture | pages [19] -->
m

<!-- b003769 | furniture | pages [19] -->
m

<!-- b003770 | furniture | pages [19] -->
m

<!-- b003771 | furniture | pages [19] -->
m

<!-- b003772 | furniture | pages [19] -->
m

<!-- b003773 | furniture | pages [19] -->
m

<!-- b003774 | furniture | pages [19] -->
m

<!-- b003775 | furniture | pages [19] -->
m

<!-- b003776 | furniture | pages [19] -->
m

<!-- b003777 | furniture | pages [19] -->
m

<!-- b003778 | furniture | pages [19] -->
m

<!-- b003779 | furniture | pages [19] -->
m

<!-- b003780 | furniture | pages [19] -->
m

<!-- b003781 | furniture | pages [19] -->
m

<!-- b003782 | furniture | pages [19] -->
m

<!-- b003783 | furniture | pages [19] -->
m

<!-- b003784 | furniture | pages [19] -->
m

<!-- b003785 | furniture | pages [19] -->
m

<!-- b003786 | furniture | pages [19] -->
m

<!-- b003787 | furniture | pages [19] -->
m

<!-- b003788 | furniture | pages [19] -->
m

<!-- b003789 | furniture | pages [19] -->
m

<!-- b003790 | furniture | pages [19] -->
m

<!-- b003791 | furniture | pages [19] -->
m

<!-- b003792 | furniture | pages [19] -->
m

<!-- b003793 | furniture | pages [19] -->
m

<!-- b003794 | furniture | pages [19] -->
m

<!-- b003795 | furniture | pages [19] -->
m

<!-- b003796 | furniture | pages [19] -->
m

<!-- b003797 | furniture | pages [19] -->
m

<!-- b003798 | furniture | pages [19] -->
m

<!-- b003799 | furniture | pages [19] -->
m

<!-- b003800 | furniture | pages [19] -->
m

<!-- b003801 | furniture | pages [19] -->
m

<!-- b003802 | furniture | pages [19] -->
m

<!-- b003803 | furniture | pages [19] -->
m

<!-- b003804 | furniture | pages [19] -->
m

<!-- b003805 | furniture | pages [19] -->
m

<!-- b003806 | furniture | pages [19] -->
m

<!-- b003807 | furniture | pages [19] -->
m

<!-- b003808 | furniture | pages [19] -->
m

<!-- b003809 | furniture | pages [19] -->
m

<!-- b003810 | furniture | pages [19] -->
m

<!-- b003811 | furniture | pages [19] -->
m

<!-- b003812 | furniture | pages [19] -->
m

<!-- b003813 | furniture | pages [19] -->
m

<!-- b003814 | furniture | pages [19] -->
m

<!-- b003815 | furniture | pages [19] -->
m

<!-- b003816 | furniture | pages [19] -->
m

<!-- b003817 | furniture | pages [19] -->
m

<!-- b003818 | furniture | pages [19] -->
m

<!-- b003819 | furniture | pages [19] -->
m

<!-- b003820 | furniture | pages [19] -->
m

<!-- b003821 | furniture | pages [19] -->
m

<!-- b003822 | furniture | pages [19] -->
m

<!-- b003823 | furniture | pages [19] -->
m

<!-- b003824 | furniture | pages [19] -->
m

<!-- b003825 | furniture | pages [19] -->
m

<!-- b003826 | furniture | pages [19] -->
m

<!-- b003827 | furniture | pages [19] -->
m

<!-- b003828 | furniture | pages [19] -->
m

<!-- b003829 | furniture | pages [19] -->
m

<!-- b003830 | furniture | pages [19] -->
m

<!-- b003831 | furniture | pages [19] -->
m

<!-- b003832 | furniture | pages [19] -->
m

<!-- b003833 | furniture | pages [19] -->
m

<!-- b003834 | furniture | pages [19] -->
m

<!-- b003835 | furniture | pages [19] -->
m

<!-- b003836 | furniture | pages [19] -->
m

<!-- b003837 | furniture | pages [19] -->
m

<!-- b003838 | furniture | pages [19] -->
m

<!-- b003839 | furniture | pages [19] -->
m

<!-- b003840 | furniture | pages [19] -->
m

<!-- b003841 | furniture | pages [19] -->
m

<!-- b003842 | furniture | pages [19] -->
m

<!-- b003843 | furniture | pages [19] -->
m

<!-- b003844 | furniture | pages [19] -->
m

<!-- b003845 | furniture | pages [19] -->
m

<!-- b003846 | furniture | pages [19] -->
m

<!-- b003847 | furniture | pages [19] -->
m

<!-- b003848 | furniture | pages [19] -->
m

<!-- b003849 | furniture | pages [19] -->
m

<!-- b003850 | furniture | pages [19] -->
m

<!-- b003851 | furniture | pages [19] -->
m

<!-- b003852 | furniture | pages [19] -->
m

<!-- b003853 | furniture | pages [19] -->
m

<!-- b003854 | furniture | pages [19] -->
m

<!-- b003855 | furniture | pages [19] -->
m

<!-- b003856 | furniture | pages [19] -->
m

<!-- b003857 | furniture | pages [19] -->
m

<!-- b003858 | furniture | pages [19] -->
m

<!-- b003859 | furniture | pages [19] -->
m

<!-- b003860 | furniture | pages [19] -->
m

<!-- b003861 | furniture | pages [19] -->
m

<!-- b003862 | furniture | pages [19] -->
m

<!-- b003863 | furniture | pages [19] -->
m

<!-- b003864 | furniture | pages [19] -->
m

<!-- b003865 | furniture | pages [19] -->
m

<!-- b003866 | furniture | pages [19] -->
m

<!-- b003867 | furniture | pages [19] -->
m

<!-- b003868 | furniture | pages [19] -->
m

<!-- b003869 | furniture | pages [19] -->
m

<!-- b003870 | furniture | pages [19] -->
m

<!-- b003871 | furniture | pages [19] -->
m

<!-- b003872 | furniture | pages [19] -->
m

<!-- b003873 | furniture | pages [19] -->
m

<!-- b003874 | furniture | pages [19] -->
m

<!-- b003875 | furniture | pages [20] -->
Team 2522820

<!-- b003876 | furniture | pages [20] -->
Page 20

<!-- b003877 | prose | pages [20] -->
2. When the difference in points between performances at consecutive games is at least 2s, call these positive change points.

<!-- b003878 | prose | pages [20] -->
3. When the difference in points between consecutive games is less than or equal to −3s, call these negative change points.

<!-- b003879 | prose | pages [20] -->
4. Let segments be the years between positive and negative change points.

<!-- b003880 | prose | pages [20] -->
5. If a positive change point is followed by another positive change point before a negative change point appears, combine the segments.

<!-- b003881 | prose | pages [20] -->
6. For each segment, calculate the z-score of x compared to the population distribution of points: x−µ σ .

<!-- b003882 | prose | pages [20] -->
7. Choose segments with x that have z-scores greater than or equal to 1.5—these indicate the great coach effect.

<!-- b003883 | prose | pages [20] -->
8. For each of these chosen segments, calculate the coefficient of variation: s

<!-- b003884 | prose | pages [20] -->
4.1.3

<!-- b003885 | heading | pages [20] -->
Results and Notable Findings

<!-- b003886 | prose | pages [20] -->
x.

<!-- b003887 | prose | pages [20] -->
It was impractical to apply this analysis to all pairs of countries and sports, so we chose the 20 countries with the highest points over the history of the Games. Though many great coaches have coached teams outside of these top 20 countries, it is reasonable to assume that many of these top-performing countries have achieved such success at least partly due to the great coach effect, making it more likely that our model detects instances of the effect for these countries’ performances.

<!-- b003888 | prose | pages [20] -->
The table below shows the top 10 segments, ranked by order of decreasing z-score.

<!-- b003889 | caption | pages [20] -->
Table 16: Analysis of Significant Performance Changes in Olympic Sports

<!-- b003890 | prose | pages [20] -->
Coefficient Year Z-Score Country (Sport)

<!-- b003891 | prose | pages [20] -->
of Variation Start End

<!-- b003892 | prose | pages [20] -->
0.222 1972 1976 2.497 Romania (Handball) 0.286 2004 2008 2.284 Canada (Trampolining) 0.353 1996 2000 2.264 Russia (Diving) 0.622 2004 2008 2.207 China (Trampolining) 0.667 2000 2004 2.167 Russia (Basketball) 0.374 2000 2004 2.146 Russia (Weightlifting) 0.547 1984 2004 2.143 South Korea (Handball) 0.286 1996 2016 2.100 Russia (Modern Pentathlon) 0.766 1908 1912 2.076 Netherlands (Fencing) 0.182 1996 2000 2.070 Australia (Basketball)

<!-- b003893 | prose | pages [20] -->
Here, the start year is the year before the potential great coach effect, and the end year is the last year of the potential great coach effect. Matching with known information about coaches, many of these results line up with the leadership of coaches who may be considered “great”: the 1976 Romanian handball team was coached by Radu Voina, who won the world championship and three Olympic medals himself;[3] the 2008 Canadian trampolining team was coached by David Ross, whose club athletes have won seven Olympic medals;[4] and so on. Many of these coaches had very successful coaching careers and may be considered particularly great coaches, even among the exceedingly high standards that Olympic coaches are held to.

<!-- b003894 | prose | pages [20] -->
Most of these great coach effects last only for one Games, but this makes sense when considering the fact that it is common for coaches to switch teams: in a particularly notable case, Lang Ping, the “great” volleyball

<!-- b003895 | prose | pages [20] -->
关注数学模型

<!-- b003896 | furniture | pages [20] -->
2

<!-- b003897 | furniture | pages [20] -->
MATHmodels

<!-- b003898 | furniture | pages [20] -->
获取更多资讯

<!-- b003899 | furniture | pages [21] -->
Team 2522820

<!-- b003900 | furniture | pages [21] -->
Page 21

<!-- b003901 | prose | pages [21] -->
coach, coached the Chinese team to silver in 1996, the American team to silver in 2008, and the Chinese team to

<!-- b003902 | prose | pages [21] -->
微信公众号：数学模型

<!-- b003903 | prose | pages [21] -->
gold in 2016.

<!-- b003904 | prose | pages [21] -->
This is why we did not use the coefficient of variation as a variable in determining whether a segment of successful performances was likely to be due to the great coach effect: it would disqualify some segments with high coefficients of variation even though they were no less likely than other segments with lower coefficients of variation to be due to the great coach effect. However, we still included it in the table because it allows for greater interpretability of the data. For instance, we can tell that Australia consistently performed well around 1996 to 2000 because of its relatively low coefficient of variation value of 0.182, even though it did not reach our requirements to extend the segment.

<!-- b003905 | prose | pages [21] -->
4.2 Estimating Impacts of Great Coaches

<!-- b003906 | prose | pages [21] -->
微信号：MATHmodels

<!-- b003907 | prose | pages [21] -->
Our model from 4.1 gave us many valuable insights that can be used not only to find potential instances of the great coach effect but also to estimate the impacts of these great coaches. For each of the top 20 country-sport pairs we found with the highest z-scores, we calculated C:

<!-- b003908 | prose | pages [21] -->
C = (Ps −µ · L) · 100%.

<!-- b003909 | prose | pages [21] -->
This is the percentage of points that can be assumed to be due to the great coach effect out of the country’s historical point count for that sport.

<!-- b003910 | caption | pages [21] -->
Table 17: Top 10 Countries with Highest Contributions in Olympic Sports

<!-- b003911 | prose | pages [21] -->
Year Contribution (%)

<!-- b003912 | prose | pages [21] -->
Start End

<!-- b003913 | prose | pages [21] -->
1988 2012 100.0 1980 2004 100.0 1996 2016 88.9 1984 2004 80.8 1968 1988 59.6 1904 1908 55.0 1924 1928 50.0 1908 1912 40.0 2004 2008 38.9 1972 1976 33.3

<!-- b003914 | prose | pages [21] -->
Country (Sport)

<!-- b003915 | prose | pages [21] -->
Sweden (Handball) United States (Synchronized Swimming) Russia (Modern Pentathlon) South Korea (Handball) Hungary (Weightlifting) Great Britain (Tug-Of-War) Germany (Water Polo) Netherlands (Fencing) China (Trampolining) Romania (Handball)

<!-- b003916 | prose | pages [21] -->
Based on this table, we can see that the dominance of the United States’ synchronized swimming teams from 1984 to 2004 and of Sweden’s handball teams from 1992 to 2012 accounted for 100% of their points over their entire history competing at the Games for those sports. Indeed, great coaches had a hand in these dominant runs: Gail Emery—whose athletes won 14 gold and silver medals in the Olympics and 23 gold and silver medals in World Championships[5]—coached the United States synchronized swimming team from 1988 to 1996, and Bengt Johansson coached the Swedish handball team from 1988 to 2004. In fact, Johansson’s coaching ability was so influential that, under his leadership, the Swedish handball team were known as the Bengan Boys, after his first name.[6]

<!-- b003917 | prose | pages [21] -->
Another notable detail is that, as soon as these great coaches left their positions, their teams experienced a negative change point, immediately ending their segments of increased performance. This suggests that the influence of coaches may only last during their direct involvement and that great coaches have limited influence in improving their teams to the extent that they continue to improve even after the coaches have left.

<!-- b003918 | prose | pages [21] -->
m

<!-- b003919 | prose | pages [21] -->
m

<!-- b003920 | prose | pages [21] -->
m

<!-- b003921 | prose | pages [21] -->
m

<!-- b003922 | prose | pages [21] -->
m

<!-- b003923 | prose | pages [21] -->
m

<!-- b003924 | prose | pages [21] -->
m

<!-- b003925 | prose | pages [21] -->
m

<!-- b003926 | prose | pages [21] -->
m

<!-- b003927 | prose | pages [21] -->
m

<!-- b003928 | prose | pages [21] -->
m

<!-- b003929 | prose | pages [21] -->
m

<!-- b003930 | prose | pages [21] -->
m

<!-- b003931 | prose | pages [21] -->
m

<!-- b003932 | prose | pages [21] -->
m

<!-- b003933 | prose | pages [21] -->
m

<!-- b003934 | prose | pages [21] -->
m

<!-- b003935 | prose | pages [21] -->
m

<!-- b003936 | prose | pages [21] -->
m

<!-- b003937 | prose | pages [21] -->
m

<!-- b003938 | prose | pages [21] -->
m

<!-- b003939 | prose | pages [21] -->
m

<!-- b003940 | prose | pages [21] -->
m

<!-- b003941 | prose | pages [21] -->
m

<!-- b003942 | prose | pages [21] -->
m

<!-- b003943 | prose | pages [21] -->
m

<!-- b003944 | prose | pages [21] -->
m

<!-- b003945 | prose | pages [21] -->
m

<!-- b003946 | prose | pages [21] -->
m

<!-- b003947 | prose | pages [21] -->
m

<!-- b003948 | prose | pages [21] -->
m

<!-- b003949 | prose | pages [21] -->
m

<!-- b003950 | prose | pages [21] -->
m

<!-- b003951 | prose | pages [21] -->
m

<!-- b003952 | prose | pages [21] -->
m

<!-- b003953 | prose | pages [21] -->
m

<!-- b003954 | prose | pages [21] -->
m

<!-- b003955 | prose | pages [21] -->
m

<!-- b003956 | prose | pages [21] -->
m

<!-- b003957 | prose | pages [21] -->
m

<!-- b003958 | prose | pages [21] -->
m

<!-- b003959 | prose | pages [21] -->
m

<!-- b003960 | prose | pages [21] -->
m

<!-- b003961 | prose | pages [21] -->
m

<!-- b003962 | prose | pages [21] -->
m

<!-- b003963 | prose | pages [21] -->
m

<!-- b003964 | prose | pages [21] -->
m

<!-- b003965 | prose | pages [21] -->
m

<!-- b003966 | prose | pages [21] -->
m

<!-- b003967 | prose | pages [21] -->
m

<!-- b003968 | prose | pages [21] -->
m

<!-- b003969 | prose | pages [21] -->
m

<!-- b003970 | prose | pages [21] -->
m

<!-- b003971 | prose | pages [21] -->
m

<!-- b003972 | prose | pages [21] -->
m

<!-- b003973 | prose | pages [21] -->
m

<!-- b003974 | prose | pages [21] -->
m

<!-- b003975 | prose | pages [21] -->
m

<!-- b003976 | prose | pages [21] -->
m

<!-- b003977 | prose | pages [21] -->
m

<!-- b003978 | prose | pages [21] -->
m

<!-- b003979 | prose | pages [21] -->
m

<!-- b003980 | prose | pages [21] -->
m

<!-- b003981 | prose | pages [21] -->
m

<!-- b003982 | prose | pages [21] -->
m

<!-- b003983 | prose | pages [21] -->
m

<!-- b003984 | prose | pages [21] -->
m

<!-- b003985 | prose | pages [21] -->
m

<!-- b003986 | prose | pages [21] -->
m

<!-- b003987 | prose | pages [21] -->
m

<!-- b003988 | prose | pages [21] -->
m

<!-- b003989 | prose | pages [21] -->
m

<!-- b003990 | prose | pages [21] -->
m

<!-- b003991 | prose | pages [21] -->
m

<!-- b003992 | prose | pages [21] -->
m

<!-- b003993 | prose | pages [21] -->
m

<!-- b003994 | prose | pages [21] -->
m

<!-- b003995 | prose | pages [21] -->
m

<!-- b003996 | prose | pages [21] -->
m

<!-- b003997 | prose | pages [21] -->
m

<!-- b003998 | prose | pages [21] -->
m

<!-- b003999 | prose | pages [21] -->
m

<!-- b004000 | prose | pages [21] -->
m

<!-- b004001 | prose | pages [21] -->
m

<!-- b004002 | prose | pages [21] -->
m

<!-- b004003 | prose | pages [21] -->
m

<!-- b004004 | prose | pages [21] -->
m

<!-- b004005 | prose | pages [21] -->
m

<!-- b004006 | prose | pages [21] -->
m

<!-- b004007 | prose | pages [21] -->
m

<!-- b004008 | prose | pages [21] -->
m

<!-- b004009 | prose | pages [21] -->
m

<!-- b004010 | prose | pages [21] -->
m

<!-- b004011 | prose | pages [21] -->
m

<!-- b004012 | prose | pages [21] -->
m

<!-- b004013 | prose | pages [21] -->
m

<!-- b004014 | prose | pages [21] -->
m

<!-- b004015 | prose | pages [21] -->
m

<!-- b004016 | prose | pages [21] -->
m

<!-- b004017 | prose | pages [21] -->
m

<!-- b004018 | prose | pages [21] -->
m

<!-- b004019 | prose | pages [21] -->
m

<!-- b004020 | prose | pages [21] -->
m

<!-- b004021 | prose | pages [21] -->
m

<!-- b004022 | prose | pages [21] -->
m

<!-- b004023 | prose | pages [21] -->
m

<!-- b004024 | prose | pages [21] -->
m

<!-- b004025 | prose | pages [21] -->
m

<!-- b004026 | prose | pages [21] -->
m

<!-- b004027 | prose | pages [21] -->
m

<!-- b004028 | prose | pages [21] -->
m

<!-- b004029 | prose | pages [21] -->
m

<!-- b004030 | prose | pages [21] -->
m

<!-- b004031 | prose | pages [21] -->
m

<!-- b004032 | prose | pages [21] -->
m

<!-- b004033 | prose | pages [21] -->
m

<!-- b004034 | prose | pages [21] -->
m

<!-- b004035 | prose | pages [21] -->
m

<!-- b004036 | prose | pages [21] -->
m

<!-- b004037 | prose | pages [21] -->
m

<!-- b004038 | prose | pages [21] -->
m

<!-- b004039 | prose | pages [21] -->
m

<!-- b004040 | prose | pages [21] -->
m

<!-- b004041 | prose | pages [21] -->
m

<!-- b004042 | prose | pages [21] -->
m

<!-- b004043 | prose | pages [21] -->
m

<!-- b004044 | prose | pages [21] -->
m

<!-- b004045 | prose | pages [21] -->
m

<!-- b004046 | prose | pages [21] -->
m

<!-- b004047 | prose | pages [21] -->
m

<!-- b004048 | prose | pages [21] -->
m

<!-- b004049 | prose | pages [21] -->
m

<!-- b004050 | prose | pages [21] -->
m

<!-- b004051 | prose | pages [21] -->
m

<!-- b004052 | prose | pages [21] -->
m

<!-- b004053 | prose | pages [21] -->
m

<!-- b004054 | prose | pages [21] -->
m

<!-- b004055 | prose | pages [21] -->
m

<!-- b004056 | prose | pages [21] -->
m

<!-- b004057 | prose | pages [21] -->
m

<!-- b004058 | prose | pages [21] -->
m

<!-- b004059 | prose | pages [21] -->
m

<!-- b004060 | prose | pages [21] -->
m

<!-- b004061 | prose | pages [21] -->
m

<!-- b004062 | prose | pages [21] -->
m

<!-- b004063 | prose | pages [21] -->
m

<!-- b004064 | prose | pages [21] -->
m

<!-- b004065 | prose | pages [21] -->
m

<!-- b004066 | prose | pages [21] -->
m

<!-- b004067 | prose | pages [21] -->
m

<!-- b004068 | prose | pages [21] -->
m

<!-- b004069 | prose | pages [21] -->
m

<!-- b004070 | prose | pages [21] -->
m

<!-- b004071 | prose | pages [21] -->
m

<!-- b004072 | prose | pages [21] -->
m

<!-- b004073 | prose | pages [21] -->
m

<!-- b004074 | prose | pages [21] -->
m

<!-- b004075 | prose | pages [21] -->
m

<!-- b004076 | prose | pages [21] -->
m

<!-- b004077 | prose | pages [21] -->
m

<!-- b004078 | prose | pages [21] -->
m

<!-- b004079 | prose | pages [21] -->
m

<!-- b004080 | prose | pages [21] -->
m

<!-- b004081 | prose | pages [21] -->
m

<!-- b004082 | prose | pages [21] -->
m

<!-- b004083 | prose | pages [21] -->
m

<!-- b004084 | prose | pages [21] -->
m

<!-- b004085 | prose | pages [21] -->
m

<!-- b004086 | prose | pages [21] -->
m

<!-- b004087 | prose | pages [21] -->
m

<!-- b004088 | prose | pages [21] -->
m

<!-- b004089 | prose | pages [21] -->
m

<!-- b004090 | prose | pages [21] -->
m

<!-- b004091 | prose | pages [21] -->
m

<!-- b004092 | prose | pages [21] -->
m

<!-- b004093 | prose | pages [21] -->
m

<!-- b004094 | prose | pages [21] -->
m

<!-- b004095 | prose | pages [21] -->
m

<!-- b004096 | prose | pages [21] -->
m

<!-- b004097 | prose | pages [21] -->
m

<!-- b004098 | prose | pages [21] -->
m

<!-- b004099 | prose | pages [21] -->
m

<!-- b004100 | prose | pages [21] -->
m

<!-- b004101 | prose | pages [21] -->
m

<!-- b004102 | prose | pages [21] -->
m

<!-- b004103 | prose | pages [21] -->
m

<!-- b004104 | prose | pages [21] -->
m

<!-- b004105 | prose | pages [21] -->
m

<!-- b004106 | prose | pages [21] -->
m

<!-- b004107 | prose | pages [21] -->
m

<!-- b004108 | prose | pages [21] -->
m

<!-- b004109 | prose | pages [21] -->
m

<!-- b004110 | prose | pages [21] -->
m

<!-- b004111 | prose | pages [21] -->
m

<!-- b004112 | prose | pages [21] -->
m

<!-- b004113 | prose | pages [21] -->
m

<!-- b004114 | prose | pages [21] -->
m

<!-- b004115 | prose | pages [21] -->
m

<!-- b004116 | prose | pages [21] -->
m

<!-- b004117 | prose | pages [21] -->
m

<!-- b004118 | prose | pages [21] -->
m

<!-- b004119 | prose | pages [21] -->
m

<!-- b004120 | prose | pages [21] -->
m

<!-- b004121 | prose | pages [21] -->
m

<!-- b004122 | prose | pages [21] -->
m

<!-- b004123 | prose | pages [21] -->
m

<!-- b004124 | prose | pages [21] -->
m

<!-- b004125 | prose | pages [21] -->
m

<!-- b004126 | prose | pages [21] -->
m

<!-- b004127 | prose | pages [21] -->
m

<!-- b004128 | prose | pages [21] -->
m

<!-- b004129 | prose | pages [21] -->
m

<!-- b004130 | prose | pages [21] -->
m

<!-- b004131 | prose | pages [21] -->
m

<!-- b004132 | prose | pages [21] -->
m

<!-- b004133 | prose | pages [21] -->
m

<!-- b004134 | prose | pages [21] -->
m

<!-- b004135 | prose | pages [21] -->
m

<!-- b004136 | prose | pages [21] -->
m

<!-- b004137 | prose | pages [21] -->
m

<!-- b004138 | prose | pages [21] -->
m

<!-- b004139 | prose | pages [21] -->
m

<!-- b004140 | prose | pages [21] -->
m

<!-- b004141 | prose | pages [21] -->
m

<!-- b004142 | prose | pages [21] -->
m

<!-- b004143 | prose | pages [21] -->
m

<!-- b004144 | prose | pages [21] -->
m

<!-- b004145 | prose | pages [21] -->
m

<!-- b004146 | prose | pages [21] -->
m

<!-- b004147 | prose | pages [21] -->
m

<!-- b004148 | prose | pages [21] -->
m

<!-- b004149 | prose | pages [21] -->
m

<!-- b004150 | prose | pages [21] -->
m

<!-- b004151 | prose | pages [21] -->
m

<!-- b004152 | prose | pages [21] -->
m

<!-- b004153 | prose | pages [21] -->
m

<!-- b004154 | prose | pages [21] -->
m

<!-- b004155 | prose | pages [21] -->
m

<!-- b004156 | prose | pages [21] -->
m

<!-- b004157 | prose | pages [21] -->
m

<!-- b004158 | prose | pages [21] -->
m

<!-- b004159 | prose | pages [21] -->
m

<!-- b004160 | prose | pages [21] -->
m

<!-- b004161 | prose | pages [21] -->
m

<!-- b004162 | prose | pages [21] -->
m

<!-- b004163 | prose | pages [21] -->
m

<!-- b004164 | prose | pages [21] -->
m

<!-- b004165 | prose | pages [21] -->
m

<!-- b004166 | prose | pages [21] -->
m

<!-- b004167 | prose | pages [21] -->
m

<!-- b004168 | prose | pages [21] -->
m

<!-- b004169 | prose | pages [21] -->
m

<!-- b004170 | prose | pages [21] -->
m

<!-- b004171 | prose | pages [21] -->
m

<!-- b004172 | prose | pages [21] -->
m

<!-- b004173 | prose | pages [21] -->
m

<!-- b004174 | prose | pages [21] -->
m

<!-- b004175 | prose | pages [21] -->
m

<!-- b004176 | prose | pages [21] -->
m

<!-- b004177 | prose | pages [21] -->
m

<!-- b004178 | prose | pages [21] -->
m

<!-- b004179 | prose | pages [21] -->
m

<!-- b004180 | prose | pages [21] -->
m

<!-- b004181 | prose | pages [21] -->
m

<!-- b004182 | prose | pages [21] -->
m

<!-- b004183 | prose | pages [21] -->
m

<!-- b004184 | prose | pages [21] -->
m

<!-- b004185 | prose | pages [21] -->
m

<!-- b004186 | prose | pages [21] -->
m

<!-- b004187 | prose | pages [21] -->
m

<!-- b004188 | prose | pages [21] -->
m

<!-- b004189 | prose | pages [21] -->
m

<!-- b004190 | prose | pages [21] -->
m

<!-- b004191 | prose | pages [21] -->
m

<!-- b004192 | prose | pages [21] -->
m

<!-- b004193 | prose | pages [21] -->
m

<!-- b004194 | prose | pages [21] -->
m

<!-- b004195 | prose | pages [21] -->
m

<!-- b004196 | prose | pages [21] -->
m

<!-- b004197 | prose | pages [21] -->
m

<!-- b004198 | prose | pages [21] -->
m

<!-- b004199 | prose | pages [21] -->
m

<!-- b004200 | prose | pages [21] -->
m

<!-- b004201 | prose | pages [21] -->
m

<!-- b004202 | furniture | pages [21] -->
m

<!-- b004203 | furniture | pages [21] -->
m

<!-- b004204 | furniture | pages [21] -->
m

<!-- b004205 | furniture | pages [21] -->
m

<!-- b004206 | furniture | pages [21] -->
m

<!-- b004207 | furniture | pages [21] -->
m

<!-- b004208 | furniture | pages [21] -->
m

<!-- b004209 | furniture | pages [21] -->
m

<!-- b004210 | furniture | pages [21] -->
m

<!-- b004211 | furniture | pages [21] -->
m

<!-- b004212 | furniture | pages [21] -->
m

<!-- b004213 | furniture | pages [21] -->
m

<!-- b004214 | furniture | pages [21] -->
m

<!-- b004215 | furniture | pages [21] -->
m

<!-- b004216 | furniture | pages [21] -->
m

<!-- b004217 | furniture | pages [21] -->
m

<!-- b004218 | furniture | pages [21] -->
m

<!-- b004219 | furniture | pages [21] -->
m

<!-- b004220 | furniture | pages [21] -->
m

<!-- b004221 | furniture | pages [21] -->
m

<!-- b004222 | furniture | pages [21] -->
m

<!-- b004223 | furniture | pages [21] -->
m

<!-- b004224 | furniture | pages [21] -->
m

<!-- b004225 | furniture | pages [21] -->
m

<!-- b004226 | furniture | pages [21] -->
m

<!-- b004227 | furniture | pages [21] -->
m

<!-- b004228 | furniture | pages [21] -->
m

<!-- b004229 | furniture | pages [21] -->
m

<!-- b004230 | furniture | pages [21] -->
m

<!-- b004231 | furniture | pages [21] -->
m

<!-- b004232 | furniture | pages [21] -->
m

<!-- b004233 | furniture | pages [21] -->
m

<!-- b004234 | furniture | pages [21] -->
m

<!-- b004235 | furniture | pages [21] -->
m

<!-- b004236 | furniture | pages [21] -->
m

<!-- b004237 | furniture | pages [21] -->
m

<!-- b004238 | furniture | pages [21] -->
m

<!-- b004239 | furniture | pages [21] -->
m

<!-- b004240 | furniture | pages [21] -->
m

<!-- b004241 | furniture | pages [21] -->
m

<!-- b004242 | furniture | pages [21] -->
m

<!-- b004243 | furniture | pages [21] -->
m

<!-- b004244 | furniture | pages [21] -->
m

<!-- b004245 | furniture | pages [21] -->
m

<!-- b004246 | furniture | pages [21] -->
m

<!-- b004247 | furniture | pages [21] -->
m

<!-- b004248 | furniture | pages [21] -->
m

<!-- b004249 | furniture | pages [21] -->
m

<!-- b004250 | furniture | pages [21] -->
m

<!-- b004251 | furniture | pages [21] -->
m

<!-- b004252 | furniture | pages [21] -->
m

<!-- b004253 | furniture | pages [21] -->
m

<!-- b004254 | furniture | pages [21] -->
m

<!-- b004255 | furniture | pages [21] -->
m

<!-- b004256 | furniture | pages [21] -->
m

<!-- b004257 | furniture | pages [21] -->
m

<!-- b004258 | furniture | pages [21] -->
m

<!-- b004259 | furniture | pages [21] -->
m

<!-- b004260 | furniture | pages [21] -->
m

<!-- b004261 | furniture | pages [21] -->
m

<!-- b004262 | furniture | pages [21] -->
m

<!-- b004263 | furniture | pages [21] -->
m

<!-- b004264 | furniture | pages [21] -->
m

<!-- b004265 | furniture | pages [21] -->
m

<!-- b004266 | furniture | pages [21] -->
m

<!-- b004267 | furniture | pages [21] -->
m

<!-- b004268 | furniture | pages [21] -->
m

<!-- b004269 | furniture | pages [21] -->
m

<!-- b004270 | furniture | pages [21] -->
m

<!-- b004271 | furniture | pages [21] -->
m

<!-- b004272 | furniture | pages [21] -->
m

<!-- b004273 | furniture | pages [21] -->
m

<!-- b004274 | furniture | pages [21] -->
m

<!-- b004275 | furniture | pages [21] -->
m

<!-- b004276 | furniture | pages [21] -->
m

<!-- b004277 | furniture | pages [21] -->
m

<!-- b004278 | furniture | pages [21] -->
m

<!-- b004279 | furniture | pages [21] -->
m

<!-- b004280 | furniture | pages [21] -->
m

<!-- b004281 | furniture | pages [21] -->
m

<!-- b004282 | furniture | pages [21] -->
m

<!-- b004283 | furniture | pages [21] -->
m

<!-- b004284 | furniture | pages [21] -->
m

<!-- b004285 | furniture | pages [21] -->
m

<!-- b004286 | furniture | pages [21] -->
m

<!-- b004287 | furniture | pages [21] -->
m

<!-- b004288 | furniture | pages [21] -->
m

<!-- b004289 | furniture | pages [21] -->
m

<!-- b004290 | furniture | pages [21] -->
m

<!-- b004291 | furniture | pages [21] -->
m

<!-- b004292 | furniture | pages [21] -->
m

<!-- b004293 | furniture | pages [21] -->
m

<!-- b004294 | furniture | pages [21] -->
m

<!-- b004295 | furniture | pages [21] -->
m

<!-- b004296 | furniture | pages [21] -->
m

<!-- b004297 | furniture | pages [21] -->
m

<!-- b004298 | furniture | pages [21] -->
m

<!-- b004299 | furniture | pages [21] -->
m

<!-- b004300 | furniture | pages [21] -->
m

<!-- b004301 | furniture | pages [21] -->
m

<!-- b004302 | furniture | pages [21] -->
m

<!-- b004303 | furniture | pages [21] -->
m

<!-- b004304 | furniture | pages [21] -->
m

<!-- b004305 | furniture | pages [21] -->
m

<!-- b004306 | furniture | pages [21] -->
m

<!-- b004307 | furniture | pages [21] -->
m

<!-- b004308 | furniture | pages [21] -->
m

<!-- b004309 | furniture | pages [21] -->
m

<!-- b004310 | furniture | pages [21] -->
m

<!-- b004311 | furniture | pages [21] -->
m

<!-- b004312 | furniture | pages [21] -->
m

<!-- b004313 | furniture | pages [21] -->
m

<!-- b004314 | furniture | pages [21] -->
m

<!-- b004315 | furniture | pages [21] -->
m

<!-- b004316 | furniture | pages [21] -->
m

<!-- b004317 | furniture | pages [21] -->
m

<!-- b004318 | furniture | pages [21] -->
m

<!-- b004319 | furniture | pages [21] -->
m

<!-- b004320 | furniture | pages [21] -->
m

<!-- b004321 | furniture | pages [21] -->
m

<!-- b004322 | furniture | pages [21] -->
m

<!-- b004323 | furniture | pages [21] -->
m

<!-- b004324 | furniture | pages [21] -->
m

<!-- b004325 | furniture | pages [21] -->
m

<!-- b004326 | furniture | pages [21] -->
m

<!-- b004327 | furniture | pages [21] -->
m

<!-- b004328 | furniture | pages [21] -->
m

<!-- b004329 | furniture | pages [21] -->
m

<!-- b004330 | furniture | pages [21] -->
m

<!-- b004331 | furniture | pages [21] -->
m

<!-- b004332 | furniture | pages [21] -->
m

<!-- b004333 | furniture | pages [21] -->
m

<!-- b004334 | furniture | pages [21] -->
m

<!-- b004335 | furniture | pages [21] -->
m

<!-- b004336 | furniture | pages [21] -->
m

<!-- b004337 | furniture | pages [21] -->
m

<!-- b004338 | furniture | pages [21] -->
m

<!-- b004339 | furniture | pages [21] -->
m

<!-- b004340 | furniture | pages [21] -->
m

<!-- b004341 | furniture | pages [21] -->
m

<!-- b004342 | furniture | pages [21] -->
m

<!-- b004343 | furniture | pages [21] -->
m

<!-- b004344 | furniture | pages [21] -->
m

<!-- b004345 | furniture | pages [21] -->
m

<!-- b004346 | furniture | pages [21] -->
m

<!-- b004347 | furniture | pages [21] -->
m

<!-- b004348 | furniture | pages [21] -->
m

<!-- b004349 | furniture | pages [21] -->
m

<!-- b004350 | furniture | pages [21] -->
m

<!-- b004351 | furniture | pages [21] -->
m

<!-- b004352 | furniture | pages [21] -->
m

<!-- b004353 | furniture | pages [21] -->
m

<!-- b004354 | furniture | pages [21] -->
m

<!-- b004355 | furniture | pages [21] -->
m

<!-- b004356 | furniture | pages [21] -->
m

<!-- b004357 | furniture | pages [21] -->
m

<!-- b004358 | furniture | pages [21] -->
m

<!-- b004359 | furniture | pages [21] -->
m

<!-- b004360 | furniture | pages [21] -->
m

<!-- b004361 | furniture | pages [21] -->
m

<!-- b004362 | furniture | pages [21] -->
m

<!-- b004363 | furniture | pages [21] -->
m

<!-- b004364 | furniture | pages [21] -->
m

<!-- b004365 | furniture | pages [21] -->
m

<!-- b004366 | furniture | pages [21] -->
m

<!-- b004367 | furniture | pages [21] -->
m

<!-- b004368 | furniture | pages [21] -->
m

<!-- b004369 | furniture | pages [21] -->
m

<!-- b004370 | furniture | pages [21] -->
m

<!-- b004371 | furniture | pages [21] -->
m

<!-- b004372 | furniture | pages [21] -->
m

<!-- b004373 | furniture | pages [21] -->
m

<!-- b004374 | furniture | pages [21] -->
m

<!-- b004375 | furniture | pages [21] -->
m

<!-- b004376 | furniture | pages [21] -->
m

<!-- b004377 | furniture | pages [21] -->
m

<!-- b004378 | furniture | pages [21] -->
m

<!-- b004379 | furniture | pages [21] -->
m

<!-- b004380 | furniture | pages [21] -->
m

<!-- b004381 | furniture | pages [21] -->
m

<!-- b004382 | furniture | pages [21] -->
m

<!-- b004383 | furniture | pages [21] -->
m

<!-- b004384 | furniture | pages [21] -->
m

<!-- b004385 | furniture | pages [21] -->
m

<!-- b004386 | furniture | pages [21] -->
m

<!-- b004387 | furniture | pages [21] -->
m

<!-- b004388 | furniture | pages [21] -->
m

<!-- b004389 | furniture | pages [21] -->
m

<!-- b004390 | furniture | pages [21] -->
m

<!-- b004391 | furniture | pages [21] -->
m

<!-- b004392 | furniture | pages [21] -->
m

<!-- b004393 | furniture | pages [21] -->
m

<!-- b004394 | furniture | pages [21] -->
m

<!-- b004395 | furniture | pages [21] -->
m

<!-- b004396 | furniture | pages [21] -->
m

<!-- b004397 | furniture | pages [21] -->
m

<!-- b004398 | furniture | pages [21] -->
m

<!-- b004399 | furniture | pages [21] -->
m

<!-- b004400 | furniture | pages [21] -->
m

<!-- b004401 | furniture | pages [21] -->
m

<!-- b004402 | furniture | pages [21] -->
m

<!-- b004403 | furniture | pages [21] -->
m

<!-- b004404 | furniture | pages [21] -->
m

<!-- b004405 | furniture | pages [21] -->
m

<!-- b004406 | furniture | pages [21] -->
m

<!-- b004407 | furniture | pages [21] -->
m

<!-- b004408 | furniture | pages [21] -->
m

<!-- b004409 | furniture | pages [21] -->
m

<!-- b004410 | furniture | pages [21] -->
m

<!-- b004411 | furniture | pages [21] -->
m

<!-- b004412 | furniture | pages [21] -->
m

<!-- b004413 | furniture | pages [21] -->
m

<!-- b004414 | furniture | pages [21] -->
m

<!-- b004415 | furniture | pages [21] -->
m

<!-- b004416 | furniture | pages [21] -->
m

<!-- b004417 | furniture | pages [21] -->
m

<!-- b004418 | furniture | pages [21] -->
m

<!-- b004419 | furniture | pages [21] -->
m

<!-- b004420 | furniture | pages [21] -->
m

<!-- b004421 | furniture | pages [21] -->
m

<!-- b004422 | furniture | pages [21] -->
m

<!-- b004423 | furniture | pages [21] -->
m

<!-- b004424 | furniture | pages [21] -->
m

<!-- b004425 | furniture | pages [21] -->
m

<!-- b004426 | furniture | pages [21] -->
m

<!-- b004427 | furniture | pages [21] -->
m

<!-- b004428 | furniture | pages [21] -->
m

<!-- b004429 | furniture | pages [21] -->
m

<!-- b004430 | furniture | pages [21] -->
m

<!-- b004431 | furniture | pages [21] -->
m

<!-- b004432 | furniture | pages [21] -->
m

<!-- b004433 | furniture | pages [21] -->
m

<!-- b004434 | furniture | pages [21] -->
m

<!-- b004435 | furniture | pages [21] -->
m

<!-- b004436 | furniture | pages [21] -->
m

<!-- b004437 | furniture | pages [21] -->
m

<!-- b004438 | furniture | pages [21] -->
m

<!-- b004439 | furniture | pages [21] -->
m

<!-- b004440 | furniture | pages [21] -->
m

<!-- b004441 | furniture | pages [21] -->
m

<!-- b004442 | furniture | pages [21] -->
m

<!-- b004443 | furniture | pages [21] -->
m

<!-- b004444 | furniture | pages [21] -->
m

<!-- b004445 | furniture | pages [21] -->
m

<!-- b004446 | furniture | pages [21] -->
m

<!-- b004447 | furniture | pages [21] -->
m

<!-- b004448 | furniture | pages [21] -->
m

<!-- b004449 | furniture | pages [21] -->
m

<!-- b004450 | furniture | pages [21] -->
m

<!-- b004451 | furniture | pages [21] -->
m

<!-- b004452 | furniture | pages [21] -->
m

<!-- b004453 | furniture | pages [21] -->
m

<!-- b004454 | furniture | pages [21] -->
m

<!-- b004455 | furniture | pages [21] -->
m

<!-- b004456 | furniture | pages [21] -->
m

<!-- b004457 | furniture | pages [21] -->
m

<!-- b004458 | furniture | pages [21] -->
m

<!-- b004459 | furniture | pages [21] -->
m

<!-- b004460 | furniture | pages [21] -->
m

<!-- b004461 | furniture | pages [21] -->
m

<!-- b004462 | furniture | pages [21] -->
m

<!-- b004463 | furniture | pages [21] -->
m

<!-- b004464 | furniture | pages [21] -->
m

<!-- b004465 | furniture | pages [21] -->
m

<!-- b004466 | furniture | pages [21] -->
m

<!-- b004467 | furniture | pages [21] -->
m

<!-- b004468 | furniture | pages [21] -->
m

<!-- b004469 | furniture | pages [21] -->
m

<!-- b004470 | furniture | pages [21] -->
m

<!-- b004471 | furniture | pages [21] -->
m

<!-- b004472 | furniture | pages [21] -->
m

<!-- b004473 | furniture | pages [21] -->
m

<!-- b004474 | furniture | pages [21] -->
m

<!-- b004475 | furniture | pages [21] -->
m

<!-- b004476 | furniture | pages [21] -->
m

<!-- b004477 | furniture | pages [21] -->
m

<!-- b004478 | furniture | pages [21] -->
m

<!-- b004479 | furniture | pages [21] -->
m

<!-- b004480 | furniture | pages [21] -->
m

<!-- b004481 | furniture | pages [21] -->
m

<!-- b004482 | furniture | pages [21] -->
m

<!-- b004483 | furniture | pages [21] -->
m

<!-- b004484 | furniture | pages [21] -->
m

<!-- b004485 | furniture | pages [21] -->
m

<!-- b004486 | furniture | pages [21] -->
m

<!-- b004487 | furniture | pages [21] -->
m

<!-- b004488 | furniture | pages [21] -->
m

<!-- b004489 | furniture | pages [21] -->
m

<!-- b004490 | furniture | pages [21] -->
m

<!-- b004491 | furniture | pages [21] -->
m

<!-- b004492 | furniture | pages [21] -->
m

<!-- b004493 | furniture | pages [21] -->
m

<!-- b004494 | furniture | pages [21] -->
m

<!-- b004495 | furniture | pages [21] -->
m

<!-- b004496 | furniture | pages [21] -->
m

<!-- b004497 | furniture | pages [21] -->
m

<!-- b004498 | furniture | pages [21] -->
m

<!-- b004499 | furniture | pages [21] -->
m

<!-- b004500 | furniture | pages [21] -->
m

<!-- b004501 | furniture | pages [21] -->
m

<!-- b004502 | furniture | pages [21] -->
m

<!-- b004503 | furniture | pages [21] -->
m

<!-- b004504 | furniture | pages [21] -->
m

<!-- b004505 | furniture | pages [21] -->
m

<!-- b004506 | furniture | pages [21] -->
m

<!-- b004507 | furniture | pages [21] -->
m

<!-- b004508 | furniture | pages [21] -->
m

<!-- b004509 | furniture | pages [21] -->
m

<!-- b004510 | furniture | pages [21] -->
m

<!-- b004511 | furniture | pages [21] -->
m

<!-- b004512 | furniture | pages [21] -->
m

<!-- b004513 | furniture | pages [21] -->
m

<!-- b004514 | furniture | pages [21] -->
m

<!-- b004515 | furniture | pages [21] -->
m

<!-- b004516 | furniture | pages [21] -->
m

<!-- b004517 | furniture | pages [21] -->
m

<!-- b004518 | furniture | pages [21] -->
m

<!-- b004519 | furniture | pages [21] -->
m

<!-- b004520 | furniture | pages [21] -->
m

<!-- b004521 | furniture | pages [21] -->
m

<!-- b004522 | furniture | pages [21] -->
m

<!-- b004523 | furniture | pages [21] -->
m

<!-- b004524 | furniture | pages [21] -->
m

<!-- b004525 | furniture | pages [21] -->
m

<!-- b004526 | furniture | pages [21] -->
m

<!-- b004527 | furniture | pages [21] -->
m

<!-- b004528 | furniture | pages [21] -->
m

<!-- b004529 | furniture | pages [21] -->
m

<!-- b004530 | furniture | pages [21] -->
m

<!-- b004531 | furniture | pages [21] -->
m

<!-- b004532 | furniture | pages [21] -->
m

<!-- b004533 | furniture | pages [21] -->
m

<!-- b004534 | furniture | pages [21] -->
m

<!-- b004535 | furniture | pages [21] -->
m

<!-- b004536 | furniture | pages [21] -->
m

<!-- b004537 | furniture | pages [21] -->
m

<!-- b004538 | furniture | pages [21] -->
m

<!-- b004539 | furniture | pages [21] -->
m

<!-- b004540 | furniture | pages [21] -->
m

<!-- b004541 | furniture | pages [21] -->
m

<!-- b004542 | furniture | pages [21] -->
m

<!-- b004543 | furniture | pages [21] -->
m

<!-- b004544 | furniture | pages [21] -->
m

<!-- b004545 | furniture | pages [21] -->
m

<!-- b004546 | furniture | pages [21] -->
m

<!-- b004547 | furniture | pages [21] -->
m

<!-- b004548 | furniture | pages [21] -->
m

<!-- b004549 | furniture | pages [21] -->
m

<!-- b004550 | furniture | pages [21] -->
m

<!-- b004551 | furniture | pages [21] -->
m

<!-- b004552 | furniture | pages [21] -->
m

<!-- b004553 | furniture | pages [21] -->
m

<!-- b004554 | furniture | pages [21] -->
m

<!-- b004555 | furniture | pages [21] -->
m

<!-- b004556 | furniture | pages [21] -->
m

<!-- b004557 | furniture | pages [21] -->
m

<!-- b004558 | furniture | pages [21] -->
m

<!-- b004559 | furniture | pages [21] -->
m

<!-- b004560 | furniture | pages [21] -->
m

<!-- b004561 | furniture | pages [21] -->
m

<!-- b004562 | furniture | pages [21] -->
m

<!-- b004563 | furniture | pages [21] -->
m

<!-- b004564 | furniture | pages [21] -->
m

<!-- b004565 | furniture | pages [21] -->
m

<!-- b004566 | furniture | pages [21] -->
m

<!-- b004567 | furniture | pages [21] -->
m

<!-- b004568 | furniture | pages [21] -->
m

<!-- b004569 | furniture | pages [21] -->
m

<!-- b004570 | furniture | pages [21] -->
m

<!-- b004571 | furniture | pages [21] -->
m

<!-- b004572 | furniture | pages [21] -->
m

<!-- b004573 | furniture | pages [21] -->
m

<!-- b004574 | furniture | pages [21] -->
m

<!-- b004575 | furniture | pages [21] -->
m

<!-- b004576 | furniture | pages [21] -->
m

<!-- b004577 | furniture | pages [21] -->
m

<!-- b004578 | furniture | pages [21] -->
m

<!-- b004579 | furniture | pages [21] -->
m

<!-- b004580 | furniture | pages [21] -->
m

<!-- b004581 | furniture | pages [21] -->
m

<!-- b004582 | furniture | pages [21] -->
m

<!-- b004583 | furniture | pages [21] -->
m

<!-- b004584 | furniture | pages [21] -->
m

<!-- b004585 | furniture | pages [21] -->
m

<!-- b004586 | furniture | pages [21] -->
m

<!-- b004587 | furniture | pages [21] -->
m

<!-- b004588 | furniture | pages [21] -->
m

<!-- b004589 | furniture | pages [21] -->
m

<!-- b004590 | furniture | pages [21] -->
m

<!-- b004591 | furniture | pages [21] -->
m

<!-- b004592 | furniture | pages [21] -->
m

<!-- b004593 | furniture | pages [21] -->
m

<!-- b004594 | furniture | pages [21] -->
m

<!-- b004595 | furniture | pages [21] -->
m

<!-- b004596 | furniture | pages [21] -->
m

<!-- b004597 | furniture | pages [21] -->
m

<!-- b004598 | furniture | pages [21] -->
m

<!-- b004599 | furniture | pages [21] -->
m

<!-- b004600 | furniture | pages [21] -->
m

<!-- b004601 | furniture | pages [21] -->
m

<!-- b004602 | furniture | pages [21] -->
m

<!-- b004603 | furniture | pages [21] -->
m

<!-- b004604 | furniture | pages [21] -->
m

<!-- b004605 | furniture | pages [22] -->
Team 2522820

<!-- b004606 | furniture | pages [22] -->
Page 22

<!-- b004607 | prose | pages [22] -->
Identifying Country-Sport Pairs Fit for Great Coaches and Estimating Impacts 4.3

<!-- b004608 | prose | pages [22] -->
Similarly, we can interpret the results of our model from 4.1 yet another way to identify country-sport pairs that would particularly benefit from investing in great coaches. For the same set of the top 20 country-sport pairs we found with the highest z-scores that we used in 4.2, we calculated ∆Pnorm:

<!-- b004609 | prose | pages [22] -->
∆Pnorm = C

<!-- b004610 | prose | pages [22] -->
L = Ps −µ · L

<!-- b004611 | prose | pages [22] -->
. L

<!-- b004612 | prose | pages [22] -->
This is the value that great coaches add to the given sport, normalized per Games so they can be compared with values for different sports. Countries should invest in coaches for sports where performances have been shown to be greatly affected by great coaches. It is also reasonable for countries to invest in great coaches for sports that they have previously excelled in under the leadership of great coaches in hopes of replicating previous success.

<!-- b004613 | caption | pages [22] -->
Table 18: Top 10 Countries with Highest ∆Pnorm in Olympic Sports

<!-- b004614 | prose | pages [22] -->
∆Pnorm Country (Sport) Year

<!-- b004615 | prose | pages [22] -->
Start End

<!-- b004616 | prose | pages [22] -->
Romania (Rowing) 1980 1984 42.0 Russia (Weightlifting) 2000 2004 20.0 Russia (Diving) 1996 2000 19.0 China (Trampolining) 2004 2008 14.0 China (Taekwondo) 2000 2004 12.0 Great Britain (Tug-Of-War) 1904 1908 11.0 Hungary (Weightlifting) 1968 1988 6.8 United States (Synchronized Swimming) 1980 2004 6.7 Canada (Trampolining) 2004 2008 6.0 United States (Softball) 1992 1996 6.0

<!-- b004617 | prose | pages [22] -->
From this table, it is important to note that the 1984 Olympics were an anomaly because it took place in Los Angeles and was the target of boycotts from many of the Eastern Bloc nations, which played a major role in the anomalous success of the Romanian rowing teams.[7]

<!-- b004618 | prose | pages [22] -->
Aside from this outlier, Russia could benefit from investing in a great coach for weightlifting: in 2004, Russia’s weightlifting athletes were coached by David Rigert, who set 65 world records and won an Olympic gold himself.[8]

<!-- b004619 | prose | pages [22] -->
m

<!-- b004620 | prose | pages [22] -->
m

<!-- b004621 | prose | pages [22] -->
m

<!-- b004622 | prose | pages [22] -->
m

<!-- b004623 | prose | pages [22] -->
m

<!-- b004624 | prose | pages [22] -->
m

<!-- b004625 | prose | pages [22] -->
m

<!-- b004626 | prose | pages [22] -->
m

<!-- b004627 | prose | pages [22] -->
m

<!-- b004628 | prose | pages [22] -->
m

<!-- b004629 | prose | pages [22] -->
m

<!-- b004630 | prose | pages [22] -->
m

<!-- b004631 | prose | pages [22] -->
m

<!-- b004632 | prose | pages [22] -->
m

<!-- b004633 | prose | pages [22] -->
m

<!-- b004634 | prose | pages [22] -->
m

<!-- b004635 | prose | pages [22] -->
m

<!-- b004636 | prose | pages [22] -->
m

<!-- b004637 | prose | pages [22] -->
m

<!-- b004638 | prose | pages [22] -->
m

<!-- b004639 | prose | pages [22] -->
m

<!-- b004640 | prose | pages [22] -->
m

<!-- b004641 | prose | pages [22] -->
m

<!-- b004642 | prose | pages [22] -->
m

<!-- b004643 | prose | pages [22] -->
m

<!-- b004644 | prose | pages [22] -->
m

<!-- b004645 | prose | pages [22] -->
m

<!-- b004646 | prose | pages [22] -->
m

<!-- b004647 | prose | pages [22] -->
m

<!-- b004648 | prose | pages [22] -->
m

<!-- b004649 | prose | pages [22] -->
m

<!-- b004650 | prose | pages [22] -->
m

<!-- b004651 | prose | pages [22] -->
m

<!-- b004652 | prose | pages [22] -->
m

<!-- b004653 | prose | pages [22] -->
m

<!-- b004654 | prose | pages [22] -->
m

<!-- b004655 | prose | pages [22] -->
m

<!-- b004656 | prose | pages [22] -->
m

<!-- b004657 | prose | pages [22] -->
m

<!-- b004658 | prose | pages [22] -->
m

<!-- b004659 | prose | pages [22] -->
m

<!-- b004660 | prose | pages [22] -->
m

<!-- b004661 | prose | pages [22] -->
m

<!-- b004662 | prose | pages [22] -->
m

<!-- b004663 | prose | pages [22] -->
m

<!-- b004664 | prose | pages [22] -->
m

<!-- b004665 | prose | pages [22] -->
m

<!-- b004666 | prose | pages [22] -->
m

<!-- b004667 | prose | pages [22] -->
m

<!-- b004668 | prose | pages [22] -->
m

<!-- b004669 | prose | pages [22] -->
m

<!-- b004670 | prose | pages [22] -->
m

<!-- b004671 | prose | pages [22] -->
m

<!-- b004672 | prose | pages [22] -->
m

<!-- b004673 | prose | pages [22] -->
m

<!-- b004674 | prose | pages [22] -->
m

<!-- b004675 | prose | pages [22] -->
m

<!-- b004676 | prose | pages [22] -->
m

<!-- b004677 | prose | pages [22] -->
m

<!-- b004678 | prose | pages [22] -->
m

<!-- b004679 | prose | pages [22] -->
m

<!-- b004680 | prose | pages [22] -->
m

<!-- b004681 | prose | pages [22] -->
m

<!-- b004682 | prose | pages [22] -->
m

<!-- b004683 | prose | pages [22] -->
m

<!-- b004684 | prose | pages [22] -->
m

<!-- b004685 | prose | pages [22] -->
m

<!-- b004686 | prose | pages [22] -->
m

<!-- b004687 | prose | pages [22] -->
m

<!-- b004688 | prose | pages [22] -->
m

<!-- b004689 | prose | pages [22] -->
m

<!-- b004690 | prose | pages [22] -->
m

<!-- b004691 | prose | pages [22] -->
m

<!-- b004692 | prose | pages [22] -->
m

<!-- b004693 | prose | pages [22] -->
m

<!-- b004694 | prose | pages [22] -->
m

<!-- b004695 | prose | pages [22] -->
m

<!-- b004696 | prose | pages [22] -->
m

<!-- b004697 | prose | pages [22] -->
m

<!-- b004698 | prose | pages [22] -->
m

<!-- b004699 | prose | pages [22] -->
m

<!-- b004700 | prose | pages [22] -->
m

<!-- b004701 | prose | pages [22] -->
m

<!-- b004702 | prose | pages [22] -->
m

<!-- b004703 | prose | pages [22] -->
m

<!-- b004704 | prose | pages [22] -->
m

<!-- b004705 | prose | pages [22] -->
m

<!-- b004706 | prose | pages [22] -->
m

<!-- b004707 | prose | pages [22] -->
m

<!-- b004708 | prose | pages [22] -->
m

<!-- b004709 | prose | pages [22] -->
m

<!-- b004710 | prose | pages [22] -->
m

<!-- b004711 | prose | pages [22] -->
m

<!-- b004712 | prose | pages [22] -->
m

<!-- b004713 | prose | pages [22] -->
m

<!-- b004714 | prose | pages [22] -->
m

<!-- b004715 | prose | pages [22] -->
m

<!-- b004716 | prose | pages [22] -->
m

<!-- b004717 | prose | pages [22] -->
m

<!-- b004718 | prose | pages [22] -->
m

<!-- b004719 | prose | pages [22] -->
m

<!-- b004720 | prose | pages [22] -->
m

<!-- b004721 | prose | pages [22] -->
m

<!-- b004722 | prose | pages [22] -->
m

<!-- b004723 | prose | pages [22] -->
m

<!-- b004724 | prose | pages [22] -->
m

<!-- b004725 | prose | pages [22] -->
m

<!-- b004726 | prose | pages [22] -->
m

<!-- b004727 | prose | pages [22] -->
m

<!-- b004728 | prose | pages [22] -->
m

<!-- b004729 | prose | pages [22] -->
m

<!-- b004730 | prose | pages [22] -->
m

<!-- b004731 | prose | pages [22] -->
m

<!-- b004732 | prose | pages [22] -->
m

<!-- b004733 | prose | pages [22] -->
m

<!-- b004734 | prose | pages [22] -->
m

<!-- b004735 | prose | pages [22] -->
m

<!-- b004736 | prose | pages [22] -->
m

<!-- b004737 | prose | pages [22] -->
m

<!-- b004738 | prose | pages [22] -->
m

<!-- b004739 | prose | pages [22] -->
m

<!-- b004740 | prose | pages [22] -->
m

<!-- b004741 | prose | pages [22] -->
m

<!-- b004742 | prose | pages [22] -->
m

<!-- b004743 | prose | pages [22] -->
m

<!-- b004744 | prose | pages [22] -->
m

<!-- b004745 | prose | pages [22] -->
m

<!-- b004746 | prose | pages [22] -->
m

<!-- b004747 | prose | pages [22] -->
m

<!-- b004748 | prose | pages [22] -->
m

<!-- b004749 | prose | pages [22] -->
m

<!-- b004750 | prose | pages [22] -->
m

<!-- b004751 | prose | pages [22] -->
m

<!-- b004752 | prose | pages [22] -->
m

<!-- b004753 | prose | pages [22] -->
m

<!-- b004754 | prose | pages [22] -->
m

<!-- b004755 | prose | pages [22] -->
m

<!-- b004756 | prose | pages [22] -->
m

<!-- b004757 | prose | pages [22] -->
m

<!-- b004758 | prose | pages [22] -->
m

<!-- b004759 | prose | pages [22] -->
m

<!-- b004760 | prose | pages [22] -->
m

<!-- b004761 | prose | pages [22] -->
m

<!-- b004762 | prose | pages [22] -->
m

<!-- b004763 | prose | pages [22] -->
m

<!-- b004764 | prose | pages [22] -->
m

<!-- b004765 | prose | pages [22] -->
m

<!-- b004766 | prose | pages [22] -->
m

<!-- b004767 | prose | pages [22] -->
m

<!-- b004768 | prose | pages [22] -->
m

<!-- b004769 | prose | pages [22] -->
m

<!-- b004770 | prose | pages [22] -->
m

<!-- b004771 | prose | pages [22] -->
m

<!-- b004772 | prose | pages [22] -->
m

<!-- b004773 | prose | pages [22] -->
m

<!-- b004774 | prose | pages [22] -->
m

<!-- b004775 | prose | pages [22] -->
m

<!-- b004776 | prose | pages [22] -->
m

<!-- b004777 | prose | pages [22] -->
m

<!-- b004778 | prose | pages [22] -->
m

<!-- b004779 | prose | pages [22] -->
m

<!-- b004780 | prose | pages [22] -->
m

<!-- b004781 | prose | pages [22] -->
m

<!-- b004782 | prose | pages [22] -->
m

<!-- b004783 | prose | pages [22] -->
m

<!-- b004784 | prose | pages [22] -->
m

<!-- b004785 | prose | pages [22] -->
m

<!-- b004786 | prose | pages [22] -->
m

<!-- b004787 | prose | pages [22] -->
m

<!-- b004788 | prose | pages [22] -->
m

<!-- b004789 | prose | pages [22] -->
m

<!-- b004790 | prose | pages [22] -->
m

<!-- b004791 | prose | pages [22] -->
m

<!-- b004792 | prose | pages [22] -->
m

<!-- b004793 | prose | pages [22] -->
m

<!-- b004794 | prose | pages [22] -->
m

<!-- b004795 | prose | pages [22] -->
m

<!-- b004796 | prose | pages [22] -->
m

<!-- b004797 | prose | pages [22] -->
m

<!-- b004798 | prose | pages [22] -->
m

<!-- b004799 | prose | pages [22] -->
m

<!-- b004800 | prose | pages [22] -->
m

<!-- b004801 | prose | pages [22] -->
m

<!-- b004802 | prose | pages [22] -->
m

<!-- b004803 | prose | pages [22] -->
m

<!-- b004804 | prose | pages [22] -->
m

<!-- b004805 | prose | pages [22] -->
m

<!-- b004806 | prose | pages [22] -->
m

<!-- b004807 | prose | pages [22] -->
m

<!-- b004808 | prose | pages [22] -->
m

<!-- b004809 | prose | pages [22] -->
m

<!-- b004810 | prose | pages [22] -->
m

<!-- b004811 | prose | pages [22] -->
m

<!-- b004812 | prose | pages [22] -->
m

<!-- b004813 | prose | pages [22] -->
m

<!-- b004814 | prose | pages [22] -->
m

<!-- b004815 | prose | pages [22] -->
m

<!-- b004816 | prose | pages [22] -->
m

<!-- b004817 | prose | pages [22] -->
m

<!-- b004818 | prose | pages [22] -->
m

<!-- b004819 | prose | pages [22] -->
m

<!-- b004820 | prose | pages [22] -->
m

<!-- b004821 | prose | pages [22] -->
m

<!-- b004822 | prose | pages [22] -->
m

<!-- b004823 | prose | pages [22] -->
m

<!-- b004824 | prose | pages [22] -->
m

<!-- b004825 | prose | pages [22] -->
m

<!-- b004826 | prose | pages [22] -->
m

<!-- b004827 | prose | pages [22] -->
m

<!-- b004828 | prose | pages [22] -->
m

<!-- b004829 | prose | pages [22] -->
m

<!-- b004830 | prose | pages [22] -->
m

<!-- b004831 | prose | pages [22] -->
m

<!-- b004832 | prose | pages [22] -->
m

<!-- b004833 | prose | pages [22] -->
m

<!-- b004834 | prose | pages [22] -->
m

<!-- b004835 | prose | pages [22] -->
m

<!-- b004836 | prose | pages [22] -->
m

<!-- b004837 | prose | pages [22] -->
m

<!-- b004838 | prose | pages [22] -->
m

<!-- b004839 | prose | pages [22] -->
m

<!-- b004840 | prose | pages [22] -->
m

<!-- b004841 | prose | pages [22] -->
m

<!-- b004842 | prose | pages [22] -->
m

<!-- b004843 | prose | pages [22] -->
m

<!-- b004844 | prose | pages [22] -->
m

<!-- b004845 | prose | pages [22] -->
m

<!-- b004846 | prose | pages [22] -->
m

<!-- b004847 | prose | pages [22] -->
m

<!-- b004848 | prose | pages [22] -->
m

<!-- b004849 | prose | pages [22] -->
m

<!-- b004850 | prose | pages [22] -->
m

<!-- b004851 | prose | pages [22] -->
m

<!-- b004852 | prose | pages [22] -->
m

<!-- b004853 | prose | pages [22] -->
m

<!-- b004854 | prose | pages [22] -->
m

<!-- b004855 | prose | pages [22] -->
m

<!-- b004856 | prose | pages [22] -->
m

<!-- b004857 | prose | pages [22] -->
m

<!-- b004858 | prose | pages [22] -->
m

<!-- b004859 | prose | pages [22] -->
m

<!-- b004860 | prose | pages [22] -->
m

<!-- b004861 | prose | pages [22] -->
m

<!-- b004862 | prose | pages [22] -->
m

<!-- b004863 | prose | pages [22] -->
m

<!-- b004864 | prose | pages [22] -->
m

<!-- b004865 | prose | pages [22] -->
m

<!-- b004866 | prose | pages [22] -->
m

<!-- b004867 | prose | pages [22] -->
m

<!-- b004868 | prose | pages [22] -->
m

<!-- b004869 | prose | pages [22] -->
m

<!-- b004870 | prose | pages [22] -->
m

<!-- b004871 | prose | pages [22] -->
m

<!-- b004872 | prose | pages [22] -->
m

<!-- b004873 | prose | pages [22] -->
m

<!-- b004874 | prose | pages [22] -->
m

<!-- b004875 | prose | pages [22] -->
m

<!-- b004876 | prose | pages [22] -->
m

<!-- b004877 | prose | pages [22] -->
m

<!-- b004878 | prose | pages [22] -->
m

<!-- b004879 | prose | pages [22] -->
m

<!-- b004880 | prose | pages [22] -->
m

<!-- b004881 | prose | pages [22] -->
China could benefit from investing in a great coach for trampolining, based on the success of its 2008 athletes.

<!-- b004882 | prose | pages [22] -->
m

<!-- b004883 | prose | pages [22] -->
m

<!-- b004884 | prose | pages [22] -->
m

<!-- b004885 | prose | pages [22] -->
m

<!-- b004886 | prose | pages [22] -->
m

<!-- b004887 | prose | pages [22] -->
m

<!-- b004888 | prose | pages [22] -->
m

<!-- b004889 | prose | pages [22] -->
m

<!-- b004890 | prose | pages [22] -->
m

<!-- b004891 | prose | pages [22] -->
m

<!-- b004892 | prose | pages [22] -->
m

<!-- b004893 | prose | pages [22] -->
m

<!-- b004894 | prose | pages [22] -->
m

<!-- b004895 | prose | pages [22] -->
m

<!-- b004896 | prose | pages [22] -->
m

<!-- b004897 | prose | pages [22] -->
m

<!-- b004898 | prose | pages [22] -->
m

<!-- b004899 | prose | pages [22] -->
m

<!-- b004900 | prose | pages [22] -->
m

<!-- b004901 | prose | pages [22] -->
m

<!-- b004902 | prose | pages [22] -->
m

<!-- b004903 | prose | pages [22] -->
m

<!-- b004904 | prose | pages [22] -->
m

<!-- b004905 | prose | pages [22] -->
m

<!-- b004906 | prose | pages [22] -->
m

<!-- b004907 | prose | pages [22] -->
m

<!-- b004908 | prose | pages [22] -->
m

<!-- b004909 | prose | pages [22] -->
m

<!-- b004910 | prose | pages [22] -->
m

<!-- b004911 | prose | pages [22] -->
m

<!-- b004912 | prose | pages [22] -->
m

<!-- b004913 | prose | pages [22] -->
m

<!-- b004914 | prose | pages [22] -->
m

<!-- b004915 | prose | pages [22] -->
m

<!-- b004916 | prose | pages [22] -->
m

<!-- b004917 | prose | pages [22] -->
m

<!-- b004918 | prose | pages [22] -->
m

<!-- b004919 | prose | pages [22] -->
m

<!-- b004920 | prose | pages [22] -->
m

<!-- b004921 | prose | pages [22] -->
m

<!-- b004922 | prose | pages [22] -->
m

<!-- b004923 | prose | pages [22] -->
m

<!-- b004924 | prose | pages [22] -->
m

<!-- b004925 | prose | pages [22] -->
m

<!-- b004926 | prose | pages [22] -->
m

<!-- b004927 | prose | pages [22] -->
m

<!-- b004928 | prose | pages [22] -->
m

<!-- b004929 | prose | pages [22] -->
m

<!-- b004930 | prose | pages [22] -->
m

<!-- b004931 | prose | pages [22] -->
m

<!-- b004932 | prose | pages [22] -->
m

<!-- b004933 | prose | pages [22] -->
m

<!-- b004934 | prose | pages [22] -->
m

<!-- b004935 | prose | pages [22] -->
m

<!-- b004936 | prose | pages [22] -->
m

<!-- b004937 | prose | pages [22] -->
m

<!-- b004938 | prose | pages [22] -->
m

<!-- b004939 | prose | pages [22] -->
m

<!-- b004940 | prose | pages [22] -->
m

<!-- b004941 | prose | pages [22] -->
m

<!-- b004942 | prose | pages [22] -->
m

<!-- b004943 | prose | pages [22] -->
m

<!-- b004944 | prose | pages [22] -->
m

<!-- b004945 | prose | pages [22] -->
m

<!-- b004946 | prose | pages [22] -->
m

<!-- b004947 | prose | pages [22] -->
m

<!-- b004948 | prose | pages [22] -->
m

<!-- b004949 | prose | pages [22] -->
m

<!-- b004950 | prose | pages [22] -->
m

<!-- b004951 | prose | pages [22] -->
m

<!-- b004952 | prose | pages [22] -->
m

<!-- b004953 | prose | pages [22] -->
m

<!-- b004954 | prose | pages [22] -->
m

<!-- b004955 | prose | pages [22] -->
m

<!-- b004956 | prose | pages [22] -->
m

<!-- b004957 | prose | pages [22] -->
m

<!-- b004958 | prose | pages [22] -->
m

<!-- b004959 | prose | pages [22] -->
m

<!-- b004960 | prose | pages [22] -->
m

<!-- b004961 | prose | pages [22] -->
m

<!-- b004962 | prose | pages [22] -->
m

<!-- b004963 | prose | pages [22] -->
m

<!-- b004964 | prose | pages [22] -->
m

<!-- b004965 | prose | pages [22] -->
m

<!-- b004966 | prose | pages [22] -->
m

<!-- b004967 | prose | pages [22] -->
m

<!-- b004968 | prose | pages [22] -->
m

<!-- b004969 | prose | pages [22] -->
m

<!-- b004970 | prose | pages [22] -->
m

<!-- b004971 | prose | pages [22] -->
m

<!-- b004972 | prose | pages [22] -->
m

<!-- b004973 | prose | pages [22] -->
m

<!-- b004974 | prose | pages [22] -->
m

<!-- b004975 | prose | pages [22] -->
m

<!-- b004976 | prose | pages [22] -->
m

<!-- b004977 | prose | pages [22] -->
m

<!-- b004978 | prose | pages [22] -->
m

<!-- b004979 | prose | pages [22] -->
m

<!-- b004980 | prose | pages [22] -->
m

<!-- b004981 | prose | pages [22] -->
m

<!-- b004982 | prose | pages [22] -->
m

<!-- b004983 | prose | pages [22] -->
m

<!-- b004984 | prose | pages [22] -->
m

<!-- b004985 | prose | pages [22] -->
m

<!-- b004986 | prose | pages [22] -->
m

<!-- b004987 | prose | pages [22] -->
m

<!-- b004988 | prose | pages [22] -->
m

<!-- b004989 | prose | pages [22] -->
m

<!-- b004990 | prose | pages [22] -->
m

<!-- b004991 | prose | pages [22] -->
m

<!-- b004992 | prose | pages [22] -->
m

<!-- b004993 | prose | pages [22] -->
m

<!-- b004994 | prose | pages [22] -->
m

<!-- b004995 | prose | pages [22] -->
m

<!-- b004996 | prose | pages [22] -->
m

<!-- b004997 | prose | pages [22] -->
m

<!-- b004998 | prose | pages [22] -->
m

<!-- b004999 | prose | pages [22] -->
m

<!-- b005000 | prose | pages [22] -->
m

<!-- b005001 | prose | pages [22] -->
m

<!-- b005002 | prose | pages [22] -->
m

<!-- b005003 | prose | pages [22] -->
m

<!-- b005004 | prose | pages [22] -->
m

<!-- b005005 | prose | pages [22] -->
m

<!-- b005006 | prose | pages [22] -->
m

<!-- b005007 | prose | pages [22] -->
Hungary could benefit from investing in a great coach for weightlifting, based on the success of its athletes from 1972 to 1988.

<!-- b005008 | prose | pages [22] -->
m

<!-- b005009 | prose | pages [22] -->
m

<!-- b005010 | prose | pages [22] -->
m

<!-- b005011 | prose | pages [22] -->
m

<!-- b005012 | prose | pages [22] -->
m

<!-- b005013 | prose | pages [22] -->
m

<!-- b005014 | prose | pages [22] -->
m

<!-- b005015 | prose | pages [22] -->
m

<!-- b005016 | prose | pages [22] -->
m

<!-- b005017 | prose | pages [22] -->
m

<!-- b005018 | prose | pages [22] -->
m

<!-- b005019 | prose | pages [22] -->
m

<!-- b005020 | prose | pages [22] -->
m

<!-- b005021 | prose | pages [22] -->
m

<!-- b005022 | prose | pages [22] -->
m

<!-- b005023 | prose | pages [22] -->
m

<!-- b005024 | prose | pages [22] -->
m

<!-- b005025 | prose | pages [22] -->
m

<!-- b005026 | prose | pages [22] -->
m

<!-- b005027 | prose | pages [22] -->
m

<!-- b005028 | prose | pages [22] -->
m

<!-- b005029 | prose | pages [22] -->
m

<!-- b005030 | prose | pages [22] -->
m

<!-- b005031 | prose | pages [22] -->
m

<!-- b005032 | prose | pages [22] -->
m

<!-- b005033 | prose | pages [22] -->
m

<!-- b005034 | prose | pages [22] -->
m

<!-- b005035 | prose | pages [22] -->
m

<!-- b005036 | prose | pages [22] -->
m

<!-- b005037 | prose | pages [22] -->
m

<!-- b005038 | prose | pages [22] -->
m

<!-- b005039 | prose | pages [22] -->
m

<!-- b005040 | prose | pages [22] -->
m

<!-- b005041 | prose | pages [22] -->
m

<!-- b005042 | prose | pages [22] -->
m

<!-- b005043 | prose | pages [22] -->
m

<!-- b005044 | prose | pages [22] -->
m

<!-- b005045 | prose | pages [22] -->
m

<!-- b005046 | prose | pages [22] -->
m

<!-- b005047 | prose | pages [22] -->
m

<!-- b005048 | prose | pages [22] -->
m

<!-- b005049 | prose | pages [22] -->
m

<!-- b005050 | prose | pages [22] -->
m

<!-- b005051 | prose | pages [22] -->
m

<!-- b005052 | prose | pages [22] -->
m

<!-- b005053 | prose | pages [22] -->
m

<!-- b005054 | prose | pages [22] -->
m

<!-- b005055 | prose | pages [22] -->
m

<!-- b005056 | prose | pages [22] -->
m

<!-- b005057 | prose | pages [22] -->
m

<!-- b005058 | prose | pages [22] -->
m

<!-- b005059 | prose | pages [22] -->
m

<!-- b005060 | prose | pages [22] -->
m

<!-- b005061 | prose | pages [22] -->
m

<!-- b005062 | prose | pages [22] -->
m

<!-- b005063 | prose | pages [22] -->
m

<!-- b005064 | prose | pages [22] -->
m

<!-- b005065 | prose | pages [22] -->
m

<!-- b005066 | prose | pages [22] -->
m

<!-- b005067 | prose | pages [22] -->
m

<!-- b005068 | prose | pages [22] -->
m

<!-- b005069 | prose | pages [22] -->
m

<!-- b005070 | prose | pages [22] -->
m

<!-- b005071 | prose | pages [22] -->
m

<!-- b005072 | prose | pages [22] -->
m

<!-- b005073 | prose | pages [22] -->
m

<!-- b005074 | prose | pages [22] -->
m

<!-- b005075 | prose | pages [22] -->
m

<!-- b005076 | prose | pages [22] -->
m

<!-- b005077 | prose | pages [22] -->
m

<!-- b005078 | prose | pages [22] -->
m

<!-- b005079 | prose | pages [22] -->
m

<!-- b005080 | prose | pages [22] -->
m

<!-- b005081 | prose | pages [22] -->
m

<!-- b005082 | prose | pages [22] -->
m

<!-- b005083 | prose | pages [22] -->
m

<!-- b005084 | prose | pages [22] -->
m

<!-- b005085 | prose | pages [22] -->
m

<!-- b005086 | prose | pages [22] -->
m

<!-- b005087 | prose | pages [22] -->
m

<!-- b005088 | prose | pages [22] -->
m

<!-- b005089 | prose | pages [22] -->
m

<!-- b005090 | prose | pages [22] -->
m

<!-- b005091 | prose | pages [22] -->
m

<!-- b005092 | prose | pages [22] -->
m

<!-- b005093 | prose | pages [22] -->
m

<!-- b005094 | prose | pages [22] -->
m

<!-- b005095 | prose | pages [22] -->
m

<!-- b005096 | prose | pages [22] -->
m

<!-- b005097 | prose | pages [22] -->
m

<!-- b005098 | prose | pages [22] -->
m

<!-- b005099 | prose | pages [22] -->
m

<!-- b005100 | prose | pages [22] -->
m

<!-- b005101 | prose | pages [22] -->
m

<!-- b005102 | prose | pages [22] -->
m

<!-- b005103 | prose | pages [22] -->
m

<!-- b005104 | prose | pages [22] -->
m

<!-- b005105 | prose | pages [22] -->
m

<!-- b005106 | prose | pages [22] -->
m

<!-- b005107 | prose | pages [22] -->
m

<!-- b005108 | prose | pages [22] -->
m

<!-- b005109 | prose | pages [22] -->
m

<!-- b005110 | prose | pages [22] -->
m

<!-- b005111 | prose | pages [22] -->
m

<!-- b005112 | prose | pages [22] -->
m

<!-- b005113 | prose | pages [22] -->
m

<!-- b005114 | prose | pages [22] -->
m

<!-- b005115 | prose | pages [22] -->
m

<!-- b005116 | prose | pages [22] -->
m

<!-- b005117 | prose | pages [22] -->
m

<!-- b005118 | prose | pages [22] -->
m

<!-- b005119 | prose | pages [22] -->
m

<!-- b005120 | prose | pages [22] -->
m

<!-- b005121 | prose | pages [22] -->
m

<!-- b005122 | prose | pages [22] -->
m

<!-- b005123 | prose | pages [22] -->
m

<!-- b005124 | prose | pages [22] -->
m

<!-- b005125 | prose | pages [22] -->
m

<!-- b005126 | prose | pages [22] -->
m

<!-- b005127 | prose | pages [22] -->
m

<!-- b005128 | prose | pages [22] -->
m

<!-- b005129 | prose | pages [22] -->
m

<!-- b005130 | prose | pages [22] -->
m

<!-- b005131 | prose | pages [22] -->
m

<!-- b005132 | prose | pages [22] -->
m

<!-- b005133 | prose | pages [22] -->
m

<!-- b005134 | prose | pages [22] -->
m

<!-- b005135 | prose | pages [22] -->
m

<!-- b005136 | prose | pages [22] -->
m

<!-- b005137 | prose | pages [22] -->
m

<!-- b005138 | prose | pages [22] -->
m

<!-- b005139 | prose | pages [22] -->
m

<!-- b005140 | prose | pages [22] -->
m

<!-- b005141 | prose | pages [22] -->
m

<!-- b005142 | prose | pages [22] -->
m

<!-- b005143 | prose | pages [22] -->
m

<!-- b005144 | prose | pages [22] -->
m

<!-- b005145 | prose | pages [22] -->
m

<!-- b005146 | prose | pages [22] -->
m

<!-- b005147 | prose | pages [22] -->
m

<!-- b005148 | prose | pages [22] -->
m

<!-- b005149 | prose | pages [22] -->
m

<!-- b005150 | prose | pages [22] -->
m

<!-- b005151 | prose | pages [22] -->
m

<!-- b005152 | prose | pages [22] -->
m

<!-- b005153 | prose | pages [22] -->
m

<!-- b005154 | prose | pages [22] -->
m

<!-- b005155 | prose | pages [22] -->
m

<!-- b005156 | prose | pages [22] -->
m

<!-- b005157 | prose | pages [22] -->
m

<!-- b005158 | prose | pages [22] -->
m

<!-- b005159 | prose | pages [22] -->
m

<!-- b005160 | prose | pages [22] -->
m

<!-- b005161 | prose | pages [22] -->
m

<!-- b005162 | prose | pages [22] -->
m

<!-- b005163 | prose | pages [22] -->
m

<!-- b005164 | prose | pages [22] -->
m

<!-- b005165 | prose | pages [22] -->
m

<!-- b005166 | prose | pages [22] -->
m

<!-- b005167 | prose | pages [22] -->
m

<!-- b005168 | prose | pages [22] -->
m

<!-- b005169 | prose | pages [22] -->
m

<!-- b005170 | prose | pages [22] -->
m

<!-- b005171 | prose | pages [22] -->
m

<!-- b005172 | prose | pages [22] -->
m

<!-- b005173 | prose | pages [22] -->
m

<!-- b005174 | prose | pages [22] -->
m

<!-- b005175 | prose | pages [22] -->
m

<!-- b005176 | prose | pages [22] -->
m

<!-- b005177 | prose | pages [22] -->
m

<!-- b005178 | prose | pages [22] -->
m

<!-- b005179 | prose | pages [22] -->
m

<!-- b005180 | prose | pages [22] -->
m

<!-- b005181 | prose | pages [22] -->
m

<!-- b005182 | prose | pages [22] -->
m

<!-- b005183 | prose | pages [22] -->
m

<!-- b005184 | prose | pages [22] -->
m

<!-- b005185 | prose | pages [22] -->
m

<!-- b005186 | prose | pages [22] -->
m

<!-- b005187 | prose | pages [22] -->
m

<!-- b005188 | prose | pages [22] -->
m

<!-- b005189 | prose | pages [22] -->
m

<!-- b005190 | prose | pages [22] -->
m

<!-- b005191 | prose | pages [22] -->
m

<!-- b005192 | prose | pages [22] -->
m

<!-- b005193 | prose | pages [22] -->
m

<!-- b005194 | prose | pages [22] -->
m

<!-- b005195 | prose | pages [22] -->
m

<!-- b005196 | prose | pages [22] -->
m

<!-- b005197 | prose | pages [22] -->
m

<!-- b005198 | prose | pages [22] -->
m

<!-- b005199 | prose | pages [22] -->
m

<!-- b005200 | prose | pages [22] -->
m

<!-- b005201 | prose | pages [22] -->
m

<!-- b005202 | prose | pages [22] -->
m

<!-- b005203 | prose | pages [22] -->
m

<!-- b005204 | prose | pages [22] -->
m

<!-- b005205 | prose | pages [22] -->
m

<!-- b005206 | prose | pages [22] -->
m

<!-- b005207 | prose | pages [22] -->
m

<!-- b005208 | prose | pages [22] -->
m

<!-- b005209 | prose | pages [22] -->
m

<!-- b005210 | prose | pages [22] -->
m

<!-- b005211 | prose | pages [22] -->
m

<!-- b005212 | prose | pages [22] -->
m

<!-- b005213 | prose | pages [22] -->
m

<!-- b005214 | prose | pages [22] -->
m

<!-- b005215 | prose | pages [22] -->
m

<!-- b005216 | prose | pages [22] -->
m

<!-- b005217 | prose | pages [22] -->
m

<!-- b005218 | prose | pages [22] -->
m

<!-- b005219 | prose | pages [22] -->
m

<!-- b005220 | prose | pages [22] -->
m

<!-- b005221 | prose | pages [22] -->
m

<!-- b005222 | prose | pages [22] -->
m

<!-- b005223 | prose | pages [22] -->
m

<!-- b005224 | prose | pages [22] -->
m

<!-- b005225 | prose | pages [22] -->
m

<!-- b005226 | prose | pages [22] -->
m

<!-- b005227 | prose | pages [22] -->
m

<!-- b005228 | prose | pages [22] -->
m

<!-- b005229 | prose | pages [22] -->
m

<!-- b005230 | prose | pages [22] -->
m

<!-- b005231 | prose | pages [22] -->
m

<!-- b005232 | prose | pages [22] -->
m

<!-- b005233 | prose | pages [22] -->
m

<!-- b005234 | prose | pages [22] -->
m

<!-- b005235 | prose | pages [22] -->
m

<!-- b005236 | prose | pages [22] -->
m

<!-- b005237 | prose | pages [22] -->
m

<!-- b005238 | prose | pages [22] -->
m

<!-- b005239 | prose | pages [22] -->
m

<!-- b005240 | prose | pages [22] -->
m

<!-- b005241 | prose | pages [22] -->
m

<!-- b005242 | prose | pages [22] -->
m

<!-- b005243 | prose | pages [22] -->
m

<!-- b005244 | prose | pages [22] -->
m

<!-- b005245 | prose | pages [22] -->
m

<!-- b005246 | prose | pages [22] -->
m

<!-- b005247 | prose | pages [22] -->
m

<!-- b005248 | prose | pages [22] -->
m

<!-- b005249 | prose | pages [22] -->
m

<!-- b005250 | prose | pages [22] -->
m

<!-- b005251 | prose | pages [22] -->
m

<!-- b005252 | prose | pages [22] -->
m

<!-- b005253 | prose | pages [22] -->
m

<!-- b005254 | prose | pages [22] -->
m

<!-- b005255 | prose | pages [22] -->
m

<!-- b005256 | prose | pages [22] -->
m

<!-- b005257 | prose | pages [22] -->
m

<!-- b005258 | prose | pages [22] -->
m

<!-- b005259 | prose | pages [22] -->
m

<!-- b005260 | prose | pages [22] -->
m

<!-- b005261 | prose | pages [22] -->
m

<!-- b005262 | prose | pages [22] -->
m

<!-- b005263 | prose | pages [22] -->
m

<!-- b005264 | prose | pages [22] -->
m

<!-- b005265 | prose | pages [22] -->
m

<!-- b005266 | prose | pages [22] -->
m

<!-- b005267 | prose | pages [22] -->
m

<!-- b005268 | prose | pages [22] -->
m

<!-- b005269 | prose | pages [22] -->
m

<!-- b005270 | prose | pages [22] -->
m

<!-- b005271 | prose | pages [22] -->
m

<!-- b005272 | prose | pages [22] -->
m

<!-- b005273 | prose | pages [22] -->
m

<!-- b005274 | prose | pages [22] -->
m

<!-- b005275 | prose | pages [22] -->
m

<!-- b005276 | prose | pages [22] -->
m

<!-- b005277 | prose | pages [22] -->
m

<!-- b005278 | prose | pages [22] -->
m

<!-- b005279 | prose | pages [22] -->
m

<!-- b005280 | prose | pages [22] -->
m

<!-- b005281 | prose | pages [22] -->
m

<!-- b005282 | prose | pages [22] -->
m

<!-- b005283 | prose | pages [22] -->
Outside of these three countries, it seems that weightlifting and trampolining are especially high return-on-

<!-- b005284 | prose | pages [22] -->
m

<!-- b005285 | prose | pages [22] -->
m

<!-- b005286 | prose | pages [22] -->
m

<!-- b005287 | prose | pages [22] -->
m

<!-- b005288 | prose | pages [22] -->
m

<!-- b005289 | prose | pages [22] -->
m

<!-- b005290 | prose | pages [22] -->
m

<!-- b005291 | prose | pages [22] -->
m

<!-- b005292 | prose | pages [22] -->
m

<!-- b005293 | prose | pages [22] -->
m

<!-- b005294 | prose | pages [22] -->
m

<!-- b005295 | prose | pages [22] -->
m

<!-- b005296 | prose | pages [22] -->
m

<!-- b005297 | prose | pages [22] -->
m

<!-- b005298 | prose | pages [22] -->
m

<!-- b005299 | prose | pages [22] -->
m

<!-- b005300 | prose | pages [22] -->
m

<!-- b005301 | prose | pages [22] -->
m

<!-- b005302 | prose | pages [22] -->
m

<!-- b005303 | prose | pages [22] -->
m

<!-- b005304 | prose | pages [22] -->
m

<!-- b005305 | prose | pages [22] -->
m

<!-- b005306 | prose | pages [22] -->
m

<!-- b005307 | prose | pages [22] -->
m

<!-- b005308 | prose | pages [22] -->
m

<!-- b005309 | prose | pages [22] -->
interest investments for great coaches, as they both appeared twice in this list of the highest values added by great coaches.

<!-- b005310 | prose | pages [22] -->
Conveniently, these ∆Pnorm are precisely the predicted points that these countries would gain if they invested in great coaches: we predict that Russia’s investing in a great weightlifting coach could lead to up to 20 points, that China’s investing in a great trampolining coach could lead to up to 14 points, and that Hungary’s investing in a great weightlifting coach could lead to up to 6.8 points.

<!-- b005311 | prose | pages [22] -->
Problem 3: Insights into Olympic Medal Counts 5

<!-- b005312 | prose | pages [22] -->
Purely based on the regression results, it is clear that the United States dominating is sensible given their previous record and their host status in 2028. Some unexpected results include Germany and China’s performance,

<!-- b005313 | prose | pages [22] -->
关注数学模型

<!-- b005314 | furniture | pages [22] -->
2

<!-- b005315 | furniture | pages [22] -->
MATHmodels

<!-- b005316 | furniture | pages [22] -->
获取更多资讯

<!-- b005317 | furniture | pages [23] -->
Team 2522820

<!-- b005318 | furniture | pages [23] -->
Page 23

<!-- b005319 | prose | pages [23] -->
as China worsened in medal count quite a bit from 2024 and Germany came out of nowhere to take second place in gold medals. There are multitudes more observations like this to make, and they can be predicted to be due to any amount of reasons. Since the model accounts for unobserved effects, it’s entirely possible that this is representative of some culture change or effect of China’s governmental policy, or really anything under the sun

<!-- b005320 | prose | pages [23] -->
微信公众号：数学模型

<!-- b005321 | prose | pages [23] -->
that can be thought up.

<!-- b005322 | prose | pages [23] -->
Though we tried our best to predict the medal counts, there is a large confidence interval associated with the predictions, so in the end it is likely true that Number of Athletes, Host Status, and Past Performance are not sufficient indicators (at least through our method of regression) of Olympic medal performance. We suspect this is due to a lack of an economic/political factor, since that understandably has a major impact and there has been many cases where politics (such as political regimes) have affected the outcome of the Olympics much more than these predictors have. In addition, for developing countries (especially ones on track to earn their first medal), economic factors are many times more important than number of athletes or past performance, and countries at this level will definitely not be hosting. There is a large discrepancy in the number of countries performing poorly at the Olympics. An interesting question is whether this is a good thing or a bad thing: does the dominance of the United States and other developed countries motivate or demotivate developing countries

<!-- b005323 | prose | pages [23] -->
微信号：MATHmodels

<!-- b005324 | prose | pages [23] -->
to try to place in future Olympics? From a first world perspective, it may seem like we are giving them a chance to participate, and we are definitely doing so for the select few great talents from these countries. However, resources are overwhelmingly skewed for developed countries as are medal counts, as is especially highlighted in our 2028 predictions. Is it not in the interest of both high caliber players and coaches to gravitate towards where these resources are concentrated? The Olympic Committee should carefully consider how sports are chosen and how resources are allocated (to the extent they can), as this is very influential to the medal distribution.

<!-- b005325 | prose | pages [23] -->
6

<!-- b005326 | heading | pages [23] -->
Strengths and Weaknesses

<!-- b005327 | prose | pages [23] -->
6.1

<!-- b005328 | heading | pages [23] -->
Hierarchical Regression Model

<!-- b005329 | prose | pages [23] -->
A strength of our model is that, by implementing mixed effects and clusters, it is able to account for various levels of unobserved random effects that can influence medal counts. There are many factors that influence how a country performs at the individual competitor level or national level, so many that we cannot account for them all. So, our model implements random variables at the cluster and individual country level for each parameter to attempt to account for this, allowing for a more realistic prediction that isn’t just purely data driven. In addition, our model appropriately accounts for the zero-inflation/censoring of Olympic medal data by using a Hurdle model approach with a probit regression to find probability of earning 0 medals or not.

<!-- b005330 | prose | pages [23] -->
One weakness about this model is it’s fit. Maximizing the Log Likelihood function would lead to a good fit, but during implementation the optimization did not converge for many methods of optimization. This inevitably led to log likelihoods and AIC/BIC fits that were subpar. Though we tried to account for this by weighting one of the clusters to reduce heteroscedasticity, it didn’t help the convergence issue. This may imply the nature of the data is different from how our model assumes it to be (in fact it is, since we tested the data to still be heteroscedastic even after improvements). One improvement we explored was to use a Hamiltonian Monte Carlo optimization to replace MLE, but this approach did not end up working. Some approach that accounts for the heteroscedasticity error would improve the model significantly.

<!-- b005331 | prose | pages [23] -->
6.2

<!-- b005332 | heading | pages [23] -->
Time Series Analysis with Moving Average Model

<!-- b005333 | prose | pages [23] -->
Our model’s main strength lies in its moving average, which allowed us to interpret anomalous performances in the context of performances immediately before and after it. This, in turn, allowed us to create segments of increased performance, which we interpreted as possible signs of the great coach effect. This was much

<!-- b005334 | prose | pages [23] -->
m

<!-- b005335 | prose | pages [23] -->
m

<!-- b005336 | prose | pages [23] -->
m

<!-- b005337 | prose | pages [23] -->
m

<!-- b005338 | prose | pages [23] -->
m

<!-- b005339 | prose | pages [23] -->
m

<!-- b005340 | prose | pages [23] -->
m

<!-- b005341 | prose | pages [23] -->
m

<!-- b005342 | prose | pages [23] -->
m

<!-- b005343 | prose | pages [23] -->
m

<!-- b005344 | prose | pages [23] -->
m

<!-- b005345 | prose | pages [23] -->
m

<!-- b005346 | prose | pages [23] -->
m

<!-- b005347 | prose | pages [23] -->
m

<!-- b005348 | prose | pages [23] -->
m

<!-- b005349 | prose | pages [23] -->
m

<!-- b005350 | prose | pages [23] -->
m

<!-- b005351 | prose | pages [23] -->
m

<!-- b005352 | prose | pages [23] -->
m

<!-- b005353 | prose | pages [23] -->
m

<!-- b005354 | prose | pages [23] -->
m

<!-- b005355 | prose | pages [23] -->
m

<!-- b005356 | prose | pages [23] -->
m

<!-- b005357 | prose | pages [23] -->
m

<!-- b005358 | prose | pages [23] -->
m

<!-- b005359 | prose | pages [23] -->
m

<!-- b005360 | prose | pages [23] -->
m

<!-- b005361 | prose | pages [23] -->
m

<!-- b005362 | prose | pages [23] -->
m

<!-- b005363 | prose | pages [23] -->
m

<!-- b005364 | prose | pages [23] -->
m

<!-- b005365 | prose | pages [23] -->
m

<!-- b005366 | prose | pages [23] -->
m

<!-- b005367 | prose | pages [23] -->
m

<!-- b005368 | prose | pages [23] -->
m

<!-- b005369 | prose | pages [23] -->
m

<!-- b005370 | prose | pages [23] -->
m

<!-- b005371 | prose | pages [23] -->
m

<!-- b005372 | prose | pages [23] -->
m

<!-- b005373 | prose | pages [23] -->
m

<!-- b005374 | prose | pages [23] -->
m

<!-- b005375 | prose | pages [23] -->
m

<!-- b005376 | prose | pages [23] -->
m

<!-- b005377 | prose | pages [23] -->
m

<!-- b005378 | prose | pages [23] -->
m

<!-- b005379 | prose | pages [23] -->
m

<!-- b005380 | prose | pages [23] -->
m

<!-- b005381 | prose | pages [23] -->
m

<!-- b005382 | prose | pages [23] -->
m

<!-- b005383 | prose | pages [23] -->
m

<!-- b005384 | prose | pages [23] -->
m

<!-- b005385 | prose | pages [23] -->
m

<!-- b005386 | prose | pages [23] -->
m

<!-- b005387 | prose | pages [23] -->
m

<!-- b005388 | prose | pages [23] -->
m

<!-- b005389 | prose | pages [23] -->
m

<!-- b005390 | prose | pages [23] -->
m

<!-- b005391 | prose | pages [23] -->
m

<!-- b005392 | prose | pages [23] -->
m

<!-- b005393 | prose | pages [23] -->
m

<!-- b005394 | prose | pages [23] -->
m

<!-- b005395 | prose | pages [23] -->
m

<!-- b005396 | prose | pages [23] -->
m

<!-- b005397 | prose | pages [23] -->
m

<!-- b005398 | prose | pages [23] -->
m

<!-- b005399 | prose | pages [23] -->
m

<!-- b005400 | prose | pages [23] -->
m

<!-- b005401 | prose | pages [23] -->
m

<!-- b005402 | prose | pages [23] -->
m

<!-- b005403 | prose | pages [23] -->
m

<!-- b005404 | prose | pages [23] -->
m

<!-- b005405 | prose | pages [23] -->
m

<!-- b005406 | prose | pages [23] -->
m

<!-- b005407 | prose | pages [23] -->
m

<!-- b005408 | prose | pages [23] -->
m

<!-- b005409 | prose | pages [23] -->
m

<!-- b005410 | prose | pages [23] -->
m

<!-- b005411 | prose | pages [23] -->
m

<!-- b005412 | prose | pages [23] -->
m

<!-- b005413 | prose | pages [23] -->
m

<!-- b005414 | prose | pages [23] -->
m

<!-- b005415 | prose | pages [23] -->
m

<!-- b005416 | prose | pages [23] -->
m

<!-- b005417 | prose | pages [23] -->
m

<!-- b005418 | prose | pages [23] -->
m

<!-- b005419 | prose | pages [23] -->
m

<!-- b005420 | prose | pages [23] -->
m

<!-- b005421 | prose | pages [23] -->
m

<!-- b005422 | prose | pages [23] -->
m

<!-- b005423 | prose | pages [23] -->
m

<!-- b005424 | prose | pages [23] -->
m

<!-- b005425 | prose | pages [23] -->
m

<!-- b005426 | prose | pages [23] -->
m

<!-- b005427 | prose | pages [23] -->
m

<!-- b005428 | prose | pages [23] -->
m

<!-- b005429 | prose | pages [23] -->
m

<!-- b005430 | prose | pages [23] -->
m

<!-- b005431 | prose | pages [23] -->
m

<!-- b005432 | prose | pages [23] -->
m

<!-- b005433 | prose | pages [23] -->
m

<!-- b005434 | prose | pages [23] -->
m

<!-- b005435 | prose | pages [23] -->
m

<!-- b005436 | prose | pages [23] -->
m

<!-- b005437 | prose | pages [23] -->
m

<!-- b005438 | prose | pages [23] -->
m

<!-- b005439 | prose | pages [23] -->
m

<!-- b005440 | prose | pages [23] -->
m

<!-- b005441 | prose | pages [23] -->
m

<!-- b005442 | prose | pages [23] -->
m

<!-- b005443 | prose | pages [23] -->
m

<!-- b005444 | prose | pages [23] -->
m

<!-- b005445 | prose | pages [23] -->
m

<!-- b005446 | prose | pages [23] -->
m

<!-- b005447 | prose | pages [23] -->
m

<!-- b005448 | prose | pages [23] -->
m

<!-- b005449 | prose | pages [23] -->
m

<!-- b005450 | prose | pages [23] -->
m

<!-- b005451 | prose | pages [23] -->
m

<!-- b005452 | prose | pages [23] -->
m

<!-- b005453 | prose | pages [23] -->
m

<!-- b005454 | prose | pages [23] -->
m

<!-- b005455 | prose | pages [23] -->
m

<!-- b005456 | prose | pages [23] -->
m

<!-- b005457 | prose | pages [23] -->
m

<!-- b005458 | prose | pages [23] -->
m

<!-- b005459 | prose | pages [23] -->
m

<!-- b005460 | prose | pages [23] -->
m

<!-- b005461 | prose | pages [23] -->
m

<!-- b005462 | prose | pages [23] -->
m

<!-- b005463 | prose | pages [23] -->
m

<!-- b005464 | prose | pages [23] -->
m

<!-- b005465 | prose | pages [23] -->
m

<!-- b005466 | prose | pages [23] -->
m

<!-- b005467 | prose | pages [23] -->
m

<!-- b005468 | prose | pages [23] -->
m

<!-- b005469 | prose | pages [23] -->
m

<!-- b005470 | prose | pages [23] -->
m

<!-- b005471 | prose | pages [23] -->
m

<!-- b005472 | prose | pages [23] -->
m

<!-- b005473 | prose | pages [23] -->
m

<!-- b005474 | prose | pages [23] -->
m

<!-- b005475 | prose | pages [23] -->
m

<!-- b005476 | prose | pages [23] -->
m

<!-- b005477 | prose | pages [23] -->
m

<!-- b005478 | prose | pages [23] -->
m

<!-- b005479 | prose | pages [23] -->
m

<!-- b005480 | prose | pages [23] -->
m

<!-- b005481 | prose | pages [23] -->
m

<!-- b005482 | prose | pages [23] -->
m

<!-- b005483 | prose | pages [23] -->
m

<!-- b005484 | prose | pages [23] -->
m

<!-- b005485 | prose | pages [23] -->
m

<!-- b005486 | prose | pages [23] -->
m

<!-- b005487 | prose | pages [23] -->
m

<!-- b005488 | prose | pages [23] -->
m

<!-- b005489 | prose | pages [23] -->
m

<!-- b005490 | prose | pages [23] -->
m

<!-- b005491 | prose | pages [23] -->
m

<!-- b005492 | prose | pages [23] -->
m

<!-- b005493 | prose | pages [23] -->
m

<!-- b005494 | prose | pages [23] -->
m

<!-- b005495 | prose | pages [23] -->
m

<!-- b005496 | prose | pages [23] -->
m

<!-- b005497 | prose | pages [23] -->
m

<!-- b005498 | prose | pages [23] -->
m

<!-- b005499 | prose | pages [23] -->
m

<!-- b005500 | prose | pages [23] -->
m

<!-- b005501 | prose | pages [23] -->
m

<!-- b005502 | prose | pages [23] -->
m

<!-- b005503 | prose | pages [23] -->
m

<!-- b005504 | prose | pages [23] -->
m

<!-- b005505 | prose | pages [23] -->
m

<!-- b005506 | prose | pages [23] -->
m

<!-- b005507 | prose | pages [23] -->
m

<!-- b005508 | prose | pages [23] -->
m

<!-- b005509 | prose | pages [23] -->
m

<!-- b005510 | prose | pages [23] -->
m

<!-- b005511 | prose | pages [23] -->
m

<!-- b005512 | prose | pages [23] -->
m

<!-- b005513 | prose | pages [23] -->
m

<!-- b005514 | prose | pages [23] -->
m

<!-- b005515 | prose | pages [23] -->
m

<!-- b005516 | prose | pages [23] -->
m

<!-- b005517 | prose | pages [23] -->
m

<!-- b005518 | prose | pages [23] -->
m

<!-- b005519 | prose | pages [23] -->
m

<!-- b005520 | prose | pages [23] -->
m

<!-- b005521 | prose | pages [23] -->
m

<!-- b005522 | prose | pages [23] -->
m

<!-- b005523 | prose | pages [23] -->
m

<!-- b005524 | prose | pages [23] -->
m

<!-- b005525 | prose | pages [23] -->
m

<!-- b005526 | prose | pages [23] -->
m

<!-- b005527 | prose | pages [23] -->
m

<!-- b005528 | prose | pages [23] -->
m

<!-- b005529 | prose | pages [23] -->
m

<!-- b005530 | prose | pages [23] -->
m

<!-- b005531 | prose | pages [23] -->
m

<!-- b005532 | prose | pages [23] -->
m

<!-- b005533 | prose | pages [23] -->
m

<!-- b005534 | prose | pages [23] -->
m

<!-- b005535 | prose | pages [23] -->
m

<!-- b005536 | prose | pages [23] -->
m

<!-- b005537 | prose | pages [23] -->
m

<!-- b005538 | prose | pages [23] -->
m

<!-- b005539 | prose | pages [23] -->
m

<!-- b005540 | prose | pages [23] -->
m

<!-- b005541 | prose | pages [23] -->
m

<!-- b005542 | prose | pages [23] -->
m

<!-- b005543 | prose | pages [23] -->
m

<!-- b005544 | prose | pages [23] -->
m

<!-- b005545 | prose | pages [23] -->
m

<!-- b005546 | prose | pages [23] -->
m

<!-- b005547 | prose | pages [23] -->
m

<!-- b005548 | prose | pages [23] -->
m

<!-- b005549 | prose | pages [23] -->
m

<!-- b005550 | prose | pages [23] -->
m

<!-- b005551 | prose | pages [23] -->
m

<!-- b005552 | prose | pages [23] -->
m

<!-- b005553 | prose | pages [23] -->
m

<!-- b005554 | prose | pages [23] -->
m

<!-- b005555 | prose | pages [23] -->
m

<!-- b005556 | prose | pages [23] -->
m

<!-- b005557 | prose | pages [23] -->
m

<!-- b005558 | prose | pages [23] -->
m

<!-- b005559 | prose | pages [23] -->
m

<!-- b005560 | prose | pages [23] -->
m

<!-- b005561 | prose | pages [23] -->
m

<!-- b005562 | prose | pages [23] -->
m

<!-- b005563 | prose | pages [23] -->
m

<!-- b005564 | prose | pages [23] -->
m

<!-- b005565 | prose | pages [23] -->
m

<!-- b005566 | prose | pages [23] -->
m

<!-- b005567 | prose | pages [23] -->
m

<!-- b005568 | prose | pages [23] -->
m

<!-- b005569 | prose | pages [23] -->
m

<!-- b005570 | prose | pages [23] -->
m

<!-- b005571 | prose | pages [23] -->
m

<!-- b005572 | prose | pages [23] -->
m

<!-- b005573 | prose | pages [23] -->
m

<!-- b005574 | prose | pages [23] -->
m

<!-- b005575 | prose | pages [23] -->
m

<!-- b005576 | prose | pages [23] -->
m

<!-- b005577 | prose | pages [23] -->
m

<!-- b005578 | prose | pages [23] -->
m

<!-- b005579 | prose | pages [23] -->
m

<!-- b005580 | prose | pages [23] -->
m

<!-- b005581 | prose | pages [23] -->
m

<!-- b005582 | prose | pages [23] -->
m

<!-- b005583 | prose | pages [23] -->
m

<!-- b005584 | prose | pages [23] -->
m

<!-- b005585 | prose | pages [23] -->
m

<!-- b005586 | prose | pages [23] -->
m

<!-- b005587 | prose | pages [23] -->
m

<!-- b005588 | prose | pages [23] -->
m

<!-- b005589 | prose | pages [23] -->
m

<!-- b005590 | prose | pages [23] -->
m

<!-- b005591 | prose | pages [23] -->
m

<!-- b005592 | prose | pages [23] -->
m

<!-- b005593 | prose | pages [23] -->
m

<!-- b005594 | prose | pages [23] -->
m

<!-- b005595 | prose | pages [23] -->
m

<!-- b005596 | prose | pages [23] -->
m

<!-- b005597 | prose | pages [23] -->
m

<!-- b005598 | prose | pages [23] -->
m

<!-- b005599 | prose | pages [23] -->
m

<!-- b005600 | prose | pages [23] -->
m

<!-- b005601 | prose | pages [23] -->
m

<!-- b005602 | prose | pages [23] -->
m

<!-- b005603 | prose | pages [23] -->
m

<!-- b005604 | prose | pages [23] -->
m

<!-- b005605 | prose | pages [23] -->
m

<!-- b005606 | prose | pages [23] -->
m

<!-- b005607 | prose | pages [23] -->
m

<!-- b005608 | prose | pages [23] -->
m

<!-- b005609 | prose | pages [23] -->
m

<!-- b005610 | prose | pages [23] -->
m

<!-- b005611 | prose | pages [23] -->
m

<!-- b005612 | prose | pages [23] -->
m

<!-- b005613 | prose | pages [23] -->
m

<!-- b005614 | prose | pages [23] -->
m

<!-- b005615 | prose | pages [23] -->
m

<!-- b005616 | prose | pages [23] -->
m

<!-- b005617 | prose | pages [23] -->
m

<!-- b005618 | furniture | pages [23] -->
m

<!-- b005619 | furniture | pages [23] -->
m

<!-- b005620 | furniture | pages [23] -->
m

<!-- b005621 | furniture | pages [23] -->
m

<!-- b005622 | furniture | pages [23] -->
m

<!-- b005623 | furniture | pages [23] -->
m

<!-- b005624 | furniture | pages [23] -->
m

<!-- b005625 | furniture | pages [23] -->
m

<!-- b005626 | furniture | pages [23] -->
m

<!-- b005627 | furniture | pages [23] -->
m

<!-- b005628 | furniture | pages [23] -->
m

<!-- b005629 | furniture | pages [23] -->
m

<!-- b005630 | furniture | pages [23] -->
m

<!-- b005631 | furniture | pages [23] -->
m

<!-- b005632 | furniture | pages [23] -->
m

<!-- b005633 | furniture | pages [23] -->
m

<!-- b005634 | furniture | pages [23] -->
m

<!-- b005635 | furniture | pages [23] -->
m

<!-- b005636 | furniture | pages [23] -->
m

<!-- b005637 | furniture | pages [23] -->
m

<!-- b005638 | furniture | pages [23] -->
m

<!-- b005639 | furniture | pages [23] -->
m

<!-- b005640 | furniture | pages [23] -->
m

<!-- b005641 | furniture | pages [23] -->
m

<!-- b005642 | furniture | pages [23] -->
m

<!-- b005643 | furniture | pages [23] -->
m

<!-- b005644 | furniture | pages [23] -->
m

<!-- b005645 | furniture | pages [23] -->
m

<!-- b005646 | furniture | pages [23] -->
m

<!-- b005647 | furniture | pages [23] -->
m

<!-- b005648 | furniture | pages [23] -->
m

<!-- b005649 | furniture | pages [23] -->
m

<!-- b005650 | furniture | pages [23] -->
m

<!-- b005651 | furniture | pages [23] -->
m

<!-- b005652 | furniture | pages [23] -->
m

<!-- b005653 | furniture | pages [23] -->
m

<!-- b005654 | furniture | pages [23] -->
m

<!-- b005655 | furniture | pages [23] -->
m

<!-- b005656 | furniture | pages [23] -->
m

<!-- b005657 | furniture | pages [23] -->
m

<!-- b005658 | furniture | pages [23] -->
m

<!-- b005659 | furniture | pages [23] -->
m

<!-- b005660 | furniture | pages [23] -->
m

<!-- b005661 | furniture | pages [23] -->
m

<!-- b005662 | furniture | pages [23] -->
m

<!-- b005663 | furniture | pages [23] -->
m

<!-- b005664 | furniture | pages [23] -->
m

<!-- b005665 | furniture | pages [23] -->
m

<!-- b005666 | furniture | pages [23] -->
m

<!-- b005667 | furniture | pages [23] -->
m

<!-- b005668 | furniture | pages [23] -->
m

<!-- b005669 | furniture | pages [23] -->
m

<!-- b005670 | furniture | pages [23] -->
m

<!-- b005671 | furniture | pages [23] -->
m

<!-- b005672 | furniture | pages [23] -->
m

<!-- b005673 | furniture | pages [23] -->
m

<!-- b005674 | furniture | pages [23] -->
m

<!-- b005675 | furniture | pages [23] -->
m

<!-- b005676 | furniture | pages [23] -->
m

<!-- b005677 | furniture | pages [23] -->
m

<!-- b005678 | furniture | pages [23] -->
m

<!-- b005679 | furniture | pages [23] -->
m

<!-- b005680 | furniture | pages [23] -->
m

<!-- b005681 | furniture | pages [23] -->
m

<!-- b005682 | furniture | pages [23] -->
m

<!-- b005683 | furniture | pages [23] -->
m

<!-- b005684 | furniture | pages [23] -->
m

<!-- b005685 | furniture | pages [23] -->
m

<!-- b005686 | furniture | pages [23] -->
m

<!-- b005687 | furniture | pages [23] -->
m

<!-- b005688 | furniture | pages [23] -->
m

<!-- b005689 | furniture | pages [23] -->
m

<!-- b005690 | furniture | pages [23] -->
m

<!-- b005691 | furniture | pages [23] -->
m

<!-- b005692 | furniture | pages [23] -->
m

<!-- b005693 | furniture | pages [23] -->
m

<!-- b005694 | furniture | pages [23] -->
m

<!-- b005695 | furniture | pages [23] -->
m

<!-- b005696 | furniture | pages [23] -->
m

<!-- b005697 | furniture | pages [23] -->
m

<!-- b005698 | furniture | pages [23] -->
m

<!-- b005699 | furniture | pages [23] -->
m

<!-- b005700 | furniture | pages [23] -->
m

<!-- b005701 | furniture | pages [23] -->
m

<!-- b005702 | furniture | pages [23] -->
m

<!-- b005703 | furniture | pages [23] -->
m

<!-- b005704 | furniture | pages [23] -->
m

<!-- b005705 | furniture | pages [23] -->
m

<!-- b005706 | furniture | pages [23] -->
m

<!-- b005707 | furniture | pages [23] -->
m

<!-- b005708 | furniture | pages [23] -->
m

<!-- b005709 | furniture | pages [23] -->
m

<!-- b005710 | furniture | pages [23] -->
m

<!-- b005711 | furniture | pages [23] -->
m

<!-- b005712 | furniture | pages [23] -->
m

<!-- b005713 | furniture | pages [23] -->
m

<!-- b005714 | furniture | pages [23] -->
m

<!-- b005715 | furniture | pages [23] -->
m

<!-- b005716 | furniture | pages [23] -->
m

<!-- b005717 | furniture | pages [23] -->
m

<!-- b005718 | furniture | pages [23] -->
m

<!-- b005719 | furniture | pages [23] -->
m

<!-- b005720 | furniture | pages [23] -->
m

<!-- b005721 | furniture | pages [23] -->
m

<!-- b005722 | furniture | pages [23] -->
m

<!-- b005723 | furniture | pages [23] -->
m

<!-- b005724 | furniture | pages [23] -->
m

<!-- b005725 | furniture | pages [23] -->
m

<!-- b005726 | furniture | pages [23] -->
m

<!-- b005727 | furniture | pages [23] -->
m

<!-- b005728 | furniture | pages [23] -->
m

<!-- b005729 | furniture | pages [23] -->
m

<!-- b005730 | furniture | pages [23] -->
m

<!-- b005731 | furniture | pages [23] -->
m

<!-- b005732 | furniture | pages [23] -->
m

<!-- b005733 | furniture | pages [23] -->
m

<!-- b005734 | furniture | pages [23] -->
m

<!-- b005735 | furniture | pages [23] -->
m

<!-- b005736 | furniture | pages [23] -->
m

<!-- b005737 | furniture | pages [23] -->
m

<!-- b005738 | furniture | pages [23] -->
m

<!-- b005739 | furniture | pages [23] -->
m

<!-- b005740 | furniture | pages [23] -->
m

<!-- b005741 | furniture | pages [23] -->
m

<!-- b005742 | furniture | pages [23] -->
m

<!-- b005743 | furniture | pages [23] -->
m

<!-- b005744 | furniture | pages [23] -->
m

<!-- b005745 | furniture | pages [23] -->
m

<!-- b005746 | furniture | pages [23] -->
m

<!-- b005747 | furniture | pages [23] -->
m

<!-- b005748 | furniture | pages [23] -->
m

<!-- b005749 | furniture | pages [23] -->
m

<!-- b005750 | furniture | pages [23] -->
m

<!-- b005751 | furniture | pages [23] -->
m

<!-- b005752 | furniture | pages [23] -->
m

<!-- b005753 | furniture | pages [23] -->
m

<!-- b005754 | furniture | pages [23] -->
m

<!-- b005755 | furniture | pages [23] -->
m

<!-- b005756 | furniture | pages [23] -->
m

<!-- b005757 | furniture | pages [23] -->
m

<!-- b005758 | furniture | pages [23] -->
m

<!-- b005759 | furniture | pages [23] -->
m

<!-- b005760 | furniture | pages [23] -->
m

<!-- b005761 | furniture | pages [23] -->
m

<!-- b005762 | furniture | pages [23] -->
m

<!-- b005763 | furniture | pages [23] -->
m

<!-- b005764 | furniture | pages [23] -->
m

<!-- b005765 | furniture | pages [23] -->
m

<!-- b005766 | furniture | pages [23] -->
m

<!-- b005767 | furniture | pages [23] -->
m

<!-- b005768 | furniture | pages [23] -->
m

<!-- b005769 | furniture | pages [23] -->
m

<!-- b005770 | furniture | pages [23] -->
m

<!-- b005771 | furniture | pages [23] -->
m

<!-- b005772 | furniture | pages [23] -->
m

<!-- b005773 | furniture | pages [23] -->
m

<!-- b005774 | furniture | pages [23] -->
m

<!-- b005775 | furniture | pages [23] -->
m

<!-- b005776 | furniture | pages [23] -->
m

<!-- b005777 | furniture | pages [23] -->
m

<!-- b005778 | furniture | pages [23] -->
m

<!-- b005779 | furniture | pages [23] -->
m

<!-- b005780 | furniture | pages [23] -->
m

<!-- b005781 | furniture | pages [23] -->
m

<!-- b005782 | furniture | pages [23] -->
m

<!-- b005783 | furniture | pages [23] -->
m

<!-- b005784 | furniture | pages [23] -->
m

<!-- b005785 | furniture | pages [23] -->
m

<!-- b005786 | furniture | pages [23] -->
m

<!-- b005787 | furniture | pages [23] -->
m

<!-- b005788 | furniture | pages [23] -->
m

<!-- b005789 | furniture | pages [23] -->
m

<!-- b005790 | furniture | pages [23] -->
m

<!-- b005791 | furniture | pages [23] -->
m

<!-- b005792 | furniture | pages [23] -->
m

<!-- b005793 | furniture | pages [23] -->
m

<!-- b005794 | furniture | pages [23] -->
m

<!-- b005795 | furniture | pages [23] -->
m

<!-- b005796 | furniture | pages [23] -->
m

<!-- b005797 | furniture | pages [23] -->
m

<!-- b005798 | furniture | pages [23] -->
m

<!-- b005799 | furniture | pages [23] -->
m

<!-- b005800 | furniture | pages [23] -->
m

<!-- b005801 | furniture | pages [23] -->
m

<!-- b005802 | furniture | pages [23] -->
m

<!-- b005803 | furniture | pages [23] -->
m

<!-- b005804 | furniture | pages [23] -->
m

<!-- b005805 | furniture | pages [23] -->
m

<!-- b005806 | furniture | pages [23] -->
m

<!-- b005807 | furniture | pages [23] -->
m

<!-- b005808 | furniture | pages [23] -->
m

<!-- b005809 | furniture | pages [23] -->
m

<!-- b005810 | furniture | pages [23] -->
m

<!-- b005811 | furniture | pages [23] -->
m

<!-- b005812 | furniture | pages [23] -->
m

<!-- b005813 | furniture | pages [23] -->
m

<!-- b005814 | furniture | pages [23] -->
m

<!-- b005815 | furniture | pages [23] -->
m

<!-- b005816 | furniture | pages [23] -->
m

<!-- b005817 | furniture | pages [23] -->
m

<!-- b005818 | furniture | pages [23] -->
m

<!-- b005819 | furniture | pages [23] -->
m

<!-- b005820 | furniture | pages [23] -->
m

<!-- b005821 | furniture | pages [23] -->
m

<!-- b005822 | furniture | pages [23] -->
m

<!-- b005823 | furniture | pages [23] -->
m

<!-- b005824 | furniture | pages [23] -->
m

<!-- b005825 | furniture | pages [23] -->
m

<!-- b005826 | furniture | pages [23] -->
m

<!-- b005827 | furniture | pages [23] -->
m

<!-- b005828 | furniture | pages [23] -->
m

<!-- b005829 | furniture | pages [23] -->
m

<!-- b005830 | furniture | pages [23] -->
m

<!-- b005831 | furniture | pages [23] -->
m

<!-- b005832 | furniture | pages [23] -->
m

<!-- b005833 | furniture | pages [23] -->
m

<!-- b005834 | furniture | pages [23] -->
m

<!-- b005835 | furniture | pages [23] -->
m

<!-- b005836 | furniture | pages [23] -->
m

<!-- b005837 | furniture | pages [23] -->
m

<!-- b005838 | furniture | pages [23] -->
m

<!-- b005839 | furniture | pages [23] -->
m

<!-- b005840 | furniture | pages [23] -->
m

<!-- b005841 | furniture | pages [23] -->
m

<!-- b005842 | furniture | pages [23] -->
m

<!-- b005843 | furniture | pages [23] -->
m

<!-- b005844 | furniture | pages [23] -->
m

<!-- b005845 | furniture | pages [23] -->
m

<!-- b005846 | furniture | pages [23] -->
m

<!-- b005847 | furniture | pages [23] -->
m

<!-- b005848 | furniture | pages [23] -->
m

<!-- b005849 | furniture | pages [23] -->
m

<!-- b005850 | furniture | pages [23] -->
m

<!-- b005851 | furniture | pages [23] -->
m

<!-- b005852 | furniture | pages [23] -->
m

<!-- b005853 | furniture | pages [23] -->
m

<!-- b005854 | furniture | pages [23] -->
m

<!-- b005855 | furniture | pages [23] -->
m

<!-- b005856 | furniture | pages [23] -->
m

<!-- b005857 | furniture | pages [23] -->
m

<!-- b005858 | furniture | pages [23] -->
m

<!-- b005859 | furniture | pages [23] -->
m

<!-- b005860 | furniture | pages [23] -->
m

<!-- b005861 | furniture | pages [23] -->
m

<!-- b005862 | furniture | pages [23] -->
m

<!-- b005863 | furniture | pages [23] -->
m

<!-- b005864 | furniture | pages [23] -->
m

<!-- b005865 | furniture | pages [23] -->
m

<!-- b005866 | furniture | pages [23] -->
m

<!-- b005867 | furniture | pages [23] -->
m

<!-- b005868 | furniture | pages [23] -->
m

<!-- b005869 | furniture | pages [23] -->
m

<!-- b005870 | furniture | pages [23] -->
m

<!-- b005871 | furniture | pages [23] -->
m

<!-- b005872 | furniture | pages [23] -->
m

<!-- b005873 | furniture | pages [23] -->
m

<!-- b005874 | furniture | pages [23] -->
m

<!-- b005875 | furniture | pages [23] -->
m

<!-- b005876 | furniture | pages [23] -->
m

<!-- b005877 | furniture | pages [23] -->
m

<!-- b005878 | furniture | pages [23] -->
m

<!-- b005879 | furniture | pages [23] -->
m

<!-- b005880 | furniture | pages [23] -->
m

<!-- b005881 | furniture | pages [23] -->
m

<!-- b005882 | furniture | pages [23] -->
m

<!-- b005883 | furniture | pages [23] -->
m

<!-- b005884 | furniture | pages [23] -->
m

<!-- b005885 | furniture | pages [23] -->
m

<!-- b005886 | furniture | pages [23] -->
m

<!-- b005887 | furniture | pages [23] -->
m

<!-- b005888 | furniture | pages [23] -->
m

<!-- b005889 | furniture | pages [23] -->
m

<!-- b005890 | furniture | pages [23] -->
m

<!-- b005891 | furniture | pages [23] -->
m

<!-- b005892 | furniture | pages [23] -->
m

<!-- b005893 | furniture | pages [23] -->
m

<!-- b005894 | furniture | pages [23] -->
m

<!-- b005895 | furniture | pages [23] -->
m

<!-- b005896 | furniture | pages [23] -->
m

<!-- b005897 | furniture | pages [23] -->
m

<!-- b005898 | furniture | pages [23] -->
m

<!-- b005899 | furniture | pages [23] -->
m

<!-- b005900 | furniture | pages [23] -->
m

<!-- b005901 | furniture | pages [23] -->
m

<!-- b005902 | furniture | pages [23] -->
m

<!-- b005903 | furniture | pages [23] -->
m

<!-- b005904 | furniture | pages [23] -->
m

<!-- b005905 | furniture | pages [23] -->
m

<!-- b005906 | furniture | pages [23] -->
m

<!-- b005907 | furniture | pages [23] -->
m

<!-- b005908 | furniture | pages [23] -->
m

<!-- b005909 | furniture | pages [23] -->
m

<!-- b005910 | furniture | pages [23] -->
m

<!-- b005911 | furniture | pages [23] -->
m

<!-- b005912 | furniture | pages [23] -->
m

<!-- b005913 | furniture | pages [23] -->
m

<!-- b005914 | furniture | pages [23] -->
m

<!-- b005915 | furniture | pages [23] -->
m

<!-- b005916 | furniture | pages [23] -->
m

<!-- b005917 | furniture | pages [23] -->
m

<!-- b005918 | furniture | pages [23] -->
m

<!-- b005919 | furniture | pages [23] -->
m

<!-- b005920 | furniture | pages [23] -->
m

<!-- b005921 | furniture | pages [23] -->
m

<!-- b005922 | furniture | pages [23] -->
m

<!-- b005923 | furniture | pages [23] -->
m

<!-- b005924 | furniture | pages [23] -->
m

<!-- b005925 | furniture | pages [23] -->
m

<!-- b005926 | furniture | pages [23] -->
m

<!-- b005927 | furniture | pages [23] -->
m

<!-- b005928 | furniture | pages [23] -->
m

<!-- b005929 | furniture | pages [23] -->
m

<!-- b005930 | furniture | pages [23] -->
m

<!-- b005931 | furniture | pages [23] -->
m

<!-- b005932 | furniture | pages [23] -->
m

<!-- b005933 | furniture | pages [23] -->
m

<!-- b005934 | furniture | pages [23] -->
m

<!-- b005935 | furniture | pages [23] -->
m

<!-- b005936 | furniture | pages [23] -->
m

<!-- b005937 | furniture | pages [23] -->
m

<!-- b005938 | furniture | pages [23] -->
m

<!-- b005939 | furniture | pages [23] -->
m

<!-- b005940 | furniture | pages [23] -->
m

<!-- b005941 | furniture | pages [23] -->
m

<!-- b005942 | furniture | pages [23] -->
m

<!-- b005943 | furniture | pages [23] -->
m

<!-- b005944 | furniture | pages [23] -->
m

<!-- b005945 | furniture | pages [23] -->
m

<!-- b005946 | furniture | pages [23] -->
m

<!-- b005947 | furniture | pages [23] -->
m

<!-- b005948 | furniture | pages [23] -->
m

<!-- b005949 | furniture | pages [23] -->
m

<!-- b005950 | furniture | pages [23] -->
m

<!-- b005951 | furniture | pages [23] -->
m

<!-- b005952 | furniture | pages [23] -->
m

<!-- b005953 | furniture | pages [23] -->
m

<!-- b005954 | furniture | pages [23] -->
m

<!-- b005955 | furniture | pages [23] -->
m

<!-- b005956 | furniture | pages [23] -->
m

<!-- b005957 | furniture | pages [23] -->
m

<!-- b005958 | furniture | pages [23] -->
m

<!-- b005959 | furniture | pages [23] -->
m

<!-- b005960 | furniture | pages [23] -->
m

<!-- b005961 | furniture | pages [23] -->
m

<!-- b005962 | furniture | pages [23] -->
m

<!-- b005963 | furniture | pages [23] -->
m

<!-- b005964 | furniture | pages [23] -->
m

<!-- b005965 | furniture | pages [23] -->
m

<!-- b005966 | furniture | pages [23] -->
m

<!-- b005967 | furniture | pages [23] -->
m

<!-- b005968 | furniture | pages [23] -->
m

<!-- b005969 | furniture | pages [23] -->
m

<!-- b005970 | furniture | pages [23] -->
m

<!-- b005971 | furniture | pages [23] -->
m

<!-- b005972 | furniture | pages [23] -->
m

<!-- b005973 | furniture | pages [23] -->
m

<!-- b005974 | furniture | pages [23] -->
m

<!-- b005975 | furniture | pages [23] -->
m

<!-- b005976 | furniture | pages [23] -->
m

<!-- b005977 | furniture | pages [23] -->
m

<!-- b005978 | furniture | pages [23] -->
m

<!-- b005979 | furniture | pages [23] -->
m

<!-- b005980 | furniture | pages [23] -->
m

<!-- b005981 | furniture | pages [23] -->
m

<!-- b005982 | furniture | pages [23] -->
m

<!-- b005983 | furniture | pages [23] -->
m

<!-- b005984 | furniture | pages [23] -->
m

<!-- b005985 | furniture | pages [23] -->
m

<!-- b005986 | furniture | pages [23] -->
m

<!-- b005987 | furniture | pages [23] -->
m

<!-- b005988 | furniture | pages [23] -->
m

<!-- b005989 | furniture | pages [23] -->
m

<!-- b005990 | furniture | pages [23] -->
m

<!-- b005991 | furniture | pages [23] -->
m

<!-- b005992 | furniture | pages [23] -->
m

<!-- b005993 | furniture | pages [23] -->
m

<!-- b005994 | furniture | pages [23] -->
m

<!-- b005995 | furniture | pages [23] -->
m

<!-- b005996 | furniture | pages [23] -->
m

<!-- b005997 | furniture | pages [23] -->
m

<!-- b005998 | furniture | pages [23] -->
m

<!-- b005999 | furniture | pages [23] -->
m

<!-- b006000 | furniture | pages [23] -->
m

<!-- b006001 | furniture | pages [23] -->
m

<!-- b006002 | furniture | pages [23] -->
m

<!-- b006003 | furniture | pages [23] -->
m

<!-- b006004 | furniture | pages [23] -->
m

<!-- b006005 | furniture | pages [23] -->
m

<!-- b006006 | furniture | pages [23] -->
m

<!-- b006007 | furniture | pages [23] -->
m

<!-- b006008 | furniture | pages [23] -->
m

<!-- b006009 | furniture | pages [23] -->
m

<!-- b006010 | furniture | pages [23] -->
m

<!-- b006011 | furniture | pages [23] -->
m

<!-- b006012 | furniture | pages [23] -->
m

<!-- b006013 | furniture | pages [23] -->
m

<!-- b006014 | furniture | pages [23] -->
m

<!-- b006015 | furniture | pages [23] -->
m

<!-- b006016 | furniture | pages [23] -->
m

<!-- b006017 | furniture | pages [23] -->
m

<!-- b006018 | furniture | pages [23] -->
m

<!-- b006019 | furniture | pages [23] -->
m

<!-- b006020 | furniture | pages [23] -->
m

<!-- b006021 | furniture | pages [24] -->
m

<!-- b006022 | furniture | pages [24] -->
m

<!-- b006023 | furniture | pages [24] -->
m

<!-- b006024 | furniture | pages [24] -->
m

<!-- b006025 | furniture | pages [24] -->
m

<!-- b006026 | furniture | pages [24] -->
m

<!-- b006027 | furniture | pages [24] -->
m

<!-- b006028 | furniture | pages [24] -->
m

<!-- b006029 | furniture | pages [24] -->
m

<!-- b006030 | furniture | pages [24] -->
m

<!-- b006031 | furniture | pages [24] -->
m

<!-- b006032 | furniture | pages [24] -->
m

<!-- b006033 | furniture | pages [24] -->
m

<!-- b006034 | furniture | pages [24] -->
m

<!-- b006035 | furniture | pages [24] -->
m

<!-- b006036 | furniture | pages [24] -->
m

<!-- b006037 | furniture | pages [24] -->
m

<!-- b006038 | furniture | pages [24] -->
m

<!-- b006039 | furniture | pages [24] -->
m

<!-- b006040 | furniture | pages [24] -->
m

<!-- b006041 | furniture | pages [24] -->
m

<!-- b006042 | furniture | pages [24] -->
m

<!-- b006043 | furniture | pages [24] -->
m

<!-- b006044 | furniture | pages [24] -->
m

<!-- b006045 | furniture | pages [24] -->
m

<!-- b006046 | furniture | pages [24] -->
m

<!-- b006047 | furniture | pages [24] -->
m

<!-- b006048 | furniture | pages [24] -->
m

<!-- b006049 | furniture | pages [24] -->
m

<!-- b006050 | furniture | pages [24] -->
m

<!-- b006051 | furniture | pages [24] -->
m

<!-- b006052 | furniture | pages [24] -->
m

<!-- b006053 | furniture | pages [24] -->
m

<!-- b006054 | furniture | pages [24] -->
m

<!-- b006055 | furniture | pages [24] -->
m

<!-- b006056 | furniture | pages [24] -->
m

<!-- b006057 | furniture | pages [24] -->
m

<!-- b006058 | furniture | pages [24] -->
m

<!-- b006059 | furniture | pages [24] -->
m

<!-- b006060 | furniture | pages [24] -->
m

<!-- b006061 | furniture | pages [24] -->
m

<!-- b006062 | furniture | pages [24] -->
m

<!-- b006063 | furniture | pages [24] -->
m

<!-- b006064 | furniture | pages [24] -->
m

<!-- b006065 | furniture | pages [24] -->
m

<!-- b006066 | furniture | pages [24] -->
m

<!-- b006067 | furniture | pages [24] -->
m

<!-- b006068 | furniture | pages [24] -->
m

<!-- b006069 | furniture | pages [24] -->
m

<!-- b006070 | furniture | pages [24] -->
m

<!-- b006071 | furniture | pages [24] -->
m

<!-- b006072 | furniture | pages [24] -->
m

<!-- b006073 | furniture | pages [24] -->
m

<!-- b006074 | furniture | pages [24] -->
m

<!-- b006075 | furniture | pages [24] -->
m

<!-- b006076 | furniture | pages [24] -->
m

<!-- b006077 | furniture | pages [24] -->
m

<!-- b006078 | furniture | pages [24] -->
m

<!-- b006079 | furniture | pages [24] -->
m

<!-- b006080 | furniture | pages [24] -->
m

<!-- b006081 | furniture | pages [24] -->
m

<!-- b006082 | furniture | pages [24] -->
m

<!-- b006083 | furniture | pages [24] -->
m

<!-- b006084 | furniture | pages [24] -->
m

<!-- b006085 | furniture | pages [24] -->
m

<!-- b006086 | furniture | pages [24] -->
m

<!-- b006087 | furniture | pages [24] -->
m

<!-- b006088 | furniture | pages [24] -->
m

<!-- b006089 | furniture | pages [24] -->
m

<!-- b006090 | furniture | pages [24] -->
m

<!-- b006091 | furniture | pages [24] -->
m

<!-- b006092 | furniture | pages [24] -->
m

<!-- b006093 | furniture | pages [24] -->
m

<!-- b006094 | furniture | pages [24] -->
m

<!-- b006095 | furniture | pages [24] -->
m

<!-- b006096 | furniture | pages [24] -->
m

<!-- b006097 | furniture | pages [24] -->
m

<!-- b006098 | furniture | pages [24] -->
m

<!-- b006099 | furniture | pages [24] -->
m

<!-- b006100 | furniture | pages [24] -->
m

<!-- b006101 | furniture | pages [24] -->
m

<!-- b006102 | furniture | pages [24] -->
m

<!-- b006103 | furniture | pages [24] -->
m

<!-- b006104 | furniture | pages [24] -->
m

<!-- b006105 | furniture | pages [24] -->
m

<!-- b006106 | furniture | pages [24] -->
m

<!-- b006107 | furniture | pages [24] -->
m

<!-- b006108 | furniture | pages [24] -->
m

<!-- b006109 | furniture | pages [24] -->
m

<!-- b006110 | furniture | pages [24] -->
m

<!-- b006111 | furniture | pages [24] -->
m

<!-- b006112 | furniture | pages [24] -->
m

<!-- b006113 | furniture | pages [24] -->
m

<!-- b006114 | furniture | pages [24] -->
m

<!-- b006115 | furniture | pages [24] -->
m

<!-- b006116 | furniture | pages [24] -->
m

<!-- b006117 | furniture | pages [24] -->
m

<!-- b006118 | furniture | pages [24] -->
m

<!-- b006119 | furniture | pages [24] -->
m

<!-- b006120 | furniture | pages [24] -->
m

<!-- b006121 | furniture | pages [24] -->
m

<!-- b006122 | furniture | pages [24] -->
m

<!-- b006123 | furniture | pages [24] -->
m

<!-- b006124 | furniture | pages [24] -->
m

<!-- b006125 | furniture | pages [24] -->
m

<!-- b006126 | furniture | pages [24] -->
m

<!-- b006127 | furniture | pages [24] -->
m

<!-- b006128 | furniture | pages [24] -->
m

<!-- b006129 | furniture | pages [24] -->
m

<!-- b006130 | furniture | pages [24] -->
m

<!-- b006131 | furniture | pages [24] -->
m

<!-- b006132 | furniture | pages [24] -->
m

<!-- b006133 | furniture | pages [24] -->
m

<!-- b006134 | furniture | pages [24] -->
m

<!-- b006135 | furniture | pages [24] -->
m

<!-- b006136 | furniture | pages [24] -->
m

<!-- b006137 | furniture | pages [24] -->
m

<!-- b006138 | furniture | pages [24] -->
m

<!-- b006139 | furniture | pages [24] -->
m

<!-- b006140 | furniture | pages [24] -->
m

<!-- b006141 | furniture | pages [24] -->
m

<!-- b006142 | furniture | pages [24] -->
m

<!-- b006143 | furniture | pages [24] -->
m

<!-- b006144 | furniture | pages [24] -->
m

<!-- b006145 | furniture | pages [24] -->
m

<!-- b006146 | furniture | pages [24] -->
m

<!-- b006147 | furniture | pages [24] -->
m

<!-- b006148 | furniture | pages [24] -->
m

<!-- b006149 | furniture | pages [24] -->
m

<!-- b006150 | furniture | pages [24] -->
m

<!-- b006151 | furniture | pages [24] -->
m

<!-- b006152 | furniture | pages [24] -->
m

<!-- b006153 | furniture | pages [24] -->
m

<!-- b006154 | furniture | pages [24] -->
m

<!-- b006155 | furniture | pages [24] -->
m

<!-- b006156 | furniture | pages [24] -->
m

<!-- b006157 | furniture | pages [24] -->
m

<!-- b006158 | furniture | pages [24] -->
m

<!-- b006159 | furniture | pages [24] -->
m

<!-- b006160 | furniture | pages [24] -->
m

<!-- b006161 | furniture | pages [24] -->
m

<!-- b006162 | furniture | pages [24] -->
m

<!-- b006163 | furniture | pages [24] -->
m

<!-- b006164 | furniture | pages [24] -->
m

<!-- b006165 | furniture | pages [24] -->
m

<!-- b006166 | furniture | pages [24] -->
m

<!-- b006167 | furniture | pages [24] -->
m

<!-- b006168 | furniture | pages [24] -->
m

<!-- b006169 | furniture | pages [24] -->
m

<!-- b006170 | furniture | pages [24] -->
m

<!-- b006171 | furniture | pages [24] -->
m

<!-- b006172 | furniture | pages [24] -->
m

<!-- b006173 | furniture | pages [24] -->
m

<!-- b006174 | furniture | pages [24] -->
m

<!-- b006175 | furniture | pages [24] -->
m

<!-- b006176 | furniture | pages [24] -->
m

<!-- b006177 | furniture | pages [24] -->
m

<!-- b006178 | furniture | pages [24] -->
m

<!-- b006179 | furniture | pages [24] -->
m

<!-- b006180 | furniture | pages [24] -->
m

<!-- b006181 | furniture | pages [24] -->
m

<!-- b006182 | furniture | pages [24] -->
m

<!-- b006183 | furniture | pages [24] -->
m

<!-- b006184 | furniture | pages [24] -->
m

<!-- b006185 | furniture | pages [24] -->
m

<!-- b006186 | furniture | pages [24] -->
m

<!-- b006187 | furniture | pages [24] -->
m

<!-- b006188 | furniture | pages [24] -->
m

<!-- b006189 | furniture | pages [24] -->
m

<!-- b006190 | furniture | pages [24] -->
m

<!-- b006191 | furniture | pages [24] -->
m

<!-- b006192 | furniture | pages [24] -->
m

<!-- b006193 | furniture | pages [24] -->
m

<!-- b006194 | furniture | pages [24] -->
m

<!-- b006195 | furniture | pages [24] -->
m

<!-- b006196 | furniture | pages [24] -->
m

<!-- b006197 | furniture | pages [24] -->
m

<!-- b006198 | furniture | pages [24] -->
m

<!-- b006199 | furniture | pages [24] -->
m

<!-- b006200 | furniture | pages [24] -->
m

<!-- b006201 | furniture | pages [24] -->
m

<!-- b006202 | furniture | pages [24] -->
m

<!-- b006203 | furniture | pages [24] -->
m

<!-- b006204 | furniture | pages [24] -->
m

<!-- b006205 | furniture | pages [24] -->
m

<!-- b006206 | furniture | pages [24] -->
m

<!-- b006207 | furniture | pages [24] -->
m

<!-- b006208 | furniture | pages [24] -->
m

<!-- b006209 | furniture | pages [24] -->
m

<!-- b006210 | furniture | pages [24] -->
m

<!-- b006211 | furniture | pages [24] -->
m

<!-- b006212 | furniture | pages [24] -->
m

<!-- b006213 | furniture | pages [24] -->
m

<!-- b006214 | furniture | pages [24] -->
m

<!-- b006215 | furniture | pages [24] -->
m

<!-- b006216 | furniture | pages [24] -->
m

<!-- b006217 | furniture | pages [24] -->
m

<!-- b006218 | furniture | pages [24] -->
m

<!-- b006219 | furniture | pages [24] -->
m

<!-- b006220 | furniture | pages [24] -->
m

<!-- b006221 | furniture | pages [24] -->
m

<!-- b006222 | furniture | pages [24] -->
m

<!-- b006223 | furniture | pages [24] -->
m

<!-- b006224 | furniture | pages [24] -->
m

<!-- b006225 | furniture | pages [24] -->
m

<!-- b006226 | furniture | pages [24] -->
m

<!-- b006227 | furniture | pages [24] -->
m

<!-- b006228 | furniture | pages [24] -->
m

<!-- b006229 | furniture | pages [24] -->
m

<!-- b006230 | furniture | pages [24] -->
m

<!-- b006231 | furniture | pages [24] -->
m

<!-- b006232 | furniture | pages [24] -->
m

<!-- b006233 | furniture | pages [24] -->
m

<!-- b006234 | furniture | pages [24] -->
m

<!-- b006235 | furniture | pages [24] -->
m

<!-- b006236 | furniture | pages [24] -->
m

<!-- b006237 | furniture | pages [24] -->
m

<!-- b006238 | furniture | pages [24] -->
m

<!-- b006239 | furniture | pages [24] -->
m

<!-- b006240 | furniture | pages [24] -->
m

<!-- b006241 | furniture | pages [24] -->
m

<!-- b006242 | furniture | pages [24] -->
m

<!-- b006243 | furniture | pages [24] -->
m

<!-- b006244 | furniture | pages [24] -->
m

<!-- b006245 | furniture | pages [24] -->
m

<!-- b006246 | furniture | pages [24] -->
m

<!-- b006247 | furniture | pages [24] -->
m

<!-- b006248 | furniture | pages [24] -->
m

<!-- b006249 | furniture | pages [24] -->
m

<!-- b006250 | furniture | pages [24] -->
m

<!-- b006251 | furniture | pages [24] -->
m

<!-- b006252 | furniture | pages [24] -->
m

<!-- b006253 | furniture | pages [24] -->
m

<!-- b006254 | furniture | pages [24] -->
m

<!-- b006255 | furniture | pages [24] -->
m

<!-- b006256 | furniture | pages [24] -->
m

<!-- b006257 | furniture | pages [24] -->
m

<!-- b006258 | furniture | pages [24] -->
m

<!-- b006259 | furniture | pages [24] -->
m

<!-- b006260 | furniture | pages [24] -->
m

<!-- b006261 | furniture | pages [24] -->
m

<!-- b006262 | furniture | pages [24] -->
m

<!-- b006263 | furniture | pages [24] -->
m

<!-- b006264 | furniture | pages [24] -->
m

<!-- b006265 | furniture | pages [24] -->
m

<!-- b006266 | furniture | pages [24] -->
m

<!-- b006267 | furniture | pages [24] -->
m

<!-- b006268 | furniture | pages [24] -->
m

<!-- b006269 | furniture | pages [24] -->
m

<!-- b006270 | furniture | pages [24] -->
m

<!-- b006271 | furniture | pages [24] -->
m

<!-- b006272 | furniture | pages [24] -->
m

<!-- b006273 | furniture | pages [24] -->
m

<!-- b006274 | furniture | pages [24] -->
m

<!-- b006275 | furniture | pages [24] -->
m

<!-- b006276 | furniture | pages [24] -->
m

<!-- b006277 | furniture | pages [24] -->
m

<!-- b006278 | furniture | pages [24] -->
m

<!-- b006279 | furniture | pages [24] -->
m

<!-- b006280 | furniture | pages [24] -->
m

<!-- b006281 | furniture | pages [24] -->
m

<!-- b006282 | furniture | pages [24] -->
m

<!-- b006283 | furniture | pages [24] -->
m

<!-- b006284 | furniture | pages [24] -->
m

<!-- b006285 | furniture | pages [24] -->
m

<!-- b006286 | furniture | pages [24] -->
m

<!-- b006287 | furniture | pages [24] -->
m

<!-- b006288 | furniture | pages [24] -->
m

<!-- b006289 | furniture | pages [24] -->
m

<!-- b006290 | furniture | pages [24] -->
m

<!-- b006291 | furniture | pages [24] -->
m

<!-- b006292 | furniture | pages [24] -->
m

<!-- b006293 | furniture | pages [24] -->
m

<!-- b006294 | furniture | pages [24] -->
m

<!-- b006295 | furniture | pages [24] -->
m

<!-- b006296 | furniture | pages [24] -->
m

<!-- b006297 | furniture | pages [24] -->
m

<!-- b006298 | furniture | pages [24] -->
m

<!-- b006299 | furniture | pages [24] -->
m

<!-- b006300 | furniture | pages [24] -->
m

<!-- b006301 | furniture | pages [24] -->
m

<!-- b006302 | furniture | pages [24] -->
m

<!-- b006303 | furniture | pages [24] -->
m

<!-- b006304 | furniture | pages [24] -->
m

<!-- b006305 | furniture | pages [24] -->
m

<!-- b006306 | furniture | pages [24] -->
m

<!-- b006307 | furniture | pages [24] -->
m

<!-- b006308 | furniture | pages [24] -->
m

<!-- b006309 | furniture | pages [24] -->
m

<!-- b006310 | furniture | pages [24] -->
m

<!-- b006311 | furniture | pages [24] -->
m

<!-- b006312 | furniture | pages [24] -->
m

<!-- b006313 | furniture | pages [24] -->
m

<!-- b006314 | furniture | pages [24] -->
m

<!-- b006315 | furniture | pages [24] -->
m

<!-- b006316 | furniture | pages [24] -->
m

<!-- b006317 | furniture | pages [24] -->
m

<!-- b006318 | furniture | pages [24] -->
m

<!-- b006319 | furniture | pages [24] -->
m

<!-- b006320 | furniture | pages [24] -->
m

<!-- b006321 | furniture | pages [24] -->
Team 2522820

<!-- b006322 | furniture | pages [24] -->
Page 24

<!-- b006323 | prose | pages [24] -->
more effective than identifying individual anomalous performances by considering only the population mean and standard deviation instead of the rolling statistics we used.

<!-- b006324 | prose | pages [24] -->
The main weakness of our model is that there is no way to determine whether anomalous performances were due to the great coach effect or any number of outside influences without manually comparing our findings to historical great coaches. Because of the limited data, this is inevitable.

<!-- b006325 | prose | pages [24] -->
7

<!-- b006326 | heading | pages [24] -->
Conclusion

<!-- b006327 | prose | pages [24] -->
The Olympics is not only a stage for athletes to show off their skills, but for countries to establish their presence in the world. Developing countries are increasingly entering the Olympics, and their participation adds a new layer of competition and uncertainty to the Games. As the Olympics continue to grow in scope and diversity, the ability to predict medal counts becomes increasingly complex. By leveraging statistical models to investigate data on Olympic medal distributions, we have explored the nature of such data and how it is affected by great coaches.

<!-- b006328 | prose | pages [24] -->
关注数学模型

<!-- b006329 | furniture | pages [24] -->
2

<!-- b006330 | furniture | pages [24] -->
MATHmodels

<!-- b006331 | furniture | pages [24] -->
获取更多资讯
