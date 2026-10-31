# P-D-2025-2519935-f07f7c47

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen D 2025 MCM/ICM Summary Sheet Team Control Number 2519935

<!-- b000003 | title | pages [1] -->
Navigating Baltimore’s Growth: A Multi-Layer Network Approach to Urban Transportation Optimization

<!-- b000004 | heading | pages [1] -->
Summary

<!-- b000005 | prose | pages [1] -->
The collapse of the Francis Scott Key Bridge in 2024 cut off a vital route to the port, posing an unprecedented challenge to Baltimore’s transportation system and bringing the optimization of traffic network back into the public view. This paper analyzes the city transportation system based on a multi-layered road network model and proposes several improvement strategies.

<!-- b000006 | prose | pages [1] -->
Before assessing the traffic conditions in Baltimore, we conduct data preprocessing. Firstly, we use uniqueness of osmid to complete 354,420 missing road names. Subsequently, roads with three or more osmid records (9,953 entries) between two nodes are treated as outliers and removed. For roads with two osmids, we follow the "road smoothing" principle to determine their proper names. Finally, we uniform different road names.

<!-- b000007 | prose | pages [1] -->
For task 1, to evaluate the influence of bridge collapse on the urban transport system, we establish an impact assessment model, which analyzes the changes in route choices of commuters and non-commuters based on AADT and AAWDT. Additionally, we construct a subnetwork using critical nodes of the highway network, and compute the proximity centrality of these nodes to reflect their efficiency in network propagation, which can reveal the effect of bridge collapse on the connectivity of surrounding areas. Results indicate that in Baltimore Harbor Tunnel Thurway, the traffic flow of commuters increases by 14%, while non-commuters declines by 25%. The Beltway emerges as a heavily loaded segment for diverse user types.

<!-- b000008 | prose | pages [1] -->
For task 2, we develop a three-layer bus network model to determine the optimal placement of new bus lines. Firstly we use the entropy-weight-TOPSIS method incorporating both infrastructure levels and passenger volume at bus stops, and utilizes the weighted k-shell decomposition method to classify them into core, bridge, and outer layers accordingly. The designed lines aim to enhance inter-layer connectivity and advance the interests of various stakeholders. Statistics demonstrate that the composition of core-bridge edges increases by 18.3% and that of outer layer decreases by 82.9%.

<!-- b000009 | prose | pages [1] -->
For task 3, we raise a project of adding an Orange Line rail transit to meet the growing demand of residents. The line connecting Penn Station, parks, and large markets, facilitates transfers to the airport and offers benefits to various stakeholders. The total travel time from the farthest station, White Marsh, to the airport is compressed to approximately 65 minutes. Lastly, focusing on the influence on bus stops, we construct a double density fitting model. A quadratic function is utilized to depict the relationship between bus stop density and road network density, thus evaluating the contribution of the rail transit. Results showed an increased demand for bus services along the rail line, averaging around 2.31 times.

<!-- b000010 | prose | pages [1] -->
The proposed multi-layer network model exhibited strong robustness and stability, as confirmed through sensitivity analysis, highlighting its considerable practical utility. The approach we suggest, by synthesizing a range of transportation factors, provides a robust framework for informing the design and implementation of transportation improvements in Baltimore City.

<!-- b000011 | keywords | pages [1] -->
Keywords: Multi-layer network model, three-layer bus network model, Baltimore

<!-- b000012 | furniture | pages [1] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000013 | heading | pages [2] -->
Contents

<!-- b000014 | heading | pages [2] -->
Introduction

<!-- b000015 | prose | pages [2] -->
3 1

<!-- b000016 | heading | pages [2] -->
Background

<!-- b000017 | prose | pages [2] -->
1.1 3 1.2

<!-- b000018 | heading | pages [2] -->
Restatement of the Problem

<!-- b000019 | prose | pages [2] -->
3 1.3 Our Work 4

<!-- b000020 | heading | pages [2] -->
Model Assumptions and Notation

<!-- b000021 | prose | pages [2] -->
2 4 4 2.1

<!-- b000022 | heading | pages [2] -->
Assumptions

<!-- b000023 | heading | pages [2] -->
Notation

<!-- b000024 | prose | pages [2] -->
2.2 4 Data Preprocessing 5 3 5 3.1 Imputation of Missing Values 3.2 5 Outlier Removal 6 3.3 Handling Cluttered Road Information 3.4 Processing Abbreviation Information 6 7 Multi-layer Transportation Network Model 4

<!-- b000025 | prose | pages [2] -->
Task 1: Analysis of the Bridge Collapse's Impact 5 8

<!-- b000026 | heading | pages [2] -->
Impact Assessment Model(IA)

<!-- b000027 | prose | pages [2] -->
8 5.1 Model Solution and Results . 10 5.2 10 5.2.1 5.2.2 The Impact in Baltimore 11 Task 2: The impact of the project on the bus system 13 6

<!-- b000028 | heading | pages [2] -->
Three-layer Bus Network Model (TBN)

<!-- b000029 | prose | pages [2] -->
6.1 13

<!-- b000030 | heading | pages [2] -->
Model Solution and Results

<!-- b000031 | prose | pages [2] -->
6.2 15 17 7

<!-- b000032 | heading | pages [2] -->
Improved Dijkstra Algorithm

<!-- b000033 | prose | pages [2] -->
17 7.1 Double Density Fitting Model (DDF) . 7.2 17 Model Solution and Results . . 18 7.3 19 Question a: The Benefits to Residents 7.3.1 Question b: The Impact on Other Stakeholders 19 Question c: Disruption to Other Transportation Needs . 20

<!-- b000034 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000035 | prose | pages [2] -->
22 8

<!-- b000036 | prose | pages [2] -->
22

<!-- b000037 | heading | pages [2] -->
Model Evaluation and Further Discussion

<!-- b000038 | prose | pages [2] -->
9 Strengths . 22 9.1 ● 9.2

<!-- b000039 | heading | pages [2] -->
Weaknesses

<!-- b000040 | prose | pages [2] -->
23

<!-- b000041 | heading | pages [2] -->
Further Discussion

<!-- b000042 | prose | pages [2] -->
23 9.3

<!-- b000043 | heading | pages [2] -->
10 Memorandum

<!-- b000044 | prose | pages [2] -->
24

<!-- b000045 | heading | pages [2] -->
References

<!-- b000046 | references | pages [2] -->
25

<!-- b000047 | references | pages [2] -->
家

<!-- b000048 | references | pages [2] -->
关注数学模型

<!-- b000049 | furniture | pages [2] -->
获取更多资讯

<!-- b000050 | furniture | pages [3] -->
Team # 2519935

<!-- b000051 | furniture | pages [3] -->
Page 3 of 25

<!-- b000052 | heading | pages [3] -->
1 Introduction

<!-- b000053 | heading | pages [3] -->
1.1 Background

<!-- b000054 | prose | pages [3] -->
Baltimore, Maryland faces significant challenges in its aging transportation infrastructure, 微信公众号：数学模型 which affects both residents and businesses. The collapse of the Francis Scott Key Bridge has disrupted major routes across the harbor, causing delays for commuters, freight, and local traffic[1]. With a bustling port and proximity to key highways, the city is critical for both regional and national commerce. However, the city’s infrastructure has long been a barrier to efficient movement, especially with highways and rail systems that divide neighborhoods and hinder access to jobs, schools, and local businesses.

<!-- b000055 | prose | pages [3] -->
In response, Baltimore aims to improve its transportation network as part of a broader sustainability initiative. This involves enhancing public transit, such as rail and bus systems, and repairing or upgrading key infrastructure. The city seeks to address both the practical challenges of transportation—such as congestion, poor transit coverage, and access to major 微信号：MATHmodels commercial centers—and broader community goals, like reducing environmental impact and improving safety. These efforts also include rethinking how highways and rail systems can be redesigned to reconnect neighborhoods and improve residents’ quality of life.

<!-- b000056 | caption | pages [3] -->
Figure 1: The Collapse of Francis Scott Key Bridge

<!-- b000057 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000058 | prose | pages [3] -->
In order to solve those problems, we will proceed as follows:

<!-- b000059 | prose | pages [3] -->
• Firstly, develop a network model of the city’s transportation system to assess traffic flow and the impact of the Francis Scott Key Bridge collapse.

<!-- b000060 | prose | pages [3] -->
• Secondly, analyze key transportation issues, including public transit limitations and pedestrian infrastructure, to identify potential improvements.

<!-- b000061 | prose | pages [3] -->
• Furthermore, evaluate stakeholder impacts, considering the needs of commuters, resi- dents, and businesses.

<!-- b000062 | prose | pages [3] -->
• Finally, recommend a project that best improves the city’s transportation, balancing benefits, disruptions, and safety. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

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
Team # 2519935

<!-- b000388 | furniture | pages [4] -->
Page 4 of 25

<!-- b000389 | heading | pages [4] -->
1.3 Our Work

<!-- b000390 | caption | pages [4] -->
Figure 2: The Framwork

<!-- b000391 | heading | pages [4] -->
2 Model Assumptions and Notation

<!-- b000392 | heading | pages [4] -->
2.1 Assumptions

<!-- b000393 | prose | pages [4] -->
To build up our model, we make the following model assumptions.

<!-- b000394 | prose | pages [4] -->
• All vehicles within a transportation network operate at the maximum speed limit, with varying speeds across different network layers.

<!-- b000395 | prose | pages [4] -->
• Commuters travel only on weekdays, while the numbers of non-commuters on weekends and weekdays is identical.

<!-- b000396 | prose | pages [4] -->
• Any two nodes in the graph are connected by a path.

<!-- b000397 | heading | pages [4] -->
2.2 Notation

<!-- b000398 | caption | pages [4] -->
Table 1: Notations

<!-- b000399 | prose | pages [4] -->
Symbols Description

<!-- b000400 | prose | pages [4] -->
L(u, v) Hierarchical layer of the arc between nodes u and v t(u, v) Travel time on the segment between nodes u and v ks Weighted degree representing the importance of a node

<!-- b000401 | prose | pages [4] -->
关注数学模型

<!-- b000402 | furniture | pages [4] -->
2

<!-- b000403 | furniture | pages [4] -->
MATHmodels

<!-- b000404 | furniture | pages [4] -->
获取更多资讯

<!-- b000405 | furniture | pages [5] -->
Team # 2519935

<!-- b000406 | furniture | pages [5] -->
Page 5 of 25

<!-- b000407 | heading | pages [5] -->
3 Data Preprocessing

<!-- b000408 | prose | pages [5] -->
The "edges_all" and "AADT" files play a crucial role in understanding the distribution of city roads in Baltimore and subsequent analyses. Upon examining the datasets, it became 微信公众号：数学模型 evident that they contained significant noise, necessitating a thorough preprocessing process. The data preprocessing workflow is illustrated in Figure 3.

<!-- b000409 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000410 | caption | pages [5] -->
Figure 3: Data Preprocessing Process

<!-- b000411 | heading | pages [5] -->
3.1 Imputation of Missing Values

<!-- b000412 | prose | pages [5] -->
In the "edges_all" file, the "name" column is found to contain missing values. Preliminary analysis indicated a one-to-one correspondence between the "osmid" and the road name, allow- ing the missing values in the "name" column to be imputed based on the corresponding "osmid" values. Table 2 provides a sample of osmids and their corresponding road names.

<!-- b000413 | caption | pages [5] -->
Table 2: Road Names Corresponding to Osmids

<!-- b000414 | prose | pages [5] -->
osmid road_name osmid road_name osmid road_name 5250723 Wells Avenue 355848252 Kelly Way 5289021 Bengies Road 5308620 Maxwell Avenue 435579752 Rushley Road 5320737 Loveton Circle

<!-- b000415 | prose | pages [5] -->
Using the above correspondence, a total of 354,420 missing values in the "name" column are imputed. Other columns, such as "lanes," which has a large number of missing values, are excluded from further analysis, as they do not significantly impact the problem under investigation.

<!-- b000416 | heading | pages [5] -->
3.2 Outlier Removal

<!-- b000417 | prose | pages [5] -->
As previously noted, each "osmid" corresponds to a unique road. Therefore, any occurrence of three or more "osmids" between two nodes, indicating the presence of multiple roads, is considered an outlier and removed. Table 3 presents examples of outliers identified in the "osmid" column.Ultimately, 9,953 outliers are removed from the dataset.

<!-- b000418 | caption | pages [5] -->
Table 3: Example of Outliers

<!-- b000419 | prose | pages [5] -->
u v osmid 89606346 1930984898 [425106099, 425106102, 974337038] 96250866 968161510 [10832171, 10832167, 61424703] 96250866 37412403 [425007969, 425007970, 10832168, 83204409, 83204413]

<!-- b000420 | furniture | pages [6] -->
Team # 2519935

<!-- b000421 | furniture | pages [6] -->
Page 6 of 25

<!-- b000422 | heading | pages [6] -->
3.3 Handling Cluttered Road Information

<!-- b000423 | prose | pages [6] -->
In the "edges_all" file, there are cases where two roads exist for some edges. Since the provided information does not specify the boundary between the two roads, and to facilitate subsequent processing, this section defines such cases as a single road. First, the nodes A and B with this condition are identified. The slope k3 between these two nodes is then calculated. Assuming that the edge contains two roads, R1 and R2, a node A1, directly connected to node A and exclusive to road R1, is identified, and its slope k1 is computed. Similarly, for node B, a point exclusive to road R2 that is directly connected to node B is found, and its slope k2 is calculated. The following relationship is then evaluated:

<!-- b000424 | prose | pages [6] -->
|k3 −k1| < |k3 −k2| . (1)

<!-- b000425 | prose | pages [6] -->
If this condition holds, the edge is considered to belong to road R1; otherwise, it is assigned to road R2. A concrete example is illustrated in Figure 4.

<!-- b000426 | caption | pages [6] -->
Figure 4: Handling Cluttered Road Information

<!-- b000427 | prose | pages [6] -->
As shown in the figure above, after calculating the three slopes, the original road is identified as Ross Avenue. This method ensures that sharp turns are minimized within a single road.

<!-- b000428 | heading | pages [6] -->
3.4 Processing Abbreviation Information

<!-- b000429 | prose | pages [6] -->
During the analysis of the "AADT" file, it is observed that the "Road Name" column contains abbreviations that do not match the previously used road names. Upon further investigation, it is found that the road names are abbreviated. To standardize the road names for subsequent analyses, this section converts all abbreviations to their full forms. Table 4 provides a list of common abbreviations and their corresponding full names.

<!-- b000430 | caption | pages [6] -->
Table 4: Abbreviations and Full Names

<!-- b000431 | prose | pages [6] -->
Abbreviation Full Name Abbreviation Full Name Abbreviation Full Name ST STREET AVE AVENUE RD ROAD DR DRIVE TERR TERRACE BLVD BOULEVARD

<!-- b000432 | prose | pages [6] -->
关注数学模型

<!-- b000433 | furniture | pages [6] -->
2

<!-- b000434 | furniture | pages [6] -->
MATHmodels

<!-- b000435 | furniture | pages [6] -->
获取更多资讯

<!-- b000436 | furniture | pages [7] -->
Team # 2519935

<!-- b000437 | furniture | pages [7] -->
Page 7 of 25

<!-- b000438 | heading | pages [7] -->
4 Multi-layer Transportation Network Model

<!-- b000439 | prose | pages [7] -->
Baltimore can be abstracted as a multi-layer Arc-Node grid model, which represents the transportation network with a topological structure [2]. The core concept of the Arc-Node model is to approximate real-world road curves with a series of straight line segments [3]. The entire transportation network consists of nodes and arcs, represented as a graph G = (N, A), where N denotes the set of nodes and A represents the arcs. This is formally defined as:

<!-- b000440 | prose | pages [7] -->
 G = (N, A)   N = {(x, y) | (x, y) ∈Ns} . (2)  A = {(u, v) | u, v ∈N}  微信公众号：数学模型 Here, N represents the set of nodes with coordinates (x, y) in the road network, and A denotes the set of arcs representing road segments between nodes u and v.

<!-- b000441 | prose | pages [7] -->
Based on the specific characteristics of the city, Baltimore’s road network can be categorized into different types, such as motorways, residential roads, and primary roads. Consequently, the transportation network can be abstracted into a multi-layer structure. Each layer Li corresponds to a subgraph Gi of the graph G. The layers are independent of one another, ensuring the topo- logical connectivity of the network and enabling hierarchical management of the transportation system. This can be represented as:

<!-- b000442 | prose | pages [7] -->
微信号：MATHmodels  G = G1 ∪G1 ∪G2 ∪· · · ∪Gk   N(Gi) ∈N(G), ∀i ∈k , (3)  A(Gi) ∈A(G), ∀i ∈k  where N(G) and A(G) denote the sets of nodes and arcs in the graph G, respectively.

<!-- b000443 | prose | pages [7] -->
A diagram of the multi-layer road network model is shown below:

<!-- b000444 | caption | pages [7] -->
Figure 5: Layered Road Network Diagram

<!-- b000445 | prose | pages [7] -->
For each arc, various attributes are constructed to provide a comprehensive description of the city’s transportation network system:

<!-- b000446 | prose | pages [7, 8] -->
• d(u, v) represents the shortest path length between nodes u and v. In multi-layer path planning, it is necessary to compute the shortest path by transferring input nodes to higher-layer networks. If node u starts at a lower layer, its shortest path to the higher-layer network must be searched within a local area [4]. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • L(u, v) indicates the hierarchy of the arc between nodes u and v, used to differentiate between main roads and secondary roads. Typically, higher-layer roads allow faster traffic flow.

<!-- b000447 | furniture | pages [7] -->
m

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

<!-- b000771 | furniture | pages [8] -->
Team # 2519935

<!-- b000772 | furniture | pages [8] -->
Page 8 of 25

<!-- b000774 | prose | pages [8] -->
• t(u, v) represents the travel time from node u to node v, calculated as the path length divided by the speed allowed on that layer:

<!-- b000775 | prose | pages [8] -->
d(u, v) t(u, v) = v(L(u, v)). (4)

<!-- b000776 | prose | pages [8] -->
• q(u, v) denotes the traffic flow on the road segment between nodes u and v. In traffic flow models, the flow must be conserved along the same path, i.e.,

<!-- b000777 | prose | pages [8] -->
X X q(v, u), ∀u, v ∈N. q(u, v) = (5) u∈N v∈N

<!-- b000778 | heading | pages [8] -->
5 Task 1: Analysis of the Bridge Collapse’s Impact

<!-- b000779 | heading | pages [8] -->
5.1 Impact Assessment Model(IA)

<!-- b000780 | prose | pages [8] -->
• The Impact in Baltimore

<!-- b000781 | prose | pages [8] -->
In order to assess the impact of the bridge collapse on stakeholders in Baltimore, we select AADT (Annual Average Daily Traffic) and AAWDT (Annual Average Weekday Traffic) as the evaluation indicators, which effectively describe the traffic conditions in Baltimore. Based on the changes in these two indicators before and after the bridge collapse, we can analyze the impact of the collapse of the Francis Scott Key Bridge.

<!-- b000782 | prose | pages [8] -->
As one of the oldest towns in the United States, Baltimore’s economy is steadily growing [5]. It is observed that the AADT and AAWDT data for most roads remained relatively stable Therefore, to estimate the AADT and AAWDT on road i at the between 2014 and 2022. beginning of 2024, with the bridge still in place, we calculate the historical averages:

<!-- b000783 | prose | pages [8] -->
 2022 AADTi,2024 = 1 X  AADTi,y   9    y=2014 . (6) 2022 AAWDTi,2024 = 1  X  AAWDTi,y   9   y=2014

<!-- b000784 | prose | pages [8] -->
Here, we categorize the stakeholders into commuters and non-commuters [6]. The average number of commuters passing through road i in year y is denoted by Ji,y, and the number of non-commuters is denoted by Ki,y. The AADT and AAWDT for road i in year y can then be expressed as:

<!-- b000785 | prose | pages [8] -->
AADTi,y = 5 · Ji,y + 7 · Ki,y    7 . (7) AAWDTi,y = 5 · Ji,y + 5 · Ki,y   5

<!-- b000786 | prose | pages [8, 9] -->
关注数学模型 After simplification the above equations yields the following formulas for commuters and non-commuters:

<!-- b000787 | furniture | pages [8] -->
2

<!-- b000788 | furniture | pages [8] -->
MATHmodels

<!-- b000789 | furniture | pages [8] -->
获取更多资讯

<!-- b000790 | furniture | pages [9] -->
Team # 2519935

<!-- b000791 | furniture | pages [9] -->
Page 9 of 25

<!-- b000793 | prose | pages [9] -->
Ji,y = 1  2 × (7 · AADTi,y −5 · AAWDTi,y)   微信公众号：数学模型 . (8) Ki,y = 7 2 × (AAWDTi,y −AADTi,y)  

<!-- b000794 | prose | pages [9] -->
Let the impact coefficient for road i be denoted by βi. For each road, we can analyze the impact of the bridge collapse on commuters and non-commuters. The calculation of the impact coefficient is shown in the figure below.

<!-- b000795 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000796 | caption | pages [9] -->
Figure 6: Calculation of Influence Coefficient

<!-- b000797 | prose | pages [9] -->
The analysis shows that if the impact coefficient βi is greater than 1, the traffic volume on this road segment increases after the bridge collapse. If βi is less than 1, the traffic volume decreases.

<!-- b000798 | prose | pages [9] -->
• The Impact around Baltimore

