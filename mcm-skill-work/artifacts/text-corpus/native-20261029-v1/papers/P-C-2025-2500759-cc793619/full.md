# P-C-2025-2500759-cc793619

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

<!-- b000006 | title | pages [1] -->
2500759

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Olympic Multi-dimensional Predictive Integrator

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
To ensure a systematic and multidimensional approach to Olympic medal prediction, this study constructs a dynamic and coupled comprehensive prediction framework. This framework integrates various objectives, including medal distribution prediction, break-

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
through country identification, event performance evaluation, and the impact analysis of coaching resource allocation. By employing multi-source heterogeneous data fusion and machine learning integration methods, we achieve an in-depth analysis and reliable pre- diction of the development patterns in competitive sports.

<!-- b000013 | prose | pages [1] -->
First, we develop a multidimensional predictive model to analyze Olympic medal patterns. Utilizing Principal Component Analysis (PCA) for dimensionality reduction and noise filtering of the Olympic event dataset, we combine Long Short-Term Mem- ory (LSTM) networks to mine temporal features and integrate home advantage effects. A dual-channel XGBoost-Bootstrap model is established to generate predictions with a 95% confidence interval. The results indicate an upward trend for countries such as

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
the United States and the United Kingdom, while countries like France and China show a decline. The model has a low MAE and MAPE, exhibiting a high accuracy and strong ro- bustness. Through non-parametric testing, potential breakthrough countries are identified, with San Marino and Kuwait showing gold medal breakthrough probabilities of 84.7% and 68.4%, respectively. Event analysis reveals a strong correlation between swimming, athletics, and medal counts, while SHapley Additive exPlanations (SHAP) quantifies shooting as a core contributing event. Principal component analysis uncovers the positive driving effects of swimming and wrestling on medal augmentation, informing optimal sports event allocation.

<!-- b000016 | prose | pages [1] -->
Subsequently, we develop a Difference-in-Differences (DID) model to quantify the competitive benefits of coaching replacement and conduct statistical significance tests as well as parallel trends tests to ensure the reliability of our results. It is found that during the 2020-2024 period, Australia, South Korea, and Poland experienced significant "great coach" policy effects through strategic restructuring of their coaching teams. Based on this, we recommend prioritizing investment in high-elasticity projects.

<!-- b000017 | prose | pages [1] -->
Finally, we synthesize all models and analyses to present new insights and corre- sponding decision supports.

<!-- b000018 | keywords | pages [1] -->
Keywords: Prediction Model, PCA, LSTM, XGBoost, SHAP, DID

<!-- b000019 | furniture | pages [3] -->
Team # 2500759

<!-- b000020 | furniture | pages [3] -->
Page 3 of 26

<!-- b000021 | prose | pages [3] -->
1

<!-- b000022 | heading | pages [3] -->
Introduction

<!-- b000023 | prose | pages [3] -->
1.1 Problem Background

<!-- b000024 | prose | pages [3] -->
The medal standings of the 2024 Paris Summer Olympics illustrate the diversity of international sports competition: the United States led with 126 total medals, while China tied for the gold medal count. The host nation, France, underscores the advantages of hosting by securing the fourth position in total medal accumulation. Emerging powers such as Albania have achieved their first gold medal, whereas over 60 countries have yet to register any medals, reflecting the uneven distribution of competitive resources.

<!-- b000025 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000026 | prose | pages [3] -->
Current predictions largely rely on pre-competition data6; however, key variables such as historical trends, adjustments to events, and coaching effects have not yet been adequately quantified. By constructing data-driven models2, it becomes possible to accurately iden- tify potential medal-winning events, optimize coaching resources, leverage host country advantages, and reveal the pathways to the emergence of "invisible champions". This ap- proach provides dynamic insights that can aid nations in formulating strategies and foster a rebalancing of the Olympic landscape.

<!-- b000027 | prose | pages [3] -->
1.2 Clarifications and Restatements

<!-- b000028 | prose | pages [3] -->
Given the background information and constraints of the problem, we must complete

<!-- b000029 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000030 | prose | pages [3] -->
the following tasks:

<!-- b000031 | prose | pages [3] -->
Task 1: Develop a model to predict gold and total medal counts for each country at the 2028 Los Angeles Olympics and compare predictions with the 2024 Paris Olympics. Task 2: Identify countries expected to win their first medals at the upcoming Olympics using the model from Task 1, and estimate the likelihood of a "zero breakthrough". Task 3: Analyze the relationship between Olympic sports and medal counts, considering the impact of the host nation and selected sports. Task 4: Create a model to identify countries with the "great coach" effect in specific sports and provide contribution coefficients. Task 5: Based on the topic and the work conducted, additional original insights are pre- sented.

<!-- b000032 | prose | pages [3] -->
1.3 Our Work

<!-- b000033 | prose | pages [3] -->
First, dimensionality reduction is performed using PCA. Next, trend information is incorporated through LSTM, leading to the establishment of an XGBoost prediction model. Subsequently, the Wlicoxon signed rank test is employed to investigate which countries achieve a breakthrough in winning their first medals and to determine the cor- responding probabilities. Furthermore, Spearman correlation coefficients and SHAP are utilized to conduct relationship and importance analyses. Finally, a DID approach is ap- plied to examine the "great coach" effect and provide new insights. For ease of description and visualization, we have drawn Fig. 1 to represent our work.

<!-- b000034 | prose | pages [3] -->
2

<!-- b000035 | heading | pages [3] -->
Preparation for Modeling

<!-- b000036 | prose | pages [3] -->
2.1

<!-- b000037 | heading | pages [3] -->
Model Assumptions

<!-- b000038 | prose | pages [3] -->
Some fundamental assumptions are listed below.

<!-- b000039 | heading | pages [3] -->
• Assumption 1: Athletes are in optimal physical condition throughout the competi-

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

<!-- b000323 | prose | pages [3] -->
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

<!-- b000726 | furniture | pages [3] -->
m

<!-- b000727 | furniture | pages [5] -->
Team # 2500759

<!-- b000728 | furniture | pages [5] -->
Page 5 of 26

<!-- b000729 | prose | pages [5] -->
can observe that the scale of information constitutes a small dataset. However, the data is lengthy and complex, with intricate relationships among different data points, represent- ing a type of data pertinent to decision-making in real-world scenarios.

<!-- b000730 | prose | pages [5] -->
• For attachment 2, we will perform a natural join with the "summerOly_medal_counts" dataset to match the columns for country names and their abbreviations, thereby en- hancing the information provided. • During the data aggregation process, we will retrieve and consolidate data from attachment 2 based on the fields "Team," "Year," "Sport," and "Medal," calculating the medal counts for each country in every Olympic event. Furthermore, we will merge and compute data for various sports across different years, thereby deriving the types and counts of events for each Olympic Games, which will provide vital

<!-- b000731 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000732 | prose | pages [5] -->
data support for subsequent medal predictions and trend analysis. • For attachment 5, we will address missing values in the columns "Code," "Sports Governing Body," and "Year" through interpolation methods and by removing rows or columns that contain missing values.

<!-- b000733 | prose | pages [5] -->
3 Problem 1: Medal Prediction

<!-- b000734 | prose | pages [5] -->
This study focuses on predicting medal counts for the 2028 Los Angeles Olympic Games. By considering the interval prediction of medal rankings and recognizing the memoryless characteristic of Olympic medal trends akin to Markov chains, we employ an

<!-- b000735 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000736 | prose | pages [5] -->
innovative XGBoost5 algorithm enhanced by PCA8,9 and LSTM3,7 to model predictions for gold and total medal rankings while assessing model uncertainty. Using the PCA- LSTM-enhanced dataset from 2024, we derive predictive intervals for the gold and total medals by country for 2028, facilitating performance prediction analysis.

<!-- b000737 | prose | pages [5] -->
In terms of predicting the probability of nations "breaking the zero" for gold medals, we analyze the interval prediction results from XGBoost. We perform a symmetric rank sum test on Bootstrap samples where point estimates are greater than or equal to 1, con- cluding that countries with a P-value less than 0.05 are likely to achieve at least one gold medal in 2028.

<!-- b000738 | prose | pages [5] -->
Additionally, we examine the correlation and importance of different Olympic events in relation to countries’ medal counts. We start with a Spearman correlation analysis be- tween gold and total medal counts for each country in 2024 and the weighted values of key Olympic events. Building on our PCA-LSTM-enhanced XGBoost model, we utilize SHAP analysis to assess the importance of each sport based on principal component im- portance values. Univariate dependence plots further explore the relationships between individual sports and overall gold and medal counts, while SHAP force plots provide insights into the interrelationships and significance of different sports within nations re- garding their gold and total medal counts.

<!-- b000739 | prose | pages [5] -->
3.1 Medal Ranking

<!-- b000740 | prose | pages [5] -->
3.1.1 PCA: Reducing Dimensions

<!-- b000741 | prose | pages [5] -->
In predicting Olympic gold medals and rankings, outcomes are closely linked to the medal counts and compositions from previous Games. Thus, we weighted the gold, silver, and bronze medals of each country in major sporting events at 50%, 30%, and 20%, respectively, to assess their potential impact on future medal standings.

<!-- b000742 | prose | pages [5] -->
m

<!-- b000743 | prose | pages [5] -->
m

<!-- b000744 | prose | pages [5] -->
m

<!-- b000745 | prose | pages [5] -->
m

<!-- b000746 | prose | pages [5] -->
m

<!-- b000747 | prose | pages [5] -->
m

<!-- b000748 | prose | pages [5] -->
m

<!-- b000749 | prose | pages [5] -->
m

<!-- b000750 | prose | pages [5] -->
m

<!-- b000751 | prose | pages [5] -->
m

<!-- b000752 | prose | pages [5] -->
m

<!-- b000753 | prose | pages [5] -->
m

<!-- b000754 | prose | pages [5] -->
m

<!-- b000755 | prose | pages [5] -->
m

<!-- b000756 | prose | pages [5] -->
m

<!-- b000757 | prose | pages [5] -->
m

<!-- b000758 | prose | pages [5] -->
m

<!-- b000759 | prose | pages [5] -->
m

<!-- b000760 | prose | pages [5] -->
m

<!-- b000761 | prose | pages [5] -->
m

<!-- b000762 | prose | pages [5] -->
m

<!-- b000763 | prose | pages [5] -->
m

<!-- b000764 | prose | pages [5] -->
m

<!-- b000765 | prose | pages [5] -->
m

<!-- b000766 | prose | pages [5] -->
m

<!-- b000767 | prose | pages [5] -->
m

<!-- b000768 | prose | pages [5] -->
m

<!-- b000769 | prose | pages [5] -->
m

<!-- b000770 | prose | pages [5] -->
m

<!-- b000771 | prose | pages [5] -->
m

<!-- b000772 | prose | pages [5] -->
m

<!-- b000773 | prose | pages [5] -->
m

<!-- b000774 | prose | pages [5] -->
m

<!-- b000775 | prose | pages [5] -->
m

<!-- b000776 | prose | pages [5] -->
m

<!-- b000777 | prose | pages [5] -->
m

<!-- b000778 | prose | pages [5] -->
m

<!-- b000779 | prose | pages [5] -->
m

<!-- b000780 | prose | pages [5] -->
m

<!-- b000781 | prose | pages [5] -->
m

<!-- b000782 | prose | pages [5] -->
m

<!-- b000783 | prose | pages [5] -->
m

<!-- b000784 | prose | pages [5] -->
m

<!-- b000785 | prose | pages [5] -->
m

<!-- b000786 | prose | pages [5] -->
m

<!-- b000787 | prose | pages [5] -->
m

<!-- b000788 | prose | pages [5] -->
m

<!-- b000789 | prose | pages [5] -->
m

<!-- b000790 | prose | pages [5] -->
m

<!-- b000791 | prose | pages [5] -->
m

<!-- b000792 | prose | pages [5] -->
m

<!-- b000793 | prose | pages [5] -->
m

<!-- b000794 | prose | pages [5] -->
m

<!-- b000795 | prose | pages [5] -->
m

<!-- b000796 | prose | pages [5] -->
m

<!-- b000797 | prose | pages [5] -->
m

<!-- b000798 | prose | pages [5] -->
m

<!-- b000799 | prose | pages [5] -->
m

<!-- b000800 | prose | pages [5] -->
m

<!-- b000801 | prose | pages [5] -->
m

<!-- b000802 | prose | pages [5] -->
m

<!-- b000803 | prose | pages [5] -->
m

<!-- b000804 | prose | pages [5] -->
m

<!-- b000805 | prose | pages [5] -->
m

<!-- b000806 | prose | pages [5] -->
m

<!-- b000807 | prose | pages [5] -->
m

<!-- b000808 | prose | pages [5] -->
m

<!-- b000809 | prose | pages [5] -->
m

<!-- b000810 | prose | pages [5] -->
m

<!-- b000811 | prose | pages [5] -->
m

<!-- b000812 | prose | pages [5] -->
m

<!-- b000813 | prose | pages [5] -->
m

<!-- b000814 | prose | pages [5] -->
m

<!-- b000815 | prose | pages [5] -->
m

<!-- b000816 | prose | pages [5] -->
m

<!-- b000817 | prose | pages [5] -->
m

<!-- b000818 | prose | pages [5] -->
m

<!-- b000819 | prose | pages [5] -->
m

<!-- b000820 | prose | pages [5] -->
m

<!-- b000821 | prose | pages [5] -->
m

<!-- b000822 | prose | pages [5] -->
m

<!-- b000823 | prose | pages [5] -->
m

<!-- b000824 | prose | pages [5] -->
m

<!-- b000825 | prose | pages [5] -->
m

<!-- b000826 | prose | pages [5] -->
m

<!-- b000827 | prose | pages [5] -->
m

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
m

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

<!-- b001026 | furniture | pages [5] -->
m

<!-- b001027 | furniture | pages [5] -->
m

<!-- b001028 | furniture | pages [5] -->
m

<!-- b001029 | furniture | pages [5] -->
m

<!-- b001030 | furniture | pages [5] -->
m

<!-- b001031 | furniture | pages [5] -->
m

<!-- b001032 | furniture | pages [5] -->
m

<!-- b001033 | furniture | pages [5] -->
m

<!-- b001034 | furniture | pages [5] -->
m

<!-- b001035 | furniture | pages [5] -->
m

<!-- b001036 | furniture | pages [5] -->
m

<!-- b001037 | furniture | pages [5] -->
m

<!-- b001038 | furniture | pages [5] -->
m

<!-- b001039 | furniture | pages [5] -->
m

<!-- b001040 | furniture | pages [5] -->
m

<!-- b001041 | furniture | pages [5] -->
m

<!-- b001042 | furniture | pages [5] -->
m

<!-- b001043 | furniture | pages [5] -->
m

<!-- b001044 | furniture | pages [5] -->
m

<!-- b001045 | furniture | pages [5] -->
m

<!-- b001046 | furniture | pages [5] -->
m

<!-- b001047 | furniture | pages [5] -->
m

<!-- b001048 | furniture | pages [5] -->
m

<!-- b001049 | furniture | pages [5] -->
m

<!-- b001050 | furniture | pages [5] -->
m

<!-- b001051 | furniture | pages [5] -->
m

<!-- b001052 | furniture | pages [5] -->
m

<!-- b001053 | furniture | pages [5] -->
m

<!-- b001054 | furniture | pages [5] -->
m

<!-- b001055 | furniture | pages [5] -->
m

<!-- b001056 | furniture | pages [5] -->
m

<!-- b001057 | furniture | pages [5] -->
m

<!-- b001058 | furniture | pages [5] -->
m

<!-- b001059 | furniture | pages [5] -->
m

<!-- b001060 | furniture | pages [5] -->
m

<!-- b001061 | furniture | pages [5] -->
m

<!-- b001062 | furniture | pages [5] -->
m

<!-- b001063 | furniture | pages [5] -->
m

<!-- b001064 | furniture | pages [5] -->
m

<!-- b001065 | furniture | pages [5] -->
m

<!-- b001066 | furniture | pages [5] -->
m

<!-- b001067 | furniture | pages [5] -->
m

<!-- b001068 | furniture | pages [5] -->
m

<!-- b001069 | furniture | pages [5] -->
m

<!-- b001070 | furniture | pages [5] -->
m

<!-- b001071 | furniture | pages [5] -->
m

<!-- b001072 | furniture | pages [5] -->
m

<!-- b001073 | furniture | pages [5] -->
m

<!-- b001074 | furniture | pages [5] -->
m

<!-- b001075 | furniture | pages [5] -->
m

<!-- b001076 | furniture | pages [5] -->
m

<!-- b001077 | furniture | pages [5] -->
m

<!-- b001078 | furniture | pages [5] -->
m

<!-- b001079 | furniture | pages [5] -->
m

<!-- b001080 | furniture | pages [5] -->
m

<!-- b001081 | furniture | pages [5] -->
m

<!-- b001082 | furniture | pages [5] -->
m

<!-- b001083 | furniture | pages [5] -->
m

<!-- b001084 | furniture | pages [5] -->
m

<!-- b001085 | furniture | pages [5] -->
m

<!-- b001086 | furniture | pages [5] -->
m

<!-- b001087 | furniture | pages [5] -->
m

<!-- b001088 | furniture | pages [5] -->
m

<!-- b001089 | furniture | pages [5] -->
m

<!-- b001090 | furniture | pages [5] -->
m

<!-- b001091 | furniture | pages [5] -->
m

<!-- b001092 | furniture | pages [5] -->
m

<!-- b001093 | furniture | pages [5] -->
m

<!-- b001094 | furniture | pages [5] -->
m

<!-- b001095 | furniture | pages [5] -->
m

<!-- b001096 | furniture | pages [5] -->
m

<!-- b001097 | furniture | pages [5] -->
m

<!-- b001098 | furniture | pages [5] -->
m

<!-- b001099 | furniture | pages [5] -->
m

<!-- b001100 | furniture | pages [5] -->
m

<!-- b001101 | furniture | pages [5] -->
m

<!-- b001102 | furniture | pages [5] -->
m

<!-- b001103 | furniture | pages [5] -->
m

<!-- b001104 | furniture | pages [5] -->
m

<!-- b001105 | furniture | pages [5] -->
m

<!-- b001106 | furniture | pages [5] -->
m

<!-- b001107 | furniture | pages [5] -->
m

<!-- b001108 | furniture | pages [5] -->
m

<!-- b001109 | furniture | pages [5] -->
m

<!-- b001110 | furniture | pages [5] -->
m

<!-- b001111 | furniture | pages [5] -->
m

<!-- b001112 | furniture | pages [5] -->
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

<!-- b001429 | furniture | pages [6] -->
Team # 2500759

<!-- b001430 | furniture | pages [6] -->
Page 6 of 26

<!-- b001431 | prose | pages [6] -->
Principal Component Analysis (PCA) was employed to reduce the dimensionality of the weighted medal count dataset across 45 sporting events. This approach effec- tively addresses multicollinearity among original metrics by utilizing uncorrelated prin- cipal components, thereby eliminating redundancy and improving the convergence speed and accuracy of subsequent algorithms. Subsequently, Figs. 2(a)-(b) illustrate the first two dimensions of the PCA results.

<!-- b001432 | prose | pages [6] -->
(a) (b)

<!-- b001433 | caption | pages [6] -->
Figure 2: PCA Bioplot

<!-- b001434 | prose | pages [6] -->
In the five-dimensional principal components, the cumulative variance contributions reach 76.4%, effectively capturing most characteristics of the original data. This indicates that data can be reduced to five dimensions for analysis. Fig. 2(b) shows that shooting has the highest score on the principal components, indicating its significant influence among events. Following shooting, swimming, athletics, and wrestling also exhibit no- table medal weights. The remaining events cluster distinctly, likely due to their correlated medal weights. Collectively, swimming, athletics, wrestling, shooting, rhythmic gym- nastics, boxing, and diving significantly impact PC1, suggesting it represents a principal component for major sports. Conversely, the other components (PC2 to PC5) are influ- enced by fewer variables. This analysis yields five principal component characteristics regarding medal weights of sporting events at the 2020 Olympics through PCA dimen- sionality reduction.

<!-- b001435 | prose | pages [6] -->
3.1.2 LSTM: Trends Based on Time

<!-- b001436 | prose | pages [6] -->
Predicting the Olympic medal tally can be framed as a time series forecasting prob- lem, as countries’ medal counts show temporal continuity. Strong sports powers often maintain high medal counts, while emerging nations may experience short-term break- throughs. Thus, the model must capture patterns and long-term trends across different Olympic Games.

<!-- b001437 | prose | pages [6] -->
LSTM is advantageous for handling long-range dependencies in time series data. For instance, if a country’s medal count has steadily increased over the last three Games, LSTM can identify this trend to predict further increases. The four-year gap between Olympics makes traditional models less effective; however, LSTM’s gating mechanisms help retain essential historical information, improving prediction accuracy.

<!-- b001438 | prose | pages [6] -->
Additionally, Olympic medal data can be noisy, with some countries showing incon- sistent performances. LSTM mitigates this noise by learning broader trends. It can also incorporate extra features like host country metrics to enhance predictions. To tackle data

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
sparsity, especially for smaller nations with limited data points, we have implemented a regularization technique.

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

<!-- b001631 | prose | pages [6] -->
m

<!-- b001632 | prose | pages [6] -->
m

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
m

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
m

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
m

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
The process of constructing the LSTM model is as follows.

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
m

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
关注数学模型

<!-- b002129 | furniture | pages [6] -->
2

<!-- b002130 | furniture | pages [6] -->
MATHmodels

<!-- b002131 | furniture | pages [6] -->
获取更多资讯

<!-- b002132 | furniture | pages [8] -->
Team # 2500759

<!-- b002133 | furniture | pages [8] -->
Page 8 of 26

<!-- b002134 | prose | pages [8] -->
comparisons. As illustrated in Figs. 3(a) and 3(d) (circle is the minimum of error), the optimal configuration is 32×6. Figs. 3(b) and 3(e) indicate that both 64×8 and 64×10 meet the objective; however, in Fig. 3(b), the model with 64×8 demonstrates a more sig- nificant reduction in error compared to the other parameter settings, leading us to select 64×8. Figs. 3(c) and 3(f) reveal that 128×10 exhibits the best performance.

<!-- b002135 | prose | pages [8] -->
Subsequently, we conducted a direct comparison of these three models. As shown in Fig. 4, the performance of the configurations 32×6 and 128×10 is quite similar; nonethe- less, the overall error for 128×10 is lower. Therefore, we ultimately determined the pa- rameters to be hidden_size=128 and patience=10. This selection provides critical trends measures for subsequent research involving XGBoost.

<!-- b002136 | prose | pages [8] -->
P wc|yc −ˆyc| P wc

<!-- b002137 | prose | pages [8] -->
WMAE_Gold or Total =

<!-- b002138 | prose | pages [8] -->
(6)

<!-- b002139 | prose | pages [8] -->
where wc is the weight of country c’s gold medals or total medals, yc is the true and ˆyc is the prediction.

<!-- b002140 | prose | pages [8] -->
(a)

<!-- b002141 | prose | pages [8] -->
(d)

<!-- b002142 | prose | pages [8] -->
(b) (b) (c)

<!-- b002143 | prose | pages [8] -->
(e) (e) (f)

<!-- b002144 | caption | pages [8] -->
Figure 3: Variations in Parameter Tuning of WMAE_Gold and WMAE_Total

<!-- b002145 | caption | pages [8] -->
Figure 4: Comparison on Hidden_size

<!-- b002146 | prose | pages [8] -->
关注数学模型

<!-- b002147 | furniture | pages [8] -->
2

<!-- b002148 | furniture | pages [8] -->
MATHmodels

<!-- b002149 | furniture | pages [8] -->
获取更多资讯

<!-- b002150 | furniture | pages [9] -->
Team # 2500759

<!-- b002151 | prose | pages [9] -->
3.1.3

<!-- b002152 | heading | pages [9] -->
XGBoost-Bootstrap Modeling

<!-- b002153 | furniture | pages [9] -->
Page 9 of 26

<!-- b002154 | prose | pages [9] -->
Based on the aforementioned PCA dimensionality reduction and LSTM trend mea- surement, we obtain the input data for XGBoost. Subsequently, we construct XGBoost prediction models based on gold medal counts and total medal counts, respectively. A key aspect of this model (Fig. 5) is the construction of a relatively optimal XGBoost model through 10-fold cross-validation grid parameter tuning, along with the estimation of con- fidence intervals for medal prediction values using the Bootstrap resampling strategy.

<!-- b002155 | prose | pages [9] -->
微信公众号：数学模型

<!-- b002156 | prose | pages [9] -->
微信号：MATHmodels

<!-- b002157 | caption | pages [9] -->
Figure 5: Schematic of XGBoost-Bootstrap

<!-- b002158 | prose | pages [9] -->
XGBoost is an ensemble learning algorithm based on gradient-boosted trees, which centers on the incremental and parallel optimization of the loss function by constructing multiple CART base classifiers. It employs a second-order Taylor expansion of the ob- jective function, enhancing the efficiency of gradient descent while incorporating regular- ization into the objective function to effectively prevent model overfitting. This algorithm aims to leverage these features to elucidate the nonlinear relationships among gold medal counts, total medal counts, home advantage, weighted values for individual sport medals, and medal trend values. The objective function is Equation 7.

<!-- b002159 | prose | pages [9] -->
n X

<!-- b002160 | prose | pages [9] -->
K X

<!-- b002161 | prose | pages [9] -->
l(yi, ˆyi) +

<!-- b002162 | prose | pages [9] -->
L(θ) =

<!-- b002163 | prose | pages [9] -->
i=1

<!-- b002164 | prose | pages [9] -->
Ω(fk) (7)

<!-- b002165 | prose | pages [9] -->
k=1

<!-- b002166 | prose | pages [9] -->
where l(·) is the loss function, Ω(·) is the regularization term.

<!-- b002167 | prose | pages [9] -->
Bootstrap is a non-parametric resampling method. By employing this approach, we independently run the constructed XGBoost model 1,000 times, allowing us to calculate the 95% confidence interval for each country’s fitted values of gold and total medals based on these iterations.

<!-- b002168 | prose | pages [9] -->
3.1.4

<!-- b002169 | heading | pages [9] -->
Results Display

<!-- b002170 | prose | pages [9] -->
The hyperparameter tuning of the predictive models employed RMSE as the evalua- tion criterion, aimed at selecting the model with the minimum RMSE value (see section 6.2 for a detailed analysis). During the training of the gold medal prediction model, the

<!-- b002171 | furniture | pages [10] -->
Team # 2500759

<!-- b002172 | furniture | pages [10] -->
Page 10 of 26

<!-- b002173 | prose | pages [10] -->
optimal combination of model parameters was determined through hyperparameter tun- ing, yielding: nrounds = 75, max_depth = 2, eta = 0.1, gamma = 0.5, colsample_bytree = 1, min_child_weight = 1, and subsample = 0.5. Notably, the subsample parameter re- mained constant throughout the tuning process, set at 0.5 to ensure a reasonable sampling proportion.

<!-- b002174 | prose | pages [10] -->
In the training process of the medal prediction model, the only change compared to the gold medal prediction model was the adjustment of the gamma parameter. In this model, the gamma value was set to 0.25 to optimize the model’s predictive ability for the number of medals. Consequently, the relatively optimal XGBoost model was utilized to perform Bootstrap resampling and interval estimation for "the trend values of gold and medal counts for various countries in 2028", "the five principal component dimensions of medal weights for various sports in 2024" and "the estimated home-field effect values for 2028." The results for the top 20 countries in both gold medal counts and total medal counts for the 2028 Los Angeles Olympic Games are illustrated in Figs. 6(a)-(b).

<!-- b002175 | prose | pages [10] -->
(a) (a)

<!-- b002176 | prose | pages [10] -->
(b) (b)

<!-- b002177 | caption | pages [10] -->
Figure 6: Top 20 Predictions for Gold and Medal Counts at 2028 Olympics

<!-- b002178 | prose | pages [10] -->
Based on Figs. 6(a)-(b) and Table 2, it can be observed that as the host country, the United States is projected to see a significant increase in both gold and medal counts for the 2028 Olympic Games. Additionally, countries such as the United Kingdom, Australia, Canada, and Cuba may also experience an increase in their respective gold and medal counts. In contrast, France, the host of the 2024 Olympic Games, is expected to achieve unprecedented results due to home-field advantage, but model predictions suggest that its gold and medal counts will notably decrease in the subsequent Olympic Games. Similarly, countries like China, Italy, South Korea, Japan, and Uzbekistan are also likely to perform poorly in the next Olympic Games.

<!-- b002179 | prose | pages [10] -->
3.2 Breaking the Zero

<!-- b002180 | prose | pages [10] -->
Based on the aforementioned analysis and the criteria for achieving a "breakthrough of zero," we identify the countries projected to achieve at least one gold medal in the 2028

<!-- b002181 | prose | pages [10] -->
关注数学模型

<!-- b002182 | furniture | pages [10] -->
2

<!-- b002183 | furniture | pages [10] -->
MATHmodels

<!-- b002184 | furniture | pages [10] -->
获取更多资讯

<!-- b002185 | furniture | pages [11] -->
Team # 2500759

<!-- b002186 | furniture | pages [11] -->
Page 11 of 26

<!-- b002187 | caption | pages [11] -->
Table 2: Predicted Medal Counts & CI for Top 20 Countries at 2028 Olympics

<!-- b002188 | prose | pages [11] -->
Gold

<!-- b002189 | prose | pages [11] -->
NOC Gold_Pred CI_95% Trend

<!-- b002190 | prose | pages [11] -->
↑ USA 51 (32.08,58.34) ↓ CHN 34 (23.33,40.19) ↑ AUS 19 (10.41,16.13) ↓ JPN 17 (11.88,18.80)

<!-- b002191 | prose | pages [11] -->
Total

<!-- b002192 | prose | pages [11] -->
NOC Total_Pred CI_95% Trend

<!-- b002193 | prose | pages [11] -->
↑ USA 133 (79.60,147.35) ↓ CHN 90 (59.13,103.51) ↑ GBR 69 (43.12,75.84) ↓ JPN 55 (38.19,64.94)

<!-- b002194 | prose | pages [11] -->
微信公众号：数学模型

<!-- b002195 | prose | pages [11] -->
↑ GBR 16 (11.92,19.12) ↓ FRA 12 (9.00,14.86) ↓ GER 12 (8.41,14.38) ↓ ITA 11 (7.06,13.03) ↓ NED 11 (6.84,13.18) ↑ NZL 11 (4.82,9.33) ↑ CAN 10 (5.73,11.70) ↑ HUN 8 (5.18,10.87) ↓ KOR 7 (5.69,9.38) ↓ BRA 6 (3.70,8.06) ↓ ESP 5 (3.08,6.72) ↑ AUS 49 (33.37,63.77) ↓ FRA 41 (29.86,60.60) ↑ NED 34 (24.58,39.30) ↓ GER 33 (25.18,48.98) ↑ CAN 29 (21.72,33.68) ↓ ITA 29 (22.58,34.13) ↓ KOR 25 (18.08,34.28) ↑ BRA 21 (14.67,24.32) ↓ NZL 18 (13.98,23.86) ↓ HUN 17 (13.00,22.69) ↑ CUB 15 (10.91,18.57)

<!-- b002196 | prose | pages [11] -->
微信号：MATHmodels

<!-- b002197 | prose | pages [11] -->
↑ UKR 5 (3.39,7.88) ↓ KEN 5 (2.51,6.01) ↑ CUB 4 (2.36,5.92) ↓ UZB 4 (1.96,5.83) ↑ TPE 4 (2.79,4.53) ↓ ESP 14 (8.84,19.47) ↑ SWE 12 (7.06,14.99) ↓ UZB 11 (8.45,13.61) ↓ KEN 9 (7.63,14.35) ↓ UKR 9 (6.96,11.12)

<!-- b002198 | prose | pages [11] -->
Olympics as MKD, BFA, TKM, KSA, SMR, and KUW. We will conduct a signed rank test on the point estimates derived from Bootstrap resampling for these countries to sta- tistically assess whether they can achieve this gold medal breakthrough. The significance of these observations will be further elucidated by considering the size of the P-values, which indicate the probability of the events occurring.

<!-- b002199 | prose | pages [11] -->
The decision to utilize the signed rank test, rather than employing a one-sample t-test or defining a binary variable for "having won a gold medal" to apply logistic regression or binary classification machine learning algorithms, is based on the following consider- ations.

<!-- b002200 | prose | pages [11] -->
• The signed rank test is a non-parametric method that does not require any assump- tions regarding the distribution of the underlying population. In contrast, the t-test is a parametric method that assumes that the data originate from a normally dis- tributed population or that the sample itself is normally distributed. As such, the non-parametric test is more aligned with real-world scenarios, thus minimizing the likelihood of substantial errors. • Implementing a binary variable for "winning a gold medal" to design a classification algorithm and calculate the estimated probability of countries achieving a "break- through of zero" would replace the quantitative variable of gold medal counts with a qualitative variable. This approach neglects the correlation between feature vari- ables and may lead to biased and unreasonable results. Given the analysis outlined above, we will employ the signed rank test to statistically determine the significance of the gold medal breakthrough and to provide probability

<!-- b002201 | prose | pages [11] -->
m

<!-- b002202 | prose | pages [11] -->
m

<!-- b002203 | prose | pages [11] -->
m

<!-- b002204 | prose | pages [11] -->
m

<!-- b002205 | prose | pages [11] -->
m

<!-- b002206 | prose | pages [11] -->
m

<!-- b002207 | prose | pages [11] -->
m

<!-- b002208 | prose | pages [11] -->
m

<!-- b002209 | prose | pages [11] -->
m

<!-- b002210 | prose | pages [11] -->
m

<!-- b002211 | prose | pages [11] -->
m

<!-- b002212 | prose | pages [11] -->
m

<!-- b002213 | prose | pages [11] -->
m

<!-- b002214 | prose | pages [11] -->
m

<!-- b002215 | prose | pages [11] -->
m

<!-- b002216 | prose | pages [11] -->
m

<!-- b002217 | prose | pages [11] -->
m

<!-- b002218 | prose | pages [11] -->
m

<!-- b002219 | prose | pages [11] -->
m

<!-- b002220 | prose | pages [11] -->
m

<!-- b002221 | prose | pages [11] -->
m

<!-- b002222 | prose | pages [11] -->
m

<!-- b002223 | prose | pages [11] -->
estimates.

<!-- b002224 | prose | pages [11] -->
m

<!-- b002225 | prose | pages [11] -->
m

<!-- b002226 | prose | pages [11] -->
m

<!-- b002227 | prose | pages [11] -->
m

<!-- b002228 | prose | pages [11] -->
m

<!-- b002229 | prose | pages [11] -->
m

<!-- b002230 | prose | pages [11] -->
m

<!-- b002231 | prose | pages [11] -->
m

<!-- b002232 | prose | pages [11] -->
m

<!-- b002233 | prose | pages [11] -->
m

<!-- b002234 | prose | pages [11] -->
m

<!-- b002235 | prose | pages [11] -->
m

<!-- b002236 | prose | pages [11] -->
m

<!-- b002237 | prose | pages [11] -->
m

<!-- b002238 | prose | pages [11] -->
m

<!-- b002239 | prose | pages [11] -->
m

<!-- b002240 | prose | pages [11] -->
m

<!-- b002241 | prose | pages [11] -->
m

<!-- b002242 | prose | pages [11] -->
m

<!-- b002243 | prose | pages [11] -->
m

<!-- b002244 | prose | pages [11] -->
m

<!-- b002245 | prose | pages [11] -->
m

<!-- b002246 | prose | pages [11] -->
m

<!-- b002247 | prose | pages [11] -->
m

<!-- b002248 | prose | pages [11] -->
m

<!-- b002249 | prose | pages [11] -->
m

<!-- b002250 | prose | pages [11] -->
m

<!-- b002251 | prose | pages [11] -->
m

<!-- b002252 | prose | pages [11] -->
m

<!-- b002253 | prose | pages [11] -->
m

<!-- b002254 | prose | pages [11] -->
m

<!-- b002255 | prose | pages [11] -->
m

<!-- b002256 | prose | pages [11] -->
m

<!-- b002257 | prose | pages [11] -->
m

<!-- b002258 | prose | pages [11] -->
m

<!-- b002259 | prose | pages [11] -->
m

<!-- b002260 | prose | pages [11] -->
m

<!-- b002261 | prose | pages [11] -->
m

<!-- b002262 | prose | pages [11] -->
m

<!-- b002263 | prose | pages [11] -->
m

<!-- b002264 | prose | pages [11] -->
m

<!-- b002265 | prose | pages [11] -->
m

<!-- b002266 | prose | pages [11] -->
m

<!-- b002267 | prose | pages [11] -->
m

<!-- b002268 | prose | pages [11] -->
m

<!-- b002269 | prose | pages [11] -->
m

<!-- b002270 | prose | pages [11] -->
m

<!-- b002271 | prose | pages [11] -->
m

<!-- b002272 | prose | pages [11] -->
m

<!-- b002273 | prose | pages [11] -->
m

<!-- b002274 | prose | pages [11] -->
m

<!-- b002275 | prose | pages [11] -->
m

<!-- b002276 | prose | pages [11] -->
m

<!-- b002277 | prose | pages [11] -->
m

<!-- b002278 | prose | pages [11] -->
m

<!-- b002279 | prose | pages [11] -->
m

