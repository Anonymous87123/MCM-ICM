# P-D-2025-2504188-db12259e

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000002 | furniture | pages [1] -->
Team # 2504188 Page 1 of 25

<!-- b000003 | front_matter | pages [1] -->
Problem Chosen D 2025 MCM/ICM Summary Sheet Team Number 2504188

<!-- b000004 | title | pages [1] -->
Revitalizing Transport: A Safer, Smarter Future for Baltimore's Network

<!-- b000005 | heading | pages [1] -->
Summary

<!-- b000006 | prose | pages [1] -->
In Baltimore, the population continues to grow, and the aging transportation network is struggling to meet the increasing travel demands. The collapse of the Francis Scott Key Bridge has exacerbated the already strained city traffic. Optimizing the transportation system has become urgent. To address this, we conducted an evaluation of Baltimore’s transportation network based on stakeholder needs, followed by targeted optimization measures.

<!-- b000007 | prose | pages [1] -->
For Task 1, we first visualized Baltimore's transportation network. To assess the overall traffic conditions, we used Queueing Theory to calculate the congestion index. For each stakeholder, we quantified their needs using Accessibility to various locations, with different types of accessibility considered for each stakeholder. We used a method combining A* and GA to calculate Accessibility. Finally, we simulated actual data on the map, comparing the changes in the above metrics and the overall network before and after the bridge collapse to highlight its severe negative impact. The results are shown in Figure 6, Figure 7, and Figure 9.

<!-- b000008 | prose | pages [1] -->
For Task 2, we chose bus route optimization as a potential project. First, we established the Baltimore bus network and measured the importance of each station using node Betweenness Centrality and Degree Centrality, identifying areas in need of optimization. We then created a nonlinear programming model with the objective of maximizing bus coverage, subject to constraints on the coordinates and number of new stations, as well as the distance between new and original stations. Since the area is irregular, we used Monte Carlo Simulations to calculate the bus coverage. This project increased bus coverage from 61.37% to 78.13%. Finally, we compared stakeholder ratings before and after the improvement, proving the significant positive impact on stakeholders, as shown in Figure 12.

<!-- b000009 | prose | pages [1] -->
For Task 3, we recommended a project to improve Road Availability in neighborhoods. We selected Connectivity Index, Congestion Index, and Mixing Index as metrics for Road Availability. We used Approximate Dynamic Programming(ADP) to optimize paths in low-scoring areas, with the results shown in Figure 13. We proved this project had a positive impact on multiple aspects for various stakeholders.

<!-- b000010 | prose | pages [1] -->
Additionally, to ensure the safety of the transportation system, we developed software that integrates the indicators and conclusions from the three models.

<!-- b000011 | prose | pages [1] -->
Lastly, we conducted sensitivity analysis to prove the robustness of the models and the reasonableness of parameter selection. The key highlight of this study is the comprehensive visualization and in-depth analysis of local conditions, the practical selection of models, and the thorough simulation of the established models.

<!-- b000012 | keywords | pages [1] -->
Keywords: Stakeholder; Queueing Theory; Accessibility; A* and GA; Monte Carlo Simulations; ADP

<!-- b000013 | furniture | pages [1] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000014 | furniture | pages [2] -->
Page 2 of 25

<!-- b000015 | furniture | pages [2] -->
Team # 2504188

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1 Introduction.

<!-- b000018 | contents | pages [2] -->
1.1 Problem Background.

<!-- b000019 | contents | pages [2] -->
1.2 Restatement of the Problem.

<!-- b000020 | contents | pages [2] -->
1.3 Our Work.

<!-- b000021 | contents | pages [2] -->
2 Assumptions and Justifications

<!-- b000022 | contents | pages [2] -->
3Notations.

<!-- b000023 | contents | pages [2] -->
4 Data Processing

<!-- b000024 | contents | pages [2] -->
5 Bridge Collapse Impact Quantification Model,

<!-- b000025 | contents | pages [2] -->
5.1 Network model building and visualization....

<!-- b000026 | contents | pages [2] -->
5.2 Quantification of impact indicators.

<!-- b000027 | contents | pages [2] -->
5.3 Accessibility definition and solution.

<!-- b000028 | contents | pages [2] -->
.10

<!-- b000029 | contents | pages [2] -->
5.4 Bridge collapse data processing ......

<!-- b000030 | contents | pages [2] -->
0

<!-- b000031 | contents | pages [2] -->
5.5 Solution.

<!-- b000032 | contents | pages [2] -->
12

<!-- b000033 | contents | pages [2] -->
6 Transit Network Optimization Model.

<!-- b000034 | contents | pages [2] -->
.14

<!-- b000035 | contents | pages [2] -->
6.1 Urban Bus Network Visualization

<!-- b000036 | contents | pages [2] -->
.14

<!-- b000037 | contents | pages [2] -->
.15

<!-- b000038 | contents | pages [2] -->
6.2 Single-objective Optimization Model.

<!-- b000039 | contents | pages [2] -->
6.3 Solution ..

<!-- b000040 | contents | pages [2] -->
17

<!-- b000041 | contents | pages [2] -->
7 Community Road Availability Optimization Model.

<!-- b000042 | contents | pages [2] -->
19

<!-- b000043 | contents | pages [2] -->
7.1 Supplementary Datasets.

<!-- b000044 | contents | pages [2] -->
.19

<!-- b000045 | contents | pages [2] -->
7.2 Community transportation availability evaluation.

<!-- b000046 | contents | pages [2] -->
19

<!-- b000047 | contents | pages [2] -->
.20

<!-- b000048 | contents | pages [2] -->
7.4 Solution.

<!-- b000049 | contents | pages [2] -->
.21

<!-- b000050 | contents | pages [2] -->
8 Model Application for Security

<!-- b000051 | contents | pages [2] -->
.22

<!-- b000052 | contents | pages [2] -->
.23

<!-- b000053 | contents | pages [2] -->
9 Sensitivity Analysis

<!-- b000054 | contents | pages [2] -->
●

<!-- b000055 | contents | pages [2] -->
10 Model Evaluation......

<!-- b000056 | contents | pages [2] -->
.24

<!-- b000057 | contents | pages [2] -->
10.1 Strengths......

<!-- b000058 | contents | pages [2] -->
24

<!-- b000059 | contents | pages [2] -->
10.2 Weaknesses..

<!-- b000060 | contents | pages [2] -->
24

<!-- b000061 | contents | pages [2] -->
References...

<!-- b000062 | contents | pages [2] -->
24

<!-- b000063 | contents | pages [2] -->
关注数学模型

<!-- b000064 | furniture | pages [2] -->
获取更多资讯

<!-- b000065 | furniture | pages [3] -->
Team # 2504188

<!-- b000066 | furniture | pages [3] -->
Page 3 of 25

<!-- b000067 | heading | pages [3] -->
1 Introduction

<!-- b000068 | heading | pages [3] -->
1.1 Problem Background

<!-- b000069 | prose | pages [3] -->
"Traffic safety is a very serious matter. Every year thousands of people die in 微信公众号：数学模型 traffic-related accidents. This is not a matter of numbers; it’s about lives, families, and communities. We need to act together to make our roads safer."

<!-- b000070 | prose | pages [3] -->
Barbara Boxer

<!-- b000071 | prose | pages [3] -->
The transportation system directly impacts urban development and residents' lives. An efficient transportation network can promote economic growth, attract new businesses and residents, but it often faces conflicts between the needs of different groups. Baltimore is currently dealing with issues such as aging infrastructure, limited transportation options, and problems like the collapse of the Francis Scott Key Bridge, 微信号：MATHmodels which have caused traffic congestion, affecting residents' mobility and the city's economic development. To address these issues, Baltimore is undergoing a transportation network overhaul, with the goal of enhancing public transit, improving infrastructure, and achieving sustainable development.

<!-- b000072 | caption | pages [3] -->
Figure 1: Background Screening

<!-- b000073 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000074 | prose | pages [3] -->
Your team needs to propose recommendations to help improve Baltimore's transportation network, with a focus on the following issues: the impact of the collapse of the Francis Scott Key Bridge on the transportation system, the inadequacy of public transit and walking infrastructure, and the disruption caused by urban highways to communities. By building a transportation network model, you need to analyze how these issues affect different groups and propose corresponding solutions.

<!-- b000075 | prose | pages [3] -->
· Impact of Bridge Collapse: Analyze the impact of the Francis Scott Key Bridge collapse on transportation, particularly how it affects commuters, businesses, and residents, and propose improvements.

<!-- b000076 | prose | pages [3] -->
· Public Transit and Walking Infrastructure: Study potential projects to improve the bus or walking systems, analyze how these projects can enhance residents' mobility, and their impact on other groups.

<!-- b000077 | heading | pages [3] -->
·Improvement Recommendations: Propose a project to improve Baltimore's

<!-- b000078 | prose | pages [3, 4] -->
transportation network, detailing the project's advantages and disadvantages, especially its impact on residents' lives, travel safety, and economic activities.

<!-- b000079 | furniture | pages [4] -->
Team # 2504188

<!-- b000080 | furniture | pages [4] -->
Page 4 of 25

<!-- b000082 | heading | pages [4] -->
1.3 Our Work

<!-- b000083 | prose | pages [4] -->
Based on the problem analysis, we construct three distinctive models—Bridge Collapse Impact Quantification Model, Transit Network Optimization Model and Community transportation availability optimization model. Then we have designed a software to enhance the traffic safety of Baltimore City. Finally, we conduct sensitivity to test the robustness of our models. The work we have done is mainly shown in Figure 2.

<!-- b000084 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000085 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000086 | heading | pages [4] -->
▲Assumption: The departure and destination points of stakeholders follow a

<!-- b000087 | prose | pages [4] -->
specific spatial flow pattern.

<!-- b000088 | prose | pages [4] -->
▼Justification: In reality, the exact departure and destination points for each stakeholder in the traffic network are difficult to predict and influenced by various factors. However, as a general trend, the flow patterns tend to follow certain

<!-- b000089 | prose | pages [4, 5] -->
关注数学模型 regularities, which can be modeled based on known spatial patterns and specific probability distributions.

<!-- b000090 | furniture | pages [4] -->
2

<!-- b000091 | furniture | pages [4] -->
MATHmodels

<!-- b000092 | furniture | pages [4] -->
获取更多资讯

<!-- b000093 | furniture | pages [5] -->
Team # 2504188

<!-- b000094 | furniture | pages [5] -->
Page 5 of 25

<!-- b000096 | prose | pages [5] -->
▲Assumption: Traffic flow in the network is stable, with no consideration for short-term disruptions (such as weather, accidents, etc.).

<!-- b000097 | prose | pages [5] -->
▼Justification: To simplify the analysis, short-term external factors such as weather and accidents are excluded, and the focus is placed on the impact of large-scale disruptive events, like bridge collapses.

<!-- b000098 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000099 | heading | pages [5] -->
▲Assumption: Vehicles arrive at a road segment randomly and independently,

<!-- b000100 | prose | pages [5] -->
with the same travel time through the segment.

<!-- b000101 | prose | pages [5] -->
▼Justification: The travel decisions of different vehicles are independent. In some traffic-controlled routes in Baltimore, vehicles are strictly required to maintain a specific speed, significantly reducing speed differences, which makes the time taken by vehicles to pass through these segments nearly identical.

<!-- b000102 | heading | pages [5] -->
3 Notations

<!-- b000103 | prose | pages [5] -->
微信号：MATHmodels The key mathematical notations used in this paper are listed in Table 1.

<!-- b000104 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000105 | heading | pages [5] -->
Symbol

<!-- b000106 | prose | pages [5] -->
Description Unit 퐿푞 Traffic Congestion Index 5 푁표푑푒푠 Crossroads Collection 5 퐸푑푔푒푠 Path Collection 5 퐶퐵(푣) Betweenness Centrality 6 퐶퐷(푣) Degree centrality 6 퐶퐼 The connectivity index 7 퐿푈푀퐼 The hybrid index 7 Note: There are some variables that are not listed here and will be discussed in detail in each section.

<!-- b000107 | heading | pages [5] -->
4 Data Processing

<!-- b000108 | prose | pages [5] -->
·Data Filtering To ensure that all routes belong to the Baltimore transportation network, we screened the routes according to the latitude and longitude range of Baltimore, and only retained the sections with latitudes between 39.18 and 39.33 and longitudes between -76.71 and -76.45. ·Data Cleaning Outliers: Some fields in the dataset have serious data missing, exceeding 50%, and it is impossible to use interpolation or other methods to supplement valid data. Therefore, we decided not to use these fields in subsequent modeling.

<!-- b000109 | prose | pages [5] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000110 | furniture | pages [5] -->
m

<!-- b000111 | furniture | pages [5] -->
m

<!-- b000112 | furniture | pages [5] -->
m

<!-- b000113 | furniture | pages [5] -->
m

<!-- b000114 | furniture | pages [5] -->
m

<!-- b000115 | furniture | pages [5] -->
m

<!-- b000116 | furniture | pages [5] -->
m

<!-- b000117 | furniture | pages [5] -->
m

<!-- b000118 | furniture | pages [5] -->
m

<!-- b000119 | furniture | pages [5] -->
m

<!-- b000120 | furniture | pages [5] -->
m

<!-- b000121 | furniture | pages [5] -->
m

<!-- b000122 | furniture | pages [5] -->
m

<!-- b000123 | furniture | pages [5] -->
m

<!-- b000124 | furniture | pages [5] -->
m

<!-- b000125 | furniture | pages [5] -->
m

<!-- b000126 | furniture | pages [5] -->
m

<!-- b000127 | furniture | pages [5] -->
m

<!-- b000128 | furniture | pages [5] -->
m

<!-- b000129 | furniture | pages [5] -->
m

<!-- b000130 | furniture | pages [5] -->
m

<!-- b000131 | furniture | pages [5] -->
m

<!-- b000132 | furniture | pages [5] -->
m

<!-- b000133 | furniture | pages [5] -->
m

<!-- b000134 | furniture | pages [5] -->
m

<!-- b000135 | furniture | pages [5] -->
m

<!-- b000136 | furniture | pages [5] -->
m

<!-- b000137 | furniture | pages [5] -->
m

<!-- b000138 | furniture | pages [5] -->
m

<!-- b000139 | furniture | pages [5] -->
m

<!-- b000140 | furniture | pages [5] -->
m

<!-- b000141 | furniture | pages [5] -->
m

<!-- b000142 | furniture | pages [5] -->
m

<!-- b000143 | furniture | pages [5] -->
m

<!-- b000144 | furniture | pages [5] -->
m

<!-- b000145 | furniture | pages [5] -->
m

<!-- b000146 | furniture | pages [5] -->
m

<!-- b000147 | furniture | pages [5] -->
m

<!-- b000148 | furniture | pages [5] -->
m

<!-- b000149 | furniture | pages [5] -->
m

<!-- b000150 | furniture | pages [5] -->
m

<!-- b000151 | furniture | pages [5] -->
m

<!-- b000152 | furniture | pages [5] -->
m

<!-- b000153 | furniture | pages [5] -->
m

<!-- b000154 | furniture | pages [5] -->
m

<!-- b000155 | furniture | pages [5] -->
m

<!-- b000156 | furniture | pages [5] -->
m

<!-- b000157 | furniture | pages [5] -->
m

<!-- b000158 | furniture | pages [5] -->
m

<!-- b000159 | furniture | pages [5] -->
m

<!-- b000160 | furniture | pages [5] -->
m

<!-- b000161 | furniture | pages [5] -->
m

<!-- b000162 | furniture | pages [5] -->
m

<!-- b000163 | furniture | pages [5] -->
m

<!-- b000164 | furniture | pages [5] -->
m

<!-- b000165 | furniture | pages [5] -->
m

<!-- b000166 | furniture | pages [5] -->
m

<!-- b000167 | furniture | pages [5] -->
m

<!-- b000168 | furniture | pages [5] -->
m

<!-- b000169 | furniture | pages [5] -->
m

<!-- b000170 | furniture | pages [5] -->
m

<!-- b000171 | furniture | pages [5] -->
m

<!-- b000172 | furniture | pages [5] -->
m

<!-- b000173 | furniture | pages [5] -->
m

<!-- b000174 | furniture | pages [5] -->
m

<!-- b000175 | furniture | pages [5] -->
m

<!-- b000176 | furniture | pages [5] -->
m

<!-- b000177 | furniture | pages [5] -->
m

<!-- b000178 | furniture | pages [5] -->
m

<!-- b000179 | furniture | pages [5] -->
m

<!-- b000180 | furniture | pages [5] -->
m

<!-- b000181 | furniture | pages [5] -->
m

<!-- b000182 | furniture | pages [5] -->
m

<!-- b000183 | furniture | pages [5] -->
m

<!-- b000184 | furniture | pages [5] -->
m

<!-- b000185 | furniture | pages [5] -->
m

<!-- b000186 | furniture | pages [5] -->
m

<!-- b000187 | furniture | pages [5] -->
m

<!-- b000188 | furniture | pages [5] -->
m

<!-- b000189 | furniture | pages [5] -->
m

<!-- b000190 | furniture | pages [5] -->
m

<!-- b000191 | furniture | pages [5] -->
m

<!-- b000192 | furniture | pages [5] -->
m

<!-- b000193 | furniture | pages [5] -->
m

<!-- b000194 | furniture | pages [5] -->
m

<!-- b000195 | furniture | pages [5] -->
m

<!-- b000196 | furniture | pages [5] -->
m

<!-- b000197 | furniture | pages [5] -->
m

<!-- b000198 | furniture | pages [5] -->
m

<!-- b000199 | furniture | pages [5] -->
m

<!-- b000200 | furniture | pages [5] -->
m

<!-- b000201 | furniture | pages [5] -->
m

<!-- b000202 | furniture | pages [5] -->
m

<!-- b000203 | furniture | pages [5] -->
m

<!-- b000204 | furniture | pages [5] -->
m

<!-- b000205 | furniture | pages [5] -->
m

<!-- b000206 | furniture | pages [5] -->
m

<!-- b000207 | furniture | pages [5] -->
m

<!-- b000208 | furniture | pages [5] -->
m

<!-- b000209 | furniture | pages [5] -->
m

<!-- b000210 | furniture | pages [5] -->
m

<!-- b000211 | furniture | pages [5] -->
m

<!-- b000212 | furniture | pages [5] -->
m

<!-- b000213 | furniture | pages [5] -->
m

<!-- b000214 | furniture | pages [5] -->
m

<!-- b000215 | furniture | pages [5] -->
m

<!-- b000216 | furniture | pages [5] -->
m

<!-- b000217 | furniture | pages [5] -->
m

<!-- b000218 | furniture | pages [5] -->
m

<!-- b000219 | furniture | pages [5] -->
m

<!-- b000220 | furniture | pages [5] -->
m

<!-- b000221 | furniture | pages [5] -->
m

<!-- b000222 | furniture | pages [5] -->
m

<!-- b000223 | furniture | pages [5] -->
m

<!-- b000224 | furniture | pages [5] -->
m

<!-- b000225 | furniture | pages [5] -->
m

<!-- b000226 | furniture | pages [5] -->
m

<!-- b000227 | furniture | pages [5] -->
m

<!-- b000228 | furniture | pages [5] -->
m

<!-- b000229 | furniture | pages [5] -->
m

<!-- b000230 | furniture | pages [5] -->
m

<!-- b000231 | furniture | pages [5] -->
m

<!-- b000232 | furniture | pages [5] -->
m

<!-- b000233 | furniture | pages [5] -->
m

<!-- b000234 | furniture | pages [5] -->
m

<!-- b000235 | furniture | pages [5] -->
m

<!-- b000236 | furniture | pages [5] -->
m

<!-- b000237 | furniture | pages [5] -->
m

<!-- b000238 | furniture | pages [5] -->
m

<!-- b000239 | furniture | pages [5] -->
m

<!-- b000240 | furniture | pages [5] -->
m

<!-- b000241 | furniture | pages [5] -->
m

<!-- b000242 | furniture | pages [5] -->
m

<!-- b000243 | furniture | pages [5] -->
m

<!-- b000244 | furniture | pages [5] -->
m

<!-- b000245 | furniture | pages [5] -->
m

<!-- b000246 | furniture | pages [5] -->
m

<!-- b000247 | furniture | pages [5] -->
m

<!-- b000248 | furniture | pages [5] -->
m

<!-- b000249 | furniture | pages [5] -->
m

<!-- b000250 | furniture | pages [5] -->
m

<!-- b000251 | furniture | pages [5] -->
m

<!-- b000252 | furniture | pages [5] -->
m

<!-- b000253 | furniture | pages [5] -->
m

<!-- b000254 | furniture | pages [5] -->
m

<!-- b000255 | furniture | pages [5] -->
m

<!-- b000256 | furniture | pages [5] -->
m

<!-- b000257 | furniture | pages [5] -->
m

<!-- b000258 | furniture | pages [5] -->
m

<!-- b000259 | furniture | pages [5] -->
m

<!-- b000260 | furniture | pages [5] -->
m

<!-- b000261 | furniture | pages [5] -->
m

<!-- b000262 | furniture | pages [5] -->
m

<!-- b000263 | furniture | pages [5] -->
m

<!-- b000264 | furniture | pages [5] -->
m

<!-- b000265 | furniture | pages [5] -->
m

<!-- b000266 | furniture | pages [5] -->
m

<!-- b000267 | furniture | pages [5] -->
m

<!-- b000268 | furniture | pages [5] -->
m

<!-- b000269 | furniture | pages [5] -->
m

<!-- b000270 | furniture | pages [5] -->
m

<!-- b000271 | furniture | pages [5] -->
m

<!-- b000272 | furniture | pages [5] -->
m

<!-- b000273 | furniture | pages [5] -->
m

<!-- b000274 | furniture | pages [5] -->
m

<!-- b000275 | furniture | pages [5] -->
m

<!-- b000276 | furniture | pages [5] -->
m

<!-- b000277 | furniture | pages [5] -->
m

<!-- b000278 | furniture | pages [5] -->
m

<!-- b000279 | furniture | pages [5] -->
m

<!-- b000280 | furniture | pages [5] -->
m

<!-- b000281 | furniture | pages [5] -->
m

<!-- b000282 | furniture | pages [5] -->
m

<!-- b000283 | furniture | pages [5] -->
m

<!-- b000284 | furniture | pages [5] -->
m

<!-- b000285 | furniture | pages [5] -->
m

<!-- b000286 | furniture | pages [5] -->
m

<!-- b000287 | furniture | pages [5] -->
m

<!-- b000288 | furniture | pages [5] -->
m

<!-- b000289 | furniture | pages [5] -->
m

<!-- b000290 | furniture | pages [5] -->
m

<!-- b000291 | furniture | pages [5] -->
m

<!-- b000292 | furniture | pages [5] -->
m

<!-- b000293 | furniture | pages [5] -->
m

<!-- b000294 | furniture | pages [5] -->
m

<!-- b000295 | furniture | pages [5] -->
m

<!-- b000296 | furniture | pages [5] -->
m

<!-- b000297 | furniture | pages [5] -->
m

<!-- b000298 | furniture | pages [5] -->
m

<!-- b000299 | furniture | pages [5] -->
m

<!-- b000300 | furniture | pages [5] -->
m

<!-- b000301 | furniture | pages [5] -->
m

<!-- b000302 | furniture | pages [5] -->
m

<!-- b000303 | furniture | pages [5] -->
m

<!-- b000304 | furniture | pages [5] -->
m

<!-- b000305 | furniture | pages [5] -->
m

<!-- b000306 | furniture | pages [5] -->
m

<!-- b000307 | furniture | pages [5] -->
m

<!-- b000308 | furniture | pages [5] -->
m

