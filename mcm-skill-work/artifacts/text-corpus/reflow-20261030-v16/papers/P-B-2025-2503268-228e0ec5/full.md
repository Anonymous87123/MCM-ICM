# P-B-2025-2503268-228e0ec5

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

<!-- b000022 | heading | pages [2] -->
Memo

<!-- b000023 | prose | pages [2] -->
Dear Members of the Juneau Tourist Council,

<!-- b000024 | prose | pages [2] -->
Juneau's record-breaking 1.6 million cruise passengers in 2023 has undoubtedly brought significant economic benefits, but it has also amplified the challenges of overcrowding, resource depletion, and ecological strain, particularly on Mendenhall Glacier. As the glacier continues to recede, we must confront the reality that the very attractions drawing visitors to Juneau are under threat. Strikinga balance between tourism growth and sustainability is not just essential—it is urgent.

<!-- b000025 | prose | pages [2] -->
Our team has developed a dynamic model to address these challenges by evaluating the interplay between economic benefits, environmental conservation, and community well-being. Through this framework, we've identified actionable strategies that can optimize outcomes for all stakeholders.

<!-- b000026 | prose | pages [2] -->
First, we recommend implementing visitor caps at key attractions like Mendenhall Glacier to mitigate environmental stress while maintaining toun   dd sis  d   tsts sne ecological protection with revenue retention. Additionally, allocating a gr orrf  u nr  user o rtod rueos glaats d a i e  ai ie the natural environment and extend the lifespan of Juneau's unique attractions. For example, directing 40% of annual tourism revenue toward environmental initiatives could reduce glacier degradation rates by up to 30% annually.

<!-- b000027 | prose | pages [2] -->
Equally important is addressing the concerns of Juneau's residents. Overcrowdingand rising housing costs have left many locals feeling sidelined tn em  e l  r     ust  s using tourism revenues to improve housingaffordability andprovide community incentives, such as tax relief or subsidies for residents. These measures not only ease tensions but also reinforce the idea that sustainable tourism benefits everyone—not just visitors.

<!-- b000028 | prose | pages [2] -->
Sustainable tourism is a delicate yet achievable goal for Juneau. By integrating ecological protection, community engagement, and thoughtful revenue allocation into its policies, the city can preserve its natural beauty and economic vitality for years to come. We are confident that the strategies outlined above will provide a robust starting point for achieving this vision.

<!-- b000029 | prose | pages [2] -->
Sincerely,

<!-- b000030 | heading | pages [2] -->
MCM Team #2503268

<!-- b000031 | prose | pages [2] -->
January 27, 2025

<!-- b000032 | furniture | pages [3] -->
Team # 2503268

<!-- b000033 | furniture | pages [3] -->
Page 1 of 24

<!-- b000034 | heading | pages [3] -->
Contents

<!-- b000035 | contents | pages [3] -->
1 Introduction

<!-- b000036 | contents | pages [3] -->
2

<!-- b000037 | contents | pages [3] -->
微信公众号：数学模型

<!-- b000038 | contents | pages [3] -->
1.1

<!-- b000039 | contents | pages [3] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [3] -->
2

<!-- b000041 | contents | pages [3] -->
1.2

<!-- b000042 | contents | pages [3] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [3] -->
2

<!-- b000044 | contents | pages [3] -->
1.3

<!-- b000045 | contents | pages [3] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [3] -->
2

<!-- b000047 | contents | pages [3] -->
2 Assumptions and Justiﬁcations

<!-- b000048 | contents | pages [3] -->
3

<!-- b000049 | contents | pages [3] -->
3 Notations

<!-- b000050 | contents | pages [3] -->
4

<!-- b000051 | contents | pages [3] -->
4 Model Preparation

<!-- b000052 | contents | pages [3] -->
5

<!-- b000053 | contents | pages [3] -->
4.1

<!-- b000054 | contents | pages [3] -->
Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [3] -->
5

<!-- b000056 | contents | pages [3] -->
4.2

<!-- b000057 | contents | pages [3] -->
Data Selection Explanation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [3] -->
5

<!-- b000059 | contents | pages [3] -->
5 Model Design

<!-- b000060 | contents | pages [3] -->
6

<!-- b000061 | contents | pages [3] -->
微信号：MATHmodels

<!-- b000062 | contents | pages [3] -->
5.1

<!-- b000063 | contents | pages [3] -->
Sustainable Tourism Dynamics Model (STDM) . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [3] -->
6

<!-- b000065 | contents | pages [3] -->
5.1.1

<!-- b000066 | contents | pages [3] -->
Glacier ELA Height Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [3] -->
6

<!-- b000068 | contents | pages [3] -->
5.1.2

<!-- b000069 | contents | pages [3] -->
Tourist Number Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [3] -->
7

<!-- b000071 | contents | pages [3] -->
5.1.3

<!-- b000072 | contents | pages [3] -->
Economic Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [3] -->
7

<!-- b000074 | contents | pages [3] -->
5.1.4

<!-- b000075 | contents | pages [3] -->
Model Integration and Parameter Estimation . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [3] -->
7

<!-- b000077 | contents | pages [3] -->
5.2

<!-- b000078 | contents | pages [3] -->
Intervention Strategies

<!-- b000079 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [3] -->
9

<!-- b000081 | contents | pages [3] -->
5.2.1

<!-- b000082 | contents | pages [3] -->
Intervention Impact on Models . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [3] -->
9

<!-- b000084 | contents | pages [3] -->
5.2.2

<!-- b000085 | contents | pages [3] -->
Tax Revenue Allocation

<!-- b000086 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [3] -->
10

<!-- b000088 | contents | pages [3] -->
5.2.3

<!-- b000089 | contents | pages [3] -->
Policies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [3] -->
10

<!-- b000091 | contents | pages [3] -->
6 Evaluation Model

<!-- b000092 | contents | pages [3] -->
10

<!-- b000093 | contents | pages [3] -->
6.1

<!-- b000094 | contents | pages [3] -->
Indicators Determination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [3] -->
10

<!-- b000096 | contents | pages [3] -->
6.2

<!-- b000097 | contents | pages [3] -->
Score Calculation Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [3] -->
11

<!-- b000099 | contents | pages [3] -->
6.3

<!-- b000100 | contents | pages [3] -->
Values of Parameters

<!-- b000101 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [3] -->
14

<!-- b000103 | contents | pages [3] -->
6.4

<!-- b000104 | contents | pages [3] -->
Weights Distribution Outcomes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [3] -->
14

<!-- b000106 | contents | pages [3] -->
7 Analysis of Factors

<!-- b000107 | contents | pages [3] -->
14

<!-- b000108 | contents | pages [3] -->
8 Results and Discussion

<!-- b000109 | contents | pages [3] -->
16

<!-- b000110 | contents | pages [3] -->
9 Sensitivity Analysis

<!-- b000111 | contents | pages [3] -->
17

<!-- b000112 | contents | pages [3] -->
9.1

<!-- b000113 | contents | pages [3] -->
Qualitative analysis: Morris Method . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000114 | contents | pages [3] -->
17

<!-- b000115 | contents | pages [3] -->
9.2

<!-- b000116 | contents | pages [3] -->
Quantitative analysis: Local Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . .

<!-- b000117 | contents | pages [3] -->
18

<!-- b000118 | contents | pages [3] -->
10 Reimagining Big Sur

<!-- b000119 | contents | pages [3] -->
19

<!-- b000120 | contents | pages [3] -->
10.1 Fundamental Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [3] -->
19

<!-- b000122 | contents | pages [3] -->
10.2 Model Validation and Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [3] -->
20

<!-- b000124 | contents | pages [3] -->
11 Strengths and Weaknesses

<!-- b000125 | contents | pages [3] -->
22

<!-- b000126 | contents | pages [3] -->
11.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000127 | contents | pages [3] -->
22

<!-- b000128 | contents | pages [3] -->
11.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000129 | contents | pages [3] -->
22

<!-- b000130 | contents | pages [3] -->
References

<!-- b000131 | contents | pages [3] -->
23

<!-- b000132 | contents | pages [3] -->
m

<!-- b000133 | contents | pages [3] -->
m

<!-- b000134 | contents | pages [3] -->
m

<!-- b000135 | contents | pages [3] -->
m

<!-- b000136 | contents | pages [3] -->
m

<!-- b000137 | contents | pages [3] -->
m

<!-- b000138 | contents | pages [3] -->
m

<!-- b000139 | contents | pages [3] -->
m

<!-- b000140 | contents | pages [3] -->
m

<!-- b000141 | contents | pages [3] -->
m

<!-- b000142 | contents | pages [3] -->
m

<!-- b000143 | contents | pages [3] -->
m

<!-- b000144 | contents | pages [3] -->
m

<!-- b000145 | contents | pages [3] -->
m

<!-- b000146 | contents | pages [3] -->
m

<!-- b000147 | contents | pages [3] -->
m

<!-- b000148 | contents | pages [3] -->
m

<!-- b000149 | contents | pages [3] -->
m

<!-- b000150 | contents | pages [3] -->
m

<!-- b000151 | contents | pages [3] -->
m

<!-- b000152 | contents | pages [3] -->
m

<!-- b000153 | contents | pages [3] -->
m

<!-- b000154 | contents | pages [3] -->
m

<!-- b000155 | contents | pages [3] -->
m

<!-- b000156 | contents | pages [3] -->
m

<!-- b000157 | contents | pages [3] -->
m

<!-- b000158 | contents | pages [3] -->
m

<!-- b000159 | contents | pages [3] -->
m

<!-- b000160 | contents | pages [3] -->
m

<!-- b000161 | contents | pages [3] -->
m

<!-- b000162 | contents | pages [3] -->
m

<!-- b000163 | contents | pages [3] -->
m

<!-- b000164 | contents | pages [3] -->
m

<!-- b000165 | contents | pages [3] -->
m

<!-- b000166 | contents | pages [3] -->
m

<!-- b000167 | contents | pages [3] -->
m

<!-- b000168 | contents | pages [3] -->
m

<!-- b000169 | contents | pages [3] -->
m

<!-- b000170 | contents | pages [3] -->
m

<!-- b000171 | contents | pages [3] -->
m

<!-- b000172 | contents | pages [3] -->
m

<!-- b000173 | contents | pages [3] -->
m

<!-- b000174 | contents | pages [3] -->
m

<!-- b000175 | contents | pages [3] -->
m

<!-- b000176 | contents | pages [3] -->
m

<!-- b000177 | contents | pages [3] -->
m

<!-- b000178 | contents | pages [3] -->
m

<!-- b000179 | contents | pages [3] -->
m

<!-- b000180 | contents | pages [3] -->
m

<!-- b000181 | contents | pages [3] -->
m

<!-- b000182 | contents | pages [3] -->
m

<!-- b000183 | contents | pages [3] -->
m

<!-- b000184 | contents | pages [3] -->
m

<!-- b000185 | contents | pages [3] -->
m

<!-- b000186 | contents | pages [3] -->
m

<!-- b000187 | contents | pages [3] -->
m

<!-- b000188 | contents | pages [3] -->
m

<!-- b000189 | contents | pages [3] -->
m

<!-- b000190 | contents | pages [3] -->
m

<!-- b000191 | contents | pages [3] -->
m

<!-- b000192 | contents | pages [3] -->
m

<!-- b000193 | contents | pages [3] -->
m

<!-- b000194 | contents | pages [3] -->
m

<!-- b000195 | contents | pages [3] -->
m

<!-- b000196 | contents | pages [3] -->
m

<!-- b000197 | contents | pages [3] -->
m

<!-- b000198 | contents | pages [3] -->
m

<!-- b000199 | contents | pages [3] -->
m

<!-- b000200 | contents | pages [3] -->
m

<!-- b000201 | contents | pages [3] -->
m

<!-- b000202 | contents | pages [3] -->
m

<!-- b000203 | contents | pages [3] -->
m

<!-- b000204 | contents | pages [3] -->
m

<!-- b000205 | contents | pages [3] -->
m

<!-- b000206 | contents | pages [3] -->
m

<!-- b000207 | contents | pages [3] -->
m

<!-- b000208 | contents | pages [3] -->
m

<!-- b000209 | contents | pages [3] -->
m

<!-- b000210 | contents | pages [3] -->
m

<!-- b000211 | contents | pages [3] -->
m

<!-- b000212 | contents | pages [3] -->
m

<!-- b000213 | contents | pages [3] -->
m

<!-- b000214 | contents | pages [3] -->
m

<!-- b000215 | contents | pages [3] -->
m

<!-- b000216 | contents | pages [3] -->
m

<!-- b000217 | contents | pages [3] -->
m

<!-- b000218 | contents | pages [3] -->
m

<!-- b000219 | contents | pages [3] -->
m

<!-- b000220 | contents | pages [3] -->
m

<!-- b000221 | contents | pages [3] -->
m

<!-- b000222 | contents | pages [3] -->
m

<!-- b000223 | contents | pages [3] -->
m

<!-- b000224 | contents | pages [3] -->
m

<!-- b000225 | contents | pages [3] -->
m

<!-- b000226 | contents | pages [3] -->
m

<!-- b000227 | contents | pages [3] -->
m

<!-- b000228 | contents | pages [3] -->
m

<!-- b000229 | contents | pages [3] -->
m

<!-- b000230 | contents | pages [3] -->
m

<!-- b000231 | contents | pages [3] -->
m

<!-- b000232 | contents | pages [3] -->
m

<!-- b000233 | contents | pages [3] -->
m

<!-- b000234 | contents | pages [3] -->
m

<!-- b000235 | contents | pages [3] -->
m

<!-- b000236 | contents | pages [3] -->
m

<!-- b000237 | contents | pages [3] -->
m

<!-- b000238 | contents | pages [3] -->
m

<!-- b000239 | contents | pages [3] -->
m

<!-- b000240 | contents | pages [3] -->
m

<!-- b000241 | contents | pages [3] -->
m

<!-- b000242 | contents | pages [3] -->
m

<!-- b000243 | contents | pages [3] -->
m

<!-- b000244 | contents | pages [3] -->
m

<!-- b000245 | contents | pages [3] -->
m

<!-- b000246 | contents | pages [3] -->
m

<!-- b000247 | contents | pages [3] -->
m

<!-- b000248 | contents | pages [3] -->
m

<!-- b000249 | contents | pages [3] -->
m

<!-- b000250 | contents | pages [3] -->
m

<!-- b000251 | contents | pages [3] -->
m

<!-- b000252 | contents | pages [3] -->
m

<!-- b000253 | contents | pages [3] -->
m

<!-- b000254 | contents | pages [3] -->
m

<!-- b000255 | contents | pages [3] -->
m

<!-- b000256 | contents | pages [3] -->
m

<!-- b000257 | contents | pages [3] -->
m

<!-- b000258 | contents | pages [3] -->
m

<!-- b000259 | contents | pages [3] -->
m

<!-- b000260 | contents | pages [3] -->
m

<!-- b000261 | contents | pages [3] -->
m

<!-- b000262 | contents | pages [3] -->
m

<!-- b000263 | contents | pages [3] -->
m

<!-- b000264 | contents | pages [3] -->
m

<!-- b000265 | contents | pages [3] -->
m

<!-- b000266 | contents | pages [3] -->
m

<!-- b000267 | contents | pages [3] -->
m

<!-- b000268 | contents | pages [3] -->
m

<!-- b000269 | contents | pages [3] -->
m

<!-- b000270 | contents | pages [3] -->
m

<!-- b000271 | contents | pages [3] -->
m

<!-- b000272 | contents | pages [3] -->
m

<!-- b000273 | contents | pages [3] -->
m

<!-- b000274 | contents | pages [3] -->
m

<!-- b000275 | contents | pages [3] -->
m

<!-- b000276 | contents | pages [3] -->
m

<!-- b000277 | contents | pages [3] -->
m

<!-- b000278 | contents | pages [3] -->
m

<!-- b000279 | contents | pages [3] -->
m

<!-- b000280 | contents | pages [3] -->
m

<!-- b000281 | contents | pages [3] -->
m

<!-- b000282 | contents | pages [3] -->
m

<!-- b000283 | contents | pages [3] -->
m

<!-- b000284 | contents | pages [3] -->
m

<!-- b000285 | contents | pages [3] -->
m

<!-- b000286 | contents | pages [3] -->
m

<!-- b000287 | contents | pages [3] -->
m

<!-- b000288 | contents | pages [3] -->
m

<!-- b000289 | contents | pages [3] -->
m

<!-- b000290 | contents | pages [3] -->
m

<!-- b000291 | contents | pages [3] -->
m

<!-- b000292 | contents | pages [3] -->
m

<!-- b000293 | contents | pages [3] -->
m

<!-- b000294 | contents | pages [3] -->
m

<!-- b000295 | contents | pages [3] -->
m

<!-- b000296 | contents | pages [3] -->
m

<!-- b000297 | contents | pages [3] -->
m

<!-- b000298 | contents | pages [3] -->
m

<!-- b000299 | contents | pages [3] -->
m

<!-- b000300 | contents | pages [3] -->
m

<!-- b000301 | contents | pages [3] -->
m

<!-- b000302 | contents | pages [3] -->
m

<!-- b000303 | contents | pages [3] -->
m

<!-- b000304 | contents | pages [3] -->
m

<!-- b000305 | contents | pages [3] -->
m

<!-- b000306 | contents | pages [3] -->
m

<!-- b000307 | contents | pages [3] -->
m

<!-- b000308 | contents | pages [3] -->
m

<!-- b000309 | contents | pages [3] -->
m

<!-- b000310 | contents | pages [3] -->
m

<!-- b000311 | contents | pages [3] -->
m

<!-- b000312 | contents | pages [3] -->
m

<!-- b000313 | contents | pages [3] -->
m

<!-- b000314 | contents | pages [3] -->
m

<!-- b000315 | contents | pages [3] -->
m

<!-- b000316 | contents | pages [3] -->
m

<!-- b000317 | contents | pages [3] -->
m

<!-- b000318 | contents | pages [3] -->
m

<!-- b000319 | contents | pages [3] -->
m

<!-- b000320 | contents | pages [3] -->
m

<!-- b000321 | contents | pages [3] -->
m

<!-- b000322 | contents | pages [3] -->
m

<!-- b000323 | contents | pages [3] -->
m

<!-- b000324 | contents | pages [3] -->
m

<!-- b000325 | contents | pages [3] -->
m

<!-- b000326 | contents | pages [3] -->
m

<!-- b000327 | contents | pages [3] -->
m

<!-- b000328 | contents | pages [3] -->
m

<!-- b000329 | contents | pages [3] -->
m

<!-- b000330 | contents | pages [3] -->
m

<!-- b000331 | contents | pages [3] -->
m

<!-- b000332 | contents | pages [3] -->
m

<!-- b000333 | contents | pages [3] -->
m

<!-- b000334 | contents | pages [3] -->
m

<!-- b000335 | contents | pages [3] -->
m

<!-- b000336 | contents | pages [3] -->
m

<!-- b000337 | contents | pages [3] -->
m

<!-- b000338 | contents | pages [3] -->
m

<!-- b000339 | contents | pages [3] -->
m

<!-- b000340 | contents | pages [3] -->
m

<!-- b000341 | contents | pages [3] -->
m

<!-- b000342 | contents | pages [3] -->
m

<!-- b000343 | contents | pages [3] -->
m

<!-- b000344 | contents | pages [3] -->
m

<!-- b000345 | contents | pages [3] -->
m

<!-- b000346 | contents | pages [3] -->
m

<!-- b000347 | contents | pages [3] -->
m

<!-- b000348 | contents | pages [3] -->
m

<!-- b000349 | contents | pages [3] -->
m

<!-- b000350 | contents | pages [3] -->
m

<!-- b000351 | contents | pages [3] -->
m

<!-- b000352 | contents | pages [3] -->
m

<!-- b000353 | contents | pages [3] -->
m

<!-- b000354 | contents | pages [3] -->
m

<!-- b000355 | contents | pages [3] -->
m

<!-- b000356 | contents | pages [3] -->
m

<!-- b000357 | contents | pages [3] -->
m

<!-- b000358 | contents | pages [3] -->
m

<!-- b000359 | contents | pages [3] -->
m

<!-- b000360 | contents | pages [3] -->
m

<!-- b000361 | contents | pages [3] -->
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

<!-- b000686 | furniture | pages [4] -->
m

<!-- b000687 | furniture | pages [4] -->
m

<!-- b000688 | furniture | pages [4] -->
m

<!-- b000689 | furniture | pages [4] -->
m

<!-- b000690 | furniture | pages [4] -->
m

<!-- b000691 | furniture | pages [4] -->
m

<!-- b000692 | furniture | pages [4] -->
m

<!-- b000693 | furniture | pages [4] -->
m

<!-- b000694 | furniture | pages [4] -->
m

<!-- b000695 | furniture | pages [4] -->
m

<!-- b000696 | furniture | pages [4] -->
m

<!-- b000697 | furniture | pages [4] -->
m

<!-- b000698 | furniture | pages [4] -->
m

<!-- b000699 | furniture | pages [4] -->
m

<!-- b000700 | furniture | pages [4] -->
m

<!-- b000701 | furniture | pages [4] -->
m

<!-- b000702 | furniture | pages [4] -->
m

<!-- b000703 | furniture | pages [4] -->
m

<!-- b000704 | furniture | pages [4] -->
m

<!-- b000705 | furniture | pages [4] -->
m

<!-- b000706 | furniture | pages [4] -->
m

<!-- b000707 | furniture | pages [4] -->
m

<!-- b000708 | furniture | pages [4] -->
m

<!-- b000709 | furniture | pages [4] -->
m

<!-- b000710 | furniture | pages [4] -->
m

<!-- b000711 | furniture | pages [4] -->
m

<!-- b000712 | furniture | pages [4] -->
m

<!-- b000713 | furniture | pages [4] -->
m

<!-- b000714 | furniture | pages [4] -->
m

<!-- b000715 | furniture | pages [4] -->
m

<!-- b000716 | furniture | pages [4] -->
m

<!-- b000717 | furniture | pages [4] -->
m

<!-- b000718 | furniture | pages [4] -->
m

<!-- b000719 | furniture | pages [4] -->
m

<!-- b000720 | furniture | pages [4] -->
m

<!-- b000721 | furniture | pages [4] -->
m

<!-- b000722 | furniture | pages [4] -->
m

<!-- b000723 | furniture | pages [4] -->
m

<!-- b000724 | furniture | pages [4] -->
m

<!-- b000725 | furniture | pages [4] -->
m

<!-- b000726 | furniture | pages [4] -->
m

<!-- b000727 | furniture | pages [4] -->
m

<!-- b000728 | furniture | pages [4] -->
m

<!-- b000729 | furniture | pages [4] -->
m

<!-- b000730 | furniture | pages [4] -->
m

<!-- b000731 | furniture | pages [4] -->
m

<!-- b000732 | furniture | pages [4] -->
m

<!-- b000733 | furniture | pages [4] -->
m

<!-- b000734 | furniture | pages [4] -->
m

<!-- b000735 | furniture | pages [4] -->
m

<!-- b000736 | furniture | pages [4] -->
m

<!-- b000737 | furniture | pages [4] -->
m

<!-- b000738 | furniture | pages [4] -->
m

<!-- b000739 | furniture | pages [4] -->
m

<!-- b000740 | furniture | pages [4] -->
m

<!-- b000741 | furniture | pages [4] -->
m

<!-- b000742 | furniture | pages [4] -->
m

<!-- b000743 | furniture | pages [4] -->
m

<!-- b000744 | furniture | pages [4] -->
m

<!-- b000745 | furniture | pages [4] -->
m

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
Team # 2503268

<!-- b001032 | furniture | pages [4] -->
Page 2 of 24

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
m

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

<!-- b001188 | heading | pages [4] -->
1 Introduction

<!-- b001189 | heading | pages [4] -->
1.1 Problem Background

<!-- b001190 | prose | pages [4] -->
Juneau, Alaska, renowned for its stunning natural landscapes and rich tourism resources, has be- come a prominent destination for cruise passengers. But the rapid increase in tourist numbers in recent years has posed signiﬁcant challenges to the local environment, infrastructure, and residents’ quality of life. While measures such as daily visitor caps and agreements with cruise operators represent initial steps toward addressing these issues, they remain insuﬃcient to ensure the sustainable development of tourism in the region.

<!-- b001191 | prose | pages [4] -->
Notably, the challenges faced by Juneau reﬂect a global issue. Numerous destinations worldwide grapple with similar issues. Destinations like Mount Rainier National Park use reservation systems, while Venice and Barcelona impose day-trip fees. Athens is exploring tourist limits, highlighting the need for a framework balancing economic beneﬁts and conservation. This work aims to create a scal- able model for sustainable tourism, addressing Juneau’s needs and oﬀering solutions for overtourism and long-term resilience.

<!-- b001192 | heading | pages [4] -->
1.2 Restatement of the Problem

<!-- b001193 | prose | pages [4] -->
To ensure the sustainable development of Juneau’s tourism industry, we aim to develop a scien- tiﬁc model and management strategies to balance the number of visitors, revenue, and resource conservation. To achieve this, we need to address the following problems:

<!-- b001194 | prose | pages [4] -->
1. Develop a model to optimize the sustainability of Juneau’s tourism industry. Clearly deﬁne the objectives to optimize (e.g., number of visitors, revenue growth) and constraints (e.g., infras- tructure capacity, environmental protection), and propose management strategies to stabilize the industry.

<!-- b001195 | prose | pages [4] -->
2. Perform sensitivity analysis to evaluate the impact of various factors in the model and identify key variables that critically inﬂuence sustainable development, enabling policymakers to adjust strategies eﬀectively.

<!-- b001196 | prose | pages [4] -->
3. Adapt the model to other tourist destinations, assess its applicability, and reﬁne it to promote less-visited attractions and improve tourism balance across diﬀerent locations.

<!-- b001197 | heading | pages [4] -->
1.3 Our Work

<!-- b001198 | prose | pages [4] -->
To address the challenges of sustainable tourism in Juneau, we propose a tourism system made up of a Sustainable Tourism Dynamics Model (STDM), an Evaluation Model and Intervention Strate- gies. The SDTM, formulated with ordinary diﬀerential equations (ODE), establishes the relationships among key variables, including environmental degradation, tourist numbers and tax revenue from tourism. The Intervention Strategies contain ﬁnite number of predeﬁned strategy combination that will inﬂuence the dynamics with the STDM. The resulting outputs from the STDM, along with the strategy combinations, are assessed through an Analytical Hierarchy Process (AHP)-based evaluation model, which will give feedback to reﬁne and optimize the strategy combination.

<!-- b001199 | prose | pages [4, 5] -->
Then, we apply the model to both Juneau and Big Sur, utilizing location speciﬁc parameters to conduct comparative analyses and predict optimal strategies for sustainable development. By applying this model, we predict the best intervention strategies and the comprehensive development of the places. In this way, we can give useful suggestions to the government. By analyzing results and doing sensitivity analysis, we have an insight of the strengths and weaknesses of the model. 关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b001200 | furniture | pages [4] -->
2

<!-- b001201 | furniture | pages [4] -->
MATHmodels

<!-- b001202 | furniture | pages [4] -->
获取更多资讯

<!-- b001203 | furniture | pages [5] -->
Team # 2503268

<!-- b001204 | furniture | pages [5] -->
Page 3 of 24

<!-- b001206 | caption | pages [5] -->
Figure 1: Pipeline of Our Model

<!-- b001207 | heading | pages [5] -->
2 Assumptions and Justiﬁcations

<!-- b001208 | prose | pages [5] -->
Through the full analysis of the problem, to simplify our model, we make the following reasonable assumptions.

<!-- b001209 | prose | pages [5] -->
• Assumption 1:Government policies are assumed to be fully implemented instantaneously.

<!-- b001210 | prose | pages [5] -->
→Justiﬁcation: In reality, the time required for policy implementation can vary depending on administrative processes, public response, and logistical challenges. However, these delays are often unpredictable and context-dependent, making them diﬃcult to generalize within a theoretical framework. By assuming instantaneous implementation, the model prioritizes the analysis of long-term systemic outcomes and policy eﬀectiveness, enabling clearer insights into the relationships between variables.

<!-- b001211 | prose | pages [5] -->
• Assumption 2: Incidents, sudden changes, minor factors and extreme situations are not taken into consideration.

<!-- b001212 | heading | pages [5] -->
→Justiﬁcation: Including these factors would greatly increase the model’s complexity without

<!-- b001213 | prose | pages [5] -->
signiﬁcantly enhancing its predictive accuracy in typical scenarios. Such events are rare, unpredictable, and context-speciﬁc, making them hard to generalize. Focusing on primary factors ensures the model remains eﬃcient, broadly applicable, and capable of capturing essential system dynamics.

