# P-C-2017-55278-a011d0e2

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
55278

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
F1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
T3

<!-- b000010 | prose | pages [1] -->
F3

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | title | pages [1] -->
C

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | title | pages [1] -->
The Effects of Self-Driving Cooperating Vehicles on

<!-- b000018 | title | pages [1] -->
Trafﬁc Capacity of Highways

<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
We propose an innovative model based on cellar automata to analyze the effects of self-driving cooperating vehicles on highway trafﬁc capacity. We extend the traditional cellar automata used for trafﬁc analysis to increase the ﬂexibility of our model, so that it can deal with complex dynamics of self-driving vehicles.

<!-- b000021 | prose | pages [1] -->
Based on the extended cellar automata, we ﬁrst model the car generation process using Poisson distributions. This model generates speciﬁed volume of vehicles on a segment of highway. Our car generation model distinguishes the trafﬁc volumes during peak hours and nonpeak hours. Then we model the behaviors of vehicle-following and lane-changing. In this part, we consider the cooperation between self-driving vehicles and interaction between self-driving and human-driven vehicles. Finally, we propose a probability model to analyze the behavior of trafﬁc ﬂow at highway intersections.

<!-- b000022 | prose | pages [1] -->
We verify the feasibility of our model by running various simulations. Our model is tested with different percentages of self-driving cars, different lane numbers and trafﬁc volumes. We ﬁnd that self-driving cars can stabilize the performance of trafﬁc system when the lane number and trafﬁc volume change.

<!-- b000023 | prose | pages [1] -->
Then we apply our model to the data of four highways in the Greater Seattle area. Our results show that the trafﬁc capacity increases with rising percentage of self-driving cooperating vehicles. The average velocity of trafﬁc ﬂow doubles when the percentage increasing from 10% to 50%. And in most cases an equilibria exists after 60%. We also test the effects of dedicated lanes for self-driving cars. We suggest using 70% as a dividing point for whether to use dedicated lanes or not. When the percentage of self-driving vehicles is higher than 70% percent, dedicated lanes can be helpful. We also compare the performance during peak hours with average performance during a whole day, and ﬁnd that self-driving cars signiﬁcantly speed up peak-hour trafﬁc ﬂows.

<!-- b000024 | prose | pages [1] -->
Finally, we analyze the effect of potential error of self-driving system. We ﬁnd that defects of self-driving system can degrade the beneﬁt to trafﬁc capacity. We also do sensitivity analysis of various parameters, including probability of lane-changing and parameters in the vehicle dynamics, to prove the robustness of our model.

<!-- b000025 | keywords | pages [1] -->
Keywords: trafﬁc capacity; cellar automata; self-driving; cooperating vehicles

<!-- b000026 | furniture | pages [2] -->
Team # 55278

<!-- b000027 | furniture | pages [2] -->
Page 1 of 24

<!-- b000028 | prose | pages [2] -->
The Effects of Self-Driving Cooperating Vehicles on

<!-- b000029 | prose | pages [2] -->
Trafﬁc Capacity of Highways

<!-- b000030 | prose | pages [2] -->
January 24, 2017

<!-- b000031 | heading | pages [2] -->
Contents

<!-- b000032 | contents | pages [2] -->
1

<!-- b000033 | heading | pages [2] -->
Introduction

<!-- b000034 | prose | pages [2] -->
3

<!-- b000035 | prose | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 4

<!-- b000036 | prose | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000037 | prose | pages [2] -->
2

<!-- b000038 | heading | pages [2] -->
The Models

<!-- b000039 | prose | pages [2] -->
4

<!-- b000040 | prose | pages [2] -->
4

<!-- b000041 | prose | pages [2] -->
Basic Settings of Cellar Automata . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4

<!-- b000042 | prose | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 5

<!-- b000043 | prose | pages [2] -->
Introducing Acceleration into Cellar Automata . . . . . . . . . . . . 2.2.1 5

<!-- b000044 | prose | pages [2] -->
Attributes of a Cell . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2.2 6

<!-- b000045 | prose | pages [2] -->
Generation Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 6

<!-- b000046 | prose | pages [2] -->
Vehicle-Following Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4 8

<!-- b000047 | prose | pages [2] -->
The follower car is Human Driven . . . . . . . . . . . . . . . . . . . 2.4.1 8

<!-- b000048 | prose | pages [2] -->
Self-Driving Vehicle Follows a Human Driven Vehicle . . . . . . . . 2.4.2 9

<!-- b000049 | prose | pages [2] -->
Following Model For Two Self-Driving Vehicles . . . . . . . . . . . 2.4.3 9

<!-- b000050 | prose | pages [2] -->
Lane-Changing Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.5 10

<!-- b000051 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.6 Intersection Model

<!-- b000052 | prose | pages [2] -->
3

<!-- b000053 | heading | pages [2] -->
Analyzing the Model by Simulation

<!-- b000054 | prose | pages [2] -->
10

<!-- b000055 | prose | pages [2] -->
12

<!-- b000056 | prose | pages [2] -->
Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 12

<!-- b000057 | prose | pages [2] -->
Effects of Percentage of Self-Driving Vehicles . . . . . . . . . . . . . . . . . 3.2 12

<!-- b000058 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 Effects of Lane Number 13

<!-- b000059 | prose | pages [2] -->
Effects of Dedicated Lanes for Self-Driving Cars 3.4 . . . . . . . . . . . . . . .

<!-- b000060 | prose | pages [2] -->
14

<!-- b000061 | prose | pages [2] -->
Effects of Trafﬁc Volume . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.5

<!-- b000062 | prose | pages [2] -->
4 Apply to the Real Data

<!-- b000063 | prose | pages [2] -->
15

<!-- b000064 | prose | pages [2] -->
15

<!-- b000065 | furniture | pages [3] -->
Team # 55278

<!-- b000066 | furniture | pages [3] -->
Page 2 of 24

<!-- b000067 | prose | pages [3] -->
Percentage of Self-Driving Vehicles . . . . . . . . . . . . . . . . . . . . . . . 4.1 16

<!-- b000068 | prose | pages [3] -->
Average Velocity During a Whole Day . . . . . . . . . . . . . . . . . 4.1.1 16

<!-- b000069 | prose | pages [3] -->
Average Velocity During Peak Hours 4.1.2 . . . . . . . . . . . . . . . . .

<!-- b000070 | prose | pages [3] -->
17

<!-- b000071 | prose | pages [3] -->
Trafﬁc Density . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.3 17

<!-- b000072 | prose | pages [3] -->
Average Velocity at Intersections . . . . . . . . . . . . . . . . . . . . 4.1.4 18

<!-- b000073 | prose | pages [3] -->
Dedicated Lanes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2

<!-- b000074 | prose | pages [3] -->
5

<!-- b000075 | heading | pages [3] -->
Sensitivity Analysis

<!-- b000076 | prose | pages [3] -->
19

<!-- b000077 | prose | pages [3] -->
19

<!-- b000078 | prose | pages [3] -->
Lane-Changing Probability Pc . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 19

<!-- b000079 | prose | pages [3] -->
Coefﬁcients α, β, and γ in Vehicle Following Model 5.2 . . . . . . . . . . . . .

<!-- b000080 | prose | pages [3] -->
20

<!-- b000081 | prose | pages [3] -->
Error of Self-Driving Systems . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000082 | prose | pages [3] -->
6

<!-- b000083 | heading | pages [3] -->
Conclusion

<!-- b000084 | prose | pages [3] -->
7 The Letter

<!-- b000085 | prose | pages [3] -->
20

<!-- b000086 | prose | pages [3] -->
22

<!-- b000087 | prose | pages [3] -->
24

