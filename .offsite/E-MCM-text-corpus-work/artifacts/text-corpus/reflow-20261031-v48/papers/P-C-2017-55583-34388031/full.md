# P-C-2017-55583-34388031

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
55583

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | prose | pages [1] -->
T4 F4

<!-- b000007 | title | pages [1] -->
2017

<!-- b000008 | prose | pages [1] -->
MCM/ICM

<!-- b000009 | heading | pages [1] -->
Summary Sheet

<!-- b000010 | title | pages [1] -->
Self-driving vehicle’s prospect in trafﬁc

<!-- b000011 | title | pages [1] -->
network

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
We construct a Mixed Cooperation model to simulate each section of the trafﬁc network independently based on Cellular Automata. We assume that self-driving vehicles need no safety interval compared with non-self-driving ones because of good synchronization with the former vehicle. And also, we assume that the junctions have little inﬂuence on simulation because the trafﬁc performance is relatively continuous. Our Mixed Cooperation model contains three main part.

<!-- b000014 | prose | pages [1] -->
First, in our basic model, we presume that trafﬁc counts satisﬁes uniform distribution in a day. We know the trafﬁc count and lanes of each section of the trafﬁc network , so we can get the trafﬁc density of each road section in a period and continue to use different self-driving ratio to simulate the trafﬁc ﬂow.

<!-- b000015 | prose | pages [1] -->
Next, in our time-based model, we take time model into considera- tion. We presume that trafﬁc density function over time is identical to dual-Gaussian distribution in a day, which means that there are two period of trafﬁc peaks. So we can get the trafﬁc density of each road section in each period of one day and continue to simulate similarly as the basic model.

<!-- b000016 | prose | pages [1] -->
Further, based on our time-based model, we construct a dedication- model, considering dedicated lanes for self-driving vehicles and con- tinue to simulate similarly as the time-based model.

<!-- b000017 | prose | pages [1] -->
In conclusion, we use the average velocity of vehicles in each road section in each period to evaluate the performance and capacity. Our models give the result of effect of self-driving on trafﬁc performance under different trafﬁc density. Furthermore, our models point out the condition of needing dedicated lanes for self-driving vehicles.

<!-- b000018 | keywords | pages [1] -->
Keywords: Trafﬁc ﬂow; Self-driving; Cooperating system;

<!-- b000019 | prose | pages [2] -->
Governor Jay Inslee

<!-- b000020 | prose | pages [2] -->
Ofﬁce of the Governor

<!-- b000021 | prose | pages [2] -->
PO Box 40002

<!-- b000022 | prose | pages [2] -->
Olympia, WA 98504-0002

<!-- b000023 | prose | pages [2] -->
Dear Governor Inslee:

<!-- b000024 | prose | pages [2] -->
I write to you on behalf of the MCM team 55583. We are extremely concerned about the trafﬁc condition in the Great Seattle area. Investigation shows that the trafﬁc ﬂow usually exceeds the trafﬁc capacity in many regions in the Great Seattle, especially during peak hours. We hope to help you improve the trafﬁc conditions.

<!-- b000025 | prose | pages [2] -->
The current trafﬁc condition could lead to many severe problems. The ﬁrst problem is unacceptable delay during peak hours.During the morning commute and at the end of the day these delays become extreme long. Also it could lead to congested roads, and potentially increase the probability of occurrence of trafﬁc accidents. Congested roads could also cause problems for emergency vehicles, making them unable to respond in an appropriate amount of time.

<!-- b000026 | prose | pages [2] -->
After an in-depth study of the trafﬁc conditions in the Great Seattle area, we have come up with some ideas that can help address this issue. We propose self- driving, cooperating cars as a solution to increase the trafﬁc capacity without building extra lanes.

<!-- b000027 | prose | pages [2] -->
Compared to human-drived cars, self-driving cars have many advantages. The biggest advantage is that it take much less time to react in terms of emer- gency. This actually allows self-driving cars to keep a closer distance with the car in front of it, thus it takes up much less trafﬁc resource. In addition to this, self driving cars can tune their acceleration and deceleration proﬁles to consume less fuel.

<!-- b000028 | prose | pages [2] -->
Those advantages mentioned above make self-driving cars an excellent choice for addressing heavy trafﬁc load. We build a model to simulate the trafﬁc ﬂow of the most busy roads in the Great Seattle area and evaluate the effectiveness of self-driving cars addressing the problem of heavy trafﬁc load. The simula- tion shows promising results. The introduction of self-driving cars makes all cars among all roads in the Great Seattle area go faster, it works especially well among busy roads during trafﬁc peak hours. When no self-driving cars are in- troduced, the trafﬁc goes very slow during peak hours, but after introducing approximately 50% self-driving cars the trafﬁc ﬂow goes 1.5 2 times faster.

<!-- b000029 | prose | pages [2] -->
In addition to making trafﬁc ﬂow faster, self-driving cars also make trafﬁc ﬂow more stable. From our simulation, we observed that introduction of self- driving cars help to reduce the variance of trafﬁc delay. This is important because it helps to estimate times, and helps to reduce "just in case" time.

<!-- b000030 | prose | pages [2, 3] -->
For the above reasons, we propose self-driving cars as a solution to heavy trafﬁc load in the Great Seattle. We appreciate all that you do for this city, and we look forward to seeing positive changes. We hope you can accept out advices.

<!-- b000032 | prose | pages [3] -->
Sincerely yours

<!-- b000033 | prose | pages [3] -->
MCM 2017 Team 55583

<!-- b000034 | furniture | pages [4] -->
Team # 55583

<!-- b000035 | heading | pages [4] -->
Contents

<!-- b000036 | contents | pages [4] -->
1 Introduction

<!-- b000037 | contents | pages [4] -->
1

<!-- b000038 | contents | pages [4] -->
1.1

<!-- b000039 | contents | pages [4] -->
Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [4] -->
1

<!-- b000041 | contents | pages [4] -->
1.2

<!-- b000042 | contents | pages [4] -->
Related Work

<!-- b000043 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [4] -->
1

<!-- b000045 | contents | pages [4] -->
2 Assumptions and Notations

<!-- b000046 | contents | pages [4] -->
2

<!-- b000047 | contents | pages [4] -->
2.1

<!-- b000048 | contents | pages [4] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [4] -->
2

<!-- b000050 | contents | pages [4] -->
2.2

<!-- b000051 | contents | pages [4] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [4] -->
2

<!-- b000053 | contents | pages [4] -->
3 Model Construction

<!-- b000054 | contents | pages [4] -->
3

<!-- b000055 | contents | pages [4] -->
3.1

<!-- b000056 | contents | pages [4] -->
The self-driving, cooperating car model . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [4] -->
3

<!-- b000058 | contents | pages [4] -->
3.2

