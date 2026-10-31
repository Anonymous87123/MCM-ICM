# P-A-2022-2212245-8b85eeb2

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
A

<!-- b000006 | title | pages [1] -->
2212245

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
How to Ride a Cycling Time Trial

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
As a mathematician you’re used to solving problems on your own, so that’s the way I approach cycling.

<!-- b000011 | prose | pages [1] -->
—— Anna Kiesenhofer, the winner of women’s road race in Tokyo 2020

<!-- b000012 | prose | pages [1] -->
As Anna Kiesenhofer, a Ph.D. in mathematics, said, a proper mathematical model can help cyclists to plan their races better and more efficiently. And that is exactly what we do in this paper.

<!-- b000013 | prose | pages [1] -->
We begin with the analysis on energy supply system of the cyclists. According to basic biological knowledge, we divide the contribution of overall output power into three different energy supply sys- tems: ATP-CP system, glycolysis system and aerobic system. We base our model on ODEs to describe the change of content of various substances in human body during cycling.

<!-- b000014 | prose | pages [1] -->
Based on our energy supply model, we then define the power profiles of the time trial specialists and sprinters, with different genders considered. The comparison between our theoretical power curves and real-world power curves implies the reliability of the energy model we have developed. It is worth noting that power curves here is presented as an intermediate results. We use our energy model for further discussions, which is more essential and accurate.

<!-- b000015 | prose | pages [1] -->
Then in order to evaluate the power needed for maintaining a given speed, we analyze the motion of bicycle-cyclist system. We include different drag resistances, hilly terrain and sharp turnings into our model. A motion equation is obtained here to determine the relation between the acceleration and propulsive force.

<!-- b000016 | prose | pages [1] -->
With the energy model and motion model developed, we discuss the optimal strategies on each characteristic terrains. It is found that the optimal strategy in most cases is to maintain a fixed speed, threshold speed, all along the race. The exception is when on a hilly course or sharply curved road. Slowing down is generally needed for cycling uphill or sharp turnings. Accordingly, we propose a feasible strategy, which is a combination of optimal strategies on each specific terrains.

<!-- b000017 | prose | pages [1] -->
To test our model in real world conditions, we first reconstruct the courses and obtain necessary data by processing the official roadmaps. Then we simulate the actual performance of cyclists of four different types on three courses. The simulation shows that the optimal time on 2021 UCI Champi- onship in Belgium is 53.02 minutes, which is very close to the champion’s 57.78 minutes on this course.

<!-- b000018 | prose | pages [1] -->
We evaluate the sensitivity of the deviations from our strategy, where we find 30% deviation only gives 3.11% difference in time. Then for sensitivity of weather, we focus on the wind directions and strengths. The analysis shows that the wind greatly affects the strategy adopted and expected perfor- mance.

<!-- b000019 | prose | pages [1] -->
Finally, we modify our model to include Team Time Trials, where the drafting effect is considered to reduce the overall aerodynamic resistance. We propose a strategy for TTT that cyclists rotate to take pulls and modify themselves before and in sprint stage. The team strategy can improve the speed by 14.43% compared to individual case.

<!-- b000020 | keywords | pages [1] -->
Keywords: cyclist; power profile; time trial; ODE;

<!-- b000021 | furniture | pages [2] -->
Team # 2212245

<!-- b000022 | furniture | pages [2] -->
Page 2 of 25

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
1

<!-- b000025 | heading | pages [2] -->
Introduction

<!-- b000026 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background 3 Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000027 | prose | pages [2] -->
2

<!-- b000028 | heading | pages [2] -->
Assumptions and Notations

<!-- b000029 | prose | pages [2] -->
3

<!-- b000030 | prose | pages [2] -->
4 Basic Assumptions and Justifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000031 | prose | pages [2] -->
3

<!-- b000032 | heading | pages [2] -->
The Cyclist Energy Supply Model

<!-- b000033 | prose | pages [2] -->
4

<!-- b000034 | prose | pages [2] -->
5 ATP-CP System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5 Glycolysis-Aerobic System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 6 The Overall Energy Supply Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3

<!-- b000035 | prose | pages [2] -->
4 Power Profiles of the Cyclists

<!-- b000036 | prose | pages [2] -->
7

<!-- b000037 | prose | pages [2] -->
8 Solving Power Curves Based on Energy Supply Model 4.1 . . . . . . . . . . . . . . . . . . .

<!-- b000038 | prose | pages [2] -->
8 Gender Differences in Cyclists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 9 Power Profiles of Time Trial Specialists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 10 Power Profiles of Sprinters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | heading | pages [2] -->
The Cyclist Motion Model

<!-- b000041 | prose | pages [2] -->
11

<!-- b000042 | prose | pages [2] -->
12 Drag Resistances in Cyclist Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 12 Linear Motion of Cyclists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 Cyclist Motion on the Curved Road

<!-- b000043 | prose | pages [2] -->
6 The Optimal Strategy for Individual Time Trial

<!-- b000044 | prose | pages [2] -->
14

<!-- b000045 | prose | pages [2] -->
14 Strategy for Flat Straight Courses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 15 Strategy for Sharp Turning and Hilly Course . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000046 | prose | pages [2] -->
7

<!-- b000047 | heading | pages [2] -->
Model Application on Time Trial Courses

<!-- b000048 | prose | pages [2] -->
15

<!-- b000049 | prose | pages [2] -->
16 The Course Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 16 Model Application Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 17 Sensitivity Analysis of the deviations from the target power 7.3

<!-- b000050 | prose | pages [2] -->
8 The Impact of Weather on Cycling

<!-- b000051 | prose | pages [2] -->
. . . . . . . . . . . . . . . .

<!-- b000052 | prose | pages [2] -->
18

<!-- b000053 | prose | pages [2] -->
19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Influence of weather 19 Sensitivity Analysis of the weather . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000054 | prose | pages [2] -->
9

<!-- b000055 | heading | pages [2] -->
Modified Model for Team Time Trial

<!-- b000056 | prose | pages [2] -->
20

<!-- b000057 | prose | pages [2] -->
20 Team Strategy before Sprint Stage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 21 Team Strategy for Final Sprint Stage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 21 Solution of the Team Time Trial Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3

<!-- b000058 | heading | pages [2] -->
10 Model Evaluation and Further Discussion

<!-- b000059 | prose | pages [2] -->
22

<!-- b000060 | prose | pages [2] -->
22 Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.1 22 Possible Improvement of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2

<!-- b000061 | heading | pages [2] -->
References

<!-- b000062 | references | pages [2] -->
Rider’s Race Guidance

<!-- b000063 | references | pages [2] -->
22

<!-- b000064 | references | pages [2] -->
22

<!-- b000065 | references | pages [2] -->
24

<!-- b000066 | furniture | pages [3] -->
Team # 2212245

<!-- b000067 | furniture | pages [3] -->
Page 3 of 25

<!-- b000068 | references | pages [3] -->
1

<!-- b000069 | heading | pages [3] -->
Introduction

<!-- b000070 | prose | pages [3] -->
1.1

<!-- b000071 | heading | pages [3] -->
Background

<!-- b000072 | prose | pages [3] -->
After Karl von Drais created world’s first bicycle, cycling soon became a popular sports activity. And it has been featured in all Olympic Games since 1894 when first Modern Olympic Game was held.[1]

<!-- b000073 | prose | pages [3] -->
Today, over 44 million people in the U.S. participate in road cycling events, and the number still keeps increasing.[2]

<!-- b000074 | caption | pages [3] -->
Figure 1: Fuji Speedway, Tokyo 2020 Olympic Game[3]

<!-- b000075 | prose | pages [3] -->
There are various types of bicycle road races, among which we focus on time trial events. There are two main forms of time trial:

<!-- b000076 | prose | pages [3] -->
In an individual time trial (ITT), cyclists complete a fixed course one at a time. They are forbid to cooperate with or ride near each other. The time to complete the course is recorded for each cyclist, and the one who finish the course with the least amount of time wins the race.

<!-- b000077 | prose | pages [3] -->
In a team time trial (TTT), teams of cyclists race against the clock one at time. Unlike ITT where cooperation is not allowed, in TTT, cyclists in the same team can ride in each other’s slipstream to reduce aerodynamic resistance. The winning team in a TTT is usually determined by comparing the finish times of the 4th cyclist in each team.[4]

<!-- b000078 | prose | pages [3] -->
1.2

<!-- b000079 | heading | pages [3] -->
Problem Restatement

<!-- b000080 | prose | pages [3] -->
This paper aims to build a proper model to provide optimal race strategies and possible performances for cyclists and Directeur Sportif.

<!-- b000081 | prose | pages [3] -->
• Establish a model for any type of cyclists to determine the power distribution along the whole course. In other words, given a position on the course, the model should suggest an optimal power to apply. The model ought to take power curve of the cyclists, weather, and terrains into consideration.

<!-- b000082 | prose | pages [3] -->
• Define power profiles for cyclists of two types and different genders. Our profiles should include the profile of time trail specialist.

<!-- b000083 | prose | pages [3] -->
• Apply our model to various time trial courses, including two real-world courses in 2021 and a self-designed course with enough sharp turns and climbs.

<!-- b000084 | prose | pages [3] -->
• Sensitivity Analysis for possible deviations from the optimal power distribution and small dif- ference in the weather and environment.

<!-- b000085 | furniture | pages [4] -->
Team # 2212245

<!-- b000086 | furniture | pages [4] -->
Page 4 of 25

