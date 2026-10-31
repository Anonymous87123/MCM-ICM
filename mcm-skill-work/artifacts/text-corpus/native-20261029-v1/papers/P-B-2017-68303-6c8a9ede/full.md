# P-B-2017-68303-6c8a9ede

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
68303

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

<!-- b000012 | prose | pages [1] -->
T4

<!-- b000013 | prose | pages [1] -->
F4

<!-- b000014 | title | pages [1] -->
B

<!-- b000015 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | title | pages [1] -->
Merge Better After Toll

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
With the rapid increment of the trafﬁc ﬂow, the problem of merging after the toll barriers has risen public concern. In our paper, we aim to construct a model to ﬁnd a better design of the area following the toll barrier.

<!-- b000020 | prose | pages [1] -->
First, we classify the area following the toll barrier which may already be imple- mented into eight kinds according to the different shapes, sizes, and merging patterns of the area based on the toll plazas in reality.

<!-- b000021 | prose | pages [1] -->
Second, we use VISSIM to do the simulation of the typical eight models of the area following the toll barrier. Through setting the necessary observation points, we obtain the data of throughput, length of queues and the average time of delay we need in the following evaluation model.

<!-- b000022 | prose | pages [1] -->
Third, we build a comprehensive evaluation model based on PCA to evaluate the eight typical models and the optimum model we build. Considering the selection of the index, we choose the number of merging points to indicate accident prevention of the area, the length of queues, the throughput and the average time of delay to indicate the trafﬁc capacity of the area, and the height of the trapezoid area to indicate the con- struction cost of the area. After data normalization, we get the best model which is in the shape of isosceles trapezoid with stipulated merging pattern and medium size of the area among the eight existing models.

<!-- b000023 | prose | pages [1] -->
Fourth, in order to obtain a better solution, we build two models to obtain the opti- mum solution. The ﬁrst one is a differential equation model aimed at acquire the opti- mum height of the trapezoid area and the optimum number of tollbooths. The second one is a linear programming model which can calculate the optimum merging pattern while maximizing the throughput of the area.

<!-- b000024 | prose | pages [1] -->
Last but not least, we analyze the performance of our model under various condi- tions, and modify our model to accommodate to those conditions. Also, we use Lingo to construct sensitivity analysis of the linear programming model.

<!-- b000025 | prose | pages [1] -->
To sum up, our model is a feasible and reasonable model which can accommodate to various situations.

<!-- b000026 | furniture | pages [2] -->
Team # 68303

<!-- b000027 | furniture | pages [2] -->
Page 1 of 20

<!-- b000028 | heading | pages [2] -->
Contents

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | heading | pages [2] -->
Introduction

<!-- b000031 | prose | pages [2] -->
2

<!-- b000032 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background 2

<!-- b000033 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2

<!-- b000034 | prose | pages [2] -->
Overview of Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 2

<!-- b000035 | prose | pages [2] -->
General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000036 | prose | pages [2] -->
2 Classify the Design

<!-- b000037 | prose | pages [2] -->
3

<!-- b000038 | heading | pages [2] -->
Simulation Model

<!-- b000039 | prose | pages [2] -->
4

<!-- b000040 | heading | pages [2] -->
Evaluation Model

<!-- b000041 | prose | pages [2] -->
3

<!-- b000042 | prose | pages [2] -->
3

<!-- b000043 | prose | pages [2] -->
4

<!-- b000044 | prose | pages [2] -->
7

<!-- b000045 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Index variables 7

<!-- b000046 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 PCA Model 8

<!-- b000047 | prose | pages [2] -->
Analysis and Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3

<!-- b000048 | prose | pages [2] -->
5

<!-- b000049 | heading | pages [2] -->
Find the Optimum Solution

<!-- b000050 | prose | pages [2] -->
8

<!-- b000051 | prose | pages [2] -->
9

<!-- b000052 | prose | pages [2] -->
Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 9

<!-- b000053 | prose | pages [2] -->
Differential Equation Model . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 9

<!-- b000054 | prose | pages [2] -->
Linear Programming Model . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 12

<!-- b000055 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 Result and Model Testing

<!-- b000056 | prose | pages [2] -->
6 Effects and Adjustment

<!-- b000057 | prose | pages [2] -->
13

<!-- b000058 | prose | pages [2] -->
14

<!-- b000059 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Light and Heavy Trafﬁc 14

<!-- b000060 | prose | pages [2] -->
Add Autonomous Vehicles . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 14

<!-- b000061 | prose | pages [2] -->
Compositions of Tollbooths . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000062 | prose | pages [2] -->
7

<!-- b000063 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000064 | prose | pages [2] -->
15

<!-- b000065 | prose | pages [2] -->
16

<!-- b000066 | prose | pages [2] -->
Reduced Cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 16

<!-- b000067 | prose | pages [2] -->
Change Range of Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000068 | prose | pages [2] -->
8

<!-- b000069 | heading | pages [2] -->
Conclusion

<!-- b000070 | prose | pages [2] -->
16

<!-- b000071 | prose | pages [2] -->
17

<!-- b000072 | prose | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 17

<!-- b000073 | prose | pages [2] -->
Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 18

<!-- b000074 | furniture | pages [3] -->
Team # 68303

<!-- b000075 | furniture | pages [3] -->
Page 2 of 20

<!-- b000076 | prose | pages [3] -->
1

<!-- b000077 | heading | pages [3] -->
Introduction

<!-- b000078 | prose | pages [3] -->
1.1

<!-- b000079 | heading | pages [3] -->
Background

<!-- b000080 | prose | pages [3] -->
The major problems facing motorists on today’s highways are congestion, accidents, and costs-too many automobiles traveling to the same place at the same time; too many automobiles, trucks, buses, bicycles, and pedestrians attempting to use the same space; too many motorists losing time unnecessarily; too many accidents occurring; and too many decisions being made on highway improvements without adequate analytical tools[1].

<!-- b000081 | prose | pages [3] -->
As an important part of the highway, the toll plaza is to blame for most of the con- gestions and accidents happen around it. Since there are usually more tollbooths than there are incoming lanes of trafﬁc, vehicles must "fan in" from larger number of tollbooth egress lanes to the smaller number of regular travel lanes. In other words, vehicles need to merge after toll.

<!-- b000082 | prose | pages [3] -->
Trafﬁc congestion normally happens when merging points are met[2], which may re- sult in long trafﬁc queues on the road. When designing merging area of the toll plaza, shape, size and merging pattern of the area should be taken into consideration. More- over, the design should reduce the risk of accident, the cost of road construction and increase the throughput as much as possible.

<!-- b000083 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000084 | prose | pages [3] -->
We are required not only to analyze the performance of the area following the toll bar- rier with different shapes, sizes, and merging patterns that may already be implemented on the aspect of accident prevention, throughput, and cost, but also to determine if there are better solutions than any in common use and evaluate the performance of them un- der different circumstances.

<!-- b000085 | prose | pages [3] -->
The problem can be analyzed into four parts:

<!-- b000086 | prose | pages [3] -->
• Analyze the existing design of the area following the toll barrier with different shapes, sizes and merging patterns.

<!-- b000087 | prose | pages [3] -->
• Build a simulation model to simulate the trafﬁc condition of different designs of the area following the toll barrier.

<!-- b000088 | prose | pages [3] -->
• Build an evaluation model to rate the performance of different designs of the area following the toll barrier.

<!-- b000089 | prose | pages [3] -->
• Find a solution which can perform better than any in common use.

<!-- b000090 | prose | pages [3] -->
1.3 Overview of Our Work

<!-- b000091 | prose | pages [3] -->
With the increment of trafﬁc ﬂow, the trafﬁc congestion happens more and more fre- quently on the highway, as it gradually becomes the main cause of trafﬁc accidents. The problem of merging after toll has become the common concern of the society.

<!-- b000092 | furniture | pages [4] -->
Team # 68303