<!-- b000799 | prose | pages [9] -->
To assess the impact of the bridge collapse on cities surrounding Baltimore, we refer to [7], which indicates that the primary sources of impact come from the highways connecting Baltimore to surrounding cities and the highways crossing Baltimore. Based on this reference, we select 39 representative nodes in Baltimore for analysis, as shown in the diagram below.

<!-- b000800 | caption | pages [9] -->
Figure 7: Selection of Highway Nodes

<!-- b000801 | prose | pages [9, 10] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m During the node abstraction process, if node 37 is connected to node 39, this represents the situation before the bridge collapse (denoted as Graph G2); if the connection is broken, it represents the situation after the bridge collapse (denoted as Graph G).

<!-- b000802 | furniture | pages [9] -->
m

<!-- b000803 | furniture | pages [9] -->
m

<!-- b000804 | furniture | pages [9] -->
m

<!-- b000805 | furniture | pages [9] -->
m

<!-- b000806 | furniture | pages [9] -->
m

<!-- b000807 | furniture | pages [9] -->
m

<!-- b000808 | furniture | pages [9] -->
m

<!-- b000809 | furniture | pages [9] -->
m

<!-- b000810 | furniture | pages [9] -->
m

<!-- b000811 | furniture | pages [9] -->
m

<!-- b000812 | furniture | pages [9] -->
m

<!-- b000813 | furniture | pages [9] -->
m

<!-- b000814 | furniture | pages [9] -->
m

<!-- b000815 | furniture | pages [9] -->
m

<!-- b000816 | furniture | pages [9] -->
m

<!-- b000817 | furniture | pages [9] -->
m

<!-- b000818 | furniture | pages [9] -->
m

<!-- b000819 | furniture | pages [9] -->
m

<!-- b000820 | furniture | pages [9] -->
m

<!-- b000821 | furniture | pages [9] -->
m

<!-- b000822 | furniture | pages [9] -->
m

<!-- b000823 | furniture | pages [9] -->
m

<!-- b000824 | furniture | pages [9] -->
m

<!-- b000825 | furniture | pages [9] -->
m

<!-- b000826 | furniture | pages [9] -->
m

<!-- b000827 | furniture | pages [9] -->
m

<!-- b000828 | furniture | pages [9] -->
m

<!-- b000829 | furniture | pages [9] -->
m

<!-- b000830 | furniture | pages [9] -->
m

<!-- b000831 | furniture | pages [9] -->
m

<!-- b000832 | furniture | pages [9] -->
m

<!-- b000833 | furniture | pages [9] -->
m

<!-- b000834 | furniture | pages [9] -->
m

<!-- b000835 | furniture | pages [9] -->
m

<!-- b000836 | furniture | pages [9] -->
m

<!-- b000837 | furniture | pages [9] -->
m

<!-- b000838 | furniture | pages [9] -->
m

<!-- b000839 | furniture | pages [9] -->
m

<!-- b000840 | furniture | pages [9] -->
m

<!-- b000841 | furniture | pages [9] -->
m

<!-- b000842 | furniture | pages [9] -->
m

<!-- b000843 | furniture | pages [9] -->
m

<!-- b000844 | furniture | pages [9] -->
m

<!-- b000845 | furniture | pages [9] -->
m

<!-- b000846 | furniture | pages [9] -->
m

<!-- b000847 | furniture | pages [9] -->
m

<!-- b000848 | furniture | pages [9] -->
m

<!-- b000849 | furniture | pages [9] -->
m

<!-- b000850 | furniture | pages [9] -->
m

<!-- b000851 | furniture | pages [9] -->
m

<!-- b000852 | furniture | pages [9] -->
m

<!-- b000853 | furniture | pages [9] -->
m

<!-- b000854 | furniture | pages [9] -->
m

<!-- b000855 | furniture | pages [9] -->
m

<!-- b000856 | furniture | pages [9] -->
m

<!-- b000857 | furniture | pages [9] -->
m

<!-- b000858 | furniture | pages [9] -->
m

<!-- b000859 | furniture | pages [9] -->
m

<!-- b000860 | furniture | pages [9] -->
m

<!-- b000861 | furniture | pages [9] -->
m

<!-- b000862 | furniture | pages [9] -->
m

<!-- b000863 | furniture | pages [9] -->
m

<!-- b000864 | furniture | pages [9] -->
m

<!-- b000865 | furniture | pages [9] -->
m

<!-- b000866 | furniture | pages [9] -->
m

<!-- b000867 | furniture | pages [9] -->
m

<!-- b000868 | furniture | pages [9] -->
m

<!-- b000869 | furniture | pages [9] -->
m

<!-- b000870 | furniture | pages [9] -->
m

<!-- b000871 | furniture | pages [9] -->
m

<!-- b000872 | furniture | pages [9] -->
m

<!-- b000873 | furniture | pages [9] -->
m

<!-- b000874 | furniture | pages [9] -->
m

<!-- b000875 | furniture | pages [9] -->
m

<!-- b000876 | furniture | pages [9] -->
m

<!-- b000877 | furniture | pages [9] -->
m

<!-- b000878 | furniture | pages [9] -->
m

<!-- b000879 | furniture | pages [9] -->
m

<!-- b000880 | furniture | pages [9] -->
m

<!-- b000881 | furniture | pages [9] -->
m

<!-- b000882 | furniture | pages [9] -->
m

<!-- b000883 | furniture | pages [9] -->
m

<!-- b000884 | furniture | pages [9] -->
m

<!-- b000885 | furniture | pages [9] -->
m

<!-- b000886 | furniture | pages [9] -->
m

<!-- b000887 | furniture | pages [9] -->
m

<!-- b000888 | furniture | pages [9] -->
m

<!-- b000889 | furniture | pages [9] -->
m

<!-- b000890 | furniture | pages [9] -->
m

<!-- b000891 | furniture | pages [9] -->
m

<!-- b000892 | furniture | pages [9] -->
m

<!-- b000893 | furniture | pages [9] -->
m

<!-- b000894 | furniture | pages [9] -->
m

<!-- b000895 | furniture | pages [9] -->
m

<!-- b000896 | furniture | pages [9] -->
m

<!-- b000897 | furniture | pages [9] -->
m

<!-- b000898 | furniture | pages [9] -->
m

<!-- b000899 | furniture | pages [9] -->
m

<!-- b000900 | furniture | pages [9] -->
m

<!-- b000901 | furniture | pages [9] -->
m

<!-- b000902 | furniture | pages [9] -->
m

<!-- b000903 | furniture | pages [9] -->
m

<!-- b000904 | furniture | pages [9] -->
m

<!-- b000905 | furniture | pages [9] -->
m

<!-- b000906 | furniture | pages [9] -->
m

<!-- b000907 | furniture | pages [9] -->
m

<!-- b000908 | furniture | pages [9] -->
m

<!-- b000909 | furniture | pages [9] -->
m

<!-- b000910 | furniture | pages [9] -->
m

<!-- b000911 | furniture | pages [9] -->
m

<!-- b000912 | furniture | pages [9] -->
m

<!-- b000913 | furniture | pages [9] -->
m

<!-- b000914 | furniture | pages [9] -->
m

<!-- b000915 | furniture | pages [9] -->
m

<!-- b000916 | furniture | pages [9] -->
m

<!-- b000917 | furniture | pages [9] -->
m

<!-- b000918 | furniture | pages [9] -->
m

<!-- b000919 | furniture | pages [9] -->
m

<!-- b000920 | furniture | pages [9] -->
m

<!-- b000921 | furniture | pages [9] -->
m

<!-- b000922 | furniture | pages [9] -->
m

<!-- b000923 | furniture | pages [9] -->
m

<!-- b000924 | furniture | pages [9] -->
m

<!-- b000925 | furniture | pages [9] -->
m

<!-- b000926 | furniture | pages [9] -->
m

<!-- b000927 | furniture | pages [9] -->
m

<!-- b000928 | furniture | pages [9] -->
m

<!-- b000929 | furniture | pages [9] -->
m

<!-- b000930 | furniture | pages [9] -->
m

<!-- b000931 | furniture | pages [9] -->
m

<!-- b000932 | furniture | pages [9] -->
m

<!-- b000933 | furniture | pages [9] -->
m

<!-- b000934 | furniture | pages [9] -->
m

<!-- b000935 | furniture | pages [9] -->
m

<!-- b000936 | furniture | pages [9] -->
m

<!-- b000937 | furniture | pages [9] -->
m

<!-- b000938 | furniture | pages [9] -->
m

<!-- b000939 | furniture | pages [9] -->
m

<!-- b000940 | furniture | pages [9] -->
m

<!-- b000941 | furniture | pages [9] -->
m

<!-- b000942 | furniture | pages [9] -->
m

<!-- b000943 | furniture | pages [9] -->
m

<!-- b000944 | furniture | pages [9] -->
m

<!-- b000945 | furniture | pages [9] -->
m

<!-- b000946 | furniture | pages [9] -->
m

<!-- b000947 | furniture | pages [9] -->
m

<!-- b000948 | furniture | pages [9] -->
m

<!-- b000949 | furniture | pages [9] -->
m

<!-- b000950 | furniture | pages [9] -->
m

<!-- b000951 | furniture | pages [9] -->
m

<!-- b000952 | furniture | pages [9] -->
m

<!-- b000953 | furniture | pages [9] -->
m

<!-- b000954 | furniture | pages [9] -->
m

<!-- b000955 | furniture | pages [9] -->
m

<!-- b000956 | furniture | pages [9] -->
m

<!-- b000957 | furniture | pages [9] -->
m

<!-- b000958 | furniture | pages [9] -->
m

<!-- b000959 | furniture | pages [9] -->
m

<!-- b000960 | furniture | pages [9] -->
m

<!-- b000961 | furniture | pages [9] -->
m

<!-- b000962 | furniture | pages [9] -->
m

<!-- b000963 | furniture | pages [9] -->
m

<!-- b000964 | furniture | pages [9] -->
m

<!-- b000965 | furniture | pages [9] -->
m

<!-- b000966 | furniture | pages [9] -->
m

<!-- b000967 | furniture | pages [9] -->
m

<!-- b000968 | furniture | pages [9] -->
m

<!-- b000969 | furniture | pages [9] -->
m

<!-- b000970 | furniture | pages [9] -->
m

<!-- b000971 | furniture | pages [9] -->
m

<!-- b000972 | furniture | pages [9] -->
m

<!-- b000973 | furniture | pages [9] -->
m

<!-- b000974 | furniture | pages [9] -->
m

<!-- b000975 | furniture | pages [9] -->
m

<!-- b000976 | furniture | pages [9] -->
m

<!-- b000977 | furniture | pages [9] -->
m

<!-- b000978 | furniture | pages [9] -->
m

<!-- b000979 | furniture | pages [9] -->
m

<!-- b000980 | furniture | pages [9] -->
m

<!-- b000981 | furniture | pages [9] -->
m

<!-- b000982 | furniture | pages [9] -->
m

<!-- b000983 | furniture | pages [9] -->
m

<!-- b000984 | furniture | pages [9] -->
m

<!-- b000985 | furniture | pages [9] -->
m

<!-- b000986 | furniture | pages [9] -->
m

<!-- b000987 | furniture | pages [9] -->
m

<!-- b000988 | furniture | pages [9] -->
m

<!-- b000989 | furniture | pages [9] -->
m

<!-- b000990 | furniture | pages [9] -->
m

<!-- b000991 | furniture | pages [9] -->
m

<!-- b000992 | furniture | pages [9] -->
m

<!-- b000993 | furniture | pages [9] -->
m

<!-- b000994 | furniture | pages [9] -->
m

<!-- b000995 | furniture | pages [9] -->
m

<!-- b000996 | furniture | pages [9] -->
m

<!-- b000997 | furniture | pages [9] -->
m

<!-- b000998 | furniture | pages [9] -->
m

<!-- b000999 | furniture | pages [9] -->
m

<!-- b001000 | furniture | pages [9] -->
m

<!-- b001001 | furniture | pages [9] -->
m

<!-- b001002 | furniture | pages [9] -->
m

<!-- b001003 | furniture | pages [9] -->
m

<!-- b001004 | furniture | pages [9] -->
m

<!-- b001005 | furniture | pages [9] -->
m

<!-- b001006 | furniture | pages [9] -->
m

<!-- b001007 | furniture | pages [9] -->
m

<!-- b001008 | furniture | pages [9] -->
m

<!-- b001009 | furniture | pages [9] -->
m

<!-- b001010 | furniture | pages [9] -->
m

<!-- b001011 | furniture | pages [9] -->
m

<!-- b001012 | furniture | pages [9] -->
m

<!-- b001013 | furniture | pages [9] -->
m

<!-- b001014 | furniture | pages [9] -->
m

<!-- b001015 | furniture | pages [9] -->
m

<!-- b001016 | furniture | pages [9] -->
m

<!-- b001017 | furniture | pages [9] -->
m

<!-- b001018 | furniture | pages [9] -->
m

<!-- b001019 | furniture | pages [9] -->
m

<!-- b001020 | furniture | pages [9] -->
m

<!-- b001021 | furniture | pages [9] -->
m

<!-- b001022 | furniture | pages [9] -->
m

<!-- b001023 | furniture | pages [9] -->
m

<!-- b001024 | furniture | pages [9] -->
m

<!-- b001025 | furniture | pages [9] -->
m

<!-- b001026 | furniture | pages [9] -->
m

<!-- b001027 | furniture | pages [9] -->
m

<!-- b001028 | furniture | pages [9] -->
m

<!-- b001029 | furniture | pages [9] -->
m

<!-- b001030 | furniture | pages [9] -->
m

<!-- b001031 | furniture | pages [9] -->
m

<!-- b001032 | furniture | pages [9] -->
m

<!-- b001033 | furniture | pages [9] -->
m

<!-- b001034 | furniture | pages [9] -->
m

<!-- b001035 | furniture | pages [9] -->
m

<!-- b001036 | furniture | pages [9] -->
m

<!-- b001037 | furniture | pages [9] -->
m

<!-- b001038 | furniture | pages [9] -->
m

<!-- b001039 | furniture | pages [9] -->
m

<!-- b001040 | furniture | pages [9] -->
m

<!-- b001041 | furniture | pages [9] -->
m

<!-- b001042 | furniture | pages [9] -->
m

<!-- b001043 | furniture | pages [9] -->
m

<!-- b001044 | furniture | pages [9] -->
m

<!-- b001045 | furniture | pages [9] -->
m

<!-- b001046 | furniture | pages [9] -->
m

<!-- b001047 | furniture | pages [9] -->
m

<!-- b001048 | furniture | pages [9] -->
m

<!-- b001049 | furniture | pages [9] -->
m

<!-- b001050 | furniture | pages [9] -->
m

<!-- b001051 | furniture | pages [9] -->
m

<!-- b001052 | furniture | pages [9] -->
m

<!-- b001053 | furniture | pages [9] -->
m

<!-- b001054 | furniture | pages [9] -->
m

<!-- b001055 | furniture | pages [9] -->
m

<!-- b001056 | furniture | pages [9] -->
m

<!-- b001057 | furniture | pages [9] -->
m

<!-- b001058 | furniture | pages [9] -->
m

<!-- b001059 | furniture | pages [9] -->
m

<!-- b001060 | furniture | pages [9] -->
m

<!-- b001061 | furniture | pages [9] -->
m

<!-- b001062 | furniture | pages [9] -->
m

<!-- b001063 | furniture | pages [9] -->
m

<!-- b001064 | furniture | pages [9] -->
m

<!-- b001065 | furniture | pages [9] -->
m

<!-- b001066 | furniture | pages [9] -->
m

<!-- b001067 | furniture | pages [9] -->
m

<!-- b001068 | furniture | pages [9] -->
m

<!-- b001069 | furniture | pages [9] -->
m

<!-- b001070 | furniture | pages [9] -->
m

<!-- b001071 | furniture | pages [9] -->
m

<!-- b001072 | furniture | pages [9] -->
m

<!-- b001073 | furniture | pages [9] -->
m

<!-- b001074 | furniture | pages [9] -->
m

<!-- b001075 | furniture | pages [9] -->
m

<!-- b001076 | furniture | pages [9] -->
m

<!-- b001077 | furniture | pages [9] -->
m

<!-- b001078 | furniture | pages [9] -->
m

<!-- b001079 | furniture | pages [9] -->
m

<!-- b001080 | furniture | pages [9] -->
m

<!-- b001081 | furniture | pages [9] -->
m

<!-- b001082 | furniture | pages [9] -->
m

<!-- b001083 | furniture | pages [9] -->
m

<!-- b001084 | furniture | pages [9] -->
m

<!-- b001085 | furniture | pages [9] -->
m

<!-- b001086 | furniture | pages [9] -->
m

<!-- b001087 | furniture | pages [9] -->
m

<!-- b001088 | furniture | pages [9] -->
m

<!-- b001089 | furniture | pages [9] -->
m

<!-- b001090 | furniture | pages [9] -->
m

<!-- b001091 | furniture | pages [9] -->
m

<!-- b001092 | furniture | pages [9] -->
m

<!-- b001093 | furniture | pages [9] -->
m

<!-- b001094 | furniture | pages [9] -->
m

<!-- b001095 | furniture | pages [9] -->
m

<!-- b001096 | furniture | pages [9] -->
m

<!-- b001097 | furniture | pages [9] -->
m

<!-- b001098 | furniture | pages [9] -->
m

<!-- b001099 | furniture | pages [9] -->
m

<!-- b001100 | furniture | pages [9] -->
m

<!-- b001101 | furniture | pages [9] -->
m

<!-- b001102 | furniture | pages [9] -->
m

<!-- b001103 | furniture | pages [9] -->
m

<!-- b001104 | furniture | pages [9] -->
m

<!-- b001105 | furniture | pages [9] -->
m

<!-- b001106 | furniture | pages [9] -->
m

<!-- b001107 | furniture | pages [9] -->
m

<!-- b001108 | furniture | pages [9] -->
m

<!-- b001109 | furniture | pages [9] -->
m

<!-- b001110 | furniture | pages [9] -->
m

<!-- b001111 | furniture | pages [9] -->
m

<!-- b001112 | furniture | pages [9] -->
m

<!-- b001113 | furniture | pages [9] -->
m

<!-- b001114 | furniture | pages [9] -->
m

<!-- b001115 | furniture | pages [9] -->
m

<!-- b001116 | furniture | pages [9] -->
m

<!-- b001117 | furniture | pages [9] -->
m

<!-- b001118 | furniture | pages [9] -->
m

<!-- b001119 | furniture | pages [9] -->
m

<!-- b001120 | furniture | pages [9] -->
m

<!-- b001121 | furniture | pages [9] -->
m

<!-- b001122 | furniture | pages [9] -->
m

<!-- b001123 | furniture | pages [9] -->
m

<!-- b001124 | furniture | pages [9] -->
m

<!-- b001125 | furniture | pages [9] -->
m

<!-- b001126 | furniture | pages [10] -->
Team # 2519935

<!-- b001127 | furniture | pages [10] -->
Page 10 of 25

<!-- b001129 | prose | pages [10] -->
By analyzing the Closeness Centrality of G and G2, we can assess the impact of the bridge collapse before and after its occurrence. Closeness Centrality refers to the inverse of the average shortest path length from a node to all other nodes in the network, reflecting the efficiency of propagation within the network. For node v, the Closeness Centrality CC(v) is calculated as follows:

<!-- b001130 | prose | pages [10] -->
N −1 CC(v) = t d(v, t), (9) P

<!-- b001131 | prose | pages [10] -->
where d(v, t) is the shortest path length between node v and node t, and N is the total number of nodes in the network.

<!-- b001132 | heading | pages [10] -->
5.2 Model Solution and Results

<!-- b001133 | heading | pages [10] -->
5.2.1 The Impact around Baltimore

<!-- b001134 | prose | pages [10] -->
The impact of the bridge collapse on areas surrounding Baltimore primarily manifests through the highways. Using the model, we can calculate the Closeness Centrality for 39 highway nodes before and after the bridge collapse. The results are shown in the figure below.

<!-- b001135 | caption | pages [10] -->
Figure 8: Closeness Centrality of Nodes in G and G2

<!-- b001136 | prose | pages [10] -->
It can be observed that nodes 36-38 are most affected by the bridge collapse, corresponding to nodes 37-39 in Figure 7. Specifically, nodes 38 and 39 are located outside of Baltimore, which suggests that the collapse of the bridge indeed impacted the cities surrounding Baltimore, particularly node 39, which has been affected the most.

<!-- b001137 | prose | pages [10] -->
It is also evident that the Closeness Centrality of nodes 0-26 remains largely unchanged or experiences only minimal variation, suggesting that the impact of the bridge collapse on these nodes is relatively insignificant.

<!-- b001138 | prose | pages [10, 11] -->
关注数学模型 5.2.2 The Impact in Baltimore

<!-- b001139 | furniture | pages [10] -->
2

<!-- b001140 | furniture | pages [10] -->
MATHmodels

<!-- b001141 | furniture | pages [10] -->
获取更多资讯

<!-- b001142 | furniture | pages [11] -->
Team # 2519935

<!-- b001143 | furniture | pages [11] -->
Page 11 of 25

<!-- b001145 | prose | pages [11] -->
First, we analyze the impact in Baltimore. Based on the established Impact Assessment Model, we can calculate the AADT and AAWDT for different nodes before the bridge collapse in 2024. Using the formulas from equation (8), we can calculate the traffic volume for both commuters and non-commuters on different roads.

<!-- b001146 | prose | pages [11] -->
We find that traffic volume for non-commuters is generally concentrated in smaller ranges, while the traffic volume for commuters is distributed more evenly between 0 and 10,000.

