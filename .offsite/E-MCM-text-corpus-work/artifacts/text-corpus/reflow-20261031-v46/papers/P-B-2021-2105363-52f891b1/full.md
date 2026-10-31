# P-B-2021-2105363-52f891b1

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
2021

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
B

<!-- b000007 | furniture | pages [1] -->
2105363

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Rapid Bushﬁre Response for Emergency Response

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
How to respond and deal with ﬁres in time when they occur is a question worth thinking about. This paper provides a ﬁre response plan for Victoria through the ratio- nal deployment of EOC, drones and forward teams.

<!-- b000013 | prose | pages [1] -->
In Task 1, the paper establishes the area safety evaluation model with ﬁre frequency, size, and recent ﬁre situation as indicators to classify the danger levels of different areas in Victoria. Then, we conﬁrm that drones should provide different services for high- risk and dangerous areas. In order to increase the service capacity, we optimize both capacity and cost. For capability, we make the average response time of SSA drones to high-risk areas as short as possible, and reserve as many SSA drones to dangerous areas as possible. For cost, we quantify the demand for SSA drones in terms of ﬁre acreage, and take into account the rounds and the attrition rate of drones. We also

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
consider the mix between SSA drones and radio repeater drones, and calculate the number of repeater drones using a greedy mix-based maximum number solving algo- rithm. The total cost is calculated and ﬁnally the quantity optimization model based on the maximum mix rate and minimum cost is obtained. 200 SSA drones and 32 radio repeater drones are needed, respectively.

<!-- b000016 | prose | pages [1] -->
In Task 2, we consider countermeasures in terms of both predicting extreme ﬁre events and increasing equipment. We ﬁrst build a ternary commensurable ﬁre predic- tion model to predict the probability and magnitude of extreme ﬁre events. Then, we use the expectation of the number of extreme ﬁres to estimate the amount of equip- ment that should be added to the EOC. Also, based on the size of the ﬁre and the number of ﬁreﬁghters’ equipment, we obtain a probability of success formula for ex- treme ﬁres, and the expected value of the additional equipment, given that the success rate of each extreme ﬁre rescue by the "boots on the ground" team is 80%. The unit cost of the equipment is reﬁned with relevant information to obtain the expected value of the increased equipment cost. So the total cost of additional equipment is A$4,952.25.

<!-- b000017 | prose | pages [1] -->
In Task 3, we consider signal range loss and drone safety to optimize the distribu- tion range of repeater drones. First, we establish a signal loss model with improved Standard Propagation Model (SPM) model to quantify the signal-to-noise ratio of the repeater drone’s signal around obstacles of different heights, and eliminate the loca- tions where the repeater signal-to-noise ratio is less than 20 dB. Then, we build a dynamics-based ﬁre spread model to calculate the edge length of ﬁre in each direc- tion. The locations where the distance between the repeater drone and the ﬁre edge is less than 50m are excluded. Finally, we simulate three locations at different altitudes, and ﬁnds that the wind direction directly affects the distribution of the optimized repeater drones, which is concentrated at the edge of the ideal range perpendicular to the wind direction.

<!-- b000018 | prose | pages [1] -->
We verify the robustness of the model by sensitivity analysis with respect to the parameters affecting the safety factors, and ﬁnd that the recent ﬁre conditions have a strong inﬂuence. We analyze the inﬂuence of different ﬁre frequencies and regions on the number of SSA drones, and the results with higher sensitivity are, ﬁre frequency in the [1600,2000] interval and located in the central region of Victoria, respectively. Finally, an annotated Budget Request is provided by collating all the expenses.

<!-- b000019 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000020 | prose | pages [1] -->
关注数学模型

<!-- b000021 | keywords | pages [1] -->
Keywords: safety factor

<!-- b000022 | prose | pages [1] -->
commensurable signal-to-noise ratio

<!-- b000023 | furniture | pages [1] -->
2

<!-- b000024 | furniture | pages [1] -->
MATHmodels

<!-- b000025 | furniture | pages [1] -->
获取更多资讯

<!-- b000026 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000027 | furniture | pages [2] -->
Team # 2105363

<!-- b000028 | furniture | pages [2] -->
Page 2 of 25

<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | contents | pages [2] -->
1 Introduction

<!-- b000031 | contents | pages [2] -->
3

<!-- b000032 | contents | pages [2] -->
1.1

<!-- b000033 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
3

<!-- b000035 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000036 | contents | pages [2] -->
1.2

<!-- b000037 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
3

<!-- b000039 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000040 | contents | pages [2] -->
3

<!-- b000041 | contents | pages [2] -->
2.1

<!-- b000042 | contents | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
3

<!-- b000044 | contents | pages [2] -->
2.2

<!-- b000045 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
4

<!-- b000047 | contents | pages [2] -->
2.3

<!-- b000048 | contents | pages [2] -->
Drones voyage model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
4

<!-- b000050 | contents | pages [2] -->
2.4

<!-- b000051 | contents | pages [2] -->
Data pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
5

<!-- b000053 | contents | pages [2] -->
3 Task 1: Optimal Numbers and Mix of Two Types of Drones

<!-- b000054 | contents | pages [2] -->
5

<!-- b000055 | contents | pages [2] -->
3.1

<!-- b000056 | contents | pages [2] -->
Area safety evaluation model . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
5

<!-- b000058 | contents | pages [2] -->
3.1.1

<!-- b000059 | contents | pages [2] -->
Indicators establishment . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
5

<!-- b000061 | contents | pages [2] -->
Safety factors S(x, y) and danger levels . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
3.1.2

<!-- b000063 | contents | pages [2] -->
7

<!-- b000064 | contents | pages [2] -->
3.1.3

<!-- b000065 | contents | pages [2] -->
Result analyze of heat map

<!-- b000066 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
8

<!-- b000068 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000069 | contents | pages [2] -->
3.2

<!-- b000070 | contents | pages [2] -->
Optimization of the number and mix of drones . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
8

<!-- b000072 | contents | pages [2] -->
3.2.1

<!-- b000073 | contents | pages [2] -->
Maximum drone capability . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
8

<!-- b000075 | contents | pages [2] -->
3.2.2

<!-- b000076 | contents | pages [2] -->
Minimal drone costs . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
9

<!-- b000078 | contents | pages [2] -->
3.2.3

<!-- b000079 | contents | pages [2] -->
Number and mix of drones . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
9

<!-- b000081 | contents | pages [2] -->
3.3

<!-- b000082 | contents | pages [2] -->
Optimization model with maximum mix rate and minimum cost

<!-- b000083 | contents | pages [2] -->
. . . .

<!-- b000084 | contents | pages [2] -->
13

<!-- b000085 | contents | pages [2] -->
3.3.1

<!-- b000086 | contents | pages [2] -->
Result Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
13

<!-- b000088 | contents | pages [2] -->
4 Task 2: Adaptation of Model and Cost Increases for Equipment

<!-- b000089 | contents | pages [2] -->
13

<!-- b000090 | contents | pages [2] -->
4.1

<!-- b000091 | contents | pages [2] -->
Ternary commensurable ﬁre prediction model

<!-- b000092 | contents | pages [2] -->
. . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
14

<!-- b000094 | contents | pages [2] -->
4.1.1

<!-- b000095 | contents | pages [2] -->
Model building process

<!-- b000096 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
14

<!-- b000098 | contents | pages [2] -->
4.1.2

<!-- b000099 | contents | pages [2] -->
Result of ternary commensurable ﬁre prediction model . . . . . .

<!-- b000100 | contents | pages [2] -->
16

<!-- b000101 | contents | pages [2] -->
4.2

<!-- b000102 | contents | pages [2] -->
Increased Equipment Costs

<!-- b000103 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
16

<!-- b000105 | contents | pages [2] -->
Additional equipment costs for EOCs Cost(EOC) . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
4.2.1

<!-- b000107 | contents | pages [2] -->
17

<!-- b000108 | contents | pages [2] -->
Additional equipment costs for ﬁreﬁghters Cost(ﬁreﬁghter) . . .

<!-- b000109 | contents | pages [2] -->
4.2.2

<!-- b000110 | contents | pages [2] -->
17

<!-- b000111 | contents | pages [2] -->
4.2.3

<!-- b000112 | contents | pages [2] -->
Results of additional equipment

<!-- b000113 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000114 | contents | pages [2] -->
18

<!-- b000115 | contents | pages [2] -->
5 Task 3: Location Optimization

<!-- b000116 | contents | pages [2] -->
18

<!-- b000117 | contents | pages [2] -->
5.1

<!-- b000118 | contents | pages [2] -->
Signal loss model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
18

<!-- b000120 | contents | pages [2] -->
5.2

<!-- b000121 | contents | pages [2] -->
Drone safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [2] -->
19

<!-- b000123 | contents | pages [2] -->
5.3

<!-- b000124 | contents | pages [2] -->
Result analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [2] -->
21

<!-- b000126 | contents | pages [2] -->
6 Sensitivity analysis

<!-- b000127 | contents | pages [2] -->
21

<!-- b000128 | contents | pages [2] -->
Sensitivity Analysis of safety factor S(x, y)

<!-- b000129 | contents | pages [2] -->
6.1

<!-- b000130 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000131 | contents | pages [2] -->
21

<!-- b000132 | contents | pages [2] -->
6.2

<!-- b000133 | contents | pages [2] -->
Sensitivity analysis of ﬁre frequency in different regions per year

<!-- b000134 | contents | pages [2] -->
. . . .

<!-- b000135 | contents | pages [2] -->
22

<!-- b000136 | contents | pages [2] -->
7 Strengths and Weaknesses

<!-- b000137 | contents | pages [2] -->
23

<!-- b000138 | contents | pages [2] -->
7.1

<!-- b000139 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000140 | contents | pages [2] -->
23

<!-- b000141 | contents | pages [2] -->
7.2

<!-- b000142 | contents | pages [2] -->
Weaknesses

<!-- b000143 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000144 | contents | pages [2] -->
23

<!-- b000145 | contents | pages [2] -->
8 Annotated Budget Request

<!-- b000146 | contents | pages [2] -->
23

<!-- b000147 | contents | pages [2] -->
References

<!-- b000148 | contents | pages [2] -->
25

<!-- b000149 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000150 | contents | pages [2] -->
关注数学模型

<!-- b000151 | furniture | pages [2] -->
2

<!-- b000152 | furniture | pages [2] -->
MATHmodels

<!-- b000153 | furniture | pages [2] -->
获取更多资讯