<!-- b002280 | prose | pages [11] -->
m

<!-- b002281 | prose | pages [11] -->
m

<!-- b002282 | prose | pages [11] -->
m

<!-- b002283 | prose | pages [11] -->
m

<!-- b002284 | prose | pages [11] -->
m

<!-- b002285 | prose | pages [11] -->
m

<!-- b002286 | prose | pages [11] -->
m

<!-- b002287 | prose | pages [11] -->
m

<!-- b002288 | prose | pages [11] -->
m

<!-- b002289 | prose | pages [11] -->
m

<!-- b002290 | prose | pages [11] -->
m

<!-- b002291 | prose | pages [11] -->
m

<!-- b002292 | prose | pages [11] -->
m

<!-- b002293 | prose | pages [11] -->
m

<!-- b002294 | prose | pages [11] -->
m

<!-- b002295 | prose | pages [11] -->
m

<!-- b002296 | prose | pages [11] -->
m

<!-- b002297 | prose | pages [11] -->
m

<!-- b002298 | prose | pages [11] -->
m

<!-- b002299 | prose | pages [11] -->
m

<!-- b002300 | prose | pages [11] -->
m

<!-- b002301 | prose | pages [11] -->
m

<!-- b002302 | prose | pages [11] -->
m

<!-- b002303 | prose | pages [11] -->
m

<!-- b002304 | prose | pages [11] -->
m

<!-- b002305 | prose | pages [11] -->
m

<!-- b002306 | prose | pages [11] -->
m

<!-- b002307 | prose | pages [11] -->
m

<!-- b002308 | prose | pages [11] -->
m

<!-- b002309 | prose | pages [11] -->
m

<!-- b002310 | prose | pages [11] -->
m

<!-- b002311 | prose | pages [11] -->
m

<!-- b002312 | prose | pages [11] -->
m

<!-- b002313 | prose | pages [11] -->
m

<!-- b002314 | prose | pages [11] -->
m

<!-- b002315 | prose | pages [11] -->
m

<!-- b002316 | prose | pages [11] -->
m

<!-- b002317 | prose | pages [11] -->
m

<!-- b002318 | prose | pages [11] -->
m

<!-- b002319 | prose | pages [11] -->
m

<!-- b002320 | prose | pages [11] -->
m

<!-- b002321 | prose | pages [11] -->
m

<!-- b002322 | prose | pages [11] -->
m

<!-- b002323 | prose | pages [11] -->
m

<!-- b002324 | prose | pages [11] -->
m

<!-- b002325 | prose | pages [11] -->
m

<!-- b002326 | prose | pages [11] -->
m

<!-- b002327 | prose | pages [11] -->
m

<!-- b002328 | prose | pages [11] -->
m

<!-- b002329 | prose | pages [11] -->
m

<!-- b002330 | prose | pages [11] -->
m

<!-- b002331 | prose | pages [11] -->
m

<!-- b002332 | prose | pages [11] -->
m

<!-- b002333 | prose | pages [11] -->
m

<!-- b002334 | prose | pages [11] -->
m

<!-- b002335 | prose | pages [11] -->
m

<!-- b002336 | prose | pages [11] -->
m

<!-- b002337 | prose | pages [11] -->
m

<!-- b002338 | prose | pages [11] -->
m

<!-- b002339 | prose | pages [11] -->
m

<!-- b002340 | prose | pages [11] -->
m

<!-- b002341 | prose | pages [11] -->
m

<!-- b002342 | prose | pages [11] -->
m

<!-- b002343 | prose | pages [11] -->
m

<!-- b002344 | prose | pages [11] -->
m

<!-- b002345 | prose | pages [11] -->
m

<!-- b002346 | prose | pages [11] -->
m

<!-- b002347 | prose | pages [11] -->
m

<!-- b002348 | prose | pages [11] -->
m

<!-- b002349 | prose | pages [11] -->
m

<!-- b002350 | prose | pages [11] -->
m

<!-- b002351 | prose | pages [11] -->
m

<!-- b002352 | prose | pages [11] -->
m

<!-- b002353 | prose | pages [11] -->
m

<!-- b002354 | prose | pages [11] -->
m

<!-- b002355 | prose | pages [11] -->
m

<!-- b002356 | prose | pages [11] -->
m

<!-- b002357 | prose | pages [11] -->
m

<!-- b002358 | prose | pages [11] -->
m

<!-- b002359 | prose | pages [11] -->
m

<!-- b002360 | prose | pages [11] -->
m

<!-- b002361 | prose | pages [11] -->
m

<!-- b002362 | prose | pages [11] -->
m

<!-- b002363 | prose | pages [11] -->
m

<!-- b002364 | prose | pages [11] -->
m

<!-- b002365 | prose | pages [11] -->
m

<!-- b002366 | prose | pages [11] -->
m

<!-- b002367 | prose | pages [11] -->
m

<!-- b002368 | prose | pages [11] -->
m

<!-- b002369 | prose | pages [11] -->
m

<!-- b002370 | prose | pages [11] -->
m

<!-- b002371 | prose | pages [11] -->
m

<!-- b002372 | prose | pages [11] -->
m

<!-- b002373 | prose | pages [11] -->
m

<!-- b002374 | prose | pages [11] -->
m

<!-- b002375 | prose | pages [11] -->
m

<!-- b002376 | prose | pages [11] -->
m

<!-- b002377 | prose | pages [11] -->
m

<!-- b002378 | prose | pages [11] -->
m

<!-- b002379 | prose | pages [11] -->
m

<!-- b002380 | prose | pages [11] -->
m

<!-- b002381 | prose | pages [11] -->
m

<!-- b002382 | prose | pages [11] -->
m

<!-- b002383 | prose | pages [11] -->
m

<!-- b002384 | prose | pages [11] -->
m

<!-- b002385 | prose | pages [11] -->
m

<!-- b002386 | prose | pages [11] -->
m

<!-- b002387 | prose | pages [11] -->
m

<!-- b002388 | prose | pages [11] -->
m

<!-- b002389 | prose | pages [11] -->
m

<!-- b002390 | prose | pages [11] -->
m

<!-- b002391 | prose | pages [11] -->
m

<!-- b002392 | prose | pages [11] -->
m

<!-- b002393 | prose | pages [11] -->
m

<!-- b002394 | prose | pages [11] -->
m

<!-- b002395 | prose | pages [11] -->
m

<!-- b002396 | prose | pages [11] -->
m

<!-- b002397 | prose | pages [11] -->
m

<!-- b002398 | prose | pages [11] -->
m

<!-- b002399 | prose | pages [11] -->
m

<!-- b002400 | prose | pages [11] -->
m

<!-- b002401 | prose | pages [11] -->
m

<!-- b002402 | prose | pages [11] -->
m

<!-- b002403 | prose | pages [11] -->
m

<!-- b002404 | prose | pages [11] -->
m

<!-- b002405 | prose | pages [11] -->
m

<!-- b002406 | prose | pages [11] -->
m

<!-- b002407 | prose | pages [11] -->
m

<!-- b002408 | prose | pages [11] -->
m

<!-- b002409 | prose | pages [11] -->
m

<!-- b002410 | prose | pages [11] -->
m

<!-- b002411 | prose | pages [11] -->
m

<!-- b002412 | prose | pages [11] -->
m

<!-- b002413 | prose | pages [11] -->
m

<!-- b002414 | prose | pages [11] -->
m

<!-- b002415 | prose | pages [11] -->
m

<!-- b002416 | prose | pages [11] -->
m

<!-- b002417 | prose | pages [11] -->
m

<!-- b002418 | prose | pages [11] -->
m

<!-- b002419 | prose | pages [11] -->
m

<!-- b002420 | prose | pages [11] -->
m

<!-- b002421 | prose | pages [11] -->
m

<!-- b002422 | prose | pages [11] -->
m

<!-- b002423 | prose | pages [11] -->
m

<!-- b002424 | prose | pages [11] -->
m

<!-- b002425 | prose | pages [11] -->
m

<!-- b002426 | prose | pages [11] -->
m

<!-- b002427 | prose | pages [11] -->
m

<!-- b002428 | prose | pages [11] -->
m

<!-- b002429 | prose | pages [11] -->
m

<!-- b002430 | prose | pages [11] -->
m

<!-- b002431 | prose | pages [11] -->
m

<!-- b002432 | prose | pages [11] -->
m

<!-- b002433 | prose | pages [11] -->
m

<!-- b002434 | prose | pages [11] -->
m

<!-- b002435 | prose | pages [11] -->
m

<!-- b002436 | prose | pages [11] -->
m

<!-- b002437 | prose | pages [11] -->
m

<!-- b002438 | prose | pages [11] -->
m

<!-- b002439 | prose | pages [11] -->
m

<!-- b002440 | prose | pages [11] -->
m

<!-- b002441 | prose | pages [11] -->
m

<!-- b002442 | prose | pages [11] -->
m

<!-- b002443 | prose | pages [11] -->
m

<!-- b002444 | prose | pages [11] -->
m

<!-- b002445 | prose | pages [11] -->
m

<!-- b002446 | prose | pages [11] -->
m

<!-- b002447 | prose | pages [11] -->
m

<!-- b002448 | prose | pages [11] -->
m

<!-- b002449 | prose | pages [11] -->
m

<!-- b002450 | prose | pages [11] -->
m

<!-- b002451 | prose | pages [11] -->
m

<!-- b002452 | prose | pages [11] -->
m

<!-- b002453 | prose | pages [11] -->
m

<!-- b002454 | prose | pages [11] -->
m

<!-- b002455 | prose | pages [11] -->
m

<!-- b002456 | prose | pages [11] -->
m

<!-- b002457 | prose | pages [11] -->
m

<!-- b002458 | prose | pages [11] -->
m

<!-- b002459 | prose | pages [11] -->
m

<!-- b002460 | prose | pages [11] -->
m

<!-- b002461 | prose | pages [11] -->
m

<!-- b002462 | prose | pages [11] -->
m

<!-- b002463 | prose | pages [11] -->
m

<!-- b002464 | prose | pages [11] -->
m

<!-- b002465 | prose | pages [11] -->
m

<!-- b002466 | prose | pages [11] -->
m

<!-- b002467 | prose | pages [11] -->
m

<!-- b002468 | prose | pages [11] -->
m

<!-- b002469 | prose | pages [11] -->
m

<!-- b002470 | prose | pages [11] -->
m

<!-- b002471 | prose | pages [11] -->
m

<!-- b002472 | prose | pages [11] -->
m

<!-- b002473 | prose | pages [11] -->
m

<!-- b002474 | prose | pages [11] -->
m

<!-- b002475 | prose | pages [11] -->
m

<!-- b002476 | prose | pages [11] -->
m

<!-- b002477 | prose | pages [11] -->
m

<!-- b002478 | prose | pages [11] -->
m

<!-- b002479 | prose | pages [11] -->
m

<!-- b002480 | prose | pages [11] -->
m

<!-- b002481 | prose | pages [11] -->
m

<!-- b002482 | prose | pages [11] -->
m

<!-- b002483 | prose | pages [11] -->
m

<!-- b002484 | prose | pages [11] -->
m

<!-- b002485 | prose | pages [11] -->
m

<!-- b002486 | furniture | pages [11] -->
m

<!-- b002487 | furniture | pages [11] -->
m

<!-- b002488 | furniture | pages [11] -->
m

<!-- b002489 | furniture | pages [11] -->
m

<!-- b002490 | furniture | pages [11] -->
m

<!-- b002491 | furniture | pages [11] -->
m

<!-- b002492 | furniture | pages [11] -->
m

<!-- b002493 | furniture | pages [11] -->
m

<!-- b002494 | furniture | pages [11] -->
m

<!-- b002495 | furniture | pages [11] -->
m

<!-- b002496 | furniture | pages [11] -->
m

<!-- b002497 | furniture | pages [11] -->
m

<!-- b002498 | furniture | pages [11] -->
m

<!-- b002499 | furniture | pages [11] -->
m

<!-- b002500 | furniture | pages [11] -->
m

<!-- b002501 | furniture | pages [11] -->
m

<!-- b002502 | furniture | pages [11] -->
m

<!-- b002503 | furniture | pages [11] -->
m

<!-- b002504 | furniture | pages [11] -->
m

<!-- b002505 | furniture | pages [11] -->
m

<!-- b002506 | furniture | pages [11] -->
m

<!-- b002507 | furniture | pages [11] -->
m

<!-- b002508 | furniture | pages [11] -->
m

<!-- b002509 | furniture | pages [11] -->
m

<!-- b002510 | furniture | pages [11] -->
m

<!-- b002511 | furniture | pages [11] -->
m

<!-- b002512 | furniture | pages [11] -->
m

<!-- b002513 | furniture | pages [11] -->
m

<!-- b002514 | furniture | pages [11] -->
m

<!-- b002515 | furniture | pages [11] -->
m

<!-- b002516 | furniture | pages [11] -->
m

<!-- b002517 | furniture | pages [11] -->
m

<!-- b002518 | furniture | pages [11] -->
m

<!-- b002519 | furniture | pages [11] -->
m

<!-- b002520 | furniture | pages [11] -->
m

<!-- b002521 | furniture | pages [11] -->
m

<!-- b002522 | furniture | pages [11] -->
m

<!-- b002523 | furniture | pages [11] -->
m

<!-- b002524 | furniture | pages [11] -->
m

<!-- b002525 | furniture | pages [11] -->
m

<!-- b002526 | furniture | pages [11] -->
m

<!-- b002527 | furniture | pages [11] -->
m

<!-- b002528 | furniture | pages [11] -->
m

<!-- b002529 | furniture | pages [11] -->
m

<!-- b002530 | furniture | pages [11] -->
m

<!-- b002531 | furniture | pages [11] -->
m

<!-- b002532 | furniture | pages [11] -->
m

<!-- b002533 | furniture | pages [11] -->
m

<!-- b002534 | furniture | pages [11] -->
m

<!-- b002535 | furniture | pages [11] -->
m

<!-- b002536 | furniture | pages [11] -->
m

<!-- b002537 | furniture | pages [11] -->
m

<!-- b002538 | furniture | pages [11] -->
m

<!-- b002539 | furniture | pages [11] -->
m

<!-- b002540 | furniture | pages [11] -->
m

<!-- b002541 | furniture | pages [11] -->
m

<!-- b002542 | furniture | pages [11] -->
m

<!-- b002543 | furniture | pages [11] -->
m

<!-- b002544 | furniture | pages [11] -->
m

<!-- b002545 | furniture | pages [11] -->
m

<!-- b002546 | furniture | pages [11] -->
m

<!-- b002547 | furniture | pages [11] -->
m

<!-- b002548 | furniture | pages [11] -->
m

<!-- b002549 | furniture | pages [11] -->
m

<!-- b002550 | furniture | pages [11] -->
m

<!-- b002551 | furniture | pages [11] -->
m

<!-- b002552 | furniture | pages [11] -->
m

<!-- b002553 | furniture | pages [11] -->
m

<!-- b002554 | furniture | pages [11] -->
m

<!-- b002555 | furniture | pages [11] -->
m

<!-- b002556 | furniture | pages [11] -->
m

<!-- b002557 | furniture | pages [11] -->
m

<!-- b002558 | furniture | pages [11] -->
m

<!-- b002559 | furniture | pages [11] -->
m

<!-- b002560 | furniture | pages [11] -->
m

<!-- b002561 | furniture | pages [11] -->
m

<!-- b002562 | furniture | pages [11] -->
m

<!-- b002563 | furniture | pages [11] -->
m

<!-- b002564 | furniture | pages [11] -->
m

<!-- b002565 | furniture | pages [11] -->
m

<!-- b002566 | furniture | pages [11] -->
m

<!-- b002567 | furniture | pages [11] -->
m

<!-- b002568 | furniture | pages [11] -->
m

<!-- b002569 | furniture | pages [11] -->
m

<!-- b002570 | furniture | pages [11] -->
m

<!-- b002571 | furniture | pages [11] -->
m

<!-- b002572 | furniture | pages [11] -->
m

<!-- b002573 | furniture | pages [11] -->
m

<!-- b002574 | furniture | pages [11] -->
m

<!-- b002575 | furniture | pages [11] -->
m

<!-- b002576 | furniture | pages [11] -->
m

<!-- b002577 | furniture | pages [11] -->
m

<!-- b002578 | furniture | pages [11] -->
m

<!-- b002579 | furniture | pages [11] -->
m

<!-- b002580 | furniture | pages [11] -->
m

<!-- b002581 | furniture | pages [11] -->
m

<!-- b002582 | furniture | pages [11] -->
m

<!-- b002583 | furniture | pages [11] -->
m

<!-- b002584 | furniture | pages [11] -->
m

<!-- b002585 | furniture | pages [11] -->
m

<!-- b002586 | furniture | pages [11] -->
m

<!-- b002587 | furniture | pages [11] -->
m

<!-- b002588 | furniture | pages [11] -->
m

<!-- b002589 | furniture | pages [11] -->
m

<!-- b002590 | furniture | pages [11] -->
m

<!-- b002591 | furniture | pages [11] -->
m

<!-- b002592 | furniture | pages [11] -->
m

<!-- b002593 | furniture | pages [11] -->
m

<!-- b002594 | furniture | pages [11] -->
m

<!-- b002595 | furniture | pages [11] -->
m

<!-- b002596 | furniture | pages [11] -->
m

<!-- b002597 | furniture | pages [11] -->
m

<!-- b002598 | furniture | pages [11] -->
m

<!-- b002599 | furniture | pages [11] -->
m

<!-- b002600 | furniture | pages [11] -->
m

<!-- b002601 | furniture | pages [11] -->
m

<!-- b002602 | furniture | pages [11] -->
m

<!-- b002603 | furniture | pages [11] -->
m

<!-- b002604 | furniture | pages [11] -->
m

<!-- b002605 | furniture | pages [11] -->
m

<!-- b002606 | furniture | pages [11] -->
m

<!-- b002607 | furniture | pages [11] -->
m

<!-- b002608 | furniture | pages [11] -->
m

<!-- b002609 | furniture | pages [11] -->
m

<!-- b002610 | furniture | pages [11] -->
m

<!-- b002611 | furniture | pages [11] -->
m

<!-- b002612 | furniture | pages [11] -->
m

<!-- b002613 | furniture | pages [11] -->
m

<!-- b002614 | furniture | pages [11] -->
m

<!-- b002615 | furniture | pages [11] -->
m

<!-- b002616 | furniture | pages [11] -->
m

<!-- b002617 | furniture | pages [11] -->
m

<!-- b002618 | furniture | pages [11] -->
m

<!-- b002619 | furniture | pages [11] -->
m

<!-- b002620 | furniture | pages [11] -->
m

<!-- b002621 | furniture | pages [11] -->
m

<!-- b002622 | furniture | pages [11] -->
m

<!-- b002623 | furniture | pages [11] -->
m

<!-- b002624 | furniture | pages [11] -->
m

<!-- b002625 | furniture | pages [11] -->
m

<!-- b002626 | furniture | pages [11] -->
m

<!-- b002627 | furniture | pages [11] -->
m

<!-- b002628 | furniture | pages [11] -->
m

<!-- b002629 | furniture | pages [11] -->
m

<!-- b002630 | furniture | pages [11] -->
m

<!-- b002631 | furniture | pages [11] -->
m

<!-- b002632 | furniture | pages [11] -->
m

<!-- b002633 | furniture | pages [11] -->
m

<!-- b002634 | furniture | pages [11] -->
m

<!-- b002635 | furniture | pages [11] -->
m

<!-- b002636 | furniture | pages [11] -->
m

<!-- b002637 | furniture | pages [11] -->
m

<!-- b002638 | furniture | pages [11] -->
m

<!-- b002639 | furniture | pages [11] -->
m

<!-- b002640 | furniture | pages [11] -->
m

<!-- b002641 | furniture | pages [11] -->
m

<!-- b002642 | furniture | pages [11] -->
m

<!-- b002643 | furniture | pages [11] -->
m

<!-- b002644 | furniture | pages [11] -->
m

<!-- b002645 | furniture | pages [11] -->
m

<!-- b002646 | furniture | pages [11] -->
m

<!-- b002647 | furniture | pages [11] -->
m

<!-- b002648 | furniture | pages [11] -->
m

<!-- b002649 | furniture | pages [11] -->
m

<!-- b002650 | furniture | pages [11] -->
m

<!-- b002651 | furniture | pages [11] -->
m

<!-- b002652 | furniture | pages [11] -->
m

<!-- b002653 | furniture | pages [11] -->
m

<!-- b002654 | furniture | pages [11] -->
m

<!-- b002655 | furniture | pages [11] -->
m

<!-- b002656 | furniture | pages [11] -->
m

<!-- b002657 | furniture | pages [11] -->
m

<!-- b002658 | furniture | pages [11] -->
m

<!-- b002659 | furniture | pages [11] -->
m

<!-- b002660 | furniture | pages [11] -->
m

<!-- b002661 | furniture | pages [11] -->
m

<!-- b002662 | furniture | pages [11] -->
m

<!-- b002663 | furniture | pages [11] -->
m

<!-- b002664 | furniture | pages [11] -->
m

<!-- b002665 | furniture | pages [11] -->
m

<!-- b002666 | furniture | pages [11] -->
m

<!-- b002667 | furniture | pages [11] -->
m

<!-- b002668 | furniture | pages [11] -->
m

<!-- b002669 | furniture | pages [11] -->
m

<!-- b002670 | furniture | pages [11] -->
m

<!-- b002671 | furniture | pages [11] -->
m

<!-- b002672 | furniture | pages [11] -->
m

<!-- b002673 | furniture | pages [11] -->
m

<!-- b002674 | furniture | pages [11] -->
m

<!-- b002675 | furniture | pages [11] -->
m

<!-- b002676 | furniture | pages [11] -->
m

<!-- b002677 | furniture | pages [11] -->
m

<!-- b002678 | furniture | pages [11] -->
m

<!-- b002679 | furniture | pages [11] -->
m

<!-- b002680 | furniture | pages [11] -->
m

<!-- b002681 | furniture | pages [11] -->
m

<!-- b002682 | furniture | pages [11] -->
m

<!-- b002683 | furniture | pages [11] -->
m

<!-- b002684 | furniture | pages [11] -->
m

<!-- b002685 | furniture | pages [11] -->
m

<!-- b002686 | furniture | pages [11] -->
m

<!-- b002687 | furniture | pages [11] -->
m

<!-- b002688 | furniture | pages [11] -->
m

<!-- b002689 | furniture | pages [11] -->
m

<!-- b002690 | furniture | pages [11] -->
m

<!-- b002691 | furniture | pages [11] -->
m

<!-- b002692 | furniture | pages [11] -->
m

<!-- b002693 | furniture | pages [11] -->
m

<!-- b002694 | furniture | pages [11] -->
m

<!-- b002695 | furniture | pages [11] -->
m

<!-- b002696 | furniture | pages [11] -->
m

<!-- b002697 | furniture | pages [11] -->
m

<!-- b002698 | furniture | pages [11] -->
m

<!-- b002699 | furniture | pages [11] -->
m

<!-- b002700 | furniture | pages [11] -->
m

<!-- b002701 | furniture | pages [11] -->
m

<!-- b002702 | furniture | pages [11] -->
m

<!-- b002703 | furniture | pages [11] -->
m

<!-- b002704 | furniture | pages [11] -->
m

<!-- b002705 | furniture | pages [11] -->
m

<!-- b002706 | furniture | pages [11] -->
m

<!-- b002707 | furniture | pages [11] -->
m

<!-- b002708 | furniture | pages [11] -->
m

<!-- b002709 | furniture | pages [11] -->
m

<!-- b002710 | furniture | pages [11] -->
m

<!-- b002711 | furniture | pages [11] -->
m

<!-- b002712 | furniture | pages [11] -->
m

<!-- b002713 | furniture | pages [11] -->
m

<!-- b002714 | furniture | pages [11] -->
m

<!-- b002715 | furniture | pages [11] -->
m

<!-- b002716 | furniture | pages [11] -->
m

<!-- b002717 | furniture | pages [11] -->
m

<!-- b002718 | furniture | pages [11] -->
m

<!-- b002719 | furniture | pages [11] -->
m

<!-- b002720 | furniture | pages [11] -->
m

<!-- b002721 | furniture | pages [11] -->
m

<!-- b002722 | furniture | pages [11] -->
m

<!-- b002723 | furniture | pages [11] -->
m

<!-- b002724 | furniture | pages [11] -->
m

<!-- b002725 | furniture | pages [11] -->
m

<!-- b002726 | furniture | pages [11] -->
m

<!-- b002727 | furniture | pages [11] -->
m

<!-- b002728 | furniture | pages [11] -->
m

<!-- b002729 | furniture | pages [11] -->
m

<!-- b002730 | furniture | pages [11] -->
m

<!-- b002731 | furniture | pages [11] -->
m

<!-- b002732 | furniture | pages [11] -->
m

<!-- b002733 | furniture | pages [11] -->
m

<!-- b002734 | furniture | pages [11] -->
m

<!-- b002735 | furniture | pages [11] -->
m

<!-- b002736 | furniture | pages [11] -->
m

<!-- b002737 | furniture | pages [11] -->
m

<!-- b002738 | furniture | pages [11] -->
m

<!-- b002739 | furniture | pages [11] -->
m

<!-- b002740 | furniture | pages [11] -->
m

<!-- b002741 | furniture | pages [11] -->
m

<!-- b002742 | furniture | pages [11] -->
m

<!-- b002743 | furniture | pages [11] -->
m

<!-- b002744 | furniture | pages [11] -->
m

<!-- b002745 | furniture | pages [11] -->
m

<!-- b002746 | furniture | pages [11] -->
m

<!-- b002747 | furniture | pages [11] -->
m

<!-- b002748 | furniture | pages [11] -->
m

<!-- b002749 | furniture | pages [11] -->
m

<!-- b002750 | furniture | pages [11] -->
m

<!-- b002751 | furniture | pages [11] -->
m

<!-- b002752 | furniture | pages [11] -->
m

<!-- b002753 | furniture | pages [11] -->
m

<!-- b002754 | furniture | pages [11] -->
m

<!-- b002755 | furniture | pages [11] -->
m

<!-- b002756 | furniture | pages [11] -->
m

<!-- b002757 | furniture | pages [11] -->
m

<!-- b002758 | furniture | pages [11] -->
m

<!-- b002759 | furniture | pages [11] -->
m

<!-- b002760 | furniture | pages [11] -->
m

<!-- b002761 | furniture | pages [11] -->
m

<!-- b002762 | furniture | pages [11] -->
m

<!-- b002763 | furniture | pages [11] -->
m

<!-- b002764 | furniture | pages [11] -->
m

<!-- b002765 | furniture | pages [11] -->
m

<!-- b002766 | furniture | pages [11] -->
m

<!-- b002767 | furniture | pages [11] -->
m

<!-- b002768 | furniture | pages [11] -->
m

<!-- b002769 | furniture | pages [11] -->
m

<!-- b002770 | furniture | pages [11] -->
m

<!-- b002771 | furniture | pages [11] -->
m

<!-- b002772 | furniture | pages [11] -->
m

<!-- b002773 | furniture | pages [11] -->
m

<!-- b002774 | furniture | pages [11] -->
m

<!-- b002775 | furniture | pages [11] -->
m

<!-- b002776 | furniture | pages [11] -->
m

<!-- b002777 | furniture | pages [11] -->
m

<!-- b002778 | furniture | pages [11] -->
m

<!-- b002779 | furniture | pages [11] -->
m

<!-- b002780 | furniture | pages [11] -->
m

<!-- b002781 | furniture | pages [11] -->
m

<!-- b002782 | furniture | pages [11] -->
m

<!-- b002783 | furniture | pages [11] -->
m

<!-- b002784 | furniture | pages [11] -->
m

<!-- b002785 | furniture | pages [11] -->
m

<!-- b002786 | furniture | pages [11] -->
m

<!-- b002787 | furniture | pages [11] -->
m

<!-- b002788 | furniture | pages [11] -->
m

<!-- b002789 | furniture | pages [11] -->
m

<!-- b002790 | furniture | pages [11] -->
m

<!-- b002791 | furniture | pages [11] -->
m

<!-- b002792 | furniture | pages [11] -->
m

<!-- b002793 | furniture | pages [11] -->
m

<!-- b002794 | furniture | pages [11] -->
m

<!-- b002795 | furniture | pages [11] -->
m

<!-- b002796 | furniture | pages [11] -->
m

<!-- b002797 | furniture | pages [11] -->
m

<!-- b002798 | furniture | pages [11] -->
m

<!-- b002799 | furniture | pages [11] -->
m

<!-- b002800 | furniture | pages [11] -->
m

<!-- b002801 | furniture | pages [11] -->
m

<!-- b002802 | furniture | pages [11] -->
m

<!-- b002803 | furniture | pages [11] -->
m

<!-- b002804 | furniture | pages [11] -->
m

<!-- b002805 | furniture | pages [11] -->
m

<!-- b002806 | furniture | pages [11] -->
m

<!-- b002807 | furniture | pages [11] -->
m

<!-- b002808 | furniture | pages [11] -->
m

<!-- b002809 | furniture | pages [11] -->
m

<!-- b002810 | furniture | pages [11] -->
m

<!-- b002811 | furniture | pages [11] -->
m

<!-- b002812 | furniture | pages [11] -->
m

<!-- b002813 | furniture | pages [11] -->
m

<!-- b002814 | furniture | pages [11] -->
m

<!-- b002815 | furniture | pages [11] -->
m

<!-- b002816 | furniture | pages [11] -->
m

<!-- b002817 | furniture | pages [11] -->
m

<!-- b002818 | furniture | pages [11] -->
m

<!-- b002819 | furniture | pages [11] -->
m

<!-- b002820 | furniture | pages [11] -->
m

<!-- b002821 | furniture | pages [11] -->
m

<!-- b002822 | furniture | pages [11] -->
m

<!-- b002823 | furniture | pages [11] -->
m

<!-- b002824 | furniture | pages [11] -->
m

<!-- b002825 | furniture | pages [11] -->
m

<!-- b002826 | furniture | pages [11] -->
m

<!-- b002827 | furniture | pages [11] -->
m

<!-- b002828 | furniture | pages [11] -->
m

<!-- b002829 | furniture | pages [11] -->
m

<!-- b002830 | furniture | pages [11] -->
m

<!-- b002831 | furniture | pages [11] -->
m

<!-- b002832 | furniture | pages [11] -->
m

<!-- b002833 | furniture | pages [11] -->
m

<!-- b002834 | furniture | pages [11] -->
m

<!-- b002835 | furniture | pages [11] -->
m

<!-- b002836 | furniture | pages [11] -->
m

<!-- b002837 | furniture | pages [11] -->
m

<!-- b002838 | furniture | pages [11] -->
m

<!-- b002839 | furniture | pages [11] -->
m

<!-- b002840 | furniture | pages [11] -->
m

<!-- b002841 | furniture | pages [11] -->
m

<!-- b002842 | furniture | pages [11] -->
m

<!-- b002843 | furniture | pages [11] -->
m

<!-- b002844 | furniture | pages [11] -->
m

<!-- b002845 | furniture | pages [11] -->
m

<!-- b002846 | furniture | pages [11] -->
m

<!-- b002847 | furniture | pages [11] -->
m

<!-- b002848 | furniture | pages [11] -->
m

<!-- b002849 | furniture | pages [11] -->
m

<!-- b002850 | furniture | pages [11] -->
m

<!-- b002851 | furniture | pages [11] -->
m

<!-- b002852 | furniture | pages [11] -->
m

<!-- b002853 | furniture | pages [11] -->
m

<!-- b002854 | furniture | pages [11] -->
m

<!-- b002855 | furniture | pages [11] -->
m

<!-- b002856 | furniture | pages [11] -->
m

<!-- b002857 | furniture | pages [11] -->
m

<!-- b002858 | furniture | pages [11] -->
m

<!-- b002859 | furniture | pages [11] -->
m

<!-- b002860 | furniture | pages [11] -->
m

<!-- b002861 | furniture | pages [11] -->
m

<!-- b002862 | furniture | pages [11] -->
m

<!-- b002863 | furniture | pages [11] -->
m

<!-- b002864 | furniture | pages [11] -->
m

<!-- b002865 | furniture | pages [11] -->
m

<!-- b002866 | furniture | pages [11] -->
m

<!-- b002867 | furniture | pages [11] -->
m

<!-- b002868 | furniture | pages [11] -->
m

<!-- b002869 | furniture | pages [11] -->
m

<!-- b002870 | furniture | pages [11] -->
m

<!-- b002871 | furniture | pages [11] -->
m

<!-- b002872 | furniture | pages [11] -->
m

<!-- b002873 | furniture | pages [11] -->
m

<!-- b002874 | furniture | pages [11] -->
m

<!-- b002875 | furniture | pages [11] -->
m

<!-- b002876 | furniture | pages [11] -->
m

<!-- b002877 | furniture | pages [11] -->
m

<!-- b002878 | furniture | pages [11] -->
m

<!-- b002879 | furniture | pages [11] -->
m

<!-- b002880 | furniture | pages [11] -->
m

<!-- b002881 | furniture | pages [11] -->
m

<!-- b002882 | furniture | pages [11] -->
m

<!-- b002883 | furniture | pages [11] -->
m

<!-- b002884 | furniture | pages [11] -->
m

<!-- b002885 | furniture | pages [11] -->
m

<!-- b002886 | furniture | pages [11] -->
m

<!-- b002887 | furniture | pages [11] -->
m

<!-- b002888 | furniture | pages [11] -->
m

<!-- b002889 | furniture | pages [12] -->
Team # 2500759

<!-- b002890 | prose | pages [12] -->
1) Hypothesis testing setup

<!-- b002891 | furniture | pages [12] -->
Page 12 of 26

<!-- b002892 | prose | pages [12] -->
Let dij represent the i-th Bootstrap prediction value for the j-th country, and θj denote the symmetric center of the corresponding population. When the final prediction value

<!-- b002893 | prose | pages [12] -->
ˆyj ≥1, we establish a left-sided signed rank test with a location parameter of 1:

<!-- b002894 | prose | pages [12] -->
H0 : θj = 1 H1 : θj < 1 vs.

<!-- b002895 | prose | pages [12] -->
2) Data transformation and statistic construction We perform a shift transformation on the original data d∗

<!-- b002896 | prose | pages [12] -->
the absolute value ranks R+ ij = dij −1. Next, we compute

<!-- b002897 | prose | pages [12] -->
ij<0}(d∗

<!-- b002898 | prose | pages [12] -->
ij and the indicator variable: uij = I{d∗

<!-- b002899 | prose | pages [12] -->
excluding data points where d∗ ij). After

<!-- b002900 | prose | pages [12] -->
ij = 0, we construct the signed rank sum statistic:

<!-- b002901 | prose | pages [12] -->
w+

<!-- b002902 | prose | pages [12] -->
j =

<!-- b002903 | prose | pages [12] -->
nj X

<!-- b002904 | prose | pages [12] -->
uijR+

<!-- b002905 | prose | pages [12] -->
ij

<!-- b002906 | prose | pages [12] -->
i=1

<!-- b002907 | prose | pages [12] -->
where nj is the adjusted effective sample size.

<!-- b002908 | prose | pages [12] -->
3) Asymptotic distribution theory Under large sample conditions, when the null hypothesis is true, wj follows a normal distribution:

<!-- b002909 | prose | pages [12] -->
L

<!-- b002910 | prose | pages [12] -->
w+

<!-- b002911 | prose | pages [12] -->
H0 N(µj, σ2

<!-- b002912 | prose | pages [12] -->
−→

<!-- b002913 | prose | pages [12] -->
j

<!-- b002914 | prose | pages [12] -->
j)

<!-- b002915 | prose | pages [12] -->
µj = nj(nj + 1)

<!-- b002916 | prose | pages [12] -->
4

<!-- b002917 | prose | pages [12] -->
Pk

<!-- b002918 | prose | pages [12] -->
i=1(t3

<!-- b002919 | prose | pages [12] -->
i −ti)

<!-- b002920 | prose | pages [12] -->
j = nj(nj + 1)(2nj + 1)

<!-- b002921 | prose | pages [12] -->
σ2

<!-- b002922 | prose | pages [12] -->
24

<!-- b002923 | prose | pages [12] -->
4) P-value calculation

<!-- b002924 | prose | pages [12] -->
P-value = Φ

<!-- b002925 | prose | pages [12] -->
−

<!-- b002926 | prose | pages [12] -->
48

<!-- b002927 | prose | pages [12] -->
!

<!-- b002928 | furniture | pages [12] -->


<!-- b002929 | prose | pages [12] -->
w+

<!-- b002930 | prose | pages [12] -->
j −µj

<!-- b002931 | prose | pages [12] -->
σj

<!-- b002932 | prose | pages [12] -->
If the P-value is less than or equal to 0.05, falling within the rejection region, it is concluded that the country is statistically unable to achieve a "breakthrough of zero" in gold medals at the 2028 Olympics. Conversely, if the P-value is greater than 0.05, it suggests that the country has a favorable chance of achieving a "breakthrough of zero" in gold medals. Furthermore, a larger P-value indicates a smaller probability of committing a Type II error, thereby increasing the likelihood of realizing the "breakthrough of zero" in gold medals. Based on the model established above, the results of the Wlicoxon signed rank test for the countries aiming to achieve this "breakthrough of zero" in gold medals are illustrated in Fig. 7 and Table 3 .

