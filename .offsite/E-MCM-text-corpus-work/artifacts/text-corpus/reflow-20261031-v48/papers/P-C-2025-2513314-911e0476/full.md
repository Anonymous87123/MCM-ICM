# P-C-2025-2513314-911e0476

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
This method exhibits strong performance, achieving R2 of 0.85 for total medals and 0.80 for gold medals, surpassing all baseline models. Our 2028 projections show the U.S. winning 146 medals (95% CI: 136–156) and 53 golds (95% CI: 50–56), an increase from 2024, while China’s total medals decline to 82. We also computed ice-breaking probabilities, with Malaysia (68.6%) and South Sudan (39.0%) most likely to win their first medals. Regression analysis identified key sports for the U.S., China, the U.K., and France, offering strategic insights for host nations to optimize medal prospects.

<!-- b000018 | prose | pages [1] -->
For Task 2, we investigate the “Great Coach” effect. First, we define great coaches and construct a national-level great coach variable to quantify each country’s coaching strength. We then incorporate this variable into the BHDM model and analyze its impact through regression coefficients.

<!-- b000019 | prose | pages [1] -->
The results indicate that great coaches significantly influence both total and gold medal counts. Specifically, for the United States, China, and Japan, a one-unit increase in this vari- able leads to an expected medal count increase of 3.74%, 4.55%, and 2.87%, respectively. Additionally, we examine key sports in these three nations to assess the impact of this effect.

<!-- b000020 | prose | pages [1] -->
To test the robustness of our model, we conducted sensitivity analyses on both the weakly informative priors and the assumption of equal medal distribution. The results indicate that, despite adjustments in parameters and distributions, the model maintains reasonable predictive performance, with onlyminor deviationsfrom theoriginal baseline, demonstratingits robustness.

<!-- b000021 | prose | pages [1] -->
For Task 3, based on the comprehensive modeling process above, we derived three additional insights: Economic level determines medals, Home Turf and Aligned Systems Prevail, and Emerging Sports Aid Low-GDP Countries. We communicated these insights in a letter to the NOC, aiming to enhance their strategies and help nations secure more gold medals.

<!-- b000022 | keywords | pages [1] -->
Keywords: Bayesian Hierarchical Dirichlet-Multinomial, Posterior inference, Uncertainty

<!-- b000023 | prose | pages [1] -->
Quantification, Regression Analysis, Credible Intervals

<!-- b000024 | furniture | pages [2] -->
Team # 2513314

<!-- b000025 | furniture | pages [2] -->
Page 2 of 22

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | heading | pages [2] -->
Introduction

<!-- b000029 | prose | pages [2] -->
1 3 1.1

<!-- b000030 | heading | pages [2] -->
Background

<!-- b000031 | prose | pages [2] -->
模型 1.2

<!-- b000032 | heading | pages [2] -->
Problem Restatement

<!-- b000033 | prose | pages [2] -->
3 1.3 4 Our Work

<!-- b000034 | prose | pages [2] -->
5 Assumptions and Justifications 2

<!-- b000035 | heading | pages [2] -->
Notations

<!-- b000036 | prose | pages [2] -->
5 3

<!-- b000037 | prose | pages [2] -->
Data Pre-processing 5 4 Data Cleaning 6 4.1 4.2 A glimpse of dataset 6

<!-- b000038 | prose | pages [2] -->
Task 1: Predicting Medals of 2028 LA Olympics 6 5 Key Variables Influencing Olympic Medal Success 5.1 6 5.2

<!-- b000039 | heading | pages [2] -->
Bayesian Hierarchical Dirichlet-Multinomial (BHDM) Model

<!-- b000040 | prose | pages [2] -->
7 10 5.3 Projects of LA 2028 .

<!-- b000041 | prose | pages [2] -->
11 5.4 The country that will achieve a Breakthrough From Zero 12 5.5 Important Sports and Home Event Impact

<!-- b000042 | prose | pages [2] -->
Task 2: Dive Into Great Coach Effect 13 6 6.1 What is a Great Coach? 14 Great Coach Affect the Medals 6.2 14 Invest in Great Coach and Estimate its Impact 15 6.3

<!-- b000043 | prose | pages [2] -->
16 7

<!-- b000044 | heading | pages [2] -->
Sensitivity Analysis for τ2 Values

<!-- b000045 | prose | pages [2] -->
16 7.1

<!-- b000046 | heading | pages [2] -->
Sensitivity Analysis of Equal Distribution Assumptions

<!-- b000047 | prose | pages [2] -->
17 7.2

<!-- b000048 | heading | pages [2] -->
Strengths and Limitation of the Proposed Model

<!-- b000049 | prose | pages [2] -->
17 8

<!-- b000050 | heading | pages [2] -->
Task 3: Other Original Insights of Our BHDM Model

<!-- b000051 | prose | pages [2] -->
19 9 19 Economic level determines medals 9.1 9.2 Home Turf and Aligned Systems Prevail 19 9.3 Emerging Sports Aid Low-GDP Countries 20 A letter to inform NOC 20 9.4

<!-- b000052 | prose | pages [2] -->
Some insights about Olympics Medal Counts 21 信 微

<!-- b000053 | heading | pages [2] -->
References

<!-- b000054 | references | pages [2] -->
22

<!-- b000055 | references | pages [2] -->
关注数学模型

<!-- b000056 | furniture | pages [2] -->
获取更多资讯

<!-- b000057 | furniture | pages [3] -->
Team # 2513314

<!-- b000058 | furniture | pages [3] -->
Page 3 of 22

<!-- b000059 | heading | pages [3] -->
1 Introduction

<!-- b000060 | heading | pages [3] -->
1.1 Background

<!-- b000061 | prose | pages [3] -->
The Olympic Games, held every four years, bring together the world’s top athletes to compete in a wide range of sports. Since the first modern Olympics in 1896, the event has grown significantly in scale, with more countries participating and more events being introduced. 微信公众号：数学模型 Medal counts serve as a key indicator of national sports performance, reflecting a country’s investment in athletics, talent development, and international competitiveness.

<!-- b000062 | caption | pages [3] -->
Figure 1: The 2028 Summer Olympics will be held in Los Angeles, USA.

<!-- b000063 | prose | pages [3] -->
微信号：MATHmodels Predicting Olympic medal counts is an important challenge, as it provides insights into national sports strategies and performance trends. Various factors influence a country’s medal prospects, including economic resources, population size, sports infrastructure, and historical performance. Additionally, host nations often experience a boost in medal counts due to home-field advantages and increased investment. A robust predictive model can help sports organizations allocate resources efficiently and set realistic goals for future Olympic Games.

<!-- b000064 | prose | pages [3] -->
Beyond national investment, coaching plays a critical role in athletic success. Some elite coaches have significantly impacted multiple countries’ performances, demonstrating a “Great Coach” effect. By analyzing historical data, it is possible to quantify this effect and identify sports where hiring top-level coaches could maximize a nation’s medal potential. Understanding the role of coaching in Olympic success can provide strategic recommendations for countries aiming to improve their performance.

<!-- b000065 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000066 | prose | pages [3, 4] -->
The distribution of Olympic medals is a key topic of interest for analysts, sports federations, and policymakers. Medal standings reflect national athletic strength, investment in sports development, and strategic resource allocation. This study focuses on developing a predictive model for Olympic medal counts and exploring the underlying factors that influence national m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m performance. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Specifically, our objectives include: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • Developing a mathematical model to predict the number of Gold and total medals for each country in the 2028 Los Angeles Summer Olympics, incorporating factors such as historical performance, host nation advantages, and event distributions.

<!-- b000067 | furniture | pages [3] -->
m

<!-- b000068 | furniture | pages [3] -->
m

<!-- b000069 | furniture | pages [3] -->
m

<!-- b000070 | furniture | pages [3] -->
m

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

<!-- b000391 | furniture | pages [4] -->
Team # 2513314

<!-- b000392 | furniture | pages [4] -->
Page 4 of 22

<!-- b000394 | prose | pages [4] -->
• Estimating the likelihood of countries earning their first Olympic medal and analyzing the probability of new medal-winning nations emerging.

<!-- b000395 | prose | pages [4] -->
• Examining the relationship between specific sports events and national success, identifying key disciplines that contribute significantly to a country’s medal tally.

<!-- b000396 | prose | pages [4] -->
• Investigating the potential impact of elite coaches on national performance, quantifying the "Great Coach" effect, and recommending strategic investments in coaching for selected countries. By addressing these questions, this study aims to provide valuable insights into Olympic medal trends, helping national Olympic committees optimize their training programs and re- source allocation for future competitions.

<!-- b000397 | heading | pages [4] -->
1.3 Our Work

<!-- b000398 | prose | pages [4] -->
Our workflow is illustrated in Figure 2. Before modeling, we first conducted model assump- tions (Section 2) and data exploration (Section 4.2) to facilitate the modeling process. After exploring the data distribution, we identified eight key variables (Section 5.1) and constructed a Bayesian Hierarchical Decision Model (BHDM) (Section 5.2) to better fit our observed distri- butions.

<!-- b000399 | caption | pages [4] -->
Figure 2: Our workflow.

<!-- b000400 | prose | pages [4] -->
A glimpse of dataset

<!-- b000401 | heading | pages [4] -->
Model Assumption

<!-- b000402 | prose | pages [4] -->
Equal Medal Country Distribution Heterogeneity Distribution Some insights about Olympics Medal Counts To: Country Olympic Committees From: Team #2513314 Data: January 27, 2025 Dear Country Olympic Committee leaders:

<!-- b000403 | prose | pages [4] -->
… Overdispersion and Heavy Tails Sum Fixed and Discrete

<!-- b000404 | prose | pages [4] -->
Task 2: Dive Into Great Coach Effect Task 1: Predicting Medals of 2028 LA Olympics

<!-- b000405 | heading | pages [4] -->
BHDM Model Setup

<!-- b000406 | prose | pages [4] -->
Key Variables for Medals Why NOT Other Models? Dataset Coaching Two-phase RF Deep Learning 𝜽𝜽𝒊𝒊= 𝝓𝝓𝒊𝒊𝒆𝒆𝒆𝒆𝒆𝒆𝒙𝒙𝒊𝒊 𝑻𝑻𝜷𝜷𝒊𝒊 𝑿𝑿𝟏𝟏−𝑿𝑿𝟖𝟖 𝜷𝜷𝒊𝒊follows a weakly informative prior

<!-- b000407 | prose | pages [4] -->
Breaking the Ice Probability Posterior Distribution

<!-- b000408 | prose | pages [4] -->
The country that will achieve Important Sports and a Breakthrough From Zero Home Event Impact

<!-- b000409 | heading | pages [4] -->
Sensitivity Analysis

<!-- b000410 | prose | pages [4] -->
All Ability Coach Great Coach Poisson Neg. Binomial 𝑿𝑿𝟗𝟗 Database Predictive Uncertainty and Discrete Outcomes Posterior Summary Our BHDM Model of 𝑿𝑿𝟗𝟗

<!-- b000411 | prose | pages [4] -->
Projects of LA 2028 Japan China United State

<!-- b000412 | prose | pages [4] -->
Task 3: Other Original Insights of BHDM

<!-- b000413 | heading | pages [4] -->
Sensitivity analysis of weak

<!-- b000414 | heading | pages [4] -->
Sensitivity Analysis of Equal

<!-- b000415 | prose | pages [4] -->
Economic level determines medals priors for β

<!-- b000416 | heading | pages [4] -->
Distribution Assumptions

<!-- b000417 | prose | pages [4] -->
Proved to be Great Robustness! Home Turf and Aligned Systems Prevail Emerging Sports Aid Low-GDP Countries

<!-- b000418 | prose | pages [4] -->
During the modeling process, we also considered alternative models; however, they were either inconsistent with the data distribution or incapable of capturing the differences between countries, leading to their exclusion. Using our model, we then projected the medal distribution for the 2028 Los Angeles Olympics along with its 95% prediction interval. Additionally, we analyzed breakthrough probabilities, identified key sports for specific countries, and proposed adjustments to the sports program for the host nation.

<!-- b000419 | prose | pages [4, 5] -->
To investigate the "Great Coach" effect, we first cross-referenced Wikipedia databases with 关注数学模型 our dataset to identify elite coaches. We then quantified each country’s coaching strength and incorporated it as a new variable into our BHDM model. By analyzing the posterior parameters of this variable for three selected countries, we assessed the impact of great coaches on their Olympic performance (Section 6).

<!-- b000420 | furniture | pages [4] -->
2

<!-- b000421 | furniture | pages [4] -->
MATHmodels

<!-- b000422 | furniture | pages [4] -->
获取更多资讯

<!-- b000423 | furniture | pages [5] -->
Team # 2513314

<!-- b000424 | furniture | pages [5] -->
Page 5 of 22

<!-- b000426 | prose | pages [5] -->
Subsequently, we conducted a sensitivity analysis to determine the influence of model parameters and distributional variations on our results, thereby validating the robustness of our model (Section 7). Finally, based on our entire modeling process, we derived three original insights and drafted a letter to the COC to communicate these findings (Section 9).

<!-- b000427 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000428 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000429 | prose | pages [5] -->
To simplify our modeling process, we make the following assumptions:

<!-- b000430 | heading | pages [5] -->
Assumption 1 (Medal Distribution Assumption): The distribution of medal counts to be

<!-- b000431 | prose | pages [5] -->
modeled necessitates integer-valued predictions that sum to a fixed total, often exhibits overdis- persion and heavy tails. This forms our core assumption and directly informs our choice of modeling approach. In Section 4.2, we will validate this assumption through visual analysis.

<!-- b000432 | heading | pages [5] -->
Assumption 2 (Equal Distribution Assumption): The composition and skill levels of athletes

<!-- b000433 | prose | pages [5] -->
representing each country, as well as the events featured in the 2028 Olympics, will be largely consistent with those of the 2024 Paris Olympics. Given the absence of data for the 2028 Games, 微信号：MATHmodels we assume that key factors such as event availability and athlete participation remain comparable to those in 2024. In Section 7.2, we will explore relaxations of this assumption.

<!-- b000434 | heading | pages [5] -->
Assumption 3 (Country Heterogeneity Assumption): Each country excels in different sports

<!-- b000435 | prose | pages [5] -->
and exhibits varying adaptability to the same set of variables, leading to cross-country hetero- geneity. In Section 5.2, we will explore this phenomenon in detail and incorporate it as a key assumption in our modeling approach.

<!-- b000436 | heading | pages [5] -->
3 Notations

<!-- b000437 | caption | pages [5] -->
Table 1: Notations used in the BHDM model and related analyses.

<!-- b000438 | heading | pages [5] -->
Symbol

<!-- b000439 | prose | pages [5] -->
Description 𝑁 Number of countries 𝑇 Total medals across all countries Covariate (feature) vector for country 𝑖 x𝑖 𝝁𝛽 Global mean of coefficient vectors 𝜙𝑖 Concentration parameter for country 𝑖 𝜃𝑖 Latent rate for country 𝑖 𝑋1,𝑖 Historical medal record 𝑋3,𝑖 Host nation flag (binary) 𝑋5,𝑖 Athletics events 𝑋7,𝑖 Ball sports events 𝑋9,𝑖 Great Coach variable (aggregate coaching ability)

<!-- b000440 | heading | pages [5] -->
4 Data Pre-processing

<!-- b000441 | heading | pages [5] -->
Symbol

<!-- b000442 | prose | pages [5] -->
Description 𝑀𝑖 Medal count of country 𝑖 𝑇new Total medals in a future Olympics Random coefficient vector for country 𝑖 𝜷𝑖 Σ𝛽 Covariance matrix (weakly informative prior) 𝛼𝜙, 𝛽𝜙 Hyperparameters for 𝜙𝑖(Gamma distribution) 𝑀𝑖,new Predicted medal count of country 𝑖in future 𝑋2,𝑖 Athlete delegation size 𝑋4,𝑖 Social system congruence (binary) 𝑋6,𝑖 Tactical & strength events 𝑋8,𝑖 Emerging events 𝐺, 𝑆, 𝐵 Gold, silver, and bronze medal counts 𝐴 Coaching ability metric (6G + 3S + B)

<!-- b000443 | prose | pages [5] -->
Before proceeding with modeling, we conducted data cleaning and an initial exploratory m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m analysis to better understand the dataset’s characteristics. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000444 | furniture | pages [5] -->
m

<!-- b000445 | furniture | pages [5] -->
m

<!-- b000446 | furniture | pages [5] -->
m

<!-- b000447 | furniture | pages [5] -->
m

<!-- b000448 | furniture | pages [5] -->
m

<!-- b000449 | furniture | pages [5] -->
m

<!-- b000450 | furniture | pages [5] -->
m

<!-- b000451 | furniture | pages [5] -->
m

<!-- b000452 | furniture | pages [5] -->
m

<!-- b000453 | furniture | pages [5] -->
m

<!-- b000454 | furniture | pages [5] -->
m

<!-- b000455 | furniture | pages [5] -->
m

<!-- b000456 | furniture | pages [5] -->
m

<!-- b000457 | furniture | pages [5] -->
m

<!-- b000458 | furniture | pages [5] -->
m

<!-- b000459 | furniture | pages [5] -->
m

<!-- b000460 | furniture | pages [5] -->
m

<!-- b000461 | furniture | pages [5] -->
m

<!-- b000462 | furniture | pages [5] -->
m

<!-- b000463 | furniture | pages [5] -->
m

<!-- b000464 | furniture | pages [5] -->
m

<!-- b000465 | furniture | pages [5] -->
m

<!-- b000466 | furniture | pages [5] -->
m

<!-- b000467 | furniture | pages [5] -->
m

<!-- b000468 | furniture | pages [5] -->
m

<!-- b000469 | furniture | pages [5] -->
m

<!-- b000470 | furniture | pages [5] -->
m

<!-- b000471 | furniture | pages [5] -->
m

<!-- b000472 | furniture | pages [5] -->
m

<!-- b000473 | furniture | pages [5] -->
m

<!-- b000474 | furniture | pages [5] -->
m

<!-- b000475 | furniture | pages [5] -->
m

<!-- b000476 | furniture | pages [5] -->
m

<!-- b000477 | furniture | pages [5] -->
m

<!-- b000478 | furniture | pages [5] -->
m

<!-- b000479 | furniture | pages [5] -->
m

<!-- b000480 | furniture | pages [5] -->
m

<!-- b000481 | furniture | pages [5] -->
m

<!-- b000482 | furniture | pages [5] -->
m

<!-- b000483 | furniture | pages [5] -->
m

<!-- b000484 | furniture | pages [5] -->
m

<!-- b000485 | furniture | pages [5] -->
m

<!-- b000486 | furniture | pages [5] -->
m

<!-- b000487 | furniture | pages [5] -->
m

<!-- b000488 | furniture | pages [5] -->
m

<!-- b000489 | furniture | pages [5] -->
m

<!-- b000490 | furniture | pages [5] -->
m

