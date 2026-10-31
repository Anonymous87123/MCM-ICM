# P-C-2025-2514362-c904f1a9

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
2514362

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Unveiling 2028 Glory: Data-Driven Predictions and

<!-- b000009 | title | pages [1] -->
Strategic Insights via Advanced Statistical Models

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
The 2024 Summer Olympics have concluded, yet the memorable moments remain cap- tivating, fueling anticipation for the 2028 Los Angeles Olympics. People are already spec- ulating on the medal counts for various nations in 2028, examining the interplay between countries and sports, exploring in which sports their own country can make progress.

<!-- b000013 | prose | pages [1] -->
We initiated our analysis with data preprocessing to construct a spatiotemporally coher- ent dataset. Subsequently, we engineered features leveraging historical data and incorpo- rated variables to account for host advantages and the introduction of new Olympic events. Additionally, during the data processing, a marked shift in medal distribution from 1952 to

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
1991 prompted the introduction of a Cold War correction factor to reﬁne our model.

<!-- b000016 | prose | pages [1] -->
We constructed a mixed-effect negative binomial regression model to address the discrete nature of medal counts, effectively capturing country heterogeneity and tempo- ral unpredictability while quantifying the impact of factors like historical performance and We predicted the 2028 medal table: the United States leads with 42 gold host effects. medals(95%CI:[37,46]) and 122 total medals(95%CI:[113,131]) , followed by China with 36 gold medals([32,41]) and 91 total medals([83,100]). The 3rd to 5th places are Japan, the United Kingdom and Australia.

<!-- b000017 | prose | pages [1] -->
A zero-inﬂated model is developed to predict the probability of zero medals, sharing features with the main model but focusing on competitive countries and identifying poten- tial ﬁrst-time medal winners. Cyprus, Fiji, and Kuwait are identiﬁed as the most likely medal winners with probabilities of 58.2%, 42.1%, and 33.5% respectively.

<!-- b000018 | prose | pages [1] -->
By employing modular collaboration and structural nesting, we combined these models into a multi-level ensemble model to analyze the regression and progress of each country in 2028. This approach further explores the relationship between countries and sports and identiﬁes advantageous projects for each country. Additionally, we modeled the impact of new events selected by the host country on the 2028 medal table projections.

<!-- b000019 | prose | pages [1] -->
To solve the challenges of statistical bias and interpretability of coaching effect analy- sis under small sample conditions, we propose a simpliﬁed analysis framework based on Bayesian modiﬁed entropy. By introducing the Laplace smoothing technique to recon- struct the probability estimation, the model designs a dual veriﬁcation mechanism of binary event-driven information gain (IG) and effect intensity ratio to form a closed-loop veriﬁca- tion. We suggest that Sweden consider bringing in a great coach for wrestling, Hungary for wrestling, and France for rowing. This might increase the medal counts for Sweden, Hun- gary, and France by 5-8, 3-5, and 6-10 medals respectively in the next two Olympic Games.

<!-- b000020 | prose | pages [1] -->
Throughout the modeling process, we also gained insights into various aspects, such as the duality of the host effect and the uncertainty of black swan events, providing reference opinions for the Olympic Committees of various countries.

<!-- b000021 | keywords | pages [1] -->
Keywords: Bayesian entropy analysis, Zero-inﬂated negative binomial regression, Mixed-

<!-- b000022 | prose | pages [1] -->
effect negative binomial regression, Laplace smoothing, Information gain for quantifying associations, Exponential decay weight design.

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
2

<!-- b000025 | heading | pages [2] -->
Introduction

<!-- b000026 | prose | pages [2] -->
1 Problem Background 1.1 2 Problem Restatement . 1.2 2 Literature Review 1.3 3 模型 1.4 Data Cleaning 3

<!-- b000027 | heading | pages [2] -->
1.5 Our Work

<!-- b000028 | prose | pages [2] -->
4

<!-- b000029 | heading | pages [2] -->
Assumptions and Justifications

<!-- b000030 | prose | pages [2] -->
4 2

<!-- b000031 | heading | pages [2] -->
Notations

<!-- b000032 | prose | pages [2] -->
5 3

<!-- b000033 | heading | pages [2] -->
Multi-level integrated forecasting model

<!-- b000034 | prose | pages [2] -->
6 4

<!-- b000035 | heading | pages [2] -->
Mixed effects negative binomial regression model

<!-- b000036 | prose | pages [2] -->
4.1 6 4.1.1 Model selection background . 6 4.1.2

<!-- b000037 | heading | pages [2] -->
The establishment of mathematical model

<!-- b000038 | prose | pages [2] -->
6 4.1.3 7 Case Analysis

<!-- b000039 | heading | pages [2] -->
Predictions for the Results of the 2028 Summer Olympics

<!-- b000040 | prose | pages [2] -->
4.1.4 8

<!-- b000041 | heading | pages [2] -->
Zero expansion negative binomial model (ZINB)

<!-- b000042 | prose | pages [2] -->
9 4.2 Model selection background . 9 4.2.1 4.2.2

<!-- b000043 | heading | pages [2] -->
The establishment of mathematical model

<!-- b000044 | prose | pages [2] -->
10 11 4.2.3 The result of mathematical model .

<!-- b000045 | prose | pages [2] -->
Relationship between the Events and Countries 11 4.3 Project Selection and its Impact.. 4.4 12

<!-- b000046 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000047 | prose | pages [2] -->
13 4.5 Analysis of the Volatility of Country Rankings 4.5.1 13 III

<!-- b000048 | heading | pages [2] -->
Model comparison

<!-- b000049 | prose | pages [2] -->
4.5.2 13

<!-- b000050 | heading | pages [2] -->
Parameter sensitivity analysis

<!-- b000051 | prose | pages [2] -->
4.5.3 13 4.5.4 Ablation Study 14

<!-- b000052 | heading | pages [2] -->
Entropy model based on Bayesian Modification

<!-- b000053 | prose | pages [2] -->
14 5

<!-- b000054 | heading | pages [2] -->
5.1 Model Selection Background .

<!-- b000055 | prose | pages [2] -->
14 The Establishment of the Mathematical Model . 5.2 15 16 5.3 Case Analysis The result of the mathematical model. 17 5.4

<!-- b000056 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000057 | prose | pages [2] -->
19 5.5 Original Insights 20 6 Analysis of "Potential Medal" in Non-Medal-Winning Nations 20 6.1 The Multiplier Effect of Elite Coaches 6.2 20 6.3 Dual Nature of Host Effect 21 The reference value of Cold War factors 6.4 22 22

<!-- b000058 | heading | pages [2] -->
Strengths and weaknesses

<!-- b000059 | prose | pages [2] -->
7

<!-- b000060 | heading | pages [2] -->
7.1 Strengths

<!-- b000061 | prose | pages [2] -->
22

<!-- b000062 | heading | pages [2] -->
7.2 Weaknesses

<!-- b000063 | prose | pages [2] -->
22

<!-- b000064 | heading | pages [2] -->
Conclusion

<!-- b000065 | prose | pages [2] -->
23 8 25 Report on the Use of Al A

<!-- b000066 | prose | pages [2] -->
关注数学模型

<!-- b000067 | furniture | pages [2] -->
获取更多资讯

<!-- b000068 | furniture | pages [2] -->
1

<!-- b000069 | furniture | pages [3] -->
Team # 2514362

<!-- b000070 | furniture | pages [3] -->
Page 2 of 26

<!-- b000071 | heading | pages [3] -->
1 Introduction

<!-- b000072 | heading | pages [3] -->
1.1 Problem Background

<!-- b000073 | prose | pages [3] -->
As the preeminent global sporting event, the Olympic Games is not merely a show- case of athletic prowess and achievement; it also serves as a powerful indicator of a na- tion’s sporting capabilities and its broader national strength. During the Games, spectators and stakeholders alike are keenly interested in tracking the medal tally, eager to know how many medals their favorite athletes have secured and how their country is performing over- 微信公众号：数学模型 all. While much attention is naturally directed toward the top of the medal table, there is also signiﬁcant interest in those countries and regions that trail behind. For these nations, securing even a single additional medal represents a signiﬁcant leap forward.

<!-- b000074 | caption | pages [3] -->
Figure 1: Awards of some countries in the past 11 Olympic Games

<!-- b000075 | prose | pages [3] -->
微信号：MATHmodels The top 16 in the gold medal The performance of the U.S. The performance of China table and their total number of medals

<!-- b000076 | prose | pages [3] -->
Moreover, beyond the focus on medal counts, countries also analyze their performance across various sports to identify areas of untapped potential. Recognizing the overwhelm- ing impact of exceptional coaching, many nations consider strategic investments in top-tier coaches to enhance their athletes’ performance and propel them to higher positions in the medal standings.

<!-- b000077 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000078 | prose | pages [3] -->
Task 1 : Construct a medal table model that encompasses the medal counts of all partic- ipating countries, with a minimum inclusion of gold medals and total medals.

<!-- b000079 | prose | pages [3] -->
• Forecast the medal results for the 2028 Olympic Games hosted in Los Angeles, USA and identify which countries are likely to experience an increase in their medal tally and which may see a decline.

<!-- b000080 | prose | pages [3] -->
• Predict which countries will secure their ﬁrst Olympic medals in the upcoming Games and estimate the associated probability.

<!-- b000081 | prose | pages [3] -->
• Investigate the correlation between Olympic sports and the medal counts of participat- ing countries. Identify which sports are most crucial to speciﬁc countries and provide explanations for these trends. Additionally, explore how the selection of events by the organizing committee can impact the competitive outcomes.

<!-- b000082 | prose | pages [3, 4] -->
Task 2 : Evaluate the impact of elite coaching on Olympic medal performance. Identify three countries and recommend speciﬁc sports in which they should prioritize investing in top-tier coaching talent. Assess the potential inﬂuence of such strategic investments on their medal outcomes. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Task 3 : Reveal the models distinctive perspectives on Olympic medal distribution and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m elucidate how these insights can inform decisions for National Olympic Committees.

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

<!-- b000407 | furniture | pages [4] -->
Team # 2514362

<!-- b000408 | furniture | pages [4] -->
Page 3 of 26

<!-- b000410 | heading | pages [4] -->
1.3 Literature Review

<!-- b000411 | prose | pages [4] -->
Recent Olympic medal prediction research has evolved from macro-level analyses to multidimensional modeling, incorporating socioeconomic factors, historical performance, event dynamics, and the inﬂuence of elite coaching. Shi et al.(2024) used SHAP method to show that medal predictability varies across sports, with China’s table tennis dominance linked to population size, GDP per capita, and historical success. Team-speciﬁc effects, likely from elite coaches, contributed over 40% to predictions in sports like Russian gym- nastics and Chinese diving. Fei(2013) identiﬁed a global sports pattern: Europe dominates in throwing events, the Americas in sprints, Africa in middle- and long-distance running, and Asia in endurance events like racewalking. These regional disparities highlight the need for nuanced predictive models.

<!-- b000412 | prose | pages [4] -->
Methodologically, Wang(2019) validated the correlation between GDP per capita, host advantages, and historical performance using neural networks and a Cobb-Douglas frame- work. However, these models are sensitive to transient factors like athlete performance ﬂuctuations. Zhao et al.(2012) improved accuracy by optimizing v-SVR parameters with genetic algorithms and incorporating home advantage adjustments.

<!-- b000413 | prose | pages [4] -->
The Great Coach Effect Empirical studies on elite coaching are limited, but case analyses suggest its transformative impact. Lang Ping’s coaching revitalized Chinese womens volley- ball, leading to a gold medal in 2016 after a ﬁfth-place ﬁnish in 2012. Béla Károlyis difﬁculty- ﬁrst approach in U.S. gymnastics resulted in a 50% medal increase post-1991. Jowetts (2007) 3+1Cs model indicates that coaching can contribute 1020% to performance gains through enhanced team cohesion and leadership. Isolating coaching impacts from other variables requires advanced methods like DID or SHAP decomposition.

<!-- b000414 | prose | pages [4] -->
In this paper, we develop a novel dual-model framework combining Bayesian entropy- driven coaching effect analysis and mixed-effects zero-inﬂated negative binomial regres- sion to address critical gaps in Olympic medal prediction. Our approach uniquely inte- grates Laplace-smoothed information gain to quantify small-sample coaching impacts, time- decayed historical performance with host-country dynamics, and event-speciﬁc adaptability to resolve overdispersion and zero-inﬂation challenges. By synthesizing these innovations, the model advances beyond traditional single-method approaches, offering robust uncer- tainty quantiﬁcation through asymmetric bootstrap intervals and actionable insights into strategic resource allocation for Olympic committees.

<!-- b000415 | heading | pages [4] -->
1.4 Data Cleaning

<!-- b000416 | prose | pages [4] -->
In our analysis of Olympic medal data, several challenges emerged that required careful m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m consideration. One issue was the inconsistency in country names, particularly the transition m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m from the Soviet Union to Russia. We have adopted the convention that Russia(now ROC) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m inherits the medal count of the Soviet Union, ensuring continuity in dataset. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Additionally, we encountered missing values for countries that did not participate in m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m certain Olympic Games in the data processing process. To address this, we have assigned a medal count of zero for those years, thereby maintaining a comprehensive and uninter- rupted dataset for analysis.

<!-- b000417 | prose | pages [4] -->
There are also some problems related to history. For example, Germany have tow IOC codes (GER and FGR), both of which needed to be counted. Refugee Olympic Team, Inde- pendent Olympians, which served as unique bodies of Olympic Games, should be noted when counting the medals, with the ﬁrst identiﬁed as a playing body, the second identiﬁed as a part of Russia (now ROC). 关注数学模型

<!-- b000418 | furniture | pages [4] -->
2

<!-- b000419 | furniture | pages [4] -->
MATHmodels

<!-- b000420 | furniture | pages [4] -->
获取更多资讯

<!-- b000421 | furniture | pages [5] -->
Team # 2514362

<!-- b000422 | furniture | pages [5] -->
Page 4 of 26

<!-- b000423 | heading | pages [5] -->
1.5 Our Work

<!-- b000424 | prose | pages [5] -->
The ﬂow chart below shows our work’s framework visually.

<!-- b000425 | prose | pages [5] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000426 | caption | pages [5] -->
Figure 2: Our Work

<!-- b000427 | heading | pages [5] -->
2 Assumptions and Justiﬁcations

<!-- b000428 | prose | pages [5] -->
The following assumptions are made to make the problem easier to handle. Also, they help to make the predicting results more precise.

<!-- b000429 | prose | pages [5] -->
• Assumption 1 Data after World War II is important and can serve as a source of predic- tion for more preciseness. Olympic Games before 1940 had only a small number of coun- tries to participate in. Meanwhile, after World War II, more countries had the accessibil- ity to the Olympic Games. The geopolitical landscape nowadays is largely determined by World War II, despite few changes. For more preciseness and more convenience in counting medals and predicting, we only use the data from the year of 1952 in the given excel ﬁle to construct our model. Conclusions could be shown in the Figure 3.

<!-- b000430 | caption | pages [5] -->
Figure 4: Medal Trend Analysis

<!-- b000431 | caption | pages [5] -->
Figure 3: Comparison of the number

<!-- b000432 | prose | pages [5, 6] -->
of participating countries • Assumption 2 Unquantifiable external factors could be ignored in the process. The im- pact of sudden factors such as political turmoil and economic crisis on the number of medals can be ignored in the forecast. Focusing on observable variables such as histori- cal medals and the number of events can improve the interpretability of the model. Assumption 3 The historical trend of medal count exhibits temporal autocorrelation.

<!-- b000433 | furniture | pages [6] -->
Page 5 of 26

<!-- b000434 | furniture | pages [6] -->
Team # 2514362

<!-- b000436 | prose | pages [6] -->
Time series analysis can capture long-term trends in a country's performance. If the data indicates that the medal count of certain countries steadily increases or decreases over time, short-term fluctuations can be ignored to reduce model complexity. It could be captured from Figure 4 that this kind of consistency truly exists.

<!-- b000437 | prose | pages [6] -->
Assumption 4 Excluding uncontrollable factors such as injuries, retirements, etc., the number of participants and events(excluding a few new events) in the 2028 Olympics will be similar to those in the 2024 Olympics. This will help make the prediction of medals for the 2028 Olympics more executable.

<!-- b000438 | heading | pages [6] -->
3 Notations

<!-- b000439 | prose | pages [6] -->
Description

<!-- b000440 | heading | pages [6] -->
Symbol

<!-- b000441 | prose | pages [6] -->
General Symbols Medal count (gold YG Yit or total Y t) for country i at the t-th Olympics λ Exponential decay weight for historical data (default λ = 0.6) WMAE Weighted Mean Absolute Error (weights wit = 1/√Var(Yit)) Mixed-Effects Negative Binomial Model Expected medal count, Yit ∼ NB(µit, α) µit Overdispersion parameter α β1 Historical effect coefficient (constrained positive) β2 Host country effect coefficient ColdWart Binary variable for Cold War period (1 if 1952–1991) Std. dev. of country heterogeneity and time trend random effects σu, σv

<!-- b000442 | heading | pages [6] -->
Zero-Inflated Negative Binomial Model (ZINB)

<!-- b000443 | prose | pages [6] -->
Probability of country i winning zero medals at the t-th Olympics πit ProjectMatchit Project matching degree (historical medals aligned with current events) Athletesut w Weighted participant count (dynamic 3-year window)

<!-- b000444 | heading | pages [6] -->
Bayesian Entropy Model

<!-- b000445 | prose | pages [6] -->
∆Mc,s,t Medal increment for country c in sport s (Mc,s,t − Mc,s,t-4) IG Information Gain (H (M) − H (M | X)) Sc,s Potential score (combines IG and historical medal gap) Other Symbols SHAP Shapley Additive Explanations (model interpretability method) DID Difference-in-Differences (causal inference method) MAE Mean Absolute Error (used in ablation studies)

<!-- b000446 | heading | pages [6] -->
F1 Score

<!-- b000447 | heading | pages [6] -->
Harmonic mean of precision and recall (model performance metric)

<!-- b000448 | prose | pages [6] -->
95% CI 95% Confidence Interval (uncertainty quantification) Laplace Smoothing Bayesian prior adjustment with parameters α, β Γ(·) Gamma function (used in negative binomial PMF) θ Threshold for information gain significance (e.g., θ = 0.3) Normal distribution with mean µ and variance σ2 N(µ, σ2)

<!-- b000449 | prose | pages [6] -->
关注数学模型

<!-- b000450 | furniture | pages [6] -->
获取更多资讯

<!-- b000451 | furniture | pages [7] -->
Team # 2514362

<!-- b000452 | furniture | pages [7] -->
Page 6 of 26

<!-- b000453 | heading | pages [7] -->
4 Multi-level integrated forecasting model

<!-- b000454 | heading | pages [7] -->
4.1 Mixed effects negative binomial regression model

<!-- b000455 | heading | pages [7] -->
4.1.1 Model selection background

<!-- b000456 | prose | pages [7] -->
The Olympic medal count is characterized by overdispersion, where the variance signif- 微信公众号：数学模型 icantly exceeds the mean. Traditional Poisson regression, which assumes that the variance equals the mean, is not suitable for this scenario. In contrast, negative binomial regression, which incorporates a dispersion parameter, is more appropriate for modeling medal counts. Additionally, mixed-effects models are employed to account for both observable predictors (e.g., historical performance, host advantages) and unobserved heterogeneity (e.g., national resource differences, time-speciﬁc events), thereby enhancing the accuracy and robustness of medal predictions.

<!-- b000457 | heading | pages [7] -->
4.1.2 The establishment of mathematical model

<!-- b000458 | prose | pages [7] -->
First, we deal with response variables and distribution assumptions. Suppose Yit is the 微信号：MATHmodels number of medals (either gold Y G it or overall Y T it ) won by the country i at the t-th Olympic Games, and suppose Yit follows a negative binomial distribution. Next, we build a linear simulator log(µit). The linear predictor of the model (i.e. the logarithmic expected number of medals) consists of both ﬁxed and random effects. The speciﬁc formulas and limiting factors are shown in the Table 1.

<!-- b000459 | prose | pages [7] -->
In the Olympic medal prediction model, the time decay factor of historical data is used to control the weight of different historical event data on the current prediction. WMAE (Weighted Average Absolute Error) is a key indicator for optimizing λ . The following results were obtained through grid search:

<!-- b000460 | prose | pages [7] -->
⇒ λ = 0.4 WMAE = 12.3, ⇒ λ = 0.6 WMAE = 11.8 (Optimal), (1) ⇒ λ = 0.8 WMAE = 12.6.

<!-- b000461 | prose | pages [7] -->
So λ is determined as 0.6 in our model.

<!-- b000462 | prose | pages [7] -->
The ColdWar factor introduces a novel political-historical dimension to Olympic medal predictions by systematically adjusting for ideological competition effects from 1952 to 1991. It quantiﬁes the anomalous medal surplus of state-driven athletic programs (e.g., USSR, GDR) and decouples transient geopolitical biases from long-term sports trends, enhancing model robustness in post-Cold War predictions. Our model shows more preciseness after adding this coefﬁcient. Its contribution could be seen in the sensitivity analysis process.

<!-- b000463 | prose | pages [7] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000464 | furniture | pages [7] -->
m

<!-- b000465 | furniture | pages [7] -->
m

<!-- b000466 | furniture | pages [7] -->
m

<!-- b000467 | furniture | pages [7] -->
m