<!-- b000087 | prose | pages [4] -->
• Extend our model for TTT where cyclists can take advantages of their teammates to allow higher power and quicker recovery.

<!-- b000088 | prose | pages [4] -->
2

<!-- b000089 | heading | pages [4] -->
Assumptions and Notations

<!-- b000090 | prose | pages [4] -->
2.1

<!-- b000091 | heading | pages [4] -->
Basic Assumptions and Justifications

<!-- b000092 | prose | pages [4] -->
• Cyclists and their bicycles are considered as particles. A typical Olympic Time trail course is about 20 km long for women and 40 km long for men. On such a grand scale, the size of the cyclists is negligible.

<!-- b000093 | prose | pages [4] -->
• Suppose that the sharp turning parts of the courses is relatively flat, and athletes keep uniform motion in the sharp turning. For safety considerations, organizers generally choose a relatively flat area for sharp turns.

<!-- b000094 | prose | pages [4] -->
• Cyclists of the same gender have the same weight, which is the average weight of each gender.

<!-- b000095 | prose | pages [4] -->
Although the cyclist’s weight is a factor that affects the results of the problem, it is not the main problem we need to explore, so it can be ignored.

<!-- b000096 | prose | pages [4] -->
• The biological process of human energy supply is carried out at a constant speed. In fact, the biological process of human energy supply is very complex, and its speed is affected by many factors such as enzyme concentration. It is difficult to give a mathematical expression. Through this assumption, the analysis of energy supply problem becomes feasible in a short time.

<!-- b000097 | prose | pages [4] -->
2.2

<!-- b000098 | heading | pages [4] -->
Notations

<!-- b000099 | caption | pages [4] -->
Table 1: Notations

<!-- b000100 | heading | pages [4] -->
Notation

<!-- b000101 | prose | pages [4] -->
vATP,i(i = 1, 2, 3)

<!-- b000102 | prose | pages [4] -->
Definition

<!-- b000103 | prose | pages [4] -->
the ATP production rate of each energy supply system evATP,i(i = 1, 2, 3) the maximum ATP production rate of each energy supply system vATP the overall ATP production rate µ the energy contained in unit ATP P the overall output power of the cyclist Pi(i = 1, 2, 3) the output power of different part Vx(x = CP, O2, LA) corresponding substance content αi(i = 1, 2, 3) conversion efficiency under three ways of energy supply Mx(x = CP, O2, LA) storage upper limit of corresponding substance fa fr fs m∗ air resistance rolling resistance slope resistance the effective mass of bicycle-cyclist system m the sum of mass of bicycle-cyclist system p coefficient of air resistance η F vr drivetrain efficiency propulsive force the relative velocity

<!-- b000104 | furniture | pages [5] -->
Team # 2212245

<!-- b000105 | furniture | pages [5] -->
Page 5 of 25

<!-- b000106 | heading | pages [5] -->
The Cyclist Energy Supply Model: A Mixture of Three Energy

<!-- b000107 | prose | pages [5] -->
3 Supply Systems

<!-- b000108 | prose | pages [5] -->
Each cyclist’s power curve is unique, due to different features of their energy supply system. For example, a sprinter has stronger explosive power, because of the better performance of ATP-CP energy supply system, which is the main energy supply system for short and extremely intense exercise.

<!-- b000109 | prose | pages [5] -->
As we know, ATP is the direct energy source of the human body. The ATP production speed and output power interrelated through a constant — the energy contained in unit ATP µ. Then the output power P and the ATP production rate vATP satisfy the following formula:

<!-- b000110 | prose | pages [5] -->
P = µvATP.

<!-- b000111 | prose | pages [5] -->
(1)

<!-- b000112 | prose | pages [5] -->
Generally, only a small amount of ATP is stored in the cells, and can exist for only 1-3s during intense exercise. The subsequent energy supply mainly relies on ATP regeneration.

<!-- b000113 | prose | pages [5] -->
There are three energy supply system in human body that can produce ATP to provide energy. They are ATP-CP system, glycolysis system and aerobic system[5] respectively. The overall output power is regarded as the sum of output power of each energy supply system:

<!-- b000114 | prose | pages [5] -->
P = P1 + P2 + P3.

<!-- b000115 | prose | pages [5] -->
(2) We are now going to discuss the ATP production of each energy supply system.

<!-- b000116 | prose | pages [5] -->
3.1 ATP-CP System

<!-- b000117 | prose | pages [5] -->
The decomposition of intracellular creatine phosphate (CP) can provide energy and inorganic phos- phate, so that ADP can resynthesize ATP. This process is shown in the following figure.

<!-- b000118 | caption | pages [5] -->
Figure 2: Schematic diagram of ATP-CP energy supply system

<!-- b000119 | prose | pages [5] -->
3.1.1 ATP Production of ATP-CP System

<!-- b000120 | prose | pages [5] -->
For CP consumption process, we can write

<!-- b000121 | prose | pages [5] -->
dVCP(t) = −vCPdt

<!-- b000122 | prose | pages [5] -->
 

<!-- b000123 | prose | pages [5] -->
vATP,1 = α1vCP

<!-- b000124 | prose | pages [5] -->
, (3)

<!-- b000125 | prose | pages [5] -->
VCP(t = 0) = MCP

<!-- b000126 | prose | pages [5] -->


<!-- b000127 | prose | pages [5] -->
where VCP is the CP concentration in human body, MCP is the maximum storage of CP in human body, α1 is the number of ATP produced by decomposing unit CP, vCP is the decomposition rate of CP. Solving (3), we obtain

<!-- b000128 | prose | pages [5] -->
α1VCP(t) = vATP,1τ, (4)

<!-- b000129 | furniture | pages [6] -->
Team # 2212245

<!-- b000130 | furniture | pages [6] -->
Page 6 of 25

<!-- b000131 | prose | pages [6] -->
where τ is the lasting time for given ATP production rate.

<!-- b000132 | prose | pages [6] -->
Due to the limitation of the actual biological structure, the speed of ATP production must be physi- ologically limited. Given the maximum ATP production speed of ATP-CP system is evATP,1, then using (1), we obtain

<!-- b000133 | prose | pages [6] -->
P1 = µvATP,1 = µ min

<!-- b000134 | prose | pages [6] -->
α1VCP

<!-- b000135 | prose | pages [6] -->


<!-- b000136 | prose | pages [6] -->
, evATP,1

<!-- b000137 | prose | pages [6] -->
.

<!-- b000138 | prose | pages [6] -->
(5)

<!-- b000139 | prose | pages [6] -->
τ

<!-- b000140 | prose | pages [6] -->
The ATP-CP process can be carried out under both anaerobic and aerobic conditions, and the dura- tion is about 6–8 seconds. The output power is very high, so it is the major energy supply system for short-time and intense exercise.

<!-- b000141 | prose | pages [6] -->
3.1.2 Restoration of CP

<!-- b000142 | prose | pages [6] -->
During aerobic breathing, the CP concentration in the human body is restored. If the restoration rate of CP is defined as vr1, then the formula and initial condition for restoration process is  dVCP(t) = vr1dt

<!-- b000143 | prose | pages [6] -->
.

<!-- b000144 | prose | pages [6] -->
(6) VCP(t = 0) = 0

<!-- b000145 | prose | pages [6] -->
When VCP reaches its maximum value MCP, the restoration finishes. After exhaustion, the restora- tion time of CP is about 3 – 5 min.

<!-- b000146 | prose | pages [6] -->
3.2 Glycolysis-Aerobic System

<!-- b000147 | prose | pages [6] -->
Glycolysis system and aerobic system cooperate closely with each other. We therefore consider them together in this subsection.

<!-- b000148 | caption | pages [6] -->
Figure 3: Schematic diagram of glycolysis and aerobic energy supply system

<!-- b000149 | prose | pages [6] -->
Under anaerobic conditions, glycogen, or glucose is degraded by glycolysis to produce lactate and ATP, and most of the energy is stored in lactate. This process is also a preparation pathway for glucose oxidative metabolism. Under aerobic conditions, lactate continues to decompose through oxidative metabolism to generate a large amount of ATP for energy. This process is represented by Fig. 3.

<!-- b000150 | prose | pages [6] -->
ATP Production of Glycolysis-Aerobic System 3.2.1

<!-- b000151 | prose | pages [6] -->
Similar with what we do in ATP-CP system, we can write the equations for glycolysis system.

<!-- b000152 | furniture | pages [7] -->
Team # 2212245

<!-- b000153 | prose | pages [7] -->


<!-- b000154 | prose | pages [7] -->
vout = kvde

<!-- b000155 | prose | pages [7] -->
 

<!-- b000156 | furniture | pages [7] -->
Page 7 of 25

<!-- b000157 | prose | pages [7] -->
dVO2(t) = (vin −vout)dt

<!-- b000158 | prose | pages [7] -->
   

<!-- b000159 | prose | pages [7] -->
dVLA(t) = (vge −vde)dt

<!-- b000160 | prose | pages [7] -->
  

<!-- b000161 | prose | pages [7] -->
vATP,2 = α2vge

<!-- b000162 | prose | pages [7] -->
, (7)

<!-- b000163 | prose | pages [7] -->
vATP,3 = α3vout

<!-- b000164 | prose | pages [7] -->
   

<!-- b000165 | prose | pages [7] -->
VO2(t = 0) = MO2

<!-- b000166 | prose | pages [7] -->
   

<!-- b000167 | prose | pages [7] -->
VLA(t = 0) = 0

<!-- b000168 | prose | pages [7] -->