<!-- b002933 | prose | pages [12] -->
Based on the Table 2 and the gold medal counts from participating countries in 2024, it was determined that eight countries, which did not secure any gold medals in 2024, may potentially achieve a breakthrough in gold medals by 2028. Historical data shows that GHA and GRD achieved a breakthrough of zero gold medals in 1960 and 2012, respectively.

<!-- b002934 | prose | pages [12] -->
From Table 3, we can know only two countries, SMR and KWT, had test statistics corresponding to P-values greater than 0.05, indicating that they did not fall within the

<!-- b002935 | prose | pages [12] -->
关注数学模型

<!-- b002936 | furniture | pages [12] -->
2

<!-- b002937 | furniture | pages [12] -->
MATHmodels

<!-- b002938 | furniture | pages [12] -->
获取更多资讯

<!-- b002939 | furniture | pages [13] -->
Team # 2500759

<!-- b002940 | furniture | pages [13] -->
Page 13 of 26

<!-- b002941 | caption | pages [13] -->
Figure 7: Violin-Raincloud Hybrid Plot

<!-- b002942 | prose | pages [13] -->
微信公众号：数学模型

<!-- b002943 | caption | pages [13] -->
Table 3: Sign Rank Sum Test Table

<!-- b002944 | prose | pages [13] -->
w+ NOC

<!-- b002945 | prose | pages [13] -->
GRD 538231 GHA 532048 SMR 498067 KWT 389859 SAU 222158 TKM 197115 MKD 153243

<!-- b002946 | prose | pages [13] -->
p pred

<!-- b002947 | prose | pages [13] -->
1 1 1 1 0.847 2 0.684 1 0.0011 1 3.01e-09 1 1.22e-26 1

<!-- b002948 | prose | pages [13] -->
微信号：MATHmodels

<!-- b002949 | prose | pages [13] -->
BFA 153243 1.22e-26 1

<!-- b002950 | prose | pages [13] -->
rejection region. This suggests that the predicted gold medal counts for SMR and KWT at the 2028 Olympics are significantly greater than 1, implying that both countries are likely to achieve a “breakthrough of zero” in gold medals, with probabilities of 0.847 and 0.684, respectively.

<!-- b002951 | prose | pages [13] -->
According to Table 3, the predicted gold medal count for SMR at the 2028 Olympics is 2, with a 95% approximate confidence interval of [1, 3], indicating relatively stable predictions. For KWT, the predicted gold medal count is 1, with a 95% approximate confidence interval of [0, 2]. The violin plot in Fig. 7 illustrates that most of the prediction data for KWT falls within the range of 1 to 2.

<!-- b002952 | prose | pages [13] -->
Olympic Events and Medal Counts 3.3

<!-- b002953 | prose | pages [13] -->
We have chosen to utilize SHAP1,10 analysis tools for the correlation analysis and importance measurement between Olympic events and medal counts.

<!-- b002954 | prose | pages [13] -->
Spearman: A Mathematical Analysis 3.3.1

<!-- b002955 | prose | pages [13] -->
The Spearman correlation coefficient is a non-parametric measure of rank correla- tion. In contrast to the Pearson correlation coefficient, which is limited to characterizing linear relationships and requires data to follow a normal distribution, the Spearman corre- lation is computed based on rank orders. This approach makes it less sensitive to outliers and allows for a more robust representation of the degree of correlation between variables.

<!-- b002956 | furniture | pages [14] -->
Team # 2500759

<!-- b002957 | furniture | pages [14] -->
Page 14 of 26

<!-- b002958 | prose | pages [14] -->
The Spearman correlation coefficient is defined mathematically as follows:

<!-- b002959 | prose | pages [14] -->
n

<!-- b002960 | prose | pages [14] -->
1

<!-- b002961 | prose | pages [14] -->


<!-- b002962 | prose | pages [14] -->
X

<!-- b002963 | prose | pages [14] -->
 

<!-- b002964 | prose | pages [14] -->


<!-- b002965 | prose | pages [14] -->
R(xi) −R(x)

<!-- b002966 | prose | pages [14] -->
n

<!-- b002967 | prose | pages [14] -->
i=1

<!-- b002968 | prose | pages [14] -->
ρ =

<!-- b002969 | prose | pages [14] -->
v

<!-- b002970 | prose | pages [14] -->
n

<!-- b002971 | prose | pages [14] -->
u t1

<!-- b002972 | prose | pages [14] -->


<!-- b002973 | prose | pages [14] -->
X

<!-- b002974 | prose | pages [14] -->
u

<!-- b002975 | prose | pages [14] -->
R(xi) −R(x)

<!-- b002976 | prose | pages [14] -->
n

<!-- b002977 | prose | pages [14] -->
i=1

<!-- b002978 | prose | pages [14] -->
R(yi) −R(y)

<!-- b002979 | prose | pages [14] -->
(8)

<!-- b002980 | prose | pages [14] -->
v

<!-- b002981 | prose | pages [14] -->
n

<!-- b002982 | prose | pages [14] -->
u t1

<!-- b002983 | prose | pages [14] -->
2 2

<!-- b002984 | prose | pages [14] -->
2

<!-- b002985 | prose | pages [14] -->


<!-- b002986 | prose | pages [14] -->
X

<!-- b002987 | prose | pages [14] -->
u

<!-- b002988 | prose | pages [14] -->
·

<!-- b002989 | prose | pages [14] -->
R(yi) −R(y)

<!-- b002990 | prose | pages [14] -->
n

<!-- b002991 | prose | pages [14] -->
i=1

<!-- b002992 | prose | pages [14] -->
where R(·) denotes the rank of the variable within the sample.

<!-- b002993 | prose | pages [14] -->
Coming up with hypotheses:

<!-- b002994 | prose | pages [14] -->
H0 : ρ = 0 H1 : ρ̸ = 0 vs. vs.

<!-- b002995 | prose | pages [14] -->
The t-test statistic is constructed, and a judgment is made using the rejection region:

<!-- b002996 | prose | pages [14] -->
|ρ| t = r

<!-- b002997 | prose | pages [14] -->
ρ2

<!-- b002998 | prose | pages [14] -->
n −2

<!-- b002999 | prose | pages [14] -->
H0 ∼t(n −2)

<!-- b003000 | prose | pages [14] -->
t > tα(n −2)

<!-- b003001 | prose | pages [14] -->


<!-- b003002 | prose | pages [14] -->
m

<!-- b003003 | prose | pages [14] -->
m

<!-- b003004 | prose | pages [14] -->
m

<!-- b003005 | prose | pages [14] -->
m

<!-- b003006 | prose | pages [14] -->
m

<!-- b003007 | prose | pages [14] -->
m

<!-- b003008 | prose | pages [14] -->
m

<!-- b003009 | prose | pages [14] -->
m

<!-- b003010 | prose | pages [14] -->
m

<!-- b003011 | prose | pages [14] -->
m

<!-- b003012 | prose | pages [14] -->
m

<!-- b003013 | prose | pages [14] -->
m

<!-- b003014 | prose | pages [14] -->
m

<!-- b003015 | prose | pages [14] -->
m

<!-- b003016 | prose | pages [14] -->
m

<!-- b003017 | prose | pages [14] -->
w =

<!-- b003018 | prose | pages [14] -->
(x, y)

<!-- b003019 | prose | pages [14] -->
m

<!-- b003020 | prose | pages [14] -->
m

<!-- b003021 | prose | pages [14] -->
m

<!-- b003022 | prose | pages [14] -->
m

<!-- b003023 | prose | pages [14] -->
m

<!-- b003024 | prose | pages [14] -->
m

<!-- b003025 | prose | pages [14] -->
m

<!-- b003026 | prose | pages [14] -->
m

<!-- b003027 | prose | pages [14] -->
m

<!-- b003028 | prose | pages [14] -->
m

<!-- b003029 | prose | pages [14] -->
m

<!-- b003030 | prose | pages [14] -->
m

<!-- b003031 | prose | pages [14] -->
m

<!-- b003032 | prose | pages [14] -->
m

<!-- b003033 | prose | pages [14] -->
m

<!-- b003034 | prose | pages [14] -->
m

<!-- b003035 | prose | pages [14] -->
m

<!-- b003036 | prose | pages [14] -->
m

<!-- b003037 | prose | pages [14] -->
m

<!-- b003038 | prose | pages [14] -->
m

<!-- b003039 | prose | pages [14] -->
m

<!-- b003040 | prose | pages [14] -->
m

<!-- b003041 | prose | pages [14] -->
m

<!-- b003042 | prose | pages [14] -->
m

<!-- b003043 | prose | pages [14] -->
m

<!-- b003044 | prose | pages [14] -->
m

<!-- b003045 | prose | pages [14] -->
m

<!-- b003046 | prose | pages [14] -->
m

<!-- b003047 | prose | pages [14] -->
m

<!-- b003048 | prose | pages [14] -->
m

<!-- b003049 | prose | pages [14] -->
m

<!-- b003050 | prose | pages [14] -->
m

<!-- b003051 | prose | pages [14] -->
m

<!-- b003052 | prose | pages [14] -->
m

<!-- b003053 | prose | pages [14] -->
m

<!-- b003054 | prose | pages [14] -->
m

<!-- b003055 | prose | pages [14] -->
m

<!-- b003056 | prose | pages [14] -->
m

<!-- b003057 | prose | pages [14] -->
m

<!-- b003058 | prose | pages [14] -->
m

<!-- b003059 | prose | pages [14] -->
m

<!-- b003060 | prose | pages [14] -->
m

<!-- b003061 | prose | pages [14] -->
m

<!-- b003062 | prose | pages [14] -->
m

<!-- b003063 | prose | pages [14] -->
m

<!-- b003064 | prose | pages [14] -->
m

<!-- b003065 | prose | pages [14] -->
m

<!-- b003066 | prose | pages [14] -->
m

<!-- b003067 | prose | pages [14] -->
m

<!-- b003068 | prose | pages [14] -->
m

<!-- b003069 | prose | pages [14] -->
m

<!-- b003070 | prose | pages [14] -->
m

<!-- b003071 | prose | pages [14] -->
m

<!-- b003072 | prose | pages [14] -->
m

<!-- b003073 | prose | pages [14] -->
m

<!-- b003074 | prose | pages [14] -->
m

<!-- b003075 | prose | pages [14] -->
m

<!-- b003076 | prose | pages [14] -->
m

<!-- b003077 | prose | pages [14] -->
m

<!-- b003078 | prose | pages [14] -->
m

<!-- b003079 | prose | pages [14] -->
m

<!-- b003080 | prose | pages [14] -->
m

<!-- b003081 | prose | pages [14] -->
m

<!-- b003082 | prose | pages [14] -->
m

<!-- b003083 | prose | pages [14] -->
m

<!-- b003084 | prose | pages [14] -->
m

<!-- b003085 | prose | pages [14] -->
m

<!-- b003086 | prose | pages [14] -->
m

<!-- b003087 | prose | pages [14] -->
m

<!-- b003088 | prose | pages [14] -->
m

<!-- b003089 | prose | pages [14] -->
m

<!-- b003090 | prose | pages [14] -->
m

<!-- b003091 | prose | pages [14] -->
m

<!-- b003092 | prose | pages [14] -->
m

<!-- b003093 | prose | pages [14] -->
m

<!-- b003094 | prose | pages [14] -->
m

<!-- b003095 | prose | pages [14] -->
m

<!-- b003096 | prose | pages [14] -->
m

<!-- b003097 | prose | pages [14] -->
m

<!-- b003098 | prose | pages [14] -->
m

<!-- b003099 | prose | pages [14] -->
m

<!-- b003100 | prose | pages [14] -->
m

<!-- b003101 | prose | pages [14] -->
m

<!-- b003102 | prose | pages [14] -->
m

<!-- b003103 | prose | pages [14] -->
m

<!-- b003104 | prose | pages [14] -->
m

<!-- b003105 | prose | pages [14] -->
m

<!-- b003106 | prose | pages [14] -->
m

<!-- b003107 | prose | pages [14] -->
m

<!-- b003108 | prose | pages [14] -->
m

<!-- b003109 | prose | pages [14] -->
m

<!-- b003110 | prose | pages [14] -->
m

<!-- b003111 | prose | pages [14] -->
m

<!-- b003112 | prose | pages [14] -->
m

<!-- b003113 | prose | pages [14] -->
m

<!-- b003114 | prose | pages [14] -->
m

<!-- b003115 | prose | pages [14] -->
m

<!-- b003116 | prose | pages [14] -->
m

<!-- b003117 | prose | pages [14] -->
m

<!-- b003118 | prose | pages [14] -->
m

<!-- b003119 | prose | pages [14] -->
m

<!-- b003120 | prose | pages [14] -->
m

<!-- b003121 | prose | pages [14] -->
m

<!-- b003122 | prose | pages [14] -->
m

<!-- b003123 | prose | pages [14] -->
m

<!-- b003124 | prose | pages [14] -->
m

<!-- b003125 | prose | pages [14] -->
m

<!-- b003126 | prose | pages [14] -->
m

<!-- b003127 | prose | pages [14] -->
m

<!-- b003128 | prose | pages [14] -->
m

<!-- b003129 | prose | pages [14] -->
m

<!-- b003130 | prose | pages [14] -->
m

<!-- b003131 | prose | pages [14] -->
m

<!-- b003132 | prose | pages [14] -->
m

<!-- b003133 | prose | pages [14] -->
m

<!-- b003134 | prose | pages [14] -->
m

<!-- b003135 | prose | pages [14] -->
m

<!-- b003136 | prose | pages [14] -->
m

<!-- b003137 | prose | pages [14] -->
m

<!-- b003138 | prose | pages [14] -->
m

<!-- b003139 | prose | pages [14] -->
m

<!-- b003140 | prose | pages [14] -->
m

<!-- b003141 | prose | pages [14] -->
m

<!-- b003142 | prose | pages [14] -->
m

<!-- b003143 | prose | pages [14] -->
m

<!-- b003144 | prose | pages [14] -->
m

<!-- b003145 | prose | pages [14] -->
m

<!-- b003146 | prose | pages [14] -->
m

<!-- b003147 | prose | pages [14] -->
m

<!-- b003148 | prose | pages [14] -->
m

<!-- b003149 | prose | pages [14] -->
m

<!-- b003150 | prose | pages [14] -->
m

<!-- b003151 | prose | pages [14] -->
m

<!-- b003152 | prose | pages [14] -->
m

<!-- b003153 | prose | pages [14] -->
m

<!-- b003154 | prose | pages [14] -->
m

<!-- b003155 | prose | pages [14] -->
m

<!-- b003156 | prose | pages [14] -->
m

<!-- b003157 | prose | pages [14] -->
m

<!-- b003158 | prose | pages [14] -->
m

<!-- b003159 | prose | pages [14] -->
m

<!-- b003160 | prose | pages [14] -->
m

<!-- b003161 | prose | pages [14] -->
m

<!-- b003162 | prose | pages [14] -->
m

<!-- b003163 | prose | pages [14] -->
m

<!-- b003164 | prose | pages [14] -->
m

<!-- b003165 | prose | pages [14] -->
m

<!-- b003166 | prose | pages [14] -->
m

<!-- b003167 | prose | pages [14] -->
m

<!-- b003168 | prose | pages [14] -->
m

<!-- b003169 | prose | pages [14] -->
m

<!-- b003170 | prose | pages [14] -->
m

<!-- b003171 | prose | pages [14] -->
m

<!-- b003172 | prose | pages [14] -->
m

<!-- b003173 | prose | pages [14] -->
m

<!-- b003174 | prose | pages [14] -->
m

<!-- b003175 | prose | pages [14] -->
m

<!-- b003176 | prose | pages [14] -->
m

<!-- b003177 | prose | pages [14] -->
m

<!-- b003178 | prose | pages [14] -->
m

<!-- b003179 | prose | pages [14] -->
m

<!-- b003180 | prose | pages [14] -->
m

<!-- b003181 | prose | pages [14] -->
m

<!-- b003182 | prose | pages [14] -->
m

<!-- b003183 | prose | pages [14] -->
m

<!-- b003184 | prose | pages [14] -->
m

<!-- b003185 | prose | pages [14] -->
m

<!-- b003186 | prose | pages [14] -->
m

<!-- b003187 | prose | pages [14] -->
m

<!-- b003188 | prose | pages [14] -->
m

<!-- b003189 | prose | pages [14] -->
m

<!-- b003190 | prose | pages [14] -->
m

<!-- b003191 | prose | pages [14] -->
m

<!-- b003192 | prose | pages [14] -->
m

<!-- b003193 | prose | pages [14] -->
m

<!-- b003194 | prose | pages [14] -->
m

<!-- b003195 | prose | pages [14] -->
m

<!-- b003196 | prose | pages [14] -->
m

<!-- b003197 | prose | pages [14] -->
m

<!-- b003198 | prose | pages [14] -->
m

<!-- b003199 | prose | pages [14] -->
m

<!-- b003200 | prose | pages [14] -->
m

<!-- b003201 | prose | pages [14] -->
m

<!-- b003202 | prose | pages [14] -->
m

<!-- b003203 | prose | pages [14] -->
m

<!-- b003204 | prose | pages [14] -->
m

<!-- b003205 | prose | pages [14] -->
m

<!-- b003206 | prose | pages [14] -->
m

<!-- b003207 | prose | pages [14] -->
m

<!-- b003208 | prose | pages [14] -->
m

<!-- b003209 | prose | pages [14] -->
m

<!-- b003210 | prose | pages [14] -->
m

<!-- b003211 | prose | pages [14] -->
m

<!-- b003212 | prose | pages [14] -->
m

<!-- b003213 | prose | pages [14] -->
m

<!-- b003214 | prose | pages [14] -->
m

<!-- b003215 | prose | pages [14] -->
m

<!-- b003216 | prose | pages [14] -->
m

<!-- b003217 | prose | pages [14] -->
m

<!-- b003218 | prose | pages [14] -->
m

<!-- b003219 | prose | pages [14] -->
m

<!-- b003220 | prose | pages [14] -->
m

<!-- b003221 | prose | pages [14] -->
m

<!-- b003222 | prose | pages [14] -->
m

<!-- b003223 | prose | pages [14] -->
m

<!-- b003224 | prose | pages [14] -->
m

<!-- b003225 | prose | pages [14] -->
m

<!-- b003226 | prose | pages [14] -->
m

<!-- b003227 | prose | pages [14] -->
m

<!-- b003228 | prose | pages [14] -->
m

<!-- b003229 | prose | pages [14] -->
m

<!-- b003230 | prose | pages [14] -->
m

<!-- b003231 | prose | pages [14] -->
m

<!-- b003232 | prose | pages [14] -->
m

<!-- b003233 | prose | pages [14] -->
m

<!-- b003234 | prose | pages [14] -->
m

<!-- b003235 | prose | pages [14] -->
m

<!-- b003236 | prose | pages [14] -->
m

<!-- b003237 | prose | pages [14] -->
m

<!-- b003238 | prose | pages [14] -->
m

<!-- b003239 | prose | pages [14] -->
m

<!-- b003240 | prose | pages [14] -->
m

<!-- b003241 | prose | pages [14] -->


<!-- b003242 | prose | pages [14] -->
m m

<!-- b003243 | prose | pages [14] -->
m m

<!-- b003244 | prose | pages [14] -->
m m

<!-- b003245 | prose | pages [14] -->
m m

<!-- b003246 | prose | pages [14] -->
m

<!-- b003247 | prose | pages [14] -->
m

<!-- b003248 | prose | pages [14] -->
m

<!-- b003249 | prose | pages [14] -->
m m

<!-- b003250 | prose | pages [14] -->
m m

<!-- b003251 | prose | pages [14] -->
m m

<!-- b003252 | prose | pages [14] -->
m

<!-- b003253 | prose | pages [14] -->
m

<!-- b003254 | prose | pages [14] -->
m m

<!-- b003255 | prose | pages [14] -->
m m

<!-- b003256 | prose | pages [14] -->
m m

<!-- b003257 | prose | pages [14] -->
m

<!-- b003258 | prose | pages [14] -->
m

<!-- b003259 | prose | pages [14] -->
m

<!-- b003260 | prose | pages [14] -->
m m

<!-- b003261 | prose | pages [14] -->
m m

<!-- b003262 | prose | pages [14] -->
m

<!-- b003263 | prose | pages [14] -->
m

<!-- b003264 | prose | pages [14] -->
m

<!-- b003265 | prose | pages [14] -->
m

<!-- b003266 | prose | pages [14] -->
m m

<!-- b003267 | prose | pages [14] -->
m m

<!-- b003268 | prose | pages [14] -->
m m

<!-- b003269 | prose | pages [14] -->
m m

<!-- b003270 | prose | pages [14] -->
m m

<!-- b003271 | prose | pages [14] -->
m m

<!-- b003272 | prose | pages [14] -->
m

<!-- b003273 | prose | pages [14] -->
m

<!-- b003274 | prose | pages [14] -->
m

<!-- b003275 | prose | pages [14] -->
m m

<!-- b003276 | prose | pages [14] -->
m m

<!-- b003277 | prose | pages [14] -->
m m

<!-- b003278 | prose | pages [14] -->
m

<!-- b003279 | prose | pages [14] -->
m

<!-- b003280 | prose | pages [14] -->
m m

<!-- b003281 | prose | pages [14] -->
m m

<!-- b003282 | prose | pages [14] -->
m m

<!-- b003283 | prose | pages [14] -->
m m

<!-- b003284 | prose | pages [14] -->
m

<!-- b003285 | prose | pages [14] -->
m

<!-- b003286 | prose | pages [14] -->
m

<!-- b003287 | prose | pages [14] -->
m

<!-- b003288 | prose | pages [14] -->
m m

<!-- b003289 | prose | pages [14] -->
m m

<!-- b003290 | prose | pages [14] -->
m m

<!-- b003291 | prose | pages [14] -->
m m

<!-- b003292 | prose | pages [14] -->
m

<!-- b003293 | prose | pages [14] -->
m

<!-- b003294 | prose | pages [14] -->
m

<!-- b003295 | prose | pages [14] -->
m m

<!-- b003296 | prose | pages [14] -->
m m

<!-- b003297 | prose | pages [14] -->
m m

<!-- b003298 | prose | pages [14] -->
m m

<!-- b003299 | prose | pages [14] -->
m m

<!-- b003300 | prose | pages [14] -->
m

<!-- b003301 | prose | pages [14] -->
m

<!-- b003302 | prose | pages [14] -->
m

<!-- b003303 | prose | pages [14] -->
m

<!-- b003304 | prose | pages [14] -->
m m

<!-- b003305 | prose | pages [14] -->
m m

<!-- b003306 | prose | pages [14] -->
m m

<!-- b003307 | prose | pages [14] -->
m m

<!-- b003308 | prose | pages [14] -->
m m

<!-- b003309 | prose | pages [14] -->
m m

<!-- b003310 | prose | pages [14] -->
m m

<!-- b003311 | prose | pages [14] -->
m m

<!-- b003312 | prose | pages [14] -->
m

<!-- b003313 | prose | pages [14] -->
m m

<!-- b003314 | prose | pages [14] -->
m m

<!-- b003315 | prose | pages [14] -->
m m

<!-- b003316 | prose | pages [14] -->
m m

<!-- b003317 | prose | pages [14] -->
m

<!-- b003318 | prose | pages [14] -->
m

<!-- b003319 | prose | pages [14] -->
m m

<!-- b003320 | prose | pages [14] -->
m m

<!-- b003321 | prose | pages [14] -->
m m

<!-- b003322 | prose | pages [14] -->
m m

<!-- b003323 | prose | pages [14] -->
m m

<!-- b003324 | prose | pages [14] -->
m m

<!-- b003325 | prose | pages [14] -->
m

<!-- b003326 | prose | pages [14] -->
m

<!-- b003327 | prose | pages [14] -->
m

<!-- b003328 | prose | pages [14] -->
m m

<!-- b003329 | prose | pages [14] -->
m m

<!-- b003330 | prose | pages [14] -->
m m

<!-- b003331 | prose | pages [14] -->
m m

<!-- b003332 | prose | pages [14] -->
m m

<!-- b003333 | prose | pages [14] -->
m m

<!-- b003334 | prose | pages [14] -->
m

<!-- b003335 | prose | pages [14] -->
m m

<!-- b003336 | prose | pages [14] -->
m m

<!-- b003337 | prose | pages [14] -->
m m

<!-- b003338 | prose | pages [14] -->
m

<!-- b003339 | prose | pages [14] -->
m

<!-- b003340 | prose | pages [14] -->
m

<!-- b003341 | prose | pages [14] -->
m

<!-- b003342 | prose | pages [14] -->
m m

<!-- b003343 | prose | pages [14] -->
m m

<!-- b003344 | prose | pages [14] -->
m m

<!-- b003345 | prose | pages [14] -->
m m

<!-- b003346 | prose | pages [14] -->
m m

<!-- b003347 | prose | pages [14] -->
m

<!-- b003348 | prose | pages [14] -->
m

<!-- b003349 | prose | pages [14] -->
m

<!-- b003350 | prose | pages [14] -->
m

<!-- b003351 | prose | pages [14] -->
m

<!-- b003352 | prose | pages [14] -->
m m

<!-- b003353 | prose | pages [14] -->
m m

<!-- b003354 | prose | pages [14] -->
m m

<!-- b003355 | prose | pages [14] -->
m

<!-- b003356 | prose | pages [14] -->
m m

<!-- b003357 | prose | pages [14] -->
m m

<!-- b003358 | prose | pages [14] -->
m m

<!-- b003359 | prose | pages [14] -->
m m

<!-- b003360 | prose | pages [14] -->
m m

<!-- b003361 | prose | pages [14] -->
m

<!-- b003362 | prose | pages [14] -->
m

<!-- b003363 | prose | pages [14] -->
m m

<!-- b003364 | prose | pages [14] -->
m m

<!-- b003365 | prose | pages [14] -->
m m

<!-- b003366 | prose | pages [14] -->
m m

<!-- b003367 | prose | pages [14] -->
m

<!-- b003368 | prose | pages [14] -->
m

<!-- b003369 | prose | pages [14] -->
m

<!-- b003370 | prose | pages [14] -->
m m

<!-- b003371 | prose | pages [14] -->
m m

<!-- b003372 | prose | pages [14] -->
m m

<!-- b003373 | prose | pages [14] -->
m

<!-- b003374 | prose | pages [14] -->
m

<!-- b003375 | prose | pages [14] -->
m

<!-- b003376 | prose | pages [14] -->
m

<!-- b003377 | prose | pages [14] -->
m m

<!-- b003378 | prose | pages [14] -->
m m

<!-- b003379 | prose | pages [14] -->
m m

<!-- b003380 | prose | pages [14] -->
m m

<!-- b003381 | prose | pages [14] -->
m m

<!-- b003382 | prose | pages [14] -->
m

<!-- b003383 | prose | pages [14] -->
m

<!-- b003384 | prose | pages [14] -->
m

<!-- b003385 | prose | pages [14] -->
m

<!-- b003386 | prose | pages [14] -->
m m

<!-- b003387 | prose | pages [14] -->
m m

<!-- b003388 | prose | pages [14] -->
m m

<!-- b003389 | prose | pages [14] -->
m m

<!-- b003390 | prose | pages [14] -->
m

<!-- b003391 | prose | pages [14] -->
m

<!-- b003392 | prose | pages [14] -->
Significance t-test is typically conducted at a significance level of 0.05. In this study,

<!-- b003393 | prose | pages [14] -->
m

<!-- b003394 | prose | pages [14] -->
m

<!-- b003395 | prose | pages [14] -->
m

<!-- b003396 | prose | pages [14] -->
m

<!-- b003397 | prose | pages [14] -->
m

<!-- b003398 | prose | pages [14] -->
m

<!-- b003399 | prose | pages [14] -->
m

<!-- b003400 | prose | pages [14] -->
m

<!-- b003401 | prose | pages [14] -->
m

<!-- b003402 | prose | pages [14] -->
m

<!-- b003403 | prose | pages [14] -->
m

<!-- b003404 | prose | pages [14] -->
m

<!-- b003405 | prose | pages [14] -->
m

<!-- b003406 | prose | pages [14] -->
m

<!-- b003407 | prose | pages [14] -->
m

<!-- b003408 | prose | pages [14] -->
m

<!-- b003409 | prose | pages [14] -->
m

<!-- b003410 | prose | pages [14] -->
m

<!-- b003411 | prose | pages [14] -->
m

<!-- b003412 | prose | pages [14] -->
m

<!-- b003413 | prose | pages [14] -->
m

<!-- b003414 | prose | pages [14] -->
m

<!-- b003415 | prose | pages [14] -->
m

<!-- b003416 | prose | pages [14] -->
m

<!-- b003417 | prose | pages [14] -->
m

<!-- b003418 | prose | pages [14] -->
m

<!-- b003419 | prose | pages [14] -->
m

<!-- b003420 | prose | pages [14] -->
m

<!-- b003421 | prose | pages [14] -->
m

<!-- b003422 | prose | pages [14] -->
m

<!-- b003423 | prose | pages [14] -->
m

<!-- b003424 | prose | pages [14] -->
m

<!-- b003425 | prose | pages [14] -->
m

<!-- b003426 | prose | pages [14] -->
m

<!-- b003427 | prose | pages [14] -->
m

<!-- b003428 | prose | pages [14] -->
m

<!-- b003429 | prose | pages [14] -->
m

<!-- b003430 | prose | pages [14] -->
m

<!-- b003431 | prose | pages [14] -->
m

<!-- b003432 | prose | pages [14] -->
m

<!-- b003433 | prose | pages [14] -->
m

<!-- b003434 | prose | pages [14] -->
m

<!-- b003435 | prose | pages [14] -->
m

<!-- b003436 | prose | pages [14] -->
m

<!-- b003437 | prose | pages [14] -->
m

<!-- b003438 | prose | pages [14] -->
m

<!-- b003439 | prose | pages [14] -->
m

<!-- b003440 | prose | pages [14] -->
m

<!-- b003441 | prose | pages [14] -->
m

<!-- b003442 | prose | pages [14] -->
m

<!-- b003443 | prose | pages [14] -->
m

<!-- b003444 | prose | pages [14] -->
m

<!-- b003445 | prose | pages [14] -->
m

<!-- b003446 | prose | pages [14] -->
m

<!-- b003447 | prose | pages [14] -->
m

<!-- b003448 | prose | pages [14] -->
m

<!-- b003449 | prose | pages [14] -->
m

<!-- b003450 | prose | pages [14] -->
m

<!-- b003451 | prose | pages [14] -->
m

<!-- b003452 | prose | pages [14] -->
m

<!-- b003453 | prose | pages [14] -->
m

<!-- b003454 | prose | pages [14] -->
m

<!-- b003455 | prose | pages [14] -->
m

<!-- b003456 | prose | pages [14] -->
m

<!-- b003457 | prose | pages [14] -->
m

<!-- b003458 | prose | pages [14] -->
m

<!-- b003459 | prose | pages [14] -->
m

<!-- b003460 | prose | pages [14] -->
m

<!-- b003461 | prose | pages [14] -->
m

<!-- b003462 | prose | pages [14] -->
m

<!-- b003463 | prose | pages [14] -->
m

<!-- b003464 | prose | pages [14] -->
m

<!-- b003465 | prose | pages [14] -->
m

<!-- b003466 | prose | pages [14] -->
m

<!-- b003467 | prose | pages [14] -->
m

<!-- b003468 | prose | pages [14] -->
m

<!-- b003469 | prose | pages [14] -->
m

<!-- b003470 | prose | pages [14] -->
m

<!-- b003471 | prose | pages [14] -->
m

<!-- b003472 | prose | pages [14] -->
m

<!-- b003473 | prose | pages [14] -->
m

<!-- b003474 | prose | pages [14] -->
m

<!-- b003475 | prose | pages [14] -->
m

<!-- b003476 | prose | pages [14] -->
m

<!-- b003477 | prose | pages [14] -->
m

<!-- b003478 | prose | pages [14] -->
m

<!-- b003479 | prose | pages [14] -->
m

<!-- b003480 | prose | pages [14] -->
m

<!-- b003481 | prose | pages [14] -->
m

<!-- b003482 | prose | pages [14] -->
m

<!-- b003483 | prose | pages [14] -->
m

<!-- b003484 | prose | pages [14] -->
m

<!-- b003485 | prose | pages [14] -->
m

<!-- b003486 | prose | pages [14] -->
m

<!-- b003487 | prose | pages [14] -->
m m

<!-- b003488 | prose | pages [14] -->
m m

<!-- b003489 | prose | pages [14] -->
m m

<!-- b003490 | prose | pages [14] -->
m m

<!-- b003491 | prose | pages [14] -->
m m

<!-- b003492 | prose | pages [14] -->
m

<!-- b003493 | prose | pages [14] -->
m

<!-- b003494 | prose | pages [14] -->
m m

<!-- b003495 | prose | pages [14] -->
m m

<!-- b003496 | prose | pages [14] -->
m m

<!-- b003497 | prose | pages [14] -->
m m

<!-- b003498 | prose | pages [14] -->
m

<!-- b003499 | prose | pages [14] -->
m

<!-- b003500 | prose | pages [14] -->
m

<!-- b003501 | prose | pages [14] -->
m m

<!-- b003502 | prose | pages [14] -->
m m

<!-- b003503 | prose | pages [14] -->
m m

<!-- b003504 | prose | pages [14] -->
m

<!-- b003505 | prose | pages [14] -->
m

<!-- b003506 | prose | pages [14] -->
m

<!-- b003507 | prose | pages [14] -->
m m

<!-- b003508 | prose | pages [14] -->
m m

<!-- b003509 | prose | pages [14] -->
m m

<!-- b003510 | prose | pages [14] -->
m m

<!-- b003511 | prose | pages [14] -->
m m

<!-- b003512 | prose | pages [14] -->
m

<!-- b003513 | prose | pages [14] -->
m m

<!-- b003514 | prose | pages [14] -->
m m

<!-- b003515 | prose | pages [14] -->
m m

<!-- b003516 | prose | pages [14] -->
m

<!-- b003517 | prose | pages [14] -->
m

<!-- b003518 | prose | pages [14] -->
m m

<!-- b003519 | prose | pages [14] -->
m m

<!-- b003520 | prose | pages [14] -->
m m

<!-- b003521 | prose | pages [14] -->
m m

<!-- b003522 | prose | pages [14] -->
m

<!-- b003523 | prose | pages [14] -->
m

<!-- b003524 | prose | pages [14] -->
m m

<!-- b003525 | prose | pages [14] -->
m m

<!-- b003526 | prose | pages [14] -->
m m

<!-- b003527 | prose | pages [14] -->
m

<!-- b003528 | prose | pages [14] -->
m

<!-- b003529 | prose | pages [14] -->
m

<!-- b003530 | prose | pages [14] -->
m m

<!-- b003531 | prose | pages [14] -->
m m

<!-- b003532 | prose | pages [14] -->
m m

<!-- b003533 | prose | pages [14] -->
m m

<!-- b003534 | prose | pages [14] -->
m

<!-- b003535 | prose | pages [14] -->
m

<!-- b003536 | prose | pages [14] -->
m

<!-- b003537 | prose | pages [14] -->
m

<!-- b003538 | prose | pages [14] -->
we calculate the Spearman correlation coefficients and conduct hypothesis testing based

<!-- b003539 | prose | pages [14] -->
m

<!-- b003540 | prose | pages [14] -->
m

<!-- b003541 | prose | pages [14] -->
m

<!-- b003542 | prose | pages [14] -->
m

<!-- b003543 | prose | pages [14] -->
m

<!-- b003544 | prose | pages [14] -->
m

<!-- b003545 | prose | pages [14] -->
m

<!-- b003546 | prose | pages [14] -->
m

<!-- b003547 | prose | pages [14] -->
m

<!-- b003548 | prose | pages [14] -->
m

<!-- b003549 | prose | pages [14] -->
m

<!-- b003550 | prose | pages [14] -->
m

<!-- b003551 | prose | pages [14] -->
m

<!-- b003552 | prose | pages [14] -->
m

<!-- b003553 | prose | pages [14] -->
m

<!-- b003554 | prose | pages [14] -->
m

<!-- b003555 | prose | pages [14] -->
m

<!-- b003556 | prose | pages [14] -->
m

<!-- b003557 | prose | pages [14] -->
m

<!-- b003558 | prose | pages [14] -->
m

<!-- b003559 | prose | pages [14] -->
m

<!-- b003560 | prose | pages [14] -->
m

<!-- b003561 | prose | pages [14] -->
m

<!-- b003562 | prose | pages [14] -->
m

<!-- b003563 | prose | pages [14] -->
m

<!-- b003564 | prose | pages [14] -->
m

<!-- b003565 | prose | pages [14] -->
m

<!-- b003566 | prose | pages [14] -->
m

<!-- b003567 | prose | pages [14] -->
m

<!-- b003568 | prose | pages [14] -->
m

<!-- b003569 | prose | pages [14] -->
m

<!-- b003570 | prose | pages [14] -->
m

<!-- b003571 | prose | pages [14] -->
m

<!-- b003572 | prose | pages [14] -->
m

<!-- b003573 | prose | pages [14] -->
m

<!-- b003574 | prose | pages [14] -->
m

<!-- b003575 | prose | pages [14] -->
m

<!-- b003576 | prose | pages [14] -->
m