<!-- b000154 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000155 | furniture | pages [3] -->
Team # 2105363

<!-- b000156 | furniture | pages [3] -->
Page 3 of 25

<!-- b000157 | heading | pages [3] -->
1 Introduction

<!-- b000158 | heading | pages [3] -->
1.1 Problem Background

<!-- b000159 | prose | pages [3] -->
微信公众号：数学模型 Australia’s hot and dry climate, with many hills and few mountains, makes it one of the most forest ﬁre-prone places in the world. Since the ﬁrst ﬁre in New South Wales in September 2019, New South Wales and eastern Victoria was severly affected.

<!-- b000160 | prose | pages [3] -->
Fireﬁghters have used drones for surveillance and situational awareness (SSA) to allow the Emergency Operations Center (EOC) best direct active crews for optimal effect and maximal safety. The main task of drones is to monitor places where ﬁres are violent and where it is easy to grow into active ﬁres.

<!-- b000161 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000162 | prose | pages [3] -->
After understanding the relevant background information, the team are supposed 微信号：MATHmodels to do the following:

<!-- b000163 | prose | pages [3] -->
• Create a model to determine the optimal numbers and mix of SSA drones and Radio Repeater drones.

<!-- b000164 | prose | pages [3] -->
• Illustrate how your model adapts to the changing likelihood of extreme ﬁre events over the next decade. Project what equipment cost increases will occur assuming the cost of drone systems stays constant.

<!-- b000165 | prose | pages [3] -->
• Determine a model for optimizing the locations of hovering VHF/UHF radio- repeater drones.

<!-- b000166 | heading | pages [3] -->
2 Preparation of the Models

<!-- b000167 | heading | pages [3] -->
2.1 Assumptions and Justiﬁcations

<!-- b000168 | heading | pages [3] -->
1. The EOC can be deployed and moved to locations as needed for ﬁreﬁghting mis-

<!-- b000169 | prose | pages [3] -->
sions, with negligible cost of deployment and movement. And it is responsible for ﬁre rescue situations in only one area at a time.

<!-- b000170 | prose | pages [3] -->
EOC can be moved and deployed according to the ﬁre situation, and its cost is labor cost and equipment cost. The labor cost is more complicated and is a ﬁxed expendi- ture for the ﬁre department, so it is not considered.

<!-- b000171 | heading | pages [3] -->
2. When calculating the distance we consider that the distance is a straight line dis-

<!-- b000172 | prose | pages [3] -->
tance in a spatial three-dimensional coordinate system.

<!-- b000173 | prose | pages [3] -->
There is a big difference between the altitude of the Victorian mountains and the plains, so the distance obtained by considering the altitude is more accurate.

<!-- b000174 | heading | pages [3] -->
3. The repeaters can receive signals from multiple targets and forward them to mul-

<!-- b000175 | prose | pages [3] -->
tiple targets.

<!-- b000176 | prose | pages [3] -->
This is determined by the function of the repeater. A repeater located between the front lines and the EOC can relay radio signals both from the front lines to the EOC

<!-- b000177 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000178 | prose | pages [3] -->
关注数学模型 and from the EOC to the front lines.

<!-- b000179 | furniture | pages [3] -->
2

<!-- b000180 | furniture | pages [3] -->
MATHmodels

<!-- b000181 | furniture | pages [3] -->
获取更多资讯

<!-- b000182 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000183 | furniture | pages [4] -->
Team # 2105363

<!-- b000184 | furniture | pages [4] -->
Page 4 of 25

<!-- b000185 | heading | pages [4] -->
4. Drones only serve part of the ﬁre.

<!-- b000186 | prose | pages [4] -->
Fires in Australia are common, thus it is less likely to attract widespread attention when an average sized ﬁre occurs. And can be quickly extinguished by local ﬁre forces, without dedicated drone deployment. 微信公众号：数学模型

<!-- b000187 | heading | pages [4] -->
5. The drone needs to adjust its position when working.

<!-- b000188 | prose | pages [4] -->
To avoid damage to the drone caused by the effects of ﬁre.

<!-- b000189 | heading | pages [4] -->
2.2 Notations

<!-- b000190 | prose | pages [4] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000191 | caption | pages [4] -->
Table 1: Notations

<!-- b000192 | prose | pages [4] -->
Symbol Deﬁnition 微信号：MATHmodels r drone scanning radius (x, y) a place with longitude x and latitude y f(x, y) ﬁre frequency at (x, y) size(x, y) ﬁre size at (x, y) situation(x, y) recent ﬁre situation at (x, t) S(x, y) safety factor at (x, y) xi the distance between the EOC and the high-risk area Cost(drone) total cost of two types of drones m number of SSA drones n number radio repeater drones L2 signal-to-noise ratio

<!-- b000193 | heading | pages [4] -->
2.3 Drones voyage model

<!-- b000194 | prose | pages [4] -->
Considering the drone power problem, (km ) Voyage the ﬂight range of the drones are related to the average velocity (only consider single 30 trip), and the relationship between them is parabolic. For practical considerations, we formulate that the average speed of the drone 27.8 cannot exceed 10m/s (i.e., max{v} = 10m/s). When the drone is in the maximum ﬂight At this speed, the drone time (i.e. 2.5 hours), the drone range is max- has the largest range. imum, and the average velocity of the drone is 30km/2.5h ≈3.3m/s. The corresponding 0 3.3 10 ( / ) vavg m s relationship is shown in the ﬁgure below.

<!-- b000195 | caption | pages [4] -->
Figure 1: Relationship of V oyage and vmax

<!-- b000196 | caption | pages [4] -->
Figure 1 shows the length of drones’ voy-

<!-- b000197 | prose | pages [4] -->
age average velocity curve, which is a parabolic. What we obtain is as follows by ﬁtting data. V oyage(v) = −0.2 × v2 + 1.32 × v + 27.8 (km), (1)

<!-- b000198 | prose | pages [4] -->
where V oyage(v) is the length of vayage when drones travel with the average speed of

<!-- b000199 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000200 | prose | pages [4] -->
关注数学模型 v.

<!-- b000201 | furniture | pages [4] -->
2

<!-- b000202 | furniture | pages [4] -->
MATHmodels

<!-- b000203 | furniture | pages [4] -->
获取更多资讯

<!-- b000204 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000205 | furniture | pages [5] -->
Team # 2105363

<!-- b000206 | furniture | pages [5] -->
Page 5 of 25

<!-- b000207 | heading | pages [5] -->
2.4 Data pre-processing

<!-- b000208 | prose | pages [5] -->
In order to simplify the problem, the range of the repeater signal in the calculation of the ﬁrst question is always 20 km. Handheld two-way radios have a range of 2 km 微信公众号：数学模型 in urban, forest and mountainous areas and 5 km elsewhere. This greatly simpliﬁes the calculation and will be further optimized in the third question.

<!-- b000209 | heading | pages [5] -->
Fires data processing

<!-- b000210 | prose | pages [5] -->
Combined with life experience we know that the spread of ﬁre presents a convex polygon, which is approximately estimated as a circle. The circumference of the jth ﬁre with latitude and longitude of (xj, yj) is dj(xj, yj), which yields:

<!-- b000211 | prose | pages [5] -->
• Radius: rj(xj, yj) = dj(xj,yj) ; 2π

<!-- b000212 | prose | pages [5] -->
• Area: Scircle,j(xj, yj) = π × r2 j(xj, yj).

<!-- b000213 | prose | pages [5] -->
We combine ﬁres that occurred on the same day and in close proximity into one ﬁre point.

<!-- b000214 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000215 | heading | pages [5] -->
3 Task 1: Optimal Numbers and Mix of Two Types of

<!-- b000216 | prose | pages [5] -->
Drones

<!-- b000217 | prose | pages [5] -->
In the model for determining the number and combination of drones, it is necessary to provide an evaluation standard for whether the ﬁre point needs drone rescue to improve rescue efﬁciency. To do this, we ﬁrst classify the ﬁres into different safety levels. On the basis of the known safety level of each area, we optimize the number and combination of drones based on maximum mix rate and minimum cost.

<!-- b000218 | heading | pages [5] -->
3.1 Area safety evaluation model

<!-- b000219 | prose | pages [5] -->
In order to assess the safety factor for dif- ferent areas of Victoria, the gridded map is shown in Figure 2. The longitude and lati- tude of each region are denoted by x, y, re- spectively. For different latitude and longi- tude (x, y) regions, we establish three eval- uation indicators: ﬁre frequency f(x, y), re- cent ﬁre situation situation(x, y), andﬁre size size(x,y) , which are used to measure the safety factor S(x, y). The safety coefﬁcients of the grid and the adjacent grid are scored to get the safety levels of the different grids on

<!-- b000220 | caption | pages [5] -->
Figure 2: Map gridding schematic

<!-- b000221 | prose | pages [5] -->
the map.

<!-- b000222 | heading | pages [5] -->
3.1.1 Indicators establishment

<!-- b000223 | prose | pages [5] -->
(1) Fire frequency f(x, y)

<!-- b000224 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000225 | prose | pages [5, 6] -->
In order to fully understand the ﬁre frequency when ﬁres are most severe in differ-关注数学模型 ent areas, we need the maximum value of the daily ﬁre frequency at that location and explore it on different time scales to estimate that maximum value.

<!-- b000226 | furniture | pages [5] -->
2

<!-- b000227 | furniture | pages [5] -->
MATHmodels

<!-- b000228 | furniture | pages [5] -->
获取更多资讯

<!-- b000229 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000230 | furniture | pages [6] -->
Team # 2105363

<!-- b000231 | furniture | pages [6] -->
Page 6 of 25

<!-- b000233 | prose | pages [6] -->
f(x, y) = max{u(ts, i, x, y) 微信公众号：数学模型 }, (2) ts where:

<!-- b000234 | prose | pages [6] -->
• ts is the time scale in days, ts ∈[1, 365];

<!-- b000235 | prose | pages [6] -->
• i denotes the number of times, i ∈[1, ⌊365 ts ⌋];

<!-- b000236 | prose | pages [6] -->
• u(ts, i, x, y) = [number of ﬁres that occurred from day (1+(i−1)×ts) to day (1+ i × ts)]/ts (in place (x,y)), indicating the number of ﬁres that occurred in the ith time scale.

<!-- b000237 | caption | pages [6] -->
Figure 3 shows a detailed illustration about the time scale.