<!-- b000059 | contents | pages [4] -->
The mixed, dynamic road model . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [4] -->
4

<!-- b000061 | contents | pages [4] -->
3.3

<!-- b000062 | contents | pages [4] -->
Performance evaluation criteria . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [4] -->
6

<!-- b000064 | contents | pages [4] -->
Car Velocity v . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [4] -->
3.3.1

<!-- b000066 | contents | pages [4] -->
6

<!-- b000067 | contents | pages [4] -->
1

<!-- b000068 | contents | pages [4] -->
1

<!-- b000069 | contents | pages [4] -->
3.3.2

<!-- b000070 | contents | pages [4] -->
Daily Equilibria

<!-- b000071 | contents | pages [4] -->
t ,

<!-- b000072 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [4] -->
6

<!-- b000074 | contents | pages [4] -->
σ2

<!-- b000075 | contents | pages [4] -->
σ2s

<!-- b000076 | contents | pages [4] -->
4 Model Extension and Simulation Analysis

<!-- b000077 | contents | pages [4] -->
7

<!-- b000078 | contents | pages [4] -->
4.1

<!-- b000079 | contents | pages [4] -->
Problem1: The effects of auto-driving cars in trafﬁc network . . . .

<!-- b000080 | contents | pages [4] -->
7

<!-- b000081 | contents | pages [4] -->
Car Velocity/Performance v

<!-- b000082 | contents | pages [4] -->
4.1.1

<!-- b000083 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [4] -->
8

<!-- b000085 | contents | pages [4] -->
Space Daily Equilibria 1/σ2

<!-- b000086 | contents | pages [4] -->
4.1.2

<!-- b000087 | contents | pages [4] -->
s . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [4] -->
8

<!-- b000089 | contents | pages [4] -->
4.1.3

<!-- b000090 | contents | pages [4] -->
Sensitivity Analysis

<!-- b000091 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [4] -->
10

<!-- b000093 | contents | pages [4] -->
4.2

<!-- b000094 | contents | pages [4] -->
Problem2: The different effects on peak/average hours . . . . . . .

<!-- b000095 | contents | pages [4] -->
10

<!-- b000096 | contents | pages [4] -->
4.2.1

<!-- b000097 | contents | pages [4] -->
Trafﬁc Density Distribution of Time . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [4] -->
10

<!-- b000099 | contents | pages [4] -->
4.2.2

<!-- b000100 | contents | pages [4] -->
Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000101 | contents | pages [4] -->
10

<!-- b000102 | contents | pages [4] -->
4.2.3

<!-- b000103 | contents | pages [4] -->
Sensitivity Analysis

<!-- b000104 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [4] -->
13

<!-- b000106 | contents | pages [4] -->
4.3

<!-- b000107 | contents | pages [4] -->
Problem3: Dedicated lane assessment

<!-- b000108 | contents | pages [4] -->
. . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [4] -->
15

<!-- b000110 | contents | pages [4] -->
4.3.1

<!-- b000111 | contents | pages [4] -->
Sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [4] -->
16

<!-- b000113 | contents | pages [4] -->
5 Strengths and Weaknesses

<!-- b000114 | contents | pages [4] -->
17

<!-- b000115 | contents | pages [4] -->
5.1

<!-- b000116 | contents | pages [4] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000117 | contents | pages [4] -->
17

<!-- b000118 | contents | pages [4] -->
5.2

<!-- b000119 | contents | pages [4] -->
Weaknesses

<!-- b000120 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [4] -->
17

<!-- b000122 | furniture | pages [5] -->
Team # 55583

<!-- b000123 | contents | pages [5] -->
5.3

<!-- b000124 | contents | pages [5] -->
Future work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [5] -->
17

<!-- b000126 | heading | pages [5] -->
6 Conclusion

<!-- b000127 | prose | pages [5] -->
18

<!-- b000128 | heading | pages [5] -->
Appendices

<!-- b000129 | prose | pages [5] -->
20

<!-- b000130 | heading | pages [5] -->
Appendix A Cellular automata program:Moving behavior

<!-- b000131 | prose | pages [5] -->
20

<!-- b000132 | heading | pages [5] -->
Appendix B

<!-- b000133 | prose | pages [5] -->
Cellular automata program:Create new vehicles 23

<!-- b000134 | heading | pages [5] -->
Appendix C Cellular automata program:Create new vehicles considering

<!-- b000135 | prose | pages [5] -->
dedicated lanes 23

<!-- b000136 | furniture | pages [6] -->
Page 1 of 24

<!-- b000137 | furniture | pages [6] -->
Team # 55583

<!-- b000138 | heading | pages [6] -->
1 Introduction

<!-- b000139 | heading | pages [6] -->
1.1 Problem Statement

<!-- b000140 | prose | pages [6] -->
Trafﬁc capacity is limited in many regions of the United States due to the num- ber of lanes of roads. For example, in the Greater Seattle area drivers experi- ence long delays during peak trafﬁc hours because the volume of trafﬁc exceeds the designed capacity of the road networks. This is particularly pronounced on Interstates 5, 90, and 405, as well as State Route 520, the roads of particular in- terest for this problem. Self-driving, cooperating cars have been proposed as a solution to increase capacity of highways without increasing number of lanes or roads. The behavior of these cars interacting with the existing trafﬁc ﬂow and each other is not well understood at this point. Based on the road listed above in Thurston, Pierce, King, and Snohomish counties, we considered how the ef- fects would change as the percentage of self-driving cars increases from 10% to 50% to 90%, and the equilibria as well as the tipping point where performance changes markedly. Also we simulated that under what conditions, if any, should lanes be dedicated to these cars. Based on our model, we listed several practical suggestions to the local government.

<!-- b000141 | heading | pages [6] -->
1.2 Related Work

<!-- b000142 | prose | pages [6] -->
Trafﬁc ﬂow has been researched for a long time by many people.We can get some basic models about relationship among trafﬁc density, speed and through- put[5].When trafﬁc density is medium, there is a linear relationship:

<!-- b000143 | prose | pages [6] -->
traffic density Speed = Maximum Speed ∗(1 − Maximum density) (1)

<!-- b000144 | prose | pages [6] -->
When trafﬁc density is nearly full, there is a logarithmic relationship:

<!-- b000145 | prose | pages [6] -->
Speed = Maximum Speed ∗ln (Maximum density ) (2) traffic density

<!-- b000146 | prose | pages [6] -->
When trafﬁc density is very low, there is a exponential relationship:

<!-- b000147 | prose | pages [6] -->
Speed = Maximum Speed ∗(1 −exp (Maximum density )) (3) traffic density

<!-- b000148 | prose | pages [6] -->
Self-driving has entered our vision and may be popular in the future.The accu- racy and safety have been improved a lot thanks to the development of artiﬁ- cial intelligence.One of the most important point is the sensors on the vehicle[1], which can detect the motion state of the surrounding vehicles, including velocity, distance and acceleration.So, in our models, we assume that self-driving vehicles can keep the same motion state with the former one, without safe interval.

