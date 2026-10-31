# P-A-2022-2216547-e72f44f2

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2022

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
A

<!-- b000005 | title | pages [1] -->
2216547

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Optimal Cycling Solution Based on Physiology,

<!-- b000008 | title | pages [1] -->
Newtonian Mechanics and Dynamic Programming

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In this paper, we want to figure out the power curves of different riders and how riders can allocate their power during the course to get better performance in an individual time trial competition.

<!-- b000011 | prose | pages [1] -->
To begin with, We design the Muscle Fatigue-Recovery Model and the Energy Reserve Model, and combine them to obtain the Rider Power Output Model. Then, we use the data from the "maximum-effort" experiment in [4] [5] to adjust the model parameters. After that, we take both male and female of Time Trial Specialist(TTS) and Sprinter as examples, obtaining their power curves by using our model.

<!-- b000012 | prose | pages [1] -->
Next, We collect the coordinate information of real-world road points from Google Earth, to build a data structure of roads and define its attribute fields to re-express the road elevation, length, curvature and other attributes in the computer. Thus the bike course can be visualized.

<!-- b000013 | prose | pages [1] -->
Then, using the bike course information, we model the Newtonian mechanics of the bicycle and established the equations of motion of the rider based on Newton’s second law.

<!-- b000014 | prose | pages [1] -->
Later, based on these three models, we formally define the power planning optimization problem. The optimal solution of this problem is found by dynamic programming algorithm.

<!-- b000015 | prose | pages [1] -->
Furthermore, based on this model, we add the environmental factors of wind speed, wind direction, and the ground humidity. Besides, we investigate the effect of the rider on the execution error of the plan.

<!-- b000016 | prose | pages [1] -->
Finally, we modified the parameters of the previous model to simulate Team Time Trials, in which teams often use the "mountain train" tactic: the team members line up to minimize overall air resistance by finding information and processing data in [13].

<!-- b000017 | prose | pages [1] -->
Based on the above modeling, we can draw the following conclusions:

<!-- b000018 | prose | pages [1] -->
1. For a relatively undulating section of road, the optimal power planning plan for the Sprinter is to power up at the beginning and on uphill section, and to ride at a lower power on the relatively gentle sections of road to preserve energy. For the TTS, the opposite is true.

<!-- b000019 | prose | pages [1] -->
2. Gender makes no significant difference to the above strategy.

<!-- b000020 | prose | pages [1] -->
3. Higher ground humidity and stronger headwinds will lengthen the time for riders to finish the race, while lower ground humidity and stronger tailwinds will shorten the time.

<!-- b000021 | prose | pages [1] -->
4. If a riders do not follow a highly detailed plan and miss the power targets, their finishing time will be longer.

<!-- b000022 | prose | pages [1] -->
5. In Team Time Trials, thanks to the "mountain-train" strategy used in the team competition, the average wind resistance for each rider is reduced, allowing the team to move at a faster pace.

<!-- b000023 | keywords | pages [1] -->
Keywords: Power Curve; Newtonian mechanics; Dynamic Programming; Cycling

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1 Introduction

<!-- b000026 | contents | pages [2] -->
2

<!-- b000027 | contents | pages [2] -->
1.1

<!-- b000028 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
2

<!-- b000030 | contents | pages [2] -->
1.2

<!-- b000031 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
2

<!-- b000033 | contents | pages [2] -->
1.3

<!-- b000034 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
2

<!-- b000036 | contents | pages [2] -->
2 Assumptions and Justification

<!-- b000037 | contents | pages [2] -->
3

<!-- b000038 | contents | pages [2] -->
3 Notations

<!-- b000039 | contents | pages [2] -->
4

<!-- b000040 | contents | pages [2] -->
4 Our Model

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
4.1

<!-- b000043 | contents | pages [2] -->
Rider Power Output Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
4

<!-- b000045 | contents | pages [2] -->
4.1.1

<!-- b000046 | contents | pages [2] -->
Muscle Fatigue-Recovery Model . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
5

<!-- b000048 | contents | pages [2] -->
4.1.2

<!-- b000049 | contents | pages [2] -->
Energy Reserve Model . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
6

<!-- b000051 | contents | pages [2] -->
4.1.3

<!-- b000052 | contents | pages [2] -->
Parameter Rectification . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
7

<!-- b000054 | contents | pages [2] -->
4.1.4

<!-- b000055 | contents | pages [2] -->
Power Curve

<!-- b000056 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
8

<!-- b000058 | contents | pages [2] -->
4.2

<!-- b000059 | contents | pages [2] -->
Roads Discretization and Virtualization

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
9

<!-- b000062 | contents | pages [2] -->
4.2.1

<!-- b000063 | contents | pages [2] -->
Discretization of the Cycling Courses . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
10

<!-- b000065 | contents | pages [2] -->
4.2.2

<!-- b000066 | contents | pages [2] -->
The Data Structure Definition of the Road . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
11

<!-- b000068 | contents | pages [2] -->
4.2.3

<!-- b000069 | contents | pages [2] -->
Radius of Curvature Definitions of Points and Roads . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
11

<!-- b000071 | contents | pages [2] -->
4.3

<!-- b000072 | contents | pages [2] -->
Newtonian mechanics analysis of cycling

<!-- b000073 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
12

<!-- b000075 | contents | pages [2] -->
4.3.1

<!-- b000076 | contents | pages [2] -->
Cycling on a straight course

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
12

<!-- b000079 | contents | pages [2] -->
4.3.2

<!-- b000080 | contents | pages [2] -->
Cycling on a curved course . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
13

<!-- b000082 | contents | pages [2] -->
4.4

<!-- b000083 | contents | pages [2] -->
Formalization and Numerical Solution of the Optimizing Problem . . . . . . .

<!-- b000084 | contents | pages [2] -->
13

<!-- b000085 | contents | pages [2] -->
4.4.1

<!-- b000086 | contents | pages [2] -->
Formalization of the Problem

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
13

<!-- b000089 | contents | pages [2] -->
4.4.2

<!-- b000090 | contents | pages [2] -->
Numerically Solving the Optimizing Problem Using Dynamic Program-

<!-- b000091 | contents | pages [2] -->
ming

<!-- b000092 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
14

<!-- b000094 | contents | pages [2] -->
4.4.3

<!-- b000095 | contents | pages [2] -->
Complexity Analysis of Dynamic Programming Solution . . . . . . . .

<!-- b000096 | contents | pages [2] -->
15

<!-- b000097 | contents | pages [2] -->
5 Results

<!-- b000098 | contents | pages [2] -->
15

<!-- b000099 | contents | pages [2] -->
5.1

<!-- b000100 | contents | pages [2] -->
The Power Profiles of Time Trail Specialist and Sprinter of Different Genders .

<!-- b000101 | contents | pages [2] -->
15

<!-- b000102 | contents | pages [2] -->
5.2

<!-- b000103 | contents | pages [2] -->
Power Distribution for Various Courses

<!-- b000104 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
16

<!-- b000106 | contents | pages [2] -->
5.2.1

<!-- b000107 | contents | pages [2] -->
2021 Olympic Time Trial course in Tokyo, Japan . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
16

<!-- b000109 | contents | pages [2] -->
5.2.2

<!-- b000110 | contents | pages [2] -->
2021 UCI World Championship Time Trial Course and The Course We

<!-- b000111 | contents | pages [2] -->
Designed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [2] -->
17

<!-- b000113 | contents | pages [2] -->
5.3

<!-- b000114 | contents | pages [2] -->
Result Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000115 | contents | pages [2] -->
18

<!-- b000116 | contents | pages [2] -->
5.4

<!-- b000117 | contents | pages [2] -->
Potential Impact of Weather Conditions

<!-- b000118 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
18

<!-- b000120 | contents | pages [2] -->
5.4.1

<!-- b000121 | contents | pages [2] -->
Wind . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [2] -->
18

<!-- b000123 | contents | pages [2] -->
5.4.2

<!-- b000124 | contents | pages [2] -->
Ground Humidity . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [2] -->
18

<!-- b000126 | contents | pages [2] -->
5.5

<!-- b000127 | contents | pages [2] -->
Sensitivity of the Results to Rider Deviations from the Target Power Distribution 19

<!-- b000128 | contents | pages [2] -->
5.6

<!-- b000129 | contents | pages [2] -->
Result of Team Time Trial

