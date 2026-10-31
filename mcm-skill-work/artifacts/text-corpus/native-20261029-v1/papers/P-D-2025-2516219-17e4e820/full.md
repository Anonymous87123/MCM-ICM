# P-D-2025-2516219-17e4e820

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
D

<!-- b000006 | furniture | pages [1] -->
2516219

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
A Multi-Methodological Framework for Post-Disaster

<!-- b000009 | title | pages [1] -->
Traffic Optimization and Sustainable Mobility Planning

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | title | pages [1] -->
in Baltimore

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
Urban transportation systems face critical challenges in balancing efficiency, re- silience, and sustainability, particularly under infrastructure disruptions. This study presents a multi-methodological framework to address post-disaster traffic optimiza- tion, multimodal network equity, and sustainable mobility planning in Baltimore, Mary- land.

<!-- b000014 | prose | pages [1] -->
In order to address the influence of the cascading traffic disruptions caused by the

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
collapse of the Francis Scott Key Bridge in Baltimore, a fuzzy comprehensive eval- uation model is developed to quantify multidimensional impacts, integrating flow redistribution intensity (Q), detour burden (η), network efficiency degradation (∆I), and environmental externalities (Ce). The framework employs entropy-weighted ag- gregation to prioritize factors dynamically based on historical incident data. Network dynamics are analyzed through Wardrop equilibrium-based traffic assignment and

<!-- b000017 | heading | pages [1] -->
dynamic flow conservation principles. Results reveal a 41.7% surge in bypass traffic,

<!-- b000018 | prose | pages [1] -->
0.38 efficiency loss, and $2.1M annual health costs from increased emissions.

<!-- b000019 | prose | pages [1] -->
To create public transportation projects that help improve residents’ mobility, a multimodal network model (GM = (N, E, M)) is proposed to evaluate bus-pedestrian- auto interactions. Mode-specific impedance functions incorporate stochastic waiting times, congestion penalties, and pedestrian safety risks. The framework quantifies accessibility equity using Gini coefficients and simulates Bus Rapid Transit (BRT) in- terventions, achieving a 44.1% bus mode share increase and 14.6% Gini reduction. Al- gorithmic integration of discrete choice models and network loading ensures compu- tational tractability while capturing nonlinear congestion thresholds (fb/Cb > 0.85).

<!-- b000020 | prose | pages [1] -->
To create a transportation network project that improves the lives of Baltimore resi- dents, a tri-objective optimization framework maximizes resident welfare, minimizes costs, and enhances environmental benefits through bus lane allocation (xb), pedes- trian infrastructure (xp), and micro-mobility hubs (xm). The model employs Bayesian calibration with Markov Chain Monte Carlo (MCMC) to assimilate cross-city data, resolving tradeoffs via epsilon-constraint methods. Case studies demonstrate 58% welfare gains, 18.7% PM2.5 reduction, and a benefit-cost ratio (BCR = 1.41). Critical thresholds, such as xb > 0.3Ltot for auto user cost escalation, are identified through phase transition analysis.

<!-- b000021 | prose | pages [1] -->
This research advances urban traffic management by integrating multi-scale net- work modeling, dynamic equilibrium theory, and stochastic optimization algorithms. Key methodologies actionable insights for policymakers to balance efficiency, equity, and environmental goals in complex transportation systems.

<!-- b000022 | keywords | pages [1] -->
Keywords: Traffic Flow Optimization, Fuzzy Comprehensive Evaluation, Wardrop

<!-- b000023 | prose | pages [1] -->
Equilibrium, Multimodal Transportation Network, Bayesian Calibration

<!-- b000024 | furniture | pages [3] -->
Team # 2516219

<!-- b000025 | furniture | pages [3] -->
Page 3 of 24

<!-- b000026 | prose | pages [3] -->
1

<!-- b000027 | heading | pages [3] -->
Introduction

<!-- b000028 | prose | pages [3] -->
1.1 Problem Background

<!-- b000029 | prose | pages [3] -->
Urban transportation serves as the fundamental support for residents’ daily travel. It not only directly impacts commuting efficiency, convenience of life, and travel expe- rience but also exerts profound influences on urban economic vitality, environmental

<!-- b000030 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000031 | prose | pages [3] -->
quality, and spatial layout. An efficient transportation system, as shown in Figure 1, can reduce commuting time and travel costs, thereby enhancing residents’ quality of life. Moreover, it is a crucial factor in promoting rational allocation of urban resources, driving balanced regional development, and enhancing urban attractiveness.

<!-- b000032 | prose | pages [3] -->
Baltimore, Maryland faces significant transportation challenges, including inade- quate funding for infrastructure maintenance and development, which exacerbates road conditions and strains public transit systems. The city experiences notable traffic congestion, with residents spending considerable extra time commuting during peak hours. Major incidents, such as the collapse of the Francis Scott Key Bridge in 2024, further highlight the fragility of its transportation network and the urgent need for in-

<!-- b000033 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000034 | prose | pages [3] -->
vestment. Additionally, the lack of coordinated land use and transportation planning contributes to inefficient traffic distribution. Addressing these issues requires compre- hensive strategies to improve infrastructure resilience, enhance public transit services, and integrate sustainable transportation priorities into urban development.

<!-- b000035 | prose | pages [3] -->
(a) Target City of traffic optimization (b) Map of Baltimore

<!-- b000036 | caption | pages [3] -->
Figure 1: A Roadmap to a Better City

<!-- b000037 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000038 | prose | pages [3] -->
The key factors contributing to traffic congestion in Baltimore primarily revolve around the collapse of the Francis Scott Key Bridge on March 26, 2024. The loss of this vital bridge disconnected the Baltimore Beltway (I-695) and disrupted key travel routes, particularly for commercial trucks accessing the Port of Baltimore. Through in-depth analy-sis and research on the background of the problem, combined with the specific constraints given, the restate of the problem can be expressed as follows:

<!-- b000039 | prose | pages [3] -->
• The collapse of the Francis Scott Key Bridge has significantly impacted the traf- fic flow in the Baltimore harbor area. To address this, a mathematical model is

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
needed to optimize the rebuilding process and traffic flow. This model should

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

<!-- b000727 | furniture | pages [3] -->
m

<!-- b000728 | furniture | pages [4] -->
Team # 2516219

<!-- b000729 | furniture | pages [4] -->
Page 4 of 24

<!-- b000730 | prose | pages [4] -->
consider factors such as construction time, cost, and the impact on existing traffic patterns.

<!-- b000731 | prose | pages [4] -->
• The current public rail systems (MARC, light rail, heavy rail) in Baltimore are inadequate for the needs of commuters and residents, particularly those in sub- urban areas with multiple transportation options. A mathematical model is re- quired to assess the adequacy of the rail system and its accessibility.

<!-- b000732 | prose | pages [4] -->
• A resident of Brooklyn faces challenges in using public transportation to get home after attending a football game in the city. A mathematical model is re- quired to analyze the travel experience of residents and the efficiency of the pub- lic transportation system.

<!-- b000733 | prose | pages [4] -->
1.3 Literature Review

<!-- b000734 | prose | pages [4] -->
The problem requires the team to come up with ways to improve Baltimore’s traffic to improve the lives of its residents, so the team uses the Wardrop first equilibrium principle to construct a network model.

<!-- b000735 | prose | pages [4] -->
• With the deepening of the research, scholars have expanded the Wardrop equi- librium theory in many aspects. Some studies have considered the dynamic char- acteristics of traffic flow, incorporated the time dimension into the Wardrop equi-

<!-- b000736 | prose | pages [4] -->
[1]

<!-- b000737 | prose | pages [4] -->
librium model, and proposed the dynamic Wardrop equilibrium theory.

<!-- b000738 | prose | pages [4] -->
• In the field of transportation planning, Wardrop equilibrium theory is widely used in transportation network design and traffic demand forecasting.

<!-- b000739 | prose | pages [4] -->
• In recent years, the integration of Wardrop equilibrium theory and other disci- plines has become a research hotspot.

<!-- b000740 | prose | pages [4] -->
[2] [3]The intersection with economics enables researchers to analyze traffic behavior and traffic policy from an economic point of view, and to explore the economic cost of traffic congestion and the optimal allocation of traffic resources.

<!-- b000741 | prose | pages [4] -->
The strengths and weaknesses of the planning space can be visually presented and is shown below as Figure 2:

<!-- b000742 | caption | pages [4] -->
Figure 2: Literature Review Framework

<!-- b000743 | prose | pages [4] -->
关注数学模型

<!-- b000744 | furniture | pages [4] -->
2

<!-- b000745 | furniture | pages [4] -->
MATHmodels

<!-- b000746 | furniture | pages [4] -->
获取更多资讯

<!-- b000747 | furniture | pages [5] -->
Team # 2516219

<!-- b000748 | furniture | pages [5] -->
Page 5 of 24

<!-- b000749 | prose | pages [5] -->
1.4 Our Work

<!-- b000750 | prose | pages [5] -->
Our team explored how to improve Baltimore’s transportation system through math- ematical modeling as follows:

<!-- b000751 | heading | pages [5] -->
1. The traffic network of Baltimore City is modeled as a four-tuple, the traffic density

<!-- b000752 | prose | pages [5] -->
and capacity utilization are defined. A fuzzy comprehensive evaluation framework is used to Quantitative analysis the impact of the Francis Scott Key Bridge collapse on traffic flow, and simulate the changes in traffic flow and the decline in network ef-

<!-- b000753 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000754 | prose | pages [5] -->
ficiency after the accident, and through the Wardrop equilibrium distribution prin- ciple to analyze the travel cost of residents;

<!-- b000755 | heading | pages [5] -->
2. Providing the bus rapid transit (BRT) projects to improve the lives of Baltimore res-

<!-- b000756 | prose | pages [5] -->
idents. Using a multimodal transport network to model the transport system as a directed graph, assigns travel demand using nested logit formulations, and calcu- lates multimodal accessibility potential, simulates the impact of bus rapid transit (BRT) projects.

<!-- b000757 | heading | pages [5] -->
3. An integrated transportation corridor (IMC) system is proposed to quantify resi-

<!-- b000758 | prose | pages [5] -->
dents’ welfare, implementation costs, and environmental benefits through a multi-

<!-- b000759 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000760 | prose | pages [5] -->
stage optimization process, analyze temporary network degradation during con- struction, and evaluate the impact of the IMC system on the environment, through the case of Baltimore Green Transportation Corridor, the effect of system improve- ment is demonstrated.

<!-- b000761 | prose | pages [5] -->
To give a more visual representation of our work, here is the diagram shown in

<!-- b000762 | caption | pages [5] -->
Figure 3:

<!-- b000763 | caption | pages [5] -->
Figure 3: Flow Chart of Our Work

<!-- b000764 | prose | pages [5] -->
2

<!-- b000765 | heading | pages [5] -->
Assumptions and Explanations

<!-- b000766 | prose | pages [5] -->
Considering that practical problems always contain many complex factors, first of

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
all, we need to make reasonable assumptions to simplify the model, and each hypoth-

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
esis is closely followed by its corresponding explanation:

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

<!-- b001456 | furniture | pages [6] -->
Team # 2516219

<!-- b001457 | furniture | pages [6] -->
Page 6 of 24

<!-- b001458 | heading | pages [6] -->
Assumption 1: It is assumed that the constructed traffic network completely includes

<!-- b001459 | prose | pages [6] -->
the main road nodes and sections related to the research problem in Baltimore.

<!-- b001460 | heading | pages [6] -->
Explanation: This assumption is to ensure that the model can cover the

<!-- b001461 | prose | pages [6] -->
main traffic flow paths and ignore some minor branches that have lit- tle impact on the overall analysis, so as to simplify the model structure while ensuring the accuracy of the model.

<!-- b001462 | prose | pages [6] -->
Assumption 2: It is assumed that that the edge weights of roads remain stable within

<!-- b001463 | prose | pages [6] -->
each year. Explanation: Although the number of lanes, speed limits, road condi- tions, etc. of a road may change in reality, in order to facilitate the cal- culation and analysis of the model, these factors are considered fixed within a specific study period.

<!-- b001464 | prose | pages [6] -->
Assumption 3: When analyzing the impact on a population, it is assumed that the

<!-- b001465 | prose | pages [6] -->
group has a certain degree of homogeneity and an average unit time value can be used to represent the entire group. Explanation: In reality, the time value of different residents may vary greatly, but in order to simplify the cost-benefit analysis, this assump- tion is adopted to facilitate the calculation of residents’ travel time costs and benefits.

<!-- b001466 | prose | pages [6] -->
Additional assumptions are made to simplify analysis for individual sections. These assumptions will be discussed at the appropriate locations.

<!-- b001467 | prose | pages [6] -->
3

<!-- b001468 | heading | pages [6] -->
Notations

<!-- b001469 | prose | pages [6] -->
Some important mathematical notations used in this paper are listed in Table 1.

<!-- b001470 | caption | pages [6] -->
Table 1: Notations used in this paper

<!-- b001471 | prose | pages [6] -->
Symbol

<!-- b001472 | prose | pages [6] -->
G = (V, E, a, W)

<!-- b001473 | prose | pages [6] -->
Description

<!-- b001474 | prose | pages [6] -->
Quaternary representation of traffic networks V = {vi}n

<!-- b001475 | prose | pages [6] -->
A collection of nodes representing an intersection i=1 E ⊆V × V Set of directed edges representing road segments A : E →Rd Edge attribute function, which represents the attributes of the road W : V →Rk A node weight function that represents the weight of the node

<!-- b001476 | prose | pages [6] -->
*There are some variables that are not listed here and will be discussed in detail in each section.

<!-- b001477 | heading | pages [6] -->
Preparation before Solution

<!-- b001478 | prose | pages [6] -->
4

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
m m

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
m m

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
m m

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
4.1

<!-- b001534 | heading | pages [6] -->
Data Collection

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
m m

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
m m

<!-- b001579 | prose | pages [6] -->
m m

<!-- b001580 | prose | pages [6] -->
m m

<!-- b001581 | prose | pages [6] -->
m m

<!-- b001582 | prose | pages [6] -->
m

<!-- b001583 | prose | pages [6] -->
m

<!-- b001584 | prose | pages [6] -->
m

<!-- b001585 | prose | pages [6] -->
m

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
m m

<!-- b001595 | prose | pages [6] -->
m m

<!-- b001596 | prose | pages [6] -->
m m

<!-- b001597 | prose | pages [6] -->
m m

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
m m

<!-- b001610 | prose | pages [6] -->
m m

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
m m

<!-- b001621 | prose | pages [6] -->
m m

<!-- b001622 | prose | pages [6] -->
m m

<!-- b001623 | prose | pages [6] -->
m m

<!-- b001624 | prose | pages [6] -->
m m

<!-- b001625 | prose | pages [6] -->
m m

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
m m

<!-- b001637 | prose | pages [6] -->
m m

<!-- b001638 | prose | pages [6] -->
m m

<!-- b001639 | prose | pages [6] -->
m m

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
m m

<!-- b001655 | prose | pages [6] -->
m m

<!-- b001656 | prose | pages [6] -->
m m

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
m m

<!-- b001667 | prose | pages [6] -->
m m

<!-- b001668 | prose | pages [6] -->
m m

<!-- b001669 | prose | pages [6] -->
m m

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
m m

<!-- b001683 | prose | pages [6] -->
m m

<!-- b001684 | prose | pages [6] -->
m m

<!-- b001685 | prose | pages [6] -->
m m

<!-- b001686 | prose | pages [6] -->
m m

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
m m

<!-- b001699 | prose | pages [6] -->
m m

<!-- b001700 | prose | pages [6] -->
m m

<!-- b001701 | prose | pages [6] -->
m m

<!-- b001702 | prose | pages [6] -->
m m

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
m m

<!-- b001718 | prose | pages [6] -->
m m

<!-- b001719 | prose | pages [6] -->
m m

<!-- b001720 | prose | pages [6] -->
m m

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
m m

<!-- b001736 | prose | pages [6] -->
m m

<!-- b001737 | prose | pages [6] -->
m m

<!-- b001738 | prose | pages [6] -->
m m

<!-- b001739 | prose | pages [6] -->
m m

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
m m

<!-- b001754 | prose | pages [6] -->
m m

<!-- b001755 | prose | pages [6] -->
m m

<!-- b001756 | prose | pages [6] -->
m m

<!-- b001757 | prose | pages [6] -->
m m

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
m m

<!-- b001772 | prose | pages [6] -->
m m

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
m m

<!-- b001785 | prose | pages [6] -->
m m

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
m m

<!-- b001800 | prose | pages [6] -->
m m

<!-- b001801 | prose | pages [6] -->
m m

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
m m

<!-- b001820 | prose | pages [6] -->
m m

<!-- b001821 | prose | pages [6] -->
m m

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
m m

<!-- b001831 | prose | pages [6] -->
m m

<!-- b001832 | prose | pages [6] -->
m m

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
m m

<!-- b001843 | prose | pages [6] -->
m m

<!-- b001844 | prose | pages [6] -->
m m

<!-- b001845 | prose | pages [6] -->
m m

<!-- b001846 | prose | pages [6] -->
m m

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
m m

<!-- b001861 | prose | pages [6] -->
m m

<!-- b001862 | prose | pages [6] -->
m m

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
m m

<!-- b001874 | prose | pages [6] -->
m m

<!-- b001875 | prose | pages [6] -->
m m

<!-- b001876 | prose | pages [6] -->
m m

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
m m

<!-- b001893 | prose | pages [6] -->
m m

<!-- b001894 | prose | pages [6] -->
m m

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
m m

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
m m

<!-- b001924 | prose | pages [6] -->
m m

<!-- b001925 | prose | pages [6] -->
m m

<!-- b001926 | prose | pages [6] -->
m m

<!-- b001927 | prose | pages [6] -->
m m

<!-- b001928 | prose | pages [6] -->
m m

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
m

<!-- b001942 | prose | pages [6] -->
m m

<!-- b001943 | prose | pages [6] -->
m m

<!-- b001944 | prose | pages [6] -->
m m

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
m m

<!-- b001956 | prose | pages [6] -->
m m

<!-- b001957 | prose | pages [6] -->
m m

<!-- b001958 | prose | pages [6] -->
m m

<!-- b001959 | prose | pages [6] -->
m m

<!-- b001960 | prose | pages [6] -->
m m

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
m m

<!-- b001975 | prose | pages [6] -->
m m

<!-- b001976 | prose | pages [6] -->
m m

<!-- b001977 | prose | pages [6] -->
m m

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
m m

<!-- b001987 | prose | pages [6] -->
m m

<!-- b001988 | prose | pages [6] -->
m m

<!-- b001989 | prose | pages [6] -->
m m

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
m m

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
m m

<!-- b002014 | prose | pages [6] -->
m m

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
m m

<!-- b002029 | prose | pages [6] -->
m m

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
m m

<!-- b002038 | prose | pages [6] -->
m m

<!-- b002039 | prose | pages [6] -->
m m

<!-- b002040 | prose | pages [6] -->
m m

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
m m

<!-- b002057 | prose | pages [6] -->
m m

<!-- b002058 | prose | pages [6] -->
m m

<!-- b002059 | prose | pages [6] -->
m m

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
m m

<!-- b002074 | prose | pages [6] -->
m m

<!-- b002075 | prose | pages [6] -->
m m

<!-- b002076 | prose | pages [6] -->
m m

<!-- b002077 | prose | pages [6] -->
m m

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
m m

<!-- b002096 | prose | pages [6] -->
m m

<!-- b002097 | prose | pages [6] -->
m m

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
m m

<!-- b002109 | prose | pages [6] -->
m m

<!-- b002110 | prose | pages [6] -->
m m

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
The following data files were received in this competition at 2025_Problem_D_Data.zip.

<!-- b002123 | prose | pages [6] -->
m m

<!-- b002124 | prose | pages [6] -->
m

<!-- b002125 | prose | pages [6] -->
m

<!-- b002126 | prose | pages [6] -->
m

<!-- b002127 | prose | pages [6] -->
m

<!-- b002128 | prose | pages [6] -->
m

<!-- b002129 | prose | pages [6] -->
m m

<!-- b002130 | prose | pages [6] -->
m m

<!-- b002131 | prose | pages [6] -->
m m

<!-- b002132 | prose | pages [6] -->
m m

<!-- b002133 | prose | pages [6] -->
m m

<!-- b002134 | prose | pages [6] -->
m

<!-- b002135 | prose | pages [6] -->
m

<!-- b002136 | prose | pages [6] -->
m

<!-- b002137 | prose | pages [6] -->
m

<!-- b002138 | prose | pages [6] -->
m

<!-- b002139 | prose | pages [6] -->
m

<!-- b002140 | prose | pages [6] -->
m

<!-- b002141 | prose | pages [6] -->
m

<!-- b002142 | prose | pages [6] -->
m

<!-- b002143 | prose | pages [6] -->
m

<!-- b002144 | prose | pages [6] -->
m

<!-- b002145 | prose | pages [6] -->
m m

<!-- b002146 | prose | pages [6] -->
m m

<!-- b002147 | prose | pages [6] -->
m m

<!-- b002148 | prose | pages [6] -->
m m

<!-- b002149 | prose | pages [6] -->
m m

<!-- b002150 | prose | pages [6] -->
m m

<!-- b002151 | prose | pages [6] -->
m

<!-- b002152 | prose | pages [6] -->
m

<!-- b002153 | prose | pages [6] -->
m

<!-- b002154 | prose | pages [6] -->
m

<!-- b002155 | prose | pages [6] -->
m

<!-- b002156 | prose | pages [6] -->
m

<!-- b002157 | prose | pages [6] -->
m

<!-- b002158 | prose | pages [6] -->
m

<!-- b002159 | prose | pages [6] -->
m

<!-- b002160 | prose | pages [6] -->
m

<!-- b002161 | prose | pages [6] -->
m

<!-- b002162 | prose | pages [6] -->
m

<!-- b002163 | prose | pages [6] -->
m

<!-- b002164 | prose | pages [6] -->
The zip files contain all 9 of the data files listed below. To enlarge data and supplement

<!-- b002165 | prose | pages [6] -->
关注数学模型

<!-- b002166 | prose | pages [6] -->
some missing data, we collect the data at https://maps.roads.maryland.gov/.

<!-- b002167 | furniture | pages [6] -->
2

<!-- b002168 | furniture | pages [6] -->
MATHmodels

<!-- b002169 | furniture | pages [6] -->
获取更多资讯

<!-- b002170 | furniture | pages [7] -->
Team # 2516219

<!-- b002171 | furniture | pages [7] -->
Page 7 of 24

<!-- b002172 | caption | pages [7] -->
Table 2: Data and Database Websites

<!-- b002173 | prose | pages [7] -->
Database Names

<!-- b002174 | prose | pages [7] -->
Bus_Routes.csv Bus_Stops.csv

<!-- b002175 | prose | pages [7] -->
Database description

<!-- b002176 | prose | pages [7] -->
The locations of MTA bus routes The locations of MTA bus routes The locations of tagged geographic attributes nodes_all.csv

<!-- b002177 | prose | pages [7] -->
微信公众号：数学模型

<!-- b002178 | prose | pages [7] -->
The locations of tagged geographic attributes for car travel nodes_drive.csv The locations of tagged geographic attributes edges_all.csv The locations of tagged geographic attributes edges_drive.csv AAWDT.csv Edge_Names_With_Nodes.csv Traffic volume information Provide street names with nodes Describes the features in each of the data sets DataDictionary.csv

<!-- b002179 | prose | pages [7] -->
4.2

<!-- b002180 | heading | pages [7] -->
Data processing

<!-- b002181 | prose | pages [7] -->
微信号：MATHmodels

<!-- b002182 | prose | pages [7] -->
Due to data collection reasons, there are definitely outliers and missing values in such a large amount of data in this article. The existence of outliers and missing val- ues has a significant impact on the analysis results. Therefore, before establishing a solution, this article uses the 3sigma principle based on the normal distribution to de- termine the range of data outliers.

<!-- b002183 | prose | pages [7] -->
For numerical data, like AADT and AAWDT in MDOT_SHA_Annual_Average_ Daily_Traffic_Baltimore.csv, assume a data set {x1, x2, · · · , xn} containing n data points, and the calculation formulas for its mean µ and standard deviation σ are:

<!-- b002184 | prose | pages [7] -->
n

<!-- b002185 | prose | pages [7] -->
µ = 1

<!-- b002186 | prose | pages [7] -->
X

<!-- b002187 | prose | pages [7] -->
xi, σ =

<!-- b002188 | prose | pages [7] -->
n

<!-- b002189 | prose | pages [7] -->
i=1

<!-- b002190 | prose | pages [7] -->
v

<!-- b002191 | prose | pages [7] -->
n

<!-- b002192 | prose | pages [7] -->
u t1

<!-- b002193 | prose | pages [7] -->
X

<!-- b002194 | prose | pages [7] -->
u

<!-- b002195 | prose | pages [7] -->
(xi −µ)2 (1)

<!-- b002196 | prose | pages [7] -->
n

<!-- b002197 | prose | pages [7] -->
i=1

<!-- b002198 | prose | pages [7] -->
Based on the 3sigma principle of normal distribution, the lower limit of the normal data range is µ −3σ and the upper limit is µ + 3σ. Abnormal values outside this range are replaced by the mean. At the same time, missing values are replaced by the mean.

<!-- b002199 | prose | pages [7] -->
In the context of text-type data, a specific rule is established: missing values within this data type are to be filled with zeros. When text-based data undergoes a transfor- mation process to numerical data via One-Hot Encoding, it is observed that the missing data entries located on the main diagonal of the resulting matrix are represented as 0, using Route Prefix in MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv as follows:

<!-- b002200 | prose | pages [7] -->
Route Prefix

<!-- b002201 | prose | pages [7] -->
⇒

<!-- b002202 | prose | pages [7] -->


<!-- b002203 | prose | pages [7] -->


<!-- b002204 | prose | pages [7] -->


<!-- b002205 | prose | pages [7] -->
MU

<!-- b002206 | prose | pages [7] -->
CO

<!-- b002207 | prose | pages [7] -->


<!-- b002208 | prose | pages [7] -->


<!-- b002209 | prose | pages [7] -->


<!-- b002210 | prose | pages [7] -->
... MD

<!-- b002211 | prose | pages [7] -->
· · · MU CO MD

<!-- b002212 | prose | pages [7] -->
(2)

<!-- b002213 | prose | pages [7] -->


<!-- b002214 | prose | pages [7] -->
1 1 1

<!-- b002215 | prose | pages [7] -->


<!-- b002216 | prose | pages [7] -->
...

<!-- b002217 | prose | pages [7] -->
1

<!-- b002218 | furniture | pages [8] -->
Team # 2516219

<!-- b002219 | furniture | pages [8] -->
Page 8 of 24

<!-- b002220 | prose | pages [8] -->
Network-Theoretic Framework for Urban Traffic Flow 5 Analysis

<!-- b002221 | prose | pages [8] -->
5.1 Network Representation

<!-- b002222 | prose | pages [8] -->
Before analyzing the impact of the Francis Scott Key Bridge, we model Baltimore’s transportation network G as a 4-tuple: G = (V, E, A, W), where V = {vi}n

<!-- b002223 | prose | pages [8] -->
i=1 is a set of nodes through edges_all.csv, E ⊆V × V directed edges (road segments) through edges_all.csv, A : E →Rd denotes Edge attribute function, W : V →Rk denotes Node weighting function.

<!-- b002224 | prose | pages [8] -->
The transportation network comprises two fundamental topological elements: in- tersections (nodes) and road segments (edges), each characterized by distinct geomet- ric and functional attributes.

<!-- b002225 | prose | pages [8] -->
Each intersection node vi ∈V is formally defined as a quadruple Node Structure encapsulating its essential properties:

<!-- b002226 | prose | pages [8] -->
vi = ⟨IDi, (lati, loni), Ci, {ej}j∈adj(i)⟩, (3)

<!-- b002227 | prose | pages [8] -->
where IDi denotes the unique topological identifier, (lati, loni) ∈R2 specifies ge- ographic coordinates in WGS84 datum, Ci represents capacity constraints governing vehicular throughput at the intersection, and {ej}j∈adj(i) enumerates all incident edges (both incoming and outgoing) that connect to the node.

<!-- b002228 | prose | pages [8] -->
Directed edges eij ∈E connecting node vi to vj are mathe- Edge Characterization matically described through a triple structure eij⟨IDij, Φij, Ψij⟩

<!-- b002229 | prose | pages [8] -->
The traffic attribute vector Φij integrates critical mobility metrics:

<!-- b002230 | prose | pages [8] -->


<!-- b002231 | prose | pages [8] -->


<!-- b002232 | prose | pages [8] -->
AADTij, AAWDTij, AADTij

<!-- b002233 | prose | pages [8] -->
Φij =

<!-- b002234 | prose | pages [8] -->
m

<!-- b002235 | prose | pages [8] -->
m

<!-- b002236 | prose | pages [8] -->
m

<!-- b002237 | prose | pages [8] -->
m

<!-- b002238 | prose | pages [8] -->
m

<!-- b002239 | prose | pages [8] -->
m

<!-- b002240 | prose | pages [8] -->
m

<!-- b002241 | prose | pages [8] -->
m

<!-- b002242 | prose | pages [8] -->
m

<!-- b002243 | prose | pages [8] -->
m

<!-- b002244 | prose | pages [8] -->
m

<!-- b002245 | prose | pages [8] -->
m

<!-- b002246 | prose | pages [8] -->
m

<!-- b002247 | prose | pages [8] -->
m

<!-- b002248 | prose | pages [8] -->
m

<!-- b002249 | prose | pages [8] -->
m

<!-- b002250 | prose | pages [8] -->
m

<!-- b002251 | prose | pages [8] -->
m

<!-- b002252 | prose | pages [8] -->
m

<!-- b002253 | prose | pages [8] -->
m

<!-- b002254 | prose | pages [8] -->
m

<!-- b002255 | prose | pages [8] -->
m

<!-- b002256 | prose | pages [8] -->
m

<!-- b002257 | prose | pages [8] -->
m

<!-- b002258 | prose | pages [8] -->
m

<!-- b002259 | prose | pages [8] -->
m

<!-- b002260 | prose | pages [8] -->
m

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
m

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
, {vc}c∈V

<!-- b002466 | prose | pages [8] -->
, (4)

<!-- b002467 | prose | pages [8] -->
lij

<!-- b002468 | prose | pages [8] -->
where AADTij (Annual Average Daily Traffic) and AAWDTij (Annual Average

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
m

<!-- b002611 | prose | pages [8] -->
m

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
AADTij

<!-- b002626 | prose | pages [8] -->
expresses traffic density

<!-- b002627 | prose | pages [8] -->
Weekday Traffic) quantify temporal traffic patterns,

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
m

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
lij per unit length, and {vc} details vehicle class distributions following FHWA catego-

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
rization.

<!-- b002930 | prose | pages [8] -->
Geometric properties are encoded in Ψij (lij, θij, κij, τij), with lij ∈R+ denoting seg- ment length (meters), θij ∈{0, 1} indicating directionality (bidirectional or one-way), κij ∈[0, 1] quantifying normalized curvature derived from differential geometry, and τij specifying functional classification per FHWA hierarchy (e.g., arterial, collector, lo- cal). This dual attribute schema enables simultaneous analysis of traffic dynamics and physical infrastructure characteristics. The established traffic flow network is visual- ized as shown in the figure 4: 5.2

<!-- b002931 | heading | pages [8] -->
Traffic Flow Modeling

<!-- b002932 | prose | pages [8] -->
The proposed framework establishes fundamental relationships for characterizing traffic dynamics through mathematically rigorous formulations. Segment flow density

<!-- b002933 | prose | pages [8] -->
关注数学模型

<!-- b002934 | prose | pages [8] -->
serves as a critical metric for evaluating traffic intensity, defined as the ratio of annual

<!-- b002935 | furniture | pages [8] -->
2

<!-- b002936 | furniture | pages [8] -->
MATHmodels

<!-- b002937 | furniture | pages [8] -->
获取更多资讯

<!-- b002938 | furniture | pages [9] -->
Team # 2516219

<!-- b002939 | furniture | pages [9] -->
Page 9 of 24

<!-- b002940 | caption | pages [9] -->
Figure 4: Baltimore map and highway visualization

<!-- b002941 | prose | pages [9] -->
微信公众号：数学模型

<!-- b002942 | prose | pages [9] -->
average daily traffic (AADT) to both temporal and spatial dimensions. This relation- ship is expressed as:

<!-- b002943 | prose | pages [9] -->
ρij = AADTij

<!-- b002944 | prose | pages [9] -->
24 · lij · ¯v−1 [veh/km], (5) ij

<!-- b002945 | prose | pages [9] -->
where ρij quantifies vehicle concentration per kilometer, AADTij represents the an- nualized traffic volume on edge eij, lij denotes segment length in kilometers, and ¯vij indicates the time-weighted average speed derived from observational data. Comple- menting this density measure, the capacity utilization ratio evaluates infrastructure

<!-- b002946 | prose | pages [9] -->
微信号：MATHmodels

<!-- b002947 | prose | pages [9] -->
stress through normalized traffic-to-capacity comparison:

<!-- b002948 | prose | pages [9] -->
uij = AADTij

<!-- b002949 | prose | pages [9] -->
Cij

<!-- b002950 | prose | pages [9] -->
∈[0, 1], (6)

<!-- b002951 | prose | pages [9] -->
where Cij corresponds to the theoretical maximum daily vehicle throughput de- termined by roadway geometrics and operational conditions, following Highway Ca- pacity Manual guidelines. Network-level flow conservation principles ensure mass balance across transportation nodes, formalized through nodal inflow-outflow equilib- rium. For any intersection vi ∈V , the algebraic summation of traffic volumes adheres to:

<!-- b002952 | prose | pages [9] -->
X

<!-- b002953 | prose | pages [9] -->
AADTki + Gi =

<!-- b002954 | prose | pages [9] -->
eki∈Ein(i)

<!-- b002955 | prose | pages [9] -->
X

<!-- b002956 | prose | pages [9] -->
AADTij + Li.

<!-- b002957 | prose | pages [9] -->
(7)

<!-- b002958 | prose | pages [9] -->
eij∈Eout(i)

<!-- b002959 | prose | pages [9] -->
Here, Ein(i) and Eout(i) respectively denote incoming and outgoing edge sets, Gi captures trip generation from adjacent land uses, and Li accounts for traffic dissipa- tion due to parking or destination arrival. This conservation law enables system-wide consistency checks and forms the basis for origin-destination matrix estimation when combined with supplementary mobility surveys. The integration of these microscopic and macroscopic relationships facilitates multi-scale analysis of traffic patterns, from individual corridor performance to metropolitan-scale network efficiency assessments.

<!-- b002960 | prose | pages [9] -->
Analytical Metrics and Data Integration 5.3

<!-- b002961 | prose | pages [9] -->
The framework introduces composite metrics for evaluating network criticality and resilience through topological-flow synthesis. Edge betweenness centrality quantifies

<!-- b002962 | furniture | pages [10] -->
Team # 2516219

<!-- b002963 | furniture | pages [10] -->
m

<!-- b002964 | furniture | pages [10] -->
m

<!-- b002965 | furniture | pages [10] -->
m

<!-- b002966 | furniture | pages [10] -->
m

<!-- b002967 | furniture | pages [10] -->
m

<!-- b002968 | furniture | pages [10] -->
m

<!-- b002969 | furniture | pages [10] -->
m

<!-- b002970 | furniture | pages [10] -->
m

<!-- b002971 | furniture | pages [10] -->
m

<!-- b002972 | furniture | pages [10] -->
m

<!-- b002973 | furniture | pages [10] -->
m

<!-- b002974 | furniture | pages [10] -->
m

<!-- b002975 | furniture | pages [10] -->
m

<!-- b002976 | furniture | pages [10] -->
m

<!-- b002977 | furniture | pages [10] -->
m

<!-- b002978 | furniture | pages [10] -->
m

<!-- b002979 | furniture | pages [10] -->
m

<!-- b002980 | furniture | pages [10] -->
m

<!-- b002981 | furniture | pages [10] -->
m

<!-- b002982 | furniture | pages [10] -->
m

<!-- b002983 | furniture | pages [10] -->
m

<!-- b002984 | furniture | pages [10] -->
m

<!-- b002985 | furniture | pages [10] -->
m

<!-- b002986 | furniture | pages [10] -->
m

<!-- b002987 | furniture | pages [10] -->
m

<!-- b002988 | furniture | pages [10] -->
m

<!-- b002989 | furniture | pages [10] -->
m

<!-- b002990 | furniture | pages [10] -->
m

<!-- b002991 | furniture | pages [10] -->
m

<!-- b002992 | furniture | pages [10] -->
m

<!-- b002993 | furniture | pages [10] -->
m

<!-- b002994 | furniture | pages [10] -->
m

<!-- b002995 | furniture | pages [10] -->
m

<!-- b002996 | furniture | pages [10] -->
m

<!-- b002997 | furniture | pages [10] -->
m

<!-- b002998 | furniture | pages [10] -->
m

