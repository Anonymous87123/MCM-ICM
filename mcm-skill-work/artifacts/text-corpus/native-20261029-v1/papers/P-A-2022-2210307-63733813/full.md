# P-A-2022-2210307-63733813

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
2210307

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Power Planning Model: Magic Weapon for Cyclists

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In the time trial, many factors will aﬀect the rider’s performance. To help riders achieve better results, we need to establish a model that can comprehensively consider many factors and provide a reasonable power distribution plan at diﬀerent course positions.

<!-- b000011 | prose | pages [1] -->
First, we established a Rider Ability Evaluation Model and deﬁned the rider’s power proﬁle. A power-time scatterplot is drawn from the relationship between power and the maximum duration at this power level. Then four diﬀerent exercise intensity domains were divided according to the power-time relationship. We selected the 3P-CP Model to ﬁt the scatter plot, and obtained the rider’s power-time curve, thereby obtaining the three important rider ability indicators: Maximum instantaneous power (Pmax), critical power (CP) and anaerobic energy reserve (W ′). We take multiple sets of data to evaluate the ﬁtting results. After calculation, the ﬁtting degree is stable at about 0.86, indicating good ﬁtting eﬀect.

<!-- b000012 | prose | pages [1] -->
Secondly, we built an External Factor Analysis Model to identify the potential impact of external conditions. We quantitatively evaluated the inﬂuence of weather and environment from two aspects, namely road rolling resistance and wind resistance. After that, we select actual courses for veriﬁcation and the degree of compliance exceeds 90%.

<!-- b000013 | prose | pages [1] -->
Thirdly, Power Overall Planning Model is established. After the course segmentation and dynamics analysis, the average power (AP) and normalized power (NP) are proposed, and the constraints of the power of each track are obtained, so that the problem can be transformed into a multivariate nonlinear programming problem with total time t as objective function. We use gradient descent method to gradually approach the local minimum of t and give a power distribution plan for each road section. The deviation between our results and the actual is +-10%, indicating a good agreement with the actual.

<!-- b000014 | prose | pages [1] -->
Next, we apply the Rider Apability Evaluation Model to diﬀerent types of riders and courses, and obtained the riders output power, speed at a speciﬁc position and minimum time to complete the race.

<!-- b000015 | heading | pages [1] -->
Afterwards, we performed sensitivity analysis of the model, analyzing its robustness to

<!-- b000016 | prose | pages [1] -->
weather and environment and rider performance. The failure probabilities of air temperature, air pressure, altitude, and wind resistance are 0.18%, 3.97%, 0.18%, and 4.22% respectively. Air pressure and wind resistance are sensitive factors, while temperature and altitude are non-sensitive factors. We calculate the probability of failure caused by the deviation from power plan, and give the priority order of strategy execution: slope > corner > ﬂat.

<!-- b000017 | prose | pages [1] -->
Finally, we extend the model to a Team Time-Trial Power Distribution Model, and obtain the extended multivariate nonlinear programming problem. Our suggestion is: the ﬁrst 45% of the course are led by two riders with strong explosive strength, the last 15% are led by the rider with the strongest stamina, and the remaining 4 riders take turns leading in the middle.

<!-- b000018 | keywords | pages [1] -->
Keywords: Time trial, Power overall planning, Multivariate nonlinear programming

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1

<!-- b000021 | heading | pages [2] -->
Introduction

<!-- b000022 | prose | pages [2] -->
3 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000023 | prose | pages [2] -->
2

<!-- b000024 | heading | pages [2] -->
Assumptions and Justiﬁcation

<!-- b000025 | prose | pages [2] -->
3

<!-- b000026 | heading | pages [2] -->
Notations

<!-- b000027 | prose | pages [2] -->
4

<!-- b000028 | heading | pages [2] -->
Model Preparation

<!-- b000029 | prose | pages [2] -->
3

<!-- b000030 | prose | pages [2] -->
4

<!-- b000031 | prose | pages [2] -->
4

<!-- b000032 | prose | pages [2] -->
4 Explanation of Nouns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Data Preparation

<!-- b000033 | prose | pages [2] -->
5

<!-- b000034 | heading | pages [2] -->
Power Overall Planning Model

<!-- b000035 | prose | pages [2] -->
6

<!-- b000036 | prose | pages [2] -->
7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Model Overview 7 Sub-Model 1: Rider Ability Evaluation Model . . . . . . . . . . . . . . . . . . 5.2 7 Overview of sub-model 1 . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 7 Exercise intensity domain division . . . . . . . . . . . . . . . . . . . . 5.2.2 7 Three-parameter critical power model . . . . . . . . . . . . . . . . . . 5.2.3 8 Evaluation of ﬁtting result . . . . . . . . . . . . . . . . . . . . . . . . 5.2.4 9 Sub-Model 2: External Factors Analysis Model . . . . . . . . . . . . . . . . . 5.3 9 Weather and environmental factors . . . . . . . . . . . . . . . . . . . . 5.3.1 9 Time trial course factors . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.2 11 Establish the Power Overall Planning Model . . . . . . . . . . . . . . . . . . . 5.4 12 Dynamic analysis on the course 5.4.1 . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | prose | pages [2] -->
12 Power output evaluation throughout the race . . . . . . . . . . . . . . . 5.4.2 13 Multivariate nonlinear programming . . . . . . . . . . . . . . . . . . . 5.4.3 13 Model Solving and Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5 14 Model Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5.1 14 Model Solution Method Evaluation 5.5.2 . . . . . . . . . . . . . . . . . . .

<!-- b000038 | prose | pages [2] -->
15

<!-- b000039 | heading | pages [2] -->
Application of the Model: Rider and Course

<!-- b000040 | prose | pages [2] -->
6 6.1 Rider: Diﬀerent Gender and Type 15 . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | prose | pages [2] -->
15 Course: Three Time Trial Courses . . . . . . . . . . . . . . . . . . . . . . . . 6.2 15 Self designed course . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.1

<!-- b000042 | prose | pages [2] -->
7

<!-- b000043 | heading | pages [2] -->
Model Sensitivity Analysis

<!-- b000044 | prose | pages [2] -->
19

<!-- b000045 | prose | pages [2] -->
20 Sensitivity to Weather and Environment . . . . . . . . . . . . . . . . . . . . . 7.1 20 Sensitivity to Deviations from Target Power . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000046 | prose | pages [2] -->
8

<!-- b000047 | heading | pages [2] -->
Model Extension to Team Time Trial

<!-- b000048 | prose | pages [2] -->
9

<!-- b000049 | heading | pages [2] -->
Strength and Weakness

<!-- b000050 | prose | pages [2] -->
21

<!-- b000051 | prose | pages [2] -->
21

<!-- b000052 | prose | pages [2] -->
22 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 22 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2

<!-- b000053 | prose | pages [2] -->
Reference

<!-- b000054 | prose | pages [2] -->
22

<!-- b000055 | prose | pages [2] -->
23

<!-- b000056 | prose | pages [2] -->
2 2

<!-- b000057 | furniture | pages [3] -->
Team # 2210307

<!-- b000058 | furniture | pages [3] -->
Page 3

<!-- b000059 | prose | pages [3] -->
1

<!-- b000060 | heading | pages [3] -->
Introduction

<!-- b000061 | prose | pages [3] -->
1.1

<!-- b000062 | heading | pages [3] -->
Background

<!-- b000063 | prose | pages [3] -->
"Higher, faster, stronger - more united" is the Olympic motto and the goal of every athlete. In order to show the spirit of hard work and enterprising, athletes try to achieve better results. However, many factors aﬀect a rider’s performance, including the type of event, the course and the ability of the riders. In order to help these riders to respond to diﬀerent situations and achieve better results, we are required to formulate reasonable plans.

<!-- b000064 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000065 | prose | pages [3] -->
1) In order to determine the relationship between the riders position on the course and the power the rider applies, we set up a model which can be applied to any type of riders and race courses.

<!-- b000066 | prose | pages [3] -->
2) Deﬁne the power proﬁles of 2 types of riders of diﬀerent genders.

<!-- b000067 | prose | pages [3] -->
3) Apply our model to various time trial courses, and design our own time trial course.

<!-- b000068 | prose | pages [3] -->
4) Determine the sensitivity of our model to weather and environment and deviations from target power.

<!-- b000069 | prose | pages [3] -->
5) Extend our model, use it for a team.

<!-- b000070 | prose | pages [3] -->
1.3 Our Work

<!-- b000071 | prose | pages [3] -->
• For question 1), we intend to propose a model to measure the diﬀerence between diﬀerent types of riders, segment the course and generalize it into several characteristics. We can calculate the parameters by ﬁtting a curve with discrete points. We need to do dynamic analysis on diﬀerent courses. For the overall planning of power distribution, multivariate nonlinear programming method can be tried. Finally, the best plan of power distribution is obtained after the information of the rider, environment, track, etc. is known.

<!-- b000072 | prose | pages [3] -->
• For question 2), which is the model application to diﬀerent types of riders. We measure the ability values of diﬀerent riders in various aspects and substitute them into the model.

<!-- b000073 | prose | pages [3] -->
• For problem 3), which is the model application to diﬀerent courses, we need to control the variables to derive three diﬀerent power distributions using the same player and three sets of known course information.

<!-- b000074 | prose | pages [3] -->
• For questions 4) and 5), both questions are sensitivity analyses. We calculate the failure probabilities of diﬀerent variables and measure the sensitivity based on the idea of simulating importance sampling with subsets.

