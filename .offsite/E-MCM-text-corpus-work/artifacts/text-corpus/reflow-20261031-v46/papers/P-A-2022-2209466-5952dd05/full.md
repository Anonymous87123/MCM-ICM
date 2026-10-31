# P-A-2022-2209466-5952dd05

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
2209466

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Optimal Power Distribution of a Cyclist

<!-- b000008 | prose | pages [1] -->
Bicycle road races have always been popular and competitive. For the cyclists, it is of vital importance to distribute the power properly on the course. In order to help riders distribute their limited energy reasonably, we established a model to simulate the rider's power output to find the optimal distribution of their power.

<!-- b000009 | prose | pages [1] -->
Firstly, we established a Fatigue Physiological Model to characterize riders' power curve, which describes a rider's average power output as a function of sustained output time. From the perspective of aerobic respiration and anaerobic respiration, we fully consider the limitation of energy and the process of energy recovery, and establish Aerobic and Anaerobic Energy Fa- tigue Model. We fit the model to the obtained data using the ordinary least squares to verify the validity of the model, considering different types and genders of the riders. The power curves of different riders are provided, and the relationship between their features and model parameters was also explored. The specific results are shown in Figure 6 and its analysis.

<!-- b000010 | prose | pages [1] -->
Secondly, we establish an Optimal Individual Power Distribution Model to provide an optimal power allocation strategy, which describes the relationship between the power applied by the rider and the position on the track. A Single Objective Programming model is estab- lished, using the race time as the optimization objective, the rider state and track conditions as constraints, and the power applied by the rider as the decision variable. A resistance model is built to describe resistance and a track undulation and turn model are used to describe the track conditions. Based on above model and rider's power curve, we use dynamic program- ming to obtain the optimal power distribution strategy and corresponding shortest time. The effect of track conditions and rider status on rider power distribution was also investigated. Distribution diagrams of power output and discussions will be shown in Section 5.4.

<!-- b000011 | prose | pages [1] -->
Thirdly, we performed a sensitivity analysis for weather conditions, including wind direc- tion and wind speed. The previous resistance model was improved to wind resistance model. In 24 environments with eight directions of wind and three levels of wind speed, the shortest game time was calculated, as shown in Figure 13. Completion time has changed greatly, reach- ing a maximum of 16%, so the results are considered sensitive to weather conditions.

<!-- b000012 | prose | pages [1] -->
Fourthly, we performed a sensitivity analysis of rider deviations from the power distribu- tion strategy. We use MATLAB to randomly make change on optimal power distribution strat- egy, using the mean absolute value of the deviation between the rider's actual power output and the optimal power at each position as a measure of the degree of deviation. The relationship between completion time and degree of deviation is shown in Table 4. Completion time did not increase by 10% until the average deviation change reached 5%. Therefore, we believe that the model results are insensitive to rider deviation from target power. For a near-optimal time, the time reference ranges for each position of the track are shown in Table 5.

<!-- b000013 | prose | pages [1] -->
Finally, we consider the features of team time trial and generalize the individual game model to the Team Strategy Decision Model. We consider the effect of blocking wind among team members, modify the wind resistance model, and propose the draft strategy and drop strategy. In addition, we also provide a guidance for individual time trial.

<!-- b000014 | keywords | pages [1] -->
Keywords: Individual Time Trial, Power Curve, Optimal Power Distribution, Dynamic Pro-

<!-- b000015 | prose | pages [1] -->
gramming

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1 Introduction................................................................................................... 3

<!-- b000018 | contents | pages [2] -->
1.1 Problem Background ................................................................................................... 3

<!-- b000019 | contents | pages [2] -->
1.2 Restatement of the Problem ......................................................................................... 3

<!-- b000020 | contents | pages [2] -->
1.3 Literature Review ........................................................................................................ 4

<!-- b000021 | contents | pages [2] -->
1.4 Our Work..................................................................................................................... 4

<!-- b000022 | contents | pages [2] -->
2 Assumptions and Justifications .................................................................... 5

<!-- b000023 | contents | pages [2] -->
3 Definitions and Notations ............................................................................. 6

<!-- b000024 | contents | pages [2] -->
3.1 Definitions................................................................................................................... 6

<!-- b000025 | contents | pages [2] -->
3.2 Notations ..................................................................................................................... 6

<!-- b000026 | contents | pages [2] -->
4 Cyclist’s Physiological Model of Fatigue ..................................................... 6

<!-- b000027 | contents | pages [2] -->
4.1 The Establishment of the Model .................................................................................. 7

<!-- b000028 | contents | pages [2] -->
4.2 Result and Discussion .................................................................................................. 8

<!-- b000029 | contents | pages [2] -->
5 Optimal Individual Power Distribution Model ......................................... 10

<!-- b000030 | contents | pages [2] -->
5.1 Data Processing ......................................................................................................... 10

<!-- b000031 | contents | pages [2] -->
5.2 The Establishment of the Model ................................................................................ 11

<!-- b000032 | contents | pages [2] -->
5.3 Solve the Model ........................................................................................................ 14

<!-- b000033 | contents | pages [2] -->
5.4 Results and Analysis .................................................................................................. 14

<!-- b000034 | contents | pages [2] -->
6 Sensitivity Analysis...................................................................................... 17

<!-- b000035 | contents | pages [2] -->
6.1 Weather and Environmental Effects ........................................................................... 17

<!-- b000036 | contents | pages [2] -->
6.2 Deviation effects........................................................................................................ 18

<!-- b000037 | contents | pages [2] -->
7 Model Evaluation and Further Discussion ................................................ 19

<!-- b000038 | contents | pages [2] -->
7.1 Strengths ................................................................................................................... 19

<!-- b000039 | contents | pages [2] -->
7.2 Weaknesses ............................................................................................................... 19

<!-- b000040 | contents | pages [2] -->
7.3 Model Extension ....................................................................................................... 20

<!-- b000041 | contents | pages [2] -->
8 Conclusion ................................................................................................... 21

<!-- b000042 | contents | pages [2] -->
Men Elite Individual Time Trial Guidance .................................................. 22

<!-- b000043 | contents | pages [2] -->
References ...................................................................................................... 24

<!-- b000044 | contents | pages [2] -->
Appendix ........................................................................................................ 25

<!-- b000045 | heading | pages [3] -->
1 Introduction

<!-- b000046 | heading | pages [3] -->
1.1 Problem Background

<!-- b000047 | prose | pages [3] -->
There are many types of road cycling competitions, in which the individual time trial re- quires the cyclist to ride a certain distance alone, with the completion time as the result, and the one with the shortest time wins.

<!-- b000048 | prose | pages [3] -->
The curvilinear relationship between power output and its duration can serve as an essen- tial feature of high-intensity exercise, a concept known as a power curve. Essentially, this con- cept describes the tolerable duration of high-intensity exercise. It represents the maximum power an athlete can deliver over a certain period of time and has enormous potential applica- tions in optimizing athletic training programs and performance and improving the quality of life of individuals with chronic diseases [1].

<!-- b000049 | prose | pages [3] -->
Different types of riders have different shapes of power curves. In a given time-trial run, they need to manage their power distribution so that to finish the race in the least amount of time. Figure 1 shows a cyclist in competition.

<!-- b000050 | caption | pages [3] -->
Figure 1: A cyclist in competition [2]

<!-- b000051 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000052 | prose | pages [3] -->
Considering the background information and restricted conditions identified in the prob- lem statement, we need to develop a model to determine the optimal power distribution of one rider for one course and solve the following problems:

<!-- b000053 | prose | pages [3] -->
 Problem 1: Give the definition of power profiles for both types of riders, taking into account riders of different genders. One of the riders is a time trial specialist; the other is required to be of another type.

<!-- b000054 | prose | pages [3] -->
 Problem 2: Apply the above model to three specific time trial courses.

<!-- b000055 | prose | pages [3] -->
 Problem 3: Analyze the influence of weather conditions on model results and sensi- tivity of the model to this influence.

<!-- b000056 | prose | pages [3] -->
 Problem 4: Analyze the sensitivity of the model to deviation from the result power distribution.

<!-- b000057 | prose | pages [3] -->
 Problem 5: Discuss how to develop the model to provide the best power usage sce- nario for a six-person team competing in a team time trial.

<!-- b000058 | heading | pages [4] -->
1.3 Literature Review

<!-- b000059 | prose | pages [4] -->
The problem that this paper aims at is the power distribution of cyclist during cycling, which has been discussed in previous studies. Andrew M. Jones et al. introduced the power curve into intermittent high-intensity exercise, and used the existing two-parameter model (hy- perbolic relationship between power and duration) to make better predictions for athlete fatigue monitoring [3]. Morton extended the two-parameter model to a three-parameter model, and es- tablished a new power curve model [4]. Dr. Andrew Coggan et al. used a three-parameter model to analyze the advantages and disadvantages of different types of riders through statistical data, and obtained the corresponding power curve [5].

<!-- b000060 | prose | pages [4] -->
There is also a lot of research on how to properly distribute power for the rider to win. The critical power model of Monod and Scherrer is a widely recognized model for optimizing pace strategy and analyzing the endurance capacity of cyclists. It consists of two parts: infinite aerobic and limited anaerobic [6]. A more complex model is the three-component Morton-Mar- garia model, or the 3-Tank model [7], which is another feasible bioenergy model that provides a direction for research on power distribution in bicycle racing.

<!-- b000061 | heading | pages [4] -->
1.4 Our Work

<!-- b000062 | prose | pages [4] -->
We need a model that works for any type of rider to characterize the relationship between the rider's position on the track and the force applied. Our work mainly includes the following parts:

<!-- b000063 | prose | pages [4] -->
Firstly, we refer to previous literature and propose our Cyclist’s Physiological Model of Fatigue based on the three-Tank model, including aerobic energy fatigue model and anaerobic energy fatigue model. We used this model to explain the rider's power curve. After that, we performed least squares fitting on the curves of different riders, and used the obtained param- eters to distinguish riders into different categories.

<!-- b000064 | prose | pages [4] -->
Next, we established a resistance model dominated by aerodynamic resistance and rolling friction resistance, and revised the resistance model when considering the influence of weather conditions. In addition, we abstract the track as a function of ground undulation as a function of race schedule and curves as a function of race schedule. This is our Optimal Individual Power Distribution model. After that, we used the specific track data and the proposed fatigue physiological model to solve it by dynamic programming, and obtained the best power-race curve and the best finish time of the player on the track.

<!-- b000065 | prose | pages [4] -->
Then, we separately conduct sensitivity analysis to wind speed and direction and power deviation, and analyze the strengths and weaknesses of the model.

<!-- b000066 | prose | pages [4] -->
Finally, we generalized the model to team time trials. To account for the resistance reduc- tion effect between teams, we reworked the resistance model for individuals in team matches. After that, we considered the possible strategies in the team game—Draft and Drop, and took the positions of these strategies as new decision variables, and theoretically the optimal solution in the team game can be obtained.

<!-- b000067 | prose | pages [4] -->
For better understanding of the overall model, a flowchart is provided to describe our process.

<!-- b000068 | prose | pages [5] -->
Figure 2：Overview of our work

<!-- b000069 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000070 | prose | pages [5] -->
Considering that practical problems always contain many complex factors, first of all, we need to make reasonable assumptions to simplify the model, and each hypothesis is closely followed by its corresponding explanation:  Assumption 1: Cyclists will never be influenced by others during the race. According to the cycling individual time trial rules of UCI, the riders start alone at certain intervals.

<!-- b000071 | prose | pages [5] -->
So, the rider will not be influenced by others during the race.  Assumption 2: Energy of cyclists is limited during the race. On the one hand, this comes from the limitation of the topic, and on the other hand, cyclists usually do not supplement energy in actual races.  Assumption 3: The only sources of resistance are the viscous resistance of the air and the rolling friction of the ground. Because these two resistances account for the largest part [8], while the small resistance from the transmission efficiency of the bicycle chain can be ignored.  Assumption 4: Cyclists move in one dimension along the track, regardless of track width. This is a reasonable simplification of the model. Analysis of lateral motion intro- duces unnecessary complexity.  Assumption 5: The influence of weather on the players only exists in the wind direc- tion and speed, and does not consider the influence of rainfall or snowfall. This is a reasonable simplification of the model, as actual races are generally not played in harsher weather conditions.

<!-- b000072 | heading | pages [6] -->
3 Definitions and Notations

<!-- b000073 | heading | pages [6] -->
3.1 Definitions

<!-- b000074 | prose | pages [6] -->
Power-to-weight ratio: The ratio of the rider's output power to his own body weight. The higher the value, the stronger the climbing ability.

<!-- b000075 | prose | pages [6] -->
Functional Threshold Power: The maximum average power a rider can achieve during an hour of full and steady riding. It is an important indicator of a rider's aerobic capacity. Also known as lactate threshold, it is usually determined by testing.

<!-- b000076 | prose | pages [6] -->
Critical Power: The maximum average power a rider can get during a given period of time while riding with full force and stability.

<!-- b000077 | prose | pages [6] -->
Sharp turn: The turning angle is greater than or equal to 90 degrees within 50 meters.

<!-- b000078 | heading | pages [6] -->
3.2 Notations

<!-- b000079 | prose | pages [6] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000080 | caption | pages [6] -->
Table 1: Notations used in this paper

<!-- b000081 | heading | pages [6] -->
Symbol

<!-- b000082 | prose | pages [6] -->
Description Unit Aerobic respiratory energy output power W/Kg s-1 Consumption rate of aerobic pool energy ratio Anaerobic respiration energy output power W/Kg s-1 Consumption rate of anaerobic pool energy ratio Anaerobic energy storage J Time Duration s s-1 Recovery rate of anaerobic pool energy ratio Total output power of cyclist W/Kg Total resistance N Rider's Velocity Relative to Air m/s Rolling friction coefficient / Power provided by the rider N Position of the rider on the course m Slope angle of the course ° Altitude m Corners of the course / The angle between the travel direction and the wind direction ° Wind speed m/s Optimal decision function for draft / Note: There are some variables that are not listed here and will be discussed in detail in each section.

<!-- b000083 | heading | pages [6] -->
4 Cyclist’s Physiological Model of Fatigue

<!-- b000084 | prose | pages [6, 7] -->
We will now elaborate on our model. Based on the 3-Tank model, we propose an aerobic and anaerobic energy fatigue model, and use the least squares fitting curve to obtain the power- time curves of different types of players.

<!-- b000086 | heading | pages [7] -->
4.1 The Establishment of the Model

<!-- b000087 | heading | pages [7] -->
4.1.1 Power Curve Model

