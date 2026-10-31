# P-B-2021-2105363-52f891b1

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | furniture | pages [1] -->
2021

<!-- b000004 | prose | pages [1] -->
Problem Chosen

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

<!-- b000020 | keywords | pages [1] -->
Keywords: safety factor

<!-- b000021 | prose | pages [1] -->
关注数学模型 commensurable signal-to-noise ratio

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team # 2105363

<!-- b000026 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000027 | furniture | pages [2] -->
Page 2 of 25

<!-- b000028 | heading | pages [2] -->
Contents

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | heading | pages [2] -->
Introduction

<!-- b000031 | prose | pages [2] -->
3 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000032 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000033 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000034 | prose | pages [2] -->
2

<!-- b000035 | heading | pages [2] -->
Preparation of the Models

<!-- b000036 | prose | pages [2] -->
3

<!-- b000037 | prose | pages [2] -->
3 Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . 2.1 3 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 4 Drones voyage model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 4 Data pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4 5

<!-- b000038 | prose | pages [2] -->
Task 1: Optimal Numbers and Mix of Two Types of Drones 3 5 Area safety evaluation model . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5 Indicators establishment . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1 5 Safety factors S(x, y) and danger levels . . . . . . . . . . . . . . . 3.1.2 3.1.3 Result analyze of heat map 7 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | prose | pages [2] -->
8

<!-- b000040 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000041 | prose | pages [2] -->
Optimization of the number and mix of drones . . . . . . . . . . . . . . . 3.2 8 Maximum drone capability . . . . . . . . . . . . . . . . . . . . . . 3.2.1 8 Minimal drone costs . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2 9 Number and mix of drones . . . . . . . . . . . . . . . . . . . . . . 3.2.3 9 Optimization model with maximum mix rate and minimum cost 3.3 . . . .

<!-- b000042 | prose | pages [2] -->
13 Result Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.1 13

<!-- b000043 | heading | pages [2] -->
Task 2: Adaptation of Model and Cost Increases for Equipment

<!-- b000044 | prose | pages [2] -->
4 13 Ternary commensurable ﬁre prediction model 4.1 . . . . . . . . . . . . . . .

<!-- b000045 | prose | pages [2] -->
14 . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 Model building process 14 Result of ternary commensurable ﬁre prediction model . . . . . . 4.1.2 16 . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Increased Equipment Costs 16 Additional equipment costs for EOCs Cost(EOC) . . . . . . . . . 4.2.1 17 Additional equipment costs for ﬁreﬁghters Cost(ﬁreﬁghter) . . . 4.2.2 17 Results of additional equipment 4.2.3

<!-- b000046 | prose | pages [2] -->
5 Task 3: Location Optimization

<!-- b000047 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000048 | prose | pages [2] -->
18

<!-- b000049 | prose | pages [2] -->
18 Signal loss model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 18 Drone safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 19 Result analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000050 | prose | pages [2] -->
6

<!-- b000051 | heading | pages [2] -->
Sensitivity analysis

<!-- b000052 | prose | pages [2] -->
21

<!-- b000053 | prose | pages [2] -->
21 Sensitivity Analysis of safety factor S(x, y) 6.1 . . . . . . . . . . . . . . . . .

<!-- b000054 | prose | pages [2] -->
21 Sensitivity analysis of ﬁre frequency in different regions per year 6.2

<!-- b000055 | prose | pages [2] -->
7

<!-- b000056 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000057 | prose | pages [2] -->
. . . .

<!-- b000058 | prose | pages [2] -->
22

<!-- b000059 | prose | pages [2] -->
23 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 23 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Weaknesses

<!-- b000060 | prose | pages [2] -->
8 Annotated Budget Request

<!-- b000061 | heading | pages [2] -->
References

<!-- b000062 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000063 | references | pages [2] -->
23

<!-- b000064 | references | pages [2] -->
23

<!-- b000065 | references | pages [2] -->
25

<!-- b000066 | references | pages [2] -->
关注数学模型

<!-- b000067 | furniture | pages [2] -->
2

<!-- b000068 | furniture | pages [2] -->
MATHmodels

<!-- b000069 | furniture | pages [2] -->
获取更多资讯

<!-- b000070 | furniture | pages [3] -->
Team # 2105363

<!-- b000071 | references | pages [3] -->
1

<!-- b000072 | heading | pages [3] -->
Introduction

<!-- b000073 | prose | pages [3] -->
1.1 Problem Background

<!-- b000074 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000075 | furniture | pages [3] -->
Page 3 of 25

<!-- b000076 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000077 | prose | pages [3] -->
Australia’s hot and dry climate, with many hills and few mountains, makes it one of the most forest ﬁre-prone places in the world. Since the ﬁrst ﬁre in New South Wales in September 2019, New South Wales and eastern Victoria was severly affected.

<!-- b000078 | prose | pages [3] -->
Fireﬁghters have used drones for surveillance and situational awareness (SSA) to allow the Emergency Operations Center (EOC) best direct active crews for optimal effect and maximal safety. The main task of drones is to monitor places where ﬁres are violent and where it is easy to grow into active ﬁres.

<!-- b000079 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000080 | prose | pages [3] -->
After understanding the relevant background information, the team are supposed

<!-- b000081 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000082 | prose | pages [3] -->
to do the following:

<!-- b000083 | prose | pages [3] -->
• Create a model to determine the optimal numbers and mix of SSA drones and Radio Repeater drones.

<!-- b000084 | prose | pages [3] -->
• Illustrate how your model adapts to the changing likelihood of extreme ﬁre events over the next decade. Project what equipment cost increases will occur assuming the cost of drone systems stays constant.

<!-- b000085 | prose | pages [3] -->
• Determine a model for optimizing the locations of hovering VHF/UHF radio- repeater drones.

<!-- b000086 | prose | pages [3] -->
2

<!-- b000087 | heading | pages [3] -->
Preparation of the Models

<!-- b000088 | heading | pages [3] -->
Assumptions and Justiﬁcations

<!-- b000089 | prose | pages [3] -->
2.1

<!-- b000090 | heading | pages [3] -->
1. The EOC can be deployed and moved to locations as needed for ﬁreﬁghting mis-

<!-- b000091 | prose | pages [3] -->
sions, with negligible cost of deployment and movement. And it is responsible for ﬁre rescue situations in only one area at a time.

<!-- b000092 | prose | pages [3] -->
EOC can be moved and deployed according to the ﬁre situation, and its cost is labor cost and equipment cost. The labor cost is more complicated and is a ﬁxed expendi- ture for the ﬁre department, so it is not considered.

<!-- b000093 | heading | pages [3] -->
2. When calculating the distance we consider that the distance is a straight line dis-

<!-- b000094 | prose | pages [3] -->
tance in a spatial three-dimensional coordinate system.

<!-- b000095 | prose | pages [3] -->
There is a big difference between the altitude of the Victorian mountains and the plains, so the distance obtained by considering the altitude is more accurate.

<!-- b000096 | heading | pages [3] -->
3. The repeaters can receive signals from multiple targets and forward them to mul-

<!-- b000097 | prose | pages [3] -->
tiple targets.

<!-- b000098 | prose | pages [3] -->
This is determined by the function of the repeater. A repeater located between the front lines and the EOC can relay radio signals both from the front lines to the EOC

<!-- b000099 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000100 | prose | pages [3] -->
and from the EOC to the front lines.

<!-- b000101 | prose | pages [3] -->
关注数学模型

<!-- b000102 | furniture | pages [3] -->
2

<!-- b000103 | furniture | pages [3] -->
MATHmodels

<!-- b000104 | furniture | pages [3] -->
获取更多资讯

<!-- b000105 | furniture | pages [4] -->
Team # 2105363

<!-- b000106 | heading | pages [4] -->
4. Drones only serve part of the ﬁre.

<!-- b000107 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000108 | furniture | pages [4] -->
Page 4 of 25

<!-- b000109 | prose | pages [4] -->
Fires in Australia are common, thus it is less likely to attract widespread attention when an average sized ﬁre occurs. And can be quickly extinguished by local ﬁre forces, without dedicated drone deployment.

<!-- b000110 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000111 | heading | pages [4] -->
5. The drone needs to adjust its position when working.

<!-- b000112 | prose | pages [4] -->
To avoid damage to the drone caused by the effects of ﬁre.

<!-- b000113 | prose | pages [4] -->
2.2

<!-- b000114 | heading | pages [4] -->
Notations

<!-- b000115 | prose | pages [4] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000116 | caption | pages [4] -->
Table 1: Notations

<!-- b000117 | prose | pages [4] -->
Symbol Deﬁnition

<!-- b000118 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000119 | prose | pages [4] -->
r drone scanning radius a place with longitude x and latitude y (x, y) ﬁre frequency at (x, y) f(x, y) size(x, y) ﬁre size at (x, y) recent ﬁre situation at (x, t) situation(x, y) safety factor at (x, y) S(x, y) xi the distance between the EOC and the high-risk area Cost(drone) total cost of two types of drones m number of SSA drones n number radio repeater drones L2 signal-to-noise ratio

<!-- b000120 | prose | pages [4] -->
2.3

<!-- b000121 | heading | pages [4] -->
Drones voyage model

<!-- b000122 | prose | pages [4] -->
Considering the drone power problem,

<!-- b000123 | prose | pages [4] -->
(km ) Voyage

<!-- b000124 | prose | pages [4] -->
the ﬂight range of the drones are related to the average velocity (only consider single

<!-- b000125 | prose | pages [4] -->
30

<!-- b000126 | prose | pages [4] -->
trip), and the relationship between them is For practical considerations, we parabolic. formulate that the average speed of the drone

<!-- b000127 | prose | pages [4] -->
27.8

<!-- b000128 | prose | pages [4] -->
cannot exceed 10m/s (i.e., max{v} = 10m/s). When the drone is in the maximum ﬂight

<!-- b000129 | prose | pages [4] -->
At this speed, the drone

<!-- b000130 | prose | pages [4] -->
time (i.e. 2.5 hours), the drone range is max-

<!-- b000131 | prose | pages [4] -->
has the largest range.

<!-- b000132 | prose | pages [4] -->
imum, and the average velocity of the drone is 30km/2.5h ≈3.3m/s. The corresponding relationship is shown in the ﬁgure below.

<!-- b000133 | prose | pages [4] -->
0 3.3 10 ( / ) vavg m s

<!-- b000134 | caption | pages [4] -->
Figure 1: Relationship of V oyage and vmax

<!-- b000135 | caption | pages [4] -->
Figure 1 shows the length of drones’ voy-

<!-- b000136 | prose | pages [4] -->
age average velocity curve, which is a parabolic. What we obtain is as follows by ﬁtting data.

<!-- b000137 | prose | pages [4] -->
V oyage(v) = −0.2 × v2 + 1.32 × v + 27.8 (km), (1)

<!-- b000138 | prose | pages [4] -->
where V oyage(v) is the length of vayage when drones travel with the average speed of

<!-- b000139 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000140 | prose | pages [4] -->
v.

<!-- b000141 | prose | pages [4] -->
关注数学模型

<!-- b000142 | furniture | pages [4] -->
2

<!-- b000143 | furniture | pages [4] -->
MATHmodels

<!-- b000144 | furniture | pages [4] -->
获取更多资讯

<!-- b000145 | furniture | pages [5] -->
Team # 2105363

<!-- b000146 | prose | pages [5] -->
2.4 Data pre-processing

<!-- b000147 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000148 | furniture | pages [5] -->
Page 5 of 25