<!-- b000075 | prose | pages [3] -->
• For problem 6), we need to ﬁnd the similarities and diﬀerences between the team race and the individual race, and discuss how to give an optimal team strategy.

<!-- b000076 | furniture | pages [4] -->
Team # 2210307

<!-- b000077 | furniture | pages [4] -->
Page 4

<!-- b000078 | heading | pages [4] -->
Assumptions and Justiﬁcation

<!-- b000079 | prose | pages [4] -->
2

<!-- b000080 | prose | pages [4] -->
In order to make better use of the data about both the riders and courses, and improve the validity of the model, we propose the following reasonable assumptions:

<!-- b000081 | prose | pages [4] -->
• Safety comes ﬁrst.The physical health and safety of athletes is the premise of everything. We assume that riders have speed, energy and rage upper limits to prevent our model from putting them in a dangerous overdraft state.

<!-- b000082 | prose | pages [4] -->
• The inﬂuence of secondary factors is negligible. Since race results are aﬀected by so many factors while our model mainly focuses on diﬀerent types of riders, it is necessary to ignore the inﬂuence from secondary factors such as riders’ equipment.

<!-- b000083 | prose | pages [4] -->
• We divide the whole course into n sections, and each section belongs to one of the following four types: ﬂat, uphill, downhill, and sharp corner.The standard of segmen- tation is: when the continuous change of slope does not exceed 1%, it is deﬁned as the same segment of ﬂat ground; when the radius of curvature exceeds 40m, it is considered as a straight road; when it is less than 40m and the radius changes not more than 5m, it is deﬁned as the same corner.

<!-- b000084 | prose | pages [4] -->
• All participants have sportsmanship, maintain the fairness of the game, and can play their best in the game.

<!-- b000085 | prose | pages [4] -->
3

<!-- b000086 | heading | pages [4] -->
Notations

<!-- b000087 | heading | pages [4] -->
Symbols

<!-- b000088 | prose | pages [4] -->
Description

<!-- b000089 | prose | pages [4] -->
e

<!-- b000090 | prose | pages [4] -->
Value/Unit

<!-- b000091 | prose | pages [4] -->
e = 2.178 Basis of the natural logarithm

<!-- b000092 | prose | pages [4] -->
R Gas constant

<!-- b000093 | prose | pages [4] -->
g

<!-- b000094 | prose | pages [4] -->
8.31Jmol−1K−1

<!-- b000095 | prose | pages [4] -->
g=9.8m/s2 Gravitational acceleration

<!-- b000096 | prose | pages [4] -->
CP Critical power

<!-- b000097 | prose | pages [4] -->
MMP

<!-- b000098 | prose | pages [4] -->
watt

<!-- b000099 | prose | pages [4] -->
watt Mean maximal power output

<!-- b000100 | prose | pages [4] -->
W ′ Anaerobic capacity

<!-- b000101 | prose | pages [4] -->
ρ Air density

<!-- b000102 | prose | pages [4] -->
kr

<!-- b000103 | prose | pages [4] -->
J

<!-- b000104 | prose | pages [4] -->
g/L

<!-- b000105 | prose | pages [4] -->
Rolling resistance coeﬃcient

<!-- b000106 | prose | pages [4] -->
cd Wind resistance coeﬃcient

<!-- b000107 | prose | pages [4] -->
S Windward area

<!-- b000108 | prose | pages [4] -->
4

<!-- b000109 | heading | pages [4] -->
Model Preparation

<!-- b000110 | prose | pages [4] -->
m2

<!-- b000111 | prose | pages [4] -->
To make our paper clearer and easier to understand, we will explain some nouns, data types, and data sources in this section.

<!-- b000112 | furniture | pages [5] -->
Team # 2210307

<!-- b000113 | furniture | pages [5] -->
Page 5

<!-- b000114 | prose | pages [5] -->
4.1 Explanation of Nouns

<!-- b000115 | prose | pages [5] -->
• Normalized power output(NP) It takes the diﬀerence between steady and wave workouts into account. NP is better at quantifying the physiological "cost" of the harder "feeling" of variable eﬀort. For a highly variable workout, NP can be much higher than average power(AP), when for a very steady workout, NP and AP are almost equivalent. A relatively high NP indicates that the exercise has large ﬂuctuations and is physiologically more diﬃcult than the average power would represent.

<!-- b000116 | prose | pages [5] -->
• Average power output(AP) A rider’s average power output is the ratio of the total energy expended to the time spent completing a long race. The calculation method of AP is given below:

<!-- b000117 | prose | pages [5] -->
AP = total energy

<!-- b000118 | prose | pages [5] -->
(1) total time

<!-- b000119 | prose | pages [5] -->
• Mean maximal power output(MMP) MMP is the amount of power a rider can produce for a given time eﬀort. For example, the highest average power output recorded over a 5-minute duration is the 5−minuteMMP. Such MMP data are valuable because they can identify the energy output and duration a rider needs to produce.

<!-- b000120 | prose | pages [5] -->
• Anaerobic capacity(W ′) W ′ represents work capacity above critical power.

<!-- b000121 | prose | pages [5] -->
• Critical power(CP)

<!-- b000122 | caption | pages [5] -->
Figure 1: The relationship between W ′ & CP. The red curve is the critical power curve.

<!-- b000123 | prose | pages [5] -->
CP is the lower limit (or horizontal asymptote) of power curve.

<!-- b000124 | prose | pages [5] -->
It is a physiologi- cal threshold that divides metabolic sustainable eﬀort and unsustainable eﬀort during exercise.

<!-- b000125 | prose | pages [5] -->
• Maximum instantaneous output power(Pmax) Pmax is the peak power over 1 second, which indicates the rider’s explosive strength.

<!-- b000126 | prose | pages [5] -->
• VO2max(V O2max) V O2max refers to the amount of oxygen that the body can take in during maximum

<!-- b000127 | furniture | pages [6] -->
Team # 2210307

<!-- b000128 | furniture | pages [6] -->
Page 6

<!-- b000129 | prose | pages [6] -->
intensity exercise. Since oxygen is the basis of many substance metabolism and energy metabolism activities in the body, V O2max is an important measure of rider stamina, reﬂecting the body’s aerobic exercise capacity.

<!-- b000130 | caption | pages [6] -->
Figure 2: Several thresholds reached by the rider in the process of energy consumption. As can

<!-- b000131 | prose | pages [6] -->
be seen from the ﬁgure, the rider will arrive lactate threshold, critical power, VO2max in turn in the process of energy consumption.

<!-- b000132 | prose | pages [6] -->
4.2

<!-- b000133 | heading | pages [6] -->
Data Preparation

<!-- b000134 | prose | pages [6] -->
• Course conditions We found all the data we needed from the websites[1][2], along with the corresponding weather and environmental conditions.

<!-- b000135 | prose | pages [6] -->
• Rider type The riders are divided into ﬁve types as is given from the problem, namely time trial specialist, climber, sprinter, rouleur, and puncheur. We brieﬂy describe the ﬁve types of riders and summarize their characteristics, as shown in Table 1.

<!-- b000136 | caption | pages [6] -->
Table 1: Description and Characteristics of Five Types of Riders

<!-- b000137 | prose | pages [6] -->
Type of Rider Description

<!-- b000138 | prose | pages [6] -->
An experienced and capable time trial rider. Large lactate threshold, great muscle endurance, generally large FTP value,

<!-- b000139 | prose | pages [6] -->
Time trial specialist

<!-- b000140 | prose | pages [6] -->
great at maximizing the utilization of physical energy (physical ﬁtness assessment and allocation), and great endurance.

<!-- b000141 | prose | pages [6] -->
Riders specialize in long hill race. Climber Light weight, great endurance and limb strength.

<!-- b000142 | prose | pages [6] -->
Riders who specialize in producing extreme power in a short amount of time. Sprinter High explosive power, low endurance.

<!-- b000143 | prose | pages [6] -->
All-rounder for a variety of terrains. Rouleur Various indicators are relatively balanced, but not the top.

<!-- b000144 | prose | pages [6] -->
Riders who specialize in races including many short, steep climbs or sharp accelerations.

<!-- b000145 | prose | pages [6] -->
Puncheur

<!-- b000146 | prose | pages [6] -->
Heavy weight, strong leg strength, strong endurance, moderate explosive power, low waist strength.

<!-- b000147 | prose | pages [6] -->
The more power a rider produces, the less time the rider can maintain that power before having to recover. We use the tmaintain-p image to describe this physical diﬀerence of riders.

<!-- b000148 | furniture | pages [7] -->
Team # 2210307

<!-- b000149 | furniture | pages [7] -->
Page 7

<!-- b000150 | caption | pages [7] -->
Figure 3: Time to exhaustion(t −maintain in the ﬁgure) under diﬀerent power level(P in the

<!-- b000151 | prose | pages [7] -->
ﬁgure). P is the sustained level of power to the pedals. T −maintain is the time a rider takes to consume all his energy while maintaining his current power level.

<!-- b000152 | prose | pages [7] -->
• Power curve Riders are asked to do 3-5 full-power outputs of diﬀerent durations and record the riders’ power. The recovery between each full output should be set to at least 1 hour to ensure that the rider is getting enough recovery time. As an example, we got a scatterplot of the rider’s MMP for diﬀerent durations of full power output.The purpose of this is to perform ﬁtting and regression analysis on metrics such as critical power (CP).

<!-- b000153 | prose | pages [7] -->
5

<!-- b000154 | heading | pages [7] -->
Power Overall Planning Model

<!-- b000155 | prose | pages [7] -->
5.1

<!-- b000156 | heading | pages [7] -->
Model Overview

