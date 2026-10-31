# P-A-2014-25142-c5c79dc7

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only 25142 T1 ________________ F1 ________________ T2 ________________ F2 ________________ Problem Chosen T3 ________________ F3 ________________

<!-- b000003 | front_matter | pages [1] -->
A

<!-- b000004 | front_matter | pages [1] -->
T4 ________________ F4 ________________

<!-- b000005 | front_matter | pages [1] -->
2014

<!-- b000006 | front_matter | pages [1] -->
Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000007 | title | pages [1] -->
Freeway Traffic Model Based on Cellular

<!-- b000008 | title | pages [1] -->
Automata and Monte-Carlo Method

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Based on Cellular Automata and Monte-Carlo method, we build a model to discuss the influence of the “Keep right except to pass” rule. First we break down the process of vehicle movement and establish corresponding sub-models, inflow model for car-generation, vehicle-following model for one vehicle following another, and overtaking model for one vehicle passing another.

<!-- b000011 | prose | pages [1] -->
Then we design rules to simulate the movement of vehicles in sub-models. We further discuss rules for our model to adapt to the keep-right situation, the unrestricted situation, and the situation where transportation is controlled by intelligent system. We also design a formula to evaluate the danger index of the road.

<!-- b000012 | prose | pages [1] -->
We simulate the traffic on two-lane freeway (two lanes per direction, four lanes in total), and three-lane freeway (three lanes per direction, six lanes in total) via computer and analyze the data. We record the average velocity, overtaking rate, road density and danger index and assess the performance of the keep-right rule by comparison with the unrestricted rule.  We vary the upper speed limitations to analyze the sensitivity of the model and see the impacts of different upper speed limits. Left-hand traffic is also discussed.

<!-- b000013 | prose | pages [1] -->
Based on our analysis, we come up with a new rule combining the two existing rules (the keep-right rule and the unrestricted rule) for an intelligent system to achieve better performance.

<!-- b000014 | furniture | pages [2] -->
Team # 25142

<!-- b000015 | furniture | pages [2] -->
Page 2 of 34

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1

<!-- b000018 | contents | pages [2] -->
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000019 | contents | pages [2] -->
4

<!-- b000020 | contents | pages [2] -->
1.1

<!-- b000021 | contents | pages [2] -->
Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000022 | contents | pages [2] -->
5

<!-- b000023 | contents | pages [2] -->
1.2

<!-- b000024 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
5

<!-- b000026 | contents | pages [2] -->
2

<!-- b000027 | contents | pages [2] -->
The Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
6

<!-- b000029 | contents | pages [2] -->
2.1

<!-- b000030 | contents | pages [2] -->
Design of Cellular Automata

<!-- b000031 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
6

<!-- b000033 | contents | pages [2] -->
2.2

<!-- b000034 | contents | pages [2] -->
Inﬂow Model

<!-- b000035 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
7

<!-- b000037 | contents | pages [2] -->
2.3

<!-- b000038 | contents | pages [2] -->
Vehicle-Following Model . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
8

<!-- b000040 | contents | pages [2] -->
2.4

<!-- b000041 | contents | pages [2] -->
Overtaking Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
10

<!-- b000043 | contents | pages [2] -->
2.4.1

<!-- b000044 | contents | pages [2] -->
Overtaking Probability . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
10

<!-- b000046 | contents | pages [2] -->
2.4.2

<!-- b000047 | contents | pages [2] -->
Overtaking Condition . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
10

<!-- b000049 | contents | pages [2] -->
2.4.3

<!-- b000050 | contents | pages [2] -->
Danger Index . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
11

<!-- b000052 | contents | pages [2] -->
2.5

<!-- b000053 | contents | pages [2] -->
Two Sets of Rules for CA Model . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
13

<!-- b000055 | contents | pages [2] -->
2.5.1

<!-- b000056 | contents | pages [2] -->
Keep Right Except to Pass Rule . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
13

<!-- b000058 | contents | pages [2] -->
2.5.2

<!-- b000059 | contents | pages [2] -->
Unrestricted Rule . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
14

<!-- b000061 | contents | pages [2] -->
3

<!-- b000062 | contents | pages [2] -->
Supplementary Analysis on the Model . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
14

<!-- b000064 | contents | pages [2] -->
3.1

<!-- b000065 | contents | pages [2] -->
Design of the Acceleration and Deceleration Probability Distribu-

<!-- b000066 | contents | pages [2] -->
tions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
14

<!-- b000068 | contents | pages [2] -->
3.2

<!-- b000069 | contents | pages [2] -->
Design to Avoid Collision

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
14

<!-- b000072 | contents | pages [2] -->
4

<!-- b000073 | contents | pages [2] -->
Model Implementation with Computer . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
15

<!-- b000075 | contents | pages [2] -->
5 Data Analysis and Model Validation

<!-- b000076 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
16

<!-- b000078 | contents | pages [2] -->
5.1

<!-- b000079 | contents | pages [2] -->
Average Velocity

<!-- b000080 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
16

<!-- b000082 | furniture | pages [3] -->
Team # 25142

<!-- b000083 | furniture | pages [3] -->
Page 3 of 34

<!-- b000084 | contents | pages [3] -->
5.2

<!-- b000085 | contents | pages [3] -->
Average Velocity of Fast Cars . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [3] -->
17

<!-- b000087 | contents | pages [3] -->
5.3

<!-- b000088 | contents | pages [3] -->
Density . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [3] -->
18

<!-- b000090 | contents | pages [3] -->
5.4

<!-- b000091 | contents | pages [3] -->
Overtaking Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [3] -->
19

<!-- b000093 | contents | pages [3] -->
5.5

<!-- b000094 | contents | pages [3] -->
Danger Index

<!-- b000095 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [3] -->
19

<!-- b000097 | heading | pages [3] -->
6 Sensitivity Evaluation of the Model under Different Speed Limitations 20

<!-- b000098 | prose | pages [3] -->
7 Driving on the Left . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000099 | prose | pages [3] -->
8 Transportation under Intelligent System . . . . . . . . . . . . . . . . . 21

<!-- b000100 | prose | pages [3] -->
8.1 New Rule for Intelligent System . . . . . . . . . . . . . . . . . . . . 21

<!-- b000101 | prose | pages [3] -->
8.2 Adaption of the Model . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000102 | prose | pages [3] -->
8.3 Result of Intelligent System . . . . . . . . . . . . . . . . . . . . . . 23

<!-- b000103 | prose | pages [3] -->
9 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

<!-- b000104 | heading | pages [3] -->
10 Strengths and Weaknesses

<!-- b000105 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 25

<!-- b000106 | prose | pages [3] -->
10.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

<!-- b000107 | prose | pages [3] -->
10.2 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

<!-- b000108 | prose | pages [3] -->
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

<!-- b000109 | heading | pages [3] -->
Appendices

<!-- b000110 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

<!-- b000111 | furniture | pages [4] -->
Team # 25142

<!-- b000112 | furniture | pages [4] -->
Page 4 of 34

<!-- b000113 | heading | pages [4] -->
1 Introduction

<!-- b000114 | prose | pages [4] -->
Today, about 65% of the world’s population live in countries with right-hand trafﬁc and 35% in countries with left-hand trafﬁc. [worldstandards.eu,2013] In countries with right-hand trafﬁc, like USA and China, regulations request driv- ing and walking keep to the right side of the road. Multi-lane freeways in these countries often employ a rule that requires drivers to drive in the right-most lane unless they are passing another vehicle, in which case they move one lane to the left, pass, and return to their former travel lane. This rule on driving and overtaking is referred to as the ”Keep right except to pass” rule, or the keep- right rule in our paper. The rule in countries with left-hand trafﬁc is exactly mirror symmetrical to the keep-right rule(”Keep left except to pass”). So, what’s the purpose of applying such a rule? Does the keep-right rule ameliorate the freeway trafﬁc condition? Transportation free of the restriction of the keep-right rule (Vehicles can choose either side for overtaking.) is referred to as obeying the unrestricted rule. How does the keep-right rule perform comparing with the unrestricted rule?