<!-- b000149 | prose | pages [5] -->
In order to simplify the problem, the range of the repeater signal in the calculation of the ﬁrst question is always 20 km. Handheld two-way radios have a range of 2 km

<!-- b000150 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000151 | prose | pages [5] -->
in urban, forest and mountainous areas and 5 km elsewhere. This greatly simpliﬁes the calculation and will be further optimized in the third question.

<!-- b000152 | heading | pages [5] -->
Fires data processing

<!-- b000153 | prose | pages [5] -->
Combined with life experience we know that the spread of ﬁre presents a convex polygon, which is approximately estimated as a circle. The circumference of the jth ﬁre with latitude and longitude of (xj, yj) is dj(xj, yj), which yields:

<!-- b000154 | prose | pages [5] -->
• Radius: rj(xj, yj) = dj(xj,yj) ; 2π

<!-- b000155 | prose | pages [5] -->
• Area: Scircle,j(xj, yj) = π × r2 j(xj, yj).

<!-- b000156 | prose | pages [5] -->
We combine ﬁres that occurred on the same day and in close proximity into one ﬁre point.

<!-- b000157 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000158 | prose | pages [5] -->
Task 1: Optimal Numbers and Mix of Two Types of 3 Drones

<!-- b000159 | prose | pages [5] -->
In the model for determining the number and combination of drones, it is necessary to provide an evaluation standard for whether the ﬁre point needs drone rescue to improve rescue efﬁciency. To do this, we ﬁrst classify the ﬁres into different safety levels. On the basis of the known safety level of each area, we optimize the number and combination of drones based on maximum mix rate and minimum cost.

<!-- b000160 | prose | pages [5] -->
3.1

<!-- b000161 | heading | pages [5] -->
Area safety evaluation model

<!-- b000162 | prose | pages [5] -->
In order to assess the safety factor for dif- ferent areas of Victoria, the gridded map is shown in Figure 2. The longitude and lati- tude of each region are denoted by x, y, re- spectively. For different latitude and longi- tude (x, y) regions, we establish three eval- uation indicators: ﬁre frequency f(x, y), re- cent ﬁre situation situation(x, y), andﬁre size size(x,y) , which are used to measure the safety factor S(x, y). The safety coefﬁcients of the grid and the adjacent grid are scored to get the safety levels of the different grids on the map.

<!-- b000163 | prose | pages [5] -->
3.1.1 Indicators establishment

<!-- b000164 | prose | pages [5] -->
(1) Fire frequency f(x, y)

<!-- b000165 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000166 | caption | pages [5] -->
Figure 2: Map gridding schematic

<!-- b000167 | prose | pages [5] -->
In order to fully understand the ﬁre frequency when ﬁres are most severe in differ-关注数学模型

<!-- b000168 | furniture | pages [5] -->
2

<!-- b000169 | furniture | pages [5] -->
MATHmodels

<!-- b000170 | furniture | pages [5] -->
获取更多资讯

<!-- b000171 | furniture | pages [6] -->
Team # 2105363

<!-- b000172 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000173 | furniture | pages [6] -->
Page 6 of 25

<!-- b000174 | prose | pages [6] -->
ent areas, we need the maximum value of the daily ﬁre frequency at that location and explore it on different time scales to estimate that maximum value.

<!-- b000175 | prose | pages [6] -->
f(x, y) = max{u(ts, i, x, y)

<!-- b000176 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000177 | prose | pages [6] -->
where:

<!-- b000178 | prose | pages [6] -->
• ts is the time scale in days, ts ∈[1, 365];

<!-- b000179 | prose | pages [6] -->
}, (2)

<!-- b000180 | prose | pages [6] -->
ts

<!-- b000181 | prose | pages [6] -->
• i denotes the number of times, i ∈[1, ⌊365 ts ⌋];

<!-- b000182 | prose | pages [6] -->
• u(ts, i, x, y) = [number of ﬁres that occurred from day (1+(i−1)×ts) to day (1+ i × ts)]/ts (in place (x,y)), indicating the number of ﬁres that occurred in the ith

<!-- b000183 | prose | pages [6] -->
time scale.

<!-- b000184 | caption | pages [6] -->
Figure 3 shows a detailed illustration about the time scale.

<!-- b000185 | prose | pages [6] -->
𝑢(𝑡௦, 𝑖) is the number of fires that occurred during this period

<!-- b000186 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000187 | prose | pages [6] -->
𝑡௦

<!-- b000188 | prose | pages [6] -->
𝑖= 1 𝑖= 2

<!-- b000189 | prose | pages [6] -->
1

<!-- b000190 | prose | pages [6] -->
1 + 𝑡௦ 1 + 2𝑡௦

<!-- b000191 | prose | pages [6] -->
1 + (𝑖−1)𝑡௦

<!-- b000192 | prose | pages [6] -->
𝑖 𝑖

<!-- b000193 | prose | pages [6] -->
A year (365days)

<!-- b000194 | prose | pages [6] -->
1 + 𝑖ȉ 𝑡௦

<!-- b000195 | caption | pages [6] -->
Figure 3: Time scale diagram

<!-- b000196 | prose | pages [6] -->
(2) Recent ﬁre situation situation(x, y)

<!-- b000197 | prose | pages [6] -->
[2] we know that the "mini-weather zone" formed by smoke and

<!-- b000198 | prose | pages [6] -->
From the website

<!-- b000199 | prose | pages [6] -->
heat absorbing atmospheric moisture can continue to spread the ﬁre through the sparks and form new ignition sites, which is also known as "embers attack". In other words, the area where the ﬁre just broke out is more likely to reignite. during the period t0 (the time period corresponding to Figure 1 in the title, i.e., October 1, 2019 to January 7, 2020). We use t0 as the time criterion for determining the presence of recent ﬁres and the period for updating the safety level, making the following divisions.

<!-- b000200 | caption | pages [6] -->
Table 2: A three-way score table

<!-- b000201 | prose | pages [6] -->
Recent ﬁre situation

<!-- b000202 | prose | pages [6] -->
Burning Happened recently

<!-- b000203 | prose | pages [6] -->
Scores

<!-- b000204 | prose | pages [6] -->
3 2 Not happened recently

<!-- b000205 | prose | pages [6] -->
(3) Fire size size(x, y)

<!-- b000206 | prose | pages [6] -->
1

<!-- b000207 | prose | pages [6] -->
[1], we extract the circumference

<!-- b000208 | prose | pages [6] -->
Based on the data obtained from Active Fire Data

<!-- b000209 | prose | pages [6] -->
dj(x, y) for the jth ﬁre in the (x, y) region and obtain annual average size:

<!-- b000210 | prose | pages [6] -->
size(x, y) =

<!-- b000211 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000212 | prose | pages [6] -->
365

<!-- b000213 | prose | pages [6] -->
dj(x, y)

<!-- b000214 | prose | pages [6] -->
X

<!-- b000215 | prose | pages [6] -->
.

<!-- b000216 | prose | pages [6] -->
(3) 365

<!-- b000217 | prose | pages [6] -->
j=1

<!-- b000218 | prose | pages [6] -->
关注数学模型

<!-- b000219 | furniture | pages [6] -->
2

<!-- b000220 | furniture | pages [6] -->
MATHmodels

<!-- b000221 | furniture | pages [6] -->
获取更多资讯

<!-- b000222 | furniture | pages [7] -->
Team # 2105363

<!-- b000223 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000224 | furniture | pages [7] -->
Page 7 of 25

<!-- b000225 | prose | pages [7] -->
Safety factors S(x, y) and danger levels 3.1.2

<!-- b000226 | heading | pages [7] -->
1. Safety factors based on AHP AHP is a systematic and hierarchical multi-objective

<!-- b000227 | prose | pages [7] -->
comprehensive evaluation method. We build the importance matrix of S(x, y):

<!-- b000228 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000229 | prose | pages [7] -->


<!-- b000230 | prose | pages [7] -->
1 2 2 1

<!-- b000231 | prose | pages [7] -->


<!-- b000232 | prose | pages [7] -->
6 5

<!-- b000233 | prose | pages [7] -->


<!-- b000234 | prose | pages [7] -->
1/6 1/5

<!-- b000235 | prose | pages [7] -->
.

<!-- b000236 | prose | pages [7] -->
1

<!-- b000237 | prose | pages [7] -->
We take the average size of the ﬁre as the most important indicator, and the purpose is to make the area with a high safety factor correspond to a larger average size. The resulting ﬁre is more active or can develop into a more larger size, which is in line with the characteristics of the objects monitored by drones.

<!-- b000238 | prose | pages [7] -->
The consistency ratio is

<!-- b000239 | prose | pages [7] -->
CR = 0.0739,

<!-- b000240 | prose | pages [7] -->
which is less than 0.1, so the degree of inconsistency of S(x, y) is within the tolerance range. And it passes the consistency test.

<!-- b000241 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000242 | prose | pages [7] -->
In order to eliminate the differences in the different magnitudes, after normaliza- tion, we get:

<!-- b000243 | prose | pages [7] -->
S(x, y) = a1 × f(x, y) + a2 × situation(x, y) + a3 × size(x, y).

<!-- b000244 | prose | pages [7] -->
(4)

<!-- b000245 | prose | pages [7] -->
The result of Formula 4 is a1 = 0.1628, a2 = 0.1088, a3 = 0.7285.

<!-- b000246 | heading | pages [7] -->
2. Safety Assessment of the area:

<!-- b000247 | prose | pages [7] -->
When we consider whether a region is safe or not, in addition to the safety fac- tor S(x, y) for that region, for its neighboring regions is also of reference value. We convolve the nine safety factors with a convolution kernel

<!-- b000248 | prose | pages [7] -->


<!-- b000249 | prose | pages [7] -->
S(x −1, y + 1) S(x, y + 1)

<!-- b000250 | prose | pages [7] -->
S′(x, y) =

<!-- b000251 | prose | pages [7] -->
S(x −1, y) S(x, y)

<!-- b000252 | prose | pages [7] -->


<!-- b000253 | prose | pages [7] -->
S(x −1, y −1) S(x, y −1)

<!-- b000254 | prose | pages [7] -->


<!-- b000255 | prose | pages [7] -->


<!-- b000256 | prose | pages [7] -->


<!-- b000257 | prose | pages [7] -->
S(x + 1, y + 1)

<!-- b000258 | prose | pages [7] -->
0.05 0.05 0.05

<!-- b000259 | prose | pages [7] -->
⊗

<!-- b000260 | prose | pages [7] -->
S(x + 1, y)

<!-- b000261 | prose | pages [7] -->
0.05 0.6 0.05

<!-- b000262 | prose | pages [7] -->
.

<!-- b000263 | prose | pages [7] -->


<!-- b000264 | prose | pages [7] -->
S(x + 1, y −1)

<!-- b000265 | prose | pages [7] -->
0.05 0.05 0.05

<!-- b000266 | prose | pages [7] -->
While the safety factor is already a valuable indicator when considering the safety situation, it is clear that we cannot ignore the inﬂuence of topography for the Rapid Bushﬁre Response program. There are signiﬁcant differences in landscape from region to region. Therefore, ﬁres in forested and vegetated hills and mountains (collectively referred to as ﬂammable topography) are more likely to develop over time into ﬁres that are ﬁerce and difﬁcult to extinguish. And urban, desert, plains and other areas (collectively referred to as non-combustible topography) after the ﬁre is difﬁcult to further develop into a larger scale. Do the following division.

<!-- b000267 | caption | pages [7] -->
Table 3: Dangerous level classiﬁcation