<!-- b000157 | prose | pages [7] -->
The rider ability and other external factors (including road conditions, weather conditions, etc.) are model’s input parameters, and rider’s power output in diﬀerent road sections as the output parameters. The model helps the rider to ride the course using a least amount of time, we need two steps. Step 1: Evaluate a rider ’s ability, using our Rider Ability Evaluation Model. Step 2: Segment the course, classify diﬀerent road sections, and analyze each of them. Then the relationship between the power and the time of each road section that aﬀects the rider’s ﬁnal performance is obtained.

<!-- b000158 | prose | pages [7] -->
5.2

<!-- b000159 | heading | pages [7] -->
Sub-Model 1: Rider Ability Evaluation Model

<!-- b000160 | prose | pages [7] -->
5.2.1

<!-- b000161 | heading | pages [7] -->
Overview of sub-model 1

<!-- b000162 | prose | pages [7] -->
We use power as our primary measure of rider ability. Through multiple tests of diﬀerent durations, a scatter plot describing the relationship of a rider’s maximum sustained power and maximum duration can be drawn, which we consider ﬁtting to a smooth curve. Why can the ﬁtted curve be smooth? Due to the continuous series of physiological responses in our body, the power-duration curve is inherently smooth. Since only a part of the ﬁtted curve is in good agreement with the actual situation, we conduct the exercise intensity domain division to clearly describe which part of the curve is closer to the actual situation.

<!-- b000163 | prose | pages [7] -->
5.2.2 Exercise intensity domain division

<!-- b000164 | prose | pages [7] -->
According to Burnley and Jones’ study in 2007[4],from a physiological perspective, the power-duration relationship is comprised of four distinct exercise intensity domains, namely,

<!-- b000165 | furniture | pages [8] -->
Team # 2210307

<!-- b000166 | furniture | pages [8] -->
Page 8

<!-- b000167 | prose | pages [8] -->
moderate, heavy, severe, and extreme. The basis for this division is that, for each exercise intensity domain, its power-duration curve has a relatively obvious diﬀerence.

<!-- b000168 | caption | pages [8] -->
Figure 4: Rider’s power output throughout the race.

<!-- b000169 | prose | pages [8] -->
In the ﬁgure, four exercise intensity domains are divided according to the power output and represented by diﬀerent colors.

<!-- b000170 | prose | pages [8] -->
5.2.3

<!-- b000171 | heading | pages [8] -->
Three-parameter critical power model

<!-- b000172 | prose | pages [8] -->
We choose the three-parameter critical power model as the Rider Ability Evaluation Model. In a paper by Peter Leo [3], ﬁve models describing the power-time relationship were compared, in which the 3-P CP model’s (Three-parameter critical power model) results in severe and extreme exercise intensity domains best match the actual situation. Thus the power output in the severe and extreme exercise intensity domains is more important in predicting the rider performance, so we decided to use the 3-P CP model as the power-time relationship model to ﬁt the test data. From the ﬁtted curve we can obtain the power curve of the rider, as well as the rider ability indicators.

<!-- b000173 | caption | pages [8] -->
Table 2: Rider’s physiological and ability indicators

<!-- b000174 | prose | pages [8] -->
Ability type

<!-- b000175 | heading | pages [8] -->
Symbol

<!-- b000176 | prose | pages [8] -->
Description

<!-- b000177 | prose | pages [8] -->
Rider’s standing height, the unit is meter(m). h Body height

<!-- b000178 | prose | pages [8] -->
The unit is kilogram(kg). m Body weight

<!-- b000179 | prose | pages [8] -->
The mean maximal power (MMP) that a rider can output within a given 5s is used to measure the explosive strength of

<!-- b000180 | prose | pages [8] -->
Pmax Explosive strength

<!-- b000181 | prose | pages [8] -->
a rider, in watts.

<!-- b000182 | prose | pages [8] -->
We measure a rider’s stamina by anaerobic capacity, namely the W Stamina amount of energy stored without oxygen.

<!-- b000183 | prose | pages [8] -->
We use critical power(CP) to represent a rider’s oxygen uptake capacity, and CP represents the theoretical asymptote of power,

<!-- b000184 | prose | pages [8] -->
CP Oxygen uptake ability

<!-- b000185 | prose | pages [8] -->
indicating that a given power output is sustainable all the time.

<!-- b000186 | prose | pages [8] -->
The stronger the bike control ability, the higher the rider’s BC Bike control ability maximum speed and upper limit of aggression.

<!-- b000187 | prose | pages [8] -->
Predictive trials of less than 2 minutes do not guarantee V O2max (ie, they are not in the severe intensity range). Recent work proposes that CP better estimates maximal metabolic

<!-- b000188 | furniture | pages [9] -->
Team # 2210307

<!-- b000189 | furniture | pages [9] -->
Page 9

<!-- b000190 | prose | pages [9] -->
homeostasis, i.e. the highest power output at which oxygen uptake homeostasis (V O2) responses are observed despite increased blood lactate values.

<!-- b000191 | heading | pages [9] -->
Power-Time Relationship Model

<!-- b000192 | prose | pages [9] -->
The relationship between power and time is shown as the equation below:

<!-- b000193 | prose | pages [9] -->
W ′ t =

<!-- b000194 | prose | pages [9] -->
P −CP + W ′

<!-- b000195 | prose | pages [9] -->
(2)

<!-- b000196 | prose | pages [9] -->
CP −Pmax

<!-- b000197 | prose | pages [9] -->
where t is the duration; P is the maximum continuous power; W ′ is the anaerobic energy; CP is the critical power; Pmax is the maximum instantaneous power.

<!-- b000198 | prose | pages [9] -->
The ﬁtting of the model is achieved by using the ﬁtting tool for custom parameter functions in the MATLAB ﬁtting toolbox, and the ﬁtting result will be shown in the next part. In practice, if the actual conditions are not enough to obtain more power-time scatter values, the three parameters of the power-time curve can be measured by a simpliﬁed experiment, so that the power-time curve can also be obtained. CP can be measured by measuring the AP of the last 30s of a three-minute full-power output power curve, and Pmax can be obtained by measuring the average of the 5s full-power output power. After CP is measured, MMP and t can be obtained through a speciﬁc output power duration test. At this time, W ′ can be expressed by the following formula:

<!-- b000199 | prose | pages [9] -->
W ′ = (MMP −CP) × t (3)

<!-- b000200 | prose | pages [9] -->
It is worth noting that although it is simpler, the power-time curve measured by the above method will have a larger error than the ﬁtted result.

<!-- b000201 | prose | pages [9] -->
5.2.4

<!-- b000202 | heading | pages [9] -->
Evaluation of ﬁtting result

<!-- b000203 | prose | pages [9] -->
In order to evaluate the ﬁtting, we ﬁt a scatter plot drawn with data from multiple tests of an athlete, and the ﬁtting results are shown in Figure 5. The Goodness of Fit is 0.864, which is close to the perfect 1, so the ﬁtting is good and the model has practical signiﬁcance.

<!-- b000204 | caption | pages [9] -->
Figure 5: Curve ﬁtting of scatter plot

<!-- b000205 | prose | pages [9] -->
We can obtain the expression of the smooth curve after curve ﬁtting, and each parameter in the expression is the rider ability indicator.

<!-- b000206 | heading | pages [9] -->
Sub-Model 2: External Factors Analysis Model

<!-- b000207 | prose | pages [9] -->
5.3

<!-- b000208 | prose | pages [9] -->
5.3.1 Weather and environmental factors

<!-- b000209 | prose | pages [9] -->
The inﬂuence of weather and environment on the race is complex, as is shown in Figure 6:

<!-- b000210 | furniture | pages [10] -->
Team # 2210307

<!-- b000211 | furniture | pages [10] -->
Page 10

<!-- b000212 | caption | pages [10] -->
Figure 6: Road surface factors & Air resistance factors

<!-- b000213 | prose | pages [10] -->
The resistance to the rider mainly comes from the ground rolling resistance and wind resistance, and the rider often has to pay 40% of the full power to overcome these two resistances. Therefore, we consider the inﬂuence of weather and environmental factors from two aspects: road conditions and wind resistance.

<!-- b000214 | prose | pages [10] -->
• Road conditions The rolling resistance is mainly determined by the elastic force of the ground and the rolling resistance coeﬃcient, and its expression is:

<!-- b000215 | prose | pages [10] -->
Fr = kr × F (4)

<!-- b000216 | prose | pages [10] -->
where Fr is the rolling resistance, F is the elastic force of the ground, kr is the rolling resistance coeﬃcient which is related to the type of road surface, the tire structure, etc.

<!-- b000217 | prose | pages [10] -->
• Wind resistance

<!-- b000218 | prose | pages [10] -->
– Wind strength and wind direction. Wind resistance is the component of the wind

<!-- b000219 | prose | pages [10] -->
force in the riding direction generated during high-speed riding, which is mainly related to the wind speed and wind direction. When there is no wind, the formula for calculating wind resistance is:

<!-- b000220 | prose | pages [10] -->
Fw = 1

<!-- b000221 | prose | pages [10] -->
2 × cd × S × ρ × v2 (5)

<!-- b000222 | prose | pages [10] -->
where v is the riders speed, , cd is wind resistance coeﬃcient, S is the windward area. When there is wind, it is assumed that the wind speed and wind direction are ﬁxed in a short time, and the angle between the wind direction and the riding direction is θ. When the wind is used as the reference frame, the rider is in a state of no wind, and the speed of the rider(vr) is

