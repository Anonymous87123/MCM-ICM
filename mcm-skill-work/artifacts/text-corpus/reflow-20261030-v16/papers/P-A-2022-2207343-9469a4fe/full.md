# P-A-2022-2207343-9469a4fe

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
2207343

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Optimal Power Allocation −Ride to The Future

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Who would have thought that the champion of the Tokyo Olympics cycling time trial was a mathematician? Believe it or not, math does it. In this paper, we will build a mathematical model of the power curve to help riders win races.

<!-- b000010 | prose | pages [1] -->
In Task 1, we build a power-duration model based on biological principles. This model has three stages: Extreme, Severe, Heavy. After substituting the searched rider data into the model, we plot the power curves of the sprinter and time trial specialist of diﬀerent genders.

<!-- b000011 | prose | pages [1] -->
In Task 2, we ﬁrst use the power curve in Task 1 to build the Human Energy Expenditure Model, which describes the rider’s constraints on energy limits. We analyzed the dynamic bicycle model to determine the Pout −v relationship during cycling. By analyzing the characteristics of the track, we establish a piecewise nonlinear programming model with a wide range of applications for straights, curves, and slopes. For large slope segments or sharp bends, we made detailed calculations individually. Finally, the optimal output power curves of the riders when riding on the three courses in Task 1 are solved by Mathematica. The completion times are shown in the table below. Compared with the champion, our model lags within 6%, reﬂecting the model’s accuracy.

<!-- b000012 | prose | pages [1] -->
Male time Female time Course Male sprinter Female sprinter trial specialist trial specialist Self-designed 47.53min 48.58min 46.48min 48.20min In Japan 62.68min 40.97min 56.03min 33.63min In Belgium 58.15min 59.62min 53.03min 54.05min After the model is solved, we perform sensitivity analysis in Task 3 and Task 4. For weather factors, we focus on the eﬀects of wind speed and direction. When the wind speed changes within ±2m/s and the direction changes within ±180◦, we get the change graph of the output power with Python. We conclude that the model is robust as its sensitivity to crosswinds is within 1%. And it has a 10% impact on headwinds, which provides us with ideas for team competition strategies.

<!-- b000013 | prose | pages [1] -->
We also tested the model’s sensitivity to rider deviations. Taking the Belgian track as an example, we establish the riders’ actual output power function Pout and add a random disturbance term g Pout to simulate the randomness of the rider. After calculation, the riders can ﬁnish the race before they run out of energy. The time lag is within 2%.

<!-- b000014 | prose | pages [1] -->
Inspired by the model’s high sensitivity to headwind, we develop a team time trial strategy in Task 5. The results are shown in the table below.

<!-- b000015 | prose | pages [1] -->
Stage Balance(48%) Storage(27%) Sprint(25%) Formation Pyramid formation Linear array Shield formation

<!-- b000016 | prose | pages [1] -->
Finally, we write to Directeur Sportif with a race guidance for time trial specialists and sprinters.

<!-- b000017 | keywords | pages [1] -->
Keywords: power curve, nonlinear programming, dynamics model, formation planning

<!-- b000018 | furniture | pages [2] -->
Team # 2207343

<!-- b000019 | furniture | pages [2] -->
Page 1 of 22

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1 Introduction

<!-- b000022 | contents | pages [2] -->
2

<!-- b000023 | contents | pages [2] -->
1.1

<!-- b000024 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
1.2

<!-- b000027 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
1.3

<!-- b000030 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
3

<!-- b000032 | contents | pages [2] -->
2 Assumptions and Justiﬁcations

<!-- b000033 | contents | pages [2] -->
4

<!-- b000034 | contents | pages [2] -->
3 Notations

<!-- b000035 | contents | pages [2] -->
4

<!-- b000036 | contents | pages [2] -->
4 Three stage power-duration models

<!-- b000037 | contents | pages [2] -->
4

<!-- b000038 | contents | pages [2] -->
4.1

<!-- b000039 | contents | pages [2] -->
The Establishment of power-duration model . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
5

<!-- b000041 | contents | pages [2] -->
4.2

<!-- b000042 | contents | pages [2] -->
The Solution of Power-Duration Model . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
6

<!-- b000044 | contents | pages [2] -->
5 Piecewise Nonlinear Programming for Time Trial

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
5.1

<!-- b000047 | contents | pages [2] -->
The Establishment of Human Energy Expenditure Model . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
6

<!-- b000049 | contents | pages [2] -->
5.2

<!-- b000050 | contents | pages [2] -->
The Mathematical Relationship Between Power Output And Speed . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
7

<!-- b000052 | contents | pages [2] -->
5.3

<!-- b000053 | contents | pages [2] -->
The Racing Strategy of Self-designed course . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
8

<!-- b000055 | contents | pages [2] -->
5.3.1

<!-- b000056 | contents | pages [2] -->
Analysis of Riding Strategies on Curved Roads . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
9

<!-- b000058 | contents | pages [2] -->
5.3.2

<!-- b000059 | contents | pages [2] -->
Analysis of Straight Riding Strategy . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
9

<!-- b000061 | contents | pages [2] -->
5.4

<!-- b000062 | contents | pages [2] -->
The Strategy of 2021 UCI World Championship time trial course . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
11

<!-- b000064 | contents | pages [2] -->
5.4.1

<!-- b000065 | contents | pages [2] -->
The Strategy of Straight and Ramp Riding in Belgium course . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
12

<!-- b000067 | contents | pages [2] -->
5.4.2

<!-- b000068 | contents | pages [2] -->
The Strategy of Turning in Belgium course

<!-- b000069 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
13

<!-- b000071 | contents | pages [2] -->
5.5

<!-- b000072 | contents | pages [2] -->
The Strategy of 2021 Olympic Time Trial course

<!-- b000073 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
13

<!-- b000075 | contents | pages [2] -->
5.5.1

<!-- b000076 | contents | pages [2] -->
The Strategy for Regular Road Sections in Japan

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
14

<!-- b000079 | contents | pages [2] -->
5.5.2

<!-- b000080 | contents | pages [2] -->
The Strategy for Special Road Sections in Japan . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
15

<!-- b000082 | contents | pages [2] -->
6 Sensitivity Analysis

<!-- b000083 | contents | pages [2] -->
16

<!-- b000084 | contents | pages [2] -->
6.1

<!-- b000085 | contents | pages [2] -->
Sensitive Analysis of Weather

<!-- b000086 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
16

<!-- b000088 | contents | pages [2] -->
6.2

<!-- b000089 | contents | pages [2] -->
Sensitive Analysis of Rider Deviations . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
18

<!-- b000091 | contents | pages [2] -->
7 Further Discussion of The Team Time Trial

<!-- b000092 | contents | pages [2] -->
19

<!-- b000093 | contents | pages [2] -->
8 Model Evaluation and Further Discussion

<!-- b000094 | contents | pages [2] -->
21

<!-- b000095 | contents | pages [2] -->
8.1

<!-- b000096 | contents | pages [2] -->
Strengths

<!-- b000097 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000098 | contents | pages [2] -->
8.2

<!-- b000099 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000100 | contents | pages [2] -->
8.3

<!-- b000101 | contents | pages [2] -->
Conclusion

<!-- b000102 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000103 | furniture | pages [3] -->
Team # 2207343

<!-- b000104 | furniture | pages [3] -->
Page 2 of 22

<!-- b000105 | heading | pages [3] -->
1 Introduction

<!-- b000106 | heading | pages [3] -->
1.1 Restatement of the Problem

<!-- b000107 | prose | pages [3] -->
Cycling is characterized by high power output over a period. This capability can be summarized by a power curve representing the maximum power a cyclist has generated over time. Due to the limited endurance of humans, the power curve generally slopes downward to the right, as shown in ﬁg. 1.

<!-- b000108 | prose | pages [3] -->
The power curve is used to specify pacing strategies for diﬀerent courses. And it can prevent the rider from incurring signiﬁcant energy losses on impulse. This can be useful in any cycling race requiring pacing, such as a time trial, Strava segment, or mid-race climb. Using diﬀerent riding powers on diﬀerent road conditions can help riders store energy for sprints and win races.

<!-- b000109 | caption | pages [3] -->
Figure 1: Power curve

<!-- b000110 | prose | pages [3] -->
We are developing a mathematical model for diﬀerent types of cyclists. This model is limited by the total energy a cyclist can expend, focusing on several characteristics of the cyclist, such as the riding capacity, the position of the rider, and the output power of the rider. Based on the above understanding, we need to solve the following problems:

<!-- b000111 | prose | pages [3] -->
• Deﬁne the power curve of a time trial specialist and a sprinter, and consider the genders.

<!-- b000112 | prose | pages [3] -->
• Use each power proﬁle deﬁned in Task 1 to apply the model to the following time trial.

<!-- b000113 | prose | pages [3] -->
◦2021 Olympic Time Trial course in Tokyo, Japan, ◦2021 UCI World Championship time trial course in Flanders, Belgium, ◦At a minimum, a self-designed track that includes at least four sharp turns and a nontrivial road grade. The end of the course should be near its start point.

