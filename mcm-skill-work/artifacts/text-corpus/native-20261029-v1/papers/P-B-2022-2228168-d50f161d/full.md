# P-B-2022-2228168-d50f161d

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2022

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | title | pages [1] -->
2228168

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | title | pages [1] -->
A Two-Stage Water Resource Optimal Operation Model

<!-- b000011 | title | pages [1] -->
Based on Genetic Algorithm

<!-- b000012 | heading | pages [1] -->
Abstract

<!-- b000013 | prose | pages [1] -->
In 2021, the Western United States experienced unprecedented dry weather that caused local reservoir levels to drop to record lows. Our team use operational research, mathematics, finance, computer science and other knowledge to build a mathematical model, providing a variety of practical solutions for reservoir water resource scheduling.

<!-- b000014 | prose | pages [1] -->
Firstly, we draw and fit the elevation and storage linear function of Lake Powell and Lake Mead in recent ten years. The linear programming model of total transportation cost minimization is established and solved by matlab linear programming solver. The amount of water extracted from Lake Powell and Lake Mead is 858333 acre-feet and 391666 acre-feet respectively. When there is no rainfall data, the solution is based on the objective of minimum transportation cost, and it is obtained that after 23 months, water resources will not be enough to meet the water demand of each state. At least 1051875.051 acre-ft is required for the 24th month. After that, the monthly external water supply amount for the two reservoirs is 1,118,780.48 acre-ft.

<!-- b000015 | prose | pages [1] -->
Secondly, we analyze the competing interests of agriculture, industry, residential water usage and electricity production; construct a two-stage programming model. The lower-level stage model solves the assignment of the total water intake and total power generation of the two dams, and the enhanced elite reservation genetic algorithm is used to get the optimal solution and the maximum value into the single-objective differential evolution algorithm for deeper optimization. The results of production value is $412,208,7017, and the total water consumption is 49,52007 acre-feet, with more water extracted from Lake Powell.

<!-- b000016 | prose | pages [1] -->
Thirdly, When there is not enough water to meet all water and electricity needs, we establish a nonlinear programming model under the premise of meeting the minimum demand ,to minimize the excess power generation and water discharge, so as to cope with the state of drought and water shortage for as long as possible. Genetic algorithm is used to solve the water and energy demand distribution of the system. The water extracted from Lake Powell and Lake Mead in a month is 1946626.71 acre-feet and 4040078.68 acre-feet, Glen Canyon Dam and Hoover Dam output 30037.82 acre- feet and 110848.56 acre-feet downstream respectively.

<!-- b000017 | prose | pages [1] -->
Fourthly, As drought intensifies, demand for electricity declines. If the degree of drought is too high, the total electricity demand will not be satisfied. With the development of new energy technology, the demand for hydroelectric power is decreasing. When the water demand is unchanged and the electricity demand decreases by 25%, 50% and 75% respectively, the calculation shows that the water demand for reservoirs in each state is much higher than the electricity demand. When water saving and electricity saving measures are adopted and the respective demand decreases by more than 75%, the water consumption of users can be satisfied.

<!-- b000018 | prose | pages [1] -->
Finally, We submit an article for Drought and Thirst magazine based on the above process.

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | furniture | pages [2] -->


<!-- b000021 | contents | pages [2] -->
1.

<!-- b000022 | contents | pages [2] -->
Introduction ............................................................................................................................... 1

<!-- b000023 | contents | pages [2] -->
2.

<!-- b000024 | contents | pages [2] -->
Assumptions and Justification ................................................................................................... 2

<!-- b000025 | contents | pages [2] -->
3.

<!-- b000026 | contents | pages [2] -->
Notations ................................................................................................................................... 3

<!-- b000027 | contents | pages [2] -->
4.

<!-- b000028 | contents | pages [2] -->
Models and solutions of problem 1 ........................................................................................... 4

<!-- b000029 | contents | pages [2] -->
4.1 The optimal transportation .................................................................................................. 4

<!-- b000030 | contents | pages [2] -->
4.1.1 Water supply meets requirements ............................................................................. 4

<!-- b000031 | contents | pages [2] -->
4.1.2 Constraints on the height of the dam water level ..................................................... 6

<!-- b000032 | contents | pages [2] -->
4.1.3 Equilibrium constraints on Colorado River recharge and outflow ........................... 7

<!-- b000033 | contents | pages [2] -->
4.1.4 Dam release constraint ............................................................................................. 9

<!-- b000034 | contents | pages [2] -->
4.1.5 Objective function .................................................................................................... 9

<!-- b000035 | contents | pages [2] -->
4.1.6 Model solving ......................................................................................................... 10

<!-- b000036 | contents | pages [2] -->
4.2 Optimal duration of water allocation ................................................................................ 11

<!-- b000037 | contents | pages [2] -->
4.3 The relationship of external water transfer with time ....................................................... 12

<!-- b000038 | contents | pages [2] -->
5.

<!-- b000039 | contents | pages [2] -->
Models and solutions of problem 2 ......................................................................................... 12

<!-- b000040 | contents | pages [2] -->
5.1 Lower-level model construction ........................................................................................ 13

<!-- b000041 | contents | pages [2] -->
5.2 Lower model solution ....................................................................................................... 14

<!-- b000042 | contents | pages [2] -->
5.3 Upper-level model construction ........................................................................................ 16

<!-- b000043 | contents | pages [2] -->
5.4 The final result of the upper model ................................................................................... 16

<!-- b000044 | contents | pages [2] -->
6.

<!-- b000045 | contents | pages [2] -->
Models and solutions of problem 3 ......................................................................................... 17

<!-- b000046 | contents | pages [2] -->
7.

<!-- b000047 | contents | pages [2] -->
Sensitivity Analysis ................................................................................................................. 18

<!-- b000048 | contents | pages [2] -->
8.

<!-- b000049 | contents | pages [2] -->
Conclusions ............................................................................................................................. 20

<!-- b000050 | contents | pages [2] -->
8.1 Conclusions of the problem1 ............................................................................................ 20

<!-- b000051 | contents | pages [2] -->
8.2 Conclusions of the problem2 ............................................................................................ 20

<!-- b000052 | contents | pages [2] -->
8.3 Conclusions of the problem3 ............................................................................................ 20

<!-- b000053 | contents | pages [2] -->
8.4 Conclusions of the problem4 ............................................................................................ 20

<!-- b000054 | contents | pages [2] -->
9.

<!-- b000055 | contents | pages [2] -->
Model Evaluation and Further Discussion .............................................................................. 20

<!-- b000056 | contents | pages [2] -->
9.1 Strengths............................................................................................................................ 20

<!-- b000057 | contents | pages [2] -->
9.2 Weakness ........................................................................................................................... 21

<!-- b000058 | contents | pages [2] -->
10. Article for Drought and Thirst magazine ................................................................................ 22

<!-- b000059 | furniture | pages [2] -->


<!-- b000060 | furniture | pages [2] -->


<!-- b000061 | heading | pages [3] -->
1. Introduction

<!-- b000062 | heading | pages [3] -->
1.1 Problem Background

<!-- b000063 | prose | pages [3] -->
In 2021 , the western United States has experienced unprecedented dry weather , which not only led to two of the nation's largest reservoirs of the Colorado River , Lake Powell and Lake Mead , permanently low but also posed a threat to the production and life of the people . The low water flows have reduced the amount of electricity produced by hydropower plants , leading to interruptions in power supplies in these areas . As shown in Figure 1，the white ‘bathtub ring’ around Lake Mead shows the record low water levels as drought continues to worsen in Nevada [1].

<!-- b000064 | furniture | pages [3] -->


<!-- b000065 | furniture | pages [3] -->


<!-- b000066 | caption | pages [3] -->
Figure 1: the white ‘bathtub ring’ around Lake Mead

<!-- b000067 | furniture | pages [3] -->


<!-- b000068 | prose | pages [3] -->
Because of such conditions, a rational, defensible water allocation plan for current and future water supply conditions is critically important. This article will use operational research, mathematics, physics, computer science, environmental science and other knowledge to construct mathematical models and finally provide practical solutions for the dam operations.

<!-- b000069 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000070 | prose | pages [3] -->
⚫ Considering the restrictions identified with the problem statement, we need

<!-- b000071 | prose | pages [3] -->
to address the following problems: ⚫ Build mathematical models to develop rational water allocation plans for

<!-- b000072 | prose | pages [3] -->
current and future water supply conditions. Analyze how much water should be drawn from each of Lake Mead and Lake Powell to meet customer water and electricity needs. ⚫ Without taking into account the replenishment of other water resources such

<!-- b000073 | prose | pages [3] -->
as rainfall, how long will it take before the demands are not met? ⚫ According to the established mathematical model, analyze and solve the

<!-- b000074 | prose | pages [3] -->
competition relationship between general water use in agriculture, industry, residence and electricity production water . Explain the standards used to solve competitive interests clearly. ⚫ If there is not enough water to supply the residents' water and electricity

<!-- b000075 | prose | pages [3] -->
needs, what should be done.

<!-- b000076 | prose | pages [4] -->
⚫ The water and electricity demands of the communities change over time.

<!-- b000077 | prose | pages [4] -->
What happens when analyzing population, agriculture, or industry growth or shrinkage in affected areas? ⚫ How should the model adjust as the proportion of renewable energy

<!-- b000078 | prose | pages [4] -->
technologies increases or when additional water and electricity savings are implemented?

<!-- b000079 | furniture | pages [4] -->


<!-- b000080 | heading | pages [4] -->
1.3 Our work

<!-- b000081 | prose | pages [4] -->
⚫ We collected the water level and stock data of Lake Powell and Lake Mead in recent ten years, drew and fitted the water level and stock linear function of the two reservoirs. ⚫ We established a linear programming model for minimizing the total

<!-- b000082 | prose | pages [4] -->
transportation cost, taking the total water transfer and transportation cost as the objective function, the amount of water taken from each state and the discharge of two dams as the decision-making variables, and the discharge of the dam, the level of the reservoir after dispatching, and the water resources demand of each state as the constraints. ⚫ we construct a two-stage mathematical model. The first stage model solved

<!-- b000083 | prose | pages [4] -->
the task assignment of the total water intake and total power generation of the two dams, and the enhanced elite reservation genetic algorithm is used to put the optimal solution and the optimal value into the single-objective differential evolution algorithm for deeper optimization. ⚫ We submit an article for Drought and Thirst magazine.

<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | heading | pages [4] -->
2. Assumptions and Justification

<!-- b000086 | prose | pages [4] -->
⚫ The starting point of water supply is set at the dam. The location of the

<!-- b000087 | prose | pages [4] -->
dam and the lake is close, and the distance calculation is more convenient. So we can set the dam as the starting point of water supply. ⚫ Water supply target points are set at the centroids of the state's planar

<!-- b000088 | prose | pages [4] -->
terrain. The water consumption in different regions of each state is unbalanced. By setting the target points at the centroids of the state's planar terrain, we can measure the distance directly . ⚫ The transportation cost per unit of distance and unit of water flow in

<!-- b000089 | prose | pages [4] -->
each state is equal. The transportation distance and flow of water resources may be different. Assuming the same unit transportation cost, it is convenient to solve the distrubution scheme.

<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | furniture | pages [4] -->


<!-- b000092 | furniture | pages [4] -->


<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | furniture | pages [4] -->


<!-- b000095 | furniture | pages [4] -->


<!-- b000096 | heading | pages [5] -->
3. Notations

<!-- b000097 | heading | pages [5] -->
Symbols

<!-- b000098 | prose | pages [5] -->
Description

<!-- b000099 | prose | pages [5] -->
x

<!-- b000100 | furniture | pages [5] -->


<!-- b000101 | prose | pages [5] -->
dispatched water flow from Lake powell to state i p i ,

<!-- b000102 | prose | pages [5] -->
x

<!-- b000103 | furniture | pages [5] -->


<!-- b000104 | prose | pages [5] -->
dispatched water flow from Lake mead to state i m i ,

<!-- b000105 | prose | pages [5] -->
( )

<!-- b000106 | furniture | pages [5] -->


<!-- b000107 | prose | pages [5] -->
lake powell water level after a water dispatch + P t T 0