<!-- b001214 | furniture | pages [6] -->
Team # 2503268

<!-- b001215 | furniture | pages [6] -->
Page 4 of 24

<!-- b001216 | prose | pages [6] -->
• Assumption 3: When determining strategies, some stable variables, are treated as con- stants. →Justiﬁcation: Stable variables like the local population show minimal short-term ﬂuctuations and have little impact on system dynamics. Treating them as constants avoids unnecessary complexity, allowing the model to focus on key drivers of change while remaining eﬃcient and easy to analyze.

<!-- b001217 | prose | pages [6] -->
• Assumption 4: The data and materials used in the model are accurate, reliable, and sourced from trusted and authoritative databases or publications.

<!-- b001218 | heading | pages [6] -->
→Justiﬁcation: The assumption of data reliability ensures consistency and avoids errors caused

<!-- b001219 | prose | pages [6] -->
by faulty or incomplete information. All data used in this model is sourced from reputable organizations, government reports, or peer-reviewed publications, which guarantees its cred- ibility and relevance.

<!-- b001220 | heading | pages [6] -->
3 Notations

<!-- b001221 | prose | pages [6] -->
Important notations used in this paper are listed below.

<!-- b001222 | caption | pages [6] -->
Table 1: Major Notations

<!-- b001223 | heading | pages [6] -->
Symbol

<!-- b001224 | prose | pages [6] -->
Description Unit HJuneau Glacier ELA height in Juneau, m NJuneau Annual number of tourists in Juneau / TJuneau Annual hotel tax revenue in Juneau $ H↑ Normalized HJuneau / Juneau N↑ Normalized NJuneau / Juneau T ↑ Normalized TJuneau / Juneau P↑ The resident population in Juneau / Juneau HS ur Height of coastal landslide loss in Pfeiﬀer Big Sur cm NS ur Annual number of tourists in Pfeiﬀer Big Sur / TS ur Annual revenue gained from tourism in Pfeiﬀer Big Sur $ H↑ Normalized HS ur / S ur N↑ Normalized NS ur / S ur T ↑ Normalized TS ur / S ur P↑ The resident population in Pfeiﬀer Big Sur / S ur S core The weighted comprehensive assessment score of the current year / S corei The weighted score considering the ith factor / S coreij The score considering the jth secondary indicator in the ith factor / Factors of disturbance in variable x % ϖx Percentage distribution of tax revenue of infrastructure, glacier protection, µ1 to µ5 % waste disposal, cultural development and police security.

<!-- b001225 | prose | pages [6] -->
关注数学模型

<!-- b001226 | furniture | pages [6] -->
2

<!-- b001227 | furniture | pages [6] -->
MATHmodels

<!-- b001228 | furniture | pages [6] -->
获取更多资讯

<!-- b001229 | furniture | pages [7] -->
Team # 2503268

<!-- b001230 | heading | pages [7] -->
Model Preparation

<!-- b001231 | prose | pages [7] -->
4

<!-- b001232 | heading | pages [7] -->
4.1 Data Collection

<!-- b001233 | furniture | pages [7] -->
Page 5 of 24

<!-- b001234 | prose | pages [7] -->
This problem lacks predefined data, requiring careful selection of data to collect before and during modeling. Key data sources are outlined in Table 2. Due to the vast and diverse data available, listing everything is impractical. Instead, we focus on accurate and representative data for effective modeling.

<!-- b001235 | caption | pages [7] -->
Table 2: Main Data Description and Source

<!-- b001236 | prose | pages [7] -->
Data Description

<!-- b001237 | prose | pages [7] -->
Annual Hotel Tax in Juneau Annual Number of Tourists in Juneau

<!-- b001238 | heading | pages [7] -->
Data Source

<!-- b001239 | prose | pages [7] -->
https://juneau.org/finance/controller https://juneau.org/wp-content/uploads/2024/02/ Juneau-Visitor-Circulator-Study-Final-Report-2024-1.pdf Annual Glacier ELA height in Juneau Juneau Tourism Management Plan https://www.nature.com/articles https://juneau.org/wp-content/Juneau-Tourism-Mgt-Plan State Park System Statistical Report California Coastal Cliff Erosion Survey https://www.parks.ca.gov https://siocpg.ucsd.edu/ca-cliff-viewer/

<!-- b001240 | prose | pages [7] -->
To minimize the influence of unknown factors and simplify the complexity of the model, we estab- lish a three-dimensional coordinate system encompassing population, environment and economy. We collect data on glacier ELA height, tourist numbers and hotel tax revenue as representative indicators for each dimension. In the following subsections, we will elaborate on the rationale behind selections.

<!-- b001241 | prose | pages [7] -->
1 Data Selection Explanation 4.2

<!-- b001242 | prose | pages [7] -->
First, from an environmental perspective, the carbon footprint is a common evaluation standard in academia. To visualize our model, we analyze its direct impact on the Equilibrium Line Altitude (ELA)—the glacier elevation where annual snow accumulation equals annual melt, separating the accumulation and ablation zones. The process is shown in the figure below.

<!-- b001243 | prose | pages [7] -->
Snow Equilibriu line

<!-- b001244 | prose | pages [7] -->
Sublimation Calving Iceberg Zone of ablation Zone of accumulation

<!-- b001245 | prose | pages [7, 8] -->
Flow trajectory Meltwater pool on glacier Terminus (toe) Meltwater Meltwater tunnel stream Secondly, considering that the number of tourists far exceeds the local resident population, and given the distinct impacts these two groups have on the environment and economy, the local population can be considered negligible in the population dimension. This makes it reasonable to use tourist numbers as a representative indicator for the population metric. According to the most recent Juneau Tourism Survey, hotel revenue consistently accounts for a stable proportion of the total government revenue. Therefore, we use hotel tax revenue as an indicator to represent the economic dimension.

<!-- b001246 | caption | pages [7] -->
Figure 2: Construction Process of ELA

<!-- b001247 | furniture | pages [8] -->
Team # 2503268

<!-- b001248 | furniture | pages [8] -->
Page 6 of 24

<!-- b001250 | heading | pages [8] -->
5 Model Design

<!-- b001251 | heading | pages [8] -->
5.1 Sustainable Tourism Dynamics Model (STDM)

<!-- b001252 | prose | pages [8] -->
Natural environments, economic factors, and population dynamics are deeply interconnected. This study aims to represent the dynamics between glacier ELA height, annual number of tourists, and annual hotel tax revenue using fundamental data. Such a model provides an essential explanatory m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m framework for understanding the logical relationships between these factors, laying the foundation for m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m more detailed analysis and decision-making in subsequent sections. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001253 | heading | pages [8] -->
5.1.1 Glacier ELA Height Dynamics

<!-- b001254 | prose | pages [8] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m One critical aspect of glacier health is the Equilibrium Line Altitude (ELA), which represents the altitude on a glacier where accumulation and ablation are balanced. According to the study by Braithwaite et al. [1], changes in ELA are driven primarily by temperature and precipitation. As the ELA rises, it reﬂects increased glacier melting and reduced stability. Similarly, another study by Oerlemans [2] highlights that ELA is a key indicator of glacier health and is directly aﬀected by climatic variations.

<!-- b001255 | prose | pages [8] -->
The ELA is inﬂuenced by feedback mechanisms within the glacier itself. For instance, the albedo eﬀect causes melting glaciers to absorb more solar radiation as their surface darkens, further acceler- ating the loss of ice. This intrinsic dependency makes the ELA height of glacier HJuneau sensitive to its prior state, represented in the model by k1HJuneau.

<!-- b001256 | prose | pages [8] -->
Tourism signiﬁcantly aﬀects glacier health. Increased tourist numbers NJuneau can lead to en- vironmental degradation through waste, infrastructure development, and direct interaction with the glacier environment. These impacts are proportional to both the existing glacier health and the level of tourism, captured in the term k2HJuneauNJuneau.

<!-- b001257 | prose | pages [8] -->
Economic factors, such as investments in preservation funded by hotel tax revenue TJuneau, also play a vital role in mitigating the negative eﬀects of tourism. Higher revenues enable conservation projects, such as restricting access to sensitive areas or implementing restoration eﬀorts. This dynamic is mod- eled as k3TJuneauHJuneau, showing how economic resources contribute to sustaining glacier health.

<!-- b001258 | prose | pages [8] -->
Bringing these factors together, the equation governing glacier health HJuneau is expressed as:

<!-- b001259 | prose | pages [8] -->
dHJuneau = k1HJuneau + k2HJuneauNJuneau + k3TJuneauHJuneau. (1) dt

<!-- b001260 | prose | pages [8] -->
Here, k1 represents the intrinsic changes in glacier health due to natural processes, k2 quantiﬁes the impact of tourism, and k3 captures the restorative eﬀects of economic investments.

<!-- b001261 | prose | pages [8] -->
关注数学模型

<!-- b001262 | furniture | pages [8] -->
2

<!-- b001263 | furniture | pages [8] -->
MATHmodels

<!-- b001264 | furniture | pages [8] -->
获取更多资讯

<!-- b001265 | furniture | pages [9] -->
Team # 2503268

<!-- b001266 | furniture | pages [9] -->
Page 7 of 24

<!-- b001267 | heading | pages [9] -->
5.1.2 Tourist Number Dynamics

<!-- b001268 | prose | pages [9] -->
The dynamics of tourist numbers NJuneau are governed by both natural growth patterns and their in- teraction with the glacier environment. According to Verhulst’s logistic model [3], population growth typically follows an S-shaped curve, with initial exponential growth slowing as it approaches the car- ! " 微信公众号：数学模型 1 ↓NJuneau rying capacity K. This relationship is represented by the term r1NJuneau , where r1 is the K intrinsic growth rate and K is the environmental or infrastructural limit for tourist numbers.

<!-- b001269 | prose | pages [9] -->
The health of the glacier environment HJuneau also plays a critical role in attracting tourists. Re- search by Buckley [4] shows that pristine natural environments signiﬁcantly boost tourism demand. This inﬂuence is captured by the term k4HJuneauNJuneau, which indicates that better glacier health am- pliﬁes tourist numbers.

<!-- b001270 | prose | pages [9] -->
Combining these factors, the equation for tourist numbers NJuneau is expressed as:

<!-- b001271 | prose | pages [9] -->
# $ dNJuneau 1 ↓NJuneau = r1NJuneau + k4HJuneauNJuneau. (2) dt K 微信号：MATHmodels Here, r1 represents the natural growth rate of tourism, constrained by the carrying capacity K, while k4 quantiﬁes the positive impact of glacier health HJuneau on tourism growth. Together, these terms de- scribe the interplay between environmental conditions and tourism dynamics, providing a framework to assess the sustainability of tourism in glacier regions.

<!-- b001272 | heading | pages [9] -->
5.1.3 Economic Dynamics

<!-- b001273 | prose | pages [9] -->
The dynamics of annual hotel tax revenue TJuneau are closely tied to tourism and economic factors. According to studies on tourism-driven economies [5], the revenue generated from hotel taxes is di- rectly proportional to the number of tourists. This relationship is captured by the term k6NJuneau, which indicates that an increase in tourist numbers NJuneau results in higher tax revenue.

<!-- b001274 | prose | pages [9] -->
In addition, economic growth independent of tourism also plays a role. Research by Frechtling [6] shows that baseline economic trends contribute to steady growth in tax revenue, even in the absence of signiﬁcant changes in tourism. This baseline growth is represented by the term k5TJuneau, which accounts for general economic development and inﬂationary factors.

<!-- b001275 | prose | pages [9] -->
Combining these inﬂuences, the equation for hotel tax revenue TJuneau is expressed as:

<!-- b001276 | prose | pages [9] -->
dTJuneau = k5TJuneau + k6NJuneau. (3) dt Here, k5 represents the baseline economic growth, while k6 quantiﬁes the direct contribution of tourist numbers NJuneau to tax revenue.

<!-- b001277 | heading | pages [9] -->
5.1.4 Model Integration and Parameter Estimation

<!-- b001278 | prose | pages [9, 10] -->
To evaluate the interconnected dynamics of glacier health, tourist numbers, and hotel tax revenue, we integrate the above equations into a single system. Using data from 2010 to 2019, we estimate the parameters ki and ri through nonlinear regression. Due to the complexity of real-world systems, these parameters are inﬂuenced not only by the core variables but also by external, unmeasured factors. Speciﬁcally, the anomalous marine heatwave event known as “The Blob” in 2013 signiﬁcantly aﬀected m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m glacier data for that year. To address this, we excluded the 2013 data from the analysis and performed interpolation on the remaining years to ensure consistency. The adjusted dataset was then used to ﬁt the equations and estimate ki and ri.

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

<!-- b001425 | furniture | pages [9] -->
m

<!-- b001426 | furniture | pages [9] -->
m

<!-- b001427 | furniture | pages [9] -->
m

<!-- b001428 | furniture | pages [9] -->
m

<!-- b001429 | furniture | pages [9] -->
m

<!-- b001430 | furniture | pages [9] -->
m

<!-- b001431 | furniture | pages [9] -->
m

<!-- b001432 | furniture | pages [9] -->
m

<!-- b001433 | furniture | pages [9] -->
m

<!-- b001434 | furniture | pages [9] -->
m

<!-- b001435 | furniture | pages [9] -->
m

<!-- b001436 | furniture | pages [9] -->
m

<!-- b001437 | furniture | pages [9] -->
m

<!-- b001438 | furniture | pages [9] -->
m

<!-- b001439 | furniture | pages [9] -->
m

<!-- b001440 | furniture | pages [9] -->
m

<!-- b001441 | furniture | pages [9] -->
m

<!-- b001442 | furniture | pages [9] -->
m

<!-- b001443 | furniture | pages [9] -->
m

<!-- b001444 | furniture | pages [9] -->
m

<!-- b001445 | furniture | pages [9] -->
m

<!-- b001446 | furniture | pages [9] -->
m

<!-- b001447 | furniture | pages [9] -->
m

<!-- b001448 | furniture | pages [9] -->
m

<!-- b001449 | furniture | pages [9] -->
m

<!-- b001450 | furniture | pages [9] -->
m

<!-- b001451 | furniture | pages [9] -->
m

<!-- b001452 | furniture | pages [9] -->
m

<!-- b001453 | furniture | pages [9] -->
m

<!-- b001454 | furniture | pages [9] -->
m

<!-- b001455 | furniture | pages [9] -->
m

<!-- b001456 | furniture | pages [9] -->
m

<!-- b001457 | furniture | pages [9] -->
m

<!-- b001458 | furniture | pages [9] -->
m

<!-- b001459 | furniture | pages [9] -->
m

<!-- b001460 | furniture | pages [9] -->
m

<!-- b001461 | furniture | pages [9] -->
m

<!-- b001462 | furniture | pages [9] -->
m

<!-- b001463 | furniture | pages [9] -->
m

<!-- b001464 | furniture | pages [9] -->
m

<!-- b001465 | furniture | pages [9] -->
m

<!-- b001466 | furniture | pages [9] -->
m

<!-- b001467 | furniture | pages [9] -->
m

<!-- b001468 | furniture | pages [9] -->
m

<!-- b001469 | furniture | pages [9] -->
m

<!-- b001470 | furniture | pages [9] -->
m

<!-- b001471 | furniture | pages [9] -->
m

<!-- b001472 | furniture | pages [9] -->
m

<!-- b001473 | furniture | pages [9] -->
m

<!-- b001474 | furniture | pages [9] -->
m

<!-- b001475 | furniture | pages [9] -->
m

<!-- b001476 | furniture | pages [9] -->
m

<!-- b001477 | furniture | pages [9] -->
m

<!-- b001478 | furniture | pages [9] -->
m

<!-- b001479 | furniture | pages [9] -->
m

<!-- b001480 | furniture | pages [9] -->
m

<!-- b001481 | furniture | pages [9] -->
m

<!-- b001482 | furniture | pages [9] -->
m

<!-- b001483 | furniture | pages [9] -->
m

<!-- b001484 | furniture | pages [9] -->
m

<!-- b001485 | furniture | pages [9] -->
m

<!-- b001486 | furniture | pages [9] -->
m

<!-- b001487 | furniture | pages [9] -->
m

<!-- b001488 | furniture | pages [9] -->
m

<!-- b001489 | furniture | pages [9] -->
m

<!-- b001490 | furniture | pages [9] -->
m

<!-- b001491 | furniture | pages [9] -->
m

<!-- b001492 | furniture | pages [9] -->
m

<!-- b001493 | furniture | pages [9] -->
m

<!-- b001494 | furniture | pages [9] -->
m

<!-- b001495 | furniture | pages [9] -->
m

<!-- b001496 | furniture | pages [9] -->
m

<!-- b001497 | furniture | pages [9] -->
m

<!-- b001498 | furniture | pages [9] -->
m

<!-- b001499 | furniture | pages [9] -->
m

<!-- b001500 | furniture | pages [9] -->
m

<!-- b001501 | furniture | pages [9] -->
m

<!-- b001502 | furniture | pages [9] -->
m

<!-- b001503 | furniture | pages [9] -->
m

<!-- b001504 | furniture | pages [9] -->
m

<!-- b001505 | furniture | pages [9] -->
m

<!-- b001506 | furniture | pages [9] -->
m

<!-- b001507 | furniture | pages [9] -->
m

<!-- b001508 | furniture | pages [9] -->
m

<!-- b001509 | furniture | pages [9] -->
m

<!-- b001510 | furniture | pages [9] -->
m

<!-- b001511 | furniture | pages [9] -->
m

<!-- b001512 | furniture | pages [9] -->
m

<!-- b001513 | furniture | pages [9] -->
m

<!-- b001514 | furniture | pages [9] -->
m

<!-- b001515 | furniture | pages [9] -->
m

<!-- b001516 | furniture | pages [9] -->
m

<!-- b001517 | furniture | pages [9] -->
m

<!-- b001518 | furniture | pages [9] -->
m

<!-- b001519 | furniture | pages [9] -->
m

<!-- b001520 | furniture | pages [9] -->
m

<!-- b001521 | furniture | pages [9] -->
m

<!-- b001522 | furniture | pages [9] -->
m

<!-- b001523 | furniture | pages [9] -->
m

<!-- b001524 | furniture | pages [9] -->
m

<!-- b001525 | furniture | pages [9] -->
m

<!-- b001526 | furniture | pages [9] -->
m

<!-- b001527 | furniture | pages [9] -->
m

<!-- b001528 | furniture | pages [9] -->
m

<!-- b001529 | furniture | pages [9] -->
m

<!-- b001530 | furniture | pages [9] -->
m

<!-- b001531 | furniture | pages [9] -->
m

<!-- b001532 | furniture | pages [9] -->
m

<!-- b001533 | furniture | pages [9] -->
m

<!-- b001534 | furniture | pages [9] -->
m

<!-- b001535 | furniture | pages [9] -->
m

<!-- b001536 | furniture | pages [9] -->
m

<!-- b001537 | furniture | pages [9] -->
m

<!-- b001538 | furniture | pages [9] -->
m

<!-- b001539 | furniture | pages [9] -->
m

<!-- b001540 | furniture | pages [9] -->
m

<!-- b001541 | furniture | pages [9] -->
m

<!-- b001542 | furniture | pages [9] -->
m

<!-- b001543 | furniture | pages [9] -->
m

<!-- b001544 | furniture | pages [9] -->
m

<!-- b001545 | furniture | pages [9] -->
m

<!-- b001546 | furniture | pages [9] -->
m

<!-- b001547 | furniture | pages [9] -->
m

<!-- b001548 | furniture | pages [9] -->
m

<!-- b001549 | furniture | pages [9] -->
m

<!-- b001550 | furniture | pages [9] -->
m

<!-- b001551 | furniture | pages [9] -->
m

<!-- b001552 | furniture | pages [9] -->
m

<!-- b001553 | furniture | pages [9] -->
m

<!-- b001554 | furniture | pages [9] -->
m

<!-- b001555 | furniture | pages [9] -->
m

<!-- b001556 | furniture | pages [9] -->
m

<!-- b001557 | furniture | pages [9] -->
m

<!-- b001558 | furniture | pages [9] -->
m

<!-- b001559 | furniture | pages [9] -->
m

<!-- b001560 | furniture | pages [9] -->
m

<!-- b001561 | furniture | pages [9] -->
m

<!-- b001562 | furniture | pages [9] -->
m

<!-- b001563 | furniture | pages [9] -->
m

<!-- b001564 | furniture | pages [9] -->
m

<!-- b001565 | furniture | pages [9] -->
m

<!-- b001566 | furniture | pages [9] -->
m

<!-- b001567 | furniture | pages [9] -->
m

<!-- b001568 | furniture | pages [9] -->
m

<!-- b001569 | furniture | pages [9] -->
m

<!-- b001570 | furniture | pages [9] -->
m

<!-- b001571 | furniture | pages [9] -->
m

<!-- b001572 | furniture | pages [9] -->
m

<!-- b001573 | furniture | pages [9] -->
m

<!-- b001574 | furniture | pages [9] -->
m

<!-- b001575 | furniture | pages [9] -->
m

<!-- b001576 | furniture | pages [9] -->
m

<!-- b001577 | furniture | pages [9] -->
m

<!-- b001578 | furniture | pages [9] -->
m

<!-- b001579 | furniture | pages [9] -->
m

<!-- b001580 | furniture | pages [9] -->
m

<!-- b001581 | furniture | pages [9] -->
m

<!-- b001582 | furniture | pages [9] -->
m

<!-- b001583 | furniture | pages [9] -->
m

<!-- b001584 | furniture | pages [9] -->
m

<!-- b001585 | furniture | pages [9] -->
m

<!-- b001586 | furniture | pages [9] -->
m

<!-- b001587 | furniture | pages [9] -->
m

<!-- b001588 | furniture | pages [9] -->
m

<!-- b001589 | furniture | pages [9] -->
m

<!-- b001590 | furniture | pages [9] -->
m

<!-- b001591 | furniture | pages [9] -->
m

<!-- b001592 | furniture | pages [9] -->
m

<!-- b001593 | furniture | pages [9] -->
m

<!-- b001594 | furniture | pages [9] -->
m

<!-- b001595 | furniture | pages [9] -->
m

<!-- b001596 | furniture | pages [9] -->
m

<!-- b001597 | furniture | pages [9] -->
m

<!-- b001598 | furniture | pages [9] -->
m

<!-- b001599 | furniture | pages [9] -->
m

<!-- b001600 | furniture | pages [9] -->
m

<!-- b001601 | furniture | pages [9] -->
m

<!-- b001602 | furniture | pages [9] -->
m

<!-- b001603 | furniture | pages [10] -->
Team # 2503268

<!-- b001604 | furniture | pages [10] -->
Page 8 of 24

<!-- b001606 | prose | pages [10] -->
The ﬁnal integrated system of equations, including ϖ, is expressed as:

<!-- b001607 | prose | pages [10] -->
dHJuneau = k1HJuneau + k2HJuneauNJuneau + k3TJuneauHJuneau + ϖHJuneau, (4) dt # $ dNJuneau 1 ↓NJuneau = r1NJuneau + k4HJuneauNJuneau + ϖNJuneau, (5) dt K dTJuneau = k5TJuneau + k6NJuneau + ϖTJuneau. (6) dt

<!-- b001608 | caption | pages [10] -->
Figure 3: System 3D schematic with projection

<!-- b001609 | caption | pages [10] -->
Figure 4: Respective projections

<!-- b001610 | prose | pages [10, 11] -->
关注数学模型 The ﬁtting results and the corresponding parameter values are visualized in Figure3, and the ac- curacy of the model is validated using historical data. Using data from 2010 to 2019, we performed parameter ﬁtting for the integrated model equations. The resulting parameter values were derived through nonlinear regression, incorporating the error terms ϖHJuneau, ϖNJuneau, and ϖTJuneau to account for external unmeasured inﬂuences.

<!-- b001611 | furniture | pages [10] -->
2

<!-- b001612 | furniture | pages [10] -->
MATHmodels

<!-- b001613 | furniture | pages [10] -->
获取更多资讯

<!-- b001614 | furniture | pages [11] -->
Team # 2503268

<!-- b001615 | furniture | pages [11] -->
Page 9 of 24

<!-- b001617 | caption | pages [11] -->
Figure3 illustrates the observed data and the trajectories generated by the model in a 3D space,

<!-- b001618 | prose | pages [11] -->
showing the dynamic interactions between glacier health HJuneau, tourist numbers NJuneau, and hotel 微信公众号：数学模型 tax revenue TJuneau. The ﬁtted trajectories closely align with the observed data points, suggesting that the model captures the essential dynamics of the system.

<!-- b001619 | prose | pages [11] -->
Additionally, Figure3 displays the feasible regions in the (HJuneau, NJuneau), (HJuneau, TJuneau), and (NJuneau, TJuneau) planes. These regions represent the range of plausible model outcomes given the ﬁtted parameters. The observed data points (red stars) fall predominantly within these feasible regions, further validating the model’s predictive accuracy.

<!-- b001620 | prose | pages [11] -->
The results highlight several key insights:

<!-- b001621 | prose | pages [11] -->
1. The positive correlation between the ELA height of the glacier HJuneau and the tourist numbers NJuneau is evident in the trajectories, supporting the hypothesis that an increase in visitors nega- 微信号：MATHmodels tively impacts the environment, thereby causing the ELA height to rise.

<!-- b001622 | prose | pages [11] -->
2. Annual hotel tax revenue TJuneau shows a direct dependency on tourist numbers NJuneau, as indi- cated by the tight clustering of observed data along the model trajectories in the (NJuneau, TJuneau) plane.

<!-- b001623 | prose | pages [11] -->
3. Variability in the system, represented by the error terms ϖ, likely captures external factors such as climatic anomalies or economic shocks, which are not directly modeled but are essential for explaining deviations.

<!-- b001624 | prose | pages [11] -->
These ﬁtting results provide a robust foundation for analyzing the dynamic interplay among nat- ural, social, and economic factors, and they oﬀer valuable insights for policy-making and resource management in glacier regions.

<!-- b001625 | heading | pages [11] -->
5.2 Intervention Strategies

<!-- b001626 | heading | pages [11] -->
5.2.1 Intervention Impact on Models

<!-- b001627 | prose | pages [11] -->
To maintain a balance between the three variables when maximizing utility, we categorize our intervention strategies into two components: tax revenue allocation and policies. Each component features a ﬁnite set of typical and representative solutions. By iterating through these solutions, we obtain a ﬁnite set of potential strategy combinations.

<!-- b001628 | prose | pages [11] -->
Given the current values of HJuneau, NJuneau, and TJuneau, each combination, under the given con- straints, produces new HJuneau, NJuneau, and TJuneau values along with corresponding scores. We then select the combination with the highest score to serve as the current intervention strategy, and update HJuneau, NJuneau, and TJuneau accordingly to these new values.

<!-- b001629 | furniture | pages [12] -->
Team # 2503268

<!-- b001630 | furniture | pages [12] -->
Page 10 of 24

<!-- b001631 | heading | pages [12] -->
5.2.2 Tax Revenue Allocation

<!-- b001632 | prose | pages [12] -->
The variables µ1, µ2, µ3, µ4, µ5 are inputs to the evaluation model. We modeled nine representative arrays [µ1, µ2, µ3, µ4, µ5] based on diﬀerent allocation patterns, which are displayed in the ﬁgure below.

<!-- b001633 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001634 | caption | pages [12] -->
Figure 5: Allocations

<!-- b001635 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001636 | heading | pages [12] -->
5.2.3 Policies

<!-- b001637 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We design 8 policies with diﬀerent focuses and assign diﬀerent vectors v1, v2, v3 to each policy. The vector satisﬁes ↓v1 + v2 + v3 = 10 as 10 is the sum assigned to the policies but H is a negative indicator. The detailed 8 policies are as follows:

<!-- b001638 | prose | pages [12] -->
Policy Description Vector Promote local business development [0, 0, 10] Comprehensive and balanced development [↓3, 3, 4] Develop infrastructure [↓4, 4, 2] Market promotion and brand building [0, 4, 6] Direct measures to attract tourists [↓2, 8, 0] Improve tourist experience [0, 8, 2] Natural resource conservation [↓13, 0, ↓3], [↓14, ↓2, ↓2]

<!-- b001639 | caption | pages [12] -->
Table 3: Indicators Selected

<!-- b001640 | caption | pages [12] -->
Figure 6 displays the way how policies impact the system. We use the output of the evaluation

<!-- b001641 | prose | pages [12] -->
model to decide the policies too.

<!-- b001642 | heading | pages [12] -->
6 Evaluation Model

<!-- b001643 | heading | pages [12] -->
6.1 Indicators Determination