<!-- b000115 | prose | pages [4] -->
Based on the Cellular Automata model and the Monte Carlo algorithm, we establish a model to simulate freeway trafﬁc under different conditions (under the keep-right rule or the unrestricted rule, in light trafﬁc or in heavy trafﬁc, 2-lane or 3-lane per direction). Our model is divided into 3 sub-models the in- ﬂow model, the vehicle-following model and the overtaking model. The inﬂow model employs the Poisson probability distribution for the simulation of the vehicle-generation process. The vehicle-following model introduces a special probability distribution model which makes the simulation of the process of a car following another more realistic. The overtaking model simulates the over- taking behavior and deﬁnes the danger index to evaluate the safety risk of a certain freeway. We also build an extended model for transportation under the control of an intelligent system.

<!-- b000116 | prose | pages [4] -->
We implement the model in MATLAB, and obtain sufﬁcient data. We test the average velocity, the density, the overtaking rate and the danger index, analyze their properties and assess the performance of the keep-right rule by comparison with the unrestricted rule. In addition, we analyze the sensitivity of our model under different speed limits. It turns out that our model is robust.

<!-- b000117 | prose | pages [4] -->
Then we come to our conclusions which consist with common sense. We also put forward a new rule for transportation under the control of an intelligent system.

<!-- b000118 | furniture | pages [5] -->
Team # 25142

<!-- b000119 | furniture | pages [5] -->
Page 5 of 34

<!-- b000120 | caption | pages [5] -->
Table 1: Notation

<!-- b000121 | prose | pages [5] -->
Symbol Meaning

<!-- b000122 | prose | pages [5] -->
V current velocity of the vehicle Vm maximum velocity of the vehicle Vl the upper speed limit of the freeway V0 the velocity before overtaking V1 the velocity in the overtaking process G the distance between a vehicle and the vehicle ahead of it Gs the minimum gap required for safety consideration G0 the minimum gap after the vehicle stops Tr PIEV time(human reaction time) Po the overtaking probability Pa the acceleration probability Pb the deceleration probability f the frictional force when braking d danger index in one overtaking event D danger index of the road system a the acceleration during overtaking ap the component parallel to the lane of acceleration during overtaking ad the available deceleration

<!-- b000123 | heading | pages [5] -->
1.1 Terminology

<!-- b000124 | prose | pages [5] -->
• Two-lane road: Two lanes on right-half of the road, four lanes in total.

<!-- b000125 | prose | pages [5] -->
• Three-lane road: Three lanes on right-half of the road, six lanes in total.

<!-- b000126 | prose | pages [5] -->
• Danger index: An index designed in our paper to evaluate the danger of the road system.

<!-- b000127 | prose | pages [5] -->
• Minimum safety gap: The distance between two vehicles that deemed safe enough in our model.

<!-- b000128 | prose | pages [5] -->
• Keep-right rule:Keep right except to pass rule.

<!-- b000129 | prose | pages [5] -->
• Unrestricted rule:Vehicles are not restricted and can overtake others from either side.

<!-- b000130 | prose | pages [5] -->
• Free-driving style:When there is no vehicles nearby, drivers will not accel- erate or decelerate deliberately,but the speed will still ﬂuctuate slightly.

<!-- b000131 | heading | pages [5] -->
1.2 Assumptions

<!-- b000132 | prose | pages [5] -->
• The road is straight and there is no bypass.

<!-- b000133 | furniture | pages [6] -->
Team # 25142

<!-- b000134 | furniture | pages [6] -->
Page 6 of 34

<!-- b000135 | prose | pages [6] -->
• The width of one lane is only enough for one vehicle.

<!-- b000136 | prose | pages [6] -->
• All vehicles have the same volume.

<!-- b000137 | prose | pages [6] -->
• There are only two kinds of vehicles on the road(fast one and slow one).

<!-- b000138 | prose | pages [6] -->
• The environment and climate are good for driving.

<!-- b000139 | prose | pages [6] -->
• Driving on the right is the norm.

<!-- b000140 | prose | pages [6] -->
• Pedestrians are ignored.

<!-- b000141 | heading | pages [6] -->
2 The Models

<!-- b000142 | heading | pages [6] -->
2.1 Design of Cellular Automata

<!-- b000143 | prose | pages [6] -->
Large quantities of former trafﬁc simulations [Wagner P et al.2005] based on Cellular Automata (CA) indicate that CA model is a feasible and effective method to emulate trafﬁc ﬂow. Space, time and status are all discrete in Cellu- lar Automata. For example, the model divides the road into small rectangular cells, and time is divided into small units. This feature predigests the simulation process signiﬁcantly. Besides, the status of a cell is controlled by its neighboring cells following a set of rules, which is much similar to real-life trafﬁc where a car’s movement largely depends on its neighboring cars’ movement. Therefore, it is rational for us to apply Cellular Automata in solving our problem.

<!-- b000144 | prose | pages [6] -->
In our simulation, we divide each lane into 1000 cells. Each cell is 4 meters long in length and width and has two properties, the current velocity V and the maximum velocity Vm. A cell is empty when V is 0, because a car won’t stop in our crash-free simulation. We consider only one direction of the freeway for simplicity. Thus, a freeway of n lanes is converted into an n*1000 matrix.

<!-- b000145 | prose | pages [6] -->
In our simulation, we employ two kinds of vehicles,faster ones to simulate the cars and slower ones to simulate the trucks.

<!-- b000146 | prose | pages [6] -->
For each lane, the ﬁrst 6 cells are used as car-generation area, trafﬁc ﬂow is observed in the last 10 cells and trafﬁc density is calculated on the basis of the last 500 cells.Our model updates once per second, while the period T = 1s is the average reaction time of a driver.

<!-- b000147 | prose | pages [6] -->
We discuss the basic processes for the CA model:

<!-- b000148 | prose | pages [6] -->
• Inﬂow Process: According to the inﬂow model that we will discuss later, assign vehicles in the vehicle-generation area.

<!-- b000149 | furniture | pages [7] -->
Team # 25142

<!-- b000150 | furniture | pages [7] -->
Page 7 of 34

<!-- b000151 | prose | pages [7] -->
• Acceleration Process: If V < Vm, a vehicle accelerates by ∆V , and the new speed is V ′ = V + ∆V .

<!-- b000152 | prose | pages [7] -->
• Deceleration Process: If the distance between a vehicle and the vehicle ahead of it (Front bumper to front bumper distance, we call it the gap, and the gap is denoted by G and its unit is cell. When there is no vehicle ahead , G is set to +∞.) is no more than V , the vehicle decelerates to V ′ = (G −1)/T.

<!-- b000153 | prose | pages [7] -->
• Moving Process: Vehicles move forward by V ′ ∗T cells only when G > Gs(V ′). ( Gs(V ′) is the minimum gap required for safety consideration, and is to be deﬁned later.)

<!-- b000154 | prose | pages [7] -->
Speciﬁc rules will be set in the inﬂow model, the following model and the overtaking model to simulate trafﬁc under the Keep-Right-Except-To-Pass rule and trafﬁc under no such restriction.

<!-- b000155 | heading | pages [7] -->
2.2 Inﬂow Model

<!-- b000156 | prose | pages [7] -->
The inﬂow model, or the vehicle-generation model, simulates the stochastic arrivals of vehicles at the entrance of the freeway. For each lane, the ﬁrst six cells in the cellular automata are set as vehicle-generation area. We assume that the arrival of each vehicle obeys the binomial probability distribution. Let ts denote the sampling time interval and N denote the total of vehicle arrivals during ts. Then N can be approximated to obey the Poisson probability distribution. Let Pts(N) be the probability of N and we have

<!-- b000157 | prose | pages [7] -->
P ts(N) = λN N!e−λ, N > 0

<!-- b000158 | prose | pages [7] -->
With ts being one second in our implementation, we can assign the expecta- tion of N to a range of values from 0 to 3.6. N being the total of vehicle arrivals in each second, the expectation of N, can effectively reﬂect the trafﬁc condition. The smaller the λ is, the lighter the trafﬁc is; the greater, the heavier. Thus we are able to simulate different trafﬁc conditions, light or heavy, by assigning cor- responding values to λ . After the value of λ is set, we get the stochastic number of vehicles entering the freeway for every second in simulation. Which lane to enter is then randomly assigned.

<!-- b000159 | prose | pages [7] -->
Our model supports two kinds of vehicles of different velocity ranges, the initial speed of all vehicles are set to 20 m/s. Such practice brings simpliﬁcation and doesn’t weaken the result.

<!-- b000160 | furniture | pages [8] -->
Team # 25142

<!-- b000161 | furniture | pages [8] -->
Page 8 of 34