<!-- b000108 | prose | pages [5] -->
( )

<!-- b000109 | furniture | pages [5] -->


<!-- b000110 | prose | pages [5] -->
water levels at Lake Mead after a water dispatch + M t T 0

<!-- b000111 | prose | pages [5] -->
the magnitude of surface water flow into Lake Mead during q m the transfer period

<!-- b000112 | prose | pages [5] -->
the magnitude of surface water flow into Mexico during the q

<!-- b000113 | furniture | pages [5] -->


<!-- b000114 | prose | pages [5] -->
M transfer period

<!-- b000115 | prose | pages [5] -->
electricity generated by Lake powell hydroelectric power E p generation during water transfer period

<!-- b000116 | prose | pages [5] -->
electricity generated by Lake mead hydroelectric power E m generation during the water transfer period

<!-- b000117 | prose | pages [5] -->
d

<!-- b000118 | furniture | pages [5] -->


<!-- b000119 | prose | pages [5] -->
the distance from Lake Powell to State i p i ,

<!-- b000120 | prose | pages [5] -->
d

<!-- b000121 | furniture | pages [5] -->


<!-- b000122 | prose | pages [5] -->
the distance from Lake Mead to State i, m i ,

<!-- b000123 | prose | pages [5] -->
ik the cost of state i unit distance unit water flow transportation

<!-- b000124 | prose | pages [5] -->
T time required for a water dispatch

<!-- b000125 | prose | pages [5] -->
( ) M t initial water level at Lake Mead before a water dispatch 0

<!-- b000126 | prose | pages [5] -->
the magnitude of surface water flow into Lake powell during q p the diversion period

<!-- b000127 | prose | pages [5] -->
( ) P t initial water level at Lake powell before a water dispatch 0

<!-- b000128 | prose | pages [5] -->
the magnitude of rainfall flow into Lake powell during the q

<!-- b000129 | furniture | pages [5] -->


<!-- b000130 | prose | pages [5] -->
,r p diversion period

<!-- b000131 | prose | pages [5] -->
the magnitude of rainfall flow into Lake Mead during the q

<!-- b000132 | furniture | pages [5] -->


<!-- b000133 | prose | pages [5] -->
,r m transfer period

<!-- b000134 | prose | pages [5] -->
the lowest and highest water levels allowed by Lake Powell; P , P

<!-- b000135 | furniture | pages [5] -->


<!-- b000136 | prose | pages [5] -->
min max corresponding to stagnant water levels and flood levels.

<!-- b000137 | prose | pages [5] -->
minimum and maximum water levels allowed by Lake Mead; M , M

<!-- b000138 | furniture | pages [5] -->


<!-- b000139 | prose | pages [5] -->
min max corresponding to standing water and flood levels

<!-- b000140 | prose | pages [5] -->
the maximum water flow allowed into Lake Mead Mexico

<!-- b000141 | prose | pages [5] -->
q , q

<!-- b000142 | furniture | pages [5] -->


<!-- b000143 | prose | pages [5] -->
during the dispatch period; corresponds to the maximum

<!-- b000144 | prose | pages [5] -->
m ,max M ,max

<!-- b000145 | prose | pages [5] -->
discharge of Colombier and Hoover Dams ( ) S P lake powell water level as a function of lake surface area p

<!-- b000146 | prose | pages [5] -->
( ) S M

<!-- b000147 | furniture | pages [5] -->


<!-- b000148 | prose | pages [5] -->
Lake Mead water level as a function of lake surface area m

<!-- b000149 | furniture | pages [5] -->


<!-- b000150 | furniture | pages [5] -->


<!-- b000151 | furniture | pages [5] -->


<!-- b000152 | heading | pages [6] -->
4. Models and solutions of problem 1

<!-- b000153 | prose | pages [6] -->
Negotiating teams in the states asked us to build models to guide the operation of

<!-- b000154 | prose | pages [6] -->
the dam, which is the ultimate goal of the issue.

<!-- b000155 | prose | pages [6] -->
We found that the water supply strategy affects the water level of the corresponding reservoirs of the two dams, which indirectly affects hydropower generation. This indicates that there are constraints on water supply and electricity demand. Our team temporarily separated the water supply and electricity demand, and set up several small stages to analyze and simplify the problem. And the complete model will eventually be shown in the second question.

<!-- b000156 | prose | pages [6] -->
⚫ Firstly, meet the water needs. ⚫ Secondly, meet the supply of power resources.

<!-- b000157 | prose | pages [6] -->
⚫ Finally meet both water supply and electricity demand.

<!-- b000158 | prose | pages [6] -->
The demand for water resources mainly involves two aspects: the respective withdrawals of the two reservoirs and the distribution of the withdrawn water among the five states. Constraints need to be considered when analysing the model. The model we established is mainly subject to the following constraints.

<!-- b000159 | heading | pages [6] -->
4.1 The optimal transportation

<!-- b000160 | heading | pages [6] -->
4.1.1 Water supply meets requirements

<!-- b000161 | prose | pages [6] -->
Seven states in the Colorado River basin need to meet their water supply, and the amount of water flowing out of the United States needs to meet Mexico's requirements.

<!-- b000162 | prose | pages [6] -->
For the total water demand, through the relevant data of the Colorado River [2]

<!-- b000163 | prose | pages [6] -->
and the distribution map [3] as shown below. We can get the water storage for five states: Arizona (AZ), California (CA), Wyoming (WY), New Mexico (NM), and Colorado (CO).

<!-- b000164 | prose | pages [6] -->
But at the same time, we also noticed that the Colorado River Basin covers more than the five states mentioned above, and two other states, Utah (UT) and Nevada (NV), also participate in the distribution of Colorado River water resources. Because water resources are interconnected and the large amount of water abstraction in the two states, it is unrealistic to ignore the impact of water abstraction in these two states. The final water demand table we obtained is shown in Table 1. In addition, Mexico has a water demand of 1.5MAF.

<!-- b000165 | furniture | pages [6] -->


<!-- b000166 | furniture | pages [6] -->


<!-- b000167 | furniture | pages [6] -->


<!-- b000168 | furniture | pages [6] -->


<!-- b000169 | furniture | pages [6] -->


<!-- b000170 | caption | pages [7] -->
Table 1 Water requirement and proportion

<!-- b000171 | prose | pages [7] -->
Water Requirement (MAF) State Proportion

<!-- b000172 | prose | pages [7] -->
4.400 CA (Lower Basin) 29.3%

<!-- b000173 | prose | pages [7] -->
3.881 CO (Upper Basin) 25.9% 2.800 AZ (Lower Basin) 18.7% 1.725 UT (Upper Basin) 11.5% 1.050 WY (Upper Basin) 7.0% 0.844 NM (Upper Basin) 5.6% 0.300 NV (Lower Basin)

<!-- b000174 | furniture | pages [7] -->


<!-- b000175 | prose | pages [7] -->
2.0%

<!-- b000176 | furniture | pages [7] -->


<!-- b000177 | caption | pages [7] -->
Figure 2 Colorado River Basin Allocations

<!-- b000178 | furniture | pages [7] -->


<!-- b000179 | prose | pages [7] -->
It is also important to note that due to the requirement to divide the pumping volume between the two lakes, the total pumping volume may not equal the total demand in each state. Additional sources of water may be obtained from other sources. Our proposed mathematical model only needs to account for the allocation of water withdrawals from the Colorado River.

<!-- b000180 | prose | pages [7] -->
Based on the above content, the constraint conditions of water supply corresponding to this part are as follows:

<!-- b000181 | prose | pages [7] -->
+ = ( x x ) T D p i , m i , w i

<!-- b000182 | prose | pages [7] -->
D 

<!-- b000183 | prose | pages [7] -->
w M ,

<!-- b000184 | prose | pages [7] -->
T

<!-- b000185 | prose | pages [7] -->
= , , i 1,2...7

<!-- b000186 | furniture | pages [7] -->


<!-- b000187 | prose | pages [7] -->
（1） , ,

<!-- b000188 | prose | pages [7] -->
q q （2）

<!-- b000189 | furniture | pages [7] -->


<!-- b000190 | prose | pages [7] -->
m m

<!-- b000191 | prose | pages [8] -->
In Formula (1), the first half of the equation represents the total water supply of the two reservoirs to State i in time period T, and the right side of the equation represents the water demand of State i.

<!-- b000192 | prose | pages [8] -->
It's a constraint on the water supply in seven states. Equation (2) is an inequality reflecting the requirement that does not affect Mexico's water demand.

<!-- b000193 | heading | pages [8] -->
4.1.2 Constraints on the height of the dam water level

<!-- b000194 | prose | pages [8] -->
As for the water level elevation limitation of Glen Canyon Dam (Lake Powell) and The Hoover Dam (Lake Mead), the following table2 can be obtained through data sorting of the US Bureau of Reclamation[4,5]:

<!-- b000195 | furniture | pages [8] -->


<!-- b000196 | caption | pages [8] -->
Table2 Dam-related attribute values (feet)

<!-- b000197 | prose | pages [8] -->
Glen Canyon Dam Elevation

<!-- b000198 | prose | pages [8] -->
Maximum Water Surface Top of Dead Storage Pool Streambed at Dam Axis

<!-- b000199 | furniture | pages [8] -->


<!-- b000200 | furniture | pages [8] -->


<!-- b000201 | prose | pages [8] -->
Hoover Dam

<!-- b000202 | prose | pages [8] -->
3711.0 1232.0 3370.0 895.0 3132.0 2640.0

<!-- b000203 | furniture | pages [8] -->


<!-- b000204 | caption | pages [8] -->
Figure 3 Schematic diagram of dam and associated elevation

<!-- b000205 | furniture | pages [8] -->


<!-- b000206 | prose | pages [8] -->
h The altitude of the Top of Dead Storage Pool is h . The altitude of the. min . The altitude of the river bed of dam foundation Maximum Water Surface is max h . While meeting the pumping needs of the states, the water levels in the two is base dams should also be limited between

<!-- b000207 | prose | pages [8] -->
inequality constraints:

<!-- b000208 | furniture | pages [8] -->


<!-- b000209 | prose | pages [8] -->
( )

<!-- b000210 | prose | pages [8] -->
 +

<!-- b000211 | prose | pages [8] -->
P P t T

<!-- b000212 | prose | pages [8] -->
min

<!-- b000213 | prose | pages [8] -->
(

<!-- b000214 | prose | pages [8] -->
 +

<!-- b000215 | prose | pages [8] -->
M M t T

<!-- b000216 | prose | pages [8] -->
min

<!-- b000217 | furniture | pages [8] -->


<!-- b000218 | furniture | pages [8] -->


<!-- b000219 | prose | pages [8] -->
h h h and , which results in the following min max

<!-- b000220 | prose | pages [8] -->
 

<!-- b000221 | prose | pages [8] -->
P

<!-- b000222 | prose | pages [8] -->
max

<!-- b000223 | furniture | pages [8] -->


<!-- b000224 | prose | pages [8] -->
（3）

<!-- b000225 | prose | pages [8] -->
) )

<!-- b000226 | prose | pages [8] -->


<!-- b000227 | prose | pages [8] -->
M

<!-- b000228 | prose | pages [8] -->
max

<!-- b000229 | heading | pages [9] -->
4.1.3 Equilibrium constraints on Colorado River recharge and outflow

<!-- b000230 | prose | pages [9] -->
Considering the replenishment and consumption balance of the Colorado River

<!-- b000231 | prose | pages [9] -->
water resources, as well as the mutual constraints between the two DAMS, the reservoir water balance conditions need to be met:

<!-- b000232 | prose | pages [9] -->


<!-- b000233 | prose | pages [9] -->
( )

<!-- b000234 | prose | pages [9] -->
+

<!-- b000235 | prose | pages [9] -->
P t T

<!-- b000236 | prose | pages [9] -->
( )

<!-- b000237 | prose | pages [9] -->


<!-- b000238 | prose | pages [9] -->
= +

<!-- b000239 | prose | pages [9] -->
0

<!-- b000240 | prose | pages [9] -->
S P dP q q

<!-- b000241 | prose | pages [9] -->