<!-- b000169 | prose | pages [7] -->
where k is the oxygen needed to decompose unit lactate, α2, α3 is the number of ATP produced by generating unit lactate or consuming unit oxygen, VO2 is oxygen concentration of human body, MO2 is the maximum oxygen concentration, VLA is the lactate concentration, vin is the speed of lung providing oxygen for human body, vout is the speed of oxygen consumed by aerobic respiration, vge is the speed of sugar decomposition into lactate, and vde is the speed of lactate decomposition under aerobic conditions.

<!-- b000170 | prose | pages [7] -->
Solving the (7), we obtain

<!-- b000171 | prose | pages [7] -->


<!-- b000172 | prose | pages [7] -->
MLA −VLA + VO2 + vinτ

<!-- b000173 | prose | pages [7] -->


<!-- b000174 | prose | pages [7] -->
α2

<!-- b000175 | prose | pages [7] -->


<!-- b000176 | prose | pages [7] -->


<!-- b000177 | prose | pages [7] -->
= vATP,2τ

<!-- b000178 | prose | pages [7] -->
k

<!-- b000179 | prose | pages [7] -->
, (8)

<!-- b000180 | prose | pages [7] -->
α3(VO2 + vinτ) = vATP,3τ

<!-- b000181 | prose | pages [7] -->


<!-- b000182 | prose | pages [7] -->
Similar with the case in ATP-CP system, the speed of ATP production is physiologically limited, i.e., vATP,2 ⩽evATP,2 and vATP,3 ⩽evATP,3, using (1), we finally obtain

<!-- b000183 | prose | pages [7] -->
α2(MLA −VLA + VO2/k)

<!-- b000184 | prose | pages [7] -->
P2 = µvATP,2 = µ min

<!-- b000185 | prose | pages [7] -->


<!-- b000186 | prose | pages [7] -->
VO2

<!-- b000187 | prose | pages [7] -->
P3 = µvATP,3 = µ min

<!-- b000188 | prose | pages [7] -->
α3

<!-- b000189 | prose | pages [7] -->
τ

<!-- b000190 | prose | pages [7] -->
3.2.2 Restoration of Glycolysis Subsystem

<!-- b000191 | prose | pages [7] -->


<!-- b000192 | prose | pages [7] -->
+ vin

<!-- b000193 | prose | pages [7] -->
k , evATP,2

<!-- b000194 | prose | pages [7] -->
, (9)

<!-- b000195 | prose | pages [7] -->
τ

<!-- b000196 | prose | pages [7] -->


<!-- b000197 | prose | pages [7] -->


<!-- b000198 | prose | pages [7] -->
+ vin

<!-- b000199 | prose | pages [7] -->
, evATP,3

<!-- b000200 | prose | pages [7] -->
.

<!-- b000201 | prose | pages [7] -->
(10)

<!-- b000202 | prose | pages [7] -->
When the lactate concentration reaches the lactate threshold MLA, glycolysis ends. Glycolysis can con- tinue only if the glycolysis system is restored by decomposing lactate through aerobic respiration. And when oxygen concentration in human body is insufficient, the intensity of aerobic respiration will also be inhibited.

<!-- b000203 | prose | pages [7] -->
Overall Energy Supply : Put Them All Together 3.3

<!-- b000204 | prose | pages [7] -->
Real-world human energy supply is completed by all three energy supply systems at the same time. Whether a system is dominant or not mainly depends on the intensity level of exercise.

<!-- b000205 | prose | pages [7] -->
First, it should be noted that during the whole process of a race, the total sugar content in human body is fixed. However, in the actual race, there is generally no lack of sugar in the cyclist. What limits the cyclist in energy supply is muscle fatigue (which can be quantified by the concentration of lactate and CP) and other problems. Therefore, the limitation of total sugar will not actually take effect in our analysis.

<!-- b000206 | prose | pages [7] -->
We define an algorithm to determine the dominant energy supply process:

<!-- b000207 | furniture | pages [8] -->
Team # 2212245

<!-- b000208 | furniture | pages [8] -->
Page 8 of 25

<!-- b000209 | caption | pages [8] -->
Figure 4: Schematic diagram of overall energy supply

<!-- b000210 | prose | pages [8] -->
The human body sends out instructions to output a certain power P and its duration t. Step 1

<!-- b000211 | prose | pages [8] -->
According to the duration t and the current concentrations of CP, lactate and oxygen in human Step 2 body, the maximum output power limit Plimit is calculated.

<!-- b000212 | prose | pages [8] -->
Step 3 Select the dominant energy supply system according to the power needed. When the power is low, the aerobic system can meet the power requirements ; when the aerobic power is not enough, consider adding glycolysis system, or even ATP-CP system for energy supply. If the power of all three energy supply systems in total is still not adequate, then report unachievable.

<!-- b000213 | prose | pages [8] -->
Finally, considering the effect of adrenaline and other hormone, the model above can be further modified. When the three energy supply systems work together and still can not meet the power output requirements, it is allowed to forcibly exceed the power limit through glycolysis within a limited range, at the cost of producing more lactate, namely, the part exceeding the lactate threshold. With the

<!-- b000214 | heading | pages [8] -->
introduction of the over-limit constant e > 1, we modify (2) to

<!-- b000215 | prose | pages [8] -->
P ⩽e(P1 + P2 + P3).

<!-- b000216 | prose | pages [8] -->
(11)

<!-- b000217 | prose | pages [8] -->
Compared with normal glycolysis, the glycolysis beyond lactate threshold is more incomplete. Therefore, if we introduce the constant b describing incomplete decomposition, the content of newly produced lactate is

<!-- b000218 | prose | pages [8] -->
dVLA = b [P −(P1 + P2 + P3)] dt (12)

<!-- b000219 | prose | pages [8] -->
4

<!-- b000220 | heading | pages [8] -->
Application of Energy Supply Model : Power Profiles of the Cy-

<!-- b000221 | prose | pages [8] -->
clists

<!-- b000222 | prose | pages [8] -->
After the establishment of energy supply model for cyclists, we can discuss the power profiles in depth.

<!-- b000223 | prose | pages [8] -->
4.1

<!-- b000224 | heading | pages [8] -->
Solving Power Curves Based on Energy Supply Model

<!-- b000225 | prose | pages [8] -->
The cyclist’s power curve describes the length of time it maintains different levels of output power, which is easy to obtain by our energy supply model.

<!-- b000226 | prose | pages [8] -->
According to the definition of power curve, the overall power curve is the sum of the power curves of the three energy supply systems.

<!-- b000227 | furniture | pages [9] -->
Team # 2212245

<!-- b000228 | furniture | pages [9] -->
Page 9 of 25

<!-- b000229 | prose | pages [9] -->
VCP(t = 0) = MCP

<!-- b000230 | prose | pages [9] -->
VO2(t = 0) = MO2 VLA(t = 0) = 0 After assigning the initial value above and other relevant parameters according to the rider’s char- acteristics, the cyclist’s power curve can be obtained by summing the expressions of the power curves of the three energy supply systems in the energy supply model.

<!-- b000231 | prose | pages [9] -->
Due to the complexity of the actual biological process, the meaningful value of parameters is the relative value between parameters, not the absolute value; The power curve and power value obtained have been processed to remove the effect of cyclist’s weight, that is, the power value displayed below multiplied by the cyclist’s weight is the actual output power.

<!-- b000232 | prose | pages [9] -->
4.2 Gender Differences in Cyclists

<!-- b000233 | prose | pages [9] -->
The power curve features of cyclists of different genders are also significantly different.

<!-- b000234 | prose | pages [9] -->
To begin with, we introduce the four most important values on the power curve:[6]

<!-- b000235 | prose | pages [9] -->
• sprint abilities (power at 5s)

<!-- b000236 | prose | pages [9] -->
• anaerobic capacity (power at 1min)

<!-- b000237 | prose | pages [9] -->
• VO2 max capability (power at 5min)

<!-- b000238 | prose | pages [9] -->
• functional threshold power (power at 1h)

<!-- b000239 | prose | pages [9] -->
FTP stands for Functional Threshold Power. It estimates the highest average power the cyclist can sustain for one hour. In cycling, FTP is a measure of fitness and indicates the amount of work you can sustain for long durations.[7]

<!-- b000240 | prose | pages [9] -->
VO2Max is the first zone above "Threshold" zone it starts from 105% of your FTP and ends on 120%.[8] The advantage of VO2Max helps the cyclist to excel at short and punchy climbs.[9]

<!-- b000241 | prose | pages [9] -->
We will show the differences between cyclists of different genders by comparing the above four characteristic values of male and female cyclists of different levels. The analysis is based on the data retrieved online.[6]

<!-- b000242 | caption | pages [9] -->
Figure 5: Comparison between male and female cyclists

<!-- b000243 | prose | pages [9] -->
The horizontal axis represents different levels of cyclists. Smaller number indicates higher level of the cyclists; The longitudinal axis is the power value after weight removal treatment; Four colors rep- resent the four important reference values respectively; Solid dots represent men and dotted triangles represents women.

<!-- b000244 | prose | pages [9] -->
By analyzing the data, it is not difficult to reach to the following conclusions:

<!-- b000245 | furniture | pages [10] -->
Team # 2212245

<!-- b000246 | furniture | pages [10] -->
Page 10 of 25

<!-- b000247 | prose | pages [10] -->
• The output power intensity of female riders is lower than that of male riders in all duration length, and the difference is more obvious with the increase of rider level;