<!-- b000093 | furniture | pages [4] -->
Page 3 of 20

<!-- b000094 | prose | pages [4] -->
Firstly, we classify the area following the toll plaza into 8 kinds according to the different shapes, sizes, and merging patterns of the area.

<!-- b000095 | prose | pages [4] -->
Secondly, we select a series of index to evaluate the existing design of the area fol- lowing the toll plaza. Through the comprehensive evaluation model based on PCA, we evaluate the existing design of the area and our own design.

<!-- b000096 | prose | pages [4] -->
Thirdly, we build a differential equation model to obtain the optimum number of toll- booths and the height of the trapezoid area and a linear programming model to acquire the optimum merging pattern of the area following the toll barrier.

<!-- b000097 | prose | pages [4] -->
Finally, we analyze the performance of our model under various conditions and the sensitivity of our model.

<!-- b000098 | prose | pages [4] -->
1.4

<!-- b000099 | heading | pages [4] -->
General Assumptions

<!-- b000100 | prose | pages [4] -->
• All the motorists would obey the trafﬁc rules. We don’t take accidents resulted from drink-driving or speeding into consideration.

<!-- b000101 | prose | pages [4] -->
• We set the average speed of the vehicles under normal circumstances. Ignore the impact of weather conditions.

<!-- b000102 | prose | pages [4] -->
• We assume the vehicles on the highway are all cars, for other kinds of vehicles accounts for a relatively small proportion.

<!-- b000103 | prose | pages [4] -->
• The queue at the merging point would not affect the service of the tollbooths.

<!-- b000104 | prose | pages [4] -->
• All the tollbooths on the toll plaza operate all day.

<!-- b000105 | prose | pages [4] -->
2 Classify the Design

<!-- b000106 | prose | pages [4] -->
Before constructing the simulation model, we need to classify the design of the area following the toll barrier according to the shape, the size, as well as the merging pattern.

<!-- b000107 | prose | pages [4] -->
According to the satellite map, we ﬁnd that most of the area following the toll bar- rier can be abstracted into two shapes which are right-angled trapezoid and isosceles trapezoid.