<!-- b003577 | prose | pages [14] -->
m

<!-- b003578 | prose | pages [14] -->
m

<!-- b003579 | prose | pages [14] -->
m

<!-- b003580 | prose | pages [14] -->
m

<!-- b003581 | prose | pages [14] -->
m

<!-- b003582 | prose | pages [14] -->
m

<!-- b003583 | prose | pages [14] -->
m

<!-- b003584 | prose | pages [14] -->
m

<!-- b003585 | prose | pages [14] -->
m

<!-- b003586 | prose | pages [14] -->
m

<!-- b003587 | prose | pages [14] -->
m

<!-- b003588 | prose | pages [14] -->
m

<!-- b003589 | prose | pages [14] -->
m

<!-- b003590 | prose | pages [14] -->
m

<!-- b003591 | prose | pages [14] -->
m

<!-- b003592 | prose | pages [14] -->
m

<!-- b003593 | prose | pages [14] -->
m

<!-- b003594 | prose | pages [14] -->
m

<!-- b003595 | prose | pages [14] -->
m

<!-- b003596 | prose | pages [14] -->
m

<!-- b003597 | prose | pages [14] -->
m

<!-- b003598 | prose | pages [14] -->
m

<!-- b003599 | prose | pages [14] -->
m

<!-- b003600 | prose | pages [14] -->
m

<!-- b003601 | prose | pages [14] -->
m

<!-- b003602 | prose | pages [14] -->
m

<!-- b003603 | prose | pages [14] -->
m

<!-- b003604 | prose | pages [14] -->
m

<!-- b003605 | prose | pages [14] -->
m

<!-- b003606 | prose | pages [14] -->
m

<!-- b003607 | prose | pages [14] -->
m

<!-- b003608 | prose | pages [14] -->
m

<!-- b003609 | prose | pages [14] -->
m

<!-- b003610 | prose | pages [14] -->
m

<!-- b003611 | prose | pages [14] -->
m

<!-- b003612 | prose | pages [14] -->
m

<!-- b003613 | prose | pages [14] -->
m

<!-- b003614 | prose | pages [14] -->
m

<!-- b003615 | prose | pages [14] -->
m

<!-- b003616 | prose | pages [14] -->
m

<!-- b003617 | prose | pages [14] -->
m

<!-- b003618 | prose | pages [14] -->
m

<!-- b003619 | prose | pages [14] -->
m

<!-- b003620 | prose | pages [14] -->
m

<!-- b003621 | prose | pages [14] -->
m

<!-- b003622 | prose | pages [14] -->
m

<!-- b003623 | prose | pages [14] -->
m

<!-- b003624 | prose | pages [14] -->
m

<!-- b003625 | prose | pages [14] -->
m

<!-- b003626 | prose | pages [14] -->
m

<!-- b003627 | prose | pages [14] -->
m

<!-- b003628 | prose | pages [14] -->
m

<!-- b003629 | prose | pages [14] -->
m

<!-- b003630 | prose | pages [14] -->
m

<!-- b003631 | prose | pages [14] -->
m

<!-- b003632 | prose | pages [14] -->
m

<!-- b003633 | prose | pages [14] -->
m

<!-- b003634 | prose | pages [14] -->
m

<!-- b003635 | prose | pages [14] -->
m

<!-- b003636 | prose | pages [14] -->
m

<!-- b003637 | prose | pages [14] -->
m

<!-- b003638 | prose | pages [14] -->
m m m m

<!-- b003639 | prose | pages [14] -->
m m

<!-- b003640 | prose | pages [14] -->
m m

<!-- b003641 | prose | pages [14] -->
m m

<!-- b003642 | prose | pages [14] -->
m m

<!-- b003643 | prose | pages [14] -->
m

<!-- b003644 | prose | pages [14] -->
m

<!-- b003645 | prose | pages [14] -->
m

<!-- b003646 | prose | pages [14] -->
m

<!-- b003647 | prose | pages [14] -->
m

<!-- b003648 | prose | pages [14] -->
m m

<!-- b003649 | prose | pages [14] -->
m m

<!-- b003650 | prose | pages [14] -->
m m

<!-- b003651 | prose | pages [14] -->
m m

<!-- b003652 | prose | pages [14] -->
m

<!-- b003653 | prose | pages [14] -->
m m

<!-- b003654 | prose | pages [14] -->
m m

<!-- b003655 | prose | pages [14] -->
m m

<!-- b003656 | prose | pages [14] -->
m m

<!-- b003657 | prose | pages [14] -->
m m

<!-- b003658 | prose | pages [14] -->
m m

<!-- b003659 | prose | pages [14] -->
m

<!-- b003660 | prose | pages [14] -->
m

<!-- b003661 | prose | pages [14] -->
m

<!-- b003662 | prose | pages [14] -->
m

<!-- b003663 | prose | pages [14] -->
m m

<!-- b003664 | prose | pages [14] -->
m m

<!-- b003665 | prose | pages [14] -->
m m

<!-- b003666 | prose | pages [14] -->
m m

<!-- b003667 | prose | pages [14] -->
m

<!-- b003668 | prose | pages [14] -->
m

<!-- b003669 | prose | pages [14] -->
m

<!-- b003670 | prose | pages [14] -->
m

<!-- b003671 | prose | pages [14] -->
m m

<!-- b003672 | prose | pages [14] -->
m m

<!-- b003673 | prose | pages [14] -->
m m

<!-- b003674 | prose | pages [14] -->
m

<!-- b003675 | prose | pages [14] -->
m

<!-- b003676 | prose | pages [14] -->
m

<!-- b003677 | prose | pages [14] -->
m

<!-- b003678 | prose | pages [14] -->
m m

<!-- b003679 | prose | pages [14] -->
m m

<!-- b003680 | prose | pages [14] -->
m m

<!-- b003681 | prose | pages [14] -->
m m

<!-- b003682 | prose | pages [14] -->
m m

<!-- b003683 | prose | pages [14] -->
m

<!-- b003684 | prose | pages [14] -->
m m

<!-- b003685 | prose | pages [14] -->
m m

<!-- b003686 | prose | pages [14] -->
m m

<!-- b003687 | prose | pages [14] -->
m m

<!-- b003688 | prose | pages [14] -->
m

<!-- b003689 | prose | pages [14] -->
m

<!-- b003690 | prose | pages [14] -->
m

<!-- b003691 | prose | pages [14] -->
m

<!-- b003692 | prose | pages [14] -->
m

<!-- b003693 | prose | pages [14] -->
on the weighted values of the various sports in the 2024 Paris Olympics in relation to the number of gold medals and total medals won by each country. This analysis aims to explore the interrelationships between the different sports and their respective gold and medal counts from a mathematical perspective.

<!-- b003694 | prose | pages [14] -->
SHAP: Revealing Correlations and Importance 3.3.2

<!-- b003695 | prose | pages [14] -->
SHAP is a game theory-based tool that enhances the interpretability of machine learning models. Its core advantages lie in providing consistent, precise, and fair expla- nations. The rationale for selecting SHAP analysis tools to examine the interrelationships and importance of each sport in relation to various countries is as follows:

<!-- b003696 | prose | pages [14] -->
• Explanation of predictive models The fundamental function of SHAP is to compute the contribution of each feature to the final prediction outcome while also indicating the direction of this contribu- tion—positive or negative. Utilizing the beeswarm plot and importance plot, SHAP allows for the quantification of each sport’s significance regarding the number of gold and total medals won, in conjunction with the PCA loading matrix.

<!-- b003697 | prose | pages [14] -->
• Nonlinear processing and feature dependencies SHAP can reveal the nonlinear relationships of each feature within the XGBoost model when multiple features interact. It provides accurate contribution scores for each feature, with univariate dependence plots illustrating the impact of different sports’ principal components on gold and medal counts.

<!-- b003698 | prose | pages [14] -->
• Local and global explanations In addition to the aforementioned analyses, SHAP provides local explanations for

<!-- b003699 | prose | pages [14] -->
关注数学模型

<!-- b003700 | furniture | pages [14] -->
2

<!-- b003701 | furniture | pages [14] -->
MATHmodels

<!-- b003702 | furniture | pages [14] -->
获取更多资讯

<!-- b003703 | furniture | pages [15] -->
Team # 2500759

<!-- b003704 | furniture | pages [15] -->
Page 15 of 26

<!-- b003705 | prose | pages [15] -->
individual samples, allowing for a detailed examination of the degree of contribu- tion from each feature. This facilitates an in-depth analysis of the associations be- tween different sports and various countries. Specifically, by leveraging the SHAP force plot for a single sample, one can observe which sports primarily influence the medal counts of a particular country.

<!-- b003706 | prose | pages [15] -->
3.3.3 Analysis of Relationships and Importance

<!-- b003707 | prose | pages [15] -->
Based on the formula for the Spearman correlation coefficient and hypothesis test- ing, sports with non-significant correlation coefficients, such as Wrestling, Beach Volley- ball, Handball, Trampoline Gymnastics, and Cycling, were excluded. Fig. 8 illustrates

<!-- b003708 | prose | pages [15] -->
微信公众号：数学模型

<!-- b003709 | prose | pages [15] -->
the correlation between gold medals, total medals, and various sports for the 2024 Paris Olympics.

<!-- b003710 | caption | pages [15] -->
Figure 8: Spearman Correlation Coefficient Heatmap

<!-- b003711 | prose | pages [15] -->
微信号：MATHmodels

<!-- b003712 | prose | pages [15] -->
The Spearman correlation analysis reveals several key insights: Sports such as Swim- ming, Athletics, and Shooting demonstrate a strong relationship between gold and total medals, primarily due to their multiple events that enhance medal potential, with strong nations particularly excelling in Swimming and Athletics. Conversely, team sports (e.g., Basketball, Volleyball) and some group sports (e.g., Rowing, Canoeing) exhibit weaker correlations between gold and total medals, as their gold counts are less concentrated despite higher total medal counts attributed to broader participation across nations. Addi- tionally, newly introduced sports like Skateboarding and Karate showcase a lower corre- lation for gold medals (0.210) but a higher correlation for total medals (0.496), indicating a more dispersed gold distribution alongside increased total medals. The growth of these sports likely stems from greater participation and competition, contributing to a more equitable medal distribution overall.

<!-- b003713 | prose | pages [15] -->
The XGBoost prediction model for gold and total medals at the 2028 Olympics, constructed previously, calculates SHAP values based on the training set, resulting in the hexagonal importance mix plot in Fig. 9 for five principal component features. In the gold medal prediction model, the two most important principal components are PC1 (0.8345) and PC2 (0.1055). For the total medal prediction model, the leading components are PC1 (0.6242) and PC5 (0.3024), aligning with the highest variance contribution from PC1. The absolute values of the loadings of individual items on the principal components are then weighted by the importance of the components, summed, and normalized to calculate their significance, as shown in Fig. 10.

<!-- b003714 | prose | pages [15] -->
The PCA and SHAP analysis reveals important insights into sports. Shooting and Gymnastics rank among the top three in gold and total medal significance, emphasizing their vital Olympic roles. Shooting’s diversity and Gymnastics’ strong participation from countries like the USA and China contribute to their rankings. Swimming ranks third in

<!-- b003715 | prose | pages [15] -->
m

<!-- b003716 | prose | pages [15] -->
m

<!-- b003717 | prose | pages [15] -->
m

<!-- b003718 | prose | pages [15] -->
m

<!-- b003719 | prose | pages [15] -->
m

<!-- b003720 | prose | pages [15] -->
m

<!-- b003721 | prose | pages [15] -->
m

<!-- b003722 | prose | pages [15] -->
m

<!-- b003723 | prose | pages [15] -->
m

<!-- b003724 | prose | pages [15] -->
m

<!-- b003725 | prose | pages [15] -->
m

<!-- b003726 | prose | pages [15] -->
m

<!-- b003727 | prose | pages [15] -->
m

<!-- b003728 | prose | pages [15] -->
m

<!-- b003729 | prose | pages [15] -->
m

<!-- b003730 | prose | pages [15] -->
m

<!-- b003731 | prose | pages [15] -->
m

<!-- b003732 | prose | pages [15] -->
m

<!-- b003733 | prose | pages [15] -->
m

<!-- b003734 | prose | pages [15] -->
m

<!-- b003735 | prose | pages [15] -->
m

<!-- b003736 | prose | pages [15] -->
m

<!-- b003737 | prose | pages [15] -->
m

<!-- b003738 | prose | pages [15] -->
m

<!-- b003739 | prose | pages [15] -->
m

<!-- b003740 | prose | pages [15] -->
m

<!-- b003741 | prose | pages [15] -->
m

<!-- b003742 | prose | pages [15] -->
m

<!-- b003743 | prose | pages [15] -->
m

<!-- b003744 | prose | pages [15] -->
m

<!-- b003745 | prose | pages [15] -->
m

<!-- b003746 | prose | pages [15] -->
m

<!-- b003747 | prose | pages [15] -->
m

<!-- b003748 | prose | pages [15] -->
m

<!-- b003749 | prose | pages [15] -->
m

<!-- b003750 | prose | pages [15] -->
m

<!-- b003751 | prose | pages [15] -->
m

<!-- b003752 | prose | pages [15] -->
m

<!-- b003753 | prose | pages [15] -->
m

<!-- b003754 | prose | pages [15] -->
m

<!-- b003755 | prose | pages [15] -->
m

<!-- b003756 | prose | pages [15] -->
m

<!-- b003757 | prose | pages [15] -->
m

<!-- b003758 | prose | pages [15] -->
m

<!-- b003759 | prose | pages [15] -->
m

<!-- b003760 | prose | pages [15] -->
m

<!-- b003761 | prose | pages [15] -->
m

<!-- b003762 | prose | pages [15] -->
m

<!-- b003763 | prose | pages [15] -->
m

<!-- b003764 | prose | pages [15] -->
m

<!-- b003765 | prose | pages [15] -->
m

<!-- b003766 | prose | pages [15] -->
m

<!-- b003767 | prose | pages [15] -->
m

<!-- b003768 | prose | pages [15] -->
m

<!-- b003769 | prose | pages [15] -->
m

<!-- b003770 | prose | pages [15] -->
m

<!-- b003771 | prose | pages [15] -->
m

<!-- b003772 | prose | pages [15] -->
m

<!-- b003773 | prose | pages [15] -->
m

<!-- b003774 | prose | pages [15] -->
m

<!-- b003775 | prose | pages [15] -->
m

<!-- b003776 | prose | pages [15] -->
m

<!-- b003777 | prose | pages [15] -->
m

<!-- b003778 | prose | pages [15] -->
m

<!-- b003779 | prose | pages [15] -->
m

<!-- b003780 | prose | pages [15] -->
m

<!-- b003781 | prose | pages [15] -->
m

<!-- b003782 | prose | pages [15] -->
m

<!-- b003783 | prose | pages [15] -->
m

<!-- b003784 | prose | pages [15] -->
m

<!-- b003785 | prose | pages [15] -->
m

<!-- b003786 | prose | pages [15] -->
m

<!-- b003787 | prose | pages [15] -->
m

<!-- b003788 | prose | pages [15] -->
m

<!-- b003789 | prose | pages [15] -->
m

<!-- b003790 | prose | pages [15] -->
m

<!-- b003791 | prose | pages [15] -->
m

<!-- b003792 | prose | pages [15] -->
m

<!-- b003793 | prose | pages [15] -->
m

<!-- b003794 | prose | pages [15] -->
m

<!-- b003795 | prose | pages [15] -->
m

<!-- b003796 | prose | pages [15] -->
m

<!-- b003797 | prose | pages [15] -->
m

<!-- b003798 | prose | pages [15] -->
m

<!-- b003799 | prose | pages [15] -->
m

<!-- b003800 | prose | pages [15] -->
m

<!-- b003801 | prose | pages [15] -->
m

<!-- b003802 | prose | pages [15] -->
m

<!-- b003803 | prose | pages [15] -->
m

<!-- b003804 | prose | pages [15] -->
m

<!-- b003805 | prose | pages [15] -->
m

<!-- b003806 | prose | pages [15] -->
m

<!-- b003807 | prose | pages [15] -->
m

<!-- b003808 | prose | pages [15] -->
m

<!-- b003809 | prose | pages [15] -->
m

<!-- b003810 | prose | pages [15] -->
m

<!-- b003811 | prose | pages [15] -->
m

<!-- b003812 | prose | pages [15] -->
m

<!-- b003813 | prose | pages [15] -->
m

<!-- b003814 | prose | pages [15] -->
m

<!-- b003815 | prose | pages [15] -->
m

<!-- b003816 | prose | pages [15] -->
m

<!-- b003817 | prose | pages [15] -->
m

<!-- b003818 | prose | pages [15] -->
m

<!-- b003819 | prose | pages [15] -->
m

<!-- b003820 | prose | pages [15] -->
m

<!-- b003821 | prose | pages [15] -->
m

<!-- b003822 | prose | pages [15] -->
m

<!-- b003823 | prose | pages [15] -->
m

<!-- b003824 | prose | pages [15] -->
m

<!-- b003825 | prose | pages [15] -->
m

<!-- b003826 | prose | pages [15] -->
m

<!-- b003827 | prose | pages [15] -->
m

<!-- b003828 | prose | pages [15] -->
m

<!-- b003829 | prose | pages [15] -->
m

<!-- b003830 | prose | pages [15] -->
m

<!-- b003831 | prose | pages [15] -->
m

<!-- b003832 | prose | pages [15] -->
m

<!-- b003833 | prose | pages [15] -->
m

<!-- b003834 | prose | pages [15] -->
m

<!-- b003835 | prose | pages [15] -->
m

<!-- b003836 | prose | pages [15] -->
m

<!-- b003837 | prose | pages [15] -->
m

<!-- b003838 | prose | pages [15] -->
m

<!-- b003839 | prose | pages [15] -->
m

<!-- b003840 | prose | pages [15] -->
m

<!-- b003841 | prose | pages [15] -->
m

<!-- b003842 | prose | pages [15] -->
m

<!-- b003843 | prose | pages [15] -->
m

<!-- b003844 | prose | pages [15] -->
m

<!-- b003845 | prose | pages [15] -->
m

<!-- b003846 | prose | pages [15] -->
m

<!-- b003847 | prose | pages [15] -->
m

<!-- b003848 | prose | pages [15] -->
m

<!-- b003849 | prose | pages [15] -->
m

<!-- b003850 | prose | pages [15] -->
m

<!-- b003851 | prose | pages [15] -->
m

<!-- b003852 | prose | pages [15] -->
m

<!-- b003853 | prose | pages [15] -->
m

<!-- b003854 | prose | pages [15] -->
m

<!-- b003855 | prose | pages [15] -->
m

<!-- b003856 | prose | pages [15] -->
m

<!-- b003857 | prose | pages [15] -->
m

<!-- b003858 | prose | pages [15] -->
m

<!-- b003859 | prose | pages [15] -->
m

<!-- b003860 | prose | pages [15] -->
m

<!-- b003861 | prose | pages [15] -->
m

<!-- b003862 | prose | pages [15] -->
m

<!-- b003863 | prose | pages [15] -->
m

<!-- b003864 | prose | pages [15] -->
m

<!-- b003865 | prose | pages [15] -->
m

<!-- b003866 | prose | pages [15] -->
m

<!-- b003867 | prose | pages [15] -->
m

<!-- b003868 | prose | pages [15] -->
m

<!-- b003869 | prose | pages [15] -->
m

<!-- b003870 | prose | pages [15] -->
m

<!-- b003871 | prose | pages [15] -->
m

<!-- b003872 | prose | pages [15] -->
m

<!-- b003873 | prose | pages [15] -->
m

<!-- b003874 | prose | pages [15] -->
m

<!-- b003875 | prose | pages [15] -->
m

<!-- b003876 | prose | pages [15] -->
m

<!-- b003877 | prose | pages [15] -->
m

<!-- b003878 | prose | pages [15] -->
m

<!-- b003879 | prose | pages [15] -->
m

<!-- b003880 | prose | pages [15] -->
m

<!-- b003881 | prose | pages [15] -->
m

<!-- b003882 | prose | pages [15] -->
m

<!-- b003883 | prose | pages [15] -->
m

<!-- b003884 | prose | pages [15] -->
m

<!-- b003885 | prose | pages [15] -->
m

<!-- b003886 | prose | pages [15] -->
m

<!-- b003887 | prose | pages [15] -->
m

<!-- b003888 | prose | pages [15] -->
m

<!-- b003889 | prose | pages [15] -->
m

<!-- b003890 | prose | pages [15] -->
m

<!-- b003891 | prose | pages [15] -->
m

<!-- b003892 | prose | pages [15] -->
m

<!-- b003893 | prose | pages [15] -->
m

<!-- b003894 | prose | pages [15] -->
m

<!-- b003895 | prose | pages [15] -->
m

<!-- b003896 | prose | pages [15] -->
m

<!-- b003897 | prose | pages [15] -->
m

<!-- b003898 | prose | pages [15] -->
m

<!-- b003899 | prose | pages [15] -->
m

<!-- b003900 | prose | pages [15] -->
m

<!-- b003901 | prose | pages [15] -->
m

<!-- b003902 | prose | pages [15] -->
m

<!-- b003903 | prose | pages [15] -->
m

<!-- b003904 | prose | pages [15] -->
m

<!-- b003905 | prose | pages [15] -->
m

<!-- b003906 | prose | pages [15] -->
m

<!-- b003907 | prose | pages [15] -->
m

<!-- b003908 | prose | pages [15] -->
m

<!-- b003909 | prose | pages [15] -->
m

<!-- b003910 | prose | pages [15] -->
m

<!-- b003911 | prose | pages [15] -->
m

<!-- b003912 | prose | pages [15] -->
m

<!-- b003913 | prose | pages [15] -->
m

<!-- b003914 | prose | pages [15] -->
m

<!-- b003915 | prose | pages [15] -->
m

<!-- b003916 | prose | pages [15] -->
m

<!-- b003917 | prose | pages [15] -->
m

<!-- b003918 | prose | pages [15] -->
m

<!-- b003919 | prose | pages [15] -->
m

<!-- b003920 | prose | pages [15] -->
m

<!-- b003921 | prose | pages [15] -->
m

<!-- b003922 | prose | pages [15] -->
m

<!-- b003923 | prose | pages [15] -->
m

<!-- b003924 | prose | pages [15] -->
m

<!-- b003925 | prose | pages [15] -->
m

<!-- b003926 | prose | pages [15] -->
m

<!-- b003927 | prose | pages [15] -->
m

<!-- b003928 | prose | pages [15] -->
m

<!-- b003929 | prose | pages [15] -->
m

<!-- b003930 | prose | pages [15] -->
m

<!-- b003931 | prose | pages [15] -->
m

<!-- b003932 | prose | pages [15] -->
m

<!-- b003933 | prose | pages [15] -->
m

<!-- b003934 | prose | pages [15] -->
m

<!-- b003935 | prose | pages [15] -->
m

<!-- b003936 | prose | pages [15] -->
m

<!-- b003937 | prose | pages [15] -->
m

<!-- b003938 | prose | pages [15] -->
m

<!-- b003939 | prose | pages [15] -->
m

<!-- b003940 | prose | pages [15] -->
m

<!-- b003941 | prose | pages [15] -->
m

<!-- b003942 | prose | pages [15] -->
m

<!-- b003943 | prose | pages [15] -->
m

<!-- b003944 | prose | pages [15] -->
m

<!-- b003945 | prose | pages [15] -->
m

<!-- b003946 | prose | pages [15] -->
m

<!-- b003947 | prose | pages [15] -->
m

<!-- b003948 | prose | pages [15] -->
m

<!-- b003949 | prose | pages [15] -->
m

<!-- b003950 | prose | pages [15] -->
m

<!-- b003951 | prose | pages [15] -->
m

<!-- b003952 | prose | pages [15] -->
m

<!-- b003953 | prose | pages [15] -->
m

<!-- b003954 | prose | pages [15] -->
m

<!-- b003955 | prose | pages [15] -->
m

<!-- b003956 | prose | pages [15] -->
m

<!-- b003957 | prose | pages [15] -->
m

<!-- b003958 | prose | pages [15] -->
m

<!-- b003959 | prose | pages [15] -->
m

<!-- b003960 | prose | pages [15] -->
m

<!-- b003961 | prose | pages [15] -->
m

<!-- b003962 | prose | pages [15] -->
m

<!-- b003963 | prose | pages [15] -->
m

<!-- b003964 | prose | pages [15] -->
m

<!-- b003965 | prose | pages [15] -->
m

<!-- b003966 | prose | pages [15] -->
m

<!-- b003967 | prose | pages [15] -->
m

<!-- b003968 | prose | pages [15] -->
m

<!-- b003969 | prose | pages [15] -->
m

<!-- b003970 | prose | pages [15] -->
m

<!-- b003971 | prose | pages [15] -->
m

<!-- b003972 | prose | pages [15] -->
m

<!-- b003973 | prose | pages [15] -->
m

<!-- b003974 | prose | pages [15] -->
m

<!-- b003975 | prose | pages [15] -->
m

<!-- b003976 | prose | pages [15] -->
m

<!-- b003977 | prose | pages [15] -->
m

<!-- b003978 | prose | pages [15] -->
m

<!-- b003979 | prose | pages [15] -->
m

<!-- b003980 | prose | pages [15] -->
m

<!-- b003981 | prose | pages [15] -->
m

<!-- b003982 | prose | pages [15] -->
m

<!-- b003983 | prose | pages [15] -->
m

<!-- b003984 | prose | pages [15] -->
m

<!-- b003985 | prose | pages [15] -->
m

<!-- b003986 | prose | pages [15] -->
m

<!-- b003987 | prose | pages [15] -->
m

<!-- b003988 | prose | pages [15] -->
m

<!-- b003989 | prose | pages [15] -->
m

<!-- b003990 | prose | pages [15] -->
m

<!-- b003991 | prose | pages [15] -->
m

<!-- b003992 | prose | pages [15] -->
m

<!-- b003993 | prose | pages [15] -->
m

<!-- b003994 | prose | pages [15] -->
m

<!-- b003995 | prose | pages [15] -->
m

<!-- b003996 | prose | pages [15] -->
m

<!-- b003997 | prose | pages [15] -->
m

<!-- b003998 | prose | pages [15] -->
m

<!-- b003999 | furniture | pages [15] -->
m

<!-- b004000 | furniture | pages [15] -->
m

<!-- b004001 | furniture | pages [15] -->
m

<!-- b004002 | furniture | pages [15] -->
m

<!-- b004003 | furniture | pages [15] -->
m

<!-- b004004 | furniture | pages [15] -->
m

<!-- b004005 | furniture | pages [15] -->
m

<!-- b004006 | furniture | pages [15] -->
m

<!-- b004007 | furniture | pages [15] -->
m

<!-- b004008 | furniture | pages [15] -->
m

<!-- b004009 | furniture | pages [15] -->
m

<!-- b004010 | furniture | pages [15] -->
m

<!-- b004011 | furniture | pages [15] -->
m

<!-- b004012 | furniture | pages [15] -->
m

<!-- b004013 | furniture | pages [15] -->
m

<!-- b004014 | furniture | pages [15] -->
m

<!-- b004015 | furniture | pages [15] -->
m

<!-- b004016 | furniture | pages [15] -->
m

<!-- b004017 | furniture | pages [15] -->
m

<!-- b004018 | furniture | pages [15] -->
m

<!-- b004019 | furniture | pages [15] -->
m

<!-- b004020 | furniture | pages [15] -->
m

<!-- b004021 | furniture | pages [15] -->
m

<!-- b004022 | furniture | pages [15] -->
m

<!-- b004023 | furniture | pages [15] -->
m

<!-- b004024 | furniture | pages [15] -->
m

<!-- b004025 | furniture | pages [15] -->
m

<!-- b004026 | furniture | pages [15] -->
m

<!-- b004027 | furniture | pages [15] -->
m

<!-- b004028 | furniture | pages [15] -->
m

<!-- b004029 | furniture | pages [15] -->
m

<!-- b004030 | furniture | pages [15] -->
m

<!-- b004031 | furniture | pages [15] -->
m

<!-- b004032 | furniture | pages [15] -->
m

<!-- b004033 | furniture | pages [15] -->
m

<!-- b004034 | furniture | pages [15] -->
m

<!-- b004035 | furniture | pages [15] -->
m

<!-- b004036 | furniture | pages [15] -->
m

<!-- b004037 | furniture | pages [15] -->
m

<!-- b004038 | furniture | pages [15] -->
m

<!-- b004039 | furniture | pages [15] -->
m

<!-- b004040 | furniture | pages [15] -->
m

<!-- b004041 | furniture | pages [15] -->
m

<!-- b004042 | furniture | pages [15] -->
m

<!-- b004043 | furniture | pages [15] -->
m

<!-- b004044 | furniture | pages [15] -->
m

<!-- b004045 | furniture | pages [15] -->
m

<!-- b004046 | furniture | pages [15] -->
m

<!-- b004047 | furniture | pages [15] -->
m

<!-- b004048 | furniture | pages [15] -->
m

<!-- b004049 | furniture | pages [15] -->
m

<!-- b004050 | furniture | pages [15] -->
m

<!-- b004051 | furniture | pages [15] -->
m

<!-- b004052 | furniture | pages [15] -->
m

<!-- b004053 | furniture | pages [15] -->
m

<!-- b004054 | furniture | pages [15] -->
m

<!-- b004055 | furniture | pages [15] -->
m

<!-- b004056 | furniture | pages [15] -->
m

<!-- b004057 | furniture | pages [15] -->
m

<!-- b004058 | furniture | pages [15] -->
m

<!-- b004059 | furniture | pages [15] -->
m

<!-- b004060 | furniture | pages [15] -->
m

<!-- b004061 | furniture | pages [15] -->
m

<!-- b004062 | furniture | pages [15] -->
m

<!-- b004063 | furniture | pages [15] -->
m

<!-- b004064 | furniture | pages [15] -->
m

<!-- b004065 | furniture | pages [15] -->
m

<!-- b004066 | furniture | pages [15] -->
m

<!-- b004067 | furniture | pages [15] -->
m

<!-- b004068 | furniture | pages [15] -->
m

<!-- b004069 | furniture | pages [15] -->
m

<!-- b004070 | furniture | pages [15] -->
m

<!-- b004071 | furniture | pages [15] -->
m

<!-- b004072 | furniture | pages [15] -->
m

<!-- b004073 | furniture | pages [15] -->
m

<!-- b004074 | furniture | pages [15] -->
m

<!-- b004075 | furniture | pages [15] -->
m

<!-- b004076 | furniture | pages [15] -->
m

<!-- b004077 | furniture | pages [15] -->
m

<!-- b004078 | furniture | pages [15] -->
m

<!-- b004079 | furniture | pages [15] -->
m

<!-- b004080 | furniture | pages [15] -->
m

<!-- b004081 | furniture | pages [15] -->
m

<!-- b004082 | furniture | pages [15] -->
m

<!-- b004083 | furniture | pages [15] -->
m

<!-- b004084 | furniture | pages [15] -->
m

<!-- b004085 | furniture | pages [15] -->
m

<!-- b004086 | furniture | pages [15] -->
m

<!-- b004087 | furniture | pages [15] -->
m

<!-- b004088 | furniture | pages [15] -->
m

<!-- b004089 | furniture | pages [15] -->
m

<!-- b004090 | furniture | pages [15] -->
m

<!-- b004091 | furniture | pages [15] -->
m

<!-- b004092 | furniture | pages [15] -->
m

<!-- b004093 | furniture | pages [15] -->
m

<!-- b004094 | furniture | pages [15] -->
m

<!-- b004095 | furniture | pages [15] -->
m

<!-- b004096 | furniture | pages [15] -->
m

<!-- b004097 | furniture | pages [15] -->
m

<!-- b004098 | furniture | pages [15] -->
m

<!-- b004099 | furniture | pages [15] -->
m

<!-- b004100 | furniture | pages [15] -->
m

<!-- b004101 | furniture | pages [15] -->
m

<!-- b004102 | furniture | pages [15] -->
m

<!-- b004103 | furniture | pages [15] -->
m

<!-- b004104 | furniture | pages [15] -->
m

<!-- b004105 | furniture | pages [15] -->
m

<!-- b004106 | furniture | pages [15] -->
m

<!-- b004107 | furniture | pages [15] -->
m

<!-- b004108 | furniture | pages [15] -->
m

<!-- b004109 | furniture | pages [15] -->
m

<!-- b004110 | furniture | pages [15] -->
m

<!-- b004111 | furniture | pages [15] -->
m

<!-- b004112 | furniture | pages [15] -->
m

<!-- b004113 | furniture | pages [15] -->
m

<!-- b004114 | furniture | pages [15] -->
m

<!-- b004115 | furniture | pages [15] -->
m

<!-- b004116 | furniture | pages [15] -->
m

<!-- b004117 | furniture | pages [15] -->
m

<!-- b004118 | furniture | pages [15] -->
m

<!-- b004119 | furniture | pages [15] -->
m

<!-- b004120 | furniture | pages [15] -->
m

<!-- b004121 | furniture | pages [15] -->
m

<!-- b004122 | furniture | pages [15] -->
m

<!-- b004123 | furniture | pages [15] -->
m

<!-- b004124 | furniture | pages [15] -->
m

<!-- b004125 | furniture | pages [15] -->
m

<!-- b004126 | furniture | pages [15] -->
m

<!-- b004127 | furniture | pages [15] -->
m

<!-- b004128 | furniture | pages [15] -->
m

<!-- b004129 | furniture | pages [15] -->
m

<!-- b004130 | furniture | pages [15] -->
m

<!-- b004131 | furniture | pages [15] -->
m

<!-- b004132 | furniture | pages [15] -->
m

<!-- b004133 | furniture | pages [15] -->
m

<!-- b004134 | furniture | pages [15] -->
m

<!-- b004135 | furniture | pages [15] -->
m

<!-- b004136 | furniture | pages [15] -->
m

<!-- b004137 | furniture | pages [15] -->
m

<!-- b004138 | furniture | pages [15] -->
m

<!-- b004139 | furniture | pages [15] -->
m

<!-- b004140 | furniture | pages [15] -->
m

<!-- b004141 | furniture | pages [15] -->
m

<!-- b004142 | furniture | pages [15] -->
m

<!-- b004143 | furniture | pages [15] -->
m

<!-- b004144 | furniture | pages [15] -->
m

<!-- b004145 | furniture | pages [15] -->
m

<!-- b004146 | furniture | pages [15] -->
m

<!-- b004147 | furniture | pages [15] -->
m

<!-- b004148 | furniture | pages [15] -->
m

<!-- b004149 | furniture | pages [15] -->
m

<!-- b004150 | furniture | pages [15] -->
m

<!-- b004151 | furniture | pages [15] -->
m

<!-- b004152 | furniture | pages [15] -->
m

<!-- b004153 | furniture | pages [15] -->
m

<!-- b004154 | furniture | pages [15] -->
m

<!-- b004155 | furniture | pages [15] -->
m

<!-- b004156 | furniture | pages [15] -->
m

<!-- b004157 | furniture | pages [15] -->
m

<!-- b004158 | furniture | pages [15] -->
m

<!-- b004159 | furniture | pages [15] -->
m

<!-- b004160 | furniture | pages [15] -->
m

<!-- b004161 | furniture | pages [15] -->
m

<!-- b004162 | furniture | pages [15] -->
m

<!-- b004163 | furniture | pages [15] -->
m

<!-- b004164 | furniture | pages [15] -->
m

<!-- b004165 | furniture | pages [15] -->
m

<!-- b004166 | furniture | pages [15] -->
m

<!-- b004167 | furniture | pages [15] -->
m

<!-- b004168 | furniture | pages [15] -->
m

<!-- b004169 | furniture | pages [15] -->
m

<!-- b004170 | furniture | pages [15] -->
m

<!-- b004171 | furniture | pages [15] -->
m

<!-- b004172 | furniture | pages [15] -->
m

<!-- b004173 | furniture | pages [15] -->
m

<!-- b004174 | furniture | pages [15] -->
m

<!-- b004175 | furniture | pages [15] -->
m

<!-- b004176 | furniture | pages [15] -->
m

<!-- b004177 | furniture | pages [15] -->
m

<!-- b004178 | furniture | pages [15] -->
m

<!-- b004179 | furniture | pages [15] -->
m

<!-- b004180 | furniture | pages [15] -->
m

<!-- b004181 | furniture | pages [15] -->
m

<!-- b004182 | furniture | pages [15] -->
m

<!-- b004183 | furniture | pages [15] -->
m

<!-- b004184 | furniture | pages [15] -->
m

<!-- b004185 | furniture | pages [15] -->
m

<!-- b004186 | furniture | pages [15] -->
m

<!-- b004187 | furniture | pages [15] -->
m

<!-- b004188 | furniture | pages [15] -->
m

<!-- b004189 | furniture | pages [15] -->
m

<!-- b004190 | furniture | pages [15] -->
m

<!-- b004191 | furniture | pages [15] -->
m

<!-- b004192 | furniture | pages [15] -->
m

<!-- b004193 | furniture | pages [15] -->
m

<!-- b004194 | furniture | pages [15] -->
m

<!-- b004195 | furniture | pages [15] -->
m

<!-- b004196 | furniture | pages [15] -->
m

<!-- b004197 | furniture | pages [15] -->
m

<!-- b004198 | furniture | pages [15] -->
m