<!-- b000248 | prose | pages [10] -->
• Although the ability of female riders of the same level is lower than that of male riders gener- ally, the difference is greater in short-term explosive power, while the difference in long-term endurance is relatively small.

<!-- b000249 | prose | pages [10] -->
The above conclusions are also consistent with the physiological characteristics of men and women.

<!-- b000250 | prose | pages [10] -->
Power Profiles of Time Trial Specialists 4.3

<!-- b000251 | prose | pages [10] -->
Based on Python, we use Numpy, Sympy and other libraries to simulate, solve and analyze our model. Time trial specialists are characterized by strong endurance, high level of fatigue endurance and the ability to keep close to the threshold power for a long time.

<!-- b000252 | prose | pages [10] -->
The values of important parameters are shown in the Table. 4.

<!-- b000253 | caption | pages [10] -->
Table 2: Physical Fitness of Time Trial Specialists

<!-- b000254 | prose | pages [10] -->
MCP vin MO2

<!-- b000255 | prose | pages [10] -->
Male 30 1.6 13000 Female 22 1.6 10500

<!-- b000256 | prose | pages [10] -->
MLA evATP,1 evATP,2 evATP,3

<!-- b000257 | prose | pages [10] -->
220 20 7.1 5 180 18 6.8 4.8

<!-- b000258 | prose | pages [10] -->
Using the algorithm in section 3.3, the overall power curve can be calculated. The result is shown in

<!-- b000259 | caption | pages [10] -->
Fig. 6 (the power curves of three energy supply systems are also given). In order to show the difference

<!-- b000260 | prose | pages [10] -->
of the power curve at the beginning more clearly, logarithmic coordinates is used in the right figure.

<!-- b000261 | caption | pages [10] -->
Figure 6: Theoretical power profile of male time trial specialists

<!-- b000262 | caption | pages [10] -->
Figure 7: Theoretical power profile of female time trial specialists

<!-- b000263 | prose | pages [10] -->
The four characteristic powers are listed in Table. 5.

<!-- b000264 | furniture | pages [11] -->
Team # 2212245

<!-- b000265 | furniture | pages [11] -->
Page 11 of 25

<!-- b000266 | caption | pages [11] -->
Table 3: Characteristic Powers of Time Trial Specialists

<!-- b000267 | prose | pages [11] -->
Duration

<!-- b000268 | prose | pages [11] -->
Male Power/Watt · kg−1 Female

<!-- b000269 | prose | pages [11] -->
5s 1min 5min FTP(1h)

<!-- b000270 | prose | pages [11] -->
18.10 9.17 5.83 5.07 16.00 8.17 5.47 4.58

<!-- b000271 | prose | pages [11] -->
We will display the following result in the way similar with this section and not repeat the explana- tion later.

<!-- b000272 | prose | pages [11] -->
4.4 Power Profiles of Sprinters

<!-- b000273 | prose | pages [11] -->
Sprinters are characterized by strong explosive power and can produce high power in a short time, so they are expert in sprinting.

<!-- b000274 | caption | pages [11] -->
Table 4: Physical Fitness of Sprinters

<!-- b000275 | prose | pages [11] -->
MCP vin MO2

<!-- b000276 | prose | pages [11] -->
Male 55 1.32 11000 Female 50 1.2 10000

<!-- b000277 | prose | pages [11] -->
MLA evATP,1 evATP,2 evATP,3

<!-- b000278 | prose | pages [11] -->
285 25 7.3 3.98 265 24 7.12 3.75

<!-- b000279 | caption | pages [11] -->
Figure 8: Theoretical power profile of male sprinters

<!-- b000280 | caption | pages [11] -->
Figure 9: Theoretical power profile of female sprinters

<!-- b000281 | caption | pages [11] -->
Table 5: Characteristic powers of sprinters

<!-- b000282 | prose | pages [11] -->
Duration

<!-- b000283 | prose | pages [11] -->
Male Power/Watt · kg−1 Female

<!-- b000284 | prose | pages [11] -->
5s 1min 5min FTP(1h)

<!-- b000285 | prose | pages [11] -->
22.28 9.65 5.11 4.07 20.87 9.00 4.80 3.84

<!-- b000286 | furniture | pages [12] -->
Team # 2212245

<!-- b000287 | furniture | pages [12] -->
Page 12 of 25

<!-- b000288 | prose | pages [12] -->
The results given by our model tally well with the real-world data, which proves the reliability of the model. We therefore can estimate the abilities of three energy supply systems from given cyclist’s power curve. With our model, we make it possible to evaluate the explosive power beyond their power curves and recovery time, which guides the strategy to choose.

<!-- b000289 | prose | pages [12] -->
5

<!-- b000290 | heading | pages [12] -->
The Cyclist Motion Model

<!-- b000291 | prose | pages [12] -->
Before we can talk about strategies on the course, we need to establish a model to describe the motion of cyclists.

<!-- b000292 | prose | pages [12] -->
5.1 Drag Resistances in Cyclist Motion

<!-- b000293 | prose | pages [12] -->
The motion of cyclists is affected by various types of drag resistances, including aerodynamic resis- tance, drivetrain resistance, slope resistance and rolling resistance. The influence of each kind of resis- tance is analyzed below.

<!-- b000294 | prose | pages [12] -->
5.1.1 Aerodynamic Resistance

<!-- b000295 | prose | pages [12] -->
Aerodynamic resistance is a significant part of the resistance for high-speed bicycles on flat roads. The aerodynamic resistance of the cyclist (and the bicycle) can be divided into differential pressure resistance and friction resistance.

<!-- b000296 | prose | pages [12] -->
When there is a relative movement between the cyclist and the air, the cyclist and the bicycle com- press the air ahead, which means there will be a relatively high pressure area in the front of the cyclist, while there will be a relatively low pressure area behind the cyclist due to air escape. The pressure difference between these two parts constitutes the differential pressure resistance. At the same time, when the cyclist moves at high speed, the air will produce a friction resistance on the surface of the bicycle body and the human body.

<!-- b000297 | prose | pages [12] -->
The practical discussion of aerodynamic resistance is rather complicated. According to classical fluid mechanics, aerodynamic resistance can be shown as the following formula:[10]

<!-- b000298 | prose | pages [12] -->
fa = 1

<!-- b000299 | prose | pages [12] -->
2CρSv2 r , (13)

<!-- b000300 | prose | pages [12] -->
where fa is aerodynamic resistance force, C is resistance coefficient, ρ is the density of the air, S is the frontal area of the cyclist and vr is relative velocity between the cyclist and the air. Considering that for a particular cyclist, the first three parameters keep almost unchanged during the race, the formula can be rewritten in the following form :

<!-- b000301 | prose | pages [12] -->
fa = pv2

<!-- b000302 | prose | pages [12] -->
5.1.2 Drivetrain Resistance

<!-- b000303 | prose | pages [12] -->
r .

<!-- b000304 | prose | pages [12] -->
(13a)

<!-- b000305 | prose | pages [12] -->
During cycling, some energy provided by the cyclist is wasted due to drivetrain resistance, the fric- tions between drivetrain components. The energy loss caused by drivetrain resistance can be indicated by the drivetrain efficiency η. For real bicycles designed for races, the drivetrain efficiency averages around 0.95.[11] We therefore assume the drivetrain efficiency η = 0.95.

<!-- b000306 | prose | pages [12] -->
5.1.3 Slope Resistance

<!-- b000307 | prose | pages [12] -->
We regard the gravity component of the bicycle parallel to the slope as a part of the resistance, which is so-called slope resistance. Given that the inclination angle of the slope is α, it is easy to show that

<!-- b000308 | furniture | pages [13] -->
Team # 2212245

<!-- b000309 | prose | pages [13] -->
fs = mg sin α,

<!-- b000310 | furniture | pages [13] -->
Page 13 of 25

<!-- b000311 | prose | pages [13] -->
−π

<!-- b000312 | prose | pages [13] -->
2 , π

<!-- b000313 | prose | pages [13] -->
h

<!-- b000314 | prose | pages [13] -->
i

<!-- b000315 | prose | pages [13] -->
α ∈

<!-- b000316 | prose | pages [13] -->
, (14)

<!-- b000317 | prose | pages [13] -->
2

<!-- b000318 | prose | pages [13] -->
where fs is slope resistance, α is positive for uphill, and negative for downhill.

<!-- b000319 | prose | pages [13] -->
5.1.4 Rolling Resistance

<!-- b000320 | prose | pages [13] -->
Rolling resistance is generally caused by the deformation of the wheel or ground and can be expressed by the following equation:

<!-- b000321 | prose | pages [13] -->
fr = CrrN, (15)

<!-- b000322 | prose | pages [13] -->
where fr is the rolling resistance, Crr is the rolling resistance coefficient (RRC), N is the normal force perpendicular to the road. The RRCs of ordinary bicycle tires vary from 0.007 to 0.014,[12] and for bicycles designed for races, the RRC can be as low as 0.004, according to the coasting-down experi- ments.[13]

<!-- b000323 | prose | pages [13] -->
If the cyclist is on a slope with inclination angle α, the normal force can be given by N = mg cos α, so the formula (15) can be written as

<!-- b000324 | prose | pages [13] -->
fr = Crrmg cos α.

<!-- b000325 | prose | pages [13] -->
5.2 Linear Motion of Cyclists

<!-- b000326 | prose | pages [13] -->
(16)

<!-- b000327 | prose | pages [13] -->
Taking the drivetrain efficiency η into account, the equation of cyclist power is

<!-- b000328 | prose | pages [13] -->
ηP = Fv, (17)

