# P-C-2017-55585-278f2f68

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
55585

<!-- b000005 | prose | pages [1] -->
F1

<!-- b000006 | prose | pages [1] -->
T1

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

<!-- b000012 | title | pages [1] -->
C

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | title | pages [1] -->
Highway Trafﬁc Flow Model with Self-Driving Vehicles

<!-- b000018 | title | pages [1] -->
Based on Cellular Automata

<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
With the increasing lack of transportation capacity and the growth of self-driving vehicle(SDV) industry, an evaluation should be made to ﬁnd out the inﬂuence on trafﬁc when more and more non- self-driving-vehicles(NSDV) are replaced by SDVs while few studies were done on the interactions between SDVs and NSDVs and the cooperations among SDVs themselves.

<!-- b000021 | prose | pages [1] -->
We choose cellular automata(CA) model to evaluate this problem after a careful study and com- parison of different kinds of trafﬁc ﬂow models in the past few decades. In order to take the re- lationships of SDVs and NSDVs into consideration, we improve the traditional CA model which emphasizes on status and rules of changes, by redesigning these two factors. Before building a CA model, discretization should be done ﬁrst. By learning the average length, speed, acceleration of running vehicles on highway and the reaction time of human beings, the size of a cell and the time length of a turn are decided. After making assumptions and simplifying the problem, two inter- related CA models are covered in this paper to simulate the changeable trafﬁc: the Following Model and the Multilane Trafﬁc Model.

<!-- b000022 | prose | pages [1] -->
The Following Model is designed to simulate how a vehicle follows another in a single lane. Rules for NSDVs and SDVs are different from each other: For an NSDV, the driver’s reaction time and psychological characteristics are considered; For an SDV, the rules are based on the sharing of information with other SDVs and the joint decision making. Speciﬁcally, we create a new conception ’SDV-Train’ to simulate the cooperations among SDVs.

<!-- b000023 | prose | pages [1] -->
The Multilane Trafﬁc Model is based on the Following Model. In this model, besides following, we try to ﬁnd out when and how should a vehicle change a lane. Two main parameters are involved in this model: Lane-Changing Motivation (LCM) and Lane-Changing Secuirty (LCS). LCM depends on whether changing a lane can increase the speed and LCS shows the whether it is safe when lane- changing. Only when both LCM and LCS are satisﬁed, may a vehicle change its lane. Details of these two parameters vary between SDVs and NSDVs considering the huge difference between an automatic control system and a human driver. A two-step turning method is specially made for this model in correspondence with the real world.

<!-- b000024 | prose | pages [1] -->
After building and making improvements to the model, we write programs to simulate it and get huge volumes of data. We analyze and visualize the data using Matlab, showing strong correlations among three parameters: the average speed, the trafﬁc ﬂow and the percentage of the SDVs running on the road. The increasing number of SDVs has great inﬂuence on the trafﬁc ﬂow which almost triples when all the NSDVs are replaced by SDVs. Also, we ﬁnd that a special lane for SDVs (SDV Lane) should be built when the percentage reaches a certain level.

<!-- b000025 | prose | pages [1] -->
Based on the correlations we get in analysis, we apply our model to the Great Seattle area by comparing the real data and the data we gain from simulations. We ﬁnd that the lack of trafﬁc capacity in this area is huge. Although adding SDVs to the street can reduce this lack, it is not a cure. We believe a comprehensive method should be applied in this area including setting a SDV Lane and broadening highways in some particularly narrow parts.

<!-- b000026 | keywords | pages [1] -->
Keywords: Trafﬁc Flow Model; Self-Driving Vehicle; Cellular Automata

<!-- b000027 | furniture | pages [2] -->
Team # 55585

<!-- b000028 | heading | pages [2] -->
Contents

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | heading | pages [2] -->
Introduction

<!-- b000031 | prose | pages [2] -->
1

<!-- b000032 | heading | pages [2] -->
Simpliﬁcations and Assumptions of the Problem

<!-- b000033 | prose | pages [2] -->
2 1 Features of the Highway . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 1 Features of Vehicles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 2 Special Features of NSDVs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 3 Special Features of SDVs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4

<!-- b000034 | prose | pages [2] -->
3

<!-- b000035 | heading | pages [2] -->
Choice and Basic Settings of the Model

<!-- b000036 | prose | pages [2] -->
3

<!-- b000037 | prose | pages [2] -->
3 Choice of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 3 Discretization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 Basic Settings

<!-- b000038 | prose | pages [2] -->
4

<!-- b000039 | heading | pages [2] -->
Details of the Model

<!-- b000040 | prose | pages [2] -->
4

<!-- b000041 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Following Model 4 Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 5 Following Rules for NSDVs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 6 Following Rules for SDVs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.3 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Multilane Trafﬁc Model 9 Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 4.2.2 General Rules of Changing Lanes 9 . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
10 Lane-Changing Rules for NSDVs . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.3 10 Lane-Changing Rules for SDVs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4 12

<!-- b000043 | heading | pages [2] -->
Analysis of the Results Obtained from the Model Simulation

<!-- b000044 | prose | pages [2] -->
5 13 Results of Following Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 13 Results of the Multilane Trafﬁc Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 15 SDV Lane . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000045 | prose | pages [2] -->
6

<!-- b000046 | heading | pages [2] -->
Appliance of the Model

<!-- b000047 | prose | pages [2] -->
7

<!-- b000048 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000049 | prose | pages [2] -->
16

<!-- b000050 | prose | pages [2] -->
17

<!-- b000051 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 Choice of the Parameters in LCP 18 Different Speed Limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000052 | prose | pages [2] -->
8

<!-- b000053 | heading | pages [2] -->
Conclusions

<!-- b000054 | prose | pages [2] -->
9

<!-- b000055 | heading | pages [2] -->
Strengths and weaknesses

<!-- b000056 | prose | pages [2] -->
18

<!-- b000057 | prose | pages [2] -->
19

<!-- b000058 | prose | pages [2] -->
19 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 Weaknesses

<!-- b000059 | heading | pages [2] -->
10 A Letter

<!-- b000060 | heading | pages [2] -->
Appendices

<!-- b000061 | prose | pages [2] -->
19

<!-- b000062 | prose | pages [2] -->
20

<!-- b000063 | prose | pages [2] -->
22

<!-- b000064 | furniture | pages [3] -->
Team # 55585

<!-- b000065 | furniture | pages [3] -->
Page 1 of 34

<!-- b000066 | prose | pages [3] -->
1

<!-- b000067 | heading | pages [3] -->
Introduction

<!-- b000068 | prose | pages [3] -->
Built in the 20th century, many highways were designed to meet the transportation demands at that time. With the boom of population, urbanization and economy, the need of transportation grows rapidly in the new century. Nowadays, highways in the Great Seattle area can no longer meet people’s need and trafﬁc delays can be seen everywhere during peak hours. However, at this time building more roads or adding lanes in this area is extremely difﬁcult and expensive. In order to increase the capacity of highways without increasing the number of lanes or roads, allowing self- driving vehicles(SDVs) to run on the road should be taken into consideration. A model is needed to evaluate SDVs’ inﬂuence on the trafﬁc ﬂow.

<!-- b000069 | prose | pages [3] -->
We proposed to decompose this problem into three parts:

<!-- b000070 | prose | pages [3] -->
• Build a model that can simulate the trafﬁc ﬂow in different percentage of SDVs and non-self- driving vehicles (NSDVs), number of lanes and trafﬁc volume.

<!-- b000071 | prose | pages [3] -->
• Use the model to ﬁnd the equilibria or tipping points and apply the model to the provided data.

<!-- b000072 | prose | pages [3] -->
• Based on the data, decide whether there are some conditions where lanes should be dedicated to SDVs and how the policy should be changed.

<!-- b000073 | prose | pages [3] -->
Firstly, we use cellular automata(CA) to simulate the trafﬁc ﬂow when there is only one lane. This model is called the Following Model. In our model, we rule the way each cell behaves by simplifying the behaviors of vehicles in real life, like when a vehicle will slow down or speed up. We use different rules for SDVs and NSDVs in our model to simulate the cooperations among SDVs, interactions between SDVs and NSDVs, unpredictability of human-beings and other factors.

<!-- b000074 | prose | pages [3] -->
Based on the Following Model we built, we put separate parrel lanes together and add new rules to simulate the trafﬁc ﬂow on a multilane highway. This is the Multilane Trafﬁc Model. After simplifying the behaviors of real vehicles’ changing lanes, we make rules on when and how a cell move across lanes. Both the motivation and the safety concern are considered. Furthermore, we make special rules to simulate human behaviors and cooperations among SDVs including the form of a chain of SDVs called the SDV-Train.

<!-- b000075 | prose | pages [3] -->
Secondly, using real-life parameters, we run the CA model and get a large number of data. By analyzing the data, we ﬁnd several interesting features of the mixed trafﬁc ﬂow. The correlations among the average speed, the trafﬁc ﬂow and the percentage of SDVs are strong. These three pa- rameters inﬂuence each other in their own way. When there are many lanes, the situation changes and more interesting phenomena are found including the relationships between the efﬁciency of each line and the percentage of SDVs. After comparison, we ﬁnd out when and how to build a special lane for SDVs (SDV Lane).

<!-- b000076 | prose | pages [3] -->
Thirdly, we compared our data with real data in the Great Seattle area. We ﬁnd that there is indeed a great lack of trafﬁc capacity in this area. After changing NSDVs to SDVs, the trafﬁc capacity increases and even triples but we believe the trafﬁc situation in this area is still not abundant. More methods including broaden a few parts of the current highway and setting a SDV Lane should be taken into consideration.

<!-- b000077 | prose | pages [3] -->
2

<!-- b000078 | heading | pages [3] -->
Simpliﬁcations and Assumptions of the Problem

<!-- b000079 | prose | pages [3] -->
2.1 Features of the Highway

<!-- b000080 | heading | pages [3] -->
1. Straight Road

<!-- b000081 | prose | pages [3] -->
A highway in this model should be straight or its degree of curvature can be ignored [1]. A vehicle’s speed and other conditions does not change because of the shape of the road.

<!-- b000082 | furniture | pages [4] -->
Team # 55585

<!-- b000083 | furniture | pages [4] -->
Page 2 of 34

<!-- b000084 | heading | pages [4] -->
2. The number of lanes should remain constant for a long period.

<!-- b000085 | heading | pages [4] -->
3. The highway is in good condition and the trafﬁc ﬂow is not affected by the rough road.

<!-- b000086 | heading | pages [4] -->
4. No pedestrian, animal or any form of obstacle can be found on the highway so the trafﬁc ﬂow

<!-- b000087 | prose | pages [4] -->
would not be blocked.

<!-- b000088 | heading | pages [4] -->
5. Weather changes and illumination difference during different time is not taken into consid-

<!-- b000089 | prose | pages [4] -->
eration.

<!-- b000090 | heading | pages [4] -->
6. Rules for SDV Lane

<!-- b000091 | prose | pages [4] -->
• If a SDV Lane is set, all SDVs should run in this line while none of the NSDVs may run in it.

<!-- b000092 | prose | pages [4] -->
• Only one SDV Lane can be set in our model considering the width of the highway is limited.

<!-- b000093 | prose | pages [4] -->
• The SDV Lane will be placed on the edge of the road to prevent a separation of lanes for NSDVs.

<!-- b000094 | prose | pages [4] -->
7. The width of each lane is 12 feet.

<!-- b000095 | prose | pages [4] -->
8. The speed limit of all highways is 60mph.

<!-- b000096 | prose | pages [4] -->
2.2 Features of Vehicles

<!-- b000097 | heading | pages [4] -->
1. In this model, only average length, speed, acceleration and other features of vehicles are used.

<!-- b000098 | prose | pages [4] -->
Although there is a great diversity among different vehicles, this difference can be ignored and the result of the model would not be greatly affected.

<!-- b000099 | heading | pages [4] -->
2. All vehicles obey trafﬁc laws. The violation of trafﬁc laws does great harm to the driver’s

<!-- b000100 | prose | pages [4] -->
health, public security as well as the speed of total trafﬁc ﬂow. As a result, these circumstances would not occur in our model:

<!-- b000101 | prose | pages [4] -->
• a vehicle exceeds the speed limit;

<!-- b000102 | prose | pages [4] -->
• a vehicle stops for no reason;

<!-- b000103 | prose | pages [4] -->
• a vehicle runs in an emergency lane or on the shoulder for no reason;

<!-- b000104 | prose | pages [4] -->
• a vehicle changes its lane but

<!-- b000105 | prose | pages [4] -->
– its turning light is not turned on in advance; – the vehicle behind it shows its intention to change the lane;

<!-- b000106 | prose | pages [4] -->
• two vehicles run side by side in one lane;

<!-- b000107 | prose | pages [4] -->
• the distance between two vehicles in the same lane is too short.

<!-- b000108 | heading | pages [4] -->
3. Trafﬁc accident is not taken into consideration. Details of its inﬂuence will be discussed in

<!-- b000109 | prose | pages [4] -->
Section 9.2.

<!-- b000110 | heading | pages [4] -->
4. Average daily trafﬁc ﬂow is used in this model. Trafﬁc ﬂow varies in different days, so an

<!-- b000111 | prose | pages [4] -->
average level should be used to simplify this model.

<!-- b000112 | heading | pages [4] -->
5. Horn is not used in our model. On highway, the inﬂuence of a horn is limited because the

<!-- b000113 | prose | pages [4] -->
distance between two vehicles is too long for a complicated sound signal to be heard and understood clearly.

<!-- b000114 | furniture | pages [5] -->
Team # 55585

<!-- b000115 | furniture | pages [5] -->
Page 3 of 34

<!-- b000116 | prose | pages [5] -->
2.3 Special Features of NSDVs

<!-- b000117 | heading | pages [5] -->
1. Uncertainty of the estimation of distance and speed

<!-- b000118 | prose | pages [5] -->
Compared with computer systems, human drivers are more likely to make mistakes, especially when it comes to the evaluation of distance and speed. Therefore, human drivers tend to slow down the vehicle and choose not to change a lane when they cannot estimate the distance clearly even when other vehicles are out of the minimum safe distance.

<!-- b000119 | heading | pages [5] -->
2. Longer reaction time

<!-- b000120 | prose | pages [5] -->
Human drivers need more time to decelerate and start their vehicle compared with self-driving ones especially on the highway [2].

<!-- b000121 | prose | pages [5] -->
2.4 Special Features of SDVs

<!-- b000122 | heading | pages [5] -->
1. Short reaction time

<!-- b000123 | prose | pages [5] -->
SDVs are controlled by computer systems which run fast and can stay active for the whole time. With modern technology, it is easy for an SDV to perceive the outside world and make reactions accordingly in a short time.

<!-- b000124 | heading | pages [5] -->
2. Cooperations among SDVs

<!-- b000125 | prose | pages [5] -->
The system of an SDV is connected to the Internet, therefore information of all the SDVs on a road is shared. With more information, a network decision-making system can be built which is mentioned in previous studies [3].

<!-- b000126 | heading | pages [5] -->
3. Mature technology

<!-- b000127 | prose | pages [5] -->
The technology of self-driving is mature enough and no malfunction of SDVs’ guiding, driving and decision-making system is taken into consideration in this model. If an accident does happen to an SDV’s system, this SDV should be labeled as an NSDV.

<!-- b000128 | heading | pages [5] -->
4. Interactions between an NSDV and an SDV

<!-- b000129 | prose | pages [5] -->
As discussed in Section 3, for a human driver, there is no difference between an SDV and an NSDV that he or she encounters on the street, for SDVs would make less mistakes than NSDVs and would not cause more trouble to human drivers.

<!-- b000130 | prose | pages [5] -->
3

<!-- b000131 | heading | pages [5] -->
Choice and Basic Settings of the Model

<!-- b000132 | prose | pages [5] -->
3.1

<!-- b000133 | heading | pages [5] -->
Choice of the Model

