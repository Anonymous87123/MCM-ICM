# P-A-2014-29911-ac64b43b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team#29911

<!-- b000002 | furniture | pages [1] -->
Page 1 of 40

<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->
Team Control Number

<!-- b000007 | title | pages [1] -->
29911

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
T1 ________________

<!-- b000010 | prose | pages [1] -->
T2 ________________

<!-- b000011 | furniture | pages [1] -->


<!-- b000012 | prose | pages [1] -->
T3 ________________

<!-- b000013 | prose | pages [1] -->
For office use only

<!-- b000014 | prose | pages [1] -->
F1 ________________

<!-- b000015 | prose | pages [1] -->
F2 ________________

<!-- b000016 | prose | pages [1] -->
F3 ________________

<!-- b000017 | prose | pages [1] -->
Problem Chosen

<!-- b000018 | prose | pages [1] -->
T4 ________________

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | prose | pages [1] -->
F4 ________________

<!-- b000021 | title | pages [1] -->
A

<!-- b000022 | title | pages [1] -->
A

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | heading | pages [1] -->
Summary

<!-- b000026 | prose | pages [1] -->
The keep-right-except-to-pass (KRETP) rule has been adopted by many

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | prose | pages [1] -->
countries around the world, but does this rule actually make our transportation system more efficient? This report aims to analyze this rule along with several other traffic regulations.

<!-- b000029 | prose | pages [1] -->
Using a discrete cellular-automaton (CA) model and a continuum model, we

<!-- b000030 | furniture | pages [1] -->


<!-- b000031 | prose | pages [1] -->
can simulate real-life traffic situation on freeways via the Monte Carlo method and PDE system respectively. Through comparison with other two traffic rules, we obtain the conclusion that the KRETP rule is rather effective.

<!-- b000032 | prose | pages [1] -->
First we define three parameters---traffic flow, safety index and average

<!-- b000033 | furniture | pages [1] -->


<!-- b000034 | prose | pages [1] -->
energy consumption (AEC) to evaluate the performance of the KRETP rule under

<!-- b000035 | prose | pages [1] -->
various vehicle density. By calculating the optimal maximum velocities during light and heavy traffic, we obtain the influence of under-posted and over-posted speed limits. We also assert that our model can be transferred in "left-most" countries with a simple change of orientation.

<!-- b000036 | prose | pages [1] -->
Then we introduce two other traffic rules----the "Slow-Cars-To-Right" (SCTR)

<!-- b000037 | furniture | pages [1] -->


<!-- b000038 | prose | pages [1] -->
rule and the "Free Driving & Free Overtaking" (FDFO) rule. By comparing these three rules in terms of our pre-defined parameters, we confirm KRETP rule's superiority and provide strategic advice for future freeway construction.

<!-- b000039 | prose | pages [1] -->
Next, under the control of an intelligent system, a "median" optimization

<!-- b000040 | furniture | pages [1] -->


<!-- b000041 | prose | pages [1] -->
method is proposed to improve the overall quality of freeway transportation

<!-- b000042 | prose | pages [1] -->
system. According to simulation result, our optimization method does improve the performance in terms of all three parameters.

<!-- b000043 | prose | pages [1] -->
Finally, we discuss upon several defects of our model that require further

<!-- b000044 | furniture | pages [1] -->


<!-- b000045 | prose | pages [1] -->
research.

<!-- b000046 | furniture | pages [1] -->


<!-- b000047 | keywords | pages [1] -->
Keywords: KRETP Rule, CA Model, Continuum Model, Monte Carlo Method,

<!-- b000048 | prose | pages [1] -->
Traffic Flow, Safety Index, Average Energy Consumption (AEC), Optimization

<!-- b000049 | furniture | pages [1] -->


<!-- b000050 | prose | pages [1] -->


<!-- b000051 | furniture | pages [2] -->
Team#29911

<!-- b000052 | prose | pages [2] -->


<!-- b000053 | prose | pages [2] -->


<!-- b000054 | furniture | pages [2] -->
Page 2 of 40

<!-- b000055 | furniture | pages [2] -->


<!-- b000056 | furniture | pages [2] -->


<!-- b000057 | furniture | pages [2] -->


<!-- b000058 | prose | pages [2] -->


<!-- b000059 | prose | pages [2] -->


<!-- b000060 | prose | pages [2] -->


<!-- b000061 | prose | pages [2] -->
The Keep-Right-Except-To-Pass Rule

<!-- b000062 | furniture | pages [2] -->


<!-- b000063 | furniture | pages [2] -->


<!-- b000064 | furniture | pages [2] -->


<!-- b000065 | furniture | pages [2] -->


<!-- b000066 | furniture | pages [2] -->


<!-- b000067 | furniture | pages [2] -->


<!-- b000068 | furniture | pages [2] -->


<!-- b000069 | furniture | pages [2] -->


<!-- b000070 | furniture | pages [2] -->


<!-- b000071 | furniture | pages [2] -->


<!-- b000072 | furniture | pages [2] -->


<!-- b000073 | furniture | pages [2] -->


<!-- b000074 | furniture | pages [2] -->


<!-- b000075 | furniture | pages [2] -->


<!-- b000076 | furniture | pages [2] -->


<!-- b000077 | furniture | pages [2] -->


<!-- b000078 | furniture | pages [2] -->


<!-- b000079 | furniture | pages [2] -->


<!-- b000080 | furniture | pages [2] -->


<!-- b000081 | furniture | pages [3] -->
Page 3 of 40

<!-- b000082 | furniture | pages [3] -->
Team#29911

<!-- b000083 | furniture | pages [3] -->


<!-- b000084 | furniture | pages [3] -->


<!-- b000085 | heading | pages [3] -->
Contents

<!-- b000086 | contents | pages [3] -->
1

<!-- b000087 | contents | pages [3] -->
Introduction..................................................................................................................................4

<!-- b000088 | contents | pages [3] -->
2

<!-- b000089 | contents | pages [3] -->
Assumptions.................................................................................................................................5

<!-- b000090 | contents | pages [3] -->
3

<!-- b000091 | contents | pages [3] -->
Modeling for Right-Most Rule...............................................................................................5

<!-- b000092 | furniture | pages [3] -->


<!-- b000093 | contents | pages [3] -->
3.1 Discrete Modeling for Right-Most Rule.....................................................................5

<!-- b000094 | furniture | pages [3] -->


<!-- b000095 | furniture | pages [3] -->


<!-- b000096 | contents | pages [3] -->
3.1.1 Model Establishment............................................................................................5

<!-- b000097 | furniture | pages [3] -->


<!-- b000098 | furniture | pages [3] -->


<!-- b000099 | contents | pages [3] -->
3.1.2 Parameter Evaluation.........................................................................................10

<!-- b000100 | furniture | pages [3] -->


<!-- b000101 | furniture | pages [3] -->


<!-- b000102 | contents | pages [3] -->
3.1.3 Model Solution and Analysis...........................................................................10

<!-- b000103 | furniture | pages [3] -->


<!-- b000104 | contents | pages [3] -->
3.2 Continuum Modeling for Right-Most Rule.............................................................17

<!-- b000105 | furniture | pages [3] -->


<!-- b000106 | furniture | pages [3] -->


<!-- b000107 | contents | pages [3] -->
3.2.1 Model Establishment..........................................................................................17

<!-- b000108 | furniture | pages [3] -->


<!-- b000109 | furniture | pages [3] -->


<!-- b000110 | contents | pages [3] -->
3.2.2 Model Solution and Analysis...........................................................................18

<!-- b000111 | furniture | pages [3] -->


<!-- b000112 | contents | pages [3] -->
3.3 Comparison of Discrete Model and Continuum Model....................................22

<!-- b000113 | furniture | pages [3] -->


<!-- b000114 | contents | pages [3] -->
3.4 Transferability Analysis of Model in "Left-Handed" Countries.....................22

<!-- b000115 | contents | pages [3] -->
4

<!-- b000116 | contents | pages [3] -->
Modeling for Alternative Freeway Traffic Rules.........................................................22

<!-- b000117 | furniture | pages [3] -->


<!-- b000118 | contents | pages [3] -->
4.1 "Slow-Cars-To-Right" Rule............................................................................................22

<!-- b000119 | furniture | pages [3] -->


<!-- b000120 | contents | pages [3] -->
4.2 "Free Driving & Free Overtaking" Rule....................................................................23

<!-- b000121 | furniture | pages [3] -->


<!-- b000122 | contents | pages [3] -->
4.3 Comparison of Different Traffic Rules......................................................................24

<!-- b000123 | contents | pages [3] -->
5

<!-- b000124 | contents | pages [3] -->
Modeling for Intelligent-System Control........................................................................26

<!-- b000125 | furniture | pages [3] -->


<!-- b000126 | contents | pages [3] -->
5.1 "Median" Optimization...................................................................................................26

<!-- b000127 | furniture | pages [3] -->


<!-- b000128 | contents | pages [3] -->
5.2 Possible Further Improvements…………………………………………………………29

<!-- b000129 | contents | pages [3] -->
6

<!-- b000130 | contents | pages [3] -->
Superiority and Weakness....................................................................................................29

<!-- b000131 | furniture | pages [3] -->


<!-- b000132 | contents | pages [3] -->
6.1 Superiority Analysis.........................................................................................................29

<!-- b000133 | furniture | pages [3] -->


<!-- b000134 | contents | pages [3] -->
6.2 Weakness Analysis............................................................................................................30

<!-- b000135 | furniture | pages [3] -->


<!-- b000136 | contents | pages [3] -->
6.3 Future Research.................................................................................................................30

<!-- b000137 | furniture | pages [3] -->


<!-- b000138 | furniture | pages [3] -->


<!-- b000139 | contents | pages [3] -->
6.3.1 Possible Optimization of Discrete Model....................................................30

<!-- b000140 | furniture | pages [3] -->


<!-- b000141 | furniture | pages [3] -->


<!-- b000142 | contents | pages [3] -->
6.3.2 Possible Optimization of Continuum Model..............................................31

<!-- b000143 | contents | pages [3] -->
7

<!-- b000144 | contents | pages [3] -->
Conclusion...................................................................................................................................31

<!-- b000145 | contents | pages [3] -->
8

<!-- b000146 | contents | pages [3] -->
References...................................................................................................................................32

<!-- b000147 | contents | pages [3] -->
9

<!-- b000148 | contents | pages [3] -->
Appendix..................................................................................................................................... 32

<!-- b000149 | furniture | pages [4] -->
Team#29911

<!-- b000150 | heading | pages [4] -->
1 Introduction

<!-- b000151 | furniture | pages [4] -->
Page 4 of 40

<!-- b000152 | furniture | pages [4] -->


<!-- b000153 | furniture | pages [4] -->


<!-- b000154 | furniture | pages [4] -->


<!-- b000155 | prose | pages [4] -->
Traffic rule plays an essential role in a nation's transportation system. An

<!-- b000156 | furniture | pages [4] -->


<!-- b000157 | prose | pages [4] -->
optimal traffic rule can dramatically enhance the capacity and efficiency of the

<!-- b000158 | prose | pages [4] -->
transportation network, providing common citizens with tremendous

<!-- b000159 | prose | pages [4] -->
convenience. In this report, we will mainly focus on one such rule which requires

<!-- b000160 | prose | pages [4] -->
automobiles to stay in the right lane unless they have to overtake.

<!-- b000161 | prose | pages [4] -->
America first enacted the "keep-right-except-to-pass" law in New York State

<!-- b000162 | furniture | pages [4] -->


<!-- b000163 | prose | pages [4] -->
in 1804, followed by many other countries in the following decades. [1] Up to now,

<!-- b000164 | prose | pages [4] -->
most countries are "right-handed" countries with very few exceptions such as the

<!-- b000165 | prose | pages [4] -->
UK and Australia. On American multilane freeways, for example, drivers are

<!-- b000166 | prose | pages [4] -->
required to drive in the right-most lane unless they need to overtake, in which

<!-- b000167 | prose | pages [4] -->
case they move one lane to the left and then switch back to the right-most lane.

<!-- b000168 | prose | pages [4] -->
See in Figure 1.

<!-- b000169 | prose | pages [4] -->
Despite the long history of this rule, there has been little scientific inquiry

<!-- b000170 | furniture | pages [4] -->


<!-- b000171 | prose | pages [4] -->
into the effect of this rule. In such circumstances, a systematic analysis of this

<!-- b000172 | prose | pages [4] -->
rule's realistic effect, including the change in traffic flow, safety index and energy

<!-- b000173 | prose | pages [4] -->
consumption.

<!-- b000174 | prose | pages [4] -->
More specifically, we are expected to examine the following issues in our

<!-- b000175 | furniture | pages [4] -->


<!-- b000176 | prose | pages [4] -->
report:

<!-- b000177 | prose | pages [4] -->
Analyze the effect of the "keep-right-except-to-pass" rule in various terms 

<!-- b000178 | prose | pages [4] -->
under different vehicle densities (light and heavy traffic);

<!-- b000179 | furniture | pages [4] -->


<!-- b000180 | prose | pages [4] -->
Calculate the optimized speed to maximize a weighted function of the 

<!-- b000181 | prose | pages [4] -->
traffic flow, safety index and average energy consumption.

<!-- b000182 | furniture | pages [4] -->


<!-- b000183 | prose | pages [4] -->
Discuss the role of under-posted and over-posted speed limits and the 

<!-- b000184 | prose | pages [4] -->
transferability of our model in "left-handed" countries where driving on the

<!-- b000185 | furniture | pages [4] -->


<!-- b000186 | furniture | pages [4] -->


<!-- b000187 | prose | pages [4] -->
left lane is the norm;

<!-- b000188 | prose | pages [4] -->
Propose other possible freeway traffics rules and compare them with the 

<!-- b000189 | furniture | pages [4] -->


<!-- b000190 | prose | pages [4] -->
"keep-right-except-to-pass" rule;

<!-- b000191 | prose | pages [4] -->
Discuss the transferability of our model in "left-handed" countries where 

<!-- b000192 | furniture | pages [4] -->


<!-- b000193 | prose | pages [4] -->
driving on the left lane is the norm;

<!-- b000194 | prose | pages [4] -->
Design optimization method to enlarge traffic flow when equipped with an 

<!-- b000195 | furniture | pages [4] -->


<!-- b000196 | prose | pages [4] -->
intelligent system.

<!-- b000197 | furniture | pages [4] -->


<!-- b000198 | furniture | pages [4] -->


<!-- b000199 | furniture | pages [5] -->
Page 5 of 40

<!-- b000200 | furniture | pages [5] -->
Team#29911

<!-- b000201 | furniture | pages [5] -->


<!-- b000202 | furniture | pages [5] -->


<!-- b000203 | furniture | pages [5] -->


<!-- b000204 | furniture | pages [5] -->


<!-- b000205 | furniture | pages [5] -->


<!-- b000206 | furniture | pages [5] -->


<!-- b000207 | furniture | pages [5] -->


<!-- b000208 | furniture | pages [5] -->


<!-- b000209 | caption | pages [5] -->
Figure 1. Illustration of "Keep-Right-Except-To-Pass" Rule

<!-- b000210 | heading | pages [5] -->
2 Assumptions

<!-- b000211 | prose | pages [5] -->
 Assuming automobile to move in straight lines;

<!-- b000212 | prose | pages [5] -->
 Assuming that jams only occur because of gradual piling of automobiles;

<!-- b000213 | prose | pages [5] -->
 Without consideration of sudden crashes that will influence the behavior of

<!-- b000214 | furniture | pages [5] -->


<!-- b000215 | prose | pages [5] -->
subsequent vehicles;

<!-- b000216 | prose | pages [5] -->
 Assuming that the parallel movement of a vehicle into another lane takes no

<!-- b000217 | furniture | pages [5] -->


<!-- b000218 | prose | pages [5] -->
time;

<!-- b000219 | prose | pages [5] -->
 Assuming that all the drivers on the freeway are abide by the traffic rules;

<!-- b000220 | prose | pages [5] -->
 Assuming that the vehicles have the same length and mass;

<!-- b000221 | prose | pages [5] -->
 Assuming that freeways have no extra entrance or exit.

<!-- b000222 | heading | pages [5] -->
3 Modeling for Right-Most Rule

<!-- b000223 | furniture | pages [5] -->


<!-- b000224 | prose | pages [5] -->
In order to analyze the effect of the "right-most" rule, first we have to

<!-- b000225 | prose | pages [5] -->
establish a model to simulate the traffic flow on the multilane freeway. Then we

<!-- b000226 | prose | pages [5] -->
add certain driving and lane-changing rules to make sure that in our simulation

<!-- b000227 | prose | pages [5] -->
the automobiles are abide by the "right-most" rule.

<!-- b000228 | heading | pages [5] -->
3.1 Discrete Modeling for Right-Most Rule

<!-- b000229 | furniture | pages [5] -->


<!-- b000230 | prose | pages [5] -->
Discrete models treat both time and the position of vehicles as discrete quantities

<!-- b000231 | prose | pages [5] -->
and simulate the moving of automobiles step by step. We start out simulation with a

<!-- b000232 | prose | pages [5] -->
single kind of vehicle (single maximum speed) on a double-lane freeway (right lane is

<!-- b000233 | prose | pages [5] -->
slow lane and left lane is fast lane) and then extend to two kinds of vehicles, namely,

<!-- b000234 | prose | pages [5] -->
fast car and slow car (two maximum speeds), which is closer to realistic situation.

<!-- b000235 | heading | pages [5] -->
3.1.1 Model Establishment

<!-- b000236 | prose | pages [5] -->
 Vehicles of a Single Kind

<!-- b000237 | furniture | pages [5] -->


<!-- b000238 | prose | pages [5] -->
Among the various discrete models, we adopt the "Particle-Hopping" model,

<!-- b000239 | prose | pages [5] -->
which was initially formulated by Nagel and Schreckenberg (NS) to idealize the

<!-- b000240 | furniture | pages [6] -->
Team#29911

<!-- b000241 | furniture | pages [6] -->
Page 6 of 40

<!-- b000242 | furniture | pages [6] -->


<!-- b000243 | furniture | pages [6] -->


<!-- b000244 | furniture | pages [6] -->


<!-- b000245 | prose | pages [6] -->
movement of vehicles as the discrete "hopping" of particles. Figure 2 is a vivid

<!-- b000246 | prose | pages [6] -->
illustration of our model. We treat the double-lane freeway as a two-column

<!-- b000247 | prose | pages [6] -->
lattice and each vehicle contains exactly one lattice.

<!-- b000248 | furniture | pages [6] -->


<!-- b000249 | furniture | pages [6] -->


<!-- b000250 | furniture | pages [6] -->


<!-- b000251 | furniture | pages [6] -->


<!-- b000252 | furniture | pages [6] -->


<!-- b000253 | furniture | pages [6] -->


<!-- b000254 | furniture | pages [6] -->


<!-- b000255 | furniture | pages [6] -->


<!-- b000256 | furniture | pages [6] -->


<!-- b000257 | furniture | pages [6] -->


<!-- b000258 | furniture | pages [6] -->


<!-- b000259 | caption | pages [6] -->
Figure 2. Representation of the "Particle-Hopping" Model

<!-- b000260 | prose | pages [6] -->
We apply the Monte Carlo method to simulate the traffic flow on the

<!-- b000261 | furniture | pages [6] -->


<!-- b000262 | prose | pages [6] -->
double-lane freeway.[2] The quantities involved in the simulation are shown in

<!-- b000263 | caption | pages [6] -->
Table 1.

<!-- b000264 | furniture | pages [6] -->


<!-- b000265 | heading | pages [6] -->
Notation

<!-- b000266 | prose | pages [6] -->
Definition

<!-- b000267 | prose | pages [6] -->
The position of car numbered 𝑘 𝑋(𝑘)

