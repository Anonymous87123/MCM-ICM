# P-B-2025-2502617-613354d9

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2025

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
Problem Chosen MCM/ICM

<!-- b000004 | furniture | pages [1] -->
2502617

<!-- b000005 | prose | pages [1] -->
B

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Economic-Social-Environmental Triangle

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
The rapid growth of tourism has led many countries and regions to recognize the tension between environmental preservation and the short-term economic benefits of traditional tourism models. The overload alarm of tourism industry prompts the question: How should tourism evolve in the future? Sustainable tourism has emerged as a crucial solution to this dilemma. This paper develops a multi-objective planning model that integrates economic, social, and environmental factors, tailored to the current state of the tourism industry in Juneau and its development goals.

<!-- b000010 | prose | pages [1] -->
In Sub-model I, economic benefit is the primary optimization objective. Considering the diminishing marginal returns and increasing marginal costs associated with a rising number of tourists, we developed a mathematical relationship between economic benefits and costs as a function of tourist volume. Through a cost-benefit analysis (CBA) model, we then defined the feasible domain of economic constraints and determined the maximum economic benefit.

<!-- b000011 | prose | pages [1] -->
In Sub-model II, social benefit is the second optimization objective. It is assessed through social satisfaction analysis and monetization. Social satisfaction is influenced by residents' living pressure and regional congestion. We use the potential benefit per unit of social satisfaction as the conversion factor and model social benefit changes with tourist numbers. A social welfare optimization model identifies the feasible domain and calculates the maximum social benefit.

<!-- b000012 | prose | pages [1] -->
● In Sub-model III, environmental benefit is the third optimization objective. Focusing on glacier degradation, the primary y environmental issue in Juneau. Given the link between glacier degradation and carbon emissions, the carbon footprint is chosen as the key environmental indicator. The monetization of this effect follows a similar method to that of social satisfaction. Through ecological carrying capacity analysis, we determine the feasible range for environmental benefits and calculate the maximum achievable value.

<!-- b000013 | prose | pages [1] -->
Furthermore, we integrate the three preceding models and account for the coupling relationships among them. Using the SLSQP method, we determine the global Pareto-optimal solution for tourist numbers and overall benefits. Specifically, when the number of tourists reaches 1.32 million, the economic measure of the municipal weighted total benefit is 10 million USD, while the net income for Juneau amounts to 576 million USD.

<!-- b000014 | prose | pages [1] -->
Finally, we analyze the sensitivity of key model parameters, as well as the sources of additional government revenue and spending programs. We also write a memo to the Tourist Council of Juneau and extend the model to Jiuzhaigou, China. The results show that our model has good usability and robustness.

<!-- b000015 | keywords | pages [1] -->
Keywords: Sustainable Tourism, Management Measures, Multi-objective Planning Model, Pareto

<!-- b000016 | prose | pages [1] -->
Optimization, SLSQP

<!-- b000017 | furniture | pages [2] -->
Team # 2502617

<!-- b000018 | furniture | pages [2] -->
Page 2 of 25

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | heading | pages [2] -->
Introduction

<!-- b000021 | prose | pages [2] -->
3 1 3 1.1 Problem Background . 1.2 4 Restatement of the Problem 1.3 4 Literature Review . 1.4 5 Our Work .

<!-- b000022 | heading | pages [2] -->
Assumptions and Justifications

<!-- b000023 | prose | pages [2] -->
5 2

<!-- b000024 | heading | pages [2] -->
Notations

<!-- b000025 | prose | pages [2] -->
3 6

<!-- b000026 | heading | pages [2] -->
Multi-Objective Optimization Model

<!-- b000027 | prose | pages [2] -->
7 4

<!-- b000028 | heading | pages [2] -->
Sub-model I: Cost-benefit Analysis Considering Marginal Effects

<!-- b000029 | prose | pages [2] -->
7 4.1 4.1.1 Analysis of Economic benefits 8 4.1.2 Analysis of Economic Costs 8 4.1.3 Overall Economic Performance 9 4.2

<!-- b000030 | heading | pages [2] -->
Sub-model II: Social Welfare Optimization Model

<!-- b000031 | prose | pages [2] -->
10 Estimation of Social Satisfaction Indicator 4.2.1 10 4.2.2 Monetized Conversion of Social Satisfaction 10 4.2.3 Overall Social Performance 11

<!-- b000032 | heading | pages [2] -->
Sub-model III: Environmental Carrying Capacity Model

<!-- b000033 | prose | pages [2] -->
4.3 11 4.3.1 Carbon Footprint Accounting 12 4.3.2 Monetization of Carbon Footprint 13 4.3.3 13 Overall Environmental Performance 4.4 14 Pareto Optimal Solution for Total benefit 4.4.1 14 Determination of Weight Value 4.4.2 Global Pareto Optimization in the Game between Scenic Spots 15 1 15

<!-- b000034 | heading | pages [2] -->
Results and Extension

<!-- b000035 | prose | pages [2] -->
5 Optimization Objectives 15 5.1 Constraints Analysis 15 5.2

<!-- b000036 | heading | pages [2] -->
Optimization Result Analysis

<!-- b000037 | prose | pages [2] -->
16 5.3 Key Parameter Determination 5.4 18 19 Additional Income and Expenditure Plan 6

<!-- b000038 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000039 | prose | pages [2] -->
20 7 Effect of Changes in Total Tourists and Performance per Tourist 20 7.1 7.2 Effect of Changes in Total benefit 20 21

<!-- b000040 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000041 | prose | pages [2] -->
8

<!-- b000042 | heading | pages [2] -->
Strengths

<!-- b000043 | prose | pages [2] -->
1 21 8.1 8.2

<!-- b000044 | heading | pages [2] -->
Weaknesses

<!-- b000045 | prose | pages [2] -->
21 21

<!-- b000046 | heading | pages [2] -->
Conclusion

<!-- b000047 | prose | pages [2] -->
9

<!-- b000048 | heading | pages [2] -->
References

<!-- b000049 | references | pages [2] -->
23

<!-- b000050 | references | pages [2] -->
25

<!-- b000051 | references | pages [2] -->
Memo

<!-- b000052 | references | pages [2] -->
关注数学模型

<!-- b000053 | furniture | pages [2] -->
获取更多资讯

<!-- b000054 | furniture | pages [3] -->
Team # 2502617

<!-- b000055 | furniture | pages [3] -->
Page 3 of 25

<!-- b000056 | heading | pages [3] -->
1 Introduction

<!-- b000057 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000058 | heading | pages [3] -->
1.1 Problem Background

<!-- b000059 | prose | pages [3] -->
In recent years, tourism has played an increasingly significant role in driving local economic growth, generating substantial revenue and gradually becoming a pillar industry for both local and global economies[1]. However, with the continuous rise in tourist numbers, issues such as environmental degradation, increased infrastructure costs, and declining resident satisfaction have emerged, posing serious threats to the sustainable development of local tourism. This phenomenon is particularly evident in Juneau, Alaska.

<!-- b000060 | prose | pages [3] -->
Juneau is renowned for its unique and breathtaking natural landscapes, which include expansive 微信号：MATHmodels national parks, majestic glaciers, and a 6,640-mile coastline. These attractions draw hundreds of thousands to over a million tourists annually, with the majority arriving via luxury cruise ships. In 2023, the tourism sector brought 1.6 million cruise passengers to Juneau, generating $375 million in economic revenue[2] , alongside nearly 4,000 cruise-related jobs and $18 million in tax revenue[3]. However, the influx of tourists has resulted in traffic congestion, overcrowded tourist sites, and rising hidden costs, such as increased infrastructure costs and the need for environmental remediation. Additionally, the noise from passenger helicopters has significantly disrupted the daily lives of local residents. More concerning is the impact of the surge in tourist numbers on the environment, including rising temperatures that have led to the retreat of the iconic Mendenhall Glacier. The pristine air, clean water, and natural beauty that once defined Juneau’s allure are now being threatened by the ongoing influx of tourists.

<!-- b000061 | caption | pages [3] -->
Figure 1: Overview of Tourism Industry in Juneau, Alaska

<!-- b000062 | prose | pages [3, 4] -->
To mitigate the negative impacts of unsustainable tourism growth, the Juneau government has implemented measures such as raising taxes and limiting visitor numbers to regulate tourist flow. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Additionally, it has intensified efforts to promote alternative attractions, such as wildlife viewing, in areas beyond the Mendenhall Glacier. Moving forward, the Juneau government should consider adopting more effective strategies to balance the social and economic benefits of tourism while developing comprehensive management plans. These plans should aim to advance the tourism sector while protecting the natural environment as much as possible, ensuring the long-term sustainability of tourism. This challenge not only affects the long-term sustainability of Juneau’s tourism industry but also represents a common issue faced by tourist cities worldwide.

<!-- b000063 | furniture | pages [3] -->
m

<!-- b000064 | furniture | pages [3] -->
m

<!-- b000065 | furniture | pages [3] -->
m

<!-- b000066 | furniture | pages [3] -->
m

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

<!-- b000387 | furniture | pages [4] -->
Team # 2502617

<!-- b000388 | furniture | pages [4] -->
Page 4 of 25

<!-- b000390 | heading | pages [4] -->
1.2 Restatement of the Problem

<!-- b000391 | prose | pages [4] -->
Based on the current situation in Juneau and the information outlined in the problem statement, it is essential to develop a comprehensive sustainable tourism management plan to maximize economic, social, and environmental benefits. Specifically, the plan must address the following three issues:

<!-- b000392 | prose | pages [4] -->
Problem 1: Develop a sustainable tourism management model tailored to the specific context of Juneau, considering all factors that may infvluence the long-term sustainable tourism industry. These factors include: environmental carrying capacity, both visible and hidden management costs, and local resident satisfaction.

<!-- b000393 | prose | pages [4] -->
Problem 2: Extend the model to other cities negatively affected by tourism and demonstrate its applicability in these cities. Analyze the impact of urban differences on the selection of key man- agement measures, promote attractions with fewer tourists, and promote sustainable development of local tourism industry.

<!-- b000394 | prose | pages [4] -->
Problem 3: Based on the model developed in Problem 1, submit a one page memo to the Juneau Tourism Commission, using actual data to illustrate the necessity of developing sustainable tourism and providing feasible tourism management optimization paths and measures for Juneau.

<!-- b000395 | heading | pages [4] -->
1.3 Literature Review

<!-- b000396 | prose | pages [4] -->
The development of tourism has contributed to the growth, but at the same time it has also had some impact on the natural environment[4]. Sustainable tourism has become an important topic of academic research[5]. The main indicators of the relevant discussions focus on the environmental, economic and social aspects[6]. In the existing studies, some scholars analyze the environmental benefits of tourism development[7], while Saayam[8] believe that sustainable tourism contributes to long-term social-economic stability, and Whitford et al.[9] discuss the role of sustainable tourism in product development for local residents. In addition, in the analysis of social benefits, scholars have analyzed the role of sustainable tourism in improving the quality of life of the residents[10], and improving the happiness of the residents’ life[11].

<!-- b000397 | prose | pages [4] -->
In addition, some scholars try the integrated management model of sustainable tourism. Stoica et al.[12] use the methods of benchmarking and SWOT analysis to construct a tourism manage- ment decision model, and Sripateep et al.[13] comprehensively consider the maximization of the interests of tourism stakeholders on the basis of the multi-objective planning model. However, the models that introduce Pareto optimization method into sustainable tourism management model and comprehensively consider the economic, social and environmental tripartite benefits are still few, and more scholars use Pareto optimization method to analyze the maximization of the interests of

<!-- b000398 | prose | pages [4, 5] -->
关注数学模型 some classes of stakeholders. For example, Ko,YD [14]derived the economic-environmental effect of sustainable tourism development in Seoul through Pareto optimization model, and Wang,XP et al.[15]analyzed the effect of tourism intermediate product price on the Pareto effectiveness of supply chain.In this analysis, we introduce the Pareto optimization method into the multi-objective model, which is innovative and reasonable.

<!-- b000399 | furniture | pages [4] -->
2

<!-- b000400 | furniture | pages [4] -->
MATHmodels

<!-- b000401 | furniture | pages [4] -->
获取更多资讯

<!-- b000402 | furniture | pages [5] -->
Team # 2502617

<!-- b000403 | furniture | pages [5] -->
Page 5 of 25

<!-- b000405 | heading | pages [5] -->
1.4 Our Work

<!-- b000406 | prose | pages [5] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000407 | caption | pages [5] -->
Figure 2: Our Work

<!-- b000408 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000409 | prose | pages [5] -->
Assumption1: Demandandexpenditureexhibitincreasingmarginalutility, whilerevenue(including hidden costs) follows decreasing marginal returns.

<!-- b000410 | heading | pages [5] -->
Justification: This aligns with classical economic models characterizing resource-constrained

<!-- b000411 | prose | pages [5] -->
benefit-cost curves. Demand and expenditure can be modeled as strictly convex functions with tunable parameters, whereas revenue is fitted via concave functions to reflect diminishing returns.

<!-- b000412 | prose | pages [5] -->
Assumption 2: Hidden costs (e.g., infrastructure strain, carbon footprint) are monetize in USD.

<!-- b000413 | prose | pages [5] -->
Justification: This provides dimensional consistency for quantitative analysis. Environmental economics employs shadow pricing for such conversions—for instance, carbon trading market rates or public facility maintenance costs can quantify ecological impacts. Empirical carbon pricing frameworks (e.g., Carbon Border Adjustment Mechanism) validate this assumption’s practicality.

<!-- b000414 | prose | pages [5] -->
Assumption 3: Tourist spending or policy changes instantaneously affect visitor numbers.

<!-- b000415 | prose | pages [5, 6] -->
Justification: This assumes a full-information market, simplifying tourism’s inherent time-lag dynamics. While idealistic, it enables static Pareto-optimal equilibrium modeling. Deviations from reality are addressable via elasticity coefficients (e.g., price elasticity of demand)

<!-- b000416 | furniture | pages [6] -->
Team # 2502617

<!-- b000417 | furniture | pages [6] -->
Page 6 of 25

<!-- b000419 | prose | pages [6] -->
Assumption 4: Parameters are spatiotemporally localized, ignoring external competition, in- frastructure decay, or seasonal fluctuations.

<!-- b000420 | prose | pages [6] -->
Justification: Focusing on Juneau’s internal resource allocation efficiency, this supports short- term partial equilibrium analysis. Such simplification suits rapid policy pilot evaluations while acknowledging scope limitations.

<!-- b000421 | heading | pages [6] -->
3 Notations

<!-- b000422 | caption | pages [6] -->
Table 1: Variations and Parameters

<!-- b000423 | prose | pages [6] -->
Symbols Description Unit

<!-- b000424 | prose | pages [6] -->
Number of Tourists Millions Nt Number of Residents in Juneau Millions Nr Indexes of Decay Elasticity - ki(i = 0, 1, 2)

<!-- b000425 | heading | pages [6] -->
Economic Notations

<!-- b000426 | prose | pages [6] -->
Economic benefits USD E Consumption Generated by Tourists USD Ct Economic Revenues of Government USD CGi Economic Cost of Government USD CGc Economic Revenues of Residents USD CRi Infrastructure Costs USD Ci Fixed Expenditure Costs USD Cfix Basic Consumption per Tourist USD A0 Tax Rate % t

<!-- b000427 | heading | pages [6] -->
Social Notations

<!-- b000428 | prose | pages [6] -->
Social benefits USD S Virtual Economic Value Equivalent USD Cadd Generated by Unit of Social Satisfaction Incremental Cost of Residents’ Living USD CRc Hidden benefits from Social Satisfaction USD A1 Social Satisfaction - s Pressure on the Lives of Local Residents - Pl Congestion Pressure due to Increased Tourist Flow - Pf

<!-- b000429 | heading | pages [6] -->
Environmental Notations

<!-- b000430 | prose | pages [6] -->
Environmental benefits USD Env Government Expenditure on Environmental Governance USD Cenv Hidden Costs Arising Caused by Carbon Emissions USD CCO2 Virtual Costs Corresponding to a Unit of CO2 Emissions USD CperC Total CO2 Emissions ton ECO2 Average Carbon Emissions by Each Tourist ton γ Proportion of Tax to Improve the Environment - A2

<!-- b000431 | prose | pages [6, 7] -->
关注数学模型 Symbols V alue Notes Symbols V alue Notes

<!-- b000432 | furniture | pages [6] -->
2

<!-- b000433 | furniture | pages [6] -->
MATHmodels

<!-- b000434 | furniture | pages [6] -->
获取更多资讯

<!-- b000435 | furniture | pages [7] -->
Team # 2502617

<!-- b000436 | furniture | pages [7] -->
Page 7 of 25

<!-- b000437 | caption | pages [7] -->
Table 2: Value of Partial Parameters

<!-- b000439 | prose | pages [7] -->
from Statistic[16] 0.032 from Government 0.081 Nr γ 5 from Government 3000 from Government t A0 Estimate from Article[17] 0.0068 Estimate 5 k0 A1 0.3574 Estimate 0.03 from Government k1 A2 1.6000 Estimate k2

<!-- b000440 | prose | pages [7] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000441 | caption | pages [7] -->
Figure 3: Chart of Current Income and Expenditure

<!-- b000442 | prose | pages [7] -->
The symbols in Table 1 not mentioned in Table 2 and Figure 3 are all intermediate or decision variations used in model calculation.

<!-- b000443 | heading | pages [7] -->
4 Multi-Objective Optimization Model

<!-- b000444 | heading | pages [7] -->
4.1 Sub-model I: Cost-benefit Analysis Considering Marginal Effects

<!-- b000445 | prose | pages [7] -->
Economic benefits is the first core objective of local tourism development. An increase in the number of tourists not only promotes local economic growth and increases municipal revenues, but also provides more employment opportunities for local residents, thus raising their incomes. In addition, economic efficiency is a key factor in sustainable tourism management strategies. When the economic benefits are too low or the costs do not match the benefits, the local government may seek new economic growth points or even give up the continued development of tourism. Therefore, maximizing economic benefits should be the first objective function in the planning model.

<!-- b000446 | prose | pages [7] -->
Maximization of economic benefits can be expressed as follows:

<!-- b000447 | prose | pages [7] -->
(1) max E = CGi −CGc where CGi represents the visible economic revenues of the local government from the growth in the number of tourists, and CGc is the increase of the local government in the cost of infrastructure operation and maintenance and other public services due to the excessive number of tourists. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000448 | furniture | pages [7] -->
m

<!-- b000449 | furniture | pages [7] -->
m

<!-- b000450 | furniture | pages [7] -->
m

<!-- b000451 | furniture | pages [7] -->
m

<!-- b000452 | furniture | pages [7] -->
m

<!-- b000453 | furniture | pages [7] -->
m

<!-- b000454 | furniture | pages [7] -->
m

<!-- b000455 | furniture | pages [7] -->
m

<!-- b000456 | furniture | pages [7] -->
m

<!-- b000457 | furniture | pages [7] -->
m

<!-- b000458 | furniture | pages [7] -->
m

<!-- b000459 | furniture | pages [7] -->
m

<!-- b000460 | furniture | pages [7] -->
m

<!-- b000461 | furniture | pages [7] -->
m

<!-- b000462 | furniture | pages [7] -->
m

<!-- b000463 | furniture | pages [7] -->
m

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

<!-- b000772 | furniture | pages [8] -->
Team # 2502617

<!-- b000773 | furniture | pages [8] -->
Page 8 of 25

<!-- b000774 | heading | pages [8] -->
4.1.1 Analysis of Economic benefits

<!-- b000775 | prose | pages [8] -->
The direct consumption generated by tourists is most significantly influenced by the number of tourists, so it can be regarded as a linear function of the number of tourists (i.e., assuming that the expected spending per tourist remains constant over the course of a year). Therefore, the formula for calculating the direct consumption Ct generated by tourists is given by

<!-- b000776 | prose | pages [8] -->
(2) m m m m m m m m m m m m m m m m m m m m m m Ct = α × Nt m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m where α represents the average economic benefits per tourist, Nt represents the number of tourists, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and as the number of tourists increases, the benefits arising from consumption generated by tourists m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m exhibits diminishing marginal returns, meaning that α1 will decrease as Nt increases. The formula m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m for calculating α is as follows:

<!-- b000777 | prose | pages [8] -->
A0 (3) α = (1 + ek0A0Nt(t−tbasic))(1 + ek0(A0−A0max))

<!-- b000778 | prose | pages [8] -->
where A0 represents the basic per capita consumption, k0 represents the rate at which per capita consumption tends to saturate as the number of tourists increases, and t represents tax rate. The formula also reflects the tolerance of tourists to the increase of tax and average cost, and the attenuation will be further increased when the tax or average cost is greater than the threshold. By default, we consider t = tbasic, A0max = 1.5A0 A portion of the consumption generated by tourists during their trip is used to pay fees such as VAT on goods and hotel taxes levied by municipalities, while the other portion is used to purchase tourism-related goods and services provided by local residents. Therefore, we can get the following formula:

<!-- b000779 | prose | pages [8] -->
(4) Ct = CGi + CRi where CGi represents the portion of tourist spending that goes to municipal revenues, and CRi represents the revenues of tourist spending that accrue to residents engaged in the tourism industry. Government benefits and residents’ benefits can be expressed as follows:

<!-- b000780 | prose | pages [8] -->
( CGi = αNtt (5) CRi = αNt(1 −t)

<!-- b000781 | heading | pages [8] -->
4.1.2 Analysis of Economic Costs

<!-- b000782 | prose | pages [8] -->
The components of economic costs are more complex than economic revenues. On the one hand, the government of Juneau needs to invest a certain amount of fixed expenditures on public services every year, such as household garbage removal and sewage disposal, etc. On the other hand, the surge in the number of tourists has led to accelerated destruction of the infrastructure in Juneau, and the government has to invest more revenues in the construction and maintenance of the infrastructure. At the same time, the cruise ship traffic brings a large amount of carbon emissions, the government of Juneau needs to solve these challenges.

<!-- b000783 | prose | pages [8] -->
It is important to note that the economic costs are not strictly linear with the number of tourists. When the number of tourists is high, the rate of infrastructure damage may be faster, showing an

<!-- b000784 | prose | pages [8, 9] -->
关注数学模型 increasing trend of marginal costs at the level of government management costs. Therefore, in the economic cost analysis we fully consider the actual situation of increasing marginal cost and 微信公众号：数学模型 construct an economic cost analysis model.

<!-- b000785 | furniture | pages [8] -->
2

<!-- b000786 | furniture | pages [8] -->
MATHmodels

<!-- b000787 | furniture | pages [8] -->
获取更多资讯

<!-- b000788 | furniture | pages [9] -->
Team # 2502617

<!-- b000789 | furniture | pages [9] -->
Page 9 of 25

<!-- b000791 | prose | pages [9] -->
(6) CGc = CiN 2 t + Cfix where Ci represents the cost required for the operation and management of the infrastructure and Cfix is the fixed cost to be incurred by the government.

<!-- b000792 | prose | pages [9] -->
The additional tax revenues of the Government and a portion of municipal revenues are invested in public services, and a higher level of public services improves the satisfaction of local residents and tourists, thus contributing to the development of sustainable tourism.

<!-- b000793 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000794 | heading | pages [9] -->
4.1.3 Overall Economic Performance

<!-- b000795 | prose | pages [9] -->
As mentioned earlier, total economic efficiency E can be summarized as a composite variable reflecting the overall returns to economic activity. Considering the two key economic principles of diminishing marginal benefits and increasing marginal costs, it can be hypothesized that the government should have two break-even points. The break-even point is the point at which economic benefits equal economic costs, i.e. CGi = CGc, at which the government has neither a profit nor a loss.

<!-- b000796 | prose | pages [9] -->
The break-even point provides upper and lower thresholds for the number of tourists. As the number of tourists increases, the marginal benefit gradually decreases while the marginal cost gradually increases, resulting in the economic benefit turning negative after the breakeven point is exceeded.

<!-- b000797 | caption | pages [9] -->
Figure 4: Economic benefits - Schematic Cost-benefit Analysis

<!-- b000798 | prose | pages [9] -->
When the number of tourists exceeds this threshold, the marginal benefits from additional tourists are not sufficient to cover the increased costs, which in turn leads to a decline in economic benefits. The break-even point therefore provides the government with a range of acceptable tourist numbers beyond which measures need to be taken to avoid negative economic benefits.

<!-- b000799 | furniture | pages [10] -->
Team # 2502617

<!-- b000800 | furniture | pages [10] -->
Page 10 of 25

<!-- b000801 | heading | pages [10] -->
4.2 Sub-model II: Social Welfare Optimization Model

<!-- b000802 | prose | pages [10] -->
The social benefits is the second key objective that we analyze in our models. When the number of tourists is too high, local residents feel more pressure to live due to the increase in the cost of living, and at the same time, when the number of tourists far exceeds the number of local residents, the regional congestion rises and the social satisfaction of the residents decreases. On the contrary, when the number of tourists is too low, residents mainly engaged in the tourism service industry may feel an increase in life pressure due to a decrease in income.

<!-- b000803 | prose | pages [10] -->
Combining life stress and crowding, we can obtain the formula for the indicator measure of social satisfaction. Further, combining the historical data of Juneau, we analyze the virtual economic value equivalent that can be generated by a unit of social satisfaction, and calculate the economic benefits of social satisfaction metrics based on this. Ultimately, we can get the result of maximizing social benefits as follows (7) max S = s × Cadd where s represents overall social satisfaction and Cadd represents the hidden economic value equivalent that can be generated by a unit of life satisfaction.

<!-- b000804 | heading | pages [10] -->
4.2.1 Estimation of Social Satisfaction Indicator

<!-- b000805 | prose | pages [10] -->
In our model, residents’ social satisfaction is mainly determined by two mutually constraining factors: pressure on living and pressure on congestion. An increase in the number of tourists will both increase residents’ income and lead to an increase in residents’ cost of living. When the increase in residents’ cost of living exceeds the increment in income, residents’ life satisfaction will decrease. Since Juneau has fewer residents, it can be assumed that there is a significant linear relationship between congestion pressure and the number of tourists.

<!-- b000806 | prose | pages [10] -->
Pl = CRi    CRc  (8) Pf = Nr    Nt

<!-- b000807 | prose | pages [10] -->
where CRc represents the incremental cost of living to residents due to an increase in the number of tourists, which is considered as a constant since CRi reflects a decrease; and Nr is the number of residents in Juneau. Thus, the dimensionless indicator of social satisfaction s can be denoted as

<!-- b000808 | prose | pages [10] -->
(9) s = Pl × Pf

<!-- b000809 | heading | pages [10] -->
4.2.2 Monetized Conversion of Social Satisfaction

<!-- b000810 | prose | pages [10] -->
We use the virtual economic benefits generated by unit social satisfaction as an equivalent quantitative indicator to comprehensively analyze social satisfaction. Through the monetization transformation of social satisfaction, the quantitative outline of the sub-model can be further ensured to be unified, thus ensuring the model has better usability and comparability.

<!-- b000811 | prose | pages [10] -->
Specifically, the monetized conversion of social satisfaction indicators includes two steps. (1) the hidden economic benefit equivalent generated by the unit of social satisfaction; (2) the total

<!-- b000812 | prose | pages [10, 11] -->
关注数学模型 hidden economic benefit generated by social satisfaction.

<!-- b000813 | furniture | pages [10] -->
2

<!-- b000814 | furniture | pages [10] -->
MATHmodels

<!-- b000815 | furniture | pages [10] -->
获取更多资讯

<!-- b000816 | furniture | pages [11] -->
Team # 2502617

<!-- b000817 | furniture | pages [11] -->
Page 11 of 25

<!-- b000819 | prose | pages [11] -->
A1 (10) Cadd = 1 + e(Nt−k1Nr)t where A1 represents the hidden benefits derived from social satisfaction as equivalent quantitative metrics, which diminish when the number of tourists reaches a certain ratio k1 of the local population 微信公众号：数学模型 or when tax revenue increases.

<!-- b000820 | heading | pages [11] -->
4.2.3 Overall Social Performance

<!-- b000821 | prose | pages [11] -->
In Model II, we combine the stress of living in Juneau with the stress of overcrowding due to the growth in the number of tourists and obtain the social benefit equivalent by measuring satisfaction through a virtual economic value. Since satisfaction is judged differently by different groups, subject to the 2023 Statistic of Juneau[3], it can be assumed that the social benefits are in an acceptable range when more than 60%, of residents achieve a state of satisfaction.

<!-- b000822 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000823 | caption | pages [11] -->
Figure 5: Social benefits - Schematic Social Satisfaction Analysis

<!-- b000824 | prose | pages [11] -->
In 2023, Juneau reaches 1.67 million visitors and the reality of residents being dissatisfied with the excessive number of visitors arises. In this context, we take the social satisfaction in 2023 as the baseline social satisfaction and calculate the off between the number of tourists and social satisfaction. That is, when the social satisfaction satisfies S > 0.6 × S2023, the social benefit satisfies the constraint.

<!-- b000825 | heading | pages [11] -->
4.3 Sub-model III: Environmental Carrying Capacity Model

<!-- b000826 | prose | pages [11] -->
Minimizing environmental benefits is the third important objective in addition to maximizing economic and social benefits. Excessive numbers of tourists at any given time may result in the destruction of local natural and cultural resources due to insufficient carrying capacity. In addition, the airplanes, cruise ships, and other means of transportation used by tourists to travel to destinations such as Juneau can also lead to increased emissions of greenhouse gases such as carbon dioxide, which in turn leads to higher temperatures and glacier melting.

<!-- b000827 | furniture | pages [12] -->
Team # 2502617

<!-- b000828 | furniture | pages [12] -->
Page 12 of 25

<!-- b000829 | prose | pages [12] -->
Environmental damage has significant hidden economic costs for the tourism industry and increases potential government expenditures. In order to quantitatively assess the hidden economic costs of environmental damage, in the environmental benefit analysis, we accounted for the carbon footprint of attractions in the city of Juneau and conducted an economization analysis using the equivalent of economic growth per unit of carbon emissions. Specifically, the primary objectives and key analyses of economic benefits are shown below

<!-- b000830 | prose | pages [12] -->
(11) min Env = CCO2 −Cenv where, Cenv represents government expenditure on environmental governance, while Cco2 repre- sents the hidden costs arising from environmental degradation caused by carbon emissions. The difference between these two variables quantifies the magnitude of tourism’s environmental impact.

<!-- b000831 | heading | pages [12] -->
4.3.1 Carbon Footprint Accounting

<!-- b000832 | prose | pages [12] -->
Since the primary cause of glacier melt is temperature increase, the glacier recession equation summarized for assessing the recession of Mendenhall Glacier in Juneau is as follows m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ! ∆V 1 + ∆ECO2 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (12) m m m m m m m m m m m m m m m m m m = λ ln m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m V0 C0 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m where ECO2 represents the total carbon emissions from each scenic area in Juneau City, C0 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m represents the air carbon dioxide concentration in Juneau City in 2023, and λ represents the climate m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000833 | prose | pages [12] -->
sensitivity, which is usually taken as 0.8◦C/(W/m2).

<!-- b000834 | prose | pages [12] -->
It can be seen from the above equation that the retreat of Mendenhall glacier is mainly related to carbon emission. In addition, in order to prevent over-parameterization, this formula is only used to predict the melting rate of glacier, and it is not added to the environmental benefit evaluation model, but replaced by carbon emission.

<!-- b000835 | prose | pages [12] -->
In the process of carbon footprint accounting, we take into account that changes in the number of visitors to different attractions may lead to different carbon emissions, and analyze the carbon emissions of different attractions separately, so as to measure the impact of the growth in the number of visitors on the environment. According to the McKinsey Marginal Emission Reduction Curve[18], the carbon emissions from visitors to each attraction can be derived as follows

<!-- b000836 | prose | pages [12] -->
(13) Eci = γ × (riNt)2 where γ represents the average carbon emissions generated by each tourist, and ri represents the proportion of tourists visiting the i-th attraction out of the total number of tourists. According to the statistics[3], we think the value of r is {0.2, 0.2, 0.6}, among these, 0.6 is the proportion of tourists going to the glacier.

<!-- b000837 | prose | pages [12] -->
From this, the total carbon emissions from the sites in Juneau can be expressed as

<!-- b000838 | prose | pages [12] -->
(14) X Eco2 = Eci i where Eci represents the carbon emissions from managing the i-th tourist attraction, and the equation calculates the total decentralized carbon emissions Eco2 by taking the sum of the individual emission costs.

<!-- b000839 | prose | pages [12] -->
关注数学模型

<!-- b000840 | furniture | pages [12] -->
2

<!-- b000841 | furniture | pages [12] -->
MATHmodels

<!-- b000842 | furniture | pages [12] -->
获取更多资讯

<!-- b000843 | furniture | pages [13] -->
Team # 2502617

<!-- b000844 | furniture | pages [13] -->
Page 13 of 25

<!-- b000845 | heading | pages [13] -->
4.3.2 Monetization of Carbon Footprint

<!-- b000846 | prose | pages [13] -->
Municipal revenues increase when the number of tourists increases. However, environmental 微信公众号：数学模型 benefits decrease as CO2 emissions increase. To ensure the sustainability of tourism development at the attraction, the hidden environmental management costs of the municipality rise.

<!-- b000847 | prose | pages [13] -->
In the carbon footprint economic analysis model, for Cenv, we use tax to reflect the government’s additional revenue; for CCO2, firstly estimate the virtual cost equivalent per unit of carbon emissions, and then calculate the potential economic loss due to environmental pollution. Specifically, the model we use is shown below  A2t Cenv = Nt ·   (15) 1 + ek2t CCO2 = CperCECO2   where CperC represents the virtual economic cost corresponding to a unit of CO2 emissions, A2 微信号：MATHmodels represents the proportion of tax revenues used to improve the environment, and k2 represents the elasticity adjustment coefficient, which indicates that as tax revenues increase, their effect in environmental management tends to be saturated.

<!-- b000848 | heading | pages [13] -->
4.3.3 Overall Environmental Performance

<!-- b000849 | prose | pages [13] -->
The presented environmental impact model integrates two critical nonlinear dynamics to quan- tify tourism sustainability. The formulation exhibits a dual structure balancing government-led environmental investments against dispersed carbon emission costs. The environmental gover- nance component Cenv reflects diminishing returns on tax-funded ecological improvements as expenditures increase —— a mechanism preventing over-reliance on financial solutions.

<!-- b000850 | caption | pages [13] -->
Figure 6: Environmental benefits - Schematic Minimization of Environmental Impact Analysis

<!-- b000851 | prose | pages [13] -->
Conversely, the carbon cost aggregation CCO2 inherently penalizes concentrated tourism pat- terns through its quadratic summation structure. This mathematical design creates an optimization landscape where effective environmental management requires both strategic fiscal allocation and tourist flow distribution.

<!-- b000852 | furniture | pages [14] -->
Team # 2502617

<!-- b000853 | furniture | pages [14] -->
Page 14 of 25

<!-- b000854 | prose | pages [14] -->
The model’s nonlinear interactions emphasize that simply increasing environmental spending becomes progressively less effective, while carbon costs grow disproportionately with visitor con- centration, demanding balanced spatial-temporal management of tourism resources for sustainable outcomes.

<!-- b000855 | heading | pages [14] -->
4.4 Pareto Optimal Solution for Total benefit

<!-- b000856 | prose | pages [14] -->
From the analysis in the preceding three sections, expressions for economic, social, and en- vironmental benefits can be derived respectively. The total benefit is formulated as a weighted average of these three dimensions, yielding the following optimization objective:

<!-- b000857 | prose | pages [14] -->
max E = CGi −CGc    max S = s × Cadd   (16) min Env = Cco2 −Cenv    max T = ω1E + ω2S −ω3Env 

<!-- b000858 | prose | pages [14] -->
where ωi(i = 1, 2, 3) is the weight of three benefits.

<!-- b000859 | prose | pages [14] -->
Additionally, the constraints are formulated as follows:

<!-- b000860 | prose | pages [14] -->
 E > 0    S > Smin     (17) Env < 0 st.

<!-- b000861 | prose | pages [14] -->
T > 0      Ntmax > Nt > 0   where Ntmax denotes the maximum tourist capacity, which can be set to the 2023 tourist volume(i.e., 1.67 million); where Smin denotes the minimum social benefit that Juneau can sustain, based on the social benefit in 2023 and calculated using the parameters from 2023 according to the aforementioned formula.

<!-- b000862 | heading | pages [14] -->
4.4.1 Determination of Weight Value

<!-- b000863 | prose | pages [14] -->
The weights for economic, social, and environmental benefits are derived from state-level reference metrics: U.S. state GDP rankings[19], cost-of-living rankings by the Missouri Economic Research and Information Center (MERIC)[20], and Yale University’s state-level Environmental Performance Index (EPI) rankings[21]. This methodology assumes that a lower ranking (denoted as rki, which i means the i-th dimension) in a specific dimension indicates a greater demand for improvement in that dimension, thus justifying a higher assigned weight. For instance, the Alaska’s multidimensional rankings are expressed as rk = {47/50, 46/50, 43/50}.

<!-- b000864 | prose | pages [14] -->
It is crucial to emphasize that the relative interdimensional relationships are contingent upon state-specific contextual factors. This dependency thus necessitates the following weight method formulation:

<!-- b000865 | prose | pages [14] -->
rki (18) ωi = P rki where, the weights for the three dimensions (economic, social, and environmental) in the Alaska are calculated as ω = {0.346, 0.338, 0.316}, which can be approximated as those of Juneau, given its role as the state’s central hub for cruise tourism and primary data collection point.

<!-- b000866 | prose | pages [14] -->
关注数学模型

<!-- b000867 | furniture | pages [14] -->
2

<!-- b000868 | furniture | pages [14] -->
MATHmodels

<!-- b000869 | furniture | pages [14] -->
获取更多资讯

<!-- b000870 | furniture | pages [15] -->
Team # 2502617

<!-- b000871 | furniture | pages [15] -->
Page 15 of 25

<!-- b000872 | heading | pages [15] -->
4.4.2 Global Pareto Optimization in the Game between Scenic Spots

<!-- b000873 | prose | pages [15] -->
Economic, social and environmental benefits usually form a competitive relationship. This competition is typically influenced by multiple factors (e.g., the number of tourists and tax rates), and in the absence of coordinated mechanisms, natural game-theoretic interactions often lead to outcomes that deviate from Pareto Optimization, with strategic autonomy tending to converge toward suboptimal equilibria.

<!-- b000874 | prose | pages [15] -->
Specifically, by solving the Multi-Objective Programming Model using the SLSQP method, under the above constraints, we can obtain a Pareto optimal solution where the benefits are most reasonably allocated, and there is no room for improvement in the total benefit, which is the results 微信公众号：数学模型 of the Multi-Objective Programming Model.

<!-- b000875 | prose | pages [15] -->
Economic vs Social Trade-off Economic vs Environmental Trade-off Social vs Environmental Trade-off 5000 0 0 Environmental Benefit (Carbon Units) Environmental Benefit (Carbon Units) 1750 1000 4000 4000 Social Benefit (Index Score) 2000 2000 1500 2000 Environmental Benefit 3000 Economic Benefit 1250 3000 3000 Social Benefit 4000 4000 4000 1000 5000 2000 2000 750 6000 6000 6000 500 1000 7000 1000 250 8000 8000 8000 0 微信号：MATHmodels 0 250 500 750 1000 1250 1500 1750 2000 0 250 500 750 1000 1250 1500 1750 2000 0 1000 2000 3000 4000 5000 Economic Benefit (Million USD) Economic Benefit (Million USD) Social Benefit (Index Score)

<!-- b000876 | caption | pages [15] -->
Figure 7: Schematic Pareto Optimization Solving Procedure

<!-- b000877 | heading | pages [15] -->
5 Results and Extension

<!-- b000878 | heading | pages [15] -->
5.1 Optimization Objectives

<!-- b000879 | prose | pages [15] -->
In the model, we try to analyze and optimize the total maximization of benefits by finding the optimal number of tourists, in which the economic, social and environmental benefits are all within the acceptable domain are the main constraints in the optimization process.

<!-- b000880 | heading | pages [15] -->
5.2 Constraints Analysis

<!-- b000881 | prose | pages [15] -->
• Juneau 1.Economic Constraints Analysis: Taking into account the diminishing marginal benefit and increasing marginal cost effects brought about by the growth in the number of tourists, the acceptable number of tourists under economic constraints can be derived. When the economic benefit is greater than 0, the economic benefit is acceptable. The economic constraint fully takes into account the effects of tourist spending, tax rates and other factors, and is able to reflect the additional revenue generated by tourism development.

<!-- b000882 | prose | pages [15, 16] -->
2.Social Constraints Analysis: When the number of tourists increases, the income of the residents will increase, but the cost of living necessities, such as rent, food and beverage, will likewise rise. At the same time, when the number of tourists is too high, residents may be dissatisfied with the reduced convenience of social services due to crowding. The acceptable number of tourists under social constraints can be derived. Based on empirical data, the social benefits are acceptable when more than 60% of the residents are satisfied with the standard.

<!-- b000883 | furniture | pages [16] -->
Team # 2502617

<!-- b000884 | furniture | pages [16] -->
Page 16 of 25

<!-- b000886 | prose | pages [16] -->
3.Environmental Constraints Analysis: Since the maximum carrying capacity of the envi- ronment is limited, when the number of tourists is too high or the distribution of tourists is too centralized, the possibility of environmental damage increases, which leads to adverse effects. In addition, tourists traveling by cruise ships, airplanes and other means of transportation will produce a certain carbon footprint. Accordingly, the acceptable number of tourists under environmental constraints can be derived.

<!-- b000887 | caption | pages [16] -->
Figure 8: Tourist-Constraint Stringency Heatmap

<!-- b000888 | prose | pages [16] -->
• Jiuzhaigou As a tourist city that also uses natural resources as its main attraction, Jiuzhaigou’s constraints m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to sustainable tourism development are roughly the same as those of Juneau. However, unlike the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m better economic benefit of Juneau, Jiuzhaigou is much more influenced by economic benefit in its m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m development and less influenced by environment benefit due to the temperate, therefore need give m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m more consideration to economic constraints and more consideration to environment constraints.the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m initial weighting parameters were adjusted to w = {0.625, 0.313, 0.062}. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000889 | heading | pages [16] -->
5.3 Optimization Result Analysis

<!-- b000890 | prose | pages [16] -->
• Juneau 1.Optimal Number of Tourists: We traverse the number of tourists in the range of 0-10 million, and through the coupled analysis of social, economic, and environmental benefits, we conclude that the total benefits is maximized when the total number of tourists is 1.32 million.

<!-- b000891 | prose | pages [16] -->
2.Global Pareto Optimization: The maximum total benefits T is about 8 million when considering only the changes in the decision variables, at which point the net income (Ct −Cgc) is 576 million dollars and the total performance (E + S −Env, means the direct sum of each benefit, representing the total benefit, used to measure the overall benefit; while weighted T used for optimization) is about 15 million. The optimal solution where the benefit first increases and then decreases with the number of tourists is shown in Figure 9, which is obviously in line with reality.

<!-- b000892 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型 10 0 Economic Benefit Social Benefit 7 Positive Benefit Area Positive Benefit Area Negative Impact Area Negative Impact Area 25 0 6 50 5 Environmental Benefit Economic Benefit 10 Social Benefit 4 75 20 3 100 2 30 125 1 Environmental Benefit 150 Negative Benefit Area 40 0 Positive Impact Area 0 2 4 6 8 10 0 2 4 6 8 10 0 2 4 6 8 10 Nt Nt Nt 1.0 0.3 20 Benefit Increase Velocity Net Income Increase Velocity Performance Increase Velocity 0 0 500 0.8 10 15 0.2 0 0.6 50 20 10 500 30 0.4 0.1 100 40 1000 5 0.2 微信号：MATHmodels 50 0.0 1500 0.0 150 0 60 2000 0.2 0.1 70 Total Performance Total Benefit Net Income 5 200 2500 0 2 4 6 8 10 0 2 4 6 8 10 0 2 4 6 8 10 Nt Nt Nt

<!-- b000893 | furniture | pages [16] -->
2

<!-- b000894 | furniture | pages [16] -->
MATHmodels

<!-- b000895 | furniture | pages [16] -->
获取更多资讯

<!-- b000896 | furniture | pages [17] -->
Team # 2502617

<!-- b000897 | furniture | pages [17] -->
Page 17 of 25

<!-- b000899 | caption | pages [17] -->
Figure 9: Optimization Results - Juneau

<!-- b000900 | prose | pages [17] -->
• Jiuzhaigou In the process of optimization for Jiuzhaigou, the selection of key parameters is basically the same as that of Juneau, but some parameters have been adjusted according to national conditions and environmental changes. According to China’s value-added tax rate, t=13% of Jiuzhaigou; while the other two key parameters are considered to be approximately the same as Juneau’s.

<!-- b000901 | prose | pages [17] -->
50 0 Social Benefit 50 Positive Benefit Area 0 Negative Impact Area 100 40 50 Environmental Benefit 200 100 Economic Benefit 30 Social Benefit 150 300 20 200 400 250 10 500 Economic Benefit Environmental Benefit 300 Positive Benefit Area Negative Benefit Area 0 Negative Impact Area Positive Impact Area 350 600 0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30 Nt Nt Nt 15 Benefit Increase Velocity Net Income Increase Velocity Performance Increase Velocity 1.0 1.5 0 0 0 10 0.8 1.0 200 0.6 2000 5 50 0.5 0.4 0 400 100 4000 0.0 0.2 5 150 0.0 600 0.5 6000 10 0.2 200 1.0 800 8000 15 0.4 Total Performance Total Benefit Net Income 1.5 250 0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30 Nt Nt Nt

<!-- b000902 | caption | pages [17] -->
Figure 10: Optimization Results - Jiuzhaigou

<!-- b000903 | prose | pages [17] -->
1.Optimal Number of Tourists: We traverse the number of tourists in the range of 0-10 million, and through the coupled analysis of social, economic, and environmental benefits, we conclude that the total benefits are maximized when the total number of tourists is 3.32 million.

<!-- b000904 | prose | pages [17, 18] -->
2.Global Pareto Optimization: The maximum total benefits T (total benefits of the municipal sector) is 37 million when considering only the changes in the decision variables, at which point m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the net economic is 743 million dollars.

<!-- b000905 | furniture | pages [17] -->
m

<!-- b000906 | furniture | pages [17] -->
m

<!-- b000907 | furniture | pages [17] -->
m

<!-- b000908 | furniture | pages [17] -->
m

<!-- b000909 | furniture | pages [17] -->
m

<!-- b000910 | furniture | pages [17] -->
m

<!-- b000911 | furniture | pages [17] -->
m

<!-- b000912 | furniture | pages [17] -->
m

<!-- b000913 | furniture | pages [17] -->
m

<!-- b000914 | furniture | pages [17] -->
m

<!-- b000915 | furniture | pages [17] -->
m

<!-- b000916 | furniture | pages [17] -->
m

<!-- b000917 | furniture | pages [17] -->
m

<!-- b000918 | furniture | pages [17] -->
m

<!-- b000919 | furniture | pages [17] -->
m

<!-- b000920 | furniture | pages [17] -->
m

<!-- b000921 | furniture | pages [17] -->
m

<!-- b000922 | furniture | pages [17] -->
m

<!-- b000923 | furniture | pages [17] -->
m

<!-- b000924 | furniture | pages [17] -->
m

<!-- b000925 | furniture | pages [17] -->
m

<!-- b000926 | furniture | pages [17] -->
m

<!-- b000927 | furniture | pages [17] -->
m

<!-- b000928 | furniture | pages [17] -->
m

<!-- b000929 | furniture | pages [17] -->
m

<!-- b000930 | furniture | pages [17] -->
m

<!-- b000931 | furniture | pages [17] -->
m

<!-- b000932 | furniture | pages [17] -->
m

<!-- b000933 | furniture | pages [17] -->
m

<!-- b000934 | furniture | pages [17] -->
m

<!-- b000935 | furniture | pages [17] -->
m

<!-- b000936 | furniture | pages [17] -->
m

<!-- b000937 | furniture | pages [17] -->
m

<!-- b000938 | furniture | pages [17] -->
m

<!-- b000939 | furniture | pages [17] -->
m

<!-- b000940 | furniture | pages [17] -->
m

<!-- b000941 | furniture | pages [17] -->
m

<!-- b000942 | furniture | pages [17] -->
m

<!-- b000943 | furniture | pages [17] -->
m

<!-- b000944 | furniture | pages [17] -->
m

<!-- b000945 | furniture | pages [17] -->
m

<!-- b000946 | furniture | pages [17] -->
m

<!-- b000947 | furniture | pages [17] -->
m

<!-- b000948 | furniture | pages [17] -->
m

<!-- b000949 | furniture | pages [17] -->
m

<!-- b000950 | furniture | pages [17] -->
m

<!-- b000951 | furniture | pages [17] -->
m

<!-- b000952 | furniture | pages [17] -->
m

<!-- b000953 | furniture | pages [17] -->
m

<!-- b000954 | furniture | pages [17] -->
m

<!-- b000955 | furniture | pages [17] -->
m

<!-- b000956 | furniture | pages [17] -->
m

<!-- b000957 | furniture | pages [17] -->
m

<!-- b000958 | furniture | pages [17] -->
m

<!-- b000959 | furniture | pages [17] -->
m

<!-- b000960 | furniture | pages [17] -->
m

<!-- b000961 | furniture | pages [17] -->
m

<!-- b000962 | furniture | pages [17] -->
m

<!-- b000963 | furniture | pages [17] -->
m

<!-- b000964 | furniture | pages [17] -->
m

<!-- b000965 | furniture | pages [17] -->
m

<!-- b000966 | furniture | pages [17] -->
m

<!-- b000967 | furniture | pages [17] -->
m

<!-- b000968 | furniture | pages [17] -->
m

<!-- b000969 | furniture | pages [17] -->
m

<!-- b000970 | furniture | pages [17] -->
m

<!-- b000971 | furniture | pages [17] -->
m

<!-- b000972 | furniture | pages [17] -->
m

<!-- b000973 | furniture | pages [17] -->
m

<!-- b000974 | furniture | pages [17] -->
m

<!-- b000975 | furniture | pages [17] -->
m

<!-- b000976 | furniture | pages [17] -->
m

<!-- b000977 | furniture | pages [17] -->
m

<!-- b000978 | furniture | pages [17] -->
m

<!-- b000979 | furniture | pages [17] -->
m

<!-- b000980 | furniture | pages [17] -->
m

<!-- b000981 | furniture | pages [17] -->
m

<!-- b000982 | furniture | pages [17] -->
m

<!-- b000983 | furniture | pages [17] -->
m

<!-- b000984 | furniture | pages [17] -->
m

<!-- b000985 | furniture | pages [17] -->
m

<!-- b000986 | furniture | pages [17] -->
m

<!-- b000987 | furniture | pages [17] -->
m

<!-- b000988 | furniture | pages [17] -->
m

<!-- b000989 | furniture | pages [17] -->
m

<!-- b000990 | furniture | pages [17] -->
m

<!-- b000991 | furniture | pages [17] -->
m

<!-- b000992 | furniture | pages [17] -->
m

<!-- b000993 | furniture | pages [17] -->
m

<!-- b000994 | furniture | pages [17] -->
m

<!-- b000995 | furniture | pages [17] -->
m

<!-- b000996 | furniture | pages [17] -->
m

<!-- b000997 | furniture | pages [17] -->
m

<!-- b000998 | furniture | pages [17] -->
m

<!-- b000999 | furniture | pages [17] -->
m

<!-- b001000 | furniture | pages [17] -->
m

<!-- b001001 | furniture | pages [17] -->
m

<!-- b001002 | furniture | pages [17] -->
m

<!-- b001003 | furniture | pages [17] -->
m

<!-- b001004 | furniture | pages [17] -->
m

<!-- b001005 | furniture | pages [17] -->
m

<!-- b001006 | furniture | pages [17] -->
m

<!-- b001007 | furniture | pages [17] -->
m

<!-- b001008 | furniture | pages [17] -->
m

<!-- b001009 | furniture | pages [17] -->
m

<!-- b001010 | furniture | pages [17] -->
m

<!-- b001011 | furniture | pages [17] -->
m

<!-- b001012 | furniture | pages [17] -->
m

<!-- b001013 | furniture | pages [17] -->
m

<!-- b001014 | furniture | pages [17] -->
m

<!-- b001015 | furniture | pages [17] -->
m

<!-- b001016 | furniture | pages [17] -->
m

<!-- b001017 | furniture | pages [17] -->
m

<!-- b001018 | furniture | pages [17] -->
m

<!-- b001019 | furniture | pages [17] -->
m

<!-- b001020 | furniture | pages [17] -->
m

<!-- b001021 | furniture | pages [17] -->
m

<!-- b001022 | furniture | pages [17] -->
m

<!-- b001023 | furniture | pages [17] -->
m

<!-- b001024 | furniture | pages [17] -->
m

<!-- b001025 | furniture | pages [17] -->
m

<!-- b001026 | furniture | pages [17] -->
m

<!-- b001027 | furniture | pages [17] -->
m

<!-- b001028 | furniture | pages [17] -->
m

<!-- b001029 | furniture | pages [17] -->
m

<!-- b001030 | furniture | pages [17] -->
m

<!-- b001031 | furniture | pages [17] -->
m

<!-- b001032 | furniture | pages [17] -->
m

<!-- b001033 | furniture | pages [17] -->
m

<!-- b001034 | furniture | pages [17] -->
m

<!-- b001035 | furniture | pages [17] -->
m

<!-- b001036 | furniture | pages [17] -->
m

<!-- b001037 | furniture | pages [17] -->
m

<!-- b001038 | furniture | pages [17] -->
m

<!-- b001039 | furniture | pages [17] -->
m

<!-- b001040 | furniture | pages [17] -->
m

<!-- b001041 | furniture | pages [17] -->
m

<!-- b001042 | furniture | pages [17] -->
m

<!-- b001043 | furniture | pages [17] -->
m

<!-- b001044 | furniture | pages [17] -->
m

<!-- b001045 | furniture | pages [17] -->
m

<!-- b001046 | furniture | pages [17] -->
m

<!-- b001047 | furniture | pages [17] -->
m

<!-- b001048 | furniture | pages [17] -->
m

<!-- b001049 | furniture | pages [17] -->
m

<!-- b001050 | furniture | pages [17] -->
m

<!-- b001051 | furniture | pages [17] -->
m

<!-- b001052 | furniture | pages [17] -->
m

<!-- b001053 | furniture | pages [17] -->
m

<!-- b001054 | furniture | pages [17] -->
m

<!-- b001055 | furniture | pages [17] -->
m

<!-- b001056 | furniture | pages [17] -->
m

<!-- b001057 | furniture | pages [17] -->
m

<!-- b001058 | furniture | pages [17] -->
m

<!-- b001059 | furniture | pages [17] -->
m

<!-- b001060 | furniture | pages [17] -->
m

<!-- b001061 | furniture | pages [17] -->
m

<!-- b001062 | furniture | pages [17] -->
m

<!-- b001063 | furniture | pages [17] -->
m

<!-- b001064 | furniture | pages [17] -->
m

<!-- b001065 | furniture | pages [17] -->
m

<!-- b001066 | furniture | pages [17] -->
m

<!-- b001067 | furniture | pages [17] -->
m

<!-- b001068 | furniture | pages [17] -->
m

<!-- b001069 | furniture | pages [17] -->
m

<!-- b001070 | furniture | pages [17] -->
m

<!-- b001071 | furniture | pages [17] -->
m

<!-- b001072 | furniture | pages [17] -->
m

<!-- b001073 | furniture | pages [17] -->
m

<!-- b001074 | furniture | pages [17] -->
m

<!-- b001075 | furniture | pages [17] -->
m

<!-- b001076 | furniture | pages [17] -->
m

<!-- b001077 | furniture | pages [17] -->
m

<!-- b001078 | furniture | pages [17] -->
m

<!-- b001079 | furniture | pages [17] -->
m

<!-- b001080 | furniture | pages [17] -->
m

<!-- b001081 | furniture | pages [17] -->
m

<!-- b001082 | furniture | pages [17] -->
m

<!-- b001083 | furniture | pages [17] -->
m

<!-- b001084 | furniture | pages [17] -->
m

<!-- b001085 | furniture | pages [17] -->
m

<!-- b001086 | furniture | pages [17] -->
m

<!-- b001087 | furniture | pages [17] -->
m

<!-- b001088 | furniture | pages [17] -->
m

<!-- b001089 | furniture | pages [17] -->
m

<!-- b001090 | furniture | pages [17] -->
m

<!-- b001091 | furniture | pages [17] -->
m

<!-- b001092 | furniture | pages [17] -->
m

<!-- b001093 | furniture | pages [17] -->
m

<!-- b001094 | furniture | pages [17] -->
m

<!-- b001095 | furniture | pages [17] -->
m

<!-- b001096 | furniture | pages [17] -->
m

<!-- b001097 | furniture | pages [17] -->
m

<!-- b001098 | furniture | pages [17] -->
m

<!-- b001099 | furniture | pages [17] -->
m

<!-- b001100 | furniture | pages [17] -->
m

<!-- b001101 | furniture | pages [17] -->
m

<!-- b001102 | furniture | pages [17] -->
m

<!-- b001103 | furniture | pages [17] -->
m

<!-- b001104 | furniture | pages [17] -->
m

<!-- b001105 | furniture | pages [17] -->
m

<!-- b001106 | furniture | pages [17] -->
m

<!-- b001107 | furniture | pages [17] -->
m

<!-- b001108 | furniture | pages [17] -->
m

<!-- b001109 | furniture | pages [17] -->
m

<!-- b001110 | furniture | pages [17] -->
m

<!-- b001111 | furniture | pages [17] -->
m

<!-- b001112 | furniture | pages [17] -->
m

<!-- b001113 | furniture | pages [17] -->
m

<!-- b001114 | furniture | pages [17] -->
m

<!-- b001115 | furniture | pages [17] -->
m

<!-- b001116 | furniture | pages [17] -->
m

<!-- b001117 | furniture | pages [17] -->
m

<!-- b001118 | furniture | pages [17] -->
m

<!-- b001119 | furniture | pages [17] -->
m

<!-- b001120 | furniture | pages [17] -->
m

<!-- b001121 | furniture | pages [17] -->
m

<!-- b001122 | furniture | pages [17] -->
m

<!-- b001123 | furniture | pages [17] -->
m

<!-- b001124 | furniture | pages [17] -->
m

<!-- b001125 | furniture | pages [17] -->
m

<!-- b001126 | furniture | pages [17] -->
m

<!-- b001127 | furniture | pages [17] -->
m

<!-- b001128 | furniture | pages [17] -->
m

<!-- b001129 | furniture | pages [17] -->
m

<!-- b001130 | furniture | pages [17] -->
m

<!-- b001131 | furniture | pages [17] -->
m

<!-- b001132 | furniture | pages [17] -->
m

<!-- b001133 | furniture | pages [17] -->
m

<!-- b001134 | furniture | pages [17] -->
m

<!-- b001135 | furniture | pages [17] -->
m

<!-- b001136 | furniture | pages [17] -->
m

<!-- b001137 | furniture | pages [17] -->
m

<!-- b001138 | furniture | pages [17] -->
m

<!-- b001139 | furniture | pages [17] -->
m

<!-- b001140 | furniture | pages [17] -->
m

<!-- b001141 | furniture | pages [17] -->
m

<!-- b001142 | furniture | pages [17] -->
m

<!-- b001143 | furniture | pages [17] -->
m

<!-- b001144 | furniture | pages [17] -->
m

<!-- b001145 | furniture | pages [17] -->
m

<!-- b001146 | furniture | pages [17] -->
m

<!-- b001147 | furniture | pages [17] -->
m

<!-- b001148 | furniture | pages [17] -->
m

<!-- b001149 | furniture | pages [17] -->
m

<!-- b001150 | furniture | pages [17] -->
m

<!-- b001151 | furniture | pages [17] -->
m

<!-- b001152 | furniture | pages [17] -->
m

<!-- b001153 | furniture | pages [17] -->
m

<!-- b001154 | furniture | pages [17] -->
m

<!-- b001155 | furniture | pages [17] -->
m

<!-- b001156 | furniture | pages [17] -->
m

<!-- b001157 | furniture | pages [17] -->
m

<!-- b001158 | furniture | pages [17] -->
m

<!-- b001159 | furniture | pages [17] -->
m

<!-- b001160 | furniture | pages [17] -->
m

<!-- b001161 | furniture | pages [17] -->
m

<!-- b001162 | furniture | pages [17] -->
m

<!-- b001163 | furniture | pages [17] -->
m

<!-- b001164 | furniture | pages [17] -->
m

<!-- b001165 | furniture | pages [17] -->
m

<!-- b001166 | furniture | pages [17] -->
m

<!-- b001167 | furniture | pages [17] -->
m

<!-- b001168 | furniture | pages [17] -->
m

<!-- b001169 | furniture | pages [17] -->
m

<!-- b001170 | furniture | pages [17] -->
m

<!-- b001171 | furniture | pages [17] -->
m

<!-- b001172 | furniture | pages [17] -->
m

<!-- b001173 | furniture | pages [17] -->
m

<!-- b001174 | furniture | pages [17] -->
m

<!-- b001175 | furniture | pages [17] -->
m

<!-- b001176 | furniture | pages [17] -->
m

<!-- b001177 | furniture | pages [17] -->
m

<!-- b001178 | furniture | pages [17] -->
m

<!-- b001179 | furniture | pages [17] -->
m

<!-- b001180 | furniture | pages [17] -->
m

<!-- b001181 | furniture | pages [17] -->
m

<!-- b001182 | furniture | pages [17] -->
m

<!-- b001183 | furniture | pages [17] -->
m

<!-- b001184 | furniture | pages [17] -->
m

<!-- b001185 | furniture | pages [17] -->
m

<!-- b001186 | furniture | pages [17] -->
m

<!-- b001187 | furniture | pages [17] -->
m

<!-- b001188 | furniture | pages [17] -->
m

<!-- b001189 | furniture | pages [17] -->
m

<!-- b001190 | furniture | pages [17] -->
m

<!-- b001191 | furniture | pages [17] -->
m

<!-- b001192 | furniture | pages [17] -->
m

<!-- b001193 | furniture | pages [17] -->
m

<!-- b001194 | furniture | pages [17] -->
m

<!-- b001195 | furniture | pages [17] -->
m

<!-- b001196 | furniture | pages [17] -->
m

<!-- b001197 | furniture | pages [17] -->
m

<!-- b001198 | furniture | pages [17] -->
m

<!-- b001199 | furniture | pages [17] -->
m

<!-- b001200 | furniture | pages [17] -->
m

<!-- b001201 | furniture | pages [17] -->
m

<!-- b001202 | furniture | pages [17] -->
m

<!-- b001203 | furniture | pages [17] -->
m

<!-- b001204 | furniture | pages [17] -->
m

<!-- b001205 | furniture | pages [17] -->
m

<!-- b001206 | furniture | pages [17] -->
m

<!-- b001207 | furniture | pages [17] -->
m

<!-- b001208 | furniture | pages [17] -->
m

<!-- b001209 | furniture | pages [17] -->
m

<!-- b001210 | furniture | pages [17] -->
m

<!-- b001211 | furniture | pages [17] -->
m

<!-- b001212 | furniture | pages [17] -->
m

<!-- b001213 | furniture | pages [17] -->
m

<!-- b001214 | furniture | pages [17] -->
m

<!-- b001215 | furniture | pages [17] -->
m

<!-- b001216 | furniture | pages [17] -->
m

<!-- b001217 | furniture | pages [17] -->
m

<!-- b001218 | furniture | pages [17] -->
m

<!-- b001219 | furniture | pages [17] -->
m

<!-- b001220 | furniture | pages [17] -->
m

<!-- b001221 | furniture | pages [17] -->
m

<!-- b001222 | furniture | pages [17] -->
m

<!-- b001223 | furniture | pages [17] -->
m

<!-- b001224 | furniture | pages [17] -->
m

<!-- b001225 | furniture | pages [17] -->
m

<!-- b001226 | furniture | pages [17] -->
m

<!-- b001227 | furniture | pages [17] -->
m

<!-- b001228 | furniture | pages [17] -->
m

<!-- b001229 | furniture | pages [18] -->
Team # 2502617

<!-- b001230 | furniture | pages [18] -->
Page 18 of 25

<!-- b001232 | prose | pages [18] -->
From the Figure 9 and Figure 10, it can be observed that the overall trend of benefits changes is approximately similar, which reflects the good scalability of the model. However, due to the extremely small weight of environmental benefits in Jiuzhaigou, its value is much lower than that of Juneau. This also reflects Jiuzhaigou’s selective neglect of environmental benefits in its pursuit of economic gains, reflecting the differences between different cities.

<!-- b001233 | heading | pages [18] -->
5.4 Key Parameter Determination

<!-- b001234 | prose | pages [18] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001235 | prose | pages [18] -->
• Juneau m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1.Proportion of Tourist(rglacier):The degree of dispersion of tourists reflects the ratio of the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m actual number of tourists accommodated in different scenic spots, Juneau Tourism Bureau website m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m statistics show that more than 60% of tourists to Juneau City will go to Mendenhall Glacier. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001236 | prose | pages [18] -->
2.Tax Rate(t): Based on the data of various local tax rates published on the official website of the Juneau City Government, combined with the data of the total income generated by the tourism industry in Juneau and the municipal economic income, the comprehensive tax rate for tourists during their travel in Juneau is calculated to be 5%.

<!-- b001237 | prose | pages [18] -->
3.Visitor Consumption(A0):Visitor Consumption reflects the cost of food, lodging, excursions, and souvenir purchases incurred by tourists during their visit to the City of Juneau. In short, tourist consumption reflects to some extent the prices of scenic spots and local life.

<!-- b001238 | prose | pages [18] -->
Related images of changes in visitor numbers and total benefits when each key factor changes are in the section Sensitivity Analysis.

<!-- b001239 | prose | pages [18] -->
• Jiuzhaigou

<!-- b001240 | caption | pages [18] -->
Figure 11: Changes of Total Tourists and Performance per Tourist in Jiuzhaigou

<!-- b001241 | prose | pages [18] -->
(Performance per Tourist is short for Performance)

<!-- b001242 | prose | pages [18] -->
From Figure 11, the following observations can be made: (1) When the proportion of tourists visiting Jiuzhaigou valley (r) is approximately equal to the proportion visiting other attractions, the optimal total benefit corresponds to the maximum tourist volume and maximum performance. This indicates that maintaining diversion measures is beneficial for sustainable tourism. (2) As tax rates (t) increase, the additional expenditure for tourists also rises, leading to a reduction in the number of tourists required to achieve optimal performance. Meanwhile, performance itself increases. (3) The effect of increased tourist expenditure is similar to that of increasing t; however, due to diminishing marginal benefits, the graph exhibits an inflection point.

<!-- b001243 | prose | pages [18, 19] -->
关注数学模型 The total benefit of the first two graphs in Figure 12 is proportional to the tourist volume(Nt), while the third graph is similar to the shape of performance. It can be concluded that the influence of performance increases while the Nt decreases with the increase in Tourist Consumption(A0). This is in line with objective reality; At the same time, it can be seen that T generated by the optimal Nt is slightly different when different key parameters change, which provides convenience for the manager's top placement policy. S

<!-- b001244 | furniture | pages [18] -->
2

<!-- b001245 | furniture | pages [18] -->
MATHmodels

<!-- b001246 | furniture | pages [18] -->
获取更多资讯

<!-- b001247 | furniture | pages [19] -->
Team#2502617

<!-- b001248 | furniture | pages [19] -->
Page 19 of 25

<!-- b001249 | caption | pages [19] -->
Figure 12: Changes of Total benefit in Jiuzhaigou

<!-- b001251 | prose | pages [19] -->
Additional Income and Expenditure Plan 6

<!-- b001252 | prose | pages [19] -->
• Sources of Additional Revenue:

<!-- b001253 | prose | pages [19] -->
Additional revenue is the revenue generated when the number of visitors changes. The main sources of additional revenue mainly include:

<!-- b001254 | heading | pages [19] -->
1. Direct economic income from consumption behavior occurring among tourists. Direct

<!-- b001255 | prose | pages [19] -->
economic income is reflected in municipal economic benefits through two channels of tax. One is the rate of VAT and hotel tax paid by tourists when they spend; rather, it is the rise in the amount of personal income tax brought about by the increase in residents' income.

<!-- b001256 | heading | pages [19] -->
2. Hidden sociol benefits generated when the number of tourists decreases. Hidden social

<!-- b001257 | prose | pages [19] -->
benefits is reflected through the monetized equivalent of social satisfaction, and Hidden social benefits will bring the government some economic gains in the long run.

<!-- b001258 | prose | pages [19] -->
• Revenue Expenditure Plan:

<!-- b001259 | prose | pages [19] -->
In order to achieve sustainable development of the tourism industry, the government needs to for- mulate a reasonable additional revenue expenditure plan. Specifically, the elements of expenditure that the government can adjust include the following:

<!-- b001260 | prose | pages [19] -->
1.Infrastructure management and operation expenditure. Infrastructure, including public build- ing construction and maintenance costs, urban pipeline maintenance fees, etc. A reasonable increase in infrastructure management and maintenance expenditures within a certain range can effectively improve social satisfaction and bring higher social benefits.

<!-- b001261 | prose | pages [19] -->
2.Environmental maintenance expenditure. Before environmental damage occurs, the gov- ernment needs to set aside and spend on environmental maintenance in advance. The increase of environmental maintenance expenses can improve the carrying capacity of the environment, promote the sustainable development of tourism, and then improve the total benefits.

<!-- b001262 | prose | pages [19, 20] -->
3.Expenditures on the management of environmental damage. This expenditure is a potential economic expenditure. The government must take this item into account in its revenue and expenditure plan, carefully assess the probability of environmental damage, and prevent the chain reaction caused by reduced environmental benefits.

<!-- b001263 | furniture | pages [20] -->
Team # 2502617

<!-- b001264 | furniture | pages [20] -->
Page 20 of 25

<!-- b001266 | heading | pages [20] -->
7 Sensitivity Analysis

<!-- b001267 | heading | pages [20] -->
7.1 Effect of Changes in Total Tourists and Performance per Tourist

<!-- b001268 | prose | pages [20] -->
In the model sensitivity analysis, we mainly analyzed the effects of small perturbations in the proportion of tourists, tax rate and tourist consumption, on the total number of tourists and total benefits. The results of the sensitivity analysis are shown in Figures 13 and 14.

<!-- b001269 | caption | pages [20] -->
Figure 13: Sensitivity Analysis - Changes of Total Tourists and Performance per Tourist

<!-- b001270 | prose | pages [20] -->
The conclusions that can be drawn from the two graphs on the left are that (1) the greatest number of tourists visit the glacier when the proportion of tourists visiting the glacier is roughly equal to the proportion of tourists visiting the other attractions (2) the number of tourists required for optimal performance decreases further as the tax rate increases. These are roughly the same conclusions reached in the Jiuzhaigou analysis.

<!-- b001271 | prose | pages [20] -->
Compared to Jiuzhaigou, there is a big difference in Juno’s performance when the number of tourists changes. When tourist spending is below US$4,000, consumers view tourism expenses as a price inelastic product, so the number of tourists continues to increase, while the performance gen- erated per tourist shows a slow increase because the rate of diminishing marginal effects is smaller than the rate of rising tourist numbers. Subsequently, when spending per tourist exceeds $4,000, the sensitivity of tourists to price changes increases, and tourism expenditures are transformed into a price-elastic good, with the number of tourists decreasing sharply, the total benefits of the tourist attractions, and the performance generated per tourist decreasing in the same trend.

<!-- b001272 | heading | pages [20] -->
7.2 Effect of Changes in Total benefit

<!-- b001273 | caption | pages [20] -->
Figure 14: Sensitivity Analysis - Changes of Total benefit

<!-- b001274 | prose | pages [20, 21] -->
关注数学模型 In the sensitivity analysis of total benefits, the tax rate, tourist proportion, and tourist consump- 微信公众号：数学模型 tion were analyzed as key parameters. The results are as follows: (1) As the tourist proportion increases by 1% from 0, social, environmental, economic, and total benefits all increase due to a more balanced distribution of tourists. (2) As the tax rate increases by 1% from 5%, environmen- tal benefits rise, while economic, social, and total benefits decline. (3) As tourist consumption increases by 1.25% from 3,000 USD, economic and social benefits rise, environmental benefits decrease, and total benefits first increase and then decrease.

<!-- b001275 | furniture | pages [20] -->
2

<!-- b001276 | furniture | pages [20] -->
MATHmodels

<!-- b001277 | furniture | pages [20] -->
获取更多资讯

<!-- b001278 | furniture | pages [21] -->
Team # 2502617

<!-- b001279 | furniture | pages [21] -->
Page 21 of 25

<!-- b001281 | heading | pages [21] -->
8 Strengths and Weaknesses

<!-- b001282 | heading | pages [21] -->
8.1 Strengths

<!-- b001283 | prose | pages [21] -->
微信号：MATHmodels

<!-- b001284 | heading | pages [21] -->
1. Computational Feasibility:

<!-- b001285 | prose | pages [21] -->
The model employs Pareto-optimal solutions with nonlinear marginal effect formulations, ensuring theoretical rigor while balancing realism and numerical stability. By integrating economic, social, and ecological dimensions into a unified framework, Pareto optimization explicitly reveals trade-offs among these aspects, providing policymakers with systematic pathways for optimization.

<!-- b001286 | prose | pages [21] -->
2. Holistic Cost Internalization: Social policies and environmental impacts are consolidated into quantifiable metrics, translating hidden costs (e.g., carbon footprint, infrastructure strain) into monetary terms. This approach mitigates over-parameterization risks in multi-objective models.

<!-- b001287 | prose | pages [21] -->
3. Generalizability & Practicality: The framework is adaptable to other tourism destinations suffering from overtourism, demonstrating strong generalizability. Its visual outputs and sen- sitivity analyses align with empirical trends, accurately reflecting real-world requirements and policy constraints.

<!-- b001288 | heading | pages [21] -->
8.2 Weaknesses

<!-- b001289 | heading | pages [21] -->
1. Temporal Simplification: The model ignores time-lag effects in tourism’s response to policy

<!-- b001290 | prose | pages [21] -->
changes. While elasticity coefficients partially correct deviations, their calibration remains subjective. Delayed demand adjustments necessitate dynamic extensions, for example, time- series models for long-term impact analysis.

<!-- b001291 | heading | pages [21] -->
2. Spatiotemporal Narrowness: External competition, infrastructure decay, and seasonal fluctua-

<!-- b001292 | prose | pages [21] -->
tions are excluded, potentially inflating optimization results. Future iterations should incorporate regional linkage mechanisms (e.g., cross-border tourism flows, shared infrastructure costs) to enhance realism.

<!-- b001293 | heading | pages [21] -->
9 Conclusion

<!-- b001294 | prose | pages [21, 22] -->
The model provides a practical tool in places like Juneau, which balances simplicity with real-world applicabilityaddressing economic, society, and environmental benefit by hidden cost monetization . The fixed system approach allows quick policy solutions, matching the focus of cities on short-term budgets. Its strength lies in showing Pareto Optimization –— giving leaders clear metrics when managing tourism pressures. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m After expanding the model to Jiuzhaigou, China, although both locations are affected by overtourism, the measures adopted differ due to the distinct geographical attributes of the two areas. The model can well reflect the differences and similarities between the two places, and has good extensibility. Specific conclusion can be found in the table below:

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

<!-- b001333 | furniture | pages [21] -->
m

<!-- b001334 | furniture | pages [21] -->
m

<!-- b001335 | furniture | pages [21] -->
m

<!-- b001336 | furniture | pages [21] -->
m

<!-- b001337 | furniture | pages [21] -->
m

<!-- b001338 | furniture | pages [21] -->
m

<!-- b001339 | furniture | pages [21] -->
m

<!-- b001340 | furniture | pages [21] -->
m

<!-- b001341 | furniture | pages [21] -->
m

<!-- b001342 | furniture | pages [21] -->
m

<!-- b001343 | furniture | pages [21] -->
m

<!-- b001344 | furniture | pages [21] -->
m

<!-- b001345 | furniture | pages [21] -->
m

<!-- b001346 | furniture | pages [21] -->
m

<!-- b001347 | furniture | pages [21] -->
m

<!-- b001348 | furniture | pages [21] -->
m

<!-- b001349 | furniture | pages [21] -->
m

<!-- b001350 | furniture | pages [21] -->
m

<!-- b001351 | furniture | pages [21] -->
m

<!-- b001352 | furniture | pages [21] -->
m

<!-- b001353 | furniture | pages [21] -->
m

<!-- b001354 | furniture | pages [21] -->
m

<!-- b001355 | furniture | pages [21] -->
m

<!-- b001356 | furniture | pages [21] -->
m

<!-- b001357 | furniture | pages [21] -->
m

<!-- b001358 | furniture | pages [21] -->
m

<!-- b001359 | furniture | pages [21] -->
m

<!-- b001360 | furniture | pages [21] -->
m

<!-- b001361 | furniture | pages [21] -->
m

<!-- b001362 | furniture | pages [21] -->
m

<!-- b001363 | furniture | pages [21] -->
m

<!-- b001364 | furniture | pages [21] -->
m

<!-- b001365 | furniture | pages [21] -->
m

<!-- b001366 | furniture | pages [21] -->
m

<!-- b001367 | furniture | pages [21] -->
m

<!-- b001368 | furniture | pages [21] -->
m

<!-- b001369 | furniture | pages [21] -->
m

<!-- b001370 | furniture | pages [21] -->
m

<!-- b001371 | furniture | pages [21] -->
m

<!-- b001372 | furniture | pages [21] -->
m

<!-- b001373 | furniture | pages [21] -->
m

<!-- b001374 | furniture | pages [21] -->
m

<!-- b001375 | furniture | pages [21] -->
m

<!-- b001376 | furniture | pages [21] -->
m

<!-- b001377 | furniture | pages [21] -->
m

<!-- b001378 | furniture | pages [21] -->
m

<!-- b001379 | furniture | pages [21] -->
m

<!-- b001380 | furniture | pages [21] -->
m

<!-- b001381 | furniture | pages [21] -->
m

<!-- b001382 | furniture | pages [21] -->
m

<!-- b001383 | furniture | pages [21] -->
m

<!-- b001384 | furniture | pages [21] -->
m

<!-- b001385 | furniture | pages [21] -->
m

<!-- b001386 | furniture | pages [21] -->
m

<!-- b001387 | furniture | pages [21] -->
m

<!-- b001388 | furniture | pages [21] -->
m

<!-- b001389 | furniture | pages [21] -->
m

<!-- b001390 | furniture | pages [21] -->
m

<!-- b001391 | furniture | pages [21] -->
m

<!-- b001392 | furniture | pages [21] -->
m

<!-- b001393 | furniture | pages [21] -->
m

<!-- b001394 | furniture | pages [21] -->
m

<!-- b001395 | furniture | pages [21] -->
m

<!-- b001396 | furniture | pages [21] -->
m

<!-- b001397 | furniture | pages [21] -->
m

<!-- b001398 | furniture | pages [21] -->
m

<!-- b001399 | furniture | pages [21] -->
m

<!-- b001400 | furniture | pages [21] -->
m

<!-- b001401 | furniture | pages [21] -->
m

<!-- b001402 | furniture | pages [21] -->
m

<!-- b001403 | furniture | pages [21] -->
m

<!-- b001404 | furniture | pages [21] -->
m

<!-- b001405 | furniture | pages [21] -->
m

<!-- b001406 | furniture | pages [21] -->
m

<!-- b001407 | furniture | pages [21] -->
m

<!-- b001408 | furniture | pages [21] -->
m

<!-- b001409 | furniture | pages [21] -->
m

<!-- b001410 | furniture | pages [21] -->
m

<!-- b001411 | furniture | pages [21] -->
m

<!-- b001412 | furniture | pages [21] -->
m

<!-- b001413 | furniture | pages [21] -->
m

<!-- b001414 | furniture | pages [21] -->
m

<!-- b001415 | furniture | pages [21] -->
m

<!-- b001416 | furniture | pages [21] -->
m

<!-- b001417 | furniture | pages [21] -->
m

<!-- b001418 | furniture | pages [21] -->
m

<!-- b001419 | furniture | pages [21] -->
m

<!-- b001420 | furniture | pages [21] -->
m

<!-- b001421 | furniture | pages [21] -->
m

<!-- b001422 | furniture | pages [21] -->
m

<!-- b001423 | furniture | pages [21] -->
m

<!-- b001424 | furniture | pages [21] -->
m

<!-- b001425 | furniture | pages [21] -->
m

<!-- b001426 | furniture | pages [21] -->
m

<!-- b001427 | furniture | pages [21] -->
m

<!-- b001428 | furniture | pages [21] -->
m

<!-- b001429 | furniture | pages [21] -->
m

<!-- b001430 | furniture | pages [21] -->
m

<!-- b001431 | furniture | pages [21] -->
m

<!-- b001432 | furniture | pages [21] -->
m

<!-- b001433 | furniture | pages [21] -->
m

<!-- b001434 | furniture | pages [21] -->
m

<!-- b001435 | furniture | pages [21] -->
m

<!-- b001436 | furniture | pages [21] -->
m

<!-- b001437 | furniture | pages [21] -->
m

<!-- b001438 | furniture | pages [21] -->
m

<!-- b001439 | furniture | pages [21] -->
m

<!-- b001440 | furniture | pages [21] -->
m

<!-- b001441 | furniture | pages [21] -->
m

<!-- b001442 | furniture | pages [21] -->
m

<!-- b001443 | furniture | pages [21] -->
m

<!-- b001444 | furniture | pages [21] -->
m

<!-- b001445 | furniture | pages [21] -->
m

<!-- b001446 | furniture | pages [21] -->
m

<!-- b001447 | furniture | pages [21] -->
m

<!-- b001448 | furniture | pages [21] -->
m

<!-- b001449 | furniture | pages [21] -->
m

<!-- b001450 | furniture | pages [21] -->
m

<!-- b001451 | furniture | pages [21] -->
m

<!-- b001452 | furniture | pages [21] -->
m

<!-- b001453 | furniture | pages [21] -->
m

<!-- b001454 | furniture | pages [21] -->
m

<!-- b001455 | furniture | pages [21] -->
m

<!-- b001456 | furniture | pages [21] -->
m

<!-- b001457 | furniture | pages [21] -->
m

<!-- b001458 | furniture | pages [21] -->
m

<!-- b001459 | furniture | pages [21] -->
m

<!-- b001460 | furniture | pages [21] -->
m

<!-- b001461 | furniture | pages [21] -->
m

<!-- b001462 | furniture | pages [21] -->
m

<!-- b001463 | furniture | pages [21] -->
m

<!-- b001464 | furniture | pages [21] -->
m

<!-- b001465 | furniture | pages [21] -->
m

<!-- b001466 | furniture | pages [21] -->
m

<!-- b001467 | furniture | pages [21] -->
m

<!-- b001468 | furniture | pages [21] -->
m

<!-- b001469 | furniture | pages [21] -->
m

<!-- b001470 | furniture | pages [21] -->
m

<!-- b001471 | furniture | pages [21] -->
m

<!-- b001472 | furniture | pages [21] -->
m

<!-- b001473 | furniture | pages [21] -->
m

<!-- b001474 | furniture | pages [21] -->
m

<!-- b001475 | furniture | pages [21] -->
m

<!-- b001476 | furniture | pages [21] -->
m

<!-- b001477 | furniture | pages [21] -->
m

<!-- b001478 | furniture | pages [21] -->
m

<!-- b001479 | furniture | pages [21] -->
m

<!-- b001480 | furniture | pages [21] -->
m

<!-- b001481 | furniture | pages [21] -->
m

<!-- b001482 | furniture | pages [21] -->
m

<!-- b001483 | furniture | pages [21] -->
m

<!-- b001484 | furniture | pages [21] -->
m

<!-- b001485 | furniture | pages [21] -->
m

<!-- b001486 | furniture | pages [21] -->
m

<!-- b001487 | furniture | pages [21] -->
m

<!-- b001488 | furniture | pages [21] -->
m

<!-- b001489 | furniture | pages [21] -->
m

<!-- b001490 | furniture | pages [21] -->
m

<!-- b001491 | furniture | pages [21] -->
m

<!-- b001492 | furniture | pages [21] -->
m

<!-- b001493 | furniture | pages [21] -->
m

<!-- b001494 | furniture | pages [21] -->
m

<!-- b001495 | furniture | pages [21] -->
m

<!-- b001496 | furniture | pages [21] -->
m

<!-- b001497 | furniture | pages [21] -->
m

<!-- b001498 | furniture | pages [21] -->
m

<!-- b001499 | furniture | pages [21] -->
m

<!-- b001500 | furniture | pages [21] -->
m

<!-- b001501 | furniture | pages [21] -->
m

<!-- b001502 | furniture | pages [21] -->
m

<!-- b001503 | furniture | pages [21] -->
m

<!-- b001504 | furniture | pages [21] -->
m

<!-- b001505 | furniture | pages [21] -->
m

<!-- b001506 | furniture | pages [21] -->
m

<!-- b001507 | furniture | pages [21] -->
m

<!-- b001508 | furniture | pages [21] -->
m

<!-- b001509 | furniture | pages [21] -->
m

<!-- b001510 | furniture | pages [21] -->
m

<!-- b001511 | furniture | pages [21] -->
m

<!-- b001512 | furniture | pages [21] -->
m

<!-- b001513 | furniture | pages [21] -->
m

<!-- b001514 | furniture | pages [21] -->
m

<!-- b001515 | furniture | pages [21] -->
m

<!-- b001516 | furniture | pages [21] -->
m

<!-- b001517 | furniture | pages [21] -->
m

<!-- b001518 | furniture | pages [21] -->
m

<!-- b001519 | furniture | pages [21] -->
m

<!-- b001520 | furniture | pages [21] -->
m

<!-- b001521 | furniture | pages [21] -->
m

<!-- b001522 | furniture | pages [21] -->
m

<!-- b001523 | furniture | pages [21] -->
m

<!-- b001524 | furniture | pages [21] -->
m

<!-- b001525 | furniture | pages [21] -->
m

<!-- b001526 | furniture | pages [21] -->
m

<!-- b001527 | furniture | pages [21] -->
m

<!-- b001528 | furniture | pages [21] -->
m

<!-- b001529 | furniture | pages [21] -->
m

<!-- b001530 | furniture | pages [21] -->
m

<!-- b001531 | furniture | pages [21] -->
m

<!-- b001532 | furniture | pages [21] -->
m

<!-- b001533 | furniture | pages [21] -->
m

<!-- b001534 | furniture | pages [21] -->
m

<!-- b001535 | furniture | pages [21] -->
m

<!-- b001536 | furniture | pages [21] -->
m

<!-- b001537 | furniture | pages [21] -->
m

<!-- b001538 | furniture | pages [21] -->
m

<!-- b001539 | furniture | pages [21] -->
m

<!-- b001540 | furniture | pages [21] -->
m

<!-- b001541 | furniture | pages [21] -->
m

<!-- b001542 | furniture | pages [21] -->
m

<!-- b001543 | furniture | pages [21] -->
m

<!-- b001544 | furniture | pages [21] -->
m

<!-- b001545 | furniture | pages [21] -->
m

<!-- b001546 | furniture | pages [21] -->
m

<!-- b001547 | furniture | pages [21] -->
m

<!-- b001548 | furniture | pages [21] -->
m

<!-- b001549 | furniture | pages [21] -->
m

<!-- b001550 | furniture | pages [21] -->
m

<!-- b001551 | furniture | pages [21] -->
m

<!-- b001552 | furniture | pages [21] -->
m

<!-- b001553 | furniture | pages [21] -->
m

<!-- b001554 | furniture | pages [21] -->
m

<!-- b001555 | furniture | pages [21] -->
m

<!-- b001556 | furniture | pages [21] -->
m

<!-- b001557 | furniture | pages [21] -->
m

<!-- b001558 | furniture | pages [21] -->
m

<!-- b001559 | furniture | pages [21] -->
m

<!-- b001560 | furniture | pages [21] -->
m

<!-- b001561 | furniture | pages [21] -->
m

<!-- b001562 | furniture | pages [21] -->
m

<!-- b001563 | furniture | pages [21] -->
m

<!-- b001564 | furniture | pages [21] -->
m

<!-- b001565 | furniture | pages [21] -->
m

<!-- b001566 | furniture | pages [21] -->
m

<!-- b001567 | furniture | pages [21] -->
m

<!-- b001568 | furniture | pages [21] -->
m

<!-- b001569 | furniture | pages [21] -->
m

<!-- b001570 | furniture | pages [21] -->
m

<!-- b001571 | furniture | pages [21] -->
m

<!-- b001572 | furniture | pages [21] -->
m

<!-- b001573 | furniture | pages [21] -->
m

<!-- b001574 | furniture | pages [21] -->
m

<!-- b001575 | furniture | pages [21] -->
m

<!-- b001576 | furniture | pages [21] -->
m

<!-- b001577 | furniture | pages [21] -->
m

<!-- b001578 | furniture | pages [21] -->
m

<!-- b001579 | furniture | pages [21] -->
m

<!-- b001580 | furniture | pages [21] -->
m

<!-- b001581 | furniture | pages [21] -->
m

<!-- b001582 | furniture | pages [21] -->
m

<!-- b001583 | furniture | pages [21] -->
m

<!-- b001584 | furniture | pages [21] -->
m

<!-- b001585 | furniture | pages [21] -->
m

<!-- b001586 | furniture | pages [21] -->
m

<!-- b001587 | furniture | pages [21] -->
m

<!-- b001588 | furniture | pages [21] -->
m

<!-- b001589 | furniture | pages [21] -->
m

<!-- b001590 | furniture | pages [21] -->
m

<!-- b001591 | furniture | pages [21] -->
m

<!-- b001592 | furniture | pages [21] -->
m

<!-- b001593 | furniture | pages [21] -->
m

<!-- b001594 | furniture | pages [21] -->
m

<!-- b001595 | furniture | pages [21] -->
m

<!-- b001596 | furniture | pages [21] -->
m

<!-- b001597 | furniture | pages [21] -->
m

<!-- b001598 | furniture | pages [21] -->
m

<!-- b001599 | furniture | pages [21] -->
m

<!-- b001600 | furniture | pages [21] -->
m

<!-- b001601 | furniture | pages [21] -->
m

<!-- b001602 | furniture | pages [21] -->
m

<!-- b001603 | furniture | pages [21] -->
m

<!-- b001604 | furniture | pages [21] -->
m

<!-- b001605 | furniture | pages [21] -->
m

<!-- b001606 | furniture | pages [21] -->
m

<!-- b001607 | furniture | pages [21] -->
m

<!-- b001608 | furniture | pages [21] -->
m

<!-- b001609 | furniture | pages [21] -->
m

<!-- b001610 | furniture | pages [21] -->
m

<!-- b001611 | furniture | pages [21] -->
m

<!-- b001612 | furniture | pages [21] -->
m

<!-- b001613 | furniture | pages [21] -->
m

<!-- b001614 | furniture | pages [21] -->
m

<!-- b001615 | furniture | pages [21] -->
m

<!-- b001616 | furniture | pages [21] -->
m

<!-- b001617 | furniture | pages [21] -->
m

<!-- b001618 | furniture | pages [21] -->
m

<!-- b001619 | furniture | pages [22] -->
Page 22 of 25

<!-- b001620 | furniture | pages [22] -->
Team # 2502617

<!-- b001622 | caption | pages [22] -->
Table 3: Comparison of Information and Conclusions in Juneau and Jiuzhaigou

<!-- b001623 | prose | pages [22] -->
City Jiuzhaigou, China Juneau, Alaska

<!-- b001624 | prose | pages [22] -->
Small population

<!-- b001625 | prose | pages [22] -->
Economiey predominantly dependent on tourism Similar Part Environment and society vulnerable to the impacts of overtourism The tourist destination is concentrated in a certain scenic spot Current Situation Relatively developed Relatively worse economy economy Closer to the Arctic, the Temperate regions have a Different Part ecosystem is even less more stable environment stable

<!-- b001626 | prose | pages [22] -->
Government spending There are differences in varies government policies

<!-- b001627 | prose | pages [22] -->
Lower Higher Tax rate

<!-- b001628 | prose | pages [22] -->
Key Proportion of Similar Similar Tourists Parameter Tourist Higher Lower Consumption Constraint More consideration of More consideration of Measures to Factors environment benefit economy benefit Mitigate Optimized Overtourism Number of tourists in Global Pareto Optimization Factors

<!-- b001629 | prose | pages [22] -->
Properly reduce local taxes, discount goods for tourists, and reduce tourist expenses to attract tourists

<!-- b001630 | prose | pages [22] -->
How to Promote Locations Achieve a win-win situation between tourists' that satisfaction and residents' satisfaction to achieve fame Have Fewer Tourists publicity Lucid water and lush mountains are golden hills and invaluable assets, which ensure a good environment as a tourist attraction

<!-- b001631 | prose | pages [22] -->
关注数学模型

<!-- b001632 | furniture | pages [22] -->
获取更多资讯

<!-- b001633 | furniture | pages [23] -->
Team # 2502617

<!-- b001634 | furniture | pages [23] -->
Page 23 of 25

<!-- b001635 | heading | pages [23] -->
References

<!-- b001636 | references | pages [23] -->
[1]

<!-- b001637 | references | pages [23] -->
Cristina Campos Herrero et al. “Tourism under a life cycle thinking approach: A review of

<!-- b001638 | references | pages [23] -->
perspectives and new challenges for the tourism sector in the last decades”. In: Science of

<!-- b001639 | references | pages [23] -->
the Total Environment (2022). doi: 10.1016/j.scitotenv.2022.157261.

<!-- b001640 | references | pages [23] -->
[2]

<!-- b001641 | references | pages [23] -->
url: https://abc7.com/post/juneau-alaska-cruise-ship-limits-overtourism/

<!-- b001642 | references | pages [23] -->
15048713/.

<!-- b001643 | references | pages [23] -->
微信公众号：数学模型

<!-- b001644 | references | pages [23] -->
[3]

<!-- b001645 | references | pages [23] -->
url: https://juneau.org/wp-content/uploads/2024/01/CBJ-Cruise-Impacts-

<!-- b001646 | references | pages [23] -->
2023-Report-1.22.24.pdf.

<!-- b001647 | references | pages [23] -->
[4]

<!-- b001648 | references | pages [23] -->
SF McCool. “Making tourism sustainable, sustainable tourism, and what should tourism sus-

<!-- b001649 | references | pages [23] -->
tain: Different questions, different indicators”. In: PROCEEDINGS OF THE 1999 INTERNA-

<!-- b001650 | references | pages [23] -->
TIONAL SYMPOSIUM ON COASTAL AND MARINE TOURISM: BALANCING TOURISM

<!-- b001651 | references | pages [23] -->
AND CONSERVATION (2002).

<!-- b001652 | references | pages [23] -->
[5]

<!-- b001653 | references | pages [23] -->
ClaireWeishar. “Frommasstourismtosustainabletourism?”In: CONFINS-REVUEFRANCO-

<!-- b001654 | references | pages [23] -->
BRESILIENNE DE GEOGRAPHIE-REVISTA FRANCO-BRASILEIRA DE GEOGRAFIA

<!-- b001655 | references | pages [23] -->
(2021).

<!-- b001656 | references | pages [23] -->
微信号：MATHmodels

<!-- b001657 | references | pages [23] -->
[6]

<!-- b001658 | references | pages [23] -->
Yi Guo, Jinbo Jiang, and Shengchao Li. “A Sustainable Tourism Policy Research Review”.

<!-- b001659 | references | pages [23] -->
In: SUSTAINABILITY (2019). doi: {10.3390/su11113187}.

<!-- b001660 | references | pages [23] -->
[7]

<!-- b001661 | references | pages [23] -->
Haiyan Kong et al. “Exploring Chinese sustainable tourism: a 25-year perspective”. In:

<!-- b001662 | references | pages [23] -->
JOURNAL OF SUSTAINABLE TOURISM (2024). doi: {10 . 1080 / 09669582 . 2024 .

<!-- b001663 | references | pages [23] -->
2347547}.

<!-- b001664 | references | pages [23] -->
[8]

<!-- b001665 | references | pages [23] -->
Andrea Saayman and ShiNa Li. “The contribution of economics to sustainable tourism re-

<!-- b001666 | references | pages [23] -->
search”. In: JOURNAL OF SUSTAINABLE TOURISM 31 (2023). doi: 10.1080/09669582.

<!-- b001667 | references | pages [23] -->
2023.2224943.

<!-- b001668 | references | pages [23] -->
[9]

<!-- b001669 | references | pages [23] -->
Michelle M. Whitford and Lisa M. Ruhanen. “Australian indigenous tourism policy: practical

<!-- b001670 | references | pages [23] -->
and sustainable policies?” In: JOURNAL OF SUSTAINABLE TOURISM 18 (2010). doi:

<!-- b001671 | references | pages [23] -->
10.1080/09669581003602325.

<!-- b001672 | references | pages [23] -->
[10]

<!-- b001673 | references | pages [23] -->
Muhamad and Anugrah Gusta Prima. “Implementation Of Sustainable Tourism Destination

<!-- b001674 | references | pages [23] -->
Development Achievements (Indicators of Sustainable Tourism Development (STD), Sus-

<!-- b001675 | references | pages [23] -->
tainable Tourism Observatory (STO) Towards Sustainable Tourism Certification (STC) in

<!-- b001676 | references | pages [23] -->
Pulesari Village, Wonokerto, Turi District, Sleman Regency, Daerah Istimewa Yogyakarta)”.

<!-- b001677 | references | pages [23] -->
In: PROCEEDINGS OF THE ASIA TOURISM FORUM 2016 - THE 12TH BIENNIAL CON-

<!-- b001678 | references | pages [23] -->
FERENCE OF HOSPITALITY AND TOURISM INDUSTRY IN ASIA (2016).

<!-- b001679 | references | pages [23] -->
[11]

<!-- b001680 | references | pages [23] -->
Seldjan Timur and Donald Getz. “Sustainable Tourism Development: How Do Destination

<!-- b001681 | references | pages [23] -->
Stakeholders Perceive Sustainable Urban Tourism?” In: SUSTAINABLE DEVELOPMENT

<!-- b001682 | references | pages [23] -->
17 (2009). doi: 10.1002/sd.384.

<!-- b001683 | references | pages [23] -->
[12]

<!-- b001684 | references | pages [23] -->
Georgiana Daniela Stoica et al. “Perspectives for the Development of Sustainable Cultural

<!-- b001685 | references | pages [23] -->
Tourism”. In: SUSTAINABILITY 14 (2022). doi: 10.3390/su14095678.

<!-- b001686 | references | pages [23] -->
[13]

<!-- b001687 | references | pages [23] -->
Keartisak Sriprateep et al. “Multi-Objective Optimization of Resilient, Sustainable, and

<!-- b001688 | references | pages [23] -->
Safe Urban Bus Routes for Tourism Promotion Using a Hybrid Reinforcement Learning

<!-- b001689 | references | pages [23] -->
Algorithm”. In: MATHEMATICS 12 (2024). doi: 10.3390/math12142283.

<!-- b001690 | references | pages [23] -->
m

<!-- b001691 | references | pages [23] -->
m

<!-- b001692 | references | pages [23] -->
m

<!-- b001693 | references | pages [23] -->
m

<!-- b001694 | references | pages [23] -->
m

<!-- b001695 | references | pages [23] -->
m

<!-- b001696 | references | pages [23] -->
m

<!-- b001697 | references | pages [23] -->
m

<!-- b001698 | references | pages [23] -->
m

<!-- b001699 | references | pages [23] -->
m

<!-- b001700 | references | pages [23] -->
m

<!-- b001701 | references | pages [23] -->
m

<!-- b001702 | references | pages [23] -->
m

<!-- b001703 | references | pages [23] -->
m

<!-- b001704 | references | pages [23] -->
m

<!-- b001705 | references | pages [23] -->
m

<!-- b001706 | references | pages [23] -->
m

<!-- b001707 | references | pages [23] -->
m

<!-- b001708 | references | pages [23] -->
m

<!-- b001709 | references | pages [23] -->
m

<!-- b001710 | references | pages [23] -->
m

<!-- b001711 | references | pages [23] -->
m

<!-- b001712 | references | pages [23] -->
m

<!-- b001713 | references | pages [23] -->
m

<!-- b001714 | references | pages [23] -->
m

<!-- b001715 | references | pages [23] -->
m

<!-- b001716 | references | pages [23] -->
m

<!-- b001717 | references | pages [23] -->
m

<!-- b001718 | references | pages [23] -->
m

<!-- b001719 | references | pages [23] -->
m

<!-- b001720 | references | pages [23] -->
m

<!-- b001721 | references | pages [23] -->
m

<!-- b001722 | references | pages [23] -->
m

<!-- b001723 | references | pages [23] -->
m

<!-- b001724 | references | pages [23] -->
m

<!-- b001725 | references | pages [23] -->
m

<!-- b001726 | references | pages [23] -->
m

<!-- b001727 | references | pages [23] -->
m

<!-- b001728 | references | pages [23] -->
m

<!-- b001729 | references | pages [23] -->
m

<!-- b001730 | references | pages [23] -->
m

<!-- b001731 | references | pages [23] -->
m

<!-- b001732 | references | pages [23] -->
m

<!-- b001733 | references | pages [23] -->
m

<!-- b001734 | references | pages [23] -->
m

<!-- b001735 | references | pages [23] -->
m

<!-- b001736 | references | pages [23] -->
m

<!-- b001737 | references | pages [23] -->
m

<!-- b001738 | references | pages [23] -->
m

<!-- b001739 | references | pages [23] -->
m

<!-- b001740 | references | pages [23] -->
m

<!-- b001741 | references | pages [23] -->
m

<!-- b001742 | references | pages [23] -->
m

<!-- b001743 | references | pages [23] -->
m

<!-- b001744 | references | pages [23] -->
m

<!-- b001745 | references | pages [23] -->
m

<!-- b001746 | references | pages [23] -->
m

<!-- b001747 | references | pages [23] -->
m

<!-- b001748 | references | pages [23] -->
m

<!-- b001749 | references | pages [23] -->
m

<!-- b001750 | references | pages [23] -->
m

<!-- b001751 | references | pages [23] -->
m

<!-- b001752 | references | pages [23] -->
m

<!-- b001753 | references | pages [23] -->
m

<!-- b001754 | references | pages [23] -->
m

<!-- b001755 | references | pages [23] -->
m

<!-- b001756 | references | pages [23] -->
m

<!-- b001757 | references | pages [23] -->
m

<!-- b001758 | references | pages [23] -->
m

<!-- b001759 | references | pages [23] -->
m

<!-- b001760 | references | pages [23] -->
m

<!-- b001761 | references | pages [23] -->
m

<!-- b001762 | references | pages [23] -->
m

<!-- b001763 | references | pages [23] -->
m

<!-- b001764 | references | pages [23] -->
m

<!-- b001765 | references | pages [23] -->
m

<!-- b001766 | references | pages [23] -->
m

<!-- b001767 | references | pages [23] -->
m

<!-- b001768 | references | pages [23] -->
m

<!-- b001769 | references | pages [23] -->
m

<!-- b001770 | references | pages [23] -->
m

<!-- b001771 | references | pages [23] -->
m

<!-- b001772 | references | pages [23] -->
m

<!-- b001773 | references | pages [23] -->
m

<!-- b001774 | references | pages [23] -->
m

<!-- b001775 | references | pages [23] -->
m

<!-- b001776 | references | pages [23] -->
m

<!-- b001777 | references | pages [23] -->
m

<!-- b001778 | references | pages [23] -->
m

<!-- b001779 | references | pages [23] -->
m

<!-- b001780 | references | pages [23] -->
m

<!-- b001781 | references | pages [23] -->
m

<!-- b001782 | references | pages [23] -->
m

<!-- b001783 | references | pages [23] -->
m

<!-- b001784 | references | pages [23] -->
m

<!-- b001785 | references | pages [23] -->
m

<!-- b001786 | references | pages [23] -->
m

<!-- b001787 | references | pages [23] -->
m

<!-- b001788 | references | pages [23] -->
m

<!-- b001789 | references | pages [23] -->
m

<!-- b001790 | references | pages [23] -->
m

<!-- b001791 | references | pages [23] -->
m

<!-- b001792 | references | pages [23] -->
m

<!-- b001793 | references | pages [23] -->
m

<!-- b001794 | references | pages [23] -->
m

<!-- b001795 | references | pages [23] -->
m

<!-- b001796 | references | pages [23] -->
m

<!-- b001797 | references | pages [23] -->
m

<!-- b001798 | references | pages [23] -->
m

<!-- b001799 | references | pages [23] -->
m

<!-- b001800 | references | pages [23] -->
m

<!-- b001801 | references | pages [23] -->
m

<!-- b001802 | references | pages [23] -->
m

<!-- b001803 | references | pages [23] -->
m

<!-- b001804 | references | pages [23] -->
m

<!-- b001805 | references | pages [23] -->
m

<!-- b001806 | references | pages [23] -->
m

<!-- b001807 | references | pages [23] -->
m

<!-- b001808 | references | pages [23] -->
m

<!-- b001809 | references | pages [23] -->
m

<!-- b001810 | references | pages [23] -->
m

<!-- b001811 | references | pages [23] -->
m

<!-- b001812 | references | pages [23] -->
m

<!-- b001813 | references | pages [23] -->
m

<!-- b001814 | references | pages [23] -->
m

<!-- b001815 | references | pages [23] -->
m

<!-- b001816 | references | pages [23] -->
m

<!-- b001817 | references | pages [23] -->
m

<!-- b001818 | references | pages [23] -->
m

<!-- b001819 | references | pages [23] -->
m

<!-- b001820 | references | pages [23] -->
m

<!-- b001821 | references | pages [23] -->
m

<!-- b001822 | references | pages [23] -->
m

<!-- b001823 | references | pages [23] -->
m

<!-- b001824 | references | pages [23] -->
m

<!-- b001825 | references | pages [23] -->
m

<!-- b001826 | references | pages [23] -->
m

<!-- b001827 | references | pages [23] -->
m

<!-- b001828 | references | pages [23] -->
m

<!-- b001829 | references | pages [23] -->
m

<!-- b001830 | references | pages [23] -->
m

<!-- b001831 | references | pages [23] -->
m

<!-- b001832 | references | pages [23] -->
m

<!-- b001833 | references | pages [23] -->
m

<!-- b001834 | references | pages [23] -->
m

<!-- b001835 | references | pages [23] -->
m

<!-- b001836 | references | pages [23] -->
m

<!-- b001837 | references | pages [23] -->
m

<!-- b001838 | references | pages [23] -->
m

<!-- b001839 | references | pages [23] -->
m

<!-- b001840 | references | pages [23] -->
m

<!-- b001841 | references | pages [23] -->
m

<!-- b001842 | references | pages [23] -->
m

<!-- b001843 | references | pages [23] -->
m

<!-- b001844 | references | pages [23] -->
m

<!-- b001845 | references | pages [23] -->
m

<!-- b001846 | references | pages [23] -->
m

<!-- b001847 | references | pages [23] -->
m

<!-- b001848 | references | pages [23] -->
m

<!-- b001849 | references | pages [23] -->
m

<!-- b001850 | references | pages [23] -->
m

<!-- b001851 | references | pages [23] -->
m

<!-- b001852 | references | pages [23] -->
m

<!-- b001853 | references | pages [23] -->
m

<!-- b001854 | references | pages [23] -->
m

<!-- b001855 | references | pages [23] -->
m

<!-- b001856 | references | pages [23] -->
m

<!-- b001857 | references | pages [23] -->
m

<!-- b001858 | references | pages [23] -->
m

<!-- b001859 | references | pages [23] -->
m

<!-- b001860 | references | pages [23] -->
m

<!-- b001861 | references | pages [23] -->
m

<!-- b001862 | references | pages [23] -->
m

<!-- b001863 | references | pages [23] -->
m

<!-- b001864 | references | pages [23] -->
m

<!-- b001865 | references | pages [23] -->
m

<!-- b001866 | references | pages [23] -->
m

<!-- b001867 | references | pages [23] -->
m

<!-- b001868 | references | pages [23] -->
m

<!-- b001869 | references | pages [23] -->
m

<!-- b001870 | references | pages [23] -->
m

<!-- b001871 | references | pages [23] -->
m

<!-- b001872 | references | pages [23] -->
m

<!-- b001873 | references | pages [23] -->
m

<!-- b001874 | references | pages [23] -->
m

<!-- b001875 | references | pages [23] -->
m

<!-- b001876 | references | pages [23] -->
m

<!-- b001877 | references | pages [23] -->
m

<!-- b001878 | references | pages [23] -->
m

<!-- b001879 | references | pages [23] -->
m

<!-- b001880 | references | pages [23] -->
m

<!-- b001881 | references | pages [23] -->
m

<!-- b001882 | references | pages [23] -->
m

<!-- b001883 | references | pages [23] -->
m

<!-- b001884 | references | pages [23] -->
m

<!-- b001885 | references | pages [23] -->
m

<!-- b001886 | references | pages [23] -->
m

<!-- b001887 | references | pages [23] -->
m

<!-- b001888 | references | pages [23] -->
m

<!-- b001889 | references | pages [23] -->
m

<!-- b001890 | references | pages [23] -->
m

<!-- b001891 | references | pages [23] -->
m

<!-- b001892 | references | pages [23] -->
m

<!-- b001893 | references | pages [23] -->
m

<!-- b001894 | references | pages [23] -->
m

<!-- b001895 | references | pages [23] -->
m

<!-- b001896 | references | pages [23] -->
m

<!-- b001897 | references | pages [23] -->
m

<!-- b001898 | references | pages [23] -->
m

<!-- b001899 | references | pages [23] -->
m

<!-- b001900 | references | pages [23] -->
m

<!-- b001901 | references | pages [23] -->
m

<!-- b001902 | references | pages [23] -->
m

<!-- b001903 | references | pages [23] -->
m

<!-- b001904 | references | pages [23] -->
m

<!-- b001905 | references | pages [23] -->
m

<!-- b001906 | references | pages [23] -->
m

<!-- b001907 | references | pages [23] -->
m

<!-- b001908 | references | pages [23] -->
m

<!-- b001909 | references | pages [23] -->
m

<!-- b001910 | references | pages [23] -->
m

<!-- b001911 | references | pages [23] -->
m

<!-- b001912 | references | pages [23] -->
m

<!-- b001913 | references | pages [23] -->
m

<!-- b001914 | references | pages [23] -->
m

<!-- b001915 | references | pages [23] -->
m

<!-- b001916 | references | pages [23] -->
m

<!-- b001917 | references | pages [23] -->
m

<!-- b001918 | references | pages [23] -->
m

<!-- b001919 | references | pages [23] -->
m

<!-- b001920 | furniture | pages [23] -->
m

<!-- b001921 | furniture | pages [23] -->
m

<!-- b001922 | furniture | pages [23] -->
m

<!-- b001923 | furniture | pages [23] -->
m

<!-- b001924 | furniture | pages [23] -->
m

<!-- b001925 | furniture | pages [23] -->
m

<!-- b001926 | furniture | pages [23] -->
m

<!-- b001927 | furniture | pages [23] -->
m

<!-- b001928 | furniture | pages [23] -->
m

<!-- b001929 | furniture | pages [23] -->
m

<!-- b001930 | furniture | pages [23] -->
m

<!-- b001931 | furniture | pages [23] -->
m

<!-- b001932 | furniture | pages [23] -->
m

<!-- b001933 | furniture | pages [23] -->
m

<!-- b001934 | furniture | pages [23] -->
m

<!-- b001935 | furniture | pages [23] -->
m

<!-- b001936 | furniture | pages [23] -->
m

<!-- b001937 | furniture | pages [23] -->
m

<!-- b001938 | furniture | pages [23] -->
m

<!-- b001939 | furniture | pages [23] -->
m

<!-- b001940 | furniture | pages [23] -->
m

<!-- b001941 | furniture | pages [23] -->
m

<!-- b001942 | furniture | pages [23] -->
m

<!-- b001943 | furniture | pages [23] -->
m

<!-- b001944 | furniture | pages [23] -->
m

<!-- b001945 | furniture | pages [23] -->
m

<!-- b001946 | furniture | pages [23] -->
m

<!-- b001947 | furniture | pages [23] -->
m

<!-- b001948 | furniture | pages [23] -->
m

<!-- b001949 | furniture | pages [23] -->
m

<!-- b001950 | furniture | pages [23] -->
m

<!-- b001951 | furniture | pages [23] -->
m

<!-- b001952 | furniture | pages [23] -->
m

<!-- b001953 | furniture | pages [23] -->
m

<!-- b001954 | furniture | pages [23] -->
m

<!-- b001955 | furniture | pages [23] -->
m

<!-- b001956 | furniture | pages [23] -->
m

<!-- b001957 | furniture | pages [23] -->
m

<!-- b001958 | furniture | pages [23] -->
m

<!-- b001959 | furniture | pages [23] -->
m

<!-- b001960 | furniture | pages [23] -->
m

<!-- b001961 | furniture | pages [23] -->
m

<!-- b001962 | furniture | pages [23] -->
m

<!-- b001963 | furniture | pages [23] -->
m

<!-- b001964 | furniture | pages [23] -->
m

<!-- b001965 | furniture | pages [23] -->
m

<!-- b001966 | furniture | pages [23] -->
m

<!-- b001967 | furniture | pages [23] -->
m

<!-- b001968 | furniture | pages [23] -->
m

<!-- b001969 | furniture | pages [23] -->
m

<!-- b001970 | furniture | pages [23] -->
m

<!-- b001971 | furniture | pages [23] -->
m

<!-- b001972 | furniture | pages [23] -->
m

<!-- b001973 | furniture | pages [23] -->
m

<!-- b001974 | furniture | pages [23] -->
m

<!-- b001975 | furniture | pages [23] -->
m

<!-- b001976 | furniture | pages [23] -->
m

<!-- b001977 | furniture | pages [23] -->
m

<!-- b001978 | furniture | pages [23] -->
m

<!-- b001979 | furniture | pages [23] -->
m

<!-- b001980 | furniture | pages [23] -->
m

<!-- b001981 | furniture | pages [23] -->
m

<!-- b001982 | furniture | pages [23] -->
m

<!-- b001983 | furniture | pages [23] -->
m

<!-- b001984 | furniture | pages [23] -->
m

<!-- b001985 | furniture | pages [23] -->
m

<!-- b001986 | furniture | pages [23] -->
m

<!-- b001987 | furniture | pages [23] -->
m

<!-- b001988 | furniture | pages [23] -->
m

<!-- b001989 | furniture | pages [23] -->
m

<!-- b001990 | furniture | pages [23] -->
m

<!-- b001991 | furniture | pages [23] -->
m

<!-- b001992 | furniture | pages [23] -->
m

<!-- b001993 | furniture | pages [23] -->
m

<!-- b001994 | furniture | pages [23] -->
m

<!-- b001995 | furniture | pages [23] -->
m

<!-- b001996 | furniture | pages [23] -->
m

<!-- b001997 | furniture | pages [23] -->
m

<!-- b001998 | furniture | pages [23] -->
m

<!-- b001999 | furniture | pages [23] -->
m

<!-- b002000 | furniture | pages [23] -->
m

<!-- b002001 | furniture | pages [23] -->
m

<!-- b002002 | furniture | pages [23] -->
m

<!-- b002003 | furniture | pages [23] -->
m

<!-- b002004 | furniture | pages [23] -->
m

<!-- b002005 | furniture | pages [23] -->
m

<!-- b002006 | furniture | pages [23] -->
m

<!-- b002007 | furniture | pages [23] -->
m

<!-- b002008 | furniture | pages [23] -->
m

<!-- b002009 | furniture | pages [23] -->
m

<!-- b002010 | furniture | pages [23] -->
m

<!-- b002011 | furniture | pages [23] -->
m

<!-- b002012 | furniture | pages [23] -->
m

<!-- b002013 | furniture | pages [23] -->
m

<!-- b002014 | furniture | pages [23] -->
m

<!-- b002015 | furniture | pages [23] -->
m

<!-- b002016 | furniture | pages [23] -->
m

<!-- b002017 | furniture | pages [23] -->
m

<!-- b002018 | furniture | pages [23] -->
m

<!-- b002019 | furniture | pages [23] -->
m

<!-- b002020 | furniture | pages [23] -->
m

<!-- b002021 | furniture | pages [23] -->
m

<!-- b002022 | furniture | pages [23] -->
m

<!-- b002023 | furniture | pages [23] -->
m

<!-- b002024 | furniture | pages [23] -->
m

<!-- b002025 | furniture | pages [23] -->
m

<!-- b002026 | furniture | pages [23] -->
m

<!-- b002027 | furniture | pages [23] -->
m

<!-- b002028 | furniture | pages [23] -->
m

<!-- b002029 | furniture | pages [23] -->
m

<!-- b002030 | furniture | pages [23] -->
m

<!-- b002031 | furniture | pages [23] -->
m

<!-- b002032 | furniture | pages [23] -->
m

<!-- b002033 | furniture | pages [23] -->
m

<!-- b002034 | furniture | pages [23] -->
m

<!-- b002035 | furniture | pages [23] -->
m

<!-- b002036 | furniture | pages [23] -->
m

<!-- b002037 | furniture | pages [23] -->
m

<!-- b002038 | furniture | pages [23] -->
m

<!-- b002039 | furniture | pages [23] -->
m

<!-- b002040 | furniture | pages [23] -->
m

<!-- b002041 | furniture | pages [23] -->
m

<!-- b002042 | furniture | pages [23] -->
m

<!-- b002043 | furniture | pages [23] -->
m

<!-- b002044 | furniture | pages [23] -->
m

<!-- b002045 | furniture | pages [23] -->
m

<!-- b002046 | furniture | pages [23] -->
m

<!-- b002047 | furniture | pages [23] -->
m

<!-- b002048 | furniture | pages [23] -->
m

<!-- b002049 | furniture | pages [23] -->
m

<!-- b002050 | furniture | pages [23] -->
m

<!-- b002051 | furniture | pages [23] -->
m

<!-- b002052 | furniture | pages [23] -->
m

<!-- b002053 | furniture | pages [23] -->
m

<!-- b002054 | furniture | pages [23] -->
m

<!-- b002055 | furniture | pages [23] -->
m

<!-- b002056 | furniture | pages [23] -->
m

<!-- b002057 | furniture | pages [23] -->
m

<!-- b002058 | furniture | pages [23] -->
m

<!-- b002059 | furniture | pages [23] -->
m

<!-- b002060 | furniture | pages [23] -->
m

<!-- b002061 | furniture | pages [23] -->
m

<!-- b002062 | furniture | pages [23] -->
m

<!-- b002063 | furniture | pages [23] -->
m

<!-- b002064 | furniture | pages [23] -->
m

<!-- b002065 | furniture | pages [23] -->
m

<!-- b002066 | furniture | pages [23] -->
m

<!-- b002067 | furniture | pages [23] -->
m

<!-- b002068 | furniture | pages [23] -->
m

<!-- b002069 | furniture | pages [23] -->
m

<!-- b002070 | furniture | pages [23] -->
m

<!-- b002071 | furniture | pages [23] -->
m

<!-- b002072 | furniture | pages [23] -->
m

<!-- b002073 | furniture | pages [23] -->
m

<!-- b002074 | furniture | pages [23] -->
m

<!-- b002075 | furniture | pages [23] -->
m

<!-- b002076 | furniture | pages [23] -->
m

<!-- b002077 | furniture | pages [23] -->
m

<!-- b002078 | furniture | pages [23] -->
m

<!-- b002079 | furniture | pages [23] -->
m

<!-- b002080 | furniture | pages [23] -->
m

<!-- b002081 | furniture | pages [23] -->
m

<!-- b002082 | furniture | pages [23] -->
m

<!-- b002083 | furniture | pages [23] -->
m

<!-- b002084 | furniture | pages [23] -->
m

<!-- b002085 | furniture | pages [23] -->
m

<!-- b002086 | furniture | pages [23] -->
m

<!-- b002087 | furniture | pages [23] -->
m

<!-- b002088 | furniture | pages [23] -->
m

<!-- b002089 | furniture | pages [23] -->
m

<!-- b002090 | furniture | pages [23] -->
m

<!-- b002091 | furniture | pages [23] -->
m

<!-- b002092 | furniture | pages [23] -->
m

<!-- b002093 | furniture | pages [23] -->
m

<!-- b002094 | furniture | pages [23] -->
m

<!-- b002095 | furniture | pages [23] -->
m

<!-- b002096 | furniture | pages [23] -->
m

<!-- b002097 | furniture | pages [23] -->
m

<!-- b002098 | furniture | pages [23] -->
m

<!-- b002099 | furniture | pages [23] -->
m

<!-- b002100 | furniture | pages [23] -->
m

<!-- b002101 | furniture | pages [23] -->
m

<!-- b002102 | furniture | pages [23] -->
m

<!-- b002103 | furniture | pages [23] -->
m

<!-- b002104 | furniture | pages [23] -->
m

<!-- b002105 | furniture | pages [23] -->
m

<!-- b002106 | furniture | pages [23] -->
m

<!-- b002107 | furniture | pages [23] -->
m

<!-- b002108 | furniture | pages [23] -->
m

<!-- b002109 | furniture | pages [23] -->
m

<!-- b002110 | furniture | pages [23] -->
m

<!-- b002111 | furniture | pages [23] -->
m

<!-- b002112 | furniture | pages [23] -->
m

<!-- b002113 | furniture | pages [23] -->
m

<!-- b002114 | furniture | pages [23] -->
m

<!-- b002115 | furniture | pages [23] -->
m

<!-- b002116 | furniture | pages [23] -->
m

<!-- b002117 | furniture | pages [23] -->
m

<!-- b002118 | furniture | pages [23] -->
m

<!-- b002119 | furniture | pages [23] -->
m

<!-- b002120 | furniture | pages [23] -->
m

<!-- b002121 | furniture | pages [23] -->
m

<!-- b002122 | furniture | pages [23] -->
m

<!-- b002123 | furniture | pages [23] -->
m

<!-- b002124 | furniture | pages [23] -->
m

<!-- b002125 | furniture | pages [23] -->
m

<!-- b002126 | furniture | pages [23] -->
m

<!-- b002127 | furniture | pages [23] -->
m

<!-- b002128 | furniture | pages [23] -->
m

<!-- b002129 | furniture | pages [23] -->
m

<!-- b002130 | furniture | pages [23] -->
m

<!-- b002131 | furniture | pages [23] -->
m

<!-- b002132 | furniture | pages [23] -->
m

<!-- b002133 | furniture | pages [23] -->
m

<!-- b002134 | furniture | pages [23] -->
m

<!-- b002135 | furniture | pages [23] -->
m

<!-- b002136 | furniture | pages [23] -->
m

<!-- b002137 | furniture | pages [23] -->
m

<!-- b002138 | furniture | pages [23] -->
m

<!-- b002139 | furniture | pages [23] -->
m

<!-- b002140 | furniture | pages [23] -->
m

<!-- b002141 | furniture | pages [23] -->
m

<!-- b002142 | furniture | pages [23] -->
m

<!-- b002143 | furniture | pages [23] -->
m

<!-- b002144 | furniture | pages [23] -->
m

<!-- b002145 | furniture | pages [23] -->
m

<!-- b002146 | furniture | pages [23] -->
m

<!-- b002147 | furniture | pages [23] -->
m

<!-- b002148 | furniture | pages [23] -->
m

<!-- b002149 | furniture | pages [23] -->
m

<!-- b002150 | furniture | pages [23] -->
m

<!-- b002151 | furniture | pages [23] -->
m

<!-- b002152 | furniture | pages [23] -->
m

<!-- b002153 | furniture | pages [23] -->
m

<!-- b002154 | furniture | pages [23] -->
m

<!-- b002155 | furniture | pages [23] -->
m

<!-- b002156 | furniture | pages [23] -->
m

<!-- b002157 | furniture | pages [23] -->
m

<!-- b002158 | furniture | pages [23] -->
m

<!-- b002159 | furniture | pages [23] -->
m

<!-- b002160 | furniture | pages [23] -->
m

<!-- b002161 | furniture | pages [23] -->
m

<!-- b002162 | furniture | pages [23] -->
m

<!-- b002163 | furniture | pages [23] -->
m

<!-- b002164 | furniture | pages [23] -->
m

<!-- b002165 | furniture | pages [23] -->
m

<!-- b002166 | furniture | pages [23] -->
m

<!-- b002167 | furniture | pages [23] -->
m

<!-- b002168 | furniture | pages [23] -->
m

<!-- b002169 | furniture | pages [23] -->
m

<!-- b002170 | furniture | pages [23] -->
m

<!-- b002171 | furniture | pages [23] -->
m

<!-- b002172 | furniture | pages [23] -->
m

<!-- b002173 | furniture | pages [23] -->
m

<!-- b002174 | furniture | pages [23] -->
m

<!-- b002175 | furniture | pages [23] -->
m

<!-- b002176 | furniture | pages [23] -->
m

<!-- b002177 | furniture | pages [23] -->
m

<!-- b002178 | furniture | pages [23] -->
m

<!-- b002179 | furniture | pages [23] -->
m

<!-- b002180 | furniture | pages [23] -->
m

<!-- b002181 | furniture | pages [23] -->
m

<!-- b002182 | furniture | pages [23] -->
m

<!-- b002183 | furniture | pages [23] -->
m

<!-- b002184 | furniture | pages [23] -->
m

<!-- b002185 | furniture | pages [23] -->
m

<!-- b002186 | furniture | pages [23] -->
m

<!-- b002187 | furniture | pages [23] -->
m

<!-- b002188 | furniture | pages [23] -->
m

<!-- b002189 | furniture | pages [23] -->
m

<!-- b002190 | furniture | pages [23] -->
m

<!-- b002191 | furniture | pages [23] -->
m

<!-- b002192 | furniture | pages [23] -->
m

<!-- b002193 | furniture | pages [23] -->
m

<!-- b002194 | furniture | pages [23] -->
m

<!-- b002195 | furniture | pages [23] -->
m

<!-- b002196 | furniture | pages [23] -->
m

<!-- b002197 | furniture | pages [23] -->
m

<!-- b002198 | furniture | pages [23] -->
m

<!-- b002199 | furniture | pages [23] -->
m

<!-- b002200 | furniture | pages [23] -->
m

<!-- b002201 | furniture | pages [23] -->
m

<!-- b002202 | furniture | pages [23] -->
m

<!-- b002203 | furniture | pages [23] -->
m

<!-- b002204 | furniture | pages [23] -->
m

<!-- b002205 | furniture | pages [23] -->
m

<!-- b002206 | furniture | pages [23] -->
m

<!-- b002207 | furniture | pages [23] -->
m

<!-- b002208 | furniture | pages [23] -->
m

<!-- b002209 | furniture | pages [23] -->
m

<!-- b002210 | furniture | pages [23] -->
m

<!-- b002211 | furniture | pages [23] -->
m

<!-- b002212 | furniture | pages [23] -->
m

<!-- b002213 | furniture | pages [23] -->
m

<!-- b002214 | furniture | pages [23] -->
m

<!-- b002215 | furniture | pages [23] -->
m

<!-- b002216 | furniture | pages [23] -->
m

<!-- b002217 | furniture | pages [23] -->
m

<!-- b002218 | furniture | pages [23] -->
m

<!-- b002219 | furniture | pages [23] -->
m

<!-- b002220 | furniture | pages [23] -->
m

<!-- b002221 | furniture | pages [23] -->
m

<!-- b002222 | furniture | pages [23] -->
m

<!-- b002223 | furniture | pages [23] -->
m

<!-- b002224 | furniture | pages [23] -->
m

<!-- b002225 | furniture | pages [23] -->
m

<!-- b002226 | furniture | pages [23] -->
m

<!-- b002227 | furniture | pages [23] -->
m

<!-- b002228 | furniture | pages [23] -->
m

<!-- b002229 | furniture | pages [23] -->
m

<!-- b002230 | furniture | pages [23] -->
m

<!-- b002231 | furniture | pages [23] -->
m

<!-- b002232 | furniture | pages [23] -->
m

<!-- b002233 | furniture | pages [23] -->
m

<!-- b002234 | furniture | pages [23] -->
m

<!-- b002235 | furniture | pages [23] -->
m

<!-- b002236 | furniture | pages [23] -->
m

<!-- b002237 | furniture | pages [23] -->
m

<!-- b002238 | furniture | pages [23] -->
m

<!-- b002239 | furniture | pages [23] -->
m

<!-- b002240 | furniture | pages [23] -->
m

<!-- b002241 | furniture | pages [23] -->
m

<!-- b002242 | furniture | pages [23] -->
m

<!-- b002243 | furniture | pages [23] -->
m

<!-- b002244 | furniture | pages [24] -->
Team # 2502617

<!-- b002245 | furniture | pages [24] -->
Page 24 of 25

<!-- b002246 | references | pages [24] -->
[14]

<!-- b002247 | references | pages [24] -->
Young Dae Ko and Byung Duk Song. “Sustainable service design and revenue management

<!-- b002248 | references | pages [24] -->
for electric tour bus systems: seoul city tour bus service and the eco-mileage program”.

<!-- b002249 | references | pages [24] -->
In: JOURNAL OF SUSTAINABLE TOURISM 27 (2019). doi: 10.1080/09669582.2018.

<!-- b002250 | references | pages [24] -->
m

<!-- b002251 | references | pages [24] -->
m

<!-- b002252 | references | pages [24] -->
m

<!-- b002253 | references | pages [24] -->
m

<!-- b002254 | references | pages [24] -->
m

<!-- b002255 | references | pages [24] -->
m

<!-- b002256 | references | pages [24] -->
m

<!-- b002257 | references | pages [24] -->
m

<!-- b002258 | references | pages [24] -->
m

<!-- b002259 | references | pages [24] -->
m

<!-- b002260 | references | pages [24] -->
m

<!-- b002261 | references | pages [24] -->
m

<!-- b002262 | references | pages [24] -->
m

<!-- b002263 | references | pages [24] -->
m

<!-- b002264 | references | pages [24] -->
m

<!-- b002265 | references | pages [24] -->
m

<!-- b002266 | references | pages [24] -->
m

<!-- b002267 | references | pages [24] -->
m

<!-- b002268 | references | pages [24] -->
m

<!-- b002269 | references | pages [24] -->
m

<!-- b002270 | references | pages [24] -->
m

<!-- b002271 | references | pages [24] -->
m

<!-- b002272 | references | pages [24] -->
m

<!-- b002273 | references | pages [24] -->
m

<!-- b002274 | references | pages [24] -->
m

<!-- b002275 | references | pages [24] -->
m

<!-- b002276 | references | pages [24] -->
m

<!-- b002277 | references | pages [24] -->
m

<!-- b002278 | references | pages [24] -->
m

<!-- b002279 | references | pages [24] -->
m

<!-- b002280 | references | pages [24] -->
m

<!-- b002281 | references | pages [24] -->
m

<!-- b002282 | references | pages [24] -->
m

<!-- b002283 | references | pages [24] -->
m

<!-- b002284 | references | pages [24] -->
m

<!-- b002285 | references | pages [24] -->
m

<!-- b002286 | references | pages [24] -->
m

<!-- b002287 | references | pages [24] -->
m

<!-- b002288 | references | pages [24] -->
m

<!-- b002289 | references | pages [24] -->
m

<!-- b002290 | references | pages [24] -->
m

<!-- b002291 | references | pages [24] -->
m

<!-- b002292 | references | pages [24] -->
m

<!-- b002293 | references | pages [24] -->
m

<!-- b002294 | references | pages [24] -->
m

<!-- b002295 | references | pages [24] -->
m

<!-- b002296 | references | pages [24] -->
m

<!-- b002297 | references | pages [24] -->
m

<!-- b002298 | references | pages [24] -->
m

<!-- b002299 | references | pages [24] -->
m

<!-- b002300 | references | pages [24] -->
m

<!-- b002301 | references | pages [24] -->
m

<!-- b002302 | references | pages [24] -->
m

<!-- b002303 | references | pages [24] -->
m

<!-- b002304 | references | pages [24] -->
m

<!-- b002305 | references | pages [24] -->
m

<!-- b002306 | references | pages [24] -->
m

<!-- b002307 | references | pages [24] -->
m

<!-- b002308 | references | pages [24] -->
m

<!-- b002309 | references | pages [24] -->
m

<!-- b002310 | references | pages [24] -->
m

<!-- b002311 | references | pages [24] -->
m

<!-- b002312 | references | pages [24] -->
m

<!-- b002313 | references | pages [24] -->
m

<!-- b002314 | references | pages [24] -->
m

<!-- b002315 | references | pages [24] -->
m

<!-- b002316 | references | pages [24] -->
m

<!-- b002317 | references | pages [24] -->
m

<!-- b002318 | references | pages [24] -->
m

<!-- b002319 | references | pages [24] -->
m

<!-- b002320 | references | pages [24] -->
m

<!-- b002321 | references | pages [24] -->
m

<!-- b002322 | references | pages [24] -->
m

<!-- b002323 | references | pages [24] -->
m

<!-- b002324 | references | pages [24] -->
m

<!-- b002325 | references | pages [24] -->
m

<!-- b002326 | references | pages [24] -->
m

<!-- b002327 | references | pages [24] -->
m

<!-- b002328 | references | pages [24] -->
m

<!-- b002329 | references | pages [24] -->
m

<!-- b002330 | references | pages [24] -->
m

<!-- b002331 | references | pages [24] -->
m

<!-- b002332 | references | pages [24] -->
m

<!-- b002333 | references | pages [24] -->
m

<!-- b002334 | references | pages [24] -->
m

<!-- b002335 | references | pages [24] -->
m

<!-- b002336 | references | pages [24] -->
m

<!-- b002337 | references | pages [24] -->
m

<!-- b002338 | references | pages [24] -->
m

<!-- b002339 | references | pages [24] -->
m

<!-- b002340 | references | pages [24] -->
m

<!-- b002341 | references | pages [24] -->
m

<!-- b002342 | references | pages [24] -->
m

<!-- b002343 | references | pages [24] -->
m

<!-- b002344 | references | pages [24] -->
m

<!-- b002345 | references | pages [24] -->
m

<!-- b002346 | references | pages [24] -->
m

<!-- b002347 | references | pages [24] -->
m

<!-- b002348 | references | pages [24] -->
m

<!-- b002349 | references | pages [24] -->
m

<!-- b002350 | references | pages [24] -->
m

<!-- b002351 | references | pages [24] -->
m

<!-- b002352 | references | pages [24] -->
m

<!-- b002353 | references | pages [24] -->
m

<!-- b002354 | references | pages [24] -->
m

<!-- b002355 | references | pages [24] -->
m

<!-- b002356 | references | pages [24] -->
m

<!-- b002357 | references | pages [24] -->
m

<!-- b002358 | references | pages [24] -->
m

<!-- b002359 | references | pages [24] -->
m

<!-- b002360 | references | pages [24] -->
m

<!-- b002361 | references | pages [24] -->
m

<!-- b002362 | references | pages [24] -->
m

<!-- b002363 | references | pages [24] -->
m

<!-- b002364 | references | pages [24] -->
m

<!-- b002365 | references | pages [24] -->
m

<!-- b002366 | references | pages [24] -->
m

<!-- b002367 | references | pages [24] -->
m

<!-- b002368 | references | pages [24] -->
m

<!-- b002369 | references | pages [24] -->
m

<!-- b002370 | references | pages [24] -->
m

<!-- b002371 | references | pages [24] -->
m

<!-- b002372 | references | pages [24] -->
m

<!-- b002373 | references | pages [24] -->
m

<!-- b002374 | references | pages [24] -->
m

<!-- b002375 | references | pages [24] -->
m

<!-- b002376 | references | pages [24] -->
m

<!-- b002377 | references | pages [24] -->
m

<!-- b002378 | references | pages [24] -->
m

<!-- b002379 | references | pages [24] -->
m

<!-- b002380 | references | pages [24] -->
m

<!-- b002381 | references | pages [24] -->
m

<!-- b002382 | references | pages [24] -->
m

<!-- b002383 | references | pages [24] -->
m

<!-- b002384 | references | pages [24] -->
m

<!-- b002385 | references | pages [24] -->
m

<!-- b002386 | references | pages [24] -->
m

<!-- b002387 | references | pages [24] -->
m

<!-- b002388 | references | pages [24] -->
m

<!-- b002389 | references | pages [24] -->
m

<!-- b002390 | references | pages [24] -->
m

<!-- b002391 | references | pages [24] -->
m

<!-- b002392 | references | pages [24] -->
m

<!-- b002393 | references | pages [24] -->
m

<!-- b002394 | references | pages [24] -->
m

<!-- b002395 | references | pages [24] -->
m

<!-- b002396 | references | pages [24] -->
1560453.

<!-- b002397 | references | pages [24] -->
m

<!-- b002398 | references | pages [24] -->
m

<!-- b002399 | references | pages [24] -->
m

<!-- b002400 | references | pages [24] -->
m

<!-- b002401 | references | pages [24] -->
m

<!-- b002402 | references | pages [24] -->
m

<!-- b002403 | references | pages [24] -->
m

<!-- b002404 | references | pages [24] -->
m

<!-- b002405 | references | pages [24] -->
m

<!-- b002406 | references | pages [24] -->
m

<!-- b002407 | references | pages [24] -->
m

<!-- b002408 | references | pages [24] -->
m

<!-- b002409 | references | pages [24] -->
m

<!-- b002410 | references | pages [24] -->
m

<!-- b002411 | references | pages [24] -->
m

<!-- b002412 | references | pages [24] -->
m

<!-- b002413 | references | pages [24] -->
m

<!-- b002414 | references | pages [24] -->
m

<!-- b002415 | references | pages [24] -->
m

<!-- b002416 | references | pages [24] -->
m

<!-- b002417 | references | pages [24] -->
m

<!-- b002418 | references | pages [24] -->
m

<!-- b002419 | references | pages [24] -->
m

<!-- b002420 | references | pages [24] -->
m

<!-- b002421 | references | pages [24] -->
m

<!-- b002422 | references | pages [24] -->
m

<!-- b002423 | references | pages [24] -->
m

<!-- b002424 | references | pages [24] -->
m

<!-- b002425 | references | pages [24] -->
m

<!-- b002426 | references | pages [24] -->
m

<!-- b002427 | references | pages [24] -->
m

<!-- b002428 | references | pages [24] -->
m

<!-- b002429 | references | pages [24] -->
m

<!-- b002430 | references | pages [24] -->
m

<!-- b002431 | references | pages [24] -->
m

<!-- b002432 | references | pages [24] -->
m

<!-- b002433 | references | pages [24] -->
m

<!-- b002434 | references | pages [24] -->
m

<!-- b002435 | references | pages [24] -->
m

<!-- b002436 | references | pages [24] -->
m

<!-- b002437 | references | pages [24] -->
m

<!-- b002438 | references | pages [24] -->
m

<!-- b002439 | references | pages [24] -->
m

<!-- b002440 | references | pages [24] -->
m

<!-- b002441 | references | pages [24] -->
m

<!-- b002442 | references | pages [24] -->
m

<!-- b002443 | references | pages [24] -->
m

<!-- b002444 | references | pages [24] -->
m

<!-- b002445 | references | pages [24] -->
m

<!-- b002446 | references | pages [24] -->
m

<!-- b002447 | references | pages [24] -->
m

<!-- b002448 | references | pages [24] -->
m

<!-- b002449 | references | pages [24] -->
m

<!-- b002450 | references | pages [24] -->
m

<!-- b002451 | references | pages [24] -->
m

<!-- b002452 | references | pages [24] -->
m

<!-- b002453 | references | pages [24] -->
m

<!-- b002454 | references | pages [24] -->
m

<!-- b002455 | references | pages [24] -->
m

<!-- b002456 | references | pages [24] -->
m

<!-- b002457 | references | pages [24] -->
m

<!-- b002458 | references | pages [24] -->
m

<!-- b002459 | references | pages [24] -->
m

<!-- b002460 | references | pages [24] -->
m

<!-- b002461 | references | pages [24] -->
m

<!-- b002462 | references | pages [24] -->
m

<!-- b002463 | references | pages [24] -->
m

<!-- b002464 | references | pages [24] -->
m

<!-- b002465 | references | pages [24] -->
m

<!-- b002466 | references | pages [24] -->
m

<!-- b002467 | references | pages [24] -->
m

<!-- b002468 | references | pages [24] -->
m

<!-- b002469 | references | pages [24] -->
m

<!-- b002470 | references | pages [24] -->
m

<!-- b002471 | references | pages [24] -->
m

<!-- b002472 | references | pages [24] -->
m

<!-- b002473 | references | pages [24] -->
m

<!-- b002474 | references | pages [24] -->
m

<!-- b002475 | references | pages [24] -->
m

<!-- b002476 | references | pages [24] -->
m

<!-- b002477 | references | pages [24] -->
m

<!-- b002478 | references | pages [24] -->
m

<!-- b002479 | references | pages [24] -->
m

<!-- b002480 | references | pages [24] -->
m

<!-- b002481 | references | pages [24] -->
m

<!-- b002482 | references | pages [24] -->
m

<!-- b002483 | references | pages [24] -->
m

<!-- b002484 | references | pages [24] -->
m

<!-- b002485 | references | pages [24] -->
m

<!-- b002486 | references | pages [24] -->
m

<!-- b002487 | references | pages [24] -->
m

<!-- b002488 | references | pages [24] -->
m

<!-- b002489 | references | pages [24] -->
m

<!-- b002490 | references | pages [24] -->
m

<!-- b002491 | references | pages [24] -->
m

<!-- b002492 | references | pages [24] -->
m

<!-- b002493 | references | pages [24] -->
m

<!-- b002494 | references | pages [24] -->
m

<!-- b002495 | references | pages [24] -->
m

<!-- b002496 | references | pages [24] -->
m

<!-- b002497 | references | pages [24] -->
m

<!-- b002498 | references | pages [24] -->
m

<!-- b002499 | references | pages [24] -->
m

<!-- b002500 | references | pages [24] -->
m

<!-- b002501 | references | pages [24] -->
m

<!-- b002502 | references | pages [24] -->
m

<!-- b002503 | references | pages [24] -->
m

<!-- b002504 | references | pages [24] -->
m

<!-- b002505 | references | pages [24] -->
m

<!-- b002506 | references | pages [24] -->
m

<!-- b002507 | references | pages [24] -->
m

<!-- b002508 | references | pages [24] -->
m

<!-- b002509 | references | pages [24] -->
m

<!-- b002510 | references | pages [24] -->
m

<!-- b002511 | references | pages [24] -->
m

<!-- b002512 | references | pages [24] -->
m

<!-- b002513 | references | pages [24] -->
m

<!-- b002514 | references | pages [24] -->
m

<!-- b002515 | references | pages [24] -->
m

<!-- b002516 | references | pages [24] -->
m

<!-- b002517 | references | pages [24] -->
m

<!-- b002518 | references | pages [24] -->
m

<!-- b002519 | references | pages [24] -->
m

<!-- b002520 | references | pages [24] -->
m

<!-- b002521 | references | pages [24] -->
m

<!-- b002522 | references | pages [24] -->
m

<!-- b002523 | references | pages [24] -->
m

<!-- b002524 | references | pages [24] -->
m

<!-- b002525 | references | pages [24] -->
m

<!-- b002526 | references | pages [24] -->
m

<!-- b002527 | references | pages [24] -->
m

<!-- b002528 | references | pages [24] -->
m

<!-- b002529 | references | pages [24] -->
m

<!-- b002530 | references | pages [24] -->
m

<!-- b002531 | references | pages [24] -->
m

<!-- b002532 | references | pages [24] -->
m

<!-- b002533 | references | pages [24] -->
m

<!-- b002534 | references | pages [24] -->
m

<!-- b002535 | references | pages [24] -->
m

<!-- b002536 | references | pages [24] -->
m

<!-- b002537 | references | pages [24] -->
m

<!-- b002538 | references | pages [24] -->
m

<!-- b002539 | references | pages [24] -->
m

<!-- b002540 | references | pages [24] -->
m

<!-- b002541 | references | pages [24] -->
m

<!-- b002542 | references | pages [24] -->
m

<!-- b002543 | references | pages [24] -->
m

<!-- b002544 | references | pages [24] -->
m

<!-- b002545 | references | pages [24] -->
m

<!-- b002546 | references | pages [24] -->
m

<!-- b002547 | references | pages [24] -->
m

<!-- b002548 | references | pages [24] -->
m

<!-- b002549 | references | pages [24] -->
m

<!-- b002550 | references | pages [24] -->
m

<!-- b002551 | references | pages [24] -->
m

<!-- b002552 | references | pages [24] -->
m

<!-- b002553 | references | pages [24] -->
m

<!-- b002554 | references | pages [24] -->
m

<!-- b002555 | references | pages [24] -->
m

<!-- b002556 | references | pages [24] -->
m

<!-- b002557 | references | pages [24] -->
m

<!-- b002558 | references | pages [24] -->
m

<!-- b002559 | references | pages [24] -->
m

<!-- b002560 | references | pages [24] -->
m

<!-- b002561 | references | pages [24] -->
m

<!-- b002562 | references | pages [24] -->
m

<!-- b002563 | references | pages [24] -->
m

<!-- b002564 | references | pages [24] -->
m

<!-- b002565 | references | pages [24] -->
m

<!-- b002566 | references | pages [24] -->
m

<!-- b002567 | references | pages [24] -->
m

<!-- b002568 | references | pages [24] -->
m

<!-- b002569 | references | pages [24] -->
m

<!-- b002570 | references | pages [24] -->
m

<!-- b002571 | references | pages [24] -->
m

<!-- b002572 | references | pages [24] -->
m

<!-- b002573 | references | pages [24] -->
m

<!-- b002574 | references | pages [24] -->
m

<!-- b002575 | references | pages [24] -->
m

<!-- b002576 | references | pages [24] -->
m

<!-- b002577 | references | pages [24] -->
m

<!-- b002578 | references | pages [24] -->
m

<!-- b002579 | references | pages [24] -->
m

<!-- b002580 | references | pages [24] -->
m

<!-- b002581 | references | pages [24] -->
m

<!-- b002582 | references | pages [24] -->
m

<!-- b002583 | references | pages [24] -->
[15]

<!-- b002584 | references | pages [24] -->
Xiangping Wang and Huajun Tang. “Research on Tourism Supply Chain Coordination Un-

<!-- b002585 | references | pages [24] -->
m

<!-- b002586 | references | pages [24] -->
m

<!-- b002587 | references | pages [24] -->
m

<!-- b002588 | references | pages [24] -->
m

<!-- b002589 | references | pages [24] -->
m

<!-- b002590 | references | pages [24] -->
m

<!-- b002591 | references | pages [24] -->
m

<!-- b002592 | references | pages [24] -->
m

<!-- b002593 | references | pages [24] -->
m

<!-- b002594 | references | pages [24] -->
m

<!-- b002595 | references | pages [24] -->
m

<!-- b002596 | references | pages [24] -->
m

<!-- b002597 | references | pages [24] -->
m

<!-- b002598 | references | pages [24] -->
m

<!-- b002599 | references | pages [24] -->
m

<!-- b002600 | references | pages [24] -->
m

<!-- b002601 | references | pages [24] -->
m

<!-- b002602 | references | pages [24] -->
m

<!-- b002603 | references | pages [24] -->
m

<!-- b002604 | references | pages [24] -->
m

<!-- b002605 | references | pages [24] -->
m

<!-- b002606 | references | pages [24] -->
m

<!-- b002607 | references | pages [24] -->
m

<!-- b002608 | references | pages [24] -->
m

<!-- b002609 | references | pages [24] -->
m

<!-- b002610 | references | pages [24] -->
m

<!-- b002611 | references | pages [24] -->
m

<!-- b002612 | references | pages [24] -->
m

<!-- b002613 | references | pages [24] -->
m

<!-- b002614 | references | pages [24] -->
m

<!-- b002615 | references | pages [24] -->
m

<!-- b002616 | references | pages [24] -->
m

<!-- b002617 | references | pages [24] -->
m

<!-- b002618 | references | pages [24] -->
m

<!-- b002619 | references | pages [24] -->
m

<!-- b002620 | references | pages [24] -->
m

<!-- b002621 | references | pages [24] -->
m

<!-- b002622 | references | pages [24] -->
m

<!-- b002623 | references | pages [24] -->
m

<!-- b002624 | references | pages [24] -->
m

<!-- b002625 | references | pages [24] -->
m

<!-- b002626 | references | pages [24] -->
m

<!-- b002627 | references | pages [24] -->
m

<!-- b002628 | references | pages [24] -->
m

<!-- b002629 | references | pages [24] -->
m

<!-- b002630 | references | pages [24] -->
m

<!-- b002631 | references | pages [24] -->
m

<!-- b002632 | references | pages [24] -->
m

<!-- b002633 | references | pages [24] -->
m

<!-- b002634 | references | pages [24] -->
m

<!-- b002635 | references | pages [24] -->
m

<!-- b002636 | references | pages [24] -->
m

<!-- b002637 | references | pages [24] -->
m

<!-- b002638 | references | pages [24] -->
m

<!-- b002639 | references | pages [24] -->
m

<!-- b002640 | references | pages [24] -->
m

<!-- b002641 | references | pages [24] -->
m

<!-- b002642 | references | pages [24] -->
m

<!-- b002643 | references | pages [24] -->
m

<!-- b002644 | references | pages [24] -->
m

<!-- b002645 | references | pages [24] -->
m

<!-- b002646 | references | pages [24] -->
m

<!-- b002647 | references | pages [24] -->
m

<!-- b002648 | references | pages [24] -->
m

<!-- b002649 | references | pages [24] -->
m

<!-- b002650 | references | pages [24] -->
m

<!-- b002651 | references | pages [24] -->
m

<!-- b002652 | references | pages [24] -->
m

<!-- b002653 | references | pages [24] -->
m

<!-- b002654 | references | pages [24] -->
m

<!-- b002655 | references | pages [24] -->
m

<!-- b002656 | references | pages [24] -->
m

<!-- b002657 | references | pages [24] -->
m

<!-- b002658 | references | pages [24] -->
m

<!-- b002659 | references | pages [24] -->
m

<!-- b002660 | references | pages [24] -->
m

<!-- b002661 | references | pages [24] -->
m

<!-- b002662 | references | pages [24] -->
m

<!-- b002663 | references | pages [24] -->
m

<!-- b002664 | references | pages [24] -->
m

<!-- b002665 | references | pages [24] -->
m

<!-- b002666 | references | pages [24] -->
m

<!-- b002667 | references | pages [24] -->
m

<!-- b002668 | references | pages [24] -->
m

<!-- b002669 | references | pages [24] -->
m

<!-- b002670 | references | pages [24] -->
m

<!-- b002671 | references | pages [24] -->
m

<!-- b002672 | references | pages [24] -->
m

<!-- b002673 | references | pages [24] -->
m

<!-- b002674 | references | pages [24] -->
m

<!-- b002675 | references | pages [24] -->
m

<!-- b002676 | references | pages [24] -->
m

<!-- b002677 | references | pages [24] -->
m

<!-- b002678 | references | pages [24] -->
m

<!-- b002679 | references | pages [24] -->
m

<!-- b002680 | references | pages [24] -->
m

<!-- b002681 | references | pages [24] -->
m

<!-- b002682 | references | pages [24] -->
m

<!-- b002683 | references | pages [24] -->
m

<!-- b002684 | references | pages [24] -->
m

<!-- b002685 | references | pages [24] -->
m

<!-- b002686 | references | pages [24] -->
m

<!-- b002687 | references | pages [24] -->
m

<!-- b002688 | references | pages [24] -->
m

<!-- b002689 | references | pages [24] -->
m

<!-- b002690 | references | pages [24] -->
m

<!-- b002691 | references | pages [24] -->
m

<!-- b002692 | references | pages [24] -->
m

<!-- b002693 | references | pages [24] -->
m

<!-- b002694 | references | pages [24] -->
m

<!-- b002695 | references | pages [24] -->
m

<!-- b002696 | references | pages [24] -->
m

<!-- b002697 | references | pages [24] -->
m

<!-- b002698 | references | pages [24] -->
m

<!-- b002699 | references | pages [24] -->
m

<!-- b002700 | references | pages [24] -->
m

<!-- b002701 | references | pages [24] -->
m

<!-- b002702 | references | pages [24] -->
m

<!-- b002703 | references | pages [24] -->
m

<!-- b002704 | references | pages [24] -->
m

<!-- b002705 | references | pages [24] -->
m

<!-- b002706 | references | pages [24] -->
m

<!-- b002707 | references | pages [24] -->
m

<!-- b002708 | references | pages [24] -->
m

<!-- b002709 | references | pages [24] -->
m

<!-- b002710 | references | pages [24] -->
m

<!-- b002711 | references | pages [24] -->
m

<!-- b002712 | references | pages [24] -->
m

<!-- b002713 | references | pages [24] -->
m

<!-- b002714 | references | pages [24] -->
m

<!-- b002715 | references | pages [24] -->
m

<!-- b002716 | references | pages [24] -->
m

<!-- b002717 | references | pages [24] -->
m

<!-- b002718 | references | pages [24] -->
m

<!-- b002719 | references | pages [24] -->
m

<!-- b002720 | references | pages [24] -->
m

<!-- b002721 | references | pages [24] -->
m

<!-- b002722 | references | pages [24] -->
m

<!-- b002723 | references | pages [24] -->
m

<!-- b002724 | references | pages [24] -->
m

<!-- b002725 | references | pages [24] -->
m

<!-- b002726 | references | pages [24] -->
m

<!-- b002727 | references | pages [24] -->
m

<!-- b002728 | references | pages [24] -->
m

<!-- b002729 | references | pages [24] -->
m

<!-- b002730 | references | pages [24] -->
m

<!-- b002731 | references | pages [24] -->
m

<!-- b002732 | references | pages [24] -->
m

<!-- b002733 | references | pages [24] -->
m

<!-- b002734 | references | pages [24] -->
m

<!-- b002735 | references | pages [24] -->
der the Background of Low-Carbon Tourism”. In: (). doi: 10.1109/ieem45057.2020.

<!-- b002736 | references | pages [24] -->
m

<!-- b002737 | references | pages [24] -->
m

<!-- b002738 | references | pages [24] -->
m

<!-- b002739 | references | pages [24] -->
m

<!-- b002740 | references | pages [24] -->
m

<!-- b002741 | references | pages [24] -->
m

<!-- b002742 | references | pages [24] -->
m

<!-- b002743 | references | pages [24] -->
m

<!-- b002744 | references | pages [24] -->
m

<!-- b002745 | references | pages [24] -->
m

<!-- b002746 | references | pages [24] -->
m

<!-- b002747 | references | pages [24] -->
m

<!-- b002748 | references | pages [24] -->
m

<!-- b002749 | references | pages [24] -->
m

<!-- b002750 | references | pages [24] -->
m

<!-- b002751 | references | pages [24] -->
m

<!-- b002752 | references | pages [24] -->
m

<!-- b002753 | references | pages [24] -->
m

<!-- b002754 | references | pages [24] -->
m

<!-- b002755 | references | pages [24] -->
m

<!-- b002756 | references | pages [24] -->
m

<!-- b002757 | references | pages [24] -->
m

<!-- b002758 | references | pages [24] -->
m

<!-- b002759 | references | pages [24] -->
m

<!-- b002760 | references | pages [24] -->
m

<!-- b002761 | references | pages [24] -->
m

<!-- b002762 | references | pages [24] -->
m

<!-- b002763 | references | pages [24] -->
m

<!-- b002764 | references | pages [24] -->
m

<!-- b002765 | references | pages [24] -->
m

<!-- b002766 | references | pages [24] -->
m

<!-- b002767 | references | pages [24] -->
m

<!-- b002768 | references | pages [24] -->
m

<!-- b002769 | references | pages [24] -->
m

<!-- b002770 | references | pages [24] -->
m

<!-- b002771 | references | pages [24] -->
m

<!-- b002772 | references | pages [24] -->
m

<!-- b002773 | references | pages [24] -->
m

<!-- b002774 | references | pages [24] -->
m

<!-- b002775 | references | pages [24] -->
m

<!-- b002776 | references | pages [24] -->
m

<!-- b002777 | references | pages [24] -->
m

<!-- b002778 | references | pages [24] -->
m

<!-- b002779 | references | pages [24] -->
m

<!-- b002780 | references | pages [24] -->
m

<!-- b002781 | references | pages [24] -->
m

<!-- b002782 | references | pages [24] -->
m

<!-- b002783 | references | pages [24] -->
m

<!-- b002784 | references | pages [24] -->
m

<!-- b002785 | references | pages [24] -->
m

<!-- b002786 | references | pages [24] -->
m

<!-- b002787 | references | pages [24] -->
m

<!-- b002788 | references | pages [24] -->
m

<!-- b002789 | references | pages [24] -->
m

<!-- b002790 | references | pages [24] -->
m

<!-- b002791 | references | pages [24] -->
m

<!-- b002792 | references | pages [24] -->
m

<!-- b002793 | references | pages [24] -->
m

<!-- b002794 | references | pages [24] -->
m

<!-- b002795 | references | pages [24] -->
m

<!-- b002796 | references | pages [24] -->
m

<!-- b002797 | references | pages [24] -->
m

<!-- b002798 | references | pages [24] -->
m

<!-- b002799 | references | pages [24] -->
m

<!-- b002800 | references | pages [24] -->
m

<!-- b002801 | references | pages [24] -->
m

<!-- b002802 | references | pages [24] -->
m

<!-- b002803 | references | pages [24] -->
m

<!-- b002804 | references | pages [24] -->
m

<!-- b002805 | references | pages [24] -->
m

<!-- b002806 | references | pages [24] -->
m

<!-- b002807 | references | pages [24] -->
m

<!-- b002808 | references | pages [24] -->
m

<!-- b002809 | references | pages [24] -->
m

<!-- b002810 | references | pages [24] -->
m

<!-- b002811 | references | pages [24] -->
m

<!-- b002812 | references | pages [24] -->
m

<!-- b002813 | references | pages [24] -->
m

<!-- b002814 | references | pages [24] -->
m

<!-- b002815 | references | pages [24] -->
m

<!-- b002816 | references | pages [24] -->
m

<!-- b002817 | references | pages [24] -->
m

<!-- b002818 | references | pages [24] -->
m

<!-- b002819 | references | pages [24] -->
m

<!-- b002820 | references | pages [24] -->
m

<!-- b002821 | references | pages [24] -->
m

<!-- b002822 | references | pages [24] -->
m

<!-- b002823 | references | pages [24] -->
m

<!-- b002824 | references | pages [24] -->
m

<!-- b002825 | references | pages [24] -->
m

<!-- b002826 | references | pages [24] -->
m

<!-- b002827 | references | pages [24] -->
m

<!-- b002828 | references | pages [24] -->
m

<!-- b002829 | references | pages [24] -->
m

<!-- b002830 | references | pages [24] -->
m

<!-- b002831 | references | pages [24] -->
m

<!-- b002832 | references | pages [24] -->
m

<!-- b002833 | references | pages [24] -->
m

<!-- b002834 | references | pages [24] -->
m

<!-- b002835 | references | pages [24] -->
m

<!-- b002836 | references | pages [24] -->
m

<!-- b002837 | references | pages [24] -->
m

<!-- b002838 | references | pages [24] -->
m

<!-- b002839 | references | pages [24] -->
m

<!-- b002840 | references | pages [24] -->
m

<!-- b002841 | references | pages [24] -->
m

<!-- b002842 | references | pages [24] -->
m

<!-- b002843 | references | pages [24] -->
m

<!-- b002844 | references | pages [24] -->
m

<!-- b002845 | references | pages [24] -->
m

<!-- b002846 | references | pages [24] -->
m

<!-- b002847 | references | pages [24] -->
m

<!-- b002848 | references | pages [24] -->
m

<!-- b002849 | references | pages [24] -->
m

<!-- b002850 | references | pages [24] -->
m

<!-- b002851 | references | pages [24] -->
m

<!-- b002852 | references | pages [24] -->
m

<!-- b002853 | references | pages [24] -->
m

<!-- b002854 | references | pages [24] -->
m

<!-- b002855 | references | pages [24] -->
m

<!-- b002856 | references | pages [24] -->
m

<!-- b002857 | references | pages [24] -->
m

<!-- b002858 | references | pages [24] -->
m

<!-- b002859 | references | pages [24] -->
m

<!-- b002860 | references | pages [24] -->
m

<!-- b002861 | references | pages [24] -->
m

<!-- b002862 | references | pages [24] -->
m

<!-- b002863 | references | pages [24] -->
m

<!-- b002864 | references | pages [24] -->
m

<!-- b002865 | references | pages [24] -->
m

<!-- b002866 | references | pages [24] -->
m

<!-- b002867 | references | pages [24] -->
m

<!-- b002868 | references | pages [24] -->
m

<!-- b002869 | references | pages [24] -->
m

<!-- b002870 | references | pages [24] -->
m

<!-- b002871 | references | pages [24] -->
m

<!-- b002872 | references | pages [24] -->
m

<!-- b002873 | references | pages [24] -->
m

<!-- b002874 | references | pages [24] -->
m

<!-- b002875 | references | pages [24] -->
m

<!-- b002876 | references | pages [24] -->
m

<!-- b002877 | references | pages [24] -->
m

<!-- b002878 | references | pages [24] -->
m

<!-- b002879 | references | pages [24] -->
m

<!-- b002880 | references | pages [24] -->
m

<!-- b002881 | references | pages [24] -->
9309894.

<!-- b002882 | references | pages [24] -->
m

<!-- b002883 | references | pages [24] -->
m

<!-- b002884 | references | pages [24] -->
m

<!-- b002885 | references | pages [24] -->
m

<!-- b002886 | references | pages [24] -->
m

<!-- b002887 | references | pages [24] -->
m

<!-- b002888 | references | pages [24] -->
m

<!-- b002889 | references | pages [24] -->
m

<!-- b002890 | references | pages [24] -->
m

<!-- b002891 | references | pages [24] -->
m

<!-- b002892 | references | pages [24] -->
m

<!-- b002893 | references | pages [24] -->
m

<!-- b002894 | references | pages [24] -->
m

<!-- b002895 | references | pages [24] -->
m

<!-- b002896 | references | pages [24] -->
m

<!-- b002897 | references | pages [24] -->
m

<!-- b002898 | references | pages [24] -->
m

<!-- b002899 | references | pages [24] -->
m

<!-- b002900 | references | pages [24] -->
m

<!-- b002901 | references | pages [24] -->
m

<!-- b002902 | references | pages [24] -->
m

<!-- b002903 | references | pages [24] -->
m

<!-- b002904 | references | pages [24] -->
m

<!-- b002905 | references | pages [24] -->
m

<!-- b002906 | references | pages [24] -->
m

<!-- b002907 | references | pages [24] -->
m

<!-- b002908 | references | pages [24] -->
m

<!-- b002909 | references | pages [24] -->
m

<!-- b002910 | references | pages [24] -->
m

<!-- b002911 | references | pages [24] -->
m

<!-- b002912 | references | pages [24] -->
m

<!-- b002913 | references | pages [24] -->
m

<!-- b002914 | references | pages [24] -->
m

<!-- b002915 | references | pages [24] -->
m

<!-- b002916 | references | pages [24] -->
m

<!-- b002917 | references | pages [24] -->
m

<!-- b002918 | references | pages [24] -->
m

<!-- b002919 | references | pages [24] -->
m

<!-- b002920 | references | pages [24] -->
m

<!-- b002921 | references | pages [24] -->
m

<!-- b002922 | references | pages [24] -->
m

<!-- b002923 | references | pages [24] -->
m

<!-- b002924 | references | pages [24] -->
m

<!-- b002925 | references | pages [24] -->
m

<!-- b002926 | references | pages [24] -->
m

<!-- b002927 | references | pages [24] -->
m

<!-- b002928 | references | pages [24] -->
m

<!-- b002929 | references | pages [24] -->
m

<!-- b002930 | references | pages [24] -->
m

<!-- b002931 | references | pages [24] -->
m

<!-- b002932 | references | pages [24] -->
m

<!-- b002933 | references | pages [24] -->
m

<!-- b002934 | references | pages [24] -->
m

<!-- b002935 | references | pages [24] -->
m

<!-- b002936 | references | pages [24] -->
m

<!-- b002937 | references | pages [24] -->
m

<!-- b002938 | references | pages [24] -->
m

<!-- b002939 | references | pages [24] -->
m

<!-- b002940 | references | pages [24] -->
m

<!-- b002941 | references | pages [24] -->
m

<!-- b002942 | references | pages [24] -->
[16]

<!-- b002943 | references | pages [24] -->
url: https://foe.org/news/cruise-passengers-carbon/.

<!-- b002944 | references | pages [24] -->
[17]

<!-- b002945 | references | pages [24] -->
Bernard M. S. van Praag. “Perspectives from the happiness literature and the role of new

<!-- b002946 | references | pages [24] -->
instruments for policy analysis”. In: CESIFO ECONOMIC STUDIES 53 (2007). doi: 10.

<!-- b002947 | references | pages [24] -->
1093/cesifo/ifm002.

<!-- b002948 | references | pages [24] -->
[18]

<!-- b002949 | references | pages [24] -->
Frank Ackerman, Elizabeth A. Stanton, and Ramon Bueno. “CRED: A new model of cli-

<!-- b002950 | references | pages [24] -->
mate and development”. In: ECOLOGICAL ECONOMICS 85 (2013). doi: 10.1016/j.

<!-- b002951 | references | pages [24] -->
ecolecon.2011.04.006.

<!-- b002952 | references | pages [24] -->
[19]

<!-- b002953 | references | pages [24] -->
url: https://meric.mo.gov/.

<!-- b002954 | references | pages [24] -->
[20]

<!-- b002955 | references | pages [24] -->
url: https://www.bea.gov/data/gdp/gdp-state.

<!-- b002956 | references | pages [24] -->
[21]

<!-- b002957 | references | pages [24] -->
url: https://epi.yale.edu/.

<!-- b002958 | references | pages [24] -->
关注数学模型

<!-- b002959 | furniture | pages [24] -->
2

<!-- b002960 | furniture | pages [24] -->
MATHmodels

<!-- b002961 | furniture | pages [24] -->
获取更多资讯

<!-- b002962 | furniture | pages [25] -->
Team # 2502617

<!-- b002963 | furniture | pages [25] -->
Page 25 of 25

<!-- b002964 | heading | pages [25] -->
Memo

<!-- b002965 | prose | pages [25] -->
To: Juneau Tourism Council

<!-- b002966 | prose | pages [25] -->
微信公众号：数学模型

<!-- b002967 | heading | pages [25] -->
Subject: Sustainable Tourism Management Recommendations for Juneau

<!-- b002968 | prose | pages [25] -->
Honorable Members of the Juneau Tourism Council,

<!-- b002969 | prose | pages [25] -->
The city of Juneau is attracting the attention and love of tourists with its beautiful natural landscape and comfortable living environment, which undoubtedly brings great economic benefits to the city of Juneau. However, it has been noted that due to the rapid increase in the number of tourists, the natural resources of the City of Juneau are being damaged and the normal life of the residents is being disturbed by the swarm of tourists.

<!-- b002970 | prose | pages [25] -->
Our assessment of the current state of tourism development in the City of Juneau indicates that if no management measures are taken to limit the number of visitors or protect the natural 微信号：MATHmodels environment, the number of visitors will remain above 1.6 million for the next decade, and the most popular attraction, the Mendenhall Glacier, will disappear from its current viewpoints within 25 years and completely recede within 90 years, which will inevitably affect the long- term tourism and economic development of the City of Juneau. As the makers of management decisions for tourism management in Juneau, it is important to develop appropriate management strategies to achieve sustainable tourism. To this end, we have constructed a mathematical model and propose the following actionable measures to you:

<!-- b002971 | prose | pages [25] -->
Measure 1: Increase Visitor Dispersion Methods: Increase publicity for niche attractions and limit visitor flow or periodically close popular scenic spots

<!-- b002972 | prose | pages [25] -->
Effect: The greater the dispersion of tourists, the more balanced the number of tourists accepted by each attraction, and when the dispersion of tourists is close to 1/n (n is the total number of attractions), the greater the total benefits.

<!-- b002973 | prose | pages [25] -->
Measure 2: Increase Tourist Consumption Methods: Increase tax rates and commodity prices at scenic spots Effect: When the tax rate and prices increase, the number of tourists decreases and the total benefits increases. The total benefit is greatest when the tax rate is adjusted to 0.58.

<!-- b002974 | prose | pages [25] -->
Measure 3: Determine the Optimal Number of Tourists Method: Analyze the number of tourists when the total benefits is maximum through Pareto optimality

<!-- b002975 | prose | pages [25] -->
Effect: Ensure the Sustainable evelopment of regional tourism and promote the maximization of social benefits. The social benefit is maximized when the total number of tourists is 1.32 million in the year.

<!-- b002976 | prose | pages [25] -->
Sincerely,

<!-- b002977 | furniture | pages [25] -->
Team #2502617

<!-- b002978 | prose | pages [25] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002979 | furniture | pages [25] -->
m

<!-- b002980 | furniture | pages [25] -->
m

<!-- b002981 | furniture | pages [25] -->
m

<!-- b002982 | furniture | pages [25] -->
m

<!-- b002983 | furniture | pages [25] -->
m

<!-- b002984 | furniture | pages [25] -->
m

<!-- b002985 | furniture | pages [25] -->
m

<!-- b002986 | furniture | pages [25] -->
m

<!-- b002987 | furniture | pages [25] -->
m

<!-- b002988 | furniture | pages [25] -->
m

<!-- b002989 | furniture | pages [25] -->
m

<!-- b002990 | furniture | pages [25] -->
m

<!-- b002991 | furniture | pages [25] -->
m

<!-- b002992 | furniture | pages [25] -->
m

<!-- b002993 | furniture | pages [25] -->
m

<!-- b002994 | furniture | pages [25] -->
m

<!-- b002995 | furniture | pages [25] -->
m

<!-- b002996 | furniture | pages [25] -->
m

<!-- b002997 | furniture | pages [25] -->
m

<!-- b002998 | furniture | pages [25] -->
m

<!-- b002999 | furniture | pages [25] -->
m

<!-- b003000 | furniture | pages [25] -->
m

<!-- b003001 | furniture | pages [25] -->
m

<!-- b003002 | furniture | pages [25] -->
m

<!-- b003003 | furniture | pages [25] -->
m

<!-- b003004 | furniture | pages [25] -->
m

<!-- b003005 | furniture | pages [25] -->
m

<!-- b003006 | furniture | pages [25] -->
m

<!-- b003007 | furniture | pages [25] -->
m

<!-- b003008 | furniture | pages [25] -->
m

<!-- b003009 | furniture | pages [25] -->
m

<!-- b003010 | furniture | pages [25] -->
m

<!-- b003011 | furniture | pages [25] -->
m

<!-- b003012 | furniture | pages [25] -->
m

<!-- b003013 | furniture | pages [25] -->
m

<!-- b003014 | furniture | pages [25] -->
m

<!-- b003015 | furniture | pages [25] -->
m

<!-- b003016 | furniture | pages [25] -->
m

<!-- b003017 | furniture | pages [25] -->
m

<!-- b003018 | furniture | pages [25] -->
m

<!-- b003019 | furniture | pages [25] -->
m

<!-- b003020 | furniture | pages [25] -->
m

<!-- b003021 | furniture | pages [25] -->
m

<!-- b003022 | furniture | pages [25] -->
m

<!-- b003023 | furniture | pages [25] -->
m

<!-- b003024 | furniture | pages [25] -->
m

<!-- b003025 | furniture | pages [25] -->
m

<!-- b003026 | furniture | pages [25] -->
m

<!-- b003027 | furniture | pages [25] -->
m

<!-- b003028 | furniture | pages [25] -->
m

<!-- b003029 | furniture | pages [25] -->
m

<!-- b003030 | furniture | pages [25] -->
m

<!-- b003031 | furniture | pages [25] -->
m

<!-- b003032 | furniture | pages [25] -->
m

<!-- b003033 | furniture | pages [25] -->
m

<!-- b003034 | furniture | pages [25] -->
m

<!-- b003035 | furniture | pages [25] -->
m

<!-- b003036 | furniture | pages [25] -->
m

<!-- b003037 | furniture | pages [25] -->
m

<!-- b003038 | furniture | pages [25] -->
m

<!-- b003039 | furniture | pages [25] -->
m

<!-- b003040 | furniture | pages [25] -->
m

<!-- b003041 | furniture | pages [25] -->
m

<!-- b003042 | furniture | pages [25] -->
m

<!-- b003043 | furniture | pages [25] -->
m

<!-- b003044 | furniture | pages [25] -->
m

<!-- b003045 | furniture | pages [25] -->
m

<!-- b003046 | furniture | pages [25] -->
m

<!-- b003047 | furniture | pages [25] -->
m

<!-- b003048 | furniture | pages [25] -->
m

<!-- b003049 | furniture | pages [25] -->
m

<!-- b003050 | furniture | pages [25] -->
m

<!-- b003051 | furniture | pages [25] -->
m

<!-- b003052 | furniture | pages [25] -->
m

<!-- b003053 | furniture | pages [25] -->
m

<!-- b003054 | furniture | pages [25] -->
m

<!-- b003055 | furniture | pages [25] -->
m

<!-- b003056 | furniture | pages [25] -->
m

<!-- b003057 | furniture | pages [25] -->
m

<!-- b003058 | furniture | pages [25] -->
m

<!-- b003059 | furniture | pages [25] -->
m

<!-- b003060 | furniture | pages [25] -->
m

<!-- b003061 | furniture | pages [25] -->
m

<!-- b003062 | furniture | pages [25] -->
m

<!-- b003063 | furniture | pages [25] -->
m

<!-- b003064 | furniture | pages [25] -->
m

<!-- b003065 | furniture | pages [25] -->
m

<!-- b003066 | furniture | pages [25] -->
m

<!-- b003067 | furniture | pages [25] -->
m

<!-- b003068 | furniture | pages [25] -->
m

<!-- b003069 | furniture | pages [25] -->
m

<!-- b003070 | furniture | pages [25] -->
m

<!-- b003071 | furniture | pages [25] -->
m

<!-- b003072 | furniture | pages [25] -->
m

<!-- b003073 | furniture | pages [25] -->
m

<!-- b003074 | furniture | pages [25] -->
m

<!-- b003075 | furniture | pages [25] -->
m

<!-- b003076 | furniture | pages [25] -->
m

<!-- b003077 | furniture | pages [25] -->
m

<!-- b003078 | furniture | pages [25] -->
m

<!-- b003079 | furniture | pages [25] -->
m

<!-- b003080 | furniture | pages [25] -->
m

<!-- b003081 | furniture | pages [25] -->
m

<!-- b003082 | furniture | pages [25] -->
m

<!-- b003083 | furniture | pages [25] -->
m

<!-- b003084 | furniture | pages [25] -->
m

<!-- b003085 | furniture | pages [25] -->
m

<!-- b003086 | furniture | pages [25] -->
m

<!-- b003087 | furniture | pages [25] -->
m

<!-- b003088 | furniture | pages [25] -->
m

<!-- b003089 | furniture | pages [25] -->
m

<!-- b003090 | furniture | pages [25] -->
m

<!-- b003091 | furniture | pages [25] -->
m

<!-- b003092 | furniture | pages [25] -->
m

<!-- b003093 | furniture | pages [25] -->
m

<!-- b003094 | furniture | pages [25] -->
m

<!-- b003095 | furniture | pages [25] -->
m

<!-- b003096 | furniture | pages [25] -->
m

<!-- b003097 | furniture | pages [25] -->
m

<!-- b003098 | furniture | pages [25] -->
m

<!-- b003099 | furniture | pages [25] -->
m

<!-- b003100 | furniture | pages [25] -->
m

<!-- b003101 | furniture | pages [25] -->
m

<!-- b003102 | furniture | pages [25] -->
m

<!-- b003103 | furniture | pages [25] -->
m

<!-- b003104 | furniture | pages [25] -->
m

<!-- b003105 | furniture | pages [25] -->
m

<!-- b003106 | furniture | pages [25] -->
m

<!-- b003107 | furniture | pages [25] -->
m

<!-- b003108 | furniture | pages [25] -->
m

<!-- b003109 | furniture | pages [25] -->
m

<!-- b003110 | furniture | pages [25] -->
m

<!-- b003111 | furniture | pages [25] -->
m

<!-- b003112 | furniture | pages [25] -->
m

<!-- b003113 | furniture | pages [25] -->
m

<!-- b003114 | furniture | pages [25] -->
m

<!-- b003115 | furniture | pages [25] -->
m

<!-- b003116 | furniture | pages [25] -->
m

<!-- b003117 | furniture | pages [25] -->
m

<!-- b003118 | furniture | pages [25] -->
m

<!-- b003119 | furniture | pages [25] -->
m

<!-- b003120 | furniture | pages [25] -->
m

<!-- b003121 | furniture | pages [25] -->
m

<!-- b003122 | furniture | pages [25] -->
m

<!-- b003123 | furniture | pages [25] -->
m

<!-- b003124 | furniture | pages [25] -->
m

<!-- b003125 | furniture | pages [25] -->
m

<!-- b003126 | furniture | pages [25] -->
m

<!-- b003127 | furniture | pages [25] -->
m

<!-- b003128 | furniture | pages [25] -->
m

<!-- b003129 | furniture | pages [25] -->
m

<!-- b003130 | furniture | pages [25] -->
m

<!-- b003131 | furniture | pages [25] -->
m

<!-- b003132 | furniture | pages [25] -->
m

<!-- b003133 | furniture | pages [25] -->
m

<!-- b003134 | furniture | pages [25] -->
m

<!-- b003135 | furniture | pages [25] -->
m

<!-- b003136 | furniture | pages [25] -->
m

<!-- b003137 | furniture | pages [25] -->
m

<!-- b003138 | furniture | pages [25] -->
m

<!-- b003139 | furniture | pages [25] -->
m

<!-- b003140 | furniture | pages [25] -->
m

<!-- b003141 | furniture | pages [25] -->
m

<!-- b003142 | furniture | pages [25] -->
m

<!-- b003143 | furniture | pages [25] -->
m

<!-- b003144 | furniture | pages [25] -->
m

<!-- b003145 | furniture | pages [25] -->
m

<!-- b003146 | furniture | pages [25] -->
m

<!-- b003147 | furniture | pages [25] -->
m

<!-- b003148 | furniture | pages [25] -->
m

<!-- b003149 | furniture | pages [25] -->
m

<!-- b003150 | furniture | pages [25] -->
m

<!-- b003151 | furniture | pages [25] -->
m

<!-- b003152 | furniture | pages [25] -->
m

<!-- b003153 | furniture | pages [25] -->
m

<!-- b003154 | furniture | pages [25] -->
m

<!-- b003155 | furniture | pages [25] -->
m

<!-- b003156 | furniture | pages [25] -->
m

<!-- b003157 | furniture | pages [25] -->
m

<!-- b003158 | furniture | pages [25] -->
m

<!-- b003159 | furniture | pages [25] -->
m

<!-- b003160 | furniture | pages [25] -->
m

<!-- b003161 | furniture | pages [25] -->
m

<!-- b003162 | furniture | pages [25] -->
m

<!-- b003163 | furniture | pages [25] -->
m

<!-- b003164 | furniture | pages [25] -->
m

<!-- b003165 | furniture | pages [25] -->
m

<!-- b003166 | furniture | pages [25] -->
m

<!-- b003167 | furniture | pages [25] -->
m

<!-- b003168 | furniture | pages [25] -->
m

<!-- b003169 | furniture | pages [25] -->
m

<!-- b003170 | furniture | pages [25] -->
m

<!-- b003171 | furniture | pages [25] -->
m

<!-- b003172 | furniture | pages [25] -->
m

<!-- b003173 | furniture | pages [25] -->
m

<!-- b003174 | furniture | pages [25] -->
m

<!-- b003175 | furniture | pages [25] -->
m

<!-- b003176 | furniture | pages [25] -->
m

<!-- b003177 | furniture | pages [25] -->
m

<!-- b003178 | furniture | pages [25] -->
m

<!-- b003179 | furniture | pages [25] -->
m

<!-- b003180 | furniture | pages [25] -->
m

<!-- b003181 | furniture | pages [25] -->
m

<!-- b003182 | furniture | pages [25] -->
m

<!-- b003183 | furniture | pages [25] -->
m

<!-- b003184 | furniture | pages [25] -->
m

<!-- b003185 | furniture | pages [25] -->
m

<!-- b003186 | furniture | pages [25] -->
m

<!-- b003187 | furniture | pages [25] -->
m

<!-- b003188 | furniture | pages [25] -->
m

<!-- b003189 | furniture | pages [25] -->
m

<!-- b003190 | furniture | pages [25] -->
m

<!-- b003191 | furniture | pages [25] -->
m

<!-- b003192 | furniture | pages [25] -->
m

<!-- b003193 | furniture | pages [25] -->
m

<!-- b003194 | furniture | pages [25] -->
m

<!-- b003195 | furniture | pages [25] -->
m

<!-- b003196 | furniture | pages [25] -->
m

<!-- b003197 | furniture | pages [25] -->
m

<!-- b003198 | furniture | pages [25] -->
m

<!-- b003199 | furniture | pages [25] -->
m

<!-- b003200 | furniture | pages [25] -->
m

<!-- b003201 | furniture | pages [25] -->
m

<!-- b003202 | furniture | pages [25] -->
m

<!-- b003203 | furniture | pages [25] -->
m

<!-- b003204 | furniture | pages [25] -->
m

<!-- b003205 | furniture | pages [25] -->
m

<!-- b003206 | furniture | pages [25] -->
m

<!-- b003207 | furniture | pages [25] -->
m

<!-- b003208 | furniture | pages [25] -->
m

<!-- b003209 | furniture | pages [25] -->
m

<!-- b003210 | furniture | pages [25] -->
m

<!-- b003211 | furniture | pages [25] -->
m

<!-- b003212 | furniture | pages [25] -->
m

<!-- b003213 | furniture | pages [25] -->
m

<!-- b003214 | furniture | pages [25] -->
m

<!-- b003215 | furniture | pages [25] -->
m

<!-- b003216 | furniture | pages [25] -->
m

<!-- b003217 | furniture | pages [25] -->
m

<!-- b003218 | furniture | pages [25] -->
m

<!-- b003219 | furniture | pages [25] -->
m

<!-- b003220 | furniture | pages [25] -->
m

<!-- b003221 | furniture | pages [25] -->
m

<!-- b003222 | furniture | pages [25] -->
m

<!-- b003223 | furniture | pages [25] -->
m

<!-- b003224 | furniture | pages [25] -->
m

<!-- b003225 | furniture | pages [25] -->
m

<!-- b003226 | furniture | pages [25] -->
m

<!-- b003227 | furniture | pages [25] -->
m

<!-- b003228 | furniture | pages [25] -->
m

<!-- b003229 | furniture | pages [25] -->
m

<!-- b003230 | furniture | pages [25] -->
m

<!-- b003231 | furniture | pages [25] -->
m

<!-- b003232 | furniture | pages [25] -->
m

<!-- b003233 | furniture | pages [25] -->
m

<!-- b003234 | furniture | pages [25] -->
m

<!-- b003235 | furniture | pages [25] -->
m

<!-- b003236 | furniture | pages [25] -->
m

<!-- b003237 | furniture | pages [25] -->
m

<!-- b003238 | furniture | pages [25] -->
m

<!-- b003239 | furniture | pages [25] -->
m

<!-- b003240 | furniture | pages [25] -->
m

<!-- b003241 | furniture | pages [25] -->
m

<!-- b003242 | furniture | pages [25] -->
m

<!-- b003243 | furniture | pages [25] -->
m

<!-- b003244 | furniture | pages [25] -->
m

<!-- b003245 | furniture | pages [25] -->
m

<!-- b003246 | furniture | pages [25] -->
m

<!-- b003247 | furniture | pages [25] -->
m

<!-- b003248 | furniture | pages [25] -->
m

<!-- b003249 | furniture | pages [25] -->
m

<!-- b003250 | furniture | pages [25] -->
m

<!-- b003251 | furniture | pages [25] -->
m

<!-- b003252 | furniture | pages [25] -->
m

<!-- b003253 | furniture | pages [25] -->
m

<!-- b003254 | furniture | pages [25] -->
m

<!-- b003255 | furniture | pages [25] -->
m

<!-- b003256 | furniture | pages [25] -->
m

<!-- b003257 | furniture | pages [25] -->
m

<!-- b003258 | furniture | pages [25] -->
m

<!-- b003259 | furniture | pages [25] -->
m

<!-- b003260 | furniture | pages [25] -->
m

<!-- b003261 | furniture | pages [25] -->
m

<!-- b003262 | furniture | pages [25] -->
m

<!-- b003263 | furniture | pages [25] -->
m

<!-- b003264 | furniture | pages [25] -->
m

<!-- b003265 | furniture | pages [25] -->
m

<!-- b003266 | furniture | pages [25] -->
m

<!-- b003267 | furniture | pages [25] -->
m

<!-- b003268 | furniture | pages [25] -->
m

<!-- b003269 | furniture | pages [25] -->
m

<!-- b003270 | furniture | pages [25] -->
m

<!-- b003271 | furniture | pages [25] -->
m

<!-- b003272 | furniture | pages [25] -->
m

<!-- b003273 | furniture | pages [25] -->
m

<!-- b003274 | furniture | pages [25] -->
m

<!-- b003275 | furniture | pages [25] -->
m

<!-- b003276 | furniture | pages [25] -->
m

<!-- b003277 | furniture | pages [25] -->
m

<!-- b003278 | furniture | pages [25] -->
m

<!-- b003279 | furniture | pages [25] -->
m

<!-- b003280 | furniture | pages [25] -->
m

<!-- b003281 | furniture | pages [25] -->
m

<!-- b003282 | furniture | pages [25] -->
m

<!-- b003283 | furniture | pages [25] -->
m

<!-- b003284 | furniture | pages [25] -->
m

<!-- b003285 | furniture | pages [25] -->
m

<!-- b003286 | furniture | pages [25] -->
m

<!-- b003287 | furniture | pages [25] -->
m

<!-- b003288 | furniture | pages [25] -->
m

<!-- b003289 | furniture | pages [25] -->
m

<!-- b003290 | furniture | pages [25] -->
m

<!-- b003291 | furniture | pages [25] -->
m

<!-- b003292 | furniture | pages [25] -->
m

<!-- b003293 | furniture | pages [25] -->
m

<!-- b003294 | furniture | pages [25] -->
m

<!-- b003295 | furniture | pages [25] -->
m

<!-- b003296 | furniture | pages [25] -->
m

<!-- b003297 | furniture | pages [25] -->
m

<!-- b003298 | furniture | pages [25] -->
m

<!-- b003299 | furniture | pages [25] -->
m

<!-- b003300 | furniture | pages [25] -->
m

<!-- b003301 | furniture | pages [25] -->
m

<!-- b003302 | furniture | pages [25] -->
m

<!-- b003303 | heading | pages [26] -->
Report on use of AI

<!-- b003304 | ai_disclosure | pages [26] -->
1. OpenAl ChatGPT

<!-- b003305 | ai_disclosure | pages [26] -->
Query1: <Please explain to me in simple terms the meaning of Pareto optimization and the

<!-- b003306 | ai_disclosure | pages [26] -->
scenarios of its use>

<!-- b003307 | ai_disclosure | pages [26] -->
Output: <Pareto optimization means a situation where you can’t improve someone’s situation

<!-- b003308 | ai_disclosure | pages [26] -->
without making someone else worse off. It’s about finding the best outcome where no one

<!-- b003309 | ai_disclosure | pages [26] -->
can benefit without someone else losing out. Example: Imagine sharing a pizza. If you take

<!-- b003310 | ai_disclosure | pages [26] -->
more, your friend gets less. A Pareto optimal split means neither of you can get a better

<!-- b003311 | ai_disclosure | pages [26] -->
deal without the other losing. Scenarios: Economics: Resources are used as efficiently as

<!-- b003312 | ai_disclosure | pages [26] -->
possible. Negotiations: Both parties try to find a deal where both benefit without harming

<!-- b003313 | ai_disclosure | pages [26] -->
the other. Public Policy: Governments aim to improve welfare without negatively impacting

<!-- b003314 | ai_disclosure | pages [26] -->
anyone. It’s about balance and fairness, where no one can be made better off without hurting

<!-- b003315 | ai_disclosure | pages [26] -->
someone else.>

<!-- b003316 | ai_disclosure | pages [26] -->
2. OpenAl chatGPT

<!-- b003317 | ai_disclosure | pages [26] -->
Query1: <I will send you the paragraphs of the paper written in Chinese and ask you to

<!-- b003318 | ai_disclosure | pages [26] -->
translate the content of the paragraphs into English. Requirements: standardized use of

<!-- b003319 | ai_disclosure | pages [26] -->
language, no grammatical errors, no mistakes or omissions.>

<!-- b003320 | ai_disclosure | pages [26] -->
Output: <Got it! Feel free to send me the paragraphs, and I’ll translate them into English

<!-- b003321 | ai_disclosure | pages [26] -->
with accuracy and attention to detail.>

<!-- b003322 | ai_disclosure | pages [26] -->
3. OpenAl ChatGPT

<!-- b003323 | ai_disclosure | pages [26] -->
Query1: <Next I’m going to talk about sending you a piece of Python code and ask you to

<!-- b003324 | ai_disclosure | pages [26] -->
check the code for syntax errors.>

<!-- b003325 | ai_disclosure | pages [26] -->
Output: <Your Python code looks mostly fine, but I did spot a couple of potential issues and

<!-- b003326 | ai_disclosure | pages [26] -->
suggestions: Line 18: You are using np.exp(k1 ∗t) but haven’t defined k1 yet. If this is a typo

<!-- b003327 | ai_disclosure | pages [26] -->
or unintentional, make sure to replace k1 with a value or a properly defined variable. Line

<!-- b003328 | ai_disclosure | pages [26] -->
22: α1 is calculated using np.linspace(0, 1.5, 100), but this will generate an array. When

<!-- b003329 | ai_disclosure | pages [26] -->
you use it in the CCO2 equation, it might cause dimension mismatch. You should check if this

<!-- b003330 | ai_disclosure | pages [26] -->
is intended or modify your approach accordingly. Line 25: In the equation for CCO2, you are

<!-- b003331 | ai_disclosure | pages [26] -->
using α1 on both sides of the equation, which is fine as long as it makes sense for the model.

<!-- b003332 | ai_disclosure | pages [26] -->
Just make sure this is not a mistake. Line 33: For plt.scatter(minEnvN t, minEnvvalue, ...),

<!-- b003333 | ai_disclosure | pages [26] -->
you’re plotting a point without explicitly checking if minEnvvalue is finite or valid. You may

<!-- b003334 | ai_disclosure | pages [26] -->
want to check for NaN or inf before plotting. Font warning: The Times New Roman font

<!-- b003335 | ai_disclosure | pages [26] -->
you’re setting might not always be available in all environments. You could include a fallback

<!-- b003336 | ai_disclosure | pages [26] -->
font like this:>

<!-- b003337 | ai_disclosure | pages [26] -->
4. OpenAl ChatGPT

<!-- b003338 | ai_disclosure | pages [26] -->
Query1: <Could you briefly tell me the format of the Memo?>

<!-- b003339 | ai_disclosure | pages [26] -->
Output: <Certainly! Here’s a brief summary of the memo format: Header Section: To:

<!-- b003340 | ai_disclosure | pages [26] -->
Recipient(s) of the memo. From: The sender’s name or title. Date: The date the memo is

<!-- b003341 | ai_disclosure | pages [26] -->
being sent. Subject: A short, clear statement of the memo’s topic. Body Section: A clear and

<!-- b003342 | ai_disclosure | pages [26] -->
concise explanation of the memo’s purpose. You can break it into numbered or bulleted points

<!-- b003343 | ai_disclosure | pages [26] -->
for clarity, especially if providing instructions, updates, or details. Closing (Optional)>

<!-- b003344 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b003345 | furniture | pages [26] -->
2

<!-- b003346 | furniture | pages [26] -->
MATHmodels

<!-- b003347 | furniture | pages [26] -->
获取更多资讯