<!-- b000329 | prose | pages [13] -->
which shows the relation between the output power of the cyclist P, current velocity of the cyclist v and the propulsive force F.

<!-- b000330 | prose | pages [13] -->
The critical theorem here is the work-energy principle, that the change in the kinetic energy is equal to the work done by the external forces.[14] The kinetic energy is the sum of translational energy 1

<!-- b000331 | prose | pages [13] -->
2Iω2 =

<!-- b000332 | prose | pages [13] -->
2mv2

<!-- b000333 | prose | pages [13] -->
2(I/R2)v2 for each wheel, where m is the mass of the cyclist and the

<!-- b000334 | prose | pages [13] -->
and rotational energy 1

<!-- b000335 | prose | pages [13] -->
1

<!-- b000336 | prose | pages [13] -->
bicycle, R is the outer radius of bicycle wheels and I is the moment of inertia of the wheels. We therefore obtain

<!-- b000337 | prose | pages [13] -->
1

<!-- b000338 | prose | pages [13] -->


<!-- b000339 | prose | pages [13] -->


<!-- b000340 | prose | pages [13] -->


<!-- b000341 | prose | pages [13] -->
d

<!-- b000342 | prose | pages [13] -->
m + 2I

<!-- b000343 | prose | pages [13] -->
v2

<!-- b000344 | prose | pages [13] -->
R2

<!-- b000345 | prose | pages [13] -->
dt

<!-- b000346 | prose | pages [13] -->
2

<!-- b000347 | prose | pages [13] -->
Simple calculation of (18) shows that

<!-- b000348 | prose | pages [13] -->


<!-- b000349 | prose | pages [13] -->


<!-- b000350 | prose | pages [13] -->
m + 2I

<!-- b000351 | prose | pages [13] -->
m∗a =

<!-- b000352 | prose | pages [13] -->
R2

<!-- b000353 | prose | pages [13] -->
= (F −fa −fr −fs) v.

<!-- b000354 | prose | pages [13] -->
(18)

<!-- b000355 | prose | pages [13] -->
a = F −fa −fr −fs, (19)

<!-- b000356 | prose | pages [13] -->
where m∗= m + 2I/R2 is effective mass of the cyclist and the bicycle, a is the acceleration of the cyclist.

<!-- b000357 | furniture | pages [14] -->
Team # 2212245

<!-- b000358 | prose | pages [14] -->
5.3 Cyclist Motion on the Curved Road

<!-- b000359 | furniture | pages [14] -->
Page 14 of 25

<!-- b000360 | prose | pages [14] -->
Cyclists lean inwards while riding along a curved road for the maximum speed. This method is called inclination method.

<!-- b000361 | prose | pages [14] -->
Cyclists keep their bicycle in a straight line when passing the curve, and at the same time make the bicycle incline to the inside of the curve. The resultant force of ground support for the bicycle and its own gravity provides centripetal acceleration for the circular motion of the bicycle. This strategy can obtain a high curve speed, and is also conducive to observing the road ahead.

<!-- b000362 | caption | pages [14] -->
Figure 10: Inclination Method for the Curved Road

<!-- b000363 | prose | pages [14] -->
As shown by Fig. 10, the blue rectangle represents the bicycle, the yellow arrow represents the support force of the bicycle and the total gravity of the cyclist and the bicycle. The red arrow represents the resultant force of the bicycle, which is the centripetal force required for passing the curved road, thus obtaining the following formula:

<!-- b000364 | prose | pages [14] -->
mv2

<!-- b000365 | prose | pages [14] -->
r = mg

<!-- b000366 | prose | pages [14] -->
tan β .

<!-- b000367 | prose | pages [14] -->
(20)

<!-- b000368 | prose | pages [14] -->
Considering the restrictions from friction between the bicycle tire and ground, the formula should mv2

<!-- b000369 | prose | pages [14] -->
r = mg

<!-- b000370 | prose | pages [14] -->
be:

<!-- b000371 | prose | pages [14] -->
tan β ≤kmg.

<!-- b000372 | prose | pages [14] -->
(21)

<!-- b000373 | prose | pages [14] -->
Therefore, the maximum speed allowed for passing the curved road is

<!-- b000374 | prose | pages [14] -->
vm =

<!-- b000375 | prose | pages [14] -->
p

<!-- b000376 | prose | pages [14] -->
grk , (22)

<!-- b000377 | prose | pages [14] -->
where g is the acceleration of gravity, r is the radius of curve, and k is the coefficient of ground friction, which is about 0.3. When the radius of curvature of the curve is large, the restrictions becomes fairly loose. Under such situations, the motion of the cyclists is approximately equivalent to moving on a straight road.

<!-- b000378 | prose | pages [14] -->
The Optimal Strategy for Individual Time Trial 6

<!-- b000379 | prose | pages [14] -->
Considering the actual possible state of the rider, it will include the following three: 1. Output power is greater than the threshold value, physical consumption. 2. The output power is equal to the balance value, no physical consumption 3. Output power is lower than the threshold value, it restores the physical strength. The following is the strategy selection model after taking the energy supply model and road condition into consideration:

<!-- b000380 | furniture | pages [15] -->
Team # 2212245

<!-- b000381 | furniture | pages [15] -->
Page 15 of 25

<!-- b000382 | caption | pages [15] -->
Figure 11: Optimal Strategy for Individual Time Trial

<!-- b000383 | prose | pages [15] -->
6.1 Strategy for Flat Straight Courses

<!-- b000384 | prose | pages [15] -->
Let’s start from the simplest situation, where cyclists ride on a flat road in straight line. It is conceivable that maintaining higher speed corresponds to higher power output. Here are two strategies:

<!-- b000385 | prose | pages [15] -->
• The rider keeps moving at a specific speed, at which the threshold value of the output power is just enough to make the rider move at a constant speed.

<!-- b000386 | prose | pages [15] -->
• The rider alternates with high power and low power, and the actual performance is to acceler- ate and decelerate alternately. The acceleration process and deceleration process need to keep symmetry, so that the process can be established.

<!-- b000387 | prose | pages [15] -->
Speed change process: a = v0 −v

<!-- b000388 | prose | pages [15] -->
m∗v0vP0 + ∆P

<!-- b000389 | prose | pages [15] -->
m∗v

<!-- b000390 | prose | pages [15] -->
For alternating between two speeds, it requires strict control of parameters such as time and accel- eration, which is relatively difficult for riders to achieve. On the other hand, it does not provide more energy in a cycle than a strategy of maintaining speed:

<!-- b000391 | prose | pages [15] -->
Z

<!-- b000392 | prose | pages [15] -->
Z

<!-- b000393 | prose | pages [15] -->
v3dt + f

<!-- b000394 | prose | pages [15] -->
Pt = a

<!-- b000395 | prose | pages [15] -->
vdt (23)

<!-- b000396 | prose | pages [15] -->
In the case of variable speed, where the average speed remains constant, the energy demand is higher, so a reasonable strategy would be to keep moving at a certain speed. That is, to first accelerate in the shortest possible time to a given speed at which the rider is able to maintain a constant speed.

<!-- b000397 | prose | pages [15] -->
6.2 Strategy for Sharp Turning and Hilly Course

<!-- b000398 | prose | pages [15] -->
For curves, if the speed is greater than the maximum speed allowed for the curves, slow down to this speed when entering the curves and maintain it, and follow the straight strategy when leaving the curves and entering the straights.

<!-- b000399 | prose | pages [15] -->
There are two solutions for going uphill from the straight:

<!-- b000400 | prose | pages [15] -->
1. If the uphill section is long, the uphill can be regarded as a straight with extra resistance. Referring to the above analysis, the strategy we choose is to slow down only at the moment before the uphill.

<!-- b000401 | furniture | pages [16] -->
Team # 2212245

<!-- b000402 | furniture | pages [16] -->
Page 16 of 25

<!-- b000403 | prose | pages [16] -->
2. If the uphill section is short, it is also possible to slow down a short distance before going uphill to regain your strength and then leave the uphill section as fast as possible.

<!-- b000404 | prose | pages [16] -->
For downhills, use the same strategy as for the straight. When entering the straight from downhill, adopt the strategy selection of entering uphill from straight.

<!-- b000405 | prose | pages [16] -->
7

<!-- b000406 | heading | pages [16] -->
Model Application on Time Trial Courses

<!-- b000407 | prose | pages [16] -->
In this section, we first model three courses. One is a simple self-designed course, the others are real- world courses in 2021.

<!-- b000408 | prose | pages [16] -->
7.1

<!-- b000409 | heading | pages [16] -->
The Course Models

<!-- b000410 | caption | pages [16] -->
Figure 12: Simple self-designed course

<!-- b000411 | prose | pages [16] -->
We begin with our self-designed course, which is made up of straights, ramps, 90° and 180° curves. The actual shape and parameters are already marked in Fig. 12.

<!-- b000412 | prose | pages [16] -->
The real-world courses are reconstructed by straight lines and arcs. And the altitude change was assigned by estimation. In the case that the average speed of the 2021’s Olympic champion is about 13 km/h, we only count the curves with radius less than 60 m. Curves with larger radius is considered equivalent to straight roads.

<!-- b000413 | prose | pages [16] -->
(a) Actual Course (b) Model

<!-- b000414 | caption | pages [16] -->
Figure 13: 2021 Olympic ITT Course (Female) in Tokyo, Japan

<!-- b000415 | prose | pages [16] -->
Under the condition that some arcs are ignored, the length of a lap of the reconstructed model is 21.1 km, and the error is about 4.5% compared with the total length of the actual course, which is acceptable.