<!-- b000468 | furniture | pages [7] -->
m

<!-- b000469 | furniture | pages [7] -->
m

<!-- b000470 | furniture | pages [7] -->
m

<!-- b000471 | furniture | pages [7] -->
m

<!-- b000472 | furniture | pages [7] -->
m

<!-- b000473 | furniture | pages [7] -->
m

<!-- b000474 | furniture | pages [7] -->
m

<!-- b000475 | furniture | pages [7] -->
m

<!-- b000476 | furniture | pages [7] -->
m

<!-- b000477 | furniture | pages [7] -->
m

<!-- b000478 | furniture | pages [7] -->
m

<!-- b000479 | furniture | pages [7] -->
m

<!-- b000480 | furniture | pages [7] -->
m

<!-- b000481 | furniture | pages [7] -->
m

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

<!-- b000788 | furniture | pages [8] -->
Team # 2514362

<!-- b000789 | furniture | pages [8] -->
Page 7 of 26

<!-- b000790 | caption | pages [8] -->
Table 1: Summary of Formulas for the Mixed Effects Negative Binomial Regression Model

<!-- b000791 | heading | pages [8] -->
Symbol

<!-- b000792 | prose | pages [8] -->
Description Formula Response Variable Yit ∼NegativeBinomial(µit, α) Yit Medal count for country i in the t-th Olympics (gold medals Y G it or total medals Y T it ) µit Expected medal count α Overdispersion parameter log(µit) = β0 + β1Historyw log(µit) it + β2Hostit Log of the expected medal count + β3∆Et + β4TimeTrendt + β5ColdWart + ui + vt Fixed Effects β0 ∼N(0, 10) β0 Global intercept β1 ∼N(0.8, 0.1) β1 Historical effect (constrained to be posi- tive) β2 ∼N(0, 0.1) β2 Host effect β3 ∼N(0, 0.1) β3 Effect of new events β4 ∼N(0, 0.1) β4 Time trend effect β5 ∼N(0.15, 0.1) β5 Cold War correction factor Random Effects ui ∼N(0, σ2 ui u) Random effect for country heterogeneity vt ∼N(0, σ2 vt v) Random effect for time trend σu, σv ∼HalfNormal(1) σu, σv Prior distribution for standard devia- tions of country heterogeneity and time trend random effects Covariates ∑5 k=1 e−λ(k−1)Yi,t−4k Historyw Historyw = , λ = Time-weighted mean of the medal counts ∑5 it it k=1 e−λ(k−1) in the last 5 Olympics for country i 0.6 = Hostit Binary variable indicating whether Hostit { country i is the host of the t-th Olympics 1 i is the host of the tth Olympics 0 otherwise

<!-- b000793 | prose | pages [8] -->
∆Et = Et −Et−4 ∆Et Number of new events in the t-th Olympics t−tmin Standardized year t to the interval [0, 1] = tmax−tmin , tmin = TimeTrendt TimeTrendt 1952, tmax = 2024 { if t ∈[1952, 1991] 1 Variable indicating whether the t-th ColdWart = ColdWart 0 otherwise Olympics occurred during the Cold War Evaluation Metrics ∑wit|Yit −ˆYit|, 1 WMAE = ∑wit wit = WMAE Weighted Mean Absolute Error 1 √ Var( ˆYit)

<!-- b000794 | heading | pages [8] -->
4.1.3 Case Analysis

<!-- b000795 | prose | pages [8] -->
We trained the model using historical data spanning from 1952 to 2008. Based on these insights, we predicted the medal winners of selected countries in the four Olympic Games held between 2012 and 2024.

<!-- b000796 | prose | pages [8, 9] -->
The Figure 5 clearly illustrates that the dashed line corresponds to the ideal prediction trajectory, and the majority of the data points are tightly clustered around this line, which underscores the model’s reliability in forecasting outcomes. Additionally, the length of the 关注数学模型 box in the Figure 6 serves as a visual indicator of prediction accuracy. The close alignment of the mean and median values suggests that the data set’s central tendency aligns well with our assumption of a normal distribution.

<!-- b000797 | furniture | pages [8] -->
2

<!-- b000798 | furniture | pages [8] -->
MATHmodels

<!-- b000799 | furniture | pages [8] -->
获取更多资讯

<!-- b000800 | furniture | pages [9] -->
Team # 2514362

<!-- b000801 | furniture | pages [9] -->
Page 8 of 26

<!-- b000803 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000804 | caption | pages [9] -->
Figure 5: Prediction vs.Actual

<!-- b000805 | caption | pages [9] -->
Figure 6: Gold Medal Prediction Analysis

<!-- b000806 | heading | pages [9] -->
4.1.4 Predictions for the Results of the 2028 Summer Olympics

<!-- b000807 | prose | pages [9] -->
微信号：MATHmodels The projected outcomes of the 2028 Summer Olympics, as generated by our model, are depicted in the Figure 7. (Here we speciﬁcally concentrate on the predictions for the top 15 gold medal winners. ) Additionally, We will also provide the award-winning situations of about the top 30% of countries in the Table 2.

<!-- b000808 | caption | pages [9] -->
Figure 7: The predictions for the top 15 gold medal winners and their total medal counts.

<!-- b000809 | prose | pages [9] -->
Top 15 Gold Medal Table Predictions Top 15 Total Medal Table Predictions

<!-- b000810 | caption | pages [9] -->
Table 2: Forecast Result

<!-- b000811 | prose | pages [9, 10] -->
Based on the model’s predictions, we’ve also identiﬁed some potential "dark horses" at the 2028 Summer Olympics: countries that might surprise everyone and perform exception- ally well. At the same time, we’ve spotted a few others that could face a bit of a letdown, as shown in Figure 8 and Figure 9.

<!-- b000812 | furniture | pages [10] -->
Team # 2514362

<!-- b000813 | furniture | pages [10] -->
Page 9 of 26

<!-- b000815 | caption | pages [10] -->
Figure 9: Changes in gold medals

<!-- b000816 | caption | pages [10] -->
Figure 8: Changes in total medals

<!-- b000817 | prose | pages [10] -->
Great Britain is predicted to win 19 gold medals ( 95% CI : [15, 24] ) at the 2028 Olympics, an increase from the 14 gold medals in 2024. The overall medal forecast is 63, close to the 65 medals in 2024. This improvement is driven by the weighted average of recent Olympic performances ( weight λ = 0.6 ), particularly in traditional strengths like cycling and rowing. The introduction of new events such as skateboarding and rock climbing is expected to contribute an additional 23 gold medals. The historical performance weight ( β1 = 0.85 ) indicates that past achievements account for over 60% of the gold medal prediction.

<!-- b000818 | prose | pages [10] -->
Italy is predicted to win 12 gold medals ( 95% CI : [7, 16] ) and a total of 38 medals ( 95% CI : [30, 47] ), similar to the 2024 results but with potential for improvement. Italy’s histor- ical success in fencing and shooting, which accounts for 25% of its medals, will be further supported by the addition of laser running in 2028. The variance of country heterogeneity ( σu = 0.2 ) suggests that Italy has the potential to achieve breakthroughs in non-traditional sports such as track and ﬁeld sprints.

<!-- b000819 | prose | pages [10] -->
China’s forecast for gold medals in the upcoming Olympics is 36, with a range of 32 to 41. This is a decline from the 40 gold medals in 2024. The total medal forecast range is between 83 and 100, indicating a potential risk of falling below the 91 medals won in 2024. This trend may be attributed to a weakening time trend. The standardized time coefﬁcient (β4 = −0.12) suggests that traditional strongholds such as weightlifting and gymnastics have been impacted by regulatory changes, leading to reduced competitiveness.

<!-- b000820 | prose | pages [10] -->
France’s total medal forecast stands at 50, a notable decrease from the 64 medals won in 2024. This reduction may be due to the loss of the host advantage. The host gain coefﬁcient ( β2 = 0.3 ) in 2024 will be reduced to zero in 2028, which is expected to directly lower the medal count in events like judo and fencing by 5 to 7. Additionally, the shrinking number of participants cannot be overlooked. The weight of dynamic participants has dropped by 15%, affecting the medal output in sports that rely on a "quantity over quality" strategy, such as track and ﬁeld and swimming.

<!-- b000821 | heading | pages [10] -->
4.2 Zero expansion negative binomial model (ZINB)

<!-- b000822 | heading | pages [10] -->
4.2.1 Model selection background

<!-- b000823 | prose | pages [10, 11] -->
Our primary aim is to forecast the number of Olympic medals that each country will win. This prediction is essential for identifying the most likely ﬁrst-time medal winners. However, our initial modeling efforts encountered several challenges. For example, many countries, particularly small nations or those participating in the Olympics for the ﬁrst time, have never won a medal before. Additionally, the medal counts exhibit a variance that is signiﬁcantly higher than the mean, which violates the assumptions of the traditional Poisson model. To address these issues, we propose to employ a zero-inﬂated negative binomial 关注数学模型 model. This approach effectively separates the processes of "whether a country will win a medal" and "how many medals a country will win." By replacing the Poisson distribution, it allows for a variance that is greater than the mean, thereby providing a more accurate and robust framework for our analysis.

<!-- b000824 | furniture | pages [10] -->
2

<!-- b000825 | furniture | pages [10] -->
MATHmodels

<!-- b000826 | furniture | pages [10] -->
获取更多资讯

<!-- b000827 | furniture | pages [11] -->
Team # 2514362

<!-- b000828 | furniture | pages [11] -->
Page 10 of 26

<!-- b000830 | heading | pages [11] -->
4.2.2 The establishment of mathematical model

<!-- b000831 | prose | pages [11] -->
We use historical data and model projections to screen out countries that had never won any Olympic medals. We estimate that the probability of country i not winning any medals in the t-th Olympic Games is πit . 微信公众号：数学模型 log it(πit) = γ0 + γ1Athletesw + γ2ProjectMatch (2)

<!-- b000832 | prose | pages [11] -->
We predict that if country i does win medals, the expected number of medals is µit.

<!-- b000833 | prose | pages [11] -->
log(µit) = β0 + β1Athletesw + β2ProjectMatch (3)

<!-- b000834 | prose | pages [11] -->
Combining the above two formulas (2) (3), we can get the ﬁnal estimator:

<!-- b000835 | prose | pages [11] -->
{ πit + (1 −πit) · NB(0; µit, α) if y = 0 P(Yit = y) = (4) (1 −πit) · NB(y; µit, α) if y > 0 微信号：MATHmodels

<!-- b000836 | prose | pages [11] -->
• γ0 :The intercept term in the zero-inﬂated component of the model is assigned a prior distribution that follows a normal distribution with a mean of 0 and a standard deviation of 10. This speciﬁcation implies that, in the absence of other covariates, the logit of the probability of winning no medals is centered at 0, while also accommodating substantial uncertainty around this estimate.

<!-- b000837 | prose | pages [11] -->
γ0 ∼N(0, 10) (5)

<!-- b000838 | prose | pages [11] -->
• γ1 , γ2 : They are the coefﬁcients of the dynamic number of participants in the zero expansion part (Athletesw it) and the match degree of the project (ProjectMatchit). Their prior distributions are normal distributions with a mean of 0 and a standard deviation of 1. If γ1 < 0, the probability of zero decreases with an increasing number of participants.

<!-- b000839 | prose | pages [11] -->
If γ2 < 0, the probability of zero decreases with a higher degree of matching.

<!-- b000840 | prose | pages [11] -->
γ1, γ2 ∼N(0, 1) (6)

<!-- b000841 | prose | pages [11] -->
• β0 : It is the intercept term of the count part, and its prior distribution is a normal dis- tribution with a mean of 0 and a standard deviation of 10. This means that without the inﬂuence of other variables, the logarithmic expected value of the number of medals is expected to be 0, but allows for large uncertainties.

<!-- b000842 | prose | pages [11] -->
β0 ∼N(0, 10) (7)

<!-- b000843 | prose | pages [11] -->
• β1,β2 : They are the coefﬁcients of the dynamic number of participants (Athletesw it) and the match degree of the event in the counting section (ProjectMatchit) . Their prior distributions are normal distributions with a mean of 0 and a standard deviation of 1.

<!-- b000844 | prose | pages [11] -->
This means that these coefﬁcients are expected to be 0, but allow for some variation. If β1 > 0, the probability of zero decreases with an increasing number of participants. If β2 > 0, the probability of zero also decreases with a higher degree of matching.

<!-- b000845 | prose | pages [11, 12] -->
β1, β2 ∼N(0, 1) (8) • Athletesw it : It represents the weighted sum of the number of participants in the last 3 Olympics (the recent weight is higher, reﬂecting the continuous participation invest- ment).

<!-- b000846 | furniture | pages [12] -->
Team # 2514362

<!-- b000847 | furniture | pages [12] -->
Page 11 of 26

<!-- b000849 | prose | pages [12] -->
3 ∑ e−0.5k · Ni,t−4k Athletesw it = (9) k=1

<!-- b000850 | prose | pages [12] -->
• ProjectMatchit : It represents the proportion of historical medals related to the St of the current event (the greater the value, the more the dominant event ﬁts the current event).

<!-- b000851 | prose | pages [12] -->
∑ s∈St Medalsis ProjectMatchit = (10) TotalMedalsi

<!-- b000852 | prose | pages [12] -->
• NB(y; µ, α) : This is the probability mass function of the negative binomial distribution.

<!-- b000853 | prose | pages [12] -->
( t = πit , µ = µit) ( ) ( ) 1 α ( )y y + 1 Γ 1 αµ α ( 1 ) NB(y; µ, α) = (11) 1 + αµ 1 + αµ Γ(y + 1)Γ α

<!-- b000854 | prose | pages [12] -->
• α :

<!-- b000855 | prose | pages [12] -->
α ∼Gamma(1, 0.1) (12)

<!-- b000856 | heading | pages [12] -->
4.2.3 The result of mathematical model

<!-- b000857 | prose | pages [12] -->
Our model identiﬁes Cyprus, Fiji and Kuwait as the most likely ﬁrst-time medal win- ners among countries that have not yet secured a medal. Despite Cyprus’ relatively low event matching degree, its large number of dynamic participants results in a 58.2% proba- bility of winning its ﬁrst medal, according to the zero-inﬂated model. Fiji and Kuwait exhibit better combinations of participant numbers and event matching, with respective ﬁrst-time winning probabilities of 42.1% and 33.5%, as shown in Figure 10.

<!-- b000858 | caption | pages [12] -->
Figure 10: First-Time Medal Winners

<!-- b000859 | caption | pages [12] -->
Figure 11: Event-Country Relationship

<!-- b000860 | heading | pages [12] -->
4.3 Relationship between the Events and Countries

<!-- b000861 | prose | pages [12] -->
We assess the proportion of a speciﬁc event to a country’s total medals through the medal contribution of country i in event s, which can reﬂect historical strengths. If the medal contribution share exceeds 0.15, we deﬁne it as an advantageous event. For example, China’s diving accounts for 35% of its total medals. Medal contribution helps identify core national competitions and predict future medal distribution. Additionally, we evaluate the historical advantage coverage of country i in the current Olympic program based on the previously deﬁned event matching degree as equation (10). For example, if a new event like breaking is added to the Olympics and China has no historical medals in it, while China’s 关注数学模型 dominant events remain unchanged, the matching degree will be reduced.

<!-- b000862 | furniture | pages [12] -->
2

<!-- b000863 | furniture | pages [12] -->
MATHmodels

<!-- b000864 | furniture | pages [12] -->
获取更多资讯

<!-- b000865 | furniture | pages [13] -->
Team # 2514362

<!-- b000866 | furniture | pages [13] -->
Page 12 of 26

<!-- b000867 | prose | pages [13] -->
The core strengths of the United States in the Olympics are swimming and track and ﬁeld, accounting for 28% and 24% of its medals respectively. In the 2024 Olympics, the U.S. won 14 gold medals in swimming (38% of its total gold medals ) and 9 in track and ﬁeld ( 24% ). With a historical decay factor of 0.6, swimming’s time-weighted contribution rate peaks at 0.62 in the model. The dominance in these sports may be attributed to the American comprehensive commercial sports system. This has signiﬁcantly boosted the development of American swimming.

<!-- b000868 | prose | pages [13] -->
Historically, China’s core strengths in the Olympics have been diving, table tennis and weightlifting, which account for 35%, 29% and 22% of its gold medals respectively. In the 2024 Olympics, China’s diving team won seven out of eight gold medals in their events, while the table tennis team secured four gold medals. However, weightlifting has seen a decline in contribution rate from 28% in 2016 to 18% in 2024 due to regulatory changes. China’s dominance in these sports can be attributed to its sports system. This not only helps to sharpen their skills but also continuously elevates the overall competitive level of Chinese 微信公众号：数学模型 table tennis.

<!-- b000869 | prose | pages [13] -->
There are some other countries’ advantages (e.g., GBR, JPN, AUS) shown in Figure 11.

<!-- b000870 | heading | pages [13] -->
4.4 Project Selection and its Impact

<!-- b000871 | prose | pages [13] -->
The 2028 Los Angeles Olympics will introduce new sports such as esports, cricket, lacrosse, and breakdancing, following their addition in Paris 2024. Based on historical data from the United States, several of these new events align well with American strengths, par- ticularly lacrosse and breakdancing. Lacrosse is popular in American college leagues and shares tactical similarities with ice hockey, potentially securing at least one gold and one 微信号：MATHmodels silver medal for the U.S. The U.S. also dominates the World Hip-hop Championships and has a historical edge in gymnastics, which can translate well to breakdancing, likely adding at least one gold and one bronze medal to its tally. Overall, we found a signiﬁcant posi- tive correlation between the host country’s new event match and medal gain. It could be observed from Figure 12 that the matching degree of new events in the host country (pro- portion of historical medals) is signiﬁcantly positively correlated with medal gain. For every 0.1 increase in matching degree, the expected increase in medal count is approximately 1.8% .

<!-- b000872 | caption | pages [13] -->
Figure 12: Medal gain analysis

<!-- b000873 | caption | pages [13] -->
Figure 13: Uncertainty of Host-NewProject

<!-- b000874 | prose | pages [13] -->
Interaction Effect

<!-- b000875 | prose | pages [13, 14] -->
These new sports will signiﬁcantly impact the competitive landscape. For China, the addition of esports is challenging due to cultural factors and domestic policies that limit gaming hours, restricting the talent pool and likely reducing its esports medal count by about two. Canada, a traditional lacrosse powerhouse, will directly compete with the U.S., potentially lowering America’s medal projections. Meanwhile, India’s cricket program, a core strength, could challenge the U.S. monopoly and secure India a silver or even a gold medal. From Figure 13, it could be established that the posterior mean is µ = 0.18 and standard deviation σ = 0.04, which indicates that the host country can steadily increase the number of medals by adding advantageous events.

<!-- b000876 | furniture | pages [14] -->
Team # 2514362

<!-- b000877 | furniture | pages [14] -->
Page 13 of 26

<!-- b000879 | heading | pages [14] -->
4.5 Sensitivity Analysis

<!-- b000880 | heading | pages [14] -->
4.5.1 Analysis of the Volatility of Country Rankings

<!-- b000881 | prose | pages [14] -->
We want to assess the probability of each country ﬁnishing in the top ﬁve of the medal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m table as a way to reﬂect the stability of the model’s predictions. Based on the 1,000 bootstrap m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m samples, we calculate the probability that each country will be in the top ﬁve in the simu- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m lation prediction. The results (shown in Figure 14) show that the probability of the United m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m States and China is 99% and 95%, respectively, showing absolute superiority, compared to m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 85% and 70% for the United Kingdom and France respectively, ﬂuctuating within a certain range. Japan and Australia have a 65% and 55% probability respectively, with a lower prob- ability of ﬁnishing in the top ﬁve of the medal table. It was found that there was a high prob- ability of the country who ranks high. For example, compare with Japan, China’s forecasts are more reliable, because of its multi-project layout and other factors, while high-volatility countries such as Australia need to be interpreted with caution.

<!-- b000882 | caption | pages [14] -->
Figure 14: Country ranking volatility

<!-- b000883 | caption | pages [14] -->
Figure 15: Model comparison

<!-- b000884 | heading | pages [14] -->
4.5.2 Model comparison

<!-- b000885 | prose | pages [14] -->
We train the negative binomial model and the Poisson model respectively to compare the distribution of their prediction errors. In this diagram, the horizontal axis represents the forecast error and is the actual number of gold medals minus the predicted number of gold medals. The vertical axis represents the density value (the probability density reﬂects the degree of concentration of the error distribution). As can be seen from the Figure 15, the negative binomial model has a higher peak and narrower tail, which is concentrated in [−2, 2], while the Poisson model is more dispersed, in [−4, 6]. This indicates that the prediction error of the negative binomial model is more concentrated, and its stability is signiﬁcantly better than that of the Poisson model. At the same time, the negative binomial model has a stronger ability to process discrete data. The allowable variance of the discrete parameter alpha is introduced to be greater than the mean, and the interval coverage is increased from 81.5% to 93.7% of the Poisson model.

<!-- b000886 | heading | pages [14] -->
4.5.3 Parameter sensitivity analysis

<!-- b000887 | prose | pages [14, 15] -->
Here we quantify the inﬂuence of the parameter on the gold medal forecast by adjust- ing the parameter values, such as the host effect of the historical weighting coefﬁcient, and calculating its mean difference on the prediction results. For example, here we ﬁx other pa- rameters and increase the historical weighting factor β1 by 10% from the benchmark value to observe the change in the gold forecast. From Figure 16 we can ﬁnd out: the mean devi- ation of the β1 of the historical weighting coefﬁcient is 3.2 gold medals, indicating that the 关注数学模型 model is highly sensitive to the timeliness of historical data, and the mean deviation of the host effect is 2.1, which veriﬁes that home ﬁeld advantage also has a signiﬁcant impact on performance. At the same time, the sensitivity value of the new project is 1.5, and its impact depends on the project ﬁt, but it also has a non-negligible effect on the actual results. At the same time, the sensitivity of the Cold War modiﬁer factor is 0.73. The low sensitivity may be due to the fact that the Cold War effects have weakened over time and their contribution to modern projections is weak, especially for post-1992 data.

<!-- b000888 | furniture | pages [14] -->
2

<!-- b000889 | furniture | pages [14] -->
MATHmodels

<!-- b000890 | furniture | pages [14] -->
获取更多资讯

<!-- b000891 | furniture | pages [15] -->
Team # 2514362

<!-- b000892 | furniture | pages [15] -->
Page 14 of 26

<!-- b000894 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000895 | caption | pages [15] -->
Figure 16: Parameter sensitivity

<!-- b000896 | caption | pages [15] -->
Figure 17: Single Factor Elimination Analysis

<!-- b000897 | heading | pages [15] -->
4.5.4 Ablation Study

<!-- b000898 | prose | pages [15] -->
We performed a ablation study to quantify the importance of various features to the prediction model by removing a feature one by one and calculating the change in the mean absolute error of the model. The larger the value of MAE, the more important it is to indicate 微信号：MATHmodels this feature. As can be seen from the Figure 17, historical data play a dominant role, with the host effect and new projects being of similar importance to the model, both signiﬁcantly higher than the contribution of the Cold War factor. This can be due to the large true coefﬁ- cients of historical data and the high variance of the data generated. However, the host effect and the new project show a certain degree of synergy, which may be due to some overlap in the interpretation of the target variables, and there may also be business coupling, so that the results can be jointly affected.

<!-- b000899 | heading | pages [15] -->
5 Entropy model based on Bayesian Modiﬁcation

<!-- b000900 | heading | pages [15] -->
5.1 Model Selection Background

<!-- b000901 | prose | pages [15] -->
Due to the relatively sparse coach replacement events, especially the low turnover fre- quency of top coaches, the traditional probabilistic model is susceptible to zero-shot distor- tion, so we use Bayesian correction to process sparse data to enhance the stability of small- sample scenarios. The addition of excellent coaches may improve performance quickly in the short term. Therefore, we wanted to identify small but signiﬁcant medal increments with ∆m greater than or equal to 1 by using the abnormal event threshold (T .= 1) to cap- ture the mutation signal brought by the coach. But coaching isn’t the only reason for the improvement. The role of the coach needs to be evaluated in tandem with different factors such as funding, athlete level, etc. Therefore, we chose the information gain (IG) to quantify the independent contribution of individual characteristics to the medals, so as to clarify the relative importance of coaching factors.

<!-- b000902 | prose | pages [15, 16] -->
Our model’s novelty stems from merging information theory (Cover Thomas, 2006) and Bayesian regularization (Kass Raftery, 1995) to address small-sample challenges. From the former, we adopt information gain to rigorously quantify how discrete events (e.g., per- formance anomalies) correlate with medal improvements. From the latter, Laplace smooth- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ing mitigates bias in probability estimation for sparse datasets. This integration creates a m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m transparent yet robust framework, balancing theoretical rigor with practical adaptability- critical for data-scarce sports analytics.

<!-- b000903 | furniture | pages [15] -->
m

<!-- b000904 | furniture | pages [15] -->
m

<!-- b000905 | furniture | pages [15] -->
m

<!-- b000906 | furniture | pages [15] -->
m

<!-- b000907 | furniture | pages [15] -->
m

<!-- b000908 | furniture | pages [15] -->
m

<!-- b000909 | furniture | pages [15] -->
m

<!-- b000910 | furniture | pages [15] -->
m

<!-- b000911 | furniture | pages [15] -->
m

<!-- b000912 | furniture | pages [15] -->
m

<!-- b000913 | furniture | pages [15] -->
m

<!-- b000914 | furniture | pages [15] -->
m

<!-- b000915 | furniture | pages [15] -->
m

<!-- b000916 | furniture | pages [15] -->
m

<!-- b000917 | furniture | pages [15] -->
m

<!-- b000918 | furniture | pages [15] -->
m

<!-- b000919 | furniture | pages [15] -->
m

<!-- b000920 | furniture | pages [15] -->
m

<!-- b000921 | furniture | pages [15] -->
m

<!-- b000922 | furniture | pages [15] -->
m

<!-- b000923 | furniture | pages [15] -->
m

<!-- b000924 | furniture | pages [15] -->
m

<!-- b000925 | furniture | pages [15] -->
m

<!-- b000926 | furniture | pages [15] -->
m

<!-- b000927 | furniture | pages [15] -->
m

<!-- b000928 | furniture | pages [15] -->
m

<!-- b000929 | furniture | pages [15] -->
m

<!-- b000930 | furniture | pages [15] -->
m

<!-- b000931 | furniture | pages [15] -->
m

<!-- b000932 | furniture | pages [15] -->
m

<!-- b000933 | furniture | pages [15] -->
m

<!-- b000934 | furniture | pages [15] -->
m

<!-- b000935 | furniture | pages [15] -->
m

<!-- b000936 | furniture | pages [15] -->
m

<!-- b000937 | furniture | pages [15] -->
m

<!-- b000938 | furniture | pages [15] -->
m

<!-- b000939 | furniture | pages [15] -->
m

<!-- b000940 | furniture | pages [15] -->
m

<!-- b000941 | furniture | pages [15] -->
m

<!-- b000942 | furniture | pages [15] -->
m

<!-- b000943 | furniture | pages [15] -->
m

<!-- b000944 | furniture | pages [15] -->
m

<!-- b000945 | furniture | pages [15] -->
m

<!-- b000946 | furniture | pages [15] -->
m

<!-- b000947 | furniture | pages [15] -->
m

<!-- b000948 | furniture | pages [15] -->
m

<!-- b000949 | furniture | pages [15] -->
m

<!-- b000950 | furniture | pages [15] -->
m

<!-- b000951 | furniture | pages [15] -->
m

<!-- b000952 | furniture | pages [15] -->
m

<!-- b000953 | furniture | pages [15] -->
m

<!-- b000954 | furniture | pages [15] -->
m

<!-- b000955 | furniture | pages [15] -->
m

<!-- b000956 | furniture | pages [15] -->
m

<!-- b000957 | furniture | pages [15] -->
m

<!-- b000958 | furniture | pages [15] -->
m

<!-- b000959 | furniture | pages [15] -->
m

<!-- b000960 | furniture | pages [15] -->
m

<!-- b000961 | furniture | pages [15] -->
m

<!-- b000962 | furniture | pages [15] -->
m

<!-- b000963 | furniture | pages [15] -->
m

<!-- b000964 | furniture | pages [15] -->
m

<!-- b000965 | furniture | pages [15] -->
m

<!-- b000966 | furniture | pages [15] -->
m

<!-- b000967 | furniture | pages [15] -->
m

<!-- b000968 | furniture | pages [15] -->
m

<!-- b000969 | furniture | pages [15] -->
m

<!-- b000970 | furniture | pages [15] -->
m

<!-- b000971 | furniture | pages [15] -->
m

<!-- b000972 | furniture | pages [15] -->
m

<!-- b000973 | furniture | pages [15] -->
m

<!-- b000974 | furniture | pages [15] -->
m

<!-- b000975 | furniture | pages [15] -->
m

<!-- b000976 | furniture | pages [15] -->
m

<!-- b000977 | furniture | pages [15] -->
m

<!-- b000978 | furniture | pages [15] -->
m

<!-- b000979 | furniture | pages [15] -->
m

<!-- b000980 | furniture | pages [15] -->
m

<!-- b000981 | furniture | pages [15] -->
m

<!-- b000982 | furniture | pages [15] -->
m

<!-- b000983 | furniture | pages [15] -->
m

<!-- b000984 | furniture | pages [15] -->
m

<!-- b000985 | furniture | pages [15] -->
m

<!-- b000986 | furniture | pages [15] -->
m

<!-- b000987 | furniture | pages [15] -->
m

<!-- b000988 | furniture | pages [15] -->
m

<!-- b000989 | furniture | pages [15] -->
m

<!-- b000990 | furniture | pages [15] -->
m

<!-- b000991 | furniture | pages [15] -->
m

<!-- b000992 | furniture | pages [15] -->
m

<!-- b000993 | furniture | pages [15] -->
m

<!-- b000994 | furniture | pages [15] -->
m

<!-- b000995 | furniture | pages [15] -->
m

<!-- b000996 | furniture | pages [15] -->
m

<!-- b000997 | furniture | pages [15] -->
m

<!-- b000998 | furniture | pages [15] -->
m

<!-- b000999 | furniture | pages [15] -->
m

<!-- b001000 | furniture | pages [15] -->
m

<!-- b001001 | furniture | pages [15] -->
m

<!-- b001002 | furniture | pages [15] -->
m

<!-- b001003 | furniture | pages [15] -->
m

<!-- b001004 | furniture | pages [15] -->
m

<!-- b001005 | furniture | pages [15] -->
m

<!-- b001006 | furniture | pages [15] -->
m

<!-- b001007 | furniture | pages [15] -->
m

<!-- b001008 | furniture | pages [15] -->
m

<!-- b001009 | furniture | pages [15] -->
m

<!-- b001010 | furniture | pages [15] -->
m

<!-- b001011 | furniture | pages [15] -->
m

<!-- b001012 | furniture | pages [15] -->
m

<!-- b001013 | furniture | pages [15] -->
m

<!-- b001014 | furniture | pages [15] -->
m

<!-- b001015 | furniture | pages [15] -->
m

<!-- b001016 | furniture | pages [15] -->
m

<!-- b001017 | furniture | pages [15] -->
m

<!-- b001018 | furniture | pages [15] -->
m

<!-- b001019 | furniture | pages [15] -->
m

<!-- b001020 | furniture | pages [15] -->
m

<!-- b001021 | furniture | pages [15] -->
m

<!-- b001022 | furniture | pages [15] -->
m

<!-- b001023 | furniture | pages [15] -->
m

<!-- b001024 | furniture | pages [15] -->
m

<!-- b001025 | furniture | pages [15] -->
m

<!-- b001026 | furniture | pages [15] -->
m

<!-- b001027 | furniture | pages [15] -->
m

<!-- b001028 | furniture | pages [15] -->
m

<!-- b001029 | furniture | pages [15] -->
m

<!-- b001030 | furniture | pages [15] -->
m

<!-- b001031 | furniture | pages [15] -->
m

<!-- b001032 | furniture | pages [15] -->
m

<!-- b001033 | furniture | pages [15] -->
m

<!-- b001034 | furniture | pages [15] -->
m

<!-- b001035 | furniture | pages [15] -->
m

<!-- b001036 | furniture | pages [15] -->
m

<!-- b001037 | furniture | pages [15] -->
m

<!-- b001038 | furniture | pages [15] -->
m

<!-- b001039 | furniture | pages [15] -->
m

<!-- b001040 | furniture | pages [15] -->
m

<!-- b001041 | furniture | pages [15] -->
m

<!-- b001042 | furniture | pages [15] -->
m

<!-- b001043 | furniture | pages [15] -->
m

<!-- b001044 | furniture | pages [15] -->
m

<!-- b001045 | furniture | pages [15] -->
m

<!-- b001046 | furniture | pages [15] -->
m

<!-- b001047 | furniture | pages [15] -->
m

<!-- b001048 | furniture | pages [15] -->
m

<!-- b001049 | furniture | pages [15] -->
m

<!-- b001050 | furniture | pages [15] -->
m

<!-- b001051 | furniture | pages [15] -->
m

<!-- b001052 | furniture | pages [15] -->
m

<!-- b001053 | furniture | pages [15] -->
m

<!-- b001054 | furniture | pages [15] -->
m

<!-- b001055 | furniture | pages [15] -->
m

<!-- b001056 | furniture | pages [15] -->
m

<!-- b001057 | furniture | pages [15] -->
m

<!-- b001058 | furniture | pages [15] -->
m

<!-- b001059 | furniture | pages [15] -->
m

<!-- b001060 | furniture | pages [15] -->
m

<!-- b001061 | furniture | pages [15] -->
m

<!-- b001062 | furniture | pages [15] -->
m

<!-- b001063 | furniture | pages [15] -->
m

<!-- b001064 | furniture | pages [15] -->
m

<!-- b001065 | furniture | pages [15] -->
m

<!-- b001066 | furniture | pages [15] -->
m

<!-- b001067 | furniture | pages [15] -->
m

<!-- b001068 | furniture | pages [15] -->
m

<!-- b001069 | furniture | pages [15] -->
m

<!-- b001070 | furniture | pages [15] -->
m

<!-- b001071 | furniture | pages [15] -->
m

<!-- b001072 | furniture | pages [15] -->
m

<!-- b001073 | furniture | pages [15] -->
m

<!-- b001074 | furniture | pages [15] -->
m

<!-- b001075 | furniture | pages [15] -->
m

<!-- b001076 | furniture | pages [15] -->
m

<!-- b001077 | furniture | pages [15] -->
m

<!-- b001078 | furniture | pages [15] -->
m

<!-- b001079 | furniture | pages [15] -->
m

<!-- b001080 | furniture | pages [15] -->
m

<!-- b001081 | furniture | pages [15] -->
m

<!-- b001082 | furniture | pages [15] -->
m

<!-- b001083 | furniture | pages [15] -->
m

<!-- b001084 | furniture | pages [15] -->
m

<!-- b001085 | furniture | pages [15] -->
m

<!-- b001086 | furniture | pages [15] -->
m

<!-- b001087 | furniture | pages [15] -->
m

<!-- b001088 | furniture | pages [15] -->
m

<!-- b001089 | furniture | pages [15] -->
m

<!-- b001090 | furniture | pages [15] -->
m

<!-- b001091 | furniture | pages [15] -->
m

<!-- b001092 | furniture | pages [15] -->
m

<!-- b001093 | furniture | pages [15] -->
m

<!-- b001094 | furniture | pages [15] -->
m

<!-- b001095 | furniture | pages [15] -->
m

<!-- b001096 | furniture | pages [15] -->
m

<!-- b001097 | furniture | pages [15] -->
m

<!-- b001098 | furniture | pages [15] -->
m

<!-- b001099 | furniture | pages [15] -->
m

<!-- b001100 | furniture | pages [15] -->
m

<!-- b001101 | furniture | pages [15] -->
m

<!-- b001102 | furniture | pages [15] -->
m

<!-- b001103 | furniture | pages [15] -->
m

<!-- b001104 | furniture | pages [15] -->
m

<!-- b001105 | furniture | pages [15] -->
m

<!-- b001106 | furniture | pages [15] -->
m

<!-- b001107 | furniture | pages [15] -->
m

<!-- b001108 | furniture | pages [15] -->
m

<!-- b001109 | furniture | pages [15] -->
m

<!-- b001110 | furniture | pages [15] -->
m

<!-- b001111 | furniture | pages [15] -->
m

<!-- b001112 | furniture | pages [15] -->
m

<!-- b001113 | furniture | pages [15] -->
m

<!-- b001114 | furniture | pages [15] -->
m

<!-- b001115 | furniture | pages [15] -->
m

<!-- b001116 | furniture | pages [15] -->
m

<!-- b001117 | furniture | pages [15] -->
m

<!-- b001118 | furniture | pages [15] -->
m

<!-- b001119 | furniture | pages [15] -->
m

<!-- b001120 | furniture | pages [15] -->
m

<!-- b001121 | furniture | pages [15] -->
m

<!-- b001122 | furniture | pages [15] -->
m

<!-- b001123 | furniture | pages [15] -->
m

<!-- b001124 | furniture | pages [15] -->
m

<!-- b001125 | furniture | pages [15] -->
m

<!-- b001126 | furniture | pages [15] -->
m

<!-- b001127 | furniture | pages [15] -->
m

<!-- b001128 | furniture | pages [15] -->
m

<!-- b001129 | furniture | pages [15] -->
m

<!-- b001130 | furniture | pages [15] -->
m

<!-- b001131 | furniture | pages [15] -->
m

<!-- b001132 | furniture | pages [15] -->
m

<!-- b001133 | furniture | pages [15] -->
m

<!-- b001134 | furniture | pages [15] -->
m

<!-- b001135 | furniture | pages [15] -->
m

<!-- b001136 | furniture | pages [15] -->
m

<!-- b001137 | furniture | pages [15] -->
m

<!-- b001138 | furniture | pages [15] -->
m

<!-- b001139 | furniture | pages [15] -->
m

<!-- b001140 | furniture | pages [15] -->
m

<!-- b001141 | furniture | pages [15] -->
m

<!-- b001142 | furniture | pages [15] -->
m

<!-- b001143 | furniture | pages [15] -->
m

<!-- b001144 | furniture | pages [15] -->
m

<!-- b001145 | furniture | pages [15] -->
m

<!-- b001146 | furniture | pages [15] -->
m

<!-- b001147 | furniture | pages [15] -->
m

<!-- b001148 | furniture | pages [15] -->
m

<!-- b001149 | furniture | pages [15] -->
m

<!-- b001150 | furniture | pages [15] -->
m

<!-- b001151 | furniture | pages [15] -->
m

<!-- b001152 | furniture | pages [15] -->
m

<!-- b001153 | furniture | pages [15] -->
m

<!-- b001154 | furniture | pages [15] -->
m

<!-- b001155 | furniture | pages [15] -->
m

<!-- b001156 | furniture | pages [15] -->
m

<!-- b001157 | furniture | pages [15] -->
m

<!-- b001158 | furniture | pages [15] -->
m

<!-- b001159 | furniture | pages [15] -->
m

<!-- b001160 | furniture | pages [15] -->
m

<!-- b001161 | furniture | pages [15] -->
m

<!-- b001162 | furniture | pages [15] -->
m

<!-- b001163 | furniture | pages [15] -->
m

<!-- b001164 | furniture | pages [15] -->
m

<!-- b001165 | furniture | pages [15] -->
m

<!-- b001166 | furniture | pages [15] -->
m

<!-- b001167 | furniture | pages [15] -->
m

<!-- b001168 | furniture | pages [15] -->
m

<!-- b001169 | furniture | pages [15] -->
m

<!-- b001170 | furniture | pages [15] -->
m

<!-- b001171 | furniture | pages [15] -->
m

<!-- b001172 | furniture | pages [15] -->
m

<!-- b001173 | furniture | pages [15] -->
m

<!-- b001174 | furniture | pages [15] -->
m

<!-- b001175 | furniture | pages [15] -->
m

<!-- b001176 | furniture | pages [15] -->
m

<!-- b001177 | furniture | pages [15] -->
m

<!-- b001178 | furniture | pages [15] -->
m

<!-- b001179 | furniture | pages [15] -->
m

<!-- b001180 | furniture | pages [15] -->
m

<!-- b001181 | furniture | pages [15] -->
m

<!-- b001182 | furniture | pages [15] -->
m

<!-- b001183 | furniture | pages [15] -->
m

<!-- b001184 | furniture | pages [15] -->
m

<!-- b001185 | furniture | pages [15] -->
m

<!-- b001186 | furniture | pages [15] -->
m

<!-- b001187 | furniture | pages [15] -->
m

<!-- b001188 | furniture | pages [15] -->
m

<!-- b001189 | furniture | pages [15] -->
m

<!-- b001190 | furniture | pages [15] -->
m

<!-- b001191 | furniture | pages [15] -->
m

<!-- b001192 | furniture | pages [15] -->
m

<!-- b001193 | furniture | pages [15] -->
m

<!-- b001194 | furniture | pages [15] -->
m

<!-- b001195 | furniture | pages [15] -->
m

<!-- b001196 | furniture | pages [15] -->
m

<!-- b001197 | furniture | pages [15] -->
m

<!-- b001198 | furniture | pages [15] -->
m

<!-- b001199 | furniture | pages [15] -->
m

<!-- b001200 | furniture | pages [15] -->
m

<!-- b001201 | furniture | pages [15] -->
m

<!-- b001202 | furniture | pages [15] -->
m

<!-- b001203 | furniture | pages [15] -->
m

<!-- b001204 | furniture | pages [15] -->
m

<!-- b001205 | furniture | pages [15] -->
m

<!-- b001206 | furniture | pages [15] -->
m

<!-- b001207 | furniture | pages [15] -->
m

<!-- b001208 | furniture | pages [15] -->
m

<!-- b001209 | furniture | pages [15] -->
m

<!-- b001210 | furniture | pages [15] -->
m

<!-- b001211 | furniture | pages [15] -->
m

<!-- b001212 | furniture | pages [15] -->
m

<!-- b001213 | furniture | pages [15] -->
m

<!-- b001214 | furniture | pages [15] -->
m

<!-- b001215 | furniture | pages [15] -->
m

<!-- b001216 | furniture | pages [15] -->
m

<!-- b001217 | furniture | pages [15] -->
m

<!-- b001218 | furniture | pages [15] -->
m

<!-- b001219 | furniture | pages [15] -->
m

<!-- b001220 | furniture | pages [15] -->
m

<!-- b001221 | furniture | pages [15] -->
m

<!-- b001222 | furniture | pages [15] -->
m

<!-- b001223 | furniture | pages [15] -->
m

<!-- b001224 | furniture | pages [15] -->
m

<!-- b001225 | furniture | pages [15] -->
m

<!-- b001226 | furniture | pages [15] -->
m

<!-- b001227 | furniture | pages [16] -->
Team # 2514362

<!-- b001228 | furniture | pages [16] -->
Page 15 of 26

<!-- b001230 | heading | pages [16] -->
5.2 The Establishment of the Mathematical Model

<!-- b001231 | prose | pages [16] -->
We extract the number of medals won in the past year for the country-sport combination from the ﬁle and calculate medal increments ∆Mc,s,t at four-year intervals, skipping the calculation if the data for the ﬁrst four years is missing. The medal increment is deﬁned as:

<!-- b001232 | prose | pages [16] -->
∆Mc,s,t = Mc,s,t −Mc,s,t−4, (13)

<!-- b001233 | prose | pages [16] -->
where Mc,s,t represents the number of medals won by country c in sport s at time t.

<!-- b001234 | prose | pages [16] -->
Deﬁnition of Abnormal Progress Events

<!-- b001235 | prose | pages [16] -->
To identify signiﬁcant progress, we deﬁne a binary variable Xc,s,t to mark "abnormal progress events":

<!-- b001236 | prose | pages [16] -->
{ if ∆Mc,s,t ≥1, 1, Xc,s,t = (14) 0, otherwise.

<!-- b001237 | prose | pages [16] -->
This variable helps screen out cases of signiﬁcant progress in medal counts.

<!-- b001238 | prose | pages [16] -->
Bayesian Correction for Small Sample Probability Estimation

<!-- b001239 | prose | pages [16] -->
To address the bias in small sample probability estimation, we introduce Bayesian cor- rection with Laplacian smoothing. The probability of progress Pprogress is calculated as:

<!-- b001240 | prose | pages [16] -->
Pprogress = Progressive sample number + 1 . (15) Total sample number + 2

<!-- b001241 | prose | pages [16] -->
The probability of non-progress Pnon-progress is derived as:

<!-- b001242 | prose | pages [16] -->
Pnon-progress = 1 −Pprogress. (16)

<!-- b001243 | prose | pages [16] -->
Entropy and Conditional Entropy

<!-- b001244 | prose | pages [16] -->
The total entropy H(M) of medal increment is calculated to measure the uncertainty of medal growth:

<!-- b001245 | prose | pages [16] -->
( ) H(M) = − Pprogress log2 Pprogress + Pnon-progress log2 Pnon-progress . (17)

<!-- b001246 | prose | pages [16] -->
Next, the conditional entropy H(M | X) is computed to quantify the uncertainty of medal increment given the occurrence of abnormal events X:

<!-- b001247 | prose | pages [16] -->
(Nx + 1 ) ( ∑ ) H(M | X) = − Pprogress|x log2 Pprogress|x + Pnon-progress|x log2 Pnon-progress|x , N + 2 x∈{0,1} (18)

<!-- b001248 | prose | pages [16] -->
where Nx is the number of samples with X = x, and N is the total number of samples.

<!-- b001249 | prose | pages [16, 17] -->
关注数学模型 Information Gain

<!-- b001250 | furniture | pages [16] -->
2

<!-- b001251 | furniture | pages [16] -->
MATHmodels

<!-- b001252 | furniture | pages [16] -->
获取更多资讯

<!-- b001253 | furniture | pages [17] -->
Team # 2514362

<!-- b001254 | furniture | pages [17] -->
Page 16 of 26

<!-- b001256 | prose | pages [17] -->
The information gain IG quantiﬁes the association between abnormal events and medal progress. It is deﬁned as:

<!-- b001257 | prose | pages [17] -->
IG = H(M) −H(M | X). (19)

<!-- b001258 | prose | pages [17] -->
A positive IG indicates a signiﬁcant relationship between abnormal events and medal progress.

<!-- b001259 | prose | pages [17] -->
Effect Quantiﬁcation 微信公众号：数学模型 To evaluate the impact of abnormal events, we deﬁne the "effect intensity" as the ratio of the average medal increment of the abnormal event group to the average increment of the whole sample:

<!-- b001260 | prose | pages [17] -->
Average ∆Mc,s,t for X = 1 Effect Intensity = Average ∆Mc,s,t for all samples. (20)

<!-- b001261 | prose | pages [17] -->
If the effect intensity is greater than 1, the positive effect is considered signiﬁcant.

<!-- b001262 | prose | pages [17] -->
Potential Score 微信号：MATHmodels A "potential score" Sc,s is designed to prioritize country-sport combinations with high potential for improvement. It combines information gain IG and the gap between the cur- rent medal count and the historical peak:

<!-- b001263 | prose | pages [17] -->
( ) 1 −M current c,s Sc,s = IGc,s × , (21) M max c,s

<!-- b001264 | prose | pages [17] -->
where M current is the current medal count and M max is the historical peak medal count c,s c,s for country c in sport s.

<!-- b001265 | heading | pages [17] -->
5.3 Case Analysis

<!-- b001266 | prose | pages [17] -->
It’s shown that great coach effect truly has an impact on country’s performing in certain events. Here are examples to analyze. While coaching the U.S. Women’s Volleyball team from 2005 to 2008, Lang led the team to win three medals at the 2008 Beijing Olympics, an increase from one medal in 2004 ( ∆M .= 2 ), and an information gain ( IG .= 0.45 ) that met the criteria of "Great coach effect" ( ∆M ⩾1 and IG > 0.3 ). When she coached the Chinese Women’s Volleyball Team from 2013 to 2020, she led the team to increase the number of .= 3, IG .= 0.62 ), MEDALS from 0 in 2012 to 3 in the 2016 Rio Olympic Games ( ∆M signiﬁcantly exceeding the model threshold; However, the number of medals won at the 2020 Tokyo Olympics did not increase ( ∆M .= 0 ), and no coaching effect was detected. The results of the model are consistent with its historical achievements, highlighting the key role of coaching in improving both Chinese and American teams.

<!-- b001267 | prose | pages [17, 18] -->
Bela Karoli coached the Romanian gymnastics team from 1976 to 1981, helping the team achieve an increase of 4 medals ( ∆M .= 4, IG .= 0.52 ) at the 1976 Montreal Olympics, in line with the "Great coach effect" ; Medal growth at the 1980 Moscow Olympics slowed ( .= 1, IG = 0.30 ), approaching the boundary. From 1991-2016, he coached the U.S. ∆M Women’s gymnastics team, increasing its medal tally from 3 in 1992 to 9 ( ∆M .= 6, IG .= 0.68 ) at the 1996 Atlanta Olympics and 12 ( ∆M .= 3, IG = 0.41 ) at the 2016 Rio Olympics. The m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m model veriﬁed his breakthrough contribution to the number of medals during his coaching m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m in the two countries, and reﬂected the excellent coaching ability across times and regions. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m In addition to the two well-known coaches mentioned above, we also analyzed and validated the estimated results of the model with historical data, some of which are shown in the Table 3.

<!-- b001268 | furniture | pages [17] -->
m

<!-- b001269 | furniture | pages [17] -->
m

<!-- b001270 | furniture | pages [17] -->
m

<!-- b001271 | furniture | pages [17] -->
m

<!-- b001272 | furniture | pages [17] -->
m

<!-- b001273 | furniture | pages [17] -->
m

<!-- b001274 | furniture | pages [17] -->
m

<!-- b001275 | furniture | pages [17] -->
m

<!-- b001276 | furniture | pages [17] -->
m

<!-- b001277 | furniture | pages [17] -->
m

<!-- b001278 | furniture | pages [17] -->
m

<!-- b001279 | furniture | pages [17] -->
m

<!-- b001280 | furniture | pages [17] -->
m

<!-- b001281 | furniture | pages [17] -->
m

<!-- b001282 | furniture | pages [17] -->
m

<!-- b001283 | furniture | pages [17] -->
m

<!-- b001284 | furniture | pages [17] -->
m

<!-- b001285 | furniture | pages [17] -->
m

<!-- b001286 | furniture | pages [17] -->
m

<!-- b001287 | furniture | pages [17] -->
m

<!-- b001288 | furniture | pages [17] -->
m

<!-- b001289 | furniture | pages [17] -->
m

<!-- b001290 | furniture | pages [17] -->
m

<!-- b001291 | furniture | pages [17] -->
m

<!-- b001292 | furniture | pages [17] -->
m

<!-- b001293 | furniture | pages [17] -->
m

<!-- b001294 | furniture | pages [17] -->
m

<!-- b001295 | furniture | pages [17] -->
m

<!-- b001296 | furniture | pages [17] -->
m

<!-- b001297 | furniture | pages [17] -->
m

<!-- b001298 | furniture | pages [17] -->
m

<!-- b001299 | furniture | pages [17] -->
m

<!-- b001300 | furniture | pages [17] -->
m

<!-- b001301 | furniture | pages [17] -->
m

<!-- b001302 | furniture | pages [17] -->
m

<!-- b001303 | furniture | pages [17] -->
m

<!-- b001304 | furniture | pages [17] -->
m

<!-- b001305 | furniture | pages [17] -->
m

<!-- b001306 | furniture | pages [17] -->
m

<!-- b001307 | furniture | pages [17] -->
m

<!-- b001308 | furniture | pages [17] -->
m

<!-- b001309 | furniture | pages [17] -->
m

<!-- b001310 | furniture | pages [17] -->
m

<!-- b001311 | furniture | pages [17] -->
m

<!-- b001312 | furniture | pages [17] -->
m

<!-- b001313 | furniture | pages [17] -->
m

<!-- b001314 | furniture | pages [17] -->
m

<!-- b001315 | furniture | pages [17] -->
m

<!-- b001316 | furniture | pages [17] -->
m

<!-- b001317 | furniture | pages [17] -->
m

<!-- b001318 | furniture | pages [17] -->
m

<!-- b001319 | furniture | pages [17] -->
m

<!-- b001320 | furniture | pages [17] -->
m

<!-- b001321 | furniture | pages [17] -->
m

<!-- b001322 | furniture | pages [17] -->
m

<!-- b001323 | furniture | pages [17] -->
m

<!-- b001324 | furniture | pages [17] -->
m

<!-- b001325 | furniture | pages [17] -->
m

<!-- b001326 | furniture | pages [17] -->
m

<!-- b001327 | furniture | pages [17] -->
m

<!-- b001328 | furniture | pages [17] -->
m

<!-- b001329 | furniture | pages [17] -->
m

<!-- b001330 | furniture | pages [17] -->
m

<!-- b001331 | furniture | pages [17] -->
m

<!-- b001332 | furniture | pages [17] -->
m

<!-- b001333 | furniture | pages [17] -->
m

<!-- b001334 | furniture | pages [17] -->
m

<!-- b001335 | furniture | pages [17] -->
m

<!-- b001336 | furniture | pages [17] -->
m

<!-- b001337 | furniture | pages [17] -->
m

<!-- b001338 | furniture | pages [17] -->
m

<!-- b001339 | furniture | pages [17] -->
m

<!-- b001340 | furniture | pages [17] -->
m

<!-- b001341 | furniture | pages [17] -->
m

<!-- b001342 | furniture | pages [17] -->
m

<!-- b001343 | furniture | pages [17] -->
m

<!-- b001344 | furniture | pages [17] -->
m

<!-- b001345 | furniture | pages [17] -->
m

<!-- b001346 | furniture | pages [17] -->
m

<!-- b001347 | furniture | pages [17] -->
m

<!-- b001348 | furniture | pages [17] -->
m

<!-- b001349 | furniture | pages [17] -->
m

<!-- b001350 | furniture | pages [17] -->
m

<!-- b001351 | furniture | pages [17] -->
m

<!-- b001352 | furniture | pages [17] -->
m

<!-- b001353 | furniture | pages [17] -->
m

<!-- b001354 | furniture | pages [17] -->
m

<!-- b001355 | furniture | pages [17] -->
m

<!-- b001356 | furniture | pages [17] -->
m

<!-- b001357 | furniture | pages [17] -->
m

<!-- b001358 | furniture | pages [17] -->
m

<!-- b001359 | furniture | pages [17] -->
m

<!-- b001360 | furniture | pages [17] -->
m

<!-- b001361 | furniture | pages [17] -->
m

<!-- b001362 | furniture | pages [17] -->
m

<!-- b001363 | furniture | pages [17] -->
m

<!-- b001364 | furniture | pages [17] -->
m

<!-- b001365 | furniture | pages [17] -->
m

<!-- b001366 | furniture | pages [17] -->
m

<!-- b001367 | furniture | pages [17] -->
m

<!-- b001368 | furniture | pages [17] -->
m

<!-- b001369 | furniture | pages [17] -->
m

<!-- b001370 | furniture | pages [17] -->
m

<!-- b001371 | furniture | pages [17] -->
m

<!-- b001372 | furniture | pages [17] -->
m

<!-- b001373 | furniture | pages [17] -->
m

<!-- b001374 | furniture | pages [17] -->
m

<!-- b001375 | furniture | pages [17] -->
m

<!-- b001376 | furniture | pages [17] -->
m

<!-- b001377 | furniture | pages [17] -->
m

<!-- b001378 | furniture | pages [17] -->
m

<!-- b001379 | furniture | pages [17] -->
m

<!-- b001380 | furniture | pages [17] -->
m

<!-- b001381 | furniture | pages [17] -->
m

<!-- b001382 | furniture | pages [17] -->
m

<!-- b001383 | furniture | pages [17] -->
m

<!-- b001384 | furniture | pages [17] -->
m

<!-- b001385 | furniture | pages [17] -->
m

<!-- b001386 | furniture | pages [17] -->
m

<!-- b001387 | furniture | pages [17] -->
m

<!-- b001388 | furniture | pages [17] -->
m

<!-- b001389 | furniture | pages [17] -->
m

<!-- b001390 | furniture | pages [17] -->
m

<!-- b001391 | furniture | pages [17] -->
m

<!-- b001392 | furniture | pages [17] -->
m

<!-- b001393 | furniture | pages [17] -->
m

<!-- b001394 | furniture | pages [17] -->
m

<!-- b001395 | furniture | pages [17] -->
m

<!-- b001396 | furniture | pages [17] -->
m

<!-- b001397 | furniture | pages [17] -->
m

<!-- b001398 | furniture | pages [17] -->
m

<!-- b001399 | furniture | pages [17] -->
m

<!-- b001400 | furniture | pages [17] -->
m

<!-- b001401 | furniture | pages [17] -->
m

<!-- b001402 | furniture | pages [17] -->
m

<!-- b001403 | furniture | pages [17] -->
m

<!-- b001404 | furniture | pages [17] -->
m

<!-- b001405 | furniture | pages [17] -->
m

<!-- b001406 | furniture | pages [17] -->
m

<!-- b001407 | furniture | pages [17] -->
m

<!-- b001408 | furniture | pages [17] -->
m

<!-- b001409 | furniture | pages [17] -->
m

<!-- b001410 | furniture | pages [17] -->
m

<!-- b001411 | furniture | pages [17] -->
m

<!-- b001412 | furniture | pages [17] -->
m

<!-- b001413 | furniture | pages [17] -->
m

<!-- b001414 | furniture | pages [17] -->
m

<!-- b001415 | furniture | pages [17] -->
m

<!-- b001416 | furniture | pages [17] -->
m

<!-- b001417 | furniture | pages [17] -->
m

<!-- b001418 | furniture | pages [17] -->
m

<!-- b001419 | furniture | pages [17] -->
m

<!-- b001420 | furniture | pages [17] -->
m

<!-- b001421 | furniture | pages [17] -->
m

<!-- b001422 | furniture | pages [17] -->
m

<!-- b001423 | furniture | pages [17] -->
m

<!-- b001424 | furniture | pages [17] -->
m

<!-- b001425 | furniture | pages [17] -->
m

<!-- b001426 | furniture | pages [17] -->
m

<!-- b001427 | furniture | pages [17] -->
m

<!-- b001428 | furniture | pages [17] -->
m

<!-- b001429 | furniture | pages [17] -->
m

<!-- b001430 | furniture | pages [17] -->
m

<!-- b001431 | furniture | pages [17] -->
m

<!-- b001432 | furniture | pages [17] -->
m

<!-- b001433 | furniture | pages [17] -->
m

<!-- b001434 | furniture | pages [17] -->
m

<!-- b001435 | furniture | pages [17] -->
m

<!-- b001436 | furniture | pages [17] -->
m

<!-- b001437 | furniture | pages [17] -->
m

<!-- b001438 | furniture | pages [17] -->
m

<!-- b001439 | furniture | pages [17] -->
m

<!-- b001440 | furniture | pages [17] -->
m

<!-- b001441 | furniture | pages [17] -->
m

<!-- b001442 | furniture | pages [17] -->
m

<!-- b001443 | furniture | pages [17] -->
m

<!-- b001444 | furniture | pages [17] -->
m

<!-- b001445 | furniture | pages [17] -->
m

<!-- b001446 | furniture | pages [17] -->
m

<!-- b001447 | furniture | pages [17] -->
m

<!-- b001448 | furniture | pages [17] -->
m

<!-- b001449 | furniture | pages [17] -->
m

<!-- b001450 | furniture | pages [17] -->
m

<!-- b001451 | furniture | pages [17] -->
m

<!-- b001452 | furniture | pages [17] -->
m

<!-- b001453 | furniture | pages [17] -->
m

<!-- b001454 | furniture | pages [17] -->
m

<!-- b001455 | furniture | pages [17] -->
m

<!-- b001456 | furniture | pages [17] -->
m

<!-- b001457 | furniture | pages [17] -->
m

<!-- b001458 | furniture | pages [17] -->
m

<!-- b001459 | furniture | pages [17] -->
m

<!-- b001460 | furniture | pages [17] -->
m

<!-- b001461 | furniture | pages [17] -->
m

<!-- b001462 | furniture | pages [17] -->
m

<!-- b001463 | furniture | pages [17] -->
m

<!-- b001464 | furniture | pages [17] -->
m

<!-- b001465 | furniture | pages [17] -->
m

<!-- b001466 | furniture | pages [17] -->
m

<!-- b001467 | furniture | pages [17] -->
m

<!-- b001468 | furniture | pages [17] -->
m

<!-- b001469 | furniture | pages [17] -->
m

<!-- b001470 | furniture | pages [17] -->
m

<!-- b001471 | furniture | pages [17] -->
m

<!-- b001472 | furniture | pages [17] -->
m

<!-- b001473 | furniture | pages [17] -->
m

<!-- b001474 | furniture | pages [17] -->
m

<!-- b001475 | furniture | pages [17] -->
m

<!-- b001476 | furniture | pages [17] -->
m

<!-- b001477 | furniture | pages [17] -->
m

<!-- b001478 | furniture | pages [17] -->
m

<!-- b001479 | furniture | pages [17] -->
m

<!-- b001480 | furniture | pages [17] -->
m

<!-- b001481 | furniture | pages [17] -->
m

<!-- b001482 | furniture | pages [17] -->
m

<!-- b001483 | furniture | pages [17] -->
m

<!-- b001484 | furniture | pages [17] -->
m

<!-- b001485 | furniture | pages [17] -->
m

<!-- b001486 | furniture | pages [17] -->
m

<!-- b001487 | furniture | pages [17] -->
m

<!-- b001488 | furniture | pages [17] -->
m

<!-- b001489 | furniture | pages [17] -->
m

<!-- b001490 | furniture | pages [17] -->
m

<!-- b001491 | furniture | pages [17] -->
m

<!-- b001492 | furniture | pages [17] -->
m

<!-- b001493 | furniture | pages [17] -->
m

<!-- b001494 | furniture | pages [17] -->
m

<!-- b001495 | furniture | pages [17] -->
m

<!-- b001496 | furniture | pages [17] -->
m

<!-- b001497 | furniture | pages [17] -->
m

<!-- b001498 | furniture | pages [17] -->
m

<!-- b001499 | furniture | pages [17] -->
m

<!-- b001500 | furniture | pages [17] -->
m

<!-- b001501 | furniture | pages [17] -->
m

<!-- b001502 | furniture | pages [17] -->
m

<!-- b001503 | furniture | pages [17] -->
m

<!-- b001504 | furniture | pages [17] -->
m

<!-- b001505 | furniture | pages [17] -->
m

<!-- b001506 | furniture | pages [17] -->
m

<!-- b001507 | furniture | pages [17] -->
m

<!-- b001508 | furniture | pages [17] -->
m

<!-- b001509 | furniture | pages [17] -->
m

<!-- b001510 | furniture | pages [17] -->
m

<!-- b001511 | furniture | pages [17] -->
m

<!-- b001512 | furniture | pages [17] -->
m

<!-- b001513 | furniture | pages [17] -->
m

<!-- b001514 | furniture | pages [17] -->
m

<!-- b001515 | furniture | pages [17] -->
m

<!-- b001516 | furniture | pages [17] -->
m

<!-- b001517 | furniture | pages [17] -->
m

<!-- b001518 | furniture | pages [17] -->
m

<!-- b001519 | furniture | pages [17] -->
m

<!-- b001520 | furniture | pages [17] -->
m

<!-- b001521 | furniture | pages [17] -->
m

<!-- b001522 | furniture | pages [17] -->
m

<!-- b001523 | furniture | pages [17] -->
m

<!-- b001524 | furniture | pages [17] -->
m

<!-- b001525 | furniture | pages [17] -->
m

<!-- b001526 | furniture | pages [17] -->
m

<!-- b001527 | furniture | pages [17] -->
m

<!-- b001528 | furniture | pages [17] -->
m

<!-- b001529 | furniture | pages [17] -->
m

<!-- b001530 | furniture | pages [17] -->
m

<!-- b001531 | furniture | pages [17] -->
m

<!-- b001532 | furniture | pages [17] -->
m

<!-- b001533 | furniture | pages [17] -->
m

<!-- b001534 | furniture | pages [17] -->
m

<!-- b001535 | furniture | pages [17] -->
m

<!-- b001536 | furniture | pages [17] -->
m

<!-- b001537 | furniture | pages [17] -->
m

<!-- b001538 | furniture | pages [17] -->
m

<!-- b001539 | furniture | pages [17] -->
m

<!-- b001540 | furniture | pages [17] -->
m

<!-- b001541 | furniture | pages [17] -->
m

<!-- b001542 | furniture | pages [17] -->
m

<!-- b001543 | furniture | pages [17] -->
m

<!-- b001544 | furniture | pages [17] -->
m

<!-- b001545 | furniture | pages [17] -->
m

<!-- b001546 | furniture | pages [17] -->
m

<!-- b001547 | furniture | pages [17] -->
m

<!-- b001548 | furniture | pages [17] -->
m

<!-- b001549 | furniture | pages [17] -->
m

<!-- b001550 | furniture | pages [17] -->
m

<!-- b001551 | furniture | pages [17] -->
m

<!-- b001552 | furniture | pages [17] -->
m

<!-- b001553 | furniture | pages [17] -->
m

<!-- b001554 | furniture | pages [17] -->
m

<!-- b001555 | furniture | pages [17] -->
m

<!-- b001556 | furniture | pages [17] -->
m

<!-- b001557 | furniture | pages [17] -->
m

<!-- b001558 | furniture | pages [17] -->
m

<!-- b001559 | furniture | pages [17] -->
m

<!-- b001560 | furniture | pages [17] -->
m

<!-- b001561 | furniture | pages [17] -->
m

<!-- b001562 | furniture | pages [17] -->
m

<!-- b001563 | furniture | pages [17] -->
m

<!-- b001564 | furniture | pages [17] -->
m

<!-- b001565 | furniture | pages [17] -->
m

<!-- b001566 | furniture | pages [17] -->
m

<!-- b001567 | furniture | pages [17] -->
m

<!-- b001568 | furniture | pages [17] -->
m

<!-- b001569 | furniture | pages [17] -->
m

<!-- b001570 | furniture | pages [17] -->
m

<!-- b001571 | furniture | pages [17] -->
m

<!-- b001572 | furniture | pages [17] -->
m

<!-- b001573 | furniture | pages [17] -->
m

<!-- b001574 | furniture | pages [17] -->
m

<!-- b001575 | furniture | pages [17] -->
m

<!-- b001576 | furniture | pages [17] -->
m

<!-- b001577 | furniture | pages [17] -->
m

<!-- b001578 | furniture | pages [17] -->
m

<!-- b001579 | furniture | pages [17] -->
m

<!-- b001580 | furniture | pages [17] -->
m

<!-- b001581 | furniture | pages [17] -->
m

<!-- b001582 | furniture | pages [17] -->
m

<!-- b001583 | furniture | pages [17] -->
m

<!-- b001584 | furniture | pages [17] -->
m

<!-- b001585 | furniture | pages [17] -->
m

<!-- b001586 | furniture | pages [17] -->
m

<!-- b001587 | furniture | pages [17] -->
m

<!-- b001588 | furniture | pages [17] -->
m

<!-- b001589 | furniture | pages [17] -->
m

<!-- b001590 | furniture | pages [17] -->
m

<!-- b001591 | furniture | pages [17] -->
m

<!-- b001592 | furniture | pages [18] -->
Page 17 of 26

<!-- b001593 | furniture | pages [18] -->
Team # 2514362

<!-- b001595 | prose | pages [18] -->
Country-Year Model Recommended Events Actual Matched Events Coach Effect Evidence Matching Score Clear (Coaching system innovation) AUS-2000 Swimming, Cycling Swimming, Cycling ★☆⭐☆★ Volleyball BRA-2008 Volleyball Clear (Golden era initiation) ⭐食女⭐商 AUS-2020 Skateboarding, Canoeing Skateboarding, Canoeing Clear (New events/strategy optimization) ★女女女★ ★⭐⭐食★ ARG-2004 Basketball, Football Basketball, Football Clear (Tactical breakthrough) Weightlifting Weightlifting BUL-1980 Clear (Training method revolution) 古古古古☆ Athletics CAN-1904 Athletics ★★★☆☆ Partial (Incomplete records) Rowing Rowing CAN-1908 ★古★☆☆ Partial (Historical limitation)

<!-- b001596 | caption | pages [18] -->
Table 3: Historical Data Validation Analysis

<!-- b001597 | heading | pages [18] -->
5.4 The result of the mathematical model

<!-- b001598 | prose | pages [18] -->
Between 1994 and 2024, a positive correlation was observed between medal increment (∆M ) and information gain (IG), indicating that abnormal events, such as the influence of coaching, significantly impact medal growth, as shown in Figure 18 . The United States and Australia exhibited stable medal growth, while Brazil's performance was more volatile. Additionally, some countries had outliers, which may be attributed to short-term increases caused by external factors like home-field advantage.

<!-- b001599 | prose | pages [18] -->
AM vs. IG: Selected Countries (1994-2024) 0.7 oC Country ● AUS 0.6 ARG ●o BRA ● Information Gain (IG) 0.5 O ● 0.4 ● O 0.3 ● 0000 cos 0000 ●

<!-- b001600 | prose | pages [18] -->
● 0.2 ● ● n0o ● ●

<!-- b001601 | prose | pages [18] -->
● 0.1 ● 0.0 O -30 -20 -10 20 30 40 10 0 Medal Increment (ΔM)

<!-- b001602 | caption | pages [18] -->
Figure 18: ∆M vs. IG scatter plot

<!-- b001603 | caption | pages [18] -->
Figure 19 shows that from 1952 to 2024, Australia's medal growth generally showed an

<!-- b001604 | prose | pages [18] -->
upward trend, particularly after the Sydney 2000 Olympic Games. Brazil peaked at the 2016 Rio Olympics and then declined, while Argentina's medal growth fluctuated greatly with- out an obvious upward trend. All three countries experienced a sharp drop in medal growth in specific years, such as the 1980 boycott, but Australia recovered faster, demonstrating a more resilient sports system. Brazil's significant increase in medal growth at the 2016 Rio Olympics validated the short-term boost provided by home-field advantage.

<!-- b001605 | prose | pages [18] -->
Australia, Argentina, and Brazil have great potential in sports such as swimming and athletics, which should be prioritized for investment due to their high growth potential, as shown in Figure 20. Countries should also focus on remaining opportunities, such as Argentina's potential in hockey, to maximize medal growth.

<!-- b001606 | prose | pages [18] -->
Taken together, the three charts reveal the key drivers of Olympic medal growth from different perspectives, validate the predictive power of abnormal events (such as coaching effects) on medal growth, and provide countries with clear strategic direction to optimize 关注数学模型 resource allocation and achieve medal growth targets.

<!-- b001607 | furniture | pages [18] -->
获取更多资讯

<!-- b001608 | furniture | pages [19] -->
Team # 2514362

<!-- b001609 | furniture | pages [19] -->
Page 18 of 26

<!-- b001610 | caption | pages [19] -->
Figure 19: Medal Trends

<!-- b001611 | caption | pages [19] -->
Figure 20: Recommended Projects

<!-- b001612 | prose | pages [19] -->
Based on the results of the model analysis, we identiﬁed three countries and programs that most need to bring in good coaches, as is shown in Table 4.

<!-- b001613 | prose | pages [19] -->
微信公众号：数学模型

<!-- b001614 | caption | pages [19] -->
Table 4: Sport Medal Potential by Country

<!-- b001615 | prose | pages [19] -->
IG Country Sport Current Medal Max Medal Potential Score

<!-- b001616 | prose | pages [19] -->
SWE Wrestling 0.6541 0.0 13.0 0.6541 HUN Wrestling 0.6541 0.0 7.0 0.6541 FRA Rowing 0.6509 0.0 18.0 0.6509

<!-- b001617 | prose | pages [19] -->
• SWE–Wrestling : Both information gain ( IG = 0.654 ) and residual opportunity ( 1.0 ) were signiﬁcant, indicating that abnormal progress events were strongly correlated with 微信号：MATHmodels medal growth, and the current number of medals was 0, with great room for improve- ment. Sweden, which has a record of 13 medals at its peak, currently has no medals, presumably due to the loss of coaches (such as retirement or moving to another country) resulting in a precipitous decline in results. It has an urgent need to bring in top coaches to restore its traditional strength.

<!-- b001618 | prose | pages [19] -->
• HUN–Wrestling : IG is tied for ﬁrst place with Swedish Wrestling with a residual chance of 1.0, indicating that the sport has frequent abnormal progress events (such as short bursts after coaching intervention), but the current medal count is 0, and the need for stability support is urgent. Hungary has a history of ﬂuctuating performance and needs to build long-term competitiveness by bringing in good coaches to avoid ups and downs.

<!-- b001619 | prose | pages [19] -->
• FRA–Rowing : The IG value was high ( 0.651 ) and the remaining chance was 1.0, indi- cating that the coaching intervention may activate the potential quickly. France, which peaked at 18 medals in its history and has languished in recent years, needs to revive its technical system by bringing in foreign coaches, such as Eastern European or British rowers, to achieve a medal breakthrough in the short term.

<!-- b001620 | caption | pages [19] -->
Table 5 illustrates the potential short-term and long-term impacts on medal counts if

<!-- b001621 | prose | pages [19] -->
these countries were to introduce highly capable coaches in the respective sports, while also highlighting possible risks and corresponding measures.

<!-- b001622 | caption | pages [19] -->
Table 5: The Impact Brought by the Introduction of Coaches

<!-- b001623 | prose | pages [19] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001624 | furniture | pages [19] -->
m

<!-- b001625 | furniture | pages [19] -->
m

<!-- b001626 | furniture | pages [19] -->
m

<!-- b001627 | furniture | pages [19] -->
m

<!-- b001628 | furniture | pages [19] -->
m

<!-- b001629 | furniture | pages [19] -->
m

<!-- b001630 | furniture | pages [19] -->
m

<!-- b001631 | furniture | pages [19] -->
m

<!-- b001632 | furniture | pages [19] -->
m

<!-- b001633 | furniture | pages [19] -->
m

<!-- b001634 | furniture | pages [19] -->
m

<!-- b001635 | furniture | pages [19] -->
m

<!-- b001636 | furniture | pages [19] -->
m

<!-- b001637 | furniture | pages [19] -->
m

<!-- b001638 | furniture | pages [19] -->
m

<!-- b001639 | furniture | pages [19] -->
m

<!-- b001640 | furniture | pages [19] -->
m

<!-- b001641 | furniture | pages [19] -->
m

<!-- b001642 | furniture | pages [19] -->
m

<!-- b001643 | furniture | pages [19] -->
m

<!-- b001644 | furniture | pages [19] -->
m

<!-- b001645 | furniture | pages [19] -->
m

<!-- b001646 | furniture | pages [19] -->
m

<!-- b001647 | furniture | pages [19] -->
m

<!-- b001648 | furniture | pages [19] -->
m

<!-- b001649 | furniture | pages [19] -->
m

<!-- b001650 | furniture | pages [19] -->
m

<!-- b001651 | furniture | pages [19] -->
m

<!-- b001652 | furniture | pages [19] -->
m

<!-- b001653 | furniture | pages [19] -->
m

<!-- b001654 | furniture | pages [19] -->
m

<!-- b001655 | furniture | pages [19] -->
m

<!-- b001656 | furniture | pages [19] -->
m

<!-- b001657 | furniture | pages [19] -->
m

<!-- b001658 | furniture | pages [19] -->
m

<!-- b001659 | furniture | pages [19] -->
m

<!-- b001660 | furniture | pages [19] -->
m

<!-- b001661 | furniture | pages [19] -->
m

<!-- b001662 | furniture | pages [19] -->
m

<!-- b001663 | furniture | pages [19] -->
m

<!-- b001664 | furniture | pages [19] -->
m

<!-- b001665 | furniture | pages [19] -->
m

<!-- b001666 | furniture | pages [19] -->
m

<!-- b001667 | furniture | pages [19] -->
m

<!-- b001668 | furniture | pages [19] -->
m

<!-- b001669 | furniture | pages [19] -->
m

<!-- b001670 | furniture | pages [19] -->
m

<!-- b001671 | furniture | pages [19] -->
m

<!-- b001672 | furniture | pages [19] -->
m

<!-- b001673 | furniture | pages [19] -->
m

<!-- b001674 | furniture | pages [19] -->
m

<!-- b001675 | furniture | pages [19] -->
m

<!-- b001676 | furniture | pages [19] -->
m

<!-- b001677 | furniture | pages [19] -->
m

<!-- b001678 | furniture | pages [19] -->
m

<!-- b001679 | furniture | pages [19] -->
m

<!-- b001680 | furniture | pages [19] -->
m

<!-- b001681 | furniture | pages [19] -->
m

<!-- b001682 | furniture | pages [19] -->
m

<!-- b001683 | furniture | pages [19] -->
m

<!-- b001684 | furniture | pages [19] -->
m

<!-- b001685 | furniture | pages [19] -->
m

<!-- b001686 | furniture | pages [19] -->
m

<!-- b001687 | furniture | pages [19] -->
m

<!-- b001688 | furniture | pages [19] -->
m

<!-- b001689 | furniture | pages [19] -->
m

<!-- b001690 | furniture | pages [19] -->
m

<!-- b001691 | furniture | pages [19] -->
m

<!-- b001692 | furniture | pages [19] -->
m

<!-- b001693 | furniture | pages [19] -->
m

<!-- b001694 | furniture | pages [19] -->
m

<!-- b001695 | furniture | pages [19] -->
m

<!-- b001696 | furniture | pages [19] -->
m

<!-- b001697 | furniture | pages [19] -->
m

<!-- b001698 | furniture | pages [19] -->
m

<!-- b001699 | furniture | pages [19] -->
m

<!-- b001700 | furniture | pages [19] -->
m

<!-- b001701 | furniture | pages [19] -->
m

<!-- b001702 | furniture | pages [19] -->
m

<!-- b001703 | furniture | pages [19] -->
m

<!-- b001704 | furniture | pages [19] -->
m

<!-- b001705 | furniture | pages [19] -->
m

<!-- b001706 | furniture | pages [19] -->
m

<!-- b001707 | furniture | pages [19] -->
m

<!-- b001708 | furniture | pages [19] -->
m

<!-- b001709 | furniture | pages [19] -->
m

<!-- b001710 | furniture | pages [19] -->
m

<!-- b001711 | furniture | pages [19] -->
m

<!-- b001712 | furniture | pages [19] -->
m

<!-- b001713 | furniture | pages [19] -->
m

<!-- b001714 | furniture | pages [19] -->
m

<!-- b001715 | furniture | pages [19] -->
m

<!-- b001716 | furniture | pages [19] -->
m

<!-- b001717 | furniture | pages [19] -->
m

<!-- b001718 | furniture | pages [19] -->
m

<!-- b001719 | furniture | pages [19] -->
m

<!-- b001720 | furniture | pages [19] -->
m

<!-- b001721 | furniture | pages [19] -->
m

<!-- b001722 | furniture | pages [19] -->
m

<!-- b001723 | furniture | pages [19] -->
m

<!-- b001724 | furniture | pages [19] -->
m

<!-- b001725 | furniture | pages [19] -->
m

<!-- b001726 | furniture | pages [19] -->
m

<!-- b001727 | furniture | pages [19] -->
m

<!-- b001728 | furniture | pages [19] -->
m

<!-- b001729 | furniture | pages [19] -->
m

<!-- b001730 | furniture | pages [19] -->
m

<!-- b001731 | furniture | pages [19] -->
m

<!-- b001732 | furniture | pages [19] -->
m

<!-- b001733 | furniture | pages [19] -->
m

<!-- b001734 | furniture | pages [19] -->
m

<!-- b001735 | furniture | pages [19] -->
m

<!-- b001736 | furniture | pages [19] -->
m

<!-- b001737 | furniture | pages [19] -->
m

<!-- b001738 | furniture | pages [19] -->
m

<!-- b001739 | furniture | pages [19] -->
m

<!-- b001740 | furniture | pages [19] -->
m

<!-- b001741 | furniture | pages [19] -->
m

<!-- b001742 | furniture | pages [19] -->
m

<!-- b001743 | furniture | pages [19] -->
m

<!-- b001744 | furniture | pages [19] -->
m

<!-- b001745 | furniture | pages [19] -->
m

<!-- b001746 | furniture | pages [19] -->
m

<!-- b001747 | furniture | pages [19] -->
m

<!-- b001748 | furniture | pages [19] -->
m

<!-- b001749 | furniture | pages [19] -->
m

<!-- b001750 | furniture | pages [19] -->
m

<!-- b001751 | furniture | pages [19] -->
m

<!-- b001752 | furniture | pages [19] -->
m

<!-- b001753 | furniture | pages [19] -->
m

<!-- b001754 | furniture | pages [19] -->
m

<!-- b001755 | furniture | pages [19] -->
m

<!-- b001756 | furniture | pages [19] -->
m

<!-- b001757 | furniture | pages [19] -->
m

<!-- b001758 | furniture | pages [19] -->
m

<!-- b001759 | furniture | pages [19] -->
m

<!-- b001760 | furniture | pages [19] -->
m

<!-- b001761 | furniture | pages [19] -->
m

<!-- b001762 | furniture | pages [19] -->
m

<!-- b001763 | furniture | pages [19] -->
m

<!-- b001764 | furniture | pages [19] -->
m

<!-- b001765 | furniture | pages [19] -->
m

<!-- b001766 | furniture | pages [19] -->
m

<!-- b001767 | furniture | pages [19] -->
m

<!-- b001768 | furniture | pages [19] -->
m

<!-- b001769 | furniture | pages [19] -->
m

<!-- b001770 | furniture | pages [19] -->
m

<!-- b001771 | furniture | pages [19] -->
m

<!-- b001772 | furniture | pages [19] -->
m

<!-- b001773 | furniture | pages [19] -->
m

<!-- b001774 | furniture | pages [19] -->
m

<!-- b001775 | furniture | pages [19] -->
m

<!-- b001776 | furniture | pages [19] -->
m

<!-- b001777 | furniture | pages [19] -->
m

<!-- b001778 | furniture | pages [19] -->
m

<!-- b001779 | furniture | pages [19] -->
m

<!-- b001780 | furniture | pages [19] -->
m

<!-- b001781 | furniture | pages [19] -->
m

<!-- b001782 | furniture | pages [19] -->
m

<!-- b001783 | furniture | pages [19] -->
m

<!-- b001784 | furniture | pages [19] -->
m

<!-- b001785 | furniture | pages [19] -->
m

<!-- b001786 | furniture | pages [19] -->
m

<!-- b001787 | furniture | pages [19] -->
m

<!-- b001788 | furniture | pages [19] -->
m

<!-- b001789 | furniture | pages [19] -->
m

<!-- b001790 | furniture | pages [19] -->
m

<!-- b001791 | furniture | pages [19] -->
m

<!-- b001792 | furniture | pages [19] -->
m

<!-- b001793 | furniture | pages [19] -->
m

<!-- b001794 | furniture | pages [19] -->
m

<!-- b001795 | furniture | pages [19] -->
m

<!-- b001796 | furniture | pages [19] -->
m

<!-- b001797 | furniture | pages [19] -->
m

<!-- b001798 | furniture | pages [19] -->
m

<!-- b001799 | furniture | pages [19] -->
m

<!-- b001800 | furniture | pages [19] -->
m

<!-- b001801 | furniture | pages [19] -->
m

<!-- b001802 | furniture | pages [19] -->
m

<!-- b001803 | furniture | pages [19] -->
m

<!-- b001804 | furniture | pages [19] -->
m

<!-- b001805 | furniture | pages [19] -->
m

<!-- b001806 | furniture | pages [19] -->
m

<!-- b001807 | furniture | pages [19] -->
m

<!-- b001808 | furniture | pages [19] -->
m

<!-- b001809 | furniture | pages [19] -->
m

<!-- b001810 | furniture | pages [19] -->
m

<!-- b001811 | furniture | pages [19] -->
m

<!-- b001812 | furniture | pages [19] -->
m

<!-- b001813 | furniture | pages [19] -->
m

<!-- b001814 | furniture | pages [19] -->
m

<!-- b001815 | furniture | pages [19] -->
m

<!-- b001816 | furniture | pages [19] -->
m

<!-- b001817 | furniture | pages [19] -->
m

<!-- b001818 | furniture | pages [19] -->
m

<!-- b001819 | furniture | pages [19] -->
m

<!-- b001820 | furniture | pages [19] -->
m

<!-- b001821 | furniture | pages [19] -->
m

<!-- b001822 | furniture | pages [19] -->
m

<!-- b001823 | furniture | pages [19] -->
m

<!-- b001824 | furniture | pages [19] -->
m

<!-- b001825 | furniture | pages [19] -->
m

<!-- b001826 | furniture | pages [19] -->
m

<!-- b001827 | furniture | pages [19] -->
m

<!-- b001828 | furniture | pages [19] -->
m

<!-- b001829 | furniture | pages [19] -->
m

<!-- b001830 | furniture | pages [19] -->
m

<!-- b001831 | furniture | pages [19] -->
m

<!-- b001832 | furniture | pages [19] -->
m

<!-- b001833 | furniture | pages [19] -->
m

<!-- b001834 | furniture | pages [19] -->
m

<!-- b001835 | furniture | pages [19] -->
m

<!-- b001836 | furniture | pages [19] -->
m

<!-- b001837 | furniture | pages [19] -->
m

<!-- b001838 | furniture | pages [19] -->
m

<!-- b001839 | furniture | pages [19] -->
m

<!-- b001840 | furniture | pages [19] -->
m

<!-- b001841 | furniture | pages [19] -->
m

<!-- b001842 | furniture | pages [19] -->
m

<!-- b001843 | furniture | pages [19] -->
m

<!-- b001844 | furniture | pages [19] -->
m

<!-- b001845 | furniture | pages [19] -->
m

<!-- b001846 | furniture | pages [19] -->
m

<!-- b001847 | furniture | pages [19] -->
m

<!-- b001848 | furniture | pages [19] -->
m

<!-- b001849 | furniture | pages [19] -->
m

<!-- b001850 | furniture | pages [19] -->
m

<!-- b001851 | furniture | pages [19] -->
m

<!-- b001852 | furniture | pages [19] -->
m

<!-- b001853 | furniture | pages [19] -->
m

<!-- b001854 | furniture | pages [19] -->
m

<!-- b001855 | furniture | pages [19] -->
m

<!-- b001856 | furniture | pages [19] -->
m

<!-- b001857 | furniture | pages [19] -->
m

<!-- b001858 | furniture | pages [19] -->
m

<!-- b001859 | furniture | pages [19] -->
m

<!-- b001860 | furniture | pages [19] -->
m

<!-- b001861 | furniture | pages [19] -->
m

<!-- b001862 | furniture | pages [19] -->
m

<!-- b001863 | furniture | pages [19] -->
m

<!-- b001864 | furniture | pages [19] -->
m

<!-- b001865 | furniture | pages [19] -->
m

<!-- b001866 | furniture | pages [19] -->
m

<!-- b001867 | furniture | pages [19] -->
m

<!-- b001868 | furniture | pages [19] -->
m

<!-- b001869 | furniture | pages [19] -->
m

<!-- b001870 | furniture | pages [19] -->
m

<!-- b001871 | furniture | pages [19] -->
m

<!-- b001872 | furniture | pages [19] -->
m

<!-- b001873 | furniture | pages [19] -->
m

<!-- b001874 | furniture | pages [19] -->
m

<!-- b001875 | furniture | pages [19] -->
m

<!-- b001876 | furniture | pages [19] -->
m

<!-- b001877 | furniture | pages [19] -->
m

<!-- b001878 | furniture | pages [19] -->
m

<!-- b001879 | furniture | pages [19] -->
m

<!-- b001880 | furniture | pages [19] -->
m

<!-- b001881 | furniture | pages [19] -->
m

<!-- b001882 | furniture | pages [19] -->
m

<!-- b001883 | furniture | pages [19] -->
m

<!-- b001884 | furniture | pages [19] -->
m

<!-- b001885 | furniture | pages [19] -->
m

<!-- b001886 | furniture | pages [19] -->
m

<!-- b001887 | furniture | pages [19] -->
m

<!-- b001888 | furniture | pages [19] -->
m

<!-- b001889 | furniture | pages [19] -->
m

<!-- b001890 | furniture | pages [19] -->
m

<!-- b001891 | furniture | pages [19] -->
m

<!-- b001892 | furniture | pages [19] -->
m

<!-- b001893 | furniture | pages [19] -->
m

<!-- b001894 | furniture | pages [19] -->
m

<!-- b001895 | furniture | pages [19] -->
m

<!-- b001896 | furniture | pages [19] -->
m

<!-- b001897 | furniture | pages [19] -->
m

<!-- b001898 | furniture | pages [19] -->
m

<!-- b001899 | furniture | pages [19] -->
m

<!-- b001900 | furniture | pages [19] -->
m

<!-- b001901 | furniture | pages [19] -->
m

<!-- b001902 | furniture | pages [19] -->
m

<!-- b001903 | furniture | pages [19] -->
m

<!-- b001904 | furniture | pages [19] -->
m

<!-- b001905 | furniture | pages [19] -->
m

<!-- b001906 | furniture | pages [19] -->
m

<!-- b001907 | furniture | pages [19] -->
m

<!-- b001908 | furniture | pages [19] -->
m

<!-- b001909 | furniture | pages [19] -->
m

<!-- b001910 | furniture | pages [19] -->
m

<!-- b001911 | furniture | pages [19] -->
m

<!-- b001912 | furniture | pages [19] -->
m

<!-- b001913 | furniture | pages [19] -->
m

<!-- b001914 | furniture | pages [19] -->
m

<!-- b001915 | furniture | pages [19] -->
m

<!-- b001916 | furniture | pages [19] -->
m

<!-- b001917 | furniture | pages [19] -->
m

<!-- b001918 | furniture | pages [19] -->
m

<!-- b001919 | furniture | pages [19] -->
m

<!-- b001920 | furniture | pages [19] -->
m

<!-- b001921 | furniture | pages [19] -->
m

<!-- b001922 | furniture | pages [19] -->
m

<!-- b001923 | furniture | pages [19] -->
m

<!-- b001924 | furniture | pages [19] -->
m

<!-- b001925 | furniture | pages [19] -->
m

<!-- b001926 | furniture | pages [19] -->
m

<!-- b001927 | furniture | pages [19] -->
m

<!-- b001928 | furniture | pages [19] -->
m

<!-- b001929 | furniture | pages [19] -->
m

<!-- b001930 | furniture | pages [19] -->
m

<!-- b001931 | furniture | pages [19] -->
m

<!-- b001932 | furniture | pages [19] -->
m

<!-- b001933 | furniture | pages [19] -->
m

<!-- b001934 | furniture | pages [19] -->
m

<!-- b001935 | furniture | pages [19] -->
m

<!-- b001936 | furniture | pages [19] -->
m

<!-- b001937 | furniture | pages [19] -->
m

<!-- b001938 | furniture | pages [19] -->
m

<!-- b001939 | furniture | pages [19] -->
m

<!-- b001940 | furniture | pages [19] -->
m

<!-- b001941 | furniture | pages [19] -->
m

<!-- b001942 | furniture | pages [19] -->
m

<!-- b001943 | furniture | pages [19] -->
m

<!-- b001944 | furniture | pages [19] -->
m

<!-- b001945 | furniture | pages [19] -->
m

<!-- b001946 | furniture | pages [19] -->
m

<!-- b001947 | furniture | pages [19] -->
m

<!-- b001948 | furniture | pages [20] -->
Team # 2514362

<!-- b001949 | furniture | pages [20] -->
Page 19 of 26

<!-- b001950 | heading | pages [20] -->
5.5 Sensitivity Analysis

<!-- b001951 | prose | pages [20] -->
• Laplace Smoothing Parameters (α, β) (Bayesian prior adjustment):

<!-- b001952 | prose | pages [20] -->
X + α α, β ∈R+ Ppost = N + α + β , (22)

<!-- b001953 | prose | pages [20] -->
– Default conﬁguration (α = β = 1) achieves optimal trade-off:

<!-- b001954 | prose | pages [20] -->
• Noise suppression: ↑43% (p < 0.001, Cohen’s d = 1.2)

<!-- b001955 | prose | pages [20] -->
• Information preservation: ↓15% (95% CI: 12.3–17.8) – Sparse data regime: α, β ∈[1.5, 2.0] yields ∆F1 = +7.2% (95% CI [5.1, 9.3])

<!-- b001956 | prose | pages [20] -->
• Detection Threshold (T) (Abnormal medal increment criterion):

<!-- b001957 | prose | pages [20] -->
T θ Events Avg. IG Projects Max IG

<!-- b001958 | prose | pages [20] -->
0.23 ± 0.04 202 63 0.309 1 0.2 0.11 ± 0.02 152 40 0.309 3 0.3 0 0.4 –

<!-- b001959 | prose | pages [20] -->
– Statistical relationships:

<!-- b001960 | prose | pages [20] -->
Coverage ∝T −0.92 (R2 = 0.96) Precision ∝θ0.68 (R2 = 0.89)

<!-- b001961 | prose | pages [20] -->
• Operational Protocol:

<!-- b001962 | prose | pages [20] -->
– Exploratory analysis (n ≥5.0 × 103):

<!-- b001963 | prose | pages [20] -->
▷Optimal conﬁguration: {T = 1, θ = 0.2} ▷Performance: Recall = 0.923 (95% CI [0.901, 0.942]) – Production deployment (n ≥2.0 × 104):

<!-- b001964 | prose | pages [20] -->
▷Optimal conﬁguration: {T ≥3, θ = 0.35} ▷Performance: Precision = 0.891 (95% CI [0.875, 0.906]) †All metrics derived from 10-fold cross-validation (N=11,234 samples; stratiﬁed sampling) ‡IG: Information Gain (H0 −H1), measured in nats

<!-- b001965 | prose | pages [20] -->
In general, we performed the analysis of the sensitivity of the Laplace smoothing pa- rameter, the sensitivity of the threshold of abnormal events, and the sensitivity of the infor- mation gain threshold.The heat map in Figure 21 shows the average information gain(Avg_IG) for different α and β combinations. As can be seen from the graph, the average information gain gradually decreases as the α and β increase. The line chart in Figure 21 shows the av- erage information gain and the number of abnormal events at different thresholds T, and it is found that the increasing T will reduce the number of abnormal events, but signiﬁcantly reduce the average information gain. At the same time, the bar chart in Figure 21 also shows the number of recommended items under different θ (θ is described in the notation section). We can see that when the θ is raised, the number of recommended items decreases, but the highest potential score remains the same.

<!-- b001966 | prose | pages [20, 21] -->
关注数学模型 IG vs. ∆M Threshold Sensitivity to α and β Projects Count vs. 0

<!-- b001967 | furniture | pages [20] -->
2

<!-- b001968 | furniture | pages [20] -->
MATHmodels

<!-- b001969 | furniture | pages [20] -->
获取更多资讯

<!-- b001970 | furniture | pages [21] -->
Page 20 of 26

<!-- b001971 | furniture | pages [21] -->
Team # 2514362

<!-- b001972 | caption | pages [21] -->
Figure 21: Sensitivity Analysis

<!-- b001974 | prose | pages [21] -->
0.35 60 0.22 55 0.346 0.374 0.334 50 0.30 0.20 Number of Projects 40 Average IG Average IG 0.18 0.25 Alpha 0.264 0.251 0.230 30 0.16 0.20 20 0.14 0.15 20 0.132 0.03 0.111 10 0.12 0.10 0 0.5 1.0 20 1.0 1.5 0.2 0.3 0.4 2.5 2.0 3.0 Beta Threshold (T) θ

<!-- b001975 | prose | pages [21] -->
Original Insights 6

<!-- b001976 | prose | pages [21] -->
Analysis of "Potential Medal" in Non-Medal-Winning Nations 6.1

<!-- b001977 | prose | pages [21] -->
Methodology ● The Zero-Inflated Negative Binomial model is employed to quantify the latent medal potential of nations that have not yet won Olympic medals. This model integrates dynamic variables like the weighted number of participants (Athletesit) and the degree of alignment between a nation's historical strengths and the current Olympic program (ProjectMatchit). m Key Findings

<!-- b001978 | prose | pages [21] -->
• High-Match Nations: 38% of non-medal-winning nations exhibit a high project match index (ProjectMatchit > 0.2) in at least one sport, indicating significant potential for medal success.

<!-- b001979 | prose | pages [21] -->
Resource Efficiency: A 1% increase in resource allocation efficiency (proxied by per capita training expenditure) boosts the probability of medal success by 2.3% (p < 0.01).

<!-- b001980 | prose | pages [21] -->
The radar chart (Figure 22) visualizes the sport-specific potential distribution of three representative medal-less nations. Saint Lucia demonstrates 85% matching potential in sprinting, consistent with its historic gold medal breakthrough at Paris 2024. The asym- metric polar coordinates emphasize strategic priorities.

<!-- b001981 | heading | pages [21] -->
Strategic Recommendations

<!-- b001982 | prose | pages [21] -->
Nations should prioritize targeted investment in high-match, low-resource sports.

<!-- b001983 | heading | pages [21] -->
6.2 The Multiplier Effect of Elite Coaches

<!-- b001984 | prose | pages [21] -->
Methodology The Bayesian Entropy Model is utilized to quantify the impact of elite coaches on medal performance. The core metric, Information Gain (IG), measures the reduction in uncertainty regarding medal outcomes due to coaching interventions. A threshold of IG > 0.3 indicates a significant impact.

<!-- b001985 | prose | pages [21, 22] -->
Key Findings Coach Effect: In sports with IG > 0.3, the introduction of elite coaches increases medal counts by 1.82.5 times, with particularly pronounced effects in technically complex sports such as gymnastics and swimming.

<!-- b001986 | furniture | pages [22] -->
Team # 2514362

<!-- b001987 | furniture | pages [22] -->
Page 21 of 26

<!-- b001988 | caption | pages [22] -->
Figure 22: Event Matching Potential

<!-- b001989 | caption | pages [22] -->
Figure 23: Dynamic Evolution

<!-- b001991 | prose | pages [22] -->
• Temporal Dynamics: The full impact of coaching changes typically manifests after 1.5 Olympic cycles (6 years), reﬂecting the time required for technical system overhauls.

<!-- b001992 | prose | pages [22] -->
This spatiotemporal visualization ( Figure 23 ) shows the medal multiplier effect of elite coaches. Bubble size encodes coaching impact index, colors denote sports, and asterisks indicate statistical signiﬁcance. The peak multiplier in Gymnastics ( Paris 2024 ) validates model predictions.

<!-- b001993 | heading | pages [22] -->
Strategic Recommendations

<!-- b001994 | prose | pages [22] -->
Nations should adopt dynamic recruitment strategies, focusing on sports with high IG values and current medal counts below 70% of historical maxima. Performance-based con- tracts, linking coach compensation to IG values and medal increments, can further incen- tivize success.

<!-- b001995 | heading | pages [22] -->
6.3 Dual Nature of Host Effect

<!-- b001996 | prose | pages [22] -->
Positive Effects: Resource Concentration and Short-Term Gains

<!-- b001997 | prose | pages [22] -->
As the host of the 2028 Olympic Games, the United States has a projected performance of 42 gold medals and a total of about 122 medals, ﬁrmly leading the list. This may be due to the fact that the renovation cost of the Los Angeles Olympic Village, which directly improved the training conditions for American athletes in athletics, swimming, and other events. The second is because of the new project dividends. In our model, β2 .= 0.32 with the United States as the host in 2028 Hostit .= 1, the medal expectation increases by 37%, which is in line with the upper limit of 46 gold medals in the actual forecast range.

<!-- b001998 | prose | pages [22] -->
Negative Effects: Fiscal Overextension and Long-Term Decline

<!-- b001999 | prose | pages [22] -->
The host effect also brings the risk of ﬁscal overdraft. For example, the maintenance burden of the venue and the short-term investment are unsustainable. Greece, as the host in 2004, had a prolonged debt crisis after hosting this Olympics. Therefore, we recommend the use of "debt suppressors" to avoid overly optimistic forecasts.

<!-- b002000 | prose | pages [22] -->
At the same time, it can also put pressure on athletes to perform. Pressure and injuries might be caused.

<!-- b002001 | prose | pages [22] -->
关注数学模型

<!-- b002002 | furniture | pages [22] -->
2

<!-- b002003 | furniture | pages [22] -->
MATHmodels

<!-- b002004 | furniture | pages [22] -->
获取更多资讯

<!-- b002005 | furniture | pages [23] -->
Team # 2514362

<!-- b002006 | furniture | pages [23] -->
Page 22 of 26

<!-- b002007 | heading | pages [23] -->
6.4 The reference value of Cold War factors

<!-- b002008 | prose | pages [23] -->
During our data analysis, we observed signiﬁcant changes in Olympic medal data dur- ing and around the Cold War period, prompting us to consider incorporating the Cold War factor as a parameter. As illustrated in the Figure 24, the model’s predictions without the Cold War factor during the relevant Cold War times were far from the actual results. Thus, when dealing with this period, the Cold War factor can exert a certain constraining effect. However, after constructing our model and making predictions, we found that the Cold War factor had minimal impact on modern forecasting analysis results.

<!-- b002009 | prose | pages [23] -->
However, in view of the complex situation in the current world, we suggest that when considering local conﬂicts or geopolitical contradictions, variables similar to the Cold War factor can be introduced to further improve the accuracy of the model prediction.

<!-- b002010 | prose | pages [23] -->
微信公众号：数学模型

<!-- b002011 | caption | pages [23] -->
Figure 24: The Impact of Cold War

<!-- b002012 | caption | pages [23] -->
Figure 25: Impact of "Black Swan" on Brazil

<!-- b002013 | prose | pages [23] -->
微信号：MATHmodels

<!-- b002014 | heading | pages [23] -->
7 Strengths and weaknesses

<!-- b002015 | heading | pages [23] -->
7.1 Strengths

<!-- b002016 | prose | pages [23] -->
• Preciseness In our ﬁrst model, we add coefﬁcients like ColdWar coefﬁcient and Project- Match coefﬁcient to better forecast the medal table and build the relationship between events and nations. Alao, the exponential decay weighting of historical performance en- sures that the model prioritizes reﬂecting recent trends, which is crucial for events with fast athlete turnover. In our second model, we use laplace smoothing and entropy based metrics alleviate overﬁtting issues, enabling effective inference even for countries with sparse medal histories.

<!-- b002017 | prose | pages [23] -->
• Computable The second model based on Bayesian entropy only requires basic statisti- cal operations (such as logarithm), without the need for complex algorithms or high- performance hardware, making it suitable for rapid deployment in resource limited Olympic committees. It turned out that the process could be ﬁnished within a second.

<!-- b002018 | prose | pages [23] -->
• Portable The model supports dynamic adjustment of key parameters (such as historical decay factor λ , information gain threshold IG) through grid search or Bayesian opti- mization to meet the personalized needs of different countries.

<!-- b002019 | heading | pages [23] -->
7.2 Weaknesses

<!-- b002020 | prose | pages [23] -->
• Historical data deviation The model heavily relies on historical medal data and compe- tition records, but early Olympic data (such as 1896-1950) may have issues with incom- plete records, statistical error or inconsistent classiﬁcation standards (such as national restructuring after the dissolution of the Soviet Union), which affects the accuracy of long-term trend analysis.

<!-- b002021 | prose | pages [23, 24] -->
• Insufﬁcient adaptability to unexpected events The model lacks the ability to due with Black Swan Events. The model did not take into account the impact of unforeseeable emergencies such as the COVID-19 pandemic, political boycotts, and large-scale bans on training and competition. For example, The COVID-19 caused rare disturbances in the history of the Olympic Games (such as the postponement of events, the interruption of athletes’ training, and the cancellation of qualiﬁcation events), and the model could not capture these effects because it relied on the assumption of historical continuity. Taking Brazil as an example, the Figure 25 clearly shows that before the outbreak of the COVID- 19 pandemic,the model’s prediction accuracy was around 80%. However, after the pan- demic erupted in 2020, the prediction accuracy for the Tokyo Olympics plummeted to below 50%, only gradually recovering to nearly 80% by 2024.

<!-- b002022 | furniture | pages [24] -->
Team # 2514362

<!-- b002023 | furniture | pages [24] -->
Page 23 of 26

<!-- b002025 | heading | pages [24] -->
8 Conclusion

<!-- b002026 | prose | pages [24] -->
This study presents a dual-model framework to forecast Olympic medal outcomes and evaluate strategic interventions for National Olympic Committees. The multi-level inte- grated forecasting model, incorporating mixed-effects negative binomial regression and zero- inﬂated negative binomial approaches, effectively addresses overdispersion and zero-inﬂation challenges in medal prediction. Key ﬁndings project the United States (42 gold medals) and China (36 gold medals) as top contenders in 2028, with emerging nations like Cyprus and Fiji identiﬁed as potential ﬁrst-time medalists. The entropy model with Bayesian modiﬁca- tion quantiﬁes the multiplier effect of elite coaching, highlighting wrestling for Sweden and Hungary, and rowing for France as high-impact investment areas.

<!-- b002027 | prose | pages [24] -->
The models demonstrate robustness through sensitivity analyses and ablation studies, validating their adaptability to historical trends and event dynamics. However, reliance on historical continuity limits their capacity to account for black swan events like pandemics. Strategic recommendations emphasize prioritizing sports with high information gain (IG > 0.3) and optimizing resource allocation through dynamic coach recruitment. Future work could integrate real-time athlete performance data and geopolitical factors to enhance pre- dictive precision. These insights equip Olympic committees with actionable tools to unlock medal potential and sustain competitive excellence.

<!-- b002028 | prose | pages [24] -->
As for the advice to NOCs, according to the speciﬁc situation of each country, prior- ity should be given to investing in projects with high information gain values and current medal counts below 70% of historical peaks. For small countries that have not yet won Olympic medals, such as Cyprus, Fiji, and Kuwait, the chances of winning can be increased m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m by concentrating resources on speciﬁc events or increasing the number of participants. For m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m host countries, like USA in the year of 2028, the US Olympic Committee should fully utilize m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m its home advantage, optimize infrastructure and audience support, strengthen traditional m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m advantage events such as swimming and athletics, actively prepare for new events such as m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m esports and breakdancing, introduce top coaches and establish a psychological counseling m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002029 | prose | pages [24] -->
system.

<!-- b002030 | heading | pages [24] -->
References

<!-- b002031 | references | pages [24] -->
[1] Fei, P. S. (2013). Analysis on Intercontinental Distribution Characteristics of Track and Field

<!-- b002032 | references | pages [24] -->
Medals from the 23rd to 30th Olympic Games. China Sport Science and Technology, 49(2), 9–15.

<!-- b002033 | references | pages [24] -->
[2] Jowett, S. (2007). Interdependence analysis and the 3+1Cs in the coach-athlete relationship.

<!-- b002034 | references | pages [24] -->
Psychology of Sport and Exercise, 8(4), 541–560.

<!-- b002035 | references | pages [24] -->
DOI: https://doi.org/10.1016/j.psychsport.2006.11.001

<!-- b002036 | references | pages [24] -->
[3] Schinke, R. J., Hanrahan, S. J., & Catina, P. (2012). The adaptation challenges and strategies

<!-- b002037 | references | pages [24] -->
of immigrant athletes and coaches. Psychology of Sport and Exercise, 13(5), 615–621.

<!-- b002038 | references | pages [24] -->
关注数学模型

<!-- b002039 | references | pages [24] -->
DOI: https://doi.org/10.1016/j.psychsport.2012.03.006

<!-- b002040 | furniture | pages [24] -->
2

<!-- b002041 | furniture | pages [24] -->
MATHmodels

<!-- b002042 | furniture | pages [24] -->
获取更多资讯

<!-- b002043 | furniture | pages [25] -->
Team # 2514362

<!-- b002044 | furniture | pages [25] -->
Page 24 of 26

<!-- b002045 | references | pages [25] -->
[4] Shi, H. M., Zhang, D. Y., & Zhang, Y. H. (2024). Can Olympic Medals Be Predicted?A

<!-- b002046 | references | pages [25] -->
Perspective from Explainable Machine Learning. Journal of Shanghai University of Sport, 48(4),

<!-- b002047 | references | pages [25] -->
26–36.

<!-- b002048 | references | pages [25] -->
[5] Wang, F. (2019). Prediction of 2020 Tokyo Olympic Medal Performance Based on Neural

<!-- b002049 | references | pages [25] -->
Networks. Statistics and Decision, (5), 89–91.

<!-- b002050 | references | pages [25] -->
[6] Zhao, W., Tang, T. R., & Wang, G. F. (2012). Study on Performance Prediction of 2012 London

<!-- b002051 | references | pages [25] -->
微信公众号：数学模型

<!-- b002052 | references | pages [25] -->
Olympics Based on v-SVR with Optimal Parameters. Journal of Anhui Normal University

<!-- b002053 | references | pages [25] -->
(Natural Science), 35(4), 381–386.

<!-- b002054 | references | pages [25] -->
[7] Cover, T. M., & Thomas, J. A. (2006). Elements of Information Theory (2nd ed.). Wiley-

<!-- b002055 | references | pages [25] -->
Interscience.

<!-- b002056 | references | pages [25] -->
[8] Kass, R. E., & Raftery, A. E. (1995). Bayes Factors. Journal of the American Statistical

<!-- b002057 | references | pages [25] -->
Association, 90(430), 773–795.

<!-- b002058 | references | pages [25] -->
微信号：MATHmodels

<!-- b002059 | references | pages [25] -->
m

<!-- b002060 | references | pages [25] -->
m

<!-- b002061 | references | pages [25] -->
m

<!-- b002062 | references | pages [25] -->
m

<!-- b002063 | references | pages [25] -->
m

<!-- b002064 | references | pages [25] -->
m

<!-- b002065 | references | pages [25] -->
m

<!-- b002066 | references | pages [25] -->
m

<!-- b002067 | references | pages [25] -->
m

<!-- b002068 | references | pages [25] -->
m

<!-- b002069 | references | pages [25] -->
m

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

<!-- b002289 | furniture | pages [25] -->
m

<!-- b002290 | furniture | pages [25] -->
m

<!-- b002291 | furniture | pages [25] -->
m

<!-- b002292 | furniture | pages [25] -->
m

<!-- b002293 | furniture | pages [25] -->
m

<!-- b002294 | furniture | pages [25] -->
m

<!-- b002295 | furniture | pages [25] -->
m

<!-- b002296 | furniture | pages [25] -->
m

<!-- b002297 | furniture | pages [25] -->
m

<!-- b002298 | furniture | pages [25] -->
m

<!-- b002299 | furniture | pages [25] -->
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

<!-- b002613 | furniture | pages [26] -->
Team # 2514362

<!-- b002614 | furniture | pages [26] -->
Page 25 of 26

<!-- b002615 | references | pages [26] -->
A

<!-- b002616 | heading | pages [26] -->
Report on the Use of AI

<!-- b002617 | ai_disclosure | pages [26] -->
1.OpenAI ChatGPT(May 14, 2024 version, ChatGPT-4o)

<!-- b002618 | ai_disclosure | pages [26] -->
Query1:How to effectively handle small sample data?

<!-- b002619 | ai_disclosure | pages [26] -->
Output:Handling small sample data effectively requires a combination of data-centric

<!-- b002620 | ai_disclosure | pages [26] -->
strategies and model adaptation techniques. First, augment the dataset artiﬁcially using

<!-- b002621 | ai_disclosure | pages [26] -->
methods like data augmentation (e.g., image rotation, noise injection) or synthetic data gen-

<!-- b002622 | ai_disclosure | pages [26] -->
eration (e.g., GANs, SMOTE). Feature engineering and dimensionality reduction (PCA, t-

<!-- b002623 | ai_disclosure | pages [26] -->
SNE) can also reduce noise and highlight meaningful patterns. These approaches mitigate

<!-- b002624 | ai_disclosure | pages [26] -->
overﬁtting by expanding or reﬁning the limited data while preserving its underlying struc-

<!-- b002625 | ai_disclosure | pages [26] -->
ture.

<!-- b002626 | ai_disclosure | pages [26] -->
Leverage transfer learning and simpliﬁed models to reduce dependency on large datasets.

<!-- b002627 | ai_disclosure | pages [26] -->
Pre-trained models can be ﬁne-tuned on small samples, as they carry prior knowledge from

<!-- b002628 | ai_disclosure | pages [26] -->
larger datasets. Simplify model architectures to avoid over-parameterization, and apply reg-

<!-- b002629 | ai_disclosure | pages [26] -->
ularization techniques (e.g., dropout, L1/L2) to penalize complexity. Meta-learning frame-

<!-- b002630 | ai_disclosure | pages [26] -->
works like MAML enable models to adapt quickly to new tasks with minimal data by learn-

<!-- b002631 | ai_disclosure | pages [26] -->
ing generalizable initialization parameters.

<!-- b002632 | ai_disclosure | pages [26] -->
Prioritize robust validation and hybrid learning paradigms. Use leave-one-out or strati-

<!-- b002633 | ai_disclosure | pages [26] -->
ﬁed k-fold cross-validation to assess model performance reliably. Combine semi-supervised

<!-- b002634 | ai_disclosure | pages [26] -->
learning (utilizing unlabeled data) with active learning, where the model iteratively queries

<!-- b002635 | ai_disclosure | pages [26] -->
the most informative samples for labeling. Techniques like bootstrapping improve stabil-

<!-- b002636 | ai_disclosure | pages [26] -->
ity, while Bayesian methods quantify uncertainty to guide decision-making. By integrating

<!-- b002637 | ai_disclosure | pages [26] -->
these strategies, small datasets can yield insights comparable to larger ones when handled

<!-- b002638 | ai_disclosure | pages [26] -->
thoughtfully.

<!-- b002639 | ai_disclosure | pages [26] -->
2.OpenAI ChatGPT(May 14, 2024 version, ChatGPT-4o)

<!-- b002640 | ai_disclosure | pages [26] -->
Query2:Explain information entropy.

<!-- b002641 | ai_disclosure | pages [26] -->
Output:Information entropy, introduced by Claude Shannon, quantiﬁes the uncertainty

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
or "disorder" in a system or dataset. It is deﬁned as H(X) = −∑p(xi) log2 p(xi), where p(xi)

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
m

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
m

<!-- b002887 | ai_disclosure | pages [26] -->
represents the probability of event xi. The higher the entropy, the more unpredictable the

<!-- b002888 | ai_disclosure | pages [26] -->
m

<!-- b002889 | ai_disclosure | pages [26] -->
m

<!-- b002890 | ai_disclosure | pages [26] -->
m

<!-- b002891 | ai_disclosure | pages [26] -->
m

<!-- b002892 | ai_disclosure | pages [26] -->
m

<!-- b002893 | ai_disclosure | pages [26] -->
m

<!-- b002894 | ai_disclosure | pages [26] -->
m

<!-- b002895 | ai_disclosure | pages [26] -->
m

<!-- b002896 | ai_disclosure | pages [26] -->
m

<!-- b002897 | ai_disclosure | pages [26] -->
m

<!-- b002898 | ai_disclosure | pages [26] -->
m

<!-- b002899 | ai_disclosure | pages [26] -->
m

<!-- b002900 | ai_disclosure | pages [26] -->
m

<!-- b002901 | ai_disclosure | pages [26] -->
m

<!-- b002902 | ai_disclosure | pages [26] -->
m

<!-- b002903 | ai_disclosure | pages [26] -->
m

<!-- b002904 | ai_disclosure | pages [26] -->
m

<!-- b002905 | ai_disclosure | pages [26] -->
m

<!-- b002906 | ai_disclosure | pages [26] -->
m

<!-- b002907 | ai_disclosure | pages [26] -->
m

<!-- b002908 | ai_disclosure | pages [26] -->
m

<!-- b002909 | ai_disclosure | pages [26] -->
m

<!-- b002910 | ai_disclosure | pages [26] -->
m

<!-- b002911 | ai_disclosure | pages [26] -->
m

<!-- b002912 | ai_disclosure | pages [26] -->
m

<!-- b002913 | ai_disclosure | pages [26] -->
m

<!-- b002914 | ai_disclosure | pages [26] -->
m

<!-- b002915 | ai_disclosure | pages [26] -->
m

<!-- b002916 | ai_disclosure | pages [26] -->
m

<!-- b002917 | ai_disclosure | pages [26] -->
m

<!-- b002918 | ai_disclosure | pages [26] -->
m

<!-- b002919 | ai_disclosure | pages [26] -->
m

<!-- b002920 | ai_disclosure | pages [26] -->
m

<!-- b002921 | ai_disclosure | pages [26] -->
m

<!-- b002922 | ai_disclosure | pages [26] -->
m

<!-- b002923 | ai_disclosure | pages [26] -->
m

<!-- b002924 | ai_disclosure | pages [26] -->
m

<!-- b002925 | ai_disclosure | pages [26] -->
m

<!-- b002926 | ai_disclosure | pages [26] -->
m

<!-- b002927 | ai_disclosure | pages [26] -->
m

<!-- b002928 | ai_disclosure | pages [26] -->
m

<!-- b002929 | ai_disclosure | pages [26] -->
m

<!-- b002930 | ai_disclosure | pages [26] -->
m

<!-- b002931 | ai_disclosure | pages [26] -->
m

<!-- b002932 | ai_disclosure | pages [26] -->
m

<!-- b002933 | ai_disclosure | pages [26] -->
m

<!-- b002934 | ai_disclosure | pages [26] -->
m

<!-- b002935 | ai_disclosure | pages [26] -->
m

<!-- b002936 | ai_disclosure | pages [26] -->
m

<!-- b002937 | ai_disclosure | pages [26] -->
m

<!-- b002938 | ai_disclosure | pages [26] -->
m

<!-- b002939 | ai_disclosure | pages [26] -->
m

<!-- b002940 | ai_disclosure | pages [26] -->
m

<!-- b002941 | ai_disclosure | pages [26] -->
m

<!-- b002942 | ai_disclosure | pages [26] -->
m

<!-- b002943 | ai_disclosure | pages [26] -->
m

<!-- b002944 | ai_disclosure | pages [26] -->
m

<!-- b002945 | ai_disclosure | pages [26] -->
m

<!-- b002946 | ai_disclosure | pages [26] -->
m

<!-- b002947 | ai_disclosure | pages [26] -->
m

<!-- b002948 | ai_disclosure | pages [26] -->
m

<!-- b002949 | ai_disclosure | pages [26] -->
m

<!-- b002950 | ai_disclosure | pages [26] -->
m

<!-- b002951 | ai_disclosure | pages [26] -->
m

<!-- b002952 | ai_disclosure | pages [26] -->
m

<!-- b002953 | ai_disclosure | pages [26] -->
m

<!-- b002954 | ai_disclosure | pages [26] -->
m

<!-- b002955 | ai_disclosure | pages [26] -->
m

<!-- b002956 | ai_disclosure | pages [26] -->
m

<!-- b002957 | ai_disclosure | pages [26] -->
m

<!-- b002958 | ai_disclosure | pages [26] -->
m

<!-- b002959 | ai_disclosure | pages [26] -->
m

<!-- b002960 | ai_disclosure | pages [26] -->
m

<!-- b002961 | ai_disclosure | pages [26] -->
m

<!-- b002962 | ai_disclosure | pages [26] -->
m

<!-- b002963 | ai_disclosure | pages [26] -->
m

<!-- b002964 | ai_disclosure | pages [26] -->
m

<!-- b002965 | ai_disclosure | pages [26] -->
m

<!-- b002966 | ai_disclosure | pages [26] -->
m

<!-- b002967 | ai_disclosure | pages [26] -->
m

<!-- b002968 | ai_disclosure | pages [26] -->
m

<!-- b002969 | ai_disclosure | pages [26] -->
m

<!-- b002970 | ai_disclosure | pages [26] -->
m

<!-- b002971 | ai_disclosure | pages [26] -->
m

<!-- b002972 | ai_disclosure | pages [26] -->
m

<!-- b002973 | ai_disclosure | pages [26] -->
m

<!-- b002974 | ai_disclosure | pages [26] -->
m

<!-- b002975 | ai_disclosure | pages [26] -->
m

<!-- b002976 | ai_disclosure | pages [26] -->
m

<!-- b002977 | ai_disclosure | pages [26] -->
m

<!-- b002978 | ai_disclosure | pages [26] -->
m

<!-- b002979 | ai_disclosure | pages [26] -->
m

<!-- b002980 | ai_disclosure | pages [26] -->
m

<!-- b002981 | ai_disclosure | pages [26] -->
m

<!-- b002982 | ai_disclosure | pages [26] -->
m

<!-- b002983 | ai_disclosure | pages [26] -->
m

<!-- b002984 | ai_disclosure | pages [26] -->
m

<!-- b002985 | ai_disclosure | pages [26] -->
m

<!-- b002986 | ai_disclosure | pages [26] -->
m

<!-- b002987 | ai_disclosure | pages [26] -->
m

<!-- b002988 | ai_disclosure | pages [26] -->
m

<!-- b002989 | ai_disclosure | pages [26] -->
m

<!-- b002990 | ai_disclosure | pages [26] -->
m

<!-- b002991 | ai_disclosure | pages [26] -->
m

<!-- b002992 | ai_disclosure | pages [26] -->
m

<!-- b002993 | ai_disclosure | pages [26] -->
m

<!-- b002994 | ai_disclosure | pages [26] -->
m

<!-- b002995 | ai_disclosure | pages [26] -->
m

<!-- b002996 | ai_disclosure | pages [26] -->
m

<!-- b002997 | ai_disclosure | pages [26] -->
m

<!-- b002998 | ai_disclosure | pages [26] -->
m

<!-- b002999 | ai_disclosure | pages [26] -->
m

<!-- b003000 | ai_disclosure | pages [26] -->
m

<!-- b003001 | ai_disclosure | pages [26] -->
m

<!-- b003002 | ai_disclosure | pages [26] -->
m

<!-- b003003 | ai_disclosure | pages [26] -->
m

<!-- b003004 | ai_disclosure | pages [26] -->
m

<!-- b003005 | ai_disclosure | pages [26] -->
m

<!-- b003006 | ai_disclosure | pages [26] -->
m

<!-- b003007 | ai_disclosure | pages [26] -->
m

<!-- b003008 | ai_disclosure | pages [26] -->
m

<!-- b003009 | ai_disclosure | pages [26] -->
m

<!-- b003010 | ai_disclosure | pages [26] -->
m

<!-- b003011 | ai_disclosure | pages [26] -->
m

<!-- b003012 | ai_disclosure | pages [26] -->
m

<!-- b003013 | ai_disclosure | pages [26] -->
m

<!-- b003014 | ai_disclosure | pages [26] -->
m

<!-- b003015 | ai_disclosure | pages [26] -->
m

<!-- b003016 | ai_disclosure | pages [26] -->
m

<!-- b003017 | ai_disclosure | pages [26] -->
m

<!-- b003018 | ai_disclosure | pages [26] -->
m

<!-- b003019 | ai_disclosure | pages [26] -->
m

<!-- b003020 | ai_disclosure | pages [26] -->
m

<!-- b003021 | ai_disclosure | pages [26] -->
m

<!-- b003022 | ai_disclosure | pages [26] -->
m

<!-- b003023 | ai_disclosure | pages [26] -->
m

<!-- b003024 | ai_disclosure | pages [26] -->
m

<!-- b003025 | ai_disclosure | pages [26] -->
m

<!-- b003026 | ai_disclosure | pages [26] -->
m

<!-- b003027 | ai_disclosure | pages [26] -->
m

<!-- b003028 | ai_disclosure | pages [26] -->
m

<!-- b003029 | ai_disclosure | pages [26] -->
m

<!-- b003030 | ai_disclosure | pages [26] -->
m

<!-- b003031 | ai_disclosure | pages [26] -->
system. For example, a fair coin (50% heads/tails) has maximum entropy (1 bit), while a bi-

<!-- b003032 | ai_disclosure | pages [26] -->
m

<!-- b003033 | ai_disclosure | pages [26] -->
m

<!-- b003034 | ai_disclosure | pages [26] -->
m

<!-- b003035 | ai_disclosure | pages [26] -->
m

<!-- b003036 | ai_disclosure | pages [26] -->
m

<!-- b003037 | ai_disclosure | pages [26] -->
m

<!-- b003038 | ai_disclosure | pages [26] -->
m

<!-- b003039 | ai_disclosure | pages [26] -->
m

<!-- b003040 | ai_disclosure | pages [26] -->
m

<!-- b003041 | ai_disclosure | pages [26] -->
m

<!-- b003042 | ai_disclosure | pages [26] -->
m

<!-- b003043 | ai_disclosure | pages [26] -->
m

<!-- b003044 | ai_disclosure | pages [26] -->
m

<!-- b003045 | ai_disclosure | pages [26] -->
m

<!-- b003046 | ai_disclosure | pages [26] -->
m

<!-- b003047 | ai_disclosure | pages [26] -->
m

<!-- b003048 | ai_disclosure | pages [26] -->
m

<!-- b003049 | ai_disclosure | pages [26] -->
m

<!-- b003050 | ai_disclosure | pages [26] -->
m

<!-- b003051 | ai_disclosure | pages [26] -->
m

<!-- b003052 | ai_disclosure | pages [26] -->
m

<!-- b003053 | ai_disclosure | pages [26] -->
m

<!-- b003054 | ai_disclosure | pages [26] -->
m

<!-- b003055 | ai_disclosure | pages [26] -->
m

<!-- b003056 | ai_disclosure | pages [26] -->
m

<!-- b003057 | ai_disclosure | pages [26] -->
m

<!-- b003058 | ai_disclosure | pages [26] -->
m

<!-- b003059 | ai_disclosure | pages [26] -->
m

<!-- b003060 | ai_disclosure | pages [26] -->
m

<!-- b003061 | ai_disclosure | pages [26] -->
m

<!-- b003062 | ai_disclosure | pages [26] -->
m

<!-- b003063 | ai_disclosure | pages [26] -->
m

<!-- b003064 | ai_disclosure | pages [26] -->
m

<!-- b003065 | ai_disclosure | pages [26] -->
m

<!-- b003066 | ai_disclosure | pages [26] -->
m

<!-- b003067 | ai_disclosure | pages [26] -->
m

<!-- b003068 | ai_disclosure | pages [26] -->
m

<!-- b003069 | ai_disclosure | pages [26] -->
m

<!-- b003070 | ai_disclosure | pages [26] -->
m

<!-- b003071 | ai_disclosure | pages [26] -->
m

<!-- b003072 | ai_disclosure | pages [26] -->
m

<!-- b003073 | ai_disclosure | pages [26] -->
m

<!-- b003074 | ai_disclosure | pages [26] -->
m

<!-- b003075 | ai_disclosure | pages [26] -->
m

<!-- b003076 | ai_disclosure | pages [26] -->
m

<!-- b003077 | ai_disclosure | pages [26] -->
m

<!-- b003078 | ai_disclosure | pages [26] -->
m

<!-- b003079 | ai_disclosure | pages [26] -->
m

<!-- b003080 | ai_disclosure | pages [26] -->
m

<!-- b003081 | ai_disclosure | pages [26] -->
m

<!-- b003082 | ai_disclosure | pages [26] -->
m

<!-- b003083 | ai_disclosure | pages [26] -->
m

<!-- b003084 | ai_disclosure | pages [26] -->
m

<!-- b003085 | ai_disclosure | pages [26] -->
m

<!-- b003086 | ai_disclosure | pages [26] -->
m

<!-- b003087 | ai_disclosure | pages [26] -->
m

<!-- b003088 | ai_disclosure | pages [26] -->
m

<!-- b003089 | ai_disclosure | pages [26] -->
m

<!-- b003090 | ai_disclosure | pages [26] -->
m

<!-- b003091 | ai_disclosure | pages [26] -->
m

<!-- b003092 | ai_disclosure | pages [26] -->
m

<!-- b003093 | ai_disclosure | pages [26] -->
m

<!-- b003094 | ai_disclosure | pages [26] -->
m

<!-- b003095 | ai_disclosure | pages [26] -->
m

<!-- b003096 | ai_disclosure | pages [26] -->
m

<!-- b003097 | ai_disclosure | pages [26] -->
m

<!-- b003098 | ai_disclosure | pages [26] -->
m

<!-- b003099 | ai_disclosure | pages [26] -->
m

<!-- b003100 | ai_disclosure | pages [26] -->
m

<!-- b003101 | ai_disclosure | pages [26] -->
m

<!-- b003102 | ai_disclosure | pages [26] -->
m

<!-- b003103 | ai_disclosure | pages [26] -->
m

<!-- b003104 | ai_disclosure | pages [26] -->
m

<!-- b003105 | ai_disclosure | pages [26] -->
m

<!-- b003106 | ai_disclosure | pages [26] -->
m

<!-- b003107 | ai_disclosure | pages [26] -->
m

<!-- b003108 | ai_disclosure | pages [26] -->
m

<!-- b003109 | ai_disclosure | pages [26] -->
m

<!-- b003110 | ai_disclosure | pages [26] -->
m

<!-- b003111 | ai_disclosure | pages [26] -->
m

<!-- b003112 | ai_disclosure | pages [26] -->
m

<!-- b003113 | ai_disclosure | pages [26] -->
m

<!-- b003114 | ai_disclosure | pages [26] -->
m

<!-- b003115 | ai_disclosure | pages [26] -->
m

<!-- b003116 | ai_disclosure | pages [26] -->
m

<!-- b003117 | ai_disclosure | pages [26] -->
m

<!-- b003118 | ai_disclosure | pages [26] -->
m

<!-- b003119 | ai_disclosure | pages [26] -->
m

<!-- b003120 | ai_disclosure | pages [26] -->
m

<!-- b003121 | ai_disclosure | pages [26] -->
m

<!-- b003122 | ai_disclosure | pages [26] -->
m

<!-- b003123 | ai_disclosure | pages [26] -->
m

<!-- b003124 | ai_disclosure | pages [26] -->
m

<!-- b003125 | ai_disclosure | pages [26] -->
m

<!-- b003126 | ai_disclosure | pages [26] -->
m

<!-- b003127 | ai_disclosure | pages [26] -->
m

<!-- b003128 | ai_disclosure | pages [26] -->
m

<!-- b003129 | ai_disclosure | pages [26] -->
m

<!-- b003130 | ai_disclosure | pages [26] -->
m

<!-- b003131 | ai_disclosure | pages [26] -->
m

<!-- b003132 | ai_disclosure | pages [26] -->
m

<!-- b003133 | ai_disclosure | pages [26] -->
m

<!-- b003134 | ai_disclosure | pages [26] -->
m

<!-- b003135 | ai_disclosure | pages [26] -->
m

<!-- b003136 | ai_disclosure | pages [26] -->
m

<!-- b003137 | ai_disclosure | pages [26] -->
m

<!-- b003138 | ai_disclosure | pages [26] -->
m

<!-- b003139 | ai_disclosure | pages [26] -->
m

<!-- b003140 | ai_disclosure | pages [26] -->
m

<!-- b003141 | ai_disclosure | pages [26] -->
m

<!-- b003142 | ai_disclosure | pages [26] -->
m

<!-- b003143 | ai_disclosure | pages [26] -->
m

<!-- b003144 | ai_disclosure | pages [26] -->
m

<!-- b003145 | ai_disclosure | pages [26] -->
m

<!-- b003146 | ai_disclosure | pages [26] -->
m

<!-- b003147 | ai_disclosure | pages [26] -->
m

<!-- b003148 | ai_disclosure | pages [26] -->
m

<!-- b003149 | ai_disclosure | pages [26] -->
m

<!-- b003150 | ai_disclosure | pages [26] -->
m

<!-- b003151 | ai_disclosure | pages [26] -->
m

<!-- b003152 | ai_disclosure | pages [26] -->
m

<!-- b003153 | ai_disclosure | pages [26] -->
m

<!-- b003154 | ai_disclosure | pages [26] -->
m

<!-- b003155 | ai_disclosure | pages [26] -->
m

<!-- b003156 | ai_disclosure | pages [26] -->
m

<!-- b003157 | ai_disclosure | pages [26] -->
m

<!-- b003158 | ai_disclosure | pages [26] -->
m

<!-- b003159 | ai_disclosure | pages [26] -->
m

<!-- b003160 | ai_disclosure | pages [26] -->
m

<!-- b003161 | ai_disclosure | pages [26] -->
m

<!-- b003162 | ai_disclosure | pages [26] -->
m

<!-- b003163 | ai_disclosure | pages [26] -->
m

<!-- b003164 | ai_disclosure | pages [26] -->
m

<!-- b003165 | ai_disclosure | pages [26] -->
m

<!-- b003166 | ai_disclosure | pages [26] -->
m

<!-- b003167 | ai_disclosure | pages [26] -->
m

<!-- b003168 | ai_disclosure | pages [26] -->
m

<!-- b003169 | ai_disclosure | pages [26] -->
m

<!-- b003170 | ai_disclosure | pages [26] -->
m

<!-- b003171 | ai_disclosure | pages [26] -->
m

<!-- b003172 | ai_disclosure | pages [26] -->
m

<!-- b003173 | ai_disclosure | pages [26] -->
m

<!-- b003174 | ai_disclosure | pages [26] -->
m

<!-- b003175 | ai_disclosure | pages [26] -->
m

<!-- b003176 | ai_disclosure | pages [26] -->
m

<!-- b003177 | ai_disclosure | pages [26] -->
ased coin (100% heads) has zero entropy. Entropy essentially measures the average informa-

<!-- b003178 | ai_disclosure | pages [26] -->
m

<!-- b003179 | ai_disclosure | pages [26] -->
m

<!-- b003180 | ai_disclosure | pages [26] -->
m

<!-- b003181 | ai_disclosure | pages [26] -->
m

<!-- b003182 | ai_disclosure | pages [26] -->
m

<!-- b003183 | ai_disclosure | pages [26] -->
m

<!-- b003184 | ai_disclosure | pages [26] -->
m

<!-- b003185 | ai_disclosure | pages [26] -->
m

<!-- b003186 | ai_disclosure | pages [26] -->
m

<!-- b003187 | ai_disclosure | pages [26] -->
m

<!-- b003188 | ai_disclosure | pages [26] -->
m

<!-- b003189 | ai_disclosure | pages [26] -->
m

<!-- b003190 | ai_disclosure | pages [26] -->
m

<!-- b003191 | ai_disclosure | pages [26] -->
m

<!-- b003192 | ai_disclosure | pages [26] -->
m

<!-- b003193 | ai_disclosure | pages [26] -->
m

<!-- b003194 | ai_disclosure | pages [26] -->
m

<!-- b003195 | ai_disclosure | pages [26] -->
m

<!-- b003196 | ai_disclosure | pages [26] -->
m

<!-- b003197 | ai_disclosure | pages [26] -->
m

<!-- b003198 | ai_disclosure | pages [26] -->
m

<!-- b003199 | ai_disclosure | pages [26] -->
m

<!-- b003200 | ai_disclosure | pages [26] -->
m

<!-- b003201 | ai_disclosure | pages [26] -->
m

<!-- b003202 | ai_disclosure | pages [26] -->
m

<!-- b003203 | ai_disclosure | pages [26] -->
m

<!-- b003204 | ai_disclosure | pages [26] -->
m

<!-- b003205 | ai_disclosure | pages [26] -->
m

<!-- b003206 | ai_disclosure | pages [26] -->
m

<!-- b003207 | ai_disclosure | pages [26] -->
m

<!-- b003208 | ai_disclosure | pages [26] -->
m

<!-- b003209 | ai_disclosure | pages [26] -->
m

<!-- b003210 | ai_disclosure | pages [26] -->
m

<!-- b003211 | ai_disclosure | pages [26] -->
m

<!-- b003212 | ai_disclosure | pages [26] -->
m

<!-- b003213 | ai_disclosure | pages [26] -->
m

<!-- b003214 | ai_disclosure | pages [26] -->
m

<!-- b003215 | ai_disclosure | pages [26] -->
m

<!-- b003216 | ai_disclosure | pages [26] -->
m

<!-- b003217 | ai_disclosure | pages [26] -->
m

<!-- b003218 | ai_disclosure | pages [26] -->
m

<!-- b003219 | ai_disclosure | pages [26] -->
m

<!-- b003220 | ai_disclosure | pages [26] -->
m

<!-- b003221 | ai_disclosure | pages [26] -->
m

<!-- b003222 | ai_disclosure | pages [26] -->
m

<!-- b003223 | ai_disclosure | pages [26] -->
m

<!-- b003224 | ai_disclosure | pages [26] -->
m

<!-- b003225 | ai_disclosure | pages [26] -->
m

<!-- b003226 | ai_disclosure | pages [26] -->
m

<!-- b003227 | ai_disclosure | pages [26] -->
m

<!-- b003228 | ai_disclosure | pages [26] -->
m

<!-- b003229 | ai_disclosure | pages [26] -->
m

<!-- b003230 | ai_disclosure | pages [26] -->
m

<!-- b003231 | ai_disclosure | pages [26] -->
m

<!-- b003232 | ai_disclosure | pages [26] -->
m

<!-- b003233 | ai_disclosure | pages [26] -->
m

<!-- b003234 | ai_disclosure | pages [26] -->
m

<!-- b003235 | ai_disclosure | pages [26] -->
m

<!-- b003236 | ai_disclosure | pages [26] -->
m

<!-- b003237 | ai_disclosure | pages [26] -->
m

<!-- b003238 | ai_disclosure | pages [26] -->
m

<!-- b003239 | ai_disclosure | pages [26] -->
m

<!-- b003240 | ai_disclosure | pages [26] -->
m

<!-- b003241 | ai_disclosure | pages [26] -->
m

<!-- b003242 | ai_disclosure | pages [26] -->
m

<!-- b003243 | ai_disclosure | pages [26] -->
m

<!-- b003244 | ai_disclosure | pages [26] -->
m

<!-- b003245 | ai_disclosure | pages [26] -->
m

<!-- b003246 | ai_disclosure | pages [26] -->
m

<!-- b003247 | ai_disclosure | pages [26] -->
m

<!-- b003248 | ai_disclosure | pages [26] -->
m

<!-- b003249 | ai_disclosure | pages [26] -->
m

<!-- b003250 | ai_disclosure | pages [26] -->
m

<!-- b003251 | ai_disclosure | pages [26] -->
m

<!-- b003252 | ai_disclosure | pages [26] -->
m

<!-- b003253 | ai_disclosure | pages [26] -->
m

<!-- b003254 | ai_disclosure | pages [26] -->
m

<!-- b003255 | ai_disclosure | pages [26] -->
m

<!-- b003256 | ai_disclosure | pages [26] -->
m

<!-- b003257 | ai_disclosure | pages [26] -->
m

<!-- b003258 | ai_disclosure | pages [26] -->
m

<!-- b003259 | ai_disclosure | pages [26] -->
m

<!-- b003260 | ai_disclosure | pages [26] -->
m

<!-- b003261 | ai_disclosure | pages [26] -->
m

<!-- b003262 | ai_disclosure | pages [26] -->
m

<!-- b003263 | ai_disclosure | pages [26] -->
m

<!-- b003264 | ai_disclosure | pages [26] -->
m

<!-- b003265 | ai_disclosure | pages [26] -->
m

<!-- b003266 | ai_disclosure | pages [26] -->
m

<!-- b003267 | ai_disclosure | pages [26] -->
m

<!-- b003268 | ai_disclosure | pages [26] -->
m

<!-- b003269 | ai_disclosure | pages [26] -->
m

<!-- b003270 | ai_disclosure | pages [26] -->
m

<!-- b003271 | ai_disclosure | pages [26] -->
m

<!-- b003272 | ai_disclosure | pages [26] -->
m

<!-- b003273 | ai_disclosure | pages [26] -->
m

<!-- b003274 | ai_disclosure | pages [26] -->
m

<!-- b003275 | ai_disclosure | pages [26] -->
m

<!-- b003276 | ai_disclosure | pages [26] -->
m

<!-- b003277 | ai_disclosure | pages [26] -->
m

<!-- b003278 | ai_disclosure | pages [26] -->
m

<!-- b003279 | ai_disclosure | pages [26] -->
m

<!-- b003280 | ai_disclosure | pages [26] -->
m

<!-- b003281 | ai_disclosure | pages [26] -->
m

<!-- b003282 | ai_disclosure | pages [26] -->
m

<!-- b003283 | ai_disclosure | pages [26] -->
m

<!-- b003284 | ai_disclosure | pages [26] -->
m

<!-- b003285 | ai_disclosure | pages [26] -->
m

<!-- b003286 | ai_disclosure | pages [26] -->
m

<!-- b003287 | ai_disclosure | pages [26] -->
m

<!-- b003288 | ai_disclosure | pages [26] -->
m

<!-- b003289 | ai_disclosure | pages [26] -->
m

<!-- b003290 | ai_disclosure | pages [26] -->
m

<!-- b003291 | ai_disclosure | pages [26] -->
m

<!-- b003292 | ai_disclosure | pages [26] -->
m

<!-- b003293 | ai_disclosure | pages [26] -->
m

<!-- b003294 | ai_disclosure | pages [26] -->
m

<!-- b003295 | ai_disclosure | pages [26] -->
m

<!-- b003296 | ai_disclosure | pages [26] -->
m

<!-- b003297 | ai_disclosure | pages [26] -->
m

<!-- b003298 | ai_disclosure | pages [26] -->
m

<!-- b003299 | ai_disclosure | pages [26] -->
m

<!-- b003300 | ai_disclosure | pages [26] -->
m

<!-- b003301 | ai_disclosure | pages [26] -->
m

<!-- b003302 | ai_disclosure | pages [26] -->
m

<!-- b003303 | ai_disclosure | pages [26] -->
m

<!-- b003304 | ai_disclosure | pages [26] -->
m

<!-- b003305 | ai_disclosure | pages [26] -->
m

<!-- b003306 | ai_disclosure | pages [26] -->
m

<!-- b003307 | ai_disclosure | pages [26] -->
m

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
tion gained when resolving uncertaintymore chaotic systems require more bits to describe

<!-- b003334 | ai_disclosure | pages [26] -->
outcomes.

<!-- b003335 | ai_disclosure | pages [26] -->
Practically, entropy is foundational in ﬁelds like data compression (low-entropy data is

<!-- b003336 | ai_disclosure | pages [26] -->
easier to compress), cryptography (high-entropy randomness enhances security), and ma-

<!-- b003337 | ai_disclosure | pages [26] -->
chine learning. In ML, entropy guides decision-making: decision trees split features to min-

<!-- b003338 | ai_disclosure | pages [26] -->
imize entropy, improving class purity. It also underpins metrics for evaluating model uncer-

<!-- b003339 | ai_disclosure | pages [26] -->
tainty. By quantifying unpredictability, entropy bridges theoretical information theory and

<!-- b003340 | ai_disclosure | pages [26] -->
real-world applications, enabling efﬁcient data handling and informed predictions.

<!-- b003341 | ai_disclosure | pages [26] -->
3.OpenAI ChatGPT(May 14, 2024 version, ChatGPT-4o)

<!-- b003342 | ai_disclosure | pages [26] -->
Query3: What is the role of Laplacian Smoothing?

<!-- b003343 | ai_disclosure | pages [26] -->
Output: Laplacian Smoothing (or add-one smoothing) is a technique used to handle

<!-- b003344 | ai_disclosure | pages [26] -->
zero-probability issues in datasets, particularly in probability estimation tasks like text clas-

<!-- b003345 | ai_disclosure | pages [26] -->
siﬁcation or naïve Bayes models. When a categorical feature or event in training data has

<!-- b003346 | ai_disclosure | pages [26] -->
no observed occurrences (e.g., a word never appearing in a spam email dataset), traditional

<!-- b003347 | ai_disclosure | pages [26] -->
frequency-based probability calculations would assign it a probability of zero. This leads to

<!-- b003348 | ai_disclosure | pages [26] -->
model failure when encountering unseen data. Laplacian smoothing resolves this by adding

<!-- b003349 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b003350 | furniture | pages [26] -->
2

<!-- b003351 | furniture | pages [26] -->
MATHmodels

<!-- b003352 | furniture | pages [26] -->
获取更多资讯

<!-- b003353 | furniture | pages [27] -->
Page 26 of 26

<!-- b003354 | furniture | pages [27] -->
Team # 2514362

<!-- b003355 | ai_disclosure | pages [27] -->
a small constant (often 1) to each count, ensuring no event has zero probability while main-

<!-- b003356 | ai_disclosure | pages [27] -->
taining a valid probability distribution.

<!-- b003357 | ai_disclosure | pages [27] -->
The core benefit lies in balancing robustness and generalization. By artificially intro-

<!-- b003358 | ai_disclosure | pages [27] -->
ducing pseudo-counts, it prevents overfitting to sparse training data and accounts for the

<!-- b003359 | ai_disclosure | pages [27] -->
possibility of rare or unseen events in real-world scenarios. For instance, in natural language

<!-- b003360 | ai_disclosure | pages [27] -->
processing (NLP), it avoids assigning zero likelihood to unobserved n-grams, enabling mod-

<!-- b003361 | ai_disclosure | pages [27] -->
els to handle new phrases gracefully. This regularization effect improves model reliability,

<!-- b003362 | ai_disclosure | pages [27] -->
especially in low-data regimes or highly imbalanced datasets.

<!-- b003363 | ai_disclosure | pages [27] -->
Applications extend beyond text analysis. It is widely used in recommendation systems

<!-- b003364 | ai_disclosure | pages [27] -->
(to address cold-start problems), genetics (for rare gene sequence predictions), and Bayesian

<!-- b003365 | ai_disclosure | pages [27] -->
ne -rn  n r n r ss o an

<!-- b003366 | ai_disclosure | pages [27] -->
sometimes oversimplify complex distributionsalternatives like Lidstone smoothing (using

<!-- b003367 | ai_disclosure | pages [27] -->
fractional constants) offer more flexibility. Nevertheless, its computational efficiency and in-

<!-- b003368 | ai_disclosure | pages [27] -->
terpretability make it a foundational tool for mitigating data sparsity in probabilistic models.

<!-- b003369 | ai_disclosure | pages [27] -->
4.OpenAI ChatGPT(May 14, 2024 version, ChatGPT-4o)

<!-- b003370 | ai_disclosure | pages [27] -->
Query4: How to conduct Ablation Study?

<!-- b003371 | ai_disclosure | pages [27] -->
Output:An ablation study is a method used in machine learning and neural network

<!-- b003372 | ai_disclosure | pages [27] -->
research to determine the contribution of individual components or features to the overall

<!-- b003373 | ai_disclosure | pages [27] -->
performance of a model. To conduct an ablation study, start by identifying the components

<!-- b003374 | ai_disclosure | pages [27] -->
you wish to evaluate. These can be specific layers in a neural network, certain features in a

<!-- b003375 | ai_disclosure | pages [27] -->
dataset, preprocessing steps, or even hyperparameters. Once the components are identified,

<!-- b003376 | ai_disclosure | pages [27] -->
create multiple versions of your model, each with a different component or combination of

<!-- b003377 | ai_disclosure | pages [27] -->
components removed or altered. The baseline model is the full model with all components

<!-- b003378 | ai_disclosure | pages [27] -->
intact, and each subsequent model represents a removal or modification of a part of the

<!-- b003379 | ai_disclosure | pages [27] -->
model.

<!-- b003380 | ai_disclosure | pages [27] -->
Next, train each version of the model under the same conditions and evaluate them

<!-- b003381 | ai_disclosure | pages [27] -->
using the same metrics to ensure comparability. Analyze the differences in performance

<!-- b003382 | ai_disclosure | pages [27] -->
between the baseline and the modified models to understand the impact of each component.

<!-- b003383 | ai_disclosure | pages [27] -->
This process helps in identifying which parts of the model are crucial for its performance

<!-- b003384 | ai_disclosure | pages [27] -->
and which can be refined or removed to potentially simplify the architecture or improve

<!-- b003385 | ai_disclosure | pages [27] -->
efficiency without significant loss of accuracy. Ablation studies are essential for gaining

<!-- b003386 | ai_disclosure | pages [27] -->
deeper insights into how different aspects of a model affect its outcomes, facilitating more

<!-- b003387 | ai_disclosure | pages [27] -->
informed decisions in model design and optimization.

<!-- b003388 | ai_disclosure | pages [27] -->
信

<!-- b003389 | ai_disclosure | pages [27] -->
微
