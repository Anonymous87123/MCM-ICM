# P-B-2025-2504448-aa644b6e

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
B

<!-- b000006 | furniture | pages [1] -->
2504448

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
微信公众号：数学模型

<!-- b000009 | title | pages [1] -->
Sustainable Tourism Management in Juneau

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
Juneau, Alaska has become a popular tourist destination in recent years While tourism spurs economic growth, it also brings significant pressure on environment and local in- frastructure. To address this issue, we develop a multi-objective dynamic programming model that optimizes economic, environmental, and social outcomes for sustainable tourism management.

<!-- b000012 | title | pages [1] -->
微信号：MATHmodels

<!-- b000013 | prose | pages [1] -->
For Problem 1, we begin with a total tourist demand model, considering factors of nat- ural growth, seasonal variations, taxation effect, and government promotion. This model serves as an input to the three interconnected models. First, the economic model estimates profit by deducting operational costs from tourism revenue, both of which are assumed to scale linearly with tourist volume. Second, the environmental model quantifies tourism’s impact through an index aggregating key ecological factors of temperature, ocean temper- ature, snowfall, and ocean pH using entropy weight method. This environment model also accounts for natural recovery and government intervention. Third, the social im- pact model evaluates resident satisfaction based on their attitudes towards public service stress, environmental quality decrease, and tourism taxation.

<!-- b000014 | prose | pages [1] -->
The objective of our model is to maximize economic profit, environmental sustain- ability, and resident satisfaction under constraints of tourist capacity, environmental protection measures, and government budget limitations. We use dynamic program- ming to solve the model and stimulate the results over a 5-year period. Our model recom- mends a dynamic tax rate in a range of 3.2% to 5.0%, and a schema of government expen- ditures with large portions of environmental protection and infrastructure construction. Our results predict a stable tourist volume of around 1.6 million visitors per year. Both government revenue and environment quality rise steadily after implementing our rec-

<!-- b000015 | heading | pages [1] -->
ommended policies. Additionally, we perform a sensitivity analysis to identify the most

<!-- b000016 | prose | pages [1] -->
influential factors and assess the robustness of proposed policy measures.

<!-- b000017 | prose | pages [1] -->
For Problem 2, we further validate our model by adapting it to the tourism situation of Miami, another destination troubled by overtourism. Differences in culture, visitor behavior, and government intervention require adapation of parameters of our model.

<!-- b000018 | prose | pages [1] -->
For Problem 3, we prepare a memo for the tourism council of Juneau. Based on the predicted results given by our model, we summarize key findings and offer practical rec- ommendations to achieve sustainable tourism development.

<!-- b000019 | prose | pages [1] -->
In conclusion, our multi-objective dynamic programming model provides a compre- hensive framework for balancing economic, environmental, and social aspects of Juneau tourism. Our model has certain limitations to some extent, including potential uncertain- ties in data and simplifications made towards complex human-environment interactions. In future work, we could optimize our model using more granular data and refine our assumptions to further improve the model’s predictive capabilities.

<!-- b000020 | keywords | pages [1] -->
Keywords: Multi-Objective Model, Dynamic Programming, Sustainable Tourism

<!-- b000021 | furniture | pages [3] -->
Team # 2504448

<!-- b000022 | furniture | pages [3] -->
Page 3 of 25

<!-- b000023 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000024 | prose | pages [3] -->
1

<!-- b000025 | heading | pages [3] -->
Introduction

<!-- b000026 | prose | pages [3] -->
1.1 Problem Background

<!-- b000027 | prose | pages [3] -->
Juneau, Alaska has become a popular choice for visitors with its glacier, wild animals, museums, and historic districts. Local tourism has grown significantly in the past decades. This remote town with a population of about 30,000 set a record of 1.6 million cruise pas- sengers in 2023. While the huge number of tourists has brought unprecedented develop-

<!-- b000028 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000029 | prose | pages [3] -->
ment for the local economy, people should attach importance to the negative environmen- tal and social impacts simultaneously. Mendenhall Glacier has experienced rapid retreat, warning people of the costs of overtourism. Meanwhile, according to recent reports, the rising pressure on public services and the increased congestion in the transportation sys- tem are major concerns of local residents.

<!-- b000030 | caption | pages [3] -->
Figure 1: Retreat of Mendenhall Glacier and tourism-related concerns from Juneau residents

<!-- b000031 | prose | pages [3] -->
In order to restrict the development of overtourism, a few measures are enacted, in- cluding limiting the tourist capacity and increasing tourism taxes. These efforts serve as a start point for pursuing the sustainable tourism plan for Juneau in the long-term. It is imperative to figure out a more considerate approach to achieve an equilibrium between economic growth and social well-being.

<!-- b000032 | prose | pages [3] -->
1.2

<!-- b000033 | heading | pages [3] -->
Problem Restatement

<!-- b000034 | prose | pages [3] -->
The status quo in Juneau demands a solution to the ongoing issues regarding eco- nomic, environmental, and social aspects. Through in-depth investigation and analysis of

<!-- b000035 | prose | pages [3] -->
m

<!-- b000036 | prose | pages [3] -->
m

<!-- b000037 | prose | pages [3] -->
m

<!-- b000038 | prose | pages [3] -->
m

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
the problem’s context, the objectives are restated as follows:

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

<!-- b000723 | furniture | pages [4] -->
Team # 2504448

<!-- b000724 | furniture | pages [4] -->
Page 4 of 25

<!-- b000725 | prose | pages [4] -->
• Construct a model that takes into account both the economic benefits and hidden costs associated with tourism. Discuss a plan for government expenditures from additional revenues and demonstrate how these expenditures feed back into the model.

<!-- b000726 | prose | pages [4] -->
• Provide a sensitivity analysis for the model and identify the most important factors.

<!-- b000727 | prose | pages [4] -->
• Illustrate the adaptability of the model by applying it to another over-touristed desti- nation. Discuss which measures are most important in that context and demonstrate the application of the model on attractions and locations with fewer tourists.

<!-- b000728 | prose | pages [4] -->
• Write a memo summarizing the results of the model, including predictions, the ef- fects of different measures, and suggestions to promote sustainable tourism.

<!-- b000729 | prose | pages [4] -->
1.3 Our Work

<!-- b000730 | prose | pages [4] -->
The following figure describes our work in detail. We construct four models: total tourism demand model, economic benefit model, environmental impact model, and resi- dent satisfaction model. We go through a comprehensive process of preparing data, con- structing the models, analyzing the models, and discussing the results.

<!-- b000731 | caption | pages [4] -->
Figure 2: Flow chart of the work

<!-- b000732 | prose | pages [4] -->
2

<!-- b000733 | heading | pages [4] -->
Preparation of the Models

<!-- b000734 | prose | pages [4] -->
2.1

<!-- b000735 | heading | pages [4] -->
Assumptions

<!-- b000736 | prose | pages [4] -->
Several assumptions are made to provide a robust foundation for model construction and analysis.

<!-- b000737 | prose | pages [4] -->
关注数学模型

<!-- b000738 | furniture | pages [4] -->
2

<!-- b000739 | furniture | pages [4] -->
MATHmodels

<!-- b000740 | furniture | pages [4] -->
获取更多资讯

<!-- b000741 | furniture | pages [6] -->
Team # 2504448

<!-- b000742 | prose | pages [6] -->
2.3

<!-- b000743 | heading | pages [6] -->
Data Preparation

<!-- b000744 | furniture | pages [6] -->
Page 6 of 25

<!-- b000745 | prose | pages [6] -->
Before constructing our model, we collect data related to tourism in Juneau, Alaska from various reliable sources, including government reports, climate monitoring organi- zations, and tourism industry research.

<!-- b000746 | prose | pages [6] -->
The data used in this study is obtained from the following sources:

<!-- b000747 | prose | pages [6] -->
• Tourism Data: The number of tourists and tourism revenue figures are collected from the Alaska Travel Industry Association’s annual reports and the City and Bor- ough of Juneau’s 2023 Tourism Survey Report. These reports provide statistics on visitor volume, revenue generation, and public sentiment regarding tourism activi- ties.

<!-- b000748 | prose | pages [6] -->
• Environmental Data: Climate-change-related information, including average tem- perature, total annual snowfall, and ocean temperature, is obtained from the Na- tional Oceanic and Atmospheric Administration (NOAA) climate database and the Alaska Climate Research Center. These institutions monitor and provide historical climate data for the region.

<!-- b000749 | prose | pages [6] -->
• Social Impact Data: Resident feedback regarding tourism impacts, particularly neg- ative attitudes of residents, is collected from the CBJ Tourism Survey 2023, which assesses public opinions on the effects of rising tourist numbers on daily life and public services.

<!-- b000750 | caption | pages [6] -->
Table 2 presents a summary of key tourism and environmental statistics for Juneau

<!-- b000751 | prose | pages [6] -->
from 2019 to 2023, with statistics of 2020 and 2021 affected by pandemic. We do not elim- nate these outliners as they could help us to determine the environmental and social de- velopment without tourists.

<!-- b000752 | prose | pages [6] -->
Year Tourist

<!-- b000753 | prose | pages [6] -->
Tourism

<!-- b000754 | prose | pages [6] -->
Resident

<!-- b000755 | prose | pages [6] -->
count

<!-- b000756 | prose | pages [6] -->
revenue

<!-- b000757 | prose | pages [6] -->
negative

<!-- b000758 | prose | pages [6] -->
(mil-

<!-- b000759 | prose | pages [6] -->
(million

<!-- b000760 | prose | pages [6] -->
attitude

<!-- b000761 | prose | pages [6] -->
lion)

<!-- b000762 | prose | pages [6] -->
$)

<!-- b000763 | prose | pages [6] -->
(%)

<!-- b000764 | prose | pages [6] -->
m

<!-- b000765 | prose | pages [6] -->
m

<!-- b000766 | prose | pages [6] -->
m

<!-- b000767 | prose | pages [6] -->
m

<!-- b000768 | prose | pages [6] -->
m

<!-- b000769 | prose | pages [6] -->
m

<!-- b000770 | prose | pages [6] -->
m

<!-- b000771 | prose | pages [6] -->
m

<!-- b000772 | prose | pages [6] -->
m

<!-- b000773 | prose | pages [6] -->
m

<!-- b000774 | prose | pages [6] -->
m

<!-- b000775 | prose | pages [6] -->
m

<!-- b000776 | prose | pages [6] -->
m

<!-- b000777 | prose | pages [6] -->
m

<!-- b000778 | prose | pages [6] -->
m

<!-- b000779 | prose | pages [6] -->
m

<!-- b000780 | prose | pages [6] -->
m

<!-- b000781 | prose | pages [6] -->
m

<!-- b000782 | prose | pages [6] -->
m

<!-- b000783 | prose | pages [6] -->
m

<!-- b000784 | prose | pages [6] -->
m

<!-- b000785 | prose | pages [6] -->
m

<!-- b000786 | prose | pages [6] -->
m

<!-- b000787 | prose | pages [6] -->
m

<!-- b000788 | prose | pages [6] -->
m

<!-- b000789 | prose | pages [6] -->
m

<!-- b000790 | prose | pages [6] -->
m

<!-- b000791 | prose | pages [6] -->
m

<!-- b000792 | prose | pages [6] -->
m

<!-- b000793 | prose | pages [6] -->
m

<!-- b000794 | prose | pages [6] -->
m

<!-- b000795 | prose | pages [6] -->
m

<!-- b000796 | prose | pages [6] -->
m

<!-- b000797 | prose | pages [6] -->
m

<!-- b000798 | prose | pages [6] -->
m

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
2019 1.33 237 6

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
2020 0 0 0

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
2021 0.125 25.6 8

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
2022 1.20 301 7

<!-- b001455 | prose | pages [6] -->
2023 1.65 375 11

<!-- b001456 | prose | pages [6] -->
Average

<!-- b001457 | prose | pages [6] -->
Total

<!-- b001458 | prose | pages [6] -->
Average

<!-- b001459 | prose | pages [6] -->
Ocean

<!-- b001460 | prose | pages [6] -->
temper-

<!-- b001461 | prose | pages [6] -->
annual

<!-- b001462 | prose | pages [6] -->
ocean

<!-- b001463 | prose | pages [6] -->
pH

<!-- b001464 | prose | pages [6] -->
ature

<!-- b001465 | prose | pages [6] -->
snowfall

<!-- b001466 | prose | pages [6] -->
tempera-

<!-- b001467 | prose | pages [6] -->
level

<!-- b001468 | prose | pages [6] -->
(◦F)

<!-- b001469 | prose | pages [6] -->
ture (◦C)

<!-- b001470 | prose | pages [6] -->
(inches)

<!-- b001471 | prose | pages [6] -->
41.2 118.7 6.3 8.06

<!-- b001472 | prose | pages [6] -->
40.7 99.3 6.3 8.06

<!-- b001473 | prose | pages [6] -->
41.0 121.0 6.4 8.05

<!-- b001474 | prose | pages [6] -->
40.8 110.2 6.5 8.04

<!-- b001475 | prose | pages [6] -->
40.6 108.5 6.6 8.04

<!-- b001476 | caption | pages [6] -->
Table 2: Juneau tourism and environmental data (2019-2023)

<!-- b001477 | caption | pages [6] -->
Figure 3 provides a visual representation of the relationship between tourism revenue

<!-- b001478 | prose | pages [6] -->
and tourist volume over the years. The plot shows a strong positive correlation between

<!-- b001479 | prose | pages [6] -->
关注数学模型

<!-- b001480 | prose | pages [6] -->
tourist count and revenue, indicating a direct economic benefit from increased tourism.

<!-- b001481 | furniture | pages [6] -->
2

<!-- b001482 | furniture | pages [6] -->
MATHmodels

<!-- b001483 | furniture | pages [6] -->
获取更多资讯

<!-- b001484 | furniture | pages [7] -->
Team # 2504448

<!-- b001485 | furniture | pages [7] -->
Page 7 of 25

<!-- b001486 | prose | pages [7] -->
Tourism Revenue vs Tourist Count

<!-- b001487 | prose | pages [7] -->
Actual Data Fitted Values (Actual Domain)

<!-- b001488 | prose | pages [7] -->
500

<!-- b001489 | prose | pages [7] -->
Fitted Values (Extrapolated)

<!-- b001490 | prose | pages [7] -->
Tourism Revenue (in million dollars)

<!-- b001491 | prose | pages [7] -->
400

<!-- b001492 | prose | pages [7] -->
微信公众号：数学模型

<!-- b001493 | prose | pages [7] -->
MSE: 922.28 R2: 0.96

<!-- b001494 | prose | pages [7] -->
300

<!-- b001495 | prose | pages [7] -->
200

<!-- b001496 | prose | pages [7] -->
100

<!-- b001497 | prose | pages [7] -->
0

<!-- b001498 | prose | pages [7] -->
0 50 100 150 200 250

<!-- b001499 | prose | pages [7] -->
Tourist Count (in ten thousands people)

<!-- b001500 | caption | pages [7] -->
Figure 3: Pattern of tourism revenue and environmental index against tourist count

<!-- b001501 | prose | pages [7] -->
3

<!-- b001502 | heading | pages [7] -->
The Models

<!-- b001503 | prose | pages [7] -->
微信号：MATHmodels

<!-- b001504 | prose | pages [7] -->
We aim to find a sustainable tourism strategy that achieves a balance between eco- nomic, environmental, and social aspects. All of the models are built in order to achieve these objectives.

<!-- b001505 | caption | pages [7] -->
Figure 4: Objectives of the model

<!-- b001506 | prose | pages [7] -->
3.1

<!-- b001507 | heading | pages [7] -->
Tourist Demand Model

<!-- b001508 | prose | pages [7] -->
3.1.1 Base Tourist Demand Equation

<!-- b001509 | prose | pages [7] -->
The tourist demand model estimates the number of visitors to Juneau over time. The model accounts for economic conditions, taxation policies, and external demand shocks. The number of tourists, denoted as T(t) in year t, is influenced by the tourism growth rate g(t), the tax rate τ(t) applied to tourism revenue, and random demand shocks δ(t) that reflect external influences. Furthermore, the model includes the demand elasticity parameter γ, which captures the negative impact of taxation on tourism growth.

<!-- b001510 | prose | pages [7] -->
The detail can be described by equation (1):

<!-- b001511 | furniture | pages [8] -->
Team # 2504448

<!-- b001512 | furniture | pages [8] -->
Page 8 of 25

<!-- b001513 | prose | pages [8] -->
T(t) = T(t −1) · (1 + g(t) −γ · τ(t) + δ(t)) (1)

<!-- b001514 | prose | pages [8] -->
This formulation assumes that tourism demand grows at a predictable rate, where tax increases result in reduced tourist arrivals based on an elasticity effect. The inclusion of stochastic demand shocks accounts for uncertainties such as economic downturns or geopolitical events, ensuring a more realistic model representation and according with economic theories.

<!-- b001515 | caption | pages [8] -->
Figure 5: Tourism demand from 2019 to 2023

<!-- b001516 | prose | pages [8] -->
3.1.2 Seasonal Adjustments

<!-- b001517 | prose | pages [8] -->
Tourism in Juneau shows significant seasonal variations due to climatic conditions and cruise ship schedules. To account for these fluctuations, our model introduces seasonal adjustment factors that modify the total number of tourists based on whether it is a peak or off-peak season. The total number of tourists T(t) is divided into peak-season tourists Tpeak(t) and off-peak tourists Toff(t), with the seasonal effects captured by multiplicative factors Speak and Soff. The detail can be described by the system of equations:

<!-- b001518 | prose | pages [8] -->


<!-- b001519 | prose | pages [8] -->
Tpeak(t) = Speak · T(t)

<!-- b001520 | prose | pages [8] -->
 

<!-- b001521 | prose | pages [8] -->
Toff(t) = Soff · T(t)

<!-- b001522 | prose | pages [8] -->
 

<!-- b001523 | prose | pages [8] -->
Speak > 1

<!-- b001524 | prose | pages [8] -->
  

<!-- b001525 | prose | pages [8] -->
Soff < 1

<!-- b001526 | prose | pages [8] -->


<!-- b001527 | prose | pages [8] -->
(2)

<!-- b001528 | prose | pages [8] -->
The seasonal adjustment are determined based on historical trends, accounting for sea- sonal demand fluctuations. It allows better resource allocation and operational planning so that infrastructure and services can accommodate varying tourist volumes through- out the year. We assume that these seasonal factors remain relatively stable across years, influenced primarily by established travel patterns and climatic conditions.

<!-- b001529 | prose | pages [8] -->
关注数学模型

<!-- b001530 | furniture | pages [8] -->
2

<!-- b001531 | furniture | pages [8] -->
MATHmodels

<!-- b001532 | furniture | pages [8] -->
获取更多资讯

<!-- b001533 | furniture | pages [10] -->
Team # 2504448

<!-- b001534 | furniture | pages [10] -->
Page 10 of 25

<!-- b001535 | prose | pages [10] -->
The net profit P(t) from tourism activities, after accounting for operational costs, is given by equation (7). It is crucial for evaluating the long-term economic sustainability of tourism and guiding reinvestment strategies.

<!-- b001536 | prose | pages [10] -->
P(t) = R(t) −C(t) (7)

<!-- b001537 | caption | pages [10] -->
Figure 6: Tourism revenue from 2019 to 2023

<!-- b001538 | prose | pages [10] -->
3.3

<!-- b001539 | heading | pages [10] -->
Environmental Impact Model

<!-- b001540 | prose | pages [10] -->
3.3.1 Environmental Index Calculation

<!-- b001541 | prose | pages [10] -->
The environmental index is computed by integrating various environmental variables, including temperature, snowfall, ocean temperature, and ocean pH level. The methodol- ogy consists of several key steps:

<!-- b001542 | prose | pages [10] -->
Normalization and Weighting Each environmental variable is normalized to the range [0, 1] to eliminate unit bias, using the formula:

<!-- b001543 | prose | pages [10] -->
m

<!-- b001544 | prose | pages [10] -->
m

<!-- b001545 | prose | pages [10] -->
m

<!-- b001546 | prose | pages [10] -->
m

<!-- b001547 | prose | pages [10] -->
m

<!-- b001548 | prose | pages [10] -->
m

<!-- b001549 | prose | pages [10] -->
m

<!-- b001550 | prose | pages [10] -->
m

<!-- b001551 | prose | pages [10] -->
m

<!-- b001552 | prose | pages [10] -->
m

<!-- b001553 | prose | pages [10] -->
m

<!-- b001554 | prose | pages [10] -->
m

<!-- b001555 | prose | pages [10] -->
m

<!-- b001556 | prose | pages [10] -->
m

<!-- b001557 | prose | pages [10] -->
m

<!-- b001558 | prose | pages [10] -->
m

<!-- b001559 | prose | pages [10] -->
m

<!-- b001560 | prose | pages [10] -->
m

<!-- b001561 | prose | pages [10] -->
m

<!-- b001562 | prose | pages [10] -->
m

<!-- b001563 | prose | pages [10] -->
m

<!-- b001564 | prose | pages [10] -->
m

<!-- b001565 | prose | pages [10] -->
x −xmin

<!-- b001566 | prose | pages [10] -->
m

<!-- b001567 | prose | pages [10] -->
m

<!-- b001568 | prose | pages [10] -->
m

<!-- b001569 | prose | pages [10] -->
m

<!-- b001570 | prose | pages [10] -->
m

<!-- b001571 | prose | pages [10] -->
m

<!-- b001572 | prose | pages [10] -->
m

<!-- b001573 | prose | pages [10] -->
m

<!-- b001574 | prose | pages [10] -->
m

<!-- b001575 | prose | pages [10] -->
m

<!-- b001576 | prose | pages [10] -->
m

<!-- b001577 | prose | pages [10] -->
m

<!-- b001578 | prose | pages [10] -->
m

<!-- b001579 | prose | pages [10] -->
m

<!-- b001580 | prose | pages [10] -->
m

<!-- b001581 | prose | pages [10] -->
m

<!-- b001582 | prose | pages [10] -->
m

<!-- b001583 | prose | pages [10] -->
m

<!-- b001584 | prose | pages [10] -->
m

<!-- b001585 | prose | pages [10] -->
m

<!-- b001586 | prose | pages [10] -->
m

<!-- b001587 | prose | pages [10] -->
m

<!-- b001588 | prose | pages [10] -->
m

<!-- b001589 | prose | pages [10] -->
m

<!-- b001590 | prose | pages [10] -->
m

<!-- b001591 | prose | pages [10] -->
m

<!-- b001592 | prose | pages [10] -->
m

<!-- b001593 | prose | pages [10] -->
m

<!-- b001594 | prose | pages [10] -->
m

<!-- b001595 | prose | pages [10] -->
m

<!-- b001596 | prose | pages [10] -->
m

<!-- b001597 | prose | pages [10] -->
m

<!-- b001598 | prose | pages [10] -->
m

<!-- b001599 | prose | pages [10] -->
m

<!-- b001600 | prose | pages [10] -->
m

<!-- b001601 | prose | pages [10] -->
m

<!-- b001602 | prose | pages [10] -->
m

<!-- b001603 | prose | pages [10] -->
m

<!-- b001604 | prose | pages [10] -->
m

<!-- b001605 | prose | pages [10] -->
m

<!-- b001606 | prose | pages [10] -->
m

<!-- b001607 | prose | pages [10] -->
m

<!-- b001608 | prose | pages [10] -->
m

<!-- b001609 | prose | pages [10] -->
m

<!-- b001610 | prose | pages [10] -->
m

<!-- b001611 | prose | pages [10] -->
m

<!-- b001612 | prose | pages [10] -->
m

<!-- b001613 | prose | pages [10] -->
m

<!-- b001614 | prose | pages [10] -->
m

<!-- b001615 | prose | pages [10] -->
m

<!-- b001616 | prose | pages [10] -->
m

<!-- b001617 | prose | pages [10] -->
m

<!-- b001618 | prose | pages [10] -->
m

<!-- b001619 | prose | pages [10] -->
m

<!-- b001620 | prose | pages [10] -->
m

<!-- b001621 | prose | pages [10] -->
m

<!-- b001622 | prose | pages [10] -->
m

<!-- b001623 | prose | pages [10] -->
m

<!-- b001624 | prose | pages [10] -->
m

<!-- b001625 | prose | pages [10] -->
m

<!-- b001626 | prose | pages [10] -->
m

<!-- b001627 | prose | pages [10] -->
m

<!-- b001628 | prose | pages [10] -->
m

<!-- b001629 | prose | pages [10] -->
m

<!-- b001630 | prose | pages [10] -->
m

<!-- b001631 | prose | pages [10] -->
m

<!-- b001632 | prose | pages [10] -->
m

<!-- b001633 | prose | pages [10] -->
m

<!-- b001634 | prose | pages [10] -->
m

<!-- b001635 | prose | pages [10] -->
m

<!-- b001636 | prose | pages [10] -->
m

<!-- b001637 | prose | pages [10] -->
m

<!-- b001638 | prose | pages [10] -->
m

<!-- b001639 | prose | pages [10] -->
Normalized Value =

<!-- b001640 | prose | pages [10] -->
m

<!-- b001641 | prose | pages [10] -->
m

<!-- b001642 | prose | pages [10] -->
m

<!-- b001643 | prose | pages [10] -->
m

<!-- b001644 | prose | pages [10] -->
m

<!-- b001645 | prose | pages [10] -->
m

<!-- b001646 | prose | pages [10] -->
m

<!-- b001647 | prose | pages [10] -->
m

<!-- b001648 | prose | pages [10] -->
m

<!-- b001649 | prose | pages [10] -->
m

<!-- b001650 | prose | pages [10] -->
m

<!-- b001651 | prose | pages [10] -->
m

<!-- b001652 | prose | pages [10] -->
m

<!-- b001653 | prose | pages [10] -->
(8)

<!-- b001654 | prose | pages [10] -->
m

<!-- b001655 | prose | pages [10] -->
m

<!-- b001656 | prose | pages [10] -->
m

<!-- b001657 | prose | pages [10] -->
m

<!-- b001658 | prose | pages [10] -->
m

<!-- b001659 | prose | pages [10] -->
m

<!-- b001660 | prose | pages [10] -->
m

<!-- b001661 | prose | pages [10] -->
m

<!-- b001662 | prose | pages [10] -->
m

<!-- b001663 | prose | pages [10] -->
m

<!-- b001664 | prose | pages [10] -->
m

<!-- b001665 | prose | pages [10] -->
m

<!-- b001666 | prose | pages [10] -->
m

<!-- b001667 | prose | pages [10] -->
m

<!-- b001668 | prose | pages [10] -->
m

<!-- b001669 | prose | pages [10] -->
m

<!-- b001670 | prose | pages [10] -->
m

<!-- b001671 | prose | pages [10] -->
m

<!-- b001672 | prose | pages [10] -->
m

<!-- b001673 | prose | pages [10] -->
m

<!-- b001674 | prose | pages [10] -->
m

<!-- b001675 | prose | pages [10] -->
m

<!-- b001676 | prose | pages [10] -->
m

<!-- b001677 | prose | pages [10] -->
m

<!-- b001678 | prose | pages [10] -->
m

<!-- b001679 | prose | pages [10] -->
m

<!-- b001680 | prose | pages [10] -->
m

<!-- b001681 | prose | pages [10] -->
m

<!-- b001682 | prose | pages [10] -->
m

<!-- b001683 | prose | pages [10] -->
m

<!-- b001684 | prose | pages [10] -->
m

<!-- b001685 | prose | pages [10] -->
m

<!-- b001686 | prose | pages [10] -->
m

<!-- b001687 | prose | pages [10] -->
m

<!-- b001688 | prose | pages [10] -->
m

<!-- b001689 | prose | pages [10] -->
m

<!-- b001690 | prose | pages [10] -->
m

<!-- b001691 | prose | pages [10] -->
m

<!-- b001692 | prose | pages [10] -->
m

<!-- b001693 | prose | pages [10] -->
m

<!-- b001694 | prose | pages [10] -->
m

<!-- b001695 | prose | pages [10] -->
m

<!-- b001696 | prose | pages [10] -->
m

<!-- b001697 | prose | pages [10] -->
m

<!-- b001698 | prose | pages [10] -->
m

<!-- b001699 | prose | pages [10] -->
m

<!-- b001700 | prose | pages [10] -->
m

<!-- b001701 | prose | pages [10] -->
m

<!-- b001702 | prose | pages [10] -->
m

<!-- b001703 | prose | pages [10] -->
m

<!-- b001704 | prose | pages [10] -->
m

<!-- b001705 | prose | pages [10] -->
m

<!-- b001706 | prose | pages [10] -->
m

<!-- b001707 | prose | pages [10] -->
m

<!-- b001708 | prose | pages [10] -->
m

<!-- b001709 | prose | pages [10] -->
m

<!-- b001710 | prose | pages [10] -->
m

<!-- b001711 | prose | pages [10] -->
m

<!-- b001712 | prose | pages [10] -->
m

<!-- b001713 | prose | pages [10] -->
xmax −xmin

<!-- b001714 | prose | pages [10] -->
m

<!-- b001715 | prose | pages [10] -->
m

<!-- b001716 | prose | pages [10] -->
m

<!-- b001717 | prose | pages [10] -->
m

<!-- b001718 | prose | pages [10] -->
m

<!-- b001719 | prose | pages [10] -->
m

<!-- b001720 | prose | pages [10] -->
m

<!-- b001721 | prose | pages [10] -->
m

<!-- b001722 | prose | pages [10] -->
m

<!-- b001723 | prose | pages [10] -->
m

<!-- b001724 | prose | pages [10] -->
m

<!-- b001725 | prose | pages [10] -->
m

<!-- b001726 | prose | pages [10] -->
m

<!-- b001727 | prose | pages [10] -->
m

<!-- b001728 | prose | pages [10] -->
m

<!-- b001729 | prose | pages [10] -->
m

<!-- b001730 | prose | pages [10] -->
m

<!-- b001731 | prose | pages [10] -->
m

<!-- b001732 | prose | pages [10] -->
m

<!-- b001733 | prose | pages [10] -->
m

<!-- b001734 | prose | pages [10] -->
m

<!-- b001735 | prose | pages [10] -->
m

<!-- b001736 | prose | pages [10] -->
m

<!-- b001737 | prose | pages [10] -->
m

<!-- b001738 | prose | pages [10] -->
m

<!-- b001739 | prose | pages [10] -->
m

<!-- b001740 | prose | pages [10] -->
m

<!-- b001741 | prose | pages [10] -->
m

<!-- b001742 | prose | pages [10] -->
m

<!-- b001743 | prose | pages [10] -->
m

<!-- b001744 | prose | pages [10] -->
m

<!-- b001745 | prose | pages [10] -->
m

<!-- b001746 | prose | pages [10] -->
m

<!-- b001747 | prose | pages [10] -->
m

<!-- b001748 | prose | pages [10] -->
m

<!-- b001749 | prose | pages [10] -->
m

<!-- b001750 | prose | pages [10] -->
m

<!-- b001751 | prose | pages [10] -->
m

<!-- b001752 | prose | pages [10] -->
m

<!-- b001753 | prose | pages [10] -->
m

<!-- b001754 | prose | pages [10] -->
m

<!-- b001755 | prose | pages [10] -->
m

<!-- b001756 | prose | pages [10] -->
m

<!-- b001757 | prose | pages [10] -->
m

<!-- b001758 | prose | pages [10] -->
m

<!-- b001759 | prose | pages [10] -->
m

<!-- b001760 | prose | pages [10] -->
m

<!-- b001761 | prose | pages [10] -->
m

<!-- b001762 | prose | pages [10] -->
m

<!-- b001763 | prose | pages [10] -->
m

<!-- b001764 | prose | pages [10] -->
m

<!-- b001765 | prose | pages [10] -->
m

<!-- b001766 | prose | pages [10] -->
m

<!-- b001767 | prose | pages [10] -->
m

<!-- b001768 | prose | pages [10] -->
m

<!-- b001769 | prose | pages [10] -->
m

<!-- b001770 | prose | pages [10] -->
m

<!-- b001771 | prose | pages [10] -->
m

<!-- b001772 | prose | pages [10] -->
m

<!-- b001773 | prose | pages [10] -->
m

<!-- b001774 | prose | pages [10] -->
m

<!-- b001775 | prose | pages [10] -->
m

<!-- b001776 | prose | pages [10] -->
m

<!-- b001777 | prose | pages [10] -->
m

<!-- b001778 | prose | pages [10] -->
m

<!-- b001779 | prose | pages [10] -->
m

<!-- b001780 | prose | pages [10] -->
m

<!-- b001781 | prose | pages [10] -->
m

<!-- b001782 | prose | pages [10] -->
m

<!-- b001783 | prose | pages [10] -->
m

<!-- b001784 | prose | pages [10] -->
m

<!-- b001785 | prose | pages [10] -->
m

<!-- b001786 | prose | pages [10] -->
m

<!-- b001787 | prose | pages [10] -->
m

<!-- b001788 | prose | pages [10] -->
m

<!-- b001789 | prose | pages [10] -->
m

<!-- b001790 | prose | pages [10] -->
m

<!-- b001791 | prose | pages [10] -->
m

<!-- b001792 | prose | pages [10] -->
m

<!-- b001793 | prose | pages [10] -->
m

<!-- b001794 | prose | pages [10] -->
m

<!-- b001795 | prose | pages [10] -->
m

<!-- b001796 | prose | pages [10] -->
m

<!-- b001797 | prose | pages [10] -->
m

<!-- b001798 | prose | pages [10] -->
m

<!-- b001799 | prose | pages [10] -->
m

<!-- b001800 | prose | pages [10] -->
m

<!-- b001801 | prose | pages [10] -->
m

<!-- b001802 | prose | pages [10] -->
m

<!-- b001803 | prose | pages [10] -->
m

<!-- b001804 | prose | pages [10] -->
m

<!-- b001805 | prose | pages [10] -->
m

<!-- b001806 | prose | pages [10] -->
m

<!-- b001807 | prose | pages [10] -->
m

<!-- b001808 | prose | pages [10] -->
m

<!-- b001809 | prose | pages [10] -->
m

<!-- b001810 | prose | pages [10] -->
m

<!-- b001811 | prose | pages [10] -->
m

<!-- b001812 | prose | pages [10] -->
m

<!-- b001813 | prose | pages [10] -->
m

<!-- b001814 | prose | pages [10] -->
m

<!-- b001815 | prose | pages [10] -->
m

<!-- b001816 | prose | pages [10] -->
m

<!-- b001817 | prose | pages [10] -->
m

<!-- b001818 | prose | pages [10] -->
m

<!-- b001819 | prose | pages [10] -->
m

<!-- b001820 | prose | pages [10] -->
m

<!-- b001821 | prose | pages [10] -->
m

<!-- b001822 | prose | pages [10] -->
m

<!-- b001823 | prose | pages [10] -->
m

<!-- b001824 | prose | pages [10] -->
m

<!-- b001825 | prose | pages [10] -->
m

<!-- b001826 | prose | pages [10] -->
m

<!-- b001827 | prose | pages [10] -->
m

<!-- b001828 | prose | pages [10] -->
m

<!-- b001829 | prose | pages [10] -->
m

<!-- b001830 | prose | pages [10] -->
m

<!-- b001831 | prose | pages [10] -->
m

<!-- b001832 | prose | pages [10] -->
m

<!-- b001833 | prose | pages [10] -->
m