<!-- b000238 | prose | pages [6] -->
𝑢(𝑡௦, 𝑖) is the number of fires that occurred during this period 微信号：MATHmodels 𝑡௦ 𝑖= 1 𝑖= 2 𝑖 A year (365days) 1 1 + 𝑡௦ 1 + 2𝑡௦ 1 + (𝑖−1)𝑡௦ 1 + 𝑖ȉ 𝑡௦

<!-- b000239 | caption | pages [6] -->
Figure 3: Time scale diagram

<!-- b000240 | prose | pages [6] -->
(2) Recent ﬁre situation situation(x, y)

<!-- b000241 | prose | pages [6] -->
[2] we know that the "mini-weather zone" formed by smoke and From the website heat absorbing atmospheric moisture can continue to spread the ﬁre through the sparks and form new ignition sites, which is also known as "embers attack". In other words, the area where the ﬁre just broke out is more likely to reignite. during the period t0 (the time period corresponding to Figure 1 in the title, i.e., October 1, 2019 to January 7, 2020). We use t0 as the time criterion for determining the presence of recent ﬁres and the period for updating the safety level, making the following divisions.

<!-- b000242 | caption | pages [6] -->
Table 2: A three-way score table

<!-- b000243 | prose | pages [6] -->
Recent ﬁre situation Scores

<!-- b000244 | prose | pages [6] -->
Burning 3 Happened recently 2 Not happened recently 1

<!-- b000245 | prose | pages [6] -->
(3) Fire size size(x, y)

<!-- b000246 | prose | pages [6] -->
[1], we extract the circumference Based on the data obtained from Active Fire Data dj(x, y) for the jth ﬁre in the (x, y) region and obtain annual average size:

<!-- b000247 | prose | pages [6] -->
365 dj(x, y) X size(x, y) = . (3) 365 j=1

<!-- b000248 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000249 | prose | pages [6] -->
关注数学模型

<!-- b000250 | furniture | pages [6] -->
2

<!-- b000251 | furniture | pages [6] -->
MATHmodels

<!-- b000252 | furniture | pages [6] -->
获取更多资讯

<!-- b000253 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000254 | furniture | pages [7] -->
Team # 2105363

<!-- b000255 | furniture | pages [7] -->
Page 7 of 25

<!-- b000256 | heading | pages [7] -->
3.1.2 Safety factors S(x, y) and danger levels

<!-- b000257 | prose | pages [7] -->
1. Safety factors based on AHP AHP is a systematic and hierarchical multi-objective comprehensive evaluation method. We build the importance matrix of S(x, y): 微信公众号：数学模型   1 2 1/6 2 1 1/5 .  6 5 1

<!-- b000258 | prose | pages [7] -->
We take the average size of the ﬁre as the most important indicator, and the purpose is to make the area with a high safety factor correspond to a larger average size. The resulting ﬁre is more active or can develop into a more larger size, which is in line with the characteristics of the objects monitored by drones.

<!-- b000259 | prose | pages [7] -->
The consistency ratio is CR = 0.0739, which is less than 0.1, so the degree of inconsistency of S(x, y) is within the tolerance range. And it passes the consistency test. 微信号：MATHmodels In order to eliminate the differences in the different magnitudes, after normaliza- tion, we get:

<!-- b000260 | prose | pages [7] -->
S(x, y) = a1 × f(x, y) + a2 × situation(x, y) + a3 × size(x, y). (4)

<!-- b000261 | prose | pages [7] -->
The result of Formula 4 is a1 = 0.1628, a2 = 0.1088, a3 = 0.7285.

<!-- b000262 | heading | pages [7] -->
2. Safety Assessment of the area:

<!-- b000263 | prose | pages [7] -->
When we consider whether a region is safe or not, in addition to the safety fac- tor S(x, y) for that region, for its neighboring regions is also of reference value. We convolve the nine safety factors with a convolution kernel

<!-- b000264 | prose | pages [7] -->
    S(x −1, y + 1) S(x, y + 1) S(x + 1, y + 1) 0.05 0.05 0.05 S′(x, y) = S(x −1, y) ⊗ S(x, y) S(x + 1, y) 0.05 0.6 0.05 .   S(x −1, y −1) S(x, y −1) S(x + 1, y −1) 0.05 0.05 0.05

<!-- b000265 | prose | pages [7] -->
While the safety factor is already a valuable indicator when considering the safety situation, it is clear that we cannot ignore the inﬂuence of topography for the Rapid Bushﬁre Response program. There are signiﬁcant differences in landscape from region to region. Therefore, ﬁres in forested and vegetated hills and mountains (collectively referred to as ﬂammable topography) are more likely to develop over time into ﬁres that are ﬁerce and difﬁcult to extinguish. And urban, desert, plains and other areas (collectively referred to as non-combustible topography) after the ﬁre is difﬁcult to further develop into a larger scale. Do the following division.

<!-- b000266 | caption | pages [7] -->
Table 3: Dangerous level classiﬁcation

<!-- b000267 | prose | pages [7] -->
Non-flammable topography Flammable topography

<!-- b000268 | prose | pages [7] -->
Safety factor Danger level Safety factor Danger level 0 0.25 very safe 0 0.25 safe 0.25 0.5 safe 0.25 0.5 general 0.5 0.75 general 0.5 0.75 dangerous

<!-- b000269 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000270 | prose | pages [7] -->
0.75 1 dangerous 0.75 1 high-risk 关注数学模型

<!-- b000271 | furniture | pages [7] -->
2

<!-- b000272 | furniture | pages [7] -->
MATHmodels

<!-- b000273 | furniture | pages [7] -->
获取更多资讯

<!-- b000274 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000275 | furniture | pages [8] -->
Team # 2105363

<!-- b000276 | furniture | pages [8] -->
Page 8 of 25

<!-- b000277 | heading | pages [8] -->
3.1.3 Result analyze of heat map

<!-- b000278 | prose | pages [8] -->
The map of different security levels is shown in Figure 4. The areas in different colors represent areas of different levels. 微信公众号：数学模型 High-risk Dangerous General Safe & very safe

<!-- b000279 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000280 | caption | pages [8] -->
Figure 4: Different danger levels on the Victoria map

<!-- b000281 | prose | pages [8] -->
As can be seen in Figure 4, central Victoria is safer, probably because it is at a low altitude and is not affected much by climate. There are many high-risk areas in the east, west and south, which is because these areas are very vegetated.

<!-- b000282 | prose | pages [8] -->
For SSA drones, it should maintain timely response capability to the high-risk area and have certain prevention capability to the dangerous area. Repeater drones, on the other hand, work with SSA drones to maintain communications and surveillance ac- tivities in high-risk areas, while reserving a certain number of radio-repeater drones for dangerous areas to support communications that may be established. In order to ensure the safety of the EOC, set the EOC to move freely in the safe area.

<!-- b000283 | heading | pages [8] -->
3.2 Optimization of the number and mix of drones

<!-- b000284 | prose | pages [8] -->
After dividing the gridded map into areas with different security levels, we dis- patch drones to implement emergency response or preventive deployment based on the security level of the ﬁre, demonstrating the advantages and disadvantages of the solution using capability and cost metrics. We evaluate the mix of the two types of drones and optimize the number of drones based on as much capability and as little cost as possible.

<!-- b000285 | heading | pages [8] -->
3.2.1 Maximum drone capability

<!-- b000286 | prose | pages [8] -->
The capability of the drone is reﬂected in two aspects: the response time of the high-risk area is as short as possible (response capability) and the response time of the dangerous area is as reasonable as possible (prevention capability). There are M high-risk areas and N precautionary areas in the statistics. These two capabilities are analyzed separately below.

<!-- b000287 | prose | pages [8] -->
• Response capability

<!-- b000288 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000289 | prose | pages [8, 9] -->
关注数学模型 We consider the ith EOC to be responsible for communication and surveillance. the role of the EOC is to direct the SSA drone to reach the high risk area from a location closer to the ith high risk area in a safer area, such that the average response time tavg is minimized. 微信公众号：数学模型 M ti X tavg = M , i=1 xi ti = . vmax

<!-- b000290 | furniture | pages [8] -->
2

<!-- b000291 | furniture | pages [8] -->
MATHmodels

<!-- b000292 | furniture | pages [8] -->
获取更多资讯

<!-- b000293 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000294 | furniture | pages [9] -->
Team # 2105363

<!-- b000295 | furniture | pages [9] -->
Page 9 of 25

<!-- b000297 | prose | pages [9] -->
To ensure that the drone can travel back to,

<!-- b000298 | prose | pages [9] -->
xi < 0.5 × V oyage(vmax). (5)

<!-- b000299 | prose | pages [9] -->
xi is the distance between the EOC and the high-risk area, and ti is the time the aircraft ﬂies in the process. In order to maximize the response capability of the drone, tavg should be as small as possible. Therefore, we make the EOC located at the nearest 微信号：MATHmodels point to the ith high-risk area in the safer region.

<!-- b000300 | prose | pages [9] -->
• Prevention capability

<!-- b000301 | prose | pages [9] -->
We conﬁgure a certain number of SSA drones in the dangerous area, so that when the EOC is movable, we can ensure that there are SSA drones or EOCs in the dangerous area at regular intervals to check whether there are ﬁres. Prepare a certain number of drones, the more the number, the better the ability to prevent, see Section 3.2.3 for quantiﬁcation.

<!-- b000302 | heading | pages [9] -->
3.2.2 Minimal drone costs

<!-- b000303 | prose | pages [9] -->
We calculate the total cost of the two drones and their number separately. Let the number of SSA drones be m and the number of Radio Repeater drones be n. The calculation is as follows.

<!-- b000304 | prose | pages [9] -->
Cost(drone) = m × Cost(SSA drone) + n × Cost(radio repeater drone), (6)

<!-- b000305 | prose | pages [9] -->
where Cost(SSA drone) = SSA drones’ HD camera cost+ remote sensing camera cost+ drone cost, Cost(radio repeater drone) = repeater cost+ Radio Repeater drones’ cost. So we want min{Cost(SSA drone).} (7)

<!-- b000306 | heading | pages [9] -->
3.2.3 Number and mix of drones

<!-- b000307 | prose | pages [9] -->
The m, n are the number of SSA drones and radio-repeater drones, respectively. We determine the number of SSA drones from the demand of the ﬁre scene and the round system, then determine the number of radio repeater drones by the combination relationship between SSA drones and radio repeater drones, and ﬁnally prepare some drones to prevent dangerous area.