<!-- b000416 | furniture | pages [17] -->
Team # 2212245

<!-- b000417 | prose | pages [17] -->
(a) Actual Course

<!-- b000418 | furniture | pages [17] -->
Page 17 of 25

<!-- b000419 | prose | pages [17] -->
(b) Model

<!-- b000420 | caption | pages [17] -->
Figure 14: 2021 UCI World Championship ITT Course (Male) in Flanders, Belgium

<!-- b000421 | prose | pages [17] -->
The same method was adopted to model the course of UCI World Championship Time Trial Course in Belgium. The reconstructed model has a total length of 43.0 km, and the error is about 3% compared with the actual course of 44.3 km.

<!-- b000422 | prose | pages [17] -->
7.2

<!-- b000423 | heading | pages [17] -->
Model Application Results

<!-- b000424 | caption | pages [17] -->
Table 6: The Time Needed for Each Course

<!-- b000425 | prose | pages [17] -->
Male Sprinter Time(min) Male TT Specialist

<!-- b000426 | prose | pages [17] -->
Tokyo 28.10 31.32 Belgium 53.02 57.02 Self-designed 21.01 22.95

<!-- b000427 | prose | pages [17] -->
Female TT Specialist Female Sprinter

<!-- b000428 | prose | pages [17] -->
32.69 32.72 54.23 58.74 22.41 23.85

<!-- b000429 | prose | pages [17] -->
On the course in Tokyo and Belgium, our model application results are slightly inferior to the actual world championship’s results, but it also shows the rationality of our model. According to the results, we can see that men perform better than women, and TT specialist perform better than sprinter. Here comes more detailed information of the results:

<!-- b000430 | prose | pages [17] -->
(a) Self-designed

<!-- b000431 | furniture | pages [18] -->
Team # 2212245

<!-- b000432 | furniture | pages [18] -->
Page 18 of 25

<!-- b000433 | prose | pages [18] -->
(b) Tokyo

<!-- b000434 | prose | pages [18] -->
(c) Belgium

<!-- b000435 | caption | pages [18] -->
Figure 15: The Relationship Between Power, Velocity and Position on the Course

<!-- b000436 | prose | pages [18] -->
In the model we build, the riders follow the strategy we set up very well. Our decisions are based on road conditions, which are also reflected in the figure above. When competitors adopt the same strategy in the course, their performance is related to their basic qualities.At the same time, we can also see that in the case of large changes in terrain, the speed will be affected by the addition, which is also consistent with the reality.

<!-- b000437 | heading | pages [18] -->
Sensitivity Analysis of the deviations from the target power

<!-- b000438 | prose | pages [18] -->
7.3

<!-- b000439 | caption | pages [18] -->
Figure 16: Simple Self-designed course

<!-- b000440 | caption | pages [18] -->
Table 7: Time to Finish Under Different Deviations of Our Strategy

<!-- b000441 | prose | pages [18] -->
Deviation 0 -10% -20%

<!-- b000442 | prose | pages [18] -->
Time(s) 1260.80 1272.55 1306.60

<!-- b000443 | prose | pages [18] -->
± 20% ± 30% -30% -40%

<!-- b000444 | prose | pages [18] -->
1358.67 1445.73 1289.00 1300.04

<!-- b000445 | furniture | pages [19] -->
Team # 2212245

<!-- b000446 | furniture | pages [19] -->
Page 19 of 25

<!-- b000447 | prose | pages [19] -->
From the figure and table above, we can see that even though the target power is only 70% of the ideal target, this produces a time deviation of only 7.76%. And when the target power missed the ideal target range by 30%, resulting in a time deviation of only 3.11%. This data shows that our strategy model is not very sensitive to the deviation of the player’s target power, which means that our strategy has better value in practical use.

<!-- b000448 | prose | pages [19] -->
The Impact of Weather on Cycling 8

<!-- b000449 | prose | pages [19] -->
8.1 Influence of weather

<!-- b000450 | prose | pages [19] -->
In cycling, the weather and road conditions all affect the performance of the cyclists. Among the various weather factors, we mainly focus on wind, direction, and precipitation conditions.

<!-- b000451 | prose | pages [19] -->
In the straight motion of bicycle, the wind and direction mainly affect the air resistance, thus af- fecting the actual performance of athletes on the course. But during the turn, the wind direction is constantly changing relative to the cyclist’s speed, so we need to discuss the average air resistance under the wind.

<!-- b000452 | prose | pages [19] -->
Suppose that the bicycle needs to turn an angle of γ and a radius of R, and the wind direction is decomposed into two components perpendicular to and along the initial movement direction of the cyclist, which are vx and vy respectively.

<!-- b000453 | caption | pages [19] -->
Figure 17: Impact of Wind on Sharp Turning

<!-- b000454 | prose | pages [19] -->
After time t, the bike moves from the original blue square position to the yellow square position:

<!-- b000455 | prose | pages [19] -->
µP = pv2

<!-- b000456 | prose | pages [19] -->
φ = vt

<!-- b000457 | prose | pages [19] -->
r ,

<!-- b000458 | prose | pages [19] -->
r v (24)

<!-- b000459 | prose | pages [19] -->
γ = vT

<!-- b000460 | prose | pages [19] -->
(25) r

<!-- b000461 | prose | pages [19] -->
vr = v + vx sin φ + vy cos φ (26)

<!-- b000462 | prose | pages [19] -->
We then can calculate the average wind resistance via an integral:

<!-- b000463 | prose | pages [19] -->
¯fT = p

<!-- b000464 | prose | pages [19] -->
Z T

<!-- b000465 | prose | pages [19] -->
v2

<!-- b000466 | prose | pages [19] -->
r dt (27)

<!-- b000467 | prose | pages [19] -->
0

<!-- b000468 | prose | pages [19] -->
In particular, we calculate the average wind resistance when the turning angle γ is π/2 and π. The results are

<!-- b000469 | prose | pages [19] -->


<!-- b000470 | prose | pages [19] -->
v2 + 1

<!-- b000471 | prose | pages [19] -->
¯fπ/2 = p

<!-- b000472 | prose | pages [19] -->
v2

<!-- b000473 | prose | pages [19] -->
x −v2

<!-- b000474 | prose | pages [19] -->
 

<!-- b000475 | prose | pages [19] -->
y

<!-- b000476 | prose | pages [19] -->
2

<!-- b000477 | prose | pages [19] -->
and

<!-- b000478 | prose | pages [19] -->


<!-- b000479 | prose | pages [19] -->


<!-- b000480 | prose | pages [19] -->
+ 2

<!-- b000481 | prose | pages [19] -->
 

<!-- b000482 | prose | pages [19] -->
π [2v (vx + vy) + vxvy]

<!-- b000483 | prose | pages [19] -->
(28)

<!-- b000484 | prose | pages [19] -->


<!-- b000485 | prose | pages [19] -->
v2 + 4

<!-- b000486 | prose | pages [19] -->
¯fπ = p

<!-- b000487 | prose | pages [19] -->
πvvx

<!-- b000488 | prose | pages [19] -->
.

<!-- b000489 | prose | pages [19] -->
(29)

<!-- b000490 | prose | pages [19] -->
In the case of rain, the water will change the friction coefficient of the road surface. Referring to the analysis of the sharp turning, it can be found that the maximum speed allowed by the bicycle cornering decreases, which will affect the riding strategy of the rider.

<!-- b000491 | furniture | pages [20] -->
Team # 2212245

<!-- b000492 | furniture | pages [20] -->
Page 20 of 25

<!-- b000493 | prose | pages [20] -->
8.2

<!-- b000494 | heading | pages [20] -->
Sensitivity Analysis of the weather

<!-- b000495 | caption | pages [20] -->
Figure 18: The relationship between wind and completion time

<!-- b000496 | caption | pages [20] -->
Figure 19: detailed information

<!-- b000497 | prose | pages [20] -->
We take the male specialists as an example, and let him test to finish our self-designed course in various wind conditions. The results are summarized as above.

<!-- b000498 | prose | pages [20] -->
√

<!-- b000499 | prose | pages [20] -->
2m/s, we can

<!-- b000500 | prose | pages [20] -->
According to the left picture in Figure 17, which is plotted at a wind speed of 5

<!-- b000501 | prose | pages [20] -->
assume that the wind direction does significantly affect the time needed to finish the race. The influence of wind direction on the race is very related to the course itself, which means that the symmetry shown in the picture can be explained, because our self-designed course has a certain symmetry.

<!-- b000502 | prose | pages [20] -->
With a wind direction fixed at 45° and a gradual increase in wind speed, it can also be seen that the average speed of the cyclist is greatly affected. In the Figure 18, the figures in brackets show the wind speed and direction respectively. We know that the influence of wind condition on the driver is a relatively complex process, which is not only related to the race field, but also affects the driver’s strategy choice.

<!-- b000503 | prose | pages [20] -->
9

<!-- b000504 | heading | pages [20] -->
Modified Model for Team Time Trial

<!-- b000505 | heading | pages [20] -->
Additional Assumptions

<!-- b000506 | prose | pages [20] -->
We need more assumptions to extend our ITT model for Team Time Trials.

<!-- b000507 | prose | pages [20] -->
• All six members of the team are of the same or similar physical quality. In the case of differences in the physical quality of riders, the problem will be much more complicated.

<!-- b000508 | furniture | pages [21] -->
Team # 2212245

<!-- b000509 | furniture | pages [21] -->
Page 21 of 25