<!-- b000162 | prose | pages [8] -->
That is because the speed of all vehicles tends to converge toward a value controlled by the trafﬁc density and by the distribution of acceleration proba- bility which is to be introduced later. When trafﬁc density is low, vehicles can always accelerate freely to the maximum speed without worrying about colli- sions, so the convergence speed is near the highest speed allowed. When trafﬁc density is high, all the lanes will be ﬁlled with vehicles, and the speed of the trafﬁc ﬂow is decided by the speed of the slowest vehicle on the lane, so the con- vergence speed is near the lower speed limit. The preliminary analysis on the convergence speed will be justiﬁed by later implementation of the model.

<!-- b000163 | prose | pages [8] -->
The utilization of the Poisson probability distribution makes our inﬂow mod- el close to reality and practical. Because of the convergence tendency, the same initial speed policy can yield simpliﬁcation without harm to the simulation.

<!-- b000164 | heading | pages [8] -->
2.3 Vehicle-Following Model

<!-- b000165 | prose | pages [8] -->
The Federal Highway Administration of the United States Department of Transportation deﬁnes, in its Manual on Uniform Trafﬁc Control Devices, deﬁne driver’s reaction time as PIEV time. PIEV time consists of four parts:

<!-- b000166 | prose | pages [8] -->
• Perception process: A driver perceives the change in driving environment.

<!-- b000167 | prose | pages [8] -->
• Intellection process: The driver analyzes the information about the change.

<!-- b000168 | prose | pages [8] -->
• Evaluation process: The driver determines driving behavior based on his analysis.

<!-- b000169 | prose | pages [8] -->
• Volition process: The driver executes the driving behavior.

<!-- b000170 | prose | pages [8] -->
We apply the PIEV process in our vehicle-following model and overtaking model. In every time cycle, we ﬁrst obtain the velocity and position of each vehicle, calculate the gap, and then determine the driving behavior (whether to continue following or to change lane for overtaking). According to driving behavior, compute the acceleration and update the speed and position.

<!-- b000171 | prose | pages [8] -->
Decision on driving behavior based primarily on the current gap. If the gap G is safe enough, acceleration is feasible; otherwise, the vehicle should slow down. Here, we deﬁne the minimum safe gap Gs to be Tr ∗V . (Tr stands for the PIEV time, and V is the current velocity.)

<!-- b000172 | prose | pages [8] -->
We assume that decisions on driving behavior follow certain principles:

<!-- b000173 | furniture | pages [9] -->
Team # 25142

<!-- b000174 | furniture | pages [9] -->
Page 9 of 34

<!-- b000175 | prose | pages [9] -->
• When G > Gs, the vehicle tends to accelerate (Later we will introduce a probability model to simulate the tendency.), until achieving the freeway speed limit or its maximum possible velocity;

<!-- b000176 | prose | pages [9] -->
• When G < Gs, whether to overtake or to follow is determined by the over- taking probability Po and the overtaking conditions (Po and overtaking conditions are to be discussed in the overtaking model).

<!-- b000177 | prose | pages [9] -->
When following, a vehicle can accelerate, decelerate or keep the original speed. We introduce two parameters [SUN yue 2005], the acceleration proba- bility Pa and deceleration probability Pb. The higher the speed, the smaller the Pa and the greater the Pb. Vl represents the higher speed limit of the freeway, and Vmax is the maximum speed the vehicle can reach. This probability model takes into account the fact that speeding can’t be ignored. When V > Vl, Pa gets even smaller and Pb gets even bigger, which makes it possible for speeding but the possibility is small. We use a stochastic variable R for implementation:

<!-- b000178 | prose | pages [9] -->
• If R < Pb, the vehicle decelerates;

<!-- b000179 | prose | pages [9] -->
• If R > 1 −Pa, the vehicle accelerates;

<!-- b000180 | prose | pages [9] -->
• Otherwise, the vehicle maintains the current speed.

<!-- b000181 | prose | pages [9] -->
Based on the probability model, we create several rules for the Cellular Au- tomata:( The maximum possible speed of vehicle i is Vmax , the current gap is G, the minimum safe gap is Gs and its velocity is denoted as V , Pa and Pb are functions of velocity V , and Pa + Pb ≤1.)

<!-- b000182 | prose | pages [9] -->
• Free driving rule: If G ≥Gs,

<!-- b000183 | prose | pages [9] -->
 min(Vmax, V + 1), with probability Pa;  V ′ = max(Vmin, V −1), with probability Pb;

<!-- b000184 | prose | pages [9] -->
V, others. 

<!-- b000185 | prose | pages [9] -->
• Safe deceleration rule: If G < Gs but won’t crash if moving forward,

<!-- b000186 | prose | pages [9] -->
V ′ = max(Vmin, V −1)

<!-- b000187 | prose | pages [9] -->
Vmin is under-posted the lower speed limit

<!-- b000188 | prose | pages [9] -->
• Crash-free rule: If moving forward causes crash, stop behind the former vehicle.

<!-- b000189 | prose | pages [9] -->
The values of Pa and Pb are listed in table 2 for fast cars, table 3 for slow ones.

<!-- b000190 | furniture | pages [10] -->
Team # 25142

<!-- b000191 | furniture | pages [10] -->
Page 10 of 34

<!-- b000192 | caption | pages [10] -->
Table 2: Acceleration and Deceleration Probability for Fast Vehicles

<!-- b000193 | prose | pages [10] -->
V/cell · s−1 3 4 5 6 7 8

<!-- b000194 | prose | pages [10] -->
pa 1 0.8 0.7 0.5 0.3 0 pb 0 0.1 0.2 0.3 0.4 0.8

<!-- b000195 | caption | pages [10] -->
Table 3: Acceleration and Deceleration Probability for Slow Vehicles

<!-- b000196 | prose | pages [10] -->
V/cell · s−1 3 4 5 6

<!-- b000197 | prose | pages [10] -->
pa 1 0.7 0.4 0 pb 0 0.2 0.4 0.8

<!-- b000198 | heading | pages [10] -->
2.4 Overtaking Model

<!-- b000199 | heading | pages [10] -->
2.4.1 Overtaking Probability

<!-- b000200 | prose | pages [10] -->
The driver will decide wether to overtake another car with the probability Po. Probability Po depends on the vehicle A and the vehicle B ahead. Let Vmax1 be the velocity of vehicle A, and Vmax2 be the velocity of vehicle B. The probability Po satisﬁes:

<!-- b000201 | prose | pages [10] -->
 1 −0.9 · eVmax 2−Vmax 1 , if Vmax2 < Vmax1 Po = if Vmax2 ≥Vmax1 0.1 ,

<!-- b000202 | prose | pages [10] -->
It is rational to assume that the larger the difference in velocity, the more like- ly the vehicle is to accelerate. The probability distribution reﬂects the tendency well.

<!-- b000203 | heading | pages [10] -->
2.4.2 Overtaking Condition

<!-- b000204 | prose | pages [10] -->
A driver can’t overtake as he pleases. Overtaking can be sometimes danger- ous, and a vehicle should to be able to overtake successfully, i.e. able to return to the former lane, under the Keep right except to pass rule. Thus, restrictions are made on overtaking.

<!-- b000205 | prose | pages [10] -->
Condition of Overtaking:

<!-- b000206 | prose | pages [10] -->
• the gap G′ on the target lane is larger than Gs, and

<!-- b000207 | prose | pages [10] -->
• the velocity of the vehicle is larger than that of the vehicle ahead.

<!-- b000208 | furniture | pages [11] -->
Team # 25142

<!-- b000209 | furniture | pages [11] -->
Page 11 of 34

<!-- b000210 | heading | pages [11] -->
2.4.3 Danger Index

<!-- b000211 | prose | pages [11] -->
Here we redeﬁne the minimum safe gap Gs using a different method to cal- culate the danger index. The theoretical relationship between Gs and the current velocity V is:

<!-- b000212 | prose | pages [11] -->
1 2mV 2 = f(Gs −G0)

<!-- b000213 | prose | pages [11] -->
f is the frictional force when braking; G0 is the minimum gap after the vehicle stops.

<!-- b000214 | prose | pages [11] -->
Considering normal driving speed is under 200 km / h in reality and drivers’ acceptance gap is usually larger than the theoretical safe value, and for the sake of simplicity of computer implementation, we approximate Gs, as a function of present speed V , to be linear to V .

<!-- b000215 | caption | pages [11] -->
Figure 1: Relationship between safe-gap and velocity