<!-- b001147 | prose | pages [11] -->
Next, using the diagram in Figure 6, we can calculate the impact coefficient βi for road ¿. The impact coefficients for commuters and non-commuters are shown in the figure below.

<!-- b001148 | prose | pages [11] -->
300 400 Commuter Non-commuter 250 350 300 200 Frequency 250 150 200 150 100 100 50 50 0 0.00 0.25 0.50 1.50 1.75 2.00 0.25 0.50 1.50 1.75 2.00 0.00 0.75 1.00 1.25 0.75 1.00 1.25 Influence Coefficient β Influence Coefficient β

<!-- b001149 | prose | pages [11] -->
● ●

<!-- b001150 | caption | pages [11] -->
Figure 9: Influence Coefficients of Various Stakeholders

<!-- b001151 | prose | pages [11] -->
From this figure, it is clear that the impact coefficients for commuters are mostly concentrated around 1, while those for non-commuters are more dispersed, with the majority of impact coefficients being less than 1. This indicates that the collapse of the bridge hindered non- commuters' travel, resulting in a decrease in traffic volume for non-commuters on many roads. For commuter traffic, some roads saw an increase in traffic, while others experienced a decrease.

<!-- b001152 | prose | pages [11] -->
We further visualize the top 5 and bottom 5 roads in terms of impact coefficients for both commuters and non-commuters in the figure below.

<!-- b001153 | prose | pages [11, 12] -->
Commuter Mean Non-commuter Mean RAMP 5 FR RAMP 9 (FR MD655) TO MD 157 58 RR    MS8 Non-commuter Current Commuter Current RAMP 6 FR RAMP 3 TO GREENSPRING AVE RAMP 6 FR RAMP 3 TO GREENSPRING AVE Roeaed Name Roadd Nme RAMP 3 FR MD 158 TO MD 695 NB RAMP 3 FR MD 158 TO MD 695 NB RAMP 8 FRIS 83 S8 TO MT ROYAL AVE RAMP 8 FR IS 83 SB TO MT ROYAL AVE R D      MO O  PGS) R P   P  P  P 9S) 1000 3000 4000 5000 200 400 800 1000 1200 2000 600 Value Value (b) Top 5 Roads with Largest Non-commuter Traffic Increase (a) Top 5 Roads with Largest Commuter Traffic Increase Non-commuter Mean RAMP 3 FR IS 695 EB TO GREENSPRING AVE RAMP 9 FR IS 79S SB TO METRO CENTRE Non-commuter Current RAMP 6 FR PARALLEL DR TO RAMP 8 RAMIP 3 FR IS 695 EB TO GREENSPRING AVE Roadd eame Koadd ame BALTIMORE BLVD LAKE MONTEBELLO DR METROPOLITAN BLVD RAMP 6 FR PARALLEL DR TO RAMP 8 Commuter Mean LAKE MONTEBELLO DR EAST AVE Commuter Current 2000 8000 10000 12000 4000 4000 6000 1000 2000 3000 5000 6000 Value Value (d) Top 5 Roads with Largest Non-commuter Traffic Decrease (c) Top 5 Roads with Largest Commuter Traffic Decrease These roads are most significantly affected by the bridge collapse. The road "RAMP 5 FR RAMP 9 (FR MD695) TO MD 157 SB" has the highest impact coefficient for both commuters and non-commuters, reaching 11.994. Among commuters, the road "RAMP 9 FR IS 795 SB TO METRO CENTRE" has the smallest impact coefficient of 0.005, while for non-commuters, "RAMP 3 FR IS 695 EB TO GREENSPRING AVE" has the smallest impact coefficient of 0.059.

<!-- b001154 | caption | pages [11] -->
Figure 10: The Roads with the Greatest Impact

<!-- b001155 | furniture | pages [12] -->
Team # 2519935

<!-- b001156 | furniture | pages [12] -->
Page 12 of 25

<!-- b001158 | prose | pages [12] -->
The following visualizations display the top 100 and bottom 100 roads for commuters and non-commuters, providing a more intuitive representation of how different roads in Baltimore are affected by the bridge collapse. Roads where the impact coefficient is closer to blue are negatively affected, while those closer to red are positively heavily impacted.

<!-- b001159 | caption | pages [12] -->
Figure 11: Visualization of the Top 100 Affected Roads

<!-- b001160 | prose | pages [12] -->
For commuters, due to the collapse of the bridge, the traffic that previously crossed the Patapsco River must now be rerouted through "Bridge-II" (as shown in the figure), leading to an increase in traffic volume on this bridge, with an impact coefficient greater than 1. However, for non-commuters, the impact coefficient is less than 1, possibly because the collapse of the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m bridge reduced non-commuters’ willingness to travel across the river, thereby decreasing traffic m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m volume compared to before the collapse. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The figure also reveals a significant increase in Beltway traffic for both stakeholder groups, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m particularly on the segment “RAMP 5 FR RAMP 9 (FR MD695) TO MD 157 SB” shown in m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001161 | caption | pages [12] -->
Figure 10. This suggests that, following the bridge collapse, both stakeholder groups are more

<!-- b001162 | prose | pages [12] -->
frequently traveling on the Beltway. A possible explanation for this behavior is the higher speed limit on this road, which allows drivers to reach their destinations more quickly.

<!-- b001163 | prose | pages [12, 13] -->
关注数学模型 Task 2: The impact of the project on the bus system 6

<!-- b001164 | furniture | pages [12] -->
2

<!-- b001165 | furniture | pages [12] -->
MATHmodels

<!-- b001166 | furniture | pages [12] -->
获取更多资讯

<!-- b001167 | furniture | pages [13] -->
Page 13 of 25

<!-- b001168 | furniture | pages [13] -->
Team # 2519935

<!-- b001170 | prose | pages [13] -->
6.1

<!-- b001171 | heading | pages [13] -->
Three-layer Bus Network Model (TBN)

<!-- b001172 | prose | pages [13] -->
As urban development progresses, various modes of transportation have emerged, yet buses remain the preferred mode of travel for most individuals. This study focuses on optimizing the public transportation system of Baltimore City, assessing the potential impact on existing urban residents after its implementation. By utilizing the originally constructed transportation network, we develop a TBN Model to analyze the connectivity between higher and lower layers.

<!-- b001173 | prose | pages [13] -->
▶Step 1: Classification of Bus Station Levels

<!-- b001174 | prose | pages [13] -->
We apply and refine the weighted k-shell decomposition algorithm for classifying each bus station[8][9]. In the original weighted k-shell decomposition method, the weighted degree ks is calculated by considering both the degree of the node and the weight of its edges, reflecting the importance of a node. It is defined as follows:

<!-- b001175 | prose | pages [13] -->
ki ks = [ka(∑ wij)β]a+β, (10) j ● where ki represents the degree of node i; wij represents the weight of the edge between nodes ¿ 1 and j; α andβ denote the influence of degree and weight, respectively.

<!-- b001176 | prose | pages [13] -->
However, in a bus network, stations are abstracted as nodes, overlooking their intrinsic attributes such as geographical location, connections to surrounding environments, and popu- lation density in the area. To address this, we introduce a weighted metric S to quantify each bus station's attributes, incorporating the POI (Point of Interest) [11] indicator and the num- ber of on-off passengers. This approach ensures a comprehensive consideration of the actual conditions, linking bus stations closely with urban planning.

<!-- b001177 | prose | pages [13] -->
(11) where Ni represents the total number of passengers boarding and alighting at station i, and the POI indicator reflects the distribution of infrastructure within a defined area, often used to gauge service convenience and resident activity. Based on Baltimore's actual conditions, we classify five types as shown below:

<!-- b001178 | caption | pages [13] -->
Table 5: POI Weight

<!-- b001179 | prose | pages [13] -->
Weight POI Type Weight POI Type Weight POI Type 0.7 1.5 railway station subway exchange tourist attraction 0.5 0.75 markets universities

<!-- b001180 | prose | pages [13] -->
Next, we employ the entropy weight method (TOPSIS) to compute the weight of the two indicators and derive the bus station scores S. Based on the bus station scores S and equation (11), we design an improved weighted k-shell model, assuming that all bus routes are of equal importance, with edge weights wij set to 1. Typically, α = β = 1, assuming equal influence of degree and weight.

<!-- b001181 | prose | pages [13, 14] -->
ks = √ki × S, (12) where ki represents the degree of node i, i.e., the number of edges connecting to the node. In the transportation network model, the number of routes served by bus station i is equivalent to its degree:

<!-- b001182 | furniture | pages [14] -->
Page 14 of 25

<!-- b001183 | furniture | pages [14] -->
Team # 2519935

<!-- b001185 | prose | pages [14] -->
(13) ki = length(Routes_Seri),

<!-- b001186 | prose | pages [14] -->
where Routes_Seri denotes the set of routes served by station i.

<!-- b001187 | prose | pages [14] -->
Thus, we assign a unique ks to each bus station. A higher ks indicates greater importance of the station in the network, and it corresponds to a higher tier in the model.

<!-- b001188 | prose | pages [14] -->
Finally, we discretize the ks values to facilitate the counting of nodes within each range. In this paper, we define the interval length as 0.05. For example, if ks = 0.045 ∈ (0, 0.05), all nodes within this range have their ks values adjusted to 0.25, which represents the interval mean.

<!-- b001189 | prose | pages [14] -->
▶Step 2: Construction of the Three-tier Bus Network

<!-- b001190 | prose | pages [14] -->
At this point, we have obtained the distribution of ks, as shown in the following histogram:

<!-- b001191 | prose | pages [14] -->
400 80 Derivative of Cumulative Sum 20

<!-- b001192 | prose | pages [14] -->
15 60 300 Frequency 10

<!-- b001193 | prose | pages [14] -->
40 5 200

<!-- b001194 | prose | pages [14] -->
2.0 1.9 1.7 1.8 1.6 20 100

<!-- b001195 | prose | pages [14] -->
0 0 0.0 0.5 1.0 2.5 1.5 2.0 3.0 Evaluation Score

<!-- b001196 | caption | pages [14] -->
Figure 12: Histogram of Evaluation Indicators

<!-- b001197 | prose | pages [14] -->
Based on the distribution of ks values, we divide the transportation network into three tiers: the core layer, the bridge layer, and the peripheral layer [12]. The core layer consists of key traffic nodes that serve as hubs in the network, with the highest ks values. Analyzing the high ks values, we identify a breaking point at a certain value ks,i, which signifies the boundary between the core and bridge layers. Nodes with ks > ks,i are categorized as belonging to the core layer.

<!-- b001198 | prose | pages [14] -->
We then analyze the nodes with low ks values. Defining the cumulative ksvalue for a node: for a node ks < a, we calculate the total number of nodes within this range and sum their ks values to obtain the cumulative ks value. The point at which the cumulative ks value reaches a peak corresponds to the boundary between the bridge and peripheral layers. Nodes with ks < ks,j are classified into the peripheral layer. The remaining nodes, where ks,i < ks < ks,j, belong to the bridge layer.

<!-- b001199 | prose | pages [14] -->
关注数学模型

<!-- b001200 | furniture | pages [14] -->
获取更多资讯

<!-- b001201 | furniture | pages [15] -->
Team # 2519935

<!-- b001202 | furniture | pages [15] -->
Page 15 of 25

<!-- b001203 | heading | pages [15] -->
6.2 Model Solution and Results

<!-- b001204 | prose | pages [15] -->
The project aims to improve the public transportation network by adding two new bus routes after analyzing the tiers of bus stations. To assess the need for additional bus routes, data regarding key infrastructure in Baltimore — such as popular tourist attractions, universities, and supermarkets — are collected to evaluate the residential activity levels at different bus stations. 微信公众号：数学模型 Based on the constructed Three-layer Bus Network (TBN) model, the three-tier bus network of Baltimore is shown in the figure below.

<!-- b001205 | prose | pages [15] -->
微信号：MATHmodels

<!-- b001206 | caption | pages [15] -->
Figure 13: The three layers in the higher-order bus network

<!-- b001207 | prose | pages [15] -->
In the Core Layer, there are 11 bus stations, in the Bridge Layer there are 1,180 bus stations, and in the Outer Layer, there are 1,444 bus stations. To enhance the network, roads within different layers are classified using a shortest distance search method, dividing the roads into five categories. The locations(a) and distribution percentages of these roads(b) are depicted in the figure below.

<!-- b001208 | caption | pages [15] -->
Figure 14: Bus routes in TBN model

<!-- b001209 | prose | pages [15, 16] -->
Based on the TBN model, our goal is to construct additional bus routes connecting the Core Layer and Bridge Layer, as well as more routes between the Bridge Layer and Outer Layer, to facilitate residents’ travel from the outer regions to the city center, specifically to bus stations in the Core Layer. Thus, the proposed project suggests adding two new bus routes to achieve this objective. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m A 2-kilometer radius circle is drawn with the average coordinates of the 11 bus stations in the Core Layer as the center. The surrounding local transportation network and infrastructure are shown in figure (a). The final bus route plan is shown in figure (b), where the two new routes significantly improve connectivity between the Core Layer and Bridge Layer bus stations.

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

<!-- b001227 | furniture | pages [15] -->
m

<!-- b001228 | furniture | pages [15] -->
m

<!-- b001229 | furniture | pages [15] -->
m

<!-- b001230 | furniture | pages [15] -->
m

<!-- b001231 | furniture | pages [15] -->
m

<!-- b001232 | furniture | pages [15] -->
m

<!-- b001233 | furniture | pages [15] -->
m

<!-- b001234 | furniture | pages [15] -->
m

<!-- b001235 | furniture | pages [15] -->
m

<!-- b001236 | furniture | pages [15] -->
m

<!-- b001237 | furniture | pages [15] -->
m

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

<!-- b001534 | furniture | pages [16] -->
Team # 2519935

<!-- b001535 | furniture | pages [16] -->
Page 16 of 25

<!-- b001537 | caption | pages [16] -->
Figure 15: Project Analysis

<!-- b001538 | prose | pages [16] -->
• Tourists: For tourists, the new bus routes connect many famous attractions, making it easier to travel between different points of interest.

<!-- b001539 | prose | pages [16] -->
• Suburban Residents: For suburban residents, the project significantly improves connec- tivity between the Bridge and Core Layers, providing easier access from the suburbs to areas with more developed infrastructure.

<!-- b001540 | prose | pages [16] -->
• College Students: For college students, the project also considers universities such as Johns Hopkins University, offering students more transportation options.

<!-- b001541 | prose | pages [16] -->
Based on the project, the following five variations in road conditions are observed, as illustrated in the figure below.

<!-- b001542 | caption | pages [16] -->
Figure 16: Changes in road conditions before and after project implementation

<!-- b001543 | prose | pages [16] -->
As depicted in the figure, the implementation of this project resulted in an 18.3% increase in road conditions between the Core and Bridge layers. Additionally, the road conditions within the Core layer increased by 95%, highlighting the significant advantages of this project. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001544 | furniture | pages [16] -->
2

<!-- b001545 | furniture | pages [16] -->
m

<!-- b001546 | furniture | pages [16] -->
m

<!-- b001547 | furniture | pages [16] -->
m

<!-- b001548 | furniture | pages [16] -->
m

<!-- b001549 | furniture | pages [16] -->
m

<!-- b001550 | furniture | pages [16] -->
m

<!-- b001551 | furniture | pages [16] -->
m

<!-- b001552 | furniture | pages [16] -->
m

<!-- b001553 | furniture | pages [16] -->
m

<!-- b001554 | furniture | pages [16] -->
m

<!-- b001555 | furniture | pages [16] -->
m

<!-- b001556 | furniture | pages [16] -->
m

<!-- b001557 | furniture | pages [16] -->
m

<!-- b001558 | furniture | pages [16] -->
m

<!-- b001559 | furniture | pages [16] -->
m

<!-- b001560 | furniture | pages [16] -->
m

<!-- b001561 | furniture | pages [16] -->
m

<!-- b001562 | furniture | pages [16] -->
m

<!-- b001563 | furniture | pages [16] -->
m

<!-- b001564 | furniture | pages [16] -->
m

<!-- b001565 | furniture | pages [16] -->
m

<!-- b001566 | furniture | pages [16] -->
m

<!-- b001567 | furniture | pages [16] -->
m

<!-- b001568 | furniture | pages [16] -->
m

<!-- b001569 | furniture | pages [16] -->
m

<!-- b001570 | furniture | pages [16] -->
m

<!-- b001571 | furniture | pages [16] -->
m

<!-- b001572 | furniture | pages [16] -->
m

<!-- b001573 | furniture | pages [16] -->
m

<!-- b001574 | furniture | pages [16] -->
m

<!-- b001575 | furniture | pages [16] -->
m

<!-- b001576 | furniture | pages [16] -->
m

<!-- b001577 | furniture | pages [16] -->
m

<!-- b001578 | furniture | pages [16] -->
m

<!-- b001579 | furniture | pages [16] -->
m

<!-- b001580 | furniture | pages [16] -->
m

<!-- b001581 | furniture | pages [16] -->
m

<!-- b001582 | furniture | pages [16] -->
m

<!-- b001583 | furniture | pages [16] -->
m

<!-- b001584 | furniture | pages [16] -->
m

<!-- b001585 | furniture | pages [16] -->
m

<!-- b001586 | furniture | pages [16] -->
m

<!-- b001587 | furniture | pages [16] -->
m

<!-- b001588 | furniture | pages [16] -->
m

<!-- b001589 | furniture | pages [16] -->
m

<!-- b001590 | furniture | pages [16] -->
m

<!-- b001591 | furniture | pages [16] -->
m

<!-- b001592 | furniture | pages [16] -->
m

<!-- b001593 | furniture | pages [16] -->
m

<!-- b001594 | furniture | pages [16] -->
m

<!-- b001595 | furniture | pages [16] -->
m

<!-- b001596 | furniture | pages [16] -->
m

<!-- b001597 | furniture | pages [16] -->
m

<!-- b001598 | furniture | pages [16] -->
m

<!-- b001599 | furniture | pages [16] -->
m

<!-- b001600 | furniture | pages [16] -->
m

<!-- b001601 | furniture | pages [16] -->
m

<!-- b001602 | furniture | pages [16] -->
m

<!-- b001603 | furniture | pages [16] -->
m

<!-- b001604 | furniture | pages [16] -->
m

<!-- b001605 | furniture | pages [16] -->
m

<!-- b001606 | furniture | pages [16] -->
m

<!-- b001607 | furniture | pages [16] -->
m

<!-- b001608 | furniture | pages [16] -->
m

<!-- b001609 | furniture | pages [16] -->
m

<!-- b001610 | furniture | pages [16] -->
m

<!-- b001611 | furniture | pages [16] -->
m

<!-- b001612 | furniture | pages [16] -->
m

<!-- b001613 | furniture | pages [16] -->
m

<!-- b001614 | furniture | pages [16] -->
m

<!-- b001615 | furniture | pages [16] -->
m

<!-- b001616 | furniture | pages [16] -->
m

<!-- b001617 | furniture | pages [16] -->
m

<!-- b001618 | furniture | pages [16] -->
m

<!-- b001619 | furniture | pages [16] -->
m

<!-- b001620 | furniture | pages [16] -->
m

<!-- b001621 | furniture | pages [16] -->
m

<!-- b001622 | furniture | pages [16] -->
m

<!-- b001623 | furniture | pages [16] -->
m

<!-- b001624 | furniture | pages [16] -->
m

<!-- b001625 | furniture | pages [16] -->
m

<!-- b001626 | furniture | pages [16] -->
m

<!-- b001627 | furniture | pages [16] -->
m

<!-- b001628 | furniture | pages [16] -->
m

<!-- b001629 | furniture | pages [16] -->
m

<!-- b001630 | furniture | pages [16] -->
m

<!-- b001631 | furniture | pages [16] -->
m

<!-- b001632 | furniture | pages [16] -->
m

<!-- b001633 | furniture | pages [16] -->
m

<!-- b001634 | furniture | pages [16] -->
m

<!-- b001635 | furniture | pages [16] -->
m

<!-- b001636 | furniture | pages [16] -->
m

<!-- b001637 | furniture | pages [16] -->
m

<!-- b001638 | furniture | pages [16] -->
m

<!-- b001639 | furniture | pages [16] -->
m

<!-- b001640 | furniture | pages [16] -->
m

<!-- b001641 | furniture | pages [16] -->
m

<!-- b001642 | furniture | pages [16] -->
m

<!-- b001643 | furniture | pages [16] -->
m

<!-- b001644 | furniture | pages [16] -->
m

<!-- b001645 | furniture | pages [16] -->
m

<!-- b001646 | furniture | pages [16] -->
m

<!-- b001647 | furniture | pages [16] -->
m

<!-- b001648 | furniture | pages [16] -->
m

<!-- b001649 | furniture | pages [16] -->
m

<!-- b001650 | furniture | pages [16] -->
m

<!-- b001651 | furniture | pages [16] -->
m

<!-- b001652 | furniture | pages [16] -->
m

<!-- b001653 | furniture | pages [16] -->
m

<!-- b001654 | furniture | pages [16] -->
m

<!-- b001655 | furniture | pages [16] -->
m

<!-- b001656 | furniture | pages [16] -->
m

<!-- b001657 | furniture | pages [16] -->
m

<!-- b001658 | furniture | pages [16] -->
MATHmodels

<!-- b001659 | furniture | pages [16] -->
获取更多资讯

<!-- b001660 | furniture | pages [16] -->
m

<!-- b001661 | furniture | pages [16] -->
m

<!-- b001662 | furniture | pages [16] -->
m

<!-- b001663 | furniture | pages [16] -->
m