<!-- b000088 | prose | pages [7] -->
The three-Tank model [7] mentioned above theoretically holds that an aerobic source can provide unlimited energy. However, in the actual process, according to Assumption 2, the total energy is limited. So, we can assume that there is a negative correlation between aerobic res- piratory power and duration.

<!-- b000089 | prose | pages [7] -->
When a person is fully active, the power provided by aerobic respiration is limited due to the limited rate of aerobic respiration. When the output power exceeds the functional power threshold (FTP), anaerobic respiration is required to make up. So aerobic breathing power be- longs to an interval with an upper limit, and the consumption rate also has an upper limit.

<!-- b000090 | prose | pages [7] -->
From the above two points, combined with other energy models, we normalize the energy of the aerobic pool and define the rate at which the rider consumes the energy of the aerobic pool as:

<!-- b000091 | prose | pages [7] -->
(1) where, is aerobic respiratory energy output power. are both undetermined parameters.

<!-- b000092 | prose | pages [7] -->
When the output power exceeds the functional power threshold, the aerobic respiration power reaches saturation, and the excess part needs to be supplemented by anaerobic respira- tion. And the initial power of anaerobic respiration can be approximated as FTP.

<!-- b000093 | prose | pages [7] -->
From the two-parameter model, there is a hyperbolic relationship between the anaerobic respiration power and the duration, that is, the energy storage of the anaerobic energy pool is a fixed value. Therefore, the output power of the anaerobic respiration part can be expressed as:

<!-- b000094 | prose | pages [7] -->
(2)

<!-- b000095 | prose | pages [7] -->
where, represents the energy storage of the anaerobic energy pool. is time duration.

<!-- b000096 | prose | pages [7] -->
Considering that the higher the output power of the human body is, the faster the energy consumption is. According to the two-parameter model, we normalize the anaerobic energy pool to one, and define the rate at which the rider consumes the energy of the anaerobic energy pool as:

<!-- b000097 | prose | pages [7] -->
(3) where, is the ratio of the anaerobic energy consumption rate of the human body to the an- aerobic respiration output power.

<!-- b000098 | prose | pages [7] -->
Additionally, a cyclist may choose to temporarily exceed the limits of their power curve. However, after the output power drops below FTP, the cyclist needs additional time to restore the energy of the anaerobic energy pool at a lower power level, and we define the speed of the rider to restore the energy ratio of the anaerobic energy pool here.

<!-- b000099 | prose | pages [7] -->
(4)

<!-- b000100 | prose | pages [7] -->
where, is the coefficient of recovery, which means that when the output power exceeds the limit of the curve, the rider needs roughly twice the time to restore the stored energy in the energy pool.

<!-- b000101 | prose | pages [7] -->
Therefore, when the output power is kept constant, the time for the rider to maintain the power can be expressed as:

<!-- b000102 | prose | pages [8] -->
(5)

<!-- b000103 | prose | pages [8] -->
It should be noted that the above formula does not involve the recovery of anaerobic pool energy. This is because the rider keeps the power constant. When the output power is higher than FTP, the energy of the anaerobic pool is consumed and will not recover; when the output power is lower than FTP, the energy of the anaerobic pool will not be consumed.

<!-- b000104 | prose | pages [8] -->
To sum up, we can get the relationship between the total output power and the duration as:

<!-- b000105 | prose | pages [8] -->
(6)

<!-- b000106 | prose | pages [8] -->
where, are adjustment coefficients to ensure that the function satisfies . represents the rate of energy consumption when aerobic respiration supplies energy.

<!-- b000107 | heading | pages [8] -->
4.2 Result and Discussion

<!-- b000108 | heading | pages [8] -->
4.2.1 Model Validation

<!-- b000109 | prose | pages [8] -->
The above analysis provides a basic model for power-time curves for various types of cyclists. Parameters of different cyclists will differ due to their own conditions, thereby affect- ing their power-time curves. For different players, the specific power-time curve can be ob- tained by measurement to reflect various indicators, and then the consumption functions of the corresponding aerobic energy pool and anaerobic energy pool can be obtained, which is of great significance for fatigue monitoring and other aspects.

<!-- b000110 | prose | pages [8] -->
Using the data mentioned above, we conducted the least squares method to fit the curve, and the fitting results of the power-time curve are shown in Figures 4 and 5 below:

<!-- b000111 | caption | pages [8] -->
Figure 3: Curve Fitting Results for Men

<!-- b000112 | caption | pages [8] -->
Figure 4: Curve Fitting Results for Women

<!-- b000113 | prose | pages [9] -->
First of all, it should be noted that since human beings have limits in power output, the output power when the output time is very short is not considered. So, the image abscissa starts at 10s. To describe the rider's power curve more fairly, we consider the power applied by the rider normalized by weight as the ordinate.

<!-- b000114 | prose | pages [9] -->
From the above figure, from the fitting effect, the result curve of the two fits well with the original data, especially for segments where . The result curve of women is more in line with the original data than the result curve of men, which may be related to the accuracy and chance of the data, or it may be related to the conservative estimation of model parameters.

<!-- b000115 | prose | pages [9] -->
From the fitting results, the trend of the power time curves of men and women is the same, and the power decreases in an S-shaped manner with the increase of time. This is consistent with Assumption 2. The FTP of women is slightly smaller than that of men, but the limit power in a short time is higher than that of men. This reflects the effect of rider gender on that curve. The reason may be that women are lighter in weight and have higher power bursts for short periods of time, but weaker oxygen supply capacity for long periods of time. The difference between the two curves after a certain period of time is small, which indicates that in a rela- tively long period of riding, the difference caused by gender can be ignored.

<!-- b000116 | heading | pages [9] -->
4.2.2 Power curves of different types of riders

<!-- b000117 | prose | pages [9] -->
In addition to the gender of the rider, we should also consider the characteristics of differ- ent types of riders to determine their corresponding power-time curves. Sprinters need a lot of power against wind resistance, so they will have heavier body weight and muscle mass, and their anaerobic pools will have high energy storage, but their power-to-weight ratio will be less suitable for climbing. In order to resist gravity, the Puncheur is lighter in weight, has a low muscle limit, and a high sprinting ability, but it is inferior to sprinters. Rouleur is good in all aspects, has strong stamina, and is usually aggressive in attacking. In order to visually represent the relationship between the player's ability index and the model parameters, the radar chart of each type of rider's index is shown in Figure 5 below:

<!-- b000118 | caption | pages [9] -->
Figure 5: Metrics for all types of cyclists

<!-- b000119 | prose | pages [9, 10] -->
As shown above, select FTP, restore factor , the model parameters , body weight, anaerobic pool energy as indicators to characterize the output power of various types of riders. Different weights are given and normalized according to the characteristics of each type of rider. Based on this, we assign different parameter values to the above model to obtain the corresponding power-time curve, as shown in Figure 6:

<!-- b000121 | caption | pages [10] -->
Figure 6: Power time curves for various types of riders

<!-- b000122 | prose | pages [10] -->
The graph above shows the power-time curves for each type of rider. Due to the different abilities of various riders, the model parameters are different, and so are the curves. The anal- ysis leads to the following conclusions, which are consistent with the radar chart:

<!-- b000123 | prose | pages [10] -->
 Rouleur is balanced in all aspects, so his/her power-time curve is in the middle section as a whole. His/Her sprint ability is strong, and he/she can also maintain a certain power during long-term riding.

