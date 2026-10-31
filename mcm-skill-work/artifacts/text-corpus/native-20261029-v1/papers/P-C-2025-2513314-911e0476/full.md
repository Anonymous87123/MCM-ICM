# P-C-2025-2513314-911e0476

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
2513314

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
A Glimpse of Olympics Medals through Bayesian Model

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
The Olympic medal count fluctuates over time, driven by various influencing factors. Through a comprehensive analysis of historical data and predict projections for 2028, we have identified key trends and valuable insights.

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
First, we conducted an exploratory data analysis to understand the distribution characteristics of our target variable, providing a solid foundation for our modeling process.

<!-- b000013 | prose | pages [1] -->
For Task 1, our objective is to predict the medal counts for the 2028 Olympic Games. To improve accuracy and quantify uncertainty, we propose a Bayesian Hierarchical Dirichlet- Multinomial (BHDM) Model, which captures the discrete, sum-constrained nature of medal counts while addressing overdispersion and cross-country heterogeneity through hierarchical priors.

<!-- b000014 | prose | pages [1] -->
A key strength of this model is its robust uncertainty quantification. Each country’s medal count follows a Dirichlet-Multinomial distribution with latent rates governed by country- specific regression coefficients and a Gamma-distributed concentration parameter. MCMC-

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
based posterior inference provides 95% credible intervals, assessing both medal forecasts and extreme outcomes like "ice-breaking" probabilities. By analyzing posterior distributions, the model offers interpretable insights into key predictors, ensuring informed decision-making under uncertainty.

<!-- b000017 | prose | pages [1] -->
This method exhibits strong performance, achieving R2 of 0.85 for total medals and 0.80 for gold medals, surpassing all baseline models. Our 2028 projections show the U.S. winning

<!-- b000018 | heading | pages [1] -->
146 medals (95% CI: 136–156) and 53 golds (95% CI: 50–56), an increase from 2024,

<!-- b000019 | prose | pages [1] -->
while China’s total medals decline to 82. We also computed ice-breaking probabilities, with Malaysia (68.6%) and South Sudan (39.0%) most likely to win their first medals. Regression analysis identified key sports for the U.S., China, the U.K., and France, offering strategic insights for host nations to optimize medal prospects.

<!-- b000020 | prose | pages [1] -->
For Task 2, we investigate the “Great Coach” effect. First, we define great coaches and construct a national-level great coach variable to quantify each country’s coaching strength. We then incorporate this variable into the BHDM model and analyze its impact through regression coefficients.

<!-- b000021 | prose | pages [1] -->
The results indicate that great coaches significantly influence both total and gold medal counts. Specifically, for the United States, China, and Japan, a one-unit increase in this vari- able leads to an expected medal count increase of 3.74%, 4.55%, and 2.87%, respectively. Additionally, we examine key sports in these three nations to assess the impact of this effect.

<!-- b000022 | prose | pages [1] -->
To test the robustness of our model, we conducted sensitivity analyses on both the weakly informative priors and the assumption of equal medal distribution. The results indicate that, despite adjustments in parameters and distributions, the model maintains reasonable predictive performance, with onlyminor deviationsfrom theoriginal baseline, demonstratingits robustness.

<!-- b000023 | prose | pages [1] -->
For Task 3, based on the comprehensive modeling process above, we derived three additional insights: Economic level determines medals, Home Turf and Aligned Systems Prevail, and Emerging Sports Aid Low-GDP Countries. We communicated these insights in a letter to the NOC, aiming to enhance their strategies and help nations secure more gold medals.

<!-- b000024 | keywords | pages [1] -->
Keywords: Bayesian Hierarchical Dirichlet-Multinomial, Posterior inference, Uncertainty

<!-- b000025 | prose | pages [1] -->
Quantification, Regression Analysis, Credible Intervals

<!-- b000026 | furniture | pages [3] -->
Team # 2513314

<!-- b000027 | furniture | pages [3] -->
Page 3 of 22

<!-- b000028 | prose | pages [3] -->
1

<!-- b000029 | heading | pages [3] -->
Introduction

<!-- b000030 | prose | pages [3] -->
1.1

<!-- b000031 | heading | pages [3] -->
Background

<!-- b000032 | prose | pages [3] -->
The Olympic Games, held every four years, bring together the world’s top athletes to compete in a wide range of sports.

<!-- b000033 | prose | pages [3] -->
Since the first modern Olympics in 1896, the event has grown significantly in scale, with more countries participating and more events being introduced.

<!-- b000034 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000035 | prose | pages [3] -->
Medal counts serve as a key indicator of national sports performance, reflecting a country’s investment in athletics, talent development, and international competitiveness.

<!-- b000036 | caption | pages [3] -->
Figure 1: The 2028 Summer Olympics will be held in Los Angeles, USA.

<!-- b000037 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000038 | prose | pages [3] -->
Predicting Olympic medal counts is an important challenge, as it provides insights into national sports strategies and performance trends. Various factors influence a country’s medal prospects, including economic resources, population size, sports infrastructure, and historical performance.

<!-- b000039 | prose | pages [3] -->
Additionally, host nations often experience a boost in medal counts due to home-field advantages and increased investment. A robust predictive model can help sports organizations allocate resources efficiently and set realistic goals for future Olympic Games.

<!-- b000040 | prose | pages [3] -->
Beyond national investment, coaching plays a critical role in athletic success. Some elite coaches have significantly impacted multiple countries’ performances, demonstrating a “Great Coach” effect. By analyzing historical data, it is possible to quantify this effect and identify sports where hiring top-level coaches could maximize a nation’s medal potential. Understanding the role of coaching in Olympic success can provide strategic recommendations for countries aiming to improve their performance.

<!-- b000041 | prose | pages [3] -->
1.2

<!-- b000042 | heading | pages [3] -->
Problem Restatement

<!-- b000043 | prose | pages [3] -->
The distribution of Olympic medals is a key topic of interest for analysts, sports federations, and policymakers.

<!-- b000044 | prose | pages [3] -->
Medal standings reflect national athletic strength, investment in sports development, and strategic resource allocation. This study focuses on developing a predictive model for Olympic medal counts and exploring the underlying factors that influence national

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
performance.

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
Specifically, our objectives include:

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

<!-- b000734 | furniture | pages [4] -->
Team # 2513314

<!-- b000735 | furniture | pages [4] -->
Page 4 of 22

<!-- b000736 | prose | pages [4] -->
• Developing a mathematical model to predict the number of Gold and total medals for each country in the 2028 Los Angeles Summer Olympics, incorporating factors such as historical performance, host nation advantages, and event distributions. • Estimating the likelihood of countries earning their first Olympic medal and analyzing the probability of new medal-winning nations emerging. • Examining the relationship between specific sports events and national success, identifying key disciplines that contribute significantly to a country’s medal tally. • Investigating the potential impact of elite coaches on national performance, quantifying the "Great Coach" effect, and recommending strategic investments in coaching for selected countries. By addressing these questions, this study aims to provide valuable insights into Olympic medal trends, helping national Olympic committees optimize their training programs and re- source allocation for future competitions.

<!-- b000737 | prose | pages [4] -->
1.3 Our Work

<!-- b000738 | prose | pages [4] -->
Our workflow is illustrated in Figure 2. Before modeling, we first conducted model assump- tions (Section 2) and data exploration (Section 4.2) to facilitate the modeling process. After exploring the data distribution, we identified eight key variables (Section 5.1) and constructed a Bayesian Hierarchical Decision Model (BHDM) (Section 5.2) to better fit our observed distri- butions.

<!-- b000739 | caption | pages [4] -->
Figure 2: Our workflow.

<!-- b000740 | prose | pages [4] -->
A glimpse of dataset

<!-- b000741 | heading | pages [4] -->
Model Assumption

<!-- b000742 | prose | pages [4] -->
Equal

<!-- b000743 | prose | pages [4] -->
Medal

<!-- b000744 | prose | pages [4] -->
Country

<!-- b000745 | prose | pages [4] -->
Distribution

<!-- b000746 | prose | pages [4] -->
Heterogeneity

<!-- b000747 | prose | pages [4] -->
Distribution

<!-- b000748 | furniture | pages [4] -->


<!-- b000749 | prose | pages [4] -->
Some insights about Olympics Medal Counts To: Country Olympic Committees From: Team #2513314 Data: January 27, 2025 Dear Country Olympic Committee leaders:

<!-- b000750 | furniture | pages [4] -->


<!-- b000751 | prose | pages [4] -->
…

<!-- b000752 | prose | pages [4] -->
Overdispersion and Heavy Tails

<!-- b000753 | prose | pages [4] -->
Sum Fixed and Discrete

<!-- b000754 | furniture | pages [4] -->


<!-- b000755 | prose | pages [4] -->
Task 2: Dive Into Great Coach Effect

<!-- b000756 | prose | pages [4] -->
Task 1: Predicting Medals of 2028 LA Olympics

<!-- b000757 | prose | pages [4] -->
𝜽𝜽𝒊𝒊= 𝝓𝝓𝒊𝒊𝒆𝒆𝒆𝒆𝒆𝒆𝒙𝒙𝒊𝒊

<!-- b000758 | prose | pages [4] -->
𝑻𝑻𝜷𝜷𝒊𝒊

<!-- b000759 | prose | pages [4] -->
𝑿𝑿𝟏𝟏−𝑿𝑿𝟖𝟖

<!-- b000760 | heading | pages [4] -->
BHDM Model Setup

<!-- b000761 | prose | pages [4] -->
Key Variables for Medals

<!-- b000762 | prose | pages [4] -->
Why NOT Other Models?

<!-- b000763 | prose | pages [4] -->
Dataset

<!-- b000764 | prose | pages [4] -->
Coaching

<!-- b000765 | prose | pages [4] -->
Two-phase RF Deep Learning

<!-- b000766 | prose | pages [4] -->
𝜷𝜷𝒊𝒊follows a weakly informative prior

<!-- b000767 | prose | pages [4] -->
Breaking the Ice Probability Posterior Distribution

<!-- b000768 | prose | pages [4] -->
The country that will achieve

<!-- b000769 | prose | pages [4] -->
Important Sports and

<!-- b000770 | prose | pages [4] -->
a Breakthrough From Zero

<!-- b000771 | prose | pages [4] -->
Home Event Impact

<!-- b000772 | heading | pages [4] -->
Sensitivity Analysis

<!-- b000773 | prose | pages [4] -->
𝑿𝑿𝟗𝟗

<!-- b000774 | prose | pages [4] -->
All

<!-- b000775 | prose | pages [4] -->
Ability

<!-- b000776 | prose | pages [4] -->
Coach

<!-- b000777 | prose | pages [4] -->
Great Coach

<!-- b000778 | prose | pages [4] -->
Poisson

<!-- b000779 | prose | pages [4] -->
Neg. Binomial

<!-- b000780 | prose | pages [4] -->
Database

<!-- b000781 | prose | pages [4] -->
Predictive Uncertainty

<!-- b000782 | prose | pages [4] -->
of 𝑿𝑿𝟗𝟗

<!-- b000783 | prose | pages [4] -->
and Discrete Outcomes

<!-- b000784 | prose | pages [4] -->
Posterior Summary Our BHDM Model

<!-- b000785 | prose | pages [4] -->
Projects of LA 2028

<!-- b000786 | prose | pages [4] -->
Japan China United State

<!-- b000787 | prose | pages [4] -->
Task 3: Other Original Insights of BHDM

<!-- b000788 | heading | pages [4] -->
Sensitivity analysis of weak

<!-- b000789 | heading | pages [4] -->
Sensitivity Analysis of Equal

<!-- b000790 | prose | pages [4] -->
Economic level determines medals

<!-- b000791 | prose | pages [4] -->
priors for β

<!-- b000792 | heading | pages [4] -->
Distribution Assumptions

<!-- b000793 | prose | pages [4] -->
Proved to be Great Robustness!

<!-- b000794 | prose | pages [4] -->
Home Turf and Aligned Systems Prevail

<!-- b000795 | prose | pages [4] -->
Emerging Sports Aid Low-GDP Countries

<!-- b000796 | prose | pages [4] -->
During the modeling process, we also considered alternative models; however, they were either inconsistent with the data distribution or incapable of capturing the differences between countries, leading to their exclusion. Using our model, we then projected the medal distribution for the 2028 Los Angeles Olympics along with its 95% prediction interval. Additionally, we analyzed breakthrough probabilities, identified key sports for specific countries, and proposed adjustments to the sports program for the host nation.

<!-- b000797 | prose | pages [4] -->
To investigate the "Great Coach" effect, we first cross-referenced Wikipedia databases with

<!-- b000798 | prose | pages [4] -->
关注数学模型

<!-- b000799 | prose | pages [4] -->
our dataset to identify elite coaches. We then quantified each country’s coaching strength and

<!-- b000800 | furniture | pages [4] -->
2

<!-- b000801 | furniture | pages [4] -->
MATHmodels

<!-- b000802 | furniture | pages [4] -->
获取更多资讯

<!-- b000803 | furniture | pages [5] -->
Team # 2513314

<!-- b000804 | furniture | pages [5] -->
Page 5 of 22

<!-- b000805 | prose | pages [5] -->
incorporated it as a new variable into our BHDM model. By analyzing the posterior parameters of this variable for three selected countries, we assessed the impact of great coaches on their Olympic performance (Section 6).

<!-- b000806 | prose | pages [5] -->
Subsequently, we conducted a sensitivity analysis to determine the influence of model parameters and distributional variations on our results, thereby validating the robustness of our model (Section 7). Finally, based on our entire modeling process, we derived three original insights and drafted a letter to the COC to communicate these findings (Section 9).

<!-- b000807 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000808 | heading | pages [5] -->
Assumptions and Justifications

<!-- b000809 | prose | pages [5] -->
2

<!-- b000810 | prose | pages [5] -->
To simplify our modeling process, we make the following assumptions:

<!-- b000811 | heading | pages [5] -->
Assumption 1 (Medal Distribution Assumption): The distribution of medal counts to be

<!-- b000812 | prose | pages [5] -->
modeled necessitates integer-valued predictions that sum to a fixed total, often exhibits overdis- persion and heavy tails. This forms our core assumption and directly informs our choice of modeling approach. In Section 4.2, we will validate this assumption through visual analysis.

<!-- b000813 | heading | pages [5] -->
Assumption 2 (Equal Distribution Assumption): The composition and skill levels of athletes

<!-- b000814 | prose | pages [5] -->
representing each country, as well as the events featured in the 2028 Olympics, will be largely consistent with those of the 2024 Paris Olympics. Given the absence of data for the 2028 Games,

<!-- b000815 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000816 | prose | pages [5] -->
we assume that key factors such as event availability and athlete participation remain comparable to those in 2024. In Section 7.2, we will explore relaxations of this assumption.

<!-- b000817 | heading | pages [5] -->
Assumption 3 (Country Heterogeneity Assumption): Each country excels in different sports

<!-- b000818 | prose | pages [5] -->
and exhibits varying adaptability to the same set of variables, leading to cross-country hetero- geneity. In Section 5.2, we will explore this phenomenon in detail and incorporate it as a key assumption in our modeling approach.

<!-- b000819 | prose | pages [5] -->
3

<!-- b000820 | heading | pages [5] -->
Notations

<!-- b000821 | caption | pages [5] -->
Table 1: Notations used in the BHDM model and related analyses.

<!-- b000822 | heading | pages [5] -->
Symbol

<!-- b000823 | prose | pages [5] -->
Description 𝑁 Number of countries 𝑇 Total medals across all countries Covariate (feature) vector for country 𝑖 x𝑖 𝝁𝛽 Global mean of coefficient vectors 𝜙𝑖 Concentration parameter for country 𝑖 𝜃𝑖 Latent rate for country 𝑖 𝑋1,𝑖 Historical medal record 𝑋3,𝑖 Host nation flag (binary) 𝑋5,𝑖 Athletics events 𝑋7,𝑖 Ball sports events 𝑋9,𝑖 Great Coach variable (aggregate coaching ability)

<!-- b000824 | prose | pages [5] -->
4 Data Pre-processing

<!-- b000825 | heading | pages [5] -->
Symbol

<!-- b000826 | prose | pages [5] -->
Description 𝑀𝑖 Medal count of country 𝑖 𝑇new Total medals in a future Olympics Random coefficient vector for country 𝑖 𝜷𝑖 Σ𝛽 Covariance matrix (weakly informative prior) 𝛼𝜙, 𝛽𝜙 Hyperparameters for 𝜙𝑖(Gamma distribution) 𝑀𝑖,new Predicted medal count of country 𝑖in future 𝑋2,𝑖 Athlete delegation size 𝑋4,𝑖 Social system congruence (binary) 𝑋6,𝑖 Tactical & strength events 𝑋8,𝑖 Emerging events 𝐺, 𝑆, 𝐵 Gold, silver, and bronze medal counts 𝐴 Coaching ability metric (6G + 3S + B)

<!-- b000827 | prose | pages [5] -->
Before proceeding with modeling, we conducted data cleaning and an initial exploratory

<!-- b000828 | prose | pages [5] -->
m

<!-- b000829 | prose | pages [5] -->
m

<!-- b000830 | prose | pages [5] -->
m

<!-- b000831 | prose | pages [5] -->
m

<!-- b000832 | prose | pages [5] -->
m

<!-- b000833 | prose | pages [5] -->
m

<!-- b000834 | prose | pages [5] -->
m

<!-- b000835 | prose | pages [5] -->
m

<!-- b000836 | prose | pages [5] -->
m

<!-- b000837 | prose | pages [5] -->
m

<!-- b000838 | prose | pages [5] -->
m

<!-- b000839 | prose | pages [5] -->
m

<!-- b000840 | prose | pages [5] -->
m

<!-- b000841 | prose | pages [5] -->
m

<!-- b000842 | prose | pages [5] -->
m

<!-- b000843 | prose | pages [5] -->
m

<!-- b000844 | prose | pages [5] -->
m

<!-- b000845 | prose | pages [5] -->
m

<!-- b000846 | prose | pages [5] -->
m

<!-- b000847 | prose | pages [5] -->
m

<!-- b000848 | prose | pages [5] -->
m

<!-- b000849 | prose | pages [5] -->
m

<!-- b000850 | prose | pages [5] -->
m

<!-- b000851 | prose | pages [5] -->
m

<!-- b000852 | prose | pages [5] -->
m

<!-- b000853 | prose | pages [5] -->
m

<!-- b000854 | prose | pages [5] -->
m

<!-- b000855 | prose | pages [5] -->
m

<!-- b000856 | prose | pages [5] -->
m

<!-- b000857 | prose | pages [5] -->
m

<!-- b000858 | prose | pages [5] -->
m

<!-- b000859 | prose | pages [5] -->
m

<!-- b000860 | prose | pages [5] -->
m

<!-- b000861 | prose | pages [5] -->
m

<!-- b000862 | prose | pages [5] -->
m

<!-- b000863 | prose | pages [5] -->
m

<!-- b000864 | prose | pages [5] -->
m

<!-- b000865 | prose | pages [5] -->
m

<!-- b000866 | prose | pages [5] -->
m

<!-- b000867 | prose | pages [5] -->
m

<!-- b000868 | prose | pages [5] -->
m

<!-- b000869 | prose | pages [5] -->
m

<!-- b000870 | prose | pages [5] -->
m

<!-- b000871 | prose | pages [5] -->
m

<!-- b000872 | prose | pages [5] -->
m

<!-- b000873 | prose | pages [5] -->
m

<!-- b000874 | prose | pages [5] -->
m

<!-- b000875 | prose | pages [5] -->
m

<!-- b000876 | prose | pages [5] -->
m

<!-- b000877 | prose | pages [5] -->
m

<!-- b000878 | prose | pages [5] -->
m

<!-- b000879 | prose | pages [5] -->
m

<!-- b000880 | prose | pages [5] -->
m

<!-- b000881 | prose | pages [5] -->
m

<!-- b000882 | prose | pages [5] -->
m

<!-- b000883 | prose | pages [5] -->
m

<!-- b000884 | prose | pages [5] -->
m

<!-- b000885 | prose | pages [5] -->
m

<!-- b000886 | prose | pages [5] -->
m

<!-- b000887 | prose | pages [5] -->
m

<!-- b000888 | prose | pages [5] -->
m

<!-- b000889 | prose | pages [5] -->
m

<!-- b000890 | prose | pages [5] -->
m

<!-- b000891 | prose | pages [5] -->
m

<!-- b000892 | prose | pages [5] -->
m

<!-- b000893 | prose | pages [5] -->
m

<!-- b000894 | prose | pages [5] -->
m

<!-- b000895 | prose | pages [5] -->
m

<!-- b000896 | prose | pages [5] -->
m

<!-- b000897 | prose | pages [5] -->
m

<!-- b000898 | prose | pages [5] -->
m

<!-- b000899 | prose | pages [5] -->
m

<!-- b000900 | prose | pages [5] -->
m

<!-- b000901 | prose | pages [5] -->
m

<!-- b000902 | prose | pages [5] -->
m

<!-- b000903 | prose | pages [5] -->
m

<!-- b000904 | prose | pages [5] -->
m

<!-- b000905 | prose | pages [5] -->
m

<!-- b000906 | prose | pages [5] -->
m

<!-- b000907 | prose | pages [5] -->
m

<!-- b000908 | prose | pages [5] -->
m

<!-- b000909 | prose | pages [5] -->
m

<!-- b000910 | prose | pages [5] -->
m

<!-- b000911 | prose | pages [5] -->
m

<!-- b000912 | prose | pages [5] -->
m

<!-- b000913 | prose | pages [5] -->
m

<!-- b000914 | prose | pages [5] -->
m

<!-- b000915 | prose | pages [5] -->
m

<!-- b000916 | prose | pages [5] -->
m

<!-- b000917 | prose | pages [5] -->
m

<!-- b000918 | prose | pages [5] -->
m

<!-- b000919 | prose | pages [5] -->
m

<!-- b000920 | prose | pages [5] -->
m

<!-- b000921 | prose | pages [5] -->
m

<!-- b000922 | prose | pages [5] -->
m

<!-- b000923 | prose | pages [5] -->
m

<!-- b000924 | prose | pages [5] -->
m

<!-- b000925 | prose | pages [5] -->
m

<!-- b000926 | prose | pages [5] -->
m

<!-- b000927 | prose | pages [5] -->
m

<!-- b000928 | prose | pages [5] -->
m

<!-- b000929 | prose | pages [5] -->
m

<!-- b000930 | prose | pages [5] -->
m

<!-- b000931 | prose | pages [5] -->
m

<!-- b000932 | prose | pages [5] -->
m

<!-- b000933 | prose | pages [5] -->
m

<!-- b000934 | prose | pages [5] -->
m

<!-- b000935 | prose | pages [5] -->
m

<!-- b000936 | prose | pages [5] -->
analysis to better understand the dataset’s characteristics.

<!-- b000937 | prose | pages [5] -->
m

<!-- b000938 | prose | pages [5] -->
m

<!-- b000939 | prose | pages [5] -->
m

<!-- b000940 | prose | pages [5] -->
m

<!-- b000941 | prose | pages [5] -->
m

<!-- b000942 | prose | pages [5] -->
m

