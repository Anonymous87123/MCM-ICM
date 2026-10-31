# P-A-2022-2209812-101c692c

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
2209812

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Power Curve Make Cyclists Faster and Faster

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Every ride has a pace—whether or not you’re in control of that pace all comes down to essential planning based on his or her power profile. In this paper, we develop models to guide cycling races based on power curves (PC), measure the sensitivity to weather and power distribution’s deviation, and optimal power use for a team time trial.

<!-- b000010 | prose | pages [1] -->
In Task 1 & 2: First, we choose a three-parameter hyperbolic model based on exercise physi- ology that is more accurate in the critical power (CP) model. Based on it, we utilize data to define the PC of male and female time trial specialists, male and female sprinters (Figure 7). Among them, the sprinters have higher explosive power, but the time trial specialists (TTS) have more long-term endurance, and female players have less explosive power and endurance than male players.

<!-- b000011 | prose | pages [1] -->
After that, we found out the fatigue and recovery (FR) model, forming optimal pacing control. Then we obtain the necessary condition based on the Pontryagin’s Minimum Principle (PMP) and the numerical solution of Behrman equation based on dynamic programming (DP) and Behrman’s principle. We apply the PC to the time trial course of Tokyo Olympic, UCI World Championship and own design, which is located at Italy’s San Felice Circeo (Figure 12), and the power distribution of cyclists are shown in Figure 10, 11, and 13. We found this result to be consistent with the characteristics of the cyclists above, which including the duration of man time trial specialist in Tokyo Olympic is 1h:41m:29.4s (3641.49 s), and the woman is 0h:33m:4.51s (1984.51 s).

<!-- b000012 | prose | pages [1] -->
In Task 3 & 4: in this section, we measure the sensitivity of our model to weather and power distribution’s deviation.

<!-- b000013 | prose | pages [1] -->
For wind, the sensitivity to wind effect is up to corresponding course. The closer the course is to a bar or strip, the more regular the wind direction and velocity is to the cyclist, otherwise the more uncertain it is. For temperature influence, in a suitable range, the lower the temperature, the better for cyclists. Thus, cyclists should observe the terrain well, make reasonable use of the wind direction, and pay attention to do certain heat dissipation measures.

<!-- b000014 | prose | pages [1] -->
For power distribution’s deviation, the greater deviation probability, the greater the time cost and the trend of time cost.Therefore, maintaining good pacing stability is the key to getting good results. For power deviations occurring on different sections, the impact on cyclists is more sensi- tive when the elevation is more undulating, and less so when the undulation is smaller. Maintaining their pedaling rhythm while riding uphill, while resting and attempting to maintain high speed when riding downhill are significant to cyclists.

<!-- b000015 | prose | pages [1] -->
In Task 5: this section shows how team riding reduces resistance and maximizes the team power. We found that the real-time position of the cyclist in the team and the time the cyclist lead each time are key factors in determining the team’s performance. Based on them, we develop a team time trial Optimization Model to maximize power use.

<!-- b000016 | prose | pages [1] -->
Finally, we evaluate the strengths and weaknesses of model. And a two-page rider’s race guid- ance has been written for a Directeur Sportif.

<!-- b000017 | keywords | pages [1] -->
Keywords: Power Curve, Dynamics Analysis, DP, PMP, Behrman Equation.

<!-- b000018 | furniture | pages [2] -->
Team # 2209812

<!-- b000019 | furniture | pages [2] -->
Page 2 of 24

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1 Introduction

<!-- b000022 | contents | pages [2] -->
3

<!-- b000023 | contents | pages [2] -->
1.1

<!-- b000024 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
3

<!-- b000026 | contents | pages [2] -->
1.2

<!-- b000027 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
1.3

<!-- b000030 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000033 | contents | pages [2] -->
4

<!-- b000034 | contents | pages [2] -->
2.1

<!-- b000035 | contents | pages [2] -->
Assumptions and Explanations . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
4

<!-- b000037 | contents | pages [2] -->
2.2

<!-- b000038 | contents | pages [2] -->
Notations

<!-- b000039 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
5

<!-- b000041 | contents | pages [2] -->
2.3

<!-- b000042 | contents | pages [2] -->
The Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
5

<!-- b000044 | contents | pages [2] -->
2.3.1

<!-- b000045 | contents | pages [2] -->
Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
5

<!-- b000047 | contents | pages [2] -->
2.3.2

<!-- b000048 | contents | pages [2] -->
Data Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
5

<!-- b000050 | contents | pages [2] -->
3 TASK 1 & 2: Guiding Cycling Races Based on Power Curves

<!-- b000051 | contents | pages [2] -->
6

<!-- b000052 | contents | pages [2] -->
3.1

<!-- b000053 | contents | pages [2] -->
The Critical Power Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
6

<!-- b000055 | contents | pages [2] -->
3.1.1

<!-- b000056 | contents | pages [2] -->
The 2-parameter Hyperbolic Model . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
6

<!-- b000058 | contents | pages [2] -->
3.1.2

<!-- b000059 | contents | pages [2] -->
The 3-parameter Hyperbolic Model . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
7

<!-- b000061 | contents | pages [2] -->
3.2

<!-- b000062 | contents | pages [2] -->
Define the Power Profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
7

<!-- b000064 | contents | pages [2] -->
3.3

<!-- b000065 | contents | pages [2] -->
Optimal Pacing of a Cyclist . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
8

<!-- b000067 | contents | pages [2] -->
3.3.1

<!-- b000068 | contents | pages [2] -->
Fatigue and Recovery of Cyclists

<!-- b000069 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
8

<!-- b000071 | contents | pages [2] -->
3.3.2

<!-- b000072 | contents | pages [2] -->
Optimal Control Formulation

<!-- b000073 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
9

<!-- b000075 | contents | pages [2] -->
3.3.3

<!-- b000076 | contents | pages [2] -->
Necessary Condition for Optimal Solution . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
11

<!-- b000078 | contents | pages [2] -->
3.3.4

<!-- b000079 | contents | pages [2] -->
Numerical Solution of the Problem

<!-- b000080 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
12

<!-- b000082 | contents | pages [2] -->
3.4

<!-- b000083 | contents | pages [2] -->
Apply Model to Time Trial Courses

<!-- b000084 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [2] -->
13

<!-- b000086 | contents | pages [2] -->
3.4.1

<!-- b000087 | contents | pages [2] -->
Determine the Constants’ Values.

<!-- b000088 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [2] -->
13

<!-- b000090 | contents | pages [2] -->
3.4.2

<!-- b000091 | contents | pages [2] -->
Simulation Results and Analysis . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
14

<!-- b000093 | contents | pages [2] -->
4 TASK 3 & 4: Sensitivity to Weather and Power Distribution’s Deviations

<!-- b000094 | contents | pages [2] -->
16

<!-- b000095 | contents | pages [2] -->
4.1

<!-- b000096 | contents | pages [2] -->
The influence of the weather . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
16

<!-- b000098 | contents | pages [2] -->
4.1.1

<!-- b000099 | contents | pages [2] -->
Wind Influence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
16

<!-- b000101 | contents | pages [2] -->
4.1.2

<!-- b000102 | contents | pages [2] -->
Temperature Influence . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
17

<!-- b000104 | contents | pages [2] -->
4.2

<!-- b000105 | contents | pages [2] -->
The Influence of Power Distribution’s Deviation . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
18

<!-- b000107 | contents | pages [2] -->
4.2.1

<!-- b000108 | contents | pages [2] -->
Sensitivity of Deviation Probability . . . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
18

<!-- b000110 | contents | pages [2] -->
4.2.2

<!-- b000111 | contents | pages [2] -->
Sensitivity of Location Deviation

<!-- b000112 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [2] -->
19

<!-- b000114 | contents | pages [2] -->
5 TASK 5: Optimal Power Use for a Team Time Trial

<!-- b000115 | contents | pages [2] -->
20

<!-- b000116 | contents | pages [2] -->
5.1

<!-- b000117 | contents | pages [2] -->
The Benefit of Team Riding

