# P-A-2022-2200289-b3e3573b

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
2200289

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Game Theory in Cycling

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
The rider’s strategy has a huge impact on the outcome of the race. In this article, we analyze the physiological and dynamic model of the rider’s power output, on the basis of which we obtain the optimal power output strategy over the entire course using Simulated Annealing Algorithm. We then conduct sensitivity analysis of possible inﬂuential factors. We extend our model to Team time trial.

<!-- b000011 | prose | pages [1] -->
In Model 1, we establish a model describing the rider’s power limit and physical strength based on physiology. By ﬁtting the data in the literature, we obtain the quantitative parameters of rider’s physical ability. Then a model describing the relation between power output and duration is established and utilized to give power proﬁles of three diﬀerent types of riders.

<!-- b000012 | prose | pages [1] -->
In model 2, the courses are divided into 1164 sections. We ﬁrst conduct analysis of power output, dynamic model and weather condition to quantitatively solve for energy and speed variation and time for each section of the course. We use Simulated Annealing Algorithm to optimize the power distribution over the course with the optimization objective of reducing the total race time. We then apply the model to two realistic courses and one self-designed course and give the optimal power distributions accordingly. All the results are properly explained.

<!-- b000013 | prose | pages [1] -->
In sensitivity analysis, we ﬁrst examine the inﬂuence of wind speed and wind direction on results in Model 2 by changing the two parameters in two diﬀerent types of courses. And we ﬁnd that the closer the course gets to the circle ,the less sensitive our model is to weather conditions.

<!-- b000014 | prose | pages [1] -->
When analyzing the sensitivity of the optimized results of the model to the deviations of cyclists’ power distribution, We ﬁnd that the total time is positively correlated with the variance of disturbance and is fairly sensitive to it. Then we conduct sensitivity analysis on each road section in turn to determine which road sections are the key parts and inversely solve for the possible range of expected split times at key parts.

<!-- b000015 | prose | pages [1] -->
In the Extension part, we ﬁrst study the simpliﬁed situation to consider the team as a whole. We establish a model to describe the aerodynamic drag on each rider in all permutations. We then study the complex model that applies the strategy of sacriﬁcing two wind breakers at certain point. Based on Model 2, we change the objective function and add the dropping point as a decision variable to extend our model to TTT.

<!-- b000016 | prose | pages [1] -->
Finally, we give a racing guidance for a certain course to introduce our model and demon- strate how to use it.

<!-- b000017 | keywords | pages [1] -->
Keywords: Physiology; Dynamics; Simulated Annealing Algorithm;

<!-- b000018 | furniture | pages [2] -->
Team # 2200289

<!-- b000019 | furniture | pages [2] -->
Page 1 of 24

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | heading | pages [2] -->
Introduction

<!-- b000023 | prose | pages [2] -->
3

<!-- b000024 | prose | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000025 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3

<!-- b000026 | prose | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000027 | prose | pages [2] -->
2 Assuptions and Justiﬁcations

<!-- b000028 | prose | pages [2] -->
3 The Data

<!-- b000029 | prose | pages [2] -->
4

<!-- b000030 | heading | pages [2] -->
Notations

<!-- b000031 | prose | pages [2] -->
5

<!-- b000032 | heading | pages [2] -->
Analysis and Modeling

<!-- b000033 | prose | pages [2] -->
3

<!-- b000034 | prose | pages [2] -->
4

<!-- b000035 | prose | pages [2] -->
5

<!-- b000036 | prose | pages [2] -->
5

<!-- b000037 | prose | pages [2] -->
6

<!-- b000038 | prose | pages [2] -->
Model I: Power Output and Recovery . . . . . . . . . . . . . . . . . . . . . . . 5.1 6

<!-- b000039 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 Power Curve 6

<!-- b000040 | prose | pages [2] -->
Power Proﬁles of Three Typical Riders 5.1.2

<!-- b000041 | prose | pages [2] -->
5.2 Model II: Optimal Power Distribution

<!-- b000042 | prose | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000043 | prose | pages [2] -->
8

<!-- b000044 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | prose | pages [2] -->
9

<!-- b000046 | prose | pages [2] -->
Power and Energy Analysis . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 9

<!-- b000047 | prose | pages [2] -->
Weather Condition Analysis . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 9

<!-- b000048 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 Dynamic Analysis 10

<!-- b000049 | prose | pages [2] -->
Optimization of Power Distribution 5.2.4 . . . . . . . . . . . . . . . . . . .

<!-- b000050 | prose | pages [2] -->
12

<!-- b000051 | prose | pages [2] -->
2021 Olympic Time Trial course . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 14

<!-- b000052 | prose | pages [2] -->
2021 UCI World Championship time trial course 5.4 . . . . . . . . . . . . . . . .

<!-- b000053 | prose | pages [2] -->
15

<!-- b000054 | prose | pages [2] -->
Self-Designed Course . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5

<!-- b000055 | prose | pages [2] -->
6

<!-- b000056 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000057 | prose | pages [2] -->
16

<!-- b000058 | prose | pages [2] -->
16

<!-- b000059 | prose | pages [2] -->
Weather Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 16

<!-- b000060 | prose | pages [2] -->
Deviations From Target Power Distribution 6.2

<!-- b000061 | prose | pages [2] -->
7

<!-- b000062 | heading | pages [2] -->
Extend Our Model

<!-- b000063 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000064 | prose | pages [2] -->
18

<!-- b000065 | prose | pages [2] -->
20

<!-- b000066 | prose | pages [2] -->
Simpliﬁed Situation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 20

<!-- b000067 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Complex Situation

<!-- b000068 | prose | pages [2] -->
8

<!-- b000069 | heading | pages [2] -->
Discussion

<!-- b000070 | prose | pages [2] -->
21

<!-- b000071 | prose | pages [2] -->
21

<!-- b000072 | furniture | pages [3] -->
Team # 2200289

<!-- b000073 | furniture | pages [3] -->
Page 2 of 24

<!-- b000074 | prose | pages [3] -->
8.1 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | prose | pages [3] -->
21

<!-- b000076 | prose | pages [3] -->
8.2 Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | prose | pages [3] -->
21

<!-- b000078 | prose | pages [3] -->
9 Guidance 22

<!-- b000079 | furniture | pages [4] -->
Team # 2200289

<!-- b000080 | furniture | pages [4] -->
Page 3 of 24

<!-- b000081 | prose | pages [4] -->
1

<!-- b000082 | heading | pages [4] -->
Introduction

<!-- b000083 | prose | pages [4] -->
1.1 Problem Background

<!-- b000084 | prose | pages [4] -->
Cycling is one of the most popular modern competitive sports. The three types of bicycle road races are criterium, team time trial, and individual time trial. During the cycling racesmany factors aﬀect the outcome, including ability of the player, weather conditions, the course and the strategy. Therefore, the importance of scientiﬁc strategy based on the speciﬁc player and course is more appreciable in cycling, compared with sports that mostly require high explosive power of players.

<!-- b000085 | prose | pages [4] -->
Diﬀerent types of athletes have diﬀerent physical characteristics, reﬂected in not only the capacity to generate much power, but how long the power can endure.

<!-- b000086 | prose | pages [4] -->
Athletes with high explosive power but short of endurance tend not to achieve the best and vice versa. Mathematically modeling physical changes of athletes in the movement can help coaches to develop the optimal strategy, in order to minimize the time of covering the course for a given physical ability of the player. Scientiﬁc competition strategies can not only help top athletes break records, but make sense for cycling enthusiasts to make individual plans and save energy as well.

<!-- b000087 | prose | pages [4] -->
1.2 Restatement of the Problem

<!-- b000088 | prose | pages [4] -->
Considering the background information and restricted conditions identiﬁed in the problem statement, we need to establish a model that is universal in its applicability to diﬀerent athletes and complete the following tasks using the model:

<!-- b000089 | prose | pages [4] -->
• Give the deﬁnition of the power proﬁles of two typical riders of diﬀerent gender.