<!-- b000943 | prose | pages [5] -->
m

<!-- b000944 | prose | pages [5] -->
m

<!-- b000945 | prose | pages [5] -->
m

<!-- b000946 | prose | pages [5] -->
m

<!-- b000947 | prose | pages [5] -->
m

<!-- b000948 | prose | pages [5] -->
m

<!-- b000949 | prose | pages [5] -->
m

<!-- b000950 | prose | pages [5] -->
m

<!-- b000951 | prose | pages [5] -->
m

<!-- b000952 | prose | pages [5] -->
m

<!-- b000953 | prose | pages [5] -->
m

<!-- b000954 | prose | pages [5] -->
m

<!-- b000955 | prose | pages [5] -->
m

<!-- b000956 | prose | pages [5] -->
m

<!-- b000957 | prose | pages [5] -->
m

<!-- b000958 | prose | pages [5] -->
m

<!-- b000959 | prose | pages [5] -->
m

<!-- b000960 | prose | pages [5] -->
m

<!-- b000961 | prose | pages [5] -->
m

<!-- b000962 | prose | pages [5] -->
m

<!-- b000963 | prose | pages [5] -->
m

<!-- b000964 | prose | pages [5] -->
m

<!-- b000965 | prose | pages [5] -->
m

<!-- b000966 | prose | pages [5] -->
m

<!-- b000967 | prose | pages [5] -->
m

<!-- b000968 | prose | pages [5] -->
m

<!-- b000969 | prose | pages [5] -->
m

<!-- b000970 | prose | pages [5] -->
m

<!-- b000971 | prose | pages [5] -->
m

<!-- b000972 | prose | pages [5] -->
m

<!-- b000973 | prose | pages [5] -->
m

<!-- b000974 | prose | pages [5] -->
m

<!-- b000975 | prose | pages [5] -->
m

<!-- b000976 | prose | pages [5] -->
m

<!-- b000977 | prose | pages [5] -->
m

<!-- b000978 | prose | pages [5] -->
m

<!-- b000979 | prose | pages [5] -->
m

<!-- b000980 | prose | pages [5] -->
m

<!-- b000981 | prose | pages [5] -->
m

<!-- b000982 | prose | pages [5] -->
m

<!-- b000983 | prose | pages [5] -->
m

<!-- b000984 | prose | pages [5] -->
m

<!-- b000985 | prose | pages [5] -->
m

<!-- b000986 | prose | pages [5] -->
m

<!-- b000987 | prose | pages [5] -->
m

<!-- b000988 | prose | pages [5] -->
m

<!-- b000989 | prose | pages [5] -->
m

<!-- b000990 | prose | pages [5] -->
m

<!-- b000991 | prose | pages [5] -->
m

<!-- b000992 | prose | pages [5] -->
m

<!-- b000993 | prose | pages [5] -->
m

<!-- b000994 | prose | pages [5] -->
m

<!-- b000995 | prose | pages [5] -->
m

<!-- b000996 | prose | pages [5] -->
m

<!-- b000997 | prose | pages [5] -->
m

<!-- b000998 | prose | pages [5] -->
m

<!-- b000999 | prose | pages [5] -->
m

<!-- b001000 | prose | pages [5] -->
m

<!-- b001001 | prose | pages [5] -->
m

<!-- b001002 | prose | pages [5] -->
m

<!-- b001003 | prose | pages [5] -->
m

<!-- b001004 | prose | pages [5] -->
m

<!-- b001005 | prose | pages [5] -->
m

<!-- b001006 | prose | pages [5] -->
m

<!-- b001007 | prose | pages [5] -->
m

<!-- b001008 | prose | pages [5] -->
m

<!-- b001009 | prose | pages [5] -->
m

<!-- b001010 | prose | pages [5] -->
m

<!-- b001011 | prose | pages [5] -->
m

<!-- b001012 | prose | pages [5] -->
m

<!-- b001013 | prose | pages [5] -->
m

<!-- b001014 | prose | pages [5] -->
m

<!-- b001015 | prose | pages [5] -->
m

<!-- b001016 | prose | pages [5] -->
m

<!-- b001017 | prose | pages [5] -->
m

<!-- b001018 | prose | pages [5] -->
m

<!-- b001019 | prose | pages [5] -->
m

<!-- b001020 | prose | pages [5] -->
m

<!-- b001021 | prose | pages [5] -->
m

<!-- b001022 | prose | pages [5] -->
m

<!-- b001023 | prose | pages [5] -->
m

<!-- b001024 | prose | pages [5] -->
m

<!-- b001025 | prose | pages [5] -->
m

<!-- b001026 | prose | pages [5] -->
m

<!-- b001027 | prose | pages [5] -->
m

<!-- b001028 | prose | pages [5] -->
m

<!-- b001029 | prose | pages [5] -->
m

<!-- b001030 | prose | pages [5] -->
m

<!-- b001031 | prose | pages [5] -->
m

<!-- b001032 | prose | pages [5] -->
m

<!-- b001033 | prose | pages [5] -->
m

<!-- b001034 | prose | pages [5] -->
m

<!-- b001035 | prose | pages [5] -->
m

<!-- b001036 | prose | pages [5] -->
m

<!-- b001037 | prose | pages [5] -->
m

<!-- b001038 | prose | pages [5] -->
m

<!-- b001039 | prose | pages [5] -->
m

<!-- b001040 | prose | pages [5] -->
m

<!-- b001041 | prose | pages [5] -->
m

<!-- b001042 | prose | pages [5] -->
m

<!-- b001043 | prose | pages [5] -->
m

<!-- b001044 | prose | pages [5] -->
m

<!-- b001045 | prose | pages [5] -->
m

<!-- b001046 | prose | pages [5] -->
m

<!-- b001047 | prose | pages [5] -->
m

<!-- b001048 | prose | pages [5] -->
m

<!-- b001049 | prose | pages [5] -->
m

<!-- b001050 | prose | pages [5] -->
m

<!-- b001051 | prose | pages [5] -->
m

<!-- b001052 | prose | pages [5] -->
m

<!-- b001053 | prose | pages [5] -->
m

<!-- b001054 | prose | pages [5] -->
m

<!-- b001055 | prose | pages [5] -->
m

<!-- b001056 | prose | pages [5] -->
m

<!-- b001057 | prose | pages [5] -->
m

<!-- b001058 | prose | pages [5] -->
m

<!-- b001059 | prose | pages [5] -->
m

<!-- b001060 | prose | pages [5] -->
m

<!-- b001061 | prose | pages [5] -->
m

<!-- b001062 | prose | pages [5] -->
m

<!-- b001063 | prose | pages [5] -->
m

<!-- b001064 | prose | pages [5] -->
m

<!-- b001065 | prose | pages [5] -->
m

<!-- b001066 | prose | pages [5] -->
m

<!-- b001067 | prose | pages [5] -->
m

<!-- b001068 | prose | pages [5] -->
m

<!-- b001069 | prose | pages [5] -->
m

<!-- b001070 | prose | pages [5] -->
m

<!-- b001071 | prose | pages [5] -->
m

<!-- b001072 | prose | pages [5] -->
m

<!-- b001073 | prose | pages [5] -->
m

<!-- b001074 | prose | pages [5] -->
m

<!-- b001075 | prose | pages [5] -->
m

<!-- b001076 | prose | pages [5] -->
m

<!-- b001077 | prose | pages [5] -->
m

<!-- b001078 | prose | pages [5] -->
m

<!-- b001079 | prose | pages [5] -->
m

<!-- b001080 | prose | pages [5] -->
m

<!-- b001081 | prose | pages [5] -->
m

<!-- b001082 | prose | pages [5] -->
m

<!-- b001083 | prose | pages [5] -->
m

<!-- b001084 | prose | pages [5] -->
m

<!-- b001085 | prose | pages [5] -->
m

<!-- b001086 | prose | pages [5] -->
m

<!-- b001087 | prose | pages [5] -->
m

<!-- b001088 | prose | pages [5] -->
m

<!-- b001089 | prose | pages [5] -->
m

<!-- b001090 | prose | pages [5] -->
m

<!-- b001091 | prose | pages [5] -->
m

<!-- b001092 | prose | pages [5] -->
m

<!-- b001093 | prose | pages [5] -->
m

<!-- b001094 | prose | pages [5] -->
m

<!-- b001095 | prose | pages [5] -->
m

<!-- b001096 | prose | pages [5] -->
m

<!-- b001097 | prose | pages [5] -->
m

<!-- b001098 | prose | pages [5] -->
m

<!-- b001099 | prose | pages [5] -->
m

<!-- b001100 | prose | pages [5] -->
m

<!-- b001101 | prose | pages [5] -->
m

<!-- b001102 | prose | pages [5] -->
m

<!-- b001103 | prose | pages [5] -->
m

<!-- b001104 | prose | pages [5] -->
m

<!-- b001105 | prose | pages [5] -->
m

<!-- b001106 | prose | pages [5] -->
m

<!-- b001107 | prose | pages [5] -->
m

<!-- b001108 | prose | pages [5] -->
m

<!-- b001109 | prose | pages [5] -->
m

<!-- b001110 | prose | pages [5] -->
m

<!-- b001111 | prose | pages [5] -->
m

<!-- b001112 | prose | pages [5] -->
m

<!-- b001113 | furniture | pages [5] -->
m

<!-- b001114 | furniture | pages [5] -->
m

<!-- b001115 | furniture | pages [5] -->
m

<!-- b001116 | furniture | pages [5] -->
m

<!-- b001117 | furniture | pages [5] -->
m

<!-- b001118 | furniture | pages [5] -->
m

<!-- b001119 | furniture | pages [5] -->
m

<!-- b001120 | furniture | pages [5] -->
m

<!-- b001121 | furniture | pages [5] -->
m

<!-- b001122 | furniture | pages [5] -->
m

<!-- b001123 | furniture | pages [5] -->
m

<!-- b001124 | furniture | pages [5] -->
m

<!-- b001125 | furniture | pages [5] -->
m

<!-- b001126 | furniture | pages [5] -->
m

<!-- b001127 | furniture | pages [5] -->
m

<!-- b001128 | furniture | pages [5] -->
m

<!-- b001129 | furniture | pages [5] -->
m

<!-- b001130 | furniture | pages [5] -->
m

<!-- b001131 | furniture | pages [5] -->
m

<!-- b001132 | furniture | pages [5] -->
m

<!-- b001133 | furniture | pages [5] -->
m

<!-- b001134 | furniture | pages [5] -->
m

<!-- b001135 | furniture | pages [5] -->
m

<!-- b001136 | furniture | pages [5] -->
m

<!-- b001137 | furniture | pages [5] -->
m

<!-- b001138 | furniture | pages [5] -->
m

<!-- b001139 | furniture | pages [5] -->
m

<!-- b001140 | furniture | pages [5] -->
m

<!-- b001141 | furniture | pages [5] -->
m

<!-- b001142 | furniture | pages [5] -->
m

<!-- b001143 | furniture | pages [5] -->
m

<!-- b001144 | furniture | pages [5] -->
m

<!-- b001145 | furniture | pages [5] -->
m

<!-- b001146 | furniture | pages [5] -->
m

<!-- b001147 | furniture | pages [5] -->
m

<!-- b001148 | furniture | pages [5] -->
m

<!-- b001149 | furniture | pages [5] -->
m

<!-- b001150 | furniture | pages [5] -->
m

<!-- b001151 | furniture | pages [5] -->
m

<!-- b001152 | furniture | pages [5] -->
m

<!-- b001153 | furniture | pages [5] -->
m

<!-- b001154 | furniture | pages [5] -->
m

<!-- b001155 | furniture | pages [5] -->
m

<!-- b001156 | furniture | pages [5] -->
m

<!-- b001157 | furniture | pages [5] -->
m

<!-- b001158 | furniture | pages [5] -->
m

<!-- b001159 | furniture | pages [5] -->
m

<!-- b001160 | furniture | pages [5] -->
m

<!-- b001161 | furniture | pages [5] -->
m

<!-- b001162 | furniture | pages [5] -->
m

<!-- b001163 | furniture | pages [5] -->
m

<!-- b001164 | furniture | pages [5] -->
m

<!-- b001165 | furniture | pages [5] -->
m

<!-- b001166 | furniture | pages [5] -->
m

<!-- b001167 | furniture | pages [5] -->
m

<!-- b001168 | furniture | pages [5] -->
m

<!-- b001169 | furniture | pages [5] -->
m

<!-- b001170 | furniture | pages [5] -->
m

<!-- b001171 | furniture | pages [5] -->
m

<!-- b001172 | furniture | pages [5] -->
m

<!-- b001173 | furniture | pages [5] -->
m

<!-- b001174 | furniture | pages [5] -->
m

<!-- b001175 | furniture | pages [5] -->
m

<!-- b001176 | furniture | pages [5] -->
m

<!-- b001177 | furniture | pages [5] -->
m

<!-- b001178 | furniture | pages [5] -->
m

<!-- b001179 | furniture | pages [5] -->
m

<!-- b001180 | furniture | pages [5] -->
m

<!-- b001181 | furniture | pages [5] -->
m

<!-- b001182 | furniture | pages [5] -->
m

<!-- b001183 | furniture | pages [5] -->
m

<!-- b001184 | furniture | pages [5] -->
m

<!-- b001185 | furniture | pages [5] -->
m

<!-- b001186 | furniture | pages [5] -->
m

<!-- b001187 | furniture | pages [5] -->
m

<!-- b001188 | furniture | pages [5] -->
m

<!-- b001189 | furniture | pages [5] -->
m

<!-- b001190 | furniture | pages [5] -->
m

<!-- b001191 | furniture | pages [5] -->
m

<!-- b001192 | furniture | pages [5] -->
m

<!-- b001193 | furniture | pages [5] -->
m

<!-- b001194 | furniture | pages [5] -->
m

<!-- b001195 | furniture | pages [5] -->
m

<!-- b001196 | furniture | pages [5] -->
m

<!-- b001197 | furniture | pages [5] -->
m

<!-- b001198 | furniture | pages [5] -->
m

<!-- b001199 | furniture | pages [5] -->
m

<!-- b001200 | furniture | pages [5] -->
m

<!-- b001201 | furniture | pages [5] -->
m

<!-- b001202 | furniture | pages [5] -->
m

<!-- b001203 | furniture | pages [5] -->
m

<!-- b001204 | furniture | pages [5] -->
m

<!-- b001205 | furniture | pages [5] -->
m

<!-- b001206 | furniture | pages [5] -->
m

<!-- b001207 | furniture | pages [5] -->
m

<!-- b001208 | furniture | pages [5] -->
m

<!-- b001209 | furniture | pages [5] -->
m

<!-- b001210 | furniture | pages [5] -->
m

<!-- b001211 | furniture | pages [5] -->
m

<!-- b001212 | furniture | pages [5] -->
m

<!-- b001213 | furniture | pages [5] -->
m

<!-- b001214 | furniture | pages [5] -->
m

<!-- b001215 | furniture | pages [5] -->
m

<!-- b001216 | furniture | pages [5] -->
m

<!-- b001217 | furniture | pages [5] -->
m

<!-- b001218 | furniture | pages [5] -->
m

<!-- b001219 | furniture | pages [5] -->
m

<!-- b001220 | furniture | pages [5] -->
m

<!-- b001221 | furniture | pages [5] -->
m

<!-- b001222 | furniture | pages [5] -->
m

<!-- b001223 | furniture | pages [5] -->
m

<!-- b001224 | furniture | pages [5] -->
m

<!-- b001225 | furniture | pages [5] -->
m

<!-- b001226 | furniture | pages [5] -->
m

<!-- b001227 | furniture | pages [5] -->
m

<!-- b001228 | furniture | pages [5] -->
m

<!-- b001229 | furniture | pages [5] -->
m

<!-- b001230 | furniture | pages [5] -->
m

<!-- b001231 | furniture | pages [5] -->
m

<!-- b001232 | furniture | pages [5] -->
m

<!-- b001233 | furniture | pages [5] -->
m

<!-- b001234 | furniture | pages [5] -->
m

<!-- b001235 | furniture | pages [5] -->
m

<!-- b001236 | furniture | pages [5] -->
m

<!-- b001237 | furniture | pages [5] -->
m

<!-- b001238 | furniture | pages [5] -->
m

<!-- b001239 | furniture | pages [5] -->
m

<!-- b001240 | furniture | pages [5] -->
m

<!-- b001241 | furniture | pages [5] -->
m

<!-- b001242 | furniture | pages [5] -->
m

<!-- b001243 | furniture | pages [5] -->
m

<!-- b001244 | furniture | pages [5] -->
m

<!-- b001245 | furniture | pages [5] -->
m

<!-- b001246 | furniture | pages [5] -->
m

<!-- b001247 | furniture | pages [5] -->
m

<!-- b001248 | furniture | pages [5] -->
m

<!-- b001249 | furniture | pages [5] -->
m

<!-- b001250 | furniture | pages [5] -->
m

<!-- b001251 | furniture | pages [5] -->
m

<!-- b001252 | furniture | pages [5] -->
m

<!-- b001253 | furniture | pages [5] -->
m

<!-- b001254 | furniture | pages [5] -->
m

<!-- b001255 | furniture | pages [5] -->
m

<!-- b001256 | furniture | pages [5] -->
m

<!-- b001257 | furniture | pages [5] -->
m

<!-- b001258 | furniture | pages [5] -->
m

<!-- b001259 | furniture | pages [5] -->
m

<!-- b001260 | furniture | pages [5] -->
m

<!-- b001261 | furniture | pages [5] -->
m

<!-- b001262 | furniture | pages [5] -->
m

<!-- b001263 | furniture | pages [5] -->
m

<!-- b001264 | furniture | pages [5] -->
m

<!-- b001265 | furniture | pages [5] -->
m

<!-- b001266 | furniture | pages [5] -->
m

<!-- b001267 | furniture | pages [5] -->
m

<!-- b001268 | furniture | pages [5] -->
m

<!-- b001269 | furniture | pages [5] -->
m

<!-- b001270 | furniture | pages [5] -->
m

<!-- b001271 | furniture | pages [5] -->
m

<!-- b001272 | furniture | pages [5] -->
m

<!-- b001273 | furniture | pages [5] -->
m

<!-- b001274 | furniture | pages [5] -->
m

<!-- b001275 | furniture | pages [5] -->
m

<!-- b001276 | furniture | pages [5] -->
m

<!-- b001277 | furniture | pages [5] -->
m

<!-- b001278 | furniture | pages [5] -->
m

<!-- b001279 | furniture | pages [5] -->
m

<!-- b001280 | furniture | pages [5] -->
m

<!-- b001281 | furniture | pages [5] -->
m

<!-- b001282 | furniture | pages [5] -->
m

<!-- b001283 | furniture | pages [5] -->
m

<!-- b001284 | furniture | pages [5] -->
m

<!-- b001285 | furniture | pages [5] -->
m

<!-- b001286 | furniture | pages [5] -->
m

<!-- b001287 | furniture | pages [5] -->
m

<!-- b001288 | furniture | pages [5] -->
m

<!-- b001289 | furniture | pages [5] -->
m

<!-- b001290 | furniture | pages [5] -->
m

<!-- b001291 | furniture | pages [5] -->
m

<!-- b001292 | furniture | pages [5] -->
m

<!-- b001293 | furniture | pages [5] -->
m

<!-- b001294 | furniture | pages [5] -->
m

<!-- b001295 | furniture | pages [5] -->
m

<!-- b001296 | furniture | pages [5] -->
m

<!-- b001297 | furniture | pages [5] -->
m

<!-- b001298 | furniture | pages [5] -->
m

<!-- b001299 | furniture | pages [5] -->
m

<!-- b001300 | furniture | pages [5] -->
m

<!-- b001301 | furniture | pages [5] -->
m

<!-- b001302 | furniture | pages [5] -->
m

<!-- b001303 | furniture | pages [5] -->
m

<!-- b001304 | furniture | pages [5] -->
m

<!-- b001305 | furniture | pages [5] -->
m

<!-- b001306 | furniture | pages [5] -->
m

<!-- b001307 | furniture | pages [5] -->
m

<!-- b001308 | furniture | pages [5] -->
m

<!-- b001309 | furniture | pages [5] -->
m

<!-- b001310 | furniture | pages [5] -->
m

<!-- b001311 | furniture | pages [5] -->
m

<!-- b001312 | furniture | pages [5] -->
m

<!-- b001313 | furniture | pages [5] -->
m

<!-- b001314 | furniture | pages [5] -->
m

<!-- b001315 | furniture | pages [5] -->
m

<!-- b001316 | furniture | pages [5] -->
m

<!-- b001317 | furniture | pages [5] -->
m

<!-- b001318 | furniture | pages [5] -->
m

<!-- b001319 | furniture | pages [5] -->
m

<!-- b001320 | furniture | pages [5] -->
m

<!-- b001321 | furniture | pages [5] -->
m

<!-- b001322 | furniture | pages [5] -->
m

<!-- b001323 | furniture | pages [5] -->
m

<!-- b001324 | furniture | pages [5] -->
m

<!-- b001325 | furniture | pages [5] -->
m

<!-- b001326 | furniture | pages [5] -->
m

<!-- b001327 | furniture | pages [5] -->
m

<!-- b001328 | furniture | pages [5] -->
m

<!-- b001329 | furniture | pages [5] -->
m

<!-- b001330 | furniture | pages [5] -->
m

<!-- b001331 | furniture | pages [5] -->
m

<!-- b001332 | furniture | pages [5] -->
m

<!-- b001333 | furniture | pages [5] -->
m

<!-- b001334 | furniture | pages [5] -->
m

<!-- b001335 | furniture | pages [5] -->
m

<!-- b001336 | furniture | pages [5] -->
m

<!-- b001337 | furniture | pages [5] -->
m

<!-- b001338 | furniture | pages [5] -->
m

<!-- b001339 | furniture | pages [5] -->
m

<!-- b001340 | furniture | pages [5] -->
m

<!-- b001341 | furniture | pages [5] -->
m

<!-- b001342 | furniture | pages [5] -->
m

<!-- b001343 | furniture | pages [5] -->
m

<!-- b001344 | furniture | pages [5] -->
m

<!-- b001345 | furniture | pages [5] -->
m

<!-- b001346 | furniture | pages [5] -->
m

<!-- b001347 | furniture | pages [5] -->
m

<!-- b001348 | furniture | pages [5] -->
m

<!-- b001349 | furniture | pages [5] -->
m

<!-- b001350 | furniture | pages [5] -->
m

<!-- b001351 | furniture | pages [5] -->
m

<!-- b001352 | furniture | pages [5] -->
m

<!-- b001353 | furniture | pages [5] -->
m

<!-- b001354 | furniture | pages [5] -->
m

<!-- b001355 | furniture | pages [5] -->
m

<!-- b001356 | furniture | pages [5] -->
m

<!-- b001357 | furniture | pages [5] -->
m

<!-- b001358 | furniture | pages [5] -->
m

<!-- b001359 | furniture | pages [5] -->
m

<!-- b001360 | furniture | pages [5] -->
m

<!-- b001361 | furniture | pages [5] -->
m

<!-- b001362 | furniture | pages [5] -->
m