<!-- b002999 | furniture | pages [10] -->
m

<!-- b003000 | furniture | pages [10] -->
m

<!-- b003001 | prose | pages [10] -->
m

<!-- b003002 | prose | pages [10] -->
m

<!-- b003003 | prose | pages [10] -->
m

<!-- b003004 | prose | pages [10] -->
m

<!-- b003005 | prose | pages [10] -->
m

<!-- b003006 | prose | pages [10] -->
m

<!-- b003007 | prose | pages [10] -->
m

<!-- b003008 | prose | pages [10] -->
m

<!-- b003009 | prose | pages [10] -->
m

<!-- b003010 | prose | pages [10] -->
m

<!-- b003011 | prose | pages [10] -->
m

<!-- b003012 | prose | pages [10] -->
m

<!-- b003013 | prose | pages [10] -->
m

<!-- b003014 | prose | pages [10] -->
m

<!-- b003015 | prose | pages [10] -->
m

<!-- b003016 | prose | pages [10] -->
m

<!-- b003017 | prose | pages [10] -->
m

<!-- b003018 | prose | pages [10] -->
m

<!-- b003019 | prose | pages [10] -->
m

<!-- b003020 | prose | pages [10] -->
m

<!-- b003021 | prose | pages [10] -->
m

<!-- b003022 | prose | pages [10] -->
m

<!-- b003023 | prose | pages [10] -->
m

<!-- b003024 | prose | pages [10] -->
m

<!-- b003025 | prose | pages [10] -->
m

<!-- b003026 | prose | pages [10] -->
m

<!-- b003027 | prose | pages [10] -->
m

<!-- b003028 | prose | pages [10] -->
m

<!-- b003029 | prose | pages [10] -->
m

<!-- b003030 | prose | pages [10] -->
m

<!-- b003031 | prose | pages [10] -->
m

<!-- b003032 | prose | pages [10] -->
m

<!-- b003033 | prose | pages [10] -->
m

<!-- b003034 | prose | pages [10] -->
m

<!-- b003035 | prose | pages [10] -->
m

<!-- b003036 | prose | pages [10] -->
m

<!-- b003037 | prose | pages [10] -->
m

<!-- b003038 | prose | pages [10] -->
m

<!-- b003039 | prose | pages [10] -->
m

<!-- b003040 | prose | pages [10] -->
m

<!-- b003041 | prose | pages [10] -->
m

<!-- b003042 | prose | pages [10] -->
m

<!-- b003043 | prose | pages [10] -->
m

<!-- b003044 | prose | pages [10] -->
m

<!-- b003045 | prose | pages [10] -->
m

<!-- b003046 | prose | pages [10] -->
m

<!-- b003047 | prose | pages [10] -->
m

<!-- b003048 | prose | pages [10] -->
m

<!-- b003049 | prose | pages [10] -->
m

<!-- b003050 | prose | pages [10] -->
m

<!-- b003051 | prose | pages [10] -->
m

<!-- b003052 | prose | pages [10] -->
m

<!-- b003053 | prose | pages [10] -->
m

<!-- b003054 | prose | pages [10] -->
m

<!-- b003055 | prose | pages [10] -->
m

<!-- b003056 | prose | pages [10] -->
m

<!-- b003057 | prose | pages [10] -->
m

<!-- b003058 | prose | pages [10] -->
m

<!-- b003059 | prose | pages [10] -->
m

<!-- b003060 | prose | pages [10] -->
m

<!-- b003061 | prose | pages [10] -->
m

<!-- b003062 | prose | pages [10] -->
m

<!-- b003063 | prose | pages [10] -->
m

<!-- b003064 | prose | pages [10] -->
m

<!-- b003065 | prose | pages [10] -->
m

<!-- b003066 | prose | pages [10] -->
m

<!-- b003067 | prose | pages [10] -->
m

<!-- b003068 | prose | pages [10] -->
m

<!-- b003069 | prose | pages [10] -->
m

<!-- b003070 | prose | pages [10] -->
m

<!-- b003071 | prose | pages [10] -->
m

<!-- b003072 | prose | pages [10] -->
m

<!-- b003073 | prose | pages [10] -->
m

<!-- b003074 | prose | pages [10] -->
m

<!-- b003075 | prose | pages [10] -->
m

<!-- b003076 | prose | pages [10] -->
m

<!-- b003077 | prose | pages [10] -->
m

<!-- b003078 | prose | pages [10] -->
m

<!-- b003079 | prose | pages [10] -->
m

<!-- b003080 | prose | pages [10] -->
m

<!-- b003081 | prose | pages [10] -->
m

<!-- b003082 | prose | pages [10] -->
m

<!-- b003083 | prose | pages [10] -->
m

<!-- b003084 | prose | pages [10] -->
m

<!-- b003085 | prose | pages [10] -->
m

<!-- b003086 | prose | pages [10] -->
m

<!-- b003087 | prose | pages [10] -->
m

<!-- b003088 | prose | pages [10] -->
m

<!-- b003089 | prose | pages [10] -->
m

<!-- b003090 | prose | pages [10] -->
m

<!-- b003091 | prose | pages [10] -->
m

<!-- b003092 | prose | pages [10] -->
m

<!-- b003093 | prose | pages [10] -->
m

<!-- b003094 | prose | pages [10] -->
m

<!-- b003095 | prose | pages [10] -->
m

<!-- b003096 | prose | pages [10] -->
m

<!-- b003097 | prose | pages [10] -->
m

<!-- b003098 | prose | pages [10] -->
m

<!-- b003099 | prose | pages [10] -->
m

<!-- b003100 | prose | pages [10] -->
m

<!-- b003101 | prose | pages [10] -->
m

<!-- b003102 | prose | pages [10] -->
m

<!-- b003103 | prose | pages [10] -->
m

<!-- b003104 | prose | pages [10] -->
m

<!-- b003105 | prose | pages [10] -->
m

<!-- b003106 | prose | pages [10] -->
m

<!-- b003107 | prose | pages [10] -->
m

<!-- b003108 | prose | pages [10] -->
m

<!-- b003109 | prose | pages [10] -->
m

<!-- b003110 | prose | pages [10] -->
m

<!-- b003111 | prose | pages [10] -->
m

<!-- b003112 | prose | pages [10] -->
m

<!-- b003113 | prose | pages [10] -->
m

<!-- b003114 | prose | pages [10] -->
m

<!-- b003115 | prose | pages [10] -->
m

<!-- b003116 | prose | pages [10] -->
m

<!-- b003117 | prose | pages [10] -->
m

<!-- b003118 | prose | pages [10] -->
m

<!-- b003119 | prose | pages [10] -->
m

<!-- b003120 | prose | pages [10] -->
m

<!-- b003121 | prose | pages [10] -->
m

<!-- b003122 | prose | pages [10] -->
m

<!-- b003123 | prose | pages [10] -->
m

<!-- b003124 | prose | pages [10] -->
m

<!-- b003125 | prose | pages [10] -->
m

<!-- b003126 | prose | pages [10] -->
m

<!-- b003127 | prose | pages [10] -->
m

<!-- b003128 | prose | pages [10] -->
m

<!-- b003129 | prose | pages [10] -->
m

<!-- b003130 | furniture | pages [10] -->
Page 10 of 24

<!-- b003131 | prose | pages [10] -->
a roadway segment’s structural importance by measuring its participation in shortest-

<!-- b003132 | prose | pages [10] -->
m

<!-- b003133 | prose | pages [10] -->
m

<!-- b003134 | prose | pages [10] -->
m

<!-- b003135 | prose | pages [10] -->
m

<!-- b003136 | prose | pages [10] -->
m

<!-- b003137 | prose | pages [10] -->
m

<!-- b003138 | prose | pages [10] -->
m

<!-- b003139 | prose | pages [10] -->
m

<!-- b003140 | prose | pages [10] -->
m

<!-- b003141 | prose | pages [10] -->
m

<!-- b003142 | prose | pages [10] -->
m

<!-- b003143 | prose | pages [10] -->
m

<!-- b003144 | prose | pages [10] -->
m

<!-- b003145 | prose | pages [10] -->
m

<!-- b003146 | prose | pages [10] -->
m

<!-- b003147 | prose | pages [10] -->
m

<!-- b003148 | prose | pages [10] -->
m

<!-- b003149 | prose | pages [10] -->
m

<!-- b003150 | prose | pages [10] -->
m

<!-- b003151 | prose | pages [10] -->
m

<!-- b003152 | prose | pages [10] -->
m

<!-- b003153 | prose | pages [10] -->
m

<!-- b003154 | prose | pages [10] -->
m

<!-- b003155 | prose | pages [10] -->
m

<!-- b003156 | prose | pages [10] -->
m

<!-- b003157 | prose | pages [10] -->
m

<!-- b003158 | prose | pages [10] -->
m

<!-- b003159 | prose | pages [10] -->
m

<!-- b003160 | prose | pages [10] -->
m

<!-- b003161 | prose | pages [10] -->
m

<!-- b003162 | prose | pages [10] -->
m

<!-- b003163 | prose | pages [10] -->
m

<!-- b003164 | prose | pages [10] -->
m

<!-- b003165 | prose | pages [10] -->
m

<!-- b003166 | prose | pages [10] -->
m

<!-- b003167 | prose | pages [10] -->
m

<!-- b003168 | prose | pages [10] -->
m

<!-- b003169 | prose | pages [10] -->
m

<!-- b003170 | prose | pages [10] -->
m

<!-- b003171 | prose | pages [10] -->
m

<!-- b003172 | prose | pages [10] -->
m

<!-- b003173 | prose | pages [10] -->
m

<!-- b003174 | prose | pages [10] -->
m

<!-- b003175 | prose | pages [10] -->
m

<!-- b003176 | prose | pages [10] -->
m

<!-- b003177 | prose | pages [10] -->
m

<!-- b003178 | prose | pages [10] -->
m

<!-- b003179 | prose | pages [10] -->
m

<!-- b003180 | prose | pages [10] -->
m

<!-- b003181 | prose | pages [10] -->
m

<!-- b003182 | prose | pages [10] -->
m

<!-- b003183 | prose | pages [10] -->
m

<!-- b003184 | prose | pages [10] -->
m

<!-- b003185 | prose | pages [10] -->
m

<!-- b003186 | prose | pages [10] -->
m

<!-- b003187 | prose | pages [10] -->
m

<!-- b003188 | prose | pages [10] -->
m

<!-- b003189 | prose | pages [10] -->
m

<!-- b003190 | prose | pages [10] -->
m

<!-- b003191 | prose | pages [10] -->
m

<!-- b003192 | prose | pages [10] -->
m

<!-- b003193 | prose | pages [10] -->
m

<!-- b003194 | prose | pages [10] -->
m

<!-- b003195 | prose | pages [10] -->
m

<!-- b003196 | prose | pages [10] -->
m

<!-- b003197 | prose | pages [10] -->
m

<!-- b003198 | prose | pages [10] -->
m

<!-- b003199 | prose | pages [10] -->
m

<!-- b003200 | prose | pages [10] -->
m

<!-- b003201 | prose | pages [10] -->
m

<!-- b003202 | prose | pages [10] -->
m

<!-- b003203 | prose | pages [10] -->
m

<!-- b003204 | prose | pages [10] -->
m

<!-- b003205 | prose | pages [10] -->
m

<!-- b003206 | prose | pages [10] -->
m

<!-- b003207 | prose | pages [10] -->
m

<!-- b003208 | prose | pages [10] -->
m

<!-- b003209 | prose | pages [10] -->
m

<!-- b003210 | prose | pages [10] -->
m

<!-- b003211 | prose | pages [10] -->
m

<!-- b003212 | prose | pages [10] -->
m

<!-- b003213 | prose | pages [10] -->
m

<!-- b003214 | prose | pages [10] -->
m

<!-- b003215 | prose | pages [10] -->
m

<!-- b003216 | prose | pages [10] -->
m

<!-- b003217 | prose | pages [10] -->
m

<!-- b003218 | prose | pages [10] -->
m

<!-- b003219 | prose | pages [10] -->
m

<!-- b003220 | prose | pages [10] -->
m

<!-- b003221 | prose | pages [10] -->
m

<!-- b003222 | prose | pages [10] -->
m

<!-- b003223 | prose | pages [10] -->
m

<!-- b003224 | prose | pages [10] -->
m

<!-- b003225 | prose | pages [10] -->
m

<!-- b003226 | prose | pages [10] -->
m

<!-- b003227 | prose | pages [10] -->
m

<!-- b003228 | prose | pages [10] -->
m

<!-- b003229 | prose | pages [10] -->
m

<!-- b003230 | prose | pages [10] -->
m

<!-- b003231 | prose | pages [10] -->
m

<!-- b003232 | prose | pages [10] -->
m

<!-- b003233 | prose | pages [10] -->
m

<!-- b003234 | prose | pages [10] -->
m

<!-- b003235 | prose | pages [10] -->
m

<!-- b003236 | prose | pages [10] -->
m

<!-- b003237 | prose | pages [10] -->
m

<!-- b003238 | prose | pages [10] -->
m

<!-- b003239 | prose | pages [10] -->
m

<!-- b003240 | prose | pages [10] -->
m

<!-- b003241 | prose | pages [10] -->
m

<!-- b003242 | prose | pages [10] -->
m

<!-- b003243 | prose | pages [10] -->
m

<!-- b003244 | prose | pages [10] -->
m

<!-- b003245 | prose | pages [10] -->
m

<!-- b003246 | prose | pages [10] -->
m

<!-- b003247 | prose | pages [10] -->
m

<!-- b003248 | prose | pages [10] -->
m

<!-- b003249 | prose | pages [10] -->
m

<!-- b003250 | prose | pages [10] -->
m

<!-- b003251 | prose | pages [10] -->
m

<!-- b003252 | prose | pages [10] -->
m

<!-- b003253 | prose | pages [10] -->
m

<!-- b003254 | prose | pages [10] -->
m

<!-- b003255 | prose | pages [10] -->
m

<!-- b003256 | prose | pages [10] -->
m

<!-- b003257 | prose | pages [10] -->
m

<!-- b003258 | prose | pages [10] -->
m

<!-- b003259 | prose | pages [10] -->
m

<!-- b003260 | prose | pages [10] -->
m

<!-- b003261 | prose | pages [10] -->
m

<!-- b003262 | prose | pages [10] -->
m

<!-- b003263 | prose | pages [10] -->
m

<!-- b003264 | prose | pages [10] -->
m

<!-- b003265 | prose | pages [10] -->
m

<!-- b003266 | prose | pages [10] -->
m

<!-- b003267 | prose | pages [10] -->
m

<!-- b003268 | prose | pages [10] -->
m

<!-- b003269 | prose | pages [10] -->
m

<!-- b003270 | prose | pages [10] -->
m

<!-- b003271 | prose | pages [10] -->
m

<!-- b003272 | prose | pages [10] -->
m

<!-- b003273 | prose | pages [10] -->
m

<!-- b003274 | prose | pages [10] -->
m

<!-- b003275 | prose | pages [10] -->
path connectivity:

<!-- b003276 | prose | pages [10] -->
m

<!-- b003277 | prose | pages [10] -->
m

<!-- b003278 | prose | pages [10] -->
m

<!-- b003279 | prose | pages [10] -->
m

<!-- b003280 | prose | pages [10] -->
m

<!-- b003281 | prose | pages [10] -->
m

<!-- b003282 | prose | pages [10] -->
m

<!-- b003283 | prose | pages [10] -->
m

<!-- b003284 | prose | pages [10] -->
m

<!-- b003285 | prose | pages [10] -->
m

<!-- b003286 | prose | pages [10] -->
m

<!-- b003287 | prose | pages [10] -->
m

<!-- b003288 | prose | pages [10] -->
m

<!-- b003289 | prose | pages [10] -->
m

<!-- b003290 | prose | pages [10] -->
m

<!-- b003291 | prose | pages [10] -->
m

<!-- b003292 | prose | pages [10] -->
m

<!-- b003293 | prose | pages [10] -->
m

<!-- b003294 | prose | pages [10] -->
m

<!-- b003295 | prose | pages [10] -->
m

<!-- b003296 | prose | pages [10] -->
m

<!-- b003297 | prose | pages [10] -->
m

<!-- b003298 | prose | pages [10] -->
m

<!-- b003299 | prose | pages [10] -->
m

<!-- b003300 | prose | pages [10] -->
m

<!-- b003301 | prose | pages [10] -->
m

<!-- b003302 | prose | pages [10] -->
m

<!-- b003303 | prose | pages [10] -->
m

<!-- b003304 | prose | pages [10] -->
m

<!-- b003305 | prose | pages [10] -->
m

<!-- b003306 | prose | pages [10] -->
m

<!-- b003307 | prose | pages [10] -->
m

<!-- b003308 | prose | pages [10] -->
m

<!-- b003309 | prose | pages [10] -->
m

<!-- b003310 | prose | pages [10] -->
m

<!-- b003311 | prose | pages [10] -->
m

<!-- b003312 | prose | pages [10] -->
m

<!-- b003313 | prose | pages [10] -->
m

<!-- b003314 | prose | pages [10] -->
m

<!-- b003315 | prose | pages [10] -->
m

<!-- b003316 | prose | pages [10] -->
m

<!-- b003317 | prose | pages [10] -->
m

<!-- b003318 | prose | pages [10] -->
m

<!-- b003319 | prose | pages [10] -->
m

<!-- b003320 | prose | pages [10] -->
m

<!-- b003321 | prose | pages [10] -->
m

<!-- b003322 | prose | pages [10] -->
m

<!-- b003323 | prose | pages [10] -->
m

<!-- b003324 | prose | pages [10] -->
m

<!-- b003325 | prose | pages [10] -->
m

<!-- b003326 | prose | pages [10] -->
m

<!-- b003327 | prose | pages [10] -->
m

<!-- b003328 | prose | pages [10] -->
m

<!-- b003329 | prose | pages [10] -->
m

<!-- b003330 | prose | pages [10] -->
m

<!-- b003331 | prose | pages [10] -->
m

<!-- b003332 | prose | pages [10] -->
m

<!-- b003333 | prose | pages [10] -->
m

<!-- b003334 | prose | pages [10] -->
m

<!-- b003335 | prose | pages [10] -->
m

<!-- b003336 | prose | pages [10] -->
m

<!-- b003337 | prose | pages [10] -->
m

<!-- b003338 | prose | pages [10] -->
m

<!-- b003339 | prose | pages [10] -->
m

<!-- b003340 | prose | pages [10] -->
m

<!-- b003341 | prose | pages [10] -->
m

<!-- b003342 | prose | pages [10] -->
m

<!-- b003343 | prose | pages [10] -->
m

<!-- b003344 | prose | pages [10] -->
m

<!-- b003345 | prose | pages [10] -->
m

<!-- b003346 | prose | pages [10] -->
m

<!-- b003347 | prose | pages [10] -->
m

<!-- b003348 | prose | pages [10] -->
m

<!-- b003349 | prose | pages [10] -->
m

<!-- b003350 | prose | pages [10] -->
m

<!-- b003351 | prose | pages [10] -->
m

<!-- b003352 | prose | pages [10] -->
m

<!-- b003353 | prose | pages [10] -->
m

<!-- b003354 | prose | pages [10] -->
m

<!-- b003355 | prose | pages [10] -->
m

<!-- b003356 | prose | pages [10] -->
m

<!-- b003357 | prose | pages [10] -->
m

<!-- b003358 | prose | pages [10] -->
m

<!-- b003359 | prose | pages [10] -->
m

<!-- b003360 | prose | pages [10] -->
m

<!-- b003361 | prose | pages [10] -->
m

<!-- b003362 | prose | pages [10] -->
m

<!-- b003363 | prose | pages [10] -->
m

<!-- b003364 | prose | pages [10] -->
m

<!-- b003365 | prose | pages [10] -->
m

<!-- b003366 | prose | pages [10] -->
m

<!-- b003367 | prose | pages [10] -->
m

<!-- b003368 | prose | pages [10] -->
m

<!-- b003369 | prose | pages [10] -->
m

<!-- b003370 | prose | pages [10] -->
m

<!-- b003371 | prose | pages [10] -->
m

<!-- b003372 | prose | pages [10] -->
m

<!-- b003373 | prose | pages [10] -->
m

<!-- b003374 | prose | pages [10] -->
m

<!-- b003375 | prose | pages [10] -->
m

<!-- b003376 | prose | pages [10] -->
m

<!-- b003377 | prose | pages [10] -->
m

<!-- b003378 | prose | pages [10] -->
m

<!-- b003379 | prose | pages [10] -->
m

<!-- b003380 | prose | pages [10] -->
m

<!-- b003381 | prose | pages [10] -->
m

<!-- b003382 | prose | pages [10] -->
m

<!-- b003383 | prose | pages [10] -->
m

<!-- b003384 | prose | pages [10] -->
m

<!-- b003385 | prose | pages [10] -->
m

<!-- b003386 | prose | pages [10] -->
m

<!-- b003387 | prose | pages [10] -->
m

<!-- b003388 | prose | pages [10] -->
m

<!-- b003389 | prose | pages [10] -->
m

<!-- b003390 | prose | pages [10] -->
m

<!-- b003391 | prose | pages [10] -->
m

<!-- b003392 | prose | pages [10] -->
m

<!-- b003393 | prose | pages [10] -->
m

<!-- b003394 | prose | pages [10] -->
m

<!-- b003395 | prose | pages [10] -->
m

<!-- b003396 | prose | pages [10] -->
m

<!-- b003397 | prose | pages [10] -->
m

<!-- b003398 | prose | pages [10] -->
m

<!-- b003399 | prose | pages [10] -->
m

<!-- b003400 | prose | pages [10] -->
m

<!-- b003401 | prose | pages [10] -->
m

<!-- b003402 | prose | pages [10] -->
m

<!-- b003403 | prose | pages [10] -->
m

<!-- b003404 | prose | pages [10] -->
m

<!-- b003405 | prose | pages [10] -->
m

<!-- b003406 | prose | pages [10] -->
m

<!-- b003407 | prose | pages [10] -->
m

<!-- b003408 | prose | pages [10] -->
m

<!-- b003409 | prose | pages [10] -->
m

<!-- b003410 | prose | pages [10] -->
m

<!-- b003411 | prose | pages [10] -->
m

<!-- b003412 | prose | pages [10] -->
m

<!-- b003413 | prose | pages [10] -->
m

<!-- b003414 | prose | pages [10] -->
m

<!-- b003415 | prose | pages [10] -->
m

<!-- b003416 | prose | pages [10] -->
m

<!-- b003417 | prose | pages [10] -->
m

<!-- b003418 | prose | pages [10] -->
m

<!-- b003419 | prose | pages [10] -->
m

<!-- b003420 | prose | pages [10] -->
m

<!-- b003421 | prose | pages [10] -->
m

<!-- b003422 | prose | pages [10] -->
m

<!-- b003423 | prose | pages [10] -->
m

<!-- b003424 | prose | pages [10] -->
m

<!-- b003425 | prose | pages [10] -->
m

<!-- b003426 | prose | pages [10] -->
m

<!-- b003427 | prose | pages [10] -->
m

<!-- b003428 | prose | pages [10] -->
m

<!-- b003429 | prose | pages [10] -->
m

<!-- b003430 | prose | pages [10] -->
m

<!-- b003431 | prose | pages [10] -->
m

<!-- b003432 | prose | pages [10] -->
m

<!-- b003433 | prose | pages [10] -->
m

<!-- b003434 | prose | pages [10] -->
m

<!-- b003435 | prose | pages [10] -->
m

<!-- b003436 | prose | pages [10] -->
m

<!-- b003437 | prose | pages [10] -->
m

<!-- b003438 | prose | pages [10] -->
m

<!-- b003439 | prose | pages [10] -->
m

<!-- b003440 | prose | pages [10] -->
m

<!-- b003441 | prose | pages [10] -->
m

<!-- b003442 | prose | pages [10] -->
m

<!-- b003443 | prose | pages [10] -->
m

<!-- b003444 | prose | pages [10] -->
m

<!-- b003445 | prose | pages [10] -->
m

<!-- b003446 | prose | pages [10] -->
m

<!-- b003447 | prose | pages [10] -->
m

<!-- b003448 | prose | pages [10] -->
m

<!-- b003449 | prose | pages [10] -->
m

<!-- b003450 | prose | pages [10] -->
m

<!-- b003451 | prose | pages [10] -->
m

<!-- b003452 | prose | pages [10] -->
m

<!-- b003453 | prose | pages [10] -->
m

<!-- b003454 | prose | pages [10] -->
m

<!-- b003455 | prose | pages [10] -->
m

<!-- b003456 | prose | pages [10] -->
m

<!-- b003457 | prose | pages [10] -->
m

<!-- b003458 | prose | pages [10] -->
m

<!-- b003459 | prose | pages [10] -->
m

<!-- b003460 | prose | pages [10] -->
m

<!-- b003461 | prose | pages [10] -->
m

<!-- b003462 | prose | pages [10] -->
m

<!-- b003463 | prose | pages [10] -->
m

<!-- b003464 | prose | pages [10] -->
m

<!-- b003465 | prose | pages [10] -->
m

<!-- b003466 | prose | pages [10] -->
m

<!-- b003467 | prose | pages [10] -->
m

<!-- b003468 | prose | pages [10] -->
m

<!-- b003469 | prose | pages [10] -->
m

<!-- b003470 | prose | pages [10] -->
m

<!-- b003471 | prose | pages [10] -->
m

<!-- b003472 | prose | pages [10] -->
m

<!-- b003473 | prose | pages [10] -->
m

<!-- b003474 | prose | pages [10] -->
m

<!-- b003475 | prose | pages [10] -->
m

<!-- b003476 | prose | pages [10] -->
m

<!-- b003477 | prose | pages [10] -->
m

<!-- b003478 | prose | pages [10] -->
m

<!-- b003479 | prose | pages [10] -->
m

<!-- b003480 | prose | pages [10] -->
m

<!-- b003481 | prose | pages [10] -->
m

<!-- b003482 | prose | pages [10] -->
B(eij) =

<!-- b003483 | prose | pages [10] -->
m

<!-- b003484 | prose | pages [10] -->
m

<!-- b003485 | prose | pages [10] -->
m

<!-- b003486 | prose | pages [10] -->
m

<!-- b003487 | prose | pages [10] -->
m

<!-- b003488 | prose | pages [10] -->
m

<!-- b003489 | prose | pages [10] -->
m

<!-- b003490 | prose | pages [10] -->
m

<!-- b003491 | prose | pages [10] -->
m

<!-- b003492 | prose | pages [10] -->
m

<!-- b003493 | prose | pages [10] -->
m

<!-- b003494 | prose | pages [10] -->
m

<!-- b003495 | prose | pages [10] -->
m

<!-- b003496 | prose | pages [10] -->
m

<!-- b003497 | prose | pages [10] -->
m

<!-- b003498 | prose | pages [10] -->
m

<!-- b003499 | prose | pages [10] -->
m

<!-- b003500 | prose | pages [10] -->
m

<!-- b003501 | prose | pages [10] -->
m

<!-- b003502 | prose | pages [10] -->
m

<!-- b003503 | prose | pages [10] -->
m

<!-- b003504 | prose | pages [10] -->
m

<!-- b003505 | prose | pages [10] -->
m

<!-- b003506 | prose | pages [10] -->
m

<!-- b003507 | prose | pages [10] -->
m

<!-- b003508 | prose | pages [10] -->
m

<!-- b003509 | prose | pages [10] -->
m

<!-- b003510 | prose | pages [10] -->
m

<!-- b003511 | prose | pages [10] -->
m

<!-- b003512 | prose | pages [10] -->
m

<!-- b003513 | prose | pages [10] -->
m

<!-- b003514 | prose | pages [10] -->
m

<!-- b003515 | prose | pages [10] -->
m

<!-- b003516 | prose | pages [10] -->
m

<!-- b003517 | prose | pages [10] -->
m

<!-- b003518 | prose | pages [10] -->
m

<!-- b003519 | prose | pages [10] -->
m

<!-- b003520 | prose | pages [10] -->
m

<!-- b003521 | prose | pages [10] -->
m

<!-- b003522 | prose | pages [10] -->
m

<!-- b003523 | prose | pages [10] -->
m

<!-- b003524 | prose | pages [10] -->
m

<!-- b003525 | prose | pages [10] -->
m

<!-- b003526 | prose | pages [10] -->
m

<!-- b003527 | prose | pages [10] -->
m

<!-- b003528 | prose | pages [10] -->
m

<!-- b003529 | prose | pages [10] -->
m

<!-- b003530 | prose | pages [10] -->
m

<!-- b003531 | prose | pages [10] -->
m

<!-- b003532 | prose | pages [10] -->
m

<!-- b003533 | prose | pages [10] -->
m

<!-- b003534 | prose | pages [10] -->
m

<!-- b003535 | prose | pages [10] -->
m

<!-- b003536 | prose | pages [10] -->
m

<!-- b003537 | prose | pages [10] -->
m

<!-- b003538 | prose | pages [10] -->
m

<!-- b003539 | prose | pages [10] -->
m

<!-- b003540 | prose | pages [10] -->
m

<!-- b003541 | prose | pages [10] -->
m

<!-- b003542 | prose | pages [10] -->
m

<!-- b003543 | prose | pages [10] -->
m

<!-- b003544 | prose | pages [10] -->
m

<!-- b003545 | prose | pages [10] -->
m

<!-- b003546 | prose | pages [10] -->
m

<!-- b003547 | prose | pages [10] -->
m

<!-- b003548 | prose | pages [10] -->
m

<!-- b003549 | prose | pages [10] -->
m

<!-- b003550 | prose | pages [10] -->
m

<!-- b003551 | prose | pages [10] -->
m

<!-- b003552 | prose | pages [10] -->
m

<!-- b003553 | prose | pages [10] -->
m

<!-- b003554 | prose | pages [10] -->
m

<!-- b003555 | prose | pages [10] -->
m

<!-- b003556 | prose | pages [10] -->
m

<!-- b003557 | prose | pages [10] -->
m

<!-- b003558 | prose | pages [10] -->
m

<!-- b003559 | prose | pages [10] -->
m

<!-- b003560 | prose | pages [10] -->
m

<!-- b003561 | prose | pages [10] -->
m

<!-- b003562 | prose | pages [10] -->
m

<!-- b003563 | prose | pages [10] -->
m

<!-- b003564 | prose | pages [10] -->
m

<!-- b003565 | prose | pages [10] -->
m

<!-- b003566 | prose | pages [10] -->
m

<!-- b003567 | prose | pages [10] -->
m

<!-- b003568 | prose | pages [10] -->
m

<!-- b003569 | prose | pages [10] -->
m

<!-- b003570 | prose | pages [10] -->
m

<!-- b003571 | prose | pages [10] -->
m

<!-- b003572 | prose | pages [10] -->
m

<!-- b003573 | prose | pages [10] -->
m

<!-- b003574 | prose | pages [10] -->
m

<!-- b003575 | prose | pages [10] -->
m

<!-- b003576 | prose | pages [10] -->
m

<!-- b003577 | prose | pages [10] -->
m

<!-- b003578 | prose | pages [10] -->
m

<!-- b003579 | prose | pages [10] -->
m

<!-- b003580 | prose | pages [10] -->
m

<!-- b003581 | prose | pages [10] -->
m

<!-- b003582 | prose | pages [10] -->
m

<!-- b003583 | prose | pages [10] -->
m

<!-- b003584 | prose | pages [10] -->
m

<!-- b003585 | prose | pages [10] -->
m

<!-- b003586 | prose | pages [10] -->
m

<!-- b003587 | prose | pages [10] -->
m

<!-- b003588 | prose | pages [10] -->
m

<!-- b003589 | prose | pages [10] -->
m

<!-- b003590 | prose | pages [10] -->
m

<!-- b003591 | prose | pages [10] -->
m

<!-- b003592 | prose | pages [10] -->
m

<!-- b003593 | prose | pages [10] -->
m

<!-- b003594 | prose | pages [10] -->
m

<!-- b003595 | prose | pages [10] -->
m

<!-- b003596 | prose | pages [10] -->
m

<!-- b003597 | prose | pages [10] -->
m

<!-- b003598 | prose | pages [10] -->
m

<!-- b003599 | prose | pages [10] -->
m

<!-- b003600 | prose | pages [10] -->
m

<!-- b003601 | prose | pages [10] -->
m

<!-- b003602 | prose | pages [10] -->
m

<!-- b003603 | prose | pages [10] -->
m

<!-- b003604 | prose | pages [10] -->
m

<!-- b003605 | prose | pages [10] -->
m

<!-- b003606 | prose | pages [10] -->
m

<!-- b003607 | prose | pages [10] -->
m

<!-- b003608 | prose | pages [10] -->
m

<!-- b003609 | prose | pages [10] -->
m

<!-- b003610 | prose | pages [10] -->
m

<!-- b003611 | prose | pages [10] -->
m

<!-- b003612 | prose | pages [10] -->
m

<!-- b003613 | prose | pages [10] -->
m

<!-- b003614 | prose | pages [10] -->
m

<!-- b003615 | prose | pages [10] -->
m

<!-- b003616 | prose | pages [10] -->
m

<!-- b003617 | prose | pages [10] -->
m

<!-- b003618 | prose | pages [10] -->
m

<!-- b003619 | prose | pages [10] -->
m

<!-- b003620 | prose | pages [10] -->
m

<!-- b003621 | prose | pages [10] -->
m

<!-- b003622 | prose | pages [10] -->
m

<!-- b003623 | prose | pages [10] -->
m

<!-- b003624 | prose | pages [10] -->
m

<!-- b003625 | prose | pages [10] -->
m

<!-- b003626 | prose | pages [10] -->
m

<!-- b003627 | prose | pages [10] -->
m

<!-- b003628 | prose | pages [10] -->
m

<!-- b003629 | prose | pages [10] -->
m

<!-- b003630 | prose | pages [10] -->
m

<!-- b003631 | prose | pages [10] -->
m

<!-- b003632 | prose | pages [10] -->
m

<!-- b003633 | prose | pages [10] -->
m

<!-- b003634 | prose | pages [10] -->
m

<!-- b003635 | prose | pages [10] -->
m

<!-- b003636 | prose | pages [10] -->
m

<!-- b003637 | prose | pages [10] -->
m

<!-- b003638 | prose | pages [10] -->
m

<!-- b003639 | prose | pages [10] -->
m

<!-- b003640 | prose | pages [10] -->
m

<!-- b003641 | prose | pages [10] -->
m

<!-- b003642 | prose | pages [10] -->
m

<!-- b003643 | prose | pages [10] -->
m

<!-- b003644 | prose | pages [10] -->
m

<!-- b003645 | prose | pages [10] -->
m

<!-- b003646 | prose | pages [10] -->
m

<!-- b003647 | prose | pages [10] -->
m

<!-- b003648 | prose | pages [10] -->
m

<!-- b003649 | prose | pages [10] -->
m

<!-- b003650 | prose | pages [10] -->
m

<!-- b003651 | prose | pages [10] -->
m

<!-- b003652 | prose | pages [10] -->
m

<!-- b003653 | prose | pages [10] -->
m

<!-- b003654 | prose | pages [10] -->
σst(eij)

<!-- b003655 | prose | pages [10] -->
X

<!-- b003656 | prose | pages [10] -->
, (8)

<!-- b003657 | prose | pages [10] -->
σst

<!-- b003658 | prose | pages [10] -->
vs̸=vt∈V

<!-- b003659 | prose | pages [10] -->
where σst enumerates all shortest paths between origin-destination pair (vs, vt), and σst(eij) counts those traversing edge eij. To integrate traffic dynamics with topologi- cal significance, the flow-criticality index combines centrality measures with capacity- sensitive traffic intensity:

<!-- b003660 | prose | pages [10] -->
AADTij γij = B(eij) · ∂uij maxe∈E AADT ·

<!-- b003661 | prose | pages [10] -->
.

<!-- b003662 | prose | pages [10] -->
(9)

<!-- b003663 | prose | pages [10] -->
∂AADTij

<!-- b003664 | prose | pages [10] -->
This dimensionless metric captures both the structural role of edges and their marginal contribution to capacity saturation, enabling identification of segments where high traffic volume coincides with critical topological positioning.

<!-- b003665 | prose | pages [10] -->
Network vulnerability is assessed through targeted disruption analysis, where the impact of edge removal is quantified via normalized efficiency loss:

<!-- b003666 | prose | pages [10] -->
∆G(eij) = I(G) −I(G \ eij)

<!-- b003667 | prose | pages [10] -->
.

<!-- b003668 | prose | pages [10] -->
(10) I(G)

<!-- b003669 | prose | pages [10] -->
The global efficiency metric I(G) evaluates network-wide connectivity as:

<!-- b003670 | prose | pages [10] -->
1 I(G) = n(n −1)

<!-- b003671 | prose | pages [10] -->
1

<!-- b003672 | prose | pages [10] -->
X

<!-- b003673 | prose | pages [10] -->
d(vi, vj), (11)

<!-- b003674 | prose | pages [10] -->
vi̸=vj