<!-- b000090 | prose | pages [4] -->
• Apply your model to various time trial courses.

<!-- b000091 | prose | pages [4] -->
• Study the inﬂuence of weather conditions on the model and conduct sensitivity analysis on it.

<!-- b000092 | prose | pages [4] -->
• Study the inﬂuence of rider deviations from the strategy and conduct sensitivity analysis on it.

<!-- b000093 | prose | pages [4] -->
• Extend the model to the optimal strategy for a team time trial of six members per team.

<!-- b000094 | prose | pages [4] -->
• Design a two-page cycling guidance for a Directeur Sportif including an outline of dierctions and a summary of the model.

<!-- b000095 | prose | pages [4] -->
1.3 Our Work

<!-- b000096 | prose | pages [4] -->
The problem requires us to mathematically model the power of riders and design the optimal racing strategy with our model. Therefore, our Work includes the following:

<!-- b000097 | furniture | pages [5] -->
Team # 2200289

<!-- b000098 | furniture | pages [5] -->
Page 4 of 24

<!-- b000099 | caption | pages [5] -->
Figure 1: Structure of Our Work

<!-- b000100 | prose | pages [5] -->
2 Assuptions and Justiﬁcations

<!-- b000101 | prose | pages [5] -->
Assumptions are made as follows to simplify the problem. Each of them is properly justiﬁed.

<!-- b000102 | prose | pages [5] -->
• Assumption1: The rider’s stamina recovers all the time and the recovery rate is a constant. Justiﬁcation: Recovery rate is the measure of aerobic capacity that is related to the athlete’s recovery ability. For the same athlete, recovery rate can be regarded as constant during the whole competition.

<!-- b000103 | prose | pages [5] -->
• Assumption2: The maximum instantaneous power that the rider can output is related to the body’s remaining energy. Justiﬁcation: The human body can burst out the maximum power when energy is not consumed yet, and can not produce a lot of power when the energy is exhausted. It is reasonable to assume that the rider’s remaining energy determines the upper limit of performance.

<!-- b000104 | prose | pages [5] -->
• Assumption3: The wind direction is parallel to the direction of movement of the rider. Justiﬁcation: According to Fluid Dynamics, when air hits an obstacle at a certain speed, the airﬂow will go along its surface, going parallel with the direction of rider’s movement, not to mention that in racing courses, the slant angle is fairly small(<22 degree). Besides, accurate simulation of air stream is hard to conduct due to the complex topography and that is not the focus of our study.

<!-- b000105 | prose | pages [5] -->
• Assumption4: Every member in the team has the same physical ability. Justiﬁcation: In practice, small diﬀerences in physical ability between athletes are inevitable and it is not feasible to consider them in the mathematical model. Therefore, to simplify the problem and to facilitate modeling, we consider that each athlete in a team game has the same power proﬁle.

<!-- b000106 | furniture | pages [6] -->
Team # 2200289

<!-- b000107 | furniture | pages [6] -->
Page 5 of 24

<!-- b000108 | prose | pages [6] -->
• Assumption5: The formation change of the cycling team is done in an instant. Justiﬁcation: It only takes seconds for riders to complete the formation change, during which the energy consumption is negligible compared to that of the entire match.

<!-- b000109 | prose | pages [6] -->
• Assumption6: In the team time trial, riders maintain a constant safe distance between each other. Justiﬁcation: In order to minimize wind resistance while ensuring safety, a safe distance between riders should be maintained. Considering the techniques of professional cyclists and a very small number of severe acceleration and deceleration sections, we assume that the cyclist can maintain the distance almost all the time.

<!-- b000110 | prose | pages [6] -->
• Assumption7: The data in this research is accurate. Justiﬁcation: We assume the data we collect of cyclists is accurate so that we can base a reasonable mathematical model on it.

<!-- b000111 | prose | pages [6] -->
3 The Data

<!-- b000112 | prose | pages [6] -->
The data we collect includes the course information, performance and physical data of several groups of cycling athletes, and kinetic parameters of the rider.

<!-- b000113 | prose | pages [6] -->
We collected topographic maps of the 2021 Olympic Time Trial course and the 2021 UCI World Championship time trial course. We use Python to process the image ﬁle of the track to get the slope of the course in every section, as shown in the ﬁgure. Taking the 2021 Olympic

<!-- b000114 | caption | pages [6] -->
Figure 2: Topographic map of the 2021 Olympic Time Trial course

<!-- b000115 | prose | pages [6] -->
Time Trial course as an example, we read pixel points via python and divided the track into more than a thousand nodes so we can obtain the lateral and vertical distances of each one for further study.

<!-- b000116 | prose | pages [6] -->
4

<!-- b000117 | heading | pages [6] -->
Notations

<!-- b000118 | prose | pages [6] -->
Notations are shown in Table1.

<!-- b000119 | furniture | pages [7] -->
Team # 2200289

<!-- b000120 | furniture | pages [7] -->
Page 6 of 24

<!-- b000121 | caption | pages [7] -->
Table 1: Notations

<!-- b000122 | prose | pages [7] -->
Symbol P Pc Description Unit W Instantaneous power W Critical power of aerobic exercise w AWC J Anaerobic energy J Anaerobic Work Capacity Duration at power of P T Plim s W Power limit of the rider s−1 Coeﬃcient of w in Plim α

<!-- b000123 | prose | pages [7] -->
ρ

<!-- b000124 | prose | pages [7] -->
Seff

<!-- b000125 | prose | pages [7] -->
kg/m3 Air density

<!-- b000126 | prose | pages [7] -->
m2 Eﬀective windward area

<!-- b000127 | prose | pages [7] -->
v vw vr m/s Velocity of the rider m/s Velocity of wind m/s Relative velocity of the rider and wind Included angle between the direction of v and vw ϕ Peff rad W Eﬀetive power of driving force λ Conversion eﬃciency of the rider’s power output µ Eﬀective friction coeﬃcient µs Static friction coeﬃcient FN N Normal force between the tires and the ground Ep Ek m J Potential energy J Kinetic energy kg Total mass of the rider and bicycle θ s rad Tilt angle of the slope m The distance the rider covers from start point R The radius of curvature vsafe ftau fn

<!-- b000128 | prose | pages [7] -->
5

<!-- b000129 | heading | pages [7] -->
Analysis and Modeling

<!-- b000130 | prose | pages [7] -->
m/s Safe speed N Tangential friction N Normal friction

<!-- b000131 | heading | pages [7] -->
Model I: Power Output and Recovery

<!-- b000132 | prose | pages [7] -->
5.1

<!-- b000133 | prose | pages [7] -->
5.1.1 Power Curve

<!-- b000134 | prose | pages [7] -->
Considering the type of energy consumption, the body has two working states: aerobic exercise and anaerobic exercise. During aerobic exercise, the body expends energy from ATP produced by the aerobic system, the glycogen-lactic acid system, and the phosphorus system. Although aerobic breathing can continuously generate energy during exercise, its power is limited. When the required power exceeds the power limit of aerobic exercis, which is deﬁned as the critical power Pc, the body will expend energy from anaerobic energy sources. However, there is limit on the total amount of anaerobic energy that the body can utilize while continuously working above the critical power. The amount of energy used to measure the endurance capacity is called Anaerobic Work Capacity(AWC).

<!-- b000135 | prose | pages [7] -->
Aerobic exercise can last indeﬁnitely, as long as the power output is below the critical power.

<!-- b000136 | furniture | pages [8] -->
Team # 2200289

<!-- b000137 | furniture | pages [8] -->
Page 7 of 24

<!-- b000138 | prose | pages [8] -->
Nevertheless anaerobic exercise can endure only a limited time and then enters the recovery phase when the rider works below the critical power to regain enough anaerobic energy. Therefore, we divide a rider’s movement phase into the recovery phase(aerobic exercise) and working phase(anaerobic exercise), and conduct the following analysis on this basis.

<!-- b000139 | prose | pages [8] -->
We deﬁne P as the instantaneous power and w as the anaerobic energy. During the working phase, the variation rate of anaerobic energy dw

