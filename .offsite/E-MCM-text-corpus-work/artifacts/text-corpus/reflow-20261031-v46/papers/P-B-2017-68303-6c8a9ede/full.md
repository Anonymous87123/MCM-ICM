# P-B-2017-68303-6c8a9ede

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
68303

<!-- b000004 | prose | pages [1] -->
T1 F1

<!-- b000005 | prose | pages [1] -->
T2 F2

<!-- b000006 | prose | pages [1] -->
T3 F3 Problem Chosen T4 F4

<!-- b000007 | title | pages [1] -->
B

<!-- b000008 | title | pages [1] -->
2017

<!-- b000009 | prose | pages [1] -->
MCM/ICM

<!-- b000010 | heading | pages [1] -->
Summary Sheet

<!-- b000011 | title | pages [1] -->
Merge Better After Toll

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
With the rapid increment of the trafﬁc ﬂow, the problem of merging after the toll barriers has risen public concern. In our paper, we aim to construct a model to ﬁnd a better design of the area following the toll barrier.

<!-- b000014 | prose | pages [1] -->
First, we classify the area following the toll barrier which may already be imple- mented into eight kinds according to the different shapes, sizes, and merging patterns of the area based on the toll plazas in reality.

<!-- b000015 | prose | pages [1] -->
Second, we use VISSIM to do the simulation of the typical eight models of the area following the toll barrier. Through setting the necessary observation points, we obtain the data of throughput, length of queues and the average time of delay we need in the following evaluation model.

<!-- b000016 | prose | pages [1] -->
Third, we build a comprehensive evaluation model based on PCA to evaluate the eight typical models and the optimum model we build. Considering the selection of the index, we choose the number of merging points to indicate accident prevention of the area, the length of queues, the throughput and the average time of delay to indicate the trafﬁc capacity of the area, and the height of the trapezoid area to indicate the con- struction cost of the area. After data normalization, we get the best model which is in the shape of isosceles trapezoid with stipulated merging pattern and medium size of the area among the eight existing models.

<!-- b000017 | prose | pages [1] -->
Fourth, in order to obtain a better solution, we build two models to obtain the opti- mum solution. The ﬁrst one is a differential equation model aimed at acquire the opti- mum height of the trapezoid area and the optimum number of tollbooths. The second one is a linear programming model which can calculate the optimum merging pattern while maximizing the throughput of the area.

<!-- b000018 | prose | pages [1] -->
Last but not least, we analyze the performance of our model under various condi- tions, and modify our model to accommodate to those conditions. Also, we use Lingo to construct sensitivity analysis of the linear programming model.

<!-- b000019 | prose | pages [1] -->
To sum up, our model is a feasible and reasonable model which can accommodate to various situations.

<!-- b000020 | furniture | pages [2] -->
Team # 68303

<!-- b000021 | furniture | pages [2] -->
Page 1 of 20

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
1 Introduction

<!-- b000024 | contents | pages [2] -->
2

<!-- b000025 | contents | pages [2] -->
1.1

<!-- b000026 | contents | pages [2] -->
Background

<!-- b000027 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
1.2

<!-- b000030 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
2

<!-- b000032 | contents | pages [2] -->
1.3

<!-- b000033 | contents | pages [2] -->
Overview of Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
2

<!-- b000035 | contents | pages [2] -->
1.4

<!-- b000036 | contents | pages [2] -->
General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
3

<!-- b000038 | contents | pages [2] -->
2 Classify the Design

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
3 Simulation Model

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
4 Evaluation Model

<!-- b000043 | contents | pages [2] -->
7

<!-- b000044 | contents | pages [2] -->
4.1

<!-- b000045 | contents | pages [2] -->
Index variables

<!-- b000046 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
7

<!-- b000048 | contents | pages [2] -->
4.2

<!-- b000049 | contents | pages [2] -->
PCA Model

<!-- b000050 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
4.3

<!-- b000053 | contents | pages [2] -->
Analysis and Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
8

<!-- b000055 | contents | pages [2] -->
5 Find the Optimum Solution

<!-- b000056 | contents | pages [2] -->
9

<!-- b000057 | contents | pages [2] -->
5.1

<!-- b000058 | contents | pages [2] -->
Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
9

<!-- b000060 | contents | pages [2] -->
5.2

<!-- b000061 | contents | pages [2] -->
Differential Equation Model . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
9

<!-- b000063 | contents | pages [2] -->
5.3

<!-- b000064 | contents | pages [2] -->
Linear Programming Model . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
12

<!-- b000066 | contents | pages [2] -->
5.4

<!-- b000067 | contents | pages [2] -->
Result and Model Testing

<!-- b000068 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
13

<!-- b000070 | contents | pages [2] -->
6 Effects and Adjustment

<!-- b000071 | contents | pages [2] -->
14

<!-- b000072 | contents | pages [2] -->
6.1

<!-- b000073 | contents | pages [2] -->
Light and Heavy Trafﬁc

<!-- b000074 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
14

<!-- b000076 | contents | pages [2] -->
6.2

<!-- b000077 | contents | pages [2] -->
Add Autonomous Vehicles . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
14

<!-- b000079 | contents | pages [2] -->
6.3

<!-- b000080 | contents | pages [2] -->
Compositions of Tollbooths . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
15

<!-- b000082 | contents | pages [2] -->
7 Sensitivity Analysis

<!-- b000083 | contents | pages [2] -->
16

<!-- b000084 | contents | pages [2] -->
7.1

<!-- b000085 | contents | pages [2] -->
Reduced Cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
16

<!-- b000087 | contents | pages [2] -->
7.2

<!-- b000088 | contents | pages [2] -->
Change Range of Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [2] -->
16

<!-- b000090 | contents | pages [2] -->
8 Conclusion

<!-- b000091 | contents | pages [2] -->
17

<!-- b000092 | contents | pages [2] -->
8.1

<!-- b000093 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
17

<!-- b000095 | contents | pages [2] -->
8.2

<!-- b000096 | contents | pages [2] -->
Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
18

<!-- b000098 | furniture | pages [3] -->
Team # 68303

<!-- b000099 | furniture | pages [3] -->
Page 2 of 20

<!-- b000100 | heading | pages [3] -->
1 Introduction

<!-- b000101 | heading | pages [3] -->
1.1 Background

<!-- b000102 | prose | pages [3] -->
The major problems facing motorists on today’s highways are congestion, accidents, and costs-too many automobiles traveling to the same place at the same time; too many automobiles, trucks, buses, bicycles, and pedestrians attempting to use the same space; too many motorists losing time unnecessarily; too many accidents occurring; and too many decisions being made on highway improvements without adequate analytical tools[1].