<!-- b000309 | furniture | pages [5] -->
m

<!-- b000310 | furniture | pages [5] -->
m

<!-- b000311 | furniture | pages [5] -->
m

<!-- b000312 | furniture | pages [5] -->
m

<!-- b000313 | furniture | pages [5] -->
m

<!-- b000314 | furniture | pages [5] -->
m

<!-- b000315 | furniture | pages [5] -->
m

<!-- b000316 | furniture | pages [5] -->
m

<!-- b000317 | furniture | pages [5] -->
m

<!-- b000318 | furniture | pages [5] -->
m

<!-- b000319 | furniture | pages [5] -->
m

<!-- b000320 | furniture | pages [5] -->
m

<!-- b000321 | furniture | pages [5] -->
m

<!-- b000322 | furniture | pages [5] -->
m

<!-- b000323 | furniture | pages [5] -->
m

<!-- b000324 | furniture | pages [5] -->
m

<!-- b000325 | furniture | pages [5] -->
m

<!-- b000326 | furniture | pages [5] -->
m

<!-- b000327 | furniture | pages [5] -->
m

<!-- b000328 | furniture | pages [5] -->
m

<!-- b000329 | furniture | pages [5] -->
m

<!-- b000330 | furniture | pages [5] -->
m

<!-- b000331 | furniture | pages [5] -->
m

<!-- b000332 | furniture | pages [5] -->
m

<!-- b000333 | furniture | pages [5] -->
m

<!-- b000334 | furniture | pages [5] -->
m

<!-- b000335 | furniture | pages [5] -->
m

<!-- b000336 | furniture | pages [5] -->
m

<!-- b000337 | furniture | pages [5] -->
m

<!-- b000338 | furniture | pages [5] -->
m

<!-- b000339 | furniture | pages [5] -->
m

<!-- b000340 | furniture | pages [5] -->
m

<!-- b000341 | furniture | pages [5] -->
m

<!-- b000342 | furniture | pages [5] -->
m

<!-- b000343 | furniture | pages [5] -->
m

<!-- b000344 | furniture | pages [5] -->
m

<!-- b000345 | furniture | pages [5] -->
m

<!-- b000346 | furniture | pages [5] -->
m

<!-- b000347 | furniture | pages [5] -->
m

<!-- b000348 | furniture | pages [5] -->
m

<!-- b000349 | furniture | pages [5] -->
m

<!-- b000350 | furniture | pages [5] -->
m

<!-- b000351 | furniture | pages [5] -->
m

<!-- b000352 | furniture | pages [5] -->
m

<!-- b000353 | furniture | pages [5] -->
m

<!-- b000354 | furniture | pages [5] -->
m

<!-- b000355 | furniture | pages [5] -->
m

<!-- b000356 | furniture | pages [5] -->
m

<!-- b000357 | furniture | pages [5] -->
m

<!-- b000358 | furniture | pages [5] -->
m

<!-- b000359 | furniture | pages [5] -->
m

<!-- b000360 | furniture | pages [5] -->
m

<!-- b000361 | furniture | pages [5] -->
m

<!-- b000362 | furniture | pages [5] -->
m

<!-- b000363 | furniture | pages [5] -->
m

<!-- b000364 | furniture | pages [5] -->
m

<!-- b000365 | furniture | pages [5] -->
m

<!-- b000366 | furniture | pages [5] -->
m

<!-- b000367 | furniture | pages [5] -->
m

<!-- b000368 | furniture | pages [5] -->
m

<!-- b000369 | furniture | pages [5] -->
m

<!-- b000370 | furniture | pages [5] -->
m

<!-- b000371 | furniture | pages [5] -->
m

<!-- b000372 | furniture | pages [5] -->
m

<!-- b000373 | furniture | pages [5] -->
m

<!-- b000374 | furniture | pages [5] -->
m

<!-- b000375 | furniture | pages [5] -->
m

<!-- b000376 | furniture | pages [5] -->
m

<!-- b000377 | furniture | pages [5] -->
m

<!-- b000378 | furniture | pages [5] -->
m

<!-- b000379 | furniture | pages [5] -->
m

<!-- b000380 | furniture | pages [5] -->
m

<!-- b000381 | furniture | pages [5] -->
m

<!-- b000382 | furniture | pages [5] -->
m

<!-- b000383 | furniture | pages [5] -->
m

<!-- b000384 | furniture | pages [5] -->
m

<!-- b000385 | furniture | pages [5] -->
m

<!-- b000386 | furniture | pages [5] -->
m

<!-- b000387 | furniture | pages [5] -->
m

<!-- b000388 | furniture | pages [5] -->
m

<!-- b000389 | furniture | pages [5] -->
m

<!-- b000390 | furniture | pages [5] -->
m

<!-- b000391 | furniture | pages [5] -->
m

<!-- b000392 | furniture | pages [5] -->
m

<!-- b000393 | furniture | pages [5] -->
m

<!-- b000394 | furniture | pages [5] -->
m

<!-- b000395 | furniture | pages [5] -->
m

<!-- b000396 | furniture | pages [5] -->
m

<!-- b000397 | furniture | pages [5] -->
m

<!-- b000398 | furniture | pages [5] -->
m

<!-- b000399 | furniture | pages [5] -->
m

<!-- b000400 | furniture | pages [5] -->
m

<!-- b000401 | furniture | pages [5] -->
m

<!-- b000402 | furniture | pages [5] -->
m

<!-- b000403 | furniture | pages [5] -->
m

<!-- b000404 | furniture | pages [5] -->
m

<!-- b000405 | furniture | pages [5] -->
m

<!-- b000406 | furniture | pages [5] -->
m

<!-- b000407 | furniture | pages [5] -->
m

<!-- b000408 | furniture | pages [5] -->
m

<!-- b000409 | furniture | pages [5] -->
m

<!-- b000410 | furniture | pages [5] -->
m

<!-- b000411 | furniture | pages [5] -->
m

<!-- b000412 | furniture | pages [5] -->
m

<!-- b000413 | furniture | pages [5] -->
m

<!-- b000414 | furniture | pages [5] -->
m

<!-- b000415 | furniture | pages [5] -->
m

<!-- b000416 | furniture | pages [5] -->
m

<!-- b000417 | furniture | pages [5] -->
m

<!-- b000418 | furniture | pages [5] -->
m

<!-- b000419 | furniture | pages [5] -->
m

<!-- b000420 | furniture | pages [5] -->
m

<!-- b000421 | furniture | pages [5] -->
m

<!-- b000422 | furniture | pages [5] -->
m

<!-- b000423 | furniture | pages [5] -->
m

<!-- b000424 | furniture | pages [5] -->
m

<!-- b000425 | furniture | pages [5] -->
m

<!-- b000426 | furniture | pages [5] -->
m

<!-- b000427 | furniture | pages [5] -->
m

<!-- b000428 | furniture | pages [5] -->
m

<!-- b000429 | furniture | pages [5] -->
m

<!-- b000430 | furniture | pages [5] -->
m

<!-- b000431 | furniture | pages [5] -->
m

<!-- b000432 | furniture | pages [5] -->
m

<!-- b000433 | furniture | pages [5] -->
m

<!-- b000434 | furniture | pages [6] -->
Team # 2504188

<!-- b000435 | furniture | pages [6] -->
Page 6 of 25

<!-- b000436 | heading | pages [6] -->
5 Bridge Collapse Impact Quantification Model

<!-- b000437 | heading | pages [6] -->
5.1 Network model building and visualization

<!-- b000438 | prose | pages [6] -->
To clearly understand the actual traffic situation in Baltimore, we first need to build a transportation network. In the city’s spatial structure, intersections and turning points play a significant role. From the perspective of the road network and daily lo-cations, they are intuitive and easily identifiable. In terms of the relationship between buildings and roads, small building clusters are typically surrounded by intersections. When constructing the graph model, these intersections serve as nodes, simulating brain cognition to make the model more realistic and provide a more practical per-spective for urban space analysis.The intersections and turning points of the path are taken as nodes of the traffic network, recorded as the set 푁표푑푒푠= {푛표푑푒푖} .The path is taken as the edge of the traffic network, recorded as the set 퐸푑푔푒푠= {푒푑푔푒푠푖}.The starting point u and the ending node v of the path can both be found in the set Node, that is, 푢, 푣∈푁표푑푒.The time required to pass the path is taken as the weight, that is, 푊= {푇푖푚푒푖}.

<!-- b000439 | prose | pages [6] -->
Here's a visualization of the entire Baltimore transit network.

<!-- b000440 | caption | pages [6] -->
Figure 3: Baltimore Transportation Network

<!-- b000441 | prose | pages [6] -->
The different colored nodes in the diagram represent various types of road inter-sections, corresponding to the "highway" column in the edges_all dataset. The width of the edges reflects the weight, which represents the significance of each road. In general, the weight of an edge is closely related to the importance of the road, with higher weights indicating main roads. Since major roads experience heavier traffic and are more prone to congestion, vehicles tend to spend more time traveling through these areas. From the diagram, it’s evident that Baltimore’s urban traffic network is

<!-- b000442 | prose | pages [6, 7] -->
关注数学模型 highly complex, with a dense web of roads, which could potentially impact traffic safety.

<!-- b000443 | furniture | pages [6] -->
2

<!-- b000444 | furniture | pages [6] -->
MATHmodels

<!-- b000445 | furniture | pages [6] -->
获取更多资讯

<!-- b000446 | furniture | pages [7] -->
Team # 2504188

<!-- b000447 | furniture | pages [7] -->
Page 7 of 25

<!-- b000449 | prose | pages [7] -->
Traditional network graphs are difficult to visually present the absolute position relationship between nodes. To overcome this limitation, we build a search set 푑푖푐푡= {[표푠푚푖푑, 푙푎푡푖푡푢푑푒, 푙표푛푔푖푡푢푑푒]} based on the dataset nodes_all. Each item in the set contains a node unique 微信公众号：数学模型 identifier (osmid) and a geographic location, providing a basis for mapping nodes to actual locations. By searching the set to determine the location of each node on the actual map, the abstract network graph is closely associated with the real geographic space. The result is shown in Figure 4.

<!-- b000450 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000451 | caption | pages [7] -->
Figure 4: Transportation map

<!-- b000452 | heading | pages [7] -->
5.2 Quantification of impact indicators

<!-- b000453 | prose | pages [7] -->
The collapse of the Francis Scott Key Bridge had a significant impact on city residents, business owners, suburban residents, commuters, passthrough travelers, and tourists. These impacts can be categorized into common and individual aspects. From a common perspective, the collapse forced all individuals who originally relied on the bridge to find alternative routes. This change led to a surge in traffic on other routes, causing congestion. This negative effect is consistent across all stakeholders, as it di-rectly disrupted daily commutes, goods transportation, and travel plans. However, the detour’s shortest path varies depending on factors such as travel mode, destination, and time of travel, reflecting the individual impacts on each stakeholder.

<!-- b000454 | heading | pages [7] -->
1. Common Impacts

<!-- b000455 | prose | pages [7] -->
A. Congestion Index The Francis Scott Key Bridge is a suburban fortress in Baltimore, with a large amount of traffic every day. After the bridge collapsed, vehicles that originally passed through the bridge had to take a detour, which would increase the traffic volume on other traffic routes and would greatly cause traffic congestion. Therefore, we use the queuing theory (MMC) model to measure the changes in the congestion index of other routes around the bridge. In the previous article, we demonstrated the rationality of Assumption 1, so we believe that vehicle arrivals follow a Poisson distribution. Taking into account realistic factors, we have improved the queuing theory model. The state formula of the queuing theory is as follows:

<!-- b000456 | furniture | pages [8] -->
Page 8 of 25

<!-- b000457 | furniture | pages [8] -->
Team # 2504188

<!-- b000458 | prose | pages [8] -->
2 /n! μ (1) Pn k λ /k! μ k=0 Where Pn represents the state probability distribution, c represents the number of lanes, and k represents the correction factor, which is related to the road type. λ represents the number of vehicles arriving per unit time. Here we take the unit time as 1 hour and use the AADT field data in the dataset “MDOT"to calculate.

<!-- b000459 | prose | pages [8] -->
AADT (2) λ= 24

<!-- b000460 | prose | pages [8] -->
μ indicates the number of vehicles passing through the road per unit time, which is inversely proportional to the time it takes a vehicle to pass through the road section.

<!-- b000461 | prose | pages [8] -->
1 ν (3) = n1 L T

<!-- b000462 | prose | pages [8] -->
Where L represents the length of the road section, and v represents the driving speed of the road section. Generally speaking, different types of road sections have different speeds. We supplemented the data based on the ClassCode data representing the road section type in the table.

<!-- b000463 | caption | pages [8] -->
Table2: Speed limit table for each type of road

<!-- b000464 | prose | pages [8] -->
v(m·s−1) Class Name Class Code 65~75 Interstate 1 2/3 60~70 Principal Arterial 35~45 4 Minor Arterial 40~50 5 Major Collector 30~40 6 Minor Collector 25~40 Local 7 For the MMC queuing system, we can calculate its average queue length.

<!-- b000465 | prose | pages [8] -->
C λ 1 1 2 io μ λ cμ (4) Ⅱ k λ μ 3 k! k=0 We use the average queue length as the congestion index of the road section. The longer the average queue length, the more congested the road section is.

<!-- b000466 | heading | pages [8] -->
2. Individual Impacts

<!-- b000467 | prose | pages [8] -->
We mainly use Accessibility to quantify the interests among various stakeholders.

<!-- b000468 | prose | pages [8, 9] -->
关注数学模型 Accessibility is denoted as the function of measuring interests,Co is the community, Ci is the city,Bi is the enterprise,Si is the suburb,Mi is the urban edge,Ai is the area with concentrated scenic spots, and Pi is the port and shipping center.

<!-- b000469 | furniture | pages [8] -->
获取更多资讯

<!-- b000470 | furniture | pages [9] -->
Page 9 of 25

<!-- b000471 | furniture | pages [9] -->
Team # 2504188

<!-- b000473 | prose | pages [9] -->
tourists

<!-- b000474 | prose | pages [9] -->
stakeholders

<!-- b000475 | prose | pages [9] -->
Office locatic

<!-- b000476 | prose | pages [9] -->
Within the city

<!-- b000477 | caption | pages [9] -->
Figure 5: Metrics for measuring stakeholders

<!-- b000478 | prose | pages [9] -->
B.Residents The Francis Scott Key Bridge plays a crucial role as a connective link in Baltimore's urban spatial structure, primarily linking the city to the suburbs. Based on this charac-teristic, we can divide residents into city and suburban categories.

<!-- b000479 | prose | pages [9] -->
a.Urban Residents The port and shipping center are located far from the city, making it difficult for city residents to access related jobs. The bridge collapse affects port operations, and its reconstruction is essential to restore connectivity. The accessibility between the city and the portinfluences both employment opportunities and the residents' daily lives. Additionally, city residents often travel between communities, making in-ter-community accessibility important. The bridge's reconstruction should avoid cre-ating barriers between communities to prevent reducing travel efficiency and nega-tively impacting residents' quality of life.

<!-- b000480 | prose | pages [9] -->
(5) BC = Accessibility(Co j, Pi) + Accessibility(Co j, Cok) ● b.Suburbanites Suburban residents often work, entertain, and seek medical care in the city, mak-ing frequent trips between the city and the suburbs. The accessibility from the city to the suburbs affects travel costs, which in turn impacts the quality of life and work efficiency. Poor accessibility leads to longer commute times, reducing overall well-being, while better accessibility saves time and could even drive suburban real estate development.

<!-- b000481 | prose | pages [9] -->
(6) BS = Accessibility(Ci, Sj)

<!-- b000482 | furniture | pages [10] -->
Team # 2504188

<!-- b000483 | furniture | pages [10] -->
Page 10 of 25

<!-- b000484 | heading | pages [10] -->
C. Commuters

<!-- b000485 | prose | pages [10] -->
Most commuters live and work within the city, so the city's transportation layout affects their commute time. Good internal accessibility in the city shortens commute times, improves work-life efficiency, reduces commuter fatigue, and enhances overall satisfaction with both work and life.

<!-- b000486 | prose | pages [10] -->
(7) ( , ) BM Accessibility C C  i j

<!-- b000487 | prose | pages [10] -->
D.Transit passengers Travelers with intercity needs, such as those connecting flights or buses, or on cross-city road trips, are impacted by the accessibility between the urban fringes. Poor accessibility can lead to missed connections and higher costs, while good accessibility ensures a smooth journey and improves the overall impression of the city.

<!-- b000488 | prose | pages [10] -->
(8) ( , ) BP Accessibility M M  i j

<!-- b000489 | prose | pages [10] -->
E.Visitors Tourists often visit multiple attractions in a single day, and the accessibility be-tween these attractions affects their experience and time management. Good connec-tivity allows tourists to move between attractions more easily, visit more sites, and have a higher level of satisfaction. On the other hand, poor connectivity may lead them to skip some attractions, reducing the overall experience. We quantify the bene-fits for tourists based on the accessibility between these attractions.

<!-- b000490 | prose | pages [10] -->
(9) ( , ) BT Accessibility A A  i j

<!-- b000491 | prose | pages [10] -->
F. Entrepreneur The accessibility from businesses to communities affects entrepreneurs' business strategies and operational costs. External connectivity also plays a key role in deter-mining logistics costs and market expansion efficiency. For example, good connectiv-ity with the port reduces logistics costs, while strong connections with other cities fa-cilitate collaboration opportunities.

<!-- b000492 | prose | pages [10] -->
(10) ( , ) BB Accessibility B Co  i j

<!-- b000493 | heading | pages [10] -->
5.3 Accessibility definition and solution

<!-- b000494 | prose | pages [10] -->
The function is used to calculate the shortest path between regions. In the specific calculation process, we innovatively combine the A* algorithm with the genetic algorithm to improve both efficiency and accuracy. The improved A* heuristic cost function is as follows:

<!-- b000495 | prose | pages [10] -->
(11) ( ) ( ) ( ) f  n g n h n    

<!-- b000496 | prose | pages [10] -->
Where 훼represents the weighted parameter, 푔(푛) represents the sum of the weights of the paths, and ℎ(푛) is the heuristic distance. We usually think that the cost of

<!-- b000497 | prose | pages [10, 11] -->
关注数学模型 getting from one place to another is not only related to the weight, but also to the spatial distance. We use the Haversine formula to measure the spatial distance between two points on the sphere.

<!-- b000498 | furniture | pages [10] -->
2

<!-- b000499 | furniture | pages [10] -->
MATHmodels

<!-- b000500 | furniture | pages [10] -->
获取更多资讯

<!-- b000501 | furniture | pages [11] -->
Team # 2504188

<!-- b000502 | furniture | pages [11] -->
Page 11 of 25

<!-- b000504 | prose | pages [11] -->
(12)   2 1 2 1 La La Lon Lon       2 2 2 1 2 ( ) asin sin cos( ) cos( ) sin h n R L L              2 2       微信公众号：数学模型 Where 퐿푎1 and 퐿푎2 represent the latitude (푟푎푑) between two points, and 퐿표푛1 and 퐿표푛2 represent the longitude (푟푎푑) between two points.

<!-- b000505 | prose | pages [11] -->
The fitness is calculated as follows.

<!-- b000506 | prose | pages [11] -->
1 1 ( ) fitness P   (13) 1 k  ( ) g n  ( , ) w v v 1 i i  1 i 

<!-- b000507 | prose | pages [11] -->
The selection probability is calculated as follows.

<!-- b000508 | prose | pages [11] -->
微信号：MATHmodels  fitness P i (14) p  i N    fitness P j 1 j 

<!-- b000509 | prose | pages [11] -->
The specific algorithm design ideas are given in pseudocode form.

<!-- b000510 | heading | pages [11] -->
Algorithm 1 A* and GA

<!-- b000511 | prose | pages [11] -->
Input: Baltimore transportation network graph, A List of starting and ending points Output: A set of shortest paths 1: for search in List do 2: Use the A* algorithm to search for a path as a better initial population for the genetic algorithm.

<!-- b000512 | prose | pages [11] -->
for generation in 100 do 3:

<!-- b000513 | prose | pages [11] -->
path1,path2=the last two parent paths generated 4:

<!-- b000514 | prose | pages [11] -->
child= combine path1 and path2 5:

<!-- b000515 | prose | pages [11] -->
if len(path) > 2 and random.random() < self.mutation_rate do 6: 7: Swap two nodes and recalculate the path end if 8:

<!-- b000516 | prose | pages [11] -->
best_path=The path with the highest fitness 9:

<!-- b000517 | prose | pages [11] -->
best_cost=The cost of the best path 10:

<!-- b000518 | prose | pages [11] -->
end for 11: 12: Add the shortest path to the result set ans 13: end for 14: return ans

<!-- b000519 | heading | pages [11] -->
5.4 Bridge collapse data processing

<!-- b000520 | prose | pages [11] -->
The Francis Scott Key Bridge is a transportation hub in Baltimore, mainly used to connect the city with external areas.