<!-- b000134 | prose | pages [5] -->
In the past few decades, with the development of transportation, a great variety of models simu- lating the trafﬁc were built and improved, among which Continuous Medium model and CA model are the most popular ones. Lighthill and Whitham ﬁrstly put forward the concept of continuous medium model, while shortly afterwards Richards also put forward it independently, therefore it is also named LWR model [4]. LWR model mainly focuses on the macroscopic homogeneity and sta- bility of the trafﬁc ﬂow. However, in this problem, the cooperations between SDVs and the reactions between an SDV and an NSDV must be further discussed, which makes it hard for us to adapt the LWR model, because LWR model neglects the interactions between different particles in the ﬂow. After careful comparison, we ﬁnd that traditional CA model with modiﬁcations can be used in this problem.

<!-- b000135 | prose | pages [5] -->
In real life, the action of a vehicle taken by both human drivers and computer systems depends on the status of the vehicle itself and the surrounding trafﬁc, which is similar to the rules of CA, which is originally discovered in the 1940s by Stanislaw Ulam and John von Neumann [5]. The basic idea of CA is that it starts with a set of cells with status. A simple set of rules are created that the

<!-- b000136 | furniture | pages [6] -->
Team # 55585

<!-- b000137 | furniture | pages [6] -->
Page 4 of 34

<!-- b000138 | prose | pages [6] -->
status are updated depending on the status of the cell and its neighbors. With multiple iterations, CA models can simulate the movement of complex objects. Changes are made to the status and the rules of the original CA model in order, ensuring that this model can work for a mixture of SDVs and NSDVs. In order to make a CA model, discretization should be done ﬁrst to almost all variables.

<!-- b000139 | prose | pages [6] -->
3.2 Discretization

<!-- b000140 | prose | pages [6] -->
In our CA models, each vehicle is regarded as a cell with its own status. Besides, each lane is also divided into cells that can contain the vehicles while time is divided into small units(turns).

<!-- b000141 | heading | pages [6] -->
1. Size of a cell

<!-- b000142 | prose | pages [6] -->
The average length of vehicle in U.S. is a bit longer than 4 meters. As every cell represents a vehicle, the length of the cell should be the same as the average length. To simplify the calculation, we use

<!-- b000143 | prose | pages [6] -->
1cell = 4m (3.1)

<!-- b000144 | heading | pages [6] -->
2. Time unit

<!-- b000145 | prose | pages [6] -->
As the results of Triggs, T. J. and Harris, W. G’s work shows, the average reaction time for drivers is around 1.5 seconds [2]. In one turn of the CA model, a vehicle makes one action, so 1.5 seconds is a good choice for our CA model’s time unit.

<!-- b000146 | prose | pages [6] -->
1turn = 1.5s (3.2)

<!-- b000147 | prose | pages [6] -->
3.3 Basic Settings

<!-- b000148 | heading | pages [6] -->
1. Speed

<!-- b000149 | prose | pages [6] -->
The speed limit of road is 60mph, which is 10cell per turn, using Eqn. (3.1) and Eqn. (3.2). Because CA model is discretized, the speed is regarded as a natural number from 0 to 10 in our model.

<!-- b000150 | heading | pages [6] -->
2. Acceleration

<!-- b000151 | prose | pages [6] -->
According to the assumption , the speed of a vehicle should change step by step. In our model, the speed can only change 1cell in a turn. Use Eqn. (3.1) and Eqn. (3.2), the acceleration of a vehicle is 2.67m/s2, which is in line with daily experience.

<!-- b000152 | heading | pages [6] -->
3. Minimum Safe Following Distance(MinSFD)

<!-- b000153 | prose | pages [6] -->
A vehicle should not get too close to the vehicle ahead to prevent accident when running on a high way. Minimum Safe Following Distance(MinSFD) is designed to make sure that a normal vehicle running at a certain speed can stop before collision.

<!-- b000154 | prose | pages [6] -->
4

<!-- b000155 | heading | pages [6] -->
Details of the Model

<!-- b000156 | prose | pages [6] -->
In our CA models, rules are made to simulate vehicles’ movement. Among all kinds of move- ments, two types of vehicle’s actions are the most important ones: following and lane-changing. The Following Model and the Multilane Trafﬁc Model are made to simulate these two types of actions.

<!-- b000157 | prose | pages [6] -->
4.1

<!-- b000158 | heading | pages [6] -->
Following Model

<!-- b000159 | prose | pages [6] -->
The Following Model simulates the ﬂow of vehicles in a single lane on the highway. Large quan- tities of single-lane trafﬁc ﬂow models have been developed, the most famous one of which is the NaSch(NS) model. Kai Nagel and Michael Schreckenberg built this CA model for highway trafﬁc in 1992 [6]. Their model’s simulations show a transition from laminar trafﬁc ﬂow to start-stop waves

<!-- b000160 | furniture | pages [7] -->
Team # 55585

<!-- b000161 | furniture | pages [7] -->
Page 5 of 34

<!-- b000162 | prose | pages [7] -->
with increasing vehicle density. In real life, SDVs’ behavior is different from the non-self-driving ones, so our modiﬁcations for the NaSch model are mainly focused on the SDVs.

<!-- b000163 | prose | pages [7] -->
4.1.1 Variables

<!-- b000164 | caption | pages [7] -->
Table 1: Main Variables Used in the Following Model

<!-- b000165 | prose | pages [7] -->
Variable Deﬁnation Unit

<!-- b000166 | prose | pages [7] -->
Distance between vehicle No. i and the start point di cell Distance between vehicle No. i and the vehicle ahead of it ∆di vi Speed of vehicle No.i cell cell/time step Whether vehicle No.i is accelerating or not ai unitless Status of the back light of vehicle No.i bi ti Type of vehicle No.i

<!-- b000167 | prose | pages [7] -->
MinSFD between two vehicles Dmin(v) when the latter one’s speed is v

<!-- b000168 | prose | pages [7] -->
unitless unitless

<!-- b000169 | prose | pages [7] -->
cell

<!-- b000170 | prose | pages [7] -->
Maximum distance between two vehicles when the latter one’s Dmax(v) cell speed is v and the action of the former one can be ignored

<!-- b000171 | prose | pages [7] -->
P1,i Possibility of a human driver to decelerate out of caution

<!-- b000172 | prose | pages [7] -->
vA A

<!-- b000173 | prose | pages [7] -->
vA A

<!-- b000174 | prose | pages [7] -->
vC

<!-- b000175 | prose | pages [7] -->
C

<!-- b000176 | prose | pages [7] -->
SDV NSDV

<!-- b000177 | prose | pages [7] -->
unitless

<!-- b000178 | prose | pages [7] -->
ΔdA

<!-- b000179 | prose | pages [7] -->
vB

<!-- b000180 | prose | pages [7] -->
B

<!-- b000181 | prose | pages [7] -->
vD

<!-- b000182 | prose | pages [7] -->
D

<!-- b000183 | prose | pages [7] -->
Back Light On

<!-- b000184 | prose | pages [7] -->
Back Light Off

<!-- b000185 | prose | pages [7] -->
bi=1

<!-- b000186 | prose | pages [7] -->
bi=0

<!-- b000187 | caption | pages [7] -->
Figure 1: Diagram of Main Variables Used in the Following Model

<!-- b000188 | prose | pages [7] -->
Main variables used in the Following Model are shown in Tab. 4.1.1 and Fig. 1. Speciﬁcally, Eqn. (4.3) shows the functions for the status of the back light and the vehicle type separately:

<!-- b000189 | prose | pages [7] -->
{

<!-- b000190 | prose | pages [7] -->
the back light of vehicle No. i is off 0,

<!-- b000191 | prose | pages [7] -->
bi =

<!-- b000192 | prose | pages [7] -->
the back light of vehicle No.i is on 1,

<!-- b000193 | prose | pages [7] -->
{

<!-- b000194 | prose | pages [7] -->
(4.3)

<!-- b000195 | prose | pages [7] -->
vehicle No. i is an NSDV 0,

<!-- b000196 | prose | pages [7] -->
ti =

<!-- b000197 | prose | pages [7] -->
vehicle No.i is an SDV 1,

<!-- b000198 | prose | pages [7] -->
For an NSDV, no light signal shows whether it is accelerating or not, which parameter ai indicates. However, this information is shared among self-driving ones, which is what Eqn. (4.4) shows:

<!-- b000199 | prose | pages [7] -->
{

<!-- b000200 | prose | pages [7] -->
vehicle No.i is not accelerating 0,

<!-- b000201 | prose | pages [7] -->
ai =

<!-- b000202 | prose | pages [7] -->
(4.4) vehicle No.i is accelerating 1,

<!-- b000203 | furniture | pages [8] -->
Team # 55585

<!-- b000204 | prose | pages [8] -->
4.1.2 Following Rules for NSDVs

<!-- b000205 | prose | pages [8] -->
• Deceleration

<!-- b000206 | furniture | pages [8] -->
Page 6 of 34

<!-- b000207 | prose | pages [8] -->
As we discussed in part 1 and part 2 of Section 2.4, human driver need more time to react and they sometimes choose to slow down to maintain a longer following distance out of caution. In this Following Model, if vehicle No.i is Non-Self-Driving, a possibility function P1,i is made for it to simulate the two factors mentioned above. For an NSDV A, Eqn. (4.5) shows the function, in which B represents the ﬁrst vehicle that is in front of A.

<!-- b000208 | prose | pages [8] -->
 

<!-- b000209 | prose | pages [8] -->
bB = 1 ∧∆dA > Dmin(vA) ∧∆dA < Dmax(vA) P11,

<!-- b000210 | prose | pages [8] -->
   

<!-- b000211 | prose | pages [8] -->
bB = 0 ∧∆dA > Dmin(vA) ∧∆dA < Dmax(vA) P12,

<!-- b000212 | prose | pages [8] -->
P1,A =

<!-- b000213 | prose | pages [8] -->


<!-- b000214 | prose | pages [8] -->
P13, vA = 0

<!-- b000215 | prose | pages [8] -->
   

<!-- b000216 | prose | pages [8] -->
0, other cases

<!-- b000217 | prose | pages [8] -->
(4.5)

<!-- b000218 | prose | pages [8] -->
In calculation, we use the results got from pervious works [7] [8]:

<!-- b000219 | prose | pages [8] -->
P11 = 0.94, P12 = 0.50, P13 = 0.20 (4.6)

<!-- b000220 | prose | pages [8] -->
In short, there is a rate for NSDVs to decelerate under certain circumstances. As shown in Lane 1 in Fig. 2, for an NSDV A, every turn a random number R between 0 and 1 is given in the Following Model, and:

<!-- b000221 | prose | pages [8] -->
P1,A ⩾R ⇒vA = vA −1, bA = 1

<!-- b000222 | prose | pages [8] -->
Besides this effect, if there is another vehicle within vehicle A’s MinSFD, A has to decelerate and turn its back light on. That is:

<!-- b000223 | prose | pages [8] -->
∆dA ⩽Dmin(vA) ⇒vA = vA −1, bA = 1

<!-- b000224 | prose | pages [8] -->
And this is Lane 2 in Fig. 2.

<!-- b000225 | prose | pages [8] -->
Dmax(vA)

<!-- b000226 | prose | pages [8] -->
Dmin(vA)

<!-- b000227 | prose | pages [8] -->
vA

<!-- b000228 | prose | pages [8] -->
Lane 1

<!-- b000229 | prose | pages [8] -->
A

<!-- b000230 | prose | pages [8] -->
vA

<!-- b000231 | prose | pages [8] -->
Lane 2

<!-- b000232 | prose | pages [8] -->
A B

<!-- b000233 | prose | pages [8] -->
vA

<!-- b000234 | prose | pages [8] -->
Lane 3

<!-- b000235 | prose | pages [8] -->
A

<!-- b000236 | prose | pages [8] -->
vA

<!-- b000237 | prose | pages [8] -->
Lane 4

<!-- b000238 | prose | pages [8] -->
A

<!-- b000239 | prose | pages [8] -->
vA

<!-- b000240 | prose | pages [8] -->
Lane 5

<!-- b000241 | prose | pages [8] -->
A

<!-- b000242 | prose | pages [8] -->
Deceleration B B

<!-- b000243 | prose | pages [8] -->
(P1,A R)

<!-- b000244 | prose | pages [8] -->
Deceleration

<!-- b000245 | prose | pages [8] -->
Acceleration B

<!-- b000246 | prose | pages [8] -->
Acceleration B

<!-- b000247 | prose | pages [8] -->
Hold B B (P1,A R)

<!-- b000248 | caption | pages [8] -->
Figure 2: Following Rules for NSDVs

<!-- b000249 | prose | pages [8] -->
• Acceleration

<!-- b000250 | prose | pages [8] -->
If NSDV A does not decelerate because of PA, and vehicle B is

<!-- b000251 | prose | pages [8] -->
– far away, or

<!-- b000252 | prose | pages [8] -->
– not decelerating and out of A’s MinSFD

<!-- b000253 | furniture | pages [9] -->
Team # 55585

<!-- b000254 | furniture | pages [9] -->
Page 7 of 34

<!-- b000255 | prose | pages [9] -->
then A will accelerate, which are shown separately in Lane 3 and Lane 4 in Fig. 2. That is:

<!-- b000256 | prose | pages [9] -->
(

<!-- b000257 | prose | pages [9] -->
))

<!-- b000258 | prose | pages [9] -->
(

<!-- b000259 | prose | pages [9] -->
∆dA > Dmax(vA) ∨

<!-- b000260 | prose | pages [9] -->
P1,A < R ∧

<!-- b000261 | prose | pages [9] -->
• Hold

<!-- b000262 | prose | pages [9] -->
bB = 0 ∧∆dA > Dmin(vA)

<!-- b000263 | prose | pages [9] -->
⇒vA = vA + 1, bA = 0

<!-- b000264 | prose | pages [9] -->
On other circumstances, an NSDV holds its speed,which is shown in Lane 5 of Fig. 2:

<!-- b000265 | prose | pages [9] -->
[OtherCircumstances] ⇒bA = 0.

<!-- b000266 | prose | pages [9] -->
4.1.3 Following Rules for SDVs

<!-- b000267 | prose | pages [9] -->
According to the discussion in part 1 and part 2 of Section 2.4, SDVs have short reaction time and they can cooperate with each other. Considering that an accident happens right in front of a straight line of vehicles, all vehicles should decelerate in order to keep the MinSFD. If they are controlled by human beings whose reaction time cannot be ignored, vehicles will decelerate one by one but with a delay. However, if all vehicles are self-driving ones, they can decelerate at the same time, thanks to the cooperating system. It is the same for the acceleration process, because ai can be known for all SDVs,which is mentioned in Section 4.1.1.

<!-- b000268 | prose | pages [9] -->
Another factor is that the way changes to calculate minimum safe following distance between two SDVs which one follows another closely, because all SDVs share the information of speed and other parameters of the SDVs in front of them, which is mentioned in part 2 of Section 2.4. As is also assumed in part 3 of Section 2.4, malfunction of the self-driving system is not taken into consideration in this model. The two adjacent SDVs can decelerate at the same time if emergency happens, so that the MinSFD for an SDV can be calculated following Eqn. (4.7), in which the Braking Distance of the former can be removed. No collision between SDVs will happen when all information is shared and decisions are made cooperatively.

<!-- b000269 | prose | pages [9] -->
BrakingDistanceE = Dmin(max(vE −2, 0))

<!-- b000270 | prose | pages [9] -->
(

<!-- b000271 | prose | pages [9] -->
) (4.7)

<!-- b000272 | prose | pages [9] -->
Dmin(vA) −BrakingDistanceE + 1, 1

<!-- b000273 | prose | pages [9] -->
Dmin(SDV −SDV )(vA) = max

<!-- b000274 | prose | pages [9] -->
In Eqn. (4.7) E is the SDV ahead of A.

<!-- b000275 | prose | pages [9] -->
With the change of Dmin(SDV −SDV ), the distance between SDVs can be shortened and therefore a row of pure SDVs can be formed. When all the distances between two consecutive SDVs are their Dmin(SDV −SDV ), this chain of SDVs can be called a SDV-Train. For an SDV A, if it is in an SDV- Train, let F be the SDV in the front of the train. The three vehicles in Lane 4 from Fig. 3 form a typical SDV-Train.

<!-- b000276 | prose | pages [9] -->
Dmax(vA)

<!-- b000277 | prose | pages [9] -->
Dmin(vA)

<!-- b000278 | prose | pages [9] -->
vA A

<!-- b000279 | prose | pages [9] -->
Lane 1

<!-- b000280 | prose | pages [9] -->
vA A

<!-- b000281 | prose | pages [9] -->
Lane 2

<!-- b000282 | prose | pages [9] -->
vA

<!-- b000283 | prose | pages [9] -->
vA

<!-- b000284 | prose | pages [9] -->
A

<!-- b000285 | prose | pages [9] -->
Lane 3

<!-- b000286 | prose | pages [9] -->
vA A

<!-- b000287 | prose | pages [9] -->
Lane 4

<!-- b000288 | prose | pages [9] -->
a SDV-Train

<!-- b000289 | prose | pages [9] -->
Acceleration B

<!-- b000290 | prose | pages [9] -->
C C Acceleration

<!-- b000291 | prose | pages [9] -->
Acceleration E E

<!-- b000292 | prose | pages [9] -->
Acceleration

<!-- b000293 | prose | pages [9] -->
F (aF=1)

<!-- b000294 | caption | pages [9] -->
Figure 3: Following Rules for SDVs: Acceleration

<!-- b000295 | furniture | pages [10] -->
Team # 55585

<!-- b000296 | prose | pages [10] -->
• Acceleration

<!-- b000297 | prose | pages [10] -->
An SDV accelerates under 4 conditions:

<!-- b000298 | furniture | pages [10] -->
Page 8 of 34

<!-- b000299 | prose | pages [10] -->
1. it follows a vehicle B, and their distance is longer than Dmax(vA), that is:

<!-- b000300 | prose | pages [10] -->
∆DA ⩾Dmax(vA) ⇒vA = vA + 1; bA = 0; aA = 1;

<!-- b000301 | prose | pages [10] -->
which is the situation in Lane 1 in Fig. 3;

<!-- b000302 | prose | pages [10] -->
2. it follows an NSDV C, whose back light is off and their distance is longer than the MinSFD of A, that is:

<!-- b000303 | prose | pages [10] -->
tC = 0 ∧bC = 0 ∧∆DA ⩾Dmin(vA) ⇒vA = vA + 1; bA = 0; aA = 1;

<!-- b000304 | prose | pages [10] -->
which is the situation in Lane 2 in Fig. 3;

<!-- b000305 | prose | pages [10] -->
3. it follows an SDV E, and their distance is longer than the Dmin(SDV −SDV ) of A, that is:

<!-- b000306 | prose | pages [10] -->
tE = 1 ∧∆DA > Dmin(SDV −SDV )(vA) ⇒vA = vA + 1; bA = 0; aA = 1;

<!-- b000307 | prose | pages [10] -->
which is the situation in Lane 3 in Fig. 3;

<!-- b000308 | prose | pages [10] -->
4. it is in a ’SDV-Train’, and the ﬁrst SDV F in train accelerates, that is:

<!-- b000309 | prose | pages [10] -->
∆DA = Dmin(SDV −SDV )(vA) ∧aF = 1 ⇒vA = vA + 1; bA = 0; aA = 1.

<!-- b000310 | prose | pages [10] -->
which is the situation in Lane 4 in Fig. 3.

<!-- b000311 | prose | pages [10] -->
• Deceleration

<!-- b000312 | prose | pages [10] -->
Dmax(vA)

<!-- b000313 | prose | pages [10] -->
Dmin(vA)

<!-- b000314 | prose | pages [10] -->
vA C

<!-- b000315 | prose | pages [10] -->
Lane 1

<!-- b000316 | prose | pages [10] -->
A

<!-- b000317 | prose | pages [10] -->
vA

<!-- b000318 | prose | pages [10] -->
vA

<!-- b000319 | prose | pages [10] -->
Lane 2

<!-- b000320 | prose | pages [10] -->
A E

<!-- b000321 | prose | pages [10] -->
vA A

<!-- b000322 | prose | pages [10] -->
Lane 3

<!-- b000323 | prose | pages [10] -->
a SDV-Train

<!-- b000324 | prose | pages [10] -->
Deceleration

<!-- b000325 | prose | pages [10] -->
Deceleration

<!-- b000326 | prose | pages [10] -->
Deceleration F

<!-- b000327 | caption | pages [10] -->
Figure 4: Following Rules for SDVs: Deceleration

<!-- b000328 | prose | pages [10] -->
An SDV decelerates under 3 conditions:

<!-- b000329 | prose | pages [10] -->
1. it follows an NSDV C, and their distance is shorter than the MinSFD of A, that is:

<!-- b000330 | prose | pages [10] -->
tC = 0 ∧∆DA ⩽Dmin(vA) ⇒vA = vA −1; bA = 1; aA = 0;

<!-- b000331 | prose | pages [10] -->
which is the situation in Lane 1 in Fig. 4;

<!-- b000332 | prose | pages [10] -->
2. it follows an SDV E, and their distance is shorter than the Dmin(SDV −SDV ) of A, that is:

<!-- b000333 | prose | pages [10] -->
tE = 1 ∧∆DA ⩽Dmin(SDV −SDV )(vA) ⇒vA = vA −1; bA = 1; aA = 0;

<!-- b000334 | prose | pages [10] -->
which is the situation in Lane 2 in Fig. 4;

<!-- b000335 | furniture | pages [11] -->
Team # 55585

<!-- b000336 | furniture | pages [11] -->
Page 9 of 34

<!-- b000337 | prose | pages [11] -->
3. it is in a ’SDV-Train’, and the ﬁrst SDV F in train decelerates, that is:

<!-- b000338 | prose | pages [11] -->
∆DA = Dmin(SDV −SDV )(vA) ∧bF = 1 ⇒vA = vA −1; bA = 1; aA = 0.

<!-- b000339 | prose | pages [11] -->
which is the situation in Lane 3 in Fig. 4.

<!-- b000340 | prose | pages [11] -->
• Hold

<!-- b000341 | prose | pages [11] -->
On other circumstances, an SDV holds its speed:

<!-- b000342 | prose | pages [11] -->
[OtherCircumstances] ⇒bA = 0; aA = 0.

<!-- b000343 | prose | pages [11] -->
Two different situations are shown in Fig. 5:

<!-- b000344 | prose | pages [11] -->
Dmax(vA)

<!-- b000345 | prose | pages [11] -->
Dmin(vA)

<!-- b000346 | prose | pages [11] -->
vA A

<!-- b000347 | prose | pages [11] -->
Lane 1

<!-- b000348 | prose | pages [11] -->
vA

<!-- b000349 | prose | pages [11] -->
Lane 2

<!-- b000350 | prose | pages [11] -->
A

<!-- b000351 | prose | pages [11] -->
Hold C

<!-- b000352 | prose | pages [11] -->
Hold F （aF=0）

<!-- b000353 | prose | pages [11] -->
a SDV-Train

<!-- b000354 | caption | pages [11] -->
Figure 5: Following Rules for SDVs: Hold

<!-- b000355 | prose | pages [11] -->
4.2

<!-- b000356 | heading | pages [11] -->
Multilane Trafﬁc Model

<!-- b000357 | prose | pages [11] -->
On multilane highways, vehicles tend to stay on its own lane, which is the same as the Following Model mentioned above in Section 4.1. However, under certain circumstances, drivers change their lanes. The Multilane Trafﬁc Model is designed on the basis of the Following Model to simulate this lane-changing action [9]. Because of SDVs’ cooperation with each other and the formation of SDV-Trains, SDVs’ rules of changing lanes vary with NSDVs’.

<!-- b000358 | prose | pages [11] -->
4.2.1 Variables

<!-- b000359 | caption | pages [11] -->
Table 2: Additional Variables Used in the Multilane Trafﬁc Model

<!-- b000360 | prose | pages [11] -->
Variable Deﬁnation Unit

<!-- b000361 | prose | pages [11] -->
Distance between vehicle No. i and vehicle No.j ∆di,j cell Status of the turning lights of vehicle No.i ci unitless Number of lane which vehicle No.i is on li unitless

<!-- b000362 | prose | pages [11] -->
Possbility of a human driver of vehicle No.i P2,i unitless to change the lane when condition allows

<!-- b000363 | prose | pages [11] -->
Besides variables listed in Tab. 4.1.1, additional variables used in the Multilane Trafﬁc Model are listed in Tab. 4.2.1 and Fig. 6. Speciﬁcally, Eqn. (4.8) shows the function for the status of vehicle No.i’s turning lights:

<!-- b000364 | prose | pages [11] -->
 

<!-- b000365 | prose | pages [11] -->
turning lights of vehicle No. i are off 0,

<!-- b000366 | prose | pages [11] -->


<!-- b000367 | prose | pages [11] -->
ci =

<!-- b000368 | prose | pages [11] -->
the right turning light of vehicle No.i is on 1,

<!-- b000369 | prose | pages [11] -->
 

<!-- b000370 | prose | pages [11] -->
−1,

<!-- b000371 | prose | pages [11] -->
(4.8)

<!-- b000372 | prose | pages [11] -->
the left turning light of vehicle No.i is on

<!-- b000373 | furniture | pages [12] -->
Team # 55585

<!-- b000374 | prose | pages [12] -->
C vC lC=2

<!-- b000375 | prose | pages [12] -->
vF

<!-- b000376 | prose | pages [12] -->
Lane 1

<!-- b000377 | prose | pages [12] -->
F

<!-- b000378 | prose | pages [12] -->
vC

<!-- b000379 | prose | pages [12] -->
Lane 2

<!-- b000380 | prose | pages [12] -->
C

<!-- b000381 | prose | pages [12] -->
Both Lights Off

<!-- b000382 | prose | pages [12] -->
ci=0

<!-- b000383 | furniture | pages [12] -->
Page 10 of 34

<!-- b000384 | prose | pages [12] -->
ΔdA,E

<!-- b000385 | prose | pages [12] -->
vE E

<!-- b000386 | prose | pages [12] -->
vA vB A A B

<!-- b000387 | prose | pages [12] -->
Right Light On

<!-- b000388 | prose | pages [12] -->
Left Light On

<!-- b000389 | prose | pages [12] -->
ci=1

<!-- b000390 | prose | pages [12] -->
ci=-1

<!-- b000391 | caption | pages [12] -->
Figure 6: Diagram of Additional Variables Used in the Multilane Trafﬁc Model

<!-- b000392 | prose | pages [12] -->
4.2.2 General Rules of Changing Lanes

<!-- b000393 | prose | pages [12] -->
As we assumed in part 2 of Section 2.2, drivers only change their lane when necessary:

<!-- b000394 | prose | pages [12] -->
1. The vehicle on the same lane ahead is not far away and is running much slower;

<!-- b000395 | prose | pages [12] -->
2. The trafﬁc condition on the lane beside is better.

<!-- b000396 | prose | pages [12] -->
This is called Lane-Changing Motivation(LCM). After the satisfaction of LCM, two steps should be done when a vehicle’s driver wants to change the lane:

<!-- b000397 | prose | pages [12] -->
1. turn on the turning light when the condition permits;

<!-- b000398 | prose | pages [12] -->
2. change the lane when it is safe.

<!-- b000399 | prose | pages [12] -->
During this process, Lane-Changing Security(LCS) must be taken into consideration.

<!-- b000400 | prose | pages [12] -->
In short, only when both LCM and LCS are satisﬁed, may a vehicle change its lane.

<!-- b000401 | prose | pages [12] -->
4.2.3 Lane-Changing Rules for NSDVs

<!-- b000402 | prose | pages [12] -->
As showed in Fig. 6, B is the vehicle ahead of A and C is behind A. Three of them are all in the same lane. Only left-turning is discussed below because turning right is the same. Both E and F are in A’s left lane. E is the vehicle ahead and F is the vehicle behind.

<!-- b000403 | prose | pages [12] -->
• LCM of NSDV

<!-- b000404 | prose | pages [12] -->
As mentioned in Section 4.2.2, there are two components of LCM:

<!-- b000405 | prose | pages [12] -->
– B is running slower than A and not far away;

<!-- b000406 | prose | pages [12] -->
– E is running faster or far away.

<!-- b000407 | prose | pages [12] -->
So,

<!-- b000408 | prose | pages [12] -->
LCMA = (∆dA,B < Dmax(vA) ∧vB < vA) ∧(∆dA,E > Dmax(vA) ∨vE > vA) (4.9)

<!-- b000409 | prose | pages [12] -->
Some of the circumstances are shown in Fig. 7.

<!-- b000410 | furniture | pages [13] -->
Team # 55585

<!-- b000411 | furniture | pages [13] -->
Page 11 of 34

<!-- b000412 | prose | pages [13] -->
Dmax(vA)

<!-- b000413 | prose | pages [13] -->
Dmin(vA)

<!-- b000414 | prose | pages [13] -->
Lane 1

<!-- b000415 | prose | pages [13] -->
vA A

<!-- b000416 | prose | pages [13] -->
Lane 2

<!-- b000417 | prose | pages [13] -->
Lane 1

<!-- b000418 | prose | pages [13] -->
vA

<!-- b000419 | prose | pages [13] -->
Lane 2

<!-- b000420 | prose | pages [13] -->
A

<!-- b000421 | prose | pages [13] -->
LCMA

<!-- b000422 | prose | pages [13] -->
×

<!-- b000423 | prose | pages [13] -->
vE E

<!-- b000424 | prose | pages [13] -->
vB

<!-- b000425 | prose | pages [13] -->
(vA<vB)

<!-- b000426 | prose | pages [13] -->
B B

<!-- b000427 | prose | pages [13] -->
vE E

<!-- b000428 | furniture | pages [13] -->


<!-- b000429 | prose | pages [13] -->
vB B B

<!-- b000430 | caption | pages [13] -->
Figure 7: LCM for NSDVs under Certain Conditions

<!-- b000431 | prose | pages [13] -->
• LCS of NSDV

<!-- b000432 | prose | pages [13] -->
Three parts of LCS should be taken into consideration:

<!-- b000433 | prose | pages [13] -->
– B and E are not in A’s MinSFD ;

<!-- b000434 | prose | pages [13] -->
– A will not be in F’s MinSFD after A’s changing lane;

<!-- b000435 | prose | pages [13] -->
– C’s left turning light is off.

<!-- b000436 | prose | pages [13] -->
That is:

<!-- b000437 | prose | pages [13] -->
LCSA = ∆dA,B > Dmin(vA) ∧∆dA,E > Dmin(vA) ∧∆dA,F > Dmin(vF ) ∧cC̸ = −1 (4.10)

<!-- b000438 | prose | pages [13] -->
A few of the circumstances are shown in Fig. 8.

<!-- b000439 | prose | pages [13] -->
Dmax(vA)

<!-- b000440 | prose | pages [13] -->
LCSA

<!-- b000441 | prose | pages [13] -->
Dmin(vA)

<!-- b000442 | prose | pages [13] -->
vE Lane 1 E

<!-- b000443 | prose | pages [13] -->
vC

<!-- b000444 | prose | pages [13] -->
vA

<!-- b000445 | prose | pages [13] -->
C

<!-- b000446 | prose | pages [13] -->
A

<!-- b000447 | prose | pages [13] -->
Lane 2

<!-- b000448 | prose | pages [13] -->
Lane 1

<!-- b000449 | prose | pages [13] -->
vC

<!-- b000450 | prose | pages [13] -->
vA

<!-- b000451 | prose | pages [13] -->
Lane 2

<!-- b000452 | prose | pages [13] -->
C

<!-- b000453 | prose | pages [13] -->
A

<!-- b000454 | prose | pages [13] -->
Lane 1

<!-- b000455 | prose | pages [13] -->
vC

<!-- b000456 | prose | pages [13] -->
vA

<!-- b000457 | prose | pages [13] -->
Lane 2

<!-- b000458 | prose | pages [13] -->
C

<!-- b000459 | prose | pages [13] -->
A

<!-- b000460 | prose | pages [13] -->
×

<!-- b000461 | prose | pages [13] -->
vB B

<!-- b000462 | prose | pages [13] -->
ΔdA,E<Dmin(vA)

<!-- b000463 | prose | pages [13] -->
×

<!-- b000464 | prose | pages [13] -->
vE E

<!-- b000465 | prose | pages [13] -->
cC=-1

<!-- b000466 | prose | pages [13] -->
vB B

<!-- b000467 | prose | pages [13] -->
vE E

<!-- b000468 | furniture | pages [13] -->


<!-- b000469 | prose | pages [13] -->
vB B

<!-- b000470 | caption | pages [13] -->
Figure 8: LCS for NSDVs under Certain Conditions

<!-- b000471 | prose | pages [13] -->
• Lane-Changing Possibility(LCP).

<!-- b000472 | furniture | pages [14] -->
Team # 55585

<!-- b000473 | furniture | pages [14] -->
Page 12 of 34

<!-- b000474 | prose | pages [14] -->
Even when both LCM and LCS are satisﬁed, a human driver may not change a lane to make the vehicle run faster [9]. To simulate this statistical randomness of physiological character- istics, function P2,i is introduced in the Multilane Trafﬁc Model. As Eqn.(4.11) shows, there is a possibility for an NSDV to change its lane and it varies upon three different circumstances, considering B as the vehicle in front of A in the same lane.

<!-- b000475 | prose | pages [14] -->
 

<!-- b000476 | prose | pages [14] -->
bB = 1 ∧∆dA > Dmin(vA) ∧∆dA < Dmax(vA) P21,

<!-- b000477 | prose | pages [14] -->
   

<!-- b000478 | prose | pages [14] -->
bB = 0 ∧∆dA > Dmin(vA) ∧∆dA < Dmax(vA) P22,

<!-- b000479 | prose | pages [14] -->
P2,A =

<!-- b000480 | prose | pages [14] -->


<!-- b000481 | prose | pages [14] -->
P23, vA = 0

<!-- b000482 | prose | pages [14] -->
   

<!-- b000483 | prose | pages [14] -->
0, other cases

<!-- b000484 | prose | pages [14] -->
(4.11)

<!-- b000485 | prose | pages [14] -->
Let R be a random number between 0 and 1, and LCP follows Eqn. (4.12):

<!-- b000486 | prose | pages [14] -->
LCPA = (P2,A ⩾R)

<!-- b000487 | prose | pages [14] -->
• Total Effect of LCM, LCS and LCP

<!-- b000488 | prose | pages [14] -->
(4.12)

<!-- b000489 | prose | pages [14] -->
As Section 4.2.2 mentioned, there are two steps to change a lane: turn on the turning light and take the turn. That is:

<!-- b000490 | prose | pages [14] -->
STEP 1: LCMA ∧LCSA ∧LCPA ⇒cA = −1;

<!-- b000491 | prose | pages [14] -->
STEP 2: LCMA ∧LCSA ∧cA = −1 ⇒rA = rA −1; cA = 0.

<!-- b000492 | prose | pages [14] -->
4.2.4 Lane-Changing Rules for SDVs

<!-- b000493 | prose | pages [14] -->
Compared with NSDVs, SDVs can share information with each other and Lane-Changing Rules for SDVs should be changed. The rules are almost the same as those in 4.1.3:

<!-- b000494 | prose | pages [14] -->
1. The calculation of MinSFD should be changed as Eqn. (4.13) shows:

<!-- b000495 | prose | pages [14] -->
{

<!-- b000496 | prose | pages [14] -->
Dmin(SDV −SDV )(vA),

<!-- b000497 | prose | pages [14] -->
D∗

<!-- b000498 | prose | pages [14] -->
min(A,B)(vA) =

<!-- b000499 | prose | pages [14] -->
Dmin(vA), both A and B are SDV (4.13) other circumstances

<!-- b000500 | prose | pages [14] -->
2. An SDV-Train can be formed and in this case the whole train can change a lane at the same time;

<!-- b000501 | prose | pages [14] -->
3. An SDV does not have an LCP.

<!-- b000502 | prose | pages [14] -->
Therefore, for an SDV, Eqn. (4.9) and Eqn. (4.10) should be modiﬁed to Eqn. (4.14) and Eqn. (4.15):

<!-- b000503 | prose | pages [14] -->
LCMA = (∆dA,B < Dmax(vA) ∧vB < vA) ∧(∆dA,E > Dmax(vA) ∨vE > vA)

<!-- b000504 | prose | pages [14] -->
(4.14) ∨cB = −1 ∧tB = 1 ∨cG = −1

<!-- b000505 | prose | pages [14] -->
min(A,E)(vA)∧∆dA,F > D∗

<!-- b000506 | prose | pages [14] -->
LCSA = ∆dA,B > D∗

<!-- b000507 | prose | pages [14] -->
min(A,B)(vA)∧∆dA,E > D∗

<!-- b000508 | prose | pages [14] -->
min(A,F)(vF )∧(cC̸ = −1∨tC = 1)

<!-- b000509 | prose | pages [14] -->
(4.15) In Eqn. (4.14) and Eqn. (4.15), the deﬁnitions of vehicle B,C,E,F are the same as those in . Vehicle G is the ﬁrst SDV in A’s SDV-Train. Some of the circumstances are shown in Fig. 9 and Fig. 10. And the 2-step procedure for an SDV to change a lane is:

<!-- b000510 | prose | pages [14] -->
STEP 1: LCM ∧LCS ⇒cA = −1;

<!-- b000511 | prose | pages [14] -->
STEP 2: LCM ∧LCS ∧cA = −1 ⇒rA = rA −1; cA = 0.

<!-- b000512 | furniture | pages [15] -->
Team # 55585

<!-- b000513 | prose | pages [15] -->
Dmax(vA) LCMA

<!-- b000514 | prose | pages [15] -->
Dmin(vA)

<!-- b000515 | prose | pages [15] -->
×

<!-- b000516 | prose | pages [15] -->
vE Lane 1 E

<!-- b000517 | prose | pages [15] -->
(vA<vB，

<!-- b000518 | prose | pages [15] -->
vA vB A B

<!-- b000519 | prose | pages [15] -->
Lane 2 cB -1)

<!-- b000520 | prose | pages [15] -->
×

<!-- b000521 | prose | pages [15] -->
vE E Lane 1

<!-- b000522 | prose | pages [15] -->
vA vB

<!-- b000523 | prose | pages [15] -->
(tB=0)

<!-- b000524 | prose | pages [15] -->
A B

<!-- b000525 | prose | pages [15] -->
Lane 2

<!-- b000526 | furniture | pages [15] -->


<!-- b000527 | prose | pages [15] -->
vE E Lane 1

<!-- b000528 | prose | pages [15] -->
vA vB

<!-- b000529 | prose | pages [15] -->
vG (cG=-1)

<!-- b000530 | prose | pages [15] -->
A B

<!-- b000531 | prose | pages [15] -->
G

<!-- b000532 | prose | pages [15] -->
Lane 2

<!-- b000533 | caption | pages [15] -->
Figure 9: LCM for SDVs under Certain Condi-

<!-- b000534 | prose | pages [15] -->
tions

<!-- b000535 | furniture | pages [15] -->
Page 13 of 34

<!-- b000536 | prose | pages [15] -->
Dmax(vA)

<!-- b000537 | prose | pages [15] -->
LCSA

<!-- b000538 | prose | pages [15] -->
Dmin(vA)

<!-- b000539 | prose | pages [15] -->
×

<!-- b000540 | prose | pages [15] -->
vE Lane 1 E

<!-- b000541 | prose | pages [15] -->
vC

<!-- b000542 | prose | pages [15] -->
vA vB

<!-- b000543 | prose | pages [15] -->
ΔdA,E<Δdmin(vA) C

<!-- b000544 | prose | pages [15] -->
A B

<!-- b000545 | prose | pages [15] -->
Lane 2

<!-- b000546 | prose | pages [15] -->
×

<!-- b000547 | prose | pages [15] -->
vE Lane 1 E

<!-- b000548 | prose | pages [15] -->
cC=-1

<!-- b000549 | prose | pages [15] -->
vC

<!-- b000550 | prose | pages [15] -->
vA vB

<!-- b000551 | prose | pages [15] -->
Lane 2

<!-- b000552 | prose | pages [15] -->
C

<!-- b000553 | prose | pages [15] -->
A B

<!-- b000554 | prose | pages [15] -->
tC=0

<!-- b000555 | prose | pages [15] -->
vE Lane 1 E

<!-- b000556 | furniture | pages [15] -->


<!-- b000557 | prose | pages [15] -->
vC

<!-- b000558 | prose | pages [15] -->
vA vB

<!-- b000559 | prose | pages [15] -->
Lane 2

<!-- b000560 | prose | pages [15] -->
C

<!-- b000561 | prose | pages [15] -->
A B

<!-- b000562 | caption | pages [15] -->
Figure 10: LCS for SDVs under Certain Conditions

<!-- b000563 | heading | pages [15] -->
Analysis of the Results Obtained from the Model Simulation

<!-- b000564 | prose | pages [15] -->
5

<!-- b000565 | prose | pages [15] -->
After programming according to our CA models, we get a large number of data from simulations using parameters in real life. Matlab and other softwares are used to calculate and visualize the data, showing many good features as follows:

<!-- b000566 | prose | pages [15] -->
5.1

<!-- b000567 | heading | pages [15] -->
Results of Following Model

<!-- b000568 | prose | pages [15] -->
Δd=22 cell

<!-- b000569 | prose | pages [15] -->
Δd=10 cell

<!-- b000570 | prose | pages [15] -->
SDV NSDV Time

<!-- b000571 | prose | pages [15] -->
an SDV-Train

<!-- b000572 | caption | pages [15] -->
Figure 11: One of the Results of Following Model Simulation

<!-- b000573 | caption | pages [15] -->
Fig. 11 shows one of the results of the Following Model, in which each dot represents a vehicle

<!-- b000574 | prose | pages [15] -->
and each line represents the lane during different time. The time difference between two adjacent lane is one turn. As time goes by, all vehicles run forward with different speed. We can ﬁnd that in this simulation, the distance between two NSDVs are much longer than that between two SDVs, which is in line with the MinSFD we set. An SDV-Train is also found in the simulation, saving the space on the road and speeding up the trafﬁc ﬂow.

<!-- b000575 | prose | pages [15] -->
After calculating and summarizing the data, we found strong correlations among the average speed of all vehicles, the percentage in SDVs of all vehicles and the overall trafﬁc ﬂow, which is

<!-- b000576 | furniture | pages [16] -->
Team # 55585

<!-- b000577 | furniture | pages [16] -->
Page 14 of 34

<!-- b000578 | prose | pages [16] -->
shown in a three dimension map in Fig. 12. In this ﬁgure each data point represents an average of 6 simulations based on same parameters.

<!-- b000579 | prose | pages [16] -->
60

<!-- b000580 | prose | pages [16] -->
55

<!-- b000581 | prose | pages [16] -->
50

<!-- b000582 | prose | pages [16] -->
Average Speed (mph)

<!-- b000583 | prose | pages [16] -->
45

<!-- b000584 | prose | pages [16] -->
40

<!-- b000585 | prose | pages [16] -->
35

<!-- b000586 | prose | pages [16] -->
30

<!-- b000587 | prose | pages [16] -->
25

<!-- b000588 | prose | pages [16] -->
20

<!-- b000589 | prose | pages [16] -->
15

<!-- b000590 | prose | pages [16] -->
10

<!-- b000591 | prose | pages [16] -->
100

<!-- b000592 | prose | pages [16] -->
50

<!-- b000593 | prose | pages [16] -->
200 0

<!-- b000594 | prose | pages [16] -->
Percentage of SDVs

<!-- b000595 | prose | pages [16] -->
0

<!-- b000596 | prose | pages [16] -->
55

<!-- b000597 | prose | pages [16] -->
50

<!-- b000598 | prose | pages [16] -->
45

<!-- b000599 | prose | pages [16] -->
40

<!-- b000600 | prose | pages [16] -->
35

<!-- b000601 | prose | pages [16] -->
30

<!-- b000602 | prose | pages [16] -->
25

<!-- b000603 | prose | pages [16] -->
20

<!-- b000604 | prose | pages [16] -->
15

<!-- b000605 | prose | pages [16] -->
1400 1200 1000

<!-- b000606 | prose | pages [16] -->
800 600 400

<!-- b000607 | prose | pages [16] -->
Traffic Flow (vehicle/h)

<!-- b000608 | caption | pages [16] -->
Figure 12: Correlations Among Average Speed, the Percentage of SDVs and the Trafﬁc Flow

<!-- b000609 | prose | pages [16] -->
As we can ﬁnd in Fig. 12, all data points ﬁt to a continuous smooth surface, showing that the higher the percentage of SDVs is, the faster all vehicles run and the larger the trafﬁc ﬂow is, the lower the average speed is. These two features are consistent with common sense. Another interesting feature is that the decreasing trend of speed related to the trafﬁc ﬂow is stongly inﬂuenced by the percentage of SDVs. Some typical curves of that are shown in Fig. 13. Also, we can ﬁnd that there is a maximum trafﬁc ﬂow for each percentage of SDVs, which is shown in detail in Fig. 14.

<!-- b000610 | prose | pages [16] -->
60

<!-- b000611 | prose | pages [16] -->
PSDV=0%

<!-- b000612 | prose | pages [16] -->
x x x

<!-- b000613 | prose | pages [16] -->
55

<!-- b000614 | prose | pages [16] -->
PSDV=10%

<!-- b000615 | prose | pages [16] -->
x x

<!-- b000616 | prose | pages [16] -->
50

<!-- b000617 | prose | pages [16] -->
PSDV=50%

<!-- b000618 | prose | pages [16] -->
Average Speed (mph)

<!-- b000619 | prose | pages [16] -->
PSDV=70%

<!-- b000620 | prose | pages [16] -->
45

<!-- b000621 | prose | pages [16] -->
PSDV=90%

<!-- b000622 | prose | pages [16] -->
40

<!-- b000623 | prose | pages [16] -->
35

<!-- b000624 | prose | pages [16] -->
30

<!-- b000625 | prose | pages [16] -->
25

<!-- b000626 | prose | pages [16] -->
20

<!-- b000627 | prose | pages [16] -->
15

<!-- b000628 | prose | pages [16] -->
10

<!-- b000629 | prose | pages [16] -->
0 200 400 800 1000 600 Traffic Flow (vehicle/h)

<!-- b000630 | prose | pages [16] -->
1300

<!-- b000631 | prose | pages [16] -->
Maximum Traffic Flow (vehicle/h)

<!-- b000632 | prose | pages [16] -->
1200

<!-- b000633 | prose | pages [16] -->
1100

<!-- b000634 | prose | pages [16] -->
1000

<!-- b000635 | prose | pages [16] -->
900

<!-- b000636 | prose | pages [16] -->
800

<!-- b000637 | prose | pages [16] -->
700

<!-- b000638 | prose | pages [16] -->
600

<!-- b000639 | prose | pages [16] -->
500

<!-- b000640 | prose | pages [16] -->
400

<!-- b000641 | prose | pages [16] -->
0 20 40 60 80 100

<!-- b000642 | prose | pages [16] -->
1200

<!-- b000643 | prose | pages [16] -->
Percentage of SDVs

<!-- b000644 | caption | pages [16] -->
Figure 14:

<!-- b000645 | prose | pages [16] -->
Relationship between Maxi-

<!-- b000646 | caption | pages [16] -->
Figure 13: Relationship between Average Speed and

<!-- b000647 | prose | pages [16] -->
the Trafﬁc Flow under Certain Ratios of SDVs

<!-- b000648 | prose | pages [16] -->
mum Trafﬁc Flow and Percentage of SDVs

<!-- b000649 | prose | pages [16] -->
In Fig. 13, we can see clearly that the percentage of SDVs makes a great difference on the trafﬁc. As the blue curve shows, only when the trafﬁc ﬂow is below 200 vehicles per hour is the average speed above 50mph. When the trafﬁc ﬂow is around 400 vehicles per hour, the average speed main- tains at 15mph and a larger trafﬁc ﬂow would not get through when all vehicles are NSDVs. From

<!-- b000650 | furniture | pages [17] -->
Team # 55585

<!-- b000651 | furniture | pages [17] -->
Page 15 of 34

<!-- b000652 | prose | pages [17] -->
the green curve we can see that the situation changes dramatically when the percentage of SDVs increases. At the percentage of 90% the average speed stays higher than 50mph when the trafﬁc ﬂow is up tp 600 vehicles per hour and the maximum trafﬁc ﬂow is about 950 vehicles per hour which is more than twice of that when there is no SDV on the road.

<!-- b000653 | prose | pages [17] -->
Also in Fig. 13, tipping points where the slope of the curve changes greatly are marked as red crosses. Before these points, the average speed changes slowly as the trafﬁc ﬂow grows while after these points, the speed drops rapidly and soon reach its lowest. When the speed is lower than about 14mph, equilibria are found. When too many vehicles are running on the road, a trafﬁc jam is formed, therefore the speed maintains at a low level.

<!-- b000654 | prose | pages [17] -->
The relationship between the maximum trafﬁc ﬂow and the percentage of SDVs is shown in

<!-- b000655 | caption | pages [17] -->
Fig. 14. As we can see, the maximum trafﬁc ﬂow is almost a continuous function of the percentage,

<!-- b000656 | prose | pages [17] -->
indicating the great inﬂuence of trafﬁc ﬂow by the appearance of SDVs: the maximum trafﬁc ﬂow almost triples when the percentage is 100%.

<!-- b000657 | prose | pages [17] -->
5.2

<!-- b000658 | heading | pages [17] -->
Results of the Multilane Trafﬁc Model

<!-- b000659 | prose | pages [17] -->
B

<!-- b000660 | prose | pages [17] -->
an SDV-Train

<!-- b000661 | prose | pages [17] -->
SDV NSDV

<!-- b000662 | prose | pages [17] -->
A

<!-- b000663 | prose | pages [17] -->
Time Speed

<!-- b000664 | caption | pages [17] -->
Figure 15: One of the Results of the Multilane Trafﬁc Model Simulation

<!-- b000665 | prose | pages [17] -->
In Fig. 15 is one of the results of the Following Model where lane-changing is taken into consid- eration. This is a highway of 4 lanes. In section A of Fig. 15, an overtaking happens in the Multilane Trafﬁc Model. This situation cannot happen in the Following Model according to our rules. In sec- tion B of Fig. 15, we can ﬁnd that an SDV chooses to change its lane to form a longer SDV-Train. Lane-changing and overtaking occur when a vehicle wants to speed up, but whether their inﬂuence on the trafﬁc ﬂow is positive or not is complicated, which will be discussed afterwards.

<!-- b000666 | prose | pages [17] -->
Obviously, a highway with more lanes has a larger total trafﬁc ﬂow, which is shown in Fig. 16. The total ﬂow is almost proportional to the number of lanes, which is in line with common sense. We can also ﬁnd that more vehicles can travel through when more SDVs are on the road. This is the same as the results of the Following Model in Section 5.1.

<!-- b000667 | prose | pages [17] -->
The relative trafﬁc ﬂow per lane is interesting, which is shown in Fig. 17. In this ﬁgure, the y-axis shows the car ﬂow per lane divided by this number of the situation when there is only 1 lane. We can ﬁnd that before 50%, the efﬁciency of each lane decreases as the number of lanes increases. This phenomenon is corresponding to the study in Bridges and Transmission Line Structures [10], suggesting that the lane-changing and overtaking of a human driver interfere the ﬂuency of the trafﬁc ﬂow, resulting in a slow down and the decrease of the lane efﬁciency. Lane-changing and overtaking happens more frequently when there are more lanes, so it is natural that the efﬁciency goes down as the number of lanes goes up.

<!-- b000668 | furniture | pages [18] -->
Team # 55585

<!-- b000669 | prose | pages [18] -->
3000

<!-- b000670 | prose | pages [18] -->
1 lane

<!-- b000671 | prose | pages [18] -->
2 lanes

<!-- b000672 | prose | pages [18] -->
2500

<!-- b000673 | prose | pages [18] -->
Total Traffic Flow (vehicle/hour)

<!-- b000674 | prose | pages [18] -->
3 lanes

<!-- b000675 | prose | pages [18] -->
4 lanes

<!-- b000676 | prose | pages [18] -->
2000

<!-- b000677 | prose | pages [18] -->
5 lanes

<!-- b000678 | prose | pages [18] -->
1500

<!-- b000679 | prose | pages [18] -->
1000

<!-- b000680 | prose | pages [18] -->
500

<!-- b000681 | prose | pages [18] -->
0

<!-- b000682 | prose | pages [18] -->
0 10 20 30 40 50 60 70 80 90 100 Percentage of SDVs

<!-- b000683 | caption | pages [18] -->
Figure 16:

<!-- b000684 | prose | pages [18] -->
Relationships Between Total Trafﬁc Flow and the Percentage of SDVs

<!-- b000685 | furniture | pages [18] -->
Page 16 of 34

<!-- b000686 | prose | pages [18] -->
1.01

<!-- b000687 | prose | pages [18] -->
1 lane 2 lanes

<!-- b000688 | prose | pages [18] -->
1.005

<!-- b000689 | prose | pages [18] -->
3 lanes 4 lanes

<!-- b000690 | prose | pages [18] -->
Relative Traffic Flow Per Lane

<!-- b000691 | prose | pages [18] -->
1

<!-- b000692 | prose | pages [18] -->
5 lanes

<!-- b000693 | prose | pages [18] -->
0.995

<!-- b000694 | prose | pages [18] -->
0.99

<!-- b000695 | prose | pages [18] -->
0.985

<!-- b000696 | prose | pages [18] -->
0.98

<!-- b000697 | prose | pages [18] -->
0.975

<!-- b000698 | prose | pages [18] -->
0.97

<!-- b000699 | prose | pages [18] -->
0 10 20 30 40 50 60 70 80 90 100 Percentage of SDVs

<!-- b000700 | caption | pages [18] -->
Figure 17: Relationships Between Relative Trafﬁc

<!-- b000701 | prose | pages [18] -->
Flow Per Lane and the Percentage of SDVs

<!-- b000702 | prose | pages [18] -->
In our study, the situation is a bit different from the result in Bridges and Transmission Line Struc- tures [10] because SDVs are added on the road and their behaviors are different from those of NSDVs. As we can see in Fig. 17, the efﬁciency reaches its lowest when the percentage of SDVs is about 50%, suggesting that there are as many SDVs as NSDVs on the road when the efﬁciency is the lowest. This is mainly because the formation and collapse of SDV-Trains happen frequently when both SDVs and NSDVs try to change their lanes to gain more speed. Their motivations conﬂict with each other and these lead to a great interfere to the trafﬁc ﬂow. The form and reform of SDV-Trains take time and SDVs’ speed change a lot during these sections, which result in the decrease of the efﬁciency. This situation happens most frequently when the number of SDVs and that of NSDVs are almost the same, explaining the peak at 50%.

<!-- b000703 | prose | pages [18] -->
The reason for the rise of efﬁciency when the percentage of SDVs is higher than 50% is that NSDVs that interfere SDV-Trains will become fewer as the ratio of SDVs rises. When this percentage is close to 100%, almost all vehicles on the road are SDVs and a long SDV-Train can be formed even from the beginning to the end of the road. With the short MinSFD between SDVs in an SDV-Train, the efﬁciency raises rapidly and it is even higher than that of the situation when there is only one lane, because adjustments to form a longer SDV-Train are easily made on a multilane highway full of SDVs while no adjustment can be made on a single-lane road.

<!-- b000704 | prose | pages [18] -->
5.3 SDV Lane

<!-- b000705 | prose | pages [18] -->
3000

<!-- b000706 | prose | pages [18] -->
1 lane 2 lanes

<!-- b000707 | prose | pages [18] -->
2 lanes with 1 SDV lane

<!-- b000708 | prose | pages [18] -->
Average Traffic Flow Per Hour

<!-- b000709 | prose | pages [18] -->
3 lanes

<!-- b000710 | prose | pages [18] -->
3 lanes with 1 SDV lane

<!-- b000711 | prose | pages [18] -->
2500

<!-- b000712 | prose | pages [18] -->
4 lanes

<!-- b000713 | prose | pages [18] -->
4 lanes with 1 SDV lane

<!-- b000714 | prose | pages [18] -->
5 lanes

<!-- b000715 | prose | pages [18] -->
5 lanes with 1 SDV lane

<!-- b000716 | prose | pages [18] -->
2000

<!-- b000717 | prose | pages [18] -->
1500

<!-- b000718 | prose | pages [18] -->
1000

<!-- b000719 | prose | pages [18] -->
500

<!-- b000720 | prose | pages [18] -->
0

<!-- b000721 | prose | pages [18] -->
0 10 20 30 40 50 60 70 80 90 100 Possibility of SDVs

<!-- b000722 | caption | pages [18] -->
Figure 18: The Inﬂuence of Setting an SDV Lane

<!-- b000723 | furniture | pages [19] -->
Team # 55585

<!-- b000724 | furniture | pages [19] -->
Page 17 of 34

<!-- b000725 | prose | pages [19] -->
As shown in Fig. 18, the solid lines represent the relationships between average trafﬁc ﬂow and percentage of SDVs running on a multilane highway with 1 SDV Lane. When the percentage of SDVs is low, the ﬂow is lower than that of the original one with the same number of lanes, because in this situation, the using rate of the SDV Lane is too low. Speciﬁcally, when the percentage is 0, the trafﬁc ﬂow equals to the ﬂow of highway with one less lane as the SDV Lane is empty. When the percentage rises, the trafﬁc ﬂow increases and soon it is higher than that of the orginal one. After this point, the setting of a SDV Lane brings beneﬁt to the transportation capacity. The fall of the curve when the percentage is high is reasonable because we assumed in Section 2.1 that all SDVs should run in only one SDV lane, resulting a trafﬁc jam and a waste of space on the non-SDV Lanes.

<!-- b000726 | prose | pages [19] -->
6

<!-- b000727 | heading | pages [19] -->
Appliance of the Model

<!-- b000728 | prose | pages [19] -->
7000

<!-- b000729 | prose | pages [19] -->
Average Traffic Flow Per Hour (vehicle/

<!-- b000730 | prose | pages [19] -->
6000

<!-- b000731 | prose | pages [19] -->
5000

<!-- b000732 | prose | pages [19] -->
4000

<!-- b000733 | prose | pages [19] -->
3000

<!-- b000734 | prose | pages [19] -->
2000

<!-- b000735 | prose | pages [19] -->
1000

<!-- b000736 | prose | pages [19] -->
hour)

<!-- b000737 | prose | pages [19] -->
0

<!-- b000738 | prose | pages [19] -->
100 120 140 160 180 200 220 Mileage(DECR) (mile)

<!-- b000739 | prose | pages [19] -->
7000 The actual situation Simulation: PDSV=100%

<!-- b000740 | prose | pages [19] -->
6000

<!-- b000741 | prose | pages [19] -->
Simulation: PDSV=50%

<!-- b000742 | prose | pages [19] -->
Simulation: PDSV=0%

<!-- b000743 | prose | pages [19] -->
5000

<!-- b000744 | prose | pages [19] -->
4000

<!-- b000745 | prose | pages [19] -->
3000

<!-- b000746 | prose | pages [19] -->
2000

<!-- b000747 | prose | pages [19] -->
1000

<!-- b000748 | prose | pages [19] -->
0

<!-- b000749 | prose | pages [19] -->
100 120 140 160 180 200 220 Mileage(INCR) (mile)

<!-- b000750 | caption | pages [19] -->
Figure 19: Appliance of Our Model on Interstate 5

<!-- b000751 | prose | pages [19] -->
We apply our model on Interstates 5, 90, 402 and State Route 520 by comparing the real average trafﬁc ﬂow and the results of simluations, as Fig. 19 and Fig. 20 show. In the ﬁgure, much higher than the red curve, the black curve represents the actual situation, one that represents the simulation without SDVs, indicating that the transportation need in the Great Seattle is way beyond the trans- portation capacity now. The rules for speed limit and the safe following distance cannot be followed as the ﬁgure suggest, which may result in serious trafﬁc accidents even fatal ones.

<!-- b000752 | prose | pages [19] -->
6000

<!-- b000753 | prose | pages [19] -->
6000

<!-- b000754 | prose | pages [19] -->
4000

<!-- b000755 | prose | pages [19] -->
4000

<!-- b000756 | prose | pages [19] -->
DECR

<!-- b000757 | prose | pages [19] -->
2000

<!-- b000758 | prose | pages [19] -->
2000

<!-- b000759 | prose | pages [19] -->
0

<!-- b000760 | prose | pages [19] -->
0

<!-- b000761 | prose | pages [19] -->
0 5 10 15 20 25

<!-- b000762 | prose | pages [19] -->
0 10

<!-- b000763 | prose | pages [19] -->
6000

<!-- b000764 | prose | pages [19] -->
6000

<!-- b000765 | prose | pages [19] -->
4000

<!-- b000766 | prose | pages [19] -->
4000

<!-- b000767 | prose | pages [19] -->
INCR

<!-- b000768 | prose | pages [19] -->
2000

<!-- b000769 | prose | pages [19] -->
2000

<!-- b000770 | prose | pages [19] -->
0

<!-- b000771 | prose | pages [19] -->
0

<!-- b000772 | prose | pages [19] -->
0 5 20 25

<!-- b000773 | prose | pages [19] -->
0

<!-- b000774 | prose | pages [19] -->
10 15

<!-- b000775 | prose | pages [19] -->
10

<!-- b000776 | prose | pages [19] -->
6000

<!-- b000777 | prose | pages [19] -->
4000

<!-- b000778 | prose | pages [19] -->
2000

<!-- b000779 | prose | pages [19] -->
0

<!-- b000780 | prose | pages [19] -->
20 30

<!-- b000781 | prose | pages [19] -->
0 5 10

<!-- b000782 | prose | pages [19] -->
6000

<!-- b000783 | prose | pages [19] -->
4000

<!-- b000784 | prose | pages [19] -->
2000

<!-- b000785 | prose | pages [19] -->
0

<!-- b000786 | prose | pages [19] -->
30

<!-- b000787 | prose | pages [19] -->
0 5 10

<!-- b000788 | prose | pages [19] -->
20 Interstate 405

<!-- b000789 | prose | pages [19] -->
Interstate 90

<!-- b000790 | prose | pages [19] -->
State Route 520

<!-- b000791 | caption | pages [19] -->
Figure 20: Appliance of Our Model on Interstates 90, 402 and State Route 520

<!-- b000792 | prose | pages [19] -->
In order to reduce trafﬁc congestion and trafﬁc accidents, changing from NSDVs to SDVs has been considered, which is shown in Fig. 19 and Fig. 20. As the green curve suggests, if all the vehicles are SDVs, the trafﬁc capacity of these 4 roads can basically reach the need. This shows that

<!-- b000793 | furniture | pages [20] -->
Team # 55585

<!-- b000794 | furniture | pages [20] -->
Page 18 of 34

<!-- b000795 | prose | pages [20] -->
the lack of trafﬁc capacity can be reduced by not completely solved by SDVs and a vast varieties of different methods including broadening the road should be taken into consideration. From Fig. 19 and Fig. 20, we can ﬁnd out that only a small part of the road has extremely high trafﬁc ﬂow, so broaden this few parts is feasible. Another way to enlarge the trafﬁc capacity is to set a SDV Lane.

<!-- b000796 | caption | pages [20] -->
Fig. 18 suggests that when the percentage of SDVs is larger than about 30%, a SDV Lane should be

<!-- b000797 | prose | pages [20] -->
built to speed up the trafﬁc.

<!-- b000798 | prose | pages [20] -->
7

<!-- b000799 | heading | pages [20] -->
Sensitivity Analysis

<!-- b000800 | prose | pages [20] -->
As the parameters in LCP of NSDVs which is mentioned in 4.12 may be hard to obtain or there might be some uncertainty, the choice of LCPs might inﬂuence the result of out model. Also, we need to ﬁnd out whether our model speciﬁcally ﬁt the situation where the speed limit is 60 mph by changing the maximum speed in our model to see whether the result will be thoroughly different. To test the robustness and speciﬁcity of our model, a sensitivity analysis is implemented, testing our model with various LCPs and speed limit. The analysis proves that our model does not behave randomly and has good sensitivity.

<!-- b000801 | prose | pages [20] -->
7.1 Choice of the Parameters in LCP

<!-- b000802 | prose | pages [20] -->
The LCP shows the statistical randomness of a car driver’s choice inﬂuenced by his or her psy- chological characteristics to change the lane when the condition permitted. Because the hardness to obtain the accurate LCP, we assume the P21, P22 and P23 as 0.8, 0.4 and 0.1, in our model. By changing the parameters by 15%, our model produces the data of a 3-lane road in the following Tab. 3 which shows that the result will not be changed greatly by the choice of parameters in LCP reﬂecting the robustness of our model.

<!-- b000803 | caption | pages [20] -->
Table 3: the Inﬂuence of the Changing of the Parameters in LCP in 3-lane Road

<!-- b000804 | prose | pages [20] -->
P21 P22 P23 Changing Proportion

<!-- b000805 | prose | pages [20] -->
Origin 80.0% 40.0% 10.0% 0.0% P21 ↑ 92.0% 40.0% 10.0% +15.0% P21 ↓ 68.0% 40.0% 10.0% -15.0% P22 ↑ 80.0% 46.0% 10.0% +15.0% P22 ↓ 80.0% 34.0% 10.0% -15.0% P23 ↑ 80.0% 40.0% 12.0% +15.0% P23 ↓ 80.0% 40.0% 8.0% -15.0%

<!-- b000806 | prose | pages [20] -->
7.2 Different Speed Limit

<!-- b000807 | prose | pages [20] -->
Average Time Deviation of time

<!-- b000808 | prose | pages [20] -->
405.5 0.0% 406.4 +0.22% 405.1 -0.10% 406.8 +0.32% 404.3 -0.30% 407.4 +4.7% 402.3 -7.9%

<!-- b000809 | prose | pages [20] -->
Speed limit is the maximum speed that a vehicle on the road can reach, as we assumed in part 2 of Section 2.2, no exceed speed is allowed. Different speed limit will show the unique character of different roads. In light trafﬁc, the average time it takes for a car passing the roads should be changed by the speed limit. And in Tab. 4, we can ﬁnd that our model performs quite well and shows great speciﬁcity to different kind of road, showing the speciﬁcity of our model.

<!-- b000810 | caption | pages [20] -->
Table 4: the Inﬂuence of the Changing of the Speed Limit

<!-- b000811 | prose | pages [20] -->
the Speed Limit Changing Proportion

<!-- b000812 | prose | pages [20] -->
10 cell/turn(Original) 0.0% 5 cell/turn -50.0% 15 cell/turn +50.0%

<!-- b000813 | prose | pages [20] -->
Average Time(turns) Deviation of Time

<!-- b000814 | prose | pages [20] -->
107.7 0.0% 204.3 +89.7% 79.2 -26.5%

<!-- b000815 | furniture | pages [21] -->
Team # 55585

<!-- b000816 | furniture | pages [21] -->
Page 19 of 34

<!-- b000817 | prose | pages [21] -->
8

<!-- b000818 | heading | pages [21] -->
Conclusions

<!-- b000819 | prose | pages [21] -->
To ﬁnd how the percentage of SDVs impacts on the trafﬁc ﬂow and whether a valid solution exists to increase capacity of highways to the most extent, we formulate a model based on CA with two parts: the Following Model and the Multilane Trafﬁc Model. In the Following Model, we consider the difference between how SDVs and NSDVs gain, decide upon and react to information. Information sharing among SDVs and physiological characteristics of NSDVs are simulated. In the Multilane Trafﬁc Model, when and how SDVs and NSDVs change a lane are discussed thoroughly and many situations in real life are taken into consideration. With the simulation by computers, we conclude some useful features and suggestions:

<!-- b000820 | prose | pages [21] -->
1. Trafﬁc ﬂow becomes larger as the percentage of SDVs grows. Thanks to the short reaction time and the coordination between SDVs, they can make the best choice to run faster. In terms of simulated data, the trafﬁc ﬂow almost triples when all NSDVs are replaced by SDVs.

<!-- b000821 | prose | pages [21] -->
2. Tipping points are found in the relationship of average speed and trafﬁc ﬂow. Equilibria are formed when trafﬁc jam occur. The percentage of SDVs change the position of tipping points and equilibria.

<!-- b000822 | prose | pages [21] -->
3. When the percentage of SDVs comes up to 30%, it is more efﬁcient to increase the capacity of highways to set up an SDV Lane.

<!-- b000823 | prose | pages [21] -->
4. The trafﬁc ﬂow in real life is much larger than the expected one, suggesting a huge lack of trafﬁc capacity. Although the result gained from case of all SDVs can fairly satisfy it, we suggest that the government advocate SDVs.

<!-- b000824 | prose | pages [21] -->
9

<!-- b000825 | heading | pages [21] -->
Strengths and weaknesses

<!-- b000826 | prose | pages [21] -->
9.1

<!-- b000827 | heading | pages [21] -->
Strengths

<!-- b000828 | prose | pages [21] -->
1. The statistical randomness of human mental states and the interactions between SDVs and NSDVs are taken into consideration;

<!-- b000829 | prose | pages [21] -->
2. Following and lane-changing rules are designed fully corresponding to the trafﬁc rules while specially rules are made for SDVs to make full use of the coordination among them;

<!-- b000830 | prose | pages [21] -->
3. Our model is fairly robust to the changes in parameters based on sensitivity analysis, which means a slight change in parameters will not cause a signiﬁcant change in the result;

<!-- b000831 | prose | pages [21] -->
4. The model is capable of simulating the situation in real life. The results also agree with common sense and life experience.

<!-- b000832 | prose | pages [21] -->
9.2

<!-- b000833 | heading | pages [21] -->
Weaknesses

<!-- b000834 | prose | pages [21] -->
1. Some of our assumptions are highly ideal and not very scientiﬁc, such as the length of vehicles and the value of acceleration.

<!-- b000835 | prose | pages [21] -->
2. Factors involved in human judgments may be over-simpliﬁed.

<!-- b000836 | prose | pages [21] -->
3. The speed of a vehicle is discrete in our model and has limitations, which is not closely corre- sponding to the situation in real life.

<!-- b000837 | prose | pages [21] -->
4. We have ignored trafﬁc accidents in this model. Although it happens at a very low rate, the occurrence of the accidents has its own effect on the trafﬁc ﬂow.

<!-- b000838 | furniture | pages [22] -->
Team # 55585

<!-- b000839 | furniture | pages [22] -->
Page 20 of 34

<!-- b000840 | prose | pages [22] -->
10 A Letter

<!-- b000841 | prose | pages [22] -->
To the Governor Ofﬁce of Washington State:

<!-- b000842 | prose | pages [22] -->
Last century witnesses the glory of development in the Great Seattle area as the boom of population, urbanization and the growth of industry bring this area prosperity. However, the increase of trans- portation capacity in this area can no longer keep pace with the de- velopment of the economy, as broadening roads in a developed ur- ban agglomeration is limited, resulting in long delays during peak hours on highways. As the technology of self-driving vehicles is con- tinuously improved at a rapid speed nowadays, there is no wonder that in the near future vehicles with self-driving functions will be put into the market and will soon occupy the road. Considering this trend, our team develop a model showing how self-driving vehicles will change our road network.

<!-- b000843 | prose | pages [22] -->
Our model is based on cellular automata model which was ﬁrst introduced into trafﬁc by Kai Nagel and Michael Schreckenberg in 1992. We make several changes to this model because the interactions between self-driving ones and non-self-driving ones and the cooperations between the self-driving ones must be considered. This model can be divided into two parts: the Following Model and the Multilane Trafﬁc Model.

<!-- b000844 | prose | pages [22] -->
We design the Following Model to simulate how a vehicle behaves when following another one. Self-driving ones’ control system run faster as human beings need time to react. Another difference between them is that the information can be shared among computers but human drivers can only get the information from nearby ones. These features are all considered in our Following Model. In this model, human mind’s psychological characteristics also have inﬂuences. An interesting thing of this model is that a chain of self-driving vehicles can form a train to save time.

<!-- b000845 | prose | pages [22] -->
The Multilane Trafﬁc Model is designed based on the Following Model. In this model, we add features of lane-changing and overtaking. The motivation to change a lane and the safety of this action are carefully considered. With lane-changing, a train of pure self-driving vehicles is easier to form. However, changing lanes interferes the trafﬁc ﬂow and its inﬂuence is complicated.

<!-- b000846 | prose | pages [22] -->
After building and improving our models, we write programs to simulate it. We ﬁnd strong connections among the average speed, the trafﬁc ﬂow and the percentage of self-driving vehicles, showing that auto systems do beneﬁt our society. We think the state should invest more in tech- nology companies especially in those developing self-driving technology. Researches on this should also be supported and funded by the state government.

<!-- b000847 | prose | pages [22] -->
After comparing the data with the real world, we ﬁnd that the Great Seattle area really suffers from the lack of trafﬁc capacity. Almost all parts of the roads are not wide enough for transportation needs, suggesting that overspeed and the neglect of safe following distance occur frequently. As the ﬁgure shows, although self-driving technology can triple the capacity, some of roads will still be jammed. The widening of highways or redesigning of the road-network in these area is an urgency for the state.

<!-- b000848 | prose | pages [22] -->
Another result we obtained from this model is when and how we should set lanes dedicated to self-driving ones. According to our data, we suggest that a special lane only for self-driving vehicles should be set up when more than 30% of vehicles running on the highway are equipped with welf- driving systems.

<!-- b000849 | prose | pages [22] -->
We hope our model can help you understand the inﬂuence of self-driving vehicles on the trafﬁc ﬂow. We believe the trafﬁc conditions in Washington State will become better after the introduction of scientiﬁc and longtime policies. For more details please read our paper.

<!-- b000850 | prose | pages [22] -->
Yours sincerely

<!-- b000851 | furniture | pages [22] -->
Team #55585

<!-- b000852 | furniture | pages [23] -->
Team # 55585

<!-- b000853 | furniture | pages [23] -->
Page 21 of 34

<!-- b000854 | prose | pages [23] -->
Reference

<!-- b000855 | prose | pages [23] -->
[1] H. T. Ofﬁcials and A. A. O. S. H. Ofﬁcials, “A policy on geometric design of highways and

<!-- b000856 | prose | pages [23] -->
streets, 1994,” 2001.

<!-- b000857 | prose | pages [23] -->
[2] th., “Reaction time of drivers to road stimuli.,” Drivers, 1982.

<!-- b000858 | prose | pages [23] -->
[3] V. Bond and A. Thurlow, “Sae panel: Will people trust self-driving cars?,” Automotive News,

<!-- b000859 | prose | pages [23] -->
2013.

<!-- b000860 | prose | pages [23] -->
[4] M. Treiber and A. Kesting, The LighthillWhithamRichards Model.

<!-- b000861 | prose | pages [23] -->
Springer Berlin Heidelberg, 2013.

<!-- b000862 | prose | pages [23] -->
[5] S. Wolfram and A. J. Mallinckrodt, “Cellular automata and complexity,” Computers in Physics,

<!-- b000863 | prose | pages [23] -->
vol. 9, no. 1, p. 55, 1995.

<!-- b000864 | prose | pages [23] -->
[6] N. Kai and M. Schreckenberg, “A cellular automaton model for freeway trafﬁc,” Journal of

<!-- b000865 | prose | pages [23] -->
Physics I France, vol. 2, no. 12, pp. 2221–2229, 1992.

<!-- b000866 | prose | pages [23] -->
[7] W. Knospe, A. Schadschneider, M. Schreckenberg, and L. Santen, “Towards a realistic micro-

<!-- b000867 | prose | pages [23] -->
scopic description of highway trafﬁc,” Journal of Physics A General Physics, vol. 33, no. 48, p. L477, 2000.

<!-- b000868 | prose | pages [23] -->
[8] G. Hong-xia, The dynamical characteristics and nonlinear density waves with consideration of naviga-

<!-- b000869 | prose | pages [23] -->
tion. PhD thesis, Shanghai University, 2006.

<!-- b000870 | prose | pages [23] -->
[9] J. C. Deutsch, C. R. Santhosh-Kumar, M. Rickert, K. Nagel, M. Schreckenberg, and A. Latour,

<!-- b000871 | prose | pages [23] -->
“Two lane trafﬁc simulations using cellular automata,” Physica A Statistical Mechanics & Its Ap- plications, vol. 231, no. 4, pp. 534–550, 1995.

<!-- b000872 | prose | pages [23] -->
[10] L. G. Jaeger and B. Bakht, “Multiple presence reduction factors for bridges,” in Bridges and

<!-- b000873 | prose | pages [23] -->
Transmission Line Structures, 2015.

<!-- b000874 | furniture | pages [24] -->
Team # 55585

<!-- b000875 | furniture | pages [24] -->
Page 22 of 34

<!-- b000876 | heading | pages [24] -->
Appendices

<!-- b000877 | heading | pages [24] -->
Appendix A: Matlab Program for Visualization

<!-- b000878 | prose | pages [24] -->
clear all clc hold on; grid on; A=importdata(’data.txt’); r=A(:,1); s=A(:,2); e=A(:,3); f=A(:,4); l1=A(:,5); l2=A(:,6); f1=f/(l1+l2)*l1/24; f2=f/(l1+l2)*l2/24;

<!-- b000879 | prose | pages [24] -->
B=importdata(’1st_res_lane1.txt’); d(:,1)=B(:,1); B=importdata(’1st_res_lane2.txt’); d(:,2)=B(:,1); B=importdata(’1st_res_lane3.txt’); d(:,3)=B(:,1); B=importdata(’1st_res_lane4.txt’); d(:,4)=B(:,1); B=importdata(’1st_res_lane5.txt’); d(:,5)=B(:,1);

<!-- b000880 | prose | pages [24] -->
d(:,:)=d(:,:)/(1000*1.5)*3600; road(:)=[90 405 520]; length(:)=[25 30 13]; for mi=1:2

<!-- b000881 | prose | pages [24] -->
for mj=1:3

<!-- b000882 | prose | pages [24] -->
c=0; clear m md gca; for i=1:1:224

<!-- b000883 | prose | pages [24] -->
if (r(i)==road(mj))

<!-- b000884 | prose | pages [24] -->
for t=s(i):0.1:e(i)

<!-- b000885 | prose | pages [24] -->
c=c+1; m(c,1)=t; if mi==1

<!-- b000886 | prose | pages [24] -->
m(c,2)=f1(i); else

<!-- b000887 | prose | pages [24] -->
m(c,2)=f2(i); end for p=0:2:100

<!-- b000888 | prose | pages [24] -->
if mi==1

<!-- b000889 | prose | pages [24] -->
md(c,p+1)=d((100-p)/2+1,l1(i)); else

<!-- b000890 | prose | pages [24] -->
md(c,p+1)=d((100-p)/2+1,l2(i)); end end end end end subplot(2,3,(mi-1)*3+mj); hold on;

<!-- b000891 | prose | pages [24] -->
set( gca, ’xLim’,[0, length(mj)]);

<!-- b000892 | furniture | pages [25] -->
Team # 55585

<!-- b000893 | furniture | pages [25] -->
Page 23 of 34

<!-- b000894 | prose | pages [25] -->
plot(m(:,1),m(:,2),’k-’,’LineWidth’,1.2);

<!-- b000895 | prose | pages [25] -->
plot(m(:,1),md(:,100+1),’g-’); plot(m(:,1),md(:,50+1),’b-’); plot(m(:,1),md(:,0+1),’r-’);

<!-- b000896 | prose | pages [25] -->
if (mj==1)&(mi==1)

<!-- b000897 | prose | pages [25] -->
ylabel(’DECR’, ’Fontsize’, 14); end if (mj==1)&(mi==2)

<!-- b000898 | prose | pages [25] -->
ylabel(’INCR’, ’Fontsize’, 14); end if (mi==2)&(mj==1)

<!-- b000899 | prose | pages [25] -->
xlabel(’Interstate 90’, ’Fontsize’, 14); end if (mi==2)&(mj==2)

<!-- b000900 | prose | pages [25] -->
xlabel(’Interstate 405’, ’Fontsize’, 14); end if (mi==2)&(mj==3)

<!-- b000901 | prose | pages [25] -->
xlabel(’State Route 520’, ’Fontsize’, 14); end end end

<!-- b000902 | heading | pages [25] -->
Appendix B: C++ Program for Simulation

<!-- b000903 | prose | pages [25] -->
/* *================================================================ *Multi-lane model with change lane simulation *Using cell automata and certain rules *The situation of the Lanes or statistic collection *22-1-2016 *================================================================ */

<!-- b000904 | prose | pages [25] -->
#include <iostream> #include <fstream>

<!-- b000905 | heading | pages [25] -->
#include <algorithm>

<!-- b000906 | prose | pages [25] -->
#include <random> #include <ctime> #include <fstream> using namespace std;

<!-- b000907 | prose | pages [25] -->
//Switch button of output lanes/collect data //#define output_lanes #define statistic_collect

<!-- b000908 | prose | pages [25] -->
//Error class class Cannot_produce_car {};

<!-- b000909 | prose | pages [25] -->
ofstream out; ofstream crash("crash_msg");

<!-- b000910 | prose | pages [25] -->
const int dedicated_lane = 0; int *tempremain; int safe_space_max[11], safe_space_min[11], appear = 1, safe_space_maxax, total_time; int road_length = 1000; int lane_num = 3; int p1, p2, p3,cp1,cp2,cp3; int appear_speed_low, appear_speed_high, kindpossibility;

<!-- b000911 | prose | pages [25] -->
//Class of every cell in the CA Model class Cars {

<!-- b000912 | prose | pages [25] -->
friend istream & operator >> (istream & is, Cars & rc) {

<!-- b000913 | furniture | pages [26] -->
Team # 55585

<!-- b000914 | furniture | pages [26] -->
Page 24 of 34

<!-- b000915 | prose | pages [26] -->
is >> rc.kind >> rc.speed; return is; } friend ostream & operator << (ostream & os, Cars & rc) {

<!-- b000916 | prose | pages [26] -->
//os << "(" << rc.kind << ", " << rc.speed << ")"; os << rc.kind; return os; } public:

<!-- b000917 | prose | pages [26] -->
int speed; int kind;//0:no car, 1:non_self_driving, 2:self_driving int light; int timer; int turning_light; Cars(int _speed = 0, int _kind = 0, int _light = 0, int _timer = 0,int _turning = 0) :speed(_speed), kind(_kind), light(_light), timer(_timer), turning_light(_turning) {}

<!-- b000918 | prose | pages [26] -->
}; Cars **roadnew, **roadold;

<!-- b000919 | prose | pages [26] -->
void initialize() {

<!-- b000920 | prose | pages [26] -->
//initialize cout << "Please input the total time:" << endl; cout << "Please input the number of lanes" << endl; cout << "Please input the length of the road: " << endl; cout << "Please input the min/max safe_space of every speed:" << endl; cout << "Please input the possibility appearance of the cars and the possibility of the car to be a non-self-driving car: possibility(0-100), speedrange(0-10), kindpossibility(0-100)" << endl; cout << "Please input the possibility of p1 p2 p3:(0-100) " << endl; cout << "Please input the change lane possibility cp1 cp2 cp3:(0-100)" << endl; //cout << "Do we need to initialize the road?[y/n]" << endl; //cout << "If yes, please input the initialization:[kind(0-2) speed(0-10)](example 1 2 0 0 7 1)" << endl; system("pause"); cout << "Make sure that you have closed the in.in file" << endl; system("pause");

<!-- b000921 | prose | pages [26] -->
ifstream in("in.in");

<!-- b000922 | prose | pages [26] -->
in >> total_time; clog << total_time << endl; out << "total_time = " << total_time << endl; in >> lane_num >> road_length; clog << lane_num << " " << road_length << endl; out << "lane_num = "<< lane_num << " " << "road_length = " << road_length << endl;

<!-- b000923 | prose | pages [26] -->
for (int i = 0; i != 11; ++i) {

<!-- b000924 | prose | pages [26] -->
in >> safe_space_min[i] >> safe_space_max[i]; clog << safe_space_min[i] << " " << safe_space_max[i] << endl; }

<!-- b000925 | prose | pages [26] -->
in >> appear >> kindpossibility; clog << appear << " " << kindpossibility << endl;

<!-- b000926 | prose | pages [26] -->
in >> p1 >> p2 >> p3; clog << p1 << " " << p2 << " " << p3 << endl;

<!-- b000927 | prose | pages [26] -->
in >> cp1 >> cp2 >> cp3; clog << cp1 << " " << cp2 << " " << cp3 << endl;

<!-- b000928 | prose | pages [26] -->
/*char c; in >> c; clog << c << endl;

<!-- b000929 | furniture | pages [27] -->
Team # 55585

<!-- b000930 | furniture | pages [27] -->
Page 25 of 34

<!-- b000931 | prose | pages [27] -->
if (c == ’Y’ || c == ’y’) {

<!-- b000932 | prose | pages [27] -->
for (int i = 0; i != road_length; ++i) in >> roadold[i]; }*/ }

<!-- b000933 | prose | pages [27] -->
//Find the car exactly ahead of the car input inline int direction_cal(int aimlane, int num, Cars **r) {

<!-- b000934 | prose | pages [27] -->
for (int t = num + 1; t != road_length; ++t) {

<!-- b000935 | prose | pages [27] -->
if (r[aimlane][t].kind) return t; } return 2 * road_length; }

<!-- b000936 | prose | pages [27] -->
//Clear up the array of roadnew inline void clearup() {

<!-- b000937 | prose | pages [27] -->
for (int i = 0; i != lane_num; ++i)

<!-- b000938 | prose | pages [27] -->
for (int j = 0; j != road_length; ++j)

<!-- b000939 | prose | pages [27] -->
roadnew[i][j] = Cars(); }

<!-- b000940 | prose | pages [27] -->
//Find the first car of a SDV-Train int findthefirst(int aimlane, int num) {

<!-- b000941 | prose | pages [27] -->
int first = 2 * road_length; for (int i = num + 1; i != road_length; ++i) {

<!-- b000942 | prose | pages [27] -->
if (roadold[aimlane][i].kind == 2) first = i; else if (roadold[aimlane][i].kind == 1) break; } return first; }

<!-- b000943 | prose | pages [27] -->
//Find the car exactly behind the car input int findnext(int aimlane, int num) {

<!-- b000944 | prose | pages [27] -->
for (int i = num - 1; i >= 0; --i) {

<!-- b000945 | prose | pages [27] -->
if (roadold[aimlane][i].kind != 0) return i; } return 0; }