<!-- b000491 | furniture | pages [5] -->
m

<!-- b000492 | furniture | pages [5] -->
m

<!-- b000493 | furniture | pages [5] -->
m

<!-- b000494 | furniture | pages [5] -->
m

<!-- b000495 | furniture | pages [5] -->
m

<!-- b000496 | furniture | pages [5] -->
m

<!-- b000497 | furniture | pages [5] -->
m

<!-- b000498 | furniture | pages [5] -->
m

<!-- b000499 | furniture | pages [5] -->
m

<!-- b000500 | furniture | pages [5] -->
m

<!-- b000501 | furniture | pages [5] -->
m

<!-- b000502 | furniture | pages [5] -->
m

<!-- b000503 | furniture | pages [5] -->
m

<!-- b000504 | furniture | pages [5] -->
m

<!-- b000505 | furniture | pages [5] -->
m

<!-- b000506 | furniture | pages [5] -->
m

<!-- b000507 | furniture | pages [5] -->
m

<!-- b000508 | furniture | pages [5] -->
m

<!-- b000509 | furniture | pages [5] -->
m

<!-- b000510 | furniture | pages [5] -->
m

<!-- b000511 | furniture | pages [5] -->
m

<!-- b000512 | furniture | pages [5] -->
m

<!-- b000513 | furniture | pages [5] -->
m

<!-- b000514 | furniture | pages [5] -->
m

<!-- b000515 | furniture | pages [5] -->
m

<!-- b000516 | furniture | pages [5] -->
m

<!-- b000517 | furniture | pages [5] -->
m

<!-- b000518 | furniture | pages [5] -->
m

<!-- b000519 | furniture | pages [5] -->
m

<!-- b000520 | furniture | pages [5] -->
m

<!-- b000521 | furniture | pages [5] -->
m

<!-- b000522 | furniture | pages [5] -->
m

<!-- b000523 | furniture | pages [5] -->
m

<!-- b000524 | furniture | pages [5] -->
m

<!-- b000525 | furniture | pages [5] -->
m

<!-- b000526 | furniture | pages [5] -->
m

<!-- b000527 | furniture | pages [5] -->
m

<!-- b000528 | furniture | pages [5] -->
m

<!-- b000529 | furniture | pages [5] -->
m

<!-- b000530 | furniture | pages [5] -->
m

<!-- b000531 | furniture | pages [5] -->
m

<!-- b000532 | furniture | pages [5] -->
m

<!-- b000533 | furniture | pages [5] -->
m

<!-- b000534 | furniture | pages [5] -->
m

<!-- b000535 | furniture | pages [5] -->
m

<!-- b000536 | furniture | pages [5] -->
m

<!-- b000537 | furniture | pages [5] -->
m

<!-- b000538 | furniture | pages [5] -->
m

<!-- b000539 | furniture | pages [5] -->
m

<!-- b000540 | furniture | pages [5] -->
m

<!-- b000541 | furniture | pages [5] -->
m

<!-- b000542 | furniture | pages [5] -->
m

<!-- b000543 | furniture | pages [5] -->
m

<!-- b000544 | furniture | pages [5] -->
m

<!-- b000545 | furniture | pages [5] -->
m

<!-- b000546 | furniture | pages [5] -->
m

<!-- b000547 | furniture | pages [5] -->
m

<!-- b000548 | furniture | pages [5] -->
m

<!-- b000549 | furniture | pages [5] -->
m

<!-- b000550 | furniture | pages [5] -->
m

<!-- b000551 | furniture | pages [5] -->
m

<!-- b000552 | furniture | pages [5] -->
m

<!-- b000553 | furniture | pages [5] -->
m

<!-- b000554 | furniture | pages [5] -->
m

<!-- b000555 | furniture | pages [5] -->
m

<!-- b000556 | furniture | pages [5] -->
m

<!-- b000557 | furniture | pages [5] -->
m

<!-- b000558 | furniture | pages [5] -->
m

<!-- b000559 | furniture | pages [5] -->
m

<!-- b000560 | furniture | pages [5] -->
m

<!-- b000561 | furniture | pages [5] -->
m

<!-- b000562 | furniture | pages [5] -->
m

<!-- b000563 | furniture | pages [5] -->
m

<!-- b000564 | furniture | pages [5] -->
m

<!-- b000565 | furniture | pages [5] -->
m

<!-- b000566 | furniture | pages [5] -->
m

<!-- b000567 | furniture | pages [5] -->
m

<!-- b000568 | furniture | pages [5] -->
m

<!-- b000569 | furniture | pages [5] -->
m

<!-- b000570 | furniture | pages [5] -->
m

<!-- b000571 | furniture | pages [5] -->
m

<!-- b000572 | furniture | pages [5] -->
m

<!-- b000573 | furniture | pages [5] -->
m

<!-- b000574 | furniture | pages [5] -->
m

<!-- b000575 | furniture | pages [5] -->
m

<!-- b000576 | furniture | pages [5] -->
m

<!-- b000577 | furniture | pages [5] -->
m

<!-- b000578 | furniture | pages [5] -->
m

<!-- b000579 | furniture | pages [5] -->
m

<!-- b000580 | furniture | pages [5] -->
m

<!-- b000581 | furniture | pages [5] -->
m

<!-- b000582 | furniture | pages [5] -->
m

<!-- b000583 | furniture | pages [5] -->
m

<!-- b000584 | furniture | pages [5] -->
m

<!-- b000585 | furniture | pages [5] -->
m

<!-- b000586 | furniture | pages [5] -->
m

<!-- b000587 | furniture | pages [5] -->
m

<!-- b000588 | furniture | pages [5] -->
m

<!-- b000589 | furniture | pages [5] -->
m

<!-- b000590 | furniture | pages [5] -->
m

<!-- b000591 | furniture | pages [5] -->
m

<!-- b000592 | furniture | pages [5] -->
m

<!-- b000593 | furniture | pages [5] -->
m

<!-- b000594 | furniture | pages [5] -->
m

<!-- b000595 | furniture | pages [5] -->
m

<!-- b000596 | furniture | pages [5] -->
m

<!-- b000597 | furniture | pages [5] -->
m

<!-- b000598 | furniture | pages [5] -->
m

<!-- b000599 | furniture | pages [5] -->
m

<!-- b000600 | furniture | pages [5] -->
m

<!-- b000601 | furniture | pages [5] -->
m

<!-- b000602 | furniture | pages [5] -->
m

<!-- b000603 | furniture | pages [5] -->
m

<!-- b000604 | furniture | pages [5] -->
m

<!-- b000605 | furniture | pages [5] -->
m

<!-- b000606 | furniture | pages [5] -->
m

<!-- b000607 | furniture | pages [5] -->
m

<!-- b000608 | furniture | pages [5] -->
m

<!-- b000609 | furniture | pages [5] -->
m

<!-- b000610 | furniture | pages [5] -->
m

<!-- b000611 | furniture | pages [5] -->
m

<!-- b000612 | furniture | pages [5] -->
m

<!-- b000613 | furniture | pages [5] -->
m

<!-- b000614 | furniture | pages [5] -->
m

<!-- b000615 | furniture | pages [5] -->
m

<!-- b000616 | furniture | pages [5] -->
m

<!-- b000617 | furniture | pages [5] -->
m

<!-- b000618 | furniture | pages [5] -->
m

<!-- b000619 | furniture | pages [5] -->
m

<!-- b000620 | furniture | pages [5] -->
m

<!-- b000621 | furniture | pages [5] -->
m

<!-- b000622 | furniture | pages [5] -->
m

<!-- b000623 | furniture | pages [5] -->
m

<!-- b000624 | furniture | pages [5] -->
m

<!-- b000625 | furniture | pages [5] -->
m

<!-- b000626 | furniture | pages [5] -->
m

<!-- b000627 | furniture | pages [5] -->
m

<!-- b000628 | furniture | pages [5] -->
m

<!-- b000629 | furniture | pages [5] -->
m

<!-- b000630 | furniture | pages [5] -->
m

<!-- b000631 | furniture | pages [5] -->
m

<!-- b000632 | furniture | pages [5] -->
m

<!-- b000633 | furniture | pages [5] -->
m

<!-- b000634 | furniture | pages [5] -->
m

<!-- b000635 | furniture | pages [5] -->
m

<!-- b000636 | furniture | pages [5] -->
m

<!-- b000637 | furniture | pages [5] -->
m

<!-- b000638 | furniture | pages [5] -->
m

<!-- b000639 | furniture | pages [5] -->
m

<!-- b000640 | furniture | pages [5] -->
m

<!-- b000641 | furniture | pages [5] -->
m

<!-- b000642 | furniture | pages [5] -->
m

<!-- b000643 | furniture | pages [5] -->
m

<!-- b000644 | furniture | pages [5] -->
m

<!-- b000645 | furniture | pages [5] -->
m

<!-- b000646 | furniture | pages [5] -->
m

<!-- b000647 | furniture | pages [5] -->
m

<!-- b000648 | furniture | pages [5] -->
m

<!-- b000649 | furniture | pages [5] -->
m

<!-- b000650 | furniture | pages [5] -->
m

<!-- b000651 | furniture | pages [5] -->
m

<!-- b000652 | furniture | pages [5] -->
m

<!-- b000653 | furniture | pages [5] -->
m

<!-- b000654 | furniture | pages [5] -->
m

<!-- b000655 | furniture | pages [5] -->
m

<!-- b000656 | furniture | pages [5] -->
m

<!-- b000657 | furniture | pages [5] -->
m

<!-- b000658 | furniture | pages [5] -->
m

<!-- b000659 | furniture | pages [5] -->
m

<!-- b000660 | furniture | pages [5] -->
m

<!-- b000661 | furniture | pages [5] -->
m

<!-- b000662 | furniture | pages [5] -->
m

<!-- b000663 | furniture | pages [5] -->
m

<!-- b000664 | furniture | pages [5] -->
m

<!-- b000665 | furniture | pages [5] -->
m

<!-- b000666 | furniture | pages [5] -->
m

<!-- b000667 | furniture | pages [5] -->
m

<!-- b000668 | furniture | pages [5] -->
m

<!-- b000669 | furniture | pages [5] -->
m

<!-- b000670 | furniture | pages [5] -->
m

<!-- b000671 | furniture | pages [5] -->
m

<!-- b000672 | furniture | pages [5] -->
m

<!-- b000673 | furniture | pages [5] -->
m

<!-- b000674 | furniture | pages [5] -->
m

<!-- b000675 | furniture | pages [5] -->
m

<!-- b000676 | furniture | pages [5] -->
m

<!-- b000677 | furniture | pages [5] -->
m

<!-- b000678 | furniture | pages [5] -->
m

<!-- b000679 | furniture | pages [5] -->
m

<!-- b000680 | furniture | pages [5] -->
m

<!-- b000681 | furniture | pages [5] -->
m

<!-- b000682 | furniture | pages [5] -->
m

<!-- b000683 | furniture | pages [5] -->
m

<!-- b000684 | furniture | pages [5] -->
m

<!-- b000685 | furniture | pages [5] -->
m

<!-- b000686 | furniture | pages [5] -->
m

<!-- b000687 | furniture | pages [5] -->
m

<!-- b000688 | furniture | pages [5] -->
m

<!-- b000689 | furniture | pages [5] -->
m

<!-- b000690 | furniture | pages [5] -->
m

<!-- b000691 | furniture | pages [5] -->
m

<!-- b000692 | furniture | pages [5] -->
m

<!-- b000693 | furniture | pages [5] -->
m

<!-- b000694 | furniture | pages [5] -->
m

<!-- b000695 | furniture | pages [5] -->
m

<!-- b000696 | furniture | pages [5] -->
m

<!-- b000697 | furniture | pages [5] -->
m

<!-- b000698 | furniture | pages [5] -->
m

<!-- b000699 | furniture | pages [5] -->
m

<!-- b000700 | furniture | pages [5] -->
m

<!-- b000701 | furniture | pages [5] -->
m

<!-- b000702 | furniture | pages [5] -->
m

<!-- b000703 | furniture | pages [5] -->
m

<!-- b000704 | furniture | pages [5] -->
m

<!-- b000705 | furniture | pages [5] -->
m

<!-- b000706 | furniture | pages [5] -->
m

<!-- b000707 | furniture | pages [5] -->
m

<!-- b000708 | furniture | pages [5] -->
m

<!-- b000709 | furniture | pages [5] -->
m

<!-- b000710 | furniture | pages [5] -->
m

<!-- b000711 | furniture | pages [5] -->
m

<!-- b000712 | furniture | pages [5] -->
m

<!-- b000713 | furniture | pages [5] -->
m

<!-- b000714 | furniture | pages [5] -->
m

<!-- b000715 | furniture | pages [5] -->
m

<!-- b000716 | furniture | pages [5] -->
m

<!-- b000717 | furniture | pages [5] -->
m

<!-- b000718 | furniture | pages [5] -->
m

<!-- b000719 | furniture | pages [5] -->
m

<!-- b000720 | furniture | pages [5] -->
m

<!-- b000721 | furniture | pages [5] -->
m

<!-- b000722 | furniture | pages [5] -->
m

<!-- b000723 | furniture | pages [5] -->
m

<!-- b000724 | furniture | pages [5] -->
m

<!-- b000725 | furniture | pages [5] -->
m

<!-- b000726 | furniture | pages [5] -->
m

<!-- b000727 | furniture | pages [5] -->
m

<!-- b000728 | furniture | pages [5] -->
m

<!-- b000729 | furniture | pages [5] -->
m

<!-- b000730 | furniture | pages [5] -->
m

<!-- b000731 | furniture | pages [5] -->
m

<!-- b000732 | furniture | pages [5] -->
m

<!-- b000733 | furniture | pages [5] -->
m

<!-- b000734 | furniture | pages [5] -->
m

<!-- b000735 | furniture | pages [5] -->
m

<!-- b000736 | furniture | pages [5] -->
m

<!-- b000737 | furniture | pages [5] -->
m

<!-- b000738 | furniture | pages [5] -->
m

<!-- b000739 | furniture | pages [5] -->
m

<!-- b000740 | furniture | pages [5] -->
m

<!-- b000741 | furniture | pages [5] -->
m

<!-- b000742 | furniture | pages [5] -->
m

<!-- b000743 | furniture | pages [5] -->
m

<!-- b000744 | furniture | pages [5] -->
m

<!-- b000745 | furniture | pages [5] -->
m

<!-- b000746 | furniture | pages [5] -->
m

<!-- b000747 | furniture | pages [5] -->
m

<!-- b000748 | furniture | pages [5] -->
m

<!-- b000749 | furniture | pages [5] -->
m

<!-- b000750 | furniture | pages [5] -->
m

<!-- b000751 | furniture | pages [5] -->
m

<!-- b000752 | furniture | pages [5] -->
m

<!-- b000753 | furniture | pages [5] -->
m

<!-- b000754 | furniture | pages [5] -->
m

<!-- b000755 | furniture | pages [5] -->
m

<!-- b000756 | furniture | pages [5] -->
m

<!-- b000757 | furniture | pages [5] -->
m

<!-- b000758 | furniture | pages [5] -->
m

<!-- b000759 | furniture | pages [5] -->
m

<!-- b000760 | furniture | pages [5] -->
m

<!-- b000761 | furniture | pages [5] -->
m

<!-- b000762 | furniture | pages [5] -->
m

<!-- b000763 | furniture | pages [5] -->
m

<!-- b000764 | furniture | pages [5] -->
m

<!-- b000765 | furniture | pages [5] -->
m

<!-- b000766 | furniture | pages [5] -->
m

<!-- b000767 | furniture | pages [5] -->
m

<!-- b000768 | furniture | pages [6] -->
Page 6 of 22

<!-- b000769 | furniture | pages [6] -->
Team # 2513314

<!-- b000770 | heading | pages [6] -->
4.1 Data Cleaning

<!-- b000771 | prose | pages [6] -->
Upon inspection, we identified missing values in the summer0ly_programs . csv file. These gaps resulted from certain events not being held in specific years, leading to the absence of corresponding records. To address this issue, we replaced the missing values with 0.

<!-- b000772 | prose | pages [6] -->
Additionally, inconsistencies were found in the representation of country codes (NOC) across the four datasets: summerOly_programs.csv, summerOly_hosts.csv, summerOly_medal_counts.csv, and summerOly_athletes.csv. To standardize these variations, we converted all country codes into a unified three-letter format. However, for clarity and readability, country names are used instead of three-letter codes in all subsequent discussions within this paper.

<!-- b000773 | prose | pages [6] -->
Furthermore, we identified newly established countries as well as temporary representative teams, such as the Refugee Olympic Team. Since these entities lack historical records, all their past data were initialized with 0 to maintain consistency across the dataset. However, an exception was made for Russia, as its NOC was updated to ROC in 2020. In this case, historical data associated with Russia were retained to reflect its prior participation accurately.

<!-- b000774 | heading | pages [6] -->
4.2 A glimpse of dataset

<!-- b000775 | prose | pages [6] -->
Understanding the distribution patterns of gold medals and total medals is essential, as it directly impacts the selection of appropriate modeling strategies for further analysis. To illustrate this, Figure 3 presents the country-level distributions of gold and total medals of Olympics history. Notably, these distributions demonstrate clear signs of overdispersion and heavy tails, which stem from the inherently discrete nature of medal counts and the constraint of a fixed total sum.

<!-- b000776 | caption | pages [6] -->
Figure 3: Total Medal and Gold Medal Distribution of Olympics History.

<!-- b000777 | prose | pages [6] -->
Distribution of Total Medals and Gold Medals by Country 2500- Total Medals Number of Medals Gold Medals 2000-

<!-- b000778 | prose | pages [6] -->
1500

<!-- b000779 | prose | pages [6] -->
1000

<!-- b000780 | prose | pages [6] -->
500