<!-- b001644 | prose | pages [12] -->
Based on the statement of the question and the literature, the degree of comprehensive devel- opment in the City of Juneau can be mainly categorized into three factors, which are life of local

<!-- b001645 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型

<!-- b001646 | furniture | pages [12] -->
2

<!-- b001647 | furniture | pages [12] -->
MATHmodels

<!-- b001648 | furniture | pages [12] -->
获取更多资讯

<!-- b001649 | furniture | pages [13] -->
Team # 2503268

<!-- b001650 | furniture | pages [13] -->
Page 11 of 24

<!-- b001652 | caption | pages [13] -->
Figure 6: policy impact on system

<!-- b001653 | prose | pages [13] -->
residents(LoR), local environmental protection(EP), along with local economy and development of society(EDoS). 微信号：MATHmodels In consideration of tourism impact, We have overall listed 29 secondary indicators that are related to the three main factors, and picked 4 most signiﬁcant secondary indicators for each main factor. The main factors and related secondary indicators are listed below.

<!-- b001654 | prose | pages [13] -->
Factor Indicator Score No- tation LoR the increase of average individual income S 11 crowding level S 12 housing aﬀordability S 13 noise level S 14 EP natural resources like glacier coverage S 21 water and energy usage S 22 waste production level S 23 carbon footprint S 24 EDoS tourism tax revenue S 31 employment growth S 32 cultural resource protection or utilization S 33 social safety or security index S 34

<!-- b001655 | caption | pages [13] -->
Table 4: Indicators Selected

<!-- b001656 | heading | pages [13] -->
6.2 Score Calculation Model

<!-- b001657 | prose | pages [13, 14] -->
Here, P = 31685. Here we use the Analytic Hierarchy Process(AHP). AHP assigns weights to criteria through pairwise comparisons, checks the consistency of these comparisons, and calculates an overall score by aggregating the weighted scores, which is displayed in the formulas below. S core1, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m S core2 and S core3 are scores computed from secondary scores, and the ﬁnal S core is the overall sum. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001658 | furniture | pages [13] -->
m

<!-- b001659 | furniture | pages [13] -->
m

<!-- b001660 | furniture | pages [13] -->
m

<!-- b001661 | furniture | pages [13] -->
m

<!-- b001662 | furniture | pages [13] -->
m

<!-- b001663 | furniture | pages [13] -->
m

<!-- b001664 | furniture | pages [13] -->
m

<!-- b001665 | furniture | pages [13] -->
m

<!-- b001666 | furniture | pages [13] -->
m

<!-- b001667 | furniture | pages [13] -->
m

<!-- b001668 | furniture | pages [13] -->
m

<!-- b001669 | furniture | pages [13] -->
m

<!-- b001670 | furniture | pages [13] -->
m

<!-- b001671 | furniture | pages [13] -->
m

<!-- b001672 | furniture | pages [13] -->
m

<!-- b001673 | furniture | pages [13] -->
m

<!-- b001674 | furniture | pages [13] -->
m

<!-- b001675 | furniture | pages [13] -->
m

<!-- b001676 | furniture | pages [13] -->
m

<!-- b001677 | furniture | pages [13] -->
m

<!-- b001678 | furniture | pages [13] -->
m

<!-- b001679 | furniture | pages [13] -->
m

<!-- b001680 | furniture | pages [13] -->
m

<!-- b001681 | furniture | pages [13] -->
m

<!-- b001682 | furniture | pages [13] -->
m

<!-- b001683 | furniture | pages [13] -->
m

<!-- b001684 | furniture | pages [13] -->
m

<!-- b001685 | furniture | pages [13] -->
m

<!-- b001686 | furniture | pages [13] -->
m

<!-- b001687 | furniture | pages [13] -->
m

<!-- b001688 | furniture | pages [13] -->
m

<!-- b001689 | furniture | pages [13] -->
m

<!-- b001690 | furniture | pages [13] -->
m

<!-- b001691 | furniture | pages [13] -->
m

<!-- b001692 | furniture | pages [13] -->
m

<!-- b001693 | furniture | pages [13] -->
m

<!-- b001694 | furniture | pages [13] -->
m

<!-- b001695 | furniture | pages [13] -->
m

<!-- b001696 | furniture | pages [13] -->
m

<!-- b001697 | furniture | pages [13] -->
m

<!-- b001698 | furniture | pages [13] -->
m

<!-- b001699 | furniture | pages [13] -->
m

<!-- b001700 | furniture | pages [13] -->
m

<!-- b001701 | furniture | pages [13] -->
m

<!-- b001702 | furniture | pages [13] -->
m

<!-- b001703 | furniture | pages [13] -->
m

<!-- b001704 | furniture | pages [13] -->
m

<!-- b001705 | furniture | pages [13] -->
m

<!-- b001706 | furniture | pages [13] -->
m

<!-- b001707 | furniture | pages [13] -->
m

<!-- b001708 | furniture | pages [13] -->
m

<!-- b001709 | furniture | pages [13] -->
m

<!-- b001710 | furniture | pages [13] -->
m

<!-- b001711 | furniture | pages [13] -->
m

<!-- b001712 | furniture | pages [13] -->
m

<!-- b001713 | furniture | pages [13] -->
m

<!-- b001714 | furniture | pages [13] -->
m

<!-- b001715 | furniture | pages [13] -->
m

<!-- b001716 | furniture | pages [13] -->
m

<!-- b001717 | furniture | pages [13] -->
m

<!-- b001718 | furniture | pages [13] -->
m

<!-- b001719 | furniture | pages [13] -->
m

<!-- b001720 | furniture | pages [13] -->
m

<!-- b001721 | furniture | pages [13] -->
m

<!-- b001722 | furniture | pages [13] -->
m

<!-- b001723 | furniture | pages [13] -->
m

<!-- b001724 | furniture | pages [13] -->
m

<!-- b001725 | furniture | pages [13] -->
m

<!-- b001726 | furniture | pages [13] -->
m

<!-- b001727 | furniture | pages [13] -->
m

<!-- b001728 | furniture | pages [13] -->
m

<!-- b001729 | furniture | pages [13] -->
m

<!-- b001730 | furniture | pages [13] -->
m

<!-- b001731 | furniture | pages [13] -->
m

<!-- b001732 | furniture | pages [13] -->
m

<!-- b001733 | furniture | pages [13] -->
m

<!-- b001734 | furniture | pages [13] -->
m

<!-- b001735 | furniture | pages [13] -->
m

<!-- b001736 | furniture | pages [13] -->
m

<!-- b001737 | furniture | pages [13] -->
m

<!-- b001738 | furniture | pages [13] -->
m

<!-- b001739 | furniture | pages [13] -->
m

<!-- b001740 | furniture | pages [13] -->
m

<!-- b001741 | furniture | pages [13] -->
m

<!-- b001742 | furniture | pages [13] -->
m

<!-- b001743 | furniture | pages [13] -->
m

<!-- b001744 | furniture | pages [13] -->
m

<!-- b001745 | furniture | pages [13] -->
m

<!-- b001746 | furniture | pages [13] -->
m

<!-- b001747 | furniture | pages [13] -->
m

<!-- b001748 | furniture | pages [13] -->
m

<!-- b001749 | furniture | pages [13] -->
m

<!-- b001750 | furniture | pages [13] -->
m

<!-- b001751 | furniture | pages [13] -->
m

<!-- b001752 | furniture | pages [13] -->
m

<!-- b001753 | furniture | pages [13] -->
m

<!-- b001754 | furniture | pages [13] -->
m

<!-- b001755 | furniture | pages [13] -->
m

<!-- b001756 | furniture | pages [13] -->
m

<!-- b001757 | furniture | pages [13] -->
m

<!-- b001758 | furniture | pages [13] -->
m

<!-- b001759 | furniture | pages [13] -->
m

<!-- b001760 | furniture | pages [13] -->
m

<!-- b001761 | furniture | pages [13] -->
m

<!-- b001762 | furniture | pages [13] -->
m

<!-- b001763 | furniture | pages [13] -->
m

<!-- b001764 | furniture | pages [13] -->
m

<!-- b001765 | furniture | pages [13] -->
m

<!-- b001766 | furniture | pages [13] -->
m

<!-- b001767 | furniture | pages [13] -->
m

<!-- b001768 | furniture | pages [13] -->
m

<!-- b001769 | furniture | pages [13] -->
m

<!-- b001770 | furniture | pages [13] -->
m

<!-- b001771 | furniture | pages [13] -->
m

<!-- b001772 | furniture | pages [13] -->
m

<!-- b001773 | furniture | pages [13] -->
m

<!-- b001774 | furniture | pages [13] -->
m

<!-- b001775 | furniture | pages [13] -->
m

<!-- b001776 | furniture | pages [13] -->
m

<!-- b001777 | furniture | pages [13] -->
m

<!-- b001778 | furniture | pages [13] -->
m

<!-- b001779 | furniture | pages [13] -->
m

<!-- b001780 | furniture | pages [13] -->
m

<!-- b001781 | furniture | pages [13] -->
m

<!-- b001782 | furniture | pages [13] -->
m

<!-- b001783 | furniture | pages [13] -->
m

<!-- b001784 | furniture | pages [13] -->
m

<!-- b001785 | furniture | pages [13] -->
m

<!-- b001786 | furniture | pages [13] -->
m

<!-- b001787 | furniture | pages [13] -->
m

<!-- b001788 | furniture | pages [13] -->
m

<!-- b001789 | furniture | pages [13] -->
m

<!-- b001790 | furniture | pages [13] -->
m

<!-- b001791 | furniture | pages [13] -->
m

<!-- b001792 | furniture | pages [13] -->
m

<!-- b001793 | furniture | pages [13] -->
m

<!-- b001794 | furniture | pages [13] -->
m

<!-- b001795 | furniture | pages [13] -->
m

<!-- b001796 | furniture | pages [13] -->
m

<!-- b001797 | furniture | pages [13] -->
m

<!-- b001798 | furniture | pages [13] -->
m

<!-- b001799 | furniture | pages [13] -->
m

<!-- b001800 | furniture | pages [13] -->
m

<!-- b001801 | furniture | pages [13] -->
m

<!-- b001802 | furniture | pages [13] -->
m

<!-- b001803 | furniture | pages [13] -->
m

<!-- b001804 | furniture | pages [13] -->
m

<!-- b001805 | furniture | pages [13] -->
m

<!-- b001806 | furniture | pages [13] -->
m

<!-- b001807 | furniture | pages [13] -->
m

<!-- b001808 | furniture | pages [13] -->
m

<!-- b001809 | furniture | pages [13] -->
m

<!-- b001810 | furniture | pages [13] -->
m

<!-- b001811 | furniture | pages [13] -->
m

<!-- b001812 | furniture | pages [13] -->
m

<!-- b001813 | furniture | pages [13] -->
m

<!-- b001814 | furniture | pages [13] -->
m

<!-- b001815 | furniture | pages [13] -->
m

<!-- b001816 | furniture | pages [13] -->
m

<!-- b001817 | furniture | pages [13] -->
m

<!-- b001818 | furniture | pages [13] -->
m

<!-- b001819 | furniture | pages [13] -->
m

<!-- b001820 | furniture | pages [13] -->
m

<!-- b001821 | furniture | pages [13] -->
m

<!-- b001822 | furniture | pages [13] -->
m

<!-- b001823 | furniture | pages [13] -->
m

<!-- b001824 | furniture | pages [13] -->
m

<!-- b001825 | furniture | pages [13] -->
m

<!-- b001826 | furniture | pages [13] -->
m

<!-- b001827 | furniture | pages [13] -->
m

<!-- b001828 | furniture | pages [13] -->
m

<!-- b001829 | furniture | pages [13] -->
m

<!-- b001830 | furniture | pages [13] -->
m

<!-- b001831 | furniture | pages [13] -->
m

<!-- b001832 | furniture | pages [13] -->
m

<!-- b001833 | furniture | pages [13] -->
m

<!-- b001834 | furniture | pages [13] -->
m

<!-- b001835 | furniture | pages [13] -->
m

<!-- b001836 | furniture | pages [13] -->
m

<!-- b001837 | furniture | pages [13] -->
m

<!-- b001838 | furniture | pages [13] -->
m

<!-- b001839 | furniture | pages [13] -->
m

<!-- b001840 | furniture | pages [13] -->
m

<!-- b001841 | furniture | pages [13] -->
m

<!-- b001842 | furniture | pages [13] -->
m

<!-- b001843 | furniture | pages [13] -->
m

<!-- b001844 | furniture | pages [13] -->
m

<!-- b001845 | furniture | pages [13] -->
m

<!-- b001846 | furniture | pages [13] -->
m

<!-- b001847 | furniture | pages [13] -->
m

<!-- b001848 | furniture | pages [13] -->
m

<!-- b001849 | furniture | pages [13] -->
m

<!-- b001850 | furniture | pages [13] -->
m

<!-- b001851 | furniture | pages [13] -->
m

<!-- b001852 | furniture | pages [13] -->
m

<!-- b001853 | furniture | pages [13] -->
m

<!-- b001854 | furniture | pages [13] -->
m

<!-- b001855 | furniture | pages [13] -->
m

<!-- b001856 | furniture | pages [13] -->
m

<!-- b001857 | furniture | pages [13] -->
m

<!-- b001858 | furniture | pages [13] -->
m

<!-- b001859 | furniture | pages [13] -->
m

<!-- b001860 | furniture | pages [13] -->
m

<!-- b001861 | furniture | pages [13] -->
m

<!-- b001862 | furniture | pages [13] -->
m

<!-- b001863 | furniture | pages [13] -->
m

<!-- b001864 | furniture | pages [13] -->
m

<!-- b001865 | furniture | pages [13] -->
m

<!-- b001866 | furniture | pages [13] -->
m

<!-- b001867 | furniture | pages [13] -->
m

<!-- b001868 | furniture | pages [13] -->
m

<!-- b001869 | furniture | pages [13] -->
m

<!-- b001870 | furniture | pages [13] -->
m

<!-- b001871 | furniture | pages [13] -->
m

<!-- b001872 | furniture | pages [13] -->
m

<!-- b001873 | furniture | pages [13] -->
m

<!-- b001874 | furniture | pages [13] -->
m

<!-- b001875 | furniture | pages [13] -->
m

<!-- b001876 | furniture | pages [13] -->
m

<!-- b001877 | furniture | pages [13] -->
m

<!-- b001878 | furniture | pages [13] -->
m

<!-- b001879 | furniture | pages [13] -->
m

<!-- b001880 | furniture | pages [13] -->
m

<!-- b001881 | furniture | pages [13] -->
m

<!-- b001882 | furniture | pages [13] -->
m

<!-- b001883 | furniture | pages [13] -->
m

<!-- b001884 | furniture | pages [13] -->
m

<!-- b001885 | furniture | pages [13] -->
m

<!-- b001886 | furniture | pages [13] -->
m

<!-- b001887 | furniture | pages [13] -->
m

<!-- b001888 | furniture | pages [13] -->
m

<!-- b001889 | furniture | pages [13] -->
m

<!-- b001890 | furniture | pages [13] -->
m

<!-- b001891 | furniture | pages [13] -->
m

<!-- b001892 | furniture | pages [13] -->
m

<!-- b001893 | furniture | pages [13] -->
m

<!-- b001894 | furniture | pages [13] -->
m

<!-- b001895 | furniture | pages [13] -->
m

<!-- b001896 | furniture | pages [13] -->
m

<!-- b001897 | furniture | pages [13] -->
m

<!-- b001898 | furniture | pages [13] -->
m

<!-- b001899 | furniture | pages [13] -->
m

<!-- b001900 | furniture | pages [13] -->
m

<!-- b001901 | furniture | pages [13] -->
m

<!-- b001902 | furniture | pages [13] -->
m

<!-- b001903 | furniture | pages [13] -->
m

<!-- b001904 | furniture | pages [13] -->
m

<!-- b001905 | furniture | pages [13] -->
m

<!-- b001906 | furniture | pages [13] -->
m

<!-- b001907 | furniture | pages [13] -->
m

<!-- b001908 | furniture | pages [13] -->
m

<!-- b001909 | furniture | pages [13] -->
m

<!-- b001910 | furniture | pages [13] -->
m

<!-- b001911 | furniture | pages [13] -->
m

<!-- b001912 | furniture | pages [13] -->
m

<!-- b001913 | furniture | pages [13] -->
m

<!-- b001914 | furniture | pages [13] -->
m

<!-- b001915 | furniture | pages [13] -->
m

<!-- b001916 | furniture | pages [13] -->
m

<!-- b001917 | furniture | pages [13] -->
m

<!-- b001918 | furniture | pages [13] -->
m

<!-- b001919 | furniture | pages [13] -->
m

<!-- b001920 | furniture | pages [13] -->
m

<!-- b001921 | furniture | pages [13] -->
m

<!-- b001922 | furniture | pages [13] -->
m

<!-- b001923 | furniture | pages [13] -->
m

<!-- b001924 | furniture | pages [13] -->
m

<!-- b001925 | furniture | pages [13] -->
m

<!-- b001926 | furniture | pages [13] -->
m

<!-- b001927 | furniture | pages [13] -->
m

<!-- b001928 | furniture | pages [13] -->
m

<!-- b001929 | furniture | pages [13] -->
m

<!-- b001930 | furniture | pages [13] -->
m

<!-- b001931 | furniture | pages [13] -->
m

<!-- b001932 | furniture | pages [13] -->
m

<!-- b001933 | furniture | pages [13] -->
m

<!-- b001934 | furniture | pages [13] -->
m

<!-- b001935 | furniture | pages [13] -->
m

<!-- b001936 | furniture | pages [13] -->
m

<!-- b001937 | furniture | pages [13] -->
m

<!-- b001938 | furniture | pages [13] -->
m

<!-- b001939 | furniture | pages [13] -->
m

<!-- b001940 | furniture | pages [13] -->
m

<!-- b001941 | furniture | pages [13] -->
m

<!-- b001942 | furniture | pages [13] -->
m

<!-- b001943 | furniture | pages [13] -->
m

<!-- b001944 | furniture | pages [13] -->
m

<!-- b001945 | furniture | pages [13] -->
m

<!-- b001946 | furniture | pages [13] -->
m

<!-- b001947 | furniture | pages [13] -->
m

<!-- b001948 | furniture | pages [13] -->
m

<!-- b001949 | furniture | pages [13] -->
m

<!-- b001950 | furniture | pages [13] -->
m

<!-- b001951 | furniture | pages [13] -->
m

<!-- b001952 | furniture | pages [13] -->
m

<!-- b001953 | furniture | pages [13] -->
m

<!-- b001954 | furniture | pages [13] -->
m

<!-- b001955 | furniture | pages [13] -->
m

<!-- b001956 | furniture | pages [13] -->
m

<!-- b001957 | furniture | pages [13] -->
m

<!-- b001958 | furniture | pages [13] -->
m

<!-- b001959 | furniture | pages [13] -->
m

<!-- b001960 | furniture | pages [13] -->
m

<!-- b001961 | furniture | pages [13] -->
m

<!-- b001962 | furniture | pages [13] -->
m

<!-- b001963 | furniture | pages [13] -->
m

<!-- b001964 | furniture | pages [13] -->
m

<!-- b001965 | furniture | pages [13] -->
m

<!-- b001966 | furniture | pages [13] -->
m

<!-- b001967 | furniture | pages [13] -->
m

<!-- b001968 | furniture | pages [13] -->
m

<!-- b001969 | furniture | pages [13] -->
m

<!-- b001970 | furniture | pages [13] -->
m

<!-- b001971 | furniture | pages [13] -->
m

<!-- b001972 | furniture | pages [13] -->
m

<!-- b001973 | furniture | pages [13] -->
m

<!-- b001974 | furniture | pages [13] -->
m

<!-- b001975 | furniture | pages [13] -->
m

<!-- b001976 | furniture | pages [13] -->
m

<!-- b001977 | furniture | pages [13] -->
m

<!-- b001978 | furniture | pages [13] -->
m

<!-- b001979 | furniture | pages [13] -->
m

<!-- b001980 | furniture | pages [13] -->
m

<!-- b001981 | furniture | pages [13] -->
m

<!-- b001982 | furniture | pages [14] -->
m

<!-- b001983 | furniture | pages [14] -->
m

<!-- b001984 | furniture | pages [14] -->
m

<!-- b001985 | furniture | pages [14] -->
m

<!-- b001986 | furniture | pages [14] -->
m

<!-- b001987 | furniture | pages [14] -->
m

<!-- b001988 | furniture | pages [14] -->
m

<!-- b001989 | furniture | pages [14] -->
m

<!-- b001990 | furniture | pages [14] -->
m

<!-- b001991 | furniture | pages [14] -->
m

<!-- b001992 | furniture | pages [14] -->
m

<!-- b001993 | furniture | pages [14] -->
m

<!-- b001994 | furniture | pages [14] -->
m

<!-- b001995 | furniture | pages [14] -->
m

<!-- b001996 | furniture | pages [14] -->
m

<!-- b001997 | furniture | pages [14] -->
m

<!-- b001998 | furniture | pages [14] -->
m

<!-- b001999 | furniture | pages [14] -->
m

<!-- b002000 | furniture | pages [14] -->
m

<!-- b002001 | furniture | pages [14] -->
m

<!-- b002002 | furniture | pages [14] -->
m

<!-- b002003 | furniture | pages [14] -->
m

<!-- b002004 | furniture | pages [14] -->
m

<!-- b002005 | furniture | pages [14] -->
m

<!-- b002006 | furniture | pages [14] -->
m

<!-- b002007 | furniture | pages [14] -->
m

<!-- b002008 | furniture | pages [14] -->
m

<!-- b002009 | furniture | pages [14] -->
m

<!-- b002010 | furniture | pages [14] -->
m

<!-- b002011 | furniture | pages [14] -->
m

<!-- b002012 | furniture | pages [14] -->
m

<!-- b002013 | furniture | pages [14] -->
m

<!-- b002014 | furniture | pages [14] -->
m

<!-- b002015 | furniture | pages [14] -->
m

<!-- b002016 | furniture | pages [14] -->
m

<!-- b002017 | furniture | pages [14] -->
m

<!-- b002018 | furniture | pages [14] -->
m

<!-- b002019 | furniture | pages [14] -->
m

<!-- b002020 | furniture | pages [14] -->
m

<!-- b002021 | furniture | pages [14] -->
m

<!-- b002022 | furniture | pages [14] -->
m

<!-- b002023 | furniture | pages [14] -->
m

<!-- b002024 | furniture | pages [14] -->
m

<!-- b002025 | furniture | pages [14] -->
m

<!-- b002026 | furniture | pages [14] -->
m

<!-- b002027 | furniture | pages [14] -->
m

<!-- b002028 | furniture | pages [14] -->
m

<!-- b002029 | furniture | pages [14] -->
m

<!-- b002030 | furniture | pages [14] -->
m

<!-- b002031 | furniture | pages [14] -->
m

<!-- b002032 | furniture | pages [14] -->
m

<!-- b002033 | furniture | pages [14] -->
m

<!-- b002034 | furniture | pages [14] -->
m

<!-- b002035 | furniture | pages [14] -->
m

<!-- b002036 | furniture | pages [14] -->
m

<!-- b002037 | furniture | pages [14] -->
m

<!-- b002038 | furniture | pages [14] -->
m

<!-- b002039 | furniture | pages [14] -->
m

<!-- b002040 | furniture | pages [14] -->
m

<!-- b002041 | furniture | pages [14] -->
m

<!-- b002042 | furniture | pages [14] -->
m

<!-- b002043 | furniture | pages [14] -->
m

<!-- b002044 | furniture | pages [14] -->
m

<!-- b002045 | furniture | pages [14] -->
m

<!-- b002046 | furniture | pages [14] -->
m

<!-- b002047 | furniture | pages [14] -->
m

<!-- b002048 | furniture | pages [14] -->
m

<!-- b002049 | furniture | pages [14] -->
m

<!-- b002050 | furniture | pages [14] -->
m

<!-- b002051 | furniture | pages [14] -->
m

<!-- b002052 | furniture | pages [14] -->
m

<!-- b002053 | furniture | pages [14] -->
m

<!-- b002054 | furniture | pages [14] -->
m

<!-- b002055 | furniture | pages [14] -->
m

<!-- b002056 | furniture | pages [14] -->
m

<!-- b002057 | furniture | pages [14] -->
m

<!-- b002058 | furniture | pages [14] -->
m

<!-- b002059 | furniture | pages [14] -->
m

<!-- b002060 | furniture | pages [14] -->
m

<!-- b002061 | furniture | pages [14] -->
m

<!-- b002062 | furniture | pages [14] -->
m

<!-- b002063 | furniture | pages [14] -->
m

<!-- b002064 | furniture | pages [14] -->
m

<!-- b002065 | furniture | pages [14] -->
m

<!-- b002066 | furniture | pages [14] -->
m

<!-- b002067 | furniture | pages [14] -->
m

<!-- b002068 | furniture | pages [14] -->
m

<!-- b002069 | furniture | pages [14] -->
m

<!-- b002070 | furniture | pages [14] -->
m

<!-- b002071 | furniture | pages [14] -->
m

<!-- b002072 | furniture | pages [14] -->
m

<!-- b002073 | furniture | pages [14] -->
m

<!-- b002074 | furniture | pages [14] -->
m

<!-- b002075 | furniture | pages [14] -->
m

<!-- b002076 | furniture | pages [14] -->
m

<!-- b002077 | furniture | pages [14] -->
m

<!-- b002078 | furniture | pages [14] -->
m

<!-- b002079 | furniture | pages [14] -->
m

<!-- b002080 | furniture | pages [14] -->
m

<!-- b002081 | furniture | pages [14] -->
m

<!-- b002082 | furniture | pages [14] -->
m

<!-- b002083 | furniture | pages [14] -->
m

<!-- b002084 | furniture | pages [14] -->
m

<!-- b002085 | furniture | pages [14] -->
m

<!-- b002086 | furniture | pages [14] -->
m

<!-- b002087 | furniture | pages [14] -->
m

<!-- b002088 | furniture | pages [14] -->
m

<!-- b002089 | furniture | pages [14] -->
m

<!-- b002090 | furniture | pages [14] -->
m

<!-- b002091 | furniture | pages [14] -->
m

<!-- b002092 | furniture | pages [14] -->
m

<!-- b002093 | furniture | pages [14] -->
m

<!-- b002094 | furniture | pages [14] -->
m

<!-- b002095 | furniture | pages [14] -->
m

<!-- b002096 | furniture | pages [14] -->
m

<!-- b002097 | furniture | pages [14] -->
m

<!-- b002098 | furniture | pages [14] -->
m

<!-- b002099 | furniture | pages [14] -->
m

<!-- b002100 | furniture | pages [14] -->
m

<!-- b002101 | furniture | pages [14] -->
m

<!-- b002102 | furniture | pages [14] -->
m

<!-- b002103 | furniture | pages [14] -->
m

<!-- b002104 | furniture | pages [14] -->
m

<!-- b002105 | furniture | pages [14] -->
m

<!-- b002106 | furniture | pages [14] -->
m

<!-- b002107 | furniture | pages [14] -->
m

<!-- b002108 | furniture | pages [14] -->
m

<!-- b002109 | furniture | pages [14] -->
m

<!-- b002110 | furniture | pages [14] -->
m

<!-- b002111 | furniture | pages [14] -->
m

<!-- b002112 | furniture | pages [14] -->
m

<!-- b002113 | furniture | pages [14] -->
m

<!-- b002114 | furniture | pages [14] -->
m

<!-- b002115 | furniture | pages [14] -->
m

<!-- b002116 | furniture | pages [14] -->
m

<!-- b002117 | furniture | pages [14] -->
m

<!-- b002118 | furniture | pages [14] -->
m

<!-- b002119 | furniture | pages [14] -->
m

<!-- b002120 | furniture | pages [14] -->
m

<!-- b002121 | furniture | pages [14] -->
m

<!-- b002122 | furniture | pages [14] -->
m

<!-- b002123 | furniture | pages [14] -->
m

<!-- b002124 | furniture | pages [14] -->
m

<!-- b002125 | furniture | pages [14] -->
m

<!-- b002126 | furniture | pages [14] -->
m

<!-- b002127 | furniture | pages [14] -->
m

<!-- b002128 | furniture | pages [14] -->
m

<!-- b002129 | furniture | pages [14] -->
m

<!-- b002130 | furniture | pages [14] -->
m

<!-- b002131 | furniture | pages [14] -->
m

<!-- b002132 | furniture | pages [14] -->
m

<!-- b002133 | furniture | pages [14] -->
m

<!-- b002134 | furniture | pages [14] -->
m