<!-- b004199 | furniture | pages [15] -->
m

<!-- b004200 | furniture | pages [15] -->
m

<!-- b004201 | furniture | pages [15] -->
m

<!-- b004202 | furniture | pages [15] -->
m

<!-- b004203 | furniture | pages [15] -->
m

<!-- b004204 | furniture | pages [15] -->
m

<!-- b004205 | furniture | pages [15] -->
m

<!-- b004206 | furniture | pages [15] -->
m

<!-- b004207 | furniture | pages [15] -->
m

<!-- b004208 | furniture | pages [15] -->
m

<!-- b004209 | furniture | pages [15] -->
m

<!-- b004210 | furniture | pages [15] -->
m

<!-- b004211 | furniture | pages [15] -->
m

<!-- b004212 | furniture | pages [15] -->
m

<!-- b004213 | furniture | pages [15] -->
m

<!-- b004214 | furniture | pages [15] -->
m

<!-- b004215 | furniture | pages [15] -->
m

<!-- b004216 | furniture | pages [15] -->
m

<!-- b004217 | furniture | pages [15] -->
m

<!-- b004218 | furniture | pages [15] -->
m

<!-- b004219 | furniture | pages [15] -->
m

<!-- b004220 | furniture | pages [15] -->
m

<!-- b004221 | furniture | pages [15] -->
m

<!-- b004222 | furniture | pages [15] -->
m

<!-- b004223 | furniture | pages [15] -->
m

<!-- b004224 | furniture | pages [15] -->
m

<!-- b004225 | furniture | pages [15] -->
m

<!-- b004226 | furniture | pages [15] -->
m

<!-- b004227 | furniture | pages [15] -->
m

<!-- b004228 | furniture | pages [15] -->
m

<!-- b004229 | furniture | pages [15] -->
m

<!-- b004230 | furniture | pages [15] -->
m

<!-- b004231 | furniture | pages [15] -->
m

<!-- b004232 | furniture | pages [15] -->
m

<!-- b004233 | furniture | pages [15] -->
m

<!-- b004234 | furniture | pages [15] -->
m

<!-- b004235 | furniture | pages [15] -->
m

<!-- b004236 | furniture | pages [15] -->
m

<!-- b004237 | furniture | pages [15] -->
m

<!-- b004238 | furniture | pages [15] -->
m

<!-- b004239 | furniture | pages [15] -->
m

<!-- b004240 | furniture | pages [15] -->
m

<!-- b004241 | furniture | pages [15] -->
m

<!-- b004242 | furniture | pages [15] -->
m

<!-- b004243 | furniture | pages [15] -->
m

<!-- b004244 | furniture | pages [15] -->
m

<!-- b004245 | furniture | pages [15] -->
m

<!-- b004246 | furniture | pages [15] -->
m

<!-- b004247 | furniture | pages [15] -->
m

<!-- b004248 | furniture | pages [15] -->
m

<!-- b004249 | furniture | pages [15] -->
m

<!-- b004250 | furniture | pages [15] -->
m

<!-- b004251 | furniture | pages [15] -->
m

<!-- b004252 | furniture | pages [15] -->
m

<!-- b004253 | furniture | pages [15] -->
m

<!-- b004254 | furniture | pages [15] -->
m

<!-- b004255 | furniture | pages [15] -->
m

<!-- b004256 | furniture | pages [15] -->
m

<!-- b004257 | furniture | pages [15] -->
m

<!-- b004258 | furniture | pages [15] -->
m

<!-- b004259 | furniture | pages [15] -->
m

<!-- b004260 | furniture | pages [15] -->
m

<!-- b004261 | furniture | pages [15] -->
m

<!-- b004262 | furniture | pages [15] -->
m

<!-- b004263 | furniture | pages [15] -->
m

<!-- b004264 | furniture | pages [15] -->
m

<!-- b004265 | furniture | pages [15] -->
m

<!-- b004266 | furniture | pages [15] -->
m

<!-- b004267 | furniture | pages [15] -->
m

<!-- b004268 | furniture | pages [15] -->
m

<!-- b004269 | furniture | pages [15] -->
m

<!-- b004270 | furniture | pages [15] -->
m

<!-- b004271 | furniture | pages [15] -->
m

<!-- b004272 | furniture | pages [15] -->
m

<!-- b004273 | furniture | pages [15] -->
m

<!-- b004274 | furniture | pages [15] -->
m

<!-- b004275 | furniture | pages [15] -->
m

<!-- b004276 | furniture | pages [15] -->
m

<!-- b004277 | furniture | pages [15] -->
m

<!-- b004278 | furniture | pages [15] -->
m

<!-- b004279 | furniture | pages [15] -->
m

<!-- b004280 | furniture | pages [15] -->
m

<!-- b004281 | furniture | pages [15] -->
m

<!-- b004282 | furniture | pages [15] -->
m

<!-- b004283 | furniture | pages [15] -->
m

<!-- b004284 | furniture | pages [15] -->
m

<!-- b004285 | furniture | pages [15] -->
m

<!-- b004286 | furniture | pages [15] -->
m

<!-- b004287 | furniture | pages [15] -->
m

<!-- b004288 | furniture | pages [15] -->
m

<!-- b004289 | furniture | pages [15] -->
m

<!-- b004290 | furniture | pages [15] -->
m

<!-- b004291 | furniture | pages [15] -->
m

<!-- b004292 | furniture | pages [15] -->
m

<!-- b004293 | furniture | pages [15] -->
m

<!-- b004294 | furniture | pages [15] -->
m

<!-- b004295 | furniture | pages [15] -->
m

<!-- b004296 | furniture | pages [15] -->
m

<!-- b004297 | furniture | pages [15] -->
m

<!-- b004298 | furniture | pages [15] -->
m

<!-- b004299 | furniture | pages [15] -->
m

<!-- b004300 | furniture | pages [15] -->
m

<!-- b004301 | furniture | pages [15] -->
m

<!-- b004302 | furniture | pages [15] -->
m

<!-- b004303 | furniture | pages [15] -->
m

<!-- b004304 | furniture | pages [15] -->
m

<!-- b004305 | furniture | pages [15] -->
m

<!-- b004306 | furniture | pages [15] -->
m

<!-- b004307 | furniture | pages [15] -->
m

<!-- b004308 | furniture | pages [15] -->
m

<!-- b004309 | furniture | pages [15] -->
m

<!-- b004310 | furniture | pages [15] -->
m

<!-- b004311 | furniture | pages [15] -->
m

<!-- b004312 | furniture | pages [15] -->
m

<!-- b004313 | furniture | pages [15] -->
m

<!-- b004314 | furniture | pages [15] -->
m

<!-- b004315 | furniture | pages [15] -->
m

<!-- b004316 | furniture | pages [15] -->
m

<!-- b004317 | furniture | pages [15] -->
m

<!-- b004318 | furniture | pages [15] -->
m

<!-- b004319 | furniture | pages [15] -->
m

<!-- b004320 | furniture | pages [15] -->
m

<!-- b004321 | furniture | pages [15] -->
m

<!-- b004322 | furniture | pages [15] -->
m

<!-- b004323 | furniture | pages [15] -->
m

<!-- b004324 | furniture | pages [15] -->
m

<!-- b004325 | furniture | pages [15] -->
m

<!-- b004326 | furniture | pages [15] -->
m

<!-- b004327 | furniture | pages [15] -->
m

<!-- b004328 | furniture | pages [15] -->
m

<!-- b004329 | furniture | pages [15] -->
m

<!-- b004330 | furniture | pages [15] -->
m

<!-- b004331 | furniture | pages [15] -->
m

<!-- b004332 | furniture | pages [15] -->
m

<!-- b004333 | furniture | pages [15] -->
m

<!-- b004334 | furniture | pages [15] -->
m

<!-- b004335 | furniture | pages [15] -->
m

<!-- b004336 | furniture | pages [15] -->
m

<!-- b004337 | furniture | pages [15] -->
m

<!-- b004338 | furniture | pages [15] -->
m

<!-- b004339 | furniture | pages [15] -->
m

<!-- b004340 | furniture | pages [15] -->
m

<!-- b004341 | furniture | pages [15] -->
m

<!-- b004342 | furniture | pages [15] -->
m

<!-- b004343 | furniture | pages [15] -->
m

<!-- b004344 | furniture | pages [15] -->
m

<!-- b004345 | furniture | pages [15] -->
m

<!-- b004346 | furniture | pages [15] -->
m

<!-- b004347 | furniture | pages [15] -->
m

<!-- b004348 | furniture | pages [15] -->
m

<!-- b004349 | furniture | pages [15] -->
m

<!-- b004350 | furniture | pages [15] -->
m

<!-- b004351 | furniture | pages [15] -->
m

<!-- b004352 | furniture | pages [15] -->
m

<!-- b004353 | furniture | pages [15] -->
m

<!-- b004354 | furniture | pages [15] -->
m

<!-- b004355 | furniture | pages [15] -->
m

<!-- b004356 | furniture | pages [15] -->
m

<!-- b004357 | furniture | pages [15] -->
m

<!-- b004358 | furniture | pages [15] -->
m

<!-- b004359 | furniture | pages [15] -->
m

<!-- b004360 | furniture | pages [15] -->
m

<!-- b004361 | furniture | pages [15] -->
m

<!-- b004362 | furniture | pages [15] -->
m

<!-- b004363 | furniture | pages [15] -->
m

<!-- b004364 | furniture | pages [15] -->
m

<!-- b004365 | furniture | pages [15] -->
m

<!-- b004366 | furniture | pages [15] -->
m

<!-- b004367 | furniture | pages [15] -->
m

<!-- b004368 | furniture | pages [15] -->
m

<!-- b004369 | furniture | pages [15] -->
m

<!-- b004370 | furniture | pages [15] -->
m

<!-- b004371 | furniture | pages [15] -->
m

<!-- b004372 | furniture | pages [15] -->
m

<!-- b004373 | furniture | pages [15] -->
m

<!-- b004374 | furniture | pages [15] -->
m

<!-- b004375 | furniture | pages [15] -->
m

<!-- b004376 | furniture | pages [15] -->
m

<!-- b004377 | furniture | pages [15] -->
m

<!-- b004378 | furniture | pages [15] -->
m

<!-- b004379 | furniture | pages [15] -->
m

<!-- b004380 | furniture | pages [15] -->
m

<!-- b004381 | furniture | pages [15] -->
m

<!-- b004382 | furniture | pages [15] -->
m

<!-- b004383 | furniture | pages [15] -->
m

<!-- b004384 | furniture | pages [15] -->
m

<!-- b004385 | furniture | pages [15] -->
m

<!-- b004386 | furniture | pages [15] -->
m

<!-- b004387 | furniture | pages [15] -->
m

<!-- b004388 | furniture | pages [15] -->
m

<!-- b004389 | furniture | pages [15] -->
m

<!-- b004390 | furniture | pages [15] -->
m

<!-- b004391 | furniture | pages [15] -->
m

<!-- b004392 | furniture | pages [15] -->
m

<!-- b004393 | furniture | pages [15] -->
m

<!-- b004394 | furniture | pages [15] -->
m

<!-- b004395 | furniture | pages [15] -->
m

<!-- b004396 | furniture | pages [15] -->
m

<!-- b004397 | furniture | pages [15] -->
m

<!-- b004398 | furniture | pages [15] -->
m

<!-- b004399 | furniture | pages [15] -->
m

<!-- b004400 | furniture | pages [15] -->
m

<!-- b004401 | furniture | pages [15] -->
m

<!-- b004402 | furniture | pages [16] -->
m

<!-- b004403 | furniture | pages [16] -->
m

<!-- b004404 | furniture | pages [16] -->
m

<!-- b004405 | furniture | pages [16] -->
m

<!-- b004406 | furniture | pages [16] -->
m

<!-- b004407 | furniture | pages [16] -->
m

<!-- b004408 | furniture | pages [16] -->
m

<!-- b004409 | furniture | pages [16] -->
m

<!-- b004410 | furniture | pages [16] -->
m

<!-- b004411 | furniture | pages [16] -->
m

<!-- b004412 | furniture | pages [16] -->
m

<!-- b004413 | furniture | pages [16] -->
m

<!-- b004414 | furniture | pages [16] -->
m

<!-- b004415 | furniture | pages [16] -->
m

<!-- b004416 | furniture | pages [16] -->
m

<!-- b004417 | furniture | pages [16] -->
m

<!-- b004418 | furniture | pages [16] -->
m

<!-- b004419 | furniture | pages [16] -->
m

<!-- b004420 | furniture | pages [16] -->
m

<!-- b004421 | furniture | pages [16] -->
m

<!-- b004422 | furniture | pages [16] -->
m

<!-- b004423 | furniture | pages [16] -->
m

<!-- b004424 | furniture | pages [16] -->
m

<!-- b004425 | furniture | pages [16] -->
m

<!-- b004426 | furniture | pages [16] -->
m

<!-- b004427 | furniture | pages [16] -->
m

<!-- b004428 | furniture | pages [16] -->
m

<!-- b004429 | furniture | pages [16] -->
m

<!-- b004430 | furniture | pages [16] -->
m

<!-- b004431 | furniture | pages [16] -->
m

<!-- b004432 | furniture | pages [16] -->
m

<!-- b004433 | furniture | pages [16] -->
m

<!-- b004434 | furniture | pages [16] -->
m

<!-- b004435 | furniture | pages [16] -->
m

<!-- b004436 | furniture | pages [16] -->
m

<!-- b004437 | furniture | pages [16] -->
m

<!-- b004438 | furniture | pages [16] -->
m

<!-- b004439 | furniture | pages [16] -->
m

<!-- b004440 | furniture | pages [16] -->
m

<!-- b004441 | furniture | pages [16] -->
m

<!-- b004442 | furniture | pages [16] -->
m

<!-- b004443 | furniture | pages [16] -->
m

<!-- b004444 | furniture | pages [16] -->
m

<!-- b004445 | furniture | pages [16] -->
m

<!-- b004446 | furniture | pages [16] -->
m

<!-- b004447 | furniture | pages [16] -->
m

<!-- b004448 | furniture | pages [16] -->
m

<!-- b004449 | furniture | pages [16] -->
m

<!-- b004450 | furniture | pages [16] -->
m

<!-- b004451 | furniture | pages [16] -->
m

<!-- b004452 | furniture | pages [16] -->
m

<!-- b004453 | furniture | pages [16] -->
m

<!-- b004454 | furniture | pages [16] -->
m

<!-- b004455 | furniture | pages [16] -->
Team # 2500759

<!-- b004456 | furniture | pages [16] -->
m

<!-- b004457 | furniture | pages [16] -->
m

<!-- b004458 | furniture | pages [16] -->
m

<!-- b004459 | furniture | pages [16] -->
m

<!-- b004460 | furniture | pages [16] -->
m

<!-- b004461 | furniture | pages [16] -->
m

<!-- b004462 | furniture | pages [16] -->
m

<!-- b004463 | furniture | pages [16] -->
m

<!-- b004464 | furniture | pages [16] -->
m

<!-- b004465 | furniture | pages [16] -->
m

<!-- b004466 | furniture | pages [16] -->
m

<!-- b004467 | furniture | pages [16] -->
m

<!-- b004468 | furniture | pages [16] -->
m

<!-- b004469 | furniture | pages [16] -->
m

<!-- b004470 | furniture | pages [16] -->
m

<!-- b004471 | furniture | pages [16] -->
m

<!-- b004472 | furniture | pages [16] -->
m

<!-- b004473 | furniture | pages [16] -->
m

<!-- b004474 | furniture | pages [16] -->
m

<!-- b004475 | furniture | pages [16] -->
m

<!-- b004476 | furniture | pages [16] -->
m

<!-- b004477 | furniture | pages [16] -->
m

<!-- b004478 | furniture | pages [16] -->
m

<!-- b004479 | furniture | pages [16] -->
m

<!-- b004480 | furniture | pages [16] -->
m

<!-- b004481 | furniture | pages [16] -->
m

<!-- b004482 | furniture | pages [16] -->
m

<!-- b004483 | furniture | pages [16] -->
m

<!-- b004484 | furniture | pages [16] -->
m

<!-- b004485 | furniture | pages [16] -->
m

<!-- b004486 | furniture | pages [16] -->
m

<!-- b004487 | furniture | pages [16] -->
m

<!-- b004488 | furniture | pages [16] -->
m

<!-- b004489 | furniture | pages [16] -->
m

<!-- b004490 | furniture | pages [16] -->
m

<!-- b004491 | furniture | pages [16] -->
m

<!-- b004492 | furniture | pages [16] -->
m

<!-- b004493 | furniture | pages [16] -->
m

<!-- b004494 | furniture | pages [16] -->
m

<!-- b004495 | furniture | pages [16] -->
m

<!-- b004496 | furniture | pages [16] -->
m

<!-- b004497 | furniture | pages [16] -->
m

<!-- b004498 | furniture | pages [16] -->
m

<!-- b004499 | furniture | pages [16] -->
m

<!-- b004500 | furniture | pages [16] -->
m

<!-- b004501 | furniture | pages [16] -->
m

<!-- b004502 | furniture | pages [16] -->
m

<!-- b004503 | furniture | pages [16] -->
m

<!-- b004504 | furniture | pages [16] -->
m

<!-- b004505 | furniture | pages [16] -->
m

<!-- b004506 | furniture | pages [16] -->
m

<!-- b004507 | furniture | pages [16] -->
m

<!-- b004508 | furniture | pages [16] -->
m

<!-- b004509 | furniture | pages [16] -->
m

<!-- b004510 | furniture | pages [16] -->
m

<!-- b004511 | furniture | pages [16] -->
m

<!-- b004512 | furniture | pages [16] -->
m

<!-- b004513 | furniture | pages [16] -->
m

<!-- b004514 | furniture | pages [16] -->
m

<!-- b004515 | furniture | pages [16] -->
m

<!-- b004516 | furniture | pages [16] -->
m

<!-- b004517 | furniture | pages [16] -->
m

<!-- b004518 | furniture | pages [16] -->
m

<!-- b004519 | furniture | pages [16] -->
m

<!-- b004520 | furniture | pages [16] -->
m

<!-- b004521 | furniture | pages [16] -->
m

<!-- b004522 | furniture | pages [16] -->
m

<!-- b004523 | furniture | pages [16] -->
m

<!-- b004524 | furniture | pages [16] -->
m

<!-- b004525 | furniture | pages [16] -->
m

<!-- b004526 | furniture | pages [16] -->
m

<!-- b004527 | furniture | pages [16] -->
m

<!-- b004528 | furniture | pages [16] -->
m

<!-- b004529 | furniture | pages [16] -->
m

<!-- b004530 | furniture | pages [16] -->
m

<!-- b004531 | furniture | pages [16] -->
m

<!-- b004532 | furniture | pages [16] -->
m

<!-- b004533 | furniture | pages [16] -->
m

<!-- b004534 | furniture | pages [16] -->
m

<!-- b004535 | furniture | pages [16] -->
m

<!-- b004536 | furniture | pages [16] -->
m

<!-- b004537 | furniture | pages [16] -->
m

<!-- b004538 | furniture | pages [16] -->
m

<!-- b004539 | furniture | pages [16] -->
m

<!-- b004540 | furniture | pages [16] -->
m

<!-- b004541 | furniture | pages [16] -->
m

<!-- b004542 | furniture | pages [16] -->
m

<!-- b004543 | furniture | pages [16] -->
m

<!-- b004544 | furniture | pages [16] -->
m

<!-- b004545 | furniture | pages [16] -->
m

<!-- b004546 | furniture | pages [16] -->
m

<!-- b004547 | furniture | pages [16] -->
m

<!-- b004548 | furniture | pages [16] -->
m

<!-- b004549 | furniture | pages [16] -->
m

<!-- b004550 | furniture | pages [16] -->
m

<!-- b004551 | furniture | pages [16] -->
m

<!-- b004552 | furniture | pages [16] -->
m

<!-- b004553 | furniture | pages [16] -->
m

<!-- b004554 | furniture | pages [16] -->
m

<!-- b004555 | furniture | pages [16] -->
m

<!-- b004556 | furniture | pages [16] -->
m

<!-- b004557 | furniture | pages [16] -->
m

<!-- b004558 | furniture | pages [16] -->
m

<!-- b004559 | furniture | pages [16] -->
m

<!-- b004560 | furniture | pages [16] -->
m

<!-- b004561 | furniture | pages [16] -->
m

<!-- b004562 | furniture | pages [16] -->
m

<!-- b004563 | furniture | pages [16] -->
m

<!-- b004564 | furniture | pages [16] -->
m

<!-- b004565 | furniture | pages [16] -->
m

<!-- b004566 | furniture | pages [16] -->
m

<!-- b004567 | furniture | pages [16] -->
m

<!-- b004568 | furniture | pages [16] -->
m

<!-- b004569 | furniture | pages [16] -->
m

<!-- b004570 | furniture | pages [16] -->
m

<!-- b004571 | furniture | pages [16] -->
m

<!-- b004572 | furniture | pages [16] -->
m

<!-- b004573 | furniture | pages [16] -->
m

<!-- b004574 | furniture | pages [16] -->
m

<!-- b004575 | furniture | pages [16] -->
m

<!-- b004576 | furniture | pages [16] -->
m

<!-- b004577 | furniture | pages [16] -->
m

<!-- b004578 | furniture | pages [16] -->
m

<!-- b004579 | furniture | pages [16] -->
m

<!-- b004580 | furniture | pages [16] -->
m

<!-- b004581 | furniture | pages [16] -->
m

<!-- b004582 | furniture | pages [16] -->
m

<!-- b004583 | furniture | pages [16] -->
m

<!-- b004584 | furniture | pages [16] -->
m

<!-- b004585 | furniture | pages [16] -->
m

<!-- b004586 | furniture | pages [16] -->
m

<!-- b004587 | furniture | pages [16] -->
m

<!-- b004588 | furniture | pages [16] -->
m

<!-- b004589 | furniture | pages [16] -->
m

<!-- b004590 | furniture | pages [16] -->
m

<!-- b004591 | furniture | pages [16] -->
m

<!-- b004592 | furniture | pages [16] -->
m

<!-- b004593 | furniture | pages [16] -->
m

<!-- b004594 | furniture | pages [16] -->
m

<!-- b004595 | furniture | pages [16] -->
m

<!-- b004596 | furniture | pages [16] -->
m

<!-- b004597 | furniture | pages [16] -->
m

<!-- b004598 | furniture | pages [16] -->
m

<!-- b004599 | furniture | pages [16] -->
m

<!-- b004600 | furniture | pages [16] -->
m

<!-- b004601 | furniture | pages [16] -->
m

<!-- b004602 | furniture | pages [16] -->
m

<!-- b004603 | furniture | pages [16] -->
m

<!-- b004604 | furniture | pages [16] -->
m

<!-- b004605 | furniture | pages [16] -->
m

<!-- b004606 | furniture | pages [16] -->
m

<!-- b004607 | furniture | pages [16] -->
m

<!-- b004608 | furniture | pages [16] -->
m

<!-- b004609 | furniture | pages [16] -->
m

<!-- b004610 | furniture | pages [16] -->
m

<!-- b004611 | furniture | pages [16] -->
m

<!-- b004612 | furniture | pages [16] -->
m

<!-- b004613 | furniture | pages [16] -->
m

<!-- b004614 | furniture | pages [16] -->
m

<!-- b004615 | furniture | pages [16] -->
m

<!-- b004616 | furniture | pages [16] -->
m

<!-- b004617 | furniture | pages [16] -->
m

<!-- b004618 | furniture | pages [16] -->
m

<!-- b004619 | furniture | pages [16] -->
m

<!-- b004620 | furniture | pages [16] -->
m

<!-- b004621 | furniture | pages [16] -->
m

<!-- b004622 | furniture | pages [16] -->
m

<!-- b004623 | furniture | pages [16] -->
m

<!-- b004624 | furniture | pages [16] -->
m

<!-- b004625 | furniture | pages [16] -->
m

<!-- b004626 | furniture | pages [16] -->
m

<!-- b004627 | furniture | pages [16] -->
m

<!-- b004628 | furniture | pages [16] -->
m

<!-- b004629 | furniture | pages [16] -->
m

<!-- b004630 | furniture | pages [16] -->
m

<!-- b004631 | furniture | pages [16] -->
m

<!-- b004632 | furniture | pages [16] -->
m

<!-- b004633 | furniture | pages [16] -->
m

<!-- b004634 | furniture | pages [16] -->
m

<!-- b004635 | furniture | pages [16] -->
m

<!-- b004636 | furniture | pages [16] -->
m

<!-- b004637 | furniture | pages [16] -->
m

<!-- b004638 | furniture | pages [16] -->
m

<!-- b004639 | furniture | pages [16] -->
m

<!-- b004640 | furniture | pages [16] -->
m

<!-- b004641 | furniture | pages [16] -->
m

<!-- b004642 | furniture | pages [16] -->
m

<!-- b004643 | furniture | pages [16] -->
m

<!-- b004644 | furniture | pages [16] -->
m

<!-- b004645 | furniture | pages [16] -->
m

<!-- b004646 | furniture | pages [16] -->
m

<!-- b004647 | furniture | pages [16] -->
m

<!-- b004648 | furniture | pages [16] -->
m

<!-- b004649 | furniture | pages [16] -->
m

<!-- b004650 | furniture | pages [16] -->
m

<!-- b004651 | furniture | pages [16] -->
m

<!-- b004652 | furniture | pages [16] -->
m

<!-- b004653 | furniture | pages [16] -->
m

<!-- b004654 | furniture | pages [16] -->
m

<!-- b004655 | furniture | pages [16] -->
m

<!-- b004656 | furniture | pages [16] -->
m

<!-- b004657 | furniture | pages [16] -->
m

<!-- b004658 | furniture | pages [16] -->
m

<!-- b004659 | furniture | pages [16] -->
m

<!-- b004660 | furniture | pages [16] -->
m

<!-- b004661 | furniture | pages [16] -->
m

<!-- b004662 | furniture | pages [16] -->
m

<!-- b004663 | furniture | pages [16] -->
m

<!-- b004664 | furniture | pages [16] -->
m

<!-- b004665 | furniture | pages [16] -->
m

<!-- b004666 | furniture | pages [16] -->
m

<!-- b004667 | furniture | pages [16] -->
m

<!-- b004668 | furniture | pages [16] -->
m

<!-- b004669 | furniture | pages [16] -->
m

<!-- b004670 | furniture | pages [16] -->
m

<!-- b004671 | furniture | pages [16] -->
m

<!-- b004672 | furniture | pages [16] -->
m

<!-- b004673 | furniture | pages [16] -->
m

<!-- b004674 | furniture | pages [16] -->
m

<!-- b004675 | furniture | pages [16] -->
m

<!-- b004676 | furniture | pages [16] -->
m

<!-- b004677 | furniture | pages [16] -->
m

<!-- b004678 | furniture | pages [16] -->
m

<!-- b004679 | furniture | pages [16] -->
m

<!-- b004680 | furniture | pages [16] -->
m

<!-- b004681 | furniture | pages [16] -->
m

<!-- b004682 | furniture | pages [16] -->
m

<!-- b004683 | furniture | pages [16] -->
m

<!-- b004684 | furniture | pages [16] -->
m

<!-- b004685 | furniture | pages [16] -->
m

<!-- b004686 | furniture | pages [16] -->
m

<!-- b004687 | furniture | pages [16] -->
m

<!-- b004688 | furniture | pages [16] -->
m

<!-- b004689 | furniture | pages [16] -->
m

<!-- b004690 | furniture | pages [16] -->
m

<!-- b004691 | furniture | pages [16] -->
m

<!-- b004692 | furniture | pages [16] -->
m

<!-- b004693 | furniture | pages [16] -->
m

<!-- b004694 | furniture | pages [16] -->
m

<!-- b004695 | furniture | pages [16] -->
m

<!-- b004696 | furniture | pages [16] -->
m

<!-- b004697 | furniture | pages [16] -->
m

<!-- b004698 | furniture | pages [16] -->
m

<!-- b004699 | furniture | pages [16] -->
m

<!-- b004700 | furniture | pages [16] -->
m

<!-- b004701 | furniture | pages [16] -->
m

<!-- b004702 | furniture | pages [16] -->
m

<!-- b004703 | furniture | pages [16] -->
m

<!-- b004704 | furniture | pages [16] -->
m

<!-- b004705 | furniture | pages [16] -->
m

<!-- b004706 | furniture | pages [16] -->
m

<!-- b004707 | furniture | pages [16] -->
m

<!-- b004708 | furniture | pages [16] -->
m

<!-- b004709 | furniture | pages [16] -->
m

<!-- b004710 | furniture | pages [16] -->
m

<!-- b004711 | furniture | pages [16] -->
m

<!-- b004712 | furniture | pages [16] -->
m

<!-- b004713 | furniture | pages [16] -->
m

<!-- b004714 | furniture | pages [16] -->
m

<!-- b004715 | furniture | pages [16] -->
m

<!-- b004716 | furniture | pages [16] -->
m

<!-- b004717 | furniture | pages [16] -->
m

<!-- b004718 | furniture | pages [16] -->
m

<!-- b004719 | furniture | pages [16] -->
m

<!-- b004720 | furniture | pages [16] -->
m

<!-- b004721 | furniture | pages [16] -->
m

<!-- b004722 | furniture | pages [16] -->
m

<!-- b004723 | furniture | pages [16] -->
m

<!-- b004724 | furniture | pages [16] -->
m

<!-- b004725 | furniture | pages [16] -->
m

<!-- b004726 | furniture | pages [16] -->
m

<!-- b004727 | furniture | pages [16] -->
m

<!-- b004728 | furniture | pages [16] -->
m

<!-- b004729 | furniture | pages [16] -->
m

<!-- b004730 | furniture | pages [16] -->
m

<!-- b004731 | furniture | pages [16] -->
m

<!-- b004732 | furniture | pages [16] -->
m

<!-- b004733 | furniture | pages [16] -->
m

<!-- b004734 | furniture | pages [16] -->
m

<!-- b004735 | prose | pages [16] -->
m

<!-- b004736 | prose | pages [16] -->
m

<!-- b004737 | prose | pages [16] -->
m

<!-- b004738 | prose | pages [16] -->
m

<!-- b004739 | prose | pages [16] -->
m

<!-- b004740 | prose | pages [16] -->
m

<!-- b004741 | prose | pages [16] -->
m

<!-- b004742 | prose | pages [16] -->
m

<!-- b004743 | prose | pages [16] -->
m

<!-- b004744 | prose | pages [16] -->
m

<!-- b004745 | prose | pages [16] -->
m

<!-- b004746 | prose | pages [16] -->
m

<!-- b004747 | prose | pages [16] -->
m

<!-- b004748 | prose | pages [16] -->
m

<!-- b004749 | prose | pages [16] -->
m

<!-- b004750 | prose | pages [16] -->
m

<!-- b004751 | prose | pages [16] -->
m

<!-- b004752 | prose | pages [16] -->
m

<!-- b004753 | prose | pages [16] -->
m

<!-- b004754 | prose | pages [16] -->
m

<!-- b004755 | prose | pages [16] -->
m

<!-- b004756 | prose | pages [16] -->
m

<!-- b004757 | prose | pages [16] -->
m

<!-- b004758 | prose | pages [16] -->
m

<!-- b004759 | prose | pages [16] -->
m

<!-- b004760 | prose | pages [16] -->
m

<!-- b004761 | prose | pages [16] -->
m

<!-- b004762 | prose | pages [16] -->
m

<!-- b004763 | prose | pages [16] -->
m

<!-- b004764 | prose | pages [16] -->
m

<!-- b004765 | prose | pages [16] -->
m

<!-- b004766 | prose | pages [16] -->
m

<!-- b004767 | prose | pages [16] -->
m

<!-- b004768 | prose | pages [16] -->
m

<!-- b004769 | prose | pages [16] -->
m

<!-- b004770 | prose | pages [16] -->
m

<!-- b004771 | prose | pages [16] -->
m

<!-- b004772 | prose | pages [16] -->
m

<!-- b004773 | prose | pages [16] -->
m

<!-- b004774 | prose | pages [16] -->
m

<!-- b004775 | prose | pages [16] -->
m

<!-- b004776 | prose | pages [16] -->
m

<!-- b004777 | prose | pages [16] -->
m

<!-- b004778 | prose | pages [16] -->
m

<!-- b004779 | prose | pages [16] -->
m

<!-- b004780 | prose | pages [16] -->
m

<!-- b004781 | prose | pages [16] -->
m

<!-- b004782 | prose | pages [16] -->
m

<!-- b004783 | prose | pages [16] -->
m

<!-- b004784 | prose | pages [16] -->
m

<!-- b004785 | prose | pages [16] -->
m

<!-- b004786 | prose | pages [16] -->
m

<!-- b004787 | prose | pages [16] -->
m

<!-- b004788 | prose | pages [16] -->
m

<!-- b004789 | prose | pages [16] -->
m

<!-- b004790 | prose | pages [16] -->
m

<!-- b004791 | prose | pages [16] -->
m

<!-- b004792 | prose | pages [16] -->
m

<!-- b004793 | prose | pages [16] -->
m

<!-- b004794 | prose | pages [16] -->
m

<!-- b004795 | prose | pages [16] -->
m

<!-- b004796 | prose | pages [16] -->
m

<!-- b004797 | prose | pages [16] -->
m

<!-- b004798 | prose | pages [16] -->
m

<!-- b004799 | prose | pages [16] -->
m

<!-- b004800 | prose | pages [16] -->
m

<!-- b004801 | prose | pages [16] -->
m

<!-- b004802 | prose | pages [16] -->
m

<!-- b004803 | prose | pages [16] -->
m

<!-- b004804 | prose | pages [16] -->
m

<!-- b004805 | prose | pages [16] -->
m

<!-- b004806 | prose | pages [16] -->
m

<!-- b004807 | prose | pages [16] -->
m

<!-- b004808 | prose | pages [16] -->
m

<!-- b004809 | prose | pages [16] -->
m

<!-- b004810 | prose | pages [16] -->
m

<!-- b004811 | prose | pages [16] -->
m

<!-- b004812 | prose | pages [16] -->
m

<!-- b004813 | prose | pages [16] -->
m

<!-- b004814 | prose | pages [16] -->
m

<!-- b004815 | prose | pages [16] -->
m

<!-- b004816 | prose | pages [16] -->
m

<!-- b004817 | prose | pages [16] -->
m

<!-- b004818 | prose | pages [16] -->
m

<!-- b004819 | prose | pages [16] -->
m

<!-- b004820 | prose | pages [16] -->
m

<!-- b004821 | prose | pages [16] -->
m

<!-- b004822 | prose | pages [16] -->
m

<!-- b004823 | prose | pages [16] -->
m

<!-- b004824 | prose | pages [16] -->
m

<!-- b004825 | prose | pages [16] -->
m

<!-- b004826 | prose | pages [16] -->
m

<!-- b004827 | prose | pages [16] -->
m

<!-- b004828 | prose | pages [16] -->
m

<!-- b004829 | prose | pages [16] -->
m

<!-- b004830 | prose | pages [16] -->
m

<!-- b004831 | prose | pages [16] -->
m

<!-- b004832 | prose | pages [16] -->
m

<!-- b004833 | prose | pages [16] -->
m

<!-- b004834 | prose | pages [16] -->
m

<!-- b004835 | prose | pages [16] -->
m

<!-- b004836 | prose | pages [16] -->
m

<!-- b004837 | prose | pages [16] -->
m

<!-- b004838 | prose | pages [16] -->
m

<!-- b004839 | prose | pages [16] -->
m

<!-- b004840 | prose | pages [16] -->
m

<!-- b004841 | prose | pages [16] -->
m

<!-- b004842 | prose | pages [16] -->
m

<!-- b004843 | prose | pages [16] -->
m

<!-- b004844 | prose | pages [16] -->
m

<!-- b004845 | prose | pages [16] -->
m

<!-- b004846 | prose | pages [16] -->
m

<!-- b004847 | prose | pages [16] -->
m

<!-- b004848 | prose | pages [16] -->
m

<!-- b004849 | prose | pages [16] -->
m

<!-- b004850 | prose | pages [16] -->
m

<!-- b004851 | prose | pages [16] -->
m

<!-- b004852 | prose | pages [16] -->
m

<!-- b004853 | prose | pages [16] -->
m

<!-- b004854 | prose | pages [16] -->
m

<!-- b004855 | prose | pages [16] -->
m

<!-- b004856 | prose | pages [16] -->
m

<!-- b004857 | prose | pages [16] -->
m

<!-- b004858 | prose | pages [16] -->
m

<!-- b004859 | prose | pages [16] -->
m

<!-- b004860 | prose | pages [16] -->
m

<!-- b004861 | prose | pages [16] -->
m

<!-- b004862 | prose | pages [16] -->
m

<!-- b004863 | prose | pages [16] -->
m

<!-- b004864 | prose | pages [16] -->
m

<!-- b004865 | prose | pages [16] -->
m

<!-- b004866 | prose | pages [16] -->
m

<!-- b004867 | prose | pages [16] -->
m

<!-- b004868 | prose | pages [16] -->
m

<!-- b004869 | prose | pages [16] -->
m

<!-- b004870 | prose | pages [16] -->
m

<!-- b004871 | prose | pages [16] -->
m

<!-- b004872 | prose | pages [16] -->
m

<!-- b004873 | prose | pages [16] -->
m