<!-- b000124 | prose | pages [10] -->
 The Sprinter has a strong sprinting ability, and his/her power-time curve presents a very high front, that is, the extreme power is very large in a short time, which is suit- able for short-term explosive riding. He/She has a relatively prominent anaerobic en- ergy supply capacity and a large anaerobic pool energy storage.

<!-- b000125 | prose | pages [10] -->
 Puncheur has poor endurance, and his/her power-time curve is generally low, with a certain explosive power in a short period of time. The anaerobic energy supply ca- pacity is slightly better.

<!-- b000126 | prose | pages [10] -->
 The time trial specialist has the strongest comprehensive ability, and can maintain a high power during a long-term riding process. He/She has a relatively prominent aer- obic energy supply capacity and a high FTP, which corresponds to a larger aerobic energy supply rate in the above model.

<!-- b000127 | heading | pages [10] -->
5 Optimal Individual Power Distribution Model

<!-- b000128 | prose | pages [10] -->
By analyzing the force of the rider during the riding process, combined with the track conditions, we propose an Optimal Individual Power Distribution Model, and use the dynamic programming method to find the optimal power distribution suitable for riding.

<!-- b000129 | heading | pages [10] -->
5.1 Data Processing

<!-- b000130 | prose | pages [10] -->
We need to apply the first model built to three specific tracks. So, we need to collect the altitude data and camber data of the track. The relevant datasets and source websites are shown in Table 2:

<!-- b000131 | caption | pages [10] -->
Table 2: Data and Database Websites

<!-- b000132 | prose | pages [10, 11] -->
Database Names Database Websites Altitude and camber of Olympic Time Trial course https://olympics.com/ in Tokyo, Japan Altitude and camber of UCI World Championship https://www.flanders2021.com/ time trial course in Flanders, Belgium

<!-- b000134 | prose | pages [11] -->
In order to facilitate research analysis and application to modeling, we present the col- lected data in the form of a function graph in Figure 7:

<!-- b000135 | caption | pages [11] -->
Figure 7: Altitude and Camber of the Course

<!-- b000136 | prose | pages [11] -->
From the figure, the top left picture among the three represents the data of the Tokyo Olympics time trial, the top right picture represents the data of UCI time trial, and the bottom picture is the data of self-designed track. In fact, in the UCI time trial, the men's and women's runners have different tracks. In the Olympics Time Trial, the men and women use the same track, but the men run an extra lap. Due to space limitations, the specific situation will be given in detail in the result analysis.

<!-- b000137 | prose | pages [11] -->
We can see that the UCI time trial track has a lower altitude, is flatter but has slightly more corners. The track of the Olympics Time Trial Circuit has a higher altitude, is steeper, has fewer turns, and the turns are concentrated in the first half of the track. The altitude of our self-de- signed track is in between the two, the slopes are concentrated in the first half and the end of the race, and there are five corners, which are concentrated in the second half of the race. The purpose of our design is to distinguish between slopes and corners to a certain extent, so that it is convenient to study the effect of the two on the rider's power separately.

<!-- b000138 | heading | pages [11] -->
5.2 The Establishment of the Model

<!-- b000139 | prose | pages [11] -->
In the process of establishing the model, we mainly consider the resistance of the rider during his cycling, analyze the force of the rider, and propose a Riding Resistance Model.

<!-- b000140 | heading | pages [11] -->
5.2.1 Riding Resistance Model

<!-- b000141 | prose | pages [11] -->
In individual races, the interference effects of other riders are not considered. Therefore, we consider that the resistance received by the rider during the riding process is mainly com- posed of two parts, one of which is aerodynamic resistance, and the other is the rolling friction between the bicycle and the ground. According to the experimental research of others [8], we give the total resistance received by the rider in the process of flat ground movement as:

<!-- b000142 | prose | pages [12] -->
(7) where, is the fluid density, and it is the air density here. is the frontal area of the total projection of the rider and the bicycle, that is, the effective area. is the resistance coeffi- cient. is the speed of the rider relative to the fluid. is the coefficient of rolling friction.

<!-- b000143 | prose | pages [12] -->
is the total mass of the rider and bike. is the gravitational acceleration.

<!-- b000144 | prose | pages [12] -->
In order to obtain a more specific expression, we discuss the above parameters to directly use the existing data to facilitate the solution. For fluid density we have:

<!-- b000145 | prose | pages [12] -->
(8)

<!-- b000146 | prose | pages [12] -->
(9) where, is a constant, the general value is 1.293Kg/m3. is air pressure. is the tem- perature in Kelvin. is the local altitude.

<!-- b000147 | prose | pages [12] -->
For the projected effective area, we have:

<!-- b000148 | prose | pages [12] -->
(10) where, are the rider's height and weight, respectively. is the horizontal declination angle of the rider's helmet, in order to simplify the problem, we take its value as zero.

<!-- b000149 | prose | pages [12] -->
For the resistance coefficient, we have:

<!-- b000150 | prose | pages [12] -->
(11) Considering the coefficient of rolling friction, according to empirical data [9], the coeffi- cient of rolling friction of mountain bikes on asphalt roads is 0.003, while the coefficient of rolling friction of road bicycles is usually smaller. Since rolling friction accounts for about 10% of the total resistance, and in order to simplify the problem, we do not consider the material of the track, we take .

<!-- b000151 | heading | pages [12] -->
5.2.2 Abstract Course Model

<!-- b000152 | prose | pages [12] -->
For the individual cycling track, we mainly consider the situation analysis of the rider going up and down and turning during the riding process.

<!-- b000153 | prose | pages [12] -->
For the uphill process, we simplify the rider as a mass point and perform force analysis on it, as shown in Figure 8:

<!-- b000154 | caption | pages [12] -->
Figure 8: Analysis of the rider's force during the uphill process

<!-- b000155 | prose | pages [12] -->
As shown in the above analysis, we can simply get the physical model of the uphill process:

<!-- b000156 | prose | pages [12] -->
(12)

<!-- b000157 | prose | pages [12, 13] -->
Where, is the motivation provided to the rider, which is related to the power provided by the rider. is the slope angle, when the rider is going downhill, it is an obtuse angle.

<!-- b000159 | prose | pages [13] -->
It should be pointed out that the force analysis of the rider in the process of going downhill is the same as the force analysis in the process of going uphill, and the above physical model is applicable to both scenarios.

<!-- b000160 | prose | pages [13] -->
For the curve process, in order to simplify the model and calculation, we consider the process as a circular motion. We perform a simple force analysis on it, as shown in Figure 8:

<!-- b000161 | caption | pages [13] -->
Figure 9: Analysis of the rider's force in the process of turning

<!-- b000162 | prose | pages [13] -->
According to the graph above, in the tangential direction of the corner, the rider is exposed to the total resistance as well as the power provided by himself. This is in line with what a rider would do when riding on straight roads.

<!-- b000163 | prose | pages [13] -->
In the radial direction, the combined force of the rider's gravity and the supporting force of the road surface provides the centripetal force. However, due to the limited inclination of the rider to the road during cornering, the resultant force is limited. Therefore, during a turn, the rider's speed cannot exceed a certain threshold. In addition, we divide the corners into two categories according to the size of the turning radius, sharp turns and soft turns.

<!-- b000164 | prose | pages [13] -->
From this, we get the processing method for the curve process:

<!-- b000165 | prose | pages [13] -->
 For the sharp turning process, the speed of the rider should not be too high, and the rider should reduce the output power to lower the speed below this threshold, other- wise the turning process cannot be completed. That is to say, we consider the corners to be speed checkpoints on the track, which can only be passed below the speed threshold.