<!-- b000308 | heading | pages [9] -->
1. Number of SSA drones

<!-- b000309 | prose | pages [9, 10] -->
For SSA drones, because SSA drones monitor the ﬁre scene directly, the mixed re- lationship with the radio-repeater drones does not change their utilization rate in the关注数学模型 ﬁre now, so it is sufﬁcient to calculate the number of SSA drones directly according to the ﬁre demand.

<!-- b000310 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000311 | furniture | pages [9] -->
2

<!-- b000312 | furniture | pages [9] -->
MATHmodels

<!-- b000313 | furniture | pages [9] -->
获取更多资讯

<!-- b000314 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000315 | furniture | pages [10] -->
Team # 2105363

<!-- b000316 | furniture | pages [10] -->
Page 10 of 25

<!-- b000318 | prose | pages [10] -->
(1) For high-risk areas 微信公众号：数学模型 Let the longitude and latitude of the jth high-risk area be (x′ j, y′ j), and ﬁnd the num- ber of SSA drones needed to scan the jth high-risk area.

<!-- b000319 | prose | pages [10] -->
Fires that need to maintain a timely response are very active, large and mostly in terrain that is prone to further expansion.

<!-- b000320 | prose | pages [10] -->
Side view

<!-- b000321 | prose | pages [10] -->
Top view

<!-- b000322 | prose | pages [10] -->
𝑣୫ୟ୶× 𝑡

<!-- b000323 | prose | pages [10] -->
𝜃= 40° 𝜃 𝑟 𝑟

<!-- b000324 | prose | pages [10] -->
微信号：MATHmodels 𝑟 𝑟 ℎ= 300𝑚

<!-- b000325 | prose | pages [10] -->
Scanning acreage 𝑟 𝑟

<!-- b000326 | caption | pages [10] -->
Figure 5: SSA drones surveillance schematic

<!-- b000327 | prose | pages [10] -->
To ensure ﬁreﬁghting efﬁciency, SSA drones on scene should assure that they can complete scanning surveillance of the entire scene area within half a minute. The scan radius can be obtained from Figure 5.

<!-- b000328 | prose | pages [10] -->
S′ circle,j m1,j = πr2 + 2r · vmax × 30 seconds. (8)

<!-- b000329 | prose | pages [10] -->
SSA drones have constant round trips and recharges, and there are handoffs. So the number of SSA required for the jth high-risk area is the product of the number of handoffs and the number of SSA drones required at the same time.

<!-- b000330 | prose | pages [10] -->
2¯xi v + recharge time m2,j = m1,j · , (9) −xj V oyage(v) v v

<!-- b000331 | prose | pages [10] -->
where the biggest fractional equation in Formula (9) represents the rounds of the drone, which is obtained by the quotient of the time returning from the disaster area to recharge and arriving at the disaster area again and the time spent in the disaster area.

<!-- b000332 | prose | pages [10] -->
(2) For dangerous areas For the ith dangerous area, the number of SSA drones should reach a certain thresh- old in order to check for ﬁres in these areas, such that even in the worst case scenario (i.e., when all dangerous areas are on ﬁre), the number of SSA drones in reserve is suf- ﬁcient to dispatch one SSA drone for each hazard area for temporary surveillance and situational awareness. Thus there is a total number of SSAs:

<!-- b000333 | prose | pages [10] -->
M X m2,j + N × (1 + ϕ), m = (10)

<!-- b000334 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000335 | prose | pages [10, 11] -->
关注数学模型 i=1 where ϕ is loss rate. Considering the attrition of reserve drones, we prepare some additional drones to cope with this attrition. ϕ is the number of extra prepared drones divided by the number of dangerous area drones.

<!-- b000336 | furniture | pages [10] -->
2

<!-- b000337 | furniture | pages [10] -->
MATHmodels

<!-- b000338 | furniture | pages [10] -->
获取更多资讯

<!-- b000339 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000340 | furniture | pages [11] -->
Team # 2105363

<!-- b000341 | furniture | pages [11] -->
Page 11 of 25

<!-- b000343 | heading | pages [11] -->
2. Mix of Radio Repeater drones

<!-- b000344 | prose | pages [11] -->
微信公众号：数学模型 For the radio-repeater drones, consider its combination with the SSA drones, so that each radio-repeater drone can receive as many signals as possible and forward more signals to determine the best number , optimize utilization.

<!-- b000345 | heading | pages [11] -->
(1) Greedy and multiplexing based solution algorithms

<!-- b000346 | prose | pages [11] -->
Using a greedy algorithm, the solution that allows each radio repeater drone to reuse the maximum number of SSA drones is planned, and the minimum number of radio repeater drones, n, is output.

<!-- b000347 | prose | pages [11] -->
The idea of the algorithm is to ﬁnd candidate locations of radio repeater drones that can be multiplexed. Starting from the candidate location with the most multiplex- ing, a radio repeater drone is determined to be placed at that location, while removing the SSA drones in high-risk areas that can use that repeater drone to send and receive 微信号：MATHmodels signals. Then candidate locations with the second highest reuse rate is identiﬁed. Con- tinue this process until all high-risk areas are taken care of by the repeater.

<!-- b000348 | prose | pages [11] -->
Given the meaning of some symbols:

<!-- b000349 | prose | pages [11] -->
• n1, n2 are the number of prepared radio-repeater drones and the number of radio- repeater drones responding to the high-risk area, respectively. When calculating n1, the input n is n1, so does n2.

<!-- b000350 | prose | pages [11] -->
• mi is the number of SSA drones in ith.

<!-- b000351 | prose | pages [11] -->
• U is the number of corresponding areas when considering high-risk or dangerous areas.

<!-- b000352 | prose | pages [11] -->
• Rradio = 2km and Rrepeater = 20km are the ranges of the handheld two-way radios and repeaters, respectively.

<!-- b000353 | prose | pages [11] -->
• SCi is the candidate range of radio repeater drone for the ith high-risk area, SC = {SC1, SC2, · · · , SCM}.

<!-- b000354 | prose | pages [11] -->
• SRi is the number of radio repeater drones multiplexed corresponding to the ith high-risk area (other high-risk areas use this repeater at the same time), equal to 1 means that this radio repeater drone is only responsible for the signal transceiver in this high-risk area. SR = {SR1, SR2, · · · , SRM}.

<!-- b000355 | prose | pages [11] -->
• SNj is the reuse number of the radio repeater drones corresponding to the jth high-risk region. If another high-risk area multiplexes this repeater, the serial number of this high-risk area is an element of the set SN. SN = {SN1, SN2, · · · , SNM}

<!-- b000356 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000357 | prose | pages [11] -->
关注数学模型

<!-- b000358 | furniture | pages [11] -->
2

<!-- b000359 | furniture | pages [11] -->
MATHmodels

<!-- b000360 | furniture | pages [11] -->
获取更多资讯

<!-- b000361 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000362 | furniture | pages [12] -->
Team # 2105363

<!-- b000363 | furniture | pages [12] -->
Page 12 of 25

<!-- b000364 | heading | pages [12] -->
Algorithm: Radio Repeater drones number solving algorithm

<!-- b000365 | prose | pages [12] -->
Input: xi, Rradio, Rrepeater, n = 0 Output: n 1 for i = 1; i ⩽U; i + + do 微信公众号：数学模型 if xi > Rradio then 2 take the ith high-risk area as the center and Rradio as the radius to 3 make a circle O1;

<!-- b000366 | prose | pages [12] -->
take the ith EOC as the center and Rrepeater as the radius to make 4 a circle O2;

<!-- b000367 | prose | pages [12] -->
SCi = O1 ∩O2; 5 SRi = 1; 6

<!-- b000368 | prose | pages [12] -->
7 for i = 1; i ⩽U; i + + do for j = 1; j ⩽U; j + + do 8 if SCi ∩SCj̸ = ∅and i̸ = j then 9 SRi = SRi + mj; 10 SCi = SCi ∩SCj; 微信号：MATHmodels 11 SNi = SNi ∪{j}; 12

<!-- b000369 | prose | pages [12] -->
13 while SR1 + SR2 + · · · + SRU = 0 do SRk = max{SR}, k is the maximum value’s serial number in SR; 14 n = n + 1; 15 for i = 1; i ⩽U; i + + do 16 if k ∈SNi then 17 SNi = ∅; 18 SRi = 0; 19

<!-- b000370 | prose | pages [12] -->
(2) Maximize the reuse rate m n Using the reuse rate: m n indicates the mix relationship of drone conﬁguration, the larger this indicator is the better the mix relationship of two drones. Then we have: max{m n }. (11)

<!-- b000371 | prose | pages [12] -->
(3) Continuous supply to high-risk areas

<!-- b000372 | prose | pages [12] -->
Considering the process of repeater drone round trip and charging, there is hand- offs, so it is necessary to get the number of repeater drones that respond to high risk areas: 2¯xi v + recharge time n′ 1 = n1 × , V oyage(v) −¯xi v v

<!-- b000373 | prose | pages [12] -->
ditto, 3.3 ⩽v ⩽10,

<!-- b000374 | prose | pages [12] -->
V oyage(v) > 2 × max(xj).

<!-- b000375 | prose | pages [12] -->
So the total number of repeater drones:

<!-- b000376 | prose | pages [12] -->
n = n′ 1 + n2, (12)

<!-- b000377 | prose | pages [12] -->
where n2 is radio repeater drones that dangerous areas need.

<!-- b000378 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000379 | prose | pages [12] -->
关注数学模型

<!-- b000380 | furniture | pages [12] -->
2

<!-- b000381 | furniture | pages [12] -->
MATHmodels

<!-- b000382 | furniture | pages [12] -->
获取更多资讯

<!-- b000383 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000384 | furniture | pages [13] -->
Team # 2105363

<!-- b000385 | furniture | pages [13] -->
Page 13 of 25

<!-- b000386 | heading | pages [13] -->
3.3 Optimization model with maximum mix rate and minimum cost

<!-- b000387 | prose | pages [13] -->
Combining all the above, λ is introduced to reﬂect the priority of the drone capabil- ity indicators. The larger λ is, the higher the priority of the capability indicators in the 微信公众号：数学模型 drone conﬁguration scheme obtained from the planning. The ﬁnal model is:

<!-- b000388 | prose | pages [13] -->
min{( n m)λ × Cost(drone)(1−λ)},

<!-- b000389 | prose | pages [13] -->
n = n′  1 + n2   0 ⩽ϕ ⩽1   s.t. . 0 ⩽λ ⩽13.3 ⩽v ⩽10    V oyage(v) > 2 × max{xj} 