<!-- b000149 | furniture | pages [7] -->
Page 2 of 24

<!-- b000150 | furniture | pages [7] -->
Team # 55583

<!-- b000151 | heading | pages [7] -->
2 Assumptions and Notations

<!-- b000152 | heading | pages [7] -->
2.1 Assumptions

<!-- b000153 | prose | pages [7] -->
We make the following basic assumptions in order to simplify the problem. Each of our assumptions is justiﬁed and is consistent with the basic fact.

<!-- b000154 | prose | pages [7] -->
• Time consumed on the crossroads and toll on the roads is not in consid- eration. We suppose that the cars are in the same speed and ignored the wasted time due to the road conditions.

<!-- b000155 | prose | pages [7] -->
• The trafﬁc counts on the speciﬁc roads will not change after adjustment.

<!-- b000156 | prose | pages [7] -->
We presume that at certain day or certain hours the car that need to use certain road will not change because of our adjustment.

<!-- b000157 | prose | pages [7] -->
• No lane changing situation is considered. This assumption will be ex- plained in 3.1 when we illustrate the self-driving, cooperating car model.

<!-- b000158 | prose | pages [7] -->
• The capacities and sizes of different kinds of cars will not be differenti- ated. To simplify our model, we assume that all the car in our model share the same regular length 4m and regular width for one car a lane.

<!-- b000159 | heading | pages [7] -->
2.2 Notations

<!-- b000160 | prose | pages [7] -->
The notation table contains all the notations we use in this paper.

<!-- b000161 | prose | pages [7] -->
Symbol Deﬁnition Notes

<!-- b000162 | prose | pages [7] -->
vins instantaneous speed of a car tresponse equals 1s the response time of a human driver lu equals 4m unit length of a block in Cellular Automaton model nl lane counts of a certain road section d the distance between two adjacent cars LR the whole length of a certain road section Vmax equals7units/s the maximum speed that a car can reach TC TC during a day trafﬁc count during a certain time slot TC24 is a constant v car velocity tavg the average car passing time σ2 car velocity variance during different period in a day t σ2 car velocity variance among different road sections s Pself the possibility of a self-driving car to show up PNself the possibility of a non-self-driving car to show up

<!-- b000163 | caption | pages [7] -->
Table 1: Notations.

<!-- b000164 | furniture | pages [8] -->
Page 3 of 24

<!-- b000165 | furniture | pages [8] -->
Team # 55583

<!-- b000166 | heading | pages [8] -->
3 Model Construction

<!-- b000167 | heading | pages [8] -->
3.1 The self-driving, cooperating car model

<!-- b000168 | prose | pages [8] -->
From article [1] and [2], we can know that the self-driving, cooperating cars have four potential beneﬁts:

<!-- b000169 | prose | pages [8] -->
• Fewer accidents. Driverless car can dramatically reduce the accident toll due to drivers’ error.

<!-- b000170 | prose | pages [8] -->
• More productive commutes. Driverless cars would enable the unproduc- tive hours and minutes to be converted into productive work and/or leisure time. In other word, self-driving car can help reduce the useless waste on time.

<!-- b000171 | prose | pages [8] -->
• Environmental friendliness. Autonomous cars and trucks can tune their acceleration and deceleration proﬁles to reduce wasted fuel.

<!-- b000172 | prose | pages [8] -->
• Fewer trafﬁc jams. Driverless cars would be better adapted to higher vol- umes of trafﬁc, as they would be able to travel at higher speeds while keep- ing shorter distances between vehicles.

<!-- b000173 | prose | pages [8] -->
In our model, we paid special attention to the forth beneﬁt and considered a lot about the self-driving cars’ effects on trafﬁc jams.

<!-- b000174 | prose | pages [8] -->
A self-driving, cooperating car is guided by internal computers and exter- nal sensors, and it can communicate and exchange datas with other self-driving, cooperating cars as it decides what to do. In our model, we think self-driving, cooperating cars can better deal with emergent situation and almost don’t need the reaction time that human take in face of emergencies.

<!-- b000175 | prose | pages [8] -->
From article [3] we can see on the one hand, when cars pull over or over- take, they may have trouble recognizing lane markers especially in low light, bad weather, on curves, and at forks and merging lanes. On the other hand, lane change prediction of self-driving cars may not be accurate enough, and the time it will take for a complete turnover of all cars to self-driving cars makes planning for it more than a little premature. So we reasonably assume that in our model, no lane changing situation is considered.

<!-- b000176 | prose | pages [8] -->
Here is the structural difference between self-driving, cooperating cars and non-self-driving cars.

<!-- b000177 | furniture | pages [9] -->
Page 4 of 24

<!-- b000178 | furniture | pages [9] -->
Team # 55583

<!-- b000179 | prose | pages [9] -->
(a) non-self-driving car (b) self-driving car

<!-- b000180 | caption | pages [9] -->
Figure 1: The difference between self-driving and non-self-driving cars in face of

<!-- b000181 | prose | pages [9] -->
emergency situations

<!-- b000182 | prose | pages [9] -->
Deﬁnition 1. Safe interval is the shortest distance from the former car to guarantee the safety, considering the current speed and response time of a human driver. And we can compute it as follows:

<!-- b000183 | prose | pages [9] -->
safe interval = vins × tresponse (4)

<!-- b000184 | prose | pages [9] -->
When two cars’ distance is less than the safe interval, drivers will slow down and keep distance with the former car, which is just as the Figure 1(a) showed above. But for self-driving cooperating cars, they are controlled by artiﬁcial intel- ligence system and they can always react in time when the speed of the former car changes. So these cars donnot need to keep safe interval and they can just follow the former car at best, which is shown in Figure 1(b) above.

<!-- b000185 | heading | pages [9] -->
3.2 The mixed, dynamic road model

<!-- b000186 | prose | pages [9] -->
In order to better reproduce the dynamic road trafﬁc ﬂow model, we choose Cellular Automaton to simulate the Real-Time Trafﬁc of every road section. The following Figure2 shows the improved Cellular Automaton model used in our paper.

<!-- b000187 | prose | pages [9] -->
We update the model data every second. Every line in the CA represents a lane on the road. Every volume block represent a unit length to represent the length of a car and the distance between adjacent cars. As shown in Figure 2, the yellow-colored blocks represents the self-driving cars and the blue-colored blocks represent the non-self-driving cars. The following list contains all the pa- rameters and procedures in our CA based road model.

<!-- b000188 | prose | pages [9] -->
• Unit length lu: For convenience, the unit length lu = 4m, equals the length of a regular car.