<!-- b001363 | furniture | pages [5] -->
m

<!-- b001364 | furniture | pages [5] -->
m

<!-- b001365 | furniture | pages [5] -->
m

<!-- b001366 | furniture | pages [5] -->
m

<!-- b001367 | furniture | pages [5] -->
m

<!-- b001368 | furniture | pages [5] -->
m

<!-- b001369 | furniture | pages [5] -->
m

<!-- b001370 | furniture | pages [5] -->
m

<!-- b001371 | furniture | pages [5] -->
m

<!-- b001372 | furniture | pages [5] -->
m

<!-- b001373 | furniture | pages [5] -->
m

<!-- b001374 | furniture | pages [5] -->
m

<!-- b001375 | furniture | pages [5] -->
m

<!-- b001376 | furniture | pages [5] -->
m

<!-- b001377 | furniture | pages [5] -->
m

<!-- b001378 | furniture | pages [5] -->
m

<!-- b001379 | furniture | pages [5] -->
m

<!-- b001380 | furniture | pages [5] -->
m

<!-- b001381 | furniture | pages [5] -->
m

<!-- b001382 | furniture | pages [5] -->
m

<!-- b001383 | furniture | pages [5] -->
m

<!-- b001384 | furniture | pages [5] -->
m

<!-- b001385 | furniture | pages [5] -->
m

<!-- b001386 | furniture | pages [5] -->
m

<!-- b001387 | furniture | pages [5] -->
m

<!-- b001388 | furniture | pages [5] -->
m

<!-- b001389 | furniture | pages [5] -->
m

<!-- b001390 | furniture | pages [5] -->
m

<!-- b001391 | furniture | pages [5] -->
m

<!-- b001392 | furniture | pages [5] -->
m

<!-- b001393 | furniture | pages [5] -->
m

<!-- b001394 | furniture | pages [5] -->
m

<!-- b001395 | furniture | pages [5] -->
m

<!-- b001396 | furniture | pages [5] -->
m

<!-- b001397 | furniture | pages [5] -->
m

<!-- b001398 | furniture | pages [5] -->
m

<!-- b001399 | furniture | pages [5] -->
m

<!-- b001400 | furniture | pages [5] -->
m

<!-- b001401 | furniture | pages [5] -->
m

<!-- b001402 | furniture | pages [5] -->
m

<!-- b001403 | furniture | pages [5] -->
m

<!-- b001404 | furniture | pages [5] -->
m

<!-- b001405 | furniture | pages [5] -->
m

<!-- b001406 | furniture | pages [5] -->
m

<!-- b001407 | furniture | pages [5] -->
m

<!-- b001408 | furniture | pages [5] -->
m

<!-- b001409 | furniture | pages [5] -->
m

<!-- b001410 | furniture | pages [5] -->
m

<!-- b001411 | furniture | pages [5] -->
m

<!-- b001412 | furniture | pages [5] -->
m

<!-- b001413 | furniture | pages [5] -->
m

<!-- b001414 | furniture | pages [5] -->
m

<!-- b001415 | furniture | pages [5] -->
m

<!-- b001416 | furniture | pages [5] -->
m

<!-- b001417 | furniture | pages [5] -->
m

<!-- b001418 | furniture | pages [5] -->
m

<!-- b001419 | furniture | pages [5] -->
m

<!-- b001420 | furniture | pages [5] -->
m

<!-- b001421 | furniture | pages [5] -->
m

<!-- b001422 | furniture | pages [5] -->
m

<!-- b001423 | furniture | pages [5] -->
m

<!-- b001424 | furniture | pages [5] -->
m

<!-- b001425 | furniture | pages [5] -->
m

<!-- b001426 | furniture | pages [5] -->
m

<!-- b001427 | furniture | pages [5] -->
m

<!-- b001428 | furniture | pages [5] -->
m

<!-- b001429 | furniture | pages [5] -->
m

<!-- b001430 | furniture | pages [5] -->
m

<!-- b001431 | furniture | pages [5] -->
m

<!-- b001432 | furniture | pages [5] -->
m

<!-- b001433 | furniture | pages [5] -->
m

<!-- b001434 | furniture | pages [5] -->
m

<!-- b001435 | furniture | pages [5] -->
m

<!-- b001436 | furniture | pages [5] -->
m

<!-- b001437 | furniture | pages [5] -->
m

<!-- b001438 | furniture | pages [5] -->
m

<!-- b001439 | furniture | pages [5] -->
m

<!-- b001440 | furniture | pages [5] -->
m

<!-- b001441 | furniture | pages [5] -->
m

<!-- b001442 | furniture | pages [5] -->
m

<!-- b001443 | furniture | pages [5] -->
m

<!-- b001444 | furniture | pages [5] -->
m

<!-- b001445 | furniture | pages [5] -->
m

<!-- b001446 | furniture | pages [5] -->
m

<!-- b001447 | furniture | pages [5] -->
m

<!-- b001448 | furniture | pages [5] -->
m

<!-- b001449 | furniture | pages [5] -->
m

<!-- b001450 | furniture | pages [5] -->
m

<!-- b001451 | furniture | pages [5] -->
m

<!-- b001452 | furniture | pages [5] -->
m

<!-- b001453 | furniture | pages [5] -->
m

<!-- b001454 | furniture | pages [5] -->
m

<!-- b001455 | furniture | pages [5] -->
m

<!-- b001456 | furniture | pages [5] -->
m

<!-- b001457 | furniture | pages [5] -->
m

<!-- b001458 | furniture | pages [5] -->
m

<!-- b001459 | furniture | pages [5] -->
m

<!-- b001460 | furniture | pages [5] -->
m

<!-- b001461 | furniture | pages [5] -->
m

<!-- b001462 | furniture | pages [5] -->
m

<!-- b001463 | furniture | pages [5] -->
m

<!-- b001464 | furniture | pages [5] -->
m

<!-- b001465 | furniture | pages [5] -->
m

<!-- b001466 | furniture | pages [5] -->
m

<!-- b001467 | furniture | pages [5] -->
m

<!-- b001468 | furniture | pages [5] -->
m

<!-- b001469 | furniture | pages [5] -->
m

<!-- b001470 | furniture | pages [5] -->
m

<!-- b001471 | furniture | pages [5] -->
m

<!-- b001472 | furniture | pages [5] -->
m

<!-- b001473 | furniture | pages [5] -->
m

<!-- b001474 | furniture | pages [5] -->
m

<!-- b001475 | furniture | pages [5] -->
m

<!-- b001476 | furniture | pages [5] -->
m

<!-- b001477 | furniture | pages [5] -->
m

<!-- b001478 | furniture | pages [5] -->
m

<!-- b001479 | furniture | pages [5] -->
m

<!-- b001480 | furniture | pages [5] -->
m

<!-- b001481 | furniture | pages [5] -->
m

<!-- b001482 | furniture | pages [5] -->
m

<!-- b001483 | furniture | pages [5] -->
m

<!-- b001484 | furniture | pages [5] -->
m

<!-- b001485 | furniture | pages [5] -->
m

<!-- b001486 | furniture | pages [5] -->
m

<!-- b001487 | furniture | pages [5] -->
m

<!-- b001488 | furniture | pages [5] -->
m

<!-- b001489 | furniture | pages [5] -->
m

<!-- b001490 | furniture | pages [5] -->
m

<!-- b001491 | furniture | pages [5] -->
m

<!-- b001492 | furniture | pages [5] -->
m

<!-- b001493 | furniture | pages [5] -->
m

<!-- b001494 | furniture | pages [5] -->
m

<!-- b001495 | furniture | pages [5] -->
m

<!-- b001496 | furniture | pages [5] -->
m

<!-- b001497 | furniture | pages [5] -->
m

<!-- b001498 | furniture | pages [5] -->
m

<!-- b001499 | furniture | pages [5] -->
m

<!-- b001500 | furniture | pages [5] -->
m

<!-- b001501 | furniture | pages [5] -->
m

<!-- b001502 | furniture | pages [5] -->
m

<!-- b001503 | furniture | pages [5] -->
m

<!-- b001504 | furniture | pages [5] -->
m

<!-- b001505 | furniture | pages [5] -->
m

<!-- b001506 | furniture | pages [5] -->
m

<!-- b001507 | furniture | pages [5] -->
m

<!-- b001508 | furniture | pages [5] -->
m

<!-- b001509 | furniture | pages [5] -->
m

<!-- b001510 | furniture | pages [5] -->
m

<!-- b001511 | furniture | pages [5] -->
m

<!-- b001512 | furniture | pages [5] -->
m

<!-- b001513 | furniture | pages [5] -->
m

<!-- b001514 | furniture | pages [5] -->
m

<!-- b001515 | furniture | pages [5] -->
m

<!-- b001516 | furniture | pages [7] -->
Team # 2513314

<!-- b001517 | furniture | pages [7] -->
Page 7 of 22

<!-- b001518 | heading | pages [7] -->
1. Economic Capacity.

<!-- b001519 | prose | pages [7] -->
Historical Medal Record (𝑋1): Reflects a country’s medal haul in the immediately preceding

<!-- b001520 | prose | pages [7] -->
Olympic cycle (for gold-medal-focused forecasts, this specifically denotes the previous count of gold medals).

<!-- b001521 | prose | pages [7] -->
A strong performance history is frequently underpinned by

<!-- b001522 | prose | pages [7] -->
微信公众号：数学模型

<!-- b001523 | prose | pages [7] -->
consistent investment in athletic programs and robust training infrastructures.

<!-- b001524 | prose | pages [7] -->
Athlete Delegation Size (𝑋2): Represents the total number of athletes sent to the current

<!-- b001525 | prose | pages [7] -->
Games, serving as a proxy measure of institutional support and the breadth of a na- tion’s talent pool. Larger delegations often correlate with stronger financial backing and more extensive development pathways in multiple sporting disciplines.

<!-- b001526 | heading | pages [7] -->
2. Hosting Advantages.

<!-- b001527 | prose | pages [7] -->
Host Nation Flag (𝑋3 ∈{0, 1}): Indicates whether a nation is the host (𝑋3 = 1). Host countries

<!-- b001528 | prose | pages [7] -->
frequently capitalize on superior familiarity with the local environment, elevated fan

<!-- b001529 | prose | pages [7] -->
微信号：MATHmodels

<!-- b001530 | prose | pages [7] -->
support, and logistical conveniences.

<!-- b001531 | prose | pages [7] -->
Social System Congruence (𝑋4 ∈{0, 1}): Identifies nations whose social or institutional struc-

<!-- b001532 | prose | pages [7] -->
tures are closely aligned with those of the host (𝑋4 = 1). Such alignment can minimize cultural barriers and facilitate smoother acclimatization, indirectly bolstering athletic per- formance.

<!-- b001533 | heading | pages [7] -->
3. Event-Specific Attributes.

<!-- b001534 | prose | pages [7] -->
Substantial heterogeneity exists across Olympic events, with certain countries historically excelling in specific domains. Cultural traditions, regional training practices, and even genetic predispositions can foster a competitive edge in certain sports [6]. To capture this diversity, we classify events into four key segments:

<!-- b001535 | prose | pages [7] -->
Athletics Events (𝑋5): Comprising all track and field competitions, a domain frequently marked

<!-- b001536 | prose | pages [7] -->
by widespread global participation and prominent displays of speed, endurance, and agility.

<!-- b001537 | heading | pages [7] -->
Tactical & Strength Events (𝑋6): Encompassessportssuchasfencing, racquetsports, wrestling,

<!-- b001538 | prose | pages [7] -->
and weightlifting, where strategic thinking, technical skills, and physical power play in- terdependent roles.

<!-- b001539 | prose | pages [7] -->
Ball Sports Events (𝑋7): Encompassing team-focused competitions including football, bas-

<!-- b001540 | prose | pages [7] -->
ketball, and volleyball, these events rely heavily on synergy among participants and well-established support systems.

<!-- b001541 | prose | pages [7] -->
Emerging Events (𝑋8): NewlyintroduceddisciplinesorcontestsdebutinginthecurrentOlympic

<!-- b001542 | prose | pages [7] -->
cycle. Nations pioneering these events may enjoy early-adopter advantages but also face higher uncertainty due to the limited availability of historical data.

<!-- b001543 | prose | pages [7] -->
Overall, these variables not only serve as potential predictors in quantitative analyses but also offer a structured lens for examining how resources, environmental factors, and sport-specific nuances collectively shape a nation’s Olympic performance.

<!-- b001544 | prose | pages [7] -->
5.2

<!-- b001545 | heading | pages [7] -->
Bayesian Hierarchical Dirichlet–Multinomial (BHDM) Model

<!-- b001546 | prose | pages [7] -->
Section 4.2 reveals that Olympic medal data typically demand integer-valued predictions that sum to a known total, often exhibit overdispersion and heavy tails, and require partial pooling

<!-- b001547 | prose | pages [7] -->
m

<!-- b001548 | prose | pages [7] -->
m

<!-- b001549 | prose | pages [7] -->
m

<!-- b001550 | prose | pages [7] -->
m

<!-- b001551 | prose | pages [7] -->
m

<!-- b001552 | prose | pages [7] -->
m

<!-- b001553 | prose | pages [7] -->
m

<!-- b001554 | prose | pages [7] -->
m

<!-- b001555 | prose | pages [7] -->
m

<!-- b001556 | prose | pages [7] -->
m

<!-- b001557 | prose | pages [7] -->
m

<!-- b001558 | prose | pages [7] -->
m

<!-- b001559 | prose | pages [7] -->
m

<!-- b001560 | prose | pages [7] -->
m

<!-- b001561 | prose | pages [7] -->
m

<!-- b001562 | prose | pages [7] -->
m

<!-- b001563 | prose | pages [7] -->
m

<!-- b001564 | prose | pages [7] -->
m

<!-- b001565 | prose | pages [7] -->
m

<!-- b001566 | prose | pages [7] -->
m

<!-- b001567 | prose | pages [7] -->
m

<!-- b001568 | prose | pages [7] -->
m

<!-- b001569 | prose | pages [7] -->
m

<!-- b001570 | prose | pages [7] -->
m

<!-- b001571 | prose | pages [7] -->
m

<!-- b001572 | prose | pages [7] -->
m

<!-- b001573 | prose | pages [7] -->
m

<!-- b001574 | prose | pages [7] -->
m

<!-- b001575 | prose | pages [7] -->
m

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
to handle cross-country heterogeneity. Under this distributional constraint, deep learning and

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
machine learning methods (e.g., RNN and two-stage RF) are clearly unsuitable, as they fail

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

<!-- b001833 | furniture | pages [7] -->
m

<!-- b001834 | furniture | pages [7] -->
m

<!-- b001835 | furniture | pages [7] -->
m

<!-- b001836 | furniture | pages [7] -->
m

<!-- b001837 | furniture | pages [7] -->
m

<!-- b001838 | furniture | pages [7] -->
m

<!-- b001839 | furniture | pages [7] -->
m

<!-- b001840 | furniture | pages [7] -->
m

<!-- b001841 | furniture | pages [7] -->
m

<!-- b001842 | furniture | pages [7] -->
m

<!-- b001843 | furniture | pages [7] -->
m

<!-- b001844 | furniture | pages [7] -->
m

<!-- b001845 | furniture | pages [7] -->
m

<!-- b001846 | furniture | pages [7] -->
m

<!-- b001847 | furniture | pages [7] -->
m

<!-- b001848 | furniture | pages [7] -->
m

<!-- b001849 | furniture | pages [7] -->
m

<!-- b001850 | furniture | pages [7] -->
m

<!-- b001851 | furniture | pages [7] -->
m

<!-- b001852 | furniture | pages [7] -->
m

<!-- b001853 | furniture | pages [7] -->
m

<!-- b001854 | furniture | pages [7] -->
m

<!-- b001855 | furniture | pages [7] -->
m

<!-- b001856 | furniture | pages [7] -->
m

<!-- b001857 | furniture | pages [7] -->
m

<!-- b001858 | furniture | pages [7] -->
m

<!-- b001859 | furniture | pages [7] -->
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

<!-- b002236 | furniture | pages [8] -->
Team # 2513314

<!-- b002237 | furniture | pages [8] -->
Page 8 of 22

<!-- b002238 | prose | pages [8] -->
to enforce the fixed-total and discrete conditions without special modifications.

<!-- b002239 | prose | pages [8] -->
Statistical approaches such as Negative Binomial and Poisson are also inadequate due to their poor

<!-- b002240 | heading | pages [8] -->
handling of long-tailed data. While a standard Bayesian Multinomial Model can effectively

<!-- b002241 | prose | pages [8] -->
model such data, it does not satisfy our Country Heterogeneity Assumption, as it assumes a shared 𝜷across all countries, which is incompatible with our framework.

<!-- b002242 | prose | pages [8] -->
The Bayesian Hierarchical Dirichlet–Multinomial (BHDM) model addresses these challenges by combining a Dirichlet–Multinomial likelihood, which enforces both discreteness and sum constraints, with hierarchical priors on regression parameters, enabling each country to have its own coefficient vector.

<!-- b002243 | prose | pages [8] -->
 be the observed medal

<!-- b002244 | prose | pages [8] -->
Model Setup. Let 𝑁be the number of countries, and let  𝑀1, . . . , 𝑀𝑁

<!-- b002245 | prose | pages [8] -->
counts, with the total

<!-- b002246 | prose | pages [8] -->
𝑇=

<!-- b002247 | prose | pages [8] -->
𝑁 𝑁 ∑︁

<!-- b002248 | prose | pages [8] -->
𝑀𝑖.

<!-- b002249 | prose | pages [8] -->
(1)

<!-- b002250 | prose | pages [8] -->
𝑖=1

<!-- b002251 | prose | pages [8] -->
For each country 𝑖, we define a covariate vector x𝑖and a random coefficient vector 𝜷𝑖. In our setting, we adopt a weakly informative prior for 𝜷𝑖, specifically assuming that

<!-- b002252 | prose | pages [8] -->


<!-- b002253 | prose | pages [8] -->
𝝁𝛽, Σ𝛽

<!-- b002254 | prose | pages [8] -->
𝜷𝑖∼N

<!-- b002255 | prose | pages [8] -->
with

<!-- b002256 | prose | pages [8] -->
Σ𝛽= 𝜏2𝐼𝑝

<!-- b002257 | prose | pages [8] -->
 

<!-- b002258 | prose | pages [8] -->
, , 𝑖= 1, . . . , 𝑁, (2)

<!-- b002259 | prose | pages [8] -->
𝜏2 = 1. and

<!-- b002260 | prose | pages [8] -->
This choice reflects our prior belief that, while allowing for moderate variation in the regression coefficients across countries, the individual effects should not be overly dispersed. The weakly informative prior thus provides regularization without imposing overly restrictive assumptions, enabling the data to primarily inform the posterior inferences.

<!-- b002261 | prose | pages [8] -->
m

<!-- b002262 | prose | pages [8] -->
m

<!-- b002263 | prose | pages [8] -->
m

<!-- b002264 | prose | pages [8] -->
m

<!-- b002265 | prose | pages [8] -->
m

<!-- b002266 | prose | pages [8] -->
m

<!-- b002267 | prose | pages [8] -->
m

<!-- b002268 | prose | pages [8] -->
m

<!-- b002269 | prose | pages [8] -->
m

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
We additionally introduce a concentration parameter 𝜙𝑖for country 𝑖:

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
𝜙𝑖∼Gamma(𝛼𝜙, 𝛽𝜙).

<!-- b002611 | prose | pages [8] -->
Each country 𝑖has an associated feature vector

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
(3)

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
⊤,

<!-- b002953 | prose | pages [8] -->
x𝑖=  𝑋1,𝑖, 𝑋2,𝑖, 𝑋3,𝑖, 𝑋4,𝑖, 𝑋5,𝑖, 𝑋6,𝑖, 𝑋7,𝑖, 𝑋8,𝑖

<!-- b002954 | prose | pages [8] -->
Combining these, each country’s latent rate is

<!-- b002955 | prose | pages [8] -->
(4)

<!-- b002956 | prose | pages [8] -->


<!-- b002957 | prose | pages [8] -->


<!-- b002958 | prose | pages [8] -->
x⊤

<!-- b002959 | prose | pages [8] -->
𝜃𝑖= 𝜙𝑖exp

<!-- b002960 | prose | pages [8] -->
.

<!-- b002961 | prose | pages [8] -->
𝑖𝜷𝑖

<!-- b002962 | prose | pages [8] -->
(5)

<!-- b002963 | prose | pages [8] -->
 follows a Dirichlet–Multinomial distribution:

<!-- b002964 | prose | pages [8] -->
Conditioned on {𝜃𝑖}, the vector  𝑀1, . . . , 𝑀𝑁

<!-- b002965 | prose | pages [8] -->
 ∼Dirichlet-Multinomial 𝑇; 𝜃1, . . . , 𝜃𝑁

<!-- b002966 | prose | pages [8] -->
 𝑀1, . . . , 𝑀𝑁

<!-- b002967 | prose | pages [8] -->
ensuring each 𝑀𝑖is integer-valued and that Í𝑁

<!-- b002968 | prose | pages [8] -->
, (6)

<!-- b002969 | prose | pages [8] -->
𝑖=1 𝑀𝑖= 𝑇. Let M = (𝑀1, . . . , 𝑀𝑁) and recall 𝜃𝑖as in (5). Posterior Distribution.

<!-- b002970 | prose | pages [8] -->
Combining the likelihood Eq. (6) with hierarchical priors leads to

<!-- b002971 | prose | pages [8] -->
M

<!-- b002972 | prose | pages [8] -->
𝑝 {𝜷𝑖}, {𝜙𝑖}, 𝝁𝛽, Σ𝛽

<!-- b002973 | prose | pages [8] -->


<!-- b002974 | prose | pages [8] -->
𝑁

<!-- b002975 | prose | pages [8] -->


<!-- b002976 | prose | pages [8] -->
h

<!-- b002977 | prose | pages [8] -->
i

<!-- b002978 | prose | pages [8] -->
Ö

<!-- b002979 | prose | pages [8] -->
M; 𝜃1, . . . , 𝜃𝑁

<!-- b002980 | prose | pages [8] -->
∝Dirichlet-Multinomial

<!-- b002981 | prose | pages [8] -->
𝑁

<!-- b002982 | prose | pages [8] -->
h

<!-- b002983 | prose | pages [8] -->
i

<!-- b002984 | prose | pages [8] -->
Ö

<!-- b002985 | prose | pages [8] -->
N  𝜷𝑖; 𝝁𝛽, Σ𝛽

<!-- b002986 | prose | pages [8] -->
×

<!-- b002987 | prose | pages [8] -->
×

<!-- b002988 | prose | pages [8] -->
(7)

<!-- b002989 | prose | pages [8] -->
𝑖=1

<!-- b002990 | prose | pages [8] -->
× 𝑝(𝝁𝛽, Σ𝛽) · · ·

<!-- b002991 | prose | pages [8] -->
Gamma 𝜙𝑖; 𝛼𝜙, 𝛽𝜙

<!-- b002992 | prose | pages [8] -->
𝑖=1

<!-- b002993 | prose | pages [8] -->
关注数学模型

<!-- b002994 | furniture | pages [8] -->
2