<!-- b000268 | prose | pages [7] -->
Non-flammable topography

<!-- b000269 | prose | pages [7] -->
Safety factor Danger level

<!-- b000270 | prose | pages [7] -->
0 0.25 very safe

<!-- b000271 | prose | pages [7] -->
0.25 0.5 safe

<!-- b000272 | prose | pages [7] -->
0.5 0.75 general

<!-- b000273 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000274 | prose | pages [7] -->
0.75 1 dangerous

<!-- b000275 | prose | pages [7] -->
Flammable topography

<!-- b000276 | prose | pages [7] -->
Safety factor Danger level

<!-- b000277 | prose | pages [7] -->
0 0.25 safe

<!-- b000278 | prose | pages [7] -->
0.25 0.5 general

<!-- b000279 | prose | pages [7] -->
0.5 0.75 dangerous

<!-- b000280 | prose | pages [7] -->
0.75 1 high-risk 关注数学模型

<!-- b000281 | furniture | pages [7] -->
2

<!-- b000282 | furniture | pages [7] -->
MATHmodels

<!-- b000283 | furniture | pages [7] -->
获取更多资讯

<!-- b000284 | furniture | pages [8] -->
Team # 2105363

<!-- b000285 | prose | pages [8] -->
3.1.3

<!-- b000286 | heading | pages [8] -->
Result analyze of heat map

<!-- b000287 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000288 | furniture | pages [8] -->
Page 8 of 25

<!-- b000289 | prose | pages [8] -->
The map of different security levels is shown in Figure 4. The areas in different colors represent areas of different levels.

<!-- b000290 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000291 | prose | pages [8] -->
High-risk

<!-- b000292 | prose | pages [8] -->
Dangerous

<!-- b000293 | prose | pages [8] -->
General

<!-- b000294 | prose | pages [8] -->
Safe & very safe

<!-- b000295 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000296 | caption | pages [8] -->
Figure 4: Different danger levels on the Victoria map

<!-- b000297 | prose | pages [8] -->
As can be seen in Figure 4, central Victoria is safer, probably because it is at a low altitude and is not affected much by climate. There are many high-risk areas in the east, west and south, which is because these areas are very vegetated.

<!-- b000298 | prose | pages [8] -->
For SSA drones, it should maintain timely response capability to the high-risk area and have certain prevention capability to the dangerous area. Repeater drones, on the other hand, work with SSA drones to maintain communications and surveillance ac- tivities in high-risk areas, while reserving a certain number of radio-repeater drones for dangerous areas to support communications that may be established. In order to ensure the safety of the EOC, set the EOC to move freely in the safe area.

<!-- b000299 | prose | pages [8] -->
Optimization of the number and mix of drones 3.2

<!-- b000300 | prose | pages [8] -->
After dividing the gridded map into areas with different security levels, we dis- patch drones to implement emergency response or preventive deployment based on the security level of the ﬁre, demonstrating the advantages and disadvantages of the solution using capability and cost metrics. We evaluate the mix of the two types of drones and optimize the number of drones based on as much capability and as little cost as possible.

<!-- b000301 | prose | pages [8] -->
3.2.1 Maximum drone capability

<!-- b000302 | prose | pages [8] -->
The capability of the drone is reﬂected in two aspects: the response time of the high-risk area is as short as possible (response capability) and the response time of the dangerous area is as reasonable as possible (prevention capability). There are M high-risk areas and N precautionary areas in the statistics. These two capabilities are analyzed separately below.

<!-- b000303 | prose | pages [8] -->
• Response capability

<!-- b000304 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000305 | prose | pages [8] -->
关注数学模型

<!-- b000306 | furniture | pages [8] -->
2

<!-- b000307 | furniture | pages [8] -->
MATHmodels

<!-- b000308 | furniture | pages [8] -->
获取更多资讯

<!-- b000309 | furniture | pages [9] -->
Team # 2105363

<!-- b000310 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000311 | furniture | pages [9] -->
Page 9 of 25

<!-- b000312 | prose | pages [9] -->
We consider the ith EOC to be responsible for communication and surveillance. the role of the EOC is to direct the SSA drone to reach the high risk area from a location closer to the ith high risk area in a safer area, such that the average response time tavg is minimized.

<!-- b000313 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000314 | prose | pages [9] -->
tavg =

<!-- b000315 | prose | pages [9] -->
ti =

<!-- b000316 | prose | pages [9] -->
M

<!-- b000317 | prose | pages [9] -->
ti

<!-- b000318 | prose | pages [9] -->
X

<!-- b000319 | prose | pages [9] -->
M ,

<!-- b000320 | prose | pages [9] -->
i=1

<!-- b000321 | prose | pages [9] -->
xi

<!-- b000322 | prose | pages [9] -->
.

<!-- b000323 | prose | pages [9] -->
vmax

<!-- b000324 | prose | pages [9] -->
To ensure that the drone can travel back to,

<!-- b000325 | prose | pages [9] -->
xi < 0.5 × V oyage(vmax).

<!-- b000326 | prose | pages [9] -->
(5)

<!-- b000327 | prose | pages [9] -->
xi is the distance between the EOC and the high-risk area, and ti is the time the aircraft ﬂies in the process. In order to maximize the response capability of the drone, tavg should be as small as possible. Therefore, we make the EOC located at the nearest

<!-- b000328 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000329 | prose | pages [9] -->
point to the ith high-risk area in the safer region.

<!-- b000330 | prose | pages [9] -->
• Prevention capability

<!-- b000331 | prose | pages [9] -->
We conﬁgure a certain number of SSA drones in the dangerous area, so that when the EOC is movable, we can ensure that there are SSA drones or EOCs in the dangerous area at regular intervals to check whether there are ﬁres. Prepare a certain number of drones, the more the number, the better the ability to prevent, see Section 3.2.3 for quantiﬁcation.

<!-- b000332 | prose | pages [9] -->
3.2.2 Minimal drone costs

<!-- b000333 | prose | pages [9] -->
We calculate the total cost of the two drones and their number separately. Let the number of SSA drones be m and the number of Radio Repeater drones be n. The calculation is as follows.

<!-- b000334 | prose | pages [9] -->
Cost(drone) = m × Cost(SSA drone) + n × Cost(radio repeater drone), (6)

<!-- b000335 | prose | pages [9] -->
where Cost(SSA drone) = SSA drones’ HD camera cost+ remote sensing camera cost+ drone cost, Cost(radio repeater drone) = repeater cost+ Radio Repeater drones’ cost. So we want

<!-- b000336 | prose | pages [9] -->
min{Cost(SSA drone).}

<!-- b000337 | prose | pages [9] -->
3.2.3 Number and mix of drones

<!-- b000338 | prose | pages [9] -->
(7)

<!-- b000339 | prose | pages [9] -->
The m, n are the number of SSA drones and radio-repeater drones, respectively. We determine the number of SSA drones from the demand of the ﬁre scene and the round system, then determine the number of radio repeater drones by the combination relationship between SSA drones and radio repeater drones, and ﬁnally prepare some drones to prevent dangerous area.

<!-- b000340 | heading | pages [9] -->
1. Number of SSA drones

<!-- b000341 | prose | pages [9] -->
For SSA drones, because SSA drones monitor the ﬁre scene directly, the mixed re- lationship with the radio-repeater drones does not change their utilization rate in the关注数学模型

<!-- b000342 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000343 | furniture | pages [9] -->
2

<!-- b000344 | furniture | pages [9] -->
MATHmodels

<!-- b000345 | furniture | pages [9] -->
获取更多资讯

<!-- b000346 | furniture | pages [10] -->
Team # 2105363

<!-- b000347 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000348 | furniture | pages [10] -->
Page 10 of 25

<!-- b000349 | prose | pages [10] -->
ﬁre now, so it is sufﬁcient to calculate the number of SSA drones directly according to the ﬁre demand.

<!-- b000350 | prose | pages [10] -->
(1) For high-risk areas

<!-- b000351 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000352 | prose | pages [10] -->
Let the longitude and latitude of the jth high-risk area be (x′

<!-- b000353 | prose | pages [10] -->
j, y′

<!-- b000354 | prose | pages [10] -->
j), and ﬁnd the num- ber of SSA drones needed to scan the jth high-risk area.

<!-- b000355 | prose | pages [10] -->
Fires that need to maintain a timely response are very active, large and mostly in terrain that is prone to further expansion.

<!-- b000356 | prose | pages [10] -->
Top view

<!-- b000357 | prose | pages [10] -->
𝑣୫ୟ୶× 𝑡

<!-- b000358 | prose | pages [10] -->
𝑟

<!-- b000359 | prose | pages [10] -->
𝑟

<!-- b000360 | prose | pages [10] -->
Side view

<!-- b000361 | prose | pages [10] -->
𝜃= 40°

<!-- b000362 | prose | pages [10] -->
𝜃

<!-- b000363 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000364 | prose | pages [10] -->
𝑟

<!-- b000365 | prose | pages [10] -->
𝑟

<!-- b000366 | prose | pages [10] -->
Scanning acreage

<!-- b000367 | prose | pages [10] -->
ℎ= 300𝑚

<!-- b000368 | prose | pages [10] -->
𝑟

<!-- b000369 | prose | pages [10] -->
𝑟

<!-- b000370 | caption | pages [10] -->
Figure 5: SSA drones surveillance schematic

<!-- b000371 | prose | pages [10] -->
To ensure ﬁreﬁghting efﬁciency, SSA drones on scene should assure that they can complete scanning surveillance of the entire scene area within half a minute. The scan radius can be obtained from Figure 5.

<!-- b000372 | prose | pages [10] -->
S′

<!-- b000373 | prose | pages [10] -->
circle,j πr2 + 2r · vmax × 30 seconds.

<!-- b000374 | prose | pages [10] -->
m1,j =

<!-- b000375 | prose | pages [10] -->
(8)

<!-- b000376 | prose | pages [10] -->
SSA drones have constant round trips and recharges, and there are handoffs. So the number of SSA required for the jth high-risk area is the product of the number of handoffs and the number of SSA drones required at the same time.

<!-- b000377 | prose | pages [10] -->
2¯xi v + recharge time

<!-- b000378 | prose | pages [10] -->
m2,j = m1,j ·

<!-- b000379 | prose | pages [10] -->
, (9)

<!-- b000380 | prose | pages [10] -->
−xj

<!-- b000381 | prose | pages [10] -->
V oyage(v)

<!-- b000382 | prose | pages [10] -->
v

<!-- b000383 | prose | pages [10] -->
v

<!-- b000384 | prose | pages [10] -->
where the biggest fractional equation in Formula (9) represents the rounds of the drone, which is obtained by the quotient of the time returning from the disaster area to recharge and arriving at the disaster area again and the time spent in the disaster area.

<!-- b000385 | prose | pages [10] -->
(2) For dangerous areas

<!-- b000386 | prose | pages [10] -->
For the ith dangerous area, the number of SSA drones should reach a certain thresh- old in order to check for ﬁres in these areas, such that even in the worst case scenario (i.e., when all dangerous areas are on ﬁre), the number of SSA drones in reserve is suf- ﬁcient to dispatch one SSA drone for each hazard area for temporary surveillance and situational awareness. Thus there is a total number of SSAs:

<!-- b000387 | prose | pages [10] -->
M X

<!-- b000388 | prose | pages [10] -->
m2,j + N × (1 + ϕ),

<!-- b000389 | prose | pages [10] -->
m =

<!-- b000390 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000391 | prose | pages [10] -->
i=1

<!-- b000392 | prose | pages [10] -->
(10)