<!-- b000390 | heading | pages [13] -->
3.3.1 Result Analysis

<!-- b000391 | prose | pages [13] -->
微信号：MATHmodels The result of the optimization model with maximum drone capability and mini- mum cost are shown in Figure 6.

<!-- b000392 | prose | pages [13] -->
Pareto front

<!-- b000393 | prose | pages [13] -->
Choose the relatively optimal solution for the two objective functions in this area.

<!-- b000394 | prose | pages [13] -->
Cost(drone)

<!-- b000395 | prose | pages [13] -->
n m

<!-- b000396 | caption | pages [13] -->
Figure 6: The results of the optimization model

<!-- b000397 | prose | pages [13] -->
As shown in the Figure 6, the inverse of m n shows an inverse relationship with the cost of the drone, which indicates that our bi-objective optimization is effective. We intercept the middle section of the interval as the solution space, and we can choose a non-inferior solution in the left half of the interval when we prefer the combination rate to be optimal, and in the right half of the interval when we prefer the cost to be minimal.

<!-- b000398 | heading | pages [13] -->
4 Task 2: Adaptation of Model and Cost Increases for

<!-- b000399 | prose | pages [13] -->
Equipment

<!-- b000400 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000401 | prose | pages [13] -->
关注数学模型 For simplicity, we make the following two assumptions:

<!-- b000402 | furniture | pages [13] -->
2

<!-- b000403 | furniture | pages [13] -->
MATHmodels

<!-- b000404 | furniture | pages [13] -->
获取更多资讯

<!-- b000405 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000406 | furniture | pages [14] -->
Team # 2105363

<!-- b000407 | furniture | pages [14] -->
Page 14 of 25

<!-- b000408 | prose | pages [14] -->
• The topography of Australia will not change dramatically in the next ten years (not considering changes in topography caused by unavoidable factors such as earthquakes).

<!-- b000409 | prose | pages [14] -->
• The probability of ﬁre occurrence in different hazard areas is independent of each 微信公众号：数学模型 other.

<!-- b000410 | heading | pages [14] -->
4.1 Ternary commensurable ﬁre prediction model

<!-- b000411 | heading | pages [14] -->
4.1.1 Model building process

<!-- b000412 | prose | pages [14] -->
Since the terrain does not change dramatically over the course of a decade, the main task of predicting ﬁre is when extreme ﬁre conditions will occur, what the probability of occurrence is, and what the amount of equipment prepared to respond to ﬁres of different sizes is. We obtained data on extreme ﬁre conditions in Victoria over the last [5], and used this as the few decades by referring to List of major bushﬁres in Australia basis for our predictions. 微信号：MATHmodels The commensurable prediction model is a method of forecasting special events based on special events, and he bases his forecasting on the universal existence of com- mensurability of events, which is a generalized periodicity. Commensurability is a law that is common to all elements of a system and reﬂects the occurrence of special events [6]. (small probability events) in nature

<!-- b000413 | prose | pages [14] -->
1. The general commensurable prediction model is:

<!-- b000414 | prose | pages [14] -->
l X Xi+1 = IjXj, j=1

<!-- b000415 | prose | pages [14] -->
where X is entered in chronological order for the past years in which extreme ﬁre events occurred to obtain X = {X1, X2, ..., X17} in the sequence.. {j} ∈{i}, that is, j is an element of the set i. Ij is an integer.

<!-- b000416 | heading | pages [14] -->
2. In order to get the optimal results, the ternary commensurable prediction model

<!-- b000417 | prose | pages [14] -->
[7]. And the formula is: with the best results in general is selected

<!-- b000418 | prose | pages [14] -->
Xa + Xb −Xc = Xu(a,b,c),

<!-- b000419 | prose | pages [14] -->
where a, b, c, d, e, f, g = 1, 2, · · · , n, u, v, w = 1, 2, · · · , m.

<!-- b000420 | heading | pages [14] -->
3. Enumerate the equations that match the above relationship by enumeration, and

<!-- b000421 | prose | pages [14] -->
process the sequence numbers to obtain a vector

<!-- b000422 | prose | pages [14] -->
V = (b −a, c −b, u −c,′ +′,′ −′),

<!-- b000423 | prose | pages [14] -->
which means the difference between the serial numbers of the ﬁrst two years, the differ- ence between the serial numbers of the second and third years, the difference between the serial numbers of the third and fourth years, the sign before the second year, and the sign before the third year.

<!-- b000424 | prose | pages [14] -->
Find among all vectors the vectors that exist identical to itself and obtain the multi- set ternary commensurable forecast formula:

<!-- b000425 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000426 | prose | pages [14, 15] -->
关注数学模型 i = 1, 2, · · · , XiV4Xi+V 1V5Xi+V1+V2 = Xi+V1+V2+V3 let the term with the largest ordinal number in the forecast equation be X18, and the forecast value for multiple years corresponding to X18 can be calculated.

<!-- b000427 | furniture | pages [14] -->
2

<!-- b000428 | furniture | pages [14] -->
MATHmodels

<!-- b000429 | furniture | pages [14] -->
获取更多资讯

<!-- b000430 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000431 | furniture | pages [15] -->
Team # 2105363

<!-- b000432 | furniture | pages [15] -->
Page 15 of 25

<!-- b000434 | prose | pages [15] -->
4. We sort the past year series and the forecasted year series from left to right by serial number, enumerate four years from all of them, ﬁnd the ternary commensurable 微信公众号：数学模型 forecast formula they match, and connect them two by two with their differences to get the butterﬂy diagram.

<!-- b000435 | prose | pages [15] -->
Δ = 17 Δ = 17(18) Δ = 17 Δ = 17 Δ = 17 Δ = 17(18) Δ =17(18)

<!-- b000436 | prose | pages [15] -->
1851 1898 1926 1939 1944 1951 1965 1977 1983 1985 1997 2003 2006 2007 2009 2014 2020 2023

<!-- b000437 | prose | pages [15] -->
𝚫= 9(8) 𝚫= 9 𝚫= 9 𝚫= 9(8) Years not used in the forecast 微信号：MATHmodels Δ = 3 Δ = 3(4) Δ = 3 Δ = 3(2) Δ = 3 Two Years with difference of 17 Two Years with difference of 9 Two Years with difference of 3

<!-- b000438 | caption | pages [15] -->
Figure 7: Butterﬂy structure diagram

<!-- b000439 | prose | pages [15] -->
According to the K. Pearson-Fisher theorem, Figure 7 satisﬁes the butterﬂy struc- ture probability reference criterion. It reﬂects the most important quasi-cycles since 1851 as 3, 9, 17a, with 17a being the most typical, occurring seven times.

<!-- b000440 | heading | pages [15] -->
5. Count statistically the total number of extreme ﬁres used to predict the ith extreme

<!-- b000441 | prose | pages [15] -->
ﬁre situation as ni, and the number of extreme ﬁres participating in the prediction of the ith extreme ﬁre case is mi, then the probability of the ith extreme ﬁre event is

<!-- b000442 | prose | pages [15] -->
P(ith extreme ﬁre occur) = mi , ni

<!-- b000443 | prose | pages [15] -->
and mi can be seen by butterﬂy structure diagram clearly.

<!-- b000444 | prose | pages [15] -->
For example, our predicted year for the next extreme ﬁre is 2023, which is involved in all three cycles, and the number of years involved in the prediction is 16. The prob- ability of the event prediction is P = m/n = 16/17 = 94.12%, which is the probability of an extreme severe ﬁre in 2023.

<!-- b000445 | prose | pages [15] -->
6. We use the ﬁre acreage in the data to indicate the severity of extreme ﬁre condi- tions Sdanger, and similarly the ﬁre scale can be predicted by the ternary commensurable prediction model.

<!-- b000446 | heading | pages [15] -->
7. Test the predicted values and calculate the relative residuals:

<!-- b000447 | prose | pages [15] -->
ε(k) = x(0)(k) −ˆx(0)(k) , k = 1, 2, . . . , n. x(0)(k)

<!-- b000448 | prose | pages [15] -->
If for all ε|(k)| < 0.1, the higher requirement is considered to be reached; otherwise, if for all |ε(k)| < 0.2, the general requirement is considered to be reached.

<!-- b000449 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000450 | prose | pages [15] -->
关注数学模型

<!-- b000451 | furniture | pages [15] -->
2

<!-- b000452 | furniture | pages [15] -->
MATHmodels

<!-- b000453 | furniture | pages [15] -->
获取更多资讯

<!-- b000454 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000455 | furniture | pages [16] -->
Team # 2105363

<!-- b000456 | furniture | pages [16] -->
Page 16 of 25

<!-- b000457 | heading | pages [16] -->
4.1.2 Result of ternary commensurable ﬁre prediction model

<!-- b000458 | heading | pages [16] -->
1. Table of predicted years and residual test

<!-- b000459 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000460 | caption | pages [16] -->
Table 4: Table of predicted years

<!-- b000461 | prose | pages [16] -->
Years Probability Residual Residual change

<!-- b000462 | prose | pages [16] -->
2022 64.71% 53 2.62% 2023 94.12% 54 2.67% 2024 52.94% 55 2.72% 2027 41.18% 58 2.86%

<!-- b000463 | caption | pages [16] -->
Table 4 shows our predictions for the four possible years of extreme severity ﬁres

<!-- b000464 | prose | pages [16] -->
and the corresponding probabilities of it. The fourth column shows that the residual change in the occurrence of extreme ﬁres for all four years is around 2%, which is less 微信号：MATHmodels than 5%. This indicates that our predictions have a strong accuracy.

<!-- b000465 | heading | pages [16] -->
2. Pie map of predicted relative index

<!-- b000466 | caption | pages [16] -->
Figure 8: Pie map of predicted relative index

<!-- b000467 | prose | pages [16] -->
Based on the commensurable model, we predict the relative index of severity that would result from the next extreme severity ﬁre when it occurred. As shown in Figure 8, the next extreme severity ﬁre is most likely to produce a ﬁre with a severity index of 0-50. Also, ﬁres with larger severity indices have a high likelihood, accounting for more than half of the likelihood. Therefore, in order to meet future emergency response needs for large ﬁres, we may need to increase the number of drones or "Boots-on-the- ground" Forward Teams.

<!-- b000468 | heading | pages [16] -->
4.2 Increased Equipment Costs