<!-- b001834 | prose | pages [10] -->
m

<!-- b001835 | prose | pages [10] -->
m

<!-- b001836 | prose | pages [10] -->
m

<!-- b001837 | prose | pages [10] -->
m

<!-- b001838 | prose | pages [10] -->
m

<!-- b001839 | prose | pages [10] -->
m

<!-- b001840 | prose | pages [10] -->
m

<!-- b001841 | prose | pages [10] -->
m

<!-- b001842 | prose | pages [10] -->
m

<!-- b001843 | prose | pages [10] -->
m

<!-- b001844 | prose | pages [10] -->
m

<!-- b001845 | prose | pages [10] -->
m

<!-- b001846 | prose | pages [10] -->
m

<!-- b001847 | prose | pages [10] -->
m

<!-- b001848 | prose | pages [10] -->
m

<!-- b001849 | prose | pages [10] -->
m

<!-- b001850 | prose | pages [10] -->
m

<!-- b001851 | prose | pages [10] -->
m

<!-- b001852 | prose | pages [10] -->
m

<!-- b001853 | prose | pages [10] -->
m

<!-- b001854 | prose | pages [10] -->
m

<!-- b001855 | prose | pages [10] -->
m

<!-- b001856 | prose | pages [10] -->
m

<!-- b001857 | prose | pages [10] -->
m

<!-- b001858 | prose | pages [10] -->
m

<!-- b001859 | prose | pages [10] -->
m

<!-- b001860 | prose | pages [10] -->
m

<!-- b001861 | prose | pages [10] -->
m

<!-- b001862 | prose | pages [10] -->
m

<!-- b001863 | prose | pages [10] -->
m

<!-- b001864 | prose | pages [10] -->
m

<!-- b001865 | prose | pages [10] -->
m

<!-- b001866 | prose | pages [10] -->
m

<!-- b001867 | prose | pages [10] -->
m

<!-- b001868 | prose | pages [10] -->
m

<!-- b001869 | prose | pages [10] -->
m

<!-- b001870 | prose | pages [10] -->
m

<!-- b001871 | prose | pages [10] -->
m

<!-- b001872 | prose | pages [10] -->
m

<!-- b001873 | prose | pages [10] -->
m

<!-- b001874 | prose | pages [10] -->
m

<!-- b001875 | prose | pages [10] -->
m

<!-- b001876 | prose | pages [10] -->
m

<!-- b001877 | prose | pages [10] -->
m

<!-- b001878 | prose | pages [10] -->
m

<!-- b001879 | prose | pages [10] -->
m

<!-- b001880 | prose | pages [10] -->
m

<!-- b001881 | prose | pages [10] -->
m

<!-- b001882 | prose | pages [10] -->
m

<!-- b001883 | prose | pages [10] -->
m

<!-- b001884 | prose | pages [10] -->
m

<!-- b001885 | prose | pages [10] -->
m

<!-- b001886 | prose | pages [10] -->
m

<!-- b001887 | prose | pages [10] -->
m

<!-- b001888 | prose | pages [10] -->
m

<!-- b001889 | prose | pages [10] -->
m

<!-- b001890 | prose | pages [10] -->
m

<!-- b001891 | prose | pages [10] -->
m

<!-- b001892 | prose | pages [10] -->
m

<!-- b001893 | prose | pages [10] -->
m

<!-- b001894 | prose | pages [10] -->
m

<!-- b001895 | prose | pages [10] -->
m

<!-- b001896 | prose | pages [10] -->
m

<!-- b001897 | prose | pages [10] -->
m

<!-- b001898 | prose | pages [10] -->
m

<!-- b001899 | prose | pages [10] -->
m

<!-- b001900 | prose | pages [10] -->
m

<!-- b001901 | prose | pages [10] -->
m

<!-- b001902 | prose | pages [10] -->
m

<!-- b001903 | prose | pages [10] -->
m

<!-- b001904 | prose | pages [10] -->
m

<!-- b001905 | prose | pages [10] -->
m

<!-- b001906 | prose | pages [10] -->
m

<!-- b001907 | prose | pages [10] -->
m

<!-- b001908 | prose | pages [10] -->
m

<!-- b001909 | prose | pages [10] -->
m

<!-- b001910 | prose | pages [10] -->
m

<!-- b001911 | prose | pages [10] -->
m

<!-- b001912 | prose | pages [10] -->
m

<!-- b001913 | prose | pages [10] -->
m

<!-- b001914 | prose | pages [10] -->
m

<!-- b001915 | prose | pages [10] -->
m

<!-- b001916 | prose | pages [10] -->
m

<!-- b001917 | prose | pages [10] -->
m

<!-- b001918 | prose | pages [10] -->
m

<!-- b001919 | prose | pages [10] -->
m

<!-- b001920 | prose | pages [10] -->
m

<!-- b001921 | prose | pages [10] -->
m

<!-- b001922 | prose | pages [10] -->
m

<!-- b001923 | prose | pages [10] -->
m

<!-- b001924 | prose | pages [10] -->
m

<!-- b001925 | prose | pages [10] -->
m

<!-- b001926 | prose | pages [10] -->
m

<!-- b001927 | prose | pages [10] -->
m

<!-- b001928 | prose | pages [10] -->
m

<!-- b001929 | prose | pages [10] -->
m

<!-- b001930 | prose | pages [10] -->
m

<!-- b001931 | prose | pages [10] -->
m

<!-- b001932 | prose | pages [10] -->
m

<!-- b001933 | prose | pages [10] -->
m

<!-- b001934 | prose | pages [10] -->
m

<!-- b001935 | prose | pages [10] -->
m

<!-- b001936 | prose | pages [10] -->
m

<!-- b001937 | prose | pages [10] -->
m

<!-- b001938 | prose | pages [10] -->
m

<!-- b001939 | prose | pages [10] -->
m

<!-- b001940 | prose | pages [10] -->
m

<!-- b001941 | prose | pages [10] -->
m

<!-- b001942 | prose | pages [10] -->
m

<!-- b001943 | prose | pages [10] -->
m

<!-- b001944 | prose | pages [10] -->
m

<!-- b001945 | prose | pages [10] -->
m

<!-- b001946 | prose | pages [10] -->
m

<!-- b001947 | prose | pages [10] -->
m

<!-- b001948 | prose | pages [10] -->
m

<!-- b001949 | prose | pages [10] -->
m

<!-- b001950 | prose | pages [10] -->
m

<!-- b001951 | prose | pages [10] -->
m

<!-- b001952 | prose | pages [10] -->
m

<!-- b001953 | prose | pages [10] -->
m

<!-- b001954 | prose | pages [10] -->
m

<!-- b001955 | prose | pages [10] -->
m

<!-- b001956 | prose | pages [10] -->
m

<!-- b001957 | prose | pages [10] -->
m

<!-- b001958 | prose | pages [10] -->
m

<!-- b001959 | prose | pages [10] -->
m

<!-- b001960 | prose | pages [10] -->
m

<!-- b001961 | prose | pages [10] -->
m

<!-- b001962 | prose | pages [10] -->
m

<!-- b001963 | prose | pages [10] -->
m

<!-- b001964 | prose | pages [10] -->
m

<!-- b001965 | prose | pages [10] -->
m

<!-- b001966 | prose | pages [10] -->
m

<!-- b001967 | prose | pages [10] -->
m

<!-- b001968 | prose | pages [10] -->
m

<!-- b001969 | prose | pages [10] -->
m

<!-- b001970 | prose | pages [10] -->
m

<!-- b001971 | prose | pages [10] -->
m

<!-- b001972 | prose | pages [10] -->
m

<!-- b001973 | prose | pages [10] -->
m

<!-- b001974 | prose | pages [10] -->
m

<!-- b001975 | prose | pages [10] -->
m

<!-- b001976 | prose | pages [10] -->
Weighting is used to reflect the impact of each factor on environmental quality:

<!-- b001977 | prose | pages [10] -->
m

<!-- b001978 | prose | pages [10] -->
m

<!-- b001979 | prose | pages [10] -->
m

<!-- b001980 | prose | pages [10] -->
m

<!-- b001981 | prose | pages [10] -->
m

<!-- b001982 | prose | pages [10] -->
m

<!-- b001983 | prose | pages [10] -->
m

<!-- b001984 | prose | pages [10] -->
m

<!-- b001985 | prose | pages [10] -->
m

<!-- b001986 | prose | pages [10] -->
m

<!-- b001987 | prose | pages [10] -->
m

<!-- b001988 | prose | pages [10] -->
m

<!-- b001989 | prose | pages [10] -->
m

<!-- b001990 | prose | pages [10] -->
m

<!-- b001991 | prose | pages [10] -->
m

<!-- b001992 | prose | pages [10] -->
m

<!-- b001993 | prose | pages [10] -->
m

<!-- b001994 | prose | pages [10] -->
m

<!-- b001995 | prose | pages [10] -->
m

<!-- b001996 | prose | pages [10] -->
m

<!-- b001997 | prose | pages [10] -->
m

<!-- b001998 | prose | pages [10] -->
m

<!-- b001999 | prose | pages [10] -->
m

<!-- b002000 | prose | pages [10] -->
m

<!-- b002001 | prose | pages [10] -->
m

<!-- b002002 | prose | pages [10] -->
m

<!-- b002003 | prose | pages [10] -->
m

<!-- b002004 | prose | pages [10] -->
m

<!-- b002005 | prose | pages [10] -->
m

<!-- b002006 | prose | pages [10] -->
m

<!-- b002007 | prose | pages [10] -->
m

<!-- b002008 | prose | pages [10] -->
m

<!-- b002009 | prose | pages [10] -->
m

<!-- b002010 | prose | pages [10] -->
m

<!-- b002011 | prose | pages [10] -->
m

<!-- b002012 | prose | pages [10] -->
m

<!-- b002013 | prose | pages [10] -->
m

<!-- b002014 | prose | pages [10] -->
m

<!-- b002015 | prose | pages [10] -->
m

<!-- b002016 | prose | pages [10] -->
m

<!-- b002017 | prose | pages [10] -->
m

<!-- b002018 | prose | pages [10] -->
m

<!-- b002019 | prose | pages [10] -->
m

<!-- b002020 | prose | pages [10] -->
m

<!-- b002021 | prose | pages [10] -->
m

<!-- b002022 | prose | pages [10] -->
m

<!-- b002023 | prose | pages [10] -->
m

<!-- b002024 | prose | pages [10] -->
m

<!-- b002025 | prose | pages [10] -->
m

<!-- b002026 | prose | pages [10] -->
m

<!-- b002027 | prose | pages [10] -->
m

<!-- b002028 | prose | pages [10] -->
m

<!-- b002029 | prose | pages [10] -->
m

<!-- b002030 | prose | pages [10] -->
m

<!-- b002031 | prose | pages [10] -->
m

<!-- b002032 | prose | pages [10] -->
m

<!-- b002033 | prose | pages [10] -->
m

<!-- b002034 | prose | pages [10] -->
m

<!-- b002035 | prose | pages [10] -->
m

<!-- b002036 | prose | pages [10] -->
m

<!-- b002037 | prose | pages [10] -->
m

<!-- b002038 | prose | pages [10] -->
m

<!-- b002039 | prose | pages [10] -->
m

<!-- b002040 | prose | pages [10] -->
m

<!-- b002041 | prose | pages [10] -->
m

<!-- b002042 | prose | pages [10] -->
m

<!-- b002043 | prose | pages [10] -->
m

<!-- b002044 | prose | pages [10] -->
m

<!-- b002045 | prose | pages [10] -->
m

<!-- b002046 | prose | pages [10] -->
m

<!-- b002047 | prose | pages [10] -->
m

<!-- b002048 | prose | pages [10] -->
m

<!-- b002049 | prose | pages [10] -->
m

<!-- b002050 | prose | pages [10] -->
m

<!-- b002051 | prose | pages [10] -->
m

<!-- b002052 | prose | pages [10] -->
m

<!-- b002053 | prose | pages [10] -->
m

<!-- b002054 | prose | pages [10] -->
m

<!-- b002055 | prose | pages [10] -->
m

<!-- b002056 | prose | pages [10] -->
m

<!-- b002057 | prose | pages [10] -->
m

<!-- b002058 | prose | pages [10] -->
m

<!-- b002059 | prose | pages [10] -->
m

<!-- b002060 | prose | pages [10] -->
m

<!-- b002061 | prose | pages [10] -->
m

<!-- b002062 | prose | pages [10] -->
m

<!-- b002063 | prose | pages [10] -->
m

<!-- b002064 | prose | pages [10] -->
m

<!-- b002065 | prose | pages [10] -->
m

<!-- b002066 | prose | pages [10] -->
m

<!-- b002067 | prose | pages [10] -->
m

<!-- b002068 | prose | pages [10] -->
m

<!-- b002069 | prose | pages [10] -->
m

<!-- b002070 | prose | pages [10] -->
m

<!-- b002071 | prose | pages [10] -->
m

<!-- b002072 | prose | pages [10] -->
m

<!-- b002073 | prose | pages [10] -->
m

<!-- b002074 | prose | pages [10] -->
m

<!-- b002075 | prose | pages [10] -->
m

<!-- b002076 | prose | pages [10] -->
m

<!-- b002077 | prose | pages [10] -->
m

<!-- b002078 | prose | pages [10] -->
m

<!-- b002079 | prose | pages [10] -->
m

<!-- b002080 | prose | pages [10] -->
m

<!-- b002081 | prose | pages [10] -->
m

<!-- b002082 | prose | pages [10] -->
m

<!-- b002083 | prose | pages [10] -->
m

<!-- b002084 | prose | pages [10] -->
m

<!-- b002085 | prose | pages [10] -->
m

<!-- b002086 | prose | pages [10] -->
m

<!-- b002087 | prose | pages [10] -->
m

<!-- b002088 | prose | pages [10] -->
m

<!-- b002089 | prose | pages [10] -->
m

<!-- b002090 | prose | pages [10] -->
m

<!-- b002091 | prose | pages [10] -->
m

<!-- b002092 | prose | pages [10] -->
m

<!-- b002093 | prose | pages [10] -->
m

<!-- b002094 | prose | pages [10] -->
m

<!-- b002095 | prose | pages [10] -->
m

<!-- b002096 | prose | pages [10] -->
m

<!-- b002097 | prose | pages [10] -->
m

<!-- b002098 | prose | pages [10] -->
m

<!-- b002099 | prose | pages [10] -->
m

<!-- b002100 | prose | pages [10] -->
m

<!-- b002101 | prose | pages [10] -->
m

<!-- b002102 | prose | pages [10] -->
m

<!-- b002103 | prose | pages [10] -->
m

<!-- b002104 | prose | pages [10] -->
m

<!-- b002105 | prose | pages [10] -->
m

<!-- b002106 | prose | pages [10] -->
m

<!-- b002107 | prose | pages [10] -->
m

<!-- b002108 | prose | pages [10] -->
m

<!-- b002109 | prose | pages [10] -->
m

<!-- b002110 | prose | pages [10] -->
m

<!-- b002111 | prose | pages [10] -->
m

<!-- b002112 | prose | pages [10] -->
m

<!-- b002113 | prose | pages [10] -->
m

<!-- b002114 | prose | pages [10] -->
m

<!-- b002115 | prose | pages [10] -->
m

<!-- b002116 | prose | pages [10] -->
m

<!-- b002117 | prose | pages [10] -->
m

<!-- b002118 | prose | pages [10] -->
m

<!-- b002119 | prose | pages [10] -->
m

<!-- b002120 | prose | pages [10] -->
m

<!-- b002121 | prose | pages [10] -->
m

<!-- b002122 | prose | pages [10] -->
m

<!-- b002123 | prose | pages [10] -->
m

<!-- b002124 | prose | pages [10] -->
m

<!-- b002125 | prose | pages [10] -->
m

<!-- b002126 | prose | pages [10] -->
m

<!-- b002127 | prose | pages [10] -->
m

<!-- b002128 | prose | pages [10] -->
m

<!-- b002129 | prose | pages [10] -->
m

<!-- b002130 | prose | pages [10] -->
m

<!-- b002131 | prose | pages [10] -->
m

<!-- b002132 | prose | pages [10] -->
m

<!-- b002133 | prose | pages [10] -->
m

<!-- b002134 | prose | pages [10] -->
m

<!-- b002135 | prose | pages [10] -->
m

<!-- b002136 | prose | pages [10] -->
m

<!-- b002137 | prose | pages [10] -->
m

<!-- b002138 | prose | pages [10] -->
m

<!-- b002139 | prose | pages [10] -->
m

<!-- b002140 | prose | pages [10] -->
m

<!-- b002141 | prose | pages [10] -->
m

<!-- b002142 | prose | pages [10] -->
m

<!-- b002143 | prose | pages [10] -->
m

<!-- b002144 | prose | pages [10] -->
m

<!-- b002145 | prose | pages [10] -->
m

<!-- b002146 | prose | pages [10] -->
m

<!-- b002147 | prose | pages [10] -->
m

<!-- b002148 | prose | pages [10] -->
m

<!-- b002149 | prose | pages [10] -->
m

<!-- b002150 | prose | pages [10] -->
m

<!-- b002151 | prose | pages [10] -->
m

<!-- b002152 | prose | pages [10] -->
m

<!-- b002153 | prose | pages [10] -->
m

<!-- b002154 | prose | pages [10] -->
m

<!-- b002155 | prose | pages [10] -->
m

<!-- b002156 | prose | pages [10] -->
m

<!-- b002157 | prose | pages [10] -->
m

<!-- b002158 | prose | pages [10] -->
m

<!-- b002159 | prose | pages [10] -->
m

<!-- b002160 | prose | pages [10] -->
m

<!-- b002161 | prose | pages [10] -->
m

<!-- b002162 | prose | pages [10] -->
m

<!-- b002163 | prose | pages [10] -->
m

<!-- b002164 | prose | pages [10] -->
m

<!-- b002165 | prose | pages [10] -->
m

<!-- b002166 | prose | pages [10] -->
m

<!-- b002167 | prose | pages [10] -->
m

<!-- b002168 | prose | pages [10] -->
m

<!-- b002169 | prose | pages [10] -->
m

<!-- b002170 | prose | pages [10] -->
m

<!-- b002171 | prose | pages [10] -->
m

<!-- b002172 | prose | pages [10] -->
m

<!-- b002173 | prose | pages [10] -->
m

<!-- b002174 | prose | pages [10] -->
m

<!-- b002175 | prose | pages [10] -->
m

<!-- b002176 | prose | pages [10] -->
m

<!-- b002177 | prose | pages [10] -->
m

<!-- b002178 | prose | pages [10] -->
m

<!-- b002179 | prose | pages [10] -->
m

<!-- b002180 | prose | pages [10] -->
m

<!-- b002181 | prose | pages [10] -->
m

<!-- b002182 | prose | pages [10] -->
m

<!-- b002183 | prose | pages [10] -->
m

<!-- b002184 | prose | pages [10] -->
m

<!-- b002185 | prose | pages [10] -->
m

<!-- b002186 | prose | pages [10] -->
m

<!-- b002187 | prose | pages [10] -->
m

<!-- b002188 | prose | pages [10] -->
m

<!-- b002189 | prose | pages [10] -->
m

<!-- b002190 | prose | pages [10] -->
m

<!-- b002191 | prose | pages [10] -->
m

<!-- b002192 | prose | pages [10] -->
m

<!-- b002193 | prose | pages [10] -->
m

<!-- b002194 | prose | pages [10] -->
m

<!-- b002195 | prose | pages [10] -->
m

<!-- b002196 | prose | pages [10] -->
m

<!-- b002197 | prose | pages [10] -->
m

<!-- b002198 | prose | pages [10] -->
m

<!-- b002199 | prose | pages [10] -->
m

<!-- b002200 | prose | pages [10] -->
m

<!-- b002201 | prose | pages [10] -->
m

<!-- b002202 | prose | pages [10] -->
m

<!-- b002203 | prose | pages [10] -->
m

<!-- b002204 | prose | pages [10] -->
m

<!-- b002205 | prose | pages [10] -->
m

<!-- b002206 | prose | pages [10] -->
m

<!-- b002207 | prose | pages [10] -->
m

<!-- b002208 | prose | pages [10] -->
m

<!-- b002209 | prose | pages [10] -->
m

<!-- b002210 | prose | pages [10] -->
m

<!-- b002211 | prose | pages [10] -->
m

<!-- b002212 | prose | pages [10] -->
m

<!-- b002213 | prose | pages [10] -->
m

<!-- b002214 | prose | pages [10] -->
m

<!-- b002215 | prose | pages [10] -->
m

<!-- b002216 | prose | pages [10] -->
m

<!-- b002217 | prose | pages [10] -->
m

<!-- b002218 | prose | pages [10] -->
m

<!-- b002219 | prose | pages [10] -->
m

<!-- b002220 | prose | pages [10] -->
m

<!-- b002221 | prose | pages [10] -->
m

<!-- b002222 | prose | pages [10] -->
m

<!-- b002223 | prose | pages [10] -->
m

<!-- b002224 | prose | pages [10] -->
m

<!-- b002225 | prose | pages [10] -->
m

<!-- b002226 | prose | pages [10] -->
m

<!-- b002227 | prose | pages [10] -->
m

<!-- b002228 | prose | pages [10] -->
m

<!-- b002229 | prose | pages [10] -->
m

<!-- b002230 | prose | pages [10] -->
m

<!-- b002231 | prose | pages [10] -->
m

<!-- b002232 | prose | pages [10] -->
m

<!-- b002233 | prose | pages [10] -->
m

<!-- b002234 | prose | pages [10] -->
m

<!-- b002235 | prose | pages [10] -->
• Temperature and ocean temperature are assigned a weight of −1 (negative impact).

<!-- b002236 | prose | pages [10] -->
• Snowfall and ocean pH are assigned a weight of +1 (positive impact).

<!-- b002237 | prose | pages [10] -->
关注数学模型

<!-- b002238 | furniture | pages [10] -->
2

<!-- b002239 | furniture | pages [10] -->
MATHmodels

<!-- b002240 | furniture | pages [10] -->
获取更多资讯

<!-- b002241 | furniture | pages [11] -->
Team # 2504448

<!-- b002242 | prose | pages [11] -->
Entropy-Based Weighting

<!-- b002243 | furniture | pages [11] -->
Page 11 of 25

<!-- b002244 | prose | pages [11] -->
The importance of each variable is determined using entropy- based weighting. The use of entropy weighting prioritizes variables with greater variabil-

<!-- b002245 | prose | pages [11] -->
微信公众号：数学模型

<!-- b002246 | prose | pages [11] -->
ity, ensuring that the index remains sensitive to significant environmental changes. The entropy of each variable is calculated as:

<!-- b002247 | prose | pages [11] -->
Entropy = −∑pi log(pi) (9)

<!-- b002248 | prose | pages [11] -->
where pi is the normalized value of the variable. The entropy weight is then computed as:

<!-- b002249 | prose | pages [11] -->
Entropy Weight = 1 −Entropy (10)

<!-- b002250 | prose | pages [11] -->
微信号：MATHmodels

<!-- b002251 | prose | pages [11] -->
Final Environmental Index Calculation

<!-- b002252 | prose | pages [11] -->
∑(1 −Entropy)

<!-- b002253 | prose | pages [11] -->
The environmental index is calculated by com- bining the normalized and weighted environmental data using the following formula:

<!-- b002254 | prose | pages [11] -->
Environmental Index = ∑wi · xi −Indexmin

<!-- b002255 | prose | pages [11] -->
(11)

<!-- b002256 | prose | pages [11] -->
Indexmax −Indexmin

<!-- b002257 | prose | pages [11] -->
where wi represents the entropy-based weights and xi denotes the normalized values of the environmental factors.

<!-- b002258 | caption | pages [11] -->
Figure 7: Computation of environmental index

<!-- b002259 | prose | pages [11] -->
3.3.2 Government Intervention

<!-- b002260 | prose | pages [11] -->
To control the negative effects of tourism on the environment, a fraction of govern- ment revenue from tourism taxation is reinvested into environmental conservation. The improved environmental index Esub(t), after applying government intervention. M(t) is the government expenditures, and α is the sensitivity of environment to the additional government expenditures. The environmental index is modeled as follows:

<!-- b002261 | prose | pages [11] -->
Esub(t) = E(t) + α · M(t) (12)

<!-- b002262 | furniture | pages [12] -->
Team # 2504448

<!-- b002263 | prose | pages [12] -->
3.3.3 Environmental Recovery

<!-- b002264 | furniture | pages [12] -->
Page 12 of 25

<!-- b002265 | prose | pages [12] -->
By assumption, the environment has a natural recovery rate r that helps restore its quality over time. However, tourism activities continuously exert pressure on the ecosys- tem at the same time, as a function of the environmental harm factor caused by tourism h and the carrying capacity Tmax.

<!-- b002266 | prose | pages [12] -->
 T(t)

<!-- b002267 | prose | pages [12] -->


<!-- b002268 | prose | pages [12] -->
E(t + 1) = Esub(t) + r · (1 −Esub(t)) −h ·

<!-- b002269 | prose | pages [12] -->
3.4

<!-- b002270 | heading | pages [12] -->
Resident Satisfaction Model

<!-- b002271 | prose | pages [12] -->
3.4.1

<!-- b002272 | heading | pages [12] -->
Model Formulation

<!-- b002273 | prose | pages [12] -->
(13)

<!-- b002274 | prose | pages [12] -->
Tmax

<!-- b002275 | prose | pages [12] -->
Resident satisfaction, denoted as Q(t), is influenced by the number of tourists T(t), the environmental index E(t), and the taxation rate τ(t) applied to tourism revenue. Our model assumes that an optimal level of tourism Topt exists, beyond which further in- creases in tourist numbers negatively impact resident satisfaction. In addition, increased taxation on tourism revenue leads to lower resident satisfaction due to potential financial burdens and rising costs.

<!-- b002276 | prose | pages [12] -->
1 −|T(t) −Topt|

<!-- b002277 | prose | pages [12] -->


<!-- b002278 | prose | pages [12] -->
Q(t) = ω1

<!-- b002279 | prose | pages [12] -->
Topt

<!-- b002280 | prose | pages [12] -->


<!-- b002281 | prose | pages [12] -->
+ ω2E(t) −ω3τ(t) (14)

<!-- b002282 | prose | pages [12] -->
ω1, ω2, and ω3 are weighting coefficients that represent the relative importance of each factor in determining resident satisfaction. A higher ω1 places more emphasis on managing the tourist population, whereas a greater ω2 prioritizes environmental quality, and ω3 controls the impact of taxation.

<!-- b002283 | heading | pages [12] -->
Model Solving using Dynamic Programming

<!-- b002284 | prose | pages [12] -->
3.5

<!-- b002285 | caption | pages [12] -->
Figure 8: Framework of the model

<!-- b002286 | prose | pages [12] -->
关注数学模型

<!-- b002287 | furniture | pages [12] -->
2

<!-- b002288 | furniture | pages [12] -->
MATHmodels

<!-- b002289 | furniture | pages [12] -->
获取更多资讯

<!-- b002290 | furniture | pages [13] -->
Team # 2504448

<!-- b002291 | prose | pages [13] -->
3.5.1 Variables Being Optimized

<!-- b002292 | furniture | pages [13] -->
Page 13 of 25

<!-- b002293 | prose | pages [13] -->
微信公众号：数学模型

<!-- b002294 | prose | pages [13] -->
In our model, we aim to maximize the following factors:

<!-- b002295 | prose | pages [13] -->
• Economic Profit P(t):

<!-- b002296 | prose | pages [13] -->
This represents the net benefit derived from tourism, calculated as total revenue minus operational and environmental costs.

<!-- b002297 | prose | pages [13] -->
• Environmental Index E(t):

<!-- b002298 | prose | pages [13] -->
A measure of environmental sustainability, reflecting the long-term ecological bal- ance affected by tourism activities. The model incorporates it within the value func- tion to ensure sustainability considerations.

<!-- b002299 | prose | pages [13] -->
微信号：MATHmodels

<!-- b002300 | prose | pages [13] -->
• Resident Satisfaction Q(t):

<!-- b002301 | prose | pages [13] -->
A social metric evaluating how tourism impacts local communities. It accounts for factors such as congestion, public services, and overall community well-being.

<!-- b002302 | prose | pages [13] -->
In sum, our model aims to maximize the profit derived from tourism while ensur- ing environmental sustainability and maintaining resident satisfaction. The optimization problem is formulated as follows:

<!-- b002303 | prose | pages [13] -->
V(t) = τ(t),M(t) {P(t) + ω4E(t) + ω5Q(t) + γV(t + 1)} max

<!-- b002304 | prose | pages [13] -->
3.5.2 Variables Serving as Constraints

<!-- b002305 | prose | pages [13] -->
(15)

<!-- b002306 | prose | pages [13] -->
The optimization is subject to several constraints that ensure sustainability across mul- tiple dimensions:

<!-- b002307 | prose | pages [13] -->
T(t) ≤Cmax (16)

<!-- b002308 | prose | pages [13] -->
E(t) ≥Emin (17)

<!-- b002309 | prose | pages [13] -->
Q(t) ≥Qmin (18)

<!-- b002310 | prose | pages [13] -->
G(t) ≥M(t)

<!-- b002311 | prose | pages [13] -->
where:

<!-- b002312 | prose | pages [13] -->
(19)

<!-- b002313 | prose | pages [13] -->
• Cmax – the maximum carrying capacity of Juneau’s infrastructure,

<!-- b002314 | prose | pages [13] -->
• Emin – the minimum acceptable environmental index to ensure sustainability,

<!-- b002315 | prose | pages [13] -->
• Qmin – the minimum threshold for resident satisfaction,

<!-- b002316 | prose | pages [13] -->
• M(t) – government expenditures in sustainability initiatives.

<!-- b002317 | furniture | pages [14] -->
Team # 2504448

<!-- b002318 | prose | pages [14] -->
3.5.3 Decision Variables

<!-- b002319 | furniture | pages [14] -->
Page 14 of 25

<!-- b002320 | prose | pages [14] -->
Our model considers the following decision variables to optimize tourism growth while maintaining sustainability:

<!-- b002321 | prose | pages [14] -->
• τ(t) - The tax rate imposed on tourism revenue, influencing both government rev- enue and resident satisfaction.

<!-- b002322 | prose | pages [14] -->
• M(t) - Government spending allocated to attract tourists and stimulate economic growth.

<!-- b002323 | prose | pages [14] -->
3.5.4

<!-- b002324 | heading | pages [14] -->
Solution Approach

<!-- b002325 | prose | pages [14] -->
m

<!-- b002326 | prose | pages [14] -->
m

<!-- b002327 | prose | pages [14] -->
m

<!-- b002328 | prose | pages [14] -->
m

<!-- b002329 | prose | pages [14] -->
m

<!-- b002330 | prose | pages [14] -->
m

<!-- b002331 | prose | pages [14] -->
m

<!-- b002332 | prose | pages [14] -->
m

<!-- b002333 | prose | pages [14] -->
m

<!-- b002334 | prose | pages [14] -->
m

<!-- b002335 | prose | pages [14] -->
m

<!-- b002336 | prose | pages [14] -->
m

<!-- b002337 | prose | pages [14] -->
m

<!-- b002338 | prose | pages [14] -->
m

<!-- b002339 | prose | pages [14] -->
m

<!-- b002340 | prose | pages [14] -->
m

<!-- b002341 | prose | pages [14] -->
m

<!-- b002342 | prose | pages [14] -->
m

<!-- b002343 | prose | pages [14] -->
m

<!-- b002344 | prose | pages [14] -->
m

<!-- b002345 | prose | pages [14] -->
m

<!-- b002346 | prose | pages [14] -->
m

<!-- b002347 | prose | pages [14] -->
m

<!-- b002348 | prose | pages [14] -->
m

<!-- b002349 | prose | pages [14] -->
m

<!-- b002350 | prose | pages [14] -->
m

<!-- b002351 | prose | pages [14] -->
m

<!-- b002352 | prose | pages [14] -->
m

<!-- b002353 | prose | pages [14] -->
m

<!-- b002354 | prose | pages [14] -->
m

<!-- b002355 | prose | pages [14] -->
m

<!-- b002356 | prose | pages [14] -->
m

<!-- b002357 | prose | pages [14] -->
m

<!-- b002358 | prose | pages [14] -->
m

<!-- b002359 | prose | pages [14] -->
m

<!-- b002360 | prose | pages [14] -->
m

<!-- b002361 | prose | pages [14] -->
m

<!-- b002362 | prose | pages [14] -->
m

<!-- b002363 | prose | pages [14] -->
m

<!-- b002364 | prose | pages [14] -->
m

<!-- b002365 | prose | pages [14] -->
m

<!-- b002366 | prose | pages [14] -->
m

<!-- b002367 | prose | pages [14] -->
m

<!-- b002368 | prose | pages [14] -->
m

<!-- b002369 | prose | pages [14] -->
m

<!-- b002370 | prose | pages [14] -->
m

<!-- b002371 | prose | pages [14] -->
m

<!-- b002372 | prose | pages [14] -->
m

<!-- b002373 | prose | pages [14] -->
m

<!-- b002374 | prose | pages [14] -->
m

<!-- b002375 | prose | pages [14] -->
m

<!-- b002376 | prose | pages [14] -->
m

<!-- b002377 | prose | pages [14] -->
m

<!-- b002378 | prose | pages [14] -->
m

<!-- b002379 | prose | pages [14] -->
m

<!-- b002380 | prose | pages [14] -->
m

<!-- b002381 | prose | pages [14] -->
m

<!-- b002382 | prose | pages [14] -->
m

<!-- b002383 | prose | pages [14] -->
m

<!-- b002384 | prose | pages [14] -->
m

<!-- b002385 | prose | pages [14] -->
m

<!-- b002386 | prose | pages [14] -->
m

<!-- b002387 | prose | pages [14] -->
m

<!-- b002388 | prose | pages [14] -->
m

<!-- b002389 | prose | pages [14] -->
m

<!-- b002390 | prose | pages [14] -->
m

<!-- b002391 | prose | pages [14] -->
m

<!-- b002392 | prose | pages [14] -->
m

<!-- b002393 | prose | pages [14] -->
m

<!-- b002394 | prose | pages [14] -->
m

<!-- b002395 | prose | pages [14] -->
m

<!-- b002396 | prose | pages [14] -->
m

<!-- b002397 | prose | pages [14] -->
m

<!-- b002398 | prose | pages [14] -->
m

<!-- b002399 | prose | pages [14] -->
m

<!-- b002400 | prose | pages [14] -->
m

<!-- b002401 | prose | pages [14] -->
m

<!-- b002402 | prose | pages [14] -->
m

<!-- b002403 | prose | pages [14] -->
m

<!-- b002404 | prose | pages [14] -->
m

<!-- b002405 | prose | pages [14] -->
m

<!-- b002406 | prose | pages [14] -->
m

<!-- b002407 | prose | pages [14] -->
m

<!-- b002408 | prose | pages [14] -->
m

<!-- b002409 | prose | pages [14] -->
m

<!-- b002410 | prose | pages [14] -->
m

<!-- b002411 | prose | pages [14] -->
m

<!-- b002412 | prose | pages [14] -->
m

<!-- b002413 | prose | pages [14] -->
m

<!-- b002414 | prose | pages [14] -->
m

<!-- b002415 | prose | pages [14] -->
m