<!-- b004874 | prose | pages [16] -->
m

<!-- b004875 | prose | pages [16] -->
m

<!-- b004876 | prose | pages [16] -->
m

<!-- b004877 | prose | pages [16] -->
m

<!-- b004878 | prose | pages [16] -->
m

<!-- b004879 | prose | pages [16] -->
m

<!-- b004880 | prose | pages [16] -->
m

<!-- b004881 | prose | pages [16] -->
m

<!-- b004882 | prose | pages [16] -->
m

<!-- b004883 | prose | pages [16] -->
m

<!-- b004884 | prose | pages [16] -->
m

<!-- b004885 | prose | pages [16] -->
m

<!-- b004886 | prose | pages [16] -->
m

<!-- b004887 | prose | pages [16] -->
m

<!-- b004888 | prose | pages [16] -->
m

<!-- b004889 | prose | pages [16] -->
m

<!-- b004890 | prose | pages [16] -->
m

<!-- b004891 | prose | pages [16] -->
m

<!-- b004892 | prose | pages [16] -->
m

<!-- b004893 | prose | pages [16] -->
m

<!-- b004894 | prose | pages [16] -->
m

<!-- b004895 | prose | pages [16] -->
m

<!-- b004896 | prose | pages [16] -->
m

<!-- b004897 | prose | pages [16] -->
m

<!-- b004898 | prose | pages [16] -->
m

<!-- b004899 | prose | pages [16] -->
m

<!-- b004900 | prose | pages [16] -->
m

<!-- b004901 | prose | pages [16] -->
m

<!-- b004902 | prose | pages [16] -->
m

<!-- b004903 | prose | pages [16] -->
m

<!-- b004904 | prose | pages [16] -->
m

<!-- b004905 | prose | pages [16] -->
m

<!-- b004906 | prose | pages [16] -->
m

<!-- b004907 | prose | pages [16] -->
m

<!-- b004908 | prose | pages [16] -->
m

<!-- b004909 | prose | pages [16] -->
m

<!-- b004910 | prose | pages [16] -->
m

<!-- b004911 | prose | pages [16] -->
m

<!-- b004912 | prose | pages [16] -->
m

<!-- b004913 | prose | pages [16] -->
m

<!-- b004914 | prose | pages [16] -->
m

<!-- b004915 | prose | pages [16] -->
m

<!-- b004916 | prose | pages [16] -->
m

<!-- b004917 | prose | pages [16] -->
m

<!-- b004918 | prose | pages [16] -->
m

<!-- b004919 | prose | pages [16] -->
m

<!-- b004920 | prose | pages [16] -->
m

<!-- b004921 | prose | pages [16] -->
m

<!-- b004922 | prose | pages [16] -->
m

<!-- b004923 | prose | pages [16] -->
m

<!-- b004924 | prose | pages [16] -->
m

<!-- b004925 | prose | pages [16] -->
m

<!-- b004926 | prose | pages [16] -->
m

<!-- b004927 | prose | pages [16] -->
m

<!-- b004928 | prose | pages [16] -->
m

<!-- b004929 | prose | pages [16] -->
m

<!-- b004930 | prose | pages [16] -->
m

<!-- b004931 | prose | pages [16] -->
m

<!-- b004932 | prose | pages [16] -->
m

<!-- b004933 | prose | pages [16] -->
m

<!-- b004934 | prose | pages [16] -->
m

<!-- b004935 | prose | pages [16] -->
m

<!-- b004936 | prose | pages [16] -->
m

<!-- b004937 | prose | pages [16] -->
m

<!-- b004938 | prose | pages [16] -->
m

<!-- b004939 | prose | pages [16] -->
m

<!-- b004940 | prose | pages [16] -->
m

<!-- b004941 | prose | pages [16] -->
m

<!-- b004942 | prose | pages [16] -->
m

<!-- b004943 | prose | pages [16] -->
m

<!-- b004944 | prose | pages [16] -->
m

<!-- b004945 | prose | pages [16] -->
m

<!-- b004946 | prose | pages [16] -->
m

<!-- b004947 | prose | pages [16] -->
m

<!-- b004948 | prose | pages [16] -->
m

<!-- b004949 | prose | pages [16] -->
m

<!-- b004950 | prose | pages [16] -->
m

<!-- b004951 | prose | pages [16] -->
m

<!-- b004952 | prose | pages [16] -->
m

<!-- b004953 | prose | pages [16] -->
m

<!-- b004954 | prose | pages [16] -->
m

<!-- b004955 | prose | pages [16] -->
m

<!-- b004956 | prose | pages [16] -->
m

<!-- b004957 | prose | pages [16] -->
m

<!-- b004958 | prose | pages [16] -->
m

<!-- b004959 | prose | pages [16] -->
m

<!-- b004960 | prose | pages [16] -->
m

<!-- b004961 | prose | pages [16] -->
m

<!-- b004962 | prose | pages [16] -->
m

<!-- b004963 | prose | pages [16] -->
m

<!-- b004964 | prose | pages [16] -->
m

<!-- b004965 | prose | pages [16] -->
m

<!-- b004966 | prose | pages [16] -->
m

<!-- b004967 | prose | pages [16] -->
m

<!-- b004968 | prose | pages [16] -->
m

<!-- b004969 | prose | pages [16] -->
m

<!-- b004970 | prose | pages [16] -->
m

<!-- b004971 | prose | pages [16] -->
m

<!-- b004972 | prose | pages [16] -->
m

<!-- b004973 | prose | pages [16] -->
m

<!-- b004974 | prose | pages [16] -->
m

<!-- b004975 | prose | pages [16] -->
m

<!-- b004976 | prose | pages [16] -->
m

<!-- b004977 | prose | pages [16] -->
m

<!-- b004978 | prose | pages [16] -->
m

<!-- b004979 | prose | pages [16] -->
m

<!-- b004980 | prose | pages [16] -->
m

<!-- b004981 | prose | pages [16] -->
m

<!-- b004982 | prose | pages [16] -->
m

<!-- b004983 | prose | pages [16] -->
m

<!-- b004984 | prose | pages [16] -->
m

<!-- b004985 | prose | pages [16] -->
m

<!-- b004986 | prose | pages [16] -->
m

<!-- b004987 | prose | pages [16] -->
m

<!-- b004988 | prose | pages [16] -->
m

<!-- b004989 | prose | pages [16] -->
m

<!-- b004990 | prose | pages [16] -->
m

<!-- b004991 | prose | pages [16] -->
m

<!-- b004992 | prose | pages [16] -->
m

<!-- b004993 | prose | pages [16] -->
m

<!-- b004994 | prose | pages [16] -->
m

<!-- b004995 | prose | pages [16] -->
m

<!-- b004996 | prose | pages [16] -->
m

<!-- b004997 | prose | pages [16] -->
m

<!-- b004998 | prose | pages [16] -->
m

<!-- b004999 | prose | pages [16] -->
m

<!-- b005000 | prose | pages [16] -->
m

<!-- b005001 | prose | pages [16] -->
m

<!-- b005002 | prose | pages [16] -->
m

<!-- b005003 | prose | pages [16] -->
m

<!-- b005004 | prose | pages [16] -->
m

<!-- b005005 | prose | pages [16] -->
m

<!-- b005006 | prose | pages [16] -->
m

<!-- b005007 | prose | pages [16] -->
m

<!-- b005008 | prose | pages [16] -->
m

<!-- b005009 | prose | pages [16] -->
m

<!-- b005010 | prose | pages [16] -->
m

<!-- b005011 | prose | pages [16] -->
m

<!-- b005012 | prose | pages [16] -->
m

<!-- b005013 | prose | pages [16] -->
m

<!-- b005014 | prose | pages [16] -->
m

<!-- b005015 | prose | pages [16] -->
m

<!-- b005016 | prose | pages [16] -->
m

<!-- b005017 | prose | pages [16] -->
m

<!-- b005018 | prose | pages [16] -->
m

<!-- b005019 | prose | pages [16] -->
m

<!-- b005020 | prose | pages [16] -->
m

<!-- b005021 | prose | pages [16] -->
m

<!-- b005022 | prose | pages [16] -->
m

<!-- b005023 | prose | pages [16] -->
m

<!-- b005024 | prose | pages [16] -->
m

<!-- b005025 | prose | pages [16] -->
m

<!-- b005026 | prose | pages [16] -->
m

<!-- b005027 | prose | pages [16] -->
m

<!-- b005028 | prose | pages [16] -->
m

<!-- b005029 | prose | pages [16] -->
m

<!-- b005030 | prose | pages [16] -->
m

<!-- b005031 | prose | pages [16] -->
m

<!-- b005032 | prose | pages [16] -->
m

<!-- b005033 | prose | pages [16] -->
m

<!-- b005034 | prose | pages [16] -->
m

<!-- b005035 | prose | pages [16] -->
m

<!-- b005036 | prose | pages [16] -->
m

<!-- b005037 | prose | pages [16] -->
m

<!-- b005038 | prose | pages [16] -->
m

<!-- b005039 | prose | pages [16] -->
m

<!-- b005040 | prose | pages [16] -->
m

<!-- b005041 | prose | pages [16] -->
m

<!-- b005042 | prose | pages [16] -->
m

<!-- b005043 | prose | pages [16] -->
m

<!-- b005044 | prose | pages [16] -->
m

<!-- b005045 | prose | pages [16] -->
m

<!-- b005046 | prose | pages [16] -->
m

<!-- b005047 | prose | pages [16] -->
m

<!-- b005048 | prose | pages [16] -->
m

<!-- b005049 | prose | pages [16] -->
m

<!-- b005050 | prose | pages [16] -->
m

<!-- b005051 | prose | pages [16] -->
m

<!-- b005052 | prose | pages [16] -->
m

<!-- b005053 | prose | pages [16] -->
m

<!-- b005054 | prose | pages [16] -->
m

<!-- b005055 | prose | pages [16] -->
m

<!-- b005056 | prose | pages [16] -->
m

<!-- b005057 | prose | pages [16] -->
m

<!-- b005058 | prose | pages [16] -->
m

<!-- b005059 | prose | pages [16] -->
m

<!-- b005060 | prose | pages [16] -->
m

<!-- b005061 | prose | pages [16] -->
m

<!-- b005062 | prose | pages [16] -->
m

<!-- b005063 | prose | pages [16] -->
m

<!-- b005064 | prose | pages [16] -->
m

<!-- b005065 | prose | pages [16] -->
m

<!-- b005066 | prose | pages [16] -->
m

<!-- b005067 | prose | pages [16] -->
m

<!-- b005068 | prose | pages [16] -->
m

<!-- b005069 | prose | pages [16] -->
m

<!-- b005070 | prose | pages [16] -->
m

<!-- b005071 | prose | pages [16] -->
m

<!-- b005072 | prose | pages [16] -->
m

<!-- b005073 | prose | pages [16] -->
m

<!-- b005074 | prose | pages [16] -->
m

<!-- b005075 | prose | pages [16] -->
m

<!-- b005076 | prose | pages [16] -->
m

<!-- b005077 | prose | pages [16] -->
m

<!-- b005078 | prose | pages [16] -->
m

<!-- b005079 | prose | pages [16] -->
m

<!-- b005080 | prose | pages [16] -->
m

<!-- b005081 | prose | pages [16] -->
m

<!-- b005082 | prose | pages [16] -->
m

<!-- b005083 | prose | pages [16] -->
m

<!-- b005084 | prose | pages [16] -->
m

<!-- b005085 | prose | pages [16] -->
m

<!-- b005086 | prose | pages [16] -->
m

<!-- b005087 | prose | pages [16] -->
m

<!-- b005088 | prose | pages [16] -->
m

<!-- b005089 | prose | pages [16] -->
m

<!-- b005090 | prose | pages [16] -->
(a)

<!-- b005091 | furniture | pages [16] -->
Page 16 of 26

<!-- b005092 | prose | pages [16] -->
(b)

<!-- b005093 | caption | pages [16] -->
Figure 9: Cellular-Importance Mixed Plot

<!-- b005094 | caption | pages [16] -->
Figure 10: Top 15 Sports Event Importance Score

<!-- b005095 | prose | pages [16] -->
gold importance (0.9039) due to its variety and competition. Table Tennis, while lower in gold importance, is second in total medals (0.95), reflecting its global popularity and China’s dominance. Diving and Wrestling also hold significance, with Diving showcasing China’s strength.

<!-- b005096 | prose | pages [16] -->
Next, we will create univariate dependence plots for PC1, which has the highest SHAP importance. This analysis will illustrate the nonlinear relationship between PC1 and medal counts, highlighting contributions from sports such as Swimming, Athletics, Wrestling, Gymnastics, and Basketball.

<!-- b005097 | prose | pages [16] -->
In the gold medal prediction model (Fig. 11(a)), the negative region of PC1 is closely associated with sports that have high loadings, such as Swimming, Athletics, Wrestling, Gymnastics, and Basketball, which perform well when PC1 is negative, significantly con- tributing to the gold medal count. The upward trend in the dependence plot indicates that outstanding performances in these sports lead to a considerable increase in gold medals, highlighting their crucial impact, particularly in the negative PC1 area. As PC1 turns positive, their influence diminishes, demonstrating that their effects on gold medal counts are primarily concentrated in the negative region. Similarly, in the total medal prediction model (Fig. 11(b)), these same sports significantly impact the total medal count; high performance when PC1 is negative enhances both gold and overall medal tallies. The ascent of SHAP values in the dependence plot signifies that their excellence contributes notably not only to gold but also to silver and bronze medals. As PC1 becomes positive, their influence on total medal counts weakens, further confirming their critical role in the negative PC1 region.

<!-- b005098 | prose | pages [16] -->
关注数学模型

<!-- b005099 | furniture | pages [16] -->
2

<!-- b005100 | furniture | pages [16] -->
MATHmodels

<!-- b005101 | furniture | pages [16] -->
获取更多资讯

<!-- b005102 | furniture | pages [17] -->
Team # 2500759

<!-- b005103 | furniture | pages [17] -->
Page 17 of 26

<!-- b005104 | prose | pages [17] -->
微信公众号：数学模型

<!-- b005105 | prose | pages [17] -->
(a) (b)

<!-- b005106 | prose | pages [17] -->
微信号：MATHmodels

<!-- b005107 | caption | pages [17] -->
Figure 11: PC1-SHAP Mixed Plot

<!-- b005108 | prose | pages [17] -->
Finally, this study incorporates SHAP values for individual samples to analyze the impact of different sports on gold and total medal predictions for the U.S. and France, particularly focusing on the contributions of traditional powerhouses like Swimming and Athletics. Additionally, it discusses the host country effect, exploring how the upcoming host nations, France in 2024 and the USA in 2028, can positively influence predictions of gold and total medal counts through home advantage.

<!-- b005109 | prose | pages [17] -->
(a) (b)

<!-- b005110 | caption | pages [17] -->
Figure 12: 2028 U.S. Medal and Gold Medal Prediction SHAP Plot

<!-- b005111 | prose | pages [17] -->
(a) (b)

<!-- b005112 | caption | pages [17] -->
Figure 13: 2028 France Medal and Gold Medal Prediction SHAP Plot

<!-- b005113 | prose | pages [17] -->
Figs.

<!-- b005114 | prose | pages [17] -->
12(a)-(b) show that traditional power sports like Swimming and Athletics carry significant weight in the PCA components, particularly with high loadings in prin- cipal components PC1 and PC2, indicating their substantial contributions to the U.S. gold medal count. With a PC1 value of 18 for gold medal predictions, this confirms the driv- ing role of these sports. In contrast, the total medal count prediction for the U.S. is 133,

<!-- b005115 | furniture | pages [20] -->
Team # 2500759

<!-- b005116 | furniture | pages [20] -->
Page 20 of 26

<!-- b005117 | caption | pages [20] -->
Figure 14: The Top 10 Countries by Contribution Coefficient

<!-- b005118 | caption | pages [20] -->
Figure 15: Trends in Medals Acquisition in Japan from 1996 to 2016

<!-- b005119 | prose | pages [20] -->
that certain countries display relatively stable performances across different Olympic cy- cles, while others experience significant fluctuations in their medal counts. For instance, some major nations show a limited range of variance in their medal counts, highlighting their sustained competitiveness across multiple events. In contrast, some smaller nations exhibit greater volatility in their medal counts, suggesting that their performance may be heavily influenced by specific events or sudden occurrences.

<!-- b005120 | prose | pages [20] -->
(2) Decision support: The findings can assist the Olympic committees in developing more flexible strategies for future Olympic cycles. If a country exhibits instability in its medal counts, the committee can mitigate uncertainty by diversifying resource allocation, thereby avoiding excessive reliance on any single event. For example, increasing train- ing investments in unstable events and enhancing the competitiveness of other promising sports can help ensure consistent performance across various disciplines. Additionally, for countries showing more stable performances, the Olympic committees could focus on maintaining existing advantages while bolstering research and technical support to ensure they remain competitive at the forefront.

<!-- b005121 | prose | pages [20] -->
2. Correlation Between Olympic Medal Counts and Specific Events

<!-- b005122 | prose | pages [20] -->
(1) Insight: The model, through the integration of PCA and LSTM, reveals the sig- nificance of certain specific events in predicting medal counts. The research demonstrates that disciplines such as swimming, athletics, and shooting play a crucial role in the medal contributions of many countries. These events are not only widely recognized and highly competitive at the Olympics but also serve as essential battlegrounds for countries vying for medals. In particular, swimming and athletics stand out as primary sources of medal counts for many nations due to their frequent competitions and high viewer engagement.

<!-- b005123 | prose | pages [20] -->
关注数学模型

<!-- b005124 | furniture | pages [20] -->
2

<!-- b005125 | furniture | pages [20] -->
MATHmodels

<!-- b005126 | furniture | pages [20] -->
获取更多资讯

<!-- b005127 | furniture | pages [21] -->
Team # 2500759

<!-- b005128 | furniture | pages [21] -->
Page 21 of 26

<!-- b005129 | prose | pages [21] -->
(2) Decision support: Olympic committees can leverage these analytical findings for strategic planning, particularly in resource allocation and event development. For events that display a strong competitive advantage, countries can increase their invest- ments by providing additional training facilities and financial support. For instance, in nations where swimming and athletics are particularly strong, committees could enhance athlete training by collaborating with top domestic and international coaches to refine skills and improve overall performance. Furthermore, informed by data analysis, coun- tries can identify potential medal-winning events in advance, enabling them to formulate effective athlete development programs and promotional strategies for these disciplines.

<!-- b005130 | prose | pages [21] -->
微信公众号：数学模型

<!-- b005131 | prose | pages [21] -->
3. Coaching Investment Directions in National Strategies

<!-- b005132 | prose | pages [21] -->
(1) Insight: Through model analysis, some countries exhibit strong medal returns following coaching changes, as seen in Australia. Conversely, other nations experience minimal impact from such coaching transitions, despite implementing changes.

<!-- b005133 | prose | pages [21] -->
(2) Decision support: Olympic committees should develop personalized strategies based on the specific circumstances of different countries, prioritizing support for events that demonstrate significant improvements post-coaching changes. For countries such as Japan, Italy, and Australia, the committees could enhance investments in judo, athletics, and swimming to increase medal returns. Meanwhile, for events that show less pro-

<!-- b005134 | prose | pages [21] -->
微信号：MATHmodels

<!-- b005135 | prose | pages [21] -->
nounced results, committees could reduce excessive investments in those coaching staff and reallocate resources to focus on areas more likely to yield medals.

<!-- b005136 | prose | pages [21] -->
6

<!-- b005137 | heading | pages [21] -->
Sensitivity Analysis

<!-- b005138 | prose | pages [21] -->
6.1 The Number of Principal Components

<!-- b005139 | prose | pages [21] -->
To simplify the data structure and improve the efficiency of the prediction model, Principal Component Analysis (PCA) was used. PCA was performed on the Olympic event dataset, and the variance contribution rates of each principal component were cal- culated. The selection of five principal components was based on their explanation of 76.4% of the cumulative variance, effectively capturing most of the information in the original dataset. This choice is supported by Fig. 16, which shows a steep drop-off after the first few components, validating the use of five components. This approach reduces data dimensionality while retaining essential information and eliminating redundant fea- tures.

<!-- b005140 | caption | pages [21] -->
Figure 16: Scree Plot for Principal Component Selection

<!-- b005141 | prose | pages [21] -->
6.2

<!-- b005142 | heading | pages [21] -->
Prediction Model Evaluation

<!-- b005143 | prose | pages [21] -->
In the model evaluation, we examined both the predictive accuracy and robustness of the gold medal and total medal prediction models.

<!-- b005144 | prose | pages [21] -->
m

<!-- b005145 | prose | pages [21] -->
m

<!-- b005146 | prose | pages [21] -->
m

<!-- b005147 | prose | pages [21] -->
m

<!-- b005148 | prose | pages [21] -->
m

<!-- b005149 | prose | pages [21] -->
m

<!-- b005150 | prose | pages [21] -->
m

<!-- b005151 | prose | pages [21] -->
m

<!-- b005152 | prose | pages [21] -->
m

<!-- b005153 | prose | pages [21] -->
m

<!-- b005154 | prose | pages [21] -->
m

<!-- b005155 | prose | pages [21] -->
m

<!-- b005156 | prose | pages [21] -->
m

<!-- b005157 | prose | pages [21] -->
m

<!-- b005158 | prose | pages [21] -->
m

<!-- b005159 | prose | pages [21] -->
m

<!-- b005160 | prose | pages [21] -->
m

<!-- b005161 | prose | pages [21] -->
m

<!-- b005162 | prose | pages [21] -->
m

<!-- b005163 | prose | pages [21] -->
m

<!-- b005164 | prose | pages [21] -->
m

<!-- b005165 | prose | pages [21] -->
m

<!-- b005166 | prose | pages [21] -->
m

<!-- b005167 | prose | pages [21] -->
m

<!-- b005168 | prose | pages [21] -->
m

<!-- b005169 | prose | pages [21] -->
m

<!-- b005170 | prose | pages [21] -->
m

<!-- b005171 | prose | pages [21] -->
m

<!-- b005172 | prose | pages [21] -->
m

<!-- b005173 | prose | pages [21] -->
m

<!-- b005174 | prose | pages [21] -->
m

<!-- b005175 | prose | pages [21] -->
m

<!-- b005176 | prose | pages [21] -->
m

<!-- b005177 | prose | pages [21] -->
m

<!-- b005178 | prose | pages [21] -->
m

<!-- b005179 | prose | pages [21] -->
m

<!-- b005180 | prose | pages [21] -->
m

<!-- b005181 | prose | pages [21] -->
m

<!-- b005182 | prose | pages [21] -->
m

<!-- b005183 | prose | pages [21] -->
m

<!-- b005184 | prose | pages [21] -->
m

<!-- b005185 | prose | pages [21] -->
m

<!-- b005186 | prose | pages [21] -->
m

<!-- b005187 | prose | pages [21] -->
m

<!-- b005188 | prose | pages [21] -->
m

<!-- b005189 | prose | pages [21] -->
m

<!-- b005190 | prose | pages [21] -->
m

<!-- b005191 | prose | pages [21] -->
m

<!-- b005192 | prose | pages [21] -->
m

<!-- b005193 | prose | pages [21] -->
m

<!-- b005194 | prose | pages [21] -->
m

<!-- b005195 | prose | pages [21] -->
m

<!-- b005196 | prose | pages [21] -->
m

<!-- b005197 | prose | pages [21] -->
m

<!-- b005198 | prose | pages [21] -->
m

<!-- b005199 | prose | pages [21] -->
m

<!-- b005200 | prose | pages [21] -->
m

<!-- b005201 | prose | pages [21] -->
m

<!-- b005202 | prose | pages [21] -->
m

<!-- b005203 | prose | pages [21] -->
m

<!-- b005204 | prose | pages [21] -->
m

<!-- b005205 | prose | pages [21] -->
m

<!-- b005206 | prose | pages [21] -->
m

<!-- b005207 | prose | pages [21] -->
m

<!-- b005208 | prose | pages [21] -->
m

<!-- b005209 | prose | pages [21] -->
m

<!-- b005210 | prose | pages [21] -->
m

<!-- b005211 | prose | pages [21] -->
m

<!-- b005212 | prose | pages [21] -->
m

<!-- b005213 | prose | pages [21] -->
m

<!-- b005214 | prose | pages [21] -->
m

<!-- b005215 | prose | pages [21] -->
m

<!-- b005216 | prose | pages [21] -->
m

<!-- b005217 | prose | pages [21] -->
m

<!-- b005218 | prose | pages [21] -->
m

<!-- b005219 | prose | pages [21] -->
m

<!-- b005220 | prose | pages [21] -->
m

<!-- b005221 | prose | pages [21] -->
m

<!-- b005222 | prose | pages [21] -->
m

<!-- b005223 | prose | pages [21] -->
m

<!-- b005224 | prose | pages [21] -->
m

<!-- b005225 | prose | pages [21] -->
m

<!-- b005226 | prose | pages [21] -->
m

<!-- b005227 | prose | pages [21] -->
m

<!-- b005228 | prose | pages [21] -->
m

<!-- b005229 | prose | pages [21] -->
m

<!-- b005230 | prose | pages [21] -->
m

<!-- b005231 | prose | pages [21] -->
m

<!-- b005232 | prose | pages [21] -->
m

<!-- b005233 | prose | pages [21] -->
m

<!-- b005234 | prose | pages [21] -->
m

<!-- b005235 | prose | pages [21] -->
m

<!-- b005236 | prose | pages [21] -->
m

<!-- b005237 | prose | pages [21] -->
m

<!-- b005238 | prose | pages [21] -->
m

<!-- b005239 | prose | pages [21] -->
m

<!-- b005240 | prose | pages [21] -->
m

<!-- b005241 | prose | pages [21] -->
m

<!-- b005242 | prose | pages [21] -->
m

<!-- b005243 | prose | pages [21] -->
m

<!-- b005244 | prose | pages [21] -->
m

<!-- b005245 | prose | pages [21] -->
m

<!-- b005246 | prose | pages [21] -->
m

<!-- b005247 | prose | pages [21] -->
m

<!-- b005248 | prose | pages [21] -->
m

<!-- b005249 | prose | pages [21] -->
m

<!-- b005250 | prose | pages [21] -->
m

<!-- b005251 | prose | pages [21] -->
m

<!-- b005252 | prose | pages [21] -->
m

<!-- b005253 | prose | pages [21] -->
m

<!-- b005254 | prose | pages [21] -->
m

<!-- b005255 | prose | pages [21] -->
m

<!-- b005256 | prose | pages [21] -->
m

<!-- b005257 | prose | pages [21] -->
m

<!-- b005258 | prose | pages [21] -->
m

<!-- b005259 | prose | pages [21] -->
m

<!-- b005260 | prose | pages [21] -->
m

<!-- b005261 | prose | pages [21] -->
m

<!-- b005262 | prose | pages [21] -->
m

<!-- b005263 | prose | pages [21] -->
m

<!-- b005264 | prose | pages [21] -->
m

<!-- b005265 | prose | pages [21] -->
m

<!-- b005266 | prose | pages [21] -->
m

<!-- b005267 | prose | pages [21] -->
m

<!-- b005268 | prose | pages [21] -->
m

<!-- b005269 | prose | pages [21] -->
m

<!-- b005270 | prose | pages [21] -->
m

<!-- b005271 | prose | pages [21] -->
m

<!-- b005272 | prose | pages [21] -->
m

<!-- b005273 | prose | pages [21] -->
m

<!-- b005274 | prose | pages [21] -->
m

<!-- b005275 | prose | pages [21] -->
m

<!-- b005276 | prose | pages [21] -->
m

<!-- b005277 | prose | pages [21] -->
m

<!-- b005278 | prose | pages [21] -->
m

<!-- b005279 | prose | pages [21] -->
m

<!-- b005280 | prose | pages [21] -->
m

<!-- b005281 | prose | pages [21] -->
m

<!-- b005282 | prose | pages [21] -->
m

<!-- b005283 | prose | pages [21] -->
m

<!-- b005284 | prose | pages [21] -->
m

<!-- b005285 | prose | pages [21] -->
m

<!-- b005286 | prose | pages [21] -->
m

<!-- b005287 | prose | pages [21] -->
m

<!-- b005288 | prose | pages [21] -->
m

<!-- b005289 | prose | pages [21] -->
m

<!-- b005290 | prose | pages [21] -->
m

<!-- b005291 | prose | pages [21] -->
m

<!-- b005292 | prose | pages [21] -->
m

<!-- b005293 | prose | pages [21] -->
m

<!-- b005294 | prose | pages [21] -->
m

<!-- b005295 | prose | pages [21] -->
m

<!-- b005296 | prose | pages [21] -->
m

<!-- b005297 | prose | pages [21] -->
m

<!-- b005298 | prose | pages [21] -->
m

<!-- b005299 | prose | pages [21] -->
m

<!-- b005300 | prose | pages [21] -->
m

<!-- b005301 | prose | pages [21] -->
m

<!-- b005302 | prose | pages [21] -->
m

<!-- b005303 | prose | pages [21] -->
m

<!-- b005304 | prose | pages [21] -->
m

<!-- b005305 | prose | pages [21] -->
m

<!-- b005306 | prose | pages [21] -->
m

<!-- b005307 | prose | pages [21] -->
m

<!-- b005308 | prose | pages [21] -->
m

<!-- b005309 | prose | pages [21] -->
m

<!-- b005310 | prose | pages [21] -->
m

<!-- b005311 | prose | pages [21] -->
m

<!-- b005312 | prose | pages [21] -->
m

<!-- b005313 | prose | pages [21] -->
m

<!-- b005314 | prose | pages [21] -->
m

<!-- b005315 | prose | pages [21] -->
m

<!-- b005316 | prose | pages [21] -->
m

<!-- b005317 | prose | pages [21] -->
m

<!-- b005318 | prose | pages [21] -->
m

<!-- b005319 | prose | pages [21] -->
m

<!-- b005320 | prose | pages [21] -->
m

<!-- b005321 | prose | pages [21] -->
m

<!-- b005322 | prose | pages [21] -->
m

<!-- b005323 | prose | pages [21] -->
m

<!-- b005324 | prose | pages [21] -->
m

<!-- b005325 | prose | pages [21] -->
m

<!-- b005326 | prose | pages [21] -->
m

<!-- b005327 | prose | pages [21] -->
m

<!-- b005328 | prose | pages [21] -->
m

<!-- b005329 | prose | pages [21] -->
m

<!-- b005330 | prose | pages [21] -->
m

<!-- b005331 | prose | pages [21] -->
m

<!-- b005332 | prose | pages [21] -->
m

<!-- b005333 | prose | pages [21] -->
m

<!-- b005334 | prose | pages [21] -->
m

<!-- b005335 | prose | pages [21] -->
m

<!-- b005336 | prose | pages [21] -->
m

<!-- b005337 | prose | pages [21] -->
m

<!-- b005338 | prose | pages [21] -->
m

<!-- b005339 | prose | pages [21] -->
m

<!-- b005340 | prose | pages [21] -->
m

<!-- b005341 | prose | pages [21] -->
m

<!-- b005342 | prose | pages [21] -->
m

<!-- b005343 | prose | pages [21] -->
m

<!-- b005344 | prose | pages [21] -->
m

<!-- b005345 | prose | pages [21] -->
m

<!-- b005346 | prose | pages [21] -->
m

<!-- b005347 | prose | pages [21] -->
m

<!-- b005348 | prose | pages [21] -->
m

<!-- b005349 | prose | pages [21] -->
m

<!-- b005350 | prose | pages [21] -->
m

<!-- b005351 | prose | pages [21] -->
m

<!-- b005352 | prose | pages [21] -->
m

<!-- b005353 | prose | pages [21] -->
m

<!-- b005354 | prose | pages [21] -->
m

<!-- b005355 | prose | pages [21] -->
m

<!-- b005356 | prose | pages [21] -->
m

<!-- b005357 | prose | pages [21] -->
m

<!-- b005358 | prose | pages [21] -->
m

<!-- b005359 | prose | pages [21] -->
m

<!-- b005360 | prose | pages [21] -->
m

<!-- b005361 | prose | pages [21] -->
m

<!-- b005362 | prose | pages [21] -->
m

<!-- b005363 | prose | pages [21] -->
m

<!-- b005364 | prose | pages [21] -->
m

<!-- b005365 | prose | pages [21] -->
m

<!-- b005366 | prose | pages [21] -->
m

<!-- b005367 | prose | pages [21] -->
m

<!-- b005368 | prose | pages [21] -->
m

<!-- b005369 | prose | pages [21] -->
m

<!-- b005370 | prose | pages [21] -->
m

<!-- b005371 | prose | pages [21] -->
m

<!-- b005372 | prose | pages [21] -->
m

<!-- b005373 | prose | pages [21] -->
m

<!-- b005374 | prose | pages [21] -->
m

<!-- b005375 | prose | pages [21] -->
m

<!-- b005376 | prose | pages [21] -->
m

<!-- b005377 | prose | pages [21] -->
m

<!-- b005378 | prose | pages [21] -->
m

<!-- b005379 | prose | pages [21] -->
m

<!-- b005380 | prose | pages [21] -->
m

<!-- b005381 | prose | pages [21] -->
m

<!-- b005382 | prose | pages [21] -->
m

<!-- b005383 | prose | pages [21] -->
m

<!-- b005384 | prose | pages [21] -->
m

<!-- b005385 | prose | pages [21] -->
m

<!-- b005386 | prose | pages [21] -->
m

<!-- b005387 | prose | pages [21] -->
m

<!-- b005388 | prose | pages [21] -->
m

<!-- b005389 | prose | pages [21] -->
m

<!-- b005390 | prose | pages [21] -->
m

<!-- b005391 | prose | pages [21] -->
m

<!-- b005392 | prose | pages [21] -->
m

<!-- b005393 | prose | pages [21] -->
m

<!-- b005394 | prose | pages [21] -->
m

<!-- b005395 | prose | pages [21] -->
m

<!-- b005396 | prose | pages [21] -->
m

<!-- b005397 | prose | pages [21] -->
m

<!-- b005398 | prose | pages [21] -->
m

<!-- b005399 | prose | pages [21] -->
m

<!-- b005400 | prose | pages [21] -->
m

<!-- b005401 | prose | pages [21] -->
m

<!-- b005402 | prose | pages [21] -->
m

<!-- b005403 | prose | pages [21] -->
m

<!-- b005404 | prose | pages [21] -->
m

<!-- b005405 | prose | pages [21] -->
m

<!-- b005406 | prose | pages [21] -->
m

<!-- b005407 | prose | pages [21] -->
m

<!-- b005408 | prose | pages [21] -->
m

<!-- b005409 | prose | pages [21] -->
m

<!-- b005410 | prose | pages [21] -->
m

<!-- b005411 | prose | pages [21] -->
m

<!-- b005412 | prose | pages [21] -->
m

<!-- b005413 | prose | pages [21] -->
m

<!-- b005414 | prose | pages [21] -->
m

<!-- b005415 | prose | pages [21] -->
m

<!-- b005416 | prose | pages [21] -->
m

<!-- b005417 | prose | pages [21] -->
m

<!-- b005418 | prose | pages [21] -->
m

<!-- b005419 | prose | pages [21] -->
m

<!-- b005420 | prose | pages [21] -->
m

<!-- b005421 | prose | pages [21] -->
m

<!-- b005422 | prose | pages [21] -->
m

<!-- b005423 | prose | pages [21] -->
m

<!-- b005424 | prose | pages [21] -->
m

<!-- b005425 | prose | pages [21] -->
m

<!-- b005426 | prose | pages [21] -->
m

<!-- b005427 | prose | pages [21] -->
m

<!-- b005428 | furniture | pages [21] -->
m

<!-- b005429 | furniture | pages [21] -->
m

<!-- b005430 | furniture | pages [21] -->
m

<!-- b005431 | furniture | pages [21] -->
m

<!-- b005432 | furniture | pages [21] -->
m

<!-- b005433 | furniture | pages [21] -->
m

<!-- b005434 | furniture | pages [21] -->
m

<!-- b005435 | furniture | pages [21] -->
m

<!-- b005436 | furniture | pages [21] -->
m

<!-- b005437 | furniture | pages [21] -->
m

<!-- b005438 | furniture | pages [21] -->
m

<!-- b005439 | furniture | pages [21] -->
m

<!-- b005440 | furniture | pages [21] -->
m

<!-- b005441 | furniture | pages [21] -->
m

<!-- b005442 | furniture | pages [21] -->
m

<!-- b005443 | furniture | pages [21] -->
m

<!-- b005444 | furniture | pages [21] -->
m

<!-- b005445 | furniture | pages [21] -->
m

<!-- b005446 | furniture | pages [21] -->
m

<!-- b005447 | furniture | pages [21] -->
m

<!-- b005448 | furniture | pages [21] -->
m

<!-- b005449 | furniture | pages [21] -->
m

<!-- b005450 | furniture | pages [21] -->
m

<!-- b005451 | furniture | pages [21] -->
m

<!-- b005452 | furniture | pages [21] -->
m

<!-- b005453 | furniture | pages [21] -->
m

<!-- b005454 | furniture | pages [21] -->
m

<!-- b005455 | furniture | pages [21] -->
m

<!-- b005456 | furniture | pages [21] -->
m

<!-- b005457 | furniture | pages [21] -->
m

<!-- b005458 | furniture | pages [21] -->
m