<!-- b000268 | prose | pages [6] -->
The velocity of car numbered 𝑘 𝑉(𝑘)

<!-- b000269 | prose | pages [6] -->
𝑓(𝑘) The gap in front of car numbered 𝑘 in the present lane

<!-- b000270 | prose | pages [6] -->
Δ𝑋𝑝

<!-- b000271 | prose | pages [6] -->
𝑏(𝑘) The gap behind car numbered 𝑘 in the present lane

<!-- b000272 | prose | pages [6] -->
Δ𝑋𝑝

<!-- b000273 | prose | pages [6] -->
𝑓(𝑘) The gap in front of car numbered 𝑘 in the other lane

<!-- b000274 | prose | pages [6] -->
Δ𝑋𝑜

<!-- b000275 | prose | pages [6] -->
The gap behind car numbered 𝑘 in the other lane 𝑏(𝑘)

<!-- b000276 | prose | pages [6] -->
Δ𝑋𝑜

<!-- b000277 | prose | pages [6] -->
The maximum velocity the kth car can achieve on the freeway 𝑉𝑚𝑎𝑥(𝑘)

<!-- b000278 | prose | pages [6] -->
The traffic flow(number of cars passed per lane per unit time) 𝑄

<!-- b000279 | prose | pages [6] -->
𝛼𝑠𝑎𝑓𝑒 The safety index

<!-- b000280 | prose | pages [6] -->
The length of the lane during simulation* 𝐿

<!-- b000281 | prose | pages [6] -->
The duration of the simulation* 𝑇

<!-- b000282 | furniture | pages [7] -->
Page 7 of 40

<!-- b000283 | furniture | pages [7] -->
Team#29911

<!-- b000284 | furniture | pages [7] -->


<!-- b000285 | furniture | pages [7] -->


<!-- b000286 | prose | pages [7] -->
𝑃𝑑 The probability of a car decelerating*

<!-- b000287 | prose | pages [7] -->
𝑃𝑐 The probability of a car changing lane*

<!-- b000288 | prose | pages [7] -->
𝑛 The density of vehicles *

<!-- b000289 | prose | pages [7] -->
𝑁 The number of car during simulation 𝑁= 2𝑛𝐿

<!-- b000290 | caption | pages [7] -->
Table 1. Definition of Notation in "Particle-Hopping" Model

<!-- b000291 | prose | pages [7] -->
(Terms marked with an asterisk (*) require pre-evaluation before the simulation begins)

<!-- b000292 | furniture | pages [7] -->


<!-- b000293 | prose | pages [7] -->
Before the simulation begins, we need to evaluate the following five

<!-- b000294 | prose | pages [7] -->
parameters: number of cars 𝑁, the length of lane 𝐿, the duration of the

<!-- b000295 | prose | pages [7] -->
simulation 𝑇, the maximum velocity vehicles can achieve 𝑉𝑚𝑎𝑥, the probability

<!-- b000296 | prose | pages [7] -->
for a driver to decelerate during each unit time 𝑃𝑑 and the probability for a

<!-- b000297 | prose | pages [7] -->
driver to change lane 𝑃𝑐 if the current situation qualifies the rule of changing

<!-- b000298 | prose | pages [7] -->
lanes.

<!-- b000299 | furniture | pages [7] -->


<!-- b000300 | prose | pages [7] -->
After these parameters have been evaluated, we set the position of each car

<!-- b000301 | prose | pages [7] -->
𝑋(𝑛) randomly in the double-lane freeway with half cars on the left (fast) lane

<!-- b000302 | prose | pages [7] -->
and the other half on the right (slow) lane and the velocity of each car

<!-- b000303 | prose | pages [7] -->
𝑉(𝑛)randomly between [𝑉𝑚𝑎𝑥/2, 𝑉𝑚𝑎𝑥]. We set the entire freeway to be a

<!-- b000304 | prose | pages [7] -->
loophole so that once a car reaches the last lattices it will re-enter the

<!-- b000305 | prose | pages [7] -->
double-lane freeway in the first lattices. Under such conditions, the density of the

<!-- b000306 | prose | pages [7] -->
vehicles remain unchanged throughout the simulation.

<!-- b000307 | furniture | pages [7] -->


<!-- b000308 | prose | pages [7] -->
After the simulation begins, at each time unit the driver will either remain

<!-- b000309 | prose | pages [7] -->
in the same lane or change lane if situation permits. The rule of acceleration and

<!-- b000310 | prose | pages [7] -->
deceleration is as follows:

<!-- b000311 | furniture | pages [7] -->


<!-- b000312 | prose | pages [7] -->
(𝑖)  𝐼𝑓 𝑉(𝑛) < 𝑉𝑚𝑎𝑥, 𝑡ℎ𝑒𝑛 𝑉(𝑛) = 𝑉(𝑛) + 1;

<!-- b000313 | prose | pages [7] -->
(𝑖𝑖) 𝐼𝑓 𝑟𝑎𝑛 𝑓< 𝑝𝑑, 𝑡ℎ𝑒𝑛 𝑉(𝑛) = 𝑉(𝑛) −1;

<!-- b000314 | caption | pages [7] -->
Table 2. The Rule of Acceleration and Deceleration

<!-- b000315 | prose | pages [7] -->
where 𝑟𝑎𝑛 𝑓 is a random number between 0 and 1 generated at each time

<!-- b000316 | prose | pages [7] -->
unit.

<!-- b000317 | furniture | pages [7] -->


<!-- b000318 | prose | pages [7] -->
The permission rule for changing lane is much more complex and comprised

<!-- b000319 | prose | pages [7] -->
of several basic rules. It is derived from Wagner’s according to the statistics

<!-- b000320 | prose | pages [7] -->
gathered from a Germany freeway where "right-most" rule is adopted:[3]

<!-- b000321 | furniture | pages [8] -->
Team#29911

<!-- b000322 | furniture | pages [8] -->
Page 8 of 40

<!-- b000323 | furniture | pages [8] -->


<!-- b000324 | furniture | pages [8] -->


<!-- b000325 | furniture | pages [8] -->


<!-- b000326 | prose | pages [8] -->
Rule stay except Rule safety

<!-- b000327 | prose | pages [8] -->
Rule change when possible

