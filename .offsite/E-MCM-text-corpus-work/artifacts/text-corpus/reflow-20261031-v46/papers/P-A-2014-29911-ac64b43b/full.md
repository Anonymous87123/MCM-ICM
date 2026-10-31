# P-A-2014-29911-ac64b43b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Page 1 of 40

<!-- b000002 | front_matter | pages [1] -->
Team#29911

<!-- b000003 | front_matter | pages [1] -->
Team Control Number

<!-- b000004 | front_matter | pages [1] -->
29911

<!-- b000005 | front_matter | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000006 | front_matter | pages [1] -->
A

<!-- b000007 | heading | pages [1] -->
Summary

<!-- b000008 | prose | pages [1] -->
The keep-right-except-to-pass (KRETP) rule has been adopted by many countries around the world, but does this rule actually make our transportation system more efficient? This report aims to analyze this rule along with several other traffic regulations.

<!-- b000009 | prose | pages [1] -->
Using a discrete cellular-automaton (CA) model and a continuum model, we can simulate real-life traffic situation on freeways via the Monte Carlo method and PDE system respectively. Through comparison with other two traffic rules, we obtain the conclusion that the KRETP rule is rather effective.

<!-- b000010 | prose | pages [1] -->
First we define three parameters---traffic flow, safety index and average energy consumption (AEC) to evaluate the performance of the KRETP rule under various vehicle density. By calculating the optimal maximum velocities during light and heavy traffic, we obtain the influence of under-posted and over-posted speed limits. We also assert that our model can be transferred in "left-most" countries with a simple change of orientation.

<!-- b000011 | prose | pages [1] -->
Then we introduce two other traffic rules----the "Slow-Cars-To-Right" (SCTR) rule and the "Free Driving & Free Overtaking" (FDFO) rule. By comparing these three rules in terms of our pre-defined parameters, we confirm KRETP rule's superiority and provide strategic advice for future freeway construction.

<!-- b000012 | prose | pages [1] -->
Next, under the control of an intelligent system, a "median" optimization method is proposed to improve the overall quality of freeway transportation system. According to simulation result, our optimization method does improve the performance in terms of all three parameters.

<!-- b000013 | prose | pages [1] -->
Finally, we discuss upon several defects of our model that require further research.

<!-- b000014 | keywords | pages [1] -->
Keywords: KRETP Rule, CA Model, Continuum Model, Monte Carlo Method,

<!-- b000015 | prose | pages [1] -->
Traffic Flow, Safety Index, Average Energy Consumption (AEC), Optimization

<!-- b000016 | prose | pages [1, 2] -->
 

<!-- b000017 | furniture | pages [2] -->
Page 2 of 40

<!-- b000018 | furniture | pages [2] -->
Team#29911

<!-- b000020 | prose | pages [2] -->


<!-- b000021 | prose | pages [2] -->


<!-- b000022 | prose | pages [2] -->


<!-- b000023 | prose | pages [2] -->


<!-- b000024 | prose | pages [2] -->
The Keep-Right-Except-To-Pass Rule

<!-- b000025 | furniture | pages [3] -->
Page 3 of 40

<!-- b000026 | furniture | pages [3] -->
Team#29911

<!-- b000027 | heading | pages [3] -->
Contents

<!-- b000028 | contents | pages [3] -->
1

<!-- b000029 | contents | pages [3] -->
Introduction..................................................................................................................................4

<!-- b000030 | contents | pages [3] -->
2

<!-- b000031 | contents | pages [3] -->
Assumptions.................................................................................................................................5

<!-- b000032 | contents | pages [3] -->
3

<!-- b000033 | contents | pages [3] -->
Modeling for Right-Most Rule...............................................................................................5

<!-- b000034 | contents | pages [3] -->
3.1 Discrete Modeling for Right-Most Rule.....................................................................5

<!-- b000035 | contents | pages [3] -->
3.1.1 Model Establishment............................................................................................5

<!-- b000036 | contents | pages [3] -->
3.1.2 Parameter Evaluation.........................................................................................10

<!-- b000037 | contents | pages [3] -->
3.1.3 Model Solution and Analysis...........................................................................10

<!-- b000038 | contents | pages [3] -->
3.2 Continuum Modeling for Right-Most Rule.............................................................17

<!-- b000039 | contents | pages [3] -->
3.2.1 Model Establishment..........................................................................................17

<!-- b000040 | contents | pages [3] -->
3.2.2 Model Solution and Analysis...........................................................................18

<!-- b000041 | contents | pages [3] -->
3.3 Comparison of Discrete Model and Continuum Model....................................22

<!-- b000042 | contents | pages [3] -->
3.4 Transferability Analysis of Model in "Left-Handed" Countries.....................22

<!-- b000043 | contents | pages [3] -->
4

<!-- b000044 | contents | pages [3] -->
Modeling for Alternative Freeway Traffic Rules.........................................................22

<!-- b000045 | contents | pages [3] -->
4.1 "Slow-Cars-To-Right" Rule............................................................................................22

<!-- b000046 | contents | pages [3] -->
4.2 "Free Driving & Free Overtaking" Rule....................................................................23

<!-- b000047 | contents | pages [3] -->
4.3 Comparison of Different Traffic Rules......................................................................24

<!-- b000048 | contents | pages [3] -->
5

<!-- b000049 | contents | pages [3] -->
Modeling for Intelligent-System Control........................................................................26

<!-- b000050 | contents | pages [3] -->
5.1 "Median" Optimization...................................................................................................26

<!-- b000051 | contents | pages [3] -->
5.2 Possible Further Improvements…………………………………………………………29

<!-- b000052 | contents | pages [3] -->
6

<!-- b000053 | contents | pages [3] -->
Superiority and Weakness....................................................................................................29

<!-- b000054 | contents | pages [3] -->
6.1 Superiority Analysis.........................................................................................................29

<!-- b000055 | contents | pages [3] -->
6.2 Weakness Analysis............................................................................................................30

<!-- b000056 | contents | pages [3] -->
6.3 Future Research.................................................................................................................30

<!-- b000057 | contents | pages [3] -->
6.3.1 Possible Optimization of Discrete Model....................................................30

<!-- b000058 | contents | pages [3] -->
6.3.2 Possible Optimization of Continuum Model..............................................31

<!-- b000059 | contents | pages [3] -->
7

<!-- b000060 | contents | pages [3] -->
Conclusion...................................................................................................................................31

<!-- b000061 | contents | pages [3] -->
8

<!-- b000062 | contents | pages [3] -->
References...................................................................................................................................32

<!-- b000063 | contents | pages [3] -->
9

<!-- b000064 | contents | pages [3] -->
Appendix..................................................................................................................................... 32

<!-- b000065 | furniture | pages [4] -->
Page 4 of 40

<!-- b000066 | furniture | pages [4] -->
Team#29911

<!-- b000067 | heading | pages [4] -->
1 Introduction

<!-- b000068 | prose | pages [4] -->
Traffic rule plays an essential role in a nation's transportation system. An optimal traffic rule can dramatically enhance the capacity and efficiency of the transportation network, providing common citizens with tremendous convenience. In this report, we will mainly focus on one such rule which requires automobiles to stay in the right lane unless they have to overtake.

<!-- b000069 | prose | pages [4] -->
America first enacted the "keep-right-except-to-pass" law in New York State in 1804, followed by many other countries in the following decades. [1] Up to now, most countries are "right-handed" countries with very few exceptions such as the UK and Australia. On American multilane freeways, for example, drivers are required to drive in the right-most lane unless they need to overtake, in which case they move one lane to the left and then switch back to the right-most lane. See in Figure 1.

<!-- b000070 | prose | pages [4] -->
Despite the long history of this rule, there has been little scientific inquiry into the effect of this rule. In such circumstances, a systematic analysis of this rule's realistic effect, including the change in traffic flow, safety index and energy consumption.

<!-- b000071 | prose | pages [4] -->
More specifically, we are expected to examine the following issues in our report:  Analyze the effect of the "keep-right-except-to-pass" rule in various terms under different vehicle densities (light and heavy traffic);  Calculate the optimized speed to maximize a weighted function of the traffic flow, safety index and average energy consumption.  Discuss the role of under-posted and over-posted speed limits and the transferability of our model in "left-handed" countries where driving on the left lane is the norm;  Propose other possible freeway traffics rules and compare them with the "keep-right-except-to-pass" rule;  Discuss the transferability of our model in "left-handed" countries where driving on the left lane is the norm;  Design optimization method to enlarge traffic flow when equipped with an intelligent system.

<!-- b000072 | furniture | pages [5] -->
Page 5 of 40

<!-- b000073 | furniture | pages [5] -->
Team#29911

<!-- b000074 | caption | pages [5] -->
Figure 1. Illustration of "Keep-Right-Except-To-Pass" Rule

<!-- b000075 | heading | pages [5] -->
2 Assumptions

<!-- b000076 | prose | pages [5] -->
 Assuming automobile to move in straight lines;  Assuming that jams only occur because of gradual piling of automobiles;  Without consideration of sudden crashes that will influence the behavior of subsequent vehicles;  Assuming that the parallel movement of a vehicle into another lane takes no time;  Assuming that all the drivers on the freeway are abide by the traffic rules;  Assuming that the vehicles have the same length and mass;  Assuming that freeways have no extra entrance or exit.

<!-- b000077 | heading | pages [5] -->
3 Modeling for Right-Most Rule

<!-- b000078 | prose | pages [5] -->
In order to analyze the effect of the "right-most" rule, first we have to establish a model to simulate the traffic flow on the multilane freeway. Then we add certain driving and lane-changing rules to make sure that in our simulation the automobiles are abide by the "right-most" rule.

<!-- b000079 | heading | pages [5] -->
3.1 Discrete Modeling for Right-Most Rule

<!-- b000080 | prose | pages [5] -->
Discrete models treat both time and the position of vehicles as discrete quantities and simulate the moving of automobiles step by step. We start out simulation with a single kind of vehicle (single maximum speed) on a double-lane freeway (right lane is slow lane and left lane is fast lane) and then extend to two kinds of vehicles, namely, fast car and slow car (two maximum speeds), which is closer to realistic situation.

<!-- b000081 | heading | pages [5] -->
3.1.1 Model Establishment

<!-- b000082 | prose | pages [5, 6] -->
 Vehicles of a Single Kind Among the various discrete models, we adopt the "Particle-Hopping" model, which was initially formulated by Nagel and Schreckenberg (NS) to idealize the movement of vehicles as the discrete "hopping" of particles. Figure 2 is a vivid illustration of our model. We treat the double-lane freeway as a two-column lattice and each vehicle contains exactly one lattice.