<!-- b005459 | furniture | pages [21] -->
m

<!-- b005460 | furniture | pages [21] -->
m

<!-- b005461 | furniture | pages [21] -->
m

<!-- b005462 | furniture | pages [21] -->
m

<!-- b005463 | furniture | pages [21] -->
m

<!-- b005464 | furniture | pages [21] -->
m

<!-- b005465 | furniture | pages [21] -->
m

<!-- b005466 | furniture | pages [21] -->
m

<!-- b005467 | furniture | pages [21] -->
m

<!-- b005468 | furniture | pages [21] -->
m

<!-- b005469 | furniture | pages [21] -->
m

<!-- b005470 | furniture | pages [21] -->
m

<!-- b005471 | furniture | pages [21] -->
m

<!-- b005472 | furniture | pages [21] -->
m

<!-- b005473 | furniture | pages [21] -->
m

<!-- b005474 | furniture | pages [21] -->
m

<!-- b005475 | furniture | pages [21] -->
m

<!-- b005476 | furniture | pages [21] -->
m

<!-- b005477 | furniture | pages [21] -->
m

<!-- b005478 | furniture | pages [21] -->
m

<!-- b005479 | furniture | pages [21] -->
m

<!-- b005480 | furniture | pages [21] -->
m

<!-- b005481 | furniture | pages [21] -->
m

<!-- b005482 | furniture | pages [21] -->
m

<!-- b005483 | furniture | pages [21] -->
m

<!-- b005484 | furniture | pages [21] -->
m

<!-- b005485 | furniture | pages [21] -->
m

<!-- b005486 | furniture | pages [21] -->
m

<!-- b005487 | furniture | pages [21] -->
m

<!-- b005488 | furniture | pages [21] -->
m

<!-- b005489 | furniture | pages [21] -->
m

<!-- b005490 | furniture | pages [21] -->
m

<!-- b005491 | furniture | pages [21] -->
m

<!-- b005492 | furniture | pages [21] -->
m

<!-- b005493 | furniture | pages [21] -->
m

<!-- b005494 | furniture | pages [21] -->
m

<!-- b005495 | furniture | pages [21] -->
m

<!-- b005496 | furniture | pages [21] -->
m

<!-- b005497 | furniture | pages [21] -->
m

<!-- b005498 | furniture | pages [21] -->
m

<!-- b005499 | furniture | pages [21] -->
m

<!-- b005500 | furniture | pages [21] -->
m

<!-- b005501 | furniture | pages [21] -->
m

<!-- b005502 | furniture | pages [21] -->
m

<!-- b005503 | furniture | pages [21] -->
m

<!-- b005504 | furniture | pages [21] -->
m

<!-- b005505 | furniture | pages [21] -->
m

<!-- b005506 | furniture | pages [21] -->
m

<!-- b005507 | furniture | pages [21] -->
m

<!-- b005508 | furniture | pages [21] -->
m

<!-- b005509 | furniture | pages [21] -->
m

<!-- b005510 | furniture | pages [21] -->
m

<!-- b005511 | furniture | pages [21] -->
m

<!-- b005512 | furniture | pages [21] -->
m

<!-- b005513 | furniture | pages [21] -->
m

<!-- b005514 | furniture | pages [21] -->
m

<!-- b005515 | furniture | pages [21] -->
m

<!-- b005516 | furniture | pages [21] -->
m

<!-- b005517 | furniture | pages [21] -->
m

<!-- b005518 | furniture | pages [21] -->
m

<!-- b005519 | furniture | pages [21] -->
m

<!-- b005520 | furniture | pages [21] -->
m

<!-- b005521 | furniture | pages [21] -->
m

<!-- b005522 | furniture | pages [21] -->
m

<!-- b005523 | furniture | pages [21] -->
m

<!-- b005524 | furniture | pages [21] -->
m

<!-- b005525 | furniture | pages [21] -->
m

<!-- b005526 | furniture | pages [21] -->
m

<!-- b005527 | furniture | pages [21] -->
m

<!-- b005528 | furniture | pages [21] -->
m

<!-- b005529 | furniture | pages [21] -->
m

<!-- b005530 | furniture | pages [21] -->
m

<!-- b005531 | furniture | pages [21] -->
m

<!-- b005532 | furniture | pages [21] -->
m

<!-- b005533 | furniture | pages [21] -->
m

<!-- b005534 | furniture | pages [21] -->
m

<!-- b005535 | furniture | pages [21] -->
m

<!-- b005536 | furniture | pages [21] -->
m

<!-- b005537 | furniture | pages [21] -->
m

<!-- b005538 | furniture | pages [21] -->
m

<!-- b005539 | furniture | pages [21] -->
m

<!-- b005540 | furniture | pages [21] -->
m

<!-- b005541 | furniture | pages [21] -->
m

<!-- b005542 | furniture | pages [21] -->
m

<!-- b005543 | furniture | pages [21] -->
m

<!-- b005544 | furniture | pages [21] -->
m

<!-- b005545 | furniture | pages [21] -->
m

<!-- b005546 | furniture | pages [21] -->
m

<!-- b005547 | furniture | pages [21] -->
m

<!-- b005548 | furniture | pages [21] -->
m

<!-- b005549 | furniture | pages [21] -->
m

<!-- b005550 | furniture | pages [21] -->
m

<!-- b005551 | furniture | pages [21] -->
m

<!-- b005552 | furniture | pages [21] -->
m

<!-- b005553 | furniture | pages [21] -->
m

<!-- b005554 | furniture | pages [21] -->
m

<!-- b005555 | furniture | pages [21] -->
m

<!-- b005556 | furniture | pages [21] -->
m

<!-- b005557 | furniture | pages [21] -->
m

<!-- b005558 | furniture | pages [21] -->
m

<!-- b005559 | furniture | pages [21] -->
m

<!-- b005560 | furniture | pages [21] -->
m

<!-- b005561 | furniture | pages [21] -->
m

<!-- b005562 | furniture | pages [21] -->
m

<!-- b005563 | furniture | pages [21] -->
m

<!-- b005564 | furniture | pages [21] -->
m

<!-- b005565 | furniture | pages [21] -->
m

<!-- b005566 | furniture | pages [21] -->
m

<!-- b005567 | furniture | pages [21] -->
m

<!-- b005568 | furniture | pages [21] -->
m

<!-- b005569 | furniture | pages [21] -->
m

<!-- b005570 | furniture | pages [21] -->
m

<!-- b005571 | furniture | pages [21] -->
m

<!-- b005572 | furniture | pages [21] -->
m

<!-- b005573 | furniture | pages [21] -->
m

<!-- b005574 | furniture | pages [21] -->
m

<!-- b005575 | furniture | pages [21] -->
m

<!-- b005576 | furniture | pages [21] -->
m

<!-- b005577 | furniture | pages [21] -->
m

<!-- b005578 | furniture | pages [21] -->
m

<!-- b005579 | furniture | pages [21] -->
m

<!-- b005580 | furniture | pages [21] -->
m

<!-- b005581 | furniture | pages [21] -->
m

<!-- b005582 | furniture | pages [21] -->
m

<!-- b005583 | furniture | pages [21] -->
m

<!-- b005584 | furniture | pages [21] -->
m

<!-- b005585 | furniture | pages [21] -->
m

<!-- b005586 | furniture | pages [21] -->
m

<!-- b005587 | furniture | pages [21] -->
m

<!-- b005588 | furniture | pages [21] -->
m

<!-- b005589 | furniture | pages [21] -->
m

<!-- b005590 | furniture | pages [21] -->
m

<!-- b005591 | furniture | pages [21] -->
m

<!-- b005592 | furniture | pages [21] -->
m

<!-- b005593 | furniture | pages [21] -->
m

<!-- b005594 | furniture | pages [21] -->
m

<!-- b005595 | furniture | pages [21] -->
m

<!-- b005596 | furniture | pages [21] -->
m

<!-- b005597 | furniture | pages [21] -->
m

<!-- b005598 | furniture | pages [21] -->
m

<!-- b005599 | furniture | pages [21] -->
m

<!-- b005600 | furniture | pages [21] -->
m

<!-- b005601 | furniture | pages [21] -->
m

<!-- b005602 | furniture | pages [21] -->
m

<!-- b005603 | furniture | pages [21] -->
m

<!-- b005604 | furniture | pages [21] -->
m

<!-- b005605 | furniture | pages [21] -->
m

<!-- b005606 | furniture | pages [21] -->
m

<!-- b005607 | furniture | pages [21] -->
m

<!-- b005608 | furniture | pages [21] -->
m

<!-- b005609 | furniture | pages [21] -->
m

<!-- b005610 | furniture | pages [21] -->
m

<!-- b005611 | furniture | pages [21] -->
m

<!-- b005612 | furniture | pages [21] -->
m

<!-- b005613 | furniture | pages [21] -->
m

<!-- b005614 | furniture | pages [21] -->
m

<!-- b005615 | furniture | pages [21] -->
m

<!-- b005616 | furniture | pages [21] -->
m

<!-- b005617 | furniture | pages [21] -->
m

<!-- b005618 | furniture | pages [21] -->
m

<!-- b005619 | furniture | pages [21] -->
m

<!-- b005620 | furniture | pages [21] -->
m

<!-- b005621 | furniture | pages [21] -->
m

<!-- b005622 | furniture | pages [21] -->
m

<!-- b005623 | furniture | pages [21] -->
m

<!-- b005624 | furniture | pages [21] -->
m

<!-- b005625 | furniture | pages [21] -->
m

<!-- b005626 | furniture | pages [21] -->
m

<!-- b005627 | furniture | pages [21] -->
m

<!-- b005628 | furniture | pages [21] -->
m

<!-- b005629 | furniture | pages [21] -->
m

<!-- b005630 | furniture | pages [21] -->
m

<!-- b005631 | furniture | pages [21] -->
m

<!-- b005632 | furniture | pages [21] -->
m

<!-- b005633 | furniture | pages [21] -->
m

<!-- b005634 | furniture | pages [21] -->
m

<!-- b005635 | furniture | pages [21] -->
m

<!-- b005636 | furniture | pages [21] -->
m

<!-- b005637 | furniture | pages [21] -->
m

<!-- b005638 | furniture | pages [21] -->
m

<!-- b005639 | furniture | pages [21] -->
m

<!-- b005640 | furniture | pages [21] -->
m

<!-- b005641 | furniture | pages [21] -->
m

<!-- b005642 | furniture | pages [21] -->
m

<!-- b005643 | furniture | pages [21] -->
m

<!-- b005644 | furniture | pages [21] -->
m

<!-- b005645 | furniture | pages [21] -->
m

<!-- b005646 | furniture | pages [21] -->
m

<!-- b005647 | furniture | pages [21] -->
m

<!-- b005648 | furniture | pages [21] -->
m

<!-- b005649 | furniture | pages [21] -->
m

<!-- b005650 | furniture | pages [21] -->
m

<!-- b005651 | furniture | pages [21] -->
m

<!-- b005652 | furniture | pages [21] -->
m

<!-- b005653 | furniture | pages [21] -->
m

<!-- b005654 | furniture | pages [21] -->
m

<!-- b005655 | furniture | pages [21] -->
m

<!-- b005656 | furniture | pages [21] -->
m

<!-- b005657 | furniture | pages [21] -->
m

<!-- b005658 | furniture | pages [21] -->
m

<!-- b005659 | furniture | pages [21] -->
m

<!-- b005660 | furniture | pages [21] -->
m

<!-- b005661 | furniture | pages [21] -->
m

<!-- b005662 | furniture | pages [21] -->
m

<!-- b005663 | furniture | pages [21] -->
m

<!-- b005664 | furniture | pages [21] -->
m

<!-- b005665 | furniture | pages [21] -->
m

<!-- b005666 | furniture | pages [21] -->
m

<!-- b005667 | furniture | pages [21] -->
m

<!-- b005668 | furniture | pages [21] -->
m

<!-- b005669 | furniture | pages [21] -->
m

<!-- b005670 | furniture | pages [21] -->
m

<!-- b005671 | furniture | pages [21] -->
m

<!-- b005672 | furniture | pages [21] -->
m

<!-- b005673 | furniture | pages [21] -->
m

<!-- b005674 | furniture | pages [21] -->
m

<!-- b005675 | furniture | pages [21] -->
m

<!-- b005676 | furniture | pages [21] -->
m

<!-- b005677 | furniture | pages [21] -->
m

<!-- b005678 | furniture | pages [21] -->
m

<!-- b005679 | furniture | pages [21] -->
m

<!-- b005680 | furniture | pages [21] -->
m

<!-- b005681 | furniture | pages [21] -->
m

<!-- b005682 | furniture | pages [21] -->
m

<!-- b005683 | furniture | pages [21] -->
m

<!-- b005684 | furniture | pages [21] -->
m

<!-- b005685 | furniture | pages [21] -->
m

<!-- b005686 | furniture | pages [21] -->
m

<!-- b005687 | furniture | pages [21] -->
m

<!-- b005688 | furniture | pages [21] -->
m

<!-- b005689 | furniture | pages [21] -->
m

<!-- b005690 | furniture | pages [21] -->
m

<!-- b005691 | furniture | pages [21] -->
m

<!-- b005692 | furniture | pages [21] -->
m

<!-- b005693 | furniture | pages [21] -->
m

<!-- b005694 | furniture | pages [21] -->
m

<!-- b005695 | furniture | pages [21] -->
m

<!-- b005696 | furniture | pages [21] -->
m

<!-- b005697 | furniture | pages [21] -->
m

<!-- b005698 | furniture | pages [21] -->
m

<!-- b005699 | furniture | pages [21] -->
m

<!-- b005700 | furniture | pages [21] -->
m

<!-- b005701 | furniture | pages [21] -->
m

<!-- b005702 | furniture | pages [21] -->
m

<!-- b005703 | furniture | pages [21] -->
m

<!-- b005704 | furniture | pages [21] -->
m

<!-- b005705 | furniture | pages [21] -->
m

<!-- b005706 | furniture | pages [21] -->
m

<!-- b005707 | furniture | pages [21] -->
m

<!-- b005708 | furniture | pages [21] -->
m

<!-- b005709 | furniture | pages [21] -->
m

<!-- b005710 | furniture | pages [21] -->
m

<!-- b005711 | furniture | pages [21] -->
m

<!-- b005712 | furniture | pages [21] -->
m

<!-- b005713 | furniture | pages [21] -->
m

<!-- b005714 | furniture | pages [21] -->
m

<!-- b005715 | furniture | pages [21] -->
m

<!-- b005716 | furniture | pages [21] -->
m

<!-- b005717 | furniture | pages [21] -->
m

<!-- b005718 | furniture | pages [21] -->
m

<!-- b005719 | furniture | pages [21] -->
m

<!-- b005720 | furniture | pages [21] -->
m

<!-- b005721 | furniture | pages [21] -->
m

<!-- b005722 | furniture | pages [21] -->
m

<!-- b005723 | furniture | pages [21] -->
m

<!-- b005724 | furniture | pages [21] -->
m

<!-- b005725 | furniture | pages [21] -->
m

<!-- b005726 | furniture | pages [21] -->
m

<!-- b005727 | furniture | pages [21] -->
m

<!-- b005728 | furniture | pages [21] -->
m

<!-- b005729 | furniture | pages [21] -->
m

<!-- b005730 | furniture | pages [21] -->
m

<!-- b005731 | furniture | pages [21] -->
m

<!-- b005732 | furniture | pages [21] -->
m

<!-- b005733 | furniture | pages [21] -->
m

<!-- b005734 | furniture | pages [21] -->
m

<!-- b005735 | furniture | pages [21] -->
m

<!-- b005736 | furniture | pages [21] -->
m

<!-- b005737 | furniture | pages [21] -->
m

<!-- b005738 | furniture | pages [21] -->
m

<!-- b005739 | furniture | pages [21] -->
m

<!-- b005740 | furniture | pages [21] -->
m

<!-- b005741 | furniture | pages [21] -->
m

<!-- b005742 | furniture | pages [21] -->
m

<!-- b005743 | furniture | pages [21] -->
m

<!-- b005744 | furniture | pages [21] -->
m

<!-- b005745 | furniture | pages [21] -->
m

<!-- b005746 | furniture | pages [21] -->
m

<!-- b005747 | furniture | pages [21] -->
m

<!-- b005748 | furniture | pages [21] -->
m

<!-- b005749 | furniture | pages [21] -->
m

<!-- b005750 | furniture | pages [21] -->
m

<!-- b005751 | furniture | pages [21] -->
m

<!-- b005752 | furniture | pages [21] -->
m

<!-- b005753 | furniture | pages [21] -->
m

<!-- b005754 | furniture | pages [21] -->
m

<!-- b005755 | furniture | pages [21] -->
m

<!-- b005756 | furniture | pages [21] -->
m

<!-- b005757 | furniture | pages [21] -->
m

<!-- b005758 | furniture | pages [21] -->
m

<!-- b005759 | furniture | pages [21] -->
m

<!-- b005760 | furniture | pages [21] -->
m

<!-- b005761 | furniture | pages [21] -->
m

<!-- b005762 | furniture | pages [21] -->
m

<!-- b005763 | furniture | pages [21] -->
m

<!-- b005764 | furniture | pages [21] -->
m

<!-- b005765 | furniture | pages [21] -->
m

<!-- b005766 | furniture | pages [21] -->
m

<!-- b005767 | furniture | pages [21] -->
m

<!-- b005768 | furniture | pages [21] -->
m

<!-- b005769 | furniture | pages [21] -->
m

<!-- b005770 | furniture | pages [21] -->
m

<!-- b005771 | furniture | pages [21] -->
m

<!-- b005772 | furniture | pages [21] -->
m

<!-- b005773 | furniture | pages [21] -->
m

<!-- b005774 | furniture | pages [21] -->
m

<!-- b005775 | furniture | pages [21] -->
m

<!-- b005776 | furniture | pages [21] -->
m

<!-- b005777 | furniture | pages [21] -->
m

<!-- b005778 | furniture | pages [21] -->
m

<!-- b005779 | furniture | pages [21] -->
m

<!-- b005780 | furniture | pages [21] -->
m

<!-- b005781 | furniture | pages [21] -->
m

<!-- b005782 | furniture | pages [21] -->
m

<!-- b005783 | furniture | pages [21] -->
m

<!-- b005784 | furniture | pages [21] -->
m

<!-- b005785 | furniture | pages [21] -->
m

<!-- b005786 | furniture | pages [21] -->
m

<!-- b005787 | furniture | pages [21] -->
m

<!-- b005788 | furniture | pages [21] -->
m

<!-- b005789 | furniture | pages [21] -->
m

<!-- b005790 | furniture | pages [21] -->
m

<!-- b005791 | furniture | pages [21] -->
m

<!-- b005792 | furniture | pages [21] -->
m

<!-- b005793 | furniture | pages [21] -->
m

<!-- b005794 | furniture | pages [21] -->
m

<!-- b005795 | furniture | pages [21] -->
m

<!-- b005796 | furniture | pages [21] -->
m

<!-- b005797 | furniture | pages [21] -->
m

<!-- b005798 | furniture | pages [21] -->
m

<!-- b005799 | furniture | pages [21] -->
m

<!-- b005800 | furniture | pages [21] -->
m

<!-- b005801 | furniture | pages [21] -->
m

<!-- b005802 | furniture | pages [21] -->
m

<!-- b005803 | furniture | pages [21] -->
m

<!-- b005804 | furniture | pages [21] -->
m

<!-- b005805 | furniture | pages [21] -->
m

<!-- b005806 | furniture | pages [21] -->
m

<!-- b005807 | furniture | pages [21] -->
m

<!-- b005808 | furniture | pages [21] -->
m

<!-- b005809 | furniture | pages [21] -->
m

<!-- b005810 | furniture | pages [21] -->
m

<!-- b005811 | furniture | pages [21] -->
m

<!-- b005812 | furniture | pages [21] -->
m

<!-- b005813 | furniture | pages [21] -->
m

<!-- b005814 | furniture | pages [21] -->
m

<!-- b005815 | furniture | pages [21] -->
m

<!-- b005816 | furniture | pages [21] -->
m

<!-- b005817 | furniture | pages [21] -->
m

<!-- b005818 | furniture | pages [21] -->
m

<!-- b005819 | furniture | pages [21] -->
m

<!-- b005820 | furniture | pages [21] -->
m

<!-- b005821 | furniture | pages [21] -->
m

<!-- b005822 | furniture | pages [21] -->
m

<!-- b005823 | furniture | pages [21] -->
m

<!-- b005824 | furniture | pages [21] -->
m

<!-- b005825 | furniture | pages [21] -->
m

<!-- b005826 | furniture | pages [21] -->
m

<!-- b005827 | furniture | pages [21] -->
m

<!-- b005828 | furniture | pages [21] -->
m

<!-- b005829 | furniture | pages [21] -->
m

<!-- b005830 | furniture | pages [21] -->
m

<!-- b005831 | furniture | pages [22] -->
Team # 2500759

<!-- b005832 | prose | pages [22] -->
1. Predictive accuracy

<!-- b005833 | furniture | pages [22] -->
Page 22 of 26

<!-- b005834 | prose | pages [22] -->
Through 10-fold cross-validation and Bootstrap resampling, we obtained prediction intervals and confidence levels for both models. In the gold medal prediction model, the MSE of the test set was 6.83, and the RMSE was 2.61. Although these values were slightly higher compared to the training set, the MAE was 0.52, and the MAPE was 14.47%, indicating that the model’s accuracy remains acceptable for new data. The total medal prediction model showed more stable performance, with lower MSE and RMSE, indicating higher predictive accuracy. These results are summarized in Table 5.

<!-- b005835 | caption | pages [22] -->
Table 5: Model Evaluation Metrics

<!-- b005836 | prose | pages [22] -->
Gold Training Test Total Training Test 6.83 MSE 1.33 28.5 6.46 2.61 RMSE 1.16 5.34 2.54 0.52 MAE 1.49 3.68 1.04 14.47% MAPE 17.50%

<!-- b005837 | prose | pages [22] -->
2. Robustness evaluation

<!-- b005838 | prose | pages [22] -->
18.63% 16.13%

<!-- b005839 | prose | pages [22] -->
To assess the robustness of the model, we focused on the R² value and the R-squared line plot from 10-fold cross-validation, as shown in Figs. 17(a)-(b). The results showed that both the gold medal and total medal prediction models had R² values close to 1, indicating that the models fit the data well and demonstrate consistent performance across different datasets, showcasing strong generalizability.

<!-- b005840 | prose | pages [22] -->
(a) (b)

<!-- b005841 | caption | pages [22] -->
Figure 17: R2 Values Across 10-Fold Cross-Validation

<!-- b005842 | prose | pages [22] -->
7

<!-- b005843 | heading | pages [22] -->
Model Analysis

<!-- b005844 | prose | pages [22] -->
7.1

<!-- b005845 | heading | pages [22] -->
Strength

<!-- b005846 | prose | pages [22] -->
The innovation and advantages of this study lie in the development of a predictive model for Olympic medal counts by integrating the PCA-LSTM-enhanced XGBoost- Bootstrap algorithm. Additionally, it conducts a comprehensive validation of the model’s accuracy and stability through various statistical methods, while employing a DID frame- work to assess the impact of coaching changes on Olympic medal counts. This is specifi- cally reflected in the following aspects:

<!-- b005847 | prose | pages [22] -->
关注数学模型

<!-- b005848 | furniture | pages [22] -->
2

<!-- b005849 | furniture | pages [22] -->
MATHmodels

<!-- b005850 | furniture | pages [22] -->
获取更多资讯

<!-- b005851 | furniture | pages [23] -->
Team # 2500759

<!-- b005852 | furniture | pages [23] -->
Page 23 of 26

<!-- b005853 | prose | pages [23] -->
• The introduction of the Bootstrap resampling method facilitates confidence interval estimation for the predictive outcomes, quantifying the model’s uncertainty and bolstering the credibility of the results. Additionally, the application of parallel trend hypothesis testing ensures that the experimental and control groups exhibited consistent medal trend patterns prior to coaching changes, further enhancing the stability of the model and the accuracy of inferences.

<!-- b005854 | prose | pages [23] -->
• By integrating SHAP value analysis, this study conducts a thorough assessment of the contributions of different sports to medal counts, revealing key factors that in- fluence outcomes. Notably, when analyzing host nations, the findings illustrate the home advantage’s significant effect on medal totals, thereby enhancing the model’s interpretability and providing more actionable insights for decision-making.

<!-- b005855 | prose | pages [23] -->
• The use of the DID model allows for the evaluation of the causal effects of coach-

<!-- b005856 | prose | pages [23] -->
微信公众号：数学模型

<!-- b005857 | prose | pages [23] -->
ing changes on medal counts, providing an accurate quantification of the impact of such changes on Olympic performance and ensuring the reliability of causal in- ferences. Furthermore, the combination of PCA for dimensionality reduction and LSTM for trend modeling enhances the predictive accuracy of medal counts, show- casing strong modeling capabilities, particularly in addressing complex nonlinear relationships and time series data.

<!-- b005858 | prose | pages [23] -->
7.2

<!-- b005859 | heading | pages [23] -->
Weekness and Further Discussion

<!-- b005860 | prose | pages [23] -->
Our model has several limitations and incompatibilities. For instance, the computa- tional cost of the XGBoost and Bootstrap methods is relatively high, particularly when

<!-- b005861 | prose | pages [23] -->
微信号：MATHmodels

<!-- b005862 | prose | pages [23] -->
dealing with large datasets, which affects the model’s real-time applicability. Addition- ally, the application of PCA for dimensionality reduction may lead to information loss, thereby impacting the model’s performance in capturing complex relationships. While LSTM are capable of identifying trends, their predictive ability is limited when it comes to sudden events and drastic fluctuations, which reduces the robustness of the model. Fur- thermore, the DID model assumes that the impact of coaching changes on medal counts is linear; however, in reality, these effects may be nonlinear, resulting in a failure to ad- equately capture the complex relationships present in the data and affecting the accuracy of causal inferences.

<!-- b005863 | prose | pages [23] -->
Future improvements to the model focus on two key areas. First, the Olympic medal count prediction model will enhance its integration of fluctuations from the Games, po- litical factors, and athlete performance variations through advanced ensemble learning techniques. By optimizing weighted averaging and stacked modeling, the model will in- corporate a wider range of variables and improve short-term predictive accuracy via a robust real-time data update mechanism. The use of reinforcement learning will further strengthen its long-term forecasting abilities, enhancing adaptability to sudden events and policy changes, while also improving computational efficiency for better timeliness and accuracy in predictions. Second, the enhanced-DID model will merge differentiated im- pact analysis with deep learning techniques to refine medal predictions. By incorporating stochastic simulations, this model will dynamically adjust the effects of coaching changes on medal counts, significantly boosting its adaptability in fluctuating environments and improving overall predictive effectiveness.

<!-- b005864 | furniture | pages [24] -->
Team # 2500759

<!-- b005865 | prose | pages [24] -->
8

<!-- b005866 | heading | pages [24] -->
Memorandum

<!-- b005867 | prose | pages [24] -->
To: International Olympic Committee

<!-- b005868 | prose | pages [24] -->
From: Team #2500759

<!-- b005869 | furniture | pages [24] -->
Page 24 of 26

<!-- b005870 | prose | pages [24] -->
Subject: 2028 Olympics Medal Prediction and Insights

<!-- b005871 | prose | pages [24] -->
Date: January 26, 2025

<!-- b005872 | prose | pages [24] -->
Dear Members of International Olympic Committee,

<!-- b005873 | prose | pages [24] -->
We are pleased to submit our solution to the medal prediction model for the 2028 Los Angeles Summer Olympics. Our team developed this model based on the data from the 2024 Paris Olympics and additional background information, offering both precise medal predictions and valuable insights for improving Olympic performance.

<!-- b005874 | prose | pages [24] -->
To construct the model, we utilize historical medal data and employ a PCA-LSTM- enhanced XGBoost-Bootstrap approach for preliminary predictions. Subsequently, we adjust these predictions by considering the event configurations and competitive structures of the 2024 Olympic Games, analyzing how these factors influence the medal counts of

<!-- b005875 | prose | pages [24] -->
m

<!-- b005876 | prose | pages [24] -->
m

<!-- b005877 | prose | pages [24] -->
m

<!-- b005878 | prose | pages [24] -->
m

<!-- b005879 | prose | pages [24] -->
m

<!-- b005880 | prose | pages [24] -->
m

<!-- b005881 | prose | pages [24] -->
m

<!-- b005882 | prose | pages [24] -->
m

<!-- b005883 | prose | pages [24] -->
m

<!-- b005884 | prose | pages [24] -->
m

<!-- b005885 | prose | pages [24] -->
m

<!-- b005886 | prose | pages [24] -->
m

<!-- b005887 | prose | pages [24] -->
m

<!-- b005888 | prose | pages [24] -->
m

<!-- b005889 | prose | pages [24] -->
m

<!-- b005890 | prose | pages [24] -->
m

<!-- b005891 | prose | pages [24] -->
m

<!-- b005892 | prose | pages [24] -->
m

<!-- b005893 | prose | pages [24] -->
m

<!-- b005894 | prose | pages [24] -->
m

<!-- b005895 | prose | pages [24] -->
m

<!-- b005896 | prose | pages [24] -->
m

<!-- b005897 | prose | pages [24] -->
m m

<!-- b005898 | prose | pages [24] -->
m m

<!-- b005899 | prose | pages [24] -->
m m

<!-- b005900 | prose | pages [24] -->
m m

<!-- b005901 | prose | pages [24] -->
m

<!-- b005902 | prose | pages [24] -->
m

<!-- b005903 | prose | pages [24] -->
m

<!-- b005904 | prose | pages [24] -->
m

<!-- b005905 | prose | pages [24] -->
m

<!-- b005906 | prose | pages [24] -->
m

<!-- b005907 | prose | pages [24] -->
m

<!-- b005908 | prose | pages [24] -->
m

<!-- b005909 | prose | pages [24] -->
m

<!-- b005910 | prose | pages [24] -->
m

<!-- b005911 | prose | pages [24] -->
m m

<!-- b005912 | prose | pages [24] -->
m m

<!-- b005913 | prose | pages [24] -->
m m

<!-- b005914 | prose | pages [24] -->
m m

<!-- b005915 | prose | pages [24] -->
m

<!-- b005916 | prose | pages [24] -->
m

<!-- b005917 | prose | pages [24] -->
m

<!-- b005918 | prose | pages [24] -->
m

<!-- b005919 | prose | pages [24] -->
m

<!-- b005920 | prose | pages [24] -->
m

<!-- b005921 | prose | pages [24] -->
m

<!-- b005922 | prose | pages [24] -->
m

<!-- b005923 | prose | pages [24] -->
m

<!-- b005924 | prose | pages [24] -->
m m

<!-- b005925 | prose | pages [24] -->
m m

<!-- b005926 | prose | pages [24] -->
m

<!-- b005927 | prose | pages [24] -->
m

<!-- b005928 | prose | pages [24] -->
m

<!-- b005929 | prose | pages [24] -->
m

<!-- b005930 | prose | pages [24] -->
m

<!-- b005931 | prose | pages [24] -->
m

<!-- b005932 | prose | pages [24] -->
m

<!-- b005933 | prose | pages [24] -->
m

<!-- b005934 | prose | pages [24] -->
m m

<!-- b005935 | prose | pages [24] -->
m m

<!-- b005936 | prose | pages [24] -->
m m

<!-- b005937 | prose | pages [24] -->
m m

<!-- b005938 | prose | pages [24] -->
m

<!-- b005939 | prose | pages [24] -->
m

<!-- b005940 | prose | pages [24] -->
m

<!-- b005941 | prose | pages [24] -->
m

<!-- b005942 | prose | pages [24] -->
m

<!-- b005943 | prose | pages [24] -->
m

<!-- b005944 | prose | pages [24] -->
m

<!-- b005945 | prose | pages [24] -->
m

<!-- b005946 | prose | pages [24] -->
m

<!-- b005947 | prose | pages [24] -->
m

<!-- b005948 | prose | pages [24] -->
different countries. To estimate the uncertainty in our predictions, we provide confidence

<!-- b005949 | prose | pages [24] -->
m

<!-- b005950 | prose | pages [24] -->
m

<!-- b005951 | prose | pages [24] -->
m

<!-- b005952 | prose | pages [24] -->
m

<!-- b005953 | prose | pages [24] -->
m

<!-- b005954 | prose | pages [24] -->
m

<!-- b005955 | prose | pages [24] -->
m

<!-- b005956 | prose | pages [24] -->
m

<!-- b005957 | prose | pages [24] -->
m

<!-- b005958 | prose | pages [24] -->
m

<!-- b005959 | prose | pages [24] -->
m

<!-- b005960 | prose | pages [24] -->
m

<!-- b005961 | prose | pages [24] -->
m

<!-- b005962 | prose | pages [24] -->
m

<!-- b005963 | prose | pages [24] -->
m

<!-- b005964 | prose | pages [24] -->
m

<!-- b005965 | prose | pages [24] -->
m

<!-- b005966 | prose | pages [24] -->
m

<!-- b005967 | prose | pages [24] -->
m

<!-- b005968 | prose | pages [24] -->
m

<!-- b005969 | prose | pages [24] -->
m

<!-- b005970 | prose | pages [24] -->
m

<!-- b005971 | prose | pages [24] -->
m

<!-- b005972 | prose | pages [24] -->
m

<!-- b005973 | prose | pages [24] -->
m

<!-- b005974 | prose | pages [24] -->
m

<!-- b005975 | prose | pages [24] -->
m

<!-- b005976 | prose | pages [24] -->
m

<!-- b005977 | prose | pages [24] -->
m

<!-- b005978 | prose | pages [24] -->
m

<!-- b005979 | prose | pages [24] -->
m

<!-- b005980 | prose | pages [24] -->
m

<!-- b005981 | prose | pages [24] -->
m

<!-- b005982 | prose | pages [24] -->
m

<!-- b005983 | prose | pages [24] -->
m

<!-- b005984 | prose | pages [24] -->
m

<!-- b005985 | prose | pages [24] -->
m

<!-- b005986 | prose | pages [24] -->
m

<!-- b005987 | prose | pages [24] -->
m m

<!-- b005988 | prose | pages [24] -->
m m

<!-- b005989 | prose | pages [24] -->
m m

<!-- b005990 | prose | pages [24] -->
m m

<!-- b005991 | prose | pages [24] -->
m

<!-- b005992 | prose | pages [24] -->
m

<!-- b005993 | prose | pages [24] -->
m

<!-- b005994 | prose | pages [24] -->
m

<!-- b005995 | prose | pages [24] -->
m

<!-- b005996 | prose | pages [24] -->
m

<!-- b005997 | prose | pages [24] -->
m

<!-- b005998 | prose | pages [24] -->
m

<!-- b005999 | prose | pages [24] -->
m

<!-- b006000 | prose | pages [24] -->
m

<!-- b006001 | prose | pages [24] -->
m

<!-- b006002 | prose | pages [24] -->
m

<!-- b006003 | prose | pages [24] -->
m m

<!-- b006004 | prose | pages [24] -->
m m

<!-- b006005 | prose | pages [24] -->
m m

<!-- b006006 | prose | pages [24] -->
m

<!-- b006007 | prose | pages [24] -->
m

<!-- b006008 | prose | pages [24] -->
m

<!-- b006009 | prose | pages [24] -->
m

<!-- b006010 | prose | pages [24] -->
m

<!-- b006011 | prose | pages [24] -->
m

<!-- b006012 | prose | pages [24] -->
m

<!-- b006013 | prose | pages [24] -->
m

<!-- b006014 | prose | pages [24] -->
m m

<!-- b006015 | prose | pages [24] -->
m m

<!-- b006016 | prose | pages [24] -->
m m

<!-- b006017 | prose | pages [24] -->
m

<!-- b006018 | prose | pages [24] -->
m

<!-- b006019 | prose | pages [24] -->
m

<!-- b006020 | prose | pages [24] -->
m

<!-- b006021 | prose | pages [24] -->
m

<!-- b006022 | prose | pages [24] -->
m

<!-- b006023 | prose | pages [24] -->
m

<!-- b006024 | prose | pages [24] -->
m

<!-- b006025 | prose | pages [24] -->
m

<!-- b006026 | prose | pages [24] -->
m

<!-- b006027 | prose | pages [24] -->
m

<!-- b006028 | prose | pages [24] -->
m m

<!-- b006029 | prose | pages [24] -->
m m

<!-- b006030 | prose | pages [24] -->
m m

<!-- b006031 | prose | pages [24] -->
m m

<!-- b006032 | prose | pages [24] -->
m

<!-- b006033 | prose | pages [24] -->
m

<!-- b006034 | prose | pages [24] -->
m

<!-- b006035 | prose | pages [24] -->
m

<!-- b006036 | prose | pages [24] -->
m

<!-- b006037 | prose | pages [24] -->
m

<!-- b006038 | prose | pages [24] -->
m

<!-- b006039 | prose | pages [24] -->
m

<!-- b006040 | prose | pages [24] -->
m

<!-- b006041 | prose | pages [24] -->
m

<!-- b006042 | prose | pages [24] -->
m m

<!-- b006043 | prose | pages [24] -->
m m

<!-- b006044 | prose | pages [24] -->
m m

<!-- b006045 | prose | pages [24] -->
m m

<!-- b006046 | prose | pages [24] -->
m