<!-- b002416 | prose | pages [14] -->
m

<!-- b002417 | prose | pages [14] -->
m

<!-- b002418 | prose | pages [14] -->
m

<!-- b002419 | prose | pages [14] -->
m

<!-- b002420 | prose | pages [14] -->
m

<!-- b002421 | prose | pages [14] -->
m

<!-- b002422 | prose | pages [14] -->
m

<!-- b002423 | prose | pages [14] -->
m

<!-- b002424 | prose | pages [14] -->
m

<!-- b002425 | prose | pages [14] -->
m

<!-- b002426 | prose | pages [14] -->
m

<!-- b002427 | prose | pages [14] -->
m

<!-- b002428 | prose | pages [14] -->
m

<!-- b002429 | prose | pages [14] -->
m

<!-- b002430 | prose | pages [14] -->
m

<!-- b002431 | prose | pages [14] -->
m

<!-- b002432 | prose | pages [14] -->
m

<!-- b002433 | prose | pages [14] -->
m

<!-- b002434 | prose | pages [14] -->
m

<!-- b002435 | prose | pages [14] -->
m

<!-- b002436 | prose | pages [14] -->
m

<!-- b002437 | prose | pages [14] -->
m

<!-- b002438 | prose | pages [14] -->
m

<!-- b002439 | prose | pages [14] -->
m

<!-- b002440 | prose | pages [14] -->
m

<!-- b002441 | prose | pages [14] -->
m

<!-- b002442 | prose | pages [14] -->
m

<!-- b002443 | prose | pages [14] -->
m

<!-- b002444 | prose | pages [14] -->
m

<!-- b002445 | prose | pages [14] -->
m

<!-- b002446 | prose | pages [14] -->
m

<!-- b002447 | prose | pages [14] -->
m

<!-- b002448 | prose | pages [14] -->
m

<!-- b002449 | prose | pages [14] -->
m

<!-- b002450 | prose | pages [14] -->
m

<!-- b002451 | prose | pages [14] -->
m

<!-- b002452 | prose | pages [14] -->
m

<!-- b002453 | prose | pages [14] -->
m

<!-- b002454 | prose | pages [14] -->
m

<!-- b002455 | prose | pages [14] -->
m

<!-- b002456 | prose | pages [14] -->
m

<!-- b002457 | prose | pages [14] -->
m

<!-- b002458 | prose | pages [14] -->
m

<!-- b002459 | prose | pages [14] -->
m

<!-- b002460 | prose | pages [14] -->
m

<!-- b002461 | prose | pages [14] -->
m

<!-- b002462 | prose | pages [14] -->
m

<!-- b002463 | prose | pages [14] -->
m

<!-- b002464 | prose | pages [14] -->
m

<!-- b002465 | prose | pages [14] -->
m

<!-- b002466 | prose | pages [14] -->
m

<!-- b002467 | prose | pages [14] -->
m

<!-- b002468 | prose | pages [14] -->
m

<!-- b002469 | prose | pages [14] -->
m

<!-- b002470 | prose | pages [14] -->
m

<!-- b002471 | prose | pages [14] -->
m

<!-- b002472 | prose | pages [14] -->
m

<!-- b002473 | prose | pages [14] -->
m

<!-- b002474 | prose | pages [14] -->
m

<!-- b002475 | prose | pages [14] -->
m

<!-- b002476 | prose | pages [14] -->
m

<!-- b002477 | prose | pages [14] -->
m

<!-- b002478 | prose | pages [14] -->
m

<!-- b002479 | prose | pages [14] -->
m

<!-- b002480 | prose | pages [14] -->
m

<!-- b002481 | prose | pages [14] -->
m

<!-- b002482 | prose | pages [14] -->
m

<!-- b002483 | prose | pages [14] -->
m

<!-- b002484 | prose | pages [14] -->
m

<!-- b002485 | prose | pages [14] -->
m

<!-- b002486 | prose | pages [14] -->
m

<!-- b002487 | prose | pages [14] -->
m

<!-- b002488 | prose | pages [14] -->
m

<!-- b002489 | prose | pages [14] -->
m

<!-- b002490 | prose | pages [14] -->
m

<!-- b002491 | prose | pages [14] -->
m

<!-- b002492 | prose | pages [14] -->
m

<!-- b002493 | prose | pages [14] -->
m

<!-- b002494 | prose | pages [14] -->
m

<!-- b002495 | prose | pages [14] -->
m

<!-- b002496 | prose | pages [14] -->
m

<!-- b002497 | prose | pages [14] -->
m

<!-- b002498 | prose | pages [14] -->
m

<!-- b002499 | prose | pages [14] -->
m

<!-- b002500 | prose | pages [14] -->
m

<!-- b002501 | prose | pages [14] -->
m

<!-- b002502 | prose | pages [14] -->
m

<!-- b002503 | prose | pages [14] -->
m

<!-- b002504 | prose | pages [14] -->
m

<!-- b002505 | prose | pages [14] -->
m

<!-- b002506 | prose | pages [14] -->
m

<!-- b002507 | prose | pages [14] -->
m

<!-- b002508 | prose | pages [14] -->
m

<!-- b002509 | prose | pages [14] -->
m

<!-- b002510 | prose | pages [14] -->
m

<!-- b002511 | prose | pages [14] -->
m

<!-- b002512 | prose | pages [14] -->
m

<!-- b002513 | prose | pages [14] -->
m

<!-- b002514 | prose | pages [14] -->
m

<!-- b002515 | prose | pages [14] -->
m

<!-- b002516 | prose | pages [14] -->
m

<!-- b002517 | prose | pages [14] -->
m

<!-- b002518 | prose | pages [14] -->
m

<!-- b002519 | prose | pages [14] -->
m

<!-- b002520 | prose | pages [14] -->
m

<!-- b002521 | prose | pages [14] -->
m

<!-- b002522 | prose | pages [14] -->
m

<!-- b002523 | prose | pages [14] -->
m

<!-- b002524 | prose | pages [14] -->
m

<!-- b002525 | prose | pages [14] -->
m

<!-- b002526 | prose | pages [14] -->
m

<!-- b002527 | prose | pages [14] -->
m

<!-- b002528 | prose | pages [14] -->
m

<!-- b002529 | prose | pages [14] -->
m

<!-- b002530 | prose | pages [14] -->
m

<!-- b002531 | prose | pages [14] -->
m

<!-- b002532 | prose | pages [14] -->
m

<!-- b002533 | prose | pages [14] -->
m

<!-- b002534 | prose | pages [14] -->
m

<!-- b002535 | prose | pages [14] -->
m

<!-- b002536 | prose | pages [14] -->
m

<!-- b002537 | prose | pages [14] -->
m

<!-- b002538 | prose | pages [14] -->
m

<!-- b002539 | prose | pages [14] -->
m

<!-- b002540 | prose | pages [14] -->
m

<!-- b002541 | prose | pages [14] -->
m

<!-- b002542 | prose | pages [14] -->
m

<!-- b002543 | prose | pages [14] -->
m

<!-- b002544 | prose | pages [14] -->
m

<!-- b002545 | prose | pages [14] -->
m

<!-- b002546 | prose | pages [14] -->
m

<!-- b002547 | prose | pages [14] -->
m

<!-- b002548 | prose | pages [14] -->
m

<!-- b002549 | prose | pages [14] -->
m

<!-- b002550 | prose | pages [14] -->
m

<!-- b002551 | prose | pages [14] -->
m

<!-- b002552 | prose | pages [14] -->
m

<!-- b002553 | prose | pages [14] -->
m

<!-- b002554 | prose | pages [14] -->
m

<!-- b002555 | prose | pages [14] -->
m

<!-- b002556 | prose | pages [14] -->
m

<!-- b002557 | prose | pages [14] -->
m

<!-- b002558 | prose | pages [14] -->
m

<!-- b002559 | prose | pages [14] -->
m

<!-- b002560 | prose | pages [14] -->
m

<!-- b002561 | prose | pages [14] -->
m

<!-- b002562 | prose | pages [14] -->
m

<!-- b002563 | prose | pages [14] -->
m

<!-- b002564 | prose | pages [14] -->
m

<!-- b002565 | prose | pages [14] -->
m

<!-- b002566 | prose | pages [14] -->
m

<!-- b002567 | prose | pages [14] -->
m

<!-- b002568 | prose | pages [14] -->
m

<!-- b002569 | prose | pages [14] -->
m

<!-- b002570 | prose | pages [14] -->
m

<!-- b002571 | prose | pages [14] -->
m

<!-- b002572 | prose | pages [14] -->
m

<!-- b002573 | prose | pages [14] -->
m

<!-- b002574 | prose | pages [14] -->
m

<!-- b002575 | prose | pages [14] -->
m

<!-- b002576 | prose | pages [14] -->
m

<!-- b002577 | prose | pages [14] -->
m

<!-- b002578 | prose | pages [14] -->
m

<!-- b002579 | prose | pages [14] -->
m

<!-- b002580 | prose | pages [14] -->
m

<!-- b002581 | prose | pages [14] -->
m

<!-- b002582 | prose | pages [14] -->
m

<!-- b002583 | prose | pages [14] -->
m

<!-- b002584 | prose | pages [14] -->
m

<!-- b002585 | prose | pages [14] -->
m

<!-- b002586 | prose | pages [14] -->
m

<!-- b002587 | prose | pages [14] -->
m

<!-- b002588 | prose | pages [14] -->
m

<!-- b002589 | prose | pages [14] -->
m

<!-- b002590 | prose | pages [14] -->
m

<!-- b002591 | prose | pages [14] -->
m

<!-- b002592 | prose | pages [14] -->
m

<!-- b002593 | prose | pages [14] -->
m

<!-- b002594 | prose | pages [14] -->
m

<!-- b002595 | prose | pages [14] -->
m

<!-- b002596 | prose | pages [14] -->
m

<!-- b002597 | prose | pages [14] -->
m

<!-- b002598 | prose | pages [14] -->
m

<!-- b002599 | prose | pages [14] -->
m

<!-- b002600 | prose | pages [14] -->
m

<!-- b002601 | prose | pages [14] -->
m

<!-- b002602 | prose | pages [14] -->
m

<!-- b002603 | prose | pages [14] -->
m

<!-- b002604 | prose | pages [14] -->
m

<!-- b002605 | prose | pages [14] -->
m

<!-- b002606 | prose | pages [14] -->
m

<!-- b002607 | prose | pages [14] -->
m

<!-- b002608 | prose | pages [14] -->
m

<!-- b002609 | prose | pages [14] -->
m

<!-- b002610 | prose | pages [14] -->
m

<!-- b002611 | prose | pages [14] -->
m

<!-- b002612 | prose | pages [14] -->
m

<!-- b002613 | prose | pages [14] -->
m

<!-- b002614 | prose | pages [14] -->
m

<!-- b002615 | prose | pages [14] -->
m

<!-- b002616 | prose | pages [14] -->
m

<!-- b002617 | prose | pages [14] -->
m

<!-- b002618 | prose | pages [14] -->
m

<!-- b002619 | prose | pages [14] -->
m

<!-- b002620 | prose | pages [14] -->
m

<!-- b002621 | prose | pages [14] -->
m

<!-- b002622 | prose | pages [14] -->
m

<!-- b002623 | prose | pages [14] -->
m

<!-- b002624 | prose | pages [14] -->
m

<!-- b002625 | prose | pages [14] -->
m

<!-- b002626 | prose | pages [14] -->
m

<!-- b002627 | prose | pages [14] -->
m

<!-- b002628 | prose | pages [14] -->
m

<!-- b002629 | prose | pages [14] -->
m

<!-- b002630 | prose | pages [14] -->
m

<!-- b002631 | prose | pages [14] -->
m

<!-- b002632 | prose | pages [14] -->
m

<!-- b002633 | prose | pages [14] -->
m

<!-- b002634 | prose | pages [14] -->
m

<!-- b002635 | prose | pages [14] -->
m

<!-- b002636 | prose | pages [14] -->
m

<!-- b002637 | prose | pages [14] -->
m

<!-- b002638 | prose | pages [14] -->
m

<!-- b002639 | prose | pages [14] -->
m

<!-- b002640 | prose | pages [14] -->
m

<!-- b002641 | prose | pages [14] -->
m

<!-- b002642 | prose | pages [14] -->
m

<!-- b002643 | prose | pages [14] -->
m

<!-- b002644 | prose | pages [14] -->
m

<!-- b002645 | prose | pages [14] -->
m

<!-- b002646 | prose | pages [14] -->
m

<!-- b002647 | prose | pages [14] -->
m

<!-- b002648 | prose | pages [14] -->
m

<!-- b002649 | prose | pages [14] -->
m

<!-- b002650 | prose | pages [14] -->
m

<!-- b002651 | prose | pages [14] -->
m

<!-- b002652 | prose | pages [14] -->
m

<!-- b002653 | prose | pages [14] -->
m

<!-- b002654 | prose | pages [14] -->
m

<!-- b002655 | prose | pages [14] -->
m

<!-- b002656 | prose | pages [14] -->
m

<!-- b002657 | prose | pages [14] -->
m

<!-- b002658 | prose | pages [14] -->
m

<!-- b002659 | prose | pages [14] -->
m

<!-- b002660 | prose | pages [14] -->
m

<!-- b002661 | prose | pages [14] -->
m

<!-- b002662 | prose | pages [14] -->
m

<!-- b002663 | prose | pages [14] -->
m

<!-- b002664 | prose | pages [14] -->
m

<!-- b002665 | prose | pages [14] -->
m

<!-- b002666 | prose | pages [14] -->
m

<!-- b002667 | prose | pages [14] -->
m

<!-- b002668 | prose | pages [14] -->
m

<!-- b002669 | prose | pages [14] -->
m

<!-- b002670 | prose | pages [14] -->
m

<!-- b002671 | prose | pages [14] -->
m

<!-- b002672 | prose | pages [14] -->
m

<!-- b002673 | prose | pages [14] -->
m

<!-- b002674 | prose | pages [14] -->
m

<!-- b002675 | prose | pages [14] -->
m

<!-- b002676 | prose | pages [14] -->
m

<!-- b002677 | prose | pages [14] -->
m

<!-- b002678 | prose | pages [14] -->
m

<!-- b002679 | prose | pages [14] -->
m

<!-- b002680 | prose | pages [14] -->
m

<!-- b002681 | prose | pages [14] -->
m

<!-- b002682 | prose | pages [14] -->
m

<!-- b002683 | prose | pages [14] -->
m

<!-- b002684 | prose | pages [14] -->
m

<!-- b002685 | prose | pages [14] -->
m

<!-- b002686 | prose | pages [14] -->
m

<!-- b002687 | prose | pages [14] -->
m

<!-- b002688 | prose | pages [14] -->
m

<!-- b002689 | prose | pages [14] -->
m

<!-- b002690 | prose | pages [14] -->
m

<!-- b002691 | prose | pages [14] -->
m

<!-- b002692 | prose | pages [14] -->
m

<!-- b002693 | prose | pages [14] -->
m

<!-- b002694 | prose | pages [14] -->
m

<!-- b002695 | prose | pages [14] -->
m

<!-- b002696 | prose | pages [14] -->
m

<!-- b002697 | prose | pages [14] -->
m

<!-- b002698 | prose | pages [14] -->
m

<!-- b002699 | prose | pages [14] -->
m

<!-- b002700 | prose | pages [14] -->
m

<!-- b002701 | prose | pages [14] -->
m

<!-- b002702 | prose | pages [14] -->
m

<!-- b002703 | prose | pages [14] -->
m

<!-- b002704 | prose | pages [14] -->
m

<!-- b002705 | prose | pages [14] -->
m

<!-- b002706 | prose | pages [14] -->
m

<!-- b002707 | prose | pages [14] -->
m

<!-- b002708 | prose | pages [14] -->
m

<!-- b002709 | prose | pages [14] -->
m

<!-- b002710 | prose | pages [14] -->
m

<!-- b002711 | prose | pages [14] -->
m

<!-- b002712 | prose | pages [14] -->
m

<!-- b002713 | prose | pages [14] -->
m

<!-- b002714 | prose | pages [14] -->
m

<!-- b002715 | prose | pages [14] -->
m

<!-- b002716 | prose | pages [14] -->
m

<!-- b002717 | prose | pages [14] -->
m

<!-- b002718 | prose | pages [14] -->
m

<!-- b002719 | prose | pages [14] -->
m

<!-- b002720 | prose | pages [14] -->
m

<!-- b002721 | prose | pages [14] -->
m

<!-- b002722 | prose | pages [14] -->
m

<!-- b002723 | prose | pages [14] -->
m

<!-- b002724 | prose | pages [14] -->
m

<!-- b002725 | prose | pages [14] -->
m

<!-- b002726 | prose | pages [14] -->
m

<!-- b002727 | prose | pages [14] -->
m

<!-- b002728 | prose | pages [14] -->
m

<!-- b002729 | prose | pages [14] -->
m

<!-- b002730 | prose | pages [14] -->
m

<!-- b002731 | prose | pages [14] -->
m

<!-- b002732 | prose | pages [14] -->
m

<!-- b002733 | prose | pages [14] -->
m

<!-- b002734 | prose | pages [14] -->
m

<!-- b002735 | prose | pages [14] -->
m

<!-- b002736 | prose | pages [14] -->
m

<!-- b002737 | prose | pages [14] -->
m

<!-- b002738 | prose | pages [14] -->
m

<!-- b002739 | prose | pages [14] -->
m

<!-- b002740 | prose | pages [14] -->
m

<!-- b002741 | prose | pages [14] -->
m

<!-- b002742 | prose | pages [14] -->
m

<!-- b002743 | prose | pages [14] -->
m

<!-- b002744 | prose | pages [14] -->
m

<!-- b002745 | prose | pages [14] -->
m

<!-- b002746 | prose | pages [14] -->
m

<!-- b002747 | prose | pages [14] -->
m

<!-- b002748 | prose | pages [14] -->
m

<!-- b002749 | prose | pages [14] -->
m

<!-- b002750 | prose | pages [14] -->
m

<!-- b002751 | prose | pages [14] -->
m

<!-- b002752 | prose | pages [14] -->
m

<!-- b002753 | prose | pages [14] -->
m

<!-- b002754 | prose | pages [14] -->
m

<!-- b002755 | prose | pages [14] -->
m

<!-- b002756 | prose | pages [14] -->
m

<!-- b002757 | prose | pages [14] -->
m

<!-- b002758 | prose | pages [14] -->
m

<!-- b002759 | prose | pages [14] -->
m

<!-- b002760 | prose | pages [14] -->
m

<!-- b002761 | prose | pages [14] -->
m

<!-- b002762 | prose | pages [14] -->
m

<!-- b002763 | prose | pages [14] -->
m

<!-- b002764 | prose | pages [14] -->
m

<!-- b002765 | prose | pages [14] -->
m

<!-- b002766 | prose | pages [14] -->
m

<!-- b002767 | prose | pages [14] -->
m

<!-- b002768 | prose | pages [14] -->
m

<!-- b002769 | prose | pages [14] -->
m

<!-- b002770 | prose | pages [14] -->
m

<!-- b002771 | prose | pages [14] -->
m

<!-- b002772 | prose | pages [14] -->
m

<!-- b002773 | prose | pages [14] -->
m

<!-- b002774 | prose | pages [14] -->
m

<!-- b002775 | prose | pages [14] -->
m

<!-- b002776 | prose | pages [14] -->
m

<!-- b002777 | prose | pages [14] -->
m

<!-- b002778 | prose | pages [14] -->
m

<!-- b002779 | prose | pages [14] -->
m

<!-- b002780 | prose | pages [14] -->
m

<!-- b002781 | prose | pages [14] -->
m

<!-- b002782 | prose | pages [14] -->
m

<!-- b002783 | prose | pages [14] -->
m

<!-- b002784 | prose | pages [14] -->
m

<!-- b002785 | prose | pages [14] -->
m

<!-- b002786 | prose | pages [14] -->
m

<!-- b002787 | prose | pages [14] -->
m

<!-- b002788 | prose | pages [14] -->
m

<!-- b002789 | prose | pages [14] -->
m

<!-- b002790 | prose | pages [14] -->
m

<!-- b002791 | prose | pages [14] -->
m

<!-- b002792 | prose | pages [14] -->
m

<!-- b002793 | prose | pages [14] -->
m

<!-- b002794 | prose | pages [14] -->
m

<!-- b002795 | prose | pages [14] -->
m

<!-- b002796 | prose | pages [14] -->
m

<!-- b002797 | prose | pages [14] -->
m

<!-- b002798 | prose | pages [14] -->
m

<!-- b002799 | prose | pages [14] -->
m

<!-- b002800 | prose | pages [14] -->
m

<!-- b002801 | prose | pages [14] -->
m

<!-- b002802 | prose | pages [14] -->
m

<!-- b002803 | prose | pages [14] -->
m

<!-- b002804 | prose | pages [14] -->
m

<!-- b002805 | prose | pages [14] -->
m

<!-- b002806 | prose | pages [14] -->
m

<!-- b002807 | prose | pages [14] -->
m

<!-- b002808 | prose | pages [14] -->
m

<!-- b002809 | prose | pages [14] -->
m

<!-- b002810 | prose | pages [14] -->
m

<!-- b002811 | prose | pages [14] -->
m

<!-- b002812 | prose | pages [14] -->
m

<!-- b002813 | prose | pages [14] -->
m

<!-- b002814 | prose | pages [14] -->
m

<!-- b002815 | prose | pages [14] -->
m

<!-- b002816 | prose | pages [14] -->
m

<!-- b002817 | prose | pages [14] -->
m

<!-- b002818 | prose | pages [14] -->
m

<!-- b002819 | prose | pages [14] -->
m

<!-- b002820 | prose | pages [14] -->
m

<!-- b002821 | prose | pages [14] -->
m

<!-- b002822 | prose | pages [14] -->
m

<!-- b002823 | prose | pages [14] -->
m

<!-- b002824 | prose | pages [14] -->
m

<!-- b002825 | prose | pages [14] -->
m

<!-- b002826 | prose | pages [14] -->
m

<!-- b002827 | prose | pages [14] -->
m

<!-- b002828 | prose | pages [14] -->
m

<!-- b002829 | prose | pages [14] -->
m

<!-- b002830 | prose | pages [14] -->
m

<!-- b002831 | prose | pages [14] -->
m

<!-- b002832 | prose | pages [14] -->
m

<!-- b002833 | prose | pages [14] -->
m

<!-- b002834 | prose | pages [14] -->
m

<!-- b002835 | prose | pages [14] -->
m

<!-- b002836 | prose | pages [14] -->
m

<!-- b002837 | prose | pages [14] -->
m

<!-- b002838 | prose | pages [14] -->
m

<!-- b002839 | prose | pages [14] -->
m

<!-- b002840 | prose | pages [14] -->
m

<!-- b002841 | prose | pages [14] -->
m

<!-- b002842 | prose | pages [14] -->
m

<!-- b002843 | prose | pages [14] -->
m

<!-- b002844 | prose | pages [14] -->
m

<!-- b002845 | prose | pages [14] -->
m

<!-- b002846 | prose | pages [14] -->
m

<!-- b002847 | prose | pages [14] -->
m

<!-- b002848 | prose | pages [14] -->
m

<!-- b002849 | prose | pages [14] -->
m

<!-- b002850 | prose | pages [14] -->
m

<!-- b002851 | prose | pages [14] -->
m

<!-- b002852 | prose | pages [14] -->
m

<!-- b002853 | prose | pages [14] -->
m

<!-- b002854 | prose | pages [14] -->
m

<!-- b002855 | prose | pages [14] -->
m

<!-- b002856 | prose | pages [14] -->
m

<!-- b002857 | prose | pages [14] -->
m

<!-- b002858 | prose | pages [14] -->
m

<!-- b002859 | prose | pages [14] -->
m

<!-- b002860 | prose | pages [14] -->
m

<!-- b002861 | prose | pages [14] -->
m

<!-- b002862 | prose | pages [14] -->
m

<!-- b002863 | prose | pages [14] -->
m

<!-- b002864 | prose | pages [14] -->
m

<!-- b002865 | prose | pages [14] -->
m

<!-- b002866 | prose | pages [14] -->
m

<!-- b002867 | prose | pages [14] -->
m

<!-- b002868 | prose | pages [14] -->
m

<!-- b002869 | prose | pages [14] -->
m

<!-- b002870 | prose | pages [14] -->
m

<!-- b002871 | prose | pages [14] -->
m

<!-- b002872 | prose | pages [14] -->
m

<!-- b002873 | prose | pages [14] -->
m

<!-- b002874 | prose | pages [14] -->
m

<!-- b002875 | prose | pages [14] -->
m

<!-- b002876 | prose | pages [14] -->
m

<!-- b002877 | prose | pages [14] -->
m

<!-- b002878 | prose | pages [14] -->
m

<!-- b002879 | prose | pages [14] -->
m

<!-- b002880 | prose | pages [14] -->
m

<!-- b002881 | prose | pages [14] -->
m

<!-- b002882 | prose | pages [14] -->
m

<!-- b002883 | prose | pages [14] -->
m

<!-- b002884 | prose | pages [14] -->
m

<!-- b002885 | prose | pages [14] -->
m

<!-- b002886 | prose | pages [14] -->
m

<!-- b002887 | prose | pages [14] -->
m

<!-- b002888 | prose | pages [14] -->
m

<!-- b002889 | prose | pages [14] -->
m

<!-- b002890 | prose | pages [14] -->
m

<!-- b002891 | prose | pages [14] -->
m

<!-- b002892 | prose | pages [14] -->
m

<!-- b002893 | prose | pages [14] -->
m

<!-- b002894 | prose | pages [14] -->
m

<!-- b002895 | prose | pages [14] -->
m

<!-- b002896 | prose | pages [14] -->
m

<!-- b002897 | prose | pages [14] -->
m

<!-- b002898 | prose | pages [14] -->
m

<!-- b002899 | prose | pages [14] -->
m

<!-- b002900 | prose | pages [14] -->
m

<!-- b002901 | prose | pages [14] -->
m

<!-- b002902 | prose | pages [14] -->
m

<!-- b002903 | prose | pages [14] -->
m

<!-- b002904 | prose | pages [14] -->
m

<!-- b002905 | prose | pages [14] -->
m

<!-- b002906 | prose | pages [14] -->
m

<!-- b002907 | prose | pages [14] -->
m

<!-- b002908 | prose | pages [14] -->
m

<!-- b002909 | prose | pages [14] -->
m

<!-- b002910 | prose | pages [14] -->
m

<!-- b002911 | prose | pages [14] -->
m

<!-- b002912 | prose | pages [14] -->
m

<!-- b002913 | prose | pages [14] -->
m

<!-- b002914 | prose | pages [14] -->
m

<!-- b002915 | prose | pages [14] -->
m

<!-- b002916 | prose | pages [14] -->
m

<!-- b002917 | prose | pages [14] -->
m

<!-- b002918 | prose | pages [14] -->
m

<!-- b002919 | prose | pages [14] -->
m

<!-- b002920 | prose | pages [14] -->
m

<!-- b002921 | prose | pages [14] -->
m

<!-- b002922 | prose | pages [14] -->
m

<!-- b002923 | prose | pages [14] -->
m

<!-- b002924 | prose | pages [14] -->
m

<!-- b002925 | prose | pages [14] -->
m

<!-- b002926 | prose | pages [14] -->
m

<!-- b002927 | prose | pages [14] -->
m

<!-- b002928 | prose | pages [14] -->
m

<!-- b002929 | prose | pages [14] -->
m

<!-- b002930 | prose | pages [14] -->
m

<!-- b002931 | prose | pages [14] -->
m

<!-- b002932 | prose | pages [14] -->
m

<!-- b002933 | prose | pages [14] -->
m

<!-- b002934 | prose | pages [14] -->
m

<!-- b002935 | prose | pages [14] -->
m

<!-- b002936 | prose | pages [14] -->
m

<!-- b002937 | prose | pages [14] -->
m

<!-- b002938 | prose | pages [14] -->
m

<!-- b002939 | prose | pages [14] -->
m

<!-- b002940 | prose | pages [14] -->
m

<!-- b002941 | prose | pages [14] -->
m

<!-- b002942 | prose | pages [14] -->
m

<!-- b002943 | prose | pages [14] -->
m

<!-- b002944 | prose | pages [14] -->
m

<!-- b002945 | prose | pages [14] -->
m

<!-- b002946 | prose | pages [14] -->
m

<!-- b002947 | prose | pages [14] -->
m

<!-- b002948 | prose | pages [14] -->
m

<!-- b002949 | prose | pages [14] -->
m

<!-- b002950 | prose | pages [14] -->
m

<!-- b002951 | prose | pages [14] -->
m

<!-- b002952 | prose | pages [14] -->
The system evolves over time according to the following state transition equations, as equation (1), equation (13), equation (14):

<!-- b002953 | prose | pages [14] -->
m

<!-- b002954 | prose | pages [14] -->
m

<!-- b002955 | prose | pages [14] -->
m

<!-- b002956 | prose | pages [14] -->
m

<!-- b002957 | prose | pages [14] -->
m

<!-- b002958 | prose | pages [14] -->
m

<!-- b002959 | prose | pages [14] -->
m

<!-- b002960 | prose | pages [14] -->
m

<!-- b002961 | prose | pages [14] -->
m

<!-- b002962 | prose | pages [14] -->
m

<!-- b002963 | prose | pages [14] -->
m

<!-- b002964 | prose | pages [14] -->
m

<!-- b002965 | prose | pages [14] -->
m

<!-- b002966 | prose | pages [14] -->
m

<!-- b002967 | prose | pages [14] -->
m

<!-- b002968 | prose | pages [14] -->
m

<!-- b002969 | prose | pages [14] -->
m

<!-- b002970 | prose | pages [14] -->
m

<!-- b002971 | prose | pages [14] -->
m

<!-- b002972 | prose | pages [14] -->
m

<!-- b002973 | prose | pages [14] -->
m

<!-- b002974 | prose | pages [14] -->
m

<!-- b002975 | prose | pages [14] -->
m

<!-- b002976 | prose | pages [14] -->
m

<!-- b002977 | prose | pages [14] -->
m

<!-- b002978 | prose | pages [14] -->
m

<!-- b002979 | prose | pages [14] -->
m

<!-- b002980 | prose | pages [14] -->
m

<!-- b002981 | prose | pages [14] -->
m

<!-- b002982 | prose | pages [14] -->
m

<!-- b002983 | prose | pages [14] -->
m

<!-- b002984 | prose | pages [14] -->
m

<!-- b002985 | prose | pages [14] -->
m

<!-- b002986 | prose | pages [14] -->
m

<!-- b002987 | prose | pages [14] -->
m

<!-- b002988 | prose | pages [14] -->
m

<!-- b002989 | prose | pages [14] -->
m

<!-- b002990 | prose | pages [14] -->
m

<!-- b002991 | prose | pages [14] -->
m

<!-- b002992 | prose | pages [14] -->
m

<!-- b002993 | prose | pages [14] -->
m

<!-- b002994 | prose | pages [14] -->
m

<!-- b002995 | prose | pages [14] -->
m

<!-- b002996 | prose | pages [14] -->
m

<!-- b002997 | prose | pages [14] -->
m

<!-- b002998 | prose | pages [14] -->
m

<!-- b002999 | prose | pages [14] -->
m

<!-- b003000 | prose | pages [14] -->
m

<!-- b003001 | prose | pages [14] -->
m

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
T(t + 1) = T(t) · (1 + g(t) −γ · τ(t))

<!-- b003014 | prose | pages [14] -->
 T(t)

<!-- b003015 | prose | pages [14] -->


<!-- b003016 | prose | pages [14] -->
E(t + 1) = Esub(t) + r · (1 −Esub(t)) −h ·

<!-- b003017 | prose | pages [14] -->
Tmax

<!-- b003018 | prose | pages [14] -->
1 −|T(t + 1) −Topt|

<!-- b003019 | prose | pages [14] -->


<!-- b003020 | prose | pages [14] -->
Q(t + 1) = ω1

<!-- b003021 | prose | pages [14] -->
Topt

<!-- b003022 | prose | pages [14] -->


<!-- b003023 | prose | pages [14] -->
+ ω2E(t + 1) −ω3τ(t)

<!-- b003024 | prose | pages [14] -->
Our model solves the problem using backward dynamic programming, following these steps. First, we define state variables: tourist count T(t), environmental index E(t), and resident satisfaction Q(t). Second, we identify control variables: taxation τ(t) and promo- tional efforts M(t). Then we apply recursion to compute the optimal solution by solving equation (15) iteratively. At last, we trace back the optimal government decisions in our solution.

<!-- b003025 | caption | pages [14] -->
Figure 9: Overview of the DP approach

<!-- b003026 | prose | pages [14] -->
3.5.5

<!-- b003027 | heading | pages [14] -->
Model Solution

<!-- b003028 | prose | pages [14] -->
The model is implemented to optimize sustainable tourism management in Juneau over a following five-year period from 2024 to 2028 (since the data obtained end in 2023). The results shown in Table 3 provide insights into projected tourist numbers, environ- mental conditions, and economic performance under different demand shocks and policy interventions.

<!-- b003029 | prose | pages [14] -->
关注数学模型

<!-- b003030 | furniture | pages [14] -->
2

<!-- b003031 | furniture | pages [14] -->
MATHmodels

<!-- b003032 | furniture | pages [14] -->
获取更多资讯

<!-- b003033 | furniture | pages [15] -->
Team # 2504448

<!-- b003034 | prose | pages [15] -->
Year Tourists (ten

<!-- b003035 | prose | pages [15] -->
Tax

<!-- b003036 | prose | pages [15] -->
thousands)

<!-- b003037 | prose | pages [15] -->
Rate

<!-- b003038 | furniture | pages [15] -->
Page 15 of 25

<!-- b003039 | prose | pages [15] -->
Gov

<!-- b003040 | prose | pages [15] -->
Env Index Resident Sat

<!-- b003041 | prose | pages [15] -->
Revenue

<!-- b003042 | prose | pages [15] -->
微信公众号：数学模型

<!-- b003043 | prose | pages [15] -->
(Million $)

<!-- b003044 | prose | pages [15] -->
(%)

<!-- b003045 | prose | pages [15] -->
1 153.7 4.2 2 154.8 4.2 3 152.2 5.0 4 158.3 4.0 5 168.3 3.2 14.0 0.029 0.882 14.1 0.076 0.893 16.6 0.123 0.832 13.8 0.170 0.899 11.71 0.181 0.917

<!-- b003046 | caption | pages [15] -->
Table 3: Predictions of the optimized tourism plan for the next 5 years

<!-- b003047 | prose | pages [15] -->
微信号：MATHmodels

<!-- b003048 | prose | pages [15] -->
3.5.6

<!-- b003049 | heading | pages [15] -->
Discussion of Results

<!-- b003050 | caption | pages [15] -->
Figure 10: Visualization of model results

<!-- b003051 | prose | pages [15] -->
The results demonstrate a dynamic evolution of key metrics over the five-year period. The projected tourist population remains relatively stable, fluctuating between 1.52 mil- lion (152.2 ten thousand) and 1.68 million (168.3 ten thousand) visitors per year due to adjustments in taxation and demand shocks. The government applies varying tax rates ranging from 3.2% to 5.0%, generating steady annual revenue between $11.71 million and $16.6 million. The higher tax rates in Year 3 reflect an attempt to balance environmental