<!-- b000088 | furniture | pages [4] -->
Team # 55278

<!-- b000089 | furniture | pages [4] -->
Page 3 of 24

<!-- b000090 | prose | pages [4] -->
1

<!-- b000091 | heading | pages [4] -->
Introduction

<!-- b000092 | prose | pages [4] -->
Self-driving is a technology with growing importance in these years. 2016 is the tipping point for excitement in self-driving cars. In October Tesla announced that all of its new vehicles now had the hardware to drive fully autonomously. All that’s left is developing the software. Also, as mobile communication becomes ubiquitous, it is easy to build connections among self-driving vehicles to form cooperative driving systems.

<!-- b000093 | prose | pages [4] -->
Nowadays trafﬁc jam almost disturbs the daily life of every urban citizen. The arising of self-driving cooperating vehicles has long been a hope to increase the trafﬁc capacity without enlarging the roads, since these vehicles have more accurate control, better sense and prediction of the behavior of ambient vehicles than human-driven ones. In this paper, we make a quantitative and qualitative analysis of the impact on trafﬁc capacity of these newly emerging vehicles.

<!-- b000094 | prose | pages [4] -->
We establish a trafﬁc ﬂow model based on cellar automata to simulate highway trafﬁc ﬂow. We extend the traditional cellar automata to taking into account acceleration values of vehicles. This extension brings much ﬂexibility when modeling the trafﬁc ﬂow, and enable us to test the impact of more detailed control rules for self-driving cooperating cars.

<!-- b000095 | prose | pages [4] -->
Our model can be divided into four parts. First, we propose a trafﬁc generation model based on Poisson distributions. This model captures variance of trafﬁc counts during peak travel hours and the non-peak hours. Then, we model the behavior of vehicle-following, which deﬁnes how a car acts according the car running before it. Dif- ferent rules are applied to distinguish the cooperation between two self-driving cars, and interactions between self-driving and human-driven cars. Then, we design a lane- changing model for vehicle movement across lanes. Finally, we build an intersection model to describe how vehicles change from one highway to another through inter- changes.

<!-- b000096 | prose | pages [4] -->
Then we analyze the feasibility of our model by running simulations with different percentage of self-driving vehicles, different number of lanes and different daily trafﬁc volumes. Under all these simulations our model produces reasonable results, which is consistent with the properties of self-driving vehicles.

<!-- b000097 | prose | pages [4] -->
After that we apply the provided data. We analyze how the highway capacity changes with the percentage of self-driving cars. Results shows that a equilibria exists at around 50% to 70%. We also study the effect of dedicated lanes for self-driving vehicles, and propose a strategy to allocate such lanes.

<!-- b000098 | prose | pages [4] -->
Finally, we do sensitive analysis on some parameters in our model. We also consider what if self-driving systems are not perfect. In other words, these autonomous vehicles may not mature enough and new risk can be introduced. We simulate the inaccuracy of a self-driving system by random acceleration and deceleration with a small probability. Results shows that such inaccuracy can degrade the beneﬁt of self-driving vehicles.

<!-- b000099 | furniture | pages [5] -->
Team # 55278

<!-- b000100 | furniture | pages [5] -->
Page 4 of 24

<!-- b000101 | prose | pages [5] -->
1.1 Literature Review

<!-- b000102 | prose | pages [5] -->
Using cellar automata to analyze trafﬁc ﬂow is widely used by many researchers[1, 2]. This approach has been proved effective to analyze real trafﬁc ﬂow data, and it’s easy to implement. However, none of them consider the scenario with self-driving cars. Their human-driven models lack ﬂexibility to adapt to self-driving vehicles.

<!-- b000103 | prose | pages [5] -->
On the other hand, studies of self-driving vehicles start up just in recent years. Most of the researches are done by using continuous models with complex simulation soft- wares, and focus on the dynamics of self-driving vehicles and the interactions of several vehicles[3, 4]. But how self-driving technology will inﬂuence an entire highway trafﬁc ﬂow is still not answered.

<!-- b000104 | prose | pages [5] -->
Some researchers in civil and environmental engineering believe that self-driving technology can increase highway capacity and reduce air pollution[5]. But they didn’t provide quantitative analysis.

<!-- b000105 | prose | pages [5] -->
In this paper, we propose a brand new cellar automata system which models the impact of self-driving vehicles on highway trafﬁc ﬂow. We extend the traditional trafﬁc ﬂow methods by adding dynamics of self-driving vehicles. We analyze our model with simulations and successfully verify its feasibility. Finally we apply our model to real data and provide constructive advice on trafﬁc management for self-driving cars.

<!-- b000106 | prose | pages [5] -->
1.2

<!-- b000107 | heading | pages [5] -->
Assumptions

<!-- b000108 | prose | pages [5] -->
• Each highway is a straight line without bending.

<!-- b000109 | prose | pages [5] -->
• Self-driving cars can communicate real time data with each other, including veloc- ity and acceleration.

<!-- b000110 | prose | pages [5] -->
• Self-driving cars do not need response time to take action as human drivers do.

<!-- b000111 | prose | pages [5] -->
• Human driven vehicles do not communicate with any other vehicle.

<!-- b000112 | prose | pages [5] -->
• The width of each lane is only enough for one single vehicle.

<!-- b000113 | prose | pages [5] -->
• All vehicles are in the same size.

<!-- b000114 | prose | pages [5] -->
• A car change to another highway through interchanges in intersections, without crossing any trafﬁc ﬂow.

<!-- b000115 | prose | pages [5] -->
• All human-driven cars are identical and all self-driving cars are identical.

<!-- b000116 | prose | pages [5] -->
2

<!-- b000117 | heading | pages [5] -->
The Models

<!-- b000118 | prose | pages [5] -->
2.1 Basic Settings of Cellar Automata

<!-- b000119 | prose | pages [5] -->
Cellar Automata has been a widely used model for trafﬁc ﬂow analysis[1]. The road is divided into cells, each cell can have one car or no car on it. A cell also records the current velocity of the car on it, if any. In cellar automata, positions, time, velocity and acceleration are all discrete. The state of a cell is updated according to its current state

<!-- b000120 | furniture | pages [6] -->
Team # 55278

<!-- b000121 | furniture | pages [6] -->
Page 5 of 24

<!-- b000122 | prose | pages [6] -->
and current states of its surrounding cells. We apply different updating rules to distin- guish the behaviors of self-driving and human-driven cars in our models.

<!-- b000123 | prose | pages [6] -->
2.2

<!-- b000124 | heading | pages [6] -->
Notations

<!-- b000125 | prose | pages [6] -->
Symbol Meaning s An indicator representing the car type on a cell v Current velocity of a car vnew The newly updated value of v after each iteration a Current acceleration of a car anew The newly updated value of a after each iteration N Daily trafﬁc count of a highway segment n Newly arriving vehicles in a highway segment in one second p Number of peak hours. q Percentage of self-driving cars G Distance between two cars in the vehicle-following model vp Speed of the preceding vehicle in vehicle-following model ap Acceleration of preceding car in vehicle-following model Tr Response time for a human driver to take action Vmin Minimum velocity allowed on a highway Vmax Maximum velocity allowed on a highway λpeak Rate parameter of Poisson distribution for car generation during peak hours λnon−peak Rate parameter of Poisson distribution for car generation during non-peak hours Trh Response time for a human driver Trs Response time for a self-driving car Tinter Time needed to transfer from one highway to another through an interchange µij Probability of Crossing Interchanges in Intersection Model Pa Acceleration probability when G > GS Pd Deceleration probability when G > GS Pc Probability of lane-changing α, β, γ Coefﬁcients in vehicles following rules (See 2.4.2 and 2.4.3 for details)