<!-- b000946 | prose | pages [27] -->
//Judge the number input inline int iscar(int lane, int num) {

<!-- b000947 | prose | pages [27] -->
if (num >= road_length) return 0; else return roadold[lane][num].kind; }

<!-- b000948 | prose | pages [27] -->
//Produce a car at the beginning of the road, according to the appearing rate and the possibility of the kind of the cars void produce() {

<!-- b000949 | prose | pages [27] -->
int kind; int able = 0;

<!-- b000950 | prose | pages [27] -->
for (able = 0; able < lane_num; ++able) {

<!-- b000951 | prose | pages [27] -->
if (appear >= (rand() + 301) % 301) {

<!-- b000952 | prose | pages [27] -->
if(dedicated_lane == 0) kind = (kindpossibility >= (rand() + 101) % 101) ? 1 : 2 ; else {

<!-- b000953 | prose | pages [27] -->
if (able < lane_num - dedicated_lane && kindpossibility < rand() % 101)

<!-- b000954 | prose | pages [27] -->
continue; if (able >= lane_num - dedicated_lane && kindpossibility >= rand() % 101) continue;

<!-- b000955 | prose | pages [27] -->
kind = (able <= lane_num - dedicated_lane) ? 1 : 2; }

<!-- b000956 | prose | pages [27] -->
//The tempremain array ensures the possibility of the kind of the car that is produced at the beginning if (tempremain[able]==0) tempremain[able] = kind; kind = tempremain[able];

<!-- b000957 | furniture | pages [28] -->
Team # 55585

<!-- b000958 | furniture | pages [28] -->
Page 26 of 34

<!-- b000959 | prose | pages [28] -->
if (roadold[able][0].kind == 0) {

<!-- b000960 | prose | pages [28] -->
int thislane = able; int find = direction_cal(thislane, 0, roadold); int speed_up_bound = 0;

<!-- b000961 | prose | pages [28] -->
if (find > road_length) speed_up_bound = 11; else if (kind == 1) {

<!-- b000962 | prose | pages [28] -->
for (speed_up_bound = 0; speed_up_bound <= 10; ++speed_up_bound) {

<!-- b000963 | prose | pages [28] -->
if (find < safe_space_min[speed_up_bound]) break; } } else if (roadold[thislane][find].kind == 1) {

<!-- b000964 | prose | pages [28] -->
for (speed_up_bound = 0; speed_up_bound <= 10; ++speed_up_bound) {

<!-- b000965 | prose | pages [28] -->
if (find < safe_space_min[speed_up_bound]) break; } } else if (roadold[thislane][find].kind == 2) {

<!-- b000966 | prose | pages [28] -->
for (speed_up_bound = 0; speed_up_bound <= 10; ++speed_up_bound) {

<!-- b000967 | prose | pages [28] -->
if (find < safe_space_min[speed_up_bound] - safe_space_min[roadold[ thislane][find].speed] + 2 * roadold[thislane][find].speed + 1) break; } }

<!-- b000968 | prose | pages [28] -->
if (speed_up_bound <= 0) continue; else {

<!-- b000969 | prose | pages [28] -->
tempremain[able] = 0; int speed = (rand() + speed_up_bound) % speed_up_bound; if (speed > 0) --speed; roadold[thislane][0].kind = kind; roadold[thislane][0].speed = speed; roadold[thislane][0].light = 0; roadold[thislane][0].timer = 1; } } } }