<!-- b002135 | furniture | pages [14] -->
m

<!-- b002136 | furniture | pages [14] -->
m

<!-- b002137 | furniture | pages [14] -->
m

<!-- b002138 | furniture | pages [14] -->
m

<!-- b002139 | furniture | pages [14] -->
m

<!-- b002140 | furniture | pages [14] -->
m

<!-- b002141 | furniture | pages [14] -->
m

<!-- b002142 | furniture | pages [14] -->
m

<!-- b002143 | furniture | pages [14] -->
m

<!-- b002144 | furniture | pages [14] -->
m

<!-- b002145 | furniture | pages [14] -->
m

<!-- b002146 | furniture | pages [14] -->
m

<!-- b002147 | furniture | pages [14] -->
m

<!-- b002148 | furniture | pages [14] -->
m

<!-- b002149 | furniture | pages [14] -->
m

<!-- b002150 | furniture | pages [14] -->
m

<!-- b002151 | furniture | pages [14] -->
m

<!-- b002152 | furniture | pages [14] -->
m

<!-- b002153 | furniture | pages [14] -->
m

<!-- b002154 | furniture | pages [14] -->
m

<!-- b002155 | furniture | pages [14] -->
m

<!-- b002156 | furniture | pages [14] -->
m

<!-- b002157 | furniture | pages [14] -->
m

<!-- b002158 | furniture | pages [14] -->
m

<!-- b002159 | furniture | pages [14] -->
m

<!-- b002160 | furniture | pages [14] -->
m

<!-- b002161 | furniture | pages [14] -->
m

<!-- b002162 | furniture | pages [14] -->
m

<!-- b002163 | furniture | pages [14] -->
m

<!-- b002164 | furniture | pages [14] -->
m

<!-- b002165 | furniture | pages [14] -->
m

<!-- b002166 | furniture | pages [14] -->
m

<!-- b002167 | furniture | pages [14] -->
m

<!-- b002168 | furniture | pages [14] -->
m

<!-- b002169 | furniture | pages [14] -->
m

<!-- b002170 | furniture | pages [14] -->
m

<!-- b002171 | furniture | pages [14] -->
m

<!-- b002172 | furniture | pages [14] -->
m

<!-- b002173 | furniture | pages [14] -->
m

<!-- b002174 | furniture | pages [14] -->
m

<!-- b002175 | furniture | pages [14] -->
m

<!-- b002176 | furniture | pages [14] -->
m

<!-- b002177 | furniture | pages [14] -->
m

<!-- b002178 | furniture | pages [14] -->
m

<!-- b002179 | furniture | pages [14] -->
m

<!-- b002180 | furniture | pages [14] -->
m

<!-- b002181 | furniture | pages [14] -->
m

<!-- b002182 | furniture | pages [14] -->
m

<!-- b002183 | furniture | pages [14] -->
m

<!-- b002184 | furniture | pages [14] -->
m

<!-- b002185 | furniture | pages [14] -->
m

<!-- b002186 | furniture | pages [14] -->
m

<!-- b002187 | furniture | pages [14] -->
m

<!-- b002188 | furniture | pages [14] -->
m

<!-- b002189 | furniture | pages [14] -->
m

<!-- b002190 | furniture | pages [14] -->
m

<!-- b002191 | furniture | pages [14] -->
m

<!-- b002192 | furniture | pages [14] -->
m

<!-- b002193 | furniture | pages [14] -->
m

<!-- b002194 | furniture | pages [14] -->
m

<!-- b002195 | furniture | pages [14] -->
m

<!-- b002196 | furniture | pages [14] -->
m

<!-- b002197 | furniture | pages [14] -->
m

<!-- b002198 | furniture | pages [14] -->
m

<!-- b002199 | furniture | pages [14] -->
m

<!-- b002200 | furniture | pages [14] -->
m

<!-- b002201 | furniture | pages [14] -->
m

<!-- b002202 | furniture | pages [14] -->
m

<!-- b002203 | furniture | pages [14] -->
m

<!-- b002204 | furniture | pages [14] -->
m

<!-- b002205 | furniture | pages [14] -->
m

<!-- b002206 | furniture | pages [14] -->
m

<!-- b002207 | furniture | pages [14] -->
m

<!-- b002208 | furniture | pages [14] -->
m

<!-- b002209 | furniture | pages [14] -->
m

<!-- b002210 | furniture | pages [14] -->
m

<!-- b002211 | furniture | pages [14] -->
m

<!-- b002212 | furniture | pages [14] -->
m

<!-- b002213 | furniture | pages [14] -->
m

<!-- b002214 | furniture | pages [14] -->
m

<!-- b002215 | furniture | pages [14] -->
m

<!-- b002216 | furniture | pages [14] -->
m

<!-- b002217 | furniture | pages [14] -->
m

<!-- b002218 | furniture | pages [14] -->
m

<!-- b002219 | furniture | pages [14] -->
m

<!-- b002220 | furniture | pages [14] -->
m

<!-- b002221 | furniture | pages [14] -->
m

<!-- b002222 | furniture | pages [14] -->
m

<!-- b002223 | furniture | pages [14] -->
m

<!-- b002224 | furniture | pages [14] -->
m

<!-- b002225 | furniture | pages [14] -->
m

<!-- b002226 | furniture | pages [14] -->
m

<!-- b002227 | furniture | pages [14] -->
m

<!-- b002228 | furniture | pages [14] -->
m

<!-- b002229 | furniture | pages [14] -->
m

<!-- b002230 | furniture | pages [14] -->
m

<!-- b002231 | furniture | pages [14] -->
m

<!-- b002232 | furniture | pages [14] -->
m

<!-- b002233 | furniture | pages [14] -->
m

<!-- b002234 | furniture | pages [14] -->
m

<!-- b002235 | furniture | pages [14] -->
m

<!-- b002236 | furniture | pages [14] -->
m

<!-- b002237 | furniture | pages [14] -->
m

<!-- b002238 | furniture | pages [14] -->
m

<!-- b002239 | furniture | pages [14] -->
m

<!-- b002240 | furniture | pages [14] -->
m

<!-- b002241 | furniture | pages [14] -->
m

<!-- b002242 | furniture | pages [14] -->
m

<!-- b002243 | furniture | pages [14] -->
m

<!-- b002244 | furniture | pages [14] -->
Team # 2503268

<!-- b002245 | furniture | pages [14] -->
Page 12 of 24

<!-- b002246 | furniture | pages [14] -->
m

<!-- b002247 | furniture | pages [14] -->
m

<!-- b002248 | furniture | pages [14] -->
m

<!-- b002249 | furniture | pages [14] -->
m

<!-- b002250 | furniture | pages [14] -->
m

<!-- b002251 | furniture | pages [14] -->
m

<!-- b002252 | furniture | pages [14] -->
m

<!-- b002253 | furniture | pages [14] -->
m

<!-- b002254 | furniture | pages [14] -->
m

<!-- b002255 | furniture | pages [14] -->
m

<!-- b002256 | furniture | pages [14] -->
m

<!-- b002257 | furniture | pages [14] -->
m

<!-- b002258 | furniture | pages [14] -->
m

<!-- b002259 | furniture | pages [14] -->
m

<!-- b002260 | furniture | pages [14] -->
m

<!-- b002261 | furniture | pages [14] -->
m

<!-- b002262 | furniture | pages [14] -->
m

<!-- b002263 | furniture | pages [14] -->
m

<!-- b002264 | furniture | pages [14] -->
m

<!-- b002265 | furniture | pages [14] -->
m

<!-- b002266 | furniture | pages [14] -->
m

<!-- b002267 | furniture | pages [14] -->
m

<!-- b002268 | furniture | pages [14] -->
m

<!-- b002269 | furniture | pages [14] -->
m

<!-- b002270 | furniture | pages [14] -->
m

<!-- b002271 | furniture | pages [14] -->
m

<!-- b002272 | furniture | pages [14] -->
m

<!-- b002273 | furniture | pages [14] -->
m

<!-- b002274 | furniture | pages [14] -->
m

<!-- b002275 | furniture | pages [14] -->
m

<!-- b002276 | furniture | pages [14] -->
m

<!-- b002277 | furniture | pages [14] -->
m

<!-- b002278 | furniture | pages [14] -->
m

<!-- b002279 | furniture | pages [14] -->
m

<!-- b002280 | furniture | pages [14] -->
m

<!-- b002281 | furniture | pages [14] -->
m

<!-- b002282 | furniture | pages [14] -->
m

<!-- b002283 | furniture | pages [14] -->
m

<!-- b002284 | furniture | pages [14] -->
m

<!-- b002285 | furniture | pages [14] -->
m

<!-- b002286 | furniture | pages [14] -->
m

<!-- b002287 | furniture | pages [14] -->
m

<!-- b002288 | furniture | pages [14] -->
m

<!-- b002289 | furniture | pages [14] -->
m

<!-- b002290 | furniture | pages [14] -->
m

<!-- b002291 | furniture | pages [14] -->
m

<!-- b002292 | furniture | pages [14] -->
m

<!-- b002293 | furniture | pages [14] -->
m

<!-- b002294 | furniture | pages [14] -->
m

<!-- b002295 | furniture | pages [14] -->
m

<!-- b002296 | furniture | pages [14] -->
m

<!-- b002297 | furniture | pages [14] -->
m

<!-- b002298 | furniture | pages [14] -->
m

<!-- b002299 | furniture | pages [14] -->
m

<!-- b002300 | furniture | pages [14] -->
m

<!-- b002301 | furniture | pages [14] -->
m

<!-- b002302 | furniture | pages [14] -->
m

<!-- b002303 | furniture | pages [14] -->
m

<!-- b002304 | furniture | pages [14] -->
m

<!-- b002305 | furniture | pages [14] -->
m

<!-- b002306 | furniture | pages [14] -->
m

<!-- b002307 | furniture | pages [14] -->
m

<!-- b002308 | furniture | pages [14] -->
m

<!-- b002309 | furniture | pages [14] -->
m

<!-- b002310 | furniture | pages [14] -->
m

<!-- b002311 | furniture | pages [14] -->
m

<!-- b002312 | furniture | pages [14] -->
m

<!-- b002313 | furniture | pages [14] -->
m

<!-- b002314 | furniture | pages [14] -->
m

<!-- b002315 | furniture | pages [14] -->
m

<!-- b002316 | furniture | pages [14] -->
m

<!-- b002317 | furniture | pages [14] -->
m

<!-- b002318 | furniture | pages [14] -->
m

<!-- b002319 | furniture | pages [14] -->
m

<!-- b002320 | furniture | pages [14] -->
m

<!-- b002321 | furniture | pages [14] -->
m

<!-- b002322 | furniture | pages [14] -->
m

<!-- b002323 | furniture | pages [14] -->
m

<!-- b002324 | furniture | pages [14] -->
m

<!-- b002325 | furniture | pages [14] -->
m

<!-- b002326 | furniture | pages [14] -->
m

<!-- b002327 | furniture | pages [14] -->
m

<!-- b002328 | furniture | pages [14] -->
m

<!-- b002329 | furniture | pages [14] -->
m

<!-- b002330 | furniture | pages [14] -->
m

<!-- b002331 | furniture | pages [14] -->
m

<!-- b002332 | furniture | pages [14] -->
m

<!-- b002333 | furniture | pages [14] -->
m

<!-- b002334 | furniture | pages [14] -->
m

<!-- b002335 | furniture | pages [14] -->
m

<!-- b002336 | furniture | pages [14] -->
m

<!-- b002337 | furniture | pages [14] -->
m

<!-- b002338 | furniture | pages [14] -->
m

<!-- b002339 | furniture | pages [14] -->
m

<!-- b002340 | furniture | pages [14] -->
m

<!-- b002341 | furniture | pages [14] -->
m

<!-- b002342 | furniture | pages [14] -->
m

<!-- b002343 | furniture | pages [14] -->
m

<!-- b002344 | furniture | pages [14] -->
m

<!-- b002345 | furniture | pages [14] -->
m

<!-- b002346 | furniture | pages [14] -->
m

<!-- b002347 | furniture | pages [14] -->
m

<!-- b002348 | furniture | pages [14] -->
m

<!-- b002349 | furniture | pages [14] -->
m

<!-- b002350 | furniture | pages [14] -->
m

<!-- b002351 | furniture | pages [14] -->
m

<!-- b002352 | furniture | pages [14] -->
m

<!-- b002353 | furniture | pages [14] -->
m

<!-- b002354 | furniture | pages [14] -->
m

<!-- b002355 | furniture | pages [14] -->
m

<!-- b002356 | furniture | pages [14] -->
m

<!-- b002357 | furniture | pages [14] -->
m

<!-- b002358 | furniture | pages [14] -->
m

<!-- b002359 | furniture | pages [14] -->
m

<!-- b002360 | furniture | pages [14] -->
m

<!-- b002361 | furniture | pages [14] -->
m

<!-- b002362 | furniture | pages [14] -->
m

<!-- b002363 | furniture | pages [14] -->
m

<!-- b002364 | furniture | pages [14] -->
m

<!-- b002365 | furniture | pages [14] -->
m

<!-- b002366 | furniture | pages [14] -->
m

<!-- b002367 | furniture | pages [14] -->
m

<!-- b002368 | furniture | pages [14] -->
m

<!-- b002369 | furniture | pages [14] -->
m

<!-- b002370 | furniture | pages [14] -->
m

<!-- b002371 | furniture | pages [14] -->
m

<!-- b002372 | furniture | pages [14] -->
m

<!-- b002373 | furniture | pages [14] -->
m

<!-- b002374 | furniture | pages [14] -->
m

<!-- b002375 | furniture | pages [14] -->
m

<!-- b002376 | furniture | pages [14] -->
m

<!-- b002377 | furniture | pages [14] -->
m

<!-- b002378 | furniture | pages [14] -->
m

<!-- b002379 | furniture | pages [14] -->
m

<!-- b002380 | furniture | pages [14] -->
m

<!-- b002381 | furniture | pages [14] -->
m

<!-- b002382 | furniture | pages [14] -->
m

<!-- b002383 | furniture | pages [14] -->
m

<!-- b002384 | furniture | pages [14] -->
m

<!-- b002385 | furniture | pages [14] -->
m

<!-- b002386 | furniture | pages [14] -->
m

<!-- b002387 | furniture | pages [14] -->
m

<!-- b002388 | furniture | pages [14] -->
m

<!-- b002389 | furniture | pages [14] -->
m

<!-- b002390 | furniture | pages [14] -->
m

<!-- b002391 | furniture | pages [14] -->
m

<!-- b002392 | furniture | pages [14] -->
m

<!-- b002393 | furniture | pages [14] -->
m

<!-- b002394 | furniture | pages [14] -->
m

<!-- b002395 | furniture | pages [14] -->
m

<!-- b002396 | furniture | pages [14] -->
m

<!-- b002397 | furniture | pages [14] -->
m

<!-- b002398 | furniture | pages [14] -->
m

<!-- b002399 | furniture | pages [14] -->
m

<!-- b002400 | furniture | pages [14] -->
m

<!-- b002401 | furniture | pages [14] -->
m

<!-- b002402 | furniture | pages [14] -->
m

<!-- b002403 | furniture | pages [14] -->
m

<!-- b002404 | furniture | pages [14] -->
m

<!-- b002405 | furniture | pages [14] -->
m

<!-- b002406 | furniture | pages [14] -->
m

<!-- b002407 | furniture | pages [14] -->
m

<!-- b002408 | furniture | pages [14] -->
m

<!-- b002409 | furniture | pages [14] -->
m

<!-- b002410 | furniture | pages [14] -->
m

<!-- b002411 | furniture | pages [14] -->
m

<!-- b002412 | furniture | pages [14] -->
m

<!-- b002413 | furniture | pages [14] -->
m

<!-- b002414 | furniture | pages [14] -->
m

<!-- b002415 | furniture | pages [14] -->
m

<!-- b002416 | furniture | pages [14] -->
m

<!-- b002417 | furniture | pages [14] -->
m

<!-- b002418 | furniture | pages [14] -->
m

<!-- b002419 | furniture | pages [14] -->
m

<!-- b002420 | furniture | pages [14] -->
m

<!-- b002421 | furniture | pages [14] -->
m

<!-- b002422 | furniture | pages [14] -->
m

<!-- b002423 | furniture | pages [14] -->
m

<!-- b002424 | furniture | pages [14] -->
m

<!-- b002425 | furniture | pages [14] -->
m

<!-- b002426 | furniture | pages [14] -->
m

<!-- b002427 | furniture | pages [14] -->
m

<!-- b002428 | furniture | pages [14] -->
m

<!-- b002429 | furniture | pages [14] -->
m

<!-- b002430 | furniture | pages [14] -->
m

<!-- b002431 | furniture | pages [14] -->
m

<!-- b002432 | furniture | pages [14] -->
m

<!-- b002433 | furniture | pages [14] -->
m

<!-- b002434 | furniture | pages [14] -->
m

<!-- b002435 | furniture | pages [14] -->
m

<!-- b002436 | furniture | pages [14] -->
m

<!-- b002437 | furniture | pages [14] -->
m

<!-- b002438 | furniture | pages [14] -->
m

<!-- b002439 | furniture | pages [14] -->
m

<!-- b002440 | furniture | pages [14] -->
m

<!-- b002441 | furniture | pages [14] -->
m

<!-- b002442 | furniture | pages [14] -->
m

<!-- b002443 | furniture | pages [14] -->
m

<!-- b002444 | furniture | pages [14] -->
m

<!-- b002445 | furniture | pages [14] -->
m

<!-- b002446 | furniture | pages [14] -->
m

<!-- b002447 | furniture | pages [14] -->
m

<!-- b002448 | furniture | pages [14] -->
m

<!-- b002449 | furniture | pages [14] -->
m

<!-- b002450 | furniture | pages [14] -->
m

<!-- b002451 | furniture | pages [14] -->
m

<!-- b002452 | furniture | pages [14] -->
m

<!-- b002453 | furniture | pages [14] -->
m

<!-- b002454 | furniture | pages [14] -->
m

<!-- b002455 | furniture | pages [14] -->
m

<!-- b002456 | furniture | pages [14] -->
m

<!-- b002457 | furniture | pages [14] -->
m

<!-- b002458 | furniture | pages [14] -->
m

<!-- b002459 | furniture | pages [14] -->
m

<!-- b002460 | furniture | pages [14] -->
m

<!-- b002461 | furniture | pages [14] -->
m

<!-- b002462 | furniture | pages [14] -->
m

<!-- b002463 | furniture | pages [14] -->
m

<!-- b002464 | furniture | pages [14] -->
m

<!-- b002465 | furniture | pages [14] -->
m

<!-- b002466 | furniture | pages [14] -->
m

<!-- b002467 | furniture | pages [14] -->
m

<!-- b002468 | furniture | pages [14] -->
m

<!-- b002469 | furniture | pages [14] -->
m

<!-- b002470 | furniture | pages [14] -->
m

<!-- b002471 | furniture | pages [14] -->
m

<!-- b002472 | furniture | pages [14] -->
m

<!-- b002473 | furniture | pages [14] -->
m

<!-- b002474 | furniture | pages [14] -->
m

<!-- b002475 | furniture | pages [14] -->
m

<!-- b002476 | furniture | pages [14] -->
m

<!-- b002477 | furniture | pages [14] -->
m

<!-- b002478 | furniture | pages [14] -->
m

<!-- b002479 | furniture | pages [14] -->
m

<!-- b002480 | furniture | pages [14] -->
m

<!-- b002481 | furniture | pages [14] -->
m

<!-- b002482 | furniture | pages [14] -->
m

<!-- b002483 | furniture | pages [14] -->
m

<!-- b002484 | furniture | pages [14] -->
m

<!-- b002485 | furniture | pages [14] -->
m

<!-- b002486 | furniture | pages [14] -->
m

<!-- b002487 | furniture | pages [14] -->
m

<!-- b002488 | furniture | pages [14] -->
m

<!-- b002489 | furniture | pages [14] -->
m

<!-- b002490 | furniture | pages [14] -->
m

<!-- b002491 | furniture | pages [14] -->
m

<!-- b002492 | furniture | pages [14] -->
m

<!-- b002493 | furniture | pages [14] -->
m

<!-- b002494 | furniture | pages [14] -->
m

<!-- b002495 | furniture | pages [14] -->
m

<!-- b002496 | furniture | pages [14] -->
m

<!-- b002497 | furniture | pages [14] -->
m

<!-- b002498 | furniture | pages [14] -->
m

<!-- b002499 | furniture | pages [14] -->
m

<!-- b002500 | furniture | pages [14] -->
m

<!-- b002501 | furniture | pages [14] -->
m

<!-- b002502 | furniture | pages [14] -->
m

<!-- b002503 | furniture | pages [14] -->
m

<!-- b002504 | furniture | pages [14] -->
m

<!-- b002505 | furniture | pages [14] -->
m

<!-- b002506 | furniture | pages [14] -->
m

<!-- b002507 | furniture | pages [14] -->
m

<!-- b002508 | furniture | pages [14] -->
m

<!-- b002509 | furniture | pages [14] -->
m

<!-- b002510 | furniture | pages [14] -->
m

<!-- b002511 | furniture | pages [14] -->
m

<!-- b002512 | furniture | pages [14] -->
m

<!-- b002513 | furniture | pages [14] -->
m

<!-- b002514 | furniture | pages [14] -->
m

<!-- b002515 | furniture | pages [14] -->
m

<!-- b002516 | furniture | pages [14] -->
m

<!-- b002517 | furniture | pages [14] -->
m

<!-- b002518 | furniture | pages [14] -->
m

<!-- b002519 | furniture | pages [14] -->
m

<!-- b002520 | furniture | pages [14] -->
m

<!-- b002521 | furniture | pages [14] -->
m

<!-- b002522 | furniture | pages [14] -->
m

<!-- b002523 | furniture | pages [14] -->
m

<!-- b002524 | furniture | pages [14] -->
m

<!-- b002526 | prose | pages [14] -->
• w1i, w2i, w3i: the weights assigned to each sub-indicator within the three factors that satisfy %4 i=1 wmi = 1, m = 1, 2, 3. This implies that for each main factor, the four sub-indicators sum to a total weight of 1.

<!-- b002527 | prose | pages [14] -->
• wi: the weight assigned to each of the three main factors S core1, S core2, S core3. These must satisfy:

<!-- b002528 | prose | pages [14] -->
& 3 wi = 1.

<!-- b002529 | prose | pages [14] -->
i=1 S core1 = Σ4 S core2 = Σ4 S core3 = Σ4 i=1w1iS 1i i=1w2iS 2i i=1w3iS 3i S core = Σ3 i=1wiS corei

<!-- b002530 | prose | pages [14] -->
According to some materials, the average time of tourists’ stay is around 4 days. So, the average number of tourists in Juneau each day is Nt = 4NJuneau 365 .