<!-- b000130 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000131 | contents | pages [2] -->
19

<!-- b000132 | contents | pages [2] -->
6 Strength and Weakness

<!-- b000133 | contents | pages [2] -->
21

<!-- b000134 | contents | pages [2] -->
6.1

<!-- b000135 | contents | pages [2] -->
Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000136 | contents | pages [2] -->
21

<!-- b000137 | contents | pages [2] -->
6.2

<!-- b000138 | contents | pages [2] -->
Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000139 | contents | pages [2] -->
21

<!-- b000140 | contents | pages [2] -->
Reference

<!-- b000141 | contents | pages [2] -->
21

<!-- b000142 | contents | pages [2] -->
1

<!-- b000143 | furniture | pages [3] -->
Team # 2216547

<!-- b000144 | furniture | pages [3] -->
Page 2

<!-- b000145 | heading | pages [3] -->
1 Introduction

<!-- b000146 | heading | pages [3] -->
1.1 Problem Background

<!-- b000147 | prose | pages [3] -->
Cycling races are very popular worldwide, especially The Individual Time Trials (ITTs) and The Team Time Trials (TTTs), ITTs are also referred to as "the race of truth", as winning depends on each rider’s strength and endurance, and also depend on how well the rider distributes the power according to roads conditions. In order to make the rider get better results, it is very important to analyze how rider with different physical conditions (physical energy reserve, physical recovery ability, explosive ability, etc.) for riding scientifically and rationally in different road conditions by mathematical modeling.

<!-- b000148 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000149 | prose | pages [3] -->
1) Firstly we are required to establish a model about the riders according to riders’ physical attributes, and the model can output the power curve of the rider which indicates how long a rider can produce a given amount of power.

<!-- b000150 | prose | pages [3] -->
2) After modeling the riders themselves, we need to model how should that rider apply power while traversing a given time trial course. To solve this problem, we should consider road conditions, environmental factors, and the rider’s own model.

<!-- b000151 | prose | pages [3] -->
3) After this we should consider the variation of results obtained when the rider performs deviations from our model.

<!-- b000152 | prose | pages [3] -->
4) Finally we need to solve the Team Time Trials situation in our model.

<!-- b000153 | prose | pages [3] -->
In order to solve those problems, we will proceed as follows:

<!-- b000154 | prose | pages [3] -->
• Design the Rider Power Output Model. We design the Rider Power Output Model and rectify the parameters of the model

<!-- b000155 | prose | pages [3] -->
• Discrete and Visualize the Roads. We get the data of roads from Google Earth, and then discrete them into segments and visualize them with the help of Python.

<!-- b000156 | prose | pages [3] -->
• Design the Newtonian Mechanics of Cycling. By analyzing the physical model of the bicycle and combining it with the two-point environmental data of the track, we propose the Newtonian mechanics of cycling.

<!-- b000157 | prose | pages [3] -->
• Solving problems using dynamic programming. The cycling time trial speeding strat- egy as an optimal control problem and used dynamic programming to solve this optimal control problem.

<!-- b000158 | prose | pages [3] -->
• Modify Model Parameters to Fit Different Problems. We modify our model parameters to simulate the performance of athletes in different environmental conditions. Similarly, we modify our model parameters to simulate the team performance in a team competition.

<!-- b000159 | heading | pages [3] -->
1.3 Literature Review

<!-- b000160 | prose | pages [3, 4] -->
Over the decades, scientists have done a lot of work to understand the physiological concepts behind the athletic performance of riders. Among them, the concepts of critical power (CP) and anaerobic work capacity (AWC) have been frequently discussed in recent articles on the subject, and there are also articles proposing more classical models of muscle fatigue and recovery based on CP and AWC[1]. Not only that, some articles have proposed a muscle fatigue recovery model based on static force derivation[2]. In addition, the power output model based on the physical performance of cyclists also has some validity[3].

<!-- b000161 | furniture | pages [4] -->
Team # 2216547

<!-- b000162 | furniture | pages [4] -->
Page 3

<!-- b000164 | prose | pages [4] -->
Scientists have not only worked on human muscle models, but also in the area of human data measurement. Dajo Sanders et al. used data from professional cyclists on a World Cycling Tour team. They used maximal aerobic force, peak sprint force output, and an exponential constant describing the decay of force over time to establish force-duration relationships for each participant [4]. N. J. Rehrer et al. measured EI (energy intake) and EE (energy expenditure) of athletes in a six-day, 10-stage cycling race [3]. Tammie R. Ebert et al. collected power output data from 31 Australian national male road cyclists over 6 years and 207 races and subjected the subjects to a maximum graded exercise test in the laboratory to determine maximum aerobic power output [5].

<!-- b000165 | prose | pages [4] -->
S. Alireza Fayazi et al. described the cycling time trial speeding strategy as an optimal control problem and used dynamic programming to solve this optimal control problem [2]. Dy- namic programming is both a mathematical optimization method and a computer programming method. The method was developed by Richard Bellman in the 1950s. Dynamic programming refers to simplifying complex problems by decomposing them into simpler subproblems in a recursive manner [6].

<!-- b000166 | heading | pages [4] -->
2 Assumptions and Justification

<!-- b000167 | prose | pages [4] -->
In order to simplify the problem and make it convenient for us to simulate the real conditions, we make the following assumptions, and each of them is properly justified.

<!-- b000168 | prose | pages [4] -->
• All the data we have collected are accurate. The data we collect through various means are measured in different environments, at different times, and on different tracks, and are inevitably interfered with by errors caused by variables that have not been taken into account. Also, the equipment used to measure these data cannot be completely free of measurement errors. So in our model, we assume that all the data we collect are accurate.

<!-- b000169 | prose | pages [4] -->
• At the beginning of a competition, the athletes always reach their optimal initial physical condition. The initial physical state of a rider at the beginning of a race is not necessarily always the most initial physical state he or she can achieve due to the effects of the rider’s sleep and diet in the days leading up to the race. This uncertainty is troublesome for modeling purposes. In our model, we assume that at the beginning of the race, the athlete always reaches his or her optimal initial body state.

<!-- b000170 | prose | pages [4] -->
• The athletes always choose the most suitable bike gear for the current road. Choosing larger gears on a flat road is inefficient, and choosing smaller gears on a ramp is time- consuming and laborious. A more reasonable approach is to select smaller gears on a flat road and larger gears on a ramp. In our model, we assume that the rider can always choose the corresponding most available gear on different sections of road.

<!-- b000171 | prose | pages [4] -->
• No unexpected situations arise during the athletes’ competition. We assume that our simulated athletes are not unwell, fallen or injured during the race. We assume that our athletes finished the race under ideal conditions.

<!-- b000172 | furniture | pages [5] -->
Team # 2216547

<!-- b000173 | furniture | pages [5] -->
Page 4

<!-- b000174 | prose | pages [5] -->
• The environmental parameters are constant over the course of the competition.

<!-- b000175 | prose | pages [5] -->
Some bike races last for hours or even days, during which the weather and environment may change significantly, such as rain versus sunshine. But we assume in our model that the environmental parameters are constant during the race.

<!-- b000176 | prose | pages [5] -->
• Male and female riders finish the same number of laps. In order to compare the performance of male and female riders on the same course, we assume that male and female riders finish the same number of laps.

<!-- b000177 | heading | pages [5] -->
3 Notations

<!-- b000178 | heading | pages [5] -->
Symbols

<!-- b000179 | prose | pages [5] -->
Description Unit

<!-- b000180 | prose | pages [5] -->
Pmax W The maximum power can be released by the muscle at the current state

<!-- b000181 | prose | pages [5] -->
Pmax0 W The maximum power can be released by the muscle at the initial state

<!-- b000182 | prose | pages [5] -->
Prider W The output power of the rider at the current time

<!-- b000183 | prose | pages [5] -->
kf 1 Muscle fatigue coefficient

<!-- b000184 | prose | pages [5] -->
kr 1 Muscle recovery coefficient

<!-- b000185 | prose | pages [5] -->
E J body energy reserves at the current time

<!-- b000186 | prose | pages [5] -->
E0 J Initial body energy reserves

<!-- b000187 | prose | pages [5] -->
Pin W Energy recovery rate

<!-- b000188 | prose | pages [5] -->
Pout W Energy output rate

<!-- b000189 | prose | pages [5] -->
kin 1 Energy recovery coefficient