<!-- b000393 | prose | pages [10] -->
关注数学模型

<!-- b000394 | furniture | pages [10] -->
2

<!-- b000395 | furniture | pages [10] -->
MATHmodels

<!-- b000396 | furniture | pages [10] -->
获取更多资讯

<!-- b000397 | furniture | pages [11] -->
Team # 2105363

<!-- b000398 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000399 | furniture | pages [11] -->
Page 11 of 25

<!-- b000400 | prose | pages [11] -->
where ϕ is loss rate. Considering the attrition of reserve drones, we prepare some additional drones to cope with this attrition. ϕ is the number of extra prepared drones divided by the number of dangerous area drones.

<!-- b000401 | heading | pages [11] -->
2. Mix of Radio Repeater drones

<!-- b000402 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000403 | prose | pages [11] -->
For the radio-repeater drones, consider its combination with the SSA drones, so that each radio-repeater drone can receive as many signals as possible and forward more signals to determine the best number , optimize utilization.

<!-- b000404 | heading | pages [11] -->
(1) Greedy and multiplexing based solution algorithms

<!-- b000405 | prose | pages [11] -->
Using a greedy algorithm, the solution that allows each radio repeater drone to reuse the maximum number of SSA drones is planned, and the minimum number of radio repeater drones, n, is output.

<!-- b000406 | prose | pages [11] -->
The idea of the algorithm is to ﬁnd candidate locations of radio repeater drones that can be multiplexed. Starting from the candidate location with the most multiplex- ing, a radio repeater drone is determined to be placed at that location, while removing

<!-- b000407 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000408 | prose | pages [11] -->
the SSA drones in high-risk areas that can use that repeater drone to send and receive signals. Then candidate locations with the second highest reuse rate is identiﬁed. Con- tinue this process until all high-risk areas are taken care of by the repeater.

<!-- b000409 | prose | pages [11] -->
Given the meaning of some symbols:

<!-- b000410 | prose | pages [11] -->
• n1, n2 are the number of prepared radio-repeater drones and the number of radio- repeater drones responding to the high-risk area, respectively. When calculating n1, the input n is n1, so does n2.

<!-- b000411 | prose | pages [11] -->
• mi is the number of SSA drones in ith.

<!-- b000412 | prose | pages [11] -->
• U is the number of corresponding areas when considering high-risk or dangerous areas.

<!-- b000413 | prose | pages [11] -->
• Rradio = 2km and Rrepeater = 20km are the ranges of the handheld two-way radios and repeaters, respectively.

<!-- b000414 | prose | pages [11] -->
• SCi is the candidate range of radio repeater drone for the ith high-risk area, SC = {SC1, SC2, · · · , SCM}.

<!-- b000415 | prose | pages [11] -->
• SRi is the number of radio repeater drones multiplexed corresponding to the ith high-risk area (other high-risk areas use this repeater at the same time), equal to 1 means that this radio repeater drone is only responsible for the signal transceiver in this high-risk area. SR = {SR1, SR2, · · · , SRM}.

<!-- b000416 | prose | pages [11] -->
• SNj is the reuse number of the radio repeater drones corresponding to the jth

<!-- b000417 | prose | pages [11] -->
high-risk region. If another high-risk area multiplexes this repeater, the serial number of this high-risk area is an element of the set SN. SN = {SN1, SN2, · · · , SNM}

<!-- b000418 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000419 | prose | pages [11] -->
关注数学模型

<!-- b000420 | furniture | pages [11] -->
2

<!-- b000421 | furniture | pages [11] -->
MATHmodels

<!-- b000422 | furniture | pages [11] -->
获取更多资讯

<!-- b000423 | furniture | pages [12] -->
Team # 2105363

<!-- b000424 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000425 | furniture | pages [12] -->
Page 12 of 25

<!-- b000426 | heading | pages [12] -->
Algorithm: Radio Repeater drones number solving algorithm

<!-- b000427 | prose | pages [12] -->
Input: xi, Rradio, Rrepeater, n = 0 Output: n

<!-- b000428 | heading | pages [12] -->
1 for i = 1; i ⩽U; i + + do

<!-- b000429 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000430 | prose | pages [12] -->
if xi > Rradio then 2

<!-- b000431 | prose | pages [12] -->
take the ith high-risk area as the center and Rradio as the radius to 3

<!-- b000432 | prose | pages [12] -->
make a circle O1;

<!-- b000433 | prose | pages [12] -->
take the ith EOC as the center and Rrepeater as the radius to make 4

<!-- b000434 | prose | pages [12] -->
a circle O2;

<!-- b000435 | prose | pages [12] -->
SCi = O1 ∩O2; 5

<!-- b000436 | prose | pages [12] -->
SRi = 1; 6

<!-- b000437 | heading | pages [12] -->
7 for i = 1; i ⩽U; i + + do

<!-- b000438 | prose | pages [12] -->
for j = 1; j ⩽U; j + + do 8

<!-- b000439 | prose | pages [12] -->
if SCi ∩SCj̸ = ∅and i̸ = j then 9

<!-- b000440 | prose | pages [12] -->
SRi = SRi + mj; 10

<!-- b000441 | prose | pages [12] -->
SCi = SCi ∩SCj;

<!-- b000442 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000443 | prose | pages [12] -->
11

<!-- b000444 | prose | pages [12] -->
SNi = SNi ∪{j}; 12

<!-- b000445 | heading | pages [12] -->
13 while SR1 + SR2 + · · · + SRU = 0 do

<!-- b000446 | prose | pages [12] -->
SRk = max{SR}, k is the maximum value’s serial number in SR; 14

<!-- b000447 | prose | pages [12] -->
n = n + 1; 15

<!-- b000448 | prose | pages [12] -->
for i = 1; i ⩽U; i + + do 16

<!-- b000449 | prose | pages [12] -->
if k ∈SNi then 17

<!-- b000450 | prose | pages [12] -->
SNi = ∅; 18

<!-- b000451 | prose | pages [12] -->
SRi = 0; 19

<!-- b000452 | prose | pages [12] -->
n Using the reuse rate: m

<!-- b000453 | prose | pages [12] -->
(2) Maximize the reuse rate m

<!-- b000454 | prose | pages [12] -->
n indicates the mix relationship of drone conﬁguration, the larger this indicator is the better the mix relationship of two drones. Then we have:

<!-- b000455 | prose | pages [12] -->
max{m

<!-- b000456 | prose | pages [12] -->
n }.

<!-- b000457 | prose | pages [12] -->
(11)

<!-- b000458 | prose | pages [12] -->
(3) Continuous supply to high-risk areas

<!-- b000459 | prose | pages [12] -->
Considering the process of repeater drone round trip and charging, there is hand- offs, so it is necessary to get the number of repeater drones that respond to high risk areas:

<!-- b000460 | prose | pages [12] -->
2¯xi v + recharge time

<!-- b000461 | prose | pages [12] -->
n′

<!-- b000462 | prose | pages [12] -->
1 = n1 ×

<!-- b000463 | prose | pages [12] -->
ditto,

<!-- b000464 | prose | pages [12] -->
,

<!-- b000465 | prose | pages [12] -->
V oyage(v)

<!-- b000466 | prose | pages [12] -->
−¯xi v

<!-- b000467 | prose | pages [12] -->
v

<!-- b000468 | prose | pages [12] -->
3.3 ⩽v ⩽10,

<!-- b000469 | prose | pages [12] -->
V oyage(v) > 2 × max(xj).

<!-- b000470 | prose | pages [12] -->
So the total number of repeater drones:

<!-- b000471 | prose | pages [12] -->
n = n′

<!-- b000472 | prose | pages [12] -->
1 + n2, (12)

<!-- b000473 | prose | pages [12] -->
where n2 is radio repeater drones that dangerous areas need.

<!-- b000474 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000475 | prose | pages [12] -->
关注数学模型

<!-- b000476 | furniture | pages [12] -->
2

<!-- b000477 | furniture | pages [12] -->
MATHmodels

<!-- b000478 | furniture | pages [12] -->
获取更多资讯

<!-- b000479 | furniture | pages [13] -->
Team # 2105363

<!-- b000480 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000481 | furniture | pages [13] -->
Page 13 of 25

<!-- b000482 | heading | pages [13] -->
Optimization model with maximum mix rate and minimum cost

<!-- b000483 | prose | pages [13] -->
3.3

<!-- b000484 | prose | pages [13] -->
Combining all the above, λ is introduced to reﬂect the priority of the drone capabil- ity indicators. The larger λ is, the higher the priority of the capability indicators in the

<!-- b000485 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000486 | prose | pages [13] -->
drone conﬁguration scheme obtained from the planning. The ﬁnal model is:

<!-- b000487 | prose | pages [13] -->
min{( n

<!-- b000488 | prose | pages [13] -->
m)λ × Cost(drone)(1−λ)},

<!-- b000489 | prose | pages [13] -->
n = n′

<!-- b000490 | prose | pages [13] -->
  

<!-- b000491 | prose | pages [13] -->
1 + n2 0 ⩽ϕ ⩽1

<!-- b000492 | prose | pages [13] -->
 

<!-- b000493 | prose | pages [13] -->
s.t.

<!-- b000494 | prose | pages [13] -->
.

<!-- b000495 | prose | pages [13] -->
0 ⩽λ ⩽13.3 ⩽v ⩽10

<!-- b000496 | prose | pages [13] -->
  

<!-- b000497 | prose | pages [13] -->
V oyage(v) > 2 × max{xj}

<!-- b000498 | prose | pages [13] -->


<!-- b000499 | prose | pages [13] -->
3.3.1

<!-- b000500 | heading | pages [13] -->
Result Analysis

<!-- b000501 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000502 | prose | pages [13] -->
The result of the optimization model with maximum drone capability and mini- mum cost are shown in Figure 6.

<!-- b000503 | prose | pages [13] -->
Cost(drone)

<!-- b000504 | prose | pages [13] -->
Pareto front

<!-- b000505 | prose | pages [13] -->
Choose the relatively optimal solution for the two objective functions in this area.

<!-- b000506 | prose | pages [13] -->
n n m m

<!-- b000507 | caption | pages [13] -->
Figure 6: The results of the optimization model

<!-- b000508 | prose | pages [13] -->
As shown in the Figure 6, the inverse of m

<!-- b000509 | prose | pages [13] -->
n shows an inverse relationship with the cost of the drone, which indicates that our bi-objective optimization is effective. We intercept the middle section of the interval as the solution space, and we can choose a non-inferior solution in the left half of the interval when we prefer the combination rate to be optimal, and in the right half of the interval when we prefer the cost to be minimal.

<!-- b000510 | heading | pages [13] -->
Task 2: Adaptation of Model and Cost Increases for

<!-- b000511 | prose | pages [13] -->
4 Equipment

<!-- b000512 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000513 | prose | pages [13] -->
关注数学模型 For simplicity, we make the following two assumptions:

<!-- b000514 | furniture | pages [13] -->
2

<!-- b000515 | furniture | pages [13] -->
MATHmodels

<!-- b000516 | furniture | pages [13] -->
获取更多资讯

<!-- b000517 | furniture | pages [14] -->
Team # 2105363

<!-- b000518 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000519 | furniture | pages [14] -->
Page 14 of 25

<!-- b000520 | prose | pages [14] -->
• The topography of Australia will not change dramatically in the next ten years (not considering changes in topography caused by unavoidable factors such as earthquakes). • The probability of ﬁre occurrence in different hazard areas is independent of each

<!-- b000521 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000522 | prose | pages [14] -->
other.