<!-- b000469 | prose | pages [16] -->
After predicting the ﬁre, to accommodate changes in the likelihood of extreme ﬁre events over the next decade, we increase the equipment conﬁguration of the EOC and "boots-on-the-ground" ﬁreﬁghters for extreme ﬁre events only, getting the increased equipment costs.

<!-- b000470 | prose | pages [16] -->
Equipment includes handheld radios for the "boots-on-the-ground" teams, wear-

<!-- b000471 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000472 | prose | pages [16, 17] -->
able devices, and two-way radios for the EOC. From a safety perspective, we assume关注数学模型 that each "boots on the ground" squad ﬁreﬁghter has one handheld radio and one set of wearables, and that each EOC has one two-way radio for surveillance and commu- nications and one two-way radio for backup.

<!-- b000473 | furniture | pages [16] -->
2

<!-- b000474 | furniture | pages [16] -->
MATHmodels

<!-- b000475 | furniture | pages [16] -->
获取更多资讯

<!-- b000476 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000477 | furniture | pages [17] -->
Team # 2105363

<!-- b000478 | furniture | pages [17] -->
Page 17 of 25

<!-- b000480 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000481 | heading | pages [17] -->
4.2.1 Additional equipment costs for EOCs Cost(EOC)

<!-- b000482 | prose | pages [17] -->
When extreme ﬁres occur, the drone needs the appropriate EOC to support commu- nication and surveillance. Find the expected value E(number, extreme) of the number of extreme ﬁres that have a probability of occurring in the next ten years, which is equal to the sum of the probabilities of occurrence in the ﬁre prediction model.

<!-- b000483 | prose | pages [17] -->
N X P(ﬁres in i areas) · P(no ﬁres in N −i areas) · i, E(number, extreme) = i=1

<!-- b000484 | prose | pages [17] -->
where P denotes the probability.

<!-- b000485 | prose | pages [17] -->
微信号：MATHmodels From Task 1, we know that the number of EOCs responsible for extreme ﬁres is equal to the number of extreme ﬁres. So the cost of the additional equipment for the EOC is calculated as

<!-- b000486 | prose | pages [17] -->
Cost(EOC) = 2 × E(number, extreme) · Cost(radio). (13)

<!-- b000487 | heading | pages [17] -->
4.2.2 Additional equipment costs for ﬁreﬁghters Cost(ﬁreﬁghter)

<!-- b000488 | prose | pages [17] -->
The number of "boots on the ground" teams on each attendance is determined by the EOC after considering the severity of the ﬁre. The probability model for the ﬁre department to handle an extreme ﬁre event is established, and the probability of suc- cessful response to the ﬁre is estimated based on the number of team members Numi and the severity Sdanger,i in ith extreme ﬁre event.