<!-- b000114 | prose | pages [3] -->
• Determine the model’s sensitivity to weather factors, including wind speed and direction.

<!-- b000115 | prose | pages [3] -->
• Analyze how sensitive the results are to rider deviations from the target power distribution.

<!-- b000116 | prose | pages [3] -->
• Further, discuss extending the model to a six-player team time trial and get the best results.

<!-- b000117 | prose | pages [3] -->
Team time is determined by when the fourth rider crosses the ﬁnish line.

<!-- b000118 | prose | pages [3, 4] -->
• Write a two-page rider’s race guidance for a Directeur Sportif of a team, which should focus on the result of a time trial course and a rider. It needs to include a model summary and an overview of directions. Readers are people with no mathematical background.

<!-- b000119 | furniture | pages [4] -->
Team # 2207343

<!-- b000120 | furniture | pages [4] -->
Page 3 of 22

<!-- b000122 | heading | pages [4] -->
1.2 Literature Review

<!-- b000123 | prose | pages [4] -->
Power proﬁling has always been a scorching area of cycling research. Since the invention of the power meter in the late 1980s, some researchers have selected a power-duration model that best describes the training intensity range of athletes. For example, the two-parameter CP model [1] is only suitable for the severe exercise intensity domain. However, much power output falls within the high exercise intensity domains. So this model does not provide a fair generalization of the cyclist’s power curve. This also shows that diﬀerent examples maybe require diﬀerent modeling approaches.

<!-- b000124 | prose | pages [4] -->
With the development of physiology, there has been a growing awareness that a power curve can be divided into three diﬀerent exercise intensity domains: Extreme, Severe, and Heavy [2]. And it provides a comprehensive approach to studying tolerable exercise limits. Previous research has shown that the anaerobic power reserve (APR) can well predict short-term (<3 min) power outputs in the extreme exercise intensity domain [3]. In the severe exercise intensity domain, the CP models are mainly used. There is also a three-parameter CP model [4]. Currently, a full-power model exists for the heavy exercise intensity domain [5].

<!-- b000125 | heading | pages [4] -->
1.3 Our Work

<!-- b000126 | prose | pages [4] -->
We set up two models based on the assumptions and literature, including the three-stage power curve and dynamic bicycle models. The power curve model’s three stages are Extreme, Severe, and Heavy, characterized by distinct human physiological responses. The dynamic bicycle model is based on physics principles and describes the inﬂuence of weather factors on the power output. We then tested the model on diﬀerent riders and tracks, with good results. Finally, we designed the team time trial formation to make our model more applicable.

<!-- b000127 | caption | pages [4] -->
Figure 2: The structure of our paper

<!-- b000128 | furniture | pages [5] -->
Team # 2207343

<!-- b000129 | furniture | pages [5] -->
Page 4 of 22

<!-- b000130 | heading | pages [5] -->
2 Assumptions and Justiﬁcations

<!-- b000131 | prose | pages [5] -->
Through a complete analysis of the problem, in order to simplify our model, we make the following reasonable assumptions.

<!-- b000132 | prose | pages [5] -->
Assumption 1: Assuming that the temperature and humidity of the cyclist’s competition venue are suitable, and the ﬂuctuation range is small. Take the temperature range of 67.6 ∼75.6◦F and the humidity range of 35.1 ∼45.9%.

<!-- b000133 | prose | pages [5] -->
First, considering that most of the major cycling competitions, including the two cycling com- petitions given by the problem, are held in July-September. Then check the past weather conditions and ﬁnd that the temperature and humidity of the arena are relatively suitable.

<!-- b000134 | prose | pages [5] -->
Assumption 2: Assuming that cyclists in diﬀerent physical states, ride with the same power for the same time, they consume the same amount of energy.

<!-- b000135 | prose | pages [5] -->
The principle of physical strength distribution of professional athletes at diﬀerent stages during the competition is mostly based on the model of lactic acid accumulation and ATP conversion [6]. These models have linear properties in explaining human energy expenditure [7].

<!-- b000136 | prose | pages [5] -->
Assumption 3: Assuming that cyclists lose a constant 5% of their energy during cycling.

<!-- b000137 | prose | pages [5] -->
The cyclist is the engine providing the power. Friction in the drive train (chains, gears, bearings, etc.) causes a small amount of loss, usually around 5%[8], assuming the bicycle has a clean and nicely lubricated drivetrain.

<!-- b000138 | heading | pages [5] -->
3 Notations

<!-- b000139 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000140 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000141 | prose | pages [5] -->
Symbol Deﬁnitions Units CP W/kg Critical power W ′ J/kg Work capacity above critical power λE The cyclist’s remaining energy/the upper energy / Pout W/kg The output power of rider tn s Completion time vwind m/s Wind speed

<!-- b000142 | heading | pages [5] -->
4 Three stage power-duration models

<!-- b000143 | prose | pages [5] -->
As a source of parameters for power curve calculations and track-speciﬁc decisions, power proﬁles should demonstrate important biological parameters for bike racing of all types of riders. Based on this premise, we combine the literature review mentioned above to analyze various parameter characteristics of existing models. In the end, we selecte a sprinter and time trial specialist as our main subjects. We also calculate the parameters CP,W ′,etc., which can help get the power curve.

<!-- b000144 | prose | pages [5, 6] -->
Next, we obtain the maximum power that can be maintained by diﬀerent cyclists when they ride for 5s, 1min, 3min, 5min, 12min, and one has the data source for parameter calcu-lation. We also consult the relevant website to obtain the calculation method of the Maximum aerobic power MAPTTF and the value of at the end of every stage.

<!-- b000145 | furniture | pages [6] -->
Team # 2207343

<!-- b000146 | furniture | pages [6] -->
Page 5 of 22

<!-- b000148 | prose | pages [6] -->
Finally, we calculated the results and presented the power proﬁle in a tabular format, with a graph showing the power curves for both athletes of diﬀerent genders.

<!-- b000149 | heading | pages [6] -->
4.1 The Establishment of power-duration model

<!-- b000150 | prose | pages [6] -->
First, we use CP to represent the critical power of a cyclist. Critical power means the power output that cyclists tend to ride at high intensity, usually lasting 30 to 40 minutes. We then use W ′ to represent the work (in J/kg) that the cyclist can expend above CP before fully depleting energy.

<!-- b000151 | prose | pages [6] -->
Due to the complex metabolism of the human body, and the research on related biomechanics and biochemical reactions during exercise is also pending breakthroughs. Therefore, the calculation of CP, W ′ is generally obtained from experimental data. It can be seen from the literature [9] that the calculation formulas of CP and W ′ are as follows:

<!-- b000152 | prose | pages [6] -->
CP = 12 · P12 −3 · P3 (1) 9 W ′ = 0.24s · (P3 −P12) (2)

<!-- b000153 | prose | pages [6] -->
where P3 is the average power of a cyclist who rides hard for three minutes divided by his mass, while P12 is the same as P3 but for 12 minutes.And we also have the formulas of MAPTTF

<!-- b000154 | prose | pages [6] -->
W ′ W ′ MAPTTF = P −CP + (3) Pmax −CP According to relevant information[9], we estimate thatPmax ≈ where Pmaxis ultimate power. P5s.Integrating the formulas above, we get the following table:

<!-- b000155 | caption | pages [6] -->
Table 2: The power proﬁle of diﬀerent types of riders I

<!-- b000156 | prose | pages [6] -->
Race Gender 5s 1min 3min 5min 12min

<!-- b000157 | prose | pages [6] -->
M 21.03 9.09 6.95 4.81 4.70 Sprinter F 16.40 7.39 6.17 4.17 4.13 M 16.89 8.74 7.14 5.53 5.46 Time Trial Specialist F 13.39 7.11 5.85 4.83 4.75

<!-- b000158 | caption | pages [6] -->
Table 3: The power proﬁle of diﬀerent types of riders II

<!-- b000159 | prose | pages [6] -->
W ′ FTP CP MAPTTF CPTTF Race Gender

<!-- b000160 | prose | pages [6, 7] -->
M 3.91 3.94 0.54 1.10 33.79 Sprinter F 3.39 3.45 0.49 0.99 32.60 M 4.98 4.90 0.40 0.97 40.29 Time Trial Specialist F 4.38 4.38 0.26 0.92 34.41 According to the diﬀerent exercise time and the characteristics of various athletes in diﬀerent stages, we refer to the literature review to solve the power curve in three stages. Its scope and calculation model are shown in the following table:

<!-- b000161 | furniture | pages [7] -->
Team # 2207343

<!-- b000162 | furniture | pages [7] -->
Page 6 of 22

<!-- b000164 | caption | pages [7] -->
Table 4: Three stage power-duration models

<!-- b000165 | prose | pages [7] -->
Stage Model Equation Range

<!-- b000166 | prose | pages [7] -->
Anaerobic P(t) = P3 + (Pmax −P3) · e−kt t < MAPTTF I.Extreme power reserve