<!-- b000523 | heading | pages [14] -->
Ternary commensurable ﬁre prediction model

<!-- b000524 | prose | pages [14] -->
4.1

<!-- b000525 | prose | pages [14] -->
4.1.1

<!-- b000526 | heading | pages [14] -->
Model building process

<!-- b000527 | prose | pages [14] -->
Since the terrain does not change dramatically over the course of a decade, the main task of predicting ﬁre is when extreme ﬁre conditions will occur, what the probability of occurrence is, and what the amount of equipment prepared to respond to ﬁres of different sizes is. We obtained data on extreme ﬁre conditions in Victoria over the last

<!-- b000528 | prose | pages [14] -->
[5], and used this as the

<!-- b000529 | prose | pages [14] -->
few decades by referring to List of major bushﬁres in Australia

<!-- b000530 | prose | pages [14] -->
basis for our predictions.

<!-- b000531 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000532 | prose | pages [14] -->
The commensurable prediction model is a method of forecasting special events based on special events, and he bases his forecasting on the universal existence of com- mensurability of events, which is a generalized periodicity. Commensurability is a law that is common to all elements of a system and reﬂects the occurrence of special events

<!-- b000533 | prose | pages [14] -->
[6].

<!-- b000534 | prose | pages [14] -->
(small probability events) in nature

<!-- b000535 | heading | pages [14] -->
1. The general commensurable prediction model is:

<!-- b000536 | prose | pages [14] -->
Xi+1 =

<!-- b000537 | prose | pages [14] -->
l l X

<!-- b000538 | prose | pages [14] -->
IjXj,

<!-- b000539 | prose | pages [14] -->
j=1

<!-- b000540 | prose | pages [14] -->
where X is entered in chronological order for the past years in which extreme ﬁre events occurred to obtain X = {X1, X2, ..., X17} in the sequence.. {j} ∈{i}, that is, j is an element of the set i. Ij is an integer.

<!-- b000541 | heading | pages [14] -->
2. In order to get the optimal results, the ternary commensurable prediction model

<!-- b000542 | prose | pages [14] -->
[7]. And the formula is:

<!-- b000543 | prose | pages [14] -->
with the best results in general is selected

<!-- b000544 | prose | pages [14] -->
Xa + Xb −Xc = Xu(a,b,c),

<!-- b000545 | prose | pages [14] -->
where a, b, c, d, e, f, g = 1, 2, · · · , n, u, v, w = 1, 2, · · · , m.

<!-- b000546 | heading | pages [14] -->
3. Enumerate the equations that match the above relationship by enumeration, and

<!-- b000547 | prose | pages [14] -->
process the sequence numbers to obtain a vector

<!-- b000548 | prose | pages [14] -->
V = (b −a, c −b, u −c,′ +′,′ −′),

<!-- b000549 | prose | pages [14] -->
which means the difference between the serial numbers of the ﬁrst two years, the differ- ence between the serial numbers of the second and third years, the difference between the serial numbers of the third and fourth years, the sign before the second year, and the sign before the third year.

<!-- b000550 | prose | pages [14] -->
Find among all vectors the vectors that exist identical to itself and obtain the multi- set ternary commensurable forecast formula:

<!-- b000551 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000552 | prose | pages [14] -->
关注数学模型 i = 1, 2, · · · , XiV4Xi+V 1V5Xi+V1+V2 = Xi+V1+V2+V3

<!-- b000553 | furniture | pages [14] -->
2

<!-- b000554 | furniture | pages [14] -->
MATHmodels

<!-- b000555 | furniture | pages [14] -->
获取更多资讯

<!-- b000556 | furniture | pages [15] -->
Team # 2105363

<!-- b000557 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000558 | furniture | pages [15] -->
Page 15 of 25

<!-- b000559 | prose | pages [15] -->
let the term with the largest ordinal number in the forecast equation be X18, and the forecast value for multiple years corresponding to X18 can be calculated.

<!-- b000560 | heading | pages [15] -->
4. We sort the past year series and the forecasted year series from left to right by

<!-- b000561 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000562 | prose | pages [15] -->
serial number, enumerate four years from all of them, ﬁnd the ternary commensurable forecast formula they match, and connect them two by two with their differences to get the butterﬂy diagram.

<!-- b000563 | prose | pages [15] -->
Δ = 17 Δ = 17(18) Δ = 17 Δ = 17 Δ = 17 Δ = 17(18) Δ =17(18)

<!-- b000564 | prose | pages [15] -->
1983 1985 1851 1898 1926 1939 1944 1951 1965 1977

<!-- b000565 | prose | pages [15] -->
𝚫= 9(8)

<!-- b000566 | prose | pages [15] -->
Years not used in the forecast

<!-- b000567 | prose | pages [15] -->
1997 2003 2006 2007 2009 2014 2020 2023

<!-- b000568 | prose | pages [15] -->
𝚫= 9(8) 𝚫= 9 𝚫= 9

<!-- b000569 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000570 | prose | pages [15] -->
Δ = 3 Δ = 3(4) Δ = 3 Δ = 3(2)

<!-- b000571 | prose | pages [15] -->
Two Years with difference of 17

<!-- b000572 | prose | pages [15] -->
Two Years with difference of 9

<!-- b000573 | prose | pages [15] -->
Two Years with difference of 3

<!-- b000574 | prose | pages [15] -->
Δ = 3

<!-- b000575 | caption | pages [15] -->
Figure 7: Butterﬂy structure diagram

<!-- b000576 | prose | pages [15] -->
According to the K. Pearson-Fisher theorem, Figure 7 satisﬁes the butterﬂy struc- ture probability reference criterion. It reﬂects the most important quasi-cycles since 1851 as 3, 9, 17a, with 17a being the most typical, occurring seven times.

<!-- b000577 | heading | pages [15] -->
5. Count statistically the total number of extreme ﬁres used to predict the ith extreme

<!-- b000578 | prose | pages [15] -->
ﬁre situation as ni, and the number of extreme ﬁres participating in the prediction of the ith extreme ﬁre case is mi, then the probability of the ith extreme ﬁre event is

<!-- b000579 | prose | pages [15] -->
P(ith extreme ﬁre occur) = mi

<!-- b000580 | prose | pages [15] -->
,

<!-- b000581 | prose | pages [15] -->
ni

<!-- b000582 | prose | pages [15] -->
and mi can be seen by butterﬂy structure diagram clearly.

<!-- b000583 | prose | pages [15] -->
For example, our predicted year for the next extreme ﬁre is 2023, which is involved in all three cycles, and the number of years involved in the prediction is 16. The prob- ability of the event prediction is P = m/n = 16/17 = 94.12%, which is the probability of an extreme severe ﬁre in 2023.

<!-- b000584 | heading | pages [15] -->
6. We use the ﬁre acreage in the data to indicate the severity of extreme ﬁre condi-

<!-- b000585 | prose | pages [15] -->
tions Sdanger, and similarly the ﬁre scale can be predicted by the ternary commensurable prediction model.

<!-- b000586 | heading | pages [15] -->
7. Test the predicted values and calculate the relative residuals:

<!-- b000587 | prose | pages [15] -->
ε(k) = x(0)(k) −ˆx(0)(k)

<!-- b000588 | prose | pages [15] -->
x(0)(k) , k = 1, 2, . . . , n.

<!-- b000589 | prose | pages [15] -->
If for all ε|(k)| < 0.1, the higher requirement is considered to be reached; otherwise, if for all |ε(k)| < 0.2, the general requirement is considered to be reached.

<!-- b000590 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000591 | prose | pages [15] -->
关注数学模型

<!-- b000592 | furniture | pages [15] -->
2

<!-- b000593 | furniture | pages [15] -->
MATHmodels

<!-- b000594 | furniture | pages [15] -->
获取更多资讯

<!-- b000595 | furniture | pages [16] -->
Team # 2105363

<!-- b000596 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000597 | furniture | pages [16] -->
Page 16 of 25

<!-- b000598 | heading | pages [16] -->
Result of ternary commensurable ﬁre prediction model

<!-- b000599 | prose | pages [16] -->
4.1.2

<!-- b000600 | heading | pages [16] -->
1. Table of predicted years and residual test

<!-- b000601 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000602 | caption | pages [16] -->
Table 4: Table of predicted years

<!-- b000603 | prose | pages [16] -->
Years Probability

<!-- b000604 | prose | pages [16] -->
2022 64.71% 2023 94.12% 2024 52.94% 2027 41.18%

<!-- b000605 | prose | pages [16] -->
Residual Residual change

<!-- b000606 | prose | pages [16] -->
53 2.62% 54 2.67% 55 2.72% 58 2.86%

<!-- b000607 | caption | pages [16] -->
Table 4 shows our predictions for the four possible years of extreme severity ﬁres

<!-- b000608 | prose | pages [16] -->
and the corresponding probabilities of it. The fourth column shows that the residual change in the occurrence of extreme ﬁres for all four years is around 2%, which is less

<!-- b000609 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000610 | prose | pages [16] -->
than 5%. This indicates that our predictions have a strong accuracy.

<!-- b000611 | heading | pages [16] -->
2. Pie map of predicted relative index

<!-- b000612 | caption | pages [16] -->
Figure 8: Pie map of predicted relative index

<!-- b000613 | prose | pages [16] -->
Based on the commensurable model, we predict the relative index of severity that would result from the next extreme severity ﬁre when it occurred. As shown in Figure 8, the next extreme severity ﬁre is most likely to produce a ﬁre with a severity index of 0-50. Also, ﬁres with larger severity indices have a high likelihood, accounting for more than half of the likelihood. Therefore, in order to meet future emergency response needs for large ﬁres, we may need to increase the number of drones or "Boots-on-the- ground" Forward Teams.

<!-- b000614 | prose | pages [16] -->
4.2 Increased Equipment Costs

<!-- b000615 | prose | pages [16] -->
After predicting the ﬁre, to accommodate changes in the likelihood of extreme ﬁre events over the next decade, we increase the equipment conﬁguration of the EOC and "boots-on-the-ground" ﬁreﬁghters for extreme ﬁre events only, getting the increased equipment costs.

<!-- b000616 | prose | pages [16] -->
Equipment includes handheld radios for the "boots-on-the-ground" teams, wear-

<!-- b000617 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000618 | prose | pages [16] -->
able devices, and two-way radios for the EOC. From a safety perspective, we assume关注数学模型

<!-- b000619 | furniture | pages [16] -->
2

<!-- b000620 | furniture | pages [16] -->
MATHmodels

<!-- b000621 | furniture | pages [16] -->
获取更多资讯

<!-- b000622 | furniture | pages [17] -->
Team # 2105363

<!-- b000623 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000624 | furniture | pages [17] -->
Page 17 of 25

<!-- b000625 | prose | pages [17] -->
that each "boots on the ground" squad ﬁreﬁghter has one handheld radio and one set of wearables, and that each EOC has one two-way radio for surveillance and commu- nications and one two-way radio for backup.

<!-- b000626 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000627 | prose | pages [17] -->
Additional equipment costs for EOCs Cost(EOC) 4.2.1

<!-- b000628 | prose | pages [17] -->
When extreme ﬁres occur, the drone needs the appropriate EOC to support commu- nication and surveillance. Find the expected value E(number, extreme) of the number of extreme ﬁres that have a probability of occurring in the next ten years, which is equal to the sum of the probabilities of occurrence in the ﬁre prediction model.

<!-- b000629 | prose | pages [17] -->
N X