<!-- b000189 | prose | pages [9, 10] -->
• Lanes count nl: Because the two directions on each road have no distinct difference, and will not disrupt each other as well. So we regard them the same in our model, and the lanes number is the addition of lane counts of these two directions.

<!-- b000190 | furniture | pages [10] -->
Page 5 of 24

<!-- b000191 | furniture | pages [10] -->
Team # 55583

<!-- b000192 | caption | pages [10] -->
Figure 2: The Cellular Automaton based road model

<!-- b000194 | prose | pages [10] -->
nl = nleft + nright (5)

<!-- b000195 | prose | pages [10] -->
• Adjacent cars distance d: we deﬁne the number of unit length between two cars the distance from the rear end of the ﬁrst car to the head of next car, namely.

<!-- b000196 | prose | pages [10] -->
d = posformer −poslatter −1 (6)

<!-- b000197 | prose | pages [10] -->
• Road section length LR: For every section of the road, the length of this section is the number of unit length.

<!-- b000198 | prose | pages [10] -->
LR = Lreal (7) lu

<!-- b000199 | prose | pages [10] -->
• Maximum speed Vmax: we deﬁne the speed by how many unit lengths the car has gone per second.Speed limit is 60 mile/h, which is about 27 m/s, namely, 7 unit length per second.Vmax = 7 units/s

<!-- b000200 | prose | pages [10] -->
• Human response time tresponse: we deﬁne human response time as the time which a person need to start to slow down the car after he or she has found emergency. Commonly, response time is from 0.3 seconds to 1.5 sec- onds.Here we deﬁne tresponse = 1

<!-- b000201 | prose | pages [10] -->
• Instantaneous velocity of cars vins: The instantaneous speed of this corre- sponding car decides how many blocks the car will move forward at next second. And the unit of vins is blocks per second

<!-- b000202 | prose | pages [10] -->
• Trafﬁc Counts TC: During some time, the amount of the cars reaching the end of road section is the TC of this road section during that long time.

<!-- b000203 | furniture | pages [11] -->
Page 6 of 24

<!-- b000204 | furniture | pages [11] -->
Team # 55583

<!-- b000205 | heading | pages [11] -->
3.3 Performance evaluation criteria

<!-- b000206 | heading | pages [11] -->
3.3.1 Car Velocity v

<!-- b000207 | prose | pages [11] -->
From the model above, the instantaneous speed is easily accessible, but the car velocity we use to evaluate the road condition is the average velocity of cars that passed the road during certain time slot. The average car velocity can well reﬂect the road performance under different conditions. The bigger the velocity is, the less crowded the road is and thus the better the road capacity is. From our model, there is a trick to get the average car velocity:

<!-- b000208 | prose | pages [11] -->
First, we count all the cars every second on the roads and sum them up.

<!-- b000209 | prose | pages [11] -->
Nsum = Σtn(per second) (8)

<!-- b000210 | prose | pages [11] -->
Then, the average car passing time is accessible.

<!-- b000211 | prose | pages [11] -->
tavg = Nsum (9) TC

<!-- b000212 | prose | pages [11] -->
v = Lreal (10) tavg

<!-- b000213 | prose | pages [11] -->
1 1

<!-- b000214 | heading | pages [11] -->
3.3.2 Daily Equilibria

<!-- b000215 | prose | pages [11] -->
t , σ2 σ2s

<!-- b000216 | prose | pages [11] -->
We evaluated the trafﬁc network equilibria from both time aspect and space as- pect.

<!-- b000217 | prose | pages [11] -->
On the one hand, for a certain road section, during a single day, including peak hours and average hours, if the car velocity keeps stable and changes little, the time daily equilibria of the trafﬁc network is obviously better.

<!-- b000218 | prose | pages [11] -->
Deﬁnition 2. Time daily equilibria.We deﬁne it as 1 ,where σ2 t is the car velocity σ2 t variance during different period in a day for a certain road section.

<!-- b000219 | prose | pages [11] -->
t = 1 σ2 mΣm(vti −¯v)2 (11)

<!-- b000220 | prose | pages [11] -->
On the other hand, at speciﬁc time slot, if the car velocities of different road sections do not distinct too much or nearly same, the space daily equilibria of the trafﬁc network is much better. Deﬁnition 3. Space daily equilibria.We deﬁne it as 1 ,where σ2 s as the car velocity σ2 s variance at same time among different road sections. In this problem, the road sections of the particularly concerned four roads is 224.

<!-- b000221 | prose | pages [11] -->
1 σ2 224Σ(vli −¯v)2 s = (12)

<!-- b000222 | furniture | pages [12] -->
Page 7 of 24

<!-- b000223 | furniture | pages [12] -->
Team # 55583

<!-- b000224 | heading | pages [12] -->
4 Model Extension and Simulation Analysis

<!-- b000225 | prose | pages [12] -->
We decomposed our simulation into three steps and corresponded them to three problems. First of all, we ignored peak hours in a day and no dedicated lanes. Secondly, we proposed the trafﬁc counts distribution during a day considering the peak hours and average hours, and applied our model into this situation. Lastly, we considered dedicated lanes’ effect and answered the question "Under what condition, if any, should lanes be dedicated to these cars".

<!-- b000226 | heading | pages [12] -->
4.1 Problem1: The effects of auto-driving cars in trafﬁc network

<!-- b000227 | prose | pages [12] -->
When peak hours are not taken into consideration, we assume that the cars come randomly at any second during a day with evenly possibilities. So if the propor- tion of the self-driving car is p, the possiblity of a self-driving car come at the start point of a road section on each lanePself is:

<!-- b000228 | prose | pages [12] -->
Pself = TC24h/24/3600 × p/lanes (13)

<!-- b000229 | prose | pages [12] -->
and for the non-self-driving car, Pnon−self is:

<!-- b000230 | prose | pages [12] -->
PNself = TC24h/24/3600 × (1 −p)/lanes (14)

<!-- b000231 | prose | pages [12] -->
The initial velocity of each car is randomly assigned among 0 to 60 mile/h, that is, the maximum speed of a car is 7units/s. Then we use the procedure showed in Figure 3 to decide how the velocity and position will change in the next second.

<!-- b000232 | prose | pages [12] -->
First, we check if there is conﬂict between adjacent cars, if there is conﬂict, the drivers or the artiﬁcial intelligence system will brake until the velocity is the same as the car in front, so in this situation, the new velocity is the same as the car in front,and the position will be closely following the former one. Meanwhile, if there is no conﬂict, check if the distance is shorter than safe interval, if not, the car controller will accelerate until the car velocity reached the maximum velocity. If the distance is within the safe interval, for non-self-driving car, the driver will decelerate considering safety, but self-driving car will still accelerating because it has the ability to adjust the speed of itself quickly according to the speed of the former car and need no response time.In other words, self-driving cars can be perfectly synchronized with the former car automatically, and need no safety interval.

