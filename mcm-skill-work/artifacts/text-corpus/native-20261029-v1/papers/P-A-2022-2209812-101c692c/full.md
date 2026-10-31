# P-A-2022-2209812-101c692c

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
2209812

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Power Curve Make Cyclists Faster and Faster

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Every ride has a pace—whether or not you’re in control of that pace all comes down to essential planning based on his or her power profile. In this paper, we develop models to guide cycling races based on power curves (PC), measure the sensitivity to weather and power distribution’s deviation, and optimal power use for a team time trial.

<!-- b000011 | prose | pages [1] -->
In Task 1 & 2: First, we choose a three-parameter hyperbolic model based on exercise physi- ology that is more accurate in the critical power (CP) model. Based on it, we utilize data to define the PC of male and female time trial specialists, male and female sprinters (Figure 7). Among them, the sprinters have higher explosive power, but the time trial specialists (TTS) have more long-term endurance, and female players have less explosive power and endurance than male players.

<!-- b000012 | prose | pages [1] -->
After that, we found out the fatigue and recovery (FR) model, forming optimal pacing control. Then we obtain the necessary condition based on the Pontryagin’s Minimum Principle (PMP) and the numerical solution of Behrman equation based on dynamic programming (DP) and Behrman’s principle. We apply the PC to the time trial course of Tokyo Olympic, UCI World Championship and own design, which is located at Italy’s San Felice Circeo (Figure 12), and the power distribution of cyclists are shown in Figure 10, 11, and 13. We found this result to be consistent with the characteristics of the cyclists above, which including the duration of man time trial specialist in Tokyo Olympic is 1h:41m:29.4s (3641.49 s), and the woman is 0h:33m:4.51s (1984.51 s).

<!-- b000013 | prose | pages [1] -->
In Task 3 & 4: in this section, we measure the sensitivity of our model to weather and power distribution’s deviation.

<!-- b000014 | prose | pages [1] -->
For wind, the sensitivity to wind effect is up to corresponding course. The closer the course is to a bar or strip, the more regular the wind direction and velocity is to the cyclist, otherwise the more uncertain it is. For temperature influence, in a suitable range, the lower the temperature, the better for cyclists. Thus, cyclists should observe the terrain well, make reasonable use of the wind direction, and pay attention to do certain heat dissipation measures.

<!-- b000015 | prose | pages [1] -->
For power distribution’s deviation, the greater deviation probability, the greater the time cost and the trend of time cost.Therefore, maintaining good pacing stability is the key to getting good results. For power deviations occurring on different sections, the impact on cyclists is more sensi- tive when the elevation is more undulating, and less so when the undulation is smaller. Maintaining their pedaling rhythm while riding uphill, while resting and attempting to maintain high speed when riding downhill are significant to cyclists.

<!-- b000016 | prose | pages [1] -->
In Task 5: this section shows how team riding reduces resistance and maximizes the team power. We found that the real-time position of the cyclist in the team and the time the cyclist lead each time are key factors in determining the team’s performance. Based on them, we develop a team time trial Optimization Model to maximize power use.

<!-- b000017 | prose | pages [1] -->
Finally, we evaluate the strengths and weaknesses of model. And a two-page rider’s race guid- ance has been written for a Directeur Sportif.

<!-- b000018 | keywords | pages [1] -->
Keywords: Power Curve, Dynamics Analysis, DP, PMP, Behrman Equation.

<!-- b000019 | furniture | pages [2] -->
Team # 2209812

<!-- b000020 | furniture | pages [2] -->
Page 2 of 24

<!-- b000021 | heading | pages [2] -->
Contents

<!-- b000022 | contents | pages [2] -->
1

<!-- b000023 | heading | pages [2] -->
Introduction

<!-- b000024 | prose | pages [2] -->
3 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000025 | prose | pages [2] -->
2

<!-- b000026 | heading | pages [2] -->
Preparation of the Models

<!-- b000027 | prose | pages [2] -->
4

<!-- b000028 | prose | pages [2] -->
4 Assumptions and Explanations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000029 | heading | pages [2] -->
Notations

<!-- b000030 | prose | pages [2] -->
5 The Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 5 Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.1 5 Data Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.2 5

<!-- b000031 | prose | pages [2] -->
TASK 1 & 2: Guiding Cycling Races Based on Power Curves 3 6 The Critical Power Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 6 The 2-parameter Hyperbolic Model . . . . . . . . . . . . . . . . . . . . . 3.1.1 6 The 3-parameter Hyperbolic Model . . . . . . . . . . . . . . . . . . . . . 3.1.2 7 Define the Power Profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 7 Optimal Pacing of a Cyclist . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 3.3.1 Fatigue and Recovery of Cyclists 3.3.2 Optimal Control Formulation 8 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | prose | pages [2] -->
8 . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | prose | pages [2] -->
9 Necessary Condition for Optimal Solution . . . . . . . . . . . . . . . . . . 3.3.3 11 Numerical Solution of the Problem 3.3.4 3.4 Apply Model to Time Trial Courses . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | prose | pages [2] -->
12 . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | prose | pages [2] -->
13 Determine the Constants’ Values. 3.4.1 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | prose | pages [2] -->
13 Simulation Results and Analysis . . . . . . . . . . . . . . . . . . . . . . . 3.4.2 14

<!-- b000037 | heading | pages [2] -->
TASK 3 & 4: Sensitivity to Weather and Power Distribution’s Deviations

<!-- b000038 | prose | pages [2] -->
4 16 The influence of the weather . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 16 Wind Influence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 16 Temperature Influence . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 17 The Influence of Power Distribution’s Deviation . . . . . . . . . . . . . . . . . . . 4.2 18 Sensitivity of Deviation Probability . . . . . . . . . . . . . . . . . . . . . 4.2.1 4.2.2 Sensitivity of Location Deviation 18 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | prose | pages [2] -->
19

<!-- b000040 | prose | pages [2] -->
TASK 5: Optimal Power Use for a Team Time Trial 5 20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 The Benefit of Team Riding 5.2 Team Time Trial Optimization Model

<!-- b000041 | prose | pages [2] -->
6

<!-- b000042 | heading | pages [2] -->
Evaluation of Strengths and Weaknesses

<!-- b000043 | prose | pages [2] -->
20 . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | prose | pages [2] -->
20

<!-- b000045 | prose | pages [2] -->
21 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Strengths 21 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000046 | heading | pages [2] -->
References

<!-- b000047 | heading | pages [2] -->
Memo

<!-- b000048 | prose | pages [2] -->
21

<!-- b000049 | prose | pages [2] -->
21

<!-- b000050 | prose | pages [2] -->
23

<!-- b000051 | furniture | pages [3] -->
Team # 2209812

<!-- b000052 | prose | pages [3] -->
1

<!-- b000053 | heading | pages [3] -->
Introduction

<!-- b000054 | prose | pages [3] -->
1.1 Problem Background

<!-- b000055 | furniture | pages [3] -->
Page 3 of 24

<!-- b000056 | prose | pages [3] -->
Every cyclist knows that time and intensity are inextricably linked. For example, sprinting for more than a few seconds is very difficult, yet easy endurance riding may be continued for several hours with correct feeding. A power curve (PC) is a representation of this relationship, and viewing it might provide valuable information about your relative strengths and limitations.

<!-- b000057 | prose | pages [3] -->
The cyclists might use the PC to determine how much power applies based on the rider’s loca- tion on the race. In this problem, we need to accomplish the following objectives:

<!-- b000058 | prose | pages [3] -->
• Define the power profiles of a time trial specialist and another type of rider while accounting for gender. Then put the model to the test on a variety of time trial courses.

<!-- b000059 | prose | pages [3] -->
• Determine the weather’s possible influence and sensitivity, as well as how sensitive the results are to rider deviations from the target power distribution.

<!-- b000060 | prose | pages [3] -->
• Extend the model to include optimal power use for a six-rider team time trial, with the team’s time being calculated after the fourth rider crosses the finish line.

<!-- b000061 | prose | pages [3] -->
1.2 Literature Review

<!-- b000062 | prose | pages [3] -->
This question is maily about guide cyclist according to PC. In the last few years, there has been a hot line of research in both the analysis of cyclists from a physiological perspective and the optimization of cycling competition from a race perspective. Thus, this section focuses on the main models in these two aspects.

<!-- b000063 | prose | pages [3] -->
• Above all, in terms of power curve description, one is a simple two-parameter critical power (CP) model with inappropriate physiological assumptions [5], whereas the other is a somewhat more difficult but more physiologically acceptable three-parameter CP model [10].

<!-- b000064 | prose | pages [3] -->
• Regarding the optimization of the cyclist’s pace, the relationship between power distribution and power curve can be analyzed starting from the physiological model of fatigue and recovery [13]. It effectively explains the dynamic equilibrium process of fatigue and recovery of cyclists in the course of a race.

<!-- b000065 | prose | pages [3] -->
• In terms of optimizing the cyclist’s speed, Ashtiani, Faraz, et al. [13] proposed a dynamics- based optimization model. It not only contains the force model of a cyclist, but also takes the effect of weather into full consideration.

<!-- b000066 | prose | pages [3] -->
• The aerodynamic interaction between cyclists is very important to the effectiveness of a strat- egy, whick is the key to team strategy in team time trial.

<!-- b000067 | heading | pages [3] -->
2-parameter CP Model

<!-- b000068 | prose | pages [3] -->
Physiology

<!-- b000069 | prose | pages [3] -->
Simple, Inappropriate

<!-- b000070 | heading | pages [3] -->
3-parameter CP Model

<!-- b000071 | prose | pages [3] -->
Cyclists' race strategy

<!-- b000072 | prose | pages [3] -->
Complex, appropriate

<!-- b000073 | prose | pages [3] -->
Task 1

<!-- b000074 | heading | pages [3] -->
Fatigue-Recovery Model

<!-- b000075 | prose | pages [3] -->
Dynamics

<!-- b000076 | heading | pages [3] -->
Pacing Optimization Model

<!-- b000077 | prose | pages [3] -->
Task 2,3