<!-- b000630 | prose | pages [17] -->
P(ﬁres in i areas) · P(no ﬁres in N −i areas) · i,

<!-- b000631 | prose | pages [17] -->
E(number, extreme) =

<!-- b000632 | prose | pages [17] -->
i=1

<!-- b000633 | prose | pages [17] -->
where P denotes the probability.

<!-- b000634 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000635 | prose | pages [17] -->
From Task 1, we know that the number of EOCs responsible for extreme ﬁres is equal to the number of extreme ﬁres. So the cost of the additional equipment for the EOC is calculated as

<!-- b000636 | prose | pages [17] -->
Cost(EOC) = 2 × E(number, extreme) · Cost(radio).

<!-- b000637 | prose | pages [17] -->
(13)

<!-- b000638 | prose | pages [17] -->
Additional equipment costs for ﬁreﬁghters Cost(ﬁreﬁghter) 4.2.2

<!-- b000639 | prose | pages [17] -->
The number of "boots on the ground" teams on each attendance is determined by the EOC after considering the severity of the ﬁre. The probability model for the ﬁre department to handle an extreme ﬁre event is established, and the probability of suc- cessful response to the ﬁre is estimated based on the number of team members Numi and the severity Sdanger,i in ith extreme ﬁre event.

<!-- b000640 | prose | pages [17] -->
Combined with the actual situation, the more serious the ﬁre, the smaller the pos- sibility of "boots-on-the-ground" squad to put out the ﬁre, while the more the number of squad, the greater the ability to deal with the ﬁre. This change in the relationship should be the ﬁrst slow then fast and ﬁnally slow trend, so the sigmoid function is selected to ﬁt.