<!-- b000083 | furniture | pages [6] -->
Page 6 of 40

<!-- b000084 | furniture | pages [6] -->
Team#29911

<!-- b000086 | caption | pages [6] -->
Figure 2. Representation of the "Particle-Hopping" Model

<!-- b000087 | prose | pages [6] -->
We apply the Monte Carlo method to simulate the traffic flow on the double-lane freeway.[2] The quantities involved in the simulation are shown in

<!-- b000088 | caption | pages [6] -->
Table 1.

<!-- b000089 | heading | pages [6] -->
Notation

<!-- b000090 | prose | pages [6] -->
Definition

<!-- b000091 | prose | pages [6] -->
𝑋(𝑘) The position of car numbered 𝑘

<!-- b000092 | prose | pages [6] -->
𝑉(𝑘) The velocity of car numbered 𝑘

<!-- b000093 | prose | pages [6] -->
𝑓(𝑘) The gap in front of car numbered 𝑘 in the present lane Δ𝑋𝑝

<!-- b000094 | prose | pages [6] -->
𝑏(𝑘) The gap behind car numbered 𝑘 in the present lane Δ𝑋𝑝

<!-- b000095 | prose | pages [6] -->
𝑓(𝑘) The gap in front of car numbered 𝑘 in the other lane Δ𝑋𝑜

<!-- b000096 | prose | pages [6] -->
The gap behind car numbered 𝑘 in the other lane 𝑏(𝑘) Δ𝑋𝑜

<!-- b000097 | prose | pages [6] -->
𝑉𝑚𝑎𝑥(𝑘) The maximum velocity the kth car can achieve on the freeway

<!-- b000098 | prose | pages [6] -->
𝑄 The traffic flow(number of cars passed per lane per unit time)

<!-- b000099 | prose | pages [6] -->
𝛼𝑠𝑎𝑓𝑒 The safety index

<!-- b000100 | prose | pages [6] -->
𝐿 The length of the lane during simulation*

<!-- b000101 | prose | pages [6, 7] -->
𝑇 The duration of the simulation* 𝑃𝑑 The probability of a car decelerating*

<!-- b000102 | furniture | pages [7] -->
Page 7 of 40

<!-- b000103 | furniture | pages [7] -->
Team#29911

<!-- b000105 | prose | pages [7] -->
𝑃𝑐 The probability of a car changing lane*

<!-- b000106 | prose | pages [7] -->
𝑛 The density of vehicles *

<!-- b000107 | prose | pages [7] -->
𝑁 The number of car during simulation 𝑁= 2𝑛𝐿

<!-- b000108 | caption | pages [7] -->
Table 1. Definition of Notation in "Particle-Hopping" Model

<!-- b000109 | prose | pages [7] -->
(Terms marked with an asterisk (*) require pre-evaluation before the simulation begins)

<!-- b000110 | prose | pages [7] -->
Before the simulation begins, we need to evaluate the following five parameters: number of cars 𝑁, the length of lane 𝐿, the duration of the simulation 𝑇, the maximum velocity vehicles can achieve 𝑉𝑚𝑎𝑥, the probability for a driver to decelerate during each unit time 𝑃𝑑 and the probability for a driver to change lane 𝑃𝑐 if the current situation qualifies the rule of changing lanes.

<!-- b000111 | prose | pages [7] -->
After these parameters have been evaluated, we set the position of each car 𝑋(𝑛) randomly in the double-lane freeway with half cars on the left (fast) lane and the other half on the right (slow) lane and the velocity of each car 𝑉(𝑛)randomly between [𝑉𝑚𝑎𝑥/2, 𝑉𝑚𝑎𝑥]. We set the entire freeway to be a loophole so that once a car reaches the last lattices it will re-enter the double-lane freeway in the first lattices. Under such conditions, the density of the vehicles remain unchanged throughout the simulation.

<!-- b000112 | prose | pages [7] -->
After the simulation begins, at each time unit the driver will either remain in the same lane or change lane if situation permits. The rule of acceleration and deceleration is as follows:

<!-- b000113 | prose | pages [7] -->
(𝑖)  𝐼𝑓 𝑉(𝑛) < 𝑉𝑚𝑎𝑥, 𝑡ℎ𝑒𝑛 𝑉(𝑛) = 𝑉(𝑛) + 1;

<!-- b000114 | prose | pages [7] -->
(𝑖𝑖) 𝐼𝑓 𝑟𝑎𝑛 𝑓< 𝑝𝑑, 𝑡ℎ𝑒𝑛 𝑉(𝑛) = 𝑉(𝑛) −1;

<!-- b000115 | caption | pages [7] -->
Table 2. The Rule of Acceleration and Deceleration

<!-- b000116 | prose | pages [7] -->
where 𝑟𝑎𝑛 𝑓 is a random number between 0 and 1 generated at each time unit.