<!-- b000126 | prose | pages [6] -->
2.2.1 Introducing Acceleration into Cellar Automata

<!-- b000127 | prose | pages [6] -->
Most cellar automata used for trafﬁc analysis, however, only consider the velocity of vehicles[1, 2, 6], without considering accelerations. Whenever the velocity changes, it can only increase or decrease by a ﬁxed value. This is nature for human-driven cars, since human drivers have no accurate data about the behavior of ambient vehicles, they tend to be careful. Also, a human driver has no accurate perception of acceleration, so a cellar automata considering only velocity of cars is enough.

<!-- b000128 | prose | pages [6] -->
However, researchers of self-driving use acceleration as an important variable in their analysis[3, 7, 8]. In the case of self-driving cooperating vehicles, a ﬁxed acceleration can be a limitation due to their self-driving and cooperating properties.

<!-- b000129 | furniture | pages [7] -->
Team # 55278

<!-- b000130 | furniture | pages [7] -->
Page 6 of 24

<!-- b000131 | prose | pages [7] -->
• Self-Driving Autonomous vehicles are often equipped with accurate sensors[9], complex control system and even artiﬁcial intelligence technology. They can con- trol acceleration accurately. Thus they can steer more ﬂexibly and fearlessly than human-driven ones.

<!-- b000132 | prose | pages [7] -->
• Cooperating These vehicles can share data including their current acceleration[4], and with these data, they can take more accurate actions to avoid collision as well as make full use of the space of highway. Considering acceleration in our model make more complex cooperating rules possible.

<!-- b000133 | prose | pages [7] -->
Thus, we extend the traditional cellar automata trafﬁc ﬂow model by adding acceler- ation as an attribute of a cell.

<!-- b000134 | prose | pages [7] -->
2.2.2 Attributes of a Cell

<!-- b000135 | prose | pages [7] -->
In our model, a cell represent a 4 meter long space on a single lane, and each cell can only contain one car at a time. A cell has three attributes,

<!-- b000136 | prose | pages [7] -->
1. An integer s ranging from 0 to 2 (inclusive) to represent the car type. 0 for no car, 1 for human-driven, and 2 for self-driving.

<!-- b000137 | prose | pages [7] -->
2. Current velocity v a car.

<!-- b000138 | prose | pages [7] -->
3. Current acceleration a of a car.

<!-- b000139 | prose | pages [7] -->
Only when s is non-zero does the other two attributes make sense.

<!-- b000140 | prose | pages [7] -->
In each step of the simulation, a car moves forward by v cells, and v is updated by adding a and bounded by Vmin and Vmax, the speed limitations of highway. Rules are applied to update a according to the states of surrounding cells. For human-driven and self-driving vehicles we have different rules. Speciﬁc updating rules are introduced in following sections.

<!-- b000141 | prose | pages [7] -->
2.3

<!-- b000142 | heading | pages [7] -->
Generation Model

<!-- b000143 | prose | pages [7] -->
We need a model to generate cars for each highway segment. Poisson distribution is appropriate for this task[10]. It expresses the possibility of number of events occurring in a ﬁxed interval of time. Instead of using one Poisson distribution for all time during the day, we use two for peak hours and non-peak hours respectively. Our generation model also controls the percentage of self-driving cars on the way.

<!-- b000144 | prose | pages [7] -->
Assuming that there are p peak hours in a day and 8% of the daily trafﬁc volume occurs during peak travel hours. With the data of daily vehicle counts, we can calculate the average number of newly arriving cars in one second in each highway segment.

<!-- b000145 | prose | pages [7] -->
λpeak = 0.08N

<!-- b000146 | prose | pages [7] -->
0.92N 3600p , λnon−peak = 3600(24 −p)

<!-- b000147 | prose | pages [7] -->
Suppose the arrival of vehicles follows Poisson distribution, then λpeak and λnon−peak are unbiased estimation for the rate parameters. Thus each second we can sample from

<!-- b000148 | furniture | pages [8] -->
Team # 55278

<!-- b000149 | prose | pages [8] -->
the Poisson distributions

<!-- b000150 | prose | pages [8] -->
λn

<!-- b000151 | prose | pages [8] -->
peak

<!-- b000152 | prose | pages [8] -->
n! e−λpeak,

<!-- b000153 | prose | pages [8] -->
Ppeak(n) =

<!-- b000154 | furniture | pages [8] -->
Page 7 of 24

<!-- b000155 | prose | pages [8] -->
λn

<!-- b000156 | prose | pages [8] -->
non−peak

<!-- b000157 | prose | pages [8] -->
e−λnon−peak

<!-- b000158 | prose | pages [8] -->
Pnon−peak(n) =

<!-- b000159 | prose | pages [8] -->
n!

<!-- b000160 | prose | pages [8] -->
as the number of newly entered vehicles into a highway segment in our simulation, during peak hours and non-peak hours respectively.

<!-- b000161 | prose | pages [8] -->
By adjusting p, we can control the average frequency of vehicles arriving at peak hours, i.e. λpeak. Since the proportion of peak hour trafﬁc count is ﬁxed at 8%, when p is bigger, these 8% vehicles can arrive at a relatively low frequency. We will simulate with different values of p to test the inﬂuence of peak and average trafﬁc volume on our model. The following ﬁgure shows how λpeak and λnon−peak vary with respect to p, when the daily trafﬁc count is 200, 000.

<!-- b000162 | prose | pages [8] -->
Car Arriving Frequency

<!-- b000163 | prose | pages [8] -->
5

<!-- b000164 | prose | pages [8] -->
Number of arriving cars per second

<!-- b000165 | prose | pages [8] -->
4

<!-- b000166 | prose | pages [8] -->
3

<!-- b000167 | prose | pages [8] -->
2

<!-- b000168 | prose | pages [8] -->
1

<!-- b000169 | prose | pages [8] -->
0 1 2 3 4

<!-- b000170 | prose | pages [8] -->
peak

<!-- b000171 | prose | pages [8] -->
5 6 7 8 9

<!-- b000172 | prose | pages [8] -->
Peak Hours

<!-- b000173 | prose | pages [8] -->
non-peak

<!-- b000174 | caption | pages [8] -->
Figure 1: Car Arriving Frequency (N=200,000)

<!-- b000175 | prose | pages [8] -->
From Figure 1, when p = 1, we have about 2 newly arriving cars each second on average during peak hours, and about 1 during non-peak hours. As the number of peak hours increase, the trafﬁc density during peak hours decreases and that during non-peak hours increases.

<!-- b000176 | prose | pages [8] -->
For each car generated from the Poisson distributions, it will be a self-driving car with a probability of q, and a human-driven one with a probability of 1−q. As we adjust q, different percentage of self-driving cars will be on the way.

<!-- b000177 | prose | pages [8] -->
We set the initial velocity v of a newly arriving vehicle as 20m/s, which is a rela- tively low value. Setting the initial speed slow does not hurt the following simulation, because if the trafﬁc density is low, a higher velocity is allowed, and the vehicle will speed up soon according to our following model. The initial value of acceleration a is calculated according to state of ambient vehicles, using the rules introduced in the vehicle-following model.

<!-- b000178 | furniture | pages [9] -->
Team # 55278

<!-- b000179 | furniture | pages [9] -->
Page 8 of 24

<!-- b000180 | prose | pages [9] -->
2.4

<!-- b000181 | heading | pages [9] -->
Vehicle-Following Model

<!-- b000182 | prose | pages [9] -->
Vehicle-Following model deﬁnes the behavior of two cars on the same lane, one run- ning after another. We call the car running in the front preceding car, and the other car follower car.