<!-- b000970 | prose | pages [28] -->
}

<!-- b000971 | prose | pages [28] -->
//Get the value of LCS bool change_lane_safety(int nowlane, int aimlane, int num, Cars**r) {

<!-- b000972 | prose | pages [28] -->
bool ans = false; int kind = r[nowlane][num].kind, speed = r[nowlane][num].speed; int light = 0; int turning_light = r[nowlane][num].turning_light; int find = direction_cal(nowlane, num, r); int delta = find - num; int next = findnext(nowlane, num); int aimlaneahead = direction_cal(aimlane, num-1, r); int aimlanenext = findnext(aimlane, num+1);

<!-- b000973 | prose | pages [28] -->
if (kind == 1){

<!-- b000974 | prose | pages [28] -->
if (delta >= safe_space_min[speed] && aimlaneahead - num >= safe_space_min[speed]

<!-- b000975 | prose | pages [28] -->
&& num - aimlanenext >= safe_space_min[r[aimlane][aimlanenext].speed]) { if (r[nowlane][next].turning_light != aimlane - nowlane) {

<!-- b000976 | prose | pages [28] -->
ans = true; } else ans = false; } } else if (kind == 2) {

<!-- b000977 | prose | pages [28] -->
bool t1 = false, t2 = false, t3 = false; if (!iscar(nowlane, find)) t1 = true; else if (iscar(nowlane, find) == 1) {

<!-- b000978 | furniture | pages [29] -->
Team # 55585

<!-- b000979 | furniture | pages [29] -->
Page 27 of 34

<!-- b000980 | prose | pages [29] -->
t1 = (delta >= safe_space_min[speed]) ? true : false; } else {

<!-- b000981 | prose | pages [29] -->
t1 = (delta >= safe_space_min[speed] - safe_space_min[r[nowlane][find].speed] + 1 + 2 * r[nowlane][find].speed) ? true : false; } if (!iscar(aimlane, aimlaneahead)) t2 = true; else if (iscar(aimlane, aimlaneahead) == 1) {

<!-- b000982 | prose | pages [29] -->
t2 = (aimlaneahead - num >= safe_space_min[speed]) ? true : false; } else {

<!-- b000983 | prose | pages [29] -->
t2 = (aimlaneahead - num >= safe_space_min[speed] - safe_space_min[r[aimlane][ aimlaneahead].speed] + 2 * r[aimlane][aimlaneahead].speed + 1) ? true : false; } if (!iscar(aimlane, aimlanenext)) t3 = true; else if (iscar(aimlane, aimlanenext) == 1) {

<!-- b000984 | prose | pages [29] -->
t3 = (num - aimlanenext >= safe_space_min[r[aimlane][aimlanenext].speed]) ? true : false; } else {

<!-- b000985 | prose | pages [29] -->
t3 = (num - aimlanenext >= safe_space_min[r[aimlane][aimlanenext].speed] - safe_space_min[speed] + 2 * speed + 1) ? true : false; } if (t1 && t2 && t3) ans = true; } return ans; }