<!-- b001664 | furniture | pages [16] -->
m

<!-- b001665 | furniture | pages [16] -->
m

<!-- b001666 | furniture | pages [16] -->
m

<!-- b001667 | furniture | pages [16] -->
m

<!-- b001668 | furniture | pages [16] -->
m

<!-- b001669 | furniture | pages [16] -->
m

<!-- b001670 | furniture | pages [16] -->
m

<!-- b001671 | furniture | pages [16] -->
m

<!-- b001672 | furniture | pages [16] -->
m

<!-- b001673 | furniture | pages [16] -->
m

<!-- b001674 | furniture | pages [16] -->
m

<!-- b001675 | furniture | pages [16] -->
m

<!-- b001676 | furniture | pages [16] -->
m

<!-- b001677 | furniture | pages [16] -->
m

<!-- b001678 | furniture | pages [16] -->
m

<!-- b001679 | furniture | pages [16] -->
m

<!-- b001680 | furniture | pages [16] -->
m

<!-- b001681 | furniture | pages [16] -->
m

<!-- b001682 | furniture | pages [16] -->
m

<!-- b001683 | furniture | pages [16] -->
m

<!-- b001684 | furniture | pages [16] -->
m

<!-- b001685 | furniture | pages [16] -->
m

<!-- b001686 | furniture | pages [16] -->
m

<!-- b001687 | furniture | pages [16] -->
m

<!-- b001688 | furniture | pages [16] -->
m

<!-- b001689 | furniture | pages [16] -->
m

<!-- b001690 | furniture | pages [16] -->
m

<!-- b001691 | furniture | pages [16] -->
m

<!-- b001692 | furniture | pages [16] -->
m

<!-- b001693 | furniture | pages [16] -->
m

<!-- b001694 | furniture | pages [16] -->
m

<!-- b001695 | furniture | pages [16] -->
m

<!-- b001696 | furniture | pages [16] -->
m

<!-- b001697 | furniture | pages [16] -->
m

<!-- b001698 | furniture | pages [16] -->
m

<!-- b001699 | furniture | pages [16] -->
m

<!-- b001700 | furniture | pages [16] -->
m

<!-- b001701 | furniture | pages [16] -->
m

<!-- b001702 | furniture | pages [16] -->
m

<!-- b001703 | furniture | pages [16] -->
m

<!-- b001704 | furniture | pages [16] -->
m

<!-- b001705 | furniture | pages [16] -->
m

<!-- b001706 | furniture | pages [16] -->
m

<!-- b001707 | furniture | pages [16] -->
m

<!-- b001708 | furniture | pages [16] -->
m

<!-- b001709 | furniture | pages [16] -->
m

<!-- b001710 | furniture | pages [16] -->
m

<!-- b001711 | furniture | pages [16] -->
m

<!-- b001712 | furniture | pages [16] -->
m

<!-- b001713 | furniture | pages [16] -->
m

<!-- b001714 | furniture | pages [16] -->
m

<!-- b001715 | furniture | pages [16] -->
m

<!-- b001716 | furniture | pages [16] -->
m

<!-- b001717 | furniture | pages [16] -->
m

<!-- b001718 | furniture | pages [16] -->
m

<!-- b001719 | furniture | pages [16] -->
m

<!-- b001720 | furniture | pages [16] -->
m

<!-- b001721 | furniture | pages [16] -->
m

<!-- b001722 | furniture | pages [16] -->
m

<!-- b001723 | furniture | pages [16] -->
m

<!-- b001724 | furniture | pages [16] -->
m

<!-- b001725 | furniture | pages [16] -->
m

<!-- b001726 | furniture | pages [16] -->
m

<!-- b001727 | furniture | pages [16] -->
m

<!-- b001728 | furniture | pages [16] -->
m

<!-- b001729 | furniture | pages [16] -->
m

<!-- b001730 | furniture | pages [16] -->
m

<!-- b001731 | furniture | pages [16] -->
m

<!-- b001732 | furniture | pages [16] -->
m

<!-- b001733 | furniture | pages [16] -->
m

<!-- b001734 | furniture | pages [16] -->
m

<!-- b001735 | furniture | pages [16] -->
m

<!-- b001736 | furniture | pages [16] -->
m

<!-- b001737 | furniture | pages [16] -->
m

<!-- b001738 | furniture | pages [16] -->
m

<!-- b001739 | furniture | pages [16] -->
m

<!-- b001740 | furniture | pages [16] -->
m

<!-- b001741 | furniture | pages [16] -->
m

<!-- b001742 | furniture | pages [16] -->
m

<!-- b001743 | furniture | pages [16] -->
m

<!-- b001744 | furniture | pages [16] -->
m

<!-- b001745 | furniture | pages [16] -->
m

<!-- b001746 | furniture | pages [16] -->
m

<!-- b001747 | furniture | pages [16] -->
m

<!-- b001748 | furniture | pages [16] -->
m

<!-- b001749 | furniture | pages [16] -->
m

<!-- b001750 | furniture | pages [16] -->
m

<!-- b001751 | furniture | pages [16] -->
m

<!-- b001752 | furniture | pages [16] -->
m

<!-- b001753 | furniture | pages [16] -->
m

<!-- b001754 | furniture | pages [16] -->
m

<!-- b001755 | furniture | pages [16] -->
m

<!-- b001756 | furniture | pages [16] -->
m

<!-- b001757 | furniture | pages [16] -->
m

<!-- b001758 | furniture | pages [16] -->
m

<!-- b001759 | furniture | pages [16] -->
m

<!-- b001760 | furniture | pages [16] -->
m

<!-- b001761 | furniture | pages [16] -->
m

<!-- b001762 | furniture | pages [16] -->
m

<!-- b001763 | furniture | pages [16] -->
m

<!-- b001764 | furniture | pages [16] -->
m

<!-- b001765 | furniture | pages [16] -->
m

<!-- b001766 | furniture | pages [16] -->
m

<!-- b001767 | furniture | pages [16] -->
m

<!-- b001768 | furniture | pages [16] -->
m

<!-- b001769 | furniture | pages [16] -->
m

<!-- b001770 | furniture | pages [16] -->
m

<!-- b001771 | furniture | pages [16] -->
m

<!-- b001772 | furniture | pages [16] -->
m

<!-- b001773 | furniture | pages [16] -->
m

<!-- b001774 | furniture | pages [16] -->
m

<!-- b001775 | furniture | pages [16] -->
m

<!-- b001776 | furniture | pages [16] -->
m

<!-- b001777 | furniture | pages [16] -->
m

<!-- b001778 | furniture | pages [16] -->
m

<!-- b001779 | furniture | pages [16] -->
m

<!-- b001780 | furniture | pages [16] -->
m

<!-- b001781 | furniture | pages [16] -->
m

<!-- b001782 | furniture | pages [16] -->
m

<!-- b001783 | furniture | pages [16] -->
m

<!-- b001784 | furniture | pages [16] -->
m

<!-- b001785 | furniture | pages [16] -->
m

<!-- b001786 | furniture | pages [16] -->
m

<!-- b001787 | furniture | pages [16] -->
m

<!-- b001788 | furniture | pages [16] -->
m

<!-- b001789 | furniture | pages [16] -->
m

<!-- b001790 | furniture | pages [16] -->
m

<!-- b001791 | furniture | pages [16] -->
m

<!-- b001792 | furniture | pages [16] -->
m

<!-- b001793 | furniture | pages [16] -->
m

<!-- b001794 | furniture | pages [16] -->
m

<!-- b001795 | furniture | pages [16] -->
m

<!-- b001796 | furniture | pages [16] -->
m

<!-- b001797 | furniture | pages [16] -->
m

<!-- b001798 | furniture | pages [16] -->
m

<!-- b001799 | furniture | pages [16] -->
m

<!-- b001800 | furniture | pages [16] -->
m

<!-- b001801 | furniture | pages [16] -->
m

<!-- b001802 | furniture | pages [16] -->
m

<!-- b001803 | furniture | pages [16] -->
m

<!-- b001804 | furniture | pages [16] -->
m

<!-- b001805 | furniture | pages [16] -->
m

<!-- b001806 | furniture | pages [16] -->
m

<!-- b001807 | furniture | pages [16] -->
m

<!-- b001808 | furniture | pages [16] -->
m

<!-- b001809 | furniture | pages [16] -->
m

<!-- b001810 | furniture | pages [16] -->
m

<!-- b001811 | furniture | pages [16] -->
m

<!-- b001812 | furniture | pages [16] -->
m

<!-- b001813 | furniture | pages [16] -->
m

<!-- b001814 | furniture | pages [16] -->
m

<!-- b001815 | furniture | pages [16] -->
m

<!-- b001816 | furniture | pages [16] -->
m

<!-- b001817 | furniture | pages [16] -->
m

<!-- b001818 | furniture | pages [16] -->
m

<!-- b001819 | furniture | pages [16] -->
m

<!-- b001820 | furniture | pages [16] -->
m

<!-- b001821 | furniture | pages [16] -->
m

<!-- b001822 | furniture | pages [16] -->
m

<!-- b001823 | furniture | pages [16] -->
m

<!-- b001824 | furniture | pages [16] -->
m

<!-- b001825 | furniture | pages [16] -->
m

<!-- b001826 | furniture | pages [16] -->
m

<!-- b001827 | furniture | pages [16] -->
m

<!-- b001828 | furniture | pages [16] -->
m

<!-- b001829 | furniture | pages [16] -->
m

<!-- b001830 | furniture | pages [16] -->
m

<!-- b001831 | furniture | pages [16] -->
m

<!-- b001832 | furniture | pages [16] -->
m

<!-- b001833 | furniture | pages [16] -->
m

<!-- b001834 | furniture | pages [16] -->
m

<!-- b001835 | furniture | pages [16] -->
m

<!-- b001836 | furniture | pages [16] -->
m

<!-- b001837 | furniture | pages [16] -->
m

<!-- b001838 | furniture | pages [16] -->
m

<!-- b001839 | furniture | pages [16] -->
m

<!-- b001840 | furniture | pages [16] -->
m

<!-- b001841 | furniture | pages [16] -->
m

<!-- b001842 | furniture | pages [16] -->
m

<!-- b001843 | furniture | pages [16] -->
m

<!-- b001844 | furniture | pages [16] -->
m

<!-- b001845 | furniture | pages [16] -->
m

<!-- b001846 | furniture | pages [16] -->
m

<!-- b001847 | furniture | pages [16] -->
m

<!-- b001848 | furniture | pages [16] -->
m

<!-- b001849 | furniture | pages [16] -->
m

<!-- b001850 | furniture | pages [16] -->
m

<!-- b001851 | furniture | pages [16] -->
m

<!-- b001852 | furniture | pages [16] -->
m

<!-- b001853 | furniture | pages [16] -->
m

<!-- b001854 | furniture | pages [16] -->
m

<!-- b001855 | furniture | pages [16] -->
m

<!-- b001856 | furniture | pages [16] -->
m

<!-- b001857 | furniture | pages [16] -->
m

<!-- b001858 | furniture | pages [16] -->
m

<!-- b001859 | furniture | pages [16] -->
m

<!-- b001860 | furniture | pages [16] -->
m

<!-- b001861 | furniture | pages [16] -->
m

<!-- b001862 | furniture | pages [16] -->
m

<!-- b001863 | furniture | pages [16] -->
m

<!-- b001864 | furniture | pages [16] -->
m

<!-- b001865 | furniture | pages [16] -->
m

<!-- b001866 | furniture | pages [16] -->
m

<!-- b001867 | furniture | pages [16] -->
m

<!-- b001868 | furniture | pages [16] -->
m

<!-- b001869 | furniture | pages [16] -->
m

<!-- b001870 | furniture | pages [16] -->
m

<!-- b001871 | furniture | pages [16] -->
m

<!-- b001872 | furniture | pages [16] -->
m

<!-- b001873 | furniture | pages [16] -->
m

<!-- b001874 | furniture | pages [16] -->
m

<!-- b001875 | furniture | pages [16] -->
m

<!-- b001876 | furniture | pages [16] -->
m

<!-- b001877 | furniture | pages [16] -->
m

<!-- b001878 | furniture | pages [16] -->
m

<!-- b001879 | furniture | pages [16] -->
m

<!-- b001880 | furniture | pages [16] -->
m

<!-- b001881 | furniture | pages [16] -->
m

<!-- b001882 | furniture | pages [16] -->
m

<!-- b001883 | furniture | pages [16] -->
m

<!-- b001884 | furniture | pages [16] -->
m

<!-- b001885 | furniture | pages [16] -->
m

<!-- b001886 | furniture | pages [16] -->
m

<!-- b001887 | furniture | pages [16] -->
m

<!-- b001888 | furniture | pages [16] -->
m

<!-- b001889 | furniture | pages [16] -->
m

<!-- b001890 | furniture | pages [16] -->
m

<!-- b001891 | furniture | pages [16] -->
m

<!-- b001892 | furniture | pages [16] -->
m

<!-- b001893 | furniture | pages [16] -->
m

<!-- b001894 | furniture | pages [16] -->
m

<!-- b001895 | furniture | pages [16] -->
m

<!-- b001896 | furniture | pages [16] -->
m

<!-- b001897 | furniture | pages [16] -->
m

<!-- b001898 | furniture | pages [16] -->
m

<!-- b001899 | furniture | pages [16] -->
m

<!-- b001900 | furniture | pages [16] -->
m

<!-- b001901 | furniture | pages [16] -->
m

<!-- b001902 | furniture | pages [17] -->
Team # 2519935

<!-- b001903 | furniture | pages [17] -->
Page 17 of 25

<!-- b001904 | heading | pages [17] -->
7 Task 3: The project best improves the lives of the residents

<!-- b001905 | heading | pages [17] -->
7.1 Improved Dijkstra Algorithm

<!-- b001906 | prose | pages [17] -->
To analyze the impact of newly constructed metro lines on the travel patterns of Baltimore’s residents, we have developed a hierarchical path planning model. Unlike the traditional Dijkstra algorithm, we update the weights of road paths to represent travel times, with the primary objective being to minimize the total travel time:

<!-- b001907 | prose | pages [17] -->
a(u, v) X X Nd ∈N, min T = t(i, j) = v(L(u, v)), (14) 微信公众号：数学模型 i,j∈Nd i,j∈Nd where Nd denotes the set of nodes involved in achieving the shortest travel time.

<!-- b001908 | heading | pages [17] -->
7.2 Double Density Fitting Model (DDF)

<!-- b001909 | prose | pages [17] -->
Public transit station density is frequently used as an indicator of transportation accessibility, which is inherently linked to road network density. In this section, we examine the potential correlation between bus station density and road network density. We employ road density to estimate the effect of unconstructed metro stations on the density of public transit stations. Additionally, we calculate the current bus station density surrounding the existing two metro stations to evaluate the impact of metro construction on bus stations. 微信号：MATHmodels  Step 1: Grid Map Creation

<!-- b001910 | prose | pages [17] -->
A 6×6 grid map is constructed for the central district of Baltimore to estimate the density within each grid cell.

<!-- b001911 | caption | pages [17] -->
Figure 17: Grid Map

<!-- b001912 | prose | pages [17] -->
 Step 2: Calculation of Bus Station Density and Road Network Density

<!-- b001913 | prose | pages [17] -->
Since the area of each grid cell is uniform, we simplify the road network density to the total length of accessible roads within the region, while the bus station density is represented by the total number of bus stations within the grid. This is formalized as:

<!-- b001914 | prose | pages [17, 18] -->
 X Nb ∈N ρbus = v,     v∈Nb , (15) X Nr ∈N ρroad = a(i, j),     i,j∈Nr m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m where Nb represents the set of bus stations within a grid cell, and Nr represents the set of road nodes within the cell. The term aij denotes the length of the accessible road between nodes i and j.

<!-- b001915 | furniture | pages [17] -->
m

<!-- b001916 | furniture | pages [17] -->
m

<!-- b001917 | furniture | pages [17] -->
m

<!-- b001918 | furniture | pages [17] -->
m

<!-- b001919 | furniture | pages [17] -->
m

<!-- b001920 | furniture | pages [17] -->
m

<!-- b001921 | furniture | pages [17] -->
m

<!-- b001922 | furniture | pages [17] -->
m

<!-- b001923 | furniture | pages [17] -->
m

<!-- b001924 | furniture | pages [17] -->
m

<!-- b001925 | furniture | pages [17] -->
m

<!-- b001926 | furniture | pages [17] -->
m

<!-- b001927 | furniture | pages [17] -->
m

<!-- b001928 | furniture | pages [17] -->
m

<!-- b001929 | furniture | pages [17] -->
m

<!-- b001930 | furniture | pages [17] -->
m

<!-- b001931 | furniture | pages [17] -->
m

<!-- b001932 | furniture | pages [17] -->
m

<!-- b001933 | furniture | pages [17] -->
m

<!-- b001934 | furniture | pages [17] -->
m

<!-- b001935 | furniture | pages [17] -->
m

<!-- b001936 | furniture | pages [17] -->
m

<!-- b001937 | furniture | pages [17] -->
m

<!-- b001938 | furniture | pages [17] -->
m

<!-- b001939 | furniture | pages [17] -->
m

<!-- b001940 | furniture | pages [17] -->
m

<!-- b001941 | furniture | pages [17] -->
m

<!-- b001942 | furniture | pages [17] -->
m

<!-- b001943 | furniture | pages [17] -->
m

<!-- b001944 | furniture | pages [17] -->
m

<!-- b001945 | furniture | pages [17] -->
m

<!-- b001946 | furniture | pages [17] -->
m

<!-- b001947 | furniture | pages [17] -->
m

<!-- b001948 | furniture | pages [17] -->
m

<!-- b001949 | furniture | pages [17] -->
m

<!-- b001950 | furniture | pages [17] -->
m

<!-- b001951 | furniture | pages [17] -->
m

<!-- b001952 | furniture | pages [17] -->
m

<!-- b001953 | furniture | pages [17] -->
m

<!-- b001954 | furniture | pages [17] -->
m

<!-- b001955 | furniture | pages [17] -->
m

<!-- b001956 | furniture | pages [17] -->
m

<!-- b001957 | furniture | pages [17] -->
m

<!-- b001958 | furniture | pages [17] -->
m

<!-- b001959 | furniture | pages [17] -->
m

<!-- b001960 | furniture | pages [17] -->
m

<!-- b001961 | furniture | pages [17] -->
m

<!-- b001962 | furniture | pages [17] -->
m

<!-- b001963 | furniture | pages [17] -->
m

<!-- b001964 | furniture | pages [17] -->
m

<!-- b001965 | furniture | pages [17] -->
m

<!-- b001966 | furniture | pages [17] -->
m

<!-- b001967 | furniture | pages [17] -->
m

<!-- b001968 | furniture | pages [17] -->
m

<!-- b001969 | furniture | pages [17] -->
m

<!-- b001970 | furniture | pages [17] -->
m

<!-- b001971 | furniture | pages [17] -->
m

<!-- b001972 | furniture | pages [17] -->
m

<!-- b001973 | furniture | pages [17] -->
m

<!-- b001974 | furniture | pages [17] -->
m

<!-- b001975 | furniture | pages [17] -->
m

<!-- b001976 | furniture | pages [17] -->
m

<!-- b001977 | furniture | pages [17] -->
m

<!-- b001978 | furniture | pages [17] -->
m

<!-- b001979 | furniture | pages [17] -->
m

<!-- b001980 | furniture | pages [17] -->
m

<!-- b001981 | furniture | pages [17] -->
m

<!-- b001982 | furniture | pages [17] -->
m

<!-- b001983 | furniture | pages [17] -->
m

<!-- b001984 | furniture | pages [17] -->
m

<!-- b001985 | furniture | pages [17] -->
m

<!-- b001986 | furniture | pages [17] -->
m

<!-- b001987 | furniture | pages [17] -->
m

<!-- b001988 | furniture | pages [17] -->
m

<!-- b001989 | furniture | pages [17] -->
m

<!-- b001990 | furniture | pages [17] -->
m

<!-- b001991 | furniture | pages [17] -->
m

<!-- b001992 | furniture | pages [17] -->
m

<!-- b001993 | furniture | pages [17] -->
m

<!-- b001994 | furniture | pages [17] -->
m

<!-- b001995 | furniture | pages [17] -->
m

<!-- b001996 | furniture | pages [17] -->
m

<!-- b001997 | furniture | pages [17] -->
m

<!-- b001998 | furniture | pages [17] -->
m

<!-- b001999 | furniture | pages [17] -->
m

<!-- b002000 | furniture | pages [17] -->
m

<!-- b002001 | furniture | pages [17] -->
m

<!-- b002002 | furniture | pages [17] -->
m

<!-- b002003 | furniture | pages [17] -->
m

<!-- b002004 | furniture | pages [17] -->
m

<!-- b002005 | furniture | pages [17] -->
m

<!-- b002006 | furniture | pages [17] -->
m

<!-- b002007 | furniture | pages [17] -->
m

<!-- b002008 | furniture | pages [17] -->
m

<!-- b002009 | furniture | pages [17] -->
m

<!-- b002010 | furniture | pages [17] -->
m

<!-- b002011 | furniture | pages [17] -->
m

<!-- b002012 | furniture | pages [17] -->
m

<!-- b002013 | furniture | pages [17] -->
m

<!-- b002014 | furniture | pages [17] -->
m

<!-- b002015 | furniture | pages [17] -->
m

<!-- b002016 | furniture | pages [17] -->
m

<!-- b002017 | furniture | pages [17] -->
m

<!-- b002018 | furniture | pages [17] -->
m