<!-- b000216 | prose | pages [11] -->
We set G0 to be 10 meters, and use 0.7 as the friction coefﬁcient. The linear relationship we get is Gs = 10 + 2.8 × V

<!-- b000217 | prose | pages [11, 12] -->
When changing lanes for overtaking, a vehicle spare part of its acceleration to change the direction and the rest acceleration is to cope with the deceleration when facing emergency. So the assessment of safety for lane-changing should be different from that for vehicle-following.

<!-- b000218 | furniture | pages [12] -->
Team # 25142

<!-- b000219 | furniture | pages [12] -->
Page 12 of 34

<!-- b000220 | caption | pages [12] -->
Figure 2: Velocity Analysis

<!-- b000222 | prose | pages [12] -->
As is shown in the ﬁgure 2, V0 denotes the velocity before overtaking, V1 denotes the velocity in the overtaking process, and a is the acceleration during overtaking. Empirically, V1 = V0−4m/s (deceleration during lane-changing pro- cedure for safety concern). Vehicles ﬁnish lane-changing in 1s, and We calculate the component parallel to the lane of a:

<!-- b000223 | prose | pages [12] -->
ap = V0 −V1 · cos(arcsin( 4 )) V1

<!-- b000224 | prose | pages [12] -->
Then, the deceleration available is q V 2 ad = 6.86 −ap = 6.86 −(V0 − 0 −2V0)

<!-- b000225 | prose | pages [12] -->
The values of the available deceleration ad changes slightly as V0 varies, so we set ad to 5.76m/s2 for simplicity. Gs changes to 10 + 3.4V accordingly.

<!-- b000226 | prose | pages [12] -->
We create a function to assess the danger coefﬁcient of a vehicle in unit time:

<!-- b000227 | prose | pages [12] -->
 if Gs −Gr < 0 0 , d = Gs −Gr if Gs −Gr ≥0 ,

<!-- b000228 | prose | pages [12] -->
When Gr ≥Gs, we assume the danger is small enough to neglect, so the danger coefﬁcient is set to 0. When Gr < Gs, we use the difference of Gs and Gr to calculate the danger coefﬁcient. A higher danger coefﬁcient indicates the driving state of the vehicle to be more dangerous.

<!-- b000229 | prose | pages [12] -->
The danger coefﬁcients of vehicle-following are similar in various road and rule conditions, so we consider only the danger coefﬁcients of overtaking in further discussion.

<!-- b000230 | furniture | pages [13] -->
Team # 25142

<!-- b000231 | furniture | pages [13] -->
Page 13 of 34

<!-- b000232 | prose | pages [13] -->
Now we deﬁne the danger index to indicate the risk of a certain road under a certain rule. Let D be the sum of danger coefﬁcients of overtaking events happened in 300s time :

<!-- b000233 | prose | pages [13] -->
300 X A · d D = t=1

<!-- b000234 | prose | pages [13] -->
The danger index is the average D of all the vehicles.A is a parameter deﬁned as:  1 , when passing from left A = 3 , when passing from right

<!-- b000235 | prose | pages [13] -->
According to researches, if a left-hand drive vehicle (the vehicle controls lo- cated on the left hand side) tries to pass from the right side, driver’s sight will get restricted and thus increasing the danger index. We assume that the danger index of passing from the right side is three times higher than that of passing from the left side. So we set A to 1 when passing from the left, and set A to 3 when from the right.

<!-- b000236 | prose | pages [13] -->
The danger index D we introduced here is the basis to evaluate the safety of the road in our model.

<!-- b000237 | heading | pages [13] -->
2.5 Two Sets of Rules for CA Model

<!-- b000238 | heading | pages [13] -->
2.5.1 Keep Right Except to Pass Rule

<!-- b000239 | prose | pages [13] -->
We analyze the performance of the Keep Right except to Pass rule by com- paring the outcomes from the model under this rule and the model without such restriction. Applying this rule demands some rules for the Cellular Automata: (The rules are listed in descending priority, that is, if the ﬁrst rule is satisﬁed, the following ones are to be neglected.)

<!-- b000240 | prose | pages [13] -->
• If the gap G in the right lane is larger than Gs, change to the right lane;

<!-- b000241 | prose | pages [13] -->
• If the current gap G is larger than Gs, apply the free driving rule set in the vehicle-following model;

<!-- b000242 | prose | pages [13] -->
• If the gap G in the left lane is larger than Gs, apply the overtaking model with probability Po, and apply the following model with probability 1−Po.

<!-- b000243 | furniture | pages [14] -->
Team # 25142

<!-- b000244 | furniture | pages [14] -->
Page 14 of 34

<!-- b000245 | heading | pages [14] -->
2.5.2 Unrestricted Rule

<!-- b000246 | prose | pages [14] -->
Likewise, when we implement the model without such restriction, another set of rules is needed: (The rules are listed in descending priority, that is, if the ﬁrst rule is satisﬁed, the following ones are to be neglected.)

<!-- b000247 | prose | pages [14] -->
• If the current gap G is larger than Gs,follow free driving rule employed in vehicle-following model;

<!-- b000248 | prose | pages [14] -->
• If the overtaking conditions are satisﬁed, and the gap G in the left lane is larger than Gs, apply the overtaking model to pass from the left side with probability Po, and apply the vehicle-following model with probability 1− Po;

<!-- b000249 | prose | pages [14] -->
• If the overtaking conditions are satisﬁed, and the gap G in the right lane is larger than Gs, apply the overtaking model to pass from the right side with probability Po, and apply the vehicle-following model with probability 1− Po.

<!-- b000250 | heading | pages [14] -->
3 Supplementary Analysis on the Model

<!-- b000251 | heading | pages [14] -->
3.1 Design of the Acceleration and Deceleration Probability Dis-

<!-- b000252 | prose | pages [14] -->
tributions

<!-- b000253 | prose | pages [14] -->
The design of the acceleration and deceleration probability distributions we introduced in the vehicle-following model simulates the change in velocity dur- ing the driving process. The system can self-adjust the average velocity accord- ing to the density. When the density is small, the average velocity of the trafﬁc ﬂow is close to the average speed of a free-driving car which follows the prob- ability distribution. When the density is large, slow cars on the road decelerate the following cars. In other words, slower cars in the lane determine the average velocity. When the freeway is relatively crowded, the expectation of the slowest speed decreases and thus affects the average velocity of the road.

<!-- b000254 | heading | pages [14] -->
3.2 Design to Avoid Collision

<!-- b000255 | prose | pages [14] -->
While simulating heavy trafﬁc, we design rules to avoid car crashes. Normal- ly, a freeway limits the lower speed, but when a vehicle ﬁnds itself too close to the one ahead, it can brake to avoid collision regardless of the lower speed limit.

<!-- b000256 | furniture | pages [15] -->
Team # 25142

<!-- b000257 | furniture | pages [15] -->
Page 15 of 34

<!-- b000258 | prose | pages [15] -->
When the freeway is crowded, the frequency of deceleration to avoid collision rises, so the average velocity goes below the lower limit of speed.

<!-- b000259 | heading | pages [15] -->
4 Model Implementation with Computer

<!-- b000260 | prose | pages [15] -->
Based on the Cellular Automata model and Monte Carlo algorithm, we im- plement our model successfully via MATLAB. Starting from a simple situation, we ﬁrst simulate a freeway of 2 lanes under the Keep-right rule. Then with a small change to the rules, we have the unrestricted 2-lane-freeway model for comparison. We work on to extend the model to simulate a freeway of 3 lanes and both rule conditions are realized. Moreover, trafﬁc under a keep-left rule, with different speed limits as well as transportation directed by an intelligent system is also emulated. We test these models with different inﬂow rates in or- der to see the inﬂuence of trafﬁc heaviness. Supported by sufﬁcient simulated data, we are able to evaluate accurately the performance of the Keep right ex- cept to pass rule in light and heavy trafﬁc, including the tradeoffs between ﬂow and safety, the average speed, the trafﬁc density and the overtaking frequency. And we further discuss the impact of a keep-left rule and that of an intelligent system. Figure spatiotemporal diagram of vehicles, expectation of inﬂow rate is 0.5 veh/s, the ratio of smaller cars to larger vehicles is 1, three-lane. The di- agram records positions of all the vehicles in every time cycle. Red represents smaller cars and green represents larger vehicles. Every three columns stand for the freeway state of one time cycle.