<!-- b000521 | prose | pages [11, 12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Therefore, in the dataset edges_all, the ref column records the reference code of the road. The path number of the Francis Scott Key Bridge is 푟푒푓= 퐼695. The osmid represents the path or relationship to which the edge belongs, which is the unique identifier of the road segment. We use the path number to find the osmid of all sections of the Francis Scott Key Bridge and put them in set 퐴. We believe that the collapse of this bridge has made all sections containing this bridge impassable, so all osmids in 푒푑푔푒_푎푙푙are compared with the elements in set 퐴. If the 표푠푚푖푑휖퐴, delete this edge.

<!-- b000522 | furniture | pages [11] -->
m

<!-- b000523 | furniture | pages [11] -->
m

<!-- b000524 | furniture | pages [11] -->
m

<!-- b000525 | furniture | pages [11] -->
m

<!-- b000526 | furniture | pages [11] -->
m

<!-- b000527 | furniture | pages [11] -->
m

<!-- b000528 | furniture | pages [11] -->
m

<!-- b000529 | furniture | pages [11] -->
m

<!-- b000530 | furniture | pages [11] -->
m

<!-- b000531 | furniture | pages [11] -->
m

<!-- b000532 | furniture | pages [11] -->
m

<!-- b000533 | furniture | pages [11] -->
m

<!-- b000534 | furniture | pages [11] -->
m

<!-- b000535 | furniture | pages [11] -->
m

<!-- b000536 | furniture | pages [11] -->
m

<!-- b000537 | furniture | pages [11] -->
m

<!-- b000538 | furniture | pages [11] -->
m

<!-- b000539 | furniture | pages [11] -->
m

<!-- b000540 | furniture | pages [11] -->
m

<!-- b000541 | furniture | pages [11] -->
m

<!-- b000542 | furniture | pages [11] -->
m

<!-- b000543 | furniture | pages [11] -->
m

<!-- b000544 | furniture | pages [11] -->
m

<!-- b000545 | furniture | pages [11] -->
m

<!-- b000546 | furniture | pages [11] -->
m

<!-- b000547 | furniture | pages [11] -->
m

<!-- b000548 | furniture | pages [11] -->
m

<!-- b000549 | furniture | pages [11] -->
m

<!-- b000550 | furniture | pages [11] -->
m

<!-- b000551 | furniture | pages [11] -->
m

<!-- b000552 | furniture | pages [11] -->
m

<!-- b000553 | furniture | pages [11] -->
m

<!-- b000554 | furniture | pages [11] -->
m

<!-- b000555 | furniture | pages [11] -->
m

<!-- b000556 | furniture | pages [11] -->
m

<!-- b000557 | furniture | pages [11] -->
m

<!-- b000558 | furniture | pages [11] -->
m

<!-- b000559 | furniture | pages [11] -->
m

<!-- b000560 | furniture | pages [11] -->
m

<!-- b000561 | furniture | pages [11] -->
m

<!-- b000562 | furniture | pages [11] -->
m

<!-- b000563 | furniture | pages [11] -->
m

<!-- b000564 | furniture | pages [11] -->
m

<!-- b000565 | furniture | pages [11] -->
m

<!-- b000566 | furniture | pages [11] -->
m

<!-- b000567 | furniture | pages [11] -->
m

<!-- b000568 | furniture | pages [11] -->
m

<!-- b000569 | furniture | pages [11] -->
m

<!-- b000570 | furniture | pages [11] -->
m

<!-- b000571 | furniture | pages [11] -->
m

<!-- b000572 | furniture | pages [11] -->
m

<!-- b000573 | furniture | pages [11] -->
m

<!-- b000574 | furniture | pages [11] -->
m

<!-- b000575 | furniture | pages [11] -->
m

<!-- b000576 | furniture | pages [11] -->
m

<!-- b000577 | furniture | pages [11] -->
m

<!-- b000578 | furniture | pages [11] -->
m

<!-- b000579 | furniture | pages [11] -->
m

<!-- b000580 | furniture | pages [11] -->
m

<!-- b000581 | furniture | pages [11] -->
m

<!-- b000582 | furniture | pages [11] -->
m

<!-- b000583 | furniture | pages [11] -->
m

<!-- b000584 | furniture | pages [11] -->
m

<!-- b000585 | furniture | pages [11] -->
m

<!-- b000586 | furniture | pages [11] -->
m

<!-- b000587 | furniture | pages [11] -->
m

<!-- b000588 | furniture | pages [11] -->
m

<!-- b000589 | furniture | pages [11] -->
m

<!-- b000590 | furniture | pages [11] -->
m

<!-- b000591 | furniture | pages [11] -->
m

<!-- b000592 | furniture | pages [11] -->
m

<!-- b000593 | furniture | pages [11] -->
m

<!-- b000594 | furniture | pages [11] -->
m

<!-- b000595 | furniture | pages [11] -->
m

<!-- b000596 | furniture | pages [11] -->
m

<!-- b000597 | furniture | pages [11] -->
m

<!-- b000598 | furniture | pages [11] -->
m

<!-- b000599 | furniture | pages [11] -->
m

<!-- b000600 | furniture | pages [11] -->
m

<!-- b000601 | furniture | pages [11] -->
m

<!-- b000602 | furniture | pages [11] -->
m

<!-- b000603 | furniture | pages [11] -->
m

<!-- b000604 | furniture | pages [11] -->
m

<!-- b000605 | furniture | pages [11] -->
m

<!-- b000606 | furniture | pages [11] -->
m

<!-- b000607 | furniture | pages [11] -->
m

<!-- b000608 | furniture | pages [11] -->
m

<!-- b000609 | furniture | pages [11] -->
m

<!-- b000610 | furniture | pages [11] -->
m

<!-- b000611 | furniture | pages [11] -->
m

<!-- b000612 | furniture | pages [11] -->
m

<!-- b000613 | furniture | pages [11] -->
m

<!-- b000614 | furniture | pages [11] -->
m

<!-- b000615 | furniture | pages [11] -->
m

<!-- b000616 | furniture | pages [11] -->
m

<!-- b000617 | furniture | pages [11] -->
m

<!-- b000618 | furniture | pages [11] -->
m

<!-- b000619 | furniture | pages [11] -->
m

<!-- b000620 | furniture | pages [11] -->
m

<!-- b000621 | furniture | pages [11] -->
m

<!-- b000622 | furniture | pages [11] -->
m

<!-- b000623 | furniture | pages [11] -->
m

<!-- b000624 | furniture | pages [11] -->
m

<!-- b000625 | furniture | pages [11] -->
m

<!-- b000626 | furniture | pages [11] -->
m

<!-- b000627 | furniture | pages [11] -->
m

<!-- b000628 | furniture | pages [11] -->
m

<!-- b000629 | furniture | pages [11] -->
m

<!-- b000630 | furniture | pages [11] -->
m

<!-- b000631 | furniture | pages [11] -->
m

<!-- b000632 | furniture | pages [11] -->
m

<!-- b000633 | furniture | pages [11] -->
m

<!-- b000634 | furniture | pages [11] -->
m

<!-- b000635 | furniture | pages [11] -->
m

<!-- b000636 | furniture | pages [11] -->
m

<!-- b000637 | furniture | pages [11] -->
m

<!-- b000638 | furniture | pages [11] -->
m

<!-- b000639 | furniture | pages [11] -->
m

<!-- b000640 | furniture | pages [11] -->
m

<!-- b000641 | furniture | pages [11] -->
m

<!-- b000642 | furniture | pages [11] -->
m

<!-- b000643 | furniture | pages [11] -->
m

<!-- b000644 | furniture | pages [11] -->
m

<!-- b000645 | furniture | pages [11] -->
m

<!-- b000646 | furniture | pages [11] -->
m

<!-- b000647 | furniture | pages [11] -->
m

<!-- b000648 | furniture | pages [11] -->
m

<!-- b000649 | furniture | pages [11] -->
m

<!-- b000650 | furniture | pages [11] -->
m

<!-- b000651 | furniture | pages [11] -->
m

<!-- b000652 | furniture | pages [11] -->
m

<!-- b000653 | furniture | pages [11] -->
m

<!-- b000654 | furniture | pages [11] -->
m

<!-- b000655 | furniture | pages [11] -->
m

<!-- b000656 | furniture | pages [11] -->
m

<!-- b000657 | furniture | pages [11] -->
m

<!-- b000658 | furniture | pages [11] -->
m

<!-- b000659 | furniture | pages [11] -->
m

<!-- b000660 | furniture | pages [11] -->
m

<!-- b000661 | furniture | pages [11] -->
m

<!-- b000662 | furniture | pages [11] -->
m

<!-- b000663 | furniture | pages [11] -->
m

<!-- b000664 | furniture | pages [11] -->
m

<!-- b000665 | furniture | pages [11] -->
m

<!-- b000666 | furniture | pages [11] -->
m

<!-- b000667 | furniture | pages [11] -->
m

<!-- b000668 | furniture | pages [11] -->
m

<!-- b000669 | furniture | pages [11] -->
m

<!-- b000670 | furniture | pages [11] -->
m

<!-- b000671 | furniture | pages [11] -->
m

<!-- b000672 | furniture | pages [11] -->
m

<!-- b000673 | furniture | pages [11] -->
m

<!-- b000674 | furniture | pages [11] -->
m

<!-- b000675 | furniture | pages [11] -->
m

<!-- b000676 | furniture | pages [11] -->
m

<!-- b000677 | furniture | pages [11] -->
m

<!-- b000678 | furniture | pages [11] -->
m

<!-- b000679 | furniture | pages [11] -->
m

<!-- b000680 | furniture | pages [11] -->
m

<!-- b000681 | furniture | pages [11] -->
m

<!-- b000682 | furniture | pages [11] -->
m

<!-- b000683 | furniture | pages [11] -->
m

<!-- b000684 | furniture | pages [11] -->
m

<!-- b000685 | furniture | pages [11] -->
m

<!-- b000686 | furniture | pages [11] -->
m

<!-- b000687 | furniture | pages [11] -->
m

<!-- b000688 | furniture | pages [11] -->
m

<!-- b000689 | furniture | pages [11] -->
m

<!-- b000690 | furniture | pages [11] -->
m

<!-- b000691 | furniture | pages [11] -->
m

<!-- b000692 | furniture | pages [11] -->
m

<!-- b000693 | furniture | pages [11] -->
m

<!-- b000694 | furniture | pages [11] -->
m

<!-- b000695 | furniture | pages [11] -->
m

<!-- b000696 | furniture | pages [11] -->
m

<!-- b000697 | furniture | pages [11] -->
m

<!-- b000698 | furniture | pages [11] -->
m

<!-- b000699 | furniture | pages [11] -->
m

<!-- b000700 | furniture | pages [11] -->
m

<!-- b000701 | furniture | pages [11] -->
m

<!-- b000702 | furniture | pages [11] -->
m

<!-- b000703 | furniture | pages [11] -->
m

<!-- b000704 | furniture | pages [11] -->
m

<!-- b000705 | furniture | pages [11] -->
m

<!-- b000706 | furniture | pages [11] -->
m

<!-- b000707 | furniture | pages [11] -->
m

<!-- b000708 | furniture | pages [11] -->
m

<!-- b000709 | furniture | pages [11] -->
m

<!-- b000710 | furniture | pages [11] -->
m

<!-- b000711 | furniture | pages [11] -->
m

<!-- b000712 | furniture | pages [11] -->
m

<!-- b000713 | furniture | pages [11] -->
m

<!-- b000714 | furniture | pages [11] -->
m

<!-- b000715 | furniture | pages [11] -->
m

<!-- b000716 | furniture | pages [11] -->
m

<!-- b000717 | furniture | pages [11] -->
m

<!-- b000718 | furniture | pages [11] -->
m

<!-- b000719 | furniture | pages [11] -->
m

<!-- b000720 | furniture | pages [11] -->
m

<!-- b000721 | furniture | pages [11] -->
m

<!-- b000722 | furniture | pages [11] -->
m

<!-- b000723 | furniture | pages [11] -->
m

<!-- b000724 | furniture | pages [11] -->
m

<!-- b000725 | furniture | pages [11] -->
m

<!-- b000726 | furniture | pages [11] -->
m

<!-- b000727 | furniture | pages [11] -->
m

<!-- b000728 | furniture | pages [11] -->
m

<!-- b000729 | furniture | pages [11] -->
m

<!-- b000730 | furniture | pages [11] -->
m

<!-- b000731 | furniture | pages [11] -->
m

<!-- b000732 | furniture | pages [11] -->
m

<!-- b000733 | furniture | pages [11] -->
m

<!-- b000734 | furniture | pages [11] -->
m

<!-- b000735 | furniture | pages [11] -->
m

<!-- b000736 | furniture | pages [11] -->
m

<!-- b000737 | furniture | pages [11] -->
m

<!-- b000738 | furniture | pages [11] -->
m

<!-- b000739 | furniture | pages [11] -->
m

<!-- b000740 | furniture | pages [11] -->
m

<!-- b000741 | furniture | pages [11] -->
m

<!-- b000742 | furniture | pages [11] -->
m

<!-- b000743 | furniture | pages [11] -->
m

<!-- b000744 | furniture | pages [11] -->
m

<!-- b000745 | furniture | pages [11] -->
m

<!-- b000746 | furniture | pages [11] -->
m

<!-- b000747 | furniture | pages [11] -->
m

<!-- b000748 | furniture | pages [11] -->
m

<!-- b000749 | furniture | pages [11] -->
m

<!-- b000750 | furniture | pages [11] -->
m

<!-- b000751 | furniture | pages [11] -->
m

<!-- b000752 | furniture | pages [11] -->
m

<!-- b000753 | furniture | pages [11] -->
m

<!-- b000754 | furniture | pages [11] -->
m

<!-- b000755 | furniture | pages [11] -->
m

<!-- b000756 | furniture | pages [11] -->
m

<!-- b000757 | furniture | pages [11] -->
m

<!-- b000758 | furniture | pages [11] -->
m

<!-- b000759 | furniture | pages [11] -->
m

<!-- b000760 | furniture | pages [11] -->
m

<!-- b000761 | furniture | pages [11] -->
m

<!-- b000762 | furniture | pages [11] -->
m

<!-- b000763 | furniture | pages [11] -->
m

<!-- b000764 | furniture | pages [11] -->
m

<!-- b000765 | furniture | pages [11] -->
m

<!-- b000766 | furniture | pages [11] -->
m

<!-- b000767 | furniture | pages [11] -->
m

<!-- b000768 | furniture | pages [11] -->
m

<!-- b000769 | furniture | pages [11] -->
m

<!-- b000770 | furniture | pages [11] -->
m

<!-- b000771 | furniture | pages [11] -->
m

<!-- b000772 | furniture | pages [11] -->
m

<!-- b000773 | furniture | pages [11] -->
m

<!-- b000774 | furniture | pages [11] -->
m

<!-- b000775 | furniture | pages [11] -->
m

<!-- b000776 | furniture | pages [11] -->
m

<!-- b000777 | furniture | pages [11] -->
m

<!-- b000778 | furniture | pages [11] -->
m

<!-- b000779 | furniture | pages [11] -->
m

<!-- b000780 | furniture | pages [11] -->
m

<!-- b000781 | furniture | pages [11] -->
m

<!-- b000782 | furniture | pages [11] -->
m

<!-- b000783 | furniture | pages [11] -->
m

<!-- b000784 | furniture | pages [11] -->
m

<!-- b000785 | furniture | pages [11] -->
m

<!-- b000786 | furniture | pages [11] -->
m

<!-- b000787 | furniture | pages [11] -->
m

<!-- b000788 | furniture | pages [11] -->
m

<!-- b000789 | furniture | pages [11] -->
m

<!-- b000790 | furniture | pages [11] -->
m

<!-- b000791 | furniture | pages [11] -->
m

<!-- b000792 | furniture | pages [11] -->
m

<!-- b000793 | furniture | pages [11] -->
m

<!-- b000794 | furniture | pages [11] -->
m

<!-- b000795 | furniture | pages [11] -->
m

<!-- b000796 | furniture | pages [11] -->
m

<!-- b000797 | furniture | pages [11] -->
m

<!-- b000798 | furniture | pages [11] -->
m

<!-- b000799 | furniture | pages [11] -->
m

<!-- b000800 | furniture | pages [11] -->
m

<!-- b000801 | furniture | pages [11] -->
m

<!-- b000802 | furniture | pages [11] -->
m

<!-- b000803 | furniture | pages [11] -->
m

<!-- b000804 | furniture | pages [11] -->
m

<!-- b000805 | furniture | pages [11] -->
m

<!-- b000806 | furniture | pages [11] -->
m

<!-- b000807 | furniture | pages [11] -->
m

<!-- b000808 | furniture | pages [11] -->
m

<!-- b000809 | furniture | pages [11] -->
m

<!-- b000810 | furniture | pages [11] -->
m

<!-- b000811 | furniture | pages [11] -->
m

<!-- b000812 | furniture | pages [11] -->
m

<!-- b000813 | furniture | pages [11] -->
m

<!-- b000814 | furniture | pages [11] -->
m

<!-- b000815 | furniture | pages [11] -->
m

<!-- b000816 | furniture | pages [11] -->
m

<!-- b000817 | furniture | pages [11] -->
m

<!-- b000818 | furniture | pages [11] -->
m

<!-- b000819 | furniture | pages [11] -->
m

<!-- b000820 | furniture | pages [11] -->
m

<!-- b000821 | furniture | pages [11] -->
m

<!-- b000822 | furniture | pages [11] -->
m

<!-- b000823 | furniture | pages [11] -->
m

<!-- b000824 | furniture | pages [11] -->
m

<!-- b000825 | furniture | pages [11] -->
m

<!-- b000826 | furniture | pages [11] -->
m

<!-- b000827 | furniture | pages [11] -->
m

<!-- b000828 | furniture | pages [11] -->
m

<!-- b000829 | furniture | pages [11] -->
m

<!-- b000830 | furniture | pages [11] -->
m

<!-- b000831 | furniture | pages [11] -->
m

<!-- b000832 | furniture | pages [11] -->
m

<!-- b000833 | furniture | pages [11] -->
m

<!-- b000834 | furniture | pages [11] -->
m

<!-- b000835 | furniture | pages [11] -->
m

<!-- b000836 | furniture | pages [11] -->
m

<!-- b000837 | furniture | pages [11] -->
m

<!-- b000838 | furniture | pages [11] -->
m

<!-- b000839 | furniture | pages [11] -->
m

<!-- b000840 | furniture | pages [11] -->
m

<!-- b000841 | furniture | pages [11] -->
m

<!-- b000842 | furniture | pages [11] -->
m

<!-- b000843 | furniture | pages [11] -->
m

<!-- b000844 | furniture | pages [11] -->
m

<!-- b000845 | furniture | pages [11] -->
m

<!-- b000846 | furniture | pages [12] -->
Team # 2504188

<!-- b000847 | furniture | pages [12] -->
Page 12 of 25

<!-- b000849 | heading | pages [12] -->
5.5 Solution

<!-- b000850 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000851 | caption | pages [12] -->
Figure 6: Changes in transportation network

<!-- b000852 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The left figure represents the traffic network before the bridge collapse, while the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m right figure shows the traffic network after the collapse. Figure 6 illustrates that the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m collapse of the bridge has rendered many road segments impassable, significantly m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m re-ducing the number of accessible routes. We can also observe that most of the road construction around the bridge was primarily designed to facilitate travel between the city and the suburbs, but key connections between the two areas are limited. As a re-sult, the traffic network after the bridge collapse only maintains connectivity within a small area.

<!-- b000853 | caption | pages [12] -->
Figure 7: Congestion levels at different latitudes and longitudes

<!-- b000854 | prose | pages [12] -->
We calculated the degree of road congestion at different longitudes and latitudes every year. As can be seen from the figure, the changing trends in different years are roughly similar, which can be explained by the fact that the traffic volume on some

<!-- b000855 | prose | pages [12, 13] -->
关注数学模型 sections of the road is indeed greater than that on other sections, which is more likely to cause congestion. It also shows that the traffic layout in the Baltimore area has basically not changed in recent years. We can also know that the degree of congestion was the lowest in 2014, and since then the degree of congestion has basically shown an increasing trend year by year, which may be due to urban development and population growth. So far, the existing transportation network has been difficult to meet the needs of Baltimore. The congestion level in 2020 ranks first in the figure, which may be the impact of the new crown epidemic on the city, which is a relatively special change. Finally, the congestion level after the bridge collapsed was second only to 2020, which fully demonstrates the importance of the bridge in the transportation network. 微信公众号：数学模型 To verify and improve the interest measurement system, we conducted simulations. We focused on the area around the bridge collapse and randomly collected 100 data samples, which were divided into categories such as communities and cities according to their attributes. We used the established model to calculate the shortest path for 微信号：MATHmodels each category of data and depict the road sections. The results are shown in the figure on the right. We also calculated accessibility and scores for each

<!-- b000856 | furniture | pages [12] -->
2

<!-- b000857 | furniture | pages [12] -->
MATHmodels

<!-- b000858 | furniture | pages [12] -->
获取更多资讯

<!-- b000859 | furniture | pages [13] -->
Team # 2504188

<!-- b000860 | furniture | pages [13] -->
Page 13 of 25

<!-- b000862 | caption | pages [13] -->
Figure 8 Shortest path simulation

<!-- b000863 | prose | pages [13] -->
stakeholder based on this, and the results results are as follows.

<!-- b000864 | caption | pages [13] -->
Figure 9: Impact of the bridge collapse on stakeholders

<!-- b000865 | caption | pages [13] -->
Figure 9 shows the comparison of interest scores of various stakeholders before

<!-- b000866 | prose | pages [13] -->
and after the bridge collapsed. We use accessibility to measure the impact of bridge

<!-- b000867 | prose | pages [13, 14] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m collapse on stakeholders. Accessibility is determined by the time it takes for vehicles or pedestrians to pass through the road section. The longer the time, the greater the accessibility value and the more inconvenient the passage. As can be seen from the figure, the travel time of various stakeholders increased significantly after the bridge collapsed. Among them, suburban residents were most affected because there were few routes available between urban and suburban areas; urban residents were least affected because their daily activities were mostly in the urban area and they rarely traveled between urban and suburban areas.

<!-- b000868 | furniture | pages [13] -->
m

<!-- b000869 | furniture | pages [13] -->
m

<!-- b000870 | furniture | pages [13] -->
m

<!-- b000871 | furniture | pages [13] -->
m

<!-- b000872 | furniture | pages [13] -->
m

<!-- b000873 | furniture | pages [13] -->
m

<!-- b000874 | furniture | pages [13] -->
m

<!-- b000875 | furniture | pages [13] -->
m

<!-- b000876 | furniture | pages [13] -->
m

<!-- b000877 | furniture | pages [13] -->
m

<!-- b000878 | furniture | pages [13] -->
m

<!-- b000879 | furniture | pages [13] -->
m

<!-- b000880 | furniture | pages [13] -->
m

<!-- b000881 | furniture | pages [13] -->
m

<!-- b000882 | furniture | pages [13] -->
m

<!-- b000883 | furniture | pages [13] -->
m

<!-- b000884 | furniture | pages [13] -->
m

<!-- b000885 | furniture | pages [13] -->
m

<!-- b000886 | furniture | pages [13] -->
m

<!-- b000887 | furniture | pages [13] -->
m

<!-- b000888 | furniture | pages [13] -->
m

<!-- b000889 | furniture | pages [13] -->
m

<!-- b000890 | furniture | pages [13] -->
m

<!-- b000891 | furniture | pages [13] -->
m

<!-- b000892 | furniture | pages [13] -->
m

<!-- b000893 | furniture | pages [13] -->
m

<!-- b000894 | furniture | pages [13] -->
m

<!-- b000895 | furniture | pages [13] -->
m

<!-- b000896 | furniture | pages [13] -->
m

<!-- b000897 | furniture | pages [13] -->
m

<!-- b000898 | furniture | pages [13] -->
m

<!-- b000899 | furniture | pages [13] -->
m

<!-- b000900 | furniture | pages [13] -->
m

<!-- b000901 | furniture | pages [13] -->
m

<!-- b000902 | furniture | pages [13] -->
m

<!-- b000903 | furniture | pages [13] -->
m

<!-- b000904 | furniture | pages [13] -->
m

<!-- b000905 | furniture | pages [13] -->
m

<!-- b000906 | furniture | pages [13] -->
m

<!-- b000907 | furniture | pages [13] -->
m

<!-- b000908 | furniture | pages [13] -->
m

<!-- b000909 | furniture | pages [13] -->
m

<!-- b000910 | furniture | pages [13] -->
m

<!-- b000911 | furniture | pages [13] -->
m

<!-- b000912 | furniture | pages [13] -->
m

<!-- b000913 | furniture | pages [13] -->
m

<!-- b000914 | furniture | pages [13] -->
m

<!-- b000915 | furniture | pages [13] -->
m

<!-- b000916 | furniture | pages [13] -->
m

<!-- b000917 | furniture | pages [13] -->
m

<!-- b000918 | furniture | pages [13] -->
m

<!-- b000919 | furniture | pages [13] -->
m

<!-- b000920 | furniture | pages [13] -->
m

<!-- b000921 | furniture | pages [13] -->
m

<!-- b000922 | furniture | pages [13] -->
m

<!-- b000923 | furniture | pages [13] -->
m

<!-- b000924 | furniture | pages [13] -->
m

<!-- b000925 | furniture | pages [13] -->
m

<!-- b000926 | furniture | pages [13] -->
m

<!-- b000927 | furniture | pages [13] -->
m

<!-- b000928 | furniture | pages [13] -->
m

<!-- b000929 | furniture | pages [13] -->
m

<!-- b000930 | furniture | pages [13] -->
m

<!-- b000931 | furniture | pages [13] -->
m

<!-- b000932 | furniture | pages [13] -->
m

<!-- b000933 | furniture | pages [13] -->
m

<!-- b000934 | furniture | pages [13] -->
m

<!-- b000935 | furniture | pages [13] -->
m

<!-- b000936 | furniture | pages [13] -->
m

<!-- b000937 | furniture | pages [13] -->
m

<!-- b000938 | furniture | pages [13] -->
m

<!-- b000939 | furniture | pages [13] -->
m

<!-- b000940 | furniture | pages [13] -->
m

<!-- b000941 | furniture | pages [13] -->
m

<!-- b000942 | furniture | pages [13] -->
m

<!-- b000943 | furniture | pages [13] -->
m

<!-- b000944 | furniture | pages [13] -->
m

<!-- b000945 | furniture | pages [13] -->
m

<!-- b000946 | furniture | pages [13] -->
m

<!-- b000947 | furniture | pages [13] -->
m

<!-- b000948 | furniture | pages [13] -->
m

<!-- b000949 | furniture | pages [13] -->
m

<!-- b000950 | furniture | pages [13] -->
m

<!-- b000951 | furniture | pages [13] -->
m

<!-- b000952 | furniture | pages [13] -->
m

<!-- b000953 | furniture | pages [13] -->
m

<!-- b000954 | furniture | pages [13] -->
m

<!-- b000955 | furniture | pages [13] -->
m

<!-- b000956 | furniture | pages [13] -->
m

<!-- b000957 | furniture | pages [13] -->
m

<!-- b000958 | furniture | pages [13] -->
m

<!-- b000959 | furniture | pages [13] -->
m

<!-- b000960 | furniture | pages [13] -->
m

<!-- b000961 | furniture | pages [13] -->
m

<!-- b000962 | furniture | pages [13] -->
m

<!-- b000963 | furniture | pages [13] -->
m

<!-- b000964 | furniture | pages [13] -->
m

<!-- b000965 | furniture | pages [13] -->
m

<!-- b000966 | furniture | pages [13] -->
m

<!-- b000967 | furniture | pages [13] -->
m

<!-- b000968 | furniture | pages [13] -->
m

<!-- b000969 | furniture | pages [13] -->
m

<!-- b000970 | furniture | pages [13] -->
m

<!-- b000971 | furniture | pages [13] -->
m

<!-- b000972 | furniture | pages [13] -->
m

<!-- b000973 | furniture | pages [13] -->
m

<!-- b000974 | furniture | pages [13] -->
m

<!-- b000975 | furniture | pages [13] -->
m

<!-- b000976 | furniture | pages [13] -->
m

<!-- b000977 | furniture | pages [13] -->
m

<!-- b000978 | furniture | pages [13] -->
m

<!-- b000979 | furniture | pages [13] -->
m

<!-- b000980 | furniture | pages [13] -->
m

<!-- b000981 | furniture | pages [13] -->
m

<!-- b000982 | furniture | pages [13] -->
m

<!-- b000983 | furniture | pages [13] -->
m

<!-- b000984 | furniture | pages [13] -->
m

<!-- b000985 | furniture | pages [13] -->
m

<!-- b000986 | furniture | pages [13] -->
m

<!-- b000987 | furniture | pages [13] -->
m

<!-- b000988 | furniture | pages [13] -->
m

<!-- b000989 | furniture | pages [13] -->
m

<!-- b000990 | furniture | pages [13] -->
m

<!-- b000991 | furniture | pages [13] -->
m

<!-- b000992 | furniture | pages [13] -->
m

<!-- b000993 | furniture | pages [13] -->
m

<!-- b000994 | furniture | pages [13] -->
m

<!-- b000995 | furniture | pages [13] -->
m

<!-- b000996 | furniture | pages [13] -->
m

<!-- b000997 | furniture | pages [13] -->
m

<!-- b000998 | furniture | pages [13] -->
m

<!-- b000999 | furniture | pages [13] -->
m

<!-- b001000 | furniture | pages [13] -->
m

<!-- b001001 | furniture | pages [13] -->
m

<!-- b001002 | furniture | pages [13] -->
m

<!-- b001003 | furniture | pages [13] -->
m

<!-- b001004 | furniture | pages [13] -->
m

<!-- b001005 | furniture | pages [13] -->
m

<!-- b001006 | furniture | pages [13] -->
m

<!-- b001007 | furniture | pages [13] -->
m

<!-- b001008 | furniture | pages [13] -->
m

<!-- b001009 | furniture | pages [13] -->
m

<!-- b001010 | furniture | pages [13] -->
m

<!-- b001011 | furniture | pages [13] -->
m

<!-- b001012 | furniture | pages [13] -->
m

<!-- b001013 | furniture | pages [13] -->
m

<!-- b001014 | furniture | pages [13] -->
m

<!-- b001015 | furniture | pages [13] -->
m

<!-- b001016 | furniture | pages [13] -->
m

<!-- b001017 | furniture | pages [13] -->
m

<!-- b001018 | furniture | pages [13] -->
m

<!-- b001019 | furniture | pages [13] -->
m

<!-- b001020 | furniture | pages [13] -->
m

<!-- b001021 | furniture | pages [13] -->
m

<!-- b001022 | furniture | pages [13] -->
m

<!-- b001023 | furniture | pages [13] -->
m

<!-- b001024 | furniture | pages [13] -->
m

<!-- b001025 | furniture | pages [13] -->
m

<!-- b001026 | furniture | pages [13] -->
m

<!-- b001027 | furniture | pages [13] -->
m

<!-- b001028 | furniture | pages [13] -->
m

<!-- b001029 | furniture | pages [13] -->
m

<!-- b001030 | furniture | pages [13] -->
m

<!-- b001031 | furniture | pages [13] -->
m

<!-- b001032 | furniture | pages [13] -->
m

<!-- b001033 | furniture | pages [13] -->
m

<!-- b001034 | furniture | pages [13] -->
m

<!-- b001035 | furniture | pages [13] -->
m

<!-- b001036 | furniture | pages [13] -->
m

<!-- b001037 | furniture | pages [13] -->
m

<!-- b001038 | furniture | pages [13] -->
m

<!-- b001039 | furniture | pages [13] -->
m

<!-- b001040 | furniture | pages [13] -->
m

<!-- b001041 | furniture | pages [13] -->
m

<!-- b001042 | furniture | pages [13] -->
m

<!-- b001043 | furniture | pages [13] -->
m

<!-- b001044 | furniture | pages [13] -->
m

<!-- b001045 | furniture | pages [13] -->
m

<!-- b001046 | furniture | pages [13] -->
m

<!-- b001047 | furniture | pages [13] -->
m

<!-- b001048 | furniture | pages [13] -->
m

<!-- b001049 | furniture | pages [13] -->
m

<!-- b001050 | furniture | pages [13] -->
m

<!-- b001051 | furniture | pages [13] -->
m

<!-- b001052 | furniture | pages [13] -->
m

<!-- b001053 | furniture | pages [13] -->
m

<!-- b001054 | furniture | pages [13] -->
m

<!-- b001055 | furniture | pages [13] -->
m

<!-- b001056 | furniture | pages [13] -->
m

<!-- b001057 | furniture | pages [13] -->
m

<!-- b001058 | furniture | pages [13] -->
m

<!-- b001059 | furniture | pages [13] -->
m

<!-- b001060 | furniture | pages [13] -->
m

<!-- b001061 | furniture | pages [13] -->
m

<!-- b001062 | furniture | pages [13] -->
m

<!-- b001063 | furniture | pages [13] -->
m

<!-- b001064 | furniture | pages [13] -->
m

<!-- b001065 | furniture | pages [13] -->
m

<!-- b001066 | furniture | pages [13] -->
m

<!-- b001067 | furniture | pages [13] -->
m

<!-- b001068 | furniture | pages [13] -->
m

<!-- b001069 | furniture | pages [13] -->
m

<!-- b001070 | furniture | pages [13] -->
m

<!-- b001071 | furniture | pages [13] -->
m

<!-- b001072 | furniture | pages [13] -->
m

<!-- b001073 | furniture | pages [13] -->
m

<!-- b001074 | furniture | pages [13] -->
m

<!-- b001075 | furniture | pages [13] -->
m

<!-- b001076 | furniture | pages [13] -->
m

<!-- b001077 | furniture | pages [13] -->
m

<!-- b001078 | furniture | pages [13] -->
m

<!-- b001079 | furniture | pages [13] -->
m

<!-- b001080 | furniture | pages [13] -->
m

<!-- b001081 | furniture | pages [13] -->
m

<!-- b001082 | furniture | pages [13] -->
m

<!-- b001083 | furniture | pages [13] -->
m

<!-- b001084 | furniture | pages [13] -->
m

<!-- b001085 | furniture | pages [13] -->
m

<!-- b001086 | furniture | pages [13] -->
m

<!-- b001087 | furniture | pages [13] -->
m

<!-- b001088 | furniture | pages [13] -->
m

<!-- b001089 | furniture | pages [13] -->
m

<!-- b001090 | furniture | pages [13] -->
m

<!-- b001091 | furniture | pages [13] -->
m

<!-- b001092 | furniture | pages [13] -->
m

<!-- b001093 | furniture | pages [13] -->
m

<!-- b001094 | furniture | pages [13] -->
m

<!-- b001095 | furniture | pages [13] -->
m

<!-- b001096 | furniture | pages [13] -->
m

<!-- b001097 | furniture | pages [13] -->
m

<!-- b001098 | furniture | pages [13] -->
m

<!-- b001099 | furniture | pages [13] -->
m

<!-- b001100 | furniture | pages [13] -->
m

<!-- b001101 | furniture | pages [13] -->
m

<!-- b001102 | furniture | pages [13] -->
m

<!-- b001103 | furniture | pages [13] -->
m

<!-- b001104 | furniture | pages [13] -->
m

<!-- b001105 | furniture | pages [13] -->
m

<!-- b001106 | furniture | pages [13] -->
m

<!-- b001107 | furniture | pages [13] -->
m

<!-- b001108 | furniture | pages [13] -->
m

<!-- b001109 | furniture | pages [13] -->
m

<!-- b001110 | furniture | pages [13] -->
m

<!-- b001111 | furniture | pages [13] -->
m

<!-- b001112 | furniture | pages [13] -->
m

<!-- b001113 | furniture | pages [13] -->
m

<!-- b001114 | furniture | pages [13] -->
m

<!-- b001115 | furniture | pages [13] -->
m

<!-- b001116 | furniture | pages [13] -->
m

<!-- b001117 | furniture | pages [13] -->
m

<!-- b001118 | furniture | pages [13] -->
m

<!-- b001119 | furniture | pages [13] -->
m

<!-- b001120 | furniture | pages [13] -->
m

<!-- b001121 | furniture | pages [13] -->
m

<!-- b001122 | furniture | pages [13] -->
m

<!-- b001123 | furniture | pages [13] -->
m

<!-- b001124 | furniture | pages [13] -->
m

<!-- b001125 | furniture | pages [13] -->
m

<!-- b001126 | furniture | pages [13] -->
m

<!-- b001127 | furniture | pages [13] -->
m

<!-- b001128 | furniture | pages [13] -->
m

<!-- b001129 | furniture | pages [13] -->
m

<!-- b001130 | furniture | pages [13] -->
m

<!-- b001131 | furniture | pages [13] -->
m

<!-- b001132 | furniture | pages [13] -->
m

<!-- b001133 | furniture | pages [13] -->
m

<!-- b001134 | furniture | pages [13] -->
m

<!-- b001135 | furniture | pages [13] -->
m

<!-- b001136 | furniture | pages [13] -->
m

<!-- b001137 | furniture | pages [13] -->
m

<!-- b001138 | furniture | pages [13] -->
m

<!-- b001139 | furniture | pages [13] -->
m

<!-- b001140 | furniture | pages [13] -->
m

<!-- b001141 | furniture | pages [13] -->
m

<!-- b001142 | furniture | pages [13] -->
m

<!-- b001143 | furniture | pages [13] -->
m

<!-- b001144 | furniture | pages [13] -->
m

<!-- b001145 | furniture | pages [13] -->
m

<!-- b001146 | furniture | pages [13] -->
m

<!-- b001147 | furniture | pages [13] -->
m

<!-- b001148 | furniture | pages [13] -->
m

<!-- b001149 | furniture | pages [13] -->
m

<!-- b001150 | furniture | pages [13] -->
m

<!-- b001151 | furniture | pages [13] -->
m

<!-- b001152 | furniture | pages [13] -->
m

<!-- b001153 | furniture | pages [13] -->
m

<!-- b001154 | furniture | pages [13] -->
m

<!-- b001155 | furniture | pages [13] -->
m

<!-- b001156 | furniture | pages [13] -->
m

<!-- b001157 | furniture | pages [13] -->
m

<!-- b001158 | furniture | pages [13] -->
m

<!-- b001159 | furniture | pages [13] -->
m

<!-- b001160 | furniture | pages [13] -->
m

<!-- b001161 | furniture | pages [13] -->
m

<!-- b001162 | furniture | pages [13] -->
m

<!-- b001163 | furniture | pages [13] -->
m

<!-- b001164 | furniture | pages [13] -->
m

<!-- b001165 | furniture | pages [13] -->
m

<!-- b001166 | furniture | pages [13] -->
m

<!-- b001167 | furniture | pages [13] -->
m

<!-- b001168 | furniture | pages [13] -->
m

<!-- b001169 | furniture | pages [13] -->
m

<!-- b001170 | furniture | pages [13] -->
m

<!-- b001171 | furniture | pages [13] -->
m

<!-- b001172 | furniture | pages [13] -->
m

<!-- b001173 | furniture | pages [13] -->
m

<!-- b001174 | furniture | pages [13] -->
m

<!-- b001175 | furniture | pages [13] -->
m

<!-- b001176 | furniture | pages [13] -->
m

<!-- b001177 | furniture | pages [13] -->
m

<!-- b001178 | furniture | pages [13] -->
m

<!-- b001179 | furniture | pages [13] -->
m

<!-- b001180 | furniture | pages [13] -->
m

<!-- b001181 | furniture | pages [13] -->
m

<!-- b001182 | furniture | pages [13] -->
m

<!-- b001183 | furniture | pages [13] -->
m

<!-- b001184 | furniture | pages [13] -->
m

<!-- b001185 | furniture | pages [13] -->
m

<!-- b001186 | furniture | pages [13] -->
m

<!-- b001187 | furniture | pages [13] -->
m

<!-- b001188 | furniture | pages [13] -->
m

<!-- b001189 | furniture | pages [13] -->
m

<!-- b001190 | furniture | pages [13] -->
m

<!-- b001191 | furniture | pages [13] -->
m

<!-- b001192 | furniture | pages [14] -->
Page 14 of 25

<!-- b001193 | furniture | pages [14] -->
Team # 2504188

<!-- b001195 | heading | pages [14] -->
6 Transit Network Optimization Model

<!-- b001196 | prose | pages [14] -->
Baltimore's aging infrastructure has significantly impacted residents' daily lives, and its transportation network needs urgent optimization. Given that buses are envi-ronmentally friendly and affordable, making them the preferred mode of transport for many city residents, we have decided to focus on optimizing the bus network to im-prove overall transportation efficiency and accessibility. 6.1 Urban Bus Network Visualization

<!-- b001197 | prose | pages [14] -->
Based on the Bus_Stop and Bus_Routes datasets, we analyze Baltimore's bus routes, treating them as network edges (set E) and bus stops as nodes (set V). We first record the station IDs for each route, and then plot the bus stops and routes on a map based on their geographic coordinates. The resulting map is shown in Figure 10.

<!-- b001198 | prose | pages [14] -->
To measure the importance of each bus stop, we use both betweenness centrality and degree centrality. The calculation method for betweenness centrality is as follows:

<!-- b001199 | prose | pages [14] -->
σst (v) CB(v)= ∑ (15) sevet∈V

<!-- b001200 | prose | pages [14] -->
Where σst represents the number of shortest paths from node s to node t, and σst(v) represents the number of shortest paths from node s to node t passing through node v.

<!-- b001201 | prose | pages [14] -->
Degree centrality is calculated as follows.

<!-- b001202 | prose | pages [14] -->
kv (16) CD(v)= n-1

<!-- b001203 | prose | pages [14] -->
Where kvis the degree of node v and n is the total number of nodes in the graph.

<!-- b001204 | prose | pages [14] -->
The importance of a node is calculated as follows.

<!-- b001205 | prose | pages [14] -->
CB(v) CD(v) +0.5 imp(v) = 0.5 (17) CD,max

<!-- b001206 | prose | pages [14, 15] -->
关注数学模型 微信公众号：数学模型

<!-- b001207 | furniture | pages [14] -->
获取更多资讯

<!-- b001208 | furniture | pages [15] -->
Team # 2504188

<!-- b001209 | furniture | pages [15] -->
Page 15 of 25

<!-- b001211 | caption | pages [15] -->
Figure 10: Public transport network map

<!-- b001212 | prose | pages [15] -->
From the diagram, we can see that the Baltimore bus network is densely distributed in the center and sparsely distributed around, which is related to the population residence and geographical characteristics of different areas of the city. The population is dense and the traffic demand is large in the city, so buses can relieve the pressure; the population is scattered in the suburbs, the distance is far, the bus efficiency is low, and the network is sparse. The importance score of bus stations, 푖푚푝(푣) , shows that most scores are between 0 and 0.5, which means that most 微信号：MATHmodels stations only have one or two routes stopping, and residents need to transfer, the travel cost is high, and the setting is unreasonable. There are few bus routes around the Francis Scott Key Bridge. Considering its importance and travel demand, subsequent modeling will focus on optimizing the bus network in this area to improve service quality and travel convenience.

<!-- b001213 | heading | pages [15] -->
6.2 Single-objective Optimization Model

<!-- b001214 | prose | pages [15] -->
·Parameters and decision variables 푑represents the service radius of the bus station, which is 0.3 km here. 푆푠푒푟푣푖푐푒 represents the total service area of all bus stations, and 푆푐푖푡푦represents the area of the city. 푏represents the number of new bus stations. [푋, 푌] represents the location set of the new bus stations.

<!-- b001215 | prose | pages [15] -->
The decision variables are { 푿풊, 풀풊}, 푏.

<!-- b001216 | prose | pages [15] -->
·Objective function In order to facilitate people's travel, we hope that the service range of the bus station can cover the entire city, that is, we hope that the value of the bus station service area/city area is 1, which is difficult to achieve in real life, so we hope to maximize this ratio. Note that this ratio is calculated after adding b bus stops with different longitudes and latitudes.

<!-- b001217 | prose | pages [15, 16] -->
S max service (18) S city Since the service ranges of different bus stops overlap and the city area is difficult to calculate, we use Monte Carlo simulation to calculate this ratio.

<!-- b001218 | furniture | pages [16] -->
Team # 2504188

<!-- b001219 | furniture | pages [16] -->
Page 16 of 25

<!-- b001221 | prose | pages [16] -->
Step1 Randomly generate 10,0000 coordinates within the city to simulate the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m location of people who need to take the bus. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Step2 Calculate the distances from these 10,0000 sample points to the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m surrounding stations. If there is a station with a distance from the sample point less m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m than 0.3 km, it means that the sample can take the bus conveniently and is added to m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the set Service; if the distance between the station and the sample point is greater than 0.3 km, it means that the sample is not within the service range of the bus station.

<!-- b001222 | prose | pages [16] -->
Step3 The number of samples in the set Service/100000 is the current service range ratio.

<!-- b001223 | prose | pages [16] -->
·Constraints First, due to limited funds, the number of bus stations to be built is also limited.

<!-- b001224 | prose | pages [16] -->
(19) 0 b N  

<!-- b001225 | prose | pages [16] -->
Where 푁represents the number of bus stops that can be built with sufficient funds.

<!-- b001226 | prose | pages [16] -->
Secondly, the location of the bus station must be within the selected optimized area.

<!-- b001227 | prose | pages [16] -->
(20) 76 617382 76 584337 1 2 . . ( , ... ) X i b     i (21) 39 207759 39 237561 1 2 . . ( , ... ) iY i b   

<!-- b001228 | prose | pages [16] -->
(22) 0 90186 29 860591 . . Y X   i i

<!-- b001229 | prose | pages [16] -->
Among them, 푋푖represents the latitude of the newly added node, and 푌푖represents the longitude of the newly added node.

<!-- b001230 | prose | pages [16] -->
Finally, when planning new stations, the rationality of the distance between stations must be fully considered. Too long a distance between stations may cause large blank areas in the bus line coverage, which cannot meet the travel needs of residents along the line. We stipulate that the distance between a new station and any surrounding station cannot be greater than the maximum distance between the original adjacent stations.

<!-- b001231 | prose | pages [16] -->
(23) min( ( , )) max( ( , )) Ha new v Ha v v   1 i j j

<!-- b001232 | prose | pages [16] -->
Where 퐻푎represents the Hafsin formula, 푛푒푤represents the newly added node and

<!-- b001233 | prose | pages [16] -->
푣represents the original node. min 퐻푎푛푒푤, 푣푖 represents the shortest distance

<!-- b001234 | prose | pages [16] -->
between the newly added node and the surrounding nodes, and

<!-- b001235 | prose | pages [16] -->
min 퐻푎푣푗, 푣푗+1 represents the longest distance between the original adjacent

<!-- b001236 | prose | pages [16] -->
nodes.

<!-- b001237 | prose | pages [16] -->
To sum up, the planning model is as follows:

<!-- b001238 | prose | pages [16, 17] -->
关注数学模型 푚푎푥푆푠푒푟푣푖푐푒 푆푐푖푡푦 0 b N    (24)  76 617382 76 584337 1 2 . . ( , ... ) X i b     i 39 207759 39 237561 1 2 . . ( , ... ) . . #(24) Y i b s t     i  min( ( , )) max( ( , )) Ha new v Ha v v   1 i j j  0 90186 29 860591 . . Y X    i i 微信公众号：数学模型

<!-- b001239 | furniture | pages [16] -->
2

<!-- b001240 | furniture | pages [16] -->
MATHmodels

<!-- b001241 | furniture | pages [16] -->
获取更多资讯

<!-- b001242 | furniture | pages [17] -->
Team # 2504188

<!-- b001243 | furniture | pages [17] -->
Page 17 of 25

<!-- b001245 | heading | pages [17] -->
6.3 Solution

<!-- b001246 | prose | pages [17] -->
Here we mainly show the optimization process of the selected triangular area bus station. The greedy algorithm is used to solve Single-objective nonlinear programming model. The longitude and latitude of the five newly added bus stations are as follows:

<!-- b001247 | caption | pages [17] -->
Table 3: added station longitude and latitude

<!-- b001248 | prose | pages [17] -->
1 2 3 4 5 微信号：MATHmodels Latitude 39.232 39.220 39.22711 39.23373 39.2345 Longitude -76.605466 -76.594134 -76.592677 -76.590588 -76.585844

<!-- b001249 | caption | pages [17] -->
Figure 11: Monte Carlo simulation changes

<!-- b001250 | prose | pages [17] -->
The above figure is a comparison of the results of Monte Carlo simulation before and after adding stations, marking only the sample points within the service range. The red color indicates the location where the sample points appear most frequently, and the blue color indicates the location where the sample points appear less frequently. The histogram shows the traffic coverage at different longitudes and latitudes.From the figure, we can see that the five newly added stations have brought more sample points within the service range, which means that more residents can take the bus conveniently. Each bus station maximizes the service coverage, so the distance is reasonable. This is enough to prove that the model has effectively optimized the bus network. After the addition of new stations, traffic coverage increased from 61.37% to 78.13%.

<!-- b001251 | prose | pages [17] -->
To measure the changes in the convenience of travel for each stakeholder before and after the traffic improvement, we selected some buildings in the traffic improvement area, simulated the arrival process of four types of stakeholders, namely

<!-- b001252 | prose | pages [17, 18] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m urban residents, suburban residents, tourists and transit passengers, and scored them, and then compared the scores. Considering that businesses and suburban commuters rarely use public transportation, they were not included in the evaluation scope.Taking urban residents as an example, we selected the Brooklyn Ave residential area as the starting point and six places closely related to the lives of urban residents, such as the port, as the destination for simulation. The simulation process for other stakeholders is the same. Finally, the scores of each stakeholder before and after the traffic improvement are plotted into a graph, and the results are as follows.

<!-- b001253 | furniture | pages [17] -->
m

<!-- b001254 | furniture | pages [17] -->
m

<!-- b001255 | furniture | pages [17] -->
m

<!-- b001256 | furniture | pages [17] -->
m

<!-- b001257 | furniture | pages [17] -->
m

<!-- b001258 | furniture | pages [17] -->
m

<!-- b001259 | furniture | pages [17] -->
m

<!-- b001260 | furniture | pages [17] -->
m

<!-- b001261 | furniture | pages [17] -->
m

<!-- b001262 | furniture | pages [17] -->
m

<!-- b001263 | furniture | pages [17] -->
m

<!-- b001264 | furniture | pages [17] -->
m

<!-- b001265 | furniture | pages [17] -->
m

<!-- b001266 | furniture | pages [17] -->
m

<!-- b001267 | furniture | pages [17] -->
m

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

<!-- b001577 | furniture | pages [18] -->
Team # 2504188

<!-- b001578 | furniture | pages [18] -->
Page 18 of 25

<!-- b001580 | caption | pages [18] -->
Figure 12: Radar comparison before and after improvement

<!-- b001581 | prose | pages [18] -->
It is worth noting that due to the different locations selected, horizontal comparison between stakeholders is meaningless. We focus on the score changes before and after traffic improvement. It can be seen that the hexagons framed by the scores before the improvement completely surround the hexagons after the improvement. The accessibility of stakeholders is determined by the time it takes for vehicles or pedestrians to pass through the road section, that is, the longer the time spent, the greater the accessibility value, which means the more inconvenient the

<!-- b001582 | prose | pages [18, 19] -->
关注数学模型 passage. Therefore, after the traffic improvement, the travel of various stakeholders is indeed more convenient.

<!-- b001583 | furniture | pages [18] -->
2

<!-- b001584 | furniture | pages [18] -->
MATHmodels

<!-- b001585 | furniture | pages [18] -->
获取更多资讯

<!-- b001586 | furniture | pages [19] -->
Page 19 of 25

<!-- b001587 | furniture | pages [19] -->
Team # 2504188

<!-- b001589 | heading | pages [19] -->
7 Community Road Availability Optimization Model

<!-- b001590 | heading | pages [19] -->
7.1 Supplementary Datasets

<!-- b001591 | prose | pages [19] -->
Step1 Use OpenStreetMap API to obtain highway and land use information in urban areas, extract vector data and boundary data of highways.

<!-- b001592 | prose | pages [19] -->
Step2 Use QGIS to identify the area surrounded by highways as polygons, and divide the area into plots surrounded by highways.

<!-- b001593 | prose | pages [19] -->
Step3 Correspond each plot to its land type.

<!-- b001594 | heading | pages [19] -->
7.2 Community transportation availability evaluation

<!-- b001595 | prose | pages [19] -->
We evaluate the traffic availability of each community and focus on optimizing roads in areas with lower scores. We selected three indicators to measure the traffic availability of a community: connectivity index, congestion index, and hybrid index.

<!-- b001596 | prose | pages [19] -->
1. The connectivity index is used to measure the complexity and accessibility of the transportation network. The better the accessibility, the higher the availability.

<!-- b001597 | prose | pages [19] -->
(25) nodes 1 2.The Congestion Index is used to measure the degree of road congestion. The higher the congestion, the lower the traffic availability. See formula 4 for calculation.

<!-- b001598 | prose | pages [19] -->
3.The hybrid index is usually used to measure the degree of mixing of land with different uses in a specific area. Generally speaking, the larger the index, the more diverse the land uses, and the more favorable it is for road availability. We express the hybrid index in the form of entropy.

<!-- b001599 | prose | pages [19] -->
n LUMI = −∑hi · ln(hi) (26) i=1

<!-- b001600 | prose | pages [19] -->
Where n represents the number of types of land use in the community, and hrepresents the proportion of land of each type of use.

<!-- b001601 | prose | pages [19] -->
The final formula for calculating community transportation availability is as follows:

<!-- b001602 | prose | pages [19] -->
1 1 1 L (27) CI + LUMI + score = 3 3 3

<!-- b001603 | furniture | pages [20] -->
Team # 2504188

<!-- b001604 | furniture | pages [20] -->
Page 20 of 25

<!-- b001605 | heading | pages [20] -->
7.3 Traffic Layout Optimization Model

<!-- b001606 | prose | pages [20] -->
For communities with lower scores, we optimize the paths.

<!-- b001607 | prose | pages [20] -->
·Decision variables 퐿푈푀퐼푡표푡푎푙represents the overall mixedness index of the optimized area,퐶퐼푡표푡푎푙 represents the overall connectivity index of the area, 푞푢푎푛푡푖푡푦represents the total number of constructed paths, and 푙푒푛푔푡ℎrepresents the total length of constructed paths.

<!-- b001608 | prose | pages [20] -->
·Objective function The goal of the model is to change the direction of some highways to maximize the overall availability. While ensuring availability, the cost issue also needs to be considered, that is, the road to be built should be as short as possible.

<!-- b001609 | prose | pages [20] -->
length max( ) LUMI CI        (28) length H max

<!-- b001610 | prose | pages [20] -->
Where 퐻represents the planning and design variables of the highway, and 훼, 훽, and 훿are weight parameters used to balance the importance of 퐿푈푀퐼and 퐶퐼.

<!-- b001611 | prose | pages [20] -->
·Constraints Due to budget constraints, the total length of the construction and the number of construction paths also need to be limited.

<!-- b001612 | prose | pages [20] -->
(29) 0 0 quantity Q length Le     , 푄 and 퐿푒 represent the maximum number and the longest path that can be constructed by the operation.

<!-- b001613 | prose | pages [20] -->
Not all types of land are suitable for building roads. For example, near residential areas, highways will hinder the normal life of residents.

<!-- b001614 | prose | pages [20] -->
(30) ( ) L H H  allowed

<!-- b001615 | prose | pages [20] -->
We use approximate dynamic programming to solve the above model. Compared with the traditional dynamic programming algorithm, the approximate dynamic programming algorithm can continuously update and adjust the strategy according to the real-time data, can better cope with the dynamic changes and uncertainties of the problem, and can solve the problem of dimensionality explosion. Approximate dynamic programming uses a function of one parameter to approximate the state value function.

<!-- b001616 | prose | pages [20] -->
length ˆ( ; ) LUMI( ) ( ) U s s CI s          (31) 1 2 3 length max

<!-- b001617 | prose | pages [20] -->
Among them, 휃1, 휃2, 휃3 are learnable parameters, and their update process is as follows.

<!-- b001618 | prose | pages [20] -->
(32)   2   ˆ ˆ   ( ; ) ( , ) ;  U s r s a U s               

<!-- b001619 | prose | pages [20, 21] -->
关注数学模型 Regarding the state transition conditions, we consider the impact of action a on the network availability index CI.

<!-- b001620 | furniture | pages [20] -->
2

<!-- b001621 | furniture | pages [20] -->
MATHmodels

<!-- b001622 | furniture | pages [20] -->
获取更多资讯

<!-- b001623 | furniture | pages [21] -->
Team # 2504188

<!-- b001624 | furniture | pages [21] -->
Page 21 of 25

<!-- b001626 | prose | pages [21] -->
(33)    , CI s  f V  E  

<!-- b001627 | prose | pages [21] -->
Where 푓(푉', 퐸') is the connectivity calculated for the latest node set and edge set. The probability of connectivity change after executing action a is as follows.

<!-- b001628 | prose | pages [21] -->
(34) length   , max( ( ) ( ) )  P s s a soft LUMI s CI s          ∣ 1 2 3 length max 微信公众号：数学模型 When the action satisfies the constraints, the probability of change approaches 1, and when the action does not meet the constraints, the probability of change approaches 0.

<!-- b001629 | prose | pages [21] -->
The path selection strategy will be updated in real time according to the current situation, tending to select high-quality actions.

<!-- b001630 | prose | pages [21] -->
(35)      ˆ  ( | ; ) arg max ( , ) , ;    a s r s a P s s a U s       ∣   A a     S s 

<!-- b001631 | heading | pages [21] -->
7.4 Solution

<!-- b001632 | prose | pages [21] -->
微信号：MATHmodels

<!-- b001633 | caption | pages [21] -->
Figure 13: Project Optimization Process

<!-- b001634 | prose | pages [21, 22] -->
Through the calculation of community traffic availability, several areas with low availability scores were identified. As shown in the figure, this community has low traffic availability. It can be observed that a certain area of the community is surrounded by highways, which makes it inconvenient for residents in the area to travel. In response to this problem, the following improvement plans are proposed: first, build a highway connecting the area with other areas of the community; second, add a highway exit. Based on these two goals, the approximate dynamic programming method is used to solve the construction locations of the two plans, and the final results are shown in the blue box in the figure.

<!-- b001635 | furniture | pages [22] -->
Team # 2504188

<!-- b001636 | furniture | pages [22] -->
Page 22 of 25

<!-- b001638 | prose | pages [22] -->
This project has a great impact on the lives of the people of Baltimore.

<!-- b001639 | prose | pages [22] -->
a. For local residents, the project to break regional isolation will undoubtedly make their travel more convenient.

<!-- b001640 | prose | pages [22] -->
b. For entrepreneurs, the impact has both advantages and disadvantages. After the project is completed, the optimized highway will improve logistics and transportation efficiency and expand the reachable range. In addition, more convenient transportation may stimulate real estate development in the area and increase land value, so it may increase revenue. The biggest disadvantage is that it may cause highway congestion during construction. In the long run, for local governments, the project requires research and development funds and long-term maintenance, which may increase financial pressure.

<!-- b001641 | prose | pages [22] -->
c. In the past few years, traffic congestion has spread across the country, billions of hours of time and productivity have been lost due to detours and traffic jams, and civil lawsuits regarding traffic accidents have taken up the court system's time. If our model can be promoted and applied, the city's transportation network can be effectively rebuilt, greatly alleviating the problem of traffic congestion and reducing people's unnecessary time. At the same time, the optimization of traffic roads is beneficial to the appearance of the city, beautifying the urban landscape and improving the quality of life of urban residents.

<!-- b001642 | heading | pages [22] -->
8 Model Application for Security

<!-- b001643 | prose | pages [22] -->
Traffic accidents occur frequently in the United States, which has caused serious damage to the interests of stakeholders. Relevant data show that the congestion level and the number of traffic accidents in the United States are on the rise.

<!-- b001644 | caption | pages [22] -->
Figure 14: Traffic accidents and congestion

<!-- b001645 | prose | pages [22] -->
In order to effectively protect the interests of stakeholders, we have summarized the indicators of the three models and designed a software that can view the traffic conditions in Baltimore in real time, help to understand traffic dynamics in a timely manner, and reduce the occurrence of traffic accidents. This software contains the following four modules:

<!-- b001646 | prose | pages [22, 23] -->
关注数学模型 The first module can monitor structural changes and establish inspection cycles. The second module can analyze real-time data to predict possible traffic congestion and dangerous areas ,then remind users. The third module can connect emergency service departments through the platform once a traffic accident is detected, the system will automatically send a reminder mess age to residents within a certain range around the accident site by diversified ways Th e fourth module provide safety education focusing on the traffic safety awareness.

<!-- b001647 | furniture | pages [22] -->
2

<!-- b001648 | furniture | pages [22] -->
MATHmodels

<!-- b001649 | furniture | pages [22] -->
获取更多资讯

<!-- b001650 | furniture | pages [23] -->
Team # 2504188

<!-- b001651 | furniture | pages [23] -->
Page 23 of 25

<!-- b001653 | prose | pages [23] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b001654 | caption | pages [23] -->
Figure 15: Software interface design

<!-- b001655 | heading | pages [23] -->
9 Sensitivity Analysis

<!-- b001656 | prose | pages [23] -->
In order to explore the impact of service radius on bus coverage and verify the rationality of parameter selection, we conducted a sensitivity analysis on the constant 푑 representing the service radius of bus stops in the planning model. The service radius was adjusted from 100 meters to 600 meters in steps of 20 meters, and the bus coverage corresponding to each service radius was calculated. The results are shown in the figure.

<!-- b001657 | caption | pages [23] -->
Figure 16: Sensitivity analysis of d

<!-- b001658 | prose | pages [23, 24] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The bus coverage rate is sensitive to changes in the service radius. In the range of 100-480 meters, the coverage rate increases significantly with the increase of the service radius; after exceeding 500 meters, the coverage rate approaches the theoretical maximum value, and the growth slows down and enters a plateau period, indicating that expanding the service radius within a certain range can effectively improve the coverage rate, and the effect of exceeding the critical point gradually weakens.This study has practical significance. Expanding the service radius can reduce the cost of station construction, but the time for residents to walk to the station will become longer. In order to balance the construction cost and the interests of residents, the service radius corresponding to the midpoint of the coverage rate is selected for modeling, and this parameter selection is reasonable.

<!-- b001659 | furniture | pages [23] -->
m

<!-- b001660 | furniture | pages [23] -->
m

<!-- b001661 | furniture | pages [23] -->
m

<!-- b001662 | furniture | pages [23] -->
m

<!-- b001663 | furniture | pages [23] -->
m

<!-- b001664 | furniture | pages [23] -->
m

<!-- b001665 | furniture | pages [23] -->
m

<!-- b001666 | furniture | pages [23] -->
m

<!-- b001667 | furniture | pages [23] -->
m

<!-- b001668 | furniture | pages [23] -->
m

<!-- b001669 | furniture | pages [23] -->
m

<!-- b001670 | furniture | pages [23] -->
m

<!-- b001671 | furniture | pages [23] -->
m

<!-- b001672 | furniture | pages [23] -->
m

<!-- b001673 | furniture | pages [23] -->
m

<!-- b001674 | furniture | pages [23] -->
m

<!-- b001675 | furniture | pages [23] -->
m

<!-- b001676 | furniture | pages [23] -->
m

<!-- b001677 | furniture | pages [23] -->
m

<!-- b001678 | furniture | pages [23] -->
m

<!-- b001679 | furniture | pages [23] -->
m

<!-- b001680 | furniture | pages [23] -->
m

<!-- b001681 | furniture | pages [23] -->
m

<!-- b001682 | furniture | pages [23] -->
m

<!-- b001683 | furniture | pages [23] -->
m

<!-- b001684 | furniture | pages [23] -->
m

<!-- b001685 | furniture | pages [23] -->
m

<!-- b001686 | furniture | pages [23] -->
m

<!-- b001687 | furniture | pages [23] -->
m

<!-- b001688 | furniture | pages [23] -->
m

<!-- b001689 | furniture | pages [23] -->
m

<!-- b001690 | furniture | pages [23] -->
m

<!-- b001691 | furniture | pages [23] -->
m

<!-- b001692 | furniture | pages [23] -->
m

<!-- b001693 | furniture | pages [23] -->
m

<!-- b001694 | furniture | pages [23] -->
m

<!-- b001695 | furniture | pages [23] -->
m

<!-- b001696 | furniture | pages [23] -->
m

<!-- b001697 | furniture | pages [23] -->
m

<!-- b001698 | furniture | pages [23] -->
m

<!-- b001699 | furniture | pages [23] -->
m

<!-- b001700 | furniture | pages [23] -->
m

<!-- b001701 | furniture | pages [23] -->
m

<!-- b001702 | furniture | pages [23] -->
m

<!-- b001703 | furniture | pages [23] -->
m

<!-- b001704 | furniture | pages [23] -->
m

<!-- b001705 | furniture | pages [23] -->
m

<!-- b001706 | furniture | pages [23] -->
m

<!-- b001707 | furniture | pages [23] -->
m

<!-- b001708 | furniture | pages [23] -->
m

<!-- b001709 | furniture | pages [23] -->
m

<!-- b001710 | furniture | pages [23] -->
m

<!-- b001711 | furniture | pages [23] -->
m

<!-- b001712 | furniture | pages [23] -->
m

<!-- b001713 | furniture | pages [23] -->
m

<!-- b001714 | furniture | pages [23] -->
m

<!-- b001715 | furniture | pages [23] -->
m

<!-- b001716 | furniture | pages [23] -->
m

<!-- b001717 | furniture | pages [23] -->
m

<!-- b001718 | furniture | pages [23] -->
m

<!-- b001719 | furniture | pages [23] -->
m

<!-- b001720 | furniture | pages [23] -->
m

<!-- b001721 | furniture | pages [23] -->
m

<!-- b001722 | furniture | pages [23] -->
m

<!-- b001723 | furniture | pages [23] -->
m

<!-- b001724 | furniture | pages [23] -->
m

<!-- b001725 | furniture | pages [23] -->
m

<!-- b001726 | furniture | pages [23] -->
m

<!-- b001727 | furniture | pages [23] -->
m

<!-- b001728 | furniture | pages [23] -->
m

<!-- b001729 | furniture | pages [23] -->
m

<!-- b001730 | furniture | pages [23] -->
m

<!-- b001731 | furniture | pages [23] -->
m

<!-- b001732 | furniture | pages [23] -->
m

<!-- b001733 | furniture | pages [23] -->
m

<!-- b001734 | furniture | pages [23] -->
m

<!-- b001735 | furniture | pages [23] -->
m

<!-- b001736 | furniture | pages [23] -->
m

<!-- b001737 | furniture | pages [23] -->
m

<!-- b001738 | furniture | pages [23] -->
m

<!-- b001739 | furniture | pages [23] -->
m

<!-- b001740 | furniture | pages [23] -->
m

<!-- b001741 | furniture | pages [23] -->
m

<!-- b001742 | furniture | pages [23] -->
m

<!-- b001743 | furniture | pages [23] -->
m

<!-- b001744 | furniture | pages [23] -->
m

<!-- b001745 | furniture | pages [23] -->
m

<!-- b001746 | furniture | pages [23] -->
m

<!-- b001747 | furniture | pages [23] -->
m

<!-- b001748 | furniture | pages [23] -->
m

<!-- b001749 | furniture | pages [23] -->
m

<!-- b001750 | furniture | pages [23] -->
m

<!-- b001751 | furniture | pages [23] -->
m

<!-- b001752 | furniture | pages [23] -->
m

<!-- b001753 | furniture | pages [23] -->
m

<!-- b001754 | furniture | pages [23] -->
m

<!-- b001755 | furniture | pages [23] -->
m

<!-- b001756 | furniture | pages [23] -->
m

<!-- b001757 | furniture | pages [23] -->
m

<!-- b001758 | furniture | pages [23] -->
m

<!-- b001759 | furniture | pages [23] -->
m

<!-- b001760 | furniture | pages [23] -->
m

<!-- b001761 | furniture | pages [23] -->
m

<!-- b001762 | furniture | pages [23] -->
m

<!-- b001763 | furniture | pages [23] -->
m

<!-- b001764 | furniture | pages [23] -->
m

<!-- b001765 | furniture | pages [23] -->
m

<!-- b001766 | furniture | pages [23] -->
m

<!-- b001767 | furniture | pages [23] -->
m

<!-- b001768 | furniture | pages [23] -->
m

<!-- b001769 | furniture | pages [23] -->
m

<!-- b001770 | furniture | pages [23] -->
m

<!-- b001771 | furniture | pages [23] -->
m

<!-- b001772 | furniture | pages [23] -->
m

<!-- b001773 | furniture | pages [23] -->
m

<!-- b001774 | furniture | pages [23] -->
m

<!-- b001775 | furniture | pages [23] -->
m

<!-- b001776 | furniture | pages [23] -->
m

<!-- b001777 | furniture | pages [23] -->
m

<!-- b001778 | furniture | pages [23] -->
m

<!-- b001779 | furniture | pages [23] -->
m

<!-- b001780 | furniture | pages [23] -->
m

<!-- b001781 | furniture | pages [23] -->
m

<!-- b001782 | furniture | pages [23] -->
m

<!-- b001783 | furniture | pages [23] -->
m

<!-- b001784 | furniture | pages [23] -->
m

<!-- b001785 | furniture | pages [23] -->
m

<!-- b001786 | furniture | pages [23] -->
m

<!-- b001787 | furniture | pages [23] -->
m

<!-- b001788 | furniture | pages [23] -->
m

<!-- b001789 | furniture | pages [23] -->
m

<!-- b001790 | furniture | pages [23] -->
m

<!-- b001791 | furniture | pages [23] -->
m

<!-- b001792 | furniture | pages [23] -->
m

<!-- b001793 | furniture | pages [23] -->
m

<!-- b001794 | furniture | pages [23] -->
m

<!-- b001795 | furniture | pages [23] -->
m

<!-- b001796 | furniture | pages [23] -->
m

<!-- b001797 | furniture | pages [23] -->
m

<!-- b001798 | furniture | pages [23] -->
m

<!-- b001799 | furniture | pages [23] -->
m

<!-- b001800 | furniture | pages [23] -->
m

<!-- b001801 | furniture | pages [23] -->
m

<!-- b001802 | furniture | pages [23] -->
m

<!-- b001803 | furniture | pages [23] -->
m

<!-- b001804 | furniture | pages [23] -->
m

<!-- b001805 | furniture | pages [23] -->
m

<!-- b001806 | furniture | pages [23] -->
m

<!-- b001807 | furniture | pages [23] -->
m

<!-- b001808 | furniture | pages [23] -->
m

<!-- b001809 | furniture | pages [23] -->
m

<!-- b001810 | furniture | pages [23] -->
m

<!-- b001811 | furniture | pages [23] -->
m

<!-- b001812 | furniture | pages [23] -->
m

<!-- b001813 | furniture | pages [23] -->
m

<!-- b001814 | furniture | pages [23] -->
m

<!-- b001815 | furniture | pages [23] -->
m

<!-- b001816 | furniture | pages [23] -->
m

<!-- b001817 | furniture | pages [23] -->
m

<!-- b001818 | furniture | pages [23] -->
m

<!-- b001819 | furniture | pages [23] -->
m

<!-- b001820 | furniture | pages [23] -->
m

<!-- b001821 | furniture | pages [23] -->
m

<!-- b001822 | furniture | pages [23] -->
m

<!-- b001823 | furniture | pages [23] -->
m

<!-- b001824 | furniture | pages [23] -->
m

<!-- b001825 | furniture | pages [23] -->
m

<!-- b001826 | furniture | pages [23] -->
m

<!-- b001827 | furniture | pages [23] -->
m

<!-- b001828 | furniture | pages [23] -->
m

<!-- b001829 | furniture | pages [23] -->
m

<!-- b001830 | furniture | pages [23] -->
m

<!-- b001831 | furniture | pages [23] -->
m

<!-- b001832 | furniture | pages [23] -->
m

<!-- b001833 | furniture | pages [23] -->
m

<!-- b001834 | furniture | pages [23] -->
m

<!-- b001835 | furniture | pages [23] -->
m

<!-- b001836 | furniture | pages [23] -->
m

<!-- b001837 | furniture | pages [23] -->
m

<!-- b001838 | furniture | pages [23] -->
m

<!-- b001839 | furniture | pages [23] -->
m

<!-- b001840 | furniture | pages [23] -->
m

<!-- b001841 | furniture | pages [23] -->
m

<!-- b001842 | furniture | pages [23] -->
m

<!-- b001843 | furniture | pages [23] -->
m

<!-- b001844 | furniture | pages [23] -->
m

<!-- b001845 | furniture | pages [23] -->
m

<!-- b001846 | furniture | pages [23] -->
m

<!-- b001847 | furniture | pages [23] -->
m

<!-- b001848 | furniture | pages [23] -->
m

<!-- b001849 | furniture | pages [23] -->
m

<!-- b001850 | furniture | pages [23] -->
m

<!-- b001851 | furniture | pages [23] -->
m

<!-- b001852 | furniture | pages [23] -->
m

<!-- b001853 | furniture | pages [23] -->
m

<!-- b001854 | furniture | pages [23] -->
m

<!-- b001855 | furniture | pages [23] -->
m

<!-- b001856 | furniture | pages [23] -->
m

<!-- b001857 | furniture | pages [23] -->
m

<!-- b001858 | furniture | pages [23] -->
m

<!-- b001859 | furniture | pages [23] -->
m

<!-- b001860 | furniture | pages [23] -->
m

<!-- b001861 | furniture | pages [23] -->
m

<!-- b001862 | furniture | pages [23] -->
m

<!-- b001863 | furniture | pages [23] -->
m

<!-- b001864 | furniture | pages [23] -->
m

<!-- b001865 | furniture | pages [23] -->
m

<!-- b001866 | furniture | pages [23] -->
m

<!-- b001867 | furniture | pages [23] -->
m

<!-- b001868 | furniture | pages [23] -->
m

<!-- b001869 | furniture | pages [23] -->
m

<!-- b001870 | furniture | pages [23] -->
m

<!-- b001871 | furniture | pages [23] -->
m

<!-- b001872 | furniture | pages [23] -->
m

<!-- b001873 | furniture | pages [23] -->
m

<!-- b001874 | furniture | pages [23] -->
m

<!-- b001875 | furniture | pages [23] -->
m

<!-- b001876 | furniture | pages [23] -->
m

<!-- b001877 | furniture | pages [23] -->
m

<!-- b001878 | furniture | pages [23] -->
m

<!-- b001879 | furniture | pages [23] -->
m

<!-- b001880 | furniture | pages [23] -->
m

<!-- b001881 | furniture | pages [23] -->
m

<!-- b001882 | furniture | pages [23] -->
m

<!-- b001883 | furniture | pages [23] -->
m

<!-- b001884 | furniture | pages [23] -->
m

<!-- b001885 | furniture | pages [23] -->
m

<!-- b001886 | furniture | pages [23] -->
m

<!-- b001887 | furniture | pages [23] -->
m

<!-- b001888 | furniture | pages [23] -->
m

<!-- b001889 | furniture | pages [23] -->
m

<!-- b001890 | furniture | pages [23] -->
m

<!-- b001891 | furniture | pages [23] -->
m

<!-- b001892 | furniture | pages [23] -->
m

<!-- b001893 | furniture | pages [23] -->
m

<!-- b001894 | furniture | pages [23] -->
m

<!-- b001895 | furniture | pages [23] -->
m

<!-- b001896 | furniture | pages [23] -->
m

<!-- b001897 | furniture | pages [23] -->
m

<!-- b001898 | furniture | pages [23] -->
m

<!-- b001899 | furniture | pages [23] -->
m

<!-- b001900 | furniture | pages [23] -->
m

<!-- b001901 | furniture | pages [23] -->
m

<!-- b001902 | furniture | pages [23] -->
m

<!-- b001903 | furniture | pages [23] -->
m

<!-- b001904 | furniture | pages [23] -->
m

<!-- b001905 | furniture | pages [23] -->
m

<!-- b001906 | furniture | pages [23] -->
m

<!-- b001907 | furniture | pages [23] -->
m

<!-- b001908 | furniture | pages [23] -->
m

<!-- b001909 | furniture | pages [23] -->
m

<!-- b001910 | furniture | pages [23] -->
m

<!-- b001911 | furniture | pages [23] -->
m

<!-- b001912 | furniture | pages [23] -->
m

<!-- b001913 | furniture | pages [23] -->
m

<!-- b001914 | furniture | pages [23] -->
m

<!-- b001915 | furniture | pages [23] -->
m

<!-- b001916 | furniture | pages [23] -->
m

<!-- b001917 | furniture | pages [23] -->
m

<!-- b001918 | furniture | pages [23] -->
m

<!-- b001919 | furniture | pages [23] -->
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

<!-- b001983 | furniture | pages [24] -->
Team # 2504188

<!-- b001984 | furniture | pages [24] -->
Page 24 of 25

<!-- b001986 | heading | pages [24] -->
10 Model Evaluation

<!-- b001987 | heading | pages [24] -->
10.1 Strengths

<!-- b001988 | prose | pages [24] -->
Visualization: We used a reasonable visualization method to make the traffic conditions in Baltimore more intuitive.

<!-- b001989 | prose | pages [24] -->
Authenticity: For each traffic project before and after optimization, the traffic conditions before and after optimization were evaluated by simulating real scenes.

<!-- b001990 | prose | pages [24] -->
Innovation: The queuing theory was innovated in combination with the specific conditions of the model; the A* algorithm was combined with the genetic algorithm to enable the algorithm to obtain the global optimal solution for the shortest path.

<!-- b001991 | heading | pages [24] -->
10.2 Weaknesses

<!-- b001992 | prose | pages [24] -->
Although approximate dynamic programming can effectively solve the problem, the time complexity of the algorithm is high and it takes a lot of time to solve it.

<!-- b001993 | heading | pages [24] -->
References

<!-- b001994 | references | pages [24] -->
[1]Biles,R.(2014).Expressways before the Interstates: The case of Detroit,

<!-- b001995 | references | pages [24] -->
1945-1956. Journal of Urban History, 40(5), pp. 843-854.

<!-- b001996 | references | pages [24] -->
[2]Fotsch, P. M. (2007). Watching the traffic go by: Transportation and isolation

<!-- b001997 | references | pages [24] -->
in urban America. Austin, TX: University of Texas Press.

<!-- b001998 | references | pages [24] -->
[3]Rothstein, R. (2014). Modern segregation. Washington, DC: Economic Policy

<!-- b001999 | references | pages [24] -->
Institute.

<!-- b002000 | references | pages [24] -->
[4]https://www.researchgate.net/publication/220045365_Multiobjective_Optimiz

<!-- b002001 | references | pages [24] -->
ation_Using_Evolutionary_Algorithms_Wiley_New_York

<!-- b002002 | references | pages [24] -->
[5]Barreto, W., Vojinovic, Z., Price, R., & Solomatine, D. (2010). Multiobjective

<!-- b002003 | references | pages [24] -->
evolutionary approach to rehabilitation of urban drainage systems. Journal of Water

<!-- b002004 | references | pages [24] -->
Resources Planning and Management-Asce, 136(5), 547–554.

<!-- b002005 | references | pages [24] -->
m

<!-- b002006 | references | pages [24] -->
m

<!-- b002007 | references | pages [24] -->
m

<!-- b002008 | references | pages [24] -->
m

<!-- b002009 | references | pages [24] -->
m

<!-- b002010 | references | pages [24] -->
m

<!-- b002011 | references | pages [24] -->
m

<!-- b002012 | references | pages [24] -->
m

<!-- b002013 | references | pages [24] -->
m

<!-- b002014 | references | pages [24] -->
m

<!-- b002015 | references | pages [24] -->
m

<!-- b002016 | references | pages [24] -->
m

<!-- b002017 | references | pages [24] -->
m

<!-- b002018 | references | pages [24] -->
m

<!-- b002019 | references | pages [24] -->
m

<!-- b002020 | references | pages [24] -->
m

<!-- b002021 | references | pages [24] -->
m

<!-- b002022 | references | pages [24] -->
m

<!-- b002023 | references | pages [24] -->
m

<!-- b002024 | references | pages [24] -->
m

<!-- b002025 | references | pages [24] -->
m

<!-- b002026 | references | pages [24] -->
m

<!-- b002027 | references | pages [24] -->
m

<!-- b002028 | references | pages [24] -->
m

<!-- b002029 | references | pages [24] -->
m

<!-- b002030 | references | pages [24] -->
m

<!-- b002031 | references | pages [24] -->
m

<!-- b002032 | references | pages [24] -->
m

<!-- b002033 | references | pages [24] -->
m

<!-- b002034 | references | pages [24] -->
m

<!-- b002035 | references | pages [24] -->
m

<!-- b002036 | references | pages [24] -->
m

<!-- b002037 | references | pages [24] -->
m

<!-- b002038 | references | pages [24] -->
m

<!-- b002039 | references | pages [24] -->
m

<!-- b002040 | references | pages [24] -->
m

<!-- b002041 | references | pages [24] -->
m

<!-- b002042 | references | pages [24] -->
m

<!-- b002043 | references | pages [24] -->
m

<!-- b002044 | references | pages [24] -->
m

<!-- b002045 | references | pages [24] -->
m

<!-- b002046 | references | pages [24] -->
m

<!-- b002047 | references | pages [24] -->
m

<!-- b002048 | references | pages [24] -->
m

<!-- b002049 | references | pages [24] -->
m

<!-- b002050 | references | pages [24] -->
m

<!-- b002051 | references | pages [24] -->
m

<!-- b002052 | references | pages [24] -->
m

<!-- b002053 | references | pages [24] -->
m

<!-- b002054 | references | pages [24] -->
m

<!-- b002055 | references | pages [24] -->
m

<!-- b002056 | references | pages [24] -->
m

<!-- b002057 | references | pages [24] -->
m

<!-- b002058 | references | pages [24] -->
m

<!-- b002059 | references | pages [24] -->
m

<!-- b002060 | references | pages [24] -->
m

<!-- b002061 | references | pages [24] -->
m

<!-- b002062 | references | pages [24] -->
m

<!-- b002063 | references | pages [24] -->
m

<!-- b002064 | references | pages [24] -->
m

<!-- b002065 | references | pages [24] -->
m

<!-- b002066 | references | pages [24] -->
m

<!-- b002067 | references | pages [24] -->
m

<!-- b002068 | references | pages [24] -->
m

<!-- b002069 | references | pages [24] -->
m

<!-- b002070 | references | pages [24] -->
m

<!-- b002071 | references | pages [24] -->
m

<!-- b002072 | references | pages [24] -->
m

<!-- b002073 | references | pages [24] -->
m

<!-- b002074 | references | pages [24] -->
m

<!-- b002075 | references | pages [24] -->
m

<!-- b002076 | references | pages [24] -->
m

<!-- b002077 | references | pages [24] -->
m

<!-- b002078 | references | pages [24] -->
m

<!-- b002079 | references | pages [24] -->
m

<!-- b002080 | references | pages [24] -->
m

<!-- b002081 | references | pages [24] -->
m

<!-- b002082 | references | pages [24] -->
m

<!-- b002083 | references | pages [24] -->
m

<!-- b002084 | references | pages [24] -->
m

<!-- b002085 | references | pages [24] -->
m

<!-- b002086 | references | pages [24] -->
m

<!-- b002087 | references | pages [24] -->
m

<!-- b002088 | references | pages [24] -->
m

<!-- b002089 | references | pages [24] -->
m

<!-- b002090 | references | pages [24] -->
m

<!-- b002091 | references | pages [24] -->
m

<!-- b002092 | references | pages [24] -->
m

<!-- b002093 | references | pages [24] -->
m

<!-- b002094 | references | pages [24] -->
m

<!-- b002095 | references | pages [24] -->
m

<!-- b002096 | references | pages [24] -->
m

<!-- b002097 | references | pages [24] -->
m

<!-- b002098 | references | pages [24] -->
m

<!-- b002099 | references | pages [24] -->
m

<!-- b002100 | references | pages [24] -->
m

<!-- b002101 | references | pages [24] -->
m

<!-- b002102 | references | pages [24] -->
m

<!-- b002103 | references | pages [24] -->
m

<!-- b002104 | references | pages [24] -->
m

<!-- b002105 | references | pages [24] -->
m

<!-- b002106 | references | pages [24] -->
m

<!-- b002107 | references | pages [24] -->
m

<!-- b002108 | references | pages [24] -->
m

<!-- b002109 | references | pages [24] -->
m

<!-- b002110 | references | pages [24] -->
m

<!-- b002111 | references | pages [24] -->
m

<!-- b002112 | references | pages [24] -->
m

<!-- b002113 | references | pages [24] -->
m

<!-- b002114 | references | pages [24] -->
m

<!-- b002115 | references | pages [24] -->
m

<!-- b002116 | references | pages [24] -->
m

<!-- b002117 | references | pages [24] -->
m

<!-- b002118 | references | pages [24] -->
m

<!-- b002119 | references | pages [24] -->
m

<!-- b002120 | references | pages [24] -->
m

<!-- b002121 | references | pages [24] -->
m

<!-- b002122 | references | pages [24] -->
m

<!-- b002123 | references | pages [24] -->
m

<!-- b002124 | references | pages [24] -->
m

<!-- b002125 | references | pages [24] -->
m

<!-- b002126 | references | pages [24] -->
m

<!-- b002127 | references | pages [24] -->
m

<!-- b002128 | references | pages [24] -->
m

<!-- b002129 | references | pages [24] -->
m

<!-- b002130 | references | pages [24] -->
m

<!-- b002131 | references | pages [24] -->
m

<!-- b002132 | references | pages [24] -->
m

<!-- b002133 | references | pages [24] -->
m

<!-- b002134 | references | pages [24] -->
m

<!-- b002135 | references | pages [24] -->
m

<!-- b002136 | references | pages [24] -->
m

<!-- b002137 | references | pages [24] -->
m

<!-- b002138 | references | pages [24] -->
m

<!-- b002139 | references | pages [24] -->
m

<!-- b002140 | references | pages [24] -->
m

<!-- b002141 | references | pages [24] -->
m

<!-- b002142 | references | pages [24] -->
m

<!-- b002143 | references | pages [24] -->
m

<!-- b002144 | references | pages [24] -->
m

<!-- b002145 | references | pages [24] -->
m

<!-- b002146 | references | pages [24] -->
m

<!-- b002147 | references | pages [24] -->
m

<!-- b002148 | references | pages [24] -->
m

<!-- b002149 | references | pages [24] -->
m

<!-- b002150 | references | pages [24] -->
m

<!-- b002151 | references | pages [24] -->
m

<!-- b002152 | references | pages [24] -->
m

<!-- b002153 | references | pages [24] -->
m

<!-- b002154 | references | pages [24] -->
m

<!-- b002155 | references | pages [24] -->
m

<!-- b002156 | references | pages [24] -->
m

<!-- b002157 | references | pages [24] -->
m

<!-- b002158 | references | pages [24] -->
m

<!-- b002159 | references | pages [24] -->
m

<!-- b002160 | references | pages [24] -->
m

<!-- b002161 | references | pages [24] -->
m

<!-- b002162 | references | pages [24] -->
m

<!-- b002163 | references | pages [24] -->
m

<!-- b002164 | references | pages [24] -->
m

<!-- b002165 | references | pages [24] -->
m

<!-- b002166 | references | pages [24] -->
m

<!-- b002167 | references | pages [24] -->
m

<!-- b002168 | references | pages [24] -->
m

<!-- b002169 | references | pages [24] -->
m

<!-- b002170 | references | pages [24] -->
m

<!-- b002171 | references | pages [24] -->
m

<!-- b002172 | references | pages [24] -->
m

<!-- b002173 | references | pages [24] -->
m

<!-- b002174 | references | pages [24] -->
m

<!-- b002175 | references | pages [24] -->
m

<!-- b002176 | references | pages [24] -->
m

<!-- b002177 | references | pages [24] -->
m

<!-- b002178 | references | pages [24] -->
m

<!-- b002179 | references | pages [24] -->
m

<!-- b002180 | references | pages [24] -->
m

<!-- b002181 | references | pages [24] -->
m

<!-- b002182 | references | pages [24] -->
m

<!-- b002183 | references | pages [24] -->
m

<!-- b002184 | references | pages [24] -->
m

<!-- b002185 | references | pages [24] -->
m

<!-- b002186 | references | pages [24] -->
m

<!-- b002187 | references | pages [24] -->
m

<!-- b002188 | references | pages [24] -->
m

<!-- b002189 | references | pages [24] -->
m

<!-- b002190 | references | pages [24] -->
m

<!-- b002191 | references | pages [24] -->
m

<!-- b002192 | references | pages [24] -->
m

<!-- b002193 | references | pages [24] -->
m

<!-- b002194 | references | pages [24] -->
m

<!-- b002195 | references | pages [24] -->
m

<!-- b002196 | references | pages [24] -->
m

<!-- b002197 | references | pages [24] -->
m

<!-- b002198 | references | pages [24] -->
m

<!-- b002199 | references | pages [24] -->
m

<!-- b002200 | references | pages [24] -->
m

<!-- b002201 | references | pages [24] -->
m

<!-- b002202 | references | pages [24] -->
m

<!-- b002203 | references | pages [24] -->
m

<!-- b002204 | references | pages [24] -->
m

<!-- b002205 | references | pages [24] -->
m

<!-- b002206 | references | pages [24] -->
m

<!-- b002207 | references | pages [24] -->
m

<!-- b002208 | references | pages [24] -->
m

<!-- b002209 | references | pages [24] -->
m

<!-- b002210 | references | pages [24] -->
m

<!-- b002211 | references | pages [24] -->
m

<!-- b002212 | references | pages [24] -->
m

<!-- b002213 | references | pages [24] -->
m

<!-- b002214 | references | pages [24] -->
m

<!-- b002215 | references | pages [24] -->
m

<!-- b002216 | references | pages [24] -->
m

<!-- b002217 | references | pages [24] -->
m

<!-- b002218 | references | pages [24] -->
m

<!-- b002219 | references | pages [24] -->
m

<!-- b002220 | references | pages [24] -->
m

<!-- b002221 | references | pages [24] -->
m

<!-- b002222 | references | pages [24] -->
m

<!-- b002223 | references | pages [24] -->
m

<!-- b002224 | references | pages [24] -->
m

<!-- b002225 | references | pages [24] -->
m

<!-- b002226 | references | pages [24] -->
m

<!-- b002227 | references | pages [24] -->
m

<!-- b002228 | references | pages [24] -->
m

<!-- b002229 | references | pages [24] -->
m

<!-- b002230 | references | pages [24] -->
m

<!-- b002231 | references | pages [24] -->
m

<!-- b002232 | references | pages [24] -->
m

<!-- b002233 | references | pages [24] -->
m

<!-- b002234 | references | pages [24] -->
m

<!-- b002235 | references | pages [24] -->
m

<!-- b002236 | references | pages [24] -->
m

<!-- b002237 | references | pages [24] -->
m

<!-- b002238 | references | pages [24] -->
m

<!-- b002239 | references | pages [24] -->
m

<!-- b002240 | references | pages [24] -->
m

<!-- b002241 | references | pages [24] -->
m

<!-- b002242 | references | pages [24] -->
m

<!-- b002243 | references | pages [24] -->
m

<!-- b002244 | references | pages [24] -->
m

<!-- b002245 | references | pages [24] -->
m

<!-- b002246 | references | pages [24] -->
m

<!-- b002247 | references | pages [24] -->
m

<!-- b002248 | references | pages [24] -->
m

<!-- b002249 | references | pages [24] -->
m

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
m

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
m

<!-- b002584 | references | pages [24] -->
m

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
关注数学模型

<!-- b002693 | furniture | pages [24] -->
2

<!-- b002694 | furniture | pages [24] -->
MATHmodels

<!-- b002695 | furniture | pages [24] -->
获取更多资讯

<!-- b002696 | furniture | pages [25] -->
Team # 2504188

<!-- b002697 | furniture | pages [25] -->
Page 25 of 25

<!-- b002698 | references | pages [25] -->
微信公众号：数学模型

<!-- b002699 | references | pages [25] -->
微信号：MATHmodels

<!-- b002700 | references | pages [25] -->
m

<!-- b002701 | references | pages [25] -->
m

<!-- b002702 | references | pages [25] -->
m

<!-- b002703 | references | pages [25] -->
m

<!-- b002704 | references | pages [25] -->
m

<!-- b002705 | references | pages [25] -->
m

<!-- b002706 | references | pages [25] -->
m

<!-- b002707 | references | pages [25] -->
m

<!-- b002708 | references | pages [25] -->
m

<!-- b002709 | references | pages [25] -->
m

<!-- b002710 | references | pages [25] -->
m

<!-- b002711 | references | pages [25] -->
m

<!-- b002712 | references | pages [25] -->
m

<!-- b002713 | references | pages [25] -->
m

<!-- b002714 | references | pages [25] -->
m

<!-- b002715 | references | pages [25] -->
m

<!-- b002716 | references | pages [25] -->
m

<!-- b002717 | references | pages [25] -->
m

<!-- b002718 | references | pages [25] -->
m

<!-- b002719 | references | pages [25] -->
m

<!-- b002720 | references | pages [25] -->
m

<!-- b002721 | references | pages [25] -->
m

<!-- b002722 | references | pages [25] -->
m

<!-- b002723 | references | pages [25] -->
m

<!-- b002724 | references | pages [25] -->
m

<!-- b002725 | references | pages [25] -->
m

<!-- b002726 | references | pages [25] -->
m

<!-- b002727 | references | pages [25] -->
m

<!-- b002728 | references | pages [25] -->
m

<!-- b002729 | references | pages [25] -->
m

<!-- b002730 | references | pages [25] -->
m

<!-- b002731 | references | pages [25] -->
m

<!-- b002732 | references | pages [25] -->
m

<!-- b002733 | references | pages [25] -->
m

<!-- b002734 | references | pages [25] -->
m

<!-- b002735 | references | pages [25] -->
m

<!-- b002736 | references | pages [25] -->
m

<!-- b002737 | references | pages [25] -->
m

<!-- b002738 | references | pages [25] -->
m

<!-- b002739 | references | pages [25] -->
m

<!-- b002740 | references | pages [25] -->
m

<!-- b002741 | references | pages [25] -->
m

<!-- b002742 | references | pages [25] -->
m

<!-- b002743 | references | pages [25] -->
m

<!-- b002744 | references | pages [25] -->
m

<!-- b002745 | references | pages [25] -->
m

<!-- b002746 | references | pages [25] -->
m

<!-- b002747 | references | pages [25] -->
m

<!-- b002748 | references | pages [25] -->
m

<!-- b002749 | references | pages [25] -->
m

<!-- b002750 | references | pages [25] -->
m

<!-- b002751 | references | pages [25] -->
m

<!-- b002752 | references | pages [25] -->
m

<!-- b002753 | references | pages [25] -->
m

<!-- b002754 | references | pages [25] -->
m

<!-- b002755 | references | pages [25] -->
m

<!-- b002756 | references | pages [25] -->
m

<!-- b002757 | references | pages [25] -->
m

<!-- b002758 | references | pages [25] -->
m

<!-- b002759 | references | pages [25] -->
m

<!-- b002760 | references | pages [25] -->
m

<!-- b002761 | references | pages [25] -->
m

<!-- b002762 | references | pages [25] -->
m

<!-- b002763 | references | pages [25] -->
m

<!-- b002764 | references | pages [25] -->
m

<!-- b002765 | references | pages [25] -->
m

<!-- b002766 | references | pages [25] -->
m

<!-- b002767 | references | pages [25] -->
m

<!-- b002768 | references | pages [25] -->
m

<!-- b002769 | references | pages [25] -->
m

<!-- b002770 | references | pages [25] -->
m

<!-- b002771 | references | pages [25] -->
m

<!-- b002772 | references | pages [25] -->
m

<!-- b002773 | references | pages [25] -->
m

<!-- b002774 | references | pages [25] -->
m

<!-- b002775 | references | pages [25] -->
m

<!-- b002776 | references | pages [25] -->
m

<!-- b002777 | references | pages [25] -->
m

<!-- b002778 | references | pages [25] -->
m

<!-- b002779 | references | pages [25] -->
m

<!-- b002780 | references | pages [25] -->
m

<!-- b002781 | references | pages [25] -->
m

<!-- b002782 | references | pages [25] -->
m

<!-- b002783 | references | pages [25] -->
m

<!-- b002784 | references | pages [25] -->
m

<!-- b002785 | references | pages [25] -->
m

<!-- b002786 | references | pages [25] -->
m

<!-- b002787 | references | pages [25] -->
m

<!-- b002788 | references | pages [25] -->
m

<!-- b002789 | references | pages [25] -->
m

<!-- b002790 | references | pages [25] -->
m

<!-- b002791 | references | pages [25] -->
m

<!-- b002792 | references | pages [25] -->
m

<!-- b002793 | references | pages [25] -->
m

<!-- b002794 | references | pages [25] -->
m

<!-- b002795 | references | pages [25] -->
m

<!-- b002796 | references | pages [25] -->
m

<!-- b002797 | references | pages [25] -->
m

<!-- b002798 | references | pages [25] -->
m

<!-- b002799 | references | pages [25] -->
m

<!-- b002800 | references | pages [25] -->
m

<!-- b002801 | references | pages [25] -->
m

<!-- b002802 | references | pages [25] -->
m

<!-- b002803 | references | pages [25] -->
m

<!-- b002804 | references | pages [25] -->
m

<!-- b002805 | references | pages [25] -->
m

<!-- b002806 | references | pages [25] -->
m

<!-- b002807 | references | pages [25] -->
m

<!-- b002808 | references | pages [25] -->
m

<!-- b002809 | references | pages [25] -->
m

<!-- b002810 | references | pages [25] -->
m

<!-- b002811 | references | pages [25] -->
m

<!-- b002812 | references | pages [25] -->
m

<!-- b002813 | references | pages [25] -->
m

<!-- b002814 | references | pages [25] -->
m

<!-- b002815 | references | pages [25] -->
m

<!-- b002816 | references | pages [25] -->
m

<!-- b002817 | references | pages [25] -->
m

<!-- b002818 | references | pages [25] -->
m

<!-- b002819 | references | pages [25] -->
m

<!-- b002820 | references | pages [25] -->
m

<!-- b002821 | references | pages [25] -->
m

<!-- b002822 | references | pages [25] -->
m

<!-- b002823 | references | pages [25] -->
m

<!-- b002824 | references | pages [25] -->
m

<!-- b002825 | references | pages [25] -->
m

<!-- b002826 | references | pages [25] -->
m

<!-- b002827 | references | pages [25] -->
m

<!-- b002828 | references | pages [25] -->
m

<!-- b002829 | references | pages [25] -->
m

<!-- b002830 | references | pages [25] -->
m

<!-- b002831 | references | pages [25] -->
m

<!-- b002832 | references | pages [25] -->
m

<!-- b002833 | references | pages [25] -->
m

<!-- b002834 | references | pages [25] -->
m

<!-- b002835 | references | pages [25] -->
m

<!-- b002836 | references | pages [25] -->
m

<!-- b002837 | references | pages [25] -->
m

<!-- b002838 | references | pages [25] -->
m

<!-- b002839 | references | pages [25] -->
m

<!-- b002840 | references | pages [25] -->
m

<!-- b002841 | references | pages [25] -->
m

<!-- b002842 | references | pages [25] -->
m

<!-- b002843 | references | pages [25] -->
m

<!-- b002844 | references | pages [25] -->
m

<!-- b002845 | references | pages [25] -->
m

<!-- b002846 | references | pages [25] -->
m

<!-- b002847 | references | pages [25] -->
m

<!-- b002848 | references | pages [25] -->
m

<!-- b002849 | references | pages [25] -->
m

<!-- b002850 | references | pages [25] -->
m

<!-- b002851 | references | pages [25] -->
m

<!-- b002852 | references | pages [25] -->
m

<!-- b002853 | references | pages [25] -->
m

<!-- b002854 | references | pages [25] -->
m

<!-- b002855 | references | pages [25] -->
m

<!-- b002856 | references | pages [25] -->
m

<!-- b002857 | references | pages [25] -->
m

<!-- b002858 | references | pages [25] -->
m

<!-- b002859 | references | pages [25] -->
m

<!-- b002860 | references | pages [25] -->
m

<!-- b002861 | references | pages [25] -->
m

<!-- b002862 | references | pages [25] -->
m

<!-- b002863 | references | pages [25] -->
m

<!-- b002864 | references | pages [25] -->
m

<!-- b002865 | references | pages [25] -->
m

<!-- b002866 | references | pages [25] -->
m

<!-- b002867 | references | pages [25] -->
m

<!-- b002868 | references | pages [25] -->
m

<!-- b002869 | references | pages [25] -->
m

<!-- b002870 | references | pages [25] -->
m

<!-- b002871 | references | pages [25] -->
m

<!-- b002872 | references | pages [25] -->
m

<!-- b002873 | references | pages [25] -->
m

<!-- b002874 | references | pages [25] -->
m

<!-- b002875 | references | pages [25] -->
m

<!-- b002876 | references | pages [25] -->
m

<!-- b002877 | references | pages [25] -->
m

<!-- b002878 | references | pages [25] -->
m

<!-- b002879 | references | pages [25] -->
m

<!-- b002880 | references | pages [25] -->
m

<!-- b002881 | references | pages [25] -->
m

<!-- b002882 | references | pages [25] -->
m

<!-- b002883 | references | pages [25] -->
m

<!-- b002884 | references | pages [25] -->
m

<!-- b002885 | references | pages [25] -->
m

<!-- b002886 | references | pages [25] -->
m

<!-- b002887 | references | pages [25] -->
m

<!-- b002888 | references | pages [25] -->
m

<!-- b002889 | references | pages [25] -->
m

<!-- b002890 | references | pages [25] -->
m

<!-- b002891 | references | pages [25] -->
m

<!-- b002892 | references | pages [25] -->
m

<!-- b002893 | references | pages [25] -->
m

<!-- b002894 | references | pages [25] -->
m

<!-- b002895 | references | pages [25] -->
m

<!-- b002896 | references | pages [25] -->
m

<!-- b002897 | references | pages [25] -->
m

<!-- b002898 | references | pages [25] -->
m

<!-- b002899 | references | pages [25] -->
m

<!-- b002900 | references | pages [25] -->
m

<!-- b002901 | references | pages [25] -->
m

<!-- b002902 | references | pages [25] -->
m

<!-- b002903 | references | pages [25] -->
m

<!-- b002904 | references | pages [25] -->
m

<!-- b002905 | references | pages [25] -->
m

<!-- b002906 | references | pages [25] -->
m

<!-- b002907 | references | pages [25] -->
m

<!-- b002908 | references | pages [25] -->
m

<!-- b002909 | references | pages [25] -->
m

<!-- b002910 | references | pages [25] -->
m

<!-- b002911 | references | pages [25] -->
m

<!-- b002912 | references | pages [25] -->
m

<!-- b002913 | references | pages [25] -->
m

<!-- b002914 | references | pages [25] -->
m

<!-- b002915 | references | pages [25] -->
m

<!-- b002916 | references | pages [25] -->
m

<!-- b002917 | references | pages [25] -->
m

<!-- b002918 | references | pages [25] -->
m

<!-- b002919 | references | pages [25] -->
m

<!-- b002920 | references | pages [25] -->
m

<!-- b002921 | references | pages [25] -->
m

<!-- b002922 | references | pages [25] -->
m

<!-- b002923 | references | pages [25] -->
m

<!-- b002924 | references | pages [25] -->
m

<!-- b002925 | references | pages [25] -->
m

<!-- b002926 | references | pages [25] -->
m

<!-- b002927 | references | pages [25] -->
m

<!-- b002928 | references | pages [25] -->
m

<!-- b002929 | references | pages [25] -->
m

<!-- b002930 | furniture | pages [25] -->
m

<!-- b002931 | furniture | pages [25] -->
m

<!-- b002932 | furniture | pages [25] -->
m

<!-- b002933 | furniture | pages [25] -->
m

<!-- b002934 | furniture | pages [25] -->
m

<!-- b002935 | furniture | pages [25] -->
m

<!-- b002936 | furniture | pages [25] -->
m

<!-- b002937 | furniture | pages [25] -->
m

<!-- b002938 | furniture | pages [25] -->
m

<!-- b002939 | furniture | pages [25] -->
m

<!-- b002940 | furniture | pages [25] -->
m

<!-- b002941 | furniture | pages [25] -->
m

<!-- b002942 | furniture | pages [25] -->
m

<!-- b002943 | furniture | pages [25] -->
m

<!-- b002944 | furniture | pages [25] -->
m

<!-- b002945 | furniture | pages [25] -->
m

<!-- b002946 | furniture | pages [25] -->
m

<!-- b002947 | furniture | pages [25] -->
m

<!-- b002948 | furniture | pages [25] -->
m

<!-- b002949 | furniture | pages [25] -->
m

<!-- b002950 | furniture | pages [25] -->
m

<!-- b002951 | furniture | pages [25] -->
m

<!-- b002952 | furniture | pages [25] -->
m

<!-- b002953 | furniture | pages [25] -->
m

<!-- b002954 | furniture | pages [25] -->
m

<!-- b002955 | furniture | pages [25] -->
m

<!-- b002956 | furniture | pages [25] -->
m

<!-- b002957 | furniture | pages [25] -->
m

<!-- b002958 | furniture | pages [25] -->
m

<!-- b002959 | furniture | pages [25] -->
m

<!-- b002960 | furniture | pages [25] -->
m

<!-- b002961 | furniture | pages [25] -->
m

<!-- b002962 | furniture | pages [25] -->
m

<!-- b002963 | furniture | pages [25] -->
m

<!-- b002964 | furniture | pages [25] -->
m

<!-- b002965 | furniture | pages [25] -->
m

<!-- b002966 | furniture | pages [25] -->
m

<!-- b002967 | furniture | pages [25] -->
m

<!-- b002968 | furniture | pages [25] -->
m

<!-- b002969 | furniture | pages [25] -->
m

<!-- b002970 | furniture | pages [25] -->
m

<!-- b002971 | furniture | pages [25] -->
m

<!-- b002972 | furniture | pages [25] -->
m

<!-- b002973 | furniture | pages [25] -->
m

<!-- b002974 | furniture | pages [25] -->
m

<!-- b002975 | furniture | pages [25] -->
m

<!-- b002976 | furniture | pages [25] -->
m

<!-- b002977 | furniture | pages [25] -->
m

<!-- b002978 | furniture | pages [25] -->
m

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

<!-- b003254 | furniture | pages [26] -->
Team # 2504188

<!-- b003255 | furniture | pages [26] -->
Page 26 of 25

<!-- b003256 | references | pages [26] -->
m

<!-- b003257 | references | pages [26] -->
m

<!-- b003258 | references | pages [26] -->
m

<!-- b003259 | references | pages [26] -->
m

<!-- b003260 | references | pages [26] -->
m

<!-- b003261 | references | pages [26] -->
m

<!-- b003262 | references | pages [26] -->
m

<!-- b003263 | references | pages [26] -->
m

<!-- b003264 | references | pages [26] -->
m

<!-- b003265 | references | pages [26] -->
m

<!-- b003266 | references | pages [26] -->
m

<!-- b003267 | references | pages [26] -->
m

<!-- b003268 | references | pages [26] -->
m

<!-- b003269 | references | pages [26] -->
m

<!-- b003270 | references | pages [26] -->
m

<!-- b003271 | references | pages [26] -->
m

<!-- b003272 | references | pages [26] -->
m

<!-- b003273 | references | pages [26] -->
m

<!-- b003274 | references | pages [26] -->
m

<!-- b003275 | references | pages [26] -->
m

<!-- b003276 | references | pages [26] -->
m

<!-- b003277 | references | pages [26] -->
m

<!-- b003278 | references | pages [26] -->
m

<!-- b003279 | references | pages [26] -->
m

<!-- b003280 | references | pages [26] -->
m

<!-- b003281 | references | pages [26] -->
m

<!-- b003282 | references | pages [26] -->
m

<!-- b003283 | references | pages [26] -->
m

<!-- b003284 | references | pages [26] -->
m

<!-- b003285 | references | pages [26] -->
m

<!-- b003286 | references | pages [26] -->
m

<!-- b003287 | references | pages [26] -->
m

<!-- b003288 | references | pages [26] -->
m

<!-- b003289 | references | pages [26] -->
m

<!-- b003290 | references | pages [26] -->
m

<!-- b003291 | references | pages [26] -->
m

<!-- b003292 | references | pages [26] -->
m

<!-- b003293 | references | pages [26] -->
m

<!-- b003294 | references | pages [26] -->
m

<!-- b003295 | references | pages [26] -->
m

<!-- b003296 | references | pages [26] -->
m

<!-- b003297 | references | pages [26] -->
m

<!-- b003298 | references | pages [26] -->
m

<!-- b003299 | references | pages [26] -->
m

<!-- b003300 | references | pages [26] -->
m

<!-- b003301 | references | pages [26] -->
m

<!-- b003302 | references | pages [26] -->
m

<!-- b003303 | references | pages [26] -->
m

<!-- b003304 | references | pages [26] -->
m

<!-- b003305 | references | pages [26] -->
m

<!-- b003306 | references | pages [26] -->
m

<!-- b003307 | references | pages [26] -->
m

<!-- b003308 | references | pages [26] -->
m

<!-- b003309 | references | pages [26] -->
m

<!-- b003310 | references | pages [26] -->
m

<!-- b003311 | references | pages [26] -->
m

<!-- b003312 | references | pages [26] -->
m

<!-- b003313 | references | pages [26] -->
m

<!-- b003314 | references | pages [26] -->
m

<!-- b003315 | references | pages [26] -->
m

<!-- b003316 | references | pages [26] -->
m

<!-- b003317 | references | pages [26] -->
m

<!-- b003318 | references | pages [26] -->
m

<!-- b003319 | references | pages [26] -->
m

<!-- b003320 | references | pages [26] -->
m

<!-- b003321 | references | pages [26] -->
m

<!-- b003322 | references | pages [26] -->
m

<!-- b003323 | references | pages [26] -->
m

<!-- b003324 | references | pages [26] -->
m

<!-- b003325 | references | pages [26] -->
m

<!-- b003326 | references | pages [26] -->
m

<!-- b003327 | references | pages [26] -->
m

<!-- b003328 | references | pages [26] -->
m

<!-- b003329 | references | pages [26] -->
m

<!-- b003330 | references | pages [26] -->
m

<!-- b003331 | references | pages [26] -->
m

<!-- b003332 | references | pages [26] -->
m

<!-- b003333 | references | pages [26] -->
m

<!-- b003334 | references | pages [26] -->
m

<!-- b003335 | references | pages [26] -->
m

<!-- b003336 | references | pages [26] -->
m

<!-- b003337 | references | pages [26] -->
m

<!-- b003338 | references | pages [26] -->
m

<!-- b003339 | references | pages [26] -->
m

<!-- b003340 | references | pages [26] -->
m

<!-- b003341 | references | pages [26] -->
m

<!-- b003342 | references | pages [26] -->
m

<!-- b003343 | references | pages [26] -->
m

<!-- b003344 | references | pages [26] -->
m

<!-- b003345 | references | pages [26] -->
m

<!-- b003346 | references | pages [26] -->
m

<!-- b003347 | references | pages [26] -->
m

<!-- b003348 | references | pages [26] -->
m

<!-- b003349 | references | pages [26] -->
m

<!-- b003350 | references | pages [26] -->
m

<!-- b003351 | references | pages [26] -->
m

<!-- b003352 | references | pages [26] -->
m

<!-- b003353 | references | pages [26] -->
m

<!-- b003354 | references | pages [26] -->
m

<!-- b003355 | references | pages [26] -->
m

<!-- b003356 | references | pages [26] -->
m

<!-- b003357 | references | pages [26] -->
m

<!-- b003358 | references | pages [26] -->
m

<!-- b003359 | references | pages [26] -->
m

<!-- b003360 | references | pages [26] -->
m

<!-- b003361 | references | pages [26] -->
m

<!-- b003362 | references | pages [26] -->
m

<!-- b003363 | references | pages [26] -->
m

<!-- b003364 | references | pages [26] -->
m

<!-- b003365 | references | pages [26] -->
m

<!-- b003366 | references | pages [26] -->
m

<!-- b003367 | references | pages [26] -->
m

<!-- b003368 | references | pages [26] -->
m

<!-- b003369 | references | pages [26] -->
m

<!-- b003370 | references | pages [26] -->
m

<!-- b003371 | references | pages [26] -->
m

<!-- b003372 | references | pages [26] -->
m

<!-- b003373 | references | pages [26] -->
m

<!-- b003374 | references | pages [26] -->
m

<!-- b003375 | references | pages [26] -->
m

<!-- b003376 | references | pages [26] -->
m

<!-- b003377 | references | pages [26] -->
m

<!-- b003378 | references | pages [26] -->
m

<!-- b003379 | references | pages [26] -->
m

<!-- b003380 | references | pages [26] -->
m

<!-- b003381 | references | pages [26] -->
m

<!-- b003382 | references | pages [26] -->
m

<!-- b003383 | references | pages [26] -->
m

<!-- b003384 | references | pages [26] -->
m

<!-- b003385 | references | pages [26] -->
m

<!-- b003386 | references | pages [26] -->
m

<!-- b003387 | references | pages [26] -->
m

<!-- b003388 | references | pages [26] -->
m

<!-- b003389 | references | pages [26] -->
m

<!-- b003390 | references | pages [26] -->
m

<!-- b003391 | references | pages [26] -->
m

<!-- b003392 | references | pages [26] -->
m

<!-- b003393 | references | pages [26] -->
m

<!-- b003394 | references | pages [26] -->
m

<!-- b003395 | references | pages [26] -->
m

<!-- b003396 | references | pages [26] -->
m

<!-- b003397 | references | pages [26] -->
m

<!-- b003398 | references | pages [26] -->
m

<!-- b003399 | references | pages [26] -->
m

<!-- b003400 | references | pages [26] -->
m

<!-- b003401 | references | pages [26] -->
m

<!-- b003402 | references | pages [26] -->
m

<!-- b003403 | references | pages [26] -->
m

<!-- b003404 | references | pages [26] -->
m

<!-- b003405 | references | pages [26] -->
m

<!-- b003406 | references | pages [26] -->
m

<!-- b003407 | references | pages [26] -->
m

<!-- b003408 | references | pages [26] -->
m

<!-- b003409 | references | pages [26] -->
m

<!-- b003410 | references | pages [26] -->
m

<!-- b003411 | references | pages [26] -->
m

<!-- b003412 | references | pages [26] -->
m

<!-- b003413 | references | pages [26] -->
m

<!-- b003414 | references | pages [26] -->
m

<!-- b003415 | references | pages [26] -->
m

<!-- b003416 | references | pages [26] -->
m

<!-- b003417 | references | pages [26] -->
m

<!-- b003418 | references | pages [26] -->
m

<!-- b003419 | references | pages [26] -->
m

<!-- b003420 | references | pages [26] -->
m

<!-- b003421 | references | pages [26] -->
m

<!-- b003422 | references | pages [26] -->
m

<!-- b003423 | references | pages [26] -->
m

<!-- b003424 | references | pages [26] -->
m

<!-- b003425 | references | pages [26] -->
m

<!-- b003426 | references | pages [26] -->
m

<!-- b003427 | references | pages [26] -->
m

<!-- b003428 | references | pages [26] -->
m

<!-- b003429 | references | pages [26] -->
m

<!-- b003430 | references | pages [26] -->
m

<!-- b003431 | references | pages [26] -->
m

<!-- b003432 | references | pages [26] -->
m

<!-- b003433 | references | pages [26] -->
m

<!-- b003434 | references | pages [26] -->
m

<!-- b003435 | references | pages [26] -->
m

<!-- b003436 | references | pages [26] -->
m

<!-- b003437 | references | pages [26] -->
m

<!-- b003438 | references | pages [26] -->
m

<!-- b003439 | references | pages [26] -->
m

<!-- b003440 | references | pages [26] -->
m

<!-- b003441 | references | pages [26] -->
m

<!-- b003442 | references | pages [26] -->
m

<!-- b003443 | references | pages [26] -->
m

<!-- b003444 | references | pages [26] -->
m

<!-- b003445 | references | pages [26] -->
m

<!-- b003446 | references | pages [26] -->
m

<!-- b003447 | references | pages [26] -->
m

<!-- b003448 | references | pages [26] -->
m

<!-- b003449 | references | pages [26] -->
m

<!-- b003450 | references | pages [26] -->
m

<!-- b003451 | references | pages [26] -->
m

<!-- b003452 | references | pages [26] -->
m

<!-- b003453 | references | pages [26] -->
m

<!-- b003454 | references | pages [26] -->
m

<!-- b003455 | references | pages [26] -->
m

<!-- b003456 | references | pages [26] -->
m

<!-- b003457 | references | pages [26] -->
m

<!-- b003458 | references | pages [26] -->
m

<!-- b003459 | references | pages [26] -->
m

<!-- b003460 | references | pages [26] -->
m

<!-- b003461 | references | pages [26] -->
m

<!-- b003462 | references | pages [26] -->
m

<!-- b003463 | references | pages [26] -->
m

<!-- b003464 | references | pages [26] -->
m

<!-- b003465 | references | pages [26] -->
m

<!-- b003466 | references | pages [26] -->
m

<!-- b003467 | references | pages [26] -->
m

<!-- b003468 | references | pages [26] -->
m

<!-- b003469 | references | pages [26] -->
m

<!-- b003470 | references | pages [26] -->
m

<!-- b003471 | references | pages [26] -->
m

<!-- b003472 | references | pages [26] -->
m

<!-- b003473 | references | pages [26] -->
m

<!-- b003474 | references | pages [26] -->
m

<!-- b003475 | references | pages [26] -->
m

<!-- b003476 | references | pages [26] -->
m

<!-- b003477 | references | pages [26] -->
m

<!-- b003478 | references | pages [26] -->
m

<!-- b003479 | references | pages [26] -->
m

<!-- b003480 | references | pages [26] -->
m

<!-- b003481 | references | pages [26] -->
m

<!-- b003482 | references | pages [26] -->
m

<!-- b003483 | references | pages [26] -->
m

<!-- b003484 | references | pages [26] -->
m

<!-- b003485 | references | pages [26] -->
m

<!-- b003486 | references | pages [26] -->
m

<!-- b003487 | references | pages [26] -->
m

<!-- b003488 | references | pages [26] -->
m

<!-- b003489 | references | pages [26] -->
m

<!-- b003490 | references | pages [26] -->
m

<!-- b003491 | references | pages [26] -->
m

<!-- b003492 | references | pages [26] -->
m

<!-- b003493 | references | pages [26] -->
m

<!-- b003494 | references | pages [26] -->
m

<!-- b003495 | references | pages [26] -->
m

<!-- b003496 | references | pages [26] -->
m

<!-- b003497 | references | pages [26] -->
m

<!-- b003498 | references | pages [26] -->
m

<!-- b003499 | references | pages [26] -->
m

<!-- b003500 | references | pages [26] -->
m

<!-- b003501 | references | pages [26] -->
m

<!-- b003502 | references | pages [26] -->
m

<!-- b003503 | references | pages [26] -->
m

<!-- b003504 | references | pages [26] -->
m

<!-- b003505 | references | pages [26] -->
m

<!-- b003506 | references | pages [26] -->
m

<!-- b003507 | references | pages [26] -->
m

<!-- b003508 | references | pages [26] -->
m

<!-- b003509 | references | pages [26] -->
m

<!-- b003510 | references | pages [26] -->
m

<!-- b003511 | references | pages [26] -->
m

<!-- b003512 | references | pages [26] -->
m

<!-- b003513 | references | pages [26] -->
m

<!-- b003514 | references | pages [26] -->
m

<!-- b003515 | references | pages [26] -->
m

<!-- b003516 | references | pages [26] -->
m

<!-- b003517 | references | pages [26] -->
m

<!-- b003518 | references | pages [26] -->
m

<!-- b003519 | references | pages [26] -->
m

<!-- b003520 | references | pages [26] -->
m

<!-- b003521 | references | pages [26] -->
m

<!-- b003522 | references | pages [26] -->
m

<!-- b003523 | references | pages [26] -->
m

<!-- b003524 | references | pages [26] -->
m

<!-- b003525 | references | pages [26] -->
m

<!-- b003526 | references | pages [26] -->
m

<!-- b003527 | references | pages [26] -->
m

<!-- b003528 | references | pages [26] -->
m

<!-- b003529 | references | pages [26] -->
m

<!-- b003530 | references | pages [26] -->
m

<!-- b003531 | references | pages [26] -->
m

<!-- b003532 | references | pages [26] -->
m

<!-- b003533 | references | pages [26] -->
m

<!-- b003534 | references | pages [26] -->
m

<!-- b003535 | references | pages [26] -->
m

<!-- b003536 | references | pages [26] -->
m

<!-- b003537 | references | pages [26] -->
m

<!-- b003538 | references | pages [26] -->
m

<!-- b003539 | references | pages [26] -->
m

<!-- b003540 | references | pages [26] -->
关注数学模型

<!-- b003541 | references | pages [26] -->
m

<!-- b003542 | references | pages [26] -->
m

<!-- b003543 | references | pages [26] -->
m

<!-- b003544 | references | pages [26] -->
m

<!-- b003545 | references | pages [26] -->
m

<!-- b003546 | references | pages [26] -->
m

<!-- b003547 | references | pages [26] -->
m

<!-- b003548 | references | pages [26] -->
m

<!-- b003549 | references | pages [26] -->
m

<!-- b003550 | references | pages [26] -->
m

<!-- b003551 | references | pages [26] -->
m

<!-- b003552 | references | pages [26] -->
m

<!-- b003553 | references | pages [26] -->
m

<!-- b003554 | references | pages [26] -->
m

<!-- b003555 | references | pages [26] -->
m

<!-- b003556 | references | pages [26] -->
m

<!-- b003557 | references | pages [26] -->
m

<!-- b003558 | references | pages [26] -->
m

<!-- b003559 | references | pages [26] -->
m

<!-- b003560 | references | pages [26] -->
m

<!-- b003561 | references | pages [26] -->
m

<!-- b003562 | references | pages [26] -->
m

<!-- b003563 | references | pages [26] -->
m

<!-- b003564 | references | pages [26] -->
m

<!-- b003565 | references | pages [26] -->
m

<!-- b003566 | references | pages [26] -->
m

<!-- b003567 | references | pages [26] -->
m

<!-- b003568 | references | pages [26] -->
m

<!-- b003569 | references | pages [26] -->
m

<!-- b003570 | references | pages [26] -->
m

<!-- b003571 | references | pages [26] -->
m

<!-- b003572 | references | pages [26] -->
m

<!-- b003573 | references | pages [26] -->
m

<!-- b003574 | references | pages [26] -->
m

<!-- b003575 | references | pages [26] -->
m

<!-- b003576 | references | pages [26] -->
m

<!-- b003577 | references | pages [26] -->
m

<!-- b003578 | references | pages [26] -->
m

<!-- b003579 | references | pages [26] -->
m

<!-- b003580 | references | pages [26] -->
m

<!-- b003581 | references | pages [26] -->
m

<!-- b003582 | references | pages [26] -->
m

<!-- b003583 | references | pages [26] -->
m

<!-- b003584 | references | pages [26] -->
m

<!-- b003585 | references | pages [26] -->
m

<!-- b003586 | references | pages [26] -->
m

<!-- b003587 | references | pages [26] -->
m

<!-- b003588 | references | pages [26] -->
m

<!-- b003589 | references | pages [26] -->
m

<!-- b003590 | references | pages [26] -->
m

<!-- b003591 | references | pages [26] -->
m

<!-- b003592 | references | pages [26] -->
m

<!-- b003593 | references | pages [26] -->
m

<!-- b003594 | references | pages [26] -->
m

<!-- b003595 | references | pages [26] -->
m

<!-- b003596 | references | pages [26] -->
m

<!-- b003597 | references | pages [26] -->
m

<!-- b003598 | references | pages [26] -->
m

<!-- b003599 | references | pages [26] -->
m

<!-- b003600 | references | pages [26] -->
m

<!-- b003601 | references | pages [26] -->
m

<!-- b003602 | references | pages [26] -->
m

<!-- b003603 | references | pages [26] -->
m

<!-- b003604 | references | pages [26] -->
m

<!-- b003605 | furniture | pages [26] -->
2

<!-- b003606 | references | pages [26] -->
m

<!-- b003607 | references | pages [26] -->
m

<!-- b003608 | references | pages [26] -->
m

<!-- b003609 | references | pages [26] -->
m

<!-- b003610 | references | pages [26] -->
m

<!-- b003611 | references | pages [26] -->
m

<!-- b003612 | references | pages [26] -->
m

<!-- b003613 | references | pages [26] -->
m

<!-- b003614 | references | pages [26] -->
m

<!-- b003615 | references | pages [26] -->
m

<!-- b003616 | references | pages [26] -->
m

<!-- b003617 | references | pages [26] -->
m

<!-- b003618 | references | pages [26] -->
m

<!-- b003619 | references | pages [26] -->
m

<!-- b003620 | references | pages [26] -->
m

<!-- b003621 | references | pages [26] -->
m

<!-- b003622 | references | pages [26] -->
m

<!-- b003623 | references | pages [26] -->
m

<!-- b003624 | references | pages [26] -->
m

<!-- b003625 | references | pages [26] -->
m

<!-- b003626 | references | pages [26] -->
m

<!-- b003627 | references | pages [26] -->
m

<!-- b003628 | references | pages [26] -->
m

<!-- b003629 | furniture | pages [26] -->
m

<!-- b003630 | furniture | pages [26] -->
m

<!-- b003631 | furniture | pages [26] -->
m

<!-- b003632 | furniture | pages [26] -->
m

<!-- b003633 | furniture | pages [26] -->
m

<!-- b003634 | furniture | pages [26] -->
m

<!-- b003635 | furniture | pages [26] -->
m

<!-- b003636 | furniture | pages [26] -->
m

<!-- b003637 | furniture | pages [26] -->
m

<!-- b003638 | furniture | pages [26] -->
m

<!-- b003639 | furniture | pages [26] -->
m

<!-- b003640 | furniture | pages [26] -->
m

<!-- b003641 | furniture | pages [26] -->
m

<!-- b003642 | furniture | pages [26] -->
m

<!-- b003643 | furniture | pages [26] -->
m

<!-- b003644 | furniture | pages [26] -->
m

<!-- b003645 | furniture | pages [26] -->
m

<!-- b003646 | furniture | pages [26] -->
m

<!-- b003647 | furniture | pages [26] -->
m

<!-- b003648 | furniture | pages [26] -->
m

<!-- b003649 | furniture | pages [26] -->
m

<!-- b003650 | furniture | pages [26] -->
m

<!-- b003651 | furniture | pages [26] -->
m

<!-- b003652 | furniture | pages [26] -->
m

<!-- b003653 | furniture | pages [26] -->
m

<!-- b003654 | furniture | pages [26] -->
m

<!-- b003655 | furniture | pages [26] -->
m

<!-- b003656 | furniture | pages [26] -->
m

<!-- b003657 | furniture | pages [26] -->
m

<!-- b003658 | furniture | pages [26] -->
m

<!-- b003659 | furniture | pages [26] -->
m

<!-- b003660 | furniture | pages [26] -->
m

<!-- b003661 | furniture | pages [26] -->
m

<!-- b003662 | furniture | pages [26] -->
m

<!-- b003663 | furniture | pages [26] -->
m

<!-- b003664 | furniture | pages [26] -->
m

<!-- b003665 | furniture | pages [26] -->
m

<!-- b003666 | furniture | pages [26] -->
m

<!-- b003667 | furniture | pages [26] -->
m

<!-- b003668 | furniture | pages [26] -->
m

<!-- b003669 | furniture | pages [26] -->
m

<!-- b003670 | furniture | pages [26] -->
m

<!-- b003671 | furniture | pages [26] -->
m

<!-- b003672 | furniture | pages [26] -->
m

<!-- b003673 | furniture | pages [26] -->
m

<!-- b003674 | furniture | pages [26] -->
m

<!-- b003675 | furniture | pages [26] -->
m

<!-- b003676 | furniture | pages [26] -->
m

<!-- b003677 | furniture | pages [26] -->
m

<!-- b003678 | furniture | pages [26] -->
m

<!-- b003679 | furniture | pages [26] -->
m

<!-- b003680 | furniture | pages [26] -->
m

<!-- b003681 | furniture | pages [26] -->
m

<!-- b003682 | furniture | pages [26] -->
m

<!-- b003683 | furniture | pages [26] -->
m

<!-- b003684 | furniture | pages [26] -->
m

<!-- b003685 | furniture | pages [26] -->
m

<!-- b003686 | furniture | pages [26] -->
m

<!-- b003687 | furniture | pages [26] -->
m

<!-- b003688 | furniture | pages [26] -->
m

<!-- b003689 | furniture | pages [26] -->
m

<!-- b003690 | furniture | pages [26] -->
m

<!-- b003691 | furniture | pages [26] -->
m

<!-- b003692 | furniture | pages [26] -->
m

<!-- b003693 | furniture | pages [26] -->
m

<!-- b003694 | furniture | pages [26] -->
m

<!-- b003695 | furniture | pages [26] -->
m

<!-- b003696 | furniture | pages [26] -->
m

<!-- b003697 | furniture | pages [26] -->
m

<!-- b003698 | furniture | pages [26] -->
m

<!-- b003699 | furniture | pages [26] -->
m

<!-- b003700 | furniture | pages [26] -->
m

<!-- b003701 | furniture | pages [26] -->
m

<!-- b003702 | furniture | pages [26] -->
m

<!-- b003703 | furniture | pages [26] -->
m

<!-- b003704 | furniture | pages [26] -->
m

<!-- b003705 | furniture | pages [26] -->
m

<!-- b003706 | furniture | pages [26] -->
m

<!-- b003707 | furniture | pages [26] -->
m

<!-- b003708 | furniture | pages [26] -->
m

<!-- b003709 | furniture | pages [26] -->
m

<!-- b003710 | furniture | pages [26] -->
m

<!-- b003711 | furniture | pages [26] -->
m

<!-- b003712 | furniture | pages [26] -->
m

<!-- b003713 | furniture | pages [26] -->
m

<!-- b003714 | furniture | pages [26] -->
m

<!-- b003715 | furniture | pages [26] -->
m

<!-- b003716 | furniture | pages [26] -->
m

<!-- b003717 | furniture | pages [26] -->
m

<!-- b003718 | furniture | pages [26] -->
m

<!-- b003719 | furniture | pages [26] -->
m

<!-- b003720 | furniture | pages [26] -->
m

<!-- b003721 | furniture | pages [26] -->
m

<!-- b003722 | furniture | pages [26] -->
m

<!-- b003723 | furniture | pages [26] -->
m

<!-- b003724 | furniture | pages [26] -->
m

<!-- b003725 | furniture | pages [26] -->
MATHmodels

<!-- b003726 | furniture | pages [26] -->
m

<!-- b003727 | furniture | pages [26] -->
m

<!-- b003728 | furniture | pages [26] -->
m

<!-- b003729 | furniture | pages [26] -->
m

<!-- b003730 | furniture | pages [26] -->
m

<!-- b003731 | furniture | pages [26] -->
m

<!-- b003732 | furniture | pages [26] -->
m

<!-- b003733 | furniture | pages [26] -->
m

<!-- b003734 | furniture | pages [26] -->
m

<!-- b003735 | furniture | pages [26] -->
m

<!-- b003736 | furniture | pages [26] -->
m

<!-- b003737 | furniture | pages [26] -->
m

<!-- b003738 | furniture | pages [26] -->
m

<!-- b003739 | furniture | pages [26] -->
m

<!-- b003740 | furniture | pages [26] -->
m

<!-- b003741 | furniture | pages [26] -->
获取更多资讯

<!-- b003742 | furniture | pages [26] -->
m

<!-- b003743 | furniture | pages [26] -->
m

<!-- b003744 | furniture | pages [26] -->
m

<!-- b003745 | furniture | pages [26] -->
m

<!-- b003746 | furniture | pages [26] -->
m

<!-- b003747 | furniture | pages [26] -->
m

<!-- b003748 | furniture | pages [26] -->
m

<!-- b003749 | furniture | pages [26] -->
m

<!-- b003750 | furniture | pages [26] -->
m

<!-- b003751 | furniture | pages [26] -->
m

<!-- b003752 | furniture | pages [26] -->
m

<!-- b003753 | furniture | pages [26] -->
m

<!-- b003754 | furniture | pages [26] -->
m

<!-- b003755 | furniture | pages [26] -->
m

<!-- b003756 | furniture | pages [26] -->
m

<!-- b003757 | furniture | pages [26] -->
m

<!-- b003758 | furniture | pages [26] -->
m

<!-- b003759 | furniture | pages [26] -->
m

<!-- b003760 | furniture | pages [26] -->
m

<!-- b003761 | furniture | pages [26] -->
m

<!-- b003762 | furniture | pages [26] -->
m

<!-- b003763 | furniture | pages [26] -->
m

<!-- b003764 | furniture | pages [26] -->
m

<!-- b003765 | furniture | pages [26] -->
m

<!-- b003766 | furniture | pages [26] -->
m

<!-- b003767 | furniture | pages [26] -->
m

<!-- b003768 | furniture | pages [26] -->
m

<!-- b003769 | furniture | pages [26] -->
m

<!-- b003770 | furniture | pages [26] -->
m

<!-- b003771 | furniture | pages [26] -->
m

<!-- b003772 | furniture | pages [26] -->
m

<!-- b003773 | furniture | pages [26] -->
m

<!-- b003774 | furniture | pages [26] -->
m

<!-- b003775 | furniture | pages [26] -->
m

<!-- b003776 | furniture | pages [26] -->
m

<!-- b003777 | furniture | pages [26] -->
m

<!-- b003778 | furniture | pages [26] -->
m

<!-- b003779 | furniture | pages [26] -->
m

<!-- b003780 | furniture | pages [26] -->
m

<!-- b003781 | furniture | pages [26] -->
m

<!-- b003782 | furniture | pages [26] -->
m

<!-- b003783 | furniture | pages [26] -->
m

<!-- b003784 | furniture | pages [26] -->
m

<!-- b003785 | furniture | pages [26] -->
m

<!-- b003786 | furniture | pages [26] -->
m

<!-- b003787 | furniture | pages [26] -->
m

<!-- b003788 | furniture | pages [26] -->
m

<!-- b003789 | furniture | pages [26] -->
m

<!-- b003790 | furniture | pages [26] -->
m

<!-- b003791 | furniture | pages [26] -->
m

<!-- b003792 | furniture | pages [26] -->
m

<!-- b003793 | furniture | pages [26] -->
m

<!-- b003794 | furniture | pages [26] -->
m

<!-- b003795 | furniture | pages [26] -->
m

<!-- b003796 | furniture | pages [26] -->
m

<!-- b003797 | furniture | pages [26] -->
m

<!-- b003798 | furniture | pages [26] -->
m

<!-- b003799 | furniture | pages [26] -->
m

<!-- b003800 | furniture | pages [26] -->
m

<!-- b003801 | furniture | pages [26] -->
m

<!-- b003802 | furniture | pages [26] -->
m

<!-- b003803 | furniture | pages [26] -->
m

<!-- b003804 | furniture | pages [26] -->
m

<!-- b003805 | furniture | pages [26] -->
m

<!-- b003806 | furniture | pages [26] -->
m

<!-- b003807 | furniture | pages [26] -->
m

<!-- b003808 | furniture | pages [26] -->
m

<!-- b003809 | furniture | pages [26] -->
m

<!-- b003810 | furniture | pages [26] -->
m

<!-- b003811 | furniture | pages [26] -->
m

<!-- b003812 | furniture | pages [26] -->
m

<!-- b003813 | furniture | pages [26] -->
m

<!-- b003814 | furniture | pages [26] -->
m

<!-- b003815 | furniture | pages [26] -->
m

<!-- b003816 | furniture | pages [26] -->
m

<!-- b003817 | furniture | pages [26] -->
m

<!-- b003818 | furniture | pages [26] -->
m

<!-- b003819 | furniture | pages [26] -->
m

<!-- b003820 | furniture | pages [26] -->
m

<!-- b003821 | furniture | pages [26] -->
m

<!-- b003822 | furniture | pages [26] -->
m

<!-- b003823 | furniture | pages [26] -->
m

<!-- b003824 | furniture | pages [26] -->
m

<!-- b003825 | furniture | pages [26] -->
m

<!-- b003826 | furniture | pages [26] -->
m

<!-- b003827 | furniture | pages [26] -->
m

<!-- b003828 | furniture | pages [26] -->
m

<!-- b003829 | furniture | pages [26] -->
m

<!-- b003830 | furniture | pages [26] -->
m

<!-- b003831 | furniture | pages [26] -->
m

<!-- b003832 | furniture | pages [26] -->
m

<!-- b003833 | furniture | pages [26] -->
m

<!-- b003834 | furniture | pages [26] -->
m

<!-- b003835 | furniture | pages [26] -->
m

<!-- b003836 | furniture | pages [26] -->
m

<!-- b003837 | furniture | pages [26] -->
m

<!-- b003838 | furniture | pages [26] -->
m

<!-- b003839 | furniture | pages [26] -->
m

<!-- b003840 | furniture | pages [26] -->
m

<!-- b003841 | furniture | pages [26] -->
m

<!-- b003842 | furniture | pages [26] -->
m

<!-- b003843 | furniture | pages [26] -->
m

<!-- b003844 | furniture | pages [26] -->
m

<!-- b003845 | furniture | pages [26] -->
m

<!-- b003846 | furniture | pages [26] -->
m

<!-- b003847 | furniture | pages [26] -->
m

<!-- b003848 | furniture | pages [26] -->
m

<!-- b003849 | furniture | pages [26] -->
m

<!-- b003850 | furniture | pages [26] -->
m

<!-- b003851 | furniture | pages [26] -->
m

<!-- b003852 | furniture | pages [26] -->
m

<!-- b003853 | furniture | pages [26] -->
m

<!-- b003854 | furniture | pages [26] -->
m

<!-- b003855 | furniture | pages [26] -->
m

<!-- b003856 | furniture | pages [26] -->
m

<!-- b003857 | furniture | pages [26] -->
m

<!-- b003858 | furniture | pages [26] -->
m

<!-- b003859 | furniture | pages [26] -->
m

<!-- b003860 | furniture | pages [26] -->
m

<!-- b003861 | furniture | pages [26] -->
m

<!-- b003862 | furniture | pages [26] -->
m

<!-- b003863 | furniture | pages [26] -->
m

<!-- b003864 | furniture | pages [26] -->
m

<!-- b003865 | furniture | pages [26] -->
m

<!-- b003866 | furniture | pages [26] -->
m

<!-- b003867 | furniture | pages [26] -->
m

<!-- b003868 | furniture | pages [26] -->
m

<!-- b003869 | furniture | pages [26] -->
m

<!-- b003870 | furniture | pages [26] -->
m

<!-- b003871 | furniture | pages [26] -->
m

<!-- b003872 | furniture | pages [26] -->
m

<!-- b003873 | furniture | pages [26] -->
m

<!-- b003874 | furniture | pages [26] -->
m

<!-- b003875 | furniture | pages [26] -->
m

<!-- b003876 | furniture | pages [26] -->
m

<!-- b003877 | furniture | pages [26] -->
m

<!-- b003878 | furniture | pages [26] -->
m

<!-- b003879 | furniture | pages [26] -->
m

<!-- b003880 | furniture | pages [26] -->
m

<!-- b003881 | furniture | pages [26] -->
m

<!-- b003882 | furniture | pages [26] -->
m

<!-- b003883 | furniture | pages [26] -->
m

<!-- b003884 | furniture | pages [26] -->
m

<!-- b003885 | furniture | pages [26] -->
m

<!-- b003886 | furniture | pages [26] -->
m

<!-- b003887 | furniture | pages [26] -->
m

<!-- b003888 | furniture | pages [26] -->
m

<!-- b003889 | furniture | pages [26] -->
m

<!-- b003890 | furniture | pages [26] -->
m

<!-- b003891 | furniture | pages [26] -->
m

<!-- b003892 | furniture | pages [26] -->
m

<!-- b003893 | furniture | pages [26] -->
m

<!-- b003894 | furniture | pages [26] -->
m

<!-- b003895 | furniture | pages [26] -->
m

<!-- b003896 | furniture | pages [26] -->
m

<!-- b003897 | furniture | pages [26] -->
m

<!-- b003898 | furniture | pages [26] -->
m

<!-- b003899 | furniture | pages [26] -->
m

<!-- b003900 | furniture | pages [26] -->
m

<!-- b003901 | furniture | pages [26] -->
m

<!-- b003902 | furniture | pages [26] -->
m

<!-- b003903 | furniture | pages [26] -->
m

<!-- b003904 | furniture | pages [26] -->
m

<!-- b003905 | furniture | pages [26] -->
m

<!-- b003906 | furniture | pages [26] -->
m

<!-- b003907 | furniture | pages [26] -->
m

<!-- b003908 | furniture | pages [26] -->
m

<!-- b003909 | furniture | pages [26] -->
m

<!-- b003910 | furniture | pages [26] -->
m

<!-- b003911 | furniture | pages [26] -->
m

<!-- b003912 | furniture | pages [26] -->
m

<!-- b003913 | furniture | pages [26] -->
m

<!-- b003914 | furniture | pages [26] -->
m

<!-- b003915 | furniture | pages [26] -->
m

<!-- b003916 | furniture | pages [26] -->
m

<!-- b003917 | furniture | pages [26] -->
m

<!-- b003918 | furniture | pages [26] -->
m

<!-- b003919 | furniture | pages [26] -->
m

<!-- b003920 | furniture | pages [26] -->
m

<!-- b003921 | furniture | pages [26] -->
m

<!-- b003922 | furniture | pages [26] -->
m

<!-- b003923 | furniture | pages [26] -->
m

<!-- b003924 | furniture | pages [26] -->
m

<!-- b003925 | furniture | pages [26] -->
m

<!-- b003926 | furniture | pages [26] -->
m

<!-- b003927 | furniture | pages [26] -->
m

<!-- b003928 | furniture | pages [26] -->
m

<!-- b003929 | furniture | pages [26] -->
m

<!-- b003930 | furniture | pages [26] -->
m

<!-- b003931 | furniture | pages [26] -->
m

<!-- b003932 | furniture | pages [26] -->
m

<!-- b003933 | furniture | pages [26] -->
m

<!-- b003934 | furniture | pages [26] -->
m

<!-- b003935 | furniture | pages [26] -->
m

<!-- b003936 | furniture | pages [26] -->
m

<!-- b003937 | furniture | pages [26] -->
m

<!-- b003938 | furniture | pages [26] -->
m

<!-- b003939 | furniture | pages [26] -->
m

<!-- b003940 | furniture | pages [26] -->
m

<!-- b003941 | furniture | pages [26] -->
m

<!-- b003942 | furniture | pages [26] -->
m

<!-- b003943 | furniture | pages [26] -->
m

<!-- b003944 | furniture | pages [26] -->
m

<!-- b003945 | furniture | pages [26] -->
m

<!-- b003946 | furniture | pages [26] -->
m