<!-- b000781 | prose | pages [6] -->
0 Kecnya Nena d a ro Franoce Vusvia Norhk orea aand Pueo Rco [ ku n Boha E8pt Senoal Norccda onia United States HuBmry East Germany South Korea Souh iicea Czech Republic Iindocssa Cllia ESstnia Irdera Framnc Taisn KoOSOV Sneorc Cenada ordan plidues Enntea pemumy Ceylon Coatina Poftual Lavia Dominican Republic Denmark Kyrgyzstan l Baelain Aqetiina Iceland Zaqia Kuwt Cypus Nier Almnia Yyuosvava vn Vin nds poruuadl Lwwn and Switzerland Spain Braz[ Ukraine Tley Mexico Polaod 即 Sai oia Lvia Guyana roomosa [laly Cda

<!-- b000782 | prose | pages [6] -->
Country (NOC)

<!-- b000783 | prose | pages [6] -->
Task 1: Predicting Medals of 2028 LA Olympics 5

<!-- b000784 | heading | pages [6] -->
5.1 Key Variables Influencing Olympic Medal Success

<!-- b000785 | prose | pages [6] -->
Building upon insights presented by Schlembach et al. [7], it becomes evident that a nation's ability to secure Olympic medals stems from an interplay of diverse yet interlinked factors. In the following, we examine three pivotal dimensions—economic capacity, hosting advantages, and event-specific attributes—and introduce key explanatory variables associated witheachdomain!

<!-- b000786 | prose | pages [6] -->
关注数学模型

<!-- b000787 | furniture | pages [6] -->
获取更多资讯

<!-- b000788 | furniture | pages [7] -->
Team # 2513314

<!-- b000789 | furniture | pages [7] -->
Page 7 of 22

<!-- b000790 | heading | pages [7] -->
1. Economic Capacity.

<!-- b000791 | prose | pages [7] -->
Historical Medal Record (𝑋1): Reflects a country’s medal haul in the immediately preceding Olympic cycle (for gold-medal-focused forecasts, this specifically denotes the previous count of gold medals). A strong performance history is frequently underpinned by 微信公众号：数学模型 consistent investment in athletic programs and robust training infrastructures.

<!-- b000792 | prose | pages [7] -->
Athlete Delegation Size (𝑋2): Represents the total number of athletes sent to the current Games, serving as a proxy measure of institutional support and the breadth of a na- tion’s talent pool. Larger delegations often correlate with stronger financial backing and more extensive development pathways in multiple sporting disciplines.

<!-- b000793 | heading | pages [7] -->
2. Hosting Advantages.

<!-- b000794 | prose | pages [7] -->
Host Nation Flag (𝑋3 ∈{0, 1}): Indicates whether a nation is the host (𝑋3 = 1). Host countries frequently capitalize on superior familiarity with the local environment, elevated fan 微信号：MATHmodels support, and logistical conveniences.

<!-- b000795 | prose | pages [7] -->
Social System Congruence (𝑋4 ∈{0, 1}): Identifies nations whose social or institutional struc- tures are closely aligned with those of the host (𝑋4 = 1). Such alignment can minimize cultural barriers and facilitate smoother acclimatization, indirectly bolstering athletic per- formance.

<!-- b000796 | heading | pages [7] -->
3. Event-Specific Attributes.

<!-- b000797 | prose | pages [7] -->
Substantial heterogeneity exists across Olympic events, with certain countries historically excelling in specific domains. Cultural traditions, regional training practices, and even genetic predispositions can foster a competitive edge in certain sports [6]. To capture this diversity, we classify events into four key segments:

<!-- b000798 | prose | pages [7] -->
Athletics Events (𝑋5): Comprising all track and field competitions, a domain frequently marked by widespread global participation and prominent displays of speed, endurance, and agility.

<!-- b000799 | heading | pages [7] -->
Tactical & Strength Events (𝑋6): Encompassessportssuchasfencing, racquetsports, wrestling,

<!-- b000800 | prose | pages [7] -->
and weightlifting, where strategic thinking, technical skills, and physical power play in- terdependent roles.

<!-- b000801 | prose | pages [7] -->
Ball Sports Events (𝑋7): Encompassing team-focused competitions including football, bas- ketball, and volleyball, these events rely heavily on synergy among participants and well-established support systems.

<!-- b000802 | prose | pages [7] -->
Emerging Events (𝑋8): NewlyintroduceddisciplinesorcontestsdebutinginthecurrentOlympic cycle. Nations pioneering these events may enjoy early-adopter advantages but also face higher uncertainty due to the limited availability of historical data.

<!-- b000803 | prose | pages [7] -->
Overall, these variables not only serve as potential predictors in quantitative analyses but also offer a structured lens for examining how resources, environmental factors, and sport-specific nuances collectively shape a nation’s Olympic performance.

<!-- b000804 | heading | pages [7] -->
5.2 Bayesian Hierarchical Dirichlet–Multinomial (BHDM) Model

<!-- b000805 | prose | pages [7, 8] -->
Section 4.2 reveals that Olympic medal data typically demand integer-valued predictions that sum to a known total, often exhibit overdispersion and heavy tails, and require partial pooling m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to handle cross-country heterogeneity. Under this distributional constraint, deep learning and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m machine learning methods (e.g., RNN and two-stage RF) are clearly unsuitable, as they fail m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to enforce the fixed-total and discrete conditions without special modifications. Statistical approaches such as Negative Binomial and Poisson are also inadequate due to their poor handling of long-tailed data. While a standard Bayesian Multinomial Model can effectively model such data, it does not satisfy our Country Heterogeneity Assumption, as it assumes a shared 𝜷across all countries, which is incompatible with our framework. The Bayesian Hierarchical Dirichlet–Multinomial (BHDM) model addresses these challenges by combining a Dirichlet–Multinomial likelihood, which enforces both discreteness and sum constraints, with hierarchical priors on regression parameters, enabling each country to have its own coefficient vector.  be the observed medal Model Setup. Let 𝑁be the number of countries, and let  𝑀1, . . . , 𝑀𝑁 counts, with the total 𝑁 ∑︁ 𝑇= 𝑀𝑖. (1) 𝑖=1 For each country 𝑖, we define a covariate vector x𝑖and a random coefficient vector 𝜷𝑖. In our setting, we adopt a weakly informative prior for 𝜷𝑖, specifically assuming that

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

<!-- b001070 | furniture | pages [7] -->
m

<!-- b001071 | furniture | pages [7] -->
m

<!-- b001072 | furniture | pages [7] -->
m

<!-- b001073 | furniture | pages [7] -->
m

<!-- b001074 | furniture | pages [7] -->
m

<!-- b001075 | furniture | pages [7] -->
m

<!-- b001076 | furniture | pages [7] -->
m

<!-- b001077 | furniture | pages [7] -->
m

<!-- b001078 | furniture | pages [7] -->
m

<!-- b001079 | furniture | pages [7] -->
m

<!-- b001080 | furniture | pages [7] -->
m

<!-- b001081 | furniture | pages [7] -->
m

<!-- b001082 | furniture | pages [7] -->
m

<!-- b001083 | furniture | pages [7] -->
m

<!-- b001084 | furniture | pages [7] -->
m

<!-- b001085 | furniture | pages [7] -->
m

<!-- b001086 | furniture | pages [7] -->
m

<!-- b001087 | furniture | pages [7] -->
m

<!-- b001088 | furniture | pages [7] -->
m

<!-- b001089 | furniture | pages [7] -->
m

<!-- b001090 | furniture | pages [7] -->
m

<!-- b001091 | furniture | pages [7] -->
m

<!-- b001092 | furniture | pages [7] -->
m

<!-- b001093 | furniture | pages [7] -->
m

<!-- b001094 | furniture | pages [7] -->
m

<!-- b001095 | furniture | pages [7] -->
m

<!-- b001096 | furniture | pages [7] -->
m

<!-- b001097 | furniture | pages [7] -->
m

<!-- b001098 | furniture | pages [7] -->
m

<!-- b001099 | furniture | pages [7] -->
m

<!-- b001100 | furniture | pages [7] -->
m

<!-- b001101 | furniture | pages [7] -->
m

<!-- b001102 | furniture | pages [7] -->
m

<!-- b001103 | furniture | pages [7] -->
m

<!-- b001104 | furniture | pages [7] -->
m

<!-- b001105 | furniture | pages [7] -->
m

<!-- b001106 | furniture | pages [7] -->
m

<!-- b001107 | furniture | pages [7] -->
m

<!-- b001108 | furniture | pages [7] -->
m

<!-- b001109 | furniture | pages [7] -->
m

<!-- b001110 | furniture | pages [7] -->
m

<!-- b001111 | furniture | pages [7] -->
m

<!-- b001112 | furniture | pages [7] -->
m

<!-- b001113 | furniture | pages [7] -->
m

<!-- b001114 | furniture | pages [7] -->
m

<!-- b001115 | furniture | pages [7] -->
m

<!-- b001116 | furniture | pages [7] -->
m

<!-- b001117 | furniture | pages [7] -->
m

<!-- b001118 | furniture | pages [7] -->
m

<!-- b001119 | furniture | pages [7] -->
m

<!-- b001120 | furniture | pages [7] -->
m

<!-- b001121 | furniture | pages [7] -->
m

<!-- b001122 | furniture | pages [7] -->
m

<!-- b001123 | furniture | pages [7] -->
m

<!-- b001124 | furniture | pages [7] -->
m

<!-- b001125 | furniture | pages [7] -->
m

<!-- b001126 | furniture | pages [7] -->
m

<!-- b001127 | furniture | pages [7] -->
m

<!-- b001128 | furniture | pages [7] -->
m

<!-- b001129 | furniture | pages [7] -->
m

<!-- b001130 | furniture | pages [8] -->
Team # 2513314

<!-- b001131 | furniture | pages [8] -->
Page 8 of 22

<!-- b001133 | prose | pages [8] -->
  𝝁𝛽, Σ𝛽 , 𝑖= 1, . . . , 𝑁, 𝜷𝑖∼N (2)

<!-- b001134 | prose | pages [8] -->
with 𝜏2 = 1. Σ𝛽= 𝜏2𝐼𝑝 and

<!-- b001135 | prose | pages [8] -->
This choice reflects our prior belief that, while allowing for moderate variation in the regression coefficients across countries, the individual effects should not be overly dispersed. The weakly informative prior thus provides regularization without imposing overly restrictive assumptions, enabling the data to primarily inform the posterior inferences. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We additionally introduce a concentration parameter 𝜙𝑖for country 𝑖: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝜙𝑖∼Gamma(𝛼𝜙, 𝛽𝜙). m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (3) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Each country 𝑖has an associated feature vector m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001136 | prose | pages [8] -->
⊤, x𝑖=  𝑋1,𝑖, 𝑋2,𝑖, 𝑋3,𝑖, 𝑋4,𝑖, 𝑋5,𝑖, 𝑋6,𝑖, 𝑋7,𝑖, 𝑋8,𝑖 (4)

<!-- b001137 | prose | pages [8] -->
Combining these, each country’s latent rate is

<!-- b001138 | prose | pages [8] -->
  x⊤ 𝜃𝑖= 𝜙𝑖exp . 𝑖𝜷𝑖 (5)

<!-- b001139 | prose | pages [8] -->
 follows a Dirichlet–Multinomial distribution: Conditioned on {𝜃𝑖}, the vector  𝑀1, . . . , 𝑀𝑁  ∼Dirichlet-Multinomial 𝑇; 𝜃1, . . . , 𝜃𝑁  𝑀1, . . . , 𝑀𝑁 , (6)

<!-- b001140 | prose | pages [8] -->
ensuring each 𝑀𝑖is integer-valued and that Í𝑁 𝑖=1 𝑀𝑖= 𝑇. Let M = (𝑀1, . . . , 𝑀𝑁) and recall 𝜃𝑖as in (5). Posterior Distribution. Combining the likelihood Eq. (6) with hierarchical priors leads to

<!-- b001141 | prose | pages [8] -->
M 𝑝 {𝜷𝑖}, {𝜙𝑖}, 𝝁𝛽, Σ𝛽 𝑁   h i Ö M; 𝜃1, . . . , 𝜃𝑁 N  𝜷𝑖; 𝝁𝛽, Σ𝛽 ∝Dirichlet-Multinomial × × (7) 𝑖=1 𝑁 h i Ö Gamma 𝜙𝑖; 𝛼𝜙, 𝛽𝜙 × 𝑝(𝝁𝛽, Σ𝛽) · · · 关注数学模型

<!-- b001142 | furniture | pages [8] -->
2

<!-- b001143 | prose | pages [8, 9] -->
𝑖=1 where p(μβ, Σβ) is a suitable hyperprior (e.g. Normal-Inverse-Wishart). One can sample from this posterior distribution via Markov chain Monte Carlo or other approximate methods, capturing both cross-country partial pooling (through {β}) and overdispersion (through {φ}). Predictive Uncertainty and Discrete Outcomes. For a future Olympics with Tnew total medals, each posterior sample ({β(s)}, {φ(s) }) implies 2. exp(xT β(s), (8)

<!-- b001144 | furniture | pages [8] -->
MATHmodels

<!-- b001145 | furniture | pages [8] -->
获取更多资讯

<!-- b001146 | furniture | pages [9] -->
Team # 2513314

<!-- b001147 | furniture | pages [9] -->
Page 9 of 22

<!-- b001149 | prose | pages [9] -->
and yields a random draw from

<!-- b001150 | prose | pages [9] -->
(9) N,new) Because the Dirichlet-Multinomial distribution produces a vector of nonnegative integers sum- ming to Tnew, it preserves discrete counts exactly. Across many posterior samples s = 1, . . . , S, this process captures parameter uncertainty (variation in {β, φ}) and the inherent multinomial- like randomness of allocating Tnew medals among N countries. In practice, one may form 95% credible intervals from these sampled outcomes to measure the plausible range of medals for ● each country. Breaking the Ice Probability. Suppose a country i historically has zero medals. To evaluate its likelihood of winning at least one medal in the upcoming Olympics, note that each simulated (s) outcome M i,new approximate the probability of “ice-breaking" as

<!-- b001151 | prose | pages [9] -->
S 1 Pr(Mi,new > 0) = (10) s=1 This metric naturally integrates both variability in country-specific parameters and the stochastic nature of discrete medal assignments.

<!-- b001152 | prose | pages [9] -->
4N,new), we can (s) compute summary statistics such as posterior means, medians, and credible intervals at any desired confidence level (commonly 95%). A 95% credible interval [li, u] for the medal count of country i is obtained by taking the 2.5th and 97.5th percentiles of { Ms }s one can compute probabilities of surpassing a historical record or of achieving a threshold medal count. These credible intervals differ from classical “frequentist prediction intervals" but serve a similar interpretive purpose within the Bayesian framework, reflecting the distribution of plausible future outcomes under the inferred BHDM. Interpreting Regression Coefficients. Because Bayesian estimation provides posterior draws for each βi,j, one can directly compute several summary measures from these samples. First, the posterior mean β,j offers a central estimate of the effect size for covariate j on country i’s log-rate of medal acquisition. Next, the posterior standard deviation StdDev(βi,j) characterizes uncertainty around this mean. One may also calculate the posterior probability that βi,j exceeds zero, denoted Pr(βi,j > 0), which reveals how likely it is that increasing covariate j has a positive effect on the country's medal prospects. Finally, a 95% credible interval [Li,j, Ui,j] is often derived by taking the 2.5th and 97.5th percentiles of the posterior draws of βi,j. This interval indicates the range of coefficient values most consistent with the observed data, under the hierarchical model. A positive βi,j (as signaled by its posterior mean and credible interval lying mainly above zero) suggests that raising covariate j increases the country's rate of medal accumulation, whereas a negative value implies the opposite. Because of the partial pooling in the hierarchical structure, extreme estimates for small or emerging countries are naturally shrunk toward a global mean, reducing the risk of overfitting and providing robust inferences about which predictors most influence medal outcomes.

<!-- b001153 | furniture | pages [10] -->
Team # 2513314

<!-- b001154 | furniture | pages [10] -->
Page 10 of 22

<!-- b001155 | heading | pages [10] -->
5.3 Projects of LA 2028

<!-- b001156 | prose | pages [10] -->
By the Equal Distribution Assumption, we use the 2024 data as a proxy for 2028, modifying only the host country. The features are then incorporated into our model and compared against other approaches, with results presented in Table 2. As shown in Table 2, our proposed BHDM model outperforms both the machine/deep learning and traditional statistical approaches in predicting medal counts. For instance, in the All Medals category, BHDM achieves an MSE of 6.98 and an 𝑅2 of 0.85, which are notably superior to the corresponding values from the competing models that exhibit higher errors and lower fit indices. Similarly, in the Gold Medals category, BHDM records an MSE of 3.42 and an 𝑅2 of 0.80, outperforming alternative models by a substantial margin. These improvements are primarily attributable to the BHDM model’s adaptive capability in capturing the underlying data distribution, thereby effectively modeling the intrinsic variability and complex relationships in the dataset, which in turn results in more accurate predictions.

<!-- b001157 | caption | pages [10] -->
Table 2: Comparison of Model Performance Metrics for Medal Prediction. Lower values for MSE,

<!-- b001158 | prose | pages [10] -->
RMSE, and MAE indicate better performance, while higher values for 𝑅2 and Adjusted 𝑅2 indicate a better model fit. The best performance for each metric is highlighted in bold.

<!-- b001159 | prose | pages [10] -->
Machine/Deep Learning Models Statistical Models

<!-- b001160 | prose | pages [10] -->
Medal Type Metric XGBoost[1] RNN[3] RF Two-stage[5] Poisson Neg. Binomial BHDM (ours)

<!-- b001161 | prose | pages [10] -->
6.98 MSE 7.21 7.05 7.37 10.45 10.33 RMSE 2.72 2.65 2.78 3.21 3.15 2.59 All Medals MAE 1.15 1.12 1.17 1.58 1.52 1.03 𝑅2 0.85 0.84 0.83 0.77 0.71 0.74 Adjusted 𝑅2 0.84 0.82 0.78 0.74 0.68 0.69

<!-- b001162 | prose | pages [10] -->
MSE 3.71 3.63 3.82 5.25 5.12 3.42 RMSE 1.93 1.91 1.95 2.29 2.26 1.86 Gold Medals 0.95 MAE 1.03 0.99 1.04 1.23 1.25 𝑅2 0.80 0.76 0.79 0.71 0.66 0.71 Adjusted 𝑅2 0.78 0.74 0.75 0.68 0.62 0.69

<!-- b001163 | prose | pages [10] -->
Based on our Bayesian hierarchical model, our projections for the Los Angeles 2028 Olympic medal table is shown in Figure 4. It suggests that the United States will significantly improve its performance with a predicted total of 146 medals (95% CI: [136, 156]) and 53 gold medals (95% CI: [50, 56]), reflecting increases of +20 total and +13 gold medals relative to 2024; in contrast, China is forecast to decline to 82 total medals (95% CI: [75, 90]) and 31 gold medals (95% CI: [28, 34]), while Great Britain is expected to drop by 5 total medals (down to 60) and lose 2 gold medals (resulting in 12 gold medals). Moreover, after adjusting for the home advantage effect in 2024, France is projected to regress by 10 total medals (to 54) and 4 gold medals (to 12). Meanwhile, both Australia and Japan exhibit modest improvements, and the Netherlands shows a strong upward trend with an increase of 11 total medals and 5 gold medals. Overall, our model indicates that the United States and the Netherlands are most likely to improve, whereas China, Great Britain, France, Italy, and South Korea are expected to perform worse than in 2024. The 95% credible intervals, derived from the posterior predictive draws, quantify the uncertainty in our predictions and provide a robust framework for interpreting the range of plausible future outcomes.

<!-- b001164 | prose | pages [10, 11] -->
关注数学模型 represent other medals; the solid black line shows the total medal prediction, the dashed dark orange line shows the gold medal prediction, and the shaded areas indicate the 95% credible intervals.

<!-- b001165 | furniture | pages [10] -->
2

<!-- b001166 | furniture | pages [10] -->
MATHmodels

<!-- b001167 | furniture | pages [10] -->
获取更多资讯

<!-- b001168 | furniture | pages [11] -->
Team # 2513314

<!-- b001169 | furniture | pages [11] -->
Page 11 of 22

<!-- b001170 | caption | pages [11] -->
Figure 4: Predicted Medal Allocations for LA 2028. Gold bars represent gold medals and silver bars

<!-- b001172 | prose | pages [11] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b001173 | caption | pages [11] -->
Table 3: Probabilities of the country that will achieve a Breakthrough From Zero in 2028.

<!-- b001174 | prose | pages [11] -->
Category Country Probability 95% CI Malaysia 0.6861 [0.4568, 0.8132] Gold Refugee Olympic Team 0.3788 [0.3214, 0.4128] Haiti 0.2569 [0.2112, 0.0.2698] South Sudan 0.3904 [0.3315, 0.4208] Total Guinea 0.3227 [0.2774, 0.3518] Myanmar 0.1554 [0.1102, 0.1898]

<!-- b001175 | heading | pages [11] -->
5.4 The country that will achieve a Breakthrough From Zero

<!-- b001176 | caption | pages [11] -->
Table 3 presents the estimated probabilities—with associated 95% credible intervals—for

<!-- b001177 | prose | pages [11] -->
each country to achieve a breakthrough from a zero-medal history in the 2028 Olympics. Same as above, the results are stratified into two medal groups: Gold and Total. Gold Medals

<!-- b001178 | prose | pages [11] -->
• Malaysia: The estimated probability for Malaysia to secure its first gold medal is 0.6861, with a relatively wide 95% credible interval of [0.4568, 0.8132]. This interval indicates that while the central estimate is notably high, there is considerable uncertainty in the exact probability. Nonetheless, even the lower bound of approximately 0.46 suggests a strong underlying signal for Malaysia’s breakthrough potential in the gold medal group.

<!-- b001179 | prose | pages [11, 12] -->
• Refugee Olympic Team: With an estimated breakthrough probability of 0.3788 and a narrower credible interval of [0.3214, 0.4128], the Refugee Olympic Team exhibits a moderate level of potential. The narrow interval reflects greater precision in this estimate, implying that the model is more confident about this moderate probability relative to that of Malaysia.

<!-- b001180 | furniture | pages [12] -->
Team # 2513314

<!-- b001181 | furniture | pages [12] -->
Page 12 of 22

<!-- b001183 | prose | pages [12] -->
• Haiti: Haiti’s estimated probability stands at 0.2569 with a 95% credible interval of [0.2112, 0.2698]. The relatively low point estimate, coupled with a narrow interval, reinforces the conclusion that Haiti is less likely to achieve a breakthrough in the gold medal group. The tight range indicates high confidence in this low probability estimate.

<!-- b001184 | prose | pages [12] -->
The stark contrast in point estimates—particularly the high probability for Malaysia com- pared to the lower probabilities for the Refugee Olympic Team and Haiti—highlights a notable disparity in the competitive dynamics for gold medals. Total Medals

<!-- b001185 | prose | pages [12] -->
• South Sudan: In the Total Medal group, South Sudan exhibits the highest breakthrough probability at 0.3904, with a credible interval of [0.3315, 0.4208]. Although this estimate is lower than Malaysia’s gold medal probability, it indicates that South Sudan has a competitive edge when considering all medal types combined.

<!-- b001186 | prose | pages [12] -->
• Guinea: Guinea’s estimated probability is 0.3227 with a 95% credible interval of [0.2774, 0.3518]. The interval for Guinea overlaps somewhat with that of South Sudan, suggesting that while South Sudan has a slight advantage, the difference between these two countries might not be statistically significant under a Bayesian framework.

<!-- b001187 | prose | pages [12] -->
• Myanmar: Myanmar has the lowest estimated probability in the Total group at 0.1554, with a credible interval of [0.1102, 0.1898]. This clearly distinguishes Myanmar from the other candidates in terms of breakthrough potential for accumulating any medals.

<!-- b001188 | prose | pages [12] -->
The Total Medal group exhibits a more evenly distributed set of probabilities compared to the Gold Medal group. While the overall probabilities are lower, the differences among the countries (particularly between South Sudan and Guinea) appear less pronounced. This may reflect the broader range of events and competitive factors that come into play when considering the entire medal tally, as opposed to the singular focus required for a gold medal achievement.

<!-- b001189 | heading | pages [12] -->
5.5 Important Sports and Home Event Impact

<!-- b001190 | prose | pages [12, 13] -->
Events and Medal Acquisition Analysis: The regression coefficients in Table 4 reveal that event-specific attributes are critical determinants of Olympic medal success, with notable dif- ferences across countries. For example, in the United States, the coefficient for Ball Sports Events (X7) is 0.03123 with a high posterior probability of 0.98, indicating that team sports such as basketball and football substantially drive medal acquisition. Similarly, Athletics Events (X5) show a positive effect (beta = 0.02345, Pr(𝛽> 0) = 0.97), suggesting that traditional track and field competitions are also important. In contrast, China displays a relatively modest effect for Athletics Events (X5, beta = 0.01567, Pr(𝛽> 0) = 0.92) but a more pronounced impact for Emerging Events (X8, beta = 0.01765, Pr(𝛽> 0) = 0.93), which implies that their strategic diversification into new sports disciplines plays a significant role in enhancing their medal prospects. Moreover, both the United Kingdom (beta for X5 = 0.02678, Pr(𝛽> 0) = 0.98) and France (beta for X5 = 0.02631, Pr(𝛽> 0) = 0.97) exhibit strong positive associations with Athletics Events, reinforcing the view that specific sports domains are aligned with each country’s historical strengths and strategic investments. Impact of Home Country Event Selection: The regression results in Table 4 also underscore the importance of tailoring event selection to leverage home advantage. When a country hosts the Olympics, it can capitalize on localized benefits such as familiar venues, superior logistical support, and heightened fan enthusiasm. For instance, the United States demonstrates strong positive effects in Athletics Events (X5, beta = 0.02345, 95% CI: [−0.00007, 0.04697]) and even more so in Ball Sports Events (X7, beta = 0.03123, 95% CI: [0.00771, 0.05475]), suggesting that emphasizing these sports can maximize the inherent benefits of home advantage. Similarly, in the United Kingdom and France, Athletics Events yield robust positive coefficients (UK: beta 关注数学模型 Variable United States China

<!-- b001191 | furniture | pages [12] -->
2

<!-- b001192 | furniture | pages [12] -->
MATHmodels

<!-- b001193 | furniture | pages [12] -->
获取更多资讯

<!-- b001194 | furniture | pages [13] -->
Team # 2513314

<!-- b001195 | furniture | pages [13] -->
Page 13 of 22

<!-- b001196 | caption | pages [13] -->
Table 4: Posterior summary statistics for regression coefficients for various predictors across 4 countries.

<!-- b001198 | prose | pages [13] -->
Pr(𝛽> 0) Pr(𝛽> 0) Beta Std. Err. 95% CI Beta Std. Err. 95% CI

<!-- b001199 | prose | pages [13] -->
X1 0.03412 0.01234 0.99 [0.01996, 0.04828] 0.03245 0.01156 0.99 [0.01980, 0.05510] X2 0.01745 0.00852 0.99 [0.00079, 0.03411] 0.01621 0.00825 0.98 [0.00014, 0.03228] X3 0.06567 0.01245 0.99 [0.04873, 0.07007] 0.06456 0.01231 0.99 [0.04045, 0.07867] 微信公众号：数学模型 [−0.00236, 0.02704] X4 0.01234 0.00759 0.93 0.02891 0.01055 0.98 [0.00833, 0.04949] [−0.00007, 0.04697] [−0.00589, 0.03723] X5 0.02345 0.01244 0.97 0.01567 0.01143 0.92 −0.00234 [−0.02194, 0.01726] [−0.00628, 0.03096] X6 0.01038 0.32 0.01239 0.00951 0.95 [−0.01058, 0.03254] X7 0.03123 0.00713 0.98 [0.00771, 0.05475] 0.01098 0.01162 0.85 [−0.01065, 0.03639] X8 0.01287 0.01214 0.88 0.01765 0.00854 0.93 [0.00099, 0.03431]

<!-- b001200 | prose | pages [13] -->
Variable United Kingdom France

<!-- b001201 | prose | pages [13] -->
Pr(𝛽> 0) Pr(𝛽> 0) Beta Std. Err. 95% CI Beta Std. Err. 95% CI

<!-- b001202 | prose | pages [13] -->
X1 0.03789 0.01345 0.99 [0.01153, 0.05425] 0.03983 0.01273 0.99 [0.01347, 0.05419] X2 0.01567 0.00759 0.96 [0.00097, 0.03037] 0.01532 0.00795 0.94 [0.00082, 0.03012] 微信号：MATHmodels X3 0.05345 0.01120 0.99 [0.03811, 0.07501] 0.05576 0.01134 0.99 [0.03764, 0.06816] [−0.00986, 0.02738] [−0.01022, 0.02846] X4 0.00876 0.00958 0.88 0.00912 0.00933 0.86 X5 0.02678 0.01250 0.98 [0.00228, 0.05128] 0.02631 0.01232 0.97 [0.00312, 0.05076] −0.00123 [−0.02181, 0.01935] −0.00096 [−0.02147, 0.01955] X6 0.01053 0.44 0.01025 0.48 [−0.00883, 0.04017] [−0.00984, 0.04158] X7 0.01567 0.01257 0.90 0.01687 0.01243 0.91 [−0.00105, 0.04795] [−0.00123, 0.04603] X8 0.02345 0.01257 0.97 0.02257 0.01233 0.95

<!-- b001203 | prose | pages [13] -->
= 0.02678, 95% CI: [0.00228, 0.05128]; France: beta = 0.02631, 95% CI: [0.00312, 0.05076]), indicating that host nations with strong track records in these disciplines can further enhance their medal prospects by strategically prioritizing events that align with their historical strengths and local support systems. Moreover, China’s relatively higher coefficient for Emerging Events (X8, beta = 0.01765, 95% CI: [0.00099, 0.03431]) implies that even non-traditional or newer events can be exploited effectively when a host country’s infrastructure and preparatory advantages are aligned with the chosen sports. Overall, these findings suggest that by selecting events that not only reflect historical success but also amplify home advantages, host nations can significantly improve their medal tallies. 1

<!-- b001204 | heading | pages [13] -->
6 Task 2: Dive Into Great Coach Effect

<!-- b001205 | prose | pages [13] -->
In this section, we examine another factor that can influence medal counts—the coach. Unlike athletes, who are typically constrained by nationality, coaches possess a unique flexibility to work across borders. This mobility allows them to transfer their expertise and successful training methodologies from one country’s sports system to another. Such fluidity creates what we term the “great coach effect,” where the influence of a single coach can significantly enhance a country’s medal count in specific sports [2].

<!-- b001206 | prose | pages [13] -->
For example, the legendary careers of Lang Ping and Béla Károlyi exemplify this effect. Despite coaching in vastly different cultural and sporting environments, both successfully trans- formed national teams and led them to Olympic podium finishes. Lang Ping’s experience coaching volleyball teams in both the United States and China demonstrates the potential for

<!-- b001207 | prose | pages [13] -->
1Due to space constraints, gold medal data is omitted here. The conclusions for gold medals are consistent with those for total medals.

<!-- b001208 | furniture | pages [14] -->
Team # 2513314

<!-- b001209 | furniture | pages [14] -->
Page 14 of 22

<!-- b001210 | prose | pages [14] -->
exceptional coaches to transcend national boundaries [4]. Similarly, Béla Károlyi’s transition from coaching in Romania to achieving remarkable success with the U.S. women’s gymnastics team further supports this notion [8].

<!-- b001211 | prose | pages [14] -->
Following standard analytical procedures, we first define what constitutes a "great coach" and seek to quantify their coaching impact. Next, we incorporate this variable into our BHDM model and analyze regression coefficients to assess whether and to what extent great coaches significantly influence medal counts. Finally, we will identify three countries, select great coaches for them, and estimate their impact based on the regression coefficients.

<!-- b001212 | prose | pages [14] -->
6.1 What is a Great Coach?

<!-- b001213 | prose | pages [14] -->
In our analysis, we define a "great coach" as one who has demonstrated the ability to elevate an Olympic team to achieve at least bronze medal finishes in two or more different countries. By searching the Wiki database, we identified a total of 1,103 such great coaches, among whom 697 are currently active. These coaches are engaged in multiple sports across various countries, including the United States, China, and Japan.

<!-- b001214 | prose | pages [14] -->
If we use the total number of renowned coaches as a new variable, a natural hypothesis emerges: do all renowned coaches contribute equally to a country’s medal count? We believe this assumption is overly restrictive. Our selection criteria represent only the minimum threshold for inclusion, but there is likely heterogeneity among coaches, meaning that their ability to lead teams to success varies.

<!-- b001215 | prose | pages [14] -->
For example, while Lang Ping, as a renowned coach, helped China secure one gold medal and the United States one silver medal, Béla Károlyi, another renowned coach, led his teams to at least 9 gold medals. This discrepancy highlights the differences in coaching effectiveness. Therefore, to ensure a fair reflection of each coach’s impact, a more fine-grained characterization of individual coaching abilities is necessary.

<!-- b001216 | prose | pages [14] -->
Based on the latest research on coaching effectiveness, we define the following metric to quantify the coaching ability of a "renowned coach": the coaching ability 𝐴is calculated as the number of gold medals won during their tenure multiplied by 6, plus the number of silver medals multiplied by 3, and the number of bronze medals multiplied by 1. Mathematically, this is expressed as:

<!-- b001217 | prose | pages [14] -->
𝐴= 6𝐺+ 3𝑆+ 1𝐵 (11) where 𝐺represents the number of gold medals won under the coach’s leadership, 𝑆represents the number of silver medals won, and 𝐵represents the number of bronze medals won. This metric assigns the highest weight to gold medals, followed by silver and then bronze, ensuring a more precise assessment of a coach’s contribution to medal achievements.

<!-- b001218 | prose | pages [14] -->
For a country’s coaching ability variable 𝑋9, it is defined as the sum of the coaching abilities 𝐴of all renowned coaches within that country, mathematically expressed as:

<!-- b001219 | prose | pages [14] -->
𝑁 ∑︁ 𝑋9 = 𝐴𝑖 (12) 𝑖=1 where 𝐴𝑖denotes the coaching ability of the 𝑖-th coach.

<!-- b001220 | heading | pages [14] -->
6.2 Great Coach Affect the Medals

<!-- b001221 | prose | pages [14, 15] -->
We incorporate 𝑋9 into our BHDM model and obtain its regression coefficient. Since there are 46 countries with renowned coaches, we are unable to present the specific values for each due to space constraints. Table 5 displays some summary statistics of this indicator. 关注数学模型 Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean 微信公众号：数学模型 All Medals 0.036134 0.011008 0.997 46 Gold Medals 0.028167 0.009134 0.983 45

<!-- b001222 | furniture | pages [14] -->
2

<!-- b001223 | furniture | pages [14] -->
MATHmodels

<!-- b001224 | furniture | pages [14] -->
获取更多资讯

<!-- b001225 | furniture | pages [15] -->
Team # 2513314

<!-- b001226 | furniture | pages [15] -->
Page 15 of 22

<!-- b001227 | caption | pages [15] -->
Table 5: Posterior summary statistics for the Great Coach variable 𝑿9 of 46 countries.

<!-- b001229 | prose | pages [15] -->
As shown in Table 5, the posterior mean coefficients for the Great Coach variable 𝑿9 are approximately 0.036134 for all medals and 0.028167 for gold medals, respectively. Because these coefficients reflect log-rate effects, a one-unit increase in 𝑿9 corresponds to a multiplicative change of 𝑒0.036134 ≈1.037 (roughly a 3.7% rise) in the expected total medal count and 𝑒0.028167 ≈1.029 (about a 2.9% increase) in gold medals. Consequently, even modest gains 微信号：MATHmodels in “great coach” capacity—such as recruiting or developing a coach with one additional point of aggregate coaching ability—can yield a tangible percentage uplift in a nation’s overall and top-tier (i.e., gold) Olympic performance.

<!-- b001230 | prose | pages [15] -->
Moreover, the high values of Avg. Pr(𝛽> 0) (0.997 for all medals and 0.983 for gold medals) and the fact that Pr(𝛽> 0) exceeds 0.95 for nearly every country underscore that the impact of the Great Coach variable is both statistically robust and broadly consistent across the sample of 46 nations. In other words, not only does the posterior mean of 𝛽𝑋9 suggest a positive relationship, but the overwhelming majority of countries in the dataset exhibit a high probability that increasing aggregate coaching ability leads to more medals. This finding provides strong evidence for the “great coach” effect, indicating that improvements in coaching capacity are systematically tied to enhanced Olympic performance rather than being confined to a select subset of countries.

<!-- b001231 | heading | pages [15] -->
6.3 Invest in Great Coach and Estimate its Impact

<!-- b001232 | prose | pages [15] -->
We believe that only wealthy countries have more options when it comes to investing in renowned coaches. Therefore, we selected the United States, China, and Japan—three of the world’s top-ranking countries by GDP—and carefully curated projects for each of them. The regression results are shown in Table 6.

<!-- b001233 | caption | pages [15] -->
Table 6: Parameter estimates for the Great Coach variable 𝑿9 of total medals in three countries.

<!-- b001234 | prose | pages [15] -->
Pr(𝛽> 0) Country Beta Std. Err. 95% Cred. Int.

<!-- b001235 | prose | pages [15] -->
United States 0.0367 0.0091 0.98 [0.0082, 0.0450] China 0.0445 0.0102 0.99 [0.0150, 0.0558] Japan 0.0283 0.0078 0.96 [0.0031, 0.0382]

<!-- b001236 | prose | pages [15] -->
We recommend that the United States recruit at least one “great coach” for fencing and sport climbing. With a coefficient of 0.0367, a one-unit increase in coaching capacity corresponds to an estimated impact of 𝑒0.0367 −1 ≈3.74% increase in Olympic medal counts in these disciplines.

<!-- b001237 | prose | pages [15, 16] -->
For China, the coefficient of 0.0445 implies that each additional point of 𝑿9 results in roughly 𝑒0.0445 −1 ≈4.55% enhancement in overall medal achievements, making it advisable to invest in top coaching talent for sports such as basketball and beach volleyball. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Finally, Japan exhibits a coefficient of 0.0283, translating to an expected improvement of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝑒0.0283 −1 ≈2.87%; thus, Japan should consider investing in a “great coach” for gymnastics m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and short-track speed skating to boost its medal tally. These quantitative estimates demonstrate that targeted investments in coaching excellence can yield substantial and measurable gains in Olympic performance.

<!-- b001238 | furniture | pages [15] -->
m

<!-- b001239 | furniture | pages [15] -->
m

<!-- b001240 | furniture | pages [15] -->
m

<!-- b001241 | furniture | pages [15] -->
m

<!-- b001242 | furniture | pages [15] -->
m

<!-- b001243 | furniture | pages [15] -->
m

<!-- b001244 | furniture | pages [15] -->
m

<!-- b001245 | furniture | pages [15] -->
m

<!-- b001246 | furniture | pages [15] -->
m

<!-- b001247 | furniture | pages [15] -->
m

<!-- b001248 | furniture | pages [15] -->
m

<!-- b001249 | furniture | pages [15] -->
m

<!-- b001250 | furniture | pages [15] -->
m

<!-- b001251 | furniture | pages [15] -->
m

<!-- b001252 | furniture | pages [15] -->
m

<!-- b001253 | furniture | pages [15] -->
m

<!-- b001254 | furniture | pages [15] -->
m

<!-- b001255 | furniture | pages [15] -->
m

<!-- b001256 | furniture | pages [15] -->
m

<!-- b001257 | furniture | pages [15] -->
m

<!-- b001258 | furniture | pages [15] -->
m

<!-- b001259 | furniture | pages [15] -->
m

<!-- b001260 | furniture | pages [15] -->
m

<!-- b001261 | furniture | pages [15] -->
m

<!-- b001262 | furniture | pages [15] -->
m

<!-- b001263 | furniture | pages [15] -->
m

<!-- b001264 | furniture | pages [15] -->
m

<!-- b001265 | furniture | pages [15] -->
m

<!-- b001266 | furniture | pages [15] -->
m

<!-- b001267 | furniture | pages [15] -->
m

<!-- b001268 | furniture | pages [15] -->
m

<!-- b001269 | furniture | pages [15] -->
m

<!-- b001270 | furniture | pages [15] -->
m

<!-- b001271 | furniture | pages [15] -->
m

<!-- b001272 | furniture | pages [15] -->
m

<!-- b001273 | furniture | pages [15] -->
m

<!-- b001274 | furniture | pages [15] -->
m

<!-- b001275 | furniture | pages [15] -->
m

<!-- b001276 | furniture | pages [15] -->
m

<!-- b001277 | furniture | pages [15] -->
m

<!-- b001278 | furniture | pages [15] -->
m

<!-- b001279 | furniture | pages [15] -->
m

<!-- b001280 | furniture | pages [15] -->
m

<!-- b001281 | furniture | pages [15] -->
m

<!-- b001282 | furniture | pages [15] -->
m

<!-- b001283 | furniture | pages [15] -->
m

<!-- b001284 | furniture | pages [15] -->
m

<!-- b001285 | furniture | pages [15] -->
m

<!-- b001286 | furniture | pages [15] -->
m

<!-- b001287 | furniture | pages [15] -->
m

<!-- b001288 | furniture | pages [15] -->
m

<!-- b001289 | furniture | pages [15] -->
m

<!-- b001290 | furniture | pages [15] -->
m

<!-- b001291 | furniture | pages [15] -->
m

<!-- b001292 | furniture | pages [15] -->
m

<!-- b001293 | furniture | pages [15] -->
m

<!-- b001294 | furniture | pages [15] -->
m

<!-- b001295 | furniture | pages [15] -->
m

<!-- b001296 | furniture | pages [15] -->
m

<!-- b001297 | furniture | pages [15] -->
m

<!-- b001298 | furniture | pages [15] -->
m

<!-- b001299 | furniture | pages [15] -->
m

<!-- b001300 | furniture | pages [15] -->
m

<!-- b001301 | furniture | pages [15] -->
m

<!-- b001302 | furniture | pages [15] -->
m

<!-- b001303 | furniture | pages [15] -->
m

<!-- b001304 | furniture | pages [15] -->
m

<!-- b001305 | furniture | pages [15] -->
m

<!-- b001306 | furniture | pages [15] -->
m

<!-- b001307 | furniture | pages [15] -->
m

<!-- b001308 | furniture | pages [15] -->
m

<!-- b001309 | furniture | pages [15] -->
m

<!-- b001310 | furniture | pages [15] -->
m

<!-- b001311 | furniture | pages [15] -->
m

<!-- b001312 | furniture | pages [15] -->
m

<!-- b001313 | furniture | pages [15] -->
m

<!-- b001314 | furniture | pages [15] -->
m

<!-- b001315 | furniture | pages [15] -->
m

<!-- b001316 | furniture | pages [15] -->
m

<!-- b001317 | furniture | pages [15] -->
m

<!-- b001318 | furniture | pages [15] -->
m

<!-- b001319 | furniture | pages [15] -->
m

<!-- b001320 | furniture | pages [15] -->
m

<!-- b001321 | furniture | pages [15] -->
m

<!-- b001322 | furniture | pages [15] -->
m

<!-- b001323 | furniture | pages [15] -->
m

<!-- b001324 | furniture | pages [15] -->
m

<!-- b001325 | furniture | pages [15] -->
m

<!-- b001326 | furniture | pages [15] -->
m

<!-- b001327 | furniture | pages [15] -->
m

<!-- b001328 | furniture | pages [15] -->
m

<!-- b001329 | furniture | pages [15] -->
m

<!-- b001330 | furniture | pages [15] -->
m

<!-- b001331 | furniture | pages [15] -->
m

<!-- b001332 | furniture | pages [15] -->
m

<!-- b001333 | furniture | pages [15] -->
m

<!-- b001334 | furniture | pages [15] -->
m

<!-- b001335 | furniture | pages [15] -->
m

<!-- b001336 | furniture | pages [15] -->
m

<!-- b001337 | furniture | pages [15] -->
m

<!-- b001338 | furniture | pages [15] -->
m

<!-- b001339 | furniture | pages [15] -->
m

<!-- b001340 | furniture | pages [15] -->
m

<!-- b001341 | furniture | pages [15] -->
m

<!-- b001342 | furniture | pages [15] -->
m

<!-- b001343 | furniture | pages [15] -->
m

<!-- b001344 | furniture | pages [15] -->
m

<!-- b001345 | furniture | pages [15] -->
m

<!-- b001346 | furniture | pages [15] -->
m

<!-- b001347 | furniture | pages [15] -->
m

<!-- b001348 | furniture | pages [15] -->
m

<!-- b001349 | furniture | pages [15] -->
m

<!-- b001350 | furniture | pages [15] -->
m

<!-- b001351 | furniture | pages [15] -->
m

<!-- b001352 | furniture | pages [15] -->
m

<!-- b001353 | furniture | pages [15] -->
m

<!-- b001354 | furniture | pages [15] -->
m

<!-- b001355 | furniture | pages [15] -->
m

<!-- b001356 | furniture | pages [15] -->
m

<!-- b001357 | furniture | pages [15] -->
m

<!-- b001358 | furniture | pages [15] -->
m

<!-- b001359 | furniture | pages [15] -->
m

<!-- b001360 | furniture | pages [15] -->
m

<!-- b001361 | furniture | pages [15] -->
m

<!-- b001362 | furniture | pages [15] -->
m

<!-- b001363 | furniture | pages [15] -->
m

<!-- b001364 | furniture | pages [15] -->
m

<!-- b001365 | furniture | pages [15] -->
m

<!-- b001366 | furniture | pages [15] -->
m

<!-- b001367 | furniture | pages [15] -->
m

<!-- b001368 | furniture | pages [15] -->
m

<!-- b001369 | furniture | pages [15] -->
m

<!-- b001370 | furniture | pages [15] -->
m

<!-- b001371 | furniture | pages [15] -->
m

<!-- b001372 | furniture | pages [15] -->
m

<!-- b001373 | furniture | pages [15] -->
m

<!-- b001374 | furniture | pages [15] -->
m

<!-- b001375 | furniture | pages [15] -->
m

<!-- b001376 | furniture | pages [15] -->
m

<!-- b001377 | furniture | pages [15] -->
m

<!-- b001378 | furniture | pages [15] -->
m

<!-- b001379 | furniture | pages [15] -->
m

<!-- b001380 | furniture | pages [15] -->
m

<!-- b001381 | furniture | pages [15] -->
m

<!-- b001382 | furniture | pages [15] -->
m

<!-- b001383 | furniture | pages [15] -->
m

<!-- b001384 | furniture | pages [15] -->
m

<!-- b001385 | furniture | pages [15] -->
m

<!-- b001386 | furniture | pages [15] -->
m

<!-- b001387 | furniture | pages [15] -->
m

<!-- b001388 | furniture | pages [15] -->
m

<!-- b001389 | furniture | pages [15] -->
m

<!-- b001390 | furniture | pages [15] -->
m

<!-- b001391 | furniture | pages [15] -->
m

<!-- b001392 | furniture | pages [15] -->
m

<!-- b001393 | furniture | pages [15] -->
m

<!-- b001394 | furniture | pages [15] -->
m

<!-- b001395 | furniture | pages [15] -->
m

<!-- b001396 | furniture | pages [15] -->
m

<!-- b001397 | furniture | pages [15] -->
m

<!-- b001398 | furniture | pages [15] -->
m

<!-- b001399 | furniture | pages [15] -->
m

<!-- b001400 | furniture | pages [15] -->
m

<!-- b001401 | furniture | pages [15] -->
m

<!-- b001402 | furniture | pages [15] -->
m

<!-- b001403 | furniture | pages [15] -->
m

<!-- b001404 | furniture | pages [15] -->
m

<!-- b001405 | furniture | pages [15] -->
m

<!-- b001406 | furniture | pages [15] -->
m

<!-- b001407 | furniture | pages [15] -->
m

<!-- b001408 | furniture | pages [15] -->
m

<!-- b001409 | furniture | pages [15] -->
m

<!-- b001410 | furniture | pages [15] -->
m

<!-- b001411 | furniture | pages [15] -->
m

<!-- b001412 | furniture | pages [15] -->
m

<!-- b001413 | furniture | pages [15] -->
m

<!-- b001414 | furniture | pages [15] -->
m

<!-- b001415 | furniture | pages [15] -->
m

<!-- b001416 | furniture | pages [15] -->
m

<!-- b001417 | furniture | pages [15] -->
m

<!-- b001418 | furniture | pages [15] -->
m

<!-- b001419 | furniture | pages [15] -->
m

<!-- b001420 | furniture | pages [15] -->
m

<!-- b001421 | furniture | pages [15] -->
m

<!-- b001422 | furniture | pages [15] -->
m

<!-- b001423 | furniture | pages [15] -->
m

<!-- b001424 | furniture | pages [15] -->
m

<!-- b001425 | furniture | pages [15] -->
m

<!-- b001426 | furniture | pages [15] -->
m

<!-- b001427 | furniture | pages [15] -->
m

<!-- b001428 | furniture | pages [15] -->
m

<!-- b001429 | furniture | pages [15] -->
m

<!-- b001430 | furniture | pages [15] -->
m

<!-- b001431 | furniture | pages [15] -->
m

<!-- b001432 | furniture | pages [15] -->
m

<!-- b001433 | furniture | pages [15] -->
m

<!-- b001434 | furniture | pages [15] -->
m

<!-- b001435 | furniture | pages [15] -->
m

<!-- b001436 | furniture | pages [15] -->
m

<!-- b001437 | furniture | pages [15] -->
m

<!-- b001438 | furniture | pages [15] -->
m

<!-- b001439 | furniture | pages [15] -->
m

<!-- b001440 | furniture | pages [15] -->
m

<!-- b001441 | furniture | pages [15] -->
m

<!-- b001442 | furniture | pages [15] -->
m

<!-- b001443 | furniture | pages [15] -->
m

<!-- b001444 | furniture | pages [15] -->
m

<!-- b001445 | furniture | pages [15] -->
m

<!-- b001446 | furniture | pages [15] -->
m

<!-- b001447 | furniture | pages [15] -->
m

<!-- b001448 | furniture | pages [15] -->
m

<!-- b001449 | furniture | pages [15] -->
m

<!-- b001450 | furniture | pages [15] -->
m

<!-- b001451 | furniture | pages [15] -->
m

<!-- b001452 | furniture | pages [15] -->
m

<!-- b001453 | furniture | pages [15] -->
m

<!-- b001454 | furniture | pages [15] -->
m

<!-- b001455 | furniture | pages [15] -->
m

<!-- b001456 | furniture | pages [15] -->
m

<!-- b001457 | furniture | pages [15] -->
m

<!-- b001458 | furniture | pages [15] -->
m

<!-- b001459 | furniture | pages [15] -->
m

<!-- b001460 | furniture | pages [15] -->
m

<!-- b001461 | furniture | pages [15] -->
m

<!-- b001462 | furniture | pages [15] -->
m

<!-- b001463 | furniture | pages [15] -->
m

<!-- b001464 | furniture | pages [15] -->
m

<!-- b001465 | furniture | pages [15] -->
m

<!-- b001466 | furniture | pages [15] -->
m

<!-- b001467 | furniture | pages [15] -->
m

<!-- b001468 | furniture | pages [15] -->
m

<!-- b001469 | furniture | pages [15] -->
m

<!-- b001470 | furniture | pages [15] -->
m

<!-- b001471 | furniture | pages [15] -->
m

<!-- b001472 | furniture | pages [15] -->
m

<!-- b001473 | furniture | pages [15] -->
m

<!-- b001474 | furniture | pages [15] -->
m

<!-- b001475 | furniture | pages [15] -->
m

<!-- b001476 | furniture | pages [15] -->
m

<!-- b001477 | furniture | pages [15] -->
m

<!-- b001478 | furniture | pages [15] -->
m

<!-- b001479 | furniture | pages [15] -->
m

<!-- b001480 | furniture | pages [15] -->
m

<!-- b001481 | furniture | pages [15] -->
m

<!-- b001482 | furniture | pages [15] -->
m

<!-- b001483 | furniture | pages [15] -->
m

<!-- b001484 | furniture | pages [15] -->
m

<!-- b001485 | furniture | pages [15] -->
m

<!-- b001486 | furniture | pages [15] -->
m

<!-- b001487 | furniture | pages [15] -->
m

<!-- b001488 | furniture | pages [15] -->
m

<!-- b001489 | furniture | pages [15] -->
m

<!-- b001490 | furniture | pages [15] -->
m

<!-- b001491 | furniture | pages [15] -->
m

<!-- b001492 | furniture | pages [15] -->
m

<!-- b001493 | furniture | pages [15] -->
m

<!-- b001494 | furniture | pages [15] -->
m

<!-- b001495 | furniture | pages [15] -->
m

<!-- b001496 | furniture | pages [15] -->
m

<!-- b001497 | furniture | pages [15] -->
m

<!-- b001498 | furniture | pages [15] -->
m

<!-- b001499 | furniture | pages [15] -->
m

<!-- b001500 | furniture | pages [15] -->
m

<!-- b001501 | furniture | pages [15] -->
m

<!-- b001502 | furniture | pages [15] -->
m

<!-- b001503 | furniture | pages [15] -->
m

<!-- b001504 | furniture | pages [15] -->
m

<!-- b001505 | furniture | pages [15] -->
m

<!-- b001506 | furniture | pages [15] -->
m

<!-- b001507 | furniture | pages [15] -->
m

<!-- b001508 | furniture | pages [15] -->
m

<!-- b001509 | furniture | pages [15] -->
m

<!-- b001510 | furniture | pages [15] -->
m

<!-- b001511 | furniture | pages [15] -->
m

<!-- b001512 | furniture | pages [15] -->
m

<!-- b001513 | furniture | pages [15] -->
m

<!-- b001514 | furniture | pages [15] -->
m

<!-- b001515 | furniture | pages [15] -->
m

<!-- b001516 | furniture | pages [15] -->
m

<!-- b001517 | furniture | pages [15] -->
m

<!-- b001518 | furniture | pages [15] -->
m

<!-- b001519 | furniture | pages [15] -->
m

<!-- b001520 | furniture | pages [15] -->
m

<!-- b001521 | furniture | pages [15] -->
m

<!-- b001522 | furniture | pages [15] -->
m

<!-- b001523 | furniture | pages [15] -->
m

<!-- b001524 | furniture | pages [15] -->
m

<!-- b001525 | furniture | pages [15] -->
m

<!-- b001526 | furniture | pages [15] -->
m

<!-- b001527 | furniture | pages [15] -->
m

<!-- b001528 | furniture | pages [15] -->
m

<!-- b001529 | furniture | pages [15] -->
m

<!-- b001530 | furniture | pages [15] -->
m

<!-- b001531 | furniture | pages [15] -->
m

<!-- b001532 | furniture | pages [15] -->
m

<!-- b001533 | furniture | pages [15] -->
m

<!-- b001534 | furniture | pages [15] -->
m

<!-- b001535 | furniture | pages [15] -->
m

<!-- b001536 | furniture | pages [15] -->
m

<!-- b001537 | furniture | pages [15] -->
m

<!-- b001538 | furniture | pages [15] -->
m

<!-- b001539 | furniture | pages [15] -->
m

<!-- b001540 | furniture | pages [15] -->
m

<!-- b001541 | furniture | pages [15] -->
m

<!-- b001542 | furniture | pages [15] -->
m

<!-- b001543 | furniture | pages [15] -->
m

<!-- b001544 | furniture | pages [15] -->
m

<!-- b001545 | furniture | pages [15] -->
m

<!-- b001546 | furniture | pages [15] -->
m

<!-- b001547 | furniture | pages [15] -->
m

<!-- b001548 | furniture | pages [15] -->
m

<!-- b001549 | furniture | pages [15] -->
m

<!-- b001550 | furniture | pages [15] -->
m

<!-- b001551 | furniture | pages [15] -->
m

<!-- b001552 | furniture | pages [15] -->
m

<!-- b001553 | furniture | pages [15] -->
m

<!-- b001554 | furniture | pages [15] -->
m

<!-- b001555 | furniture | pages [15] -->
m

<!-- b001556 | furniture | pages [15] -->
m

<!-- b001557 | furniture | pages [15] -->
m

<!-- b001558 | furniture | pages [15] -->
m

<!-- b001559 | furniture | pages [15] -->
m

<!-- b001560 | furniture | pages [15] -->
m

<!-- b001561 | furniture | pages [15] -->
m

<!-- b001562 | furniture | pages [16] -->
Team # 2513314

<!-- b001563 | furniture | pages [16] -->
Page 16 of 22

<!-- b001565 | heading | pages [16] -->
7 Sensitivity Analysis

<!-- b001566 | heading | pages [16] -->
7.1 Sensitivity Analysis for τ2 Values

<!-- b001567 | prose | pages [16] -->
In Section 5.2, we adopted a weakly informative prior by setting the covariance matrix for the regression coefficients as 22 "dIz⊥=83 = 1, as our initial choice. In this section, we examine how varying τ2 over a range from 0.1 to 10 affects the predicted medal counts for the 2028 Olympics. This analysis aims to determine whether changes in τ² lead to substantial differences in the 2028 medal predictions. The results, as illustrated in Figure 5, provide insights into the robustness of our predictions with respect to the prior informativeness imposed by the choice of τ2.

<!-- b001568 | caption | pages [16] -->
Figure 5: Predicted Medal Allocations for LA 2028 in different τ2. We predicted the number of

<!-- b001569 | prose | pages [16] -->
medals and gold medals in 2028 under different τ2 values and provided the 95% prediction intervals.

<!-- b001570 | prose | pages [16] -->
Predicted 2028 Medal Counts under Different τ² Values 160 - Total, τ2 = 1 (Baseline) Total, τ² = 2 Gold, τ² = 2 Gold, τ² = 1 (Baseline) 140- Total, τ² = 5 Total, τ² = 0.1 Gold, τ² = 0.1 Gold, τ² = 5 Total, τ2 = 10 Total, τ² = 0.5 120 Gold, τ² = 10 Gold, τ² = 0.5

<!-- b001571 | prose | pages [16] -->
100 - Number of Medals 80

<!-- b001572 | prose | pages [16] -->
60

<!-- b001573 | prose | pages [16] -->
40

<!-- b001574 | prose | pages [16] -->
20

<!-- b001575 | prose | pages [16] -->
United States Australia South Korea New Zealand China Great Britain Japan Netherlands Italy Canada Uzbekistan Hungary Spain France Germany Country

<!-- b001576 | prose | pages [16] -->
It is evident that the predicted medal counts for the 2028 Olympics remain remarkably consistent across the range of τ2 values considered, from 0.1 to 10. Despite the deliberate variation in the weakly informative prior's variance parameter, both the total and gold medal predictions show only minor deviations from the baseline forecast obtained with τ2 = 1. This close alignment indicates that the posterior inferences are not overly sensitive to the choice of τ2, thereby reinforcing the stability of our Bayesian framework even under different prior settings.

<!-- b001577 | prose | pages [16, 17] -->
scenarios Moreover, the corresponding 95% confidence intervals across the various largely overlap with those of the baseline, highlighting that the uncertainty associated with the 关注数学模型 predictions remains virtually unchanged. The observed fluctuations, confined within anarrow margin of ±5%, are negligible in the context of the overall predictive performance. This consistency not only demonstrates that the weakly informative prior does not exert an undue influence on the results, but also confirms that the data are sufficiently informative to drive the posterior estimates independently of the prior variance specification.

<!-- b001578 | furniture | pages [16] -->
获取更多资讯

<!-- b001579 | furniture | pages [17] -->
Team # 2513314

<!-- b001580 | furniture | pages [17] -->
Page 17 of 22

<!-- b001582 | prose | pages [17] -->
Overall, the sensitivity analysis clearly illustrates the robustness of our model. Regardless of the variations in τ2, all predicted outcomes are closely aligned with the baseline results, substantiating that the model's performance is stable under different prior informativeness levels. Such robustness is crucial for ensuring that the model's predictions can be trusted for further inferential or policy-related decisions, as the underlying inference remains reliable despite moderate changes in prior assumptions.

<!-- b001583 | heading | pages [17] -->
7.2 Sensitivity Analysis of Equal Distribution Assumptions

<!-- b001584 | prose | pages [17] -->
In our initial modeling framework, we assumed that the distribution of events and the total number of medals in 2028 would exactly match those of 2024. Recognizing that such an assumption is unlikely to hold in practice, we perform a sensitivity analysis by allowing both the event-specific medal counts and the total medal count to vary by ±5%. Specifically, we adjust these counts using five discrete steps: a decrease of 5%, a decrease of 3%, an unchanged baseline (0%), an increase of 3%, and an increase of 5%. For each scenario, all medal counts are modified accordingly and then rounded upward to ensure integer-valued predictions.

<!-- b001585 | prose | pages [17] -->
This approach permits us to systematically evaluate how small, yet realistic, changes in the underlying medal distributionassumptions impact our model's forecasts for the 2028 Olympics. By applying these percentage-based adjustments uniformly across all events and the overall medal total, we capture potential fluctuations that may arise from changes in the event program, variations in competitive intensity, or adjustments in the total number of medals awarded. The modified data sets are then fed into our BHDM model to generate alternative predictions.

<!-- b001586 | prose | pages [17] -->
The results of this sensitivity analysis are crucial for assessing the robustness of our model. If the predicted medal counts remain largely consistent across these scenarios—showing only minimal differences from the baseline—it would provide strong evidence that our model is not overly sensitive to moderate shifts in the medal distribution assumptions. Such robustness is essential for ensuring that our predictions are reliable even when the real-world conditions at the 2028 Olympics deviate slightly from the 2024 baseline.

<!-- b001587 | prose | pages [17] -->
The results illustrated in Figure 6 demonstrate that, even when the underlying medal distri- bution assumptions are varied by ±5%—with adjustments applied individually to each country's predicted counts—the forecasts for both total and gold medals remain highly consistent with the baseline predictions. Minor fluctuations are observed; however, these differences are confined within a narrow range, indicating that the model's predictions are not significantly perturbed by realistic changes in the event program or overall medal totals.

<!-- b001588 | prose | pages [17] -->
Such robustness confirms that our BHDM model reliably captures the core dynamics under- lying medal allocations, even under moderate deviations from the 2024 baseline. This stability in predictions provides strong evidence that our modeling framework can be trusted for forecasting future outcomes, as it effectively mitigates the potential impact of uncertainties in the underlying medal distribution assumptions.

<!-- b001589 | heading | pages [17] -->
Strengths and Limitation of the Proposed Model

<!-- b001590 | prose | pages [17] -->
8

<!-- b001591 | prose | pages [17] -->
Strengths.

<!-- b001592 | prose | pages [17, 18] -->
• High Predictive Accuracy: The BHDM model consistently outperforms alternative machine learning (XGBoost, RNN, and RF Two-stage) and statistical methods (Poisson, Negative Binomial) in forecasting both total and gold medal counts. For example, it the number of medals and gold medals in 2028 under different medal distributions and provided the 95% prediction intervals.

<!-- b001593 | furniture | pages [18] -->
Team # 2513314

<!-- b001594 | furniture | pages [18] -->
Page 18 of 22

<!-- b001595 | caption | pages [18] -->
Figure 6: Predicted Medal Allocations for LA 2028 in different Medal Distributions. We predicted

<!-- b001597 | prose | pages [18] -->
achieves an MSE of 6.98 and an 𝑅2 of 0.85 for predicting the total number of medals, and an MSE of 3.42 with an 𝑅2 of 0.80 for gold medals (see Table 2). These improvements underscore its capacity to capture the underlying data structure more effectively than competing approaches.

<!-- b001598 | prose | pages [18] -->
• Discrete and Constrained Outcomes: By modeling medal allocations via a Dirichlet– Multinomial likelihood, the BHDM ensures integer-valued outcomes that sum to a known total 𝑇. This feature is crucial in predicting realistic medal counts, especially when evaluating discrete events like whether a country will “break the ice” and win its first medal. The model’s ability to provide exact integer predictions (e.g., forecasting 146 total medals for the United States and 82 for China) is a key advantage over approaches that produce continuous-valued outputs.

<!-- b001599 | prose | pages [18] -->
• Robustness to Prior and Distributional Changes: Sensitivity analyses demonstrate that the BHDM model’s predictive performance remains stable across different settings of 𝜏2 (ranging from 0.1 to 10) and under ±5% variations to the total medal pool. As shown in Figures 5 and 6, the predicted 2028 medal counts and their credible intervals remain largely unaffected by these adjustments, indicating that the inference is driven more by the data than by the particular choice of prior or medal distribution assumptions.

<!-- b001600 | prose | pages [18] -->
Limitation.

<!-- b001601 | prose | pages [18, 19] -->
• Complexity and Data Requirements: The hierarchical structure, while powerful for par- tial pooling and capturing cross-country heterogeneity, entails increased computational demands compared to simpler count models. Fitting the BHDM can become computa- tionally expensive for very large datasets or when a fine-grained, event-level breakdown is required for many countries. Furthermore, to reliably estimate country-specific random effects and hyperparameters (e.g., the 𝜙𝑖concentration parameters), the model benefits 关注数学模型 from detailed, high-quality data—something that may be difficult to obtain for smaller or underrepresented countries with limited historical records.

<!-- b001602 | furniture | pages [18] -->
2

<!-- b001603 | furniture | pages [18] -->
MATHmodels

<!-- b001604 | furniture | pages [18] -->
获取更多资讯

<!-- b001605 | furniture | pages [19] -->
Team # 2513314

<!-- b001606 | furniture | pages [19] -->
Page 19 of 22

<!-- b001608 | heading | pages [19] -->
9 Task 3: Other Original Insights of Our BHDM Model

<!-- b001609 | heading | pages [19] -->
9.1 Economic level determines medals

<!-- b001610 | prose | pages [19] -->
In our final analysis of all 206 countries in the dataset, two predictors stand out as having 微信公众号：数学模型 the largest impact on a nation’s Olympic medal count: historical performance (𝑋1) and athlete delegation size (𝑋2). Both variables are closely tied to a country’s economic level, as wealthier nations tend to have better-funded sports programs and a stronger history of Olympic participa- tion. Specifically, as reported in Table 7, the mean regression coefficient for past medal counts (𝛽𝑋1) is 0.035143, while that for total athlete numbers (𝛽𝑋2) is 0.011442. These results reinforce the notion that economic strength plays a decisive role in determining a country’s Olympic success. To interpret the magnitude of these effects:

<!-- b001611 | prose | pages [19] -->
𝑒0.035143 −1 ≈3.58%, 𝑒0.011442 −1 ≈1.15%. and 微信号：MATHmodels Hence, a unit increase in 𝛽𝑋1 corresponds to roughly a 3.6% increase in the expected medal count, while a similar increase in 𝛽𝑋2 implies about a 1.2% rise. These results underscore that both a strong legacy of medal achievements and a robust delegation size can significantly boost a country’s chances of reaching the podium.

<!-- b001612 | caption | pages [19] -->
Table 7: Posterior Summary of 𝛽𝑋1 and 𝛽𝑋2 Across All Countries (206 in total).

<!-- b001613 | prose | pages [19] -->
Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean

<!-- b001614 | prose | pages [19] -->
𝛽𝑋1 0.035143 0.008224 0.981 204 𝛽𝑋2 0.011442 0.006538 0.945 178

<!-- b001615 | prose | pages [19] -->
By maintaining consistent investments in sports where they have historically excelled, countries can leverage existing expertise and well-established training systems. Meanwhile, increasing the breadth of participation through a larger delegation expands the probability of discovering or nurturing world-class athletes in more disciplines, ultimately translating into higher medal tallies.

<!-- b001616 | heading | pages [19] -->
9.2 Home Turf and Aligned Systems Prevail

<!-- b001617 | prose | pages [19] -->
Focusing on the subset of 33 countries that have hosted the Olympics at least once, our model reveals two important explanatory variables for elevating medal counts. Table 8 provides the posterior summary for:

<!-- b001618 | prose | pages [19] -->
1. Home Advantage (𝑋3): 𝛽𝑋3 has a mean of about 0.061245, which corresponds to:

<!-- b001619 | prose | pages [19] -->
𝑒0.061245 −1 ≈6.32% improvement.

<!-- b001620 | prose | pages [19] -->
This aligns well with the intuitive idea that home-country athletes benefit from logistical, infrastructural, and psychological advantages when competing on familiar ground.

<!-- b001621 | furniture | pages [20] -->
Team # 2513314

<!-- b001622 | furniture | pages [20] -->
Page 20 of 22

<!-- b001623 | prose | pages [20] -->
2. Social System Congruence (𝑋4): 𝛽𝑋4 has a mean of around 0.025982. In percentage terms:

<!-- b001624 | prose | pages [20] -->
𝑒0.025982 −1 ≈2.63% improvement.

<!-- b001625 | prose | pages [20] -->
Countries whose societal and institutional structures closely resemble those of the host may adapt more seamlessly to local conditions, cultural norms, and organizational protocols.

<!-- b001626 | caption | pages [20] -->
Table 8: Posterior Summary of 𝑋3 (Home Advantage) and 𝑋4 (Social System Congruence). There

<!-- b001627 | prose | pages [20] -->
are 33 host countries in total.

<!-- b001628 | prose | pages [20] -->
Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean

<!-- b001629 | prose | pages [20] -->
𝑋3: Home Advantage 0.061245 0.010277 0.980 33 𝑋4: Soc. System Congr. 0.025982 0.007612 0.955 30

<!-- b001630 | prose | pages [20] -->
In practical terms, this means a host nation can anticipate, on average, more than a 6% increase in its medal tally relative to non-host years. Moreover, a country resembling the host’s societal ecosystem—whether by language, cultural practices, or institutional frameworks—might also see an additional bump, albeit of a smaller magnitude. Proactive planning, like scouting local venues, training under similar conditions, and ensuring linguistic or cultural familiarity, can amplify these benefits for visiting teams as well.

<!-- b001631 | heading | pages [20] -->
9.3 Emerging Sports Aid Low-GDP Countries

<!-- b001632 | prose | pages [20] -->
Finally, our model points to a strategic pathway for 38 countries identified as being in the bottom 50% of world GDP according to the World Bank 2 and having already won at least one Olympic medal. As highlighted in Table 9, investing in less-established or newly introduced disciplines—captured by the indicator variable 𝛽𝑋8 for Emerging Events—provides these lower-GDP nations with a pronounced edge.

<!-- b001633 | caption | pages [20] -->
Table 9: Posterior Summary of 𝛽𝑋8 (Emerging Events) for 38 Low-GDP Medal-Winning Countries.

<!-- b001634 | prose | pages [20] -->
Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean

<!-- b001635 | prose | pages [20] -->
𝛽𝑋8 0.032413 0.006568 0.979 37

<!-- b001636 | prose | pages [20] -->
A mean coefficient of 0.032413 for 𝛽𝑋8 translates to about a 𝑒0.032413 −1 ≈3.29%

<!-- b001637 | prose | pages [20] -->
increment in medal counts for every unit increase in emerging-sport emphasis. In practice, this suggests that under-resourced nations can “level the playing field” by channeling their limited resources into newer sporting disciplines, where established powerhouses have yet to monopolize coaching expertise, infrastructure, and athlete development. Taking advantage of these relatively uncrowded competitive landscapes may thus maximize the return on investment for nations working within tighter financial and organizational constraints.

<!-- b001638 | heading | pages [20] -->
9.4 A letter to inform NOC

<!-- b001639 | prose | pages [20] -->
Based on the insights mentioned above, we have written a letter to NOC. The content of this letter is as follows:

<!-- b001640 | prose | pages [20, 21] -->
关注数学模型 2 http://data.worldbank.org Some insights about Olympics Medal Counts

<!-- b001641 | furniture | pages [20] -->
2

<!-- b001642 | furniture | pages [20] -->
MATHmodels

<!-- b001643 | furniture | pages [20] -->
获取更多资讯

<!-- b001644 | furniture | pages [21] -->
Team # 2513314

<!-- b001645 | furniture | pages [21] -->
Page 21 of 22

<!-- b001647 | prose | pages [21] -->
To: Country Olympics Committees From: Team #2513314 Data: January 27, 2025 Dear Country Olympics Committees leaders:

<!-- b001648 | prose | pages [21] -->
We are writing to share three major insights that can guide Olympic committees in crafting more effective, practical strategies for securing medals. Our analysis reveals how a nation’s economic capacity, its hosting opportunities, and its targeted focus on emerging sports can all 微信公众号：数学模型 contribute to elevating athletic performance on the global stage. By highlighting each factor in simple terms, we hope to show that even modest interventions can make a big difference when implemented thoughtfully.

<!-- b001649 | prose | pages [21] -->
First, our study clearly links economic strength to higher medal counts, chiefly through two channels: historical performance and the number of participating athletes. In plain language, if a country has a track record of success in certain sports, it likely possesses time-tested coaching expertise and training facilities that can be reinforced. At the same time, expanding the size of the athlete delegation—whether by discovering new talent or offering more support to existing programs—broadens the pool of potential medalists. Committees can utilize this insight by directing funds to sports with proven results while systematically scouting fresh talent to sustain 微信号：MATHmodels a healthy pipeline for future competitions.

<!-- b001650 | prose | pages [21] -->
Second, there is a distinct “home turf” benefit for nations hosting the Olympics, as local teams have the advantage of competing in familiar environments with supportive crowds. Beyond that, countries that share cultural, linguistic, or societal characteristics with the host nation can also see smaller but meaningful boosts in performance. For instance, translating key materials into a common language and training athletes to adapt to local climates or customs can reduce logistical hiccups, ensuring a smoother preparation process. Committees might consider partnerships or cultural exchange programs with future hosts to gain on-the-ground knowledge and acclimate athletes well in advance.

<!-- b001651 | prose | pages [21] -->
Third, for nations with tighter budgets, focusing on newly introduced or less-established sports offers a unique chance to thrive. Because these disciplines are not yet dominated by well- funded powerhouses, smaller countries can step in with targeted investments—like specialized coaches, better equipment, or even grassroots talent-spotting efforts. By concentrating on these emerging events, committees can quickly close the gap and even outcompete wealthier nations still focused on mainstream sports. This tailored approach lets countries make the most of limited resources and diversify their medal potential.

<!-- b001652 | prose | pages [21] -->
In conclusion, each of these insights—prioritizing historically successful events and a wider athlete pool, leveraging home-field and cultural advantages, and capitalizing on emerging sports—gives Olympic committees a roadmap for thoughtful action. We trust this overview will help you shape meaningful strategies that tap into your nation’s inherent strengths and adapt to its financial realities, ultimately lifting your athletes to new heights of excellence.

<!-- b001653 | prose | pages [21] -->
Yours Sincerely,

<!-- b001654 | furniture | pages [21] -->
Team #2513314

<!-- b001655 | prose | pages [21] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001656 | furniture | pages [21] -->
m

<!-- b001657 | furniture | pages [21] -->
m

<!-- b001658 | furniture | pages [21] -->
m

<!-- b001659 | furniture | pages [21] -->
m

<!-- b001660 | furniture | pages [21] -->
m

<!-- b001661 | furniture | pages [21] -->
m

<!-- b001662 | furniture | pages [21] -->
m

<!-- b001663 | furniture | pages [21] -->
m

<!-- b001664 | furniture | pages [21] -->
m

<!-- b001665 | furniture | pages [21] -->
m

<!-- b001666 | furniture | pages [21] -->
m

<!-- b001667 | furniture | pages [21] -->
m

<!-- b001668 | furniture | pages [21] -->
m

<!-- b001669 | furniture | pages [21] -->
m

<!-- b001670 | furniture | pages [21] -->
m

<!-- b001671 | furniture | pages [21] -->
m

<!-- b001672 | furniture | pages [21] -->
m

<!-- b001673 | furniture | pages [21] -->
m

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

<!-- b001980 | furniture | pages [22] -->
Team # 2513314

<!-- b001981 | furniture | pages [22] -->
Page 22 of 22

<!-- b001982 | heading | pages [22] -->
References

<!-- b001983 | references | pages [22] -->
[1] Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system. pages 785–794,

<!-- b001984 | references | pages [22] -->
2016.

<!-- b001985 | references | pages [22] -->
[2] Gillian M Cook, David Fletcher, and Michael Peyrebrune. Olympic coaching excellence:

<!-- b001986 | references | pages [22] -->
A quantitative study of olympic swimmers’ perceptions of their coaches. Journal of sports

<!-- b001987 | references | pages [22] -->
sciences, 40(1):32–39, 2022.

<!-- b001988 | references | pages [22] -->
[3] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. Neural Computation,

<!-- b001989 | references | pages [22] -->
9(8):1735–1780, 1997.

<!-- b001990 | references | pages [22] -->
https://olympics.com/en/athletes/pin

<!-- b001991 | references | pages [22] -->
[4] Olympics.com. Biography: Lang Ping.

<!-- b001992 | references | pages [22] -->
g-lang. Accessed: January 25, 2025.

<!-- b001993 | references | pages [22] -->
m

<!-- b001994 | references | pages [22] -->
m

<!-- b001995 | references | pages [22] -->
m

<!-- b001996 | references | pages [22] -->
m

<!-- b001997 | references | pages [22] -->
m

<!-- b001998 | references | pages [22] -->
m

<!-- b001999 | references | pages [22] -->
m

<!-- b002000 | references | pages [22] -->
m

<!-- b002001 | references | pages [22] -->
m

<!-- b002002 | references | pages [22] -->
m

<!-- b002003 | references | pages [22] -->
m

<!-- b002004 | references | pages [22] -->
m

<!-- b002005 | references | pages [22] -->
m

<!-- b002006 | references | pages [22] -->
m

<!-- b002007 | references | pages [22] -->
m

<!-- b002008 | references | pages [22] -->
m

<!-- b002009 | references | pages [22] -->
m

<!-- b002010 | references | pages [22] -->
m

<!-- b002011 | references | pages [22] -->
m

<!-- b002012 | references | pages [22] -->
m

<!-- b002013 | references | pages [22] -->
m

<!-- b002014 | references | pages [22] -->
m

<!-- b002015 | references | pages [22] -->
[5] Congjun Rao, Ming Liu, Mark Goh, and Jianghui Wen. 2-stage modified random forest

<!-- b002016 | references | pages [22] -->
m

<!-- b002017 | references | pages [22] -->
m

<!-- b002018 | references | pages [22] -->
m

<!-- b002019 | references | pages [22] -->
m

<!-- b002020 | references | pages [22] -->
m

<!-- b002021 | references | pages [22] -->
m

<!-- b002022 | references | pages [22] -->
m

<!-- b002023 | references | pages [22] -->
m

<!-- b002024 | references | pages [22] -->
m

<!-- b002025 | references | pages [22] -->
m

<!-- b002026 | references | pages [22] -->
m

<!-- b002027 | references | pages [22] -->
m

<!-- b002028 | references | pages [22] -->
m

<!-- b002029 | references | pages [22] -->
m

<!-- b002030 | references | pages [22] -->
m

<!-- b002031 | references | pages [22] -->
m

<!-- b002032 | references | pages [22] -->
m

<!-- b002033 | references | pages [22] -->
m

<!-- b002034 | references | pages [22] -->
m

<!-- b002035 | references | pages [22] -->
m

<!-- b002036 | references | pages [22] -->
m

<!-- b002037 | references | pages [22] -->
m

<!-- b002038 | references | pages [22] -->
m

<!-- b002039 | references | pages [22] -->
m

<!-- b002040 | references | pages [22] -->
m

<!-- b002041 | references | pages [22] -->
m

<!-- b002042 | references | pages [22] -->
m

<!-- b002043 | references | pages [22] -->
m

<!-- b002044 | references | pages [22] -->
m

<!-- b002045 | references | pages [22] -->
m

<!-- b002046 | references | pages [22] -->
m

<!-- b002047 | references | pages [22] -->
m

<!-- b002048 | references | pages [22] -->
m

<!-- b002049 | references | pages [22] -->
m

<!-- b002050 | references | pages [22] -->
m

<!-- b002051 | references | pages [22] -->
m

<!-- b002052 | references | pages [22] -->
m

<!-- b002053 | references | pages [22] -->
m

<!-- b002054 | references | pages [22] -->
m

<!-- b002055 | references | pages [22] -->
m

<!-- b002056 | references | pages [22] -->
m

<!-- b002057 | references | pages [22] -->
m

<!-- b002058 | references | pages [22] -->
m

<!-- b002059 | references | pages [22] -->
m

<!-- b002060 | references | pages [22] -->
m

<!-- b002061 | references | pages [22] -->
m

<!-- b002062 | references | pages [22] -->
m

<!-- b002063 | references | pages [22] -->
m

<!-- b002064 | references | pages [22] -->
m

<!-- b002065 | references | pages [22] -->
m

<!-- b002066 | references | pages [22] -->
m

<!-- b002067 | references | pages [22] -->
m

<!-- b002068 | references | pages [22] -->
m

<!-- b002069 | references | pages [22] -->
m

<!-- b002070 | references | pages [22] -->
m

<!-- b002071 | references | pages [22] -->
m

<!-- b002072 | references | pages [22] -->
m

<!-- b002073 | references | pages [22] -->
m

<!-- b002074 | references | pages [22] -->
m

<!-- b002075 | references | pages [22] -->
m

<!-- b002076 | references | pages [22] -->
m

<!-- b002077 | references | pages [22] -->
m

<!-- b002078 | references | pages [22] -->
m

<!-- b002079 | references | pages [22] -->
m

<!-- b002080 | references | pages [22] -->
m

<!-- b002081 | references | pages [22] -->
m

<!-- b002082 | references | pages [22] -->
m

<!-- b002083 | references | pages [22] -->
m

<!-- b002084 | references | pages [22] -->
m

<!-- b002085 | references | pages [22] -->
m

<!-- b002086 | references | pages [22] -->
m

<!-- b002087 | references | pages [22] -->
m

<!-- b002088 | references | pages [22] -->
m

<!-- b002089 | references | pages [22] -->
m

<!-- b002090 | references | pages [22] -->
m

<!-- b002091 | references | pages [22] -->
m

<!-- b002092 | references | pages [22] -->
m

<!-- b002093 | references | pages [22] -->
m

<!-- b002094 | references | pages [22] -->
m

<!-- b002095 | references | pages [22] -->
m

<!-- b002096 | references | pages [22] -->
m

<!-- b002097 | references | pages [22] -->
m

<!-- b002098 | references | pages [22] -->
m

<!-- b002099 | references | pages [22] -->
m

<!-- b002100 | references | pages [22] -->
m

<!-- b002101 | references | pages [22] -->
m

<!-- b002102 | references | pages [22] -->
m

<!-- b002103 | references | pages [22] -->
m

<!-- b002104 | references | pages [22] -->
m

<!-- b002105 | references | pages [22] -->
m

<!-- b002106 | references | pages [22] -->
m

<!-- b002107 | references | pages [22] -->
m

<!-- b002108 | references | pages [22] -->
m

<!-- b002109 | references | pages [22] -->
m

<!-- b002110 | references | pages [22] -->
m

<!-- b002111 | references | pages [22] -->
m

<!-- b002112 | references | pages [22] -->
m

<!-- b002113 | references | pages [22] -->
m

<!-- b002114 | references | pages [22] -->
m

<!-- b002115 | references | pages [22] -->
m

<!-- b002116 | references | pages [22] -->
m

<!-- b002117 | references | pages [22] -->
m

<!-- b002118 | references | pages [22] -->
m

<!-- b002119 | references | pages [22] -->
m

<!-- b002120 | references | pages [22] -->
m

<!-- b002121 | references | pages [22] -->
m

<!-- b002122 | references | pages [22] -->
m

<!-- b002123 | references | pages [22] -->
m

<!-- b002124 | references | pages [22] -->
m

<!-- b002125 | references | pages [22] -->
m

<!-- b002126 | references | pages [22] -->
m

<!-- b002127 | references | pages [22] -->
m

<!-- b002128 | references | pages [22] -->
m

<!-- b002129 | references | pages [22] -->
m

<!-- b002130 | references | pages [22] -->
m

<!-- b002131 | references | pages [22] -->
m

<!-- b002132 | references | pages [22] -->
m

<!-- b002133 | references | pages [22] -->
m

<!-- b002134 | references | pages [22] -->
m

<!-- b002135 | references | pages [22] -->
m

<!-- b002136 | references | pages [22] -->
m

<!-- b002137 | references | pages [22] -->
m

<!-- b002138 | references | pages [22] -->
m

<!-- b002139 | references | pages [22] -->
m

<!-- b002140 | references | pages [22] -->
m

<!-- b002141 | references | pages [22] -->
m

<!-- b002142 | references | pages [22] -->
m

<!-- b002143 | references | pages [22] -->
m

<!-- b002144 | references | pages [22] -->
m

<!-- b002145 | references | pages [22] -->
m

<!-- b002146 | references | pages [22] -->
m

<!-- b002147 | references | pages [22] -->
m

<!-- b002148 | references | pages [22] -->
m

<!-- b002149 | references | pages [22] -->
m

<!-- b002150 | references | pages [22] -->
m

<!-- b002151 | references | pages [22] -->
m

<!-- b002152 | references | pages [22] -->
m

<!-- b002153 | references | pages [22] -->
m

<!-- b002154 | references | pages [22] -->
m

<!-- b002155 | references | pages [22] -->
m

<!-- b002156 | references | pages [22] -->
m

<!-- b002157 | references | pages [22] -->
m

<!-- b002158 | references | pages [22] -->
m

<!-- b002159 | references | pages [22] -->
m

<!-- b002160 | references | pages [22] -->
m

<!-- b002161 | references | pages [22] -->
model for credit risk assessment of p2p network lending to “three rurals” borrowers. Applied

<!-- b002162 | references | pages [22] -->
m

<!-- b002163 | references | pages [22] -->
m

<!-- b002164 | references | pages [22] -->
m

<!-- b002165 | references | pages [22] -->
m

<!-- b002166 | references | pages [22] -->
m

<!-- b002167 | references | pages [22] -->
m

<!-- b002168 | references | pages [22] -->
m

<!-- b002169 | references | pages [22] -->
m

<!-- b002170 | references | pages [22] -->
m

<!-- b002171 | references | pages [22] -->
m

<!-- b002172 | references | pages [22] -->
m

<!-- b002173 | references | pages [22] -->
m

<!-- b002174 | references | pages [22] -->
m

<!-- b002175 | references | pages [22] -->
m

<!-- b002176 | references | pages [22] -->
m

<!-- b002177 | references | pages [22] -->
m

<!-- b002178 | references | pages [22] -->
m

<!-- b002179 | references | pages [22] -->
m

<!-- b002180 | references | pages [22] -->
m

<!-- b002181 | references | pages [22] -->
m

<!-- b002182 | references | pages [22] -->
m

<!-- b002183 | references | pages [22] -->
m

<!-- b002184 | references | pages [22] -->
m

<!-- b002185 | references | pages [22] -->
m

<!-- b002186 | references | pages [22] -->
m

<!-- b002187 | references | pages [22] -->
m

<!-- b002188 | references | pages [22] -->
m

<!-- b002189 | references | pages [22] -->
m

<!-- b002190 | references | pages [22] -->
m

<!-- b002191 | references | pages [22] -->
m

<!-- b002192 | references | pages [22] -->
m

<!-- b002193 | references | pages [22] -->
m

<!-- b002194 | references | pages [22] -->
m

<!-- b002195 | references | pages [22] -->
m

<!-- b002196 | references | pages [22] -->
m

<!-- b002197 | references | pages [22] -->
m

<!-- b002198 | references | pages [22] -->
m

<!-- b002199 | references | pages [22] -->
m

<!-- b002200 | references | pages [22] -->
m

<!-- b002201 | references | pages [22] -->
m

<!-- b002202 | references | pages [22] -->
m

<!-- b002203 | references | pages [22] -->
m

<!-- b002204 | references | pages [22] -->
m

<!-- b002205 | references | pages [22] -->
m

<!-- b002206 | references | pages [22] -->
m

<!-- b002207 | references | pages [22] -->
m

<!-- b002208 | references | pages [22] -->
m

<!-- b002209 | references | pages [22] -->
m

<!-- b002210 | references | pages [22] -->
m

<!-- b002211 | references | pages [22] -->
m

<!-- b002212 | references | pages [22] -->
m

<!-- b002213 | references | pages [22] -->
m

<!-- b002214 | references | pages [22] -->
m

<!-- b002215 | references | pages [22] -->
m

<!-- b002216 | references | pages [22] -->
m

<!-- b002217 | references | pages [22] -->
m

<!-- b002218 | references | pages [22] -->
m

<!-- b002219 | references | pages [22] -->
m

<!-- b002220 | references | pages [22] -->
m

<!-- b002221 | references | pages [22] -->
m

<!-- b002222 | references | pages [22] -->
m

<!-- b002223 | references | pages [22] -->
m

<!-- b002224 | references | pages [22] -->
m

<!-- b002225 | references | pages [22] -->
m

<!-- b002226 | references | pages [22] -->
m

<!-- b002227 | references | pages [22] -->
m

<!-- b002228 | references | pages [22] -->
m

<!-- b002229 | references | pages [22] -->
m

<!-- b002230 | references | pages [22] -->
m

<!-- b002231 | references | pages [22] -->
m

<!-- b002232 | references | pages [22] -->
m

<!-- b002233 | references | pages [22] -->
m

<!-- b002234 | references | pages [22] -->
m

<!-- b002235 | references | pages [22] -->
m

<!-- b002236 | references | pages [22] -->
m

<!-- b002237 | references | pages [22] -->
m

<!-- b002238 | references | pages [22] -->
m

<!-- b002239 | references | pages [22] -->
m

<!-- b002240 | references | pages [22] -->
m

<!-- b002241 | references | pages [22] -->
m

<!-- b002242 | references | pages [22] -->
m

<!-- b002243 | references | pages [22] -->
m

<!-- b002244 | references | pages [22] -->
m

<!-- b002245 | references | pages [22] -->
m

<!-- b002246 | references | pages [22] -->
m

<!-- b002247 | references | pages [22] -->
m

<!-- b002248 | references | pages [22] -->
m

<!-- b002249 | references | pages [22] -->
m

<!-- b002250 | references | pages [22] -->
m

<!-- b002251 | references | pages [22] -->
m

<!-- b002252 | references | pages [22] -->
m

<!-- b002253 | references | pages [22] -->
m

<!-- b002254 | references | pages [22] -->
m

<!-- b002255 | references | pages [22] -->
m

<!-- b002256 | references | pages [22] -->
m

<!-- b002257 | references | pages [22] -->
m

<!-- b002258 | references | pages [22] -->
m

<!-- b002259 | references | pages [22] -->
m

<!-- b002260 | references | pages [22] -->
m

<!-- b002261 | references | pages [22] -->
m

<!-- b002262 | references | pages [22] -->
m

<!-- b002263 | references | pages [22] -->
m

<!-- b002264 | references | pages [22] -->
m

<!-- b002265 | references | pages [22] -->
m

<!-- b002266 | references | pages [22] -->
m

<!-- b002267 | references | pages [22] -->
m

<!-- b002268 | references | pages [22] -->
m

<!-- b002269 | references | pages [22] -->
m

<!-- b002270 | references | pages [22] -->
m

<!-- b002271 | references | pages [22] -->
m

<!-- b002272 | references | pages [22] -->
m

<!-- b002273 | references | pages [22] -->
m

<!-- b002274 | references | pages [22] -->
m

<!-- b002275 | references | pages [22] -->
m

<!-- b002276 | references | pages [22] -->
m

<!-- b002277 | references | pages [22] -->
m

<!-- b002278 | references | pages [22] -->
m

<!-- b002279 | references | pages [22] -->
m

<!-- b002280 | references | pages [22] -->
m

<!-- b002281 | references | pages [22] -->
m

<!-- b002282 | references | pages [22] -->
m

<!-- b002283 | references | pages [22] -->
m

<!-- b002284 | references | pages [22] -->
m

<!-- b002285 | references | pages [22] -->
m

<!-- b002286 | references | pages [22] -->
m

<!-- b002287 | references | pages [22] -->
m

<!-- b002288 | references | pages [22] -->
m

<!-- b002289 | references | pages [22] -->
m

<!-- b002290 | references | pages [22] -->
m

<!-- b002291 | references | pages [22] -->
Soft Computing, 95:106570, 2020.

<!-- b002292 | references | pages [22] -->
m

<!-- b002293 | references | pages [22] -->
m

<!-- b002294 | references | pages [22] -->
m

<!-- b002295 | references | pages [22] -->
m

<!-- b002296 | references | pages [22] -->
m

<!-- b002297 | references | pages [22] -->
m

<!-- b002298 | references | pages [22] -->
m

<!-- b002299 | references | pages [22] -->
m

<!-- b002300 | references | pages [22] -->
m

<!-- b002301 | references | pages [22] -->
m

<!-- b002302 | references | pages [22] -->
m

<!-- b002303 | references | pages [22] -->
m

<!-- b002304 | references | pages [22] -->
m

<!-- b002305 | references | pages [22] -->
m

<!-- b002306 | references | pages [22] -->
m

<!-- b002307 | references | pages [22] -->
m

<!-- b002308 | references | pages [22] -->
m

<!-- b002309 | references | pages [22] -->
m

<!-- b002310 | references | pages [22] -->
m

<!-- b002311 | references | pages [22] -->
m

<!-- b002312 | references | pages [22] -->
m

<!-- b002313 | references | pages [22] -->
m

<!-- b002314 | references | pages [22] -->
m

<!-- b002315 | references | pages [22] -->
m

<!-- b002316 | references | pages [22] -->
m

<!-- b002317 | references | pages [22] -->
m

<!-- b002318 | references | pages [22] -->
m

<!-- b002319 | references | pages [22] -->
m

<!-- b002320 | references | pages [22] -->
m

<!-- b002321 | references | pages [22] -->
m

<!-- b002322 | references | pages [22] -->
m

<!-- b002323 | references | pages [22] -->
m

<!-- b002324 | references | pages [22] -->
m

<!-- b002325 | references | pages [22] -->
m

<!-- b002326 | references | pages [22] -->
m

<!-- b002327 | references | pages [22] -->
m

<!-- b002328 | references | pages [22] -->
m

<!-- b002329 | references | pages [22] -->
m

<!-- b002330 | references | pages [22] -->
m

<!-- b002331 | references | pages [22] -->
m

<!-- b002332 | references | pages [22] -->
m

<!-- b002333 | references | pages [22] -->
m

<!-- b002334 | references | pages [22] -->
m

<!-- b002335 | references | pages [22] -->
m

<!-- b002336 | references | pages [22] -->
m

<!-- b002337 | references | pages [22] -->
m

<!-- b002338 | references | pages [22] -->
m

<!-- b002339 | references | pages [22] -->
m

<!-- b002340 | references | pages [22] -->
m

<!-- b002341 | references | pages [22] -->
m

<!-- b002342 | references | pages [22] -->
m

<!-- b002343 | references | pages [22] -->
m

<!-- b002344 | references | pages [22] -->
m

<!-- b002345 | references | pages [22] -->
m

<!-- b002346 | references | pages [22] -->
m

<!-- b002347 | references | pages [22] -->
m

<!-- b002348 | references | pages [22] -->
m

<!-- b002349 | references | pages [22] -->
m

<!-- b002350 | references | pages [22] -->
m

<!-- b002351 | references | pages [22] -->
m

<!-- b002352 | references | pages [22] -->
m

<!-- b002353 | references | pages [22] -->
m

<!-- b002354 | references | pages [22] -->
m

<!-- b002355 | references | pages [22] -->
m

<!-- b002356 | references | pages [22] -->
m

<!-- b002357 | references | pages [22] -->
m

<!-- b002358 | references | pages [22] -->
m

<!-- b002359 | references | pages [22] -->
m

<!-- b002360 | references | pages [22] -->
m

<!-- b002361 | references | pages [22] -->
m

<!-- b002362 | references | pages [22] -->
m

<!-- b002363 | references | pages [22] -->
m

<!-- b002364 | references | pages [22] -->
m

<!-- b002365 | references | pages [22] -->
m

<!-- b002366 | references | pages [22] -->
m

<!-- b002367 | references | pages [22] -->
m

<!-- b002368 | references | pages [22] -->
m

<!-- b002369 | references | pages [22] -->
m

<!-- b002370 | references | pages [22] -->
m

<!-- b002371 | references | pages [22] -->
m

<!-- b002372 | references | pages [22] -->
m

<!-- b002373 | references | pages [22] -->
m

<!-- b002374 | references | pages [22] -->
m

<!-- b002375 | references | pages [22] -->
m

<!-- b002376 | references | pages [22] -->
m

<!-- b002377 | references | pages [22] -->
m

<!-- b002378 | references | pages [22] -->
m

<!-- b002379 | references | pages [22] -->
m

<!-- b002380 | references | pages [22] -->
m

<!-- b002381 | references | pages [22] -->
m

<!-- b002382 | references | pages [22] -->
m

<!-- b002383 | references | pages [22] -->
m

<!-- b002384 | references | pages [22] -->
m

<!-- b002385 | references | pages [22] -->
m

<!-- b002386 | references | pages [22] -->
m

<!-- b002387 | references | pages [22] -->
m

<!-- b002388 | references | pages [22] -->
m

<!-- b002389 | references | pages [22] -->
m

<!-- b002390 | references | pages [22] -->
m

<!-- b002391 | references | pages [22] -->
m

<!-- b002392 | references | pages [22] -->
m

<!-- b002393 | references | pages [22] -->
m

<!-- b002394 | references | pages [22] -->
m

<!-- b002395 | references | pages [22] -->
m

<!-- b002396 | references | pages [22] -->
m

<!-- b002397 | references | pages [22] -->
m

<!-- b002398 | references | pages [22] -->
m

<!-- b002399 | references | pages [22] -->
m

<!-- b002400 | references | pages [22] -->
m

<!-- b002401 | references | pages [22] -->
m

<!-- b002402 | references | pages [22] -->
m

<!-- b002403 | references | pages [22] -->
m

<!-- b002404 | references | pages [22] -->
m

<!-- b002405 | references | pages [22] -->
m

<!-- b002406 | references | pages [22] -->
m

<!-- b002407 | references | pages [22] -->
m

<!-- b002408 | references | pages [22] -->
m

<!-- b002409 | references | pages [22] -->
m

<!-- b002410 | references | pages [22] -->
m

<!-- b002411 | references | pages [22] -->
m

<!-- b002412 | references | pages [22] -->
m

<!-- b002413 | references | pages [22] -->
m

<!-- b002414 | references | pages [22] -->
m

<!-- b002415 | references | pages [22] -->
m

<!-- b002416 | references | pages [22] -->
m

<!-- b002417 | references | pages [22] -->
m

<!-- b002418 | references | pages [22] -->
m

<!-- b002419 | references | pages [22] -->
m

<!-- b002420 | references | pages [22] -->
m

<!-- b002421 | references | pages [22] -->
m

<!-- b002422 | references | pages [22] -->
m

<!-- b002423 | references | pages [22] -->
m

<!-- b002424 | references | pages [22] -->
m

<!-- b002425 | references | pages [22] -->
m

<!-- b002426 | references | pages [22] -->
m

<!-- b002427 | references | pages [22] -->
m

<!-- b002428 | references | pages [22] -->
m

<!-- b002429 | references | pages [22] -->
m

<!-- b002430 | references | pages [22] -->
m

<!-- b002431 | references | pages [22] -->
m

<!-- b002432 | references | pages [22] -->
m

<!-- b002433 | references | pages [22] -->
m

<!-- b002434 | references | pages [22] -->
m

<!-- b002435 | references | pages [22] -->
m

<!-- b002436 | references | pages [22] -->
m

<!-- b002437 | references | pages [22] -->
m

<!-- b002438 | references | pages [22] -->
m

<!-- b002439 | references | pages [22] -->
m

<!-- b002440 | references | pages [22] -->
m

<!-- b002441 | references | pages [22] -->
m

<!-- b002442 | references | pages [22] -->
m

<!-- b002443 | references | pages [22] -->
m

<!-- b002444 | references | pages [22] -->
m

<!-- b002445 | references | pages [22] -->
m

<!-- b002446 | references | pages [22] -->
m

<!-- b002447 | references | pages [22] -->
m

<!-- b002448 | references | pages [22] -->
m

<!-- b002449 | references | pages [22] -->
m

<!-- b002450 | references | pages [22] -->
m

<!-- b002451 | references | pages [22] -->
m

<!-- b002452 | references | pages [22] -->
m

<!-- b002453 | references | pages [22] -->
m

<!-- b002454 | references | pages [22] -->
m

<!-- b002455 | references | pages [22] -->
m

<!-- b002456 | references | pages [22] -->
m

<!-- b002457 | references | pages [22] -->
m

<!-- b002458 | references | pages [22] -->
m

<!-- b002459 | references | pages [22] -->
m

<!-- b002460 | references | pages [22] -->
m

<!-- b002461 | references | pages [22] -->
m

<!-- b002462 | references | pages [22] -->
m

<!-- b002463 | references | pages [22] -->
m

<!-- b002464 | references | pages [22] -->
m

<!-- b002465 | references | pages [22] -->
m

<!-- b002466 | references | pages [22] -->
m

<!-- b002467 | references | pages [22] -->
m

<!-- b002468 | references | pages [22] -->
m

<!-- b002469 | references | pages [22] -->
m

<!-- b002470 | references | pages [22] -->
m

<!-- b002471 | references | pages [22] -->
m

<!-- b002472 | references | pages [22] -->
m

<!-- b002473 | references | pages [22] -->
m

<!-- b002474 | references | pages [22] -->
m

<!-- b002475 | references | pages [22] -->
m

<!-- b002476 | references | pages [22] -->
m

<!-- b002477 | references | pages [22] -->
m

<!-- b002478 | references | pages [22] -->
m

<!-- b002479 | references | pages [22] -->
m

<!-- b002480 | references | pages [22] -->
m

<!-- b002481 | references | pages [22] -->
m

<!-- b002482 | references | pages [22] -->
m

<!-- b002483 | references | pages [22] -->
m

<!-- b002484 | references | pages [22] -->
m

<!-- b002485 | references | pages [22] -->
m

<!-- b002486 | references | pages [22] -->
m

<!-- b002487 | references | pages [22] -->
m

<!-- b002488 | references | pages [22] -->
m

<!-- b002489 | references | pages [22] -->
m

<!-- b002490 | references | pages [22] -->
m

<!-- b002491 | references | pages [22] -->
m

<!-- b002492 | references | pages [22] -->
m

<!-- b002493 | references | pages [22] -->
m

<!-- b002494 | references | pages [22] -->
m

<!-- b002495 | references | pages [22] -->
m

<!-- b002496 | references | pages [22] -->
m

<!-- b002497 | references | pages [22] -->
m

<!-- b002498 | references | pages [22] -->
m

<!-- b002499 | references | pages [22] -->
m

<!-- b002500 | references | pages [22] -->
m

<!-- b002501 | references | pages [22] -->
m

<!-- b002502 | references | pages [22] -->
m

<!-- b002503 | references | pages [22] -->
m

<!-- b002504 | references | pages [22] -->
m

<!-- b002505 | references | pages [22] -->
m

<!-- b002506 | references | pages [22] -->
m

<!-- b002507 | references | pages [22] -->
m

<!-- b002508 | references | pages [22] -->
m

<!-- b002509 | references | pages [22] -->
m

<!-- b002510 | references | pages [22] -->
m

<!-- b002511 | references | pages [22] -->
m

<!-- b002512 | references | pages [22] -->
m

<!-- b002513 | references | pages [22] -->
m

<!-- b002514 | references | pages [22] -->
m

<!-- b002515 | references | pages [22] -->
m

<!-- b002516 | references | pages [22] -->
m

<!-- b002517 | references | pages [22] -->
m

<!-- b002518 | references | pages [22] -->
m

<!-- b002519 | references | pages [22] -->
m

<!-- b002520 | references | pages [22] -->
m

<!-- b002521 | references | pages [22] -->
m

<!-- b002522 | references | pages [22] -->
m

<!-- b002523 | references | pages [22] -->
m

<!-- b002524 | references | pages [22] -->
m

<!-- b002525 | references | pages [22] -->
m

<!-- b002526 | references | pages [22] -->
m

<!-- b002527 | references | pages [22] -->
m

<!-- b002528 | references | pages [22] -->
[6] Gary A Sailes. The myth of black sports supremacy. Journal of Black Studies, 21(4):480–

<!-- b002529 | references | pages [22] -->
m

<!-- b002530 | references | pages [22] -->
m

<!-- b002531 | references | pages [22] -->
m

<!-- b002532 | references | pages [22] -->
m

<!-- b002533 | references | pages [22] -->
m

<!-- b002534 | references | pages [22] -->
m

<!-- b002535 | references | pages [22] -->
m

<!-- b002536 | references | pages [22] -->
m

<!-- b002537 | references | pages [22] -->
m

<!-- b002538 | references | pages [22] -->
m

<!-- b002539 | references | pages [22] -->
m

<!-- b002540 | references | pages [22] -->
m

<!-- b002541 | references | pages [22] -->
m

<!-- b002542 | references | pages [22] -->
m

<!-- b002543 | references | pages [22] -->
m

<!-- b002544 | references | pages [22] -->
m

<!-- b002545 | references | pages [22] -->
m

<!-- b002546 | references | pages [22] -->
m

<!-- b002547 | references | pages [22] -->
m

<!-- b002548 | references | pages [22] -->
m

<!-- b002549 | references | pages [22] -->
m

<!-- b002550 | references | pages [22] -->
m

<!-- b002551 | references | pages [22] -->
m

<!-- b002552 | references | pages [22] -->
m

<!-- b002553 | references | pages [22] -->
m

<!-- b002554 | references | pages [22] -->
m

<!-- b002555 | references | pages [22] -->
m

<!-- b002556 | references | pages [22] -->
m

<!-- b002557 | references | pages [22] -->
m

<!-- b002558 | references | pages [22] -->
m

<!-- b002559 | references | pages [22] -->
m

<!-- b002560 | references | pages [22] -->
m

<!-- b002561 | references | pages [22] -->
m

<!-- b002562 | references | pages [22] -->
m

<!-- b002563 | references | pages [22] -->
m

<!-- b002564 | references | pages [22] -->
m

<!-- b002565 | references | pages [22] -->
m

<!-- b002566 | references | pages [22] -->
m

<!-- b002567 | references | pages [22] -->
m

<!-- b002568 | references | pages [22] -->
m

<!-- b002569 | references | pages [22] -->
m

<!-- b002570 | references | pages [22] -->
m

<!-- b002571 | references | pages [22] -->
m

<!-- b002572 | references | pages [22] -->
m

<!-- b002573 | references | pages [22] -->
m

<!-- b002574 | references | pages [22] -->
m

<!-- b002575 | references | pages [22] -->
m

<!-- b002576 | references | pages [22] -->
m

<!-- b002577 | references | pages [22] -->
m

<!-- b002578 | references | pages [22] -->
m

<!-- b002579 | references | pages [22] -->
m

<!-- b002580 | references | pages [22] -->
m

<!-- b002581 | references | pages [22] -->
m

<!-- b002582 | references | pages [22] -->
m

<!-- b002583 | references | pages [22] -->
m

<!-- b002584 | references | pages [22] -->
m

<!-- b002585 | references | pages [22] -->
m

<!-- b002586 | references | pages [22] -->
m

<!-- b002587 | references | pages [22] -->
m

<!-- b002588 | references | pages [22] -->
m

<!-- b002589 | references | pages [22] -->
m

<!-- b002590 | references | pages [22] -->
m

<!-- b002591 | references | pages [22] -->
m

<!-- b002592 | references | pages [22] -->
m

<!-- b002593 | references | pages [22] -->
m

<!-- b002594 | references | pages [22] -->
m

<!-- b002595 | references | pages [22] -->
m

<!-- b002596 | references | pages [22] -->
m

<!-- b002597 | references | pages [22] -->
m

<!-- b002598 | references | pages [22] -->
m

<!-- b002599 | references | pages [22] -->
m

<!-- b002600 | references | pages [22] -->
m

<!-- b002601 | references | pages [22] -->
m

<!-- b002602 | references | pages [22] -->
m

<!-- b002603 | references | pages [22] -->
m

<!-- b002604 | references | pages [22] -->
m

<!-- b002605 | references | pages [22] -->
m

<!-- b002606 | references | pages [22] -->
m

<!-- b002607 | references | pages [22] -->
m

<!-- b002608 | references | pages [22] -->
m

<!-- b002609 | references | pages [22] -->
m

<!-- b002610 | references | pages [22] -->
m

<!-- b002611 | references | pages [22] -->
m

<!-- b002612 | references | pages [22] -->
m

<!-- b002613 | references | pages [22] -->
m

<!-- b002614 | references | pages [22] -->
m

<!-- b002615 | references | pages [22] -->
m

<!-- b002616 | references | pages [22] -->
m

<!-- b002617 | references | pages [22] -->
m

<!-- b002618 | references | pages [22] -->
m

<!-- b002619 | references | pages [22] -->
m

<!-- b002620 | references | pages [22] -->
m

<!-- b002621 | references | pages [22] -->
m

<!-- b002622 | references | pages [22] -->
m

<!-- b002623 | references | pages [22] -->
m

<!-- b002624 | references | pages [22] -->
m

<!-- b002625 | references | pages [22] -->
m

<!-- b002626 | references | pages [22] -->
m

<!-- b002627 | references | pages [22] -->
m

<!-- b002628 | references | pages [22] -->
m

<!-- b002629 | references | pages [22] -->
m

<!-- b002630 | references | pages [22] -->
m

<!-- b002631 | references | pages [22] -->
m

<!-- b002632 | references | pages [22] -->
m

<!-- b002633 | references | pages [22] -->
m

<!-- b002634 | references | pages [22] -->
m

<!-- b002635 | references | pages [22] -->
m

<!-- b002636 | references | pages [22] -->
m

<!-- b002637 | references | pages [22] -->
m

<!-- b002638 | references | pages [22] -->
m

<!-- b002639 | references | pages [22] -->
m

<!-- b002640 | references | pages [22] -->
m

<!-- b002641 | references | pages [22] -->
m

<!-- b002642 | references | pages [22] -->
m

<!-- b002643 | references | pages [22] -->
m

<!-- b002644 | references | pages [22] -->
m

<!-- b002645 | references | pages [22] -->
m

<!-- b002646 | references | pages [22] -->
m

<!-- b002647 | references | pages [22] -->
m

<!-- b002648 | references | pages [22] -->
m

<!-- b002649 | references | pages [22] -->
m

<!-- b002650 | references | pages [22] -->
m

<!-- b002651 | references | pages [22] -->
m

<!-- b002652 | references | pages [22] -->
m

<!-- b002653 | references | pages [22] -->
m

<!-- b002654 | references | pages [22] -->
m

<!-- b002655 | references | pages [22] -->
m

<!-- b002656 | references | pages [22] -->
m

<!-- b002657 | references | pages [22] -->
m

<!-- b002658 | references | pages [22] -->
m

<!-- b002659 | references | pages [22] -->
m

<!-- b002660 | references | pages [22] -->
m

<!-- b002661 | references | pages [22] -->
m

<!-- b002662 | references | pages [22] -->
m

<!-- b002663 | references | pages [22] -->
m

<!-- b002664 | references | pages [22] -->
m

<!-- b002665 | references | pages [22] -->
m

<!-- b002666 | references | pages [22] -->
m

<!-- b002667 | references | pages [22] -->
m

<!-- b002668 | references | pages [22] -->
m

<!-- b002669 | references | pages [22] -->
m

<!-- b002670 | references | pages [22] -->
m

<!-- b002671 | references | pages [22] -->
m

<!-- b002672 | references | pages [22] -->
m

<!-- b002673 | references | pages [22] -->
m

<!-- b002674 | references | pages [22] -->
m

<!-- b002675 | references | pages [22] -->
m

<!-- b002676 | references | pages [22] -->
m

<!-- b002677 | references | pages [22] -->
m

<!-- b002678 | references | pages [22] -->
m

<!-- b002679 | references | pages [22] -->
m

<!-- b002680 | references | pages [22] -->
m

<!-- b002681 | references | pages [22] -->
m

<!-- b002682 | references | pages [22] -->
m

<!-- b002683 | references | pages [22] -->
m

<!-- b002684 | references | pages [22] -->
487, 1991.

<!-- b002685 | references | pages [22] -->
[7] Christoph Schlembach, Sascha L. Schmidt, Dominik Schreyer, and Linus Wunderlich.

<!-- b002686 | references | pages [22] -->
Forecasting the olympic medal distribution – a socioeconomic machine learning model.

<!-- b002687 | references | pages [22] -->
Technological Forecasting and Social Change, 175:121314, 2022.

<!-- b002688 | references | pages [22] -->
https://usagym.org/hallo

<!-- b002689 | references | pages [22] -->
[8] USA Gymnastics Hall of Fame. Béla & Márta Károlyi.

<!-- b002690 | references | pages [22] -->
ffame/inductee/coaching-team-bela-martha-karolyi/. Accessed: January 25,

<!-- b002691 | references | pages [22] -->
2025.

<!-- b002692 | references | pages [22] -->
关注数学模型

<!-- b002693 | furniture | pages [22] -->
2

<!-- b002694 | furniture | pages [22] -->
MATHmodels

<!-- b002695 | furniture | pages [22] -->
获取更多资讯