<!-- b002995 | furniture | pages [8] -->
MATHmodels

<!-- b002996 | furniture | pages [8] -->
获取更多资讯

<!-- b002997 | furniture | pages [10] -->
Team # 2513314

<!-- b002998 | prose | pages [10] -->
5.3 Projects of LA 2028

<!-- b002999 | furniture | pages [10] -->
Page 10 of 22

<!-- b003000 | prose | pages [10] -->
By the Equal Distribution Assumption, we use the 2024 data as a proxy for 2028, modifying only the host country. The features are then incorporated into our model and compared against other approaches, with results presented in Table 2. As shown in Table 2, our proposed BHDM model outperforms both the machine/deep learning and traditional statistical approaches in predicting medal counts. For instance, in the All Medals category, BHDM achieves an MSE of 6.98 and an 𝑅2 of 0.85, which are notably superior to the corresponding values from the competing models that exhibit higher errors and lower fit indices. Similarly, in the Gold Medals category, BHDM records an MSE of 3.42 and an 𝑅2 of 0.80, outperforming alternative models by a substantial margin. These improvements are primarily attributable to the BHDM model’s adaptive capability in capturing the underlying data distribution, thereby effectively modeling the intrinsic variability and complex relationships in the dataset, which in turn results in more accurate predictions.

<!-- b003001 | caption | pages [10] -->
Table 2: Comparison of Model Performance Metrics for Medal Prediction. Lower values for MSE,

<!-- b003002 | prose | pages [10] -->
RMSE, and MAE indicate better performance, while higher values for 𝑅2 and Adjusted 𝑅2 indicate a better model fit. The best performance for each metric is highlighted in bold.

<!-- b003003 | prose | pages [10] -->
Machine/Deep Learning Models Statistical Models

<!-- b003004 | prose | pages [10] -->
RF Two-stage[5] Medal Type Metric XGBoost[1] RNN[3]

<!-- b003005 | prose | pages [10] -->
MSE 7.21 7.05 RMSE 2.72 2.65

<!-- b003006 | prose | pages [10] -->
All Medals

<!-- b003007 | prose | pages [10] -->
MAE 1.15 1.12 𝑅2 0.84 0.83 Adjusted 𝑅2 0.82 0.78

<!-- b003008 | prose | pages [10] -->
MSE 3.71 3.63 RMSE 1.93 1.91

<!-- b003009 | prose | pages [10] -->
Gold Medals

<!-- b003010 | prose | pages [10] -->
MAE 1.03 0.99 𝑅2 0.76 0.79 Adjusted 𝑅2 0.74 0.75

<!-- b003011 | prose | pages [10] -->
Poisson Neg. Binomial BHDM (ours)

<!-- b003012 | prose | pages [10] -->
6.98 7.37 10.45 10.33 2.59 2.78 3.21 3.15 1.03 1.17 1.58 1.52 0.85 0.77 0.71 0.74 0.84 0.74 0.68 0.69

<!-- b003013 | prose | pages [10] -->
3.42 3.82 5.25 5.12 1.86 1.95 2.29 2.26 0.95 1.04 1.23 1.25 0.80 0.71 0.66 0.71 0.78 0.68 0.62 0.69

<!-- b003014 | prose | pages [10] -->
Based on our Bayesian hierarchical model, our projections for the Los Angeles 2028 Olympic medal table is shown in Figure 4. It suggests that the United States will significantly improve its performance with a predicted total of 146 medals (95% CI: [136, 156]) and 53 gold medals (95% CI: [50, 56]), reflecting increases of +20 total and +13 gold medals relative to 2024; in contrast, China is forecast to decline to 82 total medals (95% CI: [75, 90]) and 31 gold medals (95% CI: [28, 34]), while Great Britain is expected to drop by 5 total medals (down to 60) and lose 2 gold medals (resulting in 12 gold medals). Moreover, after adjusting for the home advantage effect in 2024, France is projected to regress by 10 total medals (to 54) and 4 gold medals (to 12). Meanwhile, both Australia and Japan exhibit modest improvements, and the Netherlands shows a strong upward trend with an increase of 11 total medals and 5 gold medals. Overall, our model indicates that the United States and the Netherlands are most likely to improve, whereas China, Great Britain, France, Italy, and South Korea are expected to perform worse than in 2024. The 95% credible intervals, derived from the posterior predictive draws, quantify the uncertainty in our predictions and provide a robust framework for interpreting the range of plausible future outcomes.

<!-- b003015 | prose | pages [10] -->
关注数学模型

<!-- b003016 | furniture | pages [10] -->
2

<!-- b003017 | furniture | pages [10] -->
MATHmodels

<!-- b003018 | furniture | pages [10] -->
获取更多资讯

<!-- b003019 | furniture | pages [11] -->
Team # 2513314

<!-- b003020 | furniture | pages [11] -->
Page 11 of 22

<!-- b003021 | caption | pages [11] -->
Figure 4: Predicted Medal Allocations for LA 2028. Gold bars represent gold medals and silver bars

<!-- b003022 | prose | pages [11] -->
represent other medals; the solid black line shows the total medal prediction, the dashed dark orange line shows the gold medal prediction, and the shaded areas indicate the 95% credible intervals.

<!-- b003023 | prose | pages [11] -->
微信公众号：数学模型

<!-- b003024 | prose | pages [11] -->
微信号：MATHmodels

<!-- b003025 | caption | pages [11] -->
Table 3: Probabilities of the country that will achieve a Breakthrough From Zero in 2028.

<!-- b003026 | prose | pages [11] -->
Category Country

<!-- b003027 | prose | pages [11] -->
Malaysia

<!-- b003028 | prose | pages [11] -->
Gold

<!-- b003029 | prose | pages [11] -->
Refugee Olympic Team Haiti

<!-- b003030 | prose | pages [11] -->
South Sudan

<!-- b003031 | prose | pages [11] -->
Total

<!-- b003032 | prose | pages [11] -->
Guinea Myanmar

<!-- b003033 | prose | pages [11] -->
Probability 95% CI

<!-- b003034 | prose | pages [11] -->
0.6861 [0.4568, 0.8132] 0.3788 [0.3214, 0.4128] 0.2569 [0.2112, 0.0.2698]

<!-- b003035 | prose | pages [11] -->
0.3904 [0.3315, 0.4208] 0.3227 [0.2774, 0.3518] 0.1554 [0.1102, 0.1898]

<!-- b003036 | prose | pages [11] -->
The country that will achieve a Breakthrough From Zero 5.4

<!-- b003037 | caption | pages [11] -->
Table 3 presents the estimated probabilities—with associated 95% credible intervals—for

<!-- b003038 | prose | pages [11] -->
each country to achieve a breakthrough from a zero-medal history in the 2028 Olympics. Same as above, the results are stratified into two medal groups: Gold and Total. Gold Medals

<!-- b003039 | prose | pages [11] -->
• Malaysia: The estimated probability for Malaysia to secure its first gold medal is 0.6861, with a relatively wide 95% credible interval of [0.4568, 0.8132]. This interval indicates that while the central estimate is notably high, there is considerable uncertainty in the exact probability. Nonetheless, even the lower bound of approximately 0.46 suggests a strong underlying signal for Malaysia’s breakthrough potential in the gold medal group. • Refugee Olympic Team: With an estimated breakthrough probability of 0.3788 and a narrower credible interval of [0.3214, 0.4128], the Refugee Olympic Team exhibits a moderate level of potential. The narrow interval reflects greater precision in this estimate, implying that the model is more confident about this moderate probability relative to that

<!-- b003040 | furniture | pages [12] -->
Team # 2513314

<!-- b003041 | prose | pages [12] -->
of Malaysia.

<!-- b003042 | furniture | pages [12] -->
Page 12 of 22

<!-- b003043 | prose | pages [12] -->
• Haiti: Haiti’s estimated probability stands at 0.2569 with a 95% credible interval of The relatively low point estimate, coupled with a narrow interval, [0.2112, 0.2698]. reinforces the conclusion that Haiti is less likely to achieve a breakthrough in the gold medal group. The tight range indicates high confidence in this low probability estimate. The stark contrast in point estimates—particularly the high probability for Malaysia com- pared to the lower probabilities for the Refugee Olympic Team and Haiti—highlights a notable disparity in the competitive dynamics for gold medals. Total Medals

<!-- b003044 | prose | pages [12] -->
• South Sudan: In the Total Medal group, South Sudan exhibits the highest breakthrough probability at 0.3904, with a credible interval of [0.3315, 0.4208]. Although this estimate is lower than Malaysia’s gold medal probability, it indicates that South Sudan has a competitive edge when considering all medal types combined. • Guinea: Guinea’s estimated probability is 0.3227 with a 95% credible interval of [0.2774, 0.3518]. The interval for Guinea overlaps somewhat with that of South Sudan, suggesting that while South Sudan has a slight advantage, the difference between these two countries might not be statistically significant under a Bayesian framework. • Myanmar: Myanmar has the lowest estimated probability in the Total group at 0.1554, with a credible interval of [0.1102, 0.1898]. This clearly distinguishes Myanmar from the other candidates in terms of breakthrough potential for accumulating any medals. The Total Medal group exhibits a more evenly distributed set of probabilities compared to the Gold Medal group. While the overall probabilities are lower, the differences among the countries (particularly between South Sudan and Guinea) appear less pronounced. This may reflect the broader range of events and competitive factors that come into play when considering the entire medal tally, as opposed to the singular focus required for a gold medal achievement.

<!-- b003045 | prose | pages [12] -->
Important Sports and Home Event Impact 5.5

<!-- b003046 | prose | pages [12] -->
Events and Medal Acquisition Analysis: The regression coefficients in Table 4 reveal that event-specific attributes are critical determinants of Olympic medal success, with notable dif- ferences across countries. For example, in the United States, the coefficient for Ball Sports Events (X7) is 0.03123 with a high posterior probability of 0.98, indicating that team sports such as basketball and football substantially drive medal acquisition. Similarly, Athletics Events (X5) show a positive effect (beta = 0.02345, Pr(𝛽> 0) = 0.97), suggesting that traditional track and field competitions are also important. In contrast, China displays a relatively modest effect for Athletics Events (X5, beta = 0.01567, Pr(𝛽> 0) = 0.92) but a more pronounced impact for Emerging Events (X8, beta = 0.01765, Pr(𝛽> 0) = 0.93), which implies that their strategic diversification into new sports disciplines plays a significant role in enhancing their medal prospects. Moreover, both the United Kingdom (beta for X5 = 0.02678, Pr(𝛽> 0) = 0.98) and France (beta for X5 = 0.02631, Pr(𝛽> 0) = 0.97) exhibit strong positive associations with Athletics Events, reinforcing the view that specific sports domains are aligned with each country’s historical strengths and strategic investments. Impact of Home Country Event Selection: The regression results in Table 4 also underscore the importance of tailoring event selection to leverage home advantage. When a country hosts the Olympics, it can capitalize on localized benefits such as familiar venues, superior logistical support, and heightened fan enthusiasm. For instance, the United States demonstrates strong positive effects in Athletics Events (X5, beta = 0.02345, 95% CI: [−0.00007, 0.04697]) and even more so in Ball Sports Events (X7, beta = 0.03123, 95% CI: [0.00771, 0.05475]), suggesting that emphasizing these sports can maximize the inherent benefits of home advantage. Similarly, in the United Kingdom and France, Athletics Events yield robust positive coefficients (UK: beta

<!-- b003047 | prose | pages [12] -->
关注数学模型

<!-- b003048 | furniture | pages [12] -->
2

<!-- b003049 | furniture | pages [12] -->
MATHmodels

<!-- b003050 | furniture | pages [12] -->
获取更多资讯

<!-- b003051 | furniture | pages [13] -->
Team # 2513314

<!-- b003052 | furniture | pages [13] -->
Page 13 of 22

<!-- b003053 | caption | pages [13] -->
Table 4: Posterior summary statistics for regression coefficients for various predictors across 4 countries.

<!-- b003054 | prose | pages [13] -->
Variable United States

<!-- b003055 | prose | pages [13] -->
Pr(𝛽> 0) Beta Std. Err.

<!-- b003056 | prose | pages [13] -->
95% CI

<!-- b003057 | prose | pages [13] -->
X1

<!-- b003058 | prose | pages [13] -->
China

<!-- b003059 | prose | pages [13] -->
Pr(𝛽> 0) Beta Std. Err.

<!-- b003060 | prose | pages [13] -->
95% CI

<!-- b003061 | prose | pages [13] -->
[0.01996, 0.04828] 0.03412 0.01234 0.99

<!-- b003062 | prose | pages [13] -->
X2

<!-- b003063 | prose | pages [13] -->
0.03245 0.01156 0.99 [0.01980, 0.05510]

<!-- b003064 | prose | pages [13] -->
[0.00079, 0.03411] 0.01745 0.00852 0.99

<!-- b003065 | prose | pages [13] -->
X3

<!-- b003066 | prose | pages [13] -->
0.01621 0.00825 0.98 [0.00014, 0.03228]

<!-- b003067 | prose | pages [13] -->
[0.04873, 0.07007] 0.06567 0.01245 0.99 0.06456 0.01231 0.99 [0.04045, 0.07867]

<!-- b003068 | prose | pages [13] -->
微信公众号：数学模型

<!-- b003069 | prose | pages [13] -->
[−0.00236, 0.02704] X4 0.01234 0.00759 0.93 0.02891 0.01055 0.98 [0.00833, 0.04949]

<!-- b003070 | prose | pages [13] -->
[−0.00007, 0.04697] X5 0.02345 0.01244 0.97 [−0.00589, 0.03723] 0.01567 0.01143 0.92

<!-- b003071 | prose | pages [13] -->
[−0.02194, 0.01726] −0.00234 X6 0.01038 0.32

<!-- b003072 | prose | pages [13] -->
X7

<!-- b003073 | prose | pages [13] -->
[−0.00628, 0.03096] 0.01239 0.00951 0.95

<!-- b003074 | prose | pages [13] -->
[−0.01058, 0.03254] [0.00771, 0.05475] 0.03123 0.00713 0.98 0.01098 0.01162 0.85

<!-- b003075 | prose | pages [13] -->
[−0.01065, 0.03639] X8 0.01287 0.01214 0.88

<!-- b003076 | prose | pages [13] -->
Variable United Kingdom

<!-- b003077 | prose | pages [13] -->
Pr(𝛽> 0) Beta Std. Err.

<!-- b003078 | prose | pages [13] -->
95% CI

<!-- b003079 | prose | pages [13] -->
X1

<!-- b003080 | prose | pages [13] -->
0.01765 0.00854 0.93 [0.00099, 0.03431]

<!-- b003081 | prose | pages [13] -->
France

<!-- b003082 | prose | pages [13] -->
Pr(𝛽> 0) Beta Std. Err.

<!-- b003083 | prose | pages [13] -->
95% CI

<!-- b003084 | prose | pages [13] -->
[0.01153, 0.05425] 0.03789 0.01345 0.99

<!-- b003085 | prose | pages [13] -->
X2

<!-- b003086 | prose | pages [13] -->
0.03983 0.01273 0.99 [0.01347, 0.05419]

<!-- b003087 | prose | pages [13] -->
[0.00097, 0.03037] 0.01567 0.00759 0.96 0.01532 0.00795 0.94 [0.00082, 0.03012]

<!-- b003088 | prose | pages [13] -->
微信号：MATHmodels

<!-- b003089 | prose | pages [13] -->
X3 [0.03811, 0.07501] 0.05345 0.01120 0.99 0.05576 0.01134 0.99 [0.03764, 0.06816]

<!-- b003090 | prose | pages [13] -->
[−0.00986, 0.02738] X4 0.00876 0.00958 0.88

<!-- b003091 | prose | pages [13] -->
X5

<!-- b003092 | prose | pages [13] -->
[−0.01022, 0.02846] 0.00912 0.00933 0.86

<!-- b003093 | prose | pages [13] -->
[0.00228, 0.05128] 0.02678 0.01250 0.98 0.02631 0.01232 0.97 [0.00312, 0.05076]

<!-- b003094 | prose | pages [13] -->
[−0.02181, 0.01935] −0.00123 X6 0.01053 0.44 −0.00096 [−0.02147, 0.01955] 0.01025 0.48

<!-- b003095 | prose | pages [13] -->
[−0.00883, 0.04017] X7 0.01567 0.01257 0.90 [−0.00984, 0.04158] 0.01687 0.01243 0.91

<!-- b003096 | prose | pages [13] -->
[−0.00105, 0.04795] X8 0.02345 0.01257 0.97 [−0.00123, 0.04603] 0.02257 0.01233 0.95

<!-- b003097 | prose | pages [13] -->
= 0.02678, 95% CI: [0.00228, 0.05128]; France: beta = 0.02631, 95% CI: [0.00312, 0.05076]), indicating that host nations with strong track records in these disciplines can further enhance their medal prospects by strategically prioritizing events that align with their historical strengths and local support systems. Moreover, China’s relatively higher coefficient for Emerging Events (X8, beta = 0.01765, 95% CI: [0.00099, 0.03431]) implies that even non-traditional or newer events can be exploited effectively when a host country’s infrastructure and preparatory advantages are aligned with the chosen sports. Overall, these findings suggest that by selecting events that not only reflect historical success but also amplify home advantages, host nations can significantly improve their medal tallies. 1

<!-- b003098 | prose | pages [13] -->
Task 2: Dive Into Great Coach Effect 6

<!-- b003099 | prose | pages [13] -->
In this section, we examine another factor that can influence medal counts—the coach. Unlike athletes, who are typically constrained by nationality, coaches possess a unique flexibility to work across borders. This mobility allows them to transfer their expertise and successful training methodologies from one country’s sports system to another. Such fluidity creates what we term the “great coach effect,” where the influence of a single coach can significantly enhance a country’s medal count in specific sports [2].

<!-- b003100 | prose | pages [13] -->
For example, the legendary careers of Lang Ping and Béla Károlyi exemplify this effect. Despite coaching in vastly different cultural and sporting environments, both successfully trans- formed national teams and led them to Olympic podium finishes.

<!-- b003101 | prose | pages [13] -->
Lang Ping’s experience coaching volleyball teams in both the United States and China demonstrates the potential for

<!-- b003102 | prose | pages [13] -->
1Due to space constraints, gold medal data is omitted here. The conclusions for gold medals are consistent with those for total medals.

<!-- b003103 | furniture | pages [14] -->
Team # 2513314

<!-- b003104 | furniture | pages [14] -->
Page 14 of 22

<!-- b003105 | prose | pages [14] -->
exceptional coaches to transcend national boundaries [4]. Similarly, Béla Károlyi’s transition from coaching in Romania to achieving remarkable success with the U.S. women’s gymnastics team further supports this notion [8].

<!-- b003106 | prose | pages [14] -->
Following standard analytical procedures, we first define what constitutes a "great coach" and seek to quantify their coaching impact. Next, we incorporate this variable into our BHDM model and analyze regression coefficients to assess whether and to what extent great coaches Finally, we will identify three countries, select great significantly influence medal counts. coaches for them, and estimate their impact based on the regression coefficients.

<!-- b003107 | prose | pages [14] -->
6.1 What is a Great Coach?

<!-- b003108 | prose | pages [14] -->
In our analysis, we define a "great coach" as one who has demonstrated the ability to elevate an Olympic team to achieve at least bronze medal finishes in two or more different countries. By searching the Wiki database, we identified a total of 1,103 such great coaches, among whom 697 are currently active. These coaches are engaged in multiple sports across various countries, including the United States, China, and Japan.

<!-- b003109 | prose | pages [14] -->
If we use the total number of renowned coaches as a new variable, a natural hypothesis emerges: do all renowned coaches contribute equally to a country’s medal count? We believe this assumption is overly restrictive. Our selection criteria represent only the minimum threshold for inclusion, but there is likely heterogeneity among coaches, meaning that their ability to lead teams to success varies.

<!-- b003110 | prose | pages [14] -->
For example, while Lang Ping, as a renowned coach, helped China secure one gold medal and the United States one silver medal, Béla Károlyi, another renowned coach, led his teams to at least 9 gold medals. This discrepancy highlights the differences in coaching effectiveness. Therefore, to ensure a fair reflection of each coach’s impact, a more fine-grained characterization of individual coaching abilities is necessary.

<!-- b003111 | prose | pages [14] -->
Based on the latest research on coaching effectiveness, we define the following metric to quantify the coaching ability of a "renowned coach": the coaching ability 𝐴is calculated as the number of gold medals won during their tenure multiplied by 6, plus the number of silver medals multiplied by 3, and the number of bronze medals multiplied by 1. Mathematically, this is expressed as:

<!-- b003112 | prose | pages [14] -->
𝐴= 6𝐺+ 3𝑆+ 1𝐵 (11)

<!-- b003113 | prose | pages [14] -->
where 𝐺represents the number of gold medals won under the coach’s leadership, 𝑆represents the number of silver medals won, and 𝐵represents the number of bronze medals won. This metric assigns the highest weight to gold medals, followed by silver and then bronze, ensuring a more precise assessment of a coach’s contribution to medal achievements.

<!-- b003114 | prose | pages [14] -->
For a country’s coaching ability variable 𝑋9, it is defined as the sum of the coaching abilities 𝐴of all renowned coaches within that country, mathematically expressed as:

<!-- b003115 | prose | pages [14] -->
𝑋9 =

<!-- b003116 | prose | pages [14] -->
𝑁 ∑︁

<!-- b003117 | prose | pages [14] -->
𝐴𝑖 (12)

<!-- b003118 | prose | pages [14] -->
𝑖=1

<!-- b003119 | prose | pages [14] -->
where 𝐴𝑖denotes the coaching ability of the 𝑖-th coach.

<!-- b003120 | prose | pages [14] -->
6.2 Great Coach Affect the Medals

<!-- b003121 | prose | pages [14] -->
We incorporate 𝑋9 into our BHDM model and obtain its regression coefficient. Since there are 46 countries with renowned coaches, we are unable to present the specific values for each due to space constraints. Table 5 displays some summary statistics of this indicator.

<!-- b003122 | prose | pages [14] -->
关注数学模型

<!-- b003123 | furniture | pages [14] -->
2

<!-- b003124 | furniture | pages [14] -->
MATHmodels

<!-- b003125 | furniture | pages [14] -->
获取更多资讯

<!-- b003126 | furniture | pages [15] -->
Team # 2513314

<!-- b003127 | furniture | pages [15] -->
Page 15 of 22

<!-- b003128 | caption | pages [15] -->
Table 5: Posterior summary statistics for the Great Coach variable 𝑿9 of 46 countries.

<!-- b003129 | prose | pages [15] -->
Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Std. Err. Mean Outcome Beta Mean

<!-- b003130 | prose | pages [15] -->
微信公众号：数学模型

<!-- b003131 | prose | pages [15] -->
All Medals 0.036134 0.011008 Gold Medals 0.028167 0.009134 0.997 46 0.983 45