<!-- b003052 | prose | pages [15] -->
m

<!-- b003053 | prose | pages [15] -->
m

<!-- b003054 | prose | pages [15] -->
m

<!-- b003055 | prose | pages [15] -->
m

<!-- b003056 | prose | pages [15] -->
m

<!-- b003057 | prose | pages [15] -->
m

<!-- b003058 | prose | pages [15] -->
m

<!-- b003059 | prose | pages [15] -->
m

<!-- b003060 | prose | pages [15] -->
m

<!-- b003061 | prose | pages [15] -->
m

<!-- b003062 | prose | pages [15] -->
m

<!-- b003063 | prose | pages [15] -->
m

<!-- b003064 | prose | pages [15] -->
m

<!-- b003065 | prose | pages [15] -->
m

<!-- b003066 | prose | pages [15] -->
m

<!-- b003067 | prose | pages [15] -->
m

<!-- b003068 | prose | pages [15] -->
m

<!-- b003069 | prose | pages [15] -->
m

<!-- b003070 | prose | pages [15] -->
m

<!-- b003071 | prose | pages [15] -->
m

<!-- b003072 | prose | pages [15] -->
m

<!-- b003073 | prose | pages [15] -->
m

<!-- b003074 | prose | pages [15] -->
m

<!-- b003075 | prose | pages [15] -->
m

<!-- b003076 | prose | pages [15] -->
m

<!-- b003077 | prose | pages [15] -->
m

<!-- b003078 | prose | pages [15] -->
m

<!-- b003079 | prose | pages [15] -->
m

<!-- b003080 | prose | pages [15] -->
m

<!-- b003081 | prose | pages [15] -->
m

<!-- b003082 | prose | pages [15] -->
m

<!-- b003083 | prose | pages [15] -->
m

<!-- b003084 | prose | pages [15] -->
m

<!-- b003085 | prose | pages [15] -->
m

<!-- b003086 | prose | pages [15] -->
m

<!-- b003087 | prose | pages [15] -->
m

<!-- b003088 | prose | pages [15] -->
m

<!-- b003089 | prose | pages [15] -->
m

<!-- b003090 | prose | pages [15] -->
m

<!-- b003091 | prose | pages [15] -->
m

<!-- b003092 | prose | pages [15] -->
m

<!-- b003093 | prose | pages [15] -->
m

<!-- b003094 | prose | pages [15] -->
m

<!-- b003095 | prose | pages [15] -->
m

<!-- b003096 | prose | pages [15] -->
m

<!-- b003097 | prose | pages [15] -->
m

<!-- b003098 | prose | pages [15] -->
m

<!-- b003099 | prose | pages [15] -->
m

<!-- b003100 | prose | pages [15] -->
m

<!-- b003101 | prose | pages [15] -->
m

<!-- b003102 | prose | pages [15] -->
m

<!-- b003103 | prose | pages [15] -->
m

<!-- b003104 | prose | pages [15] -->
m

<!-- b003105 | prose | pages [15] -->
m

<!-- b003106 | prose | pages [15] -->
m

<!-- b003107 | prose | pages [15] -->
m

<!-- b003108 | prose | pages [15] -->
m

<!-- b003109 | prose | pages [15] -->
m

<!-- b003110 | prose | pages [15] -->
m

<!-- b003111 | prose | pages [15] -->
m

<!-- b003112 | prose | pages [15] -->
m

<!-- b003113 | prose | pages [15] -->
m

<!-- b003114 | prose | pages [15] -->
m

<!-- b003115 | prose | pages [15] -->
m

<!-- b003116 | prose | pages [15] -->
m

<!-- b003117 | prose | pages [15] -->
m

<!-- b003118 | prose | pages [15] -->
m

<!-- b003119 | prose | pages [15] -->
m

<!-- b003120 | prose | pages [15] -->
m

<!-- b003121 | prose | pages [15] -->
m

<!-- b003122 | prose | pages [15] -->
m

<!-- b003123 | prose | pages [15] -->
m

<!-- b003124 | prose | pages [15] -->
m

<!-- b003125 | prose | pages [15] -->
and social objectives, which is offset by slightly reduced tourist numbers. The environ-

<!-- b003126 | prose | pages [15] -->
m

<!-- b003127 | prose | pages [15] -->
m

<!-- b003128 | prose | pages [15] -->
m

<!-- b003129 | prose | pages [15] -->
m

<!-- b003130 | prose | pages [15] -->
m

<!-- b003131 | prose | pages [15] -->
m

<!-- b003132 | prose | pages [15] -->
m

<!-- b003133 | prose | pages [15] -->
m

<!-- b003134 | prose | pages [15] -->
m

<!-- b003135 | prose | pages [15] -->
m

<!-- b003136 | prose | pages [15] -->
m

<!-- b003137 | prose | pages [15] -->
m

<!-- b003138 | prose | pages [15] -->
m

<!-- b003139 | prose | pages [15] -->
m

<!-- b003140 | prose | pages [15] -->
m

<!-- b003141 | prose | pages [15] -->
m

<!-- b003142 | prose | pages [15] -->
m

<!-- b003143 | prose | pages [15] -->
m

<!-- b003144 | prose | pages [15] -->
m

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
m

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
mental index shows a clear upward trend, increasing from 0.029 in the first year to 0.181

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

<!-- b003338 | furniture | pages [15] -->
m

<!-- b003339 | furniture | pages [15] -->
m

<!-- b003340 | furniture | pages [15] -->
m

<!-- b003341 | furniture | pages [15] -->
m

<!-- b003342 | furniture | pages [15] -->
m

<!-- b003343 | furniture | pages [15] -->
m

<!-- b003344 | furniture | pages [15] -->
m

<!-- b003345 | furniture | pages [15] -->
m

<!-- b003346 | furniture | pages [15] -->
m

<!-- b003347 | furniture | pages [15] -->
m

<!-- b003348 | furniture | pages [15] -->
m

<!-- b003349 | furniture | pages [15] -->
m

<!-- b003350 | furniture | pages [15] -->
m

<!-- b003351 | furniture | pages [15] -->
m

<!-- b003352 | furniture | pages [15] -->
m

<!-- b003353 | furniture | pages [15] -->
m

<!-- b003354 | furniture | pages [15] -->
m

<!-- b003355 | furniture | pages [15] -->
m

<!-- b003356 | furniture | pages [15] -->
m

<!-- b003357 | furniture | pages [15] -->
m

<!-- b003358 | furniture | pages [15] -->
m

<!-- b003359 | furniture | pages [15] -->
m

<!-- b003360 | furniture | pages [15] -->
m

<!-- b003361 | furniture | pages [15] -->
m

<!-- b003362 | furniture | pages [15] -->
m

<!-- b003363 | furniture | pages [15] -->
m

<!-- b003364 | furniture | pages [15] -->
m

<!-- b003365 | furniture | pages [15] -->
m

<!-- b003366 | furniture | pages [15] -->
m

<!-- b003367 | furniture | pages [15] -->
m

<!-- b003368 | furniture | pages [15] -->
m

<!-- b003369 | furniture | pages [15] -->
m

<!-- b003370 | furniture | pages [15] -->
m

<!-- b003371 | furniture | pages [15] -->
m

<!-- b003372 | furniture | pages [15] -->
m

<!-- b003373 | furniture | pages [15] -->
m

<!-- b003374 | furniture | pages [15] -->
m

<!-- b003375 | furniture | pages [15] -->
m

<!-- b003376 | furniture | pages [15] -->
m

<!-- b003377 | furniture | pages [15] -->
m

<!-- b003378 | furniture | pages [15] -->
m

<!-- b003379 | furniture | pages [15] -->
m

<!-- b003380 | furniture | pages [15] -->
m

<!-- b003381 | furniture | pages [15] -->
m

<!-- b003382 | furniture | pages [15] -->
m

<!-- b003383 | furniture | pages [15] -->
m

<!-- b003384 | furniture | pages [15] -->
m

<!-- b003385 | furniture | pages [15] -->
m

<!-- b003386 | furniture | pages [15] -->
m

<!-- b003387 | furniture | pages [15] -->
m

<!-- b003388 | furniture | pages [15] -->
m

<!-- b003389 | furniture | pages [15] -->
m

<!-- b003390 | furniture | pages [15] -->
m

<!-- b003391 | furniture | pages [15] -->
m

<!-- b003392 | furniture | pages [15] -->
m

<!-- b003393 | furniture | pages [15] -->
m

<!-- b003394 | furniture | pages [15] -->
m

<!-- b003395 | furniture | pages [15] -->
m

<!-- b003396 | furniture | pages [15] -->
m

<!-- b003397 | furniture | pages [15] -->
m

<!-- b003398 | furniture | pages [15] -->
m

<!-- b003399 | furniture | pages [15] -->
m

<!-- b003400 | furniture | pages [15] -->
m

<!-- b003401 | furniture | pages [15] -->
m

<!-- b003402 | furniture | pages [15] -->
m

<!-- b003403 | furniture | pages [15] -->
m

<!-- b003404 | furniture | pages [15] -->
m

<!-- b003405 | furniture | pages [15] -->
m

<!-- b003406 | furniture | pages [15] -->
m

<!-- b003407 | furniture | pages [15] -->
m

<!-- b003408 | furniture | pages [15] -->
m

<!-- b003409 | furniture | pages [15] -->
m

<!-- b003410 | furniture | pages [15] -->
m

<!-- b003411 | furniture | pages [15] -->
m

<!-- b003412 | furniture | pages [15] -->
m

<!-- b003413 | furniture | pages [15] -->
m

<!-- b003414 | furniture | pages [15] -->
m

<!-- b003415 | furniture | pages [15] -->
m

<!-- b003416 | furniture | pages [15] -->
m

<!-- b003417 | furniture | pages [15] -->
m

<!-- b003418 | furniture | pages [15] -->
m

<!-- b003419 | furniture | pages [15] -->
m

<!-- b003420 | furniture | pages [15] -->
m

<!-- b003421 | furniture | pages [15] -->
m

<!-- b003422 | furniture | pages [15] -->
m

<!-- b003423 | furniture | pages [15] -->
m

<!-- b003424 | furniture | pages [15] -->
m

<!-- b003425 | furniture | pages [15] -->
m

<!-- b003426 | furniture | pages [15] -->
m

<!-- b003427 | furniture | pages [15] -->
m

<!-- b003428 | furniture | pages [15] -->
m

<!-- b003429 | furniture | pages [15] -->
m

<!-- b003430 | furniture | pages [15] -->
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

<!-- b003741 | furniture | pages [16] -->
Team # 2504448

<!-- b003742 | furniture | pages [16] -->
Page 16 of 25

<!-- b003743 | prose | pages [16] -->
by the fifth year. This indicates that government interventions and policies effectively mitigate environmental impacts while promoting sustainability. Resident satisfaction also exhibits a positive trend, improving from 0.882 in the first year to 0.917 by the fifth year. The results suggest that targeted policies, including cultural investments and controlled taxation, successfully balance economic, environmental, and social priorities. Overall, our model results demonstrate the importance of adaptive policies and balanced revenue al- location in achieving sustainable tourism in Juneau.

<!-- b003744 | prose | pages [16] -->
3.5.7 Plan for Government Expenditures

<!-- b003745 | prose | pages [16] -->
The additional revenue generated from tourism, primarily through taxation, should be strategically allocated across various components to support sustainable tourism manage- ment in Juneau. We assume that the expenditures are divided into four main categories: environmental protection and recovery, infrastructure development, subsidies to reduce financial burdens, and advertising to promote tourism. The distribution of these expendi- tures is given by our model’s predictions, taking into account the priorities and challenges faced in each year.

<!-- b003746 | prose | pages [16] -->
Investment in environmental protection increases significantly over the years, reflect- ing the importance of reducing the ecological impacts of tourism. These funds are directed toward projects such as preserving the Mendenhall Glacier, restoring biodiversity, and ad- dressing pollution caused by tourist activities. Spending on infrastructure development grows in a steady rate, in order to improve accessibility, public transportation, and util- ities to better accommodate the tourist population. Subsidies play an important role in reducing financial burdens on residents and motivating sustainable practices. Subsidies might include support for local businesses, discounted public transportation, or financial incentives for environment-friendly practices. Expenditure on advertisement and promo- tion starts at 17% in Year 1, focusing on attracting tourists to under-visited locations and highlighting off-peak seasons. As tourism stabilizes, the need for advertisement dimin- ishes.

<!-- b003747 | caption | pages [16] -->
Figure 11: Composition of government expenditures

<!-- b003748 | prose | pages [16] -->
关注数学模型

<!-- b003749 | furniture | pages [16] -->
2

<!-- b003750 | furniture | pages [16] -->
MATHmodels

<!-- b003751 | furniture | pages [16] -->
获取更多资讯

<!-- b003752 | furniture | pages [17] -->
Team # 2504448

<!-- b003753 | prose | pages [17] -->
4

<!-- b003754 | heading | pages [17] -->
Sensitivity Analysis

<!-- b003755 | furniture | pages [17] -->
Page 17 of 25

<!-- b003756 | prose | pages [17] -->
微信公众号：数学模型

<!-- b003757 | prose | pages [17] -->
Average Input of Environmental Index 4.1

<!-- b003758 | prose | pages [17] -->
Output Components vs. Average Input Environmental Index

<!-- b003759 | prose | pages [17] -->
0.8

<!-- b003760 | prose | pages [17] -->
0.6

<!-- b003761 | prose | pages [17] -->
Output Components

<!-- b003762 | prose | pages [17] -->
0.4

<!-- b003763 | prose | pages [17] -->
Output Components

<!-- b003764 | prose | pages [17] -->
Tax rate Infrastructure Subsidy Advertisement Environmental protection

<!-- b003765 | prose | pages [17] -->
微信号：MATHmodels

<!-- b003766 | prose | pages [17] -->
0.2

<!-- b003767 | prose | pages [17] -->
0.0

<!-- b003768 | prose | pages [17] -->
0.0 0.2 0.4 0.6 0.8 1.0 Average Input Environmental Index

<!-- b003769 | caption | pages [17] -->
Figure 12: Output policy components vs. different average of input environmental index

<!-- b003770 | prose | pages [17] -->
The sensitivity analysis shows that the environmental index has the greatest impact on environmental protection investment. When the index is low, governments allocate more resources to restoration, while improvements reduce the need for such spending. This aligns with the ecosystem’s condition directly influencing preservation efforts.

<!-- b003771 | prose | pages [17] -->
Additionally, a lower environmental index leads to higher tax rates and reduced sub- sidies to discourage tourism and generate revenue for environmental restoration. These findings highlight the environmental index as a key factor driving investment decisions, emphasizing the need to balance sustainability with economic priorities.

<!-- b003772 | prose | pages [17] -->
Average Input of Resident Satisfaction 4.2

<!-- b003773 | prose | pages [17] -->
Output Components vs. Average Input Resident Satisfaction

<!-- b003774 | prose | pages [17] -->
0.5

<!-- b003775 | prose | pages [17] -->
0.4

<!-- b003776 | prose | pages [17] -->
Output Components

<!-- b003777 | prose | pages [17] -->
0.3

<!-- b003778 | prose | pages [17] -->
0.2

<!-- b003779 | prose | pages [17] -->
0.1

<!-- b003780 | prose | pages [17] -->
0.0

<!-- b003781 | prose | pages [17] -->
0.0 0.2 0.4

<!-- b003782 | prose | pages [17] -->
Output Components

<!-- b003783 | prose | pages [17] -->
Tax rate Infrastructure Subsidy Advertisement Environmental protection

<!-- b003784 | prose | pages [17] -->
0.6 0.8 1.0 Average Resident Satisfaction

<!-- b003785 | caption | pages [17] -->
Figure 13: Output policy components vs. different average input of resident satisfaction

<!-- b003786 | prose | pages [17] -->
The sensitivity analysis shows that average resident satisfaction strongly influences

<!-- b003787 | prose | pages [17] -->
m

<!-- b003788 | prose | pages [17] -->
m

<!-- b003789 | prose | pages [17] -->
m

<!-- b003790 | prose | pages [17] -->
m

<!-- b003791 | prose | pages [17] -->
m

<!-- b003792 | prose | pages [17] -->
m

<!-- b003793 | prose | pages [17] -->
m

<!-- b003794 | prose | pages [17] -->
m

<!-- b003795 | prose | pages [17] -->
m

<!-- b003796 | prose | pages [17] -->
m

<!-- b003797 | prose | pages [17] -->
m

<!-- b003798 | prose | pages [17] -->
m

<!-- b003799 | prose | pages [17] -->
m

<!-- b003800 | prose | pages [17] -->
m

<!-- b003801 | prose | pages [17] -->
m

<!-- b003802 | prose | pages [17] -->
m

<!-- b003803 | prose | pages [17] -->
m

<!-- b003804 | prose | pages [17] -->
m

<!-- b003805 | prose | pages [17] -->
m

<!-- b003806 | prose | pages [17] -->
m

<!-- b003807 | prose | pages [17] -->
m

<!-- b003808 | prose | pages [17] -->
m

<!-- b003809 | prose | pages [17] -->
m

<!-- b003810 | prose | pages [17] -->
m

<!-- b003811 | prose | pages [17] -->
m

<!-- b003812 | prose | pages [17] -->
m

<!-- b003813 | prose | pages [17] -->
m

<!-- b003814 | prose | pages [17] -->
m

<!-- b003815 | prose | pages [17] -->
m

<!-- b003816 | prose | pages [17] -->
m

<!-- b003817 | prose | pages [17] -->
m

<!-- b003818 | prose | pages [17] -->
m

<!-- b003819 | prose | pages [17] -->
m

<!-- b003820 | prose | pages [17] -->
m

<!-- b003821 | prose | pages [17] -->
m

<!-- b003822 | prose | pages [17] -->
m

<!-- b003823 | prose | pages [17] -->
m

<!-- b003824 | prose | pages [17] -->
m

<!-- b003825 | prose | pages [17] -->
m

<!-- b003826 | prose | pages [17] -->
m

<!-- b003827 | prose | pages [17] -->
m

<!-- b003828 | prose | pages [17] -->
m

<!-- b003829 | prose | pages [17] -->
m

<!-- b003830 | prose | pages [17] -->
m

<!-- b003831 | prose | pages [17] -->
m

<!-- b003832 | prose | pages [17] -->
m

<!-- b003833 | prose | pages [17] -->
m

<!-- b003834 | prose | pages [17] -->
m

<!-- b003835 | prose | pages [17] -->
m

<!-- b003836 | prose | pages [17] -->
m

<!-- b003837 | prose | pages [17] -->
m

<!-- b003838 | prose | pages [17] -->
m

<!-- b003839 | prose | pages [17] -->
m

<!-- b003840 | prose | pages [17] -->
m

<!-- b003841 | prose | pages [17] -->
m

<!-- b003842 | prose | pages [17] -->
m

<!-- b003843 | prose | pages [17] -->
m

<!-- b003844 | prose | pages [17] -->
m

<!-- b003845 | prose | pages [17] -->
m

<!-- b003846 | prose | pages [17] -->
m

<!-- b003847 | prose | pages [17] -->
m

<!-- b003848 | prose | pages [17] -->
m

<!-- b003849 | prose | pages [17] -->
m

<!-- b003850 | prose | pages [17] -->
m

<!-- b003851 | prose | pages [17] -->
m

<!-- b003852 | prose | pages [17] -->
m

<!-- b003853 | prose | pages [17] -->
m

<!-- b003854 | prose | pages [17] -->
m

<!-- b003855 | prose | pages [17] -->
m

<!-- b003856 | prose | pages [17] -->
m

<!-- b003857 | prose | pages [17] -->
m

<!-- b003858 | prose | pages [17] -->
m

<!-- b003859 | prose | pages [17] -->
m

<!-- b003860 | prose | pages [17] -->
m

<!-- b003861 | prose | pages [17] -->
m

<!-- b003862 | prose | pages [17] -->
m

<!-- b003863 | prose | pages [17] -->
m

<!-- b003864 | prose | pages [17] -->
m

<!-- b003865 | prose | pages [17] -->
m

<!-- b003866 | prose | pages [17] -->
m

<!-- b003867 | prose | pages [17] -->
m

<!-- b003868 | prose | pages [17] -->
m

<!-- b003869 | prose | pages [17] -->
m

<!-- b003870 | prose | pages [17] -->
m

<!-- b003871 | prose | pages [17] -->
m

<!-- b003872 | prose | pages [17] -->
m

<!-- b003873 | prose | pages [17] -->
m

<!-- b003874 | prose | pages [17] -->
m

<!-- b003875 | prose | pages [17] -->
m

<!-- b003876 | prose | pages [17] -->
m

<!-- b003877 | prose | pages [17] -->
m

<!-- b003878 | prose | pages [17] -->
m

<!-- b003879 | prose | pages [17] -->
m

<!-- b003880 | prose | pages [17] -->
m

<!-- b003881 | prose | pages [17] -->
m

<!-- b003882 | prose | pages [17] -->
m

<!-- b003883 | prose | pages [17] -->
m

<!-- b003884 | prose | pages [17] -->
m

<!-- b003885 | prose | pages [17] -->
m

<!-- b003886 | prose | pages [17] -->
m

<!-- b003887 | prose | pages [17] -->
m

<!-- b003888 | prose | pages [17] -->
m

<!-- b003889 | prose | pages [17] -->
m

<!-- b003890 | prose | pages [17] -->
m

<!-- b003891 | prose | pages [17] -->
m

<!-- b003892 | prose | pages [17] -->
m

<!-- b003893 | prose | pages [17] -->
m

<!-- b003894 | prose | pages [17] -->
m

<!-- b003895 | prose | pages [17] -->
m

<!-- b003896 | prose | pages [17] -->
m

<!-- b003897 | prose | pages [17] -->
m

<!-- b003898 | prose | pages [17] -->
m

<!-- b003899 | prose | pages [17] -->
m

<!-- b003900 | prose | pages [17] -->
m

<!-- b003901 | prose | pages [17] -->
m

<!-- b003902 | prose | pages [17] -->
m

<!-- b003903 | prose | pages [17] -->
m

<!-- b003904 | prose | pages [17] -->
m

<!-- b003905 | prose | pages [17] -->
m

<!-- b003906 | prose | pages [17] -->
m

<!-- b003907 | prose | pages [17] -->
m

<!-- b003908 | prose | pages [17] -->
m

<!-- b003909 | prose | pages [17] -->
m

<!-- b003910 | prose | pages [17] -->
m

<!-- b003911 | prose | pages [17] -->
m

<!-- b003912 | prose | pages [17] -->
m

<!-- b003913 | prose | pages [17] -->
m

<!-- b003914 | prose | pages [17] -->
m

<!-- b003915 | prose | pages [17] -->
m

<!-- b003916 | prose | pages [17] -->
m

<!-- b003917 | prose | pages [17] -->
government policies, with subsidies being the most affected component. When resident

<!-- b003918 | prose | pages [17] -->
m

<!-- b003919 | prose | pages [17] -->
m

<!-- b003920 | prose | pages [17] -->
m

<!-- b003921 | prose | pages [17] -->
m

<!-- b003922 | prose | pages [17] -->
m

<!-- b003923 | prose | pages [17] -->
m

<!-- b003924 | prose | pages [17] -->
m

<!-- b003925 | prose | pages [17] -->
m

<!-- b003926 | prose | pages [17] -->
m

<!-- b003927 | prose | pages [17] -->
m

<!-- b003928 | prose | pages [17] -->
m

<!-- b003929 | prose | pages [17] -->
m

<!-- b003930 | prose | pages [17] -->
m

<!-- b003931 | prose | pages [17] -->
m

<!-- b003932 | prose | pages [17] -->
m

<!-- b003933 | prose | pages [17] -->
m

<!-- b003934 | prose | pages [17] -->
m

<!-- b003935 | prose | pages [17] -->
m

<!-- b003936 | prose | pages [17] -->
m

<!-- b003937 | prose | pages [17] -->
m

<!-- b003938 | prose | pages [17] -->
m

<!-- b003939 | prose | pages [17] -->
m

<!-- b003940 | prose | pages [17] -->
m

<!-- b003941 | prose | pages [17] -->
m

<!-- b003942 | prose | pages [17] -->
m

<!-- b003943 | prose | pages [17] -->
m

<!-- b003944 | prose | pages [17] -->
m

<!-- b003945 | prose | pages [17] -->
m

<!-- b003946 | prose | pages [17] -->
m

<!-- b003947 | prose | pages [17] -->
m

<!-- b003948 | prose | pages [17] -->
m

<!-- b003949 | prose | pages [17] -->
m

<!-- b003950 | prose | pages [17] -->
m

<!-- b003951 | prose | pages [17] -->
m

<!-- b003952 | prose | pages [17] -->
m

<!-- b003953 | prose | pages [17] -->
m

<!-- b003954 | prose | pages [17] -->
m

<!-- b003955 | prose | pages [17] -->
m

<!-- b003956 | prose | pages [17] -->
m

<!-- b003957 | prose | pages [17] -->
m

<!-- b003958 | prose | pages [17] -->
m

<!-- b003959 | prose | pages [17] -->
m

<!-- b003960 | prose | pages [17] -->
m

<!-- b003961 | prose | pages [17] -->
m

<!-- b003962 | prose | pages [17] -->
m

<!-- b003963 | prose | pages [17] -->
m

<!-- b003964 | prose | pages [17] -->
m

<!-- b003965 | prose | pages [17] -->
m

<!-- b003966 | prose | pages [17] -->
m

<!-- b003967 | prose | pages [17] -->
m

<!-- b003968 | prose | pages [17] -->
m

<!-- b003969 | prose | pages [17] -->
m

<!-- b003970 | prose | pages [17] -->
m

<!-- b003971 | prose | pages [17] -->
m

<!-- b003972 | prose | pages [17] -->
m

<!-- b003973 | prose | pages [17] -->
m

<!-- b003974 | prose | pages [17] -->
m

<!-- b003975 | prose | pages [17] -->
m

<!-- b003976 | prose | pages [17] -->
m

<!-- b003977 | prose | pages [17] -->
m

<!-- b003978 | prose | pages [17] -->
m

<!-- b003979 | prose | pages [17] -->
m

<!-- b003980 | prose | pages [17] -->
m

<!-- b003981 | prose | pages [17] -->
m

<!-- b003982 | prose | pages [17] -->
m

<!-- b003983 | prose | pages [17] -->
m

<!-- b003984 | prose | pages [17] -->
m

<!-- b003985 | prose | pages [17] -->
m

<!-- b003986 | prose | pages [17] -->
m

<!-- b003987 | prose | pages [17] -->
m

<!-- b003988 | prose | pages [17] -->
m

<!-- b003989 | prose | pages [17] -->
m

<!-- b003990 | prose | pages [17] -->
m

<!-- b003991 | prose | pages [17] -->
m

<!-- b003992 | prose | pages [17] -->
m

<!-- b003993 | prose | pages [17] -->
m

<!-- b003994 | prose | pages [17] -->
m

<!-- b003995 | prose | pages [17] -->
m

<!-- b003996 | prose | pages [17] -->
m

<!-- b003997 | prose | pages [17] -->
m

<!-- b003998 | prose | pages [17] -->
m

<!-- b003999 | prose | pages [17] -->
m

<!-- b004000 | prose | pages [17] -->
m

<!-- b004001 | prose | pages [17] -->
m

<!-- b004002 | prose | pages [17] -->
m

<!-- b004003 | prose | pages [17] -->
m

<!-- b004004 | prose | pages [17] -->
m

<!-- b004005 | prose | pages [17] -->
m

<!-- b004006 | prose | pages [17] -->
m

<!-- b004007 | prose | pages [17] -->
m

<!-- b004008 | prose | pages [17] -->
m

<!-- b004009 | prose | pages [17] -->
m

<!-- b004010 | prose | pages [17] -->
m

<!-- b004011 | prose | pages [17] -->
m

<!-- b004012 | prose | pages [17] -->
m

<!-- b004013 | prose | pages [17] -->
m

<!-- b004014 | prose | pages [17] -->
m

<!-- b004015 | prose | pages [17] -->
m

<!-- b004016 | prose | pages [17] -->
m

<!-- b004017 | prose | pages [17] -->
m

<!-- b004018 | prose | pages [17] -->
m

<!-- b004019 | prose | pages [17] -->
m

<!-- b004020 | prose | pages [17] -->
m

<!-- b004021 | prose | pages [17] -->
m

<!-- b004022 | prose | pages [17] -->
m

<!-- b004023 | prose | pages [17] -->
m

<!-- b004024 | prose | pages [17] -->
m

<!-- b004025 | prose | pages [17] -->
m

<!-- b004026 | prose | pages [17] -->
m

<!-- b004027 | prose | pages [17] -->
m

<!-- b004028 | prose | pages [17] -->
m

<!-- b004029 | prose | pages [17] -->
m

<!-- b004030 | prose | pages [17] -->
m

<!-- b004031 | prose | pages [17] -->
m

<!-- b004032 | prose | pages [17] -->
m

<!-- b004033 | prose | pages [17] -->
m

<!-- b004034 | prose | pages [17] -->
m

<!-- b004035 | prose | pages [17] -->
m

<!-- b004036 | prose | pages [17] -->
m

<!-- b004037 | prose | pages [17] -->
m

<!-- b004038 | prose | pages [17] -->
m

<!-- b004039 | prose | pages [17] -->
m

<!-- b004040 | prose | pages [17] -->
m

<!-- b004041 | prose | pages [17] -->
m

<!-- b004042 | prose | pages [17] -->
m

<!-- b004043 | prose | pages [17] -->
m

<!-- b004044 | prose | pages [17] -->
m

<!-- b004045 | prose | pages [17] -->
m

<!-- b004046 | prose | pages [17] -->
m

<!-- b004047 | prose | pages [17] -->
m

<!-- b004048 | prose | pages [17] -->
m

<!-- b004049 | prose | pages [17] -->
m

<!-- b004050 | prose | pages [17] -->
m

<!-- b004051 | prose | pages [17] -->
m

<!-- b004052 | prose | pages [17] -->
m

<!-- b004053 | prose | pages [17] -->
m

<!-- b004054 | prose | pages [17] -->
m

<!-- b004055 | prose | pages [17] -->
m

<!-- b004056 | prose | pages [17] -->
m

<!-- b004057 | prose | pages [17] -->
m

<!-- b004058 | prose | pages [17] -->
m

<!-- b004059 | prose | pages [17] -->
m

<!-- b004060 | prose | pages [17] -->
m

<!-- b004061 | prose | pages [17] -->
m

<!-- b004062 | prose | pages [17] -->
m

<!-- b004063 | prose | pages [17] -->
m

<!-- b004064 | prose | pages [17] -->
m

<!-- b004065 | prose | pages [17] -->
m

<!-- b004066 | prose | pages [17] -->
m

<!-- b004067 | prose | pages [17] -->
m

<!-- b004068 | prose | pages [17] -->
m

<!-- b004069 | prose | pages [17] -->
m

<!-- b004070 | prose | pages [17] -->
m

<!-- b004071 | prose | pages [17] -->
m

<!-- b004072 | prose | pages [17] -->
satisfaction decreases, subsidies are significantly increased as governments aim to address

<!-- b004073 | furniture | pages [17] -->
m

<!-- b004074 | furniture | pages [17] -->
m

<!-- b004075 | furniture | pages [17] -->
m

<!-- b004076 | furniture | pages [17] -->
m

<!-- b004077 | furniture | pages [17] -->
m

<!-- b004078 | furniture | pages [17] -->
m

<!-- b004079 | furniture | pages [17] -->
m

<!-- b004080 | furniture | pages [17] -->
m

<!-- b004081 | furniture | pages [17] -->
m

<!-- b004082 | furniture | pages [17] -->
m

<!-- b004083 | furniture | pages [17] -->
m

<!-- b004084 | furniture | pages [17] -->
m

<!-- b004085 | furniture | pages [17] -->
m

<!-- b004086 | furniture | pages [17] -->
m

<!-- b004087 | furniture | pages [17] -->
m

<!-- b004088 | furniture | pages [17] -->
m

<!-- b004089 | furniture | pages [17] -->
m

<!-- b004090 | furniture | pages [17] -->
m

<!-- b004091 | furniture | pages [17] -->
m

<!-- b004092 | furniture | pages [17] -->
m

<!-- b004093 | furniture | pages [17] -->
m

<!-- b004094 | furniture | pages [17] -->
m

<!-- b004095 | furniture | pages [17] -->
m

<!-- b004096 | furniture | pages [17] -->
m

<!-- b004097 | furniture | pages [17] -->
m

<!-- b004098 | furniture | pages [17] -->
m

<!-- b004099 | furniture | pages [17] -->
m

<!-- b004100 | furniture | pages [17] -->
m

<!-- b004101 | furniture | pages [17] -->
m

<!-- b004102 | furniture | pages [17] -->
m

<!-- b004103 | furniture | pages [17] -->
m

<!-- b004104 | furniture | pages [17] -->
m

<!-- b004105 | furniture | pages [17] -->
m

<!-- b004106 | furniture | pages [17] -->
m

<!-- b004107 | furniture | pages [17] -->
m

<!-- b004108 | furniture | pages [17] -->
m

<!-- b004109 | furniture | pages [17] -->
m

<!-- b004110 | furniture | pages [17] -->
m

<!-- b004111 | furniture | pages [17] -->
m

<!-- b004112 | furniture | pages [17] -->
m

<!-- b004113 | furniture | pages [17] -->
m

<!-- b004114 | furniture | pages [17] -->
m

<!-- b004115 | furniture | pages [17] -->
m

<!-- b004116 | furniture | pages [17] -->
m

<!-- b004117 | furniture | pages [17] -->
m

<!-- b004118 | furniture | pages [17] -->
m

<!-- b004119 | furniture | pages [17] -->
m

<!-- b004120 | furniture | pages [17] -->
m

<!-- b004121 | furniture | pages [17] -->
m

<!-- b004122 | furniture | pages [17] -->
m

<!-- b004123 | furniture | pages [17] -->
m

<!-- b004124 | furniture | pages [17] -->
m

<!-- b004125 | furniture | pages [17] -->
m

<!-- b004126 | furniture | pages [17] -->
m

<!-- b004127 | furniture | pages [17] -->
m

<!-- b004128 | furniture | pages [17] -->
m

<!-- b004129 | furniture | pages [17] -->
m

<!-- b004130 | furniture | pages [17] -->
m

<!-- b004131 | furniture | pages [17] -->
m

<!-- b004132 | furniture | pages [17] -->
m

<!-- b004133 | furniture | pages [17] -->
m

<!-- b004134 | furniture | pages [17] -->
m

<!-- b004135 | furniture | pages [17] -->
m

<!-- b004136 | furniture | pages [17] -->
m

<!-- b004137 | furniture | pages [17] -->
m

<!-- b004138 | furniture | pages [17] -->
m

<!-- b004139 | furniture | pages [17] -->
m

<!-- b004140 | furniture | pages [17] -->
m

<!-- b004141 | furniture | pages [17] -->
m

<!-- b004142 | furniture | pages [17] -->
m

<!-- b004143 | furniture | pages [17] -->
m

<!-- b004144 | furniture | pages [17] -->
m

<!-- b004145 | furniture | pages [17] -->
m

<!-- b004146 | furniture | pages [17] -->
m

<!-- b004147 | furniture | pages [17] -->
m

<!-- b004148 | furniture | pages [17] -->
m