<!-- b000233 | prose | pages [12] -->
Then, we simulated the whole 224 road sections for one hour long time, and repeated every simulation for 100 times to eliminate accidental error.

<!-- b000234 | furniture | pages [13] -->
Page 8 of 24

<!-- b000235 | furniture | pages [13] -->
Team # 55583

<!-- b000236 | caption | pages [13] -->
Figure 3: The ﬂow chart indicating how we decide the velocity and position of

<!-- b000237 | prose | pages [13] -->
the car in next second

<!-- b000238 | heading | pages [13] -->
4.1.1 Car Velocity/Performance v

<!-- b000239 | prose | pages [13] -->
We simulates the trafﬁc performance when the percentage of self-driving, coop- erating cars change every 5%, and the 10%, 50%, 90% is emphasized in the Figure 4.

<!-- b000240 | prose | pages [13] -->
From the result, we can safely come to the conclusion that the car velocity steadily increase as the self-driving car percentage raises.

<!-- b000241 | prose | pages [13] -->
Space Daily Equilibria 1/σ2 4.1.2 s

<!-- b000242 | prose | pages [13] -->
The trafﬁc counts distribution of time is considered, so σs t is not compared here.

<!-- b000243 | caption | pages [13] -->
Figure 5 below shows the simulation results.

<!-- b000244 | prose | pages [13] -->
Also, Figure5 shows the car velocity variance decreases steadily, which means the space daily equilibria increase as the self-driving, cooperating cars percent- age raises.

<!-- b000245 | prose | pages [13] -->
Both this two results can prove that the self-driving, cooperating car can do release the trafﬁc pressure, and help to improve the road capacity.

<!-- b000246 | furniture | pages [14] -->
Page 9 of 24

<!-- b000247 | furniture | pages [14] -->
Team # 55583

<!-- b000248 | caption | pages [14] -->
Figure 4: Car velocity v versus self-driving ratio

<!-- b000249 | caption | pages [14] -->
Figure 5: Space daily variance σ2

<!-- b000250 | prose | pages [14] -->
s versus self-driving ratio

<!-- b000251 | furniture | pages [15] -->
Page 10 of 24

<!-- b000252 | furniture | pages [15] -->
Team # 55583

<!-- b000253 | heading | pages [15] -->
4.1.3 Sensitivity Analysis

<!-- b000254 | prose | pages [15] -->
• Sensitivity of performance to self-driving ratio.With further observation of Figure 4, we can know that the change of performance is little and the difference between maximum and minimum is about 1 m/s, which is just 4% of the performance.So, performance is not sensitive to the self-driving ratio.

<!-- b000255 | prose | pages [15] -->
• Sensitivity of variance to self-driving ratio.With further observation of Figure 5, we can get that the change of variance is relatively big and the difference between maximum and minimum is about 4m2/s−2, which is about 66% of the maximum, so the variance is relatively sensitive to the self-driving ratio.

<!-- b000256 | heading | pages [15] -->
4.2 Problem2: The different effects on peak/average hours

<!-- b000257 | heading | pages [15] -->
4.2.1 Trafﬁc Density Distribution of Time

<!-- b000258 | prose | pages [15] -->
Based on the article[4], we re-deﬁned trafﬁc density here to help us ﬁgure out and make the good use of the rules of trafﬁc count distribution of time.

<!-- b000259 | prose | pages [15] -->
Deﬁnition 4. Trafﬁc Density is the ratio of the number of vehicles arriving per hour to the daily trafﬁc count.

<!-- b000260 | prose | pages [15] -->
There are two peaks every day, so we choose dual-Gaussian distribution to approximate the trafﬁc density function. Our test and veriﬁcation show that this function can well reﬂect the truly trafﬁc density function versus time.

<!-- b000261 | prose | pages [15] -->
λ 2π(e−(x−t1)2 + e−(x−t2)2  2σ2 ) √ f(x) = 2σ2   2σ  (15) Z 24  f(x) dx = 1   0

<!-- b000262 | prose | pages [15] -->
After calculation and comparasion, we got the parameters λ, σ, t1 and t2 in the function, and the function graph is shown in Figure6.

<!-- b000263 | heading | pages [15] -->
4.2.2 Simulation

<!-- b000264 | prose | pages [15] -->
Considering peak hours’ heavy trafﬁc loads, we adjust our model’s trafﬁc count parameter according to the density function given above every hour. We simu- lated 24 hours a day for the whole 224 road sections, and repeated for 20 times to eliminate accidental error. Different from the barely three criteria, we adjust our data visualization strategies to stress the changing point.

<!-- b000265 | furniture | pages [16] -->
Page 11 of 24

<!-- b000266 | furniture | pages [16] -->
Team # 55583

<!-- b000267 | caption | pages [16] -->
Figure 6: The trafﬁc density function versus time

<!-- b000268 | prose | pages [16] -->
• The real-time car velocity of 224 road sections at peak time 17:00, during our density model, the heaviest density come at 17:00, so we chose this time point to compare different trafﬁc performance when the self-driving ratio is 0%, 10%, 50% and 90%.

<!-- b000269 | prose | pages [16] -->
We abstract the four particularly pronounced roads from the map, and cor- responding every road section to a block in the graph. The road direction as well as the road length is adapted based on the fact data on the map.

<!-- b000270 | prose | pages [16] -->
In Figure 7, we use different colors to reﬂect the real-time car velocity. The lower the car velocity is, the more crowded the road is and the worse the trafﬁc performance is, meanwhile, the color is more close to "red".

<!-- b000271 | prose | pages [16] -->
As we can see from the graphs in Figure 7, self-driving, cooperating cars can distinctively reduce the trafﬁc pressure at peak hours and get a bet- ter equilibrium of space because the color becomes more uniﬁed.When the percentage of the self-driving cars reaches 50%, the trafﬁc ﬂow can proceed almost without hindrance.

<!-- b000272 | prose | pages [16] -->
• Tipping Point Observation: In our basic model in Prob.1, the ignorance of peak time will result in the car sparse, so the changing tendency is not so representative. In this part, we compared car velocity in variable density background versus self-driving ratio. Speciﬁcally speaking, we choose the presentative busy hour 17:00, the average of the road conditions during peak hours and daily average car velocity regardless of peak hours, and show its corresponding car velocity changing tendency versus self-driving ratio.

<!-- b000273 | furniture | pages [17] -->
Page 12 of 24

<!-- b000274 | furniture | pages [17] -->
Team # 55583

<!-- b000275 | prose | pages [17] -->
(a) no self-driving car (b) 10% self-driving car

<!-- b000276 | prose | pages [17] -->
(c) 50% self-driving car (d) 90%self-driving car

<!-- b000277 | caption | pages [17] -->
Figure 7: The difference between self-driving and non-self-driving cars when in