<!-- b002019 | furniture | pages [17] -->
m

<!-- b002020 | furniture | pages [17] -->
m

<!-- b002021 | furniture | pages [17] -->
m

<!-- b002022 | furniture | pages [17] -->
m

<!-- b002023 | furniture | pages [17] -->
m

<!-- b002024 | furniture | pages [17] -->
m

<!-- b002025 | furniture | pages [17] -->
m

<!-- b002026 | furniture | pages [17] -->
m

<!-- b002027 | furniture | pages [17] -->
m

<!-- b002028 | furniture | pages [17] -->
m

<!-- b002029 | furniture | pages [17] -->
m

<!-- b002030 | furniture | pages [17] -->
m

<!-- b002031 | furniture | pages [17] -->
m

<!-- b002032 | furniture | pages [17] -->
m

<!-- b002033 | furniture | pages [17] -->
m

<!-- b002034 | furniture | pages [17] -->
m

<!-- b002035 | furniture | pages [17] -->
m

<!-- b002036 | furniture | pages [17] -->
m

<!-- b002037 | furniture | pages [17] -->
m

<!-- b002038 | furniture | pages [17] -->
m

<!-- b002039 | furniture | pages [17] -->
m

<!-- b002040 | furniture | pages [17] -->
m

<!-- b002041 | furniture | pages [17] -->
m

<!-- b002042 | furniture | pages [17] -->
m

<!-- b002043 | furniture | pages [17] -->
m

<!-- b002044 | furniture | pages [17] -->
m

<!-- b002045 | furniture | pages [17] -->
m

<!-- b002046 | furniture | pages [17] -->
m

<!-- b002047 | furniture | pages [17] -->
m

<!-- b002048 | furniture | pages [17] -->
m

<!-- b002049 | furniture | pages [17] -->
m

<!-- b002050 | furniture | pages [17] -->
m

<!-- b002051 | furniture | pages [17] -->
m

<!-- b002052 | furniture | pages [17] -->
m

<!-- b002053 | furniture | pages [17] -->
m

<!-- b002054 | furniture | pages [17] -->
m

<!-- b002055 | furniture | pages [17] -->
m

<!-- b002056 | furniture | pages [17] -->
m

<!-- b002057 | furniture | pages [17] -->
m

<!-- b002058 | furniture | pages [17] -->
m

<!-- b002059 | furniture | pages [17] -->
m

<!-- b002060 | furniture | pages [17] -->
m

<!-- b002061 | furniture | pages [17] -->
m

<!-- b002062 | furniture | pages [17] -->
m

<!-- b002063 | furniture | pages [17] -->
m

<!-- b002064 | furniture | pages [17] -->
m

<!-- b002065 | furniture | pages [17] -->
m

<!-- b002066 | furniture | pages [17] -->
m

<!-- b002067 | furniture | pages [17] -->
m

<!-- b002068 | furniture | pages [17] -->
m

<!-- b002069 | furniture | pages [17] -->
m

<!-- b002070 | furniture | pages [17] -->
m

<!-- b002071 | furniture | pages [17] -->
m

<!-- b002072 | furniture | pages [17] -->
m

<!-- b002073 | furniture | pages [17] -->
m

<!-- b002074 | furniture | pages [17] -->
m

<!-- b002075 | furniture | pages [17] -->
m

<!-- b002076 | furniture | pages [17] -->
m

<!-- b002077 | furniture | pages [17] -->
m

<!-- b002078 | furniture | pages [17] -->
m

<!-- b002079 | furniture | pages [17] -->
m

<!-- b002080 | furniture | pages [17] -->
m

<!-- b002081 | furniture | pages [17] -->
m

<!-- b002082 | furniture | pages [17] -->
m

<!-- b002083 | furniture | pages [17] -->
m

<!-- b002084 | furniture | pages [17] -->
m

<!-- b002085 | furniture | pages [17] -->
m

<!-- b002086 | furniture | pages [17] -->
m

<!-- b002087 | furniture | pages [17] -->
m

<!-- b002088 | furniture | pages [17] -->
m

<!-- b002089 | furniture | pages [17] -->
m

<!-- b002090 | furniture | pages [17] -->
m

<!-- b002091 | furniture | pages [17] -->
m

<!-- b002092 | furniture | pages [17] -->
m

<!-- b002093 | furniture | pages [17] -->
m

<!-- b002094 | furniture | pages [17] -->
m

<!-- b002095 | furniture | pages [17] -->
m

<!-- b002096 | furniture | pages [17] -->
m

<!-- b002097 | furniture | pages [17] -->
m

<!-- b002098 | furniture | pages [17] -->
m

<!-- b002099 | furniture | pages [17] -->
m

<!-- b002100 | furniture | pages [17] -->
m

<!-- b002101 | furniture | pages [17] -->
m

<!-- b002102 | furniture | pages [17] -->
m

<!-- b002103 | furniture | pages [17] -->
m

<!-- b002104 | furniture | pages [17] -->
m

<!-- b002105 | furniture | pages [17] -->
m

<!-- b002106 | furniture | pages [17] -->
m

<!-- b002107 | furniture | pages [17] -->
m

<!-- b002108 | furniture | pages [17] -->
m

<!-- b002109 | furniture | pages [17] -->
m

<!-- b002110 | furniture | pages [17] -->
m

<!-- b002111 | furniture | pages [17] -->
m

<!-- b002112 | furniture | pages [17] -->
m

<!-- b002113 | furniture | pages [17] -->
m

<!-- b002114 | furniture | pages [17] -->
m

<!-- b002115 | furniture | pages [17] -->
m

<!-- b002116 | furniture | pages [17] -->
m

<!-- b002117 | furniture | pages [17] -->
m

<!-- b002118 | furniture | pages [17] -->
m

<!-- b002119 | furniture | pages [17] -->
m

<!-- b002120 | furniture | pages [17] -->
m

<!-- b002121 | furniture | pages [17] -->
m

<!-- b002122 | furniture | pages [17] -->
m

<!-- b002123 | furniture | pages [17] -->
m

<!-- b002124 | furniture | pages [17] -->
m

<!-- b002125 | furniture | pages [17] -->
m

<!-- b002126 | furniture | pages [17] -->
m

<!-- b002127 | furniture | pages [17] -->
m

<!-- b002128 | furniture | pages [17] -->
m

<!-- b002129 | furniture | pages [17] -->
m

<!-- b002130 | furniture | pages [17] -->
m

<!-- b002131 | furniture | pages [17] -->
m

<!-- b002132 | furniture | pages [17] -->
m

<!-- b002133 | furniture | pages [17] -->
m

<!-- b002134 | furniture | pages [17] -->
m

<!-- b002135 | furniture | pages [17] -->
m

<!-- b002136 | furniture | pages [17] -->
m

<!-- b002137 | furniture | pages [17] -->
m

<!-- b002138 | furniture | pages [17] -->
m

<!-- b002139 | furniture | pages [17] -->
m

<!-- b002140 | furniture | pages [17] -->
m

<!-- b002141 | furniture | pages [17] -->
m

<!-- b002142 | furniture | pages [17] -->
m

<!-- b002143 | furniture | pages [17] -->
m

<!-- b002144 | furniture | pages [17] -->
m

<!-- b002145 | furniture | pages [17] -->
m

<!-- b002146 | furniture | pages [17] -->
m

<!-- b002147 | furniture | pages [17] -->
m

<!-- b002148 | furniture | pages [17] -->
m

<!-- b002149 | furniture | pages [17] -->
m

<!-- b002150 | furniture | pages [17] -->
m

<!-- b002151 | furniture | pages [17] -->
m

<!-- b002152 | furniture | pages [17] -->
m

<!-- b002153 | furniture | pages [17] -->
m

<!-- b002154 | furniture | pages [17] -->
m

<!-- b002155 | furniture | pages [17] -->
m

<!-- b002156 | furniture | pages [17] -->
m

<!-- b002157 | furniture | pages [17] -->
m

<!-- b002158 | furniture | pages [17] -->
m

<!-- b002159 | furniture | pages [17] -->
m

<!-- b002160 | furniture | pages [17] -->
m

<!-- b002161 | furniture | pages [17] -->
m

<!-- b002162 | furniture | pages [17] -->
m

<!-- b002163 | furniture | pages [17] -->
m

<!-- b002164 | furniture | pages [17] -->
m

<!-- b002165 | furniture | pages [17] -->
m

<!-- b002166 | furniture | pages [17] -->
m

<!-- b002167 | furniture | pages [17] -->
m

<!-- b002168 | furniture | pages [17] -->
m

<!-- b002169 | furniture | pages [17] -->
m

<!-- b002170 | furniture | pages [17] -->
m

<!-- b002171 | furniture | pages [17] -->
m

<!-- b002172 | furniture | pages [17] -->
m

<!-- b002173 | furniture | pages [17] -->
m

<!-- b002174 | furniture | pages [17] -->
m

<!-- b002175 | furniture | pages [17] -->
m

<!-- b002176 | furniture | pages [17] -->
m

<!-- b002177 | furniture | pages [17] -->
m

<!-- b002178 | furniture | pages [17] -->
m

<!-- b002179 | furniture | pages [17] -->
m

<!-- b002180 | furniture | pages [17] -->
m

<!-- b002181 | furniture | pages [17] -->
m

<!-- b002182 | furniture | pages [17] -->
m

<!-- b002183 | furniture | pages [17] -->
m

<!-- b002184 | furniture | pages [17] -->
m

<!-- b002185 | furniture | pages [17] -->
m

<!-- b002186 | furniture | pages [17] -->
m

<!-- b002187 | furniture | pages [17] -->
m

<!-- b002188 | furniture | pages [17] -->
m

<!-- b002189 | furniture | pages [17] -->
m

<!-- b002190 | furniture | pages [17] -->
m

<!-- b002191 | furniture | pages [17] -->
m

<!-- b002192 | furniture | pages [17] -->
m

<!-- b002193 | furniture | pages [17] -->
m

<!-- b002194 | furniture | pages [17] -->
m

<!-- b002195 | furniture | pages [17] -->
m

<!-- b002196 | furniture | pages [17] -->
m

<!-- b002197 | furniture | pages [17] -->
m

<!-- b002198 | furniture | pages [17] -->
m

<!-- b002199 | furniture | pages [17] -->
m

<!-- b002200 | furniture | pages [17] -->
m

<!-- b002201 | furniture | pages [17] -->
m

<!-- b002202 | furniture | pages [17] -->
m

<!-- b002203 | furniture | pages [17] -->
m

<!-- b002204 | furniture | pages [17] -->
m

<!-- b002205 | furniture | pages [17] -->
m

<!-- b002206 | furniture | pages [17] -->
m

<!-- b002207 | furniture | pages [17] -->
m

<!-- b002208 | furniture | pages [17] -->
m

<!-- b002209 | furniture | pages [17] -->
m

<!-- b002210 | furniture | pages [17] -->
m

<!-- b002211 | furniture | pages [17] -->
m

<!-- b002212 | furniture | pages [17] -->
m

<!-- b002213 | furniture | pages [17] -->
m

<!-- b002214 | furniture | pages [17] -->
m

<!-- b002215 | furniture | pages [17] -->
m

<!-- b002216 | furniture | pages [17] -->
m

<!-- b002217 | furniture | pages [17] -->
m

<!-- b002218 | furniture | pages [17] -->
m

<!-- b002219 | furniture | pages [17] -->
m

<!-- b002220 | furniture | pages [17] -->
m

<!-- b002221 | furniture | pages [17] -->
m

<!-- b002222 | furniture | pages [17] -->
m

<!-- b002223 | furniture | pages [17] -->
m

<!-- b002224 | furniture | pages [17] -->
m

<!-- b002225 | furniture | pages [17] -->
m

<!-- b002226 | furniture | pages [17] -->
m

<!-- b002227 | furniture | pages [17] -->
m

<!-- b002228 | furniture | pages [17] -->
m

<!-- b002229 | furniture | pages [17] -->
m

<!-- b002230 | furniture | pages [17] -->
m

<!-- b002231 | furniture | pages [17] -->
m

<!-- b002232 | furniture | pages [17] -->
m

<!-- b002233 | furniture | pages [17] -->
m

<!-- b002234 | furniture | pages [17] -->
m

<!-- b002235 | furniture | pages [17] -->
m

<!-- b002236 | furniture | pages [17] -->
m

<!-- b002237 | furniture | pages [17] -->
m

<!-- b002238 | furniture | pages [17] -->
m

<!-- b002239 | furniture | pages [18] -->
Team # 2519935

<!-- b002240 | furniture | pages [18] -->
Page 18 of 25

<!-- b002242 | prose | pages [18] -->
 Step 3: Fitting and Bus Station Density Prediction

<!-- b002243 | prose | pages [18] -->
Various methods, including linear, quadratic, cubic, and exponential functions, are used to fit the relationship between road network density and bus station density. The best-fitting method is selected, and the bus station density before the construction of the metro is predicted based on the current road network density.

<!-- b002244 | prose | pages [18] -->
 Step 4: Metro Impact Analysis

<!-- b002245 | prose | pages [18] -->
For a more precise analysis of the metro’s impact on public transportation, the map is further refined into a 20×20 grid. The difference between the actual bus station density and the predicted bus station density provides a measure of the impact of metro construction on bus stations, denoted as ∆ρbus:

<!-- b002246 | prose | pages [18] -->
∆ρbus = ρbus −ˆρbus. (16)

<!-- b002247 | heading | pages [18] -->
7.3 Model Solution and Results

<!-- b002248 | prose | pages [18] -->
Despite Baltimore being one of the United States’ primary port cities, existing metro lines, as reported in [10], fail to meet the daily transportation needs of its residents. A study evaluating Baltimore’s current economic condition proposed four additional metro lines. From this, we selected one line as a representative “transportation project most likely to improve residents’ quality of life” for further analysis. Additionally, we proposed the inclusion of new metro stations to accommodate the travel demands of a broader group of stakeholders. The existing metro routes and the line under analysis, marked in orange, are shown below.

<!-- b002249 | caption | pages [18] -->
Figure 18: Subway Route

<!-- b002250 | prose | pages [18] -->
The proposed line, as per the original draft, does not connect to the existing two lines, pre- venting seamless transfers. To resolve this, we added new stations, such as “Upton” connecting to the Green Line and “Cultural Center” connecting to the Navy Line, thus enabling passengers to transfer between lines.

<!-- b002251 | prose | pages [18] -->
关注数学模型

<!-- b002252 | furniture | pages [18] -->
2

<!-- b002253 | furniture | pages [18] -->
MATHmodels

<!-- b002254 | furniture | pages [18] -->
获取更多资讯

<!-- b002255 | furniture | pages [19] -->
Team # 2519935

<!-- b002256 | furniture | pages [19] -->
Page 19 of 25

<!-- b002257 | heading | pages [19] -->
7.3.1 Question a: The Benefits to Residents

<!-- b002258 | prose | pages [19] -->
By applying the improved Dijkstra algorithm, we calculate the time savings for residents in various locations when traveling to the city center (Charles Center, 39.2895, -76.6163) after the project’s implementation, in addition to the time taken to reach the city center post- implementation.

<!-- b002259 | prose | pages [19] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b002260 | caption | pages [19] -->
Figure 19: The Impact of the Project on Residents

<!-- b002261 | prose | pages [19] -->
From (a), areas shaded in yellow represent the largest time savings, indicating that the project significantly reduces travel time for residents in suburban areas. From (b), it is evident that residents along the new metro line can reach the city center faster. The metro system also offers more travel options for residents, reducing congestion risks on the roads.

<!-- b002262 | prose | pages [19] -->
- Safety Analysis: Compared to surface transportation, metro operations are unaffected by road traffic, significantly reducing the risk of accidents caused by traffic congestion. Running on independent tracks, the metro system greatly minimizes the risk of collisions with other vehicles or pedestrians and avoids intersections, further lowering the risk of accidents.

<!-- b002263 | heading | pages [19] -->
7.3.2 Question b: The Impact on Other Stakeholders

<!-- b002264 | prose | pages [19] -->
Next, we assess the project’s impact on other stakeholders. The following image illustrates the stations along the proposed line and the time required to reach the airport from each station.

<!-- b002265 | caption | pages [19] -->
Figure 20: Our Project

<!-- b002266 | furniture | pages [20] -->
Team # 2519935

<!-- b002267 | furniture | pages [20] -->
Page 20 of 25

<!-- b002268 | prose | pages [20] -->
• Flight Passengers: For passengers traveling to the airport, the metro line allows transfers at the Cultural Center station to the Navy Line, providing access to BWI Airport. The travel time from various stations to the airport is shown in Figure 20.

<!-- b002269 | prose | pages [20] -->
• Tourists: Our project passes several major tourist attractions such as “Clifton Park” and “Herring Run Park,” providing tourists with an easy access route from the airport to these locations.

<!-- b002270 | prose | pages [20] -->
• Business Owners: For businesses such as Walmart, our project will bring increased foot traffic, leading to higher revenues. Additionally, the project makes it easier for people to access the city center, indirectly benefiting local businesses.

<!-- b002271 | prose | pages [20] -->
• Commuters: As seen in Figure 20, the project also connects to Baltimore’s Penn Station, allowing commuters to travel to their workplaces by transferring from the metro to the train station.

<!-- b002272 | heading | pages [20] -->
7.3.3 Question c: Disruption to Other Transportation Needs

<!-- b002273 | prose | pages [20] -->
Based on the constructed DDF model, this section analyzes the impact of the two existing subway lines on bus routes, which in turn helps to assess the effect of the newly constructed subway on bus stations. First, a 6×6 network map is constructed, displaying the road density of Baltimore (a) and the bus stops density (b) as shown in the figure below. In the maps, the closer the color is to yellow, the higher the density; conversely, the closer the color is to blue, the lower the density.

<!-- b002274 | caption | pages [20] -->
Figure 21: Bus Stops and Road Network Density

<!-- b002275 | caption | pages [20] -->
Figure 21 shows that the density at the center of both maps is higher than that of the

<!-- b002276 | prose | pages [20] -->
surrounding grids. It is also evident that grids with higher road density tend to have higher bus station density, and vice versa. Therefore, a preliminary correlation between traffic station density and road network density can be inferred.

<!-- b002277 | prose | pages [20] -->
Linear and various nonlinear fitting methods are applied to analyze this relationship, with the fitting results presented in the following figure.

<!-- b002278 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型

<!-- b002279 | furniture | pages [20] -->
2

<!-- b002280 | furniture | pages [20] -->
MATHmodels

<!-- b002281 | furniture | pages [20] -->
获取更多资讯

<!-- b002282 | furniture | pages [21] -->
Team # 2519935

<!-- b002283 | furniture | pages [21] -->
Page 21 of 25

<!-- b002285 | caption | pages [21] -->
Figure 22: Multiple Fitting Results

<!-- b002286 | prose | pages [21] -->
微信号：MATHmodels The quadratic function provides the best fit, and the relationship between road density (y) and bus station density (x) is expressed as:

<!-- b002287 | prose | pages [21] -->
y = 16241x2 −15507x + 4751. (17)

<!-- b002288 | prose | pages [21] -->
Using this fitted relationship, we estimate bus station density, and by subtracting the esti- mated density from the actual density, we obtain the impact of the subway on bus stations, as illustrated in the figure below.

<!-- b002289 | caption | pages [21] -->
Figure 23: The Impact of Subway on Bus Stations

<!-- b002290 | prose | pages [21] -->
As shown in the figure, areas along the two existing subway lines in Baltimore exhibit a larger difference, indicating an increase in bus stations along the subway corridors after its construction. This suggests a higher demand for bus services. The likely cause is that the subway construction has increased the demand for transfers between subway and bus services, influencing the establishment of bus stations. Therefore, it can be inferred that the construction of our new subway line will similarly impact bus demand along the corridor, leading to an increase in the number of bus stations.

<!-- b002291 | furniture | pages [22] -->
Team # 2519935

<!-- b002292 | furniture | pages [22] -->
Page 22 of 25

<!-- b002293 | heading | pages [22] -->
8 Sensitivity Analysis

<!-- b002294 | prose | pages [22] -->
We conducted a sensitivity analysis to assess the robustness of our results. In evaluating the positive impact of the subway on various sections, we examined the outcomes across multiple segmentation levels, ranging from a side length of 2,400 meters to 120 meters. The results are presented in the following figure.

<!-- b002295 | caption | pages [22] -->
Figure 24: Sensitivity Analysis

<!-- b002296 | prose | pages [22] -->
The analysis reveals that the positive impact of the subway on different sections is robust. As the accuracy of grid segmentation increases, the number of bus stops per grid decreases, leading to a more pronounced positive impact of the subway on the respective sections.

<!-- b002297 | heading | pages [22] -->
9 Model Evaluation and Further Discussion

<!-- b002298 | heading | pages [22] -->
9.1 Strengths

<!-- b002299 | prose | pages [22] -->
• Impact Assessment Model: Leverages real-world AADT and AAWDT data to quantify m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the impact of the bridge collapse, effectively assessing the consequences for different m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m stakeholder groups, including both commuters and non-commuters. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002300 | prose | pages [22] -->
• Regional Impact Consideration: Uses closeness centrality to assess not only the im- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m mediate effect in Baltimore but also the wider regional transportation network, capturing m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002301 | prose | pages [22] -->
how interconnected areas may be impacted.

<!-- b002302 | prose | pages [22] -->
• Three-layer Bus Network Model (TBN): Enriches the model by considering points of interest (POI) in bus routes, providing a more realistic representation of commuter needs and prioritizing high-demand areas.