<!-- b000986 | prose | pages [29] -->
//Get the value of LCM bool change_lane_motivation(int nowlane, int aimlane, int num, Cars **r) {

<!-- b000987 | prose | pages [29] -->
//No car can change lane to the dedicated lane for SDVs if (aimlane >= lane_num - dedicated_lane) return false;

<!-- b000988 | prose | pages [29] -->
int kind = r[nowlane][num].kind, speed = r[nowlane][num].speed; int light = 0; int turning_light = r[nowlane][num].turning_light; int find = direction_cal(nowlane,num, r); int delta = find - num; int aimlaneahead = direction_cal(aimlane, num, r);

<!-- b000989 | prose | pages [29] -->
if (delta > safe_space_max[speed]) return false; if (kind == 1) {

<!-- b000990 | prose | pages [29] -->
if ((aimlaneahead > safe_space_max[speed] || r[aimlane][aimlaneahead].speed >= speed) &&

<!-- b000991 | prose | pages [29] -->
r[nowlane][find].speed < speed) return true; return false; } else {

<!-- b000992 | prose | pages [29] -->
if (r[nowlane][find].kind == 1) {

<!-- b000993 | prose | pages [29] -->
if ((aimlaneahead > safe_space_max[speed] || r[aimlane][aimlaneahead].speed >= speed) &&

<!-- b000994 | prose | pages [29] -->
r[nowlane][find].speed < speed) return true; return false; } else {

<!-- b000995 | prose | pages [29] -->
if (r[nowlane][find].turning_light == aimlane - nowlane) {

<!-- b000996 | prose | pages [29] -->
return true; } else return false; } } }