<!-- b000278 | prose | pages [17] -->
face of emergency situations

<!-- b000279 | prose | pages [17] -->
From Figure 8, especially the curve trends of the two lines of the busy roads, we can see the change is the most obvious when the self-driving car per- centage is around 45%. Therefore, only the tipping point of busy road sec- tions at peak time can be observed, and is about 45%.

<!-- b000280 | furniture | pages [18] -->
Page 13 of 24

<!-- b000281 | furniture | pages [18] -->
Team # 55583

<!-- b000282 | caption | pages [18] -->
Figure 8: The car velocity versus self-driving car percentage under different den-

<!-- b000283 | prose | pages [18] -->
sity conditions.

<!-- b000284 | prose | pages [18] -->
• In this part, we also compare Time daily equilibria and Space daily equilib- ria to illustrate what effect the self-driving, cooperating car will take to the road equilibria.

<!-- b000285 | prose | pages [18] -->
For time daily equilibria, we displayed its changing tendency with the in- crease of the self-driving car percentage. The corresponding curve is shown in Figure 9.

<!-- b000286 | prose | pages [18] -->
For space daily equilibria, we displayed its changing tendency versus time during a day when the self-driving car percentage is 10%, 50% and 90%.

<!-- b000287 | prose | pages [18] -->
The 0% line works as a reference here. The corresponding curve is shown in Figure10.

<!-- b000288 | prose | pages [18] -->
From Figure9, we can clearly observe that the σ2 t decreases as the percent- age increases, especially when the trafﬁc density is heavy, that is, espe- cially in peak hours. Also, the biggest drop come up around the tipping point 45%. From Figure10, the σ2 s decreases as the percentage increases too.

<!-- b000289 | prose | pages [18] -->
When the percentage of self-driving cars reaches 50%, the peak hours effect become less signiﬁcant.

<!-- b000290 | heading | pages [18] -->
4.2.3 Sensitivity Analysis

<!-- b000291 | prose | pages [18, 19] -->
From the results of this part, the self-driving car applied can dramatically improve the trafﬁc capacity and performance during peak hours, and for the busy roads, the tipping point come up around 45%, the percentage of the self-driving cooperating cars.Spatially, road performance is more sen- sitive to self-driving ratio during peak hours.Chronologically, road perfor- driving ratios.

<!-- b000292 | furniture | pages [19] -->
Page 14 of 24

<!-- b000293 | furniture | pages [19] -->
Team # 55583

<!-- b000294 | caption | pages [19] -->
Figure 9: The velocity variance to time versus self-driving ratio.

<!-- b000295 | caption | pages [19] -->
Figure 10: The car velocity variance to space versus time under different self-

<!-- b000297 | furniture | pages [20] -->
Page 15 of 24

<!-- b000298 | furniture | pages [20] -->
Team # 55583

<!-- b000299 | prose | pages [20] -->
mance is more sensitive to self-driving ratio at busy road sections, like In- terstate 5,milepost 163.36.

<!-- b000300 | heading | pages [20] -->
4.3 Problem3: Dedicated lane assessment

<!-- b000301 | prose | pages [20] -->
To assess the performance of dedicated lane, we added a dedicated lane to both directions of each road section. In our model, if there is a dedicated lane for self-driving, cooperating cars, these cars cannot drive on other lanes and the dedicated lane is not open for non-self-driving cars.

<!-- b000302 | prose | pages [20] -->
We simulate the performance of the road sections when two lanes are ded- icated to self-driving cars, and compare it with the performance without dedi- cated lanes.

<!-- b000303 | prose | pages [20] -->
The average car velocity performance is shown in Figure 11.

<!-- b000304 | caption | pages [20] -->
Figure 11: The car velocity versus self-driving ratio when there are lanes dedi-

<!-- b000305 | prose | pages [20] -->
cated to self-driving cars.

<!-- b000306 | prose | pages [20] -->
Also, the space daily equilibria performance is shown in Figure 12. To bet- ter represent the effects of self-driving cars, we chose the busy road to simulate instead of average road condition.

<!-- b000307 | prose | pages [20] -->
From the two ﬁgures, we can see, when the self-driving cooperating cars per- centage is less than 68%, the roads without dedicated lines have relatively bet- ter capacity and performance. However, when the percentage reaches 68%, the roads with two dedicated liens have relatively better capacity and performance.

<!-- b000308 | prose | pages [20, 21] -->
Also, we can ﬁnd that when the percentage reaches 95% or more, the perfor- lanes dedicated to self-driving cars.

<!-- b000309 | furniture | pages [21] -->
Page 16 of 24

<!-- b000310 | furniture | pages [21] -->
Team # 55583

<!-- b000311 | caption | pages [21] -->
Figure 12: The car velocity versus self-driving car percentage when there are

<!-- b000313 | prose | pages [21] -->
mance of roads with dedicated lanes declined at the same time. We think, it is because we limited the self-driving car on the dedicated lanes, and it may re- sult in the over-crowded dedicated lanes for self-driving cars. In this situation, add more lanes dedicated to self-driving, cooperating cars may get performance improve. But we did not simulate it, because of the simulation time cost.

<!-- b000314 | heading | pages [21] -->
4.3.1 Sensitivity analysis

<!-- b000315 | prose | pages [21] -->
For dedicated lanes,here we only allocate one on each road section in each direc- tion. But we ﬁnd something within our expectation.The performance is sensitive to dedicated lane number when self-driving ratio is lower than 68% because, the dedicated lanes have robbed the capacity of other lanes to serve self-driving cars, so the common lanes become more busy.Although the performance is improved by allocating a dedicated lane to each road section in each direction when self- driving ratio is higher than 68%, the performance changes little.The reason is that we only allocate one dedicated lane for self-driving vehicles and the dedicated lane becomes busy when self-driving ratio is high.

<!-- b000316 | furniture | pages [22] -->
Page 17 of 24

<!-- b000317 | furniture | pages [22] -->
Team # 55583

<!-- b000318 | heading | pages [22] -->
5 Strengths and Weaknesses

<!-- b000319 | heading | pages [22] -->
5.1 Strengths

<!-- b000320 | prose | pages [22] -->
Our model take time, space, self-driving ratio, trafﬁc density and dedicated lanes into consideration. Based on the analysis above, we list strengths of our model as follows:

<!-- b000321 | prose | pages [22] -->
• Extensibility. Our models deal with each road section independently, so we can extend them easily. For instance, given the trafﬁc density function of time over the whole year, we can get the effect of self-driving-ratio on the trafﬁc during a whole year. Furthermore, we can modify the moving behavior in 4.1 to construct a more complicated but more practical model.

<!-- b000322 | prose | pages [22] -->
Such as adding lane changing situation into consideration as the technol- ogy improved.