<!-- b003132 | prose | pages [15] -->
As shown in Table 5, the posterior mean coefficients for the Great Coach variable 𝑿9 are approximately 0.036134 for all medals and 0.028167 for gold medals, respectively. Because these coefficients reflect log-rate effects, a one-unit increase in 𝑿9 corresponds to a multiplicative change of 𝑒0.036134 ≈1.037 (roughly a 3.7% rise) in the expected total medal count and 𝑒0.028167 ≈1.029 (about a 2.9% increase) in gold medals. Consequently, even modest gains

<!-- b003133 | prose | pages [15] -->
微信号：MATHmodels

<!-- b003134 | prose | pages [15] -->
in “great coach” capacity—such as recruiting or developing a coach with one additional point of aggregate coaching ability—can yield a tangible percentage uplift in a nation’s overall and top-tier (i.e., gold) Olympic performance.

<!-- b003135 | prose | pages [15] -->
Moreover, the high values of Avg. Pr(𝛽> 0) (0.997 for all medals and 0.983 for gold medals) and the fact that Pr(𝛽> 0) exceeds 0.95 for nearly every country underscore that the impact of the Great Coach variable is both statistically robust and broadly consistent across the sample of 46 nations. In other words, not only does the posterior mean of 𝛽𝑋9 suggest a positive relationship, but the overwhelming majority of countries in the dataset exhibit a high probability that increasing aggregate coaching ability leads to more medals. This finding provides strong evidence for the “great coach” effect, indicating that improvements in coaching capacity are systematically tied to enhanced Olympic performance rather than being confined to a select subset of countries.

<!-- b003136 | prose | pages [15] -->
Invest in Great Coach and Estimate its Impact 6.3

<!-- b003137 | prose | pages [15] -->
We believe that only wealthy countries have more options when it comes to investing in renowned coaches. Therefore, we selected the United States, China, and Japan—three of the world’s top-ranking countries by GDP—and carefully curated projects for each of them. The regression results are shown in Table 6.

<!-- b003138 | caption | pages [15] -->
Table 6: Parameter estimates for the Great Coach variable 𝑿9 of total medals in three countries.

<!-- b003139 | prose | pages [15] -->
Country Beta Std. Err.

<!-- b003140 | prose | pages [15] -->
United States 0.0367 0.0091 China 0.0445 0.0102 Japan 0.0283 0.0078

<!-- b003141 | prose | pages [15] -->
Pr(𝛽> 0) 95% Cred. Int.

<!-- b003142 | prose | pages [15] -->
0.98 [0.0082, 0.0450] 0.99 [0.0150, 0.0558] 0.96 [0.0031, 0.0382]

<!-- b003143 | prose | pages [15] -->
We recommend that the United States recruit at least one “great coach” for fencing and sport climbing. With a coefficient of 0.0367, a one-unit increase in coaching capacity corresponds to an estimated impact of 𝑒0.0367 −1 ≈3.74% increase in Olympic medal counts in these disciplines.

<!-- b003144 | prose | pages [15] -->
For China, the coefficient of 0.0445 implies that each additional point of 𝑿9 results in roughly 𝑒0.0445 −1 ≈4.55% enhancement in overall medal achievements, making it advisable to invest in top coaching talent for sports such as basketball and beach volleyball.

<!-- b003145 | prose | pages [15] -->
m

<!-- b003146 | prose | pages [15] -->
m

<!-- b003147 | prose | pages [15] -->
m

<!-- b003148 | prose | pages [15] -->
m

<!-- b003149 | prose | pages [15] -->
m

<!-- b003150 | prose | pages [15] -->
m

<!-- b003151 | prose | pages [15] -->
m

<!-- b003152 | prose | pages [15] -->
m

<!-- b003153 | prose | pages [15] -->
m

<!-- b003154 | prose | pages [15] -->
m

<!-- b003155 | prose | pages [15] -->
m

<!-- b003156 | prose | pages [15] -->
m

<!-- b003157 | prose | pages [15] -->
m

<!-- b003158 | prose | pages [15] -->
m

<!-- b003159 | prose | pages [15] -->
m

<!-- b003160 | prose | pages [15] -->
m

<!-- b003161 | prose | pages [15] -->
m

<!-- b003162 | prose | pages [15] -->
m

<!-- b003163 | prose | pages [15] -->
m

<!-- b003164 | prose | pages [15] -->
m

<!-- b003165 | prose | pages [15] -->
m

<!-- b003166 | prose | pages [15] -->
m

<!-- b003167 | prose | pages [15] -->
m

<!-- b003168 | prose | pages [15] -->
m

<!-- b003169 | prose | pages [15] -->
m

<!-- b003170 | prose | pages [15] -->
m

<!-- b003171 | prose | pages [15] -->
m

<!-- b003172 | prose | pages [15] -->
m

<!-- b003173 | prose | pages [15] -->
m

<!-- b003174 | prose | pages [15] -->
m

<!-- b003175 | prose | pages [15] -->
m

<!-- b003176 | prose | pages [15] -->
m

<!-- b003177 | prose | pages [15] -->
m

<!-- b003178 | prose | pages [15] -->
m

<!-- b003179 | prose | pages [15] -->
m

<!-- b003180 | prose | pages [15] -->
m

<!-- b003181 | prose | pages [15] -->
m

<!-- b003182 | prose | pages [15] -->
m

<!-- b003183 | prose | pages [15] -->
m

<!-- b003184 | prose | pages [15] -->
m

<!-- b003185 | prose | pages [15] -->
m

<!-- b003186 | prose | pages [15] -->
m

<!-- b003187 | prose | pages [15] -->
m

<!-- b003188 | prose | pages [15] -->
m

<!-- b003189 | prose | pages [15] -->
m

<!-- b003190 | prose | pages [15] -->
m

<!-- b003191 | prose | pages [15] -->
m

<!-- b003192 | prose | pages [15] -->
m

<!-- b003193 | prose | pages [15] -->
m

<!-- b003194 | prose | pages [15] -->
m

<!-- b003195 | prose | pages [15] -->
m

<!-- b003196 | prose | pages [15] -->
m

<!-- b003197 | prose | pages [15] -->
m

<!-- b003198 | prose | pages [15] -->
m

<!-- b003199 | prose | pages [15] -->
m

<!-- b003200 | prose | pages [15] -->
m

<!-- b003201 | prose | pages [15] -->
m

<!-- b003202 | prose | pages [15] -->
m

<!-- b003203 | prose | pages [15] -->
m

<!-- b003204 | prose | pages [15] -->
m

<!-- b003205 | prose | pages [15] -->
m

<!-- b003206 | prose | pages [15] -->
m

<!-- b003207 | prose | pages [15] -->
m

<!-- b003208 | prose | pages [15] -->
m

<!-- b003209 | prose | pages [15] -->
m

<!-- b003210 | prose | pages [15] -->
m

<!-- b003211 | prose | pages [15] -->
m

<!-- b003212 | prose | pages [15] -->
m

<!-- b003213 | prose | pages [15] -->
m

<!-- b003214 | prose | pages [15] -->
m

<!-- b003215 | prose | pages [15] -->
m

<!-- b003216 | prose | pages [15] -->
m

<!-- b003217 | prose | pages [15] -->
m

<!-- b003218 | prose | pages [15] -->
m

<!-- b003219 | prose | pages [15] -->
m

<!-- b003220 | prose | pages [15] -->
m

<!-- b003221 | prose | pages [15] -->
m

<!-- b003222 | prose | pages [15] -->
m

<!-- b003223 | prose | pages [15] -->
m

<!-- b003224 | prose | pages [15] -->
m

<!-- b003225 | prose | pages [15] -->
m

<!-- b003226 | prose | pages [15] -->
m

<!-- b003227 | prose | pages [15] -->
m

<!-- b003228 | prose | pages [15] -->
m

<!-- b003229 | prose | pages [15] -->
m

<!-- b003230 | prose | pages [15] -->
m

<!-- b003231 | prose | pages [15] -->
m

<!-- b003232 | prose | pages [15] -->
m

<!-- b003233 | prose | pages [15] -->
m

<!-- b003234 | prose | pages [15] -->
m

<!-- b003235 | prose | pages [15] -->
m

<!-- b003236 | prose | pages [15] -->
m

<!-- b003237 | prose | pages [15] -->
m

<!-- b003238 | prose | pages [15] -->
m

<!-- b003239 | prose | pages [15] -->
m

<!-- b003240 | prose | pages [15] -->
Finally, Japan exhibits a coefficient of 0.0283, translating to an expected improvement of

<!-- b003241 | prose | pages [15] -->
m

<!-- b003242 | prose | pages [15] -->
m

<!-- b003243 | prose | pages [15] -->
m

<!-- b003244 | prose | pages [15] -->
m

<!-- b003245 | prose | pages [15] -->
m

<!-- b003246 | prose | pages [15] -->
m

<!-- b003247 | prose | pages [15] -->
m

<!-- b003248 | prose | pages [15] -->
m

<!-- b003249 | prose | pages [15] -->
m

<!-- b003250 | prose | pages [15] -->
m

<!-- b003251 | prose | pages [15] -->
m

<!-- b003252 | prose | pages [15] -->
m

<!-- b003253 | prose | pages [15] -->
m

<!-- b003254 | prose | pages [15] -->
m

<!-- b003255 | prose | pages [15] -->
m

<!-- b003256 | prose | pages [15] -->
m

<!-- b003257 | prose | pages [15] -->
m

<!-- b003258 | prose | pages [15] -->
m

<!-- b003259 | prose | pages [15] -->
m

<!-- b003260 | prose | pages [15] -->
m

<!-- b003261 | prose | pages [15] -->
m

<!-- b003262 | prose | pages [15] -->
m

<!-- b003263 | prose | pages [15] -->
m

<!-- b003264 | prose | pages [15] -->
m

<!-- b003265 | prose | pages [15] -->
m

<!-- b003266 | prose | pages [15] -->
m

<!-- b003267 | prose | pages [15] -->
m

<!-- b003268 | prose | pages [15] -->
m

<!-- b003269 | prose | pages [15] -->
m

<!-- b003270 | prose | pages [15] -->
m

<!-- b003271 | prose | pages [15] -->
m

<!-- b003272 | prose | pages [15] -->
m

<!-- b003273 | prose | pages [15] -->
m

<!-- b003274 | prose | pages [15] -->
m

<!-- b003275 | prose | pages [15] -->
m

<!-- b003276 | prose | pages [15] -->
m

<!-- b003277 | prose | pages [15] -->
m

<!-- b003278 | prose | pages [15] -->
m

<!-- b003279 | prose | pages [15] -->
m

<!-- b003280 | prose | pages [15] -->
m

<!-- b003281 | prose | pages [15] -->
m

<!-- b003282 | prose | pages [15] -->
m

<!-- b003283 | prose | pages [15] -->
m

<!-- b003284 | prose | pages [15] -->
m

<!-- b003285 | prose | pages [15] -->
m

<!-- b003286 | prose | pages [15] -->
m

<!-- b003287 | prose | pages [15] -->
m

<!-- b003288 | prose | pages [15] -->
m

<!-- b003289 | prose | pages [15] -->
m

<!-- b003290 | prose | pages [15] -->
m

<!-- b003291 | prose | pages [15] -->
m

<!-- b003292 | prose | pages [15] -->
m

<!-- b003293 | prose | pages [15] -->
m

<!-- b003294 | prose | pages [15] -->
m

<!-- b003295 | prose | pages [15] -->
m

<!-- b003296 | prose | pages [15] -->
m

<!-- b003297 | prose | pages [15] -->
m

<!-- b003298 | prose | pages [15] -->
m

<!-- b003299 | prose | pages [15] -->
m

<!-- b003300 | prose | pages [15] -->
m

<!-- b003301 | prose | pages [15] -->
m

<!-- b003302 | prose | pages [15] -->
m

<!-- b003303 | prose | pages [15] -->
m

<!-- b003304 | prose | pages [15] -->
m

<!-- b003305 | prose | pages [15] -->
m

<!-- b003306 | prose | pages [15] -->
m

<!-- b003307 | prose | pages [15] -->
m

<!-- b003308 | prose | pages [15] -->
m

<!-- b003309 | prose | pages [15] -->
m

<!-- b003310 | prose | pages [15] -->
m

<!-- b003311 | prose | pages [15] -->
m

<!-- b003312 | prose | pages [15] -->
m

<!-- b003313 | prose | pages [15] -->
m

<!-- b003314 | prose | pages [15] -->
m

<!-- b003315 | prose | pages [15] -->
m

<!-- b003316 | prose | pages [15] -->
m

<!-- b003317 | prose | pages [15] -->
m

<!-- b003318 | prose | pages [15] -->
m

<!-- b003319 | prose | pages [15] -->
m

<!-- b003320 | prose | pages [15] -->
m

<!-- b003321 | prose | pages [15] -->
m

<!-- b003322 | prose | pages [15] -->
m

<!-- b003323 | prose | pages [15] -->
m

<!-- b003324 | prose | pages [15] -->
m

<!-- b003325 | prose | pages [15] -->
m

<!-- b003326 | prose | pages [15] -->
m

<!-- b003327 | prose | pages [15] -->
m

<!-- b003328 | prose | pages [15] -->
m

<!-- b003329 | prose | pages [15] -->
m

<!-- b003330 | prose | pages [15] -->
m

<!-- b003331 | prose | pages [15] -->
m

<!-- b003332 | prose | pages [15] -->
m

<!-- b003333 | prose | pages [15] -->
m

<!-- b003334 | prose | pages [15] -->
m

<!-- b003335 | prose | pages [15] -->
m

<!-- b003336 | prose | pages [15] -->
m

<!-- b003337 | prose | pages [15] -->
m

<!-- b003338 | prose | pages [15] -->
m

<!-- b003339 | prose | pages [15] -->
m

<!-- b003340 | prose | pages [15] -->
m

<!-- b003341 | prose | pages [15] -->
m

<!-- b003342 | prose | pages [15] -->
m

<!-- b003343 | prose | pages [15] -->
m

<!-- b003344 | prose | pages [15] -->
m

<!-- b003345 | prose | pages [15] -->
m

<!-- b003346 | prose | pages [15] -->
m

<!-- b003347 | prose | pages [15] -->
m

<!-- b003348 | prose | pages [15] -->
m

<!-- b003349 | prose | pages [15] -->
m

<!-- b003350 | prose | pages [15] -->
m

<!-- b003351 | prose | pages [15] -->
m

<!-- b003352 | prose | pages [15] -->
m

<!-- b003353 | prose | pages [15] -->
m

<!-- b003354 | prose | pages [15] -->
m

<!-- b003355 | prose | pages [15] -->
𝑒0.0283 −1 ≈2.87%; thus, Japan should consider investing in a “great coach” for gymnastics

<!-- b003356 | prose | pages [15] -->
m

<!-- b003357 | prose | pages [15] -->
m

<!-- b003358 | prose | pages [15] -->
m

<!-- b003359 | prose | pages [15] -->
m

<!-- b003360 | prose | pages [15] -->
m

<!-- b003361 | prose | pages [15] -->
m

<!-- b003362 | prose | pages [15] -->
m

<!-- b003363 | prose | pages [15] -->
m

<!-- b003364 | prose | pages [15] -->
m

<!-- b003365 | prose | pages [15] -->
m

<!-- b003366 | prose | pages [15] -->
m

<!-- b003367 | prose | pages [15] -->
m

<!-- b003368 | prose | pages [15] -->
m

<!-- b003369 | prose | pages [15] -->
m

<!-- b003370 | prose | pages [15] -->
m

<!-- b003371 | prose | pages [15] -->
m

<!-- b003372 | prose | pages [15] -->
m

<!-- b003373 | prose | pages [15] -->
m

<!-- b003374 | prose | pages [15] -->
m

<!-- b003375 | prose | pages [15] -->
m

<!-- b003376 | prose | pages [15] -->
m

<!-- b003377 | prose | pages [15] -->
m

<!-- b003378 | prose | pages [15] -->
m

<!-- b003379 | prose | pages [15] -->
m

<!-- b003380 | prose | pages [15] -->
m

<!-- b003381 | prose | pages [15] -->
m

<!-- b003382 | prose | pages [15] -->
m

<!-- b003383 | prose | pages [15] -->
m

<!-- b003384 | prose | pages [15] -->
m

<!-- b003385 | prose | pages [15] -->
m

<!-- b003386 | prose | pages [15] -->
m

<!-- b003387 | prose | pages [15] -->
m

<!-- b003388 | prose | pages [15] -->
m

<!-- b003389 | prose | pages [15] -->
m

<!-- b003390 | prose | pages [15] -->
m

<!-- b003391 | prose | pages [15] -->
m

<!-- b003392 | prose | pages [15] -->
m

<!-- b003393 | prose | pages [15] -->
m

<!-- b003394 | prose | pages [15] -->
m

<!-- b003395 | prose | pages [15] -->
m

<!-- b003396 | prose | pages [15] -->
m

<!-- b003397 | prose | pages [15] -->
m

<!-- b003398 | prose | pages [15] -->
m

<!-- b003399 | prose | pages [15] -->
m

<!-- b003400 | prose | pages [15] -->
m

<!-- b003401 | prose | pages [15] -->
m

<!-- b003402 | prose | pages [15] -->
m

<!-- b003403 | prose | pages [15] -->
m

<!-- b003404 | prose | pages [15] -->
m

<!-- b003405 | prose | pages [15] -->
m

<!-- b003406 | prose | pages [15] -->
m

<!-- b003407 | prose | pages [15] -->
m

<!-- b003408 | prose | pages [15] -->
m

<!-- b003409 | prose | pages [15] -->
m

<!-- b003410 | prose | pages [15] -->
m

<!-- b003411 | prose | pages [15] -->
m

<!-- b003412 | prose | pages [15] -->
m

<!-- b003413 | prose | pages [15] -->
m

<!-- b003414 | prose | pages [15] -->
m

<!-- b003415 | prose | pages [15] -->
m

<!-- b003416 | prose | pages [15] -->
m

<!-- b003417 | prose | pages [15] -->
m

<!-- b003418 | prose | pages [15] -->
m

<!-- b003419 | prose | pages [15] -->
m

<!-- b003420 | prose | pages [15] -->
m

<!-- b003421 | prose | pages [15] -->
m

<!-- b003422 | prose | pages [15] -->
m

<!-- b003423 | prose | pages [15] -->
m

<!-- b003424 | prose | pages [15] -->
m

<!-- b003425 | prose | pages [15] -->
m

<!-- b003426 | prose | pages [15] -->
m

<!-- b003427 | prose | pages [15] -->
m

<!-- b003428 | prose | pages [15] -->
m

<!-- b003429 | prose | pages [15] -->
m

<!-- b003430 | prose | pages [15] -->
m

<!-- b003431 | furniture | pages [15] -->
m

<!-- b003432 | furniture | pages [15] -->
m

<!-- b003433 | furniture | pages [15] -->
m

<!-- b003434 | furniture | pages [15] -->
m

<!-- b003435 | furniture | pages [15] -->
m

<!-- b003436 | furniture | pages [15] -->
m

<!-- b003437 | furniture | pages [15] -->
m

<!-- b003438 | furniture | pages [15] -->
m

<!-- b003439 | furniture | pages [15] -->
m

<!-- b003440 | furniture | pages [15] -->
m

<!-- b003441 | furniture | pages [15] -->
m

<!-- b003442 | furniture | pages [15] -->
m

<!-- b003443 | furniture | pages [15] -->
m

<!-- b003444 | furniture | pages [15] -->
m

<!-- b003445 | furniture | pages [15] -->
m

<!-- b003446 | furniture | pages [15] -->
m

<!-- b003447 | furniture | pages [15] -->
m

<!-- b003448 | furniture | pages [15] -->
m

<!-- b003449 | furniture | pages [15] -->
m

<!-- b003450 | furniture | pages [15] -->
m

<!-- b003451 | furniture | pages [15] -->
m

<!-- b003452 | furniture | pages [15] -->
m

<!-- b003453 | furniture | pages [15] -->
m

<!-- b003454 | furniture | pages [15] -->
m

<!-- b003455 | furniture | pages [15] -->
m

<!-- b003456 | furniture | pages [15] -->
m

<!-- b003457 | furniture | pages [15] -->
m

<!-- b003458 | furniture | pages [15] -->
m

<!-- b003459 | furniture | pages [15] -->
m

<!-- b003460 | furniture | pages [15] -->
m

<!-- b003461 | furniture | pages [15] -->
m

<!-- b003462 | furniture | pages [15] -->
m

<!-- b003463 | furniture | pages [15] -->
m

<!-- b003464 | furniture | pages [15] -->
m

<!-- b003465 | furniture | pages [15] -->
m

<!-- b003466 | furniture | pages [15] -->
m

<!-- b003467 | furniture | pages [15] -->
m

<!-- b003468 | furniture | pages [15] -->
m

<!-- b003469 | furniture | pages [15] -->
m

<!-- b003470 | furniture | pages [15] -->
m

<!-- b003471 | furniture | pages [15] -->
m

<!-- b003472 | furniture | pages [15] -->
m

<!-- b003473 | furniture | pages [15] -->
m

<!-- b003474 | furniture | pages [15] -->
m

<!-- b003475 | furniture | pages [15] -->
m

<!-- b003476 | furniture | pages [15] -->
m

<!-- b003477 | furniture | pages [15] -->
m

<!-- b003478 | furniture | pages [15] -->
m

<!-- b003479 | furniture | pages [15] -->
m

<!-- b003480 | furniture | pages [15] -->
m

<!-- b003481 | furniture | pages [15] -->
m

<!-- b003482 | furniture | pages [15] -->
m

<!-- b003483 | furniture | pages [15] -->
m

<!-- b003484 | furniture | pages [15] -->
m

<!-- b003485 | furniture | pages [15] -->
m

<!-- b003486 | furniture | pages [15] -->
m

<!-- b003487 | furniture | pages [15] -->
m

<!-- b003488 | furniture | pages [15] -->
m

<!-- b003489 | furniture | pages [15] -->
m

<!-- b003490 | furniture | pages [15] -->
m

<!-- b003491 | furniture | pages [15] -->
m

<!-- b003492 | furniture | pages [15] -->
m

<!-- b003493 | furniture | pages [15] -->
m

<!-- b003494 | furniture | pages [15] -->
m

<!-- b003495 | furniture | pages [15] -->
m

<!-- b003496 | furniture | pages [15] -->
m

<!-- b003497 | furniture | pages [15] -->
m

<!-- b003498 | furniture | pages [15] -->
m

<!-- b003499 | furniture | pages [15] -->
m

<!-- b003500 | furniture | pages [15] -->
m

<!-- b003501 | furniture | pages [15] -->
m

<!-- b003502 | furniture | pages [15] -->
m

<!-- b003503 | furniture | pages [15] -->
m

<!-- b003504 | furniture | pages [15] -->
m

<!-- b003505 | furniture | pages [15] -->
m

<!-- b003506 | furniture | pages [15] -->
m

<!-- b003507 | furniture | pages [15] -->
m

<!-- b003508 | furniture | pages [15] -->
m

<!-- b003509 | furniture | pages [15] -->
m

<!-- b003510 | furniture | pages [15] -->
m

<!-- b003511 | furniture | pages [15] -->
m

<!-- b003512 | furniture | pages [15] -->
m

<!-- b003513 | furniture | pages [15] -->
m

<!-- b003514 | furniture | pages [15] -->
m