<!-- b000183 | prose | pages [9] -->
The vehicle-following model deﬁnes how the follower car changes its velocity and acceleration according to the status of the preceding car. We consider three different cases:

<!-- b000184 | prose | pages [9] -->
1. The follower car is human driven.

<!-- b000185 | prose | pages [9] -->
2. The follower car is self-driving and preceding car is human driven.

<!-- b000186 | prose | pages [9] -->
3. Both cars are self-driving.

<!-- b000187 | prose | pages [9] -->
In each case, we deﬁne a rule to update the velocity and acceleration of the follower car.

<!-- b000188 | prose | pages [9] -->
2.4.1 The follower car is Human Driven

<!-- b000189 | prose | pages [9] -->
When the follower car is human driven, the driver can only try to keep a safe dis- tance with the preceding car, since a human driver needs longer response time than self-driving cars to react when the preceding car decelerates suddenly. Here’s the safe distance of a human driven follower car

<!-- b000190 | prose | pages [9] -->
GS = Trhv

<!-- b000191 | prose | pages [9] -->
where Trh stands for response time of a human driver. According to the Two Second Rule[11], Trh = 2s is an appropriate setting, which will be used in our simulation.

<!-- b000192 | prose | pages [9] -->
Human drivers tend to be careful due to potential human error when changing speed. Thus their acceleration is a ﬁxed value. In every second, they can either increase or decrease the velocity by one unit, which is also a convention taken by previous cellar automata based trafﬁc ﬂow analysis.

<!-- b000193 | prose | pages [9] -->
Thus the behavior of a human-driven cars can be divided into two cases:

<!-- b000194 | prose | pages [9] -->
• When the current distance G ≤GS, the driver decelerates.

<!-- b000195 | prose | pages [9] -->
• When G > GS, the driver can accelerate with a probability Pa and decelerate with a probability Pd, and keep the velocity unchanged otherwise. Here Pa + Pd ≤1. The values of Pa and Pd will be specify later.

<!-- b000196 | prose | pages [9] -->
When decelerating, the velocity decreases by 1, i.e. vnew = max(Vmin, v −1). When accelerating, the velocity increases by 1 and bounded by the maximum velocity of high- way, i.e. vnew = min(v + 1, Vmax).

<!-- b000197 | prose | pages [9] -->
Finally let’s specify values of Pa and Pd. When a car runs fast, the human driver tends to slow down. Thus as current velocity v increases, Pa decreases and Pd increases. Each cell is 4 meters long, the maximum speed allowed is 60 miles, which is about 7 cells per second. The following table shows values of Pa and Pd for different v’s.

<!-- b000198 | furniture | pages [10] -->
Team # 55278

<!-- b000199 | furniture | pages [10] -->
Page 9 of 24

<!-- b000200 | caption | pages [10] -->
Table 1: Acceleration and Deceleration Probabilities when G > GS

<!-- b000201 | prose | pages [10] -->
v 1 2 3 Pa 1 0.9 0.8 Pd 0 0.1 0.2 4 5 6 7 0.7 0.5 0.2 0 0.2 0.3 0.4 0.6

<!-- b000202 | prose | pages [10] -->
Self-Driving Vehicle Follows a Human Driven Vehicle 2.4.2

<!-- b000203 | prose | pages [10] -->
Even if self-driving vehicle cannot communicate with the preceding human driver, their sensors can still detect the real time velocity of human-driven car and make a reac- tion immediately. Thus the response time is much shorter than a human driver. The safe distance in this case is still measured by GS = Trsv, but here Trs can take a smaller value than the human response time Trh. We’ll use Trs = 1s in our simulation.

<!-- b000204 | prose | pages [10] -->
Unlike human drivers, self-driving cars equipped with accurate controller have large ﬂexibility in the control of acceleration, they can adjust their acceleration value con- stantly. In every second, we have the updating rules for its velocity and acceleration