<!-- b003675 | prose | pages [10] -->
where d(vi, vj) represents shortest-path distance between nodes. This formulation penalizes both complete disconnections and increased travel distances, providing sen- sitivity to partial network degradation.

<!-- b003676 | prose | pages [10] -->
Spatiotemporal alignment of MDOT files records with network components em- ploys geometric and semantic mapping protocols. Spatial correspondence is estab- lished through Hausdorff distance minimization between road segment geometries geom(eij) and traffic data features geom(Dk):

<!-- b003677 | prose | pages [10] -->
eij ↔Dk ⇐⇒Hausdorff(geom(eij), geom(Dk)) < ϵ (ϵ = 10m).

<!-- b003678 | prose | pages [10] -->
(12)

<!-- b003679 | prose | pages [10] -->
This tolerance threshold accommodates positional discrepancies inherent in multi- source geospatial data while maintaining topological fidelity. Attribute transfer fol- lows a deterministic mapping scheme:

<!-- b003680 | prose | pages [10] -->
Φij ∋{AADT, AAWDT, V ehicleClass} ←Dk[FieldAADT, FieldAAWDT, FieldV ehClass],

<!-- b003681 | prose | pages [10] -->
(13)

<!-- b003682 | prose | pages [10] -->
where field correspondence is verified through metadata analysis and domain con- sistency checks. The integration framework ensures bijective relationships between traffic observations and network elements, crucial for maintaining data integrity in large-scale urban analyses.

<!-- b003683 | prose | pages [10] -->
关注数学模型

<!-- b003684 | furniture | pages [10] -->
2

<!-- b003685 | furniture | pages [10] -->
MATHmodels

<!-- b003686 | furniture | pages [10] -->
获取更多资讯

<!-- b003687 | furniture | pages [12] -->
Team # 2516219

<!-- b003688 | furniture | pages [12] -->
Page 12 of 24

<!-- b003689 | prose | pages [12] -->
(a) Average Daily traffic in 2014 (b) Average Daily traffic in 2022 (c) Current Average Daily traffic

<!-- b003690 | prose | pages [12] -->
(e) Average Weekday Daily Traf-

<!-- b003691 | prose | pages [12] -->
(d) Average Weekday Daily Traf- fic in 2014

<!-- b003692 | prose | pages [12] -->
fic in 2022

<!-- b003693 | prose | pages [12] -->
(f) Current Average Weekday Daily Traffic

<!-- b003694 | caption | pages [12] -->
Figure 5: Traffic Flow Diagram

<!-- b003695 | prose | pages [12] -->
At this time, the traffic is distributed based on the free flow time t0

<!-- b003696 | prose | pages [12] -->
e on the Francis Scott Key Bridge. After the collapse, the travel time te(ve) under the current traffic is calculated. The new traffic is distributed to the shortest path, and the updated traffic is as follows:

<!-- b003697 | prose | pages [12] -->
v(k+1)

<!-- b003698 | prose | pages [12] -->
= v(k) e

<!-- b003699 | prose | pages [12] -->
e + λ(˜ve −v(k)

<!-- b003700 | prose | pages [12] -->
e ) (16)

<!-- b003701 | prose | pages [12] -->
The step size λ is determined by line search.

<!-- b003702 | prose | pages [12] -->
Analysis of the impact of Francis Scott Key Bridge on stakehold- 6.3 ers

<!-- b003703 | prose | pages [12] -->
We presents a fuzzy comprehensive evaluation model to quantify the cascading effects of critical infrastructure failure on urban mobility systems. The framework in- tegrates multi-dimensional traffic metrics, environmental externalities, and network topology characteristics to assess the Francis Scott Key Bridge collapse consequences systematically.

<!-- b003704 | prose | pages [12] -->
关注数学模型

<!-- b003705 | furniture | pages [12] -->
2

<!-- b003706 | furniture | pages [12] -->
MATHmodels

<!-- b003707 | furniture | pages [12] -->
获取更多资讯

<!-- b003708 | furniture | pages [13] -->
Team # 2516219

<!-- b003709 | prose | pages [13] -->
6.3.1

<!-- b003710 | heading | pages [13] -->
Model Architecture

<!-- b003711 | furniture | pages [13] -->
Page 13 of 24

<!-- b003712 | prose | pages [13] -->
This study establishes a fuzzy comprehensive evaluation framework for assessing critical infrastructure failure impacts through multidimensional traffic network anal- ysis, integrating geometric, topological, and environmental dimensions. The model architecture operates within a four-dimensional factor space U = {Q, η, ∆I, Ce}, where Q quantifies flow redistribution intensity through normalized traffic volume ratios be- tween alternative and disrupted routes, η characterizes detour burden via temporal- spatial impedance metrics, ∆I measures network efficiency degradation via global connectivity indices, and Ce estimates environmental externalities through emission

<!-- b003713 | prose | pages [13] -->
微信公众号：数学模型

<!-- b003714 | prose | pages [13] -->
cost accumulation.

<!-- b003715 | prose | pages [13] -->
Linguistic evaluation terms V = {Negligible, Moderate, Severe, Catastrophic} are mapped through hybrid membership functions combining trapezoidal distributions for gradual traffic transitions, Gaussian kernels for probabilistic detour impacts, and sigmoidal activations for nonlinear efficiency degradation.

<!-- b003716 | prose | pages [13] -->
The flow redistribution intensity metric Q formalizes traffic reassignment dynamics as:

<!-- b003717 | prose | pages [13] -->
P

<!-- b003718 | prose | pages [13] -->
e∈Ealt AADTe

<!-- b003719 | prose | pages [13] -->
Q =

<!-- b003720 | prose | pages [13] -->
P

<!-- b003721 | prose | pages [13] -->
· lalt

<!-- b003722 | prose | pages [13] -->
, (17)

<!-- b003723 | prose | pages [13] -->
lorig

<!-- b003724 | prose | pages [13] -->
e∈Eclosed AADTe

<!-- b003725 | prose | pages [13] -->
微信号：MATHmodels

<!-- b003726 | prose | pages [13] -->
with trapezoidal membership parameters a = [0, 1, 3, 5], b = [1, 3, 5, 7], c = [3, 5, 7, 9], and d = [5, 7, 9, ∞) calibrated through historical congestion patterns. Detour burden coefficient η synthesizes temporal delays and density-criticality ratios:

<!-- b003727 | prose | pages [13] -->
P

<!-- b003728 | prose | pages [13] -->
p∈Pdetour tp

<!-- b003729 | prose | pages [13] -->
η =

<!-- b003730 | prose | pages [13] -->
P

<!-- b003731 | prose | pages [13] -->
· ρdetour

<!-- b003732 | prose | pages [13] -->
, (18)

<!-- b003733 | prose | pages [13] -->
p∈Porig tp

<!-- b003734 | prose | pages [13] -->
ρcrit

<!-- b003735 | prose | pages [13] -->
employing Gaussian distributions parameterized by m = [0.2, 0.5, 1.0, 1.5] and σ = [0.1, 0.2, 0.3, 0.4] derived from empirical routing data. Network efficiency degradation ∆I quantifies connectivity loss through normalized global efficiency differentials:

<!-- b003736 | prose | pages [13] -->
∆I = I(Gpre) −I(Gpost)

<!-- b003737 | prose | pages [13] -->
, (19) I(Gpre)

<!-- b003738 | prose | pages [13] -->
modulated by sigmoidal functions with tunable steepness α = [10, 8, 6, 4] and in- flection points β = [0.1, 0.3, 0.5, 0.7]. Environmental externalities Ce aggregate emission increases as:

<!-- b003739 | prose | pages [13] -->
X

<!-- b003740 | prose | pages [13] -->
(∆AADTe · le · 0.22)

<!-- b003741 | prose | pages [13] -->
Ce =

<!-- b003742 | prose | pages [13] -->
e∈E

<!-- b003743 | prose | pages [13] -->
[kg CO2/day], (20)

<!-- b003744 | prose | pages [13] -->
with piecewise linear thresholds [0, 50), [50, 200), [200, 500), [500, ∞) reflecting regu- latory air quality standards.

<!-- b003745 | prose | pages [13] -->
An adaptive entropy-weighting mechanism addresses parameter uncertainty through information-theoretic optimization, where weights wi are determined by historical ac- cident frequency distributions fik from MDOT SHA databases:

<!-- b003746 | prose | pages [13] -->
1 −Hi

<!-- b003747 | prose | pages [13] -->
,

<!-- b003748 | prose | pages [13] -->
wi = P4

<!-- b003749 | prose | pages [13] -->
j=1(1 −Hj)

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

<!-- b003787 | prose | pages [13] -->
m

<!-- b003788 | prose | pages [13] -->
m

<!-- b003789 | prose | pages [13] -->
m

<!-- b003790 | prose | pages [13] -->
m

<!-- b003791 | prose | pages [13] -->
m

<!-- b003792 | prose | pages [13] -->
m

<!-- b003793 | prose | pages [13] -->
m

<!-- b003794 | prose | pages [13] -->
m

<!-- b003795 | prose | pages [13] -->
m

<!-- b003796 | prose | pages [13] -->
m

<!-- b003797 | prose | pages [13] -->
m

<!-- b003798 | prose | pages [13] -->
m

<!-- b003799 | prose | pages [13] -->
m

<!-- b003800 | prose | pages [13] -->
m

<!-- b003801 | prose | pages [13] -->
m

<!-- b003802 | prose | pages [13] -->
m

<!-- b003803 | prose | pages [13] -->
m

<!-- b003804 | prose | pages [13] -->
m

<!-- b003805 | prose | pages [13] -->
m

<!-- b003806 | prose | pages [13] -->
m

<!-- b003807 | prose | pages [13] -->
m

<!-- b003808 | prose | pages [13] -->
m

<!-- b003809 | prose | pages [13] -->
m

<!-- b003810 | prose | pages [13] -->
m

<!-- b003811 | prose | pages [13] -->
m

<!-- b003812 | prose | pages [13] -->
m

<!-- b003813 | prose | pages [13] -->
m

<!-- b003814 | prose | pages [13] -->
m

<!-- b003815 | prose | pages [13] -->
m

<!-- b003816 | prose | pages [13] -->
m

<!-- b003817 | prose | pages [13] -->
m

<!-- b003818 | prose | pages [13] -->
m

<!-- b003819 | prose | pages [13] -->
m

<!-- b003820 | prose | pages [13] -->
m

<!-- b003821 | prose | pages [13] -->
m

<!-- b003822 | prose | pages [13] -->
m

<!-- b003823 | prose | pages [13] -->
m

<!-- b003824 | prose | pages [13] -->
m

<!-- b003825 | prose | pages [13] -->
m

<!-- b003826 | prose | pages [13] -->
m

<!-- b003827 | prose | pages [13] -->
m

<!-- b003828 | prose | pages [13] -->
m

<!-- b003829 | prose | pages [13] -->
m

<!-- b003830 | prose | pages [13] -->
m

<!-- b003831 | prose | pages [13] -->
m

<!-- b003832 | prose | pages [13] -->
m

<!-- b003833 | prose | pages [13] -->
m

<!-- b003834 | prose | pages [13] -->
m

<!-- b003835 | prose | pages [13] -->
m

<!-- b003836 | prose | pages [13] -->
m

<!-- b003837 | prose | pages [13] -->
m

<!-- b003838 | prose | pages [13] -->
m

<!-- b003839 | prose | pages [13] -->
m

<!-- b003840 | prose | pages [13] -->
m

<!-- b003841 | prose | pages [13] -->
m

<!-- b003842 | prose | pages [13] -->
m

<!-- b003843 | prose | pages [13] -->
m

<!-- b003844 | prose | pages [13] -->
m

<!-- b003845 | prose | pages [13] -->
m

<!-- b003846 | prose | pages [13] -->
m

<!-- b003847 | prose | pages [13] -->
m

<!-- b003848 | prose | pages [13] -->
m

<!-- b003849 | prose | pages [13] -->
m

<!-- b003850 | prose | pages [13] -->
m

<!-- b003851 | prose | pages [13] -->
m

<!-- b003852 | prose | pages [13] -->
m

<!-- b003853 | prose | pages [13] -->
m

<!-- b003854 | prose | pages [13] -->
m

<!-- b003855 | prose | pages [13] -->
m

<!-- b003856 | prose | pages [13] -->
m

<!-- b003857 | prose | pages [13] -->
m

<!-- b003858 | prose | pages [13] -->
m

<!-- b003859 | prose | pages [13] -->
m

<!-- b003860 | prose | pages [13] -->
m

<!-- b003861 | prose | pages [13] -->
m

<!-- b003862 | prose | pages [13] -->
m

<!-- b003863 | prose | pages [13] -->
m

<!-- b003864 | prose | pages [13] -->
m

<!-- b003865 | prose | pages [13] -->
m

<!-- b003866 | prose | pages [13] -->
m

<!-- b003867 | prose | pages [13] -->
m

<!-- b003868 | prose | pages [13] -->
m

<!-- b003869 | prose | pages [13] -->
m

<!-- b003870 | prose | pages [13] -->
m

<!-- b003871 | prose | pages [13] -->
m

<!-- b003872 | prose | pages [13] -->
m

<!-- b003873 | prose | pages [13] -->
m

<!-- b003874 | prose | pages [13] -->
m

<!-- b003875 | prose | pages [13] -->
m

<!-- b003876 | prose | pages [13] -->
m

<!-- b003877 | prose | pages [13] -->
m

<!-- b003878 | prose | pages [13] -->
m

<!-- b003879 | prose | pages [13] -->
m

<!-- b003880 | prose | pages [13] -->
4

<!-- b003881 | prose | pages [13] -->
Hi = −1

<!-- b003882 | prose | pages [13] -->
X

<!-- b003883 | prose | pages [13] -->
fik ln fik.

<!-- b003884 | prose | pages [13] -->
(21)

<!-- b003885 | prose | pages [13] -->
ln 4

<!-- b003886 | prose | pages [13] -->
k=1

<!-- b003887 | prose | pages [13] -->
This dynamically adjusts evaluation priorities based on regional incident patterns.

<!-- b003888 | prose | pages [13] -->
m

<!-- b003889 | prose | pages [13] -->
m

<!-- b003890 | prose | pages [13] -->
m

<!-- b003891 | prose | pages [13] -->
m

<!-- b003892 | prose | pages [13] -->
m

<!-- b003893 | prose | pages [13] -->
m

<!-- b003894 | prose | pages [13] -->
m

<!-- b003895 | prose | pages [13] -->
m

<!-- b003896 | prose | pages [13] -->
m

<!-- b003897 | prose | pages [13] -->
m

<!-- b003898 | prose | pages [13] -->
m

<!-- b003899 | prose | pages [13] -->
m

<!-- b003900 | prose | pages [13] -->
m

<!-- b003901 | prose | pages [13] -->
m

<!-- b003902 | prose | pages [13] -->
m

<!-- b003903 | prose | pages [13] -->
m

<!-- b003904 | prose | pages [13] -->
m

<!-- b003905 | prose | pages [13] -->
m

<!-- b003906 | prose | pages [13] -->
m

<!-- b003907 | prose | pages [13] -->
m

<!-- b003908 | prose | pages [13] -->
m

<!-- b003909 | prose | pages [13] -->
m

<!-- b003910 | prose | pages [13] -->
m

<!-- b003911 | prose | pages [13] -->
m

<!-- b003912 | prose | pages [13] -->
m

<!-- b003913 | prose | pages [13] -->
m

<!-- b003914 | prose | pages [13] -->
m

<!-- b003915 | prose | pages [13] -->
m

<!-- b003916 | prose | pages [13] -->
m

<!-- b003917 | prose | pages [13] -->
m

<!-- b003918 | prose | pages [13] -->
m

<!-- b003919 | prose | pages [13] -->
m

<!-- b003920 | prose | pages [13] -->
m

<!-- b003921 | prose | pages [13] -->
m

<!-- b003922 | prose | pages [13] -->
m

<!-- b003923 | prose | pages [13] -->
m

<!-- b003924 | prose | pages [13] -->
m

<!-- b003925 | prose | pages [13] -->
m

<!-- b003926 | prose | pages [13] -->
m

<!-- b003927 | prose | pages [13] -->
m

<!-- b003928 | prose | pages [13] -->
m

<!-- b003929 | prose | pages [13] -->
m

<!-- b003930 | prose | pages [13] -->
m

<!-- b003931 | prose | pages [13] -->
m

<!-- b003932 | prose | pages [13] -->
m

<!-- b003933 | prose | pages [13] -->
m

<!-- b003934 | prose | pages [13] -->
m

<!-- b003935 | prose | pages [13] -->
m

<!-- b003936 | prose | pages [13] -->
m

<!-- b003937 | prose | pages [13] -->
m

<!-- b003938 | prose | pages [13] -->
m

<!-- b003939 | prose | pages [13] -->
m

<!-- b003940 | prose | pages [13] -->
m

<!-- b003941 | prose | pages [13] -->
m

<!-- b003942 | prose | pages [13] -->
m

<!-- b003943 | prose | pages [13] -->
m

<!-- b003944 | prose | pages [13] -->
m

<!-- b003945 | prose | pages [13] -->
m

<!-- b003946 | prose | pages [13] -->
m

<!-- b003947 | prose | pages [13] -->
m

<!-- b003948 | prose | pages [13] -->
m

<!-- b003949 | prose | pages [13] -->
m

<!-- b003950 | prose | pages [13] -->
m

<!-- b003951 | prose | pages [13] -->
m

<!-- b003952 | prose | pages [13] -->
m

<!-- b003953 | prose | pages [13] -->
m

<!-- b003954 | prose | pages [13] -->
m

<!-- b003955 | prose | pages [13] -->
m

<!-- b003956 | prose | pages [13] -->
m

<!-- b003957 | prose | pages [13] -->
m

<!-- b003958 | prose | pages [13] -->
m

<!-- b003959 | prose | pages [13] -->
m

<!-- b003960 | prose | pages [13] -->
m

<!-- b003961 | prose | pages [13] -->
m

<!-- b003962 | prose | pages [13] -->
m

<!-- b003963 | prose | pages [13] -->
m

<!-- b003964 | prose | pages [13] -->
m

<!-- b003965 | prose | pages [13] -->
m

<!-- b003966 | prose | pages [13] -->
m

<!-- b003967 | prose | pages [13] -->
m

<!-- b003968 | prose | pages [13] -->
m

<!-- b003969 | prose | pages [13] -->
m

<!-- b003970 | prose | pages [13] -->
m

<!-- b003971 | prose | pages [13] -->
m

<!-- b003972 | prose | pages [13] -->
m

<!-- b003973 | prose | pages [13] -->
m

<!-- b003974 | prose | pages [13] -->
m

<!-- b003975 | prose | pages [13] -->
m

<!-- b003976 | prose | pages [13] -->
m

<!-- b003977 | prose | pages [13] -->
m

<!-- b003978 | prose | pages [13] -->
m

<!-- b003979 | prose | pages [13] -->
m

<!-- b003980 | prose | pages [13] -->
m

<!-- b003981 | prose | pages [13] -->
m

<!-- b003982 | prose | pages [13] -->
m

<!-- b003983 | prose | pages [13] -->
m

<!-- b003984 | prose | pages [13] -->
m

<!-- b003985 | prose | pages [13] -->
m

<!-- b003986 | prose | pages [13] -->
m

<!-- b003987 | prose | pages [13] -->
m

<!-- b003988 | prose | pages [13] -->
m

<!-- b003989 | prose | pages [13] -->
m

<!-- b003990 | prose | pages [13] -->
m

<!-- b003991 | prose | pages [13] -->
m

<!-- b003992 | prose | pages [13] -->
m

<!-- b003993 | prose | pages [13] -->
m

<!-- b003994 | prose | pages [13] -->
m

<!-- b003995 | prose | pages [13] -->
m

<!-- b003996 | prose | pages [13] -->
m

<!-- b003997 | prose | pages [13] -->
m

<!-- b003998 | prose | pages [13] -->
m

<!-- b003999 | prose | pages [13] -->
m

<!-- b004000 | prose | pages [13] -->
m

<!-- b004001 | prose | pages [13] -->
m

<!-- b004002 | prose | pages [13] -->
m

<!-- b004003 | prose | pages [13] -->
m

<!-- b004004 | prose | pages [13] -->
m

<!-- b004005 | prose | pages [13] -->
m

<!-- b004006 | prose | pages [13] -->
m

<!-- b004007 | prose | pages [13] -->
m

<!-- b004008 | prose | pages [13] -->
m

<!-- b004009 | prose | pages [13] -->
m

<!-- b004010 | prose | pages [13] -->
m

<!-- b004011 | prose | pages [13] -->
m

<!-- b004012 | prose | pages [13] -->
m

<!-- b004013 | prose | pages [13] -->
m

<!-- b004014 | prose | pages [13] -->
m

<!-- b004015 | prose | pages [13] -->
m

<!-- b004016 | prose | pages [13] -->
m

<!-- b004017 | prose | pages [13] -->
m

<!-- b004018 | prose | pages [13] -->
m

<!-- b004019 | prose | pages [13] -->
m

<!-- b004020 | prose | pages [13] -->
The fuzzy relation matrix R systematically organizes membership degrees across all

<!-- b004021 | prose | pages [13] -->
m

<!-- b004022 | prose | pages [13] -->
m

<!-- b004023 | prose | pages [13] -->
m

<!-- b004024 | prose | pages [13] -->
m

<!-- b004025 | prose | pages [13] -->
m

<!-- b004026 | prose | pages [13] -->
m

<!-- b004027 | prose | pages [13] -->
m

<!-- b004028 | prose | pages [13] -->
m

<!-- b004029 | prose | pages [13] -->
m

<!-- b004030 | prose | pages [13] -->
m

<!-- b004031 | prose | pages [13] -->
m

<!-- b004032 | prose | pages [13] -->
m

<!-- b004033 | prose | pages [13] -->
m

<!-- b004034 | prose | pages [13] -->
m

<!-- b004035 | prose | pages [13] -->
m

<!-- b004036 | prose | pages [13] -->
m

<!-- b004037 | prose | pages [13] -->
m

<!-- b004038 | prose | pages [13] -->
m

<!-- b004039 | prose | pages [13] -->
m

<!-- b004040 | prose | pages [13] -->
m

<!-- b004041 | prose | pages [13] -->
m

<!-- b004042 | prose | pages [13] -->
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

<!-- b004190 | furniture | pages [13] -->
m

<!-- b004191 | furniture | pages [13] -->
m

<!-- b004192 | furniture | pages [13] -->
m

<!-- b004193 | furniture | pages [13] -->
m

<!-- b004194 | furniture | pages [13] -->
m

<!-- b004195 | furniture | pages [13] -->
m

<!-- b004196 | furniture | pages [13] -->
m

<!-- b004197 | furniture | pages [13] -->
m

<!-- b004198 | furniture | pages [13] -->
m

<!-- b004199 | furniture | pages [13] -->
m

<!-- b004200 | furniture | pages [13] -->
m

<!-- b004201 | furniture | pages [13] -->
m

<!-- b004202 | furniture | pages [13] -->
m

<!-- b004203 | furniture | pages [13] -->
m

<!-- b004204 | furniture | pages [13] -->
m

<!-- b004205 | furniture | pages [13] -->
m

<!-- b004206 | furniture | pages [13] -->
m

<!-- b004207 | furniture | pages [13] -->
m

<!-- b004208 | furniture | pages [13] -->
m

<!-- b004209 | furniture | pages [13] -->
m

<!-- b004210 | furniture | pages [13] -->
m

<!-- b004211 | furniture | pages [13] -->
m

<!-- b004212 | furniture | pages [13] -->
m

<!-- b004213 | furniture | pages [13] -->
m

<!-- b004214 | furniture | pages [13] -->
m

<!-- b004215 | furniture | pages [13] -->
m

<!-- b004216 | furniture | pages [13] -->
m

<!-- b004217 | furniture | pages [13] -->
m

<!-- b004218 | furniture | pages [13] -->
m

<!-- b004219 | furniture | pages [13] -->
m

<!-- b004220 | furniture | pages [13] -->
m

<!-- b004221 | furniture | pages [13] -->
m

<!-- b004222 | furniture | pages [13] -->
m

<!-- b004223 | furniture | pages [13] -->
m

<!-- b004224 | furniture | pages [13] -->
m

<!-- b004225 | furniture | pages [13] -->
m

<!-- b004226 | furniture | pages [13] -->
m

<!-- b004227 | furniture | pages [13] -->
m

<!-- b004228 | furniture | pages [13] -->
m

<!-- b004229 | furniture | pages [13] -->
m

<!-- b004230 | furniture | pages [13] -->
m

<!-- b004231 | furniture | pages [13] -->
m

<!-- b004232 | furniture | pages [13] -->
m

<!-- b004233 | furniture | pages [13] -->
m

<!-- b004234 | furniture | pages [13] -->
m

<!-- b004235 | furniture | pages [13] -->
m

<!-- b004236 | furniture | pages [13] -->
m

<!-- b004237 | furniture | pages [13] -->
m

<!-- b004238 | furniture | pages [13] -->
m

<!-- b004239 | furniture | pages [13] -->
m

<!-- b004240 | furniture | pages [13] -->
m

<!-- b004241 | furniture | pages [13] -->
m

<!-- b004242 | furniture | pages [13] -->
m

<!-- b004243 | furniture | pages [13] -->
m

<!-- b004244 | furniture | pages [13] -->
m

<!-- b004245 | furniture | pages [13] -->
m

<!-- b004246 | furniture | pages [13] -->
m

<!-- b004247 | furniture | pages [13] -->
m

<!-- b004248 | furniture | pages [13] -->
m

<!-- b004249 | furniture | pages [13] -->
m

<!-- b004250 | furniture | pages [13] -->
m

<!-- b004251 | furniture | pages [13] -->
m

<!-- b004252 | furniture | pages [13] -->
m

<!-- b004253 | furniture | pages [13] -->
m

<!-- b004254 | furniture | pages [13] -->
m

<!-- b004255 | furniture | pages [13] -->
m

<!-- b004256 | furniture | pages [13] -->
m

<!-- b004257 | furniture | pages [13] -->
m

<!-- b004258 | furniture | pages [13] -->
m

<!-- b004259 | furniture | pages [13] -->
m

<!-- b004260 | furniture | pages [13] -->
m

<!-- b004261 | furniture | pages [13] -->
m

<!-- b004262 | furniture | pages [13] -->
m

<!-- b004263 | furniture | pages [13] -->
m

<!-- b004264 | furniture | pages [13] -->
m

<!-- b004265 | furniture | pages [13] -->
m

<!-- b004266 | furniture | pages [13] -->
m

<!-- b004267 | furniture | pages [13] -->
m

<!-- b004268 | furniture | pages [13] -->
m

<!-- b004269 | furniture | pages [13] -->
m

<!-- b004270 | furniture | pages [13] -->
m

<!-- b004271 | furniture | pages [13] -->
m

<!-- b004272 | furniture | pages [13] -->
m

<!-- b004273 | furniture | pages [13] -->
m

<!-- b004274 | furniture | pages [13] -->
m

<!-- b004275 | furniture | pages [13] -->
m

<!-- b004276 | furniture | pages [13] -->
m

<!-- b004277 | furniture | pages [13] -->
m

<!-- b004278 | furniture | pages [13] -->
m

<!-- b004279 | furniture | pages [13] -->
m

<!-- b004280 | furniture | pages [13] -->
m

<!-- b004281 | furniture | pages [13] -->
m

<!-- b004282 | furniture | pages [13] -->
m

<!-- b004283 | furniture | pages [13] -->
m

<!-- b004284 | furniture | pages [13] -->
m

<!-- b004285 | furniture | pages [13] -->
m

<!-- b004286 | furniture | pages [13] -->
m

<!-- b004287 | furniture | pages [13] -->
m

<!-- b004288 | furniture | pages [13] -->
m

<!-- b004289 | furniture | pages [13] -->
m

<!-- b004290 | furniture | pages [13] -->
m

<!-- b004291 | furniture | pages [13] -->
m

<!-- b004292 | furniture | pages [13] -->
m

<!-- b004293 | furniture | pages [13] -->
m

<!-- b004294 | furniture | pages [13] -->
m

<!-- b004295 | furniture | pages [13] -->
m

<!-- b004296 | furniture | pages [13] -->
m

<!-- b004297 | furniture | pages [13] -->
m

<!-- b004298 | furniture | pages [13] -->
m

<!-- b004299 | furniture | pages [13] -->
m

<!-- b004300 | furniture | pages [13] -->
m

<!-- b004301 | furniture | pages [13] -->
m

<!-- b004302 | furniture | pages [13] -->
m

<!-- b004303 | furniture | pages [13] -->
m

<!-- b004304 | furniture | pages [13] -->
m

<!-- b004305 | furniture | pages [13] -->
m

<!-- b004306 | furniture | pages [13] -->
m

<!-- b004307 | furniture | pages [13] -->
m

<!-- b004308 | furniture | pages [13] -->
m

<!-- b004309 | furniture | pages [13] -->
m

<!-- b004310 | furniture | pages [13] -->
m

<!-- b004311 | furniture | pages [13] -->
m

<!-- b004312 | furniture | pages [13] -->
m

<!-- b004313 | furniture | pages [13] -->
m

<!-- b004314 | furniture | pages [13] -->
m

<!-- b004315 | furniture | pages [13] -->
m

<!-- b004316 | furniture | pages [13] -->
m

<!-- b004317 | furniture | pages [13] -->
m

<!-- b004318 | furniture | pages [13] -->
m

<!-- b004319 | furniture | pages [13] -->
m

<!-- b004320 | furniture | pages [13] -->
m

<!-- b004321 | furniture | pages [13] -->
m

<!-- b004322 | furniture | pages [13] -->
m

<!-- b004323 | furniture | pages [13] -->
m

<!-- b004324 | furniture | pages [13] -->
m

<!-- b004325 | furniture | pages [13] -->
m

<!-- b004326 | furniture | pages [13] -->
m

<!-- b004327 | furniture | pages [13] -->
m

<!-- b004328 | furniture | pages [13] -->
m

<!-- b004329 | furniture | pages [13] -->
m

<!-- b004330 | furniture | pages [13] -->
m

<!-- b004331 | furniture | pages [13] -->
m

<!-- b004332 | furniture | pages [13] -->
m

<!-- b004333 | furniture | pages [13] -->
m

<!-- b004334 | furniture | pages [13] -->
m

<!-- b004335 | furniture | pages [13] -->
m

<!-- b004336 | furniture | pages [13] -->
m

<!-- b004337 | furniture | pages [13] -->
m

<!-- b004338 | furniture | pages [13] -->
m

<!-- b004339 | furniture | pages [13] -->
m

<!-- b004340 | furniture | pages [13] -->
m

<!-- b004341 | furniture | pages [13] -->
m

<!-- b004342 | furniture | pages [13] -->
m

<!-- b004343 | furniture | pages [13] -->
m

<!-- b004344 | furniture | pages [13] -->
m

<!-- b004345 | furniture | pages [13] -->
m

<!-- b004346 | furniture | pages [13] -->
m

<!-- b004347 | furniture | pages [13] -->
m

<!-- b004348 | furniture | pages [13] -->
m

<!-- b004349 | furniture | pages [13] -->
m

<!-- b004350 | furniture | pages [13] -->
m

<!-- b004351 | furniture | pages [13] -->
m

<!-- b004352 | furniture | pages [13] -->
m

<!-- b004353 | furniture | pages [13] -->
m

<!-- b004354 | furniture | pages [13] -->
m

<!-- b004355 | furniture | pages [13] -->
m

<!-- b004356 | furniture | pages [13] -->
m

<!-- b004357 | furniture | pages [13] -->
m

<!-- b004358 | furniture | pages [13] -->
m

<!-- b004359 | furniture | pages [13] -->
m

<!-- b004360 | furniture | pages [13] -->
m

<!-- b004361 | furniture | pages [13] -->
m

<!-- b004362 | furniture | pages [13] -->
m

<!-- b004363 | furniture | pages [13] -->
m

<!-- b004364 | furniture | pages [13] -->
m

<!-- b004365 | furniture | pages [13] -->
m

<!-- b004366 | furniture | pages [13] -->
m

<!-- b004367 | furniture | pages [13] -->
m

<!-- b004368 | furniture | pages [13] -->
m

<!-- b004369 | furniture | pages [13] -->
m

<!-- b004370 | furniture | pages [13] -->
m

<!-- b004371 | furniture | pages [13] -->
m

<!-- b004372 | furniture | pages [13] -->
m

<!-- b004373 | furniture | pages [13] -->
m

<!-- b004374 | furniture | pages [13] -->
m

<!-- b004375 | furniture | pages [13] -->
m

<!-- b004376 | furniture | pages [13] -->
m

<!-- b004377 | furniture | pages [13] -->
m

<!-- b004378 | furniture | pages [13] -->
m

<!-- b004379 | furniture | pages [13] -->
m

<!-- b004380 | furniture | pages [13] -->
m

<!-- b004381 | furniture | pages [13] -->
m

<!-- b004382 | furniture | pages [13] -->
m

<!-- b004383 | furniture | pages [13] -->
m

<!-- b004384 | furniture | pages [13] -->
m

<!-- b004385 | furniture | pages [13] -->
m

<!-- b004386 | furniture | pages [13] -->
m

<!-- b004387 | furniture | pages [13] -->
m

<!-- b004388 | furniture | pages [13] -->
m

<!-- b004389 | furniture | pages [13] -->
m

<!-- b004390 | furniture | pages [13] -->
m

<!-- b004391 | furniture | pages [13] -->
m

<!-- b004392 | furniture | pages [13] -->
m

<!-- b004393 | furniture | pages [13] -->
m

<!-- b004394 | furniture | pages [13] -->
m

<!-- b004395 | furniture | pages [13] -->
m

<!-- b004396 | furniture | pages [13] -->
m

<!-- b004397 | furniture | pages [13] -->
m

<!-- b004398 | furniture | pages [13] -->
m

<!-- b004399 | furniture | pages [13] -->
m

<!-- b004400 | furniture | pages [13] -->
m

<!-- b004401 | furniture | pages [13] -->
m

<!-- b004402 | furniture | pages [13] -->
m

<!-- b004403 | furniture | pages [13] -->
m

<!-- b004404 | furniture | pages [13] -->
m

<!-- b004405 | furniture | pages [13] -->
m

<!-- b004406 | furniture | pages [13] -->
m

<!-- b004407 | furniture | pages [13] -->
m

<!-- b004408 | furniture | pages [13] -->
m

<!-- b004409 | furniture | pages [13] -->
m

<!-- b004410 | furniture | pages [13] -->
m

<!-- b004411 | furniture | pages [13] -->
m

<!-- b004412 | furniture | pages [13] -->
m

<!-- b004413 | furniture | pages [13] -->
m

<!-- b004414 | furniture | pages [13] -->
m

<!-- b004415 | furniture | pages [13] -->
m

<!-- b004416 | furniture | pages [13] -->
m

<!-- b004417 | furniture | pages [13] -->
m

<!-- b004418 | furniture | pages [13] -->
m

<!-- b004419 | furniture | pages [13] -->
m

<!-- b004420 | furniture | pages [13] -->
m

<!-- b004421 | furniture | pages [13] -->
m

<!-- b004422 | furniture | pages [13] -->
m

<!-- b004423 | furniture | pages [13] -->
m

<!-- b004424 | furniture | pages [13] -->
m

<!-- b004425 | furniture | pages [13] -->
m

<!-- b004426 | furniture | pages [13] -->
m

<!-- b004427 | furniture | pages [13] -->
m

<!-- b004428 | furniture | pages [13] -->
m

<!-- b004429 | furniture | pages [13] -->
m

<!-- b004430 | furniture | pages [13] -->
m

<!-- b004431 | furniture | pages [13] -->
m

<!-- b004432 | furniture | pages [13] -->
m

<!-- b004433 | furniture | pages [13] -->
m

<!-- b004434 | furniture | pages [13] -->
m

<!-- b004435 | furniture | pages [13] -->
m

<!-- b004436 | furniture | pages [13] -->
m

<!-- b004437 | furniture | pages [13] -->
m

<!-- b004438 | furniture | pages [13] -->
m

<!-- b004439 | furniture | pages [13] -->
m

<!-- b004440 | furniture | pages [13] -->
m

<!-- b004441 | furniture | pages [13] -->
m

<!-- b004442 | furniture | pages [13] -->
m

<!-- b004443 | furniture | pages [13] -->
m

<!-- b004444 | furniture | pages [13] -->
m

<!-- b004445 | furniture | pages [13] -->
m

<!-- b004446 | furniture | pages [14] -->
Team # 2516219

<!-- b004447 | furniture | pages [14] -->
Page 14 of 24

<!-- b004448 | prose | pages [14] -->
factor-term pairs, enabling comprehensive impact synthesis through weighted aggre- gation:

<!-- b004449 | furniture | pages [14] -->


<!-- b004450 | prose | pages [14] -->
B = W ◦R =

<!-- b004451 | prose | pages [14] -->
!4

<!-- b004452 | prose | pages [14] -->
4 4 X

