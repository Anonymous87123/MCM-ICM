# P-B-2025-2503268-228e0ec5

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
2503268

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Rebalancing Nature’s Scale: A Model to Tame Overtourism

<!-- b000009 | prose | pages [1] -->
Overtourism has become a global challenge, disrupting economic growth, environmental protec- tion, and residents’ quality of life. Rising tourist numbers have caused environmental damage, strained

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
infrastructure, and social tensions. Meanwhile, strict tourism limits can reduce local income and well- being. This dual challenge highlights the need for sustainable tourism strategies and data-driven models to optimize resources and maximize overall beneﬁts.

<!-- b000012 | prose | pages [1] -->
We selected Juneau, Alaska, as the representative city for modeling. Tourist numbers, Equilibrium Line Altitude (ELA), and hotel tax revenue were chosen as indicators for population, environment, and economy, respectively. Inspired by the Lotka-Volterra model, logistic population model, and SIS model, we developed the Sustainable Tourism Dynamics Model (STDM). This system uses ordinary diﬀerential equations to capture and visualize interactions among the three dimensions.

<!-- b000013 | prose | pages [1] -->
Intervention strategies include tax revenue allocation and policies, enacted by the government. Both consist of predeﬁned measures represented by constraint vectors, serving as impact factors in the

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
STDM and evaluation model. Static and dynamic constraints ensure the feasibility of these strategies.

<!-- b000016 | prose | pages [1] -->
According to some materials, we propose to three main factors (life of local residents, local en- vironmental protection, local economy and development of society), and four secondary indicators for each main factor combined with Analytic Hierarchy Process (AHP) to attain the comprehen- sive evaluation score. The values from the strategies and the dynamic system are input to the system, related to the score via various equations.

<!-- b000017 | prose | pages [1] -->
The model integrates all components into a uniﬁed system, where variables strongly connect the sub-models. Intervention strategies serve as inputs to the STDM, and its outputs, combined with strat- egy choices, determine the AHP-based evaluation model’s score. This score provides feedback to optimize strategies dynamically. Using this process, governments can adjust interventions and pre- dict their outcomes. For example, our model improves a score from 0.446 to 0.692 through targeted interventions.

<!-- b000018 | prose | pages [1] -->
We assessed our model’s sensitivity using two methods. The Morris method identiﬁed key factors through the µ-ω diagram, showing that the environmental degradation coeﬃcient (k2) and tourism rev- enue factor (k6) had the strongest direct eﬀects and moderate parameter interactions. Local sensitivity analysis revealed that the growth rate of tourist numbers (r1) and baseline economic growth rate (k5) were most sensitive, with partial derivatives of 792.18 and 575.2. In contrast, crowding perception (εc) and carbon footprint scaling (ϑCE) showed low sensitivities, at 0.017 and -34.5 . These results highlight the importance of high-impact parameters and conﬁrm the model’s stability under small changes.

<!-- b000019 | prose | pages [1] -->
We tested our model’s adaptability in Big Sur, a coastal destination facing overtourism. Glacier- related parameters were replaced with region-speciﬁc indicators, such as coastal landslide rates (HSur = 2.1 m/year) and visitor numbers (NSur = 1,532,000 annually). The recalibrated model improved the normalized sustainability score from 0.32773 to 0.73563 with optimized strategies. Key recommenda- tions included strengthening infrastructure resilience and promoting inland attractions to ease coastal pressure. These results highlight the model’s versatility in managing overtourism and supporting sus- tainable tourism. A memo to the Juneau Tourism Council outlines predictions, impacts of measures, and strategic recommendations for sustainable tourism in Juneau.

<!-- b000020 | keywords | pages [1] -->
Keywords: Overtourism, Sustainable Tourism Dynamic Model, Lotka-Volterra model, SIS model,

<!-- b000021 | prose | pages [1] -->
Intervention Strategies, Analytic Hierarchy Process, Sensitivity Analysis

<!-- b000022 | furniture | pages [3] -->
Team # 2503268

<!-- b000023 | furniture | pages [3] -->
Page 1 of 24

<!-- b000024 | heading | pages [3] -->
Contents

<!-- b000025 | contents | pages [3] -->
1

<!-- b000026 | heading | pages [3] -->
Introduction

<!-- b000027 | prose | pages [3] -->
2

<!-- b000028 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000029 | prose | pages [3] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 2

<!-- b000030 | heading | pages [3] -->
Assumptions and Justiﬁcations

<!-- b000031 | prose | pages [3] -->
3

<!-- b000032 | heading | pages [3] -->
Notations

<!-- b000033 | prose | pages [3] -->
4

<!-- b000034 | heading | pages [3] -->
Model Preparation

<!-- b000035 | prose | pages [3] -->
2 3 4 5 Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 5 Data Selection Explanation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 5

<!-- b000036 | heading | pages [3] -->
Model Design

<!-- b000037 | prose | pages [3] -->
5 6

<!-- b000038 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000039 | prose | pages [3] -->
Sustainable Tourism Dynamics Model (STDM) . . . . . . . . . . . . . . . . . . . . . 5.1 6 Glacier ELA Height Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 6 Tourist Number Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.2 7 Economic Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.3 7 Model Integration and Parameter Estimation . . . . . . . . . . . . . . . . . . . 5.1.4 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 Intervention Strategies 9 Intervention Impact on Models . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 Tax Revenue Allocation 10 Policies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 6

<!-- b000040 | heading | pages [3] -->
Evaluation Model

<!-- b000041 | prose | pages [3] -->
10 10 Indicators Determination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 10 Score Calculation Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 Values of Parameters 14 Weights Distribution Outcomes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.4 7 Analysis of Factors 8

<!-- b000042 | heading | pages [3] -->
Results and Discussion

<!-- b000043 | prose | pages [3] -->
9

<!-- b000044 | heading | pages [3] -->
Sensitivity Analysis

<!-- b000045 | prose | pages [3] -->
14 14 16 17 Qualitative analysis: Morris Method . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 17 Quantitative analysis: Local Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . 9.2

<!-- b000046 | heading | pages [3] -->
10 Reimagining Big Sur

<!-- b000047 | prose | pages [3] -->
18 19 10.1 Fundamental Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | prose | pages [3] -->
19 10.2 Model Validation and Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | heading | pages [3] -->
11 Strengths and Weaknesses

<!-- b000050 | prose | pages [3] -->
20 22 11.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | prose | pages [3] -->
22 11.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | heading | pages [3] -->
References

<!-- b000053 | references | pages [3] -->
m

<!-- b000054 | references | pages [3] -->
m

<!-- b000055 | references | pages [3] -->
m

<!-- b000056 | references | pages [3] -->
m

<!-- b000057 | references | pages [3] -->
m

<!-- b000058 | references | pages [3] -->
m

<!-- b000059 | references | pages [3] -->
m

<!-- b000060 | references | pages [3] -->
m

<!-- b000061 | references | pages [3] -->
m

<!-- b000062 | references | pages [3] -->
m

<!-- b000063 | references | pages [3] -->
m

<!-- b000064 | references | pages [3] -->
m

<!-- b000065 | references | pages [3] -->
m

<!-- b000066 | references | pages [3] -->
m

<!-- b000067 | references | pages [3] -->
m

<!-- b000068 | references | pages [3] -->
m

<!-- b000069 | references | pages [3] -->
m

<!-- b000070 | references | pages [3] -->
m

<!-- b000071 | references | pages [3] -->
m

<!-- b000072 | references | pages [3] -->
m

<!-- b000073 | references | pages [3] -->
m

<!-- b000074 | references | pages [3] -->
m

<!-- b000075 | references | pages [3] -->
m

<!-- b000076 | references | pages [3] -->
m

<!-- b000077 | references | pages [3] -->
m

<!-- b000078 | references | pages [3] -->
m

<!-- b000079 | references | pages [3] -->
m

<!-- b000080 | references | pages [3] -->
m

<!-- b000081 | references | pages [3] -->
m

<!-- b000082 | references | pages [3] -->
m

<!-- b000083 | references | pages [3] -->
m

<!-- b000084 | references | pages [3] -->
m

<!-- b000085 | references | pages [3] -->
m

<!-- b000086 | references | pages [3] -->
m

<!-- b000087 | references | pages [3] -->
m

<!-- b000088 | references | pages [3] -->
m

<!-- b000089 | references | pages [3] -->
m

<!-- b000090 | references | pages [3] -->
m

<!-- b000091 | references | pages [3] -->
m

<!-- b000092 | references | pages [3] -->
m

<!-- b000093 | references | pages [3] -->
m

<!-- b000094 | references | pages [3] -->
m

<!-- b000095 | references | pages [3] -->
m

<!-- b000096 | references | pages [3] -->
m

<!-- b000097 | references | pages [3] -->
m

<!-- b000098 | references | pages [3] -->
m

<!-- b000099 | references | pages [3] -->
m

<!-- b000100 | references | pages [3] -->
m

<!-- b000101 | references | pages [3] -->
m

<!-- b000102 | references | pages [3] -->
m

<!-- b000103 | references | pages [3] -->
m

<!-- b000104 | references | pages [3] -->
m

<!-- b000105 | references | pages [3] -->
m

<!-- b000106 | references | pages [3] -->
m

<!-- b000107 | references | pages [3] -->
m

<!-- b000108 | references | pages [3] -->
m

<!-- b000109 | references | pages [3] -->
m

<!-- b000110 | references | pages [3] -->
m

<!-- b000111 | references | pages [3] -->
m

<!-- b000112 | references | pages [3] -->
m

<!-- b000113 | references | pages [3] -->
m

<!-- b000114 | references | pages [3] -->
m

<!-- b000115 | references | pages [3] -->
m

<!-- b000116 | references | pages [3] -->
m

<!-- b000117 | references | pages [3] -->
m

<!-- b000118 | references | pages [3] -->
m

<!-- b000119 | references | pages [3] -->
m

<!-- b000120 | references | pages [3] -->
m

<!-- b000121 | references | pages [3] -->
m

<!-- b000122 | references | pages [3] -->
m

<!-- b000123 | references | pages [3] -->
m

<!-- b000124 | references | pages [3] -->
m

<!-- b000125 | references | pages [3] -->
m

<!-- b000126 | references | pages [3] -->
m

<!-- b000127 | references | pages [3] -->
m

<!-- b000128 | references | pages [3] -->
m

<!-- b000129 | references | pages [3] -->
m

<!-- b000130 | references | pages [3] -->
m

<!-- b000131 | references | pages [3] -->
m

<!-- b000132 | references | pages [3] -->
m

<!-- b000133 | references | pages [3] -->
m

<!-- b000134 | references | pages [3] -->
m

<!-- b000135 | references | pages [3] -->
m

<!-- b000136 | references | pages [3] -->
m

<!-- b000137 | references | pages [3] -->
m

<!-- b000138 | references | pages [3] -->
m

<!-- b000139 | references | pages [3] -->
m

<!-- b000140 | references | pages [3] -->
m

<!-- b000141 | references | pages [3] -->
m

<!-- b000142 | references | pages [3] -->
m

<!-- b000143 | references | pages [3] -->
m

<!-- b000144 | references | pages [3] -->
m

<!-- b000145 | references | pages [3] -->
m

<!-- b000146 | references | pages [3] -->
m

<!-- b000147 | references | pages [3] -->
m

<!-- b000148 | references | pages [3] -->
m

<!-- b000149 | references | pages [3] -->
m

<!-- b000150 | references | pages [3] -->
m

<!-- b000151 | references | pages [3] -->
m

<!-- b000152 | references | pages [3] -->
m

<!-- b000153 | references | pages [3] -->
m

<!-- b000154 | references | pages [3] -->
m

<!-- b000155 | references | pages [3] -->
m

<!-- b000156 | references | pages [3] -->
m

<!-- b000157 | references | pages [3] -->
m

<!-- b000158 | references | pages [3] -->
m

<!-- b000159 | references | pages [3] -->
m

<!-- b000160 | references | pages [3] -->
m

<!-- b000161 | references | pages [3] -->
m

<!-- b000162 | references | pages [3] -->
m

<!-- b000163 | references | pages [3] -->
m

<!-- b000164 | references | pages [3] -->
m

<!-- b000165 | references | pages [3] -->
m

<!-- b000166 | references | pages [3] -->
m

<!-- b000167 | references | pages [3] -->
m

<!-- b000168 | references | pages [3] -->
m

<!-- b000169 | references | pages [3] -->
m

<!-- b000170 | references | pages [3] -->
m

<!-- b000171 | references | pages [3] -->
m

<!-- b000172 | references | pages [3] -->
m

<!-- b000173 | references | pages [3] -->
m

<!-- b000174 | references | pages [3] -->
m

<!-- b000175 | references | pages [3] -->
m

<!-- b000176 | references | pages [3] -->
m

<!-- b000177 | references | pages [3] -->
m

<!-- b000178 | references | pages [3] -->
m

<!-- b000179 | references | pages [3] -->
m

<!-- b000180 | references | pages [3] -->
m

<!-- b000181 | references | pages [3] -->
m

<!-- b000182 | references | pages [3] -->
m

<!-- b000183 | references | pages [3] -->
m

<!-- b000184 | references | pages [3] -->
m

<!-- b000185 | references | pages [3] -->
m

<!-- b000186 | references | pages [3] -->
m

<!-- b000187 | references | pages [3] -->
m

<!-- b000188 | references | pages [3] -->
m

<!-- b000189 | references | pages [3] -->
m

<!-- b000190 | references | pages [3] -->
m

<!-- b000191 | references | pages [3] -->
m

<!-- b000192 | references | pages [3] -->
m

<!-- b000193 | references | pages [3] -->
m

<!-- b000194 | references | pages [3] -->
m

<!-- b000195 | references | pages [3] -->
m

<!-- b000196 | references | pages [3] -->
m

<!-- b000197 | references | pages [3] -->
m

<!-- b000198 | references | pages [3] -->
m

<!-- b000199 | references | pages [3] -->
m

<!-- b000200 | references | pages [3] -->
m

<!-- b000201 | references | pages [3] -->
m

<!-- b000202 | references | pages [3] -->
m

<!-- b000203 | references | pages [3] -->
m

<!-- b000204 | references | pages [3] -->
m

<!-- b000205 | references | pages [3] -->
m

<!-- b000206 | references | pages [3] -->
m

<!-- b000207 | references | pages [3] -->
m

<!-- b000208 | references | pages [3] -->
m

<!-- b000209 | references | pages [3] -->
m

<!-- b000210 | references | pages [3] -->
m

<!-- b000211 | references | pages [3] -->
m

<!-- b000212 | references | pages [3] -->
m

<!-- b000213 | references | pages [3] -->
m

<!-- b000214 | references | pages [3] -->
m

<!-- b000215 | references | pages [3] -->
m

<!-- b000216 | references | pages [3] -->
m

<!-- b000217 | references | pages [3] -->
m

<!-- b000218 | references | pages [3] -->
m

<!-- b000219 | references | pages [3] -->
m

<!-- b000220 | references | pages [3] -->
m

<!-- b000221 | references | pages [3] -->
m

<!-- b000222 | references | pages [3] -->
m

<!-- b000223 | references | pages [3] -->
m

<!-- b000224 | references | pages [3] -->
m

<!-- b000225 | references | pages [3] -->
m

<!-- b000226 | references | pages [3] -->
m

<!-- b000227 | references | pages [3] -->
m

<!-- b000228 | references | pages [3] -->
m

<!-- b000229 | references | pages [3] -->
m

<!-- b000230 | references | pages [3] -->
m

<!-- b000231 | references | pages [3] -->
m

<!-- b000232 | references | pages [3] -->
m

<!-- b000233 | references | pages [3] -->
m

<!-- b000234 | references | pages [3] -->
m

<!-- b000235 | references | pages [3] -->
m

<!-- b000236 | references | pages [3] -->
m

<!-- b000237 | references | pages [3] -->
m

<!-- b000238 | references | pages [3] -->
m

<!-- b000239 | references | pages [3] -->
m

<!-- b000240 | references | pages [3] -->
m

<!-- b000241 | references | pages [3] -->
m

<!-- b000242 | references | pages [3] -->
m

<!-- b000243 | references | pages [3] -->
m

<!-- b000244 | references | pages [3] -->
m

<!-- b000245 | references | pages [3] -->
m

<!-- b000246 | references | pages [3] -->
m

<!-- b000247 | references | pages [3] -->
m

<!-- b000248 | references | pages [3] -->
m

<!-- b000249 | references | pages [3] -->
m

<!-- b000250 | references | pages [3] -->
m

<!-- b000251 | references | pages [3] -->
m

<!-- b000252 | references | pages [3] -->
m

<!-- b000253 | references | pages [3] -->
m

<!-- b000254 | references | pages [3] -->
m

<!-- b000255 | references | pages [3] -->
m

<!-- b000256 | references | pages [3] -->
m

<!-- b000257 | references | pages [3] -->
m

<!-- b000258 | references | pages [3] -->
m

<!-- b000259 | references | pages [3] -->
m

<!-- b000260 | references | pages [3] -->
m

<!-- b000261 | references | pages [3] -->
m

<!-- b000262 | references | pages [3] -->
m

<!-- b000263 | references | pages [3] -->
m

<!-- b000264 | references | pages [3] -->
m

<!-- b000265 | references | pages [3] -->
m

<!-- b000266 | references | pages [3] -->
m

<!-- b000267 | references | pages [3] -->
m

<!-- b000268 | references | pages [3] -->
m

<!-- b000269 | references | pages [3] -->
m

<!-- b000270 | references | pages [3] -->
m

<!-- b000271 | references | pages [3] -->
m

<!-- b000272 | references | pages [3] -->
m

<!-- b000273 | references | pages [3] -->
m

<!-- b000274 | references | pages [3] -->
m

<!-- b000275 | references | pages [3] -->
m

<!-- b000276 | references | pages [3] -->
m

<!-- b000277 | references | pages [3] -->
m

<!-- b000278 | references | pages [3] -->
m

<!-- b000279 | references | pages [3] -->
m

<!-- b000280 | references | pages [3] -->
m

<!-- b000281 | references | pages [3] -->
m

<!-- b000282 | references | pages [3] -->
m

<!-- b000283 | references | pages [3] -->
m

<!-- b000284 | references | pages [3] -->
m

<!-- b000285 | references | pages [3] -->
m

<!-- b000286 | references | pages [3] -->
m

<!-- b000287 | references | pages [3] -->
m

<!-- b000288 | references | pages [3] -->
m

<!-- b000289 | references | pages [3] -->
m

<!-- b000290 | references | pages [3] -->
m

<!-- b000291 | references | pages [3] -->
m

<!-- b000292 | references | pages [3] -->
m

<!-- b000293 | references | pages [3] -->
m

<!-- b000294 | references | pages [3] -->
m

<!-- b000295 | references | pages [3] -->
m

<!-- b000296 | references | pages [3] -->
m

<!-- b000297 | references | pages [3] -->
m

<!-- b000298 | references | pages [3] -->
m

<!-- b000299 | references | pages [3] -->
m

<!-- b000300 | references | pages [3] -->
m

<!-- b000301 | references | pages [3] -->
m

<!-- b000302 | references | pages [3] -->
m

<!-- b000303 | references | pages [3] -->
m

<!-- b000304 | references | pages [3] -->
m

<!-- b000305 | references | pages [3] -->
m

<!-- b000306 | references | pages [3] -->
m

<!-- b000307 | references | pages [3] -->
m

<!-- b000308 | references | pages [3] -->
m

<!-- b000309 | references | pages [3] -->
m

<!-- b000310 | references | pages [3] -->
m

<!-- b000311 | references | pages [3] -->
m

<!-- b000312 | references | pages [3] -->
m

<!-- b000313 | references | pages [3] -->
m

<!-- b000314 | references | pages [3] -->
m

<!-- b000315 | references | pages [3] -->
m

<!-- b000316 | references | pages [3] -->
m

<!-- b000317 | references | pages [3] -->
m

<!-- b000318 | references | pages [3] -->
m

<!-- b000319 | references | pages [3] -->
m

<!-- b000320 | references | pages [3] -->
m

<!-- b000321 | references | pages [3] -->
m

<!-- b000322 | references | pages [3] -->
m

<!-- b000323 | references | pages [3] -->
m

<!-- b000324 | references | pages [3] -->
m

<!-- b000325 | references | pages [3] -->
m

<!-- b000326 | references | pages [3] -->
m

<!-- b000327 | references | pages [3] -->
m

<!-- b000328 | references | pages [3] -->
m

<!-- b000329 | references | pages [3] -->
m

<!-- b000330 | references | pages [3] -->
m

<!-- b000331 | references | pages [3] -->
m

<!-- b000332 | references | pages [3] -->
m

<!-- b000333 | references | pages [3] -->
m

<!-- b000334 | references | pages [3] -->
m

<!-- b000335 | references | pages [3] -->
m

<!-- b000336 | references | pages [3] -->
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

<!-- b000740 | references | pages [3] -->
22

<!-- b000741 | references | pages [3] -->
23

<!-- b000742 | furniture | pages [4] -->
Team # 2503268

<!-- b000743 | references | pages [4] -->
1

<!-- b000744 | heading | pages [4] -->
Introduction

<!-- b000745 | prose | pages [4] -->
1.1 Problem Background

<!-- b000746 | furniture | pages [4] -->
m

<!-- b000747 | furniture | pages [4] -->
m

<!-- b000748 | furniture | pages [4] -->
m

<!-- b000749 | furniture | pages [4] -->
m

<!-- b000750 | furniture | pages [4] -->
m

<!-- b000751 | furniture | pages [4] -->
m

<!-- b000752 | furniture | pages [4] -->
m

<!-- b000753 | furniture | pages [4] -->
m

<!-- b000754 | furniture | pages [4] -->
m

<!-- b000755 | furniture | pages [4] -->
m

<!-- b000756 | furniture | pages [4] -->
m

<!-- b000757 | furniture | pages [4] -->
m

<!-- b000758 | furniture | pages [4] -->
m

<!-- b000759 | furniture | pages [4] -->
m

<!-- b000760 | furniture | pages [4] -->
m

<!-- b000761 | furniture | pages [4] -->
m

<!-- b000762 | furniture | pages [4] -->
m

<!-- b000763 | furniture | pages [4] -->
m

<!-- b000764 | furniture | pages [4] -->
m

<!-- b000765 | furniture | pages [4] -->
m

<!-- b000766 | furniture | pages [4] -->
m

<!-- b000767 | furniture | pages [4] -->
m

<!-- b000768 | furniture | pages [4] -->
m

<!-- b000769 | furniture | pages [4] -->
m

<!-- b000770 | furniture | pages [4] -->
m

<!-- b000771 | furniture | pages [4] -->
m

<!-- b000772 | furniture | pages [4] -->
m

<!-- b000773 | furniture | pages [4] -->
m

<!-- b000774 | furniture | pages [4] -->
m

<!-- b000775 | furniture | pages [4] -->
m

<!-- b000776 | furniture | pages [4] -->
m

<!-- b000777 | furniture | pages [4] -->
m

<!-- b000778 | furniture | pages [4] -->
m

<!-- b000779 | furniture | pages [4] -->
m

<!-- b000780 | furniture | pages [4] -->
m

<!-- b000781 | furniture | pages [4] -->
m

<!-- b000782 | furniture | pages [4] -->
m

<!-- b000783 | furniture | pages [4] -->
m

<!-- b000784 | furniture | pages [4] -->
m

<!-- b000785 | furniture | pages [4] -->
m

<!-- b000786 | furniture | pages [4] -->
m

<!-- b000787 | furniture | pages [4] -->
m

<!-- b000788 | furniture | pages [4] -->
m

<!-- b000789 | furniture | pages [4] -->
m

<!-- b000790 | furniture | pages [4] -->
m

<!-- b000791 | furniture | pages [4] -->
m

<!-- b000792 | furniture | pages [4] -->
m

<!-- b000793 | furniture | pages [4] -->
m

<!-- b000794 | furniture | pages [4] -->
m

<!-- b000795 | furniture | pages [4] -->
m

<!-- b000796 | furniture | pages [4] -->
m

<!-- b000797 | furniture | pages [4] -->
m

<!-- b000798 | furniture | pages [4] -->
m

<!-- b000799 | furniture | pages [4] -->
m

<!-- b000800 | furniture | pages [4] -->
m

<!-- b000801 | furniture | pages [4] -->
m

<!-- b000802 | furniture | pages [4] -->
m

<!-- b000803 | furniture | pages [4] -->
m

<!-- b000804 | furniture | pages [4] -->
m

<!-- b000805 | furniture | pages [4] -->
m

<!-- b000806 | furniture | pages [4] -->
m

<!-- b000807 | furniture | pages [4] -->
m

<!-- b000808 | furniture | pages [4] -->
m

<!-- b000809 | furniture | pages [4] -->
m

<!-- b000810 | furniture | pages [4] -->
m

<!-- b000811 | furniture | pages [4] -->
m

<!-- b000812 | furniture | pages [4] -->
m

<!-- b000813 | furniture | pages [4] -->
m

<!-- b000814 | furniture | pages [4] -->
m

<!-- b000815 | furniture | pages [4] -->
m

<!-- b000816 | furniture | pages [4] -->
m

<!-- b000817 | furniture | pages [4] -->
m

<!-- b000818 | furniture | pages [4] -->
m

<!-- b000819 | furniture | pages [4] -->
m

<!-- b000820 | furniture | pages [4] -->
m

<!-- b000821 | furniture | pages [4] -->
m

<!-- b000822 | furniture | pages [4] -->
m

<!-- b000823 | furniture | pages [4] -->
m

<!-- b000824 | furniture | pages [4] -->
m

<!-- b000825 | furniture | pages [4] -->
m

<!-- b000826 | furniture | pages [4] -->
m

<!-- b000827 | furniture | pages [4] -->
m

<!-- b000828 | furniture | pages [4] -->
m

<!-- b000829 | furniture | pages [4] -->
m

<!-- b000830 | furniture | pages [4] -->
m

<!-- b000831 | furniture | pages [4] -->
m

<!-- b000832 | furniture | pages [4] -->
m

<!-- b000833 | furniture | pages [4] -->
m

<!-- b000834 | furniture | pages [4] -->
m

<!-- b000835 | furniture | pages [4] -->
m

<!-- b000836 | furniture | pages [4] -->
m

<!-- b000837 | furniture | pages [4] -->
m

<!-- b000838 | furniture | pages [4] -->
m

<!-- b000839 | furniture | pages [4] -->
m

<!-- b000840 | furniture | pages [4] -->
m

<!-- b000841 | furniture | pages [4] -->
m

<!-- b000842 | furniture | pages [4] -->
m

<!-- b000843 | furniture | pages [4] -->
m

<!-- b000844 | furniture | pages [4] -->
m

<!-- b000845 | furniture | pages [4] -->
m

<!-- b000846 | furniture | pages [4] -->
m

<!-- b000847 | furniture | pages [4] -->
m

<!-- b000848 | furniture | pages [4] -->
m

<!-- b000849 | furniture | pages [4] -->
m

<!-- b000850 | furniture | pages [4] -->
m

<!-- b000851 | furniture | pages [4] -->
m

<!-- b000852 | furniture | pages [4] -->
m

<!-- b000853 | furniture | pages [4] -->
m

<!-- b000854 | furniture | pages [4] -->
m

<!-- b000855 | furniture | pages [4] -->
m

<!-- b000856 | furniture | pages [4] -->
m

<!-- b000857 | furniture | pages [4] -->
m

<!-- b000858 | furniture | pages [4] -->
m

<!-- b000859 | furniture | pages [4] -->
m

<!-- b000860 | furniture | pages [4] -->
m

<!-- b000861 | furniture | pages [4] -->
m

<!-- b000862 | furniture | pages [4] -->
m

<!-- b000863 | furniture | pages [4] -->
m

<!-- b000864 | furniture | pages [4] -->
m

<!-- b000865 | furniture | pages [4] -->
m

<!-- b000866 | furniture | pages [4] -->
m

<!-- b000867 | furniture | pages [4] -->
m

<!-- b000868 | furniture | pages [4] -->
m

<!-- b000869 | furniture | pages [4] -->
m

<!-- b000870 | furniture | pages [4] -->
m

<!-- b000871 | furniture | pages [4] -->
m

<!-- b000872 | furniture | pages [4] -->
m

<!-- b000873 | furniture | pages [4] -->
m

<!-- b000874 | furniture | pages [4] -->
m

<!-- b000875 | furniture | pages [4] -->
m

<!-- b000876 | furniture | pages [4] -->
m

<!-- b000877 | furniture | pages [4] -->
m

<!-- b000878 | furniture | pages [4] -->
m

<!-- b000879 | furniture | pages [4] -->
m

<!-- b000880 | furniture | pages [4] -->
m

<!-- b000881 | furniture | pages [4] -->
m

<!-- b000882 | furniture | pages [4] -->
m

<!-- b000883 | furniture | pages [4] -->
m

<!-- b000884 | furniture | pages [4] -->
m

<!-- b000885 | furniture | pages [4] -->
m

<!-- b000886 | furniture | pages [4] -->
m

<!-- b000887 | furniture | pages [4] -->
m

<!-- b000888 | furniture | pages [4] -->
m

<!-- b000889 | furniture | pages [4] -->
m

<!-- b000890 | furniture | pages [4] -->
m

<!-- b000891 | furniture | pages [4] -->
m

<!-- b000892 | furniture | pages [4] -->
m

<!-- b000893 | furniture | pages [4] -->
m

<!-- b000894 | furniture | pages [4] -->
m

<!-- b000895 | furniture | pages [4] -->
m

<!-- b000896 | furniture | pages [4] -->
m

<!-- b000897 | furniture | pages [4] -->
m

<!-- b000898 | furniture | pages [4] -->
m

<!-- b000899 | furniture | pages [4] -->
m

<!-- b000900 | furniture | pages [4] -->
m

<!-- b000901 | furniture | pages [4] -->
m

<!-- b000902 | furniture | pages [4] -->
m

<!-- b000903 | furniture | pages [4] -->
m

<!-- b000904 | furniture | pages [4] -->
m

<!-- b000905 | furniture | pages [4] -->
m

<!-- b000906 | furniture | pages [4] -->
m

<!-- b000907 | furniture | pages [4] -->
m

<!-- b000908 | furniture | pages [4] -->
m

<!-- b000909 | furniture | pages [4] -->
m

<!-- b000910 | furniture | pages [4] -->
m

<!-- b000911 | furniture | pages [4] -->
m

<!-- b000912 | furniture | pages [4] -->
m

<!-- b000913 | furniture | pages [4] -->
m

<!-- b000914 | furniture | pages [4] -->
m

<!-- b000915 | furniture | pages [4] -->
m

<!-- b000916 | furniture | pages [4] -->
m

<!-- b000917 | furniture | pages [4] -->
m

<!-- b000918 | furniture | pages [4] -->
m

<!-- b000919 | furniture | pages [4] -->
m

<!-- b000920 | furniture | pages [4] -->
m

<!-- b000921 | furniture | pages [4] -->
m

<!-- b000922 | furniture | pages [4] -->
m

<!-- b000923 | furniture | pages [4] -->
m

<!-- b000924 | furniture | pages [4] -->
m

<!-- b000925 | furniture | pages [4] -->
m

<!-- b000926 | furniture | pages [4] -->
m

<!-- b000927 | furniture | pages [4] -->
m

<!-- b000928 | furniture | pages [4] -->
m

<!-- b000929 | furniture | pages [4] -->
m

<!-- b000930 | furniture | pages [4] -->
m

<!-- b000931 | furniture | pages [4] -->
m

<!-- b000932 | furniture | pages [4] -->
m

<!-- b000933 | furniture | pages [4] -->
m

<!-- b000934 | furniture | pages [4] -->
m

<!-- b000935 | furniture | pages [4] -->
m

<!-- b000936 | furniture | pages [4] -->
m

<!-- b000937 | furniture | pages [4] -->
m

<!-- b000938 | furniture | pages [4] -->
m

<!-- b000939 | furniture | pages [4] -->
m

<!-- b000940 | furniture | pages [4] -->
m

<!-- b000941 | furniture | pages [4] -->
m

<!-- b000942 | furniture | pages [4] -->
m

<!-- b000943 | furniture | pages [4] -->
m

<!-- b000944 | furniture | pages [4] -->
m

<!-- b000945 | furniture | pages [4] -->
m

<!-- b000946 | furniture | pages [4] -->
m

<!-- b000947 | furniture | pages [4] -->
m

<!-- b000948 | furniture | pages [4] -->
m

<!-- b000949 | furniture | pages [4] -->
m

<!-- b000950 | furniture | pages [4] -->
m

<!-- b000951 | furniture | pages [4] -->
m

<!-- b000952 | furniture | pages [4] -->
m

<!-- b000953 | furniture | pages [4] -->
m

<!-- b000954 | furniture | pages [4] -->
m

<!-- b000955 | furniture | pages [4] -->
m

<!-- b000956 | furniture | pages [4] -->
m

<!-- b000957 | furniture | pages [4] -->
m

<!-- b000958 | furniture | pages [4] -->
m

<!-- b000959 | furniture | pages [4] -->
m

<!-- b000960 | furniture | pages [4] -->
m

<!-- b000961 | furniture | pages [4] -->
m

<!-- b000962 | furniture | pages [4] -->
m

<!-- b000963 | furniture | pages [4] -->
m

<!-- b000964 | furniture | pages [4] -->
m

<!-- b000965 | furniture | pages [4] -->
m

<!-- b000966 | furniture | pages [4] -->
m

<!-- b000967 | furniture | pages [4] -->
m

<!-- b000968 | furniture | pages [4] -->
m

<!-- b000969 | furniture | pages [4] -->
m

<!-- b000970 | furniture | pages [4] -->
m

<!-- b000971 | furniture | pages [4] -->
m

<!-- b000972 | furniture | pages [4] -->
m

<!-- b000973 | furniture | pages [4] -->
m

<!-- b000974 | furniture | pages [4] -->
m

<!-- b000975 | furniture | pages [4] -->
m

<!-- b000976 | furniture | pages [4] -->
m

<!-- b000977 | furniture | pages [4] -->
m

<!-- b000978 | furniture | pages [4] -->
m

<!-- b000979 | furniture | pages [4] -->
m

<!-- b000980 | furniture | pages [4] -->
m

<!-- b000981 | furniture | pages [4] -->
m

<!-- b000982 | furniture | pages [4] -->
m

<!-- b000983 | furniture | pages [4] -->
m

<!-- b000984 | furniture | pages [4] -->
m

<!-- b000985 | furniture | pages [4] -->
m

<!-- b000986 | furniture | pages [4] -->
m

<!-- b000987 | furniture | pages [4] -->
m

<!-- b000988 | furniture | pages [4] -->
m

<!-- b000989 | furniture | pages [4] -->
m

<!-- b000990 | furniture | pages [4] -->
m

<!-- b000991 | furniture | pages [4] -->
m

<!-- b000992 | furniture | pages [4] -->
m

<!-- b000993 | furniture | pages [4] -->
m

<!-- b000994 | furniture | pages [4] -->
m

<!-- b000995 | furniture | pages [4] -->
m

<!-- b000996 | furniture | pages [4] -->
m

<!-- b000997 | furniture | pages [4] -->
m

<!-- b000998 | furniture | pages [4] -->
m

<!-- b000999 | furniture | pages [4] -->
m

<!-- b001000 | furniture | pages [4] -->
m

<!-- b001001 | furniture | pages [4] -->
m

<!-- b001002 | furniture | pages [4] -->
m

<!-- b001003 | furniture | pages [4] -->
m

<!-- b001004 | furniture | pages [4] -->
m

<!-- b001005 | furniture | pages [4] -->
m

<!-- b001006 | furniture | pages [4] -->
m

<!-- b001007 | furniture | pages [4] -->
m

<!-- b001008 | furniture | pages [4] -->
m

<!-- b001009 | furniture | pages [4] -->
m

<!-- b001010 | furniture | pages [4] -->
m

<!-- b001011 | furniture | pages [4] -->
m

<!-- b001012 | furniture | pages [4] -->
m

<!-- b001013 | furniture | pages [4] -->
m

<!-- b001014 | furniture | pages [4] -->
m

<!-- b001015 | furniture | pages [4] -->
m

<!-- b001016 | furniture | pages [4] -->
m

<!-- b001017 | furniture | pages [4] -->
m

<!-- b001018 | furniture | pages [4] -->
m

<!-- b001019 | furniture | pages [4] -->
m

<!-- b001020 | furniture | pages [4] -->
m

<!-- b001021 | furniture | pages [4] -->
m

<!-- b001022 | furniture | pages [4] -->
m

<!-- b001023 | furniture | pages [4] -->
m

<!-- b001024 | furniture | pages [4] -->
m

<!-- b001025 | furniture | pages [4] -->
m

<!-- b001026 | furniture | pages [4] -->
m

<!-- b001027 | furniture | pages [4] -->
m

<!-- b001028 | furniture | pages [4] -->
m

<!-- b001029 | furniture | pages [4] -->
m

<!-- b001030 | furniture | pages [4] -->
m

<!-- b001031 | furniture | pages [4] -->
m

<!-- b001032 | furniture | pages [4] -->
m

<!-- b001033 | furniture | pages [4] -->
m

<!-- b001034 | furniture | pages [4] -->
m

<!-- b001035 | furniture | pages [4] -->
m

<!-- b001036 | furniture | pages [4] -->
m

<!-- b001037 | furniture | pages [4] -->
m

<!-- b001038 | furniture | pages [4] -->
m

<!-- b001039 | furniture | pages [4] -->
m

<!-- b001040 | furniture | pages [4] -->
m

<!-- b001041 | furniture | pages [4] -->
m

<!-- b001042 | furniture | pages [4] -->
m

<!-- b001043 | furniture | pages [4] -->
m

<!-- b001044 | furniture | pages [4] -->
m

<!-- b001045 | furniture | pages [4] -->
m

<!-- b001046 | furniture | pages [4] -->
m

<!-- b001047 | furniture | pages [4] -->
m

<!-- b001048 | furniture | pages [4] -->
m

<!-- b001049 | furniture | pages [4] -->
m

<!-- b001050 | furniture | pages [4] -->
m

<!-- b001051 | furniture | pages [4] -->
m

<!-- b001052 | furniture | pages [4] -->
m

<!-- b001053 | furniture | pages [4] -->
m

<!-- b001054 | furniture | pages [4] -->
m

<!-- b001055 | furniture | pages [4] -->
m

<!-- b001056 | furniture | pages [4] -->
m

<!-- b001057 | furniture | pages [4] -->
m

<!-- b001058 | furniture | pages [4] -->
m

<!-- b001059 | furniture | pages [4] -->
m

<!-- b001060 | furniture | pages [4] -->
m

<!-- b001061 | furniture | pages [4] -->
m

<!-- b001062 | furniture | pages [4] -->
m

<!-- b001063 | furniture | pages [4] -->
m

<!-- b001064 | furniture | pages [4] -->
m

<!-- b001065 | furniture | pages [4] -->
m

<!-- b001066 | furniture | pages [4] -->
m

<!-- b001067 | furniture | pages [4] -->
m

<!-- b001068 | furniture | pages [4] -->
m

<!-- b001069 | furniture | pages [4] -->
m

<!-- b001070 | furniture | pages [4] -->
m

<!-- b001071 | furniture | pages [4] -->
m

<!-- b001072 | furniture | pages [4] -->
m

<!-- b001073 | furniture | pages [4] -->
m

<!-- b001074 | furniture | pages [4] -->
m

<!-- b001075 | furniture | pages [4] -->
m

<!-- b001076 | furniture | pages [4] -->
m

<!-- b001077 | furniture | pages [4] -->
m

<!-- b001078 | furniture | pages [4] -->
m

<!-- b001079 | furniture | pages [4] -->
m

<!-- b001080 | furniture | pages [4] -->
m

<!-- b001081 | furniture | pages [4] -->
m

<!-- b001082 | furniture | pages [4] -->
m

<!-- b001083 | furniture | pages [4] -->
m

<!-- b001084 | furniture | pages [4] -->
m

<!-- b001085 | furniture | pages [4] -->
m

<!-- b001086 | furniture | pages [4] -->
m

<!-- b001087 | furniture | pages [4] -->
m

<!-- b001088 | furniture | pages [4] -->
m

<!-- b001089 | furniture | pages [4] -->
m

<!-- b001090 | furniture | pages [4] -->
m

<!-- b001091 | furniture | pages [4] -->
Page 2 of 24

<!-- b001092 | furniture | pages [4] -->
m

<!-- b001093 | furniture | pages [4] -->
m

<!-- b001094 | furniture | pages [4] -->
m

<!-- b001095 | furniture | pages [4] -->
m

<!-- b001096 | furniture | pages [4] -->
m

<!-- b001097 | furniture | pages [4] -->
m

<!-- b001098 | furniture | pages [4] -->
m

<!-- b001099 | furniture | pages [4] -->
m

<!-- b001100 | furniture | pages [4] -->
m

<!-- b001101 | furniture | pages [4] -->
m

<!-- b001102 | furniture | pages [4] -->
m

<!-- b001103 | furniture | pages [4] -->
m

<!-- b001104 | furniture | pages [4] -->
m

<!-- b001105 | furniture | pages [4] -->
m

<!-- b001106 | furniture | pages [4] -->
m

<!-- b001107 | furniture | pages [4] -->
m

<!-- b001108 | furniture | pages [4] -->
m

<!-- b001109 | furniture | pages [4] -->
m

<!-- b001110 | furniture | pages [4] -->
m

<!-- b001111 | furniture | pages [4] -->
m

<!-- b001112 | furniture | pages [4] -->
m

<!-- b001113 | furniture | pages [4] -->
m

<!-- b001114 | furniture | pages [4] -->
m

<!-- b001115 | furniture | pages [4] -->
m

<!-- b001116 | furniture | pages [4] -->
m

<!-- b001117 | furniture | pages [4] -->
m

<!-- b001118 | furniture | pages [4] -->
m

<!-- b001119 | furniture | pages [4] -->
m

<!-- b001120 | furniture | pages [4] -->
m

<!-- b001121 | furniture | pages [4] -->
m

<!-- b001122 | furniture | pages [4] -->
m

<!-- b001123 | furniture | pages [4] -->
m

<!-- b001124 | furniture | pages [4] -->
m

<!-- b001125 | furniture | pages [4] -->
m

<!-- b001126 | furniture | pages [4] -->
m

<!-- b001127 | furniture | pages [4] -->
m

<!-- b001128 | furniture | pages [4] -->
m

<!-- b001129 | furniture | pages [4] -->
m

<!-- b001130 | furniture | pages [4] -->
m

<!-- b001131 | furniture | pages [4] -->
m

<!-- b001132 | furniture | pages [4] -->
m

<!-- b001133 | furniture | pages [4] -->
m

<!-- b001134 | furniture | pages [4] -->
m

<!-- b001135 | furniture | pages [4] -->
m

<!-- b001136 | furniture | pages [4] -->
m

<!-- b001137 | furniture | pages [4] -->
m

<!-- b001138 | furniture | pages [4] -->
m

<!-- b001139 | furniture | pages [4] -->
m

<!-- b001140 | furniture | pages [4] -->
m

<!-- b001141 | furniture | pages [4] -->
m

<!-- b001142 | furniture | pages [4] -->
m

<!-- b001143 | furniture | pages [4] -->
m

<!-- b001144 | furniture | pages [4] -->
m

<!-- b001145 | furniture | pages [4] -->
m

<!-- b001146 | furniture | pages [4] -->
m

<!-- b001147 | furniture | pages [4] -->
m

<!-- b001148 | furniture | pages [4] -->
m

<!-- b001149 | furniture | pages [4] -->
m

<!-- b001150 | furniture | pages [4] -->
m

<!-- b001151 | furniture | pages [4] -->
m

<!-- b001152 | furniture | pages [4] -->
m

<!-- b001153 | furniture | pages [4] -->
m

<!-- b001154 | furniture | pages [4] -->
m

<!-- b001155 | furniture | pages [4] -->
m

<!-- b001156 | furniture | pages [4] -->
m

<!-- b001157 | furniture | pages [4] -->
m

<!-- b001158 | furniture | pages [4] -->
m

<!-- b001159 | furniture | pages [4] -->
m

<!-- b001160 | furniture | pages [4] -->
m

<!-- b001161 | furniture | pages [4] -->
m

<!-- b001162 | furniture | pages [4] -->
m

<!-- b001163 | furniture | pages [4] -->
m

<!-- b001164 | furniture | pages [4] -->
m

<!-- b001165 | furniture | pages [4] -->
m

<!-- b001166 | furniture | pages [4] -->
m

<!-- b001167 | furniture | pages [4] -->
m

<!-- b001168 | furniture | pages [4] -->
m

<!-- b001169 | furniture | pages [4] -->
m

<!-- b001170 | furniture | pages [4] -->
m

<!-- b001171 | furniture | pages [4] -->
m

<!-- b001172 | furniture | pages [4] -->
m

<!-- b001173 | furniture | pages [4] -->
m

<!-- b001174 | furniture | pages [4] -->
m

<!-- b001175 | furniture | pages [4] -->
m

<!-- b001176 | furniture | pages [4] -->
m

<!-- b001177 | furniture | pages [4] -->
m

<!-- b001178 | furniture | pages [4] -->
m

<!-- b001179 | furniture | pages [4] -->
m

<!-- b001180 | furniture | pages [4] -->
m

<!-- b001181 | furniture | pages [4] -->
m

<!-- b001182 | furniture | pages [4] -->
m

<!-- b001183 | furniture | pages [4] -->
m

<!-- b001184 | furniture | pages [4] -->
m

<!-- b001185 | furniture | pages [4] -->
m

<!-- b001186 | furniture | pages [4] -->
m

<!-- b001187 | furniture | pages [4] -->
m

<!-- b001188 | furniture | pages [4] -->
m

<!-- b001189 | furniture | pages [4] -->
m

<!-- b001190 | furniture | pages [4] -->
m

<!-- b001191 | furniture | pages [4] -->
m

<!-- b001192 | furniture | pages [4] -->
m

<!-- b001193 | furniture | pages [4] -->
m

<!-- b001194 | furniture | pages [4] -->
m

<!-- b001195 | furniture | pages [4] -->
m

<!-- b001196 | furniture | pages [4] -->
m

<!-- b001197 | furniture | pages [4] -->
m

<!-- b001198 | furniture | pages [4] -->
m

<!-- b001199 | furniture | pages [4] -->
m

<!-- b001200 | furniture | pages [4] -->
m

<!-- b001201 | furniture | pages [4] -->
m

<!-- b001202 | furniture | pages [4] -->
m

<!-- b001203 | furniture | pages [4] -->
m

<!-- b001204 | furniture | pages [4] -->
m

<!-- b001205 | furniture | pages [4] -->
m

<!-- b001206 | furniture | pages [4] -->
m

<!-- b001207 | furniture | pages [4] -->
m

<!-- b001208 | furniture | pages [4] -->
m

<!-- b001209 | furniture | pages [4] -->
m

<!-- b001210 | furniture | pages [4] -->
m

<!-- b001211 | furniture | pages [4] -->
m

<!-- b001212 | furniture | pages [4] -->
m

<!-- b001213 | furniture | pages [4] -->
m

<!-- b001214 | furniture | pages [4] -->
m

<!-- b001215 | furniture | pages [4] -->
m

<!-- b001216 | furniture | pages [4] -->
m

<!-- b001217 | furniture | pages [4] -->
m

<!-- b001218 | furniture | pages [4] -->
m

<!-- b001219 | furniture | pages [4] -->
m

<!-- b001220 | furniture | pages [4] -->
m

<!-- b001221 | furniture | pages [4] -->
m

<!-- b001222 | furniture | pages [4] -->
m

<!-- b001223 | furniture | pages [4] -->
m

<!-- b001224 | furniture | pages [4] -->
m

<!-- b001225 | furniture | pages [4] -->
m

<!-- b001226 | furniture | pages [4] -->
m

<!-- b001227 | furniture | pages [4] -->
m

<!-- b001228 | furniture | pages [4] -->
m

<!-- b001229 | furniture | pages [4] -->
m

<!-- b001230 | furniture | pages [4] -->
m

<!-- b001231 | furniture | pages [4] -->
m

<!-- b001232 | furniture | pages [4] -->
m

<!-- b001233 | furniture | pages [4] -->
m

<!-- b001234 | furniture | pages [4] -->
m

<!-- b001235 | furniture | pages [4] -->
m

<!-- b001236 | furniture | pages [4] -->
m

<!-- b001237 | furniture | pages [4] -->
m

<!-- b001238 | furniture | pages [4] -->
m

<!-- b001239 | furniture | pages [4] -->
m

<!-- b001240 | furniture | pages [4] -->
m

<!-- b001241 | furniture | pages [4] -->
m

<!-- b001242 | furniture | pages [4] -->
m

<!-- b001243 | furniture | pages [4] -->
m

<!-- b001244 | furniture | pages [4] -->
m

<!-- b001245 | furniture | pages [4] -->
m

<!-- b001246 | furniture | pages [4] -->
m

<!-- b001247 | prose | pages [4] -->
Juneau, Alaska, renowned for its stunning natural landscapes and rich tourism resources, has be- come a prominent destination for cruise passengers. But the rapid increase in tourist numbers in recent years has posed signiﬁcant challenges to the local environment, infrastructure, and residents’ quality of life. While measures such as daily visitor caps and agreements with cruise operators represent initial steps toward addressing these issues, they remain insuﬃcient to ensure the sustainable development of tourism in the region.

<!-- b001248 | prose | pages [4] -->
Notably, the challenges faced by Juneau reﬂect a global issue. Numerous destinations worldwide grapple with similar issues. Destinations like Mount Rainier National Park use reservation systems, while Venice and Barcelona impose day-trip fees. Athens is exploring tourist limits, highlighting the need for a framework balancing economic beneﬁts and conservation. This work aims to create a scal- able model for sustainable tourism, addressing Juneau’s needs and oﬀering solutions for overtourism and long-term resilience.

<!-- b001249 | prose | pages [4] -->
1.2 Restatement of the Problem

<!-- b001250 | prose | pages [4] -->
To ensure the sustainable development of Juneau’s tourism industry, we aim to develop a scien- tiﬁc model and management strategies to balance the number of visitors, revenue, and resource conservation. To achieve this, we need to address the following problems:

<!-- b001251 | prose | pages [4] -->
1. Develop a model to optimize the sustainability of Juneau’s tourism industry. Clearly deﬁne the objectives to optimize (e.g., number of visitors, revenue growth) and constraints (e.g., infras- tructure capacity, environmental protection), and propose management strategies to stabilize the industry. 2. Perform sensitivity analysis to evaluate the impact of various factors in the model and identify key variables that critically inﬂuence sustainable development, enabling policymakers to adjust strategies eﬀectively. 3. Adapt the model to other tourist destinations, assess its applicability, and reﬁne it to promote less-visited attractions and improve tourism balance across diﬀerent locations.

<!-- b001252 | prose | pages [4] -->
1.3 Our Work

<!-- b001253 | prose | pages [4] -->
To address the challenges of sustainable tourism in Juneau, we propose a tourism system made up of a Sustainable Tourism Dynamics Model (STDM), an Evaluation Model and Intervention Strate- gies. The SDTM, formulated with ordinary diﬀerential equations (ODE), establishes the relationships among key variables, including environmental degradation, tourist numbers and tax revenue from tourism. The Intervention Strategies contain ﬁnite number of predeﬁned strategy combination that will inﬂuence the dynamics with the STDM. The resulting outputs from the STDM, along with the strategy combinations, are assessed through an Analytical Hierarchy Process (AHP)-based evaluation model, which will give feedback to reﬁne and optimize the strategy combination.

<!-- b001254 | prose | pages [4] -->
Then, we apply the model to both Juneau and Big Sur, utilizing location speciﬁc parameters to conduct comparative analyses and predict optimal strategies for sustainable development. By applying this model, we predict the best intervention strategies and the comprehensive development of the places. In this way, we can give useful suggestions to the government. By analyzing results and doing sensitivity analysis, we have an insight of the strengths and weaknesses of the model.

<!-- b001255 | prose | pages [4] -->
关注数学模型

<!-- b001256 | furniture | pages [4] -->
2

<!-- b001257 | furniture | pages [4] -->
MATHmodels

<!-- b001258 | furniture | pages [4] -->
获取更多资讯

<!-- b001259 | furniture | pages [5] -->
Team # 2503268

<!-- b001260 | furniture | pages [5] -->
Page 3 of 24

<!-- b001261 | prose | pages [5] -->
微信公众号：数学模型

<!-- b001262 | prose | pages [5] -->
微信号：MATHmodels

<!-- b001263 | caption | pages [5] -->
Figure 1: Pipeline of Our Model

<!-- b001264 | prose | pages [5] -->
2

<!-- b001265 | heading | pages [5] -->
Assumptions and Justiﬁcations

<!-- b001266 | prose | pages [5] -->
Through the full analysis of the problem, to simplify our model, we make the following reasonable assumptions.

<!-- b001267 | prose | pages [5] -->
• Assumption 1:Government policies are assumed to be fully implemented instantaneously. →Justiﬁcation: In reality, the time required for policy implementation can vary depending on

<!-- b001268 | prose | pages [5] -->
administrative processes, public response, and logistical challenges. However, these delays are often unpredictable and context-dependent, making them diﬃcult to generalize within a theoretical framework. By assuming instantaneous implementation, the model prioritizes the analysis of long-term systemic outcomes and policy eﬀectiveness, enabling clearer insights into the relationships between variables.

<!-- b001269 | prose | pages [5] -->
• Assumption 2: Incidents, sudden changes, minor factors and extreme situations are not taken into consideration.

<!-- b001270 | heading | pages [5] -->
→Justiﬁcation: Including these factors would greatly increase the model’s complexity without

<!-- b001271 | prose | pages [5] -->
signiﬁcantly enhancing its predictive accuracy in typical scenarios. Such events are rare, unpredictable, and context-speciﬁc, making them hard to generalize. Focusing on primary factors ensures the model remains eﬃcient, broadly applicable, and capable of capturing essential system dynamics.

<!-- b001272 | furniture | pages [6] -->
Team # 2503268

<!-- b001273 | furniture | pages [6] -->
Page 4 of 24

<!-- b001274 | prose | pages [6] -->
• Assumption 3: When determining strategies, some stable variables, are treated as con- stants. →Justiﬁcation: Stable variables like the local population show minimal short-term ﬂuctuations

<!-- b001275 | prose | pages [6] -->
and have little impact on system dynamics. Treating them as constants avoids unnecessary complexity, allowing the model to focus on key drivers of change while remaining eﬃcient and easy to analyze.

<!-- b001276 | prose | pages [6] -->
• Assumption 4: The data and materials used in the model are accurate, reliable, and sourced from trusted and authoritative databases or publications.

<!-- b001277 | heading | pages [6] -->
→Justiﬁcation: The assumption of data reliability ensures consistency and avoids errors caused

<!-- b001278 | prose | pages [6] -->
by faulty or incomplete information. All data used in this model is sourced from reputable organizations, government reports, or peer-reviewed publications, which guarantees its cred- ibility and relevance.

<!-- b001279 | prose | pages [6] -->
3

<!-- b001280 | heading | pages [6] -->
Notations

<!-- b001281 | prose | pages [6] -->
Important notations used in this paper are listed below.

<!-- b001282 | caption | pages [6] -->
Table 1: Major Notations

<!-- b001283 | prose | pages [6] -->
Description

<!-- b001284 | heading | pages [6] -->
Symbol

<!-- b001285 | prose | pages [6] -->
Unit

<!-- b001286 | prose | pages [6] -->
Glacier ELA height in Juneau, HJuneau m Annual number of tourists in Juneau NJuneau / Annual hotel tax revenue in Juneau TJuneau H↑ $

<!-- b001287 | prose | pages [6] -->
Normalized HJuneau Juneau N↑ /

<!-- b001288 | prose | pages [6] -->
Normalized NJuneau Juneau T ↑ /

<!-- b001289 | prose | pages [6] -->
Normalized TJuneau Juneau P↑ /

<!-- b001290 | prose | pages [6] -->
The resident population in Juneau Juneau / Height of coastal landslide loss in Pfeiﬀer Big Sur HS ur cm Annual number of tourists in Pfeiﬀer Big Sur NS ur / Annual revenue gained from tourism in Pfeiﬀer Big Sur TS ur H↑ $

<!-- b001291 | prose | pages [6] -->
Normalized HS ur S ur N↑ /

<!-- b001292 | prose | pages [6] -->
Normalized NS ur S ur T ↑ /

<!-- b001293 | prose | pages [6] -->
Normalized TS ur S ur P↑ /

<!-- b001294 | prose | pages [6] -->
The resident population in Pfeiﬀer Big Sur S ur / The weighted comprehensive assessment score of the current year S core / The weighted score considering the ith factor S corei / The score considering the jth secondary indicator in the ith factor S coreij / Factors of disturbance in variable x ϖx % Percentage distribution of tax revenue of infrastructure, glacier protection, µ1 to µ5 % waste disposal, cultural development and police security.

<!-- b001295 | prose | pages [6] -->
关注数学模型

<!-- b001296 | furniture | pages [6] -->
2

<!-- b001297 | furniture | pages [6] -->
MATHmodels

<!-- b001298 | furniture | pages [6] -->
获取更多资讯

<!-- b001299 | furniture | pages [8] -->
Team # 2503268

<!-- b001300 | furniture | pages [8] -->
Page 6 of 24

<!-- b001301 | prose | pages [8] -->
Secondly, considering that the number of tourists far exceeds the local resident population, and given the distinct impacts these two groups have on the environment and economy, the local population can be considered negligible in the population dimension. This makes it reasonable to use tourist numbers as a representative indicator for the population metric. According to the most recent Juneau Tourism Survey, hotel revenue consistently accounts for a stable proportion of the total government revenue. Therefore, we use hotel tax revenue as an indicator to represent the economic dimension. 5

<!-- b001302 | heading | pages [8] -->
Model Design

<!-- b001303 | heading | pages [8] -->
Sustainable Tourism Dynamics Model (STDM)

<!-- b001304 | prose | pages [8] -->
5.1

<!-- b001305 | prose | pages [8] -->
Natural environments, economic factors, and population dynamics are deeply interconnected. This study aims to represent the dynamics between glacier ELA height, annual number of tourists, and annual hotel tax revenue using fundamental data. Such a model provides an essential explanatory

<!-- b001306 | prose | pages [8] -->
m

<!-- b001307 | prose | pages [8] -->
m

<!-- b001308 | prose | pages [8] -->
m

<!-- b001309 | prose | pages [8] -->
m

<!-- b001310 | prose | pages [8] -->
m

<!-- b001311 | prose | pages [8] -->
m

<!-- b001312 | prose | pages [8] -->
m

<!-- b001313 | prose | pages [8] -->
m

<!-- b001314 | prose | pages [8] -->
m

<!-- b001315 | prose | pages [8] -->
m

<!-- b001316 | prose | pages [8] -->
m

<!-- b001317 | prose | pages [8] -->
m

<!-- b001318 | prose | pages [8] -->
m

<!-- b001319 | prose | pages [8] -->
m

<!-- b001320 | prose | pages [8] -->
m

<!-- b001321 | prose | pages [8] -->
m

<!-- b001322 | prose | pages [8] -->
m

<!-- b001323 | prose | pages [8] -->
m

<!-- b001324 | prose | pages [8] -->
m

<!-- b001325 | prose | pages [8] -->
m

<!-- b001326 | prose | pages [8] -->
m

<!-- b001327 | prose | pages [8] -->
m

<!-- b001328 | prose | pages [8] -->
m

<!-- b001329 | prose | pages [8] -->
m

<!-- b001330 | prose | pages [8] -->
m

<!-- b001331 | prose | pages [8] -->
m

<!-- b001332 | prose | pages [8] -->
m

<!-- b001333 | prose | pages [8] -->
m

<!-- b001334 | prose | pages [8] -->
m

<!-- b001335 | prose | pages [8] -->
m

<!-- b001336 | prose | pages [8] -->
m

<!-- b001337 | prose | pages [8] -->
m

<!-- b001338 | prose | pages [8] -->
m

<!-- b001339 | prose | pages [8] -->
m

<!-- b001340 | prose | pages [8] -->
m

<!-- b001341 | prose | pages [8] -->
m

<!-- b001342 | prose | pages [8] -->
m

<!-- b001343 | prose | pages [8] -->
m

<!-- b001344 | prose | pages [8] -->
m

<!-- b001345 | prose | pages [8] -->
m

<!-- b001346 | prose | pages [8] -->
m

<!-- b001347 | prose | pages [8] -->
m

<!-- b001348 | prose | pages [8] -->
m

<!-- b001349 | prose | pages [8] -->
m

<!-- b001350 | prose | pages [8] -->
m

<!-- b001351 | prose | pages [8] -->
m

<!-- b001352 | prose | pages [8] -->
m

<!-- b001353 | prose | pages [8] -->
m

<!-- b001354 | prose | pages [8] -->
m

<!-- b001355 | prose | pages [8] -->
m

<!-- b001356 | prose | pages [8] -->
m

<!-- b001357 | prose | pages [8] -->
m

<!-- b001358 | prose | pages [8] -->
m

<!-- b001359 | prose | pages [8] -->
m

<!-- b001360 | prose | pages [8] -->
m

<!-- b001361 | prose | pages [8] -->
m

<!-- b001362 | prose | pages [8] -->
m

<!-- b001363 | prose | pages [8] -->
m

<!-- b001364 | prose | pages [8] -->
m

<!-- b001365 | prose | pages [8] -->
m

<!-- b001366 | prose | pages [8] -->
m

<!-- b001367 | prose | pages [8] -->
m

<!-- b001368 | prose | pages [8] -->
m

<!-- b001369 | prose | pages [8] -->
m

<!-- b001370 | prose | pages [8] -->
m

<!-- b001371 | prose | pages [8] -->
m

<!-- b001372 | prose | pages [8] -->
m

<!-- b001373 | prose | pages [8] -->
m

<!-- b001374 | prose | pages [8] -->
m

<!-- b001375 | prose | pages [8] -->
m

<!-- b001376 | prose | pages [8] -->
m

<!-- b001377 | prose | pages [8] -->
m

<!-- b001378 | prose | pages [8] -->
m

<!-- b001379 | prose | pages [8] -->
m

<!-- b001380 | prose | pages [8] -->
m

<!-- b001381 | prose | pages [8] -->
m

<!-- b001382 | prose | pages [8] -->
m

<!-- b001383 | prose | pages [8] -->
m

<!-- b001384 | prose | pages [8] -->
m

<!-- b001385 | prose | pages [8] -->
m

<!-- b001386 | prose | pages [8] -->
m

<!-- b001387 | prose | pages [8] -->
m

<!-- b001388 | prose | pages [8] -->
m

<!-- b001389 | prose | pages [8] -->
m

<!-- b001390 | prose | pages [8] -->
m

<!-- b001391 | prose | pages [8] -->
m

<!-- b001392 | prose | pages [8] -->
m

<!-- b001393 | prose | pages [8] -->
m

<!-- b001394 | prose | pages [8] -->
m

<!-- b001395 | prose | pages [8] -->
m

<!-- b001396 | prose | pages [8] -->
m

<!-- b001397 | prose | pages [8] -->
m

<!-- b001398 | prose | pages [8] -->
m

<!-- b001399 | prose | pages [8] -->
m

<!-- b001400 | prose | pages [8] -->
m

<!-- b001401 | prose | pages [8] -->
m

<!-- b001402 | prose | pages [8] -->
m

<!-- b001403 | prose | pages [8] -->
m

<!-- b001404 | prose | pages [8] -->
m

<!-- b001405 | prose | pages [8] -->
m

<!-- b001406 | prose | pages [8] -->
m

<!-- b001407 | prose | pages [8] -->
m

<!-- b001408 | prose | pages [8] -->
m

<!-- b001409 | prose | pages [8] -->
m

<!-- b001410 | prose | pages [8] -->
m

<!-- b001411 | prose | pages [8] -->
m

<!-- b001412 | prose | pages [8] -->
m

<!-- b001413 | prose | pages [8] -->
m

<!-- b001414 | prose | pages [8] -->
m

<!-- b001415 | prose | pages [8] -->
m

<!-- b001416 | prose | pages [8] -->
m

<!-- b001417 | prose | pages [8] -->
m

<!-- b001418 | prose | pages [8] -->
m

<!-- b001419 | prose | pages [8] -->
m

<!-- b001420 | prose | pages [8] -->
m

<!-- b001421 | prose | pages [8] -->
m

<!-- b001422 | prose | pages [8] -->
m

<!-- b001423 | prose | pages [8] -->
m

<!-- b001424 | prose | pages [8] -->
m

<!-- b001425 | prose | pages [8] -->
m

<!-- b001426 | prose | pages [8] -->
m

<!-- b001427 | prose | pages [8] -->
m

<!-- b001428 | prose | pages [8] -->
m

<!-- b001429 | prose | pages [8] -->
m

<!-- b001430 | prose | pages [8] -->
m

<!-- b001431 | prose | pages [8] -->
m

<!-- b001432 | prose | pages [8] -->
m

<!-- b001433 | prose | pages [8] -->
m

<!-- b001434 | prose | pages [8] -->
m

<!-- b001435 | prose | pages [8] -->
m

<!-- b001436 | prose | pages [8] -->
m

<!-- b001437 | prose | pages [8] -->
m

<!-- b001438 | prose | pages [8] -->
m

<!-- b001439 | prose | pages [8] -->
m

<!-- b001440 | prose | pages [8] -->
m

<!-- b001441 | prose | pages [8] -->
m

<!-- b001442 | prose | pages [8] -->
m

<!-- b001443 | prose | pages [8] -->
m

<!-- b001444 | prose | pages [8] -->
m

<!-- b001445 | prose | pages [8] -->
m

<!-- b001446 | prose | pages [8] -->
m

<!-- b001447 | prose | pages [8] -->
m

<!-- b001448 | prose | pages [8] -->
m

<!-- b001449 | prose | pages [8] -->
m

<!-- b001450 | prose | pages [8] -->
m

<!-- b001451 | prose | pages [8] -->
m

<!-- b001452 | prose | pages [8] -->
framework for understanding the logical relationships between these factors, laying the foundation for

<!-- b001453 | prose | pages [8] -->
m

<!-- b001454 | prose | pages [8] -->
m

<!-- b001455 | prose | pages [8] -->
m

<!-- b001456 | prose | pages [8] -->
m

<!-- b001457 | prose | pages [8] -->
m

<!-- b001458 | prose | pages [8] -->
m

<!-- b001459 | prose | pages [8] -->
m

<!-- b001460 | prose | pages [8] -->
m

<!-- b001461 | prose | pages [8] -->
m

<!-- b001462 | prose | pages [8] -->
m

<!-- b001463 | prose | pages [8] -->
m

<!-- b001464 | prose | pages [8] -->
m

<!-- b001465 | prose | pages [8] -->
m

<!-- b001466 | prose | pages [8] -->
m

<!-- b001467 | prose | pages [8] -->
m

<!-- b001468 | prose | pages [8] -->
m

<!-- b001469 | prose | pages [8] -->
m

<!-- b001470 | prose | pages [8] -->
m

<!-- b001471 | prose | pages [8] -->
m

<!-- b001472 | prose | pages [8] -->
m

<!-- b001473 | prose | pages [8] -->
m

<!-- b001474 | prose | pages [8] -->
m

<!-- b001475 | prose | pages [8] -->
m

<!-- b001476 | prose | pages [8] -->
m

<!-- b001477 | prose | pages [8] -->
m

<!-- b001478 | prose | pages [8] -->
m

<!-- b001479 | prose | pages [8] -->
m

<!-- b001480 | prose | pages [8] -->
m

<!-- b001481 | prose | pages [8] -->
m

<!-- b001482 | prose | pages [8] -->
m

<!-- b001483 | prose | pages [8] -->
m

<!-- b001484 | prose | pages [8] -->
m

<!-- b001485 | prose | pages [8] -->
m

<!-- b001486 | prose | pages [8] -->
m

<!-- b001487 | prose | pages [8] -->
m

<!-- b001488 | prose | pages [8] -->
m

<!-- b001489 | prose | pages [8] -->
m

<!-- b001490 | prose | pages [8] -->
m

<!-- b001491 | prose | pages [8] -->
m

<!-- b001492 | prose | pages [8] -->
m

<!-- b001493 | prose | pages [8] -->
m

<!-- b001494 | prose | pages [8] -->
m

<!-- b001495 | prose | pages [8] -->
m

<!-- b001496 | prose | pages [8] -->
m

<!-- b001497 | prose | pages [8] -->
m

<!-- b001498 | prose | pages [8] -->
m

<!-- b001499 | prose | pages [8] -->
m

<!-- b001500 | prose | pages [8] -->
m

<!-- b001501 | prose | pages [8] -->
m

<!-- b001502 | prose | pages [8] -->
m

<!-- b001503 | prose | pages [8] -->
m

<!-- b001504 | prose | pages [8] -->
m

<!-- b001505 | prose | pages [8] -->
m

<!-- b001506 | prose | pages [8] -->
m

<!-- b001507 | prose | pages [8] -->
m

<!-- b001508 | prose | pages [8] -->
m

<!-- b001509 | prose | pages [8] -->
m

<!-- b001510 | prose | pages [8] -->
m

<!-- b001511 | prose | pages [8] -->
m

<!-- b001512 | prose | pages [8] -->
m

<!-- b001513 | prose | pages [8] -->
m

<!-- b001514 | prose | pages [8] -->
m

<!-- b001515 | prose | pages [8] -->
m

<!-- b001516 | prose | pages [8] -->
m

<!-- b001517 | prose | pages [8] -->
m

<!-- b001518 | prose | pages [8] -->
m

<!-- b001519 | prose | pages [8] -->
m

<!-- b001520 | prose | pages [8] -->
m

<!-- b001521 | prose | pages [8] -->
m

<!-- b001522 | prose | pages [8] -->
m

<!-- b001523 | prose | pages [8] -->
m

<!-- b001524 | prose | pages [8] -->
m

<!-- b001525 | prose | pages [8] -->
m

<!-- b001526 | prose | pages [8] -->
m

<!-- b001527 | prose | pages [8] -->
m

<!-- b001528 | prose | pages [8] -->
m

<!-- b001529 | prose | pages [8] -->
m

<!-- b001530 | prose | pages [8] -->
m

<!-- b001531 | prose | pages [8] -->
m

<!-- b001532 | prose | pages [8] -->
m

<!-- b001533 | prose | pages [8] -->
m

<!-- b001534 | prose | pages [8] -->
m

<!-- b001535 | prose | pages [8] -->
m

<!-- b001536 | prose | pages [8] -->
m

<!-- b001537 | prose | pages [8] -->
m

<!-- b001538 | prose | pages [8] -->
m

<!-- b001539 | prose | pages [8] -->
m

<!-- b001540 | prose | pages [8] -->
m

<!-- b001541 | prose | pages [8] -->
m

<!-- b001542 | prose | pages [8] -->
m

<!-- b001543 | prose | pages [8] -->
m

<!-- b001544 | prose | pages [8] -->
m

<!-- b001545 | prose | pages [8] -->
m

<!-- b001546 | prose | pages [8] -->
m

<!-- b001547 | prose | pages [8] -->
m

<!-- b001548 | prose | pages [8] -->
m

<!-- b001549 | prose | pages [8] -->
m

<!-- b001550 | prose | pages [8] -->
m

<!-- b001551 | prose | pages [8] -->
m

<!-- b001552 | prose | pages [8] -->
m

<!-- b001553 | prose | pages [8] -->
m

<!-- b001554 | prose | pages [8] -->
m

<!-- b001555 | prose | pages [8] -->
m

<!-- b001556 | prose | pages [8] -->
m

<!-- b001557 | prose | pages [8] -->
m

<!-- b001558 | prose | pages [8] -->
m

<!-- b001559 | prose | pages [8] -->
m

<!-- b001560 | prose | pages [8] -->
m

<!-- b001561 | prose | pages [8] -->
m

<!-- b001562 | prose | pages [8] -->
m

<!-- b001563 | prose | pages [8] -->
m

<!-- b001564 | prose | pages [8] -->
m

<!-- b001565 | prose | pages [8] -->
m

<!-- b001566 | prose | pages [8] -->
m

<!-- b001567 | prose | pages [8] -->
m

<!-- b001568 | prose | pages [8] -->
m

<!-- b001569 | prose | pages [8] -->
m

<!-- b001570 | prose | pages [8] -->
m

<!-- b001571 | prose | pages [8] -->
m

<!-- b001572 | prose | pages [8] -->
m

<!-- b001573 | prose | pages [8] -->
m

<!-- b001574 | prose | pages [8] -->
m

<!-- b001575 | prose | pages [8] -->
m

<!-- b001576 | prose | pages [8] -->
m

<!-- b001577 | prose | pages [8] -->
m

<!-- b001578 | prose | pages [8] -->
m

<!-- b001579 | prose | pages [8] -->
m

<!-- b001580 | prose | pages [8] -->
m

<!-- b001581 | prose | pages [8] -->
m

<!-- b001582 | prose | pages [8] -->
m

<!-- b001583 | prose | pages [8] -->
m

<!-- b001584 | prose | pages [8] -->
m

<!-- b001585 | prose | pages [8] -->
m

<!-- b001586 | prose | pages [8] -->
m

<!-- b001587 | prose | pages [8] -->
m

<!-- b001588 | prose | pages [8] -->
m

<!-- b001589 | prose | pages [8] -->
m

<!-- b001590 | prose | pages [8] -->
m

<!-- b001591 | prose | pages [8] -->
m

<!-- b001592 | prose | pages [8] -->
m

<!-- b001593 | prose | pages [8] -->
m

<!-- b001594 | prose | pages [8] -->
m

<!-- b001595 | prose | pages [8] -->
m

<!-- b001596 | prose | pages [8] -->
m

<!-- b001597 | prose | pages [8] -->
m

<!-- b001598 | prose | pages [8] -->
m

<!-- b001599 | prose | pages [8] -->
m

<!-- b001600 | prose | pages [8] -->
m

<!-- b001601 | prose | pages [8] -->
m

<!-- b001602 | prose | pages [8] -->
m

<!-- b001603 | prose | pages [8] -->
more detailed analysis and decision-making in subsequent sections.

<!-- b001604 | prose | pages [8] -->
5.1.1 Glacier ELA Height Dynamics

<!-- b001605 | prose | pages [8] -->
m

<!-- b001606 | prose | pages [8] -->
m

<!-- b001607 | prose | pages [8] -->
m

<!-- b001608 | prose | pages [8] -->
m

<!-- b001609 | prose | pages [8] -->
m

<!-- b001610 | prose | pages [8] -->
m

<!-- b001611 | prose | pages [8] -->
m

<!-- b001612 | prose | pages [8] -->
m

<!-- b001613 | prose | pages [8] -->
m

<!-- b001614 | prose | pages [8] -->
m

<!-- b001615 | prose | pages [8] -->
m

<!-- b001616 | prose | pages [8] -->
m

<!-- b001617 | prose | pages [8] -->
m

<!-- b001618 | prose | pages [8] -->
m

<!-- b001619 | prose | pages [8] -->
m

<!-- b001620 | prose | pages [8] -->
m

<!-- b001621 | prose | pages [8] -->
m

<!-- b001622 | prose | pages [8] -->
m

<!-- b001623 | prose | pages [8] -->
m

<!-- b001624 | prose | pages [8] -->
m

<!-- b001625 | prose | pages [8] -->
m

<!-- b001626 | prose | pages [8] -->
m

<!-- b001627 | prose | pages [8] -->
m

<!-- b001628 | prose | pages [8] -->
m

<!-- b001629 | prose | pages [8] -->
m

<!-- b001630 | prose | pages [8] -->
m

<!-- b001631 | prose | pages [8] -->
m

<!-- b001632 | prose | pages [8] -->
m

<!-- b001633 | prose | pages [8] -->
m

<!-- b001634 | prose | pages [8] -->
m

<!-- b001635 | prose | pages [8] -->
m

<!-- b001636 | prose | pages [8] -->
m

<!-- b001637 | prose | pages [8] -->
m

<!-- b001638 | prose | pages [8] -->
m

<!-- b001639 | prose | pages [8] -->
m

<!-- b001640 | prose | pages [8] -->
m

<!-- b001641 | prose | pages [8] -->
m

<!-- b001642 | prose | pages [8] -->
m

<!-- b001643 | prose | pages [8] -->
m

<!-- b001644 | prose | pages [8] -->
m

<!-- b001645 | prose | pages [8] -->
m

<!-- b001646 | prose | pages [8] -->
m

<!-- b001647 | prose | pages [8] -->
m

<!-- b001648 | prose | pages [8] -->
m

<!-- b001649 | prose | pages [8] -->
m

<!-- b001650 | prose | pages [8] -->
m

<!-- b001651 | prose | pages [8] -->
m

<!-- b001652 | prose | pages [8] -->
m

<!-- b001653 | prose | pages [8] -->
m

<!-- b001654 | prose | pages [8] -->
m

<!-- b001655 | prose | pages [8] -->
m

<!-- b001656 | prose | pages [8] -->
m

<!-- b001657 | prose | pages [8] -->
m

<!-- b001658 | prose | pages [8] -->
m

<!-- b001659 | prose | pages [8] -->
m

<!-- b001660 | prose | pages [8] -->
m

<!-- b001661 | prose | pages [8] -->
m

<!-- b001662 | prose | pages [8] -->
m

<!-- b001663 | prose | pages [8] -->
m

<!-- b001664 | prose | pages [8] -->
m

<!-- b001665 | prose | pages [8] -->
m

<!-- b001666 | prose | pages [8] -->
m

<!-- b001667 | prose | pages [8] -->
m

<!-- b001668 | prose | pages [8] -->
m

<!-- b001669 | prose | pages [8] -->
m

<!-- b001670 | prose | pages [8] -->
m

<!-- b001671 | prose | pages [8] -->
m

<!-- b001672 | prose | pages [8] -->
m

<!-- b001673 | prose | pages [8] -->
m

<!-- b001674 | prose | pages [8] -->
m

<!-- b001675 | prose | pages [8] -->
m

<!-- b001676 | prose | pages [8] -->
m

<!-- b001677 | prose | pages [8] -->
m

<!-- b001678 | prose | pages [8] -->
m

<!-- b001679 | prose | pages [8] -->
m

<!-- b001680 | prose | pages [8] -->
m

<!-- b001681 | prose | pages [8] -->
m

<!-- b001682 | prose | pages [8] -->
m

<!-- b001683 | prose | pages [8] -->
m

<!-- b001684 | prose | pages [8] -->
m

<!-- b001685 | prose | pages [8] -->
m

<!-- b001686 | prose | pages [8] -->
m

<!-- b001687 | prose | pages [8] -->
m

<!-- b001688 | prose | pages [8] -->
m

<!-- b001689 | prose | pages [8] -->
m

<!-- b001690 | prose | pages [8] -->
m

<!-- b001691 | prose | pages [8] -->
m

<!-- b001692 | prose | pages [8] -->
m

<!-- b001693 | prose | pages [8] -->
m

<!-- b001694 | prose | pages [8] -->
m

<!-- b001695 | prose | pages [8] -->
m

<!-- b001696 | prose | pages [8] -->
m

<!-- b001697 | prose | pages [8] -->
m

<!-- b001698 | prose | pages [8] -->
m

<!-- b001699 | prose | pages [8] -->
m

<!-- b001700 | prose | pages [8] -->
m

<!-- b001701 | prose | pages [8] -->
m

<!-- b001702 | prose | pages [8] -->
m

<!-- b001703 | prose | pages [8] -->
m

<!-- b001704 | prose | pages [8] -->
m

<!-- b001705 | prose | pages [8] -->
m

<!-- b001706 | prose | pages [8] -->
m

<!-- b001707 | prose | pages [8] -->
m

<!-- b001708 | prose | pages [8] -->
m

<!-- b001709 | prose | pages [8] -->
m

<!-- b001710 | prose | pages [8] -->
m

<!-- b001711 | prose | pages [8] -->
m

<!-- b001712 | prose | pages [8] -->
m

<!-- b001713 | prose | pages [8] -->
m

<!-- b001714 | prose | pages [8] -->
m

<!-- b001715 | prose | pages [8] -->
m

<!-- b001716 | prose | pages [8] -->
m

<!-- b001717 | prose | pages [8] -->
m

<!-- b001718 | prose | pages [8] -->
m

<!-- b001719 | prose | pages [8] -->
m

<!-- b001720 | prose | pages [8] -->
m

<!-- b001721 | prose | pages [8] -->
m

<!-- b001722 | prose | pages [8] -->
m

<!-- b001723 | prose | pages [8] -->
m

<!-- b001724 | prose | pages [8] -->
m

<!-- b001725 | prose | pages [8] -->
m

<!-- b001726 | prose | pages [8] -->
m

<!-- b001727 | prose | pages [8] -->
m

<!-- b001728 | prose | pages [8] -->
m

<!-- b001729 | prose | pages [8] -->
m

<!-- b001730 | prose | pages [8] -->
m

<!-- b001731 | prose | pages [8] -->
m

<!-- b001732 | prose | pages [8] -->
m

<!-- b001733 | prose | pages [8] -->
m

<!-- b001734 | prose | pages [8] -->
m

<!-- b001735 | prose | pages [8] -->
m

<!-- b001736 | prose | pages [8] -->
m

<!-- b001737 | prose | pages [8] -->
m

<!-- b001738 | prose | pages [8] -->
m

<!-- b001739 | prose | pages [8] -->
m

<!-- b001740 | prose | pages [8] -->
m

<!-- b001741 | prose | pages [8] -->
m

<!-- b001742 | prose | pages [8] -->
m

<!-- b001743 | prose | pages [8] -->
m

<!-- b001744 | prose | pages [8] -->
m

<!-- b001745 | prose | pages [8] -->
m

<!-- b001746 | prose | pages [8] -->
m

<!-- b001747 | prose | pages [8] -->
m

<!-- b001748 | prose | pages [8] -->
m

<!-- b001749 | prose | pages [8] -->
m

<!-- b001750 | prose | pages [8] -->
m

<!-- b001751 | prose | pages [8] -->
m

<!-- b001752 | prose | pages [8] -->
m

<!-- b001753 | prose | pages [8] -->
m

<!-- b001754 | prose | pages [8] -->
m

<!-- b001755 | prose | pages [8] -->
m

<!-- b001756 | prose | pages [8] -->
m

<!-- b001757 | prose | pages [8] -->
m

<!-- b001758 | prose | pages [8] -->
m

<!-- b001759 | prose | pages [8] -->
m

<!-- b001760 | prose | pages [8] -->
m

<!-- b001761 | prose | pages [8] -->
m

<!-- b001762 | prose | pages [8] -->
m

<!-- b001763 | prose | pages [8] -->
m

<!-- b001764 | prose | pages [8] -->
m

<!-- b001765 | prose | pages [8] -->
m

<!-- b001766 | prose | pages [8] -->
m

<!-- b001767 | prose | pages [8] -->
m

<!-- b001768 | prose | pages [8] -->
m

<!-- b001769 | prose | pages [8] -->
m

<!-- b001770 | prose | pages [8] -->
m

<!-- b001771 | prose | pages [8] -->
m

<!-- b001772 | prose | pages [8] -->
m

<!-- b001773 | prose | pages [8] -->
m

<!-- b001774 | prose | pages [8] -->
m

<!-- b001775 | prose | pages [8] -->
m

<!-- b001776 | prose | pages [8] -->
m

<!-- b001777 | prose | pages [8] -->
m

<!-- b001778 | prose | pages [8] -->
m

<!-- b001779 | prose | pages [8] -->
m

<!-- b001780 | prose | pages [8] -->
m

<!-- b001781 | prose | pages [8] -->
m

<!-- b001782 | prose | pages [8] -->
m

<!-- b001783 | prose | pages [8] -->
m

<!-- b001784 | prose | pages [8] -->
m

<!-- b001785 | prose | pages [8] -->
m

<!-- b001786 | prose | pages [8] -->
m

<!-- b001787 | prose | pages [8] -->
m

<!-- b001788 | prose | pages [8] -->
m

<!-- b001789 | prose | pages [8] -->
m

<!-- b001790 | prose | pages [8] -->
m

<!-- b001791 | prose | pages [8] -->
m

<!-- b001792 | prose | pages [8] -->
m

<!-- b001793 | prose | pages [8] -->
m

<!-- b001794 | prose | pages [8] -->
m

<!-- b001795 | prose | pages [8] -->
m

<!-- b001796 | prose | pages [8] -->
m

<!-- b001797 | prose | pages [8] -->
m

<!-- b001798 | prose | pages [8] -->
m

<!-- b001799 | prose | pages [8] -->
m

<!-- b001800 | prose | pages [8] -->
m

<!-- b001801 | prose | pages [8] -->
m

<!-- b001802 | prose | pages [8] -->
m

<!-- b001803 | prose | pages [8] -->
m

<!-- b001804 | prose | pages [8] -->
m

<!-- b001805 | prose | pages [8] -->
m

<!-- b001806 | prose | pages [8] -->
m

<!-- b001807 | prose | pages [8] -->
m

<!-- b001808 | prose | pages [8] -->
m

<!-- b001809 | prose | pages [8] -->
m

<!-- b001810 | prose | pages [8] -->
m

<!-- b001811 | prose | pages [8] -->
m

<!-- b001812 | prose | pages [8] -->
m

<!-- b001813 | prose | pages [8] -->
m

<!-- b001814 | prose | pages [8] -->
m

<!-- b001815 | prose | pages [8] -->
m

<!-- b001816 | prose | pages [8] -->
m

<!-- b001817 | prose | pages [8] -->
m

<!-- b001818 | prose | pages [8] -->
m

<!-- b001819 | prose | pages [8] -->
m

<!-- b001820 | prose | pages [8] -->
m

<!-- b001821 | prose | pages [8] -->
m

<!-- b001822 | prose | pages [8] -->
m

<!-- b001823 | prose | pages [8] -->
m

<!-- b001824 | prose | pages [8] -->
m

<!-- b001825 | prose | pages [8] -->
m

<!-- b001826 | prose | pages [8] -->
m

<!-- b001827 | prose | pages [8] -->
m

<!-- b001828 | prose | pages [8] -->
m

<!-- b001829 | prose | pages [8] -->
m

<!-- b001830 | prose | pages [8] -->
m

<!-- b001831 | prose | pages [8] -->
m

<!-- b001832 | prose | pages [8] -->
m

<!-- b001833 | prose | pages [8] -->
m

<!-- b001834 | prose | pages [8] -->
m

<!-- b001835 | prose | pages [8] -->
m

<!-- b001836 | prose | pages [8] -->
m

<!-- b001837 | prose | pages [8] -->
m

<!-- b001838 | prose | pages [8] -->
m

<!-- b001839 | prose | pages [8] -->
m

<!-- b001840 | prose | pages [8] -->
m

<!-- b001841 | prose | pages [8] -->
m

<!-- b001842 | prose | pages [8] -->
m

<!-- b001843 | prose | pages [8] -->
m

<!-- b001844 | prose | pages [8] -->
m

<!-- b001845 | prose | pages [8] -->
m

<!-- b001846 | prose | pages [8] -->
m

<!-- b001847 | prose | pages [8] -->
m

<!-- b001848 | prose | pages [8] -->
m

<!-- b001849 | prose | pages [8] -->
m

<!-- b001850 | prose | pages [8] -->
m

<!-- b001851 | prose | pages [8] -->
m

<!-- b001852 | prose | pages [8] -->
m

<!-- b001853 | prose | pages [8] -->
m

<!-- b001854 | prose | pages [8] -->
m

<!-- b001855 | prose | pages [8] -->
m

<!-- b001856 | prose | pages [8] -->
m

<!-- b001857 | prose | pages [8] -->
m

<!-- b001858 | prose | pages [8] -->
m

<!-- b001859 | prose | pages [8] -->
m

<!-- b001860 | prose | pages [8] -->
m

<!-- b001861 | prose | pages [8] -->
m

<!-- b001862 | prose | pages [8] -->
m

<!-- b001863 | prose | pages [8] -->
m

<!-- b001864 | prose | pages [8] -->
m

<!-- b001865 | prose | pages [8] -->
m

<!-- b001866 | prose | pages [8] -->
m

<!-- b001867 | prose | pages [8] -->
m

<!-- b001868 | prose | pages [8] -->
m

<!-- b001869 | prose | pages [8] -->
m

<!-- b001870 | prose | pages [8] -->
m

<!-- b001871 | prose | pages [8] -->
m

<!-- b001872 | prose | pages [8] -->
m

<!-- b001873 | prose | pages [8] -->
m

<!-- b001874 | prose | pages [8] -->
m

<!-- b001875 | prose | pages [8] -->
m

<!-- b001876 | prose | pages [8] -->
m

<!-- b001877 | prose | pages [8] -->
m

<!-- b001878 | prose | pages [8] -->
m

<!-- b001879 | prose | pages [8] -->
m

<!-- b001880 | prose | pages [8] -->
m

<!-- b001881 | prose | pages [8] -->
m

<!-- b001882 | prose | pages [8] -->
m

<!-- b001883 | prose | pages [8] -->
m

<!-- b001884 | prose | pages [8] -->
m

<!-- b001885 | prose | pages [8] -->
m

<!-- b001886 | prose | pages [8] -->
m

<!-- b001887 | prose | pages [8] -->
m

<!-- b001888 | prose | pages [8] -->
m

<!-- b001889 | prose | pages [8] -->
m

<!-- b001890 | prose | pages [8] -->
m

<!-- b001891 | prose | pages [8] -->
m

<!-- b001892 | prose | pages [8] -->
m

<!-- b001893 | prose | pages [8] -->
m

<!-- b001894 | prose | pages [8] -->
m

<!-- b001895 | prose | pages [8] -->
m

<!-- b001896 | prose | pages [8] -->
m

<!-- b001897 | prose | pages [8] -->
m

<!-- b001898 | prose | pages [8] -->
m

<!-- b001899 | prose | pages [8] -->
m

<!-- b001900 | prose | pages [8] -->
m

<!-- b001901 | prose | pages [8] -->
m

<!-- b001902 | prose | pages [8] -->
m

<!-- b001903 | prose | pages [8] -->
m

<!-- b001904 | prose | pages [8] -->
m

<!-- b001905 | prose | pages [8] -->
m

<!-- b001906 | prose | pages [8] -->
m

<!-- b001907 | prose | pages [8] -->
m

<!-- b001908 | prose | pages [8] -->
m

<!-- b001909 | prose | pages [8] -->
m

<!-- b001910 | prose | pages [8] -->
m

<!-- b001911 | prose | pages [8] -->
m

<!-- b001912 | prose | pages [8] -->
m

<!-- b001913 | prose | pages [8] -->
m

<!-- b001914 | prose | pages [8] -->
m

<!-- b001915 | prose | pages [8] -->
m

<!-- b001916 | prose | pages [8] -->
m

<!-- b001917 | prose | pages [8] -->
m

<!-- b001918 | prose | pages [8] -->
m

<!-- b001919 | prose | pages [8] -->
m

<!-- b001920 | prose | pages [8] -->
m

<!-- b001921 | prose | pages [8] -->
m

<!-- b001922 | prose | pages [8] -->
m

<!-- b001923 | prose | pages [8] -->
m

<!-- b001924 | prose | pages [8] -->
m

<!-- b001925 | prose | pages [8] -->
m

<!-- b001926 | prose | pages [8] -->
m

<!-- b001927 | prose | pages [8] -->
m

<!-- b001928 | prose | pages [8] -->
m

<!-- b001929 | prose | pages [8] -->
m

<!-- b001930 | prose | pages [8] -->
m

<!-- b001931 | prose | pages [8] -->
m

<!-- b001932 | prose | pages [8] -->
m

<!-- b001933 | prose | pages [8] -->
m

<!-- b001934 | prose | pages [8] -->
m

<!-- b001935 | prose | pages [8] -->
m

<!-- b001936 | prose | pages [8] -->
m

<!-- b001937 | prose | pages [8] -->
m

<!-- b001938 | prose | pages [8] -->
m

<!-- b001939 | prose | pages [8] -->
m

<!-- b001940 | prose | pages [8] -->
m

<!-- b001941 | prose | pages [8] -->
m

<!-- b001942 | prose | pages [8] -->
m

<!-- b001943 | prose | pages [8] -->
m

<!-- b001944 | prose | pages [8] -->
m

<!-- b001945 | prose | pages [8] -->
m

<!-- b001946 | prose | pages [8] -->
m

<!-- b001947 | prose | pages [8] -->
m

<!-- b001948 | prose | pages [8] -->
m

<!-- b001949 | prose | pages [8] -->
m

<!-- b001950 | prose | pages [8] -->
m

<!-- b001951 | prose | pages [8] -->
m

<!-- b001952 | prose | pages [8] -->
m

<!-- b001953 | prose | pages [8] -->
m

<!-- b001954 | prose | pages [8] -->
m

<!-- b001955 | prose | pages [8] -->
m

<!-- b001956 | prose | pages [8] -->
m

<!-- b001957 | prose | pages [8] -->
m

<!-- b001958 | prose | pages [8] -->
m

<!-- b001959 | prose | pages [8] -->
m

<!-- b001960 | prose | pages [8] -->
m

<!-- b001961 | prose | pages [8] -->
m

<!-- b001962 | prose | pages [8] -->
m

<!-- b001963 | prose | pages [8] -->
m

<!-- b001964 | prose | pages [8] -->
m

<!-- b001965 | prose | pages [8] -->
m

<!-- b001966 | prose | pages [8] -->
m

<!-- b001967 | prose | pages [8] -->
m

<!-- b001968 | prose | pages [8] -->
m

<!-- b001969 | prose | pages [8] -->
m

<!-- b001970 | prose | pages [8] -->
m

<!-- b001971 | prose | pages [8] -->
m

<!-- b001972 | prose | pages [8] -->
m

<!-- b001973 | prose | pages [8] -->
m

<!-- b001974 | prose | pages [8] -->
m

<!-- b001975 | prose | pages [8] -->
m

<!-- b001976 | prose | pages [8] -->
m

<!-- b001977 | prose | pages [8] -->
m

<!-- b001978 | prose | pages [8] -->
m

<!-- b001979 | prose | pages [8] -->
m

<!-- b001980 | prose | pages [8] -->
m

<!-- b001981 | prose | pages [8] -->
m

<!-- b001982 | prose | pages [8] -->
m

<!-- b001983 | prose | pages [8] -->
m

<!-- b001984 | prose | pages [8] -->
m

<!-- b001985 | prose | pages [8] -->
m

<!-- b001986 | prose | pages [8] -->
m

<!-- b001987 | prose | pages [8] -->
m

<!-- b001988 | prose | pages [8] -->
m

<!-- b001989 | prose | pages [8] -->
m

<!-- b001990 | prose | pages [8] -->
m

<!-- b001991 | prose | pages [8] -->
m

<!-- b001992 | prose | pages [8] -->
m

<!-- b001993 | prose | pages [8] -->
m

<!-- b001994 | prose | pages [8] -->
m

<!-- b001995 | prose | pages [8] -->
m

<!-- b001996 | prose | pages [8] -->
One critical aspect of glacier health is the Equilibrium Line Altitude (ELA), which represents the altitude on a glacier where accumulation and ablation are balanced. According to the study by Braithwaite et al. [1], changes in ELA are driven primarily by temperature and precipitation. As the ELA rises, it reﬂects increased glacier melting and reduced stability. Similarly, another study by Oerlemans [2] highlights that ELA is a key indicator of glacier health and is directly aﬀected by climatic variations.

<!-- b001997 | prose | pages [8] -->
The ELA is inﬂuenced by feedback mechanisms within the glacier itself. For instance, the albedo eﬀect causes melting glaciers to absorb more solar radiation as their surface darkens, further acceler- ating the loss of ice. This intrinsic dependency makes the ELA height of glacier HJuneau sensitive to its prior state, represented in the model by k1HJuneau.

<!-- b001998 | prose | pages [8] -->
Tourism signiﬁcantly aﬀects glacier health. Increased tourist numbers NJuneau can lead to en- vironmental degradation through waste, infrastructure development, and direct interaction with the glacier environment. These impacts are proportional to both the existing glacier health and the level of tourism, captured in the term k2HJuneauNJuneau.

<!-- b001999 | prose | pages [8] -->
Economic factors, such as investments in preservation funded by hotel tax revenue TJuneau, also play a vital role in mitigating the negative eﬀects of tourism. Higher revenues enable conservation projects, such as restricting access to sensitive areas or implementing restoration eﬀorts. This dynamic is mod- eled as k3TJuneauHJuneau, showing how economic resources contribute to sustaining glacier health.

<!-- b002000 | prose | pages [8] -->
Bringing these factors together, the equation governing glacier health HJuneau is expressed as:

<!-- b002001 | prose | pages [8] -->
dHJuneau

<!-- b002002 | prose | pages [8] -->
= k1HJuneau + k2HJuneauNJuneau + k3TJuneauHJuneau. dt (1)

<!-- b002003 | prose | pages [8] -->
Here, k1 represents the intrinsic changes in glacier health due to natural processes, k2 quantiﬁes the impact of tourism, and k3 captures the restorative eﬀects of economic investments.

<!-- b002004 | prose | pages [8] -->
关注数学模型

<!-- b002005 | furniture | pages [8] -->
2

<!-- b002006 | furniture | pages [8] -->
MATHmodels

<!-- b002007 | furniture | pages [8] -->
获取更多资讯

<!-- b002008 | furniture | pages [9] -->
Team # 2503268

<!-- b002009 | prose | pages [9] -->
5.1.2 Tourist Number Dynamics

<!-- b002010 | furniture | pages [9] -->
Page 7 of 24

<!-- b002011 | prose | pages [9] -->
The dynamics of tourist numbers NJuneau are governed by both natural growth patterns and their in- teraction with the glacier environment. According to Verhulst’s logistic model [3], population growth typically follows an S-shaped curve, with initial exponential growth slowing as it approaches the car-

<!-- b002012 | prose | pages [9] -->
!

<!-- b002013 | prose | pages [9] -->
"

<!-- b002014 | prose | pages [9] -->
微信公众号：数学模型

<!-- b002015 | prose | pages [9] -->
1 ↓NJuneau

<!-- b002016 | prose | pages [9] -->
rying capacity K. This relationship is represented by the term r1NJuneau

<!-- b002017 | prose | pages [9] -->
, where r1 is the

<!-- b002018 | prose | pages [9] -->
K

<!-- b002019 | prose | pages [9] -->
intrinsic growth rate and K is the environmental or infrastructural limit for tourist numbers.

<!-- b002020 | prose | pages [9] -->
The health of the glacier environment HJuneau also plays a critical role in attracting tourists. Re- search by Buckley [4] shows that pristine natural environments signiﬁcantly boost tourism demand. This inﬂuence is captured by the term k4HJuneauNJuneau, which indicates that better glacier health am- pliﬁes tourist numbers.

<!-- b002021 | prose | pages [9] -->
Combining these factors, the equation for tourist numbers NJuneau is expressed as:

<!-- b002022 | prose | pages [9] -->
#

<!-- b002023 | prose | pages [9] -->
$

<!-- b002024 | prose | pages [9] -->
1 ↓NJuneau

<!-- b002025 | prose | pages [9] -->
dNJuneau

<!-- b002026 | prose | pages [9] -->
= r1NJuneau dt

<!-- b002027 | prose | pages [9] -->
+ k4HJuneauNJuneau.

<!-- b002028 | prose | pages [9] -->
(2)

<!-- b002029 | prose | pages [9] -->
K

<!-- b002030 | prose | pages [9] -->
微信号：MATHmodels

<!-- b002031 | prose | pages [9] -->
Here, r1 represents the natural growth rate of tourism, constrained by the carrying capacity K, while k4 quantiﬁes the positive impact of glacier health HJuneau on tourism growth. Together, these terms de- scribe the interplay between environmental conditions and tourism dynamics, providing a framework to assess the sustainability of tourism in glacier regions.

<!-- b002032 | prose | pages [9] -->
5.1.3 Economic Dynamics

<!-- b002033 | prose | pages [9] -->
The dynamics of annual hotel tax revenue TJuneau are closely tied to tourism and economic factors. According to studies on tourism-driven economies [5], the revenue generated from hotel taxes is di- rectly proportional to the number of tourists. This relationship is captured by the term k6NJuneau, which indicates that an increase in tourist numbers NJuneau results in higher tax revenue.

<!-- b002034 | prose | pages [9] -->
In addition, economic growth independent of tourism also plays a role. Research by Frechtling [6] shows that baseline economic trends contribute to steady growth in tax revenue, even in the absence of signiﬁcant changes in tourism. This baseline growth is represented by the term k5TJuneau, which accounts for general economic development and inﬂationary factors.

<!-- b002035 | prose | pages [9] -->
Combining these inﬂuences, the equation for hotel tax revenue TJuneau is expressed as:

<!-- b002036 | prose | pages [9] -->
dTJuneau

<!-- b002037 | prose | pages [9] -->
= k5TJuneau + k6NJuneau. dt (3)

<!-- b002038 | prose | pages [9] -->
Here, k5 represents the baseline economic growth, while k6 quantiﬁes the direct contribution of tourist numbers NJuneau to tax revenue.

<!-- b002039 | heading | pages [9] -->
Model Integration and Parameter Estimation

<!-- b002040 | prose | pages [9] -->
5.1.4

<!-- b002041 | prose | pages [9] -->
To evaluate the interconnected dynamics of glacier health, tourist numbers, and hotel tax revenue, we integrate the above equations into a single system. Using data from 2010 to 2019, we estimate the parameters ki and ri through nonlinear regression. Due to the complexity of real-world systems, these parameters are inﬂuenced not only by the core variables but also by external, unmeasured factors. Speciﬁcally, the anomalous marine heatwave event known as “The Blob” in 2013 signiﬁcantly aﬀected

<!-- b002042 | prose | pages [9] -->
m

<!-- b002043 | prose | pages [9] -->
m

<!-- b002044 | prose | pages [9] -->
m

<!-- b002045 | prose | pages [9] -->
m

<!-- b002046 | prose | pages [9] -->
m

<!-- b002047 | prose | pages [9] -->
m

<!-- b002048 | prose | pages [9] -->
m

<!-- b002049 | prose | pages [9] -->
m

<!-- b002050 | prose | pages [9] -->
m

<!-- b002051 | prose | pages [9] -->
m

<!-- b002052 | prose | pages [9] -->
m

<!-- b002053 | prose | pages [9] -->
m

<!-- b002054 | prose | pages [9] -->
m

<!-- b002055 | prose | pages [9] -->
m

<!-- b002056 | prose | pages [9] -->
m

<!-- b002057 | prose | pages [9] -->
m

<!-- b002058 | prose | pages [9] -->
m

<!-- b002059 | prose | pages [9] -->
m

<!-- b002060 | prose | pages [9] -->
m

<!-- b002061 | prose | pages [9] -->
m

<!-- b002062 | prose | pages [9] -->
m

<!-- b002063 | prose | pages [9] -->
m

<!-- b002064 | prose | pages [9] -->
m

<!-- b002065 | prose | pages [9] -->
m

<!-- b002066 | prose | pages [9] -->
m

<!-- b002067 | prose | pages [9] -->
m

<!-- b002068 | prose | pages [9] -->
m

<!-- b002069 | prose | pages [9] -->
m

<!-- b002070 | prose | pages [9] -->
m

<!-- b002071 | prose | pages [9] -->
m

<!-- b002072 | prose | pages [9] -->
m

<!-- b002073 | prose | pages [9] -->
m

<!-- b002074 | prose | pages [9] -->
m

<!-- b002075 | prose | pages [9] -->
m

<!-- b002076 | prose | pages [9] -->
m

<!-- b002077 | prose | pages [9] -->
m

<!-- b002078 | prose | pages [9] -->
m

<!-- b002079 | prose | pages [9] -->
m

<!-- b002080 | prose | pages [9] -->
m

<!-- b002081 | prose | pages [9] -->
m

<!-- b002082 | prose | pages [9] -->
m

<!-- b002083 | prose | pages [9] -->
m

<!-- b002084 | prose | pages [9] -->
m

<!-- b002085 | prose | pages [9] -->
m

<!-- b002086 | prose | pages [9] -->
m

<!-- b002087 | prose | pages [9] -->
m

<!-- b002088 | prose | pages [9] -->
m

<!-- b002089 | prose | pages [9] -->
m

<!-- b002090 | prose | pages [9] -->
m

<!-- b002091 | prose | pages [9] -->
m

<!-- b002092 | prose | pages [9] -->
m

<!-- b002093 | prose | pages [9] -->
m

<!-- b002094 | prose | pages [9] -->
m

<!-- b002095 | prose | pages [9] -->
m

<!-- b002096 | prose | pages [9] -->
m

<!-- b002097 | prose | pages [9] -->
m

<!-- b002098 | prose | pages [9] -->
m

<!-- b002099 | prose | pages [9] -->
m

<!-- b002100 | prose | pages [9] -->
m

<!-- b002101 | prose | pages [9] -->
m

<!-- b002102 | prose | pages [9] -->
m

<!-- b002103 | prose | pages [9] -->
m

<!-- b002104 | prose | pages [9] -->
m

<!-- b002105 | prose | pages [9] -->
m

<!-- b002106 | prose | pages [9] -->
m

<!-- b002107 | prose | pages [9] -->
m

<!-- b002108 | prose | pages [9] -->
m

<!-- b002109 | prose | pages [9] -->
m

<!-- b002110 | prose | pages [9] -->
m

<!-- b002111 | prose | pages [9] -->
m

<!-- b002112 | prose | pages [9] -->
m

<!-- b002113 | prose | pages [9] -->
m

<!-- b002114 | prose | pages [9] -->
m

<!-- b002115 | prose | pages [9] -->
m

<!-- b002116 | prose | pages [9] -->
m

<!-- b002117 | prose | pages [9] -->
m

<!-- b002118 | prose | pages [9] -->
m

<!-- b002119 | prose | pages [9] -->
m

<!-- b002120 | prose | pages [9] -->
m

<!-- b002121 | prose | pages [9] -->
m

<!-- b002122 | prose | pages [9] -->
m

<!-- b002123 | prose | pages [9] -->
m

<!-- b002124 | prose | pages [9] -->
m

<!-- b002125 | prose | pages [9] -->
m

<!-- b002126 | prose | pages [9] -->
m

<!-- b002127 | prose | pages [9] -->
m

<!-- b002128 | prose | pages [9] -->
m

<!-- b002129 | prose | pages [9] -->
m

<!-- b002130 | prose | pages [9] -->
m

<!-- b002131 | prose | pages [9] -->
m

<!-- b002132 | prose | pages [9] -->
m

<!-- b002133 | prose | pages [9] -->
m

<!-- b002134 | prose | pages [9] -->
m

<!-- b002135 | prose | pages [9] -->
m

<!-- b002136 | prose | pages [9] -->
m

<!-- b002137 | prose | pages [9] -->
m

<!-- b002138 | prose | pages [9] -->
m

<!-- b002139 | prose | pages [9] -->
m

<!-- b002140 | prose | pages [9] -->
m

<!-- b002141 | prose | pages [9] -->
m

<!-- b002142 | prose | pages [9] -->
m

<!-- b002143 | prose | pages [9] -->
m

<!-- b002144 | prose | pages [9] -->
m

<!-- b002145 | prose | pages [9] -->
m

<!-- b002146 | prose | pages [9] -->
m

<!-- b002147 | prose | pages [9] -->
m

<!-- b002148 | prose | pages [9] -->
m

<!-- b002149 | prose | pages [9] -->
m

<!-- b002150 | prose | pages [9] -->
m

<!-- b002151 | prose | pages [9] -->
m

<!-- b002152 | prose | pages [9] -->
m

<!-- b002153 | prose | pages [9] -->
m

<!-- b002154 | prose | pages [9] -->
m

<!-- b002155 | prose | pages [9] -->
m

<!-- b002156 | prose | pages [9] -->
m

<!-- b002157 | prose | pages [9] -->
m

<!-- b002158 | prose | pages [9] -->
m

<!-- b002159 | prose | pages [9] -->
m

<!-- b002160 | prose | pages [9] -->
m

<!-- b002161 | prose | pages [9] -->
m

<!-- b002162 | prose | pages [9] -->
m

<!-- b002163 | prose | pages [9] -->
m

<!-- b002164 | prose | pages [9] -->
m

<!-- b002165 | prose | pages [9] -->
m

<!-- b002166 | prose | pages [9] -->
m

<!-- b002167 | prose | pages [9] -->
m

<!-- b002168 | prose | pages [9] -->
m

<!-- b002169 | prose | pages [9] -->
m

<!-- b002170 | prose | pages [9] -->
m

<!-- b002171 | prose | pages [9] -->
m

<!-- b002172 | prose | pages [9] -->
m

<!-- b002173 | prose | pages [9] -->
m

<!-- b002174 | prose | pages [9] -->
m

<!-- b002175 | prose | pages [9] -->
m

<!-- b002176 | prose | pages [9] -->
m

<!-- b002177 | prose | pages [9] -->
m

<!-- b002178 | prose | pages [9] -->
m

<!-- b002179 | prose | pages [9] -->
m

<!-- b002180 | prose | pages [9] -->
m

<!-- b002181 | prose | pages [9] -->
m

<!-- b002182 | prose | pages [9] -->
m

<!-- b002183 | prose | pages [9] -->
m

<!-- b002184 | prose | pages [9] -->
m

<!-- b002185 | prose | pages [9] -->
m

<!-- b002186 | prose | pages [9] -->
m

<!-- b002187 | prose | pages [9] -->
m

<!-- b002188 | prose | pages [9] -->
m

<!-- b002189 | prose | pages [9] -->
m

<!-- b002190 | prose | pages [9] -->
m

<!-- b002191 | prose | pages [9] -->
m

<!-- b002192 | prose | pages [9] -->
m

<!-- b002193 | prose | pages [9] -->
m

<!-- b002194 | prose | pages [9] -->
m

<!-- b002195 | prose | pages [9] -->
m

<!-- b002196 | prose | pages [9] -->
m

<!-- b002197 | prose | pages [9] -->
m

<!-- b002198 | prose | pages [9] -->
m

<!-- b002199 | prose | pages [9] -->
m

<!-- b002200 | prose | pages [9] -->
m

<!-- b002201 | prose | pages [9] -->
m

<!-- b002202 | prose | pages [9] -->
m

<!-- b002203 | prose | pages [9] -->
m

<!-- b002204 | prose | pages [9] -->
m

<!-- b002205 | prose | pages [9] -->
m

<!-- b002206 | prose | pages [9] -->
m

<!-- b002207 | prose | pages [9] -->
m

<!-- b002208 | prose | pages [9] -->
m

<!-- b002209 | prose | pages [9] -->
m

<!-- b002210 | prose | pages [9] -->
m

<!-- b002211 | prose | pages [9] -->
m

<!-- b002212 | prose | pages [9] -->
m

<!-- b002213 | prose | pages [9] -->
m

<!-- b002214 | prose | pages [9] -->
m

<!-- b002215 | prose | pages [9] -->
m

<!-- b002216 | prose | pages [9] -->
m

<!-- b002217 | prose | pages [9] -->
m

<!-- b002218 | prose | pages [9] -->
m

<!-- b002219 | prose | pages [9] -->
m

<!-- b002220 | prose | pages [9] -->
m

<!-- b002221 | prose | pages [9] -->
m

<!-- b002222 | prose | pages [9] -->
m

<!-- b002223 | prose | pages [9] -->
m

<!-- b002224 | prose | pages [9] -->
m

<!-- b002225 | prose | pages [9] -->
m

<!-- b002226 | prose | pages [9] -->
m

<!-- b002227 | prose | pages [9] -->
m

<!-- b002228 | prose | pages [9] -->
m

<!-- b002229 | prose | pages [9] -->
m

<!-- b002230 | prose | pages [9] -->
m

<!-- b002231 | prose | pages [9] -->
m

<!-- b002232 | prose | pages [9] -->
m

<!-- b002233 | prose | pages [9] -->
m

<!-- b002234 | prose | pages [9] -->
m

<!-- b002235 | prose | pages [9] -->
m

<!-- b002236 | prose | pages [9] -->
m

<!-- b002237 | prose | pages [9] -->
m

<!-- b002238 | prose | pages [9] -->
m

<!-- b002239 | prose | pages [9] -->
m

<!-- b002240 | prose | pages [9] -->
m

<!-- b002241 | prose | pages [9] -->
m

<!-- b002242 | prose | pages [9] -->
m

<!-- b002243 | prose | pages [9] -->
m

<!-- b002244 | prose | pages [9] -->
m

<!-- b002245 | prose | pages [9] -->
m

<!-- b002246 | prose | pages [9] -->
m

<!-- b002247 | prose | pages [9] -->
m

<!-- b002248 | prose | pages [9] -->
m

<!-- b002249 | prose | pages [9] -->
m

<!-- b002250 | prose | pages [9] -->
m

<!-- b002251 | prose | pages [9] -->
m

<!-- b002252 | prose | pages [9] -->
m

<!-- b002253 | prose | pages [9] -->
m

<!-- b002254 | prose | pages [9] -->
m

<!-- b002255 | prose | pages [9] -->
m

<!-- b002256 | prose | pages [9] -->
m

<!-- b002257 | prose | pages [9] -->
m

<!-- b002258 | prose | pages [9] -->
m

<!-- b002259 | prose | pages [9] -->
m

<!-- b002260 | prose | pages [9] -->
m

<!-- b002261 | prose | pages [9] -->
m

<!-- b002262 | prose | pages [9] -->
m

<!-- b002263 | prose | pages [9] -->
m

<!-- b002264 | prose | pages [9] -->
m

<!-- b002265 | prose | pages [9] -->
m

<!-- b002266 | prose | pages [9] -->
m

<!-- b002267 | prose | pages [9] -->
m

<!-- b002268 | prose | pages [9] -->
m

<!-- b002269 | prose | pages [9] -->
m

<!-- b002270 | prose | pages [9] -->
m

<!-- b002271 | prose | pages [9] -->
m

<!-- b002272 | prose | pages [9] -->
m

<!-- b002273 | prose | pages [9] -->
m

<!-- b002274 | prose | pages [9] -->
m

<!-- b002275 | prose | pages [9] -->
m

<!-- b002276 | prose | pages [9] -->
m

<!-- b002277 | prose | pages [9] -->
m

<!-- b002278 | prose | pages [9] -->
m

<!-- b002279 | prose | pages [9] -->
m

<!-- b002280 | prose | pages [9] -->
m

<!-- b002281 | prose | pages [9] -->
m

<!-- b002282 | prose | pages [9] -->
m

<!-- b002283 | prose | pages [9] -->
m

<!-- b002284 | prose | pages [9] -->
m

<!-- b002285 | prose | pages [9] -->
m

<!-- b002286 | prose | pages [9] -->
m

<!-- b002287 | prose | pages [9] -->
m

<!-- b002288 | prose | pages [9] -->
m

<!-- b002289 | prose | pages [9] -->
m

<!-- b002290 | prose | pages [9] -->
m

<!-- b002291 | prose | pages [9] -->
m

<!-- b002292 | prose | pages [9] -->
m

<!-- b002293 | prose | pages [9] -->
m

<!-- b002294 | prose | pages [9] -->
m

<!-- b002295 | prose | pages [9] -->
m

<!-- b002296 | prose | pages [9] -->
m

<!-- b002297 | prose | pages [9] -->
m

<!-- b002298 | prose | pages [9] -->
m

<!-- b002299 | prose | pages [9] -->
m

<!-- b002300 | prose | pages [9] -->
m

<!-- b002301 | prose | pages [9] -->
m

<!-- b002302 | prose | pages [9] -->
m

<!-- b002303 | prose | pages [9] -->
m

<!-- b002304 | prose | pages [9] -->
m

<!-- b002305 | prose | pages [9] -->
m

<!-- b002306 | prose | pages [9] -->
m

<!-- b002307 | prose | pages [9] -->
m

<!-- b002308 | prose | pages [9] -->
m

<!-- b002309 | prose | pages [9] -->
m

<!-- b002310 | prose | pages [9] -->
m

<!-- b002311 | prose | pages [9] -->
m

<!-- b002312 | prose | pages [9] -->
m

<!-- b002313 | prose | pages [9] -->
m

<!-- b002314 | prose | pages [9] -->
m

<!-- b002315 | prose | pages [9] -->
m

<!-- b002316 | prose | pages [9] -->
m

<!-- b002317 | prose | pages [9] -->
m

<!-- b002318 | prose | pages [9] -->
m

<!-- b002319 | prose | pages [9] -->
m

<!-- b002320 | prose | pages [9] -->
m

<!-- b002321 | prose | pages [9] -->
m

<!-- b002322 | prose | pages [9] -->
m

<!-- b002323 | prose | pages [9] -->
m

<!-- b002324 | prose | pages [9] -->
m

<!-- b002325 | prose | pages [9] -->
m

<!-- b002326 | furniture | pages [9] -->
m

<!-- b002327 | furniture | pages [9] -->
m

<!-- b002328 | furniture | pages [9] -->
m

<!-- b002329 | furniture | pages [9] -->
m

<!-- b002330 | furniture | pages [9] -->
m

<!-- b002331 | furniture | pages [9] -->
m

<!-- b002332 | furniture | pages [9] -->
m

<!-- b002333 | furniture | pages [9] -->
m

<!-- b002334 | furniture | pages [9] -->
m

<!-- b002335 | furniture | pages [9] -->
m

<!-- b002336 | furniture | pages [9] -->
m

<!-- b002337 | furniture | pages [9] -->
m

<!-- b002338 | furniture | pages [9] -->
m

<!-- b002339 | furniture | pages [9] -->
m

<!-- b002340 | furniture | pages [9] -->
m

<!-- b002341 | furniture | pages [9] -->
m

<!-- b002342 | furniture | pages [9] -->
m

<!-- b002343 | furniture | pages [9] -->
m

<!-- b002344 | furniture | pages [9] -->
m

<!-- b002345 | furniture | pages [9] -->
m

<!-- b002346 | furniture | pages [9] -->
m

<!-- b002347 | furniture | pages [9] -->
m

<!-- b002348 | furniture | pages [9] -->
m

<!-- b002349 | furniture | pages [9] -->
m

<!-- b002350 | furniture | pages [9] -->
m

<!-- b002351 | furniture | pages [9] -->
m

<!-- b002352 | furniture | pages [9] -->
m

<!-- b002353 | furniture | pages [9] -->
m

<!-- b002354 | furniture | pages [9] -->
m

<!-- b002355 | furniture | pages [9] -->
m

<!-- b002356 | furniture | pages [9] -->
m

<!-- b002357 | furniture | pages [9] -->
m

<!-- b002358 | furniture | pages [9] -->
m

<!-- b002359 | furniture | pages [9] -->
m

<!-- b002360 | furniture | pages [9] -->
m

<!-- b002361 | furniture | pages [9] -->
m

<!-- b002362 | furniture | pages [9] -->
m

<!-- b002363 | furniture | pages [9] -->
m

<!-- b002364 | furniture | pages [9] -->
m

<!-- b002365 | furniture | pages [9] -->
m

<!-- b002366 | furniture | pages [9] -->
m

<!-- b002367 | furniture | pages [9] -->
m

<!-- b002368 | furniture | pages [9] -->
m

<!-- b002369 | furniture | pages [9] -->
m

<!-- b002370 | furniture | pages [9] -->
m

<!-- b002371 | furniture | pages [9] -->
m

<!-- b002372 | furniture | pages [9] -->
m

<!-- b002373 | furniture | pages [9] -->
m

<!-- b002374 | furniture | pages [9] -->
m

<!-- b002375 | furniture | pages [9] -->
m

<!-- b002376 | furniture | pages [9] -->
m

<!-- b002377 | furniture | pages [9] -->
m

<!-- b002378 | furniture | pages [9] -->
m

<!-- b002379 | furniture | pages [9] -->
m

<!-- b002380 | furniture | pages [9] -->
m

<!-- b002381 | furniture | pages [9] -->
m

<!-- b002382 | furniture | pages [9] -->
m

<!-- b002383 | furniture | pages [9] -->
m

<!-- b002384 | furniture | pages [9] -->
m

<!-- b002385 | furniture | pages [9] -->
m

<!-- b002386 | furniture | pages [9] -->
m

<!-- b002387 | furniture | pages [9] -->
m

<!-- b002388 | furniture | pages [9] -->
m

<!-- b002389 | furniture | pages [9] -->
m

<!-- b002390 | furniture | pages [9] -->
m

<!-- b002391 | furniture | pages [9] -->
m

<!-- b002392 | furniture | pages [9] -->
m

<!-- b002393 | furniture | pages [9] -->
m

<!-- b002394 | furniture | pages [9] -->
m

<!-- b002395 | furniture | pages [9] -->
m

<!-- b002396 | furniture | pages [9] -->
m

<!-- b002397 | furniture | pages [9] -->
m

<!-- b002398 | furniture | pages [9] -->
m

<!-- b002399 | furniture | pages [9] -->
m

<!-- b002400 | furniture | pages [9] -->
m

<!-- b002401 | furniture | pages [9] -->
m

<!-- b002402 | furniture | pages [9] -->
m

<!-- b002403 | furniture | pages [9] -->
m

<!-- b002404 | furniture | pages [9] -->
m

<!-- b002405 | furniture | pages [9] -->
m

<!-- b002406 | furniture | pages [9] -->
m

<!-- b002407 | furniture | pages [9] -->
m

<!-- b002408 | furniture | pages [9] -->
m

<!-- b002409 | furniture | pages [9] -->
m

<!-- b002410 | furniture | pages [9] -->
m

<!-- b002411 | furniture | pages [9] -->
m

<!-- b002412 | furniture | pages [9] -->
m

<!-- b002413 | furniture | pages [9] -->
m

<!-- b002414 | furniture | pages [9] -->
m

<!-- b002415 | furniture | pages [9] -->
m

<!-- b002416 | furniture | pages [9] -->
m

<!-- b002417 | furniture | pages [9] -->
m

<!-- b002418 | furniture | pages [9] -->
m

<!-- b002419 | furniture | pages [9] -->
m

<!-- b002420 | furniture | pages [9] -->
m

<!-- b002421 | furniture | pages [9] -->
m

<!-- b002422 | furniture | pages [9] -->
m

<!-- b002423 | furniture | pages [9] -->
m

<!-- b002424 | furniture | pages [9] -->
m

<!-- b002425 | furniture | pages [9] -->
m

<!-- b002426 | furniture | pages [9] -->
m

<!-- b002427 | furniture | pages [9] -->
m

<!-- b002428 | furniture | pages [9] -->
m

<!-- b002429 | furniture | pages [9] -->
m

<!-- b002430 | furniture | pages [9] -->
m

<!-- b002431 | furniture | pages [9] -->
m

<!-- b002432 | furniture | pages [9] -->
m

<!-- b002433 | furniture | pages [9] -->
m

<!-- b002434 | furniture | pages [9] -->
m

<!-- b002435 | furniture | pages [9] -->
m

<!-- b002436 | furniture | pages [9] -->
m

<!-- b002437 | furniture | pages [9] -->
m

<!-- b002438 | furniture | pages [9] -->
m

<!-- b002439 | furniture | pages [9] -->
m

<!-- b002440 | furniture | pages [9] -->
m

<!-- b002441 | furniture | pages [9] -->
m

<!-- b002442 | furniture | pages [9] -->
m

<!-- b002443 | furniture | pages [9] -->
m

<!-- b002444 | furniture | pages [9] -->
m

<!-- b002445 | furniture | pages [9] -->
m

<!-- b002446 | furniture | pages [9] -->
m

<!-- b002447 | furniture | pages [9] -->
m

<!-- b002448 | furniture | pages [9] -->
m

<!-- b002449 | furniture | pages [9] -->
m

<!-- b002450 | furniture | pages [9] -->
m

<!-- b002451 | furniture | pages [9] -->
m

<!-- b002452 | furniture | pages [9] -->
m

<!-- b002453 | furniture | pages [9] -->
m

<!-- b002454 | furniture | pages [9] -->
m

<!-- b002455 | furniture | pages [9] -->
m

<!-- b002456 | furniture | pages [9] -->
m

<!-- b002457 | furniture | pages [9] -->
m

<!-- b002458 | furniture | pages [9] -->
m

<!-- b002459 | furniture | pages [9] -->
m

<!-- b002460 | furniture | pages [9] -->
m

<!-- b002461 | furniture | pages [9] -->
m

<!-- b002462 | furniture | pages [9] -->
m

<!-- b002463 | furniture | pages [9] -->
m

<!-- b002464 | furniture | pages [9] -->
m

<!-- b002465 | furniture | pages [9] -->
m

<!-- b002466 | furniture | pages [9] -->
m

<!-- b002467 | furniture | pages [9] -->
m

<!-- b002468 | furniture | pages [9] -->
m

<!-- b002469 | furniture | pages [9] -->
m

<!-- b002470 | furniture | pages [9] -->
m

<!-- b002471 | furniture | pages [9] -->
m

<!-- b002472 | furniture | pages [9] -->
m

<!-- b002473 | furniture | pages [9] -->
m

<!-- b002474 | furniture | pages [9] -->
m

<!-- b002475 | furniture | pages [9] -->
m

<!-- b002476 | furniture | pages [9] -->
m

<!-- b002477 | furniture | pages [9] -->
m

<!-- b002478 | furniture | pages [9] -->
m

<!-- b002479 | furniture | pages [9] -->
m

<!-- b002480 | furniture | pages [9] -->
m

<!-- b002481 | furniture | pages [9] -->
m

<!-- b002482 | furniture | pages [9] -->
m

<!-- b002483 | furniture | pages [9] -->
m

<!-- b002484 | furniture | pages [9] -->
m

<!-- b002485 | furniture | pages [9] -->
m

<!-- b002486 | furniture | pages [9] -->
m

<!-- b002487 | furniture | pages [9] -->
m

<!-- b002488 | furniture | pages [9] -->
m

<!-- b002489 | furniture | pages [9] -->
m

<!-- b002490 | furniture | pages [9] -->
m

<!-- b002491 | furniture | pages [9] -->
m

<!-- b002492 | furniture | pages [9] -->
m

<!-- b002493 | furniture | pages [9] -->
m

<!-- b002494 | furniture | pages [9] -->
m

<!-- b002495 | furniture | pages [9] -->
m

<!-- b002496 | furniture | pages [9] -->
m

<!-- b002497 | furniture | pages [9] -->
m

<!-- b002498 | furniture | pages [9] -->
m

<!-- b002499 | furniture | pages [9] -->
m

<!-- b002500 | furniture | pages [9] -->
m

<!-- b002501 | furniture | pages [9] -->
m

<!-- b002502 | furniture | pages [9] -->
m

<!-- b002503 | furniture | pages [9] -->
m

<!-- b002504 | furniture | pages [9] -->
m

<!-- b002505 | furniture | pages [9] -->
m

<!-- b002506 | furniture | pages [9] -->
m

<!-- b002507 | furniture | pages [9] -->
m

<!-- b002508 | furniture | pages [9] -->
m

<!-- b002509 | furniture | pages [9] -->
m

<!-- b002510 | furniture | pages [9] -->
m

<!-- b002511 | furniture | pages [9] -->
m

<!-- b002512 | furniture | pages [9] -->
m

<!-- b002513 | furniture | pages [9] -->
m

<!-- b002514 | furniture | pages [9] -->
m

<!-- b002515 | furniture | pages [9] -->
m

<!-- b002516 | furniture | pages [9] -->
m

<!-- b002517 | furniture | pages [9] -->
m

<!-- b002518 | furniture | pages [9] -->
m

<!-- b002519 | furniture | pages [9] -->
m

<!-- b002520 | furniture | pages [9] -->
m

<!-- b002521 | furniture | pages [9] -->
m

<!-- b002522 | furniture | pages [9] -->
m

<!-- b002523 | furniture | pages [9] -->
m

<!-- b002524 | furniture | pages [9] -->
m

<!-- b002525 | furniture | pages [9] -->
m

<!-- b002526 | furniture | pages [9] -->
m

<!-- b002527 | furniture | pages [9] -->
m

<!-- b002528 | furniture | pages [9] -->
m

<!-- b002529 | furniture | pages [9] -->
m

<!-- b002530 | furniture | pages [9] -->
m

<!-- b002531 | furniture | pages [9] -->
m

<!-- b002532 | furniture | pages [9] -->
m

<!-- b002533 | furniture | pages [9] -->
m

<!-- b002534 | furniture | pages [9] -->
m

<!-- b002535 | furniture | pages [9] -->
m

<!-- b002536 | furniture | pages [9] -->
m

<!-- b002537 | furniture | pages [9] -->
m

<!-- b002538 | furniture | pages [9] -->
m

<!-- b002539 | furniture | pages [9] -->
m

<!-- b002540 | furniture | pages [9] -->
m

<!-- b002541 | furniture | pages [9] -->
m

<!-- b002542 | furniture | pages [9] -->
m

<!-- b002543 | furniture | pages [9] -->
m

<!-- b002544 | furniture | pages [9] -->
m

<!-- b002545 | furniture | pages [9] -->
m

<!-- b002546 | furniture | pages [9] -->
m

<!-- b002547 | furniture | pages [9] -->
m

<!-- b002548 | furniture | pages [9] -->
m

<!-- b002549 | furniture | pages [9] -->
m

<!-- b002550 | furniture | pages [9] -->
m

<!-- b002551 | furniture | pages [9] -->
m

<!-- b002552 | furniture | pages [9] -->
m

<!-- b002553 | furniture | pages [9] -->
m

<!-- b002554 | furniture | pages [9] -->
m

<!-- b002555 | furniture | pages [9] -->
m

<!-- b002556 | furniture | pages [9] -->
m

<!-- b002557 | furniture | pages [9] -->
m

<!-- b002558 | furniture | pages [9] -->
m

<!-- b002559 | furniture | pages [9] -->
m

<!-- b002560 | furniture | pages [9] -->
m

<!-- b002561 | furniture | pages [9] -->
m

<!-- b002562 | furniture | pages [9] -->
m

<!-- b002563 | furniture | pages [9] -->
m

<!-- b002564 | furniture | pages [9] -->
m

<!-- b002565 | furniture | pages [9] -->
m

<!-- b002566 | furniture | pages [9] -->
m

<!-- b002567 | furniture | pages [9] -->
m

<!-- b002568 | furniture | pages [9] -->
m

<!-- b002569 | furniture | pages [9] -->
m

<!-- b002570 | furniture | pages [9] -->
m

<!-- b002571 | furniture | pages [9] -->
m

<!-- b002572 | furniture | pages [9] -->
m

<!-- b002573 | furniture | pages [9] -->
m

<!-- b002574 | furniture | pages [9] -->
m

<!-- b002575 | furniture | pages [9] -->
m

<!-- b002576 | furniture | pages [9] -->
m

<!-- b002577 | furniture | pages [9] -->
m

<!-- b002578 | furniture | pages [9] -->
m

<!-- b002579 | furniture | pages [9] -->
m

<!-- b002580 | furniture | pages [9] -->
m

<!-- b002581 | furniture | pages [9] -->
m

<!-- b002582 | furniture | pages [9] -->
m

<!-- b002583 | furniture | pages [9] -->
m

<!-- b002584 | furniture | pages [9] -->
m

<!-- b002585 | furniture | pages [9] -->
m

<!-- b002586 | furniture | pages [9] -->
m

<!-- b002587 | furniture | pages [9] -->
m

<!-- b002588 | furniture | pages [9] -->
m

<!-- b002589 | furniture | pages [9] -->
m

<!-- b002590 | furniture | pages [9] -->
m

<!-- b002591 | furniture | pages [9] -->
m

<!-- b002592 | furniture | pages [9] -->
m

<!-- b002593 | furniture | pages [9] -->
m

<!-- b002594 | furniture | pages [9] -->
m

<!-- b002595 | furniture | pages [9] -->
m

<!-- b002596 | furniture | pages [9] -->
m

<!-- b002597 | furniture | pages [9] -->
m

<!-- b002598 | furniture | pages [9] -->
m

<!-- b002599 | furniture | pages [9] -->
m

<!-- b002600 | furniture | pages [9] -->
m

<!-- b002601 | furniture | pages [9] -->
m

<!-- b002602 | furniture | pages [9] -->
m

<!-- b002603 | furniture | pages [9] -->
m

<!-- b002604 | furniture | pages [9] -->
m

<!-- b002605 | furniture | pages [9] -->
m

<!-- b002606 | furniture | pages [9] -->
m

<!-- b002607 | furniture | pages [9] -->
m

<!-- b002608 | furniture | pages [9] -->
m

<!-- b002609 | furniture | pages [9] -->
m

<!-- b002610 | furniture | pages [9] -->
m

<!-- b002611 | furniture | pages [9] -->
m

<!-- b002612 | furniture | pages [9] -->
m

<!-- b002613 | furniture | pages [9] -->
m

<!-- b002614 | furniture | pages [9] -->
m

<!-- b002615 | furniture | pages [9] -->
m

<!-- b002616 | furniture | pages [9] -->
m

<!-- b002617 | furniture | pages [9] -->
m

<!-- b002618 | furniture | pages [9] -->
m

<!-- b002619 | furniture | pages [9] -->
m

<!-- b002620 | furniture | pages [9] -->
m

<!-- b002621 | furniture | pages [9] -->
m

<!-- b002622 | furniture | pages [9] -->
m

<!-- b002623 | furniture | pages [9] -->
m

<!-- b002624 | furniture | pages [9] -->
m

<!-- b002625 | furniture | pages [9] -->
m

<!-- b002626 | furniture | pages [9] -->
m

<!-- b002627 | furniture | pages [9] -->
m

<!-- b002628 | furniture | pages [9] -->
m

<!-- b002629 | furniture | pages [9] -->
m

<!-- b002630 | furniture | pages [9] -->
m

<!-- b002631 | furniture | pages [9] -->
m

<!-- b002632 | furniture | pages [9] -->
m

<!-- b002633 | furniture | pages [9] -->
m

<!-- b002634 | furniture | pages [9] -->
m

<!-- b002635 | furniture | pages [9] -->
m

<!-- b002636 | furniture | pages [9] -->
m

<!-- b002637 | furniture | pages [9] -->
m

<!-- b002638 | furniture | pages [9] -->
m

<!-- b002639 | furniture | pages [9] -->
m

<!-- b002640 | furniture | pages [9] -->
m

<!-- b002641 | furniture | pages [9] -->
m

<!-- b002642 | furniture | pages [9] -->
m

<!-- b002643 | furniture | pages [9] -->
m

<!-- b002644 | furniture | pages [9] -->
m

<!-- b002645 | furniture | pages [9] -->
m

<!-- b002646 | furniture | pages [9] -->
m

<!-- b002647 | furniture | pages [9] -->
m

<!-- b002648 | furniture | pages [9] -->
m

<!-- b002649 | furniture | pages [9] -->
m

<!-- b002650 | furniture | pages [9] -->
m

<!-- b002651 | furniture | pages [9] -->
m

<!-- b002652 | furniture | pages [9] -->
m

<!-- b002653 | furniture | pages [9] -->
m

<!-- b002654 | furniture | pages [9] -->
m

<!-- b002655 | furniture | pages [9] -->
m

<!-- b002656 | furniture | pages [9] -->
m

<!-- b002657 | furniture | pages [9] -->
m

<!-- b002658 | furniture | pages [9] -->
m

<!-- b002659 | furniture | pages [9] -->
m

<!-- b002660 | furniture | pages [9] -->
m

<!-- b002661 | furniture | pages [9] -->
m

<!-- b002662 | furniture | pages [9] -->
m

<!-- b002663 | furniture | pages [9] -->
m

<!-- b002664 | furniture | pages [9] -->
m

<!-- b002665 | furniture | pages [9] -->
m

<!-- b002666 | furniture | pages [9] -->
m

<!-- b002667 | furniture | pages [9] -->
m

<!-- b002668 | furniture | pages [9] -->
m

<!-- b002669 | furniture | pages [9] -->
m

<!-- b002670 | furniture | pages [9] -->
m

<!-- b002671 | furniture | pages [9] -->
m

<!-- b002672 | furniture | pages [9] -->
m

<!-- b002673 | furniture | pages [9] -->
m

<!-- b002674 | furniture | pages [9] -->
m

<!-- b002675 | furniture | pages [9] -->
m

<!-- b002676 | furniture | pages [9] -->
m

<!-- b002677 | furniture | pages [9] -->
m

<!-- b002678 | furniture | pages [9] -->
m

<!-- b002679 | furniture | pages [9] -->
m

<!-- b002680 | furniture | pages [9] -->
m

<!-- b002681 | furniture | pages [9] -->
m

<!-- b002682 | furniture | pages [9] -->
m

<!-- b002683 | furniture | pages [9] -->
m

<!-- b002684 | furniture | pages [9] -->
m

<!-- b002685 | furniture | pages [9] -->
m

<!-- b002686 | furniture | pages [9] -->
m

<!-- b002687 | furniture | pages [9] -->
m

<!-- b002688 | furniture | pages [9] -->
m

<!-- b002689 | furniture | pages [9] -->
m

<!-- b002690 | furniture | pages [9] -->
m

<!-- b002691 | furniture | pages [9] -->
m

<!-- b002692 | furniture | pages [9] -->
m

<!-- b002693 | furniture | pages [9] -->
m

<!-- b002694 | furniture | pages [9] -->
m

<!-- b002695 | furniture | pages [9] -->
m

<!-- b002696 | furniture | pages [9] -->
m

<!-- b002697 | furniture | pages [9] -->
m

<!-- b002698 | furniture | pages [9] -->
m

<!-- b002699 | furniture | pages [9] -->
m

<!-- b002700 | furniture | pages [9] -->
m

<!-- b002701 | furniture | pages [9] -->
m

<!-- b002702 | furniture | pages [9] -->
m

<!-- b002703 | furniture | pages [9] -->
m

<!-- b002704 | furniture | pages [9] -->
m

<!-- b002705 | furniture | pages [9] -->
m

<!-- b002706 | furniture | pages [9] -->
m

<!-- b002707 | furniture | pages [9] -->
m

<!-- b002708 | furniture | pages [9] -->
m

<!-- b002709 | furniture | pages [9] -->
m

<!-- b002710 | furniture | pages [9] -->
m

<!-- b002711 | furniture | pages [9] -->
m

<!-- b002712 | furniture | pages [9] -->
m

<!-- b002713 | furniture | pages [9] -->
m

<!-- b002714 | furniture | pages [9] -->
m

<!-- b002715 | furniture | pages [9] -->
m

<!-- b002716 | furniture | pages [9] -->
m

<!-- b002717 | furniture | pages [9] -->
m

<!-- b002718 | furniture | pages [9] -->
m

<!-- b002719 | furniture | pages [9] -->
m

<!-- b002720 | furniture | pages [9] -->
m

<!-- b002721 | furniture | pages [9] -->
m

<!-- b002722 | furniture | pages [9] -->
m

<!-- b002723 | furniture | pages [9] -->
m

<!-- b002724 | furniture | pages [9] -->
m

<!-- b002725 | furniture | pages [9] -->
m

<!-- b002726 | furniture | pages [9] -->
m

<!-- b002727 | furniture | pages [9] -->
m

<!-- b002728 | furniture | pages [9] -->
m

<!-- b002729 | furniture | pages [10] -->
Team # 2503268

<!-- b002730 | furniture | pages [10] -->
Page 8 of 24

<!-- b002731 | prose | pages [10] -->
glacier data for that year. To address this, we excluded the 2013 data from the analysis and performed interpolation on the remaining years to ensure consistency. The adjusted dataset was then used to ﬁt the equations and estimate ki and ri.

<!-- b002732 | prose | pages [10] -->
The ﬁnal integrated system of equations, including ϖ, is expressed as:

<!-- b002733 | prose | pages [10] -->
dHJuneau

<!-- b002734 | prose | pages [10] -->
= k1HJuneau + k2HJuneauNJuneau + k3TJuneauHJuneau + ϖHJuneau, dt

<!-- b002735 | prose | pages [10] -->
#

<!-- b002736 | prose | pages [10] -->
dNJuneau

<!-- b002737 | prose | pages [10] -->
1 ↓NJuneau

<!-- b002738 | prose | pages [10] -->
= r1NJuneau dt

<!-- b002739 | prose | pages [10] -->
K

<!-- b002740 | prose | pages [10] -->
dTJuneau

<!-- b002741 | prose | pages [10] -->
(4)

<!-- b002742 | prose | pages [10] -->
$

<!-- b002743 | prose | pages [10] -->
+ k4HJuneauNJuneau + ϖNJuneau, (5)

<!-- b002744 | prose | pages [10] -->
= k5TJuneau + k6NJuneau + ϖTJuneau. dt (6)

<!-- b002745 | caption | pages [10] -->
Figure 3: System 3D schematic with projection

<!-- b002746 | caption | pages [10] -->
Figure 4: Respective projections

<!-- b002747 | prose | pages [10] -->
关注数学模型

<!-- b002748 | furniture | pages [10] -->
2

<!-- b002749 | furniture | pages [10] -->
MATHmodels

<!-- b002750 | furniture | pages [10] -->
获取更多资讯

<!-- b002751 | furniture | pages [11] -->
Team # 2503268

<!-- b002752 | furniture | pages [11] -->
Page 9 of 24

<!-- b002753 | prose | pages [11] -->
The ﬁtting results and the corresponding parameter values are visualized in Figure3, and the ac- curacy of the model is validated using historical data. Using data from 2010 to 2019, we performed parameter ﬁtting for the integrated model equations. The resulting parameter values were derived through nonlinear regression, incorporating the error terms ϖHJuneau, ϖNJuneau, and ϖTJuneau to account for external unmeasured inﬂuences.

<!-- b002754 | caption | pages [11] -->
Figure3 illustrates the observed data and the trajectories generated by the model in a 3D space,

<!-- b002755 | prose | pages [11] -->
showing the dynamic interactions between glacier health HJuneau, tourist numbers NJuneau, and hotel

<!-- b002756 | prose | pages [11] -->
微信公众号：数学模型

<!-- b002757 | prose | pages [11] -->
tax revenue TJuneau. The ﬁtted trajectories closely align with the observed data points, suggesting that the model captures the essential dynamics of the system.

<!-- b002758 | prose | pages [11] -->
Additionally, Figure3 displays the feasible regions in the (HJuneau, NJuneau), (HJuneau, TJuneau), and (NJuneau, TJuneau) planes. These regions represent the range of plausible model outcomes given the ﬁtted parameters. The observed data points (red stars) fall predominantly within these feasible regions, further validating the model’s predictive accuracy.

<!-- b002759 | prose | pages [11] -->
The results highlight several key insights:

<!-- b002760 | prose | pages [11] -->
1. The positive correlation between the ELA height of the glacier HJuneau and the tourist numbers NJuneau is evident in the trajectories, supporting the hypothesis that an increase in visitors nega-

<!-- b002761 | prose | pages [11] -->
微信号：MATHmodels

<!-- b002762 | prose | pages [11] -->
tively impacts the environment, thereby causing the ELA height to rise.

<!-- b002763 | prose | pages [11] -->
2. Annual hotel tax revenue TJuneau shows a direct dependency on tourist numbers NJuneau, as indi- cated by the tight clustering of observed data along the model trajectories in the (NJuneau, TJuneau) plane.

<!-- b002764 | prose | pages [11] -->
3. Variability in the system, represented by the error terms ϖ, likely captures external factors such as climatic anomalies or economic shocks, which are not directly modeled but are essential for explaining deviations.

<!-- b002765 | prose | pages [11] -->
These ﬁtting results provide a robust foundation for analyzing the dynamic interplay among nat- ural, social, and economic factors, and they oﬀer valuable insights for policy-making and resource management in glacier regions.

<!-- b002766 | prose | pages [11] -->
5.2 Intervention Strategies

<!-- b002767 | prose | pages [11] -->
5.2.1

<!-- b002768 | heading | pages [11] -->
Intervention Impact on Models

<!-- b002769 | prose | pages [11] -->
To maintain a balance between the three variables when maximizing utility, we categorize our intervention strategies into two components: tax revenue allocation and policies. Each component features a ﬁnite set of typical and representative solutions. By iterating through these solutions, we obtain a ﬁnite set of potential strategy combinations.

<!-- b002770 | prose | pages [11] -->
Given the current values of HJuneau, NJuneau, and TJuneau, each combination, under the given con- straints, produces new HJuneau, NJuneau, and TJuneau values along with corresponding scores. We then select the combination with the highest score to serve as the current intervention strategy, and update HJuneau, NJuneau, and TJuneau accordingly to these new values.

<!-- b002771 | furniture | pages [12] -->
Team # 2503268

<!-- b002772 | prose | pages [12] -->
5.2.2 Tax Revenue Allocation

<!-- b002773 | furniture | pages [12] -->
Page 10 of 24

<!-- b002774 | prose | pages [12] -->
The variables µ1, µ2, µ3, µ4, µ5 are inputs to the evaluation model. We modeled nine representative arrays [µ1, µ2, µ3, µ4, µ5] based on diﬀerent allocation patterns, which are displayed in the ﬁgure below.

<!-- b002775 | prose | pages [12] -->
m

<!-- b002776 | prose | pages [12] -->
m

<!-- b002777 | prose | pages [12] -->
m

<!-- b002778 | prose | pages [12] -->
m

<!-- b002779 | prose | pages [12] -->
m

<!-- b002780 | prose | pages [12] -->
m

<!-- b002781 | prose | pages [12] -->
m

<!-- b002782 | prose | pages [12] -->
m

<!-- b002783 | prose | pages [12] -->
m

<!-- b002784 | prose | pages [12] -->
m

<!-- b002785 | prose | pages [12] -->
m

<!-- b002786 | prose | pages [12] -->
m

<!-- b002787 | prose | pages [12] -->
m

<!-- b002788 | prose | pages [12] -->
m

<!-- b002789 | prose | pages [12] -->
m

<!-- b002790 | prose | pages [12] -->
m

<!-- b002791 | prose | pages [12] -->
m

<!-- b002792 | prose | pages [12] -->
m

<!-- b002793 | prose | pages [12] -->
m

<!-- b002794 | prose | pages [12] -->
m

<!-- b002795 | prose | pages [12] -->
m

<!-- b002796 | prose | pages [12] -->
m

<!-- b002797 | prose | pages [12] -->
m

<!-- b002798 | prose | pages [12] -->
m

<!-- b002799 | prose | pages [12] -->
m

<!-- b002800 | prose | pages [12] -->
m

<!-- b002801 | prose | pages [12] -->
m

<!-- b002802 | prose | pages [12] -->
m

<!-- b002803 | prose | pages [12] -->
m

<!-- b002804 | prose | pages [12] -->
m

<!-- b002805 | prose | pages [12] -->
m

<!-- b002806 | prose | pages [12] -->
m

<!-- b002807 | prose | pages [12] -->
m

<!-- b002808 | prose | pages [12] -->
m

<!-- b002809 | prose | pages [12] -->
m

<!-- b002810 | prose | pages [12] -->
m

<!-- b002811 | prose | pages [12] -->
m

<!-- b002812 | prose | pages [12] -->
m

<!-- b002813 | prose | pages [12] -->
m

<!-- b002814 | prose | pages [12] -->
m

<!-- b002815 | prose | pages [12] -->
m

<!-- b002816 | prose | pages [12] -->
m

<!-- b002817 | prose | pages [12] -->
m

<!-- b002818 | prose | pages [12] -->
m

<!-- b002819 | prose | pages [12] -->
m

<!-- b002820 | prose | pages [12] -->
m

<!-- b002821 | prose | pages [12] -->
m

<!-- b002822 | prose | pages [12] -->
m

<!-- b002823 | prose | pages [12] -->
m

<!-- b002824 | prose | pages [12] -->
m

<!-- b002825 | prose | pages [12] -->
m

<!-- b002826 | prose | pages [12] -->
m

<!-- b002827 | prose | pages [12] -->
m

<!-- b002828 | prose | pages [12] -->
m

<!-- b002829 | prose | pages [12] -->
m

<!-- b002830 | prose | pages [12] -->
m

<!-- b002831 | prose | pages [12] -->
m

<!-- b002832 | prose | pages [12] -->
m

<!-- b002833 | prose | pages [12] -->
m

<!-- b002834 | prose | pages [12] -->
m

<!-- b002835 | prose | pages [12] -->
m

<!-- b002836 | prose | pages [12] -->
m

<!-- b002837 | prose | pages [12] -->
m

<!-- b002838 | prose | pages [12] -->
m

<!-- b002839 | prose | pages [12] -->
m

<!-- b002840 | prose | pages [12] -->
m

<!-- b002841 | prose | pages [12] -->
m

<!-- b002842 | prose | pages [12] -->
m

<!-- b002843 | prose | pages [12] -->
m

<!-- b002844 | prose | pages [12] -->
m

<!-- b002845 | prose | pages [12] -->
m

<!-- b002846 | prose | pages [12] -->
m

<!-- b002847 | prose | pages [12] -->
m

<!-- b002848 | prose | pages [12] -->
m

<!-- b002849 | prose | pages [12] -->
m

<!-- b002850 | prose | pages [12] -->
m

<!-- b002851 | prose | pages [12] -->
m

<!-- b002852 | prose | pages [12] -->
m

<!-- b002853 | prose | pages [12] -->
m

<!-- b002854 | prose | pages [12] -->
m

<!-- b002855 | prose | pages [12] -->
m

<!-- b002856 | prose | pages [12] -->
m

<!-- b002857 | prose | pages [12] -->
m

<!-- b002858 | prose | pages [12] -->
m

<!-- b002859 | prose | pages [12] -->
m

<!-- b002860 | prose | pages [12] -->
m

<!-- b002861 | prose | pages [12] -->
m

<!-- b002862 | prose | pages [12] -->
m

<!-- b002863 | prose | pages [12] -->
m

<!-- b002864 | prose | pages [12] -->
m

<!-- b002865 | prose | pages [12] -->
m

<!-- b002866 | prose | pages [12] -->
m

<!-- b002867 | prose | pages [12] -->
m

<!-- b002868 | prose | pages [12] -->
m

<!-- b002869 | prose | pages [12] -->
m

<!-- b002870 | prose | pages [12] -->
m

<!-- b002871 | prose | pages [12] -->
m

<!-- b002872 | prose | pages [12] -->
m

<!-- b002873 | prose | pages [12] -->
m

<!-- b002874 | prose | pages [12] -->
m

<!-- b002875 | prose | pages [12] -->
m

<!-- b002876 | prose | pages [12] -->
m

<!-- b002877 | prose | pages [12] -->
m

<!-- b002878 | prose | pages [12] -->
m

<!-- b002879 | prose | pages [12] -->
m

<!-- b002880 | prose | pages [12] -->
m

<!-- b002881 | prose | pages [12] -->
m

<!-- b002882 | prose | pages [12] -->
m

<!-- b002883 | prose | pages [12] -->
m

<!-- b002884 | prose | pages [12] -->
m

<!-- b002885 | prose | pages [12] -->
m

<!-- b002886 | prose | pages [12] -->
m

<!-- b002887 | prose | pages [12] -->
m

<!-- b002888 | prose | pages [12] -->
m

<!-- b002889 | prose | pages [12] -->
m

<!-- b002890 | prose | pages [12] -->
m

<!-- b002891 | prose | pages [12] -->
m

<!-- b002892 | prose | pages [12] -->
m

<!-- b002893 | prose | pages [12] -->
m

<!-- b002894 | prose | pages [12] -->
m

<!-- b002895 | prose | pages [12] -->
m

<!-- b002896 | prose | pages [12] -->
m

<!-- b002897 | prose | pages [12] -->
m

<!-- b002898 | prose | pages [12] -->
m

<!-- b002899 | prose | pages [12] -->
m

<!-- b002900 | prose | pages [12] -->
m

<!-- b002901 | prose | pages [12] -->
m

<!-- b002902 | prose | pages [12] -->
m

<!-- b002903 | prose | pages [12] -->
m

<!-- b002904 | prose | pages [12] -->
m

<!-- b002905 | prose | pages [12] -->
m

<!-- b002906 | prose | pages [12] -->
m

<!-- b002907 | prose | pages [12] -->
m

<!-- b002908 | prose | pages [12] -->
m

<!-- b002909 | prose | pages [12] -->
m

<!-- b002910 | prose | pages [12] -->
m

<!-- b002911 | prose | pages [12] -->
m

<!-- b002912 | prose | pages [12] -->
m

<!-- b002913 | prose | pages [12] -->
m

<!-- b002914 | prose | pages [12] -->
m

<!-- b002915 | prose | pages [12] -->
m

<!-- b002916 | prose | pages [12] -->
m

<!-- b002917 | prose | pages [12] -->
m

<!-- b002918 | prose | pages [12] -->
m

<!-- b002919 | prose | pages [12] -->
m

<!-- b002920 | prose | pages [12] -->
m

<!-- b002921 | prose | pages [12] -->
m

<!-- b002922 | prose | pages [12] -->
m

<!-- b002923 | prose | pages [12] -->
m

<!-- b002924 | prose | pages [12] -->
m

<!-- b002925 | prose | pages [12] -->
m

<!-- b002926 | prose | pages [12] -->
m

<!-- b002927 | prose | pages [12] -->
m

<!-- b002928 | prose | pages [12] -->
m

<!-- b002929 | prose | pages [12] -->
m

<!-- b002930 | prose | pages [12] -->
m

<!-- b002931 | prose | pages [12] -->
m

<!-- b002932 | prose | pages [12] -->
m

<!-- b002933 | prose | pages [12] -->
m

<!-- b002934 | prose | pages [12] -->
m

<!-- b002935 | prose | pages [12] -->
m

<!-- b002936 | prose | pages [12] -->
m

<!-- b002937 | prose | pages [12] -->
m

<!-- b002938 | prose | pages [12] -->
m

<!-- b002939 | prose | pages [12] -->
m

<!-- b002940 | prose | pages [12] -->
m

<!-- b002941 | prose | pages [12] -->
m

<!-- b002942 | prose | pages [12] -->
m

<!-- b002943 | prose | pages [12] -->
m

<!-- b002944 | prose | pages [12] -->
m

<!-- b002945 | prose | pages [12] -->
m

<!-- b002946 | prose | pages [12] -->
m

<!-- b002947 | prose | pages [12] -->
m

<!-- b002948 | prose | pages [12] -->
m

<!-- b002949 | prose | pages [12] -->
m

<!-- b002950 | prose | pages [12] -->
m

<!-- b002951 | prose | pages [12] -->
m

<!-- b002952 | prose | pages [12] -->
m

<!-- b002953 | prose | pages [12] -->
m

<!-- b002954 | prose | pages [12] -->
m

<!-- b002955 | prose | pages [12] -->
m

<!-- b002956 | prose | pages [12] -->
m

<!-- b002957 | prose | pages [12] -->
m

<!-- b002958 | prose | pages [12] -->
m

<!-- b002959 | prose | pages [12] -->
m

<!-- b002960 | prose | pages [12] -->
m

<!-- b002961 | prose | pages [12] -->
m

<!-- b002962 | prose | pages [12] -->
m

<!-- b002963 | prose | pages [12] -->
m

<!-- b002964 | prose | pages [12] -->
m

<!-- b002965 | prose | pages [12] -->
m

<!-- b002966 | prose | pages [12] -->
m

<!-- b002967 | prose | pages [12] -->
m

<!-- b002968 | prose | pages [12] -->
m

<!-- b002969 | prose | pages [12] -->
m

<!-- b002970 | prose | pages [12] -->
m

<!-- b002971 | prose | pages [12] -->
m

<!-- b002972 | prose | pages [12] -->
m

<!-- b002973 | prose | pages [12] -->
m

<!-- b002974 | prose | pages [12] -->
m

<!-- b002975 | prose | pages [12] -->
m

<!-- b002976 | prose | pages [12] -->
m

<!-- b002977 | prose | pages [12] -->
m

<!-- b002978 | prose | pages [12] -->
m

<!-- b002979 | prose | pages [12] -->
m

<!-- b002980 | prose | pages [12] -->
m

<!-- b002981 | prose | pages [12] -->
m

<!-- b002982 | prose | pages [12] -->
m

<!-- b002983 | prose | pages [12] -->
m

<!-- b002984 | prose | pages [12] -->
m

<!-- b002985 | prose | pages [12] -->
m

<!-- b002986 | prose | pages [12] -->
m

<!-- b002987 | prose | pages [12] -->
m

<!-- b002988 | prose | pages [12] -->
m

<!-- b002989 | prose | pages [12] -->
m

<!-- b002990 | prose | pages [12] -->
m

<!-- b002991 | prose | pages [12] -->
m

<!-- b002992 | prose | pages [12] -->
m

<!-- b002993 | prose | pages [12] -->
m

<!-- b002994 | prose | pages [12] -->
m

<!-- b002995 | prose | pages [12] -->
m

<!-- b002996 | prose | pages [12] -->
m

<!-- b002997 | prose | pages [12] -->
m

<!-- b002998 | prose | pages [12] -->
m

<!-- b002999 | prose | pages [12] -->
m

<!-- b003000 | prose | pages [12] -->
m

<!-- b003001 | prose | pages [12] -->
m

<!-- b003002 | prose | pages [12] -->
m

<!-- b003003 | prose | pages [12] -->
m

<!-- b003004 | prose | pages [12] -->
m

<!-- b003005 | prose | pages [12] -->
m

<!-- b003006 | prose | pages [12] -->
m

<!-- b003007 | prose | pages [12] -->
m

<!-- b003008 | prose | pages [12] -->
m

<!-- b003009 | prose | pages [12] -->
m

<!-- b003010 | prose | pages [12] -->
m

<!-- b003011 | prose | pages [12] -->
m

<!-- b003012 | prose | pages [12] -->
m

<!-- b003013 | prose | pages [12] -->
m

<!-- b003014 | prose | pages [12] -->
m

<!-- b003015 | prose | pages [12] -->
m

<!-- b003016 | prose | pages [12] -->
m

<!-- b003017 | prose | pages [12] -->
m

<!-- b003018 | prose | pages [12] -->
m

<!-- b003019 | prose | pages [12] -->
m

<!-- b003020 | prose | pages [12] -->
m

<!-- b003021 | prose | pages [12] -->
m

<!-- b003022 | prose | pages [12] -->
m

<!-- b003023 | prose | pages [12] -->
m

<!-- b003024 | prose | pages [12] -->
m

<!-- b003025 | prose | pages [12] -->
m

<!-- b003026 | prose | pages [12] -->
m

<!-- b003027 | prose | pages [12] -->
m

<!-- b003028 | prose | pages [12] -->
m

<!-- b003029 | prose | pages [12] -->
m

<!-- b003030 | prose | pages [12] -->
m

<!-- b003031 | prose | pages [12] -->
m

<!-- b003032 | prose | pages [12] -->
m

<!-- b003033 | prose | pages [12] -->
m

<!-- b003034 | prose | pages [12] -->
m

<!-- b003035 | prose | pages [12] -->
m

<!-- b003036 | prose | pages [12] -->
m

<!-- b003037 | prose | pages [12] -->
m

<!-- b003038 | prose | pages [12] -->
m

<!-- b003039 | prose | pages [12] -->
m

<!-- b003040 | prose | pages [12] -->
m

<!-- b003041 | prose | pages [12] -->
m

<!-- b003042 | prose | pages [12] -->
m

<!-- b003043 | prose | pages [12] -->
m

<!-- b003044 | prose | pages [12] -->
m

<!-- b003045 | prose | pages [12] -->
m

<!-- b003046 | prose | pages [12] -->
m

<!-- b003047 | prose | pages [12] -->
m

<!-- b003048 | prose | pages [12] -->
m

<!-- b003049 | prose | pages [12] -->
m

<!-- b003050 | prose | pages [12] -->
m

<!-- b003051 | prose | pages [12] -->
m

<!-- b003052 | prose | pages [12] -->
m

<!-- b003053 | prose | pages [12] -->
m

<!-- b003054 | prose | pages [12] -->
m

<!-- b003055 | prose | pages [12] -->
m

<!-- b003056 | prose | pages [12] -->
m

<!-- b003057 | prose | pages [12] -->
m

<!-- b003058 | prose | pages [12] -->
m

<!-- b003059 | prose | pages [12] -->
m

<!-- b003060 | prose | pages [12] -->
m

<!-- b003061 | prose | pages [12] -->
m

<!-- b003062 | prose | pages [12] -->
m

<!-- b003063 | prose | pages [12] -->
m

<!-- b003064 | prose | pages [12] -->
m

<!-- b003065 | prose | pages [12] -->
m

<!-- b003066 | prose | pages [12] -->
m

<!-- b003067 | prose | pages [12] -->
m

<!-- b003068 | prose | pages [12] -->
m

<!-- b003069 | prose | pages [12] -->
m

<!-- b003070 | prose | pages [12] -->
m

<!-- b003071 | prose | pages [12] -->
m

<!-- b003072 | prose | pages [12] -->
m

<!-- b003073 | prose | pages [12] -->
m

<!-- b003074 | prose | pages [12] -->
m

<!-- b003075 | prose | pages [12] -->
m

<!-- b003076 | prose | pages [12] -->
m

<!-- b003077 | prose | pages [12] -->
m

<!-- b003078 | prose | pages [12] -->
m

<!-- b003079 | prose | pages [12] -->
m

<!-- b003080 | prose | pages [12] -->
m

<!-- b003081 | prose | pages [12] -->
m

<!-- b003082 | prose | pages [12] -->
m

<!-- b003083 | prose | pages [12] -->
m

<!-- b003084 | prose | pages [12] -->
m

<!-- b003085 | prose | pages [12] -->
m

<!-- b003086 | prose | pages [12] -->
m

<!-- b003087 | prose | pages [12] -->
m

<!-- b003088 | prose | pages [12] -->
m

<!-- b003089 | prose | pages [12] -->
m

<!-- b003090 | prose | pages [12] -->
m

<!-- b003091 | prose | pages [12] -->
m

<!-- b003092 | prose | pages [12] -->
m

<!-- b003093 | prose | pages [12] -->
m

<!-- b003094 | prose | pages [12] -->
m

<!-- b003095 | prose | pages [12] -->
m

<!-- b003096 | prose | pages [12] -->
m

<!-- b003097 | prose | pages [12] -->
m

<!-- b003098 | prose | pages [12] -->
m

<!-- b003099 | prose | pages [12] -->
m

<!-- b003100 | prose | pages [12] -->
m

<!-- b003101 | prose | pages [12] -->
m

<!-- b003102 | prose | pages [12] -->
m

<!-- b003103 | prose | pages [12] -->
m

<!-- b003104 | prose | pages [12] -->
m

<!-- b003105 | prose | pages [12] -->
m

<!-- b003106 | prose | pages [12] -->
m

<!-- b003107 | prose | pages [12] -->
m

<!-- b003108 | prose | pages [12] -->
m

<!-- b003109 | prose | pages [12] -->
m

<!-- b003110 | prose | pages [12] -->
m

<!-- b003111 | prose | pages [12] -->
m

<!-- b003112 | prose | pages [12] -->
m

<!-- b003113 | prose | pages [12] -->
m

<!-- b003114 | prose | pages [12] -->
m

<!-- b003115 | prose | pages [12] -->
m

<!-- b003116 | prose | pages [12] -->
m

<!-- b003117 | prose | pages [12] -->
m

<!-- b003118 | prose | pages [12] -->
m

<!-- b003119 | prose | pages [12] -->
m

<!-- b003120 | prose | pages [12] -->
m

<!-- b003121 | prose | pages [12] -->
m

<!-- b003122 | prose | pages [12] -->
m

<!-- b003123 | caption | pages [12] -->
Figure 5: Allocations

<!-- b003124 | prose | pages [12] -->
m

<!-- b003125 | prose | pages [12] -->
m

<!-- b003126 | prose | pages [12] -->
m

<!-- b003127 | prose | pages [12] -->
m

<!-- b003128 | prose | pages [12] -->
m

<!-- b003129 | prose | pages [12] -->
m

<!-- b003130 | prose | pages [12] -->
m

<!-- b003131 | prose | pages [12] -->
m

<!-- b003132 | prose | pages [12] -->
m

<!-- b003133 | prose | pages [12] -->
m

<!-- b003134 | prose | pages [12] -->
m

<!-- b003135 | prose | pages [12] -->
m

<!-- b003136 | prose | pages [12] -->
m

<!-- b003137 | prose | pages [12] -->
m

<!-- b003138 | prose | pages [12] -->
m

<!-- b003139 | prose | pages [12] -->
m

<!-- b003140 | prose | pages [12] -->
m

<!-- b003141 | prose | pages [12] -->
m

<!-- b003142 | prose | pages [12] -->
m

<!-- b003143 | prose | pages [12] -->
m

<!-- b003144 | prose | pages [12] -->
m

<!-- b003145 | prose | pages [12] -->
m

<!-- b003146 | prose | pages [12] -->
m

<!-- b003147 | prose | pages [12] -->
m

<!-- b003148 | prose | pages [12] -->
m

<!-- b003149 | prose | pages [12] -->
m

<!-- b003150 | prose | pages [12] -->
m

<!-- b003151 | prose | pages [12] -->
m

<!-- b003152 | prose | pages [12] -->
m

<!-- b003153 | prose | pages [12] -->
m

<!-- b003154 | prose | pages [12] -->
m

<!-- b003155 | prose | pages [12] -->
m

<!-- b003156 | prose | pages [12] -->
m

<!-- b003157 | prose | pages [12] -->
m

<!-- b003158 | prose | pages [12] -->
m

<!-- b003159 | prose | pages [12] -->
m

<!-- b003160 | prose | pages [12] -->
m

<!-- b003161 | prose | pages [12] -->
m

<!-- b003162 | prose | pages [12] -->
m

<!-- b003163 | prose | pages [12] -->
m

<!-- b003164 | prose | pages [12] -->
m

<!-- b003165 | prose | pages [12] -->
m

<!-- b003166 | prose | pages [12] -->
m

<!-- b003167 | prose | pages [12] -->
m

<!-- b003168 | prose | pages [12] -->
m

<!-- b003169 | prose | pages [12] -->
m

<!-- b003170 | prose | pages [12] -->
m

<!-- b003171 | prose | pages [12] -->
m

<!-- b003172 | prose | pages [12] -->
m

<!-- b003173 | prose | pages [12] -->
m

<!-- b003174 | prose | pages [12] -->
m

<!-- b003175 | prose | pages [12] -->
m

<!-- b003176 | prose | pages [12] -->
m

<!-- b003177 | prose | pages [12] -->
m

<!-- b003178 | prose | pages [12] -->
m

<!-- b003179 | prose | pages [12] -->
m

<!-- b003180 | prose | pages [12] -->
m

<!-- b003181 | prose | pages [12] -->
m

<!-- b003182 | prose | pages [12] -->
m

<!-- b003183 | prose | pages [12] -->
m

<!-- b003184 | prose | pages [12] -->
m

<!-- b003185 | prose | pages [12] -->
m

<!-- b003186 | prose | pages [12] -->
m

<!-- b003187 | prose | pages [12] -->
m

<!-- b003188 | prose | pages [12] -->
m

<!-- b003189 | prose | pages [12] -->
m

<!-- b003190 | prose | pages [12] -->
m

<!-- b003191 | prose | pages [12] -->
m

<!-- b003192 | prose | pages [12] -->
m

<!-- b003193 | prose | pages [12] -->
m

<!-- b003194 | prose | pages [12] -->
m

<!-- b003195 | prose | pages [12] -->
m

<!-- b003196 | prose | pages [12] -->
m

<!-- b003197 | prose | pages [12] -->
m

<!-- b003198 | prose | pages [12] -->
m

<!-- b003199 | prose | pages [12] -->
m

<!-- b003200 | prose | pages [12] -->
m

<!-- b003201 | prose | pages [12] -->
m

<!-- b003202 | prose | pages [12] -->
m

<!-- b003203 | prose | pages [12] -->
m

<!-- b003204 | prose | pages [12] -->
m

<!-- b003205 | prose | pages [12] -->
m

<!-- b003206 | prose | pages [12] -->
m

<!-- b003207 | prose | pages [12] -->
m

<!-- b003208 | prose | pages [12] -->
m

<!-- b003209 | prose | pages [12] -->
m

<!-- b003210 | prose | pages [12] -->
m

<!-- b003211 | prose | pages [12] -->
m

<!-- b003212 | prose | pages [12] -->
m

<!-- b003213 | prose | pages [12] -->
m

<!-- b003214 | prose | pages [12] -->
m

<!-- b003215 | prose | pages [12] -->
m

<!-- b003216 | prose | pages [12] -->
m

<!-- b003217 | prose | pages [12] -->
m

<!-- b003218 | prose | pages [12] -->
m

<!-- b003219 | prose | pages [12] -->
m

<!-- b003220 | prose | pages [12] -->
m

<!-- b003221 | prose | pages [12] -->
m

<!-- b003222 | prose | pages [12] -->
m

<!-- b003223 | prose | pages [12] -->
m

<!-- b003224 | prose | pages [12] -->
m

<!-- b003225 | prose | pages [12] -->
m

<!-- b003226 | prose | pages [12] -->
m

<!-- b003227 | prose | pages [12] -->
m

<!-- b003228 | prose | pages [12] -->
m

<!-- b003229 | prose | pages [12] -->
m

<!-- b003230 | prose | pages [12] -->
m

<!-- b003231 | prose | pages [12] -->
m

<!-- b003232 | prose | pages [12] -->
m

<!-- b003233 | prose | pages [12] -->
m

<!-- b003234 | prose | pages [12] -->
m

<!-- b003235 | prose | pages [12] -->
m

<!-- b003236 | prose | pages [12] -->
m

<!-- b003237 | prose | pages [12] -->
m

<!-- b003238 | prose | pages [12] -->
m

<!-- b003239 | prose | pages [12] -->
m

<!-- b003240 | prose | pages [12] -->
m

<!-- b003241 | prose | pages [12] -->
m

<!-- b003242 | prose | pages [12] -->
m

<!-- b003243 | prose | pages [12] -->
m

<!-- b003244 | prose | pages [12] -->
m

<!-- b003245 | prose | pages [12] -->
m

<!-- b003246 | prose | pages [12] -->
m

<!-- b003247 | prose | pages [12] -->
m

<!-- b003248 | prose | pages [12] -->
m

<!-- b003249 | prose | pages [12] -->
m

<!-- b003250 | prose | pages [12] -->
m

<!-- b003251 | prose | pages [12] -->
m

<!-- b003252 | prose | pages [12] -->
m

<!-- b003253 | prose | pages [12] -->
m

<!-- b003254 | prose | pages [12] -->
m

<!-- b003255 | prose | pages [12] -->
m

<!-- b003256 | prose | pages [12] -->
m

<!-- b003257 | prose | pages [12] -->
m

<!-- b003258 | prose | pages [12] -->
5.2.3 Policies

<!-- b003259 | prose | pages [12] -->
m

<!-- b003260 | prose | pages [12] -->
m

<!-- b003261 | prose | pages [12] -->
m

<!-- b003262 | prose | pages [12] -->
m

<!-- b003263 | prose | pages [12] -->
m

<!-- b003264 | prose | pages [12] -->
m

<!-- b003265 | prose | pages [12] -->
m

<!-- b003266 | prose | pages [12] -->
m

<!-- b003267 | prose | pages [12] -->
m

<!-- b003268 | prose | pages [12] -->
m

<!-- b003269 | prose | pages [12] -->
m

<!-- b003270 | prose | pages [12] -->
m

<!-- b003271 | prose | pages [12] -->
m

<!-- b003272 | prose | pages [12] -->
m

<!-- b003273 | prose | pages [12] -->
m

<!-- b003274 | prose | pages [12] -->
m

<!-- b003275 | prose | pages [12] -->
m

<!-- b003276 | prose | pages [12] -->
m

<!-- b003277 | prose | pages [12] -->
m

<!-- b003278 | prose | pages [12] -->
m

<!-- b003279 | prose | pages [12] -->
m

<!-- b003280 | prose | pages [12] -->
m

<!-- b003281 | prose | pages [12] -->
m

<!-- b003282 | prose | pages [12] -->
m

<!-- b003283 | prose | pages [12] -->
m

<!-- b003284 | prose | pages [12] -->
m

<!-- b003285 | prose | pages [12] -->
m

<!-- b003286 | prose | pages [12] -->
m

<!-- b003287 | prose | pages [12] -->
m

<!-- b003288 | prose | pages [12] -->
m

<!-- b003289 | prose | pages [12] -->
m

<!-- b003290 | prose | pages [12] -->
m

<!-- b003291 | prose | pages [12] -->
m

<!-- b003292 | prose | pages [12] -->
m

<!-- b003293 | prose | pages [12] -->
m

<!-- b003294 | prose | pages [12] -->
m

<!-- b003295 | prose | pages [12] -->
m

<!-- b003296 | prose | pages [12] -->
m

<!-- b003297 | prose | pages [12] -->
m

<!-- b003298 | prose | pages [12] -->
m

<!-- b003299 | prose | pages [12] -->
m

<!-- b003300 | prose | pages [12] -->
m

<!-- b003301 | prose | pages [12] -->
m

<!-- b003302 | prose | pages [12] -->
m

<!-- b003303 | prose | pages [12] -->
m

<!-- b003304 | prose | pages [12] -->
m

<!-- b003305 | prose | pages [12] -->
m

<!-- b003306 | prose | pages [12] -->
m

<!-- b003307 | prose | pages [12] -->
m

<!-- b003308 | prose | pages [12] -->
m

<!-- b003309 | prose | pages [12] -->
m

<!-- b003310 | prose | pages [12] -->
m

<!-- b003311 | prose | pages [12] -->
m

<!-- b003312 | prose | pages [12] -->
m

<!-- b003313 | prose | pages [12] -->
m

<!-- b003314 | prose | pages [12] -->
m

<!-- b003315 | prose | pages [12] -->
m

<!-- b003316 | prose | pages [12] -->
m

<!-- b003317 | prose | pages [12] -->
m

<!-- b003318 | prose | pages [12] -->
m

<!-- b003319 | prose | pages [12] -->
m

<!-- b003320 | prose | pages [12] -->
m

<!-- b003321 | prose | pages [12] -->
m

<!-- b003322 | prose | pages [12] -->
m

<!-- b003323 | prose | pages [12] -->
m

<!-- b003324 | prose | pages [12] -->
m

<!-- b003325 | prose | pages [12] -->
m

<!-- b003326 | prose | pages [12] -->
m

<!-- b003327 | prose | pages [12] -->
m

<!-- b003328 | prose | pages [12] -->
m

<!-- b003329 | prose | pages [12] -->
m

<!-- b003330 | prose | pages [12] -->
m

<!-- b003331 | prose | pages [12] -->
m

<!-- b003332 | prose | pages [12] -->
m

<!-- b003333 | prose | pages [12] -->
m

<!-- b003334 | prose | pages [12] -->
m

<!-- b003335 | prose | pages [12] -->
m

<!-- b003336 | prose | pages [12] -->
m

<!-- b003337 | prose | pages [12] -->
m

<!-- b003338 | prose | pages [12] -->
m

<!-- b003339 | prose | pages [12] -->
m

<!-- b003340 | prose | pages [12] -->
m

<!-- b003341 | prose | pages [12] -->
m

<!-- b003342 | prose | pages [12] -->
m

<!-- b003343 | prose | pages [12] -->
m

<!-- b003344 | prose | pages [12] -->
m

<!-- b003345 | prose | pages [12] -->
m

<!-- b003346 | prose | pages [12] -->
m

<!-- b003347 | prose | pages [12] -->
m

<!-- b003348 | prose | pages [12] -->
m

<!-- b003349 | prose | pages [12] -->
m

<!-- b003350 | prose | pages [12] -->
m

<!-- b003351 | prose | pages [12] -->
m

<!-- b003352 | prose | pages [12] -->
m

<!-- b003353 | prose | pages [12] -->
m

<!-- b003354 | prose | pages [12] -->
m

<!-- b003355 | prose | pages [12] -->
m

<!-- b003356 | prose | pages [12] -->
m

<!-- b003357 | prose | pages [12] -->
m

<!-- b003358 | prose | pages [12] -->
m

<!-- b003359 | prose | pages [12] -->
m

<!-- b003360 | prose | pages [12] -->
m

<!-- b003361 | prose | pages [12] -->
m

<!-- b003362 | prose | pages [12] -->
m

<!-- b003363 | prose | pages [12] -->
m

<!-- b003364 | prose | pages [12] -->
m

<!-- b003365 | prose | pages [12] -->
m

<!-- b003366 | prose | pages [12] -->
m

<!-- b003367 | prose | pages [12] -->
m

<!-- b003368 | prose | pages [12] -->
m

<!-- b003369 | prose | pages [12] -->
m

<!-- b003370 | prose | pages [12] -->
m

<!-- b003371 | prose | pages [12] -->
m

<!-- b003372 | prose | pages [12] -->
m

<!-- b003373 | prose | pages [12] -->
m

<!-- b003374 | prose | pages [12] -->
m

<!-- b003375 | prose | pages [12] -->
m

<!-- b003376 | prose | pages [12] -->
m

<!-- b003377 | prose | pages [12] -->
m

<!-- b003378 | prose | pages [12] -->
m

<!-- b003379 | prose | pages [12] -->
m

<!-- b003380 | prose | pages [12] -->
m

<!-- b003381 | prose | pages [12] -->
m

<!-- b003382 | prose | pages [12] -->
m

<!-- b003383 | prose | pages [12] -->
m

<!-- b003384 | prose | pages [12] -->
m

<!-- b003385 | prose | pages [12] -->
m

<!-- b003386 | prose | pages [12] -->
m

<!-- b003387 | prose | pages [12] -->
m

<!-- b003388 | prose | pages [12] -->
m

<!-- b003389 | prose | pages [12] -->
m

<!-- b003390 | prose | pages [12] -->
m

<!-- b003391 | prose | pages [12] -->
m

<!-- b003392 | prose | pages [12] -->
m

<!-- b003393 | prose | pages [12] -->
m

<!-- b003394 | prose | pages [12] -->
m

<!-- b003395 | prose | pages [12] -->
m

<!-- b003396 | prose | pages [12] -->
m

<!-- b003397 | prose | pages [12] -->
m

<!-- b003398 | prose | pages [12] -->
m

<!-- b003399 | prose | pages [12] -->
m

<!-- b003400 | prose | pages [12] -->
m

<!-- b003401 | prose | pages [12] -->
m

<!-- b003402 | prose | pages [12] -->
m

<!-- b003403 | prose | pages [12] -->
m

<!-- b003404 | prose | pages [12] -->
m

<!-- b003405 | prose | pages [12] -->
m

<!-- b003406 | prose | pages [12] -->
m

<!-- b003407 | prose | pages [12] -->
m

<!-- b003408 | prose | pages [12] -->
m

<!-- b003409 | prose | pages [12] -->
m

<!-- b003410 | prose | pages [12] -->
m

<!-- b003411 | prose | pages [12] -->
m

<!-- b003412 | prose | pages [12] -->
m

<!-- b003413 | prose | pages [12] -->
m

<!-- b003414 | prose | pages [12] -->
m

<!-- b003415 | prose | pages [12] -->
m

<!-- b003416 | prose | pages [12] -->
m

<!-- b003417 | prose | pages [12] -->
m

<!-- b003418 | prose | pages [12] -->
m

<!-- b003419 | prose | pages [12] -->
m

<!-- b003420 | prose | pages [12] -->
m

<!-- b003421 | prose | pages [12] -->
m

<!-- b003422 | prose | pages [12] -->
m

<!-- b003423 | prose | pages [12] -->
m

<!-- b003424 | prose | pages [12] -->
m

<!-- b003425 | prose | pages [12] -->
m

<!-- b003426 | prose | pages [12] -->
m

<!-- b003427 | prose | pages [12] -->
m

<!-- b003428 | prose | pages [12] -->
m

<!-- b003429 | prose | pages [12] -->
m

<!-- b003430 | prose | pages [12] -->
m

<!-- b003431 | prose | pages [12] -->
m

<!-- b003432 | prose | pages [12] -->
m

<!-- b003433 | prose | pages [12] -->
m

<!-- b003434 | prose | pages [12] -->
m

<!-- b003435 | prose | pages [12] -->
m

<!-- b003436 | prose | pages [12] -->
m

<!-- b003437 | prose | pages [12] -->
m

<!-- b003438 | prose | pages [12] -->
m

<!-- b003439 | prose | pages [12] -->
m

<!-- b003440 | prose | pages [12] -->
m

<!-- b003441 | prose | pages [12] -->
m

<!-- b003442 | prose | pages [12] -->
m

<!-- b003443 | prose | pages [12] -->
m

<!-- b003444 | prose | pages [12] -->
m

<!-- b003445 | prose | pages [12] -->
m

<!-- b003446 | prose | pages [12] -->
m

<!-- b003447 | prose | pages [12] -->
m

<!-- b003448 | prose | pages [12] -->
m

<!-- b003449 | prose | pages [12] -->
m

<!-- b003450 | prose | pages [12] -->
m

<!-- b003451 | prose | pages [12] -->
m

<!-- b003452 | prose | pages [12] -->
m

<!-- b003453 | prose | pages [12] -->
m

<!-- b003454 | prose | pages [12] -->
m

<!-- b003455 | prose | pages [12] -->
m

<!-- b003456 | prose | pages [12] -->
m

<!-- b003457 | prose | pages [12] -->
m

<!-- b003458 | prose | pages [12] -->
m

<!-- b003459 | prose | pages [12] -->
m

<!-- b003460 | prose | pages [12] -->
m

<!-- b003461 | prose | pages [12] -->
m

<!-- b003462 | prose | pages [12] -->
m

<!-- b003463 | prose | pages [12] -->
m

<!-- b003464 | prose | pages [12] -->
We design 8 policies with diﬀerent focuses and assign diﬀerent vectors v1, v2, v3 to each policy. The vector satisﬁes ↓v1 + v2 + v3 = 10 as 10 is the sum assigned to the policies but H is a negative indicator. The detailed 8 policies are as follows:

<!-- b003465 | prose | pages [12] -->
Policy Description Vector

<!-- b003466 | prose | pages [12] -->
Promote local business development [0, 0, 10]

<!-- b003467 | prose | pages [12] -->
Comprehensive and balanced development

<!-- b003468 | prose | pages [12] -->
Develop infrastructure

<!-- b003469 | prose | pages [12] -->
[↓3, 3, 4]

<!-- b003470 | prose | pages [12] -->
[↓4, 4, 2]

<!-- b003471 | prose | pages [12] -->
Market promotion and brand building

<!-- b003472 | prose | pages [12] -->
Direct measures to attract tourists

<!-- b003473 | prose | pages [12] -->
Improve tourist experience

<!-- b003474 | prose | pages [12] -->
Natural resource conservation

<!-- b003475 | prose | pages [12] -->
[0, 4, 6]

<!-- b003476 | prose | pages [12] -->
[↓2, 8, 0]

<!-- b003477 | prose | pages [12] -->
[0, 8, 2]

<!-- b003478 | prose | pages [12] -->
[↓13, 0, ↓3], [↓14, ↓2, ↓2]

<!-- b003479 | caption | pages [12] -->
Table 3: Indicators Selected

<!-- b003480 | caption | pages [12] -->
Figure 6 displays the way how policies impact the system. We use the output of the evaluation

<!-- b003481 | prose | pages [12] -->
model to decide the policies too.

<!-- b003482 | prose | pages [12] -->
6

<!-- b003483 | heading | pages [12] -->
Evaluation Model

<!-- b003484 | prose | pages [12] -->
6.1 Indicators Determination

<!-- b003485 | prose | pages [12] -->
Based on the statement of the question and the literature, the degree of comprehensive devel- opment in the City of Juneau can be mainly categorized into three factors, which are life of local

<!-- b003486 | prose | pages [12] -->
关注数学模型

<!-- b003487 | furniture | pages [12] -->
2

<!-- b003488 | furniture | pages [12] -->
MATHmodels

<!-- b003489 | furniture | pages [12] -->
获取更多资讯

<!-- b003490 | furniture | pages [13] -->
Team # 2503268

<!-- b003491 | furniture | pages [13] -->
Page 11 of 24

<!-- b003492 | prose | pages [13] -->
微信公众号：数学模型

<!-- b003493 | caption | pages [13] -->
Figure 6: policy impact on system

<!-- b003494 | prose | pages [13] -->
residents(LoR), local environmental protection(EP), along with local economy and development of society(EDoS).

<!-- b003495 | prose | pages [13] -->
微信号：MATHmodels

<!-- b003496 | prose | pages [13] -->
In consideration of tourism impact, We have overall listed 29 secondary indicators that are related to the three main factors, and picked 4 most signiﬁcant secondary indicators for each main factor. The main factors and related secondary indicators are listed below.

<!-- b003497 | prose | pages [13] -->
Factor Indicator Score No- tation

<!-- b003498 | prose | pages [13] -->
the increase of average individual income LoR crowding level housing aﬀordability noise level S 11 S 12 S 13 S 14 natural resources like glacier coverage EP S 21 water and energy usage waste production level carbon footprint EDoS tourism tax revenue employment growth S 22 S 23 S 24 S 31 S 32 cultural resource protection or utilization S 33 social safety or security index S 34

<!-- b003499 | caption | pages [13] -->
Table 4: Indicators Selected

<!-- b003500 | prose | pages [13] -->
6.2

<!-- b003501 | heading | pages [13] -->
Score Calculation Model

<!-- b003502 | prose | pages [13] -->
Here, P = 31685. Here we use the Analytic Hierarchy Process(AHP). AHP assigns weights to criteria through pairwise comparisons, checks the consistency of these comparisons, and calculates an overall score by aggregating the weighted scores, which is displayed in the formulas below. S core1,

<!-- b003503 | prose | pages [13] -->
m

<!-- b003504 | prose | pages [13] -->
m

<!-- b003505 | prose | pages [13] -->
m

<!-- b003506 | prose | pages [13] -->
m

<!-- b003507 | prose | pages [13] -->
m

<!-- b003508 | prose | pages [13] -->
m

<!-- b003509 | prose | pages [13] -->
m

<!-- b003510 | prose | pages [13] -->
m

<!-- b003511 | prose | pages [13] -->
m

<!-- b003512 | prose | pages [13] -->
m

<!-- b003513 | prose | pages [13] -->
m

<!-- b003514 | prose | pages [13] -->
m

<!-- b003515 | prose | pages [13] -->
m

<!-- b003516 | prose | pages [13] -->
m

<!-- b003517 | prose | pages [13] -->
m

<!-- b003518 | prose | pages [13] -->
m

<!-- b003519 | prose | pages [13] -->
m

<!-- b003520 | prose | pages [13] -->
m

<!-- b003521 | prose | pages [13] -->
m

<!-- b003522 | prose | pages [13] -->
m

<!-- b003523 | prose | pages [13] -->
m

<!-- b003524 | prose | pages [13] -->
m

<!-- b003525 | prose | pages [13] -->
m

<!-- b003526 | prose | pages [13] -->
m

<!-- b003527 | prose | pages [13] -->
m

<!-- b003528 | prose | pages [13] -->
m

<!-- b003529 | prose | pages [13] -->
m

<!-- b003530 | prose | pages [13] -->
m

<!-- b003531 | prose | pages [13] -->
m

<!-- b003532 | prose | pages [13] -->
m

<!-- b003533 | prose | pages [13] -->
m

<!-- b003534 | prose | pages [13] -->
m

<!-- b003535 | prose | pages [13] -->
m

<!-- b003536 | prose | pages [13] -->
m

<!-- b003537 | prose | pages [13] -->
m

<!-- b003538 | prose | pages [13] -->
m

<!-- b003539 | prose | pages [13] -->
m

<!-- b003540 | prose | pages [13] -->
m

<!-- b003541 | prose | pages [13] -->
m

<!-- b003542 | prose | pages [13] -->
m

<!-- b003543 | prose | pages [13] -->
m

<!-- b003544 | prose | pages [13] -->
m

<!-- b003545 | prose | pages [13] -->
m

<!-- b003546 | prose | pages [13] -->
m

<!-- b003547 | prose | pages [13] -->
m

<!-- b003548 | prose | pages [13] -->
m

<!-- b003549 | prose | pages [13] -->
m

<!-- b003550 | prose | pages [13] -->
m

<!-- b003551 | prose | pages [13] -->
m

<!-- b003552 | prose | pages [13] -->
m

<!-- b003553 | prose | pages [13] -->
m

<!-- b003554 | prose | pages [13] -->
m

<!-- b003555 | prose | pages [13] -->
m

<!-- b003556 | prose | pages [13] -->
m

<!-- b003557 | prose | pages [13] -->
m

<!-- b003558 | prose | pages [13] -->
m

<!-- b003559 | prose | pages [13] -->
m

<!-- b003560 | prose | pages [13] -->
m

<!-- b003561 | prose | pages [13] -->
m

<!-- b003562 | prose | pages [13] -->
m

<!-- b003563 | prose | pages [13] -->
m

<!-- b003564 | prose | pages [13] -->
m

<!-- b003565 | prose | pages [13] -->
m

<!-- b003566 | prose | pages [13] -->
m

<!-- b003567 | prose | pages [13] -->
m

<!-- b003568 | prose | pages [13] -->
m

<!-- b003569 | prose | pages [13] -->
m

<!-- b003570 | prose | pages [13] -->
m

<!-- b003571 | prose | pages [13] -->
m

<!-- b003572 | prose | pages [13] -->
m

<!-- b003573 | prose | pages [13] -->
m

<!-- b003574 | prose | pages [13] -->
m

<!-- b003575 | prose | pages [13] -->
m

<!-- b003576 | prose | pages [13] -->
m

<!-- b003577 | prose | pages [13] -->
m

<!-- b003578 | prose | pages [13] -->
m

<!-- b003579 | prose | pages [13] -->
m

<!-- b003580 | prose | pages [13] -->
m

<!-- b003581 | prose | pages [13] -->
m

<!-- b003582 | prose | pages [13] -->
m

<!-- b003583 | prose | pages [13] -->
m

<!-- b003584 | prose | pages [13] -->
m

<!-- b003585 | prose | pages [13] -->
m

<!-- b003586 | prose | pages [13] -->
m

<!-- b003587 | prose | pages [13] -->
m

<!-- b003588 | prose | pages [13] -->
m

<!-- b003589 | prose | pages [13] -->
m

<!-- b003590 | prose | pages [13] -->
m

<!-- b003591 | prose | pages [13] -->
m

<!-- b003592 | prose | pages [13] -->
m

<!-- b003593 | prose | pages [13] -->
m

<!-- b003594 | prose | pages [13] -->
m

<!-- b003595 | prose | pages [13] -->
m

<!-- b003596 | prose | pages [13] -->
m

<!-- b003597 | prose | pages [13] -->
m

<!-- b003598 | prose | pages [13] -->
m

<!-- b003599 | prose | pages [13] -->
m

<!-- b003600 | prose | pages [13] -->
m

<!-- b003601 | prose | pages [13] -->
m

<!-- b003602 | prose | pages [13] -->
m

<!-- b003603 | prose | pages [13] -->
m

<!-- b003604 | prose | pages [13] -->
m

<!-- b003605 | prose | pages [13] -->
m

<!-- b003606 | prose | pages [13] -->
m

<!-- b003607 | prose | pages [13] -->
m

<!-- b003608 | prose | pages [13] -->
m

<!-- b003609 | prose | pages [13] -->
m

<!-- b003610 | prose | pages [13] -->
m

<!-- b003611 | prose | pages [13] -->
m

<!-- b003612 | prose | pages [13] -->
m

<!-- b003613 | prose | pages [13] -->
m

<!-- b003614 | prose | pages [13] -->
m

<!-- b003615 | prose | pages [13] -->
m

<!-- b003616 | prose | pages [13] -->
m

<!-- b003617 | prose | pages [13] -->
m

<!-- b003618 | prose | pages [13] -->
m

<!-- b003619 | prose | pages [13] -->
m

<!-- b003620 | prose | pages [13] -->
m

<!-- b003621 | prose | pages [13] -->
m

<!-- b003622 | prose | pages [13] -->
m

<!-- b003623 | prose | pages [13] -->
m

<!-- b003624 | prose | pages [13] -->
m

<!-- b003625 | prose | pages [13] -->
m

<!-- b003626 | prose | pages [13] -->
m

<!-- b003627 | prose | pages [13] -->
m

<!-- b003628 | prose | pages [13] -->
m

<!-- b003629 | prose | pages [13] -->
m

<!-- b003630 | prose | pages [13] -->
m

<!-- b003631 | prose | pages [13] -->
m

<!-- b003632 | prose | pages [13] -->
m

<!-- b003633 | prose | pages [13] -->
m

<!-- b003634 | prose | pages [13] -->
m

<!-- b003635 | prose | pages [13] -->
m

<!-- b003636 | prose | pages [13] -->
m

<!-- b003637 | prose | pages [13] -->
m

<!-- b003638 | prose | pages [13] -->
m

<!-- b003639 | prose | pages [13] -->
m

<!-- b003640 | prose | pages [13] -->
m

<!-- b003641 | prose | pages [13] -->
m

<!-- b003642 | prose | pages [13] -->
m

<!-- b003643 | prose | pages [13] -->
m

<!-- b003644 | prose | pages [13] -->
m

<!-- b003645 | prose | pages [13] -->
m

<!-- b003646 | prose | pages [13] -->
m

<!-- b003647 | prose | pages [13] -->
m

<!-- b003648 | prose | pages [13] -->
m

<!-- b003649 | prose | pages [13] -->
m

<!-- b003650 | prose | pages [13] -->
m

<!-- b003651 | prose | pages [13] -->
m

<!-- b003652 | prose | pages [13] -->
m

<!-- b003653 | prose | pages [13] -->
m

<!-- b003654 | prose | pages [13] -->
m

<!-- b003655 | prose | pages [13] -->
m

<!-- b003656 | prose | pages [13] -->
m

<!-- b003657 | prose | pages [13] -->
m

<!-- b003658 | prose | pages [13] -->
m

<!-- b003659 | prose | pages [13] -->
m

<!-- b003660 | prose | pages [13] -->
m

<!-- b003661 | prose | pages [13] -->
m

<!-- b003662 | prose | pages [13] -->
m

<!-- b003663 | prose | pages [13] -->
m

<!-- b003664 | prose | pages [13] -->
m

<!-- b003665 | prose | pages [13] -->
m

<!-- b003666 | prose | pages [13] -->
m

<!-- b003667 | prose | pages [13] -->
m

<!-- b003668 | prose | pages [13] -->
m

<!-- b003669 | prose | pages [13] -->
m

<!-- b003670 | prose | pages [13] -->
m

<!-- b003671 | prose | pages [13] -->
m

<!-- b003672 | prose | pages [13] -->
m

<!-- b003673 | prose | pages [13] -->
m

<!-- b003674 | prose | pages [13] -->
m

<!-- b003675 | prose | pages [13] -->
m

<!-- b003676 | prose | pages [13] -->
m

<!-- b003677 | prose | pages [13] -->
m

<!-- b003678 | prose | pages [13] -->
m

<!-- b003679 | prose | pages [13] -->
m

<!-- b003680 | prose | pages [13] -->
m

<!-- b003681 | prose | pages [13] -->
m

<!-- b003682 | prose | pages [13] -->
m

<!-- b003683 | prose | pages [13] -->
m

<!-- b003684 | prose | pages [13] -->
m

<!-- b003685 | prose | pages [13] -->
m

<!-- b003686 | prose | pages [13] -->
m

<!-- b003687 | prose | pages [13] -->
m

<!-- b003688 | prose | pages [13] -->
m

<!-- b003689 | prose | pages [13] -->
m

<!-- b003690 | prose | pages [13] -->
m

<!-- b003691 | prose | pages [13] -->
m

<!-- b003692 | prose | pages [13] -->
m

<!-- b003693 | prose | pages [13] -->
m

<!-- b003694 | prose | pages [13] -->
m

<!-- b003695 | prose | pages [13] -->
m

<!-- b003696 | prose | pages [13] -->
m

<!-- b003697 | prose | pages [13] -->
m

<!-- b003698 | prose | pages [13] -->
m

<!-- b003699 | prose | pages [13] -->
m

<!-- b003700 | prose | pages [13] -->
m

<!-- b003701 | prose | pages [13] -->
m

<!-- b003702 | prose | pages [13] -->
m

<!-- b003703 | prose | pages [13] -->
m

<!-- b003704 | prose | pages [13] -->
m

<!-- b003705 | prose | pages [13] -->
m

<!-- b003706 | prose | pages [13] -->
m

<!-- b003707 | prose | pages [13] -->
m

<!-- b003708 | prose | pages [13] -->
m

<!-- b003709 | prose | pages [13] -->
m

<!-- b003710 | prose | pages [13] -->
m

<!-- b003711 | prose | pages [13] -->
m

<!-- b003712 | prose | pages [13] -->
m

<!-- b003713 | prose | pages [13] -->
m

<!-- b003714 | prose | pages [13] -->
m

<!-- b003715 | prose | pages [13] -->
m

<!-- b003716 | prose | pages [13] -->
m

<!-- b003717 | prose | pages [13] -->
m

<!-- b003718 | prose | pages [13] -->
m

<!-- b003719 | prose | pages [13] -->
m

<!-- b003720 | prose | pages [13] -->
m

<!-- b003721 | prose | pages [13] -->
m

<!-- b003722 | prose | pages [13] -->
m

<!-- b003723 | prose | pages [13] -->
m

<!-- b003724 | prose | pages [13] -->
m

<!-- b003725 | prose | pages [13] -->
m

<!-- b003726 | prose | pages [13] -->
m

<!-- b003727 | prose | pages [13] -->
m

<!-- b003728 | prose | pages [13] -->
m

<!-- b003729 | prose | pages [13] -->
m

<!-- b003730 | prose | pages [13] -->
m

<!-- b003731 | prose | pages [13] -->
m

<!-- b003732 | prose | pages [13] -->
m

<!-- b003733 | prose | pages [13] -->
m

<!-- b003734 | prose | pages [13] -->
m

<!-- b003735 | prose | pages [13] -->
m

<!-- b003736 | prose | pages [13] -->
m

<!-- b003737 | prose | pages [13] -->
m

<!-- b003738 | prose | pages [13] -->
m

<!-- b003739 | prose | pages [13] -->
m

<!-- b003740 | prose | pages [13] -->
m

<!-- b003741 | prose | pages [13] -->
m

<!-- b003742 | prose | pages [13] -->
m

<!-- b003743 | prose | pages [13] -->
m

<!-- b003744 | prose | pages [13] -->
m

<!-- b003745 | prose | pages [13] -->
m

<!-- b003746 | prose | pages [13] -->
m

<!-- b003747 | prose | pages [13] -->
m

<!-- b003748 | prose | pages [13] -->
m

<!-- b003749 | prose | pages [13] -->
m

<!-- b003750 | prose | pages [13] -->
m

<!-- b003751 | prose | pages [13] -->
m

<!-- b003752 | prose | pages [13] -->
m

<!-- b003753 | prose | pages [13] -->
m

<!-- b003754 | prose | pages [13] -->
m

<!-- b003755 | prose | pages [13] -->
m

<!-- b003756 | prose | pages [13] -->
m

<!-- b003757 | prose | pages [13] -->
m

<!-- b003758 | prose | pages [13] -->
m

<!-- b003759 | prose | pages [13] -->
m

<!-- b003760 | prose | pages [13] -->
m

<!-- b003761 | prose | pages [13] -->
m

<!-- b003762 | prose | pages [13] -->
m

<!-- b003763 | prose | pages [13] -->
m

<!-- b003764 | prose | pages [13] -->
m

<!-- b003765 | prose | pages [13] -->
m

<!-- b003766 | prose | pages [13] -->
m

<!-- b003767 | prose | pages [13] -->
m

<!-- b003768 | prose | pages [13] -->
m

<!-- b003769 | prose | pages [13] -->
m

<!-- b003770 | prose | pages [13] -->
m

<!-- b003771 | prose | pages [13] -->
m

<!-- b003772 | prose | pages [13] -->
m

<!-- b003773 | prose | pages [13] -->
m

<!-- b003774 | prose | pages [13] -->
m

<!-- b003775 | prose | pages [13] -->
m

<!-- b003776 | prose | pages [13] -->
m

<!-- b003777 | prose | pages [13] -->
m

<!-- b003778 | prose | pages [13] -->
m

<!-- b003779 | prose | pages [13] -->
m

<!-- b003780 | prose | pages [13] -->
m

<!-- b003781 | prose | pages [13] -->
m

<!-- b003782 | prose | pages [13] -->
m

<!-- b003783 | prose | pages [13] -->
m

<!-- b003784 | prose | pages [13] -->
m

<!-- b003785 | prose | pages [13] -->
m

<!-- b003786 | prose | pages [13] -->
m

<!-- b003787 | furniture | pages [13] -->
m

<!-- b003788 | furniture | pages [13] -->
m

<!-- b003789 | furniture | pages [13] -->
m

<!-- b003790 | furniture | pages [13] -->
m

<!-- b003791 | furniture | pages [13] -->
m

<!-- b003792 | furniture | pages [13] -->
m

<!-- b003793 | furniture | pages [13] -->
m

<!-- b003794 | furniture | pages [13] -->
m

<!-- b003795 | furniture | pages [13] -->
m

<!-- b003796 | furniture | pages [13] -->
m

<!-- b003797 | furniture | pages [13] -->
m

<!-- b003798 | furniture | pages [13] -->
m

<!-- b003799 | furniture | pages [13] -->
m

<!-- b003800 | furniture | pages [13] -->
m

<!-- b003801 | furniture | pages [13] -->
m

<!-- b003802 | furniture | pages [13] -->
m

<!-- b003803 | furniture | pages [13] -->
m

<!-- b003804 | furniture | pages [13] -->
m

<!-- b003805 | furniture | pages [13] -->
m

<!-- b003806 | furniture | pages [13] -->
m

<!-- b003807 | furniture | pages [13] -->
m

<!-- b003808 | furniture | pages [13] -->
m

<!-- b003809 | furniture | pages [13] -->
m

<!-- b003810 | furniture | pages [13] -->
m

<!-- b003811 | furniture | pages [13] -->
m

<!-- b003812 | furniture | pages [13] -->
m

<!-- b003813 | furniture | pages [13] -->
m

<!-- b003814 | furniture | pages [13] -->
m

<!-- b003815 | furniture | pages [13] -->
m

<!-- b003816 | furniture | pages [13] -->
m

<!-- b003817 | furniture | pages [13] -->
m

<!-- b003818 | furniture | pages [13] -->
m

<!-- b003819 | furniture | pages [13] -->
m

<!-- b003820 | furniture | pages [13] -->
m

<!-- b003821 | furniture | pages [13] -->
m

<!-- b003822 | furniture | pages [13] -->
m

<!-- b003823 | furniture | pages [13] -->
m

<!-- b003824 | furniture | pages [13] -->
m

<!-- b003825 | furniture | pages [13] -->
m

<!-- b003826 | furniture | pages [13] -->
m

<!-- b003827 | furniture | pages [13] -->
m

<!-- b003828 | furniture | pages [13] -->
m

<!-- b003829 | furniture | pages [13] -->
m

<!-- b003830 | furniture | pages [13] -->
m

<!-- b003831 | furniture | pages [13] -->
m

<!-- b003832 | furniture | pages [13] -->
m

<!-- b003833 | furniture | pages [13] -->
m

<!-- b003834 | furniture | pages [13] -->
m

<!-- b003835 | furniture | pages [13] -->
m

<!-- b003836 | furniture | pages [13] -->
m

<!-- b003837 | furniture | pages [13] -->
m

<!-- b003838 | furniture | pages [13] -->
m

<!-- b003839 | furniture | pages [13] -->
m

<!-- b003840 | furniture | pages [13] -->
m

<!-- b003841 | furniture | pages [13] -->
m

<!-- b003842 | furniture | pages [13] -->
m

<!-- b003843 | furniture | pages [13] -->
m

<!-- b003844 | furniture | pages [13] -->
m

<!-- b003845 | furniture | pages [13] -->
m

<!-- b003846 | furniture | pages [13] -->
m

<!-- b003847 | furniture | pages [13] -->
m

<!-- b003848 | furniture | pages [13] -->
m

<!-- b003849 | furniture | pages [13] -->
m

<!-- b003850 | furniture | pages [13] -->
m

<!-- b003851 | furniture | pages [13] -->
m

<!-- b003852 | furniture | pages [13] -->
m

<!-- b003853 | furniture | pages [13] -->
m

<!-- b003854 | furniture | pages [13] -->
m

<!-- b003855 | furniture | pages [13] -->
m

<!-- b003856 | furniture | pages [13] -->
m

<!-- b003857 | furniture | pages [13] -->
m

<!-- b003858 | furniture | pages [13] -->
m

<!-- b003859 | furniture | pages [13] -->
m

<!-- b003860 | furniture | pages [13] -->
m

<!-- b003861 | furniture | pages [13] -->
m

<!-- b003862 | furniture | pages [13] -->
m

<!-- b003863 | furniture | pages [13] -->
m

<!-- b003864 | furniture | pages [13] -->
m

<!-- b003865 | furniture | pages [13] -->
m

<!-- b003866 | furniture | pages [13] -->
m

<!-- b003867 | furniture | pages [13] -->
m

<!-- b003868 | furniture | pages [13] -->
m

<!-- b003869 | furniture | pages [13] -->
m

<!-- b003870 | furniture | pages [13] -->
m

<!-- b003871 | furniture | pages [13] -->
m

<!-- b003872 | furniture | pages [13] -->
m

<!-- b003873 | furniture | pages [13] -->
m

<!-- b003874 | furniture | pages [13] -->
m

<!-- b003875 | furniture | pages [13] -->
m

<!-- b003876 | furniture | pages [13] -->
m

<!-- b003877 | furniture | pages [13] -->
m

<!-- b003878 | furniture | pages [13] -->
m

<!-- b003879 | furniture | pages [13] -->
m

<!-- b003880 | furniture | pages [13] -->
m

<!-- b003881 | furniture | pages [13] -->
m

<!-- b003882 | furniture | pages [13] -->
m

<!-- b003883 | furniture | pages [13] -->
m

<!-- b003884 | furniture | pages [13] -->
m

<!-- b003885 | furniture | pages [13] -->
m

<!-- b003886 | furniture | pages [13] -->
m

<!-- b003887 | furniture | pages [13] -->
m

<!-- b003888 | furniture | pages [13] -->
m

<!-- b003889 | furniture | pages [13] -->
m

<!-- b003890 | furniture | pages [13] -->
m

<!-- b003891 | furniture | pages [13] -->
m

<!-- b003892 | furniture | pages [13] -->
m

<!-- b003893 | furniture | pages [13] -->
m

<!-- b003894 | furniture | pages [13] -->
m

<!-- b003895 | furniture | pages [13] -->
m

<!-- b003896 | furniture | pages [13] -->
m

<!-- b003897 | furniture | pages [13] -->
m

<!-- b003898 | furniture | pages [13] -->
m

<!-- b003899 | furniture | pages [13] -->
m

<!-- b003900 | furniture | pages [13] -->
m

<!-- b003901 | furniture | pages [13] -->
m

<!-- b003902 | furniture | pages [13] -->
m

<!-- b003903 | furniture | pages [13] -->
m

<!-- b003904 | furniture | pages [13] -->
m

<!-- b003905 | furniture | pages [13] -->
m

<!-- b003906 | furniture | pages [13] -->
m

<!-- b003907 | furniture | pages [13] -->
m

<!-- b003908 | furniture | pages [13] -->
m

<!-- b003909 | furniture | pages [13] -->
m

<!-- b003910 | furniture | pages [13] -->
m

<!-- b003911 | furniture | pages [13] -->
m

<!-- b003912 | furniture | pages [13] -->
m

<!-- b003913 | furniture | pages [13] -->
m

<!-- b003914 | furniture | pages [13] -->
m

<!-- b003915 | furniture | pages [13] -->
m

<!-- b003916 | furniture | pages [13] -->
m

<!-- b003917 | furniture | pages [13] -->
m

<!-- b003918 | furniture | pages [13] -->
m

<!-- b003919 | furniture | pages [13] -->
m

<!-- b003920 | furniture | pages [13] -->
m

<!-- b003921 | furniture | pages [13] -->
m

<!-- b003922 | furniture | pages [13] -->
m

<!-- b003923 | furniture | pages [13] -->
m

<!-- b003924 | furniture | pages [13] -->
m

<!-- b003925 | furniture | pages [13] -->
m

<!-- b003926 | furniture | pages [13] -->
m

<!-- b003927 | furniture | pages [13] -->
m

<!-- b003928 | furniture | pages [13] -->
m

<!-- b003929 | furniture | pages [13] -->
m

<!-- b003930 | furniture | pages [13] -->
m

<!-- b003931 | furniture | pages [13] -->
m

<!-- b003932 | furniture | pages [13] -->
m

<!-- b003933 | furniture | pages [13] -->
m

<!-- b003934 | furniture | pages [13] -->
m

<!-- b003935 | furniture | pages [13] -->
m

<!-- b003936 | furniture | pages [13] -->
m

<!-- b003937 | furniture | pages [13] -->
m

<!-- b003938 | furniture | pages [13] -->
m

<!-- b003939 | furniture | pages [13] -->
m

<!-- b003940 | furniture | pages [13] -->
m

<!-- b003941 | furniture | pages [13] -->
m

<!-- b003942 | furniture | pages [13] -->
m

<!-- b003943 | furniture | pages [13] -->
m

<!-- b003944 | furniture | pages [13] -->
m

<!-- b003945 | furniture | pages [13] -->
m

<!-- b003946 | furniture | pages [13] -->
m

<!-- b003947 | furniture | pages [13] -->
m

<!-- b003948 | furniture | pages [13] -->
m

<!-- b003949 | furniture | pages [13] -->
m

<!-- b003950 | furniture | pages [13] -->
m

<!-- b003951 | furniture | pages [13] -->
m

<!-- b003952 | furniture | pages [13] -->
m

<!-- b003953 | furniture | pages [13] -->
m

<!-- b003954 | furniture | pages [13] -->
m

<!-- b003955 | furniture | pages [13] -->
m

<!-- b003956 | furniture | pages [13] -->
m

<!-- b003957 | furniture | pages [13] -->
m

<!-- b003958 | furniture | pages [13] -->
m

<!-- b003959 | furniture | pages [13] -->
m

<!-- b003960 | furniture | pages [13] -->
m

<!-- b003961 | furniture | pages [13] -->
m

<!-- b003962 | furniture | pages [13] -->
m

<!-- b003963 | furniture | pages [13] -->
m

<!-- b003964 | furniture | pages [13] -->
m

<!-- b003965 | furniture | pages [13] -->
m

<!-- b003966 | furniture | pages [13] -->
m

<!-- b003967 | furniture | pages [13] -->
m

<!-- b003968 | furniture | pages [13] -->
m

<!-- b003969 | furniture | pages [13] -->
m

<!-- b003970 | furniture | pages [13] -->
m

<!-- b003971 | furniture | pages [13] -->
m

<!-- b003972 | furniture | pages [13] -->
m

<!-- b003973 | furniture | pages [13] -->
m

<!-- b003974 | furniture | pages [13] -->
m

<!-- b003975 | furniture | pages [13] -->
m

<!-- b003976 | furniture | pages [13] -->
m

<!-- b003977 | furniture | pages [13] -->
m

<!-- b003978 | furniture | pages [13] -->
m

<!-- b003979 | furniture | pages [13] -->
m

<!-- b003980 | furniture | pages [13] -->
m

<!-- b003981 | furniture | pages [13] -->
m

<!-- b003982 | furniture | pages [13] -->
m

<!-- b003983 | furniture | pages [13] -->
m

<!-- b003984 | furniture | pages [13] -->
m

<!-- b003985 | furniture | pages [13] -->
m

<!-- b003986 | furniture | pages [13] -->
m

<!-- b003987 | furniture | pages [13] -->
m

<!-- b003988 | furniture | pages [13] -->
m

<!-- b003989 | furniture | pages [13] -->
m

<!-- b003990 | furniture | pages [13] -->
m

<!-- b003991 | furniture | pages [13] -->
m

<!-- b003992 | furniture | pages [13] -->
m

<!-- b003993 | furniture | pages [13] -->
m

<!-- b003994 | furniture | pages [13] -->
m

<!-- b003995 | furniture | pages [13] -->
m

<!-- b003996 | furniture | pages [13] -->
m

<!-- b003997 | furniture | pages [13] -->
m

<!-- b003998 | furniture | pages [13] -->
m

<!-- b003999 | furniture | pages [13] -->
m

<!-- b004000 | furniture | pages [13] -->
m

<!-- b004001 | furniture | pages [13] -->
m

<!-- b004002 | furniture | pages [13] -->
m

<!-- b004003 | furniture | pages [13] -->
m

<!-- b004004 | furniture | pages [13] -->
m

<!-- b004005 | furniture | pages [13] -->
m

<!-- b004006 | furniture | pages [13] -->
m

<!-- b004007 | furniture | pages [13] -->
m

<!-- b004008 | furniture | pages [13] -->
m

<!-- b004009 | furniture | pages [13] -->
m

<!-- b004010 | furniture | pages [13] -->
m

<!-- b004011 | furniture | pages [13] -->
m

<!-- b004012 | furniture | pages [13] -->
m

<!-- b004013 | furniture | pages [13] -->
m

<!-- b004014 | furniture | pages [13] -->
m

<!-- b004015 | furniture | pages [13] -->
m

<!-- b004016 | furniture | pages [13] -->
m

<!-- b004017 | furniture | pages [13] -->
m

<!-- b004018 | furniture | pages [13] -->
m

<!-- b004019 | furniture | pages [13] -->
m

<!-- b004020 | furniture | pages [13] -->
m

<!-- b004021 | furniture | pages [13] -->
m

<!-- b004022 | furniture | pages [13] -->
m

<!-- b004023 | furniture | pages [13] -->
m

<!-- b004024 | furniture | pages [13] -->
m

<!-- b004025 | furniture | pages [13] -->
m

<!-- b004026 | furniture | pages [13] -->
m

<!-- b004027 | furniture | pages [13] -->
m

<!-- b004028 | furniture | pages [13] -->
m

<!-- b004029 | furniture | pages [13] -->
m

<!-- b004030 | furniture | pages [13] -->
m

<!-- b004031 | furniture | pages [13] -->
m

<!-- b004032 | furniture | pages [13] -->
m

<!-- b004033 | furniture | pages [13] -->
m

<!-- b004034 | furniture | pages [13] -->
m

<!-- b004035 | furniture | pages [13] -->
m

<!-- b004036 | furniture | pages [13] -->
m

<!-- b004037 | furniture | pages [13] -->
m

<!-- b004038 | furniture | pages [13] -->
m

<!-- b004039 | furniture | pages [13] -->
m

<!-- b004040 | furniture | pages [13] -->
m

<!-- b004041 | furniture | pages [13] -->
m

<!-- b004042 | furniture | pages [13] -->
m

<!-- b004043 | furniture | pages [13] -->
m

<!-- b004044 | furniture | pages [13] -->
m

<!-- b004045 | furniture | pages [13] -->
m

<!-- b004046 | furniture | pages [13] -->
m

<!-- b004047 | furniture | pages [13] -->
m

<!-- b004048 | furniture | pages [13] -->
m

<!-- b004049 | furniture | pages [13] -->
m

<!-- b004050 | furniture | pages [13] -->
m

<!-- b004051 | furniture | pages [13] -->
m

<!-- b004052 | furniture | pages [13] -->
m

<!-- b004053 | furniture | pages [13] -->
m

<!-- b004054 | furniture | pages [13] -->
m

<!-- b004055 | furniture | pages [13] -->
m

<!-- b004056 | furniture | pages [13] -->
m

<!-- b004057 | furniture | pages [13] -->
m

<!-- b004058 | furniture | pages [13] -->
m

<!-- b004059 | furniture | pages [13] -->
m

<!-- b004060 | furniture | pages [13] -->
m

<!-- b004061 | furniture | pages [13] -->
m

<!-- b004062 | furniture | pages [13] -->
m

<!-- b004063 | furniture | pages [13] -->
m

<!-- b004064 | furniture | pages [13] -->
m

<!-- b004065 | furniture | pages [13] -->
m

<!-- b004066 | furniture | pages [13] -->
m

<!-- b004067 | furniture | pages [13] -->
m

<!-- b004068 | furniture | pages [13] -->
m

<!-- b004069 | furniture | pages [13] -->
m

<!-- b004070 | furniture | pages [13] -->
m

<!-- b004071 | furniture | pages [13] -->
m

<!-- b004072 | furniture | pages [13] -->
m

<!-- b004073 | furniture | pages [13] -->
m

<!-- b004074 | furniture | pages [13] -->
m

<!-- b004075 | furniture | pages [13] -->
m

<!-- b004076 | furniture | pages [13] -->
m

<!-- b004077 | furniture | pages [13] -->
m

<!-- b004078 | furniture | pages [13] -->
m

<!-- b004079 | furniture | pages [13] -->
m

<!-- b004080 | furniture | pages [13] -->
m

<!-- b004081 | furniture | pages [13] -->
m

<!-- b004082 | furniture | pages [13] -->
m

<!-- b004083 | furniture | pages [13] -->
m

<!-- b004084 | furniture | pages [13] -->
m

<!-- b004085 | furniture | pages [13] -->
m

<!-- b004086 | furniture | pages [13] -->
m

<!-- b004087 | furniture | pages [13] -->
m

<!-- b004088 | furniture | pages [13] -->
m

<!-- b004089 | furniture | pages [13] -->
m

<!-- b004090 | furniture | pages [13] -->
m

<!-- b004091 | furniture | pages [13] -->
m

<!-- b004092 | furniture | pages [13] -->
m

<!-- b004093 | furniture | pages [13] -->
m

<!-- b004094 | furniture | pages [13] -->
m

<!-- b004095 | furniture | pages [13] -->
m

<!-- b004096 | furniture | pages [13] -->
m

<!-- b004097 | furniture | pages [13] -->
m

<!-- b004098 | furniture | pages [13] -->
m

<!-- b004099 | furniture | pages [13] -->
m

<!-- b004100 | furniture | pages [13] -->
m

<!-- b004101 | furniture | pages [13] -->
m

<!-- b004102 | furniture | pages [13] -->
m

<!-- b004103 | furniture | pages [13] -->
m

<!-- b004104 | furniture | pages [13] -->
m

<!-- b004105 | furniture | pages [13] -->
m

<!-- b004106 | furniture | pages [13] -->
m

<!-- b004107 | furniture | pages [13] -->
m

<!-- b004108 | furniture | pages [13] -->
m

<!-- b004109 | furniture | pages [13] -->
m

<!-- b004110 | furniture | pages [13] -->
m

<!-- b004111 | furniture | pages [13] -->
m

<!-- b004112 | furniture | pages [13] -->
m

<!-- b004113 | furniture | pages [13] -->
m

<!-- b004114 | furniture | pages [13] -->
m

<!-- b004115 | furniture | pages [13] -->
m

<!-- b004116 | furniture | pages [13] -->
m

<!-- b004117 | furniture | pages [13] -->
m

<!-- b004118 | furniture | pages [13] -->
m

<!-- b004119 | furniture | pages [13] -->
m

<!-- b004120 | furniture | pages [13] -->
m

<!-- b004121 | furniture | pages [13] -->
m

<!-- b004122 | furniture | pages [13] -->
m

<!-- b004123 | furniture | pages [13] -->
m

<!-- b004124 | furniture | pages [13] -->
m

<!-- b004125 | furniture | pages [13] -->
m

<!-- b004126 | furniture | pages [13] -->
m

<!-- b004127 | furniture | pages [13] -->
m

<!-- b004128 | furniture | pages [13] -->
m

<!-- b004129 | furniture | pages [13] -->
m

<!-- b004130 | furniture | pages [13] -->
m

<!-- b004131 | furniture | pages [13] -->
m

<!-- b004132 | furniture | pages [13] -->
m

<!-- b004133 | furniture | pages [13] -->
m

<!-- b004134 | furniture | pages [13] -->
m

<!-- b004135 | furniture | pages [13] -->
m

<!-- b004136 | furniture | pages [13] -->
m

<!-- b004137 | furniture | pages [13] -->
m

<!-- b004138 | furniture | pages [13] -->
m

<!-- b004139 | furniture | pages [13] -->
m

<!-- b004140 | furniture | pages [13] -->
m

<!-- b004141 | furniture | pages [13] -->
m

<!-- b004142 | furniture | pages [13] -->
m

<!-- b004143 | furniture | pages [13] -->
m

<!-- b004144 | furniture | pages [13] -->
m

<!-- b004145 | furniture | pages [13] -->
m

<!-- b004146 | furniture | pages [13] -->
m

<!-- b004147 | furniture | pages [13] -->
m

<!-- b004148 | furniture | pages [13] -->
m

<!-- b004149 | furniture | pages [13] -->
m

<!-- b004150 | furniture | pages [13] -->
m

<!-- b004151 | furniture | pages [13] -->
m

<!-- b004152 | furniture | pages [13] -->
m

<!-- b004153 | furniture | pages [13] -->
m

<!-- b004154 | furniture | pages [13] -->
m

<!-- b004155 | furniture | pages [13] -->
m

<!-- b004156 | furniture | pages [13] -->
m

<!-- b004157 | furniture | pages [13] -->
m

<!-- b004158 | furniture | pages [13] -->
m

<!-- b004159 | furniture | pages [13] -->
m

<!-- b004160 | furniture | pages [13] -->
m

<!-- b004161 | furniture | pages [13] -->
m

<!-- b004162 | furniture | pages [13] -->
m

<!-- b004163 | furniture | pages [13] -->
m

<!-- b004164 | furniture | pages [13] -->
m

<!-- b004165 | furniture | pages [13] -->
m

<!-- b004166 | furniture | pages [13] -->
m

<!-- b004167 | furniture | pages [13] -->
m

<!-- b004168 | furniture | pages [13] -->
m

<!-- b004169 | furniture | pages [13] -->
m

<!-- b004170 | furniture | pages [13] -->
m

<!-- b004171 | furniture | pages [13] -->
m

<!-- b004172 | furniture | pages [13] -->
m

<!-- b004173 | furniture | pages [13] -->
m

<!-- b004174 | furniture | pages [13] -->
m

<!-- b004175 | furniture | pages [13] -->
m

<!-- b004176 | furniture | pages [13] -->
m

<!-- b004177 | furniture | pages [13] -->
m

<!-- b004178 | furniture | pages [13] -->
m

<!-- b004179 | furniture | pages [13] -->
m

<!-- b004180 | furniture | pages [13] -->
m

<!-- b004181 | furniture | pages [13] -->
m

<!-- b004182 | furniture | pages [13] -->
m

<!-- b004183 | furniture | pages [13] -->
m

<!-- b004184 | furniture | pages [13] -->
m

<!-- b004185 | furniture | pages [13] -->
m

<!-- b004186 | furniture | pages [13] -->
m

<!-- b004187 | furniture | pages [13] -->
m

<!-- b004188 | furniture | pages [13] -->
m

<!-- b004189 | furniture | pages [13] -->
m

<!-- b004190 | furniture | pages [14] -->
m

<!-- b004191 | furniture | pages [14] -->
m

<!-- b004192 | furniture | pages [14] -->
m

<!-- b004193 | furniture | pages [14] -->
m

<!-- b004194 | furniture | pages [14] -->
m

<!-- b004195 | furniture | pages [14] -->
m

<!-- b004196 | furniture | pages [14] -->
m

<!-- b004197 | furniture | pages [14] -->
m

<!-- b004198 | furniture | pages [14] -->
m

<!-- b004199 | furniture | pages [14] -->
m

<!-- b004200 | furniture | pages [14] -->
m

<!-- b004201 | furniture | pages [14] -->
m

<!-- b004202 | furniture | pages [14] -->
m

<!-- b004203 | furniture | pages [14] -->
m

<!-- b004204 | furniture | pages [14] -->
m

<!-- b004205 | furniture | pages [14] -->
m

<!-- b004206 | furniture | pages [14] -->
m

<!-- b004207 | furniture | pages [14] -->
m

<!-- b004208 | furniture | pages [14] -->
m

<!-- b004209 | furniture | pages [14] -->
m

<!-- b004210 | furniture | pages [14] -->
m

<!-- b004211 | furniture | pages [14] -->
m

<!-- b004212 | furniture | pages [14] -->
m

<!-- b004213 | furniture | pages [14] -->
m

<!-- b004214 | furniture | pages [14] -->
m

<!-- b004215 | furniture | pages [14] -->
m

<!-- b004216 | furniture | pages [14] -->
m

<!-- b004217 | furniture | pages [14] -->
m

<!-- b004218 | furniture | pages [14] -->
m

<!-- b004219 | furniture | pages [14] -->
m

<!-- b004220 | furniture | pages [14] -->
m

<!-- b004221 | furniture | pages [14] -->
m

<!-- b004222 | furniture | pages [14] -->
m

<!-- b004223 | furniture | pages [14] -->
m

<!-- b004224 | furniture | pages [14] -->
m

<!-- b004225 | furniture | pages [14] -->
m

<!-- b004226 | furniture | pages [14] -->
m

<!-- b004227 | furniture | pages [14] -->
m

<!-- b004228 | furniture | pages [14] -->
m

<!-- b004229 | furniture | pages [14] -->
m

<!-- b004230 | furniture | pages [14] -->
m

<!-- b004231 | furniture | pages [14] -->
m

<!-- b004232 | furniture | pages [14] -->
m

<!-- b004233 | furniture | pages [14] -->
m

<!-- b004234 | furniture | pages [14] -->
m

<!-- b004235 | furniture | pages [14] -->
m

<!-- b004236 | furniture | pages [14] -->
m

<!-- b004237 | furniture | pages [14] -->
m

<!-- b004238 | furniture | pages [14] -->
m

<!-- b004239 | furniture | pages [14] -->
m

<!-- b004240 | furniture | pages [14] -->
m

<!-- b004241 | furniture | pages [14] -->
m

<!-- b004242 | furniture | pages [14] -->
m

<!-- b004243 | furniture | pages [14] -->
m

<!-- b004244 | furniture | pages [14] -->
m

<!-- b004245 | furniture | pages [14] -->
m

<!-- b004246 | furniture | pages [14] -->
m

<!-- b004247 | furniture | pages [14] -->
m

<!-- b004248 | furniture | pages [14] -->
m

<!-- b004249 | furniture | pages [14] -->
m

<!-- b004250 | furniture | pages [14] -->
m

<!-- b004251 | furniture | pages [14] -->
m

<!-- b004252 | furniture | pages [14] -->
m

<!-- b004253 | furniture | pages [14] -->
m

<!-- b004254 | furniture | pages [14] -->
m

<!-- b004255 | furniture | pages [14] -->
m

<!-- b004256 | furniture | pages [14] -->
m

<!-- b004257 | furniture | pages [14] -->
m

<!-- b004258 | furniture | pages [14] -->
m

<!-- b004259 | furniture | pages [14] -->
m

<!-- b004260 | furniture | pages [14] -->
m

<!-- b004261 | furniture | pages [14] -->
m

<!-- b004262 | furniture | pages [14] -->
m

<!-- b004263 | furniture | pages [14] -->
m

<!-- b004264 | furniture | pages [14] -->
m

<!-- b004265 | furniture | pages [14] -->
m

<!-- b004266 | furniture | pages [14] -->
m

<!-- b004267 | furniture | pages [14] -->
m

<!-- b004268 | furniture | pages [14] -->
m

<!-- b004269 | furniture | pages [14] -->
m

<!-- b004270 | furniture | pages [14] -->
m

<!-- b004271 | furniture | pages [14] -->
m

<!-- b004272 | furniture | pages [14] -->
m

<!-- b004273 | furniture | pages [14] -->
m

<!-- b004274 | furniture | pages [14] -->
m

<!-- b004275 | furniture | pages [14] -->
m

<!-- b004276 | furniture | pages [14] -->
m

<!-- b004277 | furniture | pages [14] -->
m

<!-- b004278 | furniture | pages [14] -->
m

<!-- b004279 | furniture | pages [14] -->
m

<!-- b004280 | furniture | pages [14] -->
m

<!-- b004281 | furniture | pages [14] -->
m

<!-- b004282 | furniture | pages [14] -->
m

<!-- b004283 | furniture | pages [14] -->
m

<!-- b004284 | furniture | pages [14] -->
m

<!-- b004285 | furniture | pages [14] -->
m

<!-- b004286 | furniture | pages [14] -->
m

<!-- b004287 | furniture | pages [14] -->
m

<!-- b004288 | furniture | pages [14] -->
m

<!-- b004289 | furniture | pages [14] -->
m

<!-- b004290 | furniture | pages [14] -->
m

<!-- b004291 | furniture | pages [14] -->
m

<!-- b004292 | furniture | pages [14] -->
m

<!-- b004293 | furniture | pages [14] -->
m

<!-- b004294 | furniture | pages [14] -->
m

<!-- b004295 | furniture | pages [14] -->
m

<!-- b004296 | furniture | pages [14] -->
m

<!-- b004297 | furniture | pages [14] -->
m

<!-- b004298 | furniture | pages [14] -->
m

<!-- b004299 | furniture | pages [14] -->
m

<!-- b004300 | furniture | pages [14] -->
m

<!-- b004301 | furniture | pages [14] -->
m

<!-- b004302 | furniture | pages [14] -->
m

<!-- b004303 | furniture | pages [14] -->
m

<!-- b004304 | furniture | pages [14] -->
m

<!-- b004305 | furniture | pages [14] -->
m

<!-- b004306 | furniture | pages [14] -->
m

<!-- b004307 | furniture | pages [14] -->
m

<!-- b004308 | furniture | pages [14] -->
m

<!-- b004309 | furniture | pages [14] -->
m

<!-- b004310 | furniture | pages [14] -->
m

<!-- b004311 | furniture | pages [14] -->
m

<!-- b004312 | furniture | pages [14] -->
m

<!-- b004313 | furniture | pages [14] -->
m

<!-- b004314 | furniture | pages [14] -->
m

<!-- b004315 | furniture | pages [14] -->
m

<!-- b004316 | furniture | pages [14] -->
m

<!-- b004317 | furniture | pages [14] -->
m

<!-- b004318 | furniture | pages [14] -->
m

<!-- b004319 | furniture | pages [14] -->
m

<!-- b004320 | furniture | pages [14] -->
m

<!-- b004321 | furniture | pages [14] -->
m

<!-- b004322 | furniture | pages [14] -->
m

<!-- b004323 | furniture | pages [14] -->
m

<!-- b004324 | furniture | pages [14] -->
m

<!-- b004325 | furniture | pages [14] -->
m

<!-- b004326 | furniture | pages [14] -->
m

<!-- b004327 | furniture | pages [14] -->
m

<!-- b004328 | furniture | pages [14] -->
m

<!-- b004329 | furniture | pages [14] -->
m

<!-- b004330 | furniture | pages [14] -->
m

<!-- b004331 | furniture | pages [14] -->
m

<!-- b004332 | furniture | pages [14] -->
m

<!-- b004333 | furniture | pages [14] -->
m

<!-- b004334 | furniture | pages [14] -->
m

<!-- b004335 | furniture | pages [14] -->
m

<!-- b004336 | furniture | pages [14] -->
m

<!-- b004337 | furniture | pages [14] -->
m

<!-- b004338 | furniture | pages [14] -->
m

<!-- b004339 | furniture | pages [14] -->
m

<!-- b004340 | furniture | pages [14] -->
m

<!-- b004341 | furniture | pages [14] -->
m

<!-- b004342 | furniture | pages [14] -->
m

<!-- b004343 | furniture | pages [14] -->
m

<!-- b004344 | furniture | pages [14] -->
m

<!-- b004345 | furniture | pages [14] -->
m

<!-- b004346 | furniture | pages [14] -->
m

<!-- b004347 | furniture | pages [14] -->
m

<!-- b004348 | furniture | pages [14] -->
m

<!-- b004349 | furniture | pages [14] -->
m

<!-- b004350 | furniture | pages [14] -->
m

<!-- b004351 | furniture | pages [14] -->
m

<!-- b004352 | furniture | pages [14] -->
m

<!-- b004353 | furniture | pages [14] -->
m

<!-- b004354 | furniture | pages [14] -->
m

<!-- b004355 | furniture | pages [14] -->
m

<!-- b004356 | furniture | pages [14] -->
m

<!-- b004357 | furniture | pages [14] -->
m

<!-- b004358 | furniture | pages [14] -->
m

<!-- b004359 | furniture | pages [14] -->
m

<!-- b004360 | furniture | pages [14] -->
m

<!-- b004361 | furniture | pages [14] -->
m

<!-- b004362 | furniture | pages [14] -->
m

<!-- b004363 | furniture | pages [14] -->
m

<!-- b004364 | furniture | pages [14] -->
m

<!-- b004365 | furniture | pages [14] -->
m

<!-- b004366 | furniture | pages [14] -->
m

<!-- b004367 | furniture | pages [14] -->
m

<!-- b004368 | furniture | pages [14] -->
m

<!-- b004369 | furniture | pages [14] -->
m

<!-- b004370 | furniture | pages [14] -->
m

<!-- b004371 | furniture | pages [14] -->
m

<!-- b004372 | furniture | pages [14] -->
m

<!-- b004373 | furniture | pages [14] -->
m

<!-- b004374 | furniture | pages [14] -->
m

<!-- b004375 | furniture | pages [14] -->
m

<!-- b004376 | furniture | pages [14] -->
m

<!-- b004377 | furniture | pages [14] -->
m

<!-- b004378 | furniture | pages [14] -->
m

<!-- b004379 | furniture | pages [14] -->
m

<!-- b004380 | furniture | pages [14] -->
m

<!-- b004381 | furniture | pages [14] -->
m

<!-- b004382 | furniture | pages [14] -->
m

<!-- b004383 | furniture | pages [14] -->
m

<!-- b004384 | furniture | pages [14] -->
m

<!-- b004385 | furniture | pages [14] -->
m

<!-- b004386 | furniture | pages [14] -->
m

<!-- b004387 | furniture | pages [14] -->
m

<!-- b004388 | furniture | pages [14] -->
m

<!-- b004389 | furniture | pages [14] -->
m

<!-- b004390 | furniture | pages [14] -->
m

<!-- b004391 | furniture | pages [14] -->
m

<!-- b004392 | furniture | pages [14] -->
m

<!-- b004393 | furniture | pages [14] -->
m

<!-- b004394 | furniture | pages [14] -->
m

<!-- b004395 | furniture | pages [14] -->
m

<!-- b004396 | furniture | pages [14] -->
m

<!-- b004397 | furniture | pages [14] -->
m

<!-- b004398 | furniture | pages [14] -->
m

<!-- b004399 | furniture | pages [14] -->
m

<!-- b004400 | furniture | pages [14] -->
m

<!-- b004401 | furniture | pages [14] -->
m

<!-- b004402 | furniture | pages [14] -->
m

<!-- b004403 | furniture | pages [14] -->
m

<!-- b004404 | furniture | pages [14] -->
m

<!-- b004405 | furniture | pages [14] -->
m

<!-- b004406 | furniture | pages [14] -->
m

<!-- b004407 | furniture | pages [14] -->
m

<!-- b004408 | furniture | pages [14] -->
m

<!-- b004409 | furniture | pages [14] -->
m

<!-- b004410 | furniture | pages [14] -->
m

<!-- b004411 | furniture | pages [14] -->
m

<!-- b004412 | furniture | pages [14] -->
m

<!-- b004413 | furniture | pages [14] -->
m

<!-- b004414 | furniture | pages [14] -->
m

<!-- b004415 | furniture | pages [14] -->
m

<!-- b004416 | furniture | pages [14] -->
m

<!-- b004417 | furniture | pages [14] -->
m

<!-- b004418 | furniture | pages [14] -->
m

<!-- b004419 | furniture | pages [14] -->
m

<!-- b004420 | furniture | pages [14] -->
m

<!-- b004421 | furniture | pages [14] -->
m

<!-- b004422 | furniture | pages [14] -->
m

<!-- b004423 | furniture | pages [14] -->
m

<!-- b004424 | furniture | pages [14] -->
m

<!-- b004425 | furniture | pages [14] -->
m

<!-- b004426 | furniture | pages [14] -->
m

<!-- b004427 | furniture | pages [14] -->
m

<!-- b004428 | furniture | pages [14] -->
m

<!-- b004429 | furniture | pages [14] -->
m

<!-- b004430 | furniture | pages [14] -->
m

<!-- b004431 | furniture | pages [14] -->
m

<!-- b004432 | furniture | pages [14] -->
m

<!-- b004433 | furniture | pages [14] -->
m

<!-- b004434 | furniture | pages [14] -->
m

<!-- b004435 | furniture | pages [14] -->
m

<!-- b004436 | furniture | pages [14] -->
m

<!-- b004437 | furniture | pages [14] -->
m

<!-- b004438 | furniture | pages [14] -->
m

<!-- b004439 | furniture | pages [14] -->
m

<!-- b004440 | furniture | pages [14] -->
m

<!-- b004441 | furniture | pages [14] -->
m

<!-- b004442 | furniture | pages [14] -->
m

<!-- b004443 | furniture | pages [14] -->
m

<!-- b004444 | furniture | pages [14] -->
m

<!-- b004445 | furniture | pages [14] -->
m

<!-- b004446 | furniture | pages [14] -->
m

<!-- b004447 | furniture | pages [14] -->
m

<!-- b004448 | furniture | pages [14] -->
m

<!-- b004449 | furniture | pages [14] -->
m

<!-- b004450 | furniture | pages [14] -->
m

<!-- b004451 | furniture | pages [14] -->
m

<!-- b004452 | furniture | pages [14] -->
Team # 2503268

<!-- b004453 | furniture | pages [14] -->
m

<!-- b004454 | furniture | pages [14] -->
m

<!-- b004455 | furniture | pages [14] -->
m

<!-- b004456 | furniture | pages [14] -->
m

<!-- b004457 | furniture | pages [14] -->
m

<!-- b004458 | furniture | pages [14] -->
m

<!-- b004459 | furniture | pages [14] -->
m

<!-- b004460 | furniture | pages [14] -->
m

<!-- b004461 | furniture | pages [14] -->
m

<!-- b004462 | furniture | pages [14] -->
m

<!-- b004463 | furniture | pages [14] -->
m

<!-- b004464 | furniture | pages [14] -->
m

<!-- b004465 | furniture | pages [14] -->
m

<!-- b004466 | furniture | pages [14] -->
m

<!-- b004467 | furniture | pages [14] -->
m

<!-- b004468 | furniture | pages [14] -->
m

<!-- b004469 | furniture | pages [14] -->
m

<!-- b004470 | furniture | pages [14] -->
m

<!-- b004471 | furniture | pages [14] -->
m

<!-- b004472 | furniture | pages [14] -->
m

<!-- b004473 | furniture | pages [14] -->
m

<!-- b004474 | furniture | pages [14] -->
m

<!-- b004475 | furniture | pages [14] -->
m

<!-- b004476 | furniture | pages [14] -->
m

<!-- b004477 | furniture | pages [14] -->
m

<!-- b004478 | furniture | pages [14] -->
m

<!-- b004479 | furniture | pages [14] -->
m

<!-- b004480 | furniture | pages [14] -->
m

<!-- b004481 | furniture | pages [14] -->
m

<!-- b004482 | furniture | pages [14] -->
m

<!-- b004483 | furniture | pages [14] -->
m

<!-- b004484 | furniture | pages [14] -->
m

<!-- b004485 | furniture | pages [14] -->
m

<!-- b004486 | furniture | pages [14] -->
m

<!-- b004487 | furniture | pages [14] -->
m

<!-- b004488 | furniture | pages [14] -->
m

<!-- b004489 | furniture | pages [14] -->
m

<!-- b004490 | furniture | pages [14] -->
m

<!-- b004491 | furniture | pages [14] -->
m

<!-- b004492 | furniture | pages [14] -->
m

<!-- b004493 | furniture | pages [14] -->
m

<!-- b004494 | furniture | pages [14] -->
m

<!-- b004495 | furniture | pages [14] -->
m

<!-- b004496 | furniture | pages [14] -->
m

<!-- b004497 | furniture | pages [14] -->
m

<!-- b004498 | furniture | pages [14] -->
m

<!-- b004499 | furniture | pages [14] -->
m

<!-- b004500 | furniture | pages [14] -->
m

<!-- b004501 | furniture | pages [14] -->
m

<!-- b004502 | furniture | pages [14] -->
m

<!-- b004503 | furniture | pages [14] -->
m

<!-- b004504 | furniture | pages [14] -->
m

<!-- b004505 | furniture | pages [14] -->
m

<!-- b004506 | furniture | pages [14] -->
m

<!-- b004507 | furniture | pages [14] -->
m

<!-- b004508 | furniture | pages [14] -->
m

<!-- b004509 | furniture | pages [14] -->
m

<!-- b004510 | furniture | pages [14] -->
m

<!-- b004511 | furniture | pages [14] -->
m

<!-- b004512 | furniture | pages [14] -->
m

<!-- b004513 | furniture | pages [14] -->
m

<!-- b004514 | furniture | pages [14] -->
m

<!-- b004515 | furniture | pages [14] -->
m

<!-- b004516 | furniture | pages [14] -->
m

<!-- b004517 | furniture | pages [14] -->
m

<!-- b004518 | furniture | pages [14] -->
m

<!-- b004519 | furniture | pages [14] -->
m

<!-- b004520 | furniture | pages [14] -->
m

<!-- b004521 | furniture | pages [14] -->
m

<!-- b004522 | furniture | pages [14] -->
m

<!-- b004523 | furniture | pages [14] -->
m

<!-- b004524 | furniture | pages [14] -->
m

<!-- b004525 | furniture | pages [14] -->
m

<!-- b004526 | furniture | pages [14] -->
m

<!-- b004527 | furniture | pages [14] -->
m

<!-- b004528 | furniture | pages [14] -->
m

<!-- b004529 | furniture | pages [14] -->
m

<!-- b004530 | furniture | pages [14] -->
m

<!-- b004531 | furniture | pages [14] -->
m

<!-- b004532 | furniture | pages [14] -->
m

<!-- b004533 | furniture | pages [14] -->
m

<!-- b004534 | furniture | pages [14] -->
m

<!-- b004535 | furniture | pages [14] -->
m

<!-- b004536 | furniture | pages [14] -->
m

<!-- b004537 | furniture | pages [14] -->
m

<!-- b004538 | furniture | pages [14] -->
m

<!-- b004539 | furniture | pages [14] -->
m

<!-- b004540 | furniture | pages [14] -->
m

<!-- b004541 | furniture | pages [14] -->
m

<!-- b004542 | furniture | pages [14] -->
m

<!-- b004543 | furniture | pages [14] -->
m

<!-- b004544 | furniture | pages [14] -->
m

<!-- b004545 | furniture | pages [14] -->
m

<!-- b004546 | furniture | pages [14] -->
m

<!-- b004547 | furniture | pages [14] -->
m

<!-- b004548 | furniture | pages [14] -->
m

<!-- b004549 | furniture | pages [14] -->
m

<!-- b004550 | furniture | pages [14] -->
m

<!-- b004551 | furniture | pages [14] -->
m

<!-- b004552 | furniture | pages [14] -->
m

<!-- b004553 | furniture | pages [14] -->
m

<!-- b004554 | furniture | pages [14] -->
m

<!-- b004555 | furniture | pages [14] -->
m

<!-- b004556 | furniture | pages [14] -->
m

<!-- b004557 | furniture | pages [14] -->
m

<!-- b004558 | furniture | pages [14] -->
m

<!-- b004559 | furniture | pages [14] -->
m

<!-- b004560 | furniture | pages [14] -->
m

<!-- b004561 | furniture | pages [14] -->
m

<!-- b004562 | furniture | pages [14] -->
m

<!-- b004563 | furniture | pages [14] -->
m

<!-- b004564 | furniture | pages [14] -->
m

<!-- b004565 | furniture | pages [14] -->
m

<!-- b004566 | furniture | pages [14] -->
m

<!-- b004567 | furniture | pages [14] -->
m

<!-- b004568 | furniture | pages [14] -->
m

<!-- b004569 | furniture | pages [14] -->
m

<!-- b004570 | furniture | pages [14] -->
m

<!-- b004571 | furniture | pages [14] -->
m

<!-- b004572 | furniture | pages [14] -->
m

<!-- b004573 | furniture | pages [14] -->
m

<!-- b004574 | furniture | pages [14] -->
m

<!-- b004575 | furniture | pages [14] -->
m

<!-- b004576 | furniture | pages [14] -->
m

<!-- b004577 | furniture | pages [14] -->
m

<!-- b004578 | furniture | pages [14] -->
m

<!-- b004579 | furniture | pages [14] -->
m

<!-- b004580 | furniture | pages [14] -->
m

<!-- b004581 | furniture | pages [14] -->
m

<!-- b004582 | furniture | pages [14] -->
m

<!-- b004583 | furniture | pages [14] -->
m

<!-- b004584 | furniture | pages [14] -->
m

<!-- b004585 | furniture | pages [14] -->
m

<!-- b004586 | furniture | pages [14] -->
m

<!-- b004587 | furniture | pages [14] -->
m

<!-- b004588 | furniture | pages [14] -->
m

<!-- b004589 | furniture | pages [14] -->
m

<!-- b004590 | furniture | pages [14] -->
m

<!-- b004591 | furniture | pages [14] -->
m

<!-- b004592 | furniture | pages [14] -->
m

<!-- b004593 | furniture | pages [14] -->
m

<!-- b004594 | furniture | pages [14] -->
m

<!-- b004595 | furniture | pages [14] -->
m

<!-- b004596 | furniture | pages [14] -->
m

<!-- b004597 | furniture | pages [14] -->
m

<!-- b004598 | furniture | pages [14] -->
m

<!-- b004599 | furniture | pages [14] -->
m

<!-- b004600 | furniture | pages [14] -->
m

<!-- b004601 | furniture | pages [14] -->
m

<!-- b004602 | furniture | pages [14] -->
m

<!-- b004603 | furniture | pages [14] -->
m

<!-- b004604 | furniture | pages [14] -->
m

<!-- b004605 | furniture | pages [14] -->
m

<!-- b004606 | furniture | pages [14] -->
m

<!-- b004607 | furniture | pages [14] -->
m

<!-- b004608 | furniture | pages [14] -->
m

<!-- b004609 | furniture | pages [14] -->
m

<!-- b004610 | furniture | pages [14] -->
m

<!-- b004611 | furniture | pages [14] -->
m

<!-- b004612 | furniture | pages [14] -->
m

<!-- b004613 | furniture | pages [14] -->
m

<!-- b004614 | furniture | pages [14] -->
m

<!-- b004615 | furniture | pages [14] -->
m

<!-- b004616 | furniture | pages [14] -->
m

<!-- b004617 | furniture | pages [14] -->
m

<!-- b004618 | furniture | pages [14] -->
m

<!-- b004619 | furniture | pages [14] -->
m

<!-- b004620 | furniture | pages [14] -->
m

<!-- b004621 | furniture | pages [14] -->
m

<!-- b004622 | furniture | pages [14] -->
m

<!-- b004623 | furniture | pages [14] -->
m

<!-- b004624 | furniture | pages [14] -->
m

<!-- b004625 | furniture | pages [14] -->
m

<!-- b004626 | furniture | pages [14] -->
m

<!-- b004627 | furniture | pages [14] -->
m

<!-- b004628 | furniture | pages [14] -->
m

<!-- b004629 | furniture | pages [14] -->
m

<!-- b004630 | furniture | pages [14] -->
m

<!-- b004631 | furniture | pages [14] -->
m

<!-- b004632 | furniture | pages [14] -->
m

<!-- b004633 | furniture | pages [14] -->
m

<!-- b004634 | furniture | pages [14] -->
m

<!-- b004635 | furniture | pages [14] -->
m

<!-- b004636 | furniture | pages [14] -->
m

<!-- b004637 | furniture | pages [14] -->
m

<!-- b004638 | furniture | pages [14] -->
m

<!-- b004639 | furniture | pages [14] -->
m

<!-- b004640 | furniture | pages [14] -->
m

<!-- b004641 | furniture | pages [14] -->
m

<!-- b004642 | furniture | pages [14] -->
m

<!-- b004643 | furniture | pages [14] -->
m

<!-- b004644 | furniture | pages [14] -->
m

<!-- b004645 | furniture | pages [14] -->
m

<!-- b004646 | furniture | pages [14] -->
m

<!-- b004647 | furniture | pages [14] -->
m

<!-- b004648 | furniture | pages [14] -->
m

<!-- b004649 | furniture | pages [14] -->
m

<!-- b004650 | furniture | pages [14] -->
m

<!-- b004651 | furniture | pages [14] -->
m

<!-- b004652 | furniture | pages [14] -->
m

<!-- b004653 | furniture | pages [14] -->
m

<!-- b004654 | furniture | pages [14] -->
m

<!-- b004655 | furniture | pages [14] -->
m

<!-- b004656 | furniture | pages [14] -->
m

<!-- b004657 | furniture | pages [14] -->
m

<!-- b004658 | furniture | pages [14] -->
m

<!-- b004659 | furniture | pages [14] -->
m

<!-- b004660 | furniture | pages [14] -->
m

<!-- b004661 | furniture | pages [14] -->
m

<!-- b004662 | furniture | pages [14] -->
m

<!-- b004663 | furniture | pages [14] -->
m

<!-- b004664 | furniture | pages [14] -->
m

<!-- b004665 | furniture | pages [14] -->
m

<!-- b004666 | furniture | pages [14] -->
m

<!-- b004667 | furniture | pages [14] -->
m

<!-- b004668 | furniture | pages [14] -->
m

<!-- b004669 | furniture | pages [14] -->
m

<!-- b004670 | furniture | pages [14] -->
m

<!-- b004671 | furniture | pages [14] -->
m

<!-- b004672 | furniture | pages [14] -->
m

<!-- b004673 | furniture | pages [14] -->
m

<!-- b004674 | furniture | pages [14] -->
m

<!-- b004675 | furniture | pages [14] -->
m

<!-- b004676 | furniture | pages [14] -->
m

<!-- b004677 | furniture | pages [14] -->
m

<!-- b004678 | furniture | pages [14] -->
m

<!-- b004679 | furniture | pages [14] -->
m

<!-- b004680 | furniture | pages [14] -->
m

<!-- b004681 | furniture | pages [14] -->
m

<!-- b004682 | furniture | pages [14] -->
m

<!-- b004683 | furniture | pages [14] -->
m

<!-- b004684 | furniture | pages [14] -->
m

<!-- b004685 | furniture | pages [14] -->
m

<!-- b004686 | furniture | pages [14] -->
m

<!-- b004687 | furniture | pages [14] -->
m

<!-- b004688 | furniture | pages [14] -->
m

<!-- b004689 | furniture | pages [14] -->
m

<!-- b004690 | furniture | pages [14] -->
m

<!-- b004691 | furniture | pages [14] -->
m

<!-- b004692 | furniture | pages [14] -->
m

<!-- b004693 | furniture | pages [14] -->
m

<!-- b004694 | furniture | pages [14] -->
m

<!-- b004695 | furniture | pages [14] -->
m

<!-- b004696 | furniture | pages [14] -->
m

<!-- b004697 | furniture | pages [14] -->
m

<!-- b004698 | furniture | pages [14] -->
m

<!-- b004699 | furniture | pages [14] -->
m

<!-- b004700 | furniture | pages [14] -->
m

<!-- b004701 | furniture | pages [14] -->
m

<!-- b004702 | furniture | pages [14] -->
m

<!-- b004703 | furniture | pages [14] -->
m

<!-- b004704 | furniture | pages [14] -->
m

<!-- b004705 | furniture | pages [14] -->
m

<!-- b004706 | furniture | pages [14] -->
m

<!-- b004707 | furniture | pages [14] -->
m

<!-- b004708 | furniture | pages [14] -->
m

<!-- b004709 | furniture | pages [14] -->
m

<!-- b004710 | furniture | pages [14] -->
m

<!-- b004711 | furniture | pages [14] -->
m

<!-- b004712 | furniture | pages [14] -->
m

<!-- b004713 | furniture | pages [14] -->
m

<!-- b004714 | furniture | pages [14] -->
m

<!-- b004715 | furniture | pages [14] -->
m

<!-- b004716 | furniture | pages [14] -->
m

<!-- b004717 | furniture | pages [14] -->
m

<!-- b004718 | furniture | pages [14] -->
m

<!-- b004719 | furniture | pages [14] -->
m

<!-- b004720 | furniture | pages [14] -->
m

<!-- b004721 | furniture | pages [14] -->
m

<!-- b004722 | furniture | pages [14] -->
m

<!-- b004723 | furniture | pages [14] -->
m

<!-- b004724 | furniture | pages [14] -->
m

<!-- b004725 | furniture | pages [14] -->
m

<!-- b004726 | furniture | pages [14] -->
m

<!-- b004727 | furniture | pages [14] -->
m

<!-- b004728 | furniture | pages [14] -->
m

<!-- b004729 | furniture | pages [14] -->
m

<!-- b004730 | furniture | pages [14] -->
m

<!-- b004731 | furniture | pages [14] -->
m

<!-- b004732 | prose | pages [14] -->
m

<!-- b004733 | prose | pages [14] -->
m

<!-- b004734 | prose | pages [14] -->
m

<!-- b004735 | prose | pages [14] -->
m

<!-- b004736 | prose | pages [14] -->
m

<!-- b004737 | prose | pages [14] -->
m

<!-- b004738 | prose | pages [14] -->
m

<!-- b004739 | prose | pages [14] -->
m

<!-- b004740 | prose | pages [14] -->
m

<!-- b004741 | prose | pages [14] -->
m

<!-- b004742 | prose | pages [14] -->
m

<!-- b004743 | prose | pages [14] -->
m

<!-- b004744 | prose | pages [14] -->
m

<!-- b004745 | prose | pages [14] -->
m

<!-- b004746 | prose | pages [14] -->
m

<!-- b004747 | prose | pages [14] -->
m

<!-- b004748 | prose | pages [14] -->
m

<!-- b004749 | prose | pages [14] -->
m

<!-- b004750 | prose | pages [14] -->
m

<!-- b004751 | prose | pages [14] -->
m

<!-- b004752 | prose | pages [14] -->
m

<!-- b004753 | prose | pages [14] -->
m

<!-- b004754 | prose | pages [14] -->
m

<!-- b004755 | prose | pages [14] -->
m

<!-- b004756 | prose | pages [14] -->
m

<!-- b004757 | prose | pages [14] -->
m

<!-- b004758 | prose | pages [14] -->
m

<!-- b004759 | prose | pages [14] -->
m

<!-- b004760 | prose | pages [14] -->
m

<!-- b004761 | prose | pages [14] -->
m

<!-- b004762 | prose | pages [14] -->
m

<!-- b004763 | prose | pages [14] -->
m

<!-- b004764 | prose | pages [14] -->
m

<!-- b004765 | prose | pages [14] -->
m

<!-- b004766 | prose | pages [14] -->
m

<!-- b004767 | prose | pages [14] -->
m

<!-- b004768 | prose | pages [14] -->
m

<!-- b004769 | prose | pages [14] -->
m

<!-- b004770 | prose | pages [14] -->
m

<!-- b004771 | prose | pages [14] -->
m

<!-- b004772 | prose | pages [14] -->
m

<!-- b004773 | prose | pages [14] -->
m

<!-- b004774 | prose | pages [14] -->
m

<!-- b004775 | prose | pages [14] -->
m

<!-- b004776 | prose | pages [14] -->
m

<!-- b004777 | prose | pages [14] -->
m

<!-- b004778 | prose | pages [14] -->
m

<!-- b004779 | prose | pages [14] -->
m

<!-- b004780 | prose | pages [14] -->
m

<!-- b004781 | prose | pages [14] -->
m

<!-- b004782 | prose | pages [14] -->
m

<!-- b004783 | prose | pages [14] -->
m

<!-- b004784 | prose | pages [14] -->
m

<!-- b004785 | prose | pages [14] -->
m

<!-- b004786 | prose | pages [14] -->
m

<!-- b004787 | prose | pages [14] -->
m

<!-- b004788 | prose | pages [14] -->
m

<!-- b004789 | prose | pages [14] -->
m

<!-- b004790 | prose | pages [14] -->
m

<!-- b004791 | prose | pages [14] -->
m

<!-- b004792 | prose | pages [14] -->
m

<!-- b004793 | prose | pages [14] -->
m

<!-- b004794 | prose | pages [14] -->
m

<!-- b004795 | prose | pages [14] -->
m

<!-- b004796 | prose | pages [14] -->
m

<!-- b004797 | prose | pages [14] -->
m

<!-- b004798 | prose | pages [14] -->
m

<!-- b004799 | prose | pages [14] -->
m

<!-- b004800 | prose | pages [14] -->
m

<!-- b004801 | prose | pages [14] -->
m

<!-- b004802 | prose | pages [14] -->
m

<!-- b004803 | prose | pages [14] -->
m

<!-- b004804 | prose | pages [14] -->
m

<!-- b004805 | prose | pages [14] -->
m

<!-- b004806 | prose | pages [14] -->
m

<!-- b004807 | prose | pages [14] -->
m

<!-- b004808 | prose | pages [14] -->
m

<!-- b004809 | prose | pages [14] -->
m

<!-- b004810 | prose | pages [14] -->
m

<!-- b004811 | prose | pages [14] -->
m

<!-- b004812 | prose | pages [14] -->
m

<!-- b004813 | prose | pages [14] -->
m

<!-- b004814 | prose | pages [14] -->
m

<!-- b004815 | prose | pages [14] -->
m

<!-- b004816 | prose | pages [14] -->
m

<!-- b004817 | prose | pages [14] -->
m

<!-- b004818 | furniture | pages [14] -->
Page 12 of 24

<!-- b004819 | prose | pages [14] -->
S core2 and S core3 are scores computed from secondary scores, and the ﬁnal S core is the overall sum.

<!-- b004820 | prose | pages [14] -->
m

<!-- b004821 | prose | pages [14] -->
m

<!-- b004822 | prose | pages [14] -->
m

<!-- b004823 | prose | pages [14] -->
m

<!-- b004824 | prose | pages [14] -->
m

<!-- b004825 | prose | pages [14] -->
m

<!-- b004826 | prose | pages [14] -->
m

<!-- b004827 | prose | pages [14] -->
m

<!-- b004828 | prose | pages [14] -->
m

<!-- b004829 | prose | pages [14] -->
m

<!-- b004830 | prose | pages [14] -->
m

<!-- b004831 | prose | pages [14] -->
m

<!-- b004832 | prose | pages [14] -->
m

<!-- b004833 | prose | pages [14] -->
m

<!-- b004834 | prose | pages [14] -->
m

<!-- b004835 | prose | pages [14] -->
m

<!-- b004836 | prose | pages [14] -->
m

<!-- b004837 | prose | pages [14] -->
m

<!-- b004838 | prose | pages [14] -->
m

<!-- b004839 | prose | pages [14] -->
m

<!-- b004840 | prose | pages [14] -->
m

<!-- b004841 | prose | pages [14] -->
m

<!-- b004842 | prose | pages [14] -->
m

<!-- b004843 | prose | pages [14] -->
m

<!-- b004844 | prose | pages [14] -->
m

<!-- b004845 | prose | pages [14] -->
m

<!-- b004846 | prose | pages [14] -->
m

<!-- b004847 | prose | pages [14] -->
m

<!-- b004848 | prose | pages [14] -->
m

<!-- b004849 | prose | pages [14] -->
m

<!-- b004850 | prose | pages [14] -->
m

<!-- b004851 | prose | pages [14] -->
m

<!-- b004852 | prose | pages [14] -->
m

<!-- b004853 | prose | pages [14] -->
m

<!-- b004854 | prose | pages [14] -->
m

<!-- b004855 | prose | pages [14] -->
m

<!-- b004856 | prose | pages [14] -->
m

<!-- b004857 | prose | pages [14] -->
m

<!-- b004858 | prose | pages [14] -->
m

<!-- b004859 | prose | pages [14] -->
m

<!-- b004860 | prose | pages [14] -->
m

<!-- b004861 | prose | pages [14] -->
m

<!-- b004862 | prose | pages [14] -->
m

<!-- b004863 | prose | pages [14] -->
m

<!-- b004864 | prose | pages [14] -->
m

<!-- b004865 | prose | pages [14] -->
m

<!-- b004866 | prose | pages [14] -->
m

<!-- b004867 | prose | pages [14] -->
m

<!-- b004868 | prose | pages [14] -->
m

<!-- b004869 | prose | pages [14] -->
m

<!-- b004870 | prose | pages [14] -->
m

<!-- b004871 | prose | pages [14] -->
m

<!-- b004872 | prose | pages [14] -->
m

<!-- b004873 | prose | pages [14] -->
m

<!-- b004874 | prose | pages [14] -->
m

<!-- b004875 | prose | pages [14] -->
m

<!-- b004876 | prose | pages [14] -->
m

<!-- b004877 | prose | pages [14] -->
m

<!-- b004878 | prose | pages [14] -->
m

<!-- b004879 | prose | pages [14] -->
m

<!-- b004880 | prose | pages [14] -->
• w1i, w2i, w3i: the weights assigned to each sub-indicator within the three factors that satisfy %4

<!-- b004881 | prose | pages [14] -->
i=1 wmi = 1, m = 1, 2, 3. This implies that for each main factor, the four sub-indicators sum to a total weight of 1.

<!-- b004882 | prose | pages [14] -->
• wi: the weight assigned to each of the three main factors S core1, S core2, S core3. These must satisfy:

<!-- b004883 | prose | pages [14] -->
3 3 &

<!-- b004884 | prose | pages [14] -->
wi = 1.

<!-- b004885 | prose | pages [14] -->
i=1

<!-- b004886 | prose | pages [14] -->
S core2 = Σ4

<!-- b004887 | prose | pages [14] -->
S core1 = Σ4

<!-- b004888 | prose | pages [14] -->
i=1w1iS 1i

<!-- b004889 | prose | pages [14] -->
S core3 = Σ4 i=1w2iS 2i

<!-- b004890 | prose | pages [14] -->
i=1w3iS 3i

<!-- b004891 | prose | pages [14] -->
S core = Σ3

<!-- b004892 | prose | pages [14] -->
i=1wiS corei

<!-- b004893 | prose | pages [14] -->
According to some materials, the average time of tourists’ stay is around 4 days. So, the average number of tourists in Juneau each day is Nt = 4NJuneau

<!-- b004894 | prose | pages [14] -->
• The increase in average individual income

<!-- b004895 | prose | pages [14] -->
365 .

<!-- b004896 | prose | pages [14] -->
The formula reﬂects the impact of tourism on average individual income by considering the ratio

<!-- b004897 | prose | pages [14] -->
Juneau))↓ε ac-

<!-- b004898 | prose | pages [14] -->
of tax income to population as a measure of income of tourism. The factor (1/(1+H↑

<!-- b004899 | prose | pages [14] -->
counts for the negative inﬂuence of glacier retreat on sustainable tourism growth, assuming that environmental degradation can harm long-term economic beneﬁts. Additionally, the logarithmic term incorporates the proportional allocation of tax revenue (µ1) to infrastructure, reﬂecting how government investments boosts economy. Normalization term T0/P ensures that income growth is evaluated in comparison with a baseline, while logarithm smooth out extreme values.

<!-- b004900 | prose | pages [14] -->
Inc = TJuneau

<!-- b004901 | prose | pages [14] -->
1 · ( 1 + H↑ P

<!-- b004902 | prose | pages [14] -->
)↓ε · (1 + ϱ1 ln µ1 + 1

<!-- b004903 | prose | pages [14] -->
µI + 1) (7)

<!-- b004904 | prose | pages [14] -->
Juneau

<!-- b004905 | prose | pages [14] -->
S 11 = Inc

<!-- b004906 | prose | pages [14] -->
T0/P = TJuneau

<!-- b004907 | prose | pages [14] -->
T0

<!-- b004908 | prose | pages [14] -->
• Crowding level

<!-- b004909 | prose | pages [14] -->
1

<!-- b004910 | prose | pages [14] -->
)↓ε · (1 + ϱ1 ln µ1 + 1

<!-- b004911 | prose | pages [14] -->
· ( · (

<!-- b004912 | prose | pages [14] -->
µI + 1) (8)

<!-- b004913 | prose | pages [14] -->
1 + H↑ Juneau

<!-- b004914 | prose | pages [14] -->
The formula quantiﬁes crowding based on the ratio of average daily tourists to the population (Nt/P), using a Sigmoid function to capture how perceived crowding increases at a decreasing rate as tourist density grows. This ensures that the score accounts for diminishing sensitivity to additional tourists in high-density scenarios. Also, the score is guaranteed to be normalized. Parameters like εc and ς control the steepness and inﬂection point of the curve, respectively.

<!-- b004915 | prose | pages [14] -->
1 S 12 = ϑ · • Housing aﬀordability (9) 1 + e↓εc(Nt/P↓ς)

<!-- b004916 | prose | pages [14] -->
The formula for S 13 estimates housing costs (HCost) based on tourist density (Nt/P) and tax rev- enue allocated to infrastructure (T ↑

<!-- b004917 | prose | pages [14] -->
Juneauµ1). The study by Glaeser et al. [7] reveals the relation between number of tourists and housing aﬀorability.This reﬂects the dual pressures of increased demand for short-term housing and inﬂuences of infrastructure investments. The score is nor- malized within a historical range. The normalization method ensures that higher housing costs reduce the aﬀordability score.

<!-- b004918 | prose | pages [14] -->
关注数学模型

<!-- b004919 | furniture | pages [14] -->
2

<!-- b004920 | furniture | pages [14] -->
MATHmodels

<!-- b004921 | furniture | pages [14] -->
获取更多资讯

<!-- b004922 | furniture | pages [15] -->
Team # 2503268

<!-- b004923 | furniture | pages [15] -->
Page 13 of 24

<!-- b004924 | prose | pages [15] -->
Nt

<!-- b004925 | prose | pages [15] -->
P + ε2T ↑

<!-- b004926 | prose | pages [15] -->
HCost = ε1

<!-- b004927 | prose | pages [15] -->
(10) Juneauµ1

<!-- b004928 | prose | pages [15] -->
S 13 = Cmax ↓HCost

<!-- b004929 | prose | pages [15] -->
• Noise level (11)

<!-- b004930 | prose | pages [15] -->
Cmax ↓Cmin

<!-- b004931 | prose | pages [15] -->
We calculate noise levels as the sum of a baseline noise level (N0) and a power-law term , where

<!-- b004932 | prose | pages [15] -->
微信公众号：数学模型

<!-- b004933 | prose | pages [15] -->
tourist density contributes exponentially to increased noise. The normalization by CNN0 scales the score to reﬂect relative changes. The power-law term avoids extreme values by bounding the output.

<!-- b004934 | prose | pages [15] -->
Noise = N0 + N↑ϱ

<!-- b004935 | prose | pages [15] -->
(12) Juneau

<!-- b004936 | prose | pages [15] -->
= N0 + N↑ϱ

<!-- b004937 | prose | pages [15] -->
S 14 = Noise

<!-- b004938 | prose | pages [15] -->
• Natural resources

<!-- b004939 | prose | pages [15] -->
Juneau

<!-- b004940 | prose | pages [15] -->
(13)

<!-- b004941 | prose | pages [15] -->
CNN0

<!-- b004942 | prose | pages [15] -->
CNN0

<!-- b004943 | prose | pages [15] -->
Measure natural resources by considering glacier retreat and tax revenue allocation to environ- mental protection. A Sigmoid function ensures a smooth transition as environmental pressure increases. The term εN · µE+1

<!-- b004944 | prose | pages [15] -->
µ2+1 · H↑

<!-- b004945 | prose | pages [15] -->
Juneau highlights the trade-oﬀbetween environmental investment

<!-- b004946 | prose | pages [15] -->
微信号：MATHmodels

<!-- b004947 | prose | pages [15] -->
and degradation, as well as avoiding extreme values.

<!-- b004948 | prose | pages [15] -->
S 21 =

<!-- b004949 | prose | pages [15] -->
• Water and energy usage

<!-- b004950 | prose | pages [15] -->
φ0

<!-- b004951 | prose | pages [15] -->
(14)

<!-- b004952 | prose | pages [15] -->
1 + eεN· µE+1 µ2+1 ·H↑

<!-- b004953 | prose | pages [15] -->
Juneau

<!-- b004954 | prose | pages [15] -->
The formula evaluates water and energy consumption based on the combined population and tourist density (P + Nt). Sigmoid function captures the nonlinear relation, with ϱWE controlling the rate of increase and E0 serving as a baseline threshold. Meanwhile, the score is guaranteed to be normalized in this way.

<!-- b004955 | prose | pages [15] -->
Energy = ϱWE(P + Nt)

<!-- b004956 | prose | pages [15] -->
S 22 = 1 ↓

<!-- b004957 | prose | pages [15] -->
(15)

<!-- b004958 | prose | pages [15] -->
e↓(ϱWE(P+Nt)↓E0) 1

<!-- b004959 | prose | pages [15] -->
(16)

<!-- b004960 | prose | pages [15] -->
1 + e↓(Energy↓E0) =

<!-- b004961 | prose | pages [15] -->
• Waste production level

<!-- b004962 | prose | pages [15] -->
1 + e↓(ϱWE(P+Nt)↓E0)

<!-- b004963 | prose | pages [15] -->
Waste production is calculated as the diﬀerence between normalized tourist density (N↑) and waste management impact (ϱCµ3T ↑), with a lower bound of zero. When waste generation ex- ceeds management reduction, penalize the score. The normalization by Cw(N↑+ 1) ensures the score remains bounded.

<!-- b004964 | prose | pages [15] -->
Juneau ↓ϱCµ3T ↑

<!-- b004965 | prose | pages [15] -->
Waste = min(N↑

<!-- b004966 | prose | pages [15] -->
Juneau, 0) (17)

<!-- b004967 | prose | pages [15] -->
Cw(N↑+ 1) = 1 ↓min(N↑ Waste S 23 = 1 ↓

<!-- b004968 | prose | pages [15] -->
• Carbon footprint

<!-- b004969 | prose | pages [15] -->
Juneau ↓ϱCµ3T ↑

<!-- b004970 | prose | pages [15] -->
Juneau, 0)

<!-- b004971 | prose | pages [15] -->
(18)

<!-- b004972 | prose | pages [15] -->
Cw(N↑

<!-- b004973 | prose | pages [15] -->
Juneau + 1)

<!-- b004974 | prose | pages [15] -->
The formula uses a Sigmoid function to keep the score in a reasonable range considering tourist population(Nt). ϑCE and NC control the sensitivity and baseline.

<!-- b004975 | prose | pages [15] -->
1 S 24 = 1 ↓ (19) 1 + eϑCE(NC↓Nt)

<!-- b004976 | furniture | pages [16] -->
Team # 2503268

<!-- b004977 | prose | pages [16] -->
• Tourism tax revenue

<!-- b004978 | furniture | pages [16] -->
Page 14 of 24

<!-- b004979 | prose | pages [16] -->
Normalize the score in a reasonable range with history data.

<!-- b004980 | prose | pages [16] -->
S 31 = TJuneau ↓Tmin

<!-- b004981 | prose | pages [16] -->
• Employment growth

<!-- b004982 | prose | pages [16] -->
(20)

<!-- b004983 | prose | pages [16] -->
Tmax ↓Tmin

<!-- b004984 | prose | pages [16] -->
The S 32 formula models employment growth as a linear combination of normalized tax income (T ↑

<!-- b004985 | prose | pages [16] -->
Juneau) and population (N↑

<!-- b004986 | prose | pages [16] -->
Juneau), with coeﬃcients representing the respective contributions of tourism and local demographics.

<!-- b004987 | prose | pages [16] -->
S 32 = ϱTT ↑

<!-- b004988 | prose | pages [16] -->
• Cultural resource protection or utilization

<!-- b004989 | prose | pages [16] -->
Juneau + ϱNN↑

<!-- b004990 | prose | pages [16] -->
(21) Juneau

<!-- b004991 | prose | pages [16] -->
The S 33 formula measures cultural factors as an inverse exponential function of tax investment

<!-- b004992 | prose | pages [16] -->
Juneau) and number of tourists’ spreading (N↑).

<!-- b004993 | prose | pages [16] -->
of culture (µ4T ↑

<!-- b004994 | prose | pages [16] -->
Juneau)N↑

<!-- b004995 | prose | pages [16] -->
S 33 = (µ4T ↑

<!-- b004996 | prose | pages [16] -->
• Social safety or security index

<!-- b004997 | prose | pages [16] -->
(22)

<!-- b004998 | prose | pages [16] -->
According to study in an article by Hall, C. M. et al. [8], the S 34 formula was constructed to evaluate social safety by considering government allocated investment(µ5T ↑

<!-- b004999 | prose | pages [16] -->
(N↑ Juneau) and population

<!-- b005000 | prose | pages [16] -->
N↑

<!-- b005001 | prose | pages [16] -->
Juneau+1

<!-- b005002 | prose | pages [16] -->
Juneau) on security resources. The term 1 ↓

<!-- b005003 | prose | pages [16] -->
the impact of extreme values.

<!-- b005004 | prose | pages [16] -->
S 34 = 1 ↓

<!-- b005005 | prose | pages [16] -->
6.3 Values of Parameters

<!-- b005006 | prose | pages [16] -->
Juneau+1) prevents division by zero and smooths

<!-- b005007 | prose | pages [16] -->
ϑT µ5(T ↑

<!-- b005008 | prose | pages [16] -->
N↑

<!-- b005009 | prose | pages [16] -->
Juneau + 1

<!-- b005010 | prose | pages [16] -->
(23)

<!-- b005011 | prose | pages [16] -->
ϑTµ5(T ↑

<!-- b005012 | prose | pages [16] -->
Juneau + 1)

<!-- b005013 | prose | pages [16] -->
We estimate the parameters using methods that substitute some speciﬁc values to compute the scores and make the scores reasonable. Some of the parameters are experience-based, and some come from multiplying known data by a certain ratio, which might be a growth rate or a disturbance rate, etc. The following table of parameter values was eventually obtained. 6.4 Weights Distribution Outcomes

<!-- b005014 | prose | pages [16] -->
To calculate the weights of AHP, we compare each each combinations of factors or secondary indicators and build up four judgment matrices. Through consistency check, by making sure CR < 0.1, we guarantee that the matrices are usable. The weights along with other useful calculated results and a heatmap of weights are as follows.

<!-- b005015 | prose | pages [16] -->
7 Analysis of Factors

<!-- b005016 | prose | pages [16] -->
We have now established the STDM model. In this section, we will compare and categorize the various factors, speciﬁcally identifying which components are to be optimized and which will serve as constraints. This analysis directly addresses the requirements of the ﬁrst sub-question in our study.

<!-- b005017 | prose | pages [16] -->
Considering the ultimate goal of sustainable development, all factors listed in the Score Calculation Model can be regarded as Optimization Factors. For the Constraints Factors, we approach the

<!-- b005018 | prose | pages [16] -->
关注数学模型

<!-- b005019 | furniture | pages [16] -->
2

<!-- b005020 | furniture | pages [16] -->
MATHmodels

<!-- b005021 | furniture | pages [16] -->
获取更多资讯

<!-- b005022 | furniture | pages [17] -->
Team # 2503268

<!-- b005023 | prose | pages [17] -->
Parameter Value Parameter Value

<!-- b005024 | furniture | pages [17] -->
Page 15 of 24

<!-- b005025 | prose | pages [17] -->
Parameter Value Parameter Value

<!-- b005026 | prose | pages [17] -->
2448159 0.2 T0 ε

<!-- b005027 | prose | pages [17] -->
0.8 0.6 ϑ εc

<!-- b005028 | prose | pages [17] -->
0.3 0.2 ϱ1 µI

<!-- b005029 | prose | pages [17] -->
2 0.4 ς ε1

<!-- b005030 | prose | pages [17] -->
微信公众号：数学模型

<!-- b005031 | prose | pages [17] -->
0.6 Cmax 0.5 ε2

<!-- b005032 | prose | pages [17] -->
3 CN 1.5 ϱ

<!-- b005033 | prose | pages [17] -->
1

<!-- b005034 | prose | pages [17] -->
0.2 µE ϱWE

<!-- b005035 | prose | pages [17] -->
47528

<!-- b005036 | prose | pages [17] -->
1

<!-- b005037 | prose | pages [17] -->
Cw 1 ϑCE

<!-- b005038 | prose | pages [17] -->
25000

<!-- b005039 | prose | pages [17] -->
Tmin 1029604 0.25 ϱT

<!-- b005040 | prose | pages [17] -->
Cmin 0.2 N0 1

<!-- b005041 | prose | pages [17] -->
1 0.8 φ0 εN

<!-- b005042 | prose | pages [17] -->
E0 1 4 ϱC

<!-- b005043 | prose | pages [17] -->
Nc 24252 Tmax 1632106

<!-- b005044 | prose | pages [17] -->
0.75 5 ϱN ϑt

<!-- b005045 | caption | pages [17] -->
Table 5: Parameter values and their respective values.

<!-- b005046 | prose | pages [17] -->
Parameter Score Score_1 Score_2 Score_3

<!-- b005047 | prose | pages [17] -->
微信号：MATHmodels

<!-- b005048 | prose | pages [17] -->
Judgment Matrix

<!-- b005049 | prose | pages [17] -->


<!-- b005050 | prose | pages [17] -->


<!-- b005051 | prose | pages [17] -->


<!-- b005052 | prose | pages [17] -->
1 0.5 2.5

<!-- b005053 | prose | pages [17] -->
1 3

<!-- b005054 | prose | pages [17] -->
1

<!-- b005055 | prose | pages [17] -->
2 1 4

<!-- b005056 | prose | pages [17] -->
1 3

<!-- b005057 | prose | pages [17] -->
1 1

<!-- b005058 | prose | pages [17] -->
0.4 0.25 1

<!-- b005059 | prose | pages [17] -->
6 3 1 1 5 2

<!-- b005060 | prose | pages [17] -->
Max Eigen-

<!-- b005061 | prose | pages [17] -->
3.006 4.016

<!-- b005062 | prose | pages [17] -->
values

<!-- b005063 | prose | pages [17] -->
Consistency

<!-- b005064 | prose | pages [17] -->
0.0028 0.0052

<!-- b005065 | prose | pages [17] -->
Index (CI)

<!-- b005066 | prose | pages [17] -->
Consistency

<!-- b005067 | prose | pages [17] -->


<!-- b005068 | prose | pages [17] -->


<!-- b005069 | prose | pages [17] -->


<!-- b005070 | prose | pages [17] -->


<!-- b005071 | prose | pages [17] -->


<!-- b005072 | prose | pages [17] -->
6 5

<!-- b005073 | prose | pages [17] -->
1 4 3 2

<!-- b005074 | prose | pages [17] -->
1 1 5 4

<!-- b005075 | prose | pages [17] -->
1 1 1

<!-- b005076 | prose | pages [17] -->
3 2

<!-- b005077 | prose | pages [17] -->
1

<!-- b005078 | prose | pages [17] -->
1 1 6 3

<!-- b005079 | prose | pages [17] -->
4 2 2.5

<!-- b005080 | prose | pages [17] -->
1

<!-- b005081 | prose | pages [17] -->
2

<!-- b005082 | prose | pages [17] -->
1 5 2

<!-- b005083 | prose | pages [17] -->
1 5

<!-- b005084 | prose | pages [17] -->
1

<!-- b005085 | prose | pages [17] -->
1

<!-- b005086 | prose | pages [17] -->
1

<!-- b005087 | prose | pages [17] -->
3

<!-- b005088 | prose | pages [17] -->
3 2 3

<!-- b005089 | prose | pages [17] -->
5 6 6

<!-- b005090 | prose | pages [17] -->
3

<!-- b005091 | prose | pages [17] -->
1 3

<!-- b005092 | prose | pages [17] -->
1 1 6

<!-- b005093 | prose | pages [17] -->
1

<!-- b005094 | prose | pages [17] -->
2 1

<!-- b005095 | prose | pages [17] -->
1

<!-- b005096 | prose | pages [17] -->
2

<!-- b005097 | prose | pages [17] -->
2 2

<!-- b005098 | prose | pages [17] -->
4 3 5

<!-- b005099 | prose | pages [17] -->
4.037 4.024

<!-- b005100 | prose | pages [17] -->
0.0125 0.0079

<!-- b005101 | prose | pages [17] -->
0.0057 < 0.1 0.0048 < 0.1

<!-- b005102 | prose | pages [17] -->
Ratio (CR)

<!-- b005103 | prose | pages [17] -->
Weights 0.3041,

<!-- b005104 | prose | pages [17] -->
0.5784,

<!-- b005105 | prose | pages [17] -->
0.5648,

<!-- b005106 | prose | pages [17] -->
0.2230,

<!-- b005107 | prose | pages [17] -->
0.1311

<!-- b005108 | prose | pages [17] -->
0.0823, 0.1163

<!-- b005109 | prose | pages [17] -->
0.0139 < 0.1 0.0088 < 0.1

<!-- b005110 | prose | pages [17] -->
0.4744,

<!-- b005111 | prose | pages [17] -->
0.4092,

<!-- b005112 | prose | pages [17] -->
0.1011,

<!-- b005113 | prose | pages [17] -->
0.4017,

<!-- b005114 | prose | pages [17] -->
0.1873,

<!-- b005115 | prose | pages [17] -->
0.0795,

<!-- b005116 | prose | pages [17] -->
0.2372

<!-- b005117 | prose | pages [17] -->
0.1096

<!-- b005118 | caption | pages [17] -->
Table 6: Weights Distribution Outcomes for Scores

<!-- b005119 | prose | pages [17] -->
system from three dimensions—population, environment, and economy—examining the limitations imposed by diﬀerent policies on these factors. For instance, as identiﬁed in the Juneau Climate Action and Implementation Plan, the policy introduced by the City of Juneau in 2016, which imposed caps on the number of daily visitors, serves as a constraint within the population dimension.

<!-- b005120 | prose | pages [17] -->
m

<!-- b005121 | prose | pages [17] -->
m

<!-- b005122 | prose | pages [17] -->
m

<!-- b005123 | prose | pages [17] -->
m

<!-- b005124 | prose | pages [17] -->
m

<!-- b005125 | prose | pages [17] -->
m

<!-- b005126 | prose | pages [17] -->
m

<!-- b005127 | prose | pages [17] -->
m

<!-- b005128 | prose | pages [17] -->
m

<!-- b005129 | prose | pages [17] -->
m

<!-- b005130 | prose | pages [17] -->
m

<!-- b005131 | prose | pages [17] -->
m

<!-- b005132 | prose | pages [17] -->
m

<!-- b005133 | prose | pages [17] -->
m

<!-- b005134 | prose | pages [17] -->
m

<!-- b005135 | prose | pages [17] -->
m

<!-- b005136 | prose | pages [17] -->
m

<!-- b005137 | prose | pages [17] -->
m

<!-- b005138 | prose | pages [17] -->
m

<!-- b005139 | prose | pages [17] -->
m

<!-- b005140 | prose | pages [17] -->
m

<!-- b005141 | prose | pages [17] -->
m

<!-- b005142 | prose | pages [17] -->
m

<!-- b005143 | prose | pages [17] -->
m

<!-- b005144 | prose | pages [17] -->
m

<!-- b005145 | prose | pages [17] -->
m

<!-- b005146 | prose | pages [17] -->
m

<!-- b005147 | prose | pages [17] -->
m

<!-- b005148 | prose | pages [17] -->
m

<!-- b005149 | prose | pages [17] -->
m

<!-- b005150 | prose | pages [17] -->
m

<!-- b005151 | prose | pages [17] -->
m

<!-- b005152 | prose | pages [17] -->
m

<!-- b005153 | prose | pages [17] -->
m

<!-- b005154 | prose | pages [17] -->
m

<!-- b005155 | prose | pages [17] -->
m

<!-- b005156 | prose | pages [17] -->
m

<!-- b005157 | prose | pages [17] -->
m

<!-- b005158 | prose | pages [17] -->
m

<!-- b005159 | prose | pages [17] -->
m

<!-- b005160 | prose | pages [17] -->
m

<!-- b005161 | prose | pages [17] -->
m

<!-- b005162 | prose | pages [17] -->
m

<!-- b005163 | prose | pages [17] -->
m

<!-- b005164 | prose | pages [17] -->
m

<!-- b005165 | prose | pages [17] -->
m

<!-- b005166 | prose | pages [17] -->
m

<!-- b005167 | prose | pages [17] -->
m

<!-- b005168 | prose | pages [17] -->
m

<!-- b005169 | prose | pages [17] -->
m

<!-- b005170 | prose | pages [17] -->
m

<!-- b005171 | prose | pages [17] -->
m

<!-- b005172 | prose | pages [17] -->
m

<!-- b005173 | prose | pages [17] -->
m

<!-- b005174 | prose | pages [17] -->
m

<!-- b005175 | prose | pages [17] -->
m

<!-- b005176 | prose | pages [17] -->
m

<!-- b005177 | prose | pages [17] -->
m

<!-- b005178 | prose | pages [17] -->
m

<!-- b005179 | prose | pages [17] -->
m

<!-- b005180 | prose | pages [17] -->
m

<!-- b005181 | prose | pages [17] -->
m

<!-- b005182 | prose | pages [17] -->
m

<!-- b005183 | prose | pages [17] -->
m

<!-- b005184 | prose | pages [17] -->
m

<!-- b005185 | prose | pages [17] -->
m

<!-- b005186 | prose | pages [17] -->
m

<!-- b005187 | prose | pages [17] -->
m

<!-- b005188 | prose | pages [17] -->
m

<!-- b005189 | prose | pages [17] -->
m

<!-- b005190 | prose | pages [17] -->
m

<!-- b005191 | prose | pages [17] -->
m

<!-- b005192 | prose | pages [17] -->
m

<!-- b005193 | prose | pages [17] -->
m

<!-- b005194 | prose | pages [17] -->
m

<!-- b005195 | prose | pages [17] -->
m

<!-- b005196 | prose | pages [17] -->
m

<!-- b005197 | prose | pages [17] -->
m

<!-- b005198 | prose | pages [17] -->
m

<!-- b005199 | prose | pages [17] -->
m

<!-- b005200 | prose | pages [17] -->
m

<!-- b005201 | prose | pages [17] -->
m

<!-- b005202 | prose | pages [17] -->
m

<!-- b005203 | prose | pages [17] -->
m

<!-- b005204 | prose | pages [17] -->
m

<!-- b005205 | prose | pages [17] -->
m

<!-- b005206 | prose | pages [17] -->
m

<!-- b005207 | prose | pages [17] -->
m

<!-- b005208 | prose | pages [17] -->
m

<!-- b005209 | prose | pages [17] -->
m

<!-- b005210 | prose | pages [17] -->
m

<!-- b005211 | prose | pages [17] -->
m

<!-- b005212 | prose | pages [17] -->
m

<!-- b005213 | prose | pages [17] -->
m

<!-- b005214 | prose | pages [17] -->
m

<!-- b005215 | prose | pages [17] -->
m

<!-- b005216 | prose | pages [17] -->
m

<!-- b005217 | prose | pages [17] -->
m

<!-- b005218 | prose | pages [17] -->
m

<!-- b005219 | prose | pages [17] -->
m

<!-- b005220 | prose | pages [17] -->
m

<!-- b005221 | prose | pages [17] -->
m

<!-- b005222 | prose | pages [17] -->
m

<!-- b005223 | prose | pages [17] -->
m

<!-- b005224 | prose | pages [17] -->
m

<!-- b005225 | prose | pages [17] -->
m

<!-- b005226 | prose | pages [17] -->
m

<!-- b005227 | prose | pages [17] -->
m

<!-- b005228 | prose | pages [17] -->
m

<!-- b005229 | prose | pages [17] -->
m

<!-- b005230 | prose | pages [17] -->
m

<!-- b005231 | prose | pages [17] -->
m

<!-- b005232 | prose | pages [17] -->
m

<!-- b005233 | prose | pages [17] -->
m

<!-- b005234 | prose | pages [17] -->
m

<!-- b005235 | prose | pages [17] -->
m

<!-- b005236 | prose | pages [17] -->
m

<!-- b005237 | prose | pages [17] -->
m

<!-- b005238 | prose | pages [17] -->
m

<!-- b005239 | prose | pages [17] -->
m

<!-- b005240 | prose | pages [17] -->
m

<!-- b005241 | prose | pages [17] -->
m

<!-- b005242 | prose | pages [17] -->
m

<!-- b005243 | prose | pages [17] -->
m

<!-- b005244 | prose | pages [17] -->
m

<!-- b005245 | prose | pages [17] -->
m

<!-- b005246 | prose | pages [17] -->
m

<!-- b005247 | prose | pages [17] -->
m

<!-- b005248 | prose | pages [17] -->
m

<!-- b005249 | prose | pages [17] -->
m

<!-- b005250 | prose | pages [17] -->
m

<!-- b005251 | prose | pages [17] -->
m

<!-- b005252 | prose | pages [17] -->
m

<!-- b005253 | prose | pages [17] -->
m

<!-- b005254 | prose | pages [17] -->
m

<!-- b005255 | prose | pages [17] -->
m

<!-- b005256 | prose | pages [17] -->
m

<!-- b005257 | prose | pages [17] -->
m

<!-- b005258 | prose | pages [17] -->
m

<!-- b005259 | prose | pages [17] -->
m

<!-- b005260 | prose | pages [17] -->
m

<!-- b005261 | prose | pages [17] -->
m

<!-- b005262 | prose | pages [17] -->
m

<!-- b005263 | prose | pages [17] -->
m

<!-- b005264 | prose | pages [17] -->
m

<!-- b005265 | prose | pages [17] -->
m

<!-- b005266 | prose | pages [17] -->
m

<!-- b005267 | prose | pages [17] -->
m

<!-- b005268 | prose | pages [17] -->
m

<!-- b005269 | prose | pages [17] -->
m

<!-- b005270 | prose | pages [17] -->
m

<!-- b005271 | prose | pages [17] -->
m

<!-- b005272 | prose | pages [17] -->
m

<!-- b005273 | prose | pages [17] -->
m

<!-- b005274 | prose | pages [17] -->
m

<!-- b005275 | prose | pages [17] -->
m

<!-- b005276 | prose | pages [17] -->
m

<!-- b005277 | prose | pages [17] -->
m

<!-- b005278 | prose | pages [17] -->
m

<!-- b005279 | prose | pages [17] -->
m

<!-- b005280 | prose | pages [17] -->
m

<!-- b005281 | prose | pages [17] -->
m

<!-- b005282 | prose | pages [17] -->
m

<!-- b005283 | prose | pages [17] -->
m

<!-- b005284 | prose | pages [17] -->
m

<!-- b005285 | prose | pages [17] -->
m

<!-- b005286 | prose | pages [17] -->
m

<!-- b005287 | prose | pages [17] -->
m

<!-- b005288 | prose | pages [17] -->
m

<!-- b005289 | prose | pages [17] -->
m

<!-- b005290 | prose | pages [17] -->
m

<!-- b005291 | prose | pages [17] -->
m

<!-- b005292 | prose | pages [17] -->
m

<!-- b005293 | prose | pages [17] -->
m

<!-- b005294 | prose | pages [17] -->
m

<!-- b005295 | prose | pages [17] -->
m

<!-- b005296 | prose | pages [17] -->
m

<!-- b005297 | prose | pages [17] -->
m

<!-- b005298 | prose | pages [17] -->
m

<!-- b005299 | prose | pages [17] -->
m

<!-- b005300 | prose | pages [17] -->
m

<!-- b005301 | prose | pages [17] -->
m

<!-- b005302 | prose | pages [17] -->
m

<!-- b005303 | prose | pages [17] -->
m

<!-- b005304 | prose | pages [17] -->
m

<!-- b005305 | prose | pages [17] -->
m

<!-- b005306 | prose | pages [17] -->
m

<!-- b005307 | prose | pages [17] -->
m

<!-- b005308 | prose | pages [17] -->
m

<!-- b005309 | prose | pages [17] -->
m

<!-- b005310 | prose | pages [17] -->
m

<!-- b005311 | prose | pages [17] -->
m

<!-- b005312 | prose | pages [17] -->
m

<!-- b005313 | prose | pages [17] -->
m

<!-- b005314 | prose | pages [17] -->
m

<!-- b005315 | prose | pages [17] -->
m

<!-- b005316 | prose | pages [17] -->
m

<!-- b005317 | prose | pages [17] -->
m

<!-- b005318 | prose | pages [17] -->
m

<!-- b005319 | prose | pages [17] -->
m

<!-- b005320 | prose | pages [17] -->
m

<!-- b005321 | prose | pages [17] -->
m

<!-- b005322 | prose | pages [17] -->
m

<!-- b005323 | prose | pages [17] -->
m

<!-- b005324 | prose | pages [17] -->
m

<!-- b005325 | prose | pages [17] -->
m

<!-- b005326 | prose | pages [17] -->
m

<!-- b005327 | prose | pages [17] -->
m

<!-- b005328 | prose | pages [17] -->
m

<!-- b005329 | prose | pages [17] -->
m

<!-- b005330 | prose | pages [17] -->
m

<!-- b005331 | prose | pages [17] -->
m

<!-- b005332 | prose | pages [17] -->
m

<!-- b005333 | prose | pages [17] -->
m

<!-- b005334 | prose | pages [17] -->
m

<!-- b005335 | prose | pages [17] -->
m

<!-- b005336 | prose | pages [17] -->
m

<!-- b005337 | prose | pages [17] -->
m

<!-- b005338 | prose | pages [17] -->
m

<!-- b005339 | prose | pages [17] -->
m

<!-- b005340 | prose | pages [17] -->
m

<!-- b005341 | prose | pages [17] -->
m

<!-- b005342 | prose | pages [17] -->
m

<!-- b005343 | prose | pages [17] -->
m

<!-- b005344 | prose | pages [17] -->
m

<!-- b005345 | prose | pages [17] -->
m

<!-- b005346 | prose | pages [17] -->
m

<!-- b005347 | prose | pages [17] -->
m

<!-- b005348 | prose | pages [17] -->
m

<!-- b005349 | prose | pages [17] -->
m

<!-- b005350 | prose | pages [17] -->
m

<!-- b005351 | prose | pages [17] -->
m

<!-- b005352 | prose | pages [17] -->
m

<!-- b005353 | prose | pages [17] -->
m

<!-- b005354 | prose | pages [17] -->
m

<!-- b005355 | prose | pages [17] -->
m

<!-- b005356 | prose | pages [17] -->
m

<!-- b005357 | prose | pages [17] -->
m

<!-- b005358 | prose | pages [17] -->
m

<!-- b005359 | prose | pages [17] -->
m

<!-- b005360 | prose | pages [17] -->
m

<!-- b005361 | prose | pages [17] -->
m

<!-- b005362 | prose | pages [17] -->
m

<!-- b005363 | prose | pages [17] -->
m

<!-- b005364 | prose | pages [17] -->
m

<!-- b005365 | prose | pages [17] -->
m

<!-- b005366 | prose | pages [17] -->
m

<!-- b005367 | prose | pages [17] -->
m

<!-- b005368 | prose | pages [17] -->
m

<!-- b005369 | prose | pages [17] -->
m

<!-- b005370 | prose | pages [17] -->
m

<!-- b005371 | prose | pages [17] -->
m

<!-- b005372 | prose | pages [17] -->
m

<!-- b005373 | prose | pages [17] -->
m

<!-- b005374 | prose | pages [17] -->
m

<!-- b005375 | prose | pages [17] -->
m

<!-- b005376 | prose | pages [17] -->
m

<!-- b005377 | prose | pages [17] -->
m

<!-- b005378 | prose | pages [17] -->
m

<!-- b005379 | prose | pages [17] -->
m

<!-- b005380 | prose | pages [17] -->
m

<!-- b005381 | prose | pages [17] -->
m

<!-- b005382 | prose | pages [17] -->
m

<!-- b005383 | prose | pages [17] -->
m

<!-- b005384 | prose | pages [17] -->
m

<!-- b005385 | prose | pages [17] -->
m

<!-- b005386 | prose | pages [17] -->
m

<!-- b005387 | prose | pages [17] -->
m

<!-- b005388 | prose | pages [17] -->
m

<!-- b005389 | prose | pages [17] -->
m

<!-- b005390 | prose | pages [17] -->
m

<!-- b005391 | prose | pages [17] -->
m

<!-- b005392 | prose | pages [17] -->
m

<!-- b005393 | prose | pages [17] -->
m

<!-- b005394 | prose | pages [17] -->
m

<!-- b005395 | prose | pages [17] -->
m

<!-- b005396 | prose | pages [17] -->
m

<!-- b005397 | prose | pages [17] -->
m

<!-- b005398 | prose | pages [17] -->
m

<!-- b005399 | prose | pages [17] -->
m

<!-- b005400 | prose | pages [17] -->
m

<!-- b005401 | prose | pages [17] -->
m

<!-- b005402 | prose | pages [17] -->
m

<!-- b005403 | prose | pages [17] -->
m

<!-- b005404 | furniture | pages [17] -->
m

<!-- b005405 | furniture | pages [17] -->
m

<!-- b005406 | furniture | pages [17] -->
m

<!-- b005407 | furniture | pages [17] -->
m

<!-- b005408 | furniture | pages [17] -->
m

<!-- b005409 | furniture | pages [17] -->
m

<!-- b005410 | furniture | pages [17] -->
m

<!-- b005411 | furniture | pages [17] -->
m

<!-- b005412 | furniture | pages [17] -->
m

<!-- b005413 | furniture | pages [17] -->
m

<!-- b005414 | furniture | pages [17] -->
m

<!-- b005415 | furniture | pages [17] -->
m

<!-- b005416 | furniture | pages [17] -->
m

<!-- b005417 | furniture | pages [17] -->
m

<!-- b005418 | furniture | pages [17] -->
m

<!-- b005419 | furniture | pages [17] -->
m

<!-- b005420 | furniture | pages [17] -->
m

<!-- b005421 | furniture | pages [17] -->
m

<!-- b005422 | furniture | pages [17] -->
m

<!-- b005423 | furniture | pages [17] -->
m

<!-- b005424 | furniture | pages [17] -->
m

<!-- b005425 | furniture | pages [17] -->
m

<!-- b005426 | furniture | pages [17] -->
m

<!-- b005427 | furniture | pages [17] -->
m

<!-- b005428 | furniture | pages [17] -->
m

<!-- b005429 | furniture | pages [17] -->
m

<!-- b005430 | furniture | pages [17] -->
m

<!-- b005431 | furniture | pages [17] -->
m

<!-- b005432 | furniture | pages [17] -->
m

<!-- b005433 | furniture | pages [17] -->
m

<!-- b005434 | furniture | pages [17] -->
m

<!-- b005435 | furniture | pages [17] -->
m

<!-- b005436 | furniture | pages [17] -->
m

<!-- b005437 | furniture | pages [17] -->
m

<!-- b005438 | furniture | pages [17] -->
m

<!-- b005439 | furniture | pages [17] -->
m

<!-- b005440 | furniture | pages [17] -->
m

<!-- b005441 | furniture | pages [17] -->
m

<!-- b005442 | furniture | pages [17] -->
m

<!-- b005443 | furniture | pages [17] -->
m

<!-- b005444 | furniture | pages [17] -->
m

<!-- b005445 | furniture | pages [17] -->
m

<!-- b005446 | furniture | pages [17] -->
m

<!-- b005447 | furniture | pages [17] -->
m

<!-- b005448 | furniture | pages [17] -->
m

<!-- b005449 | furniture | pages [17] -->
m

<!-- b005450 | furniture | pages [17] -->
m

<!-- b005451 | furniture | pages [17] -->
m

<!-- b005452 | furniture | pages [17] -->
m

<!-- b005453 | furniture | pages [17] -->
m

<!-- b005454 | furniture | pages [17] -->
m

<!-- b005455 | furniture | pages [17] -->
m

<!-- b005456 | furniture | pages [17] -->
m

<!-- b005457 | furniture | pages [17] -->
m

<!-- b005458 | furniture | pages [17] -->
m

<!-- b005459 | furniture | pages [17] -->
m

<!-- b005460 | furniture | pages [17] -->
m

<!-- b005461 | furniture | pages [17] -->
m

<!-- b005462 | furniture | pages [17] -->
m

<!-- b005463 | furniture | pages [17] -->
m

<!-- b005464 | furniture | pages [17] -->
m

<!-- b005465 | furniture | pages [17] -->
m

<!-- b005466 | furniture | pages [17] -->
m

<!-- b005467 | furniture | pages [17] -->
m

<!-- b005468 | furniture | pages [17] -->
m

<!-- b005469 | furniture | pages [17] -->
m

<!-- b005470 | furniture | pages [17] -->
m

<!-- b005471 | furniture | pages [17] -->
m

<!-- b005472 | furniture | pages [17] -->
m

<!-- b005473 | furniture | pages [17] -->
m

<!-- b005474 | furniture | pages [17] -->
m

<!-- b005475 | furniture | pages [17] -->
m

<!-- b005476 | furniture | pages [17] -->
m

<!-- b005477 | furniture | pages [17] -->
m

<!-- b005478 | furniture | pages [17] -->
m

<!-- b005479 | furniture | pages [17] -->
m

<!-- b005480 | furniture | pages [17] -->
m

<!-- b005481 | furniture | pages [17] -->
m

<!-- b005482 | furniture | pages [17] -->
m

<!-- b005483 | furniture | pages [17] -->
m

<!-- b005484 | furniture | pages [17] -->
m

<!-- b005485 | furniture | pages [17] -->
m

<!-- b005486 | furniture | pages [17] -->
m

<!-- b005487 | furniture | pages [17] -->
m

<!-- b005488 | furniture | pages [17] -->
m

<!-- b005489 | furniture | pages [17] -->
m

<!-- b005490 | furniture | pages [17] -->
m

<!-- b005491 | furniture | pages [17] -->
m

<!-- b005492 | furniture | pages [17] -->
m

<!-- b005493 | furniture | pages [17] -->
m

<!-- b005494 | furniture | pages [17] -->
m

<!-- b005495 | furniture | pages [17] -->
m

<!-- b005496 | furniture | pages [17] -->
m

<!-- b005497 | furniture | pages [17] -->
m

<!-- b005498 | furniture | pages [17] -->
m

<!-- b005499 | furniture | pages [17] -->
m

<!-- b005500 | furniture | pages [17] -->
m

<!-- b005501 | furniture | pages [17] -->
m

<!-- b005502 | furniture | pages [17] -->
m

<!-- b005503 | furniture | pages [17] -->
m

<!-- b005504 | furniture | pages [17] -->
m

<!-- b005505 | furniture | pages [17] -->
m

<!-- b005506 | furniture | pages [17] -->
m

<!-- b005507 | furniture | pages [17] -->
m

<!-- b005508 | furniture | pages [17] -->
m

<!-- b005509 | furniture | pages [17] -->
m

<!-- b005510 | furniture | pages [17] -->
m

<!-- b005511 | furniture | pages [17] -->
m

<!-- b005512 | furniture | pages [17] -->
m

<!-- b005513 | furniture | pages [17] -->
m

<!-- b005514 | furniture | pages [17] -->
m

<!-- b005515 | furniture | pages [17] -->
m

<!-- b005516 | furniture | pages [17] -->
m

<!-- b005517 | furniture | pages [17] -->
m

<!-- b005518 | furniture | pages [17] -->
m

<!-- b005519 | furniture | pages [17] -->
m

<!-- b005520 | furniture | pages [17] -->
m

<!-- b005521 | furniture | pages [17] -->
m

<!-- b005522 | furniture | pages [17] -->
m

<!-- b005523 | furniture | pages [17] -->
m

<!-- b005524 | furniture | pages [17] -->
m

<!-- b005525 | furniture | pages [17] -->
m

<!-- b005526 | furniture | pages [17] -->
m

<!-- b005527 | furniture | pages [17] -->
m

<!-- b005528 | furniture | pages [17] -->
m

<!-- b005529 | furniture | pages [17] -->
m

<!-- b005530 | furniture | pages [17] -->
m

<!-- b005531 | furniture | pages [17] -->
m

<!-- b005532 | furniture | pages [17] -->
m

<!-- b005533 | furniture | pages [17] -->
m

<!-- b005534 | furniture | pages [17] -->
m

<!-- b005535 | furniture | pages [17] -->
m

<!-- b005536 | furniture | pages [17] -->
m

<!-- b005537 | furniture | pages [17] -->
m

<!-- b005538 | furniture | pages [17] -->
m

<!-- b005539 | furniture | pages [17] -->
m

<!-- b005540 | furniture | pages [17] -->
m

<!-- b005541 | furniture | pages [17] -->
m

<!-- b005542 | furniture | pages [17] -->
m

<!-- b005543 | furniture | pages [17] -->
m

<!-- b005544 | furniture | pages [17] -->
m

<!-- b005545 | furniture | pages [17] -->
m

<!-- b005546 | furniture | pages [17] -->
m

<!-- b005547 | furniture | pages [17] -->
m

<!-- b005548 | furniture | pages [17] -->
m

<!-- b005549 | furniture | pages [17] -->
m

<!-- b005550 | furniture | pages [17] -->
m

<!-- b005551 | furniture | pages [17] -->
m

<!-- b005552 | furniture | pages [17] -->
m

<!-- b005553 | furniture | pages [17] -->
m

<!-- b005554 | furniture | pages [17] -->
m

<!-- b005555 | furniture | pages [17] -->
m

<!-- b005556 | furniture | pages [17] -->
m

<!-- b005557 | furniture | pages [17] -->
m

<!-- b005558 | furniture | pages [17] -->
m

<!-- b005559 | furniture | pages [17] -->
m

<!-- b005560 | furniture | pages [17] -->
m

<!-- b005561 | furniture | pages [17] -->
m

<!-- b005562 | furniture | pages [17] -->
m

<!-- b005563 | furniture | pages [17] -->
m

<!-- b005564 | furniture | pages [17] -->
m

<!-- b005565 | furniture | pages [17] -->
m

<!-- b005566 | furniture | pages [17] -->
m

<!-- b005567 | furniture | pages [17] -->
m

<!-- b005568 | furniture | pages [17] -->
m

<!-- b005569 | furniture | pages [17] -->
m

<!-- b005570 | furniture | pages [17] -->
m

<!-- b005571 | furniture | pages [17] -->
m

<!-- b005572 | furniture | pages [17] -->
m

<!-- b005573 | furniture | pages [17] -->
m

<!-- b005574 | furniture | pages [17] -->
m

<!-- b005575 | furniture | pages [17] -->
m

<!-- b005576 | furniture | pages [17] -->
m

<!-- b005577 | furniture | pages [17] -->
m

<!-- b005578 | furniture | pages [17] -->
m

<!-- b005579 | furniture | pages [17] -->
m

<!-- b005580 | furniture | pages [17] -->
m

<!-- b005581 | furniture | pages [17] -->
m

<!-- b005582 | furniture | pages [17] -->
m

<!-- b005583 | furniture | pages [17] -->
m

<!-- b005584 | furniture | pages [17] -->
m

<!-- b005585 | furniture | pages [17] -->
m

<!-- b005586 | furniture | pages [17] -->
m

<!-- b005587 | furniture | pages [17] -->
m

<!-- b005588 | furniture | pages [17] -->
m

<!-- b005589 | furniture | pages [17] -->
m

<!-- b005590 | furniture | pages [17] -->
m

<!-- b005591 | furniture | pages [17] -->
m

<!-- b005592 | furniture | pages [17] -->
m

<!-- b005593 | furniture | pages [17] -->
m

<!-- b005594 | furniture | pages [17] -->
m

<!-- b005595 | furniture | pages [17] -->
m

<!-- b005596 | furniture | pages [17] -->
m

<!-- b005597 | furniture | pages [17] -->
m

<!-- b005598 | furniture | pages [17] -->
m

<!-- b005599 | furniture | pages [17] -->
m

<!-- b005600 | furniture | pages [17] -->
m

<!-- b005601 | furniture | pages [17] -->
m

<!-- b005602 | furniture | pages [17] -->
m

<!-- b005603 | furniture | pages [17] -->
m

<!-- b005604 | furniture | pages [17] -->
m

<!-- b005605 | furniture | pages [17] -->
m

<!-- b005606 | furniture | pages [17] -->
m

<!-- b005607 | furniture | pages [17] -->
m

<!-- b005608 | furniture | pages [17] -->
m

<!-- b005609 | furniture | pages [17] -->
m

<!-- b005610 | furniture | pages [17] -->
m

<!-- b005611 | furniture | pages [17] -->
m

<!-- b005612 | furniture | pages [17] -->
m

<!-- b005613 | furniture | pages [17] -->
m

<!-- b005614 | furniture | pages [17] -->
m

<!-- b005615 | furniture | pages [17] -->
m

<!-- b005616 | furniture | pages [17] -->
m

<!-- b005617 | furniture | pages [17] -->
m

<!-- b005618 | furniture | pages [17] -->
m

<!-- b005619 | furniture | pages [17] -->
m

<!-- b005620 | furniture | pages [17] -->
m

<!-- b005621 | furniture | pages [17] -->
m

<!-- b005622 | furniture | pages [17] -->
m

<!-- b005623 | furniture | pages [17] -->
m

<!-- b005624 | furniture | pages [17] -->
m

<!-- b005625 | furniture | pages [17] -->
m

<!-- b005626 | furniture | pages [17] -->
m

<!-- b005627 | furniture | pages [17] -->
m

<!-- b005628 | furniture | pages [17] -->
m

<!-- b005629 | furniture | pages [17] -->
m

<!-- b005630 | furniture | pages [17] -->
m

<!-- b005631 | furniture | pages [17] -->
m

<!-- b005632 | furniture | pages [17] -->
m

<!-- b005633 | furniture | pages [17] -->
m

<!-- b005634 | furniture | pages [17] -->
m

<!-- b005635 | furniture | pages [17] -->
m

<!-- b005636 | furniture | pages [17] -->
m

<!-- b005637 | furniture | pages [17] -->
m

<!-- b005638 | furniture | pages [17] -->
m

<!-- b005639 | furniture | pages [17] -->
m

<!-- b005640 | furniture | pages [17] -->
m

<!-- b005641 | furniture | pages [17] -->
m

<!-- b005642 | furniture | pages [17] -->
m

<!-- b005643 | furniture | pages [17] -->
m

<!-- b005644 | furniture | pages [17] -->
m

<!-- b005645 | furniture | pages [17] -->
m

<!-- b005646 | furniture | pages [17] -->
m

<!-- b005647 | furniture | pages [17] -->
m

<!-- b005648 | furniture | pages [17] -->
m

<!-- b005649 | furniture | pages [17] -->
m

<!-- b005650 | furniture | pages [17] -->
m

<!-- b005651 | furniture | pages [17] -->
m

<!-- b005652 | furniture | pages [17] -->
m

<!-- b005653 | furniture | pages [17] -->
m

<!-- b005654 | furniture | pages [17] -->
m

<!-- b005655 | furniture | pages [17] -->
m

<!-- b005656 | furniture | pages [17] -->
m

<!-- b005657 | furniture | pages [17] -->
m

<!-- b005658 | furniture | pages [17] -->
m

<!-- b005659 | furniture | pages [17] -->
m

<!-- b005660 | furniture | pages [17] -->
m

<!-- b005661 | furniture | pages [17] -->
m

<!-- b005662 | furniture | pages [17] -->
m

<!-- b005663 | furniture | pages [17] -->
m

<!-- b005664 | furniture | pages [17] -->
m

<!-- b005665 | furniture | pages [17] -->
m

<!-- b005666 | furniture | pages [17] -->
m

<!-- b005667 | furniture | pages [17] -->
m

<!-- b005668 | furniture | pages [17] -->
m

<!-- b005669 | furniture | pages [17] -->
m

<!-- b005670 | furniture | pages [17] -->
m

<!-- b005671 | furniture | pages [17] -->
m

<!-- b005672 | furniture | pages [17] -->
m

<!-- b005673 | furniture | pages [17] -->
m

<!-- b005674 | furniture | pages [17] -->
m

<!-- b005675 | furniture | pages [17] -->
m

<!-- b005676 | furniture | pages [17] -->
m

<!-- b005677 | furniture | pages [17] -->
m

<!-- b005678 | furniture | pages [17] -->
m

<!-- b005679 | furniture | pages [17] -->
m

<!-- b005680 | furniture | pages [17] -->
m

<!-- b005681 | furniture | pages [17] -->
m

<!-- b005682 | furniture | pages [17] -->
m

<!-- b005683 | furniture | pages [17] -->
m

<!-- b005684 | furniture | pages [17] -->
m

<!-- b005685 | furniture | pages [17] -->
m

<!-- b005686 | furniture | pages [17] -->
m

<!-- b005687 | furniture | pages [17] -->
m

<!-- b005688 | furniture | pages [17] -->
m

<!-- b005689 | furniture | pages [17] -->
m

<!-- b005690 | furniture | pages [17] -->
m

<!-- b005691 | furniture | pages [17] -->
m

<!-- b005692 | furniture | pages [17] -->
m

<!-- b005693 | furniture | pages [17] -->
m

<!-- b005694 | furniture | pages [17] -->
m

<!-- b005695 | furniture | pages [17] -->
m

<!-- b005696 | furniture | pages [17] -->
m

<!-- b005697 | furniture | pages [17] -->
m

<!-- b005698 | furniture | pages [17] -->
m

<!-- b005699 | furniture | pages [17] -->
m

<!-- b005700 | furniture | pages [17] -->
m

<!-- b005701 | furniture | pages [17] -->
m

<!-- b005702 | furniture | pages [17] -->
m

<!-- b005703 | furniture | pages [17] -->
m

<!-- b005704 | furniture | pages [17] -->
m

<!-- b005705 | furniture | pages [17] -->
m

<!-- b005706 | furniture | pages [17] -->
m

<!-- b005707 | furniture | pages [17] -->
m

<!-- b005708 | furniture | pages [17] -->
m

<!-- b005709 | furniture | pages [17] -->
m

<!-- b005710 | furniture | pages [17] -->
m

<!-- b005711 | furniture | pages [17] -->
m

<!-- b005712 | furniture | pages [17] -->
m

<!-- b005713 | furniture | pages [17] -->
m

<!-- b005714 | furniture | pages [17] -->
m

<!-- b005715 | furniture | pages [17] -->
m

<!-- b005716 | furniture | pages [17] -->
m

<!-- b005717 | furniture | pages [17] -->
m

<!-- b005718 | furniture | pages [17] -->
m

<!-- b005719 | furniture | pages [17] -->
m

<!-- b005720 | furniture | pages [17] -->
m

<!-- b005721 | furniture | pages [17] -->
m

<!-- b005722 | furniture | pages [17] -->
m

<!-- b005723 | furniture | pages [17] -->
m

<!-- b005724 | furniture | pages [17] -->
m

<!-- b005725 | furniture | pages [17] -->
m

<!-- b005726 | furniture | pages [17] -->
m

<!-- b005727 | furniture | pages [17] -->
m

<!-- b005728 | furniture | pages [17] -->
m

<!-- b005729 | furniture | pages [17] -->
m

<!-- b005730 | furniture | pages [17] -->
m

<!-- b005731 | furniture | pages [17] -->
m

<!-- b005732 | furniture | pages [17] -->
m

<!-- b005733 | furniture | pages [17] -->
m

<!-- b005734 | furniture | pages [17] -->
m

<!-- b005735 | furniture | pages [17] -->
m

<!-- b005736 | furniture | pages [17] -->
m

<!-- b005737 | furniture | pages [17] -->
m

<!-- b005738 | furniture | pages [17] -->
m

<!-- b005739 | furniture | pages [17] -->
m

<!-- b005740 | furniture | pages [17] -->
m

<!-- b005741 | furniture | pages [17] -->
m

<!-- b005742 | furniture | pages [17] -->
m

<!-- b005743 | furniture | pages [17] -->
m

<!-- b005744 | furniture | pages [17] -->
m

<!-- b005745 | furniture | pages [17] -->
m

<!-- b005746 | furniture | pages [17] -->
m

<!-- b005747 | furniture | pages [17] -->
m

<!-- b005748 | furniture | pages [17] -->
m

<!-- b005749 | furniture | pages [17] -->
m

<!-- b005750 | furniture | pages [17] -->
m

<!-- b005751 | furniture | pages [17] -->
m

<!-- b005752 | furniture | pages [17] -->
m

<!-- b005753 | furniture | pages [17] -->
m

<!-- b005754 | furniture | pages [17] -->
m

<!-- b005755 | furniture | pages [17] -->
m

<!-- b005756 | furniture | pages [17] -->
m

<!-- b005757 | furniture | pages [17] -->
m

<!-- b005758 | furniture | pages [17] -->
m

<!-- b005759 | furniture | pages [17] -->
m

<!-- b005760 | furniture | pages [17] -->
m

<!-- b005761 | furniture | pages [17] -->
m

<!-- b005762 | furniture | pages [17] -->
m

<!-- b005763 | furniture | pages [17] -->
m

<!-- b005764 | furniture | pages [17] -->
m

<!-- b005765 | furniture | pages [17] -->
m

<!-- b005766 | furniture | pages [17] -->
m

<!-- b005767 | furniture | pages [17] -->
m

<!-- b005768 | furniture | pages [17] -->
m

<!-- b005769 | furniture | pages [17] -->
m

<!-- b005770 | furniture | pages [17] -->
m

<!-- b005771 | furniture | pages [17] -->
m

<!-- b005772 | furniture | pages [17] -->
m

<!-- b005773 | furniture | pages [17] -->
m

<!-- b005774 | furniture | pages [17] -->
m

<!-- b005775 | furniture | pages [17] -->
m

<!-- b005776 | furniture | pages [17] -->
m

<!-- b005777 | furniture | pages [17] -->
m

<!-- b005778 | furniture | pages [17] -->
m

<!-- b005779 | furniture | pages [17] -->
m

<!-- b005780 | furniture | pages [17] -->
m

<!-- b005781 | furniture | pages [17] -->
m

<!-- b005782 | furniture | pages [17] -->
m

<!-- b005783 | furniture | pages [17] -->
m

<!-- b005784 | furniture | pages [17] -->
m

<!-- b005785 | furniture | pages [17] -->
m

<!-- b005786 | furniture | pages [17] -->
m

<!-- b005787 | furniture | pages [17] -->
m

<!-- b005788 | furniture | pages [17] -->
m

<!-- b005789 | furniture | pages [17] -->
m

<!-- b005790 | furniture | pages [17] -->
m

<!-- b005791 | furniture | pages [17] -->
m

<!-- b005792 | furniture | pages [17] -->
m

<!-- b005793 | furniture | pages [17] -->
m

<!-- b005794 | furniture | pages [17] -->
m

<!-- b005795 | furniture | pages [17] -->
m

<!-- b005796 | furniture | pages [17] -->
m

<!-- b005797 | furniture | pages [17] -->
m

<!-- b005798 | furniture | pages [17] -->
m

<!-- b005799 | furniture | pages [17] -->
m

<!-- b005800 | furniture | pages [17] -->
m

<!-- b005801 | furniture | pages [17] -->
m

<!-- b005802 | furniture | pages [17] -->
m

<!-- b005803 | furniture | pages [17] -->
m

<!-- b005804 | furniture | pages [17] -->
m

<!-- b005805 | furniture | pages [17] -->
m

<!-- b005806 | furniture | pages [17] -->
m

<!-- b005807 | furniture | pages [18] -->
Team # 2503268

<!-- b005808 | furniture | pages [18] -->
Page 16 of 24

<!-- b005809 | caption | pages [18] -->
Figure 7: heatmap of weights

<!-- b005810 | prose | pages [18] -->
8

<!-- b005811 | heading | pages [18] -->
Results and Discussion

<!-- b005812 | prose | pages [18] -->
The ﬁtting results of the proposed model are shown in Figure 8, which compares the modeled and observed data for glacier health (H), tourist numbers (N), and hotel tax revenue (T). The red markers represent the observed data, while the blue dashed lines depict the model’s predictions. Overall, the model demonstrates a strong ability to capture the dynamic relationships among the three variables, with certain limitations in speciﬁc scenarios.

<!-- b005813 | caption | pages [18] -->
Figure 8: H, N, T comparisons

<!-- b005814 | prose | pages [18] -->
Based on the intrinsic relationships derived from the HNT data (glacier health, tourism numbers, and economic revenue) between time steps 10 and 19, we developed a quantiﬁable policy evaluation model. By integrating policy parameters (µ1, µ2, µ3, µ4, µ5) into the model, we identiﬁed the intersec- tion between the feasible policy region and the directional optimization boundary. This intersection represents the controllable scope of policies under current conditions. From this range, the model samples points and selects the one yielding the highest evaluation score as the optimal strategy.

<!-- b005815 | prose | pages [18] -->
关注数学模型

<!-- b005816 | furniture | pages [18] -->
2

<!-- b005817 | furniture | pages [18] -->
MATHmodels

<!-- b005818 | furniture | pages [18] -->
获取更多资讯

<!-- b005819 | furniture | pages [19] -->
Team # 2503268

<!-- b005820 | furniture | pages [19] -->
Page 17 of 24

<!-- b005821 | prose | pages [19] -->
As the data of 2019 is the latest we have, we can approximate the situations then as those of now. As calculated, the best combination of allocation and policy is [0.15, 0.10, 0.35, 0.10, 0.30] and [↓3, 3, 4], which represents an allocation focused on safety and waste management and a policy highlighting

<!-- b005822 | prose | pages [19] -->
微信公众号：数学模型

<!-- b005823 | prose | pages [19] -->
comprehensive and balanced development, with a ﬁnal score of 0.6894.

<!-- b005824 | prose | pages [19] -->
We set a baseline of strategies representing a fairly average strategy. Sample some points of speciﬁc time and output the scores after applying our model and baseline and make a comparison, we draw a bar chart:

<!-- b005825 | prose | pages [19] -->
微信号：MATHmodels

<!-- b005826 | caption | pages [19] -->
Figure 9: Baseline & Model Scores

<!-- b005827 | prose | pages [19] -->
According to the ﬁgure, the model-determined strategies make a diﬀerence, performing better than baseline. Under ideal circumstances, our model helps the government with making better decisions.

<!-- b005828 | prose | pages [19] -->
9

<!-- b005829 | heading | pages [19] -->
Sensitivity Analysis

<!-- b005830 | prose | pages [19] -->
9.1 Qualitative analysis: Morris Method

<!-- b005831 | prose | pages [19] -->
In order to understand which parameters predominantly shape the model outputs and where the strongest nonlinear interactions may arise, we perform a Morris global sensitivity analysis on two key aspects of our framework: (i) the ODE parameters {k1, . . . , k11}, which govern how H, N, and T evolve over time, and (ii) the evaluation model, which combines policy-related variables such as µi, ε, and ϱ1 into a single sustainability metric.

<!-- b005832 | caption | pages [19] -->
Figure 10 illustrates these two Morris analyses side by side. The left panel (a) focuses on the ODE

<!-- b005833 | prose | pages [19] -->
parameters, treating the residual ﬁtting cost as the model’s single-output measure, while the right panel (b) targets the evaluation function. In both panels, the horizontal axis µ↔represents each parameter’s main eﬀect: a larger µ↔implies that changes in that parameter lead to larger variations in the output on average. Meanwhile, the vertical axis ω captures interaction or nonlinearity: the higher the ω, the more the parameter’s eﬀect ﬂuctuates across diﬀerent combinations of other parameters.

<!-- b005834 | prose | pages [19] -->
In panel (a), k2 and k6 show the largest µ↔among ODE parameters, signiﬁcantly impacting model

<!-- b005835 | prose | pages [19] -->
m

<!-- b005836 | prose | pages [19] -->
m

<!-- b005837 | prose | pages [19] -->
m

<!-- b005838 | prose | pages [19] -->
m

<!-- b005839 | prose | pages [19] -->
m

<!-- b005840 | prose | pages [19] -->
m

<!-- b005841 | prose | pages [19] -->
m

<!-- b005842 | prose | pages [19] -->
m

<!-- b005843 | prose | pages [19] -->
m

<!-- b005844 | prose | pages [19] -->
m

<!-- b005845 | prose | pages [19] -->
m

<!-- b005846 | prose | pages [19] -->
m

<!-- b005847 | prose | pages [19] -->
m

<!-- b005848 | prose | pages [19] -->
m

<!-- b005849 | prose | pages [19] -->
m

<!-- b005850 | prose | pages [19] -->
m

<!-- b005851 | prose | pages [19] -->
m

<!-- b005852 | prose | pages [19] -->
m

<!-- b005853 | prose | pages [19] -->
m

<!-- b005854 | prose | pages [19] -->
m

<!-- b005855 | prose | pages [19] -->
m

<!-- b005856 | prose | pages [19] -->
m

<!-- b005857 | prose | pages [19] -->
m

<!-- b005858 | prose | pages [19] -->
m

<!-- b005859 | prose | pages [19] -->
m

<!-- b005860 | prose | pages [19] -->
m

<!-- b005861 | prose | pages [19] -->
m

<!-- b005862 | prose | pages [19] -->
m

<!-- b005863 | prose | pages [19] -->
m

<!-- b005864 | prose | pages [19] -->
m

<!-- b005865 | prose | pages [19] -->
m

<!-- b005866 | prose | pages [19] -->
m

<!-- b005867 | prose | pages [19] -->
m

<!-- b005868 | prose | pages [19] -->
m

<!-- b005869 | prose | pages [19] -->
m

<!-- b005870 | prose | pages [19] -->
m

<!-- b005871 | prose | pages [19] -->
m

<!-- b005872 | prose | pages [19] -->
m

<!-- b005873 | prose | pages [19] -->
m

<!-- b005874 | prose | pages [19] -->
m

<!-- b005875 | prose | pages [19] -->
m

<!-- b005876 | prose | pages [19] -->
m

<!-- b005877 | prose | pages [19] -->
m

<!-- b005878 | prose | pages [19] -->
m

<!-- b005879 | prose | pages [19] -->
m

<!-- b005880 | prose | pages [19] -->
m

<!-- b005881 | prose | pages [19] -->
m

<!-- b005882 | prose | pages [19] -->
m

<!-- b005883 | prose | pages [19] -->
m

<!-- b005884 | prose | pages [19] -->
m

<!-- b005885 | prose | pages [19] -->
m

<!-- b005886 | prose | pages [19] -->
m

<!-- b005887 | prose | pages [19] -->
m

<!-- b005888 | prose | pages [19] -->
m

<!-- b005889 | prose | pages [19] -->
m

<!-- b005890 | prose | pages [19] -->
m

<!-- b005891 | prose | pages [19] -->
m

<!-- b005892 | prose | pages [19] -->
m

<!-- b005893 | prose | pages [19] -->
m

<!-- b005894 | prose | pages [19] -->
m

<!-- b005895 | prose | pages [19] -->
m

<!-- b005896 | prose | pages [19] -->
m

<!-- b005897 | prose | pages [19] -->
m

<!-- b005898 | prose | pages [19] -->
m

<!-- b005899 | prose | pages [19] -->
m

<!-- b005900 | prose | pages [19] -->
m

<!-- b005901 | prose | pages [19] -->
m

<!-- b005902 | prose | pages [19] -->
m

<!-- b005903 | prose | pages [19] -->
m

<!-- b005904 | prose | pages [19] -->
m

<!-- b005905 | prose | pages [19] -->
m

<!-- b005906 | prose | pages [19] -->
m

<!-- b005907 | prose | pages [19] -->
m

<!-- b005908 | prose | pages [19] -->
m

<!-- b005909 | prose | pages [19] -->
m

<!-- b005910 | prose | pages [19] -->
m

<!-- b005911 | prose | pages [19] -->
m

<!-- b005912 | prose | pages [19] -->
m

<!-- b005913 | prose | pages [19] -->
m

<!-- b005914 | prose | pages [19] -->
m

<!-- b005915 | prose | pages [19] -->
m

<!-- b005916 | prose | pages [19] -->
m

<!-- b005917 | prose | pages [19] -->
m

<!-- b005918 | prose | pages [19] -->
m

<!-- b005919 | prose | pages [19] -->
m

<!-- b005920 | prose | pages [19] -->
m

<!-- b005921 | prose | pages [19] -->
m

<!-- b005922 | prose | pages [19] -->
m

<!-- b005923 | prose | pages [19] -->
m

<!-- b005924 | prose | pages [19] -->
m

<!-- b005925 | prose | pages [19] -->
m

<!-- b005926 | prose | pages [19] -->
m

<!-- b005927 | prose | pages [19] -->
m

<!-- b005928 | prose | pages [19] -->
m

<!-- b005929 | prose | pages [19] -->
m

<!-- b005930 | prose | pages [19] -->
m

<!-- b005931 | prose | pages [19] -->
m

<!-- b005932 | prose | pages [19] -->
m

<!-- b005933 | prose | pages [19] -->
m

<!-- b005934 | prose | pages [19] -->
m

<!-- b005935 | prose | pages [19] -->
m

<!-- b005936 | prose | pages [19] -->
m

<!-- b005937 | prose | pages [19] -->
m

<!-- b005938 | prose | pages [19] -->
m

<!-- b005939 | prose | pages [19] -->
m

<!-- b005940 | prose | pages [19] -->
m

<!-- b005941 | prose | pages [19] -->
m

<!-- b005942 | prose | pages [19] -->
m

<!-- b005943 | prose | pages [19] -->
m

<!-- b005944 | prose | pages [19] -->
m

<!-- b005945 | prose | pages [19] -->
m

<!-- b005946 | prose | pages [19] -->
m

<!-- b005947 | prose | pages [19] -->
m

<!-- b005948 | prose | pages [19] -->
m

<!-- b005949 | prose | pages [19] -->
m

<!-- b005950 | prose | pages [19] -->
m

<!-- b005951 | prose | pages [19] -->
m

<!-- b005952 | prose | pages [19] -->
m

<!-- b005953 | prose | pages [19] -->
m

<!-- b005954 | prose | pages [19] -->
m

<!-- b005955 | prose | pages [19] -->
m

<!-- b005956 | prose | pages [19] -->
m

<!-- b005957 | prose | pages [19] -->
m

<!-- b005958 | prose | pages [19] -->
m

<!-- b005959 | prose | pages [19] -->
m

<!-- b005960 | prose | pages [19] -->
m

<!-- b005961 | prose | pages [19] -->
m

<!-- b005962 | prose | pages [19] -->
m

<!-- b005963 | prose | pages [19] -->
m

<!-- b005964 | prose | pages [19] -->
m

<!-- b005965 | prose | pages [19] -->
m

<!-- b005966 | prose | pages [19] -->
m

<!-- b005967 | prose | pages [19] -->
m

<!-- b005968 | prose | pages [19] -->
m

<!-- b005969 | prose | pages [19] -->
m

<!-- b005970 | prose | pages [19] -->
m

<!-- b005971 | prose | pages [19] -->
m

<!-- b005972 | prose | pages [19] -->
m

<!-- b005973 | prose | pages [19] -->
m

<!-- b005974 | prose | pages [19] -->
m

<!-- b005975 | prose | pages [19] -->
m

<!-- b005976 | prose | pages [19] -->
m

<!-- b005977 | prose | pages [19] -->
m

<!-- b005978 | prose | pages [19] -->
m

<!-- b005979 | prose | pages [19] -->
m

<!-- b005980 | prose | pages [19] -->
m

<!-- b005981 | prose | pages [19] -->
m

<!-- b005982 | prose | pages [19] -->
m

<!-- b005983 | prose | pages [19] -->
m

<!-- b005984 | prose | pages [19] -->
m

<!-- b005985 | prose | pages [19] -->
m

<!-- b005986 | prose | pages [19] -->
m

<!-- b005987 | prose | pages [19] -->
m

<!-- b005988 | prose | pages [19] -->
m

<!-- b005989 | prose | pages [19] -->
m

<!-- b005990 | prose | pages [19] -->
m

<!-- b005991 | prose | pages [19] -->
m

<!-- b005992 | prose | pages [19] -->
m

<!-- b005993 | prose | pages [19] -->
m

<!-- b005994 | prose | pages [19] -->
m

<!-- b005995 | prose | pages [19] -->
m

<!-- b005996 | prose | pages [19] -->
m

<!-- b005997 | prose | pages [19] -->
m

<!-- b005998 | prose | pages [19] -->
m

<!-- b005999 | prose | pages [19] -->
m

<!-- b006000 | prose | pages [19] -->
m

<!-- b006001 | prose | pages [19] -->
m

<!-- b006002 | prose | pages [19] -->
m

<!-- b006003 | prose | pages [19] -->
m

<!-- b006004 | prose | pages [19] -->
m

<!-- b006005 | prose | pages [19] -->
m

<!-- b006006 | prose | pages [19] -->
m

<!-- b006007 | prose | pages [19] -->
m

<!-- b006008 | prose | pages [19] -->
m

<!-- b006009 | prose | pages [19] -->
m

<!-- b006010 | prose | pages [19] -->
m

<!-- b006011 | prose | pages [19] -->
m

<!-- b006012 | prose | pages [19] -->
m

<!-- b006013 | prose | pages [19] -->
m

<!-- b006014 | prose | pages [19] -->
m

<!-- b006015 | prose | pages [19] -->
m

<!-- b006016 | prose | pages [19] -->
m

<!-- b006017 | prose | pages [19] -->
m

<!-- b006018 | prose | pages [19] -->
m

<!-- b006019 | prose | pages [19] -->
m

<!-- b006020 | prose | pages [19] -->
m

<!-- b006021 | prose | pages [19] -->
m

<!-- b006022 | prose | pages [19] -->
m

<!-- b006023 | prose | pages [19] -->
m

<!-- b006024 | prose | pages [19] -->
m

<!-- b006025 | prose | pages [19] -->
m

<!-- b006026 | prose | pages [19] -->
m

<!-- b006027 | prose | pages [19] -->
m

<!-- b006028 | prose | pages [19] -->
m

<!-- b006029 | prose | pages [19] -->
m

<!-- b006030 | prose | pages [19] -->
m

<!-- b006031 | prose | pages [19] -->
m

<!-- b006032 | prose | pages [19] -->
m

<!-- b006033 | prose | pages [19] -->
m

<!-- b006034 | prose | pages [19] -->
m

<!-- b006035 | prose | pages [19] -->
m

<!-- b006036 | prose | pages [19] -->
m

<!-- b006037 | prose | pages [19] -->
m

<!-- b006038 | prose | pages [19] -->
m

<!-- b006039 | prose | pages [19] -->
m

<!-- b006040 | prose | pages [19] -->
m

<!-- b006041 | prose | pages [19] -->
m

<!-- b006042 | prose | pages [19] -->
m

<!-- b006043 | prose | pages [19] -->
m

<!-- b006044 | prose | pages [19] -->
m

<!-- b006045 | prose | pages [19] -->
m

<!-- b006046 | prose | pages [19] -->
m

<!-- b006047 | prose | pages [19] -->
m

<!-- b006048 | prose | pages [19] -->
m

<!-- b006049 | prose | pages [19] -->
m

<!-- b006050 | prose | pages [19] -->
m

<!-- b006051 | prose | pages [19] -->
m

<!-- b006052 | prose | pages [19] -->
m

<!-- b006053 | prose | pages [19] -->
m

<!-- b006054 | prose | pages [19] -->
m

<!-- b006055 | prose | pages [19] -->
m

<!-- b006056 | prose | pages [19] -->
m

<!-- b006057 | prose | pages [19] -->
m

<!-- b006058 | prose | pages [19] -->
m

<!-- b006059 | prose | pages [19] -->
m

<!-- b006060 | prose | pages [19] -->
m

<!-- b006061 | prose | pages [19] -->
m

<!-- b006062 | prose | pages [19] -->
m

<!-- b006063 | prose | pages [19] -->
m

<!-- b006064 | prose | pages [19] -->
m

<!-- b006065 | prose | pages [19] -->
m

<!-- b006066 | prose | pages [19] -->
m

<!-- b006067 | prose | pages [19] -->
m

<!-- b006068 | prose | pages [19] -->
m

<!-- b006069 | prose | pages [19] -->
m

<!-- b006070 | prose | pages [19] -->
m

<!-- b006071 | prose | pages [19] -->
m

<!-- b006072 | prose | pages [19] -->
m

<!-- b006073 | prose | pages [19] -->
m

<!-- b006074 | prose | pages [19] -->
m

<!-- b006075 | prose | pages [19] -->
m

<!-- b006076 | prose | pages [19] -->
m

<!-- b006077 | prose | pages [19] -->
m

<!-- b006078 | prose | pages [19] -->
m

<!-- b006079 | prose | pages [19] -->
m

<!-- b006080 | prose | pages [19] -->
m

<!-- b006081 | prose | pages [19] -->
m

<!-- b006082 | prose | pages [19] -->
m

<!-- b006083 | prose | pages [19] -->
m

<!-- b006084 | prose | pages [19] -->
m

<!-- b006085 | prose | pages [19] -->
m

<!-- b006086 | prose | pages [19] -->
m

<!-- b006087 | prose | pages [19] -->
m

<!-- b006088 | prose | pages [19] -->
m

<!-- b006089 | prose | pages [19] -->
m

<!-- b006090 | prose | pages [19] -->
m

<!-- b006091 | prose | pages [19] -->
m

<!-- b006092 | prose | pages [19] -->
m

<!-- b006093 | prose | pages [19] -->
m

<!-- b006094 | prose | pages [19] -->
m

<!-- b006095 | prose | pages [19] -->
m

<!-- b006096 | prose | pages [19] -->
m

<!-- b006097 | prose | pages [19] -->
m

<!-- b006098 | prose | pages [19] -->
m

<!-- b006099 | prose | pages [19] -->
m

<!-- b006100 | prose | pages [19] -->
m

<!-- b006101 | prose | pages [19] -->
m

<!-- b006102 | prose | pages [19] -->
m

<!-- b006103 | prose | pages [19] -->
m

<!-- b006104 | prose | pages [19] -->
m

<!-- b006105 | prose | pages [19] -->
m

<!-- b006106 | prose | pages [19] -->
m

<!-- b006107 | prose | pages [19] -->
m

<!-- b006108 | prose | pages [19] -->
m

<!-- b006109 | prose | pages [19] -->
m

<!-- b006110 | prose | pages [19] -->
m

<!-- b006111 | prose | pages [19] -->
m

<!-- b006112 | prose | pages [19] -->
m

<!-- b006113 | prose | pages [19] -->
m

<!-- b006114 | prose | pages [19] -->
m

<!-- b006115 | prose | pages [19] -->
m

<!-- b006116 | prose | pages [19] -->
m

<!-- b006117 | prose | pages [19] -->
m

<!-- b006118 | prose | pages [19] -->
m

<!-- b006119 | furniture | pages [19] -->
m

<!-- b006120 | furniture | pages [19] -->
m

<!-- b006121 | furniture | pages [19] -->
m

<!-- b006122 | furniture | pages [19] -->
m

<!-- b006123 | furniture | pages [19] -->
m

<!-- b006124 | furniture | pages [19] -->
m

<!-- b006125 | furniture | pages [19] -->
m

<!-- b006126 | furniture | pages [19] -->
m

<!-- b006127 | furniture | pages [19] -->
m

<!-- b006128 | furniture | pages [19] -->
m

<!-- b006129 | furniture | pages [19] -->
m

<!-- b006130 | furniture | pages [19] -->
m

<!-- b006131 | furniture | pages [19] -->
m

<!-- b006132 | furniture | pages [19] -->
m

<!-- b006133 | furniture | pages [19] -->
m

<!-- b006134 | furniture | pages [19] -->
m

<!-- b006135 | furniture | pages [19] -->
m

<!-- b006136 | furniture | pages [19] -->
m

<!-- b006137 | furniture | pages [19] -->
m

<!-- b006138 | furniture | pages [19] -->
m

<!-- b006139 | furniture | pages [19] -->
m

<!-- b006140 | furniture | pages [19] -->
m

<!-- b006141 | furniture | pages [19] -->
m

<!-- b006142 | furniture | pages [19] -->
m

<!-- b006143 | furniture | pages [19] -->
m

<!-- b006144 | furniture | pages [19] -->
m

<!-- b006145 | furniture | pages [19] -->
m

<!-- b006146 | furniture | pages [19] -->
m

<!-- b006147 | furniture | pages [19] -->
m

<!-- b006148 | furniture | pages [19] -->
m

<!-- b006149 | furniture | pages [19] -->
m

<!-- b006150 | furniture | pages [19] -->
m

<!-- b006151 | furniture | pages [19] -->
m

<!-- b006152 | furniture | pages [19] -->
m

<!-- b006153 | furniture | pages [19] -->
m

<!-- b006154 | furniture | pages [19] -->
m

<!-- b006155 | furniture | pages [19] -->
m

<!-- b006156 | furniture | pages [19] -->
m

<!-- b006157 | furniture | pages [19] -->
m

<!-- b006158 | furniture | pages [19] -->
m

<!-- b006159 | furniture | pages [19] -->
m

<!-- b006160 | furniture | pages [19] -->
m

<!-- b006161 | furniture | pages [19] -->
m

<!-- b006162 | furniture | pages [19] -->
m

<!-- b006163 | furniture | pages [19] -->
m

<!-- b006164 | furniture | pages [19] -->
m

<!-- b006165 | furniture | pages [19] -->
m

<!-- b006166 | furniture | pages [19] -->
m

<!-- b006167 | furniture | pages [19] -->
m

<!-- b006168 | furniture | pages [19] -->
m

<!-- b006169 | furniture | pages [19] -->
m

<!-- b006170 | furniture | pages [19] -->
m

<!-- b006171 | furniture | pages [19] -->
m

<!-- b006172 | furniture | pages [19] -->
m

<!-- b006173 | furniture | pages [19] -->
m

<!-- b006174 | furniture | pages [19] -->
m

<!-- b006175 | furniture | pages [19] -->
m

<!-- b006176 | furniture | pages [19] -->
m

<!-- b006177 | furniture | pages [19] -->
m

<!-- b006178 | furniture | pages [19] -->
m

<!-- b006179 | furniture | pages [19] -->
m

<!-- b006180 | furniture | pages [19] -->
m

<!-- b006181 | furniture | pages [19] -->
m

<!-- b006182 | furniture | pages [19] -->
m

<!-- b006183 | furniture | pages [19] -->
m

<!-- b006184 | furniture | pages [19] -->
m

<!-- b006185 | furniture | pages [19] -->
m

<!-- b006186 | furniture | pages [19] -->
m

<!-- b006187 | furniture | pages [19] -->
m

<!-- b006188 | furniture | pages [19] -->
m

<!-- b006189 | furniture | pages [19] -->
m

<!-- b006190 | furniture | pages [19] -->
m

<!-- b006191 | furniture | pages [19] -->
m

<!-- b006192 | furniture | pages [19] -->
m

<!-- b006193 | furniture | pages [19] -->
m

<!-- b006194 | furniture | pages [19] -->
m

<!-- b006195 | furniture | pages [19] -->
m

<!-- b006196 | furniture | pages [19] -->
m

<!-- b006197 | furniture | pages [19] -->
m

<!-- b006198 | furniture | pages [19] -->
m

<!-- b006199 | furniture | pages [19] -->
m

<!-- b006200 | furniture | pages [19] -->
m

<!-- b006201 | furniture | pages [19] -->
m

<!-- b006202 | furniture | pages [19] -->
m

<!-- b006203 | furniture | pages [19] -->
m

<!-- b006204 | furniture | pages [19] -->
m

<!-- b006205 | furniture | pages [19] -->
m

<!-- b006206 | furniture | pages [19] -->
m

<!-- b006207 | furniture | pages [19] -->
m

<!-- b006208 | furniture | pages [19] -->
m

<!-- b006209 | furniture | pages [19] -->
m

<!-- b006210 | furniture | pages [19] -->
m

<!-- b006211 | furniture | pages [19] -->
m

<!-- b006212 | furniture | pages [19] -->
m

<!-- b006213 | furniture | pages [19] -->
m

<!-- b006214 | furniture | pages [19] -->
m

<!-- b006215 | furniture | pages [19] -->
m

<!-- b006216 | furniture | pages [19] -->
m

<!-- b006217 | furniture | pages [19] -->
m

<!-- b006218 | furniture | pages [19] -->
m

<!-- b006219 | furniture | pages [19] -->
m

<!-- b006220 | furniture | pages [19] -->
m

<!-- b006221 | furniture | pages [19] -->
m

<!-- b006222 | furniture | pages [19] -->
m

<!-- b006223 | furniture | pages [19] -->
m

<!-- b006224 | furniture | pages [19] -->
m

<!-- b006225 | furniture | pages [19] -->
m

<!-- b006226 | furniture | pages [19] -->
m

<!-- b006227 | furniture | pages [19] -->
m

<!-- b006228 | furniture | pages [19] -->
m

<!-- b006229 | furniture | pages [19] -->
m

<!-- b006230 | furniture | pages [19] -->
m

<!-- b006231 | furniture | pages [19] -->
m

<!-- b006232 | furniture | pages [19] -->
m

<!-- b006233 | furniture | pages [19] -->
m

<!-- b006234 | furniture | pages [19] -->
m

<!-- b006235 | furniture | pages [19] -->
m

<!-- b006236 | furniture | pages [19] -->
m

<!-- b006237 | furniture | pages [19] -->
m

<!-- b006238 | furniture | pages [19] -->
m

<!-- b006239 | furniture | pages [19] -->
m

<!-- b006240 | furniture | pages [19] -->
m

<!-- b006241 | furniture | pages [19] -->
m

<!-- b006242 | furniture | pages [19] -->
m

<!-- b006243 | furniture | pages [19] -->
m

<!-- b006244 | furniture | pages [19] -->
m

<!-- b006245 | furniture | pages [19] -->
m

<!-- b006246 | furniture | pages [19] -->
m

<!-- b006247 | furniture | pages [19] -->
m

<!-- b006248 | furniture | pages [19] -->
m

<!-- b006249 | furniture | pages [19] -->
m

<!-- b006250 | furniture | pages [19] -->
m

<!-- b006251 | furniture | pages [19] -->
m

<!-- b006252 | furniture | pages [19] -->
m

<!-- b006253 | furniture | pages [19] -->
m

<!-- b006254 | furniture | pages [19] -->
m

<!-- b006255 | furniture | pages [19] -->
m

<!-- b006256 | furniture | pages [19] -->
m

<!-- b006257 | furniture | pages [19] -->
m

<!-- b006258 | furniture | pages [19] -->
m

<!-- b006259 | furniture | pages [19] -->
m

<!-- b006260 | furniture | pages [19] -->
m

<!-- b006261 | furniture | pages [19] -->
m

<!-- b006262 | furniture | pages [19] -->
m

<!-- b006263 | furniture | pages [19] -->
m

<!-- b006264 | furniture | pages [19] -->
m

<!-- b006265 | furniture | pages [19] -->
m

<!-- b006266 | furniture | pages [19] -->
m

<!-- b006267 | furniture | pages [19] -->
m

<!-- b006268 | furniture | pages [19] -->
m

<!-- b006269 | furniture | pages [19] -->
m

<!-- b006270 | furniture | pages [19] -->
m

<!-- b006271 | furniture | pages [19] -->
m

<!-- b006272 | furniture | pages [19] -->
m

<!-- b006273 | furniture | pages [19] -->
m

<!-- b006274 | furniture | pages [19] -->
m

<!-- b006275 | furniture | pages [19] -->
m

<!-- b006276 | furniture | pages [19] -->
m

<!-- b006277 | furniture | pages [19] -->
m

<!-- b006278 | furniture | pages [19] -->
m

<!-- b006279 | furniture | pages [19] -->
m

<!-- b006280 | furniture | pages [19] -->
m

<!-- b006281 | furniture | pages [19] -->
m

<!-- b006282 | furniture | pages [19] -->
m

<!-- b006283 | furniture | pages [19] -->
m

<!-- b006284 | furniture | pages [19] -->
m

<!-- b006285 | furniture | pages [19] -->
m

<!-- b006286 | furniture | pages [19] -->
m

<!-- b006287 | furniture | pages [19] -->
m

<!-- b006288 | furniture | pages [19] -->
m

<!-- b006289 | furniture | pages [19] -->
m

<!-- b006290 | furniture | pages [19] -->
m

<!-- b006291 | furniture | pages [19] -->
m

<!-- b006292 | furniture | pages [19] -->
m

<!-- b006293 | furniture | pages [19] -->
m

<!-- b006294 | furniture | pages [19] -->
m

<!-- b006295 | furniture | pages [19] -->
m

<!-- b006296 | furniture | pages [19] -->
m

<!-- b006297 | furniture | pages [19] -->
m

<!-- b006298 | furniture | pages [19] -->
m

<!-- b006299 | furniture | pages [19] -->
m

<!-- b006300 | furniture | pages [19] -->
m

<!-- b006301 | furniture | pages [19] -->
m

<!-- b006302 | furniture | pages [19] -->
m

<!-- b006303 | furniture | pages [19] -->
m

<!-- b006304 | furniture | pages [19] -->
m

<!-- b006305 | furniture | pages [19] -->
m

<!-- b006306 | furniture | pages [19] -->
m

<!-- b006307 | furniture | pages [19] -->
m

<!-- b006308 | furniture | pages [19] -->
m

<!-- b006309 | furniture | pages [19] -->
m

<!-- b006310 | furniture | pages [19] -->
m

<!-- b006311 | furniture | pages [19] -->
m

<!-- b006312 | furniture | pages [19] -->
m

<!-- b006313 | furniture | pages [19] -->
m

<!-- b006314 | furniture | pages [19] -->
m

<!-- b006315 | furniture | pages [19] -->
m

<!-- b006316 | furniture | pages [19] -->
m

<!-- b006317 | furniture | pages [19] -->
m

<!-- b006318 | furniture | pages [19] -->
m

<!-- b006319 | furniture | pages [19] -->
m

<!-- b006320 | furniture | pages [19] -->
m

<!-- b006321 | furniture | pages [19] -->
m

<!-- b006322 | furniture | pages [19] -->
m

<!-- b006323 | furniture | pages [19] -->
m

<!-- b006324 | furniture | pages [19] -->
m

<!-- b006325 | furniture | pages [19] -->
m

<!-- b006326 | furniture | pages [19] -->
m

<!-- b006327 | furniture | pages [19] -->
m

<!-- b006328 | furniture | pages [19] -->
m

<!-- b006329 | furniture | pages [19] -->
m

<!-- b006330 | furniture | pages [19] -->
m

<!-- b006331 | furniture | pages [19] -->
m

<!-- b006332 | furniture | pages [19] -->
m

<!-- b006333 | furniture | pages [19] -->
m

<!-- b006334 | furniture | pages [19] -->
m

<!-- b006335 | furniture | pages [19] -->
m

<!-- b006336 | furniture | pages [19] -->
m

<!-- b006337 | furniture | pages [19] -->
m

<!-- b006338 | furniture | pages [19] -->
m

<!-- b006339 | furniture | pages [19] -->
m

<!-- b006340 | furniture | pages [19] -->
m

<!-- b006341 | furniture | pages [19] -->
m

<!-- b006342 | furniture | pages [19] -->
m

<!-- b006343 | furniture | pages [19] -->
m

<!-- b006344 | furniture | pages [19] -->
m

<!-- b006345 | furniture | pages [19] -->
m

<!-- b006346 | furniture | pages [19] -->
m

<!-- b006347 | furniture | pages [19] -->
m

<!-- b006348 | furniture | pages [19] -->
m

<!-- b006349 | furniture | pages [19] -->
m

<!-- b006350 | furniture | pages [19] -->
m

<!-- b006351 | furniture | pages [19] -->
m

<!-- b006352 | furniture | pages [19] -->
m

<!-- b006353 | furniture | pages [19] -->
m

<!-- b006354 | furniture | pages [19] -->
m

<!-- b006355 | furniture | pages [19] -->
m

<!-- b006356 | furniture | pages [19] -->
m

<!-- b006357 | furniture | pages [19] -->
m

<!-- b006358 | furniture | pages [19] -->
m

<!-- b006359 | furniture | pages [19] -->
m

<!-- b006360 | furniture | pages [19] -->
m

<!-- b006361 | furniture | pages [19] -->
m

<!-- b006362 | furniture | pages [19] -->
m

<!-- b006363 | furniture | pages [19] -->
m

<!-- b006364 | furniture | pages [19] -->
m

<!-- b006365 | furniture | pages [19] -->
m

<!-- b006366 | furniture | pages [19] -->
m

<!-- b006367 | furniture | pages [19] -->
m

<!-- b006368 | furniture | pages [19] -->
m

<!-- b006369 | furniture | pages [19] -->
m

<!-- b006370 | furniture | pages [19] -->
m

<!-- b006371 | furniture | pages [19] -->
m

<!-- b006372 | furniture | pages [19] -->
m

<!-- b006373 | furniture | pages [19] -->
m

<!-- b006374 | furniture | pages [19] -->
m

<!-- b006375 | furniture | pages [19] -->
m

<!-- b006376 | furniture | pages [19] -->
m

<!-- b006377 | furniture | pages [19] -->
m

<!-- b006378 | furniture | pages [19] -->
m

<!-- b006379 | furniture | pages [19] -->
m

<!-- b006380 | furniture | pages [19] -->
m

<!-- b006381 | furniture | pages [19] -->
m

<!-- b006382 | furniture | pages [19] -->
m

<!-- b006383 | furniture | pages [19] -->
m

<!-- b006384 | furniture | pages [19] -->
m

<!-- b006385 | furniture | pages [19] -->
m

<!-- b006386 | furniture | pages [19] -->
m

<!-- b006387 | furniture | pages [19] -->
m

<!-- b006388 | furniture | pages [19] -->
m

<!-- b006389 | furniture | pages [19] -->
m

<!-- b006390 | furniture | pages [19] -->
m

<!-- b006391 | furniture | pages [19] -->
m

<!-- b006392 | furniture | pages [19] -->
m

<!-- b006393 | furniture | pages [19] -->
m

<!-- b006394 | furniture | pages [19] -->
m

<!-- b006395 | furniture | pages [19] -->
m

<!-- b006396 | furniture | pages [19] -->
m

<!-- b006397 | furniture | pages [19] -->
m

<!-- b006398 | furniture | pages [19] -->
m

<!-- b006399 | furniture | pages [19] -->
m

<!-- b006400 | furniture | pages [19] -->
m

<!-- b006401 | furniture | pages [19] -->
m

<!-- b006402 | furniture | pages [19] -->
m

<!-- b006403 | furniture | pages [19] -->
m

<!-- b006404 | furniture | pages [19] -->
m

<!-- b006405 | furniture | pages [19] -->
m

<!-- b006406 | furniture | pages [19] -->
m

<!-- b006407 | furniture | pages [19] -->
m

<!-- b006408 | furniture | pages [19] -->
m

<!-- b006409 | furniture | pages [19] -->
m

<!-- b006410 | furniture | pages [19] -->
m

<!-- b006411 | furniture | pages [19] -->
m

<!-- b006412 | furniture | pages [19] -->
m

<!-- b006413 | furniture | pages [19] -->
m

<!-- b006414 | furniture | pages [19] -->
m

<!-- b006415 | furniture | pages [19] -->
m

<!-- b006416 | furniture | pages [19] -->
m

<!-- b006417 | furniture | pages [19] -->
m

<!-- b006418 | furniture | pages [19] -->
m

<!-- b006419 | furniture | pages [19] -->
m

<!-- b006420 | furniture | pages [19] -->
m

<!-- b006421 | furniture | pages [19] -->
m

<!-- b006422 | furniture | pages [19] -->
m

<!-- b006423 | furniture | pages [19] -->
m

<!-- b006424 | furniture | pages [19] -->
m

<!-- b006425 | furniture | pages [19] -->
m

<!-- b006426 | furniture | pages [19] -->
m

<!-- b006427 | furniture | pages [19] -->
m

<!-- b006428 | furniture | pages [19] -->
m

<!-- b006429 | furniture | pages [19] -->
m

<!-- b006430 | furniture | pages [19] -->
m

<!-- b006431 | furniture | pages [19] -->
m

<!-- b006432 | furniture | pages [19] -->
m

<!-- b006433 | furniture | pages [19] -->
m

<!-- b006434 | furniture | pages [19] -->
m

<!-- b006435 | furniture | pages [19] -->
m

<!-- b006436 | furniture | pages [19] -->
m

<!-- b006437 | furniture | pages [19] -->
m

<!-- b006438 | furniture | pages [19] -->
m

<!-- b006439 | furniture | pages [19] -->
m

<!-- b006440 | furniture | pages [19] -->
m

<!-- b006441 | furniture | pages [19] -->
m

<!-- b006442 | furniture | pages [19] -->
m

<!-- b006443 | furniture | pages [19] -->
m

<!-- b006444 | furniture | pages [19] -->
m

<!-- b006445 | furniture | pages [19] -->
m

<!-- b006446 | furniture | pages [19] -->
m

<!-- b006447 | furniture | pages [19] -->
m

<!-- b006448 | furniture | pages [19] -->
m

<!-- b006449 | furniture | pages [19] -->
m

<!-- b006450 | furniture | pages [19] -->
m

<!-- b006451 | furniture | pages [19] -->
m

<!-- b006452 | furniture | pages [19] -->
m

<!-- b006453 | furniture | pages [19] -->
m

<!-- b006454 | furniture | pages [19] -->
m

<!-- b006455 | furniture | pages [19] -->
m

<!-- b006456 | furniture | pages [19] -->
m

<!-- b006457 | furniture | pages [19] -->
m

<!-- b006458 | furniture | pages [19] -->
m

<!-- b006459 | furniture | pages [19] -->
m

<!-- b006460 | furniture | pages [19] -->
m

<!-- b006461 | furniture | pages [19] -->
m

<!-- b006462 | furniture | pages [19] -->
m

<!-- b006463 | furniture | pages [19] -->
m

<!-- b006464 | furniture | pages [19] -->
m

<!-- b006465 | furniture | pages [19] -->
m

<!-- b006466 | furniture | pages [19] -->
m

<!-- b006467 | furniture | pages [19] -->
m

<!-- b006468 | furniture | pages [19] -->
m

<!-- b006469 | furniture | pages [19] -->
m

<!-- b006470 | furniture | pages [19] -->
m

<!-- b006471 | furniture | pages [19] -->
m

<!-- b006472 | furniture | pages [19] -->
m

<!-- b006473 | furniture | pages [19] -->
m

<!-- b006474 | furniture | pages [19] -->
m

<!-- b006475 | furniture | pages [19] -->
m

<!-- b006476 | furniture | pages [19] -->
m

<!-- b006477 | furniture | pages [19] -->
m

<!-- b006478 | furniture | pages [19] -->
m

<!-- b006479 | furniture | pages [19] -->
m

<!-- b006480 | furniture | pages [19] -->
m

<!-- b006481 | furniture | pages [19] -->
m

<!-- b006482 | furniture | pages [19] -->
m

<!-- b006483 | furniture | pages [19] -->
m

<!-- b006484 | furniture | pages [19] -->
m

<!-- b006485 | furniture | pages [19] -->
m

<!-- b006486 | furniture | pages [19] -->
m

<!-- b006487 | furniture | pages [19] -->
m

<!-- b006488 | furniture | pages [19] -->
m

<!-- b006489 | furniture | pages [19] -->
m

<!-- b006490 | furniture | pages [19] -->
m

<!-- b006491 | furniture | pages [19] -->
m

<!-- b006492 | furniture | pages [19] -->
m

<!-- b006493 | furniture | pages [19] -->
m

<!-- b006494 | furniture | pages [19] -->
m

<!-- b006495 | furniture | pages [19] -->
m

<!-- b006496 | furniture | pages [19] -->
m

<!-- b006497 | furniture | pages [19] -->
m

<!-- b006498 | furniture | pages [19] -->
m

<!-- b006499 | furniture | pages [19] -->
m

<!-- b006500 | furniture | pages [19] -->
m

<!-- b006501 | furniture | pages [19] -->
m

<!-- b006502 | furniture | pages [19] -->
m

<!-- b006503 | furniture | pages [19] -->
m

<!-- b006504 | furniture | pages [19] -->
m

<!-- b006505 | furniture | pages [19] -->
m

<!-- b006506 | furniture | pages [19] -->
m

<!-- b006507 | furniture | pages [19] -->
m

<!-- b006508 | furniture | pages [19] -->
m

<!-- b006509 | furniture | pages [19] -->
m

<!-- b006510 | furniture | pages [19] -->
m

<!-- b006511 | furniture | pages [19] -->
m

<!-- b006512 | furniture | pages [19] -->
m

<!-- b006513 | furniture | pages [19] -->
m

<!-- b006514 | furniture | pages [19] -->
m

<!-- b006515 | furniture | pages [19] -->
m

<!-- b006516 | furniture | pages [19] -->
m

<!-- b006517 | furniture | pages [19] -->
m

<!-- b006518 | furniture | pages [19] -->
m

<!-- b006519 | furniture | pages [19] -->
m

<!-- b006520 | furniture | pages [19] -->
m

<!-- b006521 | furniture | pages [19] -->
m

<!-- b006522 | furniture | pages [20] -->
Team # 2503268

<!-- b006523 | furniture | pages [20] -->
Page 18 of 24

<!-- b006524 | caption | pages [20] -->
Figure 10: sensitivity analysis

<!-- b006525 | prose | pages [20] -->
ﬁt. Their moderately high ω suggests potential interactions or context-dependent eﬀects. Conversely, k10 and k1 show minimal eﬀects and nonlinearity.

<!-- b006526 | prose | pages [20] -->
Turning to panel (b), we observe that µ5 emerges with both a large µ↔and a relatively high ω in the evaluation function’s sensitivity plot, indicating a strong direct eﬀect on the score and pronounced variability under diﬀerent conditions. Other variables like ε or µ2 remain clustered near the origin, suggesting they exert less inﬂuence within the current parameter bounds. As in last year’s analysis, we conclude that parameters with high µ↔deserve focused calibration or policy-level prioritization, while those with large ω should be investigated for potential nonlinear or combined eﬀects.

<!-- b006527 | prose | pages [20] -->
Overall, these ﬁndings guide us in prioritizing certain ODE coeﬃcients (e.g., k2, k6) for reﬁned data collection or modeling eﬀorts, while also highlighting which policy parameters (e.g., µ5) most strongly aﬀect the sustainability outcome. The interplay between large µ↔and ω is especially important for anticipating how small changes in one parameter might yield disproportionately large or context- dependent shifts in ﬁnal model results.

<!-- b006528 | prose | pages [20] -->
9.2

<!-- b006529 | heading | pages [20] -->
Quantitative analysis: Local Sensitivity Analysis

<!-- b006530 | prose | pages [20] -->
Beyond the Morris global sensitivity, we have also conducted a local sensitivity analysis to evalu- ate how small perturbations in each parameter pi aﬀect the ﬁnal score ↼Score

<!-- b006531 | prose | pages [20] -->
↼pi . Table 7 shows a condensed version of the partial derivatives for selected top parameters, while Figure 7 provides a bar chart sum- marizing the average absolute sensitivity across multiple µ settings.

<!-- b006532 | prose | pages [20] -->
In general, parameters such as ϱ, r1, and k5 exhibit consistently large partial derivatives with respect to Score, indicating that even small changes can signiﬁcantly alter the sustainability metric. This aligns well with the global Morris analysis, in which these parameters also showed large µ↔values. On the policy side, µ5 retains notable sensitivity, reinforcing the idea that certain intervention intensities or policy measures (µ5) can drastically shift overall outcomes on log scale.

<!-- b006533 | prose | pages [20] -->
关注数学模型

<!-- b006534 | furniture | pages [20] -->
2

<!-- b006535 | furniture | pages [20] -->
MATHmodels

<!-- b006536 | furniture | pages [20] -->
获取更多资讯

<!-- b006537 | furniture | pages [21] -->
Team # 2503268

<!-- b006538 | furniture | pages [21] -->
Page 19 of 24

<!-- b006539 | prose | pages [21] -->
微信公众号：数学模型

<!-- b006540 | caption | pages [21] -->
Figure 11: Top parameters by mean absolute local sensitivity with respect to Score. Error bars repre-

<!-- b006541 | prose | pages [21] -->
sent standard deviation across diﬀerent µ sets.

<!-- b006542 | prose | pages [21] -->
10 Reimagining Big Sur

<!-- b006543 | prose | pages [21] -->
微信号：MATHmodels

<!-- b006544 | prose | pages [21] -->
10.1 Fundamental Information

<!-- b006545 | prose | pages [21] -->
Overtourism is inherently site-speciﬁc [9], as each destination has unique contributing factors. However, various response strategies have been proposed or implemented to address these challenges. Our developed model enhances decision-making for better evaluation outcomes, and we have selected Big Sur, California, to validate its eﬀectiveness.

<!-- b006546 | prose | pages [21] -->
Big Sur, renowned for its rugged coastline, redwood forests, and scenic Highway 1, attracts mil- lions of visitors annually. However, its popularity presents sustainability challenges, exacerbated by natural disasters, road closures, and overtourism pressures. These issues raise critical concerns for both travelers and the tourism industry regarding the long-term accessibility and sustainability of this iconic destination.

<!-- b006547 | prose | pages [21] -->
In our data selection process, we have chosen Pfeiﬀer Big Sur State Park, a renowned tourist desti- nation, as a representative site for the Big Sur Section. To obtain relevant data on tourist numbers and economic growth, we utilized the annually published California State Park System Statistical Report. For visitor attendance, we aggregated the ﬁgures from Paid Day Use, Free Day Use, and Camping categories to represent the annual number of tourists in Pfeiﬀer Big Sur, denoted as NSur. Similarly, for government revenue, we calculated the total annual revenue generated from tourism in Pfeiﬀer Big Sur, denoted as TSur, by summing the income from User Fees, Concessions, and Miscellaneous revenue sources.

<!-- b006548 | prose | pages [21] -->
For the representation of environmental factors, we adopt a methodology inspired by the inno- vative approach of Cheryl J. Hapke and Krystal R. Green [10], who assessed the rates of landsliding and cliﬀretreat along the Big Sur coast by measuring crucial baseline indicators. Similarly, we incor- porate insights from the work of Zuzanna M. Swirad [11], who analyzed spatial and temporal trends

<!-- b006549 | prose | pages [21] -->
m

<!-- b006550 | prose | pages [21] -->
m

<!-- b006551 | prose | pages [21] -->
m

<!-- b006552 | prose | pages [21] -->
m

<!-- b006553 | prose | pages [21] -->
m

<!-- b006554 | prose | pages [21] -->
m

<!-- b006555 | prose | pages [21] -->
m

<!-- b006556 | prose | pages [21] -->
m

<!-- b006557 | prose | pages [21] -->
m

<!-- b006558 | prose | pages [21] -->
m

<!-- b006559 | prose | pages [21] -->
m

<!-- b006560 | prose | pages [21] -->
m

<!-- b006561 | prose | pages [21] -->
m

<!-- b006562 | prose | pages [21] -->
m

<!-- b006563 | prose | pages [21] -->
m

<!-- b006564 | prose | pages [21] -->
m

<!-- b006565 | prose | pages [21] -->
m

<!-- b006566 | prose | pages [21] -->
m

<!-- b006567 | prose | pages [21] -->
m

<!-- b006568 | prose | pages [21] -->
m

<!-- b006569 | prose | pages [21] -->
m

<!-- b006570 | prose | pages [21] -->
m

<!-- b006571 | prose | pages [21] -->
m

<!-- b006572 | prose | pages [21] -->
m

<!-- b006573 | prose | pages [21] -->
m

<!-- b006574 | prose | pages [21] -->
m

<!-- b006575 | prose | pages [21] -->
m

<!-- b006576 | prose | pages [21] -->
m

<!-- b006577 | prose | pages [21] -->
m

<!-- b006578 | prose | pages [21] -->
m

<!-- b006579 | prose | pages [21] -->
m

<!-- b006580 | prose | pages [21] -->
m

<!-- b006581 | prose | pages [21] -->
m

<!-- b006582 | prose | pages [21] -->
m

<!-- b006583 | prose | pages [21] -->
m

<!-- b006584 | prose | pages [21] -->
m

<!-- b006585 | prose | pages [21] -->
m

<!-- b006586 | prose | pages [21] -->
m

<!-- b006587 | prose | pages [21] -->
m

<!-- b006588 | prose | pages [21] -->
m

<!-- b006589 | prose | pages [21] -->
m

<!-- b006590 | prose | pages [21] -->
m

<!-- b006591 | prose | pages [21] -->
m

<!-- b006592 | prose | pages [21] -->
m

<!-- b006593 | prose | pages [21] -->
m

<!-- b006594 | prose | pages [21] -->
m

<!-- b006595 | prose | pages [21] -->
m

<!-- b006596 | prose | pages [21] -->
m

<!-- b006597 | prose | pages [21] -->
m

<!-- b006598 | prose | pages [21] -->
m

<!-- b006599 | prose | pages [21] -->
m

<!-- b006600 | prose | pages [21] -->
m

<!-- b006601 | prose | pages [21] -->
m

<!-- b006602 | prose | pages [21] -->
m

<!-- b006603 | prose | pages [21] -->
m

<!-- b006604 | prose | pages [21] -->
m

<!-- b006605 | prose | pages [21] -->
m

<!-- b006606 | prose | pages [21] -->
m

<!-- b006607 | prose | pages [21] -->
m

<!-- b006608 | prose | pages [21] -->
m

<!-- b006609 | prose | pages [21] -->
m

<!-- b006610 | prose | pages [21] -->
m

<!-- b006611 | prose | pages [21] -->
m

<!-- b006612 | prose | pages [21] -->
m

<!-- b006613 | prose | pages [21] -->
m

<!-- b006614 | prose | pages [21] -->
m

<!-- b006615 | prose | pages [21] -->
m

<!-- b006616 | prose | pages [21] -->
m

<!-- b006617 | prose | pages [21] -->
m

<!-- b006618 | prose | pages [21] -->
m

<!-- b006619 | prose | pages [21] -->
m

<!-- b006620 | prose | pages [21] -->
m

<!-- b006621 | prose | pages [21] -->
m

<!-- b006622 | prose | pages [21] -->
m

<!-- b006623 | prose | pages [21] -->
m

<!-- b006624 | prose | pages [21] -->
m

<!-- b006625 | prose | pages [21] -->
m

<!-- b006626 | prose | pages [21] -->
m

<!-- b006627 | prose | pages [21] -->
m

<!-- b006628 | prose | pages [21] -->
m

<!-- b006629 | prose | pages [21] -->
m

<!-- b006630 | prose | pages [21] -->
m

<!-- b006631 | prose | pages [21] -->
m

<!-- b006632 | prose | pages [21] -->
m

<!-- b006633 | prose | pages [21] -->
m

<!-- b006634 | prose | pages [21] -->
m

<!-- b006635 | prose | pages [21] -->
m

<!-- b006636 | prose | pages [21] -->
m

<!-- b006637 | prose | pages [21] -->
m

<!-- b006638 | prose | pages [21] -->
m

<!-- b006639 | prose | pages [21] -->
m

<!-- b006640 | prose | pages [21] -->
m

<!-- b006641 | prose | pages [21] -->
m

<!-- b006642 | prose | pages [21] -->
m

<!-- b006643 | prose | pages [21] -->
m

<!-- b006644 | prose | pages [21] -->
m

<!-- b006645 | prose | pages [21] -->
m

<!-- b006646 | prose | pages [21] -->
m

<!-- b006647 | prose | pages [21] -->
m

<!-- b006648 | prose | pages [21] -->
m

<!-- b006649 | prose | pages [21] -->
m

<!-- b006650 | prose | pages [21] -->
m

<!-- b006651 | prose | pages [21] -->
m

<!-- b006652 | prose | pages [21] -->
m

<!-- b006653 | prose | pages [21] -->
m

<!-- b006654 | prose | pages [21] -->
m

<!-- b006655 | prose | pages [21] -->
m

<!-- b006656 | prose | pages [21] -->
m

<!-- b006657 | prose | pages [21] -->
m

<!-- b006658 | prose | pages [21] -->
m

<!-- b006659 | prose | pages [21] -->
m

<!-- b006660 | prose | pages [21] -->
m

<!-- b006661 | prose | pages [21] -->
m

<!-- b006662 | prose | pages [21] -->
m

<!-- b006663 | prose | pages [21] -->
m

<!-- b006664 | prose | pages [21] -->
m

<!-- b006665 | prose | pages [21] -->
m

<!-- b006666 | prose | pages [21] -->
m

<!-- b006667 | prose | pages [21] -->
m

<!-- b006668 | prose | pages [21] -->
m

<!-- b006669 | prose | pages [21] -->
m

<!-- b006670 | prose | pages [21] -->
m

<!-- b006671 | prose | pages [21] -->
m

<!-- b006672 | prose | pages [21] -->
m

<!-- b006673 | prose | pages [21] -->
m

<!-- b006674 | prose | pages [21] -->
m

<!-- b006675 | prose | pages [21] -->
m

<!-- b006676 | prose | pages [21] -->
m

<!-- b006677 | prose | pages [21] -->
m

<!-- b006678 | prose | pages [21] -->
m

<!-- b006679 | prose | pages [21] -->
m

<!-- b006680 | prose | pages [21] -->
m

<!-- b006681 | prose | pages [21] -->
m

<!-- b006682 | prose | pages [21] -->
m

<!-- b006683 | prose | pages [21] -->
m

<!-- b006684 | prose | pages [21] -->
m

<!-- b006685 | prose | pages [21] -->
m

<!-- b006686 | prose | pages [21] -->
m

<!-- b006687 | prose | pages [21] -->
m

<!-- b006688 | prose | pages [21] -->
m

<!-- b006689 | prose | pages [21] -->
m

<!-- b006690 | prose | pages [21] -->
m

<!-- b006691 | prose | pages [21] -->
m

<!-- b006692 | prose | pages [21] -->
m

<!-- b006693 | prose | pages [21] -->
m

<!-- b006694 | prose | pages [21] -->
m

<!-- b006695 | prose | pages [21] -->
m

<!-- b006696 | prose | pages [21] -->
m

<!-- b006697 | prose | pages [21] -->
m

<!-- b006698 | prose | pages [21] -->
m

<!-- b006699 | prose | pages [21] -->
m

<!-- b006700 | prose | pages [21] -->
m

<!-- b006701 | prose | pages [21] -->
m

<!-- b006702 | prose | pages [21] -->
m

<!-- b006703 | prose | pages [21] -->
m

<!-- b006704 | prose | pages [21] -->
m

<!-- b006705 | prose | pages [21] -->
m

<!-- b006706 | prose | pages [21] -->
m

<!-- b006707 | prose | pages [21] -->
m

<!-- b006708 | prose | pages [21] -->
m

<!-- b006709 | prose | pages [21] -->
m

<!-- b006710 | prose | pages [21] -->
m

<!-- b006711 | prose | pages [21] -->
m

<!-- b006712 | prose | pages [21] -->
m

<!-- b006713 | prose | pages [21] -->
m

<!-- b006714 | prose | pages [21] -->
m

<!-- b006715 | prose | pages [21] -->
m

<!-- b006716 | prose | pages [21] -->
m

<!-- b006717 | prose | pages [21] -->
m

<!-- b006718 | prose | pages [21] -->
m

<!-- b006719 | prose | pages [21] -->
m

<!-- b006720 | prose | pages [21] -->
m

<!-- b006721 | prose | pages [21] -->
m

<!-- b006722 | prose | pages [21] -->
m

<!-- b006723 | prose | pages [21] -->
m

<!-- b006724 | prose | pages [21] -->
m

<!-- b006725 | prose | pages [21] -->
m

<!-- b006726 | prose | pages [21] -->
m

<!-- b006727 | prose | pages [21] -->
m

<!-- b006728 | prose | pages [21] -->
m

<!-- b006729 | prose | pages [21] -->
m

<!-- b006730 | prose | pages [21] -->
m

<!-- b006731 | prose | pages [21] -->
m

<!-- b006732 | prose | pages [21] -->
m

<!-- b006733 | prose | pages [21] -->
m

<!-- b006734 | prose | pages [21] -->
m

<!-- b006735 | prose | pages [21] -->
m

<!-- b006736 | prose | pages [21] -->
m

<!-- b006737 | prose | pages [21] -->
m

<!-- b006738 | prose | pages [21] -->
m

<!-- b006739 | prose | pages [21] -->
m

<!-- b006740 | prose | pages [21] -->
m

<!-- b006741 | prose | pages [21] -->
m

<!-- b006742 | prose | pages [21] -->
m

<!-- b006743 | prose | pages [21] -->
m

<!-- b006744 | prose | pages [21] -->
m

<!-- b006745 | prose | pages [21] -->
m

<!-- b006746 | prose | pages [21] -->
m

<!-- b006747 | prose | pages [21] -->
m

<!-- b006748 | prose | pages [21] -->
m

<!-- b006749 | prose | pages [21] -->
m

<!-- b006750 | prose | pages [21] -->
m

<!-- b006751 | prose | pages [21] -->
m

<!-- b006752 | prose | pages [21] -->
m

<!-- b006753 | prose | pages [21] -->
m

<!-- b006754 | prose | pages [21] -->
m

<!-- b006755 | prose | pages [21] -->
m

<!-- b006756 | prose | pages [21] -->
m

<!-- b006757 | prose | pages [21] -->
m

<!-- b006758 | prose | pages [21] -->
m

<!-- b006759 | prose | pages [21] -->
m

<!-- b006760 | prose | pages [21] -->
m

<!-- b006761 | prose | pages [21] -->
m

<!-- b006762 | prose | pages [21] -->
m

<!-- b006763 | prose | pages [21] -->
m

<!-- b006764 | prose | pages [21] -->
m

<!-- b006765 | prose | pages [21] -->
m

<!-- b006766 | prose | pages [21] -->
m

<!-- b006767 | prose | pages [21] -->
m

<!-- b006768 | prose | pages [21] -->
m

<!-- b006769 | prose | pages [21] -->
m

<!-- b006770 | prose | pages [21] -->
m

<!-- b006771 | prose | pages [21] -->
m

<!-- b006772 | prose | pages [21] -->
m

<!-- b006773 | prose | pages [21] -->
m

<!-- b006774 | prose | pages [21] -->
m

<!-- b006775 | prose | pages [21] -->
m

<!-- b006776 | prose | pages [21] -->
m

<!-- b006777 | prose | pages [21] -->
m

<!-- b006778 | prose | pages [21] -->
m

<!-- b006779 | prose | pages [21] -->
m

<!-- b006780 | prose | pages [21] -->
m

<!-- b006781 | prose | pages [21] -->
m

<!-- b006782 | prose | pages [21] -->
m

<!-- b006783 | prose | pages [21] -->
m

<!-- b006784 | prose | pages [21] -->
m

<!-- b006785 | prose | pages [21] -->
m

<!-- b006786 | prose | pages [21] -->
m

<!-- b006787 | prose | pages [21] -->
m

<!-- b006788 | prose | pages [21] -->
m

<!-- b006789 | prose | pages [21] -->
m

<!-- b006790 | prose | pages [21] -->
m

<!-- b006791 | prose | pages [21] -->
m

<!-- b006792 | prose | pages [21] -->
m

<!-- b006793 | prose | pages [21] -->
m

<!-- b006794 | prose | pages [21] -->
m

<!-- b006795 | prose | pages [21] -->
m

<!-- b006796 | prose | pages [21] -->
m

<!-- b006797 | prose | pages [21] -->
m

<!-- b006798 | prose | pages [21] -->
m

<!-- b006799 | prose | pages [21] -->
m

<!-- b006800 | prose | pages [21] -->
m

<!-- b006801 | prose | pages [21] -->
m

<!-- b006802 | prose | pages [21] -->
m

<!-- b006803 | prose | pages [21] -->
m

<!-- b006804 | prose | pages [21] -->
m

<!-- b006805 | prose | pages [21] -->
m

<!-- b006806 | prose | pages [21] -->
m

<!-- b006807 | prose | pages [21] -->
m

<!-- b006808 | prose | pages [21] -->
m

<!-- b006809 | prose | pages [21] -->
m

<!-- b006810 | prose | pages [21] -->
m

<!-- b006811 | prose | pages [21] -->
m

<!-- b006812 | prose | pages [21] -->
m

<!-- b006813 | prose | pages [21] -->
m

<!-- b006814 | prose | pages [21] -->
m

<!-- b006815 | prose | pages [21] -->
m

<!-- b006816 | prose | pages [21] -->
m

<!-- b006817 | prose | pages [21] -->
m

<!-- b006818 | prose | pages [21] -->
m

<!-- b006819 | prose | pages [21] -->
m

<!-- b006820 | prose | pages [21] -->
m

<!-- b006821 | prose | pages [21] -->
m

<!-- b006822 | prose | pages [21] -->
m

<!-- b006823 | prose | pages [21] -->
m

<!-- b006824 | prose | pages [21] -->
m

<!-- b006825 | prose | pages [21] -->
m

<!-- b006826 | prose | pages [21] -->
m

<!-- b006827 | prose | pages [21] -->
m

<!-- b006828 | prose | pages [21] -->
m

<!-- b006829 | prose | pages [21] -->
m

<!-- b006830 | prose | pages [21] -->
m

<!-- b006831 | prose | pages [21] -->
m

<!-- b006832 | prose | pages [21] -->
m

<!-- b006833 | furniture | pages [21] -->
m

<!-- b006834 | furniture | pages [21] -->
m

<!-- b006835 | furniture | pages [21] -->
m

<!-- b006836 | furniture | pages [21] -->
m

<!-- b006837 | furniture | pages [21] -->
m

<!-- b006838 | furniture | pages [21] -->
m

<!-- b006839 | furniture | pages [21] -->
m

<!-- b006840 | furniture | pages [21] -->
m

<!-- b006841 | furniture | pages [21] -->
m

<!-- b006842 | furniture | pages [21] -->
m

<!-- b006843 | furniture | pages [21] -->
m

<!-- b006844 | furniture | pages [21] -->
m

<!-- b006845 | furniture | pages [21] -->
m

<!-- b006846 | furniture | pages [21] -->
m

<!-- b006847 | furniture | pages [21] -->
m

<!-- b006848 | furniture | pages [21] -->
m

<!-- b006849 | furniture | pages [21] -->
m

<!-- b006850 | furniture | pages [21] -->
m

<!-- b006851 | furniture | pages [21] -->
m

<!-- b006852 | furniture | pages [21] -->
m

<!-- b006853 | furniture | pages [21] -->
m

<!-- b006854 | furniture | pages [21] -->
m

<!-- b006855 | furniture | pages [21] -->
m

<!-- b006856 | furniture | pages [21] -->
m

<!-- b006857 | furniture | pages [21] -->
m

<!-- b006858 | furniture | pages [21] -->
m

<!-- b006859 | furniture | pages [21] -->
m

<!-- b006860 | furniture | pages [21] -->
m

<!-- b006861 | furniture | pages [21] -->
m

<!-- b006862 | furniture | pages [21] -->
m

<!-- b006863 | furniture | pages [21] -->
m

<!-- b006864 | furniture | pages [21] -->
m

<!-- b006865 | furniture | pages [21] -->
m

<!-- b006866 | furniture | pages [21] -->
m

<!-- b006867 | furniture | pages [21] -->
m

<!-- b006868 | furniture | pages [21] -->
m

<!-- b006869 | furniture | pages [21] -->
m

<!-- b006870 | furniture | pages [21] -->
m

<!-- b006871 | furniture | pages [21] -->
m

<!-- b006872 | furniture | pages [21] -->
m

<!-- b006873 | furniture | pages [21] -->
m

<!-- b006874 | furniture | pages [21] -->
m

<!-- b006875 | furniture | pages [21] -->
m

<!-- b006876 | furniture | pages [21] -->
m

<!-- b006877 | furniture | pages [21] -->
m

<!-- b006878 | furniture | pages [21] -->
m

<!-- b006879 | furniture | pages [21] -->
m

<!-- b006880 | furniture | pages [21] -->
m

<!-- b006881 | furniture | pages [21] -->
m

<!-- b006882 | furniture | pages [21] -->
m

<!-- b006883 | furniture | pages [21] -->
m

<!-- b006884 | furniture | pages [21] -->
m

<!-- b006885 | furniture | pages [21] -->
m

<!-- b006886 | furniture | pages [21] -->
m

<!-- b006887 | furniture | pages [21] -->
m

<!-- b006888 | furniture | pages [21] -->
m

<!-- b006889 | furniture | pages [21] -->
m

<!-- b006890 | furniture | pages [21] -->
m

<!-- b006891 | furniture | pages [21] -->
m

<!-- b006892 | furniture | pages [21] -->
m

<!-- b006893 | furniture | pages [21] -->
m

<!-- b006894 | furniture | pages [21] -->
m

<!-- b006895 | furniture | pages [21] -->
m

<!-- b006896 | furniture | pages [21] -->
m

<!-- b006897 | furniture | pages [21] -->
m

<!-- b006898 | furniture | pages [21] -->
m

<!-- b006899 | furniture | pages [21] -->
m

<!-- b006900 | furniture | pages [21] -->
m

<!-- b006901 | furniture | pages [21] -->
m

<!-- b006902 | furniture | pages [21] -->
m

<!-- b006903 | furniture | pages [21] -->
m

<!-- b006904 | furniture | pages [21] -->
m

<!-- b006905 | furniture | pages [21] -->
m

<!-- b006906 | furniture | pages [21] -->
m

<!-- b006907 | furniture | pages [21] -->
m

<!-- b006908 | furniture | pages [21] -->
m

<!-- b006909 | furniture | pages [21] -->
m

<!-- b006910 | furniture | pages [21] -->
m

<!-- b006911 | furniture | pages [21] -->
m

<!-- b006912 | furniture | pages [21] -->
m

<!-- b006913 | furniture | pages [21] -->
m

<!-- b006914 | furniture | pages [21] -->
m

<!-- b006915 | furniture | pages [21] -->
m

<!-- b006916 | furniture | pages [21] -->
m

<!-- b006917 | furniture | pages [21] -->
m

<!-- b006918 | furniture | pages [21] -->
m

<!-- b006919 | furniture | pages [21] -->
m

<!-- b006920 | furniture | pages [21] -->
m

<!-- b006921 | furniture | pages [21] -->
m

<!-- b006922 | furniture | pages [21] -->
m

<!-- b006923 | furniture | pages [21] -->
m

<!-- b006924 | furniture | pages [21] -->
m

<!-- b006925 | furniture | pages [21] -->
m

<!-- b006926 | furniture | pages [21] -->
m

<!-- b006927 | furniture | pages [21] -->
m

<!-- b006928 | furniture | pages [21] -->
m

<!-- b006929 | furniture | pages [21] -->
m

<!-- b006930 | furniture | pages [21] -->
m

<!-- b006931 | furniture | pages [21] -->
m

<!-- b006932 | furniture | pages [21] -->
m

<!-- b006933 | furniture | pages [21] -->
m

<!-- b006934 | furniture | pages [21] -->
m

<!-- b006935 | furniture | pages [21] -->
m

<!-- b006936 | furniture | pages [21] -->
m

<!-- b006937 | furniture | pages [21] -->
m

<!-- b006938 | furniture | pages [21] -->
m

<!-- b006939 | furniture | pages [21] -->
m

<!-- b006940 | furniture | pages [21] -->
m

<!-- b006941 | furniture | pages [21] -->
m

<!-- b006942 | furniture | pages [21] -->
m

<!-- b006943 | furniture | pages [21] -->
m

<!-- b006944 | furniture | pages [21] -->
m

<!-- b006945 | furniture | pages [21] -->
m

<!-- b006946 | furniture | pages [21] -->
m

<!-- b006947 | furniture | pages [21] -->
m

<!-- b006948 | furniture | pages [21] -->
m

<!-- b006949 | furniture | pages [21] -->
m

<!-- b006950 | furniture | pages [21] -->
m

<!-- b006951 | furniture | pages [21] -->
m

<!-- b006952 | furniture | pages [21] -->
m

<!-- b006953 | furniture | pages [21] -->
m

<!-- b006954 | furniture | pages [21] -->
m

<!-- b006955 | furniture | pages [21] -->
m

<!-- b006956 | furniture | pages [21] -->
m

<!-- b006957 | furniture | pages [21] -->
m

<!-- b006958 | furniture | pages [21] -->
m

<!-- b006959 | furniture | pages [21] -->
m

<!-- b006960 | furniture | pages [21] -->
m

<!-- b006961 | furniture | pages [21] -->
m

<!-- b006962 | furniture | pages [21] -->
m

<!-- b006963 | furniture | pages [21] -->
m

<!-- b006964 | furniture | pages [21] -->
m

<!-- b006965 | furniture | pages [21] -->
m

<!-- b006966 | furniture | pages [21] -->
m

<!-- b006967 | furniture | pages [21] -->
m

<!-- b006968 | furniture | pages [21] -->
m

<!-- b006969 | furniture | pages [21] -->
m

<!-- b006970 | furniture | pages [21] -->
m

<!-- b006971 | furniture | pages [21] -->
m

<!-- b006972 | furniture | pages [21] -->
m

<!-- b006973 | furniture | pages [21] -->
m

<!-- b006974 | furniture | pages [21] -->
m

<!-- b006975 | furniture | pages [21] -->
m

<!-- b006976 | furniture | pages [21] -->
m

<!-- b006977 | furniture | pages [21] -->
m

<!-- b006978 | furniture | pages [21] -->
m

<!-- b006979 | furniture | pages [21] -->
m

<!-- b006980 | furniture | pages [21] -->
m

<!-- b006981 | furniture | pages [21] -->
m

<!-- b006982 | furniture | pages [21] -->
m

<!-- b006983 | furniture | pages [21] -->
m

<!-- b006984 | furniture | pages [21] -->
m

<!-- b006985 | furniture | pages [21] -->
m

<!-- b006986 | furniture | pages [21] -->
m

<!-- b006987 | furniture | pages [21] -->
m

<!-- b006988 | furniture | pages [21] -->
m

<!-- b006989 | furniture | pages [21] -->
m

<!-- b006990 | furniture | pages [21] -->
m

<!-- b006991 | furniture | pages [21] -->
m

<!-- b006992 | furniture | pages [21] -->
m

<!-- b006993 | furniture | pages [21] -->
m

<!-- b006994 | furniture | pages [21] -->
m

<!-- b006995 | furniture | pages [21] -->
m

<!-- b006996 | furniture | pages [21] -->
m

<!-- b006997 | furniture | pages [21] -->
m

<!-- b006998 | furniture | pages [21] -->
m

<!-- b006999 | furniture | pages [21] -->
m

<!-- b007000 | furniture | pages [21] -->
m

<!-- b007001 | furniture | pages [21] -->
m

<!-- b007002 | furniture | pages [21] -->
m

<!-- b007003 | furniture | pages [21] -->
m

<!-- b007004 | furniture | pages [21] -->
m

<!-- b007005 | furniture | pages [21] -->
m

<!-- b007006 | furniture | pages [21] -->
m

<!-- b007007 | furniture | pages [21] -->
m

<!-- b007008 | furniture | pages [21] -->
m

<!-- b007009 | furniture | pages [21] -->
m

<!-- b007010 | furniture | pages [21] -->
m

<!-- b007011 | furniture | pages [21] -->
m

<!-- b007012 | furniture | pages [21] -->
m

<!-- b007013 | furniture | pages [21] -->
m

<!-- b007014 | furniture | pages [21] -->
m

<!-- b007015 | furniture | pages [21] -->
m

<!-- b007016 | furniture | pages [21] -->
m

<!-- b007017 | furniture | pages [21] -->
m

<!-- b007018 | furniture | pages [21] -->
m

<!-- b007019 | furniture | pages [21] -->
m

<!-- b007020 | furniture | pages [21] -->
m

<!-- b007021 | furniture | pages [21] -->
m

<!-- b007022 | furniture | pages [21] -->
m

<!-- b007023 | furniture | pages [21] -->
m

<!-- b007024 | furniture | pages [21] -->
m

<!-- b007025 | furniture | pages [21] -->
m

<!-- b007026 | furniture | pages [21] -->
m

<!-- b007027 | furniture | pages [21] -->
m

<!-- b007028 | furniture | pages [21] -->
m

<!-- b007029 | furniture | pages [21] -->
m

<!-- b007030 | furniture | pages [21] -->
m

<!-- b007031 | furniture | pages [21] -->
m

<!-- b007032 | furniture | pages [21] -->
m

<!-- b007033 | furniture | pages [21] -->
m

<!-- b007034 | furniture | pages [21] -->
m

<!-- b007035 | furniture | pages [21] -->
m

<!-- b007036 | furniture | pages [21] -->
m

<!-- b007037 | furniture | pages [21] -->
m

<!-- b007038 | furniture | pages [21] -->
m

<!-- b007039 | furniture | pages [21] -->
m

<!-- b007040 | furniture | pages [21] -->
m

<!-- b007041 | furniture | pages [21] -->
m

<!-- b007042 | furniture | pages [21] -->
m

<!-- b007043 | furniture | pages [21] -->
m

<!-- b007044 | furniture | pages [21] -->
m

<!-- b007045 | furniture | pages [21] -->
m

<!-- b007046 | furniture | pages [21] -->
m

<!-- b007047 | furniture | pages [21] -->
m

<!-- b007048 | furniture | pages [21] -->
m

<!-- b007049 | furniture | pages [21] -->
m

<!-- b007050 | furniture | pages [21] -->
m

<!-- b007051 | furniture | pages [21] -->
m

<!-- b007052 | furniture | pages [21] -->
m

<!-- b007053 | furniture | pages [21] -->
m

<!-- b007054 | furniture | pages [21] -->
m

<!-- b007055 | furniture | pages [21] -->
m

<!-- b007056 | furniture | pages [21] -->
m

<!-- b007057 | furniture | pages [21] -->
m

<!-- b007058 | furniture | pages [21] -->
m

<!-- b007059 | furniture | pages [21] -->
m

<!-- b007060 | furniture | pages [21] -->
m

<!-- b007061 | furniture | pages [21] -->
m

<!-- b007062 | furniture | pages [21] -->
m

<!-- b007063 | furniture | pages [21] -->
m

<!-- b007064 | furniture | pages [21] -->
m

<!-- b007065 | furniture | pages [21] -->
m

<!-- b007066 | furniture | pages [21] -->
m

<!-- b007067 | furniture | pages [21] -->
m

<!-- b007068 | furniture | pages [21] -->
m

<!-- b007069 | furniture | pages [21] -->
m

<!-- b007070 | furniture | pages [21] -->
m

<!-- b007071 | furniture | pages [21] -->
m

<!-- b007072 | furniture | pages [21] -->
m

<!-- b007073 | furniture | pages [21] -->
m

<!-- b007074 | furniture | pages [21] -->
m

<!-- b007075 | furniture | pages [21] -->
m

<!-- b007076 | furniture | pages [21] -->
m

<!-- b007077 | furniture | pages [21] -->
m

<!-- b007078 | furniture | pages [21] -->
m

<!-- b007079 | furniture | pages [21] -->
m

<!-- b007080 | furniture | pages [21] -->
m

<!-- b007081 | furniture | pages [21] -->
m

<!-- b007082 | furniture | pages [21] -->
m

<!-- b007083 | furniture | pages [21] -->
m

<!-- b007084 | furniture | pages [21] -->
m

<!-- b007085 | furniture | pages [21] -->
m

<!-- b007086 | furniture | pages [21] -->
m

<!-- b007087 | furniture | pages [21] -->
m

<!-- b007088 | furniture | pages [21] -->
m

<!-- b007089 | furniture | pages [21] -->
m

<!-- b007090 | furniture | pages [21] -->
m

<!-- b007091 | furniture | pages [21] -->
m

<!-- b007092 | furniture | pages [21] -->
m

<!-- b007093 | furniture | pages [21] -->
m

<!-- b007094 | furniture | pages [21] -->
m

<!-- b007095 | furniture | pages [21] -->
m

<!-- b007096 | furniture | pages [21] -->
m

<!-- b007097 | furniture | pages [21] -->
m

<!-- b007098 | furniture | pages [21] -->
m

<!-- b007099 | furniture | pages [21] -->
m

<!-- b007100 | furniture | pages [21] -->
m

<!-- b007101 | furniture | pages [21] -->
m

<!-- b007102 | furniture | pages [21] -->
m

<!-- b007103 | furniture | pages [21] -->
m

<!-- b007104 | furniture | pages [21] -->
m

<!-- b007105 | furniture | pages [21] -->
m

<!-- b007106 | furniture | pages [21] -->
m

<!-- b007107 | furniture | pages [21] -->
m

<!-- b007108 | furniture | pages [21] -->
m

<!-- b007109 | furniture | pages [21] -->
m

<!-- b007110 | furniture | pages [21] -->
m

<!-- b007111 | furniture | pages [21] -->
m

<!-- b007112 | furniture | pages [21] -->
m

<!-- b007113 | furniture | pages [21] -->
m

<!-- b007114 | furniture | pages [21] -->
m

<!-- b007115 | furniture | pages [21] -->
m

<!-- b007116 | furniture | pages [21] -->
m

<!-- b007117 | furniture | pages [21] -->
m

<!-- b007118 | furniture | pages [21] -->
m

<!-- b007119 | furniture | pages [21] -->
m

<!-- b007120 | furniture | pages [21] -->
m

<!-- b007121 | furniture | pages [21] -->
m

<!-- b007122 | furniture | pages [21] -->
m

<!-- b007123 | furniture | pages [21] -->
m

<!-- b007124 | furniture | pages [21] -->
m

<!-- b007125 | furniture | pages [21] -->
m

<!-- b007126 | furniture | pages [21] -->
m

<!-- b007127 | furniture | pages [21] -->
m

<!-- b007128 | furniture | pages [21] -->
m

<!-- b007129 | furniture | pages [21] -->
m

<!-- b007130 | furniture | pages [21] -->
m

<!-- b007131 | furniture | pages [21] -->
m

<!-- b007132 | furniture | pages [21] -->
m

<!-- b007133 | furniture | pages [21] -->
m

<!-- b007134 | furniture | pages [21] -->
m

<!-- b007135 | furniture | pages [21] -->
m

<!-- b007136 | furniture | pages [21] -->
m

<!-- b007137 | furniture | pages [21] -->
m

<!-- b007138 | furniture | pages [21] -->
m

<!-- b007139 | furniture | pages [21] -->
m

<!-- b007140 | furniture | pages [21] -->
m

<!-- b007141 | furniture | pages [21] -->
m

<!-- b007142 | furniture | pages [21] -->
m

<!-- b007143 | furniture | pages [21] -->
m

<!-- b007144 | furniture | pages [21] -->
m

<!-- b007145 | furniture | pages [21] -->
m

<!-- b007146 | furniture | pages [21] -->
m

<!-- b007147 | furniture | pages [21] -->
m

<!-- b007148 | furniture | pages [21] -->
m

<!-- b007149 | furniture | pages [21] -->
m

<!-- b007150 | furniture | pages [21] -->
m

<!-- b007151 | furniture | pages [21] -->
m

<!-- b007152 | furniture | pages [21] -->
m

<!-- b007153 | furniture | pages [21] -->
m

<!-- b007154 | furniture | pages [21] -->
m

<!-- b007155 | furniture | pages [21] -->
m

<!-- b007156 | furniture | pages [21] -->
m

<!-- b007157 | furniture | pages [21] -->
m

<!-- b007158 | furniture | pages [21] -->
m

<!-- b007159 | furniture | pages [21] -->
m

<!-- b007160 | furniture | pages [21] -->
m

<!-- b007161 | furniture | pages [21] -->
m

<!-- b007162 | furniture | pages [21] -->
m

<!-- b007163 | furniture | pages [21] -->
m

<!-- b007164 | furniture | pages [21] -->
m

<!-- b007165 | furniture | pages [21] -->
m

<!-- b007166 | furniture | pages [21] -->
m

<!-- b007167 | furniture | pages [21] -->
m

<!-- b007168 | furniture | pages [21] -->
m

<!-- b007169 | furniture | pages [21] -->
m

<!-- b007170 | furniture | pages [21] -->
m

<!-- b007171 | furniture | pages [21] -->
m

<!-- b007172 | furniture | pages [21] -->
m

<!-- b007173 | furniture | pages [21] -->
m

<!-- b007174 | furniture | pages [21] -->
m

<!-- b007175 | furniture | pages [21] -->
m

<!-- b007176 | furniture | pages [21] -->
m

<!-- b007177 | furniture | pages [21] -->
m

<!-- b007178 | furniture | pages [21] -->
m

<!-- b007179 | furniture | pages [21] -->
m

<!-- b007180 | furniture | pages [21] -->
m

<!-- b007181 | furniture | pages [21] -->
m

<!-- b007182 | furniture | pages [21] -->
m

<!-- b007183 | furniture | pages [21] -->
m

<!-- b007184 | furniture | pages [21] -->
m

<!-- b007185 | furniture | pages [21] -->
m

<!-- b007186 | furniture | pages [21] -->
m

<!-- b007187 | furniture | pages [21] -->
m

<!-- b007188 | furniture | pages [21] -->
m

<!-- b007189 | furniture | pages [21] -->
m

<!-- b007190 | furniture | pages [21] -->
m

<!-- b007191 | furniture | pages [21] -->
m

<!-- b007192 | furniture | pages [21] -->
m

<!-- b007193 | furniture | pages [21] -->
m

<!-- b007194 | furniture | pages [21] -->
m

<!-- b007195 | furniture | pages [21] -->
m

<!-- b007196 | furniture | pages [21] -->
m

<!-- b007197 | furniture | pages [21] -->
m

<!-- b007198 | furniture | pages [21] -->
m

<!-- b007199 | furniture | pages [21] -->
m

<!-- b007200 | furniture | pages [21] -->
m

<!-- b007201 | furniture | pages [21] -->
m

<!-- b007202 | furniture | pages [21] -->
m

<!-- b007203 | furniture | pages [21] -->
m

<!-- b007204 | furniture | pages [21] -->
m

<!-- b007205 | furniture | pages [21] -->
m

<!-- b007206 | furniture | pages [21] -->
m

<!-- b007207 | furniture | pages [21] -->
m

<!-- b007208 | furniture | pages [21] -->
m

<!-- b007209 | furniture | pages [21] -->
m

<!-- b007210 | furniture | pages [21] -->
m

<!-- b007211 | furniture | pages [21] -->
m

<!-- b007212 | furniture | pages [21] -->
m

<!-- b007213 | furniture | pages [21] -->
m

<!-- b007214 | furniture | pages [21] -->
m

<!-- b007215 | furniture | pages [21] -->
m

<!-- b007216 | furniture | pages [21] -->
m

<!-- b007217 | furniture | pages [21] -->
m

<!-- b007218 | furniture | pages [21] -->
m

<!-- b007219 | furniture | pages [21] -->
m

<!-- b007220 | furniture | pages [21] -->
m

<!-- b007221 | furniture | pages [21] -->
m

<!-- b007222 | furniture | pages [21] -->
m

<!-- b007223 | furniture | pages [21] -->
m

<!-- b007224 | furniture | pages [21] -->
m

<!-- b007225 | furniture | pages [21] -->
m

<!-- b007226 | furniture | pages [21] -->
m

<!-- b007227 | furniture | pages [21] -->
m

<!-- b007228 | furniture | pages [21] -->
m

<!-- b007229 | furniture | pages [21] -->
m

<!-- b007230 | furniture | pages [21] -->
m

<!-- b007231 | furniture | pages [21] -->
m

<!-- b007232 | furniture | pages [21] -->
m

<!-- b007233 | furniture | pages [21] -->
m

<!-- b007234 | furniture | pages [21] -->
m

<!-- b007235 | furniture | pages [21] -->
m

<!-- b007236 | furniture | pages [25] -->
Team # 2503268

<!-- b007237 | furniture | pages [25] -->
Page 23 of 24

<!-- b007238 | heading | pages [25] -->
References

<!-- b007239 | references | pages [25] -->
[1] Braithwaite, R. J. "Glacier Equilibrium-Line Altitude: An Indicator of Climate Change." Journal

<!-- b007240 | references | pages [25] -->
of Glaciology, 1984.

<!-- b007241 | references | pages [25] -->
[2] Oerlemans, J. "Glaciers and Climate Change." International Geophysics, 2001.

<!-- b007242 | references | pages [25] -->
微信公众号：数学模型

<!-- b007243 | references | pages [25] -->
[3] Verhulst, P. F. "Notice sur la loi que la population suit dans son accroissement." Correspondance

<!-- b007244 | references | pages [25] -->
Mathématique et Physique, 1838.

<!-- b007245 | references | pages [25] -->
[4] Buckley, R. "Environmental Impacts of Ecotourism." CABI Publishing, 2004.

<!-- b007246 | references | pages [25] -->
[5] Smith, M. "Tourism Economics: Impact of Visitor Spending on Tax Revenue." Tourism Review,

<!-- b007247 | references | pages [25] -->
2015.

<!-- b007248 | references | pages [25] -->
[6] Frechtling, D. C. "Forecasting Tourism Demand:

<!-- b007249 | references | pages [25] -->
Methods and Strategies." Butterworth-

<!-- b007250 | references | pages [25] -->
Heinemann, 2001.

<!-- b007251 | references | pages [25] -->
微信号：MATHmodels

<!-- b007252 | references | pages [25] -->
[7] Glaeser, E. L., Kolko, J., & Saiz, A. "Consumer city." Journal of Economic Geography, 2001.

<!-- b007253 | references | pages [25] -->
[8] Hall, C. M., Timothy, D. J., & Duval, D. T. Safety and security in tourism: Relationships, man-

<!-- b007254 | references | pages [25] -->
agement, and marketing. Haworth Hospitality Press, 2004

<!-- b007255 | references | pages [25] -->
[9] Atzori, R. "Destination stakeholders’ perceptions of overtourism impacts, causes, and responses:

<!-- b007256 | references | pages [25] -->
The case of Big Sur, California." Journal of Destination Marketing & Management, vol. 17,

<!-- b007257 | references | pages [25] -->
2020, p. 100440.

<!-- b007258 | references | pages [25] -->
[10] Hapke, C. J., & Green, K. R. "Rates of landsliding and cliﬀretreat along the Big Sur Coast,

<!-- b007259 | references | pages [25] -->
California—Measuring a crucial baseline." USGS Fact Sheet, No. 2004-3099, 2005.

<!-- b007260 | references | pages [25] -->
[11] Swirad, Z. M., & Young, A. P. "Spatial and temporal trends in California coastal cliﬀretreat."

<!-- b007261 | references | pages [25] -->
Geomorphology, vol. 412, 2022, p. 108318.

<!-- b007262 | references | pages [25] -->
m

<!-- b007263 | references | pages [25] -->
m

<!-- b007264 | references | pages [25] -->
m

<!-- b007265 | references | pages [25] -->
m

<!-- b007266 | references | pages [25] -->
m

<!-- b007267 | references | pages [25] -->
m

<!-- b007268 | references | pages [25] -->
m

<!-- b007269 | references | pages [25] -->
m

<!-- b007270 | references | pages [25] -->
m

<!-- b007271 | references | pages [25] -->
m

<!-- b007272 | references | pages [25] -->
m

<!-- b007273 | references | pages [25] -->
m

<!-- b007274 | references | pages [25] -->
m

<!-- b007275 | references | pages [25] -->
m

<!-- b007276 | references | pages [25] -->
m

<!-- b007277 | references | pages [25] -->
m

<!-- b007278 | references | pages [25] -->
m

<!-- b007279 | references | pages [25] -->
m

<!-- b007280 | references | pages [25] -->
m

<!-- b007281 | references | pages [25] -->
m

<!-- b007282 | references | pages [25] -->
m

<!-- b007283 | references | pages [25] -->
m

<!-- b007284 | references | pages [25] -->
m

<!-- b007285 | references | pages [25] -->
m

<!-- b007286 | references | pages [25] -->
m

<!-- b007287 | references | pages [25] -->
m

<!-- b007288 | references | pages [25] -->
m

<!-- b007289 | references | pages [25] -->
m

<!-- b007290 | references | pages [25] -->
m

<!-- b007291 | references | pages [25] -->
m

<!-- b007292 | references | pages [25] -->
m

<!-- b007293 | references | pages [25] -->
m

<!-- b007294 | references | pages [25] -->
m

<!-- b007295 | references | pages [25] -->
m

<!-- b007296 | references | pages [25] -->
m

<!-- b007297 | references | pages [25] -->
m

<!-- b007298 | references | pages [25] -->
m

<!-- b007299 | references | pages [25] -->
m

<!-- b007300 | references | pages [25] -->
m

<!-- b007301 | references | pages [25] -->
m

<!-- b007302 | references | pages [25] -->
m

<!-- b007303 | references | pages [25] -->
m

<!-- b007304 | references | pages [25] -->
m

<!-- b007305 | references | pages [25] -->
m

<!-- b007306 | references | pages [25] -->
m

<!-- b007307 | references | pages [25] -->
m

<!-- b007308 | references | pages [25] -->
m

<!-- b007309 | references | pages [25] -->
m

<!-- b007310 | references | pages [25] -->
m

<!-- b007311 | references | pages [25] -->
m

<!-- b007312 | references | pages [25] -->
m

<!-- b007313 | references | pages [25] -->
m

<!-- b007314 | references | pages [25] -->
m

<!-- b007315 | references | pages [25] -->
m

<!-- b007316 | references | pages [25] -->
m

<!-- b007317 | references | pages [25] -->
m

<!-- b007318 | references | pages [25] -->
m

<!-- b007319 | references | pages [25] -->
m

<!-- b007320 | references | pages [25] -->
m

<!-- b007321 | references | pages [25] -->
m

<!-- b007322 | references | pages [25] -->
m

<!-- b007323 | references | pages [25] -->
m

<!-- b007324 | references | pages [25] -->
m

<!-- b007325 | references | pages [25] -->
m

<!-- b007326 | references | pages [25] -->
m

<!-- b007327 | references | pages [25] -->
m

<!-- b007328 | references | pages [25] -->
m

<!-- b007329 | references | pages [25] -->
m

<!-- b007330 | references | pages [25] -->
m

<!-- b007331 | references | pages [25] -->
m

<!-- b007332 | references | pages [25] -->
m

<!-- b007333 | references | pages [25] -->
m

<!-- b007334 | references | pages [25] -->
m

<!-- b007335 | references | pages [25] -->
m

<!-- b007336 | references | pages [25] -->
m

<!-- b007337 | references | pages [25] -->
m

<!-- b007338 | references | pages [25] -->
m

<!-- b007339 | references | pages [25] -->
m

<!-- b007340 | references | pages [25] -->
m

<!-- b007341 | references | pages [25] -->
m

<!-- b007342 | references | pages [25] -->
m

<!-- b007343 | references | pages [25] -->
m

<!-- b007344 | references | pages [25] -->
m

<!-- b007345 | references | pages [25] -->
m

<!-- b007346 | references | pages [25] -->
m

<!-- b007347 | references | pages [25] -->
m

<!-- b007348 | references | pages [25] -->
m

<!-- b007349 | references | pages [25] -->
m

<!-- b007350 | references | pages [25] -->
m

<!-- b007351 | references | pages [25] -->
m

<!-- b007352 | references | pages [25] -->
m

<!-- b007353 | references | pages [25] -->
m

<!-- b007354 | references | pages [25] -->
m

<!-- b007355 | references | pages [25] -->
m

<!-- b007356 | references | pages [25] -->
m

<!-- b007357 | references | pages [25] -->
m

<!-- b007358 | references | pages [25] -->
m

<!-- b007359 | references | pages [25] -->
m

<!-- b007360 | references | pages [25] -->
m

<!-- b007361 | references | pages [25] -->
m

<!-- b007362 | references | pages [25] -->
m

<!-- b007363 | references | pages [25] -->
m

<!-- b007364 | references | pages [25] -->
m

<!-- b007365 | references | pages [25] -->
m

<!-- b007366 | references | pages [25] -->
m

<!-- b007367 | references | pages [25] -->
m

<!-- b007368 | references | pages [25] -->
m

<!-- b007369 | references | pages [25] -->
m

<!-- b007370 | references | pages [25] -->
m

<!-- b007371 | references | pages [25] -->
m

<!-- b007372 | references | pages [25] -->
m

<!-- b007373 | references | pages [25] -->
m

<!-- b007374 | references | pages [25] -->
m

<!-- b007375 | references | pages [25] -->
m

<!-- b007376 | references | pages [25] -->
m

<!-- b007377 | references | pages [25] -->
m

<!-- b007378 | references | pages [25] -->
m

<!-- b007379 | references | pages [25] -->
m

<!-- b007380 | references | pages [25] -->
m

<!-- b007381 | references | pages [25] -->
m

<!-- b007382 | references | pages [25] -->
m

<!-- b007383 | references | pages [25] -->
m

<!-- b007384 | references | pages [25] -->
m

<!-- b007385 | references | pages [25] -->
m

<!-- b007386 | references | pages [25] -->
m

<!-- b007387 | references | pages [25] -->
m

<!-- b007388 | references | pages [25] -->
m

<!-- b007389 | references | pages [25] -->
m

<!-- b007390 | references | pages [25] -->
m

<!-- b007391 | references | pages [25] -->
m

<!-- b007392 | references | pages [25] -->
m

<!-- b007393 | references | pages [25] -->
m

<!-- b007394 | references | pages [25] -->
m

<!-- b007395 | references | pages [25] -->
m

<!-- b007396 | references | pages [25] -->
m

<!-- b007397 | references | pages [25] -->
m

<!-- b007398 | references | pages [25] -->
m

<!-- b007399 | references | pages [25] -->
m

<!-- b007400 | references | pages [25] -->
m

<!-- b007401 | references | pages [25] -->
m

<!-- b007402 | references | pages [25] -->
m

<!-- b007403 | references | pages [25] -->
m

<!-- b007404 | references | pages [25] -->
m

<!-- b007405 | references | pages [25] -->
m

<!-- b007406 | references | pages [25] -->
m

<!-- b007407 | references | pages [25] -->
m

<!-- b007408 | references | pages [25] -->
m

<!-- b007409 | references | pages [25] -->
m

<!-- b007410 | references | pages [25] -->
m

<!-- b007411 | references | pages [25] -->
m

<!-- b007412 | references | pages [25] -->
m

<!-- b007413 | references | pages [25] -->
m

<!-- b007414 | references | pages [25] -->
m

<!-- b007415 | references | pages [25] -->
m

<!-- b007416 | references | pages [25] -->
m

<!-- b007417 | references | pages [25] -->
m

<!-- b007418 | references | pages [25] -->
m

<!-- b007419 | references | pages [25] -->
m

<!-- b007420 | references | pages [25] -->
m

<!-- b007421 | references | pages [25] -->
m

<!-- b007422 | references | pages [25] -->
m

<!-- b007423 | references | pages [25] -->
m

<!-- b007424 | references | pages [25] -->
m

<!-- b007425 | references | pages [25] -->
m

<!-- b007426 | references | pages [25] -->
m

<!-- b007427 | references | pages [25] -->
m

<!-- b007428 | references | pages [25] -->
m

<!-- b007429 | references | pages [25] -->
m

<!-- b007430 | references | pages [25] -->
m

<!-- b007431 | references | pages [25] -->
m

<!-- b007432 | references | pages [25] -->
m

<!-- b007433 | references | pages [25] -->
m

<!-- b007434 | references | pages [25] -->
m

<!-- b007435 | references | pages [25] -->
m

<!-- b007436 | references | pages [25] -->
m

<!-- b007437 | references | pages [25] -->
m

<!-- b007438 | references | pages [25] -->
m

<!-- b007439 | references | pages [25] -->
m

<!-- b007440 | references | pages [25] -->
m

<!-- b007441 | references | pages [25] -->
m

<!-- b007442 | references | pages [25] -->
m

<!-- b007443 | references | pages [25] -->
m

<!-- b007444 | references | pages [25] -->
m

<!-- b007445 | references | pages [25] -->
m

<!-- b007446 | references | pages [25] -->
m

<!-- b007447 | references | pages [25] -->
m

<!-- b007448 | references | pages [25] -->
m

<!-- b007449 | references | pages [25] -->
m

<!-- b007450 | references | pages [25] -->
m

<!-- b007451 | references | pages [25] -->
m

<!-- b007452 | references | pages [25] -->
m

<!-- b007453 | references | pages [25] -->
m

<!-- b007454 | references | pages [25] -->
m

<!-- b007455 | references | pages [25] -->
m

<!-- b007456 | references | pages [25] -->
m

<!-- b007457 | references | pages [25] -->
m

<!-- b007458 | references | pages [25] -->
m

<!-- b007459 | references | pages [25] -->
m

<!-- b007460 | references | pages [25] -->
m

<!-- b007461 | references | pages [25] -->
m

<!-- b007462 | references | pages [25] -->
m

<!-- b007463 | references | pages [25] -->
m

<!-- b007464 | references | pages [25] -->
m

<!-- b007465 | references | pages [25] -->
m

<!-- b007466 | references | pages [25] -->
m

<!-- b007467 | references | pages [25] -->
m

<!-- b007468 | references | pages [25] -->
m

<!-- b007469 | references | pages [25] -->
m

<!-- b007470 | references | pages [25] -->
m

<!-- b007471 | references | pages [25] -->
m

<!-- b007472 | references | pages [25] -->
m

<!-- b007473 | references | pages [25] -->
m

<!-- b007474 | references | pages [25] -->
m

<!-- b007475 | references | pages [25] -->
m

<!-- b007476 | references | pages [25] -->
m

<!-- b007477 | references | pages [25] -->
m

<!-- b007478 | references | pages [25] -->
m

<!-- b007479 | references | pages [25] -->
m

<!-- b007480 | references | pages [25] -->
m

<!-- b007481 | references | pages [25] -->
m

<!-- b007482 | references | pages [25] -->
m

<!-- b007483 | references | pages [25] -->
m

<!-- b007484 | references | pages [25] -->
m

<!-- b007485 | references | pages [25] -->
m

<!-- b007486 | references | pages [25] -->
m

<!-- b007487 | references | pages [25] -->
m

<!-- b007488 | references | pages [25] -->
m

<!-- b007489 | references | pages [25] -->
m

<!-- b007490 | references | pages [25] -->
m

<!-- b007491 | references | pages [25] -->
m

<!-- b007492 | references | pages [25] -->
m

<!-- b007493 | references | pages [25] -->
m

<!-- b007494 | references | pages [25] -->
m

<!-- b007495 | references | pages [25] -->
m

<!-- b007496 | references | pages [25] -->
m

<!-- b007497 | references | pages [25] -->
m

<!-- b007498 | references | pages [25] -->
m

<!-- b007499 | references | pages [25] -->
m

<!-- b007500 | references | pages [25] -->
m

<!-- b007501 | references | pages [25] -->
m

<!-- b007502 | references | pages [25] -->
m

<!-- b007503 | references | pages [25] -->
m

<!-- b007504 | references | pages [25] -->
m

<!-- b007505 | references | pages [25] -->
m

<!-- b007506 | references | pages [25] -->
m

<!-- b007507 | references | pages [25] -->
m

<!-- b007508 | references | pages [25] -->
m

<!-- b007509 | references | pages [25] -->
m

<!-- b007510 | references | pages [25] -->
m

<!-- b007511 | references | pages [25] -->
m

<!-- b007512 | references | pages [25] -->
m

<!-- b007513 | references | pages [25] -->
m

<!-- b007514 | references | pages [25] -->
m

<!-- b007515 | references | pages [25] -->
m

<!-- b007516 | references | pages [25] -->
m

<!-- b007517 | references | pages [25] -->
m

<!-- b007518 | references | pages [25] -->
m

<!-- b007519 | references | pages [25] -->
m

<!-- b007520 | references | pages [25] -->
m

<!-- b007521 | references | pages [25] -->
m

<!-- b007522 | references | pages [25] -->
m

<!-- b007523 | references | pages [25] -->
m

<!-- b007524 | references | pages [25] -->
m

<!-- b007525 | references | pages [25] -->
m

<!-- b007526 | references | pages [25] -->
m

<!-- b007527 | references | pages [25] -->
m

<!-- b007528 | references | pages [25] -->
m

<!-- b007529 | references | pages [25] -->
m

<!-- b007530 | references | pages [25] -->
m

<!-- b007531 | references | pages [25] -->
m

<!-- b007532 | references | pages [25] -->
m

<!-- b007533 | references | pages [25] -->
m

<!-- b007534 | references | pages [25] -->
m

<!-- b007535 | references | pages [25] -->
m

<!-- b007536 | references | pages [25] -->
m

<!-- b007537 | references | pages [25] -->
m

<!-- b007538 | references | pages [25] -->
m

<!-- b007539 | references | pages [25] -->
m

<!-- b007540 | references | pages [25] -->
m

<!-- b007541 | references | pages [25] -->
m

<!-- b007542 | references | pages [25] -->
m

<!-- b007543 | references | pages [25] -->
m

<!-- b007544 | references | pages [25] -->
m

<!-- b007545 | references | pages [25] -->
m

<!-- b007546 | furniture | pages [25] -->
m

<!-- b007547 | furniture | pages [25] -->
m

<!-- b007548 | furniture | pages [25] -->
m

<!-- b007549 | furniture | pages [25] -->
m

<!-- b007550 | furniture | pages [25] -->
m

<!-- b007551 | furniture | pages [25] -->
m

<!-- b007552 | furniture | pages [25] -->
m

<!-- b007553 | furniture | pages [25] -->
m

<!-- b007554 | furniture | pages [25] -->
m

<!-- b007555 | furniture | pages [25] -->
m

<!-- b007556 | furniture | pages [25] -->
m

<!-- b007557 | furniture | pages [25] -->
m

<!-- b007558 | furniture | pages [25] -->
m

<!-- b007559 | furniture | pages [25] -->
m

<!-- b007560 | furniture | pages [25] -->
m

<!-- b007561 | furniture | pages [25] -->
m

<!-- b007562 | furniture | pages [25] -->
m

<!-- b007563 | furniture | pages [25] -->
m

<!-- b007564 | furniture | pages [25] -->
m

<!-- b007565 | furniture | pages [25] -->
m

<!-- b007566 | furniture | pages [25] -->
m

<!-- b007567 | furniture | pages [25] -->
m

<!-- b007568 | furniture | pages [25] -->
m

<!-- b007569 | furniture | pages [25] -->
m

<!-- b007570 | furniture | pages [25] -->
m

<!-- b007571 | furniture | pages [25] -->
m

<!-- b007572 | furniture | pages [25] -->
m

<!-- b007573 | furniture | pages [25] -->
m

<!-- b007574 | furniture | pages [25] -->
m

<!-- b007575 | furniture | pages [25] -->
m

<!-- b007576 | furniture | pages [25] -->
m

<!-- b007577 | furniture | pages [25] -->
m

<!-- b007578 | furniture | pages [25] -->
m

<!-- b007579 | furniture | pages [25] -->
m

<!-- b007580 | furniture | pages [25] -->
m

<!-- b007581 | furniture | pages [25] -->
m

<!-- b007582 | furniture | pages [25] -->
m

<!-- b007583 | furniture | pages [25] -->
m

<!-- b007584 | furniture | pages [25] -->
m

<!-- b007585 | furniture | pages [25] -->
m

<!-- b007586 | furniture | pages [25] -->
m

<!-- b007587 | furniture | pages [25] -->
m

<!-- b007588 | furniture | pages [25] -->
m

<!-- b007589 | furniture | pages [25] -->
m

<!-- b007590 | furniture | pages [25] -->
m

<!-- b007591 | furniture | pages [25] -->
m

<!-- b007592 | furniture | pages [25] -->
m

<!-- b007593 | furniture | pages [25] -->
m

<!-- b007594 | furniture | pages [25] -->
m

<!-- b007595 | furniture | pages [25] -->
m

<!-- b007596 | furniture | pages [25] -->
m

<!-- b007597 | furniture | pages [25] -->
m

<!-- b007598 | furniture | pages [25] -->
m

<!-- b007599 | furniture | pages [25] -->
m

<!-- b007600 | furniture | pages [25] -->
m

<!-- b007601 | furniture | pages [25] -->
m

<!-- b007602 | furniture | pages [25] -->
m

<!-- b007603 | furniture | pages [25] -->
m

<!-- b007604 | furniture | pages [25] -->
m

<!-- b007605 | furniture | pages [25] -->
m

<!-- b007606 | furniture | pages [25] -->
m

<!-- b007607 | furniture | pages [25] -->
m

<!-- b007608 | furniture | pages [25] -->
m

<!-- b007609 | furniture | pages [25] -->
m

<!-- b007610 | furniture | pages [25] -->
m

<!-- b007611 | furniture | pages [25] -->
m

<!-- b007612 | furniture | pages [25] -->
m

<!-- b007613 | furniture | pages [25] -->
m

<!-- b007614 | furniture | pages [25] -->
m

<!-- b007615 | furniture | pages [25] -->
m

<!-- b007616 | furniture | pages [25] -->
m

<!-- b007617 | furniture | pages [25] -->
m

<!-- b007618 | furniture | pages [25] -->
m

<!-- b007619 | furniture | pages [25] -->
m

<!-- b007620 | furniture | pages [25] -->
m

<!-- b007621 | furniture | pages [25] -->
m

<!-- b007622 | furniture | pages [25] -->
m

<!-- b007623 | furniture | pages [25] -->
m

<!-- b007624 | furniture | pages [25] -->
m

<!-- b007625 | furniture | pages [25] -->
m

<!-- b007626 | furniture | pages [25] -->
m

<!-- b007627 | furniture | pages [25] -->
m

<!-- b007628 | furniture | pages [25] -->
m

<!-- b007629 | furniture | pages [25] -->
m

<!-- b007630 | furniture | pages [25] -->
m

<!-- b007631 | furniture | pages [25] -->
m

<!-- b007632 | furniture | pages [25] -->
m

<!-- b007633 | furniture | pages [25] -->
m

<!-- b007634 | furniture | pages [25] -->
m

<!-- b007635 | furniture | pages [25] -->
m

<!-- b007636 | furniture | pages [25] -->
m

<!-- b007637 | furniture | pages [25] -->
m

<!-- b007638 | furniture | pages [25] -->
m

<!-- b007639 | furniture | pages [25] -->
m

<!-- b007640 | furniture | pages [25] -->
m

<!-- b007641 | furniture | pages [25] -->
m

<!-- b007642 | furniture | pages [25] -->
m

<!-- b007643 | furniture | pages [25] -->
m

<!-- b007644 | furniture | pages [25] -->
m

<!-- b007645 | furniture | pages [25] -->
m

<!-- b007646 | furniture | pages [25] -->
m

<!-- b007647 | furniture | pages [25] -->
m

<!-- b007648 | furniture | pages [25] -->
m

<!-- b007649 | furniture | pages [25] -->
m

<!-- b007650 | furniture | pages [25] -->
m

<!-- b007651 | furniture | pages [25] -->
m

<!-- b007652 | furniture | pages [25] -->
m

<!-- b007653 | furniture | pages [25] -->
m

<!-- b007654 | furniture | pages [25] -->
m

<!-- b007655 | furniture | pages [25] -->
m

<!-- b007656 | furniture | pages [25] -->
m

<!-- b007657 | furniture | pages [25] -->
m

<!-- b007658 | furniture | pages [25] -->
m

<!-- b007659 | furniture | pages [25] -->
m

<!-- b007660 | furniture | pages [25] -->
m

<!-- b007661 | furniture | pages [25] -->
m

<!-- b007662 | furniture | pages [25] -->
m

<!-- b007663 | furniture | pages [25] -->
m

<!-- b007664 | furniture | pages [25] -->
m

<!-- b007665 | furniture | pages [25] -->
m

<!-- b007666 | furniture | pages [25] -->
m

<!-- b007667 | furniture | pages [25] -->
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

<!-- b007949 | furniture | pages [26] -->
Team # 2503268

<!-- b007950 | furniture | pages [26] -->
Page 24 of 24

<!-- b007951 | heading | pages [26] -->
Report on Use of AI

<!-- b007952 | ai_disclosure | pages [26] -->
OpenAI ChatGPT(Jan 14, 2025 version, ChatGPT-4o)

<!-- b007953 | ai_disclosure | pages [26] -->
Query: The intervention strategies are divided into tax revenue allocation and policies. Both

<!-- b007954 | ai_disclosure | pages [26] -->
parts have a ﬁnite set of typical and representative solutions. We iterate over these two sets to get a

<!-- b007955 | ai_disclosure | pages [26] -->
ﬁnite number of combinations. Now we have the previous value of H, N, T. For each combination,

<!-- b007956 | ai_disclosure | pages [26] -->
we’ll obtain diﬀerent values of new H, N, T and their corresponding scores if various constraints are

<!-- b007957 | ai_disclosure | pages [26] -->
satisﬁed. Then, pick the best score and the best combination as the current intervention strategy. Pick

<!-- b007958 | ai_disclosure | pages [26] -->
the corresponding H, N, T as the new H, N, T. Help me improve the ﬂuency and readability.

<!-- b007959 | ai_disclosure | pages [26] -->
Output: We categorize our intervention strategies into two components: tax revenue allocation

<!-- b007960 | ai_disclosure | pages [26] -->
and policies. Each component features a ﬁnite set of typical and representative solutions. By iterating

<!-- b007961 | ai_disclosure | pages [26] -->
through these solutions, we obtain a ﬁnite set of potential strategy combinations. Given the current

<!-- b007962 | ai_disclosure | pages [26] -->
values of H, N, and T, each combination, under the given constraints, produces new H, N, and T val-

<!-- b007963 | ai_disclosure | pages [26] -->
ues along with corresponding scores. We then select the combination with the highest score to serve

<!-- b007964 | ai_disclosure | pages [26] -->
as the current intervention strategy, and update H, N, and T accordingly to these new values.

<!-- b007965 | ai_disclosure | pages [26] -->
OpenAI ChatGPT(Jan 14, 2025 version, ChatGPT-4o)

<!-- b007966 | ai_disclosure | pages [26] -->
Query:Notably, the challenges faced by Juneau are not unique but part of a broader global phe-

<!-- b007967 | ai_disclosure | pages [26] -->
nomenon. Numerous destinations worldwide grapple with similar issues. For instance, Mount Rainier

<!-- b007968 | ai_disclosure | pages [26] -->
National Park in the United States has implemented reservation systems to mitigate overcrowding,

<!-- b007969 | ai_disclosure | pages [26] -->
while cities like Venice and Barcelona in Europe have introduced day-trip fees for visitors. Athens,

<!-- b007970 | ai_disclosure | pages [26] -->
Greece, is also exploring limits on tourist capacity. These examples underscore the pressing need for

<!-- b007971 | ai_disclosure | pages [26] -->
a comprehensive framework that balances economic beneﬁts with resource conservation. In response,

<!-- b007972 | ai_disclosure | pages [26] -->
our work seeks to develop a systematic and scalable model for sustainable tourism, oﬀering solu-

<!-- b007973 | ai_disclosure | pages [26] -->
tions tailored to Juneau while providing a blueprint for other destinations to address the challenges of

<!-- b007974 | ai_disclosure | pages [26] -->
overtourism and achieve long-term resilience. Simplify language.

<!-- b007975 | ai_disclosure | pages [26] -->
Output: The challenges faced by Juneau reﬂect a global issue. Destinations like Mount Rainier

<!-- b007976 | ai_disclosure | pages [26] -->
National Park use reservation systems, while Venice and Barcelona impose day-trip fees. Athens is

<!-- b007977 | ai_disclosure | pages [26] -->
exploring tourist limits, highlighting the need for a framework balancing economic beneﬁts and con-

<!-- b007978 | ai_disclosure | pages [26] -->
servation. This work aims to create a scalable model for sustainable tourism, addressing Juneau’s

<!-- b007979 | ai_disclosure | pages [26] -->
needs and oﬀering solutions for overtourism and long-term resilience.

<!-- b007980 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b007981 | furniture | pages [26] -->
2

<!-- b007982 | furniture | pages [26] -->
MATHmodels

<!-- b007983 | furniture | pages [26] -->
获取更多资讯