<!-- b000118 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
20

<!-- b000120 | contents | pages [2] -->
5.2

<!-- b000121 | contents | pages [2] -->
Team Time Trial Optimization Model

<!-- b000122 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
20

<!-- b000124 | contents | pages [2] -->
6 Evaluation of Strengths and Weaknesses

<!-- b000125 | contents | pages [2] -->
21

<!-- b000126 | contents | pages [2] -->
6.1

<!-- b000127 | contents | pages [2] -->
Strengths

<!-- b000128 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000129 | contents | pages [2] -->
21

<!-- b000130 | contents | pages [2] -->
6.2

<!-- b000131 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000132 | contents | pages [2] -->
21

<!-- b000133 | contents | pages [2] -->
References

<!-- b000134 | contents | pages [2] -->
21

<!-- b000135 | contents | pages [2] -->
Memo

<!-- b000136 | contents | pages [2] -->
23

<!-- b000137 | furniture | pages [3] -->
Team # 2209812

<!-- b000138 | furniture | pages [3] -->
Page 3 of 24

<!-- b000139 | heading | pages [3] -->
1 Introduction

<!-- b000140 | heading | pages [3] -->
1.1 Problem Background

<!-- b000141 | prose | pages [3] -->
Every cyclist knows that time and intensity are inextricably linked. For example, sprinting for more than a few seconds is very difficult, yet easy endurance riding may be continued for several hours with correct feeding. A power curve (PC) is a representation of this relationship, and viewing it might provide valuable information about your relative strengths and limitations.

<!-- b000142 | prose | pages [3] -->
The cyclists might use the PC to determine how much power applies based on the rider’s loca- tion on the race. In this problem, we need to accomplish the following objectives:

<!-- b000143 | prose | pages [3] -->
• Define the power profiles of a time trial specialist and another type of rider while accounting for gender. Then put the model to the test on a variety of time trial courses.

<!-- b000144 | prose | pages [3] -->
• Determine the weather’s possible influence and sensitivity, as well as how sensitive the results are to rider deviations from the target power distribution.

<!-- b000145 | prose | pages [3] -->
• Extend the model to include optimal power use for a six-rider team time trial, with the team’s time being calculated after the fourth rider crosses the finish line.

<!-- b000146 | heading | pages [3] -->
1.2 Literature Review

<!-- b000147 | prose | pages [3] -->
This question is maily about guide cyclist according to PC. In the last few years, there has been a hot line of research in both the analysis of cyclists from a physiological perspective and the optimization of cycling competition from a race perspective. Thus, this section focuses on the main models in these two aspects.

<!-- b000148 | prose | pages [3] -->
• Above all, in terms of power curve description, one is a simple two-parameter critical power (CP) model with inappropriate physiological assumptions [5], whereas the other is a somewhat more difficult but more physiologically acceptable three-parameter CP model [10].

<!-- b000149 | prose | pages [3] -->
• Regarding the optimization of the cyclist’s pace, the relationship between power distribution and power curve can be analyzed starting from the physiological model of fatigue and recovery [13]. It effectively explains the dynamic equilibrium process of fatigue and recovery of cyclists in the course of a race.

<!-- b000150 | prose | pages [3] -->
• In terms of optimizing the cyclist’s speed, Ashtiani, Faraz, et al. [13] proposed a dynamics- based optimization model. It not only contains the force model of a cyclist, but also takes the effect of weather into full consideration.

<!-- b000151 | prose | pages [3] -->
• The aerodynamic interaction between cyclists is very important to the effectiveness of a strat- egy, whick is the key to team strategy in team time trial.

<!-- b000152 | prose | pages [3] -->
2-parameter CP Model Simple, Inappropriate Physiology 3-parameter CP Model Complex, appropriate Task 1 Cyclists' race strategy

<!-- b000153 | heading | pages [3] -->
Fatigue-Recovery Model

<!-- b000154 | heading | pages [3] -->
Pacing Optimization Model

<!-- b000155 | prose | pages [3] -->
Task 2,3 Dynamics Aerodynamic Interaction Team Strategy Task 5

<!-- b000156 | caption | pages [3] -->
Figure 1: Literature Review Framework

<!-- b000157 | furniture | pages [4] -->
Team # 2209812

<!-- b000158 | furniture | pages [4] -->
Page 4 of 24

<!-- b000159 | heading | pages [4] -->
1.3 Our Work

<!-- b000160 | prose | pages [4] -->
The work we have done in this problem is mainly shown in the following Figure (2).

<!-- b000161 | prose | pages [4] -->
Guiding Cycling Races Based on Power Curves Guiding Cycling Races Based on Power Curves

<!-- b000162 | prose | pages [4] -->
Dynamic Solution Dynamic Solution 3-parameter CP Model 3-parameter CP Model Optimal Pacing Control Optimal Pacing Control Fatigue-Recovery Model Fatigue-Recovery Model Necessary Condition Necessary Condition Dynamics Solution Dynamics Solution Dynamic Programming Dynamic Programming

<!-- b000163 | prose | pages [4] -->
Behrman principle Behrman principle Power Profile and Distribution Power Profile and Distribution Processing Processing