<!-- b000489 | prose | pages [17] -->
Combined with the actual situation, the more serious the ﬁre, the smaller the pos- sibility of "boots-on-the-ground" squad to put out the ﬁre, while the more the number of squad, the greater the ability to deal with the ﬁre. This change in the relationship should be the ﬁrst slow then fast and ﬁnally slow trend, so the sigmoid function is selected to ﬁt. 1 P(success, i) = Sdanger,i + C), (14) Numi 1 + exp(−

<!-- b000490 | prose | pages [17] -->
where i ∈[1, E(number, extreme)] and C is a constant, from the article Brief introduction [3], it is known that the average number of Polish ﬁre de- of Polish volunteer ﬁre brigade partment is 24, we can use Fnumber,i = 24, Sdanger,i = average of Sdanger when the success rate is 0.8 to estimate C.

<!-- b000491 | prose | pages [17] -->
The EOC should ensure that the success rate of each team’s rescue is above 80% when making decisions. Substitute Sdanger,i, calculate the number of team members Pnumber,i for the ith extreme ﬁre with a success rate of exactly 0.8. And utilize the expected value of the increase in the number of "boots-on-the-ground" ﬁreﬁghters to estimate the number of increases needed.

<!-- b000492 | prose | pages [17] -->
M P(Numi) · P(ith extreme ﬁre occur). X E(Numi) =

<!-- b000493 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000494 | prose | pages [17, 18] -->
关注数学模型 i=1 The cost of additional equipment for ﬁreﬁghters of "boots on the ground" is:

<!-- b000495 | furniture | pages [17] -->
2

<!-- b000496 | furniture | pages [17] -->
MATHmodels

<!-- b000497 | furniture | pages [17] -->
获取更多资讯

<!-- b000498 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000499 | furniture | pages [18] -->
Team # 2105363

<!-- b000500 | furniture | pages [18] -->
Page 18 of 25

<!-- b000502 | prose | pages [18] -->
Cost(ﬁreﬁghter) = E(Numi) · (Cost(radio) + Cost(wearable device)). (15) 微信公众号：数学模型

<!-- b000503 | heading | pages [18] -->
4.2.3 Results of additional equipment

<!-- b000504 | prose | pages [18] -->
Equipment Number Single price Total price EOC radios 5 92.725 463.625 1,800 “Boots-on-the-ground” handheld radios 19 94.741 “Boots-on-the-ground” team wearable 2,688.625 19 141.507 equipment

<!-- b000505 | caption | pages [18] -->
Figure 9: Number of additional equipment

<!-- b000506 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000507 | heading | pages [18] -->
5 Task 3: Location Optimization

<!-- b000508 | prose | pages [18] -->
In the greedy and multiplexing based solution algorithms of Task 1, we have ob- tained the ideal distribution range of each repeater drone. Based on this, we consider the signal loss and safety of the repeater drone to optimize its optimal position in the ideal distribution range.

<!-- b000509 | heading | pages [18] -->
5.1 Signal loss model

<!-- b000510 | prose | pages [18] -->
SPM model is suitable for propagation loss prediction for distances from 1 to 20 km and frequencies from 150 to 3500 MHz, running GSM and other communication systems. This model takes the feature classiﬁcation map and effective antenna height [4]. into account to calculate the path loss. Its basic equation is shown in Formula 16

<!-- b000511 | prose | pages [18] -->
L1 = K1 + K2 lg d + K3 lg HTxeff + K4Diff_loss (16) + K5 lg HTxeff lg d + K6HRxeff + Kchitterf(clutter),

<!-- b000512 | prose | pages [18] -->
where K4 is the multiplicative factor of the bypassing amount; Diff_loss(unit: dB) is the loss caused by bypassing the obstacle; K6 is the multiplicative factor of HRxeff, Rxeff is the mobile station receiving antenna height. K1, K2 and other variables are related to the height and distance of the signal base station as well as environment of drones.

<!-- b000513 | prose | pages [18] -->
For the repeater drone, when the siting is varied within the ideal distribution, K1, K2, K3, HTxeff, K4, K5, K6, and Kchitter are unchanged, and the small change of d is negligible, only HRxeff and Diff_loss will change. Therefore, the signal loss model of the repeater drone is established as follows.

<!-- b000514 | prose | pages [18] -->
L2 = K4 · Diff_loss + K6 · HRxeff + L0, (17)

<!-- b000515 | prose | pages [18] -->
[8] K4 = 44.9 −6.55 log HRxeff, [8] K6 = 1.1 log frepeater −0.7, 4π

<!-- b000516 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000517 | prose | pages [18] -->
[8] 关注数学模型 L0 = 20 log10( ),

<!-- b000518 | furniture | pages [18] -->
2

<!-- b000519 | prose | pages [18, 19] -->
λtransmitted wave where fradio is frequency of repeater. λtransmitted wave is wavelength of transmitted wave in meters.

<!-- b000520 | furniture | pages [18] -->
MATHmodels

<!-- b000521 | furniture | pages [18] -->
获取更多资讯

<!-- b000522 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000523 | furniture | pages [19] -->
Team # 2105363

<!-- b000524 | furniture | pages [19] -->
Page 19 of 25

<!-- b000526 | prose | pages [19] -->
For Rxeff, drone altitude = altitude of location + height above ground.

<!-- b000527 | prose | pages [19] -->
微信公众号：数学模型 For Diff_loss, we assume that the height of the obstacle is linearly related to the loss of the repeater range, with the most severe loss for obstacle heights greater than 1.5·Rxeff and considered almost no loss effect for obstacle heights less than 0.5·Rxeff. In the ideal case the loss ratio δ is 1.0, the worst case is 0.8. The loss ratio of the ith obstacle :

<!-- b000528 | prose | pages [19] -->
δi = (Hi/Rxeff) · (1 −0.7)/(1.5 −0.5) + 0.7. where Hi is the height of the ith obstacle Counting K obstacles on the linear path be- tween the repeater drone and the ﬁre area in 1000m. Calculate Diff_loss:

<!-- b000529 | prose | pages [19] -->
Y Diff_loss = δi. (18) i=1,2,...,K

<!-- b000530 | prose | pages [19] -->
[9] we can see that we should ensure that the signal-to-noise ratio 微信号：MATHmodels From the website is not less than 20dB, that is, L2 ⩾20dB. (19)

<!-- b000531 | prose | pages [19] -->
We use this formula to ﬁlter out the areas that do not meet the requirements.

<!-- b000532 | heading | pages [19] -->
5.2 Drone safety

<!-- b000533 | prose | pages [19] -->
Depending on the scale of the ﬁre, repeater drones need to avoid nearby ﬁres to ensure safe operations. Because of the limited signal range of handheld radio, repeater drones are often located 2 to 5 km from the center of the ﬁre, and when the ﬁre is large and the terrain is ﬂammable, it is easy to spread to the repeater drone is located, causing damage to the drone in serious cases. We perform a quantitative analysis of safety based on information related to ﬁres.

<!-- b000534 | heading | pages [19] -->
Kinetics-based ﬁre spread model:

<!-- b000535 | prose | pages [19] -->
𝑣_𝑤𝑖𝑛𝑑

<!-- b000536 | caption | pages [19] -->
Figure 10: Kinetic-based ﬁre spread model schematic

<!-- b000537 | prose | pages [19] -->
As shown in the Figure 10, the ﬁre spread into eight directions, of which the direc- tion of the angle with the wind speed less than 45 degrees will spread outside (such as the direction of the yellow arrow), the other directions remain unchanged (such as the

<!-- b000538 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000539 | prose | pages [19] -->
关注数学模型 direction of the blue arrow).

<!-- b000540 | furniture | pages [19] -->
2

<!-- b000541 | furniture | pages [19] -->
MATHmodels

<!-- b000542 | furniture | pages [19] -->
获取更多资讯

<!-- b000543 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000544 | furniture | pages [20] -->
Team # 2105363

<!-- b000545 | furniture | pages [20] -->
Page 20 of 25

<!-- b000546 | prose | pages [20] -->
Vspread =⃗Vwind × exp((D + topography scoring) · ﬁre size + E),

<!-- b000547 | prose | pages [20] -->
where⃗Sr denotes the rate of spread in the vector direction, and D and E both denote 微信公众号：数学模型 constants.

<!-- b000548 | prose | pages [20] -->
In the ﬁre spread range, the amount of change in the length of the ﬁre⃗k direction is

<!-- b000549 | prose | pages [20] -->
( Vspread ×⃗k × unit time, Vspread ×⃗k > 0 ∆⃗Lk = , 0, others

<!-- b000550 | prose | pages [20] -->
and length of ﬁre⃗k direction is

<!-- b000551 | prose | pages [20] -->
Lk =⃗Lk(last time) + ∆⃗Lk.

<!-- b000552 | prose | pages [20] -->
Wind speeds were obtained from SSA drones collecting data from “boots-on-the- ground” teams, and terrain was scored to create a scoring table as follows. 微信号：MATHmodels

<!-- b000553 | caption | pages [20] -->
Table 5: Terrain scoring table

<!-- b000554 | prose | pages [20] -->
Terrains Scores

<!-- b000555 | prose | pages [20] -->
Forests, grassy hills, grasslands 3 Plains, other terrain 2 Not happened recently 1

<!-- b000556 | prose | pages [20] -->
To ensure safety, the distance between the ith repeater drone position (xdrone,i, ydrone,i), which is in a certain direction of the ﬁre, and the edge of the ﬁre should be made no less than the safety threshold, which is set here to 50 m. Therefore,

<!-- b000557 | prose | pages [20] -->
|(xdrone,i, ydrone,i) −(x, y) of center| ⩾50 + the range length of the ﬁre. (20)

<!-- b000558 | prose | pages [20] -->
where "(x, y) of the center" denotes the latitude and longitude of the ﬁre center. "The range length of the ﬁre" means the range length in a certain direction of the ﬁre at a certain moment.

<!-- b000559 | prose | pages [20] -->
Location optimization:

<!-- b000560 | prose | pages [20] -->
The signal-to-noise ratio and distance from the edge of the ﬁre are calculated for each location in the ideal distribution range, and reasonable locations are selected:

<!-- b000561 | prose | pages [20] -->
[9] L2 ⩾20dB.

<!-- b000562 | prose | pages [20] -->
We use this constraint to optimize to get the drone range from the point of view of preventing ﬁre spread hazards by drones.

<!-- b000563 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000564 | prose | pages [20] -->
关注数学模型

<!-- b000565 | furniture | pages [20] -->
2

<!-- b000566 | furniture | pages [20] -->
MATHmodels

<!-- b000567 | furniture | pages [20] -->
获取更多资讯

<!-- b000568 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000569 | furniture | pages [21] -->
Team # 2105363

<!-- b000570 | furniture | pages [21] -->
Page 21 of 25

<!-- b000571 | heading | pages [21] -->
5.3 Result analysis

<!-- b000572 | prose | pages [21] -->
𝐿𝑎𝑡𝑖𝑡𝑢𝑑𝑒 𝑎𝑛𝑑 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒: −37.4935, 147.3724 𝐿𝑎𝑡𝑖𝑡𝑢𝑑𝑒 𝑎𝑛𝑑 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒: −36.7322, 147.3058 𝐻𝑒𝑖𝑔ℎ𝑡: 14m 𝐹𝑖𝑟𝑒 𝑑𝑖𝑟𝑒𝑐𝑡𝑖𝑜𝑛 𝐻𝑒𝑖𝑔ℎ𝑡: 1986m 𝐹𝑖𝑟𝑒 𝑑𝑖𝑟𝑒𝑐𝑡𝑖𝑜𝑛 微信公众号：数学模型 𝐼𝑑𝑒𝑎𝑙 𝑐𝑎𝑛𝑑𝑖𝑑𝑎𝑡𝑒 𝑟𝑎𝑛𝑔𝑒

<!-- b000573 | prose | pages [21] -->
𝑂𝑝𝑡𝑖𝑚𝑖𝑧𝑒𝑑 𝑜𝑝𝑡𝑖𝑜𝑛𝑎𝑙 𝑟𝑎𝑛𝑔𝑒

<!-- b000574 | prose | pages [21] -->
𝑁𝑜𝑛 𝑠𝑎𝑓𝑒𝑟 𝑎𝑟𝑒𝑎𝑠 (b) The lowest altitude (a) The highest altitude

<!-- b000575 | caption | pages [21] -->
Figure 11: Optimization of the location of the highest and lowest points of altitude

<!-- b000576 | prose | pages [21] -->
Obviously, the wind direction directly affects the distribution of the optimized re- 微信号：MATHmodels peater drones, which is concentrated at the edge of the ideal range perpendicular to the wind direction. High altitude areas are more likely to be affected by the altitude of dif- ferent locations, which manifests itself in the form of a discontinuous and interrupted range of the optimized distribution.

<!-- b000577 | heading | pages [21] -->
6 Sensitivity analysis

<!-- b000578 | heading | pages [21] -->
6.1 Sensitivity Analysis of safety factor S(x, y)

<!-- b000579 | prose | pages [21] -->
In Task 1, we classify the areas of Victoria as different danger levels by calculating the safety factor. Therefore, the safety factor S(x, y) is a crucial parameter, which is cal- culated by ﬁre frequency f(x, y), ﬁze size size(x, y), recent ﬁre situation situation(x, y) (see Formula 4). As a result, we do sensitivity analysis on the coefﬁcients a1, a2 and a3 of these three parameters and the results are shown in Figure 12.

<!-- b000580 | prose | pages [21] -->
1 Comprehensive safety factor S(x,y) 0.9

<!-- b000581 | prose | pages [21] -->
0.8

<!-- b000582 | prose | pages [21] -->
0.7

<!-- b000583 | prose | pages [21] -->
0.6

<!-- b000584 | prose | pages [21] -->
0.5

<!-- b000585 | prose | pages [21] -->
0.4

<!-- b000586 | prose | pages [21] -->
0.3

<!-- b000587 | prose | pages [21] -->
0.2

<!-- b000588 | prose | pages [21] -->
0.1

<!-- b000589 | prose | pages [21] -->
0 -10% -10% -5% -5% 0 0 5% 5% 10% 10% -10% -10% -5% -5% 0 0 5% 5% 10% 10% -10% -10% -5% -5% 0 0 5% 5% 10% 10% 1a a 3a 2 The weight change of parameter a

<!-- b000590 | caption | pages [21] -->
Figure 12: Sensitivity Analysis of S(x, y)

<!-- b000591 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000592 | prose | pages [21, 22] -->
关注数学模型 In Figure 12, we select a high-risk area as a place to test sensitivity, and the coordi- nate is (x, y) = (−36.0634, 148.2911)

<!-- b000593 | furniture | pages [21] -->
2

<!-- b000594 | furniture | pages [21] -->
MATHmodels

<!-- b000595 | furniture | pages [21] -->
获取更多资讯

<!-- b000596 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000597 | furniture | pages [22] -->
Team # 2105363

<!-- b000598 | furniture | pages [22] -->
Page 22 of 25

<!-- b000600 | prose | pages [22] -->
From the ﬁgure we can conclude that When the variation of a1, a2 and a3 change from -10% to 10%, the changes in the values of S(x, y) corresponding to a1 and a3 are 微信公众号：数学模型 small and the overall trend is ﬂat. Therefore, we believe that the frequency and size of ﬁres are more robust and do not affect S too much. Meanwhile, a2 corresponds to a relatively large amount of change in S(x, y), so we think the sensitivity of the recent ﬁre situation to be strong. This result veriﬁes the reasonableness of our consideration of situation(x, y) in Section 3.1.1.

<!-- b000601 | heading | pages [22] -->
6.2 Sensitivity analysis of ﬁre frequency in different regions per year

<!-- b000602 | prose | pages [22] -->
The annual frequency of ﬁres in different regions has a signiﬁcant impact on the number of SSA drones. Therefore, we divid Victoria into central, eastern, western, and southern regions, and do sensitivity analysis on the ﬁre frequency in each of these four 微信号：MATHmodels geographic regions.

<!-- b000603 | prose | pages [22] -->
400

<!-- b000604 | prose | pages [22] -->
Number of SSA drones 320

<!-- b000605 | prose | pages [22] -->
240

<!-- b000606 | prose | pages [22] -->
180

<!-- b000607 | prose | pages [22] -->
Central region Eastern region 120 Western region Southern region

<!-- b000608 | prose | pages [22] -->
60

<!-- b000609 | prose | pages [22] -->
0 400 800 1200 1600 2000 2400 2800 3200 3600 Frequency of fire(times/year)

<!-- b000610 | caption | pages [22] -->
Figure 13: Sensitivity analysis of ﬁre frequency in different regions per year

<!-- b000611 | prose | pages [22] -->
We can analyze Figure 13 in two ways. For ﬁre frequency, the number of SSA drones vary the most when the number of ﬁres in Victoria is in the range of 1600∼2000 per year. That is, the ﬁre frequency is sensitive in the interval [1600,2000]. Therefore, when CFA uses our model, if the measured number of ﬁres in the year is within this interval, they should calculate the number of SSA drones very carefully.

<!-- b000612 | prose | pages [22] -->
For different regions, the number of SSA drones in the four regions change sig- niﬁcantly when the ﬁre frequency is greater than 1600. The central region of Victoria has the highest number, while the southern region has the lowest. Therefore, regions are also sensitive to the number of SSA drones, and CFA’s drone dispatch should be different in different regions.

<!-- b000613 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000614 | prose | pages [22] -->
关注数学模型

<!-- b000615 | furniture | pages [22] -->
2

<!-- b000616 | furniture | pages [22] -->
MATHmodels

<!-- b000617 | furniture | pages [22] -->
获取更多资讯

<!-- b000618 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000619 | furniture | pages [23] -->
Team # 2105363

<!-- b000620 | furniture | pages [23] -->
Page 23 of 25

<!-- b000621 | heading | pages [23] -->
7 Strengths and Weaknesses

<!-- b000622 | heading | pages [23] -->
7.1 Strengths

<!-- b000623 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000624 | prose | pages [23] -->
• We innovatively use safety factors to classify classes for areas with different ﬁre conditions, which improves the efﬁciency of drone response for emergency situ- ations and provides a clear idea for drone dispatching and distribution.

<!-- b000625 | prose | pages [23] -->
• The combination and reuse relationship between drones is used to optimize the utilization rate of repeater drones, which both ﬁts the actual situation and has a universal solution to other conﬁguration problems.

<!-- b000626 | prose | pages [23] -->
• The ternary commensurable prediction model is a model that predicts the prob- ability of future special situations for data of special situations, and the commen- surabiliby it considers is very accurate in the face of special situations with the superiority that other forecasting models do not have.

<!-- b000627 | prose | pages [23] -->
• We have reviewed a large amount of literature, not only with sufﬁcient data, but also with estimation and calculation methods for the parameters of each model 微信号：MATHmodels from specialized literature, and the results are scientiﬁc and rigorous.

<!-- b000628 | heading | pages [23] -->
7.2 Weaknesses

<!-- b000629 | prose | pages [23] -->
• In the problem of optimizing the position of the repeater drone, we are limited by the data for the simulation solution, and the results may be somewhat different from the real situation.

<!-- b000630 | prose | pages [23] -->
• The index estimated by using AHP model has some subjective inﬂuence, and sensitivity analysis is needed to calculate the reliability of the model.

<!-- b000631 | heading | pages [23] -->
8 Annotated Budget Request

<!-- b000632 | prose | pages [23] -->
Budget Justiﬁcation for Cost Proposal (Unit: A$)

<!-- b000633 | prose | pages [23] -->
We are a numerical modeling competition team from MCM and will be responsi- ble for the overall management and direction of the Victorian National Fire Service’s drone acquisition program for the Rapid Bushﬁre Response Division and equipment acquisition program for extreme ﬁres over the next decade, based on the soundness of our models through testing and analysis of results.

<!-- b000634 | prose | pages [23] -->
1. "Rapid Jungle Response" Project

<!-- b000635 | prose | pages [23] -->
Direct costs: 2,401,030

<!-- b000636 | prose | pages [23] -->
Drones Number Single price Total price SSA drones 200 10,390 2,077,200 Radio repeater drones 32 10,094.741 323,030

<!-- b000637 | prose | pages [23] -->
The number of SSA drones procured to respond to emergency ﬁre situations in Vic- toria includes 134 shift SSA drones for emergency response to high-risk areas, 62 SSA drones for ﬁre preparedness in prepared areas, and 4 standby drones for considera-

<!-- b000638 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000639 | prose | pages [23, 24] -->
tion of wear and tear. The cost of each SSA drone includes the cost of a bare drone at关注数学模型 A$10,000, an HD camera at A$47.370, and a thermal imaging camera at A$338.648; the repeater drones include 21 repeater drones in combination with SSA drones in high- risk areas and 21 repeater drones in combination with SSA drones in preparedness areas 11, the cost of each repeater drone includes a bare drone of A$10,000, the cost of 微信公众号：数学模型 a repeater of A$94.741.

<!-- b000640 | furniture | pages [23] -->
2

<!-- b000641 | furniture | pages [23] -->
MATHmodels

<!-- b000642 | furniture | pages [23] -->
获取更多资讯

<!-- b000643 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000644 | furniture | pages [24] -->
Team # 2105363

<!-- b000645 | furniture | pages [24] -->
Page 24 of 25

<!-- b000647 | prose | pages [24] -->
With this drone conﬁguration, the drones can detect all 373 locations (including 154 high-risk areas and 219 precautionary areas) throughout the state with high frequency and large ﬁre sizes, and have an average response time to emergency ﬁres of only 5 minutes and 17 seconds. In addition, each repeater drone achieved a combined rate of 6.25 with SSA drones. the overall system had excellent responsiveness and excellent combined relationships.

<!-- b000648 | prose | pages [24] -->
Other costs: None.

<!-- b000649 | prose | pages [24] -->
Electricity cost for drone charging: A$0.

<!-- b000650 | prose | pages [24] -->
Our analysis of the infrastructure within the Victorian State Fire Service concluded that the infrastructure within the Fire Service can accommodate the normal conduct of 微信号：MATHmodels activities for other costs and therefore the cost is 0.

<!-- b000651 | heading | pages [24] -->
2. Equipment procurement items to respond to extreme ﬁres over the next ten

<!-- b000652 | prose | pages [24] -->
years

<!-- b000653 | prose | pages [24] -->
Direct Costs: 148,950

<!-- b000654 | prose | pages [24] -->
Additional equipment (abbreviated): $A 4952.25

<!-- b000655 | prose | pages [24] -->
Equipment Number Single price Total price EOC radios 5 92.725 463.625 1,800 “Boots-on-the-ground” handheld radios 19 94.741 “Boots-on-the-ground” team wearable 2,688.625 19 141.507 equipment

<!-- b000656 | prose | pages [24] -->
From a safety perspective, we consider a one-to-one EOC for extreme ﬁres and adjust the number of ﬁreﬁghters in the Ground Boots team based on the predicted size of the extreme ﬁre. We provide a handheld radio and a set of wearables for each ﬁreﬁghter in the "boots on the ground" team, with one two-way radio and a backup two-way radio per EOC. The unit cost of the wearables included a ﬁre axe for $11.288, a heat suit for $120.442, and a ﬁre extinguisher for $9.877. According to our modeling, this scenario has a success rate of more than 80% for "boots on the ground" teams for extreme ﬁres.

<!-- b000657 | prose | pages [24] -->
Staff cost: 144,000

<!-- b000658 | prose | pages [24] -->
Staff Number Single price Total price Command staff within EOC 5 6,000 30,000 Firefighters in “Boots-on-the-ground” 19 6,000 114,000

<!-- b000659 | prose | pages [24] -->
We consider subsidizing a bonus for ﬁreﬁghters to encourage their performance in ﬁre rescue, and similarly, for each EOC, the hard work of the command staff is worth a bonus. We refer to the federal government’s subsidy for volunteer ﬁreﬁghters in New

<!-- b000660 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000661 | prose | pages [24] -->
关注数学模型 South Wales for the bonus assessment.

<!-- b000662 | furniture | pages [24] -->
2

<!-- b000663 | furniture | pages [24] -->
MATHmodels

<!-- b000664 | furniture | pages [24] -->
获取更多资讯

<!-- b000665 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000666 | furniture | pages [25] -->
Team # 2105363

<!-- b000667 | furniture | pages [25] -->
Page 25 of 25

<!-- b000668 | prose | pages [25] -->
Other costs: None

<!-- b000669 | prose | pages [25] -->
Cost of apparatus consumption: None

<!-- b000670 | prose | pages [25] -->
Wear and tear of ﬁreﬁghting equipment: A$0 Loss of drones: $0 微信公众号：数学模型 The primary job of the "boots on the ground" team is to detect ﬁrst-hand informa- tion about the ﬁre, make judgments about the rapidly changing situation, and pass additional information to the EOC. Therefore, ﬁre ﬁghting is not their main job, the consumption of ﬁreﬁghting equipment is negligible. The wear and tear of drones is already considered in the cost of drones.

<!-- b000671 | heading | pages [25] -->
References

<!-- b000672 | references | pages [25] -->
https://firms.modaps.eosdis.na

<!-- b000673 | references | pages [25] -->
[1] Active Fire Data. [online] Available at:

<!-- b000674 | references | pages [25] -->
sa.gov/active_fire/#firms-shapefile [Accessed 6 Feb. 2021]

<!-- b000675 | references | pages [25] -->
微信号：MATHmodels

<!-- b000676 | references | pages [25] -->
http:

<!-- b000677 | references | pages [25] -->
[2] When exactly will the ﬁre in Australia be put out?. [online] Available at:

<!-- b000678 | references | pages [25] -->
//www.ctoutiao.com/2585517.html [Accessed 6 Feb. 2021]

<!-- b000679 | references | pages [25] -->
[3] Zhao

<!-- b000680 | references | pages [25] -->
Zeming.

<!-- b000681 | references | pages [25] -->
Brief

<!-- b000682 | heading | pages [25] -->
introduction

<!-- b000683 | prose | pages [25] -->
of Polish volunteer ﬁre brigade[J].Fire technology and product information,2014,(6):116,47. DOI:10.3969/j.issn.1002- 784X.2014.06.044.

<!-- b000684 | prose | pages [25] -->
[4] Chu Peisi. Research and system measurement of wireless signal propagation loss prediction algorithm in mobile communication system[D]. Sichuan:University of Electronic Science and Technology, 2013. DOI:10.7666/d.D762613.

<!-- b000685 | prose | pages [25] -->
https://en.wikip [5] List of major bushﬁres in Australia. [online] Available at:

<!-- b000686 | prose | pages [25] -->
edia.org/wiki/List_of_major_bushfires_in_Australia [Accessed 8 Feb. 2021]

<!-- b000687 | prose | pages [25] -->
[6] Huang Jinfeng, Xia Jun, Du Hong, et al. Medium- and long-term ﬂood fore- casting at Lutaizi and Bengbu stations based on metrizability and gray corre- lation pattern recognition method[J]. Journal of Wuhan University (Engineering Edition),2015,48(5):622-626. DOI:10.14188/j.1671-8844.2015-05-005.

<!-- b000688 | prose | pages [25] -->
[7] Yellow River Survey, Planning and Design Co. Feasibility study report of the downstream Yellow River ﬂood control project [R]. Zhengzhou: Yellow River Sur- vey, Planning and Design Co., Ltd, 2015: 4-192.

<!-- b000689 | prose | pages [25] -->
[8] B. Sridhar and M. Z. Ali Khan, "RMSE comparison of path loss models for UH- F/VHF bands in India," 2014 IEEE REGION 10 SYMPOSIUM, Kuala Lumpur, 2014, pp. 330-335, doi: 10.1109/TENCONSpring.2014.6863052.

<!-- b000690 | prose | pages [25] -->
[9] What is the general signal-to-noise ratio, the useful signal will not be drowned. [online] zhidao.baidu.com/question/624747251070347044.ht Available at:

<!-- b000691 | prose | pages [25] -->
ml [Accessed 8 Feb. 2021]

<!-- b000692 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000693 | prose | pages [25] -->
关注数学模型

<!-- b000694 | furniture | pages [25] -->
2

<!-- b000695 | furniture | pages [25] -->
MATHmodels

<!-- b000696 | furniture | pages [25] -->
获取更多资讯