<!-- b000223 | prose | pages [10] -->
vr = v −vw × cos θ (6)

<!-- b000224 | prose | pages [10] -->
where vw is the wind speed. Then the wind resistance is:

<!-- b000225 | prose | pages [10] -->
Fw = 1

<!-- b000226 | prose | pages [10] -->
2 2 × cd × S × ρ × vr (7)

<!-- b000227 | prose | pages [10] -->
Considering the direction of the wind, then wind resistance > 0(0◦< θ < 90◦), wind resistance < 0(90◦<< 180◦), then the ﬁnal wind resistance expression is:

<!-- b000228 | prose | pages [10] -->
2 × cd × S × ρ × vr3

<!-- b000229 | prose | pages [10] -->
Fw = 1

<!-- b000230 | prose | pages [10] -->
(8) |vr|

<!-- b000231 | furniture | pages [11] -->
Team # 2210307

<!-- b000232 | prose | pages [11] -->
– Air density Air density ρ

<!-- b000233 | furniture | pages [11] -->
Page 11

<!-- b000234 | prose | pages [11] -->
It is related to temperature and air pressure, and its calculation formula is:

<!-- b000235 | prose | pages [11] -->
ρ = pM

<!-- b000236 | prose | pages [11] -->
(9) RT

<!-- b000237 | prose | pages [11] -->
where p is the air pressure, M is the molar mass of the gas, R is the proportionality constant (a constant value for any ideal gas), and T is the air temperature. Since air pressure is often not easy to measure directly, we convert changes in air pressure into changes in elevation. Their relationship is as follows:

<!-- b000238 | prose | pages [11] -->
Hs = H0 + R

<!-- b000239 | prose | pages [11] -->
g × Tm × ln P0

<!-- b000240 | prose | pages [11] -->
(10)

<!-- b000241 | prose | pages [11] -->
Ps

<!-- b000242 | prose | pages [11] -->
where H0 is the altitude, Hs is the altitude of the standard isobaric surface, P0 is the air pressure on the ground, Ps is the average height of the air column, and R and g are constants.

<!-- b000243 | prose | pages [11] -->
– Wind resistance coeﬃcient The drag coeﬃcient is determined only by the rider’s

<!-- b000244 | prose | pages [11] -->
riding position. Based on the assumptions, we consider this parameter to remain unchanged. For cyclists, we consider cd = 0.23.

<!-- b000245 | prose | pages [11] -->
– Windward area According to Stevenson formula, the windward area is related to

<!-- b000246 | prose | pages [11] -->
height and weight, and the expression is:

<!-- b000247 | prose | pages [11] -->
{ 1

<!-- b000248 | prose | pages [11] -->
4(0.0057h + 0.0121m + 0.0882), male rider

<!-- b000249 | prose | pages [11] -->
maximum windward area =

<!-- b000250 | prose | pages [11] -->
1 4(0.0073h + 0.0127m −0.0099), female rider

<!-- b000251 | prose | pages [11] -->
5.3.2 Time trial course factors

<!-- b000252 | prose | pages [11] -->
(11)

<!-- b000253 | prose | pages [11] -->
Our model also needs to be applied to any type of courses. Therefore, in order to make the course can be quantitatively analyzed, we need to summarize their characteristics. Then we divide all the course sections into four types: corner, uphill, downhill, and ﬂat ground, as is shown in Figure 7.

<!-- b000254 | caption | pages [11] -->
Figure 7: Four types of course sections

<!-- b000255 | heading | pages [11] -->
Establish the Power Overall Planning Model

<!-- b000256 | prose | pages [11] -->
5.4

<!-- b000257 | prose | pages [11] -->
5.4.1 Dynamic analysis on the course

<!-- b000258 | prose | pages [11] -->
We use parameters to measure four types of course sections: ﬂat ground(parameter: distance, speed and power), uphill (parameters: distance, slope, speed and power), downhill (parameters:

<!-- b000259 | furniture | pages [12] -->
Team # 2210307

<!-- b000260 | furniture | pages [12] -->
Page 12

<!-- b000261 | prose | pages [12] -->
distance, slope, speed and power), corner (parameters: distance,radius of curvature, speed and power) and they are discussed separately below.

<!-- b000262 | prose | pages [12] -->
(a) Flat ground force diagram (c) Downhill force diagram (b) Uphill force diagram

<!-- b000263 | caption | pages [12] -->
Figure 8: Diagrams of four types of course sections

<!-- b000264 | prose | pages [12] -->
• Flat ground P = (Fw + Fr) × v

<!-- b000265 | prose | pages [12] -->
(12)

<!-- b000266 | prose | pages [12] -->
= mg × kr × v + 1

<!-- b000267 | prose | pages [12] -->
2 × cd × S × ρ × v3

<!-- b000268 | prose | pages [12] -->
where Fw is the wind resistance(aerodynamic drag in the ﬁgure), Fr is the rolling resistance.

<!-- b000269 | prose | pages [12] -->
• Uphill P = F × v

<!-- b000270 | prose | pages [12] -->
= (Fr + Fg + Fw) × V

<!-- b000271 | prose | pages [12] -->
(13)

<!-- b000272 | prose | pages [12] -->
= (kr × mg × cos θ + mg × sin θ) v + 1

<!-- b000273 | prose | pages [12] -->
2 × cd × S × ρ × v3

<!-- b000274 | prose | pages [12] -->
where Fg is the rider’s gravity(gravity in the ﬁgure), and angle θ > 0.

<!-- b000275 | prose | pages [12] -->
• Downhill We deﬁne a downhill as a road segment with a slope of more than 2%. Due to the similarity between downhill and uphill road sections, when going uphill, θ > 0 , and when going downhill, θ < 0. So only the uphill force formula is given here as the downhill force formula is similar.

<!-- b000276 | prose | pages [12] -->
• Corner 

<!-- b000277 | prose | pages [12] -->
(

<!-- b000278 | prose | pages [12] -->


<!-- b000279 | prose | pages [12] -->
P =

<!-- b000280 | prose | pages [12] -->
Fw +

<!-- b000281 | prose | pages [12] -->


<!-- b000282 | prose | pages [12] -->
)

<!-- b000283 | prose | pages [12] -->
√

<!-- b000284 | prose | pages [12] -->
F 2

<!-- b000285 | prose | pages [12] -->
r −F 2

<!-- b000286 | prose | pages [12] -->
× v

<!-- b000287 | prose | pages [12] -->
c

<!-- b000288 | prose | pages [12] -->
(14)

<!-- b000289 | prose | pages [12] -->
Fc = m × v2

<!-- b000290 | prose | pages [12] -->
 

<!-- b000291 | prose | pages [12] -->
where Fc is the centripetal force.

<!-- b000292 | prose | pages [12] -->
r

<!-- b000293 | prose | pages [12] -->
Power output evaluation throughout the race 5.4.2

<!-- b000294 | prose | pages [12] -->
When analyzing a rider’s performance in a race, we use the indicators shown in the table below to evaluate the rider’s overall power output during the race.

<!-- b000295 | furniture | pages [13] -->
Team # 2210307

<!-- b000296 | furniture | pages [13] -->
Page 13

<!-- b000297 | caption | pages [13] -->
Table 3: Rider’s physiological and ability indicators

<!-- b000298 | prose | pages [13] -->
Indicator

<!-- b000299 | heading | pages [13] -->
Symbol

<!-- b000300 | prose | pages [13] -->
Formula

<!-- b000301 | prose | pages [13] -->
[∑(P 4

<!-- b000302 | prose | pages [13] -->
i ×ti)

<!-- b000303 | prose | pages [13] -->
AP Average power

<!-- b000304 | prose | pages [13] -->
t

<!-- b000305 | prose | pages [13] -->
∑Pi×ti NP Normalized power

<!-- b000306 | prose | pages [13] -->
t

<!-- b000307 | prose | pages [13] -->
AP × t Wt Total work

<!-- b000308 | prose | pages [13] -->
NP × t Wn Normalized work

<!-- b000309 | prose | pages [13] -->
Maximum Pmax instantaneous power

<!-- b000310 | prose | pages [13] -->
Description

<!-- b000311 | prose | pages [13] -->
] 1 ] 1

<!-- b000312 | prose | pages [13] -->
Average power is the total work in the entire ride 4 4 divided by the total ride time, which has a strong correlation with speed and force.

<!-- b000313 | prose | pages [13] -->
The results obtained after smoothing the power points that are too low and too high, and increasing the proportion of the high power output section, describe the entire movement better than the average power.

<!-- b000314 | prose | pages [13] -->
The product of the average power and the total time. It is used to reﬂect only the work done when moving, and does not consider the extra work consumption caused by power changes.

<!-- b000315 | prose | pages [13] -->
Normalized work is the product of normalized power and total time, which is used to reﬂect the actual work done in the race, including the extra work consumption caused by power changes. Usually greater than the total work.

<!-- b000316 | prose | pages [13] -->
It reﬂects the upper limit of the output power of the rider in the race. This upper limit should not be too diﬀerent from the average power, otherwise the optimal situation will not be achieved due to the extra power consumption caused by the power change.

<!-- b000317 | prose | pages [13] -->
The disadvantage of the average power is that if the power ﬂuctuates greatly during the ride, the arithmetic average power is not enough to reﬂect the entire riding intensity. For example, whileAP of high-intensity sprint training is too low to reﬂect its high intensity, normalized power NP is better.

<!-- b000318 | prose | pages [13] -->
If a rider’s power output keeps changing during the race, he will consume additional work. Therefore, if it is not necessary to keep changing for reasons such as psychological strategy, we do not recommend that since it is not conducive to the rider’s good results.