<!-- b000190 | prose | pages [5] -->
mb, mr, mt kg Mass of the bicycle, the rider and the total mass of them

<!-- b000191 | prose | pages [5] -->
kwheel 1 Bicycle power conversion coefficient m2 A Frontal area of the rider

<!-- b000192 | prose | pages [5] -->
Cd 1 Air drag coefficient

<!-- b000193 | prose | pages [5] -->
v m/s Velocity of the rider kg/m3 ρ Air density

<!-- b000194 | prose | pages [5] -->
µ 1 Rolling friction coefficient

<!-- b000195 | prose | pages [5] -->
θ rad The inclination angle of a road

<!-- b000196 | prose | pages [5] -->
where we define the main parameters while specific value of those parameters will be given later.

<!-- b000197 | heading | pages [5] -->
4 Our Model

<!-- b000198 | heading | pages [5] -->
4.1 Rider Power Output Model

<!-- b000199 | prose | pages [5, 6] -->
The power output of a cyclist during a race is determined by a variety of factors, such as the athlete’s sleep, diet, mood, muscle state (maximum power output, fatigue resistance, fatigue recovery ability, etc.), fitness state (initial fitness, fitness recovery ability), weather and temperature at the time of the race, etc. Therefore, for such a complex human power output system, we consider it in two combined single models: muscle fatigue-recovery model and human energy reserve model. We rectify the parameters of our model with data from real athletes, and finally obtain the power curves of different athletes. The power curves of athletes obtained from our model overlap well with the power curves of real athletes.

<!-- b000200 | furniture | pages [6] -->
Team # 2216547

<!-- b000201 | furniture | pages [6] -->
Page 5

<!-- b000203 | heading | pages [6] -->
4.1.1 Muscle Fatigue-Recovery Model

<!-- b000204 | prose | pages [6] -->
The main power generating muscles of cyclists are the quadriceps, gluteus maximus and gluteus medius, as shown in the figure. The maximum power that can be exerted by pedaling a bicycle is a decreasing function of the level of muscle fatigue. In this paper, we use a single-state dynamic model to capture changes in the maximum power that can be output by an athlete’s current muscles. The results of [7] justify the integration of the effects of the major physiological factors that contribute to fatigue.

<!-- b000205 | caption | pages [6] -->
Figure 1: The main power generating muscles of cyclists

<!-- b000206 | prose | pages [6] -->
We assume that Pmax is the maximum power that the athlete’s muscles can output in the current state, and its initial value is Pmax0 (i.e., the amount of maximum power that the athlete can output in the best condition of the muscles), and Prider is the current power output of the athlete’s muscles. The larger Prider is, the faster the athlete’s muscles fatigue, and the faster Pmax reduces. The results of several experiments in [8] support the following model:

<!-- b000207 | prose | pages [6] -->
dPmax(t) = −kf · Pmax(t) · Prider(t) (1) dt Pmax0 fatigue Where kf is the muscle fatigue resistance coefficient, and kf varies for each individual.

<!-- b000208 | prose | pages [6] -->
Muscle recovery also increases almost exponentially and the muscle recovery process can be represented by the following model [8]:

<!-- b000209 | prose | pages [6] -->
dPmax(t) = kr · (Pmax0 −Pmax(t)) (2) dt recovery Where kr is the muscle fatigue recovery coefficient, and kr varies for each individual.

<!-- b000210 | prose | pages [6, 7] -->
However, the fatigue and recovery of an athlete’s muscles are not completely separated in time. Each time a group of muscle fibers is in activation mode, some will fatigue and some will recover[2]. In other words, muscle fatigue and recovery occur simultaneously. To reflect this simultaneous occurrence, we combine equations (1) and (2) to obtain the muscle fatigue-recovery model:

<!-- b000211 | furniture | pages [7] -->
Team # 2216547

<!-- b000212 | furniture | pages [7] -->
Page 6

<!-- b000214 | prose | pages [7] -->
dPmax(t) = −kf · Pmax(t) · Prider(t) + kr · (Pmax0 −Pmax(t)) (3) dt Pmax0

<!-- b000215 | caption | pages [7] -->
Figure 2: The Relationship between Pmax0 , Pmax(t) and Prider(t)(handwriting for explanation)

<!-- b000216 | heading | pages [7] -->
4.1.2 Energy Reserve Model

<!-- b000217 | caption | pages [7] -->
Figure 3: Schematic diagram of the capacity storage model

<!-- b000218 | prose | pages [7] -->
We know that the body’s blood sugar levels fluctuate within a certain range during human exercise. Blood sugar is the main source of energy for aerobic exercise, such as cycling. As blood sugar is consumed, liver glycogen is broken down into blood sugar to increase blood sugar levels. At the same time, it is common sense that a cycling race will not deplete the athlete’s liver glycogen. Thus, the blood glucose concentration can be stabilized within a certain range during the race. As a result, we designed the following energy reserve model:

<!-- b000219 | prose | pages [7, 8] -->
Pin(t) = kin · (Pmax0 −Pmax(t)) (4) Pout(t) = Prider(t) + Pother(t) = kout · Prider(t) (5)

<!-- b000220 | furniture | pages [8] -->
Team # 2216547

<!-- b000221 | furniture | pages [8] -->
Page 7

<!-- b000223 | prose | pages [8] -->
Z t Z t Pin(t)dt − E(t) = E0 + Pout(t)dt (6) 0 0 Where E is the total amount of directly usable energy, which can be used to represent blood sugar concentration, and E0 is its initial value, i.e. the total amount of energy directly usable by the athlete after sufficient rest; Pin is the rate of energy replenishment, which can be used to represent the rate of hepatic glycogen breakdown; Pout is the rate of energy output, which can be used to represent the rate of blood sugar consumption; and Pother is the power of energy consumed by the athlete for physiological activities other than mechanical output.

<!-- b000224 | prose | pages [8] -->
The interpretation of equation (4) is that the rate of energy replenishment is proportional to the degree of muscle fatigue, where kin is the energy replenishment coefficient.

<!-- b000225 | prose | pages [8] -->
The interpretation of equation (5) is that the energy output rate of the athlete consists of the mechanical output rate of the muscles and the rate of energy consumption by other physiological activities. Pout is approximately proportional to Prider throughout the course of the competition, and kout is this proportional parameter.

<!-- b000226 | prose | pages [8] -->
The athlete’s output power is determined by both the muscle fatigue-recovery model and the energy reserve model.

<!-- b000227 | prose | pages [8] -->
(1) When the athlete’s muscles are fatigued and energy reserves are abundant, the maximum output power of the athlete’s muscles is limited by the degree of muscle fatigue.

<!-- b000228 | prose | pages [8] -->
(2) When the athlete’s muscle energy reserves are depleted and the muscle is not too fatigued, the maximum output power of the athlete’s muscle is limited by the energy reserves.

<!-- b000229 | caption | pages [8] -->
Figure 4 shows the effect of the muscle fatigue-recovery model and the energy reserve model

<!-- b000230 | prose | pages [8] -->
working together. The blue curve is the power curve of the athlete with more abundant energy reserves, and we can see that the maximum power output of this athlete is limited only by the degree of muscle fatigue (no point where the curve turns); the orange curve is the power curve of the athlete with average energy reserves, and the maximum power output of this athlete is determined by the degree of muscle fatigue at shorter times. The green curve is the power curve of an athlete with low energy reserves, whose muscle output rate is limited by energy reserves for a shorter period of time than the previous athlete (the point at which the curve turns is smaller).

<!-- b000231 | heading | pages [8] -->
4.1.3 Parameter Rectification

<!-- b000232 | prose | pages [8] -->
In our model, an athlete’s ability can be represented by six parameters in full: kf, Pmax0, kr, E0, kin, kout. In order to obtain different model representations for different athletes, we design different parameters for different athletes. We used data from the "Maximum-Effort" experiment in [4] to design the parameters: the "Maximum-Effort" experiment refers to an athlete sprinting with all his or her strength on a flat section of road after a full rest and recording the athlete’s power output during the process. We found the parameters that best fit the data from the actual athlete’s "Maximal-Effort" experiment and recorded them as follows:

<!-- b000233 | furniture | pages [9] -->
Team # 2216547

<!-- b000234 | furniture | pages [9] -->
Page 8

<!-- b000235 | caption | pages [9] -->
Figure 4: Power Curve for riders with different E0