<!-- b000078 | prose | pages [3] -->
Aerodynamic Interaction Team Strategy Task 5

<!-- b000079 | caption | pages [3] -->
Figure 1: Literature Review Framework

<!-- b000080 | furniture | pages [4] -->
Team # 2209812

<!-- b000081 | prose | pages [4] -->
1.3 Our Work

<!-- b000082 | furniture | pages [4] -->
Page 4 of 24

<!-- b000083 | prose | pages [4] -->
The work we have done in this problem is mainly shown in the following Figure (2).

<!-- b000084 | prose | pages [4] -->
Guiding Cycling Races Based on Power Curves

<!-- b000085 | prose | pages [4] -->
Guiding Cycling Races Based on Power Curves

<!-- b000086 | heading | pages [4] -->
3-parameter CP Model

<!-- b000087 | heading | pages [4] -->
3-parameter CP Model

<!-- b000088 | prose | pages [4] -->
Fatigue-Recovery Model

<!-- b000089 | prose | pages [4] -->
Fatigue-Recovery Model

<!-- b000090 | prose | pages [4] -->
Dynamics Solution

<!-- b000091 | prose | pages [4] -->
Dynamics Solution

<!-- b000092 | prose | pages [4] -->
Power Profile and Distribution

<!-- b000093 | prose | pages [4] -->
Power Profile and Distribution

<!-- b000094 | prose | pages [4] -->
Processing

<!-- b000095 | prose | pages [4] -->
Processing