<!-- b000103 | prose | pages [3] -->
As an important part of the highway, the toll plaza is to blame for most of the con- gestions and accidents happen around it. Since there are usually more tollbooths than there are incoming lanes of trafﬁc, vehicles must "fan in" from larger number of tollbooth egress lanes to the smaller number of regular travel lanes. In other words, vehicles need to merge after toll.

<!-- b000104 | prose | pages [3] -->
Trafﬁc congestion normally happens when merging points are met[2], which may re- sult in long trafﬁc queues on the road. When designing merging area of the toll plaza, shape, size and merging pattern of the area should be taken into consideration. More- over, the design should reduce the risk of accident, the cost of road construction and increase the throughput as much as possible.

<!-- b000105 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000106 | prose | pages [3] -->
We are required not only to analyze the performance of the area following the toll bar- rier with different shapes, sizes, and merging patterns that may already be implemented on the aspect of accident prevention, throughput, and cost, but also to determine if there are better solutions than any in common use and evaluate the performance of them un- der different circumstances.

<!-- b000107 | prose | pages [3] -->
The problem can be analyzed into four parts:

<!-- b000108 | prose | pages [3] -->
• Analyze the existing design of the area following the toll barrier with different shapes, sizes and merging patterns.

<!-- b000109 | prose | pages [3] -->
• Build a simulation model to simulate the trafﬁc condition of different designs of the area following the toll barrier.

<!-- b000110 | prose | pages [3] -->
• Build an evaluation model to rate the performance of different designs of the area following the toll barrier.

<!-- b000111 | prose | pages [3] -->
• Find a solution which can perform better than any in common use.

<!-- b000112 | heading | pages [3] -->
1.3 Overview of Our Work

<!-- b000113 | prose | pages [3] -->
With the increment of trafﬁc ﬂow, the trafﬁc congestion happens more and more fre- quently on the highway, as it gradually becomes the main cause of trafﬁc accidents. The problem of merging after toll has become the common concern of the society.

<!-- b000114 | furniture | pages [4] -->
Team # 68303

<!-- b000115 | furniture | pages [4] -->
Page 3 of 20

<!-- b000116 | prose | pages [4] -->
Firstly, we classify the area following the toll plaza into 8 kinds according to the different shapes, sizes, and merging patterns of the area.

<!-- b000117 | prose | pages [4] -->
Secondly, we select a series of index to evaluate the existing design of the area fol- lowing the toll plaza. Through the comprehensive evaluation model based on PCA, we evaluate the existing design of the area and our own design.

<!-- b000118 | prose | pages [4] -->
Thirdly, we build a differential equation model to obtain the optimum number of toll- booths and the height of the trapezoid area and a linear programming model to acquire the optimum merging pattern of the area following the toll barrier.

<!-- b000119 | prose | pages [4] -->
Finally, we analyze the performance of our model under various conditions and the sensitivity of our model.

<!-- b000120 | heading | pages [4] -->
1.4 General Assumptions

<!-- b000121 | prose | pages [4] -->
• All the motorists would obey the trafﬁc rules. We don’t take accidents resulted from drink-driving or speeding into consideration.

<!-- b000122 | prose | pages [4] -->
• We set the average speed of the vehicles under normal circumstances. Ignore the impact of weather conditions.

<!-- b000123 | prose | pages [4] -->
• We assume the vehicles on the highway are all cars, for other kinds of vehicles accounts for a relatively small proportion.

<!-- b000124 | prose | pages [4] -->
• The queue at the merging point would not affect the service of the tollbooths.

<!-- b000125 | prose | pages [4] -->
• All the tollbooths on the toll plaza operate all day.

<!-- b000126 | heading | pages [4] -->
2 Classify the Design

<!-- b000127 | prose | pages [4] -->
Before constructing the simulation model, we need to classify the design of the area following the toll barrier according to the shape, the size, as well as the merging pattern.