<!-- b000140 | prose | pages [8] -->
dt is the diﬀerence between the critical power and the instantaneous power:

<!-- b000141 | prose | pages [8] -->
dw

<!-- b000142 | prose | pages [8] -->
dt = Pc −P (1)

<!-- b000143 | prose | pages [8] -->
According to the work of Morton,R.H. and Billat,L.V.[13], during the recovery phase, this relation is still eﬀective, but the value of dw

<!-- b000144 | prose | pages [8] -->
dt is positive.

<!-- b000145 | prose | pages [8] -->
Now we try to determine a power curve that shows the rider’s ability to maintain certain level of power output continuously by giving the P-T function, where P is the given power and T is the time it can last.

<!-- b000146 | prose | pages [8] -->
Consider a process with a constant power of P. The rate of energy consumption in anaerobic respiration is the diﬀerence between instantaneous power and critical power:

<!-- b000147 | prose | pages [8] -->
w(t) = w(0) −(P −Pc)t (2)

<!-- b000148 | prose | pages [8] -->
Assume that rider can make full use of the remaining AWC, When t = T, w(T) = 0so we can obtain the equation:

<!-- b000149 | prose | pages [8] -->
P = Pc + w(0)

<!-- b000150 | prose | pages [8] -->
(3) T

<!-- b000151 | prose | pages [8] -->
When T tends to 0, P tends to inﬁnity. Under this assumption, the rider will have an inﬁnite burst of power, which is unreasonable. Therefore, we deﬁne the existence of an upper limit of power output for the rider.

<!-- b000152 | prose | pages [8] -->
Let the upper limit of instantaneous power be Plim. According to literature, the ability to do work is negatively correlated with anaerobic energy, with P decreasing as anaerobic exercise proceeds. Therefore, the coeﬃcient alpha is introduced to describe the relationship between maximum power and anaerobic energy:

<!-- b000153 | prose | pages [8] -->
Plim = αw(0) + Pc (4)

<!-- b000154 | prose | pages [8] -->
Under this assumption, Pm = αAWS + Pc is a ﬁnite value when T=0, which is in line with the actual situation.

<!-- b000155 | prose | pages [8] -->
When the rider ﬁrst enters the working phase, Plim > P, until it reaches a critical state at t = T. When t > T,Plim < P, the power cannot be maintained. Based on this analysis, we can get T, let P = Plim,t = T, w(0) = AWC:

<!-- b000156 | prose | pages [8] -->
P = α[AWC −(P −Pc)T] + Pc

<!-- b000157 | prose | pages [8] -->
solve for the relation between P and T:

<!-- b000158 | prose | pages [8] -->
(5)

<!-- b000159 | prose | pages [8] -->
P = αAWC + αPcT + Pc

<!-- b000160 | prose | pages [8] -->
(6) 1 + αT

<!-- b000161 | furniture | pages [9] -->
Team # 2200289

<!-- b000162 | furniture | pages [9] -->
Page 8 of 24

<!-- b000163 | prose | pages [9] -->
For a given rider, the power curve can be obtained by measuring the parameters AWC, α, Pc. Based on the physiological data of athletes in the paper by J. Pinot, F. Grappe (2011), the most ﬁtted results are obtained by ﬁtting the equations in the model, which are α = 0.0399s−1, Pc = 354.5W, AWC = 24010.41J. The ﬁtted curve is shown in the ﬁgure:

<!-- b000164 | caption | pages [9] -->
Figure 3: The ﬁtted power curve

<!-- b000165 | prose | pages [9] -->
The ﬁtted Power-Duration function is:

<!-- b000166 | prose | pages [9] -->
P(T) = 316.4T + 32880

<!-- b000167 | prose | pages [9] -->
(7) T + 25.02

<!-- b000168 | prose | pages [9] -->
where the unit of P is Watt and the unit of T is second.

<!-- b000169 | prose | pages [9] -->
5.1.2 Power Proﬁles of Three Typical Riders

<!-- b000170 | prose | pages [9] -->
Next, we consider the power curve of diﬀerent types of riders. According to literature data, the time trial specialists have critical power(380.2W) and AWC(26143J) that are beyond the norm, which allows the rider to have a stronger endurance and the ability to cope with a variety of complex terrain; And the sprinter’s alpha value(0.043) far exceeds the average of the cyclists, which means the Plim is fairly large and he has a surprisingly explosive power; Relatively speaking, the critical power, AWC and α of female riders are smaller than those of male riders, which are 321.3W,22189J and 0.035.The ﬁgure shows the power curves of three diﬀerent types of riders.

<!-- b000171 | furniture | pages [10] -->
Team # 2200289

<!-- b000172 | furniture | pages [10] -->
Page 9 of 24

<!-- b000173 | caption | pages [10] -->
Figure 4: Power Curves of Three Typical Riders

<!-- b000174 | prose | pages [10] -->
5.2

<!-- b000175 | heading | pages [10] -->
Model II: Optimal Power Distribution

<!-- b000176 | prose | pages [10] -->
5.2.1 Power and Energy Analysis

<!-- b000177 | prose | pages [10] -->
In the Model I, there is an upper limit to the output power during riding, represented as Plim = αw + Pc. However, in actual situation, riders can exceed the limit for better grades.

<!-- b000178 | prose | pages [10] -->
According to Physiology and requirements of the problem, exceeding the upper limit creates an additional burden on the rider, that is, the maximum power of the rider will be reduced accordingly. In order to describe the eﬀect of this excess power on the stamina of the rider, we deﬁne Wex as the work that the rider does above the power limit. The extra work done by the cyclist breaking through the limit causes a attenuation of the coeﬃcient α, which later aﬀects his anaerobic exercise ability:

<!-- b000179 | prose | pages [10] -->
α(Wex) = α(0) −0.00001αWex (8)

<!-- b000180 | prose | pages [10] -->
where the unit of Wex is J.

<!-- b000181 | prose | pages [10] -->
5.2.2 Weather Condition Analysis

<!-- b000182 | prose | pages [10] -->
The weather condition in a cycling race is wind condition, including the velocity and direciton of wind.

<!-- b000183 | prose | pages [10] -->
To simplify the calculation, we consider the wind speed and direction constant in this model.

<!-- b000184 | prose | pages [10] -->
Let the aerodynamic drag be Fair. Note that Fair does not necessarily Obstructing rider’s progress. For instance, the wind may play an accelerating role when its direction is the same as the velocity of the rider’s movement. To describe the direction of this force, we use vector analysis. Deﬁne v as the velocity of the rider and vw as the velocity of wind. According to Aerodynamics, the wind resistance can be expressed as:

<!-- b000185 | prose | pages [10] -->
F = −1

<!-- b000186 | prose | pages [10] -->
2ρ|⃗vr|2CDA ·⃗vr (9) |⃗vr|

<!-- b000187 | prose | pages [10] -->
where ρ is the air density and vr represents the relative velocity of the rider and wind. CD and

<!-- b000188 | furniture | pages [11] -->
Team # 2200289

<!-- b000189 | furniture | pages [11] -->
Page 10 of 24

<!-- b000190 | prose | pages [11] -->
A represent the coeﬃcient of drag and frontal area of the rider and bicycle. Deﬁne Seff as CDA to simplify the expression.

<!-- b000191 | prose | pages [11] -->
To quantify the vector expressions, we establish a plane right angle coordinate system, with east as the x-positive direction and north as the y-positive direction. Let the azimuth of wind speed⃗vw be ϕ and the azimuth of motion direction be γ. Then list the expressions:

<!-- b000192 | prose | pages [11] -->
 

<!-- b000193 | prose | pages [11] -->
vw = |⃗vw|(cos ϕ, sin ϕ)

<!-- b000194 | prose | pages [11] -->


<!-- b000195 | prose | pages [11] -->
v = |⃗v|(cos γ, sin γ)

<!-- b000196 | prose | pages [11] -->
 

<!-- b000197 | prose | pages [11] -->
(10)