<!-- b000166 | prose | pages [13] -->
 For the soft turning process, we regard it as a straight course and do not do special treatment.

<!-- b000167 | prose | pages [13] -->
We represent the track elevation map obtained earlier as a function of altitude as a function of the rider's position on the track . We think the rider is on an uphill course when the altitude goes up and downhill when the altitude goes down. Therefore, by taking the deri- vation of this function, we can get the slope angle as a function of the rider's position on the track .

<!-- b000168 | prose | pages [13] -->
In the same way, since we simplified the curve model, we only consider whether the cur- rent position of the rider is a straight or a curve, and do not care about the radius of the curve. So we express the camber of the track as a binary function ，that is：

<!-- b000169 | prose | pages [13] -->
(13)

<!-- b000170 | prose | pages [13] -->
where, is the position of each corner in the track.

<!-- b000171 | prose | pages [14] -->
Through the above analysis, we summarize the basic idea of modeling as shown in below:

<!-- b000172 | caption | pages [14] -->
Figure 10: The framework of the model

<!-- b000173 | heading | pages [14] -->
5.3 Solve the Model

<!-- b000174 | prose | pages [14] -->
We need to use the existing model to obtain the optimal power distribution of the rider in a race while ensuring that the energy of the aerobic pool and the anaerobic pool is not less than zero, so that the rider can reach the destination in the shortest time. Therefore, solving the model using a dynamic programming algorithm is a good choice.

<!-- b000175 | prose | pages [14] -->
The dynamic programming algorithm is an algorithm that divides the problem and defines the relationship between the state of the problem and the state, so that the problem can be solved in a recursive way. When applying this method to the above model, the main ideas are:

<!-- b000176 | prose | pages [14] -->
 Break the original problem into sub-problems. Divide the track into a certain num- ber of small sections, and find the minimum time to complete this part of the track when each section has the same amount of aerobic energy remaining, anaerobic en- ergy remaining, and the end speed. Gradually increase with the schedule until the entire track is covered. Then the minimum time to complete the track is the minimum time calculated under the condition of any remaining aerobic energy, anaerobic en- ergy remaining, and ending speed.

<!-- b000177 | prose | pages [14] -->
 Determine the status. When the remaining amount of aerobic energy is , the re- maining amount of anaerobic energy is , and the end speed is , the minimum time consumed by meters before completion.

<!-- b000178 | prose | pages [14] -->
 Given an initial value. The initial velocity is zero, the residual amount of aerobic energy is one, and the residual amount of anaerobic energy is one.

<!-- b000179 | prose | pages [14] -->
 State transition. For every segment, the value of its state function may come from all state values of the previous segment of the track. Therefore, we try all power for all state values of the previous segment of the track. If it transitions to its own state, record it. Take the minimum value after the traversal is complete.

<!-- b000180 | prose | pages [14] -->
It should be noted that, except for time, all values are discretized to ensure incremental traversal. When the difference between the values is sufficiently small, the resulting value can be considered accurate.

<!-- b000181 | heading | pages [14] -->
5.4 Results and Analysis

<!-- b000182 | prose | pages [14] -->
Taking into account the gender and type of runners, when applying the model to the track, we discussed the Time Trial Specialists and Sprinters divided into male and female runners.

<!-- b000183 | prose | pages [15] -->
In the three tracks, the power distribution strategies of the two types of male riders are shown in Figure 11 below:

<!-- b000184 | prose | pages [15] -->
Type Sprinter Time Trial Specialist

<!-- b000185 | prose | pages [15] -->
Tokyo

<!-- b000186 | prose | pages [15] -->
Belgium

<!-- b000187 | prose | pages [15] -->
Own design

<!-- b000188 | caption | pages [15] -->
Figure 11: Men's Rider Power Distribution Strategy

<!-- b000189 | prose | pages [15] -->
Based on the graph above, we got the optimal power distribution for different types of riders. According to this strategy, the corresponding power is applied at the corresponding po- sition of the race schedule, and the rider will complete the race in the shortest time under his own conditions. When the curve increases sharply, the rider should initiate a sprint; when the curve drops sharply, the rider should reduce the power to restore the energy of the anaerobic pool; most of the time, the curve fluctuates around the FTP, and the rider should maintain a relatively stable power to ride. We have also plotted the changes in anaerobic pool energy and aerobic pool energy to testify to this. Details can be found in the appendix. Furthermore, we can draw the following conclusions:

<!-- b000190 | prose | pages [15, 16] -->
 The power distribution strategies of various types of riders on the same track are basically the same. It can be seen from the foregoing that different types of riders have power curves with similar trends. When they are applied to the same track con- ditions, the power distribution strategies obtained have the same trend.

<!-- b000192 | prose | pages [16] -->
 Riders need to sprint more frequently in high-altitude races. While the average resistance at higher altitudes is less than it at lower altitudes, the gradients are more variable, so riders need to increase power to climb and then lower to recover. There- fore, on denser hills, the rider's power fluctuates more. At the same time, this also shows that the effect of gravity on the rider is greater than that of resistance.

<!-- b000193 | prose | pages [16] -->
 Turning reduces the power output to the rider. It can be seen from the self-de- signed track that the rider has a certain degree of power reduction in the corners. This is also consistent with our previous analysis.

<!-- b000194 | prose | pages [16] -->
 The Sprinter can launch a more powerful attack in the first half of the schedule than the Time Trial Specialist. Comparing the above picture horizontally, in the first half of the race, we can see that the power peak corresponding to the sprint initiated by the Sprinter is higher. In the second half of the race, the number of sprints and power peaks were slightly reduced due to the Sprinter's slightly poorer endurance.

<!-- b000195 | prose | pages [16] -->
 The Sprinter is less affected by corners than the Time Trial Specialist. At Tokyo, where the corners are denser, the Sprinter has fewer power cuts. This may be related to the lower average power of this type of riders.

<!-- b000196 | prose | pages [16] -->
 Sprinter is more affected by altitude than Time Trial Specialist. At the higher elevation and steeper slope changes at the Olympics track, the Sprinter's power curve has a lower center of undulation and lower average power.

<!-- b000197 | prose | pages [16] -->
Due to space limitations, the optimal power strategy graph for the women's race and the women's UCI track map are attached in the appendix. Due to the difference between the men's and women's tracks in the Olympics track and the UCI track, in order to control the variables, we only analyze the tracks designed by ourselves, and we can draw the following conclusions:

<!-- b000198 | prose | pages [16] -->
 The average power of women is lower than that of men. It can be seen that the power curve of women is generally lower.

<!-- b000199 | prose | pages [16] -->
 Women's sprint intensity in the first half of the race can reach higher, even more than the men's. The women's power curve peaked higher in the first half of the race.

<!-- b000200 | prose | pages [16] -->
 Women are more affected by slopes and curves than men. The women's power map fluctuates more often on successive ramps and corners.

<!-- b000201 | prose | pages [16] -->
In addition, we present a statistical graph of the minimum time required by the rider, providing intuitive data for analysis. As shown in Figure 12 below:

<!-- b000202 | caption | pages [16] -->
Figure 12: Minimum time spent by the rider