<!-- b003515 | furniture | pages [15] -->
m

<!-- b003516 | furniture | pages [15] -->
m

<!-- b003517 | furniture | pages [15] -->
m

<!-- b003518 | furniture | pages [15] -->
m

<!-- b003519 | furniture | pages [15] -->
m

<!-- b003520 | furniture | pages [15] -->
m

<!-- b003521 | furniture | pages [15] -->
m

<!-- b003522 | furniture | pages [15] -->
m

<!-- b003523 | furniture | pages [15] -->
m

<!-- b003524 | furniture | pages [15] -->
m

<!-- b003525 | furniture | pages [15] -->
m

<!-- b003526 | furniture | pages [15] -->
m

<!-- b003527 | furniture | pages [15] -->
m

<!-- b003528 | furniture | pages [15] -->
m

<!-- b003529 | furniture | pages [15] -->
m

<!-- b003530 | furniture | pages [15] -->
m

<!-- b003531 | furniture | pages [15] -->
m

<!-- b003532 | furniture | pages [15] -->
m

<!-- b003533 | furniture | pages [15] -->
m

<!-- b003534 | furniture | pages [15] -->
m

<!-- b003535 | furniture | pages [15] -->
m

<!-- b003536 | furniture | pages [15] -->
m

<!-- b003537 | furniture | pages [15] -->
m

<!-- b003538 | furniture | pages [15] -->
m

<!-- b003539 | furniture | pages [15] -->
m

<!-- b003540 | furniture | pages [15] -->
m

<!-- b003541 | furniture | pages [15] -->
m

<!-- b003542 | furniture | pages [15] -->
m

<!-- b003543 | furniture | pages [15] -->
m

<!-- b003544 | furniture | pages [15] -->
m

<!-- b003545 | furniture | pages [15] -->
m

<!-- b003546 | furniture | pages [15] -->
m

<!-- b003547 | furniture | pages [15] -->
m

<!-- b003548 | furniture | pages [15] -->
m

<!-- b003549 | furniture | pages [15] -->
m

<!-- b003550 | furniture | pages [15] -->
m

<!-- b003551 | furniture | pages [15] -->
m

<!-- b003552 | furniture | pages [15] -->
m

<!-- b003553 | furniture | pages [15] -->
m

<!-- b003554 | furniture | pages [15] -->
m

<!-- b003555 | furniture | pages [15] -->
m

<!-- b003556 | furniture | pages [15] -->
m

<!-- b003557 | furniture | pages [15] -->
m

<!-- b003558 | furniture | pages [15] -->
m

<!-- b003559 | furniture | pages [15] -->
m

<!-- b003560 | furniture | pages [15] -->
m

<!-- b003561 | furniture | pages [15] -->
m

<!-- b003562 | furniture | pages [15] -->
m

<!-- b003563 | furniture | pages [15] -->
m

<!-- b003564 | furniture | pages [15] -->
m

<!-- b003565 | furniture | pages [15] -->
m

<!-- b003566 | furniture | pages [15] -->
m

<!-- b003567 | furniture | pages [15] -->
m

<!-- b003568 | furniture | pages [15] -->
m

<!-- b003569 | furniture | pages [15] -->
m

<!-- b003570 | furniture | pages [15] -->
m

<!-- b003571 | furniture | pages [15] -->
m

<!-- b003572 | furniture | pages [15] -->
m

<!-- b003573 | furniture | pages [15] -->
m

<!-- b003574 | furniture | pages [15] -->
m

<!-- b003575 | furniture | pages [15] -->
m

<!-- b003576 | furniture | pages [15] -->
m

<!-- b003577 | furniture | pages [15] -->
m

<!-- b003578 | furniture | pages [15] -->
m

<!-- b003579 | furniture | pages [15] -->
m

<!-- b003580 | furniture | pages [15] -->
m

<!-- b003581 | furniture | pages [15] -->
m

<!-- b003582 | furniture | pages [15] -->
m

<!-- b003583 | furniture | pages [15] -->
m

<!-- b003584 | furniture | pages [15] -->
m

<!-- b003585 | furniture | pages [15] -->
m

<!-- b003586 | furniture | pages [15] -->
m

<!-- b003587 | furniture | pages [15] -->
m

<!-- b003588 | furniture | pages [15] -->
m

<!-- b003589 | furniture | pages [15] -->
m

<!-- b003590 | furniture | pages [15] -->
m

<!-- b003591 | furniture | pages [15] -->
m

<!-- b003592 | furniture | pages [15] -->
m

<!-- b003593 | furniture | pages [15] -->
m

<!-- b003594 | furniture | pages [15] -->
m

<!-- b003595 | furniture | pages [15] -->
m

<!-- b003596 | furniture | pages [15] -->
m

<!-- b003597 | furniture | pages [15] -->
m

<!-- b003598 | furniture | pages [15] -->
m

<!-- b003599 | furniture | pages [15] -->
m

<!-- b003600 | furniture | pages [15] -->
m

<!-- b003601 | furniture | pages [15] -->
m

<!-- b003602 | furniture | pages [15] -->
m

<!-- b003603 | furniture | pages [15] -->
m

<!-- b003604 | furniture | pages [15] -->
m

<!-- b003605 | furniture | pages [15] -->
m

<!-- b003606 | furniture | pages [15] -->
m

<!-- b003607 | furniture | pages [15] -->
m

<!-- b003608 | furniture | pages [15] -->
m

<!-- b003609 | furniture | pages [15] -->
m

<!-- b003610 | furniture | pages [15] -->
m

<!-- b003611 | furniture | pages [15] -->
m

<!-- b003612 | furniture | pages [15] -->
m

<!-- b003613 | furniture | pages [15] -->
m

<!-- b003614 | furniture | pages [15] -->
m

<!-- b003615 | furniture | pages [15] -->
m

<!-- b003616 | furniture | pages [15] -->
m

<!-- b003617 | furniture | pages [15] -->
m

<!-- b003618 | furniture | pages [15] -->
m

<!-- b003619 | furniture | pages [15] -->
m

<!-- b003620 | furniture | pages [15] -->
m

<!-- b003621 | furniture | pages [15] -->
m

<!-- b003622 | furniture | pages [15] -->
m

<!-- b003623 | furniture | pages [15] -->
m

<!-- b003624 | furniture | pages [15] -->
m

<!-- b003625 | furniture | pages [15] -->
m

<!-- b003626 | furniture | pages [15] -->
m

<!-- b003627 | furniture | pages [15] -->
m

<!-- b003628 | furniture | pages [15] -->
m

<!-- b003629 | furniture | pages [15] -->
m

<!-- b003630 | furniture | pages [15] -->
m

<!-- b003631 | furniture | pages [15] -->
m

<!-- b003632 | furniture | pages [15] -->
m

<!-- b003633 | furniture | pages [15] -->
m

<!-- b003634 | furniture | pages [15] -->
m

<!-- b003635 | furniture | pages [15] -->
m

<!-- b003636 | furniture | pages [15] -->
m

<!-- b003637 | furniture | pages [15] -->
m

<!-- b003638 | furniture | pages [15] -->
m

<!-- b003639 | furniture | pages [15] -->
m

<!-- b003640 | furniture | pages [15] -->
m

<!-- b003641 | furniture | pages [15] -->
m

<!-- b003642 | furniture | pages [15] -->
m

<!-- b003643 | furniture | pages [15] -->
m

<!-- b003644 | furniture | pages [15] -->
m

<!-- b003645 | furniture | pages [15] -->
m

<!-- b003646 | furniture | pages [15] -->
m

<!-- b003647 | furniture | pages [15] -->
m

<!-- b003648 | furniture | pages [15] -->
m

<!-- b003649 | furniture | pages [15] -->
m

<!-- b003650 | furniture | pages [15] -->
m

<!-- b003651 | furniture | pages [15] -->
m

<!-- b003652 | furniture | pages [15] -->
m

<!-- b003653 | furniture | pages [15] -->
m

<!-- b003654 | furniture | pages [15] -->
m

<!-- b003655 | furniture | pages [15] -->
m

<!-- b003656 | furniture | pages [15] -->
m

<!-- b003657 | furniture | pages [15] -->
m

<!-- b003658 | furniture | pages [15] -->
m

<!-- b003659 | furniture | pages [15] -->
m

<!-- b003660 | furniture | pages [15] -->
m

<!-- b003661 | furniture | pages [15] -->
m

<!-- b003662 | furniture | pages [15] -->
m

<!-- b003663 | furniture | pages [15] -->
m

<!-- b003664 | furniture | pages [15] -->
m

<!-- b003665 | furniture | pages [15] -->
m

<!-- b003666 | furniture | pages [15] -->
m

<!-- b003667 | furniture | pages [15] -->
m

<!-- b003668 | furniture | pages [15] -->
m

<!-- b003669 | furniture | pages [15] -->
m

<!-- b003670 | furniture | pages [15] -->
m

<!-- b003671 | furniture | pages [15] -->
m

<!-- b003672 | furniture | pages [15] -->
m

<!-- b003673 | furniture | pages [15] -->
m

<!-- b003674 | furniture | pages [15] -->
m

<!-- b003675 | furniture | pages [15] -->
m

<!-- b003676 | furniture | pages [15] -->
m

<!-- b003677 | furniture | pages [15] -->
m

<!-- b003678 | furniture | pages [15] -->
m

<!-- b003679 | furniture | pages [15] -->
m

<!-- b003680 | furniture | pages [15] -->
m

<!-- b003681 | furniture | pages [15] -->
m

<!-- b003682 | furniture | pages [15] -->
m

<!-- b003683 | furniture | pages [15] -->
m

<!-- b003684 | furniture | pages [15] -->
m

<!-- b003685 | furniture | pages [15] -->
m

<!-- b003686 | furniture | pages [15] -->
m

<!-- b003687 | furniture | pages [15] -->
m

<!-- b003688 | furniture | pages [15] -->
m

<!-- b003689 | furniture | pages [15] -->
m

<!-- b003690 | furniture | pages [15] -->
m

<!-- b003691 | furniture | pages [15] -->
m

<!-- b003692 | furniture | pages [15] -->
m

<!-- b003693 | furniture | pages [15] -->
m

<!-- b003694 | furniture | pages [15] -->
m

<!-- b003695 | furniture | pages [15] -->
m

<!-- b003696 | furniture | pages [15] -->
m

<!-- b003697 | furniture | pages [15] -->
m

<!-- b003698 | furniture | pages [15] -->
m

<!-- b003699 | furniture | pages [15] -->
m

<!-- b003700 | furniture | pages [15] -->
m

<!-- b003701 | furniture | pages [15] -->
m

<!-- b003702 | furniture | pages [15] -->
m

<!-- b003703 | furniture | pages [15] -->
m

<!-- b003704 | furniture | pages [15] -->
m

<!-- b003705 | furniture | pages [15] -->
m

<!-- b003706 | furniture | pages [15] -->
m

<!-- b003707 | furniture | pages [15] -->
m

<!-- b003708 | furniture | pages [15] -->
m

<!-- b003709 | furniture | pages [15] -->
m

<!-- b003710 | furniture | pages [15] -->
m

<!-- b003711 | furniture | pages [15] -->
m

<!-- b003712 | furniture | pages [15] -->
m

<!-- b003713 | furniture | pages [15] -->
m

<!-- b003714 | furniture | pages [15] -->
m

<!-- b003715 | furniture | pages [15] -->
m

<!-- b003716 | furniture | pages [15] -->
m

<!-- b003717 | furniture | pages [15] -->
m

<!-- b003718 | furniture | pages [15] -->
m

<!-- b003719 | furniture | pages [15] -->
m

<!-- b003720 | furniture | pages [15] -->
m

<!-- b003721 | furniture | pages [15] -->
m

<!-- b003722 | furniture | pages [15] -->
m

<!-- b003723 | furniture | pages [15] -->
m

<!-- b003724 | furniture | pages [15] -->
m

<!-- b003725 | furniture | pages [15] -->
m

<!-- b003726 | furniture | pages [15] -->
m

<!-- b003727 | furniture | pages [15] -->
m

<!-- b003728 | furniture | pages [15] -->
m

<!-- b003729 | furniture | pages [15] -->
m

<!-- b003730 | furniture | pages [15] -->
m

<!-- b003731 | furniture | pages [15] -->
m

<!-- b003732 | furniture | pages [15] -->
m

<!-- b003733 | furniture | pages [15] -->
m

<!-- b003734 | furniture | pages [15] -->
m

<!-- b003735 | furniture | pages [15] -->
m

<!-- b003736 | furniture | pages [15] -->
m

<!-- b003737 | furniture | pages [15] -->
m

<!-- b003738 | furniture | pages [15] -->
m

<!-- b003739 | furniture | pages [15] -->
m

<!-- b003740 | furniture | pages [15] -->
m

<!-- b003741 | furniture | pages [15] -->
m

<!-- b003742 | furniture | pages [15] -->
m

<!-- b003743 | furniture | pages [15] -->
m

<!-- b003744 | furniture | pages [15] -->
m

<!-- b003745 | furniture | pages [15] -->
m

<!-- b003746 | furniture | pages [15] -->
m

<!-- b003747 | furniture | pages [15] -->
m

<!-- b003748 | furniture | pages [15] -->
m

<!-- b003749 | furniture | pages [15] -->
m

<!-- b003750 | furniture | pages [15] -->
m

<!-- b003751 | furniture | pages [15] -->
m

<!-- b003752 | furniture | pages [15] -->
m

<!-- b003753 | furniture | pages [15] -->
m

<!-- b003754 | furniture | pages [15] -->
m

<!-- b003755 | furniture | pages [15] -->
m

<!-- b003756 | furniture | pages [15] -->
m

<!-- b003757 | furniture | pages [15] -->
m

<!-- b003758 | furniture | pages [15] -->
m

<!-- b003759 | furniture | pages [15] -->
m

<!-- b003760 | furniture | pages [15] -->
m

<!-- b003761 | furniture | pages [15] -->
m

<!-- b003762 | furniture | pages [15] -->
m

<!-- b003763 | furniture | pages [15] -->
m

<!-- b003764 | furniture | pages [15] -->
m

<!-- b003765 | furniture | pages [15] -->
m

<!-- b003766 | furniture | pages [15] -->
m

<!-- b003767 | furniture | pages [15] -->
m

<!-- b003768 | furniture | pages [15] -->
m

<!-- b003769 | furniture | pages [15] -->
m

<!-- b003770 | furniture | pages [15] -->
m

<!-- b003771 | furniture | pages [15] -->
m

<!-- b003772 | furniture | pages [15] -->
m

<!-- b003773 | furniture | pages [15] -->
m

<!-- b003774 | furniture | pages [15] -->
m

<!-- b003775 | furniture | pages [15] -->
m

<!-- b003776 | furniture | pages [15] -->
m

<!-- b003777 | furniture | pages [15] -->
m

<!-- b003778 | furniture | pages [15] -->
m

<!-- b003779 | furniture | pages [15] -->
m

<!-- b003780 | furniture | pages [15] -->
m

<!-- b003781 | furniture | pages [15] -->
m

<!-- b003782 | furniture | pages [15] -->
m

<!-- b003783 | furniture | pages [15] -->
m

<!-- b003784 | furniture | pages [15] -->
m

<!-- b003785 | furniture | pages [15] -->
m

<!-- b003786 | furniture | pages [15] -->
m

<!-- b003787 | furniture | pages [15] -->
m

<!-- b003788 | furniture | pages [15] -->
m

<!-- b003789 | furniture | pages [15] -->
m

<!-- b003790 | furniture | pages [15] -->
m

<!-- b003791 | furniture | pages [15] -->
m

<!-- b003792 | furniture | pages [15] -->
m

<!-- b003793 | furniture | pages [15] -->
m

<!-- b003794 | furniture | pages [15] -->
m

<!-- b003795 | furniture | pages [15] -->
m

<!-- b003796 | furniture | pages [15] -->
m

<!-- b003797 | furniture | pages [15] -->
m

<!-- b003798 | furniture | pages [15] -->
m

<!-- b003799 | furniture | pages [15] -->
m

<!-- b003800 | furniture | pages [15] -->
m

<!-- b003801 | furniture | pages [15] -->
m

<!-- b003802 | furniture | pages [15] -->
m

<!-- b003803 | furniture | pages [15] -->
m

<!-- b003804 | furniture | pages [15] -->
m

<!-- b003805 | furniture | pages [15] -->
m

<!-- b003806 | furniture | pages [15] -->
m

<!-- b003807 | furniture | pages [15] -->
m

<!-- b003808 | furniture | pages [15] -->
m

<!-- b003809 | furniture | pages [15] -->
m

<!-- b003810 | furniture | pages [15] -->
m

<!-- b003811 | furniture | pages [15] -->
m

<!-- b003812 | furniture | pages [15] -->
m

<!-- b003813 | furniture | pages [15] -->
m

<!-- b003814 | furniture | pages [15] -->
m

<!-- b003815 | furniture | pages [15] -->
m

<!-- b003816 | furniture | pages [15] -->
m

<!-- b003817 | furniture | pages [15] -->
m

<!-- b003818 | furniture | pages [15] -->
m

<!-- b003819 | furniture | pages [15] -->
m

<!-- b003820 | furniture | pages [15] -->
m

<!-- b003821 | furniture | pages [15] -->
m

<!-- b003822 | furniture | pages [15] -->
m

<!-- b003823 | furniture | pages [15] -->
m

<!-- b003824 | furniture | pages [15] -->
m

<!-- b003825 | furniture | pages [15] -->
m

<!-- b003826 | furniture | pages [15] -->
m

<!-- b003827 | furniture | pages [15] -->
m

<!-- b003828 | furniture | pages [15] -->
m

<!-- b003829 | furniture | pages [15] -->
m

<!-- b003830 | furniture | pages [15] -->
m

<!-- b003831 | furniture | pages [15] -->
m

<!-- b003832 | furniture | pages [15] -->
m

<!-- b003833 | furniture | pages [15] -->
m

<!-- b003834 | furniture | pages [18] -->
Team # 2513314

<!-- b003835 | furniture | pages [18] -->
Page 18 of 22

<!-- b003836 | caption | pages [18] -->
Figure 6: Predicted Medal Allocations for LA 2028 in different Medal Distributions. We predicted

<!-- b003837 | prose | pages [18] -->
the number of medals and gold medals in 2028 under different medal distributions and provided the 95% prediction intervals.

<!-- b003838 | prose | pages [18] -->
achieves an MSE of 6.98 and an 𝑅2 of 0.85 for predicting the total number of medals, and an MSE of 3.42 with an 𝑅2 of 0.80 for gold medals (see Table 2). These improvements underscore its capacity to capture the underlying data structure more effectively than competing approaches.

<!-- b003839 | heading | pages [18] -->
• Discrete and Constrained Outcomes: By modeling medal allocations via a Dirichlet–

<!-- b003840 | prose | pages [18] -->
Multinomial likelihood, the BHDM ensures integer-valued outcomes that sum to a known total 𝑇.

<!-- b003841 | prose | pages [18] -->
This feature is crucial in predicting realistic medal counts, especially when evaluating discrete events like whether a country will “break the ice” and win its first medal. The model’s ability to provide exact integer predictions (e.g., forecasting 146 total medals for the United States and 82 for China) is a key advantage over approaches that produce continuous-valued outputs.

<!-- b003842 | heading | pages [18] -->
• Robustness to Prior and Distributional Changes: Sensitivity analyses demonstrate that

<!-- b003843 | prose | pages [18] -->
the BHDM model’s predictive performance remains stable across different settings of 𝜏2

<!-- b003844 | prose | pages [18] -->
(ranging from 0.1 to 10) and under ±5% variations to the total medal pool. As shown in Figures 5 and 6, the predicted 2028 medal counts and their credible intervals remain largely unaffected by these adjustments, indicating that the inference is driven more by the data than by the particular choice of prior or medal distribution assumptions.

<!-- b003845 | prose | pages [18] -->
Limitation.

<!-- b003846 | prose | pages [18] -->
• Complexity and Data Requirements: The hierarchical structure, while powerful for par- tial pooling and capturing cross-country heterogeneity, entails increased computational demands compared to simpler count models. Fitting the BHDM can become computa- tionally expensive for very large datasets or when a fine-grained, event-level breakdown is required for many countries. Furthermore, to reliably estimate country-specific random effects and hyperparameters (e.g., the 𝜙𝑖concentration parameters), the model benefits

<!-- b003847 | prose | pages [18] -->
关注数学模型

<!-- b003848 | furniture | pages [18] -->
2

<!-- b003849 | furniture | pages [18] -->
MATHmodels

<!-- b003850 | furniture | pages [18] -->
获取更多资讯

<!-- b003851 | furniture | pages [19] -->
Team # 2513314

<!-- b003852 | furniture | pages [19] -->
Page 19 of 22

<!-- b003853 | prose | pages [19] -->
from detailed, high-quality data—something that may be difficult to obtain for smaller or underrepresented countries with limited historical records.

<!-- b003854 | heading | pages [19] -->
Task 3: Other Original Insights of Our BHDM Model

<!-- b003855 | prose | pages [19] -->
9

<!-- b003856 | prose | pages [19] -->
Economic level determines medals 9.1

<!-- b003857 | prose | pages [19] -->
In our final analysis of all 206 countries in the dataset, two predictors stand out as having

<!-- b003858 | prose | pages [19] -->
微信公众号：数学模型

<!-- b003859 | prose | pages [19] -->
the largest impact on a nation’s Olympic medal count: historical performance (𝑋1) and athlete delegation size (𝑋2). Both variables are closely tied to a country’s economic level, as wealthier nations tend to have better-funded sports programs and a stronger history of Olympic participa- tion. Specifically, as reported in Table 7, the mean regression coefficient for past medal counts (𝛽𝑋1) is 0.035143, while that for total athlete numbers (𝛽𝑋2) is 0.011442. These results reinforce the notion that economic strength plays a decisive role in determining a country’s Olympic success. To interpret the magnitude of these effects:

<!-- b003860 | prose | pages [19] -->
𝑒0.035143 −1 ≈3.58%, 𝑒0.011442 −1 ≈1.15%. and

<!-- b003861 | prose | pages [19] -->
微信号：MATHmodels

<!-- b003862 | prose | pages [19] -->
Hence, a unit increase in 𝛽𝑋1 corresponds to roughly a 3.6% increase in the expected medal count, while a similar increase in 𝛽𝑋2 implies about a 1.2% rise. These results underscore that both a strong legacy of medal achievements and a robust delegation size can significantly boost a country’s chances of reaching the podium.

<!-- b003863 | caption | pages [19] -->
Table 7: Posterior Summary of 𝛽𝑋1 and 𝛽𝑋2 Across All Countries (206 in total).

<!-- b003864 | prose | pages [19] -->
Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Std. Err. Mean Outcome Beta Mean

<!-- b003865 | prose | pages [19] -->
𝛽𝑋1 0.035143 0.008224 𝛽𝑋2 0.011442 0.006538 0.981 204 0.945 178

<!-- b003866 | prose | pages [19] -->
By maintaining consistent investments in sports where they have historically excelled, countries can leverage existing expertise and well-established training systems. Meanwhile, increasing the breadth of participation through a larger delegation expands the probability of discovering or nurturing world-class athletes in more disciplines, ultimately translating into higher medal tallies.