<!-- b000198 | prose | pages [11] -->
vr =⃗v −⃗vw = (v cos γ −vw cos ϕ, v sin γ −vw sin ϕ)

<!-- b000199 | prose | pages [11] -->
The wind resistance only aﬀects the rider in the tangential direction, and the tangential force of the wind on the rider is set to Fair, then the eﬀective force of the wind on the rider is:

<!-- b000200 | prose | pages [11] -->
2ρ|⃗vr|2Seff ·⃗vr

<!-- b000201 | prose | pages [11] -->
Fair = −1

<!-- b000202 | prose | pages [11] -->
|⃗vr| ·⃗v

<!-- b000203 | prose | pages [11] -->
(11) |⃗v|

<!-- b000204 | prose | pages [11] -->
When Fair > 0, the wind exerts a drag eﬀect on the rider; when Fair < 0 the wind exerts a thrust eﬀect.

<!-- b000205 | prose | pages [11] -->
5.2.3 Dynamic Analysis

<!-- b000206 | prose | pages [11] -->
Consider the rider and bicycle as a whole. As shown in the ﬁgure, the forces on this whole are eﬀective driving force of the rider Fdrive, aerodynamic drag Fair, internal and external friction. They account for changes in kinetic and potential energy. The force analysis is displayed below. Note that in the schematic, Fdrive is a hypothetical equivalent driving force and Feff is an eﬀective frictional force.

<!-- b000207 | caption | pages [11] -->
Figure 5: Force analysis

<!-- b000208 | prose | pages [11] -->
Deﬁne eﬀective output power as Peff = λP, where λ is the coeﬃcient describing how much the power of the rider can be utilized in driving the bicycle. According to energy change constraints, we can list a equation as below:

<!-- b000209 | prose | pages [11] -->
rSeff · v −µFN · v −∆Ep

<!-- b000210 | prose | pages [11] -->
Peff −1

<!-- b000211 | prose | pages [11] -->
2ρv2

<!-- b000212 | prose | pages [11] -->
∆t −∆Ek

<!-- b000213 | prose | pages [11] -->
∆t = 0 (12)

<!-- b000214 | furniture | pages [12] -->
Team # 2200289

<!-- b000215 | furniture | pages [12] -->
Page 11 of 24

<!-- b000216 | prose | pages [12] -->
where µ is the eﬀective coeﬃcient of friction, FN represents the nromal force applied on the tire, Ep represents the potential energy and Ek represents the kinetic energy.

<!-- b000217 | prose | pages [12] -->
For a given course, the distance is divided into a large quantity of sections(in our model there are 1164 sections).

<!-- b000218 | prose | pages [12] -->
Suppose each section is a slope with the same slant angle θi, with θ > 0 for uphill and θ < 0 for downhill; meanwhile, we use equidistant segments, each with the same distance in the horizontal direction. The velocity of the ith segment is denoted as vi, and the relation can be obtained:

<!-- b000219 | prose | pages [12] -->


<!-- b000220 | prose | pages [12] -->
∆Ep

<!-- b000221 | prose | pages [12] -->


<!-- b000222 | prose | pages [12] -->
∆t = mg sin θ

<!-- b000223 | prose | pages [12] -->


<!-- b000224 | prose | pages [12] -->
∆Ek

<!-- b000225 | prose | pages [12] -->
∆t = mv ∆v

<!-- b000226 | prose | pages [12] -->
 

<!-- b000227 | prose | pages [12] -->
(13)

<!-- b000228 | prose | pages [12] -->
∆t FN = mg cos θ

<!-- b000229 | prose | pages [12] -->
where m is the total weight of the rider and bicycle and g is the gravitational acceleration.

<!-- b000230 | prose | pages [12] -->
Combine equations (12) and (13) and substitute eﬀective power, and we can obtain the equation:

<!-- b000231 | prose | pages [12] -->
−g sin θi −µg cos θi −ρv2

<!-- b000232 | prose | pages [12] -->
∆v

<!-- b000233 | prose | pages [12] -->
∆t = λPi

<!-- b000234 | prose | pages [12] -->
mvi

<!-- b000235 | prose | pages [12] -->
rSeff (14) 2m

<!-- b000236 | prose | pages [12] -->
Based on the data in the paper by JAMES C. MARTIN (2006), we set λ = 97.7%,µ = 0.0025,λ = 097.7%. Riders in diﬀerent position have diﬀerent eﬀective frontal area. For riders in a standing position(working phase), Seff = 0.304m2; For riders in a seated position(recovery phase), Seff = 0.245m2; the air density is calculated as 1.205kg/m3 at 293.15K,1 atm.

<!-- b000237 | prose | pages [12] -->
Substituting the data into equation (14), we can get a relation of v and t in the following form:

<!-- b000238 | prose | pages [12] -->
dv

<!-- b000239 | prose | pages [12] -->
dt = a

<!-- b000240 | prose | pages [12] -->
v + bv2 + c (15)

<!-- b000241 | prose | pages [12] -->
where the value of a, b, c is known. An algebraic deformation of equation (15) is done to obtain the following diﬀerential equation:

<!-- b000242 | prose | pages [12] -->
dsv = a

<!-- b000243 | prose | pages [12] -->
dv

<!-- b000244 | prose | pages [12] -->
ds

<!-- b000245 | prose | pages [12] -->
dt = dv

<!-- b000246 | prose | pages [12] -->
ds

<!-- b000247 | prose | pages [12] -->
v + bv2 + c (16)

<!-- b000248 | prose | pages [12] -->
where s refers to the distance the rider has already covered from the start point. This is a diﬀerential equation of v and s, and the boundary condition is s = Si, v = vi. By solving this diﬀerential equation, we can obtain v as a function of s, for a divided section i, the distance Si+1 of the ith node is known, and the numerical solution of vi+1 is obtained by substituting s = Si+1.

<!-- b000249 | prose | pages [12] -->
We can now solve for vi+1. And by numerical integration of the diﬀerential equation, we can get the equation:

<!-- b000250 | prose | pages [12] -->
∫ti

<!-- b000251 | prose | pages [12] -->
∫vi+1

<!-- b000252 | prose | pages [12] -->
dt = 0

<!-- b000253 | prose | pages [12] -->
vi

<!-- b000254 | prose | pages [12] -->
dv (17) v + bv2 + c a

<!-- b000255 | prose | pages [12] -->
so that we can solve for the time ti of section i. Based on this, we can obtain the total time of the race Ttotal = ∑1164

<!-- b000256 | prose | pages [12] -->
ti. 1

<!-- b000257 | prose | pages [12] -->
The above discussion is valid for any terrain in the course. For a turn in the course, the motion of the rider during the corner can be approximated as a circular motion. The frictional forces on the tires are exerted in tangential and normal directions. The tangential frictional force

<!-- b000258 | furniture | pages [13] -->
Team # 2200289

<!-- b000259 | furniture | pages [13] -->
Page 12 of 24

<!-- b000260 | prose | pages [13] -->
ftau is the drag force discussed above, while the normal frictional force fn is the centripetal force that maintains the circular motion (the normal component of the wind resistance is negligible with respect to the frictional force).

<!-- b000261 | caption | pages [13] -->
Figure 6: Analysis of sharp turns

<!-- b000262 | prose | pages [13] -->
List the kinetic equations of circular motion:

<!-- b000263 | prose | pages [13] -->
fn = mv2

<!-- b000264 | prose | pages [13] -->
(18) R

<!-- b000265 | prose | pages [13] -->
where v is the velocity of the bike and R is the radius of curvature at the curve . We have divided the course into 1164 sections. For each section with a slant angle θi and a cross-sectional radius ri, it is can be approximated as an isometric spiral. The equivalent radius of curvature of the helix is:

<!-- b000266 | prose | pages [13] -->
√

<!-- b000267 | prose | pages [13] -->
Ri = r

<!-- b000268 | prose | pages [13] -->
1 + tan2 θi (19)