<!-- b004149 | furniture | pages [17] -->
m

<!-- b004150 | furniture | pages [17] -->
m

<!-- b004151 | furniture | pages [17] -->
m

<!-- b004152 | furniture | pages [17] -->
m

<!-- b004153 | furniture | pages [17] -->
m

<!-- b004154 | furniture | pages [17] -->
m

<!-- b004155 | furniture | pages [17] -->
m

<!-- b004156 | furniture | pages [17] -->
m

<!-- b004157 | furniture | pages [17] -->
m

<!-- b004158 | furniture | pages [17] -->
m

<!-- b004159 | furniture | pages [17] -->
m

<!-- b004160 | furniture | pages [17] -->
m

<!-- b004161 | furniture | pages [17] -->
m

<!-- b004162 | furniture | pages [17] -->
m

<!-- b004163 | furniture | pages [17] -->
m

<!-- b004164 | furniture | pages [17] -->
m

<!-- b004165 | furniture | pages [17] -->
m

<!-- b004166 | furniture | pages [17] -->
m

<!-- b004167 | furniture | pages [17] -->
m

<!-- b004168 | furniture | pages [17] -->
m

<!-- b004169 | furniture | pages [17] -->
m

<!-- b004170 | furniture | pages [17] -->
m

<!-- b004171 | furniture | pages [17] -->
m

<!-- b004172 | furniture | pages [17] -->
m

<!-- b004173 | furniture | pages [17] -->
m

<!-- b004174 | furniture | pages [17] -->
m

<!-- b004175 | furniture | pages [17] -->
m

<!-- b004176 | furniture | pages [17] -->
m

<!-- b004177 | furniture | pages [17] -->
m

<!-- b004178 | furniture | pages [17] -->
m

<!-- b004179 | furniture | pages [17] -->
m

<!-- b004180 | furniture | pages [17] -->
m

<!-- b004181 | furniture | pages [17] -->
m

<!-- b004182 | furniture | pages [17] -->
m

<!-- b004183 | furniture | pages [17] -->
m

<!-- b004184 | furniture | pages [17] -->
m

<!-- b004185 | furniture | pages [17] -->
m

<!-- b004186 | furniture | pages [17] -->
m

<!-- b004187 | furniture | pages [17] -->
m

<!-- b004188 | furniture | pages [17] -->
m

<!-- b004189 | furniture | pages [17] -->
m

<!-- b004190 | furniture | pages [17] -->
m

<!-- b004191 | furniture | pages [17] -->
m

<!-- b004192 | furniture | pages [17] -->
m

<!-- b004193 | furniture | pages [17] -->
m

<!-- b004194 | furniture | pages [17] -->
m

<!-- b004195 | furniture | pages [17] -->
m

<!-- b004196 | furniture | pages [17] -->
m

<!-- b004197 | furniture | pages [17] -->
m

<!-- b004198 | furniture | pages [17] -->
m

<!-- b004199 | furniture | pages [17] -->
m

<!-- b004200 | furniture | pages [17] -->
m

<!-- b004201 | furniture | pages [17] -->
m

<!-- b004202 | furniture | pages [17] -->
m

<!-- b004203 | furniture | pages [17] -->
m

<!-- b004204 | furniture | pages [17] -->
m

<!-- b004205 | furniture | pages [17] -->
m

<!-- b004206 | furniture | pages [17] -->
m

<!-- b004207 | furniture | pages [17] -->
m

<!-- b004208 | furniture | pages [17] -->
m

<!-- b004209 | furniture | pages [17] -->
m

<!-- b004210 | furniture | pages [17] -->
m

<!-- b004211 | furniture | pages [17] -->
m

<!-- b004212 | furniture | pages [17] -->
m

<!-- b004213 | furniture | pages [17] -->
m

<!-- b004214 | furniture | pages [17] -->
m

<!-- b004215 | furniture | pages [17] -->
m

<!-- b004216 | furniture | pages [17] -->
m

<!-- b004217 | furniture | pages [17] -->
m

<!-- b004218 | furniture | pages [17] -->
m

<!-- b004219 | furniture | pages [17] -->
m

<!-- b004220 | furniture | pages [17] -->
m

<!-- b004221 | furniture | pages [17] -->
m

<!-- b004222 | furniture | pages [17] -->
m

<!-- b004223 | furniture | pages [17] -->
m

<!-- b004224 | furniture | pages [17] -->
m

<!-- b004225 | furniture | pages [17] -->
m

<!-- b004226 | furniture | pages [17] -->
m

<!-- b004227 | furniture | pages [17] -->
m

<!-- b004228 | furniture | pages [17] -->
m

<!-- b004229 | furniture | pages [17] -->
m

<!-- b004230 | furniture | pages [17] -->
m

<!-- b004231 | furniture | pages [17] -->
m

<!-- b004232 | furniture | pages [17] -->
m

<!-- b004233 | furniture | pages [17] -->
m

<!-- b004234 | furniture | pages [17] -->
m

<!-- b004235 | furniture | pages [17] -->
m

<!-- b004236 | furniture | pages [17] -->
m

<!-- b004237 | furniture | pages [17] -->
m

<!-- b004238 | furniture | pages [17] -->
m

<!-- b004239 | furniture | pages [17] -->
m

<!-- b004240 | furniture | pages [17] -->
m

<!-- b004241 | furniture | pages [17] -->
m

<!-- b004242 | furniture | pages [17] -->
m

<!-- b004243 | furniture | pages [17] -->
m

<!-- b004244 | furniture | pages [17] -->
m

<!-- b004245 | furniture | pages [17] -->
m

<!-- b004246 | furniture | pages [17] -->
m

<!-- b004247 | furniture | pages [17] -->
m

<!-- b004248 | furniture | pages [17] -->
m

<!-- b004249 | furniture | pages [17] -->
m

<!-- b004250 | furniture | pages [17] -->
m

<!-- b004251 | furniture | pages [17] -->
m

<!-- b004252 | furniture | pages [17] -->
m

<!-- b004253 | furniture | pages [17] -->
m

<!-- b004254 | furniture | pages [17] -->
m

<!-- b004255 | furniture | pages [17] -->
m

<!-- b004256 | furniture | pages [17] -->
m

<!-- b004257 | furniture | pages [17] -->
m

<!-- b004258 | furniture | pages [17] -->
m

<!-- b004259 | furniture | pages [17] -->
m

<!-- b004260 | furniture | pages [17] -->
m

<!-- b004261 | furniture | pages [17] -->
m

<!-- b004262 | furniture | pages [17] -->
m

<!-- b004263 | furniture | pages [17] -->
m

<!-- b004264 | furniture | pages [17] -->
m

<!-- b004265 | furniture | pages [17] -->
m

<!-- b004266 | furniture | pages [17] -->
m

<!-- b004267 | furniture | pages [17] -->
m

<!-- b004268 | furniture | pages [17] -->
m

<!-- b004269 | furniture | pages [17] -->
m

<!-- b004270 | furniture | pages [17] -->
m

<!-- b004271 | furniture | pages [17] -->
m

<!-- b004272 | furniture | pages [17] -->
m

<!-- b004273 | furniture | pages [17] -->
m

<!-- b004274 | furniture | pages [17] -->
m

<!-- b004275 | furniture | pages [17] -->
m

<!-- b004276 | furniture | pages [17] -->
m

<!-- b004277 | furniture | pages [17] -->
m

<!-- b004278 | furniture | pages [17] -->
m

<!-- b004279 | furniture | pages [17] -->
m

<!-- b004280 | furniture | pages [17] -->
m

<!-- b004281 | furniture | pages [17] -->
m

<!-- b004282 | furniture | pages [17] -->
m

<!-- b004283 | furniture | pages [17] -->
m

<!-- b004284 | furniture | pages [17] -->
m

<!-- b004285 | furniture | pages [17] -->
m

<!-- b004286 | furniture | pages [17] -->
m

<!-- b004287 | furniture | pages [17] -->
m

<!-- b004288 | furniture | pages [17] -->
m

<!-- b004289 | furniture | pages [17] -->
m

<!-- b004290 | furniture | pages [17] -->
m

<!-- b004291 | furniture | pages [17] -->
m

<!-- b004292 | furniture | pages [17] -->
m

<!-- b004293 | furniture | pages [17] -->
m

<!-- b004294 | furniture | pages [17] -->
m

<!-- b004295 | furniture | pages [17] -->
m

<!-- b004296 | furniture | pages [17] -->
m

<!-- b004297 | furniture | pages [17] -->
m

<!-- b004298 | furniture | pages [17] -->
m

<!-- b004299 | furniture | pages [17] -->
m

<!-- b004300 | furniture | pages [17] -->
m

<!-- b004301 | furniture | pages [17] -->
m

<!-- b004302 | furniture | pages [17] -->
m

<!-- b004303 | furniture | pages [17] -->
m

<!-- b004304 | furniture | pages [17] -->
m

<!-- b004305 | furniture | pages [17] -->
m

<!-- b004306 | furniture | pages [17] -->
m

<!-- b004307 | furniture | pages [17] -->
m

<!-- b004308 | furniture | pages [17] -->
m

<!-- b004309 | furniture | pages [17] -->
m

<!-- b004310 | furniture | pages [17] -->
m

<!-- b004311 | furniture | pages [17] -->
m

<!-- b004312 | furniture | pages [17] -->
m

<!-- b004313 | furniture | pages [17] -->
m

<!-- b004314 | furniture | pages [17] -->
m

<!-- b004315 | furniture | pages [17] -->
m

<!-- b004316 | furniture | pages [17] -->
m

<!-- b004317 | furniture | pages [17] -->
m

<!-- b004318 | furniture | pages [17] -->
m

<!-- b004319 | furniture | pages [17] -->
m

<!-- b004320 | furniture | pages [17] -->
m

<!-- b004321 | furniture | pages [17] -->
m

<!-- b004322 | furniture | pages [17] -->
m

<!-- b004323 | furniture | pages [17] -->
m

<!-- b004324 | furniture | pages [17] -->
m

<!-- b004325 | furniture | pages [17] -->
m

<!-- b004326 | furniture | pages [17] -->
m

<!-- b004327 | furniture | pages [17] -->
m

<!-- b004328 | furniture | pages [17] -->
m

<!-- b004329 | furniture | pages [17] -->
m

<!-- b004330 | furniture | pages [17] -->
m

<!-- b004331 | furniture | pages [17] -->
m

<!-- b004332 | furniture | pages [17] -->
m

<!-- b004333 | furniture | pages [17] -->
m

<!-- b004334 | furniture | pages [17] -->
m

<!-- b004335 | furniture | pages [17] -->
m

<!-- b004336 | furniture | pages [17] -->
m

<!-- b004337 | furniture | pages [17] -->
m

<!-- b004338 | furniture | pages [17] -->
m

<!-- b004339 | furniture | pages [17] -->
m

<!-- b004340 | furniture | pages [17] -->
m

<!-- b004341 | furniture | pages [17] -->
m

<!-- b004342 | furniture | pages [17] -->
m

<!-- b004343 | furniture | pages [17] -->
m

<!-- b004344 | furniture | pages [17] -->
m

<!-- b004345 | furniture | pages [17] -->
m

<!-- b004346 | furniture | pages [17] -->
m

<!-- b004347 | furniture | pages [17] -->
m

<!-- b004348 | furniture | pages [17] -->
m

<!-- b004349 | furniture | pages [17] -->
m

<!-- b004350 | furniture | pages [17] -->
m

<!-- b004351 | furniture | pages [17] -->
m

<!-- b004352 | furniture | pages [17] -->
m

<!-- b004353 | furniture | pages [17] -->
m

<!-- b004354 | furniture | pages [17] -->
m

<!-- b004355 | furniture | pages [17] -->
m

<!-- b004356 | furniture | pages [17] -->
m

<!-- b004357 | furniture | pages [17] -->
m

<!-- b004358 | furniture | pages [17] -->
m

<!-- b004359 | furniture | pages [17] -->
m

<!-- b004360 | furniture | pages [17] -->
m

<!-- b004361 | furniture | pages [17] -->
m

<!-- b004362 | furniture | pages [17] -->
m

<!-- b004363 | furniture | pages [17] -->
m

<!-- b004364 | furniture | pages [17] -->
m

<!-- b004365 | furniture | pages [17] -->
m

<!-- b004366 | furniture | pages [17] -->
m

<!-- b004367 | furniture | pages [17] -->
m

<!-- b004368 | furniture | pages [17] -->
m

<!-- b004369 | furniture | pages [17] -->
m

<!-- b004370 | furniture | pages [17] -->
m

<!-- b004371 | furniture | pages [17] -->
m

<!-- b004372 | furniture | pages [17] -->
m

<!-- b004373 | furniture | pages [17] -->
m

<!-- b004374 | furniture | pages [17] -->
m

<!-- b004375 | furniture | pages [17] -->
m

<!-- b004376 | furniture | pages [17] -->
m

<!-- b004377 | furniture | pages [17] -->
m

<!-- b004378 | furniture | pages [17] -->
m

<!-- b004379 | furniture | pages [17] -->
m

<!-- b004380 | furniture | pages [17] -->
m

<!-- b004381 | furniture | pages [17] -->
m

<!-- b004382 | furniture | pages [17] -->
m

<!-- b004383 | furniture | pages [17] -->
m

<!-- b004384 | furniture | pages [17] -->
m

<!-- b004385 | furniture | pages [17] -->
m

<!-- b004386 | furniture | pages [17] -->
m

<!-- b004387 | furniture | pages [17] -->
m

<!-- b004388 | furniture | pages [17] -->
m

<!-- b004389 | furniture | pages [17] -->
m

<!-- b004390 | furniture | pages [17] -->
m

<!-- b004391 | furniture | pages [17] -->
m

<!-- b004392 | furniture | pages [17] -->
m

<!-- b004393 | furniture | pages [17] -->
m

<!-- b004394 | furniture | pages [17] -->
m

<!-- b004395 | furniture | pages [17] -->
m

<!-- b004396 | furniture | pages [17] -->
m

<!-- b004397 | furniture | pages [17] -->
m

<!-- b004398 | furniture | pages [17] -->
m

<!-- b004399 | furniture | pages [17] -->
m

<!-- b004400 | furniture | pages [17] -->
m

<!-- b004401 | furniture | pages [17] -->
m

<!-- b004402 | furniture | pages [17] -->
m

<!-- b004403 | furniture | pages [17] -->
m

<!-- b004404 | furniture | pages [17] -->
m

<!-- b004405 | furniture | pages [17] -->
m

<!-- b004406 | furniture | pages [17] -->
m

<!-- b004407 | furniture | pages [17] -->
m

<!-- b004408 | furniture | pages [17] -->
m

<!-- b004409 | furniture | pages [17] -->
m

<!-- b004410 | furniture | pages [17] -->
m

<!-- b004411 | furniture | pages [17] -->
m

<!-- b004412 | furniture | pages [17] -->
m

<!-- b004413 | furniture | pages [17] -->
m

<!-- b004414 | furniture | pages [17] -->
m

<!-- b004415 | furniture | pages [17] -->
m

<!-- b004416 | furniture | pages [17] -->
m

<!-- b004417 | furniture | pages [17] -->
m

<!-- b004418 | furniture | pages [17] -->
m

<!-- b004419 | furniture | pages [17] -->
m

<!-- b004420 | furniture | pages [17] -->
m

<!-- b004421 | furniture | pages [17] -->
m

<!-- b004422 | furniture | pages [17] -->
m

<!-- b004423 | furniture | pages [17] -->
m

<!-- b004424 | furniture | pages [17] -->
m

<!-- b004425 | furniture | pages [17] -->
m

<!-- b004426 | furniture | pages [17] -->
m

<!-- b004427 | furniture | pages [17] -->
m

<!-- b004428 | furniture | pages [17] -->
m

<!-- b004429 | furniture | pages [17] -->
m

<!-- b004430 | furniture | pages [17] -->
m

<!-- b004431 | furniture | pages [17] -->
m

<!-- b004432 | furniture | pages [17] -->
m

<!-- b004433 | furniture | pages [17] -->
m

<!-- b004434 | furniture | pages [17] -->
m

<!-- b004435 | furniture | pages [17] -->
m

<!-- b004436 | furniture | pages [17] -->
m

<!-- b004437 | furniture | pages [17] -->
m

<!-- b004438 | furniture | pages [17] -->
m

<!-- b004439 | furniture | pages [17] -->
m

<!-- b004440 | furniture | pages [17] -->
m

<!-- b004441 | furniture | pages [17] -->
m

<!-- b004442 | furniture | pages [17] -->
m

<!-- b004443 | furniture | pages [17] -->
m

<!-- b004444 | furniture | pages [17] -->
m

<!-- b004445 | furniture | pages [17] -->
m

<!-- b004446 | furniture | pages [17] -->
m

<!-- b004447 | furniture | pages [17] -->
m

<!-- b004448 | furniture | pages [17] -->
m

<!-- b004449 | furniture | pages [17] -->
m

<!-- b004450 | furniture | pages [17] -->
m

<!-- b004451 | furniture | pages [17] -->
m

<!-- b004452 | furniture | pages [17] -->
m

<!-- b004453 | furniture | pages [17] -->
m

<!-- b004454 | furniture | pages [17] -->
m

<!-- b004455 | furniture | pages [17] -->
m

<!-- b004456 | furniture | pages [17] -->
m

<!-- b004457 | furniture | pages [17] -->
m

<!-- b004458 | furniture | pages [17] -->
m

<!-- b004459 | furniture | pages [17] -->
m

<!-- b004460 | furniture | pages [17] -->
m

<!-- b004461 | furniture | pages [17] -->
m

<!-- b004462 | furniture | pages [17] -->
m

<!-- b004463 | furniture | pages [17] -->
m

<!-- b004464 | furniture | pages [17] -->
m

<!-- b004465 | furniture | pages [17] -->
m

<!-- b004466 | furniture | pages [17] -->
m

<!-- b004467 | furniture | pages [17] -->
m

<!-- b004468 | furniture | pages [17] -->
m

<!-- b004469 | furniture | pages [17] -->
m

<!-- b004470 | furniture | pages [17] -->
m

<!-- b004471 | furniture | pages [17] -->
m

<!-- b004472 | furniture | pages [17] -->
m

<!-- b004473 | furniture | pages [17] -->
m

<!-- b004474 | furniture | pages [17] -->
m

<!-- b004475 | furniture | pages [17] -->
m

<!-- b004476 | furniture | pages [19] -->
Team # 2504448

<!-- b004477 | furniture | pages [19] -->
Page 19 of 25

<!-- b004478 | prose | pages [19] -->
5

<!-- b004479 | heading | pages [19] -->
Adaptability of the Model

<!-- b004480 | prose | pages [19] -->
5.1

<!-- b004481 | heading | pages [19] -->
Data Collection and Processing

<!-- b004482 | prose | pages [19] -->
Miami and Juneau, though both facing overtourism challenges, show distinct tourism

<!-- b004483 | prose | pages [19] -->
微信公众号：数学模型

<!-- b004484 | prose | pages [19] -->
dynamics that require careful consideration in our modeling approach. Juneau, as a sea- sonal cruise-based destination, experiences significant fluctuations in visitor numbers, pri- marily influenced by seasonal factors and environmental constraints. In contrast, Miami is a year-round tourist hub with a diverse range of attractions, including beaches, cultural events, and nightlife, drawing visitors consistently across all seasons.

<!-- b004485 | prose | pages [19] -->
微信号：MATHmodels

<!-- b004486 | caption | pages [19] -->
Figure 15: Comparison of features in Miami and Juneau

<!-- b004487 | prose | pages [19] -->
The data is collected from a range of reliable sources. The demographic data such as population density, migration patterns, and ethnic group distributions are obtained from government databases and archival records. Some data are obtained from event statistics from major events such as Art Basel, Wynwood Art Walk, and the South Beach Wine & Food Festival. We also collect financial data related to cultural tourism revenue, public funding for the arts, and investments in cultural infrastructure from city budget reports. Lastly, we look for surveys such as the Knight Foundation’s Soul of the Community study provided insight into community engagement and perception of cultural activities.

<!-- b004488 | prose | pages [19] -->
To ensure comparability across indicators, the collected data are normalized using min-max scaling, which transforms data values into a comparable range of [0, 1]. Then, in order to determine the relative importance of each cultural indicator, the entropy weight- ing method is applied. Entropy measures the degree of variation in an indicator across all years. Once entropy values are calculated, the weights for each indicator are assigned.

<!-- b004489 | prose | pages [19] -->
A composite cultural index is derived by aggregating all weighted indicators for each year, providing a single measure of cultural evolution. This index captures the overall cultural development of Miami across different time periods.

<!-- b004490 | prose | pages [19] -->
m

<!-- b004491 | prose | pages [19] -->
m

<!-- b004492 | prose | pages [19] -->
m

<!-- b004493 | prose | pages [19] -->
m

<!-- b004494 | prose | pages [19] -->
m

<!-- b004495 | prose | pages [19] -->
m

<!-- b004496 | prose | pages [19] -->
m

<!-- b004497 | prose | pages [19] -->
m

<!-- b004498 | prose | pages [19] -->
m

<!-- b004499 | prose | pages [19] -->
m

<!-- b004500 | prose | pages [19] -->
m

<!-- b004501 | prose | pages [19] -->
m

<!-- b004502 | prose | pages [19] -->
m

<!-- b004503 | prose | pages [19] -->
m

<!-- b004504 | prose | pages [19] -->
m

<!-- b004505 | prose | pages [19] -->
m

<!-- b004506 | prose | pages [19] -->
m

<!-- b004507 | prose | pages [19] -->
m

<!-- b004508 | prose | pages [19] -->
m

<!-- b004509 | prose | pages [19] -->
m

<!-- b004510 | prose | pages [19] -->
m

<!-- b004511 | prose | pages [19] -->
m

<!-- b004512 | prose | pages [19] -->
m

<!-- b004513 | prose | pages [19] -->
m

<!-- b004514 | prose | pages [19] -->
m

<!-- b004515 | prose | pages [19] -->
m

<!-- b004516 | prose | pages [19] -->
m

<!-- b004517 | prose | pages [19] -->
m

<!-- b004518 | prose | pages [19] -->
m

<!-- b004519 | prose | pages [19] -->
m

<!-- b004520 | prose | pages [19] -->
m

<!-- b004521 | prose | pages [19] -->
m

<!-- b004522 | prose | pages [19] -->
m

<!-- b004523 | prose | pages [19] -->
m

<!-- b004524 | prose | pages [19] -->
m

<!-- b004525 | prose | pages [19] -->
m

<!-- b004526 | prose | pages [19] -->
m

<!-- b004527 | prose | pages [19] -->
m

<!-- b004528 | prose | pages [19] -->
m

<!-- b004529 | prose | pages [19] -->
m

<!-- b004530 | prose | pages [19] -->
m

<!-- b004531 | prose | pages [19] -->
m

<!-- b004532 | prose | pages [19] -->
m

<!-- b004533 | prose | pages [19] -->
m

<!-- b004534 | prose | pages [19] -->
m

<!-- b004535 | prose | pages [19] -->
m

<!-- b004536 | prose | pages [19] -->
m

<!-- b004537 | prose | pages [19] -->
m

<!-- b004538 | prose | pages [19] -->
m

<!-- b004539 | prose | pages [19] -->
m

<!-- b004540 | prose | pages [19] -->
m

<!-- b004541 | prose | pages [19] -->
m

<!-- b004542 | prose | pages [19] -->
m

<!-- b004543 | prose | pages [19] -->
m

<!-- b004544 | prose | pages [19] -->
m

<!-- b004545 | prose | pages [19] -->
m

<!-- b004546 | prose | pages [19] -->
m

<!-- b004547 | prose | pages [19] -->
m

<!-- b004548 | prose | pages [19] -->
m

<!-- b004549 | prose | pages [19] -->
m

<!-- b004550 | prose | pages [19] -->
m

<!-- b004551 | prose | pages [19] -->
m

<!-- b004552 | prose | pages [19] -->
m

<!-- b004553 | prose | pages [19] -->
m

<!-- b004554 | prose | pages [19] -->
m

<!-- b004555 | prose | pages [19] -->
m

<!-- b004556 | prose | pages [19] -->
m

<!-- b004557 | prose | pages [19] -->
m

<!-- b004558 | prose | pages [19] -->
m

<!-- b004559 | prose | pages [19] -->
m

<!-- b004560 | prose | pages [19] -->
m

<!-- b004561 | prose | pages [19] -->
m

<!-- b004562 | prose | pages [19] -->
m

<!-- b004563 | prose | pages [19] -->
m

<!-- b004564 | prose | pages [19] -->
m

<!-- b004565 | prose | pages [19] -->
m

<!-- b004566 | prose | pages [19] -->
m

<!-- b004567 | prose | pages [19] -->
m

<!-- b004568 | prose | pages [19] -->
m

<!-- b004569 | prose | pages [19] -->
m

<!-- b004570 | prose | pages [19] -->
m

<!-- b004571 | prose | pages [19] -->
m

<!-- b004572 | prose | pages [19] -->
m

<!-- b004573 | prose | pages [19] -->
m

<!-- b004574 | prose | pages [19] -->
m

<!-- b004575 | prose | pages [19] -->
m

<!-- b004576 | prose | pages [19] -->
m

<!-- b004577 | prose | pages [19] -->
m

<!-- b004578 | prose | pages [19] -->
m

<!-- b004579 | prose | pages [19] -->
m

<!-- b004580 | prose | pages [19] -->
m

<!-- b004581 | prose | pages [19] -->
m

<!-- b004582 | prose | pages [19] -->
m

<!-- b004583 | prose | pages [19] -->
m

<!-- b004584 | prose | pages [19] -->
m

<!-- b004585 | prose | pages [19] -->
m

<!-- b004586 | prose | pages [19] -->
m

<!-- b004587 | prose | pages [19] -->
m

<!-- b004588 | prose | pages [19] -->
m

<!-- b004589 | prose | pages [19] -->
m

<!-- b004590 | prose | pages [19] -->
m

<!-- b004591 | prose | pages [19] -->
m

<!-- b004592 | prose | pages [19] -->
m

<!-- b004593 | prose | pages [19] -->
m

<!-- b004594 | prose | pages [19] -->
m

<!-- b004595 | prose | pages [19] -->
m

<!-- b004596 | prose | pages [19] -->
m

<!-- b004597 | prose | pages [19] -->
m

<!-- b004598 | prose | pages [19] -->
m

<!-- b004599 | prose | pages [19] -->
m

<!-- b004600 | prose | pages [19] -->
m

<!-- b004601 | prose | pages [19] -->
m

<!-- b004602 | prose | pages [19] -->
m

<!-- b004603 | prose | pages [19] -->
m

<!-- b004604 | prose | pages [19] -->
m

<!-- b004605 | prose | pages [19] -->
m

<!-- b004606 | prose | pages [19] -->
m

<!-- b004607 | prose | pages [19] -->
m

<!-- b004608 | prose | pages [19] -->
m

<!-- b004609 | prose | pages [19] -->
m

<!-- b004610 | prose | pages [19] -->
m

<!-- b004611 | prose | pages [19] -->
m

<!-- b004612 | prose | pages [19] -->
m

<!-- b004613 | prose | pages [19] -->
m

<!-- b004614 | prose | pages [19] -->
m

<!-- b004615 | prose | pages [19] -->
m

<!-- b004616 | prose | pages [19] -->
m

<!-- b004617 | prose | pages [19] -->
m

<!-- b004618 | prose | pages [19] -->
m

<!-- b004619 | prose | pages [19] -->
m

<!-- b004620 | prose | pages [19] -->
m

<!-- b004621 | prose | pages [19] -->
m

<!-- b004622 | prose | pages [19] -->
m

<!-- b004623 | prose | pages [19] -->
m

<!-- b004624 | prose | pages [19] -->
m

<!-- b004625 | prose | pages [19] -->
m

<!-- b004626 | prose | pages [19] -->
m

<!-- b004627 | prose | pages [19] -->
m

<!-- b004628 | prose | pages [19] -->
m

<!-- b004629 | prose | pages [19] -->
m

<!-- b004630 | prose | pages [19] -->
m

<!-- b004631 | prose | pages [19] -->
m

<!-- b004632 | prose | pages [19] -->
m

<!-- b004633 | prose | pages [19] -->
m

<!-- b004634 | prose | pages [19] -->
m

<!-- b004635 | prose | pages [19] -->
m

<!-- b004636 | prose | pages [19] -->
m

<!-- b004637 | prose | pages [19] -->
m

<!-- b004638 | prose | pages [19] -->
m

<!-- b004639 | prose | pages [19] -->
m

<!-- b004640 | prose | pages [19] -->
m

<!-- b004641 | prose | pages [19] -->
m

<!-- b004642 | prose | pages [19] -->
m

<!-- b004643 | prose | pages [19] -->
m

<!-- b004644 | prose | pages [19] -->
m

<!-- b004645 | prose | pages [19] -->
m

<!-- b004646 | prose | pages [19] -->
m

<!-- b004647 | prose | pages [19] -->
m

<!-- b004648 | prose | pages [19] -->
m

<!-- b004649 | prose | pages [19] -->
m

<!-- b004650 | prose | pages [19] -->
m

<!-- b004651 | prose | pages [19] -->
m

<!-- b004652 | prose | pages [19] -->
m

<!-- b004653 | prose | pages [19] -->
m

<!-- b004654 | prose | pages [19] -->
m

<!-- b004655 | prose | pages [19] -->
m

<!-- b004656 | prose | pages [19] -->
m

<!-- b004657 | prose | pages [19] -->
m

<!-- b004658 | prose | pages [19] -->
m

<!-- b004659 | prose | pages [19] -->
m

<!-- b004660 | prose | pages [19] -->
m

<!-- b004661 | prose | pages [19] -->
m

<!-- b004662 | prose | pages [19] -->
m

<!-- b004663 | prose | pages [19] -->
m

<!-- b004664 | prose | pages [19] -->
m

<!-- b004665 | prose | pages [19] -->
m

<!-- b004666 | prose | pages [19] -->
m

<!-- b004667 | prose | pages [19] -->
m

<!-- b004668 | prose | pages [19] -->
m

<!-- b004669 | prose | pages [19] -->
m

<!-- b004670 | prose | pages [19] -->
m

<!-- b004671 | prose | pages [19] -->
m

<!-- b004672 | prose | pages [19] -->
m

<!-- b004673 | prose | pages [19] -->
m

<!-- b004674 | prose | pages [19] -->
m

<!-- b004675 | prose | pages [19] -->
m

<!-- b004676 | prose | pages [19] -->
m

<!-- b004677 | prose | pages [19] -->
m

<!-- b004678 | prose | pages [19] -->
m

<!-- b004679 | prose | pages [19] -->
m

<!-- b004680 | prose | pages [19] -->
m

<!-- b004681 | prose | pages [19] -->
m

<!-- b004682 | prose | pages [19] -->
m

<!-- b004683 | prose | pages [19] -->
m

<!-- b004684 | prose | pages [19] -->
m

<!-- b004685 | prose | pages [19] -->
m

<!-- b004686 | prose | pages [19] -->
m

<!-- b004687 | prose | pages [19] -->
m

<!-- b004688 | prose | pages [19] -->
m

<!-- b004689 | prose | pages [19] -->
m

<!-- b004690 | prose | pages [19] -->
m

<!-- b004691 | prose | pages [19] -->
m

<!-- b004692 | prose | pages [19] -->
m

<!-- b004693 | prose | pages [19] -->
m

<!-- b004694 | prose | pages [19] -->
m

<!-- b004695 | prose | pages [19] -->
m

<!-- b004696 | prose | pages [19] -->
m

<!-- b004697 | prose | pages [19] -->
m

<!-- b004698 | prose | pages [19] -->
m

<!-- b004699 | prose | pages [19] -->
m

<!-- b004700 | prose | pages [19] -->
m

<!-- b004701 | prose | pages [19] -->
m

<!-- b004702 | prose | pages [19] -->
m

<!-- b004703 | prose | pages [19] -->
m

<!-- b004704 | prose | pages [19] -->
m

<!-- b004705 | prose | pages [19] -->
m

<!-- b004706 | prose | pages [19] -->
m

<!-- b004707 | prose | pages [19] -->
m

<!-- b004708 | prose | pages [19] -->
m

<!-- b004709 | prose | pages [19] -->
m

<!-- b004710 | prose | pages [19] -->
m

<!-- b004711 | prose | pages [19] -->
m

<!-- b004712 | prose | pages [19] -->
m

<!-- b004713 | prose | pages [19] -->
m

<!-- b004714 | prose | pages [19] -->
m

<!-- b004715 | prose | pages [19] -->
m

<!-- b004716 | prose | pages [19] -->
m

<!-- b004717 | prose | pages [19] -->
m

<!-- b004718 | prose | pages [19] -->
m

<!-- b004719 | prose | pages [19] -->
m

<!-- b004720 | prose | pages [19] -->
m

<!-- b004721 | prose | pages [19] -->
m

<!-- b004722 | prose | pages [19] -->
m

<!-- b004723 | prose | pages [19] -->
m

<!-- b004724 | prose | pages [19] -->
m

<!-- b004725 | prose | pages [19] -->
m

<!-- b004726 | prose | pages [19] -->
m

<!-- b004727 | prose | pages [19] -->
m

<!-- b004728 | prose | pages [19] -->
m

<!-- b004729 | prose | pages [19] -->
m

<!-- b004730 | prose | pages [19] -->
m

<!-- b004731 | prose | pages [19] -->
m

<!-- b004732 | prose | pages [19] -->
m

<!-- b004733 | prose | pages [19] -->
m

<!-- b004734 | prose | pages [19] -->
m

<!-- b004735 | prose | pages [19] -->
m

<!-- b004736 | prose | pages [19] -->
m

<!-- b004737 | prose | pages [19] -->
m

<!-- b004738 | prose | pages [19] -->
m

<!-- b004739 | prose | pages [19] -->
m

<!-- b004740 | prose | pages [19] -->
m

<!-- b004741 | prose | pages [19] -->
m

<!-- b004742 | prose | pages [19] -->
m

<!-- b004743 | prose | pages [19] -->
m

<!-- b004744 | prose | pages [19] -->
m

<!-- b004745 | prose | pages [19] -->
m

<!-- b004746 | prose | pages [19] -->
m

<!-- b004747 | prose | pages [19] -->
m

<!-- b004748 | prose | pages [19] -->
m

<!-- b004749 | prose | pages [19] -->
m

<!-- b004750 | prose | pages [19] -->
m

<!-- b004751 | prose | pages [19] -->
m

<!-- b004752 | prose | pages [19] -->
m

<!-- b004753 | prose | pages [19] -->
m

<!-- b004754 | prose | pages [19] -->
m

<!-- b004755 | prose | pages [19] -->
m

<!-- b004756 | prose | pages [19] -->
m

<!-- b004757 | prose | pages [19] -->
m

<!-- b004758 | prose | pages [19] -->
m

<!-- b004759 | prose | pages [19] -->
m

<!-- b004760 | prose | pages [19] -->
m

<!-- b004761 | prose | pages [19] -->
m

<!-- b004762 | prose | pages [19] -->
m

<!-- b004763 | prose | pages [19] -->
m

<!-- b004764 | prose | pages [19] -->
m

<!-- b004765 | prose | pages [19] -->
m

<!-- b004766 | prose | pages [19] -->
m