<!-- b000261 | caption | pages [15] -->
Figure 3: Tempo-Spatial Distribution of Vehicles

<!-- b000262 | furniture | pages [16] -->
Team # 25142

<!-- b000263 | furniture | pages [16] -->
Page 16 of 34

<!-- b000264 | heading | pages [16] -->
5 Data Analysis and Model Validation

<!-- b000265 | heading | pages [16] -->
5.1 Average Velocity

<!-- b000266 | prose | pages [16] -->
Trafﬁc ﬂow is linear to the vehicle-generation rate. We choose the average ve- locity of the vehicle ﬂow to reﬂect the trafﬁc efﬁciency.We analyze the statistics from the two-lane model and the three-lane model, both under the keep-right rule and unrestricted. The relationships between the average speed and the in- ﬂow rate in various conditions are shown in the ﬁgure 4 and ﬁgure 5.

<!-- b000267 | caption | pages [16] -->
Figure 4: Average Velocity under Different

<!-- b000268 | caption | pages [16] -->
Figure 5: Average Velocity under Different

<!-- b000269 | prose | pages [16] -->
Rules(2 lanes) Rules(3 lanes )

<!-- b000270 | prose | pages [16] -->
It’s clear that in the two-lane model, the keep-right rule yields faster average velocity in general.When it comes to the freeway of three lanes (by statistics) or more (by deduction), the keep-right rule doesn’t improve the average velocity . We can see that when the vehicle-generation rate is over 0.75veh/s, the unre- stricted rule outperform the keep-right rule according to the ﬁgure.

<!-- b000271 | prose | pages [16] -->
High inﬂow rate may trigger trafﬁc jam, as we can learn from the ﬁgure. When the inﬂow rate is higher than 1.8veh/s, the average velocity in both mod- els goes below the lower speed limit of the freeway.

<!-- b000272 | prose | pages [16] -->
If the interference of other vehicles is neglected (that is, a vehicle drives on an empty freeway under the free-driving rule), the average speed, or we call it the ideal speed, of slow vehicles is 19.44m/s, and the ideal speed of fast cars is 25.88m/s. (The data come from our MATLAB simulation.) We can see from ﬁgure 4 and 5 that when the inﬂow rate is low, the keep-right rule can almost reach the ideal speed, but the unrestricted rule gives a worse performance.

<!-- b000273 | prose | pages [16, 17] -->
We can conclude from the analysis that on a three-lane freeway, the Keep right except to pass rule promotes the average velocity of vehicle ﬂow in light trafﬁc but makes no improvement on trafﬁc efﬁciency in heavy trafﬁc. However on a two-lane freeway,the Keep right except to pass rule promotes the average velocity of vehicle ﬂow prominently.

<!-- b000274 | furniture | pages [17] -->
Team # 25142

<!-- b000275 | furniture | pages [17] -->
Page 17 of 34

<!-- b000277 | heading | pages [17] -->
5.2 Average Velocity of Fast Cars

<!-- b000278 | prose | pages [17] -->
We calculated the average velocity of faster cars in the three-lane model. We mainly focus on the faster cars to study that to what extent the faster car is blocked by slower vehicles.

<!-- b000279 | caption | pages [17] -->
Figure 6: Average Velocity of Fast cars

<!-- b000280 | prose | pages [17] -->
The general tendency is going down for the following reasons:

<!-- b000281 | prose | pages [17] -->
• Large vehicles (slower) may block the road resulting in the limited speed of small cars.

<!-- b000282 | prose | pages [17] -->
• The more crowded the freeway is, the more will the average speed be af- fected by the slowest vehicle.

<!-- b000283 | prose | pages [17, 18] -->
The velocity goes up when the inﬂow rate is relatively low. That is because at the beginning, the inﬂow rate is so low that cars have almost no companions to overtake, which makes them move in the free-driving style. As inﬂow rate goes high in the lower range (0-0.5veh/s), cars have more chance to overtake so that their acceleration probability rises and their average velocity tends to increase. The tendency of the curve can also be interpreted as that denser trafﬁc (within a certain range) stimulates drivers’ desire of overtaking.

<!-- b000284 | furniture | pages [18] -->
Team # 25142

<!-- b000285 | furniture | pages [18] -->
Page 18 of 34

<!-- b000287 | heading | pages [18] -->
5.3 Density

<!-- b000288 | caption | pages [18] -->
Figure 7: Density of Trafﬁc in Each Lanes(2

<!-- b000289 | caption | pages [18] -->
Figure 8: Density of Trafﬁc in Each Lanes(2

<!-- b000290 | prose | pages [18] -->
lanes, keep-right) lanes, unrestricted)

<!-- b000291 | caption | pages [18] -->
Figure 9: Density of Trafﬁc in Each Lanes(3

<!-- b000292 | caption | pages [18] -->
Figure 10: Density of Trafﬁc in Each Lanes(3

<!-- b000293 | prose | pages [18] -->
lanes, keep-right) lanes, unrestricted)

<!-- b000294 | prose | pages [18] -->
These four charts show the density in each lane under different rules. We ﬁnd that the keep-right rule causes the unbalanced use of the road, which may result in different degrees of wear in the lanes in reality. So the repair for different lanes can be staggered which reduces the harm due to suspension of the lane under repair.

<!-- b000295 | furniture | pages [19] -->
Team # 25142

<!-- b000296 | furniture | pages [19] -->
Page 19 of 34

<!-- b000297 | heading | pages [19] -->
5.4 Overtaking Rate

<!-- b000298 | prose | pages [19] -->
We count the sum of overtaking or passing events happened in the three-lane model in ﬁve minutes.

<!-- b000299 | caption | pages [19] -->
Figure 11: Passing Events With Different Rules(3 lanes, 300s)

<!-- b000300 | prose | pages [19] -->
Under the unrestricted rule, overtaking from the left and from the right are equivalent in priority, so the rates on both sides are approximately the same.

<!-- b000301 | prose | pages [19] -->
Under the keep-right rule, most vehicles drive in the right lane if possible, and vacate the left lane, thus making the overtaking requirements easier to meet and causing the sum of passing events to be much more than that of the unre- stricted left lane. High passing rate keeps faster cars from the limit produced by slower vehicles, which incarnates the quickness of the keep-right rule. Besides, too many passing events on the right lane harm the safety greatly.

<!-- b000302 | prose | pages [19] -->
These data is very important for us to evaluate the danger index of the road system.

<!-- b000303 | heading | pages [19] -->
5.5 Danger Index

<!-- b000304 | prose | pages [19, 20] -->
In light trafﬁc, danger index is low; in heavy trafﬁc, the freeway is crowded, and vehicles move relatively slow, so danger index is also low. Only when the Danger Index under Differen- Danger Index under Differen- t Rules(2 lanes) t Rules(3 lanes)

<!-- b000305 | furniture | pages [20] -->
Team # 25142

<!-- b000306 | furniture | pages [20] -->
Page 20 of 34

<!-- b000307 | caption | pages [20] -->
Figure 12:

<!-- b000308 | caption | pages [20] -->
Figure 13:

<!-- b000310 | prose | pages [20] -->
density appears at a middle level, is the danger index Dm high. We learn from the charts that Dm under the keep-right rule is apparently lower than that of no restriction in both the two-lane and three-lane situations.

<!-- b000311 | heading | pages [20] -->
6 Sensitivity Evaluation of the Model under Differ-

<!-- b000312 | prose | pages [20] -->
ent Speed Limitations

<!-- b000313 | prose | pages [20] -->
We modify the upper speed limit of the freeway, and the result supports that our simulation is robust. We tested the situation where the upper speed limit is changed from 32m/s to 28m/s and to 36m/s.

<!-- b000314 | caption | pages [20] -->
Figure 14: Average Velocity under Different

<!-- b000315 | caption | pages [20] -->
Figure 15: Average Velocity under Different