<!-- b000328 | prose | pages [8] -->
(Rule #1)

<!-- b000329 | prose | pages [8] -->
blocked (Rule #0)

<!-- b000330 | prose | pages [8] -->
𝑓(𝑛) > ΔX𝑝

<!-- b000331 | prose | pages [8] -->
𝑓(𝑛)(more space

<!-- b000332 | prose | pages [8] -->
(i)ΔX𝑜

<!-- b000333 | prose | pages [8] -->
𝑓(𝑛) < 𝑉𝑚𝑎𝑥+ 1 ,

<!-- b000334 | prose | pages [8] -->
𝑓(𝑘) > 0,

<!-- b000335 | prose | pages [8] -->
(i) ΔX𝑝

<!-- b000336 | prose | pages [8] -->
(i)ΔX𝑝

<!-- b000337 | prose | pages [8] -->
𝑓(𝑛) >

<!-- b000338 | prose | pages [8] -->
on the other lane) or  ΔX𝑜

<!-- b000339 | prose | pages [8] -->
not enough space in

<!-- b000340 | prose | pages [8] -->
enough space in

<!-- b000341 | prose | pages [8] -->
front

<!-- b000342 | prose | pages [8] -->
front

<!-- b000343 | prose | pages [8] -->
𝑓(𝑛) > ΔX𝑝

<!-- b000344 | prose | pages [8] -->
(ii) The nearest

<!-- b000345 | prose | pages [8] -->
(ii)  ΔX𝑜

<!-- b000346 | prose | pages [8] -->
𝑉(𝑘)(enough space on the other

<!-- b000347 | prose | pages [8] -->
lane)

<!-- b000348 | prose | pages [8] -->
𝑓(𝑛)

<!-- b000349 | prose | pages [8] -->
, more space on the

<!-- b000350 | prose | pages [8] -->
neighbor site in the

<!-- b000351 | prose | pages [8] -->
other lane

<!-- b000352 | prose | pages [8] -->
other lane is empty.

<!-- b000353 | prose | pages [8] -->
(iii) ΔXo

<!-- b000354 | prose | pages [8] -->
b(n) > Vmax ,

<!-- b000355 | prose | pages [8] -->
enough space to the

<!-- b000356 | prose | pages [8] -->
(iii) ran f < Pc

<!-- b000357 | prose | pages [8] -->
next car on the

<!-- b000358 | prose | pages [8] -->
other lane

<!-- b000359 | prose | pages [8] -->
(ii) ran f < Pc

<!-- b000360 | furniture | pages [8] -->


<!-- b000361 | caption | pages [8] -->
Table 3. The Basic Rules

<!-- b000362 | prose | pages [8] -->
𝒓𝒊𝒈𝒉𝒕→𝒍𝒆𝒇𝒕 (i) Rule safety (ii) Rule #0 𝒍𝒆𝒇𝒕→𝒓𝒊𝒈𝒉𝒕 (i) Rule safety (ii) Rule #1

<!-- b000363 | caption | pages [8] -->
Table 4. The Rule of Lane Changing corresponding to the “rightmost” rule

<!-- b000364 | prose | pages [8] -->
Our Monte Carlo simulation has three outputs: traffic flow 𝑄 and safety

<!-- b000365 | furniture | pages [8] -->


<!-- b000366 | prose | pages [8] -->
index 𝛼𝑠𝑎𝑓𝑒 and the energy cost E0. For traffic flow 𝑄, we choose a fixed point (in our simulation we choose the end point of the lattices since the freeway is a loop) to count the total number of cars passing that point denoted as 𝑁𝑡𝑜𝑡𝑎𝑙 within the duration of the simulation 𝑇, then we use the following equation to calculate 𝑄:

<!-- b000367 | prose | pages [8] -->
𝑄= 𝑁𝑡𝑜𝑡𝑎𝑙

<!-- b000368 | prose | pages [8] -->
. 𝑇

<!-- b000369 | prose | pages [8] -->
As for 𝛼𝑠𝑎𝑓𝑒, we make the assumption that safety index is proportionate to the reaction time of all the drivers on the freeway throughout the entire simulation. We take the proportionate coefficient to be 1 for convenience:

<!-- b000370 | prose | pages [8] -->
𝑁 𝑓

<!-- b000371 | prose | pages [8] -->
∑∑[exp(−ΔX𝑝

<!-- b000372 | prose | pages [8] -->
𝑇 1

<!-- b000373 | prose | pages [8] -->
𝛼𝑠𝑎𝑓𝑒=

<!-- b000374 | prose | pages [8] -->
(𝑛)/𝑉(𝑛))]

<!-- b000375 | prose | pages [8] -->
. 𝑁⋅𝑇

<!-- b000376 | prose | pages [8] -->
In Table 5, we present the specific steps of our Monte Carlo simulation:

<!-- b000377 | furniture | pages [8] -->


<!-- b000378 | prose | pages [8] -->
Input Length of the lane, 𝑳. Duration of the simulation 𝑻.

<!-- b000379 | furniture | pages [9] -->
Team#29911

<!-- b000380 | prose | pages [9] -->
Vehicle density 𝒏. Deceleration probability 𝑷𝒅.

<!-- b000381 | furniture | pages [9] -->
Page 9 of 40

<!-- b000382 | furniture | pages [9] -->


<!-- b000383 | furniture | pages [9] -->


<!-- b000384 | furniture | pages [9] -->


<!-- b000385 | prose | pages [9] -->
Lane changing probability 𝑷𝒄. Output Traffic flow 𝑄. Safety index 𝛼𝑠𝑎𝑓𝑒. Energy cost 𝐸0 Randomly generate the initial position, speed and max speed of Step 1 vehicle 𝑖 𝑋(𝑘), 𝑉(𝑘) and 𝑉𝑚𝑎𝑥(𝑘). Step 2 Repeat Step 3 ~ 16 𝑇 times.

<!-- b000386 | prose | pages [9] -->
Repeat Step 4~5 for each vehicle Step 3

<!-- b000387 | prose | pages [9] -->
Apply the safety rule to vehicle 𝑖, skip Step 5 if vehicle 𝑖 doesn’t Step 4 pass the rule Apply either change lane rule #0 or change lane rule #1 to vehicle i Step 5 based on which lane it is on, its current speed and the current model, then decide whether it should change its lane. Update each vehicle to its new lane. Step 6

<!-- b000388 | prose | pages [9] -->
Repeat Step 8~16 for each vehicle number 𝑘. Step 7

<!-- b000389 | prose | pages [9] -->
Let the expected new speed 𝑉′(𝑘) = 𝑉(𝑘) + 1 Step 8

<!-- b000390 | prose | pages [9] -->
Step 9

<!-- b000391 | prose | pages [9] -->
𝑓(𝑘) < 𝑉′(𝑘) , let 𝑉′(𝑘) = Δ𝑋𝑝

<!-- b000392 | prose | pages [9] -->
If Δ𝑋𝑝

<!-- b000393 | prose | pages [9] -->
𝑓(𝑘) −1.

<!-- b000394 | prose | pages [9] -->
If 𝑉′(𝑘) > 0, generate a random number in [0, 1] and check Step 10 whether it is smaller than 𝑃𝑑, let 𝑉′(𝑘) = 𝑉′(𝑘) −1 if so. Step 11 Let 𝑋′(𝑘) = 𝑋(𝑘) + 𝑉′(𝑘)

<!-- b000395 | prose | pages [9] -->
Step 13

<!-- b000396 | prose | pages [9] -->
𝑓′(𝑘)

<!-- b000397 | prose | pages [9] -->
Δ𝑋𝑝

<!-- b000398 | prose | pages [9] -->
𝑉′(𝑘) )

<!-- b000399 | prose | pages [9] -->
𝛼𝑠𝑎𝑓𝑒= 𝛼𝑠𝑎𝑓𝑒+ exp (−

<!-- b000400 | prose | pages [9] -->
If 𝑋′(𝑘) ≥𝐿, then 𝑋′(𝑘)−= 𝐿, 𝑄= 𝑄+ 1 Step 14

<!-- b000401 | prose | pages [9] -->
If 𝑉(𝑘) < 𝑉′(𝑘), 𝐸0+= 𝑉(𝑘) + 𝑉′(𝑘) Step 15

<!-- b000402 | prose | pages [9] -->
Let 𝑋(𝑘) = 𝑋′(𝑘), 𝑉(𝑘) = 𝑉′(𝑘) Step 16

<!-- b000403 | prose | pages [9] -->
Step 17

<!-- b000404 | prose | pages [9] -->
𝛼𝑠𝑎𝑓𝑒

<!-- b000405 | prose | pages [9] -->
𝐸0

<!-- b000406 | prose | pages [9] -->
𝑄, 𝛼𝑠𝑎𝑓𝑒=

<!-- b000407 | prose | pages [9] -->
𝑄, 𝑄=

<!-- b000408 | prose | pages [9] -->
𝐸0 =

<!-- b000409 | prose | pages [9] -->
Step 18 Output and halt.

<!-- b000410 | prose | pages [9] -->
𝑄 𝑄

<!-- b000411 | prose | pages [9] -->
𝑇 𝑇

<!-- b000412 | caption | pages [9] -->
Table 5. Monte Carlo Procedures

<!-- b000413 | prose | pages [9] -->
 Vehicles of Two Kinds (Fast Cars & Slow Cars)

<!-- b000414 | prose | pages [9] -->
Next, we consider a more complex situation in which cars are classified into

<!-- b000415 | furniture | pages [9] -->


<!-- b000416 | prose | pages [9] -->
𝑓

<!-- b000417 | prose | pages [9] -->
fast cars and slow cars with respective maximum speed 𝑉𝑚𝑎𝑥

<!-- b000418 | prose | pages [9] -->
other conditions and rules unchanged.

<!-- b000419 | prose | pages [9] -->
and 𝑉𝑚𝑎𝑥

<!-- b000420 | prose | pages [9] -->
, with 𝑠

<!-- b000421 | furniture | pages [10] -->
Team#29911

<!-- b000422 | furniture | pages [10] -->
Page 10 of 40

<!-- b000423 | furniture | pages [10] -->


<!-- b000424 | furniture | pages [10] -->


<!-- b000425 | furniture | pages [10] -->


<!-- b000426 | prose | pages [10] -->
Next, we apply a similar Monte Carlo algorithm to simulate the traffic flow

<!-- b000427 | furniture | pages [10] -->


<!-- b000428 | prose | pages [10] -->
with two kinds of vehicles and output corresponding flow 𝑄 and safe index

<!-- b000429 | prose | pages [10] -->
𝛼𝑚𝑎𝑥.

<!-- b000430 | heading | pages [10] -->
3.1.2 Parameter Evaluation

<!-- b000431 | prose | pages [10] -->
 The length of the lattices 𝐿= 2048;

<!-- b000432 | prose | pages [10] -->
 The vehicle density 𝑛= 0.02, 0.04, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3;

<!-- b000433 | prose | pages [10] -->
 The number of the total vehicles 𝑁= 2𝑛𝐿;

<!-- b000434 | prose | pages [10] -->
 The duration of the simulation 𝑇= 4096;

<!-- b000435 | prose | pages [10] -->
 The deceleration probability 𝑃𝑑= 0.1;

<!-- b000436 | prose | pages [10] -->
 The change lane probability 𝑃𝑐= 0.7;

<!-- b000437 | prose | pages [10] -->
 In the case of vehicles of single kind, set maximum velocity 𝑉𝑚𝑎𝑥= 5;

<!-- b000438 | prose | pages [10] -->
𝑓

<!-- b000439 | prose | pages [10] -->
 In the case of vehicles of two kinds, set maximum velocity of fast car 𝑉𝑚𝑎𝑥

<!-- b000440 | prose | pages [10] -->
=

<!-- b000441 | prose | pages [10] -->
5, set maximum velocity for slow car 𝑉𝑚𝑎𝑥 = 3; 𝑠

<!-- b000442 | prose | pages [10] -->
 The ratio of fast car to slow car is 4:1, the initial number of vehicle in each

<!-- b000443 | prose | pages [10] -->
lane is 1:1.

<!-- b000444 | heading | pages [10] -->
3.1.3 Model Solution and Analysis

<!-- b000445 | prose | pages [10] -->
We mainly analyze the influence of the right-most rule on three parameters:

<!-- b000446 | furniture | pages [10] -->


<!-- b000447 | prose | pages [10] -->
Traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and average energy consumption 𝐸0. Then we

<!-- b000448 | prose | pages [10] -->
assign a relative weight to each parameter to calculate an optimal velocity during

<!-- b000449 | prose | pages [10] -->
light traffic and heavy traffic. We will only present the simulation result of the

<!-- b000450 | prose | pages [10] -->
two-kind vehicle model.

<!-- b000451 | prose | pages [10] -->
 Traffic Flow

<!-- b000452 | prose | pages [10] -->
As we have discussed before, we define the traffic flow 𝑄 as the number of

<!-- b000453 | furniture | pages [10] -->


<!-- b000454 | prose | pages [10] -->
cars passing a fixed point per unit time, or

<!-- b000455 | prose | pages [10] -->
𝑄= 𝑁𝑡𝑜𝑡𝑎𝑙

<!-- b000456 | furniture | pages [10] -->


<!-- b000457 | prose | pages [10] -->
𝑇

<!-- b000458 | prose | pages [10] -->
In Figure 3, we present the value of traffic flow 𝑄 under different vehicle

<!-- b000459 | furniture | pages [10] -->


<!-- b000460 | prose | pages [10] -->
density 𝑛.

<!-- b000461 | furniture | pages [11] -->
Team#29911

<!-- b000462 | furniture | pages [11] -->


<!-- b000463 | furniture | pages [11] -->


<!-- b000464 | furniture | pages [11] -->


<!-- b000465 | furniture | pages [11] -->


<!-- b000466 | furniture | pages [11] -->


<!-- b000467 | furniture | pages [11] -->


<!-- b000468 | furniture | pages [11] -->


<!-- b000469 | furniture | pages [11] -->


<!-- b000470 | furniture | pages [11] -->


<!-- b000471 | furniture | pages [11] -->


<!-- b000472 | furniture | pages [11] -->


<!-- b000473 | furniture | pages [11] -->


<!-- b000474 | furniture | pages [11] -->


<!-- b000475 | furniture | pages [11] -->
Page 11 of 40

<!-- b000476 | furniture | pages [11] -->


<!-- b000477 | furniture | pages [11] -->


<!-- b000478 | furniture | pages [11] -->


<!-- b000479 | caption | pages [11] -->
Figure 3. Relationship of Traffic Flow 𝑄 and Vehicle Density 𝑛

<!-- b000480 | prose | pages [11] -->
Apparently, the pattern in Figure 3 accords with realistic situation

<!-- b000481 | furniture | pages [11] -->


<!-- b000482 | prose | pages [11] -->
qualitatively. When the vehicle density on a freeway is relatively low, slight

<!-- b000483 | prose | pages [11] -->
increase of vehicle, or in other words, vehicle density will cause traffic flow to

<!-- b000484 | prose | pages [11] -->
rise dramatically because according to our rules vehicles accelerate very easily. In

<!-- b000485 | prose | pages [11] -->
our simulation, the peak value of flow 𝑄 occurs when density is around 0.2.

<!-- b000486 | prose | pages [11] -->
After the climax, the traffic flow will tend to drop as vehicle density continues to

<!-- b000487 | prose | pages [11] -->
rise because more likely car jams will obstruct vehicles from accelerating freely.

<!-- b000488 | prose | pages [11] -->
Finally, when the density approaches 1, in other words, the freeway is almost

<!-- b000489 | prose | pages [11] -->
"full", vehicles could barely move thus the flow approaches 0.

<!-- b000490 | prose | pages [11] -->
 Safety Index

<!-- b000491 | prose | pages [11] -->
Notice that the longer reaction time is, the safer the situation will be. Thus

<!-- b000492 | furniture | pages [11] -->


<!-- b000493 | prose | pages [11] -->
according to our definition of the safety index

<!-- b000494 | prose | pages [11] -->
𝑁 𝑓

<!-- b000495 | prose | pages [11] -->
∑∑[exp(−Δ𝑝

<!-- b000496 | prose | pages [11] -->
𝑇 1

<!-- b000497 | prose | pages [11] -->
𝛼𝑠𝑎𝑓𝑒=

<!-- b000498 | prose | pages [11] -->
𝑋(𝑛)/𝑉(𝑛))]

<!-- b000499 | furniture | pages [11] -->


<!-- b000500 | prose | pages [11] -->
𝑁⋅𝑇

<!-- b000501 | prose | pages [11] -->
a larger value of 𝛼𝑠𝑎𝑓𝑒 indicates a more dangerous situation. We again plot

<!-- b000502 | prose | pages [11] -->
safety index 𝛼𝑠𝑎𝑓𝑒 against vehicle density 𝑛. The result is shown in Figure 4.

<!-- b000503 | furniture | pages [11] -->


<!-- b000504 | furniture | pages [11] -->


<!-- b000505 | furniture | pages [12] -->
Team#29911

<!-- b000506 | furniture | pages [12] -->


<!-- b000507 | furniture | pages [12] -->


<!-- b000508 | furniture | pages [12] -->


<!-- b000509 | furniture | pages [12] -->


<!-- b000510 | furniture | pages [12] -->


<!-- b000511 | furniture | pages [12] -->


<!-- b000512 | furniture | pages [12] -->


<!-- b000513 | furniture | pages [12] -->


<!-- b000514 | furniture | pages [12] -->


<!-- b000515 | furniture | pages [12] -->


<!-- b000516 | furniture | pages [12] -->


<!-- b000517 | furniture | pages [12] -->


<!-- b000518 | furniture | pages [12] -->
Page 12 of 40

<!-- b000519 | furniture | pages [12] -->


<!-- b000520 | furniture | pages [12] -->


<!-- b000521 | furniture | pages [12] -->


<!-- b000522 | caption | pages [12] -->
Figure 4. Relationship of Safety Index 𝛼𝑠𝑎𝑓𝑒

<!-- b000523 | prose | pages [12] -->
and Vehicle Density 𝑛 (lower is safer)

<!-- b000524 | prose | pages [12] -->
It is easy to understand the pattern in Figure 4. When the vehicle density is

<!-- b000525 | furniture | pages [12] -->


<!-- b000526 | prose | pages [12] -->
relatively small, accidental risk rises as the number of car increases because

<!-- b000527 | prose | pages [12] -->
vehicles are likely to attain high velocities. After the peak value, the risk drops as

<!-- b000528 | prose | pages [12] -->
density rises because though the number of vehicle rises, the average velocity

<!-- b000529 | prose | pages [12] -->
decreases dramatically. Since most vehicles drive much slower, the overall

<!-- b000530 | prose | pages [12] -->
situation becomes actually safer. Finally, when all the vehicles cannot move at all

<!-- b000531 | prose | pages [12] -->
(when 𝑛= 1), the situation is absolutely safe. Notice that the climax vehicle

<!-- b000532 | prose | pages [12] -->
density are nearly the same in traffic flow and safety index because both

<!-- b000533 | prose | pages [12] -->
quantities are closely related to average velocity.

<!-- b000534 | prose | pages [12] -->
 Average Energy Consumption

<!-- b000535 | prose | pages [12] -->
Now we define another important parameter called the average energy

<!-- b000536 | furniture | pages [12] -->


<!-- b000537 | prose | pages [12] -->
consumption denoted 𝐸0. We use it to measure the energy consumed during

<!-- b000538 | prose | pages [12] -->
each acceleration. We approximate the quantity as proportionate to change of

<!-- b000539 | prose | pages [12] -->
kinetic energy. For a particular vehicle 𝑛, we denote its velocity at time 𝑡 and

<!-- b000540 | prose | pages [12] -->
𝑡+ 1 as 𝑉(𝑡)(𝑛) and 𝑉(𝑡+1)(𝑛). Furthermore, we make the assumption that

<!-- b000541 | prose | pages [12] -->
each vehicle has unit mass. Now we can derive the formula for 𝐸0:

<!-- b000542 | prose | pages [12] -->
1 2 𝑚[(𝑉(𝑡)(𝑛))2 −(𝑉(𝑡−1)(𝑛))2] 𝑇 𝑁 ∑ ∑ 𝑡=1 𝑛=1

<!-- b000543 | prose | pages [12] -->
𝐸0 ∝

<!-- b000544 | prose | pages [12] -->
1 𝑇 𝑁

<!-- b000545 | furniture | pages [12] -->


<!-- b000546 | prose | pages [12] -->
𝑄

<!-- b000547 | prose | pages [12] -->
2 𝑚[𝑉(𝑡)(𝑛) −𝑉(𝑡−1)(𝑛)][𝑉(𝑡)(𝑛) + 𝑉(𝑡−1)(𝑛)] ∑ ∑ 𝑡=1 𝑛=1

<!-- b000548 | prose | pages [12] -->
∝

<!-- b000549 | furniture | pages [12] -->


<!-- b000550 | prose | pages [12] -->
𝑄

<!-- b000551 | furniture | pages [13] -->
Team#29911

<!-- b000552 | prose | pages [13] -->
𝑇 𝑁

<!-- b000553 | furniture | pages [13] -->
Page 13 of 40

<!-- b000554 | furniture | pages [13] -->


<!-- b000555 | furniture | pages [13] -->


<!-- b000556 | furniture | pages [13] -->


<!-- b000557 | prose | pages [13] -->
[𝑉(𝑡)(𝑛) + 𝑉(𝑡−1)(𝑛)] ∑ ∑ 𝑡=1 𝑛=1

<!-- b000558 | prose | pages [13] -->
∝

<!-- b000559 | prose | pages [13] -->
𝑄

<!-- b000560 | furniture | pages [13] -->


<!-- b000561 | prose | pages [13] -->
In order for convenience, we evaluate the proportionate coefficient as 1. So

<!-- b000562 | furniture | pages [13] -->


<!-- b000563 | prose | pages [13] -->
that

<!-- b000564 | prose | pages [13] -->
𝑇 𝑁 [𝑉(𝑡)(𝑛) + 𝑉(𝑡−1)(𝑛)] ∑ ∑ 𝑡=1 𝑛=1

<!-- b000565 | prose | pages [13] -->
𝐸0 =

<!-- b000566 | furniture | pages [13] -->


<!-- b000567 | prose | pages [13] -->
𝑄

<!-- b000568 | prose | pages [13] -->
We again plot the average energy consumption against vehicle density in

<!-- b000569 | furniture | pages [13] -->


<!-- b000570 | caption | pages [13] -->
Figure 5.

<!-- b000571 | furniture | pages [13] -->


<!-- b000572 | furniture | pages [13] -->


<!-- b000573 | furniture | pages [13] -->


<!-- b000574 | furniture | pages [13] -->


<!-- b000575 | furniture | pages [13] -->


<!-- b000576 | furniture | pages [13] -->


<!-- b000577 | furniture | pages [13] -->


<!-- b000578 | furniture | pages [13] -->


<!-- b000579 | furniture | pages [13] -->


<!-- b000580 | furniture | pages [13] -->


<!-- b000581 | furniture | pages [13] -->


<!-- b000582 | furniture | pages [13] -->


<!-- b000583 | caption | pages [13] -->
Figure 5. Relationship of Energy Consumption 𝐸0

<!-- b000584 | prose | pages [13] -->
and Vehicle Density 𝑛 (lower is better)

<!-- b000585 | prose | pages [13] -->
In the first half of the figure, the increase of 𝐸0 could be explained by the

<!-- b000586 | furniture | pages [13] -->


<!-- b000587 | prose | pages [13] -->
frequent lane changing and acceleration due to a low vehicle density. In the latter

<!-- b000588 | prose | pages [13] -->
half, although vehicles are much less likely to accelerate, notice that traffic flow

<!-- b000589 | prose | pages [13] -->
also falls dramatically, therefore the average energy consumption still increases.

<!-- b000590 | prose | pages [13] -->
 Optimal Maximum Velocity Estimation (Weighted)

<!-- b000591 | prose | pages [13] -->
In this section, we will design a weighted function 𝜙 dependent on the three

<!-- b000592 | furniture | pages [13] -->


<!-- b000593 | prose | pages [13] -->
key variables---traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and average energy

<!-- b000594 | prose | pages [13] -->
consumption 𝐸0. Then we will calculate an optimal speed limit to maximize the

<!-- b000595 | prose | pages [13] -->
value of 𝜙 under light traffic and heavy traffic respectively.

<!-- b000596 | prose | pages [13] -->
We define the weighted function as follows:

<!-- b000597 | furniture | pages [13] -->


<!-- b000598 | prose | pages [13] -->
800) + 𝜔3√1 −(𝛼𝑠𝑎𝑓𝑒 1.2 + 𝜔2(1 −𝐸0 𝑄

<!-- b000599 | prose | pages [13] -->
𝜙(𝑄, 𝛼𝑠𝑎𝑓𝑒, 𝐸0) = 𝜔1

<!-- b000600 | prose | pages [13] -->
3

<!-- b000601 | furniture | pages [13] -->


<!-- b000602 | prose | pages [13] -->
0.4 )3

<!-- b000603 | furniture | pages [14] -->
Team#29911

<!-- b000604 | furniture | pages [14] -->


<!-- b000605 | furniture | pages [14] -->
Page 14 of 40

<!-- b000606 | furniture | pages [14] -->


<!-- b000607 | furniture | pages [14] -->


<!-- b000608 | furniture | pages [14] -->


<!-- b000609 | prose | pages [14] -->
𝑠. 𝑡.        𝜔1 + 𝜔2 + 𝜔3 = 1

<!-- b000610 | furniture | pages [14] -->


<!-- b000611 | prose | pages [14] -->
where  𝜔1, 𝜔2, 𝜔3 are weight coefficient.  We base on the following four rules

<!-- b000612 | prose | pages [14] -->
to design our function:

<!-- b000613 | prose | pages [14] -->
When 𝜙 reaches its peak value, we define the corresponding 𝑉𝑚𝑎𝑥 to be 

<!-- b000614 | furniture | pages [14] -->


<!-- b000615 | prose | pages [14] -->
the optimal maximum velocity;

<!-- b000616 | prose | pages [14] -->
Since the three variables 𝑄, 𝛼𝑠𝑎𝑓𝑒, 𝐸0 are independent of each other, 𝜙 

<!-- b000617 | prose | pages [14] -->
should be expressed in the form of simple sums.

<!-- b000618 | furniture | pages [14] -->


<!-- b000619 | prose | pages [14] -->
𝑄 and 𝐸0 should appear in linear forms in 𝜙; 

<!-- b000620 | prose | pages [14] -->
The value of 𝜙 should drop sharply when the safety index is rather high 

<!-- b000621 | prose | pages [14] -->
Hence 𝛼𝑠𝑎𝑓𝑒 should appear in the form of an upward-convex-function in 𝜙.

<!-- b000622 | furniture | pages [14] -->


<!-- b000623 | prose | pages [14] -->
Now under light traffic where 𝑛= 0.1 and heavy traffic where 𝑛= 0.2

<!-- b000624 | furniture | pages [14] -->


<!-- b000625 | prose | pages [14] -->
𝑙𝑖𝑔ℎ𝑡

<!-- b000626 | prose | pages [14] -->
ℎ𝑒𝑎𝑣𝑦. We plot

<!-- b000627 | prose | pages [14] -->
respectively we can calculate the corresponding 𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙

<!-- b000628 | prose | pages [14] -->
and 𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙

<!-- b000629 | prose | pages [14] -->
𝜙 against different values of 𝑉𝑚𝑎𝑥 under the condition (𝜔1 = 0.5, 𝜔2 =

<!-- b000630 | prose | pages [14] -->
0.2, 𝜔3 = 0.3) in Figure 6 and Figure 7.

<!-- b000631 | prose | pages [14] -->


<!-- b000632 | prose | pages [14] -->


<!-- b000633 | prose | pages [14] -->


<!-- b000634 | prose | pages [14] -->


<!-- b000635 | prose | pages [14] -->


<!-- b000636 | prose | pages [14] -->


<!-- b000637 | prose | pages [14] -->


<!-- b000638 | prose | pages [14] -->


<!-- b000639 | prose | pages [14] -->


<!-- b000640 | prose | pages [14] -->


<!-- b000641 | prose | pages [14] -->


<!-- b000642 | prose | pages [14] -->


<!-- b000643 | prose | pages [14] -->


<!-- b000644 | caption | pages [14] -->
Figure 6. Optimal Maximum Velocity (Light Traffic)

<!-- b000645 | furniture | pages [14] -->


<!-- b000646 | furniture | pages [14] -->


<!-- b000647 | furniture | pages [15] -->
Page 15 of 40

<!-- b000648 | furniture | pages [15] -->
Team#29911

<!-- b000649 | furniture | pages [15] -->


<!-- b000650 | furniture | pages [15] -->


<!-- b000651 | furniture | pages [15] -->


<!-- b000652 | furniture | pages [15] -->


<!-- b000653 | furniture | pages [15] -->


<!-- b000654 | furniture | pages [15] -->


<!-- b000655 | furniture | pages [15] -->


<!-- b000656 | furniture | pages [15] -->


<!-- b000657 | furniture | pages [15] -->


<!-- b000658 | furniture | pages [15] -->


<!-- b000659 | furniture | pages [15] -->


<!-- b000660 | furniture | pages [15] -->


<!-- b000661 | furniture | pages [15] -->


<!-- b000662 | caption | pages [15] -->
Figure 7. Optimal Maximum Velocity (Heavy Traffic)

<!-- b000663 | furniture | pages [15] -->


<!-- b000664 | prose | pages [15] -->
Considering the duration of light traffic and heavy traffic in a given time

<!-- b000665 | prose | pages [15] -->
period, we set the ratio 4:1 (light :heavy) to obtain the result for a "mixed- traffic"

<!-- b000666 | prose | pages [15] -->
situation. See in Figure 8.

<!-- b000667 | prose | pages [15] -->


<!-- b000668 | prose | pages [15] -->


<!-- b000669 | prose | pages [15] -->


<!-- b000670 | prose | pages [15] -->


<!-- b000671 | prose | pages [15] -->


<!-- b000672 | prose | pages [15] -->


<!-- b000673 | prose | pages [15] -->


<!-- b000674 | prose | pages [15] -->


<!-- b000675 | prose | pages [15] -->


<!-- b000676 | prose | pages [15] -->


<!-- b000677 | prose | pages [15] -->


<!-- b000678 | prose | pages [15] -->


<!-- b000679 | prose | pages [15] -->


<!-- b000680 | caption | pages [15] -->
Figure 8. Optimal Maximum Velocity (combined)

<!-- b000681 | furniture | pages [15] -->


<!-- b000682 | prose | pages [15] -->
As shown in Figure 8, the global maximum value of 𝜙 locates at 𝑉𝑚𝑎𝑥= 5,

<!-- b000683 | prose | pages [15] -->
therefore the optimal maximum velocity 𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙= 5. In other words, when we

<!-- b000684 | prose | pages [15] -->
set the speed limit at 5, we achieve a weighted optimization of traffic flow, safety

<!-- b000685 | prose | pages [15] -->
index and energy consumption.

<!-- b000686 | prose | pages [15] -->
 Analysis of Under-Posted and Over-Posted Speed Limits

<!-- b000687 | furniture | pages [15] -->


<!-- b000688 | prose | pages [15] -->
In the section above, we have calculated the optimal maximum velocity

<!-- b000689 | prose | pages [15] -->
𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙= 5. We will discuss the influence of under-posted and over-posted

<!-- b000690 | prose | pages [15] -->
speed limits in light and heavy traffic respectively.

<!-- b000691 | furniture | pages [16] -->
Page 16 of 40

<!-- b000692 | furniture | pages [16] -->
Team#29911

<!-- b000693 | furniture | pages [16] -->


<!-- b000694 | furniture | pages [16] -->


<!-- b000695 | prose | pages [16] -->
 Light Traffic

<!-- b000696 | furniture | pages [16] -->


<!-- b000697 | furniture | pages [16] -->


<!-- b000698 | prose | pages [16] -->
If a speed limit is over-posted, say, 𝑉𝑚𝑎𝑥= 7, traffic flow, safety index and

<!-- b000699 | prose | pages [16] -->
average energy consumption all increase. In other words, we sacrifice energy and

<!-- b000700 | prose | pages [16] -->
safety for larger traffic flow.

<!-- b000701 | furniture | pages [16] -->


<!-- b000702 | prose | pages [16] -->
If a speed limit is under-posted, say, 𝑉𝑚𝑎𝑥= 3, traffic flow, safety index and

<!-- b000703 | prose | pages [16] -->
average energy consumption all decrease. In other words, we sacrifice traffic

<!-- b000704 | prose | pages [16] -->
flow for lower energy consumption and a safer condition.

<!-- b000705 | prose | pages [16] -->
 Heavy Traffic

<!-- b000706 | furniture | pages [16] -->


<!-- b000707 | prose | pages [16] -->
If a speed limit is over-posted, say, 𝑉𝑚𝑎𝑥= 7, traffic flow will remain almost the same while energy consumption and safety index will rise. This is highly unwelcome.

<!-- b000708 | furniture | pages [16] -->


<!-- b000709 | prose | pages [16] -->
If a speed limit is under-posted, say, 𝑉𝑚𝑎𝑥= 3, situation will be similar to that of light traffic. Still, we will be sacrificing traffic flow for lower energy consumption and a safer condition.

<!-- b000710 | prose | pages [16] -->
 Visualization

<!-- b000711 | furniture | pages [16] -->


<!-- b000712 | prose | pages [16] -->
To make our simulation results more intuitive, we use MATLAB to visualize

<!-- b000713 | prose | pages [16] -->
our simulation. In the figures below, each row signifies the distribution of

<!-- b000714 | prose | pages [16] -->
vehicles with black dots representing vehicles occupation and margin

<!-- b000715 | prose | pages [16] -->
representing empty space. Time increases from bottom to top and vehicles move

<!-- b000716 | prose | pages [16] -->
from left to right. We visualize our simulation at low vehicle density (𝑛= 0.05)

<!-- b000717 | prose | pages [16] -->
and high density (𝑛= 0.2) respectively in Figure 9 and Figure 10. Subfigure on

<!-- b000718 | prose | pages [16] -->
the left represents the left lane and the subfigure on the right represents the

<!-- b000719 | prose | pages [16] -->
right lane.

<!-- b000720 | furniture | pages [16] -->


<!-- b000721 | furniture | pages [16] -->


<!-- b000722 | furniture | pages [16] -->


<!-- b000723 | furniture | pages [16] -->


<!-- b000724 | furniture | pages [16] -->


<!-- b000725 | furniture | pages [16] -->


<!-- b000726 | furniture | pages [16] -->


<!-- b000727 | furniture | pages [16] -->


<!-- b000728 | furniture | pages [16] -->


<!-- b000729 | furniture | pages [16] -->


<!-- b000730 | furniture | pages [16] -->


<!-- b000731 | caption | pages [16] -->
Figure 9. Visualization at Low Density

<!-- b000732 | furniture | pages [16] -->


<!-- b000733 | furniture | pages [17] -->
Team#29911

<!-- b000734 | furniture | pages [17] -->


<!-- b000735 | furniture | pages [17] -->


<!-- b000736 | furniture | pages [17] -->


<!-- b000737 | furniture | pages [17] -->


<!-- b000738 | furniture | pages [17] -->


<!-- b000739 | furniture | pages [17] -->


<!-- b000740 | furniture | pages [17] -->


<!-- b000741 | furniture | pages [17] -->


<!-- b000742 | furniture | pages [17] -->


<!-- b000743 | furniture | pages [17] -->


<!-- b000744 | furniture | pages [17] -->


<!-- b000745 | furniture | pages [17] -->


<!-- b000746 | furniture | pages [17] -->
Page 17 of 40

<!-- b000747 | furniture | pages [17] -->


<!-- b000748 | furniture | pages [17] -->


<!-- b000749 | furniture | pages [17] -->


<!-- b000750 | caption | pages [17] -->
Figure 10. Visualization at High Density

<!-- b000751 | heading | pages [17] -->
3.2 Continuum Modeling for Right-Most Rule

<!-- b000752 | prose | pages [17] -->
Apart from the discrete, microscopic cellular automaton (CA) models we

<!-- b000753 | furniture | pages [17] -->


<!-- b000754 | prose | pages [17] -->
have adopted above, in this section we will establish a continuum, macroscopic

<!-- b000755 | prose | pages [17] -->
model to describe the vehicle flow on the freeway.

<!-- b000756 | heading | pages [17] -->
3.2.1 Model Establishment

<!-- b000757 | prose | pages [17] -->
Our ultimate goal is to make a continuum model for the traffic flow on a

<!-- b000758 | furniture | pages [17] -->


<!-- b000759 | prose | pages [17] -->
double-lane freeway.

<!-- b000760 | prose | pages [17] -->
We start our work from the single-lane

<!-- b000761 | prose | pages [17] -->
situation.  According to [4], we can use partial-derivative equations (PDE)

<!-- b000762 | prose | pages [17] -->
system to describe the traffic flow on a single-lane freeway. There are two

<!-- b000763 | prose | pages [17] -->
variables in the equation system: the average speed of vehicles 𝑢(𝑥, 𝑡) and the

<!-- b000764 | prose | pages [17] -->
density of vehicles 𝜌(𝑥, 𝑡). The PDE system contains two parts:

<!-- b000765 | prose | pages [17] -->
Continuity equation:

<!-- b000766 | prose | pages [17] -->
𝜕𝑡+ 𝜕(𝜌𝑢)

<!-- b000767 | prose | pages [17] -->
𝜕𝑢

<!-- b000768 | prose | pages [17] -->
Dynamic equation:

<!-- b000769 | prose | pages [17] -->
= 0 𝜕𝑥

<!-- b000770 | prose | pages [17] -->
𝜕𝑥= 𝑢𝑒(𝜌) −𝑢

<!-- b000771 | prose | pages [17] -->
𝜕𝑢

<!-- b000772 | prose | pages [17] -->
𝜕𝑡+ 𝑢𝜕𝑢

<!-- b000773 | prose | pages [17] -->
𝜕𝑢 𝜕𝑥

<!-- b000774 | prose | pages [17] -->
+ 𝑐0 𝑇

<!-- b000775 | prose | pages [17] -->
In the second equation, the right side contains a relaxation term (𝑢𝑒(𝜌) −

<!-- b000776 | furniture | pages [17] -->


<!-- b000777 | prose | pages [17] -->
𝑢)/𝑇, which reflects the process when a driver tries to adjust his velocity to the

<!-- b000778 | prose | pages [17] -->
equilibrium velocity 𝑢𝑒(𝜌) in the time interval 𝑇 and an anticipation term

<!-- b000779 | prose | pages [17] -->
𝑐0𝜕𝑢/𝜕𝑥, which represents the process when the driver reacts to the traffic

<!-- b000780 | prose | pages [17] -->
condition ahead with the propagation speed of small disturbance 𝑐0.

<!-- b000781 | furniture | pages [18] -->
Team#29911

<!-- b000782 | furniture | pages [18] -->
Page 18 of 40

<!-- b000783 | furniture | pages [18] -->


<!-- b000784 | furniture | pages [18] -->


<!-- b000785 | furniture | pages [18] -->


<!-- b000786 | prose | pages [18] -->
Now we extend that model to accommodate the double-lane situation to

<!-- b000787 | furniture | pages [18] -->


<!-- b000788 | prose | pages [18] -->
accommodate the "keep-right-except-to-pass" rule. We will establish the

<!-- b000789 | prose | pages [18] -->
equations for the two lanes separately. In order to describe lane-changing

<!-- b000790 | prose | pages [18] -->
between the right (driving) lane and the left (overtaking) lane, we will introduce

<!-- b000791 | prose | pages [18] -->
two variables 𝑆𝑗𝑖 and 𝑆𝑖𝑗, which represent the lane changing rate. In particular,

<!-- b000792 | prose | pages [18] -->
𝑆𝑗𝑖 denotes the changing rate from lane 𝑖 to lane 𝑗(𝑖, 𝑗∈{1,2}). The overtaking

<!-- b000793 | prose | pages [18] -->
lane is denoted by Lane 1 and the driving lane is denoted by Lane 2. Thus, the net

<!-- b000794 | prose | pages [18] -->
lane change into lane 𝑖 is 𝑆𝑗𝑖 −𝑆𝑖𝑗.

<!-- b000795 | prose | pages [18] -->
Hence the continuity equation could be written as:

<!-- b000796 | furniture | pages [18] -->


<!-- b000797 | prose | pages [18] -->
𝜕𝜌𝑖

<!-- b000798 | prose | pages [18] -->
𝜕𝑡+ 𝜕(𝜌𝑖𝑢𝑖)

<!-- b000799 | prose | pages [18] -->
𝜕𝑥 = 𝑆𝑗𝑖 −𝑆𝑖𝑗

<!-- b000800 | prose | pages [18] -->
For the dynamic equation, we introduce two constant parameters 𝑟1, 𝑟2 to

<!-- b000801 | furniture | pages [18] -->


<!-- b000802 | prose | pages [18] -->
be the coefficients of 𝑆𝑗𝑖, 𝑆𝑖𝑗. The equation should be:

<!-- b000803 | prose | pages [18] -->
𝜕𝑢𝑖

<!-- b000804 | prose | pages [18] -->
𝜕𝑢𝑖

<!-- b000805 | prose | pages [18] -->
𝜕𝑥= 𝑢𝑒𝑖(𝜌𝑖) −𝑢𝑖

<!-- b000806 | prose | pages [18] -->
𝜕𝑡+ 𝑢𝑖

<!-- b000807 | prose | pages [18] -->
+ 𝑐0𝑖

<!-- b000808 | prose | pages [18] -->
𝑇𝑖

<!-- b000809 | furniture | pages [18] -->


<!-- b000810 | prose | pages [18] -->
According to [5], we assume:

<!-- b000811 | prose | pages [18] -->
𝑆12 = 𝑎𝑄𝑒1(𝜌̅)𝜌1(1 −

<!-- b000812 | prose | pages [18] -->
𝜕𝑢𝑖

<!-- b000813 | prose | pages [18] -->
𝜕𝑥+ 𝑟1𝑆𝑖𝑗−𝑟2𝑆𝑗𝑖      (𝑖= 1,2)

<!-- b000814 | prose | pages [18] -->
𝜌2 𝜌𝑚 )

<!-- b000815 | prose | pages [18] -->
𝜌1

<!-- b000816 | prose | pages [18] -->
𝑆21 = 𝑎(1 + 𝑏(𝑄𝑒1(𝜌̅) −𝑄𝑒2(𝜌̅)))𝑄𝑒2(𝜌̅)𝜌2(1 −

<!-- b000817 | prose | pages [18] -->
𝜌𝑚 )

<!-- b000818 | prose | pages [18] -->
where 𝑄𝑒1 denotes the equilibrium flow 𝑄𝑒1 = 𝜌1𝑢𝑒1(𝜌1)

<!-- b000819 | prose | pages [18] -->
𝜌̅  denotes the average density of Lane 1 and Lane 2 𝜌̅ = (𝜌1 + 𝜌2)/2

<!-- b000820 | prose | pages [18] -->
𝜌𝑚 denotes the density in a jam

<!-- b000821 | prose | pages [18] -->
𝑎, 𝑏 are two constant parameters.

<!-- b000822 | prose | pages [18] -->
Such assumption is reasonable. Firstly, notice that the expression of 𝑆12 and

<!-- b000823 | furniture | pages [18] -->


<!-- b000824 | prose | pages [18] -->
𝑆21 is not symmetric because of the asymmetricity of the double-lane freeway.

<!-- b000825 | prose | pages [18] -->
Secondly, if Lane 2 is suffering from a traffic jam, then 𝜌2 = 𝜌𝑚; if there are no

<!-- b000826 | prose | pages [18] -->
vehicles in overtaking lane 1,then 𝜌1 = 0. Under both circumstances, we can

<!-- b000827 | prose | pages [18] -->
derive 𝑆12 = 0, which implies that no car can change into the driving lane when

<!-- b000828 | prose | pages [18] -->
it has a traffic jam or when there are no vehicles on the overtaking lane.

<!-- b000829 | heading | pages [18] -->
3.2.2 Model Solution and Analysis

<!-- b000830 | prose | pages [18] -->
Study of Steady State

<!-- b000831 | prose | pages [18] -->
According to theories of PDE, we can obtain a steady state solution of our

<!-- b000832 | furniture | pages [18] -->


<!-- b000833 | furniture | pages [19] -->
Team#29911

<!-- b000834 | furniture | pages [19] -->
Page 19 of 40

<!-- b000835 | furniture | pages [19] -->


<!-- b000836 | furniture | pages [19] -->


<!-- b000837 | furniture | pages [19] -->


<!-- b000838 | prose | pages [19] -->
model by setting the derivative terms to zero. Then we can derive the following

<!-- b000839 | prose | pages [19] -->
two equations:

<!-- b000840 | prose | pages [19] -->
) = (1 + 𝑏(𝑄𝑒1(𝜌̅) −𝑄𝑒2(𝜌̅)))𝑄𝑒2(𝜌̅)𝜌2(1 −𝜌1

<!-- b000841 | prose | pages [19] -->
𝑄𝑒1(𝜌̅)𝜌1(1 −𝜌2

<!-- b000842 | prose | pages [19] -->
𝜌𝑚

<!-- b000843 | prose | pages [19] -->
𝑢𝑒𝑖(𝜌𝑖) −𝑢𝑖

<!-- b000844 | prose | pages [19] -->
𝜕𝑢𝑖

<!-- b000845 | prose | pages [19] -->
)

<!-- b000846 | prose | pages [19] -->
𝜌𝑚

<!-- b000847 | prose | pages [19] -->
𝜕𝑥+ 𝑟1𝑆𝑖𝑗−𝑟2𝑆𝑗𝑖= 0    (𝑖= 1,2)

<!-- b000848 | prose | pages [19] -->
+ 𝑐0𝑖

<!-- b000849 | prose | pages [19] -->
𝑇𝑖

<!-- b000850 | prose | pages [19] -->
Plugging in 2𝜌̅ = 𝜌1 + 𝜌2, we can derive the expression of 𝑢𝑒1(𝜌) and

<!-- b000851 | furniture | pages [19] -->


<!-- b000852 | prose | pages [19] -->
𝑢𝑒2(𝜌) from the equations above according to [6]:

<!-- b000853 | prose | pages [19] -->
𝜌

<!-- b000854 | prose | pages [19] -->
𝑢𝑒1(𝜌) = 𝑢𝑓(1 −

<!-- b000855 | prose | pages [19] -->
𝜌

<!-- b000856 | prose | pages [19] -->
𝜌𝑚)4)

<!-- b000857 | prose | pages [19] -->
𝜌𝑚)/(1 + 𝐸(

<!-- b000858 | prose | pages [19] -->
𝜌

<!-- b000859 | prose | pages [19] -->
𝜌

<!-- b000860 | prose | pages [19] -->
1

<!-- b000861 | prose | pages [19] -->
𝜌

<!-- b000862 | prose | pages [19] -->
𝜌𝑚)4)(

<!-- b000863 | prose | pages [19] -->
𝜌𝑚)/(1 + 𝐸(

<!-- b000864 | prose | pages [19] -->
𝑢𝑓(1 −

<!-- b000865 | prose | pages [19] -->
𝑢𝑒2(𝜌) = {

<!-- b000866 | prose | pages [19] -->
𝜌

<!-- b000867 | prose | pages [19] -->
2 +

<!-- b000868 | prose | pages [19] -->
2𝜌𝑐)     (𝜌< 𝜌𝑐)

<!-- b000869 | furniture | pages [19] -->


<!-- b000870 | prose | pages [19] -->
𝜌

<!-- b000871 | prose | pages [19] -->
𝜌𝑚)4)                      (𝜌≥𝜌𝑐)

<!-- b000872 | prose | pages [19] -->
𝜌𝑚)/(1 + 𝐸(

<!-- b000873 | prose | pages [19] -->
𝑢𝑓(1 −

<!-- b000874 | furniture | pages [19] -->


<!-- b000875 | prose | pages [19] -->
where 𝑢𝑓 denotes the free flow speed and 𝐸 is a constant parameter.

<!-- b000876 | prose | pages [19] -->
Using the relationship given above, we can derive the relationship between

<!-- b000877 | furniture | pages [19] -->


<!-- b000878 | prose | pages [19] -->
𝑢𝑖 and 𝜌̅. Then we use the definition 𝑞𝑖= 𝜌𝑖𝑢𝑖 to express the flow on each lane

<!-- b000879 | prose | pages [19] -->
with the average density 𝜌̅.

<!-- b000880 | prose | pages [19] -->
According to [7], we assign the following values to the parameters:

<!-- b000881 | furniture | pages [19] -->


<!-- b000882 | prose | pages [19] -->
𝑇1 = 𝑇2 = 10𝑠, 𝑢𝑓= 30 𝑚/𝑠, 𝑎= 0.01, 𝑏= 5, 𝑐01 = 𝑐02 = 10𝑚/𝑠

<!-- b000883 | prose | pages [19] -->
𝜌𝑚= 0.14 𝑣𝑒ℎ/𝑚, 𝑟1 = 150𝑚2/𝑠, 𝑟2 = 50𝑚2/𝑠, 𝜌𝑐= 0.05 𝑣𝑒ℎ/𝑚, 𝐸= 100.

<!-- b000884 | prose | pages [19] -->
Since we have established the traffic flow function of average density on both

<!-- b000885 | furniture | pages [19] -->


<!-- b000886 | prose | pages [19] -->
lane, we can plot the relationship as shown in Figure 11.

<!-- b000887 | furniture | pages [19] -->


<!-- b000888 | furniture | pages [19] -->


<!-- b000889 | furniture | pages [19] -->


<!-- b000890 | furniture | pages [19] -->


<!-- b000891 | furniture | pages [19] -->


<!-- b000892 | furniture | pages [19] -->


<!-- b000893 | furniture | pages [19] -->


<!-- b000894 | furniture | pages [19] -->


<!-- b000895 | furniture | pages [19] -->


<!-- b000896 | furniture | pages [19] -->


<!-- b000897 | furniture | pages [19] -->


<!-- b000898 | furniture | pages [19] -->


<!-- b000899 | furniture | pages [19] -->


<!-- b000900 | caption | pages [19] -->
Figure 11. The Relationship of Traffic Flow 𝑄 and Average Density 𝜌̅

<!-- b000901 | prose | pages [19] -->
In Figure 11, we can discover that all three kinds of flows experience a

<!-- b000902 | furniture | pages [19] -->


<!-- b000903 | furniture | pages [20] -->
Team#29911

<!-- b000904 | furniture | pages [20] -->
Page 20 of 40

<!-- b000905 | furniture | pages [20] -->


<!-- b000906 | furniture | pages [20] -->


<!-- b000907 | furniture | pages [20] -->


<!-- b000908 | prose | pages [20] -->
similar changing pattern---when the average density is relatively small, traffic

<!-- b000909 | prose | pages [20] -->
flow experiences a monotonic increase as the density gets larger. After reaching

<!-- b000910 | prose | pages [20] -->
its climax, the flow drops gradually to 0 as the density keeps rising. This changing

<!-- b000911 | prose | pages [20] -->
pattern is identical to the results we have obtained in the discrete model. We can

<!-- b000912 | prose | pages [20] -->
also discover that the overtaking (fast) lane reaches its climax sooner than that of

<!-- b000913 | prose | pages [20] -->
the driving (slow) lane. Due to difference of the maximum velocity, the peak

<!-- b000914 | prose | pages [20] -->
value of fast lane's traffic flow is larger than that of the slow lane. In addition, the

<!-- b000915 | prose | pages [20] -->
curves of fast lane and slow lane almost overlap when 𝜌> 𝜌𝑐= 0.05. The

<!-- b000916 | prose | pages [20] -->
overlapping part of curves actually indicates that the utility rate of both lanes is

<!-- b000917 | prose | pages [20] -->
almost the same when 𝜌 is relatively large.

<!-- b000918 | prose | pages [20] -->
 Study of Numerical Simulation

<!-- b000919 | prose | pages [20] -->
In this section, we mainly study the density function 𝜌𝑖(𝑥, 𝑡)(𝑖= 1, 2) as a

<!-- b000920 | furniture | pages [20] -->


<!-- b000921 | prose | pages [20] -->
solution of the PDE system. In order to simulate the two-lane traffic movement,

<!-- b000922 | prose | pages [20] -->
we assume that 𝐿 = 32.2 𝑘𝑚. The following initial variation of the average

<!-- b000923 | prose | pages [20] -->
density 𝜌ℎ proposed in [8] can be used on either the fast or the slow lane:

<!-- b000924 | prose | pages [20] -->
1 𝜌(𝑥, 0) = 𝜌ℎ+ Δ𝜌ℎ[

<!-- b000925 | prose | pages [20] -->
1 −

<!-- b000926 | prose | pages [20] -->
]

<!-- b000927 | prose | pages [20] -->
4𝑐𝑜𝑠ℎ2(40 𝐿(𝑥−11𝐿

<!-- b000928 | prose | pages [20] -->
𝐿(𝑥−5𝐿

<!-- b000929 | prose | pages [20] -->
𝑐𝑜𝑠ℎ2(160

<!-- b000930 | prose | pages [20] -->
32 ))

<!-- b000931 | prose | pages [20] -->
16))

<!-- b000932 | prose | pages [20] -->
Then, our model (the PDE system) can be solved by the numerical scheme

<!-- b000933 | furniture | pages [20] -->


<!-- b000934 | prose | pages [20] -->
given in reference [9]. Here we just provide the figures of the solution under

<!-- b000935 | prose | pages [20] -->
three different conditions. (All of these three figures are dynamic traffic images

<!-- b000936 | prose | pages [20] -->
of an asymmetric double-lane system with curve (a) representing the fast lane

<!-- b000937 | prose | pages [20] -->
and curve (b) representing the slow lane.)

<!-- b000938 | prose | pages [20] -->
 At Low Average Density 𝝆̅

<!-- b000939 | prose | pages [20] -->
According to Figure 12, any perturbations on the fast lane or the slow lane

<!-- b000940 | furniture | pages [20] -->


<!-- b000941 | prose | pages [20] -->
will quickly dissipate. Because of the lane-changing tendency, a cluster appeared

<!-- b000942 | prose | pages [20] -->
in the fast lane may cause a small hump in slow lane.

<!-- b000943 | prose | pages [20] -->
On the opposite side, as shown in Figure 13, a cluster in slow lane may

<!-- b000944 | furniture | pages [20] -->


<!-- b000945 | prose | pages [20] -->
quickly dissipate because people trapped by the cluster in slow (driving) lane

<!-- b000946 | prose | pages [20] -->
may choose the fast (overtaking) lane for passing.

<!-- b000947 | furniture | pages [20] -->


<!-- b000948 | furniture | pages [20] -->


<!-- b000949 | furniture | pages [21] -->
Page 21 of 40

<!-- b000950 | furniture | pages [21] -->
Team#29911

<!-- b000951 | furniture | pages [21] -->


<!-- b000952 | furniture | pages [21] -->


<!-- b000953 | furniture | pages [21] -->


<!-- b000954 | furniture | pages [21] -->


<!-- b000955 | furniture | pages [21] -->


<!-- b000956 | furniture | pages [21] -->


<!-- b000957 | furniture | pages [21] -->


<!-- b000958 | furniture | pages [21] -->


<!-- b000959 | furniture | pages [21] -->


<!-- b000960 | furniture | pages [21] -->


<!-- b000961 | furniture | pages [21] -->


<!-- b000962 | furniture | pages [21] -->


<!-- b000963 | furniture | pages [21] -->


<!-- b000964 | caption | pages [21] -->
Figure 12. Low Density(Jam First Appeared on Fast Lane)

<!-- b000965 | furniture | pages [21] -->


<!-- b000966 | furniture | pages [21] -->


<!-- b000967 | furniture | pages [21] -->


<!-- b000968 | furniture | pages [21] -->


<!-- b000969 | furniture | pages [21] -->


<!-- b000970 | furniture | pages [21] -->


<!-- b000971 | furniture | pages [21] -->


<!-- b000972 | furniture | pages [21] -->


<!-- b000973 | furniture | pages [21] -->


<!-- b000974 | furniture | pages [21] -->


<!-- b000975 | furniture | pages [21] -->


<!-- b000976 | caption | pages [21] -->
Figure 13. Low Density(Jam First Appeared on Slow Lane)

<!-- b000977 | prose | pages [21] -->
 At Normal (or Higher) Average Density 𝝆̅

<!-- b000978 | furniture | pages [21] -->


<!-- b000979 | prose | pages [21] -->
As average density continues to rise, free space for vehicles decreases and it

<!-- b000980 | prose | pages [21] -->
becomes less likely for the double-lane system to maintain stability.

<!-- b000981 | prose | pages [21] -->
Correspondingly, serious traffic jams and “stop-and-go” waves become more

<!-- b000982 | prose | pages [21] -->
probable. See in Figure 14.

<!-- b000983 | furniture | pages [21] -->


<!-- b000984 | furniture | pages [21] -->


<!-- b000985 | furniture | pages [21] -->


<!-- b000986 | furniture | pages [21] -->


<!-- b000987 | furniture | pages [21] -->


<!-- b000988 | furniture | pages [21] -->


<!-- b000989 | furniture | pages [21] -->


<!-- b000990 | furniture | pages [21] -->


<!-- b000991 | furniture | pages [21] -->


<!-- b000992 | furniture | pages [21] -->


<!-- b000993 | furniture | pages [21] -->


<!-- b000994 | furniture | pages [22] -->
Page 22 of 40

<!-- b000995 | furniture | pages [22] -->
Team#29911

<!-- b000996 | furniture | pages [22] -->


<!-- b000997 | furniture | pages [22] -->


<!-- b000998 | caption | pages [22] -->
Figure 14. Normal or Higher Density

<!-- b000999 | furniture | pages [22] -->


<!-- b001000 | prose | pages [22] -->
Parameter evaluation of the three figures:

<!-- b001001 | caption | pages [22] -->
Figure 12: 𝜌1 = 0.047𝑣𝑒ℎ/𝑚, 𝜌2 = 0.021 𝑣𝑒ℎ/𝑚, 𝜌ℎ= 0.06 𝑣𝑒ℎ/𝑚;

<!-- b001002 | caption | pages [22] -->
Figure 13: 𝜌1 = 0.047𝑣𝑒ℎ/𝑚, 𝜌2 = 0.021 𝑣𝑒ℎ/𝑚, 𝜌ℎ= 0.06 𝑣𝑒ℎ/𝑚;

<!-- b001003 | caption | pages [22] -->
Figure 14: 𝜌1 = 0.053𝑣𝑒ℎ/𝑚, 𝜌2 = 0.053 𝑣𝑒ℎ/𝑚, 𝜌ℎ= 0.06 𝑣𝑒ℎ/𝑚.

<!-- b001004 | heading | pages [22] -->
3.3 Comparison of Discrete Model and Continuum Model

<!-- b001005 | furniture | pages [22] -->


<!-- b001006 | prose | pages [22] -->
In the discrete (CA) model, we focus on the relationship between traffic flow

<!-- b001007 | prose | pages [22] -->
and vehicle density and obtain the following fact: when density is relatively small,

<!-- b001008 | prose | pages [22] -->
flow rises as density increases; after reaching its peak value, flow then decreases

<!-- b001009 | prose | pages [22] -->
gradually to 0. This coincides with the conclusion derived in the continuum

<!-- b001010 | prose | pages [22] -->
model as shown in Figure 9. More intuitively, the visualization images of both

<!-- b001011 | prose | pages [22] -->
models also convey the same conclusion.

<!-- b001012 | heading | pages [22] -->
3.4 Transferability Analysis of Model in Left-Handed Countries

<!-- b001013 | furniture | pages [22] -->


<!-- b001014 | prose | pages [22] -->
According to our research, the difference between the left-most and

<!-- b001015 | prose | pages [22] -->
right-most tradition is mainly historical. In addition, our model has no partiality

<!-- b001016 | prose | pages [22] -->
for either left orientation or right orientation. In other words, orientation is

<!-- b001017 | prose | pages [22] -->
symmetric in our model. Therefore our model could be transferred in left-handed

<!-- b001018 | prose | pages [22] -->
countries with a single change of orientation.

<!-- b001019 | heading | pages [22] -->
4 Modeling for Alternative Freeway Traffic Rules

<!-- b001020 | furniture | pages [22] -->


<!-- b001021 | prose | pages [22] -->
In this section, we will use similar Monte Carlo method to simulate the traffic

<!-- b001022 | prose | pages [22] -->
flow under two alternative traffic rules: "slow-car-to-right" rule and "free driving

<!-- b001023 | prose | pages [22] -->
& free overtaking" rule.

<!-- b001024 | prose | pages [22] -->
4.1 "Slow-Cars-To-Right" Rule

<!-- b001025 | heading | pages [22] -->
 Model Explanation

<!-- b001026 | furniture | pages [22] -->


<!-- b001027 | prose | pages [22] -->
In the "slow-cars-to-right" rule, the slow cars are designated the right lane,

<!-- b001028 | prose | pages [22] -->
the fast cars are designated among the left and right lanes and no lane changing

<!-- b001029 | prose | pages [22] -->
is allowed. In other words, this is a model of two disconnected single lanes. We

<!-- b001030 | prose | pages [22] -->
run two simulations. First, test a lane with only fast cars and calculate

<!-- b001031 | furniture | pages [23] -->
Team#29911

<!-- b001032 | furniture | pages [23] -->
Page 23 of 40

<!-- b001033 | furniture | pages [23] -->


<!-- b001034 | furniture | pages [23] -->


<!-- b001035 | furniture | pages [23] -->


<!-- b001036 | prose | pages [23] -->
𝑓; then test a lane with 60% fast cars and calculate

<!-- b001037 | prose | pages [23] -->
𝑓

<!-- b001038 | prose | pages [23] -->
corresponding 𝑄𝑓, 𝛼𝑠𝑎𝑓𝑒

<!-- b001039 | prose | pages [23] -->
, 𝐸0

<!-- b001040 | prose | pages [23] -->
𝑠

<!-- b001041 | prose | pages [23] -->
𝑠. The overall fast car percentage is 80% matching

<!-- b001042 | prose | pages [23] -->
corresponding 𝑄𝑠, 𝛼𝑠𝑎𝑓𝑒

<!-- b001043 | prose | pages [23] -->
,  𝐸0

<!-- b001044 | prose | pages [23] -->
previous simulations. The final result is a mixture of previous results with weight

<!-- b001045 | prose | pages [23] -->
(1:1).

<!-- b001046 | prose | pages [23] -->
𝑄= 0.5 ∙𝑄𝑓+ 0.5 ∙𝑄𝑠

<!-- b001047 | prose | pages [23] -->
𝑓 𝑓

<!-- b001048 | prose | pages [23] -->
𝑠

<!-- b001049 | furniture | pages [23] -->


<!-- b001050 | prose | pages [23] -->
𝛼𝑠𝑎𝑓𝑒= 0.5 ∙𝛼𝑠𝑎𝑓𝑒

<!-- b001051 | prose | pages [23] -->
𝐸0 = 0.5 ∙𝐸0

<!-- b001052 | prose | pages [23] -->
+ 0.5 ∙𝛼𝑠𝑎𝑓𝑒

<!-- b001053 | prose | pages [23] -->
𝑓+ 0.5 ∙𝐸0

<!-- b001054 | prose | pages [23] -->
𝑠

<!-- b001055 | prose | pages [23] -->
Parameter evaluation before the simulation is as follows:

<!-- b001056 | furniture | pages [23] -->


<!-- b001057 | prose | pages [23] -->
The length of the lattices 𝐿= 2048;

<!-- b001058 | prose | pages [23] -->
The vehicle density 𝑛= 0.02, 0.04, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3;

<!-- b001059 | prose | pages [23] -->
The number of the total vehicles 𝑁= 2𝑛𝐿;

<!-- b001060 | prose | pages [23] -->
The duration of the simulation 𝑇= 4096;

<!-- b001061 | prose | pages [23] -->
The deceleration probability 𝑃𝑑= 0.1;

<!-- b001062 | prose | pages [23] -->
The change lane probability 𝑃𝑐= 0.7;

<!-- b001063 | prose | pages [23] -->
The maximum velocity of fast car 𝑉𝑚𝑎𝑥

<!-- b001064 | prose | pages [23] -->
= 3. 𝑠

<!-- b001065 | prose | pages [23] -->
𝑉𝑚𝑎𝑥

<!-- b001066 | heading | pages [23] -->
 Model Solution and Analysis

<!-- b001067 | prose | pages [23] -->
𝑓 𝑓 = 5, maximum velocity for slow car

<!-- b001068 | prose | pages [23] -->
Using computer simulation, we plot traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and

<!-- b001069 | furniture | pages [23] -->


<!-- b001070 | prose | pages [23] -->
average energy consumption 𝐸0 respectively against vehicle density 𝑛. The

<!-- b001071 | prose | pages [23] -->
results will be shown in Section 4.3.

<!-- b001072 | prose | pages [23] -->
4.2 "Free Driving & Free Overtaking" Rule

<!-- b001073 | heading | pages [23] -->
 Model Explanation

<!-- b001074 | prose | pages [23] -->
Under the "free driving & free overtaking" rule, vehicles are free to drive and

<!-- b001075 | furniture | pages [23] -->


<!-- b001076 | prose | pages [23] -->
overtake with no specific requirement. The two lanes are symmetric and the only

<!-- b001077 | prose | pages [23] -->
𝑓

<!-- b001078 | prose | pages [23] -->
limitation is the respective maximum velocity 𝑉𝑚𝑎𝑥

<!-- b001079 | prose | pages [23] -->
and 𝑉𝑚𝑎𝑥

<!-- b001080 | prose | pages [23] -->
for fast vehicles 𝑠

<!-- b001081 | prose | pages [23] -->
and slow vehicles. Parameters and their evaluation are still the same as in the

<!-- b001082 | prose | pages [23] -->
"slow-cars-to-right" rule.

<!-- b001083 | heading | pages [23] -->
 Model Solution and Analysis

<!-- b001084 | prose | pages [23] -->
Again, we consider the influence of this traffic through measuring of the

<!-- b001085 | furniture | pages [23] -->


<!-- b001086 | prose | pages [23] -->
three key factors---traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and average energy

<!-- b001087 | prose | pages [23] -->
consumption 𝐸0. Further comparison of the three traffic rules will be shown in

<!-- b001088 | prose | pages [23] -->
the Section 4.3.

<!-- b001089 | furniture | pages [24] -->
Page 24 of 40

<!-- b001090 | furniture | pages [24] -->
Team#29911

<!-- b001091 | furniture | pages [24] -->


<!-- b001092 | furniture | pages [24] -->


<!-- b001093 | heading | pages [24] -->
4.3 Comparison of Different Traffic Rules

<!-- b001094 | furniture | pages [24] -->


<!-- b001095 | prose | pages [24] -->
Same as that in the slow-cars-to-right rule, we will mainly focus on the first

<!-- b001096 | prose | pages [24] -->
half of the figures to analyze the difference of the three rules.

<!-- b001097 | prose | pages [24] -->
 Traffic Flow

<!-- b001098 | furniture | pages [24] -->


<!-- b001099 | prose | pages [24] -->
We plot traffic flow 𝑄 against vehicle density 𝑛 in Figure 15.

<!-- b001100 | furniture | pages [24] -->


<!-- b001101 | furniture | pages [24] -->


<!-- b001102 | furniture | pages [24] -->


<!-- b001103 | furniture | pages [24] -->


<!-- b001104 | furniture | pages [24] -->


<!-- b001105 | furniture | pages [24] -->


<!-- b001106 | furniture | pages [24] -->


<!-- b001107 | furniture | pages [24] -->


<!-- b001108 | furniture | pages [24] -->


<!-- b001109 | furniture | pages [24] -->


<!-- b001110 | furniture | pages [24] -->


<!-- b001111 | furniture | pages [24] -->


<!-- b001112 | furniture | pages [24] -->


<!-- b001113 | caption | pages [24] -->
Figure 15. Traffic Flow under Different Traffic Rules

<!-- b001114 | furniture | pages [24] -->


<!-- b001115 | prose | pages [24] -->
As shown in Figure 15, during light-traffic situation, traffic flow under the

<!-- b001116 | prose | pages [24] -->
"keep-right-except-to-pass" rule and "slow-cars-to-right" rule are larger, traffic

<!-- b001117 | prose | pages [24] -->
flow under the "free driving & free overtaking" is the relatively small.

<!-- b001118 | furniture | pages [24] -->


<!-- b001119 | prose | pages [24] -->
During heavy-traffic situation, flow under three rules tends to be the same,

<!-- b001120 | prose | pages [24] -->
which is easy to understand because the more probable jams make the

<!-- b001121 | prose | pages [24] -->
advantages of the last two traffic rule hard to discern.

<!-- b001122 | furniture | pages [24] -->


<!-- b001123 | prose | pages [24] -->
 Safety Index

<!-- b001124 | furniture | pages [24] -->


<!-- b001125 | prose | pages [24] -->
We plot safety index 𝛼𝑠𝑎𝑓𝑒 against vehicle density 𝑛 in Figure 16.

<!-- b001126 | furniture | pages [24] -->


<!-- b001127 | furniture | pages [24] -->


<!-- b001128 | furniture | pages [25] -->
Page 25 of 40

<!-- b001129 | furniture | pages [25] -->
Team#29911

<!-- b001130 | furniture | pages [25] -->


<!-- b001131 | furniture | pages [25] -->


<!-- b001132 | furniture | pages [25] -->


<!-- b001133 | furniture | pages [25] -->


<!-- b001134 | furniture | pages [25] -->


<!-- b001135 | furniture | pages [25] -->


<!-- b001136 | furniture | pages [25] -->


<!-- b001137 | furniture | pages [25] -->


<!-- b001138 | furniture | pages [25] -->


<!-- b001139 | furniture | pages [25] -->


<!-- b001140 | furniture | pages [25] -->


<!-- b001141 | furniture | pages [25] -->


<!-- b001142 | furniture | pages [25] -->


<!-- b001143 | furniture | pages [25] -->


<!-- b001144 | furniture | pages [25] -->


<!-- b001145 | caption | pages [25] -->
Figure 16. Safety Index under Different Traffic Rules (lower is safer)

<!-- b001146 | furniture | pages [25] -->


<!-- b001147 | prose | pages [25] -->
During light-traffic situation, the condition under the "keep-right-except

<!-- b001148 | prose | pages [25] -->
-to-pass" rule and "slow-cars-to-right" rule is much safer than that under the

<!-- b001149 | prose | pages [25] -->
"free driving & free overtaking" rule.

<!-- b001150 | furniture | pages [25] -->


<!-- b001151 | prose | pages [25] -->
During heavy-traffic situation, same as that of traffic flow, safety index under

<!-- b001152 | prose | pages [25] -->
three traffic rules tend to be the same because vehicle tend to drive at a much

<!-- b001153 | prose | pages [25] -->
lower speed which make the overall condition much safer.

<!-- b001154 | prose | pages [25] -->
  Average Energy Consumption

<!-- b001155 | furniture | pages [25] -->


<!-- b001156 | prose | pages [25] -->
We plot average energy consumption 𝐸0 against vehicle density 𝑛 in

<!-- b001157 | caption | pages [25] -->
Figure 17.

<!-- b001158 | furniture | pages [25] -->


<!-- b001159 | furniture | pages [25] -->


<!-- b001160 | furniture | pages [25] -->


<!-- b001161 | furniture | pages [25] -->


<!-- b001162 | furniture | pages [25] -->


<!-- b001163 | furniture | pages [25] -->


<!-- b001164 | furniture | pages [25] -->


<!-- b001165 | furniture | pages [25] -->


<!-- b001166 | furniture | pages [25] -->


<!-- b001167 | furniture | pages [25] -->


<!-- b001168 | furniture | pages [25] -->


<!-- b001169 | furniture | pages [25] -->


<!-- b001170 | furniture | pages [25] -->


<!-- b001171 | furniture | pages [25] -->


<!-- b001172 | caption | pages [25] -->
Figure 17. Average Energy Consumption under

<!-- b001173 | prose | pages [25] -->
Different Traffic Rules (lower is better)

<!-- b001174 | furniture | pages [26] -->
Page 26 of 40

<!-- b001175 | furniture | pages [26] -->
Team#29911

<!-- b001176 | furniture | pages [26] -->


<!-- b001177 | furniture | pages [26] -->


<!-- b001178 | furniture | pages [26] -->


<!-- b001179 | prose | pages [26] -->
Since a large portion of energy consumption comes from traffic jams, and

<!-- b001180 | prose | pages [26] -->
unstable lane changing easily result in traffic jams, the "free driving & free

<!-- b001181 | prose | pages [26] -->
overtaking" rule will definitely be more energy-costly. Such trend is manifest

<!-- b001182 | prose | pages [26] -->
during light traffic when acceleration is fairly easy.

<!-- b001183 | furniture | pages [26] -->


<!-- b001184 | prose | pages [26] -->
During heavy traffic however, lane changing and acceleration become much

<!-- b001185 | prose | pages [26] -->
more difficult, most of the energy consumption is from the accelerations and

<!-- b001186 | prose | pages [26] -->
decelerations in traffic jams, therefore the average energy consumption under

<!-- b001187 | prose | pages [26] -->
three rules tends to be the same.

<!-- b001188 | prose | pages [26] -->
 Summary & Suggestions

<!-- b001189 | furniture | pages [26] -->


<!-- b001190 | prose | pages [26] -->
From the figures above, we can discover that "free driving & free overtaking"

<!-- b001191 | prose | pages [26] -->
rule is inferior to the "slow-cars-to-right" rule and "keep-right-except-to-pass"

<!-- b001192 | prose | pages [26] -->
rule. This accords with real life situation because most countries adopt a

<!-- b001193 | prose | pages [26] -->
combinational policy of "slow-cars-to-right" and "keep-right-except-to-pass".

<!-- b001194 | furniture | pages [26] -->


<!-- b001195 | prose | pages [26] -->
Meanwhile, it is unrealistic to adopt the "slow-cars-to-right" because total

<!-- b001196 | prose | pages [26] -->
forbidding of lane changing and overtaking is unreasonable. Our suggestion is

<!-- b001197 | prose | pages [26] -->
that maintain the policy of "keep-right-except-to-pass" rule and meanwhile

<!-- b001198 | prose | pages [26] -->
construct separate fast and slow lanes for those freeways frequently suffered

<!-- b001199 | prose | pages [26] -->
from car jams and obstructions.

<!-- b001200 | heading | pages [26] -->
5 Modeling for Intelligent-System Control

<!-- b001201 | furniture | pages [26] -->


<!-- b001202 | prose | pages [26] -->
In this section, we make the general assumption that equipped with an

<!-- b001203 | prose | pages [26] -->
intelligent system. The intelligent system knows about the exact velocity and

<!-- b001204 | prose | pages [26] -->
location of all the vehicles on the freeway and controls them together. We aim to

<!-- b001205 | prose | pages [26] -->
propose a new traffic rule such that the overall traffic flow of the freeway could

<!-- b001206 | prose | pages [26] -->
be even larger.

<!-- b001207 | prose | pages [26] -->
5.1 "Median" Optimization

<!-- b001208 | heading | pages [26] -->
 Model Explanation

<!-- b001209 | furniture | pages [26] -->


<!-- b001210 | prose | pages [26] -->
We now introduce a rule called “median” rule. The basic idea is to let vehicles

<!-- b001211 | prose | pages [26] -->
with higher speed stay on the left lane more, while vehicles with lower speed

<!-- b001212 | prose | pages [26] -->
stay on the right lane, reducing the possibility of fast cars following slow cars.

<!-- b001213 | prose | pages [26] -->
The separation point is the median speed, which is known easily by a system that

<!-- b001214 | prose | pages [26] -->
controls all the vehicles. The advantage of median speed is that it is automatically

<!-- b001215 | furniture | pages [27] -->
Team#29911

<!-- b001216 | furniture | pages [27] -->
Page 27 of 40

<!-- b001217 | furniture | pages [27] -->


<!-- b001218 | furniture | pages [27] -->


<!-- b001219 | furniture | pages [27] -->


<!-- b001220 | prose | pages [27] -->
adjusted according to the current average speed, then exactly demand half of the

<!-- b001221 | prose | pages [27] -->
cars go to the left lane and vice versa. Therefore this rule will not let the left lane

<!-- b001222 | prose | pages [27] -->
and right lane become unbalanced both in light and heavy traffic comparing to

<!-- b001223 | prose | pages [27] -->
the usage of a fixed speed cap.

<!-- b001224 | prose | pages [27] -->
The rule is as stated in Figure 18.

<!-- b001225 | prose | pages [27] -->
Determine the speed of

<!-- b001226 | prose | pages [27] -->
the kth car

<!-- b001227 | prose | pages [27] -->
V(k)=Vmedian?

<!-- b001228 | prose | pages [27] -->
T

<!-- b001229 | prose | pages [27] -->
Generate a random number

<!-- b001230 | prose | pages [27] -->
in [0, 1]

<!-- b001231 | prose | pages [27] -->
<0.5

<!-- b001232 | prose | pages [27] -->
Apply rule: Stay on left

<!-- b001233 | prose | pages [27] -->
lane except blocked,

<!-- b001234 | prose | pages [27] -->
return to left lane if

<!-- b001235 | prose | pages [27] -->
possible.

<!-- b001236 | prose | pages [27] -->
F

<!-- b001237 | prose | pages [27] -->
V(k)>Vmedian

<!-- b001238 | prose | pages [27] -->
>0.5 >0.5

<!-- b001239 | prose | pages [27] -->
Apply rule: Stay on right

<!-- b001240 | prose | pages [27] -->
lane except blocked, return to right lane if

<!-- b001241 | prose | pages [27] -->
possible.

<!-- b001242 | prose | pages [27] -->
End

<!-- b001243 | furniture | pages [27] -->


<!-- b001244 | caption | pages [27] -->
Figure 18. "Median" Illustration

<!-- b001245 | heading | pages [27] -->
 Model Solution and Analysis

<!-- b001246 | prose | pages [27] -->
Under the same maximum velocity, we plot traffic flow, safety index and

<!-- b001247 | furniture | pages [27] -->


<!-- b001248 | prose | pages [27] -->
average energy consumption against different vehicle density. See in Figure

<!-- b001249 | prose | pages [27] -->
19-21.

<!-- b001250 | furniture | pages [27] -->


<!-- b001251 | furniture | pages [27] -->


<!-- b001252 | furniture | pages [28] -->
Team#29911

<!-- b001253 | furniture | pages [28] -->


<!-- b001254 | furniture | pages [28] -->
Page 28 of 40

<!-- b001255 | furniture | pages [28] -->


<!-- b001256 | furniture | pages [28] -->


<!-- b001257 | furniture | pages [28] -->


<!-- b001258 | prose | pages [28] -->
Traffic Flow Q against Vehicle

<!-- b001259 | furniture | pages [28] -->


<!-- b001260 | prose | pages [28] -->
Density n

<!-- b001261 | furniture | pages [28] -->


<!-- b001262 | prose | pages [28] -->
1.5

<!-- b001263 | furniture | pages [28] -->


<!-- b001264 | prose | pages [28] -->
Traffic Flow Q

<!-- b001265 | furniture | pages [28] -->


<!-- b001266 | prose | pages [28] -->
1

<!-- b001267 | furniture | pages [28] -->


<!-- b001268 | prose | pages [28] -->
0.5

<!-- b001269 | furniture | pages [28] -->


<!-- b001270 | furniture | pages [28] -->


<!-- b001271 | prose | pages [28] -->
0

<!-- b001272 | furniture | pages [28] -->


<!-- b001273 | prose | pages [28] -->
0 0.1

<!-- b001274 | furniture | pages [28] -->


<!-- b001275 | prose | pages [28] -->
Equipped

<!-- b001276 | prose | pages [28] -->
Not Equipped

<!-- b001277 | prose | pages [28] -->
0.2 0.3 0.4

<!-- b001278 | prose | pages [28] -->
Vehicle Density n

<!-- b001279 | furniture | pages [28] -->


<!-- b001280 | caption | pages [28] -->
Figure 19. Relationship of Traffic Flow and Vehicle Density

<!-- b001281 | furniture | pages [28] -->


<!-- b001282 | furniture | pages [28] -->


<!-- b001283 | furniture | pages [28] -->


<!-- b001284 | prose | pages [28] -->
Safety Index asafe against Vehicle

<!-- b001285 | furniture | pages [28] -->


<!-- b001286 | prose | pages [28] -->
Density n

<!-- b001287 | furniture | pages [28] -->


<!-- b001288 | furniture | pages [28] -->


<!-- b001289 | prose | pages [28] -->
0.35

<!-- b001290 | prose | pages [28] -->
Safety Index asafe

<!-- b001291 | prose | pages [28] -->
0.3

<!-- b001292 | furniture | pages [28] -->


<!-- b001293 | prose | pages [28] -->
0.25

<!-- b001294 | furniture | pages [28] -->


<!-- b001295 | prose | pages [28] -->
0.2

<!-- b001296 | furniture | pages [28] -->


<!-- b001297 | prose | pages [28] -->
0.15 0.1

<!-- b001298 | furniture | pages [28] -->


<!-- b001299 | prose | pages [28] -->
0.05

<!-- b001300 | furniture | pages [28] -->


<!-- b001301 | prose | pages [28] -->
0

<!-- b001302 | furniture | pages [28] -->


<!-- b001303 | prose | pages [28] -->
0 0.1

<!-- b001304 | furniture | pages [28] -->


<!-- b001305 | prose | pages [28] -->
Equipped

<!-- b001306 | prose | pages [28] -->
Not Equipped

<!-- b001307 | prose | pages [28] -->
0.2 0.3 0.4

<!-- b001308 | prose | pages [28] -->
Vehicle Density n

<!-- b001309 | furniture | pages [28] -->


<!-- b001310 | caption | pages [28] -->
Figure 20. Relationship of Safety Index

<!-- b001311 | prose | pages [28] -->
and Vehicle Density (lower is safer)

<!-- b001312 | furniture | pages [28] -->


<!-- b001313 | prose | pages [28] -->
Average Energy Consumption E0

<!-- b001314 | furniture | pages [28] -->


<!-- b001315 | prose | pages [28] -->
against Vehicle Density n

<!-- b001316 | furniture | pages [28] -->


<!-- b001317 | furniture | pages [28] -->


<!-- b001318 | prose | pages [28] -->
2000

<!-- b001319 | furniture | pages [28] -->


<!-- b001320 | prose | pages [28] -->
Consumption E0

<!-- b001321 | prose | pages [28] -->
Average Energy

<!-- b001322 | prose | pages [28] -->
1500

<!-- b001323 | furniture | pages [28] -->


<!-- b001324 | prose | pages [28] -->
1000

<!-- b001325 | furniture | pages [28] -->


<!-- b001326 | furniture | pages [28] -->


<!-- b001327 | prose | pages [28] -->
500

<!-- b001328 | furniture | pages [28] -->


<!-- b001329 | prose | pages [28] -->
0

<!-- b001330 | furniture | pages [28] -->


<!-- b001331 | prose | pages [28] -->
0 0.05 0.1

<!-- b001332 | prose | pages [28] -->
Equipped

<!-- b001333 | prose | pages [28] -->
Not Equipped

<!-- b001334 | prose | pages [28] -->
0.15 0.2 0.25 0.3 0.35

<!-- b001335 | prose | pages [28] -->
Vehicle Density n

<!-- b001336 | furniture | pages [28] -->


<!-- b001337 | furniture | pages [28] -->


<!-- b001338 | caption | pages [28] -->
Figure 21. Relationship of Average Energy Consumption

<!-- b001339 | prose | pages [28] -->
and Vehicle Density (lower is better)

<!-- b001340 | furniture | pages [29] -->
Team#29911

<!-- b001341 | furniture | pages [29] -->
Page 29 of 40

<!-- b001342 | furniture | pages [29] -->


<!-- b001343 | furniture | pages [29] -->


<!-- b001344 | furniture | pages [29] -->


<!-- b001345 | prose | pages [29] -->
From the above Figures, we can discover that the "median" optimization

<!-- b001346 | furniture | pages [29] -->


<!-- b001347 | prose | pages [29] -->
does perform better in terms of traffic flow, safety condition and energy

<!-- b001348 | prose | pages [29] -->
consumption, even though such optimization is not very dramatic. This also

<!-- b001349 | prose | pages [29] -->
indicates that the current "keep-right-except-to-pass" rule is already a pretty

<!-- b001350 | prose | pages [29] -->
mature one.

<!-- b001351 | heading | pages [29] -->
5.2 Possible Further Improvements

<!-- b001352 | prose | pages [29] -->
The “median” rule is only a simple rule, more advantages of the intelligent

<!-- b001353 | prose | pages [29] -->
systems can be utilized. In the discrete (CA) model, a driver can only change his

<!-- b001354 | prose | pages [29] -->
speed according to the distance of cars closely in front or behind because he

<!-- b001355 | prose | pages [29] -->
doesn't know about the location of other cars and intentions of their drivers.

<!-- b001356 | prose | pages [29] -->
Therefore when he is in a car flow without any gaps as shown in Figure 22, the

<!-- b001357 | prose | pages [29] -->
only thing he can do is stop and wait for the front car to move. That's why we

<!-- b001358 | prose | pages [29] -->
𝑓 and Δ𝑋𝑜

<!-- b001359 | prose | pages [29] -->
𝑓.

<!-- b001360 | prose | pages [29] -->
only compare his current velocity 𝑉 with Δ𝑋𝑝

<!-- b001361 | furniture | pages [29] -->


<!-- b001362 | furniture | pages [29] -->


<!-- b001363 | furniture | pages [29] -->


<!-- b001364 | furniture | pages [29] -->


<!-- b001365 | furniture | pages [29] -->


<!-- b001366 | furniture | pages [29] -->


<!-- b001367 | caption | pages [29] -->
Figure 22. Illustration of Online Algorithm

<!-- b001368 | prose | pages [29] -->
But with an intelligent system, it controls all the cars at the same time. Under

<!-- b001369 | furniture | pages [29] -->


<!-- b001370 | prose | pages [29] -->
such circumstances, it can optimize traffic flow by accelerating the three cars

<!-- b001371 | prose | pages [29] -->
together with the same acceleration. This approach is extremely effective in

<!-- b001372 | prose | pages [29] -->
traffic jams.

<!-- b001373 | furniture | pages [29] -->


<!-- b001374 | heading | pages [29] -->
6 Superiority and Weakness

<!-- b001375 | heading | pages [29] -->
6.1 Superiority Analysis

<!-- b001376 | prose | pages [29] -->
By reasonable discretization and Monte Carlo method, CA model properly

<!-- b001377 | prose | pages [29] -->
simulates normal driving and overtaking on real-life double-lane freeways;

<!-- b001378 | furniture | pages [29] -->


<!-- b001379 | prose | pages [29] -->
The solution of the CA model could be presented via various forms and

<!-- b001380 | prose | pages [29] -->
standards, visualization technique makes the result even more intuitive;

<!-- b001381 | furniture | pages [29] -->


<!-- b001382 | furniture | pages [30] -->
Page 30 of 40

<!-- b001383 | furniture | pages [30] -->
Team#29911

<!-- b001384 | furniture | pages [30] -->


<!-- b001385 | furniture | pages [30] -->


<!-- b001386 | prose | pages [30] -->
Our model has robust flexibility, only minor modification could realize

<!-- b001387 | furniture | pages [30] -->


<!-- b001388 | prose | pages [30] -->
simulation under different traffic rules and parameters;

<!-- b001389 | prose | pages [30] -->
By comparing with other traffic rules, we can fully realize the influence of

<!-- b001390 | furniture | pages [30] -->


<!-- b001391 | prose | pages [30] -->
keep-right-except-to-pass rule from various aspects;

<!-- b001392 | prose | pages [30] -->
By designing algorithms under an intelligent system, our model has

<!-- b001393 | prose | pages [30] -->
reference value in terms of future freeway construction;

<!-- b001394 | furniture | pages [30] -->


<!-- b001395 | prose | pages [30] -->
 Our continuum model assigns realistic values to parameters, confirming the

<!-- b001396 | prose | pages [30] -->
results derived from the discrete model from a macroscopic perspective.

<!-- b001397 | furniture | pages [30] -->


<!-- b001398 | heading | pages [30] -->
6.2 Weakness Analysis

<!-- b001399 | prose | pages [30] -->
Due to the restriction of computer simulation, some of our assumptions are

<!-- b001400 | furniture | pages [30] -->


<!-- b001401 | prose | pages [30] -->
highly ideal, such as the length of vehicles and the value of acceleration.

<!-- b001402 | prose | pages [30] -->
The core of our system depends on computer simulation, therefore the

<!-- b001403 | furniture | pages [30] -->


<!-- b001404 | prose | pages [30] -->
calculation of key quantities such as traffic flow and safety index is

<!-- b001405 | furniture | pages [30] -->


<!-- b001406 | prose | pages [30] -->
time-costly.

<!-- b001407 | heading | pages [30] -->
6.3 Future Research

<!-- b001408 | heading | pages [30] -->
6.3.1 Possible Optimization of Discrete Model

<!-- b001409 | prose | pages [30] -->
If technique permits, we strive to make computer simulation as similar as

<!-- b001410 | furniture | pages [30] -->


<!-- b001411 | prose | pages [30] -->
possible to realistic situations. One possible measures is that we can use 1

<!-- b001412 | furniture | pages [30] -->


<!-- b001413 | prose | pages [30] -->
minute as the basic time unit and assign realistic values to lattice length

<!-- b001414 | furniture | pages [30] -->


<!-- b001415 | prose | pages [30] -->
(such as 0.5km). Since most vehicles travel at velocity between 60 𝑘𝑚/ℎ

<!-- b001416 | furniture | pages [30] -->


<!-- b001417 | prose | pages [30] -->
and 120 𝑘𝑚/ℎ, within one time unit (1 min), a vehicle is expected to pass

<!-- b001418 | furniture | pages [30] -->


<!-- b001419 | prose | pages [30] -->
2-4 lattices within one minute.

<!-- b001420 | prose | pages [30] -->
For more accurate approximation, vehicle profile should be taken into

<!-- b001421 | furniture | pages [30] -->


<!-- b001422 | prose | pages [30] -->
consideration. For example, limousines, sedans, jeeps are usually small but

<!-- b001423 | furniture | pages [30] -->


<!-- b001424 | prose | pages [30] -->
relatively fast, we can assign them with one-lattice length and larger

<!-- b001425 | furniture | pages [30] -->


<!-- b001426 | prose | pages [30] -->
maximum velocity; trucks, on the other hand, could be assigned with length

<!-- b001427 | furniture | pages [30] -->


<!-- b001428 | prose | pages [30] -->
of multiple lattices and a smaller maximum velocity.

<!-- b001429 | prose | pages [30] -->
Finally, we add a more professional factor in the transportation

<!-- b001430 | furniture | pages [30] -->


<!-- b001431 | prose | pages [30] -->
field---stopping sight distance and its limit. The stopping sight distance is

<!-- b001432 | furniture | pages [30] -->


<!-- b001433 | prose | pages [30] -->
used to measure several secure distances in driving. We can assign an

<!-- b001434 | furniture | pages [30] -->


<!-- b001435 | prose | pages [30] -->
integer to the stopping sight distance, denoted as 𝑑0. When the front gap is

<!-- b001436 | prose | pages [30] -->
𝑓> 𝑑0), we compare 𝑉+ 1 with

<!-- b001437 | furniture | pages [30] -->


<!-- b001438 | prose | pages [30] -->
larger than the stopping sight distance (Δ𝑋𝑃

<!-- b001439 | furniture | pages [31] -->
Page 31 of 40

<!-- b001440 | furniture | pages [31] -->
Team#29911

<!-- b001441 | furniture | pages [31] -->


<!-- b001442 | furniture | pages [31] -->


<!-- b001443 | prose | pages [31] -->
𝑓 or Δ𝑋𝑜

<!-- b001444 | prose | pages [31] -->
𝑓 to determine the vehicle's velocity at next

<!-- b001445 | prose | pages [31] -->
𝑑0 instead of with Δ𝑋𝑃

<!-- b001446 | furniture | pages [31] -->


<!-- b001447 | prose | pages [31] -->
time interval. We can further combine weather conditions to evaluate the

<!-- b001448 | furniture | pages [31] -->


<!-- b001449 | prose | pages [31] -->
stopping sight distance. Such model is of great importance in deciding

<!-- b001450 | prose | pages [31] -->
whether to close freeways under severe weather conditions.

<!-- b001451 | furniture | pages [31] -->


<!-- b001452 | heading | pages [31] -->
6.3.2 Possible Optimization of Continuum Model

<!-- b001453 | prose | pages [31] -->
In many countries around the world, the number of freeways are

<!-- b001454 | furniture | pages [31] -->


<!-- b001455 | prose | pages [31] -->
dramatically increasing. We can continue to develop multi-lane(more than

<!-- b001456 | furniture | pages [31] -->


<!-- b001457 | prose | pages [31] -->
two lanes) models. Speed limits could also be incorporated in the continuum

<!-- b001458 | furniture | pages [31] -->


<!-- b001459 | prose | pages [31] -->
model.

<!-- b001460 | prose | pages [31] -->
Construct a systematic theory to analyze the graphic form of 𝜌(𝑥, 𝑡) and

<!-- b001461 | furniture | pages [31] -->


<!-- b001462 | prose | pages [31] -->
look for accurate analytical expressions.

<!-- b001463 | furniture | pages [31] -->


<!-- b001464 | heading | pages [31] -->
7 Conclusion

<!-- b001465 | furniture | pages [31] -->


<!-- b001466 | prose | pages [31] -->
We use a discrete model and a continuum model research upon the influence

<!-- b001467 | prose | pages [31] -->
of "Keep-Right-Except-To-Pass" rule on traffic flow, safety index and average

<!-- b001468 | prose | pages [31] -->
energy consumption respectively. Furthermore, to fully determine the pros and

<!-- b001469 | prose | pages [31] -->
cons of the rule, we continue to build models to analyze two alternative traffic

<!-- b001470 | prose | pages [31] -->
rules---the "Slow-Cars-To-Right" rule and the "Free Driving & Free Overtaking"

<!-- b001471 | prose | pages [31] -->
rule. Finally, we propose two possible rules to optimize traffic flow when

<!-- b001472 | prose | pages [31] -->
equipped with an intelligent system. The results of our models are as follows: “Keep-Right-Except-to-Pass” Rule

<!-- b001473 | furniture | pages [31] -->


<!-- b001474 | prose | pages [31] -->
According to our model, traffic flow and safety index first rise to peak value

<!-- b001475 | prose | pages [31] -->
then decrease to zero with increasing vehicle density, while energy flow keeps

<!-- b001476 | prose | pages [31] -->
rising but with a bating speed. Furthermore, under-posted and over-posted

<!-- b001477 | prose | pages [31] -->
speed limits relative to our calculated optimal maximum velocity have different

<!-- b001478 | prose | pages [31] -->
influences during light and heavy traffic. In addition, our model could be

<!-- b001479 | prose | pages [31] -->
transferred in left-handed countries with a single change of orientation.

<!-- b001480 | prose | pages [31] -->
Alternative Traffic Rules

<!-- b001481 | furniture | pages [31] -->


<!-- b001482 | prose | pages [31] -->
The "Keep-Right-Except-To-Pass" rule and the "Slow-Cars-To-Right" rule are

<!-- b001483 | prose | pages [31] -->
superior (to the "Free Driving & Free Overtaking" rule), a combination of  these

<!-- b001484 | prose | pages [31] -->
two rules will have strengthening effects especially on heavy-traffic freeways.

<!-- b001485 | furniture | pages [32] -->
Page 32 of 40

<!-- b001486 | furniture | pages [32] -->
Team#29911

<!-- b001487 | furniture | pages [32] -->


<!-- b001488 | furniture | pages [32] -->


<!-- b001489 | prose | pages [32] -->
Intelligent System Control

<!-- b001490 | furniture | pages [32] -->


<!-- b001491 | prose | pages [32] -->
An ideal online algorithm is discussed, and a "median" optimization method

<!-- b001492 | prose | pages [32] -->
is simulated and proves to be beneficial to enlarge traffic flow.

<!-- b001493 | heading | pages [32] -->
8 References

<!-- b001494 | references | pages [32] -->
[1] Peilin Li, "Globalization and the 'Left-Most' Policy of Automobiles", Journal of

<!-- b001495 | furniture | pages [32] -->


<!-- b001496 | references | pages [32] -->
Financial Introduction, Vol.8, 2004.

<!-- b001497 | references | pages [32] -->
[2] Chowdhury, D., Wolf, D. E., & Schreckenberg, M. (1997). Particle hopping

<!-- b001498 | furniture | pages [32] -->


<!-- b001499 | references | pages [32] -->
models for two-lane traffic with two kinds of vehicles: Effects of

<!-- b001500 | furniture | pages [32] -->


<!-- b001501 | references | pages [32] -->
lane-changing rules. Physica A: Statistical Mechanics and its Applications,

<!-- b001502 | furniture | pages [32] -->


<!-- b001503 | references | pages [32] -->
235 (3), 417-439.

<!-- b001504 | references | pages [32] -->
[3] Giordano, Frank R. A first course in mathematical modeling. Cengage

<!-- b001505 | furniture | pages [32] -->


<!-- b001506 | references | pages [32] -->
Learning, 2013.

<!-- b001507 | references | pages [32] -->
[4] Haijun Huang · Tieqiao Tang · Ziyou Gao:Continuum modeling for two-lane

<!-- b001508 | furniture | pages [32] -->


<!-- b001509 | references | pages [32] -->
traffic flow, Acta Mech Sinica (2006) 22: 131–137.

<!-- b001510 | references | pages [32] -->
[5] Tang Chang-Fu, Jiang Rui, Wu Qing-Song:Extended speed gradient model for

<!-- b001511 | furniture | pages [32] -->


<!-- b001512 | references | pages [32] -->
traffic flow on two-lane freeways. Chinese Physics, 2007/16(06)

<!-- b001513 | references | pages [32] -->
[6] Lee H Y, Lee H W and Kim D 1999 Phys. Rev. E 59 5101

<!-- b001514 | references | pages [32] -->
[7] Nagel K and Schreckenberg M 1992 J. Phys. I 2 2221

<!-- b001515 | references | pages [32] -->
[8] Kerner B S and Konsh ̈auser P 1993 Phys. Rev. E 48 2335

<!-- b001516 | references | pages [32] -->
[9] Fu C J, Wang B H, Yin C Y and Gao K 2006 Acta Phys.Sin. 55 4032

<!-- b001517 | heading | pages [32] -->
9 Appendix

<!-- b001518 | prose | pages [32] -->
C++ Source Code for Monte Carlo Simulation: gen.h:

<!-- b001519 | prose | pages [32] -->
#ifndef __GEN

<!-- b001520 | prose | pages [32] -->
#define __GEN

<!-- b001521 | furniture | pages [32] -->


<!-- b001522 | prose | pages [32] -->
#include <iostream>

<!-- b001523 | prose | pages [32] -->
#include <cstdio>

<!-- b001524 | prose | pages [32] -->
#include <ctime>

<!-- b001525 | prose | pages [32] -->
#include <cstdlib>

<!-- b001526 | prose | pages [32] -->
#include <vector>

<!-- b001527 | prose | pages [32] -->
#include <cassert>

<!-- b001528 | prose | pages [32] -->
using namespace std;

<!-- b001529 | prose | pages [32] -->
/*

<!-- b001530 | prose | pages [32] -->
#define RATIO 0.3

<!-- b001531 | prose | pages [32] -->
#define L 512

<!-- b001532 | prose | pages [32] -->
#define VMAX 7

<!-- b001533 | furniture | pages [33] -->
Page 33 of 40

<!-- b001534 | furniture | pages [33] -->
Team#29911

<!-- b001535 | furniture | pages [33] -->


<!-- b001536 | furniture | pages [33] -->


<!-- b001537 | prose | pages [33] -->
#define VBASE 2

<!-- b001538 | prose | pages [33] -->
*/

<!-- b001539 | prose | pages [33] -->
int random(int low, int high){

<!-- b001540 | prose | pages [33] -->
return (rand()%(high-low+1)+low);

<!-- b001541 | prose | pages [33] -->
}

<!-- b001542 | prose | pages [33] -->
void gen(const char *fpath, int L, double den, int Vmax0, int Vmax1, double Pv){

<!-- b001543 | prose | pages [33] -->
FILE *fp = fopen(fpath, "w");

<!-- b001544 | prose | pages [33] -->
int n=den*L;

<!-- b001545 | prose | pages [33] -->
vector<int> a;

<!-- b001546 | prose | pages [33] -->
for (int i = 0; i < L && a.size() < n; i ++)

<!-- b001547 | prose | pages [33] -->
if (R((n-a.size())*1.0/(L-i)) || a.size()+L-i <= n)

<!-- b001548 | prose | pages [33] -->
a.push_back(i);

<!-- b001549 | prose | pages [33] -->
assert(a.size() == n);

<!-- b001550 | prose | pages [33] -->
fprintf(fp, "%d, %d\n", L, n);

<!-- b001551 | prose | pages [33] -->
int v;

<!-- b001552 | prose | pages [33] -->
for (int i = 0; i < n; i ++){

<!-- b001553 | prose | pages [33] -->
v=R(Pv)?Vmax0:Vmax1;

<!-- b001554 | prose | pages [33] -->
fprintf(fp, "%d, %d, %d\n", a[i], v, random(v/2, v));

<!-- b001555 | prose | pages [33] -->
}

<!-- b001556 | prose | pages [33] -->
fclose(fp);

<!-- b001557 | prose | pages [33] -->
}

<!-- b001558 | prose | pages [33] -->
#endif // __GEN

<!-- b001559 | furniture | pages [33] -->


<!-- b001560 | prose | pages [33] -->
SaveBMP.h:

<!-- b001561 | prose | pages [33] -->
#ifndef __BMP

<!-- b001562 | prose | pages [33] -->
#define __BMP

<!-- b001563 | prose | pages [33] -->
FILE *SaveBmp(const char* filename,int height,int width){

<!-- b001564 | prose | pages [33] -->
unsigned int w = ((width+7)/8+3)/4*4;

<!-- b001565 | prose | pages [33] -->
unsigned int size = w*height+0x3E;

<!-- b001566 | prose | pages [33] -->
unsigned short head[]={

<!-- b001567 | prose | pages [33] -->
0x4D42,size&0xffff,size>>16,0,0,0x3E,0,0x28,

<!-- b001568 | prose | pages [33] -->
0,width&0xffff,width>>16,height&0xffff,height>>16,1,1,0,

<!-- b001569 | prose | pages [33] -->
0,0,0,0,0,0,0,0,0,0,0,0,0,0xffff, 0x00ff

<!-- b001570 | prose | pages [33] -->
};

<!-- b001571 | prose | pages [33] -->
FILE* fp=fopen(filename,"wb");

<!-- b001572 | prose | pages [33] -->
if(!fp)return NULL;

<!-- b001573 | prose | pages [33] -->
fwrite(head,1,sizeof(head),fp);

<!-- b001574 | prose | pages [33] -->
return fp;

<!-- b001575 | prose | pages [33] -->
}

<!-- b001576 | prose | pages [33] -->
#endif

<!-- b001577 | furniture | pages [33] -->


<!-- b001578 | furniture | pages [33] -->


<!-- b001579 | prose | pages [33] -->
lane.h:

<!-- b001580 | prose | pages [33] -->
#ifndef __LANE

<!-- b001581 | furniture | pages [34] -->
Page 34 of 40

<!-- b001582 | furniture | pages [34] -->
Team#29911

<!-- b001583 | furniture | pages [34] -->


<!-- b001584 | furniture | pages [34] -->


<!-- b001585 | prose | pages [34] -->
#define __LANE

<!-- b001586 | furniture | pages [34] -->


<!-- b001587 | prose | pages [34] -->
#include <iostream>

<!-- b001588 | prose | pages [34] -->
#include <cstdio>

<!-- b001589 | prose | pages [34] -->
#include <vector>

<!-- b001590 | prose | pages [34] -->
#include <cmath>

<!-- b001591 | prose | pages [34] -->
#include <cassert>

<!-- b001592 | prose | pages [34] -->
#include <cstdlib>

<!-- b001593 | prose | pages [34] -->
#include <ctime>

<!-- b001594 | prose | pages [34] -->
#include <algorithm>

<!-- b001595 | prose | pages [34] -->
#include <cstring>

<!-- b001596 | furniture | pages [34] -->


<!-- b001597 | prose | pages [34] -->
#define out(x) cout<<(#x)<<"="<<x<<endl;

<!-- b001598 | furniture | pages [34] -->


<!-- b001599 | prose | pages [34] -->
using namespace std;

<!-- b001600 | furniture | pages [34] -->


<!-- b001601 | prose | pages [34] -->
int L, T = 2048, VISUALIZE = 0, TOT = 5;

<!-- b001602 | prose | pages [34] -->
double Pd = 0.2, Pc = 0.6, Pv = 0.8;

<!-- b001603 | prose | pages [34] -->
int Voff = 2, RULE = 0, Vmax0 = 4, Vmax1 = 3;

<!-- b001604 | prose | pages [34] -->
double ECost = 0;

<!-- b001605 | prose | pages [34] -->
double AlphaSafety=0;

<!-- b001606 | furniture | pages [34] -->


<!-- b001607 | prose | pages [34] -->
bool R(const double &P){

<!-- b001608 | prose | pages [34] -->
return rand()<RAND_MAX*P;

<!-- b001609 | prose | pages [34] -->
}

<!-- b001610 | prose | pages [34] -->
struct car{

<!-- b001611 | prose | pages [34] -->
int x, v, vmax;

<!-- b001612 | prose | pages [34] -->
car(int x, int v, int vmax):x(x), v(v), vmax(vmax){}

<!-- b001613 | prose | pages [34] -->
car(){}

<!-- b001614 | prose | pages [34] -->
bool operator<(const car &rhs) const {

<!-- b001615 | prose | pages [34] -->
return x < rhs.x;

<!-- b001616 | prose | pages [34] -->
}

<!-- b001617 | prose | pages [34] -->
};

<!-- b001618 | prose | pages [34] -->
#define fn(i) ((i)>=n?(i)-n:((i)<0?(i)+n:(i)))

<!-- b001619 | prose | pages [34] -->
#define fm(i) ((i)>=m?(i)-m:((i)<0?(i)+m:(i)))

<!-- b001620 | prose | pages [34] -->
#define fL(x) ((x)>=L?(x)-L:((x)<0?(x)+L:(x)))

<!-- b001621 | prose | pages [34] -->
#define takemin(x, y) x=(x)<(y)?(x):(y)

<!-- b001622 | prose | pages [34] -->
unsigned char buf[10000];

<!-- b001623 | prose | pages [34] -->
struct lane{

<!-- b001624 | prose | pages [34] -->
vector<car> c;

<!-- b001625 | prose | pages [34] -->
int cnt[7];

<!-- b001626 | prose | pages [34] -->
int tot() const {

<!-- b001627 | prose | pages [34] -->
int tot=0;

<!-- b001628 | prose | pages [34] -->
for(int i=0; i<7; i++)

<!-- b001629 | furniture | pages [35] -->
Page 35 of 40

<!-- b001630 | furniture | pages [35] -->
Team#29911

<!-- b001631 | furniture | pages [35] -->


<!-- b001632 | furniture | pages [35] -->


<!-- b001633 | prose | pages [35] -->
tot+=cnt[i];

<!-- b001634 | prose | pages [35] -->
return tot;

<!-- b001635 | prose | pages [35] -->
}

<!-- b001636 | prose | pages [35] -->
car &operator[](int i){return c[i];}

<!-- b001637 | prose | pages [35] -->
lane(const char *fpath){

<!-- b001638 | prose | pages [35] -->
memset(cnt, 0, sizeof cnt);

<!-- b001639 | prose | pages [35] -->
FILE *fp = fopen(fpath, "r");

<!-- b001640 | prose | pages [35] -->
int n, t;

<!-- b001641 | prose | pages [35] -->
fscanf(fp, "%d, %d, %d ", &L, &n, &t);

<!-- b001642 | prose | pages [35] -->
c.resize(n);

<!-- b001643 | prose | pages [35] -->
for(int i=0; i<n; i++){

<!-- b001644 | prose | pages [35] -->
fscanf(fp, "%d, %d, %d ", &c[i].x, &c[i].vmax, &c[i].v);

<!-- b001645 | prose | pages [35] -->
assert(c[i].vmax >= c[i].v);

<!-- b001646 | prose | pages [35] -->
cnt[c[i].v]++;

<!-- b001647 | prose | pages [35] -->
}

<!-- b001648 | prose | pages [35] -->
fclose(fp);

<!-- b001649 | prose | pages [35] -->
}

<!-- b001650 | prose | pages [35] -->
lane(){}

<!-- b001651 | prose | pages [35] -->
bool OK() const {

<!-- b001652 | prose | pages [35] -->
for(int i=0; i<c.size(); i++)

<!-- b001653 | prose | pages [35] -->
if(c[i].x<0 || c[i].x>=L)return false;

<!-- b001654 | prose | pages [35] -->
for(int i=0; i+1<c.size(); i++)

<!-- b001655 | prose | pages [35] -->
if(c[i].x >= c[i+1].x)return false;

<!-- b001656 | prose | pages [35] -->
if (tot() != c.size()) return false;

<!-- b001657 | prose | pages [35] -->
return true;

<!-- b001658 | prose | pages [35] -->
}

<!-- b001659 | prose | pages [35] -->
int size() const {

<!-- b001660 | prose | pages [35] -->
return c.size();

<!-- b001661 | prose | pages [35] -->
}

<!-- b001662 | prose | pages [35] -->
int advance(vector<car> &t){

<!-- b001663 | prose | pages [35] -->
int n;

<!-- b001664 | prose | pages [35] -->
t.resize(n = c.size());

<!-- b001665 | prose | pages [35] -->
if(n==0)return 0;

<!-- b001666 | prose | pages [35] -->
for(int i=0; i<c.size(); i++){

<!-- b001667 | prose | pages [35] -->
int j=fn(i+1);

<!-- b001668 | prose | pages [35] -->
t[i]=c[i];

<!-- b001669 | prose | pages [35] -->
if (t[i].v < t[i].vmax) t[i].v++;

<!-- b001670 | prose | pages [35] -->
int DXf = fL(c[j].x-c[i].x-1);

<!-- b001671 | prose | pages [35] -->
if (t[i].v > DXf) t[i].v = DXf;

<!-- b001672 | prose | pages [35] -->
if (t[i].v > 0 && R(Pd)) t[i].v--;

<!-- b001673 | prose | pages [35] -->
t[i].x = fL(t[i].x + t[i].v);

<!-- b001674 | prose | pages [35] -->
if (t[i].v > c[i].v) ECost += t[i].v+c[i].v;

<!-- b001675 | prose | pages [35] -->
}

<!-- b001676 | prose | pages [35] -->
if(t[n-1].x<t[0].x){

<!-- b001677 | furniture | pages [36] -->
Page 36 of 40

<!-- b001678 | furniture | pages [36] -->
Team#29911

<!-- b001679 | furniture | pages [36] -->


<!-- b001680 | furniture | pages [36] -->


<!-- b001681 | prose | pages [36] -->
for(int i=1; i<n; i++)

<!-- b001682 | prose | pages [36] -->
c[i]=t[i-1];

<!-- b001683 | prose | pages [36] -->
c[0]=t[n-1];

<!-- b001684 | prose | pages [36] -->
return 1;

<!-- b001685 | prose | pages [36] -->
} else swap(t, c);

<!-- b001686 | prose | pages [36] -->
memset(cnt, 0, sizeof cnt);

<!-- b001687 | prose | pages [36] -->
for(int i=0; i<c.size(); i++)

<!-- b001688 | prose | pages [36] -->
cnt[c[i].v]++;

<!-- b001689 | prose | pages [36] -->
return 0;

<!-- b001690 | prose | pages [36] -->
}

<!-- b001691 | prose | pages [36] -->
void print(){

<!-- b001692 | prose | pages [36] -->
for(int i=0; i<c.size(); i++)

<!-- b001693 | prose | pages [36] -->
printf("(%d, %d) ", c[i].x, c[i].v);

<!-- b001694 | prose | pages [36] -->
puts("");

<!-- b001695 | prose | pages [36] -->
}

<!-- b001696 | prose | pages [36] -->
void pos(FILE *fp){

<!-- b001697 | prose | pages [36] -->
int ll = ((L+7)/8+3)/4*4*8;

<!-- b001698 | prose | pages [36] -->
unsigned char tmp = 0;

<!-- b001699 | prose | pages [36] -->
for(int i=0, j=0; i<ll; i++){

<!-- b001700 | prose | pages [36] -->
int b=j<c.size()?(i<c[j].x?1:(i!=c[j++].x)):1;

<!-- b001701 | prose | pages [36] -->
tmp = (b<<7)|(tmp>>1);

<!-- b001702 | prose | pages [36] -->
if(i&0xff)buf[i>>3]=tmp;

<!-- b001703 | prose | pages [36] -->
}

<!-- b001704 | prose | pages [36] -->
fwrite(buf, 1, ll/8, fp);

<!-- b001705 | prose | pages [36] -->
}

<!-- b001706 | prose | pages [36] -->
};

<!-- b001707 | prose | pages [36] -->
#endif

<!-- b001708 | furniture | pages [36] -->


<!-- b001709 | prose | pages [36] -->
CA.cpp:

<!-- b001710 | prose | pages [36] -->
#include <string>

<!-- b001711 | prose | pages [36] -->
#include "lane.h"

<!-- b001712 | prose | pages [36] -->
#include "gen.h"

<!-- b001713 | prose | pages [36] -->
#include "SaveBMP.h"

<!-- b001714 | prose | pages [36] -->
lane l[2];

<!-- b001715 | prose | pages [36] -->
int cnt[2];

<!-- b001716 | prose | pages [36] -->
char VPATH[200];

<!-- b001717 | prose | pages [36] -->
bool rule_s(lane &l0, lane &l1, int i, int j, int DXf)

<!-- b001718 | prose | pages [36] -->
{

<!-- b001719 | prose | pages [36] -->
int m = l1.size();

<!-- b001720 | prose | pages [36] -->
if (m==0) return DXf > 1;

<!-- b001721 | prose | pages [36] -->
int k = fm(j-1);

<!-- b001722 | prose | pages [36] -->
if(DXf > 1 && l1[j].x != l0[i].x && //! no parralel car

<!-- b001723 | prose | pages [36] -->
fL(l0[i].x - l1[k].x) > min(l1[k].v+1, l1[k].vmax)) //! no accident in the other lane

<!-- b001724 | prose | pages [36] -->
return 1;

<!-- b001725 | furniture | pages [37] -->
Page 37 of 40

<!-- b001726 | furniture | pages [37] -->
Team#29911

<!-- b001727 | furniture | pages [37] -->


<!-- b001728 | furniture | pages [37] -->


<!-- b001729 | prose | pages [37] -->
return 0;

<!-- b001730 | prose | pages [37] -->
}

<!-- b001731 | prose | pages [37] -->
bool rule0(lane &l0, lane &l1, int i, int j, int DXf)

<!-- b001732 | prose | pages [37] -->
{

<!-- b001733 | prose | pages [37] -->
int m = l1.size();

<!-- b001734 | prose | pages [37] -->
if (m==0) return DXf < l0[i].vmax;

<!-- b001735 | prose | pages [37] -->
if(DXf < l0[i].vmax){ //! Not enough space in this lane

<!-- b001736 | prose | pages [37] -->
int k = fm(j-1);

<!-- b001737 | prose | pages [37] -->
if(fL(l1[j].x - l0[i].x) > DXf)   //! More space in the other lane

<!-- b001738 | prose | pages [37] -->
if (R(Pc)) return 1;

<!-- b001739 | prose | pages [37] -->
}

<!-- b001740 | prose | pages [37] -->
return 0;

<!-- b001741 | prose | pages [37] -->
}

<!-- b001742 | prose | pages [37] -->
bool rule1(lane &l0, lane &l1, int i, int j, int DXf)

<!-- b001743 | prose | pages [37] -->
{

<!-- b001744 | prose | pages [37] -->
if (l1.size() == 0) return R(Pc);

<!-- b001745 | prose | pages [37] -->
return R(Pc) && (fL(l1[j].x - l0[i].x)> min(l0[i].v+1, DXf));

<!-- b001746 | prose | pages [37] -->
//! Enough or more space in the other lane

<!-- b001747 | prose | pages [37] -->
}

<!-- b001748 | prose | pages [37] -->
int median(int *c0, int *c1){

<!-- b001749 | prose | pages [37] -->
int cnt[7];

<!-- b001750 | prose | pages [37] -->
for(int i=0; i<7; i++)

<!-- b001751 | prose | pages [37] -->
cnt[i] = c0[i] + c1[i];

<!-- b001752 | prose | pages [37] -->
int tot = 0;

<!-- b001753 | prose | pages [37] -->
for(int i=0; i<7; i++)

<!-- b001754 | prose | pages [37] -->
tot += cnt[i];

<!-- b001755 | prose | pages [37] -->
tot /= 2;

<!-- b001756 | prose | pages [37] -->
for(int i=0; tot>0 && i<7; i++){

<!-- b001757 | prose | pages [37] -->
tot -= cnt[i];

<!-- b001758 | prose | pages [37] -->
if (tot<=0) return i;

<!-- b001759 | prose | pages [37] -->
}

<!-- b001760 | prose | pages [37] -->
return 6;

<!-- b001761 | prose | pages [37] -->
}

<!-- b001762 | prose | pages [37] -->
void chLaneSim(lane &l0, lane &l1, vector<car> &t0, vector<car> &t1, int dir){

<!-- b001763 | prose | pages [37] -->
int n=l0.size(), m=l1.size(), j=0;

<!-- b001764 | prose | pages [37] -->
t0.clear(); t1.clear();

<!-- b001765 | prose | pages [37] -->
bool flag = 1;

<!-- b001766 | prose | pages [37] -->
if(!n){

<!-- b001767 | prose | pages [37] -->
swap(t0, l0.c);

<!-- b001768 | prose | pages [37] -->
return;

<!-- b001769 | prose | pages [37] -->
}

<!-- b001770 | prose | pages [37] -->
for(int i=0; i<n; i++){

<!-- b001771 | prose | pages [37] -->
int DXf = fL(l0[fn(i+1)].x - l0[i].x);

<!-- b001772 | prose | pages [37] -->
bool chLane = 1;

<!-- b001773 | furniture | pages [38] -->
Page 38 of 40

<!-- b001774 | furniture | pages [38] -->
Team#29911

<!-- b001775 | furniture | pages [38] -->


<!-- b001776 | furniture | pages [38] -->


<!-- b001777 | prose | pages [38] -->
for(; flag && j<m && l1[j].x<l0[i].x; j++);

<!-- b001778 | prose | pages [38] -->
if (j==m) flag=j=0;

<!-- b001779 | prose | pages [38] -->
chLane = chLane && rule_s(l0, l1, i, j, DXf);

<!-- b001780 | prose | pages [38] -->
if (RULE == 16) chLane = 0;

<!-- b001781 | prose | pages [38] -->
int rule, Vmedian = median(l0.cnt, l1.cnt);

<!-- b001782 | prose | pages [38] -->
bool ff = l0[i].v>Vmedian ? 1 : (l0[i].v==Vmedian?R(0.5):0);

<!-- b001783 | prose | pages [38] -->
rule = (dir<<1) + ((RULE&32) ? ff : (l0[i].vmax==Vmax0));

<!-- b001784 | prose | pages [38] -->
//! 0: l->r slow, 1: l->r fast

<!-- b001785 | prose | pages [38] -->
rule = (RULE>>rule) & 1;                    //! 2: r->l slow, 3: r->l fast

<!-- b001786 | prose | pages [38] -->
switch(rule){                               //! two_car: 1001=9, sym: 0000, sym_two_lane: 1100=12

<!-- b001787 | prose | pages [38] -->
case 0: chLane = chLane && rule0(l0, l1, i, j, DXf); break;

<!-- b001788 | prose | pages [38] -->
case 1: chLane = chLane && rule1(l0, l1, i, j, DXf); break;

<!-- b001789 | prose | pages [38] -->
default: break;

<!-- b001790 | prose | pages [38] -->
}

<!-- b001791 | prose | pages [38] -->
if(chLane)t1.push_back(l0[i]);

<!-- b001792 | prose | pages [38] -->
else t0.push_back(l0[i]);

<!-- b001793 | prose | pages [38] -->
}

<!-- b001794 | prose | pages [38] -->
}

<!-- b001795 | prose | pages [38] -->
void sim(lane &l0, lane &l1){

<!-- b001796 | prose | pages [38] -->
vector<car> t00, t01, t10, t11;

<!-- b001797 | prose | pages [38] -->
chLaneSim(l0, l1, t00, t01, 0);

<!-- b001798 | prose | pages [38] -->
chLaneSim(l1, l0, t11, t10, 1);

<!-- b001799 | prose | pages [38] -->
vector<car> t0, t1;

<!-- b001800 | prose | pages [38] -->
t0.resize(t00.size() + t10.size());

<!-- b001801 | prose | pages [38] -->
t1.resize(t01.size() + t11.size());

<!-- b001802 | prose | pages [38] -->
merge(t00.begin(), t00.end(), t10.begin(), t10.end(), t0.begin());

<!-- b001803 | prose | pages [38] -->
merge(t01.begin(), t01.end(), t11.begin(), t11.end(), t1.begin());

<!-- b001804 | prose | pages [38] -->
swap(t0, l0.c);

<!-- b001805 | prose | pages [38] -->
swap(t1, l1.c);

<!-- b001806 | prose | pages [38] -->
cnt[0] += l0.advance(t0);

<!-- b001807 | prose | pages [38] -->
cnt[1] += l1.advance(t1);

<!-- b001808 | prose | pages [38] -->
}

<!-- b001809 | prose | pages [38] -->
double func(int dx, int v){

<!-- b001810 | prose | pages [38] -->
if(v==0)return 0;

<!-- b001811 | prose | pages [38] -->
else return exp(-dx/v);

<!-- b001812 | prose | pages [38] -->
}

<!-- b001813 | prose | pages [38] -->
double cal_safety(lane &l){

<!-- b001814 | prose | pages [38] -->
double res=0;

<!-- b001815 | prose | pages [38] -->
if(l.size()==0)return 0;

<!-- b001816 | prose | pages [38] -->
for(int i=0; i+1<l.size(); i++)

<!-- b001817 | prose | pages [38] -->
res += func(l[i+1].x-l[i].x, l[i].v);

<!-- b001818 | prose | pages [38] -->
res += func(l[0].x-l.c.back().x+L, l.c.back().v);

<!-- b001819 | prose | pages [38] -->
return res;

<!-- b001820 | prose | pages [38] -->
}

<!-- b001821 | furniture | pages [39] -->
Page 39 of 40

<!-- b001822 | furniture | pages [39] -->
Team#29911

<!-- b001823 | furniture | pages [39] -->


<!-- b001824 | furniture | pages [39] -->


<!-- b001825 | prose | pages [39] -->
void gao()

<!-- b001826 | prose | pages [39] -->
{

<!-- b001827 | prose | pages [39] -->
l[0] = lane("lane0.csv");

<!-- b001828 | prose | pages [39] -->
l[1] = lane("lane1.csv");

<!-- b001829 | prose | pages [39] -->
FILE *fout0, *fout1;

<!-- b001830 | prose | pages [39] -->
if(VISUALIZE){

<!-- b001831 | prose | pages [39] -->
fout0 = SaveBmp((string(VPATH)+"0.bmp").c_str(), T, L);

<!-- b001832 | prose | pages [39] -->
fout1 = SaveBmp((string(VPATH)+"1.bmp").c_str(), T, L);

<!-- b001833 | prose | pages [39] -->
}

<!-- b001834 | prose | pages [39] -->
int t;

<!-- b001835 | prose | pages [39] -->
if(VISUALIZE) t=0; else t=T/5;

<!-- b001836 | prose | pages [39] -->
while (t--) sim(l[0], l[1]);

<!-- b001837 | prose | pages [39] -->
t = T;

<!-- b001838 | prose | pages [39] -->
cnt[0] = cnt[1] = 0; AlphaSafety = 0; ECost = 0;

<!-- b001839 | prose | pages [39] -->
while (t--) {

<!-- b001840 | prose | pages [39] -->
sim(l[0], l[1]);

<!-- b001841 | prose | pages [39] -->
l[0].OK();

<!-- b001842 | prose | pages [39] -->
l[1].OK();

<!-- b001843 | prose | pages [39] -->
if(VISUALIZE){

<!-- b001844 | prose | pages [39] -->
l[0].pos(fout0);

<!-- b001845 | prose | pages [39] -->
l[1].pos(fout1);

<!-- b001846 | prose | pages [39] -->
}

<!-- b001847 | prose | pages [39] -->
AlphaSafety+=cal_safety(l[0])+cal_safety(l[1]);

<!-- b001848 | prose | pages [39] -->
}

<!-- b001849 | prose | pages [39] -->
AlphaSafety/=l[0].size()+l[1].size();

<!-- b001850 | prose | pages [39] -->
AlphaSafety/=T;

<!-- b001851 | prose | pages [39] -->
//printf("Q=%.5lf AlphaS=%.5lf\n", cnt/2.0/T, AlphaSafety);

<!-- b001852 | prose | pages [39] -->
if(VISUALIZE){

<!-- b001853 | prose | pages [39] -->
fclose(fout0);

<!-- b001854 | prose | pages [39] -->
fclose(fout1);

<!-- b001855 | prose | pages [39] -->
}

<!-- b001856 | prose | pages [39] -->
}

<!-- b001857 | prose | pages [39] -->
pair<double, double> stat(vector<double> &a){

<!-- b001858 | prose | pages [39] -->
assert(a.size()>=2);

<!-- b001859 | prose | pages [39] -->
double mean=0;

<!-- b001860 | prose | pages [39] -->
for(int i=0; i<a.size(); i++)

<!-- b001861 | prose | pages [39] -->
mean+=a[i];

<!-- b001862 | prose | pages [39] -->
mean/=a.size();

<!-- b001863 | prose | pages [39] -->
double s=0;

<!-- b001864 | prose | pages [39] -->
for(int i=0; i<a.size(); i++)

<!-- b001865 | prose | pages [39] -->
s+=(a[i]-mean)*(a[i]-mean);

<!-- b001866 | prose | pages [39] -->
s/=a.size()-1;

<!-- b001867 | prose | pages [39] -->
s=sqrt(s);

<!-- b001868 | prose | pages [39] -->
return make_pair(mean, s);

<!-- b001869 | furniture | pages [40] -->
Page 40 of 40

<!-- b001870 | furniture | pages [40] -->
Team#29911

<!-- b001871 | furniture | pages [40] -->


<!-- b001872 | furniture | pages [40] -->


<!-- b001873 | prose | pages [40] -->
}

<!-- b001874 | prose | pages [40] -->
int main()

<!-- b001875 | prose | pages [40] -->
{

<!-- b001876 | prose | pages [40] -->
srand(time(0));

<!-- b001877 | prose | pages [40] -->
FILE *fin = fopen("coef.prn", "r");

<!-- b001878 | prose | pages [40] -->
FILE *fout = fopen("log.csv", "a");

<!-- b001879 | prose | pages [40] -->
if (fin == NULL || fout == NULL) return -1;

<!-- b001880 | prose | pages [40] -->
int sum=0;

<!-- b001881 | prose | pages [40] -->
double den=0;

<!-- b001882 | prose | pages [40] -->
fgets((char *)buf, 10000, fin);

<!-- b001883 | prose | pages [40] -->
while(1){

<!-- b001884 | prose | pages [40] -->
if(fscanf(fin, "%d %d %lf %lf %lf %lf %d %d %d %d %s",

<!-- b001885 | prose | pages [40] -->
&L, &T, &den, &Pd, &Pc, &Pv, &Vmax0, &Vmax1, &VISUALIZE, &RULE, VPATH)!=11){

<!-- b001886 | prose | pages [40] -->
break;

<!-- b001887 | prose | pages [40] -->
}

<!-- b001888 | prose | pages [40] -->
fprintf(fout, "%d, %d, %lf, %lf, %lf, %lf, %d, %d, %d, ",

<!-- b001889 | prose | pages [40] -->
L,  T,  den, Pd,  Pc, Pv, Vmax0, Vmax1, RULE);

<!-- b001890 | prose | pages [40] -->
vector<double> q[2], AlphaS, EC;

<!-- b001891 | prose | pages [40] -->
int REP = VISUALIZE?2:20;

<!-- b001892 | prose | pages [40] -->
for(int i=0; i<REP; i++){

<!-- b001893 | prose | pages [40] -->
gen("lane0.csv", L, den, Vmax0, Vmax1, Pv);

<!-- b001894 | prose | pages [40] -->
gen("lane1.csv", L, den, Vmax0, Vmax1, Pv);

<!-- b001895 | prose | pages [40] -->
gao();

<!-- b001896 | prose | pages [40] -->
q[0].push_back(cnt[0]*1.0/T);

<!-- b001897 | prose | pages [40] -->
q[1].push_back(cnt[1]*1.0/T);

<!-- b001898 | prose | pages [40] -->
AlphaS.push_back(AlphaSafety);

<!-- b001899 | prose | pages [40] -->
ECost /= cnt[0]+cnt[1];

<!-- b001900 | prose | pages [40] -->
EC.push_back(ECost);

<!-- b001901 | prose | pages [40] -->
printf("%d/%d RULE=%d Den=%.3lf Q0=%.3lf Q1=%.3lf AS=%.3lf EC=%.3lf\n", i+1, REP, RULE, den,

<!-- b001902 | prose | pages [40] -->
q[0].back(), q[1].back(), AlphaS.back(), EC.back());

<!-- b001903 | prose | pages [40] -->
}

<!-- b001904 | prose | pages [40] -->
pair<double, double> t0 = stat(q[0]), t1 = stat(q[1]), t2 = stat(AlphaS), t3 = stat(EC);

<!-- b001905 | prose | pages [40] -->
fprintf(fout, "%.5lf, %.5lf, %.5lf, %.5lf, %.5lf, %.5lf, %.5lf, %.5lf\n", t0.first, t0.second, t1.first, t1.second, t2.first,

<!-- b001906 | prose | pages [40] -->
t2.second, t3.first, t3.second);

<!-- b001907 | prose | pages [40] -->
}

<!-- b001908 | prose | pages [40] -->
fclose(fout);

<!-- b001909 | prose | pages [40] -->
fclose(fin);

<!-- b001910 | prose | pages [40] -->
}

<!-- b001911 | furniture | pages [40] -->