<!-- b000323 | prose | pages [22] -->
• Exactness. Our models deal with time using second as a unit, so, in fact, we monitor how vehicles move in a second, which improves the accuracy a lot. In addition, in our time-based model, thetrafﬁc density function of time during a day has a second-level accuracy better than minute-level or hour-level.

<!-- b000324 | prose | pages [22] -->
• Stability. Our models have some undetermined factors, like the initial speed of a vehicle. But we have veriﬁed that the results of many tests under the same conditions have little ﬂuctuation, which means a great stability.

<!-- b000325 | heading | pages [22] -->
5.2 Weaknesses

<!-- b000326 | prose | pages [22] -->
• Junctions are ignored. Actually, what happens in the junction between two road sections is very complex. We have observed that the two adjacent road sections have different trafﬁc counts, which means loss or gain of trafﬁc counts. If we could consider the initial condition and ﬁnal condition based on the junction parts, we are likely to get a more accurate model of the whole trafﬁc network.

<!-- b000327 | prose | pages [22] -->
• Switching lanes is ignored. Actually, for non-self-driving vehicles, switch- ing lanes is possible. If we try considering switching lanes, we also need to distinguish the left lanes and right lanes and vehicles can not cross the line between this two kinds of lanes.

<!-- b000328 | heading | pages [22] -->
5.3 Future work

<!-- b000329 | prose | pages [22, 23] -->
First, take junctions into consideration for higher exactness of the whole trafﬁc network. In our model, we can extend it by recording the ﬁnal condition of current road section and using it as the initial condition of the adjacent road section.

<!-- b000330 | furniture | pages [23] -->
Page 18 of 24

<!-- b000331 | furniture | pages [23] -->
Team # 55583

<!-- b000333 | prose | pages [23] -->
Second, take switching lanes into consideration. In our model, we can mod- ify the moving behavior of non-self-driving and self-driving vehicles, and add switching behavior into it.

<!-- b000334 | prose | pages [23] -->
Finally, in fact, how to determine a path over the whole road network is also different for non-self-driving and self-driving. Self-driving vehicles probably know the performance of each road section, and could select a path which costs least, while non-self-driving vehicles probably choose a path which is shortest physically but may cost more. If we add the way of searching a path into our models, they could be more practical and strong.

<!-- b000335 | prose | pages [23] -->
Since the time is limited, we are sorry that we implement little of the future work. But the future work is really worth considering. We suppose that the model can become more practical after the future work has been done.

<!-- b000336 | heading | pages [23] -->
6 Conclusion

<!-- b000337 | prose | pages [23] -->
From the simulation analysis of the model we proposed, self-driving, cooper- ating cars can do be regarded as a solution to increase capacity of highways without increasing number of lanes or roads. In particular, when the percentage of self-driving cars increases, the performance of the road capacity and perfor- mance increase as well. Especially for peak hours and busy road sections. From our simulation, we ﬁnd, for busy road or on peak hours, the capacity of the roads improve dramatically when the percentage of the self-driving, cooperating car is around 45%. And, we ﬁnd, when the self-driving-car ratio reached 68% or more, dedicating two lanes to self-driving cars can help to further improve the road capacity. But when the ratio reaches 95% or more, two dedicated lanes is not enough, the crowded car on the dedicated lanes will lower the performance.

<!-- b000338 | heading | pages [23] -->
References

<!-- b000339 | references | pages [23] -->
[1] Araujo, Luis, Katy Mason, and Martin Spring. "Self-driving cars." A case

<!-- b000340 | references | pages [23] -->
study in making new markets, London, UK: Big Innovation Centre 9 (2012).

<!-- b000341 | references | pages [23] -->
[2] Urmson, Chris. "Self-driving cars and the urban challenge." IEEE Intelligent

<!-- b000342 | references | pages [23] -->
Systems 23.2 (2008).

<!-- b000343 | references | pages [23] -->
[3] Foley, Emily. "Self-Driving Cars."

<!-- b000344 | references | pages [23] -->
[4] MuÃ´soz, Laura, et al. "Trafﬁc density estimation with the cell transmission

<!-- b000345 | references | pages [23] -->
model." American Control Conference, 2003. Proceedings of the 2003. Vol. 5.

<!-- b000346 | references | pages [23] -->
IEEE, 2003.

<!-- b000347 | furniture | pages [24] -->
Page 19 of 24

<!-- b000348 | furniture | pages [24] -->
Team # 55583

<!-- b000349 | references | pages [24] -->
[5] Serge Hoogendoorn, Victor Knoop. "The transport system and transport pol-

<!-- b000350 | references | pages [24] -->
icy." Chapter 7 "Trafﬁc ﬂow theory and modelling."

<!-- b000351 | furniture | pages [25] -->
Page 20 of 24

<!-- b000352 | furniture | pages [25] -->
Team # 55583

<!-- b000353 | heading | pages [25] -->
Appendices

<!-- b000354 | heading | pages [25] -->
Appendix A

<!-- b000355 | prose | pages [25] -->
Cellular automata program:Moving be- havior

<!-- b000356 | prose | pages [25] -->
Here is part of MATLAB simulation programs we used in our model.

<!-- b000357 | prose | pages [25] -->
Moving behavior

<!-- b000358 | prose | pages [25] -->
function [plaza,v,vmax,traffic_count]=move_forward(plaza,v,vmax,plazalength,cc);

<!-- b000359 | prose | pages [25] -->
[L,W]=size(plaza);% length and lane numbers gap=zeros(L,W);

<!-- b000360 | prose | pages [25] -->
count=cc;

<!-- b000361 | prose | pages [25] -->
t_response=1;%response time 1s v_pre=0;

<!-- b000362 | prose | pages [25] -->
for lanes=2:W-1;

<!-- b000363 | prose | pages [25] -->
temp=find(plaza(1:L,lanes)>=1);

<!-- b000364 | prose | pages [25] -->
nn=length(temp);% The number of the cars in the lane for k=1:nn;

<!-- b000365 | prose | pages [25] -->
i=temp(k);

<!-- b000366 | prose | pages [25] -->
if(k==nn) gap(i,lanes)=999;

<!-- b000367 | prose | pages [25] -->
continue;

<!-- b000368 | prose | pages [25] -->
end gap(i,lanes)=temp(k+1)-temp(k)-1;

<!-- b000369 | prose | pages [25] -->
end end

<!-- b000370 | prose | pages [25] -->
for lanes=2:W-1;

<!-- b000371 | prose | pages [25] -->
temp=find(plaza(1:L,lanes)>0);

<!-- b000372 | prose | pages [25] -->
nn=length(temp);

<!-- b000373 | prose | pages [25] -->
temp=flipud(temp);%from end if(nn>0) i=temp(1);

<!-- b000374 | prose | pages [25] -->
pos=i+v(i,lanes);

<!-- b000375 | prose | pages [25] -->
temp(1)=pos;