<!-- b000997 | prose | pages [29] -->
//Whether a car is on the road inline bool validlane(int lane) {

<!-- b000998 | prose | pages [29] -->
return (lane >= 0 && lane < lane_num);

<!-- b000999 | furniture | pages [30] -->
Team # 55585

<!-- b001000 | furniture | pages [30] -->
Page 28 of 34

<!-- b001001 | prose | pages [30] -->
}

<!-- b001002 | prose | pages [30] -->
//The main function of this program int main() {

<!-- b001003 | prose | pages [30] -->
//Get a seed for the random function srand(time(NULL));

<!-- b001004 | prose | pages [30] -->
//Initialize the data by the input in the file in.in initialize();

<!-- b001005 | prose | pages [30] -->
#ifdef output_lanes

<!-- b001006 | prose | pages [30] -->
out.open("lanes.txt"); #endif // output_lanes

<!-- b001007 | prose | pages [30] -->
//simulate //0:no car, 1:non_self_driving, 2:self_driving //Light : -1 means slow down, 0 means hold, 1 means spead up out << "kind: 0 is no car, 1 is non-self-driving car, 2 is self-driving car" << endl; out << "total number of passing car \t possibility of kind \t average time " << endl;

<!-- b001008 | prose | pages [30] -->
#ifdef statistic_collect

<!-- b001009 | prose | pages [30] -->
//Collect the data of different lane number, appearing possibility and possibility of kind for (lane_num = 4; lane_num <= 5; ++lane_num) {

<!-- b001010 | prose | pages [30] -->
switch (lane_num) { case 1:

<!-- b001011 | prose | pages [30] -->
out.open("1.txt"); break; case 2:

<!-- b001012 | prose | pages [30] -->
out.open("2.txt"); break; case 3:

<!-- b001013 | prose | pages [30] -->
out.open("3.txt"); break; case 4:

<!-- b001014 | prose | pages [30] -->
out.open("4.txt"); break; case 5:

<!-- b001015 | prose | pages [30] -->
out.open("5.txt"); break; }