<!-- b002303 | prose | pages [22] -->
• Weighted K-Shell Decomposition: Uses a structured, tiered approach to classify bus stations based on connectivity, helping to identify important nodes in the network and improve overall transit access.

<!-- b002304 | prose | pages [22] -->
关注数学模型

<!-- b002305 | furniture | pages [22] -->
2

<!-- b002306 | furniture | pages [22] -->
MATHmodels

<!-- b002307 | furniture | pages [22] -->
获取更多资讯

<!-- b002308 | furniture | pages [23] -->
Team # 2519935

<!-- b002309 | furniture | pages [23] -->
Page 23 of 25

<!-- b002310 | heading | pages [23] -->
9.2 Weaknesses

<!-- b002311 | prose | pages [23] -->
• Simplified Assumptions in the Impact Assessment Model: Assumes constant growth in AADT and AAWDT, which may not capture future trends or unexpected events affecting traffic.

<!-- b002312 | prose | pages [23] -->
• Limited Scope of Impact Assessment Model: Primarily focuses on highways, missing the potential impacts on local roads and alternative transportation modes, which may also be crucial to understanding the broader transportation network.

<!-- b002313 | prose | pages [23] -->
• Subjectivity in Tier Definition in TBN: The division between core, bridge, and pe- ripheral layers of the bus network may be based on somewhat subjective criteria. More objective, data-driven methods could improve accuracy.

<!-- b002314 | prose | pages [23] -->
微信公众号：数学模型 The strengths and weaknesses of our model can be visually presented and is shown below:

<!-- b002315 | prose | pages [23] -->
微信号：MATHmodels

<!-- b002316 | caption | pages [23] -->
Figure 25: Strengths and Weaknesses of Our Model

<!-- b002317 | heading | pages [23] -->
9.3 Further Discussion

<!-- b002318 | prose | pages [23] -->
Although the models provide a solid foundation for analyzing Baltimore’s transportation network, there are several areas for future improvement. Incorporating dynamic traffic patterns using real-time data and predictive algorithms would allow the models to better reflect changing traffic conditions. Expanding the scope to include multi-modal transportation options, such as cycling, walking, and ride-sharing, would offer a more comprehensive view of the transportation system. Additionally, validating the models with real-world data or through simulations would help ensure their practicality and reliability.

<!-- b002319 | prose | pages [23] -->
Furthermore, integrating socioeconomic factors into the models would enable a more eq- uitable approach to transportation planning, ensuring that the needs of all communities are addressed. Conducting detailed cost-benefit analyses would provide decision-makers with the necessary tools to prioritize projects and allocate resources efficiently. These improvements will make the models more accurate, adaptable, and applicable to a wider range of real-world transportation scenarios.

<!-- b002320 | furniture | pages [24] -->
Page 24 of 25

<!-- b002321 | furniture | pages [24] -->
Team # 2519935

<!-- b002322 | heading | pages [24] -->
10 Memorandum

<!-- b002323 | prose | pages [24] -->
Hamilton To: Baltimore Mayor

<!-- b002324 | prose | pages [24] -->
From: Team #2519935

<!-- b002325 | prose | pages [24] -->
Date: Jan 28, 2025

<!-- b002326 | prose | pages [24] -->
Subject: Two Projects to Improve the Lives of Baltimore Residents

<!-- b002327 | prose | pages [24] -->
Dear sir or madam:

<!-- b002328 | prose | pages [24] -->
We have recently conducted an in-depth exploration and study of the transportation system in Baltimore. With great enthusiasm, we would like to present two transportation project proposals aimed at enhancing the efficiency of mission-oriented travel in the city: the introduction of new bus routes and the creation of a new subway line. We understand that a robust transportation system is the foundation of urban development, and we aim to contribute thoughtfully to Baltimore's future transportation planning by weighing the advantages and challenges of these proposed projects.

<!-- b002329 | prose | pages [24] -->
Project I. Bus Route Optimization

<!-- b002330 | prose | pages [24] -->
Through gathering data on Baltimore's bus stations and referencing authoritative literature, we have constructed a three-tier bus network model. This model divides the city's bus stops into three layers: the Core Layer, Bridge Layer, and Outer Layer. Each of these layers contains several bus routes; However, we observed that the connections between the layers are not particularly strong. To address this, we propose adding two new bus routes that would link the Core and Bridge Layers. These additional routes would enhance the connectivity of the city's transportation network, allowing residents to more easily reach key destinations such as the city center, train stations, and airports. Not only would this alleviate pressure on the existing rail system, but it would also meet the growing travel needs of Baltimore's residents while supporting the development of surrounding areas. However, we acknowledge that the addition of these bus routes will lead to higher operational and maintenance costs, which could place some strain on the city's budget.

<!-- b002331 | prose | pages [24] -->
Project II. New Subway Line

<!-- b002332 | prose | pages [24] -->
We also propose the addition of a new subway line based on a DDF model we have designed. Our analysis indicates that this subway line would significantly reduce travel time to the airport compared to traditional modes of transportation. Furthermore, it is projected to increase the density of existing bus stops, facilitating smoother transfers between different modes of transportation. While the new subway line holds great potential for improving travel efficiency, we recognize that its construction timeline would be lengthy, and certain sections of the route would pass through the city center, potentially affecting short-term mobility for residents.

<!-- b002333 | prose | pages [24] -->
As university students, we understand that these projects are only preliminary ideas and that further research and feasibility studies will be necessary for implementation. Nevertheless, we sincerely hope that you will consider our proposals and that they can be incorporated into the future urban planning of Baltimore. Thank you for your time and consideration.

<!-- b002334 | prose | pages [24] -->
Yours Sincerely,

<!-- b002335 | furniture | pages [24] -->
Team #2519935

<!-- b002336 | prose | pages [24] -->
关注数学模型

<!-- b002337 | furniture | pages [24] -->
获取更多资讯

<!-- b002338 | furniture | pages [25] -->
Team # 2519935

<!-- b002339 | furniture | pages [25] -->
Page 25 of 25

<!-- b002340 | heading | pages [25] -->
References

<!-- b002341 | references | pages [25] -->
[1] TRIP. "Baltimore Bridge Collision Highlights Importance of Infrastructure Network."

<!-- b002342 | references | pages [25] -->
Rock Products, 2024, 127(6): 48-49.

<!-- b002343 | references | pages [25] -->
[2] Fu, M., Li, J., Zhang, C., et al. "Generating Navigation Electronic Map Road Network

<!-- b002344 | references | pages [25] -->
Using MapInfo Data." J. Computer-Aided Des. & Comput. Graph., 2004, (10): 1463-1465.

<!-- b002345 | references | pages [25] -->
[3] Li, Q., Zheng, N., Xu, J., et al. "A Hierarchical Path Planning Algorithm Based on

<!-- b002346 | references | pages [25] -->
Hierarchical Topology Structure of Road Network." J. Image Graph., 2007, (07): 1280-

<!-- b002347 | references | pages [25] -->
1285.

<!-- b002348 | references | pages [25] -->
微信公众号：数学模型

<!-- b002349 | references | pages [25] -->
[4] Fu, M., Li, J., Deng, Z. "A Novel Path Planning Algorithm Based on Hierarchical Road

<!-- b002350 | references | pages [25] -->
Network." J. Computer-Aided Des. & Comput. Graph., 2005, (04): 719-722.

<!-- b002351 | references | pages [25] -->
[5] Kargon, J. "One City’s ’Urban Cosmography’." Planning Perspect., 2014, (02-06): 1-10.

<!-- b002352 | references | pages [25] -->
[6] Simpson, D. B., Burnett, D. "Commuters Versus Residents." J. Coll. Stud. Retent.: Res.

<!-- b002353 | references | pages [25] -->
Theory & Pract., 2017, (05-10): 1-10.

<!-- b002354 | references | pages [25] -->
[7] Goodrich, C., Segal, H. H. "Baltimore’s Aid to Railroads: A Study in the Municipal

<!-- b002355 | references | pages [25] -->
Planning of Internal Improvements." J. Econ. Hist., 2016, (08-04): 1-10.

<!-- b002356 | references | pages [25] -->
微信号：MATHmodels

<!-- b002357 | references | pages [25] -->
[8] Dorogovtsev, S. N., Goltsev, A. V., Mendes, J. F. F. "k-Core Organization of Complex

<!-- b002358 | references | pages [25] -->
Networks." Phys. Rev. Lett., 2006, 96(4).

<!-- b002359 | references | pages [25] -->
[9] Xie, F., Wei, M., Huang, J., et al. "Identification and Optimization of Important Bus Routes

<!-- b002360 | references | pages [25] -->
Based on High-Order Network Model." J. Beijing Jiaotong Univ.

<!-- b002361 | references | pages [25] -->
[10] Fei, Y., Wen, X. L., Liu, Y., et al. "Research on Pedestrian Network Planning Method for

<!-- b002362 | references | pages [25] -->
Urban Central Area Based on POI Data: A Case Study of Xinjiekou Area in Nanjing." J.

<!-- b002363 | references | pages [25] -->
Traffic Eng., 2022, 22(6): 73-77+84.

<!-- b002364 | references | pages [25] -->
[11] VERMA, T., ARAÚJO, N. A. M., et al. "Revealing the Structure of the World Airline

<!-- b002365 | references | pages [25] -->
Network." Sci. Rep., 2014, 4(1): 1-6.

<!-- b002366 | references | pages [25] -->
[12] "Reconnecting Communities in West Baltimore." Streets of Baltimore, 2024 Jan 15. Avail-

<!-- b002367 | references | pages [25] -->
able: https://streetsofbaltimore.com/reconnecting-communities-in-west-baltimore

<!-- b002368 | references | pages [25] -->
m

<!-- b002369 | references | pages [25] -->
m

<!-- b002370 | references | pages [25] -->
m

<!-- b002371 | references | pages [25] -->
m

<!-- b002372 | references | pages [25] -->
m

<!-- b002373 | references | pages [25] -->
m

<!-- b002374 | references | pages [25] -->
m

<!-- b002375 | references | pages [25] -->
m

<!-- b002376 | references | pages [25] -->
m

<!-- b002377 | references | pages [25] -->
m

<!-- b002378 | references | pages [25] -->
m

<!-- b002379 | references | pages [25] -->
m

<!-- b002380 | references | pages [25] -->
m

<!-- b002381 | references | pages [25] -->
m

<!-- b002382 | references | pages [25] -->
m

<!-- b002383 | references | pages [25] -->
m

<!-- b002384 | references | pages [25] -->
m

<!-- b002385 | references | pages [25] -->
m

<!-- b002386 | references | pages [25] -->
m

<!-- b002387 | references | pages [25] -->
m

<!-- b002388 | references | pages [25] -->
m

<!-- b002389 | references | pages [25] -->
m

<!-- b002390 | references | pages [25] -->
m

<!-- b002391 | references | pages [25] -->
m

<!-- b002392 | references | pages [25] -->
m

<!-- b002393 | references | pages [25] -->
m

<!-- b002394 | references | pages [25] -->
m

<!-- b002395 | references | pages [25] -->
m

<!-- b002396 | references | pages [25] -->
m

<!-- b002397 | references | pages [25] -->
m

<!-- b002398 | references | pages [25] -->
m

<!-- b002399 | references | pages [25] -->
m

<!-- b002400 | references | pages [25] -->
m

<!-- b002401 | references | pages [25] -->
m

<!-- b002402 | references | pages [25] -->
m

<!-- b002403 | references | pages [25] -->
m

<!-- b002404 | references | pages [25] -->
m

<!-- b002405 | references | pages [25] -->
m

<!-- b002406 | references | pages [25] -->
m

<!-- b002407 | references | pages [25] -->
m

<!-- b002408 | references | pages [25] -->
m

<!-- b002409 | references | pages [25] -->
m

<!-- b002410 | references | pages [25] -->
m

<!-- b002411 | references | pages [25] -->
m

<!-- b002412 | references | pages [25] -->
m

<!-- b002413 | references | pages [25] -->
m

<!-- b002414 | references | pages [25] -->
m

<!-- b002415 | references | pages [25] -->
m

<!-- b002416 | references | pages [25] -->
m

<!-- b002417 | references | pages [25] -->
m

<!-- b002418 | references | pages [25] -->
m

<!-- b002419 | references | pages [25] -->
m

<!-- b002420 | references | pages [25] -->
m

<!-- b002421 | references | pages [25] -->
m

<!-- b002422 | references | pages [25] -->
m

<!-- b002423 | references | pages [25] -->
m

<!-- b002424 | references | pages [25] -->
m

<!-- b002425 | references | pages [25] -->
m

<!-- b002426 | references | pages [25] -->
m

<!-- b002427 | references | pages [25] -->
m

<!-- b002428 | references | pages [25] -->
m

<!-- b002429 | references | pages [25] -->
m

<!-- b002430 | references | pages [25] -->
m

<!-- b002431 | references | pages [25] -->
m

<!-- b002432 | references | pages [25] -->
m

<!-- b002433 | references | pages [25] -->
m

<!-- b002434 | references | pages [25] -->
m

<!-- b002435 | references | pages [25] -->
m

<!-- b002436 | references | pages [25] -->
m

<!-- b002437 | references | pages [25] -->
m

<!-- b002438 | references | pages [25] -->
m

<!-- b002439 | references | pages [25] -->
m

<!-- b002440 | references | pages [25] -->
m

<!-- b002441 | references | pages [25] -->
m

<!-- b002442 | references | pages [25] -->
m

<!-- b002443 | references | pages [25] -->
m

<!-- b002444 | references | pages [25] -->
m

<!-- b002445 | references | pages [25] -->
m

<!-- b002446 | references | pages [25] -->
m

<!-- b002447 | references | pages [25] -->
m

<!-- b002448 | references | pages [25] -->
m

<!-- b002449 | references | pages [25] -->
m

<!-- b002450 | references | pages [25] -->
m

<!-- b002451 | references | pages [25] -->
m

<!-- b002452 | references | pages [25] -->
m

<!-- b002453 | references | pages [25] -->
m

<!-- b002454 | references | pages [25] -->
m

<!-- b002455 | references | pages [25] -->
m

<!-- b002456 | references | pages [25] -->
m

<!-- b002457 | references | pages [25] -->
m

<!-- b002458 | references | pages [25] -->
m

<!-- b002459 | references | pages [25] -->
m

<!-- b002460 | references | pages [25] -->
m

<!-- b002461 | references | pages [25] -->
m

<!-- b002462 | references | pages [25] -->
m

<!-- b002463 | references | pages [25] -->
m

<!-- b002464 | references | pages [25] -->
m

<!-- b002465 | references | pages [25] -->
m

<!-- b002466 | references | pages [25] -->
m

<!-- b002467 | references | pages [25] -->
m

<!-- b002468 | references | pages [25] -->
m

<!-- b002469 | references | pages [25] -->
m

<!-- b002470 | references | pages [25] -->
m

<!-- b002471 | references | pages [25] -->
m

<!-- b002472 | references | pages [25] -->
m

<!-- b002473 | references | pages [25] -->
m

<!-- b002474 | references | pages [25] -->
m

<!-- b002475 | references | pages [25] -->
m

<!-- b002476 | references | pages [25] -->
m

<!-- b002477 | references | pages [25] -->
m

<!-- b002478 | references | pages [25] -->
m

<!-- b002479 | references | pages [25] -->
m

<!-- b002480 | references | pages [25] -->
m

<!-- b002481 | references | pages [25] -->
m

<!-- b002482 | references | pages [25] -->
m

<!-- b002483 | references | pages [25] -->
m

<!-- b002484 | references | pages [25] -->
m

<!-- b002485 | references | pages [25] -->
m

<!-- b002486 | references | pages [25] -->
m

<!-- b002487 | references | pages [25] -->
m

<!-- b002488 | references | pages [25] -->
m

<!-- b002489 | references | pages [25] -->
m

<!-- b002490 | references | pages [25] -->
m

<!-- b002491 | references | pages [25] -->
m

<!-- b002492 | references | pages [25] -->
m

<!-- b002493 | references | pages [25] -->
m

<!-- b002494 | references | pages [25] -->
m

<!-- b002495 | references | pages [25] -->
m

<!-- b002496 | references | pages [25] -->
m

<!-- b002497 | references | pages [25] -->
m

<!-- b002498 | references | pages [25] -->
m

<!-- b002499 | references | pages [25] -->
m

<!-- b002500 | references | pages [25] -->
m

<!-- b002501 | references | pages [25] -->
m

<!-- b002502 | references | pages [25] -->
m

<!-- b002503 | references | pages [25] -->
m

<!-- b002504 | references | pages [25] -->
m

<!-- b002505 | references | pages [25] -->
m

<!-- b002506 | references | pages [25] -->
m

<!-- b002507 | references | pages [25] -->
m

<!-- b002508 | references | pages [25] -->
m

<!-- b002509 | references | pages [25] -->
m

<!-- b002510 | references | pages [25] -->
m

<!-- b002511 | references | pages [25] -->
m

<!-- b002512 | references | pages [25] -->
m

<!-- b002513 | references | pages [25] -->
m

<!-- b002514 | references | pages [25] -->
m

<!-- b002515 | references | pages [25] -->
m

<!-- b002516 | references | pages [25] -->
m

<!-- b002517 | references | pages [25] -->
m

<!-- b002518 | references | pages [25] -->
m

<!-- b002519 | references | pages [25] -->
m

<!-- b002520 | references | pages [25] -->
m

<!-- b002521 | references | pages [25] -->
m

<!-- b002522 | references | pages [25] -->
m

<!-- b002523 | references | pages [25] -->
m

<!-- b002524 | references | pages [25] -->
m

<!-- b002525 | references | pages [25] -->
m

<!-- b002526 | references | pages [25] -->
m

<!-- b002527 | references | pages [25] -->
m

<!-- b002528 | references | pages [25] -->
m

<!-- b002529 | references | pages [25] -->
m

<!-- b002530 | references | pages [25] -->
m

<!-- b002531 | references | pages [25] -->
m

<!-- b002532 | references | pages [25] -->
m

<!-- b002533 | references | pages [25] -->
m

<!-- b002534 | references | pages [25] -->
m

<!-- b002535 | references | pages [25] -->
m

<!-- b002536 | references | pages [25] -->
m

<!-- b002537 | references | pages [25] -->
m

<!-- b002538 | references | pages [25] -->
m

<!-- b002539 | references | pages [25] -->
m

<!-- b002540 | references | pages [25] -->
m

<!-- b002541 | references | pages [25] -->
m

<!-- b002542 | references | pages [25] -->
m

<!-- b002543 | references | pages [25] -->
m

<!-- b002544 | references | pages [25] -->
m

<!-- b002545 | references | pages [25] -->
m

<!-- b002546 | references | pages [25] -->
m

<!-- b002547 | references | pages [25] -->
m

<!-- b002548 | references | pages [25] -->
m

<!-- b002549 | references | pages [25] -->
m

<!-- b002550 | references | pages [25] -->
m

<!-- b002551 | references | pages [25] -->
m

<!-- b002552 | references | pages [25] -->
m

<!-- b002553 | references | pages [25] -->
m

<!-- b002554 | references | pages [25] -->
m

<!-- b002555 | references | pages [25] -->
m

<!-- b002556 | references | pages [25] -->
m

<!-- b002557 | references | pages [25] -->
m

<!-- b002558 | references | pages [25] -->
m

<!-- b002559 | references | pages [25] -->
m

<!-- b002560 | references | pages [25] -->
m

<!-- b002561 | references | pages [25] -->
m

<!-- b002562 | references | pages [25] -->
m

<!-- b002563 | references | pages [25] -->
m

<!-- b002564 | references | pages [25] -->
m

<!-- b002565 | references | pages [25] -->
m

<!-- b002566 | references | pages [25] -->
m

<!-- b002567 | references | pages [25] -->
m

<!-- b002568 | references | pages [25] -->
m

<!-- b002569 | references | pages [25] -->
m

<!-- b002570 | references | pages [25] -->
m

<!-- b002571 | references | pages [25] -->
m

<!-- b002572 | references | pages [25] -->
m

<!-- b002573 | references | pages [25] -->
m

<!-- b002574 | references | pages [25] -->
m

<!-- b002575 | references | pages [25] -->
m

<!-- b002576 | references | pages [25] -->
m

<!-- b002577 | references | pages [25] -->
m

<!-- b002578 | references | pages [25] -->
m

<!-- b002579 | references | pages [25] -->
m

<!-- b002580 | references | pages [25] -->
m

<!-- b002581 | references | pages [25] -->
m

<!-- b002582 | references | pages [25] -->
m

<!-- b002583 | references | pages [25] -->
m

<!-- b002584 | references | pages [25] -->
m

<!-- b002585 | references | pages [25] -->
m

<!-- b002586 | references | pages [25] -->
m

<!-- b002587 | references | pages [25] -->
m

<!-- b002588 | references | pages [25] -->
m

<!-- b002589 | references | pages [25] -->
m

<!-- b002590 | references | pages [25] -->
m

<!-- b002591 | references | pages [25] -->
m

<!-- b002592 | references | pages [25] -->
m

<!-- b002593 | references | pages [25] -->
m

<!-- b002594 | references | pages [25] -->
m

<!-- b002595 | references | pages [25] -->
m

<!-- b002596 | references | pages [25] -->
m

<!-- b002597 | references | pages [25] -->
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

<!-- b002613 | furniture | pages [25] -->
m

<!-- b002614 | furniture | pages [25] -->
m

<!-- b002615 | furniture | pages [25] -->
m

<!-- b002616 | furniture | pages [25] -->
m

<!-- b002617 | furniture | pages [25] -->
m