<!-- b000242 | prose | pages [9] -->
p p r p

<!-- b000243 | prose | pages [9] -->
( )

<!-- b000244 | prose | pages [9] -->


<!-- b000245 | prose | pages [9] -->
P t

<!-- b000246 | prose | pages [9] -->
0

<!-- b000247 | prose | pages [9] -->


<!-- b000248 | prose | pages [9] -->
( )

<!-- b000249 | prose | pages [9] -->
+

<!-- b000250 | prose | pages [9] -->
M t T

<!-- b000251 | prose | pages [9] -->
( )

<!-- b000252 | prose | pages [9] -->


<!-- b000253 | prose | pages [9] -->
= +

<!-- b000254 | prose | pages [9] -->
0

<!-- b000255 | prose | pages [9] -->
S M dM q

<!-- b000256 | prose | pages [9] -->


<!-- b000257 | prose | pages [9] -->
m m

<!-- b000258 | prose | pages [9] -->
( )

<!-- b000259 | prose | pages [9] -->


<!-- b000260 | prose | pages [9] -->
M t

<!-- b000261 | prose | pages [9] -->
0

<!-- b000262 | prose | pages [9] -->


<!-- b000263 | prose | pages [9] -->
7

<!-- b000264 | prose | pages [9] -->


<!-- b000265 | prose | pages [9] -->
− −

<!-- b000266 | prose | pages [9] -->
q x T

<!-- b000267 | prose | pages [9] -->


<!-- b000268 | prose | pages [9] -->
, ,

<!-- b000269 | prose | pages [9] -->
m p i

<!-- b000270 | prose | pages [9] -->
,

<!-- b000271 | prose | pages [9] -->


<!-- b000272 | prose | pages [9] -->
=

<!-- b000273 | prose | pages [9] -->
i

<!-- b000274 | prose | pages [9] -->
1

<!-- b000275 | furniture | pages [9] -->


<!-- b000276 | prose | pages [9] -->
（4）

<!-- b000277 | prose | pages [9] -->


<!-- b000278 | prose | pages [9] -->
7

<!-- b000279 | prose | pages [9] -->


<!-- b000280 | prose | pages [9] -->
− −

<!-- b000281 | prose | pages [9] -->
q q q x T

<!-- b000282 | prose | pages [9] -->


<!-- b000283 | prose | pages [9] -->
r m

<!-- b000284 | prose | pages [9] -->
,

<!-- b000285 | prose | pages [9] -->
M m i

<!-- b000286 | prose | pages [9] -->
,

<!-- b000287 | prose | pages [9] -->


<!-- b000288 | prose | pages [9] -->
=

<!-- b000289 | prose | pages [9] -->
i

<!-- b000290 | prose | pages [9] -->
1

<!-- b000291 | furniture | pages [9] -->


<!-- b000292 | caption | pages [9] -->
Figure 4 Water level - storage capacity characteristic curve

<!-- b000293 | furniture | pages [9] -->


<!-- b000294 | furniture | pages [9] -->


<!-- b000295 | caption | pages [9] -->
Figure4 shows the relationship between the water level elevation of Lake Mead