<!-- b000167 | prose | pages [7] -->
t > MAPTTF 2-parameter critical P(t) = W ′ t + CP II.Severe t < CPTTF power model   1 −et· CP −Pmax P(t) = W ′ t · W ′ Omni power   t > CPTTF III.Heavy duration model t +CP −A · ln CPT T F ( Combining curve continuity, take k=0.7, A=0.1)

<!-- b000168 | heading | pages [7] -->
4.2 The Solution of Power-Duration Model

<!-- b000169 | prose | pages [7] -->
Then we combine formula (1), formula (2) and the data in Table 2, together with the data in Table 3, and substitute them into the formula in Table 4. We use Mathematica to calculate and draw the curve to get the following power curve in ﬁg .3.

<!-- b000170 | caption | pages [7] -->
Figure 3: The power curve of diﬀerent types of rider. Left: Power curve for 0∼40 min. Middle:

<!-- b000171 | prose | pages [7] -->
Power curve for 0∼1 min(Extreme domain). Right: Power curve for 1∼40 min(Severe&Heavy domain)

<!-- b000172 | prose | pages [7] -->
Looking at the curves, in the same event, the power curve of male cyclists is always above the power curve of female cyclists. This is consistent with the pattern of better physical strength in male cyclists. In addition, in terms of short bursts (t < 1s), the power of the sprinter was signiﬁcantly higher than that of the time trial specialist. In the middle- and long-distance riding competitions, the time trial specialist are better.

<!-- b000173 | heading | pages [7] -->
5 Piecewise Nonlinear Programming for Time Trial

<!-- b000174 | heading | pages [7] -->
5.1 The Establishment of Human Energy Expenditure Model

<!-- b000175 | prose | pages [7] -->
To apply the power curve model established in Task 1 to the courses, we next derive a human energy expenditure model suitable for the problem background.

<!-- b000176 | furniture | pages [8] -->
Team # 2207343

<!-- b000177 | furniture | pages [8] -->
Page 7 of 22

<!-- b000178 | prose | pages [8] -->
Let m · Pout be the power output by the cyclist at time t. where m is the weight of cyclist, and Pout is the output power per unit mass of cyclist.

<!-- b000179 | caption | pages [8] -->
Figure 4: The illustration of Task 2. Left: The schematic diagram of variable power output. Middle:

<!-- b000180 | prose | pages [8] -->
The discrete function of Pout −t. Right: The continuous function of Pout −t.

<!-- b000181 | prose | pages [8] -->
According to Assumption 2, we calculate in proportion to the total energy consumed. For the power discrete values shown in the middle of Fig. 4, the ratio of the cyclist’s remaining energy to the upper energy limit is expressed as follows:

<!-- b000182 | prose | pages [8] -->
X λE = ER ∆ti = 1 − (4) Em Ti i

<!-- b000183 | prose | pages [8] -->
where Ti is the longest holding time of the current power when the body is full of energy. In the middle of ﬁg. 4, the result of λE is λE = 1 −10s 20s −5s 10s = 0.

<!-- b000184 | prose | pages [8] -->
Change the discrete model to continuous. For the continuity Pout (t) shown in the right of ﬁg. 4, cut an approximate rectangle with a width of dt, and the height of the rectangle is T(Pout) . Next, replace the summation with the integral to get the formula for λE at time t Z t dτ λE (t) = 1 − (5) T (Pout (τ)) 0 where T(P) is the inverse function of the power curve expression P(t), i.e., T (P) = P −1 (P).

<!-- b000185 | prose | pages [8] -->
If the cyclist just uses up his energy when he reaches the ﬁnish line, the following constraint exists: Z t dτ 1 −λE (t) = T (Pout (τ)) = 1 (6) 0

<!-- b000186 | prose | pages [8] -->
However, when solving practical problems, it is impossible for cyclists to strictly follow a detailed plan of the optimization solution. This can lead to cyclists hitting their ﬁtness limits before they ﬁnish the race. Therefore, we reduce the 1 on the right side of the equation to 0.95, leaving 5% of the remaining stamina to deal with the above situation.

<!-- b000187 | heading | pages [8] -->
5.2 The Mathematical Relationship Between Power Output And Speed

<!-- b000188 | prose | pages [8] -->
We conduct a dynamic analysis on the bicycle, the force diagram is shown in the left of ﬁg. 5, and the following formula is established:

<!-- b000189 | prose | pages [8] -->
Ftotal = (Froll + Fslope + Faccel + Fwind) /η (7)

<!-- b000190 | prose | pages [8, 9] -->
where Ftotal is the athlete’s active force, Froll is the rolling friction force, Faccel is the inertial force generated by the acceleration, Fwind is the aerodynamic resistance, and Fslope is the slope resistance (negative value when going downhill). According to assumption 3, we set η as the driving eﬃciency, which is 95%.

<!-- b000191 | furniture | pages [9] -->
Team # 2207343

<!-- b000192 | furniture | pages [9] -->
Page 8 of 22

<!-- b000194 | caption | pages [9] -->
Figure 5: Left: Analysis of bicycle force. Right: Pout −v plot

<!-- b000195 | prose | pages [9] -->
According to the principles of physics, the calculation formulas of various physical quantities are as follows:

<!-- b000196 | prose | pages [9] -->
Froll = Cr · Mg (0.0015 < Cr < 0.015, M = m + mbike ≈1.2 · m) (8)

<!-- b000197 | prose | pages [9] -->
Fslope = Mg · sin θ (9)

<!-- b000198 | prose | pages [9] -->
Faccel = a · M (10) Fwind = 1 2CWA · ρ v2 (11) wind

<!-- b000199 | prose | pages [9] -->
where ρ is the air density. Based on the temperature and humidity values in Assumption 1, we get ρ = 1.29 kg/m3 . CW is the wind resistance coeﬃcient. A is the frontal area, which satisﬁes CWA = 0.39 m2 and is only valid for the frontal incident ﬂow. Under no wind conditions, vwind = vbike.

<!-- b000200 | prose | pages [9] -->
Combining the above equations, and then by m · Pout = Ftotal · v, we can obtain the conversion relationship between Pout and v, as shown in the right of ﬁg. 5.

<!-- b000201 | heading | pages [9] -->
5.3 The Racing Strategy of Self-designed course

<!-- b000202 | prose | pages [9] -->
We ﬁrst design a course that includes basic road conditions such as straights, downhill slopes, and sharp turns to obtain the strategies to be adopted in diﬀerent road conditions. This strategy is then used to solve complex course problems in two real races.

<!-- b000203 | caption | pages [9] -->
Figure 6: Left: Self-designed track scene construction. Right: Self-designed 3D map of the track

<!-- b000204 | furniture | pages [10] -->
Team # 2207343

<!-- b000205 | furniture | pages [10] -->
Page 9 of 22

<!-- b000206 | prose | pages [10] -->
We use Webots software to build the track scene, and draw the plan and 3D map of the self- designed course, as shown in ﬁg. 6. Section AB is a short uphill, section CD is a long uphill and section EF is a long downhill.

<!-- b000207 | heading | pages [10] -->
5.3.1 Analysis of Riding Strategies on Curved Roads

<!-- b000208 | prose | pages [10] -->
First, we analyze the corner riding strategy. We expect cyclists to go through the corners at the top speed allowed. This not only reduces the time to pass the curve, but also reduces the acceleration and deceleration time of the straight road.

<!-- b000209 | prose | pages [10] -->
We set the inner diameter of the curve as r, the road width as d, and R as the radius of the optimal path arc. According to the centripetal force calculation formula F = mv2 r , the maximum turning rate can be achieved by taking the route shown in the ﬁgure below. In this case, the physical quantities are related as follows:

<!-- b000210 | prose | pages [10] -->
Integrating, we get the maximum speed of cornering s   d + r −r cos θ µg · cos α · 2 (∗) vmax = 1 −cos θ 2

<!-- b000211 | prose | pages [10] -->
Since the total length of the curves of the self-designed track is 0.185km, it can be ignored compared with the total length of the straight track of 36.5km. Therefore, we ﬁrst only consider the straight time when calculating the time and ignore the speed change problem in the turn. We approximated the rider’s power output before and after the turn as a step change. After this is done, we complete the optimal passing scheme for each turn.

<!-- b000212 | heading | pages [10] -->
5.3.2 Analysis of Straight Riding Strategy

<!-- b000213 | prose | pages [10] -->
Next, we analyze the straight riding strategy. We assume that there are ni sections of horizon- tal straights (lengthsL1, L2, ..., Lni),nj sections of downhill straights(lengths D1, D2, ...Dnj) and nk sections of uphill straights(lengths U1, U2, ..., Unk). The conversion function v −Pout of the hori- zontal straight is v(straight) (P), the function for a downhill straight with an inclination angle θj is v(downhill) (P), and v(uphill) (P) is the function for a uphill straight with an inclination angle θk. The θj θk task then turns into the following planning problem:

<!-- b000214 | prose | pages [10] -->
nj nk ni X X X Li Dj Uk t = v(straight) (Pi) + + v(downhill) v(uphill) (Pj) (Pk) i=1 j=1 θj k=1 θk

<!-- b000215 | prose | pages [10, 11] -->
find Pout (t) , (12) Z tn dt∗ min {t} s.t. T (Pout (t∗)) = 0.95 0

<!-- b000216 | furniture | pages [11] -->
Team # 2207343

<!-- b000217 | furniture | pages [11] -->
Page 10 of 22

<!-- b000219 | prose | pages [11] -->
In this map, ni = 7, nj = 1, nk = 1.The subscript of L, D, U is marked in an increasing manner from the start point to the end point.

<!-- b000220 | prose | pages [11] -->
R tn dt∗ As for this function, we discretize Pout (t).This makes the numerical calculation of T(Pout(t∗)) 0 easier to implement. And we can use Pi, Pj, Pk to draw the Pout (x) graph, which is more helpful for cyclists to judge the output power according to the track landscape.

<!-- b000221 | caption | pages [11] -->
Figure 7: Ramp division

<!-- b000222 | caption | pages [11] -->
Figure 8: Time trial male rider strategy

<!-- b000223 | prose | pages [11] -->
We use Mathematica to numerically solve the inverse function and the nonlinear programming function Minimize. Then get the results shown in the table below:

<!-- b000224 | caption | pages [11] -->
Table 5: The results of the self-designed time trial course

<!-- b000225 | prose | pages [11] -->
Pout (L) Pout (U1) Pout (D1) t Rider type Gender

<!-- b000226 | prose | pages [11] -->
M 6.0 6.3 5.2 47.53min Sprinter F 5.8 6.0 5.1 48.58min M 6.5 6.4 5.1 46.48min Time Trial Specialist F 6.0 5.9 5.0 48.20min

<!-- b000227 | prose | pages [11] -->
We next solve for the turn time. We use the formula (*) and the conversion function to solve, and get the following results:

<!-- b000228 | caption | pages [11] -->
Table 6: The results of each turn

<!-- b000229 | prose | pages [11] -->
Curve number A B C D E Pout 2.94 7.27 4.94 3.23 12.13 v 7.34 11.02 9.48 7.98 13.38

<!-- b000230 | prose | pages [11] -->
Comparing the above two tables, it can be seen that the cyclist must slow down to pass the turn due to the large angle of turns A and D. Although the turn at C is 53 degrees, it is on a scope, which reduces the upper limit of static friction. So deceleration is also required. Turn B is no need to slow down.

<!-- b000231 | furniture | pages [12] -->
Team # 2207343

<!-- b000232 | furniture | pages [12] -->
Page 11 of 22

<!-- b000233 | prose | pages [12] -->
In bicycle competition, the acceleration can reach 2m/s2 when accelerating and decelerating. The time for this process can be ignored.

<!-- b000234 | prose | pages [12] -->
Combining the results of the straights and corners above, the optimal Pout (t) during the rider’s competition is shown in ﬁg. 8 (taking a male time trial specialist as an example).

<!-- b000235 | heading | pages [12] -->
5.4 The Strategy of 2021 UCI World Championship time trial course

<!-- b000236 | caption | pages [12] -->
Figure 9: 2021 UCI Track Division

<!-- b000237 | caption | pages [12] -->
Figure 10: The ﬁnish near the city center plaza

<!-- b000238 | prose | pages [12] -->
According to the data on UCI’s oﬃcial website, we determined the terrain and route characteristics of the area of the course on Google Earth. And we divide the track into 32 parts by analyzing the similarities and diﬀerences of the road sections (as shown in ﬁg. 9). Among them, 15 sections are curves, 2 sections are horizontal straights, 3 sections are downhill straights, and 12 sections are uphill straights.

<!-- b000239 | caption | pages [12] -->
Figure 11: Detail of section #25

<!-- b000240 | prose | pages [12, 13] -->
It is worth noting that the competition area is located in northwestern Belgium. It is in the High Flanders Plain with small undulations. The maximum slope angle in the uphill section of this area is 1.66◦, while in the downhill section is 0.69◦. Besides, there are suﬃciently long straights to transition between adjacent turns. The shortest straight is our section numbered 25 (shown in ﬁg. 11). Section #25 is about 400m long, which is enough for cyclists to maintain the optimum for a long time. Therefore, the rider’s passing time is hardly aﬀected by turning, and the piecewise discrete programming model is still applicable.

<!-- b000241 | furniture | pages [13] -->
Team # 2207343

<!-- b000242 | furniture | pages [13] -->
Page 12 of 22

<!-- b000244 | prose | pages [13] -->
Diﬀerent from the Olympic Time Trial course in Tokyo, this competition has relatively low requirements on players’ driving skills and cornering skills and focuses on physical distribution and endurance.

<!-- b000245 | heading | pages [13] -->
5.4.1 The Strategy of Straight and Ramp Riding in Belgium course

<!-- b000246 | prose | pages [13] -->
Based on the above analysis, we can still use the method of self-designed track. First, we solve the straight strategy, as follows:

<!-- b000247 | prose | pages [13] -->
nj nk ni X X X Li Dj Uk t = v(straight) (Pi) + + v(downhill) v(uphill) (Pj) (Pk) i=1 j=1 θj k=1 θk

<!-- b000248 | prose | pages [13] -->
find Pout (t) , (13) Z tn dt∗ min {t} s.t. T (Pout (t∗)) = 0.95 0

<!-- b000249 | prose | pages [13] -->
where ni = 2, nj = 3, nk = 12.