<!-- b000269 | prose | pages [13] -->
There exists a maximum value of friction between the ground and the tire, i.e., the static friction µsmg, where µs is the coeﬃcient of static friction between the tire and the ground. For the sake of safety, we specify that the bicycle must not skid during cornering:

<!-- b000270 | prose | pages [13] -->
√

<!-- b000271 | prose | pages [13] -->
n + f 2

<!-- b000272 | prose | pages [13] -->
f 2

<!-- b000273 | prose | pages [13] -->
ftotal =

<!-- b000274 | prose | pages [13] -->
τ ≤µsmg (20)

<!-- b000275 | prose | pages [13] -->
Combining equation (17)(19), the upper limit vi,safe of the velocity of the i-th segment is obtained

<!-- b000276 | prose | pages [13] -->
√

<!-- b000277 | prose | pages [13] -->
(µsgRi)2 −(fi,τRi

<!-- b000278 | prose | pages [13] -->
4

<!-- b000279 | prose | pages [13] -->
vi ≤vsafe =

<!-- b000280 | prose | pages [13] -->
5.2.4 Optimization of Power Distribution

<!-- b000281 | prose | pages [13] -->
) (21) m

<!-- b000282 | prose | pages [13] -->
The optimization of strategy for the rider is essentially a process of ﬁnding the best power distribution over all sections where the total time is minimized. In order to get the global optimal solution rather than the local optimal solution, we choose the Simulated Annealing

<!-- b000283 | heading | pages [13] -->
Algorithm(SA). Combining requirements of the problem and common knowledge, in this op-

<!-- b000284 | prose | pages [13] -->
timization problem, there are kinetic, velocity, energy and power constraints. The optimization model is expressed as follows:

<!-- b000285 | furniture | pages [14] -->
Team # 2200289

<!-- b000286 | furniture | pages [14] -->
Page 13 of 24

<!-- b000287 | prose | pages [14] -->
min J = Ttotal = ∑1164

<!-- b000288 | prose | pages [14] -->
subject to, 

<!-- b000289 | prose | pages [14] -->
Mathematical model:

<!-- b000290 | prose | pages [14] -->
   

<!-- b000291 | prose | pages [14] -->
ti 1

<!-- b000292 | prose | pages [14] -->
˙s = f(s, P) 0 ≤wi ≤AWC Remaining energy limits:

<!-- b000293 | prose | pages [14] -->


<!-- b000294 | prose | pages [14] -->
Velocity limits:

<!-- b000295 | prose | pages [14] -->
  

<!-- b000296 | prose | pages [14] -->
Total energy limits:

<!-- b000297 | prose | pages [14] -->
(22)

<!-- b000298 | prose | pages [14] -->
0 ≤vi ≤vi,safe

<!-- b000299 | prose | pages [14] -->
∫Ttotal

<!-- b000300 | prose | pages [14] -->
dt ≤Elim 0

<!-- b000301 | prose | pages [14] -->
After establishing the target function and constraints, the idea of our simulated annealing algorithm is displayed as follows:

<!-- b000302 | prose | pages [14] -->
• Step0 :Set the decision variable as Pi(1 ≤i ≤1164), initial solution as Pi = Pc(1 ≤ i ≤1164), the parameter describing the progress of the algorithm is temperature K. The annealing function is Kj+1 = aKj. Determine the values of the initial temperature and the termination temperature. • Step1 : Randomly disturb 100 sections in sequence, and the disturbance ∆P satisﬁes a normal distribution with mean 0. After each disturbance, we check whether the constraint is satisﬁed: if the constraint is satisﬁed, the disturbance is retained; if the constraint is not satisﬁed, the disturbance is not retained. The diagram of each perturbation is as follows:

<!-- b000303 | caption | pages [14] -->
Figure 7: Single Disturbance

<!-- b000304 | prose | pages [14] -->
• Step2 : After 100 disturbances, the total time spent on the race in this case f1 is calculated and compared with the old solution f0: when the new solution is smaller, the new solution is chosen; when the old solution is smaller, the new solution is chosen probabilistically. The probability of choosing the new solution is:

<!-- b000305 | prose | pages [14] -->
{

<!-- b000306 | prose | pages [14] -->
1, f1 < f0

<!-- b000307 | prose | pages [14] -->
P =

<!-- b000308 | prose | pages [14] -->
(23)

<!-- b000309 | prose | pages [14] -->
e−f1−f0

<!-- b000310 | prose | pages [14] -->
, f1 > f0 T

<!-- b000311 | furniture | pages [15] -->
Team # 2200289

<!-- b000312 | furniture | pages [15] -->
Page 14 of 24

<!-- b000313 | prose | pages [15] -->
• After one iteration, the annealing function is used to simulate the decrease of the "tem- perature" of the system and to determine whether the termination temperature Kf is reached. Step3 :Repeat step1 and step2 until the "temperature" reaches the termination tempera- ture.

<!-- b000314 | caption | pages [15] -->
Figure 8: Flow Chart of SA

<!-- b000315 | prose | pages [15] -->
5.3

<!-- b000316 | heading | pages [15] -->
2021 Olympic Time Trial course

<!-- b000317 | prose | pages [15] -->
The course of the Tokyo Olympics is notable for its steep gradient, which requires riders to ﬂexibly adjust the output power to take advantage of the acceleration process of the downhill. First, we assume that a rider has an average physical ability. If he outputs a constant power of Pc, the total time he spends completing the race is 6146 s. The simulated annealing algorithm designed by this model redistributes the runner’s power over the course to eﬀectively utilize AWC, and the results are as follows.

<!-- b000318 | prose | pages [15] -->
In terms of time, the runner’s performance improved by 29%. Due to the randomness of the SA algorithm, there is some noise in the power plot line. Therefore, we smooth it as shown in

<!-- b000319 | caption | pages [15] -->
Figure 9.

<!-- b000320 | prose | pages [15] -->
The AWC distribution and velocity distribution are shown in Figure 10.

<!-- b000321 | prose | pages [15] -->
It can be seen that several more reasonable strategies are produced under the SA algorithm. One is to alternate between high and low power at smoother terrain to maintain speed while ensuring that excessive energy is not expended before going uphill; the second is to increase power on the uphill and reduce it on the downhill to recover physical energy; and the third is to sprint at full power near the end to expend the remaining physical energy.

<!-- b000322 | furniture | pages [16] -->
Team # 2200289

<!-- b000323 | furniture | pages [16] -->
Page 15 of 24

<!-- b000324 | caption | pages [16] -->
Figure 9: Smoothed Power Distribution(course1)

<!-- b000325 | prose | pages [16] -->
(a) AWC Distribution(course1) (b) Velocity Distribution(course1)

<!-- b000326 | caption | pages [16] -->
Figure 10:

<!-- b000327 | prose | pages [16] -->
The following ﬁgure shows the optimization process curve. And it is obvious that our model has a good performance in optimization.

<!-- b000328 | caption | pages [16] -->
Figure 11: Optimization process curve(course1)

<!-- b000329 | prose | pages [16] -->
5.4

<!-- b000330 | heading | pages [16] -->
2021 UCI World Championship time trial course

<!-- b000331 | prose | pages [16] -->
We will apply the same research method to the UCI course. Since UCI course is relatively ﬂatter, the requirements of power distribution is not as high as in the ﬁrst course. The strategy is basically to alternate between high and low power. And the performance improvement is not

<!-- b000332 | furniture | pages [17] -->
Team # 2200289

<!-- b000333 | furniture | pages [17] -->
Page 16 of 24

<!-- b000334 | prose | pages [17] -->
appreciable, for 9%.

<!-- b000335 | prose | pages [17] -->
The power distribution is shown in Figure 12 and optimization process curve is shown in

<!-- b000336 | caption | pages [17] -->
Figure 13.

<!-- b000337 | caption | pages [17] -->
Figure 12: Power Distribution(course2)

<!-- b000338 | prose | pages [17] -->
5.5 Self-Designed Course

<!-- b000339 | prose | pages [17] -->
In our self-designed course, we arrange four sharp turns and one steep slope, with the natural concavity of the terrain obtained by a series of normally distributed points after three spline interpolations, as is shown in Figure 13.

<!-- b000340 | caption | pages [17] -->
Figure 13: Route map of self-designed course

<!-- b000341 | prose | pages [17] -->
The eﬀect of our algorithm on this course is between the ﬁrst course and the second, with an improvement of 18%, compared to constant power driving. The power distribution is shown in Figure 14.

<!-- b000342 | prose | pages [17] -->
It can be seen from the three courses that our mathematical model and the optimization process have a high superiority when the slope is large and the terrain is not ﬂat.

<!-- b000343 | prose | pages [17] -->
6

<!-- b000344 | heading | pages [17] -->
Sensitivity Analysis

<!-- b000345 | prose | pages [17] -->
6.1 Weather Conditions

<!-- b000346 | prose | pages [17] -->
We ﬁrst conduct sensitivity analysis on the weather condition. In model II, We analyze the kinetic mechanism of the aerodynamic drag on the rider and give the eﬀective force⃗Fair as a

<!-- b000347 | furniture | pages [18] -->
Team # 2200289

<!-- b000348 | furniture | pages [18] -->
Page 17 of 24

<!-- b000349 | caption | pages [18] -->
Figure 14: Power Distribution(course3)

<!-- b000350 | prose | pages [18] -->
function of⃗vr and⃗v.

<!-- b000351 | prose | pages [18] -->
To facilitate the modeling, we set the wind speed and wind direction to satisfy the normal distribution with given mathematical expectations. Next, we take the 2021 Olympic Time Trial course (course1) and 2021 UCI World Championship time trial course (course2) as examples to illustrate the eﬀect of diﬀerent wind directions and magnitudes on the results.

<!-- b000352 | prose | pages [18] -->
We continue to use the plane coordinate system in Model 2. The azimuth of the wind We ﬁrst study the situation of ﬁxed wind direction, where ϕ ∼ direction is noted as ϕ. N(π, 0.15). The wind speed expectation Evw is varied from small to large, and the optimization results at this wind speed are examined as follows(Figure 15).

<!-- b000353 | prose | pages [18] -->
(a) Analysis on vw(course1) (b) Analysis on vw(course2)

<!-- b000354 | caption | pages [18] -->
Figure 15:

<!-- b000355 | prose | pages [18] -->
As can be seen from the ﬁgure, for course1, with the increase of wind speed expectation, the optimization result of the race performance ﬂuctuates up and down in a small range and does not show a signiﬁcant correlation with the wind speed. This indicates that when our model is applied to circular courses like course1, its sensitivity to the wind speed is rather weak. For course2, with the increase of wind speed expectation, the optimization result of the race performance has a signiﬁcant improvement, which is because course2 is generally winding from north to south. Therefore, courses like course2 tend to have a strong sensitivity to wind speed.

<!-- b000356 | prose | pages [18] -->
Then we ﬁx the expectation of wind velocity Evw, increasing the expectation of wind direction Eϕ ∈(0, 2π). As can be seen from Figure 16, the optimization results of course 1 have small random ﬂuctuations, which shows that in circular courses like course1 , our model

<!-- b000357 | furniture | pages [19] -->
Team # 2200289

<!-- b000358 | furniture | pages [19] -->
Page 18 of 24

<!-- b000359 | prose | pages [19] -->
is less sensitive to wind direction compared with other types of courses. For course2, there is a signiﬁcant correlation between the ﬂuctuation of its optimization results and the overall direction of the course (it takes less time downwind, and more time upwind), and the ﬂuctuation is larger, showing that course2 has a strong sensitivity to wind direction.

<!-- b000360 | prose | pages [19] -->
(a) Analysis on ϕ(course1) (b) Analysis on ϕ(course2)

<!-- b000361 | caption | pages [19] -->
Figure 16:

<!-- b000362 | prose | pages [19] -->
Deviations From Target Power Distribution 6.2

<!-- b000363 | prose | pages [19] -->
Taking track 3 as the object, this part will do sensitivity analysis on the deviation degree between the actual power distribution of the rider and the target power distribution. We perform the following operations on the target power distribution of the rider:

<!-- b000364 | prose | pages [19] -->
{

<!-- b000365 | prose | pages [19] -->
P ′

<!-- b000366 | prose | pages [19] -->
i = Ptarget,i + ϵi (24) ϵi ∼N(0, ϵ)

<!-- b000367 | prose | pages [19] -->
Where ϵ is the indicator to quantify the actual deviation degree. However, it should be noted that the power distribution P ′

<!-- b000368 | prose | pages [19] -->
i after the above operation may not meet the constraints we mentioned above. Therefore, the following operations need to be performed:

<!-- b000369 | prose | pages [19] -->
(1) When i=1 , Ω1, namely the range of values of P1 ,is obtained from the initial conditions and constraints

<!-- b000370 | prose | pages [19] -->


<!-- b000371 | prose | pages [19] -->
P ′

<!-- b000372 | prose | pages [19] -->
1, P ′

<!-- b000373 | prose | pages [19] -->


<!-- b000374 | prose | pages [19] -->
1 ∈Ω1

<!-- b000375 | prose | pages [19] -->


<!-- b000376 | prose | pages [19] -->
max{Ω1}, P ′

<!-- b000377 | prose | pages [19] -->
Preal,1 =

<!-- b000378 | prose | pages [19] -->
 

<!-- b000379 | prose | pages [19] -->
1 > max{Ω1}

<!-- b000380 | prose | pages [19] -->
(25)

<!-- b000381 | prose | pages [19] -->
min{Ω1}, P ′

<!-- b000382 | prose | pages [19] -->
then obtain treal,1 and wreal,1.

<!-- b000383 | prose | pages [19] -->
1 < min{Ω1}

<!-- b000384 | prose | pages [19] -->
(2) When i = k(2 ≤k ≤1000), according to wreal,k−1 and constraints, we get Ωk.

<!-- b000385 | prose | pages [19] -->


<!-- b000386 | prose | pages [19] -->
P ′

<!-- b000387 | prose | pages [19] -->
k, P ′

<!-- b000388 | prose | pages [19] -->


<!-- b000389 | prose | pages [19] -->
k ∈Ωk

<!-- b000390 | prose | pages [19] -->


<!-- b000391 | prose | pages [19] -->
max{Ωk}, P ′

<!-- b000392 | prose | pages [19] -->
Preal,k =

<!-- b000393 | prose | pages [19] -->
 

<!-- b000394 | prose | pages [19] -->
k > max{Ωk}

<!-- b000395 | prose | pages [19] -->
(26)

<!-- b000396 | prose | pages [19] -->
min{Ωk}, P ′

<!-- b000397 | prose | pages [19] -->
Then we get treal,k and wreal,k

<!-- b000398 | prose | pages [19] -->
k < min{Ωk}

<!-- b000399 | prose | pages [19] -->
Sequentially adjust every section to ensure that the power distribution satisﬁes the con- straints. Then calculate Treal = ∑1000

<!-- b000400 | prose | pages [19] -->
treal,i. Gradually increase the value of ϵ and compute 1 Treal Ttarget, respectively(see Figure 17). the corresponding

<!-- b000401 | furniture | pages [20] -->
Team # 2200289

<!-- b000402 | furniture | pages [20] -->
Page 19 of 24

<!-- b000403 | caption | pages [20] -->
Figure 17: Sensitivity of the whole model

<!-- b000404 | prose | pages [20] -->
As can be seen from the graph, the model is sensitive to the deviation of the rider’s power distribution, and as the deviation becomes larger, the overall time spent in the race tends to increase.

<!-- b000405 | prose | pages [20] -->
This section will ﬁrst analyze the critical sections. The sensitivity of each individual road section will be analyzed in which we will set a 10% disturbance to the power on it , and the road section with a large sensitivity is understood as the critical road section. The analysis steps for the ith road section are as follows.

<!-- b000406 | prose | pages [20] -->
(1) determine Ωi, namely the range of Pi

<!-- b000407 | prose | pages [20] -->
(2) Pi(1) = 1.1 · Ptarget,iăPreal,i(1) = max{Pi(i), max{Ωi}}

<!-- b000408 | prose | pages [20] -->
(3) sequentially adjust Preal,i+1(1),...,and we get Treal(1)

<!-- b000409 | prose | pages [20] -->
(4) Pi(2) = 0.9 · Ptarget,i,Preal,i(2) = min{Pi(i), min{Ωi}}

<!-- b000410 | prose | pages [20] -->
(5) sequentially adjust Preal,i+1(2),...,and we getTreal(2)

<!-- b000411 | prose | pages [20] -->
(6) then we getBiai = (Treal(1) + Treal(2))/Ttarget

<!-- b000412 | prose | pages [20] -->
Get the diagram and compare it with the topographic map of the track.

<!-- b000413 | prose | pages [20] -->
(a) Sensitivity of each sections (b) Elevation distribution

<!-- b000414 | caption | pages [20] -->
Figure 18:

<!-- b000415 | furniture | pages [21] -->
Team # 2200289

<!-- b000416 | furniture | pages [21] -->
Page 20 of 24

<!-- b000417 | prose | pages [21] -->
It is easy to analyze: the uphill section (especially the steep slope) is very sensitive to the degree of deviation; the sensitivity of the sharp turn is in the second place. Accordingly, we can consider the steep slope at 11 13km as the key section, and the 100m before and after the three sharp turns as the second key section.

<!-- b000418 | prose | pages [21] -->
We specify that the deviation in performance caused by the power deviation in the key sections cannot exceed 0.3%, thus inverse solving for the possible range of expected split times at key parts respectively.

<!-- b000419 | prose | pages [21] -->
• 11 ∼13km road section passing time range is (337 ∼401)s

<!-- b000420 | prose | pages [21] -->
• 9.9 ∼10.1km road section passing time range is (36.2 ∼45.1)s

<!-- b000421 | prose | pages [21] -->
• 19.9 ∼20.1km road section passing time range is (37.4 ∼43.2)s

<!-- b000422 | prose | pages [21] -->
• 29.9 ∼30.1km raod section passing time range is (35.1 ∼41.6)s

<!-- b000423 | prose | pages [21] -->
7

<!-- b000424 | heading | pages [21] -->
Extend Our Model

<!-- b000425 | prose | pages [21] -->
The dynamics model of Team Time Trial is as follows: a group of cyclists are arranged in a straight line during the running, and the air resistance coeﬃcient of the rear riders is eﬀectively reduced compared with that of the solo riders due to the wind breaking eﬀect of the front riders. Therefore, compared with Individual Team Trial, in Team Time Trial, the Team should choose appropriate strategies to break the wind in turn, which will be the key to improve Team performance.

<!-- b000426 | prose | pages [21] -->
7.1 Simpliﬁed Situation

<!-- b000427 | prose | pages [21] -->
For the sake of simplicity, let’s start with a model that doesn’t take into account diﬀerent responsibilities between players.

<!-- b000428 | prose | pages [21] -->
According to the literature, in the process of match, the smaller the distance between two bicycles is, the more obvious the eﬀect of wind resistance reduction in the rear row is. However, in order to ensure the safety of riders, a safe distance dsafe should be set between two riders. If the distance is smaller than dsafe, there will be a risk of rear-end collision. Ideally, The cyclist can always keep the distance between the two just within a safe distance to make the average wind resistance will be minimal. From this we can assume that the speed and acceleration of cyclists are always the same.The following discussion is based on this.

<!-- b000429 | prose | pages [21] -->
In a team of six, it’s easy to know that there are 6! = 720 permutationsLet the permutations be Ak(1 ≤k ≤720).

<!-- b000430 | prose | pages [21] -->
{

<!-- b000431 | prose | pages [21] -->
1, if Ak is Chosen

<!-- b000432 | prose | pages [21] -->
Ak =

<!-- b000433 | prose | pages [21] -->
(27) 0, if Ak is not Chosen

<!-- b000434 | prose | pages [21] -->
In our modelthe course is divided into 1000 sections. In each section, the permutation remains unchanged.

<!-- b000435 | prose | pages [21] -->
We used the same dynamic model as Individual Time Trial. But in Team Time Trial, the aerodynamic drag Fair diﬀers between riders in diﬀerent position of the team, since Fairis a linear function of v2

<!-- b000436 | prose | pages [21] -->
r. Let it be Fair = Cv2

<!-- b000437 | prose | pages [21] -->
r. Let Akibe the permutation k in section i, and the coeﬃcient of the jth rider in kth permutationis cjk, the coeﬃcient of the jth rider is:

<!-- b000438 | prose | pages [21] -->
Cj,i = [A1i, · · · , A720i][cj,1, · · · , cj720]T (28)

<!-- b000439 | furniture | pages [22] -->
Team # 2200289

<!-- b000440 | furniture | pages [22] -->
Page 21 of 24

<!-- b000441 | prose | pages [22] -->
Using the method in Model II,we can get the time ti for section i.

<!-- b000442 | prose | pages [22] -->
7.2 Complex Situation

<!-- b000443 | prose | pages [22] -->
Considering the teams grade is determined by the grade of the fourth rider to cross the line, the coach needs to arrange diﬀerent duties for riders. The two wind breakers need to do more of the wind breaking in the early part of the race so that the other four can save energy for the sprint in the ﬁnal sections. Therefore, when to drop the two riders oﬀthe team becomes a critical choice.

<!-- b000444 | prose | pages [22] -->
Let idbe the section where the team drop the wind-breakers. After section id, we only need to consider a team of four members, which means there are 4! = 24 permutations. In this situation, the coeﬃcient of the jth rider can be represented as:

<!-- b000445 | prose | pages [22] -->
Cj,i = [A1i, · · · , A24i][cj,1, · · · , cj24]T (29)

<!-- b000446 | prose | pages [22] -->
As with Model II, we still treat it as an optimization problem and use the Simulated Annealing Algorithm. The decision variables are id, distribution of Pi and Ai. And the target function is:

<!-- b000447 | prose | pages [22] -->
min J=∑id

<!-- b000448 | prose | pages [22] -->
1 ti + ∑1000 id+1 ti

<!-- b000449 | prose | pages [22] -->
Due to the large number of decision variables, we adopted the following method based on the simulated annealing algorithm:

<!-- b000450 | prose | pages [22] -->
• Step1 : id Evenly takes 10 discrete values. For each id, determine the initial solution, cooling function, initial temperature and termination temperature. • Step2 : For the 10 discrete values in Step1, we compare the corresponding optimal function value, namely the total time. According to the results, the interval between the sub-peaks is taken and the id is constrained within this range. If the number of contained points is still too much, repeat Step1 within this interval. Step1. • Step3 : Add id to the decision variable, and use the SA Algorithm to get the optimal scheme

<!-- b000451 | prose | pages [22] -->
8

<!-- b000452 | heading | pages [22] -->
Discussion

<!-- b000453 | prose | pages [22] -->
8.1

<!-- b000454 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b000455 | prose | pages [22] -->
• Our dynamic model closely accords with the actual situation

<!-- b000456 | prose | pages [22] -->
• Simulated annealing algorithm cannot guarantee the global optimal solution.

<!-- b000457 | prose | pages [22] -->
• The parameters of the simulated annealing algorithm need to be adjusted every time diﬀerent track is optimized.

<!-- b000458 | prose | pages [22] -->
• The model is highly sensitive to the accuracy of quoted data.

<!-- b000459 | prose | pages [22] -->
8.2

<!-- b000460 | heading | pages [22] -->
Future Work

<!-- b000461 | prose | pages [22] -->
• Collect more data to enhance the accuracy and robustness of the model

<!-- b000462 | prose | pages [22] -->
• Apply the model to other tracks to test the validity of the model

<!-- b000463 | furniture | pages [23] -->
Team # 2200289

<!-- b000464 | furniture | pages [23] -->
Page 22 of 24

<!-- b000465 | prose | pages [23] -->
9 Guidance

<!-- b000466 | prose | pages [23] -->
Dear Directeur Sportif:

<!-- b000467 | prose | pages [23] -->
This guidance will focus on the result of a sprinter who takes part in 2021 Olympic Time Trial course in Tokyo, Japan.

<!-- b000468 | prose | pages [23] -->
As you know, the cyclist you’re in charge of is a typical Sprinter. He has extraordinary short time explosive power, can stand out in short distance sprint competition and easily win.His physical characteristics can be well reﬂected in the Power Curve compared with the time trial specialist(see Figure 19).

<!-- b000469 | caption | pages [23] -->
Figure 19: Power Proﬁles of Two Cyclists

<!-- b000470 | prose | pages [23] -->
However, in the upcoming Olympic Time Trial Course, the complex and rugged terrain and a large number of curves pose a more severe challenge to the reasonable allocation and eﬀective utilization of athletes’ physical strength in the long distance riding.

<!-- b000471 | prose | pages [23] -->
The Tokyo Olympic course features signiﬁcant slopes, which requires athletes to ﬂexibly adjust the power output and take advantage of the downhill acceleration process. If the rider does not plan his power output properly and distributes energy in a haphazard way, the race result will be disappointing for you and your team.

<!-- b000472 | prose | pages [23] -->
Fortunately, our model solves this problem well for you.

<!-- b000473 | prose | pages [23] -->
Our model divides the track into 1,164 equidistant sections. As shown in Figure 20, we have provided you and your rider with a reliable recommended power output for each section. In general, our model recommends that your racer increase power output for speed on the uphill, reduce power for recovery on the downhill, and alternate high and low power on ﬂat surfaces. If followed rigorously as recommended by our model, your runner’s performance can improve by as much as 29%, an eﬀect that is staggering.

<!-- b000474 | prose | pages [23] -->
However, athletes’ perceptual judgment of their own power output during riding is often in- accurate, which makes it diﬃcult for them to strictly implement our recommended scheme. Therefore, it is necessary to install a sensor system on the bike that can monitor the power output of the rider remotely. You and your team can tell your player,in real time, whether he

<!-- b000475 | furniture | pages [24] -->
Team # 2200289

<!-- b000476 | furniture | pages [24] -->
Page 23 of 24

<!-- b000477 | caption | pages [24] -->
Figure 20: Power Distribution

<!-- b000478 | prose | pages [24] -->
should increase or decrease his power, using tools such as headphones.

<!-- b000479 | prose | pages [24] -->
Of course, despite the help of sensors, a cyclist who is going through intense anaerobic exercise on a long, long bike ride may still have trouble controlling his power accurately. In the event of inevitable deviations, our model identiﬁes key sections of the track for the Tokyo Olympics. On these critical sections, your rider needs to be extremely strict in implementing our recommended power output, otherwise it may have a signiﬁcant impact on his race performance. These key sections include: all steep climbs and sharp turns. Your riders should take extra care when driving through these sections.

<!-- b000480 | prose | pages [24] -->
It is worth mentioning that you and your racer should not worry too much about the wind speed and direction of the day. Our aerodynamics model already takes the wind speed and direction into account, and your racer should simply follow our recommendations as strictly as possible.

<!-- b000481 | furniture | pages [25] -->
Team # 2200289

<!-- b000482 | furniture | pages [25] -->
Page 24 of 24

<!-- b000483 | heading | pages [25] -->
References

<!-- b000484 | references | pages [25] -->
[1] https://olympics.com/olympic-games/tokyo-2020&TopographicMap

<!-- b000485 | references | pages [25] -->
[2] https://www.flanders2021.com&TopographicMap

<!-- b000486 | references | pages [25] -->
[3] Vandewalle, H., 2018. Modelling of Running Performances: Comparisons of Power-Law,

<!-- b000487 | references | pages [25] -->
Hyperbolic, Logarithmic, and Exponential Models in Elite Endurance Runners. BioMed

<!-- b000488 | references | pages [25] -->
Research International, 2018, pp.1-23

<!-- b000489 | references | pages [25] -->
[4] Debraux, P., Grappe, F., Manolova, A.V. and Bertucci, W. (2011). Aerodynamic drag in

<!-- b000490 | references | pages [25] -->
cycling: methods of assessment. Sports Biomechanics, 10(3), pp.197218.

<!-- b000491 | references | pages [25] -->
[5] M ARTIN, J.C., GARDNER, A.S., BARRAS, M. and MARTIN, D.T. (2006). Modeling

<!-- b000492 | references | pages [25] -->
Sprint Cycling Using Field-Derived Parameters and Forward Integration. Medicine &

<!-- b000493 | references | pages [25] -->
Science in Sports & Exercise, 38(3), pp.592597.

<!-- b000494 | references | pages [25] -->
[6] Blocken, B., van Druenen, T., Toparlar, Y., Malizia, F., Mannion, P., Andrianne, T.,

<!-- b000495 | references | pages [25] -->
Marchal, T., Maas, G.-J. and Diepens, J. (2018). Aerodynamic drag in cycling pelotons:

<!-- b000496 | references | pages [25] -->
New insights by CFD simulation and wind tunnel testing. Journal of Wind Engineering

<!-- b000497 | references | pages [25] -->
and Industrial Aerodynamics, [online] 179, pp.319337.

<!-- b000498 | references | pages [25] -->
[7] Pinot, J. and Grappe, F. (2011). The Record Power Proﬁle to Assess Performance in Elite

<!-- b000499 | references | pages [25] -->
Cyclists. International Journal of Sports Medicine, 32(11), pp.839844.

<!-- b000500 | references | pages [25] -->
[8] Peronnet, F. and Thibault, G. (1989). Mathematical analysis of running performance and

<!-- b000501 | references | pages [25] -->
world running records. Journal of Applied Physiology, 67(1), pp.453465.

<!-- b000502 | references | pages [25] -->
[9] Pinot, J. and Grappe, F. (2011a). The PeronnetThibault mathematical model applied to

<!-- b000503 | references | pages [25] -->
the record power proﬁle in cycling. Computer Methods in Biomechanics and Biomedical

<!-- b000504 | references | pages [25] -->
Engineering, 14(sup1), pp.219220.

<!-- b000505 | references | pages [25] -->
[10] Vanhatalo, A., Jones, A.M. and Burnley, M. (2011). Application of Critical Power in

<!-- b000506 | references | pages [25] -->
Sport. International Journal of Sports Physiology and Performance, 6(1), pp.128136.

<!-- b000507 | references | pages [25] -->
[11] Pinot, J. and Grappe, F. (2010). The Power Proﬁle for determining the physical capacities

<!-- b000508 | references | pages [25] -->
of a cyclist. Computer Methods in Biomechanics and Biomedical Engineering, 13(sup1),

<!-- b000509 | references | pages [25] -->
pp.103104.

<!-- b000510 | references | pages [25] -->
[12] Millet, G.P., Tronche, C. and Grappe, F. (2014). Accuracy of Indirect Estimation of Power

<!-- b000511 | references | pages [25] -->
Output From Uphill Performance in Cycling. International Journal of Sports Physiology

<!-- b000512 | references | pages [25] -->
and Performance, 9(5), pp.777782.

<!-- b000513 | references | pages [25] -->
[13] Morton, R.H. and Billat, L.V. (2004). The critical power model for intermittent exercise.

<!-- b000514 | references | pages [25] -->
European Journal of Applied Physiology, 91(2-3), pp.303307.

<!-- b000515 | references | pages [25] -->
[14] Blocken, B., Toparlar, Y., van Druenen, T. and Andrianne, T. (2018a). Aerodynamic drag

<!-- b000516 | references | pages [25] -->
in cycling team time trials. Journal of Wind Engineering and Industrial Aerodynamics,

<!-- b000517 | references | pages [25] -->
[online] 182, pp.128145.