<!-- b000296 | prose | pages [9] -->
h ) and the water volume of the reservoir. We obtain the water level (height from the base

<!-- b000297 | prose | pages [9] -->
- storage capacity characteristic curves of two reservoirs in recent ten years.

<!-- b000298 | prose | pages [9] -->
= + y 9.1 e 04* x

<!-- b000299 | prose | pages [9] -->
square = R _

<!-- b000300 | prose | pages [9] -->
− − + 3.1 e 07

<!-- b000301 | furniture | pages [9] -->


<!-- b000302 | prose | pages [9] -->
（5）

<!-- b000303 | prose | pages [9] -->
0.9925

<!-- b000304 | furniture | pages [9] -->


<!-- b000305 | prose | pages [9] -->
It can be seen from the water-level and storage capacity characteristic curves of the two reservoirs in the past decade [6] that the range of changes in the water level and 2 R close to 1. storage capacity of the two lakes can be approximately linear and Therefore, the lake area can be set as a fixed value, which does not change with the change of water level. Then:

<!-- b000306 | furniture | pages [9] -->


<!-- b000307 | prose | pages [9] -->
( ) (

<!-- b000308 | prose | pages [9] -->
+

<!-- b000309 | prose | pages [9] -->
P t T

<!-- b000310 | prose | pages [9] -->
( )

<!-- b000311 | prose | pages [9] -->


<!-- b000312 | prose | pages [9] -->
= 

<!-- b000313 | prose | pages [9] -->
0

<!-- b000314 | prose | pages [9] -->
S P dP S P t

<!-- b000315 | prose | pages [9] -->
p p

<!-- b000316 | prose | pages [9] -->
( )

<!-- b000317 | prose | pages [9] -->
P t

<!-- b000318 | prose | pages [9] -->
0

<!-- b000319 | prose | pages [9] -->
( )

<!-- b000320 | prose | pages [9] -->
+

<!-- b000321 | prose | pages [9] -->
M t T

<!-- b000322 | prose | pages [9] -->
( )

<!-- b000323 | prose | pages [9] -->


<!-- b000324 | prose | pages [9] -->
= 

<!-- b000325 | prose | pages [9] -->
0

<!-- b000326 | prose | pages [9] -->
S M dM S

<!-- b000327 | prose | pages [9] -->
m m

<!-- b000328 | prose | pages [9] -->
( )

<!-- b000329 | prose | pages [9] -->
M t

<!-- b000330 | prose | pages [9] -->
0

<!-- b000331 | furniture | pages [9] -->


<!-- b000332 | prose | pages [9] -->
) ( ( ) ( )

<!-- b000333 | prose | pages [9] -->
+ −

<!-- b000334 | prose | pages [9] -->
T P t

<!-- b000335 | prose | pages [9] -->
0 0 0

<!-- b000336 | furniture | pages [9] -->


<!-- b000337 | prose | pages [9] -->
（6）

<!-- b000338 | prose | pages [9] -->
( ( ) ( ) ( )

<!-- b000339 | prose | pages [9] -->
+ −

<!-- b000340 | prose | pages [9] -->
M t T M t

<!-- b000341 | prose | pages [9] -->
0 0

<!-- b000342 | prose | pages [10] -->
The above equation illustrates the relationship between water level and reservoir volume originally expressed by integration, which degenerates into the product of the difference between water level change and the average surface area of the reservoir.

<!-- b000343 | prose | pages [10] -->
At the same time, the change of reservoir water volume remains conserved. The change of reservoir water quantity is equal to the amount of water flowing into the current reservoir and the increase of water replenished by rainfall in time T minus the amount of evaporation from the reservoir and the reduction of water supply withdrawn from the reservoir in time T.

<!-- b000344 | furniture | pages [10] -->


<!-- b000345 | furniture | pages [10] -->


<!-- b000346 | caption | pages [10] -->
Figure 5 Colorado River reservoir - dam system

<!-- b000347 | prose | pages [10] -->


<!-- b000348 | prose | pages [10] -->
( ) ( ) ( )

<!-- b000349 | prose | pages [10] -->
 + − = +

<!-- b000350 | prose | pages [10] -->
S P t T P t q q

<!-- b000351 | prose | pages [10] -->


<!-- b000352 | prose | pages [10] -->
p

<!-- b000353 | prose | pages [10] -->
0 0

<!-- b000354 | prose | pages [10] -->
p

<!-- b000355 | prose | pages [10] -->
 

<!-- b000356 | prose | pages [10] -->
( ) ( ) ( )

<!-- b000357 | prose | pages [10] -->
 + − = +

<!-- b000358 | prose | pages [10] -->
S M t T M t q

<!-- b000359 | prose | pages [10] -->


<!-- b000360 | prose | pages [10] -->
m

<!-- b000361 | prose | pages [10] -->
0 0

<!-- b000362 | prose | pages [10] -->
m

<!-- b000363 | prose | pages [10] -->


<!-- b000364 | furniture | pages [10] -->


<!-- b000365 | prose | pages [10] -->


<!-- b000366 | prose | pages [10] -->
7

<!-- b000367 | prose | pages [10] -->


<!-- b000368 | prose | pages [10] -->
− − −

<!-- b000369 | prose | pages [10] -->
q q x T

<!-- b000370 | prose | pages [10] -->


<!-- b000371 | prose | pages [10] -->
r p r p

<!-- b000372 | prose | pages [10] -->
, ,

<!-- b000373 | prose | pages [10] -->
e p

<!-- b000374 | prose | pages [10] -->
,

<!-- b000375 | prose | pages [10] -->
m p i

<!-- b000376 | prose | pages [10] -->
,

<!-- b000377 | prose | pages [10] -->


<!-- b000378 | prose | pages [10] -->
=

<!-- b000379 | prose | pages [10] -->
i

<!-- b000380 | prose | pages [10] -->
1

<!-- b000381 | furniture | pages [10] -->


<!-- b000382 | prose | pages [10] -->
（7）

<!-- b000383 | prose | pages [10] -->


<!-- b000384 | prose | pages [10] -->
7

<!-- b000385 | prose | pages [10] -->


<!-- b000386 | prose | pages [10] -->
− − −

<!-- b000387 | prose | pages [10] -->
q q q q x T

<!-- b000388 | prose | pages [10] -->


<!-- b000389 | prose | pages [10] -->
r m

<!-- b000390 | prose | pages [10] -->
,

<!-- b000391 | prose | pages [10] -->
e m

<!-- b000392 | prose | pages [10] -->
, M

<!-- b000393 | prose | pages [10] -->
m i

<!-- b000394 | prose | pages [10] -->
,

<!-- b000395 | prose | pages [10] -->


<!-- b000396 | prose | pages [10] -->
=

<!-- b000397 | prose | pages [10] -->
i

<!-- b000398 | prose | pages [10] -->
1

<!-- b000399 | prose | pages [10] -->
Therefore, equation (3) representing water level control and equation (7) representing access balance can be transformed into the following equation:

<!-- b000400 | prose | pages [10] -->


<!-- b000401 | prose | pages [10] -->
( ) ( )

<!-- b000402 | prose | pages [10] -->
 −  + − −

<!-- b000403 | prose | pages [10] -->
S P t P q q q q

<!-- b000404 | prose | pages [10] -->


<!-- b000405 | prose | pages [10] -->
p

<!-- b000406 | prose | pages [10] -->
0 min

<!-- b000407 | prose | pages [10] -->
p r p

<!-- b000408 | prose | pages [10] -->
,

<!-- b000409 | prose | pages [10] -->
e p

<!-- b000410 | prose | pages [10] -->
,

<!-- b000411 | prose | pages [10] -->
m

<!-- b000412 | prose | pages [10] -->
 

<!-- b000413 | prose | pages [10] -->
( ) ( )

<!-- b000414 | prose | pages [10] -->
 −  + − −

<!-- b000415 | prose | pages [10] -->
S M t M q q q

<!-- b000416 | prose | pages [10] -->


<!-- b000417 | prose | pages [10] -->
m

<!-- b000418 | prose | pages [10] -->
0 min

<!-- b000419 | prose | pages [10] -->
m r m

<!-- b000420 | prose | pages [10] -->
,

<!-- b000421 | prose | pages [10] -->
e m

<!-- b000422 | prose | pages [10] -->
,

<!-- b000423 | prose | pages [10] -->
 

<!-- b000424 | prose | pages [10] -->
7

<!-- b000425 | prose | pages [10] -->
( )

<!-- b000426 | prose | pages [10] -->


<!-- b000427 | prose | pages [10] -->
( )

<!-- b000428 | prose | pages [10] -->
− −   −

<!-- b000429 | prose | pages [10] -->
x T S P P t

<!-- b000430 | prose | pages [10] -->


<!-- b000431 | prose | pages [10] -->
p i

<!-- b000432 | prose | pages [10] -->
,

<!-- b000433 | prose | pages [10] -->
p

<!-- b000434 | prose | pages [10] -->
max 0

<!-- b000435 | prose | pages [10] -->


<!-- b000436 | prose | pages [10] -->
=

<!-- b000437 | prose | pages [10] -->
i

<!-- b000438 | prose | pages [10] -->
1

<!-- b000439 | prose | pages [10] -->
（8）

<!-- b000440 | prose | pages [10] -->


<!-- b000441 | prose | pages [10] -->
7

<!-- b000442 | prose | pages [10] -->
( )

<!-- b000443 | prose | pages [10] -->


<!-- b000444 | prose | pages [10] -->
( )

<!-- b000445 | prose | pages [10] -->
−   −

<!-- b000446 | prose | pages [10] -->
q q x T S M M t

<!-- b000447 | prose | pages [10] -->


<!-- b000448 | prose | pages [10] -->
M M

<!-- b000449 | prose | pages [10] -->
m i

<!-- b000450 | prose | pages [10] -->
,

<!-- b000451 | prose | pages [10] -->
m

<!-- b000452 | prose | pages [10] -->
max 0

<!-- b000453 | prose | pages [10] -->


<!-- b000454 | prose | pages [10] -->
=

<!-- b000455 | prose | pages [10] -->
i

<!-- b000456 | prose | pages [10] -->
1

<!-- b000457 | prose | pages [10] -->
In the equation, the leftmost of the inequality represents the difference between the initial water amount of two reservoirs and the water amount of the dead pool. The middle of the inequality represents the total amount of water flowing in and out, as shown in the system diagram above. The far right of the inequality represents the difference between the maximum water level of two dams and the amount of water below the initial water level.

<!-- b000458 | heading | pages [11] -->
4.1.4 Dam power generation constraint

<!-- b000459 | prose | pages [11] -->
According to the public data provided by the US Reclamation Bureau [4,5], the Installed Capacity of Glen Canyon Powerplant is 1,320,000 kW, and the Installed Capacity of Hoover Powerplant is 2,078,800 kW. The formula is derived from the calculation of water energy:

<!-- b000460 | prose | pages [11] -->
= N AQH

<!-- b000461 | furniture | pages [11] -->


<!-- b000462 | prose | pages [11] -->
（9） net

<!-- b000463 | prose | pages [11] -->
In the formula, N represents the power generation of the hydropower station, A is the output coefficient, and its value is related to the conversion rate of water and electricity. In this problem, the value is 9.81. Q is the amount of water discharged H is the difference between the water level of the upstream reservoir from the dam, net and the riverbed of the dam axis. Since the data does not mention the maximum flow rate of power generation flow, but has the above maximum power generation. Therefore, we obtain the range of the maximum power generation water flow Q by inverse calculation.

<!-- b000464 | furniture | pages [11] -->


<!-- b000465 | prose | pages [11] -->
N

<!-- b000466 | prose | pages [11] -->
max,

<!-- b000467 | prose | pages [11] -->
p

<!-- b000468 | prose | pages [11] -->
= = −

<!-- b000469 | prose | pages [11] -->
160218.01(

<!-- b000470 | prose | pages [11] -->
q

<!-- b000471 | prose | pages [11] -->
m

<!-- b000472 | prose | pages [11] -->
,max

<!-- b000473 | prose | pages [11] -->
−

<!-- b000474 | prose | pages [11] -->
9.81(

<!-- b000475 | prose | pages [11] -->
P h

<!-- b000476 | prose | pages [11] -->
)

<!-- b000477 | prose | pages [11] -->
max

<!-- b000478 | prose | pages [11] -->
base p

<!-- b000479 | prose | pages [11] -->
,

<!-- b000480 | prose | pages [11] -->
N

<!-- b000481 | prose | pages [11] -->
= =

<!-- b000482 | prose | pages [11] -->
max,

<!-- b000483 | prose | pages [11] -->
m

<!-- b000484 | prose | pages [11] -->
acre feet per month

<!-- b000485 | furniture | pages [11] -->


<!-- b000486 | furniture | pages [11] -->


<!-- b000487 | prose | pages [11] -->
)

<!-- b000488 | furniture | pages [11] -->


<!-- b000489 | prose | pages [11] -->
（10）

<!-- b000490 | prose | pages [11] -->
−

<!-- b000491 | prose | pages [11] -->
253627.06(

<!-- b000492 | prose | pages [11] -->
q

<!-- b000493 | prose | pages [11] -->
M

<!-- b000494 | prose | pages [11] -->
,max

<!-- b000495 | prose | pages [11] -->
−

<!-- b000496 | prose | pages [11] -->
9.81(

<!-- b000497 | prose | pages [11] -->
M h

<!-- b000498 | prose | pages [11] -->
)

<!-- b000499 | prose | pages [11] -->
max

<!-- b000500 | prose | pages [11] -->
base m

<!-- b000501 | prose | pages [11] -->
,

<!-- b000502 | prose | pages [11] -->
acre feet per month

<!-- b000503 | furniture | pages [11] -->


<!-- b000504 | furniture | pages [11] -->


<!-- b000505 | prose | pages [11] -->
)

<!-- b000506 | prose | pages [11] -->
Therefore, there is a constraint on the flow of water out of the dam q :

<!-- b000507 | prose | pages [11] -->
 

<!-- b000508 | prose | pages [11] -->
0

<!-- b000509 | prose | pages [11] -->
q q

<!-- b000510 | prose | pages [11] -->
m m

<!-- b000511 | prose | pages [11] -->
 

<!-- b000512 | prose | pages [11] -->
0

<!-- b000513 | prose | pages [11] -->
q q

<!-- b000514 | prose | pages [11] -->
M

<!-- b000515 | heading | pages [11] -->
4.1.5 Objective function

<!-- b000516 | prose | pages [11] -->
,max

<!-- b000517 | furniture | pages [11] -->


<!-- b000518 | prose | pages [11] -->
（11）

<!-- b000519 | prose | pages [11] -->
M M

<!-- b000520 | prose | pages [11] -->
,max

<!-- b000521 | prose | pages [11] -->
Considering that there may be no unique solution to this problem, optimization objectives need to be added to this mathematical model to determine the optimal solution, so we turn our attention to the objective function of minimum cost related to water resources allocation.

<!-- b000522 | prose | pages [11] -->
For the allocation of water resources, we regard it as a warehouse transportation problem, taking the dams corresponding to the two reservoirs as the water intake points, and the water levels P and M of the two reservoirs as the water stock indicators. Since the center of gravity of water demand in each state is different and difficult to determine, we use the geographic center of gravity of the seven states as the destination of water allocation to simplify the problem, and use

<!-- b000523 | prose | pages [11] -->
the transportation distance as the transportation cost. The length of each connection is shown in the table below:

<!-- b000524 | furniture | pages [11] -->


<!-- b000525 | furniture | pages [12] -->


<!-- b000526 | caption | pages [12] -->
Figure 6: water resource allocation

<!-- b000527 | caption | pages [12] -->
Table 3 Transportation distance by state (mile)

<!-- b000528 | prose | pages [12] -->
Glen Canyon dam STATE Hoover dam

<!-- b000529 | prose | pages [12] -->
562.756 CA 353.238

<!-- b000530 | prose | pages [12] -->
225.368 AZ 257.871

<!-- b000531 | prose | pages [12] -->
429.163 NM 612.090

<!-- b000532 | prose | pages [12] -->
448.691 CO 686.919

<!-- b000533 | prose | pages [12] -->
613.939 WY 802.099

<!-- b000534 | prose | pages [12] -->
210.327 UT 358.346

<!-- b000535 | prose | pages [12] -->
320.672 NV 320.672

<!-- b000536 | prose | pages [12] -->
According to the above basic conditions, we can start to build the optimization model. The objective function of water allocation cost in seven states is as follows:

<!-- b000537 | prose | pages [12] -->
7

<!-- b000538 | prose | pages [12] -->
 +

<!-- b000539 | prose | pages [12] -->
C = ( d x p i , p i ,

<!-- b000540 | prose | pages [12] -->
=

<!-- b000541 | prose | pages [12] -->
i 1

<!-- b000542 | heading | pages [12] -->
4.1.6 Model solving

<!-- b000543 | prose | pages [12] -->
d d x ) k T

<!-- b000544 | furniture | pages [12] -->


<!-- b000545 | prose | pages [12] -->
（12）

<!-- b000546 | prose | pages [12] -->
m i , , m i , i

<!-- b000547 | prose | pages [12] -->
In summary, the simplified objective function and constraints can be obtained as

<!-- b000548 | prose | pages [12] -->
follows:

<!-- b000549 | prose | pages [12] -->
7

<!-- b000550 | prose | pages [12] -->


<!-- b000551 | prose | pages [12] -->
+

<!-- b000552 | prose | pages [12] -->
Min C

<!-- b000553 | prose | pages [12] -->
= (

<!-- b000554 | prose | pages [12] -->
d x d x

<!-- b000555 | prose | pages [12] -->
)

<!-- b000556 | prose | pages [12] -->
T

<!-- b000557 | prose | pages [12] -->
p i

<!-- b000558 | prose | pages [12] -->
,

<!-- b000559 | prose | pages [12] -->
p i

<!-- b000560 | prose | pages [12] -->
,

<!-- b000561 | prose | pages [12] -->
m i

<!-- b000562 | prose | pages [12] -->
,

<!-- b000563 | prose | pages [12] -->
m i

<!-- b000564 | prose | pages [12] -->
,

<!-- b000565 | prose | pages [12] -->
=

<!-- b000566 | prose | pages [12] -->
i

<!-- b000567 | prose | pages [12] -->
1

<!-- b000568 | prose | pages [12] -->
s t

<!-- b000569 | prose | pages [12] -->
. :

<!-- b000570 | prose | pages [12] -->
+ = =

<!-- b000571 | prose | pages [12] -->
(

<!-- b000572 | prose | pages [12] -->
x x

<!-- b000573 | prose | pages [12] -->
)

<!-- b000574 | prose | pages [12] -->
T D

<!-- b000575 | prose | pages [12] -->
,

<!-- b000576 | prose | pages [12] -->
i

<!-- b000577 | prose | pages [12] -->
1,2...7

<!-- b000578 | prose | pages [12] -->
p i

<!-- b000579 | prose | pages [12] -->
,

<!-- b000580 | prose | pages [12] -->
m i

<!-- b000581 | prose | pages [12] -->
,

<!-- b000582 | prose | pages [12] -->
w i

<!-- b000583 | prose | pages [12] -->
,

<!-- b000584 | prose | pages [12] -->


<!-- b000585 | prose | pages [12] -->
( )

<!-- b000586 | prose | pages [12] -->
 + + − −

<!-- b000587 | prose | pages [12] -->
S P S P t q q q

<!-- b000588 | prose | pages [12] -->


<!-- b000589 | prose | pages [12] -->
p

<!-- b000590 | prose | pages [12] -->
min

<!-- b000591 | prose | pages [12] -->
p

<!-- b000592 | prose | pages [12] -->
0

<!-- b000593 | prose | pages [12] -->
p r p

<!-- b000594 | prose | pages [12] -->
,

<!-- b000595 | prose | pages [12] -->
m

<!-- b000596 | prose | pages [12] -->
 

<!-- b000597 | prose | pages [12] -->
( )

<!-- b000598 | prose | pages [12] -->
 + + −

<!-- b000599 | prose | pages [12] -->
S M S M t q q q

<!-- b000600 | prose | pages [12] -->


<!-- b000601 | prose | pages [12] -->
m

<!-- b000602 | prose | pages [12] -->
min

<!-- b000603 | prose | pages [12] -->
m

<!-- b000604 | prose | pages [12] -->
0

<!-- b000605 | prose | pages [12] -->
m r m

<!-- b000606 | prose | pages [12] -->
,

<!-- b000607 | prose | pages [12] -->
M

<!-- b000608 | prose | pages [12] -->


<!-- b000609 | prose | pages [12] -->
D

<!-- b000610 | prose | pages [12] -->
 

<!-- b000611 | prose | pages [12] -->
w M

<!-- b000612 | prose | pages [12] -->
,

<!-- b000613 | prose | pages [12] -->
q q

<!-- b000614 | prose | pages [12] -->
m m

<!-- b000615 | prose | pages [12] -->
,max

<!-- b000616 | prose | pages [12] -->
T

<!-- b000617 | prose | pages [12] -->
 

<!-- b000618 | prose | pages [12] -->
0

<!-- b000619 | prose | pages [12] -->
q q

<!-- b000620 | prose | pages [12] -->
M M

<!-- b000621 | prose | pages [12] -->
,max

<!-- b000622 | prose | pages [12] -->


<!-- b000623 | prose | pages [12] -->
7

<!-- b000624 | prose | pages [12] -->


<!-- b000625 | prose | pages [12] -->
− 

<!-- b000626 | prose | pages [12] -->
q q x T S P

<!-- b000627 | furniture | pages [12] -->


<!-- b000628 | prose | pages [12] -->


<!-- b000629 | prose | pages [12] -->
e p

<!-- b000630 | prose | pages [12] -->
, ,

<!-- b000631 | prose | pages [12] -->
p i

<!-- b000632 | prose | pages [12] -->
,

<!-- b000633 | prose | pages [12] -->
p

<!-- b000634 | prose | pages [12] -->
max

<!-- b000635 | prose | pages [12] -->


<!-- b000636 | prose | pages [12] -->
（13）

<!-- b000637 | prose | pages [12] -->
=

<!-- b000638 | prose | pages [12] -->
i

<!-- b000639 | prose | pages [12] -->
1

<!-- b000640 | prose | pages [12] -->


<!-- b000641 | prose | pages [12] -->
7

<!-- b000642 | prose | pages [12] -->


<!-- b000643 | prose | pages [12] -->
− − − 

<!-- b000644 | prose | pages [12] -->
q x T S M

<!-- b000645 | prose | pages [12] -->


<!-- b000646 | prose | pages [12] -->
e m

<!-- b000647 | prose | pages [12] -->
,

<!-- b000648 | prose | pages [12] -->
m i

<!-- b000649 | prose | pages [12] -->
,

<!-- b000650 | prose | pages [12] -->
m

<!-- b000651 | prose | pages [12] -->
max

<!-- b000652 | prose | pages [12] -->


<!-- b000653 | prose | pages [12] -->
=

<!-- b000654 | prose | pages [12] -->
i

<!-- b000655 | prose | pages [12] -->
1

<!-- b000656 | prose | pages [13] -->
The water surface data, flow data and rainfall data of the two lakes in January 2021 are selected as the test. It is assumed that the water transfer time is one month, and the transportation cost per unit distance per unit water flow in each state is the same. Then

<!-- b000657 | prose | pages [13] -->
the water resource allocation scheme corresponding to the minimum transportation cost can be obtained.

<!-- b000658 | caption | pages [13] -->
Table4 Basic data for January 2021

<!-- b000659 | furniture | pages [13] -->


<!-- b000660 | prose | pages [13] -->
CA AZ NM CO

<!-- b000661 | prose | pages [13] -->
Lake 0 233333 70333.3 323417 Powell

<!-- b000662 | prose | pages [13] -->
Lake 366666.7 0 0 0 Mead

<!-- b000663 | furniture | pages [13] -->


<!-- b000664 | prose | pages [13] -->
Lake WY UT NV Mexico Mead

<!-- b000665 | prose | pages [13] -->
87500 143750 0 0 —

<!-- b000666 | prose | pages [13] -->
0 0 25000 — 125000

<!-- b000667 | heading | pages [13] -->
4.2 Optimal duration of water allocation

<!-- b000668 | prose | pages [13] -->
Given that demand is fixed, it can be assumed that each state has a fixed monthly water requirement, since there is no additional rainfall water supply. Then, the total monthly water inflow of the two lakes is:

<!-- b000669 | prose | pages [13] -->
D

<!-- b000670 | prose | pages [13] -->
7

<!-- b000671 | prose | pages [13] -->
− = − − −

<!-- b000672 | prose | pages [13] -->
w i

<!-- b000673 | prose | pages [13] -->
,

<!-- b000674 | prose | pages [13] -->
=-1106074.571

<!-- b000675 | prose | pages [13] -->
q q q q q

<!-- b000676 | prose | pages [13] -->
p e p

<!-- b000677 | prose | pages [13] -->
,

<!-- b000678 | prose | pages [13] -->
M e m

<!-- b000679 | prose | pages [13] -->
,

<!-- b000680 | prose | pages [13] -->
T =

<!-- b000681 | prose | pages [13] -->
i

<!-- b000682 | prose | pages [13] -->
1

<!-- b000683 | prose | pages [13] -->
 q <0 It can be seen that

<!-- b000684 | prose | pages [13] -->
acre

<!-- b000685 | prose | pages [13] -->
-

<!-- b000686 | prose | pages [13] -->
feet per month

<!-- b000687 | furniture | pages [13] -->


<!-- b000688 | furniture | pages [13] -->


<!-- b000689 | furniture | pages [13] -->


<!-- b000690 | prose | pages [13] -->
（14）

<!-- b000691 | prose | pages [13] -->
, the total water volume of the two reservoirs is constantly

<!-- b000692 | prose | pages [13] -->
decreasing. Water resource scheduling ends when the available water stocks in the lake are insufficient to meet the water needs of individual states. Considering the month as the unit dispatching time, the above water resources optimal dispatching model is used circularly and the reservoir water level after dispatching is updated. When there is no feasible solution to the water resources optimal dispatching model, the number of cycles obtained is the duration of dispatching.

<!-- b000693 | prose | pages [13] -->
The scheduling process and results are as follows:

<!-- b000694 | furniture | pages [13] -->


<!-- b000695 | furniture | pages [14] -->


<!-- b000696 | caption | pages [14] -->
Figure 7 Water resource scheduling process

<!-- b000697 | prose | pages [14] -->
According to the figure above, the duration of water dispatching is 23 months.

<!-- b000698 | furniture | pages [14] -->


<!-- b000699 | heading | pages [14] -->
4.3 The relationship of external water transfer with time

<!-- b000700 | prose | pages [14] -->
As can be seen from the previous content, when there is no additional water supply,

<!-- b000701 | prose | pages [14] -->
the resources of the reservoir cannot meet the water demand of each state in the 24th month. At this time, the remaining available storage capacity of the two reservoirs is 0 and 54199.52 acre-ft respectively; and the total monthly water demand of the user is

<!-- b000702 | heading | pages [14] -->
1375000.00 acre-ft, so at least 1375000.00-54199.52-0=1320800.48 acre-ft of water

<!-- b000703 | prose | pages [14] -->
needs to be transferred.

<!-- b000704 | prose | pages [14] -->
Since then, the two reservoirs have no usable stock. In order to ensure water −= q -1106074.571 acre feet - demand, the minimum monthly water diversion is

<!-- b000705 | furniture | pages [14] -->


<!-- b000706 | prose | pages [14] -->
.

<!-- b000707 | heading | pages [14] -->
5. Models and solutions of problem 2

<!-- b000708 | prose | pages [14] -->
Considering the competitive interests of agricultural, industrial, residential and electricity production water, as well as the transportation costs of water resources, we establish a two-stage model.

<!-- b000709 | prose | pages [14] -->
On the basis of satisfying the residential water consumption of each state, the lower-level model introduces the agricultural water efficiency and industrial water

<!-- b000710 | prose | pages [14] -->
efficiency functions of each state.

<!-- b000711 | prose | pages [14] -->
Taking the total production benefit of seven states and the dam power production benefit as the objective function, the maximization optimization model of total production benefit is established to solve the agricultural and industrial water consumption of each state. The upper layer model considers the transportation cost

<!-- b000712 | prose | pages [15] -->
between the reservoir and each state, while the lower layer model considers the water consumption of each state and the amount of water pumped from the reservoir as the demand and constraint, establishes the transportation cost minimization optimization

<!-- b000713 | prose | pages [15] -->
model, and obtains the water extracted from the two reservoirs by seven states respectively.

<!-- b000714 | heading | pages [15] -->
5.1 Lower-level model construction

<!-- b000715 | prose | pages [15] -->
If a more accurate solution is adopted according to the resources required per unit production value of each state, the decisional variables of the objective function of the model will reach 18. There are 14 variables related to gross agricultural and industrial production and 4 variables related to dam and reservoir systems. Therefore, we comprehensively calculated the agricultural and industrial GDP of each state, the following formula:

<!-- b000716 | prose | pages [15] -->
7

<!-- b000717 | prose | pages [15] -->


<!-- b000718 | prose | pages [15] -->
=

<!-- b000719 | prose | pages [15] -->
A A

<!-- b000720 | prose | pages [15] -->
=

<!-- b000721 | prose | pages [15] -->
i

<!-- b000722 | prose | pages [15] -->
1

<!-- b000723 | prose | pages [15] -->
7

<!-- b000724 | prose | pages [15] -->


<!-- b000725 | prose | pages [15] -->
=

<!-- b000726 | prose | pages [15] -->
I I

<!-- b000727 | prose | pages [15] -->
=

<!-- b000728 | prose | pages [15] -->
i

<!-- b000729 | prose | pages [15] -->
1

<!-- b000730 | prose | pages [15] -->
7

<!-- b000731 | prose | pages [15] -->


<!-- b000732 | prose | pages [15] -->
( )

<!-- b000733 | prose | pages [15] -->
+ +

<!-- b000734 | prose | pages [15] -->
max Z =

<!-- b000735 | prose | pages [15] -->
A I T

<!-- b000736 | prose | pages [15] -->
i i

<!-- b000737 | prose | pages [15] -->
=

<!-- b000738 | prose | pages [15] -->
i 1

<!-- b000739 | prose | pages [15] -->
i i

<!-- b000740 | furniture | pages [15] -->


<!-- b000741 | furniture | pages [15] -->


<!-- b000742 | prose | pages [15] -->
（15）

<!-- b000743 | prose | pages [15] -->
i i

<!-- b000744 | prose | pages [15] -->
( )

<!-- b000745 | prose | pages [15] -->
 

<!-- b000746 | prose | pages [15] -->
+ −

<!-- b000747 | prose | pages [15] -->
E E E

<!-- b000748 | furniture | pages [15] -->


<!-- b000749 | prose | pages [15] -->
（16）

<!-- b000750 | prose | pages [15] -->
p m T

<!-- b000751 | prose | pages [15] -->
The object function is to maximize the agricultural effectiveness and the remaining electricity effectiveness as A, I; the water cost electricity cost effectiveness of the remaining water pumping.  and  representing the electricity price and average water price. The reason for the occurrence of excessing hydropower is mainly due to the assumption that the general electricity and water consumption (agricultural, industrial and residential) is proportional to a certain proportion, and the electricity and water quantities are often not allocated exactly.

<!-- b000752 | prose | pages [15] -->
The constraints of the lower model are similar to the first question, as follows: ⚫ Equation constraints of dam power generation and electricity demand:

<!-- b000753 | furniture | pages [15] -->


<!-- b000754 | prose | pages [15] -->
(

<!-- b000755 | prose | pages [15] -->
 +

<!-- b000756 | prose | pages [15] -->
q

<!-- b000757 | prose | pages [15] -->
( )

<!-- b000758 | prose | pages [15] -->
p

<!-- b000759 | prose | pages [15] -->
 = − +

<!-- b000760 | prose | pages [15] -->
E Aq P t

<!-- b000761 | prose | pages [15] -->
( )

<!-- b000762 | prose | pages [15] -->
H T

<!-- b000763 | prose | pages [15] -->


<!-- b000764 | prose | pages [15] -->
p m

<!-- b000765 | prose | pages [15] -->
0

<!-- b000766 | prose | pages [15] -->
p

<!-- b000767 | prose | pages [15] -->


<!-- b000768 | prose | pages [15] -->
(

<!-- b000769 | prose | pages [15] -->


<!-- b000770 | prose | pages [15] -->
q

<!-- b000771 | prose | pages [15] -->
( )

<!-- b000772 | prose | pages [15] -->
m

<!-- b000773 | prose | pages [15] -->
= − + 

<!-- b000774 | prose | pages [15] -->
E Aq M t

<!-- b000775 | prose | pages [15] -->
( )

<!-- b000776 | prose | pages [15] -->
H T

<!-- b000777 | prose | pages [15] -->


<!-- b000778 | prose | pages [15] -->
m M

<!-- b000779 | prose | pages [15] -->
0

<!-- b000780 | prose | pages [15] -->
m

<!-- b000781 | prose | pages [15] -->


<!-- b000782 | prose | pages [15] -->
( )

<!-- b000783 | prose | pages [15] -->
= + +

<!-- b000784 | prose | pages [15] -->
E e A e I e p T

<!-- b000785 | prose | pages [15] -->
T A I R

<!-- b000786 | furniture | pages [15] -->


<!-- b000787 | prose | pages [15] -->
)

<!-- b000788 | prose | pages [15] -->
 − − −

<!-- b000789 | prose | pages [15] -->
3

<!-- b000790 | prose | pages [15] -->
q q q q W T

<!-- b000791 | prose | pages [15] -->
r p

<!-- b000792 | prose | pages [15] -->
, ,

<!-- b000793 | prose | pages [15] -->
m e p

<!-- b000794 | prose | pages [15] -->
,

<!-- b000795 | prose | pages [15] -->
p

<!-- b000796 | prose | pages [15] -->
 

<!-- b000797 | prose | pages [15] -->
2

<!-- b000798 | prose | pages [15] -->
S

<!-- b000799 | prose | pages [15] -->


<!-- b000800 | prose | pages [15] -->
p

<!-- b000801 | prose | pages [15] -->
)

<!-- b000802 | prose | pages [15] -->
 + + − − −

<!-- b000803 | prose | pages [15] -->
3

<!-- b000804 | prose | pages [15] -->
（17）

<!-- b000805 | prose | pages [15] -->
q q q W T

<!-- b000806 | prose | pages [15] -->
r m

<!-- b000807 | prose | pages [15] -->
,

<!-- b000808 | prose | pages [15] -->
M e m

<!-- b000809 | prose | pages [15] -->
,

<!-- b000810 | prose | pages [15] -->
m

<!-- b000811 | prose | pages [15] -->


<!-- b000812 | furniture | pages [15] -->


<!-- b000813 | prose | pages [15] -->


<!-- b000814 | prose | pages [15] -->
2

<!-- b000815 | prose | pages [15] -->
S

<!-- b000816 | prose | pages [15] -->


<!-- b000817 | prose | pages [15] -->
m

<!-- b000818 | prose | pages [15] -->
⚫ The amount of water withdrawn from the two reservoirs and the supply-demand

<!-- b000819 | prose | pages [15] -->
balance conditions for agricultural, industrial and residential water usage during

<!-- b000820 | prose | pages [15] -->
the operation:

<!-- b000821 | prose | pages [16] -->
+  + + w w w A w I w p

<!-- b000822 | furniture | pages [16] -->


<!-- b000823 | prose | pages [16] -->
（18） p m A I R

<!-- b000824 | prose | pages [16] -->
⚫ Boundary conditions for agricultural and industrial production effectiveness:

<!-- b000825 | prose | pages [16] -->
A I  , 0

<!-- b000826 | furniture | pages [16] -->


<!-- b000827 | prose | pages [16] -->
（19）

<!-- b000828 | prose | pages [16] -->
⚫ For reservoir water level constraints and dam outlet flow constraints, see the

<!-- b000829 | prose | pages [16] -->
corresponding constraints in the first question.

<!-- b000830 | heading | pages [16] -->
5.2 Lower model solution

<!-- b000831 | prose | pages [16] -->
Considering this model is a nonlinear optimization problem, and the traditional method is not easy to solve, we use genetic algorithm to get best solution.

<!-- b000832 | prose | pages [16] -->
Genetic Algorithm (GA) is a computational model that simulates the natural selection of Darwin's theory of biological evolution and the biological evolution process of the genetic mechanism. It is a method to search for optimal solutions by simulating the natural evolution process.

<!-- b000833 | prose | pages [16] -->
The algorithm class we adopted in our first step implements a genetic algorithm that enhances elite retention. The algorithm flow is as follows: 1) Initialize the population of N individuals according to the coding rules. 2) Stop if the stop condition is met, otherwise continue to execute. 3) Statistical analysis of the current population, such as recording its optimal individual, average fitness, etc. 4) Independently select N mothers from the current population. 5) Perform the crossover operation on these N mothers independently. 6) Independently mutate the N crossover individuals. 7) Combine the parent population and the population obtained by crossover mutation to obtain a population with a size of 2N. 8) Select N individuals from the combined population according to the selection algorithm to obtain a new generation of population. 9) Go back to step 2. The algorithm should set a larger probability of crossover and mutation, otherwise there will be more and more repeated individuals in the new generation population generated.