<!-- b000203 | prose | pages [17] -->
Through this graph, we give the specific time of different riders under the optimal power distribution. As mentioned above, we only refer to the self-designed track for comparison be- tween men and women. It can be seen that the men's players have a shorter time, 172s ahead of the women's players, and the average power is higher. In addition, the overall time of the Time Trial Specialist is shorter than that of the Sprinter, and the average score is about 300s ahead of the latter. Their average power is higher, their comprehensive ability is stronger, and they are less affected by altitude. Especially at high altitudes, the former leads the latter by 371s, which is the largest difference between the two among the three tracks. This is in great agreement with our previous model, while validating the validity and rationality of the model.

<!-- b000204 | heading | pages [17] -->
6 Sensitivity Analysis

<!-- b000205 | heading | pages [17] -->
6.1 Weather and Environmental Effects

<!-- b000206 | prose | pages [17] -->
The model was revised to account for the potential effects of weather. We considered the effect of wind direction and wind strength (i.e. wind speed) on the model parameters and made new assumptions:

<!-- b000207 | prose | pages [17] -->
Wind direction and wind speed are only functions related to space, forming a vector field of wind in space, regardless of time. And we consider the wind as only horizontal air flow. This is due to the slow change of wind speed and direction on the field, and usually only the average wind speed within an hour is detected. Table 3 below gives the wind speed and direction data we used [10]:

<!-- b000208 | caption | pages [17] -->
Table 3: Direction and Speed of the Wind in Course

<!-- b000209 | prose | pages [17] -->
Tokyo Belgium Data Men Women Men Women Wind direction(°) 270 290 050 010 Wind speed(m/s) 0.5 1.0 2.0 6.0

<!-- b000210 | prose | pages [17] -->
The effect of wind on the model results is only due to air resistance. To simplify the model, we only consider wind in the same or opposite direction as the rider's travel to have an effect on the travel, wind in the vertical direction does not affect the ride. From this, we correct the total resistance in the previous model to be:

<!-- b000211 | prose | pages [17] -->
(14) where, is the angle between the traveling direction and the wind direction (less than or equal to the flat angle), which is essentially function of , denoted by . is the symbolic function. are the horizontal speed of the rider and the wind speed, respec- tively.

<!-- b000212 | prose | pages [17] -->
To sum up, the new model is an improvement of the original model. We can solve the model using the above data and similar methods, and modify the values of wind direction and speed to analyze the sensitivity.

<!-- b000213 | prose | pages [17] -->
In order to explore the influence of weather conditions on the results, we took the perfor- mance of women on the UCI track as an example, and set up 8 wind directions and 3 wind levels, with a total of 24 wind environments. In these environments, we simulated the perfor- mance of athletes in the wind. The results obtained are presented in Figure 13:

<!-- b000214 | caption | pages [18] -->
Figure 13: Finishing times in different weather conditions

<!-- b000215 | prose | pages [18] -->
The wind direction adopts eight gradient settings of due north, due south, due west, due east, northeast, southeast, northwest, and southwest; the wind speed is set with three gradient settings of 1m/s, 2m/s and 3m/s.

<!-- b000216 | prose | pages [18] -->
According to the above figure, When the wind direction is constant, every time the wind speed changes by one level, the completion time will change by 20~330s, and the change pro- portion is less than 10%. When the wind is constant, each time the wind direction changes in one direction, the completion time will change by 30~460s, and the maximum change ratio is 16%. Therefore, considering the influence of two factors, we believe that our model is more sensitive to changes in the weather environment.

<!-- b000217 | heading | pages [18] -->
6.2 Deviation effects

<!-- b000218 | prose | pages [18] -->
During a race, the rider cannot accurately implement the determined optimal power dis- tribution strategy. For example, the rider did not increase to optimal power on a stage where he should have increased power. Thus, the rider's power position curve is likely to deviate from the optimal curve. To simulate this deviation, we randomly change the optimal power distribu- tion curve so that the rider may output sub-optimal power at any position. We use the average absolute value of the deviation of the rider's actual output power curve from the optimal power curve at all positions as the degree to which the rider deviates from the optimal curve.

<!-- b000219 | prose | pages [18] -->
We use random numbers to generate non-optimal power distributions and plug them into the model to solve for the corresponding finish times, as shown in Table 4:

<!-- b000220 | caption | pages [18] -->
Table 4: Non-optimal Finish Time

<!-- b000221 | prose | pages [18] -->
Mean devia- 0 0.06 0.07 0.08 0.09 0.1 0.15 0.2 tion(W/Kg) Finish time(s) 4001.5 4010.8 4144.1 4159.9 4174.4 4196.7 4200.0 4325.7 Delta-time(s) 0 +9.3 +142.6 +158.4 +172.9 +195.2 +198.5 +324.2 Percentage of 0 0.232 3.563 3.959 4.142 4.878 4.961 8.101 change(%)

<!-- b000222 | prose | pages [18, 19] -->
From the data in the table, we can find that as the deviation value increases, the completion time of the rider gradually increases, which verifies that our model is indeed the best solution to a certain extent. When the average deviation is below 0.06, the variation in completion time is small, less than 0.5%. After the deviation increases to a certain value between 0.06 and 0.07, the change in the completion time increases, but is less than 5%. But when the average devia- tion is between 0.15 and 0.2, the variation of completion time increases greatly, more than 5%. If the average deviation continues to increase, the rider will not be able to finish the race properly due to not meeting the finite energy limit.

<!-- b000224 | prose | pages [19] -->
After the above analysis, when the average deviation changes by about 5%, the comple- tion time changes by about 10%. Therefore, we believe that the model results have some in- sensitivity to the rider's deviation from the target power.

<!-- b000225 | prose | pages [19] -->
Additionally, we divided the entire course into sections. The endpoint of each segment is a checkpoint. Through multiple simulations, we get the time frame for reaching each check- point. If the rider arrives at these checkpoints within these ranges, the final finish time is guar- anteed to be no later than 1 minute after the optimal finish time. Table 5 shows the acceptable time range for arriving at each checkpoint after dividing the UCI Men's ITT circuit into 11 segments.

<!-- b000226 | caption | pages [19] -->
Table 5: Acceptable time range at each checkpoint

<!-- b000227 | prose | pages [19] -->
Dis- 4 8 12 16 20 24 28 32 36 40 tance(Km) Max time(s) 287 717 1188 1469 1856 2193 2518 3035 3316 3710 Min time(s) 283 703 1148 1429 1815 2152 2477 2974 3274 3665

<!-- b000228 | heading | pages [19] -->
7 Model Evaluation and Further Discussion

<!-- b000229 | heading | pages [19] -->
7.1 Strengths

<!-- b000230 | prose | pages [19] -->
Our model offers the following strengths:

<!-- b000231 | prose | pages [19] -->
We performed a more in-depth analysis of the three-tank model and proposed aero- bic and anaerobic energy fatigue models. Drawing on the research of others, we divided rider’s power output into aerobic and anaerobic components. Finally, we found that our model fits the data fairly well. The validity of the model has been verified.

<!-- b000232 | prose | pages [19] -->
Considering a variety of factors, a rider track model is proposed. In this process, we considered various factors such as the rider's energy consumption limit and stress situation, the slope and camber of the track, wind direction and speed, etc., which is more comprehensive.

<!-- b000233 | prose | pages [19] -->
The model is highly generalizable. When building model, we started with an individual time trial. Then we revised the model based on the characteristics of the team competition, and proposed the Draft strategy to generalize the model to be suitable for team time trials.

<!-- b000234 | heading | pages [19] -->
7.2 Weaknesses

<!-- b000235 | prose | pages [19] -->
Our model has the following limitations and related improvements:

<!-- b000236 | prose | pages [19] -->
In the Anaerobic Energy Fatigue Model, we treat the recovery factor as a constant. Doing so simplifies the model but reduces the authenticity of the model to some extent. In fact, due to loss of energy, it is more appropriate to describe the recovery factor as a variable.

<!-- b000237 | prose | pages [19, 20] -->
In the construction of the Optimal Individual Power Distribution Model, the consid- eration of the Abstract Course Model is relatively simple. We only care about whether there is a turn at a certain position on the race schedule, and do not consider the size of the corner radius. Although the model is simplified, the authenticity of the model is weakened. In fact, this factor may affect a rider's low-power ride time, which in turn affects the results.

<!-- b000239 | heading | pages [20] -->
7.3 Model Extension

<!-- b000240 | prose | pages [20] -->
In this section, we mainly discuss the generalization of the model. The context for the model we built earlier was the individual time trial. As for the team time trial, Aristotle once said: "A team is more than the sum of its parts." So, we need to further modify the model.

<!-- b000241 | prose | pages [20] -->
According to the rules of the team time trial given by UCI [11], different teams should keep a certain distance, the team members should not push each other, and the following auxiliary vehicles should not be used. Therefore, the influence between teams and other factors that af- fect resistance, motivation and energy consumption are ignored. The important thing is that in team time trial, the front players can reduce drag for the rear players by arranging in front and back. Therefore, the main difference between team time trial and individual time trial is that we need to consider the different resistance between different riders.

<!-- b000242 | prose | pages [20] -->
The resistance model needs to be revised first as follows:

<!-- b000243 | prose | pages [20] -->
(15)

<!-- b000244 | prose | pages [20] -->
where, is a constant, related to the total number of riders and the position of the rider in

<!-- b000245 | prose | pages [20] -->
the cohort.

<!-- b000246 | prose | pages [20] -->
When the total number of team members is 6, the values in the expression of resistance received by riders at various positions are shown in Table 6 below:

<!-- b000247 | caption | pages [20] -->
Table 6: Resistance coefficient of players at different positions

<!-- b000248 | prose | pages [20] -->
Sequence First Second Third Fourth Fifth Sixth (%) 95 68 67 67 67 69

<!-- b000249 | prose | pages [20] -->
Furthermore, the decisions we need to consider are not limited to when to speed up and when to slow down. To make good use of the drag reduction brought by the team, the team as a whole needs to remain relatively static and move forward at a certain team speed. Because the players at the back of the team face less resistance, the movement is more labor-saving, and the players at the front are more laborious.

<!-- b000250 | prose | pages [20] -->
In team time trial, teams tend to use "Draft" to achieve the balance of team workload. The process of "Draft" is: the first player of the team moves laterally out of the queue, making the second player the leader of the team, then the first player of the team slows down, moves to the tail of the team. A schematic diagram of the process (taking four players as an example) is shown in Figure 14:

<!-- b000251 | caption | pages [20] -->
Figure 14: The strategy of Draft

<!-- b000252 | prose | pages [21] -->
So when and where to "draft" is a key decision in team time trials. So, we define a discrete- valued function to represent the replacement case:

<!-- b000253 | prose | pages [21] -->
(16)

<!-- b000254 | prose | pages [21] -->
where, is the position that needs to be drafted in the schedule.

<!-- b000255 | prose | pages [21] -->
This function provides a new decision variable, and we can find the optimal solution through more complex dynamic programming.

<!-- b000256 | prose | pages [21] -->
In addition, since the competition is based on the performance of the fourth team member, we can combine the different abilities of different team members and discard the weak players at certain points during the march to obtain better results.

<!-- b000257 | prose | pages [21] -->
There are more strategies in team time trials. In order to highlight the goal, we only select a representative strategy to simplify the decision. We can also consider that the rider who was at the front of the team does not move to the tail, but exchanges positions with the second rider or returns to other positions other than the tail of the team. This can also be modified according to the different ability levels of different riders.

<!-- b000258 | prose | pages [21] -->
In the team time trials, based on our previous model, we can consider more constraints and decision variables, and propose an improved model to solve with more complex dynamic programming. Due to space limitations, the solution process of the model is not described here.

<!-- b000259 | heading | pages [21] -->
8 Conclusion

<!-- b000260 | prose | pages [21] -->
In this paper, we establish a model suitable for various types of riders to analyze the rela- tionship between the power that the rider should apply and the position of the race, and give the optimal power distribution strategy.

<!-- b000261 | prose | pages [21] -->
First, we established aerobic and anaerobic energy fatigue models. On this basis, we quan- titatively give power curves for different rider types and genders, and use model parameters to define different types and genders of cyclists.

<!-- b000262 | prose | pages [21] -->
Secondly, we consider the force of the rider, the slope of the track and the cornering situ- ation, and combine the power curve of the player to establish Optimal Individual Power Dis- tribution Model. We used dynamic programming to obtain the optimal power distribution dia- gram for different cyclists. In addition, we also give the characteristics of different players' adaptability to different track environments, such as slopes and corners, and calculated their shortest time.

<!-- b000263 | prose | pages [21] -->
Thirdly, we take into account wind direction and speed to make corrections to the model, and perform a sensitivity analysis for weather conditions. We found that a 1m/s change in wind speed resulted in a change of no more than 10% in the results, and a 45-degree change in wind direction caused a change in the results by no more than 16%. So, we think our model is more sensitive to wind direction and wind speed. We also investigated the sensitivity of the model to deviation of the power distribution, only to find that our model is not sensitive to the deviation. Then we gave the acceptable range of deviation.

<!-- b000264 | prose | pages [21] -->
Finally, we consider the effect of wind resistance on the team and generalize the individual time trial model to the team time trial model. We give considerations about draft and drop strategies. And at the end of the paper, we provide a race guide for rider and the Directeur.

<!-- b000265 | prose | pages [22] -->
Men Elite Individual Time Trial Guidance

<!-- b000266 | prose | pages [22] -->
—— 2021 UCI World Championships in Flanders, Belgium

<!-- b000267 | heading | pages [22] -->
1. Analysis of the Race Track and Weather

<!-- b000268 | prose | pages [22] -->
The competition takes place in the Belgian province of Flanders. Riders need to travel from Knokke Heist to Bruges in northern Belgium.

<!-- b000269 | prose | pages [22] -->
The height fluctuation of the race track is shown in figure 1. The total length of the track is 43.3 kilometers, the average altitude is 15m, the range is 15m, and the standard deviation is only 3m. The track is flat and is more suitable for Flat Time Trial Specialist.

<!-- b000270 | caption | pages [22] -->
Figure 1: Elevation map of the track

<!-- b000271 | prose | pages [22] -->
The track has 7 sharp turns, which are 1.5km, 2.4km, 2.7km, 11.2km, 14.3km, 17.6km and 27.6km. NOTE: Riders need to slow down early when going through these corners. It is recommended to control the speed below 10m/s to avoid rushing out of the track.

<!-- b000272 | prose | pages [22] -->
According to the Zeebrugge Weather Observatory data provided by NOAA, the wind di- rection is 50° north by east at 16:00, on the day of the competition, that is, on September 19, 2021. The wind speed is 2m/s. It is downwind. The effect of wind on performance is about 1%, about ±10s.

<!-- b000273 | heading | pages [22] -->
2. Analysis of the Cyclist's Profile