<!-- b000236 | caption | pages [9] -->
Table 1: Parameters for different athletes

<!-- b000237 | prose | pages [9] -->
kf kr kin kout Pmax0(J) E0(J) type 106 TTS(male) 0.0416 0.0104 1.11 1.50 1000 8 ×105 TTS(female) 0.018 0.00901 1.18 1.46 900 106 Sprinter(male) 0.057 0.001078 0.50 1.57 1500 8 ×105 Sprinter(female) 0.046 0.0009 0.53 1.52 1300

<!-- b000238 | heading | pages [9] -->
4.1.4 Power Curve

<!-- b000239 | prose | pages [9] -->
The power curve represents the maximum power that the rider can maintain for a given length of time. We obtained the power curves for different types of athletes using the following algorithm.

<!-- b000240 | prose | pages [9] -->
Algorithm idea: constant output power P, find the maximum length of time that the athlete can adhere to this power output.

<!-- b000241 | furniture | pages [10] -->
Team # 2216547

<!-- b000242 | furniture | pages [10] -->
Page 9

<!-- b000243 | heading | pages [10] -->
Algorithm 1 Draw the Power Curve

<!-- b000244 | prose | pages [10] -->
Input: kf , kr , kin , kout , Pmax0(J) , E0(J): Parameters for the athlete Output: the Power Curve of the athlete 1: tlist=[] 2: Prider_list=[] 3: for Prider = 100; Prider < 1500;Prider + + do E = E0 4:

<!-- b000245 | prose | pages [10] -->
for i = 1; i < 800; i + + do 5:

<!-- b000246 | prose | pages [10] -->
update the value of Pmax 6:

<!-- b000247 | prose | pages [10] -->
update the value of E 7:

<!-- b000248 | prose | pages [10] -->
if Prider > Pmax or E < 0 then 8:

<!-- b000249 | prose | pages [10] -->
t = i 9:

<!-- b000250 | prose | pages [10] -->
break 10:

<!-- b000251 | prose | pages [10] -->
end if 11:

<!-- b000252 | prose | pages [10] -->
end for 12:

<!-- b000253 | prose | pages [10] -->
tlist.append(t) 13:

<!-- b000254 | prose | pages [10] -->
Prider_list.append(Prider) 14: 15: end for 16: plot(tlist, Prider_list)

<!-- b000255 | caption | pages [10] -->
Figure 5: Power Curve for different riders

<!-- b000256 | heading | pages [10] -->
4.2 Roads Discretization and Virtualization

<!-- b000257 | prose | pages [10] -->
For Applying our model to various time trial courses, we built discrete virtual courses using data from two real-world cycling courses in Fig.6, the 2021 Olympic Time Trial course in Tokyo, Japan and the 2021 UCI World Championship time trial course in Flanders, Belgium in Fig.7, and we designed a reasonable cycling course of our own.

<!-- b000258 | furniture | pages [11] -->
Team # 2216547

<!-- b000259 | furniture | pages [11] -->
Page 10

<!-- b000260 | caption | pages [11] -->
Figure 6: 2021 Olympic Time Trial course in Tokyo, Japan

<!-- b000261 | caption | pages [11] -->
Figure 7: 2021 UCI World Championship time trial course in Flanders, Belgium

<!-- b000262 | heading | pages [11] -->
4.2.1 Discretization of the Cycling Courses

<!-- b000263 | prose | pages [11] -->
We calibrated the discrete data points (each point contains its latitude, longitude and altitude information) on the real bike courses on the Google Earth. For the straight roads,the two discrete data points to form them are farther apart, while for the curves, the discrete data points are closer together in order to get better precision.

<!-- b000264 | furniture | pages [12] -->
Team # 2216547

<!-- b000265 | furniture | pages [12] -->
Page 11

<!-- b000266 | prose | pages [12] -->
For a point we got from Google Earth, we define it as a three-dimensional vector ′ = (x ′, y ′, z ′) p

<!-- b000267 | prose | pages [12] -->
′ is the latitude, y ′ is the longitude, z ′ is the height. Where x

<!-- b000268 | prose | pages [12] -->
And since the first two dimensions of the information points store latitude and longitude information, we converted them to planar two-dimensional coordinates in meters to achieve higher precision.

<!-- b000269 | prose | pages [12] -->
So we choose a reference point from the bike course as the origin, and based on the radius of the earth, we can calculate the length of the first two dimensions relative to the origin, so that each of our points becomes p = (x, y, z)

<!-- b000270 | prose | pages [12] -->
x and y are the coordinates length of the point relative to the origin on its course map, and z stay the same, so we can reconstruct and display the whole map on the axes in the program simulation like Fig.8.

<!-- b000271 | caption | pages [12] -->
Figure 8: visualization map

<!-- b000272 | heading | pages [12] -->
4.2.2 The Data Structure Definition of the Road

<!-- b000273 | prose | pages [12] -->
After we collected information about the points from the Google Earth, we define the data structure of the road which is basically composed of two points in our model.