<!-- b000316 | prose | pages [20] -->
Speed Limits(3 lanes, keep-right) Speed Limits(3 lanes, unrestricted

<!-- b000317 | prose | pages [20, 21] -->
Although speed limits differ, the data from the three models show a similar pattern– the lower the expectation of the vehicle-generation rate, the higher the Danger Index under Differen- Danger Index under Differen- t Speed Limits(3 lanes, keep-right) t Speed Limits(3 lanes, unrestricted)

<!-- b000318 | furniture | pages [21] -->
Team # 25142

<!-- b000319 | furniture | pages [21] -->
Page 21 of 34

<!-- b000320 | caption | pages [21] -->
Figure 16:

<!-- b000321 | caption | pages [21] -->
Figure 17:

<!-- b000323 | prose | pages [21] -->
average speed. This fact indicates that our model is applicable to a wide range of situations.

<!-- b000324 | prose | pages [21] -->
We also calculate the corresponding danger indexes under different speed limitations, and the result consists with common sense. The higher the speed limitation, the more dangerous while driving.

<!-- b000325 | prose | pages [21] -->
The speed limitation won’t make any remarkable changes in our model.

<!-- b000326 | heading | pages [21] -->
7 Driving on the Left

<!-- b000327 | prose | pages [21] -->
We’ve discussed the right-hand trafﬁc and now, let’s consider the left-hand trafﬁc. The situation is exactly mirror symmetrical to that with right-hand trafﬁc. So we require the vehicles used in this model to be right-hand drive and make a switch of the left and the right in our former model. Then the situation of driving on the left is simulated.

<!-- b000328 | heading | pages [21] -->
8 Transportation under Intelligent System

<!-- b000329 | heading | pages [21] -->
8.1 New Rule for Intelligent System

<!-- b000330 | prose | pages [21] -->
After our simulation on computer, We make a new rule for intelligent system to achieve the best performance

<!-- b000331 | prose | pages [21, 22] -->
• When the inﬂow rate is lower than 1.5veh/s, a vehicle should follow the keep-right rule.

<!-- b000332 | furniture | pages [22] -->
Team # 25142

<!-- b000333 | furniture | pages [22] -->
Page 22 of 34

<!-- b000335 | prose | pages [22] -->
• Otherwise, it follows the unrestricted rule.

<!-- b000336 | prose | pages [22] -->
We will explain why we choose such rules in the following part.

<!-- b000337 | heading | pages [22] -->
8.2 Adaption of the Model

<!-- b000338 | prose | pages [22] -->
If the vehicle transportation on the roadway was fully under the control of an intelligent system, some conditions will be changed:

<!-- b000339 | prose | pages [22] -->
• The response time of a driver no longer matters.

<!-- b000340 | prose | pages [22] -->
• A vehicle no longer changes its speed randomly, but makes a change only when necessary.

<!-- b000341 | prose | pages [22] -->
• The danger of changing lanes decreases prominently.

<!-- b000342 | prose | pages [22] -->
• The risk of changing lanes from left to right and from right to left should be the same because in an intelligent system there is no blind zone caused by the driver’s position in a car.

<!-- b000343 | prose | pages [22] -->
• The judgment on whether a car shall pass another is more scientiﬁc and less subjective.

<!-- b000344 | prose | pages [22] -->
The major goal of the intelligent system model is to achieve a high-level of trafﬁc ﬂow. We consider that an intelligent system won’t get tired or distracted as human do, so it doesn’t make mistakes. As a result, danger won’t occur unless the vehicle itself breaks down. In the aspect of safety, we simply regard it as the function of speed.

<!-- b000345 | prose | pages [22] -->
On the basis of former analysis and previous CA model, we establish some additional rules:

<!-- b000346 | prose | pages [22] -->
• Change the response time to 0.1 s, making a smaller minimum safe gap between vehicles.

<!-- b000347 | prose | pages [22] -->
• No longer change speed randomly. Change the speed toward the setting value. We adjust the free-driving speed-changing possibility (pa is possi- bility to accelerate, pb to decelerate )distribution table to:

<!-- b000348 | furniture | pages [23] -->
Team # 25142

<!-- b000349 | furniture | pages [23] -->
Page 23 of 34

<!-- b000350 | caption | pages [23] -->
Table 4: Acceleration and Deceleration Probability for Fast Car

<!-- b000351 | prose | pages [23] -->
V/cell · s−1 3 4 5 6 7 8

<!-- b000352 | prose | pages [23] -->
pa 1 1 1 1 0 0 pb 0 0 0 0 0 1

<!-- b000353 | caption | pages [23] -->
Table 5: Acceleration and Deceleration Probability for Slow Vehicle

<!-- b000354 | prose | pages [23] -->
V/cell · s−1 3 4 5 6

<!-- b000355 | prose | pages [23] -->
pa 1 1 0 0 pb 0 0 0 1

<!-- b000356 | prose | pages [23] -->
• Change the overtaking probability Po from:

<!-- b000357 | prose | pages [23] -->
 1 −0.9 · eVmax 2−Vmax 1 , if Vmax2 < Vmax1 Po = if Vmax2 ≥Vmax1 0.1 ,

<!-- b000358 | prose | pages [23] -->
to:

<!-- b000359 | prose | pages [23] -->
 1 −eVmax 2−Vmax 1 , if Vmax2 < Vmax1 Po = if Vmax2 ≥Vmax1 0 ,

<!-- b000360 | heading | pages [23] -->
8.3 Result of Intelligent System

<!-- b000361 | prose | pages [23] -->
When the inﬂow rate is low, the keep-right rule is better in promoting the average velocity. This is easy to understand. Under the unrestricted rule, slower vehicles won’t change lanes unless for overtaking. Thus they may block the entire road, resulting in a poor performance. But the keep-right rule will provide faster vehicles with more chances for overtaking.

<!-- b000362 | prose | pages [23] -->
When the inﬂow rate becomes high, the density of the road will be unbal- anced under the keep-right rule. The rightmost lane becomes so crowded that the average speed decreases greatly. But vehicles are evenly distributed on the road under the unrestricted rule, so the freeway won’t get that crowded.

<!-- b000363 | heading | pages [23] -->
9 Conclusions

<!-- b000364 | prose | pages [23, 24] -->
Keeping to the right side of the road is an accepted trafﬁc regulation in many countries, and some countries even make it a law. Through the establishment of a reasonable model and the simulation of actual road conditions, we ﬁnd that the Keep right except to pass rule can separate the fast and slow vehicles into dif- ferent lanes to some extent. Fast vehicles will receive fewer constraints from the trafﬁc ﬂow, so that freeway carrying capacity and people’s travel efﬁciency are improved. (Although in our multi-lane simulation, unrestricted rule performs a little better in heavy trafﬁc, but it also brings huge risk compared with keep- right-except-to-pass rule, so we recommend keep-right-expect-to-pass rule.

<!-- b000365 | furniture | pages [24] -->
Team # 25142

<!-- b000366 | furniture | pages [24] -->
Page 24 of 34

<!-- b000367 | caption | pages [24] -->
Figure 18: Average Velocity under Different Rules in an Intelligent System

<!-- b000369 | prose | pages [24] -->
The velocity limit directly inﬂuences trafﬁc security; the higher the speed limit, the more insecure the freeway. But it is irrational to lower the speed limit blindly, resulting in unnecessary loss in trafﬁc efﬁciency. How to balance be- tween velocity and safety asks for further study on the performance of vehicles and accident frequency under different speed limits.

<!-- b000370 | prose | pages [24] -->
In countries like Britain and Japan, vehicles are mostly right-hand drive (ve- hicle controls are located at the right-hand side). Security risks are higher if passing from the left side. Therefore, they formulate a rule exactly mirror sym- metrical to the Keep right except to pass rule, i.e. the Keep left except to pass rule, to lower the incidence of trafﬁc accidents.

<!-- b000371 | prose | pages [24, 25] -->
When we look at the model under the control of an intelligent system, where crashes and collisions won’t happen, the keep-right rule yields higher average velocity in light trafﬁc and the unrestricted rule performs better in heavy trafﬁc. Therefore, we put forward a new driving rule for transportation fully controlled by an intelligent system seeking for best performance: When the inﬂow rate is lower than 1.5veh/s, a vehicle should follow the keep-right rule. Otherwise, it follows the unrestricted rule.

<!-- b000372 | furniture | pages [25] -->
Team # 25142

<!-- b000373 | furniture | pages [25] -->
Page 25 of 34

<!-- b000375 | heading | pages [25] -->
10 Strengths and Weaknesses

<!-- b000376 | prose | pages [25] -->
Like any model,the one present above has its strengths and weaknesses. Some of the major points are presented below.

<!-- b000377 | heading | pages [25] -->
10.1 Strengths

<!-- b000378 | prose | pages [25] -->
• Fully consideration of the mental state of the driver In the vehicle-following model, we fully consider the overtaking psychol- ogy of drivers. The overtaking probability is greater when a fast car is after a slow car, or when the velocity difference is larger.

<!-- b000379 | prose | pages [25] -->
In the free-driving style, the speed of a vehicle will go up or down ac- cording to the unique probability distribution, which simulates the unpre- dictable slight change in speed in real-world driving.

<!-- b000380 | prose | pages [25] -->
• Easy to assess the safety of the system We exclude the possibility of crash in our model, but use the danger index to assess the security of the system. Such practice consists with the low probability of crash in real world.

<!-- b000381 | heading | pages [25] -->
10.2 Weakness

<!-- b000382 | prose | pages [25] -->
• Not accurate enough The change unit (a cell) of the gap and the velocity is relatively big, which may harm the accuracy of the simulation.

<!-- b000383 | prose | pages [25] -->
• Values of some parameters are not very scientiﬁc Some parameters lack real-life data, so we have to estimate based on com- mon sense.

<!-- b000384 | furniture | pages [26] -->
Team # 25142

<!-- b000385 | furniture | pages [26] -->
Page 26 of 34

<!-- b000386 | heading | pages [26] -->
References

<!-- b000387 | references | pages [26] -->
[1] SUN Yue, YU Jia, HU You-qiang ,MO Zhi-feng. Microscopic Trafﬁc Sim-

<!-- b000388 | references | pages [26] -->
ulation Mathematic Model Based on Cellular Automata[J]. Journal of

<!-- b000389 | references | pages [26] -->
Chongqing University(Natural Science Edition), 2005, 28(5): 022

<!-- b000390 | references | pages [26] -->
[2] Kesting A, Treiber M, Helbing D. General lane-changing model MOBIL for

<!-- b000391 | references | pages [26] -->
car-following models[J]. Transportation Research Record: Journal of the

<!-- b000392 | references | pages [26] -->
Transportation Research Board, 2007, 1999(1): 86-94.

<!-- b000393 | references | pages [26] -->
[3] MO Zhi-feng, YU Jia, SUN Yue. Poisson Distribution Based Mathematic

<!-- b000394 | references | pages [26] -->
Model of Producing Vehicles in Microscopic Trafﬁc Simulator[J]. Journal of

<!-- b000395 | references | pages [26] -->
Wuhan University of Technology(Transportation Science & Engineering),

<!-- b000396 | references | pages [26] -->
2003, 27(1): 73-76.

<!-- b000397 | references | pages [26] -->
[4] Wagner P, Nagel K, Wolf D E. Realistic multi-lane trafﬁc rules for cellular

<!-- b000398 | references | pages [26] -->
automata[J]. Physica A: Statistical Mechanics and its Applications, 1997,

<!-- b000399 | references | pages [26] -->
234(3): 687-698.

<!-- b000400 | references | pages [26] -->
[5] Trafﬁc C D. Manual on Uniform Trafﬁc Control Devices[J].

<!-- b000401 | references | pages [26] -->
[6] Why do some countries drive on the left and others on the right ?

<!-- b000402 | references | pages [26] -->
http://www.worldstandards.eu/cars/driving-on-the-left

<!-- b000403 | heading | pages [26] -->
Appendices

<!-- b000404 | prose | pages [26] -->
Here are the simulation programmes we used to implement our model.For different rules listed in our model,the xdeal.m function may be a little different. Here we give the code of the keep-right-except-to-pass rule with 3 lanes simula- tion.

<!-- b000405 | prose | pages [26] -->
Main function:

<!-- b000406 | prose | pages [26] -->
clear all; clear; global road1 Xsumsmall Xsumlarge Xsmallv Xlargev Xsumallcar Vaverage; Xsumsmall=0; Xsumlarge=0; Xsumallcar=0; Xsmallv=0; Xlargev=0; Vaverage=0;

<!-- b000407 | furniture | pages [27] -->
Team # 25142

<!-- b000408 | furniture | pages [27] -->
Page 27 of 34

<!-- b000409 | prose | pages [27] -->
global pass_right_count pass_left_count pass_right_v pass_left_v; pass_right_count=0; pass_left_count=0; pass_right_v=0; pass_left_v=0;

<!-- b000410 | prose | pages [27] -->
out=[]; for q=[0.1,0.3,0.5,0.7,1,1.4,1.8,2.5,3,3.6]

<!-- b000411 | prose | pages [27] -->
Xsumsmall=0; Xsumlarge=0; Xsumallcar=0; Xsmallv=0; Xlargev=0; Vaverage=0; road1=zeros(2,1000,2); out=[out;q,Xmain(q)]; end savefile=’final’; save(savefile);

<!-- b000412 | prose | pages [27] -->
Simulating different inﬂow rates function:

<!-- b000413 | prose | pages [27] -->
function [out]=Xmain(qq)

<!-- b000414 | prose | pages [27] -->
global speedmaxl speedmaxs speedmaxl=7; speedmaxs=9;

<!-- b000415 | prose | pages [27] -->
global pass_right_count pass_left_count pass_right_v pass_left_v; pass_right_count=0; pass_left_count=0; pass_right_v=0; pass_left_v=0;

<!-- b000416 | prose | pages [27] -->
sumdst=0; global road1 Xsumsmall Xsumlarge Xsmallv Xlargev Xsumallcar Vaverage numoflane; numoflane=3; Xsumsmall=0; Xsumlarge=0; Xsumallcar=0; Xsmallv=0; Xlargev=0; Vaverage=0; road1=zeros(numoflane,1000,2); Xdens=0; cdens=0; %h=figure(1); %hold all;

<!-- b000417 | furniture | pages [28] -->
Team # 25142

<!-- b000418 | furniture | pages [28] -->
Page 28 of 34

<!-- b000419 | prose | pages [28] -->
global time; for time=1:700 road1(:,991:1000,:)=zeros(numoflane,10,2); Xbegin(qq,0.5); for xdistance=990:-1:1 for lane=1:numoflane if (road1(lane,xdistance,1)==0) continue; end Xdeal(lane,xdistance);

<!-- b000420 | prose | pages [28] -->
end end %{ for xdistance=990:-1:1 for lane=1:2 Xdraw(lane,xdistance,time); end end %} for xdistance=991:1000 for lane=1:numoflane if road1(lane,xdistance,1)˜=0 Xcount( road1(lane,xdistance,1),road1(lane,xdistance,2),time); end end end if mod(time,50)==0&&time>400 [xd,dst]=Xdensity(); cdens=cdens+1; Xdens=Xdens+xd; sumdst=sumdst+dst; end

<!-- b000421 | prose | pages [28] -->
end Xaveragedens=Xdens/cdens; Xaveragedens=Xaveragedens/(400*4); %cars per m sumdst=(sumdst./cdens)./(400*4); timeall=300; Vaverage=Xsumallcar/Xaveragedens; Vaverage=Vaverage/timeall; out_v=Vaverage; out_d=Xaveragedens; out_ns=Xsumsmall; out_nl=Xsumlarge; out=[out_v,out_d,sumdst’,out_ns,Xsmallv,out_nl,Xlargev,pass_right_count,pass_right_v, savefile=num2str(qq*10); save(savefile); %saveas(gcf,’myfig05.jpg’);

<!-- b000422 | prose | pages [28] -->
Deal with different situations:

<!-- b000423 | furniture | pages [29] -->
Team # 25142

<!-- b000424 | furniture | pages [29] -->
Page 29 of 34

<!-- b000425 | prose | pages [29] -->
function Xdeal( lane,xdistance ) %XDEAL Summary of this function goes here % Detailed explanation goes here global road1 numoflane; v=road1(lane,xdistance,1); f_dis=Xcarahead(lane,xdistance,v); if lane>1 l_dis=Xcarahead(lane-1,xdistance,v); end if lane<numoflane r_dis=Xcarahead(lane+1,xdistance,v); end

<!-- b000426 | prose | pages [29] -->
if lane>1&&lane<numoflane if f_dis==0 [b,y,x]=Xfree(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); elseif l_dis==0 &&Xovertake(lane,xdistance) Xpleft(road1(lane,xdistance,1)); [b,y,x]=Xacc(lane,xdistance); road1(lane-1,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); elseif r_dis==0&&Xovertake(lane,xdistance) Xpright(road1(lane,xdistance,1)); [b,y,x]=Xacc(lane,xdistance); %return to normal road road1(lane+1,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); elseif f_dis==1 [b,y,x]=Xsub(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); else [b,y,x]=Xurgent(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); end elseif lane==1 if f_dis==0 [b,y,x]=Xfree(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2);

<!-- b000427 | prose | pages [29] -->
elseif r_dis==0&&Xovertake(lane,xdistance) Xpright(road1(lane,xdistance,1));

<!-- b000428 | prose | pages [29] -->
[b,y,x]=Xacc(lane,xdistance); %return to normal road road1(lane+1,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); elseif f_dis==1 [b,y,x]=Xsub(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:);

<!-- b000429 | furniture | pages [30] -->
Team # 25142

<!-- b000430 | furniture | pages [30] -->
Page 30 of 34

<!-- b000431 | prose | pages [30] -->
road1(lane,xdistance,:)=zeros(1,1,2); else [b,y,x]=Xurgent(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); end

<!-- b000432 | prose | pages [30] -->
elseif lane==numoflane if f_dis==0 [b,y,x]=Xfree(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); elseif l_dis==0&&Xovertake(lane,xdistance) Xpleft(road1(lane,xdistance,1)); [b,y,x]=Xacc(lane,xdistance); road1(lane-1,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2);

<!-- b000433 | prose | pages [30] -->
elseif f_dis==1 [b,y,x]=Xsub(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); else [b,y,x]=Xurgent(lane,xdistance); road1(lane,x,:)=road1(lane,xdistance,:); road1(lane,xdistance,:)=zeros(1,1,2); end end

<!-- b000434 | prose | pages [30] -->
end

<!-- b000435 | prose | pages [30] -->
Inﬂow:

<!-- b000436 | prose | pages [30] -->
function Xbegin( p,q ) % global speedmaxl speedmaxs

<!-- b000437 | prose | pages [30] -->
prnd=poissrnd(p); if (prnd>16) prnd=16; end global road1; A=road1(:,1:8,1); B=road1(:,1:8,2); S=size(road1); R=randperm(8*S(1)); for i = R(1:prnd) if A(i)==0 if rand<q A(i)=5; B(i)=speedmaxl;

<!-- b000438 | furniture | pages [31] -->
Team # 25142

<!-- b000439 | furniture | pages [31] -->
Page 31 of 34

<!-- b000440 | prose | pages [31] -->
else A(i)=5; B(i)=speedmaxs; end end end road1(:,1:8,1)=A; road1(:,1:8,2)=B; end

<!-- b000441 | prose | pages [31] -->
Acceleration:

<!-- b000442 | prose | pages [31] -->
function [ b,y,x ] = Xacc(lane ,xdistance ) %XACC Summary of this function goes here % Detailed explanation goes here global road1; road1(lane,xdistance,1)=min([road1(lane,xdistance,2),road1(lane,xdistance,1)+1]);

<!-- b000443 | prose | pages [31] -->
b=road1(lane,xdistance,1); y=lane; x=xdistance+road1(lane,xdistance,1);

<!-- b000444 | prose | pages [31] -->
end

<!-- b000445 | prose | pages [31] -->
Deceleration:

<!-- b000446 | prose | pages [31] -->
function [ b,y,x ] = Xsub(lane ,xdistance ) %XSUB Summary of this function goes here % Detailed explanation goes here global road1; global speedmaxl ; road1(lane,xdistance,1)=max([ speedmaxl-3,road1(lane,xdistance,1)-1]);

<!-- b000447 | prose | pages [31] -->
b=road1(lane,xdistance,1);; y=lane; x=xdistance+road1(lane,xdistance,1);

<!-- b000448 | prose | pages [31] -->
end

<!-- b000449 | prose | pages [31] -->
Deal with urgent deceleration:

<!-- b000450 | prose | pages [31] -->
function [ b,y,x] = Xurgent( m,n ) %XURGENT Summary of this function goes here % Detailed explanation goes here global road1; global speedmaxl ; p=find(road1(m,n+1:min(n+30,1000),1));

<!-- b000451 | prose | pages [31] -->
S=size(p); Xr=30;

<!-- b000452 | furniture | pages [32] -->
Team # 25142

<!-- b000453 | furniture | pages [32] -->
Page 32 of 34

<!-- b000454 | prose | pages [32] -->
if S(2)>=1 Xr=p(1); end y=m; %x=Xr+n-1; b=Xr-1; x=n+min([b,road1(m,n,1)-1]); road1(m,n,1)=max([speedmaxl-3,min([b,road1(m,n,1)-1])]);

<!-- b000455 | prose | pages [32] -->
end

<!-- b000456 | prose | pages [32] -->
Judge whether to overtake: function [ output_args ] = Xovertake( m,n ) %XOVERTAKE Summary of this function goes here % Detailed explanation goes here global road1; p=find(road1(m,n+1:min(n+30,1000),1));

<!-- b000457 | prose | pages [32] -->
S=size(p); Xr=30; if S(2)>=1 Xr=p(1); end

<!-- b000458 | prose | pages [32] -->
v_ahead=road1(m,n+Xr,2); v_me=road1(m,n,2); if v_me>v_ahead b=0.9; else b=0.1; end r=rand(); if r<b output_args=1; else output_args=0; end

<!-- b000459 | prose | pages [32] -->
end

<!-- b000460 | prose | pages [32] -->
Free-driving style: function [ b,x,y ] = Xfree( m,n ) % judge if the car is free. A=[1,0.7,0.4,0;0,0.2,0.4,0.8]; B=[1,0.8,0.7,0.5,0.3,0;0,0.1,0.2,0.3,0.4,0.8]; global road1; global speedmaxl ; offset=speedmaxl-4;

<!-- b000461 | prose | pages [32, 33] -->
if (1) b=1; x=m; if road1(m,n,2)==6 r=rand; if r<A(1,road1(m,n,1)-offset) road1(m,n,1)=road1(m,n,1)+1; elseif r>1-A(2,road1(m,n,1)-offset) road1(m,n,1)=road1(m,n,1)-1; end else r=rand; if r<B(1,road1(m,n,1)-offset) road1(m,n,1)=road1(m,n,1)+1; elseif r>1-B(2,road1(m,n,1)-offset) road1(m,n,1)=road1(m,n,1)-1; end end y= n+ road1(m,n,1); else b=0; x=m; y=n; end end

<!-- b000462 | furniture | pages [33] -->
Team # 25142

<!-- b000463 | furniture | pages [33] -->
Page 33 of 34

<!-- b000465 | prose | pages [33] -->
Count the trafﬁc ﬂow: function Xcount(a,b,time ) %XCOUNT Summary of this function goes here % Detailed explanation goes here global Xsumsmall Xsumlarge Xsmallv Xlargev Xsumallcar; global speedmaxl speedmaxs;

<!-- b000466 | prose | pages [33] -->
if (time<400||time>950) return end Xsumallcar=Xsumallcar+1; if b==speedmaxl Xsumlarge=Xsumlarge+1; Xlargev=Xlargev+a;

<!-- b000467 | prose | pages [33] -->
elseif b==speedmaxs Xsumsmall=Xsumsmall+1; Xsmallv=Xsmallv+a; end

<!-- b000468 | prose | pages [33] -->
end

<!-- b000469 | prose | pages [33] -->
Calculate the density:

<!-- b000470 | furniture | pages [34] -->
Team # 25142

<!-- b000471 | furniture | pages [34] -->
Page 34 of 34

<!-- b000472 | prose | pages [34] -->
function [Xd,density]= Xdensity( ) %XDENSITY Summary of this function goes here % Detailed explanation goes here global road1 ; ext=road1(:,500:900,1)>0; Xd=sum(sum(ext),2); density=sum(ext,2); end

<!-- b000473 | prose | pages [34] -->
Calculate overtaking events from left side

<!-- b000474 | prose | pages [34] -->
function Xpleft( v ) global pass_left_count pass_left_v; global time; if time<400 return; end pass_left_count=pass_left_count+1; pass_left_v = pass_left_v +v; end

<!-- b000475 | prose | pages [34] -->
Calculate overtaking events from right side

<!-- b000476 | prose | pages [34] -->
function Xpright(v ) %XPRIGHT Summary of this function goes here % Detailed explanation goes here global pass_right_count pass_right_v ; global time; if time<400 return; end pass_right_count=pass_right_count+1; pass_right_v = pass_right_v +v;

<!-- b000477 | prose | pages [34] -->
end