<!-- b000834 | prose | pages [16] -->
The optimal solution and optimal value calculated in the first part are substituted into the single-objective differential evolution algorithm to solve. The main difference between the algorithm flow and the above algorithm is as follows: 1) The current-to- best method is used to select each vector of the differential mutation, and for the current, the population is subjected to differential mutation to obtain mutant individuals. 2) Combine the current population and mutant individuals, and use the binomial distribution crossover method to obtain the test population. 3) Using the one-to-one survivor selection method between the current population and the experimental population to obtain a new generation population.

<!-- b000835 | prose | pages [16] -->
The basic parameters used by the genetic algorithm to enhance elite retention in this model are the population size of 200, the stagnation threshold for single-objective optimization is 1e-6, and the maximum upper limit of the evolutionary stagnation counter is 500; in the second part, the single-objective differential evolution In the solution of the algorithm, the differential evolution parameter F is 0.7, the crossover probability is 0.7, and the rest are the same as the first part of the algorithm. The original

<!-- b000836 | prose | pages [17] -->
data used by the model is as follows [2].

<!-- b000837 | furniture | pages [17] -->


<!-- b000838 | caption | pages [17] -->
Table5 General water and electricity basic data

<!-- b000839 | prose | pages [17] -->
w p w w

<!-- b000840 | furniture | pages [17] -->