<!-- b004767 | prose | pages [19] -->
m

<!-- b004768 | prose | pages [19] -->
m

<!-- b004769 | prose | pages [19] -->
m

<!-- b004770 | prose | pages [19] -->
m

<!-- b004771 | prose | pages [19] -->
m

<!-- b004772 | prose | pages [19] -->
m

<!-- b004773 | prose | pages [19] -->
m

<!-- b004774 | furniture | pages [19] -->
m

<!-- b004775 | furniture | pages [19] -->
m

<!-- b004776 | furniture | pages [19] -->
m

<!-- b004777 | furniture | pages [19] -->
m

<!-- b004778 | furniture | pages [19] -->
m

<!-- b004779 | furniture | pages [19] -->
m

<!-- b004780 | furniture | pages [19] -->
m

<!-- b004781 | furniture | pages [19] -->
m

<!-- b004782 | furniture | pages [19] -->
m

<!-- b004783 | furniture | pages [19] -->
m

<!-- b004784 | furniture | pages [19] -->
m

<!-- b004785 | furniture | pages [19] -->
m

<!-- b004786 | furniture | pages [19] -->
m

<!-- b004787 | furniture | pages [19] -->
m

<!-- b004788 | furniture | pages [19] -->
m

<!-- b004789 | furniture | pages [19] -->
m

<!-- b004790 | furniture | pages [19] -->
m

<!-- b004791 | furniture | pages [19] -->
m

<!-- b004792 | furniture | pages [19] -->
m

<!-- b004793 | furniture | pages [19] -->
m

<!-- b004794 | furniture | pages [19] -->
m

<!-- b004795 | furniture | pages [19] -->
m

<!-- b004796 | furniture | pages [19] -->
m

<!-- b004797 | furniture | pages [19] -->
m

<!-- b004798 | furniture | pages [19] -->
m

<!-- b004799 | furniture | pages [19] -->
m

<!-- b004800 | furniture | pages [19] -->
m

<!-- b004801 | furniture | pages [19] -->
m

<!-- b004802 | furniture | pages [19] -->
m

<!-- b004803 | furniture | pages [19] -->
m

<!-- b004804 | furniture | pages [19] -->
m

<!-- b004805 | furniture | pages [19] -->
m

<!-- b004806 | furniture | pages [19] -->
m

<!-- b004807 | furniture | pages [19] -->
m

<!-- b004808 | furniture | pages [19] -->
m

<!-- b004809 | furniture | pages [19] -->
m

<!-- b004810 | furniture | pages [19] -->
m

<!-- b004811 | furniture | pages [19] -->
m

<!-- b004812 | furniture | pages [19] -->
m

<!-- b004813 | furniture | pages [19] -->
m

<!-- b004814 | furniture | pages [19] -->
m

<!-- b004815 | furniture | pages [19] -->
m

<!-- b004816 | furniture | pages [19] -->
m

<!-- b004817 | furniture | pages [19] -->
m

<!-- b004818 | furniture | pages [19] -->
m

<!-- b004819 | furniture | pages [19] -->
m

<!-- b004820 | furniture | pages [19] -->
m

<!-- b004821 | furniture | pages [19] -->
m

<!-- b004822 | furniture | pages [19] -->
m

<!-- b004823 | furniture | pages [19] -->
m

<!-- b004824 | furniture | pages [19] -->
m

<!-- b004825 | furniture | pages [19] -->
m

<!-- b004826 | furniture | pages [19] -->
m

<!-- b004827 | furniture | pages [19] -->
m

<!-- b004828 | furniture | pages [19] -->
m

<!-- b004829 | furniture | pages [19] -->
m

<!-- b004830 | furniture | pages [19] -->
m

<!-- b004831 | furniture | pages [19] -->
m

<!-- b004832 | furniture | pages [19] -->
m

<!-- b004833 | furniture | pages [19] -->
m

<!-- b004834 | furniture | pages [19] -->
m

<!-- b004835 | furniture | pages [19] -->
m

<!-- b004836 | furniture | pages [19] -->
m

<!-- b004837 | furniture | pages [19] -->
m

<!-- b004838 | furniture | pages [19] -->
m

<!-- b004839 | furniture | pages [19] -->
m

<!-- b004840 | furniture | pages [19] -->
m

<!-- b004841 | furniture | pages [19] -->
m

<!-- b004842 | furniture | pages [19] -->
m

<!-- b004843 | furniture | pages [19] -->
m

<!-- b004844 | furniture | pages [19] -->
m

<!-- b004845 | furniture | pages [19] -->
m

<!-- b004846 | furniture | pages [19] -->
m

<!-- b004847 | furniture | pages [19] -->
m

<!-- b004848 | furniture | pages [19] -->
m

<!-- b004849 | furniture | pages [19] -->
m

<!-- b004850 | furniture | pages [19] -->
m

<!-- b004851 | furniture | pages [19] -->
m

<!-- b004852 | furniture | pages [19] -->
m

<!-- b004853 | furniture | pages [19] -->
m

<!-- b004854 | furniture | pages [19] -->
m

<!-- b004855 | furniture | pages [19] -->
m

<!-- b004856 | furniture | pages [19] -->
m

<!-- b004857 | furniture | pages [19] -->
m

<!-- b004858 | furniture | pages [19] -->
m

<!-- b004859 | furniture | pages [19] -->
m

<!-- b004860 | furniture | pages [19] -->
m

<!-- b004861 | furniture | pages [19] -->
m

<!-- b004862 | furniture | pages [19] -->
m

<!-- b004863 | furniture | pages [19] -->
m

<!-- b004864 | furniture | pages [19] -->
m

<!-- b004865 | furniture | pages [19] -->
m

<!-- b004866 | furniture | pages [19] -->
m

<!-- b004867 | furniture | pages [19] -->
m

<!-- b004868 | furniture | pages [19] -->
m

<!-- b004869 | furniture | pages [19] -->
m

<!-- b004870 | furniture | pages [19] -->
m

<!-- b004871 | furniture | pages [19] -->
m

<!-- b004872 | furniture | pages [19] -->
m

<!-- b004873 | furniture | pages [19] -->
m

<!-- b004874 | furniture | pages [19] -->
m

<!-- b004875 | furniture | pages [19] -->
m

<!-- b004876 | furniture | pages [19] -->
m

<!-- b004877 | furniture | pages [19] -->
m

<!-- b004878 | furniture | pages [19] -->
m

<!-- b004879 | furniture | pages [19] -->
m

<!-- b004880 | furniture | pages [19] -->
m

<!-- b004881 | furniture | pages [19] -->
m

<!-- b004882 | furniture | pages [19] -->
m

<!-- b004883 | furniture | pages [19] -->
m

<!-- b004884 | furniture | pages [19] -->
m

<!-- b004885 | furniture | pages [19] -->
m

<!-- b004886 | furniture | pages [19] -->
m

<!-- b004887 | furniture | pages [19] -->
m

<!-- b004888 | furniture | pages [19] -->
m

<!-- b004889 | furniture | pages [19] -->
m

<!-- b004890 | furniture | pages [19] -->
m

<!-- b004891 | furniture | pages [19] -->
m

<!-- b004892 | furniture | pages [19] -->
m

<!-- b004893 | furniture | pages [19] -->
m

<!-- b004894 | furniture | pages [19] -->
m

<!-- b004895 | furniture | pages [19] -->
m

<!-- b004896 | furniture | pages [19] -->
m

<!-- b004897 | furniture | pages [19] -->
m

<!-- b004898 | furniture | pages [19] -->
m

<!-- b004899 | furniture | pages [19] -->
m

<!-- b004900 | furniture | pages [19] -->
m

<!-- b004901 | furniture | pages [19] -->
m

<!-- b004902 | furniture | pages [19] -->
m

<!-- b004903 | furniture | pages [19] -->
m

<!-- b004904 | furniture | pages [19] -->
m

<!-- b004905 | furniture | pages [19] -->
m

<!-- b004906 | furniture | pages [19] -->
m

<!-- b004907 | furniture | pages [19] -->
m

<!-- b004908 | furniture | pages [19] -->
m

<!-- b004909 | furniture | pages [19] -->
m

<!-- b004910 | furniture | pages [19] -->
m

<!-- b004911 | furniture | pages [19] -->
m

<!-- b004912 | furniture | pages [19] -->
m

<!-- b004913 | furniture | pages [19] -->
m

<!-- b004914 | furniture | pages [19] -->
m

<!-- b004915 | furniture | pages [19] -->
m

<!-- b004916 | furniture | pages [19] -->
m

<!-- b004917 | furniture | pages [19] -->
m

<!-- b004918 | furniture | pages [19] -->
m

<!-- b004919 | furniture | pages [19] -->
m

<!-- b004920 | furniture | pages [19] -->
m

<!-- b004921 | furniture | pages [19] -->
m

<!-- b004922 | furniture | pages [19] -->
m

<!-- b004923 | furniture | pages [19] -->
m

<!-- b004924 | furniture | pages [19] -->
m

<!-- b004925 | furniture | pages [19] -->
m

<!-- b004926 | furniture | pages [19] -->
m

<!-- b004927 | furniture | pages [19] -->
m

<!-- b004928 | furniture | pages [19] -->
m

<!-- b004929 | furniture | pages [19] -->
m

<!-- b004930 | furniture | pages [19] -->
m

<!-- b004931 | furniture | pages [19] -->
m

<!-- b004932 | furniture | pages [19] -->
m

<!-- b004933 | furniture | pages [19] -->
m

<!-- b004934 | furniture | pages [19] -->
m

<!-- b004935 | furniture | pages [19] -->
m

<!-- b004936 | furniture | pages [19] -->
m

<!-- b004937 | furniture | pages [19] -->
m

<!-- b004938 | furniture | pages [19] -->
m

<!-- b004939 | furniture | pages [19] -->
m

<!-- b004940 | furniture | pages [19] -->
m

<!-- b004941 | furniture | pages [19] -->
m

<!-- b004942 | furniture | pages [19] -->
m

<!-- b004943 | furniture | pages [19] -->
m

<!-- b004944 | furniture | pages [19] -->
m

<!-- b004945 | furniture | pages [19] -->
m

<!-- b004946 | furniture | pages [19] -->
m

<!-- b004947 | furniture | pages [19] -->
m

<!-- b004948 | furniture | pages [19] -->
m

<!-- b004949 | furniture | pages [19] -->
m

<!-- b004950 | furniture | pages [19] -->
m

<!-- b004951 | furniture | pages [19] -->
m

<!-- b004952 | furniture | pages [19] -->
m

<!-- b004953 | furniture | pages [19] -->
m

<!-- b004954 | furniture | pages [19] -->
m

<!-- b004955 | furniture | pages [19] -->
m

<!-- b004956 | furniture | pages [19] -->
m

<!-- b004957 | furniture | pages [19] -->
m

<!-- b004958 | furniture | pages [19] -->
m

<!-- b004959 | furniture | pages [19] -->
m

<!-- b004960 | furniture | pages [19] -->
m

<!-- b004961 | furniture | pages [19] -->
m

<!-- b004962 | furniture | pages [19] -->
m

<!-- b004963 | furniture | pages [19] -->
m

<!-- b004964 | furniture | pages [19] -->
m

<!-- b004965 | furniture | pages [19] -->
m

<!-- b004966 | furniture | pages [19] -->
m

<!-- b004967 | furniture | pages [19] -->
m

<!-- b004968 | furniture | pages [19] -->
m

<!-- b004969 | furniture | pages [19] -->
m

<!-- b004970 | furniture | pages [19] -->
m

<!-- b004971 | furniture | pages [19] -->
m

<!-- b004972 | furniture | pages [19] -->
m

<!-- b004973 | furniture | pages [19] -->
m

<!-- b004974 | furniture | pages [19] -->
m

<!-- b004975 | furniture | pages [19] -->
m

<!-- b004976 | furniture | pages [19] -->
m

<!-- b004977 | furniture | pages [19] -->
m

<!-- b004978 | furniture | pages [19] -->
m

<!-- b004979 | furniture | pages [19] -->
m

<!-- b004980 | furniture | pages [19] -->
m

<!-- b004981 | furniture | pages [19] -->
m

<!-- b004982 | furniture | pages [19] -->
m

<!-- b004983 | furniture | pages [19] -->
m

<!-- b004984 | furniture | pages [19] -->
m

<!-- b004985 | furniture | pages [19] -->
m

<!-- b004986 | furniture | pages [19] -->
m

<!-- b004987 | furniture | pages [19] -->
m

<!-- b004988 | furniture | pages [19] -->
m

<!-- b004989 | furniture | pages [19] -->
m

<!-- b004990 | furniture | pages [19] -->
m

<!-- b004991 | furniture | pages [19] -->
m

<!-- b004992 | furniture | pages [19] -->
m

<!-- b004993 | furniture | pages [19] -->
m

<!-- b004994 | furniture | pages [19] -->
m

<!-- b004995 | furniture | pages [19] -->
m

<!-- b004996 | furniture | pages [19] -->
m

<!-- b004997 | furniture | pages [19] -->
m

<!-- b004998 | furniture | pages [19] -->
m

<!-- b004999 | furniture | pages [19] -->
m

<!-- b005000 | furniture | pages [19] -->
m

<!-- b005001 | furniture | pages [19] -->
m

<!-- b005002 | furniture | pages [19] -->
m

<!-- b005003 | furniture | pages [19] -->
m

<!-- b005004 | furniture | pages [19] -->
m

<!-- b005005 | furniture | pages [19] -->
m

<!-- b005006 | furniture | pages [19] -->
m

<!-- b005007 | furniture | pages [19] -->
m

<!-- b005008 | furniture | pages [19] -->
m

<!-- b005009 | furniture | pages [19] -->
m

<!-- b005010 | furniture | pages [19] -->
m

<!-- b005011 | furniture | pages [19] -->
m

<!-- b005012 | furniture | pages [19] -->
m

<!-- b005013 | furniture | pages [19] -->
m

<!-- b005014 | furniture | pages [19] -->
m

<!-- b005015 | furniture | pages [19] -->
m

<!-- b005016 | furniture | pages [19] -->
m

<!-- b005017 | furniture | pages [19] -->
m

<!-- b005018 | furniture | pages [19] -->
m

<!-- b005019 | furniture | pages [19] -->
m

<!-- b005020 | furniture | pages [19] -->
m

<!-- b005021 | furniture | pages [19] -->
m

<!-- b005022 | furniture | pages [19] -->
m

<!-- b005023 | furniture | pages [19] -->
m

<!-- b005024 | furniture | pages [19] -->
m

<!-- b005025 | furniture | pages [19] -->
m

<!-- b005026 | furniture | pages [19] -->
m

<!-- b005027 | furniture | pages [19] -->
m

<!-- b005028 | furniture | pages [19] -->
m

<!-- b005029 | furniture | pages [19] -->
m

<!-- b005030 | furniture | pages [19] -->
m

<!-- b005031 | furniture | pages [19] -->
m

<!-- b005032 | furniture | pages [19] -->
m

<!-- b005033 | furniture | pages [19] -->
m

<!-- b005034 | furniture | pages [19] -->
m

<!-- b005035 | furniture | pages [19] -->
m

<!-- b005036 | furniture | pages [19] -->
m

<!-- b005037 | furniture | pages [19] -->
m

<!-- b005038 | furniture | pages [19] -->
m

<!-- b005039 | furniture | pages [19] -->
m

<!-- b005040 | furniture | pages [19] -->
m

<!-- b005041 | furniture | pages [19] -->
m

<!-- b005042 | furniture | pages [19] -->
m

<!-- b005043 | furniture | pages [19] -->
m

<!-- b005044 | furniture | pages [19] -->
m

<!-- b005045 | furniture | pages [19] -->
m

<!-- b005046 | furniture | pages [19] -->
m

<!-- b005047 | furniture | pages [19] -->
m

<!-- b005048 | furniture | pages [19] -->
m

<!-- b005049 | furniture | pages [19] -->
m

<!-- b005050 | furniture | pages [19] -->
m

<!-- b005051 | furniture | pages [19] -->
m

<!-- b005052 | furniture | pages [19] -->
m

<!-- b005053 | furniture | pages [19] -->
m

<!-- b005054 | furniture | pages [19] -->
m

<!-- b005055 | furniture | pages [19] -->
m

<!-- b005056 | furniture | pages [19] -->
m

<!-- b005057 | furniture | pages [19] -->
m

<!-- b005058 | furniture | pages [19] -->
m

<!-- b005059 | furniture | pages [19] -->
m

<!-- b005060 | furniture | pages [19] -->
m

<!-- b005061 | furniture | pages [19] -->
m

<!-- b005062 | furniture | pages [19] -->
m

<!-- b005063 | furniture | pages [19] -->
m

<!-- b005064 | furniture | pages [19] -->
m

<!-- b005065 | furniture | pages [19] -->
m

<!-- b005066 | furniture | pages [19] -->
m

<!-- b005067 | furniture | pages [19] -->
m

<!-- b005068 | furniture | pages [19] -->
m

<!-- b005069 | furniture | pages [19] -->
m

<!-- b005070 | furniture | pages [19] -->
m

<!-- b005071 | furniture | pages [19] -->
m

<!-- b005072 | furniture | pages [19] -->
m

<!-- b005073 | furniture | pages [19] -->
m

<!-- b005074 | furniture | pages [19] -->
m

<!-- b005075 | furniture | pages [19] -->
m

<!-- b005076 | furniture | pages [19] -->
m

<!-- b005077 | furniture | pages [19] -->
m

<!-- b005078 | furniture | pages [19] -->
m

<!-- b005079 | furniture | pages [19] -->
m

<!-- b005080 | furniture | pages [19] -->
m

<!-- b005081 | furniture | pages [19] -->
m

<!-- b005082 | furniture | pages [19] -->
m

<!-- b005083 | furniture | pages [19] -->
m

<!-- b005084 | furniture | pages [19] -->
m

<!-- b005085 | furniture | pages [19] -->
m

<!-- b005086 | furniture | pages [19] -->
m

<!-- b005087 | furniture | pages [19] -->
m

<!-- b005088 | furniture | pages [19] -->
m

<!-- b005089 | furniture | pages [19] -->
m

<!-- b005090 | furniture | pages [19] -->
m

<!-- b005091 | furniture | pages [19] -->
m

<!-- b005092 | furniture | pages [19] -->
m

<!-- b005093 | furniture | pages [19] -->
m

<!-- b005094 | furniture | pages [19] -->
m

<!-- b005095 | furniture | pages [19] -->
m

<!-- b005096 | furniture | pages [19] -->
m

<!-- b005097 | furniture | pages [19] -->
m

<!-- b005098 | furniture | pages [19] -->
m

<!-- b005099 | furniture | pages [19] -->
m

<!-- b005100 | furniture | pages [19] -->
m

<!-- b005101 | furniture | pages [19] -->
m

<!-- b005102 | furniture | pages [19] -->
m

<!-- b005103 | furniture | pages [19] -->
m

<!-- b005104 | furniture | pages [19] -->
m

<!-- b005105 | furniture | pages [19] -->
m

<!-- b005106 | furniture | pages [19] -->
m

<!-- b005107 | furniture | pages [19] -->
m

<!-- b005108 | furniture | pages [19] -->
m

<!-- b005109 | furniture | pages [19] -->
m

<!-- b005110 | furniture | pages [19] -->
m

<!-- b005111 | furniture | pages [19] -->
m

<!-- b005112 | furniture | pages [19] -->
m

<!-- b005113 | furniture | pages [19] -->
m

<!-- b005114 | furniture | pages [19] -->
m

<!-- b005115 | furniture | pages [19] -->
m

<!-- b005116 | furniture | pages [19] -->
m

<!-- b005117 | furniture | pages [19] -->
m

<!-- b005118 | furniture | pages [19] -->
m

<!-- b005119 | furniture | pages [19] -->
m

<!-- b005120 | furniture | pages [19] -->
m

<!-- b005121 | furniture | pages [19] -->
m

<!-- b005122 | furniture | pages [19] -->
m

<!-- b005123 | furniture | pages [19] -->
m

<!-- b005124 | furniture | pages [19] -->
m

<!-- b005125 | furniture | pages [19] -->
m

<!-- b005126 | furniture | pages [19] -->
m

<!-- b005127 | furniture | pages [19] -->
m

<!-- b005128 | furniture | pages [19] -->
m

<!-- b005129 | furniture | pages [19] -->
m

<!-- b005130 | furniture | pages [19] -->
m

<!-- b005131 | furniture | pages [19] -->
m

<!-- b005132 | furniture | pages [19] -->
m

<!-- b005133 | furniture | pages [19] -->
m

<!-- b005134 | furniture | pages [19] -->
m

<!-- b005135 | furniture | pages [19] -->
m

<!-- b005136 | furniture | pages [19] -->
m

<!-- b005137 | furniture | pages [19] -->
m

<!-- b005138 | furniture | pages [19] -->
m

<!-- b005139 | furniture | pages [19] -->
m

<!-- b005140 | furniture | pages [19] -->
m

<!-- b005141 | furniture | pages [19] -->
m

<!-- b005142 | furniture | pages [19] -->
m

<!-- b005143 | furniture | pages [19] -->
m

<!-- b005144 | furniture | pages [19] -->
m

<!-- b005145 | furniture | pages [19] -->
m

<!-- b005146 | furniture | pages [19] -->
m

<!-- b005147 | furniture | pages [19] -->
m

<!-- b005148 | furniture | pages [19] -->
m

<!-- b005149 | furniture | pages [19] -->
m

<!-- b005150 | furniture | pages [19] -->
m

<!-- b005151 | furniture | pages [19] -->
m

<!-- b005152 | furniture | pages [19] -->
m

<!-- b005153 | furniture | pages [19] -->
m

<!-- b005154 | furniture | pages [19] -->
m

<!-- b005155 | furniture | pages [19] -->
m

<!-- b005156 | furniture | pages [19] -->
m

<!-- b005157 | furniture | pages [19] -->
m

<!-- b005158 | furniture | pages [19] -->
m

<!-- b005159 | furniture | pages [19] -->
m

<!-- b005160 | furniture | pages [19] -->
m

<!-- b005161 | furniture | pages [19] -->
m

<!-- b005162 | furniture | pages [19] -->
m

<!-- b005163 | furniture | pages [19] -->
m

<!-- b005164 | furniture | pages [19] -->
m

<!-- b005165 | furniture | pages [19] -->
m

<!-- b005166 | furniture | pages [19] -->
m

<!-- b005167 | furniture | pages [19] -->
m

<!-- b005168 | furniture | pages [19] -->
m

<!-- b005169 | furniture | pages [19] -->
m

<!-- b005170 | furniture | pages [19] -->
m

<!-- b005171 | furniture | pages [19] -->
m

<!-- b005172 | furniture | pages [19] -->
m

<!-- b005173 | furniture | pages [19] -->
m

<!-- b005174 | furniture | pages [19] -->
m

<!-- b005175 | furniture | pages [19] -->
m

<!-- b005176 | furniture | pages [19] -->
m

<!-- b005177 | furniture | pages [20] -->
Team # 2504448

<!-- b005178 | prose | pages [20] -->
Ci =

<!-- b005179 | furniture | pages [20] -->
Page 20 of 25

<!-- b005180 | prose | pages [20] -->
m m ∑ ∑

<!-- b005181 | prose | pages [20] -->
wjxij (20)

<!-- b005182 | prose | pages [20] -->
j=1 j=1

<!-- b005183 | prose | pages [20] -->
Cultural Index and Tourist Count Trends in Miami (2019 2023)

<!-- b005184 | prose | pages [20] -->
1.0

<!-- b005185 | prose | pages [20] -->
0.8

<!-- b005186 | prose | pages [20] -->
Cultural Index

<!-- b005187 | prose | pages [20] -->
0.6

<!-- b005188 | prose | pages [20] -->
0.4

<!-- b005189 | prose | pages [20] -->
0.2

<!-- b005190 | prose | pages [20] -->
0.0

<!-- b005191 | prose | pages [20] -->
2019 2020

<!-- b005192 | prose | pages [20] -->
7

<!-- b005193 | prose | pages [20] -->
6

<!-- b005194 | prose | pages [20] -->
Tourist Count (in millions)

<!-- b005195 | prose | pages [20] -->
5

<!-- b005196 | prose | pages [20] -->
4

<!-- b005197 | prose | pages [20] -->
3

<!-- b005198 | prose | pages [20] -->
2

<!-- b005199 | prose | pages [20] -->
1

<!-- b005200 | prose | pages [20] -->
Cultural Index Tourist Count

<!-- b005201 | prose | pages [20] -->
0

<!-- b005202 | prose | pages [20] -->
2021 2022 2023 Year

<!-- b005203 | caption | pages [20] -->
Figure 16: Cultural index in Miami computed by entropy weight method

<!-- b005204 | prose | pages [20] -->
5.2 Adaptation to Miami tourism

<!-- b005205 | prose | pages [20] -->
Miami’s tourism industry differs significantly from Juneau, requiring adjustments to our multi-objective dynamic programming model. While Juneau experiences highly sea- sonal tourism with a strong focus on natural attractions, Miami attracts a steady influx of international tourists year-round, drawn by its cultural, urban, and environmental offer- ings. The differences between the two cities and the corresponding model adjustments are summarized in Table 4.

<!-- b005206 | caption | pages [20] -->
Table 4: Comparison of Juneau and Miami tourism features and model adaptations

<!-- b005207 | prose | pages [20] -->
City City Features

<!-- b005208 | heading | pages [20] -->
Model Features

<!-- b005209 | prose | pages [20] -->
• Small population with limited Juneau urban space.

<!-- b005210 | prose | pages [20] -->
• Overcrowding heavily im- pacts resident satisfaction.

<!-- b005211 | prose | pages [20] -->
• Transportation relies primar- ily on cruise lines.

<!-- b005212 | prose | pages [20] -->
• Cruise passengers are consid- ered in tourist volume.

<!-- b005213 | prose | pages [20] -->
• Environment is the primary attraction.

<!-- b005214 | prose | pages [20] -->
• Environmental impact is a key optimization factor.

<!-- b005215 | prose | pages [20] -->
• Infrastructure needs govern- ment support.

<!-- b005216 | prose | pages [20] -->
• Government expenditure is weighted higher for impact.

<!-- b005217 | prose | pages [20] -->
Continued on next page

<!-- b005218 | prose | pages [20] -->
关注数学模型

<!-- b005219 | furniture | pages [20] -->
2

<!-- b005220 | furniture | pages [20] -->
MATHmodels

<!-- b005221 | furniture | pages [20] -->
获取更多资讯

<!-- b005222 | furniture | pages [21] -->
Team # 2504448

<!-- b005223 | furniture | pages [21] -->
Page 21 of 25

<!-- b005224 | prose | pages [21] -->
微信公众号：数学模型

<!-- b005225 | prose | pages [21] -->
City City Features

<!-- b005226 | heading | pages [21] -->
Model Features

<!-- b005227 | prose | pages [21] -->
• Large metropolitan area with Miami high population density.

<!-- b005228 | prose | pages [21] -->
• Overcrowding has less im- pact on resident satisfaction.

<!-- b005229 | prose | pages [21] -->
• More international travelers

<!-- b005230 | prose | pages [21] -->
• Focus on attracting interna- tional travelers.

<!-- b005231 | prose | pages [21] -->
with strong purchasing power.

<!-- b005232 | prose | pages [21] -->
•

<!-- b005233 | prose | pages [21] -->
• Multiple factors (culture, en-

<!-- b005234 | prose | pages [21] -->
resources Attractions and include environment, culture, and cityscape.

<!-- b005235 | prose | pages [21] -->
vironment, economy) to opti- mize.

<!-- b005236 | prose | pages [21] -->
微信号：MATHmodels

<!-- b005237 | prose | pages [21] -->
•

<!-- b005238 | prose | pages [21] -->
• Government expenditure has

<!-- b005239 | prose | pages [21] -->
infrastructure Developed

<!-- b005240 | prose | pages [21] -->
less impact.

<!-- b005241 | prose | pages [21] -->
with private sector influence.

<!-- b005242 | prose | pages [21] -->
Gov Revenue

<!-- b005243 | prose | pages [21] -->
Year Tourists

<!-- b005244 | prose | pages [21] -->
Tax Rate

<!-- b005245 | prose | pages [21] -->
Env

<!-- b005246 | prose | pages [21] -->
Culture

<!-- b005247 | prose | pages [21] -->
Resident

<!-- b005248 | prose | pages [21] -->
(Million $)

<!-- b005249 | prose | pages [21] -->
(thousands)

<!-- b005250 | prose | pages [21] -->
(%)

<!-- b005251 | prose | pages [21] -->
Index

<!-- b005252 | prose | pages [21] -->
Index

<!-- b005253 | prose | pages [21] -->
Sat 260.48 1 803.6 2.5 0.090 0.335 0.866 337.11 2 1040.1 2.5 0.149 0.342 0.865 368.92 3 1138.2 2.5 0.210 0.349 0.854 477.56 4 1473.4 2.5 0.273 0.359 0.843 427.26 5 1318.2 2.5 0.286 0.367 0.833

<!-- b005254 | caption | pages [21] -->
Table 5: Predictions of the optimized tourism plan for Miami over the next 5 years

<!-- b005255 | prose | pages [21] -->
To accurately reflect Miami’s tourism characteristics, several key modifications are made to the model.

<!-- b005256 | prose | pages [21] -->
Unlike Juneau, Miami experiences relatively stable year-round tourist inflow with slight seasonal peaks. The demand function is adapted to account for these more con- sistent trends and include factors that influence international tourism. Miami’s tourist

<!-- b005257 | heading | pages [21] -->
demand model incorporates cultural attractiveness, quantified by a cultural index C(t),

<!-- b005258 | prose | pages [21] -->
and government promotion, formulated as:

<!-- b005259 | prose | pages [21] -->
T(t) = T(t −1) · (1 + g(t) −γ · τ(t) + δ(t) + η · C(t)) (21)

<!-- b005260 | prose | pages [21] -->
Miami’s environmental concerns, such as coastal erosion and pollution, require changes to the environmental index calculation. Snow-related factors are replaced with metrics re- flecting ocean conditions and urban emissions.

<!-- b005261 | prose | pages [21] -->
Additional variables such as traffic congestion and cultural engagement are incorpo- rated into the resident satisfaction function to capture Miami’s urban dynamics. Incorpo- rating Miami’s cultural diversity and urban challenges, the updated resident satisfaction equation is:

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
1 −|T(t) −Topt|

<!-- b005371 | prose | pages [21] -->


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

<!-- b005428 | prose | pages [21] -->
m

<!-- b005429 | prose | pages [21] -->
m

<!-- b005430 | prose | pages [21] -->
m

<!-- b005431 | prose | pages [21] -->
m

<!-- b005432 | prose | pages [21] -->
m

<!-- b005433 | prose | pages [21] -->
m

<!-- b005434 | prose | pages [21] -->
m

<!-- b005435 | prose | pages [21] -->
m

<!-- b005436 | prose | pages [21] -->
m

<!-- b005437 | prose | pages [21] -->
m

<!-- b005438 | prose | pages [21] -->
m

<!-- b005439 | prose | pages [21] -->
m

<!-- b005440 | prose | pages [21] -->
m

<!-- b005441 | prose | pages [21] -->
m

<!-- b005442 | prose | pages [21] -->
m

<!-- b005443 | prose | pages [21] -->
m

<!-- b005444 | prose | pages [21] -->
m

<!-- b005445 | prose | pages [21] -->
m

<!-- b005446 | prose | pages [21] -->
m

<!-- b005447 | prose | pages [21] -->
m

<!-- b005448 | prose | pages [21] -->
m

<!-- b005449 | prose | pages [21] -->
m

<!-- b005450 | prose | pages [21] -->
m

<!-- b005451 | prose | pages [21] -->
Q(t) = ω1

<!-- b005452 | prose | pages [21] -->
m

<!-- b005453 | prose | pages [21] -->
m

<!-- b005454 | prose | pages [21] -->
m

<!-- b005455 | prose | pages [21] -->
m

<!-- b005456 | prose | pages [21] -->
m

<!-- b005457 | prose | pages [21] -->
m

<!-- b005458 | prose | pages [21] -->
m

<!-- b005459 | prose | pages [21] -->
m

<!-- b005460 | prose | pages [21] -->
m

<!-- b005461 | prose | pages [21] -->
m

<!-- b005462 | prose | pages [21] -->
m

<!-- b005463 | prose | pages [21] -->
m

<!-- b005464 | prose | pages [21] -->
m

<!-- b005465 | prose | pages [21] -->
m

<!-- b005466 | prose | pages [21] -->
m

<!-- b005467 | prose | pages [21] -->
m

<!-- b005468 | prose | pages [21] -->
m

<!-- b005469 | prose | pages [21] -->
m

<!-- b005470 | prose | pages [21] -->
m

<!-- b005471 | prose | pages [21] -->
m

<!-- b005472 | prose | pages [21] -->
m

<!-- b005473 | prose | pages [21] -->
m

<!-- b005474 | prose | pages [21] -->
m

<!-- b005475 | prose | pages [21] -->
m

<!-- b005476 | prose | pages [21] -->
m

<!-- b005477 | prose | pages [21] -->
m

<!-- b005478 | prose | pages [21] -->
m

<!-- b005479 | prose | pages [21] -->
m

<!-- b005480 | prose | pages [21] -->
m

<!-- b005481 | prose | pages [21] -->
m

<!-- b005482 | prose | pages [21] -->
m

<!-- b005483 | prose | pages [21] -->
m

<!-- b005484 | prose | pages [21] -->
m

<!-- b005485 | prose | pages [21] -->
m

<!-- b005486 | prose | pages [21] -->
m

<!-- b005487 | prose | pages [21] -->
m

<!-- b005488 | prose | pages [21] -->
m

<!-- b005489 | prose | pages [21] -->
m

<!-- b005490 | prose | pages [21] -->
m

<!-- b005491 | prose | pages [21] -->
m

<!-- b005492 | prose | pages [21] -->
m

<!-- b005493 | prose | pages [21] -->
m

<!-- b005494 | prose | pages [21] -->
m

<!-- b005495 | prose | pages [21] -->
m

<!-- b005496 | prose | pages [21] -->
m

<!-- b005497 | prose | pages [21] -->
m

<!-- b005498 | prose | pages [21] -->
m

<!-- b005499 | prose | pages [21] -->
m

<!-- b005500 | prose | pages [21] -->
m

<!-- b005501 | prose | pages [21] -->
m

<!-- b005502 | prose | pages [21] -->
m

<!-- b005503 | prose | pages [21] -->
m

<!-- b005504 | prose | pages [21] -->
m

<!-- b005505 | prose | pages [21] -->
m

<!-- b005506 | prose | pages [21] -->
m

<!-- b005507 | prose | pages [21] -->
m

<!-- b005508 | prose | pages [21] -->
m

<!-- b005509 | prose | pages [21] -->
m

<!-- b005510 | prose | pages [21] -->
m

<!-- b005511 | prose | pages [21] -->
m

<!-- b005512 | prose | pages [21] -->
m

<!-- b005513 | prose | pages [21] -->
m

<!-- b005514 | prose | pages [21] -->
m

<!-- b005515 | prose | pages [21] -->
m

<!-- b005516 | prose | pages [21] -->
m

<!-- b005517 | prose | pages [21] -->
m

<!-- b005518 | prose | pages [21] -->
m