<!-- b004453 | prose | pages [14] -->
wiµui(vk)

<!-- b004454 | prose | pages [14] -->
, (22)

<!-- b004455 | prose | pages [14] -->
i=1

<!-- b004456 | prose | pages [14] -->
k=1

<!-- b004457 | prose | pages [14] -->
yielding probabilistic impact classification across predefined linguistic categories. Implementation demonstrates robust performance with 8.724% mean absolute per- centage error against discrete-time Markov chain simulations, establishing scientific validity for infrastructure resilience management applications.

<!-- b004458 | prose | pages [14] -->
Impact Analysis of Francis Scott Key Bridge Collapse 6.3.2

<!-- b004459 | prose | pages [14] -->
The catastrophic failure of the Francis Scott Key Bridge induced multidimensional disruptions across Baltimore’s transportation ecosystem, quantified through our net-

<!-- b004460 | prose | pages [14] -->
[4] [5]Post-collapse simulations

<!-- b004461 | prose | pages [14] -->
work model with rigorous spatial-temporal analytics.

<!-- b004462 | prose | pages [14] -->
reveal a 41.7% surge in daily traffic volume along I-695 and I-95 bypass routes, in- creasing average commute durations from 28 to 52 minutes during peak periods. The global network efficiency metric I(G) plummeted by 0.38, indicating severe connectiv- ity degradation between marine terminals and inland distribution centers.

<!-- b004463 | prose | pages [14] -->
Critical path analysis identifies six arterial corridors exceeding 85% capacity uti- lization (uij > 0.85), particularly impacting:

<!-- b004464 | prose | pages [14] -->
• Port operators: Truck transit times to Seagirt Marine Terminal increased by 73%, raising drayage costs by $18.7M annually; • Commuter populations: 23 neighborhoods experienced >50% rise in PM2.5 lev- els due to redirected traffic; • Emergency services: Response times escalated by 8-14 minutes for 37% of census tracts.

<!-- b004465 | prose | pages [14] -->
The environmental externality metric Ce quantified a daily emission surplus of 412 tons CO2-equivalent, translating to $2.1M in annualized health costs through EPA’s BenMAP-CE framework. Freight mobility degradation manifested as 19% increase in cargo dwell times at Canton Rail Terminal, jeopardizing Just-In-Time supply chains for automotive manufacturers.

<!-- b004466 | prose | pages [14] -->
Bridge reconstruction modeling predicts phased recovery:

<!-- b004467 | prose | pages [14] -->
∆Irecovery(t) = 0.38 · e−0.21t (t ∈[0, 24] months) (23)

<!-- b004468 | prose | pages [14] -->
indicating 90% network functionality restoration within 18 months. Temporary ferry services could reduce commuter delays by 32% during reconstruction, though increasing maritime collision risks by 17% according to marine traffic simulations.

<!-- b004469 | prose | pages [14] -->
Stakeholder-specific impacts emerge through our flow-criticality index γij:

<!-- b004470 | prose | pages [14] -->
• Local businesses: 68% of small enterprises within 2km radius face >15% cus- tomer accessibility loss (γij > 0.25);

<!-- b004471 | prose | pages [14] -->
m

<!-- b004472 | prose | pages [14] -->
m

<!-- b004473 | prose | pages [14] -->
m

<!-- b004474 | prose | pages [14] -->
m

<!-- b004475 | prose | pages [14] -->
m

<!-- b004476 | prose | pages [14] -->
m

<!-- b004477 | prose | pages [14] -->
m

<!-- b004478 | prose | pages [14] -->
m

<!-- b004479 | prose | pages [14] -->
m

<!-- b004480 | prose | pages [14] -->
m

<!-- b004481 | prose | pages [14] -->
m

<!-- b004482 | prose | pages [14] -->
m

<!-- b004483 | prose | pages [14] -->
m

<!-- b004484 | prose | pages [14] -->
m

<!-- b004485 | prose | pages [14] -->
m

<!-- b004486 | prose | pages [14] -->
m

<!-- b004487 | prose | pages [14] -->
m

<!-- b004488 | prose | pages [14] -->
m

<!-- b004489 | prose | pages [14] -->
m

<!-- b004490 | prose | pages [14] -->
m

<!-- b004491 | prose | pages [14] -->
m

<!-- b004492 | prose | pages [14] -->
m

<!-- b004493 | prose | pages [14] -->
m

<!-- b004494 | prose | pages [14] -->
m

<!-- b004495 | prose | pages [14] -->
m

<!-- b004496 | prose | pages [14] -->
m

<!-- b004497 | prose | pages [14] -->
m

<!-- b004498 | prose | pages [14] -->
m

<!-- b004499 | prose | pages [14] -->
m

<!-- b004500 | prose | pages [14] -->
m

<!-- b004501 | prose | pages [14] -->
m

<!-- b004502 | prose | pages [14] -->
m

<!-- b004503 | prose | pages [14] -->
m

<!-- b004504 | prose | pages [14] -->
m

<!-- b004505 | prose | pages [14] -->
m

<!-- b004506 | prose | pages [14] -->
m

<!-- b004507 | prose | pages [14] -->
m

<!-- b004508 | prose | pages [14] -->
m

<!-- b004509 | prose | pages [14] -->
m

<!-- b004510 | prose | pages [14] -->
m

<!-- b004511 | prose | pages [14] -->
m

<!-- b004512 | prose | pages [14] -->
m

<!-- b004513 | prose | pages [14] -->
m

<!-- b004514 | prose | pages [14] -->
m

<!-- b004515 | prose | pages [14] -->
m

<!-- b004516 | prose | pages [14] -->
m

<!-- b004517 | prose | pages [14] -->
m

<!-- b004518 | prose | pages [14] -->
m

<!-- b004519 | prose | pages [14] -->
m

<!-- b004520 | prose | pages [14] -->
m

<!-- b004521 | prose | pages [14] -->
m

<!-- b004522 | prose | pages [14] -->
m

<!-- b004523 | prose | pages [14] -->
m

<!-- b004524 | prose | pages [14] -->
• Transit agencies: Required 14 additional circulator buses to maintain headways

<!-- b004525 | prose | pages [14] -->
m

<!-- b004526 | prose | pages [14] -->
m

<!-- b004527 | prose | pages [14] -->
m

<!-- b004528 | prose | pages [14] -->
m

<!-- b004529 | prose | pages [14] -->
m

<!-- b004530 | prose | pages [14] -->
m

<!-- b004531 | prose | pages [14] -->
m

<!-- b004532 | prose | pages [14] -->
m

<!-- b004533 | prose | pages [14] -->
m

<!-- b004534 | prose | pages [14] -->
m

<!-- b004535 | prose | pages [14] -->
m

<!-- b004536 | prose | pages [14] -->
m

<!-- b004537 | prose | pages [14] -->
m

<!-- b004538 | prose | pages [14] -->
m

<!-- b004539 | prose | pages [14] -->
m

<!-- b004540 | prose | pages [14] -->
m

<!-- b004541 | prose | pages [14] -->
m

<!-- b004542 | prose | pages [14] -->
m

<!-- b004543 | prose | pages [14] -->
m

<!-- b004544 | prose | pages [14] -->
m

<!-- b004545 | prose | pages [14] -->
m

<!-- b004546 | prose | pages [14] -->
m

<!-- b004547 | prose | pages [14] -->
m

<!-- b004548 | prose | pages [14] -->
m

<!-- b004549 | prose | pages [14] -->
m

<!-- b004550 | prose | pages [14] -->
m

<!-- b004551 | prose | pages [14] -->
m

<!-- b004552 | prose | pages [14] -->
m

<!-- b004553 | prose | pages [14] -->
m

<!-- b004554 | prose | pages [14] -->
m

<!-- b004555 | prose | pages [14] -->
m

<!-- b004556 | prose | pages [14] -->
m

<!-- b004557 | prose | pages [14] -->
m

<!-- b004558 | prose | pages [14] -->
m

<!-- b004559 | prose | pages [14] -->
m

<!-- b004560 | prose | pages [14] -->
m

<!-- b004561 | prose | pages [14] -->
m

<!-- b004562 | prose | pages [14] -->
m

<!-- b004563 | prose | pages [14] -->
m

<!-- b004564 | prose | pages [14] -->
m

<!-- b004565 | prose | pages [14] -->
m

<!-- b004566 | prose | pages [14] -->
m

<!-- b004567 | prose | pages [14] -->
m

<!-- b004568 | prose | pages [14] -->
m

<!-- b004569 | prose | pages [14] -->
m

<!-- b004570 | prose | pages [14] -->
m

<!-- b004571 | prose | pages [14] -->
m

<!-- b004572 | prose | pages [14] -->
m

<!-- b004573 | prose | pages [14] -->
m

<!-- b004574 | prose | pages [14] -->
m

<!-- b004575 | prose | pages [14] -->
m

<!-- b004576 | prose | pages [14] -->
m

<!-- b004577 | prose | pages [14] -->
m

<!-- b004578 | prose | pages [14] -->
m

<!-- b004579 | prose | pages [14] -->
m

<!-- b004580 | prose | pages [14] -->
m

<!-- b004581 | prose | pages [14] -->
m

<!-- b004582 | prose | pages [14] -->
m

<!-- b004583 | prose | pages [14] -->
m

<!-- b004584 | prose | pages [14] -->
m

<!-- b004585 | prose | pages [14] -->
m

<!-- b004586 | prose | pages [14] -->
m

<!-- b004587 | prose | pages [14] -->
m

<!-- b004588 | prose | pages [14] -->
m

<!-- b004589 | prose | pages [14] -->
m

<!-- b004590 | prose | pages [14] -->
m

<!-- b004591 | prose | pages [14] -->
m

<!-- b004592 | prose | pages [14] -->
m

<!-- b004593 | prose | pages [14] -->
m

<!-- b004594 | prose | pages [14] -->
m

<!-- b004595 | prose | pages [14] -->
m

<!-- b004596 | prose | pages [14] -->
m

<!-- b004597 | prose | pages [14] -->
m

<!-- b004598 | prose | pages [14] -->
m

<!-- b004599 | prose | pages [14] -->
m

<!-- b004600 | prose | pages [14] -->
m

<!-- b004601 | prose | pages [14] -->
m

<!-- b004602 | prose | pages [14] -->
m

<!-- b004603 | prose | pages [14] -->
m

<!-- b004604 | prose | pages [14] -->
m

<!-- b004605 | prose | pages [14] -->
m

<!-- b004606 | prose | pages [14] -->
m

<!-- b004607 | prose | pages [14] -->
m

<!-- b004608 | prose | pages [14] -->
m

<!-- b004609 | prose | pages [14] -->
m

<!-- b004610 | prose | pages [14] -->
m

<!-- b004611 | prose | pages [14] -->
m

<!-- b004612 | prose | pages [14] -->
m

<!-- b004613 | prose | pages [14] -->
m

<!-- b004614 | prose | pages [14] -->
m

<!-- b004615 | prose | pages [14] -->
m

<!-- b004616 | prose | pages [14] -->
m

<!-- b004617 | prose | pages [14] -->
m

<!-- b004618 | prose | pages [14] -->
m

<!-- b004619 | prose | pages [14] -->
m

<!-- b004620 | prose | pages [14] -->
m

<!-- b004621 | prose | pages [14] -->
m

<!-- b004622 | prose | pages [14] -->
m

<!-- b004623 | prose | pages [14] -->
m

<!-- b004624 | prose | pages [14] -->
m

<!-- b004625 | prose | pages [14] -->
m

<!-- b004626 | prose | pages [14] -->
m

<!-- b004627 | prose | pages [14] -->
m

<!-- b004628 | prose | pages [14] -->
m

<!-- b004629 | prose | pages [14] -->
m

<!-- b004630 | prose | pages [14] -->
m

<!-- b004631 | prose | pages [14] -->
m

<!-- b004632 | prose | pages [14] -->
m

<!-- b004633 | prose | pages [14] -->
m

<!-- b004634 | prose | pages [14] -->
m

<!-- b004635 | prose | pages [14] -->
m

<!-- b004636 | prose | pages [14] -->
m

<!-- b004637 | prose | pages [14] -->
m

<!-- b004638 | prose | pages [14] -->
m

<!-- b004639 | prose | pages [14] -->
m

<!-- b004640 | prose | pages [14] -->
m

<!-- b004641 | prose | pages [14] -->
m

<!-- b004642 | prose | pages [14] -->
m

<!-- b004643 | prose | pages [14] -->
m

<!-- b004644 | prose | pages [14] -->
m

<!-- b004645 | prose | pages [14] -->
m

<!-- b004646 | prose | pages [14] -->
m

<!-- b004647 | prose | pages [14] -->
m

<!-- b004648 | prose | pages [14] -->
m

<!-- b004649 | prose | pages [14] -->
m

<!-- b004650 | prose | pages [14] -->
m

<!-- b004651 | prose | pages [14] -->
m

<!-- b004652 | prose | pages [14] -->
m

<!-- b004653 | prose | pages [14] -->
m

<!-- b004654 | prose | pages [14] -->
m

<!-- b004655 | prose | pages [14] -->
m

<!-- b004656 | prose | pages [14] -->
m

<!-- b004657 | prose | pages [14] -->
m

<!-- b004658 | prose | pages [14] -->
m

<!-- b004659 | prose | pages [14] -->
m

<!-- b004660 | prose | pages [14] -->
m

<!-- b004661 | prose | pages [14] -->
m

<!-- b004662 | prose | pages [14] -->
m

<!-- b004663 | prose | pages [14] -->
m

<!-- b004664 | prose | pages [14] -->
m

<!-- b004665 | prose | pages [14] -->
m

<!-- b004666 | prose | pages [14] -->
m

<!-- b004667 | prose | pages [14] -->
m

<!-- b004668 | prose | pages [14] -->
m

<!-- b004669 | prose | pages [14] -->
m

<!-- b004670 | prose | pages [14] -->
m

<!-- b004671 | prose | pages [14] -->
m

<!-- b004672 | prose | pages [14] -->
m

<!-- b004673 | prose | pages [14] -->
m

<!-- b004674 | prose | pages [14] -->
m

<!-- b004675 | prose | pages [14] -->
m

<!-- b004676 | prose | pages [14] -->
m

<!-- b004677 | prose | pages [14] -->
m

<!-- b004678 | prose | pages [14] -->
m

<!-- b004679 | prose | pages [14] -->
m

<!-- b004680 | prose | pages [14] -->
m

<!-- b004681 | prose | pages [14] -->
(γij-driven frequency adjustments);

<!-- b004682 | prose | pages [14] -->
m

<!-- b004683 | prose | pages [14] -->
m

<!-- b004684 | prose | pages [14] -->
m

<!-- b004685 | prose | pages [14] -->
m

<!-- b004686 | prose | pages [14] -->
m

<!-- b004687 | prose | pages [14] -->
m

<!-- b004688 | prose | pages [14] -->
m

<!-- b004689 | prose | pages [14] -->
m

<!-- b004690 | prose | pages [14] -->
m

<!-- b004691 | prose | pages [14] -->
m

<!-- b004692 | prose | pages [14] -->
m

<!-- b004693 | prose | pages [14] -->
m

<!-- b004694 | prose | pages [14] -->
m

<!-- b004695 | prose | pages [14] -->
m

<!-- b004696 | prose | pages [14] -->
m

<!-- b004697 | prose | pages [14] -->
m

<!-- b004698 | prose | pages [14] -->
m

<!-- b004699 | prose | pages [14] -->
m

<!-- b004700 | prose | pages [14] -->
m

<!-- b004701 | prose | pages [14] -->
m

<!-- b004702 | prose | pages [14] -->
m

<!-- b004703 | prose | pages [14] -->
m

<!-- b004704 | prose | pages [14] -->
m

<!-- b004705 | prose | pages [14] -->
m

<!-- b004706 | prose | pages [14] -->
m

<!-- b004707 | prose | pages [14] -->
m

<!-- b004708 | prose | pages [14] -->
m

<!-- b004709 | prose | pages [14] -->
m

<!-- b004710 | prose | pages [14] -->
m

<!-- b004711 | prose | pages [14] -->
m

<!-- b004712 | prose | pages [14] -->
m

<!-- b004713 | prose | pages [14] -->
m

<!-- b004714 | prose | pages [14] -->
m

<!-- b004715 | prose | pages [14] -->
m

<!-- b004716 | prose | pages [14] -->
m

<!-- b004717 | prose | pages [14] -->
m

<!-- b004718 | prose | pages [14] -->
m

<!-- b004719 | prose | pages [14] -->
m

<!-- b004720 | prose | pages [14] -->
m

<!-- b004721 | prose | pages [14] -->
m

<!-- b004722 | prose | pages [14] -->
m

<!-- b004723 | prose | pages [14] -->
m

<!-- b004724 | prose | pages [14] -->
m

<!-- b004725 | prose | pages [14] -->
m

<!-- b004726 | prose | pages [14] -->
m

<!-- b004727 | prose | pages [14] -->
m

<!-- b004728 | prose | pages [14] -->
m

<!-- b004729 | prose | pages [14] -->
m

<!-- b004730 | prose | pages [14] -->
m

<!-- b004731 | prose | pages [14] -->
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
• Urban planners: Identified 3.2km2 of gentrification-vulnerable areas from detour-

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

<!-- b004818 | prose | pages [14] -->
m

<!-- b004819 | prose | pages [14] -->
m

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
m

<!-- b004881 | prose | pages [14] -->
m

<!-- b004882 | prose | pages [14] -->
m

<!-- b004883 | prose | pages [14] -->
m

<!-- b004884 | prose | pages [14] -->
m

<!-- b004885 | prose | pages [14] -->
m

<!-- b004886 | prose | pages [14] -->
m

<!-- b004887 | prose | pages [14] -->
m

<!-- b004888 | prose | pages [14] -->
m

<!-- b004889 | prose | pages [14] -->
m

<!-- b004890 | prose | pages [14] -->
m

<!-- b004891 | prose | pages [14] -->
m

<!-- b004892 | prose | pages [14] -->
m

<!-- b004893 | prose | pages [14] -->
m

<!-- b004894 | prose | pages [14] -->
m

<!-- b004895 | prose | pages [14] -->
m

<!-- b004896 | prose | pages [14] -->
m

<!-- b004897 | prose | pages [14] -->
m

<!-- b004898 | prose | pages [14] -->
m

<!-- b004899 | prose | pages [14] -->
m

<!-- b004900 | prose | pages [14] -->
m

<!-- b004901 | prose | pages [14] -->
m

<!-- b004902 | prose | pages [14] -->
m

<!-- b004903 | prose | pages [14] -->
m

<!-- b004904 | prose | pages [14] -->
m

<!-- b004905 | prose | pages [14] -->
m

<!-- b004906 | prose | pages [14] -->
m

<!-- b004907 | prose | pages [14] -->
m

<!-- b004908 | prose | pages [14] -->
m

<!-- b004909 | prose | pages [14] -->
m

<!-- b004910 | prose | pages [14] -->
m

<!-- b004911 | prose | pages [14] -->
m

<!-- b004912 | prose | pages [14] -->
m

<!-- b004913 | prose | pages [14] -->
m

<!-- b004914 | prose | pages [14] -->
m

<!-- b004915 | prose | pages [14] -->
m

<!-- b004916 | prose | pages [14] -->
m

<!-- b004917 | prose | pages [14] -->
m

<!-- b004918 | prose | pages [14] -->
m

<!-- b004919 | prose | pages [14] -->
m

<!-- b004920 | prose | pages [14] -->
m

<!-- b004921 | prose | pages [14] -->
m

<!-- b004922 | prose | pages [14] -->
m

<!-- b004923 | prose | pages [14] -->
m

<!-- b004924 | prose | pages [14] -->
m

<!-- b004925 | prose | pages [14] -->
m

<!-- b004926 | prose | pages [14] -->
m

<!-- b004927 | prose | pages [14] -->
m

<!-- b004928 | prose | pages [14] -->
m

<!-- b004929 | prose | pages [14] -->
m

<!-- b004930 | prose | pages [14] -->
m

<!-- b004931 | prose | pages [14] -->
m

<!-- b004932 | prose | pages [14] -->
m

<!-- b004933 | prose | pages [14] -->
m

<!-- b004934 | prose | pages [14] -->
m

<!-- b004935 | prose | pages [14] -->
m

<!-- b004936 | prose | pages [14] -->
m

<!-- b004937 | prose | pages [14] -->
m

<!-- b004938 | prose | pages [14] -->
m

<!-- b004939 | prose | pages [14] -->
m

<!-- b004940 | prose | pages [14] -->
m

<!-- b004941 | prose | pages [14] -->
m

<!-- b004942 | prose | pages [14] -->
m

<!-- b004943 | prose | pages [14] -->
m

<!-- b004944 | prose | pages [14] -->
m

<!-- b004945 | prose | pages [14] -->
m

<!-- b004946 | prose | pages [14] -->
m

<!-- b004947 | prose | pages [14] -->
m

<!-- b004948 | prose | pages [14] -->
m

<!-- b004949 | prose | pages [14] -->
m

<!-- b004950 | prose | pages [14] -->
m

<!-- b004951 | prose | pages [14] -->
m

<!-- b004952 | prose | pages [14] -->
m

<!-- b004953 | prose | pages [14] -->
m

<!-- b004954 | prose | pages [14] -->
m

<!-- b004955 | prose | pages [14] -->
m

<!-- b004956 | prose | pages [14] -->
induced accessibility shifts.

<!-- b004957 | prose | pages [14] -->
m

<!-- b004958 | prose | pages [14] -->
m

<!-- b004959 | prose | pages [14] -->
m

<!-- b004960 | prose | pages [14] -->
m

<!-- b004961 | prose | pages [14] -->
m

<!-- b004962 | prose | pages [14] -->
m

<!-- b004963 | prose | pages [14] -->
m

<!-- b004964 | prose | pages [14] -->
m

<!-- b004965 | prose | pages [14] -->
m

<!-- b004966 | prose | pages [14] -->
m

<!-- b004967 | prose | pages [14] -->
m

<!-- b004968 | prose | pages [14] -->
m

<!-- b004969 | prose | pages [14] -->
m

<!-- b004970 | prose | pages [14] -->
m

<!-- b004971 | prose | pages [14] -->
m

<!-- b004972 | prose | pages [14] -->
m

<!-- b004973 | prose | pages [14] -->
m

<!-- b004974 | prose | pages [14] -->
m

<!-- b004975 | prose | pages [14] -->
m

<!-- b004976 | prose | pages [14] -->
m

<!-- b004977 | prose | pages [14] -->
m

<!-- b004978 | prose | pages [14] -->
m

<!-- b004979 | prose | pages [14] -->
m

<!-- b004980 | prose | pages [14] -->
m

<!-- b004981 | prose | pages [14] -->
m

<!-- b004982 | prose | pages [14] -->
m

<!-- b004983 | prose | pages [14] -->
m

<!-- b004984 | prose | pages [14] -->
m

<!-- b004985 | prose | pages [14] -->
m

<!-- b004986 | prose | pages [14] -->
m

<!-- b004987 | prose | pages [14] -->
m

<!-- b004988 | prose | pages [14] -->
m

<!-- b004989 | prose | pages [14] -->
m

<!-- b004990 | prose | pages [14] -->
m

<!-- b004991 | prose | pages [14] -->
m

<!-- b004992 | prose | pages [14] -->
m

<!-- b004993 | prose | pages [14] -->
m

<!-- b004994 | prose | pages [14] -->
m

<!-- b004995 | prose | pages [14] -->
m

<!-- b004996 | prose | pages [14] -->
m

<!-- b004997 | prose | pages [14] -->
m

<!-- b004998 | prose | pages [14] -->
m

<!-- b004999 | prose | pages [14] -->
m

<!-- b005000 | prose | pages [14] -->
m

<!-- b005001 | prose | pages [14] -->
m

<!-- b005002 | prose | pages [14] -->
m

<!-- b005003 | prose | pages [14] -->
m

<!-- b005004 | prose | pages [14] -->
m

<!-- b005005 | prose | pages [14] -->
m

<!-- b005006 | prose | pages [14] -->
m

<!-- b005007 | prose | pages [14] -->
m

<!-- b005008 | prose | pages [14] -->
m

<!-- b005009 | prose | pages [14] -->
m

<!-- b005010 | prose | pages [14] -->
m

<!-- b005011 | prose | pages [14] -->
m

<!-- b005012 | prose | pages [14] -->
m

<!-- b005013 | prose | pages [14] -->
m

<!-- b005014 | prose | pages [14] -->
m

<!-- b005015 | prose | pages [14] -->
m

<!-- b005016 | prose | pages [14] -->
m

<!-- b005017 | prose | pages [14] -->
m

<!-- b005018 | prose | pages [14] -->
m

<!-- b005019 | prose | pages [14] -->
m

<!-- b005020 | prose | pages [14] -->
m

<!-- b005021 | prose | pages [14] -->
m

<!-- b005022 | prose | pages [14] -->
m

<!-- b005023 | prose | pages [14] -->
m

<!-- b005024 | prose | pages [14] -->
m

<!-- b005025 | prose | pages [14] -->
m

<!-- b005026 | prose | pages [14] -->
m

<!-- b005027 | prose | pages [14] -->
m

<!-- b005028 | prose | pages [14] -->
m

<!-- b005029 | prose | pages [14] -->
m

<!-- b005030 | prose | pages [14] -->
m

<!-- b005031 | prose | pages [14] -->
m

<!-- b005032 | prose | pages [14] -->
m

<!-- b005033 | prose | pages [14] -->
m

<!-- b005034 | prose | pages [14] -->
m

<!-- b005035 | prose | pages [14] -->
m

<!-- b005036 | prose | pages [14] -->
m

<!-- b005037 | prose | pages [14] -->
m

<!-- b005038 | prose | pages [14] -->
m

<!-- b005039 | prose | pages [14] -->
m

<!-- b005040 | prose | pages [14] -->
m

<!-- b005041 | prose | pages [14] -->
m

<!-- b005042 | prose | pages [14] -->
m

<!-- b005043 | prose | pages [14] -->
m

<!-- b005044 | prose | pages [14] -->
m

<!-- b005045 | prose | pages [14] -->
m

<!-- b005046 | prose | pages [14] -->
m

<!-- b005047 | prose | pages [14] -->
m

<!-- b005048 | prose | pages [14] -->
m

<!-- b005049 | prose | pages [14] -->
m

<!-- b005050 | prose | pages [14] -->
m

<!-- b005051 | prose | pages [14] -->
m

<!-- b005052 | prose | pages [14] -->
m

<!-- b005053 | prose | pages [14] -->
m

<!-- b005054 | prose | pages [14] -->
m

<!-- b005055 | prose | pages [14] -->
m

<!-- b005056 | prose | pages [14] -->
m

<!-- b005057 | prose | pages [14] -->
m

<!-- b005058 | prose | pages [14] -->
m

<!-- b005059 | prose | pages [14] -->
m

<!-- b005060 | prose | pages [14] -->
m

<!-- b005061 | prose | pages [14] -->
m

<!-- b005062 | prose | pages [14] -->
m

<!-- b005063 | prose | pages [14] -->
m

<!-- b005064 | prose | pages [14] -->
m

<!-- b005065 | prose | pages [14] -->
m

<!-- b005066 | prose | pages [14] -->
m

<!-- b005067 | prose | pages [14] -->
m

<!-- b005068 | prose | pages [14] -->
m

<!-- b005069 | prose | pages [14] -->
m

<!-- b005070 | prose | pages [14] -->
m

<!-- b005071 | prose | pages [14] -->
m

<!-- b005072 | prose | pages [14] -->
m

<!-- b005073 | prose | pages [14] -->
m

<!-- b005074 | prose | pages [14] -->
m

<!-- b005075 | prose | pages [14] -->
m

<!-- b005076 | prose | pages [14] -->
m

<!-- b005077 | prose | pages [14] -->
m

<!-- b005078 | prose | pages [14] -->
m

<!-- b005079 | prose | pages [14] -->
m

<!-- b005080 | prose | pages [14] -->
m

<!-- b005081 | prose | pages [14] -->
m

<!-- b005082 | prose | pages [14] -->
m

<!-- b005083 | prose | pages [14] -->
m

<!-- b005084 | prose | pages [14] -->
m

<!-- b005085 | prose | pages [14] -->
m

<!-- b005086 | prose | pages [14] -->
m

<!-- b005087 | prose | pages [14] -->
m

<!-- b005088 | prose | pages [14] -->
m

<!-- b005089 | prose | pages [14] -->
m

<!-- b005090 | prose | pages [14] -->
m

<!-- b005091 | prose | pages [14] -->
m

<!-- b005092 | prose | pages [14] -->
m

<!-- b005093 | prose | pages [14] -->
m

<!-- b005094 | prose | pages [14] -->
m

<!-- b005095 | prose | pages [14] -->
m

<!-- b005096 | prose | pages [14] -->
m

<!-- b005097 | prose | pages [14] -->
m

<!-- b005098 | prose | pages [14] -->
m

<!-- b005099 | prose | pages [14] -->
m

<!-- b005100 | prose | pages [14] -->
m

<!-- b005101 | prose | pages [14] -->
m

<!-- b005102 | prose | pages [14] -->
m

<!-- b005103 | prose | pages [14] -->
m

<!-- b005104 | prose | pages [14] -->
m

<!-- b005105 | prose | pages [14] -->
m

<!-- b005106 | prose | pages [14] -->
m

<!-- b005107 | prose | pages [14] -->
m

<!-- b005108 | prose | pages [14] -->
m

<!-- b005109 | prose | pages [14] -->
m

<!-- b005110 | prose | pages [14] -->
m

<!-- b005111 | prose | pages [14] -->
m

<!-- b005112 | prose | pages [14] -->
m

<!-- b005113 | prose | pages [14] -->
m

<!-- b005114 | prose | pages [14] -->
m

<!-- b005115 | prose | pages [14] -->
m

<!-- b005116 | prose | pages [14] -->
m

<!-- b005117 | prose | pages [14] -->
m

<!-- b005118 | prose | pages [14] -->
m

<!-- b005119 | prose | pages [14] -->
m

<!-- b005120 | prose | pages [14] -->
m

<!-- b005121 | prose | pages [14] -->
m

<!-- b005122 | prose | pages [14] -->
m

<!-- b005123 | prose | pages [14] -->
m

<!-- b005124 | prose | pages [14] -->
m

<!-- b005125 | prose | pages [14] -->
m

<!-- b005126 | prose | pages [14] -->
m

<!-- b005127 | prose | pages [14] -->
m

<!-- b005128 | prose | pages [14] -->
m

<!-- b005129 | prose | pages [14] -->
m

<!-- b005130 | prose | pages [14] -->
m

<!-- b005131 | prose | pages [14] -->
m

<!-- b005132 | prose | pages [14] -->
m

<!-- b005133 | prose | pages [14] -->
m

<!-- b005134 | prose | pages [14] -->
m

<!-- b005135 | prose | pages [14] -->
m

<!-- b005136 | prose | pages [14] -->
m

<!-- b005137 | furniture | pages [14] -->
m

<!-- b005138 | furniture | pages [14] -->
m

<!-- b005139 | furniture | pages [14] -->
m

<!-- b005140 | furniture | pages [14] -->
m

<!-- b005141 | furniture | pages [14] -->
m

<!-- b005142 | furniture | pages [14] -->
m

<!-- b005143 | furniture | pages [14] -->
m

<!-- b005144 | furniture | pages [14] -->
m

<!-- b005145 | furniture | pages [14] -->
m

<!-- b005146 | furniture | pages [14] -->
m

<!-- b005147 | furniture | pages [14] -->
m

<!-- b005148 | furniture | pages [14] -->
m

<!-- b005149 | furniture | pages [14] -->
m

<!-- b005150 | furniture | pages [14] -->
m

<!-- b005151 | furniture | pages [14] -->
m

<!-- b005152 | furniture | pages [14] -->
m

<!-- b005153 | furniture | pages [14] -->
m

<!-- b005154 | furniture | pages [14] -->
m

<!-- b005155 | furniture | pages [14] -->
m

<!-- b005156 | furniture | pages [14] -->
m

<!-- b005157 | furniture | pages [14] -->
m

<!-- b005158 | furniture | pages [14] -->
m

<!-- b005159 | furniture | pages [14] -->
m

<!-- b005160 | furniture | pages [14] -->
m

<!-- b005161 | furniture | pages [14] -->
m

<!-- b005162 | prose | pages [14] -->
关注数学模型

<!-- b005163 | furniture | pages [14] -->
2

<!-- b005164 | furniture | pages [14] -->
MATHmodels

<!-- b005165 | furniture | pages [14] -->
获取更多资讯

<!-- b005166 | furniture | pages [15] -->
Team # 2516219

<!-- b005167 | furniture | pages [15] -->
Page 15 of 24

<!-- b005168 | caption | pages [15] -->
Figure 6: Impact of Francis Scott Key Bridge Collapse

<!-- b005169 | prose | pages [15] -->
微信公众号：数学模型

<!-- b005170 | prose | pages [15] -->
Therefore, the impact of the Francis Scott Key Bridge on stakeholders can be shown in the figure 6:

<!-- b005171 | prose | pages [15] -->
Our model validates through comparison with CMAP’s regional traffic counters (R2=0.894) and AIS ship tracking data, demonstrating robust predictive capability for infrastructure failure scenarios. The analysis provides actionable intelligence for prior- itizing emergency mitigation measures while optimizing reconstruction sequencing to minimize socioeconomic disparities.

<!-- b005172 | prose | pages [15] -->
微信号：MATHmodels

<!-- b005173 | prose | pages [15] -->
7

<!-- b005174 | heading | pages [15] -->
Multimodal Transportation Network Model for Bus-

<!-- b005175 | prose | pages [15] -->
Pedestrian System Analysis

<!-- b005176 | prose | pages [15] -->
In order to use the traffic flow network to create a transportation system model for projects that can affect bus or pedestrian systems, we extend the original traffic flow network into a multi-mode framework.

<!-- b005177 | prose | pages [15] -->
7.1 Multimodal Network Representation

<!-- b005178 | prose | pages [15] -->
[6] is mathematically formalized as a directed

<!-- b005179 | prose | pages [15] -->
The multimodal transportation system

<!-- b005180 | prose | pages [15] -->
graph GM = (N, E, M), where the node set N = Nb ∪Np ∪Nv integrates hetero- geneous infrastructure elements: bus stops Nb, pedestrian-accessible zones Np, and vehicle-specific nodes Nv. The edge set E = Eb ∪Ep ∪Etrans represents movement opportunities across three layers: bus route segments Eb, pedestrian pathways Ep, and intermodal transfer links Etrans. Transportation modes M = {bus, walk, auto} govern the operational constraints and mobility rules for traversing edges within each layer.

<!-- b005181 | prose | pages [15] -->
The bus network impedance tb(eb

<!-- b005182 | prose | pages [15] -->
ij) for travers-

<!-- b005183 | prose | pages [15] -->
Mode-Specific Travel Time Functions

<!-- b005184 | prose | pages [15] -->
ing edge eb

<!-- b005185 | prose | pages [15] -->
ij is defined as a composite function integrating stochastic waiting delays,

<!-- b005186 | furniture | pages [16] -->
Team # 2516219

<!-- b005187 | furniture | pages [16] -->
Page 16 of 24

<!-- b005188 | prose | pages [16] -->
speed-dependent motion time, and congestion penalties:

<!-- b005189 | prose | pages [16] -->
1 + σ2

<!-- b005190 | prose | pages [16] -->


<!-- b005191 | prose | pages [16] -->


<!-- b005192 | prose | pages [16] -->
1

<!-- b005193 | prose | pages [16] -->
j

<!-- b005194 | prose | pages [16] -->
tb(eb

<!-- b005195 | prose | pages [16] -->
+

<!-- b005196 | prose | pages [16] -->
ij) =

<!-- b005197 | prose | pages [16] -->
h2

<!-- b005198 | prose | pages [16] -->
2hj

<!-- b005199 | prose | pages [16] -->
v0

<!-- b005200 | prose | pages [16] -->
b exp

<!-- b005201 | prose | pages [16] -->
j

<!-- b005202 | prose | pages [16] -->
{z } | tw(fj)

<!-- b005203 | prose | pages [16] -->
|

<!-- b005204 | prose | pages [16] -->
!γb

<!-- b005205 | furniture | pages [16] -->


<!-- b005206 | prose | pages [16] -->
lb

<!-- b005207 | prose | pages [16] -->
f b

<!-- b005208 | prose | pages [16] -->
ij

<!-- b005209 | prose | pages [16] -->
ij

<!-- b005210 | prose | pages [16] -->
.

<!-- b005211 | prose | pages [16] -->
+ βb

<!-- b005212 | prose | pages [16] -->
(24)

<!-- b005213 | prose | pages [16] -->
fb

<!-- b005214 | prose | pages [16] -->
µbnbκb

<!-- b005215 | prose | pages [16] -->


<!-- b005216 | prose | pages [16] -->


<!-- b005217 | prose | pages [16] -->
ij

<!-- b005218 | prose | pages [16] -->
−αb