<!-- b000841 | prose | pages [17] -->
A I

<!-- b000842 | prose | pages [17] -->
acre-

<!-- b000843 | prose | pages [17] -->
acre-

<!-- b000844 | prose | pages [17] -->
acre-

<!-- b000845 | prose | pages [17] -->
Unit

<!-- b000846 | prose | pages [17] -->
feet/(dollar-

<!-- b000847 | prose | pages [17] -->
feet/(dollar-

<!-- b000848 | prose | pages [17] -->
e Ie Re p R R A

<!-- b000849 | prose | pages [17] -->
Kwh/(dollar-

<!-- b000850 | prose | pages [17] -->
Kwh/(dollar-

<!-- b000851 | prose | pages [17] -->
Kwh/month

<!-- b000852 | prose | pages [17] -->
feet/month

<!-- b000853 | prose | pages [17] -->
year)

<!-- b000854 | prose | pages [17] -->
year)

<!-- b000855 | prose | pages [17] -->
year)

<!-- b000856 | prose | pages [17] -->
year)

<!-- b000857 | prose | pages [17] -->
1723320 CA 0.000542696 0.000005641 0.114796028 0.150928147 7293666667

<!-- b000858 | prose | pages [17] -->
1073697 AZ 0.001144970 0.000000919 0.533816413 0.461587407 2893333333

<!-- b000859 | prose | pages [17] -->
650427 NM 0.000518059 0.000003299 0.157604499 2.983333333 572666667

<!-- b000860 | prose | pages [17] -->
1768389 CO 0.000512741 0.000014216 0.153402536 0.599208144 1617083333

<!-- b000861 | prose | pages [17] -->
639581 WY 0.001541188 0.000018583 0.114617435 5.329381443 237416667

<!-- b000862 | prose | pages [17] -->
1299426 UT 0.001265428 0.000029644 0.313739157 0.471251241 811666667

<!-- b000863 | prose | pages [17] -->
562958 NV 0.002884264 0.000003058

<!-- b000864 | furniture | pages [17] -->


<!-- b000865 | prose | pages [17] -->
1.144706228 1.484587813 1072333333

<!-- b000866 | prose | pages [17] -->
Through the two genetic algorithm model solutions, the optimal value change curve of the second part is as follows:

<!-- b000867 | furniture | pages [17] -->


<!-- b000868 | caption | pages [17] -->
Figure8 Best objective Value Trace Plot (Best value is 4.61e^10)

<!-- b000869 | furniture | pages [17] -->


<!-- b000870 | prose | pages [17] -->
It can be seen that the model basically obtains the optimal solution after the 200th iteration, and the final result of stopping the iteration is 4.61e^10 (dollar). The rest of the results are shown in the table below:

<!-- b000871 | furniture | pages [17] -->


<!-- b000872 | furniture | pages [17] -->


<!-- b000873 | furniture | pages [17] -->


<!-- b000874 | furniture | pages [17] -->


<!-- b000875 | furniture | pages [17] -->


<!-- b000876 | furniture | pages [17] -->


<!-- b000877 | furniture | pages [17] -->


<!-- b000878 | caption | pages [18] -->
Table6 The results of variables

<!-- b000879 | prose | pages [18] -->
PARAMETER UNIT dollar A dollar I

<!-- b000880 | prose | pages [18] -->
q

<!-- b000881 | heading | pages [18] -->
RESULT

<!-- b000882 | prose | pages [18] -->
4122087017.49 0.00

<!-- b000883 | prose | pages [18] -->
acre-feet/month m

<!-- b000884 | prose | pages [18] -->
w

<!-- b000885 | prose | pages [18] -->
160218.01

<!-- b000886 | prose | pages [18] -->
acre-feet/month p

<!-- b000887 | prose | pages [18] -->
q

<!-- b000888 | prose | pages [18] -->
3901904.00

<!-- b000889 | prose | pages [18] -->
acre-feet/month M

<!-- b000890 | prose | pages [18] -->
w

<!-- b000891 | prose | pages [18] -->
253627.06

<!-- b000892 | prose | pages [18] -->
acre-feet/month m 2425104.00

<!-- b000893 | heading | pages [18] -->
5.3 Upper-level model construction

<!-- b000894 | prose | pages [18] -->
The total resources obtained from lower-level model, which are allocated using a model similar to the first question to simplify the mathematical model.

<!-- b000895 | prose | pages [18] -->
The objective function is:

<!-- b000896 | prose | pages [18] -->
7

<!-- b000897 | prose | pages [18] -->


<!-- b000898 | prose | pages [18] -->
Min C = ( d x p i , p i

<!-- b000899 | prose | pages [18] -->
=

<!-- b000900 | prose | pages [18] -->
i 1

<!-- b000901 | prose | pages [18] -->
Constraint:

<!-- b000902 | prose | pages [18] -->
+ +

<!-- b000903 | prose | pages [18] -->
d x ) T

<!-- b000904 | furniture | pages [18] -->


<!-- b000905 | prose | pages [18] -->
（20）

<!-- b000906 | prose | pages [18] -->
, , m i , m i ,

<!-- b000907 | prose | pages [18] -->
（1）Water demand conditions for each state

<!-- b000908 | prose | pages [18] -->
+ =

<!-- b000909 | prose | pages [18] -->
(

<!-- b000910 | prose | pages [18] -->
x x

<!-- b000911 | prose | pages [18] -->
)

<!-- b000912 | prose | pages [18] -->
T D

<!-- b000913 | prose | pages [18] -->
p i

<!-- b000914 | prose | pages [18] -->
,

<!-- b000915 | prose | pages [18] -->
m i

<!-- b000916 | prose | pages [18] -->
,

<!-- b000917 | prose | pages [18] -->
w i

<!-- b000918 | prose | pages [18] -->
,

<!-- b000919 | prose | pages [18] -->
(

<!-- b000920 | prose | pages [18] -->
= +

<!-- b000921 | prose | pages [18] -->
D w A w I

<!-- b000922 | prose | pages [18] -->
w i

<!-- b000923 | prose | pages [18] -->
,

<!-- b000924 | prose | pages [18] -->
A i

<!-- b000925 | prose | pages [18] -->
,

<!-- b000926 | prose | pages [18] -->
i I i

<!-- b000927 | prose | pages [18] -->
,

<!-- b000928 | prose | pages [18] -->
=

<!-- b000929 | prose | pages [18] -->
, ,

<!-- b000930 | prose | pages [18] -->
i

<!-- b000931 | prose | pages [18] -->
1,2...7

<!-- b000932 | furniture | pages [18] -->


<!-- b000933 | prose | pages [18] -->
（21）

<!-- b000934 | prose | pages [18] -->
)