<!-- b000250 | prose | pages [13] -->
Considering that there are many uphill sections and diﬀerent slope angles. It makes the model diﬃcult to converge, which is extremely unfavorable for the computer’s nonlinear programming solution. Due to the small undulating terrain in this area, we selected 9 road sections with slope angles below 1◦(#1, 3, 5, 7, 11, 17, 29, 30, 32) and group them together. Then we can weight the slope angle according to the road length to get the integrated new slope. We next use the new slope to solve.

<!-- b000251 | prose | pages [13] -->
Since sin θ 2 is approximately linear in the range of small slope angles. When integrating multiple ramps, we can use approximately linear properties for weighting. The parameters are determined by the following equations: X X wk · θk UC = Uk, = θC (14) k∈AU k∈AU X wk = Uk/ Uq (15) q∈AU

<!-- b000252 | prose | pages [13] -->
After processing, the problem is transformed into the following nonlinear programming problem:

<!-- b000253 | prose | pages [13, 14] -->
nj ni X X X Li Dj UC Uk t = v(straight) (Pi) + + + v(downhill) v(uphill) v(uphill) (Pj) (Pk) (PC) i=1 j=1 θj θk θC k/∈AU find Pout (t) , (16) Z tn dt∗ min {t} s.t. T (Pout (t∗)) = 0.95 0 sprinters. Middle: Pout(x) plot for time trial specialist. Right: Scatter plot of maximum rate in the turn

<!-- b000254 | furniture | pages [14] -->
Team # 2207343

<!-- b000255 | furniture | pages [14] -->
Page 13 of 22

<!-- b000256 | caption | pages [14] -->
Figure 12: The results of 2021 UCI World Championship time trial course. Left: Pout(x) plot for

<!-- b000258 | prose | pages [14] -->
We use Mathematica to solve the optimal output power of each section of the road. The athlete curves are shown in the left and middle of ﬁg. 12. The four types of riders’ complete time are shown in the following table:

<!-- b000259 | caption | pages [14] -->
Table 7: The results of 2021 UCI World Championship time trial course

<!-- b000260 | prose | pages [14] -->
Male time Female time Rider type Male sprinter Female sprinter trial specialist trial specialist

<!-- b000261 | prose | pages [14] -->
Complete time 58.15min 59.62min 53.03min 54.05min

<!-- b000262 | heading | pages [14] -->
5.4.2 The Strategy of Turning in Belgium course

<!-- b000263 | prose | pages [14] -->
After that, we use the formula (*) and Pout (v) to solve for the maximum power in the turn. The results are shown in the right of ﬁg. 12. The scatter in the ﬁgure is the maximum turning power of the curve corresponding to x while the broken line is the Pout (t) of the male time trial specialist. It can be seen from the ﬁgure that the power of the cyclists on the straights is less than the maximum turning power, except for the #23 and #32 curves that require a slight deceleration.

<!-- b000264 | prose | pages [14] -->
In the above calculations, we approximated Pout (x) as a discrete function.We will further analyze the actual output of the players in 6.2, as shown in ﬁg. 13. This would justify our approach in this matter.

<!-- b000265 | caption | pages [14] -->
Figure 13: Actual output power

<!-- b000266 | caption | pages [14] -->
Figure 14: 2021 Olympic track division

<!-- b000267 | heading | pages [14] -->
5.5 The Strategy of 2021 Olympic Time Trial course

<!-- b000268 | prose | pages [14, 15] -->
As can be seen from ﬁg. 14, the Tokyo Circuit is located near the city of Toyama, which is surrounded by the treacherous Northern Alps Tateyama Mountains on three sides. The terrain here changes greatly and the turns are sharp, which is signiﬁcantly diﬀerent from the Belgian track. This event had high requirements on the slope skills of the cyclists. Besides, male cyclists need to circle the track twice while female cyclists only need once.

<!-- b000269 | furniture | pages [15] -->
Team # 2207343

<!-- b000270 | furniture | pages [15] -->
Page 14 of 22

<!-- b000272 | prose | pages [15] -->
We divided the Tokyo circuit into 68 segments and 2 zones (large circle and small circle) based on the terrain and ramp characteristics of the area. The division situation is shown in ﬁg. 14. Among them, most road sections in the large circle and some sections in the small circle can still be calculated by the previous model. For the other two road sections (the #24-27 big climbing curve in ﬁg. 16 and the #55-56 sharp curve in ﬁg. 17), we will analyze them separately later.

<!-- b000273 | heading | pages [15] -->
5.5.1 The Strategy for Regular Road Sections in Japan

<!-- b000274 | prose | pages [15] -->
Based on our segmentation of the track, in the remaining 62 regular road segments, ni = 20, nj = 25, nk = 17. Because 1 −cos 2◦< 7 × 10−4, cos 2◦−cos 4◦< 2 × 10−3, Therefore, we apply the weighted simpliﬁcation method in 5.4 to the slopes whose angle satisﬁes θ < 2◦and 2◦< θ < 4◦ respectively. The set of road segment numbers that meet the conditions is TU2, TD2, TU4, TD4. And |TU2| = 8, |TD2| = 9, |TU4| = 9, |TD4| = 11. Ultimately, the problem transforms into the following nonlinear programming problem:

<!-- b000275 | prose | pages [15] -->
ni X X X X Li Dj Uk UTi t = v(straight) (Pi) + + + v(downhill) v(uphill) v(up/down) (Pj) (Pk) (PTi) i=1 TU,TD θj θk θT i j /∈TD k/∈TU

<!-- b000276 | prose | pages [15] -->
as t = Σi + Σj + Σk + ΣT find Pout (t) , (17) Z tn dt∗ min {t} s.t. T (Pout (t∗)) = 0.95 0 where ΣT represents the integration item.

<!-- b000277 | prose | pages [15] -->
With the help of Mathematica, we get the curve of Pout (x), and the result is shown in ﬁg. 15. Compared with 2021UCI, the Tokyo circuit is more complicated. The diﬃ-culty of players’ physical distribution strategy has also increased signiﬁcantly.

<!-- b000278 | caption | pages [15] -->
Figure 15: The result of 2021 Olympic Time Trial course. Left: The Pout (x) plot of male cyclist.

<!-- b000279 | prose | pages [15] -->
Right: The Pout (x) plot of female cyclist. (The discontinuous part is a special road section and needs to be solved separately)

<!-- b000280 | furniture | pages [16] -->
Team # 2207343

<!-- b000281 | furniture | pages [16] -->
Page 15 of 22

<!-- b000282 | caption | pages [16] -->
Figure 16: Detail of section #24-27

<!-- b000283 | heading | pages [16] -->
5.5.2 The Strategy for Special Road Sections in Japan

<!-- b000284 | prose | pages [16] -->
(1)Huge hill turn of section #24-27

<!-- b000285 | prose | pages [16] -->
The parameters of these four sections are shown in the table below:

<!-- b000286 | caption | pages [16] -->
Table 8: The data of section #24-27

<!-- b000287 | prose | pages [16] -->
Section Length Turning radius Slope angle Turning angle 6.65◦ 0◦ #24 0.1km 0m 10.25◦ 147◦ ≈0km #25 9m 5.99◦ 0◦ #26 0.1km 0m 4.22◦ 79◦ ≈0km #27 8.5m

<!-- b000288 | prose | pages [16] -->
The straight part here is steep, such as section #63 with a slope angle of 4.4◦.The cyclist speed here is 6.83m/s and the output power is 5.5W/kg. We will base our straights strategy around this data.

<!-- b000289 | prose | pages [16] -->
Next, we analyze the turning strategy. The curve is a sharp turn with continuous climbing. We use formula (*) to calculate. The best turning speed of section#25 is 6.0m/s, with P (#25) = 6.32 W/kg. And the speed of section#27 is 6.4 m/s, P (#27) = 5.31 W/kg. In this way, the time used for this max section is 31.2s.

<!-- b000290 | prose | pages [16] -->
(2)Sharp turn of section#55-56

<!-- b000291 | prose | pages [16] -->
The parameters of these four sections are shown in the table below:

<!-- b000292 | caption | pages [16] -->
Table 9: The data of section #55-56

<!-- b000293 | prose | pages [16] -->
Section Length Turning radius Slope angle Turning angle 0◦ ≈0◦ 0◦ #55km 0.2m 12◦ ≈0◦ 166.9◦ ≈0m #56km

<!-- b000294 | prose | pages [16, 17] -->
As for this turn, it has a small inner diameter and a high turning angle of 166.9◦. By calculation, v(#56) = 5.806 m/s, P (#56) = 4.32 W/kg. On the straight #55, Pout = 5.6 W/kg, v = 10.0m/s. max max We plan to start decelerating 20m before the start of section #56. And accelerate back to the original speed immediately after passing the turn #56. It take 21.7s.

<!-- b000295 | furniture | pages [17] -->
Team # 2207343

<!-- b000296 | furniture | pages [17] -->
Page 16 of 22

<!-- b000298 | caption | pages [17] -->
Figure 17: Detail of section #55-56

<!-- b000299 | prose | pages [17] -->
Combining 5.5.1 and 5.5.2, the results of the four players under the optimization strategy are shown in the following table:

<!-- b000300 | caption | pages [17] -->
Table 10: The results of 2021 Olympic Time Trial course

<!-- b000301 | prose | pages [17] -->
Male time Female time Rider type Male sprinter Female sprinter trial specialist trial specialist

<!-- b000302 | prose | pages [17] -->
Complete time 62.68min 56.03min 40.97min 33.63min

<!-- b000303 | prose | pages [17] -->
It can be seen that the nontrivial road condition increases the test of the cyclist’s climbing ability and endurance. The sprinter’s performance was signiﬁcantly lower than that of the time trial specialist. This disparity is larger than that of UCI.

<!-- b000304 | heading | pages [17] -->
6 Sensitivity Analysis

<!-- b000305 | heading | pages [17] -->
6.1 Sensitive Analysis of Weather

<!-- b000306 | prose | pages [17] -->
Weather conditions include temperature, humidity, wind speed, wind direction, etc.

<!-- b000307 | prose | pages [17] -->
According to the theory of blood CK and HB [10], within a certain range, temperature and humidity have little eﬀect on the physical ﬁtness of athletes. From Assumption 1, the conclusion can be further proved reasonable.

<!-- b000308 | prose | pages [17] -->
Secondly, rain has little eﬀect on the rolling friction coeﬃcient of the asphalt track. Rain only increases the demands on the driver’s turning skills. The literature [11] indicates that the negative impact of rain can be eliminated to a certain extent through training.

<!-- b000309 | prose | pages [17] -->
In conclusion, our analysis of the sensitivity to weather factors will focus on wind speed and direction.

<!-- b000310 | furniture | pages [18] -->
Team # 2207343

<!-- b000311 | furniture | pages [18] -->
Page 17 of 22

<!-- b000312 | prose | pages [18] -->
We divide the sensitivity analysis into two parts: straight sections and turning sections to determine the potential impact of wind directions and wind. The inﬂuence of the road gradient is mainly reﬂected in the friction of the bicycle. Therefore, we uniformly assume that the road slope is 0% in the sensitivity analysis.

<!-- b000313 | prose | pages [18] -->
(1)Straight sections

<!-- b000314 | prose | pages [18] -->
On the straights, only the eﬀective wind speed will aﬀect the ride. The eﬀective wind speed is in the same direction as the cyclist. Therefore, we only analyze the sensitivity of the model to the wind speed in this part.

<!-- b000315 | prose | pages [18] -->
According to the wind speed requirements of cycling events, as well as the average wind speed of Japan and Belgium in July, we selected the wind speed to be around 2m/s for analysis.

<!-- b000316 | prose | pages [18] -->
We use Python to draw the maximum output power curve and the wind resistance inﬂuence power curve within the range of ±1% deviation of wind speed. The results are shown in ﬁg. 18.

<!-- b000317 | caption | pages [18] -->
Figure 19: Change of Pout (v) and PW (v)

<!-- b000318 | caption | pages [18] -->
Figure 18: Sensitivity of wind speed

<!-- b000319 | caption | pages [18] -->
Figure 19 shows the changes of and curves (moving from bottom to top) when the wind speed

<!-- b000320 | prose | pages [18] -->
changes from 1m/s to 4m/s.

<!-- b000321 | prose | pages [18] -->
From the ﬁgure, when the cyclist rides at a constant speed on the straight, the deviation is 10%. Therefore, the model is more sensitive to wind speed in straight sections.

<!-- b000322 | prose | pages [18] -->
(2)Turning sections

<!-- b000323 | prose | pages [18] -->
Next, we analyze the model’s sensitivity to wind speed and direction during turning. We use Python to perturb the model within 10% of the deviation from the wind speed and direction. The results are shown in ﬁg. 20. where γ is the local wind angle.

<!-- b000324 | prose | pages [18] -->
During the turning sections, the eﬀect of wind direction change on the rider’s maximum output power is on the order of 0.1%, while the eﬀect of wind speed changes is on the order of 0.01%. Both eﬀects are much smaller than the straight sections. Therefore, the model is less sensitive to wind speed and direction in the turning sections.

<!-- b000325 | prose | pages [18] -->
In conclusion, the change of wind direction and speed within a certain range will not aﬀect the turning strategy of the model. On the other hand, the model is more sensitive to headwind. In individual races, the output power when the wind is down can be appropriately reduced, while the wind is up it can be increased.

<!-- b000326 | furniture | pages [19] -->
Team # 2207343

<!-- b000327 | furniture | pages [19] -->
Page 18 of 22

<!-- b000328 | caption | pages [19] -->
Figure 20: Sensitivity of wind speed&direction. Left: The course in Japan, withvwind = 2m/s, γ =

<!-- b000329 | prose | pages [19] -->
−45◦. Right:The course in Belguim, withvwind = 2m/s, γ = 180◦.

<!-- b000330 | prose | pages [19] -->
In addition, this phenomenon provides ideas for the strategy of team time trial, which we will focus on in Section VII.

<!-- b000331 | heading | pages [19] -->
6.2 Sensitive Analysis of Rider Deviations

<!-- b000332 | prose | pages [19] -->
In the Pout (x) solution process of 5.3-5.5, we adopt an idealized approximate discrete value model, so the power output of the rider on each small segment remains constant. In practical situations, due to the randdomness of the rider’s operation, it is diﬃcult to strictly follow the optimal power curve. In this part we will test the sensitivity of the rider deviations from the target power to the model.

<!-- b000333 | prose | pages [19] -->
First, take the time trial in the 2021 UCI as an example. We perform spline interpolation on each segment of the discrete Pout (x) based on its endpoint values. They are then used as a function Pout of Pout = P4 the actual output of the rider. Then, we add random disturbance term g i=1 Ai sin (0.1i · t), where Ai is determined by a random number and 0 < Ai < 5% · P (max) . Then the actual power out = Pout + g output function of the rider is P (real) Pout. We conduct three experiments and get three out P (real) (x) curves. Plot them in the same coordinate system as the ideal Pout (x) curve, as shown in out the left of ﬁg. 21.

<!-- b000334 | caption | pages [19] -->
Figure 21: The results of the model. Left: The curve of Pout (x) & P (real)

<!-- b000335 | prose | pages [19] -->
(x). Middle: 1- of out diﬀerent strategies. Right: The Competition time of diﬀerent strategies

<!-- b000336 | prose | pages [19, 20] -->
We put the four curves into the energy constraints, and it turned out that all riders could ﬁnish the race. In terms of whether it can ﬁnish the race, the stability of the model is excellent. The speciﬁc results are shown in the middle of ﬁg. 21.

<!-- b000337 | furniture | pages [20] -->
Team # 2207343

<!-- b000338 | furniture | pages [20] -->
Page 19 of 22

<!-- b000340 | prose | pages [20] -->
Next, we calculated the time it took for the rider to reach the ﬁnish line (see the right of ﬁg. 21). Rider results are all below the ideal output curve. But the lag time is within 2.5% of the optimal time. Therefore, the sensitivity of the race performance to the actual strategy of the rider is low. We recommend that riders maintain an ideal power curve at the end of each segment, which helps reduce lag time.

<!-- b000341 | prose | pages [20] -->
Finally, we compared the calculation results of our model with the results of the actual competition winners. The results are as follows:

<!-- b000342 | caption | pages [20] -->
Table 11: The comparison between Championship results and our model’s results

<!-- b000343 | prose | pages [20] -->
Rider type Male cycling time trial Female cycling time trial

<!-- b000344 | prose | pages [20] -->
The results of our model 56.03min 34.63min

<!-- b000345 | prose | pages [20] -->
Championship results 55.08min 30.22min

<!-- b000346 | prose | pages [20] -->
The model’s results are slightly behind the world championship results. This may be related to the fact that the experimental data samples we use to determine the power curve are from average riders rather than top riders.

<!-- b000347 | prose | pages [20] -->
Compared with the championship, the results of our model solution are reasonable. It also shows that our model has the eﬀect of bringing average-qualiﬁed riders close to the performance of champion riders, which illustrates the eﬀectiveness of the model.

<!-- b000348 | heading | pages [20] -->
7 Further Discussion of The Team Time Trial

<!-- b000349 | prose | pages [20] -->
In the 6.1, we concluded that the crosswind have little eﬀect on the rider, while the headwind have a big eﬀect. We found that this feature can be applied to the optimization of team time trials. By reviewing the literature, we came to the following conclusions:

<!-- b000350 | prose | pages [20] -->
Due to the existence of drafting yields, within a certain distance (<1m), the wind resistance of the second rider on the pace line is reduced to 60-70% of the individual rider. While the drag for the third rider dropped to about 50-63%. The drag along the convoy will gradually decrease to about 47-60%.

<!-- b000351 | prose | pages [20] -->
In addition, due to the existence of " subsonic upstream disturbance ". With multiple riders, it’s not necessarily that the last rider has the least wind resistance. In fact, the last rider is the only rider on the pace line who didn’t beneﬁt from the subsonic upstream disturbance .

<!-- b000352 | prose | pages [20] -->
We will mainly analyze the formation strategy of the cycling team to deal with the headwind on the straight. We calculated the team and individual results on the 1km straight to verify the rationality and eﬀectiveness of the strategy.

<!-- b000353 | prose | pages [20] -->
For the 6-person cycling team, we have two formations, the snake and the pyramid. For the 4-person sprint cycling team, we designed the shield formation as shown in the left of ﬁg. 22. The numbers in the heat map represent the ratio of the wind resistance of the individual in the team competition to that in the same state of the individual competitionKf.

<!-- b000354 | furniture | pages [21] -->
Team # 2207343

<!-- b000355 | furniture | pages [21] -->
Page 20 of 22

<!-- b000356 | caption | pages [21] -->
Figure 22: Left: Schematic diagram of three formations in team time trial. Right: Team strategy in

<!-- b000357 | prose | pages [21] -->
the time trial.

<!-- b000358 | prose | pages [21] -->
We divide the race into three stages to calculate the team race results on the 20km straight: Balance, Storage, and Sprint. The lengths are LB, LS, LR and LB + LS + LR = 20 km .

<!-- b000359 | prose | pages [21] -->
• Balance: 6 riders take turns riding in 6 positions. In this way, the physical energy consumption caused by wind resistance is balanced. We choose the formation with the lowest average resistance coeﬃcient Kf as the optimal one. It is calculated that the snake formation Kf = 67.17 and the pyramid formation Kf = 64.83, so we choose the pyramid formation.

<!-- b000360 | prose | pages [21] -->
• Storage: Since changing the formation will cause the rider to consume excess physical strength;

<!-- b000361 | prose | pages [21] -->
the formation should be maintained as much as possible. Besides, the four riders who cross the line should rotate in the position with the smaller drag coeﬃcient, while the other two riders (called windbreakers) should rotate in the place with the larger drag coeﬃcient. Considering the balance of the sprinters in the long snake formation, we choose the long snake formation after weighing.

<!-- b000362 | prose | pages [21] -->
• Sprint: According to the simulation results of literature [12], we choose the shield formation with the smallest drag coeﬃcient.

<!-- b000363 | prose | pages [21] -->
Next, take the data of male time trial specialists as an example to calculate. The result is that the Balance section accounts for 48%, the Storage section accounts for 27%, and the sprint section accounts for 25%, as shown in Figure e2. The 20km straight individual race was 24.8min, and the team race was 21.2min. The team competition results are signiﬁcantly better than the individual competition. Compared with the average speed of the Tour de France 2018 Stage3 champion BMC team of 56.1km/h, the average rate of our model on the straights is 56.6km/h, proving the model’s accuracy.

<!-- b000364 | caption | pages [21] -->
Figure 23: Left: Cycling strategy for lateral wind. Right: Slanted line array in Tour of Turkey 2016

<!-- b000365 | prose | pages [21] -->
In addition, for the case of crosswind, we take the wind coming from the right front as an example.

<!-- b000366 | furniture | pages [22] -->
Team # 2207343

<!-- b000367 | furniture | pages [22] -->
Page 21 of 22

<!-- b000368 | prose | pages [22] -->
The formation should be adjusted to the diagonal array, as shown in ﬁg. 23. It is beneﬁcial to reduce drag coeﬃcient and reduce crosswind disturbance.

<!-- b000369 | heading | pages [22] -->
8 Model Evaluation and Further Discussion

<!-- b000370 | heading | pages [22] -->
8.1 Strengths

<!-- b000371 | prose | pages [22] -->
• Eﬃcient solutions We exploit the linearity or near-linearity of the function when solving the optimal policy. The solution speed and convergence speed are greatly improved when performing integration and discrete approximations.

<!-- b000372 | prose | pages [22] -->
• Accuracy of results We relied on data and literature for model simpliﬁcation. And we have analyzed the special part of the track separately, which guarantees the accuracy. In addition, the solution results of the model are close to the championship results, which veriﬁes the accuracy of the results.

<!-- b000373 | prose | pages [22] -->
• Universality The piecewise nonlinear programming model we adopted is suitable for races where track information and player information are known. In addition to cycling time trials, swimming, running and other competitions can also be applied by modifying the parameters.

<!-- b000374 | prose | pages [22] -->
• Stability and high fault tolerance Our model was tested for sensitivity and its stability was veriﬁed. We chose the parameters of the average rider and set the energy utilization to 95%.

<!-- b000375 | prose | pages [22] -->
These steps also improve the fault tolerance of the model.

<!-- b000376 | heading | pages [22] -->
8.2 Weaknesses

<!-- b000377 | prose | pages [22] -->
• Lack of adversary factor Our model mainly analyzes unopposed time trials. The modeling process lacks consideration of oﬀense and defense strategies among riders.

<!-- b000378 | prose | pages [22] -->
• Diﬃculty in further improving accuracy We used numerical methods and discrete methods in the model. These methods limit the accuracy of the model. So in Sections VI and VII, we discuss the model further to improve this problem. It turns out that the improved model is more accurate.

<!-- b000379 | heading | pages [22] -->
8.3 Conclusion

<!-- b000380 | prose | pages [22] -->
Our paper provides a detailed analysis of the relationship between riding strategy and power curve. Before introducing our model, we analyze the characteristics of various types of riders and diﬀerent kinds of tracks. Then the three-stage power curve model and dynamic bicycle model are proposed.

<!-- b000381 | prose | pages [22, 23] -->
Next, in order to use the established mathematical model to optimize the strategy of the bicycle time trial, we divide the complex track into several simple segments according to the track charac- teristics such as slope and turn. Then, using nonlinear programming to solve the optimal strategy, we analyzed the self-made track, the Belgian track, and the Tokyo track. Diﬀerent types and genders of players have diﬀerent strategies. For the Belgian track, the deviation of the model solution results from the world championship results is about 8%. The model results deviate by about 6% for the Tokyo circuit. After that, we analyzed the model’s sensitivity to weather factors and rider deviations. Among the weather factors, wind speed and direction dominate. We conclude that the model is more sensitive to headwind. This conclusion is beneﬁcial to the formation analysis of the team time trial. We perturbed the model with random disturbance terms when studying the sensitivity to rider deviations, resulting in three power curves. The riders ﬁnish the race in this disturbance with little diﬀerence in their time, proving our model’s robustness.

<!-- b000382 | furniture | pages [23] -->
Team # 2207343

<!-- b000383 | furniture | pages [23] -->
Page 22 of 22

<!-- b000385 | heading | pages [23] -->
References

<!-- b000386 | references | pages [23] -->
[1] Moritani T, Ata AN, Devries HA, Muro M (1981) Critical power as a measure of physical work

<!-- b000387 | references | pages [23] -->
capacity and anaerobic threshold.Ergon 24(5):339350.

<!-- b000388 | references | pages [23] -->
[2] Burnley M, Jones AM (2007) Oxygen uptake kinetics as a determinant of sports perfor-mance.

<!-- b000389 | references | pages [23] -->
Eur J Sports Sci 7(2):6379.

<!-- b000390 | references | pages [23] -->
[3] Weyand PG, Lin JE, Bundle MW (2006) Sprint Performance-duration relationships are set by

<!-- b000391 | references | pages [23] -->
the fractional duration of external force application. Am J Physiol 290(3):5865.

<!-- b000392 | references | pages [23] -->
[4] Morton RH (1996) A 3-parameter critical power model. Ergon 39(4):611619.

<!-- b000393 | references | pages [23] -->
[5] Puchowicz MJ, Baker J, Clarke DC (2020) Development and ﬁeld validation of an omni-domain

<!-- b000394 | references | pages [23] -->
power-duration model. J Sports Sci 38(7):801813.

<!-- b000395 | references | pages [23] -->
[6] Guan Zhongwei Design and theoretical basis of lactic acid tolerance training for 400m sec-

<!-- b000396 | references | pages [23] -->
ondary athletes . Journal of Shanghai Institute of Physical Education, 2001(S1):142-144.

<!-- b000397 | references | pages [23] -->
[7] Wang Guiying A study on the main physical ﬁtness indicators and evaluation standards of

<!-- b000398 | references | pages [23] -->
Chinese men’s 400-meter athletes . Journal of Ezhou University, 2007, 14(2): 69-72.

<!-- b000399 | references | pages [23] -->
[8] Rainer Pivit Drag Force Formulas . Radfahren 2/1990, pp. 44 46

<!-- b000400 | references | pages [23] -->
[9] Tom Bell Could Critical Power be a better alternative to FTP for training?. Published: July

<!-- b000401 | references | pages [23] -->
15, 2021

<!-- b000402 | references | pages [23] -->
[10] Ji Jianmin, Cai Dapeng Eﬀects of temperature and humidity on the training eﬀect of male

<!-- b000403 | references | pages [23] -->
canoeists. Journal of Shenyang Institute of Physical Education, 2011, 30(03): 68-71.

<!-- b000404 | references | pages [23] -->
[11] Steve Westlake Are You Faster When It Rains.1 MAR 2016

<!-- b000405 | references | pages [23] -->
[12] Bert Blocken, Yasin Toparlar, Thijs van Druenen, Thomas AndrianneAerodynamic drag in

<!-- b000406 | references | pages [23] -->
cycling team time trials. Journal of Wind Engineering & Industrial Aerodynamics 182 (2018)

<!-- b000407 | references | pages [23] -->
128145

<!-- b000408 | references | pages [24] -->
with our mathematical

<!-- b000409 | references | pages [24] -->
optimization model

<!-- b000410 | references | pages [24] -->
Dear Directeur Sportif,

<!-- b000411 | references | pages [24] -->
It’s our honor to show you the results of model——a system called RIDERMAN to you. RIDERMAN is a

<!-- b000412 | references | pages [24] -->
mathematical optimization system that can give effective strategies in rider’s races. “As a mathematician you’re

<!-- b000413 | references | pages [24] -->
used to solving problems on your own, so that’s the way I approach cycling,” said by Anna van der Breggen,

<!-- b000414 | references | pages [24] -->
Women’s Individual Time Trial champion at the 2021 Tokyo Olympics. Anna holds a PhD in mathematics from

<!-- b000415 | references | pages [24] -->
Cambridge University and is a mathematician. To some extent, her victory shows the importance of mathematical

<!-- b000416 | references | pages [24] -->
optimization in sports competitions.

<!-- b000417 | references | pages [24] -->
Through the steps of dynamic modeling, subsection analysis, nonlinear programming solution and so on, a

<!-- b000418 | references | pages [24] -->
system of optimal power output strategy can be solved according to the information of the track and the players.

<!-- b000419 | references | pages [24] -->
We applied it to the Tokyo Olympic track, the Belgian UCI track, and a home-made track, and showed that even

<!-- b000420 | references | pages [24] -->
moderately fit athletes could achieve near-world championship times using the power output strategy given by

<!-- b000421 | references | pages [24] -->
our model.

<!-- b000422 | references | pages [24] -->
Next, we will explain RIDERMEN, a system based on track information and player data to a rider, and put

<!-- b000423 | references | pages [24] -->
forward some suggestions according to our mathematical optimization model.

<!-- b000424 | references | pages [24] -->
Dear rider, l am RIDERMAN—— your little helper on

<!-- b000425 | references | pages [24] -->
the road. Allow me to ask you one question first.

<!-- b000426 | references | pages [24] -->
Are you a time trial specialist or a sprinter?

<!-- b000427 | references | pages [24] -->
If you are a time trial specialist or a rouleur,

<!-- b000428 | references | pages [24] -->
WATCH THIS

<!-- b000429 | references | pages [24] -->
RIDERMAN has prepared unique strategies for

<!-- b000430 | references | pages [24] -->
you to take the crown.

<!-- b000431 | references | pages [24] -->
First of all, for a particular track:

<!-- b000432 | references | pages [24] -->
Let us divide the road sections into turns as nodes

<!-- b000433 | references | pages [24] -->
and determine the type of road sections according

<!-- b000434 | references | pages [24] -->
to the following criteria. (U for up, D for down)

<!-- b000435 | references | pages [24] -->
Straight type comparison table

<!-- b000436 | references | pages [24] -->
Slope

<!-- b000437 | references | pages [24] -->
0~2°

<!-- b000438 | references | pages [24] -->
2°~4°

<!-- b000439 | references | pages [24] -->
4°~6°

<!-- b000440 | references | pages [24] -->
Road type

<!-- b000441 | references | pages [24] -->
Flat ground

<!-- b000442 | references | pages [24] -->
U4/D4

<!-- b000443 | references | pages [24] -->
U6/D6

<!-- b000444 | references | pages [24] -->
(Tips: Your time trial experience will come in handy for

<!-- b000445 | references | pages [24] -->
sections beyond the descriptions of the above labels.)

<!-- b000446 | references | pages [24] -->
Now, let us take a look at what Strategies

<!-- b000447 | references | pages [24] -->
RIDEMAN have prepared for you to deal with

<!-- b000448 | references | pages [24] -->
different road types.

<!-- b000449 | references | pages [24] -->
① For a track with more than 90% of the

<!-- b000450 | references | pages [24] -->
road sections on flat ground:

<!-- b000451 | references | pages [24] -->
Trying to distribute the energy evenly during

<!-- b000452 | references | pages [24] -->
the ride is the best solution.

<!-- b000453 | references | pages [24] -->
(RIDEMAN have drawn power curve and

<!-- b000454 | references | pages [24] -->
power-speed conversion curve below for you

<!-- b000455 | references | pages [24] -->
to determine the actual and appropriate average

<!-- b000456 | references | pages [24] -->
output power expected to accomplish.)

<!-- b000457 | references | pages [24] -->
Power-Speed

<!-- b000458 | references | pages [24] -->
Power Curve

<!-- b000459 | references | pages [24] -->
Conversion Curve

<!-- b000460 | references | pages [25] -->
②: For multi-ramp tracks:

<!-- b000461 | references | pages [25] -->
RIDERMAN has prepared a corresponding

<!-- b000462 | references | pages [25] -->
strategy for each type of ramp:

<!-- b000463 | references | pages [25] -->
U4-type Uphill: maintain or slightly increase

<!-- b000464 | references | pages [25] -->
the power passing of the original flat ground,

<!-- b000465 | references | pages [25] -->
you can save physical energy consumption

<!-- b000466 | references | pages [25] -->
under the condition of less speed loss

<!-- b000467 | references | pages [25] -->
U6-type Uphill: the output power can be

<!-- b000468 | references | pages [25] -->
temporarily increased by 8%-10% of the

<!-- b000469 | references | pages [25] -->
leveling power, so as to reduce the acceleration

<!-- b000470 | references | pages [25] -->
and deceleration time before and after passing

<!-- b000471 | references | pages [25] -->
through the curve.

<!-- b000472 | references | pages [25] -->
D4-type Downhill: the output power can be

<!-- b000473 | references | pages [25] -->
reduced by about 24%.

<!-- b000474 | references | pages [25] -->
D6-type Downhill: the output power can be

<!-- b000475 | references | pages [25] -->
reduced by about 30%.

<!-- b000476 | references | pages [25] -->
Now it is time for the sprinter to show.

<!-- b000477 | references | pages [25] -->
If you're a sprinter professional but have a heart

<!-- b000478 | references | pages [25] -->
for being at the top of the time trial,

<!-- b000479 | references | pages [25] -->
WATCH THIS

<!-- b000480 | references | pages [25] -->
RIDERMAN has specially prepared a different

<!-- b000481 | references | pages [25] -->
strategy package for you to better adapt to the

<!-- b000482 | references | pages [25] -->
race and stand out in the time trial.

<!-- b000483 | references | pages [25] -->
First of all, for a particular track:

<!-- b000484 | references | pages [25] -->
Let us divide the road sections like a specialist,

<!-- b000485 | references | pages [25] -->
but according to a different criteria. (U for up,

<!-- b000486 | references | pages [25] -->
D for down)

<!-- b000487 | references | pages [25] -->
Straight type comparison table

<!-- b000488 | references | pages [25] -->
Slope

<!-- b000489 | references | pages [25] -->
0~1°

<!-- b000490 | references | pages [25] -->
1°~2°

<!-- b000491 | references | pages [25] -->
Road type

<!-- b000492 | references | pages [25] -->
Flat ground

<!-- b000493 | references | pages [25] -->
U2/D2

<!-- b000494 | references | pages [25] -->
Straight type comparison table

<!-- b000495 | references | pages [25] -->
Slope

<!-- b000496 | references | pages [25] -->
2°~4°

<!-- b000497 | references | pages [25] -->
4°~6°

<!-- b000498 | references | pages [25] -->
>6°

<!-- b000499 | references | pages [25] -->
Road type

<!-- b000500 | references | pages [25] -->
U4/D4

<!-- b000501 | references | pages [25] -->
U6/D6

<!-- b000502 | references | pages [25] -->
UM/DM

<!-- b000503 | references | pages [25] -->
①: For a track with more than 85% of the road

<!-- b000504 | references | pages [25] -->
sections on flat ground：

<!-- b000505 | references | pages [25] -->
Trying to distribute the energy evenly during the

<!-- b000506 | references | pages [25] -->
ride is the best solution.

<!-- b000507 | references | pages [25] -->
(RIDERMAN also draws power curve and

<!-- b000508 | references | pages [25] -->
power-speed conversion curve based on

<!-- b000509 | references | pages [25] -->
sprinters’ average level for you to determine

<!-- b000510 | references | pages [25] -->
the actual and appropriate average output power

<!-- b000511 | references | pages [25] -->
expected to accomplish.)

<!-- b000512 | references | pages [25] -->
Power-Speed

<!-- b000513 | references | pages [25] -->
Power Curve

<!-- b000514 | references | pages [25] -->
Conversion Curve

<!-- b000515 | references | pages [25] -->
②: For multi-ramp tracks:

<!-- b000516 | references | pages [25] -->
RIDERMAN also prepares different corresponding

<!-- b000517 | references | pages [25] -->
strategies for each type of ramp (use the charac-

<!-- b000518 | references | pages [25] -->
teristics of sprinters to accelerate/decelerate

<!-- b000519 | references | pages [25] -->
quickly and easily connect different states to reduce

<!-- b000520 | references | pages [25] -->
the loss of climbing.):

<!-- b000521 | references | pages [25] -->
Ramp

<!-- b000522 | references | pages [25] -->
Stratigy

<!-- b000523 | references | pages [25] -->
U2/U4-type Uphill increased the output power

<!-- b000524 | references | pages [25] -->
(about 3%)

<!-- b000525 | references | pages [25] -->
increased the output power by

<!-- b000526 | references | pages [25] -->
U6-type Uphill

<!-- b000527 | references | pages [25] -->
5%-8% of the leveling power

<!-- b000528 | references | pages [25] -->
UM-type

<!-- b000529 | references | pages [25] -->
reduce the speed to about 60%

<!-- b000530 | references | pages [25] -->
D4/D6/DM-type

<!-- b000531 | references | pages [25] -->
decreased the output power by

<!-- b000532 | references | pages [25] -->
Downhill

<!-- b000533 | references | pages [25] -->
about 24%/30%/50%

<!-- b000534 | references | pages [25] -->
Next, considering that the time-trial cornering strategy is

<!-- b000535 | references | pages [25] -->
quite different from sprinting, RIDERMAN prepares an

<!-- b000536 | references | pages [25] -->
additional spreadsheet and calculation formula

<!-- b000537 | references | pages [25] -->
(

<!-- b000538 | references | pages [25] -->
)for you. It is

<!-- b000539 | references | pages [25] -->
recommended that you fill in the curve data and

<!-- b000540 | references | pages [25] -->
calculate the maximum cornering speed.

<!-- b000541 | references | pages [25] -->
Turning Statistics

<!-- b000542 | references | pages [25] -->
Inner

<!-- b000543 | references | pages [25] -->
Turning

<!-- b000544 | references | pages [25] -->
Number

<!-- b000545 | references | pages [25] -->
Slope(deg)

<!-- b000546 | references | pages [25] -->
diameter(m)

<!-- b000547 | references | pages [25] -->
angle(deg)

<!-- b000548 | references | pages [25] -->
RIDERMAN wish you good luck in the time

<!-- b000549 | references | pages [25] -->
trial,don’t forget to flexibility according to the

<!-- b000550 | references | pages [25] -->
actual situation.

<!-- b000551 | references | pages [25] -->
Thank you for reading, you can print it or send it to the team members by

<!-- b000552 | references | pages [25] -->
email. You can also focus on the guidance during training to improve the

<!-- b000553 | references | pages [25] -->
efficiency and purpose of training.

<!-- b000554 | references | pages [25] -->
Best of luck to your team in the upcoming time trial.

<!-- b000555 | references | pages [25] -->
Yours Sincerely，

<!-- b000556 | furniture | pages [25] -->
Team #2207343