<!-- b000274 | prose | pages [12] -->
For the roadi where the i is the index the road in the roads list, and we assume that the points p(1) and p(2) are the start point and the end point of the roadi, we can obtain these properties i i below q  i .x)2 + (p(1) i .y)2 + (p(1) (p(1) i .x −p(2) i .y −p(2) i .z −p(2) i .z)2 Li =    ∆hi = p(1) i .z −p(2) (7) i .z ∆hi θi = arctan   q  (p(1) .x−p(2) .x)2+(p(1) .y−p(2) .y)2 i i i i where Li is the length, ∆hi is the height difference and θi is the inclination angle of the roadi

<!-- b000275 | heading | pages [12] -->
4.2.3 Radius of Curvature Definitions of Points and Roads

<!-- b000276 | prose | pages [12] -->
In order for our model to incorporate the effect of curves, we introduce the concept of radius of curvature of points and roads.

<!-- b000277 | prose | pages [12, 13] -->
For a given data point pi on the cycling course,the radius of curvature of it, donated as R(pi), is the radius of the excircle of the triangle formed by pi−1, pi and pi+1. If pi+1 or pi−1 do not exist, which means that pi is one of the end points of the whole course, the radius of curvature of pi is not defined.

<!-- b000278 | furniture | pages [13] -->
Team # 2216547

<!-- b000279 | furniture | pages [13] -->
Page 12

<!-- b000281 | prose | pages [13] -->
For a given road whose end points are pi and pi+1, if radius of curvature of both points exist, the radius of curvature of it is R(pi)+R(pi+1) . Otherwise, the road is the beginning or ending road 2 of the course, and the radius of curvature of it is pi+1 for beginning, pi for ending.

<!-- b000282 | caption | pages [13] -->
Figure 9: Demonstration of Radius of Curvature Definitions of Points and Roads

<!-- b000283 | prose | pages [13] -->
As shown in Fig.9, the larger the radius of curvature, the closer the section of road is to a straight line.

<!-- b000284 | heading | pages [13] -->
4.3 Newtonian mechanics analysis of cycling

<!-- b000285 | heading | pages [13] -->
4.3.1 Cycling on a straight course

<!-- b000286 | caption | pages [13] -->
Figure 10: Illustration for bike physics (straight course)

<!-- b000287 | prose | pages [13] -->
According to Newton’s second law and neglecting the inertial effect of wheel rotation, the longitudinal model of the bicycle is assumed as follows

<!-- b000288 | prose | pages [13] -->
Prider −1 2CdρAv2 −mtg(µ cos θ + sin θ) −Fb mta = krider (8) v

<!-- b000289 | prose | pages [13] -->
where mt is the total mass of the cyclist and the bike, a donates the acceleration of the cyclist. Thus mta, according to Newton’s second law, equal to the net force apply to the system.

<!-- b000290 | furniture | pages [14] -->
Team # 2216547

<!-- b000291 | furniture | pages [14] -->
Page 13

<!-- b000292 | prose | pages [14] -->
In general, cyclists have two degrees of freedom in managing their own road planning: the freedom to plan their own output power, and the freedom to plan their own gear set selection, based on road information. We assume that the cyclists are fully trained players who can optimally select gear sets based on their experience. krider indicates the conversion efficiency of the player’s output power to the bike under the gear set chosen by the player.

<!-- b000293 | prose | pages [14] -->
Prider Therefore,krider donates the output force from the cyclist to the bike. v 2CdρAv2 represents the amount of air resistance to the cyclist, where Cd is the air drag 1

<!-- b000294 | prose | pages [14] -->
coefficient, ρ is the air density at the race course, which decreases with increasing altitude, A and v are the frontal area and velocity of the rider,respectively.

<!-- b000295 | prose | pages [14] -->
The mtg(µ cos θ + sin θ) term is the combined force of the frictional resistance µmtg cos θ and the sliding force mtg sin θ on the cyclist’s system. µ is the rolling friction coefficient between the bicycle tires and the road. θ is the inclination angle of a given road.

<!-- b000296 | prose | pages [14] -->
Fb donates the resistance of the brake pads to the tires when the player decides to brake.

<!-- b000297 | prose | pages [14] -->
Typical values of the above variables are shown in the following table.

<!-- b000298 | heading | pages [14] -->
Symbols

<!-- b000299 | prose | pages [14] -->
Description Value

<!-- b000300 | prose | pages [14] -->
mt 60kg Total mass of bicycle and cyclist

<!-- b000301 | prose | pages [14] -->
kwheel 0.99 Bicycle power conversion coefficient 0.35m2 A Frontal area of the rider

<!-- b000302 | prose | pages [14] -->
Cd 0.05 Air drag coefficient 1.1kg/m3 ρ Air density

<!-- b000303 | prose | pages [14] -->
µ 0.003 Rolling friction coefficient

<!-- b000304 | heading | pages [14] -->
4.3.2 Cycling on a curved course

<!-- b000305 | prose | pages [14] -->
When a cyclist rides on a curve, a component of static friction is needed to provide the centripetal force required for his turn.

<!-- b000306 | prose | pages [14] -->
For a section of road with radius of curvature R, when the cyclist’s speed is v, mass is mt, the required centripetal force is mtv2 R . Therefore, if the maximum static friction force is µ0mtg cos θ, the velocity of the cyclist can not exceed √µ0g cos θR.

<!-- b000307 | heading | pages [14] -->
4.4 Formalization and Numerical Solution of the Optimizing Problem

<!-- b000308 | prose | pages [14] -->
In the above section, we systematically established a mathematical model of the cyclist’s body muscles, the physical properties of the bike, and the physical properties of the cycling courses.

<!-- b000309 | prose | pages [14] -->
In this section, we try to formally define the optimization problem of minimum time in an Individual Time Trail race and solve the problem using dynamic programming (DP).

<!-- b000310 | heading | pages [14] -->
4.4.1 Formalization of the Problem

<!-- b000311 | prose | pages [14] -->
In an Individual Time Trail race, the goal is to reach the finish line in as short a time as possible. Therefore, we formally define our optimization problem as follows.

<!-- b000312 | furniture | pages [15] -->
Team # 2216547

<!-- b000313 | furniture | pages [15] -->
Page 14

<!-- b000314 | prose | pages [15] -->
Z tf Z xf   dx Prider(t) T = min min dt = min (9) v(t) Prider(t) Prider(t) t0 x0 subject to, 0 ⩽v(t) ⩽min{vmax, √µg cos θR} velocity limits:

<!-- b000315 | prose | pages [15] -->
0 ⩽E(t) ⩽E0 remaining energy limits:

<!-- b000316 | prose | pages [15] -->
0 ⩽Prider(t) ⩽Pmax(t) rider’s power limit:

<!-- b000317 | prose | pages [15] -->
where the decision variable Prider(t) denotes the output power of the rider’s decision at time t, and t0, tf denote the moments at the beginning and end of the track, respectively. x0, xf denote the positions at the beginning and end of the track, respectively.

<!-- b000318 | heading | pages [15] -->
4.4.2 Numerically Solving the Optimizing Problem Using Dynamic Programming

<!-- b000319 | prose | pages [15] -->
Dynamic programming is both a mathematical optimization method and a computer pro- gramming method. The main concept of dynamic programming is straight-forward. We divide a problem into smaller nested sub-problems, and then combine the solutions to reach an overall solution. This concept is known as the principle of optimality, and a more formal exposition is provided in this section. The term “dynamic programming” was first used in the 1940’s by Richard Bellman to describe problems where one needs to find the best decisions one after another. In the 1950’s, he refined it to describe nesting small decision problems into larger ones. The mathematical statement of principle of optimality is remembered in his name as the Bellman Equation.[6]

<!-- b000320 | prose | pages [15] -->
To facilitate the discussion, we define some notations as follows:

<!-- b000321 | prose | pages [15] -->
We call quadruple si = (xi, vi, Pmax,i, Ei) a state. let the four state variables xi,vi,Pmax,i,Ei, respectively, indicate the distance of the current position from the starting point, the speed of the current state, the maximum output power of the current state, and the remaining energy of the current state.

<!-- b000322 | prose | pages [15] -->
Wedefine that statesj = (xj, vj, Pmax,j, Ej)can betransferred tostatesi = (xi, vi, Pmax,i, Ei) (xj ≤xi) at cost ∆t if and only if there exist Prider,0 ≤Prider ≤Pmax,j,that satisfies

<!-- b000323 | prose | pages [15] -->
∆t = xi−xj  vj   vi = vj + a∆t  (10) Prider Pmax,i = −kfPmax,j Pmax0∆t + kr(Pmax0 −Pmax,j)∆t    Ei = Ej + ki(Pmax0 −Pmax,j)∆t −Prider∆t We call Prider the decision from sj to si.

<!-- b000324 | prose | pages [15] -->
The cost of multiple transfers is the sum of the cost of each transfer. let T(xi, vi, Pmax,i, Ei) denotes the minimum cost used to optimally transfer from the starting state (0, 0, Pmax0, E0) to the current state (xi, vi, Pmax,i, Ei).

<!-- b000325 | prose | pages [15] -->
According to the Bellman’s principle of optimality, i.e. an optimal policy (set of decisions) has the property that whatever the initial state and decisions are, the remaining decisions must constitute and optimal policy with regard to the state resulting from the first decision.

<!-- b000326 | prose | pages [15, 16] -->
Bellman’s principle of optimality holds for our optimizing problem.Therefore,we have Prider{T(xj, vj, Pmax,j, Ej) + ∆t} T(xi, vi, Pmax,i, Ei) = max (11)

<!-- b000327 | furniture | pages [16] -->
Team # 2216547

<!-- b000328 | furniture | pages [16] -->
Page 15

<!-- b000329 | caption | pages [16] -->
Figure 11: Demonstration of use of Bellman’s principle of optimality in dynamic programming.

<!-- b000331 | prose | pages [16] -->
where Prider, ∆t are the decision and cost of transfer from state (xj, vj, Pmax,j, Ej) to (xi, vi, Pmax,i, Ei) respectively.

<!-- b000332 | heading | pages [16] -->
4.4.3 Complexity Analysis of Dynamic Programming Solution

<!-- b000333 | prose | pages [16] -->
Since modern electronic computers are very limited in their ability to process continuous data directly, so we quantify our continuous data into discrete levels.

<!-- b000334 | prose | pages [16] -->
let nx, nv, np, ne, nr donate the quantification levels (number of distinct discrete levels) of x, v, Pmax, E, Prider,respectively.

<!-- b000335 | prose | pages [16] -->
Therefore, the total number of states is as nxnvnpne , and for each state, the number of computations required can be expressed as O(nr). Thus, the time complexity of our dynamic programming algorithm is O(nxnvnpnenr), the space complexity is O(nxnvnpne).

<!-- b000336 | prose | pages [16] -->
When nx = 400, nv = 30, np = 10, ne = 10, nr = 450,the calculation takes about 10 minutes on a MacBook Pro(2020,Apple M1).

<!-- b000337 | heading | pages [16] -->
5 Results

<!-- b000338 | heading | pages [16] -->
5.1 The Power Profiles of Time Trail Specialist and Sprinter of Different

<!-- b000339 | prose | pages [16] -->
Genders

<!-- b000340 | prose | pages [16] -->
The power profiles are shown in Fig.5.

<!-- b000341 | furniture | pages [17] -->
Team # 2216547

<!-- b000342 | furniture | pages [17] -->
Page 16

<!-- b000343 | heading | pages [17] -->
5.2 Power Distribution for Various Courses

<!-- b000344 | prose | pages [17] -->
5.2.1 2021 Olympic Time Trial course in Tokyo, Japan

<!-- b000345 | caption | pages [17] -->
Figure 12: The Optimal Power Distribution of different kinds of cyclists

<!-- b000346 | caption | pages [17] -->
Fig.12 shows the optimal power distribution obtained by the dynamic programming algorithm

<!-- b000347 | prose | pages [17] -->
for different kinds of cyclists with different stages of the track.

<!-- b000348 | prose | pages [17] -->
From the graph, we can see that Sprinter cyclists are suitable to increase their power output at the beginning of the race and in the uphill phase to get a lead in the progress. However, compared to Time Trail Specialists, Sprinters are usually not good at long distance riding, so they usually lag behind Time Trail Specialists on long flat sections.

<!-- b000349 | prose | pages [17] -->
Therefore, we came up with the following planning strategy: for a relatively undulating section of road, the optimal power planning plan for the Sprinter is roughly to power up at the beginning and on the large uphill section, and to ride at a lower power on the large, relatively gentle section of road to preserve energy. For the TTS, the opposite is true: don’t accelerate at full power at the beginning of the race, and the same for the uphill, but allocate more power on the large gentle sections. Gender makes no significant difference to this strategy.

<!-- b000350 | furniture | pages [18] -->
Team # 2216547

<!-- b000351 | furniture | pages [18] -->
Page 17

<!-- b000352 | prose | pages [18] -->
5.2.2 2021 UCI World Championship Time Trial Course and The Course We Designed

<!-- b000353 | caption | pages [18] -->
Figure 13: The Optimal Power Distribution for 2021 UCI World Championship Time Trial

<!-- b000354 | prose | pages [18, 19] -->
Course The Optimal Power Distribution of 2021 UCI World Championship Time Trial Course and the Course We Designed are shown in Fig.13 and Fig.14, respectively.

<!-- b000355 | caption | pages [18] -->
Figure 14: The Optimal Power Distribution for Our Course

<!-- b000356 | furniture | pages [19] -->
Team # 2216547

<!-- b000357 | furniture | pages [19] -->
Page 18

<!-- b000359 | prose | pages [19] -->
The data from these two courses also supports our view on Time Trail Specialists and Sprinter.

<!-- b000360 | heading | pages [19] -->
5.3 Result Analysis

<!-- b000361 | caption | pages [19] -->
Figure 15: The Optimal Power Distribution,the velocity and the Altitude of 2021 Olympic Time

<!-- b000362 | prose | pages [19] -->
Trail

<!-- b000363 | caption | pages [19] -->
Fig.15 shows the power output, speed, and track height distribution of the Time Trail

<!-- b000364 | prose | pages [19] -->
Specialist (male) on the 2021 Olympic Time Trail. We can see that the runner has more power and less speed when the course is uphill, and the opposite is true for the downhill. This further confirms the validity of our model.

<!-- b000365 | heading | pages [19] -->
5.4 Potential Impact of Weather Conditions

<!-- b000366 | prose | pages [19] -->
Even on the same track, different weather conditions can cause different race results. In our model, we mainly consider the effect of wind and ground humidity on the courses.

<!-- b000367 | heading | pages [19] -->
5.4.1 Wind

<!-- b000368 | prose | pages [19] -->
The factors affecting wind on cycling races can be divided into wind direction and wind force. In the case of larger tailwind, athletes need to resist less wind resistance, and in the case of larger headwind, athletes need to resist more wind resistance. For different winds, we make different modifications to the model as follows:

<!-- b000369 | prose | pages [19] -->
v = |vrider ± vwind| · cosθ (12) Where vrider is the cyclist’s rate, vwind is the wind speed, and θ is the angle between the rider’s riding direction and the wind direction.

<!-- b000370 | heading | pages [19] -->
5.4.2 Ground Humidity

<!-- b000371 | prose | pages [19] -->
If the ground humidity is high, the cyclist will reduce his speed to prevent slipping or falling; while if the ground is dry, the cyclist can release his speed as much as he wants.In our model: µ is smaller when the ground humidity is higher, and µ is larger when the ground humidity is lower.

<!-- b000372 | furniture | pages [20] -->
Team # 2216547

<!-- b000373 | furniture | pages [20] -->
Page 19

<!-- b000374 | prose | pages [20] -->
The influence of environmental factors on rider performance can be seen as follows:

<!-- b000375 | caption | pages [20] -->
Figure 16: The Influence of Environmental Factors on Rider Performance

<!-- b000376 | prose | pages [20] -->
In Figure 16, The green line shows the "distance-power" curve of a TTS(male) under ideal conditions(Time:24’25"); The blue line shows the "distance-power" curve of the same TTS(male) in a rainy day(Time:30’10"); The yellow line shows the "distance-power" curve of the same TTS(male) during the race in upwind conditions(Time:25’11"). We can see from the simulation results that higher ground humidity and stronger headwinds will lengthen the time for riders to finish the race.

<!-- b000377 | heading | pages [20] -->
5.5 Sensitivity of the Results to Rider Deviations from the Target Power

<!-- b000378 | prose | pages [20] -->
Distribution

<!-- b000379 | prose | pages [20] -->
Due to the uncontrollability of environmental factors, riders’ own physical conditions and different views and divisions of the track between riders and coaches, riders will not strictly follow the planned optimal plan to race, we regard the actual power output of riders as the sum of the planned optimal power output plan and a random error obeying normal distribution.

<!-- b000380 | prose | pages [20] -->
Prider(t) = Prider_real(t) = Prider_plan(t) + ε(t) (13) where ε(t) is a random error that follows a normal distribution

<!-- b000381 | prose | pages [20] -->
The improved model was brought into simulation and the following results were obtained:

<!-- b000382 | caption | pages [20] -->
Figure 17: The Optimal and the After disturbance Power Distribution for Tokyo 2021

<!-- b000383 | prose | pages [20] -->
The Optimal time result is 24’25", the after disturbance is 26’44".

<!-- b000384 | heading | pages [20] -->
5.6 Result of Team Time Trial

<!-- b000385 | prose | pages [20] -->
We know that cyclists need to resist air resistance during high speed. The faster the speed, the greater the air resistance is. In team cycling, teams often use the "mountain train" tactic:

<!-- b000386 | furniture | pages [21] -->
Team # 2216547

<!-- b000387 | furniture | pages [21] -->
Page 20

<!-- b000388 | prose | pages [21] -->
the team members line up to minimize overall air resistance. The rider at the front of the line needs the most wind resistance, while the rider further back in the line needs to resist less wind resistance. By finding information and data processing [13], we got the information of wind resistance of each rider in the 6-member team, which is listed as follows:(the percentage indicates the percentage of wind resistance each rider needs to resist compared with the rider at the front of the queue)

<!-- b000389 | caption | pages [21] -->
Figure 18: Wind Resistance to Different Riders of the Team

<!-- b000390 | prose | pages [21] -->
The dynamic strategy used by the team in the "Mountain Train" tactic is that each time the rider at the front of the queue helps the team to resist the maximum wind resistance for a period of time, then switches to the last position in the queue to enjoy the least wind resistance. The rest of the riders will move forward to replace one another in turn. And so on and so forth. The average power output of each driver in the team will be different (i.e., the average speed of the team will be different) for different lengths of replacement intervals (the time a driver is at the front of the queue in each position sequence cycle). After several simulations, we found the replacement interval time that makes the average power output maximum (shortest finish time), and the simulation results are as follows:

<!-- b000391 | caption | pages [21] -->
Figure 19: The Simulation Results of Team Time Trial and Individual Time Trial

<!-- b000392 | prose | pages [21] -->
InFigure 19, The red line shows the "distance-power" curve of a Team Time Trial(Time:22’36"); The green line shows the "distance-power" curve of an Individual Time Trial(Time:24’25"). We can see from the simulation results that thanks to the "mountain-train" strategy used in the team competition, the average wind resistance for each rider is reduced, allowing the team to move at a faster pace.

<!-- b000393 | furniture | pages [22] -->
Team # 2216547

<!-- b000394 | furniture | pages [22] -->
Page 21

<!-- b000395 | heading | pages [22] -->
6 Strength and Weakness

<!-- b000396 | heading | pages [22] -->
6.1 Strength

<!-- b000397 | prose | pages [22] -->
• We establish the power output model of the rider according to the human muscle physiol- ogy and human energy model, and by considering the different input parameters of riders, we can output power profiles with their own attribute fields.

<!-- b000398 | prose | pages [22] -->
• We model the bike course with real data and reasonable design, and set data structure included height difference, radius of curvature, etc. and some global environmental variables such as ground friction coefficient, wind resistance coefficient, etc., which well rebuild the real bike courses and exhibits some important features such as road curves and wind or weather conditions, etc.

<!-- b000399 | prose | pages [22] -->
• We use the well-known Newtonian mechanics model in our model analysis of bicycle and road riding, which is simple and produces scientifically reliable mechanical analysis.

<!-- b000400 | prose | pages [22] -->
• After rigorously defining the optimization problem formally, we use a dynamic program- ming algorithm to solve the optimization problem. Under our model definition, dynamic programming is able to guarantee that the optimal solution can be solved in a relatively modest amount of time.

<!-- b000401 | heading | pages [22] -->
6.2 Weakness

<!-- b000402 | prose | pages [22] -->
• Real-life data is continuous, but computer simulations are difficult to handle continuous data, so we disaggregate the data, which makes continuous data lose some information.

<!-- b000403 | prose | pages [22] -->
• There are more factors affecting the rider such as the rider’s mental state, etc, but in mathematical modeling we can only consider a limited number of major factors to model which may also lose some details of the impact

<!-- b000404 | prose | pages [22] -->
• In the team time trials competition, we simplify the multiplayer team into prime points, and also risk missing some actions within the team that can optimize the performance.

<!-- b000405 | heading | pages [22] -->
References

<!-- b000406 | references | pages [22] -->
[1] F. Ashtiani, V . S. M. Sreedhara, A. V ahidi, R. Hutchison, and G. Mocko,“Experimental

<!-- b000407 | references | pages [22] -->
modeling of cyclists fatigue and recovery dynamics enabling optimal pacing in a time

<!-- b000408 | references | pages [22] -->
trial,” in 2019 American Control Conference (ACC). IEEE, 2019, pp. 5083–5088.

<!-- b000409 | references | pages [22] -->
[2] S. A. Fayazi, N. Wan, S. Lucich, A. Vahidi and G. Mocko, "Optimal pacing in a cycling

<!-- b000410 | references | pages [22] -->
time-trial considering cyclist’s fatigue dynamics," 2013 American Control Conference,

<!-- b000411 | references | pages [22] -->
2013, pp. 6442-6447, doi: 10.1109/ACC.2013.6580849.

<!-- b000412 | references | pages [22] -->
[3] Rehrer, N. J., et al. "Energy intake and expenditure during a 6-day cycling stage race."

<!-- b000413 | references | pages [22] -->
Scandinavian Journal of Medicine Science in Sports 20.4 (2010): 609-618.

<!-- b000414 | references | pages [22] -->
[4] Sanders, Dajo, et al. "Predicting high-power performance in professional cyclists." Inter-

<!-- b000415 | references | pages [22] -->
national journal of sports physiology and performance 12.3 (2017): 410-413.

<!-- b000416 | references | pages [22] -->
[5] Ebert, Tammie R., et al. "Power output during a professional men’s road-cycling tour."

<!-- b000417 | references | pages [22] -->
International journal of sports physiology and performance 1.4 (2006): 324-335.

<!-- b000418 | furniture | pages [23] -->
Team # 2216547

<!-- b000419 | furniture | pages [23] -->
Page 22

<!-- b000420 | references | pages [23] -->
[6] https://en.wikipedia.org/wiki/Dynamic_programming

<!-- b000421 | references | pages [23] -->
[7] T.D. Noakes, A. St. Clair Gibon, and E.V . Lambert, “From catastropheto complexity: a

<!-- b000422 | references | pages [23] -->
novel model of integrative central neural regulation of effort and fatigue during exercise in

<!-- b000423 | references | pages [23] -->
humans: summary and conclusions,” British J. of Sports Medicine, vol. 39, pp. 120–124,

<!-- b000424 | references | pages [23] -->
2005.

<!-- b000425 | references | pages [23] -->
[8] L. Ma, D. Chablat, F. Bennis, W. Zhang, and F. Guillaume, “A new fatigue and recov-

<!-- b000426 | references | pages [23] -->
ery model and its ergonomics application in human simulation,” Virtual and Physical

<!-- b000427 | references | pages [23] -->
Prototyping, pp. 123–137, 2010.

<!-- b000428 | references | pages [23] -->
[9] https://ecal.berkeley.edu/files/ce191/CH05-DynamicProgramming.pdf

<!-- b000429 | references | pages [23] -->
[10] http://ffden-2.phys.uaf.edu/webproj/211_fall_2016/Tad_Nelson/Tad_

<!-- b000430 | references | pages [23] -->
Nelson/page3.html

<!-- b000431 | references | pages [23] -->
[11] https://earth.google.com/web/

<!-- b000432 | references | pages [23] -->
[12] Ashtiani, Faraz Sreedhara, Vijay Sarthy Vahidi, Ardalan Hutchison, Randolph Mocko,

<!-- b000433 | references | pages [23] -->
Gregory. (2020). Optimal Pacing of a Cyclist in a Time Trial Based on Experimentally

<!-- b000434 | references | pages [23] -->
Calibrated Models of Fatigue and Recovery.

<!-- b000435 | references | pages [23] -->
[13] Barry, Nathan, et al. "Aerodynamic drag interactions between cyclists in a team pursuit."

<!-- b000436 | references | pages [23] -->
Sports Engineering 18.2 (2015): 93-103.

<!-- b000437 | references | pages [23] -->
[14] https://www.youtube.com/watch?v=IsfnXSdpshY

<!-- b000438 | references | pages [24] -->
1. WHY WE NEED TO PLAN OUR RIDES

<!-- b000439 | references | pages [24] -->
WISELY

<!-- b000440 | references | pages [24] -->
With the development of biology and physics,

<!-- b000441 | references | pages [24] -->
scientific and effective, race preparation and

<!-- b000442 | references | pages [24] -->
planning of races is becoming more and more

<!-- b000443 | references | pages [24] -->
important in all cycling events. If you and your

<!-- b000444 | references | pages [24] -->
rider don't plan your race scientifically, you are

<!-- b000445 | references | pages [24] -->
likely to lose energy in the early stages of a long

<!-- b000446 | references | pages [24] -->
bike course or not give your best on a short bike

<!-- b000447 | references | pages [24] -->
course. Today I would like to bring you and your

<!-- b000448 | references | pages [24] -->
athletes our scientific cycling scheme.

<!-- b000449 | references | pages [24] -->
2. HOW OUR SCHEME ENHANCES THE

<!-- b000450 | references | pages [24] -->
RIDER

<!-- b000451 | references | pages [24] -->
Different types of riders have different physica

<!-- b000452 | references | pages [24] -->
l performances and power curves, which refer to a

<!-- b000453 | references | pages [24] -->
visual representation of the maximum power a ride

<!-- b000454 | references | pages [24] -->
r can maintain for a particular length of time，

<!-- b000455 | references | pages [24] -->
So in cycling, different types of riders are suitable f

<!-- b000456 | references | pages [24] -->
or different tactics. Therefore, determining which t

<!-- b000457 | references | pages [24] -->
ype of rider you are will help you find the tactics th

<!-- b000458 | references | pages [24] -->
at work for you, which in turn will help you win bet

<!-- b000459 | references | pages [24] -->
ter.

<!-- b000460 | references | pages [24] -->
3. IDENTIFY THE TYPE OF RIDER

<!-- b000461 | references | pages [24] -->
Common types of riders are: Climber,

<!-- b000462 | references | pages [24] -->
Puncheur, Ruleur, Sprinter, Time Trial

<!-- b000463 | references | pages [24] -->
Specialist.

<!-- b000464 | references | pages [24] -->
We use Sprinter and Time Trial Specialist as e

<!-- b000465 | references | pages [24] -->
xamples to show you the difference between the dif

<!-- b000466 | references | pages [24] -->
ferent types of drivers:

<!-- b000467 | references | pages [24] -->
The Sprinter has strong explosive power, but not co

<!-- b000468 | references | pages [24] -->
nsistent output; while the Time Trial Specialist ha

<!-- b000469 | references | pages [24] -->
s consistent output, but not as strong explosive po

<!-- b000470 | references | pages [24] -->
wer as the Sprinter. So when comparing the two, S

<!-- b000471 | references | pages [24] -->
printer is suitable for focusing on winning at the en

<!-- b000472 | references | pages [24] -->
d of a race or during the intermediate sprints (if a r

<!-- b000473 | references | pages [24] -->
ace has intermediate sprints), while Time Trial Spe

<!-- b000474 | references | pages [24] -->
cialist is suitable for races that require continuous

<!-- b000475 | references | pages [24] -->
output, such as Individual time trial.

<!-- b000476 | references | pages [24] -->
Seeing this, you must want to figure out which

<!-- b000477 | references | pages [24] -->
kind of rider you are, right? You can figure out you

<!-- b000478 | references | pages [24] -->
r type by following these steps:

<!-- b000479 | references | pages [24] -->
1.Participated in the “Maximum-

<!-- b000480 | references | pages [24] -->
Effort” experiment and obtained the experim

<!-- b000481 | references | pages [24] -->
ental data.You can contact us or take part in the “

<!-- b000482 | references | pages [24] -->
Maximum_Effort” experiment yourself, which refer

<!-- b000483 | references | pages [24] -->
to an expriment in which you sprint with all your

<!-- b000484 | references | pages [24] -->
strength on a flat section of road after a full rest an

<!-- b000485 | references | pages [24] -->
d recording the your power output during the proce

<!-- b000486 | references | pages [24] -->
ss, further obtaining your “time-power” curve.

<!-- b000487 | references | pages [24] -->
2.Obtain the model parameters from the “

<!-- b000488 | references | pages [24] -->
Maximum-Effort” experimental data.

<!-- b000489 | references | pages [24] -->
You can contact us or use the formulas we give you

<!-- b000490 | references | pages [24] -->
to calculate your parameters in our model using yo

<!-- b000491 | references | pages [24] -->
ur "time-power" curve.

<!-- b000492 | references | pages [24] -->
3.Obtain the power curve through the mo

<!-- b000493 | references | pages [24] -->
del parameters by

<!-- b000494 | references | pages [24] -->
using our model and algorithm, you can easily

<!-- b000495 | references | pages [24] -->
get your own power curve by using the parameters

<!-- b000496 | references | pages [24] -->
obtained in step 2.

<!-- b000497 | references | pages [24] -->
4.Compare the power curve of a typical ty

<!-- b000498 | references | pages [24] -->
pe of player to determine your own type.

<!-- b000499 | references | pages [24] -->
Compare your power curve from step 3 with the po

<!-- b000500 | references | pages [24] -->
wer curve of a typical player, and you will be able t

<!-- b000501 | references | pages [24] -->
o determine your type. Isn’t it easy?

<!-- b000502 | references | pages [24] -->
4. COLLECT ROAD INFORMATION IN

<!-- b000503 | references | pages [24] -->
ADVANCE

<!-- b000504 | references | pages [24] -->
It's important for riders to know about the

<!-- b000505 | references | pages [24] -->
course in advance before we start the bike race. Do

<!-- b000506 | references | pages [25] -->
we need to know in advance if the course has a lot

<!-- b000507 | references | pages [25] -->
of steep hills? Or does the course have a lot of

<!-- b000508 | references | pages [25] -->
bends? We also need to know in advance what the

<!-- b000509 | references | pages [25] -->
weather will be like on the day of the race. All of

<!-- b000510 | references | pages [25] -->
this is very important for the rider's decision how

<!-- b000511 | references | pages [25] -->
to ride.

<!-- b000512 | references | pages [25] -->
It is very easy for our virtual mapping program

<!-- b000513 | references | pages [25] -->
to display the course and to calculate and store the

<!-- b000514 | references | pages [25] -->
course characteristics such as height difference,

<!-- b000515 | references | pages [25] -->
radius of curvature etc. for subsequent analysis.

<!-- b000516 | references | pages [25] -->
We also recommend that you and your riders check

<!-- b000517 | references | pages [25] -->
the environmental information on the day of the

<!-- b000518 | references | pages [25] -->
race, such as wind speed and direction, whether it

<!-- b000519 | references | pages [25] -->
is raining, etc., which will make our solution more

<!-- b000520 | references | pages [25] -->
accurate.

<!-- b000521 | references | pages [25] -->
5. IMPLEMENTATION

<!-- b000522 | references | pages [25] -->
Once you have completed the detailed modelin

<!-- b000523 | references | pages [25] -->
g of the course information and the physical profile

<!-- b000524 | references | pages [25] -->
of the rider based on these sections, you can direct

<!-- b000525 | references | pages [25] -->
ly use the tools we provide to directly obtain the op

<!-- b000526 | references | pages [25] -->
timal output power allocation scenario for that ride

<!-- b000527 | references | pages [25] -->
r in that course. If you fit this scenario, here are so

<!-- b000528 | references | pages [25] -->
me of our recommendations for you:

<!-- b000529 | references | pages [25] -->
Using the tool we provide, after entering th

<!-- b000530 | references | pages [25] -->
⚫

<!-- b000531 | references | pages [25] -->
e course information and the rider physiologica

<!-- b000532 | references | pages [25] -->
l data, you can get a visual representation of ri

<!-- b000533 | references | pages [25] -->
der’s

<!-- b000534 | references | pages [25] -->
optimal power output, speed, and course heigh

<!-- b000535 | references | pages [25] -->
t distribution with the course length, with a dy

<!-- b000536 | references | pages [25] -->
namic 3D course route information map. These

<!-- b000537 | references | pages [25] -->
icons make it very easy for you and your rider

<!-- b000538 | references | pages [25] -->
to visualize the power distribution and help hi

<!-- b000539 | references | pages [25] -->
m/her understand the optimal solution.

<!-- b000540 | references | pages [25] -->
If permitted by the event organizer, you can su

<!-- b000541 | references | pages [25] -->
⚫

<!-- b000542 | references | pages [25] -->
ggest that your rider take the power meter to t

<!-- b000543 | references | pages [25] -->
he course and ride the entire course in person

<!-- b000544 | references | pages [25] -->
and compare the data collected by the instrum

<!-- b000545 | references | pages [25] -->
ent with the optimal solution given by our prog

<!-- b000546 | references | pages [25] -->
ram, which will help the rider to better unders

<!-- b000547 | references | pages [25] -->
tand the power output distribution.

<!-- b000548 | references | pages [25] -->
If you have difficulty in determining a ride

<!-- b000549 | references | pages [25] -->
r’s Power Profile or determining course inform

<!-- b000550 | references | pages [25] -->
ation, you can generally determine the type of

<!-- b000551 | references | pages [25] -->
rider based on his or her usual training perfor

<!-- b000552 | references | pages [25] -->
mance, here are our simple suggestions for po

<!-- b000553 | references | pages [25] -->
wer distribution for different types of riders.

<!-- b000554 | references | pages [25] -->
For Climbers: The long climbs are your most

<!-- b000555 | references | pages [25] -->
⚫

<!-- b000556 | references | pages [25] -->
advantageous route, you can save your body be

<!-- b000557 | references | pages [25] -->
fore and after the long climbs and focus your p

<!-- b000558 | references | pages [25] -->
ower output on the long climbs to get a better

<!-- b000559 | references | pages [25] -->
advantage.

<!-- b000560 | references | pages [25] -->
For Puncheurs and Sprinters: You are very

<!-- b000561 | references | pages [25] -->
⚫

<!-- b000562 | references | pages [25] -->
good at making a lot of power in a short period

<!-- b000563 | references | pages [25] -->
of time, which is your biggest advantage, but i

<!-- b000564 | references | pages [25] -->
t also tends to make you less dominant on long

<!-- b000565 | references | pages [25] -->
, gentle courses. Our advice: you can use your s

<!-- b000566 | references | pages [25] -->
trengths at the beginning and end of the cours

<!-- b000567 | references | pages [25] -->
e, and on the shorter climbs.

<!-- b000568 | references | pages [25] -->
For Rouleur and Time Trial Specialists: Y

<!-- b000569 | references | pages [25] -->
⚫

<!-- b000570 | references | pages [25] -->
ou have a good combination of qualities that us

<!-- b000571 | references | pages [25] -->
ually give you an advantage on the gentle secti

<!-- b000572 | references | pages [25] -->
ons. You can try to avoid using your full streng

<!-- b000573 | references | pages [25] -->
th on long or short climbs when possible, other

<!-- b000574 | references | pages [25] -->
wise you may lose later in the race due to lack

<!-- b000575 | references | pages [25] -->
of energy.