<!-- b005219 | prose | pages [16] -->
µbnbκb

<!-- b005220 | prose | pages [16] -->
{z } | congestion penalty

<!-- b005221 | prose | pages [16] -->
{z } motion time

<!-- b005222 | prose | pages [16] -->
Here, the Weibull-distributed waiting time tw(fj) captures headway variability through service frequency hj and schedule deviation σj. The effective bus speed ¯vb = v0

<!-- b005223 | prose | pages [16] -->
b exp(−αbf b

<!-- b005224 | prose | pages [16] -->
ij/Cb) decays exponentially with passenger load f b

<!-- b005225 | prose | pages [16] -->
ij relative to line capacity Cb = µb · nb · κb, which combines fleet dispatch rate µb, vehicle count nb, and permissible occupancy

<!-- b005226 | prose | pages [16] -->
ij/Cb)γb models passenger discomfort under

<!-- b005227 | prose | pages [16] -->
κb. The nonlinear congestion term βb(f b

<!-- b005228 | prose | pages [16] -->
crowded conditions.

<!-- b005229 | prose | pages [16] -->
Pedestrian pathway costs cp(ep

<!-- b005230 | prose | pages [16] -->
kl) synthesize physical traversal time, environmental impediments, and safety risks:

<!-- b005231 | prose | pages [16] -->
M

<!-- b005232 | prose | pages [16] -->
kl) = lp

<!-- b005233 | prose | pages [16] -->
X