<!-- b003867 | prose | pages [19] -->
Home Turf and Aligned Systems Prevail 9.2

<!-- b003868 | prose | pages [19] -->
Focusing on the subset of 33 countries that have hosted the Olympics at least once, our model reveals two important explanatory variables for elevating medal counts. Table 8 provides the posterior summary for:

<!-- b003869 | prose | pages [19] -->
1. Home Advantage (𝑋3): 𝛽𝑋3 has a mean of about 0.061245, which corresponds to:

<!-- b003870 | prose | pages [19] -->
𝑒0.061245 −1 ≈6.32% improvement.

<!-- b003871 | prose | pages [19] -->
This aligns well with the intuitive idea that home-country athletes benefit from logistical, infrastructural, and psychological advantages when competing on familiar ground.

<!-- b003872 | furniture | pages [20] -->
Team # 2513314

<!-- b003873 | furniture | pages [20] -->
Page 20 of 22

<!-- b003874 | prose | pages [20] -->
2. Social System Congruence (𝑋4): 𝛽𝑋4 has a mean of around 0.025982. In percentage terms:

<!-- b003875 | prose | pages [20] -->
𝑒0.025982 −1 ≈2.63% improvement.

<!-- b003876 | prose | pages [20] -->
Countries whose societal and institutional structures closely resemble those of the host may adapt more seamlessly to local conditions, cultural norms, and organizational protocols.

<!-- b003877 | caption | pages [20] -->
Table 8: Posterior Summary of 𝑋3 (Home Advantage) and 𝑋4 (Social System Congruence). There

<!-- b003878 | prose | pages [20] -->
are 33 host countries in total.

<!-- b003879 | prose | pages [20] -->
Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Std. Err. Mean Outcome Beta Mean

<!-- b003880 | prose | pages [20] -->
𝑋3: Home Advantage 0.010277 0.061245 𝑋4: Soc. System Congr.

<!-- b003881 | prose | pages [20] -->
0.980 33 0.007612 0.025982 0.955 30

<!-- b003882 | prose | pages [20] -->
In practical terms, this means a host nation can anticipate, on average, more than a 6% increase in its medal tally relative to non-host years. Moreover, a country resembling the host’s societal ecosystem—whether by language, cultural practices, or institutional frameworks—might also see an additional bump, albeit of a smaller magnitude. Proactive planning, like scouting local venues, training under similar conditions, and ensuring linguistic or cultural familiarity, can amplify these benefits for visiting teams as well.

<!-- b003883 | prose | pages [20] -->
Emerging Sports Aid Low-GDP Countries 9.3

<!-- b003884 | prose | pages [20] -->
Finally, our model points to a strategic pathway for 38 countries identified as being in the bottom 50% of world GDP according to the World Bank 2 and having already won at least one Olympic medal. As highlighted in Table 9, investing in less-established or newly introduced disciplines—captured by the indicator variable 𝛽𝑋8 for Emerging Events—provides these lower-GDP nations with a pronounced edge.

<!-- b003885 | caption | pages [20] -->
Table 9: Posterior Summary of 𝛽𝑋8 (Emerging Events) for 38 Low-GDP Medal-Winning Countries.

<!-- b003886 | prose | pages [20] -->
Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Std. Err. Mean Outcome Beta Mean

<!-- b003887 | prose | pages [20] -->
𝛽𝑋8 0.032413 0.006568 0.979 37

<!-- b003888 | prose | pages [20] -->
A mean coefficient of 0.032413 for 𝛽𝑋8 translates to about a

<!-- b003889 | prose | pages [20] -->
𝑒0.032413 −1 ≈3.29%

<!-- b003890 | prose | pages [20] -->
increment in medal counts for every unit increase in emerging-sport emphasis. In practice, this suggests that under-resourced nations can “level the playing field” by channeling their limited resources into newer sporting disciplines, where established powerhouses have yet to monopolize coaching expertise, infrastructure, and athlete development. Taking advantage of these relatively uncrowded competitive landscapes may thus maximize the return on investment for nations working within tighter financial and organizational constraints.

<!-- b003891 | prose | pages [20] -->
9.4 A letter to inform NOC

<!-- b003892 | prose | pages [20] -->
Based on the insights mentioned above, we have written a letter to NOC. The content of this letter is as follows:

<!-- b003893 | prose | pages [20] -->
2 http://data.worldbank.org

<!-- b003894 | prose | pages [20] -->
关注数学模型

<!-- b003895 | furniture | pages [20] -->
2

<!-- b003896 | furniture | pages [20] -->
MATHmodels

<!-- b003897 | furniture | pages [20] -->
获取更多资讯

<!-- b003898 | furniture | pages [21] -->
Team # 2513314

<!-- b003899 | furniture | pages [21] -->
Page 21 of 22

<!-- b003900 | prose | pages [21] -->
Some insights about Olympics Medal Counts

<!-- b003901 | prose | pages [21] -->
To: Country Olympics Committees From: Team #2513314 Data: January 27, 2025 Dear Country Olympics Committees leaders:

<!-- b003902 | prose | pages [21] -->
We are writing to share three major insights that can guide Olympic committees in crafting more effective, practical strategies for securing medals. Our analysis reveals how a nation’s economic capacity, its hosting opportunities, and its targeted focus on emerging sports can all

<!-- b003903 | prose | pages [21] -->
微信公众号：数学模型

<!-- b003904 | prose | pages [21] -->
contribute to elevating athletic performance on the global stage. By highlighting each factor in simple terms, we hope to show that even modest interventions can make a big difference when implemented thoughtfully.

<!-- b003905 | prose | pages [21] -->
First, our study clearly links economic strength to higher medal counts, chiefly through two channels: historical performance and the number of participating athletes. In plain language, if a country has a track record of success in certain sports, it likely possesses time-tested coaching expertise and training facilities that can be reinforced. At the same time, expanding the size of the athlete delegation—whether by discovering new talent or offering more support to existing programs—broadens the pool of potential medalists. Committees can utilize this insight by directing funds to sports with proven results while systematically scouting fresh talent to sustain

<!-- b003906 | prose | pages [21] -->
微信号：MATHmodels

<!-- b003907 | prose | pages [21] -->
a healthy pipeline for future competitions.

<!-- b003908 | prose | pages [21] -->
Second, there is a distinct “home turf” benefit for nations hosting the Olympics, as local teams have the advantage of competing in familiar environments with supportive crowds. Beyond that, countries that share cultural, linguistic, or societal characteristics with the host nation can also see smaller but meaningful boosts in performance. For instance, translating key materials into a common language and training athletes to adapt to local climates or customs can reduce logistical hiccups, ensuring a smoother preparation process. Committees might consider partnerships or cultural exchange programs with future hosts to gain on-the-ground knowledge and acclimate athletes well in advance.

<!-- b003909 | prose | pages [21] -->
Third, for nations with tighter budgets, focusing on newly introduced or less-established sports offers a unique chance to thrive. Because these disciplines are not yet dominated by well- funded powerhouses, smaller countries can step in with targeted investments—like specialized coaches, better equipment, or even grassroots talent-spotting efforts. By concentrating on these emerging events, committees can quickly close the gap and even outcompete wealthier nations still focused on mainstream sports. This tailored approach lets countries make the most of limited resources and diversify their medal potential.

<!-- b003910 | prose | pages [21] -->
In conclusion, each of these insights—prioritizing historically successful events and a wider athlete pool, leveraging home-field and cultural advantages, and capitalizing on emerging sports—gives Olympic committees a roadmap for thoughtful action. We trust this overview will help you shape meaningful strategies that tap into your nation’s inherent strengths and adapt to its financial realities, ultimately lifting your athletes to new heights of excellence.

<!-- b003911 | prose | pages [21] -->
Yours Sincerely,

<!-- b003912 | furniture | pages [21] -->
Team #2513314

<!-- b003913 | prose | pages [21] -->
m

<!-- b003914 | prose | pages [21] -->
m

<!-- b003915 | prose | pages [21] -->
m

<!-- b003916 | prose | pages [21] -->
m

<!-- b003917 | prose | pages [21] -->
m

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

<!-- b004197 | furniture | pages [21] -->
m

<!-- b004198 | furniture | pages [21] -->
m

<!-- b004199 | furniture | pages [21] -->
m

<!-- b004200 | furniture | pages [21] -->
m

<!-- b004201 | furniture | pages [21] -->
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

<!-- b004600 | furniture | pages [22] -->
Team # 2513314

<!-- b004601 | heading | pages [22] -->
References

<!-- b004602 | furniture | pages [22] -->
Page 22 of 22

<!-- b004603 | references | pages [22] -->
[1] Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system. pages 785–794,

<!-- b004604 | references | pages [22] -->
2016.

<!-- b004605 | references | pages [22] -->
[2] Gillian M Cook, David Fletcher, and Michael Peyrebrune. Olympic coaching excellence:

<!-- b004606 | references | pages [22] -->
A quantitative study of olympic swimmers’ perceptions of their coaches. Journal of sports

<!-- b004607 | references | pages [22] -->
sciences, 40(1):32–39, 2022.

<!-- b004608 | references | pages [22] -->
[3] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. Neural Computation,

<!-- b004609 | references | pages [22] -->
9(8):1735–1780, 1997.

<!-- b004610 | references | pages [22] -->
[4] Olympics.com. Biography: Lang Ping.

<!-- b004611 | references | pages [22] -->
g-lang. Accessed: January 25, 2025.

<!-- b004612 | references | pages [22] -->
https://olympics.com/en/athletes/pin

<!-- b004613 | references | pages [22] -->
m

<!-- b004614 | references | pages [22] -->
m

<!-- b004615 | references | pages [22] -->
m

<!-- b004616 | references | pages [22] -->
m

<!-- b004617 | references | pages [22] -->
m

<!-- b004618 | references | pages [22] -->
m

<!-- b004619 | references | pages [22] -->
m

<!-- b004620 | references | pages [22] -->
m

<!-- b004621 | references | pages [22] -->
m

<!-- b004622 | references | pages [22] -->
m

<!-- b004623 | references | pages [22] -->
m

<!-- b004624 | references | pages [22] -->
m

<!-- b004625 | references | pages [22] -->
m

<!-- b004626 | references | pages [22] -->
m

<!-- b004627 | references | pages [22] -->
m

<!-- b004628 | references | pages [22] -->
m

<!-- b004629 | references | pages [22] -->
m

<!-- b004630 | references | pages [22] -->
m

<!-- b004631 | references | pages [22] -->
m

<!-- b004632 | references | pages [22] -->
m

<!-- b004633 | references | pages [22] -->
m

<!-- b004634 | references | pages [22] -->
m

<!-- b004635 | references | pages [22] -->
[5] Congjun Rao, Ming Liu, Mark Goh, and Jianghui Wen. 2-stage modified random forest

<!-- b004636 | references | pages [22] -->
m

<!-- b004637 | references | pages [22] -->
m

<!-- b004638 | references | pages [22] -->
m

<!-- b004639 | references | pages [22] -->
m

<!-- b004640 | references | pages [22] -->
m

<!-- b004641 | references | pages [22] -->
m

<!-- b004642 | references | pages [22] -->
m

<!-- b004643 | references | pages [22] -->
m

<!-- b004644 | references | pages [22] -->
m

<!-- b004645 | references | pages [22] -->
m

<!-- b004646 | references | pages [22] -->
m

<!-- b004647 | references | pages [22] -->
m

<!-- b004648 | references | pages [22] -->
m

<!-- b004649 | references | pages [22] -->
m

<!-- b004650 | references | pages [22] -->
m

<!-- b004651 | references | pages [22] -->
m

<!-- b004652 | references | pages [22] -->
m

<!-- b004653 | references | pages [22] -->
m

<!-- b004654 | references | pages [22] -->
m

<!-- b004655 | references | pages [22] -->
m

<!-- b004656 | references | pages [22] -->
m

<!-- b004657 | references | pages [22] -->
m

<!-- b004658 | references | pages [22] -->
m

<!-- b004659 | references | pages [22] -->
m

<!-- b004660 | references | pages [22] -->
m

<!-- b004661 | references | pages [22] -->
m

<!-- b004662 | references | pages [22] -->
m

<!-- b004663 | references | pages [22] -->
m

<!-- b004664 | references | pages [22] -->
m

<!-- b004665 | references | pages [22] -->
m

<!-- b004666 | references | pages [22] -->
m

<!-- b004667 | references | pages [22] -->
m

<!-- b004668 | references | pages [22] -->
m

<!-- b004669 | references | pages [22] -->
m

<!-- b004670 | references | pages [22] -->
m

<!-- b004671 | references | pages [22] -->
m

<!-- b004672 | references | pages [22] -->
m

<!-- b004673 | references | pages [22] -->
m

<!-- b004674 | references | pages [22] -->
m

<!-- b004675 | references | pages [22] -->
m

<!-- b004676 | references | pages [22] -->
m

<!-- b004677 | references | pages [22] -->
m

<!-- b004678 | references | pages [22] -->
m

<!-- b004679 | references | pages [22] -->
m

<!-- b004680 | references | pages [22] -->
m

<!-- b004681 | references | pages [22] -->
m

<!-- b004682 | references | pages [22] -->
m

<!-- b004683 | references | pages [22] -->
m

<!-- b004684 | references | pages [22] -->
m

<!-- b004685 | references | pages [22] -->
m

<!-- b004686 | references | pages [22] -->
m

<!-- b004687 | references | pages [22] -->
m

<!-- b004688 | references | pages [22] -->
m

<!-- b004689 | references | pages [22] -->
m

<!-- b004690 | references | pages [22] -->
m

<!-- b004691 | references | pages [22] -->
m

<!-- b004692 | references | pages [22] -->
m

<!-- b004693 | references | pages [22] -->
m

<!-- b004694 | references | pages [22] -->
m

<!-- b004695 | references | pages [22] -->
m

<!-- b004696 | references | pages [22] -->
m

<!-- b004697 | references | pages [22] -->
m

<!-- b004698 | references | pages [22] -->
m

<!-- b004699 | references | pages [22] -->
m

<!-- b004700 | references | pages [22] -->
m

<!-- b004701 | references | pages [22] -->
m

<!-- b004702 | references | pages [22] -->
m

<!-- b004703 | references | pages [22] -->
m

<!-- b004704 | references | pages [22] -->
m

<!-- b004705 | references | pages [22] -->
m

<!-- b004706 | references | pages [22] -->
m

<!-- b004707 | references | pages [22] -->
m

<!-- b004708 | references | pages [22] -->
m

<!-- b004709 | references | pages [22] -->
m

<!-- b004710 | references | pages [22] -->
m

<!-- b004711 | references | pages [22] -->
m

<!-- b004712 | references | pages [22] -->
m

<!-- b004713 | references | pages [22] -->
m

<!-- b004714 | references | pages [22] -->
m

<!-- b004715 | references | pages [22] -->
m

<!-- b004716 | references | pages [22] -->
m

<!-- b004717 | references | pages [22] -->
m

<!-- b004718 | references | pages [22] -->
m

<!-- b004719 | references | pages [22] -->
m

<!-- b004720 | references | pages [22] -->
m

<!-- b004721 | references | pages [22] -->
m

<!-- b004722 | references | pages [22] -->
m

<!-- b004723 | references | pages [22] -->
m

<!-- b004724 | references | pages [22] -->
m

<!-- b004725 | references | pages [22] -->
m

<!-- b004726 | references | pages [22] -->
m

<!-- b004727 | references | pages [22] -->
m

<!-- b004728 | references | pages [22] -->
m

<!-- b004729 | references | pages [22] -->
m

<!-- b004730 | references | pages [22] -->
m

<!-- b004731 | references | pages [22] -->
m

<!-- b004732 | references | pages [22] -->
m

<!-- b004733 | references | pages [22] -->
m

<!-- b004734 | references | pages [22] -->
m

<!-- b004735 | references | pages [22] -->
m

<!-- b004736 | references | pages [22] -->
m

<!-- b004737 | references | pages [22] -->
m

<!-- b004738 | references | pages [22] -->
m

<!-- b004739 | references | pages [22] -->
m

<!-- b004740 | references | pages [22] -->
m

<!-- b004741 | references | pages [22] -->
m

<!-- b004742 | references | pages [22] -->
m

<!-- b004743 | references | pages [22] -->
m

<!-- b004744 | references | pages [22] -->
m

<!-- b004745 | references | pages [22] -->
m

<!-- b004746 | references | pages [22] -->
m

<!-- b004747 | references | pages [22] -->
m

<!-- b004748 | references | pages [22] -->
m

<!-- b004749 | references | pages [22] -->
m

<!-- b004750 | references | pages [22] -->
m

<!-- b004751 | references | pages [22] -->
m

<!-- b004752 | references | pages [22] -->
m

<!-- b004753 | references | pages [22] -->
m

<!-- b004754 | references | pages [22] -->
m

<!-- b004755 | references | pages [22] -->
m

<!-- b004756 | references | pages [22] -->
m

<!-- b004757 | references | pages [22] -->
m

<!-- b004758 | references | pages [22] -->
m

<!-- b004759 | references | pages [22] -->
m

<!-- b004760 | references | pages [22] -->
m

<!-- b004761 | references | pages [22] -->
m

<!-- b004762 | references | pages [22] -->
m

<!-- b004763 | references | pages [22] -->
m

<!-- b004764 | references | pages [22] -->
m

<!-- b004765 | references | pages [22] -->
m

<!-- b004766 | references | pages [22] -->
m

<!-- b004767 | references | pages [22] -->
m

<!-- b004768 | references | pages [22] -->
m

<!-- b004769 | references | pages [22] -->
m

<!-- b004770 | references | pages [22] -->
m

<!-- b004771 | references | pages [22] -->
m

<!-- b004772 | references | pages [22] -->
m

<!-- b004773 | references | pages [22] -->
m

<!-- b004774 | references | pages [22] -->
m

<!-- b004775 | references | pages [22] -->
m

<!-- b004776 | references | pages [22] -->
m

<!-- b004777 | references | pages [22] -->
m

<!-- b004778 | references | pages [22] -->
m

<!-- b004779 | references | pages [22] -->
m

<!-- b004780 | references | pages [22] -->
m

<!-- b004781 | references | pages [22] -->
model for credit risk assessment of p2p network lending to “three rurals” borrowers. Applied

<!-- b004782 | references | pages [22] -->
Soft Computing, 95:106570, 2020.

<!-- b004783 | references | pages [22] -->
m

<!-- b004784 | references | pages [22] -->
m

<!-- b004785 | references | pages [22] -->
m

<!-- b004786 | references | pages [22] -->
m

<!-- b004787 | references | pages [22] -->
m

<!-- b004788 | references | pages [22] -->
m

<!-- b004789 | references | pages [22] -->
m

<!-- b004790 | references | pages [22] -->
m

<!-- b004791 | references | pages [22] -->
m

<!-- b004792 | references | pages [22] -->
m

<!-- b004793 | references | pages [22] -->
m

<!-- b004794 | references | pages [22] -->
m

<!-- b004795 | references | pages [22] -->
m

<!-- b004796 | references | pages [22] -->
m

<!-- b004797 | references | pages [22] -->
m

<!-- b004798 | references | pages [22] -->
m

<!-- b004799 | references | pages [22] -->
m

<!-- b004800 | references | pages [22] -->
m

<!-- b004801 | references | pages [22] -->
m

<!-- b004802 | references | pages [22] -->
m

<!-- b004803 | references | pages [22] -->
m

<!-- b004804 | references | pages [22] -->
m

<!-- b004805 | references | pages [22] -->
m

<!-- b004806 | references | pages [22] -->
m

<!-- b004807 | references | pages [22] -->
m

<!-- b004808 | references | pages [22] -->
m

<!-- b004809 | references | pages [22] -->
m

<!-- b004810 | references | pages [22] -->
m

<!-- b004811 | references | pages [22] -->
m

<!-- b004812 | references | pages [22] -->
m

<!-- b004813 | references | pages [22] -->
m

<!-- b004814 | references | pages [22] -->
m

<!-- b004815 | references | pages [22] -->
m

<!-- b004816 | references | pages [22] -->
m

<!-- b004817 | references | pages [22] -->
m

<!-- b004818 | references | pages [22] -->
m

<!-- b004819 | references | pages [22] -->
m

<!-- b004820 | references | pages [22] -->
m

<!-- b004821 | references | pages [22] -->
m

<!-- b004822 | references | pages [22] -->
m

<!-- b004823 | references | pages [22] -->
m

<!-- b004824 | references | pages [22] -->
m

<!-- b004825 | references | pages [22] -->
m

<!-- b004826 | references | pages [22] -->
m

<!-- b004827 | references | pages [22] -->
m

<!-- b004828 | references | pages [22] -->
m

<!-- b004829 | references | pages [22] -->
m

<!-- b004830 | references | pages [22] -->
m

<!-- b004831 | references | pages [22] -->
m

<!-- b004832 | references | pages [22] -->
m

<!-- b004833 | references | pages [22] -->
m

<!-- b004834 | references | pages [22] -->
m

<!-- b004835 | references | pages [22] -->
m

<!-- b004836 | references | pages [22] -->
m

<!-- b004837 | references | pages [22] -->
m

<!-- b004838 | references | pages [22] -->
m

<!-- b004839 | references | pages [22] -->
m

<!-- b004840 | references | pages [22] -->
m

<!-- b004841 | references | pages [22] -->
m

<!-- b004842 | references | pages [22] -->
m

<!-- b004843 | references | pages [22] -->
m

<!-- b004844 | references | pages [22] -->
m

<!-- b004845 | references | pages [22] -->
m

<!-- b004846 | references | pages [22] -->
m

<!-- b004847 | references | pages [22] -->
m

<!-- b004848 | references | pages [22] -->
m

<!-- b004849 | references | pages [22] -->
m

<!-- b004850 | references | pages [22] -->
m

<!-- b004851 | references | pages [22] -->
m

<!-- b004852 | references | pages [22] -->
m

<!-- b004853 | references | pages [22] -->
m

<!-- b004854 | references | pages [22] -->
m

<!-- b004855 | references | pages [22] -->
m

<!-- b004856 | references | pages [22] -->
m

<!-- b004857 | references | pages [22] -->
m

<!-- b004858 | references | pages [22] -->
m

<!-- b004859 | references | pages [22] -->
m

<!-- b004860 | references | pages [22] -->
m

<!-- b004861 | references | pages [22] -->
m

<!-- b004862 | references | pages [22] -->
m

<!-- b004863 | references | pages [22] -->
m

<!-- b004864 | references | pages [22] -->
m

<!-- b004865 | references | pages [22] -->
m

<!-- b004866 | references | pages [22] -->
m

<!-- b004867 | references | pages [22] -->
m

<!-- b004868 | references | pages [22] -->
m

<!-- b004869 | references | pages [22] -->
m

<!-- b004870 | references | pages [22] -->
m

<!-- b004871 | references | pages [22] -->
m

<!-- b004872 | references | pages [22] -->
m

<!-- b004873 | references | pages [22] -->
m

<!-- b004874 | references | pages [22] -->
m