<!-- b000319 | prose | pages [13] -->
5.4.3 Multivariate nonlinear programming

<!-- b000320 | prose | pages [13] -->
After the above analysis, our problem is transformed into a multivariate nonlinear program- ming problem, the objective function is the total time t, and t needs to be minimized. Its

<!-- b000321 | furniture | pages [14] -->
Team # 2210307

<!-- b000322 | prose | pages [14] -->
mathematical expression is:

<!-- b000323 | prose | pages [14] -->
n

<!-- b000324 | prose | pages [14] -->
n

<!-- b000325 | prose | pages [14] -->
∑

<!-- b000326 | prose | pages [14] -->
∑

<!-- b000327 | prose | pages [14] -->
mint =

<!-- b000328 | prose | pages [14] -->
ti =

<!-- b000329 | prose | pages [14] -->
i=1

<!-- b000330 | prose | pages [14] -->
i=1

<!-- b000331 | prose | pages [14] -->


<!-- b000332 | furniture | pages [14] -->
Page 14

<!-- b000333 | prose | pages [14] -->
di vi

<!-- b000334 | prose | pages [14] -->
1.15MMP (ti) > Pi > 0

<!-- b000335 | prose | pages [14] -->
   

<!-- b000336 | prose | pages [14] -->
NP ⩽MMP(t)

<!-- b000337 | prose | pages [14] -->
   

<!-- b000338 | prose | pages [14] -->
CP ⩽MMP(t)

<!-- b000339 | prose | pages [14] -->
  

<!-- b000340 | prose | pages [14] -->
(15)

<!-- b000341 | prose | pages [14] -->
1 MMP (ti) = CP +

<!-- b000342 | prose | pages [14] -->
S.t.

<!-- b000343 | prose | pages [14] -->
4√∑n

<!-- b000344 | prose | pages [14] -->
  

<!-- b000345 | prose | pages [14] -->
NP =

<!-- b000346 | prose | pages [14] -->
  

<!-- b000347 | prose | pages [14] -->
∑n

<!-- b000348 | prose | pages [14] -->
 

<!-- b000349 | prose | pages [14] -->
t 1 W ′ − CP −Pmax

<!-- b000350 | prose | pages [14] -->
i=1 P 4

<!-- b000351 | prose | pages [14] -->
i ti t t

<!-- b000352 | prose | pages [14] -->
i=1 Piti

<!-- b000353 | prose | pages [14] -->
AP =

<!-- b000354 | prose | pages [14] -->
 

<!-- b000355 | prose | pages [14] -->
t

<!-- b000356 | prose | pages [14] -->


<!-- b000357 | prose | pages [14] -->
Pi ⩾0, ti > 0

<!-- b000358 | prose | pages [14] -->
This problem is a typical multivariate nonlinear programming problem. The optimal output power Pi of each segment is solved to achieve the minimum total time min(t).

<!-- b000359 | prose | pages [14] -->
5.5

<!-- b000360 | heading | pages [14] -->
Model Solving and Evaluation

<!-- b000361 | prose | pages [14] -->
5.5.1

<!-- b000362 | heading | pages [14] -->
Model Solution

<!-- b000363 | prose | pages [14] -->
Since it is diﬃcult to ﬁnd the exact minimum solution for the multivariate nonlinear pro- gramming problem, we consider using the gradient descent method to gradually approach the local optimal solution to ﬁnd the optimal solution. After comparing multiple local optimal solutions, an approximate global optimal solution, that is, a better solution, can be obtained. It is solved by using the minimize function in python’s optimize toolbox.

<!-- b000364 | caption | pages [14] -->
Figure 9: Basic idea of the algorithm

<!-- b000365 | prose | pages [14] -->
It is worth noting that we cannot determine whether the next local optimum is what we are looking for, so we usually set a number of loops, and stop searching for the optimal solution after reaching the set number of times. The minimum value in the current most local minimum value is global optimal value.

<!-- b000366 | furniture | pages [15] -->
Team # 2210307

<!-- b000367 | prose | pages [15] -->
5.5.2

<!-- b000368 | heading | pages [15] -->
Model Solution Method Evaluation

<!-- b000369 | furniture | pages [15] -->
Page 15

<!-- b000370 | prose | pages [15] -->
The minimize function in python’s optimize toolbox gives a variety of methods for solv- ing multivariate nonlinear programming, including ’SLSQP’, ’Nelder-Mead’, ’Powell’ ’CG’ ’BFGS’, ’Newton-CG’, ’L-BFGS-B’, etc.

<!-- b000371 | prose | pages [15] -->
By comparing diﬀerent methods, we found that ’SLSQP’ solves faster, i.e. has less time complexity, so we choose the ’SLSQP’ method.

<!-- b000372 | heading | pages [15] -->
Application of the Model: Rider and Course

<!-- b000373 | prose | pages [15] -->
6

<!-- b000374 | prose | pages [15] -->
Rider: Diﬀerent Gender and Type 6.1

<!-- b000375 | caption | pages [15] -->
Figure 10: Radar diagram of the ability of four types of riders. The left diagram shows the six

<!-- b000376 | prose | pages [15] -->
abilities of time trial specialist and puncheur, diﬀerence between genders is shown in the central diagram, the right diagram indicates the ability of four types of riders.

<!-- b000377 | prose | pages [15] -->
Course: Three Time Trial Courses 6.2

<!-- b000378 | prose | pages [15] -->
For diﬀerent time trial courses, we adopt control variates when applying our model, that is, our model only studies the optimal power distribution strategy of the same rider when racing on diﬀerent courses. We also only looked at the course conditions of the womens individual time trial. And this rider’s information is given in Table 4.

<!-- b000379 | caption | pages [15] -->
Table 4: Rider’s information used for control variates

<!-- b000380 | heading | pages [15] -->
Explosive strength

<!-- b000381 | prose | pages [15] -->
Gender Height Weight

<!-- b000382 | prose | pages [15] -->
165cm 55kg Pmax =990W female

<!-- b000383 | prose | pages [15] -->
Stamina Oxygen uptake Bike control

<!-- b000384 | prose | pages [15] -->
W ′ =550J CP =230W 0.87

<!-- b000385 | heading | pages [15] -->
2021 Olympic Time Trial course in Tokyo, Japan

<!-- b000386 | prose | pages [15] -->
The time trial courses are exactly the same for the both the men’s and women’s races despite from the diﬀerent distances. And we analyze and segment the course from two aspects, namely corners and slopes. After calculating the data, the results can be obtained(Table 7).

<!-- b000387 | caption | pages [15] -->
Table 5: Course information

<!-- b000388 | prose | pages [15] -->
Average altitude Temperature Air pressure

<!-- b000389 | prose | pages [15] -->
15.7 ◦C 560m 0.96 atm

<!-- b000390 | prose | pages [15] -->
Wind direction

<!-- b000391 | heading | pages [15] -->
Wind strength

<!-- b000392 | prose | pages [15] -->
Air humidity

<!-- b000393 | prose | pages [15] -->
15◦west of north 7.5m/s 60%

<!-- b000394 | furniture | pages [16] -->
Team # 2210307

<!-- b000395 | furniture | pages [16] -->
Page 16

<!-- b000396 | caption | pages [16] -->
Table 6: Course environmental factors

<!-- b000397 | prose | pages [16] -->
Air density ρ Rolling resistance coeﬃcient kr Wind resistance coeﬃcient cd

<!-- b000398 | prose | pages [16] -->
1.2kg/m3 0.015

<!-- b000399 | prose | pages [16] -->
• Sharp corner

<!-- b000400 | prose | pages [16] -->
0.23

<!-- b000401 | caption | pages [16] -->
Figure 11: Fuji international speedway. The seven sharp turns are marked with red circles.

<!-- b000402 | prose | pages [16] -->
The black numbers next to the corners represent the radius of curvature, and the green numbers represent the length of the corner.

<!-- b000403 | prose | pages [16] -->
• Slope

<!-- b000404 | caption | pages [16] -->
Figure 12: Course elevation proﬁle. We divide the course into sections according to the diﬀerent

<!-- b000405 | prose | pages [16] -->
slope, and the slope and length of each section are marked with the same color.

<!-- b000406 | caption | pages [16] -->
Table 7: Calculation results of course data

<!-- b000407 | prose | pages [16] -->
Output power W Length km Number Slope

<!-- b000408 | prose | pages [16] -->
1 -2.5% 2 2 -5.5% 1.7 3 6.5% 0.3 4 -4.5% 0.85 5 4% 5.45 6 -3.5% 4.15 7 0% 1.15 8 5% 1.8 9 -2.2% 2.6 10 3% 2.1

<!-- b000409 | prose | pages [16] -->
Speed km/h time min

<!-- b000410 | prose | pages [16] -->
181.34 32.36 3.68 157.35 44.84 2.27 200.10 34.42 0.52 161.91 36.20 1.41 193.21 24.48 13.3 158.85 34.19 10.29 183.63 31.95 2.15 223.97 26.49 4.07 189.63 33.28 4.68 190.28 32.77 3.84

<!-- b000411 | furniture | pages [17] -->
Team # 2210307

<!-- b000412 | furniture | pages [17] -->
Page 17

<!-- b000413 | prose | pages [17] -->
After solving, the shortest time is 46.21 min, the total length of the track is 22.1 km(13.7 mi), the average slope of the track is 3.5%, and the slope is relatively large, which puts forward higher requirements for the rider’s continuous output power, so climber will be more advantageous because the critical power (CP) and anaerobic energy (W ′) of the climber are larger. The obtained results are visualized in Figure 13. When we divide the course into shorter sections, we get Figure 14.