<!-- b000510 | prose | pages [21] -->
• In the queue, the team members are arranged compactly. We believe that the specific handover process is approximately equivalent to the result after ignoring the factors including the time spent retreating from the front to the back of the queue and the resulting acceleration, decelera- tion, and position change. Rotate to Take Pulls

<!-- b000511 | prose | pages [21] -->
In team time trials, a few cyclists can ride at the front of the team, while other teammates draft behind in the slipstream. The cyclists taking pulls then rotate to the back. The drafting effect can reduce the overall aerodynamic to at most 2/3 resistance.[15]

<!-- b000512 | prose | pages [21] -->
It is assumed that when a cyclist is taking a pull, the air resistance of the following cyclists is reduced to 75% of the original. When the leader advances with the output power higher than his threshold value, the following five riders can recover their strength with the output power lower than their threshold value.

<!-- b000513 | prose | pages [21] -->
9.1 Team Strategy before Sprint Stage

<!-- b000514 | prose | pages [21] -->
The strategy is taking turns riding a certain distance in front, until their energy are nearly exhausted, and then they fall to the back of the queue to recover, so that the group as a whole is actually always faster than the individual rider. Suppose that the overall movement speed of the team is V , then ac- cording to the movement model, the power demands of the first rider and other riders can be obtained as P0 and P1 respectively:

<!-- b000515 | prose | pages [21] -->
µP0 = v (fair + fother ) (30) µP1 = v (0.75fair + fother ) (31) According to the energy supply model, it can be determined that the rider can persist for T0 under the condition of P0 output power, and the rider with complete fatigue can fully recover for T1 under the condition of P1 output power. In order to implement the strategy of taking pulls, it is necessary to satisfy T1 ≤5T0 . Under this limitation, we can find the maximum speed that can meet the require- ments.

<!-- b000516 | prose | pages [21] -->
For curves, uphill and downhill sections, the team is considered to have the same pull taking pro- cess on them as on straight roads. Consider the team as a whole, and its strategy for moving forward is consistent with the individual’s strategy on these roads.

<!-- b000517 | prose | pages [21] -->
9.2 Team Strategy for Final Sprint Stage We propose a strategy that abandons the recovery of the rider’s physical strength. Improve the overall speed of the team, so that each rider behind the first rider can’t recover their physical strength, that is, P1 is equal to the threshold output power.

<!-- b000518 | prose | pages [21] -->
After the first rider has exhausted his physical strength or even exceeded the power output curve, he will give up chasing the team. The second rider then repeats the strategy of the first rider and breaks away from the team.

<!-- b000519 | caption | pages [21] -->
Figure 20: Optimal Strategy for Individual Time Trial

<!-- b000520 | furniture | pages [22] -->
Team # 2212245

<!-- b000521 | furniture | pages [22] -->
Page 22 of 25

<!-- b000522 | prose | pages [22] -->
The distance between the rider and the finish line is L, the last four players consume their physical strength for further acceleration to reach v. It is assumed that the power level of the first rider consumes their physical strength at a rate of U0, and that of the next three riders is U1. Their remaining physical strength is 3V , 2V , V and 0 respectively, and the limit of physical strength consumption beyond the energy supply curve is M. The pull taking time of the four riders is ti(i = 1, 2, 3, 4) respectively, and the threshold speed of the team in the six-man straight line stage was v0, then the following formula could be obtained:

<!-- b000523 | prose | pages [22] -->


<!-- b000524 | prose | pages [22] -->
X

<!-- b000525 | prose | pages [22] -->
V (i −1) + M = u1

<!-- b000526 | prose | pages [22] -->
   

<!-- b000527 | prose | pages [22] -->
4 X

<!-- b000528 | prose | pages [22] -->
v

<!-- b000529 | prose | pages [22] -->
ti = L

<!-- b000530 | prose | pages [22] -->
   

<!-- b000531 | prose | pages [22] -->
i=1

<!-- b000532 | prose | pages [22] -->
tj + u0ti

<!-- b000533 | prose | pages [22] -->
j̸=i

<!-- b000534 | prose | pages [22] -->
(32)

<!-- b000535 | prose | pages [22] -->
4

<!-- b000536 | prose | pages [22] -->
By adjusting the values of decision variables v and ti(I =1,2,3,4), the maximum value of L

<!-- b000537 | prose | pages [22] -->
X

<!-- b000538 | prose | pages [22] -->
−

<!-- b000539 | prose | pages [22] -->
ti

<!-- b000540 | prose | pages [22] -->
v0

<!-- b000541 | prose | pages [22] -->
i=1

<!-- b000542 | prose | pages [22] -->
is obtained, which indicates that the four-person sprint stage achieves the best effect.

<!-- b000543 | heading | pages [22] -->
Solution of the Team Time Trial Model

<!-- b000544 | prose | pages [22] -->
9.3

<!-- b000545 | prose | pages [22] -->
Using the parameters we set in the single time trial, we can solve the improvement in the team time trial according to the above strategy. The results showed that the average team speed increased by 14.43% compared to individuals during the normal advance phase and 18.52% during the sprint phase.

<!-- b000546 | heading | pages [22] -->
Model Evaluation and Further Discussion

<!-- b000547 | prose | pages [22] -->
10

<!-- b000548 | prose | pages [22] -->
10.1

<!-- b000549 | heading | pages [22] -->
Model Evaluation

<!-- b000550 | prose | pages [22] -->
10.1.1

<!-- b000551 | heading | pages [22] -->
Strengths of the Model

<!-- b000552 | prose | pages [22] -->
• The problems are divided into different modules, and the relevant knowledge of physics and biology is comprehensively used

<!-- b000553 | prose | pages [22] -->
• Starting from the basic energy supply model, our modeling is closer to reality

<!-- b000554 | prose | pages [22] -->
• A comprehensive comparison is made between different players and the model results are con- vincing

<!-- b000555 | prose | pages [22] -->
10.1.2

<!-- b000556 | heading | pages [22] -->
Weaknesses of the Model

<!-- b000557 | prose | pages [22] -->
• In the process of model building, many contents are simplified, which may make the model reflect the actual problems become inaccurate

<!-- b000558 | prose | pages [22] -->
• In the strategy selection, the analysis is not thorough, the discussion only shows that the chosen strategy is the superior strategy

<!-- b000559 | heading | pages [22] -->
Possible Improvement of the Model

<!-- b000560 | prose | pages [22] -->
10.2

<!-- b000561 | prose | pages [22] -->
There is an idea of using variational method in solving the model, but no further attempt is made due to time limitation. In fact, it is possible to use the variational method to solve the power as a function of distance, which would be very helpful for an accurate description of the problem.

<!-- b000562 | furniture | pages [23] -->
Team # 2212245

<!-- b000563 | heading | pages [23] -->
References

<!-- b000564 | furniture | pages [23] -->
Page 23 of 25

<!-- b000565 | references | pages [23] -->
[1] History of Road Cycling . [Online]. Available: https://olympics.com/en/sports/cycling-road/

<!-- b000566 | references | pages [23] -->
#discipline-history-of

<!-- b000567 | references | pages [23] -->
[2] D. Lange, “Participants in road/paved surface bicycling in the U.S. 2011-2020,” Statista,

<!-- b000568 | references | pages [23] -->
Available:

<!-- b000569 | references | pages [23] -->
Tech.

<!-- b000570 | references | pages [23] -->
Rep.,

<!-- b000571 | references | pages [23] -->
Jun.

<!-- b000572 | references | pages [23] -->
2021.

<!-- b000573 | references | pages [23] -->
[Online].

<!-- b000574 | references | pages [23] -->
road-paved-surface-bicycling-participants-us/

<!-- b000575 | references | pages [23] -->
https://www.statista.com/statistics/763746/

<!-- b000576 | references | pages [23] -->
[3] CGavin. Fuji Speedway (FSW), the cycling course of Tokyo 2020. [Online]. Available:

<!-- b000577 | references | pages [23] -->
https://720yun.com/t/267jvzwwzu3?scene_id=20194410

<!-- b000578 | references | pages [23] -->
[4] Wikipedia. Team time trail. [Online]. Available: https://en.wikipedia.org/wiki/Team_time_trial

<!-- b000579 | references | pages [23] -->
[5] [Online]. Available: https://zhuanlan.zhihu.com/p/37938089

<!-- b000580 | references | pages [23] -->
[6] Damian. Power profile in cycling. [Online]. Available:

<!-- b000581 | references | pages [23] -->
power-profile/

<!-- b000582 | references | pages [23] -->
[7] J. Fortson. Functional threshold power:

<!-- b000583 | references | pages [23] -->
https://cyklopedia.cc/cycling-tips/

<!-- b000584 | references | pages [23] -->
What ftp means to cyclists. [Online]. Available:

<!-- b000585 | references | pages [23] -->
https://www.trainerroad.com/blog/what-ftp-really-means-to-cyclists/

<!-- b000586 | references | pages [23] -->
[8] Damian. Vo2 max training, ranges, workouts. [Online]. Available:

<!-- b000587 | references | pages [23] -->
cycling-tips/vo2-max/

<!-- b000588 | references | pages [23] -->
[9] J.

<!-- b000589 | references | pages [23] -->
Fortson.

<!-- b000590 | references | pages [23] -->
How

<!-- b000591 | references | pages [23] -->
to

<!-- b000592 | references | pages [23] -->
use

<!-- b000593 | references | pages [23] -->
your

<!-- b000594 | references | pages [23] -->
strengths

<!-- b000595 | references | pages [23] -->
and