<!-- b000205 | prose | pages [10] -->
(

<!-- b000206 | prose | pages [10] -->
a ≥0 min(Vmax, v + a),

<!-- b000207 | prose | pages [10] -->
vnew =

<!-- b000208 | prose | pages [10] -->
max(Vmin, v + a), a < 0

<!-- b000209 | prose | pages [10] -->
anew = α(G −GS) + β(vp −v)

<!-- b000210 | prose | pages [10] -->
The acceleration of a self-driving car depends on the current distance G, safe distance GS, current velocity v and velocity of the preceding vehicle vp. α and β are positive coefﬁ- cients depicting how much the acceleration depends on (G−GS) and velocity difference (v −vp). When G is greater than GS, the distance is too large thus an acceleration is fa- vorable. Conversely when G < GS the car should slow down. The second term β(vp −v) favors acceleration when the self-driving car is slower than preceding human-driven car, and deceleration when it is faster.

<!-- b000211 | heading | pages [10] -->
Following Model For Two Self-Driving Vehicles

<!-- b000212 | prose | pages [10] -->
2.4.3

<!-- b000213 | prose | pages [10] -->
When both vehicles are self-driving, they can communicate velocity and acceleration constantly. They still need a safe distance GS = Trsv. Since two cooperating cars can communicate, the follower car can get the accurate real time acceleration of preceding car ap. Taking ap into account when updating the acceleration provides further ﬂexibility for a self-driving car.

<!-- b000214 | prose | pages [10] -->
The updating rules[3] for the follower car are

<!-- b000215 | prose | pages [10] -->
(

<!-- b000216 | prose | pages [10] -->
min(Vmax, v + a), a ≥0

<!-- b000217 | prose | pages [10] -->
vnew =

<!-- b000218 | prose | pages [10] -->
max(Vmin, v + a), a < 0

<!-- b000219 | prose | pages [10] -->
anew = α(G −GS) + β(vp −v) + γap

<!-- b000220 | prose | pages [10] -->
Adding the term γap, when the preceding car wants to accelerate (ap > 0) or decelerate (ap < 0), the follower car will immediately take corresponding action. Thus this rule makes use of the communication between two self-driving cooperating cars.

<!-- b000221 | furniture | pages [11] -->
Team # 55278

<!-- b000222 | furniture | pages [11] -->
Page 10 of 24

<!-- b000223 | prose | pages [11] -->
2.5

<!-- b000224 | heading | pages [11] -->
Lane-Changing Model

<!-- b000225 | prose | pages [11] -->
Besides adjusting its speed and acceleration, each car has a chance to move to the neighboring lane. A lane-changing can happen only when

<!-- b000226 | prose | pages [11] -->
• Current distance with the preceding car is less than the safe distance.

<!-- b000227 | prose | pages [11] -->
• The cell on the neighboring lane is empty and distances with preceding and fol- lower cars in the neighboring lane are safe.

<!-- b000228 | prose | pages [11] -->
Formally, in the case of Figure 2, if GAB ≤GSAB, then car A can change to lane 1 when GAC > GSAC and GAD > GSAD. Here GAC is the distance between car A and C, and GAB is the distance between car A and B. GSAB, GSAC and GSAD are safe distances between A and B, A and C, and A and D respectively. They are deﬁned in the same way as vehicle-following model, according to the categories of the cars.

<!-- b000229 | caption | pages [11] -->
Figure 2: Conditions for Lane-Changing

<!-- b000230 | prose | pages [11] -->
When only one neighboring lane satisﬁes the condition, the car changes to that lane with a probability Pc. When both left and right lanes satisﬁes the condition, the car changes to either lane with a probability Pc/2.

<!-- b000231 | prose | pages [11] -->
Lane-changing happens before the velocity and acceleration update in the vehicle- following model. After lane-changing, the velocity and acceleration of a vehicle are up- dated according to the rules in the vehicle-following model.

<!-- b000232 | prose | pages [11] -->
2.6

<!-- b000233 | heading | pages [11] -->
Intersection Model

<!-- b000234 | prose | pages [11] -->
Most high way intersections are based on interchanges, a structure that allows high- way to pass through the junction without directly crossing any trafﬁc stream. Thus in an

<!-- b000235 | furniture | pages [12] -->
Team # 55278

<!-- b000236 | furniture | pages [12] -->
Page 11 of 24

<!-- b000237 | prose | pages [12] -->
intersection, a car in one highway can move to another highway without waiting for a trafﬁc light. We will use cloverleaf interchange in our model, since it is the most widely used one. Figure 3 shows the trafﬁc ﬂow on a cloverleaf interchange. A car in Position A on Lane 2 can move to Position B on Lane 3 or Position C on Lane 4. Similarly, a car can enter Lane 2 from Position D on Lane 3 and Position E on Lane 4. The trafﬁc ﬂow on Lane 1 has a similar interaction with trafﬁc ﬂow on Lane 3 and Lane 4.

<!-- b000238 | caption | pages [12] -->
Figure 3: Cloverleaf Interchange

<!-- b000239 | prose | pages [12] -->
Because there’s no crossing through the trafﬁc stream, we can assume the car disap- pears from one highway and appears on another one after a period of time.

<!-- b000240 | prose | pages [12] -->
With this assumption, we introduce 8 parameter µij and µji, for all i ∈{1, 2}, j ∈ {3, 4}, to represent the probability of cars moving from Lane i to Lane j, and from Lane j to Lane i respectively. Assuming all these movements across the interchange takes time Tinter. We summarize the rules for intersection crossing as follows

<!-- b000241 | prose | pages [12] -->
• When a car arrives at the intersection, with probability µij, its movement from Lane i to Lane j starts.

<!-- b000242 | prose | pages [12] -->
• If the movement starts and Tinter seconds pass after that, check if the destination position on Lane j is empty. If so, put the car on that position with its old velocity and update its acceleration with the rules in the vehicle-following model. Other- wise, the car has to wait until the position becomes empty.

<!-- b000243 | prose | pages [12] -->
The intersection model is simulated by running four cellar automata using vehicle- following rules and lane-changing rules, and the intersection rules deﬁned above. De- tails are deferred to the simulation part.

<!-- b000244 | furniture | pages [13] -->
Team # 55278

<!-- b000245 | furniture | pages [13] -->
Page 12 of 24

<!-- b000246 | prose | pages [13] -->
3

<!-- b000247 | heading | pages [13] -->
Analyzing the Model by Simulation

<!-- b000248 | prose | pages [13] -->
We analyze how the highway capacity varies in our model when the percentage of self-driving vehicles, number of lanes and trafﬁc volume change. We run the simulation on a highway segment of 250 cells long, which is 1000 meters. Each simulation runs for a trafﬁc ﬂow of 24 hours, using the generation model to generate vehicles.

<!-- b000249 | prose | pages [13] -->
The simulation results shows that self-driving vehicles increases the highway capac- ity. We also compare the effects of self-driving vehicles with other factors.

<!-- b000250 | prose | pages [13] -->
3.1 Criteria

<!-- b000251 | prose | pages [13] -->
To evaluate the trafﬁc capacity, we need some criteria. In our simulations, we mainly use average passing time and trafﬁc density.

<!-- b000252 | prose | pages [13] -->
• Whole-Day Average Passing Time The average time for a vehicle to pass the 250- cell long highway segment.

<!-- b000253 | prose | pages [13] -->
• Peak-Hour Average Passing Time The average time for a vehicle to pass the 250- cell long highway segment during peak hours.

<!-- b000254 | prose | pages [13] -->
• Trafﬁc Density Number of vehicles on the 250-cell long highway segment. This value will change with time as the cars run in and out the highway. So for each combination of model parameters, we can obtain a curve of trafﬁc density varying with time. Since the trafﬁc load is a time dependent value, we can further use it to analyze the stability of a trafﬁc ﬂow.

<!-- b000255 | prose | pages [13] -->
3.2 Effects of Percentage of Self-Driving Vehicles

<!-- b000256 | prose | pages [13] -->
We run the cellar automata on a highway segment, varying the percentage of self- driving vehicles to observe the change of highway capacity. The highway segment has 3 lanes on both directions. We ﬁxed the daily trafﬁc volume at 100, 000, with 50, 000 on each direction. The lane-changing probability Pc = 0.5. Number of peak hours in the generation model is p = 1. We calculate the average time to pass through the highway segment and trafﬁc load. Figure 4 and Figure 5 show the results.

<!-- b000257 | prose | pages [13] -->
We have following observations when the self-driving percentage increases.

<!-- b000258 | prose | pages [13] -->
• Average passing time reduces: As the percentage of self-driving vehicles increases, the average passing time during peak hours decreases sharply at ﬁrst, and reach a equilibria at around 70%. Self-driving vehicles can increase the trafﬁc capacity by more accurate control and cooperating. The beneﬁt is tiny when the percentage of self-driving car is low. Because cooperation is difﬁcult with few self-driving cars on the road.

<!-- b000259 | prose | pages [13] -->
• Peak-hour pressure is alleviated Self-driving cars reduce the difference between peak-hour passing time and whole-day passing time. In Figure 4, as the percentage of driving cars increases, the blue curve and black curve get closer. This reveal an important advantage of self-driving cars, that they are ﬂexible enough to deal with peak hours.

<!-- b000260 | furniture | pages [14] -->
Team # 55278

<!-- b000261 | furniture | pages [14] -->
Page 13 of 24

<!-- b000262 | caption | pages [14] -->
Figure 4: Average Passing Time

<!-- b000263 | caption | pages [14] -->
Figure 5: Trafﬁc Density

<!-- b000264 | prose | pages [14] -->
• The space capacity of highway increases: In Figure 5, as the percentage of self- driving cars increases, average number of vehicles on the 250-cell highway seg- ment reduces. When self-driving percentage is low, cars on the road moves slowly, as indicated in Figure 4. Thus, trafﬁc jam is easy to arise, which result in many cars being stuck on the road. With more self-driving cars, trafﬁc jam can be relief. Again, the impact of self-driving car is more obvious during peak hours.

<!-- b000265 | prose | pages [14] -->
3.3 Effects of Lane Number

<!-- b000266 | prose | pages [14] -->
We run simulations with 3, 4 and 5 lanes on both directions respectively. The daily trafﬁc volume is 100, 000, with 50, 000 on each direction and number of peak hours p = 1. The lane-changing probability Pc = 0.5. And the self-driving percentage is 50%.

<!-- b000267 | prose | pages [14] -->
We also test the effects of lane number with different self-driving percentage. We simulate lane numbers 3, 4 and 5 with self-driving percentage 30% and 70%.

<!-- b000268 | prose | pages [14] -->
We have two important observations based on Figure 6 and Figure 7.

<!-- b000269 | prose | pages [14] -->
• More lanes can speed up trafﬁc ﬂow: Both during the whole day and peak hours, adding lanes to the highway shorten the average passing time. This is consistent with our intuition. Because with more lanes on the highway, cars have more free- dom to change lane when the current lane is too crowded.

<!-- b000270 | prose | pages [14] -->
• Self-driving reduces the impact of lane number: Both in Figure 6 and Figure 7, as self-driving percentage increases, the three curves get closer to each other. When most of the cars are self-driving, adding more lanes to the highway make small difference.

<!-- b000271 | furniture | pages [15] -->
Team # 55278

<!-- b000272 | caption | pages [15] -->
Figure 6: Impact of Lane Number

<!-- b000273 | prose | pages [15] -->
(Whole Day)

<!-- b000274 | furniture | pages [15] -->
Page 14 of 24

<!-- b000275 | caption | pages [15] -->
Figure 7: Impact of Lane Nmber

<!-- b000276 | prose | pages [15] -->
(Peak Hours)

<!-- b000277 | prose | pages [15] -->
Effects of Dedicated Lanes for Self-Driving Cars 3.4

<!-- b000278 | prose | pages [15] -->
This section we discuss how our model reacts to dedicated lanes for self-driving cars. To test the effects of dedicated lanes, we modify the generation model and lane-changing model.

<!-- b000279 | prose | pages [15] -->
• Generation Model When a self-driving car is generated, we put it to one of the dedicated lanes.

<!-- b000280 | prose | pages [15] -->
• Lane-Changing Model A self-driving car cannot change to a non-dedicated lane.

<!-- b000281 | caption | pages [15] -->
Figure 8:

<!-- b000282 | prose | pages [15] -->
Impact of Dedicated Lanes (Whole Day)

<!-- b000283 | caption | pages [15] -->
Figure 9:

<!-- b000284 | prose | pages [15] -->
Impact of Dedicated Lanes (Peak Hours)

<!-- b000285 | furniture | pages [16] -->
Team # 55278

<!-- b000286 | furniture | pages [16] -->
Page 15 of 24

<!-- b000287 | prose | pages [16] -->
With these modiﬁcations, run the simulation with 5 lanes on both directions. The daily trafﬁc volume is 100, 000, with 50, 000 on each direction. The number of peak hours p = 1. The lane-changing probability Pc = 0.5. We increase the dedicated lanes from 1 to 3 and calculate the average passing time, when self-driving percentage is 30%, 50% and 70% respectively.

<!-- b000288 | prose | pages [16] -->
From Figure 8 and Figure 9, when the percentage of self-driving vehicles are small, dedicated lanes may hurt the trafﬁc capacity, especially during the peak hours. For ex- ample, in Figure 9, when there are only 30% of self-driving cars, 3 dedicated lines results in an average passing time of 80s, which is much slower than other cases.

<!-- b000289 | prose | pages [16] -->
However, as the percentage of self-driving cars arises, dedicated lane can improve the performance by a little. For example, in Figure 9, when 70% are self-driving, any number of dedicated lanes outperforms no dedicated lane strategy.

<!-- b000290 | prose | pages [16] -->
3.5 Effects of Trafﬁc Volume

<!-- b000291 | prose | pages [16] -->
Different daily trafﬁc volume from 100, 000 to 500, 000 are tested. The trafﬁc volume are distributed to both directions equally. Each direction has 5 lanes. The lane-changing probability Pc = 0.5. Fix the number of peak hours p = 1. Simulations are done for 30%, 50% and 70% of self-driving cars.

<!-- b000292 | caption | pages [16] -->
Figure 10: Impact of Trafﬁc Volume

<!-- b000293 | caption | pages [16] -->
Figure 11: Impact of Trafﬁc Volume

<!-- b000294 | prose | pages [16] -->
(Whole Day)

<!-- b000295 | prose | pages [16] -->
(Peak Hours)

<!-- b000296 | prose | pages [16] -->
The impact of trafﬁc volume reduces as percentage of self-driving cars increases. Thus self-driving cars can maintain the highway capacity well even when the trafﬁc is quite heavy.

<!-- b000297 | prose | pages [16] -->
4 Apply to the Real Data

<!-- b000298 | prose | pages [16] -->
We apply our model to the provided data of Interstates 5, 90, and 405, as well as State Route 520. We test how trafﬁc capacity of these roads changes with the percentage of

<!-- b000299 | furniture | pages [17] -->
Team # 55278

<!-- b000300 | furniture | pages [17] -->
Page 16 of 24

<!-- b000301 | prose | pages [17] -->
self-driving cars. We also analyze the feasibility of dedicated lanes, and give suggestions based on our analysis.

<!-- b000302 | prose | pages [17] -->
4.1 Percentage of Self-Driving Vehicles

<!-- b000303 | prose | pages [17] -->
We run simulation for each segment on the data sheet, study the impact of self- driving vehicles on highway capacity during the whole day and during peak hours. Though self-driving vehicles do not increase the highway capacity a lot on average dur- ing the day, but they have a signiﬁcant impact during the peak hours.

<!-- b000304 | prose | pages [17] -->
4.1.1 Average Velocity During a Whole Day

<!-- b000305 | prose | pages [17] -->
In the data sheet, 224 highway segments are listed. These segments belong to four roads, Interstates 5, 90, and 405 and State Route 520. For each segment and its corre- sponding daily trafﬁc count, we test the average velocity vi, i = 1, 2, ..., 224 of cars pass- ing through the segment during a day. Then we calculate the average velocity for each road, by averaging vi’s of the segments belonging to the road.

<!-- b000306 | caption | pages [17] -->
Figure 12: Average Trafﬁc Flow Velocity During a Whole Day

<!-- b000307 | prose | pages [17] -->
On each road, the average velocity increases with percentage of self-driving vehicles. As the percentage of self-driving cars increases from 10% to 50%, the average velocity increases rapidly. However, when the percentage changing from 50% to 90%, the average velocity only increases by a little. An equilibria is reached at around 80%.

<!-- b000308 | prose | pages [17] -->
The average velocity increases most markedly when percentage of self-driving vehi- cles changes from 0% to 10%, and from 10% to 20%.

<!-- b000309 | furniture | pages [18] -->
Team # 55278

<!-- b000310 | furniture | pages [18] -->
Page 17 of 24

<!-- b000311 | prose | pages [18] -->
4.1.2 Average Velocity During Peak Hours

<!-- b000312 | prose | pages [18] -->
Average velocities of each road during peak hours are calculated in the same way as 4.1.1.

<!-- b000313 | caption | pages [18] -->
Figure 13: Average Trafﬁc Flow Velocity During Peak Hours

<!-- b000314 | prose | pages [18] -->
Compared with Figure 12, we found self-driving has a more signiﬁcant impact for peak hour trafﬁc ﬂow. The average velocities on all four roads experience a huge increase as self-driving percentage increases. For example, when the percentage increases from 10% to 50%, average velocity on Route 5 increases by about 10m/s, and by about 5m/s when the percentage increases from 50% to 90%. An equilibria is reached at around 70%.

<!-- b000315 | prose | pages [18] -->
4.1.3 Trafﬁc Density

<!-- b000316 | prose | pages [18] -->
We calculated the average trafﬁc density of the four highways. We record how many trafﬁc are there on each road per second when doing the simulation in 4.1.1 and 4.1.2. Then we calculate the average number of cars per second per kilometer.

<!-- b000317 | prose | pages [18] -->
From Figure 14 and Figure 15 self-driving cars help reduce the trafﬁc density of each road. Again, the impact is more signiﬁcant during the peak hours. In Figure 15, the trafﬁc density decreases rapidly when the percentage of self-driving is low. From 10% to 50%, the trafﬁc density reduces by half. While from 50% to 90%, there’s no signiﬁcant change. An equilibria is reached at around 50%.

<!-- b000318 | furniture | pages [19] -->
Team # 55278

<!-- b000319 | caption | pages [19] -->
Figure 14: Impact of Self-Driving

<!-- b000320 | prose | pages [19] -->
Cars on Trafﬁc Density (Whole Day)

<!-- b000321 | prose | pages [19] -->
4.1.4 Average Velocity at Intersections

<!-- b000322 | furniture | pages [19] -->
Page 18 of 24

<!-- b000323 | caption | pages [19] -->
Figure 15: Impact of Self-Driving

<!-- b000324 | prose | pages [19] -->
Cars on Trafﬁc Density (Peak Hours)

<!-- b000325 | prose | pages [19] -->
We apply the intersection model to simulate the trafﬁc ﬂow at the mile post 152.72 to 155.18 of Interstate 5 highway, where it intersects with Interstate 405 (mile post 0 to 0.09). We calculate the average velocity of vehicles during the whole day. Each vehicle running through mile post 152.72 to 155.18 on Interstate 5, or on mile post 0 to 0.09 on Interstate 405 may cross the interchange or not, with all the probabilities in the intersection model being 50%. We set Tinter, the time to cross interchange, as 10s. We get similar result as in straight results.

<!-- b000326 | caption | pages [19] -->
Figure 16: Simulation of Highway Intersection

<!-- b000327 | furniture | pages [20] -->
Team # 55278

<!-- b000328 | furniture | pages [20] -->
Page 19 of 24

<!-- b000329 | prose | pages [20] -->
4.2 Dedicated Lanes

<!-- b000330 | caption | pages [20] -->
Figure 17:

<!-- b000331 | prose | pages [20] -->
Impact of Dedicated

<!-- b000332 | caption | pages [20] -->
Figure 18:

<!-- b000333 | prose | pages [20] -->
Impact of Dedicated

<!-- b000334 | prose | pages [20] -->
Lanes (Whole Day)

<!-- b000335 | prose | pages [20] -->
Lanes (Peak Hours)

<!-- b000336 | prose | pages [20] -->
We pick the data of Interstate 5 to analyze effects of dedicated lanes. Figure 17 and

<!-- b000337 | caption | pages [20] -->
Figure 18 show the average velocity of Interstate 5 with different number of dedicated

<!-- b000338 | prose | pages [20] -->
lanes for self-driving cars.

<!-- b000339 | prose | pages [20] -->
When self-driving cars take a small proportion, dedicated lanes do not help to in- crease the average velocity a lot. However, when most vehicles are self-driving, for example 70%, dedicated lanes become necessary.

<!-- b000340 | prose | pages [20] -->
5

<!-- b000341 | heading | pages [20] -->
Sensitivity Analysis

<!-- b000342 | prose | pages [20] -->
We analyze the sensitivity of some parameters in our model. We run simulations on a 250-cell long high way segment with 5 lanes, and no dedicated lane. The daily trafﬁc count is 100, 000. With this setting, we analyze how the parameters in our model inﬂuences our conclusion. The results show that our model is quite robust.

<!-- b000343 | prose | pages [20] -->
Lane-Changing Probability Pc 5.1

<!-- b000344 | prose | pages [20] -->
In our previous experiments, the default value of Pc is 0.5. So when the distance G be- tween two cars is less than safe distance GS, the follower car will change to another lane with probability 50%. Here we test the impact of self-driving cars on highway capacity with different Pc’s.

<!-- b000345 | prose | pages [20] -->
When Pc = 0.2, the cars tend to stay on the same lane even if it is crowded. Thus

<!-- b000346 | furniture | pages [21] -->
Team # 55278

<!-- b000347 | furniture | pages [21] -->
Page 20 of 24

<!-- b000348 | caption | pages [21] -->
Figure 19: Sensitivity of Lane-Changing Probability

<!-- b000349 | prose | pages [21] -->
the average passing time for a car is longer. While Pc = 0.8, the cars change lanes frequently to make use of spare spaces, so the average passing time is shorter. However, the differences with Pc = 0.5 are small.

<!-- b000350 | heading | pages [21] -->
Coefﬁcients α, β, and γ in Vehicle Following Model

<!-- b000351 | prose | pages [21] -->
5.2

<!-- b000352 | prose | pages [21] -->
Recall that α, β and γ are coefﬁcients used in the update of the acceleration of self- driving vehicles in Section 2.4.2 and 2.4.3. Our default setting is α = β = γ = 1. Recall the updating rule

<!-- b000353 | prose | pages [21] -->
anew = α(G −GS) + β(vp −v) + γαp

<!-- b000354 | prose | pages [21] -->
Thus α control how much the acceleration depends on distance. β controls the impact of relative speed. And γ controls the impact of acceleration of the preceding car. When α is bigger, the follower car tends to keep a safe distance. When β is bigger, the follower car tries to catch up the speed of the preceding car. And when γ is big, the follower car will accelerate synchronously with the preceding car.

<!-- b000355 | prose | pages [21] -->
We test different combinations of α, β and γ. The results are shown in Figure 20. We see a tiny speed up of trafﬁc ﬂow when they are larger.

<!-- b000356 | prose | pages [21] -->
5.3 Error of Self-Driving Systems

<!-- b000357 | prose | pages [21] -->
In our model, we assume self-driving cars are perfect. They don’t introduce any new risk. However, as a newly emerging technology, self-driving today is not mature enough. On June 30, 2016, a fatal crash of self-driving Tesla was reported. The driver was killed. Thus, it is necessary to test how system error will affect the performance of self-driving cars.

<!-- b000358 | furniture | pages [22] -->
Team # 55278

<!-- b000359 | furniture | pages [22] -->
Page 21 of 24

<!-- b000360 | caption | pages [22] -->
Figure 20: Sensitivity of α, β and γ

<!-- b000361 | prose | pages [22] -->
We introduce self-driving system error by making self-driving cars accelerate or de- celerate by 1 unit both with a probability of 10%. The result is shown in Figure 21. As we can see, such inaccurate acceleration and deceleration will degrade the performance, resulting longer passing time compared with perfect self-driving systems.

<!-- b000362 | caption | pages [22] -->
Figure 21: Impact of Self-Driving System Error

<!-- b000363 | furniture | pages [23] -->
Team # 55278

<!-- b000364 | furniture | pages [23] -->
Page 22 of 24

<!-- b000365 | prose | pages [23] -->
6

<!-- b000366 | heading | pages [23] -->
Conclusion

<!-- b000367 | prose | pages [23] -->
In this paper, we build a model to analyze the impact of self-driving cars on highway capacity. We analyze our models with many simulations. And ﬁnally we apply our model to the data of four real highway. Here we conclude our interesting ﬁndings.

<!-- b000368 | prose | pages [23] -->
• Self-driving vehicles can increase highway capacity. As the percentage of self- driving cars increases, the trafﬁc ﬂow proceeds with higher velocity, and lower space density.

<!-- b000369 | prose | pages [23] -->
• Dedicated lanes for self-driving cars are not necessary when the percentage of self- driving cars is low, while dedicated lanes can increase the capacity by a little when the percentage is higher than 70%.

<!-- b000370 | prose | pages [23] -->
• Self-driving vehicles can reduce the impact of lane number and trafﬁc volume.

<!-- b000371 | prose | pages [23] -->
When most of the cars are self-driving, the velocity of a trafﬁc ﬂow do not change a lot with these factors.

<!-- b000372 | heading | pages [23] -->
References

<!-- b000373 | references | pages [23] -->
[1] K. Nagel and M. Schreckenberg, “A cellular automaton model for freeway trafﬁc,”

<!-- b000374 | references | pages [23] -->
Journal De Physique I, vol. 12, pp. 2221–2229, 1992.

<!-- b000375 | references | pages [23] -->
[2] D. Ren, Y. Du, Y. Wang, and L. Huang, “Analysis of trafﬁc ﬂow based cellar au-

<!-- b000376 | references | pages [23] -->
tomata,” 1997.

<!-- b000377 | references | pages [23] -->
[3] B. Van Arem, C. J. Van Driel, and R. Visser, “The impact of cooperative adaptive

<!-- b000378 | references | pages [23] -->
cruise control on trafﬁc-ﬂow characteristics,” IEEE Transactions on Intelligent Trans-

<!-- b000379 | references | pages [23] -->
portation Systems, vol. 7, no. 4, pp. 429–436, 2006.

<!-- b000380 | references | pages [23] -->
[4] L. D. Baskar, B. De Schutter, and H. Hellendoorn, “Model-based predictive trafﬁc

<!-- b000381 | references | pages [23] -->
control for intelligent vehicles: Dynamic speed limits and dynamic lane allocation,”

<!-- b000382 | references | pages [23] -->
in Intelligent Vehicles Symposium, 2008 IEEE.

<!-- b000383 | references | pages [23] -->
IEEE, 2008, pp. 174–179.

<!-- b000384 | references | pages [23] -->
[5] A. R. Pinjari, B. Augustin, and N. Menon, “Highway capacity impacts of au-

<!-- b000385 | references | pages [23] -->
tonomous vehicles: An assessment,” Centre for Urban Transportation Research. Florida,

<!-- b000386 | references | pages [23] -->
USA, 2013.

<!-- b000387 | references | pages [23] -->
[6] S. Benjaafar, K. Dooley, and W. Setyawan, “A sensitivity study of the effectiveness

<!-- b000388 | references | pages [23] -->
of active debris removal in leo,” vol. 64, no. 2-3, pp. 236–243, 2007.

<!-- b000389 | references | pages [23] -->
[7] P. Tientrakool, Y.-C. Ho, and N. F. Maxemchuk, “Highway capacity beneﬁts from

<!-- b000390 | references | pages [23] -->
using vehicle-to-vehicle communication and sensors for collision avoidance,” in Ve-

<!-- b000391 | references | pages [23] -->
hicular Technology Conference (VTC Fall), 2011 IEEE.

<!-- b000392 | references | pages [23] -->
IEEE, 2011, pp. 1–5.

<!-- b000393 | references | pages [23] -->
[8] L. Zhao and J. Sun, “Simulation framework for vehicle platooning and car-

<!-- b000394 | references | pages [23] -->
following behaviors under connected-vehicle environment,” Procedia-Social and Be-

<!-- b000395 | references | pages [23] -->
havioral Sciences, vol. 96, pp. 914–924, 2013.

<!-- b000396 | furniture | pages [24] -->
Team # 55278

<!-- b000397 | furniture | pages [24] -->
Page 23 of 24

<!-- b000398 | references | pages [24] -->
[9] Y. Yin, M. A. Miller, and S. E. Shladover, “Assessment of the applicability of co-

<!-- b000399 | references | pages [24] -->
operative vehicle-highway automation systems to freight movement in chicago,”

<!-- b000400 | references | pages [24] -->
in Transportation Research Board 2004 Annual Meeting.(http://database. path. berkeley.

<!-- b000401 | references | pages [24] -->
edu/reports/index. cgi, 2004.

<!-- b000402 | references | pages [24] -->
[10] D. L. Gerlough and A. Schuhl, Use of Poisson distribution in highway trafﬁc.

<!-- b000403 | references | pages [24] -->
Eno

<!-- b000404 | references | pages [24] -->
Foundation for Highway Trafﬁc Control, 1955.

<!-- b000405 | references | pages [24] -->
[11] W. K. Seymour and E. J. Bertothy, Driver’s Manual.

<!-- b000406 | references | pages [24] -->
Connecticut Department of

<!-- b000407 | references | pages [24] -->
Motor Vehicles, 2016.

<!-- b000408 | furniture | pages [25] -->
Team # 55278

<!-- b000409 | furniture | pages [25] -->
Page 24 of 24

<!-- b000410 | references | pages [25] -->
7

<!-- b000411 | references | pages [25] -->
The Letter

<!-- b000412 | references | pages [25] -->
Dear Ofﬁcials,

<!-- b000413 | references | pages [25] -->
It’s our honor to help you with analyzing the effects of allowing self-driving, coop-

<!-- b000414 | references | pages [25] -->
erating vehicles on capacity of highways in the Greater Seattle area. We are writing this

<!-- b000415 | references | pages [25] -->
letter to report our latest ﬁndings.

<!-- b000416 | references | pages [25] -->
We have built a novel Cellar Automata Model to analyze the effects of allowing self-

<!-- b000417 | references | pages [25] -->
driving, cooperating cars on Interstates 5, 90, and 405, as well as State Route 520 in

<!-- b000418 | references | pages [25] -->
Thurston, Pierce, King and Snohomish counties. By running simulations with different

<!-- b000419 | references | pages [25] -->
percentage of self-driving vehicles, different number of lanes and different daily trafﬁc

<!-- b000420 | references | pages [25] -->
volumes, we analyze the feasibility of our model and then apply it to the real data. The

<!-- b000421 | references | pages [25] -->
results show that self-driving and cooperating cars can increase highway capacity. In

<!-- b000422 | references | pages [25] -->
other words, they can relieve the stress of trafﬁc jams.

<!-- b000423 | references | pages [25] -->
The capacity of highway increases markedly when there are 10% self-driving vehi-

<!-- b000424 | references | pages [25] -->
cles, and reach an equilibria at around 70%. Speciﬁcally, the average velocity of trafﬁc

<!-- b000425 | references | pages [25] -->
ﬂow increases with the arising percentage of self-driving vehicles. Also, the trafﬁc den-

<!-- b000426 | references | pages [25] -->
sity on the road decreases with more self-driving vehicles.

<!-- b000427 | references | pages [25] -->
These vehicles are equipped with accurate sensors and intelligent control systems.

<!-- b000428 | references | pages [25] -->
So they require shorter safe distance with other vehicles and have higher ﬂexibility of

<!-- b000429 | references | pages [25] -->
acceleration and deceleration. These properties enable them to make full use of the space

<!-- b000430 | references | pages [25] -->
on highways and accelerate the overall trafﬁc ﬂow.

<!-- b000431 | references | pages [25] -->
What’s more, these vehicles can communicate with each other and share data in-

<!-- b000432 | references | pages [25] -->
cluding velocity and acceleration. Such communication makes the synchronous actions

<!-- b000433 | references | pages [25] -->
between two vehicles possible and eliminate potential collisions even when two cars are

<!-- b000434 | references | pages [25] -->
very close to each other. They can also test the real time velocity of ambient vehicles, and

<!-- b000435 | references | pages [25] -->
adjust their own speed accordingly.

<!-- b000436 | references | pages [25] -->
Based on our analysis, we provide some suggestions to better manage and exploit

<!-- b000437 | references | pages [25] -->
self-driving vehicles:

<!-- b000438 | heading | pages [25] -->
1. Popularize self-driving vehicles, even only a little bit. Our analysis shows most

<!-- b000439 | prose | pages [25] -->
beneﬁt to trafﬁc capacity happens when the percentage of self-driving increases from 0% to 50%. Since self-driving vehicles are not very popular now, huge im- provement can be achieved even increase the number of these vehicles by a little.

<!-- b000440 | heading | pages [25] -->
2. Do not hurry to build dedicated lanes for self-driving cars. Our simulations sug-

<!-- b000441 | prose | pages [25] -->
gest that dedicated lanes can only be helpful when the percentage of self-driving cars is high enough, for example 70%. Allocating dedicated lanes can increase the overhead and can be expensive. Since few self-driving vehicles are on the road to- day, such dedicated lanes may even hurt the trafﬁc system by making other lanes for human-driven cars too crowded.

<!-- b000442 | prose | pages [25] -->
We believe our model is useful for management of self-driving cars in the future. You’re welcome to contact us at any time for further cooperation.

<!-- b000443 | prose | pages [25] -->
Yours Sincerely,

<!-- b000444 | furniture | pages [25] -->
Team# 55278