<!-- b000414 | caption | pages [17] -->
Figure 13: Diagram of power, speed, elevation and distance. The x-axis represents distance(mi),

<!-- b000415 | prose | pages [17] -->
the three curves in diﬀerent colors represent power(watts), speed(km/h), and elevation(ft) respectively.

<!-- b000416 | caption | pages [17] -->
Figure 14: Diagram of power, speed, elevation and distance in shorter segments

<!-- b000417 | prose | pages [17] -->
It can be seen that, in order to minimize the total time, the power distributed to the road sections with smaller slopes should be lower; the power distributed to road sections with higher slopes should be higher. The time reduction brought by the use of high output power when going uphill is greater than that when going downhill, so a larger output power is required when going uphill than when going downhill.

<!-- b000418 | heading | pages [17] -->
2021 UCI World Championship time trial course in Flanders, Belgium

<!-- b000419 | caption | pages [17] -->
Table 8: Course information

<!-- b000420 | prose | pages [17] -->
Average altitude Temperature Air pressure

<!-- b000421 | prose | pages [17] -->
28 ◦C 10m 1.013 atm

<!-- b000422 | prose | pages [17] -->
Wind direction

<!-- b000423 | heading | pages [17] -->
Wind strength

<!-- b000424 | prose | pages [17] -->
Air humidity

<!-- b000425 | prose | pages [17] -->
10◦east by south 11m/s 87%

<!-- b000426 | caption | pages [17] -->
Table 9: Course environmental factors

<!-- b000427 | prose | pages [17] -->
Air density ρ Rolling resistance coeﬃcient kr Wind resistance coeﬃcient cd

<!-- b000428 | prose | pages [17] -->
1.23kg/m3 0.012 0.241

<!-- b000429 | furniture | pages [18] -->
Team # 2210307

<!-- b000430 | prose | pages [18] -->
• Sharp corner

<!-- b000431 | furniture | pages [18] -->
Page 18

<!-- b000432 | caption | pages [18] -->
Figure 15: 2021 UCI World Championship time trial course in Flanders, Belgium.

<!-- b000433 | prose | pages [18] -->
• Slope

<!-- b000434 | caption | pages [18] -->
Figure 16: Course elevation proﬁle.

<!-- b000435 | caption | pages [18] -->
Table 10: Calculation results of course data

<!-- b000436 | prose | pages [18] -->
Output power W Length km Number Slope

<!-- b000437 | prose | pages [18] -->
1 0.3% 1.65 2 -0.5% 1.55 3 -1.35% 0.8 4 0% 7.15 5 1% 0.85 6 -0.45% 2.00 7 0% 8.10 8 0.15% 7.2

<!-- b000438 | prose | pages [18] -->
Speed km/h time min

<!-- b000439 | prose | pages [18] -->
204.58 27.34 3.62 127.93 32.96 2.82 100.04 47.00 1.02 165.97 31.83 13.47 209.77 22.19 2.29 131.45 36.82 3.25 167.90 33.01 14.68 184.38 27.65 16.26

<!-- b000440 | prose | pages [18] -->
After solving, the shortest time is 57.41 min, the total length of the track is 29.3 km(18.2 mi), the average slope of the course is 0.17%. The slope is extremely gentle, and the sprinter has more explosive power (Pmax), so it has an advantage on this course. Since there are no steep uphills, the sprinter can use all its power for fast sprints on relatively ﬂat roads, and the power output is evenly distributed.

<!-- b000441 | furniture | pages [19] -->
Team # 2210307

<!-- b000442 | furniture | pages [19] -->
Page 19

<!-- b000443 | prose | pages [19] -->
The obtained results are visualized as follows:

<!-- b000444 | caption | pages [19] -->
Figure 17: Diagram of power, speed, elevation and distance.

<!-- b000445 | prose | pages [19] -->
6.2.1 Self designed course

<!-- b000446 | caption | pages [19] -->
Figure 18: Self designed course.

<!-- b000447 | caption | pages [19] -->
Figure 19: Course elevation proﬁle.

<!-- b000448 | caption | pages [19] -->
Table 11: Course information

<!-- b000449 | prose | pages [19] -->
Average altitude Temperature Air pressure

<!-- b000450 | prose | pages [19] -->
15 ◦C 345m 0.91 atm

<!-- b000451 | prose | pages [19] -->
Wind direction

<!-- b000452 | heading | pages [19] -->
Wind strength

<!-- b000453 | prose | pages [19] -->
Air humidity

<!-- b000454 | prose | pages [19] -->
25◦east by south 7.5m/s 55%

<!-- b000455 | caption | pages [19] -->
Table 12: Course environmental factors

<!-- b000456 | prose | pages [19] -->
Air density ρ Rolling resistance coeﬃcient kr Wind resistance coeﬃcient cd

<!-- b000457 | prose | pages [19] -->
1.17kg/m3 0.019 0.23

<!-- b000458 | furniture | pages [20] -->
Team # 2210307

<!-- b000459 | furniture | pages [20] -->
Page 20

<!-- b000460 | caption | pages [20] -->
Figure 20: Diagram of power, speed, elevation and distance.

<!-- b000461 | prose | pages [20] -->
Our self-designed track has a total length of 13.78 km (8.56 mi) and is characterized by extreme steepness and ruggedness, with a maximum gradient of 25% and an average gradient of 11%. On this type of track, it is easy for a climber to get rid of his opponent on the climbing circuit. The calculated shortest time is 24.58 min.

<!-- b000462 | prose | pages [20] -->
7

<!-- b000463 | heading | pages [20] -->
Model Sensitivity Analysis

<!-- b000464 | heading | pages [20] -->
Sensitivity to Weather and Environment

<!-- b000465 | prose | pages [20] -->
7.1

<!-- b000466 | prose | pages [20] -->
In 5.4, for the inﬂuence of weather and environmental factors, we use the External Factors Analysis Model to summarize these inﬂuencing factors: air temperature (x1), air pressure (x2), altitude (x3), wind resistance (x4), and the ﬁnal target is to minimize the time t to complete the race.

<!-- b000467 | prose | pages [20] -->
Based on the idea of simulating importance sampling with subsets, we transform the sensitivity into the partial derivative of the conditional failure probability with respect to the underlying variable. This method has high computational eﬃciency and precision. As the number of samples in the data set increases, the failure probability will gradually approach a stable value.

<!-- b000468 | caption | pages [20] -->
Table 13: Weather and Environmental COV and Failure Probability

<!-- b000469 | prose | pages [20] -->
Estimation Number Exact

<!-- b000470 | prose | pages [20] -->
∂t

<!-- b000471 | prose | pages [20] -->
COV Error rate

<!-- b000472 | prose | pages [20] -->
−18886 × 10−7 −1.8921 × 10−7 ∂x1 ∂t 0.0187 0.18% −1.4294 × 10−7 −1.3748 × 10−7 ∂x2 ∂t -0.002215 ∂x3 ∂t 0.248 3.97% -0.2219 0.010 0.18% −5.8486 × 10−7 −6.1065 × 10−7 ∂x4 ∂t 0.046 4.22% 1.4687 × 10−7 1.4345 × 10−7 ∂x5 0.015 2.38%

<!-- b000473 | prose | pages [20] -->
Cov is the coeﬃcient of variation of the estimated value commonly used in statistics, which reﬂects the convergence of the estimated value. Error(%) is the failure probability of the estimated value. The larger the error rate, the higher the sensitivity of the corresponding xi. From the results of the sensitivity analysis, it can be concluded that with 1 as the dividing line, air pressure and wind resistance are sensitive factors, while temperature and altitude are insensitive factors. Therefore, air pressure and wind resistance are relatively more inﬂuential indicators for our model.

<!-- b000474 | furniture | pages [21] -->
Team # 2210307

<!-- b000475 | furniture | pages [21] -->
Page 21

<!-- b000476 | heading | pages [21] -->
Sensitivity to Deviations from Target Power

<!-- b000477 | prose | pages [21] -->
7.2

<!-- b000478 | prose | pages [21] -->
In a real race, although the rider will try his best to implement the power distribution plan formulated by the model, the accumulated rage value and energy consumption may aﬀect the rider’s judgment of the situation on the course, thus disrupting the rider’s power distribution on diﬀerent course sections.

<!-- b000479 | prose | pages [21] -->
The same player uses four strategies: the recommended strategy of the Power Overall Planning Model, start fast, start slow, and keep changing. The time of three diﬀerent track segments is used as the objective function to calculate the sensitivity.

<!-- b000480 | caption | pages [21] -->
Table 14: Failure probability of deviation from target (%)

<!-- b000481 | prose | pages [21] -->
Slope t1

<!-- b000482 | prose | pages [21] -->
Recommended strategy 0.42 Start fast 3.31 Start slow 1.54 Keep changing 5.57

<!-- b000483 | prose | pages [21] -->
Flat ground t2 Corner t3

<!-- b000484 | prose | pages [21] -->
0.23 0.33 1.81 2.60 0.84 1.21 3.05 4.38

<!-- b000485 | prose | pages [21] -->
Therefore, to improve rider performance, we supplemented the Power Overall Distribution Model by prioritizing the four strategies and ranking the importance of executing strategies for diﬀerent track segments: recommended strategy > start slow > start fast > keep changing, slope > corner > ﬂat ground.

<!-- b000486 | heading | pages [21] -->
Model Extension to Team Time Trial