<!-- b000096 | heading | pages [4] -->
Sensitivity{

<!-- b000097 | heading | pages [4] -->
Sensitivity{

<!-- b000098 | prose | pages [4] -->
Dynamic Solution

<!-- b000099 | prose | pages [4] -->
Dynamic Solution

<!-- b000100 | prose | pages [4] -->
Optimal Pacing Control

<!-- b000101 | prose | pages [4] -->
Optimal Pacing Control

<!-- b000102 | prose | pages [4] -->
Necessary Condition

<!-- b000103 | prose | pages [4] -->
Necessary Condition

<!-- b000104 | prose | pages [4] -->
Dynamic Programming

<!-- b000105 | prose | pages [4] -->
Dynamic Programming

<!-- b000106 | prose | pages [4] -->
Behrman principle

<!-- b000107 | prose | pages [4] -->
Behrman principle

<!-- b000108 | prose | pages [4] -->
Sensitvity{

<!-- b000109 | prose | pages [4] -->
Sensitvity{

<!-- b000110 | prose | pages [4] -->
Wind Influence

<!-- b000111 | prose | pages [4] -->
Wind Influence

<!-- b000112 | prose | pages [4] -->
Weather

<!-- b000113 | prose | pages [4] -->
Weather

<!-- b000114 | prose | pages [4] -->
Deviation Probability

<!-- b000115 | prose | pages [4] -->
Deviation Probability

<!-- b000116 | prose | pages [4] -->
Deviations

<!-- b000117 | prose | pages [4] -->
Deviations

<!-- b000118 | prose | pages [4] -->
Temperature Influence

<!-- b000119 | prose | pages [4] -->
Temperature Influence

<!-- b000120 | prose | pages [4] -->
data

<!-- b000121 | prose | pages [4] -->
data

<!-- b000122 | prose | pages [4] -->
Location Deviation

<!-- b000123 | prose | pages [4] -->
Location Deviation

<!-- b000124 | prose | pages [4] -->
Optimal Power Use for a Team Time Trial

<!-- b000125 | prose | pages [4] -->
Optimal Power Use for a Team Time Trial

<!-- b000126 | heading | pages [4] -->
Optimization Model

<!-- b000127 | heading | pages [4] -->
Optimization Model

<!-- b000128 | prose | pages [4] -->
Maximize the Team Power

<!-- b000129 | prose | pages [4] -->
Maximize the Team Power

<!-- b000130 | prose | pages [4] -->
Reduce Resistence

<!-- b000131 | prose | pages [4] -->
Reduce Resistence

<!-- b000132 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000133 | prose | pages [4] -->
2

<!-- b000134 | heading | pages [4] -->
Preparation of the Models

<!-- b000135 | prose | pages [4] -->
2.1

<!-- b000136 | heading | pages [4] -->
Assumptions and Explanations

<!-- b000137 | prose | pages [4] -->
Considering that practical probelms always contain many complex factors, we made the fol- lowing assumptions to help us with our modeling.

<!-- b000138 | prose | pages [4] -->
• Assumption 1: Brakes can be neglected [2]. ⇒Explanation: On the one hand, none of the bikes were equipped with a data logging system capable of measuring braking force. On the other hand, the only unwanted braking would be to avoid crashes, which is usually not an issue in individual time trials.

<!-- b000139 | prose | pages [4] -->
• Assumption 2: Lateral movement can be neglected [2]. ⇒Explanation: From an energy point of view, this makes sense. For example, With a lateral velocity of 1 m/s and most of professional cyclists’ speed of more than 10 m/s, the lateral velocity accounts for less than 1% of the total speed.

<!-- b000140 | prose | pages [4] -->
• Assumption 3: Bicycles are all the same size. ⇒Explanation: The Olympic spirit tells us that human body limits and competition results are broken by the athletes themselves, not by their equipment. Therefore, unifying bicycle standards is not just about easy modeling, it’s also part of fair play. The corresponding values for bicycles will be given in Section 3.4.1.

<!-- b000141 | heading | pages [4] -->
• Assumption 4: Cyclists will keep their posture constant during the race

<!-- b000142 | prose | pages [4] -->
⇒Explanation: From an aerodynamic standpoint [2], the resistance area is heavily reliant on the cyclist’s position. Because the cyclist’s posture are always changing, the resistance area should be averaged. At the highest levels of competition, riders develop their unique riding rhythm and maintain a stable posture for extended periods of time. Therefore, it is reasonable to assume that.

<!-- b000143 | furniture | pages [5] -->
Team # 2209812

<!-- b000144 | prose | pages [5] -->
2.2

<!-- b000145 | heading | pages [5] -->
Notations

<!-- b000146 | furniture | pages [5] -->
Page 5 of 24

<!-- b000147 | prose | pages [5] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000148 | caption | pages [5] -->
Table 1: Notations

<!-- b000149 | prose | pages [5] -->
Symbol

<!-- b000150 | prose | pages [5] -->
P CP W ′

<!-- b000151 | prose | pages [5] -->
Description

<!-- b000152 | prose | pages [5] -->
power output critical power available work over CP (anaerobic work capacity) TTE w wrec Trec Pmax s v time-to-exhaustion remaining anaerobic energy recovered anaerobic energy recovery duration maximal power possible cyclist’s traveled distance cyclist’s cycling velocity angle of wind direction with north ϕ angle of cycling direction with north γ V

<!-- b000153 | prose | pages [5] -->
2.3 The Data

<!-- b000154 | prose | pages [5] -->
2.3.1

<!-- b000155 | heading | pages [5] -->
Data Collection

<!-- b000156 | prose | pages [5] -->
wind velocity

<!-- b000157 | prose | pages [5] -->
The data we used mainly include Body data of different types of cyclists, . The data sources are summarized in Table 2 below,

<!-- b000158 | caption | pages [5] -->
Table 2: Data Source Websites

<!-- b000159 | prose | pages [5] -->
Database Names Database Websites

<!-- b000160 | prose | pages [5] -->
https://www.trainingpeaks.com/blog/power-profiling/ Training Peaks https://www.strava.com/activities/5678015293 STRAVA-Tokyo2020 https://www.strava.com/activities/6006887196 STRAVA-BelgiumUCI

<!-- b000161 | prose | pages [5] -->
where data of Training Peaks includes cyclists’ power of different genders and types at 5 s, 1 minute, 5 minutes, and functional threshold (FT). And the course data, including latitude, longi- tude and altitude, of STRAVA-Tokyo2020 is at 2021 Olympic Time Trial course in Tokyo, Japan, as well as STRAVA-BelgiumUCI is 2021 UCI World Championship men’s time trial course in Flanders, Belgium on September 22, 2021.

<!-- b000162 | prose | pages [5] -->
2.3.2

<!-- b000163 | heading | pages [5] -->
Data Processing

<!-- b000164 | prose | pages [5] -->
For the course data of STRAVA-Tokyo2020 and STRAVA-BelgiumUCI, we need to discretize the track into multiple locations and get the distance and slope between adjacent locations. More details of data processing are shown in Figure 3 and 4 below.

<!-- b000165 | furniture | pages [6] -->
Team # 2209812

<!-- b000166 | furniture | pages [6] -->
Page 6 of 24

<!-- b000167 | prose | pages [6] -->
Data processing

<!-- b000168 | prose | pages [6] -->
• Obtain the angle between two adjacent locations (approximately

<!-- b000169 | prose | pages [6] -->
step1

<!-- b000170 | prose | pages [6] -->
600m-1000m apart) on the Earth‘s sphere (Figure 3).

<!-- b000171 | prose | pages [6] -->
• Convert the latitude and longitude of two adjacent locations to their straight-line distance.

<!-- b000172 | prose | pages [6] -->
Step2

<!-- b000173 | prose | pages [6] -->
• Obtain the slope of adjacent locations based on straight-line distance and elevation.

<!-- b000174 | prose | pages [6] -->
Step3

<!-- b000175 | caption | pages [6] -->
Figure 3: Data Processing

<!-- b000176 | caption | pages [6] -->
Figure 4: Distance calculation

<!-- b000177 | prose | pages [6] -->
3 TASK 1 & 2: Guiding Cycling Races Based on Power Curves

<!-- b000178 | prose | pages [6] -->
3.1

<!-- b000179 | heading | pages [6] -->
The Critical Power Model

<!-- b000180 | prose | pages [6] -->
It is a common experience that cycling at a relatively fast yet comfortable pace can be continued for a considerable period without undue fatigue. Even a small increase in the speed, however, sig- nificantly increases the perceived effort and drastically limits the tolerated duration of exercise. The fact that these sensations have substantial mathematical and physiological foundations, which are enshrined in the critical power (CP) notion, is probably underappreciated. The CP thus represents an important parameter of aerobic function (in addition to gas exchange threshold (GET), maximal O2 uptake (VO2max), and exercise efficiency) [3]. It also offers a useful framework for studying and better understanding the processes of tiredness and exercises intolerance. Among several current PD models, the 2-parameter hyperbolic (CP2−hyp) model and the 3-parameter hyperbolic (CP3−hyp) model are studied the most [4].

<!-- b000181 | prose | pages [6] -->
3.1.1

<!-- b000182 | heading | pages [6] -->
The 2-parameter Hyperbolic Model

<!-- b000183 | prose | pages [6] -->
From a mathematical point of view, within the severe-intensity domain, the CP is one of two (or three) empirical parameters that establish the link between power output (P) and time-to- exhaustion (TTE). This connection is known to be hyperbolic, with the power-asymptote repre- senting the CP and the curvature constant denoted W ′ (Figure 5a) [5, 6].

<!-- b000184 | prose | pages [6] -->
TTE = W ′/(P−CP) (1)

<!-- b000185 | prose | pages [6] -->
(a) The hyperbolic form (b) The linear form

<!-- b000186 | caption | pages [6] -->
Figure 5: The Two-parameter Model

<!-- b000187 | furniture | pages [7] -->
Team # 2209812

<!-- b000188 | furniture | pages [7] -->
Page 7 of 24

<!-- b000189 | prose | pages [7] -->
where TTE denotes the motion maintenance time at a given power, W ′ is the available work in excess of CP, P is the average power over the duration of the exercise (the equation has another explaination at Section 3.3). CP defines the highest power output to maintain intracellular home- ostasis. The formula can be applied to predict the exercise maintenance time TTE for any given output power above CP, which has great potential application in training. It may also be useful to know which P must be chosen in order to achieve a given TTE. For this purpose the equation 1 is solved for P, thus giving it a linear form (Figure 5b):

<!-- b000190 | prose | pages [7] -->
P = W ′/TTE +CP (2) For example, if we take a hypothetical athlete with a measured CP of 300 W and W ′ of 20 kJ, we can calculate (using Equation (1)) the amount of time that this athlete could sustain a given P.

<!-- b000191 | prose | pages [7] -->
Despite the fact that this 2-parameter hyperbolic CP model can explain a wide range of occur- rences, it still has a number of incorrect assumptions that contravene known physiology [7]. They were presented below:

<!-- b000192 | prose | pages [7] -->
• Power and velocity are not achievable instantaneously. The required power takes 2 minutes or more to become accessible through the oxygen delivery system, and the required velocity takes a few seconds to attain due to body acceleration or biomechanical considerations.

<!-- b000193 | prose | pages [7] -->
• Power continues to decline below the asymptote defined by CP given enough time. The CP model is applicable to activity that lasts between 2 and 30 minutes in most persons, but up to 60 minutes in some.

<!-- b000194 | prose | pages [7] -->
• Power and velocity are not infinite since everyone has a maximum running speed that they can’t exceed [8].

<!-- b000195 | prose | pages [7] -->
• At the point of fatigue, power does not have to be entirely exhausted. The individual in constant-power trials stops exercising when he or she can no longer maintain the required power output.

<!-- b000196 | prose | pages [7] -->
3.1.2

<!-- b000197 | heading | pages [7] -->
The 3-parameter Hyperbolic Model

<!-- b000198 | prose | pages [7] -->
For middle and long distance races, studies had found that a athlete’s unique ideal velocity profile consists of three segments: a brief moment of maximum acceleration, followed by a long period of continuous (but not all-out) pace, and finally a brief period in which the racer collapses exhausted over the finish line [9]. Based on it, to overcome the limitations imposed by the two- parameter CP model’s assumptions, Morton created a three-parameter hyperbolic CP model [10]. The three-parameter model overcomes the assumptions that maximal power output is infinite and that exhaustion occurs when power is depleted. His modification is expressed mathematically as follows:

<!-- b000199 | prose | pages [7] -->
TTE = W ′

<!-- b000200 | prose | pages [7] -->
P−CP +k (3)

<!-- b000201 | prose | pages [7] -->
where k is the asymptote and assumes a negative value. Because the maximal power possible (Pmax) can only occur for instantaneous time (i.e., TTE = 0), it implies the following:

<!-- b000202 | prose | pages [7] -->
W ′ TTE =

<!-- b000203 | prose | pages [7] -->
Pmax P−CP +

<!-- b000204 | prose | pages [7] -->
3.2 Define the Power Profiles

<!-- b000205 | prose | pages [7] -->
(4)

<!-- b000206 | prose | pages [7] -->
CP−Pmax

<!-- b000207 | prose | pages [7] -->
Download the corresponding data from the Training Peaks website in Table 2. The dataset’s de- veloper established the maximum and lower limits of each range based on the known performance capacities of world-class athletes and untrained individuals. It includes cyclists of different genders

<!-- b000208 | furniture | pages [8] -->
Team # 2209812

<!-- b000209 | furniture | pages [8] -->
Page 8 of 24

<!-- b000210 | prose | pages [8] -->
and types at 5 s, 1 minute, 5 minutes, and functional threshold (FT) power, allowing us to fit the CP model based on them (Figure 6) [11].

<!-- b000211 | prose | pages [8] -->
{

<!-- b000212 | prose | pages [8] -->
Male cyclists Time Trialist

<!-- b000213 | prose | pages [8] -->
Data Data

<!-- b000214 | prose | pages [8] -->
Female cyclists Rouleur

<!-- b000215 | prose | pages [8] -->
Pursuiter

<!-- b000216 | prose | pages [8] -->
Fit model with the power

<!-- b000217 | prose | pages [8] -->
Power curve at 1s, 1m, 5m and FT

<!-- b000218 | prose | pages [8] -->
Sprinter

<!-- b000219 | caption | pages [8] -->
Figure 6: Cyclist Data Overview

<!-- b000220 | prose | pages [8] -->
Using some data in Training Peaks (Table 2), the power curves PC of different gender cyclists of time trial specialist and sprinter are shown in the Figure 7.

<!-- b000221 | prose | pages [8] -->
SM

<!-- b000222 | prose | pages [8] -->
SM

<!-- b000223 | prose | pages [8] -->
TM

<!-- b000224 | prose | pages [8] -->
TM

<!-- b000225 | prose | pages [8] -->
SW

<!-- b000226 | prose | pages [8] -->
SW

<!-- b000227 | prose | pages [8] -->
TW

<!-- b000228 | prose | pages [8] -->
TW

<!-- b000229 | prose | pages [8] -->
TM

<!-- b000230 | prose | pages [8] -->
TM

<!-- b000231 | prose | pages [8] -->
SM

<!-- b000232 | prose | pages [8] -->
SM TW

<!-- b000233 | prose | pages [8] -->
TW

<!-- b000234 | prose | pages [8] -->
SW

<!-- b000235 | prose | pages [8] -->
SW

<!-- b000236 | prose | pages [8] -->
TM

<!-- b000237 | prose | pages [8] -->
TW

<!-- b000238 | prose | pages [8] -->
SM

<!-- b000239 | prose | pages [8] -->
SW

<!-- b000240 | caption | pages [8] -->
Figure 7: the Result of Task 1

<!-- b000241 | prose | pages [8] -->
Based on this picture, we can draw some conclusions, which are shown below:

<!-- b000242 | prose | pages [8] -->
• When comparing the power of two kinds of cyclists, the sprinter has more power than the time trial specialist (PS > PT) when the duration is short (Time < 20s). This indicates that, in general, the Sprinter more dominating at the start of the race. However, as time continued to increase, the sprinter lost his edge more and more. It is obvious that when Time > 300s, the time trial specialist has the upper hand, and the longer the time, the more obvious the advantage.

<!-- b000243 | prose | pages [8] -->
• From a gender perspective, female cyclists of the same type will always have weaker power than male cyclists. Even the female sprinter can hardly win the male time trial specialist in terms of explosive power, but over time, the female sprinter can prevail over the male time trial specalist, which shows that the female cyclist’s staying power is not too weak.

<!-- b000244 | prose | pages [8] -->
3.3 Optimal Pacing of a Cyclist

<!-- b000245 | prose | pages [8] -->
3.3.1 Fatigue and Recovery of Cyclists The concept of CP is defined as the maximum power output that can be maintained indefinitely and it’s controled by Equation (1) [12]. W ′ is available work over CP. From the perspective of phys- iology, it also can be explained as anaerobic work capacity. So the Equation (1) means that a cyclist can only maintain that power for a certain period of time before running out of anaerobic energy. During the race, the overall trend of the cyclist’s power decreases, and W ′ gradually recovers when

<!-- b000246 | furniture | pages [9] -->
Team # 2209812

<!-- b000247 | furniture | pages [9] -->
Page 9 of 24

<!-- b000248 | prose | pages [9] -->
the power is less than CP. Therefore, the cyclist is in a dynamic equilibrium based on a dynamic Fatigue-Recovery (PR) model until the final acceleration.

<!-- b000249 | prose | pages [9] -->
As we discussed above, the maximum power a cyclist can produce if he or she maximizes his or her anaerobic work capacity (W ′) is CP. For further explanation, we define w as the remaining W ′ during the ride. As the following Equation (5) shows, the recovery process of w can be similar

<!-- b000250 | prose | pages [9] -->
to its consumption. If the cyclist is pedaling at a constant power (P) below CP for the duration Trec, the actual amount of recovered energy (wrec) will be less than (CP−P)×Trec. Thus, we propose the notion of an adjusted recovery power Pad j as,

<!-- b000251 | prose | pages [9] -->
Pad j = CP−wrec

<!-- b000252 | prose | pages [9] -->
(5)

<!-- b000253 | prose | pages [9] -->
Trec

<!-- b000254 | prose | pages [9] -->
to be used in a switching model of energy expenditure and recovery as follows,

<!-- b000255 | prose | pages [9] -->
(

<!-- b000256 | prose | pages [9] -->
−(P−CP) P ⩾CP

<!-- b000257 | prose | pages [9] -->
dw

<!-- b000258 | prose | pages [9] -->
dt =

<!-- b000259 | prose | pages [9] -->
 

<!-- b000260 | prose | pages [9] -->
(6)

<!-- b000261 | prose | pages [9] -->


<!-- b000262 | prose | pages [9] -->
Pad j −CP

<!-- b000263 | prose | pages [9] -->
−

<!-- b000264 | prose | pages [9] -->
P < CP

<!-- b000265 | prose | pages [9] -->
where P is the pedaling power of the cyclist. We further hypothesize that the recovery power Pad j is solely determined by the pedaling power P and not by the duration Trec. Study shows that Pad j can be well approximated as a linear function of pedaling power P with constants a and b that should be determined for each cyclist [13]. Thus Pad j is defined as,

<!-- b000266 | prose | pages [9] -->
Pad j = aP+b (7)

<!-- b000267 | prose | pages [9] -->
The cyclist’s capacity to create instantaneous maximal power (Pmax) is influenced by W’ ex- penditure. A study [14] discovered the following linear connection between Pmax and anaerobic energy w:

<!-- b000268 | prose | pages [9] -->
Pmax = aw+CP

<!-- b000269 | prose | pages [9] -->
3.3.2 Optimal Control Formulation

<!-- b000270 | prose | pages [9] -->
(8)

<!-- b000271 | prose | pages [9] -->
In this section, pacing of a cyclist is modeled as a restricted optimum control problem. The key dynamic state variables are: i) the cyclist’s remaining anaerobic energy w; ii) the cyclist’s traveled distance s; and iii) the cyclist’s cycling velocity v. The control input is the cyclist’s power at a function of time u(t). Thus the state-space model is of the form:

<!-- b000272 | prose | pages [9] -->
T

<!-- b000273 | prose | pages [9] -->


<!-- b000274 | prose | pages [9] -->
f1 f2 f3

<!-- b000275 | prose | pages [9] -->
˙x = f (x(t),u(t)) =

<!-- b000276 | prose | pages [9] -->
where the state vector is,

<!-- b000277 | prose | pages [9] -->


<!-- b000278 | prose | pages [9] -->
s(t)

<!-- b000279 | prose | pages [9] -->
x(t) =

<!-- b000280 | prose | pages [9] -->
(9)

<!-- b000281 | prose | pages [9] -->
T

<!-- b000282 | prose | pages [9] -->
v(t) w(t)

<!-- b000283 | prose | pages [9] -->
(10)

<!-- b000284 | prose | pages [9] -->
and f is a nonlinear function that maps the input and states to the rate at which they change. f1 is just velocity in Equation (9), so,

<!-- b000285 | prose | pages [9] -->
f1 = ds

<!-- b000286 | prose | pages [9] -->
dt = v (11)

<!-- b000287 | prose | pages [9] -->
And f2 is obtained using Newton’s second law (Figure 8),

<!-- b000288 | prose | pages [9] -->
f2 = dv(t)

<!-- b000289 | prose | pages [9] -->
= u(t)

<!-- b000290 | prose | pages [9] -->
mv(t) −h(s)−1

<!-- b000291 | prose | pages [9] -->
dt

<!-- b000292 | prose | pages [9] -->
where

<!-- b000293 | prose | pages [9] -->
h(s) = mb

<!-- b000294 | prose | pages [9] -->
2mCdρAv(t)2 (12)

<!-- b000295 | prose | pages [9] -->
m g(sin(θ)+CR cos(θ)) (13)

<!-- b000296 | prose | pages [9] -->
and a is the joint acceleration of the cyclist and the bicycle, G is their effective gravity, FP is the pedaling force, and FW is the resistance of the oncoming wind (wind direction will be considered

<!-- b000297 | furniture | pages [10] -->
Team # 2209812

<!-- b000298 | furniture | pages [10] -->
Page 10 of 24

<!-- b000299 | prose | pages [10] -->
in Section 4.1), f1 and f2 are frictions of bicycle, FN1 and FN2 are support forces, mb is the mass of the bicycle and cyclist, g is gravity acceleration, Cd is aerodynamic drag coefficient, A is frontal area, ρ is the density of air which is assumed to be contant and unaffected by elevation, θ is the road slope which is positive for uphill and negative for downhill, and CR is the coefficient of rolling resistance of the road, and m is the effective mass of the bicycle, which is calculated by adding the impact of the wheels’ rotational inertia to mb,

<!-- b000300 | prose | pages [10] -->
m = mb +2 Iw

<!-- b000301 | prose | pages [10] -->
(14)

<!-- b000302 | prose | pages [10] -->
R2w

<!-- b000303 | prose | pages [10] -->
where Iw is the wheel rotational inertia, and Rw is the radius of bicycle wheel.

<!-- b000304 | prose | pages [10] -->
M2 M2

<!-- b000305 | prose | pages [10] -->
FN2 FN2

<!-- b000306 | prose | pages [10] -->
G

<!-- b000307 | prose | pages [10] -->
f2f2

<!-- b000308 | prose | pages [10] -->
FW

<!-- b000309 | prose | pages [10] -->
a

<!-- b000310 | prose | pages [10] -->
M1 M1

<!-- b000311 | prose | pages [10] -->
FN1 FN1

<!-- b000312 | prose | pages [10] -->
f2f2

<!-- b000313 | prose | pages [10] -->
q

<!-- b000314 | caption | pages [10] -->
Figure 8: Cyclist and Bicycle Aerodynamic Forces

<!-- b000315 | prose | pages [10] -->
We equate the propulsion power u(t) to the cyclist’s power on the pedals if the bicycle drivetrain is 100 percent efficient. Gear selection is not a consideration in our formulation since we use cyclist pedalling power rather than force as input, which would otherwise make the optimization more complicated.

<!-- b000316 | prose | pages [10] -->
Note that the previously displayed Equation 6 is the third state equation for the time derivative of the cyclist’s remaining anaerobic energy,

<!-- b000317 | prose | pages [10] -->
(

<!-- b000318 | prose | pages [10] -->
CP−u

<!-- b000319 | prose | pages [10] -->
f3 = dw

<!-- b000320 | prose | pages [10] -->
dt =

<!-- b000321 | prose | pages [10] -->
u ⩾CP

<!-- b000322 | prose | pages [10] -->
(a) (15)

<!-- b000323 | prose | pages [10] -->
u < CP

<!-- b000324 | prose | pages [10] -->
(b)

<!-- b000325 | prose | pages [10] -->
CP−(au+b)

<!-- b000326 | prose | pages [10] -->
Now we can design a minimum-time optimum control problem for the pacing strategy in a time-trial. Time is the objective function to be minimised,

<!-- b000327 | prose | pages [10] -->
u(t) J =

<!-- b000328 | prose | pages [10] -->
min

<!-- b000329 | prose | pages [10] -->
subject to,

<!-- b000330 | prose | pages [10] -->
Z tf

<!-- b000331 | prose | pages [10] -->
dt (16)

<!-- b000332 | prose | pages [10] -->
t0

<!-- b000333 | furniture | pages [11] -->
Team # 2209812

<!-- b000334 | prose | pages [11] -->


<!-- b000335 | prose | pages [11] -->
state−space model :

<!-- b000336 | prose | pages [11] -->
  

<!-- b000337 | prose | pages [11] -->
velocity limits :

<!-- b000338 | prose | pages [11] -->


<!-- b000339 | prose | pages [11] -->
remaining energy limits :

<!-- b000340 | prose | pages [11] -->
  

<!-- b000341 | prose | pages [11] -->
cyclist power limits :

<!-- b000342 | prose | pages [11] -->


<!-- b000343 | furniture | pages [11] -->
Page 11 of 24

<!-- b000344 | prose | pages [11] -->
˙x = f (x(t),u(t)) 0 ⩽v(t) ⩽vmax

<!-- b000345 | prose | pages [11] -->
(17)

<!-- b000346 | prose | pages [11] -->
0 ⩽w(t) ⩽W ′

<!-- b000347 | prose | pages [11] -->
0 ⩽u(t) ⩽Pmax (w)

<!-- b000348 | prose | pages [11] -->
where Pmax is defined by Equation (8). The final position is specified and fixed in this formulation, while the other two states, v and w, are uncertain. The maximum speed vmax is assumed to be constant throughout the journey in the simulations in this research, including the case of sharp turns.

<!-- b000349 | heading | pages [11] -->
Necessary Condition for Optimal Solution

<!-- b000350 | prose | pages [11] -->
3.3.3 In this part, we use the variational approach to investigate the given optimum control issue. The required condition for the optimality of input u, according to Pontryagin’s Minimum Principle (PMP), is that it minimizes the following Hamiltonian function,

<!-- b000351 | prose | pages [11] -->
H (x(t),u(t),λ (t)) = L(x(t),u(t))+λ T (t){f (x(t),u(t))}

<!-- b000352 | prose | pages [11] -->
where

<!-- b000353 | prose | pages [11] -->


<!-- b000354 | prose | pages [11] -->
λ =

<!-- b000355 | prose | pages [11] -->
λ1

<!-- b000356 | prose | pages [11] -->
(18)

<!-- b000357 | prose | pages [11] -->
T (19)

<!-- b000358 | prose | pages [11] -->
λ2 λ3

<!-- b000359 | prose | pages [11] -->
where λ is the vector of co-state variables, L is the integrand in the cost function J in Equation (16), and f is the vector on the right hand side of the state equations with components represented in Equations (11), (12), and (15).

<!-- b000360 | prose | pages [11] -->
When such an inequality restriction on control and state variables exists, the Hamiltonian equa- tion must be supplemented as follows,

<!-- b000361 | prose | pages [11] -->
H = L+λ T f + µC

<!-- b000362 | prose | pages [11] -->
where

<!-- b000363 | prose | pages [11] -->
(

<!-- b000364 | prose | pages [11] -->
(20)

<!-- b000365 | prose | pages [11] -->
⩾0 C = 0

<!-- b000366 | prose | pages [11] -->
µ

<!-- b000367 | prose | pages [11] -->
(21) = 0 C < 0

<!-- b000368 | prose | pages [11] -->
Additionally, the upper and lower limits on v and w presented in Equation (17) should be taken into account as,

<!-- b000369 | prose | pages [11] -->


<!-- b000370 | prose | pages [11] -->


<!-- b000371 | prose | pages [11] -->
v(t)−vmax

<!-- b000372 | prose | pages [11] -->


<!-- b000373 | prose | pages [11] -->
S(v,w) =

<!-- b000374 | prose | pages [11] -->
−v(t)

<!-- b000375 | prose | pages [11] -->
⩽0 (22)

<!-- b000376 | prose | pages [11] -->
w(t)−W ′

<!-- b000377 | prose | pages [11] -->
−w(t)

<!-- b000378 | prose | pages [11] -->
In this case, the first derivative of S(v,w) with respect to both v and w includes u. Then, we can treat S(1)(v;w) similar to C(v,w) and augment the Hamiltonian as follows,

<!-- b000379 | prose | pages [11] -->
H = L+λ T f + µC +ηTS(1) (23)

<!-- b000380 | prose | pages [11] -->
T must obey the following conditions,

<!-- b000381 | prose | pages [11] -->


<!-- b000382 | prose | pages [11] -->
where η =

<!-- b000383 | prose | pages [11] -->
η1 η2 η3 η4

<!-- b000384 | prose | pages [11] -->
⩾0 S(1)

<!-- b000385 | prose | pages [11] -->
(

<!-- b000386 | prose | pages [11] -->
= 0 i

<!-- b000387 | prose | pages [11] -->
ηi

<!-- b000388 | prose | pages [11] -->
= 0 S(1)

<!-- b000389 | prose | pages [11] -->
< 0 i

<!-- b000390 | prose | pages [11] -->
for i = 1,2,3,4 (24)

<!-- b000391 | furniture | pages [12] -->
Team # 2209812

<!-- b000392 | furniture | pages [12] -->
Page 12 of 24

<!-- b000393 | prose | pages [12] -->
It should be emphasized that when restrictions are fulfilled, the Hamiltonian terms C and T S(1) will always be zero. The dynamics of the co-states are shown below,

<!-- b000394 | prose | pages [12] -->
λ T = −Hx = −Lx −λ T fx −µCx −ηTS(1)

<!-- b000395 | prose | pages [12] -->
Its expanded version will be, 

<!-- b000396 | prose | pages [12] -->
dθ(s)

<!-- b000397 | prose | pages [12] -->
˙λ1 = λ2gmb

<!-- b000398 | prose | pages [12] -->
(25) x

<!-- b000399 | prose | pages [12] -->
ds (cos(θ (s))−CR sin(θ (s)))

<!-- b000400 | prose | pages [12] -->


<!-- b000401 | prose | pages [12] -->
m

<!-- b000402 | prose | pages [12] -->
 

<!-- b000403 | prose | pages [12] -->


<!-- b000404 | prose | pages [12] -->
˙λ2 = −λ1 −λ2

<!-- b000405 | prose | pages [12] -->
u

<!-- b000406 | prose | pages [12] -->


<!-- b000407 | prose | pages [12] -->
v2 −CdρAv

<!-- b000408 | prose | pages [12] -->
mt

<!-- b000409 | prose | pages [12] -->


<!-- b000410 | prose | pages [12] -->
˙λ3 = 0

<!-- b000411 | prose | pages [12] -->
 

<!-- b000412 | prose | pages [12] -->
(26)

<!-- b000413 | prose | pages [12] -->
The maximum value of u minimizes the function. We can consider four cases,

<!-- b000414 | prose | pages [12] -->
λ2

<!-- b000415 | prose | pages [12] -->
Case I. λ2

<!-- b000416 | prose | pages [12] -->
mv −λ3 < 0 AND mv −aλ3 < 0

<!-- b000417 | prose | pages [12] -->
The slope is negative in both the fatigue and recovery modes, indicating that the greatest value of u in each instance minimizes the Hamiltonian. The maximum input value in the fatigue mode is umax, while the maximum input value in the recovery mode is CP. The control with the least Hamiltonian is the best of the two,

<!-- b000418 | prose | pages [12] -->


<!-- b000419 | prose | pages [12] -->
H∗= min

<!-- b000420 | furniture | pages [12] -->


<!-- b000421 | prose | pages [12] -->
Hfatigue (umax),Hrecovery (CP)

<!-- b000422 | prose | pages [12] -->
(27)

<!-- b000423 | prose | pages [12] -->
where the subscripts of H distinguish between fatigue and recovery modes due to the somewhat differing equations of the two modes. We can’t tell which Hamiltonian is smaller by substituting the aforementioned u values. The ideal input may be written as,

<!-- b000424 | prose | pages [12] -->
(

<!-- b000425 | prose | pages [12] -->
umax Hfatigue (umax) < Hrecovery (CP)

<!-- b000426 | prose | pages [12] -->
u∗=

<!-- b000427 | prose | pages [12] -->
(28) CP Hfatigue (umax) > Hrecovery (CP)

<!-- b000428 | prose | pages [12] -->
Note that in the event Hfatigue(umax) = Hrecovery(CP), both u = CP and u = umax are optimal.

<!-- b000429 | heading | pages [12] -->
The solutions of Case II. λ2

<!-- b000430 | prose | pages [12] -->
mv −λ3 > 0 AND

<!-- b000431 | prose | pages [12] -->
λ2

<!-- b000432 | prose | pages [12] -->
aλ3 < 0 and Case IV. λ2

<!-- b000433 | prose | pages [12] -->
mv −aλ3 > 0, Case III. λ2 λ2

<!-- b000434 | prose | pages [12] -->
λ2 mv −λ3 > 0 AND mv −

<!-- b000435 | prose | pages [12] -->
mv −aλ3 > 0 are based on same methods. mv −λ3 < 0 AND

<!-- b000436 | prose | pages [12] -->
Thus after considering all of the cases discussed above, the optimal power trajectory can only take values from the vector below,

<!-- b000437 | prose | pages [12] -->


<!-- b000438 | prose | pages [12] -->


<!-- b000439 | prose | pages [12] -->
u∗=

<!-- b000440 | prose | pages [12] -->


<!-- b000441 | prose | pages [12] -->
umax u˙v=0

<!-- b000442 | prose | pages [12] -->
 (29)

<!-- b000443 | prose | pages [12] -->
CP

<!-- b000444 | prose | pages [12] -->
0

<!-- b000445 | prose | pages [12] -->
which is the equation provides the necessary conditions for optimality of u since it was based on a PMP analysis.

<!-- b000446 | prose | pages [12] -->
3.3.4

<!-- b000447 | heading | pages [12] -->
Numerical Solution of the Problem

<!-- b000448 | prose | pages [12] -->
With a zero-order hold on input in between sampling intervals, the following discretized state- space equations are obtained,

<!-- b000449 | prose | pages [12] -->
ti+1 = ti + ∆s

<!-- b000450 | prose | pages [12] -->
 ui

<!-- b000451 | prose | pages [12] -->
(30)

<!-- b000452 | prose | pages [12] -->
vi

<!-- b000453 | prose | pages [12] -->


<!-- b000454 | prose | pages [12] -->
−g(sin(θi)+ µ cos(θi))−0.5CdρA

<!-- b000455 | prose | pages [12] -->
vi+1 = vi + ∆s

<!-- b000456 | prose | pages [12] -->
vi

<!-- b000457 | prose | pages [12] -->
mtvi

<!-- b000458 | prose | pages [12] -->
v2

<!-- b000459 | prose | pages [12] -->
(31)

<!-- b000460 | prose | pages [12] -->
i

<!-- b000461 | prose | pages [12] -->
mt

<!-- b000462 | furniture | pages [13] -->
Team # 2209812

<!-- b000463 | prose | pages [13] -->
(

<!-- b000464 | prose | pages [13] -->
wi+1 = wi + ∆s

<!-- b000465 | furniture | pages [13] -->
Page 13 of 24

<!-- b000466 | prose | pages [13] -->
ui ⩾CP vi (CP−ui) wi+1 = wi + ∆s

<!-- b000467 | prose | pages [13] -->
(32) vi (CP−aui −b) ui < CP

<!-- b000468 | prose | pages [13] -->
The cost function in Equation (16) is rewritten with position as the independent variable and discretized as follows,

<!-- b000469 | prose | pages [13] -->
JN =

<!-- b000470 | prose | pages [13] -->
i=N

<!-- b000471 | prose | pages [13] -->
∆si

<!-- b000472 | prose | pages [13] -->
∑

<!-- b000473 | prose | pages [13] -->
(33)

<!-- b000474 | prose | pages [13] -->
vi

<!-- b000475 | prose | pages [13] -->
i=0

<!-- b000476 | prose | pages [13] -->
According to the Bellman’s principle of optimality [16], when a system is on an optimum path from an initial state to a final state, it should follow an optimal policy throughout the duration of the trip, independent of any previous choice or condition. To discover the ideal state trajectory in dynamic programming, one may start at the final state and work backward, calculating the optimal cost-to-go from any state to the last step. J∗

<!-- b000477 | prose | pages [13] -->
i+1,N stores the optimum costs and control inputs from all of the feasible (v,w) nodes at si+1 to the end state at sN. Among them,

<!-- b000478 | prose | pages [13] -->
Ji,i+1 +J∗

<!-- b000479 | prose | pages [13] -->
J∗

<!-- b000480 | prose | pages [13] -->


<!-- b000481 | prose | pages [13] -->
i,N = min ui

<!-- b000482 | prose | pages [13] -->
where

<!-- b000483 | prose | pages [13] -->
J∗

<!-- b000484 | prose | pages [13] -->


<!-- b000485 | prose | pages [13] -->
i+1,N (x)

<!-- b000486 | prose | pages [13] -->
(34)

<!-- b000487 | prose | pages [13] -->
uiui+1,···,uN−1 [Ji+1,N] i+1,N = min (35)

<!-- b000488 | prose | pages [13] -->
The dynamic programming for Behrman’s equation is shown below,

<!-- b000489 | prose | pages [13] -->
Initialize array 𝑣 arbitrarily (e.g., 𝑣(𝑠)=0 for all s 𝑆+

<!-- b000490 | prose | pages [13] -->
Repeat

<!-- b000491 | prose | pages [13] -->
For each s 𝑆+:

<!-- b000492 | prose | pages [13] -->
Until (a small positive number)

<!-- b000493 | prose | pages [13] -->
Output a deterministic policy, , such that

<!-- b000494 | heading | pages [13] -->
Apply Model to Time Trial Courses

<!-- b000495 | prose | pages [13] -->
3.4

<!-- b000496 | prose | pages [13] -->
3.4.1 Determine the Constants’ Values.

<!-- b000497 | prose | pages [13] -->
▶The Resistance

<!-- b000498 | prose | pages [13] -->
It’s common knowledge that if we ride upright in a high wind, we’ll face a lot of resistance. Pro- fessional cyclists typically ride prone to reduce wind resistance, with the following riding posture: lower upper body, head slightly tilted forward; arms naturally bent to facilitate lumbar arch flexion, lowering the body’s center of gravity and preventing the transmission of impact to the entire body

<!-- b000499 | furniture | pages [14] -->
Team # 2209812

<!-- b000500 | furniture | pages [14] -->
Page 14 of 24

<!-- b000501 | prose | pages [14] -->
due to car bumps; hands lightly but firmly grip the handle, hips firmly on the car seat. The frontal Area (A) and drag coefficient (Cd) of various posture of cyclist are shown in Figure 9.

<!-- b000502 | prose | pages [14] -->
Thus, Cd = 0.88, A =3.9 ft2. And in general, ρ = 1.29 kg/m3, CR = 0.015. They will be using in Equation (12) and (13).

<!-- b000503 | prose | pages [14] -->
Bikes

<!-- b000504 | prose | pages [14] -->
Upright commuter

<!-- b000505 | prose | pages [14] -->
Racing

<!-- b000506 | prose | pages [14] -->
Drafting

<!-- b000507 | prose | pages [14] -->
Streamlined

<!-- b000508 | prose | pages [14] -->
Frontal Area Drag Coefficient

<!-- b000509 | prose | pages [14] -->
A = 5.5 ft2

<!-- b000510 | prose | pages [14] -->
1.10

<!-- b000511 | prose | pages [14] -->
A = 3.9 ft2

<!-- b000512 | prose | pages [14] -->
0.88

<!-- b000513 | prose | pages [14] -->
A = 3.9 ft2

<!-- b000514 | prose | pages [14] -->
0.50

<!-- b000515 | prose | pages [14] -->
A = 5.0 ft2

<!-- b000516 | prose | pages [14] -->
0.12

<!-- b000517 | caption | pages [14] -->
Figure 9: The Effect of Posture on Air Resistance

<!-- b000518 | prose | pages [14] -->
▶The Effective Mass

<!-- b000519 | prose | pages [14] -->
In Equation (14), for the sake of standardization and ease of calculation, we assume that the bicycles covered in this article are all the same, where two wheels of the same size, both with a radius of 0.35 m, weigh 1.2 kg, so that the Iw of each wheel is 0.147 kg·m2. Thus the effective mass (m) of the bicycle and the cyclist is to be about 2.3 kg larger than their actual weight (mb).

<!-- b000520 | prose | pages [14] -->
3.4.2

<!-- b000521 | heading | pages [14] -->
Simulation Results and Analysis

<!-- b000522 | prose | pages [14] -->
Using processed data of STRAVA-Tokyo2020 and STRAVA-BelgiumUCI in Table 2 and the power curve in Figure 7, we obtained the optimal power profile for cyclists at the Tokyo Olympics (men and women are in different courses) and at the UCI World Championship’s individual time trial courses, which are shown in Figure 10 and 11 below,

<!-- b000523 | prose | pages [14] -->
SW

<!-- b000524 | prose | pages [14] -->
SM

<!-- b000525 | prose | pages [14] -->
TW

<!-- b000526 | prose | pages [14] -->
TM

<!-- b000527 | prose | pages [14] -->
SM

<!-- b000528 | prose | pages [14] -->
TM

<!-- b000529 | prose | pages [14] -->
SW

<!-- b000530 | prose | pages [14] -->
SW

<!-- b000531 | prose | pages [14] -->
(b) Women

<!-- b000532 | prose | pages [14] -->
(a) Men

<!-- b000533 | caption | pages [14] -->
Figure 10: TTC of Tokyo Olympic

<!-- b000534 | caption | pages [14] -->
Figure 11: TTC of UCI

<!-- b000535 | prose | pages [14] -->
where in every subfigure, the upper part is the curve of power P with respect to distance s, and the lower part is the curve of elevation with respect to s.

<!-- b000536 | furniture | pages [15] -->
Team # 2209812

<!-- b000537 | furniture | pages [15] -->
Page 15 of 24

<!-- b000538 | caption | pages [15] -->
Figure 12 shows a course of own design located in the Italy’s San Felice Circeo, along the

<!-- b000539 | prose | pages [15] -->
suburbs and beach. The route begins in the south along the sea (bottom of the image), circles the city, and returns to the starting place, which is also the ultimate destination. The whole race decreases in height and then maintains a distance before descending a sharp slope to the finish line, with a total length of around 16 kilometers (Figure 13). In the same way as above, we obtain the optimal power profile for cyclists at this couse in Figure 13 below.

<!-- b000540 | caption | pages [15] -->
Figure 12: A Course of Own Design

<!-- b000541 | prose | pages [15] -->
SM

<!-- b000542 | prose | pages [15] -->
TM

<!-- b000543 | prose | pages [15] -->
SW

<!-- b000544 | prose | pages [15] -->
SW

<!-- b000545 | caption | pages [15] -->
Figure 13: TTC of Own Design

<!-- b000546 | prose | pages [15] -->
In addition, the minimised time cost of four cyclists in three location show in Table 3 below:

<!-- b000547 | caption | pages [15] -->
Table 3: Minimised Time Cost (s)

<!-- b000548 | prose | pages [15] -->
Tokyo Olympic Cyclist UCI Own Design

<!-- b000549 | prose | pages [15] -->
3641.49 Time Trial Specialist, Man 3258.93 1280.11 1984.51 Time Trial Specialist, Woman 3373.95 1321.25 4117.69 Sprinter, Man 3407.07 1322.85 3027.01 Sprinter, Woman

<!-- b000550 | prose | pages [15] -->
In summary, we can conclude the following,

<!-- b000551 | prose | pages [15] -->
3528.34 1497.89

<!-- b000552 | prose | pages [15] -->
• The model advocates utilizing as much power as possible at the start of a race, regardless of the kind of athlete. However, after a certain distance, aim to maintain the power at critical power. This implies that putting in a respectable all-out effort at the start of the race will have little effect on the backstretch.

<!-- b000553 | prose | pages [15] -->
• As we can see, for all power profiles, the model suggests that cyclists ride uphill with a particular level of power then ride downhill with as little power as possible while maintaining pace. Therefore, in the actual race, cyclists should make reasonable use of riding downhill to rest and have some physical preparation for the upcoming ride uphill.

<!-- b000554 | furniture | pages [16] -->
Team # 2209812

<!-- b000555 | furniture | pages [16] -->
Page 16 of 24

<!-- b000556 | heading | pages [16] -->
TASK 3 & 4: Sensitivity to Weather and Power Distribution’s

<!-- b000557 | prose | pages [16] -->
4 Deviations

<!-- b000558 | prose | pages [16] -->
4.1 The influence of the weather

<!-- b000559 | prose | pages [16] -->
In cycling, the weather is often unpredictable.

<!-- b000560 | prose | pages [16] -->
Gusty winds, high temperature, and other weather changes can have an impact on competitors. Thus exploring the cyclist’s sensitivity to weather is of great significance in guiding the race.

<!-- b000561 | prose | pages [16] -->
4.1.1 Wind Influence The following Figure 14 has shown wind effect to a cyclist,

<!-- b000562 | prose | pages [16] -->
North

<!-- b000563 | prose | pages [16] -->
North

<!-- b000564 | prose | pages [16] -->
Direction

<!-- b000565 | prose | pages [16] -->
Direction

<!-- b000566 | caption | pages [16] -->
Figure 14: Wind Effect to a Cyclist

<!-- b000567 | prose | pages [16] -->
where ϕ is the angle of wind direction with due north direction, and γ is the angle of cycling direction with due north direction. As the Assumption 2 in Section 2.1 says, we should neglect lateral effect and deviation. Thus we equate the drag force on the cyclist to the drag force on them in the cycling direction,

<!-- b000568 | prose | pages [16] -->
FW = 1

<!-- b000569 | prose | pages [16] -->
2mCdρA[v−V cos(γ −ϕ)]2

<!-- b000570 | prose | pages [16] -->
where FW is the drag force.

<!-- b000571 | prose | pages [16] -->
▶Result

<!-- b000572 | prose | pages [16] -->
(36)

<!-- b000573 | prose | pages [16] -->
Based on Equation (36) above, the minimum time and optimal energy distribution of the athletes in section 3.4.2 were re-optimized for different wind directions and wind velocities in different time trial courses (TTC) , and the results were obtained as shown in the following Figure 15, where the velocity axis represents the magnitude of the velocity of the wind along its direction, and the angle axis represents the magnitude of the angle between the wind direction and the direction due north, and the influence axis represents the percentage of affected (includes positively and negatively) on the corresponding courses for all female cyclists.

<!-- b000574 | prose | pages [16] -->
In the Figure 15, what we can see is that the results of TTC of Tokyo Olympic (Figure 15a) and own design (Figure 15b) are irregular while their route is close to a rectangular. However, the UCI World Championship (Figure 15c) is regular, which shows that when the wind direction is from north to south or south to north (wind direction is close to 0), the biggest effect occurs. And the larger the wind speed, the greater the impact that is more sensitive to wind. In summary, the model

<!-- b000575 | furniture | pages [17] -->
Team # 2209812

<!-- b000576 | furniture | pages [17] -->
Page 17 of 24

<!-- b000577 | prose | pages [17] -->
of sensitivity to wind effect is up to corresponding course. The closer the course is to a bar or strip, the more regular the wind direction and velocity is to the cyclist, otherwise the more uncertain it is.

<!-- b000578 | prose | pages [17] -->
(b) UCI World Championship (a) Tokyo Olympic (c) Own Design

<!-- b000579 | caption | pages [17] -->
Figure 15: Wind Effect to Defferent TTCs (Up is the north)

<!-- b000580 | prose | pages [17] -->
4.1.2 Temperature Influence The first thing that is affected by the temperature t (◦C) change is the air pressure and air density. From Equation (ddd), it is shown that they have a great influence on the power profile of the cyclist. According to air pressure p (Pa) relationship with the altitude h (m),

<!-- b000581 | prose | pages [17] -->
p = −0.011h+100.8

<!-- b000582 | prose | pages [17] -->
and the air density is,

<!-- b000583 | prose | pages [17] -->
ρ = 1.293p

<!-- b000584 | prose | pages [17] -->
(37)

<!-- b000585 | prose | pages [17] -->
273.15 101.325 ×

<!-- b000586 | prose | pages [17] -->
where

<!-- b000587 | prose | pages [17] -->
(38) 273.15+t

<!-- b000588 | prose | pages [17] -->
t = t0 −0.6h

<!-- b000589 | prose | pages [17] -->
(39) 100

<!-- b000590 | prose | pages [17] -->
where t0 is the temperature when the h = 0. Therefore,

<!-- b000591 | prose | pages [17] -->
ρ = f(t0,h) (40)

<!-- b000592 | prose | pages [17] -->
Based on these, we use the data of women time trail specialist in Tokyo Olympic. Then we assume that match the expected temperature is 20◦C, change the temperature in steps of 0.5 degrees in the positive and negative directions, and finally we obtain the sensitivity to temperature in Figure (16) below, where the positive effect indicates that the cyclist spends less time and, conversely, more time.

<!-- b000593 | furniture | pages [18] -->
Team # 2209812

<!-- b000594 | furniture | pages [18] -->
Page 18 of 24

<!-- b000595 | caption | pages [18] -->
Figure 16: Sensitivity to Temperature

<!-- b000596 | prose | pages [18] -->
So, under normal temperatures in non-extreme environments, the lower the temperature, the better for cyclists in general. Therefore, for cyclists, keeping their equipment light, being aware of hydration and wearing sportswear that facilitates heat dissipation are ways to help them achieve better results.

<!-- b000597 | prose | pages [18] -->
4.2 The Influence of Power Distribution’s Deviation

<!-- b000598 | prose | pages [18] -->
4.2.1

<!-- b000599 | heading | pages [18] -->
Sensitivity of Deviation Probability

<!-- b000600 | prose | pages [18] -->
In this section, the ideal energy distribution (section (3.4.2)) is discretized into several sample points. We assume that each sampling point has a probability p of having an power shift. Using data from the Tokyo women’s time trial course, multiple minimum times were measured at different

<!-- b000601 | prose | pages [18] -->
p.

<!-- b000602 | caption | pages [18] -->
Figure 17: Average Minimum Time Cost and Cost Percentage for Deviation Probability

<!-- b000603 | caption | pages [18] -->
Figure 17 shows a scatter plot with time cost and cost percentage respect to different time point

<!-- b000604 | prose | pages [18] -->
and the average time point curve. Therefore, what we can conclude is that the greater deviation probability, the greater the time cost and the trend of time cost. In other words, an athlete’s

<!-- b000605 | furniture | pages [19] -->
Team # 2209812

<!-- b000606 | furniture | pages [19] -->
Page 19 of 24

<!-- b000607 | prose | pages [19] -->
inconsistent form will cause them to go in a bad direction. As a consequence, keeping his or her pacing during the race is critical for a cyclist to achieving a positive outcome.

<!-- b000608 | prose | pages [19] -->
4.2.2

<!-- b000609 | heading | pages [19] -->
Sensitivity of Location Deviation

<!-- b000610 | prose | pages [19] -->
In the same way as in Section 4.2, the women’s time trail course of the Tokyo Olympics was divided into multiple sections (one section every 2 km) under an ideal energy distribution. Assume that the probability of energy shift is p (p = 0.1), and multiple measurements are taken to obtain multiple minimum times under each section. The scatter plot and radar plot of the effect of energy offset on the minimum time for each section are drawn as follows,

<!-- b000611 | caption | pages [19] -->
Figure 18: Curve for Location Deviation

<!-- b000612 | caption | pages [19] -->
Figure 19: Radar Plot for Location Deviation

<!-- b000613 | prose | pages [19] -->
Figures (18) and (19) demonstrate how cyclists are influenced by deviations in the energy dis- tribution over various regions of the same deviation probability. The cyclists are clearly impacted more in the uphill parts of the 10-12km, 12-14km, and 16-18km. However, t he cyclists are less impacted by the variation of energy distribution in the downhill parts of 4-6km, 8-10km, and 14- 16km. The following table shows the ideal time of arrival at these critical points in time and the deviations caused by the impact,

<!-- b000614 | caption | pages [19] -->
Table 4: Critical Point

<!-- b000615 | prose | pages [19] -->
Arrival Time (s) Point

<!-- b000616 | prose | pages [19] -->
468.05±8.66 6 km 608.76±14.95 8 km 795.81±18.10 10 km 1023.94±25.97 12 km

<!-- b000617 | prose | pages [19] -->
Arrival Time (s) Point

<!-- b000618 | prose | pages [19] -->
1196.94±33.84 14 km 1334.84±36.20 16 km 1636.44±42.49 18 km

<!-- b000619 | prose | pages [19] -->
Based on these, we can conclude that a cyclist who does not have a proper power distribu- tion while riding uphill will have a greater impact, although violating his energy distribution limit when riding downhill will not have a significant influence. Therefore, to attain better out- comes, bikers should aim to maintain their pedaling rhythm while riding uphill, while resting and attempting to maintain high speed when riding downhill.

<!-- b000620 | furniture | pages [20] -->
Team # 2209812

<!-- b000621 | furniture | pages [20] -->
Page 20 of 24

<!-- b000622 | prose | pages [20] -->
TASK 5: Optimal Power Use for a Team Time Trial 5

<!-- b000623 | prose | pages [20] -->
5.1 The Benefit of Team Riding

<!-- b000624 | prose | pages [20] -->
▶Reduce Resistance

<!-- b000625 | prose | pages [20] -->
As shown in Figure 20 below, in a cycling team race, the first person will have the largest windward area, and will therefore suffer the greatest wind resistance. And, in this case, this cyclist must also maintain a certain speed to lead the team forward.

<!-- b000626 | caption | pages [20] -->
Figure 20: An Overview of Cycling Team for the Impact of Air Resistance [15]

<!-- b000627 | prose | pages [20] -->
Each cyclist in a team has a different air resistance,

<!-- b000628 | prose | pages [20] -->
D = 1

<!-- b000629 | prose | pages [20] -->
2ρCdrCdAv2 (41)

<!-- b000630 | prose | pages [20] -->
where Cdr is coefficient of drag reduction and Cd is coefficient of drag.

<!-- b000631 | prose | pages [20] -->
▶Maximize the Team Power

<!-- b000632 | prose | pages [20] -->
As presented in figure 21 below, the strategy that is currently most used is to have a fixed order where every cyclist drives roughly ten to thirty seconds in first position and then changes to last position. In first position the drag is the highest, thus is the required power output is high. Depending on the capability of the cyclist and it’s state at the moment the cyclist will adjust the time spend in that position, shorter ifweaker or tired and longer if stronger or in a more energetic state. Cyclists that are much weaker than the others, are often dropped out of the group during the race.

<!-- b000633 | heading | pages [20] -->
Team Time Trial Optimization Model

<!-- b000634 | prose | pages [20] -->
5.2

<!-- b000635 | prose | pages [20] -->
In this section, we discuss the team time trail optimization model, where the team consists of six cyclists and the team’s time is determined when the fourth rider crosses the finish line.

<!-- b000636 | prose | pages [20] -->
We assume that the six cyclists are A,B,C,D,E,F. Thus, we develop a optimization model as follows,

<!-- b000637 | prose | pages [20] -->
u(t) J =

<!-- b000638 | prose | pages [20] -->
min

<!-- b000639 | prose | pages [20] -->
where

<!-- b000640 | prose | pages [20] -->
Z t f

<!-- b000641 | prose | pages [20] -->
dt (42)

<!-- b000642 | prose | pages [20] -->
t0

<!-- b000643 | prose | pages [20] -->
J = f (∆1,∆2,∆3,∆4,∆5,∆6,∆7,∆8) (43)

<!-- b000644 | furniture | pages [21] -->
Team # 2209812

<!-- b000645 | furniture | pages [21] -->
Page 21 of 24

<!-- b000646 | caption | pages [21] -->
Figure 21: Regular Changing Dynamics in a Team Time Trial of Four Cyclists [15]

<!-- b000647 | prose | pages [21] -->
where

<!-- b000648 | prose | pages [21] -->


<!-- b000649 | prose | pages [21] -->
∆1 = L(P0,P1,P2,···)

<!-- b000650 | prose | pages [21] -->
  

<!-- b000651 | prose | pages [21] -->
∆2 = tfront−A

<!-- b000652 | prose | pages [21] -->
   

<!-- b000653 | prose | pages [21] -->
(44)

<!-- b000654 | prose | pages [21] -->
∆3 = tfront−B

<!-- b000655 | prose | pages [21] -->


<!-- b000656 | prose | pages [21] -->
···

<!-- b000657 | prose | pages [21] -->
    

<!-- b000658 | prose | pages [21] -->
∆7 = tfront−F

<!-- b000659 | prose | pages [21] -->


<!-- b000660 | prose | pages [21] -->
where L(s) is a function respect to the order of the time, and tfront−A represents the time that A s first.

<!-- b000661 | prose | pages [21] -->
6

<!-- b000662 | heading | pages [21] -->
Evaluation of Strengths and Weaknesses

<!-- b000663 | prose | pages [21] -->
6.1

<!-- b000664 | heading | pages [21] -->
Strengths

<!-- b000665 | prose | pages [21] -->
• This article’s model analyzes individual and team competition of cyclists by combining phys- iology, dynamics, and aerodynamics. It also makes extensive use of accurate data for simulation and analysis. The final outcomes are more consistent with common sense and have a high level of confidence.

<!-- b000666 | prose | pages [21] -->
• A number of possibilities were evaluated for the sensitivity analysis. Sensitivity to weather is classified as sensitivity to wind and sensitivity to temperature. The sensitivity to power distribution deviation takes into account the deviation of power profile and the deviation of power profile in each section.

<!-- b000667 | prose | pages [21] -->
6.2

<!-- b000668 | heading | pages [21] -->
Weaknesses

<!-- b000669 | prose | pages [21] -->
• When estimating the impacts of wind, the effects of air vortices and atmospheric pressure were not fully considered. Because cyclists’ velocity is frequently more than 10m/s and their form is not totally streamlined. As a result of being impacted by the wind and air, an air vortex forms behind it, and the resistance increases due to the action of atmospheric pressure.

<!-- b000670 | furniture | pages [22] -->
Team # 2209812

<!-- b000671 | furniture | pages [22] -->
Page 22 of 24

<!-- b000672 | heading | pages [22] -->
References

<!-- b000673 | references | pages [22] -->
[1] Clarke, David C., and Philip F. Skiba. "Rationale and resources for teaching the mathematical

<!-- b000674 | references | pages [22] -->
modeling of athletic training and performance." Advances in physiology education (2013).

<!-- b000675 | references | pages [22] -->
[2] Gede, Gilbert. Optimal pacing strategies for cyclist time trials. University of California, Davis,

<!-- b000676 | references | pages [22] -->
2014.

<!-- b000677 | references | pages [22] -->
[3] Jones, Andrew M., et al. "Critical power: implications for determination of VO2max and

<!-- b000678 | references | pages [22] -->
exercise tolerance." Med Sci Sports Exerc 42.10 (2010): 1876-90.

<!-- b000679 | references | pages [22] -->
[4] Maturana, Felipe Mattioni, et al. "Critical power: how different protocols and models affect

<!-- b000680 | references | pages [22] -->
its determination." Journal of Science and Medicine in Sport 21.7 (2018): 742-747.

<!-- b000681 | references | pages [22] -->
[5] Vanhatalo, Anni, Andrew M. Jones, and Mark Burnley. "Application of critical power in

<!-- b000682 | references | pages [22] -->
sport." International journal of sports physiology and performance 6.1 (2011): 128-136.

<!-- b000683 | references | pages [22] -->
[6] J. Qiao." Application of power-maintenance time curves and critical power in predicting cy-

<!-- b000684 | references | pages [22] -->
cling performance." Sports Research 42.03(2021):99-104. doi:

<!-- b000685 | references | pages [22] -->
[7] Clarke, David C., and Philip F. Skiba. "Rationale and resources for teaching the mathematical

<!-- b000686 | references | pages [22] -->
modeling of athletic training and performance." Advances in physiology education (2013).

<!-- b000687 | references | pages [22] -->
[8] Morton, R. Hugh. "A new modelling approach demonstrating the inability to make up for lost

<!-- b000688 | references | pages [22] -->
time in endurance running events." IMA Journal of Management Mathematics 20.2 (2009):

<!-- b000689 | references | pages [22] -->
109-120.

<!-- b000690 | references | pages [22] -->
[9] Keller, Joseph B. "Optimal velocity in a race." The American Mathematical Monthly 81.5

<!-- b000691 | references | pages [22] -->
(1974): 474-480.

<!-- b000692 | references | pages [22] -->
[10] Hugh Morton, R. "A 3-parameter critical power model." Ergonomics 39.4 (1996): 611-619.

<!-- b000693 | references | pages [22] -->
[11] Coggan, A. "Creating Your Power Profile" Training Peaks. n.p. 2019. Sat. 19 Feb 2022.

<!-- b000694 | references | pages [22] -->
https://www.trainingpeaks.com/blog/power-profiling/.

<!-- b000695 | references | pages [22] -->
[12] Monod, H., and J. Scherrer. "The work capacity of a synergic muscular group." Ergonomics

<!-- b000696 | references | pages [22] -->
8.3 (1965): 329-338.

<!-- b000697 | references | pages [22] -->
[13] Ashtiani, Faraz, et al. "Optimal Pacing of a Cyclist in a Time Trial Based on Individualized

<!-- b000698 | references | pages [22] -->
Models of Fatigue and Recovery." arXiv preprint arXiv:2007.11393 (2020).

<!-- b000699 | references | pages [22] -->
[14] Ashtiani, Faraz, et al. "Experimental modeling of cyclists fatigue and recovery dynamics en-

<!-- b000700 | references | pages [22] -->
abling optimal pacing in a time trial." 2019 American Control Conference (ACC). IEEE,

<!-- b000701 | references | pages [22] -->
2019.

<!-- b000702 | references | pages [22] -->
[15] Overtoom, Mats. "Optimal Team Time Trial Strategy in Road Cycling: Optimisation of

<!-- b000703 | references | pages [22] -->
Changing Strategy using a Mathematical Performance model." (2013).

<!-- b000704 | references | pages [22] -->
[16] Behrman, Richard E., and Stuart E. Dreyfus. Applied dynamic programming. Princeton uni-

<!-- b000705 | references | pages [22] -->
versity press, 2015.

<!-- b000706 | furniture | pages [23] -->
Team # 2209812

<!-- b000707 | heading | pages [23] -->
Memo

<!-- b000708 | furniture | pages [23] -->
Page 23 of 24

<!-- b000709 | prose | pages [23] -->
Race Guidance

<!-- b000710 | prose | pages [23] -->
▶How to Use a Power Curve?

<!-- b000711 | prose | pages [23] -->
The value of a power curve is that it shows you the work you’ve done. Since it’s power plotted against time, it gives you a snapshot of your energy systems and a view of your strengths and weaknesses.

<!-- b000712 | prose | pages [23] -->
Every cyclist has strengths and weaknesses. Typical power curves are easily distinguishable. For example, in the chart below, the Sprinter maintains more power for a short period of time, while the Time Trial Specialist maintains more power for a longer period of time. Proper use of power curves allows for more professional guidance to be developed for cyclists.

<!-- b000713 | prose | pages [23] -->
SM

<!-- b000714 | prose | pages [23] -->
SM

<!-- b000715 | prose | pages [23] -->
TM

<!-- b000716 | prose | pages [23] -->
TM

<!-- b000717 | prose | pages [23] -->
SW

<!-- b000718 | prose | pages [23] -->
SW

<!-- b000719 | prose | pages [23] -->
TW

<!-- b000720 | prose | pages [23] -->
TW

<!-- b000721 | prose | pages [23] -->
TM

<!-- b000722 | prose | pages [23] -->
TM

<!-- b000723 | prose | pages [23] -->
SM

<!-- b000724 | prose | pages [23] -->
SM TW

<!-- b000725 | prose | pages [23] -->
TW

<!-- b000726 | prose | pages [23] -->
SW

<!-- b000727 | prose | pages [23] -->
SW

<!-- b000728 | prose | pages [23] -->
TM

<!-- b000729 | prose | pages [23] -->
TW

<!-- b000730 | prose | pages [23] -->
SM

<!-- b000731 | prose | pages [23] -->
SW

<!-- b000732 | prose | pages [23] -->
▶How to Determine Pacing of a Cyclist?

<!-- b000733 | prose | pages [23] -->
Three principles for pacing:

<!-- b000734 | prose | pages [23] -->
• No matter what happens, keep yourself first pacing rhythm

<!-- b000735 | prose | pages [23] -->
Keeping his or her pacing during the race is critical for a cyclist to achieving a positive outcome. In addition, from a psychological point of view, the stable pacing can improve self-confidence.

<!-- b000736 | prose | pages [23] -->
• putting in a respectable all-out effort at the start of the race.

<!-- b000737 | prose | pages [23] -->
At the start of a race, enough speed makes the cyclist not easy to lag behind. And it doesn’t has a great influence to the rest journey.

<!-- b000738 | prose | pages [23] -->
• making reasonable use of riding downhill to rest and having some physical preparation for the upcoming ride uphill

<!-- b000739 | prose | pages [23] -->
The ride uphill part takes cyclists more time and energy, and has a greater impact, if cyclists’ power profile deviations happen. However, the ride downhill part, it allows cyclists have more time to rest with easy ride.

<!-- b000740 | prose | pages [23] -->
▶How to keep Stamina in a Time Trial?

<!-- b000741 | prose | pages [23] -->
• Maintain the speed and pay attention to rest on your way down

<!-- b000742 | furniture | pages [24] -->
Team # 2209812

<!-- b000743 | furniture | pages [24] -->
Page 24 of 24

<!-- b000744 | prose | pages [24] -->
• As far as possible follow behind the other players

<!-- b000745 | prose | pages [24] -->
▶How to Prepare for a Cycling Race?

<!-- b000746 | prose | pages [24] -->
• Check the course

<!-- b000747 | prose | pages [24] -->
On the one hand, Familiar with the course help cyclists determine power distribution to prevent deviations. On the other hand, it also help cyclists determine which direction of wind influence most.

<!-- b000748 | prose | pages [24] -->
• Before the game to keep rest, pay attention to diet, make oneself of the stable condition

<!-- b000749 | prose | pages [24] -->
• Check the weather ahead of time

<!-- b000750 | prose | pages [24] -->
The weather forecast will tell the wind velocity and direction and temperature change in the race day. Based on it, what you need to do is to prepare. For example, prepare to cool down if meets the high temperature weather

<!-- b000751 | prose | pages [24] -->
• Choosing the suitable equipment

<!-- b000752 | prose | pages [24] -->
Heavy cycle will become the biggest burden of cyclists.

<!-- b000753 | prose | pages [24] -->
Suitable equipment help cyclists against the situation not expected.