<!-- b000128 | prose | pages [4] -->
According to the satellite map, we ﬁnd that most of the area following the toll bar- rier can be abstracted into two shapes which are right-angled trapezoid and isosceles trapezoid. { right-angled trapezoid, Sp1 shape isosceles trapezoid, Sp2

<!-- b000129 | prose | pages [4, 5] -->
Then we ﬁnd that the height of the trapezoid determines the size of the area following the toll barrier when the number and width of the tollbooths and travel lanes are deﬁned. According to Japan highway design essentials[3], we choose S/H to indicate the size of the area. To simplify our model, we only take small size S/H = 1/3 and large size S/H = 1/6 into simulation.  H = 1 S   3, Sz1 size H = 1 S   6, Sz2 According to our observation, vehicles can change into any lane when getting out of the toll barrier. On the basis of this observation, we assume that there may be a merging pattern which stipulates the vehicles on the left side can only drive down to the left lanes and the vehicles on the right can only drive down to the right lanes. The stipulation may reduce the risk of collision. { normal merging pattern, Mp1 merging pattern stipulated merging pattern, Mp2

<!-- b000130 | furniture | pages [5] -->
Team # 68303

<!-- b000131 | furniture | pages [5] -->
Page 4 of 20

<!-- b000133 | caption | pages [5] -->
Figure 1: normal and stipulated merging pattern

<!-- b000134 | heading | pages [5] -->
3 Simulation Model

<!-- b000135 | prose | pages [5] -->
For the lack of data, we choose frequently used software VISSIM to simulate the trafﬁc condition following the toll barrier.

<!-- b000136 | prose | pages [5] -->
Before the simulation, we need to set a series of parameters. According to the exam- ple mentioned in the problem that the toll highway has L lanes of travel in each direction and a barrier toll contains B tollbooths in each direction, we set the number of lanes and tollbooths L = 3, B = 8 the same as the example.

<!-- b000137 | prose | pages [5] -->
After consulting Highway Capacity Manual 2000 [4], we set the width of each lane d = 3.5m, the combined width of tollbooth and lane D = 5.5m, and the average speed of vehicles on the highway v = 120km/h. For S = (D ∗B −d ∗L) ∗0.5, S = 16.75. When it comes to a small-sized area S/H = 1/3, H = 50.25. Similarly, when it comes to a large-sized area S/H = 1/6, H = 50.25.

<!-- b000138 | prose | pages [5] -->
Since we only have to determine the area following the toll barrier, we just need to set the number of vehicles leaving the toll barrier per hour instead of considering the number of vehicles on the travel lanes entering the barrier toll. Through information research[5], we ﬁnd that the temporary retention time at the toll booth is 12 seconds. We want to stimulate the process for 3600 seconds, so the number of vehicles leaving the toll barrier is approximately 3600/12 = 300 vehicles per hour per lane.

<!-- b000139 | prose | pages [5] -->
To simplify our model, we set the vehicle composition as 100% cars. Considering that there will be many merging points in the area following the barrier toll, we set con- ﬂict areas between each pair of possible crossed paths to simulate the process of vehicle collision avoidance.

<!-- b000140 | furniture | pages [6] -->
Team # 68303

<!-- b000141 | furniture | pages [6] -->
Page 5 of 20

<!-- b000142 | caption | pages [6] -->
Table 1: Parameters

<!-- b000143 | prose | pages [6] -->
Parameter Symbol Value

<!-- b000144 | prose | pages [6] -->
T simulation time 3600s

<!-- b000145 | prose | pages [6] -->
L number of travel lanes 3

<!-- b000146 | prose | pages [6] -->
B number of toll booths 8

<!-- b000147 | prose | pages [6] -->
d width of travel lanes 3.5m

<!-- b000148 | prose | pages [6] -->
D combined width of tollbooth and lane 5.5m

<!-- b000149 | prose | pages [6] -->
In ingress trafﬁc ﬂow of the area 2400 vehicles/h

<!-- b000150 | prose | pages [6] -->
V average speed of vehicles on the highway 120km/h

<!-- b000151 | caption | pages [6] -->
Figure 2: Set collision areas

<!-- b000152 | prose | pages [6] -->
Afterwards, we set travel time sections, data collection point, and queue counters of the area to monitor the values of delay, number of passing vehicles and queue length.

<!-- b000153 | prose | pages [6] -->
Then, we simulate eight kinds of area following the toll barrier according to our above classiﬁcation, to obtain the data we need in the evaluation model.

<!-- b000154 | caption | pages [6] -->
Figure 3: Kind 1: Sp1,Sz1,Mp1

<!-- b000155 | caption | pages [6] -->
Figure 4: Kind 2: Sp1,Sz2,Mp1

<!-- b000156 | prose | pages [6] -->
After simulation, we collect data from the program of the eight models.

<!-- b000157 | furniture | pages [7] -->
Team # 68303

<!-- b000158 | furniture | pages [7] -->
Page 6 of 20

<!-- b000159 | caption | pages [7] -->
Figure 5: Kind 3: Sp1,Sz1,Mp2

<!-- b000160 | caption | pages [7] -->
Figure 6: Kind 4: Sp1,Sz2,Mp2

<!-- b000161 | caption | pages [7] -->
Figure 7: Kind 5: Sp2,Sz1,Mp1

<!-- b000162 | caption | pages [7] -->
Figure 8: Kind 6: Sp2,Sz2,Mp1

<!-- b000163 | caption | pages [7] -->
Figure 9: Kind 7: Sp2,Sz1,Mp2

<!-- b000164 | caption | pages [7] -->
Figure 10: Kind 8: Sp2,Sz2,Mp2

<!-- b000165 | furniture | pages [8] -->
Team # 68303

<!-- b000166 | furniture | pages [8] -->
Page 7 of 20

<!-- b000167 | caption | pages [8] -->
Table 2: simulation data of 8 kinds of models

<!-- b000168 | prose | pages [8] -->
height of throughput average length number of kind delay(s) trapezoid (m) (veh/h) of queue(m) merging points

<!-- b000169 | prose | pages [8] -->
1 50.5 2149 13.8 21.38 24

<!-- b000170 | prose | pages [8] -->
2 105 2193 20.5 25.49 24

<!-- b000171 | prose | pages [8] -->
3 50.5 2271 8.2 10.02 7

<!-- b000172 | prose | pages [8] -->
4 105 2191 14.1 17.65 7

<!-- b000173 | prose | pages [8] -->
5 50.5 2178 10.4 18.77 24

<!-- b000174 | prose | pages [8] -->
6 105 2168 17.3 20.04 24

<!-- b000175 | prose | pages [8] -->
7 50.5 2301 5.8 8.13 7

<!-- b000176 | prose | pages [8] -->
8 105 2228 11.92 13.26 7

<!-- b000177 | heading | pages [8] -->
4 Evaluation Model

<!-- b000178 | prose | pages [8] -->
To illustrate the independence, and the relationship between different variables, we use Principal Component Analysis (PCA)[6]. When some of the variables can explain a great percentage of the results, we can say these variables are strongly correlated and we can use the great one to represent others. After that, we can build a comprehensive evaluation model which based on PCA to evaluate our area models.

<!-- b000179 | heading | pages [8] -->
4.1 Index variables

<!-- b000180 | prose | pages [8] -->
We are required to consider the accident prevention, throughput and cost of our mod- els. Since some of the aspects cannot be valued directly, we have to ﬁnd some other parameters to indicate them.

<!-- b000181 | prose | pages [8] -->
Firstly, as most of the trafﬁc accidents happen at the merging point of lanes, we set the number of merging point of the area as the index to indicate accident prevention level.

<!-- b000182 | prose | pages [8] -->
Secondly, the cost of land and road construction is proportional to the area size. Since the sum of the bottoms of the trapezoid area are the same, we use the height of the trapezoid area to indicate the construction cost.

<!-- b000183 | prose | pages [8] -->
Thirdly, there are several indicators of the trafﬁc performance in the area following the toll barrier. We choose the average delay time, the length of queue at merging points and the throughput (number of vehicles per hour passing the point where the end of the plaza joins the eight outgoing trafﬁc lanes) to indicate[7].

<!-- b000184 | furniture | pages [9] -->
Team # 68303

<!-- b000185 | furniture | pages [9] -->
Page 8 of 20

<!-- b000186 | heading | pages [9] -->
4.2 PCA Model

<!-- b000187 | prose | pages [9] -->
The model is better, if the values of delay time, the length of queue at merging points and the number of merging points are smaller. Since PCA determines the ranking of the models based on the comprehensive score, we take the reciprocal of these values.

<!-- b000188 | prose | pages [9] -->
In order to facilitate the further analysis, we do the data normalization. Map the index variable data setx = x1, x2, . . . , x5. Set aij as the value of index variable j of model i. ˜aij = aij −µj , i = 1, . . . , 8, j = 1, . . . , 5 (1) sj ˜xj = xj −µj , j = 1, . . . , 5 (2) sj √ ∑n ∑n Where: µj = 1 1 i=1(aij −µi)2. i=1 aij, sj = n−1 n

<!-- b000189 | prose | pages [9] -->
Then we calculate the correlation coefﬁcient matrix R = (rij)5∗5:

<!-- b000190 | prose | pages [9] -->
∑n k=1 ˜aki ∗˜akj rij = , i, j = 1, . . . , 5 (3) n −1

<!-- b000191 | prose | pages [9] -->
Afterwards, we calculate the eigenvalues λj and the corresponding eigenvectors of R, to form the ﬁve new index variables. On the basis of the eigenvalues, we can get the contribution rate b and the accumulative contributions rate α of the parameters.

<!-- b000192 | prose | pages [9] -->
λj ∑m bj = , j = 1, . . . , 5 (4) k=1 λk ∑p k=1 λk αp = ∑5 (5) k=1 λk

<!-- b000193 | prose | pages [9] -->
Since b=[72.8902,21.8503,3.8901,1.0350,0.3341] and α=[72.8902,94.7408,98.6309,99.6659,100], we select the ﬁrst three components as the three principle components y1, y2, y3 to replace the used ﬁve index variables.

<!-- b000194 | prose | pages [9] -->
According to the principle components, the ﬁrst component contributes most to the throughput, the second component contributes most to the cost, and the third compo- nent contributes most to the accidents prevention.

<!-- b000195 | heading | pages [9] -->
4.3 Analysis and Result

<!-- b000196 | prose | pages [9] -->
Multiplying the contribution rate with the value of corresponding principle compo- nents, we can obtain the comprehensive scores of our eight models.

<!-- b000197 | prose | pages [9] -->
p ∑ Z = bjyj (6) j=1

<!-- b000198 | prose | pages [9] -->
The ﬁnal score of the eight models are shown in Table 3.

<!-- b000199 | prose | pages [9] -->
From the result above, we ﬁnd that right-angled trapezoid is better than isosceles trapezoid and the stipulated merging pattern is better than normal merging pattern.

<!-- b000200 | furniture | pages [10] -->
Team # 68303

<!-- b000201 | furniture | pages [10] -->
Page 9 of 20

<!-- b000202 | caption | pages [10] -->
Table 3: Evaluation Result of Models

<!-- b000203 | prose | pages [10] -->
Rank Model Score Rank Model Score

<!-- b000204 | prose | pages [10] -->
1 7 2.5822 5 4 -0.6187

<!-- b000205 | prose | pages [10] -->
2 3 1.6134 6 1 -0.6190

<!-- b000206 | prose | pages [10] -->
3 8 -0.0457 7 6 -1.3492

<!-- b000207 | prose | pages [10] -->
4 5 -0.1332 8 2 -1.4298

<!-- b000208 | prose | pages [10] -->
When it comes to the size of the area, we assume that the longer the height of the trapezoid area is, the larger the size of the area is which may increase the throughput of the area. According to the scores listed above, the result is contrary to our assump- tion. Then we simulate a new circumstance whose height is half of the 5th kind of model and evaluate it through the method above. The evaluation score of this model is -0.6726, while the evaluation score of the 5th kind of model is -0.1332. Thus, we can come to a conclusion that it may exist an optimum height of the trapezoid area to make the throughput of the area come to its maximum. Meanwhile, we also should take the increment of the cost resulted from the increment of the height of the trapezoid area into consideration.

<!-- b000209 | heading | pages [10] -->
5 Find the Optimum Solution

<!-- b000210 | heading | pages [10] -->
5.1 Overview

<!-- b000211 | prose | pages [10] -->
From our evaluation model, we can see that the height of the trapezoid area and the merging pattern have a great impact on the throughput of the area following the toll bar- rier. When determining if there exists a better solution, we should include quantitative or qualitative estimates of these two parameters. Also, the number of tollbooths may inﬂuence the number of the vehicles passing through the toll barrier, while this outﬂow of the toll barrier may affect the trafﬁc pressure of the area following the toll barrier. So we should also take the number of tollbooths into consideration.

<!-- b000212 | prose | pages [10] -->
When it comes to the cost of the area which is determined by the size of the area, there are two parameters to indicate: the height of the trapezoid area and the number of toll booths which determine the length of one bottom of the trapezoid area and may add to the operating cost of the toll plaza.

<!-- b000213 | prose | pages [10] -->
Then we can build two models to ﬁnd the optimum solution. The ﬁrst one is a dif- ferential equation model aimed at minimizing the cost of the road construction and the operating cost of toll booths. The second one is a linear programming model calculating the optimum strategy of merging pattern.

<!-- b000214 | heading | pages [10] -->
5.2 Differential Equation Model

<!-- b000215 | prose | pages [10, 11] -->
(1) Terms and Deﬁnitions Symbol Meaning

<!-- b000216 | furniture | pages [11] -->
Team # 68303

<!-- b000217 | furniture | pages [11] -->
Page 10 of 20

<!-- b000218 | caption | pages [11] -->
Table 4: Symbols

<!-- b000220 | prose | pages [11] -->
C total cost

<!-- b000221 | prose | pages [11] -->
W average waiting time per vehicle in the toll plaza

<!-- b000222 | prose | pages [11] -->
W1 time spent in lines

<!-- b000223 | prose | pages [11] -->
W2 service time

<!-- b000224 | prose | pages [11] -->
W3 time spent passing through the area following the toll barrier

<!-- b000225 | prose | pages [11] -->
v average time value of a person in one vehicle

<!-- b000226 | prose | pages [11] -->
µ average number of person in one vehicle

<!-- b000227 | prose | pages [11] -->
n the number of vehicles passing through the toll plaza

<!-- b000228 | prose | pages [11] -->
C1 the operation cost of a tollbooth per day

<!-- b000229 | prose | pages [11] -->
C2 the construction cost of unit area

<!-- b000230 | prose | pages [11] -->
F(t) value of inﬂux at t minute

<!-- b000231 | prose | pages [11] -->
O(t, B) value of outﬂux at t minute with B tollbooths

<!-- b000232 | prose | pages [11] -->
s the average number of vehicles which one tollbooth can serve per minute

<!-- b000233 | prose | pages [11] -->
k outﬂux barrier

<!-- b000234 | prose | pages [11] -->
• Inﬂux is the number of vehicles entering the toll plaza per minute.(veh/min)

<!-- b000235 | prose | pages [11] -->
• Outﬂux is the number of vehicles existing the toll plaza per minute.(veh/min)

<!-- b000236 | prose | pages [11] -->
• Total cost is the sum of the value of time wasted in the toll plaza, the operating cost of toll booths and the construction cost of the area.

<!-- b000237 | heading | pages [11] -->
(2) Data processing

<!-- b000238 | prose | pages [11] -->
From a previous research paper’s trafﬁc ﬂow data, we ﬁnd the value of inﬂux for a toll plaza on a given typical day. Since we need an inﬂux rate at every minute of the day, instead of just once an hour, we select a Fourier Series approximation with 8 terms to ﬁnd a close ﬁt[8]. The ﬁtting function of the inﬂux at t minute is described below where 24 = 0.2513. The approximation ﬁts the data point with an R2 value of 0.9997 which ω = 2π is close to 1. It represents the result is in good agreement with the research data.

<!-- b000239 | prose | pages [11] -->
F(t) = 41.68 −16.38 cos(tω) −18.59 cos(2tω) + 3.572 cos(3tω) + 7.876 cos(4tω) . . .

<!-- b000240 | prose | pages [11] -->
−0.5048 cos(tω) −2.970 cos(6tω) + 0.2518 cos(7tω) + 0.5785 cos(8tω) . . .

<!-- b000241 | prose | pages [11] -->
+ 12.53 sin(tω) + 0.6370 sin(2tω) −13.67 sin(3tω) + 0.4378 sin(4tω) . . .

<!-- b000242 | prose | pages [11] -->
+ 6.930 sin(5tω) + 0.4869 sin(6tω) −1.554 sin(7tω) −0.5871 sin(8tω) (7)

<!-- b000243 | prose | pages [11, 12] -->
(3) Establishment We formulate a function C(B, H) to ﬁnd the number of tollbooths B and the height of the trapezoid area H that minimize the total cost C.

<!-- b000244 | furniture | pages [12] -->
Team # 68303

<!-- b000245 | furniture | pages [12] -->
Page 11 of 20

<!-- b000247 | prose | pages [12] -->
C(B, H) = (W1 + W2 + W3)vµn + C1B + C2H(BD −Ld) (8) 2

<!-- b000248 | prose | pages [12] -->
Firstly, we need to calculate the un-known parameters in the function.

<!-- b000249 | prose | pages [12] -->
• F(t) is calculated from the above data processing.

<!-- b000250 | prose | pages [12] -->
• For the randomness of O(t, B), we use the average value of outﬂux per minute in simulation as O(t, B).

<!-- b000251 | prose | pages [12] -->
• k(veh/min) is relevant to L and H, while irrelevant to B. If the value of outﬂux exceeds k, trafﬁc congestion may happen.

<!-- b000252 | prose | pages [12] -->
∫24

<!-- b000253 | prose | pages [12] -->
• We can integrate F(t) over time to calculate n = 0 3600F(t) dt.

<!-- b000254 | prose | pages [12] -->
• For W1 represents the average amount of time each time spent waiting in lines before reaching the tollbooth, we need to integrate over time to calculate how many cars were forced to wait in line. So, the value of W1(t) can be depicted as:

<!-- b000255 | prose | pages [12] -->
{∫24 ∫t 0 3600(F(τ)−Bs) dt dτ , F(τ) > Bs 0 n W1 = (9) F(τ) ≤Bs 0,

<!-- b000256 | prose | pages [12] -->
• The way to calculate W3 is similar to the way we used to ﬁnd W1.

<!-- b000257 | prose | pages [12] -->
{∫24 ∫t 0 3600(O(τ,B)−k) dt dτ , O(τ, B) > k 0 n W3 = (10) O(τ, B) ≤k 0,

<!-- b000258 | prose | pages [12] -->
• Apparently, W2 is the reciprocal of s. So, W2 = 1 s.

<!-- b000259 | prose | pages [12] -->
(4) Calculation

<!-- b000260 | prose | pages [12] -->
When solving the integral equation above, we set a variance range for B and calculate the corresponding W1 and W3 for each B respectively. A Mathematica quartic polynom- inal ﬁt is then done on the resulting points. Through this ﬁtting procedure, we can get the function W1(B) and W3(B).

<!-- b000261 | prose | pages [12] -->
To minimize the value of C(B, H), we take the partial derivative of C(B, H).

<!-- b000262 | prose | pages [12] -->
∂C(B, H) = vµn(∂W1(B) + ∂W3(B, H) ) + C1 + C2HD (11) ∂B ∂B ∂B 2

<!-- b000263 | prose | pages [12] -->
+ C2(BD −Ld) ∂C(B, H) = vµn∂W3(B, H) (12) ∂H ∂H 2

<!-- b000264 | prose | pages [12] -->
Set these two formulas equal to 0. Then, we can compute the stationary points and the Hessian matrix. If the matrix is a positive deﬁnite matrix, the stationary point is the optimum B and H. When it comes to the example the title cite in which the number of travel lanes L = 3, the optimum number of toll booths B = 6, and the optimum height of the trapezoid area H = 35.6472m.

<!-- b000265 | furniture | pages [13] -->
Team # 68303

<!-- b000266 | furniture | pages [13] -->
Page 12 of 20

<!-- b000267 | heading | pages [13] -->
5.3 Linear Programming Model

<!-- b000268 | prose | pages [13] -->
We develop a vehicle transition matrix TB∗L in which tij represents the probability of vehicles which exit from tollbooth i drive down to lane j. We can abstract a merging pattern from matrix T by selecting the largest element i of column j in the matrix which means vehicles exiting from tollbooth i will merge into travel lane j.

<!-- b000269 | prose | pages [13] -->
Since we assume that the service ability of each toll booth is the same, we set the out- ﬂux probability vector of the toll barrier as P = [ 1 B, 1 B, . . . , 1 B]B. To increase the through- put of the area following the toll barrier, we assume the number of fan in to each of the travel lane is allocated averagely. Then, we set the inﬂux probability of the travel lane following the toll barrier as Q = [ 1 L, L L, . . . , 1 L]L.

<!-- b000270 | prose | pages [13] -->
In order to allocate the vehicles to each travel lane following the toll barrier averagely, we get:

<!-- b000271 | prose | pages [13] -->
P ∗T = Q (13)

<!-- b000272 | prose | pages [13] -->
The total probability for vehicles driving down to each of the travel lane is 1.

<!-- b000273 | prose | pages [13] -->
L ∑ Tij = 1 (14) j=1

<!-- b000274 | prose | pages [13] -->
The objective is to maximize the throughput with the speciﬁed value of L, B, H. In other words, we need to minimize the desired length of the vehicles travel path between the toll barrier and the travel lane.

<!-- b000275 | prose | pages [13, 14] -->
We build a simple model shown as ﬁgure 11 to calculate the length z of every travel path. √ H2 + [(j −1)d + (i −1)SD]2 z = (15) Then, we can get the objective function as following:

<!-- b000276 | caption | pages [13] -->
Figure 11: Simple model for calculation

<!-- b000277 | furniture | pages [14] -->
Team # 68303

<!-- b000278 | furniture | pages [14] -->
Page 13 of 20

<!-- b000280 | prose | pages [14] -->
B L ∑ ∑ Tij ∗z min g = (16) i=1 j=1

<!-- b000281 | prose | pages [14] -->
From the conditions and object functions listed above, we have constructed a linear programming model.

<!-- b000282 | prose | pages [14] -->
B L ∑ ∑ √ H2 + [(j −1)d + (i −1)SD]2 Tij ∗ min g = object function:

<!-- b000283 | prose | pages [14] -->
i=1 j=1

<!-- b000284 | prose | pages [14] -->
 P ∗T = Q    L ∑ s.t.  Tij = 1   j=1

<!-- b000285 | prose | pages [14] -->
For example, when we set B = 6, L = 3, the optimum vehicle transition matrix T is as following.   1 0 0   1 0 0

<!-- b000286 | prose | pages [14] -->
0 1 0 T = 0 1 0

<!-- b000287 | prose | pages [14] -->
0 0 1

<!-- b000288 | prose | pages [14] -->
0 0 1

<!-- b000289 | prose | pages [14] -->
From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 and 2 should merge into lane 1. Vehicles leaving from tollbooth 3 and 4 should merge into lane 2. Vehicles leaving from tollbooth 5 and 6 should merge into lane 3.

<!-- b000290 | heading | pages [14] -->
5.4 Result and Model Testing

<!-- b000291 | prose | pages [14] -->
From the result above, we ﬁnd the optimum solution of three lanes is in the shape of isosceles trapezoid with six tollbooths and stipulated merging pattern and the height of the area following the toll barrier is 35.6472m .

<!-- b000292 | prose | pages [14] -->
In order to test if the solution is better than the above eight existing models, we put the corresponding data into our simulation model and evaluation model.

<!-- b000293 | prose | pages [14] -->
The ﬁnal score of our model is 4.3026 which is higher than the existing eight models we discussed above.

<!-- b000294 | furniture | pages [15] -->
Team # 68303

<!-- b000295 | furniture | pages [15] -->
Page 14 of 20

<!-- b000296 | caption | pages [15] -->
Figure 12: Testing Simulation

<!-- b000297 | heading | pages [15] -->
6 Effects and Adjustment

<!-- b000298 | heading | pages [15] -->
6.1 Light and Heavy Trafﬁc

<!-- b000299 | prose | pages [15] -->
Under the condition of light trafﬁc, the inﬂux and outﬂux value of the tollbooths will decline. For the drop of the number of vehicles, the possibility of trafﬁc congestion will decrease. Thus when it comes to light trafﬁc, the throughput of the area will not show up while the principle problem is that the number of toll booths may exceed the demand which may waste the operation cost of the area. We can calculate the optimum number of tollbooths by modifying the inﬂux parameter of our differential equation model. Then some of the redundant tollbooths can be shut down appropriately to ensure that we can reduce the operation cost to the greatest extend without reducing the throughput of the area.

<!-- b000300 | prose | pages [15] -->
When it comes to heavy trafﬁc, the possibility of trafﬁc congestion will increase for the rise of inﬂux value of the tollbooths. Our model which adopts an optimum merging strategy, number of tollbooths and the size of the area following the toll barriers can work well under the pressure of heavy trafﬁc. However, when the number of vehicles reach a certain level, we can adjust the merging strategy to promote the capacity of the area following the toll barrier. For example, if we ﬁnd the nearest lane a of the toll barrier i, then we can set a proper number of b based on the reality and value of L to make tij = 0, j /∈[a −b, a + b].

<!-- b000301 | prose | pages [15] -->
On the one hand, the adjustment can reduce the delay time of vehicles passing through the area following the toll barrier. On the other hand, it can reduce the possibility of accident which caused from heavy trafﬁc while it may increase the length of queue at merging points which should be studied by our further research.

<!-- b000302 | heading | pages [15] -->
6.2 Add Autonomous Vehicles

<!-- b000303 | prose | pages [15] -->
After our research, we ﬁnd that the autonomous vehicles have the following advantages[9]:

<!-- b000304 | prose | pages [15, 16] -->
• Safety: The vehicle is controlled by computer. So it can adjust its driving route on time and choose the safer path when entering the area following the toll barrier. As a result, self-driving can reduce the risk of trafﬁc accidents caused by limitations of human beings.

<!-- b000305 | furniture | pages [16] -->
Team # 68303

<!-- b000306 | furniture | pages [16] -->
Page 15 of 20

<!-- b000308 | prose | pages [16] -->
• Efﬁciency: Compared to normal vehicles, autonomous vehicles can adjust the gap between vehicles and the speed of vehicles intelligently which can lead to lower possibility of trafﬁc congestion.

<!-- b000309 | prose | pages [16] -->
Due to the safety and the efﬁciency of autonomous vehicles, we do not have to stip- ulate the merge pattern of the area following the toll barrier which can bring the advan- tages of autonomous vehicles to the full play.

<!-- b000310 | heading | pages [16] -->
6.3 Compositions of Tollbooths

<!-- b000311 | prose | pages [16] -->
Different compositions of tollbooths may affect the outﬂux value of the toll barrier, which is represented by outﬂux probability vector of the toll barrier P in the linear pro- gramming model.

<!-- b000312 | prose | pages [16] -->
There are three kinds of tollbooths listed in the problem. We set the average service rate of tollbooths i in type k as rik in which type 1 is conventional tollbooth, type 2 is exact-change tollbooth, and type 3 is electronic toll collection booth. From our research[9], ri1 = 5, ri2 = 7, and ri3 = 20 .The total service rate is r = ∑B i=1 rik, k = 1, 2, 3. The outﬂux probability vector of the toll barrier P should be modiﬁed as P ′ = n r [rik, . . . , rBk], k = 1, 2, 3.

<!-- b000313 | prose | pages [16] -->
Under the optimum condition we calculated in the previous models in which L = 3, B = 6, H = 35.6472, D = 5.5, d = 3.5, we assume one kind of proportion of tollbooths in which NO.1 and NO.2 tollbooths are electronic toll collection booths, No.3 and No.4 tollbooths are conventional toll booths, and No.5 and No.6 tollbooths are exact-change tollbooths. Then we input the data into our linear programming model. The optimum result vehicle transition matrix T1 is as following:

<!-- b000314 | prose | pages [16] -->
  1 0 0   0 0.8833 0.1167

<!-- b000315 | prose | pages [16] -->
0.2667 0.7333 0 T1 = 0 0 1

<!-- b000316 | prose | pages [16] -->
0 0 1

<!-- b000317 | prose | pages [16] -->
0 0 1

<!-- b000318 | prose | pages [16] -->
From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 enter into lane 1. Vehicles leaving from tollbooth 2 and 3 should merge into lane 2. Vehicles leaving from tollbooth 4, 5 and 6 should merge into lane 3.

<!-- b000319 | prose | pages [16, 17] -->
Then, we assume another one kind of proportion of tollbooths in which NO.1, NO.2, NO.3 tollbooths are electronic toll collection booths, No.4 tollbooth is conventional toll booths, and No.5 and No.6 tollbooths are exact-change tollbooths. Then we input the data into our linear programming model. The optimum result vehicle transition matrix T2 is as following:   1 0 0   0.3167 0.6833 0

<!-- b000320 | furniture | pages [17] -->
Team # 68303

<!-- b000321 | furniture | pages [17] -->
Page 16 of 20

<!-- b000323 | prose | pages [17] -->
0 0.6363 0.3667 T2 = 0 0 1

<!-- b000324 | prose | pages [17] -->
0 0 1

<!-- b000325 | prose | pages [17] -->
0 0 1

<!-- b000326 | prose | pages [17] -->
From the optimum vehicle transition matrix above, we can ﬁnd the optimum merg- ing pattern with 3 travel lanes and 6 tollbooths. Vehicles leaving from tollbooth 1 enter into lane 1. Vehicles leaving from tollbooth 2 and 3 should merge into lane 2. Vehicles leaving from tollbooth 4, 5 and 6 should merge into lane 3.

<!-- b000327 | prose | pages [17] -->
In the way we illustrated in two examples above, Our model can adjust to different proportions of the three common kinds of tollbooths.

<!-- b000328 | prose | pages [17] -->
Then, we take extreme cases into consideration. If the proportion of electronic toll collection booths is too high, the number of vehicles exiting the toll barrier will increase signiﬁcantly. It is similar to the condition of heavy trafﬁc, we can solve it in the same way as the heavy trafﬁc condition.

<!-- b000329 | heading | pages [17] -->
7 Sensitivity Analysis

<!-- b000330 | prose | pages [17] -->
We do two kinds of sensitivity analysis on our linear programming model.

<!-- b000331 | heading | pages [17] -->
7.1 Reduced Cost

<!-- b000332 | prose | pages [17] -->
Reduced cost is the increment of objective function, when one of the variables increased by one unit. We use LINGO to calculate the reduced cost of every variables. The result is shown in ﬁgure 13.

<!-- b000333 | prose | pages [17] -->
The result indicates that when variable t13 and t61 increase by one unit, it will produce a larger deviation on the objective function. In other words, the desired number of the vehicles selecting the longest path to get into the travel lane increases signiﬁcantly, while the throughput of the area will decline at the same time. These kinds of selection may lead to the increment of merging points which is bad for accident prevention. Therefore, we should avoid this kind of situation.

<!-- b000334 | heading | pages [17] -->
7.2 Change Range of Variables

<!-- b000335 | prose | pages [17] -->
We use LINGO to calculate the change range of variables with the same optimum solution. The result is shown in ﬁgure 14.

<!-- b000336 | prose | pages [17] -->
The result indicates the reasonable error range of the construction in reality.

<!-- b000337 | furniture | pages [18] -->
Team # 68303

<!-- b000338 | furniture | pages [18] -->
Page 17 of 20

<!-- b000339 | caption | pages [18] -->
Figure 13: Reduced cost

<!-- b000340 | caption | pages [18] -->
Figure 14: Change range of variables

<!-- b000341 | heading | pages [18] -->
8 Conclusion

<!-- b000342 | heading | pages [18] -->
8.1 Strengths

<!-- b000343 | prose | pages [18] -->
• Applies widely The differential equation model and the linear programming model can be easily modiﬁed to accommodate to various situation.

<!-- b000344 | prose | pages [18] -->
• The result is a global optimum solution Our differential equation model consider the time value of the delayed passengers and the construction cost of the area at the same time which can result in a global optimum solution.

<!-- b000345 | prose | pages [18] -->
• Good ﬂexibility According to our analysis, our model can always ﬁnd the optimum solution under various kinds of conditions.

<!-- b000346 | prose | pages [18, 19] -->
• Technical supporting We use many theory and methods to support our work. And each one of them is used reasonably and properly.

<!-- b000347 | furniture | pages [19] -->
Team # 68303

<!-- b000348 | furniture | pages [19] -->
Page 18 of 20

<!-- b000350 | heading | pages [19] -->
8.2 Weakness

<!-- b000351 | prose | pages [19] -->
• Inaccuracy When considering the value of parameters, we obtain them through a lot of differ- ent research papers which may inﬂuence the result of our model.

<!-- b000352 | prose | pages [19] -->
• Simplifying assumptions To simplify the model, we make a few assumptions which may affect the result of our model.

<!-- b000353 | prose | pages [19] -->
• Lack of data For the lack of data, we have to simulate the models abstracted from the reality to obtain the data we need which may be different from the real data.

<!-- b000354 | heading | pages [19] -->
References

<!-- b000355 | references | pages [19] -->
[1] GRIGG

<!-- b000356 | references | pages [19] -->
G

<!-- b000357 | references | pages [19] -->
M.

<!-- b000358 | references | pages [19] -->
THE

<!-- b000359 | references | pages [19] -->
HIGHWAY

<!-- b000360 | references | pages [19] -->
CAPACITY

<!-- b000361 | references | pages [19] -->
MANUAL[J].

<!-- b000362 | references | pages [19] -->
ITE

<!-- b000363 | references | pages [19] -->
JOURNAL-

<!-- b000364 | references | pages [19] -->
INSTITUTE OF TRANSPORTATION ENGINEERS, 1991, 61(1): 5-5.

<!-- b000365 | references | pages [19] -->
[2] Lee W P, Osman M A, Talib A Z, et al. Dynamic trafﬁc simulation for trafﬁc con-

<!-- b000366 | references | pages [19] -->
gestion problem using an enhanced algorithm[J]. International Journal of Math-

<!-- b000367 | references | pages [19] -->
ematical, Computational, Physical, Electrical and Computer Engineering (World

<!-- b000368 | references | pages [19] -->
Academy of Science, Engineering and Technology), 2008, 2(9): 277-284.

<!-- b000369 | references | pages [19] -->
[3] Jing Li. Japan highway design essentials[J]. 1991.

<!-- b000370 | references | pages [19] -->
[4] Manual H C. Highway capacity manual[J]. Washington, DC, 2000. Addison-Wesley

<!-- b000371 | references | pages [19] -->
Publishing Company, 1986.

<!-- b000372 | references | pages [19] -->
[5] Li Su. Study on Design of expressway toll station[D]. Changan University, 2012.

<!-- b000373 | references | pages [19] -->
[6] P.T.harker. Alternative methods of questioning in the analytic hierarchy process,

<!-- b000374 | references | pages [19] -->
Math modeling,Vol.9,No.3-5(1987)

<!-- b000375 | references | pages [19] -->
[7] Honglei Ru. Study on Inﬂuencing Factors of urban road capacity[D]. Tongji Univer-

<!-- b000376 | references | pages [19] -->
sity, 2008.

<!-- b000377 | references | pages [19] -->
[8] Chandler A, Mian M, Baliga P. The Booth Tolls for Thee[J]. UMAPJournal, 2005: 283.

<!-- b000378 | references | pages [19] -->
[9] Guizzo E. How googles self-driving car works[J]. IEEE Spectrum Online, October,

<!-- b000379 | references | pages [19] -->
2011, 18.

<!-- b000380 | furniture | pages [20] -->
Team # 68303

<!-- b000381 | furniture | pages [20] -->
Page 19 of 20

<!-- b000382 | references | pages [20] -->
Dear New Jersey Turnpike Authority,

<!-- b000383 | references | pages [20] -->
We are here to help you with determining if there are better solutions of the merging

<!-- b000384 | references | pages [20] -->
area following the toll barrier than any in common use. This letter explains our optimum

<!-- b000385 | references | pages [20] -->
solution model, and provide a series of suggestions under various circumstances.

<!-- b000386 | references | pages [20] -->
As we all known, the main purpose of researching the problem of merge after toll is

<!-- b000387 | references | pages [20] -->
to control the cost and to improve the throughput and the safety of the area as much as

<!-- b000388 | references | pages [20] -->
possible at the same time. Thus our model is built based on these three factors.

<!-- b000389 | references | pages [20] -->
Firstly, before proposing a better solution, we should research the advantages and

<!-- b000390 | references | pages [20] -->
the disadvantages of the existing models. We collect the characteristics of the existing

<!-- b000391 | references | pages [20] -->
models according to the shape of the area, the size of the area and the merging pattern

<!-- b000392 | references | pages [20] -->
of the area and classify them into eight kinds.

<!-- b000393 | references | pages [20] -->
Secondly, we build a simulation model to obtain the important parameters of the

<!-- b000394 | references | pages [20] -->
corresponding model, such as trafﬁc ﬂow, average queuing time, average time of delay,

<!-- b000395 | references | pages [20] -->
etc.

<!-- b000396 | references | pages [20] -->
Thirdly, we build a comprehensive evaluation model based on PCA to evaluate the

<!-- b000397 | references | pages [20] -->
eight models listed above. From the result of evaluation, we get the rank value of each

<!-- b000398 | references | pages [20] -->
model. In this way, we get the best model which is in the shape of isosceles trapezoid

<!-- b000399 | references | pages [20] -->
with stipulated merging pattern and medium size of the area among the eight existing

<!-- b000400 | references | pages [20] -->
models.

<!-- b000401 | references | pages [20] -->
On the basis of existing models, we propose a better solution. When considering the

<!-- b000402 | references | pages [20] -->
cost of the area, we promote the deﬁnition of the cost, the total cost is not just the cost of

<!-- b000403 | references | pages [20] -->
road construction, but also includes the value of queuing time and the operating cost of

<!-- b000404 | references | pages [20] -->
the tollbooths. We can get the optimum number of tollbooths and the optimum height

<!-- b000405 | references | pages [20] -->
of the trapezoid area while minimizing the total cost of the area.

<!-- b000406 | references | pages [20] -->
In reality, when the vehicles entering the area following the toll barrier, they always

<!-- b000407 | references | pages [20] -->
want to get into the travel lanes as soon as possible. Our linear programming model

<!-- b000408 | references | pages [20] -->
which determine the merging pattern of the area is based on this principle–let the ve-

<!-- b000409 | references | pages [20] -->
hicles ﬁnd the shortest path leave the area following the toll barrier. In this way, we

<!-- b000410 | references | pages [20] -->
reduce the number of merging points of the area, increase the throughput of the area

<!-- b000411 | references | pages [20] -->
and promote the accident prevention of the area.

<!-- b000412 | references | pages [20] -->
In accordance with the above research ideas, we develop a better design of the area

<!-- b000413 | references | pages [20] -->
following the toll barrier.

<!-- b000414 | references | pages [20] -->
Of course, a good design can not only work efﬁciently under normal circumstances,

<!-- b000415 | references | pages [20] -->
but also can keep running under some speciﬁc extreme circumstances. To this end, we

<!-- b000416 | references | pages [20] -->
perform several analysis to test our model.

<!-- b000417 | references | pages [20] -->
The ﬁrst one is to change the value of trafﬁc ﬂow: at the small trafﬁc ﬂow, our model

<!-- b000418 | references | pages [20] -->
can run smoothly, but the number of tollbooths may exceeds the demand. In this situa-

<!-- b000419 | references | pages [20] -->
tion ,we can close several tollbooths appropriately to reduce the operating costs. When it

<!-- b000420 | references | pages [20] -->
comes to a heavy trafﬁc ﬂow, our model can still operating well while few of congestion

<!-- b000421 | references | pages [20] -->
may happen. We can adjust our merging pattern to divert the trafﬁc.

<!-- b000422 | references | pages [20] -->
The second aspect is the situation when more autonomous(self-driving) vehicles are

<!-- b000423 | references | pages [20] -->
added to the trafﬁc ﬂow. The autonomous vehicle is controlled by the computer, which

<!-- b000424 | references | pages [20] -->
can adjust its strategy on time by choosing safer paths.The adopt of autonomous vehicles

<!-- b000425 | references | pages [20] -->
may reduce the number of trafﬁc accidents caused by human beings, and improve the

<!-- b000426 | furniture | pages [21] -->
Team # 68303

<!-- b000427 | furniture | pages [21] -->
Page 20 of 20

<!-- b000428 | references | pages [21] -->
safety of the area. Due to the safety and the efﬁciency of autonomous vehicles, we do

<!-- b000429 | references | pages [21] -->
not have to stipulate the merge pattern of the area following the toll barrier which can

<!-- b000430 | references | pages [21] -->
bring the advantages of autonomous vehicles to the full play.

<!-- b000431 | references | pages [21] -->
Considering the proportions of different kinds of tollbooths which indicated by the

<!-- b000432 | references | pages [21] -->
service time, our model can be modiﬁed by adjusting the merging pattern to accommo-

<!-- b000433 | references | pages [21] -->
date to the speciﬁc situation in which we cite two speciﬁc examples in our paper.

<!-- b000434 | references | pages [21] -->
In summary, our model has developed a way to ﬁnd the optimum solution of the

<!-- b000435 | references | pages [21] -->
area following the toll barrier. Our model is feasible and reasonable and can be adjusted

<!-- b000436 | references | pages [21] -->
to various kinds of situation in reality. Although we have proposed a better solution,

<!-- b000437 | references | pages [21] -->
we suggest that the authority should take overall account of the reality according to the

<!-- b000438 | references | pages [21] -->
factors we listed in our paper. To know how the our model run in details,please check

<!-- b000439 | references | pages [21] -->
our paper.

<!-- b000440 | references | pages [21] -->
Wish our optimal investment strategy can inspire you at the key point of solving

<!-- b000441 | references | pages [21] -->
the probable solution of merging after toll.We are very eager to hear your opinion on

<!-- b000442 | references | pages [21] -->
our performance and to have more communication about it.We look forward to hearing

<!-- b000443 | references | pages [21] -->
from you.

<!-- b000444 | references | pages [21] -->
Yours sincerely,

<!-- b000445 | references | pages [21] -->
A group of modelers who are enthusiastic about mathematical modeling.

<!-- b000446 | references | pages [21] -->
24/1/2017