<!-- b000487 | prose | pages [21] -->
8

<!-- b000488 | prose | pages [21] -->
In an individual Time Trial (TT), riders tend to target a steady pace at or around their Functional Threshold Power. But in a TTT, each rider will take turns pulling the group at signiﬁcantly higher power for a short period of time. The goal is to keep the teams speed consistent, but higher than any individual rider could ride alone.

<!-- b000489 | prose | pages [21] -->
The best strategy is: ﬁrst, the six riders are connected in a straight line, and the riding direction of the team is parallel to the wind direction, which can ensure that the rider at the head of the team bears most of the wind resistance. Secondly, in the ﬁrst a% of the track section, the two riders with the most explosive power and the lack of endurance lead the slopes and corners respectively, and the rest of the riders are not aﬀected by wind resistance in this track section. In the back a% to b% of the track, the two players whose physical strength was severely weakened due to the wind resistance of the entire team can slowly lag behind the team, and the other four players with more physical strength take turns at the head of the team to resist the wind resistance. Each rider trails behind the team after leading for 1 min, but still has to follow the team closely, so that each rider has a rest time of about 3 min per round with low power output.

<!-- b000490 | prose | pages [21] -->
In addition, the speed of the whole team should be consistent. What should the output power of the team leader(Pleader) be equal to? Obviously, Pleader must be greater than the output power of each track in the individual time trial(PITT). So we deﬁne: Pleader = c × Pleader. In order to reﬂect the diﬀerence between diﬀerent team members, the Rider Ability Evaluation Model was used ﬁrst, and the ability indicators of each rider were calculated by curve ﬁtting.

<!-- b000491 | prose | pages [21] -->
i) If the rider is not in the lead position on a track segment, our model needs to be

<!-- b000492 | furniture | pages [22] -->
Team # 2210307

<!-- b000493 | furniture | pages [22] -->
Page 22

<!-- b000494 | prose | pages [22] -->
changed accordingly: make a change in the force analysis diagram (remove the eﬀect of AERODYNAMIC DRAG), and ignore the formula (9). ii) In other cases, use the Power Overall Planning Model without modiﬁcation.

<!-- b000495 | prose | pages [22] -->
In this way, a multivariate nonlinear programming problem with variables a, b, and c is obtained. The same algorithm is used to solve the problem, and the average value is calculated. A is about 45%, b is about 85%, and c is about 130%.

<!-- b000496 | prose | pages [22] -->
Therefore, we can get the team strategy of the six-person team: i)in the ﬁrst 45% of the track section, let two riders with strong explosive power and relatively weak comprehensive strength take turns to lead the ride, each leading for 5 min, and their output power is 130% based on the ITT model; ii)in the 45% to 85% track section, the two leading riders at the beginning gradually choose to fall behind, and the remaining four riders with stronger stamina each take turns to lead at 130% output power for 1 min. iii)In the last 15% of the track, the rider with the strongest comprehensive ability such as stamina is always in the lead until the end of the race.

<!-- b000497 | prose | pages [22] -->
9

<!-- b000498 | heading | pages [22] -->
Strength and Weakness

<!-- b000499 | prose | pages [22] -->
9.1

<!-- b000500 | heading | pages [22] -->
Strength

<!-- b000501 | prose | pages [22] -->
• Innovativeness. Our model uses 6 separate indicators to measure rider ability, which nicely captures the diﬀerences between riders, making the model relatively reliable and comprehensive. The selected indicators are in line with the latest research in related ﬁelds.

<!-- b000502 | prose | pages [22] -->
• High practical application value. To solve diﬀerent problems, we nest diﬀerent models to make the analysis of each problem more convincing.

<!-- b000503 | prose | pages [22] -->
• Vivid visualizations. Our model shows the power distribution method with many graphs, which is intuitive and clear.

<!-- b000504 | prose | pages [22] -->
9.2

<!-- b000505 | heading | pages [22] -->
Weakness

<!-- b000506 | prose | pages [22] -->
• Some data may not be accurate. We have made many assumptions, some of which are more diﬃcult to implement.

<!-- b000507 | prose | pages [22] -->
• The algorithm has too many variables, although it can comprehensively consider the problem, resulting in high time complexity.

<!-- b000508 | furniture | pages [23] -->
Team # 2210307

<!-- b000509 | furniture | pages [23] -->
Page 23

<!-- b000510 | heading | pages [23] -->
References

<!-- b000511 | references | pages [23] -->
[1] http://cyclingtips.com

<!-- b000512 | references | pages [23] -->
[2] https://olympics.com/en/news/uci-road-world-championships-2021-\

<!-- b000513 | references | pages [23] -->
cycling-flanders-preview

<!-- b000514 | references | pages [23] -->
[3] Leo P, Spragg J, Podlogar T, Lawley JS, Mujika I. Power proﬁling and the power-duration

<!-- b000515 | references | pages [23] -->
relationship in cycling: a narrative review. Eur J Appl Physiol. 2022 Feb;122(2):301-

<!-- b000516 | references | pages [23] -->
316. doi: 10.1007/s00421-021-04833-y. Epub 2021 Oct 27. PMID: 34708276; PMCID:

<!-- b000517 | references | pages [23] -->
PMC8783871.

<!-- b000518 | references | pages [23] -->
[4] Burnley M, Jones AM (2018) Powerduration relationship: physiology, fatigue, and the

<!-- b000519 | references | pages [23] -->
limits of human performance. Eur J Sports Sci 18(1):112

<!-- b000520 | references | pages [23] -->
[5] Barker T, Poole DC, Noble ML, Barstow TJ (2006) Human critical power-oxygen uptake

<!-- b000521 | references | pages [23] -->
relationship at diﬀerent pedalling frequencies. Exper Physiol 91(3):621632

<!-- b000522 | references | pages [23] -->
[6] Bassett DR et al (1999) Comparing cycling world hour records, 19671996: modeling with

<!-- b000523 | references | pages [23] -->
empirical data. Med Sci Sports Exerc 31(11):16651676

<!-- b000524 | references | pages [23] -->
[7] Billat VL et al (2003) The concept of maximal lactate steady state: a bridge between

<!-- b000525 | references | pages [23] -->
biochemistry, physiology and sport science. Sports Med 33(6):407426

<!-- b000526 | references | pages [23] -->
[8] 8. Borszcz FK et al (2018) Functional threshold power in cyclists: validity of the concept

<!-- b000527 | references | pages [23] -->
and physiological responses. Int J Sports Med 39(10):737742

<!-- b000528 | references | pages [24] -->
W`=（ܲഥ낸CP）*300s，which reflects the

<!-- b000529 | references | pages [24] -->
↍♂Race Guidance↍♂

<!-- b000530 | references | pages [24] -->
RIDER’S ABILITY

<!-- b000531 | references | pages [24] -->
How to evaluate a rider’s ability? Our answer is

<!-- b000532 | references | pages [24] -->
to plot the given power duration curve of the

<!-- b000533 | references | pages [24] -->
rider. He needs to output with given power,

<!-- b000534 | references | pages [24] -->
and we measure the duration of the rider

<!-- b000535 | references | pages [24] -->
under this power. This is a sample point.

<!-- b000536 | references | pages [24] -->
Obviously, many sample points are needed to

<!-- b000537 | references | pages [24] -->
draw this curve, and many experiments are

<!-- b000538 | references | pages [24] -->
carried out, each experiment adopts different

<!-- b000539 | references | pages [24] -->
given power and records the duration. This is

<!-- b000540 | references | pages [24] -->
unrealistic in a short time, so we provide a

<!-- b000541 | references | pages [24] -->
simpler test method with certain error: use

<!-- b000542 | references | pages [24] -->
three tests to calculate the rider's maximum

<!-- b000543 | references | pages [24] -->
instantaneous output power (Pmax), critical

<!-- b000544 | references | pages [24] -->
power (CP) and Anaerobic capacity (W `), then

<!-- b000545 | references | pages [24] -->
bring them into the following formula to get

<!-- b000546 | references | pages [24] -->
the same curve. With the increase of test times,

<!-- b000547 | references | pages [24] -->
'

<!-- b000548 | references | pages [24] -->
'

<!-- b000549 | references | pages [24] -->
൅ܹ

<!-- b000550 | references | pages [24] -->
ݐuܹ

<!-- b000551 | references | pages [24] -->
this curve will be constantly revised.

<!-- b000552 | references | pages [24] -->
낸ਹܲ

<!-- b000553 | references | pages [24] -->
ਹ

<!-- b000554 | references | pages [24] -->
낸ܲ

<!-- b000555 | references | pages [24] -->
th

<!-- b000556 | references | pages [24] -->
MEASUREMENT OF INDICATORS

<!-- b000557 | references | pages [24] -->
·The maximum instantaneous power

<!-- b000558 | references | pages [24] -->
（Pmax）is obtained through a 5S maximum

<!-- b000559 | references | pages [24] -->
power output test. The average value of 5S is

<!-- b000560 | references | pages [24] -->
the calculated value, which reflects the

<!-- b000561 | references | pages [24] -->
explosive force of the rider.

<!-- b000562 | references | pages [24] -->
·Critical power（CP）is obtained

<!-- b000563 | references | pages [24] -->
through a 3min full force output test. The

<!-- b000564 | references | pages [24] -->
average power of the rider recorded in the last

<!-- b000565 | references | pages [24] -->
30s is the calculated value, which reflects the

<!-- b000566 | references | pages [24] -->
rider's oxygen uptake ability and the rider's

<!-- b000567 | references | pages [24] -->
comprehensive time trial ability.