<!-- b000935 | prose | pages [18] -->
+

<!-- b000936 | prose | pages [18] -->
w p T

<!-- b000937 | prose | pages [18] -->
i i R i

<!-- b000938 | prose | pages [18] -->
,

<!-- b000939 | prose | pages [18] -->
i

<!-- b000940 | prose | pages [18] -->
（2）Reservoir water supply conditions:

<!-- b000941 | prose | pages [18] -->
7

<!-- b000942 | prose | pages [18] -->


<!-- b000943 | prose | pages [18] -->
=

<!-- b000944 | prose | pages [18] -->
x W

<!-- b000945 | prose | pages [18] -->
p i

<!-- b000946 | prose | pages [18] -->
,

<!-- b000947 | prose | pages [18] -->
=

<!-- b000948 | prose | pages [18] -->
i

<!-- b000949 | prose | pages [18] -->
1

<!-- b000950 | prose | pages [18] -->
7

<!-- b000951 | prose | pages [18] -->


<!-- b000952 | prose | pages [18] -->
=

<!-- b000953 | prose | pages [18] -->
x

<!-- b000954 | prose | pages [18] -->
m i

<!-- b000955 | prose | pages [18] -->
,

<!-- b000956 | prose | pages [18] -->
=

<!-- b000957 | prose | pages [18] -->
i

<!-- b000958 | prose | pages [18] -->
1

<!-- b000959 | prose | pages [18] -->
p p

<!-- b000960 | furniture | pages [18] -->


<!-- b000961 | prose | pages [18] -->
（22）

<!-- b000962 | prose | pages [18] -->
W W

<!-- b000963 | prose | pages [18] -->
m m

<!-- b000964 | heading | pages [18] -->
5.4 The final result of the upper model

<!-- b000965 | caption | pages [18] -->
Table7 Water Allocation Results by State (arce-feet)

<!-- b000966 | furniture | pages [18] -->


<!-- b000967 | prose | pages [18] -->
Lake Powell

<!-- b000968 | prose | pages [18] -->
CA

<!-- b000969 | prose | pages [18] -->
Lake Mead

<!-- b000970 | prose | pages [18] -->
0 0 2988144.83 537806.912 AZ 0

<!-- b000971 | prose | pages [18] -->
163131.647 NM 0

<!-- b000972 | prose | pages [18] -->
468407.551 CO 0 276657.046 WY 0 283708.325 UT NV 0 0 0 234151.097

<!-- b000973 | heading | pages [19] -->
6. Models and solutions of problem 3

<!-- b000974 | prose | pages [19] -->
If there is not enough water to meet all water and electricity needs, such as extreme dry weather, and minimum water and electricity demands cannot be met, only the equitable distribution of each state is considered without considering economic benefits, and the possible replenishment of water from the outside is not taken into account in our model. Therefore, we consider reducing the consumption of additional resources as much as possible under the minimum water and electricity consumption in a long-term drought. According to the model in the previous question, we change its objective function to be:

<!-- b000975 | prose | pages [19] -->
( )  + − min Z = E E E p m T ,min ( ) + +  + − W W W

<!-- b000976 | furniture | pages [19] -->


<!-- b000977 | prose | pages [19] -->
（23） p m T ,min

<!-- b000978 | prose | pages [19] -->
The economic value of water and electricity we use represents the size of the

<!-- b000979 | prose | pages [19] -->
abundant part of resources.and are the average unit electricity and water charges

<!-- b000980 | prose | pages [19] -->
respectively.

<!-- b000981 | prose | pages [19] -->
E W we have the following equation: For and min min

<!-- b000982 | prose | pages [19] -->
(

<!-- b000983 | prose | pages [19] -->
= +

<!-- b000984 | prose | pages [19] -->
E e e

<!-- b000985 | prose | pages [19] -->
T

<!-- b000986 | prose | pages [19] -->
,min

<!-- b000987 | prose | pages [19] -->
A

<!-- b000988 | prose | pages [19] -->
,min

<!-- b000989 | prose | pages [19] -->
I

<!-- b000990 | prose | pages [19] -->
,min

<!-- b000991 | prose | pages [19] -->
(

<!-- b000992 | prose | pages [19] -->
= +

<!-- b000993 | prose | pages [19] -->
W w w

<!-- b000994 | prose | pages [19] -->
T

<!-- b000995 | prose | pages [19] -->
,min

<!-- b000996 | prose | pages [19] -->
A

<!-- b000997 | prose | pages [19] -->
,min

<!-- b000998 | prose | pages [19] -->
I

<!-- b000999 | prose | pages [19] -->


<!-- b001000 | prose | pages [19] -->
E E

<!-- b001001 | prose | pages [19] -->
T

<!-- b001002 | prose | pages [19] -->
,min

<!-- b001003 | prose | pages [19] -->
p

<!-- b001004 | prose | pages [19] -->


<!-- b001005 | prose | pages [19] -->
W W

<!-- b001006 | prose | pages [19] -->
T

<!-- b001007 | prose | pages [19] -->
,min

<!-- b001008 | prose | pages [19] -->
p

<!-- b001009 | prose | pages [19] -->
)

<!-- b001010 | prose | pages [19] -->
+

<!-- b001011 | prose | pages [19] -->
e T

<!-- b001012 | prose | pages [19] -->
R

<!-- b001013 | prose | pages [19] -->
,min

<!-- b001014 | furniture | pages [19] -->


<!-- b001015 | prose | pages [19] -->
（24）

<!-- b001016 | prose | pages [19] -->
)

<!-- b001017 | prose | pages [19] -->
+

<!-- b001018 | prose | pages [19] -->
w T

<!-- b001019 | prose | pages [19] -->
,min ,min

<!-- b001020 | prose | pages [19] -->
R

<!-- b001021 | prose | pages [19] -->
,min

<!-- b001022 | prose | pages [19] -->
+ +

<!-- b001023 | prose | pages [19] -->
E

<!-- b001024 | prose | pages [19] -->
m

<!-- b001025 | furniture | pages [19] -->


<!-- b001026 | prose | pages [19] -->
（25）

<!-- b001027 | prose | pages [19] -->
+ +

<!-- b001028 | prose | pages [19] -->
W

<!-- b001029 | prose | pages [19] -->
m

<!-- b001030 | prose | pages [19] -->
The equation on the right represents the minimum demand for water and electricity for agriculture, industry and residents. The demand is based on the gross agricultural and industrial production and the number of residents. The height difference between the water level and the dead water level is also 50% of the original value in January 2021. If the demand for water and electricity is constant, there is no feasible solution to this situation.

<!-- b001031 | prose | pages [19] -->
At the same time, we note that Mexico will be affected by a severe water shortage, and in this case we estimate the minimum amount of water allocated to Mexico in proportion to population. Then there are constraints:

<!-- b001032 | prose | pages [19] -->
D 

<!-- b001033 | prose | pages [19] -->
w M , ,min

<!-- b001034 | prose | pages [19] -->
T q q （26）

<!-- b001035 | furniture | pages [19] -->


<!-- b001036 | prose | pages [19] -->
M

<!-- b001037 | prose | pages [19] -->
The amount of water replenishment in the Colorado River basin, which is affected by drought, is set at 0 for simplicity of calculation. Then there are constraints:

<!-- b001038 | prose | pages [19] -->
(

<!-- b001039 | prose | pages [19] -->
 −

<!-- b001040 | prose | pages [19] -->
( )

<!-- b001041 | prose | pages [19] -->
 = − +

<!-- b001042 | prose | pages [19] -->
E Aq P t

<!-- b001043 | prose | pages [19] -->
( )

<!-- b001044 | prose | pages [19] -->
H T

<!-- b001045 | prose | pages [19] -->


<!-- b001046 | prose | pages [19] -->
p m

<!-- b001047 | prose | pages [19] -->
0

<!-- b001048 | prose | pages [19] -->
p

<!-- b001049 | prose | pages [19] -->


<!-- b001050 | prose | pages [19] -->
(

<!-- b001051 | prose | pages [19] -->


<!-- b001052 | prose | pages [19] -->
( )

<!-- b001053 | prose | pages [19] -->
= − + 

<!-- b001054 | prose | pages [19] -->
E Aq M t

<!-- b001055 | prose | pages [19] -->
( )

<!-- b001056 | prose | pages [19] -->
H T

<!-- b001057 | prose | pages [19] -->


<!-- b001058 | prose | pages [19] -->
m M

<!-- b001059 | prose | pages [19] -->
0

<!-- b001060 | prose | pages [19] -->
m

<!-- b001061 | prose | pages [19] -->


<!-- b001062 | prose | pages [19] -->
)

<!-- b001063 | prose | pages [19] -->
 − −

<!-- b001064 | prose | pages [19] -->
3

<!-- b001065 | prose | pages [19] -->
q q q W T

<!-- b001066 | prose | pages [19] -->
m m e p

<!-- b001067 | prose | pages [19] -->
,

<!-- b001068 | prose | pages [19] -->
p

<!-- b001069 | prose | pages [19] -->
 

<!-- b001070 | prose | pages [19] -->
2

<!-- b001071 | prose | pages [19] -->
S

<!-- b001072 | prose | pages [19] -->


<!-- b001073 | prose | pages [19] -->
p

<!-- b001074 | furniture | pages [19] -->


<!-- b001075 | prose | pages [19] -->
（27）

<!-- b001076 | prose | pages [19] -->
)

<!-- b001077 | prose | pages [19] -->
 − − −

<!-- b001078 | prose | pages [19] -->
3

<!-- b001079 | prose | pages [19] -->
q q q q W T

<!-- b001080 | prose | pages [19] -->
m m M e m

<!-- b001081 | prose | pages [19] -->
,

<!-- b001082 | prose | pages [19] -->
m

<!-- b001083 | prose | pages [19] -->
 

<!-- b001084 | prose | pages [19] -->
2

<!-- b001085 | prose | pages [19] -->
S

<!-- b001086 | prose | pages [19] -->


<!-- b001087 | prose | pages [19] -->
m

<!-- b001088 | prose | pages [20] -->
For other constraints, be consistent with question 2. Since there are few decision variables in this case, we only use the first part of the genetic algorithm in the previous question to solve, and the solution results are as follows:

<!-- b001089 | furniture | pages [20] -->


<!-- b001090 | caption | pages [20] -->
Figure9 Population objective function curve

<!-- b001091 | furniture | pages [20] -->


<!-- b001092 | caption | pages [20] -->
Table8 Variables results

<!-- b001093 | prose | pages [20] -->
VARIABLE UNIT

<!-- b001094 | prose | pages [20] -->
q

<!-- b001095 | heading | pages [20] -->
RESULT

<!-- b001096 | prose | pages [20] -->
acre-feet/month m

<!-- b001097 | prose | pages [20] -->
w

<!-- b001098 | prose | pages [20] -->
30037.82

<!-- b001099 | prose | pages [20] -->
acre-feet/month p

<!-- b001100 | prose | pages [20] -->
q

<!-- b001101 | furniture | pages [20] -->


<!-- b001102 | prose | pages [20] -->
1946626.71

<!-- b001103 | prose | pages [20] -->
acre-feet/month M

<!-- b001104 | prose | pages [20] -->
w

<!-- b001105 | prose | pages [20] -->
110848.56

<!-- b001106 | prose | pages [20] -->
acre-feet/month m

<!-- b001107 | furniture | pages [20] -->


<!-- b001108 | prose | pages [20] -->
4040078.68

<!-- b001109 | prose | pages [20] -->
The results show that the height difference between water level and dead water level in January 2021 is 50% of the original value and the minimum demand is 10% of the original value. In the case of no water replenishment, the whole system can still achieve water and energy demand distribution, and meet the minimum extra consumption to maintain the overall water storage of the reservoir.

<!-- b001110 | heading | pages [20] -->
7. Sensitivity Analysis