<!-- b000274 | prose | pages [22] -->
Based on the given rider data, the rider's power curve can be obtained and is listed in

<!-- b000275 | caption | pages [22] -->
figure 2. His FTP is 4.79W/kg, so his aerobic respiration can provide high power efficiency.

<!-- b000276 | prose | pages [22] -->
His total anaerobic energy is 56.28J/Kg, so his anaerobic respiration has poor short-term power efficiency. That means his staying power is good, but his short-term explosiveness is poor.

<!-- b000277 | prose | pages [22] -->
He's the quintessential Flat Time Trial Specialist. He is more suitable for riding on flat terrain with few hills, which is in line with the characteristics of the track. Below is his power curve.

<!-- b000278 | caption | pages [22] -->
Figure 2: The power curve of a Time Trial Specialist

<!-- b000279 | heading | pages [23] -->
3. Overview of the Directions

<!-- b000280 | prose | pages [23] -->
By comprehensively analyzing the track model and the player's model, we can obtain the recommended power-distance distribution diagram for this rider who wants to achieve the best results. The P-D diagram is shown in Figure 3 below.

<!-- b000281 | caption | pages [23] -->
Figure 3: The P-D diagram

<!-- b000282 | prose | pages [23] -->
As can be seen, there are several key nodes that require more force to accelerate. Besides, there are also nodes that need to reduce power to restore stamina, including reducing power in downhill positions, and before sharp turns. The rider recommended to increase the output power at x=1km, 9.6km, 17.8km and other positions to complete the acceleration; while at x=1.6km, 2.7km and other positions to reduce power output to about 1W/kg. The rest of the time, try to maintain near the FTP, that is, the maximum value of aerobic respiration.

<!-- b000283 | prose | pages [23] -->
Completing the entire track according to this curve can optimize the performance of the players, and the estimated finishing time is 3499s (58m 19s).

<!-- b000284 | prose | pages [23] -->
However, it is impossible to highly detailed follow the above power distribution. Small deviations in power output still yield near-optimal results. So, we provide acceptable time frames for riders to reach some positions, part of which are shown in the table below. As long as the range of players arriving at these positions is within the Max Time and Min Time, the final finishing time can be no later than 57h 19s , 1min later than the optimal time.

<!-- b000285 | caption | pages [23] -->
Table 1: Time constraints

<!-- b000286 | prose | pages [23] -->
Distance(Km) 4 8 12 16 20 24 28 32 36 40 Max time(s) 287 717 1188 1469 1856 2193 2518 3035 3316 3710 Min time(s) 283 703 1148 1429 1815 2152 2477 2974 3274 3665

<!-- b000287 | heading | pages [23] -->
4. Summary of Our Model

<!-- b000288 | prose | pages [23] -->
Our model starts from studying the aerobic and anaerobic respiration of the rider and de- termines the relationship between energy expenditure and power output. The model depicts the rider's energy profile, which is expressed externally as a power curve. For any given track, we simulate the relationship between the rider state and various resistances on the track. When combining the above models, we use dynamic programming to obtain the relationship between optimal output power and track position, which has great reference value for the rider. The best results are achieved as long as the rider performs for the given power output. In order to reduce the difficulty of the players' execution, we provide a relatively loose reference time, which can get close to the best results.

<!-- b000289 | furniture | pages [23] -->
Team # 2209466

<!-- b000290 | heading | pages [24] -->
References

<!-- b000291 | references | pages [24] -->
[1]. Poole, David C et al. “Critical Power: An Important Fatigue Threshold in Exercise

<!-- b000292 | references | pages [24] -->
Physiology.” Medicine and science in sports and exercise vol. 48,11 (2016): 2320-

<!-- b000293 | references | pages [24] -->
2334. doi:10.1249/MSS.0000000000000939

<!-- b000294 | references | pages [24] -->
[2]. https://commons.wikimedia.org/w/index.php?search=road+cycling

<!-- b000295 | references | pages [24] -->
[3]. Jones, A.M., Vanhatalo, A. The ‘Critical Power’ Concept: Applications to Sports Per-

<!-- b000296 | references | pages [24] -->
formance with a Focus on Intermittent High-Intensity Exercise. Sports Med 47, 65–

<!-- b000297 | references | pages [24] -->
78 (2017).

<!-- b000298 | references | pages [24] -->
[4]. Morton RH. A 3-parameter critical power model. Ergonomics. 1996 Apr;39(4):611-

<!-- b000299 | references | pages [24] -->
619. DOI: 10.1080/00140139608964484. PMID: 8854981.

<!-- b000300 | references | pages [24] -->
[5]. Coggan, Andrew R. “Training and racing using a power meter: an introduction.”

<!-- b000301 | references | pages [24] -->
(2003).

<!-- b000302 | references | pages [24] -->
[6]. Monod, H., & Scherrer, J. (1965). The work capacity of a synergic muscular group.

<!-- b000303 | references | pages [24] -->
Ergonomics, 8(3), 329-338.

<!-- b000304 | references | pages [24] -->
[7]. Morton, R. H. (1986). A three component model of human bioenergetics. Journal of

<!-- b000305 | references | pages [24] -->
mathematical biology, 24(4), 451-466.

<!-- b000306 | references | pages [24] -->
[8]. Crouch, T.N., Burton, D., LaBry, Z.A. et al. Riding against the wind: a review of

<!-- b000307 | references | pages [24] -->
competition

<!-- b000308 | references | pages [24] -->
cycling

<!-- b000309 | references | pages [24] -->
aerodynamics. Sports

<!-- b000310 | references | pages [24] -->
Eng 20, 81–110

<!-- b000311 | references | pages [24] -->
(2017).

<!-- b000312 | references | pages [24] -->
https://doi.org/10.1007/s12283-017-0234-1

<!-- b000313 | references | pages [24] -->
[9]. Pierre Debraux, Frederic Grappe, Aneliya V. Manolova & William Ber-

<!-- b000314 | references | pages [24] -->
tucci (2011) Aerodynamic drag in cycling: methods of assessment, Sports Biome-

<!-- b000315 | references | pages [24] -->
chanics, 10:3, 197-218, DOI: 10.1080/14763141.2011.592209

<!-- b000316 | references | pages [24] -->
[10].

<!-- b000317 | references | pages [24] -->
Steyn, Wynand J. vdM, and Janike Warnich. "Comparison of tyre rolling re-

<!-- b000318 | references | pages [24] -->
sistance for different mountain bike tyre diameters and surface conditions." South Af-

<!-- b000319 | references | pages [24] -->
rican Journal for Research in Sport, Physical Education and Recreation 36.2 (2014):

<!-- b000320 | references | pages [24] -->
179-193.

<!-- b000321 | references | pages [24] -->
[11].

<!-- b000322 | references | pages [24] -->
https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-data-

<!-- b000323 | references | pages [24] -->
base.

<!-- b000324 | heading | pages [25] -->
Appendix

<!-- b000325 | heading | pages [25] -->
Appendix 1

<!-- b000326 | prose | pages [25] -->
Introduce: Women's analysis chart

<!-- b000327 | prose | pages [25] -->
1.UCI Women's track map 2.Women’s power output 3.Women’s speed

<!-- b000328 | heading | pages [25] -->
4.5.Women’s Remaining aerobic and anaerobic energy

<!-- b000329 | prose | pages [25] -->
UCI Women's track map Women’s power output of Olympics

<!-- b000330 | prose | pages [25] -->
Women’s power output of UCI Women’s power output of own design