<!-- b000108 | prose | pages [4] -->
{

<!-- b000109 | prose | pages [4] -->
right-angled trapezoid,

<!-- b000110 | prose | pages [4] -->
shape

<!-- b000111 | prose | pages [4] -->
Sp1

<!-- b000112 | prose | pages [4] -->
isosceles trapezoid, Sp2

<!-- b000113 | prose | pages [4] -->
Then we ﬁnd that the height of the trapezoid determines the size of the area following the toll barrier when the number and width of the tollbooths and travel lanes are deﬁned. According to Japan highway design essentials[3], we choose S/H to indicate the size of the area. To simplify our model, we only take small size S/H = 1/3 and large size S/H = 1/6 into simulation.

<!-- b000114 | prose | pages [4] -->


<!-- b000115 | prose | pages [4] -->
H = 1 S

<!-- b000116 | prose | pages [4] -->
 

<!-- b000117 | prose | pages [4] -->
size

<!-- b000118 | prose | pages [4] -->
3, Sz1

<!-- b000119 | prose | pages [4] -->
H = 1 S

<!-- b000120 | prose | pages [4] -->
 

<!-- b000121 | prose | pages [4] -->
6, Sz2

<!-- b000122 | furniture | pages [5] -->
Team # 68303

<!-- b000123 | furniture | pages [5] -->
Page 4 of 20

<!-- b000124 | prose | pages [5] -->
According to our observation, vehicles can change into any lane when getting out of the toll barrier. On the basis of this observation, we assume that there may be a merging pattern which stipulates the vehicles on the left side can only drive down to the left lanes and the vehicles on the right can only drive down to the right lanes. The stipulation may reduce the risk of collision.

<!-- b000125 | prose | pages [5] -->
{

<!-- b000126 | prose | pages [5] -->
normal merging pattern, Mp1

<!-- b000127 | prose | pages [5] -->
merging pattern

<!-- b000128 | prose | pages [5] -->
stipulated merging pattern, Mp2

<!-- b000129 | caption | pages [5] -->
Figure 1: normal and stipulated merging pattern

<!-- b000130 | prose | pages [5] -->
3

<!-- b000131 | heading | pages [5] -->
Simulation Model

<!-- b000132 | prose | pages [5] -->
For the lack of data, we choose frequently used software VISSIM to simulate the trafﬁc condition following the toll barrier.

<!-- b000133 | prose | pages [5] -->
Before the simulation, we need to set a series of parameters. According to the exam- ple mentioned in the problem that the toll highway has L lanes of travel in each direction and a barrier toll contains B tollbooths in each direction, we set the number of lanes and tollbooths L = 3, B = 8 the same as the example.

<!-- b000134 | prose | pages [5] -->
After consulting Highway Capacity Manual 2000 [4], we set the width of each lane d = 3.5m, the combined width of tollbooth and lane D = 5.5m, and the average speed of vehicles on the highway v = 120km/h. For S = (D ∗B −d ∗L) ∗0.5, S = 16.75. When it comes to a small-sized area S/H = 1/3, H = 50.25. Similarly, when it comes to a large-sized area S/H = 1/6, H = 50.25.

<!-- b000135 | prose | pages [5] -->
Since we only have to determine the area following the toll barrier, we just need to set the number of vehicles leaving the toll barrier per hour instead of considering the number of vehicles on the travel lanes entering the barrier toll. Through information research[5], we ﬁnd that the temporary retention time at the toll booth is 12 seconds. We want to stimulate the process for 3600 seconds, so the number of vehicles leaving the toll barrier is approximately 3600/12 = 300 vehicles per hour per lane.

<!-- b000136 | prose | pages [5] -->
To simplify our model, we set the vehicle composition as 100% cars. Considering that there will be many merging points in the area following the barrier toll, we set con- ﬂict areas between each pair of possible crossed paths to simulate the process of vehicle collision avoidance.

<!-- b000137 | furniture | pages [6] -->
Team # 68303

<!-- b000138 | furniture | pages [6] -->
Page 5 of 20

<!-- b000139 | caption | pages [6] -->
Table 1: Parameters

<!-- b000140 | prose | pages [6] -->
Parameter

<!-- b000141 | prose | pages [6] -->
simulation time

<!-- b000142 | prose | pages [6] -->
number of travel lanes

<!-- b000143 | prose | pages [6] -->
number of toll booths

<!-- b000144 | prose | pages [6] -->
width of travel lanes

<!-- b000145 | prose | pages [6] -->
Symbol Value

<!-- b000146 | prose | pages [6] -->
T 3600s

<!-- b000147 | prose | pages [6] -->
L 3

<!-- b000148 | prose | pages [6] -->
B 8

<!-- b000149 | prose | pages [6] -->
d 3.5m

<!-- b000150 | prose | pages [6] -->
D combined width of tollbooth and lane

<!-- b000151 | prose | pages [6] -->
ingress trafﬁc ﬂow of the area

<!-- b000152 | prose | pages [6] -->
5.5m

<!-- b000153 | prose | pages [6] -->
In 2400 vehicles/h

<!-- b000154 | prose | pages [6] -->
V average speed of vehicles on the highway 120km/h

<!-- b000155 | caption | pages [6] -->
Figure 2: Set collision areas

<!-- b000156 | prose | pages [6] -->
Afterwards, we set travel time sections, data collection point, and queue counters of the area to monitor the values of delay, number of passing vehicles and queue length.

<!-- b000157 | prose | pages [6] -->
Then, we simulate eight kinds of area following the toll barrier according to our above classiﬁcation, to obtain the data we need in the evaluation model.

<!-- b000158 | caption | pages [6] -->
Figure 3: Kind 1: Sp1,Sz1,Mp1

<!-- b000159 | caption | pages [6] -->
Figure 4: Kind 2: Sp1,Sz2,Mp1

<!-- b000160 | prose | pages [6] -->
After simulation, we collect data from the program of the eight models.

<!-- b000161 | furniture | pages [7] -->
Team # 68303

<!-- b000162 | furniture | pages [7] -->
Page 6 of 20

<!-- b000163 | caption | pages [7] -->
Figure 5: Kind 3: Sp1,Sz1,Mp2

<!-- b000164 | caption | pages [7] -->
Figure 6: Kind 4: Sp1,Sz2,Mp2

<!-- b000165 | caption | pages [7] -->
Figure 7: Kind 5: Sp2,Sz1,Mp1

<!-- b000166 | caption | pages [7] -->
Figure 8: Kind 6: Sp2,Sz2,Mp1

<!-- b000167 | caption | pages [7] -->
Figure 9: Kind 7: Sp2,Sz1,Mp2

<!-- b000168 | caption | pages [7] -->
Figure 10: Kind 8: Sp2,Sz2,Mp2

<!-- b000169 | furniture | pages [8] -->
Team # 68303

<!-- b000170 | furniture | pages [8] -->
Page 7 of 20

<!-- b000171 | caption | pages [8] -->
Table 2: simulation data of 8 kinds of models

<!-- b000172 | prose | pages [8] -->
height of

<!-- b000173 | prose | pages [8] -->
throughput

<!-- b000174 | prose | pages [8] -->
average length

<!-- b000175 | prose | pages [8] -->
number of

<!-- b000176 | prose | pages [8] -->
delay(s)

<!-- b000177 | prose | pages [8] -->
kind trapezoid (m)

<!-- b000178 | prose | pages [8] -->
(veh/h)

<!-- b000179 | prose | pages [8] -->
1 50.5 2149

<!-- b000180 | prose | pages [8] -->
2 105 2193

<!-- b000181 | prose | pages [8] -->
3 50.5 2271

<!-- b000182 | prose | pages [8] -->
4 105 2191

<!-- b000183 | prose | pages [8] -->
5 50.5 2178

<!-- b000184 | prose | pages [8] -->
6 105 2168

<!-- b000185 | prose | pages [8] -->
7 50.5 2301

<!-- b000186 | prose | pages [8] -->
8 105 2228

<!-- b000187 | prose | pages [8] -->
4

<!-- b000188 | heading | pages [8] -->
Evaluation Model

<!-- b000189 | prose | pages [8] -->
of queue(m)

<!-- b000190 | prose | pages [8] -->
merging points

<!-- b000191 | prose | pages [8] -->
13.8 21.38 24

<!-- b000192 | prose | pages [8] -->
20.5 25.49 24

<!-- b000193 | prose | pages [8] -->
8.2 10.02 7

<!-- b000194 | prose | pages [8] -->
14.1 17.65 7

<!-- b000195 | prose | pages [8] -->
10.4 18.77 24

<!-- b000196 | prose | pages [8] -->
17.3 20.04 24

<!-- b000197 | prose | pages [8] -->
5.8 8.13 7

<!-- b000198 | prose | pages [8] -->
11.92 13.26 7

<!-- b000199 | prose | pages [8] -->
To illustrate the independence, and the relationship between different variables, we use Principal Component Analysis (PCA)[6]. When some of the variables can explain a great percentage of the results, we can say these variables are strongly correlated and we can use the great one to represent others. After that, we can build a comprehensive evaluation model which based on PCA to evaluate our area models.

<!-- b000200 | prose | pages [8] -->
4.1 Index variables

<!-- b000201 | prose | pages [8] -->
We are required to consider the accident prevention, throughput and cost of our mod- els. Since some of the aspects cannot be valued directly, we have to ﬁnd some other parameters to indicate them.

<!-- b000202 | prose | pages [8] -->
Firstly, as most of the trafﬁc accidents happen at the merging point of lanes, we set the number of merging point of the area as the index to indicate accident prevention level.

<!-- b000203 | prose | pages [8] -->
Secondly, the cost of land and road construction is proportional to the area size. Since the sum of the bottoms of the trapezoid area are the same, we use the height of the trapezoid area to indicate the construction cost.

<!-- b000204 | prose | pages [8] -->
Thirdly, there are several indicators of the trafﬁc performance in the area following the toll barrier. We choose the average delay time, the length of queue at merging points and the throughput (number of vehicles per hour passing the point where the end of the plaza joins the eight outgoing trafﬁc lanes) to indicate[7].

<!-- b000205 | furniture | pages [9] -->
Team # 68303

<!-- b000206 | prose | pages [9] -->
4.2

<!-- b000207 | heading | pages [9] -->
PCA Model

<!-- b000208 | furniture | pages [9] -->
Page 8 of 20

<!-- b000209 | prose | pages [9] -->
The model is better, if the values of delay time, the length of queue at merging points and the number of merging points are smaller. Since PCA determines the ranking of the models based on the comprehensive score, we take the reciprocal of these values.

<!-- b000210 | prose | pages [9] -->
In order to facilitate the further analysis, we do the data normalization. Map the index variable data setx = x1, x2, . . . , x5. Set aij as the value of index variable j of model i.

<!-- b000211 | prose | pages [9] -->
˜aij = aij −µj

<!-- b000212 | prose | pages [9] -->
i = 1, . . . , 8, ,

<!-- b000213 | prose | pages [9] -->
sj

<!-- b000214 | prose | pages [9] -->
˜xj = xj −µj

<!-- b000215 | prose | pages [9] -->
sj

<!-- b000216 | prose | pages [9] -->
√

<!-- b000217 | prose | pages [9] -->
∑n

<!-- b000218 | prose | pages [9] -->
∑n

<!-- b000219 | prose | pages [9] -->
Where: µj = 1

<!-- b000220 | prose | pages [9] -->
1

<!-- b000221 | prose | pages [9] -->
j = 1, . . . , 5 (1)

<!-- b000222 | prose | pages [9] -->
, , j = 1, . . . , 5 (2)

<!-- b000223 | prose | pages [9] -->
i=1(aij −µi)2.

<!-- b000224 | prose | pages [9] -->
i=1 aij, sj =

<!-- b000225 | prose | pages [9] -->
n−1

<!-- b000226 | prose | pages [9] -->
n

<!-- b000227 | prose | pages [9] -->
Then we calculate the correlation coefﬁcient matrix R = (rij)5∗5:

<!-- b000228 | prose | pages [9] -->
∑n

<!-- b000229 | prose | pages [9] -->
k=1 ˜aki ∗˜akj

<!-- b000230 | prose | pages [9] -->
rij =

<!-- b000231 | prose | pages [9] -->
n −1 , , i, j = 1, . . . , 5 (3)

<!-- b000232 | prose | pages [9] -->
Afterwards, we calculate the eigenvalues λj and the corresponding eigenvectors of R, to form the ﬁve new index variables. On the basis of the eigenvalues, we can get the contribution rate b and the accumulative contributions rate α of the parameters.

<!-- b000233 | prose | pages [9] -->
λj ∑m bj =

<!-- b000234 | prose | pages [9] -->
k=1 λk

<!-- b000235 | prose | pages [9] -->
αp =

<!-- b000236 | prose | pages [9] -->
, , j = 1, . . . , 5 (4)

<!-- b000237 | prose | pages [9] -->
∑p

<!-- b000238 | prose | pages [9] -->
k=1 λk ∑5

<!-- b000239 | prose | pages [9] -->
(5)

<!-- b000240 | prose | pages [9] -->
k=1 λk

<!-- b000241 | prose | pages [9] -->
Since b=[72.8902,21.8503,3.8901,1.0350,0.3341] and α=[72.8902,94.7408,98.6309,99.6659,100], we select the ﬁrst three components as the three principle components y1, y2, y3 to replace the used ﬁve index variables.

<!-- b000242 | prose | pages [9] -->
According to the principle components, the ﬁrst component contributes most to the throughput, the second component contributes most to the cost, and the third compo- nent contributes most to the accidents prevention.

<!-- b000243 | prose | pages [9] -->
4.3

<!-- b000244 | heading | pages [9] -->
Analysis and Result

<!-- b000245 | prose | pages [9] -->
Multiplying the contribution rate with the value of corresponding principle compo- nents, we can obtain the comprehensive scores of our eight models.

<!-- b000246 | prose | pages [9] -->
Z =

<!-- b000247 | prose | pages [9] -->
p p ∑

<!-- b000248 | prose | pages [9] -->
bjyj (6)

<!-- b000249 | prose | pages [9] -->
j=1

<!-- b000250 | prose | pages [9] -->
The ﬁnal score of the eight models are shown in Table 3.

<!-- b000251 | prose | pages [9] -->
From the result above, we ﬁnd that right-angled trapezoid is better than isosceles trapezoid and the stipulated merging pattern is better than normal merging pattern.

<!-- b000252 | furniture | pages [10] -->
Team # 68303

<!-- b000253 | furniture | pages [10] -->
Page 9 of 20

<!-- b000254 | caption | pages [10] -->
Table 3: Evaluation Result of Models

<!-- b000255 | prose | pages [10] -->
Rank Model Score

<!-- b000256 | prose | pages [10] -->
1 7 2.5822

<!-- b000257 | prose | pages [10] -->
2 3 1.6134

<!-- b000258 | prose | pages [10] -->
3 8 -0.0457

<!-- b000259 | prose | pages [10] -->
4 5 -0.1332

<!-- b000260 | prose | pages [10] -->
Rank Model Score

<!-- b000261 | prose | pages [10] -->
5 4 -0.6187

<!-- b000262 | prose | pages [10] -->
6 1 -0.6190

<!-- b000263 | prose | pages [10] -->
7 6 -1.3492

<!-- b000264 | prose | pages [10] -->
8 2 -1.4298

<!-- b000265 | prose | pages [10] -->
When it comes to the size of the area, we assume that the longer the height of the trapezoid area is, the larger the size of the area is which may increase the throughput of the area. According to the scores listed above, the result is contrary to our assump- tion. Then we simulate a new circumstance whose height is half of the 5th kind of model and evaluate it through the method above. The evaluation score of this model is -0.6726, while the evaluation score of the 5th kind of model is -0.1332. Thus, we can come to a conclusion that it may exist an optimum height of the trapezoid area to make the throughput of the area come to its maximum. Meanwhile, we also should take the increment of the cost resulted from the increment of the height of the trapezoid area into consideration.

<!-- b000266 | prose | pages [10] -->
5

<!-- b000267 | heading | pages [10] -->
Find the Optimum Solution

<!-- b000268 | prose | pages [10] -->
5.1 Overview

<!-- b000269 | prose | pages [10] -->
From our evaluation model, we can see that the height of the trapezoid area and the merging pattern have a great impact on the throughput of the area following the toll bar- rier. When determining if there exists a better solution, we should include quantitative or qualitative estimates of these two parameters. Also, the number of tollbooths may inﬂuence the number of the vehicles passing through the toll barrier, while this outﬂow of the toll barrier may affect the trafﬁc pressure of the area following the toll barrier. So we should also take the number of tollbooths into consideration.

<!-- b000270 | prose | pages [10] -->
When it comes to the cost of the area which is determined by the size of the area, there are two parameters to indicate: the height of the trapezoid area and the number of toll booths which determine the length of one bottom of the trapezoid area and may add to the operating cost of the toll plaza.

<!-- b000271 | prose | pages [10] -->
Then we can build two models to ﬁnd the optimum solution. The ﬁrst one is a dif- ferential equation model aimed at minimizing the cost of the road construction and the operating cost of toll booths. The second one is a linear programming model calculating the optimum strategy of merging pattern.

<!-- b000272 | prose | pages [10] -->
5.2

<!-- b000273 | heading | pages [10] -->
Differential Equation Model

<!-- b000274 | prose | pages [10] -->
(1) Terms and Deﬁnitions

<!-- b000275 | furniture | pages [11] -->
Team # 68303

<!-- b000276 | furniture | pages [11] -->
Page 10 of 20

<!-- b000277 | caption | pages [11] -->
Table 4: Symbols

<!-- b000278 | prose | pages [11] -->
Symbol Meaning

<!-- b000279 | prose | pages [11] -->
C total cost

<!-- b000280 | prose | pages [11] -->
W average waiting time per vehicle in the toll plaza

<!-- b000281 | prose | pages [11] -->
W1 time spent in lines

<!-- b000282 | prose | pages [11] -->
W2 service time

<!-- b000283 | prose | pages [11] -->
W3 time spent passing through the area following the toll barrier

<!-- b000284 | prose | pages [11] -->
v average time value of a person in one vehicle

<!-- b000285 | prose | pages [11] -->
µ average number of person in one vehicle

<!-- b000286 | prose | pages [11] -->
n the number of vehicles passing through the toll plaza

<!-- b000287 | prose | pages [11] -->
C1 the operation cost of a tollbooth per day

<!-- b000288 | prose | pages [11] -->
C2 the construction cost of unit area

<!-- b000289 | prose | pages [11] -->
F(t) value of inﬂux at t minute

<!-- b000290 | prose | pages [11] -->
O(t, B) value of outﬂux at t minute with B tollbooths

<!-- b000291 | prose | pages [11] -->
s the average number of vehicles which one tollbooth can serve per minute

<!-- b000292 | prose | pages [11] -->
k outﬂux barrier

<!-- b000293 | prose | pages [11] -->
• Inﬂux is the number of vehicles entering the toll plaza per minute.(veh/min)

<!-- b000294 | prose | pages [11] -->
• Outﬂux is the number of vehicles existing the toll plaza per minute.(veh/min)

<!-- b000295 | prose | pages [11] -->
• Total cost is the sum of the value of time wasted in the toll plaza, the operating cost of toll booths and the construction cost of the area.

<!-- b000296 | heading | pages [11] -->
(2) Data processing

<!-- b000297 | prose | pages [11] -->
From a previous research paper’s trafﬁc ﬂow data, we ﬁnd the value of inﬂux for a toll plaza on a given typical day. Since we need an inﬂux rate at every minute of the day, instead of just once an hour, we select a Fourier Series approximation with 8 terms to ﬁnd a close ﬁt[8]. The ﬁtting function of the inﬂux at t minute is described below where

<!-- b000298 | prose | pages [11] -->
24 = 0.2513. The approximation ﬁts the data point with an R2 value of 0.9997 which

<!-- b000299 | prose | pages [11] -->
ω = 2π

<!-- b000300 | prose | pages [11] -->
is close to 1. It represents the result is in good agreement with the research data.

<!-- b000301 | prose | pages [11] -->
F(t) = 41.68 −16.38 cos(tω) −18.59 cos(2tω) + 3.572 cos(3tω) + 7.876 cos(4tω) . . .

<!-- b000302 | prose | pages [11] -->
−0.5048 cos(tω) −2.970 cos(6tω) + 0.2518 cos(7tω) + 0.5785 cos(8tω) . . .

<!-- b000303 | prose | pages [11] -->
+ 12.53 sin(tω) + 0.6370 sin(2tω) −13.67 sin(3tω) + 0.4378 sin(4tω) . . .

<!-- b000304 | prose | pages [11] -->
+ 6.930 sin(5tω) + 0.4869 sin(6tω) −1.554 sin(7tω) −0.5871 sin(8tω)

<!-- b000305 | prose | pages [11] -->
(7)

<!-- b000306 | prose | pages [11] -->
(3) Establishment

<!-- b000307 | furniture | pages [12] -->
Team # 68303

<!-- b000308 | furniture | pages [12] -->
Page 11 of 20

<!-- b000309 | prose | pages [12] -->
We formulate a function C(B, H) to ﬁnd the number of tollbooths B and the height of the trapezoid area H that minimize the total cost C.

<!-- b000310 | prose | pages [12] -->
C(B, H) = (W1 + W2 + W3)vµn + C1B + C2H(BD −Ld)

<!-- b000311 | prose | pages [12] -->
(8) 2

<!-- b000312 | prose | pages [12] -->
Firstly, we need to calculate the un-known parameters in the function.

<!-- b000313 | prose | pages [12] -->
• F(t) is calculated from the above data processing.

<!-- b000314 | prose | pages [12] -->
• For the randomness of O(t, B), we use the average value of outﬂux per minute in simulation as O(t, B).

<!-- b000315 | prose | pages [12] -->
• k(veh/min) is relevant to L and H, while irrelevant to B. If the value of outﬂux exceeds k, trafﬁc congestion may happen.

<!-- b000316 | prose | pages [12] -->
∫24 • We can integrate F(t) over time to calculate n =

<!-- b000317 | prose | pages [12] -->
0 3600F(t) dt.

<!-- b000318 | prose | pages [12] -->
• For W1 represents the average amount of time each time spent waiting in lines before reaching the tollbooth, we need to integrate over time to calculate how many cars were forced to wait in line. So, the value of W1(t) can be depicted as:

<!-- b000319 | prose | pages [12] -->
{∫24

<!-- b000320 | prose | pages [12] -->
∫t

<!-- b000321 | prose | pages [12] -->
0 3600(F(τ)−Bs) dt dτ

<!-- b000322 | prose | pages [12] -->
0

<!-- b000323 | prose | pages [12] -->
W1 =

<!-- b000324 | prose | pages [12] -->
0, , F(τ) > Bs n n

<!-- b000325 | prose | pages [12] -->
(9)

<!-- b000326 | prose | pages [12] -->
F(τ) ≤Bs

<!-- b000327 | prose | pages [12] -->
• The way to calculate W3 is similar to the way we used to ﬁnd W1.

<!-- b000328 | prose | pages [12] -->
{∫24

<!-- b000329 | prose | pages [12] -->
∫t

<!-- b000330 | prose | pages [12] -->
0 3600(O(τ,B)−k) dt dτ

<!-- b000331 | prose | pages [12] -->
0

<!-- b000332 | prose | pages [12] -->
W3 =

<!-- b000333 | prose | pages [12] -->
0, , O(τ, B) > k n n

<!-- b000334 | prose | pages [12] -->
(10)

<!-- b000335 | prose | pages [12] -->
O(τ, B) ≤k

<!-- b000336 | prose | pages [12] -->
• Apparently, W2 is the reciprocal of s. So, W2 = 1

<!-- b000337 | prose | pages [12] -->
(4) Calculation

<!-- b000338 | prose | pages [12] -->
s.

<!-- b000339 | prose | pages [12] -->
When solving the integral equation above, we set a variance range for B and calculate the corresponding W1 and W3 for each B respectively. A Mathematica quartic polynom- inal ﬁt is then done on the resulting points. Through this ﬁtting procedure, we can get the function W1(B) and W3(B).

<!-- b000340 | prose | pages [12] -->
To minimize the value of C(B, H), we take the partial derivative of C(B, H).

<!-- b000341 | prose | pages [12] -->
∂C(B, H)

<!-- b000342 | prose | pages [12] -->
= vµn(∂W1(B) ∂B

<!-- b000343 | prose | pages [12] -->
∂B + ∂W3(B, H)

<!-- b000344 | prose | pages [12] -->
) + C1 + C2HD

<!-- b000345 | prose | pages [12] -->
(11)

<!-- b000346 | prose | pages [12] -->
∂B

<!-- b000347 | prose | pages [12] -->
2

<!-- b000348 | prose | pages [12] -->
+ C2(BD −Ld)

<!-- b000349 | prose | pages [12] -->
= vµn∂W3(B, H)

<!-- b000350 | prose | pages [12] -->
∂C(B, H)

<!-- b000351 | prose | pages [12] -->
∂H

<!-- b000352 | prose | pages [12] -->
(12)

<!-- b000353 | prose | pages [12] -->
∂H

<!-- b000354 | prose | pages [12] -->
2

<!-- b000355 | prose | pages [12] -->
Set these two formulas equal to 0. Then, we can compute the stationary points and the Hessian matrix. If the matrix is a positive deﬁnite matrix, the stationary point is the optimum B and H. When it comes to the example the title cite in which the number of travel lanes L = 3, the optimum number of toll booths B = 6, and the optimum height of the trapezoid area H = 35.6472m.

<!-- b000356 | furniture | pages [13] -->
Team # 68303

<!-- b000357 | prose | pages [13] -->
5.3

<!-- b000358 | heading | pages [13] -->
Linear Programming Model

<!-- b000359 | furniture | pages [13] -->
Page 12 of 20

<!-- b000360 | prose | pages [13] -->
We develop a vehicle transition matrix TB∗L in which tij represents the probability of vehicles which exit from tollbooth i drive down to lane j. We can abstract a merging pattern from matrix T by selecting the largest element i of column j in the matrix which means vehicles exiting from tollbooth i will merge into travel lane j.

<!-- b000361 | prose | pages [13] -->
Since we assume that the service ability of each toll booth is the same, we set the out- ﬂux probability vector of the toll barrier as P = [ 1

<!-- b000362 | prose | pages [13] -->
B, 1

<!-- b000363 | prose | pages [13] -->
B, . . . , 1

<!-- b000364 | prose | pages [13] -->
B]B. To increase the through- put of the area following the toll barrier, we assume the number of fan in to each of the travel lane is allocated averagely. Then, we set the inﬂux probability of the travel lane following the toll barrier as Q = [ 1

<!-- b000365 | prose | pages [13] -->
L, L

<!-- b000366 | prose | pages [13] -->
L, . . . , 1

<!-- b000367 | prose | pages [13] -->
L]L.

<!-- b000368 | prose | pages [13] -->
In order to allocate the vehicles to each travel lane following the toll barrier averagely, we get:

<!-- b000369 | prose | pages [13] -->
P ∗T = Q (13)

<!-- b000370 | prose | pages [13] -->
The total probability for vehicles driving down to each of the travel lane is 1.

<!-- b000371 | prose | pages [13] -->
L ∑

<!-- b000372 | prose | pages [13] -->
j=1

<!-- b000373 | prose | pages [13] -->
Tij = 1 (14)

<!-- b000374 | prose | pages [13] -->
The objective is to maximize the throughput with the speciﬁed value of L, B, H. In other words, we need to minimize the desired length of the vehicles travel path between the toll barrier and the travel lane.

<!-- b000375 | prose | pages [13] -->
We build a simple model shown as ﬁgure 11 to calculate the length z of every travel path.

<!-- b000376 | prose | pages [13] -->
√

<!-- b000377 | prose | pages [13] -->
H2 + [(j −1)d + (i −1)SD]2

<!-- b000378 | prose | pages [13] -->
z =

<!-- b000379 | prose | pages [13] -->
(15)

<!-- b000380 | caption | pages [13] -->
Figure 11: Simple model for calculation

<!-- b000381 | furniture | pages [14] -->
Team # 68303

<!-- b000382 | furniture | pages [14] -->
Page 13 of 20

<!-- b000383 | prose | pages [14] -->
Then, we can get the objective function as following:

<!-- b000384 | prose | pages [14] -->
∑

<!-- b000385 | prose | pages [14] -->
min g =

<!-- b000386 | prose | pages [14] -->
i=1

<!-- b000387 | prose | pages [14] -->
B B

<!-- b000388 | prose | pages [14] -->
L ∑

<!-- b000389 | prose | pages [14] -->
Tij ∗z (16)

<!-- b000390 | prose | pages [14] -->
j=1

<!-- b000391 | prose | pages [14] -->
From the conditions and object functions listed above, we have constructed a linear programming model.

<!-- b000392 | prose | pages [14] -->
B

<!-- b000393 | prose | pages [14] -->
L

<!-- b000394 | prose | pages [14] -->
∑

<!-- b000395 | prose | pages [14] -->
∑

<!-- b000396 | prose | pages [14] -->
min g = object function:

<!-- b000397 | prose | pages [14] -->
i=1

<!-- b000398 | prose | pages [14] -->
j=1

<!-- b000399 | prose | pages [14] -->


<!-- b000400 | prose | pages [14] -->
√

<!-- b000401 | prose | pages [14] -->
H2 + [(j −1)d + (i −1)SD]2

<!-- b000402 | prose | pages [14] -->
Tij ∗

<!-- b000403 | prose | pages [14] -->
P ∗T = Q

<!-- b000404 | prose | pages [14] -->
  

<!-- b000405 | prose | pages [14] -->
L ∑

<!-- b000406 | prose | pages [14] -->
s.t.

<!-- b000407 | prose | pages [14] -->
  

<!-- b000408 | prose | pages [14] -->
j=1

<!-- b000409 | prose | pages [14] -->
Tij = 1

<!-- b000410 | prose | pages [14] -->
For example, when we set B = 6, L = 3, the optimum vehicle transition matrix T is as following.

<!-- b000411 | prose | pages [14] -->


<!-- b000412 | prose | pages [14] -->


<!-- b000413 | prose | pages [14] -->
T =

<!-- b000414 | prose | pages [14] -->


<!-- b000415 | prose | pages [14] -->
1 1 0 0

<!-- b000416 | prose | pages [14] -->


<!-- b000417 | prose | pages [14] -->
1 1 0 0

<!-- b000418 | prose | pages [14] -->
0 0 1 0

<!-- b000419 | prose | pages [14] -->
0 0 1 0

<!-- b000420 | prose | pages [14] -->
0 0 0 1

<!-- b000421 | prose | pages [14] -->
0 0 0 1

<!-- b000422 | prose | pages [14] -->
From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 and 2 should merge into lane 1. Vehicles leaving from tollbooth 3 and 4 should merge into lane 2. Vehicles leaving from tollbooth 5 and 6 should merge into lane 3.

<!-- b000423 | prose | pages [14] -->
5.4

<!-- b000424 | heading | pages [14] -->
Result and Model Testing

<!-- b000425 | prose | pages [14] -->
From the result above, we ﬁnd the optimum solution of three lanes is in the shape of isosceles trapezoid with six tollbooths and stipulated merging pattern and the height of the area following the toll barrier is 35.6472m .

<!-- b000426 | prose | pages [14] -->
In order to test if the solution is better than the above eight existing models, we put the corresponding data into our simulation model and evaluation model.

<!-- b000427 | prose | pages [14] -->
The ﬁnal score of our model is 4.3026 which is higher than the existing eight models we discussed above.

<!-- b000428 | furniture | pages [15] -->
Team # 68303

<!-- b000429 | furniture | pages [15] -->
Page 14 of 20

<!-- b000430 | caption | pages [15] -->
Figure 12: Testing Simulation

<!-- b000431 | prose | pages [15] -->
6 Effects and Adjustment

<!-- b000432 | prose | pages [15] -->
6.1 Light and Heavy Trafﬁc

<!-- b000433 | prose | pages [15] -->
Under the condition of light trafﬁc, the inﬂux and outﬂux value of the tollbooths will decline. For the drop of the number of vehicles, the possibility of trafﬁc congestion will decrease. Thus when it comes to light trafﬁc, the throughput of the area will not show up while the principle problem is that the number of toll booths may exceed the demand which may waste the operation cost of the area. We can calculate the optimum number of tollbooths by modifying the inﬂux parameter of our differential equation model. Then some of the redundant tollbooths can be shut down appropriately to ensure that we can reduce the operation cost to the greatest extend without reducing the throughput of the area.

<!-- b000434 | prose | pages [15] -->
When it comes to heavy trafﬁc, the possibility of trafﬁc congestion will increase for the rise of inﬂux value of the tollbooths. Our model which adopts an optimum merging strategy, number of tollbooths and the size of the area following the toll barriers can work well under the pressure of heavy trafﬁc. However, when the number of vehicles reach a certain level, we can adjust the merging strategy to promote the capacity of the area following the toll barrier. For example, if we ﬁnd the nearest lane a of the toll barrier i, then we can set a proper number of b based on the reality and value of L to make tij = 0, j /∈[a −b, a + b].

<!-- b000435 | prose | pages [15] -->
On the one hand, the adjustment can reduce the delay time of vehicles passing through the area following the toll barrier. On the other hand, it can reduce the possibility of accident which caused from heavy trafﬁc while it may increase the length of queue at merging points which should be studied by our further research.

<!-- b000436 | prose | pages [15] -->
6.2 Add Autonomous Vehicles

<!-- b000437 | prose | pages [15] -->
After our research, we ﬁnd that the autonomous vehicles have the following advantages[9]:

<!-- b000438 | prose | pages [15] -->
• Safety: The vehicle is controlled by computer. So it can adjust its driving route on

<!-- b000439 | furniture | pages [16] -->
Team # 68303

<!-- b000440 | furniture | pages [16] -->
Page 15 of 20

<!-- b000441 | prose | pages [16] -->
time and choose the safer path when entering the area following the toll barrier. As a result, self-driving can reduce the risk of trafﬁc accidents caused by limitations of human beings.

<!-- b000442 | prose | pages [16] -->
• Efﬁciency: Compared to normal vehicles, autonomous vehicles can adjust the gap between vehicles and the speed of vehicles intelligently which can lead to lower possibility of trafﬁc congestion.

<!-- b000443 | prose | pages [16] -->
Due to the safety and the efﬁciency of autonomous vehicles, we do not have to stip- ulate the merge pattern of the area following the toll barrier which can bring the advan- tages of autonomous vehicles to the full play.

<!-- b000444 | prose | pages [16] -->
6.3 Compositions of Tollbooths

<!-- b000445 | prose | pages [16] -->
Different compositions of tollbooths may affect the outﬂux value of the toll barrier, which is represented by outﬂux probability vector of the toll barrier P in the linear pro- gramming model.

<!-- b000446 | prose | pages [16] -->
There are three kinds of tollbooths listed in the problem. We set the average service rate of tollbooths i in type k as rik in which type 1 is conventional tollbooth, type 2 is exact-change tollbooth, and type 3 is electronic toll collection booth. From our research[9], ri1 = 5, ri2 = 7, and ri3 = 20 .The total service rate is r = ∑B

<!-- b000447 | prose | pages [16] -->
i=1 rik, k = 1, 2, 3. The outﬂux probability vector of the toll barrier P should be modiﬁed as P ′ = n

<!-- b000448 | prose | pages [16] -->
1, 2, 3.

<!-- b000449 | prose | pages [16] -->
r [rik, . . . , rBk], k =

<!-- b000450 | prose | pages [16] -->
Under the optimum condition we calculated in the previous models in which L = 3, B = 6, H = 35.6472, D = 5.5, d = 3.5, we assume one kind of proportion of tollbooths in which NO.1 and NO.2 tollbooths are electronic toll collection booths, No.3 and No.4 tollbooths are conventional toll booths, and No.5 and No.6 tollbooths are exact-change tollbooths. Then we input the data into our linear programming model. The optimum result vehicle transition matrix T1 is as following:

<!-- b000451 | prose | pages [16] -->


<!-- b000452 | prose | pages [16] -->
1

<!-- b000453 | prose | pages [16] -->


<!-- b000454 | prose | pages [16] -->
0

<!-- b000455 | prose | pages [16] -->
0.2667

<!-- b000456 | prose | pages [16] -->
T1 =

<!-- b000457 | prose | pages [16] -->
0

<!-- b000458 | prose | pages [16] -->
0

<!-- b000459 | prose | pages [16] -->
0

<!-- b000460 | prose | pages [16] -->


<!-- b000461 | prose | pages [16] -->
0 0

<!-- b000462 | prose | pages [16] -->


<!-- b000463 | prose | pages [16] -->
0.8833 0.1167

<!-- b000464 | prose | pages [16] -->
0.7333 0

<!-- b000465 | prose | pages [16] -->
0 1

<!-- b000466 | prose | pages [16] -->
0 1

<!-- b000467 | prose | pages [16] -->
0 1

<!-- b000468 | prose | pages [16] -->
From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 enter into lane 1. Vehicles leaving from tollbooth 2 and 3 should merge into lane 2. Vehicles leaving from tollbooth 4, 5 and 6 should merge into lane 3.

<!-- b000469 | prose | pages [16] -->
Then, we assume another one kind of proportion of tollbooths in which NO.1, NO.2, NO.3 tollbooths are electronic toll collection booths, No.4 tollbooth is conventional toll booths, and No.5 and No.6 tollbooths are exact-change tollbooths. Then we input the

<!-- b000470 | furniture | pages [17] -->
Team # 68303

<!-- b000471 | furniture | pages [17] -->
Page 16 of 20

<!-- b000472 | prose | pages [17] -->
data into our linear programming model. The optimum result vehicle transition matrix T2 is as following:

<!-- b000473 | prose | pages [17] -->


<!-- b000474 | prose | pages [17] -->
1

<!-- b000475 | prose | pages [17] -->


<!-- b000476 | prose | pages [17] -->
0.3167

<!-- b000477 | prose | pages [17] -->
0

<!-- b000478 | prose | pages [17] -->
T2 =

<!-- b000479 | prose | pages [17] -->
0

<!-- b000480 | prose | pages [17] -->
0

<!-- b000481 | prose | pages [17] -->
0

<!-- b000482 | prose | pages [17] -->


<!-- b000483 | prose | pages [17] -->
0 0

<!-- b000484 | prose | pages [17] -->


<!-- b000485 | prose | pages [17] -->
0.6833 0

<!-- b000486 | prose | pages [17] -->
0.6363 0.3667

<!-- b000487 | prose | pages [17] -->
0 1

<!-- b000488 | prose | pages [17] -->
0 1

<!-- b000489 | prose | pages [17] -->
0 1

<!-- b000490 | prose | pages [17] -->
From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 enter into lane 1. Vehicles leaving from tollbooth 2 and 3 should merge into lane 2. Vehicles leaving from tollbooth 4, 5 and 6 should merge into lane 3.

<!-- b000491 | prose | pages [17] -->
In the way we illustrated in two examples above, Our model can adjust to different proportions of the three common kinds of tollbooths.

<!-- b000492 | prose | pages [17] -->
Then, we take extreme cases into consideration. If the proportion of electronic toll collection booths is too high, the number of vehicles exiting the toll barrier will increase signiﬁcantly. It is similar to the condition of heavy trafﬁc, we can solve it in the same way as the heavy trafﬁc condition.

<!-- b000493 | prose | pages [17] -->
7

<!-- b000494 | heading | pages [17] -->
Sensitivity Analysis

<!-- b000495 | prose | pages [17] -->
We do two kinds of sensitivity analysis on our linear programming model.

<!-- b000496 | prose | pages [17] -->
7.1 Reduced Cost

<!-- b000497 | prose | pages [17] -->
Reduced cost is the increment of objective function, when one of the variables increased by one unit. We use LINGO to calculate the reduced cost of every variables. The result is shown in ﬁgure 13.

<!-- b000498 | prose | pages [17] -->
The result indicates that when variable t13 and t61 increase by one unit, it will produce a larger deviation on the objective function. In other words, the desired number of the vehicles selecting the longest path to get into the travel lane increases signiﬁcantly, while the throughput of the area will decline at the same time. These kinds of selection may lead to the increment of merging points which is bad for accident prevention. Therefore, we should avoid this kind of situation.

<!-- b000499 | prose | pages [17] -->
7.2 Change Range of Variables

<!-- b000500 | prose | pages [17] -->
We use LINGO to calculate the change range of variables with the same optimum solution. The result is shown in ﬁgure 14.

<!-- b000501 | prose | pages [17] -->
The result indicates the reasonable error range of the construction in reality.

<!-- b000502 | furniture | pages [18] -->
Team # 68303

<!-- b000503 | furniture | pages [18] -->
Page 17 of 20

<!-- b000504 | caption | pages [18] -->
Figure 13: Reduced cost

<!-- b000505 | caption | pages [18] -->
Figure 14: Change range of variables

<!-- b000506 | prose | pages [18] -->
8

<!-- b000507 | heading | pages [18] -->
Conclusion

<!-- b000508 | prose | pages [18] -->
8.1

<!-- b000509 | heading | pages [18] -->
Strengths

<!-- b000510 | prose | pages [18] -->
• Applies widely The differential equation model and the linear programming model can be easily modiﬁed to accommodate to various situation.

<!-- b000511 | heading | pages [18] -->
• The result is a global optimum solution

<!-- b000512 | prose | pages [18] -->
Our differential equation model consider the time value of the delayed passengers and the construction cost of the area at the same time which can result in a global optimum solution.

<!-- b000513 | prose | pages [18] -->
• Good ﬂexibility According to our analysis, our model can always ﬁnd the optimum solution under various kinds of conditions.

<!-- b000514 | prose | pages [18] -->
• Technical supporting We use many theory and methods to support our work. And each one of them is

<!-- b000515 | furniture | pages [19] -->
Team # 68303

<!-- b000516 | furniture | pages [19] -->
Page 18 of 20

<!-- b000517 | prose | pages [19] -->
used reasonably and properly.

<!-- b000518 | prose | pages [19] -->
8.2

<!-- b000519 | heading | pages [19] -->
Weakness

<!-- b000520 | prose | pages [19] -->
• Inaccuracy When considering the value of parameters, we obtain them through a lot of differ- ent research papers which may inﬂuence the result of our model.

<!-- b000521 | heading | pages [19] -->
• Simplifying assumptions

<!-- b000522 | prose | pages [19] -->
To simplify the model, we make a few assumptions which may affect the result of our model.

<!-- b000523 | prose | pages [19] -->
• Lack of data For the lack of data, we have to simulate the models abstracted from the reality to obtain the data we need which may be different from the real data.

<!-- b000524 | heading | pages [19] -->
References

<!-- b000525 | references | pages [19] -->
[1] GRIGG

<!-- b000526 | references | pages [19] -->
G

<!-- b000527 | references | pages [19] -->
M.

<!-- b000528 | references | pages [19] -->
THE

<!-- b000529 | references | pages [19] -->
HIGHWAY

<!-- b000530 | references | pages [19] -->
CAPACITY

<!-- b000531 | references | pages [19] -->
MANUAL[J].

<!-- b000532 | references | pages [19] -->
ITE

<!-- b000533 | references | pages [19] -->
JOURNAL-

<!-- b000534 | references | pages [19] -->
INSTITUTE OF TRANSPORTATION ENGINEERS, 1991, 61(1): 5-5.

<!-- b000535 | references | pages [19] -->
[2] Lee W P, Osman M A, Talib A Z, et al. Dynamic trafﬁc simulation for trafﬁc con-

<!-- b000536 | references | pages [19] -->
gestion problem using an enhanced algorithm[J]. International Journal of Math-

<!-- b000537 | references | pages [19] -->
ematical, Computational, Physical, Electrical and Computer Engineering (World

<!-- b000538 | references | pages [19] -->
Academy of Science, Engineering and Technology), 2008, 2(9): 277-284.

<!-- b000539 | references | pages [19] -->
[3] Jing Li. Japan highway design essentials[J]. 1991.

<!-- b000540 | references | pages [19] -->
[4] Manual H C. Highway capacity manual[J]. Washington, DC, 2000. Addison-Wesley

<!-- b000541 | references | pages [19] -->
Publishing Company, 1986.

<!-- b000542 | references | pages [19] -->
[5] Li Su. Study on Design of expressway toll station[D]. Changan University, 2012.

<!-- b000543 | references | pages [19] -->
[6] P.T.harker. Alternative methods of questioning in the analytic hierarchy process,

<!-- b000544 | references | pages [19] -->
Math modeling,Vol.9,No.3-5(1987)

<!-- b000545 | references | pages [19] -->
[7] Honglei Ru. Study on Inﬂuencing Factors of urban road capacity[D]. Tongji Univer-

<!-- b000546 | references | pages [19] -->
sity, 2008.

<!-- b000547 | references | pages [19] -->
[8] Chandler A, Mian M, Baliga P. The Booth Tolls for Thee[J]. UMAPJournal, 2005: 283.

<!-- b000548 | references | pages [19] -->
[9] Guizzo E. How googles self-driving car works[J]. IEEE Spectrum Online, October,

<!-- b000549 | references | pages [19] -->
2011, 18.

<!-- b000550 | furniture | pages [20] -->
Team # 68303

<!-- b000551 | furniture | pages [20] -->
Page 19 of 20

<!-- b000552 | references | pages [20] -->
Dear New Jersey Turnpike Authority,

<!-- b000553 | references | pages [20] -->
We are here to help you with determining if there are better solutions of the merging

<!-- b000554 | references | pages [20] -->
area following the toll barrier than any in common use. This letter explains our optimum

<!-- b000555 | references | pages [20] -->
solution model, and provide a series of suggestions under various circumstances.

<!-- b000556 | references | pages [20] -->
As we all known, the main purpose of researching the problem of merge after toll is

<!-- b000557 | references | pages [20] -->
to control the cost and to improve the throughput and the safety of the area as much as

<!-- b000558 | references | pages [20] -->
possible at the same time. Thus our model is built based on these three factors.

<!-- b000559 | references | pages [20] -->
Firstly, before proposing a better solution, we should research the advantages and

<!-- b000560 | references | pages [20] -->
the disadvantages of the existing models. We collect the characteristics of the existing

<!-- b000561 | references | pages [20] -->
models according to the shape of the area, the size of the area and the merging pattern

<!-- b000562 | references | pages [20] -->
of the area and classify them into eight kinds.

<!-- b000563 | references | pages [20] -->
Secondly, we build a simulation model to obtain the important parameters of the

<!-- b000564 | references | pages [20] -->
corresponding model, such as trafﬁc ﬂow, average queuing time, average time of delay,

<!-- b000565 | references | pages [20] -->
etc.

<!-- b000566 | references | pages [20] -->
Thirdly, we build a comprehensive evaluation model based on PCA to evaluate the

<!-- b000567 | references | pages [20] -->
eight models listed above. From the result of evaluation, we get the rank value of each

<!-- b000568 | references | pages [20] -->
model. In this way, we get the best model which is in the shape of isosceles trapezoid

<!-- b000569 | references | pages [20] -->
with stipulated merging pattern and medium size of the area among the eight existing

<!-- b000570 | references | pages [20] -->
models.

<!-- b000571 | references | pages [20] -->
On the basis of existing models, we propose a better solution. When considering the

<!-- b000572 | references | pages [20] -->
cost of the area, we promote the deﬁnition of the cost, the total cost is not just the cost of

<!-- b000573 | references | pages [20] -->
road construction, but also includes the value of queuing time and the operating cost of

<!-- b000574 | references | pages [20] -->
the tollbooths. We can get the optimum number of tollbooths and the optimum height

<!-- b000575 | references | pages [20] -->
of the trapezoid area while minimizing the total cost of the area.

<!-- b000576 | references | pages [20] -->
In reality, when the vehicles entering the area following the toll barrier, they always

<!-- b000577 | references | pages [20] -->
want to get into the travel lanes as soon as possible. Our linear programming model

<!-- b000578 | references | pages [20] -->
which determine the merging pattern of the area is based on this principle–let the ve-

<!-- b000579 | references | pages [20] -->
hicles ﬁnd the shortest path leave the area following the toll barrier. In this way, we

<!-- b000580 | references | pages [20] -->
reduce the number of merging points of the area, increase the throughput of the area

<!-- b000581 | references | pages [20] -->
and promote the accident prevention of the area.

<!-- b000582 | references | pages [20] -->
In accordance with the above research ideas, we develop a better design of the area

<!-- b000583 | references | pages [20] -->
following the toll barrier.

<!-- b000584 | references | pages [20] -->
Of course, a good design can not only work efﬁciently under normal circumstances,

<!-- b000585 | references | pages [20] -->
but also can keep running under some speciﬁc extreme circumstances. To this end, we

<!-- b000586 | references | pages [20] -->
perform several analysis to test our model.

<!-- b000587 | references | pages [20] -->
The ﬁrst one is to change the value of trafﬁc ﬂow: at the small trafﬁc ﬂow, our model

<!-- b000588 | references | pages [20] -->
can run smoothly, but the number of tollbooths may exceeds the demand. In this situa-

<!-- b000589 | references | pages [20] -->
tion ,we can close several tollbooths appropriately to reduce the operating costs. When it

<!-- b000590 | references | pages [20] -->
comes to a heavy trafﬁc ﬂow, our model can still operating well while few of congestion

<!-- b000591 | references | pages [20] -->
may happen. We can adjust our merging pattern to divert the trafﬁc.

<!-- b000592 | references | pages [20] -->
The second aspect is the situation when more autonomous(self-driving) vehicles are

<!-- b000593 | references | pages [20] -->
added to the trafﬁc ﬂow. The autonomous vehicle is controlled by the computer, which

<!-- b000594 | references | pages [20] -->
can adjust its strategy on time by choosing safer paths.The adopt of autonomous vehicles

<!-- b000595 | references | pages [20] -->
may reduce the number of trafﬁc accidents caused by human beings, and improve the

<!-- b000596 | furniture | pages [21] -->
Team # 68303

<!-- b000597 | furniture | pages [21] -->
Page 20 of 20

<!-- b000598 | references | pages [21] -->
safety of the area. Due to the safety and the efﬁciency of autonomous vehicles, we do

<!-- b000599 | references | pages [21] -->
not have to stipulate the merge pattern of the area following the toll barrier which can

<!-- b000600 | references | pages [21] -->
bring the advantages of autonomous vehicles to the full play.

<!-- b000601 | references | pages [21] -->
Considering the proportions of different kinds of tollbooths which indicated by the

<!-- b000602 | references | pages [21] -->
service time, our model can be modiﬁed by adjusting the merging pattern to accommo-

<!-- b000603 | references | pages [21] -->
date to the speciﬁc situation in which we cite two speciﬁc examples in our paper.

<!-- b000604 | references | pages [21] -->
In summary, our model has developed a way to ﬁnd the optimum solution of the

<!-- b000605 | references | pages [21] -->
area following the toll barrier. Our model is feasible and reasonable and can be adjusted

<!-- b000606 | references | pages [21] -->
to various kinds of situation in reality. Although we have proposed a better solution,

<!-- b000607 | references | pages [21] -->
we suggest that the authority should take overall account of the reality according to the

<!-- b000608 | references | pages [21] -->
factors we listed in our paper. To know how the our model run in details,please check

<!-- b000609 | references | pages [21] -->
our paper.

<!-- b000610 | references | pages [21] -->
Wish our optimal investment strategy can inspire you at the key point of solving

<!-- b000611 | references | pages [21] -->
the probable solution of merging after toll.We are very eager to hear your opinion on

<!-- b000612 | references | pages [21] -->
our performance and to have more communication about it.We look forward to hearing

<!-- b000613 | references | pages [21] -->
from you.

<!-- b000614 | references | pages [21] -->
Yours sincerely,

<!-- b000615 | references | pages [21] -->
A group of modelers who are enthusiastic about mathematical modeling.

<!-- b000616 | references | pages [21] -->
24/1/2017