<!-- b005519 | prose | pages [21] -->
m

<!-- b005520 | prose | pages [21] -->
m

<!-- b005521 | prose | pages [21] -->
m

<!-- b005522 | prose | pages [21] -->
m

<!-- b005523 | prose | pages [21] -->
m

<!-- b005524 | prose | pages [21] -->
m

<!-- b005525 | prose | pages [21] -->
m

<!-- b005526 | prose | pages [21] -->
m

<!-- b005527 | prose | pages [21] -->
m

<!-- b005528 | prose | pages [21] -->
m

<!-- b005529 | prose | pages [21] -->
m

<!-- b005530 | prose | pages [21] -->
m

<!-- b005531 | prose | pages [21] -->
m

<!-- b005532 | prose | pages [21] -->
m

<!-- b005533 | prose | pages [21] -->
m

<!-- b005534 | prose | pages [21] -->
m

<!-- b005535 | prose | pages [21] -->
m

<!-- b005536 | prose | pages [21] -->
m

<!-- b005537 | prose | pages [21] -->
m

<!-- b005538 | prose | pages [21] -->
m

<!-- b005539 | prose | pages [21] -->
m

<!-- b005540 | prose | pages [21] -->
m

<!-- b005541 | prose | pages [21] -->
m

<!-- b005542 | prose | pages [21] -->
m

<!-- b005543 | prose | pages [21] -->
m

<!-- b005544 | prose | pages [21] -->
m

<!-- b005545 | prose | pages [21] -->
m

<!-- b005546 | prose | pages [21] -->
m

<!-- b005547 | prose | pages [21] -->
m

<!-- b005548 | prose | pages [21] -->
m

<!-- b005549 | prose | pages [21] -->
Topt

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

<!-- b005831 | furniture | pages [21] -->
m

<!-- b005832 | furniture | pages [21] -->
m

<!-- b005833 | furniture | pages [21] -->
m

<!-- b005834 | furniture | pages [21] -->
m

<!-- b005835 | furniture | pages [21] -->
m

<!-- b005836 | furniture | pages [21] -->
m

<!-- b005837 | furniture | pages [21] -->
m

<!-- b005838 | furniture | pages [21] -->
m

<!-- b005839 | furniture | pages [21] -->
m

<!-- b005840 | furniture | pages [21] -->
m

<!-- b005841 | furniture | pages [21] -->
m

<!-- b005842 | furniture | pages [21] -->
m

<!-- b005843 | furniture | pages [21] -->
m

<!-- b005844 | furniture | pages [21] -->
m

<!-- b005845 | furniture | pages [21] -->
m

<!-- b005846 | furniture | pages [21] -->
m

<!-- b005847 | furniture | pages [21] -->
m

<!-- b005848 | furniture | pages [21] -->
m

<!-- b005849 | furniture | pages [21] -->
m

<!-- b005850 | furniture | pages [21] -->
m

<!-- b005851 | furniture | pages [21] -->
m

<!-- b005852 | furniture | pages [21] -->
m

<!-- b005853 | furniture | pages [21] -->
m

<!-- b005854 | furniture | pages [21] -->
m

<!-- b005855 | furniture | pages [21] -->
m

<!-- b005856 | furniture | pages [21] -->
m

<!-- b005857 | furniture | pages [21] -->
m

<!-- b005858 | furniture | pages [21] -->
m

<!-- b005859 | furniture | pages [21] -->
m

<!-- b005860 | furniture | pages [21] -->
m

<!-- b005861 | furniture | pages [21] -->
m

<!-- b005862 | furniture | pages [21] -->
m

<!-- b005863 | furniture | pages [21] -->
m

<!-- b005864 | furniture | pages [21] -->
m

<!-- b005865 | furniture | pages [21] -->
m

<!-- b005866 | furniture | pages [21] -->
m

<!-- b005867 | furniture | pages [21] -->
m

<!-- b005868 | furniture | pages [21] -->
m

<!-- b005869 | furniture | pages [21] -->
m

<!-- b005870 | furniture | pages [21] -->
m

<!-- b005871 | furniture | pages [21] -->
m

<!-- b005872 | furniture | pages [21] -->
m

<!-- b005873 | furniture | pages [21] -->
m

<!-- b005874 | furniture | pages [21] -->
m

<!-- b005875 | furniture | pages [21] -->
m

<!-- b005876 | furniture | pages [21] -->
m

<!-- b005877 | furniture | pages [21] -->
m

<!-- b005878 | furniture | pages [21] -->
m

<!-- b005879 | furniture | pages [21] -->
m

<!-- b005880 | furniture | pages [21] -->
m

<!-- b005881 | furniture | pages [21] -->
m

<!-- b005882 | furniture | pages [21] -->
m

<!-- b005883 | furniture | pages [21] -->
m

<!-- b005884 | furniture | pages [21] -->
m

<!-- b005885 | furniture | pages [21] -->
m

<!-- b005886 | furniture | pages [21] -->
m

<!-- b005887 | furniture | pages [21] -->
m

<!-- b005888 | furniture | pages [21] -->
m

<!-- b005889 | furniture | pages [21] -->
m

<!-- b005890 | furniture | pages [21] -->
m

<!-- b005891 | furniture | pages [21] -->
m

<!-- b005892 | furniture | pages [21] -->
m

<!-- b005893 | furniture | pages [21] -->
m

<!-- b005894 | furniture | pages [21] -->
m

<!-- b005895 | furniture | pages [21] -->
m

<!-- b005896 | furniture | pages [21] -->
m

<!-- b005897 | furniture | pages [21] -->
m

<!-- b005898 | furniture | pages [21] -->
m

<!-- b005899 | furniture | pages [21] -->
m

<!-- b005900 | furniture | pages [21] -->
m

<!-- b005901 | furniture | pages [21] -->
m

<!-- b005902 | furniture | pages [21] -->
m

<!-- b005903 | furniture | pages [21] -->
m

<!-- b005904 | furniture | pages [21] -->
m

<!-- b005905 | furniture | pages [21] -->
m

<!-- b005906 | furniture | pages [21] -->
m

<!-- b005907 | furniture | pages [21] -->
m

<!-- b005908 | furniture | pages [21] -->
m

<!-- b005909 | furniture | pages [21] -->
m

<!-- b005910 | furniture | pages [21] -->
m

<!-- b005911 | furniture | pages [21] -->
m

<!-- b005912 | furniture | pages [21] -->
m

<!-- b005913 | furniture | pages [21] -->
m

<!-- b005914 | furniture | pages [21] -->
m

<!-- b005915 | furniture | pages [21] -->
m

<!-- b005916 | furniture | pages [21] -->
m

<!-- b005917 | furniture | pages [21] -->
m

<!-- b005918 | furniture | pages [21] -->
m

<!-- b005919 | furniture | pages [21] -->
m

<!-- b005920 | furniture | pages [21] -->
m

<!-- b005921 | furniture | pages [21] -->
m

<!-- b005922 | furniture | pages [21] -->
m

<!-- b005923 | furniture | pages [21] -->
m

<!-- b005924 | furniture | pages [21] -->
m

<!-- b005925 | furniture | pages [21] -->
m

<!-- b005926 | furniture | pages [21] -->
m

<!-- b005927 | furniture | pages [21] -->
m

<!-- b005928 | furniture | pages [21] -->
m

<!-- b005929 | furniture | pages [21] -->
m

<!-- b005930 | furniture | pages [21] -->
m

<!-- b005931 | furniture | pages [21] -->
m

<!-- b005932 | furniture | pages [21] -->
m

<!-- b005933 | furniture | pages [21] -->
m

<!-- b005934 | furniture | pages [21] -->
m

<!-- b005935 | furniture | pages [21] -->
m

<!-- b005936 | furniture | pages [21] -->
m

<!-- b005937 | furniture | pages [21] -->
m

<!-- b005938 | furniture | pages [21] -->
m

<!-- b005939 | furniture | pages [21] -->
m

<!-- b005940 | furniture | pages [21] -->
m

<!-- b005941 | furniture | pages [21] -->
m

<!-- b005942 | furniture | pages [21] -->
m

<!-- b005943 | furniture | pages [21] -->
m

<!-- b005944 | furniture | pages [21] -->
m

<!-- b005945 | furniture | pages [21] -->
m

<!-- b005946 | furniture | pages [21] -->
m

<!-- b005947 | furniture | pages [21] -->
m

<!-- b005948 | furniture | pages [21] -->
m

<!-- b005949 | furniture | pages [21] -->
m

<!-- b005950 | furniture | pages [21] -->
m

<!-- b005951 | furniture | pages [21] -->
m

<!-- b005952 | furniture | pages [21] -->
m

<!-- b005953 | prose | pages [21] -->
 

<!-- b005954 | prose | pages [21] -->
+ ω2E(t) + ω3C(t) −ω4τ(t) (22)

<!-- b005955 | furniture | pages [22] -->
Team # 2504448

<!-- b005956 | furniture | pages [22] -->
Page 22 of 25

<!-- b005957 | prose | pages [22] -->
In contrast to Juneau, Miami’s well-developed infrastructure reduces the role of gov- ernment expenditure, leading to a lower weight on infrastructure investments and a higher allocation towards cultural initiatives.

<!-- b005958 | prose | pages [22] -->
The results are shown in Table 5.

<!-- b005959 | prose | pages [22] -->
Promotion of Attractions with Fewer Tourists 5.3

<!-- b005960 | prose | pages [22] -->
To achieve a better balance in tourist distribution and promote under-visited locations, our model incorporates the following key strategies that align with sustainable tourism objectives:

<!-- b005961 | prose | pages [22] -->
• Dynamic Visitor Caps Our model dynamically adjusts visitor capacity based on environmental and infras- tructure constraints. We could increase limits for under-visited sites like rainforest trails and cultural heritage locations, so that a balanced tourist distribution can be achieved. The optimization process ensures that environmental degradation is min- imized while maintaining economic benefits.

<!-- b005962 | prose | pages [22] -->
• Tax Differentiation To encourage tourists to explore less-crowded destinations, the model applies a dif- ferentiated tax scheme. Popular attractions are subject to higher tax rates, while under-visited areas benefit from lower taxes, making them more attractive to budget- conscious travelers. The tax revenue generated from high-demand attractions can be reinvested in infrastructure improvements for less-visited tourist destinations, ensuring long-term sustainability.

<!-- b005963 | prose | pages [22] -->
• Targeted Promotions Our model optimizes the allocation of promotional budgets to highlight the wonder of less-visited locations. Based on evidence and data, our model identifies areas with growth potential and designs marketing campaigns showcasing diverse attractions such as whale watching and rainforest hikes as viable alternatives to overcrowded sites. This approach enhances the visibility of these locations and engages more tourists.

<!-- b005964 | prose | pages [22] -->
6

<!-- b005965 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b005966 | prose | pages [22] -->
6.1

<!-- b005967 | heading | pages [22] -->
Strengths

<!-- b005968 | heading | pages [22] -->
• Comprehensive Framework: Our model integrates economic, environmental, and

<!-- b005969 | prose | pages [22] -->
social dimensions, providing a holistic approach to sustainable tourism manage- ment.

<!-- b005970 | heading | pages [22] -->
• Adaptability: Our model can be applied to different destinations, as demonstrated

<!-- b005971 | prose | pages [22] -->
in the Miami case study, ensuring its versatility across diverse contexts.

<!-- b005972 | prose | pages [22] -->
关注数学模型

<!-- b005973 | furniture | pages [22] -->
2

<!-- b005974 | furniture | pages [22] -->
MATHmodels

<!-- b005975 | furniture | pages [22] -->
获取更多资讯

<!-- b005976 | furniture | pages [23] -->
Team # 2504448

<!-- b005977 | furniture | pages [23] -->
Page 23 of 25

<!-- b005978 | prose | pages [23] -->
• Dynamic Decision-Making: The use of dynamic programming allows for adaptive policy measures, such as varying tax rates and expenditure allocations, to respond

<!-- b005979 | prose | pages [23] -->
微信公众号：数学模型

<!-- b005980 | prose | pages [23] -->
to changing conditions over time.

<!-- b005981 | heading | pages [23] -->
• Quantifiable Insights: Our model provides measurable outcomes for decision-making

<!-- b005982 | prose | pages [23] -->
by including key metrics like environmental index and resident satisfaction.

<!-- b005983 | heading | pages [23] -->
• Emphasis on Sustainability: Our model prioritizes long-term ecological preserva-

<!-- b005984 | prose | pages [23] -->
tion and community well-being, aligning with global sustainable tourism goals.

<!-- b005985 | prose | pages [23] -->
6.2

<!-- b005986 | heading | pages [23] -->
Weaknesses

<!-- b005987 | prose | pages [23] -->
微信号：MATHmodels

<!-- b005988 | prose | pages [23] -->
• Data Dependency: The accuracy of the model depends heavily on the availability and reliability of historical and real-time data, which may not always be comprehen- sive or consistent. The tourism data is only available for the last five years.

<!-- b005989 | prose | pages [23] -->
• Simplifying Assumptions: Certain aspects, such as the constant recovery rate of the environment and fixed sensitivity parameters, may oversimplify complex human- environment interactions.

<!-- b005990 | heading | pages [23] -->
• Limited Stakeholder Representation: The model does not explicitly account for

<!-- b005991 | prose | pages [23] -->
the diverse perspectives of stakeholders, such as local businesses or tourists, which could influence the outcomes.

<!-- b005992 | prose | pages [23] -->
• Computational Complexity: The dynamic programming approach, while power- ful, can become computationally intensive for more granular data or larger-scale applications.

<!-- b005993 | heading | pages [23] -->
References

<!-- b005994 | references | pages [23] -->
[1] Van der Borg, J., Costa, P., and Soriani, S. (2017). "Sustainable Tourism in Venice:

<!-- b005995 | references | pages [23] -->
Lessons for Other Fragile Cities." In Fragile and Resilient Cities on Water. Newcastle

<!-- b005996 | references | pages [23] -->
upon Tyne, UK: Cambridge Scholars Publishing.

<!-- b005997 | references | pages [23] -->
[2] Swart, W. W., C. E. Gearing, and Turgut Var. "A Dynamic Programming—Integer

<!-- b005998 | references | pages [23] -->
Programming Algorithm for Allocating Touristic Investments." The Tourist Review,

<!-- b005999 | references | pages [23] -->
27.2 (1972): 52-61.

<!-- b006000 | references | pages [23] -->
[3] Johnston, Robert J., and Timothy J. Tyrrell. "A Dynamic Model of Sustainable

<!-- b006001 | references | pages [23] -->
Tourism." Journal of Travel Research, 44.2 (2005): 124-134.

<!-- b006002 | references | pages [23] -->
[4] CBJ Tourism Survey (2023). "Tourism Survey Report 2023." City and Borough of

<!-- b006003 | references | pages [23] -->
https://juneau.org/wp-content/uploads/2023/12/

<!-- b006004 | references | pages [23] -->
Juneau. Available online:

<!-- b006005 | references | pages [23] -->
CBJ-Tourism-Survey-2023-Report-12.11.23.pdf.

<!-- b006006 | references | pages [23] -->
[5] Alaska Climate Research Center. (2023). "Juneau Climate Trends and Data." Available

<!-- b006007 | references | pages [23] -->
https://acrc.alaska.edu/juneau-climate-report/index.html.

<!-- b006008 | references | pages [23] -->
online:

<!-- b006009 | furniture | pages [24] -->
Team # 2504448

<!-- b006010 | furniture | pages [24] -->
Page 24 of 25

<!-- b006011 | heading | pages [24] -->
Memo: Sustainable Tourism Recommendations for Juneau

<!-- b006012 | prose | pages [24] -->
8

<!-- b006013 | prose | pages [24] -->
To: Tourist Council of Juneau From: Team 2504448

<!-- b006014 | heading | pages [24] -->
Re: Sustainable Tourism Recommendations for Juneau

<!-- b006015 | prose | pages [24] -->
Date: January 28, 2025

<!-- b006016 | prose | pages [24] -->
In the memo, we want to provide the recommended measures to optimize sustainable tourism in Juneau based on the results of our model. After a comprehensive investigation of the local tourism development in the past years, we integrate economic, environmen- tal, and social objectives, hoping to provide actionable insights for policy decisions.

<!-- b006017 | heading | pages [24] -->
Predictions and Key Findings: Our multi-objective dynamic programming model gives

<!-- b006018 | prose | pages [24] -->
a plan for the goal of sustainability as well as the predictions of outcomes over the next five years:

<!-- b006019 | prose | pages [24] -->
• Optimized Tax Rate: The tax rate should follow a dynamic pattern, starting at 4.2% in Year 1, peaking at 5.0% in Year 3, and then declining to 3.2% by Year 5.

<!-- b006020 | prose | pages [24] -->
• Government Expenditures: A significant portion of revenue should be allocated to environmental protection. Infrastructure investments should gradually increase, while subsidies need to be a steady component supporting sustainable practices and reducing financial burdens on residents.

<!-- b006021 | prose | pages [24] -->
• Predicted Outcomes: In our prediction, the tourist volume stabilizes between 1.52 million and 1.68 million, reflecting the effectiveness of adaptive taxation and pro- motional efforts. Government revenue from tourism taxation ranges from $11.71 million to $16.6 million per year. The environmental index (a quantitative index computed in our model) improves significantly from 0.029 to 0.181. The score of resident satisfaction steadily increases from 0.882 to 0.917.

<!-- b006022 | prose | pages [24] -->
Policy Measures and Their Effects:

<!-- b006023 | prose | pages [24] -->
• Taxation and Revenue Allocation: Dynamic taxation ensures sustainable revenue while mitigating environmental and social impacts. Our model recommends priori- tizing environmental conservation and infrastructure development.

<!-- b006024 | prose | pages [24] -->
• Visitor Distribution: Visitor caps and targeted promotions encourage the visit of under-visited locations, reducing pressure on popular sites like Mendenhall Glacier.

<!-- b006025 | prose | pages [24] -->
• Community Engagement: Subsidies for local businesses and eco-friendly initiatives help reduce the financial burden on residents and encourage sustainable practices.

<!-- b006026 | heading | pages [24] -->
Recommendations: To optimize sustainable tourism in Juneau, we advise:

<!-- b006027 | prose | pages [24] -->
• Adaptive Policies: Maintain flexible tax rates and expenditure allocations, guided by real-time environmental and social data.

<!-- b006028 | prose | pages [24] -->
• Promotional Campaigns: Promote under-visited locations and off-peak seasons through

<!-- b006029 | prose | pages [24] -->
m

<!-- b006030 | prose | pages [24] -->
m

<!-- b006031 | prose | pages [24] -->
m

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
m

<!-- b006043 | prose | pages [24] -->
m

<!-- b006044 | prose | pages [24] -->
m

<!-- b006045 | prose | pages [24] -->
m

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
m

<!-- b006060 | prose | pages [24] -->
m

<!-- b006061 | prose | pages [24] -->
m

<!-- b006062 | prose | pages [24] -->
m

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
m

<!-- b006076 | prose | pages [24] -->
m

<!-- b006077 | prose | pages [24] -->
m

<!-- b006078 | prose | pages [24] -->
m

<!-- b006079 | prose | pages [24] -->
m

<!-- b006080 | prose | pages [24] -->
m

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
m

<!-- b006092 | prose | pages [24] -->
m

<!-- b006093 | prose | pages [24] -->
m

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
targeted marketing to distribute tourist dynamics more evenly throughout Juneau.

<!-- b006103 | prose | pages [24] -->
m

<!-- b006104 | prose | pages [24] -->
m

<!-- b006105 | prose | pages [24] -->
m

<!-- b006106 | prose | pages [24] -->
m

<!-- b006107 | prose | pages [24] -->
m

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
m

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
m

<!-- b006171 | prose | pages [24] -->
m

<!-- b006172 | prose | pages [24] -->
m

<!-- b006173 | prose | pages [24] -->
m

<!-- b006174 | prose | pages [24] -->
m

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
m

<!-- b006186 | prose | pages [24] -->
m

<!-- b006187 | prose | pages [24] -->
m

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
m

<!-- b006204 | prose | pages [24] -->
m

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
m

<!-- b006212 | prose | pages [24] -->
m

<!-- b006213 | prose | pages [24] -->
m

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
m

<!-- b006223 | prose | pages [24] -->
m

<!-- b006224 | prose | pages [24] -->
m

<!-- b006225 | prose | pages [24] -->
m

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
m

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
m

<!-- b006249 | prose | pages [24] -->
m

<!-- b006250 | prose | pages [24] -->
m

<!-- b006251 | prose | pages [24] -->
m

<!-- b006252 | prose | pages [24] -->
m

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
m

<!-- b006266 | prose | pages [24] -->
m

<!-- b006267 | prose | pages [24] -->
m

<!-- b006268 | prose | pages [24] -->
m

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
m

<!-- b006279 | prose | pages [24] -->
m

<!-- b006280 | prose | pages [24] -->
m

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
m

<!-- b006296 | prose | pages [24] -->
m

<!-- b006297 | prose | pages [24] -->
m

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
m

<!-- b006311 | prose | pages [24] -->
m

<!-- b006312 | prose | pages [24] -->
m

<!-- b006313 | prose | pages [24] -->
m

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
m

<!-- b006323 | prose | pages [24] -->
m

<!-- b006324 | prose | pages [24] -->
m

<!-- b006325 | prose | pages [24] -->
m

<!-- b006326 | prose | pages [24] -->
• Feedback Mechanisms: Regularly gather input from residents and visitors to refine

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
m

<!-- b006355 | prose | pages [24] -->
m

<!-- b006356 | prose | pages [24] -->
m

<!-- b006357 | prose | pages [24] -->
m

<!-- b006358 | prose | pages [24] -->
m

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
m

<!-- b006371 | prose | pages [24] -->
m

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
m

<!-- b006380 | prose | pages [24] -->
m

<!-- b006381 | prose | pages [24] -->
m

<!-- b006382 | prose | pages [24] -->
m

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
m

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
m

<!-- b006405 | prose | pages [24] -->
m

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
m

<!-- b006419 | prose | pages [24] -->
m

<!-- b006420 | prose | pages [24] -->
m

<!-- b006421 | prose | pages [24] -->
m

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
m

<!-- b006428 | prose | pages [24] -->
m

<!-- b006429 | prose | pages [24] -->
m

<!-- b006430 | prose | pages [24] -->
m

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
关注数学模型

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
m

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
policies and ensure alignment with sustainability goals.

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
m

<!-- b006481 | prose | pages [24] -->
m

<!-- b006482 | prose | pages [24] -->
m

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
m

<!-- b006495 | prose | pages [24] -->
m

<!-- b006496 | prose | pages [24] -->
m

<!-- b006497 | prose | pages [24] -->
m

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
m

<!-- b006514 | prose | pages [24] -->
m

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
m

<!-- b006525 | prose | pages [24] -->
m

<!-- b006526 | prose | pages [24] -->
m

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

<!-- b006534 | furniture | pages [24] -->
2

<!-- b006535 | furniture | pages [24] -->
m

<!-- b006536 | furniture | pages [24] -->
m

<!-- b006537 | furniture | pages [24] -->
m

<!-- b006538 | furniture | pages [24] -->
m

<!-- b006539 | furniture | pages [24] -->
m

<!-- b006540 | furniture | pages [24] -->
m

<!-- b006541 | furniture | pages [24] -->
m

<!-- b006542 | furniture | pages [24] -->
m

<!-- b006543 | furniture | pages [24] -->
m

<!-- b006544 | furniture | pages [24] -->
m

<!-- b006545 | furniture | pages [24] -->
m

<!-- b006546 | furniture | pages [24] -->
m

<!-- b006547 | furniture | pages [24] -->
m

<!-- b006548 | furniture | pages [24] -->
m

<!-- b006549 | furniture | pages [24] -->
m

<!-- b006550 | furniture | pages [24] -->
m

<!-- b006551 | furniture | pages [24] -->
m

<!-- b006552 | furniture | pages [24] -->
m

<!-- b006553 | furniture | pages [24] -->
m

<!-- b006554 | furniture | pages [24] -->
m

<!-- b006555 | furniture | pages [24] -->
m

<!-- b006556 | furniture | pages [24] -->
m

<!-- b006557 | furniture | pages [24] -->
m

<!-- b006558 | furniture | pages [24] -->
m

<!-- b006559 | furniture | pages [24] -->
m

<!-- b006560 | furniture | pages [24] -->
m

<!-- b006561 | furniture | pages [24] -->
m

<!-- b006562 | furniture | pages [24] -->
m

<!-- b006563 | furniture | pages [24] -->
m

<!-- b006564 | furniture | pages [24] -->
m

<!-- b006565 | furniture | pages [24] -->
m

<!-- b006566 | furniture | pages [24] -->
m

<!-- b006567 | furniture | pages [24] -->
m

<!-- b006568 | furniture | pages [24] -->
m

<!-- b006569 | furniture | pages [24] -->
m

<!-- b006570 | furniture | pages [24] -->
m

<!-- b006571 | furniture | pages [24] -->
m

<!-- b006572 | furniture | pages [24] -->
m

<!-- b006573 | furniture | pages [24] -->
m

<!-- b006574 | furniture | pages [24] -->
m

<!-- b006575 | furniture | pages [24] -->
m

<!-- b006576 | furniture | pages [24] -->
m

<!-- b006577 | furniture | pages [24] -->
m

<!-- b006578 | furniture | pages [24] -->
m

<!-- b006579 | furniture | pages [24] -->
m

<!-- b006580 | furniture | pages [24] -->
m

<!-- b006581 | furniture | pages [24] -->
m

<!-- b006582 | furniture | pages [24] -->
m

<!-- b006583 | furniture | pages [24] -->
m

<!-- b006584 | furniture | pages [24] -->
m

<!-- b006585 | furniture | pages [24] -->
m

<!-- b006586 | furniture | pages [24] -->
m

<!-- b006587 | furniture | pages [24] -->
m

<!-- b006588 | furniture | pages [24] -->
m

<!-- b006589 | furniture | pages [24] -->
m

<!-- b006590 | furniture | pages [24] -->
m

<!-- b006591 | furniture | pages [24] -->
m

<!-- b006592 | furniture | pages [24] -->
m

<!-- b006593 | furniture | pages [24] -->
m

<!-- b006594 | furniture | pages [24] -->
m

<!-- b006595 | furniture | pages [24] -->
m

<!-- b006596 | furniture | pages [24] -->
m

<!-- b006597 | furniture | pages [24] -->
m

<!-- b006598 | furniture | pages [24] -->
m

<!-- b006599 | furniture | pages [24] -->
m

<!-- b006600 | furniture | pages [24] -->
m

<!-- b006601 | furniture | pages [24] -->
m

<!-- b006602 | furniture | pages [24] -->
m

<!-- b006603 | furniture | pages [24] -->
m

<!-- b006604 | furniture | pages [24] -->
m

<!-- b006605 | furniture | pages [24] -->
m

<!-- b006606 | furniture | pages [24] -->
m

<!-- b006607 | furniture | pages [24] -->
m

<!-- b006608 | furniture | pages [24] -->
m

<!-- b006609 | furniture | pages [24] -->
m

<!-- b006610 | furniture | pages [24] -->
m

<!-- b006611 | furniture | pages [24] -->
m

<!-- b006612 | furniture | pages [24] -->
m

<!-- b006613 | furniture | pages [24] -->
m

<!-- b006614 | furniture | pages [24] -->
m

<!-- b006615 | furniture | pages [24] -->
m

<!-- b006616 | furniture | pages [24] -->
m

<!-- b006617 | furniture | pages [24] -->
m

<!-- b006618 | furniture | pages [24] -->
m

<!-- b006619 | furniture | pages [24] -->
m

<!-- b006620 | furniture | pages [24] -->
m

<!-- b006621 | furniture | pages [24] -->
m

<!-- b006622 | furniture | pages [24] -->
m

<!-- b006623 | furniture | pages [24] -->
m

<!-- b006624 | furniture | pages [24] -->
m

<!-- b006625 | furniture | pages [24] -->
m

<!-- b006626 | furniture | pages [24] -->
m

<!-- b006627 | furniture | pages [24] -->
m

<!-- b006628 | furniture | pages [24] -->
m

<!-- b006629 | furniture | pages [24] -->
m

<!-- b006630 | furniture | pages [24] -->
m

<!-- b006631 | furniture | pages [24] -->
m

<!-- b006632 | furniture | pages [24] -->
m

<!-- b006633 | furniture | pages [24] -->
m

<!-- b006634 | furniture | pages [24] -->
m

<!-- b006635 | furniture | pages [24] -->
m

<!-- b006636 | furniture | pages [24] -->
m

<!-- b006637 | furniture | pages [24] -->
m

<!-- b006638 | furniture | pages [24] -->
m

<!-- b006639 | furniture | pages [24] -->
m

<!-- b006640 | furniture | pages [24] -->
m

<!-- b006641 | furniture | pages [24] -->
m

<!-- b006642 | furniture | pages [24] -->
m

<!-- b006643 | furniture | pages [24] -->
m

<!-- b006644 | furniture | pages [24] -->
MATHmodels

<!-- b006645 | furniture | pages [24] -->
获取更多资讯

<!-- b006646 | furniture | pages [24] -->
m

<!-- b006647 | furniture | pages [24] -->
m

<!-- b006648 | furniture | pages [24] -->
m

<!-- b006649 | furniture | pages [24] -->
m

<!-- b006650 | furniture | pages [24] -->
m

<!-- b006651 | furniture | pages [24] -->
m

<!-- b006652 | furniture | pages [24] -->
m

<!-- b006653 | furniture | pages [24] -->
m

<!-- b006654 | furniture | pages [24] -->
m

<!-- b006655 | furniture | pages [24] -->
m

<!-- b006656 | furniture | pages [24] -->
m

<!-- b006657 | furniture | pages [24] -->
m

<!-- b006658 | furniture | pages [24] -->
m

<!-- b006659 | furniture | pages [24] -->
m

<!-- b006660 | furniture | pages [24] -->
m

<!-- b006661 | furniture | pages [24] -->
m

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

<!-- b006723 | furniture | pages [25] -->
Team # 2504448

<!-- b006724 | furniture | pages [25] -->
Page 25 of 25

<!-- b006725 | prose | pages [25] -->
9

<!-- b006726 | heading | pages [25] -->
Report on use of AI

<!-- b006727 | heading | pages [25] -->
1. OpenAI Enie (Jan 27, 2025 version, Ernie 4.0)

<!-- b006728 | prose | pages [25] -->
Query1: What are the key factors of tourism in Juneau, Alaska?

<!-- b006729 | prose | pages [25] -->
微信公众号：数学模型

<!-- b006730 | prose | pages [25] -->
Output: Tourism in Juneau, Alaska, is influenced by several key factors: 1. Cruise Ship Tourism: Juneau is a popular stop for Alaska cruise lines, which oper- ate primarily during the summer months (May to September). The number of cruise ship arrivals and the season’s schedule significantly impact the flow of tourists. 2. Natural Attractions: Juneau’s breathtaking natural landscapes, such as the Menden- hall Glacier, Tracy Arm Fjord, and Mount Roberts, draw visitors. Accessibility and conditions of these attractions can influence tourism. 3. Wildlife Viewing: Opportunities to see wildlife, including whales, bears, bald ea- gles, and seals, are a major draw. Seasonal wildlife patterns and tour availability play a crucial role.

<!-- b006731 | prose | pages [25] -->
微信号：MATHmodels

<!-- b006732 | heading | pages [25] -->
2. OpenAI Enie (Jan 27, 2025 version, Ernie 4.0)

<!-- b006733 | prose | pages [25] -->
Query2: What are the key differences between Juneau tourism and Miami tourism? Output: Key Differences Between Juneau and Miami Tourism:

<!-- b006734 | prose | pages [25] -->
1. Climate and Geography: Juneau features cool, rainy weather with glaciers and wilderness, while Miami offers tropical weather, beaches, and urban attractions. 2. Primary Activities: Juneau focuses on glacier exploration, wildlife viewing, and outdoor adventures. Miami emphasizes beach activities, nightlife, and cultural im- mersion. 3. Tourism Seasons: Juneau’s peak season is summer (May–September), whereas Miami attracts tourists year-round, with peaks in winter and spring.

<!-- b006735 | heading | pages [25] -->
3. OpenAI Enie (Jan 27, 2025 version, Ernie 4.0)

<!-- b006736 | heading | pages [25] -->
Query3: How to model government expenditure in a tourism destination using dy-

<!-- b006737 | prose | pages [25] -->
namic programming?

<!-- b006738 | heading | pages [25] -->
Output: Model government expenditure in a tourism destination using dynamic

<!-- b006739 | prose | pages [25] -->
programming by: State: Define the state as the current period, available budget, and tourism infras- tructure status. Decision: Specify spending options for each period (e.g., infrastructure, marketing, or conservation). Transition: Model how spending decisions affect tourism revenue, infrastructure quality, and future states. Reward: Define the objective, such as maximizing long-term revenue or tourist sat- isfaction. Recursion: Use the Bellman equation to optimize spending decisions over time, con- sidering future rewards.

<!-- b006740 | prose | pages [25] -->
m

<!-- b006741 | prose | pages [25] -->
m

<!-- b006742 | prose | pages [25] -->
m

<!-- b006743 | prose | pages [25] -->
m

<!-- b006744 | prose | pages [25] -->
m

<!-- b006745 | prose | pages [25] -->
m

<!-- b006746 | prose | pages [25] -->
m

<!-- b006747 | prose | pages [25] -->
m

<!-- b006748 | prose | pages [25] -->
m

<!-- b006749 | prose | pages [25] -->
m

<!-- b006750 | prose | pages [25] -->
m

<!-- b006751 | prose | pages [25] -->
m

<!-- b006752 | prose | pages [25] -->
m

<!-- b006753 | prose | pages [25] -->
m

<!-- b006754 | prose | pages [25] -->
m

<!-- b006755 | prose | pages [25] -->
m

<!-- b006756 | prose | pages [25] -->
m

<!-- b006757 | prose | pages [25] -->
m

<!-- b006758 | prose | pages [25] -->
m

<!-- b006759 | prose | pages [25] -->
m

<!-- b006760 | prose | pages [25] -->
m

<!-- b006761 | prose | pages [25] -->
m

<!-- b006762 | prose | pages [25] -->
m

<!-- b006763 | prose | pages [25] -->
m

<!-- b006764 | prose | pages [25] -->
m

<!-- b006765 | prose | pages [25] -->
m

<!-- b006766 | prose | pages [25] -->
m

<!-- b006767 | prose | pages [25] -->
m

<!-- b006768 | prose | pages [25] -->
m

<!-- b006769 | prose | pages [25] -->
m

<!-- b006770 | prose | pages [25] -->
m

<!-- b006771 | prose | pages [25] -->
m

<!-- b006772 | prose | pages [25] -->
m

<!-- b006773 | prose | pages [25] -->
m

<!-- b006774 | prose | pages [25] -->
m

<!-- b006775 | prose | pages [25] -->
m

<!-- b006776 | prose | pages [25] -->
m

<!-- b006777 | prose | pages [25] -->
m

<!-- b006778 | prose | pages [25] -->
m

<!-- b006779 | prose | pages [25] -->
m

<!-- b006780 | prose | pages [25] -->
m

<!-- b006781 | prose | pages [25] -->
m

<!-- b006782 | prose | pages [25] -->
m

<!-- b006783 | prose | pages [25] -->
m