<!-- b006047 | prose | pages [24] -->
m

<!-- b006048 | prose | pages [24] -->
m

<!-- b006049 | prose | pages [24] -->
m

<!-- b006050 | prose | pages [24] -->
m

<!-- b006051 | prose | pages [24] -->
m

<!-- b006052 | prose | pages [24] -->
m

<!-- b006053 | prose | pages [24] -->
m

<!-- b006054 | prose | pages [24] -->
m

<!-- b006055 | prose | pages [24] -->
m

<!-- b006056 | prose | pages [24] -->
m

<!-- b006057 | prose | pages [24] -->
m

<!-- b006058 | prose | pages [24] -->
m

<!-- b006059 | prose | pages [24] -->
m m

<!-- b006060 | prose | pages [24] -->
m m

<!-- b006061 | prose | pages [24] -->
m m

<!-- b006062 | prose | pages [24] -->
m m

<!-- b006063 | prose | pages [24] -->
m

<!-- b006064 | prose | pages [24] -->
m

<!-- b006065 | prose | pages [24] -->
m

<!-- b006066 | prose | pages [24] -->
m

<!-- b006067 | prose | pages [24] -->
m

<!-- b006068 | prose | pages [24] -->
m

<!-- b006069 | prose | pages [24] -->
m

<!-- b006070 | prose | pages [24] -->
m

<!-- b006071 | prose | pages [24] -->
m

<!-- b006072 | prose | pages [24] -->
m

<!-- b006073 | prose | pages [24] -->
m

<!-- b006074 | prose | pages [24] -->
m

<!-- b006075 | prose | pages [24] -->
m m

<!-- b006076 | prose | pages [24] -->
m m

<!-- b006077 | prose | pages [24] -->
m m

<!-- b006078 | prose | pages [24] -->
m m

<!-- b006079 | prose | pages [24] -->
m m

<!-- b006080 | prose | pages [24] -->
m m

<!-- b006081 | prose | pages [24] -->
m

<!-- b006082 | prose | pages [24] -->
m

<!-- b006083 | prose | pages [24] -->
m

<!-- b006084 | prose | pages [24] -->
m

<!-- b006085 | prose | pages [24] -->
m

<!-- b006086 | prose | pages [24] -->
m

<!-- b006087 | prose | pages [24] -->
m

<!-- b006088 | prose | pages [24] -->
m

<!-- b006089 | prose | pages [24] -->
m

<!-- b006090 | prose | pages [24] -->
m

<!-- b006091 | prose | pages [24] -->
m m

<!-- b006092 | prose | pages [24] -->
m m

<!-- b006093 | prose | pages [24] -->
m m

<!-- b006094 | prose | pages [24] -->
m

<!-- b006095 | prose | pages [24] -->
m

<!-- b006096 | prose | pages [24] -->
m

<!-- b006097 | prose | pages [24] -->
m

<!-- b006098 | prose | pages [24] -->
m

<!-- b006099 | prose | pages [24] -->
m

<!-- b006100 | prose | pages [24] -->
m

<!-- b006101 | prose | pages [24] -->
m

<!-- b006102 | prose | pages [24] -->
m

<!-- b006103 | prose | pages [24] -->
m

<!-- b006104 | prose | pages [24] -->
m

<!-- b006105 | prose | pages [24] -->
m

<!-- b006106 | prose | pages [24] -->
m

<!-- b006107 | prose | pages [24] -->
intervals for gold medals and total medal counts.

<!-- b006108 | prose | pages [24] -->
m

<!-- b006109 | prose | pages [24] -->
m

<!-- b006110 | prose | pages [24] -->
m

<!-- b006111 | prose | pages [24] -->
m

<!-- b006112 | prose | pages [24] -->
m

<!-- b006113 | prose | pages [24] -->
m

<!-- b006114 | prose | pages [24] -->
m

<!-- b006115 | prose | pages [24] -->
m

<!-- b006116 | prose | pages [24] -->
m

<!-- b006117 | prose | pages [24] -->
m

<!-- b006118 | prose | pages [24] -->
m

<!-- b006119 | prose | pages [24] -->
m

<!-- b006120 | prose | pages [24] -->
m

<!-- b006121 | prose | pages [24] -->
m

<!-- b006122 | prose | pages [24] -->
m

<!-- b006123 | prose | pages [24] -->
m

<!-- b006124 | prose | pages [24] -->
m

<!-- b006125 | prose | pages [24] -->
m

<!-- b006126 | prose | pages [24] -->
m

<!-- b006127 | prose | pages [24] -->
m

<!-- b006128 | prose | pages [24] -->
m

<!-- b006129 | prose | pages [24] -->
m

<!-- b006130 | prose | pages [24] -->
m

<!-- b006131 | prose | pages [24] -->
m

<!-- b006132 | prose | pages [24] -->
m

<!-- b006133 | prose | pages [24] -->
m

<!-- b006134 | prose | pages [24] -->
m

<!-- b006135 | prose | pages [24] -->
m

<!-- b006136 | prose | pages [24] -->
m

<!-- b006137 | prose | pages [24] -->
m

<!-- b006138 | prose | pages [24] -->
m

<!-- b006139 | prose | pages [24] -->
m

<!-- b006140 | prose | pages [24] -->
m

<!-- b006141 | prose | pages [24] -->
m

<!-- b006142 | prose | pages [24] -->
m

<!-- b006143 | prose | pages [24] -->
m

<!-- b006144 | prose | pages [24] -->
m

<!-- b006145 | prose | pages [24] -->
m

<!-- b006146 | prose | pages [24] -->
m

<!-- b006147 | prose | pages [24] -->
m

<!-- b006148 | prose | pages [24] -->
m

<!-- b006149 | prose | pages [24] -->
m

<!-- b006150 | prose | pages [24] -->
m

<!-- b006151 | prose | pages [24] -->
m

<!-- b006152 | prose | pages [24] -->
m

<!-- b006153 | prose | pages [24] -->
m

<!-- b006154 | prose | pages [24] -->
m

<!-- b006155 | prose | pages [24] -->
m

<!-- b006156 | prose | pages [24] -->
m

<!-- b006157 | prose | pages [24] -->
m

<!-- b006158 | prose | pages [24] -->
m

<!-- b006159 | prose | pages [24] -->
m m

<!-- b006160 | prose | pages [24] -->
m

<!-- b006161 | prose | pages [24] -->
m

<!-- b006162 | prose | pages [24] -->
m

<!-- b006163 | prose | pages [24] -->
m

<!-- b006164 | prose | pages [24] -->
m

<!-- b006165 | prose | pages [24] -->
m

<!-- b006166 | prose | pages [24] -->
m

<!-- b006167 | prose | pages [24] -->
m

<!-- b006168 | prose | pages [24] -->
m

<!-- b006169 | prose | pages [24] -->
m

<!-- b006170 | prose | pages [24] -->
m m

<!-- b006171 | prose | pages [24] -->
m m

<!-- b006172 | prose | pages [24] -->
m m

<!-- b006173 | prose | pages [24] -->
m m

<!-- b006174 | prose | pages [24] -->
m m

<!-- b006175 | prose | pages [24] -->
m

<!-- b006176 | prose | pages [24] -->
m

<!-- b006177 | prose | pages [24] -->
m

<!-- b006178 | prose | pages [24] -->
m

<!-- b006179 | prose | pages [24] -->
m

<!-- b006180 | prose | pages [24] -->
m

<!-- b006181 | prose | pages [24] -->
m

<!-- b006182 | prose | pages [24] -->
m

<!-- b006183 | prose | pages [24] -->
m

<!-- b006184 | prose | pages [24] -->
m

<!-- b006185 | prose | pages [24] -->
m m

<!-- b006186 | prose | pages [24] -->
m m

<!-- b006187 | prose | pages [24] -->
m m

<!-- b006188 | prose | pages [24] -->
m

<!-- b006189 | prose | pages [24] -->
m

<!-- b006190 | prose | pages [24] -->
m

<!-- b006191 | prose | pages [24] -->
m

<!-- b006192 | prose | pages [24] -->
m

<!-- b006193 | prose | pages [24] -->
m

<!-- b006194 | prose | pages [24] -->
m

<!-- b006195 | prose | pages [24] -->
m

<!-- b006196 | prose | pages [24] -->
m

<!-- b006197 | prose | pages [24] -->
m

<!-- b006198 | prose | pages [24] -->
m

<!-- b006199 | prose | pages [24] -->
m

<!-- b006200 | prose | pages [24] -->
m

<!-- b006201 | prose | pages [24] -->
m

<!-- b006202 | prose | pages [24] -->
m

<!-- b006203 | prose | pages [24] -->
m m

<!-- b006204 | prose | pages [24] -->
m m

<!-- b006205 | prose | pages [24] -->
m

<!-- b006206 | prose | pages [24] -->
m

<!-- b006207 | prose | pages [24] -->
m

<!-- b006208 | prose | pages [24] -->
m

<!-- b006209 | prose | pages [24] -->
m

<!-- b006210 | prose | pages [24] -->
m

<!-- b006211 | prose | pages [24] -->
m m

<!-- b006212 | prose | pages [24] -->
m m

<!-- b006213 | prose | pages [24] -->
m m

<!-- b006214 | prose | pages [24] -->
m

<!-- b006215 | prose | pages [24] -->
m

<!-- b006216 | prose | pages [24] -->
m

<!-- b006217 | prose | pages [24] -->
m

<!-- b006218 | prose | pages [24] -->
m

<!-- b006219 | prose | pages [24] -->
m

<!-- b006220 | prose | pages [24] -->
m

<!-- b006221 | prose | pages [24] -->
m

<!-- b006222 | prose | pages [24] -->
m m

<!-- b006223 | prose | pages [24] -->
m m

<!-- b006224 | prose | pages [24] -->
m m

<!-- b006225 | prose | pages [24] -->
m m

<!-- b006226 | prose | pages [24] -->
m

<!-- b006227 | prose | pages [24] -->
m

<!-- b006228 | prose | pages [24] -->
m

<!-- b006229 | prose | pages [24] -->
m

<!-- b006230 | prose | pages [24] -->
m

<!-- b006231 | prose | pages [24] -->
m

<!-- b006232 | prose | pages [24] -->
m

<!-- b006233 | prose | pages [24] -->
m

<!-- b006234 | prose | pages [24] -->
m

<!-- b006235 | prose | pages [24] -->
m

<!-- b006236 | prose | pages [24] -->
m

<!-- b006237 | prose | pages [24] -->
m m

<!-- b006238 | prose | pages [24] -->
m

<!-- b006239 | prose | pages [24] -->
m

<!-- b006240 | prose | pages [24] -->
m

<!-- b006241 | prose | pages [24] -->
m

<!-- b006242 | prose | pages [24] -->
m

<!-- b006243 | prose | pages [24] -->
m

<!-- b006244 | prose | pages [24] -->
m

<!-- b006245 | prose | pages [24] -->
m

<!-- b006246 | prose | pages [24] -->
m

<!-- b006247 | prose | pages [24] -->
m

<!-- b006248 | prose | pages [24] -->
m m

<!-- b006249 | prose | pages [24] -->
m m

<!-- b006250 | prose | pages [24] -->
m m

<!-- b006251 | prose | pages [24] -->
m m

<!-- b006252 | prose | pages [24] -->
m m

<!-- b006253 | prose | pages [24] -->
m

<!-- b006254 | prose | pages [24] -->
m

<!-- b006255 | prose | pages [24] -->
m

<!-- b006256 | prose | pages [24] -->
m

<!-- b006257 | prose | pages [24] -->
m

<!-- b006258 | prose | pages [24] -->
m

<!-- b006259 | prose | pages [24] -->
m

<!-- b006260 | prose | pages [24] -->
m

<!-- b006261 | prose | pages [24] -->
m

<!-- b006262 | prose | pages [24] -->
m

<!-- b006263 | prose | pages [24] -->
m

<!-- b006264 | prose | pages [24] -->
m

<!-- b006265 | prose | pages [24] -->
m m

<!-- b006266 | prose | pages [24] -->
m m

<!-- b006267 | prose | pages [24] -->
m m

<!-- b006268 | prose | pages [24] -->
m m

<!-- b006269 | prose | pages [24] -->
m

<!-- b006270 | prose | pages [24] -->
m

<!-- b006271 | prose | pages [24] -->
m

<!-- b006272 | prose | pages [24] -->
m

<!-- b006273 | prose | pages [24] -->
m

<!-- b006274 | prose | pages [24] -->
m

<!-- b006275 | prose | pages [24] -->
m

<!-- b006276 | prose | pages [24] -->
m

<!-- b006277 | prose | pages [24] -->
m

<!-- b006278 | prose | pages [24] -->
m m

<!-- b006279 | prose | pages [24] -->
m m

<!-- b006280 | prose | pages [24] -->
m m

<!-- b006281 | prose | pages [24] -->
m

<!-- b006282 | prose | pages [24] -->
m

<!-- b006283 | prose | pages [24] -->
m

<!-- b006284 | prose | pages [24] -->
m

<!-- b006285 | prose | pages [24] -->
m

<!-- b006286 | prose | pages [24] -->
m

<!-- b006287 | prose | pages [24] -->
m

<!-- b006288 | prose | pages [24] -->
m

<!-- b006289 | prose | pages [24] -->
m

<!-- b006290 | prose | pages [24] -->
m

<!-- b006291 | prose | pages [24] -->
m

<!-- b006292 | prose | pages [24] -->
m

<!-- b006293 | prose | pages [24] -->
m

<!-- b006294 | prose | pages [24] -->
m

<!-- b006295 | prose | pages [24] -->
m m

<!-- b006296 | prose | pages [24] -->
m m

<!-- b006297 | prose | pages [24] -->
m m

<!-- b006298 | prose | pages [24] -->
m

<!-- b006299 | prose | pages [24] -->
m

<!-- b006300 | prose | pages [24] -->
m

<!-- b006301 | prose | pages [24] -->
m

<!-- b006302 | prose | pages [24] -->
m

<!-- b006303 | prose | pages [24] -->
m

<!-- b006304 | prose | pages [24] -->
m

<!-- b006305 | prose | pages [24] -->
m

<!-- b006306 | prose | pages [24] -->
m

<!-- b006307 | prose | pages [24] -->
m

<!-- b006308 | prose | pages [24] -->
m

<!-- b006309 | prose | pages [24] -->
m

<!-- b006310 | prose | pages [24] -->
m m

<!-- b006311 | prose | pages [24] -->
m m

<!-- b006312 | prose | pages [24] -->
m m

<!-- b006313 | prose | pages [24] -->
m m

<!-- b006314 | prose | pages [24] -->
m

<!-- b006315 | prose | pages [24] -->
m

<!-- b006316 | prose | pages [24] -->
m

<!-- b006317 | prose | pages [24] -->
m

<!-- b006318 | prose | pages [24] -->
m

<!-- b006319 | prose | pages [24] -->
m

<!-- b006320 | prose | pages [24] -->
m

<!-- b006321 | prose | pages [24] -->
m

<!-- b006322 | prose | pages [24] -->
An essential component of our model is the analysis of the "great coach" effect,

<!-- b006323 | prose | pages [24] -->
m

<!-- b006324 | prose | pages [24] -->
m

<!-- b006325 | prose | pages [24] -->
m

<!-- b006326 | prose | pages [24] -->
m

<!-- b006327 | prose | pages [24] -->
m

<!-- b006328 | prose | pages [24] -->
m

<!-- b006329 | prose | pages [24] -->
m

<!-- b006330 | prose | pages [24] -->
m

<!-- b006331 | prose | pages [24] -->
m

<!-- b006332 | prose | pages [24] -->
m

<!-- b006333 | prose | pages [24] -->
m

<!-- b006334 | prose | pages [24] -->
m

<!-- b006335 | prose | pages [24] -->
m

<!-- b006336 | prose | pages [24] -->
m

<!-- b006337 | prose | pages [24] -->
m

<!-- b006338 | prose | pages [24] -->
m

<!-- b006339 | prose | pages [24] -->
m

<!-- b006340 | prose | pages [24] -->
m

<!-- b006341 | prose | pages [24] -->
m

<!-- b006342 | prose | pages [24] -->
m

<!-- b006343 | prose | pages [24] -->
m

<!-- b006344 | prose | pages [24] -->
m

<!-- b006345 | prose | pages [24] -->
m

<!-- b006346 | prose | pages [24] -->
m

<!-- b006347 | prose | pages [24] -->
m

<!-- b006348 | prose | pages [24] -->
m

<!-- b006349 | prose | pages [24] -->
m

<!-- b006350 | prose | pages [24] -->
m

<!-- b006351 | prose | pages [24] -->
m

<!-- b006352 | prose | pages [24] -->
m

<!-- b006353 | prose | pages [24] -->
m

<!-- b006354 | prose | pages [24] -->
m m

<!-- b006355 | prose | pages [24] -->
m m

<!-- b006356 | prose | pages [24] -->
m m

<!-- b006357 | prose | pages [24] -->
m m

<!-- b006358 | prose | pages [24] -->
m m

<!-- b006359 | prose | pages [24] -->
m

<!-- b006360 | prose | pages [24] -->
m

<!-- b006361 | prose | pages [24] -->
m

<!-- b006362 | prose | pages [24] -->
m

<!-- b006363 | prose | pages [24] -->
m

<!-- b006364 | prose | pages [24] -->
m

<!-- b006365 | prose | pages [24] -->
m

<!-- b006366 | prose | pages [24] -->
m

<!-- b006367 | prose | pages [24] -->
m

<!-- b006368 | prose | pages [24] -->
m

<!-- b006369 | prose | pages [24] -->
m

<!-- b006370 | prose | pages [24] -->
m m

<!-- b006371 | prose | pages [24] -->
m m

<!-- b006372 | prose | pages [24] -->
m

<!-- b006373 | prose | pages [24] -->
m

<!-- b006374 | prose | pages [24] -->
m

<!-- b006375 | prose | pages [24] -->
m

<!-- b006376 | prose | pages [24] -->
m

<!-- b006377 | prose | pages [24] -->
m

<!-- b006378 | prose | pages [24] -->
m

<!-- b006379 | prose | pages [24] -->
m m

<!-- b006380 | prose | pages [24] -->
m m

<!-- b006381 | prose | pages [24] -->
m m

<!-- b006382 | prose | pages [24] -->
m m

<!-- b006383 | prose | pages [24] -->
m

<!-- b006384 | prose | pages [24] -->
m

<!-- b006385 | prose | pages [24] -->
m

<!-- b006386 | prose | pages [24] -->
m

<!-- b006387 | prose | pages [24] -->
m

<!-- b006388 | prose | pages [24] -->
m

<!-- b006389 | prose | pages [24] -->
m

<!-- b006390 | prose | pages [24] -->
m

<!-- b006391 | prose | pages [24] -->
m m

<!-- b006392 | prose | pages [24] -->
m

<!-- b006393 | prose | pages [24] -->
m

<!-- b006394 | prose | pages [24] -->
m

<!-- b006395 | prose | pages [24] -->
m

<!-- b006396 | prose | pages [24] -->
m

<!-- b006397 | prose | pages [24] -->
m

<!-- b006398 | prose | pages [24] -->
m

<!-- b006399 | prose | pages [24] -->
m

<!-- b006400 | prose | pages [24] -->
m

<!-- b006401 | prose | pages [24] -->
m

<!-- b006402 | prose | pages [24] -->
m

<!-- b006403 | prose | pages [24] -->
m

<!-- b006404 | prose | pages [24] -->
m m

<!-- b006405 | prose | pages [24] -->
m m

<!-- b006406 | prose | pages [24] -->
m

<!-- b006407 | prose | pages [24] -->
m

<!-- b006408 | prose | pages [24] -->
m

<!-- b006409 | prose | pages [24] -->
m

<!-- b006410 | prose | pages [24] -->
m

<!-- b006411 | prose | pages [24] -->
m

<!-- b006412 | prose | pages [24] -->
m

<!-- b006413 | prose | pages [24] -->
m

<!-- b006414 | prose | pages [24] -->
m

<!-- b006415 | prose | pages [24] -->
m

<!-- b006416 | prose | pages [24] -->
m

<!-- b006417 | prose | pages [24] -->
m

<!-- b006418 | prose | pages [24] -->
m m

<!-- b006419 | prose | pages [24] -->
m m

<!-- b006420 | prose | pages [24] -->
m m

<!-- b006421 | prose | pages [24] -->
m m

<!-- b006422 | prose | pages [24] -->
m

<!-- b006423 | prose | pages [24] -->
m

<!-- b006424 | prose | pages [24] -->
m

<!-- b006425 | prose | pages [24] -->
m

<!-- b006426 | prose | pages [24] -->
m

<!-- b006427 | prose | pages [24] -->
m m

<!-- b006428 | prose | pages [24] -->
m m

<!-- b006429 | prose | pages [24] -->
m m

<!-- b006430 | prose | pages [24] -->
m m

<!-- b006431 | prose | pages [24] -->
m

<!-- b006432 | prose | pages [24] -->
m

<!-- b006433 | prose | pages [24] -->
m

<!-- b006434 | prose | pages [24] -->
m

<!-- b006435 | prose | pages [24] -->
m

<!-- b006436 | prose | pages [24] -->
m

<!-- b006437 | prose | pages [24] -->
m

<!-- b006438 | prose | pages [24] -->
m

<!-- b006439 | prose | pages [24] -->
m

<!-- b006440 | prose | pages [24] -->
m

<!-- b006441 | prose | pages [24] -->
m

<!-- b006442 | prose | pages [24] -->
m

<!-- b006443 | prose | pages [24] -->
m

<!-- b006444 | prose | pages [24] -->
which we integrate using the DID model. By comparing countries with and without

<!-- b006445 | prose | pages [24] -->
m

<!-- b006446 | prose | pages [24] -->
m

<!-- b006447 | prose | pages [24] -->
m

<!-- b006448 | prose | pages [24] -->
m

<!-- b006449 | prose | pages [24] -->
m

<!-- b006450 | prose | pages [24] -->
m

<!-- b006451 | prose | pages [24] -->
m

<!-- b006452 | prose | pages [24] -->
m

<!-- b006453 | prose | pages [24] -->
m

<!-- b006454 | prose | pages [24] -->
m

<!-- b006455 | prose | pages [24] -->
m

<!-- b006456 | prose | pages [24] -->
m

<!-- b006457 | prose | pages [24] -->
m

<!-- b006458 | prose | pages [24] -->
m

<!-- b006459 | prose | pages [24] -->
m

<!-- b006460 | prose | pages [24] -->
m

<!-- b006461 | prose | pages [24] -->
m

<!-- b006462 | prose | pages [24] -->
m

<!-- b006463 | prose | pages [24] -->
m

<!-- b006464 | prose | pages [24] -->
m

<!-- b006465 | prose | pages [24] -->
m

<!-- b006466 | prose | pages [24] -->
m

<!-- b006467 | prose | pages [24] -->
m

<!-- b006468 | prose | pages [24] -->
m

<!-- b006469 | prose | pages [24] -->
m

<!-- b006470 | prose | pages [24] -->
m

<!-- b006471 | prose | pages [24] -->
m

<!-- b006472 | prose | pages [24] -->
m

<!-- b006473 | prose | pages [24] -->
m

<!-- b006474 | prose | pages [24] -->
m

<!-- b006475 | prose | pages [24] -->
m

<!-- b006476 | prose | pages [24] -->
m

<!-- b006477 | prose | pages [24] -->
m

<!-- b006478 | prose | pages [24] -->
m

<!-- b006479 | prose | pages [24] -->
m

<!-- b006480 | prose | pages [24] -->
m m

<!-- b006481 | prose | pages [24] -->
m m

<!-- b006482 | prose | pages [24] -->
m m

<!-- b006483 | prose | pages [24] -->
m

<!-- b006484 | prose | pages [24] -->
m

<!-- b006485 | prose | pages [24] -->
m

<!-- b006486 | prose | pages [24] -->
m

<!-- b006487 | prose | pages [24] -->
m

<!-- b006488 | prose | pages [24] -->
m

<!-- b006489 | prose | pages [24] -->
m

<!-- b006490 | prose | pages [24] -->
m

<!-- b006491 | prose | pages [24] -->
m

<!-- b006492 | prose | pages [24] -->
m

<!-- b006493 | prose | pages [24] -->
m

<!-- b006494 | prose | pages [24] -->
m m

<!-- b006495 | prose | pages [24] -->
m m

<!-- b006496 | prose | pages [24] -->
m m

<!-- b006497 | prose | pages [24] -->
m m

<!-- b006498 | prose | pages [24] -->
m

<!-- b006499 | prose | pages [24] -->
m

<!-- b006500 | prose | pages [24] -->
m

<!-- b006501 | prose | pages [24] -->
m

<!-- b006502 | prose | pages [24] -->
m

<!-- b006503 | prose | pages [24] -->
m

<!-- b006504 | prose | pages [24] -->
m

<!-- b006505 | prose | pages [24] -->
m

<!-- b006506 | prose | pages [24] -->
m

<!-- b006507 | prose | pages [24] -->
m

<!-- b006508 | prose | pages [24] -->
m

<!-- b006509 | prose | pages [24] -->
m

<!-- b006510 | prose | pages [24] -->
m

<!-- b006511 | prose | pages [24] -->
m

<!-- b006512 | prose | pages [24] -->
m

<!-- b006513 | prose | pages [24] -->
m m

<!-- b006514 | prose | pages [24] -->
m m

<!-- b006515 | prose | pages [24] -->
m

<!-- b006516 | prose | pages [24] -->
m

<!-- b006517 | prose | pages [24] -->
m

<!-- b006518 | prose | pages [24] -->
m

<!-- b006519 | prose | pages [24] -->
m

<!-- b006520 | prose | pages [24] -->
m

<!-- b006521 | prose | pages [24] -->
m

<!-- b006522 | prose | pages [24] -->
m

<!-- b006523 | prose | pages [24] -->
m

<!-- b006524 | prose | pages [24] -->
m m

<!-- b006525 | prose | pages [24] -->
m m

<!-- b006526 | prose | pages [24] -->
m m

<!-- b006527 | prose | pages [24] -->
m

<!-- b006528 | prose | pages [24] -->
m

<!-- b006529 | prose | pages [24] -->
m

<!-- b006530 | prose | pages [24] -->
m

<!-- b006531 | prose | pages [24] -->
m

<!-- b006532 | prose | pages [24] -->
m

<!-- b006533 | prose | pages [24] -->
m

<!-- b006534 | prose | pages [24] -->
m

<!-- b006535 | prose | pages [24] -->
m

<!-- b006536 | prose | pages [24] -->
m

<!-- b006537 | prose | pages [24] -->
m m

<!-- b006538 | prose | pages [24] -->
m m

<!-- b006539 | prose | pages [24] -->
m

<!-- b006540 | prose | pages [24] -->
m

<!-- b006541 | prose | pages [24] -->
m

<!-- b006542 | prose | pages [24] -->
m

<!-- b006543 | prose | pages [24] -->
m

<!-- b006544 | prose | pages [24] -->
m

<!-- b006545 | prose | pages [24] -->
m

<!-- b006546 | prose | pages [24] -->
m

<!-- b006547 | prose | pages [24] -->
m

<!-- b006548 | prose | pages [24] -->
m

<!-- b006549 | prose | pages [24] -->
m

<!-- b006550 | prose | pages [24] -->
m m

<!-- b006551 | prose | pages [24] -->
m m

<!-- b006552 | prose | pages [24] -->
m m

<!-- b006553 | prose | pages [24] -->
m m

<!-- b006554 | prose | pages [24] -->
m

<!-- b006555 | prose | pages [24] -->
m

<!-- b006556 | prose | pages [24] -->
m

<!-- b006557 | prose | pages [24] -->
m

<!-- b006558 | prose | pages [24] -->
m

<!-- b006559 | prose | pages [24] -->
m

<!-- b006560 | prose | pages [24] -->
m

<!-- b006561 | prose | pages [24] -->
m

<!-- b006562 | prose | pages [24] -->
m

<!-- b006563 | prose | pages [24] -->
m

<!-- b006564 | prose | pages [24] -->
m

<!-- b006565 | prose | pages [24] -->
m

<!-- b006566 | prose | pages [24] -->
coaching changes, we estimate the incremental impact of coaching transitions on medal outcomes. We fit the model using OLS and conduct statistical significance tests as well as parallel trends tests to ensure the reliability of our results.

<!-- b006567 | prose | pages [24] -->
Beyond simply predicting medal counts, our model also offers insights on optimizing Olympic performance. It highlights which countries are likely to make breakthroughs in specific sports by strategically increasing investments in those areas. Furthermore, our model suggests potential improvements in the types and settings of Olympic events, recommending adjustments that could help maximize medal outcomes. These findings can guide the decision-making processes of National Olympic Committees as they plan for the 2028 Olympics and beyond.

<!-- b006568 | prose | pages [24] -->
Thank you for providing the opportunity to participate in this important project. We look forward to your valuable feedback.

<!-- b006569 | prose | pages [24] -->
Sincerely yours,

<!-- b006570 | furniture | pages [24] -->
Team #2500759

<!-- b006571 | prose | pages [24] -->
关注数学模型

<!-- b006572 | furniture | pages [24] -->
2

<!-- b006573 | furniture | pages [24] -->
MATHmodels

<!-- b006574 | furniture | pages [24] -->
获取更多资讯

<!-- b006575 | furniture | pages [25] -->
Team # 2500759

<!-- b006576 | furniture | pages [25] -->
Page 25 of 26

<!-- b006577 | heading | pages [25] -->
References

<!-- b006578 | references | pages [25] -->
[1] SM Khorshed Alam, Peiyue Li, Mahbubur Rahman, Misbah Fida, and Vetrimu-

<!-- b006579 | references | pages [25] -->
rugan Elumalai. Key factors affecting groundwater nitrate levels in the yinchuan

<!-- b006580 | references | pages [25] -->
region, northwest china: Research using the extreme gradient boosting (xgboost)

<!-- b006581 | references | pages [25] -->
model with the shapley additive explanations (shap) method. Environmental Pollu-

<!-- b006582 | references | pages [25] -->
tion, 364:125336, 2025.

<!-- b006583 | references | pages [25] -->
[2] Ruobing Chen, Mingxin Zhang, Xiao Xu, and Yongfeng Liu. Game-related statistics

<!-- b006584 | references | pages [25] -->
for distinguishing winning and losing teams in olympic basketball: The impact of

<!-- b006585 | references | pages [25] -->
game pace. Journal of Sports Sciences, pages 1–12, 2025.

<!-- b006586 | references | pages [25] -->
[3] Yuejian Chen, Xuemei Liu, Meng Rao, Yong Qin, Zhipeng Wang, and Yuanjin Ji.

<!-- b006587 | references | pages [25] -->
Explicit speed-integrated lstm network for non-stationary gearbox vibration repre-

<!-- b006588 | references | pages [25] -->
微信公众号：数学模型

<!-- b006589 | references | pages [25] -->
sentation and fault detection under varying speed conditions. Reliability Engineering

<!-- b006590 | references | pages [25] -->
& System Safety, 254:110596, 2025.

<!-- b006591 | references | pages [25] -->
[4] Andrew Goodman-Bacon. Difference-in-differences with variation in treatment tim-

<!-- b006592 | references | pages [25] -->
ing. Journal of econometrics, 225(2):254–277, 2021.

<!-- b006593 | references | pages [25] -->
[5] Jiangtao Li, Xingqin An, Qingyong Li, Chao Wang, Haomin Yu, Xinyuan Zhou, and

<!-- b006594 | references | pages [25] -->
Yangli-ao Geng. Application of xgboost algorithm in the optimization of pollutant

<!-- b006595 | references | pages [25] -->
concentration. Atmospheric Research, 276:106238, 2022.

<!-- b006596 | references | pages [25] -->
[6] Wenlong Liao, Shouxiang Wang, Dechang Yang, Zhe Yang, Jiannong Fang, Chris-

<!-- b006597 | references | pages [25] -->
微信号：MATHmodels

<!-- b006598 | references | pages [25] -->
tian Rehtanz, and Fernando Porté-Agel. Timegpt in load forecasting: A large time

<!-- b006599 | references | pages [25] -->
series model perspective. Applied Energy, 379:124973, 2025.

<!-- b006600 | references | pages [25] -->
[7] Benjamin Lindemann, Benjamin Maschler, Nada Sahlab, and Michael Weyrich. A

<!-- b006601 | references | pages [25] -->
survey on anomaly detection for technical systems using lstm networks. Computers

<!-- b006602 | references | pages [25] -->
in Industry, 131:103498, 2021.

<!-- b006603 | references | pages [25] -->
[8] Tui H Nolan, Jeff Goldsmith, and David Ruppert. Bayesian functional principal

<!-- b006604 | references | pages [25] -->
components analysis via variational message passing with multilevel extensions.

<!-- b006605 | references | pages [25] -->
Bayesian Analysis, 20(1):1459–1485, 2025.

<!-- b006606 | references | pages [25] -->
[9] Cheng-Hong Yang, Borcy Lee, Yi-In Lee, Yu-Fang Chung, and Yu-Da Lin. An

<!-- b006607 | references | pages [25] -->
autoencoder-based arithmetic optimization clustering algorithm to enhance principal

<!-- b006608 | references | pages [25] -->
component analysis to study the relations between industrial market stock indices in

<!-- b006609 | references | pages [25] -->
real estate. Expert Systems with Applications, 266:126165, 2025.

<!-- b006610 | references | pages [25] -->
[10] Junyi Zhang, Xianglong Ma, Jialan Zhang, Deliang Sun, Xinzhi Zhou, Changlin

<!-- b006611 | references | pages [25] -->
Mi, and Haijia Wen. Insights into geospatial heterogeneity of landslide suscepti-

<!-- b006612 | references | pages [25] -->
bility based on the shap-xgboost model. Journal of environmental management,

<!-- b006613 | references | pages [25] -->
332:117357, 2023.

<!-- b006614 | furniture | pages [26] -->
Team # 2500759

<!-- b006615 | furniture | pages [26] -->
Page 26 of 26

<!-- b006616 | heading | pages [26] -->
Report on Use of AI

<!-- b006617 | ai_disclosure | pages [26] -->
1. OpenAI ChatGPT (January 25, 2025 version, ChatGPT-4)

<!-- b006618 | ai_disclosure | pages [26] -->
Query1: How PCA does reducing dimensions?

<!-- b006619 | ai_disclosure | pages [26] -->
Output: Start with data normalization as this is a prerequisite for PCA. Next, cal-

<!-- b006620 | ai_disclosure | pages [26] -->
culate the covariance matrix or correlation matrix, this step is to capture the relationship

<!-- b006621 | ai_disclosure | pages [26] -->
between variables. Then, eigenvalue decomposition is performed, and choosing the num-

<!-- b006622 | ai_disclosure | pages [26] -->
ber of principal components is a key step. Finally, the data is projected into the new

<!-- b006623 | ai_disclosure | pages [26] -->
feature space, which is the reduced dimensionality.

<!-- b006624 | ai_disclosure | pages [26] -->
2. OpenAI ChatGPT (January 25, 2025 version, ChatGPT-4)

<!-- b006625 | ai_disclosure | pages [26] -->
Query2: How to use SHAP?

<!-- b006626 | ai_disclosure | pages [26] -->
Output: SHAP is a game theory-based method for interpreting the predictions of a

<!-- b006627 | ai_disclosure | pages [26] -->
model. It helps to understand how the model makes a certain prediction by calculating the

<!-- b006628 | ai_disclosure | pages [26] -->
contribution of each feature to the model output. Assuming you have installed the SHAP

<!-- b006629 | ai_disclosure | pages [26] -->
library, you next need to choose a model to interpret. For example, you can use a trained

<!-- b006630 | ai_disclosure | pages [26] -->
random forest model and then use SHAP to interpret its predictions. The steps might

<!-- b006631 | ai_disclosure | pages [26] -->
include: loading the data, training the model, creating a SHAP interpreter, calculating the

<!-- b006632 | ai_disclosure | pages [26] -->
SHAP values, and finally visualizing the results. When loading data, you need to make

<!-- b006633 | ai_disclosure | pages [26] -->
sure that the data is preprocessed, such as normalized or coded categorical variables. Then

<!-- b006634 | ai_disclosure | pages [26] -->
train the model, e.g. with a random forest classifier. After that, create an interpreter object

<!-- b006635 | ai_disclosure | pages [26] -->
for SHAP, which may need to be passed in the model and data. When calculating SHAP

<!-- b006636 | ai_disclosure | pages [26] -->
values, you may need to pass in test samples using the interpreter’s shap_values method.

<!-- b006637 | ai_disclosure | pages [26] -->
3. OpenAI ChatGPT (January 25, 2025 version, ChatGPT-4)

<!-- b006638 | ai_disclosure | pages [26] -->
Query3: How do you quantify the impact of the great coach effect?

<!-- b006639 | ai_disclosure | pages [26] -->
Output: Using the number of medals as the dependent variable, consider factors

<!-- b006640 | ai_disclosure | pages [26] -->
such as historical medal counts, host country advantage, number of athletes, economic

<!-- b006641 | ai_disclosure | pages [26] -->
indicators (if any), and whether or not to bring in good coaches (as a dummy variable).

<!-- b006642 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b006643 | furniture | pages [26] -->
2

<!-- b006644 | furniture | pages [26] -->
MATHmodels

<!-- b006645 | furniture | pages [26] -->
获取更多资讯