<!-- b000568 | references | pages [24] -->
·Anaerobic energy reserve（W`）is

<!-- b000569 | references | pages [24] -->
power test. We record the valueܲഥ，

<!-- b000570 | references | pages [24] -->
obtained through a 5min maximum average

<!-- b000571 | references | pages [24] -->
endurance of the rider

<!-- b000572 | references | pages [24] -->
ABILITY INDEX

<!-- b000573 | references | pages [24] -->
After obtaining this curve, we can evaluate the

<!-- b000574 | references | pages [24] -->
rider's ability index in more detail. We selected

<!-- b000575 | references | pages [24] -->
6 quantities as a rider's ability index, including

<!-- b000576 | references | pages [24] -->
the three mentioned above: maximum

<!-- b000577 | references | pages [24] -->
instantaneous power (Pmax), critical power

<!-- b000578 | references | pages [24] -->
(CP), anaerobic energy reserve (W ') and the

<!-- b000579 | references | pages [24] -->
most basic height (H), weight (m) and vehicle

<!-- b000580 | references | pages [24] -->
control ability (BC), The vehicle control

<!-- b000581 | references | pages [24] -->
capacity BC is the height (CM) divided by 2.5

<!-- b000582 | references | pages [24] -->
times the weight (kg), which represents the

<!-- b000583 | references | pages [24] -->
ratio of the maximum speed when going

<!-- b000584 | references | pages [24] -->
downhill to turning. After obtaining six ability

<!-- b000585 | references | pages [24] -->
indexes, draw a hexagonal ability map. The size

<!-- b000586 | references | pages [24] -->
of the hexagonal area can reflect the

<!-- b000587 | references | pages [24] -->
comprehensive strength of the rider.

<!-- b000588 | references | pages [24] -->
CLASSIFICATION OF RIDERS

<!-- b000589 | references | pages [24] -->
We divide all riders into three directions

<!-- b000590 | references | pages [24] -->
according to their ability index: 1. Sprint riders:

<!-- b000591 | references | pages [24] -->
Pmax is large and explosive, and they are good

<!-- b000592 | references | pages [24] -->
at the smooth road. 2. Climbing Rider: W 'is

<!-- b000593 | references | pages [24] -->
large and has strong endurance. They are good

<!-- b000594 | references | pages [24] -->
at mountain road cycling, especially in more

<!-- b000595 | references | pages [24] -->
climbing stages. 3. All round player: CP is

<!-- b000596 | references | pages [24] -->
very high, Pmax is not as good as sprint rider

<!-- b000597 | references | pages [24] -->
but still high, W 'is not as good as climbing

<!-- b000598 | references | pages [24] -->
rider, and it is good at individual time trial

<!-- b000599 | references | pages [24] -->
and being the master in team time trial. These

<!-- b000600 | references | pages [24] -->
three types of riders should have higher height

<!-- b000601 | references | pages [24] -->
and smaller weight to improve the control

<!-- b000602 | references | pages [24] -->
ability of the vehicle, for they can maintain a

<!-- b000603 | references | pages [24] -->
high speed and avoid falling when they go

<!-- b000604 | references | pages [24] -->
downhill or turning.

<!-- b000605 | references | pages [25] -->
ALICE

<!-- b000606 | references | pages [25] -->
For example, the six ability indicators of female

<!-- b000607 | references | pages [25] -->
rider Alice are as follows:

<!-- b000608 | references | pages [25] -->
We can see that Alice is suitable for individual

<!-- b000609 | references | pages [25] -->
time course with steeper mountains, and team

<!-- b000610 | references | pages [25] -->
time trials as the master.

<!-- b000611 | references | pages [25] -->
ANALYSIS AND STRATEGIES

<!-- b000612 | references | pages [25] -->
We need to specify different strategies

<!-- b000613 | references | pages [25] -->
according to different influencing factors. The

<!-- b000614 | references | pages [25] -->
first is to segment the track according to the

<!-- b000615 | references | pages [25] -->
slope and sharp curve. We input the rider

<!-- b000616 | references | pages [25] -->
capability parameters as well as the course,

<!-- b000617 | references | pages [25] -->
environment and weather parameters, and the

<!-- b000618 | references | pages [25] -->
model can output the most reasonable output

<!-- b000619 | references | pages [25] -->
power of each track segment. The qualitative

<!-- b000620 | references | pages [25] -->
result of our model is that the greater the slope

<!-- b000621 | references | pages [25] -->
of the track, the higher the output power. The

<!-- b000622 | references | pages [25] -->
output power shall be improved, and the speed

<!-- b000623 | references | pages [25] -->
shall be reduced at the curve. Before that, safety

<!-- b000624 | references | pages [25] -->
is premise. The priority of output power

<!-- b000625 | references | pages [25] -->
allocation is uphill > curve > flat ground >

<!-- b000626 | references | pages [25] -->
downhill. Riders should give priority to uphill

<!-- b000627 | references | pages [25] -->
and curve strategies as much as possible. The

<!-- b000628 | references | pages [25] -->
actual deviation from the plan is <10%.

<!-- b000629 | references | pages [25] -->
Environmental factors: after our analysis,

<!-- b000630 | references | pages [25] -->
wind resistance has the most significant impact

<!-- b000631 | references | pages [25] -->
on competition results, so we suggest that the

<!-- b000632 | references | pages [25] -->
equipment team reduce the windward area of

<!-- b000633 | references | pages [25] -->
riding equipment, keep the rider's riding

<!-- b000634 | references | pages [25] -->
posture unchanged and minimize the wind

<!-- b000635 | references | pages [25] -->
resistance coefficient. The ground humidity is

<!-- b000636 | references | pages [25] -->
also a factor that the team needs to pay close

<!-- b000637 | references | pages [25] -->
attention to, because it directly affects the

<!-- b000638 | references | pages [25] -->
ground rolling resistance coefficient, thus

<!-- b000639 | references | pages [25] -->
affecting the safety of riders. It is recommended

<!-- b000640 | references | pages [25] -->
to use tires with large thickness and large

<!-- b000641 | references | pages [25] -->
friction coefficient in a humid track to ensure

<!-- b000642 | references | pages [25] -->
safety and reduce the rolling resistance

<!-- b000643 | references | pages [25] -->
coefficient at the same.

<!-- b000644 | references | pages [25] -->
EXAMPLE: 2021 OLYMPIC TIME

<!-- b000645 | references | pages [25] -->
TRIAL COURSE IN TOKYO, JAPAN

<!-- b000646 | references | pages [25] -->
This competition has the characteristic of large

<!-- b000647 | references | pages [25] -->
average slope and many sharp turns. If Alice

<!-- b000648 | references | pages [25] -->
attends it, she will get a great advantage. We

<!-- b000649 | references | pages [25] -->
investigate the wind force, wind direction, air

<!-- b000650 | references | pages [25] -->
pressure, air temperature, ground humidity and

<!-- b000651 | references | pages [25] -->
air density on the day of the competition,

<!-- b000652 | references | pages [25] -->
calculate the wind resistance and ground

<!-- b000653 | references | pages [25] -->
rolling resistance. After substituting into the

<!-- b000654 | references | pages [25] -->
model, the planned output power of each

<!-- b000655 | references | pages [25] -->
segment of the trial is output. What Alice

<!-- b000656 | references | pages [25] -->
needs to firstly pay attention to is that she must

<!-- b000657 | references | pages [25] -->
follow the plan as much as possible on steep

<!-- b000658 | references | pages [25] -->
uphill slopes and sharp curves.

<!-- b000659 | references | pages [25] -->
TEAM TIME TRIAL

<!-- b000660 | references | pages [25] -->
For team time trial ，we suggest that the

<!-- b000661 | references | pages [25] -->
top two sprinters with explosive power take

<!-- b000662 | references | pages [25] -->
turns to lead in the first 45% of race. They can

<!-- b000663 | references | pages [25] -->
resist air resistance for the whole team. The

<!-- b000664 | references | pages [25] -->
output power is 130% of that of individual

<!-- b000665 | references | pages [25] -->
time trial. From 45% to 85% of the track, the

<!-- b000666 | references | pages [25] -->
two sprinters consume a lot of physical energy

<!-- b000667 | references | pages [25] -->
and gradually fall behind, and the remaining

<!-- b000668 | references | pages [25] -->
four climbing and all-round riders take turns to

<!-- b000669 | references | pages [25] -->
lead the race in a cycle. Better, you can arrange

<!-- b000670 | references | pages [25] -->
climbing riders to lead the race in the uphill

<!-- b000671 | references | pages [25] -->
section and all-round riders to lead the race in

<!-- b000672 | references | pages [25] -->
the flat section. In the last 15%, two all-round

<!-- b000673 | references | pages [25] -->
riders should lead the race in turn. The two

<!-- b000674 | references | pages [25] -->
climbing riders need to keep up with the team,

<!-- b000675 | references | pages [25] -->
and the last four players almost cross the finish

<!-- b000676 | references | pages [25] -->
line at the same time. It should be noted that

<!-- b000677 | references | pages [25] -->
the track, environment, and weather factors

<!-- b000678 | references | pages [25] -->
mentioned above should still be considered in

<!-- b000679 | references | pages [25] -->
the team time trial. The rider's ability, tactical

<!-- b000680 | references | pages [25] -->
arrangement, power distribution strategy and

<!-- b000681 | references | pages [25] -->
environment should be considered in an all-

<!-- b000682 | references | pages [25] -->
round way.

<!-- b000683 | references | pages [25] -->
(Team 2210307)