<!-- b006784 | prose | pages [25] -->
m

<!-- b006785 | prose | pages [25] -->
m

<!-- b006786 | prose | pages [25] -->
m

<!-- b006787 | prose | pages [25] -->
m

<!-- b006788 | prose | pages [25] -->
m

<!-- b006789 | prose | pages [25] -->
m

<!-- b006790 | prose | pages [25] -->
m

<!-- b006791 | prose | pages [25] -->
m

<!-- b006792 | prose | pages [25] -->
m

<!-- b006793 | prose | pages [25] -->
m

<!-- b006794 | prose | pages [25] -->
m

<!-- b006795 | prose | pages [25] -->
m

<!-- b006796 | prose | pages [25] -->
m

<!-- b006797 | prose | pages [25] -->
m

<!-- b006798 | prose | pages [25] -->
m

<!-- b006799 | prose | pages [25] -->
m

<!-- b006800 | prose | pages [25] -->
m

<!-- b006801 | prose | pages [25] -->
m

<!-- b006802 | prose | pages [25] -->
m

<!-- b006803 | prose | pages [25] -->
m

<!-- b006804 | prose | pages [25] -->
m

<!-- b006805 | prose | pages [25] -->
m

<!-- b006806 | prose | pages [25] -->
m

<!-- b006807 | prose | pages [25] -->
m

<!-- b006808 | prose | pages [25] -->
m

<!-- b006809 | prose | pages [25] -->
m

<!-- b006810 | prose | pages [25] -->
m

<!-- b006811 | prose | pages [25] -->
m

<!-- b006812 | prose | pages [25] -->
m

<!-- b006813 | prose | pages [25] -->
m

<!-- b006814 | prose | pages [25] -->
m

<!-- b006815 | prose | pages [25] -->
m

<!-- b006816 | prose | pages [25] -->
m

<!-- b006817 | prose | pages [25] -->
m

<!-- b006818 | prose | pages [25] -->
m

<!-- b006819 | prose | pages [25] -->
m

<!-- b006820 | prose | pages [25] -->
m

<!-- b006821 | prose | pages [25] -->
m

<!-- b006822 | prose | pages [25] -->
m

<!-- b006823 | prose | pages [25] -->
m

<!-- b006824 | prose | pages [25] -->
m

<!-- b006825 | prose | pages [25] -->
m

<!-- b006826 | prose | pages [25] -->
m

<!-- b006827 | prose | pages [25] -->
m

<!-- b006828 | prose | pages [25] -->
m

<!-- b006829 | prose | pages [25] -->
m

<!-- b006830 | prose | pages [25] -->
m

<!-- b006831 | prose | pages [25] -->
m

<!-- b006832 | prose | pages [25] -->
m

<!-- b006833 | prose | pages [25] -->
m

<!-- b006834 | prose | pages [25] -->
m

<!-- b006835 | prose | pages [25] -->
m

<!-- b006836 | prose | pages [25] -->
m

<!-- b006837 | prose | pages [25] -->
m

<!-- b006838 | prose | pages [25] -->
m

<!-- b006839 | prose | pages [25] -->
m

<!-- b006840 | prose | pages [25] -->
m

<!-- b006841 | prose | pages [25] -->
m

<!-- b006842 | prose | pages [25] -->
m

<!-- b006843 | prose | pages [25] -->
m

<!-- b006844 | prose | pages [25] -->
m

<!-- b006845 | prose | pages [25] -->
m

<!-- b006846 | prose | pages [25] -->
m

<!-- b006847 | prose | pages [25] -->
m

<!-- b006848 | prose | pages [25] -->
m

<!-- b006849 | prose | pages [25] -->
m

<!-- b006850 | prose | pages [25] -->
m

<!-- b006851 | prose | pages [25] -->
m

<!-- b006852 | prose | pages [25] -->
m

<!-- b006853 | prose | pages [25] -->
m

<!-- b006854 | prose | pages [25] -->
m

<!-- b006855 | prose | pages [25] -->
m

<!-- b006856 | prose | pages [25] -->
m

<!-- b006857 | prose | pages [25] -->
m

<!-- b006858 | prose | pages [25] -->
m

<!-- b006859 | prose | pages [25] -->
m

<!-- b006860 | prose | pages [25] -->
m

<!-- b006861 | prose | pages [25] -->
m

<!-- b006862 | prose | pages [25] -->
m

<!-- b006863 | prose | pages [25] -->
m

<!-- b006864 | prose | pages [25] -->
m

<!-- b006865 | prose | pages [25] -->
m

<!-- b006866 | prose | pages [25] -->
m

<!-- b006867 | prose | pages [25] -->
m

<!-- b006868 | prose | pages [25] -->
m

<!-- b006869 | prose | pages [25] -->
m

<!-- b006870 | prose | pages [25] -->
m

<!-- b006871 | prose | pages [25] -->
m

<!-- b006872 | prose | pages [25] -->
m

<!-- b006873 | prose | pages [25] -->
m

<!-- b006874 | prose | pages [25] -->
m

<!-- b006875 | prose | pages [25] -->
m

<!-- b006876 | prose | pages [25] -->
m

<!-- b006877 | prose | pages [25] -->
m

<!-- b006878 | prose | pages [25] -->
m

<!-- b006879 | prose | pages [25] -->
m

<!-- b006880 | prose | pages [25] -->
m

<!-- b006881 | prose | pages [25] -->
m

<!-- b006882 | prose | pages [25] -->
m

<!-- b006883 | prose | pages [25] -->
m

<!-- b006884 | prose | pages [25] -->
m

<!-- b006885 | prose | pages [25] -->
m

<!-- b006886 | prose | pages [25] -->
m

<!-- b006887 | prose | pages [25] -->
m

<!-- b006888 | prose | pages [25] -->
m

<!-- b006889 | prose | pages [25] -->
m

<!-- b006890 | prose | pages [25] -->
m

<!-- b006891 | prose | pages [25] -->
m

<!-- b006892 | prose | pages [25] -->
m

<!-- b006893 | prose | pages [25] -->
m

<!-- b006894 | prose | pages [25] -->
m

<!-- b006895 | prose | pages [25] -->
m

<!-- b006896 | prose | pages [25] -->
m

<!-- b006897 | prose | pages [25] -->
m

<!-- b006898 | prose | pages [25] -->
m

<!-- b006899 | prose | pages [25] -->
m

<!-- b006900 | prose | pages [25] -->
m

<!-- b006901 | prose | pages [25] -->
m

<!-- b006902 | prose | pages [25] -->
m

<!-- b006903 | prose | pages [25] -->
m

<!-- b006904 | prose | pages [25] -->
m

<!-- b006905 | prose | pages [25] -->
m

<!-- b006906 | prose | pages [25] -->
m

<!-- b006907 | prose | pages [25] -->
m

<!-- b006908 | prose | pages [25] -->
m

<!-- b006909 | prose | pages [25] -->
m

<!-- b006910 | prose | pages [25] -->
m

<!-- b006911 | prose | pages [25] -->
m

<!-- b006912 | prose | pages [25] -->
m

<!-- b006913 | prose | pages [25] -->
m

<!-- b006914 | prose | pages [25] -->
m

<!-- b006915 | prose | pages [25] -->
m

<!-- b006916 | prose | pages [25] -->
m

<!-- b006917 | prose | pages [25] -->
m

<!-- b006918 | prose | pages [25] -->
m

<!-- b006919 | prose | pages [25] -->
m

<!-- b006920 | prose | pages [25] -->
m

<!-- b006921 | prose | pages [25] -->
m

<!-- b006922 | prose | pages [25] -->
m

<!-- b006923 | prose | pages [25] -->
m

<!-- b006924 | prose | pages [25] -->
m

<!-- b006925 | prose | pages [25] -->
m

<!-- b006926 | prose | pages [25] -->
m

<!-- b006927 | prose | pages [25] -->
m

<!-- b006928 | prose | pages [25] -->
m

<!-- b006929 | prose | pages [25] -->
m

<!-- b006930 | prose | pages [25] -->
m

<!-- b006931 | prose | pages [25] -->
m

<!-- b006932 | prose | pages [25] -->
m

<!-- b006933 | prose | pages [25] -->
m

<!-- b006934 | prose | pages [25] -->
m

<!-- b006935 | prose | pages [25] -->
m

<!-- b006936 | prose | pages [25] -->
m

<!-- b006937 | prose | pages [25] -->
m

<!-- b006938 | prose | pages [25] -->
m

<!-- b006939 | prose | pages [25] -->
m

<!-- b006940 | prose | pages [25] -->
m

<!-- b006941 | prose | pages [25] -->
m

<!-- b006942 | prose | pages [25] -->
m

<!-- b006943 | prose | pages [25] -->
m

<!-- b006944 | prose | pages [25] -->
m

<!-- b006945 | prose | pages [25] -->
m

<!-- b006946 | prose | pages [25] -->
m

<!-- b006947 | prose | pages [25] -->
m

<!-- b006948 | prose | pages [25] -->
m

<!-- b006949 | prose | pages [25] -->
m

<!-- b006950 | prose | pages [25] -->
m

<!-- b006951 | prose | pages [25] -->
m

<!-- b006952 | prose | pages [25] -->
m

<!-- b006953 | prose | pages [25] -->
m

<!-- b006954 | prose | pages [25] -->
m

<!-- b006955 | prose | pages [25] -->
m

<!-- b006956 | prose | pages [25] -->
m

<!-- b006957 | prose | pages [25] -->
m

<!-- b006958 | prose | pages [25] -->
m

<!-- b006959 | prose | pages [25] -->
m

<!-- b006960 | prose | pages [25] -->
m

<!-- b006961 | prose | pages [25] -->
m

<!-- b006962 | prose | pages [25] -->
m

<!-- b006963 | prose | pages [25] -->
m

<!-- b006964 | prose | pages [25] -->
m

<!-- b006965 | prose | pages [25] -->
m

<!-- b006966 | prose | pages [25] -->
m

<!-- b006967 | prose | pages [25] -->
m

<!-- b006968 | prose | pages [25] -->
m

<!-- b006969 | prose | pages [25] -->
m

<!-- b006970 | prose | pages [25] -->
m

<!-- b006971 | prose | pages [25] -->
m

<!-- b006972 | prose | pages [25] -->
m

<!-- b006973 | prose | pages [25] -->
m

<!-- b006974 | prose | pages [25] -->
m

<!-- b006975 | prose | pages [25] -->
m

<!-- b006976 | prose | pages [25] -->
m

<!-- b006977 | prose | pages [25] -->
m

<!-- b006978 | prose | pages [25] -->
m

<!-- b006979 | prose | pages [25] -->
m

<!-- b006980 | prose | pages [25] -->
m

<!-- b006981 | prose | pages [25] -->
m

<!-- b006982 | prose | pages [25] -->
m

<!-- b006983 | prose | pages [25] -->
m

<!-- b006984 | prose | pages [25] -->
m

<!-- b006985 | prose | pages [25] -->
m

<!-- b006986 | prose | pages [25] -->
m

<!-- b006987 | prose | pages [25] -->
m

<!-- b006988 | prose | pages [25] -->
m

<!-- b006989 | prose | pages [25] -->
m

<!-- b006990 | prose | pages [25] -->
m

<!-- b006991 | prose | pages [25] -->
m

<!-- b006992 | prose | pages [25] -->
m

<!-- b006993 | prose | pages [25] -->
m

<!-- b006994 | prose | pages [25] -->
m

<!-- b006995 | prose | pages [25] -->
m

<!-- b006996 | prose | pages [25] -->
m

<!-- b006997 | prose | pages [25] -->
m

<!-- b006998 | prose | pages [25] -->
m

<!-- b006999 | prose | pages [25] -->
m

<!-- b007000 | prose | pages [25] -->
m

<!-- b007001 | prose | pages [25] -->
m

<!-- b007002 | prose | pages [25] -->
m

<!-- b007003 | prose | pages [25] -->
m

<!-- b007004 | prose | pages [25] -->
m

<!-- b007005 | prose | pages [25] -->
m

<!-- b007006 | prose | pages [25] -->
m

<!-- b007007 | prose | pages [25] -->
m

<!-- b007008 | prose | pages [25] -->
m

<!-- b007009 | prose | pages [25] -->
m

<!-- b007010 | prose | pages [25] -->
m

<!-- b007011 | prose | pages [25] -->
m

<!-- b007012 | prose | pages [25] -->
m

<!-- b007013 | prose | pages [25] -->
m

<!-- b007014 | prose | pages [25] -->
m

<!-- b007015 | prose | pages [25] -->
m

<!-- b007016 | prose | pages [25] -->
m

<!-- b007017 | prose | pages [25] -->
m

<!-- b007018 | prose | pages [25] -->
m

<!-- b007019 | prose | pages [25] -->
m

<!-- b007020 | prose | pages [25] -->
m

<!-- b007021 | prose | pages [25] -->
m

<!-- b007022 | prose | pages [25] -->
m

<!-- b007023 | prose | pages [25] -->
m

<!-- b007024 | furniture | pages [25] -->
m

<!-- b007025 | furniture | pages [25] -->
m

<!-- b007026 | furniture | pages [25] -->
m

<!-- b007027 | furniture | pages [25] -->
m

<!-- b007028 | furniture | pages [25] -->
m

<!-- b007029 | furniture | pages [25] -->
m

<!-- b007030 | furniture | pages [25] -->
m

<!-- b007031 | furniture | pages [25] -->
m

<!-- b007032 | furniture | pages [25] -->
m

<!-- b007033 | furniture | pages [25] -->
m

<!-- b007034 | furniture | pages [25] -->
m

<!-- b007035 | furniture | pages [25] -->
m

<!-- b007036 | furniture | pages [25] -->
m

<!-- b007037 | furniture | pages [25] -->
m

<!-- b007038 | furniture | pages [25] -->
m

<!-- b007039 | furniture | pages [25] -->
m

<!-- b007040 | furniture | pages [25] -->
m

<!-- b007041 | furniture | pages [25] -->
m

<!-- b007042 | furniture | pages [25] -->
m

<!-- b007043 | furniture | pages [25] -->
m

<!-- b007044 | furniture | pages [25] -->
m

<!-- b007045 | furniture | pages [25] -->
m

<!-- b007046 | furniture | pages [25] -->
m

<!-- b007047 | furniture | pages [25] -->
m

<!-- b007048 | furniture | pages [25] -->
m

<!-- b007049 | furniture | pages [25] -->
m

<!-- b007050 | furniture | pages [25] -->
m

<!-- b007051 | furniture | pages [25] -->
m

<!-- b007052 | furniture | pages [25] -->
m

<!-- b007053 | furniture | pages [25] -->
m

<!-- b007054 | furniture | pages [25] -->
m

<!-- b007055 | furniture | pages [25] -->
m

<!-- b007056 | furniture | pages [25] -->
m

<!-- b007057 | furniture | pages [25] -->
m

<!-- b007058 | furniture | pages [25] -->
m

<!-- b007059 | furniture | pages [25] -->
m

<!-- b007060 | furniture | pages [25] -->
m

<!-- b007061 | furniture | pages [25] -->
m

<!-- b007062 | furniture | pages [25] -->
m

<!-- b007063 | furniture | pages [25] -->
m

<!-- b007064 | furniture | pages [25] -->
m

<!-- b007065 | furniture | pages [25] -->
m

<!-- b007066 | furniture | pages [25] -->
m

<!-- b007067 | furniture | pages [25] -->
m

<!-- b007068 | furniture | pages [25] -->
m

<!-- b007069 | furniture | pages [25] -->
m

<!-- b007070 | furniture | pages [25] -->
m

<!-- b007071 | furniture | pages [25] -->
m

<!-- b007072 | furniture | pages [25] -->
m

<!-- b007073 | furniture | pages [25] -->
m

<!-- b007074 | furniture | pages [25] -->
m

<!-- b007075 | furniture | pages [25] -->
m

<!-- b007076 | furniture | pages [25] -->
m

<!-- b007077 | furniture | pages [25] -->
m

<!-- b007078 | furniture | pages [25] -->
m

<!-- b007079 | furniture | pages [25] -->
m

<!-- b007080 | furniture | pages [25] -->
m

<!-- b007081 | furniture | pages [25] -->
m

<!-- b007082 | furniture | pages [25] -->
m

<!-- b007083 | furniture | pages [25] -->
m

<!-- b007084 | furniture | pages [25] -->
m

<!-- b007085 | furniture | pages [25] -->
m

<!-- b007086 | furniture | pages [25] -->
m

<!-- b007087 | furniture | pages [25] -->
m

<!-- b007088 | furniture | pages [25] -->
m

<!-- b007089 | furniture | pages [25] -->
m

<!-- b007090 | furniture | pages [25] -->
m

<!-- b007091 | furniture | pages [25] -->
m

<!-- b007092 | furniture | pages [25] -->
m

<!-- b007093 | furniture | pages [25] -->
m

<!-- b007094 | furniture | pages [25] -->
m

<!-- b007095 | furniture | pages [25] -->
m

<!-- b007096 | furniture | pages [25] -->
m

<!-- b007097 | furniture | pages [25] -->
m

<!-- b007098 | furniture | pages [25] -->
m

<!-- b007099 | furniture | pages [25] -->
m

<!-- b007100 | furniture | pages [25] -->
m

<!-- b007101 | furniture | pages [25] -->
m

<!-- b007102 | furniture | pages [25] -->
m

<!-- b007103 | furniture | pages [25] -->
m

<!-- b007104 | furniture | pages [25] -->
m

<!-- b007105 | furniture | pages [25] -->
m

<!-- b007106 | furniture | pages [25] -->
m

<!-- b007107 | furniture | pages [25] -->
m

<!-- b007108 | furniture | pages [25] -->
m

<!-- b007109 | furniture | pages [25] -->
m

<!-- b007110 | furniture | pages [25] -->
m

<!-- b007111 | furniture | pages [25] -->
m

<!-- b007112 | furniture | pages [25] -->
m

<!-- b007113 | furniture | pages [25] -->
m

<!-- b007114 | furniture | pages [25] -->
m

<!-- b007115 | furniture | pages [25] -->
m

<!-- b007116 | furniture | pages [25] -->
m

<!-- b007117 | furniture | pages [25] -->
m

<!-- b007118 | furniture | pages [25] -->
m

<!-- b007119 | furniture | pages [25] -->
m

<!-- b007120 | furniture | pages [25] -->
m

<!-- b007121 | furniture | pages [25] -->
m

<!-- b007122 | furniture | pages [25] -->
m

<!-- b007123 | furniture | pages [25] -->
m

<!-- b007124 | furniture | pages [25] -->
m

<!-- b007125 | furniture | pages [25] -->
m

<!-- b007126 | furniture | pages [25] -->
m

<!-- b007127 | furniture | pages [25] -->
m

<!-- b007128 | furniture | pages [25] -->
m

<!-- b007129 | furniture | pages [25] -->
m

<!-- b007130 | furniture | pages [25] -->
m

<!-- b007131 | furniture | pages [25] -->
m

<!-- b007132 | furniture | pages [25] -->
m

<!-- b007133 | furniture | pages [25] -->
m

<!-- b007134 | furniture | pages [25] -->
m

<!-- b007135 | furniture | pages [25] -->
m

<!-- b007136 | furniture | pages [25] -->
m

<!-- b007137 | furniture | pages [25] -->
m

<!-- b007138 | furniture | pages [25] -->
m

<!-- b007139 | furniture | pages [25] -->
m

<!-- b007140 | furniture | pages [25] -->
m

<!-- b007141 | furniture | pages [25] -->
m

<!-- b007142 | furniture | pages [25] -->
m

<!-- b007143 | furniture | pages [25] -->
m

<!-- b007144 | furniture | pages [25] -->
m

<!-- b007145 | furniture | pages [25] -->
m

<!-- b007146 | furniture | pages [25] -->
m

<!-- b007147 | furniture | pages [25] -->
m

<!-- b007148 | furniture | pages [25] -->
m

<!-- b007149 | furniture | pages [25] -->
m

<!-- b007150 | furniture | pages [25] -->
m

<!-- b007151 | furniture | pages [25] -->
m

<!-- b007152 | furniture | pages [25] -->
m

<!-- b007153 | furniture | pages [25] -->
m

<!-- b007154 | furniture | pages [25] -->
m

<!-- b007155 | furniture | pages [25] -->
m

<!-- b007156 | furniture | pages [25] -->
m

<!-- b007157 | furniture | pages [25] -->
m

<!-- b007158 | furniture | pages [25] -->
m

<!-- b007159 | furniture | pages [25] -->
m

<!-- b007160 | furniture | pages [25] -->
m

<!-- b007161 | furniture | pages [25] -->
m

<!-- b007162 | furniture | pages [25] -->
m

<!-- b007163 | furniture | pages [25] -->
m

<!-- b007164 | furniture | pages [25] -->
m

<!-- b007165 | furniture | pages [25] -->
m

<!-- b007166 | furniture | pages [25] -->
m

<!-- b007167 | furniture | pages [25] -->
m

<!-- b007168 | furniture | pages [25] -->
m

<!-- b007169 | furniture | pages [25] -->
m

<!-- b007170 | furniture | pages [25] -->
m

<!-- b007171 | furniture | pages [25] -->
m

<!-- b007172 | furniture | pages [25] -->
m

<!-- b007173 | furniture | pages [25] -->
m

<!-- b007174 | furniture | pages [25] -->
m

<!-- b007175 | furniture | pages [25] -->
m

<!-- b007176 | furniture | pages [25] -->
m

<!-- b007177 | furniture | pages [25] -->
m

<!-- b007178 | furniture | pages [25] -->
m

<!-- b007179 | furniture | pages [25] -->
m

<!-- b007180 | furniture | pages [25] -->
m

<!-- b007181 | furniture | pages [25] -->
m

<!-- b007182 | furniture | pages [25] -->
m

<!-- b007183 | furniture | pages [25] -->
m

<!-- b007184 | furniture | pages [25] -->
m

<!-- b007185 | furniture | pages [25] -->
m

<!-- b007186 | furniture | pages [25] -->
m

<!-- b007187 | furniture | pages [25] -->
m

<!-- b007188 | furniture | pages [25] -->
m

<!-- b007189 | furniture | pages [25] -->
m

<!-- b007190 | furniture | pages [25] -->
m

<!-- b007191 | furniture | pages [25] -->
m

<!-- b007192 | furniture | pages [25] -->
m

<!-- b007193 | furniture | pages [25] -->
m

<!-- b007194 | furniture | pages [25] -->
m

<!-- b007195 | furniture | pages [25] -->
m

<!-- b007196 | furniture | pages [25] -->
m

<!-- b007197 | furniture | pages [25] -->
m

<!-- b007198 | furniture | pages [25] -->
m

<!-- b007199 | furniture | pages [25] -->
m

<!-- b007200 | furniture | pages [25] -->
m

<!-- b007201 | furniture | pages [25] -->
m

<!-- b007202 | furniture | pages [25] -->
m

<!-- b007203 | furniture | pages [25] -->
m

<!-- b007204 | furniture | pages [25] -->
m

<!-- b007205 | furniture | pages [25] -->
m

<!-- b007206 | furniture | pages [25] -->
m

<!-- b007207 | furniture | pages [25] -->
m

<!-- b007208 | furniture | pages [25] -->
m

<!-- b007209 | furniture | pages [25] -->
m

<!-- b007210 | furniture | pages [25] -->
m

<!-- b007211 | furniture | pages [25] -->
m

<!-- b007212 | furniture | pages [25] -->
m

<!-- b007213 | furniture | pages [25] -->
m

<!-- b007214 | furniture | pages [25] -->
m

<!-- b007215 | furniture | pages [25] -->
m

<!-- b007216 | furniture | pages [25] -->
m

<!-- b007217 | furniture | pages [25] -->
m

<!-- b007218 | furniture | pages [25] -->
m

<!-- b007219 | furniture | pages [25] -->
m

<!-- b007220 | furniture | pages [25] -->
m

<!-- b007221 | furniture | pages [25] -->
m

<!-- b007222 | furniture | pages [25] -->
m

<!-- b007223 | furniture | pages [25] -->
m

<!-- b007224 | furniture | pages [25] -->
m

<!-- b007225 | furniture | pages [25] -->
m

<!-- b007226 | furniture | pages [25] -->
m

<!-- b007227 | furniture | pages [25] -->
m

<!-- b007228 | furniture | pages [25] -->
m

<!-- b007229 | furniture | pages [25] -->
m

<!-- b007230 | furniture | pages [25] -->
m

<!-- b007231 | furniture | pages [25] -->
m

<!-- b007232 | furniture | pages [25] -->
m

<!-- b007233 | furniture | pages [25] -->
m

<!-- b007234 | furniture | pages [25] -->
m

<!-- b007235 | furniture | pages [25] -->
m

<!-- b007236 | furniture | pages [25] -->
m

<!-- b007237 | furniture | pages [25] -->
m

<!-- b007238 | furniture | pages [25] -->
m

<!-- b007239 | furniture | pages [25] -->
m

<!-- b007240 | furniture | pages [25] -->
m

<!-- b007241 | furniture | pages [25] -->
m

<!-- b007242 | furniture | pages [25] -->
m

<!-- b007243 | furniture | pages [25] -->
m

<!-- b007244 | furniture | pages [25] -->
m

<!-- b007245 | furniture | pages [25] -->
m

<!-- b007246 | furniture | pages [25] -->
m

<!-- b007247 | furniture | pages [25] -->
m

<!-- b007248 | furniture | pages [25] -->
m

<!-- b007249 | furniture | pages [25] -->
m

<!-- b007250 | furniture | pages [25] -->
m

<!-- b007251 | furniture | pages [25] -->
m

<!-- b007252 | furniture | pages [25] -->
m

<!-- b007253 | furniture | pages [25] -->
m

<!-- b007254 | furniture | pages [25] -->
m

<!-- b007255 | furniture | pages [25] -->
m

<!-- b007256 | furniture | pages [25] -->
m

<!-- b007257 | furniture | pages [25] -->
m

<!-- b007258 | furniture | pages [25] -->
m

<!-- b007259 | furniture | pages [25] -->
m

<!-- b007260 | furniture | pages [25] -->
m

<!-- b007261 | furniture | pages [25] -->
m

<!-- b007262 | furniture | pages [25] -->
m

<!-- b007263 | furniture | pages [25] -->
m

<!-- b007264 | furniture | pages [25] -->
m

<!-- b007265 | furniture | pages [25] -->
m

<!-- b007266 | furniture | pages [25] -->
m

<!-- b007267 | furniture | pages [25] -->
m

<!-- b007268 | furniture | pages [25] -->
m

<!-- b007269 | furniture | pages [25] -->
m

<!-- b007270 | furniture | pages [25] -->
m

<!-- b007271 | furniture | pages [25] -->
m

<!-- b007272 | furniture | pages [25] -->
m

<!-- b007273 | furniture | pages [25] -->
m

<!-- b007274 | furniture | pages [25] -->
m

<!-- b007275 | furniture | pages [25] -->
m

<!-- b007276 | furniture | pages [25] -->
m

<!-- b007277 | furniture | pages [25] -->
m

<!-- b007278 | furniture | pages [25] -->
m

<!-- b007279 | furniture | pages [25] -->
m

<!-- b007280 | furniture | pages [25] -->
m

<!-- b007281 | furniture | pages [25] -->
m

<!-- b007282 | furniture | pages [25] -->
m

<!-- b007283 | furniture | pages [25] -->
m

<!-- b007284 | furniture | pages [25] -->
m

<!-- b007285 | furniture | pages [25] -->
m

<!-- b007286 | furniture | pages [25] -->
m

<!-- b007287 | furniture | pages [25] -->
m

<!-- b007288 | furniture | pages [25] -->
m

<!-- b007289 | furniture | pages [25] -->
m

<!-- b007290 | furniture | pages [25] -->
m

<!-- b007291 | furniture | pages [25] -->
m

<!-- b007292 | furniture | pages [25] -->
m

<!-- b007293 | furniture | pages [25] -->
m

<!-- b007294 | furniture | pages [25] -->
m

<!-- b007295 | furniture | pages [25] -->
m

<!-- b007296 | furniture | pages [25] -->
m

<!-- b007297 | furniture | pages [25] -->
m

<!-- b007298 | furniture | pages [25] -->
m

<!-- b007299 | furniture | pages [25] -->
m

<!-- b007300 | furniture | pages [25] -->
m

<!-- b007301 | furniture | pages [25] -->
m

<!-- b007302 | furniture | pages [25] -->
m

<!-- b007303 | furniture | pages [25] -->
m

<!-- b007304 | furniture | pages [25] -->
m

<!-- b007305 | furniture | pages [25] -->
m

<!-- b007306 | furniture | pages [25] -->
m

<!-- b007307 | furniture | pages [25] -->
m

<!-- b007308 | furniture | pages [25] -->
m

<!-- b007309 | furniture | pages [25] -->
m

<!-- b007310 | furniture | pages [25] -->
m

<!-- b007311 | furniture | pages [25] -->
m

<!-- b007312 | furniture | pages [25] -->
m

<!-- b007313 | furniture | pages [25] -->
m

<!-- b007314 | furniture | pages [25] -->
m

<!-- b007315 | furniture | pages [25] -->
m

<!-- b007316 | furniture | pages [25] -->
m

<!-- b007317 | furniture | pages [25] -->
m

<!-- b007318 | furniture | pages [25] -->
m

<!-- b007319 | furniture | pages [25] -->
m

<!-- b007320 | furniture | pages [25] -->
m

<!-- b007321 | furniture | pages [25] -->
m

<!-- b007322 | furniture | pages [25] -->
m

<!-- b007323 | furniture | pages [25] -->
m

<!-- b007324 | furniture | pages [25] -->
m

<!-- b007325 | furniture | pages [25] -->
m

<!-- b007326 | furniture | pages [25] -->
m

<!-- b007327 | furniture | pages [25] -->
m

<!-- b007328 | furniture | pages [25] -->
m

<!-- b007329 | furniture | pages [25] -->
m

<!-- b007330 | furniture | pages [25] -->
m

<!-- b007331 | furniture | pages [25] -->
m

<!-- b007332 | furniture | pages [25] -->
m

<!-- b007333 | furniture | pages [25] -->
m

<!-- b007334 | furniture | pages [25] -->
m

<!-- b007335 | furniture | pages [25] -->
m

<!-- b007336 | furniture | pages [25] -->
m

<!-- b007337 | furniture | pages [25] -->
m

<!-- b007338 | furniture | pages [25] -->
m

<!-- b007339 | furniture | pages [25] -->
m

<!-- b007340 | furniture | pages [25] -->
m

<!-- b007341 | furniture | pages [25] -->
m

<!-- b007342 | furniture | pages [25] -->
m

<!-- b007343 | furniture | pages [25] -->
m

<!-- b007344 | furniture | pages [25] -->
m

<!-- b007345 | furniture | pages [25] -->
m

<!-- b007346 | furniture | pages [25] -->
m

<!-- b007347 | furniture | pages [25] -->
m

<!-- b007348 | furniture | pages [25] -->
m

<!-- b007349 | furniture | pages [25] -->
m

<!-- b007350 | furniture | pages [25] -->
m

<!-- b007351 | furniture | pages [25] -->
m

<!-- b007352 | furniture | pages [25] -->
m

<!-- b007353 | furniture | pages [25] -->
m

<!-- b007354 | furniture | pages [25] -->
m

<!-- b007355 | furniture | pages [25] -->
m

<!-- b007356 | furniture | pages [25] -->
m

<!-- b007357 | furniture | pages [25] -->
m

<!-- b007358 | furniture | pages [25] -->
m

<!-- b007359 | furniture | pages [25] -->
m

<!-- b007360 | furniture | pages [25] -->
m

<!-- b007361 | furniture | pages [25] -->
m

<!-- b007362 | furniture | pages [25] -->
m

<!-- b007363 | furniture | pages [25] -->
m

<!-- b007364 | furniture | pages [25] -->
m

<!-- b007365 | furniture | pages [25] -->
m

<!-- b007366 | furniture | pages [25] -->
m

<!-- b007367 | furniture | pages [25] -->
m

<!-- b007368 | furniture | pages [25] -->
m

<!-- b007369 | furniture | pages [25] -->
m

<!-- b007370 | furniture | pages [25] -->
m

<!-- b007371 | furniture | pages [25] -->
m

<!-- b007372 | furniture | pages [25] -->
m

<!-- b007373 | furniture | pages [25] -->
m

<!-- b007374 | furniture | pages [25] -->
m

<!-- b007375 | furniture | pages [25] -->
m

<!-- b007376 | furniture | pages [25] -->
m

<!-- b007377 | furniture | pages [25] -->
m

<!-- b007378 | furniture | pages [25] -->
m

<!-- b007379 | furniture | pages [25] -->
m

<!-- b007380 | furniture | pages [25] -->
m

<!-- b007381 | furniture | pages [25] -->
m

<!-- b007382 | furniture | pages [25] -->
m

<!-- b007383 | furniture | pages [25] -->
m

<!-- b007384 | furniture | pages [25] -->
m

<!-- b007385 | furniture | pages [25] -->
m

<!-- b007386 | furniture | pages [25] -->
m

<!-- b007387 | furniture | pages [25] -->
m

<!-- b007388 | furniture | pages [25] -->
m

<!-- b007389 | furniture | pages [25] -->
m

<!-- b007390 | furniture | pages [25] -->
m

<!-- b007391 | furniture | pages [25] -->
m

<!-- b007392 | furniture | pages [25] -->
m

<!-- b007393 | furniture | pages [25] -->
m

<!-- b007394 | furniture | pages [25] -->
m

<!-- b007395 | furniture | pages [25] -->
m

<!-- b007396 | furniture | pages [25] -->
m

<!-- b007397 | furniture | pages [25] -->
m

<!-- b007398 | furniture | pages [25] -->
m

<!-- b007399 | furniture | pages [25] -->
m

<!-- b007400 | furniture | pages [25] -->
m

<!-- b007401 | furniture | pages [25] -->
m

<!-- b007402 | furniture | pages [25] -->
m

<!-- b007403 | furniture | pages [25] -->
m

<!-- b007404 | furniture | pages [25] -->
m

<!-- b007405 | furniture | pages [25] -->
m

<!-- b007406 | furniture | pages [25] -->
m

<!-- b007407 | furniture | pages [25] -->
m

<!-- b007408 | furniture | pages [25] -->
m

<!-- b007409 | furniture | pages [25] -->
m

<!-- b007410 | furniture | pages [25] -->
m

<!-- b007411 | furniture | pages [25] -->
m

<!-- b007412 | furniture | pages [25] -->
m

<!-- b007413 | furniture | pages [25] -->
m

<!-- b007414 | furniture | pages [25] -->
m

<!-- b007415 | furniture | pages [25] -->
m

<!-- b007416 | furniture | pages [25] -->
m

<!-- b007417 | furniture | pages [25] -->
m

<!-- b007418 | furniture | pages [25] -->
m

<!-- b007419 | furniture | pages [25] -->
m

<!-- b007420 | furniture | pages [25] -->
m

<!-- b007421 | furniture | pages [25] -->
m

<!-- b007422 | furniture | pages [25] -->
m

<!-- b007423 | furniture | pages [25] -->
m

<!-- b007424 | furniture | pages [25] -->
m

<!-- b007425 | furniture | pages [25] -->
m

<!-- b007426 | furniture | pages [25] -->
m