<!-- b001111 | prose | pages [20] -->
According to the distribution result of question 3, when the water level of the original reservoir decreases by 50% due to drought, if the original water and electricity demand is reduced to 10%, the water and electricity demand of each state can be satisfied, and the hydropower resources are rich.

<!-- b001112 | prose | pages [20] -->
When the water level of the original reservoir decreases by 50%, 75% and 85% due to drought, and the demand for electricity and water is met, the percentage of decrease of electricity and water is obtained.

<!-- b001113 | caption | pages [21] -->
Table9 Drought sensitivity analysis results

<!-- b001114 | prose | pages [21] -->
Percentage drop in Decrease in water demand% Reservoir water level drop % electricity demand %

<!-- b001115 | prose | pages [21] -->
87．00 50% 89．82

<!-- b001116 | prose | pages [21] -->
87．04 75% 96．74

<!-- b001117 | prose | pages [21] -->
90．38 85%

<!-- b001118 | furniture | pages [21] -->


<!-- b001119 | prose | pages [21] -->
100

<!-- b001120 | prose | pages [21] -->
It can be seen from the results that with the deepening of drought, the corresponding electricity demand also decreases. And when the degree of drought is too high (reservoir water level drops by more than 85%), the total electricity demand will not be met.

<!-- b001121 | prose | pages [21] -->
With the development of new energy technology, the demand for hydraulic power generation decreases accordingly. When the demand for electricity decreases by 25%, 50% and 75% respectively under the condition of constant water demand, the flow of dam and the amount of water pumped from reservoir are obtained. However, after calculation, it is found that the model of minimum resource consumption corresponding to the reduction of electricity demand alone has no shape solution, indicating that the demand for reservoir water in each state is much higher than the demand for electricity.

<!-- b001122 | prose | pages [21] -->
Considering that the implementation of water saving and electricity saving measures is equivalent to the reduction of total water demand and electricity demand, it is discussed that when the total demand for water and electricity decreases by 25%, 50% and 75% respectively, the corresponding dam discharge and reservoir drainage amount will be calculated.

<!-- b001123 | furniture | pages [21] -->


<!-- b001124 | caption | pages [21] -->
Table10 Energy-saving and water-saving measures sensitivity analysis results

<!-- b001125 | prose | pages [21] -->
Demand for

<!-- b001126 | prose | pages [21] -->
25%

<!-- b001127 | prose | pages [21] -->
water and electricity

<!-- b001128 | prose | pages [21] -->
Percentage decline

<!-- b001129 | prose | pages [21] -->
q — m

<!-- b001130 | prose | pages [21] -->
w — p

<!-- b001131 | prose | pages [21] -->
q

<!-- b001132 | furniture | pages [21] -->


<!-- b001133 | prose | pages [21] -->
— M

<!-- b001134 | prose | pages [21] -->
w — m

<!-- b001135 | furniture | pages [21] -->


<!-- b001136 | prose | pages [21] -->
50% 75%

<!-- b001137 | prose | pages [21] -->
30275.72402 acre-feet —

<!-- b001138 | prose | pages [21] -->
— 13272078.49 acre-feet

<!-- b001139 | prose | pages [21] -->
— 253627.06 acre-feet

<!-- b001140 | prose | pages [21] -->
— 1694688.057 acre-feet

<!-- b001141 | prose | pages [21] -->
When the percentage of water and electricity demand drops by more than 75%, user water can be satisfied, and the pumping volume of Lake Powell and Lake Mead is 13272078.49 and 1694688.057 acre-feet respectively. The outflow flows of the two DAMS are 30275.72402 and 253627.06 acre-feet respectively.

<!-- b001142 | heading | pages [22] -->
8. Conclusions

<!-- b001143 | heading | pages [22] -->
8.1 Conclusions of the problem1

<!-- b001144 | prose | pages [22] -->
⚫ Since the water supply strategy will affect the water level of the corresponding

<!-- b001145 | prose | pages [22] -->
reservoirs of the two DAMS, and thus indirectly affect hydropower generation, it indicates that there are certain constraints on water supply and power demand. ⚫ According to the characteristic curve of water-level and reservoir capacity, the

<!-- b001146 | prose | pages [22] -->
range of water level change and reservoir capacity change can be approximately linear, and the lake area can be set as a fixed value, which does not change with the change of water level. ⚫ When there is no feasible solution to the optimal water resource dispatching model,

<!-- b001147 | prose | pages [22] -->
the cycle times obtained are the duration of dispatching. Results The duration of water dispatching is 23 months. ⚫ In order to ensure water demand, the minimum monthly water transfer is

<!-- b001148 | prose | pages [22] -->
. −= q -1106074.571 acre feet per month -

<!-- b001149 | furniture | pages [22] -->


<!-- b001150 | furniture | pages [22] -->


<!-- b001151 | heading | pages [22] -->
8.2 Conclusions of the problem2

<!-- b001152 | prose | pages [22] -->
The results of question 3 are shown in Table 6,7.

<!-- b001153 | heading | pages [22] -->
8.3 Conclusions of the problem3

<!-- b001154 | prose | pages [22] -->
The results of question 3 are shown in Table 10.

<!-- b001155 | heading | pages [22] -->
8.4 Conclusions of the problem4

<!-- b001156 | prose | pages [22] -->
As drought intensifies, demand for electricity declines. When the degree of drought is too high, the total electricity demand will not be satisfied. With the development of new energy technology, the demand for hydroelectric power is decreasing. When the water demand is unchanged and the electricity demand decreases by 25%, 50% and 75% respectively, the calculation shows that the water demand for reservoirs in each state is much higher than the electricity demand. When water saving and electricity saving measures are adopted and the respective demand decreases by more than 75%, the water consumption of users can be satisfied.

<!-- b001157 | furniture | pages [22] -->


<!-- b001158 | heading | pages [22] -->
9.  Model Evaluation and Further Discussion

<!-- b001159 | heading | pages [22] -->
9.1 Strengths

<!-- b001160 | prose | pages [22] -->
⚫ The model takes into account the benefits of industrial, agricultural water, and electricity production. The pumping volume of each lake is scheduled through the optimization model of transportation cost. ⚫ It takes into account not only the scheduling of how much water to draw from the two lakes, but also the difference in transportation costs between states Considering the competitive interests of agricultural, industrial, residential and ⚫ electricity production water, as well as the transportation costs of water resources, we

<!-- b001161 | prose | pages [23] -->
establish a two-stage model. We use the genetic algorithm when solving the model, which greatly improves the efficiency of the computer. ⚫ The model is based on certain theories. Through literature review, we carefully

<!-- b001162 | prose | pages [23] -->
select the model. Therefore, our model can be consistent with the actual situation as much as possible. ⚫ The data we collected are very sufficient and the accuracy of simulation is very

<!-- b001163 | prose | pages [23] -->
high.

<!-- b001164 | heading | pages [23] -->
9.2 Weakness

<!-- b001165 | prose | pages [23] -->
⚫ The transportation cost function for each state depends only on distance, and

<!-- b001166 | prose | pages [23] -->
distance depends only on the location of each state's center of mass and dam. The model may not represent the actual transportation of water. ⚫ The model can only solve the water scheduling problem in a fixed time period.

<!-- b001167 | furniture | pages [23] -->


<!-- b001168 | furniture | pages [23] -->


<!-- b001169 | prose | pages [24] -->
10.

<!-- b001170 | prose | pages [24] -->
Article for Drought and Thirst magazine

<!-- b001171 | prose | pages [24] -->
In 2021, the western United States has experienced unprecedented dry weather. The persistent drought has caused local reservoir water levels to drop to record lows.

<!-- b001172 | prose | pages [24] -->
Low water flows have reduced the amount of electricity produced by hydropower plants, leading to interruptions in power supply in these areas. If the water level in the reservoir behind the dam is low enough, hydroelectric power generation stops. People's lives are also seriously threatened by the drought. According to the U.S. Drought Monitoring Center, about 40 percent of the U.S. is currently experiencing drought conditions.

<!-- b001173 | furniture | pages [24] -->


<!-- b001174 | caption | pages [24] -->
Figure 10 Lake Mead [7]

<!-- b001175 | caption | pages [24] -->
Figure 9. Drought map of the US [7]

<!-- b001176 | prose | pages [24] -->
Powell and Mead, the two largest reservoirs in the United States on the Colorado River, have been in a state of low water levels for a long time due to drought.

<!-- b001177 | prose | pages [24] -->
Lake Mead formed by the Hoover Dam, the water level before the dam is 45.72m lower than the highest water level, reaching the lowest level in history.

<!-- b001178 | prose | pages [24] -->
Negotiating teams in the states asked us to build models to guide the operation of the dam, which is the ultimate goal of the issue.We found that the water supply strategy affects the water level of the corresponding reservoirs of the two dams, which indirectly affects hydropower generation. Our team temporarily separated the water supply and electricity demand, and set up several small stages to analyze and simplify the problem.

<!-- b001179 | prose | pages [24] -->
According to the constraints, the optimization model is established and solved. The duration of water dispatching is 23 months.The remaining available storage capacity of the two reservoirs is 0 and 54199.52 acre-ft respectively; and the total monthly water demand of the user is 1375000.00 acre-ft, so at least 1375000.00-

<!-- b001180 | prose | pages [24] -->
54199.52-0=1320800.48 acre-ft of water needs to be transferred. Since then, the two reservoirs have no usable stock. In order to ensure water demand, the minimum monthly −= acre feet per month q -1106074.571 water diversion is -

<!-- b001181 | furniture | pages [24] -->


<!-- b001182 | furniture | pages [24] -->


<!-- b001183 | prose | pages [24] -->
. We analyze the competing interests of water for agriculture, industry, residential water, and electricity production, and construct a two-stage mathematical model. In

<!-- b001184 | prose | pages [25] -->
January 2021, the optimal gross production value is $412,208,7017, and the total water consumption is 49,52007acre-feet, with more water extracted from Lake Powell.

<!-- b001185 | prose | pages [25] -->
The height difference between water level and dead water level in January 2021 is 50% of the original value and the minimum demand is 10% of the original value. In the case of no water replenishment, the whole system can still achieve water and energy demand distribution, and meet the minimum extra consumption to maintain the overall water storage of the reservoir.

<!-- b001186 | prose | pages [25] -->
When there is not enough water to meet all water and electricity demands, we establish a nonlinear programming model under the premise of meeting the minimum demand, minimize the excess power generation and water discharge, so as to cope with the state of drought and water shortage for as long as possible. Genetic algorithm is used to solve the water and energy demand distribution of the system. The water extracted from Lake Powell and Lake Mead in a month is 1946626.71acre-feet and 4040078.68acre-feet respectively. Glen Canyon Dam and The Hoover Dam output 30037.82arce-feet and 110848.56acre-feet downstream respectively.

<!-- b001187 | prose | pages [25] -->
MCM 22thFeb2022

<!-- b001188 | prose | pages [25] -->
11.

<!-- b001189 | heading | pages [25] -->
References

<!-- b001190 | references | pages [25] -->
[1] https://www.theguardian.com/us-news/2021/jul/13/hoover-dam-lake-mead-severe-drought-us-

<!-- b001191 | references | pages [25] -->
west

<!-- b001192 | references | pages [25] -->
[2] Management of the Colorado River: Water Allocations, Drought, and the Federal Role,

<!-- b001193 | references | pages [25] -->
https://crsreports.congress.gov/product/pdf/R/R45546

<!-- b001194 | references | pages [25] -->
[3] Congressional Research Service (CRS), using data from USGS, ESRI Data & Maps, 2017, Central Arizona

<!-- b001195 | references | pages [25] -->
Project, and ESRI World Shaded Relief Map

<!-- b001196 | references | pages [25] -->
[4] Glen Canyon Powerplant (usbr.gov)

<!-- b001197 | references | pages [25] -->
[5] Hoover Powerplant (usbr.gov)

<!-- b001198 | references | pages [25] -->
[6] https://www.usbr.gov/uc/water/hydrodata/reservoir_data/919/dashboard.html

<!-- b001199 | references | pages [25] -->
[7] https://www.americanrivers.org/river/colorado-river

<!-- b001200 | furniture | pages [25] -->


<!-- b001201 | furniture | pages [25] -->