<!-- b000641 | prose | pages [17] -->
P(success, i) = 1 Sdanger,i + C), (14) Numi 1 + exp(−

<!-- b000642 | prose | pages [17] -->
where i ∈[1, E(number, extreme)] and C is a constant, from the article Brief introduction

<!-- b000643 | prose | pages [17] -->
[3], it is known that the average number of Polish ﬁre de-

<!-- b000644 | prose | pages [17] -->
of Polish volunteer ﬁre brigade

<!-- b000645 | prose | pages [17] -->
partment is 24, we can use Fnumber,i = 24, Sdanger,i = average of Sdanger when the success rate is 0.8 to estimate C.

<!-- b000646 | prose | pages [17] -->
The EOC should ensure that the success rate of each team’s rescue is above 80% when making decisions. Substitute Sdanger,i, calculate the number of team members Pnumber,i for the ith extreme ﬁre with a success rate of exactly 0.8. And utilize the expected value of the increase in the number of "boots-on-the-ground" ﬁreﬁghters to estimate the number of increases needed.

<!-- b000647 | prose | pages [17] -->
M

<!-- b000648 | prose | pages [17] -->
P(Numi) · P(ith extreme ﬁre occur).

<!-- b000649 | prose | pages [17] -->
X

<!-- b000650 | prose | pages [17] -->
E(Numi) =

<!-- b000651 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000652 | prose | pages [17] -->
i=1

<!-- b000653 | prose | pages [17] -->
关注数学模型

<!-- b000654 | furniture | pages [17] -->
2

<!-- b000655 | furniture | pages [17] -->
MATHmodels

<!-- b000656 | furniture | pages [17] -->
获取更多资讯

<!-- b000657 | furniture | pages [18] -->
Team # 2105363

<!-- b000658 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000659 | furniture | pages [18] -->
Page 18 of 25

<!-- b000660 | prose | pages [18] -->
The cost of additional equipment for ﬁreﬁghters of "boots on the ground" is:

<!-- b000661 | prose | pages [18] -->
Cost(ﬁreﬁghter) = E(Numi) · (Cost(radio) + Cost(wearable device)).

<!-- b000662 | prose | pages [18] -->
(15)

<!-- b000663 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000664 | prose | pages [18] -->
4.2.3

<!-- b000665 | heading | pages [18] -->
Results of additional equipment

<!-- b000666 | prose | pages [18] -->
Equipment

<!-- b000667 | prose | pages [18] -->
EOC radios

<!-- b000668 | prose | pages [18] -->
“Boots-on-the-ground” handheld radios

<!-- b000669 | prose | pages [18] -->
“Boots-on-the-ground” team wearable

<!-- b000670 | prose | pages [18] -->
equipment

<!-- b000671 | prose | pages [18] -->
Number Single price Total price

<!-- b000672 | prose | pages [18] -->
5 92.725 463.625

<!-- b000673 | prose | pages [18] -->
1,800 19 94.741

<!-- b000674 | prose | pages [18] -->
2,688.625 19 141.507

<!-- b000675 | caption | pages [18] -->
Figure 9: Number of additional equipment

<!-- b000676 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000677 | prose | pages [18] -->
Task 3: Location Optimization 5

<!-- b000678 | prose | pages [18] -->
In the greedy and multiplexing based solution algorithms of Task 1, we have ob- tained the ideal distribution range of each repeater drone. Based on this, we consider the signal loss and safety of the repeater drone to optimize its optimal position in the ideal distribution range.

<!-- b000679 | prose | pages [18] -->
5.1

<!-- b000680 | heading | pages [18] -->
Signal loss model

<!-- b000681 | prose | pages [18] -->
SPM model is suitable for propagation loss prediction for distances from 1 to 20 km and frequencies from 150 to 3500 MHz, running GSM and other communication systems. This model takes the feature classiﬁcation map and effective antenna height

<!-- b000682 | prose | pages [18] -->
[4].

<!-- b000683 | prose | pages [18] -->
into account to calculate the path loss. Its basic equation is shown in Formula 16

<!-- b000684 | prose | pages [18] -->
L1 = K1 + K2 lg d + K3 lg HTxeff + K4Diff_loss

<!-- b000685 | prose | pages [18] -->
(16) + K5 lg HTxeff lg d + K6HRxeff + Kchitterf(clutter),

<!-- b000686 | prose | pages [18] -->
where K4 is the multiplicative factor of the bypassing amount; Diff_loss(unit: dB) is the loss caused by bypassing the obstacle; K6 is the multiplicative factor of HRxeff, Rxeff is the mobile station receiving antenna height. K1, K2 and other variables are related to the height and distance of the signal base station as well as environment of drones.

<!-- b000687 | prose | pages [18] -->
For the repeater drone, when the siting is varied within the ideal distribution, K1, K2, K3, HTxeff, K4, K5, K6, and Kchitter are unchanged, and the small change of d is negligible, only HRxeff and Diff_loss will change. Therefore, the signal loss model of the repeater drone is established as follows.

<!-- b000688 | prose | pages [18] -->
L2 = K4 · Diff_loss + K6 · HRxeff + L0, (17)

<!-- b000689 | prose | pages [18] -->
[8]

<!-- b000690 | prose | pages [18] -->
K4 = 44.9 −6.55 log HRxeff,

<!-- b000691 | prose | pages [18] -->
[8]

<!-- b000692 | prose | pages [18] -->
K6 = 1.1 log frepeater −0.7,

<!-- b000693 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000694 | prose | pages [18] -->
L0 = 20 log10( 4π

<!-- b000695 | prose | pages [18] -->
[8] 关注数学模型

<!-- b000696 | prose | pages [18] -->
),

<!-- b000697 | furniture | pages [18] -->
2

<!-- b000698 | prose | pages [18] -->
λtransmitted wave

<!-- b000699 | furniture | pages [18] -->
MATHmodels

<!-- b000700 | furniture | pages [18] -->
获取更多资讯

<!-- b000701 | furniture | pages [19] -->
Team # 2105363

<!-- b000702 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000703 | furniture | pages [19] -->
Page 19 of 25

<!-- b000704 | prose | pages [19] -->
where fradio is frequency of repeater. λtransmitted wave is wavelength of transmitted wave in meters.

<!-- b000705 | prose | pages [19] -->
For Rxeff, drone altitude = altitude of location + height above ground.

<!-- b000706 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000707 | prose | pages [19] -->
For Diff_loss, we assume that the height of the obstacle is linearly related to the loss of the repeater range, with the most severe loss for obstacle heights greater than 1.5·Rxeff and considered almost no loss effect for obstacle heights less than 0.5·Rxeff. In the ideal case the loss ratio δ is 1.0, the worst case is 0.8. The loss ratio of the ith

<!-- b000708 | prose | pages [19] -->
obstacle :

<!-- b000709 | prose | pages [19] -->
δi = (Hi/Rxeff) · (1 −0.7)/(1.5 −0.5) + 0.7.

<!-- b000710 | prose | pages [19] -->
where Hi is the height of the ith obstacle Counting K obstacles on the linear path be- tween the repeater drone and the ﬁre area in 1000m. Calculate Diff_loss:

<!-- b000711 | prose | pages [19] -->
Diff_loss =

<!-- b000712 | prose | pages [19] -->
Y

<!-- b000713 | prose | pages [19] -->
δi.

<!-- b000714 | prose | pages [19] -->
(18)

<!-- b000715 | prose | pages [19] -->
i=1,2,...,K

<!-- b000716 | prose | pages [19] -->
[9] we can see that we should ensure that the signal-to-noise ratio

<!-- b000717 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000718 | prose | pages [19] -->
From the website

<!-- b000719 | prose | pages [19] -->
is not less than 20dB, that is,

<!-- b000720 | prose | pages [19] -->
L2 ⩾20dB.

<!-- b000721 | prose | pages [19] -->
(19)

<!-- b000722 | prose | pages [19] -->
We use this formula to ﬁlter out the areas that do not meet the requirements.

<!-- b000723 | prose | pages [19] -->
5.2 Drone safety

<!-- b000724 | prose | pages [19] -->
Depending on the scale of the ﬁre, repeater drones need to avoid nearby ﬁres to ensure safe operations. Because of the limited signal range of handheld radio, repeater drones are often located 2 to 5 km from the center of the ﬁre, and when the ﬁre is large and the terrain is ﬂammable, it is easy to spread to the repeater drone is located, causing damage to the drone in serious cases. We perform a quantitative analysis of safety based on information related to ﬁres.

<!-- b000725 | heading | pages [19] -->
Kinetics-based ﬁre spread model:

<!-- b000726 | prose | pages [19] -->
𝑣_𝑤𝑖𝑛𝑑

<!-- b000727 | caption | pages [19] -->
Figure 10: Kinetic-based ﬁre spread model schematic

<!-- b000728 | prose | pages [19] -->
As shown in the Figure 10, the ﬁre spread into eight directions, of which the direc- tion of the angle with the wind speed less than 45 degrees will spread outside (such as the direction of the yellow arrow), the other directions remain unchanged (such as the

<!-- b000729 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000730 | prose | pages [19] -->
direction of the blue arrow).

<!-- b000731 | prose | pages [19] -->
关注数学模型

<!-- b000732 | furniture | pages [19] -->
2

<!-- b000733 | furniture | pages [19] -->
MATHmodels

<!-- b000734 | furniture | pages [19] -->
获取更多资讯

<!-- b000735 | furniture | pages [20] -->
Team # 2105363

<!-- b000736 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000737 | furniture | pages [20] -->
Page 20 of 25

<!-- b000738 | prose | pages [20] -->
Vspread =⃗Vwind × exp((D + topography scoring) · ﬁre size + E),

<!-- b000739 | prose | pages [20] -->
where⃗Sr denotes the rate of spread in the vector direction, and D and E both denote

<!-- b000740 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000741 | prose | pages [20] -->
constants.

<!-- b000742 | prose | pages [20] -->
In the ﬁre spread range, the amount of change in the length of the ﬁre⃗k direction is

<!-- b000743 | prose | pages [20] -->
(

<!-- b000744 | prose | pages [20] -->
Vspread ×⃗k × unit time, Vspread ×⃗k > 0

<!-- b000745 | prose | pages [20] -->
∆⃗Lk =

<!-- b000746 | prose | pages [20] -->
0, others

<!-- b000747 | prose | pages [20] -->
and length of ﬁre⃗k direction is

<!-- b000748 | prose | pages [20] -->
,

<!-- b000749 | prose | pages [20] -->
Lk =⃗Lk(last time) + ∆⃗Lk.

<!-- b000750 | prose | pages [20] -->
Wind speeds were obtained from SSA drones collecting data from “boots-on-the- ground” teams, and terrain was scored to create a scoring table as follows.

<!-- b000751 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000752 | caption | pages [20] -->
Table 5: Terrain scoring table

<!-- b000753 | prose | pages [20] -->
Terrains Scores

<!-- b000754 | prose | pages [20] -->
Forests, grassy hills, grasslands Plains, other terrain 3 2 Not happened recently 1

<!-- b000755 | prose | pages [20] -->
To ensure safety, the distance between the ith repeater drone position (xdrone,i, ydrone,i), which is in a certain direction of the ﬁre, and the edge of the ﬁre should be made no less than the safety threshold, which is set here to 50 m. Therefore,

<!-- b000756 | prose | pages [20] -->
|(xdrone,i, ydrone,i) −(x, y) of center| ⩾50 + the range length of the ﬁre.

<!-- b000757 | prose | pages [20] -->
(20)

<!-- b000758 | prose | pages [20] -->
where "(x, y) of the center" denotes the latitude and longitude of the ﬁre center. "The range length of the ﬁre" means the range length in a certain direction of the ﬁre at a certain moment.

<!-- b000759 | prose | pages [20] -->
Location optimization:

<!-- b000760 | prose | pages [20] -->
The signal-to-noise ratio and distance from the edge of the ﬁre are calculated for each location in the ideal distribution range, and reasonable locations are selected:

<!-- b000761 | prose | pages [20] -->
[9]

<!-- b000762 | prose | pages [20] -->
L2 ⩾20dB.

<!-- b000763 | prose | pages [20] -->
We use this constraint to optimize to get the drone range from the point of view of preventing ﬁre spread hazards by drones.

<!-- b000764 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000765 | prose | pages [20] -->
关注数学模型

<!-- b000766 | furniture | pages [20] -->
2

<!-- b000767 | furniture | pages [20] -->
MATHmodels

<!-- b000768 | furniture | pages [20] -->
获取更多资讯

<!-- b000769 | furniture | pages [21] -->
Team # 2105363

<!-- b000770 | prose | pages [21] -->
5.3

<!-- b000771 | heading | pages [21] -->
Result analysis

<!-- b000772 | prose | pages [21] -->
𝐿𝑎𝑡𝑖𝑡𝑢𝑑𝑒 𝑎𝑛𝑑 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒: −36.7322, 147.3058

<!-- b000773 | prose | pages [21] -->
𝐹𝑖𝑟𝑒 𝑑𝑖𝑟𝑒𝑐𝑡𝑖𝑜𝑛

<!-- b000774 | prose | pages [21] -->
𝐻𝑒𝑖𝑔ℎ𝑡: 1986m 𝐹𝑖𝑟𝑒 𝑑𝑖𝑟𝑒𝑐𝑡𝑖𝑜𝑛

<!-- b000775 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000776 | furniture | pages [21] -->
Page 21 of 25

<!-- b000777 | prose | pages [21] -->
𝐿𝑎𝑡𝑖𝑡𝑢𝑑𝑒 𝑎𝑛𝑑 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒: −37.4935, 147.3724 𝐻𝑒𝑖𝑔ℎ𝑡: 14m

<!-- b000778 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000779 | prose | pages [21] -->
(a) The highest altitude

<!-- b000780 | prose | pages [21] -->
𝐼𝑑𝑒𝑎𝑙 𝑐𝑎𝑛𝑑𝑖𝑑𝑎𝑡𝑒 𝑟𝑎𝑛𝑔𝑒

<!-- b000781 | prose | pages [21] -->
𝑂𝑝𝑡𝑖𝑚𝑖𝑧𝑒𝑑 𝑜𝑝𝑡𝑖𝑜𝑛𝑎𝑙 𝑟𝑎𝑛𝑔𝑒

<!-- b000782 | prose | pages [21] -->
𝑁𝑜𝑛 𝑠𝑎𝑓𝑒𝑟 𝑎𝑟𝑒𝑎𝑠

<!-- b000783 | prose | pages [21] -->
(b) The lowest altitude

<!-- b000784 | caption | pages [21] -->
Figure 11: Optimization of the location of the highest and lowest points of altitude

<!-- b000785 | prose | pages [21] -->
Obviously, the wind direction directly affects the distribution of the optimized re-

<!-- b000786 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000787 | prose | pages [21] -->
peater drones, which is concentrated at the edge of the ideal range perpendicular to the wind direction. High altitude areas are more likely to be affected by the altitude of dif- ferent locations, which manifests itself in the form of a discontinuous and interrupted range of the optimized distribution.

<!-- b000788 | prose | pages [21] -->
6

<!-- b000789 | heading | pages [21] -->
Sensitivity analysis

<!-- b000790 | heading | pages [21] -->
Sensitivity Analysis of safety factor S(x, y)

<!-- b000791 | prose | pages [21] -->
6.1

<!-- b000792 | prose | pages [21] -->
In Task 1, we classify the areas of Victoria as different danger levels by calculating the safety factor. Therefore, the safety factor S(x, y) is a crucial parameter, which is cal- culated by ﬁre frequency f(x, y), ﬁze size size(x, y), recent ﬁre situation situation(x, y) (see Formula 4). As a result, we do sensitivity analysis on the coefﬁcients a1, a2 and a3 of these three parameters and the results are shown in Figure 12.

<!-- b000793 | prose | pages [21] -->
1

<!-- b000794 | prose | pages [21] -->
Comprehensive safety factor S(x,y)

<!-- b000795 | prose | pages [21] -->
0.9

<!-- b000796 | prose | pages [21] -->
0.8

<!-- b000797 | prose | pages [21] -->
0.7

<!-- b000798 | prose | pages [21] -->
0.6

<!-- b000799 | prose | pages [21] -->
0.5

<!-- b000800 | prose | pages [21] -->
0.4

<!-- b000801 | prose | pages [21] -->
0.3

<!-- b000802 | prose | pages [21] -->
0.2

<!-- b000803 | prose | pages [21] -->
0.1

<!-- b000804 | prose | pages [21] -->
0

<!-- b000805 | prose | pages [21] -->
-10% -10% -5% -5% 0 0 5% 5% 10% 10% -10% -10%

<!-- b000806 | prose | pages [21] -->
1a

<!-- b000807 | prose | pages [21] -->
-5% -5% -5% -5% 0 0 5% 5% 10% 10% -10% -10% -5% -5% 0 0 5% 5% 10% 10%

<!-- b000808 | prose | pages [21] -->
a 3a 2

<!-- b000809 | prose | pages [21] -->
The weight change of parameter a

<!-- b000810 | caption | pages [21] -->
Figure 12: Sensitivity Analysis of S(x, y)

<!-- b000811 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000812 | prose | pages [21] -->
关注数学模型

<!-- b000813 | furniture | pages [21] -->
2

<!-- b000814 | furniture | pages [21] -->
MATHmodels

<!-- b000815 | furniture | pages [21] -->
获取更多资讯

<!-- b000816 | furniture | pages [22] -->
Team # 2105363

<!-- b000817 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000818 | furniture | pages [22] -->
Page 22 of 25

<!-- b000819 | prose | pages [22] -->
In Figure 12, we select a high-risk area as a place to test sensitivity, and the coordi- nate is (x, y) = (−36.0634, 148.2911)

<!-- b000820 | prose | pages [22] -->
From the ﬁgure we can conclude that When the variation of a1, a2 and a3 change from -10% to 10%, the changes in the values of S(x, y) corresponding to a1 and a3 are

<!-- b000821 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000822 | prose | pages [22] -->
small and the overall trend is ﬂat. Therefore, we believe that the frequency and size of ﬁres are more robust and do not affect S too much. Meanwhile, a2 corresponds to a relatively large amount of change in S(x, y), so we think the sensitivity of the recent ﬁre situation to be strong. This result veriﬁes the reasonableness of our consideration of situation(x, y) in Section 3.1.1.

<!-- b000823 | heading | pages [22] -->
Sensitivity analysis of ﬁre frequency in different regions per year

<!-- b000824 | prose | pages [22] -->
6.2

<!-- b000825 | prose | pages [22] -->
The annual frequency of ﬁres in different regions has a signiﬁcant impact on the number of SSA drones. Therefore, we divid Victoria into central, eastern, western, and southern regions, and do sensitivity analysis on the ﬁre frequency in each of these four

<!-- b000826 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000827 | prose | pages [22] -->
geographic regions.

<!-- b000828 | prose | pages [22] -->
400

<!-- b000829 | prose | pages [22] -->
Number of SSA drones

<!-- b000830 | prose | pages [22] -->
320

<!-- b000831 | prose | pages [22] -->
240

<!-- b000832 | prose | pages [22] -->
180

<!-- b000833 | prose | pages [22] -->
120

<!-- b000834 | prose | pages [22] -->
60

<!-- b000835 | prose | pages [22] -->
0 400 800 1200 1600

<!-- b000836 | prose | pages [22] -->
Central region Eastern region Western region Southern region

<!-- b000837 | prose | pages [22] -->
2000 2400 2800 3200 3600

<!-- b000838 | prose | pages [22] -->
Frequency of fire(times/year)

<!-- b000839 | caption | pages [22] -->
Figure 13: Sensitivity analysis of ﬁre frequency in different regions per year

<!-- b000840 | prose | pages [22] -->
We can analyze Figure 13 in two ways. For ﬁre frequency, the number of SSA drones vary the most when the number of ﬁres in Victoria is in the range of 1600∼2000 per year. That is, the ﬁre frequency is sensitive in the interval [1600,2000]. Therefore, when CFA uses our model, if the measured number of ﬁres in the year is within this interval, they should calculate the number of SSA drones very carefully.

<!-- b000841 | prose | pages [22] -->
For different regions, the number of SSA drones in the four regions change sig- niﬁcantly when the ﬁre frequency is greater than 1600. The central region of Victoria has the highest number, while the southern region has the lowest. Therefore, regions are also sensitive to the number of SSA drones, and CFA’s drone dispatch should be different in different regions.

<!-- b000842 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000843 | prose | pages [22] -->
关注数学模型

<!-- b000844 | furniture | pages [22] -->
2

<!-- b000845 | furniture | pages [22] -->
MATHmodels

<!-- b000846 | furniture | pages [22] -->
获取更多资讯

<!-- b000847 | furniture | pages [23] -->
Team # 2105363

<!-- b000848 | prose | pages [23] -->
7

<!-- b000849 | heading | pages [23] -->
Strengths and Weaknesses

<!-- b000850 | prose | pages [23] -->
7.1

<!-- b000851 | heading | pages [23] -->
Strengths

<!-- b000852 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000853 | furniture | pages [23] -->
Page 23 of 25

<!-- b000854 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000855 | prose | pages [23] -->
• We innovatively use safety factors to classify classes for areas with different ﬁre conditions, which improves the efﬁciency of drone response for emergency situ- ations and provides a clear idea for drone dispatching and distribution. • The combination and reuse relationship between drones is used to optimize the utilization rate of repeater drones, which both ﬁts the actual situation and has a universal solution to other conﬁguration problems. • The ternary commensurable prediction model is a model that predicts the prob- ability of future special situations for data of special situations, and the commen- surabiliby it considers is very accurate in the face of special situations with the superiority that other forecasting models do not have. • We have reviewed a large amount of literature, not only with sufﬁcient data, but also with estimation and calculation methods for the parameters of each model

<!-- b000856 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000857 | prose | pages [23] -->
from specialized literature, and the results are scientiﬁc and rigorous.

<!-- b000858 | prose | pages [23] -->
7.2

<!-- b000859 | heading | pages [23] -->
Weaknesses

<!-- b000860 | prose | pages [23] -->
• In the problem of optimizing the position of the repeater drone, we are limited by the data for the simulation solution, and the results may be somewhat different from the real situation. • The index estimated by using AHP model has some subjective inﬂuence, and sensitivity analysis is needed to calculate the reliability of the model.

<!-- b000861 | prose | pages [23] -->
Annotated Budget Request 8

<!-- b000862 | prose | pages [23] -->
Budget Justiﬁcation for Cost Proposal (Unit: A$)

<!-- b000863 | prose | pages [23] -->
We are a numerical modeling competition team from MCM and will be responsi- ble for the overall management and direction of the Victorian National Fire Service’s drone acquisition program for the Rapid Bushﬁre Response Division and equipment acquisition program for extreme ﬁres over the next decade, based on the soundness of our models through testing and analysis of results.

<!-- b000864 | prose | pages [23] -->
1. "Rapid Jungle Response" Project

<!-- b000865 | prose | pages [23] -->
Direct costs: 2,401,030

<!-- b000866 | prose | pages [23] -->
Drones

<!-- b000867 | prose | pages [23] -->
SSA drones

<!-- b000868 | prose | pages [23] -->
Radio repeater drones

<!-- b000869 | prose | pages [23] -->
Number Single price Total price

<!-- b000870 | prose | pages [23] -->
200 10,390 2,077,200

<!-- b000871 | prose | pages [23] -->
32 10,094.741 323,030

<!-- b000872 | prose | pages [23] -->
The number of SSA drones procured to respond to emergency ﬁre situations in Vic- toria includes 134 shift SSA drones for emergency response to high-risk areas, 62 SSA drones for ﬁre preparedness in prepared areas, and 4 standby drones for considera-

<!-- b000873 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000874 | prose | pages [23] -->
tion of wear and tear. The cost of each SSA drone includes the cost of a bare drone at关注数学模型

<!-- b000875 | furniture | pages [23] -->
2

<!-- b000876 | furniture | pages [23] -->
MATHmodels

<!-- b000877 | furniture | pages [23] -->
获取更多资讯

<!-- b000878 | furniture | pages [24] -->
Team # 2105363

<!-- b000879 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000880 | furniture | pages [24] -->
Page 24 of 25

<!-- b000881 | prose | pages [24] -->
A$10,000, an HD camera at A$47.370, and a thermal imaging camera at A$338.648; the repeater drones include 21 repeater drones in combination with SSA drones in high- risk areas and 21 repeater drones in combination with SSA drones in preparedness areas 11, the cost of each repeater drone includes a bare drone of A$10,000, the cost of

<!-- b000882 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000883 | prose | pages [24] -->
a repeater of A$94.741.

<!-- b000884 | prose | pages [24] -->
With this drone conﬁguration, the drones can detect all 373 locations (including 154 high-risk areas and 219 precautionary areas) throughout the state with high frequency and large ﬁre sizes, and have an average response time to emergency ﬁres of only 5 minutes and 17 seconds. In addition, each repeater drone achieved a combined rate of 6.25 with SSA drones. the overall system had excellent responsiveness and excellent combined relationships.

<!-- b000885 | prose | pages [24] -->
Other costs: None.

<!-- b000886 | prose | pages [24] -->
Electricity cost for drone charging: A$0.

<!-- b000887 | prose | pages [24] -->
Our analysis of the infrastructure within the Victorian State Fire Service concluded that the infrastructure within the Fire Service can accommodate the normal conduct of

<!-- b000888 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000889 | prose | pages [24] -->
activities for other costs and therefore the cost is 0.

<!-- b000890 | heading | pages [24] -->
2. Equipment procurement items to respond to extreme ﬁres over the next ten

<!-- b000891 | prose | pages [24] -->
years

<!-- b000892 | prose | pages [24] -->
Direct Costs: 148,950

<!-- b000893 | prose | pages [24] -->
Additional equipment (abbreviated): $A 4952.25

<!-- b000894 | prose | pages [24] -->
Equipment

<!-- b000895 | prose | pages [24] -->
EOC radios

<!-- b000896 | prose | pages [24] -->
“Boots-on-the-ground” handheld radios

<!-- b000897 | prose | pages [24] -->
“Boots-on-the-ground” team wearable

<!-- b000898 | prose | pages [24] -->
equipment

<!-- b000899 | prose | pages [24] -->
Number Single price Total price

<!-- b000900 | prose | pages [24] -->
5 92.725 463.625

<!-- b000901 | prose | pages [24] -->
1,800 19 94.741

<!-- b000902 | prose | pages [24] -->
2,688.625 19 141.507

<!-- b000903 | prose | pages [24] -->
From a safety perspective, we consider a one-to-one EOC for extreme ﬁres and adjust the number of ﬁreﬁghters in the Ground Boots team based on the predicted size of the extreme ﬁre. We provide a handheld radio and a set of wearables for each ﬁreﬁghter in the "boots on the ground" team, with one two-way radio and a backup two-way radio per EOC. The unit cost of the wearables included a ﬁre axe for $11.288, a heat suit for $120.442, and a ﬁre extinguisher for $9.877. According to our modeling, this scenario has a success rate of more than 80% for "boots on the ground" teams for extreme ﬁres.

<!-- b000904 | prose | pages [24] -->
Staff cost: 144,000

<!-- b000905 | prose | pages [24] -->
Number Staff

<!-- b000906 | prose | pages [24] -->
Command staff within EOC

<!-- b000907 | prose | pages [24] -->
Firefighters in “Boots-on-the-ground”

<!-- b000908 | prose | pages [24] -->
Single price Total price

<!-- b000909 | prose | pages [24] -->
5 6,000 30,000

<!-- b000910 | prose | pages [24] -->
19 6,000 114,000

<!-- b000911 | prose | pages [24] -->
We consider subsidizing a bonus for ﬁreﬁghters to encourage their performance in ﬁre rescue, and similarly, for each EOC, the hard work of the command staff is worth a bonus. We refer to the federal government’s subsidy for volunteer ﬁreﬁghters in New

<!-- b000912 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000913 | prose | pages [24] -->
South Wales for the bonus assessment.

<!-- b000914 | prose | pages [24] -->
关注数学模型

<!-- b000915 | furniture | pages [24] -->
2

<!-- b000916 | furniture | pages [24] -->
MATHmodels

<!-- b000917 | furniture | pages [24] -->
获取更多资讯

<!-- b000918 | furniture | pages [25] -->
Team # 2105363

<!-- b000919 | prose | pages [25] -->
Other costs: None

<!-- b000920 | prose | pages [25] -->
Cost of apparatus consumption: None

<!-- b000921 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000922 | furniture | pages [25] -->
Page 25 of 25

<!-- b000923 | prose | pages [25] -->
Wear and tear of ﬁreﬁghting equipment: A$0 Loss of drones: $0

<!-- b000924 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000925 | prose | pages [25] -->
The primary job of the "boots on the ground" team is to detect ﬁrst-hand informa- tion about the ﬁre, make judgments about the rapidly changing situation, and pass additional information to the EOC. Therefore, ﬁre ﬁghting is not their main job, the consumption of ﬁreﬁghting equipment is negligible. The wear and tear of drones is already considered in the cost of drones.

<!-- b000926 | heading | pages [25] -->
References

<!-- b000927 | references | pages [25] -->
[1] Active Fire Data. [online] Available at:

<!-- b000928 | references | pages [25] -->
https://firms.modaps.eosdis.na

<!-- b000929 | references | pages [25] -->
sa.gov/active_fire/#firms-shapefile [Accessed 6 Feb. 2021]

<!-- b000930 | references | pages [25] -->
微信号：MATHmodels

<!-- b000931 | references | pages [25] -->
http:

<!-- b000932 | references | pages [25] -->
[2] When exactly will the ﬁre in Australia be put out?. [online] Available at:

<!-- b000933 | references | pages [25] -->
//www.ctoutiao.com/2585517.html [Accessed 6 Feb. 2021]

<!-- b000934 | references | pages [25] -->
[3] Zhao

<!-- b000935 | references | pages [25] -->
Zeming.

<!-- b000936 | references | pages [25] -->
Brief

<!-- b000937 | heading | pages [25] -->
introduction

<!-- b000938 | prose | pages [25] -->
of Polish volunteer ﬁre brigade[J].Fire technology and product information,2014,(6):116,47. DOI:10.3969/j.issn.1002- 784X.2014.06.044.

<!-- b000939 | prose | pages [25] -->
[4] Chu Peisi. Research and system measurement of wireless signal propagation loss

<!-- b000940 | prose | pages [25] -->
prediction algorithm in mobile communication system[D]. Sichuan:University of Electronic Science and Technology, 2013. DOI:10.7666/d.D762613.

<!-- b000941 | prose | pages [25] -->
https://en.wikip [5] List of major bushﬁres in Australia. [online] Available at:

<!-- b000942 | prose | pages [25] -->
edia.org/wiki/List_of_major_bushfires_in_Australia [Accessed 8 Feb. 2021]

<!-- b000943 | prose | pages [25] -->
[6] Huang Jinfeng, Xia Jun, Du Hong, et al. Medium- and long-term ﬂood fore-

<!-- b000944 | prose | pages [25] -->
casting at Lutaizi and Bengbu stations based on metrizability and gray corre- lation pattern recognition method[J]. Journal of Wuhan University (Engineering Edition),2015,48(5):622-626. DOI:10.14188/j.1671-8844.2015-05-005.

<!-- b000945 | prose | pages [25] -->
[7] Yellow River Survey, Planning and Design Co. Feasibility study report of the

<!-- b000946 | prose | pages [25] -->
downstream Yellow River ﬂood control project [R]. Zhengzhou: Yellow River Sur- vey, Planning and Design Co., Ltd, 2015: 4-192.

<!-- b000947 | prose | pages [25] -->
[8] B. Sridhar and M. Z. Ali Khan, "RMSE comparison of path loss models for UH-

<!-- b000948 | prose | pages [25] -->
F/VHF bands in India," 2014 IEEE REGION 10 SYMPOSIUM, Kuala Lumpur, 2014, pp. 330-335, doi: 10.1109/TENCONSpring.2014.6863052.

<!-- b000949 | prose | pages [25] -->
[9] What is the general signal-to-noise ratio, the useful signal will not be drowned. [online]

<!-- b000950 | prose | pages [25] -->
zhidao.baidu.com/question/624747251070347044.ht Available at: ml [Accessed 8 Feb. 2021]

<!-- b000951 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000952 | prose | pages [25] -->
关注数学模型

<!-- b000953 | furniture | pages [25] -->
2

<!-- b000954 | furniture | pages [25] -->
MATHmodels

<!-- b000955 | furniture | pages [25] -->
获取更多资讯