<!-- b004875 | references | pages [22] -->
m

<!-- b004876 | references | pages [22] -->
m

<!-- b004877 | references | pages [22] -->
m

<!-- b004878 | references | pages [22] -->
m

<!-- b004879 | references | pages [22] -->
m

<!-- b004880 | references | pages [22] -->
m

<!-- b004881 | references | pages [22] -->
m

<!-- b004882 | references | pages [22] -->
m

<!-- b004883 | references | pages [22] -->
m

<!-- b004884 | references | pages [22] -->
m

<!-- b004885 | references | pages [22] -->
m

<!-- b004886 | references | pages [22] -->
m

<!-- b004887 | references | pages [22] -->
m

<!-- b004888 | references | pages [22] -->
m

<!-- b004889 | references | pages [22] -->
m

<!-- b004890 | references | pages [22] -->
m

<!-- b004891 | references | pages [22] -->
m

<!-- b004892 | references | pages [22] -->
m

<!-- b004893 | references | pages [22] -->
m

<!-- b004894 | references | pages [22] -->
m

<!-- b004895 | references | pages [22] -->
m

<!-- b004896 | references | pages [22] -->
m

<!-- b004897 | references | pages [22] -->
m

<!-- b004898 | references | pages [22] -->
m

<!-- b004899 | references | pages [22] -->
m

<!-- b004900 | references | pages [22] -->
m

<!-- b004901 | references | pages [22] -->
m

<!-- b004902 | references | pages [22] -->
m

<!-- b004903 | references | pages [22] -->
m

<!-- b004904 | references | pages [22] -->
m

<!-- b004905 | references | pages [22] -->
m

<!-- b004906 | references | pages [22] -->
m

<!-- b004907 | references | pages [22] -->
m

<!-- b004908 | references | pages [22] -->
m

<!-- b004909 | references | pages [22] -->
m

<!-- b004910 | references | pages [22] -->
m

<!-- b004911 | references | pages [22] -->
m

<!-- b004912 | references | pages [22] -->
m

<!-- b004913 | references | pages [22] -->
m

<!-- b004914 | references | pages [22] -->
m

<!-- b004915 | references | pages [22] -->
m

<!-- b004916 | references | pages [22] -->
m

<!-- b004917 | references | pages [22] -->
m

<!-- b004918 | references | pages [22] -->
m

<!-- b004919 | references | pages [22] -->
m

<!-- b004920 | references | pages [22] -->
m

<!-- b004921 | references | pages [22] -->
m

<!-- b004922 | references | pages [22] -->
m

<!-- b004923 | references | pages [22] -->
m

<!-- b004924 | references | pages [22] -->
m

<!-- b004925 | references | pages [22] -->
m

<!-- b004926 | references | pages [22] -->
m

<!-- b004927 | references | pages [22] -->
m

<!-- b004928 | references | pages [22] -->
m

<!-- b004929 | references | pages [22] -->
m

<!-- b004930 | references | pages [22] -->
m

<!-- b004931 | references | pages [22] -->
m

<!-- b004932 | references | pages [22] -->
m

<!-- b004933 | references | pages [22] -->
m

<!-- b004934 | references | pages [22] -->
m

<!-- b004935 | references | pages [22] -->
m

<!-- b004936 | references | pages [22] -->
m

<!-- b004937 | references | pages [22] -->
m

<!-- b004938 | references | pages [22] -->
m

<!-- b004939 | references | pages [22] -->
m

<!-- b004940 | references | pages [22] -->
m

<!-- b004941 | references | pages [22] -->
m

<!-- b004942 | references | pages [22] -->
m

<!-- b004943 | references | pages [22] -->
m

<!-- b004944 | references | pages [22] -->
m

<!-- b004945 | references | pages [22] -->
m

<!-- b004946 | references | pages [22] -->
m

<!-- b004947 | references | pages [22] -->
m

<!-- b004948 | references | pages [22] -->
m

<!-- b004949 | references | pages [22] -->
m

<!-- b004950 | references | pages [22] -->
m

<!-- b004951 | references | pages [22] -->
m

<!-- b004952 | references | pages [22] -->
m

<!-- b004953 | references | pages [22] -->
m

<!-- b004954 | references | pages [22] -->
m

<!-- b004955 | references | pages [22] -->
m

<!-- b004956 | references | pages [22] -->
m

<!-- b004957 | references | pages [22] -->
m

<!-- b004958 | references | pages [22] -->
m

<!-- b004959 | references | pages [22] -->
m

<!-- b004960 | references | pages [22] -->
m

<!-- b004961 | references | pages [22] -->
m

<!-- b004962 | references | pages [22] -->
m

<!-- b004963 | references | pages [22] -->
m

<!-- b004964 | references | pages [22] -->
m

<!-- b004965 | references | pages [22] -->
m

<!-- b004966 | references | pages [22] -->
m

<!-- b004967 | references | pages [22] -->
m

<!-- b004968 | references | pages [22] -->
m

<!-- b004969 | references | pages [22] -->
m

<!-- b004970 | references | pages [22] -->
m

<!-- b004971 | references | pages [22] -->
m

<!-- b004972 | references | pages [22] -->
m

<!-- b004973 | references | pages [22] -->
m

<!-- b004974 | references | pages [22] -->
m

<!-- b004975 | references | pages [22] -->
m

<!-- b004976 | references | pages [22] -->
m

<!-- b004977 | references | pages [22] -->
m

<!-- b004978 | references | pages [22] -->
m

<!-- b004979 | references | pages [22] -->
m

<!-- b004980 | references | pages [22] -->
m

<!-- b004981 | references | pages [22] -->
m

<!-- b004982 | references | pages [22] -->
m

<!-- b004983 | references | pages [22] -->
m

<!-- b004984 | references | pages [22] -->
m

<!-- b004985 | references | pages [22] -->
m

<!-- b004986 | references | pages [22] -->
m

<!-- b004987 | references | pages [22] -->
m

<!-- b004988 | references | pages [22] -->
m

<!-- b004989 | references | pages [22] -->
m

<!-- b004990 | references | pages [22] -->
m

<!-- b004991 | references | pages [22] -->
m

<!-- b004992 | references | pages [22] -->
m

<!-- b004993 | references | pages [22] -->
m

<!-- b004994 | references | pages [22] -->
m

<!-- b004995 | references | pages [22] -->
m

<!-- b004996 | references | pages [22] -->
m

<!-- b004997 | references | pages [22] -->
m

<!-- b004998 | references | pages [22] -->
m

<!-- b004999 | references | pages [22] -->
m

<!-- b005000 | references | pages [22] -->
m

<!-- b005001 | references | pages [22] -->
m

<!-- b005002 | references | pages [22] -->
m

<!-- b005003 | references | pages [22] -->
m

<!-- b005004 | references | pages [22] -->
m

<!-- b005005 | references | pages [22] -->
m

<!-- b005006 | references | pages [22] -->
m

<!-- b005007 | references | pages [22] -->
m

<!-- b005008 | references | pages [22] -->
m

<!-- b005009 | references | pages [22] -->
m

<!-- b005010 | references | pages [22] -->
m

<!-- b005011 | references | pages [22] -->
m

<!-- b005012 | references | pages [22] -->
m

<!-- b005013 | references | pages [22] -->
m

<!-- b005014 | references | pages [22] -->
m

<!-- b005015 | references | pages [22] -->
m

<!-- b005016 | references | pages [22] -->
m

<!-- b005017 | references | pages [22] -->
m

<!-- b005018 | references | pages [22] -->
m

<!-- b005019 | references | pages [22] -->
m

<!-- b005020 | references | pages [22] -->
m

<!-- b005021 | references | pages [22] -->
m

<!-- b005022 | references | pages [22] -->
m

<!-- b005023 | references | pages [22] -->
m

<!-- b005024 | references | pages [22] -->
m

<!-- b005025 | references | pages [22] -->
m

<!-- b005026 | references | pages [22] -->
m

<!-- b005027 | references | pages [22] -->
m

<!-- b005028 | references | pages [22] -->
m

<!-- b005029 | references | pages [22] -->
m

<!-- b005030 | references | pages [22] -->
m

<!-- b005031 | references | pages [22] -->
m

<!-- b005032 | references | pages [22] -->
m

<!-- b005033 | references | pages [22] -->
m

<!-- b005034 | references | pages [22] -->
m

<!-- b005035 | references | pages [22] -->
m

<!-- b005036 | references | pages [22] -->
m

<!-- b005037 | references | pages [22] -->
m

<!-- b005038 | references | pages [22] -->
m

<!-- b005039 | references | pages [22] -->
m

<!-- b005040 | references | pages [22] -->
m

<!-- b005041 | references | pages [22] -->
m

<!-- b005042 | references | pages [22] -->
m

<!-- b005043 | references | pages [22] -->
m

<!-- b005044 | references | pages [22] -->
m

<!-- b005045 | references | pages [22] -->
m

<!-- b005046 | references | pages [22] -->
m

<!-- b005047 | references | pages [22] -->
m

<!-- b005048 | references | pages [22] -->
m

<!-- b005049 | references | pages [22] -->
m

<!-- b005050 | references | pages [22] -->
m

<!-- b005051 | references | pages [22] -->
m

<!-- b005052 | references | pages [22] -->
m

<!-- b005053 | references | pages [22] -->
m

<!-- b005054 | references | pages [22] -->
m

<!-- b005055 | references | pages [22] -->
m

<!-- b005056 | references | pages [22] -->
m

<!-- b005057 | references | pages [22] -->
m

<!-- b005058 | references | pages [22] -->
m

<!-- b005059 | references | pages [22] -->
m

<!-- b005060 | references | pages [22] -->
m

<!-- b005061 | references | pages [22] -->
m

<!-- b005062 | references | pages [22] -->
m

<!-- b005063 | references | pages [22] -->
m

<!-- b005064 | references | pages [22] -->
m

<!-- b005065 | references | pages [22] -->
m

<!-- b005066 | references | pages [22] -->
m

<!-- b005067 | references | pages [22] -->
m

<!-- b005068 | references | pages [22] -->
m

<!-- b005069 | references | pages [22] -->
m

<!-- b005070 | references | pages [22] -->
m

<!-- b005071 | references | pages [22] -->
m

<!-- b005072 | references | pages [22] -->
m

<!-- b005073 | references | pages [22] -->
m

<!-- b005074 | references | pages [22] -->
m

<!-- b005075 | references | pages [22] -->
m

<!-- b005076 | references | pages [22] -->
m

<!-- b005077 | references | pages [22] -->
m

<!-- b005078 | references | pages [22] -->
m

<!-- b005079 | references | pages [22] -->
m

<!-- b005080 | references | pages [22] -->
m

<!-- b005081 | references | pages [22] -->
m

<!-- b005082 | references | pages [22] -->
m

<!-- b005083 | references | pages [22] -->
m

<!-- b005084 | references | pages [22] -->
m

<!-- b005085 | references | pages [22] -->
m

<!-- b005086 | references | pages [22] -->
m

<!-- b005087 | references | pages [22] -->
m

<!-- b005088 | references | pages [22] -->
m

<!-- b005089 | references | pages [22] -->
m

<!-- b005090 | references | pages [22] -->
m

<!-- b005091 | references | pages [22] -->
m

<!-- b005092 | references | pages [22] -->
m

<!-- b005093 | references | pages [22] -->
m

<!-- b005094 | references | pages [22] -->
m

<!-- b005095 | references | pages [22] -->
m

<!-- b005096 | references | pages [22] -->
m

<!-- b005097 | references | pages [22] -->
m

<!-- b005098 | references | pages [22] -->
m

<!-- b005099 | references | pages [22] -->
m

<!-- b005100 | references | pages [22] -->
m

<!-- b005101 | references | pages [22] -->
m

<!-- b005102 | references | pages [22] -->
m

<!-- b005103 | references | pages [22] -->
m

<!-- b005104 | references | pages [22] -->
m

<!-- b005105 | references | pages [22] -->
m

<!-- b005106 | references | pages [22] -->
m

<!-- b005107 | references | pages [22] -->
m

<!-- b005108 | references | pages [22] -->
m

<!-- b005109 | references | pages [22] -->
m

<!-- b005110 | references | pages [22] -->
m

<!-- b005111 | references | pages [22] -->
m

<!-- b005112 | references | pages [22] -->
m

<!-- b005113 | references | pages [22] -->
m

<!-- b005114 | references | pages [22] -->
m

<!-- b005115 | references | pages [22] -->
m

<!-- b005116 | references | pages [22] -->
m

<!-- b005117 | references | pages [22] -->
m

<!-- b005118 | references | pages [22] -->
m

<!-- b005119 | references | pages [22] -->
m

<!-- b005120 | references | pages [22] -->
m

<!-- b005121 | references | pages [22] -->
m

<!-- b005122 | references | pages [22] -->
m

<!-- b005123 | references | pages [22] -->
m

<!-- b005124 | references | pages [22] -->
m

<!-- b005125 | references | pages [22] -->
m

<!-- b005126 | references | pages [22] -->
m

<!-- b005127 | references | pages [22] -->
m

<!-- b005128 | references | pages [22] -->
m

<!-- b005129 | references | pages [22] -->
m

<!-- b005130 | references | pages [22] -->
m

<!-- b005131 | references | pages [22] -->
m

<!-- b005132 | references | pages [22] -->
m

<!-- b005133 | references | pages [22] -->
m

<!-- b005134 | references | pages [22] -->
m

<!-- b005135 | references | pages [22] -->
m

<!-- b005136 | references | pages [22] -->
m

<!-- b005137 | references | pages [22] -->
m

<!-- b005138 | references | pages [22] -->
m

<!-- b005139 | references | pages [22] -->
m

<!-- b005140 | references | pages [22] -->
m

<!-- b005141 | references | pages [22] -->
m

<!-- b005142 | references | pages [22] -->
m

<!-- b005143 | references | pages [22] -->
m

<!-- b005144 | references | pages [22] -->
m

<!-- b005145 | references | pages [22] -->
m

<!-- b005146 | references | pages [22] -->
m

<!-- b005147 | references | pages [22] -->
m

<!-- b005148 | references | pages [22] -->
[6] Gary A Sailes. The myth of black sports supremacy. Journal of Black Studies, 21(4):480–

<!-- b005149 | references | pages [22] -->
487, 1991.

<!-- b005150 | references | pages [22] -->
m

<!-- b005151 | references | pages [22] -->
m

<!-- b005152 | references | pages [22] -->
m

<!-- b005153 | references | pages [22] -->
m

<!-- b005154 | references | pages [22] -->
m

<!-- b005155 | references | pages [22] -->
m

<!-- b005156 | references | pages [22] -->
m

<!-- b005157 | references | pages [22] -->
m

<!-- b005158 | references | pages [22] -->
m

<!-- b005159 | references | pages [22] -->
m

<!-- b005160 | references | pages [22] -->
m

<!-- b005161 | references | pages [22] -->
m

<!-- b005162 | references | pages [22] -->
m

<!-- b005163 | references | pages [22] -->
m

<!-- b005164 | references | pages [22] -->
m

<!-- b005165 | references | pages [22] -->
m

<!-- b005166 | references | pages [22] -->
m

<!-- b005167 | references | pages [22] -->
m

<!-- b005168 | references | pages [22] -->
m

<!-- b005169 | references | pages [22] -->
m

<!-- b005170 | references | pages [22] -->
m

<!-- b005171 | references | pages [22] -->
m

<!-- b005172 | references | pages [22] -->
m

<!-- b005173 | references | pages [22] -->
m

<!-- b005174 | references | pages [22] -->
m

<!-- b005175 | references | pages [22] -->
m

<!-- b005176 | references | pages [22] -->
m

<!-- b005177 | references | pages [22] -->
m

<!-- b005178 | references | pages [22] -->
m

<!-- b005179 | references | pages [22] -->
m

<!-- b005180 | references | pages [22] -->
m

<!-- b005181 | references | pages [22] -->
m

<!-- b005182 | references | pages [22] -->
m

<!-- b005183 | references | pages [22] -->
m

<!-- b005184 | references | pages [22] -->
m

<!-- b005185 | references | pages [22] -->
m

<!-- b005186 | references | pages [22] -->
m

<!-- b005187 | references | pages [22] -->
m

<!-- b005188 | references | pages [22] -->
m

<!-- b005189 | references | pages [22] -->
m

<!-- b005190 | references | pages [22] -->
m

<!-- b005191 | references | pages [22] -->
m

<!-- b005192 | references | pages [22] -->
m

<!-- b005193 | references | pages [22] -->
m

<!-- b005194 | references | pages [22] -->
m

<!-- b005195 | references | pages [22] -->
m

<!-- b005196 | references | pages [22] -->
m

<!-- b005197 | references | pages [22] -->
m

<!-- b005198 | references | pages [22] -->
m

<!-- b005199 | references | pages [22] -->
m

<!-- b005200 | references | pages [22] -->
m

<!-- b005201 | references | pages [22] -->
m

<!-- b005202 | references | pages [22] -->
m

<!-- b005203 | references | pages [22] -->
m

<!-- b005204 | references | pages [22] -->
m

<!-- b005205 | references | pages [22] -->
m

<!-- b005206 | references | pages [22] -->
m

<!-- b005207 | references | pages [22] -->
m

<!-- b005208 | references | pages [22] -->
m

<!-- b005209 | references | pages [22] -->
m

<!-- b005210 | references | pages [22] -->
m

<!-- b005211 | references | pages [22] -->
m

<!-- b005212 | references | pages [22] -->
m

<!-- b005213 | references | pages [22] -->
m

<!-- b005214 | references | pages [22] -->
m

<!-- b005215 | references | pages [22] -->
m

<!-- b005216 | references | pages [22] -->
m

<!-- b005217 | references | pages [22] -->
m

<!-- b005218 | references | pages [22] -->
m

<!-- b005219 | references | pages [22] -->
m

<!-- b005220 | references | pages [22] -->
m

<!-- b005221 | references | pages [22] -->
m

<!-- b005222 | references | pages [22] -->
m

<!-- b005223 | references | pages [22] -->
m

<!-- b005224 | references | pages [22] -->
m

<!-- b005225 | references | pages [22] -->
m

<!-- b005226 | references | pages [22] -->
m

<!-- b005227 | references | pages [22] -->
m

<!-- b005228 | references | pages [22] -->
m

<!-- b005229 | references | pages [22] -->
m

<!-- b005230 | references | pages [22] -->
m

<!-- b005231 | references | pages [22] -->
m

<!-- b005232 | references | pages [22] -->
m

<!-- b005233 | references | pages [22] -->
m

<!-- b005234 | references | pages [22] -->
m

<!-- b005235 | references | pages [22] -->
m

<!-- b005236 | references | pages [22] -->
m

<!-- b005237 | references | pages [22] -->
m

<!-- b005238 | references | pages [22] -->
m

<!-- b005239 | references | pages [22] -->
m

<!-- b005240 | references | pages [22] -->
m

<!-- b005241 | references | pages [22] -->
m

<!-- b005242 | references | pages [22] -->
m

<!-- b005243 | references | pages [22] -->
m

<!-- b005244 | references | pages [22] -->
m

<!-- b005245 | references | pages [22] -->
m

<!-- b005246 | references | pages [22] -->
m

<!-- b005247 | references | pages [22] -->
m

<!-- b005248 | references | pages [22] -->
m

<!-- b005249 | references | pages [22] -->
m

<!-- b005250 | references | pages [22] -->
m

<!-- b005251 | references | pages [22] -->
m

<!-- b005252 | references | pages [22] -->
m

<!-- b005253 | references | pages [22] -->
m

<!-- b005254 | references | pages [22] -->
m

<!-- b005255 | references | pages [22] -->
m

<!-- b005256 | references | pages [22] -->
m

<!-- b005257 | references | pages [22] -->
m

<!-- b005258 | references | pages [22] -->
m

<!-- b005259 | references | pages [22] -->
m

<!-- b005260 | references | pages [22] -->
m

<!-- b005261 | references | pages [22] -->
m

<!-- b005262 | references | pages [22] -->
m

<!-- b005263 | references | pages [22] -->
m

<!-- b005264 | references | pages [22] -->
m

<!-- b005265 | references | pages [22] -->
m

<!-- b005266 | references | pages [22] -->
m

<!-- b005267 | references | pages [22] -->
m

<!-- b005268 | references | pages [22] -->
m

<!-- b005269 | references | pages [22] -->
m

<!-- b005270 | references | pages [22] -->
m

<!-- b005271 | references | pages [22] -->
m

<!-- b005272 | references | pages [22] -->
m

<!-- b005273 | references | pages [22] -->
m

<!-- b005274 | references | pages [22] -->
m

<!-- b005275 | references | pages [22] -->
m

<!-- b005276 | references | pages [22] -->
m

<!-- b005277 | references | pages [22] -->
m

<!-- b005278 | references | pages [22] -->
m

<!-- b005279 | references | pages [22] -->
m

<!-- b005280 | references | pages [22] -->
m

<!-- b005281 | references | pages [22] -->
m

<!-- b005282 | references | pages [22] -->
m

<!-- b005283 | references | pages [22] -->
m

<!-- b005284 | references | pages [22] -->
m

<!-- b005285 | references | pages [22] -->
m

<!-- b005286 | references | pages [22] -->
m

<!-- b005287 | references | pages [22] -->
m

<!-- b005288 | references | pages [22] -->
m

<!-- b005289 | references | pages [22] -->
m

<!-- b005290 | references | pages [22] -->
m

<!-- b005291 | references | pages [22] -->
m

<!-- b005292 | references | pages [22] -->
m

<!-- b005293 | references | pages [22] -->
m

<!-- b005294 | references | pages [22] -->
m

<!-- b005295 | references | pages [22] -->
m

<!-- b005296 | references | pages [22] -->
m

<!-- b005297 | references | pages [22] -->
m

<!-- b005298 | references | pages [22] -->
m

<!-- b005299 | references | pages [22] -->
m

<!-- b005300 | references | pages [22] -->
m

<!-- b005301 | references | pages [22] -->
m

<!-- b005302 | references | pages [22] -->
m

<!-- b005303 | references | pages [22] -->
m

<!-- b005304 | references | pages [22] -->
m

<!-- b005305 | references | pages [22] -->
[7] Christoph Schlembach, Sascha L. Schmidt, Dominik Schreyer, and Linus Wunderlich.

<!-- b005306 | references | pages [22] -->
Forecasting the olympic medal distribution – a socioeconomic machine learning model.

<!-- b005307 | references | pages [22] -->
Technological Forecasting and Social Change, 175:121314, 2022.

<!-- b005308 | references | pages [22] -->
https://usagym.org/hallo

<!-- b005309 | references | pages [22] -->
[8] USA Gymnastics Hall of Fame. Béla & Márta Károlyi.

<!-- b005310 | references | pages [22] -->
ffame/inductee/coaching-team-bela-martha-karolyi/. Accessed: January 25,

<!-- b005311 | references | pages [22] -->
2025.

<!-- b005312 | references | pages [22] -->
关注数学模型

<!-- b005313 | furniture | pages [22] -->
2

<!-- b005314 | furniture | pages [22] -->
MATHmodels

<!-- b005315 | furniture | pages [22] -->
获取更多资讯