<!-- b001016 | prose | pages [30] -->
roadnew = new Cars*[lane_num]; roadold = new Cars*[lane_num]; for (int i = 0; i != lane_num; ++i) {

<!-- b001017 | prose | pages [30] -->
roadnew[i] = new Cars[road_length]; roadold[i] = new Cars[road_length]; }

<!-- b001018 | prose | pages [30] -->
for (int changeappear = 6; changeappear <= 300; changeappear += 6) {

<!-- b001019 | prose | pages [30] -->
for (int changekindpossibility = 0; changekindpossibility <= 100; changekindpossibility += 2) {

<!-- b001020 | prose | pages [30] -->
appear = changeappear; kindpossibility = changekindpossibility;

<!-- b001021 | prose | pages [30] -->
clog << "appear = " << appear << "\tkindpossibility = " << kindpossibility << endl;

<!-- b001022 | prose | pages [30] -->
for (int tot = 0; tot < 6; ++tot) {

<!-- b001023 | prose | pages [30] -->
clog << "tot = " << tot << endl; #endif // statistic_collect

<!-- b001024 | prose | pages [30] -->
#ifdef output_lanes

<!-- b001025 | prose | pages [30] -->
roadnew = new Cars*[lane_num];

<!-- b001026 | furniture | pages [31] -->
Team # 55585

<!-- b001027 | furniture | pages [31] -->
Page 29 of 34

<!-- b001028 | prose | pages [31] -->
roadold = new Cars*[lane_num]; for (int i = 0; i != lane_num; ++i) {

<!-- b001029 | prose | pages [31] -->
roadnew[i] = new Cars[road_length]; roadold[i] = new Cars[road_length]; } #endif // output_lanes

<!-- b001030 | prose | pages [31] -->
tempremain = new int[lane_num];

<!-- b001031 | prose | pages [31] -->
for (int i = 0; i != lane_num; ++i) {

<!-- b001032 | prose | pages [31] -->
tempremain[i] = 0; }

<!-- b001033 | prose | pages [31] -->
int cnt_car = 0; double timer_all = 0;

<!-- b001034 | prose | pages [31] -->
for (int i = 0; i != total_time; ++i) {

<!-- b001035 | prose | pages [31] -->
//clear up roadnew clearup();

<!-- b001036 | prose | pages [31] -->
//Produce new cars on 0 position of each lane produce();

<!-- b001037 | prose | pages [31] -->
#ifdef output_lanes

<!-- b001038 | prose | pages [31] -->
for (int nowlane1 = 0; nowlane1 < lane_num; ++nowlane1) {

<!-- b001039 | prose | pages [31] -->
for (int t = 0; t != road_length; ++t) {

<!-- b001040 | prose | pages [31] -->
out << roadold[nowlane1][t] << "\t"; } out << endl; } out << endl; #endif // output_lanes

<!-- b001041 | prose | pages [31] -->
//Change the speed, and turnning light of all the cars on the road for (int change_lane = 0; change_lane < lane_num; ++change_lane) {

<!-- b001042 | prose | pages [31] -->
for (int j = road_length - 1; j >= 0; --j) {

<!-- b001043 | prose | pages [31] -->
int kind = roadold[change_lane][j].kind, speed = roadold[change_lane][j].speed; int light = 0; int find = direction_cal(change_lane, j, roadold); int delta = find - j; int timer = roadold[change_lane][j].timer; int turning_light = roadold[change_lane][j].turning_light;

<!-- b001044 | prose | pages [31] -->
//The situation of empty cell if (kind == 0) roadnew[change_lane][j] = roadold[change_lane][j]; //The situation of NSDVs else if (kind == 1) {

<!-- b001045 | prose | pages [31] -->
++timer; int possibility;

<!-- b001046 | prose | pages [31] -->
if (delta > road_length) possibility = 0; else if (safe_space_min[speed] <= delta && roadold[change_lane][find].light == -1 && delta < safe_space_max[speed]) possibility = p1; else if (safe_space_min[speed] <= delta && roadold[change_lane][find].light >= 0 && delta < safe_space_max[speed]) possibility = p2; else if (speed == 0) possibility = p3; else possibility = 0;

<!-- b001047 | prose | pages [31] -->
//Change the turning light if (turning_light == 0) {

<!-- b001048 | prose | pages [31] -->
for (int changeto = change_lane - 1; changeto <= change_lane + 1; changeto += 2) {

<!-- b001049 | furniture | pages [32] -->
Team # 55585

<!-- b001050 | furniture | pages [32] -->
Page 30 of 34

<!-- b001051 | prose | pages [32] -->
if (!validlane(changeto)) continue;

<!-- b001052 | prose | pages [32] -->
bool lcm = change_lane_motivation(change_lane, changeto, j, roadold), lcs = change_lane_safety(change_lane, changeto, j, roadold);

<!-- b001053 | prose | pages [32] -->
if (lcm && lcs) {

<!-- b001054 | prose | pages [32] -->
turning_light = changeto - change_lane; int next = findnext(change_lane, j); if (kind == 2) {

<!-- b001055 | prose | pages [32] -->
if (roadold[change_lane][next].kind == 2) {

<!-- b001056 | prose | pages [32] -->
roadold[change_lane][j].turning_light = turning_light; } } } } }

<!-- b001057 | prose | pages [32] -->
//Change the speed of NSDVs if (delta > road_length) {

<!-- b001058 | prose | pages [32] -->
if (speed < 10) ++speed; light = 1; } else if (possibility >= ((rand() + 101) % 101)

<!-- b001059 | prose | pages [32] -->
|| delta < safe_space_min[speed]) { if (speed > 0) --speed; light = -1; } else if (delta > safe_space_max[speed] || (!roadold[change_lane][find].light && delta > safe_space_min[speed])) {

<!-- b001060 | prose | pages [32] -->
if (speed < 10) ++speed; light = 1; } else if (delta == safe_space_min[speed]) {

<!-- b001061 | prose | pages [32] -->
light = 0; } //Output the crashing information if (j + speed < road_length && roadnew[change_lane][j + speed].kind != 0) {

<!-- b001062 | prose | pages [32] -->
cerr << "non-self-driving car crash on sth when i = " << i << " j = " << j << endl; crash << "appear = " << appear << " kindpossibility = " << kindpossibility

<!-- b001063 | prose | pages [32] -->
<< " time = " << i << " lane = " << change_lane << " j = " << j << " non-self-driving car crash on kind = " << roadnew[change_lane][j + speed].kind << endl; }

<!-- b001064 | prose | pages [32] -->
roadnew[change_lane][j] = Cars();

<!-- b001065 | prose | pages [32] -->
if (j + speed >= road_length) {

<!-- b001066 | prose | pages [32] -->
++cnt_car; timer_all += timer; } if (j + speed < road_length) {

<!-- b001067 | prose | pages [32] -->
if (speed == 0) light = -1; roadnew[change_lane][j + speed] = Cars(speed, kind, light, timer, turning_light); } } //The situation of SDVs else if (kind == 2) {

<!-- b001068 | prose | pages [32] -->
++timer; int next = findnext(change_lane, j); if (turning_light == 0) {

<!-- b001069 | prose | pages [32] -->
for (int changeto = change_lane - 1;

<!-- b001070 | furniture | pages [33] -->
Team # 55585

<!-- b001071 | furniture | pages [33] -->
Page 31 of 34

<!-- b001072 | prose | pages [33] -->
changeto <= change_lane + 1; changeto += 2) {

<!-- b001073 | prose | pages [33] -->
if (!validlane(changeto)) continue; bool lcm = change_lane_motivation(change_lane, changeto, j, roadold), lcs = change_lane_safety(change_lane, changeto, j, roadold); if (lcm && lcs) {

<!-- b001074 | prose | pages [33] -->
turning_light = changeto - change_lane; int next = findnext(change_lane, j); if (kind == 2) {

<!-- b001075 | prose | pages [33] -->
if (roadold[change_lane][next].kind == 2) {

<!-- b001076 | prose | pages [33] -->
roadold[change_lane][j].turning_light = turning_light; } } } } }

<!-- b001077 | prose | pages [33] -->
//Change the speed of SDVs if (delta > road_length) {

<!-- b001078 | prose | pages [33] -->
if (speed < 10) ++speed; light = 1; if (roadold[change_lane][next].kind == 2) {

<!-- b001079 | prose | pages [33] -->
roadold[change_lane][j].light = 1; } } else if (roadold[change_lane][find].kind == 1) {

<!-- b001080 | prose | pages [33] -->
if (delta > safe_space_min[speed]) {

<!-- b001081 | prose | pages [33] -->
if (speed < 10)++speed; light = 1; if (roadold[change_lane][next].kind == 2) {

<!-- b001082 | prose | pages [33] -->
roadold[change_lane][j].light = 1; } } else if (delta < safe_space_min[speed]) {

<!-- b001083 | prose | pages [33] -->
if (speed > 0) --speed; light = -1; if (roadold[change_lane][next].kind == 2) {

<!-- b001084 | prose | pages [33] -->
roadold[change_lane][j].light = -1; } } else {

<!-- b001085 | prose | pages [33] -->
light = 0; if (roadold[change_lane][next].kind == 2) {

<!-- b001086 | prose | pages [33] -->
roadold[change_lane][j].light = 0; } } } else if (roadold[change_lane][find].kind == 2) {

<!-- b001087 | prose | pages [33] -->
int first = findthefirst(change_lane, j); if (delta > safe_space_min[speed] - safe_space_min[roadold[change_lane][find].speed] + 2 * roadold[change_lane][find].speed + 1) {

<!-- b001088 | prose | pages [33] -->
if (speed < 10)++speed; light = 1; if (roadold[change_lane][next].kind == 2) {

<!-- b001089 | prose | pages [33] -->
roadold[change_lane][j].light = 1; } } else if (delta == safe_space_min[speed] - safe_space_min[roadold[change_lane][find].speed] + 2 * roadold[change_lane][find].speed + 1) {

<!-- b001090 | prose | pages [33] -->
if (roadold[change_lane][find].light == 1) {

<!-- b001091 | prose | pages [33] -->
if (speed < 10) ++speed; light = 1; if (roadold[change_lane][next].kind == 2) {

<!-- b001092 | prose | pages [33] -->
roadold[change_lane][j].light = 1; }

<!-- b001093 | furniture | pages [34] -->
Team # 55585

<!-- b001094 | furniture | pages [34] -->
Page 32 of 34

<!-- b001095 | prose | pages [34] -->
} else if (roadold[change_lane][find].light == 0) {

<!-- b001096 | prose | pages [34] -->
light = 0; if (roadold[change_lane][next].kind == 2) {

<!-- b001097 | prose | pages [34] -->
roadold[change_lane][j].light = 0; } } else {

<!-- b001098 | prose | pages [34] -->
if (speed > 0) --speed; light = -1; if (roadold[change_lane][next].kind == 2) {

<!-- b001099 | prose | pages [34] -->
roadold[change_lane][j].light = -1; } } } else {

<!-- b001100 | prose | pages [34] -->
if (speed > 0) --speed; light = -1; if (roadold[change_lane][next].kind == 2) {

<!-- b001101 | prose | pages [34] -->
roadold[change_lane][j].light = -1; } } } //Output the crashing information if (j + speed < road_length && roadnew[change_lane][j + speed].kind != 0) {

<!-- b001102 | prose | pages [34] -->
cerr << "self-driving car crash on sth when i = " << i << " and j = " << j << endl; crash << "appear = " << appear << " kindpossibility = " << kindpossibility

<!-- b001103 | prose | pages [34] -->
<< " time = " << i << " lane = " << change_lane << " j = " << j << " self-driving car crash on kind = " << roadnew[change_lane][j + speed].kind; }

<!-- b001104 | prose | pages [34] -->
roadnew[change_lane][j] = Cars();

<!-- b001105 | prose | pages [34] -->
if (j + speed >= road_length) {

<!-- b001106 | prose | pages [34] -->
++cnt_car; timer_all += timer; } if (j + speed < road_length) {

<!-- b001107 | prose | pages [34] -->
if (speed == 0) light = -1; roadnew[change_lane][j + speed] = Cars(speed, kind, light, timer, turning_light); } }

<!-- b001108 | prose | pages [34] -->
} }

<!-- b001109 | prose | pages [34] -->
//Change lane for (int change_lane = 0; change_lane < lane_num - dedicated_lane; ++change_lane) {

<!-- b001110 | prose | pages [34] -->
for (int j = road_length - 1; j >= 0; --j) {

<!-- b001111 | prose | pages [34] -->
int kind = roadnew[change_lane][j].kind, speed = roadnew[change_lane][j].speed; int light = 0; int find = direction_cal(change_lane, j, roadnew); int delta = find - j; int turning_light = roadnew[change_lane][j].turning_light;

<!-- b001112 | prose | pages [34] -->
if (kind != 0) {

<!-- b001113 | prose | pages [34] -->
if (turning_light != 0) {

<!-- b001114 | prose | pages [34] -->
int changepossibility = 0;

<!-- b001115 | furniture | pages [35] -->
Team # 55585

<!-- b001116 | furniture | pages [35] -->
Page 33 of 34

<!-- b001117 | prose | pages [35] -->
//Initialize the possibility of changing lane if (find >= road_length) changepossibility = 0; else if (safe_space_min[speed] <= delta && roadnew[change_lane][find].light == -1 && delta < safe_space_max[speed]) changepossibility = cp1; else if (safe_space_min[speed] <= delta && roadnew[change_lane][find].light >= 0 && delta < safe_space_max[speed]) changepossibility = cp2; else if (speed == 0) changepossibility = cp3; else changepossibility = 0;

<!-- b001118 | prose | pages [35] -->
if (change_lane_motivation(change_lane, change_lane + turning_light, j, roadnew) && change_lane_safety(change_lane, change_lane + turning_light, j, roadnew)) {

<!-- b001119 | prose | pages [35] -->
if (roadnew[change_lane + turning_light][j].kind != 0); // cerr << "change_lane crash" << endl; else {

<!-- b001120 | prose | pages [35] -->
if (kind == 1 && changepossibility < (rand() % 101))

<!-- b001121 | prose | pages [35] -->
continue; roadnew[change_lane + turning_light][j] = roadnew[change_lane][j]; roadnew[change_lane + turning_light][j].turning_light = 0; roadnew[change_lane][j] = Cars(); #ifdef output_lanes

<!-- b001122 | prose | pages [35] -->
clog << "yes,change lane when i = " << i << " j = " << j << endl; #endif // output_lanes

<!-- b001123 | prose | pages [35] -->
} } else roadnew[change_lane][j].turning_light = 0; } } } }

<!-- b001124 | prose | pages [35] -->
Cars **tmp = roadold; roadold = roadnew; roadnew = tmp; }

<!-- b001125 | prose | pages [35] -->
#ifdef statistic_collect

<!-- b001126 | prose | pages [35] -->
out << cnt_car << "\t" << kindpossibility << "\t" << timer_all / cnt_car << endl; clog << cnt_car << "\t" << kindpossibility << "\t" << timer_all / cnt_car << endl; delete[]tempremain; } } }

<!-- b001127 | prose | pages [35] -->
out.close();

<!-- b001128 | prose | pages [35] -->
for (int i = 0; i < lane_num; ++i) {

<!-- b001129 | prose | pages [35] -->
delete[]roadold[i]; delete[]roadnew[i]; } delete[]roadold; delete[]roadnew; } #endif //statistic_collect

<!-- b001130 | prose | pages [35] -->
#ifdef output_lanes

<!-- b001131 | furniture | pages [36] -->
Team # 55585

<!-- b001132 | furniture | pages [36] -->
Page 34 of 34

<!-- b001133 | prose | pages [36] -->
for (int i = 0; i < lane_num; ++i) {

<!-- b001134 | prose | pages [36] -->
delete[]roadold[i]; delete[]roadnew[i]; }

<!-- b001135 | prose | pages [36] -->
delete[]roadold; delete[]roadnew; #endif // output_lanes

<!-- b001136 | prose | pages [36] -->
system("pause"); crash.close();

<!-- b001137 | prose | pages [36] -->
return 0; }