<!-- b000117 | prose | pages [7, 8] -->
The permission rule for changing lane is much more complex and comprised of several basic rules. It is derived from Wagner’s according to the statistics gathered from a Germany freeway where "right-most" rule is adopted:[3] Rule stay except Rule change when possible Rule safety (Rule #1) blocked (Rule #0) 𝑓(𝑛) > ΔX𝑝 𝑓(𝑛)(more space (i)ΔX𝑜 𝑓(𝑘) > 0, 𝑓(𝑛) < 𝑉𝑚𝑎𝑥+ 1 , (i) ΔX𝑝 (i)ΔX𝑝 𝑓(𝑛) > on the other lane) or  ΔX𝑜 enough space in not enough space in 𝑉(𝑘)(enough space on the other front front lane) 𝑓(𝑛) > ΔX𝑝 𝑓(𝑛) (ii) The nearest (ii)  ΔX𝑜 , more space on the (ii) ran f < Pc neighbor site in the other lane other lane is empty. (iii) ΔXo b(n) > Vmax , enough space to the (iii) ran f < Pc next car on the other lane

<!-- b000118 | furniture | pages [8] -->
Page 8 of 40

<!-- b000119 | furniture | pages [8] -->
Team#29911

<!-- b000121 | caption | pages [8] -->
Table 3. The Basic Rules

<!-- b000122 | prose | pages [8] -->
𝒓𝒊𝒈𝒉𝒕→𝒍𝒆𝒇𝒕 𝒍𝒆𝒇𝒕→𝒓𝒊𝒈𝒉𝒕 (i) Rule safety (i) Rule safety (ii) Rule #1 (ii) Rule #0

<!-- b000123 | caption | pages [8] -->
Table 4. The Rule of Lane Changing corresponding to the “rightmost” rule

<!-- b000124 | prose | pages [8] -->
Our Monte Carlo simulation has three outputs: traffic flow 𝑄 and safety index 𝛼𝑠𝑎𝑓𝑒 and the energy cost E0. For traffic flow 𝑄, we choose a fixed point (in our simulation we choose the end point of the lattices since the freeway is a loop) to count the total number of cars passing that point denoted as 𝑁𝑡𝑜𝑡𝑎𝑙 within the duration of the simulation 𝑇, then we use the following equation to calculate 𝑄:

<!-- b000125 | prose | pages [8] -->
𝑄= 𝑁𝑡𝑜𝑡𝑎𝑙 . 𝑇 As for 𝛼𝑠𝑎𝑓𝑒, we make the assumption that safety index is proportionate to the reaction time of all the drivers on the freeway throughout the entire simulation. We take the proportionate coefficient to be 1 for convenience:

<!-- b000126 | prose | pages [8] -->
𝑓 𝑁 ∑∑[exp(−ΔX𝑝 (𝑛)/𝑉(𝑛))] 𝑇 1 . 𝛼𝑠𝑎𝑓𝑒= 𝑁⋅𝑇

<!-- b000127 | prose | pages [8] -->
In Table 5, we present the specific steps of our Monte Carlo simulation:

<!-- b000128 | prose | pages [8] -->
Input Length of the lane, 𝑳.

<!-- b000129 | prose | pages [8] -->
Duration of the simulation 𝑻.

<!-- b000130 | furniture | pages [9] -->
Page 9 of 40

<!-- b000131 | furniture | pages [9] -->
Team#29911

<!-- b000132 | prose | pages [9] -->
Vehicle density 𝒏.

<!-- b000133 | prose | pages [9] -->
Deceleration probability 𝑷𝒅.

<!-- b000134 | prose | pages [9] -->
Lane changing probability 𝑷𝒄. Output Traffic flow 𝑄.

<!-- b000135 | prose | pages [9] -->
Safety index 𝛼𝑠𝑎𝑓𝑒.

<!-- b000136 | prose | pages [9] -->
Energy cost 𝐸0 Step 1 Randomly generate the initial position, speed and max speed of vehicle 𝑖 𝑋(𝑘), 𝑉(𝑘) and 𝑉𝑚𝑎𝑥(𝑘).

<!-- b000137 | prose | pages [9] -->
Step 2 Repeat Step 3 ~ 16 𝑇 times.

<!-- b000138 | prose | pages [9] -->
Step 3 Repeat Step 4~5 for each vehicle Step 4 Apply the safety rule to vehicle 𝑖, skip Step 5 if vehicle 𝑖 doesn’t pass the rule Step 5 Apply either change lane rule #0 or change lane rule #1 to vehicle i based on which lane it is on, its current speed and the current model, then decide whether it should change its lane.

<!-- b000139 | prose | pages [9] -->
Step 6 Update each vehicle to its new lane.

<!-- b000140 | prose | pages [9] -->
Step 7 Repeat Step 8~16 for each vehicle number 𝑘.

<!-- b000141 | prose | pages [9] -->
Step 8 Let the expected new speed 𝑉′(𝑘) = 𝑉(𝑘) + 1 Step 9 𝑓(𝑘) < 𝑉′(𝑘) , let 𝑉′(𝑘) = Δ𝑋𝑝 𝑓(𝑘) −1. If Δ𝑋𝑝 Step 10 If 𝑉′(𝑘) > 0, generate a random number in [0, 1] and check whether it is smaller than 𝑃𝑑, let 𝑉′(𝑘) = 𝑉′(𝑘) −1 if so. Step 11 Let 𝑋′(𝑘) = 𝑋(𝑘) + 𝑉′(𝑘) Step 13 𝑓′(𝑘) Δ𝑋𝑝 𝑉′(𝑘) ) 𝛼𝑠𝑎𝑓𝑒= 𝛼𝑠𝑎𝑓𝑒+ exp (−

<!-- b000142 | prose | pages [9] -->
Step 14 If 𝑋′(𝑘) ≥𝐿, then 𝑋′(𝑘)−= 𝐿, 𝑄= 𝑄+ 1 Step 15 If 𝑉(𝑘) < 𝑉′(𝑘), 𝐸0+= 𝑉(𝑘) + 𝑉′(𝑘) Step 16 Let 𝑋(𝑘) = 𝑋′(𝑘), 𝑉(𝑘) = 𝑉′(𝑘) Step 17 𝛼𝑠𝑎𝑓𝑒 𝐸0 𝑄 𝑄, 𝛼𝑠𝑎𝑓𝑒= 𝑄, 𝑄= 𝑇 𝐸0 =

<!-- b000143 | prose | pages [9] -->
Step 18 Output and halt.

<!-- b000144 | caption | pages [9] -->
Table 5. Monte Carlo Procedures

<!-- b000145 | prose | pages [9] -->
 Vehicles of Two Kinds (Fast Cars & Slow Cars)

<!-- b000146 | prose | pages [9] -->
Next, we consider a more complex situation in which cars are classified into 𝑓 fast cars and slow cars with respective maximum speed 𝑉𝑚𝑎𝑥 and 𝑉𝑚𝑎𝑥 , with 𝑠

<!-- b000147 | prose | pages [9] -->
other conditions and rules unchanged.

<!-- b000148 | furniture | pages [10] -->
Page 10 of 40

<!-- b000149 | furniture | pages [10] -->
Team#29911

<!-- b000150 | prose | pages [10] -->
Next, we apply a similar Monte Carlo algorithm to simulate the traffic flow with two kinds of vehicles and output corresponding flow 𝑄 and safe index 𝛼𝑚𝑎𝑥.

<!-- b000151 | heading | pages [10] -->
3.1.2 Parameter Evaluation

<!-- b000152 | prose | pages [10] -->
 The length of the lattices 𝐿= 2048;  The vehicle density 𝑛= 0.02, 0.04, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3;  The number of the total vehicles 𝑁= 2𝑛𝐿;  The duration of the simulation 𝑇= 4096;  The deceleration probability 𝑃𝑑= 0.1;  The change lane probability 𝑃𝑐= 0.7;  In the case of vehicles of single kind, set maximum velocity 𝑉𝑚𝑎𝑥= 5;

<!-- b000153 | prose | pages [10] -->
𝑓  In the case of vehicles of two kinds, set maximum velocity of fast car 𝑉𝑚𝑎𝑥 = 5, set maximum velocity for slow car 𝑉𝑚𝑎𝑥 = 3; 𝑠

<!-- b000154 | prose | pages [10] -->
 The ratio of fast car to slow car is 4:1, the initial number of vehicle in each lane is 1:1.

<!-- b000155 | heading | pages [10] -->
3.1.3 Model Solution and Analysis

<!-- b000156 | prose | pages [10] -->
We mainly analyze the influence of the right-most rule on three parameters: Traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and average energy consumption 𝐸0. Then we assign a relative weight to each parameter to calculate an optimal velocity during light traffic and heavy traffic. We will only present the simulation result of the two-kind vehicle model.

<!-- b000157 | prose | pages [10] -->
 Traffic Flow

<!-- b000158 | prose | pages [10] -->
As we have discussed before, we define the traffic flow 𝑄 as the number of cars passing a fixed point per unit time, or

<!-- b000159 | prose | pages [10] -->
𝑄= 𝑁𝑡𝑜𝑡𝑎𝑙 𝑇

<!-- b000160 | prose | pages [10] -->
In Figure 3, we present the value of traffic flow 𝑄 under different vehicle density 𝑛.

<!-- b000161 | furniture | pages [11] -->
Page 11 of 40

<!-- b000162 | furniture | pages [11] -->
Team#29911

<!-- b000163 | caption | pages [11] -->
Figure 3. Relationship of Traffic Flow 𝑄 and Vehicle Density 𝑛

<!-- b000164 | prose | pages [11] -->
Apparently, the pattern in Figure 3 accords with realistic situation qualitatively. When the vehicle density on a freeway is relatively low, slight increase of vehicle, or in other words, vehicle density will cause traffic flow to rise dramatically because according to our rules vehicles accelerate very easily. In our simulation, the peak value of flow 𝑄 occurs when density is around 0.2. After the climax, the traffic flow will tend to drop as vehicle density continues to rise because more likely car jams will obstruct vehicles from accelerating freely. Finally, when the density approaches 1, in other words, the freeway is almost "full", vehicles could barely move thus the flow approaches 0.

<!-- b000165 | prose | pages [11] -->
 Safety Index

<!-- b000166 | prose | pages [11] -->
Notice that the longer reaction time is, the safer the situation will be. Thus according to our definition of the safety index

<!-- b000167 | prose | pages [11] -->
𝑓 𝑁 ∑∑[exp(−Δ𝑝 𝑋(𝑛)/𝑉(𝑛))] 𝑇 1 𝛼𝑠𝑎𝑓𝑒= 𝑁⋅𝑇

<!-- b000168 | prose | pages [11] -->
a larger value of 𝛼𝑠𝑎𝑓𝑒 indicates a more dangerous situation. We again plot safety index 𝛼𝑠𝑎𝑓𝑒 against vehicle density 𝑛. The result is shown in Figure 4.

<!-- b000169 | furniture | pages [12] -->
Page 12 of 40

<!-- b000170 | furniture | pages [12] -->
Team#29911

<!-- b000171 | caption | pages [12] -->
Figure 4. Relationship of Safety Index 𝛼𝑠𝑎𝑓𝑒

<!-- b000172 | prose | pages [12] -->
and Vehicle Density 𝑛 (lower is safer)

<!-- b000173 | prose | pages [12] -->
It is easy to understand the pattern in Figure 4. When the vehicle density is relatively small, accidental risk rises as the number of car increases because vehicles are likely to attain high velocities. After the peak value, the risk drops as density rises because though the number of vehicle rises, the average velocity decreases dramatically. Since most vehicles drive much slower, the overall situation becomes actually safer. Finally, when all the vehicles cannot move at all (when 𝑛= 1), the situation is absolutely safe. Notice that the climax vehicle density are nearly the same in traffic flow and safety index because both quantities are closely related to average velocity.

<!-- b000174 | prose | pages [12] -->
 Average Energy Consumption

<!-- b000175 | prose | pages [12] -->
Now we define another important parameter called the average energy consumption denoted 𝐸0. We use it to measure the energy consumed during each acceleration. We approximate the quantity as proportionate to change of kinetic energy. For a particular vehicle 𝑛, we denote its velocity at time 𝑡 and 𝑡+ 1 as 𝑉(𝑡)(𝑛) and 𝑉(𝑡+1)(𝑛). Furthermore, we make the assumption that each vehicle has unit mass. Now we can derive the formula for 𝐸0:

<!-- b000176 | prose | pages [12] -->
1 2 𝑚[(𝑉(𝑡)(𝑛))2 −(𝑉(𝑡−1)(𝑛))2] 𝑇 𝑁 ∑ ∑ 𝑡=1 𝑛=1 𝐸0 ∝ 𝑄

<!-- b000177 | prose | pages [12, 13] -->
1 𝑇 𝑁 2 𝑚[𝑉(𝑡)(𝑛) −𝑉(𝑡−1)(𝑛)][𝑉(𝑡)(𝑛) + 𝑉(𝑡−1)(𝑛)] ∑ ∑ 𝑡=1 𝑛=1 ∝ 𝑄 𝑇 𝑁 [𝑉(𝑡)(𝑛) + 𝑉(𝑡−1)(𝑛)] ∑ ∑ 𝑡=1 𝑛=1 ∝ 𝑄

<!-- b000178 | furniture | pages [13] -->
Page 13 of 40

<!-- b000179 | furniture | pages [13] -->
Team#29911

<!-- b000181 | prose | pages [13] -->
In order for convenience, we evaluate the proportionate coefficient as 1. So that

<!-- b000182 | prose | pages [13] -->
𝑇 𝑁 [𝑉(𝑡)(𝑛) + 𝑉(𝑡−1)(𝑛)] ∑ ∑ 𝑡=1 𝑛=1 𝐸0 = 𝑄

<!-- b000183 | prose | pages [13] -->
We again plot the average energy consumption against vehicle density in

<!-- b000184 | caption | pages [13] -->
Figure 5.

<!-- b000185 | caption | pages [13] -->
Figure 5. Relationship of Energy Consumption 𝐸0

<!-- b000186 | prose | pages [13] -->
and Vehicle Density 𝑛 (lower is better)

<!-- b000187 | prose | pages [13] -->
In the first half of the figure, the increase of 𝐸0 could be explained by the frequent lane changing and acceleration due to a low vehicle density. In the latter half, although vehicles are much less likely to accelerate, notice that traffic flow also falls dramatically, therefore the average energy consumption still increases.

<!-- b000188 | prose | pages [13] -->
 Optimal Maximum Velocity Estimation (Weighted)

<!-- b000189 | prose | pages [13] -->
In this section, we will design a weighted function 𝜙 dependent on the three key variables---traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and average energy consumption 𝐸0. Then we will calculate an optimal speed limit to maximize the value of 𝜙 under light traffic and heavy traffic respectively.

<!-- b000190 | prose | pages [13] -->
We define the weighted function as follows:

<!-- b000191 | prose | pages [13, 14] -->
800) + 𝜔3√1 −(𝛼𝑠𝑎𝑓𝑒 1.2 + 𝜔2(1 −𝐸0 𝑄 3 0.4 )3 𝜙(𝑄, 𝛼𝑠𝑎𝑓𝑒, 𝐸0) = 𝜔1 𝑠. 𝑡.        𝜔1 + 𝜔2 + 𝜔3 = 1

<!-- b000192 | furniture | pages [14] -->
Page 14 of 40

<!-- b000193 | furniture | pages [14] -->
Team#29911

<!-- b000195 | prose | pages [14] -->
where  𝜔1, 𝜔2, 𝜔3 are weight coefficient.  We base on the following four rules to design our function:  When 𝜙 reaches its peak value, we define the corresponding 𝑉𝑚𝑎𝑥 to be the optimal maximum velocity;  Since the three variables 𝑄, 𝛼𝑠𝑎𝑓𝑒, 𝐸0 are independent of each other, 𝜙 should be expressed in the form of simple sums.  𝑄 and 𝐸0 should appear in linear forms in 𝜙;  The value of 𝜙 should drop sharply when the safety index is rather high Hence 𝛼𝑠𝑎𝑓𝑒 should appear in the form of an upward-convex-function in 𝜙.

<!-- b000196 | prose | pages [14] -->
Now under light traffic where 𝑛= 0.1 and heavy traffic where 𝑛= 0.2 𝑙𝑖𝑔ℎ𝑡 ℎ𝑒𝑎𝑣𝑦. We plot respectively we can calculate the corresponding 𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙 and 𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙 𝜙 against different values of 𝑉𝑚𝑎𝑥 under the condition (𝜔1 = 0.5, 𝜔2 = 0.2, 𝜔3 = 0.3) in Figure 6 and Figure 7.

<!-- b000197 | prose | pages [14, 15] -->
             Considering the duration of light traffic and heavy traffic in a given time period, we set the ratio 4:1 (light :heavy) to obtain the result for a "mixed- traffic" situation. See in Figure 8.

<!-- b000198 | caption | pages [14] -->
Figure 6. Optimal Maximum Velocity (Light Traffic)

<!-- b000199 | furniture | pages [15] -->
Page 15 of 40

<!-- b000200 | furniture | pages [15] -->
Team#29911

<!-- b000201 | caption | pages [15] -->
Figure 7. Optimal Maximum Velocity (Heavy Traffic)

<!-- b000203 | prose | pages [15] -->
            

<!-- b000204 | caption | pages [15] -->
Figure 8. Optimal Maximum Velocity (combined)

<!-- b000205 | prose | pages [15] -->
As shown in Figure 8, the global maximum value of 𝜙 locates at 𝑉𝑚𝑎𝑥= 5, therefore the optimal maximum velocity 𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙= 5. In other words, when we set the speed limit at 5, we achieve a weighted optimization of traffic flow, safety index and energy consumption.

<!-- b000206 | prose | pages [15] -->
 Analysis of Under-Posted and Over-Posted Speed Limits

<!-- b000207 | prose | pages [15] -->
In the section above, we have calculated the optimal maximum velocity 𝑉𝑜𝑝𝑡𝑖𝑚𝑎𝑙= 5. We will discuss the influence of under-posted and over-posted speed limits in light and heavy traffic respectively.

<!-- b000208 | furniture | pages [16] -->
Page 16 of 40

<!-- b000209 | furniture | pages [16] -->
Team#29911

<!-- b000210 | prose | pages [16] -->
 Light Traffic

<!-- b000211 | prose | pages [16] -->
If a speed limit is over-posted, say, 𝑉𝑚𝑎𝑥= 7, traffic flow, safety index and average energy consumption all increase. In other words, we sacrifice energy and safety for larger traffic flow.

<!-- b000212 | prose | pages [16] -->
If a speed limit is under-posted, say, 𝑉𝑚𝑎𝑥= 3, traffic flow, safety index and average energy consumption all decrease. In other words, we sacrifice traffic flow for lower energy consumption and a safer condition.

<!-- b000213 | prose | pages [16] -->
 Heavy Traffic

<!-- b000214 | prose | pages [16] -->
If a speed limit is over-posted, say, 𝑉𝑚𝑎𝑥= 7, traffic flow will remain almost the same while energy consumption and safety index will rise. This is highly unwelcome.

<!-- b000215 | prose | pages [16] -->
If a speed limit is under-posted, say, 𝑉𝑚𝑎𝑥= 3, situation will be similar to that of light traffic. Still, we will be sacrificing traffic flow for lower energy consumption and a safer condition.

<!-- b000216 | prose | pages [16] -->
 Visualization

<!-- b000217 | prose | pages [16] -->
To make our simulation results more intuitive, we use MATLAB to visualize our simulation. In the figures below, each row signifies the distribution of vehicles with black dots representing vehicles occupation and margin representing empty space. Time increases from bottom to top and vehicles move from left to right. We visualize our simulation at low vehicle density (𝑛= 0.05) and high density (𝑛= 0.2) respectively in Figure 9 and Figure 10. Subfigure on the left represents the left lane and the subfigure on the right represents the right lane.

<!-- b000218 | caption | pages [16] -->
Figure 9. Visualization at Low Density

<!-- b000219 | furniture | pages [17] -->
Page 17 of 40

<!-- b000220 | furniture | pages [17] -->
Team#29911

<!-- b000221 | caption | pages [17] -->
Figure 10. Visualization at High Density

<!-- b000222 | heading | pages [17] -->
3.2 Continuum Modeling for Right-Most Rule

<!-- b000223 | prose | pages [17] -->
Apart from the discrete, microscopic cellular automaton (CA) models we have adopted above, in this section we will establish a continuum, macroscopic model to describe the vehicle flow on the freeway.

<!-- b000224 | heading | pages [17] -->
3.2.1 Model Establishment

<!-- b000225 | prose | pages [17] -->
Our ultimate goal is to make a continuum model for the traffic flow on a double-lane freeway. We start our work from the single-lane situation.  According to [4], we can use partial-derivative equations (PDE) system to describe the traffic flow on a single-lane freeway. There are two variables in the equation system: the average speed of vehicles 𝑢(𝑥, 𝑡) and the density of vehicles 𝜌(𝑥, 𝑡). The PDE system contains two parts: Continuity equation:

<!-- b000226 | prose | pages [17] -->
𝜕𝑢 𝜕𝑡+ 𝜕(𝜌𝑢) = 0 𝜕𝑥

<!-- b000227 | prose | pages [17] -->
Dynamic equation:

<!-- b000228 | prose | pages [17] -->
𝜕𝑢 𝜕𝑡+ 𝑢𝜕𝑢 𝜕𝑥= 𝑢𝑒(𝜌) −𝑢 𝜕𝑢 𝜕𝑥 + 𝑐0 𝑇

<!-- b000229 | prose | pages [17] -->
In the second equation, the right side contains a relaxation term (𝑢𝑒(𝜌) − 𝑢)/𝑇, which reflects the process when a driver tries to adjust his velocity to the equilibrium velocity 𝑢𝑒(𝜌) in the time interval 𝑇 and an anticipation term 𝑐0𝜕𝑢/𝜕𝑥, which represents the process when the driver reacts to the traffic condition ahead with the propagation speed of small disturbance 𝑐0.

<!-- b000230 | furniture | pages [18] -->
Page 18 of 40

<!-- b000231 | furniture | pages [18] -->
Team#29911

<!-- b000232 | prose | pages [18] -->
Now we extend that model to accommodate the double-lane situation to accommodate the "keep-right-except-to-pass" rule. We will establish the equations for the two lanes separately. In order to describe lane-changing between the right (driving) lane and the left (overtaking) lane, we will introduce two variables 𝑆𝑗𝑖 and 𝑆𝑖𝑗, which represent the lane changing rate. In particular, 𝑆𝑗𝑖 denotes the changing rate from lane 𝑖 to lane 𝑗(𝑖, 𝑗∈{1,2}). The overtaking lane is denoted by Lane 1 and the driving lane is denoted by Lane 2. Thus, the net lane change into lane 𝑖 is 𝑆𝑗𝑖 −𝑆𝑖𝑗.

<!-- b000233 | prose | pages [18] -->
Hence the continuity equation could be written as:

<!-- b000234 | prose | pages [18] -->
𝜕𝜌𝑖 𝜕𝑡+ 𝜕(𝜌𝑖𝑢𝑖) = 𝑆𝑗𝑖 −𝑆𝑖𝑗 𝜕𝑥

<!-- b000235 | prose | pages [18] -->
For the dynamic equation, we introduce two constant parameters 𝑟1, 𝑟2 to be the coefficients of 𝑆𝑗𝑖, 𝑆𝑖𝑗. The equation should be:

<!-- b000236 | prose | pages [18] -->
𝜕𝑢𝑖 𝜕𝑢𝑖 𝜕𝑥= 𝑢𝑒𝑖(𝜌𝑖) −𝑢𝑖 𝜕𝑢𝑖 𝜕𝑡+ 𝑢𝑖 + 𝑐0𝑖 𝜕𝑥+ 𝑟1𝑆𝑖𝑗−𝑟2𝑆𝑗𝑖      (𝑖= 1,2) 𝑇𝑖

<!-- b000237 | prose | pages [18] -->
According to [5], we assume:

<!-- b000238 | prose | pages [18] -->
𝜌2 𝑆12 = 𝑎𝑄𝑒1(𝜌̅)𝜌1(1 − 𝜌𝑚 )

<!-- b000239 | prose | pages [18] -->
𝜌1 𝑆21 = 𝑎(1 + 𝑏(𝑄𝑒1(𝜌̅) −𝑄𝑒2(𝜌̅)))𝑄𝑒2(𝜌̅)𝜌2(1 − 𝜌𝑚 )

<!-- b000240 | prose | pages [18] -->
where 𝑄𝑒1 denotes the equilibrium flow 𝑄𝑒1 = 𝜌1𝑢𝑒1(𝜌1) 𝜌̅  denotes the average density of Lane 1 and Lane 2 𝜌̅ = (𝜌1 + 𝜌2)/2 𝜌𝑚 denotes the density in a jam 𝑎, 𝑏 are two constant parameters.

<!-- b000241 | prose | pages [18] -->
Such assumption is reasonable. Firstly, notice that the expression of 𝑆12 and 𝑆21 is not symmetric because of the asymmetricity of the double-lane freeway. Secondly, if Lane 2 is suffering from a traffic jam, then 𝜌2 = 𝜌𝑚; if there are no vehicles in overtaking lane 1,then 𝜌1 = 0. Under both circumstances, we can derive 𝑆12 = 0, which implies that no car can change into the driving lane when it has a traffic jam or when there are no vehicles on the overtaking lane.

<!-- b000242 | heading | pages [18] -->
3.2.2 Model Solution and Analysis

<!-- b000243 | prose | pages [18, 19] -->
Study of Steady State According to theories of PDE, we can obtain a steady state solution of our model by setting the derivative terms to zero. Then we can derive the following two equations:

<!-- b000244 | furniture | pages [19] -->
Page 19 of 40

<!-- b000245 | furniture | pages [19] -->
Team#29911

<!-- b000247 | prose | pages [19] -->
𝑄𝑒1(𝜌̅)𝜌1(1 −𝜌2 ) = (1 + 𝑏(𝑄𝑒1(𝜌̅) −𝑄𝑒2(𝜌̅)))𝑄𝑒2(𝜌̅)𝜌2(1 −𝜌1 ) 𝜌𝑚 𝜌𝑚 𝑢𝑒𝑖(𝜌𝑖) −𝑢𝑖 𝜕𝑢𝑖 + 𝑐0𝑖 𝜕𝑥+ 𝑟1𝑆𝑖𝑗−𝑟2𝑆𝑗𝑖= 0    (𝑖= 1,2) 𝑇𝑖

<!-- b000248 | prose | pages [19] -->
Plugging in 2𝜌̅ = 𝜌1 + 𝜌2, we can derive the expression of 𝑢𝑒1(𝜌) and 𝑢𝑒2(𝜌) from the equations above according to [6]:

<!-- b000249 | prose | pages [19] -->
𝜌 𝜌 𝑢𝑒1(𝜌) = 𝑢𝑓(1 − 𝜌𝑚)4) 𝜌𝑚)/(1 + 𝐸( 𝜌 𝜌 1 𝜌 𝜌𝑚)4)( 𝑢𝑓(1 − 𝜌𝑚)/(1 + 𝐸( 2 + 2𝜌𝑐)     (𝜌< 𝜌𝑐) 𝑢𝑒2(𝜌) = { 𝜌 𝜌 𝜌𝑚)4)                      (𝜌≥𝜌𝑐) 𝑢𝑓(1 − 𝜌𝑚)/(1 + 𝐸(

<!-- b000250 | prose | pages [19] -->
where 𝑢𝑓 denotes the free flow speed and 𝐸 is a constant parameter.

<!-- b000251 | prose | pages [19] -->
Using the relationship given above, we can derive the relationship between 𝑢𝑖 and 𝜌̅. Then we use the definition 𝑞𝑖= 𝜌𝑖𝑢𝑖 to express the flow on each lane with the average density 𝜌̅.

<!-- b000252 | prose | pages [19] -->
According to [7], we assign the following values to the parameters: 𝑇1 = 𝑇2 = 10𝑠, 𝑢𝑓= 30 𝑚/𝑠, 𝑎= 0.01, 𝑏= 5, 𝑐01 = 𝑐02 = 10𝑚/𝑠 𝜌𝑚= 0.14 𝑣𝑒ℎ/𝑚, 𝑟1 = 150𝑚2/𝑠, 𝑟2 = 50𝑚2/𝑠, 𝜌𝑐= 0.05 𝑣𝑒ℎ/𝑚, 𝐸= 100.

<!-- b000253 | prose | pages [19] -->
Since we have established the traffic flow function of average density on both lane, we can plot the relationship as shown in Figure 11.

<!-- b000254 | caption | pages [19] -->
Figure 11. The Relationship of Traffic Flow 𝑄 and Average Density 𝜌̅

<!-- b000255 | prose | pages [19, 20] -->
In Figure 11, we can discover that all three kinds of flows experience a similar changing pattern---when the average density is relatively small, traffic flow experiences a monotonic increase as the density gets larger. After reaching its climax, the flow drops gradually to 0 as the density keeps rising. This changing pattern is identical to the results we have obtained in the discrete model. We can also discover that the overtaking (fast) lane reaches its climax sooner than that of the driving (slow) lane. Due to difference of the maximum velocity, the peak value of fast lane's traffic flow is larger than that of the slow lane. In addition, the curves of fast lane and slow lane almost overlap when 𝜌> 𝜌𝑐= 0.05. The overlapping part of curves actually indicates that the utility rate of both lanes is almost the same when 𝜌 is relatively large.

<!-- b000256 | furniture | pages [20] -->
Page 20 of 40

<!-- b000257 | furniture | pages [20] -->
Team#29911

<!-- b000259 | prose | pages [20] -->
 Study of Numerical Simulation

<!-- b000260 | prose | pages [20] -->
In this section, we mainly study the density function 𝜌𝑖(𝑥, 𝑡)(𝑖= 1, 2) as a solution of the PDE system. In order to simulate the two-lane traffic movement, we assume that 𝐿 = 32.2 𝑘𝑚. The following initial variation of the average density 𝜌ℎ proposed in [8] can be used on either the fast or the slow lane:

<!-- b000261 | prose | pages [20] -->
1 1 𝜌(𝑥, 0) = 𝜌ℎ+ Δ𝜌ℎ[ − ] 4𝑐𝑜𝑠ℎ2(40 𝐿(𝑥−11𝐿 𝑐𝑜𝑠ℎ2(160 𝐿(𝑥−5𝐿 32 )) 16))

<!-- b000262 | prose | pages [20] -->
Then, our model (the PDE system) can be solved by the numerical scheme given in reference [9]. Here we just provide the figures of the solution under three different conditions. (All of these three figures are dynamic traffic images of an asymmetric double-lane system with curve (a) representing the fast lane and curve (b) representing the slow lane.)

<!-- b000263 | prose | pages [20] -->
 At Low Average Density 𝝆̅

<!-- b000264 | prose | pages [20] -->
According to Figure 12, any perturbations on the fast lane or the slow lane will quickly dissipate. Because of the lane-changing tendency, a cluster appeared in the fast lane may cause a small hump in slow lane.

<!-- b000265 | prose | pages [20] -->
On the opposite side, as shown in Figure 13, a cluster in slow lane may quickly dissipate because people trapped by the cluster in slow (driving) lane may choose the fast (overtaking) lane for passing.

<!-- b000266 | furniture | pages [21] -->
Page 21 of 40

<!-- b000267 | furniture | pages [21] -->
Team#29911

<!-- b000268 | caption | pages [21] -->
Figure 12. Low Density(Jam First Appeared on Fast Lane)

<!-- b000269 | caption | pages [21] -->
Figure 13. Low Density(Jam First Appeared on Slow Lane)

<!-- b000270 | prose | pages [21] -->
 At Normal (or Higher) Average Density 𝝆̅

<!-- b000271 | prose | pages [21] -->
As average density continues to rise, free space for vehicles decreases and it becomes less likely for the double-lane system to maintain stability. Correspondingly, serious traffic jams and “stop-and-go” waves become more probable. See in Figure 14.

<!-- b000272 | furniture | pages [22] -->
Page 22 of 40

<!-- b000273 | furniture | pages [22] -->
Team#29911

<!-- b000274 | caption | pages [22] -->
Figure 14. Normal or Higher Density

<!-- b000275 | prose | pages [22] -->
Parameter evaluation of the three figures:

<!-- b000276 | caption | pages [22] -->
Figure 12: 𝜌1 = 0.047𝑣𝑒ℎ/𝑚, 𝜌2 = 0.021 𝑣𝑒ℎ/𝑚, 𝜌ℎ= 0.06 𝑣𝑒ℎ/𝑚;

<!-- b000277 | caption | pages [22] -->
Figure 13: 𝜌1 = 0.047𝑣𝑒ℎ/𝑚, 𝜌2 = 0.021 𝑣𝑒ℎ/𝑚, 𝜌ℎ= 0.06 𝑣𝑒ℎ/𝑚;

<!-- b000278 | caption | pages [22] -->
Figure 14: 𝜌1 = 0.053𝑣𝑒ℎ/𝑚, 𝜌2 = 0.053 𝑣𝑒ℎ/𝑚, 𝜌ℎ= 0.06 𝑣𝑒ℎ/𝑚.

<!-- b000279 | heading | pages [22] -->
3.3 Comparison of Discrete Model and Continuum Model

<!-- b000280 | prose | pages [22] -->
In the discrete (CA) model, we focus on the relationship between traffic flow and vehicle density and obtain the following fact: when density is relatively small, flow rises as density increases; after reaching its peak value, flow then decreases gradually to 0. This coincides with the conclusion derived in the continuum model as shown in Figure 9. More intuitively, the visualization images of both models also convey the same conclusion.

<!-- b000281 | heading | pages [22] -->
3.4 Transferability Analysis of Model in Left-Handed Countries

<!-- b000282 | prose | pages [22] -->
According to our research, the difference between the left-most and right-most tradition is mainly historical. In addition, our model has no partiality for either left orientation or right orientation. In other words, orientation is symmetric in our model. Therefore our model could be transferred in left-handed countries with a single change of orientation.

<!-- b000283 | heading | pages [22] -->
4 Modeling for Alternative Freeway Traffic Rules

<!-- b000284 | prose | pages [22] -->
In this section, we will use similar Monte Carlo method to simulate the traffic flow under two alternative traffic rules: "slow-car-to-right" rule and "free driving & free overtaking" rule.

<!-- b000285 | prose | pages [22] -->
4.1 "Slow-Cars-To-Right" Rule

<!-- b000286 | heading | pages [22] -->
 Model Explanation

<!-- b000287 | prose | pages [22, 23] -->
In the "slow-cars-to-right" rule, the slow cars are designated the right lane, the fast cars are designated among the left and right lanes and no lane changing is allowed. In other words, this is a model of two disconnected single lanes. We run two simulations. First, test a lane with only fast cars and calculate 𝑓 𝑓; then test a lane with 60% fast cars and calculate corresponding 𝑄𝑓, 𝛼𝑠𝑎𝑓𝑒 , 𝐸0 corresponding 𝑄𝑠, 𝛼𝑠𝑎𝑓𝑒 𝑠 ,  𝐸0 𝑠. The overall fast car percentage is 80% matching previous simulations. The final result is a mixture of previous results with weight (1:1).

<!-- b000288 | furniture | pages [23] -->
Page 23 of 40

<!-- b000289 | furniture | pages [23] -->
Team#29911

<!-- b000291 | prose | pages [23] -->
𝑄= 0.5 ∙𝑄𝑓+ 0.5 ∙𝑄𝑠 𝑓 𝑠 𝛼𝑠𝑎𝑓𝑒= 0.5 ∙𝛼𝑠𝑎𝑓𝑒 + 0.5 ∙𝛼𝑠𝑎𝑓𝑒 𝑓+ 0.5 ∙𝐸0 𝑠 𝐸0 = 0.5 ∙𝐸0 Parameter evaluation before the simulation is as follows: The length of the lattices 𝐿= 2048; The vehicle density 𝑛= 0.02, 0.04, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3; The number of the total vehicles 𝑁= 2𝑛𝐿; The duration of the simulation 𝑇= 4096; The deceleration probability 𝑃𝑑= 0.1; The change lane probability 𝑃𝑐= 0.7;

<!-- b000292 | prose | pages [23] -->
𝑓 The maximum velocity of fast car 𝑉𝑚𝑎𝑥 = 5, maximum velocity for slow car = 3. 𝑠 𝑉𝑚𝑎𝑥

<!-- b000293 | heading | pages [23] -->
 Model Solution and Analysis

<!-- b000294 | prose | pages [23] -->
Using computer simulation, we plot traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and average energy consumption 𝐸0 respectively against vehicle density 𝑛. The results will be shown in Section 4.3.

<!-- b000295 | prose | pages [23] -->
4.2 "Free Driving & Free Overtaking" Rule

<!-- b000296 | heading | pages [23] -->
 Model Explanation

<!-- b000297 | prose | pages [23] -->
Under the "free driving & free overtaking" rule, vehicles are free to drive and overtake with no specific requirement. The two lanes are symmetric and the only 𝑓 limitation is the respective maximum velocity 𝑉𝑚𝑎𝑥 and 𝑉𝑚𝑎𝑥 for fast vehicles 𝑠

<!-- b000298 | prose | pages [23] -->
and slow vehicles. Parameters and their evaluation are still the same as in the "slow-cars-to-right" rule.

<!-- b000299 | heading | pages [23] -->
 Model Solution and Analysis

<!-- b000300 | prose | pages [23] -->
Again, we consider the influence of this traffic through measuring of the three key factors---traffic flow 𝑄, safety index 𝛼𝑠𝑎𝑓𝑒 and average energy consumption 𝐸0. Further comparison of the three traffic rules will be shown in the Section 4.3.

<!-- b000301 | furniture | pages [24] -->
Page 24 of 40

<!-- b000302 | furniture | pages [24] -->
Team#29911

<!-- b000303 | heading | pages [24] -->
4.3 Comparison of Different Traffic Rules

<!-- b000304 | prose | pages [24] -->
Same as that in the slow-cars-to-right rule, we will mainly focus on the first half of the figures to analyze the difference of the three rules.

<!-- b000305 | prose | pages [24] -->
 Traffic Flow

<!-- b000306 | prose | pages [24] -->
We plot traffic flow 𝑄 against vehicle density 𝑛 in Figure 15.

<!-- b000307 | caption | pages [24] -->
Figure 15. Traffic Flow under Different Traffic Rules

<!-- b000308 | prose | pages [24] -->
As shown in Figure 15, during light-traffic situation, traffic flow under the "keep-right-except-to-pass" rule and "slow-cars-to-right" rule are larger, traffic flow under the "free driving & free overtaking" is the relatively small.

<!-- b000309 | prose | pages [24] -->
During heavy-traffic situation, flow under three rules tends to be the same, which is easy to understand because the more probable jams make the advantages of the last two traffic rule hard to discern.

<!-- b000310 | prose | pages [24] -->
 Safety Index

<!-- b000311 | prose | pages [24] -->
We plot safety index 𝛼𝑠𝑎𝑓𝑒 against vehicle density 𝑛 in Figure 16.

<!-- b000312 | furniture | pages [25] -->
Page 25 of 40

<!-- b000313 | furniture | pages [25] -->
Team#29911

<!-- b000314 | caption | pages [25] -->
Figure 16. Safety Index under Different Traffic Rules (lower is safer)

<!-- b000315 | prose | pages [25] -->
During light-traffic situation, the condition under the "keep-right-except -to-pass" rule and "slow-cars-to-right" rule is much safer than that under the "free driving & free overtaking" rule.

<!-- b000316 | prose | pages [25] -->
During heavy-traffic situation, same as that of traffic flow, safety index under three traffic rules tend to be the same because vehicle tend to drive at a much lower speed which make the overall condition much safer.   Average Energy Consumption

<!-- b000317 | prose | pages [25] -->
We plot average energy consumption 𝐸0 against vehicle density 𝑛 in

<!-- b000318 | caption | pages [25] -->
Figure 17.

<!-- b000319 | caption | pages [25] -->
Figure 17. Average Energy Consumption under

<!-- b000320 | prose | pages [25, 26] -->
Different Traffic Rules (lower is better) Since a large portion of energy consumption comes from traffic jams, and unstable lane changing easily result in traffic jams, the "free driving & free overtaking" rule will definitely be more energy-costly. Such trend is manifest during light traffic when acceleration is fairly easy.

<!-- b000321 | furniture | pages [26] -->
Page 26 of 40

<!-- b000322 | furniture | pages [26] -->
Team#29911

<!-- b000324 | prose | pages [26] -->
During heavy traffic however, lane changing and acceleration become much more difficult, most of the energy consumption is from the accelerations and decelerations in traffic jams, therefore the average energy consumption under three rules tends to be the same.

<!-- b000325 | prose | pages [26] -->
 Summary & Suggestions

<!-- b000326 | prose | pages [26] -->
From the figures above, we can discover that "free driving & free overtaking" rule is inferior to the "slow-cars-to-right" rule and "keep-right-except-to-pass" rule. This accords with real life situation because most countries adopt a combinational policy of "slow-cars-to-right" and "keep-right-except-to-pass".

<!-- b000327 | prose | pages [26] -->
Meanwhile, it is unrealistic to adopt the "slow-cars-to-right" because total forbidding of lane changing and overtaking is unreasonable. Our suggestion is that maintain the policy of "keep-right-except-to-pass" rule and meanwhile construct separate fast and slow lanes for those freeways frequently suffered from car jams and obstructions.

<!-- b000328 | heading | pages [26] -->
5 Modeling for Intelligent-System Control

<!-- b000329 | prose | pages [26] -->
In this section, we make the general assumption that equipped with an intelligent system. The intelligent system knows about the exact velocity and location of all the vehicles on the freeway and controls them together. We aim to propose a new traffic rule such that the overall traffic flow of the freeway could be even larger.

<!-- b000330 | prose | pages [26] -->
5.1 "Median" Optimization

<!-- b000331 | heading | pages [26] -->
 Model Explanation

<!-- b000332 | prose | pages [26, 27] -->
We now introduce a rule called “median” rule. The basic idea is to let vehicles with higher speed stay on the left lane more, while vehicles with lower speed stay on the right lane, reducing the possibility of fast cars following slow cars. The separation point is the median speed, which is known easily by a system that controls all the vehicles. The advantage of median speed is that it is automatically adjusted according to the current average speed, then exactly demand half of the cars go to the left lane and vice versa. Therefore this rule will not let the left lane and right lane become unbalanced both in light and heavy traffic comparing to the usage of a fixed speed cap.

<!-- b000333 | furniture | pages [27] -->
Page 27 of 40

<!-- b000334 | furniture | pages [27] -->
Team#29911

<!-- b000336 | prose | pages [27] -->
The rule is as stated in Figure 18.

<!-- b000337 | prose | pages [27] -->
Determine the speed of the kth car

<!-- b000338 | prose | pages [27] -->
T V(k)=Vmedian? F

<!-- b000339 | prose | pages [27] -->
Generate a random number V(k)>Vmedian in [0, 1]

<!-- b000340 | prose | pages [27] -->
<0.5 >0.5

<!-- b000341 | prose | pages [27] -->
Apply rule: Stay on left Apply rule: Stay on right lane except blocked, lane except blocked, return to left lane if return to right lane if possible. possible.

<!-- b000342 | prose | pages [27] -->
End

<!-- b000343 | caption | pages [27] -->
Figure 18. "Median" Illustration

<!-- b000344 | heading | pages [27] -->
 Model Solution and Analysis

<!-- b000345 | prose | pages [27] -->
Under the same maximum velocity, we plot traffic flow, safety index and average energy consumption against different vehicle density. See in Figure 19-21.

<!-- b000346 | furniture | pages [28] -->
Page 28 of 40

<!-- b000347 | furniture | pages [28] -->
Team#29911

<!-- b000348 | prose | pages [28] -->
Traffic Flow Q against Vehicle Density n 1.5 Traffic Flow Q 1

<!-- b000349 | prose | pages [28] -->
Equipped 0.5 Not Equipped 0 0 0.1 0.2 0.3 0.4 Vehicle Density n

<!-- b000350 | caption | pages [28] -->
Figure 19. Relationship of Traffic Flow and Vehicle Density

<!-- b000351 | prose | pages [28] -->
Safety Index asafe against Vehicle Density n 0.35 Safety Index asafe 0.3 0.25 0.2 0.15 Equipped 0.1 Not Equipped 0.05 0 0 0.1 0.2 0.3 0.4 Vehicle Density n

<!-- b000352 | caption | pages [28] -->
Figure 20. Relationship of Safety Index

<!-- b000353 | prose | pages [28] -->
and Vehicle Density (lower is safer)

<!-- b000354 | prose | pages [28] -->
Average Energy Consumption E0 against Vehicle Density n 2000 Consumption E0 Average Energy 1500

<!-- b000355 | prose | pages [28] -->
1000 Equipped 500 Not Equipped 0 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 Vehicle Density n

<!-- b000356 | caption | pages [28] -->
Figure 21. Relationship of Average Energy Consumption

<!-- b000357 | prose | pages [28, 29] -->
and Vehicle Density (lower is better) From the above Figures, we can discover that the "median" optimization does perform better in terms of traffic flow, safety condition and energy consumption, even though such optimization is not very dramatic. This also indicates that the current "keep-right-except-to-pass" rule is already a pretty mature one.

<!-- b000358 | furniture | pages [29] -->
Page 29 of 40

<!-- b000359 | furniture | pages [29] -->
Team#29911

<!-- b000361 | heading | pages [29] -->
5.2 Possible Further Improvements

<!-- b000362 | prose | pages [29] -->
The “median” rule is only a simple rule, more advantages of the intelligent systems can be utilized. In the discrete (CA) model, a driver can only change his speed according to the distance of cars closely in front or behind because he doesn't know about the location of other cars and intentions of their drivers. Therefore when he is in a car flow without any gaps as shown in Figure 22, the only thing he can do is stop and wait for the front car to move. That's why we 𝑓 and Δ𝑋𝑜 𝑓. only compare his current velocity 𝑉 with Δ𝑋𝑝

<!-- b000363 | caption | pages [29] -->
Figure 22. Illustration of Online Algorithm

<!-- b000364 | prose | pages [29] -->
But with an intelligent system, it controls all the cars at the same time. Under such circumstances, it can optimize traffic flow by accelerating the three cars together with the same acceleration. This approach is extremely effective in traffic jams.

<!-- b000365 | heading | pages [29] -->
6 Superiority and Weakness

<!-- b000366 | heading | pages [29] -->
6.1 Superiority Analysis

<!-- b000367 | prose | pages [29] -->
By reasonable discretization and Monte Carlo method, CA model properly simulates normal driving and overtaking on real-life double-lane freeways; The solution of the CA model could be presented via various forms and standards, visualization technique makes the result even more intuitive;

<!-- b000368 | furniture | pages [30] -->
Page 30 of 40

<!-- b000369 | furniture | pages [30] -->
Team#29911

<!-- b000370 | prose | pages [30] -->
Our model has robust flexibility, only minor modification could realize simulation under different traffic rules and parameters; By comparing with other traffic rules, we can fully realize the influence of keep-right-except-to-pass rule from various aspects; By designing algorithms under an intelligent system, our model has reference value in terms of future freeway construction;  Our continuum model assigns realistic values to parameters, confirming the results derived from the discrete model from a macroscopic perspective.

<!-- b000371 | heading | pages [30] -->
6.2 Weakness Analysis

<!-- b000372 | prose | pages [30] -->
Due to the restriction of computer simulation, some of our assumptions are highly ideal, such as the length of vehicles and the value of acceleration. The core of our system depends on computer simulation, therefore the calculation of key quantities such as traffic flow and safety index is time-costly.

<!-- b000373 | heading | pages [30] -->
6.3 Future Research

<!-- b000374 | heading | pages [30] -->
6.3.1 Possible Optimization of Discrete Model

<!-- b000375 | prose | pages [30, 31] -->
If technique permits, we strive to make computer simulation as similar as possible to realistic situations. One possible measures is that we can use 1 minute as the basic time unit and assign realistic values to lattice length (such as 0.5km). Since most vehicles travel at velocity between 60 𝑘𝑚/ℎ and 120 𝑘𝑚/ℎ, within one time unit (1 min), a vehicle is expected to pass 2-4 lattices within one minute. For more accurate approximation, vehicle profile should be taken into consideration. For example, limousines, sedans, jeeps are usually small but relatively fast, we can assign them with one-lattice length and larger maximum velocity; trucks, on the other hand, could be assigned with length of multiple lattices and a smaller maximum velocity. Finally, we add a more professional factor in the transportation field---stopping sight distance and its limit. The stopping sight distance is used to measure several secure distances in driving. We can assign an integer to the stopping sight distance, denoted as 𝑑0. When the front gap is 𝑓> 𝑑0), we compare 𝑉+ 1 with larger than the stopping sight distance (Δ𝑋𝑃 𝑓 or Δ𝑋𝑜 𝑓 to determine the vehicle's velocity at next 𝑑0 instead of with Δ𝑋𝑃 time interval. We can further combine weather conditions to evaluate the stopping sight distance. Such model is of great importance in deciding whether to close freeways under severe weather conditions.

<!-- b000376 | furniture | pages [31] -->
Page 31 of 40

<!-- b000377 | furniture | pages [31] -->
Team#29911

<!-- b000379 | heading | pages [31] -->
6.3.2 Possible Optimization of Continuum Model

<!-- b000380 | prose | pages [31] -->
In many countries around the world, the number of freeways are dramatically increasing. We can continue to develop multi-lane(more than two lanes) models. Speed limits could also be incorporated in the continuum model. Construct a systematic theory to analyze the graphic form of 𝜌(𝑥, 𝑡) and look for accurate analytical expressions.

<!-- b000381 | heading | pages [31] -->
7 Conclusion

<!-- b000382 | prose | pages [31] -->
We use a discrete model and a continuum model research upon the influence of "Keep-Right-Except-To-Pass" rule on traffic flow, safety index and average energy consumption respectively. Furthermore, to fully determine the pros and cons of the rule, we continue to build models to analyze two alternative traffic rules---the "Slow-Cars-To-Right" rule and the "Free Driving & Free Overtaking" rule. Finally, we propose two possible rules to optimize traffic flow when equipped with an intelligent system. The results of our models are as follows: “Keep-Right-Except-to-Pass” Rule According to our model, traffic flow and safety index first rise to peak value then decrease to zero with increasing vehicle density, while energy flow keeps rising but with a bating speed. Furthermore, under-posted and over-posted speed limits relative to our calculated optimal maximum velocity have different influences during light and heavy traffic. In addition, our model could be transferred in left-handed countries with a single change of orientation.

<!-- b000383 | prose | pages [31] -->
Alternative Traffic Rules

<!-- b000384 | prose | pages [31] -->
The "Keep-Right-Except-To-Pass" rule and the "Slow-Cars-To-Right" rule are superior (to the "Free Driving & Free Overtaking" rule), a combination of  these two rules will have strengthening effects especially on heavy-traffic freeways.

<!-- b000385 | furniture | pages [32] -->
Page 32 of 40

<!-- b000386 | furniture | pages [32] -->
Team#29911

<!-- b000387 | prose | pages [32] -->
Intelligent System Control

<!-- b000388 | prose | pages [32] -->
An ideal online algorithm is discussed, and a "median" optimization method is simulated and proves to be beneficial to enlarge traffic flow.

<!-- b000389 | heading | pages [32] -->
8 References

<!-- b000390 | references | pages [32] -->
[1] Peilin Li, "Globalization and the 'Left-Most' Policy of Automobiles", Journal of

<!-- b000391 | references | pages [32] -->
Financial Introduction, Vol.8, 2004.

<!-- b000392 | references | pages [32] -->
[2] Chowdhury, D., Wolf, D. E., & Schreckenberg, M. (1997). Particle hopping

<!-- b000393 | references | pages [32] -->
models for two-lane traffic with two kinds of vehicles: Effects of

<!-- b000394 | references | pages [32] -->
lane-changing rules. Physica A: Statistical Mechanics and its Applications,

<!-- b000395 | references | pages [32] -->
235 (3), 417-439.

<!-- b000396 | references | pages [32] -->
[3] Giordano, Frank R. A first course in mathematical modeling. Cengage

<!-- b000397 | references | pages [32] -->
Learning, 2013.

<!-- b000398 | references | pages [32] -->
[4] Haijun Huang · Tieqiao Tang · Ziyou Gao:Continuum modeling for two-lane

<!-- b000399 | references | pages [32] -->
traffic flow, Acta Mech Sinica (2006) 22: 131–137.

<!-- b000400 | references | pages [32] -->
[5] Tang Chang-Fu, Jiang Rui, Wu Qing-Song:Extended speed gradient model for

<!-- b000401 | references | pages [32] -->
traffic flow on two-lane freeways. Chinese Physics, 2007/16(06)

<!-- b000402 | references | pages [32] -->
[6] Lee H Y, Lee H W and Kim D 1999 Phys. Rev. E 59 5101

<!-- b000403 | references | pages [32] -->
[7] Nagel K and Schreckenberg M 1992 J. Phys. I 2 2221

<!-- b000404 | references | pages [32] -->
[8] Kerner B S and Konsh ̈auser P 1993 Phys. Rev. E 48 2335

<!-- b000405 | references | pages [32] -->
[9] Fu C J, Wang B H, Yin C Y and Gao K 2006 Acta Phys.Sin. 55 4032

<!-- b000406 | heading | pages [32] -->
9 Appendix

<!-- b000407 | prose | pages [32] -->
C++ Source Code for Monte Carlo Simulation: gen.h: #ifndef __GEN #define __GEN

<!-- b000408 | prose | pages [32, 33] -->
#include <iostream> #include <cstdio> #include <ctime> #include <cstdlib> #include <vector> #include <cassert> using namespace std; /* #define RATIO 0.3 #define L 512 #define VMAX 7 #define VBASE 2 */ int random(int low, int high){ return (rand()%(high-low+1)+low); } void gen(const char *fpath, int L, double den, int Vmax0, int Vmax1, double Pv){ FILE *fp = fopen(fpath, "w"); int n=den*L; vector<int> a; for (int i = 0; i < L && a.size() < n; i ++) if (R((n-a.size())*1.0/(L-i)) || a.size()+L-i <= n) a.push_back(i); assert(a.size() == n); fprintf(fp, "%d, %d\n", L, n); int v; for (int i = 0; i < n; i ++){ v=R(Pv)?Vmax0:Vmax1; fprintf(fp, "%d, %d, %d\n", a[i], v, random(v/2, v)); } fclose(fp); } #endif // __GEN

<!-- b000409 | furniture | pages [33] -->
Page 33 of 40

<!-- b000410 | furniture | pages [33] -->
Team#29911

<!-- b000412 | prose | pages [33] -->
SaveBMP.h: #ifndef __BMP #define __BMP FILE *SaveBmp(const char* filename,int height,int width){ unsigned int w = ((width+7)/8+3)/4*4; unsigned int size = w*height+0x3E; unsigned short head[]={ 0x4D42,size&0xffff,size>>16,0,0,0x3E,0,0x28, 0,width&0xffff,width>>16,height&0xffff,height>>16,1,1,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0xffff, 0x00ff }; FILE* fp=fopen(filename,"wb"); if(!fp)return NULL; fwrite(head,1,sizeof(head),fp); return fp; } #endif

<!-- b000413 | prose | pages [33, 34] -->
lane.h: #ifndef __LANE #define __LANE

<!-- b000414 | furniture | pages [34] -->
Page 34 of 40

<!-- b000415 | furniture | pages [34] -->
Team#29911

<!-- b000417 | prose | pages [34] -->
#include <iostream> #include <cstdio> #include <vector> #include <cmath> #include <cassert> #include <cstdlib> #include <ctime> #include <algorithm> #include <cstring>

<!-- b000418 | prose | pages [34] -->
#define out(x) cout<<(#x)<<"="<<x<<endl;

<!-- b000419 | prose | pages [34] -->
using namespace std;

<!-- b000420 | prose | pages [34] -->
int L, T = 2048, VISUALIZE = 0, TOT = 5; double Pd = 0.2, Pc = 0.6, Pv = 0.8; int Voff = 2, RULE = 0, Vmax0 = 4, Vmax1 = 3; double ECost = 0; double AlphaSafety=0;

<!-- b000421 | prose | pages [34, 35, 36] -->
bool R(const double &P){ return rand()<RAND_MAX*P; } struct car{ int x, v, vmax; car(int x, int v, int vmax):x(x), v(v), vmax(vmax){} car(){} bool operator<(const car &rhs) const { return x < rhs.x; } }; #define fn(i) ((i)>=n?(i)-n:((i)<0?(i)+n:(i))) #define fm(i) ((i)>=m?(i)-m:((i)<0?(i)+m:(i))) #define fL(x) ((x)>=L?(x)-L:((x)<0?(x)+L:(x))) #define takemin(x, y) x=(x)<(y)?(x):(y) unsigned char buf[10000]; struct lane{ vector<car> c; int cnt[7]; int tot() const { int tot=0; for(int i=0; i<7; i++) tot+=cnt[i]; return tot; } car &operator[](int i){return c[i];} lane(const char *fpath){ memset(cnt, 0, sizeof cnt); FILE *fp = fopen(fpath, "r"); int n, t; fscanf(fp, "%d, %d, %d ", &L, &n, &t); c.resize(n); for(int i=0; i<n; i++){ fscanf(fp, "%d, %d, %d ", &c[i].x, &c[i].vmax, &c[i].v); assert(c[i].vmax >= c[i].v); cnt[c[i].v]++; } fclose(fp); } lane(){} bool OK() const { for(int i=0; i<c.size(); i++) if(c[i].x<0 || c[i].x>=L)return false; for(int i=0; i+1<c.size(); i++) if(c[i].x >= c[i+1].x)return false; if (tot() != c.size()) return false; return true; } int size() const { return c.size(); } int advance(vector<car> &t){ int n; t.resize(n = c.size()); if(n==0)return 0; for(int i=0; i<c.size(); i++){ int j=fn(i+1); t[i]=c[i]; if (t[i].v < t[i].vmax) t[i].v++; int DXf = fL(c[j].x-c[i].x-1); if (t[i].v > DXf) t[i].v = DXf; if (t[i].v > 0 && R(Pd)) t[i].v--; t[i].x = fL(t[i].x + t[i].v); if (t[i].v > c[i].v) ECost += t[i].v+c[i].v; } if(t[n-1].x<t[0].x){ for(int i=1; i<n; i++) c[i]=t[i-1]; c[0]=t[n-1]; return 1; } else swap(t, c); memset(cnt, 0, sizeof cnt); for(int i=0; i<c.size(); i++) cnt[c[i].v]++; return 0; } void print(){ for(int i=0; i<c.size(); i++) printf("(%d, %d) ", c[i].x, c[i].v); puts(""); } void pos(FILE *fp){ int ll = ((L+7)/8+3)/4*4*8; unsigned char tmp = 0; for(int i=0, j=0; i<ll; i++){ int b=j<c.size()?(i<c[j].x?1:(i!=c[j++].x)):1; tmp = (b<<7)|(tmp>>1); if(i&0xff)buf[i>>3]=tmp; } fwrite(buf, 1, ll/8, fp); } }; #endif

<!-- b000422 | furniture | pages [35] -->
Page 35 of 40

<!-- b000423 | furniture | pages [35] -->
Team#29911

<!-- b000425 | furniture | pages [36] -->
Page 36 of 40

<!-- b000426 | furniture | pages [36] -->
Team#29911

<!-- b000428 | prose | pages [36] -->
CA.cpp: #include <string> #include "lane.h" #include "gen.h" #include "SaveBMP.h" lane l[2]; int cnt[2]; char VPATH[200]; bool rule_s(lane &l0, lane &l1, int i, int j, int DXf) { int m = l1.size(); if (m==0) return DXf > 1; int k = fm(j-1); if(DXf > 1 && l1[j].x != l0[i].x && //! no parralel car fL(l0[i].x - l1[k].x) > min(l1[k].v+1, l1[k].vmax)) //! no accident in the other lane return 1;

<!-- b000429 | furniture | pages [37] -->
Page 37 of 40

<!-- b000430 | furniture | pages [37] -->
Team#29911

<!-- b000431 | prose | pages [37] -->
return 0; } bool rule0(lane &l0, lane &l1, int i, int j, int DXf) { int m = l1.size(); if (m==0) return DXf < l0[i].vmax; if(DXf < l0[i].vmax){ //! Not enough space in this lane int k = fm(j-1); if(fL(l1[j].x - l0[i].x) > DXf)   //! More space in the other lane if (R(Pc)) return 1; } return 0; } bool rule1(lane &l0, lane &l1, int i, int j, int DXf) { if (l1.size() == 0) return R(Pc); return R(Pc) && (fL(l1[j].x - l0[i].x)> min(l0[i].v+1, DXf)); //! Enough or more space in the other lane } int median(int *c0, int *c1){ int cnt[7]; for(int i=0; i<7; i++) cnt[i] = c0[i] + c1[i]; int tot = 0; for(int i=0; i<7; i++) tot += cnt[i]; tot /= 2; for(int i=0; tot>0 && i<7; i++){ tot -= cnt[i]; if (tot<=0) return i; } return 6; } void chLaneSim(lane &l0, lane &l1, vector<car> &t0, vector<car> &t1, int dir){ int n=l0.size(), m=l1.size(), j=0; t0.clear(); t1.clear(); bool flag = 1; if(!n){ swap(t0, l0.c); return; } for(int i=0; i<n; i++){ int DXf = fL(l0[fn(i+1)].x - l0[i].x); bool chLane = 1;

<!-- b000432 | furniture | pages [38] -->
Page 38 of 40

<!-- b000433 | furniture | pages [38] -->
Team#29911

<!-- b000434 | prose | pages [38, 39] -->
for(; flag && j<m && l1[j].x<l0[i].x; j++); if (j==m) flag=j=0; chLane = chLane && rule_s(l0, l1, i, j, DXf); if (RULE == 16) chLane = 0; int rule, Vmedian = median(l0.cnt, l1.cnt); bool ff = l0[i].v>Vmedian ? 1 : (l0[i].v==Vmedian?R(0.5):0); rule = (dir<<1) + ((RULE&32) ? ff : (l0[i].vmax==Vmax0)); //! 0: l->r slow, 1: l->r fast rule = (RULE>>rule) & 1;                    //! 2: r->l slow, 3: r->l fast switch(rule){                               //! two_car: 1001=9, sym: 0000, sym_two_lane: 1100=12 case 0: chLane = chLane && rule0(l0, l1, i, j, DXf); break; case 1: chLane = chLane && rule1(l0, l1, i, j, DXf); break; default: break; } if(chLane)t1.push_back(l0[i]); else t0.push_back(l0[i]); } } void sim(lane &l0, lane &l1){ vector<car> t00, t01, t10, t11; chLaneSim(l0, l1, t00, t01, 0); chLaneSim(l1, l0, t11, t10, 1); vector<car> t0, t1; t0.resize(t00.size() + t10.size()); t1.resize(t01.size() + t11.size()); merge(t00.begin(), t00.end(), t10.begin(), t10.end(), t0.begin()); merge(t01.begin(), t01.end(), t11.begin(), t11.end(), t1.begin()); swap(t0, l0.c); swap(t1, l1.c); cnt[0] += l0.advance(t0); cnt[1] += l1.advance(t1); } double func(int dx, int v){ if(v==0)return 0; else return exp(-dx/v); } double cal_safety(lane &l){ double res=0; if(l.size()==0)return 0; for(int i=0; i+1<l.size(); i++) res += func(l[i+1].x-l[i].x, l[i].v); res += func(l[0].x-l.c.back().x+L, l.c.back().v); return res; } void gao() { l[0] = lane("lane0.csv"); l[1] = lane("lane1.csv"); FILE *fout0, *fout1; if(VISUALIZE){ fout0 = SaveBmp((string(VPATH)+"0.bmp").c_str(), T, L); fout1 = SaveBmp((string(VPATH)+"1.bmp").c_str(), T, L); } int t; if(VISUALIZE) t=0; else t=T/5; while (t--) sim(l[0], l[1]); t = T; cnt[0] = cnt[1] = 0; AlphaSafety = 0; ECost = 0; while (t--) { sim(l[0], l[1]); l[0].OK(); l[1].OK(); if(VISUALIZE){ l[0].pos(fout0); l[1].pos(fout1); } AlphaSafety+=cal_safety(l[0])+cal_safety(l[1]); } AlphaSafety/=l[0].size()+l[1].size(); AlphaSafety/=T; //printf("Q=%.5lf AlphaS=%.5lf\n", cnt/2.0/T, AlphaSafety); if(VISUALIZE){ fclose(fout0); fclose(fout1); } } pair<double, double> stat(vector<double> &a){ assert(a.size()>=2); double mean=0; for(int i=0; i<a.size(); i++) mean+=a[i]; mean/=a.size(); double s=0; for(int i=0; i<a.size(); i++) s+=(a[i]-mean)*(a[i]-mean); s/=a.size()-1; s=sqrt(s); return make_pair(mean, s);

<!-- b000435 | furniture | pages [39] -->
Page 39 of 40

<!-- b000436 | furniture | pages [39] -->
Team#29911

<!-- b000438 | furniture | pages [40] -->
Page 40 of 40

<!-- b000439 | furniture | pages [40] -->
Team#29911

<!-- b000440 | prose | pages [40] -->
} int main() { srand(time(0)); FILE *fin = fopen("coef.prn", "r"); FILE *fout = fopen("log.csv", "a"); if (fin == NULL || fout == NULL) return -1; int sum=0; double den=0; fgets((char *)buf, 10000, fin); while(1){ if(fscanf(fin, "%d %d %lf %lf %lf %lf %d %d %d %d %s", &L, &T, &den, &Pd, &Pc, &Pv, &Vmax0, &Vmax1, &VISUALIZE, &RULE, VPATH)!=11){ break; } fprintf(fout, "%d, %d, %lf, %lf, %lf, %lf, %d, %d, %d, ", L,  T,  den, Pd,  Pc, Pv, Vmax0, Vmax1, RULE); vector<double> q[2], AlphaS, EC; int REP = VISUALIZE?2:20; for(int i=0; i<REP; i++){ gen("lane0.csv", L, den, Vmax0, Vmax1, Pv); gen("lane1.csv", L, den, Vmax0, Vmax1, Pv); gao(); q[0].push_back(cnt[0]*1.0/T); q[1].push_back(cnt[1]*1.0/T); AlphaS.push_back(AlphaSafety); ECost /= cnt[0]+cnt[1]; EC.push_back(ECost); printf("%d/%d RULE=%d Den=%.3lf Q0=%.3lf Q1=%.3lf AS=%.3lf EC=%.3lf\n", i+1, REP, RULE, den, q[0].back(), q[1].back(), AlphaS.back(), EC.back()); } pair<double, double> t0 = stat(q[0]), t1 = stat(q[1]), t2 = stat(AlphaS), t3 = stat(EC); fprintf(fout, "%.5lf, %.5lf, %.5lf, %.5lf, %.5lf, %.5lf, %.5lf, %.5lf\n", t0.first, t0.second, t1.first, t1.second, t2.first, t2.second, t3.first, t3.second); } fclose(fout); fclose(fin); }