<!-- b002531 | prose | pages [14] -->
• The increase in average individual income The formula reﬂects the impact of tourism on average individual income by considering the ratio Juneau))↓ε ac- of tax income to population as a measure of income of tourism. The factor (1/(1+H↑ counts for the negative inﬂuence of glacier retreat on sustainable tourism growth, assuming that environmental degradation can harm long-term economic beneﬁts. Additionally, the logarithmic term incorporates the proportional allocation of tax revenue (µ1) to infrastructure, reﬂecting how government investments boosts economy. Normalization term T0/P ensures that income growth is evaluated in comparison with a baseline, while logarithm smooth out extreme values.

<!-- b002532 | prose | pages [14] -->
Inc = TJuneau 1 )↓ε · (1 + ϱ1 ln µ1 + 1 · ( µI + 1) (7) 1 + H↑ P Juneau S 11 = Inc T0/P = TJuneau 1 )↓ε · (1 + ϱ1 ln µ1 + 1 · ( µI + 1) (8) 1 + H↑ T0

<!-- b002533 | prose | pages [14] -->
• Crowding level Juneau

<!-- b002534 | prose | pages [14] -->
The formula quantiﬁes crowding based on the ratio of average daily tourists to the population (Nt/P), using a Sigmoid function to capture how perceived crowding increases at a decreasing rate as tourist density grows. This ensures that the score accounts for diminishing sensitivity to additional tourists in high-density scenarios. Also, the score is guaranteed to be normalized.

<!-- b002535 | prose | pages [14] -->
Parameters like εc and ς control the steepness and inﬂection point of the curve, respectively.

<!-- b002536 | prose | pages [14] -->
1 S 12 = ϑ · (9) 1 + e↓εc(Nt/P↓ς)

<!-- b002537 | prose | pages [14] -->
• Housing aﬀordability The formula for S 13 estimates housing costs (HCost) based on tourist density (Nt/P) and tax rev- enue allocated to infrastructure (T ↑ Juneauµ1). The study by Glaeser et al. [7] reveals the relation between number of tourists and housing aﬀorability.This reﬂects the dual pressures of increased demand for short-term housing and inﬂuences of infrastructure investments. The score is nor- malized within a historical range. The normalization method ensures that higher housing costs reduce the aﬀordability score.

<!-- b002538 | prose | pages [14, 15] -->
关注数学模型 Nt P + ε2T ↑ HCost = ε1 (10) Juneauµ1 S 13 = Cmax ↓HCost (11) Cmax ↓Cmin

<!-- b002539 | furniture | pages [14] -->
2

<!-- b002540 | furniture | pages [14] -->
MATHmodels

<!-- b002541 | furniture | pages [14] -->
获取更多资讯

<!-- b002542 | furniture | pages [15] -->
Team # 2503268

<!-- b002543 | furniture | pages [15] -->
Page 13 of 24

<!-- b002545 | prose | pages [15] -->
• Noise level We calculate noise levels as the sum of a baseline noise level (N0) and a power-law term , where 微信公众号：数学模型 tourist density contributes exponentially to increased noise. The normalization by CNN0 scales the score to reﬂect relative changes. The power-law term avoids extreme values by bounding the output.

<!-- b002546 | prose | pages [15] -->
Noise = N0 + N↑ϱ (12) Juneau = N0 + N↑ϱ S 14 = Noise Juneau (13) CNN0 CNN0

<!-- b002547 | prose | pages [15] -->
• Natural resources Measure natural resources by considering glacier retreat and tax revenue allocation to environ- mental protection. A Sigmoid function ensures a smooth transition as environmental pressure increases. The term εN · µE+1 µ2+1 · H↑ Juneau highlights the trade-oﬀbetween environmental investment 微信号：MATHmodels and degradation, as well as avoiding extreme values.

<!-- b002548 | prose | pages [15] -->
φ0 S 21 = (14) 1 + eεN· µE+1 µ2+1 ·H↑ Juneau

<!-- b002549 | prose | pages [15] -->
• Water and energy usage The formula evaluates water and energy consumption based on the combined population and tourist density (P + Nt). Sigmoid function captures the nonlinear relation, with ϱWE controlling the rate of increase and E0 serving as a baseline threshold. Meanwhile, the score is guaranteed to be normalized in this way.

<!-- b002550 | prose | pages [15] -->
Energy = ϱWE(P + Nt) (15) e↓(ϱWE(P+Nt)↓E0) 1 S 22 = 1 ↓ (16) 1 + e↓(Energy↓E0) = 1 + e↓(ϱWE(P+Nt)↓E0)

<!-- b002551 | prose | pages [15] -->
• Waste production level Waste production is calculated as the diﬀerence between normalized tourist density (N↑) and waste management impact (ϱCµ3T ↑), with a lower bound of zero. When waste generation ex- ceeds management reduction, penalize the score. The normalization by Cw(N↑+ 1) ensures the score remains bounded.

<!-- b002552 | prose | pages [15] -->
Waste = min(N↑ Juneau ↓ϱCµ3T ↑ Juneau, 0) (17) Cw(N↑+ 1) = 1 ↓min(N↑ Juneau ↓ϱCµ3T ↑ Juneau, 0) Waste S 23 = 1 ↓ (18) Cw(N↑ Juneau + 1)

<!-- b002553 | prose | pages [15] -->
• Carbon footprint The formula uses a Sigmoid function to keep the score in a reasonable range considering tourist population(Nt). ϑCE and NC control the sensitivity and baseline.

<!-- b002554 | prose | pages [15, 16] -->
1 S 24 = 1 ↓ (19) 1 + eϑCE(NC↓Nt) • Tourism tax revenue Normalize the score in a reasonable range with history data.

<!-- b002555 | furniture | pages [16] -->
Team # 2503268

<!-- b002556 | furniture | pages [16] -->
Page 14 of 24

<!-- b002558 | prose | pages [16] -->
S 31 = TJuneau ↓Tmin (20) Tmax ↓Tmin

<!-- b002559 | prose | pages [16] -->
• Employment growth The S 32 formula models employment growth as a linear combination of normalized tax income (T ↑ Juneau) and population (N↑ Juneau), with coeﬃcients representing the respective contributions of tourism and local demographics.

<!-- b002560 | prose | pages [16] -->
S 32 = ϱTT ↑ Juneau + ϱNN↑ (21) Juneau

<!-- b002561 | prose | pages [16] -->
• Cultural resource protection or utilization The S 33 formula measures cultural factors as an inverse exponential function of tax investment of culture (µ4T ↑ Juneau) and number of tourists’ spreading (N↑).

<!-- b002562 | prose | pages [16] -->
Juneau)N↑ S 33 = (µ4T ↑ (22)

<!-- b002563 | prose | pages [16] -->
• Social safety or security index According to study in an article by Hall, C. M. et al. [8], the S 34 formula was constructed to evaluate social safety by considering government allocated investment(µ5T ↑ Juneau) and population N↑ Juneau+1 (N↑ Juneau) on security resources. The term 1 ↓ Juneau+1) prevents division by zero and smooths ϑT µ5(T ↑ the impact of extreme values.

<!-- b002564 | prose | pages [16] -->
N↑ Juneau + 1 S 34 = 1 ↓ (23) ϑTµ5(T ↑ Juneau + 1)

<!-- b002565 | heading | pages [16] -->
6.3 Values of Parameters

<!-- b002566 | prose | pages [16] -->
We estimate the parameters using methods that substitute some speciﬁc values to compute the scores and make the scores reasonable. Some of the parameters are experience-based, and some come from multiplying known data by a certain ratio, which might be a growth rate or a disturbance rate, etc. The following table of parameter values was eventually obtained.

<!-- b002567 | heading | pages [16] -->
6.4 Weights Distribution Outcomes

<!-- b002568 | prose | pages [16] -->
To calculate the weights of AHP, we compare each each combinations of factors or secondary indicators and build up four judgment matrices. Through consistency check, by making sure CR < 0.1, we guarantee that the matrices are usable. The weights along with other useful calculated results and a heatmap of weights are as follows.

<!-- b002569 | heading | pages [16] -->
7 Analysis of Factors

<!-- b002570 | prose | pages [16] -->
We have now established the STDM model. In this section, we will compare and categorize the various factors, speciﬁcally identifying which components are to be optimized and which will serve as constraints. This analysis directly addresses the requirements of the ﬁrst sub-question in our study.

<!-- b002571 | prose | pages [16] -->
Considering the ultimate goal of sustainable development, all factors listed in the Score Calculation Model can be regarded as Optimization Factors. For the Constraints Factors, we approach the

<!-- b002572 | prose | pages [16, 17] -->
关注数学模型 Parameter Value Parameter Value Parameter Value Parameter Value 0.2 T0 2448159 0.3 0.2 ε ϱ1 µI 0.8 0.6 2 0.4 ϑ εc ς ε1 微信公众号：数学模型 0.6 Cmax 0.5 Cmin 0.2 N0 1 ε2 3 CN 1.5 1 0.8 ϱ φ0 εN 1 0.2 E0 1 4 µE ϱWE ϱC 47528 1 Cw 1 Nc 24252 Tmax 1632106 ϑCE 25000 Tmin 1029604 0.25 0.75 5 ϱT ϱN ϑt

<!-- b002573 | furniture | pages [16] -->
2

<!-- b002574 | furniture | pages [16] -->
MATHmodels

<!-- b002575 | furniture | pages [16] -->
获取更多资讯

<!-- b002576 | furniture | pages [17] -->
Team # 2503268

<!-- b002577 | furniture | pages [17] -->
Page 15 of 24

<!-- b002579 | caption | pages [17] -->
Table 5: Parameter values and their respective values.

<!-- b002580 | prose | pages [17] -->
Parameter Score Score_1 Score_2 Score_3 微信号：MATHmodels Judgment Matrix         1 0.5 2.5 1 3 6 5 1 4 3 2 1 1 5 4 1 1 1 1 2 1 4 1 3 2 1 1 1 6 3 3 4 2 2.5 1 1 2 1 5 2 1 1 5 0.4 0.25 1 1 1 1 6 3 3 3 2 3 5 6 6 1 1 3 1 3 1 1 6 1 2 1 1 5 2 2 2 2 4 3 5

<!-- b002581 | prose | pages [17] -->
Max Eigen- 3.006 4.016 4.037 4.024 values Consistency 0.0028 0.0052 0.0125 0.0079 Index (CI) Consistency 0.0048 < 0.1 0.0057 < 0.1 0.0139 < 0.1 0.0088 < 0.1 Ratio (CR) Weights 0.3041, 0.5784, 0.4744, 0.4092, 0.5648, 0.2230, 0.1011, 0.4017, 0.1311 0.0823, 0.1873, 0.0795, 0.1163 0.2372 0.1096

<!-- b002582 | caption | pages [17] -->
Table 6: Weights Distribution Outcomes for Scores

<!-- b002583 | prose | pages [17] -->
system from three dimensions—population, environment, and economy—examining the limitations imposed by diﬀerent policies on these factors. For instance, as identiﬁed in the Juneau Climate Action and Implementation Plan, the policy introduced by the City of Juneau in 2016, which imposed caps on the number of daily visitors, serves as a constraint within the population dimension.

<!-- b002584 | prose | pages [17] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002585 | furniture | pages [17] -->
m

<!-- b002586 | furniture | pages [17] -->
m

<!-- b002587 | furniture | pages [17] -->
m

<!-- b002588 | furniture | pages [17] -->
m

<!-- b002589 | furniture | pages [17] -->
m

<!-- b002590 | furniture | pages [17] -->
m

<!-- b002591 | furniture | pages [17] -->
m

<!-- b002592 | furniture | pages [17] -->
m

<!-- b002593 | furniture | pages [17] -->
m

<!-- b002594 | furniture | pages [17] -->
m

<!-- b002595 | furniture | pages [17] -->
m

<!-- b002596 | furniture | pages [17] -->
m

<!-- b002597 | furniture | pages [17] -->
m

<!-- b002598 | furniture | pages [17] -->
m

<!-- b002599 | furniture | pages [17] -->
m

<!-- b002600 | furniture | pages [17] -->
m

<!-- b002601 | furniture | pages [17] -->
m

<!-- b002602 | furniture | pages [17] -->
m

<!-- b002603 | furniture | pages [17] -->
m

<!-- b002604 | furniture | pages [17] -->
m

<!-- b002605 | furniture | pages [17] -->
m

<!-- b002606 | furniture | pages [17] -->
m

<!-- b002607 | furniture | pages [17] -->
m

<!-- b002608 | furniture | pages [17] -->
m

<!-- b002609 | furniture | pages [17] -->
m

<!-- b002610 | furniture | pages [17] -->
m

<!-- b002611 | furniture | pages [17] -->
m

<!-- b002612 | furniture | pages [17] -->
m

<!-- b002613 | furniture | pages [17] -->
m

<!-- b002614 | furniture | pages [17] -->
m

<!-- b002615 | furniture | pages [17] -->
m

<!-- b002616 | furniture | pages [17] -->
m

<!-- b002617 | furniture | pages [17] -->
m

<!-- b002618 | furniture | pages [17] -->
m

<!-- b002619 | furniture | pages [17] -->
m

<!-- b002620 | furniture | pages [17] -->
m

<!-- b002621 | furniture | pages [17] -->
m

<!-- b002622 | furniture | pages [17] -->
m

<!-- b002623 | furniture | pages [17] -->
m

<!-- b002624 | furniture | pages [17] -->
m

<!-- b002625 | furniture | pages [17] -->
m

<!-- b002626 | furniture | pages [17] -->
m

<!-- b002627 | furniture | pages [17] -->
m

<!-- b002628 | furniture | pages [17] -->
m

<!-- b002629 | furniture | pages [17] -->
m

<!-- b002630 | furniture | pages [17] -->
m

<!-- b002631 | furniture | pages [17] -->
m

<!-- b002632 | furniture | pages [17] -->
m

<!-- b002633 | furniture | pages [17] -->
m

<!-- b002634 | furniture | pages [17] -->
m

<!-- b002635 | furniture | pages [17] -->
m

<!-- b002636 | furniture | pages [17] -->
m

<!-- b002637 | furniture | pages [17] -->
m

<!-- b002638 | furniture | pages [17] -->
m

<!-- b002639 | furniture | pages [17] -->
m

<!-- b002640 | furniture | pages [17] -->
m

<!-- b002641 | furniture | pages [17] -->
m

<!-- b002642 | furniture | pages [17] -->
m

<!-- b002643 | furniture | pages [17] -->
m

<!-- b002644 | furniture | pages [17] -->
m

<!-- b002645 | furniture | pages [17] -->
m

<!-- b002646 | furniture | pages [17] -->
m

<!-- b002647 | furniture | pages [17] -->
m

<!-- b002648 | furniture | pages [17] -->
m

<!-- b002649 | furniture | pages [17] -->
m

<!-- b002650 | furniture | pages [17] -->
m

<!-- b002651 | furniture | pages [17] -->
m

<!-- b002652 | furniture | pages [17] -->
m

<!-- b002653 | furniture | pages [17] -->
m

<!-- b002654 | furniture | pages [17] -->
m

<!-- b002655 | furniture | pages [17] -->
m

<!-- b002656 | furniture | pages [17] -->
m

<!-- b002657 | furniture | pages [17] -->
m

<!-- b002658 | furniture | pages [17] -->
m

<!-- b002659 | furniture | pages [17] -->
m

<!-- b002660 | furniture | pages [17] -->
m

<!-- b002661 | furniture | pages [17] -->
m

<!-- b002662 | furniture | pages [17] -->
m

<!-- b002663 | furniture | pages [17] -->
m

<!-- b002664 | furniture | pages [17] -->
m

<!-- b002665 | furniture | pages [17] -->
m

<!-- b002666 | furniture | pages [17] -->
m

<!-- b002667 | furniture | pages [17] -->
m

<!-- b002668 | furniture | pages [17] -->
m

<!-- b002669 | furniture | pages [17] -->
m

<!-- b002670 | furniture | pages [17] -->
m

<!-- b002671 | furniture | pages [17] -->
m

<!-- b002672 | furniture | pages [17] -->
m

<!-- b002673 | furniture | pages [17] -->
m

<!-- b002674 | furniture | pages [17] -->
m

<!-- b002675 | furniture | pages [17] -->
m

<!-- b002676 | furniture | pages [17] -->
m

<!-- b002677 | furniture | pages [17] -->
m

<!-- b002678 | furniture | pages [17] -->
m

<!-- b002679 | furniture | pages [17] -->
m

<!-- b002680 | furniture | pages [17] -->
m

<!-- b002681 | furniture | pages [17] -->
m

<!-- b002682 | furniture | pages [17] -->
m

<!-- b002683 | furniture | pages [17] -->
m

<!-- b002684 | furniture | pages [17] -->
m

<!-- b002685 | furniture | pages [17] -->
m

<!-- b002686 | furniture | pages [17] -->
m

<!-- b002687 | furniture | pages [17] -->
m

<!-- b002688 | furniture | pages [17] -->
m

<!-- b002689 | furniture | pages [17] -->
m

<!-- b002690 | furniture | pages [17] -->
m

<!-- b002691 | furniture | pages [17] -->
m

<!-- b002692 | furniture | pages [17] -->
m

<!-- b002693 | furniture | pages [17] -->
m

<!-- b002694 | furniture | pages [17] -->
m

<!-- b002695 | furniture | pages [17] -->
m

<!-- b002696 | furniture | pages [17] -->
m

<!-- b002697 | furniture | pages [17] -->
m

<!-- b002698 | furniture | pages [17] -->
m

<!-- b002699 | furniture | pages [17] -->
m

<!-- b002700 | furniture | pages [17] -->
m

<!-- b002701 | furniture | pages [17] -->
m

<!-- b002702 | furniture | pages [17] -->
m

<!-- b002703 | furniture | pages [17] -->
m

<!-- b002704 | furniture | pages [17] -->
m

<!-- b002705 | furniture | pages [17] -->
m

<!-- b002706 | furniture | pages [17] -->
m

<!-- b002707 | furniture | pages [17] -->
m

<!-- b002708 | furniture | pages [17] -->
m

<!-- b002709 | furniture | pages [17] -->
m

<!-- b002710 | furniture | pages [17] -->
m

<!-- b002711 | furniture | pages [17] -->
m

<!-- b002712 | furniture | pages [17] -->
m

<!-- b002713 | furniture | pages [17] -->
m

<!-- b002714 | furniture | pages [17] -->
m

<!-- b002715 | furniture | pages [17] -->
m

<!-- b002716 | furniture | pages [17] -->
m

<!-- b002717 | furniture | pages [17] -->
m

<!-- b002718 | furniture | pages [17] -->
m

<!-- b002719 | furniture | pages [17] -->
m

<!-- b002720 | furniture | pages [17] -->
m

<!-- b002721 | furniture | pages [17] -->
m

<!-- b002722 | furniture | pages [17] -->
m

<!-- b002723 | furniture | pages [17] -->
m

<!-- b002724 | furniture | pages [17] -->
m

<!-- b002725 | furniture | pages [17] -->
m

<!-- b002726 | furniture | pages [17] -->
m

<!-- b002727 | furniture | pages [17] -->
m

<!-- b002728 | furniture | pages [17] -->
m

<!-- b002729 | furniture | pages [17] -->
m

<!-- b002730 | furniture | pages [17] -->
m

<!-- b002731 | furniture | pages [17] -->
m

<!-- b002732 | furniture | pages [17] -->
m

<!-- b002733 | furniture | pages [17] -->
m

<!-- b002734 | furniture | pages [17] -->
m

<!-- b002735 | furniture | pages [17] -->
m

<!-- b002736 | furniture | pages [17] -->
m

<!-- b002737 | furniture | pages [17] -->
m

<!-- b002738 | furniture | pages [17] -->
m

<!-- b002739 | furniture | pages [17] -->
m

<!-- b002740 | furniture | pages [17] -->
m

<!-- b002741 | furniture | pages [17] -->
m

<!-- b002742 | furniture | pages [17] -->
m

<!-- b002743 | furniture | pages [17] -->
m

<!-- b002744 | furniture | pages [17] -->
m

<!-- b002745 | furniture | pages [17] -->
m

<!-- b002746 | furniture | pages [17] -->
m

<!-- b002747 | furniture | pages [17] -->
m

<!-- b002748 | furniture | pages [17] -->
m

<!-- b002749 | furniture | pages [17] -->
m

<!-- b002750 | furniture | pages [17] -->
m

<!-- b002751 | furniture | pages [17] -->
m

<!-- b002752 | furniture | pages [17] -->
m

<!-- b002753 | furniture | pages [17] -->
m

<!-- b002754 | furniture | pages [17] -->
m

<!-- b002755 | furniture | pages [17] -->
m

<!-- b002756 | furniture | pages [17] -->
m

<!-- b002757 | furniture | pages [17] -->
m

<!-- b002758 | furniture | pages [17] -->
m

<!-- b002759 | furniture | pages [17] -->
m

<!-- b002760 | furniture | pages [17] -->
m

<!-- b002761 | furniture | pages [17] -->
m

<!-- b002762 | furniture | pages [17] -->
m

<!-- b002763 | furniture | pages [17] -->
m

<!-- b002764 | furniture | pages [17] -->
m

<!-- b002765 | furniture | pages [17] -->
m

<!-- b002766 | furniture | pages [17] -->
m

<!-- b002767 | furniture | pages [17] -->
m

<!-- b002768 | furniture | pages [17] -->
m

<!-- b002769 | furniture | pages [17] -->
m

<!-- b002770 | furniture | pages [17] -->
m

<!-- b002771 | furniture | pages [17] -->
m

<!-- b002772 | furniture | pages [17] -->
m

<!-- b002773 | furniture | pages [17] -->
m

<!-- b002774 | furniture | pages [17] -->
m

<!-- b002775 | furniture | pages [17] -->
m

<!-- b002776 | furniture | pages [17] -->
m

<!-- b002777 | furniture | pages [17] -->
m

<!-- b002778 | furniture | pages [17] -->
m

<!-- b002779 | furniture | pages [17] -->
m

<!-- b002780 | furniture | pages [17] -->
m

<!-- b002781 | furniture | pages [17] -->
m

<!-- b002782 | furniture | pages [17] -->
m

<!-- b002783 | furniture | pages [17] -->
m

<!-- b002784 | furniture | pages [17] -->
m

<!-- b002785 | furniture | pages [17] -->
m

<!-- b002786 | furniture | pages [17] -->
m

<!-- b002787 | furniture | pages [17] -->
m

<!-- b002788 | furniture | pages [17] -->
m

<!-- b002789 | furniture | pages [17] -->
m

<!-- b002790 | furniture | pages [17] -->
m

<!-- b002791 | furniture | pages [17] -->
m

<!-- b002792 | furniture | pages [17] -->
m

<!-- b002793 | furniture | pages [17] -->
m

<!-- b002794 | furniture | pages [17] -->
m

<!-- b002795 | furniture | pages [17] -->
m

<!-- b002796 | furniture | pages [17] -->
m

<!-- b002797 | furniture | pages [17] -->
m

<!-- b002798 | furniture | pages [17] -->
m

<!-- b002799 | furniture | pages [17] -->
m

<!-- b002800 | furniture | pages [17] -->
m

<!-- b002801 | furniture | pages [17] -->
m

<!-- b002802 | furniture | pages [17] -->
m

<!-- b002803 | furniture | pages [17] -->
m

<!-- b002804 | furniture | pages [17] -->
m

<!-- b002805 | furniture | pages [17] -->
m

<!-- b002806 | furniture | pages [17] -->
m

<!-- b002807 | furniture | pages [17] -->
m

<!-- b002808 | furniture | pages [17] -->
m

<!-- b002809 | furniture | pages [17] -->
m

<!-- b002810 | furniture | pages [17] -->
m

<!-- b002811 | furniture | pages [17] -->
m

<!-- b002812 | furniture | pages [17] -->
m

<!-- b002813 | furniture | pages [17] -->
m

<!-- b002814 | furniture | pages [17] -->
m

<!-- b002815 | furniture | pages [17] -->
m

<!-- b002816 | furniture | pages [17] -->
m

<!-- b002817 | furniture | pages [17] -->
m

<!-- b002818 | furniture | pages [17] -->
m

<!-- b002819 | furniture | pages [17] -->
m

<!-- b002820 | furniture | pages [17] -->
m

<!-- b002821 | furniture | pages [17] -->
m

<!-- b002822 | furniture | pages [17] -->
m

<!-- b002823 | furniture | pages [17] -->
m

<!-- b002824 | furniture | pages [17] -->
m

<!-- b002825 | furniture | pages [17] -->
m

<!-- b002826 | furniture | pages [17] -->
m

<!-- b002827 | furniture | pages [17] -->
m

<!-- b002828 | furniture | pages [17] -->
m

<!-- b002829 | furniture | pages [17] -->
m

<!-- b002830 | furniture | pages [17] -->
m

<!-- b002831 | furniture | pages [17] -->
m

<!-- b002832 | furniture | pages [17] -->
m

<!-- b002833 | furniture | pages [17] -->
m

<!-- b002834 | furniture | pages [17] -->
m

<!-- b002835 | furniture | pages [17] -->
m

<!-- b002836 | furniture | pages [17] -->
m

<!-- b002837 | furniture | pages [17] -->
m

<!-- b002838 | furniture | pages [17] -->
m

<!-- b002839 | furniture | pages [17] -->
m

<!-- b002840 | furniture | pages [17] -->
m

<!-- b002841 | furniture | pages [17] -->
m

<!-- b002842 | furniture | pages [17] -->
m

<!-- b002843 | furniture | pages [17] -->
m

<!-- b002844 | furniture | pages [17] -->
m

<!-- b002845 | furniture | pages [17] -->
m

<!-- b002846 | furniture | pages [17] -->
m

<!-- b002847 | furniture | pages [17] -->
m

<!-- b002848 | furniture | pages [17] -->
m

<!-- b002849 | furniture | pages [17] -->
m

<!-- b002850 | furniture | pages [17] -->
m

<!-- b002851 | furniture | pages [17] -->
m

<!-- b002852 | furniture | pages [17] -->
m

<!-- b002853 | furniture | pages [17] -->
m

<!-- b002854 | furniture | pages [17] -->
m

<!-- b002855 | furniture | pages [17] -->
m

<!-- b002856 | furniture | pages [17] -->
m

<!-- b002857 | furniture | pages [17] -->
m

<!-- b002858 | furniture | pages [17] -->
m

<!-- b002859 | furniture | pages [17] -->
m

<!-- b002860 | furniture | pages [17] -->
m

<!-- b002861 | furniture | pages [17] -->
m

<!-- b002862 | furniture | pages [17] -->
m

<!-- b002863 | furniture | pages [17] -->
m

<!-- b002864 | furniture | pages [17] -->
m

<!-- b002865 | furniture | pages [17] -->
m

<!-- b002866 | furniture | pages [17] -->
m

<!-- b002867 | furniture | pages [17] -->
m

<!-- b002868 | furniture | pages [17] -->
m

<!-- b002869 | furniture | pages [17] -->
m

<!-- b002870 | furniture | pages [17] -->
m

<!-- b002871 | furniture | pages [17] -->
m

<!-- b002872 | furniture | pages [17] -->
m

<!-- b002873 | furniture | pages [17] -->
m

<!-- b002874 | furniture | pages [17] -->
m

<!-- b002875 | furniture | pages [17] -->
m

<!-- b002876 | furniture | pages [17] -->
m

<!-- b002877 | furniture | pages [17] -->
m

<!-- b002878 | furniture | pages [17] -->
m

<!-- b002879 | furniture | pages [17] -->
m

<!-- b002880 | furniture | pages [17] -->
m

<!-- b002881 | furniture | pages [17] -->
m

<!-- b002882 | furniture | pages [17] -->
m

<!-- b002883 | furniture | pages [17] -->
m

<!-- b002884 | furniture | pages [17] -->
m

<!-- b002885 | furniture | pages [17] -->
m

<!-- b002886 | furniture | pages [17] -->
m

<!-- b002887 | furniture | pages [17] -->
m

<!-- b002888 | furniture | pages [17] -->
m

<!-- b002889 | furniture | pages [17] -->
m

<!-- b002890 | furniture | pages [17] -->
m

<!-- b002891 | furniture | pages [17] -->
m

<!-- b002892 | furniture | pages [17] -->
m

<!-- b002893 | furniture | pages [17] -->
m

<!-- b002894 | furniture | pages [17] -->
m

<!-- b002895 | furniture | pages [17] -->
m

<!-- b002896 | furniture | pages [17] -->
m

<!-- b002897 | furniture | pages [17] -->
m

<!-- b002898 | furniture | pages [17] -->
m

<!-- b002899 | furniture | pages [17] -->
m

<!-- b002900 | furniture | pages [17] -->
m

<!-- b002901 | furniture | pages [17] -->
m

<!-- b002902 | furniture | pages [17] -->
m

<!-- b002903 | furniture | pages [17] -->
m

<!-- b002904 | furniture | pages [17] -->
m

<!-- b002905 | furniture | pages [17] -->
m

<!-- b002906 | furniture | pages [17] -->
m

<!-- b002907 | furniture | pages [17] -->
m

<!-- b002908 | furniture | pages [17] -->
m

<!-- b002909 | furniture | pages [18] -->
Team # 2503268

<!-- b002910 | furniture | pages [18] -->
Page 16 of 24

<!-- b002911 | caption | pages [18] -->
Figure 7: heatmap of weights

<!-- b002912 | heading | pages [18] -->
8 Results and Discussion

<!-- b002913 | prose | pages [18] -->
The ﬁtting results of the proposed model are shown in Figure 8, which compares the modeled and observed data for glacier health (H), tourist numbers (N), and hotel tax revenue (T). The red markers represent the observed data, while the blue dashed lines depict the model’s predictions. Overall, the model demonstrates a strong ability to capture the dynamic relationships among the three variables, with certain limitations in speciﬁc scenarios.

<!-- b002914 | caption | pages [18] -->
Figure 8: H, N, T comparisons

<!-- b002915 | prose | pages [18] -->
Based on the intrinsic relationships derived from the HNT data (glacier health, tourism numbers, and economic revenue) between time steps 10 and 19, we developed a quantiﬁable policy evaluation model. By integrating policy parameters (µ1, µ2, µ3, µ4, µ5) into the model, we identiﬁed the intersec- tion between the feasible policy region and the directional optimization boundary. This intersection represents the controllable scope of policies under current conditions. From this range, the model samples points and selects the one yielding the highest evaluation score as the optimal strategy.

<!-- b002916 | prose | pages [18, 19] -->
关注数学模型 As the data of 2019 is the latest we have, we can approximate the situations then as those of now. As calculated, the best combination of allocation and policy is [0.15, 0.10, 0.35, 0.10, 0.30] and [↓3, 3, 4], which represents an allocation focused on safety and waste management and a policy highlighting 微信公众号：数学模型 comprehensive and balanced development, with a ﬁnal score of 0.6894.

<!-- b002917 | furniture | pages [18] -->
2

<!-- b002918 | furniture | pages [18] -->
MATHmodels

<!-- b002919 | furniture | pages [18] -->
获取更多资讯

<!-- b002920 | furniture | pages [19] -->
Team # 2503268

<!-- b002921 | furniture | pages [19] -->
Page 17 of 24

<!-- b002923 | prose | pages [19] -->
We set a baseline of strategies representing a fairly average strategy. Sample some points of speciﬁc time and output the scores after applying our model and baseline and make a comparison, we draw a bar chart:

<!-- b002924 | prose | pages [19] -->
微信号：MATHmodels

<!-- b002925 | caption | pages [19] -->
Figure 9: Baseline & Model Scores

<!-- b002926 | prose | pages [19] -->
According to the ﬁgure, the model-determined strategies make a diﬀerence, performing better than baseline. Under ideal circumstances, our model helps the government with making better decisions.

<!-- b002927 | heading | pages [19] -->
9 Sensitivity Analysis

<!-- b002928 | heading | pages [19] -->
9.1 Qualitative analysis: Morris Method

<!-- b002929 | prose | pages [19] -->
In order to understand which parameters predominantly shape the model outputs and where the strongest nonlinear interactions may arise, we perform a Morris global sensitivity analysis on two key aspects of our framework: (i) the ODE parameters {k1, . . . , k11}, which govern how H, N, and T evolve over time, and (ii) the evaluation model, which combines policy-related variables such as µi, ε, and ϱ1 into a single sustainability metric.

<!-- b002930 | caption | pages [19] -->
Figure 10 illustrates these two Morris analyses side by side. The left panel (a) focuses on the ODE

<!-- b002931 | prose | pages [19] -->
parameters, treating the residual ﬁtting cost as the model’s single-output measure, while the right panel (b) targets the evaluation function. In both panels, the horizontal axis µ↔represents each parameter’s main eﬀect: a larger µ↔implies that changes in that parameter lead to larger variations in the output on average. Meanwhile, the vertical axis ω captures interaction or nonlinearity: the higher the ω, the more the parameter’s eﬀect ﬂuctuates across diﬀerent combinations of other parameters.

<!-- b002932 | prose | pages [19, 20] -->
In panel (a), k2 and k6 show the largest µ↔among ODE parameters, signiﬁcantly impacting model m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ﬁt. Their moderately high ω suggests potential interactions or context-dependent eﬀects. Conversely, k10 and k1 show minimal eﬀects and nonlinearity.

<!-- b002933 | furniture | pages [19] -->
m

<!-- b002934 | furniture | pages [19] -->
m

<!-- b002935 | furniture | pages [19] -->
m

<!-- b002936 | furniture | pages [19] -->
m

<!-- b002937 | furniture | pages [19] -->
m

<!-- b002938 | furniture | pages [19] -->
m

<!-- b002939 | furniture | pages [19] -->
m

<!-- b002940 | furniture | pages [19] -->
m

<!-- b002941 | furniture | pages [19] -->
m

<!-- b002942 | furniture | pages [19] -->
m

<!-- b002943 | furniture | pages [19] -->
m

<!-- b002944 | furniture | pages [19] -->
m

<!-- b002945 | furniture | pages [19] -->
m

<!-- b002946 | furniture | pages [19] -->
m

<!-- b002947 | furniture | pages [19] -->
m

<!-- b002948 | furniture | pages [19] -->
m

<!-- b002949 | furniture | pages [19] -->
m

<!-- b002950 | furniture | pages [19] -->
m

<!-- b002951 | furniture | pages [19] -->
m

<!-- b002952 | furniture | pages [19] -->
m

<!-- b002953 | furniture | pages [19] -->
m

<!-- b002954 | furniture | pages [19] -->
m

<!-- b002955 | furniture | pages [19] -->
m

<!-- b002956 | furniture | pages [19] -->
m

<!-- b002957 | furniture | pages [19] -->
m

<!-- b002958 | furniture | pages [19] -->
m

<!-- b002959 | furniture | pages [19] -->
m

<!-- b002960 | furniture | pages [19] -->
m

<!-- b002961 | furniture | pages [19] -->
m

<!-- b002962 | furniture | pages [19] -->
m

<!-- b002963 | furniture | pages [19] -->
m

<!-- b002964 | furniture | pages [19] -->
m

<!-- b002965 | furniture | pages [19] -->
m

<!-- b002966 | furniture | pages [19] -->
m

<!-- b002967 | furniture | pages [19] -->
m

<!-- b002968 | furniture | pages [19] -->
m

<!-- b002969 | furniture | pages [19] -->
m

<!-- b002970 | furniture | pages [19] -->
m

<!-- b002971 | furniture | pages [19] -->
m

<!-- b002972 | furniture | pages [19] -->
m

<!-- b002973 | furniture | pages [19] -->
m

<!-- b002974 | furniture | pages [19] -->
m

<!-- b002975 | furniture | pages [19] -->
m

<!-- b002976 | furniture | pages [19] -->
m

<!-- b002977 | furniture | pages [19] -->
m

<!-- b002978 | furniture | pages [19] -->
m

<!-- b002979 | furniture | pages [19] -->
m

<!-- b002980 | furniture | pages [19] -->
m

<!-- b002981 | furniture | pages [19] -->
m

<!-- b002982 | furniture | pages [19] -->
m

<!-- b002983 | furniture | pages [19] -->
m

<!-- b002984 | furniture | pages [19] -->
m

<!-- b002985 | furniture | pages [19] -->
m

<!-- b002986 | furniture | pages [19] -->
m

<!-- b002987 | furniture | pages [19] -->
m

<!-- b002988 | furniture | pages [19] -->
m

<!-- b002989 | furniture | pages [19] -->
m

<!-- b002990 | furniture | pages [19] -->
m

<!-- b002991 | furniture | pages [19] -->
m

<!-- b002992 | furniture | pages [19] -->
m

<!-- b002993 | furniture | pages [19] -->
m

<!-- b002994 | furniture | pages [19] -->
m

<!-- b002995 | furniture | pages [19] -->
m

<!-- b002996 | furniture | pages [19] -->
m

<!-- b002997 | furniture | pages [19] -->
m

<!-- b002998 | furniture | pages [19] -->
m

<!-- b002999 | furniture | pages [19] -->
m

<!-- b003000 | furniture | pages [19] -->
m

<!-- b003001 | furniture | pages [19] -->
m

<!-- b003002 | furniture | pages [19] -->
m

<!-- b003003 | furniture | pages [19] -->
m

<!-- b003004 | furniture | pages [19] -->
m

<!-- b003005 | furniture | pages [19] -->
m

<!-- b003006 | furniture | pages [19] -->
m

<!-- b003007 | furniture | pages [19] -->
m

<!-- b003008 | furniture | pages [19] -->
m

<!-- b003009 | furniture | pages [19] -->
m

<!-- b003010 | furniture | pages [19] -->
m

<!-- b003011 | furniture | pages [19] -->
m

<!-- b003012 | furniture | pages [19] -->
m

<!-- b003013 | furniture | pages [19] -->
m

<!-- b003014 | furniture | pages [19] -->
m

<!-- b003015 | furniture | pages [19] -->
m

<!-- b003016 | furniture | pages [19] -->
m

<!-- b003017 | furniture | pages [19] -->
m

<!-- b003018 | furniture | pages [19] -->
m

<!-- b003019 | furniture | pages [19] -->
m

<!-- b003020 | furniture | pages [19] -->
m

<!-- b003021 | furniture | pages [19] -->
m

<!-- b003022 | furniture | pages [19] -->
m

<!-- b003023 | furniture | pages [19] -->
m

<!-- b003024 | furniture | pages [19] -->
m

<!-- b003025 | furniture | pages [19] -->
m

<!-- b003026 | furniture | pages [19] -->
m

<!-- b003027 | furniture | pages [19] -->
m

<!-- b003028 | furniture | pages [19] -->
m

<!-- b003029 | furniture | pages [19] -->
m

<!-- b003030 | furniture | pages [19] -->
m

<!-- b003031 | furniture | pages [19] -->
m

<!-- b003032 | furniture | pages [19] -->
m

<!-- b003033 | furniture | pages [19] -->
m

<!-- b003034 | furniture | pages [19] -->
m

<!-- b003035 | furniture | pages [19] -->
m

<!-- b003036 | furniture | pages [19] -->
m

<!-- b003037 | furniture | pages [19] -->
m

<!-- b003038 | furniture | pages [19] -->
m

<!-- b003039 | furniture | pages [19] -->
m

<!-- b003040 | furniture | pages [19] -->
m

<!-- b003041 | furniture | pages [19] -->
m

<!-- b003042 | furniture | pages [19] -->
m

<!-- b003043 | furniture | pages [19] -->
m

<!-- b003044 | furniture | pages [19] -->
m

<!-- b003045 | furniture | pages [19] -->
m

<!-- b003046 | furniture | pages [19] -->
m

<!-- b003047 | furniture | pages [19] -->
m

<!-- b003048 | furniture | pages [19] -->
m

<!-- b003049 | furniture | pages [19] -->
m

<!-- b003050 | furniture | pages [19] -->
m

<!-- b003051 | furniture | pages [19] -->
m

<!-- b003052 | furniture | pages [19] -->
m

<!-- b003053 | furniture | pages [19] -->
m

<!-- b003054 | furniture | pages [19] -->
m

<!-- b003055 | furniture | pages [19] -->
m

<!-- b003056 | furniture | pages [19] -->
m

<!-- b003057 | furniture | pages [19] -->
m

<!-- b003058 | furniture | pages [19] -->
m

<!-- b003059 | furniture | pages [19] -->
m

<!-- b003060 | furniture | pages [19] -->
m

<!-- b003061 | furniture | pages [19] -->
m

<!-- b003062 | furniture | pages [19] -->
m

<!-- b003063 | furniture | pages [19] -->
m

<!-- b003064 | furniture | pages [19] -->
m

<!-- b003065 | furniture | pages [19] -->
m

<!-- b003066 | furniture | pages [19] -->
m

<!-- b003067 | furniture | pages [19] -->
m

<!-- b003068 | furniture | pages [19] -->
m

<!-- b003069 | furniture | pages [19] -->
m

<!-- b003070 | furniture | pages [19] -->
m

<!-- b003071 | furniture | pages [19] -->
m

<!-- b003072 | furniture | pages [19] -->
m

<!-- b003073 | furniture | pages [19] -->
m

<!-- b003074 | furniture | pages [19] -->
m

<!-- b003075 | furniture | pages [19] -->
m

<!-- b003076 | furniture | pages [19] -->
m

<!-- b003077 | furniture | pages [19] -->
m

<!-- b003078 | furniture | pages [19] -->
m

<!-- b003079 | furniture | pages [19] -->
m

<!-- b003080 | furniture | pages [19] -->
m

<!-- b003081 | furniture | pages [19] -->
m

<!-- b003082 | furniture | pages [19] -->
m

<!-- b003083 | furniture | pages [19] -->
m

<!-- b003084 | furniture | pages [19] -->
m

<!-- b003085 | furniture | pages [19] -->
m

<!-- b003086 | furniture | pages [19] -->
m

<!-- b003087 | furniture | pages [19] -->
m

<!-- b003088 | furniture | pages [19] -->
m

<!-- b003089 | furniture | pages [19] -->
m

<!-- b003090 | furniture | pages [19] -->
m

<!-- b003091 | furniture | pages [19] -->
m

<!-- b003092 | furniture | pages [19] -->
m

<!-- b003093 | furniture | pages [19] -->
m

<!-- b003094 | furniture | pages [19] -->
m

<!-- b003095 | furniture | pages [19] -->
m

<!-- b003096 | furniture | pages [19] -->
m

<!-- b003097 | furniture | pages [19] -->
m

<!-- b003098 | furniture | pages [19] -->
m

<!-- b003099 | furniture | pages [19] -->
m

<!-- b003100 | furniture | pages [19] -->
m

<!-- b003101 | furniture | pages [19] -->
m

<!-- b003102 | furniture | pages [19] -->
m

<!-- b003103 | furniture | pages [19] -->
m

<!-- b003104 | furniture | pages [19] -->
m

<!-- b003105 | furniture | pages [19] -->
m

<!-- b003106 | furniture | pages [19] -->
m

<!-- b003107 | furniture | pages [19] -->
m

<!-- b003108 | furniture | pages [19] -->
m

<!-- b003109 | furniture | pages [19] -->
m

<!-- b003110 | furniture | pages [19] -->
m

<!-- b003111 | furniture | pages [19] -->
m

<!-- b003112 | furniture | pages [19] -->
m

<!-- b003113 | furniture | pages [19] -->
m

<!-- b003114 | furniture | pages [19] -->
m

<!-- b003115 | furniture | pages [19] -->
m

<!-- b003116 | furniture | pages [19] -->
m

<!-- b003117 | furniture | pages [19] -->
m

<!-- b003118 | furniture | pages [19] -->
m

<!-- b003119 | furniture | pages [19] -->
m

<!-- b003120 | furniture | pages [19] -->
m

<!-- b003121 | furniture | pages [19] -->
m

<!-- b003122 | furniture | pages [19] -->
m

<!-- b003123 | furniture | pages [19] -->
m

<!-- b003124 | furniture | pages [19] -->
m

<!-- b003125 | furniture | pages [19] -->
m

<!-- b003126 | furniture | pages [19] -->
m

<!-- b003127 | furniture | pages [19] -->
m

<!-- b003128 | furniture | pages [19] -->
m

<!-- b003129 | furniture | pages [19] -->
m

<!-- b003130 | furniture | pages [19] -->
m

<!-- b003131 | furniture | pages [19] -->
m

<!-- b003132 | furniture | pages [19] -->
m

<!-- b003133 | furniture | pages [19] -->
m

<!-- b003134 | furniture | pages [19] -->
m

<!-- b003135 | furniture | pages [19] -->
m

<!-- b003136 | furniture | pages [19] -->
m

<!-- b003137 | furniture | pages [19] -->
m

<!-- b003138 | furniture | pages [19] -->
m

<!-- b003139 | furniture | pages [19] -->
m

<!-- b003140 | furniture | pages [19] -->
m

<!-- b003141 | furniture | pages [19] -->
m

<!-- b003142 | furniture | pages [19] -->
m

<!-- b003143 | furniture | pages [19] -->
m

<!-- b003144 | furniture | pages [19] -->
m

<!-- b003145 | furniture | pages [19] -->
m

<!-- b003146 | furniture | pages [19] -->
m

<!-- b003147 | furniture | pages [19] -->
m

<!-- b003148 | furniture | pages [19] -->
m

<!-- b003149 | furniture | pages [19] -->
m

<!-- b003150 | furniture | pages [19] -->
m

<!-- b003151 | furniture | pages [19] -->
m

<!-- b003152 | furniture | pages [19] -->
m

<!-- b003153 | furniture | pages [19] -->
m

<!-- b003154 | furniture | pages [19] -->
m

<!-- b003155 | furniture | pages [19] -->
m

<!-- b003156 | furniture | pages [19] -->
m

<!-- b003157 | furniture | pages [19] -->
m

<!-- b003158 | furniture | pages [19] -->
m

<!-- b003159 | furniture | pages [19] -->
m

<!-- b003160 | furniture | pages [19] -->
m

<!-- b003161 | furniture | pages [19] -->
m

<!-- b003162 | furniture | pages [19] -->
m

<!-- b003163 | furniture | pages [19] -->
m

<!-- b003164 | furniture | pages [19] -->
m

<!-- b003165 | furniture | pages [19] -->
m

<!-- b003166 | furniture | pages [19] -->
m

<!-- b003167 | furniture | pages [19] -->
m

<!-- b003168 | furniture | pages [19] -->
m

<!-- b003169 | furniture | pages [19] -->
m

<!-- b003170 | furniture | pages [19] -->
m

<!-- b003171 | furniture | pages [19] -->
m

<!-- b003172 | furniture | pages [19] -->
m

<!-- b003173 | furniture | pages [19] -->
m

<!-- b003174 | furniture | pages [19] -->
m

<!-- b003175 | furniture | pages [19] -->
m

<!-- b003176 | furniture | pages [19] -->
m

<!-- b003177 | furniture | pages [19] -->
m

<!-- b003178 | furniture | pages [19] -->
m

<!-- b003179 | furniture | pages [19] -->
m

<!-- b003180 | furniture | pages [19] -->
m

<!-- b003181 | furniture | pages [19] -->
m

<!-- b003182 | furniture | pages [19] -->
m

<!-- b003183 | furniture | pages [19] -->
m

<!-- b003184 | furniture | pages [19] -->
m

<!-- b003185 | furniture | pages [19] -->
m

<!-- b003186 | furniture | pages [19] -->
m

<!-- b003187 | furniture | pages [19] -->
m

<!-- b003188 | furniture | pages [19] -->
m

<!-- b003189 | furniture | pages [19] -->
m

<!-- b003190 | furniture | pages [19] -->
m

<!-- b003191 | furniture | pages [19] -->
m

<!-- b003192 | furniture | pages [19] -->
m

<!-- b003193 | furniture | pages [19] -->
m

<!-- b003194 | furniture | pages [19] -->
m

<!-- b003195 | furniture | pages [19] -->
m

<!-- b003196 | furniture | pages [19] -->
m

<!-- b003197 | furniture | pages [19] -->
m

<!-- b003198 | furniture | pages [19] -->
m

<!-- b003199 | furniture | pages [19] -->
m

<!-- b003200 | furniture | pages [19] -->
m

<!-- b003201 | furniture | pages [19] -->
m

<!-- b003202 | furniture | pages [19] -->
m

<!-- b003203 | furniture | pages [19] -->
m

<!-- b003204 | furniture | pages [19] -->
m

<!-- b003205 | furniture | pages [19] -->
m

<!-- b003206 | furniture | pages [19] -->
m

<!-- b003207 | furniture | pages [19] -->
m

<!-- b003208 | furniture | pages [19] -->
m

<!-- b003209 | furniture | pages [19] -->
m

<!-- b003210 | furniture | pages [19] -->
m

<!-- b003211 | furniture | pages [19] -->
m

<!-- b003212 | furniture | pages [19] -->
m

<!-- b003213 | furniture | pages [19] -->
m

<!-- b003214 | furniture | pages [19] -->
m

<!-- b003215 | furniture | pages [19] -->
m

<!-- b003216 | furniture | pages [19] -->
m

<!-- b003217 | furniture | pages [19] -->
m

<!-- b003218 | furniture | pages [19] -->
m

<!-- b003219 | furniture | pages [19] -->
m

<!-- b003220 | furniture | pages [19] -->
m

<!-- b003221 | furniture | pages [19] -->
m

<!-- b003222 | furniture | pages [19] -->
m

<!-- b003223 | furniture | pages [19] -->
m

<!-- b003224 | furniture | pages [19] -->
m

<!-- b003225 | furniture | pages [19] -->
m

<!-- b003226 | furniture | pages [19] -->
m

<!-- b003227 | furniture | pages [19] -->
m

<!-- b003228 | furniture | pages [19] -->
m

<!-- b003229 | furniture | pages [19] -->
m

<!-- b003230 | furniture | pages [19] -->
m

<!-- b003231 | furniture | pages [19] -->
m

<!-- b003232 | furniture | pages [19] -->
m

<!-- b003233 | furniture | pages [19] -->
m

<!-- b003234 | furniture | pages [19] -->
m

<!-- b003235 | furniture | pages [19] -->
m

<!-- b003236 | furniture | pages [19] -->
m

<!-- b003237 | furniture | pages [19] -->
m

<!-- b003238 | furniture | pages [19] -->
m

<!-- b003239 | furniture | pages [19] -->
m

<!-- b003240 | furniture | pages [19] -->
m

<!-- b003241 | furniture | pages [19] -->
m

<!-- b003242 | furniture | pages [19] -->
m

<!-- b003243 | furniture | pages [19] -->
m

<!-- b003244 | furniture | pages [19] -->
m

<!-- b003245 | furniture | pages [19] -->
m

<!-- b003246 | furniture | pages [19] -->
m

<!-- b003247 | furniture | pages [19] -->
m

<!-- b003248 | furniture | pages [19] -->
m

<!-- b003249 | furniture | pages [19] -->
m

<!-- b003250 | furniture | pages [19] -->
m

<!-- b003251 | furniture | pages [19] -->
m

<!-- b003252 | furniture | pages [19] -->
m

<!-- b003253 | furniture | pages [19] -->
m

<!-- b003254 | furniture | pages [19] -->
m

<!-- b003255 | furniture | pages [19] -->
m

<!-- b003256 | furniture | pages [19] -->
m

<!-- b003257 | furniture | pages [20] -->
Team # 2503268

<!-- b003258 | furniture | pages [20] -->
Page 18 of 24

<!-- b003259 | caption | pages [20] -->
Figure 10: sensitivity analysis

<!-- b003261 | prose | pages [20] -->
Turning to panel (b), we observe that µ5 emerges with both a large µ↔and a relatively high ω in the evaluation function’s sensitivity plot, indicating a strong direct eﬀect on the score and pronounced variability under diﬀerent conditions. Other variables like ε or µ2 remain clustered near the origin, suggesting they exert less inﬂuence within the current parameter bounds. As in last year’s analysis, we conclude that parameters with high µ↔deserve focused calibration or policy-level prioritization, while those with large ω should be investigated for potential nonlinear or combined eﬀects.

<!-- b003262 | prose | pages [20] -->
Overall, these ﬁndings guide us in prioritizing certain ODE coeﬃcients (e.g., k2, k6) for reﬁned data collection or modeling eﬀorts, while also highlighting which policy parameters (e.g., µ5) most strongly aﬀect the sustainability outcome. The interplay between large µ↔and ω is especially important for anticipating how small changes in one parameter might yield disproportionately large or context- dependent shifts in ﬁnal model results.

<!-- b003263 | heading | pages [20] -->
9.2 Quantitative analysis: Local Sensitivity Analysis

<!-- b003264 | prose | pages [20] -->
Beyond the Morris global sensitivity, we have also conducted a local sensitivity analysis to evalu- ate how small perturbations in each parameter pi aﬀect the ﬁnal score ↼Score ↼pi . Table 7 shows a condensed version of the partial derivatives for selected top parameters, while Figure 7 provides a bar chart sum- marizing the average absolute sensitivity across multiple µ settings.

<!-- b003265 | prose | pages [20] -->
In general, parameters such as ϱ, r1, and k5 exhibit consistently large partial derivatives with respect to Score, indicating that even small changes can signiﬁcantly alter the sustainability metric. This aligns well with the global Morris analysis, in which these parameters also showed large µ↔values. On the policy side, µ5 retains notable sensitivity, reinforcing the idea that certain intervention intensities or policy measures (µ5) can drastically shift overall outcomes on log scale.

<!-- b003266 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型

<!-- b003267 | furniture | pages [20] -->
2

<!-- b003268 | furniture | pages [20] -->
MATHmodels

<!-- b003269 | furniture | pages [20] -->
获取更多资讯

<!-- b003270 | furniture | pages [21] -->
Team # 2503268

<!-- b003271 | furniture | pages [21] -->
Page 19 of 24

<!-- b003273 | caption | pages [21] -->
Figure 11: Top parameters by mean absolute local sensitivity with respect to Score. Error bars repre-

<!-- b003274 | prose | pages [21] -->
sent standard deviation across diﬀerent µ sets.

<!-- b003275 | heading | pages [21] -->
10 Reimagining Big Sur

<!-- b003276 | prose | pages [21] -->
微信号：MATHmodels

<!-- b003277 | heading | pages [21] -->
10.1 Fundamental Information

<!-- b003278 | prose | pages [21] -->
Overtourism is inherently site-speciﬁc [9], as each destination has unique contributing factors. However, various response strategies have been proposed or implemented to address these challenges. Our developed model enhances decision-making for better evaluation outcomes, and we have selected Big Sur, California, to validate its eﬀectiveness.

<!-- b003279 | prose | pages [21] -->
Big Sur, renowned for its rugged coastline, redwood forests, and scenic Highway 1, attracts mil- lions of visitors annually. However, its popularity presents sustainability challenges, exacerbated by natural disasters, road closures, and overtourism pressures. These issues raise critical concerns for both travelers and the tourism industry regarding the long-term accessibility and sustainability of this iconic destination.

<!-- b003280 | prose | pages [21] -->
In our data selection process, we have chosen Pfeiﬀer Big Sur State Park, a renowned tourist desti- nation, as a representative site for the Big Sur Section. To obtain relevant data on tourist numbers and economic growth, we utilized the annually published California State Park System Statistical Report. For visitor attendance, we aggregated the ﬁgures from Paid Day Use, Free Day Use, and Camping categories to represent the annual number of tourists in Pfeiﬀer Big Sur, denoted as NSur. Similarly, for government revenue, we calculated the total annual revenue generated from tourism in Pfeiﬀer Big Sur, denoted as TSur, by summing the income from User Fees, Concessions, and Miscellaneous revenue sources.

<!-- b003281 | prose | pages [21, 22] -->
For the representation of environmental factors, we adopt a methodology inspired by the inno- vative approach of Cheryl J. Hapke and Krystal R. Green [10], who assessed the rates of landsliding and cliﬀretreat along the Big Sur coast by measuring crucial baseline indicators. Similarly, we incor- porate insights from the work of Zuzanna M. Swirad [11], who analyzed spatial and temporal trends m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Left Column Right Column ∂Score ∂Score Std Mean Rank Std Rank Param Param Mean ∂pi ∂pi 3.945 1.366 0.046 k2 0.134 k1 7 8 4.502 0.154 2.08 792.18 2 k3 6 r1 k4 463.57 k5 1.21 575.2 10.0 3 5 k6 2.15 k7 10 506.2 4 0 0 k8 12 0 k9 0 11 0 0 k11 4639 15.2 k10 13 0 0 1 0.98 0.53 0.01 15 X 234.6 9 β 18 T0 0.042 0.003 0.023 0.001 16 α1 19 -0.294 0.004 0.0617 0.002 20 γ μI 0.0008 22 -0.0027 0.0172 0.0001 23 βc θ -0.4874 0.019 21 -0.15 0.008 24 β1 β2 Hmax Hmin 0.90 0.021 -0.81 0.019 4 5 -18.14 0.45 25 40.2 N0 0 1 α CN -12.11 0.32 26 0.006 27 0.1048 φ0 -0.035 0.002 -0.024 0.001 29 βN 28 μE -332.5 9.12 E0 30 2 0.0015 0.0002 αWE Cw 78.45 1.23 24.78 0.98 3 6 αc Nc -34.5 1.01 45.87 1.45 17 14 γCE Tmax Tmin 0.84 0.02 -0.72 0.03 8 9 0.402 10 0.4825 0.012 0.011 11 αN lx 31 0.06 12 0.0033 0.0002 P 1.2 γt 32 0.02 0.001 33 -0.16 0.005 μ1 μ2 34 35 -0.0017 0.0001 0 0 μ4 μ3 36 0.1085 0.003 μ5

<!-- b003282 | furniture | pages [21] -->
m

<!-- b003283 | furniture | pages [21] -->
m

<!-- b003284 | furniture | pages [21] -->
m

<!-- b003285 | furniture | pages [21] -->
m

<!-- b003286 | furniture | pages [21] -->
m

<!-- b003287 | furniture | pages [21] -->
m

<!-- b003288 | furniture | pages [21] -->
m

<!-- b003289 | furniture | pages [21] -->
m

<!-- b003290 | furniture | pages [21] -->
m

<!-- b003291 | furniture | pages [21] -->
m

<!-- b003292 | furniture | pages [21] -->
m

<!-- b003293 | furniture | pages [21] -->
m

<!-- b003294 | furniture | pages [21] -->
m

<!-- b003295 | furniture | pages [21] -->
m

<!-- b003296 | furniture | pages [21] -->
m

<!-- b003297 | furniture | pages [21] -->
m

<!-- b003298 | furniture | pages [21] -->
m

<!-- b003299 | furniture | pages [21] -->
m

<!-- b003300 | furniture | pages [21] -->
m

<!-- b003301 | furniture | pages [21] -->
m

<!-- b003302 | furniture | pages [21] -->
m

<!-- b003303 | furniture | pages [21] -->
m

<!-- b003304 | furniture | pages [21] -->
m

<!-- b003305 | furniture | pages [21] -->
m

<!-- b003306 | furniture | pages [21] -->
m

<!-- b003307 | furniture | pages [21] -->
m

<!-- b003308 | furniture | pages [21] -->
m

<!-- b003309 | furniture | pages [21] -->
m

<!-- b003310 | furniture | pages [21] -->
m

<!-- b003311 | furniture | pages [21] -->
m

<!-- b003312 | furniture | pages [21] -->
m

<!-- b003313 | furniture | pages [21] -->
m

<!-- b003314 | furniture | pages [21] -->
m

<!-- b003315 | furniture | pages [21] -->
m

<!-- b003316 | furniture | pages [21] -->
m

<!-- b003317 | furniture | pages [21] -->
m

<!-- b003318 | furniture | pages [21] -->
m

<!-- b003319 | furniture | pages [21] -->
m

<!-- b003320 | furniture | pages [21] -->
m

<!-- b003321 | furniture | pages [21] -->
m

<!-- b003322 | furniture | pages [21] -->
m

<!-- b003323 | furniture | pages [21] -->
m

<!-- b003324 | furniture | pages [21] -->
m

<!-- b003325 | furniture | pages [21] -->
m

<!-- b003326 | furniture | pages [21] -->
m

<!-- b003327 | furniture | pages [21] -->
m

<!-- b003328 | furniture | pages [21] -->
m

<!-- b003329 | furniture | pages [21] -->
m

<!-- b003330 | furniture | pages [21] -->
m

<!-- b003331 | furniture | pages [21] -->
m

<!-- b003332 | furniture | pages [21] -->
m

<!-- b003333 | furniture | pages [21] -->
m

<!-- b003334 | furniture | pages [21] -->
m

<!-- b003335 | furniture | pages [21] -->
m

<!-- b003336 | furniture | pages [21] -->
m

<!-- b003337 | furniture | pages [21] -->
m

<!-- b003338 | furniture | pages [21] -->
m

<!-- b003339 | furniture | pages [21] -->
m

<!-- b003340 | furniture | pages [21] -->
m

<!-- b003341 | furniture | pages [21] -->
m

<!-- b003342 | furniture | pages [21] -->
m

<!-- b003343 | furniture | pages [21] -->
m

<!-- b003344 | furniture | pages [21] -->
m

<!-- b003345 | furniture | pages [21] -->
m

<!-- b003346 | furniture | pages [21] -->
m

<!-- b003347 | furniture | pages [21] -->
m

<!-- b003348 | furniture | pages [21] -->
m

<!-- b003349 | furniture | pages [21] -->
m

<!-- b003350 | furniture | pages [21] -->
m

<!-- b003351 | furniture | pages [21] -->
m

<!-- b003352 | furniture | pages [21] -->
m

<!-- b003353 | furniture | pages [21] -->
m

<!-- b003354 | furniture | pages [21] -->
m

<!-- b003355 | furniture | pages [21] -->
m

<!-- b003356 | furniture | pages [21] -->
m

<!-- b003357 | furniture | pages [21] -->
m

<!-- b003358 | furniture | pages [21] -->
m

<!-- b003359 | furniture | pages [21] -->
m

<!-- b003360 | furniture | pages [21] -->
m

<!-- b003361 | furniture | pages [21] -->
m

<!-- b003362 | furniture | pages [21] -->
m

<!-- b003363 | furniture | pages [21] -->
m

<!-- b003364 | furniture | pages [21] -->
m

<!-- b003365 | furniture | pages [21] -->
m

<!-- b003366 | furniture | pages [21] -->
m

<!-- b003367 | furniture | pages [21] -->
m

<!-- b003368 | furniture | pages [21] -->
m

<!-- b003369 | furniture | pages [21] -->
m

<!-- b003370 | furniture | pages [21] -->
m

<!-- b003371 | furniture | pages [21] -->
m

<!-- b003372 | furniture | pages [21] -->
m

<!-- b003373 | furniture | pages [21] -->
m

<!-- b003374 | furniture | pages [21] -->
m

<!-- b003375 | furniture | pages [21] -->
m

<!-- b003376 | furniture | pages [21] -->
m

<!-- b003377 | furniture | pages [21] -->
m

<!-- b003378 | furniture | pages [21] -->
m

<!-- b003379 | furniture | pages [21] -->
m

<!-- b003380 | furniture | pages [21] -->
m

<!-- b003381 | furniture | pages [21] -->
m

<!-- b003382 | furniture | pages [21] -->
m

<!-- b003383 | furniture | pages [21] -->
m

<!-- b003384 | furniture | pages [21] -->
m

<!-- b003385 | furniture | pages [21] -->
m

<!-- b003386 | furniture | pages [21] -->
m

<!-- b003387 | furniture | pages [21] -->
m

<!-- b003388 | furniture | pages [21] -->
m

<!-- b003389 | furniture | pages [21] -->
m

<!-- b003390 | furniture | pages [21] -->
m

<!-- b003391 | furniture | pages [21] -->
m

<!-- b003392 | furniture | pages [21] -->
m

<!-- b003393 | furniture | pages [21] -->
m

<!-- b003394 | furniture | pages [21] -->
m

<!-- b003395 | furniture | pages [21] -->
m

<!-- b003396 | furniture | pages [21] -->
m

<!-- b003397 | furniture | pages [21] -->
m

<!-- b003398 | furniture | pages [21] -->
m

<!-- b003399 | furniture | pages [21] -->
m

<!-- b003400 | furniture | pages [21] -->
m

<!-- b003401 | furniture | pages [21] -->
m

<!-- b003402 | furniture | pages [21] -->
m

<!-- b003403 | furniture | pages [21] -->
m

<!-- b003404 | furniture | pages [21] -->
m

<!-- b003405 | furniture | pages [21] -->
m

<!-- b003406 | furniture | pages [21] -->
m

<!-- b003407 | furniture | pages [21] -->
m

<!-- b003408 | furniture | pages [21] -->
m

<!-- b003409 | furniture | pages [21] -->
m

<!-- b003410 | furniture | pages [21] -->
m

<!-- b003411 | furniture | pages [21] -->
m

<!-- b003412 | furniture | pages [21] -->
m

<!-- b003413 | furniture | pages [21] -->
m

<!-- b003414 | furniture | pages [21] -->
m

<!-- b003415 | furniture | pages [21] -->
m

<!-- b003416 | furniture | pages [21] -->
m

<!-- b003417 | furniture | pages [21] -->
m

<!-- b003418 | furniture | pages [21] -->
m

<!-- b003419 | furniture | pages [21] -->
m

<!-- b003420 | furniture | pages [21] -->
m

<!-- b003421 | furniture | pages [21] -->
m

<!-- b003422 | furniture | pages [21] -->
m

<!-- b003423 | furniture | pages [21] -->
m

<!-- b003424 | furniture | pages [21] -->
m

<!-- b003425 | furniture | pages [21] -->
m

<!-- b003426 | furniture | pages [21] -->
m

<!-- b003427 | furniture | pages [21] -->
m

<!-- b003428 | furniture | pages [21] -->
m

<!-- b003429 | furniture | pages [21] -->
m

<!-- b003430 | furniture | pages [21] -->
m

<!-- b003431 | furniture | pages [21] -->
m

<!-- b003432 | furniture | pages [21] -->
m

<!-- b003433 | furniture | pages [21] -->
m

<!-- b003434 | furniture | pages [21] -->
m

<!-- b003435 | furniture | pages [21] -->
m

<!-- b003436 | furniture | pages [21] -->
m

<!-- b003437 | furniture | pages [21] -->
m

<!-- b003438 | furniture | pages [21] -->
m

<!-- b003439 | furniture | pages [21] -->
m

<!-- b003440 | furniture | pages [21] -->
m

<!-- b003441 | furniture | pages [21] -->
m

<!-- b003442 | furniture | pages [21] -->
m

<!-- b003443 | furniture | pages [21] -->
m

<!-- b003444 | furniture | pages [21] -->
m

<!-- b003445 | furniture | pages [21] -->
m

<!-- b003446 | furniture | pages [21] -->
m

<!-- b003447 | furniture | pages [21] -->
m

<!-- b003448 | furniture | pages [21] -->
m

<!-- b003449 | furniture | pages [21] -->
m

<!-- b003450 | furniture | pages [21] -->
m

<!-- b003451 | furniture | pages [21] -->
m

<!-- b003452 | furniture | pages [21] -->
m

<!-- b003453 | furniture | pages [21] -->
m

<!-- b003454 | furniture | pages [21] -->
m

<!-- b003455 | furniture | pages [21] -->
m

<!-- b003456 | furniture | pages [21] -->
m

<!-- b003457 | furniture | pages [21] -->
m

<!-- b003458 | furniture | pages [21] -->
m

<!-- b003459 | furniture | pages [21] -->
m

<!-- b003460 | furniture | pages [21] -->
m

<!-- b003461 | furniture | pages [21] -->
m

<!-- b003462 | furniture | pages [21] -->
m

<!-- b003463 | furniture | pages [21] -->
m

<!-- b003464 | furniture | pages [21] -->
m

<!-- b003465 | furniture | pages [21] -->
m

<!-- b003466 | furniture | pages [21] -->
m

<!-- b003467 | furniture | pages [21] -->
m

<!-- b003468 | furniture | pages [21] -->
m

<!-- b003469 | furniture | pages [21] -->
m

<!-- b003470 | furniture | pages [21] -->
m

<!-- b003471 | furniture | pages [21] -->
m

<!-- b003472 | furniture | pages [21] -->
m

<!-- b003473 | furniture | pages [21] -->
m

<!-- b003474 | furniture | pages [21] -->
m

<!-- b003475 | furniture | pages [21] -->
m

<!-- b003476 | furniture | pages [21] -->
m

<!-- b003477 | furniture | pages [21] -->
m

<!-- b003478 | furniture | pages [21] -->
m

<!-- b003479 | furniture | pages [21] -->
m

<!-- b003480 | furniture | pages [21] -->
m

<!-- b003481 | furniture | pages [21] -->
m

<!-- b003482 | furniture | pages [21] -->
m

<!-- b003483 | furniture | pages [21] -->
m

<!-- b003484 | furniture | pages [21] -->
m

<!-- b003485 | furniture | pages [21] -->
m

<!-- b003486 | furniture | pages [21] -->
m

<!-- b003487 | furniture | pages [21] -->
m

<!-- b003488 | furniture | pages [21] -->
m

<!-- b003489 | furniture | pages [21] -->
m

<!-- b003490 | furniture | pages [21] -->
m

<!-- b003491 | furniture | pages [21] -->
m

<!-- b003492 | furniture | pages [21] -->
m

<!-- b003493 | furniture | pages [21] -->
m

<!-- b003494 | furniture | pages [21] -->
m

<!-- b003495 | furniture | pages [21] -->
m

<!-- b003496 | furniture | pages [21] -->
m

<!-- b003497 | furniture | pages [21] -->
m

<!-- b003498 | furniture | pages [21] -->
m

<!-- b003499 | furniture | pages [21] -->
m

<!-- b003500 | furniture | pages [21] -->
m

<!-- b003501 | furniture | pages [21] -->
m

<!-- b003502 | furniture | pages [21] -->
m

<!-- b003503 | furniture | pages [21] -->
m

<!-- b003504 | furniture | pages [21] -->
m

<!-- b003505 | furniture | pages [21] -->
m

<!-- b003506 | furniture | pages [21] -->
m

<!-- b003507 | furniture | pages [21] -->
m

<!-- b003508 | furniture | pages [21] -->
m

<!-- b003509 | furniture | pages [21] -->
m

<!-- b003510 | furniture | pages [21] -->
m

<!-- b003511 | furniture | pages [21] -->
m

<!-- b003512 | furniture | pages [21] -->
m

<!-- b003513 | furniture | pages [21] -->
m

<!-- b003514 | furniture | pages [21] -->
m

<!-- b003515 | furniture | pages [21] -->
m

<!-- b003516 | furniture | pages [21] -->
m

<!-- b003517 | furniture | pages [21] -->
m

<!-- b003518 | furniture | pages [21] -->
m

<!-- b003519 | furniture | pages [21] -->
m

<!-- b003520 | furniture | pages [21] -->
m

<!-- b003521 | furniture | pages [21] -->
m

<!-- b003522 | furniture | pages [21] -->
m

<!-- b003523 | furniture | pages [21] -->
m

<!-- b003524 | furniture | pages [21] -->
m

<!-- b003525 | furniture | pages [21] -->
m

<!-- b003526 | furniture | pages [21] -->
m

<!-- b003527 | furniture | pages [21] -->
m

<!-- b003528 | furniture | pages [21] -->
m

<!-- b003529 | furniture | pages [21] -->
m

<!-- b003530 | furniture | pages [21] -->
m

<!-- b003531 | furniture | pages [21] -->
m

<!-- b003532 | furniture | pages [21] -->
m

<!-- b003533 | furniture | pages [21] -->
m

<!-- b003534 | furniture | pages [21] -->
m

<!-- b003535 | furniture | pages [21] -->
m

<!-- b003536 | furniture | pages [21] -->
m

<!-- b003537 | furniture | pages [21] -->
m

<!-- b003538 | furniture | pages [21] -->
m

<!-- b003539 | furniture | pages [21] -->
m

<!-- b003540 | furniture | pages [21] -->
m

<!-- b003541 | furniture | pages [21] -->
m

<!-- b003542 | furniture | pages [21] -->
m

<!-- b003543 | furniture | pages [21] -->
m

<!-- b003544 | furniture | pages [21] -->
m

<!-- b003545 | furniture | pages [21] -->
m

<!-- b003546 | furniture | pages [21] -->
m

<!-- b003547 | furniture | pages [21] -->
m

<!-- b003548 | furniture | pages [21] -->
m

<!-- b003549 | furniture | pages [21] -->
m

<!-- b003550 | furniture | pages [21] -->
m

<!-- b003551 | furniture | pages [21] -->
m

<!-- b003552 | furniture | pages [21] -->
m

<!-- b003553 | furniture | pages [21] -->
m

<!-- b003554 | furniture | pages [21] -->
m

<!-- b003555 | furniture | pages [21] -->
m

<!-- b003556 | furniture | pages [21] -->
m

<!-- b003557 | furniture | pages [21] -->
m

<!-- b003558 | furniture | pages [21] -->
m

<!-- b003559 | furniture | pages [21] -->
m

<!-- b003560 | furniture | pages [21] -->
m

<!-- b003561 | furniture | pages [21] -->
m

<!-- b003562 | furniture | pages [21] -->
m

<!-- b003563 | furniture | pages [21] -->
m

<!-- b003564 | furniture | pages [21] -->
m

<!-- b003565 | furniture | pages [21] -->
m

<!-- b003566 | furniture | pages [21] -->
m

<!-- b003567 | furniture | pages [21] -->
m

<!-- b003568 | furniture | pages [21] -->
m

<!-- b003569 | furniture | pages [21] -->
m

<!-- b003570 | furniture | pages [21] -->
m

<!-- b003571 | furniture | pages [21] -->
m

<!-- b003572 | furniture | pages [21] -->
m

<!-- b003573 | furniture | pages [21] -->
m

<!-- b003574 | furniture | pages [21] -->
m

<!-- b003575 | furniture | pages [21] -->
m

<!-- b003576 | furniture | pages [21] -->
m

<!-- b003577 | furniture | pages [21] -->
m

<!-- b003578 | furniture | pages [21] -->
m

<!-- b003579 | furniture | pages [21] -->
m

<!-- b003580 | furniture | pages [21] -->
m

<!-- b003581 | furniture | pages [21] -->
m

<!-- b003582 | furniture | pages [21] -->
m

<!-- b003583 | furniture | pages [21] -->
m

<!-- b003584 | furniture | pages [21] -->
m

<!-- b003585 | furniture | pages [21] -->
m

<!-- b003586 | furniture | pages [21] -->
m

<!-- b003587 | furniture | pages [21] -->
m

<!-- b003588 | furniture | pages [21] -->
m

<!-- b003589 | furniture | pages [21] -->
m

<!-- b003590 | furniture | pages [21] -->
m

<!-- b003591 | furniture | pages [21] -->
m

<!-- b003592 | furniture | pages [21] -->
m

<!-- b003593 | furniture | pages [21] -->
m

<!-- b003594 | furniture | pages [21] -->
m

<!-- b003595 | furniture | pages [21] -->
m

<!-- b003596 | furniture | pages [21] -->
m

<!-- b003597 | furniture | pages [21] -->
m

<!-- b003598 | furniture | pages [21] -->
m

<!-- b003599 | furniture | pages [21] -->
m

<!-- b003600 | furniture | pages [21] -->
m

<!-- b003601 | furniture | pages [21] -->
m

<!-- b003602 | furniture | pages [21] -->
m

<!-- b003603 | furniture | pages [21] -->
m

<!-- b003604 | furniture | pages [21] -->
m

<!-- b003605 | furniture | pages [21] -->
m

<!-- b003606 | furniture | pages [22] -->
Team # 2503268

<!-- b003607 | furniture | pages [22] -->
Page 20 of 24

<!-- b003609 | caption | pages [22] -->
Table 7: Full local sensitivity metrics for all parameters (Mean, Std, Rank), laid out in two columns

<!-- b003610 | prose | pages [22] -->
per row for compactness.

<!-- b003611 | prose | pages [22] -->
in California coastal cliff retreat. By leveraging these approaches and utilizing relevant data from the California Coastal Cliff Erosion Survey, we derive the height of coastal landslide loss in Pfeiffer Big Sur, denoted as Hsur:

<!-- b003612 | prose | pages [22] -->
10.2

<!-- b003613 | heading | pages [22] -->
Model Validation and Generalization

<!-- b003614 | prose | pages [22] -->
To assess the validity and generalizability of our model, we utilize three primary metrics derived from the data collected in Pfeiffer Big Sur State Park: annual visitor attendance (Nsur), govern- ment revenue (Tsur), and environmental impact indicators (Hsur). By normalizing these variables to eliminate dimensional discrepancies, we represent the dynamics of overtourism in a standardized form.

<!-- b003615 | prose | pages [22] -->
Our model is defined as a system of coupled differential equations, where each variable influences the others through non-linear interactions. Specifically, Hsur, representing the environmental degrada- tion, is influenced by visitor numbers (Nsur) and tourism revenue (Tsur) through terms like k2HsurNsur

<!-- b003616 | prose | pages [22, 23] -->
关注数学模型 1993 2001 "The challenge is not to stop tourism. The challenge is how do we get it right." Costas Christ, Beyond Green Travel, Big Sur DsP Consultant

<!-- b003617 | furniture | pages [22] -->
获取更多资讯

<!-- b003618 | furniture | pages [23] -->
Page 21 of 24

<!-- b003619 | furniture | pages [23] -->
Team # 2503268

<!-- b003621 | prose | pages [23] -->
Join Monterey County Board of Supervisors, MCCVB, Big Sur businesses, and concerned 1986 93 residents to protect our coastal community and Point Sur State Historic ark its natural resources for generations to come.

<!-- b003622 | prose | pages [23] -->
Cos Nat ΔZ 1976 86 Mon OVENTOUISM ILING RG SUR

<!-- b003623 | caption | pages [23] -->
Figure 12: (a)The current state of overtourism in Big Sur. (b) Baseline Analysis and Data Sources for

<!-- b003624 | prose | pages [23] -->
Coastal Cliff Retreat in Big Sur.

<!-- b003625 | prose | pages [23] -->
and k3TsurHsur, which account for the accelerated erosion due to human activity and mitigation efforts ● financed by tourism income. ●

<!-- b003626 | prose | pages [23] -->
dHsur = k1HSur + k2HSurNSur + k3TSurHSur, dt dNsur = r1Nsur (1 − (24) tp dTSur = k5T sur + k6Nsur. 1p

<!-- b003627 | prose | pages [23] -->
The model parameters (k1, k2, k3, . . .) were optimized using least squares to minimize the residuals between the predicted values and the normalized observed data, while incorporating tolerance thresh- olds to account for inherent variability in real-world systems. The optimization results demonstrated a high degree of alignment with the empirical data, indicating the robustness of the proposed model in capturing the dynamics of overtourism in Big Sur.

<!-- b003628 | prose | pages [23] -->
O For instance, when the data is normalized to [0.65694513,0.83935834,0.91277344], the model identifies a state of relative harmony among the environmental, economic, and passenger factors. This balance indicates that a policy focusing on comprehensive development is optimal. Specifically, the coordination across these dimensions ensures that growth in one factor does not come at the expense of another, fostering a sustainable and synergistic development strategy.

<!-- b003629 | prose | pages [23] -->
Comparing the original score of 0.32773 with the updated score of 0.73563, it is evident that the chosen policy direction significantly improves the overall system performance. The substantial increase in the normalized score reflects better alignment with the model's objectives and the achieve- ment of a more robust and balanced state. Thus, on the basis of balancing the environment, economy, and population, it helps us reimagining the fantasy of Big Sur.

<!-- b003630 | furniture | pages [24] -->
Page 22 of 24

<!-- b003631 | furniture | pages [24] -->
Team # 2503268

<!-- b003632 | heading | pages [24] -->
11 Strengths and Weaknesses

<!-- b003633 | heading | pages [24] -->
11.1 Strengths

<!-- b003634 | prose | pages [24] -->
Strength 1: Comprehensive and Thorough Consideration of Key Aspects The model systematically addresses three critical dimensions: local residents' quality of life, natu- ral resource conservation, and economic and social development. In the quality of life dimension, it incorporates factors such as average individual income, crowding levels, housing affordability, and noise from tourists. For natural resource conservation, it evaluates natural resource utilization, energy consumption management, waste management, and carbon footprint. The economic and social devel- opment dimension includes tourism tax revenue, employment growth, cultural resource protection, and social safety. This multidimensional approach ensures that the model provides a holistic perspective and a robust foundation for policy-making.

<!-- b003635 | prose | pages [24] -->
Strength 2: Dynamic and Time-Responsive Design The model employs dynamic differential equations to simulate the evolution of key variables such as glacier health, tourist numbers, and hotel tax revenue over time. This enables the model to capture the interplay between factors like resource depletion and economic reinvestment, providing an insightful depiction of how policies affect outcomes in the long term. Its ability to simulate time-dependent interactions makes it a powerful tool for real-world application.

<!-- b003636 | heading | pages [24] -->
Strength 3: High Generalizability and Applicability

<!-- b003637 | prose | pages [24] -->
With its flexible structure, the model can be easily adapted to other cities or tourist destinations by adjusting region-specific parameters such as population size, tourism capacity, and resource allocation proportions. This versatility ensures that the model can serve as a standardized yet adaptable tool for addressing sustainability challenges in diverse contexts.

<!-- b003638 | prose | pages [24] -->
Strength 4: Quantifiable Policy Evaluation The model employs a scoring mechanism to quantitatively evaluate policy impacts across the three di- mensions. By aggregating the scores for local residents' quality of life, natural resource conservation, and economic and social development, it provides a clear and intuitive representation of policy effec- tiveness. This enables policymakers to quickly identify optimal strategies and focus on areas requiring improvement.

<!-- b003639 | heading | pages [24] -->
11.2 Weaknesses

<!-- b003640 | heading | pages [24] -->
Weakness 1: Limited Capacity to Address Unexpected Events

<!-- b003641 | prose | pages [24] -->
The model assumes a relatively stable external environment, making it less effective in accounting for sudden disruptions. For instance, the 2013 marine heatwave significantly impacted glacier conditions, and the COVID-19 pandemic in 2020 drastically altered human behavior globally. Such events fall outside the model's predictive scope.

<!-- b003642 | prose | pages [24] -->
Weakness 2: Ignorance of the Delay of Policy Implementation The model presumes policies are enacted and become effective immediately upon their introduction. In real-world scenarios, there is typically a delay between the announcement of a policy and its full implementation and impact. Accounting for the time required for policies to be rolled out and to in- fluence the system would add considerable complexity to the model, which is not currently addressed. This assumption may lead to inaccuracies in scenarios where timing of policy effects is critical.

<!-- b003643 | prose | pages [24] -->
关注数学模型

<!-- b003644 | furniture | pages [24] -->
获取更多资讯

<!-- b003645 | furniture | pages [25] -->
Team # 2503268

<!-- b003646 | furniture | pages [25] -->
Page 23 of 24

<!-- b003647 | heading | pages [25] -->
References

<!-- b003648 | references | pages [25] -->
[1] Braithwaite, R. J. "Glacier Equilibrium-Line Altitude: An Indicator of Climate Change." Journal

<!-- b003649 | references | pages [25] -->
of Glaciology, 1984.

<!-- b003650 | references | pages [25] -->
[2] Oerlemans, J. "Glaciers and Climate Change." International Geophysics, 2001.

<!-- b003651 | references | pages [25] -->
微信公众号：数学模型

<!-- b003652 | references | pages [25] -->
[3] Verhulst, P. F. "Notice sur la loi que la population suit dans son accroissement." Correspondance

<!-- b003653 | references | pages [25] -->
Mathématique et Physique, 1838.

<!-- b003654 | references | pages [25] -->
[4] Buckley, R. "Environmental Impacts of Ecotourism." CABI Publishing, 2004.

<!-- b003655 | references | pages [25] -->
[5] Smith, M. "Tourism Economics: Impact of Visitor Spending on Tax Revenue." Tourism Review,

<!-- b003656 | references | pages [25] -->
2015.

<!-- b003657 | references | pages [25] -->
[6] Frechtling, D. C. "Forecasting Tourism Demand:

<!-- b003658 | references | pages [25] -->
Methods and Strategies." Butterworth-

<!-- b003659 | references | pages [25] -->
Heinemann, 2001.

<!-- b003660 | references | pages [25] -->
微信号：MATHmodels

<!-- b003661 | references | pages [25] -->
[7] Glaeser, E. L., Kolko, J., & Saiz, A. "Consumer city." Journal of Economic Geography, 2001.

<!-- b003662 | references | pages [25] -->
[8] Hall, C. M., Timothy, D. J., & Duval, D. T. Safety and security in tourism: Relationships, man-

<!-- b003663 | references | pages [25] -->
agement, and marketing. Haworth Hospitality Press, 2004

<!-- b003664 | references | pages [25] -->
[9] Atzori, R. "Destination stakeholders’ perceptions of overtourism impacts, causes, and responses:

<!-- b003665 | references | pages [25] -->
The case of Big Sur, California." Journal of Destination Marketing & Management, vol. 17,

<!-- b003666 | references | pages [25] -->
2020, p. 100440.

<!-- b003667 | references | pages [25] -->
[10] Hapke, C. J., & Green, K. R. "Rates of landsliding and cliﬀretreat along the Big Sur Coast,

<!-- b003668 | references | pages [25] -->
California—Measuring a crucial baseline." USGS Fact Sheet, No. 2004-3099, 2005.

<!-- b003669 | references | pages [25] -->
[11] Swirad, Z. M., & Young, A. P. "Spatial and temporal trends in California coastal cliﬀretreat."

<!-- b003670 | references | pages [25] -->
Geomorphology, vol. 412, 2022, p. 108318.

<!-- b003671 | references | pages [25] -->
m

<!-- b003672 | references | pages [25] -->
m

<!-- b003673 | references | pages [25] -->
m

<!-- b003674 | references | pages [25] -->
m

<!-- b003675 | references | pages [25] -->
m

<!-- b003676 | references | pages [25] -->
m

<!-- b003677 | references | pages [25] -->
m

<!-- b003678 | references | pages [25] -->
m

<!-- b003679 | references | pages [25] -->
m

<!-- b003680 | references | pages [25] -->
m

<!-- b003681 | references | pages [25] -->
m

<!-- b003682 | references | pages [25] -->
m

<!-- b003683 | references | pages [25] -->
m

<!-- b003684 | references | pages [25] -->
m

<!-- b003685 | references | pages [25] -->
m

<!-- b003686 | references | pages [25] -->
m

<!-- b003687 | references | pages [25] -->
m

<!-- b003688 | references | pages [25] -->
m

<!-- b003689 | references | pages [25] -->
m

<!-- b003690 | references | pages [25] -->
m

<!-- b003691 | references | pages [25] -->
m

<!-- b003692 | references | pages [25] -->
m

<!-- b003693 | references | pages [25] -->
m

<!-- b003694 | references | pages [25] -->
m

<!-- b003695 | references | pages [25] -->
m

<!-- b003696 | references | pages [25] -->
m

<!-- b003697 | references | pages [25] -->
m

<!-- b003698 | references | pages [25] -->
m

<!-- b003699 | references | pages [25] -->
m

<!-- b003700 | references | pages [25] -->
m

<!-- b003701 | references | pages [25] -->
m

<!-- b003702 | references | pages [25] -->
m

<!-- b003703 | references | pages [25] -->
m

<!-- b003704 | references | pages [25] -->
m

<!-- b003705 | references | pages [25] -->
m

<!-- b003706 | references | pages [25] -->
m

<!-- b003707 | references | pages [25] -->
m

<!-- b003708 | references | pages [25] -->
m

<!-- b003709 | references | pages [25] -->
m

<!-- b003710 | references | pages [25] -->
m

<!-- b003711 | references | pages [25] -->
m

<!-- b003712 | references | pages [25] -->
m

<!-- b003713 | references | pages [25] -->
m

<!-- b003714 | references | pages [25] -->
m

<!-- b003715 | references | pages [25] -->
m

<!-- b003716 | references | pages [25] -->
m

<!-- b003717 | references | pages [25] -->
m

<!-- b003718 | references | pages [25] -->
m

<!-- b003719 | references | pages [25] -->
m

<!-- b003720 | references | pages [25] -->
m

<!-- b003721 | references | pages [25] -->
m

<!-- b003722 | references | pages [25] -->
m

<!-- b003723 | references | pages [25] -->
m

<!-- b003724 | references | pages [25] -->
m

<!-- b003725 | references | pages [25] -->
m

<!-- b003726 | references | pages [25] -->
m

<!-- b003727 | references | pages [25] -->
m

<!-- b003728 | references | pages [25] -->
m

<!-- b003729 | references | pages [25] -->
m

<!-- b003730 | references | pages [25] -->
m

<!-- b003731 | references | pages [25] -->
m

<!-- b003732 | references | pages [25] -->
m

<!-- b003733 | references | pages [25] -->
m

<!-- b003734 | references | pages [25] -->
m

<!-- b003735 | references | pages [25] -->
m

<!-- b003736 | references | pages [25] -->
m

<!-- b003737 | references | pages [25] -->
m

<!-- b003738 | references | pages [25] -->
m

<!-- b003739 | references | pages [25] -->
m

<!-- b003740 | references | pages [25] -->
m

<!-- b003741 | references | pages [25] -->
m

<!-- b003742 | references | pages [25] -->
m

<!-- b003743 | references | pages [25] -->
m

<!-- b003744 | references | pages [25] -->
m

<!-- b003745 | references | pages [25] -->
m

<!-- b003746 | references | pages [25] -->
m

<!-- b003747 | references | pages [25] -->
m

<!-- b003748 | references | pages [25] -->
m

<!-- b003749 | references | pages [25] -->
m

<!-- b003750 | references | pages [25] -->
m

<!-- b003751 | references | pages [25] -->
m

<!-- b003752 | references | pages [25] -->
m

<!-- b003753 | references | pages [25] -->
m

<!-- b003754 | references | pages [25] -->
m

<!-- b003755 | references | pages [25] -->
m

<!-- b003756 | references | pages [25] -->
m

<!-- b003757 | references | pages [25] -->
m

<!-- b003758 | references | pages [25] -->
m

<!-- b003759 | references | pages [25] -->
m

<!-- b003760 | references | pages [25] -->
m

<!-- b003761 | references | pages [25] -->
m

<!-- b003762 | references | pages [25] -->
m

<!-- b003763 | references | pages [25] -->
m

<!-- b003764 | references | pages [25] -->
m

<!-- b003765 | references | pages [25] -->
m

<!-- b003766 | references | pages [25] -->
m

<!-- b003767 | references | pages [25] -->
m

<!-- b003768 | references | pages [25] -->
m

<!-- b003769 | references | pages [25] -->
m

<!-- b003770 | references | pages [25] -->
m

<!-- b003771 | references | pages [25] -->
m

<!-- b003772 | references | pages [25] -->
m

<!-- b003773 | references | pages [25] -->
m

<!-- b003774 | references | pages [25] -->
m

<!-- b003775 | references | pages [25] -->
m

<!-- b003776 | references | pages [25] -->
m

<!-- b003777 | references | pages [25] -->
m

<!-- b003778 | references | pages [25] -->
m

<!-- b003779 | references | pages [25] -->
m

<!-- b003780 | references | pages [25] -->
m

<!-- b003781 | references | pages [25] -->
m

<!-- b003782 | references | pages [25] -->
m

<!-- b003783 | references | pages [25] -->
m

<!-- b003784 | references | pages [25] -->
m

<!-- b003785 | references | pages [25] -->
m

<!-- b003786 | references | pages [25] -->
m

<!-- b003787 | references | pages [25] -->
m

<!-- b003788 | references | pages [25] -->
m

<!-- b003789 | references | pages [25] -->
m

<!-- b003790 | references | pages [25] -->
m

<!-- b003791 | references | pages [25] -->
m

<!-- b003792 | references | pages [25] -->
m

<!-- b003793 | references | pages [25] -->
m

<!-- b003794 | references | pages [25] -->
m

<!-- b003795 | references | pages [25] -->
m

<!-- b003796 | references | pages [25] -->
m

<!-- b003797 | references | pages [25] -->
m

<!-- b003798 | references | pages [25] -->
m

<!-- b003799 | references | pages [25] -->
m

<!-- b003800 | references | pages [25] -->
m

<!-- b003801 | references | pages [25] -->
m

<!-- b003802 | references | pages [25] -->
m

<!-- b003803 | references | pages [25] -->
m

<!-- b003804 | references | pages [25] -->
m

<!-- b003805 | references | pages [25] -->
m

<!-- b003806 | references | pages [25] -->
m

<!-- b003807 | references | pages [25] -->
m

<!-- b003808 | references | pages [25] -->
m

<!-- b003809 | references | pages [25] -->
m

<!-- b003810 | references | pages [25] -->
m

<!-- b003811 | references | pages [25] -->
m

<!-- b003812 | references | pages [25] -->
m

<!-- b003813 | references | pages [25] -->
m

<!-- b003814 | references | pages [25] -->
m

<!-- b003815 | references | pages [25] -->
m

<!-- b003816 | references | pages [25] -->
m

<!-- b003817 | references | pages [25] -->
m

<!-- b003818 | references | pages [25] -->
m

<!-- b003819 | references | pages [25] -->
m

<!-- b003820 | references | pages [25] -->
m

<!-- b003821 | references | pages [25] -->
m

<!-- b003822 | references | pages [25] -->
m

<!-- b003823 | references | pages [25] -->
m

<!-- b003824 | references | pages [25] -->
m

<!-- b003825 | references | pages [25] -->
m

<!-- b003826 | references | pages [25] -->
m

<!-- b003827 | references | pages [25] -->
m

<!-- b003828 | references | pages [25] -->
m

<!-- b003829 | references | pages [25] -->
m

<!-- b003830 | references | pages [25] -->
m

<!-- b003831 | references | pages [25] -->
m

<!-- b003832 | references | pages [25] -->
m

<!-- b003833 | references | pages [25] -->
m

<!-- b003834 | references | pages [25] -->
m

<!-- b003835 | references | pages [25] -->
m

<!-- b003836 | references | pages [25] -->
m

<!-- b003837 | references | pages [25] -->
m

<!-- b003838 | references | pages [25] -->
m

<!-- b003839 | references | pages [25] -->
m

<!-- b003840 | references | pages [25] -->
m

<!-- b003841 | references | pages [25] -->
m

<!-- b003842 | references | pages [25] -->
m

<!-- b003843 | references | pages [25] -->
m

<!-- b003844 | references | pages [25] -->
m

<!-- b003845 | references | pages [25] -->
m

<!-- b003846 | references | pages [25] -->
m

<!-- b003847 | references | pages [25] -->
m

<!-- b003848 | references | pages [25] -->
m

<!-- b003849 | references | pages [25] -->
m

<!-- b003850 | references | pages [25] -->
m

<!-- b003851 | references | pages [25] -->
m

<!-- b003852 | references | pages [25] -->
m

<!-- b003853 | references | pages [25] -->
m

<!-- b003854 | references | pages [25] -->
m

<!-- b003855 | references | pages [25] -->
m

<!-- b003856 | references | pages [25] -->
m

<!-- b003857 | references | pages [25] -->
m

<!-- b003858 | references | pages [25] -->
m

<!-- b003859 | references | pages [25] -->
m

<!-- b003860 | references | pages [25] -->
m

<!-- b003861 | references | pages [25] -->
m

<!-- b003862 | references | pages [25] -->
m

<!-- b003863 | references | pages [25] -->
m

<!-- b003864 | references | pages [25] -->
m

<!-- b003865 | references | pages [25] -->
m

<!-- b003866 | references | pages [25] -->
m

<!-- b003867 | references | pages [25] -->
m

<!-- b003868 | references | pages [25] -->
m

<!-- b003869 | references | pages [25] -->
m

<!-- b003870 | references | pages [25] -->
m

<!-- b003871 | references | pages [25] -->
m

<!-- b003872 | references | pages [25] -->
m

<!-- b003873 | references | pages [25] -->
m

<!-- b003874 | references | pages [25] -->
m

<!-- b003875 | references | pages [25] -->
m

<!-- b003876 | references | pages [25] -->
m

<!-- b003877 | references | pages [25] -->
m

<!-- b003878 | references | pages [25] -->
m

<!-- b003879 | references | pages [25] -->
m

<!-- b003880 | references | pages [25] -->
m

<!-- b003881 | references | pages [25] -->
m

<!-- b003882 | references | pages [25] -->
m

<!-- b003883 | references | pages [25] -->
m

<!-- b003884 | references | pages [25] -->
m

<!-- b003885 | references | pages [25] -->
m

<!-- b003886 | references | pages [25] -->
m

<!-- b003887 | references | pages [25] -->
m

<!-- b003888 | references | pages [25] -->
m

<!-- b003889 | references | pages [25] -->
m

<!-- b003890 | references | pages [25] -->
m

<!-- b003891 | references | pages [25] -->
m

<!-- b003892 | references | pages [25] -->
m

<!-- b003893 | references | pages [25] -->
m

<!-- b003894 | references | pages [25] -->
m

<!-- b003895 | references | pages [25] -->
m

<!-- b003896 | references | pages [25] -->
m

<!-- b003897 | references | pages [25] -->
m

<!-- b003898 | references | pages [25] -->
m

<!-- b003899 | references | pages [25] -->
m

<!-- b003900 | references | pages [25] -->
m

<!-- b003901 | furniture | pages [25] -->
m

<!-- b003902 | furniture | pages [25] -->
m

<!-- b003903 | furniture | pages [25] -->
m

<!-- b003904 | furniture | pages [25] -->
m

<!-- b003905 | furniture | pages [25] -->
m

<!-- b003906 | furniture | pages [25] -->
m

<!-- b003907 | furniture | pages [25] -->
m

<!-- b003908 | furniture | pages [25] -->
m

<!-- b003909 | furniture | pages [25] -->
m

<!-- b003910 | furniture | pages [25] -->
m

<!-- b003911 | furniture | pages [25] -->
m

<!-- b003912 | furniture | pages [25] -->
m

<!-- b003913 | furniture | pages [25] -->
m

<!-- b003914 | furniture | pages [25] -->
m

<!-- b003915 | furniture | pages [25] -->
m

<!-- b003916 | furniture | pages [25] -->
m

<!-- b003917 | furniture | pages [25] -->
m

<!-- b003918 | furniture | pages [25] -->
m

<!-- b003919 | furniture | pages [25] -->
m

<!-- b003920 | furniture | pages [25] -->
m

<!-- b003921 | furniture | pages [25] -->
m

<!-- b003922 | furniture | pages [25] -->
m

<!-- b003923 | furniture | pages [25] -->
m

<!-- b003924 | furniture | pages [25] -->
m

<!-- b003925 | furniture | pages [25] -->
m

<!-- b003926 | furniture | pages [25] -->
m

<!-- b003927 | furniture | pages [25] -->
m

<!-- b003928 | furniture | pages [25] -->
m

<!-- b003929 | furniture | pages [25] -->
m

<!-- b003930 | furniture | pages [25] -->
m

<!-- b003931 | furniture | pages [25] -->
m

<!-- b003932 | furniture | pages [25] -->
m

<!-- b003933 | furniture | pages [25] -->
m

<!-- b003934 | furniture | pages [25] -->
m

<!-- b003935 | furniture | pages [25] -->
m

<!-- b003936 | furniture | pages [25] -->
m

<!-- b003937 | furniture | pages [25] -->
m

<!-- b003938 | furniture | pages [25] -->
m

<!-- b003939 | furniture | pages [25] -->
m

<!-- b003940 | furniture | pages [25] -->
m

<!-- b003941 | furniture | pages [25] -->
m

<!-- b003942 | furniture | pages [25] -->
m

<!-- b003943 | furniture | pages [25] -->
m

<!-- b003944 | furniture | pages [25] -->
m

<!-- b003945 | furniture | pages [25] -->
m

<!-- b003946 | furniture | pages [25] -->
m

<!-- b003947 | furniture | pages [25] -->
m

<!-- b003948 | furniture | pages [25] -->
m

<!-- b003949 | furniture | pages [25] -->
m

<!-- b003950 | furniture | pages [25] -->
m

<!-- b003951 | furniture | pages [25] -->
m

<!-- b003952 | furniture | pages [25] -->
m

<!-- b003953 | furniture | pages [25] -->
m

<!-- b003954 | furniture | pages [25] -->
m

<!-- b003955 | furniture | pages [25] -->
m

<!-- b003956 | furniture | pages [25] -->
m

<!-- b003957 | furniture | pages [25] -->
m

<!-- b003958 | furniture | pages [25] -->
m

<!-- b003959 | furniture | pages [25] -->
m

<!-- b003960 | furniture | pages [25] -->
m

<!-- b003961 | furniture | pages [25] -->
m

<!-- b003962 | furniture | pages [25] -->
m

<!-- b003963 | furniture | pages [25] -->
m

<!-- b003964 | furniture | pages [25] -->
m

<!-- b003965 | furniture | pages [25] -->
m

<!-- b003966 | furniture | pages [25] -->
m

<!-- b003967 | furniture | pages [25] -->
m

<!-- b003968 | furniture | pages [25] -->
m

<!-- b003969 | furniture | pages [25] -->
m

<!-- b003970 | furniture | pages [25] -->
m

<!-- b003971 | furniture | pages [25] -->
m

<!-- b003972 | furniture | pages [25] -->
m

<!-- b003973 | furniture | pages [25] -->
m

<!-- b003974 | furniture | pages [25] -->
m

<!-- b003975 | furniture | pages [25] -->
m

<!-- b003976 | furniture | pages [25] -->
m

<!-- b003977 | furniture | pages [25] -->
m

<!-- b003978 | furniture | pages [25] -->
m

<!-- b003979 | furniture | pages [25] -->
m

<!-- b003980 | furniture | pages [25] -->
m

<!-- b003981 | furniture | pages [25] -->
m

<!-- b003982 | furniture | pages [25] -->
m

<!-- b003983 | furniture | pages [25] -->
m

<!-- b003984 | furniture | pages [25] -->
m

<!-- b003985 | furniture | pages [25] -->
m

<!-- b003986 | furniture | pages [25] -->
m

<!-- b003987 | furniture | pages [25] -->
m

<!-- b003988 | furniture | pages [25] -->
m

<!-- b003989 | furniture | pages [25] -->
m

<!-- b003990 | furniture | pages [25] -->
m

<!-- b003991 | furniture | pages [25] -->
m

<!-- b003992 | furniture | pages [25] -->
m

<!-- b003993 | furniture | pages [25] -->
m

<!-- b003994 | furniture | pages [25] -->
m

<!-- b003995 | furniture | pages [25] -->
m

<!-- b003996 | furniture | pages [25] -->
m

<!-- b003997 | furniture | pages [25] -->
m

<!-- b003998 | furniture | pages [25] -->
m

<!-- b003999 | furniture | pages [25] -->
m

<!-- b004000 | furniture | pages [25] -->
m

<!-- b004001 | furniture | pages [25] -->
m

<!-- b004002 | furniture | pages [25] -->
m

<!-- b004003 | furniture | pages [25] -->
m

<!-- b004004 | furniture | pages [25] -->
m

<!-- b004005 | furniture | pages [25] -->
m

<!-- b004006 | furniture | pages [25] -->
m

<!-- b004007 | furniture | pages [25] -->
m

<!-- b004008 | furniture | pages [25] -->
m

<!-- b004009 | furniture | pages [25] -->
m

<!-- b004010 | furniture | pages [25] -->
m

<!-- b004011 | furniture | pages [25] -->
m

<!-- b004012 | furniture | pages [25] -->
m

<!-- b004013 | furniture | pages [25] -->
m

<!-- b004014 | furniture | pages [25] -->
m

<!-- b004015 | furniture | pages [25] -->
m

<!-- b004016 | furniture | pages [25] -->
m

<!-- b004017 | furniture | pages [25] -->
m

<!-- b004018 | furniture | pages [25] -->
m

<!-- b004019 | furniture | pages [25] -->
m

<!-- b004020 | furniture | pages [25] -->
m

<!-- b004021 | furniture | pages [25] -->
m

<!-- b004022 | furniture | pages [25] -->
m

<!-- b004023 | furniture | pages [25] -->
m

<!-- b004024 | furniture | pages [25] -->
m

<!-- b004025 | furniture | pages [25] -->
m

<!-- b004026 | furniture | pages [25] -->
m

<!-- b004027 | furniture | pages [25] -->
m

<!-- b004028 | furniture | pages [25] -->
m

<!-- b004029 | furniture | pages [25] -->
m

<!-- b004030 | furniture | pages [25] -->
m

<!-- b004031 | furniture | pages [25] -->
m

<!-- b004032 | furniture | pages [25] -->
m

<!-- b004033 | furniture | pages [25] -->
m

<!-- b004034 | furniture | pages [25] -->
m

<!-- b004035 | furniture | pages [25] -->
m

<!-- b004036 | furniture | pages [25] -->
m

<!-- b004037 | furniture | pages [25] -->
m

<!-- b004038 | furniture | pages [25] -->
m

<!-- b004039 | furniture | pages [25] -->
m

<!-- b004040 | furniture | pages [25] -->
m

<!-- b004041 | furniture | pages [25] -->
m

<!-- b004042 | furniture | pages [25] -->
m

<!-- b004043 | furniture | pages [25] -->
m

<!-- b004044 | furniture | pages [25] -->
m

<!-- b004045 | furniture | pages [25] -->
m

<!-- b004046 | furniture | pages [25] -->
m

<!-- b004047 | furniture | pages [25] -->
m

<!-- b004048 | furniture | pages [25] -->
m

<!-- b004049 | furniture | pages [25] -->
m

<!-- b004050 | furniture | pages [25] -->
m

<!-- b004051 | furniture | pages [25] -->
m

<!-- b004052 | furniture | pages [25] -->
m

<!-- b004053 | furniture | pages [25] -->
m

<!-- b004054 | furniture | pages [25] -->
m

<!-- b004055 | furniture | pages [25] -->
m

<!-- b004056 | furniture | pages [25] -->
m

<!-- b004057 | furniture | pages [25] -->
m

<!-- b004058 | furniture | pages [25] -->
m

<!-- b004059 | furniture | pages [25] -->
m

<!-- b004060 | furniture | pages [25] -->
m

<!-- b004061 | furniture | pages [25] -->
m

<!-- b004062 | furniture | pages [25] -->
m

<!-- b004063 | furniture | pages [25] -->
m

<!-- b004064 | furniture | pages [25] -->
m

<!-- b004065 | furniture | pages [25] -->
m

<!-- b004066 | furniture | pages [25] -->
m

<!-- b004067 | furniture | pages [25] -->
m

<!-- b004068 | furniture | pages [25] -->
m

<!-- b004069 | furniture | pages [25] -->
m

<!-- b004070 | furniture | pages [25] -->
m

<!-- b004071 | furniture | pages [25] -->
m

<!-- b004072 | furniture | pages [25] -->
m

<!-- b004073 | furniture | pages [25] -->
m

<!-- b004074 | furniture | pages [25] -->
m

<!-- b004075 | furniture | pages [25] -->
m

<!-- b004076 | furniture | pages [25] -->
m

<!-- b004077 | furniture | pages [25] -->
m

<!-- b004078 | furniture | pages [25] -->
m

<!-- b004079 | furniture | pages [25] -->
m

<!-- b004080 | furniture | pages [25] -->
m

<!-- b004081 | furniture | pages [25] -->
m

<!-- b004082 | furniture | pages [25] -->
m

<!-- b004083 | furniture | pages [25] -->
m

<!-- b004084 | furniture | pages [25] -->
m

<!-- b004085 | furniture | pages [25] -->
m

<!-- b004086 | furniture | pages [25] -->
m

<!-- b004087 | furniture | pages [25] -->
m

<!-- b004088 | furniture | pages [25] -->
m

<!-- b004089 | furniture | pages [25] -->
m

<!-- b004090 | furniture | pages [25] -->
m

<!-- b004091 | furniture | pages [25] -->
m

<!-- b004092 | furniture | pages [25] -->
m

<!-- b004093 | furniture | pages [25] -->
m

<!-- b004094 | furniture | pages [25] -->
m

<!-- b004095 | furniture | pages [25] -->
m

<!-- b004096 | furniture | pages [25] -->
m

<!-- b004097 | furniture | pages [25] -->
m

<!-- b004098 | furniture | pages [25] -->
m

<!-- b004099 | furniture | pages [25] -->
m

<!-- b004100 | furniture | pages [25] -->
m

<!-- b004101 | furniture | pages [25] -->
m

<!-- b004102 | furniture | pages [25] -->
m

<!-- b004103 | furniture | pages [25] -->
m

<!-- b004104 | furniture | pages [25] -->
m

<!-- b004105 | furniture | pages [25] -->
m

<!-- b004106 | furniture | pages [25] -->
m

<!-- b004107 | furniture | pages [25] -->
m

<!-- b004108 | furniture | pages [25] -->
m

<!-- b004109 | furniture | pages [25] -->
m

<!-- b004110 | furniture | pages [25] -->
m

<!-- b004111 | furniture | pages [25] -->
m

<!-- b004112 | furniture | pages [25] -->
m

<!-- b004113 | furniture | pages [25] -->
m

<!-- b004114 | furniture | pages [25] -->
m

<!-- b004115 | furniture | pages [25] -->
m

<!-- b004116 | furniture | pages [25] -->
m

<!-- b004117 | furniture | pages [25] -->
m

<!-- b004118 | furniture | pages [25] -->
m

<!-- b004119 | furniture | pages [25] -->
m

<!-- b004120 | furniture | pages [25] -->
m

<!-- b004121 | furniture | pages [25] -->
m

<!-- b004122 | furniture | pages [25] -->
m

<!-- b004123 | furniture | pages [25] -->
m

<!-- b004124 | furniture | pages [25] -->
m

<!-- b004125 | furniture | pages [25] -->
m

<!-- b004126 | furniture | pages [25] -->
m

<!-- b004127 | furniture | pages [25] -->
m

<!-- b004128 | furniture | pages [25] -->
m

<!-- b004129 | furniture | pages [25] -->
m

<!-- b004130 | furniture | pages [25] -->
m

<!-- b004131 | furniture | pages [25] -->
m

<!-- b004132 | furniture | pages [25] -->
m

<!-- b004133 | furniture | pages [25] -->
m

<!-- b004134 | furniture | pages [25] -->
m

<!-- b004135 | furniture | pages [25] -->
m

<!-- b004136 | furniture | pages [25] -->
m

<!-- b004137 | furniture | pages [25] -->
m

<!-- b004138 | furniture | pages [25] -->
m

<!-- b004139 | furniture | pages [25] -->
m

<!-- b004140 | furniture | pages [25] -->
m

<!-- b004141 | furniture | pages [25] -->
m

<!-- b004142 | furniture | pages [25] -->
m

<!-- b004143 | furniture | pages [25] -->
m

<!-- b004144 | furniture | pages [25] -->
m

<!-- b004145 | furniture | pages [25] -->
m

<!-- b004146 | furniture | pages [25] -->
m

<!-- b004147 | furniture | pages [25] -->
m

<!-- b004148 | furniture | pages [25] -->
m

<!-- b004149 | furniture | pages [25] -->
m

<!-- b004150 | furniture | pages [25] -->
m

<!-- b004151 | furniture | pages [25] -->
m

<!-- b004152 | furniture | pages [25] -->
m

<!-- b004153 | furniture | pages [25] -->
m

<!-- b004154 | furniture | pages [25] -->
m

<!-- b004155 | furniture | pages [25] -->
m

<!-- b004156 | furniture | pages [25] -->
m

<!-- b004157 | furniture | pages [25] -->
m

<!-- b004158 | furniture | pages [25] -->
m

<!-- b004159 | furniture | pages [25] -->
m

<!-- b004160 | furniture | pages [25] -->
m

<!-- b004161 | furniture | pages [25] -->
m

<!-- b004162 | furniture | pages [25] -->
m

<!-- b004163 | furniture | pages [25] -->
m

<!-- b004164 | furniture | pages [25] -->
m

<!-- b004165 | furniture | pages [25] -->
m

<!-- b004166 | furniture | pages [25] -->
m

<!-- b004167 | furniture | pages [25] -->
m

<!-- b004168 | furniture | pages [25] -->
m

<!-- b004169 | furniture | pages [25] -->
m

<!-- b004170 | furniture | pages [25] -->
m

<!-- b004171 | furniture | pages [25] -->
m

<!-- b004172 | furniture | pages [25] -->
m

<!-- b004173 | furniture | pages [25] -->
m

<!-- b004174 | furniture | pages [25] -->
m

<!-- b004175 | furniture | pages [25] -->
m

<!-- b004176 | furniture | pages [25] -->
m

<!-- b004177 | furniture | pages [25] -->
m

<!-- b004178 | furniture | pages [25] -->
m

<!-- b004179 | furniture | pages [25] -->
m

<!-- b004180 | furniture | pages [25] -->
m

<!-- b004181 | furniture | pages [25] -->
m

<!-- b004182 | furniture | pages [25] -->
m

<!-- b004183 | furniture | pages [25] -->
m

<!-- b004184 | furniture | pages [25] -->
m

<!-- b004185 | furniture | pages [25] -->
m

<!-- b004186 | furniture | pages [25] -->
m

<!-- b004187 | furniture | pages [25] -->
m

<!-- b004188 | furniture | pages [25] -->
m

<!-- b004189 | furniture | pages [25] -->
m

<!-- b004190 | furniture | pages [25] -->
m

<!-- b004191 | furniture | pages [25] -->
m

<!-- b004192 | furniture | pages [25] -->
m

<!-- b004193 | furniture | pages [25] -->
m

<!-- b004194 | furniture | pages [25] -->
m

<!-- b004195 | furniture | pages [25] -->
m

<!-- b004196 | furniture | pages [25] -->
m

<!-- b004197 | furniture | pages [25] -->
m

<!-- b004198 | furniture | pages [25] -->
m

<!-- b004199 | furniture | pages [25] -->
m

<!-- b004200 | furniture | pages [25] -->
m

<!-- b004201 | furniture | pages [25] -->
m

<!-- b004202 | furniture | pages [25] -->
m

<!-- b004203 | furniture | pages [25] -->
m

<!-- b004204 | furniture | pages [25] -->
m

<!-- b004205 | furniture | pages [25] -->
m

<!-- b004206 | furniture | pages [25] -->
m

<!-- b004207 | furniture | pages [25] -->
m

<!-- b004208 | furniture | pages [25] -->
m

<!-- b004209 | furniture | pages [25] -->
m

<!-- b004210 | furniture | pages [25] -->
m

<!-- b004211 | furniture | pages [25] -->
m

<!-- b004212 | furniture | pages [25] -->
m

<!-- b004213 | furniture | pages [25] -->
m

<!-- b004214 | furniture | pages [25] -->
m

<!-- b004215 | furniture | pages [25] -->
m

<!-- b004216 | furniture | pages [25] -->
m

<!-- b004217 | furniture | pages [25] -->
m

<!-- b004218 | furniture | pages [25] -->
m

<!-- b004219 | furniture | pages [25] -->
m

<!-- b004220 | furniture | pages [25] -->
m

<!-- b004221 | furniture | pages [25] -->
m

<!-- b004222 | furniture | pages [25] -->
m

<!-- b004223 | furniture | pages [25] -->
m

<!-- b004224 | furniture | pages [25] -->
m

<!-- b004225 | furniture | pages [26] -->
Team # 2503268

<!-- b004226 | furniture | pages [26] -->
Page 24 of 24

<!-- b004227 | heading | pages [26] -->
Report on Use of AI

<!-- b004228 | ai_disclosure | pages [26] -->
OpenAI ChatGPT(Jan 14, 2025 version, ChatGPT-4o)

<!-- b004229 | ai_disclosure | pages [26] -->
Query: The intervention strategies are divided into tax revenue allocation and policies. Both

<!-- b004230 | ai_disclosure | pages [26] -->
parts have a ﬁnite set of typical and representative solutions. We iterate over these two sets to get a

<!-- b004231 | ai_disclosure | pages [26] -->
ﬁnite number of combinations. Now we have the previous value of H, N, T. For each combination,

<!-- b004232 | ai_disclosure | pages [26] -->
we’ll obtain diﬀerent values of new H, N, T and their corresponding scores if various constraints are

<!-- b004233 | ai_disclosure | pages [26] -->
satisﬁed. Then, pick the best score and the best combination as the current intervention strategy. Pick

<!-- b004234 | ai_disclosure | pages [26] -->
the corresponding H, N, T as the new H, N, T. Help me improve the ﬂuency and readability.

<!-- b004235 | ai_disclosure | pages [26] -->
Output: We categorize our intervention strategies into two components: tax revenue allocation

<!-- b004236 | ai_disclosure | pages [26] -->
and policies. Each component features a ﬁnite set of typical and representative solutions. By iterating

<!-- b004237 | ai_disclosure | pages [26] -->
through these solutions, we obtain a ﬁnite set of potential strategy combinations. Given the current

<!-- b004238 | ai_disclosure | pages [26] -->
values of H, N, and T, each combination, under the given constraints, produces new H, N, and T val-

<!-- b004239 | ai_disclosure | pages [26] -->
ues along with corresponding scores. We then select the combination with the highest score to serve

<!-- b004240 | ai_disclosure | pages [26] -->
as the current intervention strategy, and update H, N, and T accordingly to these new values.

<!-- b004241 | ai_disclosure | pages [26] -->
OpenAI ChatGPT(Jan 14, 2025 version, ChatGPT-4o)

<!-- b004242 | ai_disclosure | pages [26] -->
Query:Notably, the challenges faced by Juneau are not unique but part of a broader global phe-

<!-- b004243 | ai_disclosure | pages [26] -->
nomenon. Numerous destinations worldwide grapple with similar issues. For instance, Mount Rainier

<!-- b004244 | ai_disclosure | pages [26] -->
National Park in the United States has implemented reservation systems to mitigate overcrowding,

<!-- b004245 | ai_disclosure | pages [26] -->
while cities like Venice and Barcelona in Europe have introduced day-trip fees for visitors. Athens,

<!-- b004246 | ai_disclosure | pages [26] -->
Greece, is also exploring limits on tourist capacity. These examples underscore the pressing need for

<!-- b004247 | ai_disclosure | pages [26] -->
a comprehensive framework that balances economic beneﬁts with resource conservation. In response,

<!-- b004248 | ai_disclosure | pages [26] -->
our work seeks to develop a systematic and scalable model for sustainable tourism, oﬀering solu-

<!-- b004249 | ai_disclosure | pages [26] -->
tions tailored to Juneau while providing a blueprint for other destinations to address the challenges of

<!-- b004250 | ai_disclosure | pages [26] -->
overtourism and achieve long-term resilience. Simplify language.

<!-- b004251 | ai_disclosure | pages [26] -->
Output: The challenges faced by Juneau reﬂect a global issue. Destinations like Mount Rainier

<!-- b004252 | ai_disclosure | pages [26] -->
National Park use reservation systems, while Venice and Barcelona impose day-trip fees. Athens is

<!-- b004253 | ai_disclosure | pages [26] -->
exploring tourist limits, highlighting the need for a framework balancing economic beneﬁts and con-

<!-- b004254 | ai_disclosure | pages [26] -->
servation. This work aims to create a scalable model for sustainable tourism, addressing Juneau’s

<!-- b004255 | ai_disclosure | pages [26] -->
needs and oﬀering solutions for overtourism and long-term resilience.

<!-- b004256 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b004257 | furniture | pages [26] -->
2

<!-- b004258 | furniture | pages [26] -->
MATHmodels

<!-- b004259 | furniture | pages [26] -->
获取更多资讯