<!-- b000596 | references | pages [23] -->
weaknesses.

<!-- b000597 | references | pages [23] -->
[Online].

<!-- b000598 | references | pages [23] -->
https://cyklopedia.cc/

<!-- b000599 | references | pages [23] -->
cycling

<!-- b000600 | references | pages [23] -->
power

<!-- b000601 | references | pages [23] -->
curve

<!-- b000602 | references | pages [23] -->
to

<!-- b000603 | references | pages [23] -->
find

<!-- b000604 | references | pages [23] -->
your

<!-- b000605 | references | pages [23] -->
Available:

<!-- b000606 | references | pages [23] -->
https://www.trainerroad.com/blog/

<!-- b000607 | references | pages [23] -->
how-to-use-your-power-curve-to-find-your-strengths-and-weaknesses/

<!-- b000608 | references | pages [23] -->
[10] J. Lighthill, An informal introduction to theoretical fluid mechanics, Jan. 1986, pp. 97–121. [Online].

<!-- b000609 | references | pages [23] -->
Available: https://www.osti.gov/biblio/5126674

<!-- b000610 | references | pages [23] -->
[11] A.

<!-- b000611 | references | pages [23] -->
Denham.

<!-- b000612 | references | pages [23] -->
(2019,

<!-- b000613 | references | pages [23] -->
Jun.)

<!-- b000614 | references | pages [23] -->
Drivetrain

<!-- b000615 | references | pages [23] -->
Speed

<!-- b000616 | references | pages [23] -->
Between

<!-- b000617 | references | pages [23] -->
1X

<!-- b000618 | references | pages [23] -->
and

<!-- b000619 | references | pages [23] -->
2X?

<!-- b000620 | references | pages [23] -->
[Online].

<!-- b000621 | references | pages [23] -->
Efficiency:

<!-- b000622 | references | pages [23] -->
What’s

<!-- b000623 | references | pages [23] -->
The

<!-- b000624 | references | pages [23] -->
Difference

<!-- b000625 | references | pages [23] -->
In

<!-- b000626 | references | pages [23] -->
Available:

<!-- b000627 | references | pages [23] -->
https://www.cyclingabout.com/

<!-- b000628 | references | pages [23] -->
drivetrain-efficiency-difference-speed-between-1x-2x/#:~:text=The%201X%20drivetrain%20is%

<!-- b000629 | references | pages [23] -->
20as%20efficient%20as%2096.0%25%20and%20as%20inefficient%20as%2092.4%25.%20On%

<!-- b000630 | references | pages [23] -->
20average%20it%E2%80%99s%2095.1%25%20efficient.

<!-- b000631 | references | pages [23] -->
[12] N. R. C. U. T. R. B. C. for the National Tire Efficiency Study, Tires and passenger vehicle fuel economy:

<!-- b000632 | references | pages [23] -->
informing consumers, improving performance.

<!-- b000633 | references | pages [23] -->
Transportation Research Board, 2006, vol. 286, p. xvi.

<!-- b000634 | references | pages [23] -->
[13] G. de Groot, A. Sargeant, and J. Geysel, “Air friction and rolling resistance during cycling,”

<!-- b000635 | references | pages [23] -->
Medicine and science in sports and exercise, vol. 27, no. 7, pp. 1090–1095, Jul. 1995.

<!-- b000636 | references | pages [23] -->
[14] A. Pytel and J. Kiusalaas, Engineering Mechanics: Dynamics - SI Version.

<!-- b000637 | references | pages [23] -->
Cengage Learning, 2010,

<!-- b000638 | references | pages [23] -->
p. 654. [Online]. Available: https://books.google.co.jp/books?id=8gYKzgEACAAJ

<!-- b000639 | references | pages [23] -->
[15] Wikipedia. Drafting (aerodynamics). [Online]. Available:

<!-- b000640 | references | pages [23] -->
Drafting_(aerodynamics)

<!-- b000641 | references | pages [23] -->
https://en.wikipedia.org/wiki/

<!-- b000642 | furniture | pages [24] -->
Team # 2212245

<!-- b000643 | furniture | pages [24] -->
Page 24 of 25

<!-- b000644 | references | pages [24] -->
Rider’s Race Guidance

<!-- b000645 | references | pages [24] -->
In time trial course, athletes start separately at regular intervals and are ranked by the

<!-- b000646 | references | pages [24] -->
time they reach the finish line. The rules are simple, but achieving the desired results

<!-- b000647 | references | pages [24] -->
is difficult.It is influenced by a number of factors, including the athlete’s physical

<!-- b000648 | references | pages [24] -->
fitness, knowledge of the track, weather and strategies used in the race.This paper is

<!-- b000649 | references | pages [24] -->
prepared for you, the Directeur Sportif, to offer you guidance on helping your riders

<!-- b000650 | references | pages [24] -->
to get better results.

<!-- b000651 | references | pages [24] -->
First, get a good handle on your rider’s physical fitness.

<!-- b000652 | references | pages [24] -->
Pay attention to your rider’s daily training data, it will map their power profiles,

<!-- b000653 | references | pages [24] -->
from which you can determine whether he is a climber or a sprinter or so other. You

<!-- b000654 | references | pages [24] -->
also need to check this chart frequently to see how your athletes’ physical abilities are

<!-- b000655 | references | pages [24] -->
changing.

<!-- b000656 | references | pages [24] -->
In the power profile, the first part shows the explosive power of the rider, the riders

<!-- b000657 | references | pages [24] -->
with a higher level in this part tend to specialize in sprints. And we call those who

<!-- b000658 | references | pages [24] -->
have a great performance in the second part climber, it means they specialize in races

<!-- b000659 | references | pages [24] -->
that have multiple long climbs. Yet having a high level of the third part means the

<!-- b000660 | references | pages [24] -->
rider has great endurance,and their are excellent in long distance race.

<!-- b000661 | references | pages [24] -->
The power profile is mixed by three part, ATP-CP, Glycolysis, Aerobic, all of them

<!-- b000662 | references | pages [24] -->
form the power supply system for the rider. By analyzing the changes in the vari-

<!-- b000663 | references | pages [24] -->
ous substances in this system, we can get a detailed understanding of the physical

<!-- b000664 | references | pages [24] -->
condition of the rider, based on which we can provide you with professional advice.

<!-- b000665 | furniture | pages [25] -->
Team # 2212245

<!-- b000666 | furniture | pages [25] -->
Page 25 of 25

<!-- b000667 | references | pages [25] -->
Second, know the road conditions ahead of time.

<!-- b000668 | references | pages [25] -->
When the race starts, it is difficult for the rider to make the right decision if he

<!-- b000669 | references | pages [25] -->
has no idea what the road is going to be and what the weather will be like. The

<!-- b000670 | references | pages [25] -->
relationship between a rider’s speed, acceleration, and his power output is generally

<!-- b000671 | references | pages [25] -->
determined by the environment.

<!-- b000672 | references | pages [25] -->
Here’s what you should know about how the road and weather influence the

<!-- b000673 | references | pages [25] -->
rider’s performance:

<!-- b000674 | references | pages [25] -->
• In the uphill, riders need more power to keep the speed, and in the downhill,

<!-- b000675 | references | pages [25] -->
they need less.

<!-- b000676 | references | pages [25] -->
• As the riders go through the curve, keep in mind that never maintain excessive

<!-- b000677 | references | pages [25] -->
speed, especially when it rains.

<!-- b000678 | references | pages [25] -->
• You shall also understand that the faster you move relative to the wind, the more

<!-- b000679 | references | pages [25] -->
air resistance you will experience.

<!-- b000680 | references | pages [25] -->
Third, choose the best strategy

<!-- b000681 | references | pages [25] -->
Good strategy often leads the rider to success. Based on the results of our model,

<!-- b000682 | references | pages [25] -->
we then give our suggestions on the strategies that riders should adopt during the

<!-- b000683 | references | pages [25] -->
race.

<!-- b000684 | references | pages [25] -->
• On a road, the most important thing is to be clear about the threshold speed. But

<!-- b000685 | references | pages [25] -->
how to find it? Just speed up until the rider reach the maximum speed that just

<!-- b000686 | references | pages [25] -->
doesn’t make himself much tired and won’t cause him to fall around the corner.

<!-- b000687 | references | pages [25] -->
It’s much better than alternating acceleration process and deceleration process.

<!-- b000688 | references | pages [25] -->
• As the rider approaches the turn, evaluate the radius first to estimate speed with-

<!-- b000689 | references | pages [25] -->
out skidding. Use the brakes to slow down quickly, and the rider can have a short

<!-- b000690 | references | pages [25] -->
rest during the turn.

<!-- b000691 | references | pages [25] -->
• In the long ramp area, the basic strategy is the same as that on flat road. But

<!-- b000692 | references | pages [25] -->
notice that when the rider moves from a low resistance area to a high resistance

<!-- b000693 | references | pages [25] -->
area, for example, from a downhill zone to an uphill zone, evaluate whether the

<!-- b000694 | heading | pages [25] -->
rider can sprint through. If you’re confident about rider’s physical strength, let

<!-- b000695 | prose | pages [25] -->
the rider sprint through it, else just tell him to decelerate.

<!-- b000696 | prose | pages [25] -->
• In acceleration, the rider needs to estimate the distance to the destination and make sure he can reach it before running out of steam.

<!-- b000697 | prose | pages [25] -->
• In team time trial, it is important to rotate to take pulls. Let your riders rotate to take pulls, it will enable them to perform better than they did individually.