<!-- b002618 | furniture | pages [25] -->
m

<!-- b002619 | furniture | pages [25] -->
m

<!-- b002620 | furniture | pages [25] -->
m

<!-- b002621 | furniture | pages [25] -->
m

<!-- b002622 | furniture | pages [25] -->
m

<!-- b002623 | furniture | pages [25] -->
m

<!-- b002624 | furniture | pages [25] -->
m

<!-- b002625 | furniture | pages [25] -->
m

<!-- b002626 | furniture | pages [25] -->
m

<!-- b002627 | furniture | pages [25] -->
m

<!-- b002628 | furniture | pages [25] -->
m

<!-- b002629 | furniture | pages [25] -->
m

<!-- b002630 | furniture | pages [25] -->
m

<!-- b002631 | furniture | pages [25] -->
m

<!-- b002632 | furniture | pages [25] -->
m

<!-- b002633 | furniture | pages [25] -->
m

<!-- b002634 | furniture | pages [25] -->
m

<!-- b002635 | furniture | pages [25] -->
m

<!-- b002636 | furniture | pages [25] -->
m

<!-- b002637 | furniture | pages [25] -->
m

<!-- b002638 | furniture | pages [25] -->
m

<!-- b002639 | furniture | pages [25] -->
m

<!-- b002640 | furniture | pages [25] -->
m

<!-- b002641 | furniture | pages [25] -->
m

<!-- b002642 | furniture | pages [25] -->
m

<!-- b002643 | furniture | pages [25] -->
m

<!-- b002644 | furniture | pages [25] -->
m

<!-- b002645 | furniture | pages [25] -->
m

<!-- b002646 | furniture | pages [25] -->
m

<!-- b002647 | furniture | pages [25] -->
m

<!-- b002648 | furniture | pages [25] -->
m

<!-- b002649 | furniture | pages [25] -->
m

<!-- b002650 | furniture | pages [25] -->
m

<!-- b002651 | furniture | pages [25] -->
m

<!-- b002652 | furniture | pages [25] -->
m

<!-- b002653 | furniture | pages [25] -->
m

<!-- b002654 | furniture | pages [25] -->
m

<!-- b002655 | furniture | pages [25] -->
m

<!-- b002656 | furniture | pages [25] -->
m

<!-- b002657 | furniture | pages [25] -->
m

<!-- b002658 | furniture | pages [25] -->
m

<!-- b002659 | furniture | pages [25] -->
m

<!-- b002660 | furniture | pages [25] -->
m

<!-- b002661 | furniture | pages [25] -->
m

<!-- b002662 | furniture | pages [25] -->
m

<!-- b002663 | furniture | pages [25] -->
m

<!-- b002664 | furniture | pages [25] -->
m

<!-- b002665 | furniture | pages [25] -->
m

<!-- b002666 | furniture | pages [25] -->
m

<!-- b002667 | furniture | pages [25] -->
m

<!-- b002668 | furniture | pages [25] -->
m

<!-- b002669 | furniture | pages [25] -->
m

<!-- b002670 | furniture | pages [25] -->
m

<!-- b002671 | furniture | pages [25] -->
m

<!-- b002672 | furniture | pages [25] -->
m

<!-- b002673 | furniture | pages [25] -->
m

<!-- b002674 | furniture | pages [25] -->
m

<!-- b002675 | furniture | pages [25] -->
m

<!-- b002676 | furniture | pages [25] -->
m

<!-- b002677 | furniture | pages [25] -->
m

<!-- b002678 | furniture | pages [25] -->
m

<!-- b002679 | furniture | pages [25] -->
m

<!-- b002680 | furniture | pages [25] -->
m

<!-- b002681 | furniture | pages [25] -->
m

<!-- b002682 | furniture | pages [25] -->
m

<!-- b002683 | furniture | pages [25] -->
m

<!-- b002684 | furniture | pages [25] -->
m

<!-- b002685 | furniture | pages [25] -->
m

<!-- b002686 | furniture | pages [25] -->
m

<!-- b002687 | furniture | pages [25] -->
m

<!-- b002688 | furniture | pages [25] -->
m

<!-- b002689 | furniture | pages [25] -->
m

<!-- b002690 | furniture | pages [25] -->
m

<!-- b002691 | furniture | pages [25] -->
m

<!-- b002692 | furniture | pages [25] -->
m

<!-- b002693 | furniture | pages [25] -->
m

<!-- b002694 | furniture | pages [25] -->
m

<!-- b002695 | furniture | pages [25] -->
m

<!-- b002696 | furniture | pages [25] -->
m

<!-- b002697 | furniture | pages [25] -->
m

<!-- b002698 | furniture | pages [25] -->
m

<!-- b002699 | furniture | pages [25] -->
m

<!-- b002700 | furniture | pages [25] -->
m

<!-- b002701 | furniture | pages [25] -->
m

<!-- b002702 | furniture | pages [25] -->
m

<!-- b002703 | furniture | pages [25] -->
m

<!-- b002704 | furniture | pages [25] -->
m

<!-- b002705 | furniture | pages [25] -->
m

<!-- b002706 | furniture | pages [25] -->
m

<!-- b002707 | furniture | pages [25] -->
m

<!-- b002708 | furniture | pages [25] -->
m

<!-- b002709 | furniture | pages [25] -->
m

<!-- b002710 | furniture | pages [25] -->
m

<!-- b002711 | furniture | pages [25] -->
m

<!-- b002712 | furniture | pages [25] -->
m

<!-- b002713 | furniture | pages [25] -->
m

<!-- b002714 | furniture | pages [25] -->
m

<!-- b002715 | furniture | pages [25] -->
m

<!-- b002716 | furniture | pages [25] -->
m

<!-- b002717 | furniture | pages [25] -->
m

<!-- b002718 | furniture | pages [25] -->
m

<!-- b002719 | furniture | pages [25] -->
m

<!-- b002720 | furniture | pages [25] -->
m

<!-- b002721 | furniture | pages [25] -->
m

<!-- b002722 | furniture | pages [25] -->
m

<!-- b002723 | furniture | pages [25] -->
m

<!-- b002724 | furniture | pages [25] -->
m

<!-- b002725 | furniture | pages [25] -->
m

<!-- b002726 | furniture | pages [25] -->
m

<!-- b002727 | furniture | pages [25] -->
m

<!-- b002728 | furniture | pages [25] -->
m

<!-- b002729 | furniture | pages [25] -->
m

<!-- b002730 | furniture | pages [25] -->
m

<!-- b002731 | furniture | pages [25] -->
m

<!-- b002732 | furniture | pages [25] -->
m

<!-- b002733 | furniture | pages [25] -->
m

<!-- b002734 | furniture | pages [25] -->
m

<!-- b002735 | furniture | pages [25] -->
m

<!-- b002736 | furniture | pages [25] -->
m

<!-- b002737 | furniture | pages [25] -->
m

<!-- b002738 | furniture | pages [25] -->
m

<!-- b002739 | furniture | pages [25] -->
m

<!-- b002740 | furniture | pages [25] -->
m

<!-- b002741 | furniture | pages [25] -->
m

<!-- b002742 | furniture | pages [25] -->
m

<!-- b002743 | furniture | pages [25] -->
m

<!-- b002744 | furniture | pages [25] -->
m

<!-- b002745 | furniture | pages [25] -->
m

<!-- b002746 | furniture | pages [25] -->
m

<!-- b002747 | furniture | pages [25] -->
m

<!-- b002748 | furniture | pages [25] -->
m

<!-- b002749 | furniture | pages [25] -->
m

<!-- b002750 | furniture | pages [25] -->
m

<!-- b002751 | furniture | pages [25] -->
m

<!-- b002752 | furniture | pages [25] -->
m

<!-- b002753 | furniture | pages [25] -->
m

<!-- b002754 | furniture | pages [25] -->
m

<!-- b002755 | furniture | pages [25] -->
m

<!-- b002756 | furniture | pages [25] -->
m

<!-- b002757 | furniture | pages [25] -->
m

<!-- b002758 | furniture | pages [25] -->
m

<!-- b002759 | furniture | pages [25] -->
m

<!-- b002760 | furniture | pages [25] -->
m

<!-- b002761 | furniture | pages [25] -->
m

<!-- b002762 | furniture | pages [25] -->
m

<!-- b002763 | furniture | pages [25] -->
m

<!-- b002764 | furniture | pages [25] -->
m

<!-- b002765 | furniture | pages [25] -->
m

<!-- b002766 | furniture | pages [25] -->
m

<!-- b002767 | furniture | pages [25] -->
m

<!-- b002768 | furniture | pages [25] -->
m

<!-- b002769 | furniture | pages [25] -->
m

<!-- b002770 | furniture | pages [25] -->
m

<!-- b002771 | furniture | pages [25] -->
m

<!-- b002772 | furniture | pages [25] -->
m

<!-- b002773 | furniture | pages [25] -->
m

<!-- b002774 | furniture | pages [25] -->
m

<!-- b002775 | furniture | pages [25] -->
m

<!-- b002776 | furniture | pages [25] -->
m

<!-- b002777 | furniture | pages [25] -->
m

<!-- b002778 | furniture | pages [25] -->
m

<!-- b002779 | furniture | pages [25] -->
m

<!-- b002780 | furniture | pages [25] -->
m

<!-- b002781 | furniture | pages [25] -->
m

<!-- b002782 | furniture | pages [25] -->
m

<!-- b002783 | furniture | pages [25] -->
m

<!-- b002784 | furniture | pages [25] -->
m

<!-- b002785 | furniture | pages [25] -->
m

<!-- b002786 | furniture | pages [25] -->
m

<!-- b002787 | furniture | pages [25] -->
m

<!-- b002788 | furniture | pages [25] -->
m

<!-- b002789 | furniture | pages [25] -->
m

<!-- b002790 | furniture | pages [25] -->
m

<!-- b002791 | furniture | pages [25] -->
m

<!-- b002792 | furniture | pages [25] -->
m

<!-- b002793 | furniture | pages [25] -->
m

<!-- b002794 | furniture | pages [25] -->
m

<!-- b002795 | furniture | pages [25] -->
m

<!-- b002796 | furniture | pages [25] -->
m

<!-- b002797 | furniture | pages [25] -->
m

<!-- b002798 | furniture | pages [25] -->
m

<!-- b002799 | furniture | pages [25] -->
m

<!-- b002800 | furniture | pages [25] -->
m

<!-- b002801 | furniture | pages [25] -->
m

<!-- b002802 | furniture | pages [25] -->
m

<!-- b002803 | furniture | pages [25] -->
m

<!-- b002804 | furniture | pages [25] -->
m

<!-- b002805 | furniture | pages [25] -->
m

<!-- b002806 | furniture | pages [25] -->
m

<!-- b002807 | furniture | pages [25] -->
m

<!-- b002808 | furniture | pages [25] -->
m

<!-- b002809 | furniture | pages [25] -->
m

<!-- b002810 | furniture | pages [25] -->
m

<!-- b002811 | furniture | pages [25] -->
m

<!-- b002812 | furniture | pages [25] -->
m

<!-- b002813 | furniture | pages [25] -->
m

<!-- b002814 | furniture | pages [25] -->
m

<!-- b002815 | furniture | pages [25] -->
m

<!-- b002816 | furniture | pages [25] -->
m

<!-- b002817 | furniture | pages [25] -->
m

<!-- b002818 | furniture | pages [25] -->
m

<!-- b002819 | furniture | pages [25] -->
m

<!-- b002820 | furniture | pages [25] -->
m

<!-- b002821 | furniture | pages [25] -->
m

<!-- b002822 | furniture | pages [25] -->
m

<!-- b002823 | furniture | pages [25] -->
m

<!-- b002824 | furniture | pages [25] -->
m

<!-- b002825 | furniture | pages [25] -->
m

<!-- b002826 | furniture | pages [25] -->
m

<!-- b002827 | furniture | pages [25] -->
m

<!-- b002828 | furniture | pages [25] -->
m

<!-- b002829 | furniture | pages [25] -->
m

<!-- b002830 | furniture | pages [25] -->
m

<!-- b002831 | furniture | pages [25] -->
m

<!-- b002832 | furniture | pages [25] -->
m

<!-- b002833 | furniture | pages [25] -->
m

<!-- b002834 | furniture | pages [25] -->
m

<!-- b002835 | furniture | pages [25] -->
m

<!-- b002836 | furniture | pages [25] -->
m

<!-- b002837 | furniture | pages [25] -->
m

<!-- b002838 | furniture | pages [25] -->
m

<!-- b002839 | furniture | pages [25] -->
m

<!-- b002840 | furniture | pages [25] -->
m

<!-- b002841 | furniture | pages [25] -->
m

<!-- b002842 | furniture | pages [25] -->
m

<!-- b002843 | furniture | pages [25] -->
m

<!-- b002844 | furniture | pages [25] -->
m

<!-- b002845 | furniture | pages [25] -->
m

<!-- b002846 | furniture | pages [25] -->
m

<!-- b002847 | furniture | pages [25] -->
m

<!-- b002848 | furniture | pages [25] -->
m

<!-- b002849 | furniture | pages [25] -->
m

<!-- b002850 | furniture | pages [25] -->
m

<!-- b002851 | furniture | pages [25] -->
m

<!-- b002852 | furniture | pages [25] -->
m

<!-- b002853 | furniture | pages [25] -->
m

<!-- b002854 | furniture | pages [25] -->
m

<!-- b002855 | furniture | pages [25] -->
m

<!-- b002856 | furniture | pages [25] -->
m

<!-- b002857 | furniture | pages [25] -->
m

<!-- b002858 | furniture | pages [25] -->
m

<!-- b002859 | furniture | pages [25] -->
m

<!-- b002860 | furniture | pages [25] -->
m

<!-- b002861 | furniture | pages [25] -->
m

<!-- b002862 | furniture | pages [25] -->
m

<!-- b002863 | furniture | pages [25] -->
m

<!-- b002864 | furniture | pages [25] -->
m

<!-- b002865 | furniture | pages [25] -->
m

<!-- b002866 | furniture | pages [25] -->
m

<!-- b002867 | furniture | pages [25] -->
m

<!-- b002868 | furniture | pages [25] -->
m

<!-- b002869 | furniture | pages [25] -->
m

<!-- b002870 | furniture | pages [25] -->
m

<!-- b002871 | furniture | pages [25] -->
m

<!-- b002872 | furniture | pages [25] -->
m

<!-- b002873 | furniture | pages [25] -->
m

<!-- b002874 | furniture | pages [25] -->
m

<!-- b002875 | furniture | pages [25] -->
m

<!-- b002876 | furniture | pages [25] -->
m

<!-- b002877 | furniture | pages [25] -->
m

<!-- b002878 | furniture | pages [25] -->
m

<!-- b002879 | furniture | pages [25] -->
m

<!-- b002880 | furniture | pages [25] -->
m

<!-- b002881 | furniture | pages [25] -->
m

<!-- b002882 | furniture | pages [25] -->
m

<!-- b002883 | furniture | pages [25] -->
m

<!-- b002884 | furniture | pages [25] -->
m

<!-- b002885 | furniture | pages [25] -->
m

<!-- b002886 | furniture | pages [25] -->
m

<!-- b002887 | furniture | pages [25] -->
m

<!-- b002888 | furniture | pages [25] -->
m

<!-- b002889 | furniture | pages [25] -->
m

<!-- b002890 | furniture | pages [25] -->
m

<!-- b002891 | furniture | pages [25] -->
m

<!-- b002892 | furniture | pages [25] -->
m

<!-- b002893 | furniture | pages [25] -->
m

<!-- b002894 | furniture | pages [25] -->
m

<!-- b002895 | furniture | pages [25] -->
m

<!-- b002896 | furniture | pages [25] -->
m

<!-- b002897 | furniture | pages [25] -->
m

<!-- b002898 | furniture | pages [25] -->
m

<!-- b002899 | furniture | pages [25] -->
m

<!-- b002900 | furniture | pages [25] -->
m

<!-- b002901 | furniture | pages [25] -->
m

<!-- b002902 | furniture | pages [25] -->
m

<!-- b002903 | furniture | pages [25] -->
m

<!-- b002904 | furniture | pages [25] -->
m

<!-- b002905 | furniture | pages [25] -->
m

<!-- b002906 | furniture | pages [25] -->
m

<!-- b002907 | furniture | pages [25] -->
m

<!-- b002908 | furniture | pages [25] -->
m

<!-- b002909 | furniture | pages [25] -->
m

<!-- b002910 | furniture | pages [25] -->
m

<!-- b002911 | furniture | pages [25] -->
m

<!-- b002912 | furniture | pages [25] -->
m

<!-- b002913 | furniture | pages [25] -->
m

<!-- b002914 | furniture | pages [25] -->
m

<!-- b002915 | furniture | pages [25] -->
m

<!-- b002916 | furniture | pages [25] -->
m

<!-- b002917 | furniture | pages [25] -->
m

<!-- b002918 | furniture | pages [25] -->
m

<!-- b002919 | furniture | pages [25] -->
m

<!-- b002920 | furniture | pages [25] -->
m

<!-- b002921 | furniture | pages [25] -->
m

<!-- b002922 | heading | pages [26] -->
Report on Use of AI

<!-- b002923 | ai_disclosure | pages [26] -->
1. OpenAI ChatGPT (Nov 5, 2023 version, ChatGPT-4)

<!-- b002924 | ai_disclosure | pages [26] -->
Query1: What’s the average travel speed of a subway?

<!-- b002925 | ai_disclosure | pages [26] -->
Output: The average travel speed of a subway typically ranges from 30 to 40 km/h (about

<!-- b002926 | ai_disclosure | pages [26] -->
18 to 25 mph). This can vary depending on the city’s infrastructure, the specific subway

<!-- b002927 | ai_disclosure | pages [26] -->
line, and how many stops there are. For example, in cities like New York or Tokyo, the

<!-- b002928 | ai_disclosure | pages [26] -->
speed might be a little higher on express lines, but it slows down in more congested or

<!-- b002929 | ai_disclosure | pages [26] -->
older sections.

<!-- b002930 | ai_disclosure | pages [26] -->
2. OpenAI ChatGPT(Nov 5, 2023 version, ChatGPT-4)

<!-- b002931 | ai_disclosure | pages [26] -->
Query2: Introduce the current development situations of Baltimore, Maryland. Mainly

<!-- b002932 | ai_disclosure | pages [26] -->
focus on the transportation.

<!-- b002933 | ai_disclosure | pages [26] -->
Output: Baltimore, Maryland, has been undergoing significant development and revital-

<!-- b002934 | ai_disclosure | pages [26] -->
ization in recent years, particularly in the areas of urban infrastructure and transportation.

<!-- b002935 | ai_disclosure | pages [26] -->
Here’s a look at the current transportation situation and ongoing projects:

<!-- b002936 | ai_disclosure | pages [26] -->
1. Light Rail and Metro System:

<!-- b002937 | ai_disclosure | pages [26] -->
Baltimore has an existing light rail system and a metro subway system, both operated

<!-- b002938 | ai_disclosure | pages [26] -->
by the Maryland Transit Administration (MTA).

<!-- b002939 | ai_disclosure | pages [26] -->
Metro SubwayLink: Baltimore’s metro system includes a single line that runs from

<!-- b002940 | ai_disclosure | pages [26] -->
the Johns Hopkins Hospital to the suburban areas in the northwest (Pikesville). However,

<!-- b002941 | ai_disclosure | pages [26] -->
the metro system is limited in scope and coverage compared to cities like New York or

<!-- b002942 | ai_disclosure | pages [26] -->
Washington D.C., and there have been calls for its expansion and modernization.

<!-- b002943 | ai_disclosure | pages [26] -->
2. Bus Rapid Transit (BRT) & Expansion:

<!-- b002944 | ai_disclosure | pages [26] -->
Baltimore is planning a Bus Rapid Transit (BRT) system to provide faster, more

<!-- b002945 | ai_disclosure | pages [26] -->
efficient bus service. This project, known as the BaltimoreLink project, aims to overhaul

<!-- b002946 | ai_disclosure | pages [26] -->
the city’s bus routes and improve connectivity between neighborhoods, downtown, and

<!-- b002947 | ai_disclosure | pages [26] -->
the suburbs. The BRT routes are designed to provide more dedicated bus lanes and better

<!-- b002948 | ai_disclosure | pages [26] -->
coordination with other modes of transportation.

<!-- b002949 | ai_disclosure | pages [26] -->
3. Highway and Road Infrastructure:

<!-- b002950 | ai_disclosure | pages [26] -->
Baltimore’s road network, including key highways like Interstate 95 (I-95) and

<!-- b002951 | ai_disclosure | pages [26] -->
Interstate 695 (I-695), is being continually upgraded. However, these highways are often

<!-- b002952 | ai_disclosure | pages [26] -->
subject to heavy traffic, especially during peak hours.

<!-- b002953 | ai_disclosure | pages [26] -->
3. OpenAI ChatGPT(Nov 5, 2023 version, ChatGPT-4)

<!-- b002954 | ai_disclosure | pages [26] -->
Query3: TOPSIS-weight-entropy method, as a combination of two method, in which

<!-- b002955 | ai_disclosure | pages [26] -->
aspects have advantages over the single model?

<!-- b002956 | heading | pages [26] -->
Output: The TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)

<!-- b002957 | prose | pages [26] -->
combined with the entropy method offers several advantages over using each of these methods individually, especially in decision-making and multi-criteria decision analysis (MCDA). Here’s how combining these two methods benefits the process:

<!-- b002958 | prose | pages [26] -->
1. Objective Weight Determination (Entropy Method)