<!-- b000376 | prose | pages [25] -->
v_pre=v(i,lanes);

<!-- b000377 | prose | pages [25] -->
if(plaza(i,lanes)==1)%common car need to consider safety if(pos>plazalength) count=count+1;

<!-- b000378 | prose | pages [25] -->
plaza(i,lanes)=0;

<!-- b000379 | prose | pages [25] -->
v(i,lanes)=0;

<!-- b000380 | prose | pages [25] -->
vmax(i,lanes)=0;

<!-- b000381 | prose | pages [25] -->
else plaza(pos,lanes)=plaza(i,lanes);

<!-- b000382 | prose | pages [25] -->
v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes));

<!-- b000383 | prose | pages [25] -->
vmax(pos,lanes)=vmax(i,lanes);

<!-- b000384 | prose | pages [25] -->
plaza(i,lanes)=0;

<!-- b000385 | prose | pages [25] -->
v(i,lanes)=0;

<!-- b000386 | prose | pages [25] -->
vmax(i,lanes);

<!-- b000387 | prose | pages [25, 26] -->
end end if(plaza(i,lanes)==2)%Self-driving car speed up if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v(i,lanes)=0; vmax(i,lanes)=0; end end end

<!-- b000388 | furniture | pages [26] -->
Page 21 of 24

<!-- b000389 | furniture | pages [26] -->
Team # 55583

<!-- b000391 | prose | pages [26] -->
for k=2:nn;%from end i=temp(k); j=temp(k-1); if(v(i,lanes)<=j-i-1)%no conflict pos=i+v(i,lanes); temp(k)=pos; safety_dis=v(i,lanes)*t_response; if(plaza(i,lanes)==1)%common car need to consider safety if(safety_dis>gap(i,lanes))%not safe %disp(’not safe’); if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v_pre=max(v(i,lanes)-1,1); v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=max(v(i,lanes)-1,1); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; end else%if safe, accelerate %disp(’safe’); if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v_pre=v(i,lanes);%record the v before moving v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); vmax(pos,lanes)=vmax(i,lanes);

<!-- b000392 | furniture | pages [27] -->
Page 22 of 24

<!-- b000393 | furniture | pages [27] -->
Team # 55583

<!-- b000394 | prose | pages [27] -->
plaza(i,lanes)=0; v_pre=v(i,lanes);%record the v before moving v(i,lanes)=0; vmax(i,lanes)=0; end

<!-- b000395 | prose | pages [27] -->
end end if(plaza(i,lanes)==2)%self-driving car accelerate if(pos>plazalength) %plaza(pos,lanes)=plaza(i,lanes); %v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); %vmax(pos,lanes)=vmax(i,lanes) count=count+1; plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); v(pos,lanes)=min(v(i,lanes)+1,vmax(i,lanes)); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; end end else% conflict pos=j-1;%move next to the former car temp(k)=pos; if(pos>plazalength) count=count+1; plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; else plaza(pos,lanes)=plaza(i,lanes); if(j<=plazalength) v(pos,lanes)=v(j,lanes); else v(pos,lanes)=v(i,lanes); end %v(pos,lanes)=v(i,lanes); vmax(pos,lanes)=vmax(i,lanes); plaza(i,lanes)=0; v_pre=v(i,lanes); v(i,lanes)=0; vmax(i,lanes)=0; end end end end traffic_count=count;

<!-- b000396 | furniture | pages [28] -->
Page 23 of 24

<!-- b000397 | furniture | pages [28] -->
Team # 55583

<!-- b000398 | prose | pages [28] -->
end

<!-- b000399 | heading | pages [28] -->
Appendix B

<!-- b000400 | prose | pages [28] -->
Cellular automata program:Create new vehicles

<!-- b000401 | prose | pages [28] -->
Here is part of our simulation programs we used in our model.

<!-- b000402 | prose | pages [28] -->
Generate new vehicles

<!-- b000403 | prose | pages [28] -->
function [plaza,v,vmax]=new_cars(plaza_1,v_1,vmax_1,probc,probv,max_speed);

<!-- b000404 | prose | pages [28] -->
[L,W]=size(plaza_1);

<!-- b000405 | prose | pages [28] -->
plaza=plaza_1;

<!-- b000406 | prose | pages [28] -->
v=v_1;

<!-- b000407 | prose | pages [28] -->
vmax=vmax_1;

<!-- b000408 | prose | pages [28] -->
for lanes=2:W-1;

<!-- b000409 | prose | pages [28] -->
if(rand<=probc) %generate a car for a lane according to time distribution %disp(rand);

<!-- b000410 | prose | pages [28] -->
if(rand<probv(1)) %generate a self-driving vehicle in possibility p plaza(1,lanes)=2;

<!-- b000411 | prose | pages [28] -->
vmax(1,lanes)=max_speed;

<!-- b000412 | prose | pages [28] -->
v(1,lanes)=round(rand*7)+1;%random initial speed else %generate a non-self-driving vehicle in possibility 1-p plaza(1,lanes)=1;

<!-- b000413 | prose | pages [28] -->
vmax(1,lanes)=max_speed;

<!-- b000414 | prose | pages [28] -->
v(1,lanes)=round(rand*7)+1;%random initial speed end end end end

<!-- b000415 | heading | pages [28] -->
Appendix C

<!-- b000416 | prose | pages [28] -->
Cellular automata program:Create new vehicles considering dedicated lanes

<!-- b000417 | prose | pages [28] -->
Here is part of our simulation programs we used in our model.

<!-- b000418 | prose | pages [28] -->
Generate new vehicles

<!-- b000419 | prose | pages [28] -->
function [plaza,v,vmax]=new_cars(plaza_1,v_1,vmax_1,probc,probv,max_speed,dedicated_nu [L,W]=size(plaza_1);

<!-- b000420 | prose | pages [28] -->
plaza=plaza_1;

<!-- b000421 | prose | pages [28] -->
v=v_1;

<!-- b000422 | prose | pages [28] -->
vmax=vmax_1;

<!-- b000423 | prose | pages [28] -->
for lanes=2:W-1;

<!-- b000424 | prose | pages [28, 29] -->
if(lanes<2+dedicated_num)%dedicated lanes for self-driving if(rand<(probc*(W-2)/dedicated_num*probv(1))) plaza(1,lanes)=2; vmax(1,lanes)=max_speed; v(1,lanes)=round(rand*7)+1; end else %common lanes for non-self-driving vehicles if(rand<(probc*(W-2)/(W-2-dedicated_num)*(1-probv(1)))) plaza(1,lanes)=1; vmax(1,lanes)=max_speed; v(1,lanes)=round(rand*7)+1; end end end end

<!-- b000425 | furniture | pages [29] -->
Page 24 of 24

<!-- b000426 | furniture | pages [29] -->
Team # 55583