<!-- b000164 | heading | pages [4] -->
Sensitivity{

<!-- b000165 | heading | pages [4] -->
Sensitivity{

<!-- b000166 | prose | pages [4] -->
Sensitvity{ Sensitvity{ Wind Influence Wind Influence Deviation Probability Deviation Probability Weather Weather Deviations Deviations Temperature Influence Temperature Influence Location Deviation Location Deviation data data Optimal Power Use for a Team Time Trial Optimal Power Use for a Team Time Trial

<!-- b000167 | heading | pages [4] -->
Optimization Model

<!-- b000168 | heading | pages [4] -->
Optimization Model

<!-- b000169 | prose | pages [4] -->
Reduce Resistence Reduce Resistence Maximize the Team Power Maximize the Team Power

<!-- b000170 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000171 | heading | pages [4] -->
2 Preparation of the Models

<!-- b000172 | heading | pages [4] -->
2.1 Assumptions and Explanations

<!-- b000173 | prose | pages [4] -->
Considering that practical probelms always contain many complex factors, we made the fol- lowing assumptions to help us with our modeling.

<!-- b000174 | prose | pages [4] -->
• Assumption 1: Brakes can be neglected [2].

<!-- b000175 | prose | pages [4] -->
⇒Explanation: On the one hand, none of the bikes were equipped with a data logging system capable of measuring braking force. On the other hand, the only unwanted braking would be to avoid crashes, which is usually not an issue in individual time trials.

<!-- b000176 | prose | pages [4] -->
• Assumption 2: Lateral movement can be neglected [2].

<!-- b000177 | prose | pages [4] -->
⇒Explanation: From an energy point of view, this makes sense. For example, With a lateral velocity of 1 m/s and most of professional cyclists’ speed of more than 10 m/s, the lateral velocity accounts for less than 1% of the total speed.

<!-- b000178 | prose | pages [4] -->
• Assumption 3: Bicycles are all the same size.

<!-- b000179 | prose | pages [4] -->
⇒Explanation: The Olympic spirit tells us that human body limits and competition results are broken by the athletes themselves, not by their equipment. Therefore, unifying bicycle standards is not just about easy modeling, it’s also part of fair play. The corresponding values for bicycles will be given in Section 3.4.1.

<!-- b000180 | prose | pages [4] -->
• Assumption 4: Cyclists will keep their posture constant during the race ⇒Explanation: From an aerodynamic standpoint [2], the resistance area is heavily reliant on the cyclist’s position. Because the cyclist’s posture are always changing, the resistance area should be averaged. At the highest levels of competition, riders develop their unique riding rhythm and maintain a stable posture for extended periods of time. Therefore, it is reasonable to assume that.

<!-- b000181 | furniture | pages [5] -->
Team # 2209812

<!-- b000182 | furniture | pages [5] -->
Page 5 of 24

<!-- b000183 | heading | pages [5] -->
2.2 Notations

<!-- b000184 | prose | pages [5] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000185 | caption | pages [5] -->
Table 1: Notations

<!-- b000186 | prose | pages [5] -->
Symbol Description P power output CP critical power W ′ available work over CP (anaerobic work capacity) TTE time-to-exhaustion w remaining anaerobic energy wrec recovered anaerobic energy Trec recovery duration Pmax maximal power possible s cyclist’s traveled distance v cyclist’s cycling velocity angle of wind direction with north ϕ angle of cycling direction with north γ V wind velocity

<!-- b000187 | heading | pages [5] -->
2.3 The Data

<!-- b000188 | heading | pages [5] -->
2.3.1 Data Collection

<!-- b000189 | prose | pages [5] -->
The data we used mainly include Body data of different types of cyclists, . The data sources are summarized in Table 2 below,

<!-- b000190 | caption | pages [5] -->
Table 2: Data Source Websites

<!-- b000191 | prose | pages [5] -->
Database Names Database Websites

<!-- b000192 | prose | pages [5] -->
Training Peaks https://www.trainingpeaks.com/blog/power-profiling/ STRAVA-Tokyo2020 https://www.strava.com/activities/5678015293 STRAVA-BelgiumUCI https://www.strava.com/activities/6006887196

<!-- b000193 | prose | pages [5] -->
where data of Training Peaks includes cyclists’ power of different genders and types at 5 s, 1 minute, 5 minutes, and functional threshold (FT). And the course data, including latitude, longi- tude and altitude, of STRAVA-Tokyo2020 is at 2021 Olympic Time Trial course in Tokyo, Japan, as well as STRAVA-BelgiumUCI is 2021 UCI World Championship men’s time trial course in Flanders, Belgium on September 22, 2021.

<!-- b000194 | heading | pages [5] -->
2.3.2 Data Processing

<!-- b000195 | prose | pages [5] -->
For the course data of STRAVA-Tokyo2020 and STRAVA-BelgiumUCI, we need to discretize the track into multiple locations and get the distance and slope between adjacent locations. More details of data processing are shown in Figure 3 and 4 below.

<!-- b000196 | furniture | pages [6] -->
Team # 2209812

<!-- b000197 | furniture | pages [6] -->
Page 6 of 24

<!-- b000198 | prose | pages [6] -->
Data processing

<!-- b000199 | prose | pages [6] -->
• Obtain the angle between two adjacent locations (approximately step1 600m-1000m apart) on the Earth‘s sphere (Figure 3).

<!-- b000200 | prose | pages [6] -->
• Convert the latitude and longitude of two adjacent locations to their straight-line distance. Step2

<!-- b000201 | prose | pages [6] -->
• Obtain the slope of adjacent locations based on straight-line distance and elevation. Step3

<!-- b000202 | caption | pages [6] -->
Figure 3: Data Processing

<!-- b000203 | caption | pages [6] -->
Figure 4: Distance calculation

<!-- b000204 | heading | pages [6] -->
3 TASK 1 & 2: Guiding Cycling Races Based on Power Curves

<!-- b000205 | heading | pages [6] -->
3.1 The Critical Power Model

<!-- b000206 | prose | pages [6] -->
It is a common experience that cycling at a relatively fast yet comfortable pace can be continued for a considerable period without undue fatigue. Even a small increase in the speed, however, sig- nificantly increases the perceived effort and drastically limits the tolerated duration of exercise. The fact that these sensations have substantial mathematical and physiological foundations, which are enshrined in the critical power (CP) notion, is probably underappreciated. The CP thus represents an important parameter of aerobic function (in addition to gas exchange threshold (GET), maximal O2 uptake (VO2max), and exercise efficiency) [3]. It also offers a useful framework for studying and better understanding the processes of tiredness and exercises intolerance. Among several current PD models, the 2-parameter hyperbolic (CP2−hyp) model and the 3-parameter hyperbolic (CP3−hyp) model are studied the most [4].

<!-- b000207 | heading | pages [6] -->
3.1.1 The 2-parameter Hyperbolic Model

<!-- b000208 | prose | pages [6] -->
From a mathematical point of view, within the severe-intensity domain, the CP is one of two (or three) empirical parameters that establish the link between power output (P) and time-to- exhaustion (TTE). This connection is known to be hyperbolic, with the power-asymptote repre- senting the CP and the curvature constant denoted W ′ (Figure 5a) [5, 6].

<!-- b000209 | prose | pages [6] -->
TTE = W ′/(P−CP) (1)

<!-- b000210 | prose | pages [6, 7] -->
(a) The hyperbolic form (b) The linear form where TTE denotes the motion maintenance time at a given power, W ′ is the available work in excess of CP, P is the average power over the duration of the exercise (the equation has another explaination at Section 3.3). CP defines the highest power output to maintain intracellular home- ostasis. The formula can be applied to predict the exercise maintenance time TTE for any given output power above CP, which has great potential application in training. It may also be useful to know which P must be chosen in order to achieve a given TTE. For this purpose the equation 1 is solved for P, thus giving it a linear form (Figure 5b):

<!-- b000211 | caption | pages [6] -->
Figure 5: The Two-parameter Model

<!-- b000212 | furniture | pages [7] -->
Team # 2209812

<!-- b000213 | furniture | pages [7] -->
Page 7 of 24

<!-- b000215 | prose | pages [7] -->
P = W ′/TTE +CP (2) For example, if we take a hypothetical athlete with a measured CP of 300 W and W ′ of 20 kJ, we can calculate (using Equation (1)) the amount of time that this athlete could sustain a given P.

<!-- b000216 | prose | pages [7] -->
Despite the fact that this 2-parameter hyperbolic CP model can explain a wide range of occur- rences, it still has a number of incorrect assumptions that contravene known physiology [7]. They were presented below:

<!-- b000217 | prose | pages [7] -->
• Power and velocity are not achievable instantaneously. The required power takes 2 minutes or more to become accessible through the oxygen delivery system, and the required velocity takes a few seconds to attain due to body acceleration or biomechanical considerations.

<!-- b000218 | prose | pages [7] -->
• Power continues to decline below the asymptote defined by CP given enough time. The CP model is applicable to activity that lasts between 2 and 30 minutes in most persons, but up to 60 minutes in some.

<!-- b000219 | prose | pages [7] -->
• Power and velocity are not infinite since everyone has a maximum running speed that they can’t exceed [8].

<!-- b000220 | prose | pages [7] -->
• At the point of fatigue, power does not have to be entirely exhausted. The individual in constant-power trials stops exercising when he or she can no longer maintain the required power output.

<!-- b000221 | heading | pages [7] -->
3.1.2 The 3-parameter Hyperbolic Model

<!-- b000222 | prose | pages [7] -->
For middle and long distance races, studies had found that a athlete’s unique ideal velocity profile consists of three segments: a brief moment of maximum acceleration, followed by a long period of continuous (but not all-out) pace, and finally a brief period in which the racer collapses exhausted over the finish line [9]. Based on it, to overcome the limitations imposed by the two- parameter CP model’s assumptions, Morton created a three-parameter hyperbolic CP model [10]. The three-parameter model overcomes the assumptions that maximal power output is infinite and that exhaustion occurs when power is depleted. His modification is expressed mathematically as follows:

<!-- b000223 | prose | pages [7] -->
W ′ TTE = P−CP +k (3)

<!-- b000224 | prose | pages [7] -->
where k is the asymptote and assumes a negative value. Because the maximal power possible (Pmax) can only occur for instantaneous time (i.e., TTE = 0), it implies the following:

<!-- b000225 | prose | pages [7] -->
W ′ Pmax TTE = P−CP + (4) CP−Pmax

<!-- b000226 | heading | pages [7] -->
3.2 Define the Power Profiles

<!-- b000227 | prose | pages [7, 8] -->
Download the corresponding data from the Training Peaks website in Table 2. The dataset’s de- veloper established the maximum and lower limits of each range based on the known performance capacities of world-class athletes and untrained individuals. It includes cyclists of different genders and types at 5 s, 1 minute, 5 minutes, and functional threshold (FT) power, allowing us to fit the CP model based on them (Figure 6) [11].

<!-- b000228 | furniture | pages [8] -->
Team # 2209812

<!-- b000229 | furniture | pages [8] -->
Page 8 of 24

<!-- b000231 | prose | pages [8] -->
{ Male cyclists Time Trialist Pursuiter Fit model with the power Data Power curve Data at 1s, 1m, 5m and FT Female cyclists Rouleur Sprinter

<!-- b000232 | caption | pages [8] -->
Figure 6: Cyclist Data Overview

<!-- b000233 | prose | pages [8] -->
Using some data in Training Peaks (Table 2), the power curves PC of different gender cyclists of time trial specialist and sprinter are shown in the Figure 7.

<!-- b000234 | prose | pages [8] -->
SM SM

<!-- b000235 | prose | pages [8] -->
TM TM

<!-- b000236 | prose | pages [8] -->
SW SW TW TW

<!-- b000237 | prose | pages [8] -->
TM TM TM SM SM TW TW TW SM SW SW SW

<!-- b000238 | caption | pages [8] -->
Figure 7: the Result of Task 1

<!-- b000239 | prose | pages [8] -->
Based on this picture, we can draw some conclusions, which are shown below:

<!-- b000240 | prose | pages [8] -->
• When comparing the power of two kinds of cyclists, the sprinter has more power than the time trial specialist (PS > PT) when the duration is short (Time < 20s). This indicates that, in general, the Sprinter more dominating at the start of the race. However, as time continued to increase, the sprinter lost his edge more and more. It is obvious that when Time > 300s, the time trial specialist has the upper hand, and the longer the time, the more obvious the advantage.

<!-- b000241 | prose | pages [8] -->
• From a gender perspective, female cyclists of the same type will always have weaker power than male cyclists. Even the female sprinter can hardly win the male time trial specialist in terms of explosive power, but over time, the female sprinter can prevail over the male time trial specalist, which shows that the female cyclist’s staying power is not too weak.

<!-- b000242 | heading | pages [8] -->
3.3 Optimal Pacing of a Cyclist

<!-- b000243 | heading | pages [8] -->
3.3.1 Fatigue and Recovery of Cyclists

<!-- b000244 | prose | pages [8, 9] -->
The concept of CP is defined as the maximum power output that can be maintained indefinitely and it’s controled by Equation (1) [12]. W ′ is available work over CP. From the perspective of phys- iology, it also can be explained as anaerobic work capacity. So the Equation (1) means that a cyclist can only maintain that power for a certain period of time before running out of anaerobic energy. During the race, the overall trend of the cyclist’s power decreases, and W ′ gradually recovers when the power is less than CP. Therefore, the cyclist is in a dynamic equilibrium based on a dynamic Fatigue-Recovery (PR) model until the final acceleration.

<!-- b000245 | furniture | pages [9] -->
Team # 2209812

<!-- b000246 | furniture | pages [9] -->
Page 9 of 24

<!-- b000248 | prose | pages [9] -->
As we discussed above, the maximum power a cyclist can produce if he or she maximizes his or her anaerobic work capacity (W ′) is CP. For further explanation, we define w as the remaining W ′ during the ride. As the following Equation (5) shows, the recovery process of w can be similar to its consumption. If the cyclist is pedaling at a constant power (P) below CP for the duration Trec, the actual amount of recovered energy (wrec) will be less than (CP−P)×Trec. Thus, we propose the notion of an adjusted recovery power Pad j as, Pad j = CP−wrec (5) Trec to be used in a switching model of energy expenditure and recovery as follows, ( −(P−CP) P ⩾CP dw dt = (6)    − Pad j −CP P < CP

<!-- b000249 | prose | pages [9] -->
where P is the pedaling power of the cyclist. We further hypothesize that the recovery power Pad j is solely determined by the pedaling power P and not by the duration Trec. Study shows that Pad j can be well approximated as a linear function of pedaling power P with constants a and b that should be determined for each cyclist [13]. Thus Pad j is defined as, Pad j = aP+b (7) The cyclist’s capacity to create instantaneous maximal power (Pmax) is influenced by W’ ex- penditure. A study [14] discovered the following linear connection between Pmax and anaerobic energy w:

<!-- b000250 | prose | pages [9] -->
Pmax = aw+CP (8)

<!-- b000251 | heading | pages [9] -->
3.3.2 Optimal Control Formulation

<!-- b000252 | prose | pages [9] -->
In this section, pacing of a cyclist is modeled as a restricted optimum control problem. The key dynamic state variables are: i) the cyclist’s remaining anaerobic energy w; ii) the cyclist’s traveled distance s; and iii) the cyclist’s cycling velocity v. The control input is the cyclist’s power at a function of time u(t). Thus the state-space model is of the form:

<!-- b000253 | prose | pages [9] -->
T  ˙x = f (x(t),u(t)) = f1 f2 f3 (9) where the state vector is, T  s(t) v(t) w(t) x(t) = (10) and f is a nonlinear function that maps the input and states to the rate at which they change. f1 is just velocity in Equation (9), so, f1 = ds dt = v (11)

<!-- b000254 | prose | pages [9] -->
And f2 is obtained using Newton’s second law (Figure 8), f2 = dv(t) = u(t) mv(t) −h(s)−1 2mCdρAv(t)2 (12) dt where h(s) = mb m g(sin(θ)+CR cos(θ)) (13)

<!-- b000255 | prose | pages [9, 10] -->
and a is the joint acceleration of the cyclist and the bicycle, G is their effective gravity, FP is the pedaling force, and FW is the resistance of the oncoming wind (wind direction will be considered in Section 4.1), f1 and f2 are frictions of bicycle, FN1 and FN2 are support forces, mb is the mass of the bicycle and cyclist, g is gravity acceleration, Cd is aerodynamic drag coefficient, A is frontal area, ρ is the density of air which is assumed to be contant and unaffected by elevation, θ is the road slope which is positive for uphill and negative for downhill, and CR is the coefficient of rolling resistance of the road, and m is the effective mass of the bicycle, which is calculated by adding the impact of the wheels’ rotational inertia to mb, m = mb +2 Iw (14) R2w where Iw is the wheel rotational inertia, and Rw is the radius of bicycle wheel.

<!-- b000256 | furniture | pages [10] -->
Team # 2209812

<!-- b000257 | furniture | pages [10] -->
Page 10 of 24

<!-- b000259 | prose | pages [10] -->
FW

<!-- b000260 | prose | pages [10] -->
a

<!-- b000261 | prose | pages [10] -->
M1 M1

<!-- b000262 | prose | pages [10] -->
FN1 FN1 M2 M2 f2f2 FN2 FN2 G

<!-- b000263 | prose | pages [10] -->
q f2f2

<!-- b000264 | caption | pages [10] -->
Figure 8: Cyclist and Bicycle Aerodynamic Forces

<!-- b000265 | prose | pages [10] -->
We equate the propulsion power u(t) to the cyclist’s power on the pedals if the bicycle drivetrain is 100 percent efficient. Gear selection is not a consideration in our formulation since we use cyclist pedalling power rather than force as input, which would otherwise make the optimization more complicated.

<!-- b000266 | prose | pages [10, 11] -->
Note that the previously displayed Equation 6 is the third state equation for the time derivative of the cyclist’s remaining anaerobic energy, ( u ⩾CP CP−u f3 = dw (a) dt = (15) u < CP (b) CP−(au+b) Now we can design a minimum-time optimum control problem for the pacing strategy in a time-trial. Time is the objective function to be minimised, Z tf u(t) J = dt min (16) t0 subject to,  state−space model : ˙x = f (x(t),u(t))   0 ⩽v(t) ⩽vmax  velocity limits :  (17) 0 ⩽w(t) ⩽W ′ remaining energy limits :  0 ⩽u(t) ⩽Pmax (w)   cyclist power limits :  where Pmax is defined by Equation (8). The final position is specified and fixed in this formulation, while the other two states, v and w, are uncertain. The maximum speed vmax is assumed to be constant throughout the journey in the simulations in this research, including the case of sharp turns.

<!-- b000267 | furniture | pages [11] -->
Team # 2209812

<!-- b000268 | furniture | pages [11] -->
Page 11 of 24

<!-- b000270 | heading | pages [11] -->
3.3.3 Necessary Condition for Optimal Solution

<!-- b000271 | prose | pages [11] -->
In this part, we use the variational approach to investigate the given optimum control issue. The required condition for the optimality of input u, according to Pontryagin’s Minimum Principle (PMP), is that it minimizes the following Hamiltonian function, H (x(t),u(t),λ (t)) = L(x(t),u(t))+λ T (t){f (x(t),u(t))} (18)

<!-- b000272 | prose | pages [11] -->
where T  λ = (19) λ1 λ2 λ3

<!-- b000273 | prose | pages [11] -->
where λ is the vector of co-state variables, L is the integrand in the cost function J in Equation (16), and f is the vector on the right hand side of the state equations with components represented in Equations (11), (12), and (15).

<!-- b000274 | prose | pages [11] -->
When such an inequality restriction on control and state variables exists, the Hamiltonian equa- tion must be supplemented as follows, H = L+λ T f + µC (20)

<!-- b000275 | prose | pages [11, 12] -->
where ( ⩾0 C = 0 (21) µ = 0 C < 0 Additionally, the upper and lower limits on v and w presented in Equation (17) should be taken into account as,   v(t)−vmax −v(t) ⩽0  S(v,w) = (22) w(t)−W ′ −w(t) In this case, the first derivative of S(v,w) with respect to both v and w includes u. Then, we can treat S(1)(v;w) similar to C(v,w) and augment the Hamiltonian as follows, H = L+λ T f + µC +ηTS(1) (23) T must obey the following conditions,  where η = η1 η2 η3 η4 ⩾0 S(1) ( = 0 i for i = 1,2,3,4 (24) ηi = 0 S(1) < 0 i It should be emphasized that when restrictions are fulfilled, the Hamiltonian terms C and T S(1) will always be zero. The dynamics of the co-states are shown below, λ T = −Hx = −Lx −λ T fx −µCx −ηTS(1) (25) x

<!-- b000276 | furniture | pages [12] -->
Team # 2209812

<!-- b000277 | furniture | pages [12] -->
Page 12 of 24

<!-- b000279 | prose | pages [12] -->
Its expanded version will be,  dθ(s) ˙λ1 = λ2gmb ds (cos(θ (s))−CR sin(θ (s)))  m     ˙λ2 = −λ1 −λ2 u v2 −CdρAv (26) mt  ˙λ3 = 0   The maximum value of u minimizes the function. We can consider four cases, Case I. λ2 λ2 mv −λ3 < 0 AND mv −aλ3 < 0 The slope is negative in both the fatigue and recovery modes, indicating that the greatest value of u in each instance minimizes the Hamiltonian. The maximum input value in the fatigue mode is umax, while the maximum input value in the recovery mode is CP. The control with the least Hamiltonian is the best of the two,

<!-- b000280 | prose | pages [12] -->
 H∗= min Hfatigue (umax),Hrecovery (CP) (27)

<!-- b000281 | prose | pages [12] -->
where the subscripts of H distinguish between fatigue and recovery modes due to the somewhat differing equations of the two modes. We can’t tell which Hamiltonian is smaller by substituting the aforementioned u values. The ideal input may be written as, ( umax Hfatigue (umax) < Hrecovery (CP) u∗= (28) CP Hfatigue (umax) > Hrecovery (CP)

<!-- b000282 | prose | pages [12] -->
Note that in the event Hfatigue(umax) = Hrecovery(CP), both u = CP and u = umax are optimal.

<!-- b000283 | prose | pages [12] -->
The solutions of Case II. λ2 mv −aλ3 > 0, Case III. λ2 λ2 λ2 mv −λ3 > 0 AND mv −λ3 > 0 AND mv − aλ3 < 0 and Case IV. λ2 λ2 mv −λ3 < 0 AND mv −aλ3 > 0 are based on same methods.

<!-- b000284 | prose | pages [12] -->
Thus after considering all of the cases discussed above, the optimal power trajectory can only take values from the vector below,   umax u˙v=0   u∗= (29) CP 0

<!-- b000285 | prose | pages [12] -->
which is the equation provides the necessary conditions for optimality of u since it was based on a PMP analysis.

<!-- b000286 | heading | pages [12] -->
3.3.4 Numerical Solution of the Problem

<!-- b000287 | prose | pages [12, 13] -->
With a zero-order hold on input in between sampling intervals, the following discretized state- space equations are obtained, ti+1 = ti + ∆s (30) vi  ui  −g(sin(θi)+ µ cos(θi))−0.5CdρA vi+1 = vi + ∆s v2 (31) i vi mtvi mt ( ui ⩾CP wi+1 = wi + ∆s vi (CP−ui) (32) wi+1 = wi + ∆s vi (CP−aui −b) ui < CP The cost function in Equation (16) is rewritten with position as the independent variable and discretized as follows, i=N ∆si JN = ∑ (33) vi i=0 According to the Bellman’s principle of optimality [16], when a system is on an optimum path from an initial state to a final state, it should follow an optimal policy throughout the duration of the trip, independent of any previous choice or condition. To discover the ideal state trajectory in dynamic programming, one may start at the final state and work backward, calculating the optimal cost-to-go from any state to the last step. J∗ i+1,N stores the optimum costs and control inputs from all of the feasible (v,w) nodes at si+1 to the end state at sN. Among them, J∗ Ji,i+1 +J∗   i,N = min i+1,N (x) (34) ui where

<!-- b000288 | furniture | pages [13] -->
Team # 2209812

<!-- b000289 | furniture | pages [13] -->
Page 13 of 24

<!-- b000291 | prose | pages [13] -->
J∗ i+1,N = uiui+1,···,uN−1 [Ji+1,N] min (35)

<!-- b000292 | prose | pages [13] -->
The dynamic programming for Behrman’s equation is shown below,

<!-- b000293 | prose | pages [13] -->
Initialize array 𝑣 arbitrarily (e.g., 𝑣(𝑠)=0 for all s 𝑆+

<!-- b000294 | prose | pages [13] -->
Repeat

<!-- b000295 | prose | pages [13] -->
For each s 𝑆+:

<!-- b000296 | prose | pages [13] -->
Until (a small positive number)

<!-- b000297 | prose | pages [13] -->
Output a deterministic policy, , such that

<!-- b000298 | heading | pages [13] -->
3.4 Apply Model to Time Trial Courses

<!-- b000299 | prose | pages [13] -->
3.4.1 Determine the Constants’ Values. ▶The Resistance

<!-- b000300 | prose | pages [13, 14] -->
It’s common knowledge that if we ride upright in a high wind, we’ll face a lot of resistance. Pro- fessional cyclists typically ride prone to reduce wind resistance, with the following riding posture: lower upper body, head slightly tilted forward; arms naturally bent to facilitate lumbar arch flexion, lowering the body’s center of gravity and preventing the transmission of impact to the entire body due to car bumps; hands lightly but firmly grip the handle, hips firmly on the car seat. The frontal Area (A) and drag coefficient (Cd) of various posture of cyclist are shown in Figure 9.

<!-- b000301 | furniture | pages [14] -->
Team # 2209812

<!-- b000302 | furniture | pages [14] -->
Page 14 of 24

<!-- b000304 | prose | pages [14] -->
Thus, Cd = 0.88, A =3.9 ft2. And in general, ρ = 1.29 kg/m3, CR = 0.015. They will be using in Equation (12) and (13).

<!-- b000305 | prose | pages [14] -->
Bikes Frontal Area Drag Coefficient

<!-- b000306 | prose | pages [14] -->
A = 5.5 ft2 Upright commuter 1.10

<!-- b000307 | prose | pages [14] -->
A = 3.9 ft2 Racing 0.88

<!-- b000308 | prose | pages [14] -->
A = 3.9 ft2 Drafting 0.50

<!-- b000309 | prose | pages [14] -->
A = 5.0 ft2 Streamlined 0.12

<!-- b000310 | caption | pages [14] -->
Figure 9: The Effect of Posture on Air Resistance

<!-- b000311 | prose | pages [14] -->
▶The Effective Mass

<!-- b000312 | prose | pages [14] -->
In Equation (14), for the sake of standardization and ease of calculation, we assume that the bicycles covered in this article are all the same, where two wheels of the same size, both with a radius of 0.35 m, weigh 1.2 kg, so that the Iw of each wheel is 0.147 kg·m2. Thus the effective mass (m) of the bicycle and the cyclist is to be about 2.3 kg larger than their actual weight (mb).

<!-- b000313 | heading | pages [14] -->
3.4.2 Simulation Results and Analysis

<!-- b000314 | prose | pages [14] -->
Using processed data of STRAVA-Tokyo2020 and STRAVA-BelgiumUCI in Table 2 and the power curve in Figure 7, we obtained the optimal power profile for cyclists at the Tokyo Olympics (men and women are in different courses) and at the UCI World Championship’s individual time trial courses, which are shown in Figure 10 and 11 below,

<!-- b000315 | prose | pages [14] -->
SM SW SM

<!-- b000316 | prose | pages [14] -->
TM TW TM SW

<!-- b000317 | prose | pages [14] -->
SW

<!-- b000318 | prose | pages [14] -->
(a) Men (b) Women

<!-- b000319 | caption | pages [14] -->
Figure 11: TTC of UCI

<!-- b000320 | caption | pages [14] -->
Figure 10: TTC of Tokyo Olympic

<!-- b000321 | prose | pages [14] -->
where in every subfigure, the upper part is the curve of power P with respect to distance s, and the lower part is the curve of elevation with respect to s.

<!-- b000322 | furniture | pages [15] -->
Team # 2209812

<!-- b000323 | furniture | pages [15] -->
Page 15 of 24

<!-- b000324 | caption | pages [15] -->
Figure 12 shows a course of own design located in the Italy’s San Felice Circeo, along the

<!-- b000325 | prose | pages [15] -->
suburbs and beach. The route begins in the south along the sea (bottom of the image), circles the city, and returns to the starting place, which is also the ultimate destination. The whole race decreases in height and then maintains a distance before descending a sharp slope to the finish line, with a total length of around 16 kilometers (Figure 13). In the same way as above, we obtain the optimal power profile for cyclists at this couse in Figure 13 below.

<!-- b000326 | prose | pages [15] -->
SM

<!-- b000327 | prose | pages [15] -->
TM

<!-- b000328 | prose | pages [15] -->
SW

<!-- b000329 | prose | pages [15] -->
SW

<!-- b000330 | caption | pages [15] -->
Figure 12: A Course of Own Design

<!-- b000331 | caption | pages [15] -->
Figure 13: TTC of Own Design

<!-- b000332 | prose | pages [15] -->
In addition, the minimised time cost of four cyclists in three location show in Table 3 below:

<!-- b000333 | caption | pages [15] -->
Table 3: Minimised Time Cost (s)

<!-- b000334 | prose | pages [15] -->
Cyclist Tokyo Olympic UCI Own Design

<!-- b000335 | prose | pages [15] -->
Time Trial Specialist, Man 3641.49 3258.93 1280.11 Time Trial Specialist, Woman 1984.51 3373.95 1321.25 Sprinter, Man 4117.69 3407.07 1322.85 Sprinter, Woman 3027.01 3528.34 1497.89

<!-- b000336 | prose | pages [15] -->
In summary, we can conclude the following,

<!-- b000337 | prose | pages [15] -->
• The model advocates utilizing as much power as possible at the start of a race, regardless of the kind of athlete. However, after a certain distance, aim to maintain the power at critical power. This implies that putting in a respectable all-out effort at the start of the race will have little effect on the backstretch.

<!-- b000338 | prose | pages [15] -->
• As we can see, for all power profiles, the model suggests that cyclists ride uphill with a particular level of power then ride downhill with as little power as possible while maintaining pace. Therefore, in the actual race, cyclists should make reasonable use of riding downhill to rest and have some physical preparation for the upcoming ride uphill.

<!-- b000339 | furniture | pages [16] -->
Team # 2209812

<!-- b000340 | furniture | pages [16] -->
Page 16 of 24

<!-- b000341 | heading | pages [16] -->
4 TASK 3 & 4: Sensitivity to Weather and Power Distribution’s

<!-- b000342 | prose | pages [16] -->
Deviations

<!-- b000343 | heading | pages [16] -->
4.1 The influence of the weather

<!-- b000344 | prose | pages [16] -->
In cycling, the weather is often unpredictable. Gusty winds, high temperature, and other weather changes can have an impact on competitors. Thus exploring the cyclist’s sensitivity to weather is of great significance in guiding the race.

<!-- b000345 | heading | pages [16] -->
4.1.1 Wind Influence

<!-- b000346 | prose | pages [16] -->
The following Figure 14 has shown wind effect to a cyclist,

<!-- b000347 | prose | pages [16] -->
North North Direction Direction

<!-- b000348 | caption | pages [16] -->
Figure 14: Wind Effect to a Cyclist

<!-- b000349 | prose | pages [16] -->
where ϕ is the angle of wind direction with due north direction, and γ is the angle of cycling direction with due north direction. As the Assumption 2 in Section 2.1 says, we should neglect lateral effect and deviation. Thus we equate the drag force on the cyclist to the drag force on them in the cycling direction, FW = 1 2mCdρA[v−V cos(γ −ϕ)]2 (36)

<!-- b000350 | prose | pages [16] -->
where FW is the drag force. ▶Result

<!-- b000351 | prose | pages [16] -->
Based on Equation (36) above, the minimum time and optimal energy distribution of the athletes in section 3.4.2 were re-optimized for different wind directions and wind velocities in different time trial courses (TTC) , and the results were obtained as shown in the following Figure 15, where the velocity axis represents the magnitude of the velocity of the wind along its direction, and the angle axis represents the magnitude of the angle between the wind direction and the direction due north, and the influence axis represents the percentage of affected (includes positively and negatively) on the corresponding courses for all female cyclists.

<!-- b000352 | prose | pages [16, 17] -->
In the Figure 15, what we can see is that the results of TTC of Tokyo Olympic (Figure 15a) and own design (Figure 15b) are irregular while their route is close to a rectangular. However, the UCI World Championship (Figure 15c) is regular, which shows that when the wind direction is from north to south or south to north (wind direction is close to 0), the biggest effect occurs. And the larger the wind speed, the greater the impact that is more sensitive to wind. In summary, the model of sensitivity to wind effect is up to corresponding course. The closer the course is to a bar or strip, the more regular the wind direction and velocity is to the cyclist, otherwise the more uncertain it is.

<!-- b000353 | furniture | pages [17] -->
Team # 2209812

<!-- b000354 | furniture | pages [17] -->
Page 17 of 24

<!-- b000356 | prose | pages [17] -->
(a) Tokyo Olympic (b) UCI World Championship (c) Own Design

<!-- b000357 | caption | pages [17] -->
Figure 15: Wind Effect to Defferent TTCs (Up is the north)

<!-- b000358 | heading | pages [17] -->
4.1.2 Temperature Influence

<!-- b000359 | prose | pages [17] -->
The first thing that is affected by the temperature t (◦C) change is the air pressure and air density. From Equation (ddd), it is shown that they have a great influence on the power profile of the cyclist. According to air pressure p (Pa) relationship with the altitude h (m),

<!-- b000360 | prose | pages [17] -->
p = −0.011h+100.8 (37)

<!-- b000361 | prose | pages [17] -->
and the air density is, ρ = 1.293p 273.15 101.325 × (38) 273.15+t where t = t0 −0.6h (39) 100 where t0 is the temperature when the h = 0. Therefore,

<!-- b000362 | prose | pages [17] -->
ρ = f(t0,h) (40)

<!-- b000363 | prose | pages [17] -->
Based on these, we use the data of women time trail specialist in Tokyo Olympic. Then we assume that match the expected temperature is 20◦C, change the temperature in steps of 0.5 degrees in the positive and negative directions, and finally we obtain the sensitivity to temperature in Figure (16) below, where the positive effect indicates that the cyclist spends less time and, conversely, more time.

<!-- b000364 | furniture | pages [18] -->
Team # 2209812

<!-- b000365 | furniture | pages [18] -->
Page 18 of 24

<!-- b000366 | caption | pages [18] -->
Figure 16: Sensitivity to Temperature

<!-- b000367 | prose | pages [18] -->
So, under normal temperatures in non-extreme environments, the lower the temperature, the better for cyclists in general. Therefore, for cyclists, keeping their equipment light, being aware of hydration and wearing sportswear that facilitates heat dissipation are ways to help them achieve better results.

<!-- b000368 | heading | pages [18] -->
4.2 The Influence of Power Distribution’s Deviation

<!-- b000369 | heading | pages [18] -->
4.2.1 Sensitivity of Deviation Probability

<!-- b000370 | prose | pages [18] -->
In this section, the ideal energy distribution (section (3.4.2)) is discretized into several sample points. We assume that each sampling point has a probability p of having an power shift. Using data from the Tokyo women’s time trial course, multiple minimum times were measured at different p.

<!-- b000371 | caption | pages [18] -->
Figure 17: Average Minimum Time Cost and Cost Percentage for Deviation Probability

<!-- b000372 | caption | pages [18] -->
Figure 17 shows a scatter plot with time cost and cost percentage respect to different time point

<!-- b000373 | prose | pages [18, 19] -->
and the average time point curve. Therefore, what we can conclude is that the greater deviation probability, the greater the time cost and the trend of time cost. In other words, an athlete’s inconsistent form will cause them to go in a bad direction. As a consequence, keeping his or her pacing during the race is critical for a cyclist to achieving a positive outcome.

<!-- b000374 | furniture | pages [19] -->
Team # 2209812

<!-- b000375 | furniture | pages [19] -->
Page 19 of 24

<!-- b000377 | heading | pages [19] -->
4.2.2 Sensitivity of Location Deviation

<!-- b000378 | prose | pages [19] -->
In the same way as in Section 4.2, the women’s time trail course of the Tokyo Olympics was divided into multiple sections (one section every 2 km) under an ideal energy distribution. Assume that the probability of energy shift is p (p = 0.1), and multiple measurements are taken to obtain multiple minimum times under each section. The scatter plot and radar plot of the effect of energy offset on the minimum time for each section are drawn as follows,

<!-- b000379 | caption | pages [19] -->
Figure 18: Curve for Location Deviation

<!-- b000380 | caption | pages [19] -->
Figure 19: Radar Plot for Location Deviation

<!-- b000381 | prose | pages [19] -->
Figures (18) and (19) demonstrate how cyclists are influenced by deviations in the energy dis- tribution over various regions of the same deviation probability. The cyclists are clearly impacted more in the uphill parts of the 10-12km, 12-14km, and 16-18km. However, t he cyclists are less impacted by the variation of energy distribution in the downhill parts of 4-6km, 8-10km, and 14- 16km. The following table shows the ideal time of arrival at these critical points in time and the deviations caused by the impact,

<!-- b000382 | caption | pages [19] -->
Table 4: Critical Point

<!-- b000383 | prose | pages [19] -->
Arrival Time (s) Arrival Time (s) Point Point 468.05±8.66 1196.94±33.84 6 km 14 km 608.76±14.95 1334.84±36.20 8 km 16 km 795.81±18.10 1636.44±42.49 10 km 18 km 1023.94±25.97 12 km

<!-- b000384 | prose | pages [19] -->
Based on these, we can conclude that a cyclist who does not have a proper power distribu- tion while riding uphill will have a greater impact, although violating his energy distribution limit when riding downhill will not have a significant influence. Therefore, to attain better out- comes, bikers should aim to maintain their pedaling rhythm while riding uphill, while resting and attempting to maintain high speed when riding downhill.

<!-- b000385 | furniture | pages [20] -->
Team # 2209812

<!-- b000386 | furniture | pages [20] -->
Page 20 of 24

<!-- b000387 | heading | pages [20] -->
5 TASK 5: Optimal Power Use for a Team Time Trial

<!-- b000388 | heading | pages [20] -->
5.1 The Benefit of Team Riding

<!-- b000389 | prose | pages [20] -->
▶Reduce Resistance

<!-- b000390 | prose | pages [20] -->
As shown in Figure 20 below, in a cycling team race, the first person will have the largest windward area, and will therefore suffer the greatest wind resistance. And, in this case, this cyclist must also maintain a certain speed to lead the team forward.

<!-- b000391 | caption | pages [20] -->
Figure 20: An Overview of Cycling Team for the Impact of Air Resistance [15]

<!-- b000392 | prose | pages [20] -->
Each cyclist in a team has a different air resistance, D = 1 2ρCdrCdAv2 (41)

<!-- b000393 | prose | pages [20] -->
where Cdr is coefficient of drag reduction and Cd is coefficient of drag. ▶Maximize the Team Power

<!-- b000394 | prose | pages [20] -->
As presented in figure 21 below, the strategy that is currently most used is to have a fixed order where every cyclist drives roughly ten to thirty seconds in first position and then changes to last position. In first position the drag is the highest, thus is the required power output is high. Depending on the capability of the cyclist and it’s state at the moment the cyclist will adjust the time spend in that position, shorter ifweaker or tired and longer if stronger or in a more energetic state. Cyclists that are much weaker than the others, are often dropped out of the group during the race.

<!-- b000395 | heading | pages [20] -->
5.2 Team Time Trial Optimization Model

<!-- b000396 | prose | pages [20] -->
In this section, we discuss the team time trail optimization model, where the team consists of six cyclists and the team’s time is determined when the fourth rider crosses the finish line.

<!-- b000397 | prose | pages [20] -->
We assume that the six cyclists are A,B,C,D,E,F. Thus, we develop a optimization model as follows, Z t f u(t) J = dt min (42) t0 where

<!-- b000398 | prose | pages [20, 21] -->
J = f (∆1,∆2,∆3,∆4,∆5,∆6,∆7,∆8) (43) where  ∆1 = L(P0,P1,P2,···)    ∆2 = tfront−A     (44) ∆3 = tfront−B  ···      ∆7 = tfront−F  where L(s) is a function respect to the order of the time, and tfront−A represents the time that A s first.

<!-- b000399 | furniture | pages [21] -->
Team # 2209812

<!-- b000400 | furniture | pages [21] -->
Page 21 of 24

<!-- b000401 | caption | pages [21] -->
Figure 21: Regular Changing Dynamics in a Team Time Trial of Four Cyclists [15]

<!-- b000403 | heading | pages [21] -->
6 Evaluation of Strengths and Weaknesses

<!-- b000404 | heading | pages [21] -->
6.1 Strengths

<!-- b000405 | prose | pages [21] -->
• This article’s model analyzes individual and team competition of cyclists by combining phys- iology, dynamics, and aerodynamics. It also makes extensive use of accurate data for simulation and analysis. The final outcomes are more consistent with common sense and have a high level of confidence.

<!-- b000406 | prose | pages [21] -->
• A number of possibilities were evaluated for the sensitivity analysis. Sensitivity to weather is classified as sensitivity to wind and sensitivity to temperature. The sensitivity to power distribution deviation takes into account the deviation of power profile and the deviation of power profile in each section.

<!-- b000407 | heading | pages [21] -->
6.2 Weaknesses

<!-- b000408 | prose | pages [21] -->
• When estimating the impacts of wind, the effects of air vortices and atmospheric pressure were not fully considered. Because cyclists’ velocity is frequently more than 10m/s and their form is not totally streamlined. As a result of being impacted by the wind and air, an air vortex forms behind it, and the resistance increases due to the action of atmospheric pressure.

<!-- b000409 | furniture | pages [22] -->
Team # 2209812

<!-- b000410 | furniture | pages [22] -->
Page 22 of 24

<!-- b000411 | heading | pages [22] -->
References

<!-- b000412 | references | pages [22] -->
[1] Clarke, David C., and Philip F. Skiba. "Rationale and resources for teaching the mathematical

<!-- b000413 | references | pages [22] -->
modeling of athletic training and performance." Advances in physiology education (2013).

<!-- b000414 | references | pages [22] -->
[2] Gede, Gilbert. Optimal pacing strategies for cyclist time trials. University of California, Davis,

<!-- b000415 | references | pages [22] -->
2014.

<!-- b000416 | references | pages [22] -->
[3] Jones, Andrew M., et al. "Critical power: implications for determination of VO2max and

<!-- b000417 | references | pages [22] -->
exercise tolerance." Med Sci Sports Exerc 42.10 (2010): 1876-90.

<!-- b000418 | references | pages [22] -->
[4] Maturana, Felipe Mattioni, et al. "Critical power: how different protocols and models affect

<!-- b000419 | references | pages [22] -->
its determination." Journal of Science and Medicine in Sport 21.7 (2018): 742-747.

<!-- b000420 | references | pages [22] -->
[5] Vanhatalo, Anni, Andrew M. Jones, and Mark Burnley. "Application of critical power in

<!-- b000421 | references | pages [22] -->
sport." International journal of sports physiology and performance 6.1 (2011): 128-136.

<!-- b000422 | references | pages [22] -->
[6] J. Qiao." Application of power-maintenance time curves and critical power in predicting cy-

<!-- b000423 | references | pages [22] -->
cling performance." Sports Research 42.03(2021):99-104. doi:

<!-- b000424 | references | pages [22] -->
[7] Clarke, David C., and Philip F. Skiba. "Rationale and resources for teaching the mathematical

<!-- b000425 | references | pages [22] -->
modeling of athletic training and performance." Advances in physiology education (2013).

<!-- b000426 | references | pages [22] -->
[8] Morton, R. Hugh. "A new modelling approach demonstrating the inability to make up for lost

<!-- b000427 | references | pages [22] -->
time in endurance running events." IMA Journal of Management Mathematics 20.2 (2009):

<!-- b000428 | references | pages [22] -->
109-120.

<!-- b000429 | references | pages [22] -->
[9] Keller, Joseph B. "Optimal velocity in a race." The American Mathematical Monthly 81.5

<!-- b000430 | references | pages [22] -->
(1974): 474-480.

<!-- b000431 | references | pages [22] -->
[10] Hugh Morton, R. "A 3-parameter critical power model." Ergonomics 39.4 (1996): 611-619.

<!-- b000432 | references | pages [22] -->
[11] Coggan, A. "Creating Your Power Profile" Training Peaks. n.p. 2019. Sat. 19 Feb 2022.

<!-- b000433 | references | pages [22] -->
https://www.trainingpeaks.com/blog/power-profiling/.

<!-- b000434 | references | pages [22] -->
[12] Monod, H., and J. Scherrer. "The work capacity of a synergic muscular group." Ergonomics

<!-- b000435 | references | pages [22] -->
8.3 (1965): 329-338.

<!-- b000436 | references | pages [22] -->
[13] Ashtiani, Faraz, et al. "Optimal Pacing of a Cyclist in a Time Trial Based on Individualized

<!-- b000437 | references | pages [22] -->
Models of Fatigue and Recovery." arXiv preprint arXiv:2007.11393 (2020).

<!-- b000438 | references | pages [22] -->
[14] Ashtiani, Faraz, et al. "Experimental modeling of cyclists fatigue and recovery dynamics en-

<!-- b000439 | references | pages [22] -->
abling optimal pacing in a time trial." 2019 American Control Conference (ACC). IEEE,

<!-- b000440 | references | pages [22] -->
2019.

<!-- b000441 | references | pages [22] -->
[15] Overtoom, Mats. "Optimal Team Time Trial Strategy in Road Cycling: Optimisation of

<!-- b000442 | references | pages [22] -->
Changing Strategy using a Mathematical Performance model." (2013).

<!-- b000443 | references | pages [22] -->
[16] Behrman, Richard E., and Stuart E. Dreyfus. Applied dynamic programming. Princeton uni-

<!-- b000444 | references | pages [22] -->
versity press, 2015.

<!-- b000445 | furniture | pages [23] -->
Team # 2209812

<!-- b000446 | furniture | pages [23] -->
Page 23 of 24

<!-- b000447 | heading | pages [23] -->
Memo

<!-- b000448 | prose | pages [23] -->
Race Guidance

<!-- b000449 | prose | pages [23] -->
▶How to Use a Power Curve?

<!-- b000450 | prose | pages [23] -->
The value of a power curve is that it shows you the work you’ve done. Since it’s power plotted against time, it gives you a snapshot of your energy systems and a view of your strengths and weaknesses.

<!-- b000451 | prose | pages [23] -->
Every cyclist has strengths and weaknesses. Typical power curves are easily distinguishable. For example, in the chart below, the Sprinter maintains more power for a short period of time, while the Time Trial Specialist maintains more power for a longer period of time. Proper use of power curves allows for more professional guidance to be developed for cyclists.

<!-- b000452 | prose | pages [23] -->
SM SM

<!-- b000453 | prose | pages [23] -->
TM TM

<!-- b000454 | prose | pages [23] -->
SW SW TW TW

<!-- b000455 | prose | pages [23] -->
TM TM TM SM SM TW TW TW SM SW SW SW

<!-- b000456 | prose | pages [23] -->
▶How to Determine Pacing of a Cyclist?

<!-- b000457 | prose | pages [23] -->
Three principles for pacing:

<!-- b000458 | prose | pages [23] -->
• No matter what happens, keep yourself first pacing rhythm

<!-- b000459 | prose | pages [23] -->
Keeping his or her pacing during the race is critical for a cyclist to achieving a positive outcome. In addition, from a psychological point of view, the stable pacing can improve self-confidence.

<!-- b000460 | prose | pages [23] -->
• putting in a respectable all-out effort at the start of the race.

<!-- b000461 | prose | pages [23] -->
At the start of a race, enough speed makes the cyclist not easy to lag behind. And it doesn’t has a great influence to the rest journey.

<!-- b000462 | prose | pages [23] -->
• making reasonable use of riding downhill to rest and having some physical preparation for the upcoming ride uphill

<!-- b000463 | prose | pages [23] -->
The ride uphill part takes cyclists more time and energy, and has a greater impact, if cyclists’ power profile deviations happen. However, the ride downhill part, it allows cyclists have more time to rest with easy ride. ▶How to keep Stamina in a Time Trial?

<!-- b000464 | prose | pages [23, 24] -->
• Maintain the speed and pay attention to rest on your way down • As far as possible follow behind the other players

<!-- b000465 | furniture | pages [24] -->
Team # 2209812

<!-- b000466 | furniture | pages [24] -->
Page 24 of 24

<!-- b000468 | prose | pages [24] -->
▶How to Prepare for a Cycling Race?

<!-- b000469 | prose | pages [24] -->
• Check the course

<!-- b000470 | prose | pages [24] -->
On the one hand, Familiar with the course help cyclists determine power distribution to prevent deviations. On the other hand, it also help cyclists determine which direction of wind influence most.

<!-- b000471 | prose | pages [24] -->
• Before the game to keep rest, pay attention to diet, make oneself of the stable condition

<!-- b000472 | prose | pages [24] -->
• Check the weather ahead of time

<!-- b000473 | prose | pages [24] -->
The weather forecast will tell the wind velocity and direction and temperature change in the race day. Based on it, what you need to do is to prepare. For example, prepare to cool down if meets the high temperature weather

<!-- b000474 | prose | pages [24] -->
• Choosing the suitable equipment

<!-- b000475 | prose | pages [24] -->
Heavy cycle will become the biggest burden of cyclists. Suitable equipment help cyclists against the situation not expected.