<!-- b005234 | prose | pages [16] -->
cp(ep

<!-- b005235 | prose | pages [16] -->
kl

<!-- b005236 | prose | pages [16] -->
#−1

<!-- b005237 | prose | pages [16] -->
"

<!-- b005238 | prose | pages [16] -->


<!-- b005239 | prose | pages [16] -->
V

<!-- b005240 | prose | pages [16] -->
−

<!-- b005241 | prose | pages [16] -->
Cped −0.8

<!-- b005242 | prose | pages [16] -->
ωmdm(kl) + λ

<!-- b005243 | prose | pages [16] -->
1.34 +

<!-- b005244 | prose | pages [16] -->
m=1

<!-- b005245 | prose | pages [16] -->
The base traversal time lp

<!-- b005246 | prose | pages [16] -->
1 + e

<!-- b005247 | prose | pages [16] -->
.

<!-- b005248 | prose | pages [16] -->
(25)

<!-- b005249 | prose | pages [16] -->
p assumes a mean walking speed v0

<!-- b005250 | prose | pages [16] -->
kl/v0

<!-- b005251 | prose | pages [16] -->
p = 1.34 m/s, ad- justed by obstacle penalties P ωmdm(kl) weighted by pedestrian sensitivity coefficients ωm to impediments such as street furniture density d1(kl) or elevation changes d2(kl). The crossing danger index Icross(kl) employs a logistic function to quantify collision risk at intersections, where V/Cped represents the ratio of conflicting vehicle volume V to pedestrian capacity Cped, with parameter λ scaling the marginal disutility of per- ceived danger.

<!-- b005252 | prose | pages [16] -->
Multimodal Demand Allocation 7.2

<!-- b005253 | prose | pages [16] -->
The spatial distribution of travel demand across transportation modes is governed by a nested logit formulation that accounts for both systematic utility and stochastic preference heterogeneity. The conditional probability Pm|od of selecting mode m for an origin-destination pair (o, d) follows:

<!-- b005254 | prose | pages [16] -->
exp (V m Pm|od =

<!-- b005255 | prose | pages [16] -->
P

<!-- b005256 | prose | pages [16] -->
m′ exp

<!-- b005257 | prose | pages [16] -->
od + ln Sm)

<!-- b005258 | prose | pages [16] -->
od + ln Sm′, (26)

<!-- b005259 | prose | pages [16] -->
V m′

<!-- b005260 | prose | pages [16] -->
 

<!-- b005261 | prose | pages [16] -->
od +βrel ·σm

<!-- b005262 | prose | pages [16] -->
where V m

<!-- b005263 | prose | pages [16] -->
od = βcost ·cm

<!-- b005264 | prose | pages [16] -->
od +βtime ·tm

<!-- b005265 | prose | pages [16] -->
porating generalized cost cm

<!-- b005266 | prose | pages [16] -->
od, travel time tm

<!-- b005267 | prose | pages [16] -->
od exp (µm(V r

<!-- b005268 | prose | pages [16] -->
od −V m

<!-- b005269 | prose | pages [16] -->
value Sm = P

<!-- b005270 | prose | pages [16] -->
od represents the deterministic utility incor-

<!-- b005271 | prose | pages [16] -->
od, and reliability measure σm

<!-- b005272 | prose | pages [16] -->
od. The inclusive

<!-- b005273 | prose | pages [16] -->
od )) captures the composite utility of all sub-routes

<!-- b005274 | prose | pages [16] -->
r∈Rm

<!-- b005275 | prose | pages [16] -->
r within mode m, scaled by the nesting parameter µm that governs correlation among similar alternatives.

<!-- b005276 | prose | pages [16] -->
7.3 Accessibility Impact Metric

<!-- b005277 | prose | pages [16] -->
The multimodal accessibility potential Aτ

<!-- b005278 | prose | pages [16] -->
mulated as:

<!-- b005279 | prose | pages [16] -->
X

<!-- b005280 | prose | pages [16] -->
Aτ

<!-- b005281 | prose | pages [16] -->
Wj · exp

<!-- b005282 | prose | pages [16] -->
i =

<!-- b005283 | prose | pages [16] -->
j

<!-- b005284 | prose | pages [16] -->
i for location i at departure time τ is for-

<!-- b005285 | prose | pages [16] -->
 

<!-- b005286 | prose | pages [16] -->


<!-- b005287 | prose | pages [16] -->
m∈M cm

<!-- b005288 | prose | pages [16] -->
−λ · min

<!-- b005289 | prose | pages [16] -->
ij(τ)

<!-- b005290 | prose | pages [16] -->
, (27)

<!-- b005291 | prose | pages [16] -->
关注数学模型

<!-- b005292 | furniture | pages [16] -->
2

<!-- b005293 | furniture | pages [16] -->
MATHmodels

<!-- b005294 | furniture | pages [16] -->
获取更多资讯

<!-- b005295 | furniture | pages [17] -->
Team # 2516219

<!-- b005296 | furniture | pages [17] -->
Page 17 of 24

<!-- b005297 | prose | pages [17] -->
where Wj denotes the opportunity density at destination zone j, and cm

<!-- b005298 | prose | pages [17] -->
ij(τ) rep- resents the time-dependent generalized travel cost incorporating monetary, temporal, and discomfort components. The exponential decay factor λ modulates the spatial friction effect.

<!-- b005299 | prose | pages [17] -->
Equity Evaluation Spatial justice implications are quantified through the Gini coeffi- cient G, computed over the accessibility distribution {Ai}:

<!-- b005300 | prose | pages [17] -->
n

<!-- b005301 | prose | pages [17] -->
1

<!-- b005302 | prose | pages [17] -->
X

<!-- b005303 | prose | pages [17] -->
G =

<!-- b005304 | prose | pages [17] -->
n X

<!-- b005305 | prose | pages [17] -->
|Ai −Aj|,

<!-- b005306 | prose | pages [17] -->
微信公众号：数学模型

<!-- b005307 | prose | pages [17] -->
2n2 ¯A

<!-- b005308 | prose | pages [17] -->
i=1

<!-- b005309 | prose | pages [17] -->
j=1

<!-- b005310 | prose | pages [17] -->
where ¯A denotes the mean accessibility level across n spatial units. Lower G values indicate reduced inequality in opportunity distribution.

<!-- b005311 | prose | pages [17] -->
Implementation Scenario: Bus Rapid Transit (BRT) Project 7.4

<!-- b005312 | prose | pages [17] -->
A 28-km BRT corridor with 23 stations is simulated in (39.265622, -76.667171) to (39.249151, -76.639981), as shown in Figure 7, featuring operational enhancements in-

<!-- b005313 | prose | pages [17] -->
微信号：MATHmodels

<!-- b005314 | prose | pages [17] -->
cluding headway reduction hj →max(3 min, 0.7hcurrent

<!-- b005315 | prose | pages [17] -->
) and pedestrian access opti- j mization through tightened catchment radius Racc = 800 m →500 m. These interven- tions aim to improve service efficiency while promoting walk-and-ride integration. The experimental results is shown in Table 4 and Figure 8.

<!-- b005316 | caption | pages [17] -->
Figure 7: Simulated bus routes, city areas and bus route maps

<!-- b005317 | prose | pages [17] -->
The simulation outcomes demonstrate significant multimodal system improvements, with a 44.1% relative increase in bus mode share attributable to enhanced service fre- quency and reliability. The accessibility Gini coefficient reduction from 0.41 to 0.35 re- veals substantial equity gains, particularly benefiting previously underserved periph-

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

<!-- b005404 | prose | pages [17] -->
m

<!-- b005405 | prose | pages [17] -->
m

<!-- b005406 | prose | pages [17] -->
m

<!-- b005407 | prose | pages [17] -->
m

<!-- b005408 | prose | pages [17] -->
m

<!-- b005409 | prose | pages [17] -->
m

<!-- b005410 | prose | pages [17] -->
m

<!-- b005411 | prose | pages [17] -->
m

<!-- b005412 | prose | pages [17] -->
m

<!-- b005413 | prose | pages [17] -->
m

<!-- b005414 | prose | pages [17] -->
m

<!-- b005415 | prose | pages [17] -->
m

<!-- b005416 | prose | pages [17] -->
m

<!-- b005417 | prose | pages [17] -->
m

<!-- b005418 | prose | pages [17] -->
m

<!-- b005419 | prose | pages [17] -->
m

<!-- b005420 | prose | pages [17] -->
m

<!-- b005421 | prose | pages [17] -->
m

<!-- b005422 | prose | pages [17] -->
m

<!-- b005423 | prose | pages [17] -->
m

<!-- b005424 | prose | pages [17] -->
m

<!-- b005425 | prose | pages [17] -->
m

<!-- b005426 | prose | pages [17] -->
eral neighborhoods. Environmental co-benefits emerge through 10.6% lower PM2.5

<!-- b005427 | prose | pages [17] -->
m

<!-- b005428 | prose | pages [17] -->
m

<!-- b005429 | prose | pages [17] -->
m

<!-- b005430 | prose | pages [17] -->
m

<!-- b005431 | prose | pages [17] -->
m

<!-- b005432 | prose | pages [17] -->
m

<!-- b005433 | prose | pages [17] -->
m

<!-- b005434 | prose | pages [17] -->
m

<!-- b005435 | prose | pages [17] -->
m

<!-- b005436 | prose | pages [17] -->
m

<!-- b005437 | prose | pages [17] -->
m

<!-- b005438 | prose | pages [17] -->
m

<!-- b005439 | prose | pages [17] -->
m

<!-- b005440 | prose | pages [17] -->
m

<!-- b005441 | prose | pages [17] -->
m

<!-- b005442 | prose | pages [17] -->
m

<!-- b005443 | prose | pages [17] -->
m

<!-- b005444 | prose | pages [17] -->
m

<!-- b005445 | prose | pages [17] -->
m

<!-- b005446 | prose | pages [17] -->
m

<!-- b005447 | prose | pages [17] -->
m

<!-- b005448 | prose | pages [17] -->
m

<!-- b005449 | prose | pages [17] -->
m

<!-- b005450 | prose | pages [17] -->
m

<!-- b005451 | prose | pages [17] -->
m

<!-- b005452 | prose | pages [17] -->
m

<!-- b005453 | prose | pages [17] -->
m

<!-- b005454 | prose | pages [17] -->
m

<!-- b005455 | prose | pages [17] -->
m

<!-- b005456 | prose | pages [17] -->
m

<!-- b005457 | prose | pages [17] -->
m

<!-- b005458 | prose | pages [17] -->
m

<!-- b005459 | prose | pages [17] -->
m

<!-- b005460 | prose | pages [17] -->
m

<!-- b005461 | prose | pages [17] -->
m

<!-- b005462 | prose | pages [17] -->
m

<!-- b005463 | prose | pages [17] -->
m

<!-- b005464 | prose | pages [17] -->
m

<!-- b005465 | prose | pages [17] -->
m

<!-- b005466 | prose | pages [17] -->
m

<!-- b005467 | prose | pages [17] -->
m

<!-- b005468 | prose | pages [17] -->
m

<!-- b005469 | prose | pages [17] -->
m

<!-- b005470 | prose | pages [17] -->
m

<!-- b005471 | prose | pages [17] -->
m

<!-- b005472 | prose | pages [17] -->
m

<!-- b005473 | prose | pages [17] -->
m

<!-- b005474 | prose | pages [17] -->
m

<!-- b005475 | prose | pages [17] -->
m

<!-- b005476 | prose | pages [17] -->
m

<!-- b005477 | prose | pages [17] -->
m

<!-- b005478 | prose | pages [17] -->
m

<!-- b005479 | prose | pages [17] -->
m

<!-- b005480 | prose | pages [17] -->
m

<!-- b005481 | prose | pages [17] -->
m

<!-- b005482 | prose | pages [17] -->
m

<!-- b005483 | prose | pages [17] -->
m

<!-- b005484 | prose | pages [17] -->
m

<!-- b005485 | prose | pages [17] -->
m

<!-- b005486 | prose | pages [17] -->
m

<!-- b005487 | prose | pages [17] -->
m

<!-- b005488 | prose | pages [17] -->
m

<!-- b005489 | prose | pages [17] -->
m

<!-- b005490 | prose | pages [17] -->
m

<!-- b005491 | prose | pages [17] -->
m

<!-- b005492 | prose | pages [17] -->
m

<!-- b005493 | prose | pages [17] -->
m

<!-- b005494 | prose | pages [17] -->
m

<!-- b005495 | prose | pages [17] -->
m

<!-- b005496 | prose | pages [17] -->
m

<!-- b005497 | prose | pages [17] -->
m

<!-- b005498 | prose | pages [17] -->
m

<!-- b005499 | prose | pages [17] -->
m

<!-- b005500 | prose | pages [17] -->
m

<!-- b005501 | prose | pages [17] -->
m

<!-- b005502 | prose | pages [17] -->
m

<!-- b005503 | prose | pages [17] -->
m

<!-- b005504 | prose | pages [17] -->
m

<!-- b005505 | prose | pages [17] -->
m

<!-- b005506 | prose | pages [17] -->
m

<!-- b005507 | prose | pages [17] -->
m

<!-- b005508 | prose | pages [17] -->
m

<!-- b005509 | prose | pages [17] -->
m

<!-- b005510 | prose | pages [17] -->
m

<!-- b005511 | prose | pages [17] -->
m

<!-- b005512 | prose | pages [17] -->
m

<!-- b005513 | prose | pages [17] -->
m

<!-- b005514 | prose | pages [17] -->
m

<!-- b005515 | prose | pages [17] -->
m

<!-- b005516 | prose | pages [17] -->
m

<!-- b005517 | prose | pages [17] -->
m

<!-- b005518 | prose | pages [17] -->
m

<!-- b005519 | prose | pages [17] -->
m

<!-- b005520 | prose | pages [17] -->
m

<!-- b005521 | prose | pages [17] -->
m

<!-- b005522 | prose | pages [17] -->
m

<!-- b005523 | prose | pages [17] -->
m

<!-- b005524 | prose | pages [17] -->
m

<!-- b005525 | prose | pages [17] -->
m

<!-- b005526 | prose | pages [17] -->
m

<!-- b005527 | prose | pages [17] -->
m

<!-- b005528 | prose | pages [17] -->
m

<!-- b005529 | prose | pages [17] -->
m

<!-- b005530 | prose | pages [17] -->
m

<!-- b005531 | prose | pages [17] -->
m

<!-- b005532 | prose | pages [17] -->
m

<!-- b005533 | prose | pages [17] -->
m

<!-- b005534 | prose | pages [17] -->
m

<!-- b005535 | prose | pages [17] -->
m

<!-- b005536 | prose | pages [17] -->
m

<!-- b005537 | prose | pages [17] -->
m

<!-- b005538 | prose | pages [17] -->
m

<!-- b005539 | prose | pages [17] -->
m

<!-- b005540 | prose | pages [17] -->
m

<!-- b005541 | prose | pages [17] -->
m

<!-- b005542 | prose | pages [17] -->
m

<!-- b005543 | prose | pages [17] -->
m

<!-- b005544 | prose | pages [17] -->
m

<!-- b005545 | prose | pages [17] -->
m

<!-- b005546 | prose | pages [17] -->
m

<!-- b005547 | prose | pages [17] -->
m

<!-- b005548 | prose | pages [17] -->
m

<!-- b005549 | prose | pages [17] -->
m

<!-- b005550 | prose | pages [17] -->
m

<!-- b005551 | prose | pages [17] -->
m

<!-- b005552 | prose | pages [17] -->
m

<!-- b005553 | prose | pages [17] -->
m

<!-- b005554 | prose | pages [17] -->
m

<!-- b005555 | prose | pages [17] -->
m

<!-- b005556 | prose | pages [17] -->
m

<!-- b005557 | prose | pages [17] -->
m

<!-- b005558 | prose | pages [17] -->
m

<!-- b005559 | prose | pages [17] -->
m

<!-- b005560 | prose | pages [17] -->
m

<!-- b005561 | prose | pages [17] -->
m

<!-- b005562 | prose | pages [17] -->
m

<!-- b005563 | prose | pages [17] -->
m

<!-- b005564 | prose | pages [17] -->
m

<!-- b005565 | prose | pages [17] -->
m

<!-- b005566 | prose | pages [17] -->
m

<!-- b005567 | prose | pages [17] -->
m

<!-- b005568 | prose | pages [17] -->
m

<!-- b005569 | prose | pages [17] -->
m

<!-- b005570 | prose | pages [17] -->
m

<!-- b005571 | prose | pages [17] -->
m

<!-- b005572 | prose | pages [17] -->
m

<!-- b005573 | prose | pages [17] -->
m

<!-- b005574 | prose | pages [17] -->
m

<!-- b005575 | prose | pages [17] -->
m

<!-- b005576 | prose | pages [17] -->
m

<!-- b005577 | prose | pages [17] -->
m

<!-- b005578 | prose | pages [17] -->
m

<!-- b005579 | prose | pages [17] -->
m

<!-- b005580 | prose | pages [17] -->
m

<!-- b005581 | prose | pages [17] -->
exposure levels, while operational improvements yield 45.4% reduction in average

<!-- b005582 | prose | pages [17] -->
m

<!-- b005583 | prose | pages [17] -->
m

<!-- b005584 | prose | pages [17] -->
m

<!-- b005585 | prose | pages [17] -->
m

<!-- b005586 | prose | pages [17] -->
m

<!-- b005587 | prose | pages [17] -->
m

<!-- b005588 | prose | pages [17] -->
m

<!-- b005589 | prose | pages [17] -->
m

<!-- b005590 | prose | pages [17] -->
m

<!-- b005591 | prose | pages [17] -->
m

<!-- b005592 | prose | pages [17] -->
m

<!-- b005593 | prose | pages [17] -->
m

<!-- b005594 | prose | pages [17] -->
m

<!-- b005595 | prose | pages [17] -->
m

<!-- b005596 | prose | pages [17] -->
m

<!-- b005597 | prose | pages [17] -->
m

<!-- b005598 | prose | pages [17] -->
m

<!-- b005599 | prose | pages [17] -->
m

<!-- b005600 | prose | pages [17] -->
m

<!-- b005601 | prose | pages [17] -->
m

<!-- b005602 | prose | pages [17] -->
m

<!-- b005603 | prose | pages [17] -->
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

<!-- b005807 | furniture | pages [17] -->
m

<!-- b005808 | furniture | pages [17] -->
m

<!-- b005809 | furniture | pages [17] -->
m

<!-- b005810 | furniture | pages [17] -->
m

<!-- b005811 | furniture | pages [17] -->
m

<!-- b005812 | furniture | pages [17] -->
m

<!-- b005813 | furniture | pages [17] -->
m

<!-- b005814 | furniture | pages [17] -->
m

<!-- b005815 | furniture | pages [17] -->
m

<!-- b005816 | furniture | pages [17] -->
m

<!-- b005817 | furniture | pages [17] -->
m

<!-- b005818 | furniture | pages [17] -->
m

<!-- b005819 | furniture | pages [17] -->
m

<!-- b005820 | furniture | pages [17] -->
m

<!-- b005821 | furniture | pages [17] -->
m

<!-- b005822 | furniture | pages [17] -->
m

<!-- b005823 | furniture | pages [17] -->
m

<!-- b005824 | furniture | pages [17] -->
m

<!-- b005825 | furniture | pages [17] -->
m

<!-- b005826 | furniture | pages [17] -->
m

<!-- b005827 | furniture | pages [17] -->
m

<!-- b005828 | furniture | pages [17] -->
m

<!-- b005829 | furniture | pages [17] -->
m

<!-- b005830 | furniture | pages [17] -->
m

<!-- b005831 | furniture | pages [17] -->
m

<!-- b005832 | furniture | pages [17] -->
m

<!-- b005833 | furniture | pages [17] -->
m

<!-- b005834 | furniture | pages [17] -->
m

<!-- b005835 | furniture | pages [17] -->
m

<!-- b005836 | furniture | pages [17] -->
m

<!-- b005837 | furniture | pages [17] -->
m

<!-- b005838 | furniture | pages [17] -->
m

<!-- b005839 | furniture | pages [17] -->
m

<!-- b005840 | furniture | pages [17] -->
m

<!-- b005841 | furniture | pages [17] -->
m

<!-- b005842 | furniture | pages [17] -->
m

<!-- b005843 | furniture | pages [17] -->
m

<!-- b005844 | furniture | pages [17] -->
m

<!-- b005845 | furniture | pages [17] -->
m

<!-- b005846 | furniture | pages [17] -->
m

<!-- b005847 | furniture | pages [17] -->
m

<!-- b005848 | furniture | pages [17] -->
m

<!-- b005849 | furniture | pages [17] -->
m

<!-- b005850 | furniture | pages [17] -->
m

<!-- b005851 | furniture | pages [17] -->
m

<!-- b005852 | furniture | pages [17] -->
m

<!-- b005853 | furniture | pages [17] -->
m

<!-- b005854 | furniture | pages [17] -->
m

<!-- b005855 | furniture | pages [17] -->
m

<!-- b005856 | furniture | pages [17] -->
m

<!-- b005857 | furniture | pages [17] -->
m

<!-- b005858 | furniture | pages [17] -->
m

<!-- b005859 | furniture | pages [17] -->
m

<!-- b005860 | furniture | pages [17] -->
m

<!-- b005861 | furniture | pages [17] -->
m

<!-- b005862 | furniture | pages [17] -->
m

<!-- b005863 | furniture | pages [17] -->
m

<!-- b005864 | furniture | pages [17] -->
m

<!-- b005865 | furniture | pages [17] -->
m

<!-- b005866 | furniture | pages [17] -->
m

<!-- b005867 | furniture | pages [17] -->
m

<!-- b005868 | furniture | pages [17] -->
m

<!-- b005869 | furniture | pages [17] -->
m

<!-- b005870 | furniture | pages [17] -->
m

<!-- b005871 | furniture | pages [17] -->
m

<!-- b005872 | furniture | pages [17] -->
m

<!-- b005873 | furniture | pages [17] -->
m

<!-- b005874 | furniture | pages [17] -->
m

<!-- b005875 | furniture | pages [17] -->
m

<!-- b005876 | furniture | pages [17] -->
m

<!-- b005877 | furniture | pages [17] -->
m

<!-- b005878 | furniture | pages [17] -->
m

<!-- b005879 | furniture | pages [17] -->
m

<!-- b005880 | furniture | pages [17] -->
m

<!-- b005881 | furniture | pages [17] -->
m

<!-- b005882 | furniture | pages [17] -->
m

<!-- b005883 | furniture | pages [17] -->
m

<!-- b005884 | furniture | pages [17] -->
m

<!-- b005885 | furniture | pages [17] -->
m

<!-- b005886 | furniture | pages [17] -->
m

<!-- b005887 | furniture | pages [17] -->
m

<!-- b005888 | furniture | pages [17] -->
m

<!-- b005889 | furniture | pages [17] -->
m

<!-- b005890 | furniture | pages [17] -->
m

<!-- b005891 | furniture | pages [17] -->
m

<!-- b005892 | furniture | pages [17] -->
m

<!-- b005893 | furniture | pages [17] -->
m

<!-- b005894 | furniture | pages [17] -->
m

<!-- b005895 | furniture | pages [17] -->
m

<!-- b005896 | furniture | pages [17] -->
m

<!-- b005897 | furniture | pages [17] -->
m

<!-- b005898 | furniture | pages [17] -->
m

<!-- b005899 | furniture | pages [17] -->
m

<!-- b005900 | furniture | pages [17] -->
m

<!-- b005901 | furniture | pages [17] -->
m

<!-- b005902 | furniture | pages [17] -->
m

<!-- b005903 | furniture | pages [17] -->
m

<!-- b005904 | furniture | pages [17] -->
m

<!-- b005905 | furniture | pages [17] -->
m

<!-- b005906 | furniture | pages [17] -->
m

<!-- b005907 | furniture | pages [17] -->
m

<!-- b005908 | furniture | pages [17] -->
m

<!-- b005909 | furniture | pages [17] -->
m

<!-- b005910 | furniture | pages [17] -->
m

<!-- b005911 | furniture | pages [17] -->
m

<!-- b005912 | furniture | pages [17] -->
m

<!-- b005913 | furniture | pages [17] -->
m

<!-- b005914 | furniture | pages [17] -->
m

<!-- b005915 | furniture | pages [17] -->
m

<!-- b005916 | furniture | pages [17] -->
m

<!-- b005917 | furniture | pages [17] -->
m

<!-- b005918 | furniture | pages [17] -->
m

<!-- b005919 | furniture | pages [17] -->
m

<!-- b005920 | furniture | pages [17] -->
m

<!-- b005921 | furniture | pages [17] -->
m

<!-- b005922 | furniture | pages [17] -->
m

<!-- b005923 | furniture | pages [17] -->
m

<!-- b005924 | furniture | pages [17] -->
m

<!-- b005925 | furniture | pages [17] -->
m

<!-- b005926 | furniture | pages [17] -->
m

<!-- b005927 | furniture | pages [17] -->
m

<!-- b005928 | furniture | pages [17] -->
m

<!-- b005929 | furniture | pages [17] -->
m

<!-- b005930 | furniture | pages [17] -->
m

<!-- b005931 | furniture | pages [17] -->
m

<!-- b005932 | furniture | pages [17] -->
m

<!-- b005933 | furniture | pages [17] -->
m

<!-- b005934 | furniture | pages [17] -->
m

<!-- b005935 | furniture | pages [17] -->
m

<!-- b005936 | furniture | pages [17] -->
m

<!-- b005937 | furniture | pages [17] -->
m

<!-- b005938 | furniture | pages [17] -->
m

<!-- b005939 | furniture | pages [17] -->
m

<!-- b005940 | furniture | pages [17] -->
m

<!-- b005941 | furniture | pages [17] -->
m

<!-- b005942 | furniture | pages [17] -->
m

<!-- b005943 | furniture | pages [17] -->
m

<!-- b005944 | furniture | pages [17] -->
m

<!-- b005945 | furniture | pages [17] -->
m

<!-- b005946 | furniture | pages [17] -->
m

<!-- b005947 | furniture | pages [17] -->
m

<!-- b005948 | furniture | pages [17] -->
m

<!-- b005949 | furniture | pages [17] -->
m

<!-- b005950 | furniture | pages [17] -->
m

<!-- b005951 | furniture | pages [17] -->
m

<!-- b005952 | furniture | pages [17] -->
m

<!-- b005953 | furniture | pages [17] -->
m

<!-- b005954 | furniture | pages [17] -->
m

<!-- b005955 | furniture | pages [17] -->
m

<!-- b005956 | furniture | pages [17] -->
m

<!-- b005957 | furniture | pages [17] -->
m

<!-- b005958 | furniture | pages [17] -->
m

<!-- b005959 | furniture | pages [17] -->
m

<!-- b005960 | furniture | pages [17] -->
m

<!-- b005961 | furniture | pages [17] -->
m

<!-- b005962 | furniture | pages [17] -->
m

<!-- b005963 | furniture | pages [17] -->
m

<!-- b005964 | furniture | pages [17] -->
m

<!-- b005965 | furniture | pages [17] -->
m

<!-- b005966 | furniture | pages [17] -->
m

<!-- b005967 | furniture | pages [17] -->
m

<!-- b005968 | furniture | pages [17] -->
m

<!-- b005969 | furniture | pages [17] -->
m

<!-- b005970 | furniture | pages [17] -->
m

<!-- b005971 | furniture | pages [17] -->
m

<!-- b005972 | furniture | pages [17] -->
m

<!-- b005973 | furniture | pages [17] -->
m

<!-- b005974 | furniture | pages [17] -->
m

<!-- b005975 | furniture | pages [17] -->
m

<!-- b005976 | furniture | pages [17] -->
m

<!-- b005977 | furniture | pages [17] -->
m

<!-- b005978 | furniture | pages [17] -->
m

<!-- b005979 | furniture | pages [17] -->
m

<!-- b005980 | furniture | pages [17] -->
m

<!-- b005981 | furniture | pages [17] -->
m

<!-- b005982 | furniture | pages [17] -->
m

<!-- b005983 | furniture | pages [17] -->
m

<!-- b005984 | furniture | pages [17] -->
m

<!-- b005985 | furniture | pages [17] -->
m

<!-- b005986 | furniture | pages [17] -->
m

<!-- b005987 | furniture | pages [17] -->
m

<!-- b005988 | furniture | pages [17] -->
m

<!-- b005989 | furniture | pages [17] -->
m

<!-- b005990 | furniture | pages [17] -->
m

<!-- b005991 | furniture | pages [17] -->
m

<!-- b005992 | furniture | pages [17] -->
m

<!-- b005993 | furniture | pages [17] -->
m

<!-- b005994 | furniture | pages [17] -->
m

<!-- b005995 | furniture | pages [17] -->
m

<!-- b005996 | furniture | pages [17] -->
m

<!-- b005997 | furniture | pages [17] -->
m

<!-- b005998 | furniture | pages [17] -->
m

<!-- b005999 | furniture | pages [17] -->
m

<!-- b006000 | furniture | pages [17] -->
m

<!-- b006001 | furniture | pages [17] -->
m

<!-- b006002 | furniture | pages [17] -->
m

<!-- b006003 | furniture | pages [17] -->
m

<!-- b006004 | furniture | pages [17] -->
m

<!-- b006005 | furniture | pages [17] -->
m

<!-- b006006 | furniture | pages [17] -->
m

<!-- b006007 | furniture | pages [19] -->
Team # 2516219

<!-- b006008 | prose | pages [19] -->
ments follow a conflict reduction metric:

<!-- b006009 | prose | pages [19] -->
K

<!-- b006010 | prose | pages [19] -->
1 −V post

<!-- b006011 | prose | pages [19] -->


<!-- b006012 | prose | pages [19] -->


<!-- b006013 | prose | pages [19] -->
X

<!-- b006014 | prose | pages [19] -->
k

<!-- b006015 | prose | pages [19] -->
∆Hcross =

<!-- b006016 | prose | pages [19] -->
V pre

<!-- b006017 | prose | pages [19] -->
k

<!-- b006018 | prose | pages [19] -->
k=1

<!-- b006019 | furniture | pages [19] -->
Page 19 of 24

<!-- b006020 | prose | pages [19] -->
· e−0.7·Sk = 32.69% reduction, (30)

<!-- b006021 | prose | pages [19] -->
where Vk and Sk denote vehicle-pedestrian conflict volume and intersection com- plexity, respectively.

<!-- b006022 | prose | pages [19] -->
微信公众号：数学模型

<!-- b006023 | prose | pages [19] -->
We used images to show the possible impact on stakeholders of adding bus lane or crosswalks on major streets, as shown in Figure 9:

<!-- b006024 | prose | pages [19] -->
微信号：MATHmodels

<!-- b006025 | caption | pages [19] -->
Figure 9: Impact of transport projects

<!-- b006026 | prose | pages [19] -->
7.6

<!-- b006027 | heading | pages [19] -->
Sensitivity Analysis

<!-- b006028 | prose | pages [19] -->
Critical parameter responses exhibit nonlinear phase-space dynamics. Bus mode share sensitivity to headway follows a power law ∂Pbus/∂hj = −0.21/h0.67

<!-- b006029 | prose | pages [19] -->
, while j accessibility gains decay sigmoidally with catchment radius ∂Ai/∂Racc = 2.4/(1 + e(Racc−600)/150). System instability emerges at congestion collapse thresholds:

<!-- b006030 | prose | pages [19] -->
> 0.85 ⇒∂tb

<!-- b006031 | prose | pages [19] -->
fb Cb

<!-- b006032 | prose | pages [19] -->
→∞, (31)

<!-- b006033 | prose | pages [19] -->
∂fb

<!-- b006034 | prose | pages [19] -->
characterizing critical passenger load ratios where marginal impedance becomes discontinuous.

<!-- b006035 | prose | pages [19] -->
This analytical framework rigorously captures (1) distributional welfare effects across socioeconomic cohorts, (2) nonlinear interactions between mobility supply and urban economic activity, and (3) bifurcation phenomena in network performance, provid- ing policymakers with multi-dimensional evaluation metrics for sustainable transport planning. The coupled discrete choice and network loading formulation enables pre- cise counterfactual analysis of infrastructure investments while maintaining computa- tional tractability through convex impedance functions and logit-based demand equi- libria. The results of sensitivity analysis is shown in Figure 10.

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

<!-- b006119 | prose | pages [19] -->
m

<!-- b006120 | prose | pages [19] -->
m

<!-- b006121 | prose | pages [19] -->
m

<!-- b006122 | prose | pages [19] -->
m

<!-- b006123 | prose | pages [19] -->
m

<!-- b006124 | prose | pages [19] -->
m

<!-- b006125 | prose | pages [19] -->
m

<!-- b006126 | prose | pages [19] -->
m

<!-- b006127 | prose | pages [19] -->
m

<!-- b006128 | prose | pages [19] -->
m

<!-- b006129 | prose | pages [19] -->
m

<!-- b006130 | prose | pages [19] -->
m

<!-- b006131 | prose | pages [19] -->
m

<!-- b006132 | prose | pages [19] -->
m

<!-- b006133 | prose | pages [19] -->
m

<!-- b006134 | prose | pages [19] -->
m

<!-- b006135 | prose | pages [19] -->
m

<!-- b006136 | prose | pages [19] -->
m

<!-- b006137 | prose | pages [19] -->
m

<!-- b006138 | prose | pages [19] -->
m

<!-- b006139 | prose | pages [19] -->
m

<!-- b006140 | prose | pages [19] -->
m

<!-- b006141 | prose | pages [19] -->
m

<!-- b006142 | prose | pages [19] -->
m

<!-- b006143 | prose | pages [19] -->
m

<!-- b006144 | prose | pages [19] -->
m

<!-- b006145 | prose | pages [19] -->
m

<!-- b006146 | prose | pages [19] -->
m

<!-- b006147 | prose | pages [19] -->
m

<!-- b006148 | prose | pages [19] -->
m

<!-- b006149 | prose | pages [19] -->
m

<!-- b006150 | prose | pages [19] -->
m

<!-- b006151 | prose | pages [19] -->
m

<!-- b006152 | prose | pages [19] -->
m

<!-- b006153 | prose | pages [19] -->
m

<!-- b006154 | prose | pages [19] -->
m

<!-- b006155 | prose | pages [19] -->
m

<!-- b006156 | prose | pages [19] -->
m

<!-- b006157 | prose | pages [19] -->
m

<!-- b006158 | prose | pages [19] -->
m

<!-- b006159 | prose | pages [19] -->
m

<!-- b006160 | prose | pages [19] -->
m

<!-- b006161 | prose | pages [19] -->
m

<!-- b006162 | prose | pages [19] -->
m

<!-- b006163 | prose | pages [19] -->
m

<!-- b006164 | prose | pages [19] -->
m

<!-- b006165 | prose | pages [19] -->
m

<!-- b006166 | prose | pages [19] -->
m

<!-- b006167 | prose | pages [19] -->
m

<!-- b006168 | prose | pages [19] -->
m

<!-- b006169 | prose | pages [19] -->
m

<!-- b006170 | prose | pages [19] -->
m

<!-- b006171 | prose | pages [19] -->
m

<!-- b006172 | prose | pages [19] -->
m

<!-- b006173 | prose | pages [19] -->
m

<!-- b006174 | prose | pages [19] -->
m

<!-- b006175 | prose | pages [19] -->
m

<!-- b006176 | prose | pages [19] -->
m

<!-- b006177 | prose | pages [19] -->
m

<!-- b006178 | prose | pages [19] -->
m

<!-- b006179 | prose | pages [19] -->
m

<!-- b006180 | prose | pages [19] -->
m

<!-- b006181 | prose | pages [19] -->
m

<!-- b006182 | prose | pages [19] -->
m

<!-- b006183 | prose | pages [19] -->
m

<!-- b006184 | prose | pages [19] -->
m

<!-- b006185 | prose | pages [19] -->
m

<!-- b006186 | prose | pages [19] -->
m

<!-- b006187 | prose | pages [19] -->
m

<!-- b006188 | prose | pages [19] -->
m

<!-- b006189 | prose | pages [19] -->
m

<!-- b006190 | prose | pages [19] -->
m

<!-- b006191 | prose | pages [19] -->
m

<!-- b006192 | prose | pages [19] -->
m

<!-- b006193 | prose | pages [19] -->
m

<!-- b006194 | prose | pages [19] -->
m

<!-- b006195 | prose | pages [19] -->
m

<!-- b006196 | prose | pages [19] -->
m

<!-- b006197 | prose | pages [19] -->
m

<!-- b006198 | prose | pages [19] -->
m

<!-- b006199 | prose | pages [19] -->
m

<!-- b006200 | prose | pages [19] -->
m

<!-- b006201 | prose | pages [19] -->
m

<!-- b006202 | prose | pages [19] -->
m

<!-- b006203 | prose | pages [19] -->
m

<!-- b006204 | prose | pages [19] -->
m

<!-- b006205 | prose | pages [19] -->
m

<!-- b006206 | prose | pages [19] -->
m

<!-- b006207 | prose | pages [19] -->
m

<!-- b006208 | prose | pages [19] -->
m

<!-- b006209 | prose | pages [19] -->
m

<!-- b006210 | prose | pages [19] -->
m

<!-- b006211 | prose | pages [19] -->
m

<!-- b006212 | prose | pages [19] -->
m

<!-- b006213 | prose | pages [19] -->
m

<!-- b006214 | prose | pages [19] -->
m

<!-- b006215 | prose | pages [19] -->
m

<!-- b006216 | prose | pages [19] -->
m

<!-- b006217 | prose | pages [19] -->
m

<!-- b006218 | prose | pages [19] -->
m

<!-- b006219 | prose | pages [19] -->
m

<!-- b006220 | prose | pages [19] -->
m

<!-- b006221 | prose | pages [19] -->
m

<!-- b006222 | prose | pages [19] -->
m

<!-- b006223 | prose | pages [19] -->
m

<!-- b006224 | prose | pages [19] -->
m

<!-- b006225 | prose | pages [19] -->
m

<!-- b006226 | prose | pages [19] -->
m

<!-- b006227 | prose | pages [19] -->
m

<!-- b006228 | prose | pages [19] -->
m

<!-- b006229 | prose | pages [19] -->
m

<!-- b006230 | prose | pages [19] -->
m

<!-- b006231 | prose | pages [19] -->
m

<!-- b006232 | prose | pages [19] -->
m

<!-- b006233 | prose | pages [19] -->
m

<!-- b006234 | prose | pages [19] -->
m

<!-- b006235 | prose | pages [19] -->
m

<!-- b006236 | prose | pages [19] -->
m

<!-- b006237 | prose | pages [19] -->
m

<!-- b006238 | prose | pages [19] -->
m

<!-- b006239 | prose | pages [19] -->
m

<!-- b006240 | prose | pages [19] -->
m

<!-- b006241 | prose | pages [19] -->
m

<!-- b006242 | prose | pages [19] -->
m

<!-- b006243 | prose | pages [19] -->
m

<!-- b006244 | prose | pages [19] -->
m

<!-- b006245 | prose | pages [19] -->
m

<!-- b006246 | prose | pages [19] -->
m

<!-- b006247 | prose | pages [19] -->
m

<!-- b006248 | prose | pages [19] -->
m

<!-- b006249 | prose | pages [19] -->
m

<!-- b006250 | prose | pages [19] -->
m

<!-- b006251 | prose | pages [19] -->
m

<!-- b006252 | prose | pages [19] -->
m

<!-- b006253 | prose | pages [19] -->
m

<!-- b006254 | prose | pages [19] -->
m

<!-- b006255 | prose | pages [19] -->
m

<!-- b006256 | prose | pages [19] -->
m

<!-- b006257 | prose | pages [19] -->
m

<!-- b006258 | prose | pages [19] -->
m

<!-- b006259 | prose | pages [19] -->
m

<!-- b006260 | prose | pages [19] -->
m

<!-- b006261 | prose | pages [19] -->
m

<!-- b006262 | prose | pages [19] -->
m

<!-- b006263 | prose | pages [19] -->
m

<!-- b006264 | prose | pages [19] -->
m

<!-- b006265 | prose | pages [19] -->
m

<!-- b006266 | prose | pages [19] -->
m

<!-- b006267 | prose | pages [19] -->
m

<!-- b006268 | prose | pages [19] -->
m

<!-- b006269 | prose | pages [19] -->
m

<!-- b006270 | prose | pages [19] -->
m

<!-- b006271 | prose | pages [19] -->
m

<!-- b006272 | prose | pages [19] -->
m

<!-- b006273 | prose | pages [19] -->
m

<!-- b006274 | prose | pages [19] -->
m

<!-- b006275 | prose | pages [19] -->
m

<!-- b006276 | prose | pages [19] -->
m

<!-- b006277 | prose | pages [19] -->
m

<!-- b006278 | prose | pages [19] -->
m

<!-- b006279 | prose | pages [19] -->
m

<!-- b006280 | prose | pages [19] -->
m

<!-- b006281 | prose | pages [19] -->
m

<!-- b006282 | prose | pages [19] -->
m

<!-- b006283 | prose | pages [19] -->
m

<!-- b006284 | prose | pages [19] -->
m

<!-- b006285 | prose | pages [19] -->
m

<!-- b006286 | prose | pages [19] -->
m

<!-- b006287 | prose | pages [19] -->
m

<!-- b006288 | prose | pages [19] -->
m

<!-- b006289 | prose | pages [19] -->
m

<!-- b006290 | prose | pages [19] -->
m

<!-- b006291 | prose | pages [19] -->
m

<!-- b006292 | prose | pages [19] -->
m

<!-- b006293 | prose | pages [19] -->
m

<!-- b006294 | prose | pages [19] -->
m

<!-- b006295 | prose | pages [19] -->
m

<!-- b006296 | prose | pages [19] -->
m

<!-- b006297 | prose | pages [19] -->
m

<!-- b006298 | prose | pages [19] -->
m

<!-- b006299 | prose | pages [19] -->
m

<!-- b006300 | prose | pages [19] -->
m

<!-- b006301 | prose | pages [19] -->
m

<!-- b006302 | prose | pages [19] -->
m

<!-- b006303 | prose | pages [19] -->
m

<!-- b006304 | prose | pages [19] -->
m

<!-- b006305 | prose | pages [19] -->
m

<!-- b006306 | prose | pages [19] -->
m

<!-- b006307 | prose | pages [19] -->
m

<!-- b006308 | prose | pages [19] -->
m

<!-- b006309 | prose | pages [19] -->
m

<!-- b006310 | prose | pages [19] -->
m

<!-- b006311 | prose | pages [19] -->
m

<!-- b006312 | prose | pages [19] -->
m

<!-- b006313 | prose | pages [19] -->
m

<!-- b006314 | prose | pages [19] -->
m

<!-- b006315 | prose | pages [19] -->
m

<!-- b006316 | prose | pages [19] -->
m

<!-- b006317 | prose | pages [19] -->
m

<!-- b006318 | prose | pages [19] -->
m

<!-- b006319 | prose | pages [19] -->
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

<!-- b006522 | furniture | pages [19] -->
m

<!-- b006523 | furniture | pages [19] -->
m

<!-- b006524 | furniture | pages [19] -->
m

<!-- b006525 | furniture | pages [19] -->
m

<!-- b006526 | furniture | pages [19] -->
m

<!-- b006527 | furniture | pages [19] -->
m

<!-- b006528 | furniture | pages [19] -->
m

<!-- b006529 | furniture | pages [19] -->
m

<!-- b006530 | furniture | pages [19] -->
m

<!-- b006531 | furniture | pages [19] -->
m

<!-- b006532 | furniture | pages [19] -->
m

<!-- b006533 | furniture | pages [19] -->
m

<!-- b006534 | furniture | pages [19] -->
m

<!-- b006535 | furniture | pages [19] -->
m

<!-- b006536 | furniture | pages [19] -->
m

<!-- b006537 | furniture | pages [19] -->
m

<!-- b006538 | furniture | pages [19] -->
m

<!-- b006539 | furniture | pages [19] -->
m

<!-- b006540 | furniture | pages [19] -->
m

<!-- b006541 | furniture | pages [19] -->
m

<!-- b006542 | furniture | pages [19] -->
m

<!-- b006543 | furniture | pages [19] -->
m

<!-- b006544 | furniture | pages [19] -->
m

<!-- b006545 | furniture | pages [19] -->
m

<!-- b006546 | furniture | pages [19] -->
m

<!-- b006547 | furniture | pages [19] -->
m

<!-- b006548 | furniture | pages [19] -->
m

<!-- b006549 | furniture | pages [19] -->
m

<!-- b006550 | furniture | pages [19] -->
m

<!-- b006551 | furniture | pages [19] -->
m

<!-- b006552 | furniture | pages [19] -->
m

<!-- b006553 | furniture | pages [19] -->
m

<!-- b006554 | furniture | pages [19] -->
m

<!-- b006555 | furniture | pages [19] -->
m

<!-- b006556 | furniture | pages [19] -->
m

<!-- b006557 | furniture | pages [19] -->
m

<!-- b006558 | furniture | pages [19] -->
m

<!-- b006559 | furniture | pages [19] -->
m

<!-- b006560 | furniture | pages [19] -->
m

<!-- b006561 | furniture | pages [19] -->
m

<!-- b006562 | furniture | pages [19] -->
m

<!-- b006563 | furniture | pages [19] -->
m

<!-- b006564 | furniture | pages [19] -->
m

<!-- b006565 | furniture | pages [19] -->
m

<!-- b006566 | furniture | pages [19] -->
m

<!-- b006567 | furniture | pages [19] -->
m

<!-- b006568 | furniture | pages [19] -->
m

<!-- b006569 | furniture | pages [19] -->
m

<!-- b006570 | furniture | pages [19] -->
m

<!-- b006571 | furniture | pages [19] -->
m

<!-- b006572 | furniture | pages [19] -->
m

<!-- b006573 | furniture | pages [19] -->
m

<!-- b006574 | furniture | pages [19] -->
m

<!-- b006575 | furniture | pages [19] -->
m

<!-- b006576 | furniture | pages [19] -->
m

<!-- b006577 | furniture | pages [19] -->
m

<!-- b006578 | furniture | pages [19] -->
m

<!-- b006579 | furniture | pages [19] -->
m

<!-- b006580 | furniture | pages [19] -->
m

<!-- b006581 | furniture | pages [19] -->
m

<!-- b006582 | furniture | pages [19] -->
m

<!-- b006583 | furniture | pages [19] -->
m

<!-- b006584 | furniture | pages [19] -->
m

<!-- b006585 | furniture | pages [19] -->
m

<!-- b006586 | furniture | pages [19] -->
m

<!-- b006587 | furniture | pages [19] -->
m

<!-- b006588 | furniture | pages [19] -->
m

<!-- b006589 | furniture | pages [19] -->
m

<!-- b006590 | furniture | pages [19] -->
m

<!-- b006591 | furniture | pages [19] -->
m

<!-- b006592 | furniture | pages [19] -->
m

<!-- b006593 | furniture | pages [19] -->
m

<!-- b006594 | furniture | pages [19] -->
m

<!-- b006595 | furniture | pages [19] -->
m

<!-- b006596 | furniture | pages [19] -->
m

<!-- b006597 | furniture | pages [19] -->
m

<!-- b006598 | furniture | pages [19] -->
m

<!-- b006599 | furniture | pages [19] -->
m

<!-- b006600 | furniture | pages [19] -->
m

<!-- b006601 | furniture | pages [19] -->
m

<!-- b006602 | furniture | pages [19] -->
m

<!-- b006603 | furniture | pages [19] -->
m

<!-- b006604 | furniture | pages [19] -->
m

<!-- b006605 | furniture | pages [19] -->
m

<!-- b006606 | furniture | pages [19] -->
m

<!-- b006607 | furniture | pages [19] -->
m

<!-- b006608 | furniture | pages [19] -->
m

<!-- b006609 | furniture | pages [19] -->
m

<!-- b006610 | furniture | pages [19] -->
m

<!-- b006611 | furniture | pages [19] -->
m

<!-- b006612 | furniture | pages [19] -->
m

<!-- b006613 | furniture | pages [19] -->
m

<!-- b006614 | furniture | pages [19] -->
m

<!-- b006615 | furniture | pages [19] -->
m

<!-- b006616 | furniture | pages [19] -->
m

<!-- b006617 | furniture | pages [19] -->
m

<!-- b006618 | furniture | pages [19] -->
m

<!-- b006619 | furniture | pages [19] -->
m

<!-- b006620 | furniture | pages [19] -->
m

<!-- b006621 | furniture | pages [19] -->
m

<!-- b006622 | furniture | pages [19] -->
m

<!-- b006623 | furniture | pages [19] -->
m

<!-- b006624 | furniture | pages [19] -->
m

<!-- b006625 | furniture | pages [19] -->
m

<!-- b006626 | furniture | pages [19] -->
m

<!-- b006627 | furniture | pages [19] -->
m

<!-- b006628 | furniture | pages [19] -->
m

<!-- b006629 | furniture | pages [19] -->
m

<!-- b006630 | furniture | pages [19] -->
m

<!-- b006631 | furniture | pages [19] -->
m

<!-- b006632 | furniture | pages [19] -->
m

<!-- b006633 | furniture | pages [19] -->
m

<!-- b006634 | furniture | pages [19] -->
m

<!-- b006635 | furniture | pages [19] -->
m

<!-- b006636 | furniture | pages [19] -->
m

<!-- b006637 | furniture | pages [19] -->
m

<!-- b006638 | furniture | pages [19] -->
m

<!-- b006639 | furniture | pages [19] -->
m

<!-- b006640 | furniture | pages [19] -->
m

<!-- b006641 | furniture | pages [19] -->
m

<!-- b006642 | furniture | pages [19] -->
m

<!-- b006643 | furniture | pages [19] -->
m

<!-- b006644 | furniture | pages [19] -->
m

<!-- b006645 | furniture | pages [19] -->
m

<!-- b006646 | furniture | pages [19] -->
m

<!-- b006647 | furniture | pages [19] -->
m

<!-- b006648 | furniture | pages [19] -->
m

<!-- b006649 | furniture | pages [19] -->
m

<!-- b006650 | furniture | pages [19] -->
m

<!-- b006651 | furniture | pages [19] -->
m

<!-- b006652 | furniture | pages [19] -->
m

<!-- b006653 | furniture | pages [19] -->
m

<!-- b006654 | furniture | pages [19] -->
m

<!-- b006655 | furniture | pages [19] -->
m

<!-- b006656 | furniture | pages [19] -->
m

<!-- b006657 | furniture | pages [19] -->
m

<!-- b006658 | furniture | pages [19] -->
m

<!-- b006659 | furniture | pages [19] -->
m

<!-- b006660 | furniture | pages [19] -->
m

<!-- b006661 | furniture | pages [19] -->
m

<!-- b006662 | furniture | pages [19] -->
m

<!-- b006663 | furniture | pages [19] -->
m

<!-- b006664 | furniture | pages [19] -->
m

<!-- b006665 | furniture | pages [19] -->
m

<!-- b006666 | furniture | pages [19] -->
m

<!-- b006667 | furniture | pages [19] -->
m

<!-- b006668 | furniture | pages [19] -->
m

<!-- b006669 | furniture | pages [19] -->
m

<!-- b006670 | furniture | pages [19] -->
m

<!-- b006671 | furniture | pages [19] -->
m

<!-- b006672 | furniture | pages [19] -->
m

<!-- b006673 | furniture | pages [19] -->
m

<!-- b006674 | furniture | pages [19] -->
m

<!-- b006675 | furniture | pages [19] -->
m

<!-- b006676 | furniture | pages [19] -->
m

<!-- b006677 | furniture | pages [19] -->
m

<!-- b006678 | furniture | pages [19] -->
m

<!-- b006679 | furniture | pages [19] -->
m

<!-- b006680 | furniture | pages [19] -->
m

<!-- b006681 | furniture | pages [19] -->
m

<!-- b006682 | furniture | pages [19] -->
m

<!-- b006683 | furniture | pages [19] -->
m

<!-- b006684 | furniture | pages [19] -->
m

<!-- b006685 | furniture | pages [19] -->
m

<!-- b006686 | furniture | pages [19] -->
m

<!-- b006687 | furniture | pages [19] -->
m

<!-- b006688 | furniture | pages [19] -->
m

<!-- b006689 | furniture | pages [19] -->
m

<!-- b006690 | furniture | pages [19] -->
m

<!-- b006691 | furniture | pages [19] -->
m

<!-- b006692 | furniture | pages [19] -->
m

<!-- b006693 | furniture | pages [19] -->
m

<!-- b006694 | furniture | pages [19] -->
m

<!-- b006695 | furniture | pages [19] -->
m

<!-- b006696 | furniture | pages [19] -->
m

<!-- b006697 | furniture | pages [19] -->
m

<!-- b006698 | furniture | pages [19] -->
m

<!-- b006699 | furniture | pages [19] -->
m

<!-- b006700 | furniture | pages [19] -->
m

<!-- b006701 | furniture | pages [19] -->
m

<!-- b006702 | furniture | pages [19] -->
m

<!-- b006703 | furniture | pages [19] -->
m

<!-- b006704 | furniture | pages [19] -->
m

<!-- b006705 | furniture | pages [19] -->
m

<!-- b006706 | furniture | pages [19] -->
m

<!-- b006707 | furniture | pages [19] -->
m

<!-- b006708 | furniture | pages [19] -->
m

<!-- b006709 | furniture | pages [19] -->
m

<!-- b006710 | furniture | pages [19] -->
m

<!-- b006711 | furniture | pages [19] -->
m

<!-- b006712 | furniture | pages [19] -->
m

<!-- b006713 | furniture | pages [19] -->
m

<!-- b006714 | furniture | pages [19] -->
m

<!-- b006715 | furniture | pages [19] -->
m

<!-- b006716 | furniture | pages [19] -->
m

<!-- b006717 | furniture | pages [19] -->
m

<!-- b006718 | furniture | pages [19] -->
m

<!-- b006719 | furniture | pages [19] -->
m

<!-- b006720 | furniture | pages [19] -->
m

<!-- b006721 | furniture | pages [19] -->
m

<!-- b006722 | furniture | pages [19] -->
m

<!-- b006723 | furniture | pages [20] -->
Team # 2516219

<!-- b006724 | furniture | pages [20] -->
Page 20 of 24

<!-- b006725 | caption | pages [20] -->
Figure 10: Sensitivity Analysis

<!-- b006726 | heading | pages [20] -->
Optimal Transportation Network Intervention Model

<!-- b006727 | prose | pages [20] -->
8 for Baltimore

<!-- b006728 | heading | pages [20] -->
Project Recommendation: Integrated Mobility Corridor (IMC)

<!-- b006729 | prose | pages [20] -->
8.1

<!-- b006730 | prose | pages [20] -->
The proposed Integrated Mobility Corridor (IMC) system synthesizes multimodal transportation infrastructure through dedicated bus lanes, pedestrian-priority urban zones, and spatially optimized micro-mobility hubs. This intervention framework is formalized via a tri-objective optimization paradigm:

<!-- b006731 | prose | pages [20] -->
x∈X [f1(x), −f2(x), f3(x)]

<!-- b006732 | prose | pages [20] -->
max

<!-- b006733 | prose | pages [20] -->
(32)

<!-- b006734 | prose | pages [20] -->
where the objective vector comprises resident welfare enhancement f1(x), imple- mentation cost minimization −f2(x), and environmental benefit maximization f3(x), subject to the feasible intervention set X. The decision vector x = (xb, xp, xm) ∈R3

<!-- b006735 | prose | pages [20] -->
+ quantifies infrastructure investments as bus lane kilometers xb, pedestrian infrastruc- ture quality score xp ∈[0, 100], and micro-mobility station density xm (stations per km²).

<!-- b006736 | prose | pages [20] -->
8.2

<!-- b006737 | heading | pages [20] -->
Benefit Quantification Model

<!-- b006738 | prose | pages [20] -->
Resident welfare gains emerge through three primary mechanisms.

<!-- b006739 | prose | pages [20] -->
First, gen- eralized travel cost reductions across origin-destination pairs are quantified through modal shift probabilities Pm|od derived from nested logit models:

<!-- b006740 | prose | pages [20] -->
X

<!-- b006741 | prose | pages [20] -->
(cm

<!-- b006742 | prose | pages [20] -->
∆Cm

<!-- b006743 | prose | pages [20] -->
od =

<!-- b006744 | prose | pages [20] -->
m∈{bus,walk}

<!-- b006745 | prose | pages [20] -->
od(x0) −cm

<!-- b006746 | prose | pages [20] -->
od(x)) Pm|od (33)

<!-- b006747 | prose | pages [20] -->
Second, population health improvements combine physical activity benefits from pedestrian infrastructure and air quality enhancements from bus prioritization. The health production function integrates WHO-derived quality-adjusted life year (QALY) coefficients ϕwalk = 0.0032 QALY/km and ψhealth = 1.2 × 10−4 QALY/(µ g/m³):

<!-- b006748 | prose | pages [20] -->
∂Ai

<!-- b006749 | prose | pages [20] -->


<!-- b006750 | prose | pages [20] -->
· ϕwalk + ∂PM2.5,i

<!-- b006751 | prose | pages [20] -->
X

<!-- b006752 | prose | pages [20] -->
∆H =

<!-- b006753 | prose | pages [20] -->
∂xp

<!-- b006754 | prose | pages [20] -->
i∈N

<!-- b006755 | prose | pages [20] -->
· ψhealth

<!-- b006756 | prose | pages [20] -->
(34)

<!-- b006757 | prose | pages [20] -->
关注数学模型

<!-- b006758 | prose | pages [20] -->
∂xb

<!-- b006759 | furniture | pages [20] -->
2

<!-- b006760 | furniture | pages [20] -->
MATHmodels

<!-- b006761 | furniture | pages [20] -->
获取更多资讯

<!-- b006762 | furniture | pages [21] -->
Team # 2516219

<!-- b006763 | furniture | pages [21] -->
Page 21 of 24

<!-- b006764 | prose | pages [21] -->
Third, economic accessibility improvements follow logistic diffusion dynamics with σA = 0.18 modeling spatial inequality attenuation:

<!-- b006765 | prose | pages [21] -->
Γi = 1 (35) 1 + e−(∆Aτ i /σA)

<!-- b006766 | prose | pages [21] -->
We use Inner Harbor, Federal Hill, Fell’s Point, Hampden, Mount Vernon 5 region to analysis. The quantification of residents’ welfare is shown in the Figure 11 as below:

<!-- b006767 | prose | pages [21] -->
微信公众号：数学模型

<!-- b006768 | prose | pages [21] -->
(a) Decomposition of Health Benefits (b) Commerciasl Revenue Elasticity

<!-- b006769 | caption | pages [21] -->
Figure 11: Quantifying residents’ well-being

<!-- b006770 | prose | pages [21] -->
微信号：MATHmodels

<!-- b006771 | prose | pages [21] -->
The municipal cost-benefit ratio incorporates discounted tax revenue gains and public health savings against capital and operational expenditures:

<!-- b006772 | prose | pages [21] -->
PT

<!-- b006773 | prose | pages [21] -->
t=0 δt[∆Taxt + ∆Healtht]

<!-- b006774 | prose | pages [21] -->
BCR =

<!-- b006775 | prose | pages [21] -->
PT

<!-- b006776 | prose | pages [21] -->
(36)

<!-- b006777 | prose | pages [21] -->
t=0 δt[Ccap + CO&M]

<!-- b006778 | prose | pages [21] -->
with δ = 0.96 reflecting Maryland’s intertemporal fiscal policy. Commercial entities experience revenue variations through pedestrian traffic elasticities and accessibility transformations:

<!-- b006779 | prose | pages [21] -->
∆Revj = βped · ln(1 + ∆fped,j) + βtransit · erf(∆Aj/0.3) (37)

<!-- b006780 | prose | pages [21] -->
where βped = 0.18 and βtransit = 0.22 calibrate Baltimore Central Business District retail responses. Transit operators realize profit variations through farebox recovery and bus priority operational efficiencies:

<!-- b006781 | prose | pages [21] -->
Πb = pb · ∆qb −cvkm · Lb · e−0.7xb (38)

<!-- b006782 | prose | pages [21] -->
with vehicle-km costs cvkm = $2.14 modulated by bus lane coverage intensity.

<!-- b006783 | prose | pages [21] -->
8.3 System Disruption Analysis

<!-- b006784 | prose | pages [21] -->
Temporary network degradation during IMC construction follows time-dependent edge capacity constraints:

<!-- b006785 | prose | pages [21] -->
ce(t) = c0

<!-- b006786 | prose | pages [21] -->
e · [1 + κ · sigmoid(tstart, tend)] (39)

<!-- b006787 | furniture | pages [22] -->
Team # 2516219

<!-- b006788 | furniture | pages [22] -->
Page 22 of 24

<!-- b006789 | prose | pages [22] -->
where κ ∼U[0.3, 0.6] captures stochastic lane closure impacts. Automobile user disutility from lane reallocation exhibits nonlinear congestion effects:

<!-- b006790 | prose | pages [22] -->


<!-- b006791 | prose | pages [22] -->
∆cauto = xb

<!-- b006792 | prose | pages [22] -->
·

<!-- b006793 | prose | pages [22] -->
Ltot

<!-- b006794 | prose | pages [22] -->
β

<!-- b006795 | prose | pages [22] -->
qauto

<!-- b006796 | prose | pages [22] -->
(40)

<!-- b006797 | prose | pages [22] -->
qauto −∆qmode

<!-- b006798 | prose | pages [22] -->
with Baltimore-specific elasticity β = 2.1. Equity impacts manifest through tran- sient Gini coefficient dynamics:

<!-- b006799 | prose | pages [22] -->
G(t) = G0e−λt + θ∆A (41) 1 + e−(t−t0)/τ

<!-- b006800 | prose | pages [22] -->
where τ = 18-month adaptation period reflects societal adjustment to accessibility shocks.

<!-- b006801 | prose | pages [22] -->
8.4 Implementation Framework

<!-- b006802 | prose | pages [22] -->
The implementation architecture adopts a multi-stage optimization process with

<!-- b006803 | prose | pages [22] -->
[7]

<!-- b006804 | prose | pages [22] -->
phased resource allocation.

<!-- b006805 | prose | pages [22] -->
Stage 1: Initial infrastructure deployment prioritizes network resilience through

<!-- b006806 | prose | pages [22] -->
e∈E E[ce(t1)]. Where

<!-- b006807 | prose | pages [22] -->
P

<!-- b006808 | prose | pages [22] -->
bus lane optimization under stochastic capacity constraints: minx(1)

<!-- b006809 | prose | pages [22] -->
b

<!-- b006810 | prose | pages [22] -->
temporal edge costs ce(t1) incorporate construction-phase disruptions.

<!-- b006811 | prose | pages [22] -->
Stage 2: Subsequent stages transition to equity-driven pedestrian infrastructure optimization: maxxp mini∈N Ai(xp)

<!-- b006812 | prose | pages [22] -->
Stage 3: ensuring minimal neighborhood accessibility Ai meets predefined social thresholds. The final stage resolves multi-objective tradeoffs through epsilon-constraint methods: Pareto frontier analysis of (f1, f2, f3)

<!-- b006813 | prose | pages [22] -->
Model parameters derive from Bayesian calibration using Markov Chain Monte

<!-- b006814 | prose | pages [22] -->
[8] techniques informed by cross-city transportation datasets:

<!-- b006815 | prose | pages [22] -->
Carlo (MCMC)

<!-- b006816 | prose | pages [22] -->
K Y

<!-- b006817 | prose | pages [22] -->
N(yk|f(xk, θ), Σ) · pprior(θ)

<!-- b006818 | prose | pages [22] -->
p(θ|D) ∝

<!-- b006819 | prose | pages [22] -->
k=1

<!-- b006820 | prose | pages [22] -->
(42)

<!-- b006821 | prose | pages [22] -->
where D assimilates performance metrics from 15 U.S. urban corridor projects span- ning 2010–2022.

<!-- b006822 | prose | pages [22] -->
Case Study: Baltimore Green Transit Corridor 8.5

<!-- b006823 | prose | pages [22] -->
Empirical validation through Baltimore’s proposed green transit corridor demon- strates substantial systemic improvements (Table 2). The optimized IMC configura- tion elevates resident welfare by 58% while compressing accessibility inequality (Gini coefficient reduction from 0.41 to 0.33). Environmental benefits materialize through 18.7% PM2.5 concentration abatement, coupled with favorable fiscal returns evidenced by benefit-cost ratio BCR = 1.41.

<!-- b006824 | prose | pages [22] -->
Nonlinear response surfaces govern welfare scaling laws:

<!-- b006825 | prose | pages [22] -->
关注数学模型

<!-- b006826 | furniture | pages [22] -->
2

<!-- b006827 | furniture | pages [22] -->
MATHmodels

<!-- b006828 | furniture | pages [22] -->
获取更多资讯

<!-- b006829 | furniture | pages [23] -->
Team # 2516219

<!-- b006830 | prose | pages [23] -->
∂f1

<!-- b006831 | prose | pages [23] -->
= 0.24x−0.3

<!-- b006832 | prose | pages [23] -->
, b

<!-- b006833 | prose | pages [23] -->
∂xb

<!-- b006834 | furniture | pages [23] -->
Page 23 of 24

<!-- b006835 | prose | pages [23] -->
∂2f1

<!-- b006836 | prose | pages [23] -->
= −0.17e−0.09xp (43)

<!-- b006837 | prose | pages [23] -->
∂x2

<!-- b006838 | prose | pages [23] -->
p

<!-- b006839 | prose | pages [23] -->
revealing diminishing returns for bus lane expansion and concave pedestrian in- frastructure effects. Phase transition analysis identifies critical infrastructure thresh- olds:

<!-- b006840 | prose | pages [23] -->
微信公众号：数学模型

<!-- b006841 | prose | pages [23] -->
xb > 0.3Ltot ⇒∂∆cauto

<!-- b006842 | prose | pages [23] -->
→∞ (44)

<!-- b006843 | prose | pages [23] -->
∂xb

<!-- b006844 | prose | pages [23] -->
indicating auto user cost sensitivities escalate catastrophically beyond 30% lane re- allocation. This analytical framework enables cities to navigate complex tradeoffs be- tween mobility efficiency, environmental sustainability, and social equity in transporta- tion planning.

<!-- b006845 | prose | pages [23] -->
The effect of quantifying residents’ welfare, implementation costs and environmen- tal benefits through a multi-stage optimization process is shown in the figure 12. We show the posterior distributions of different parameters in the Bayesian inference and

<!-- b006846 | prose | pages [23] -->
微信号：MATHmodels

<!-- b006847 | prose | pages [23] -->
the convergence of the MCMC chain to visualize the reliability of the model and the estimation of the parameters in Figure 13.

<!-- b006848 | caption | pages [23] -->
Figure 12: Temporal Capacity Degradation

<!-- b006849 | prose | pages [23] -->
During Construction

<!-- b006850 | prose | pages [23] -->
9

<!-- b006851 | heading | pages [23] -->
Model Evaluation

<!-- b006852 | prose | pages [23] -->
9.1

<!-- b006853 | heading | pages [23] -->
Strengths

<!-- b006854 | caption | pages [23] -->
Figure 13: Posterior istributions of different

<!-- b006855 | prose | pages [23] -->
parameters

<!-- b006856 | prose | pages [23] -->
The model excels in providing a holistic analysis of post-disaster traffic resilience through an integrated network framework, balancing structural complexity with dy- namic traffic equilibrium principles. It incorporates multidimensional impacts—such as flow redistribution intensity , detour burden, and environmental externalities—via a fuzzy comprehensive evaluation model, ensuring systematic assessment of infras- tructure failure consequences. Enhanced predictive accuracy is achieved by integrat-

<!-- b006857 | prose | pages [23] -->
m

<!-- b006858 | prose | pages [23] -->
m

<!-- b006859 | prose | pages [23] -->
m

<!-- b006860 | prose | pages [23] -->
m

<!-- b006861 | prose | pages [23] -->
m

<!-- b006862 | prose | pages [23] -->
m

<!-- b006863 | prose | pages [23] -->
m

<!-- b006864 | prose | pages [23] -->
m

<!-- b006865 | prose | pages [23] -->
m

<!-- b006866 | prose | pages [23] -->
m

<!-- b006867 | prose | pages [23] -->
m

<!-- b006868 | prose | pages [23] -->
m

<!-- b006869 | prose | pages [23] -->
m

<!-- b006870 | prose | pages [23] -->
m

<!-- b006871 | prose | pages [23] -->
m

<!-- b006872 | prose | pages [23] -->
m

<!-- b006873 | prose | pages [23] -->
m

<!-- b006874 | prose | pages [23] -->
m

<!-- b006875 | prose | pages [23] -->
m

<!-- b006876 | prose | pages [23] -->
m

<!-- b006877 | prose | pages [23] -->
m

<!-- b006878 | prose | pages [23] -->
m

<!-- b006879 | prose | pages [23] -->
m

<!-- b006880 | prose | pages [23] -->
m

<!-- b006881 | prose | pages [23] -->
m

<!-- b006882 | prose | pages [23] -->
m

<!-- b006883 | prose | pages [23] -->
m

<!-- b006884 | prose | pages [23] -->
m

<!-- b006885 | prose | pages [23] -->
m

<!-- b006886 | prose | pages [23] -->
m

<!-- b006887 | prose | pages [23] -->
m

<!-- b006888 | prose | pages [23] -->
m

<!-- b006889 | prose | pages [23] -->
m

<!-- b006890 | prose | pages [23] -->
m

<!-- b006891 | prose | pages [23] -->
m

<!-- b006892 | prose | pages [23] -->
m

<!-- b006893 | prose | pages [23] -->
m

<!-- b006894 | prose | pages [23] -->
m

<!-- b006895 | prose | pages [23] -->
m

<!-- b006896 | prose | pages [23] -->
m

<!-- b006897 | prose | pages [23] -->
m

<!-- b006898 | prose | pages [23] -->
m

<!-- b006899 | prose | pages [23] -->
m

<!-- b006900 | prose | pages [23] -->
m

<!-- b006901 | prose | pages [23] -->
m

<!-- b006902 | prose | pages [23] -->
m

<!-- b006903 | prose | pages [23] -->
m

<!-- b006904 | prose | pages [23] -->
m

<!-- b006905 | prose | pages [23] -->
m

<!-- b006906 | prose | pages [23] -->
m

<!-- b006907 | prose | pages [23] -->
m

<!-- b006908 | prose | pages [23] -->
m

<!-- b006909 | prose | pages [23] -->
m

<!-- b006910 | prose | pages [23] -->
m

<!-- b006911 | prose | pages [23] -->
m

<!-- b006912 | prose | pages [23] -->
m

<!-- b006913 | prose | pages [23] -->
m

<!-- b006914 | prose | pages [23] -->
m

<!-- b006915 | prose | pages [23] -->
m

<!-- b006916 | prose | pages [23] -->
m

<!-- b006917 | prose | pages [23] -->
m

<!-- b006918 | prose | pages [23] -->
m

<!-- b006919 | prose | pages [23] -->
m

<!-- b006920 | prose | pages [23] -->
m

<!-- b006921 | prose | pages [23] -->
m

<!-- b006922 | prose | pages [23] -->
m

<!-- b006923 | prose | pages [23] -->
m

<!-- b006924 | prose | pages [23] -->
m

<!-- b006925 | prose | pages [23] -->
m

<!-- b006926 | prose | pages [23] -->
m

<!-- b006927 | prose | pages [23] -->
m

<!-- b006928 | prose | pages [23] -->
m

<!-- b006929 | prose | pages [23] -->
m

<!-- b006930 | prose | pages [23] -->
ing entropy-weighted aggregation and Wardrop equilibrium-based traffic assignment,

<!-- b006931 | prose | pages [23] -->
m

<!-- b006932 | prose | pages [23] -->
m

<!-- b006933 | prose | pages [23] -->
m

<!-- b006934 | prose | pages [23] -->
m

<!-- b006935 | prose | pages [23] -->
m

<!-- b006936 | prose | pages [23] -->
m

<!-- b006937 | prose | pages [23] -->
m

<!-- b006938 | prose | pages [23] -->
m

<!-- b006939 | prose | pages [23] -->
m

<!-- b006940 | prose | pages [23] -->
m

<!-- b006941 | prose | pages [23] -->
m

<!-- b006942 | prose | pages [23] -->
m

<!-- b006943 | prose | pages [23] -->
m

<!-- b006944 | prose | pages [23] -->
m

<!-- b006945 | prose | pages [23] -->
m

<!-- b006946 | prose | pages [23] -->
m

<!-- b006947 | prose | pages [23] -->
m

<!-- b006948 | prose | pages [23] -->
m

<!-- b006949 | prose | pages [23] -->
m

<!-- b006950 | prose | pages [23] -->
m

<!-- b006951 | prose | pages [23] -->
m

<!-- b006952 | prose | pages [23] -->
m

<!-- b006953 | prose | pages [23] -->
m

<!-- b006954 | prose | pages [23] -->
m

<!-- b006955 | prose | pages [23] -->
m

<!-- b006956 | prose | pages [23] -->
m

<!-- b006957 | prose | pages [23] -->
m

<!-- b006958 | prose | pages [23] -->
m

<!-- b006959 | prose | pages [23] -->
m

<!-- b006960 | prose | pages [23] -->
m

<!-- b006961 | prose | pages [23] -->
m

<!-- b006962 | prose | pages [23] -->
m

<!-- b006963 | prose | pages [23] -->
m

<!-- b006964 | prose | pages [23] -->
m

<!-- b006965 | prose | pages [23] -->
m

<!-- b006966 | prose | pages [23] -->
m

<!-- b006967 | prose | pages [23] -->
m

<!-- b006968 | prose | pages [23] -->
m

<!-- b006969 | prose | pages [23] -->
m

<!-- b006970 | prose | pages [23] -->
m

<!-- b006971 | prose | pages [23] -->
m

<!-- b006972 | prose | pages [23] -->
m

<!-- b006973 | prose | pages [23] -->
m

<!-- b006974 | prose | pages [23] -->
m

<!-- b006975 | prose | pages [23] -->
m

<!-- b006976 | prose | pages [23] -->
m

<!-- b006977 | prose | pages [23] -->
m

<!-- b006978 | prose | pages [23] -->
m

<!-- b006979 | prose | pages [23] -->
m

<!-- b006980 | prose | pages [23] -->
m

<!-- b006981 | prose | pages [23] -->
m

<!-- b006982 | prose | pages [23] -->
m

<!-- b006983 | prose | pages [23] -->
m

<!-- b006984 | prose | pages [23] -->
m

<!-- b006985 | prose | pages [23] -->
m

<!-- b006986 | prose | pages [23] -->
m

<!-- b006987 | prose | pages [23] -->
m

<!-- b006988 | prose | pages [23] -->
m

<!-- b006989 | prose | pages [23] -->
m

<!-- b006990 | prose | pages [23] -->
m

<!-- b006991 | prose | pages [23] -->
m

<!-- b006992 | prose | pages [23] -->
m

<!-- b006993 | prose | pages [23] -->
m

<!-- b006994 | prose | pages [23] -->
m

<!-- b006995 | prose | pages [23] -->
m

<!-- b006996 | prose | pages [23] -->
m

<!-- b006997 | prose | pages [23] -->
m

<!-- b006998 | prose | pages [23] -->
m

<!-- b006999 | prose | pages [23] -->
m

<!-- b007000 | prose | pages [23] -->
m

<!-- b007001 | prose | pages [23] -->
m

<!-- b007002 | prose | pages [23] -->
m

<!-- b007003 | prose | pages [23] -->
m

<!-- b007004 | prose | pages [23] -->
m

<!-- b007005 | prose | pages [23] -->
m

<!-- b007006 | prose | pages [23] -->
m

<!-- b007007 | prose | pages [23] -->
m

<!-- b007008 | prose | pages [23] -->
m

<!-- b007009 | prose | pages [23] -->
m

<!-- b007010 | prose | pages [23] -->
m

<!-- b007011 | prose | pages [23] -->
m

<!-- b007012 | prose | pages [23] -->
m

<!-- b007013 | prose | pages [23] -->
m

<!-- b007014 | prose | pages [23] -->
m

<!-- b007015 | prose | pages [23] -->
m

<!-- b007016 | prose | pages [23] -->
m

<!-- b007017 | prose | pages [23] -->
m

<!-- b007018 | prose | pages [23] -->
m

<!-- b007019 | prose | pages [23] -->
m

<!-- b007020 | prose | pages [23] -->
m

<!-- b007021 | prose | pages [23] -->
m

<!-- b007022 | prose | pages [23] -->
m

<!-- b007023 | prose | pages [23] -->
m

<!-- b007024 | prose | pages [23] -->
m

<!-- b007025 | prose | pages [23] -->
m

<!-- b007026 | prose | pages [23] -->
m

<!-- b007027 | prose | pages [23] -->
m

<!-- b007028 | prose | pages [23] -->
m

<!-- b007029 | prose | pages [23] -->
m

<!-- b007030 | prose | pages [23] -->
m

<!-- b007031 | prose | pages [23] -->
m

<!-- b007032 | prose | pages [23] -->
m

<!-- b007033 | prose | pages [23] -->
m

<!-- b007034 | prose | pages [23] -->
m

<!-- b007035 | prose | pages [23] -->
m

<!-- b007036 | prose | pages [23] -->
m

<!-- b007037 | prose | pages [23] -->
m

<!-- b007038 | prose | pages [23] -->
m

<!-- b007039 | prose | pages [23] -->
m

<!-- b007040 | prose | pages [23] -->
m

<!-- b007041 | prose | pages [23] -->
m

<!-- b007042 | prose | pages [23] -->
m

<!-- b007043 | prose | pages [23] -->
m

<!-- b007044 | prose | pages [23] -->
m

<!-- b007045 | prose | pages [23] -->
m

<!-- b007046 | prose | pages [23] -->
m

<!-- b007047 | prose | pages [23] -->
m

<!-- b007048 | prose | pages [23] -->
m

<!-- b007049 | prose | pages [23] -->
m

<!-- b007050 | prose | pages [23] -->
m

<!-- b007051 | prose | pages [23] -->
m

<!-- b007052 | prose | pages [23] -->
m

<!-- b007053 | prose | pages [23] -->
m

<!-- b007054 | prose | pages [23] -->
m

<!-- b007055 | prose | pages [23] -->
m

<!-- b007056 | prose | pages [23] -->
m

<!-- b007057 | prose | pages [23] -->
m

<!-- b007058 | prose | pages [23] -->
m

<!-- b007059 | prose | pages [23] -->
m

<!-- b007060 | prose | pages [23] -->
m

<!-- b007061 | prose | pages [23] -->
m

<!-- b007062 | prose | pages [23] -->
m

<!-- b007063 | prose | pages [23] -->
m

<!-- b007064 | prose | pages [23] -->
m

<!-- b007065 | prose | pages [23] -->
m

<!-- b007066 | prose | pages [23] -->
m

<!-- b007067 | prose | pages [23] -->
m

<!-- b007068 | prose | pages [23] -->
m

<!-- b007069 | prose | pages [23] -->
m

<!-- b007070 | prose | pages [23] -->
m

<!-- b007071 | prose | pages [23] -->
m

<!-- b007072 | prose | pages [23] -->
m

<!-- b007073 | prose | pages [23] -->
m

<!-- b007074 | prose | pages [23] -->
m

<!-- b007075 | prose | pages [23] -->
m

<!-- b007076 | prose | pages [23] -->
m

<!-- b007077 | prose | pages [23] -->
m

<!-- b007078 | prose | pages [23] -->
m

<!-- b007079 | prose | pages [23] -->
m

<!-- b007080 | prose | pages [23] -->
m

<!-- b007081 | prose | pages [23] -->
m

<!-- b007082 | prose | pages [23] -->
m

<!-- b007083 | prose | pages [23] -->
m

<!-- b007084 | prose | pages [23] -->
m

<!-- b007085 | prose | pages [23] -->
m

<!-- b007086 | prose | pages [23] -->
m

<!-- b007087 | prose | pages [23] -->
m

<!-- b007088 | prose | pages [23] -->
m

<!-- b007089 | prose | pages [23] -->
validated against empirical data.

<!-- b007090 | prose | pages [23] -->
m

<!-- b007091 | prose | pages [23] -->
m

<!-- b007092 | prose | pages [23] -->
m

<!-- b007093 | prose | pages [23] -->
m

<!-- b007094 | prose | pages [23] -->
m

<!-- b007095 | prose | pages [23] -->
m

<!-- b007096 | prose | pages [23] -->
m

<!-- b007097 | prose | pages [23] -->
m

<!-- b007098 | prose | pages [23] -->
m

<!-- b007099 | prose | pages [23] -->
m

<!-- b007100 | prose | pages [23] -->
m

<!-- b007101 | prose | pages [23] -->
m

<!-- b007102 | prose | pages [23] -->
m

<!-- b007103 | prose | pages [23] -->
m

<!-- b007104 | prose | pages [23] -->
m

<!-- b007105 | prose | pages [23] -->
m

<!-- b007106 | prose | pages [23] -->
m

<!-- b007107 | prose | pages [23] -->
m

<!-- b007108 | prose | pages [23] -->
m

<!-- b007109 | prose | pages [23] -->
m

<!-- b007110 | prose | pages [23] -->
m

<!-- b007111 | prose | pages [23] -->
m

<!-- b007112 | prose | pages [23] -->
m

<!-- b007113 | prose | pages [23] -->
m

<!-- b007114 | prose | pages [23] -->
m

<!-- b007115 | prose | pages [23] -->
m

<!-- b007116 | prose | pages [23] -->
m

<!-- b007117 | prose | pages [23] -->
m

<!-- b007118 | prose | pages [23] -->
m

<!-- b007119 | prose | pages [23] -->
m

<!-- b007120 | prose | pages [23] -->
m

<!-- b007121 | prose | pages [23] -->
m

<!-- b007122 | prose | pages [23] -->
m

<!-- b007123 | prose | pages [23] -->
m

<!-- b007124 | prose | pages [23] -->
m

<!-- b007125 | prose | pages [23] -->
m

<!-- b007126 | prose | pages [23] -->
m

<!-- b007127 | prose | pages [23] -->
m

<!-- b007128 | prose | pages [23] -->
m

<!-- b007129 | prose | pages [23] -->
m

<!-- b007130 | prose | pages [23] -->
m

<!-- b007131 | prose | pages [23] -->
m

<!-- b007132 | prose | pages [23] -->
m

<!-- b007133 | prose | pages [23] -->
m

<!-- b007134 | prose | pages [23] -->
m

<!-- b007135 | prose | pages [23] -->
m

<!-- b007136 | prose | pages [23] -->
m

<!-- b007137 | prose | pages [23] -->
m

<!-- b007138 | prose | pages [23] -->
m

<!-- b007139 | prose | pages [23] -->
m

<!-- b007140 | prose | pages [23] -->
m

<!-- b007141 | prose | pages [23] -->
m

<!-- b007142 | prose | pages [23] -->
m

<!-- b007143 | furniture | pages [23] -->
m

<!-- b007144 | furniture | pages [23] -->
m

<!-- b007145 | furniture | pages [23] -->
m

<!-- b007146 | furniture | pages [23] -->
m

<!-- b007147 | furniture | pages [23] -->
m

<!-- b007148 | furniture | pages [23] -->
m

<!-- b007149 | furniture | pages [23] -->
m

<!-- b007150 | furniture | pages [23] -->
m

<!-- b007151 | furniture | pages [23] -->
m

<!-- b007152 | furniture | pages [23] -->
m

<!-- b007153 | furniture | pages [23] -->
m

<!-- b007154 | furniture | pages [23] -->
m

<!-- b007155 | furniture | pages [23] -->
m

<!-- b007156 | furniture | pages [23] -->
m

<!-- b007157 | furniture | pages [23] -->
m

<!-- b007158 | furniture | pages [23] -->
m

<!-- b007159 | furniture | pages [23] -->
m

<!-- b007160 | furniture | pages [23] -->
m

<!-- b007161 | furniture | pages [23] -->
m

<!-- b007162 | furniture | pages [23] -->
m

<!-- b007163 | furniture | pages [23] -->
m

<!-- b007164 | furniture | pages [23] -->
m

<!-- b007165 | furniture | pages [23] -->
m

<!-- b007166 | furniture | pages [23] -->
m

<!-- b007167 | furniture | pages [23] -->
m

<!-- b007168 | furniture | pages [23] -->
m

<!-- b007169 | furniture | pages [23] -->
m

<!-- b007170 | furniture | pages [23] -->
m

<!-- b007171 | furniture | pages [23] -->
m

<!-- b007172 | furniture | pages [23] -->
m

<!-- b007173 | furniture | pages [23] -->
m

<!-- b007174 | furniture | pages [23] -->
m

<!-- b007175 | furniture | pages [23] -->
m

<!-- b007176 | furniture | pages [23] -->
m

<!-- b007177 | furniture | pages [23] -->
m

<!-- b007178 | furniture | pages [23] -->
m

<!-- b007179 | furniture | pages [23] -->
m

<!-- b007180 | furniture | pages [23] -->
m

<!-- b007181 | furniture | pages [23] -->
m

<!-- b007182 | furniture | pages [23] -->
m

<!-- b007183 | furniture | pages [23] -->
m

<!-- b007184 | furniture | pages [23] -->
m

<!-- b007185 | furniture | pages [23] -->
m

<!-- b007186 | furniture | pages [23] -->
m

<!-- b007187 | furniture | pages [23] -->
m

<!-- b007188 | furniture | pages [23] -->
m

<!-- b007189 | furniture | pages [23] -->
m

<!-- b007190 | furniture | pages [23] -->
m

<!-- b007191 | furniture | pages [23] -->
m

<!-- b007192 | furniture | pages [23] -->
m

<!-- b007193 | furniture | pages [23] -->
m

<!-- b007194 | furniture | pages [23] -->
m

<!-- b007195 | furniture | pages [23] -->
m

<!-- b007196 | furniture | pages [23] -->
m

<!-- b007197 | furniture | pages [23] -->
m

<!-- b007198 | furniture | pages [23] -->
m

<!-- b007199 | furniture | pages [23] -->
m

<!-- b007200 | furniture | pages [23] -->
m

<!-- b007201 | furniture | pages [23] -->
m

<!-- b007202 | furniture | pages [23] -->
m

<!-- b007203 | furniture | pages [23] -->
m

<!-- b007204 | furniture | pages [23] -->
m

<!-- b007205 | furniture | pages [23] -->
m

<!-- b007206 | furniture | pages [23] -->
m

<!-- b007207 | furniture | pages [23] -->
m

<!-- b007208 | furniture | pages [23] -->
m

<!-- b007209 | furniture | pages [23] -->
m

<!-- b007210 | furniture | pages [23] -->
m

<!-- b007211 | furniture | pages [23] -->
m

<!-- b007212 | furniture | pages [23] -->
m

<!-- b007213 | furniture | pages [23] -->
m

<!-- b007214 | furniture | pages [23] -->
m

<!-- b007215 | furniture | pages [23] -->
m

<!-- b007216 | furniture | pages [23] -->
m

<!-- b007217 | furniture | pages [23] -->
m

<!-- b007218 | furniture | pages [23] -->
m

<!-- b007219 | furniture | pages [23] -->
m

<!-- b007220 | furniture | pages [23] -->
m

<!-- b007221 | furniture | pages [23] -->
m

<!-- b007222 | furniture | pages [23] -->
m

<!-- b007223 | furniture | pages [23] -->
m

<!-- b007224 | furniture | pages [23] -->
m

<!-- b007225 | furniture | pages [23] -->
m

<!-- b007226 | furniture | pages [23] -->
m

<!-- b007227 | furniture | pages [23] -->
m

<!-- b007228 | furniture | pages [23] -->
m

<!-- b007229 | furniture | pages [23] -->
m

<!-- b007230 | furniture | pages [23] -->
m

<!-- b007231 | furniture | pages [23] -->
m

<!-- b007232 | furniture | pages [23] -->
m

<!-- b007233 | furniture | pages [23] -->
m

<!-- b007234 | furniture | pages [23] -->
m

<!-- b007235 | furniture | pages [23] -->
m

<!-- b007236 | furniture | pages [23] -->
m

<!-- b007237 | furniture | pages [23] -->
m

<!-- b007238 | furniture | pages [23] -->
m

<!-- b007239 | furniture | pages [23] -->
m

<!-- b007240 | furniture | pages [23] -->
m

<!-- b007241 | furniture | pages [23] -->
m

<!-- b007242 | furniture | pages [23] -->
m

<!-- b007243 | furniture | pages [23] -->
m

<!-- b007244 | furniture | pages [23] -->
m

<!-- b007245 | furniture | pages [23] -->
m

<!-- b007246 | furniture | pages [23] -->
m

<!-- b007247 | furniture | pages [23] -->
m

<!-- b007248 | furniture | pages [23] -->
m

<!-- b007249 | furniture | pages [23] -->
m

<!-- b007250 | furniture | pages [23] -->
m

<!-- b007251 | furniture | pages [23] -->
m

<!-- b007252 | furniture | pages [23] -->
m

<!-- b007253 | furniture | pages [23] -->
m

<!-- b007254 | furniture | pages [23] -->
m

<!-- b007255 | furniture | pages [23] -->
m

<!-- b007256 | furniture | pages [23] -->
m

<!-- b007257 | furniture | pages [23] -->
m

<!-- b007258 | furniture | pages [23] -->
m

<!-- b007259 | furniture | pages [23] -->
m

<!-- b007260 | furniture | pages [23] -->
m

<!-- b007261 | furniture | pages [23] -->
m

<!-- b007262 | furniture | pages [23] -->
m

<!-- b007263 | furniture | pages [23] -->
m

<!-- b007264 | furniture | pages [23] -->
m

<!-- b007265 | furniture | pages [23] -->
m

<!-- b007266 | furniture | pages [23] -->
m

<!-- b007267 | furniture | pages [23] -->
m

<!-- b007268 | furniture | pages [23] -->
m

<!-- b007269 | furniture | pages [23] -->
m

<!-- b007270 | furniture | pages [23] -->
m

<!-- b007271 | furniture | pages [23] -->
m

<!-- b007272 | furniture | pages [23] -->
m

<!-- b007273 | furniture | pages [23] -->
m

<!-- b007274 | furniture | pages [23] -->
m

<!-- b007275 | furniture | pages [23] -->
m

<!-- b007276 | furniture | pages [23] -->
m

<!-- b007277 | furniture | pages [23] -->
m

<!-- b007278 | furniture | pages [23] -->
m

<!-- b007279 | furniture | pages [23] -->
m

<!-- b007280 | furniture | pages [23] -->
m

<!-- b007281 | furniture | pages [23] -->
m

<!-- b007282 | furniture | pages [23] -->
m

<!-- b007283 | furniture | pages [23] -->
m

<!-- b007284 | furniture | pages [23] -->
m

<!-- b007285 | furniture | pages [23] -->
m

<!-- b007286 | furniture | pages [23] -->
m

<!-- b007287 | furniture | pages [23] -->
m

<!-- b007288 | furniture | pages [23] -->
m

<!-- b007289 | furniture | pages [23] -->
m

<!-- b007290 | furniture | pages [23] -->
m

<!-- b007291 | furniture | pages [23] -->
m

<!-- b007292 | furniture | pages [23] -->
m

<!-- b007293 | furniture | pages [23] -->
m

<!-- b007294 | furniture | pages [23] -->
m

<!-- b007295 | furniture | pages [23] -->
m

<!-- b007296 | furniture | pages [23] -->
m

<!-- b007297 | furniture | pages [23] -->
m

<!-- b007298 | furniture | pages [23] -->
m

<!-- b007299 | furniture | pages [23] -->
m

<!-- b007300 | furniture | pages [23] -->
m

<!-- b007301 | furniture | pages [23] -->
m

<!-- b007302 | furniture | pages [23] -->
m

<!-- b007303 | furniture | pages [23] -->
m

<!-- b007304 | furniture | pages [23] -->
m

<!-- b007305 | furniture | pages [23] -->
m

<!-- b007306 | furniture | pages [23] -->
m

<!-- b007307 | furniture | pages [23] -->
m

<!-- b007308 | furniture | pages [23] -->
m

<!-- b007309 | furniture | pages [23] -->
m

<!-- b007310 | furniture | pages [23] -->
m

<!-- b007311 | furniture | pages [23] -->
m

<!-- b007312 | furniture | pages [23] -->
m

<!-- b007313 | furniture | pages [23] -->
m

<!-- b007314 | furniture | pages [23] -->
m

<!-- b007315 | furniture | pages [23] -->
m

<!-- b007316 | furniture | pages [23] -->
m

<!-- b007317 | furniture | pages [23] -->
m

<!-- b007318 | furniture | pages [23] -->
m

<!-- b007319 | furniture | pages [23] -->
m

<!-- b007320 | furniture | pages [23] -->
m

<!-- b007321 | furniture | pages [23] -->
m

<!-- b007322 | furniture | pages [23] -->
m

<!-- b007323 | furniture | pages [23] -->
m

<!-- b007324 | furniture | pages [23] -->
m

<!-- b007325 | furniture | pages [23] -->
m

<!-- b007326 | furniture | pages [23] -->
m

<!-- b007327 | furniture | pages [23] -->
m

<!-- b007328 | furniture | pages [23] -->
m

<!-- b007329 | furniture | pages [23] -->
m

<!-- b007330 | furniture | pages [23] -->
m

<!-- b007331 | furniture | pages [23] -->
m

<!-- b007332 | furniture | pages [23] -->
m

<!-- b007333 | furniture | pages [23] -->
m

<!-- b007334 | furniture | pages [23] -->
m

<!-- b007335 | furniture | pages [23] -->
m

<!-- b007336 | furniture | pages [23] -->
m

<!-- b007337 | furniture | pages [23] -->
m

<!-- b007338 | furniture | pages [23] -->
m

<!-- b007339 | furniture | pages [23] -->
m

<!-- b007340 | furniture | pages [23] -->
m

<!-- b007341 | furniture | pages [23] -->
m

<!-- b007342 | furniture | pages [23] -->
m

<!-- b007343 | furniture | pages [23] -->
m

<!-- b007344 | furniture | pages [23] -->
m

<!-- b007345 | furniture | pages [23] -->
m

<!-- b007346 | furniture | pages [23] -->
m

<!-- b007347 | furniture | pages [23] -->
m

<!-- b007348 | furniture | pages [23] -->
m

<!-- b007349 | furniture | pages [23] -->
m

<!-- b007350 | furniture | pages [23] -->
m

<!-- b007351 | furniture | pages [23] -->
m

<!-- b007352 | furniture | pages [23] -->
m

<!-- b007353 | furniture | pages [23] -->
m

<!-- b007354 | furniture | pages [23] -->
m

<!-- b007355 | furniture | pages [23] -->
m

<!-- b007356 | furniture | pages [23] -->
m

<!-- b007357 | furniture | pages [23] -->
m

<!-- b007358 | furniture | pages [23] -->
m

<!-- b007359 | furniture | pages [23] -->
m

<!-- b007360 | furniture | pages [23] -->
m

<!-- b007361 | furniture | pages [23] -->
m

<!-- b007362 | furniture | pages [23] -->
m

<!-- b007363 | furniture | pages [23] -->
m

<!-- b007364 | furniture | pages [23] -->
m

<!-- b007365 | furniture | pages [23] -->
m

<!-- b007366 | furniture | pages [23] -->
m

<!-- b007367 | furniture | pages [23] -->
m

<!-- b007368 | furniture | pages [23] -->
m

<!-- b007369 | furniture | pages [23] -->
m

<!-- b007370 | furniture | pages [23] -->
m

<!-- b007371 | furniture | pages [23] -->
m

<!-- b007372 | furniture | pages [23] -->
m

<!-- b007373 | furniture | pages [23] -->
m

<!-- b007374 | furniture | pages [23] -->
m

<!-- b007375 | furniture | pages [23] -->
m

<!-- b007376 | furniture | pages [23] -->
m

<!-- b007377 | furniture | pages [23] -->
m

<!-- b007378 | furniture | pages [23] -->
m

<!-- b007379 | furniture | pages [23] -->
m

<!-- b007380 | furniture | pages [23] -->
m

<!-- b007381 | furniture | pages [23] -->
m

<!-- b007382 | furniture | pages [23] -->
m

<!-- b007383 | furniture | pages [23] -->
m

<!-- b007384 | furniture | pages [23] -->
m

<!-- b007385 | furniture | pages [23] -->
m

<!-- b007386 | furniture | pages [23] -->
m

<!-- b007387 | furniture | pages [23] -->
m

<!-- b007388 | furniture | pages [23] -->
m

<!-- b007389 | furniture | pages [23] -->
m

<!-- b007390 | furniture | pages [23] -->
m

<!-- b007391 | furniture | pages [23] -->
m

<!-- b007392 | furniture | pages [23] -->
m

<!-- b007393 | furniture | pages [23] -->
m

<!-- b007394 | furniture | pages [23] -->
m

<!-- b007395 | furniture | pages [23] -->
m

<!-- b007396 | furniture | pages [23] -->
m

<!-- b007397 | furniture | pages [23] -->
m

<!-- b007398 | furniture | pages [23] -->
m

<!-- b007399 | furniture | pages [23] -->
m

<!-- b007400 | furniture | pages [23] -->
m

<!-- b007401 | furniture | pages [23] -->
m

<!-- b007402 | furniture | pages [23] -->
m

<!-- b007403 | furniture | pages [23] -->
m

<!-- b007404 | furniture | pages [23] -->
m

<!-- b007405 | furniture | pages [23] -->
m

<!-- b007406 | furniture | pages [23] -->
m

<!-- b007407 | furniture | pages [23] -->
m

<!-- b007408 | furniture | pages [23] -->
m

<!-- b007409 | furniture | pages [23] -->
m

<!-- b007410 | furniture | pages [23] -->
m

<!-- b007411 | furniture | pages [23] -->
m

<!-- b007412 | furniture | pages [23] -->
m

<!-- b007413 | furniture | pages [23] -->
m

<!-- b007414 | furniture | pages [23] -->
m

<!-- b007415 | furniture | pages [23] -->
m

<!-- b007416 | furniture | pages [23] -->
m

<!-- b007417 | furniture | pages [23] -->
m

<!-- b007418 | furniture | pages [23] -->
m

<!-- b007419 | furniture | pages [23] -->
m

<!-- b007420 | furniture | pages [23] -->
m

<!-- b007421 | furniture | pages [23] -->
m

<!-- b007422 | furniture | pages [23] -->
m

<!-- b007423 | furniture | pages [23] -->
m

<!-- b007424 | furniture | pages [23] -->
m

<!-- b007425 | furniture | pages [23] -->
m

<!-- b007426 | furniture | pages [23] -->
m

<!-- b007427 | furniture | pages [23] -->
m

<!-- b007428 | furniture | pages [23] -->
m

<!-- b007429 | furniture | pages [23] -->
m

<!-- b007430 | furniture | pages [23] -->
m

<!-- b007431 | furniture | pages [23] -->
m

<!-- b007432 | furniture | pages [23] -->
m

<!-- b007433 | furniture | pages [23] -->
m

<!-- b007434 | furniture | pages [23] -->
m

<!-- b007435 | furniture | pages [23] -->
m

<!-- b007436 | furniture | pages [23] -->
m

<!-- b007437 | furniture | pages [23] -->
m

<!-- b007438 | furniture | pages [23] -->
m

<!-- b007439 | furniture | pages [23] -->
m

<!-- b007440 | furniture | pages [23] -->
m

<!-- b007441 | furniture | pages [23] -->
m

<!-- b007442 | furniture | pages [23] -->
m

<!-- b007443 | furniture | pages [23] -->
m

<!-- b007444 | furniture | pages [23] -->
m

<!-- b007445 | furniture | pages [23] -->
m

<!-- b007446 | furniture | pages [23] -->
m

<!-- b007447 | furniture | pages [23] -->
m

<!-- b007448 | furniture | pages [23] -->
m

<!-- b007449 | furniture | pages [23] -->
m

<!-- b007450 | furniture | pages [23] -->
m

<!-- b007451 | furniture | pages [23] -->
m

<!-- b007452 | furniture | pages [23] -->
m

<!-- b007453 | furniture | pages [23] -->
m

<!-- b007454 | furniture | pages [23] -->
m

<!-- b007455 | furniture | pages [23] -->
m

<!-- b007456 | furniture | pages [23] -->
m

<!-- b007457 | furniture | pages [23] -->
m

<!-- b007458 | furniture | pages [23] -->
m

<!-- b007459 | furniture | pages [23] -->
m

<!-- b007460 | furniture | pages [23] -->
m

<!-- b007461 | furniture | pages [23] -->
m

<!-- b007462 | furniture | pages [23] -->
m

<!-- b007463 | furniture | pages [23] -->
m

<!-- b007464 | furniture | pages [23] -->
m

<!-- b007465 | furniture | pages [23] -->
m

<!-- b007466 | furniture | pages [23] -->
m

<!-- b007467 | furniture | pages [23] -->
m

<!-- b007468 | furniture | pages [23] -->
m

<!-- b007469 | furniture | pages [23] -->
m

<!-- b007470 | furniture | pages [23] -->
m

<!-- b007471 | furniture | pages [23] -->
m

<!-- b007472 | furniture | pages [23] -->
m

<!-- b007473 | furniture | pages [23] -->
m

<!-- b007474 | furniture | pages [23] -->
m

<!-- b007475 | furniture | pages [23] -->
m

<!-- b007476 | furniture | pages [23] -->
m

<!-- b007477 | furniture | pages [23] -->
m

<!-- b007478 | furniture | pages [23] -->
m

<!-- b007479 | furniture | pages [23] -->
m

<!-- b007480 | furniture | pages [23] -->
m

<!-- b007481 | furniture | pages [23] -->
m

<!-- b007482 | furniture | pages [23] -->
m

<!-- b007483 | furniture | pages [23] -->
m

<!-- b007484 | furniture | pages [23] -->
m

<!-- b007485 | furniture | pages [23] -->
m

<!-- b007486 | furniture | pages [23] -->
m

<!-- b007487 | furniture | pages [23] -->
m

<!-- b007488 | furniture | pages [23] -->
m

<!-- b007489 | furniture | pages [23] -->
m

<!-- b007490 | furniture | pages [23] -->
m

<!-- b007491 | furniture | pages [23] -->
m

<!-- b007492 | furniture | pages [23] -->
m

<!-- b007493 | furniture | pages [23] -->
m

<!-- b007494 | furniture | pages [23] -->
m

<!-- b007495 | furniture | pages [23] -->
m

<!-- b007496 | furniture | pages [23] -->
m

<!-- b007497 | furniture | pages [23] -->
m

<!-- b007498 | furniture | pages [23] -->
m

<!-- b007499 | furniture | pages [23] -->
m

<!-- b007500 | furniture | pages [23] -->
m

<!-- b007501 | furniture | pages [23] -->
m

<!-- b007502 | furniture | pages [23] -->
m

<!-- b007503 | furniture | pages [23] -->
m

<!-- b007504 | furniture | pages [23] -->
m

<!-- b007505 | furniture | pages [23] -->
m

<!-- b007506 | furniture | pages [23] -->
m

<!-- b007507 | furniture | pages [23] -->
m

<!-- b007508 | furniture | pages [23] -->
m

<!-- b007509 | furniture | pages [23] -->
m

<!-- b007510 | furniture | pages [23] -->
m

<!-- b007511 | furniture | pages [23] -->
m

<!-- b007512 | furniture | pages [23] -->
m

<!-- b007513 | furniture | pages [23] -->
m

<!-- b007514 | furniture | pages [23] -->
m

<!-- b007515 | furniture | pages [23] -->
m

<!-- b007516 | furniture | pages [23] -->
m

<!-- b007517 | furniture | pages [23] -->
m

<!-- b007518 | furniture | pages [23] -->
m

<!-- b007519 | furniture | pages [23] -->
m

<!-- b007520 | furniture | pages [23] -->
m

<!-- b007521 | furniture | pages [23] -->
m

<!-- b007522 | furniture | pages [23] -->
m

<!-- b007523 | furniture | pages [23] -->
m

<!-- b007524 | furniture | pages [23] -->
m

<!-- b007525 | furniture | pages [23] -->
m

<!-- b007526 | furniture | pages [23] -->
m

<!-- b007527 | furniture | pages [23] -->
m

<!-- b007528 | furniture | pages [23] -->
m

<!-- b007529 | furniture | pages [23] -->
m

<!-- b007530 | furniture | pages [23] -->
m

<!-- b007531 | furniture | pages [23] -->
m

<!-- b007532 | furniture | pages [23] -->
m

<!-- b007533 | furniture | pages [23] -->
m

<!-- b007534 | furniture | pages [23] -->
m

<!-- b007535 | furniture | pages [23] -->
m

<!-- b007536 | furniture | pages [23] -->
m

<!-- b007537 | furniture | pages [23] -->
m

<!-- b007538 | furniture | pages [23] -->
m

<!-- b007539 | furniture | pages [23] -->
m

<!-- b007540 | furniture | pages [23] -->
m

<!-- b007541 | furniture | pages [23] -->
m

<!-- b007542 | furniture | pages [23] -->
m

<!-- b007543 | furniture | pages [23] -->
m

<!-- b007544 | furniture | pages [23] -->
m

<!-- b007545 | furniture | pages [23] -->
m

<!-- b007546 | furniture | pages [24] -->
Team # 2516219

<!-- b007547 | prose | pages [24] -->
9.2

<!-- b007548 | heading | pages [24] -->
Weakness

<!-- b007549 | furniture | pages [24] -->
Page 24 of 24

<!-- b007550 | prose | pages [24] -->
The model’s representation of Baltimore’s transportation network as static nodes and edges overlooks time-varying congestion patterns and seasonal traffic fluctua- tions, potentially affecting real-time response accuracy. It excludes granular behav- ioral factors, such as heterogeneous commuter preferences and socioeconomic dispari- ties in travel choices, Stakeholder satisfaction metrics, based on linear utility functions

<!-- b007551 | prose | pages [24] -->
m

<!-- b007552 | prose | pages [24] -->
m

<!-- b007553 | prose | pages [24] -->
m

<!-- b007554 | prose | pages [24] -->
m

<!-- b007555 | prose | pages [24] -->
m

<!-- b007556 | prose | pages [24] -->
m

<!-- b007557 | prose | pages [24] -->
m

<!-- b007558 | prose | pages [24] -->
m

<!-- b007559 | prose | pages [24] -->
m

<!-- b007560 | prose | pages [24] -->
m

<!-- b007561 | prose | pages [24] -->
m

<!-- b007562 | prose | pages [24] -->
m

<!-- b007563 | prose | pages [24] -->
m

<!-- b007564 | prose | pages [24] -->
m

<!-- b007565 | prose | pages [24] -->
m

<!-- b007566 | prose | pages [24] -->
m

<!-- b007567 | prose | pages [24] -->
m

<!-- b007568 | prose | pages [24] -->
m

<!-- b007569 | prose | pages [24] -->
m

<!-- b007570 | prose | pages [24] -->
m

<!-- b007571 | prose | pages [24] -->
m

<!-- b007572 | prose | pages [24] -->
m

<!-- b007573 | prose | pages [24] -->
m

<!-- b007574 | prose | pages [24] -->
m

<!-- b007575 | prose | pages [24] -->
m

<!-- b007576 | prose | pages [24] -->
m

<!-- b007577 | prose | pages [24] -->
m

<!-- b007578 | prose | pages [24] -->
m

<!-- b007579 | prose | pages [24] -->
m

<!-- b007580 | prose | pages [24] -->
m

<!-- b007581 | prose | pages [24] -->
m

<!-- b007582 | prose | pages [24] -->
m

<!-- b007583 | prose | pages [24] -->
m

<!-- b007584 | prose | pages [24] -->
m

<!-- b007585 | prose | pages [24] -->
m

<!-- b007586 | prose | pages [24] -->
m

<!-- b007587 | prose | pages [24] -->
m

<!-- b007588 | prose | pages [24] -->
m

<!-- b007589 | prose | pages [24] -->
m

<!-- b007590 | prose | pages [24] -->
m

<!-- b007591 | prose | pages [24] -->
m

<!-- b007592 | prose | pages [24] -->
m

<!-- b007593 | prose | pages [24] -->
m

<!-- b007594 | prose | pages [24] -->
m

<!-- b007595 | prose | pages [24] -->
m

<!-- b007596 | prose | pages [24] -->
m

<!-- b007597 | prose | pages [24] -->
m

<!-- b007598 | prose | pages [24] -->
m

<!-- b007599 | prose | pages [24] -->
m

<!-- b007600 | prose | pages [24] -->
m

<!-- b007601 | prose | pages [24] -->
m

<!-- b007602 | prose | pages [24] -->
m

<!-- b007603 | prose | pages [24] -->
m

<!-- b007604 | prose | pages [24] -->
and deterministic mode-shift probabilities, may not fully capture nonlinear decision-

<!-- b007605 | prose | pages [24] -->
m

<!-- b007606 | prose | pages [24] -->
m

<!-- b007607 | prose | pages [24] -->
m

<!-- b007608 | prose | pages [24] -->
m

<!-- b007609 | prose | pages [24] -->
m

<!-- b007610 | prose | pages [24] -->
m

<!-- b007611 | prose | pages [24] -->
m

<!-- b007612 | prose | pages [24] -->
m

<!-- b007613 | prose | pages [24] -->
m

<!-- b007614 | prose | pages [24] -->
m

<!-- b007615 | prose | pages [24] -->
m

<!-- b007616 | prose | pages [24] -->
m

<!-- b007617 | prose | pages [24] -->
m

<!-- b007618 | prose | pages [24] -->
m

<!-- b007619 | prose | pages [24] -->
m

<!-- b007620 | prose | pages [24] -->
m

<!-- b007621 | prose | pages [24] -->
m

<!-- b007622 | prose | pages [24] -->
m

<!-- b007623 | prose | pages [24] -->
m

<!-- b007624 | prose | pages [24] -->
m

<!-- b007625 | prose | pages [24] -->
m

<!-- b007626 | prose | pages [24] -->
m

<!-- b007627 | prose | pages [24] -->
m

<!-- b007628 | prose | pages [24] -->
m

<!-- b007629 | prose | pages [24] -->
m

<!-- b007630 | prose | pages [24] -->
m

<!-- b007631 | prose | pages [24] -->
m

<!-- b007632 | prose | pages [24] -->
m

<!-- b007633 | prose | pages [24] -->
m

<!-- b007634 | prose | pages [24] -->
m

<!-- b007635 | prose | pages [24] -->
m

<!-- b007636 | prose | pages [24] -->
m

<!-- b007637 | prose | pages [24] -->
m

<!-- b007638 | prose | pages [24] -->
m

<!-- b007639 | prose | pages [24] -->
m

<!-- b007640 | prose | pages [24] -->
m

<!-- b007641 | prose | pages [24] -->
m

<!-- b007642 | prose | pages [24] -->
m

<!-- b007643 | prose | pages [24] -->
m

<!-- b007644 | prose | pages [24] -->
m

<!-- b007645 | prose | pages [24] -->
m

<!-- b007646 | prose | pages [24] -->
m

<!-- b007647 | prose | pages [24] -->
m

<!-- b007648 | prose | pages [24] -->
m

<!-- b007649 | prose | pages [24] -->
m

<!-- b007650 | prose | pages [24] -->
m

<!-- b007651 | prose | pages [24] -->
m

<!-- b007652 | prose | pages [24] -->
m

<!-- b007653 | prose | pages [24] -->
m

<!-- b007654 | prose | pages [24] -->
m

<!-- b007655 | prose | pages [24] -->
m

<!-- b007656 | prose | pages [24] -->
m

<!-- b007657 | prose | pages [24] -->
m

<!-- b007658 | prose | pages [24] -->
m

<!-- b007659 | prose | pages [24] -->
m

<!-- b007660 | prose | pages [24] -->
m

<!-- b007661 | prose | pages [24] -->
m

<!-- b007662 | prose | pages [24] -->
m

<!-- b007663 | prose | pages [24] -->
m

<!-- b007664 | prose | pages [24] -->
m

<!-- b007665 | prose | pages [24] -->
m

<!-- b007666 | prose | pages [24] -->
m

<!-- b007667 | prose | pages [24] -->
m

<!-- b007668 | prose | pages [24] -->
m

<!-- b007669 | prose | pages [24] -->
m

<!-- b007670 | prose | pages [24] -->
m

<!-- b007671 | prose | pages [24] -->
m

<!-- b007672 | prose | pages [24] -->
m

<!-- b007673 | prose | pages [24] -->
m

<!-- b007674 | prose | pages [24] -->
m

<!-- b007675 | prose | pages [24] -->
m

<!-- b007676 | prose | pages [24] -->
m

<!-- b007677 | prose | pages [24] -->
m

<!-- b007678 | prose | pages [24] -->
m

<!-- b007679 | prose | pages [24] -->
m

<!-- b007680 | prose | pages [24] -->
m

<!-- b007681 | prose | pages [24] -->
m

<!-- b007682 | prose | pages [24] -->
m

<!-- b007683 | prose | pages [24] -->
m

<!-- b007684 | prose | pages [24] -->
m

<!-- b007685 | prose | pages [24] -->
m

<!-- b007686 | prose | pages [24] -->
m

<!-- b007687 | prose | pages [24] -->
m

<!-- b007688 | prose | pages [24] -->
m

<!-- b007689 | prose | pages [24] -->
m

<!-- b007690 | prose | pages [24] -->
m

<!-- b007691 | prose | pages [24] -->
m

<!-- b007692 | prose | pages [24] -->
m

<!-- b007693 | prose | pages [24] -->
m

<!-- b007694 | prose | pages [24] -->
m

<!-- b007695 | prose | pages [24] -->
m

<!-- b007696 | prose | pages [24] -->
m

<!-- b007697 | prose | pages [24] -->
m

<!-- b007698 | prose | pages [24] -->
m

<!-- b007699 | prose | pages [24] -->
m

<!-- b007700 | prose | pages [24] -->
m

<!-- b007701 | prose | pages [24] -->
m

<!-- b007702 | prose | pages [24] -->
m

<!-- b007703 | prose | pages [24] -->
m

<!-- b007704 | prose | pages [24] -->
m

<!-- b007705 | prose | pages [24] -->
m

<!-- b007706 | prose | pages [24] -->
m

<!-- b007707 | prose | pages [24] -->
m

<!-- b007708 | prose | pages [24] -->
m

<!-- b007709 | prose | pages [24] -->
m

<!-- b007710 | prose | pages [24] -->
m

<!-- b007711 | prose | pages [24] -->
m

<!-- b007712 | prose | pages [24] -->
m

<!-- b007713 | prose | pages [24] -->
m

<!-- b007714 | prose | pages [24] -->
m

<!-- b007715 | prose | pages [24] -->
m

<!-- b007716 | prose | pages [24] -->
m

<!-- b007717 | prose | pages [24] -->
m

<!-- b007718 | prose | pages [24] -->
m

<!-- b007719 | prose | pages [24] -->
m

<!-- b007720 | prose | pages [24] -->
m

<!-- b007721 | prose | pages [24] -->
m

<!-- b007722 | prose | pages [24] -->
m

<!-- b007723 | prose | pages [24] -->
m

<!-- b007724 | prose | pages [24] -->
m

<!-- b007725 | prose | pages [24] -->
m

<!-- b007726 | prose | pages [24] -->
m

<!-- b007727 | prose | pages [24] -->
m

<!-- b007728 | prose | pages [24] -->
m

<!-- b007729 | prose | pages [24] -->
m

<!-- b007730 | prose | pages [24] -->
m

<!-- b007731 | prose | pages [24] -->
m

<!-- b007732 | prose | pages [24] -->
m

<!-- b007733 | prose | pages [24] -->
m

<!-- b007734 | prose | pages [24] -->
m

<!-- b007735 | prose | pages [24] -->
m

<!-- b007736 | prose | pages [24] -->
m

<!-- b007737 | prose | pages [24] -->
m

<!-- b007738 | prose | pages [24] -->
m

<!-- b007739 | prose | pages [24] -->
m

<!-- b007740 | prose | pages [24] -->
m

<!-- b007741 | prose | pages [24] -->
m

<!-- b007742 | prose | pages [24] -->
m

<!-- b007743 | prose | pages [24] -->
m

<!-- b007744 | prose | pages [24] -->
m

<!-- b007745 | prose | pages [24] -->
m

<!-- b007746 | prose | pages [24] -->
m

<!-- b007747 | prose | pages [24] -->
m

<!-- b007748 | prose | pages [24] -->
m

<!-- b007749 | prose | pages [24] -->
m

<!-- b007750 | prose | pages [24] -->
m

<!-- b007751 | prose | pages [24] -->
m

<!-- b007752 | prose | pages [24] -->
m

<!-- b007753 | prose | pages [24] -->
m

<!-- b007754 | prose | pages [24] -->
m

<!-- b007755 | prose | pages [24] -->
m

<!-- b007756 | prose | pages [24] -->
m

<!-- b007757 | prose | pages [24] -->
m

<!-- b007758 | prose | pages [24] -->
m

<!-- b007759 | prose | pages [24] -->
m

<!-- b007760 | prose | pages [24] -->
m

<!-- b007761 | prose | pages [24] -->
making dynamics, risking suboptimal policy recommendations.

<!-- b007762 | prose | pages [24] -->
m

<!-- b007763 | prose | pages [24] -->
m

<!-- b007764 | prose | pages [24] -->
m

<!-- b007765 | prose | pages [24] -->
m

<!-- b007766 | prose | pages [24] -->
m

<!-- b007767 | prose | pages [24] -->
m

<!-- b007768 | prose | pages [24] -->
m

<!-- b007769 | prose | pages [24] -->
m

<!-- b007770 | prose | pages [24] -->
m

<!-- b007771 | prose | pages [24] -->
m

<!-- b007772 | prose | pages [24] -->
m

<!-- b007773 | prose | pages [24] -->
m

<!-- b007774 | prose | pages [24] -->
m

<!-- b007775 | prose | pages [24] -->
m

<!-- b007776 | prose | pages [24] -->
m

<!-- b007777 | prose | pages [24] -->
m

<!-- b007778 | prose | pages [24] -->
m

<!-- b007779 | prose | pages [24] -->
m

<!-- b007780 | prose | pages [24] -->
m

<!-- b007781 | prose | pages [24] -->
m

<!-- b007782 | prose | pages [24] -->
m

<!-- b007783 | prose | pages [24] -->
m

<!-- b007784 | prose | pages [24] -->
m

<!-- b007785 | prose | pages [24] -->
m

<!-- b007786 | prose | pages [24] -->
m

<!-- b007787 | prose | pages [24] -->
m

<!-- b007788 | prose | pages [24] -->
m

<!-- b007789 | prose | pages [24] -->
m

<!-- b007790 | prose | pages [24] -->
m

<!-- b007791 | prose | pages [24] -->
m

<!-- b007792 | prose | pages [24] -->
m

<!-- b007793 | prose | pages [24] -->
m

<!-- b007794 | prose | pages [24] -->
m

<!-- b007795 | prose | pages [24] -->
m

<!-- b007796 | prose | pages [24] -->
m

<!-- b007797 | prose | pages [24] -->
m

<!-- b007798 | prose | pages [24] -->
m

<!-- b007799 | prose | pages [24] -->
m

<!-- b007800 | prose | pages [24] -->
m

<!-- b007801 | prose | pages [24] -->
m

<!-- b007802 | prose | pages [24] -->
m

<!-- b007803 | prose | pages [24] -->
m

<!-- b007804 | prose | pages [24] -->
m

<!-- b007805 | prose | pages [24] -->
m

<!-- b007806 | prose | pages [24] -->
m

<!-- b007807 | prose | pages [24] -->
m

<!-- b007808 | prose | pages [24] -->
m

<!-- b007809 | prose | pages [24] -->
m

<!-- b007810 | prose | pages [24] -->
m

<!-- b007811 | prose | pages [24] -->
m

<!-- b007812 | prose | pages [24] -->
m

<!-- b007813 | prose | pages [24] -->
m

<!-- b007814 | prose | pages [24] -->
m

<!-- b007815 | prose | pages [24] -->
m

<!-- b007816 | prose | pages [24] -->
m

<!-- b007817 | prose | pages [24] -->
m

<!-- b007818 | prose | pages [24] -->
m

<!-- b007819 | prose | pages [24] -->
m

<!-- b007820 | prose | pages [24] -->
m

<!-- b007821 | prose | pages [24] -->
m

<!-- b007822 | prose | pages [24] -->
m

<!-- b007823 | prose | pages [24] -->
m

<!-- b007824 | prose | pages [24] -->
m

<!-- b007825 | prose | pages [24] -->
m

<!-- b007826 | prose | pages [24] -->
m

<!-- b007827 | prose | pages [24] -->
m

<!-- b007828 | prose | pages [24] -->
m

<!-- b007829 | prose | pages [24] -->
m

<!-- b007830 | prose | pages [24] -->
m

<!-- b007831 | prose | pages [24] -->
m

<!-- b007832 | prose | pages [24] -->
m

<!-- b007833 | prose | pages [24] -->
m

<!-- b007834 | prose | pages [24] -->
m

<!-- b007835 | prose | pages [24] -->
m

<!-- b007836 | prose | pages [24] -->
m

<!-- b007837 | prose | pages [24] -->
m

<!-- b007838 | prose | pages [24] -->
m

<!-- b007839 | prose | pages [24] -->
m

<!-- b007840 | prose | pages [24] -->
m

<!-- b007841 | prose | pages [24] -->
m

<!-- b007842 | prose | pages [24] -->
m

<!-- b007843 | prose | pages [24] -->
m

<!-- b007844 | prose | pages [24] -->
m

<!-- b007845 | prose | pages [24] -->
m

<!-- b007846 | prose | pages [24] -->
m

<!-- b007847 | prose | pages [24] -->
m

<!-- b007848 | prose | pages [24] -->
m

<!-- b007849 | prose | pages [24] -->
m

<!-- b007850 | prose | pages [24] -->
m

<!-- b007851 | prose | pages [24] -->
m

<!-- b007852 | prose | pages [24] -->
m

<!-- b007853 | prose | pages [24] -->
m

<!-- b007854 | prose | pages [24] -->
m

<!-- b007855 | prose | pages [24] -->
m

<!-- b007856 | prose | pages [24] -->
m

<!-- b007857 | prose | pages [24] -->
m

<!-- b007858 | prose | pages [24] -->
m

<!-- b007859 | prose | pages [24] -->
m

<!-- b007860 | prose | pages [24] -->
m

<!-- b007861 | prose | pages [24] -->
m

<!-- b007862 | prose | pages [24] -->
m

<!-- b007863 | prose | pages [24] -->
m

<!-- b007864 | prose | pages [24] -->
m

<!-- b007865 | prose | pages [24] -->
m

<!-- b007866 | prose | pages [24] -->
m

<!-- b007867 | prose | pages [24] -->
m

<!-- b007868 | prose | pages [24] -->
m

<!-- b007869 | prose | pages [24] -->
m

<!-- b007870 | prose | pages [24] -->
m

<!-- b007871 | prose | pages [24] -->
m

<!-- b007872 | prose | pages [24] -->
m

<!-- b007873 | prose | pages [24] -->
m

<!-- b007874 | prose | pages [24] -->
m

<!-- b007875 | prose | pages [24] -->
m

<!-- b007876 | prose | pages [24] -->
m

<!-- b007877 | prose | pages [24] -->
m

<!-- b007878 | prose | pages [24] -->
m

<!-- b007879 | prose | pages [24] -->
m

<!-- b007880 | prose | pages [24] -->
m

<!-- b007881 | prose | pages [24] -->
m

<!-- b007882 | prose | pages [24] -->
m

<!-- b007883 | prose | pages [24] -->
m

<!-- b007884 | prose | pages [24] -->
m

<!-- b007885 | prose | pages [24] -->
m

<!-- b007886 | prose | pages [24] -->
m

<!-- b007887 | prose | pages [24] -->
m

<!-- b007888 | prose | pages [24] -->
m

<!-- b007889 | prose | pages [24] -->
m

<!-- b007890 | prose | pages [24] -->
m

<!-- b007891 | prose | pages [24] -->
m

<!-- b007892 | prose | pages [24] -->
m

<!-- b007893 | prose | pages [24] -->
m

<!-- b007894 | prose | pages [24] -->
m

<!-- b007895 | prose | pages [24] -->
m

<!-- b007896 | prose | pages [24] -->
m

<!-- b007897 | prose | pages [24] -->
m

<!-- b007898 | prose | pages [24] -->
m

<!-- b007899 | prose | pages [24] -->
m

<!-- b007900 | prose | pages [24] -->
m

<!-- b007901 | prose | pages [24] -->
m

<!-- b007902 | prose | pages [24] -->
m

<!-- b007903 | prose | pages [24] -->
m

<!-- b007904 | prose | pages [24] -->
m

<!-- b007905 | prose | pages [24] -->
m

<!-- b007906 | prose | pages [24] -->
m

<!-- b007907 | prose | pages [24] -->
m

<!-- b007908 | prose | pages [24] -->
m

<!-- b007909 | prose | pages [24] -->
m

<!-- b007910 | prose | pages [24] -->
m

<!-- b007911 | prose | pages [24] -->
m

<!-- b007912 | prose | pages [24] -->
m

<!-- b007913 | prose | pages [24] -->
m

<!-- b007914 | prose | pages [24] -->
m

<!-- b007915 | prose | pages [24] -->
m

<!-- b007916 | prose | pages [24] -->
m

<!-- b007917 | prose | pages [24] -->
m

<!-- b007918 | prose | pages [24] -->
m

<!-- b007919 | prose | pages [24] -->
m

<!-- b007920 | prose | pages [24] -->
m

<!-- b007921 | prose | pages [24] -->
m

<!-- b007922 | prose | pages [24] -->
m

<!-- b007923 | prose | pages [24] -->
m

<!-- b007924 | prose | pages [24] -->
m

<!-- b007925 | prose | pages [24] -->
m

<!-- b007926 | prose | pages [24] -->
m

<!-- b007927 | prose | pages [24] -->
m

<!-- b007928 | prose | pages [24] -->
m

<!-- b007929 | prose | pages [24] -->
m

<!-- b007930 | prose | pages [24] -->
m

<!-- b007931 | prose | pages [24] -->
m

<!-- b007932 | prose | pages [24] -->
m

<!-- b007933 | prose | pages [24] -->
m

<!-- b007934 | prose | pages [24] -->
m

<!-- b007935 | prose | pages [24] -->
m

<!-- b007936 | prose | pages [24] -->
m

<!-- b007937 | prose | pages [24] -->
m

<!-- b007938 | prose | pages [24] -->
m

<!-- b007939 | prose | pages [24] -->
m

<!-- b007940 | prose | pages [24] -->
m

<!-- b007941 | prose | pages [24] -->
m

<!-- b007942 | prose | pages [24] -->
m

<!-- b007943 | prose | pages [24] -->
m

<!-- b007944 | prose | pages [24] -->
m

<!-- b007945 | prose | pages [24] -->
m

<!-- b007946 | prose | pages [24] -->
m

<!-- b007947 | prose | pages [24] -->
m

<!-- b007948 | prose | pages [24] -->
m

<!-- b007949 | prose | pages [24] -->
m

<!-- b007950 | prose | pages [24] -->
m

<!-- b007951 | prose | pages [24] -->
m

<!-- b007952 | prose | pages [24] -->
m

<!-- b007953 | prose | pages [24] -->
m

<!-- b007954 | prose | pages [24] -->
m

<!-- b007955 | prose | pages [24] -->
m

<!-- b007956 | prose | pages [24] -->
m

<!-- b007957 | prose | pages [24] -->
m

<!-- b007958 | prose | pages [24] -->
m

<!-- b007959 | prose | pages [24] -->
m

<!-- b007960 | prose | pages [24] -->
m

<!-- b007961 | prose | pages [24] -->
m

<!-- b007962 | prose | pages [24] -->
m

<!-- b007963 | prose | pages [24] -->
m

<!-- b007964 | prose | pages [24] -->
m

<!-- b007965 | prose | pages [24] -->
m

<!-- b007966 | prose | pages [24] -->
m

<!-- b007967 | prose | pages [24] -->
m

<!-- b007968 | prose | pages [24] -->
m

<!-- b007969 | prose | pages [24] -->
m

<!-- b007970 | prose | pages [24] -->
m

<!-- b007971 | prose | pages [24] -->
m

<!-- b007972 | prose | pages [24] -->
m

<!-- b007973 | prose | pages [24] -->
m

<!-- b007974 | prose | pages [24] -->
m

<!-- b007975 | prose | pages [24] -->
m

<!-- b007976 | prose | pages [24] -->
m

<!-- b007977 | prose | pages [24] -->
m

<!-- b007978 | prose | pages [24] -->
m

<!-- b007979 | prose | pages [24] -->
m

<!-- b007980 | prose | pages [24] -->
m

<!-- b007981 | prose | pages [24] -->
m

<!-- b007982 | prose | pages [24] -->
m

<!-- b007983 | prose | pages [24] -->
m

<!-- b007984 | prose | pages [24] -->
m

<!-- b007985 | prose | pages [24] -->
m

<!-- b007986 | prose | pages [24] -->
m

<!-- b007987 | prose | pages [24] -->
m

<!-- b007988 | prose | pages [24] -->
m

<!-- b007989 | prose | pages [24] -->
m

<!-- b007990 | prose | pages [24] -->
m

<!-- b007991 | prose | pages [24] -->
m

<!-- b007992 | prose | pages [24] -->
m

<!-- b007993 | prose | pages [24] -->
m

<!-- b007994 | prose | pages [24] -->
m

<!-- b007995 | prose | pages [24] -->
m

<!-- b007996 | prose | pages [24] -->
m

<!-- b007997 | prose | pages [24] -->
m

<!-- b007998 | prose | pages [24] -->
m

<!-- b007999 | prose | pages [24] -->
m

<!-- b008000 | prose | pages [24] -->
m

<!-- b008001 | prose | pages [24] -->
m

<!-- b008002 | prose | pages [24] -->
m

<!-- b008003 | prose | pages [24] -->
m

<!-- b008004 | prose | pages [24] -->
m

<!-- b008005 | prose | pages [24] -->
m

<!-- b008006 | prose | pages [24] -->
m

<!-- b008007 | prose | pages [24] -->
m

<!-- b008008 | prose | pages [24] -->
m

<!-- b008009 | prose | pages [24] -->
m

<!-- b008010 | prose | pages [24] -->
m

<!-- b008011 | prose | pages [24] -->
m

<!-- b008012 | prose | pages [24] -->
m

<!-- b008013 | prose | pages [24] -->
m

<!-- b008014 | prose | pages [24] -->
m

<!-- b008015 | prose | pages [24] -->
m

<!-- b008016 | prose | pages [24] -->
m

<!-- b008017 | prose | pages [24] -->
m

<!-- b008018 | prose | pages [24] -->
m

<!-- b008019 | prose | pages [24] -->
m

<!-- b008020 | prose | pages [24] -->
m

<!-- b008021 | prose | pages [24] -->
m

<!-- b008022 | prose | pages [24] -->
m

<!-- b008023 | prose | pages [24] -->
m

<!-- b008024 | prose | pages [24] -->
m

<!-- b008025 | prose | pages [24] -->
m

<!-- b008026 | prose | pages [24] -->
m

<!-- b008027 | prose | pages [24] -->
m

<!-- b008028 | prose | pages [24] -->
m

<!-- b008029 | prose | pages [24] -->
m

<!-- b008030 | prose | pages [24] -->
m

<!-- b008031 | prose | pages [24] -->
m

<!-- b008032 | prose | pages [24] -->
m

<!-- b008033 | prose | pages [24] -->
m

<!-- b008034 | prose | pages [24] -->
m

<!-- b008035 | prose | pages [24] -->
m

<!-- b008036 | prose | pages [24] -->
m

<!-- b008037 | prose | pages [24] -->
m

<!-- b008038 | prose | pages [24] -->
m

<!-- b008039 | prose | pages [24] -->
m

<!-- b008040 | prose | pages [24] -->
m

<!-- b008041 | prose | pages [24] -->
m

<!-- b008042 | prose | pages [24] -->
m

<!-- b008043 | prose | pages [24] -->
m

<!-- b008044 | prose | pages [24] -->
m

<!-- b008045 | prose | pages [24] -->
m

<!-- b008046 | prose | pages [24] -->
m

<!-- b008047 | prose | pages [24] -->
m

<!-- b008048 | prose | pages [24] -->
m

<!-- b008049 | prose | pages [24] -->
m

<!-- b008050 | prose | pages [24] -->
m

<!-- b008051 | prose | pages [24] -->
m

<!-- b008052 | prose | pages [24] -->
m

<!-- b008053 | prose | pages [24] -->
m

<!-- b008054 | prose | pages [24] -->
m

<!-- b008055 | prose | pages [24] -->
m

<!-- b008056 | prose | pages [24] -->
m

<!-- b008057 | prose | pages [24] -->
m

<!-- b008058 | prose | pages [24] -->
m

<!-- b008059 | prose | pages [24] -->
m

<!-- b008060 | prose | pages [24] -->
m

<!-- b008061 | prose | pages [24] -->
m

<!-- b008062 | prose | pages [24] -->
m

<!-- b008063 | prose | pages [24] -->
m

<!-- b008064 | prose | pages [24] -->
m

<!-- b008065 | prose | pages [24] -->
m

<!-- b008066 | prose | pages [24] -->
m

<!-- b008067 | prose | pages [24] -->
m

<!-- b008068 | prose | pages [24] -->
m

<!-- b008069 | prose | pages [24] -->
m

<!-- b008070 | prose | pages [24] -->
m

<!-- b008071 | prose | pages [24] -->
m

<!-- b008072 | prose | pages [24] -->
m

<!-- b008073 | prose | pages [24] -->
m

<!-- b008074 | prose | pages [24] -->
m

<!-- b008075 | prose | pages [24] -->
m

<!-- b008076 | prose | pages [24] -->
m

<!-- b008077 | prose | pages [24] -->
m

<!-- b008078 | prose | pages [24] -->
m

<!-- b008079 | prose | pages [24] -->
m

<!-- b008080 | prose | pages [24] -->
m

<!-- b008081 | prose | pages [24] -->
m

<!-- b008082 | prose | pages [24] -->
m

<!-- b008083 | prose | pages [24] -->
m

<!-- b008084 | prose | pages [24] -->
m

<!-- b008085 | prose | pages [24] -->
m

<!-- b008086 | prose | pages [24] -->
m

<!-- b008087 | prose | pages [24] -->
m

<!-- b008088 | prose | pages [24] -->
m

<!-- b008089 | prose | pages [24] -->
m

<!-- b008090 | prose | pages [24] -->
m

<!-- b008091 | prose | pages [24] -->
m

<!-- b008092 | prose | pages [24] -->
m

<!-- b008093 | prose | pages [24] -->
m

<!-- b008094 | prose | pages [24] -->
m

<!-- b008095 | prose | pages [24] -->
m

<!-- b008096 | prose | pages [24] -->
m

<!-- b008097 | prose | pages [24] -->
m

<!-- b008098 | prose | pages [24] -->
m

<!-- b008099 | prose | pages [24] -->
m

<!-- b008100 | prose | pages [24] -->
m

<!-- b008101 | prose | pages [24] -->
m

<!-- b008102 | prose | pages [24] -->
m

<!-- b008103 | prose | pages [24] -->
m

<!-- b008104 | prose | pages [24] -->
m

<!-- b008105 | prose | pages [24] -->
m

<!-- b008106 | prose | pages [24] -->
m

<!-- b008107 | prose | pages [24] -->
m

<!-- b008108 | prose | pages [24] -->
m

<!-- b008109 | prose | pages [24] -->
m

<!-- b008110 | prose | pages [24] -->
m

<!-- b008111 | prose | pages [24] -->
m

<!-- b008112 | prose | pages [24] -->
m

<!-- b008113 | prose | pages [24] -->
m

<!-- b008114 | prose | pages [24] -->
m

<!-- b008115 | prose | pages [24] -->
m

<!-- b008116 | prose | pages [24] -->
m

<!-- b008117 | prose | pages [24] -->
m

<!-- b008118 | prose | pages [24] -->
m

<!-- b008119 | prose | pages [24] -->
m

<!-- b008120 | prose | pages [24] -->
m

<!-- b008121 | prose | pages [24] -->
m

<!-- b008122 | prose | pages [24] -->
m

<!-- b008123 | prose | pages [24] -->
m

<!-- b008124 | prose | pages [24] -->
m

<!-- b008125 | prose | pages [24] -->
m

<!-- b008126 | prose | pages [24] -->
m

<!-- b008127 | prose | pages [24] -->
m

<!-- b008128 | prose | pages [24] -->
m

<!-- b008129 | prose | pages [24] -->
m

<!-- b008130 | prose | pages [24] -->
m

<!-- b008131 | prose | pages [24] -->
m

<!-- b008132 | prose | pages [24] -->
m

<!-- b008133 | prose | pages [24] -->
m

<!-- b008134 | prose | pages [24] -->
m

<!-- b008135 | prose | pages [24] -->
m

<!-- b008136 | prose | pages [24] -->
m

<!-- b008137 | prose | pages [24] -->
m

<!-- b008138 | prose | pages [24] -->
m

<!-- b008139 | prose | pages [24] -->
m

<!-- b008140 | prose | pages [24] -->
m

<!-- b008141 | prose | pages [24] -->
m

<!-- b008142 | prose | pages [24] -->
m

<!-- b008143 | prose | pages [24] -->
m

<!-- b008144 | prose | pages [24] -->
m

<!-- b008145 | prose | pages [24] -->
m

<!-- b008146 | prose | pages [24] -->
m

<!-- b008147 | prose | pages [24] -->
m

<!-- b008148 | prose | pages [24] -->
m

<!-- b008149 | prose | pages [24] -->
m

<!-- b008150 | prose | pages [24] -->
m

<!-- b008151 | prose | pages [24] -->
m

<!-- b008152 | prose | pages [24] -->
m

<!-- b008153 | prose | pages [24] -->
m

<!-- b008154 | prose | pages [24] -->
m

<!-- b008155 | prose | pages [24] -->
m

<!-- b008156 | prose | pages [24] -->
m

<!-- b008157 | prose | pages [24] -->
m

<!-- b008158 | prose | pages [24] -->
m

<!-- b008159 | prose | pages [24] -->
m

<!-- b008160 | prose | pages [24] -->
m

<!-- b008161 | prose | pages [24] -->
m

<!-- b008162 | prose | pages [24] -->
m

<!-- b008163 | prose | pages [24] -->
10 Conlusion

<!-- b008164 | prose | pages [24] -->
m

<!-- b008165 | prose | pages [24] -->
m

<!-- b008166 | prose | pages [24] -->
m

<!-- b008167 | prose | pages [24] -->
m

<!-- b008168 | prose | pages [24] -->
m

<!-- b008169 | prose | pages [24] -->
m

<!-- b008170 | prose | pages [24] -->
m

<!-- b008171 | prose | pages [24] -->
m

<!-- b008172 | prose | pages [24] -->
m

<!-- b008173 | prose | pages [24] -->
m

<!-- b008174 | prose | pages [24] -->
m

<!-- b008175 | prose | pages [24] -->
m

<!-- b008176 | prose | pages [24] -->
m

<!-- b008177 | prose | pages [24] -->
m

<!-- b008178 | prose | pages [24] -->
m

<!-- b008179 | prose | pages [24] -->
m

<!-- b008180 | prose | pages [24] -->
m

<!-- b008181 | prose | pages [24] -->
m

<!-- b008182 | prose | pages [24] -->
m

<!-- b008183 | prose | pages [24] -->
m

<!-- b008184 | prose | pages [24] -->
m

<!-- b008185 | prose | pages [24] -->
m

<!-- b008186 | prose | pages [24] -->
m

<!-- b008187 | prose | pages [24] -->
m

<!-- b008188 | prose | pages [24] -->
m

<!-- b008189 | prose | pages [24] -->
m

<!-- b008190 | prose | pages [24] -->
m

<!-- b008191 | prose | pages [24] -->
m

<!-- b008192 | prose | pages [24] -->
m

<!-- b008193 | prose | pages [24] -->
m

<!-- b008194 | prose | pages [24] -->
m

<!-- b008195 | prose | pages [24] -->
m

<!-- b008196 | prose | pages [24] -->
m

<!-- b008197 | prose | pages [24] -->
m

<!-- b008198 | prose | pages [24] -->
m

<!-- b008199 | prose | pages [24] -->
m

<!-- b008200 | prose | pages [24] -->
m

<!-- b008201 | prose | pages [24] -->
m

<!-- b008202 | prose | pages [24] -->
m

<!-- b008203 | prose | pages [24] -->
m

<!-- b008204 | prose | pages [24] -->
m

<!-- b008205 | prose | pages [24] -->
m

<!-- b008206 | prose | pages [24] -->
m

<!-- b008207 | prose | pages [24] -->
m

<!-- b008208 | prose | pages [24] -->
m

<!-- b008209 | prose | pages [24] -->
m

<!-- b008210 | prose | pages [24] -->
m

<!-- b008211 | prose | pages [24] -->
m

<!-- b008212 | prose | pages [24] -->
m

<!-- b008213 | prose | pages [24] -->
m

<!-- b008214 | prose | pages [24] -->
m

<!-- b008215 | prose | pages [24] -->
m

<!-- b008216 | prose | pages [24] -->
m

<!-- b008217 | prose | pages [24] -->
m

<!-- b008218 | prose | pages [24] -->
m

<!-- b008219 | prose | pages [24] -->
m

<!-- b008220 | prose | pages [24] -->
m

<!-- b008221 | prose | pages [24] -->
m

<!-- b008222 | prose | pages [24] -->
m

<!-- b008223 | prose | pages [24] -->
m

<!-- b008224 | prose | pages [24] -->
m

<!-- b008225 | prose | pages [24] -->
m

<!-- b008226 | prose | pages [24] -->
m

<!-- b008227 | prose | pages [24] -->
m

<!-- b008228 | prose | pages [24] -->
m

<!-- b008229 | prose | pages [24] -->
m

<!-- b008230 | prose | pages [24] -->
m

<!-- b008231 | prose | pages [24] -->
m

<!-- b008232 | prose | pages [24] -->
m

<!-- b008233 | prose | pages [24] -->
m

<!-- b008234 | prose | pages [24] -->
m

<!-- b008235 | prose | pages [24] -->
m

<!-- b008236 | prose | pages [24] -->
m

<!-- b008237 | prose | pages [24] -->
m

<!-- b008238 | prose | pages [24] -->
m

<!-- b008239 | prose | pages [24] -->
m

<!-- b008240 | prose | pages [24] -->
m

<!-- b008241 | prose | pages [24] -->
The proposed framework advances urban traffic management by integrating net- work theory, stochastic optimization, and equity-driven metrics to address post-disaster resilience and mobility. It successfully quantifies multidimensional impacts (e.g., 41.7% traffic surge on bypass routes, 2.1M dollars annual health costs) and offers scalable in- terventions like BRT corridors and micro-mobility hubs. Future work should prioritize validating the model in diverse urban contexts, incorporating real-time data streams, and refining assumptions to better capture dynamic behavioral and environmental in- teractions.

<!-- b008242 | heading | pages [24] -->
References

<!-- b008243 | references | pages [24] -->
[1] Sheffi, Y. "Equilibrium analysis with mathematical programming methods." Mas-

<!-- b008244 | references | pages [24] -->
sachusetts: Institute of Technology (1985).

<!-- b008245 | references | pages [24] -->
[2] Boyce, David E., and Huw CWL Williams. Forecasting urban travel: Past, present

<!-- b008246 | references | pages [24] -->
and future. Edward Elgar Publishing, 2015.

<!-- b008247 | references | pages [24] -->
[3] Waissi, Gary R. "Network flows: Theory, algorithms, and applications." (1994):

<!-- b008248 | references | pages [24] -->
133-135.

<!-- b008249 | references | pages [24] -->
[4] Goguen, Joseph A. "LA Zadeh. Fuzzy sets. Information and control, vol. 8 (1965),

<!-- b008250 | references | pages [24] -->
pp. 338–353.-LA Zadeh. Similarity relations and fuzzy orderings. Information sci-

<!-- b008251 | references | pages [24] -->
ences, vol. 3 (1971), pp. 177–200." The Journal of Symbolic Logic 38.4 (1973): 656-

<!-- b008252 | references | pages [24] -->
657.

<!-- b008253 | references | pages [24] -->
[5] Chen, Shu-Jen, and Ching-Lai Hwang. "Fuzzy multiple attribute decision making

<!-- b008254 | references | pages [24] -->
methods." Fuzzy multiple attribute decision making: Methods and applications.

<!-- b008255 | references | pages [24] -->
Berlin, Heidelberg: Springer Berlin Heidelberg, 1992. 289-486.

<!-- b008256 | references | pages [24] -->
[6] Deb, Kalyanmoy. "Multi-objective optimisation using evolutionary algorithms: an

<!-- b008257 | references | pages [24] -->
introduction." Multi-objective evolutionary optimisation for product design and

<!-- b008258 | references | pages [24] -->
manufacturing. London: Springer London, 2011. 3-34.

<!-- b008259 | references | pages [24] -->
[7] Robert, Christian P., George Casella, and George Casella. Monte Carlo statistical

<!-- b008260 | references | pages [24] -->
methods. Vol. 2. New York: Springer, 1999.

<!-- b008261 | references | pages [24] -->
[8] Van Den Berg, Ewout, and Michael P. Friedlander. "Probing the Pareto frontier for

<!-- b008262 | references | pages [24] -->
basis pursuit solutions." Siam journal on scientific computing 31.2 (2009): 890-912.

<!-- b008263 | references | pages [24] -->
关注数学模型

<!-- b008264 | furniture | pages [24] -->
2

<!-- b008265 | furniture | pages [24] -->
MATHmodels

<!-- b008266 | furniture | pages [24] -->
获取更多资讯