<!-- b002959 | prose | pages [26] -->
Entropy Method: It helps in determining the weight of each criterion based on the amount of information it provides. In decision problems, the entropy method is often

<!-- b002960 | prose | pages [26, 27] -->
关注数学模型 used to objectively assign weights to each criterion by analyzing the degree of variation or uncertainty in the data. A criterion with higher variability (more information) gets a higher weight, which is a more objective and data-driven approach than assigning arbitrary or subjective weights. Advantage: When you combine this with TOPSIS, it ensures that the weights assigned to each criterion are not biased or arbitrary. This makes the decision process more transparent and credible. 微信公众号：数学模型 2. Ranking Accuracy (TOPSIS)

<!-- b002961 | furniture | pages [26] -->
2

<!-- b002962 | furniture | pages [26] -->
MATHmodels

<!-- b002963 | furniture | pages [26] -->
获取更多资讯

<!-- b002965 | prose | pages [27] -->
TOPSIS: TOPSIS works by calculating the proximity of each alternative to the ideal and negative-ideal solutions, ultimately ranking the alternatives based on their relative closeness to the ideal solution. It’s a widely used method due to its simplicity and interpretability. Advantage: TOPSIS helps to perform the final ranking of alternatives and makes the decision-making process more straightforward by quantifying how close each alternative is to the ideal solution.

<!-- b002966 | prose | pages [27] -->
3. Handling Uncertainty (Entropy + TOPSIS)

<!-- b002967 | prose | pages [27] -->
Entropy Method for Uncertainty: In the entropy method, weights are assigned in 微信号：MATHmodels a way that reflects the uncertainty of each criterion. This is especially helpful when there is a lot of variability in the data, as it prevents overemphasis on criteria with low information content. Advantage of Combination: When used together, entropy provides an objective weight assignment that adapts to data variability, while TOPSIS handles the relative ranking based on proximity to the ideal solution. This combination ensures that the rankings are not only driven by subjective preferences but also by the intrinsic uncertainty and information content in the data.

<!-- b002968 | prose | pages [27] -->
4. Mitigating the Impact of Subjectivity

<!-- b002969 | prose | pages [27] -->
TOPSIS Alone: Without entropy, the TOPSIS method requires predefined weights, which are often subjective and based on expert judgment or assumption. This can intro- duce bias, particularly when the decision-makers have limited or inconsistent knowledge of the criteria’s relative importance. Advantage of Combination: The entropy method provides a more objective weight assignment, reducing the subjectivity involved in the decision-making process. By using entropy to calculate weights, the model ensures that the weights reflect the data characteristics, making the ranking in TOPSIS more robust and less prone to human bias.

<!-- b002970 | prose | pages [27] -->
5. Flexibility and Robustness

<!-- b002971 | prose | pages [27] -->
TOPSIS with Entropy Weights: By integrating entropy with TOPSIS, the method becomes more flexible and robust in handling a wider range of decision problems. It allows for better performance in situations where the importance of criteria may not be immediately obvious or when there is significant variability in the data. Advantage: This combination is particularly useful when dealing with complex multi-criteria decision problems in uncertain or diverse environments. The entropy method ensures that criteria with higher uncertainty or variability are weighted more appropriately, while TOPSIS provides a solid framework for ranking based on those weights.

<!-- b002972 | prose | pages [27] -->
In essence, combining TOPSIS and the entropy method enhances both the objectivity and accuracy of the decision-making process, addressing the limitations of using either method alone.

<!-- b002973 | prose | pages [27] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002974 | furniture | pages [27] -->
m

<!-- b002975 | furniture | pages [27] -->
m

<!-- b002976 | furniture | pages [27] -->
m

<!-- b002977 | furniture | pages [27] -->
m

<!-- b002978 | furniture | pages [27] -->
m

<!-- b002979 | furniture | pages [27] -->
m

<!-- b002980 | furniture | pages [27] -->
m

<!-- b002981 | furniture | pages [27] -->
m

<!-- b002982 | furniture | pages [27] -->
m

<!-- b002983 | furniture | pages [27] -->
m

<!-- b002984 | furniture | pages [27] -->
m

<!-- b002985 | furniture | pages [27] -->
m

<!-- b002986 | furniture | pages [27] -->
m

<!-- b002987 | furniture | pages [27] -->
m

<!-- b002988 | furniture | pages [27] -->
m

<!-- b002989 | furniture | pages [27] -->
m

<!-- b002990 | furniture | pages [27] -->
m

<!-- b002991 | furniture | pages [27] -->
m

<!-- b002992 | furniture | pages [27] -->
m

<!-- b002993 | furniture | pages [27] -->
m

<!-- b002994 | furniture | pages [27] -->
m

<!-- b002995 | furniture | pages [27] -->
m

<!-- b002996 | furniture | pages [27] -->
m

<!-- b002997 | furniture | pages [27] -->
m

<!-- b002998 | furniture | pages [27] -->
m

<!-- b002999 | furniture | pages [27] -->
m

<!-- b003000 | furniture | pages [27] -->
m

<!-- b003001 | furniture | pages [27] -->
m

<!-- b003002 | furniture | pages [27] -->
m

<!-- b003003 | furniture | pages [27] -->
m

<!-- b003004 | furniture | pages [27] -->
m

<!-- b003005 | furniture | pages [27] -->
m

<!-- b003006 | furniture | pages [27] -->
m

<!-- b003007 | furniture | pages [27] -->
m

<!-- b003008 | furniture | pages [27] -->
m

<!-- b003009 | furniture | pages [27] -->
m

<!-- b003010 | furniture | pages [27] -->
m

<!-- b003011 | furniture | pages [27] -->
m

<!-- b003012 | furniture | pages [27] -->
m

<!-- b003013 | furniture | pages [27] -->
m

<!-- b003014 | furniture | pages [27] -->
m

<!-- b003015 | furniture | pages [27] -->
m

<!-- b003016 | furniture | pages [27] -->
m

<!-- b003017 | furniture | pages [27] -->
m

<!-- b003018 | furniture | pages [27] -->
m

<!-- b003019 | furniture | pages [27] -->
m

<!-- b003020 | furniture | pages [27] -->
m

<!-- b003021 | furniture | pages [27] -->
m

<!-- b003022 | furniture | pages [27] -->
m

<!-- b003023 | furniture | pages [27] -->
m

<!-- b003024 | furniture | pages [27] -->
m

<!-- b003025 | furniture | pages [27] -->
m

<!-- b003026 | furniture | pages [27] -->
m

<!-- b003027 | furniture | pages [27] -->
m

<!-- b003028 | furniture | pages [27] -->
m

<!-- b003029 | furniture | pages [27] -->
m

<!-- b003030 | furniture | pages [27] -->
m

<!-- b003031 | furniture | pages [27] -->
m

<!-- b003032 | furniture | pages [27] -->
m

<!-- b003033 | furniture | pages [27] -->
m

<!-- b003034 | furniture | pages [27] -->
m

<!-- b003035 | furniture | pages [27] -->
m

<!-- b003036 | furniture | pages [27] -->
m

<!-- b003037 | furniture | pages [27] -->
m

<!-- b003038 | furniture | pages [27] -->
m

<!-- b003039 | furniture | pages [27] -->
m

<!-- b003040 | furniture | pages [27] -->
m

<!-- b003041 | furniture | pages [27] -->
m

<!-- b003042 | furniture | pages [27] -->
m

<!-- b003043 | furniture | pages [27] -->
m

<!-- b003044 | furniture | pages [27] -->
m

<!-- b003045 | furniture | pages [27] -->
m

<!-- b003046 | furniture | pages [27] -->
m

<!-- b003047 | furniture | pages [27] -->
m

<!-- b003048 | furniture | pages [27] -->
m

<!-- b003049 | furniture | pages [27] -->
m

<!-- b003050 | furniture | pages [27] -->
m

<!-- b003051 | furniture | pages [27] -->
m

<!-- b003052 | furniture | pages [27] -->
m

<!-- b003053 | furniture | pages [27] -->
m

<!-- b003054 | furniture | pages [27] -->
m

<!-- b003055 | furniture | pages [27] -->
m

<!-- b003056 | furniture | pages [27] -->
m

<!-- b003057 | furniture | pages [27] -->
m

<!-- b003058 | furniture | pages [27] -->
m

<!-- b003059 | furniture | pages [27] -->
m

<!-- b003060 | furniture | pages [27] -->
m

<!-- b003061 | furniture | pages [27] -->
m

<!-- b003062 | furniture | pages [27] -->
m

<!-- b003063 | furniture | pages [27] -->
m

<!-- b003064 | furniture | pages [27] -->
m

<!-- b003065 | furniture | pages [27] -->
m

<!-- b003066 | furniture | pages [27] -->
m

<!-- b003067 | furniture | pages [27] -->
m

<!-- b003068 | furniture | pages [27] -->
m

<!-- b003069 | furniture | pages [27] -->
m

<!-- b003070 | furniture | pages [27] -->
m

<!-- b003071 | furniture | pages [27] -->
m

<!-- b003072 | furniture | pages [27] -->
m

<!-- b003073 | furniture | pages [27] -->
m

<!-- b003074 | furniture | pages [27] -->
m

<!-- b003075 | furniture | pages [27] -->
m

<!-- b003076 | furniture | pages [27] -->
m

<!-- b003077 | furniture | pages [27] -->
m

<!-- b003078 | furniture | pages [27] -->
m

<!-- b003079 | furniture | pages [27] -->
m

<!-- b003080 | furniture | pages [27] -->
m

<!-- b003081 | furniture | pages [27] -->
m

<!-- b003082 | furniture | pages [27] -->
m

<!-- b003083 | furniture | pages [27] -->
m

<!-- b003084 | furniture | pages [27] -->
m

<!-- b003085 | furniture | pages [27] -->
m

<!-- b003086 | furniture | pages [27] -->
m

<!-- b003087 | furniture | pages [27] -->
m

<!-- b003088 | furniture | pages [27] -->
m

<!-- b003089 | furniture | pages [27] -->
m

<!-- b003090 | furniture | pages [27] -->
m

<!-- b003091 | furniture | pages [27] -->
m

<!-- b003092 | furniture | pages [27] -->
m

<!-- b003093 | furniture | pages [27] -->
m

<!-- b003094 | furniture | pages [27] -->
m

<!-- b003095 | furniture | pages [27] -->
m

<!-- b003096 | furniture | pages [27] -->
m

<!-- b003097 | furniture | pages [27] -->
m

<!-- b003098 | furniture | pages [27] -->
m

<!-- b003099 | furniture | pages [27] -->
m

<!-- b003100 | furniture | pages [27] -->
m

<!-- b003101 | furniture | pages [27] -->
m

<!-- b003102 | furniture | pages [27] -->
m

<!-- b003103 | furniture | pages [27] -->
m

<!-- b003104 | furniture | pages [27] -->
m

<!-- b003105 | furniture | pages [27] -->
m

<!-- b003106 | furniture | pages [27] -->
m

<!-- b003107 | furniture | pages [27] -->
m

<!-- b003108 | furniture | pages [27] -->
m

<!-- b003109 | furniture | pages [27] -->
m

<!-- b003110 | furniture | pages [27] -->
m

<!-- b003111 | furniture | pages [27] -->
m

<!-- b003112 | furniture | pages [27] -->
m

<!-- b003113 | furniture | pages [27] -->
m

<!-- b003114 | furniture | pages [27] -->
m

<!-- b003115 | furniture | pages [27] -->
m

<!-- b003116 | furniture | pages [27] -->
m

<!-- b003117 | furniture | pages [27] -->
m

<!-- b003118 | furniture | pages [27] -->
m

<!-- b003119 | furniture | pages [27] -->
m

<!-- b003120 | furniture | pages [27] -->
m

<!-- b003121 | furniture | pages [27] -->
m

<!-- b003122 | furniture | pages [27] -->
m

<!-- b003123 | furniture | pages [27] -->
m

<!-- b003124 | furniture | pages [27] -->
m

<!-- b003125 | furniture | pages [27] -->
m

<!-- b003126 | furniture | pages [27] -->
m

<!-- b003127 | furniture | pages [27] -->
m

<!-- b003128 | furniture | pages [27] -->
m

<!-- b003129 | furniture | pages [27] -->
m

<!-- b003130 | furniture | pages [27] -->
m

<!-- b003131 | furniture | pages [27] -->
m

<!-- b003132 | furniture | pages [27] -->
m

<!-- b003133 | furniture | pages [27] -->
m

<!-- b003134 | furniture | pages [27] -->
m

<!-- b003135 | furniture | pages [27] -->
m

<!-- b003136 | furniture | pages [27] -->
m

<!-- b003137 | furniture | pages [27] -->
m

<!-- b003138 | furniture | pages [27] -->
m

<!-- b003139 | furniture | pages [27] -->
m

<!-- b003140 | furniture | pages [27] -->
m

<!-- b003141 | furniture | pages [27] -->
m

<!-- b003142 | furniture | pages [27] -->
m

<!-- b003143 | furniture | pages [27] -->
m

<!-- b003144 | furniture | pages [27] -->
m

<!-- b003145 | furniture | pages [27] -->
m

<!-- b003146 | furniture | pages [27] -->
m

<!-- b003147 | furniture | pages [27] -->
m

<!-- b003148 | furniture | pages [27] -->
m

<!-- b003149 | furniture | pages [27] -->
m

<!-- b003150 | furniture | pages [27] -->
m

<!-- b003151 | furniture | pages [27] -->
m

<!-- b003152 | furniture | pages [27] -->
m

<!-- b003153 | furniture | pages [27] -->
m

<!-- b003154 | furniture | pages [27] -->
m

<!-- b003155 | furniture | pages [27] -->
m

<!-- b003156 | furniture | pages [27] -->
m

<!-- b003157 | furniture | pages [27] -->
m

<!-- b003158 | furniture | pages [27] -->
m

<!-- b003159 | furniture | pages [27] -->
m

<!-- b003160 | furniture | pages [27] -->
m

<!-- b003161 | furniture | pages [27] -->
m

<!-- b003162 | furniture | pages [27] -->
m

<!-- b003163 | furniture | pages [27] -->
m

<!-- b003164 | furniture | pages [27] -->
m

<!-- b003165 | furniture | pages [27] -->
m

<!-- b003166 | furniture | pages [27] -->
m

<!-- b003167 | furniture | pages [27] -->
m

<!-- b003168 | furniture | pages [27] -->
m

<!-- b003169 | furniture | pages [27] -->
m

<!-- b003170 | furniture | pages [27] -->
m

<!-- b003171 | furniture | pages [27] -->
m

<!-- b003172 | furniture | pages [27] -->
m

<!-- b003173 | furniture | pages [27] -->
m

<!-- b003174 | furniture | pages [27] -->
m

<!-- b003175 | furniture | pages [27] -->
m

<!-- b003176 | furniture | pages [27] -->
m

<!-- b003177 | furniture | pages [27] -->
m

<!-- b003178 | furniture | pages [27] -->
m

<!-- b003179 | furniture | pages [27] -->
m

<!-- b003180 | furniture | pages [27] -->
m

<!-- b003181 | furniture | pages [27] -->
m

<!-- b003182 | furniture | pages [27] -->
m

<!-- b003183 | furniture | pages [27] -->
m

<!-- b003184 | furniture | pages [27] -->
m

<!-- b003185 | furniture | pages [27] -->
m

<!-- b003186 | furniture | pages [27] -->
m

<!-- b003187 | furniture | pages [27] -->
m

<!-- b003188 | furniture | pages [27] -->
m

<!-- b003189 | furniture | pages [27] -->
m

<!-- b003190 | furniture | pages [27] -->
m

<!-- b003191 | furniture | pages [27] -->
m

<!-- b003192 | furniture | pages [27] -->
m

<!-- b003193 | furniture | pages [27] -->
m

<!-- b003194 | furniture | pages [27] -->
m

<!-- b003195 | furniture | pages [27] -->
m

<!-- b003196 | furniture | pages [27] -->
m

<!-- b003197 | furniture | pages [27] -->
m

<!-- b003198 | furniture | pages [27] -->
m

<!-- b003199 | furniture | pages [27] -->
m

<!-- b003200 | furniture | pages [27] -->
m

<!-- b003201 | furniture | pages [27] -->
m

<!-- b003202 | furniture | pages [27] -->
m

<!-- b003203 | furniture | pages [27] -->
m

<!-- b003204 | furniture | pages [27] -->
m

<!-- b003205 | furniture | pages [27] -->
m

<!-- b003206 | furniture | pages [27] -->
m

<!-- b003207 | furniture | pages [27] -->
m

<!-- b003208 | furniture | pages [27] -->
m

<!-- b003209 | furniture | pages [27] -->
m

<!-- b003210 | furniture | pages [27] -->
m

<!-- b003211 | furniture | pages [27] -->
m

<!-- b003212 | furniture | pages [27] -->
m

<!-- b003213 | furniture | pages [27] -->
m

<!-- b003214 | furniture | pages [27] -->
m

<!-- b003215 | furniture | pages [27] -->
m

<!-- b003216 | furniture | pages [27] -->
m

<!-- b003217 | furniture | pages [27] -->
m

<!-- b003218 | furniture | pages [27] -->
m

<!-- b003219 | furniture | pages [27] -->
m

<!-- b003220 | furniture | pages [27] -->
m

<!-- b003221 | furniture | pages [27] -->
m

<!-- b003222 | furniture | pages [27] -->
m

<!-- b003223 | furniture | pages [27] -->
m

<!-- b003224 | furniture | pages [27] -->
m

<!-- b003225 | furniture | pages [27] -->
m

<!-- b003226 | furniture | pages [27] -->
m

<!-- b003227 | furniture | pages [27] -->
m

<!-- b003228 | furniture | pages [27] -->
m

<!-- b003229 | furniture | pages [27] -->
m

<!-- b003230 | furniture | pages [27] -->
m

<!-- b003231 | furniture | pages [27] -->
m

<!-- b003232 | furniture | pages [27] -->
m

<!-- b003233 | furniture | pages [27] -->
m

<!-- b003234 | furniture | pages [27] -->
m

<!-- b003235 | furniture | pages [27] -->
m

<!-- b003236 | furniture | pages [27] -->
m

<!-- b003237 | furniture | pages [27] -->
m

<!-- b003238 | furniture | pages [27] -->
m

<!-- b003239 | furniture | pages [27] -->
m

<!-- b003240 | furniture | pages [27] -->
m

<!-- b003241 | furniture | pages [27] -->
m

<!-- b003242 | furniture | pages [27] -->
m

<!-- b003243 | furniture | pages [27] -->
m

<!-- b003244 | furniture | pages [27] -->
m

<!-- b003245 | furniture | pages [27] -->
m

<!-- b003246 | furniture | pages [27] -->
m

<!-- b003247 | furniture | pages [27] -->
m

<!-- b003248 | furniture | pages [27] -->
m

<!-- b003249 | furniture | pages [27] -->
m

<!-- b003250 | furniture | pages [27] -->
m

<!-- b003251 | furniture | pages [27] -->
m

<!-- b003252 | furniture | pages [27] -->
m

<!-- b003253 | furniture | pages [27] -->
m

<!-- b003254 | furniture | pages [27] -->
m

<!-- b003255 | furniture | pages [27] -->
m

<!-- b003256 | furniture | pages [27] -->
m

<!-- b003257 | furniture | pages [27] -->
m

<!-- b003258 | furniture | pages [27] -->
m

<!-- b003259 | furniture | pages [27] -->
m

<!-- b003260 | furniture | pages [27] -->
m

<!-- b003261 | furniture | pages [27] -->
m

<!-- b003262 | furniture | pages [27] -->
m

<!-- b003263 | furniture | pages [27] -->
m

<!-- b003264 | furniture | pages [27] -->
m

<!-- b003265 | furniture | pages [27] -->
m

<!-- b003266 | furniture | pages [27] -->
m

<!-- b003267 | furniture | pages [27] -->
m

<!-- b003268 | furniture | pages [27] -->
m

<!-- b003269 | furniture | pages [27] -->
m

<!-- b003270 | furniture | pages [27] -->
m

<!-- b003271 | furniture | pages [27] -->
m

<!-- b003272 | furniture | pages [27] -->
m

<!-- b003273 | furniture | pages [27] -->
m

<!-- b003274 | furniture | pages [27] -->
m

<!-- b003275 | furniture | pages [27] -->
m

<!-- b003276 | furniture | pages [27] -->
m

<!-- b003277 | furniture | pages [27] -->
m

<!-- b003278 | furniture | pages [27] -->
m

<!-- b003279 | furniture | pages [27] -->
m

<!-- b003280 | furniture | pages [27] -->
m

<!-- b003281 | furniture | pages [27] -->
m

<!-- b003282 | furniture | pages [27] -->
m

<!-- b003283 | furniture | pages [27] -->
m

<!-- b003284 | furniture | pages [27] -->
m

<!-- b003285 | furniture | pages [27] -->
m

<!-- b003286 | furniture | pages [27] -->
m

<!-- b003287 | furniture | pages [27] -->
m

<!-- b003288 | furniture | pages [27] -->
m

<!-- b003289 | furniture | pages [27] -->
m

<!-- b003290 | furniture | pages [27] -->
m

<!-- b003291 | furniture | pages [27] -->
m

<!-- b003292 | furniture | pages [27] -->
m

<!-- b003293 | furniture | pages [27] -->
m

<!-- b003294 | furniture | pages [27] -->
m

<!-- b003295 | furniture | pages [27] -->
m

<!-- b003296 | furniture | pages [27] -->
m

<!-- b003297 | furniture | pages [27] -->
m
